import cv2


class RectMarker(object):

    @staticmethod
    def markRect(contours, image):
        for contour in contours:
            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 3)

        return image
