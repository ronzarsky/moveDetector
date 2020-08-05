import cv2
import imutils


class ContourFinder:

    @staticmethod
    def findCountours(diffImage):
        threshFrame = cv2.threshold(diffImage, 30, 255, cv2.THRESH_BINARY)[1]
        threshFrame = cv2.dilate(threshFrame, None, iterations=2)
        thresh = cv2.dilate(threshFrame, None, iterations=2)
        contours = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours = imutils.grab_contours(contours)
        return [contour for contour in contours if cv2.contourArea(contour) > 50]