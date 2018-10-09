#this is a trial script to be able to iterate through files in a particualr directory

import os
from threshold_function import perform_threshold

#first get the current working directory
current_directory = os.getcwd()

#set up a loop to iterate through the current directory
for filename in os.listdir(current_directory):
    #if file is a picture
    if filename.endswith(".JPG"):
        #print full path of current file
        #what we actually want to do here is if we have a picture perform thresholding and save the image
        path_to_file = (os.path.join(current_directory, filename))
        #ideally here we will call another script that has a function that can take the path_to_file as a variable and execute a function
        perform_threshold(path_to_file)
        #seems to be staying in same directory which is great
        print('current directory' + os.getcwd())
