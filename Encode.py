import numpy as np
import scipy.misc as sp
import sys

#Define image path here
path = sys.argv[1]

#Load Image
image= sp.imread(path, flatten= 1)

#Vectorize the image to a 1-D array
image_vect = image.ravel()

#Load the start sequence
start_seq = np.loadtxt(sys.argv[2])
#Load the stop sequence
stop_seq = np.loadtxt(sys.argv[3])

#Append the start and stop sequence to the data
#'START' at the start'''
with_start = np.insert(image_vect,0,start_seq)
#'STOP' at the end
with_start_stop = np.append(with_start,stop_seq)

#Save the above as a binary dump file for GRC processing
with_start_stop.tofile('INPUT_dump',sep = "",format = "%uint8")

