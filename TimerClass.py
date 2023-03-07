import time # Import the timekeeping library
import keyboard
# Initialize global variables
runstat = False
class TimerClass:
    def __init__(self, func, rate):
        self.func = func
        self.rate = rate
        self.interval = 1.0/self.rate
        self.last_time = time.time()

    def run(self):
        while runstat:
            now = time.time()
            elapsed = now-self.last_time
            if elapsed >= self.interval:
                self.func()
                self.last_time = now
            else:
                time.sleep(self.interval-elapsed)
            if keyboard.is_pressed("enter"):
                print("Timer Ended\n")
                break
