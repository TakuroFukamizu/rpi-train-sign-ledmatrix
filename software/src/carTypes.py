from collections import namedtuple

CarType = namedtuple('CarType' , ['id', 'jp', 'en'])

car_types = [
    CarType('local', '各駅停車', 'LOCAL'),
    CarType('local2', '普通', 'LOCAL'),
    CarType('rapid', '快速', 'RAPID'),
    CarType('cr', '通勤快速', 'COMMUTER RAPID'),
    CarType('sr', '特別快速', 'SPECIAL RAPID'),
    CarType('csr', '中央特快', 'CHUO SPECIAL RAPID'),
    CarType('osr', '青梅特快', 'OME SPECIAL RAPID'),
    CarType('csr', '通勤特快', 'COMMUTER SPECIAL RAPID'),
    CarType('blank', '', '')
]

		# ["ライナー",	""],
		# ["急行",	""],
		# ["特急",	""],
		# ["L特急",	""],
		# ["寝台急行",	""],
		# ["寝台特急",	""],
		# ["回送",	""],
		# ["臨時",	""],
		# ["団体",	""],
