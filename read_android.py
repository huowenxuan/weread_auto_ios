import uiautomator2 as u2
import time
import random
import sys

ip = ''

# 获取参数，作为ip
argv = sys.argv
if len(argv) > 1:
    ip = argv[1]

# 有ip则是通过wifi连接，否则通过usb adb连接
# 先尝试wifi连接
try:
    d = u2.connect(ip)
except:
    d = u2.connect()
info = d.info
print(info)  # 1920 * 1080

screen_height = info.get('displayHeight')
screen_width = info.get('displayWidth')

def print_click(sx, sy, ex, ey, second):
    print(str(round(second, 2)) + '秒后拖拽(' + str(round(sx, 2)) + ', ' + str(round(sy, 2)) + '), 到(' + str(
        round(ex, 2)) + ',' + str(round(ey, 2)) + ')')

count = 0
while 1:
    print('已运行'+str(count)+'秒')
    if count > 60*18:
        exit()
    sx = random.uniform(screen_width * 2 / 3, screen_width - 100)
    sy = random.uniform(50, screen_height - 100)
    ex = random.uniform(20, screen_width / 3)
    ey = random.uniform(sy - 200, sy + 200)
    second = random.uniform(12, 30)
    count += second
    print_click(sx, sy, ex, ey, second)
    time.sleep(second)
    steps = random.uniform(0.1, 0.3)
    d.swipe(sx, sy, ex, ey, steps)
