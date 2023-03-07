import pygame as pg
import TimerClass


class CGame:
    def __init__(self, icrad, ocrad):
        pg.init()
        self.window = pg.display.set_mode((100, 100), pg.RESIZABLE, 0, 0)
        self.winsize = self.window.get_size()
        self.origin = (self.winsize[0] * 0.5, self.winsize[1] * 0.5)
        self.ocpos = self.origin
        self.icpos = self.origin
        self.occolor = (0, 0, 255)
        self.iccolor = (255, 0, 0)
        self.bgcolor = (255, 255, 255)
        self.ocrad = ocrad
        self.icrad = icrad
        self.runstat = True
        self.timer = TimerClass.TimerClass(self, 200)

    def resize(self, new_icrad, new_ocrad):
        self.icrad = new_icrad
        self.ocrad = new_ocrad

    def get_pos(self):
        if self.winsize != self.window.get_size():
            self.winsize = self.window.get_size()
            self.origin = (self.winsize[0] * 0.5, self.winsize[1] * 0.5)
            self.ocpos = self.origin
            self.icpos = self.origin

        if abs(self.ocpos[1]-self.icpos[1]) <= self.ocrad-self.icrad:
            self.iccolor = (0, 255, 0)
        else:
            self.iccolor = (255, 0, 0)

    def update(self):
        self.get_pos()
        self.window.fill(self.bgcolor)
        pg.draw.circle(self.window, self.occolor, self.ocpos, self.ocrad, 3)
        pg.draw.circle(self.window, self.iccolor, self.icpos, self.icrad, 0)
        pg.display.flip()

    def run(self):
        self.timer.run()
        print("Thanks for playing!")


gamer = CGame(25, 50)
gamer.run()
