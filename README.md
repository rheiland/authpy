authpy
======

Python scripts to analyze an authentication dataset.

The authentication dataset from LANL ([http://csr.lanl.gov/data/auth/](http://csr.lanl.gov/data/auth/))
provides a valuable benchmark dataset for researchers in cybersecurity and/or graphs/networks.

We recommend using the [Anaconda Python 3](https://store.continuum.io/cshop/anaconda/) distribution.

![matplotlib plot of histogram of time events](/images/mpl_authN_histo.png "Interactive matplotlib window: pan, zoom, rubberband, etc")

Interactive matplotlib window with pan, zoom, rubberband buttons.


```
$ ipython --matplotlib

Python 3.4.2 |Anaconda 2.1.0 
...
Using matplotlib backend: MacOSX

In [1]: %run readG_draw
```
After some time, the full graph will be plotted.

