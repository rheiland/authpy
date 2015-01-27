authpy
======

Python scripts to analyze an authentication dataset.

The authentication dataset from LANL ([http://csr.lanl.gov/data/auth/](http://csr.lanl.gov/data/auth/))
provides a valuable benchmark dataset for researchers in cybersecurity and/or graphs/networks.

We recommend using the [Anaconda Python 3](https://store.continuum.io/cshop/anaconda/) distribution.

## Getting Started

We begin by generating two files from the original dataset:

*  `time_secs_binary_f32.dat` - a binary file containing just the time (secs) data (32-bit values)
*  `auth_graph_adjlist.dat` - an ASCII file containing the global graph (as an adjacency list)
 
You have two choices for obtaining these two files. The script `create_time_graph_files.py` will
generate both of them. However, it took about 8 hours on a laptop. The other choice is to simply
download the graph file from [http://trustedci.org/data](http://trustedci.org/data) and generate
the other file using `create_time_file.py` (which takes just a few minutes).

## Sample scripts
```
$ ipython --matplotlib

Python 3.4.2 |Anaconda 2.1.0 
...
Using matplotlib backend: MacOSX

In [1]: %run create_time_file
...

In [2]: %run histo_time
```
![matplotlib plot of histogram of time events](/images/mpl_authN_histo.png "Interactive matplotlib window: pan, zoom, rubberband, etc")

*Interactive matplotlib window with pan, zoom, rubberband buttons*

***

```
In [3]: %run readG_draw
```
After some time, the full graph will be plotted (for what it's worth).

![authN graph](/images/mpl_global_authN_graph.png "AuthN graph")

*Global, static authN graph*

***

But keep in mind, you can then interactively zoom in on regions of interest:

![authN graph](/images/mpl_zoom_authN_graph.png "AuthN graph, zoom")

***

```
In [4]: %run readG_hub_subgraph
```
![hub subgraph](/images/U6677_hub.png "hub subgraph")

*A hub as a subgraph*
***

![hub subgraph](/images/ipynb.png "IPython notebook")

