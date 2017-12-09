import numpy as np
import scipy as sp
import scipy.misc
import matplotlib.pyplot as plt
import sys

#read output dump from gnuradio
temp = np.fromfile(sys.argv[1])

#Load the start sequence
start_seq = np.loadtxt(sys.argv[2])
#Load the stop sequence
stop_seq = np.loadtxt(sys.argv[3])

#rolling window function to get subarrays of given size from array 'a'
def rolling_window(a, size):
    shape = a.shape[:-1] + (a.shape[-1] - size + 1, size)
    strides = a.strides + (a.strides[-1],)
    return np.lib.stride_tricks.as_strided(a, shape=shape, strides=strides)

#get an array which indicates locations where the start sequence is found and get those array indices
bool_indices = np.all(rolling_window(temp, 100) == start_seq, axis=1)
start_index = np.mgrid[0:len(bool_indices)][bool_indices] + 100

#get an array which indicates locations where the stop sequence is found and get those array indices
bool_indices = np.all(rolling_window(temp, 100) == stop_seq, axis=1)
stop_index = np.mgrid[0:len(bool_indices)][bool_indices]

#extract the image array and reshape it into given dimensions
temp1=temp[start_index[0]:stop_index[0]]
temp1 = temp1.reshape((int(sys.argv[4]),int(sys.argv[5])))

#create the given image
plt.figure(1)
plt.gray()
plt.imshow(temp1)
plt.savefig("out.png")
