import multiprocessing as mp
from AlgoRunner import AlgoRunner
from Poison import Poison

class DiffProcessor(mp.Process):
    maxFrameWindowSize = 4

    def __init__(self, diffPipeCon, markedPipeCon):
        super(mp.Process, self).__init__()
        self.diffPipeCon = diffPipeCon
        self.markedPipeCon = markedPipeCon

    def run(self):
        frameWindow = []
        while True:
            msg = self.diffPipeCon.recv()
            if Poison.isPoisonMsg(msg):
                self.markedPipeCon.send(msg)
                break

            frame = msg
            frameWindow.append(frame)
            prevImage = frameWindow[0]
            currImage = frameWindow[len(frameWindow) - 1]
            markedImage = AlgoRunner.markMotion(prevImage, currImage)
            self.markedPipeCon.send(markedImage)
            if len(frameWindow) > self.maxFrameWindowSize:
                frameWindow.pop(0)


