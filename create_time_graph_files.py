"""Reads an authentication dataset and creates 2 files: time events, global graph
__author__= "Randy Heiland"
__email__ = "heiland@iu.edu"
"""
import pandas as pd
import networkx as nx

fname = 'lanl-auth-dataset-1'
csize=1000000

csize_m1 = csize-1
reader = pd.read_table(fname, chunksize=csize, header=None, iterator=True,  sep=',')

time_filename = 'time_secs_binary_f32.dat'
fd_time = open(time_filename,'w')

G = nx.Graph()
graph_filename = 'auth_graph_adjlist.dat'

loop=0
# read dataset in chunks
for df in reader:
  t = df.ix[:,0]
  t.astype(pd.np.float32).values.tofile(fd_time)

  # Get bipartite graph nodes (users, computers)
  unodes = df.ix[:,1]
  cnodes = df.ix[:,2]

  sec0 = df.ix[0,0]
  try:
    secs = df.ix[csize_m1,0] - sec0
  except:
    csize_m1 = len(df.ix.obj) - 1
    secs = df.ix[csize_m1,0] - sec0

  days = secs/86400.   # secs/day= 60*60*24

  start_time = sec0/86400.

  G.add_nodes_from(unodes,bipartite=0)
  G.add_nodes_from(cnodes,bipartite=1)
  e = [(unodes[idx],cnodes[idx]) for idx in range(len(unodes))]
  G.add_edges_from(e)

  print('{0:d}: start day= {1:.3f}; elapsed secs, days= {2:d}, {3:0.3f}; '.format(loop,start_time,secs,days), end=" " )
  loop += 1 
  print('# nodes,edges= {0:d}, {1:d}'.format(len(G.nodes()),len(G.edges()) ))


nx.write_adjlist(G,graph_filename)

print('time --> ' + time_filename)
print('graph--> ' + graph_filename)
