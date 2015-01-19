""" Read an authN graph (adjacency list) and print out hubs (descending by degree count)
"""
from __future__ import print_function
import networkx as nx
from operator import itemgetter
import sys

if ((int(sys.version[0]) == 0) and (int(sys.version[2]) < 6)):
  print("Warning: Python version < 2.6 will cause print stmt to fail")

graph_filename = 'auth_graph_adjlist.dat'
G = nx.read_adjlist(graph_filename)

num = 0
maxHubs = 20
while num < maxHubs:
  node,deg=max(G.degree_iter(),key=itemgetter(1)) # get node of max degree
  if node[0] == 'U':   # 'U'=users; 'C'=computers
    print(node, str(deg),end=', ')
    G.remove_node(node)
    num += 1
    if ((num % 5)==0):
      print()
  else:
    G.remove_node(node)

print()
