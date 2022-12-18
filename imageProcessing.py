import cv2
import numpy as np
from myThresholding import algorithm1
import time


def processImg(filename):
    img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)  # load image

    T = int(algorithm1(img))  # calculate threshold value
    imgT2 = [[255 if pix > T else 0 for pix in row] for row in img]  # threshold image
    imgT2 = np.array(imgT2, dtype=np.uint8)  # convert list to 8-bit array

    cv2.imshow("raw image", img)  # show raw image
    cv2.imshow("processed image", imgT2)  # show processed image


if __name__ == '__main__':

    filenames = ("example1.jpg", "example2.jpg", "example3.jpg")

    for filename in filenames:
        start_time = time.time()
        processImg(filename)
        print("--- %s seconds ---" % (time.time() - start_time))
        cv2.waitKey(0)                                   # wait for any key