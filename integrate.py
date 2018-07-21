import cv2
from keras.models import model_from_json
from matplotlib.pyplot import imshow
import matplotlib.pyplot as plt
import numpy as np
import time
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights("model.h5")
cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)
if vc.isOpened():
    rval, frame = vc.read()
else:
    rval = False
while rval:
    cv2.imshow("preview", frame)
    rval, frame = vc.read()
    image=cv2.resize(frame,(28,28))
    print(loaded_model.predict(np.expand_dims(np.array(image),axis=0)))
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break
cv2.destroyWindow("preview")
