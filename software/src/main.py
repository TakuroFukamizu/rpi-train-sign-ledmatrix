import sys
import time
from datetime import datetime, timezone, timedelta
from collections import namedtuple
# from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image, ImageDraw, ImageFont, ImageOps
from usecase.timeline import TimelineUsecase

fonts = {
    'jiskan16': ImageFont.truetype('./fonts/JF-Dot-jiskan16.ttf', 16),
    'msgothic': ImageFont.truetype('./fonts/msgothic.ttc', 16)
}

JST = timezone(timedelta(hours=9), 'JST')

def init_image():
    # Initialize image
    # 160(32*5)x32: 種別名3桁, 行先4桁, 時刻3桁

    image = Image.new('RGB',(128,32),(0,0,0))
    draw = ImageDraw.Draw(image)
    # clock = datetime.now().strftime('%H:%M')
    # draw.text((0,0), clock, (255,128,25), font=font)
    return image, draw

def main():
    # try:
    #     # matrix = get_matrix()

    #     print("Press CTRL-C to stop.")
    #     while True:
    #         image = drwa_image()
    #         # matrix.SetImage(image.convert('RGB'))
    #         time.sleep(2)

    # except KeyboardInterrupt:
    #     sys.exit(0)

    # test

    # 時刻表データ取得
    timelineUsecase = TimelineUsecase()
    timelineUsecase.load('./timeline.jsonc')

    now = datetime.now(JST) # 現在時刻取得
    print(now.hour)
    print(now.minute)

    # 現在時刻以降で最も速く来る電車
    values = timelineUsecase.get_nearlest_trais('jb20', 'west', now, True)
    print(values)
    
    # LED表示内容の描画
    image = draw_timetable(values)

    # image = drwa_image()

    img = image.convert('RGB')
    img.save('output.png')

def draw_distination(draw: ImageDraw, line: int, value: str):
    text_len = len(value)
    font = fonts['jiskan16']
    color = (255,128,25)
    y = 0 if line == 0 else 16 
    if text_len == 3:
        padding = 8
        font_size = 16
        draw.text((padding, y), value[0], color, font=font)
        draw.text((padding*2 + font_size, y), value[1], color, font=font)
        draw.text((padding*3 + font_size*2, y), value[2], color, font=font)
    elif text_len == 2:
        padding = 16
        font_size = 16
        draw.text((padding,y), value[0], color, font=font)
        draw.text((padding+font_size*2,y), value[1], color, font=font)
    else:
        draw.text((0,y), value, color, font=font)

def draw_time(draw: ImageDraw, line: int, value: str):
    text_len = len(value)
    font = fonts['msgothic']
    color = (127,249,50)
    y = 0 if line == 0 else 16 
    draw.text((80,y), value, color, font=font)

def draw_timetable(values: list) -> Image:
    image, draw = init_image()
    
    for i in range(0, len(values)):
        draw_distination(draw, i, values[i]['destination'])
        draw_time(draw, i, values[i]['time'])

    return image


def drwa_image():
    image, draw = init_image()

    text = '中野'
    draw_distination(draw, 1, text)
    text = '10:02'
    draw_time(draw, 1, text)

    text = '津田沼'
    draw_distination(draw, 2, text)
    text = '10:02'
    draw_time(draw, 2, text)

    return image

# def get_matrix():
#     # Configuration for the matrix
#     options = RGBMatrixOptions()
#     options.rows = 32
#     options.cols = 64
#     options.chain_length = 1
#     options.parallel = 1
#     options.hardware_mapping = 'regular'

#     options.gpio_slowdown = 5
#     options.limit_refresh_rate_hz = 120
#     # options.show_refresh_rate = 1
#     options.brightness = 50
#     options.disable_hardware_pulsing = True

#     return RGBMatrix(options = options)


if __name__ == '__main__':
    main()