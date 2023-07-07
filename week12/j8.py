import time
import sys
from curses import wrapper

def put(x, y, c):
    global scr
    scr.addstr(19-y, x, c)
def sleep(n):
    time.sleep(n)
def display():
    global scr
    scr.refresh()
def keyread():
    global scr
    scr.getkey()
def clear():
    global scr
    scr.clear()
##########################################
class Slant():
    def __init__(self, x, y, le, ch):
        if x < 0 or x > 59  :
            put(0, 0, "Error: x is out of range")
            display()
            sys.exit(1)
        if y < 0 or y > 19 :
            put(0, 0, "Error: y is out of range")
            display()
            sys.exit(1)
        if y + le > 20 or x + le > 60:
            put(0, 0, "Error: line is out of range");
            display()
            sys.exit(1)
        self.sx = x
        self.sy = y
        self.le = le
        self.ch = ch[0]
    def puts(self):
        for le in range(self.sy,self.le+self.sy):
            put(self.sx+le,le,self.ch)
    def erase(self):
        a=Slant(self.sx,self.sy,self.le," ")
        a.puts()
    def rshift(self):
        if(59>self.sx+self.le-1):
            self.erase()
            self.sx+=1
        self.puts()
            
    def lshift(self):
        if(0<self.sx):
            self.erase()
            self.sx-=1
        self.puts()
    def ushift(self):
        if(19>self.sy+self.le-1):
            self.erase()
            self.sy+=1
        self.puts()
    def dshift(self):
        if(0<self.sy):
            self.erase()
            self.sy-=1
        self.puts()

def main(stdscr):
    global scr
    scr = stdscr
    clear()

    t = Slant(30, 0, 20, "*")
    for i in range(20):
        t.rshift()
        display()
        sleep(0.1)
        t.erase()
    for i in range(10):
        t.lshift()
        display()
        sleep(0.1)
        t.erase()
    for i in range(10):
        t.puts()
        display()
        sleep(0.2)
        t.erase()
        display()
        sleep(0.1)
    clear()
    t2 = Slant(5, 0, 10, '#');
    t2.puts()
    display()
    sleep(0.1)

    for i in range(25):
        t2.erase()
        t2.ushift()
        display()
        sleep(0.1)
    for i in range(30):
        t2.erase()
        t2.dshift()
        display()
        sleep(0.05)
    for i in range(10):
        t2.erase()
        display()
        sleep(0.2)
        t2.puts()
        display()
        sleep(0.1)

    keyread()

wrapper(main)

