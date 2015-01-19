"""Display a histogram for the time events associated with a (binary) file.
"""
import numpy as np
import matplotlib.pyplot as plt

# read in entire file of time events (32-bit binary; units in seconds)
filename = 'time_secs_binary_f32.dat'
timevals = np.fromfile(filename, dtype=np.float32, count=-1)

# setup for matplotlib plotting window
fig = plt.figure()
ax = fig.add_subplot(111)

nbins = 10000   # number of bins for histogram
ax.hist(timevals/3600, nbins, facecolor='black')  # histogram: time in hours(secs/3600)

ax.set_title('authN event histogram: '+str(nbins)+' bins')
ax.set_xlabel('time(hrs)')
ax.set_ylabel('count')
plt.show()
