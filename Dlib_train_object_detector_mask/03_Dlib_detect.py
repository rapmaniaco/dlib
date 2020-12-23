#python 03_Dlib_detect.py

import cv2
import dlib


detector = dlib.simple_object_detector("mask.svm")

frame = cv2.imread('/home/edee/EdeE/Processamento_Imagem/Dlib/Dlib_03_ObjectDetection_Train_HOG/dataset/test/005.jpg')

detections = detector(frame)
if len(detections) > 0:
	print(" Number of Diesels detected: {}".format(len(detections)))
	for k, d in enumerate(detections):
		print("Diesel {}: Left: {} Top: {} Right: {} Bottom: {}".format(
		k, d.left(), d.top(), d.right(), d.bottom()))
		cv2.rectangle(frame, (d.left(), d.top()), (d.right(), d.bottom()), (0, 0, 255), 2)
cv2.imshow("raw", frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
