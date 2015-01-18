"""Read an authentication dataset and create a (binary, 32-bit) file of just time events
__author__= "Randy Heiland"
__email__ = "heiland@iu.edu"
"""
import pandas as pd

fname = 'lanl-auth-dataset-1'
csize=1000000

csize_m1 = csize-1
reader = pd.read_table(fname, chunksize=csize, header=None, iterator=True,  sep=',')

time_filename = 'time_secs_binary_f32.dat'
fd_time = open(time_filename,'w')

loop=0
# read dataset in chunks
for df in reader:
  t = df.ix[:,0]
  t.astype(pd.np.float32).values.tofile(fd_time)

  sec0 = df.ix[0,0]
  try:
    secs = df.ix[csize_m1,0] - sec0
  except:
    csize_m1 = len(df.ix.obj) - 1
    secs = df.ix[csize_m1,0] - sec0

  days = secs/86400.   # secs/day= 60*60*24
  start_time = sec0/86400.
  print('{0:d}: start day= {1:.3f}; elapsed secs, days= {2:d}, {3:0.3f}; '.format(loop,start_time,secs,days))
  loop += 1 


print('time --> ' + time_filename)
