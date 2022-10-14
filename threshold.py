import cv2
import numpy as np


image = cv2.imread("mandrill.jpg", 1)

cv2.imwrite("threshold.jpg", image)