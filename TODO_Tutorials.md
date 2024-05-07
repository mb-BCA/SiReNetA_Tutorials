# TODO list for SiReNetA tutorials and examples


### General

- Replace eigenvalue with largest norm by largest real component (?)

### Documentation, tutorial explanations, etc.

(Temptative) list of documents (.md files) that we should have.

- (DONE) 1. What is sireneta? Overall description of what is Stimulus-Response Network Analysis.
- 2. Canonical models. Summary of the (for now) five canonical models. Their equations and illustrations of the time-series for some simple graph (e.g., the N8 graph in the Chaos paper).




### Tutorial Notebooks

Temptative list and content of the Tutorials:

1. Getting Started : A quick overview of what Stimulus-Response Network Analysis is. 
	1. Installing and getting information on the library.
	2. First example: use the directed path graph.
2. Fundamentals : Fundamentals of Stimulus-Response Network Analysis. Undertanding the stimulus-responses at all levels (pairs-wise, node-wise and network level). Illustration and interpretation of pair-wise responses. Examples: directed and undirected chains. Validity in weighted networks.
3. *[Canonical models](#)* : Overview of the five canonical models. Plot their time-series and the responses for some simple network(s). *__Q: Should we actually have one (short) notebook per canonical model?__* This way, we would plot, for each model and a couple of test networks: 
	- trajectories of individual nodes.
	- pair-wise, node-wise and global responses.
4. Extracting metrics out of R(t) : 
	- global-responses, time-to-peak / time-to-threshold distances.
	- Comparison of TTP for leaky-cascade and the continuous diffusion (as used in Arnaudon's paper).
	- Self responses (returnability).
5. Metrics for directed networks. Input / output responses, help proper interpretation.
5. *[ComparingNetworks.ipynb](#)* : More tutorial-like notebook than the reproduction of Figure 3 in the Chaos (2024) paper.
6. *[WeightedNetworks.ipynb](#)* : Illustrate that we can naturally deal with weighted nets. How changing the weights alters the "topology" of the interactions.




### Specific examples, reproduce papers, etc.

- (DONE) A notebook to reproduce results of Fig. 3 in the Chaos (2024) paper.
- (DONE) A notebook to reproduce results of Fig. 4 in the Chaos (2024) paper.
- Renormalization for the LeakyCascade and the ContinuousDiffusion models. Show what the non-normalised and the intrinsic responses mean. Then, how they are related to the regressed version of the responses.





#####