from threading import Thread
from time import sleep


class TimeError(Exception):
    pass


class Animation(Thread):
    def __init__(self, text="Animation", timeToSleep=0.2, dot=4, internet=False):
        super().__init__()
        if timeToSleep >= 1:
            raise TimeError("Time must be smaller than 1 second")

        self.timeToSleep = timeToSleep
        self.maxNumOfDot = dot
        self.text = text
        self.loopTime = round(1 / timeToSleep)
        self.Running = True
        self.internet = internet

    def run(self):
        dotNum = 1
        totalTime, loopRun, barComplete = 1, 0, 0

        while self.Running:
            print(f"[{totalTime}s] {self.text} {'.' * dotNum}", flush=True)
            print("\033[F", end="\033[K")

            if dotNum == self.maxNumOfDot:
                dotNum = 0
                barComplete += 0.5

            if loopRun == self.loopTime:
                loopRun = 0
                totalTime += 1

            dotNum += 1
            loopRun += 1

            sleep(self.timeToSleep + (barComplete * 0.1 if self.internet else 0))

    def stop(self):
        self.Running = False
