import cv2
import multiprocessing as mp
import sys
from Poison import Poison
from DiffProcessor import DiffProcessor
from DisplayProcessor import DisplayProcessor


class Main(object):

    def __init__(self, videoFilename):
        self.videoFilename = videoFilename
        self.vidCap = cv2.VideoCapture(self.videoFilename);
        self.vidLen = int(self.vidCap.get(cv2.CAP_PROP_FRAME_COUNT))
        self.diffPipe = mp.Pipe()
        self.markedPipe = mp.Pipe()
        self.rgbPipe = mp.Pipe()
        self.diffPipeSendCon = self.diffPipe[0]
        self.diffPipeRcvCon = self.diffPipe[1]
        self.rgbPipeSendCon = self.rgbPipe[0]
        self.rgbPipeRcvCon = self.rgbPipe[1]
        self.markedPipeSendCon = self.markedPipe[0]
        self.markedPipeRcvCon = self.markedPipe[1]
        self.displayProcessor = DisplayProcessor(self.rgbPipeRcvCon, self.markedPipeRcvCon)
        self.diffProcessor = DiffProcessor(self.diffPipeRcvCon, self.markedPipeSendCon)

    def terminate(self):
        self.vidCap.release()
        self.diffPipeSendCon.send(Poison.poisonMsg)
        self.diffProcessor.join()
        self.rgbPipeSendCon.send(Poison.poisonMsg)
        self.displayProcessor.join()

    def run(self):
        self.displayProcessor.start()
        self.diffProcessor.start()
        for _ in range(self.vidLen):
            success, frame = self.vidCap.read()
            if success:
                self.rgbPipeSendCon.send(frame)
                self.diffPipeSendCon.send(frame)

        self.terminate()



if len(sys.argv) != 2:
    print("wrong number of command line arguments !!! need video file path ...")

videoFilename = sys.argv[1]
programMMain = Main(videoFilename)
programMMain.run()
