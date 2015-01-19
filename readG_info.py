""" Read an authN graph (adjacency list) and print out basic info
"""
from __future__ import print_function
import networkx as nx
from networkx.algorithms import bipartite
import sys

if ((int(sys.version[0]) == 0) and (int(sys.version[2]) < 6)):
  print("Warning: Python version < 2.6 will cause print stmt to fail")

graph_filename = 'auth_graph_adjlist.dat'
G = nx.read_adjlist(graph_filename)

print('# nodes = '+str(len(G.nodes())))
cnodes,unodes = bipartite.sets(G)
print('  # users     = '+str(len(unodes)))
print('  # computers = '+str(len(cnodes)))
print('# edges = '+str(len(G.edges())))

