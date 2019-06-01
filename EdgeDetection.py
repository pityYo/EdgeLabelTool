from __future__ import print_function
import cv2 as cv
import argparse
import os
import numpy as np

def draw_circle(event, x, y, flags, param):
	if event == cv.EVENT_LBUTTONDOWN or \
	flags == cv.EVENT_FLAG_LBUTTON:
		#print("yes")
		global mask2
		#print(src_gray.dtype)
		cv.circle(mask2, (x, y), 8, 0 , -1)
		#cv.circle(src_gray, (x, y), 10, 255 , 1)
		#src_gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
		CannyThreshold(BarVal)


max_lowThreshold = 100
window_name = 'Edge Map'
title_trackbar = 'Min Threshold:'
ratio = 3
kernel_size = 3 # 3
def CannyThreshold(val):
    global BarVal
    global mask2
    BarVal = val
    low_threshold = val
    #print("low_threshold = ", low_threshold)
    img_blur = cv.blur(src_gray, (3,3))
    detected_edges = cv.Canny(img_blur, low_threshold, low_threshold*ratio, kernel_size)
    mask = detected_edges != 0
    mask = mask * mask2 # manual mask
    dst = src * (mask[:,:,None].astype(src.dtype))
    cv.imshow(window_name, dst)


parser = argparse.ArgumentParser(description='Code for Canny Edge Detector tutorial.')
parser.add_argument('--file', help='Path to input image.', default='./FLIR')
args = parser.parse_args()

files = os.listdir(args.file)
# print("file\n", file)

Quit_flag = False
for file_name in files:

    window_name = file_name
    src_name = args.file + "/" + file_name
    src = cv.imread(cv.samples.findFile(src_name))

    if src is None:
        print('Could not open or find the image: ', src_name)
        exit(0)
    # additional
    # resize
    #print (src.shape)
    src = cv.resize(src, (800, 600), interpolation=cv.INTER_LINEAR) 
    
    BarVal = 0 # maintain trackbar value
    mask2 = np.ones((600, 800), dtype=np.uint8) # mask for draw
   

    src_gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    cv.namedWindow(window_name, flags=cv.WINDOW_NORMAL)
    # set mouse
    cv.setMouseCallback(window_name, draw_circle)

    cv.createTrackbar(title_trackbar, window_name , 0, max_lowThreshold, CannyThreshold)
    CannyThreshold(0)

    while(1):
        key = cv.waitKey(5)
        if key == ord('q'):
            Quit_flag = True
            break
        elif key == ord('n'):
            break
        elif key == ord('c'):
           # global mask2
            mask2 = np.ones((600, 800), dtype=np.uint8)
            CannyThreshold(BarVal)


    cv.destroyWindow(window_name)
    if Quit_flag == True:
        break