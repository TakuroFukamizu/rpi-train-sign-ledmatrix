from jsonc_parser.parser import JsoncParser
from datetime import datetime

class TimelineUsecase:

    def __init__(self) -> None:
        self.data = None

    def load(self, filepath: str) -> None:
        # 時刻表データ取得
        self.data = JsoncParser.parse_file(filepath)

    def get_nearlest_trais(self, station: str, direction: str, now: datetime, weekday: bool) -> list:
        # 現在時刻以降で最も速く来る電車を取得する

        timetable = self.data[station][direction]['weekday' if weekday else 'holiday']
        
        key_1st = 9999
        key_2nd = 9999
        value_1st = None
        value_2nd = None
        for row in timetable:
            print(row)
            time_value = row["time"].split(':')
            h = int(time_value[0])
            m = int(time_value[1])
            if h == 0:
                h == 24
            if h < now.hour:
                continue
            if m < now.minute:
                continue
            
            key = h * 100 + m

            if key < key_1st and key < key_2nd:
                key_2nd = key_1st
                value_2nd = value_1st
                key_1st = key
                value_1st = row
            elif key < key_2nd:
                key_2nd = key
                value_2nd = row
            else:
                continue
        results = []
        if value_1st != None:
            results.append(value_1st)
        if value_2nd != None:
            results.append(value_2nd)
        return results