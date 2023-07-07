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
class Tateline():
    def __init__(self, x, y, le, ch):
        if x < 0 or x > 59  :
            put(0, 0, "Error: x is out of range")
            display()
            sys.exit(1)
        if y < 0 or y > 19 :
            put(0, 0, "Error: y is out of range")
            display()
            sys.exit(1)
        if y + le > 20:
            put(0, 0, "Error: line is out of range");
            display()
            sys.exit(1)
        #if len(ch) != 1:
            #print("character length must be 1");
        self.sx = x
        self.sy = y
        self.le = le
        self.ch = ch[0]
    def puts(self):
        for le in range(self.sy,self.le+self.sy):
            put(self.sx,le,self.ch)
    def erase(self):
        a=Tateline(self.sx,self.sy,self.le," ")
        a.puts()
    def rshift(self):
        if(59>self.sx):
            self.erase()
            self.sx+=1
        self.puts()
            
    def lshift(self):
        if(0<self.sx):
            self.erase()
            self.sx-=1
        self.puts()
class Yokoline():
    def __init__(self, x, y, le, ch):
        if x < 0 or x > 59  :
            put(0, 0, "Error: x is out of range")
            display()
            sys.exit(1)
        if y < 0 or y > 19 :
            put(0, 0, "Error: y is out of range")
            display()
            sys.exit(1)
        if x + le > 60:
            put(0, 0, "Error: line is out of range");
            display()
            sys.exit(1)
        self.sx = x
        self.sy = y
        self.le = le
        self.ch = ch[0]
    def puts(self):
        for le in range(self.sx,self.le+self.sx):
            put(le,self.sy,self.ch)
    def erase(self):
        a=Yokoline(self.sx,self.sy,self.le," ")
        a.puts()
def main(stdscr):
    global scr
    scr = stdscr
    clear()

    t = Tateline(50, 0, 20, "*")
    t.puts()
    display()
    sleep(0.1)
    for i  in range(20):
        t.erase()
        t.rshift()
        display()
        sleep(0.1)
    for i  in range(20):
        t.erase()
        t.lshift()
        display()
        sleep(0.1)
    t.erase()
    t2 = Tateline(10, 0, 20, "*")
    t2.puts()
    display()
    sleep(0.1)
    for i  in range(20):
        t2.erase()
        t2.lshift()
        display()
        sleep(0.1)
    for i  in range(20):
        t2.erase()
        t2.rshift()
        display()
        sleep(0.1)


    keyread()

wrapper(main)

