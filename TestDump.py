import pygame as pg
import TimerClass
pg.init()
#window = pg.display.set_mode((0,0),pg.FULLSCREEN)
#window = pg.display.set_mode()
#x = window.get_size()
window = pg.display
x = window.get_desktop_sizes()
print(x[0][0], x[0][1])
#pg.quit()
# if pg.event.get()==pg.QUIT:
#     print("Hi !")
# window.fill((255,255,255))
# pg.draw.circle(window,(255,0,0),(x[0]*0.5,x[1]*0.5),25,3)
# pg.display.flip()
# window.fill((255,255,255))
# pg.draw.circle(window,(0,150,0),(x[0]*0.5,x[1]*0.75),25,3)
# pg.display.flip()
# t = TimerClass.TimerClass(pg.display.flip, 200, "enter")
# t.run()
# pg.quit()
