# Msci Project

## This project was investigating directed acyclic graphs embedded in Minkowski space, comparing various paths in graph to the geodesic of the space. The repository contains the code used for generating the model. 

**Realisations** has the basic version of the model and code for the HPC. It contains a low-ram method of obtaining longest, random and time greedy paths of a DAG. It also contains a .pbs jobscript. 

**Leaner_model** folder contains a streamlined version of the code in 1+1D. It doesn't create the edge objects and gets the longest, random, time greedy, and proper time greedy paths directly from the time-ordered array of node coordinates. 

**3d** folder contains the preliminary version of the 1 time + 2 spatial dimention model. It contains the longest, random, time greedy and proper time greedy paths from the time-ordered array of node coordinates. 

**Measures** folder contains the various 1+1D path measures used in the project: angles, area and protrusion from the ordered list of node coordinates consitituting the path through a network. 

**Analysis** contains the code that retrievs the .npy files from realisations, and then engages in the analysis. this is split into 2 scripts: **Path Measures Analysis** code for the statistical analysis of path properties using the measures we developed. And **Path Scaling Law Analysis** code for statistical analysis of path length scaling with number of nodes. These were originally Google Colab Notebooks that have been converted into .py files, and may contain artifacts from that conversion process.
