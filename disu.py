#coding=utf8

import autopy
import time
import threading

# print autopy.bitmap.capture_screen().height
# print autopy.bitmap.capture_screen().width
# # autopy.mouse.smooth_move(100, 100)
# print hex(autopy.bitmap.capture_screen().get_color(100, 100))
# print autopy.bitmap.capture_screen().get_color(100, 100)
# print autopy.color.hex_to_rgb(autopy.bitmap.capture_screen().get_color(12, 10))

# print autopy.bitmap.Bitmap.open('screengrab.png').to_string()

monkey1 = autopy.bitmap.Bitmap.open('1.png')
monkey2 = autopy.bitmap.Bitmap.open('2.png')
monkey  = autopy.bitmap.Bitmap.open('3.png')
monkey3 = autopy.bitmap.Bitmap.open('4.png')
monkey4 = autopy.bitmap.Bitmap.open('5.png')
monkey5 = autopy.bitmap.Bitmap.open('6.png')
monkey6 = autopy.bitmap.Bitmap.open('7.png')
monkey7 = autopy.bitmap.Bitmap.open('8.png')
monkey8 = autopy.bitmap.Bitmap.open('9.png')
monkey9 = autopy.bitmap.Bitmap.open('10.png')
# monkey = autopy.bitmap.Bitmap.open('3.png')


#  寻找地鼠。告诉我你找到它了吗？
def find(b, m):
    pos = b.find_bitmap(m)
    if pos:
        autopy.mouse.move(pos[0] + 10, pos[1] + 10)
        # time.sleep(2)
        autopy.mouse.toggle(True)
        autopy.mouse.toggle(False)
        autopy.mouse.move(pos[0] + 70, pos[1] + 10)
        print "我们找到了他！他在这里: %s" % str(pos)


def where_is_the_monkey(monkeys,monkeys3,monkeys4,monkeys5,monkeys6,monkeys7,monkeys8,monkeys9,monkeys1,monkeys2):
    # autopy.bitmap.capture_screen()
    while 1:
        # autopy.bitmap.capture_screen().save("screengrab.png")
        barrel = autopy.bitmap.capture_screen()
        # time.sleep(1)
        find(barrel, monkeys)
        find(barrel, monkeys3)
        find(barrel, monkeys4)
        find(barrel, monkeys5)
        find(barrel, monkeys6)
        find(barrel, monkeys7)
        find(barrel, monkeys8)
        find(barrel, monkeys9)
        find(barrel, monkeys1)
        find(barrel, monkeys2)


where_is_the_monkey(monkey,monkey3,monkey4,monkey5,monkey6,monkey7,monkey8,monkey9,monkey1,monkey2)
    #
    # freed = []
    # for i in range(10):
    #     freed.append(threading.Thread(target=where_is_the_monkey,args=(monkey,)))
    # for s in freed:
    #     s.start()
