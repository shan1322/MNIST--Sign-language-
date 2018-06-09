import cv2
from keras.models import model_from_json
from matplotlib.pyplot import imshow
import matplotlib.pyplot as plt
import numpy as np
import time
cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)
if vc.isOpened():
    rval, frame = vc.read()
else:
    rval = False
while rval:
    cv2.imshow("preview", frame)
    rval, frame = vc.read()
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break
cv2.destroyWindow("preview")
