import cv2
import imutils
from ContourFinder import ContourFinder
from RectMarker import RectMarker


class AlgoRunner:

    @staticmethod
    def converToGrey(image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)
        return gray

    @staticmethod
    def prepareImage(image):
         image = imutils.resize(image, width=500)
         return AlgoRunner.converToGrey(image)

    @staticmethod
    def diff(prevImage, currImage):
        return cv2.absdiff(prevImage, currImage)

    @staticmethod
    def markMotion(prevImage, currImage):
        prevImage = AlgoRunner.prepareImage(prevImage)
        currImage = AlgoRunner.prepareImage(currImage)
        diffImage = AlgoRunner.diff(prevImage, currImage)
        contours = ContourFinder.findCountours(diffImage)
        return RectMarker.markRect(contours, currImage)
