#this script should contain a function that can take a file name as a paramter and perform some kind of thresholding on it

#import neccessary modules
import cv2
import numpy as np

def perform_threshold(filename):
    #first have to read in the image which will be passed on from the higher up script
    img = cv2.imread(filename)
    #here 60 is the min val and 255 is the max val
    #here running most simple thresholding for debugging purposes
    retval, threshold = cv2.threshold(img, 60, 255, cv2.THRESH_BINARY)
    #get old filename
    new_name = str(filename)
    old_filename = new_name.rsplit('/',1)[1]
    old_filename = old_filename[:old_filename.index(".JPG")]
    new_name = old_filename + "_threshold" + ".JPG"
    cv2.imwrite(new_name,threshold)