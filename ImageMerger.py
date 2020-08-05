import imutils
import numpy as np


class ImageMerger:
    @staticmethod
    def merge(gray, rgb):
        gray = imutils.resize(gray, width=rgb.shape[1])
        rowsRgb, colsRgb, channels = rgb.shape
        rowsGray = gray.shape[0]
        colsGray = gray.shape[1]
        rowsMerged = max(rowsRgb, rowsGray)
        colsMerged = colsRgb + colsGray
        mergedImage = np.zeros(shape=(rowsMerged, colsMerged, channels), dtype=np.uint8)
        mergedImage[:rowsRgb, :colsRgb] = rgb
        mergedImage[:rowsGray, colsRgb:] = gray[:, :, None]
        return mergedImage

