""" Read an authN graph (adjacency list), list hubs, and plot one of them.
"""
from __future__ import print_function
import networkx as nx
from operator import itemgetter
from networkx.algorithms import bipartite
import matplotlib.pyplot as plt
import copy
import sys


if ((int(sys.version[0]) == 0) and (int(sys.version[2]) < 6)):
  print("Warning: Python version < 2.6 will cause print stmt to fail")

def draw_graph(G):
    pos=nx.spring_layout(G) # positions for all nodes
    cnodes,unodes = bipartite.sets(G)

    nx.draw_networkx_nodes(G,pos,nodelist=cnodes,node_color='r')
    nx.draw_networkx_nodes(G,pos,nodelist=unodes,node_color='w')
#    nx.draw_networkx_edges(G,pos)

    pos2 = copy.deepcopy(pos)
    for d in pos:
        pos2[d][1] = pos[d][1] - 0.02
    nx.draw_networkx_labels(G,pos2)

    plt.axis('off')
    plt.show()

graph_filename = 'auth_graph_adjlist.dat'
G = nx.read_adjlist(graph_filename)

num = 0
maxHubs = 160
# dump hubs (with subtraction!)
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

# get hub as a subgraph
G = nx.read_adjlist(graph_filename)
hub = 'U8804'
hub = 'U6677'
hub_nodes = G.neighbors(hub)
print(str(len(hub_nodes)) + 'nodes')
hub_nodes.append('U6677')
sg = G.subgraph(hub_nodes)
draw_graph(sg)
