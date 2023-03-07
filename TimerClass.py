import time, sys # Import the timekeeping library
import pygame as pg
from pygame.locals import *
class TimerClass:
    def __init__(self, obj, rate):
        self.obj = obj
        self.rate = rate
        self.interval = 1.0/self.rate
        self.last_time = time.time()

    def run(self):
        while True:
            now = time.time()
            elapsed = now-self.last_time
            for event in pg.event.get():
                if event.type == QUIT:
                    pg.quit()
                    sys.exit()
            if elapsed >= self.interval:
                self.obj.update()
                self.last_time = now
            else:
                time.sleep(self.interval-elapsed)

