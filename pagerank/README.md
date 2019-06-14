The file: pagerank.py, will read in the input file (representation of a web graph) and generate a transition matrix based on the in/out links.
We then generate a teleportation matrix with teleportation rate of 0.14 to ensure the webgraph is an ergodic markov chain (to ensure the steady state vector will converge)

the output scores for each page is generated in: out.txt