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

    # Split the image into BGR channels
    b, g, r = cv.split(img)

    img_adjusted = cv.subtract(g, cv.divide(b, 1.5))

    img_adjusted = adjust_contrast_brightness(img_adjusted, 3, 50)

    # # show all images
    # cv.namedWindow("Adjusted", cv.WINDOW_NORMAL)
    # cv.imshow("Adjusted", img_adjusted)
    # cv.waitKey(0)

    cv.destroyAllWindows()

    index = np.average(img_adjusted)
    print(path, index, sep=",", end="\n")
    print(path, index, sep=",", end="\n", file=outfile)
