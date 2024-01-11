import cv2 as cv
import numpy as np


def adjust_contrast_brightness(img, contrast: float = 1.0, brightness: int = 0):
    """
    Adjusts contrast and brightness of an uint8 image.
    contrast:   (0.0,  inf) with 1.0 leaving the contrast as is
    brightness: [-255, 255] with 0 leaving the brightness as is
    """
    brightness += int(round(255 * (1 - contrast) / 2))
    return cv.addWeighted(img, contrast, img, 0, brightness)


def get_algae(path, outfile):
    img = cv.imread(path)

    # diff between green and blue channels
    img = np.subtract(img[:, :, 1], img[:, :, 0])

    img = adjust_contrast_brightness(img, 1, -30)

    img = np.clip(img, 0, 100)

    index = np.average(img)
    print(path, index, sep=",", end="\n", file=outfile)
