import cv2
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox

def main():
	im = cv2.imread('Side_4+7.png')
	bbox, label, conf = cv.detect_common_objects(im)
	#output_image = draw_bbox(im, bbox, label, conf)
	#plt.imshow(output_image)
	#plt.show()
	print("_____Image 1_______")
	print('Number of cars in the image is '+ str(label.count('car')))
	print('Number of trucks in the image is '+ str(label.count('truck')))
	print('Number of buses in the image is '+ str(label.count('bus')))
	print('Number of motorcylcle in the image is '+ str(label.count('motorcylcle')))

	L = []
	m=label.count('car')+label.count('truck')+label.count('bus')+label.count('motorcylcle')
	L.append(m)

	im = cv2.imread('Side_4+2.png')
	bbox, label, conf = cv.detect_common_objects(im)
	#output_image = draw_bbox(im, bbox, label, conf)
	#plt.imshow(output_image)
	#plt.show()
	print("_____Image 2_______")
	print('Number of cars in the image is '+ str(label.count('car')))
	print('Number of trucks in the image is '+ str(label.count('truck')))
	print('Number of buses in the image is '+ str(label.count('bus')))
	print('Number of motorcylcle in the image is '+ str(label.count('motorcylcle')))

	n=label.count('car')+label.count('truck')+label.count('bus')+label.count('motorcylcle')
	L.append(n)

	im = cv2.imread('Side_4+6.png')
	bbox, label, conf = cv.detect_common_objects(im)
	#output_image = draw_bbox(im, bbox, label, conf)
	#plt.imshow(output_image)
	#plt.show()
	print("_____Image 3_______")
	print('Number of cars in the image is '+ str(label.count('car')))
	print('Number of trucks in the image is '+ str(label.count('truck')))
	print('Number of buses in the image is '+ str(label.count('bus')))
	print('Number of motorcylcle in the image is '+ str(label.count('motorcylcle')))

	o=label.count('car')+label.count('truck')+label.count('bus')+label.count('motorcylcle')
	L.append(o)

	im = cv2.imread('Side_4+8.png')
	bbox, label, conf = cv.detect_common_objects(im)
	#output_image = draw_bbox(im, bbox, label, conf)
	#plt.imshow(output_image)
	#plt.show()
	print("_____Image 4_______")
	print('Number of cars in the image is '+ str(label.count('car')))
	print('Number of trucks in the image is '+ str(label.count('truck')))
	print('Number of buses in the image is '+ str(label.count('bus')))
	print('Number of motorcylcle in the image is '+ str(label.count('motorcylcle')))

	p=label.count('car')+label.count('truck')+label.count('bus')+label.count('motorcylcle')
	L.append(p)


	print(L)
	return L

#List=main()