import multiprocessing as mp
import cv2
from Poison import Poison
from ImageMerger import ImageMerger


class DisplayProcessor(mp.Process):

    def __init__(self, rgbPipeCon, markedPipeCon):
        super(mp.Process, self).__init__()
        self.rgbPipeCon = rgbPipeCon
        self.markedPipeCon = markedPipeCon

    def run(self):
        while True:
            msg = self.rgbPipeCon.recv()
            if Poison.isPoisonMsg(msg):
                break

            rgb = msg
            rgbWidth = rgb.shape[1]
            rgbHeight = rgb.shape[0]
            gray = self.markedPipeCon.recv()
            if Poison.isPoisonMsg(gray):
                break

            mergedImage = ImageMerger.merge(gray, rgb)
            mergedImage = cv2.resize(mergedImage, (rgbWidth, rgbHeight))
            cv2.imshow('Motion Detected !!!', mergedImage)
            cv2.waitKey(1)

        cv2.destroyAllWindows()

