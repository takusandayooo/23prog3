import time
from curses import wrapper

def put(x, y, c):
    global scr
    scr.addstr(19-y, x, c)
def sleep(n):
    time.sleep(n)
def display():
    global scr
    scr.refresh()
def clear():
    global scr
    scr.clear()
def keyread():
    global scr
    scr.getkey()


def main(stdscr):
    global scr
    scr = stdscr

    clear()

    for x in range(0, 40):
        for y in range(0, 20):
            put(x, y, '*')
        sleep(0.1)
        display()
        for y in range(0, 20):
            put(x, y, ' ')

    display()
    sleep(1)
    clear()

    for y in range(19, -1, -1):
        for x in range(0, 40):
            put(x, y, '*')
        sleep(0.1)
        display()
        for x in range(0, 40):
            put(x, y, ' ')
    keyread()

wrapper(main)
