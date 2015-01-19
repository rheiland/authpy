""" Read an authN graph (adjacency list) and print out connected components
"""
from __future__ import print_function
import networkx as nx
import sys

if ((int(sys.version[0]) == 0) and (int(sys.version[2]) < 6)):
  print("Warning: Python version < 2.6 will cause print stmt to fail")

graph_filename = 'auth_graph_adjlist.dat'
G = nx.read_adjlist(graph_filename)

num_conn = 0
for c in nx.connected_components(G):
    print('{0:d}: {1:d}'.format(num_conn, len(c)))
    if len(c) == 3:
      print(c)       # print out all 3-node components
    elif len(c) > 3:
      print(c[0:19]) # print out (up to) first 20
    num_conn += 1
