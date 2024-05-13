# TODO list for SiReNetA tutorials and examples


### General

- TODO: Replace eigenvalue with largest norm by largest real component (?)
- IDEA: Divide all notebooks into four categories:
	- **Tutorials**. Basic, getting familiar.
	- **Use Cases**. Discuss more in detail specific points, "how to" style and good/bad practices.
	- **Focus points**. Discuss more in detail specific points. Deeper analysis, help understand some problem/point better.
	- **Repro**. Reproduce paper figures and results.
- TODO: Add a README.md file to the folder of the tutorial notebooks (?)

### Documentation, tutorial explanations, etc.

(Temptative) list of documents (.md files) that we should have.

- (DONE) 1. What is sireneta? Overall description of what is Stimulus-Response Network Analysis.
- 2. Canonical models. Summary of the (for now) five canonical models. Their equations and illustrations of the time-series for some simple graph (e.g., the N8 graph in the Chaos paper).




### Tutorial Notebooks

Temptative list and content of the Tutorials:

1. Getting Started : A quick overview of what Stimulus-Response Network Analysis is. 
	1. Installing and getting information on the library.
	2. First example: use a simple, small graph to illustrate a typical analysis workflow.
2. Fundamentals : Fundamentals of Stimulus-Response Network Analysis. 
	1. Understanding the stimulus-responses at all levels (pairs-wise, node-wise and network level). 
	2. Illustration and interpretation of pair-wise responses. 
	3. Examples: directed and undirected chains.
    - **MG: I wouldn't talk about TTP in this notebook, leave it for notebook #5**
	5. **MG: I would move this to notebook #6** Validity in weighted networks.
3. *[Canonical models](#)* : Overview of the five canonical models. Use one simple graph ('TestNet\_N8.txt'?) *__Q: Should we actually have one (short) notebook per canonical model?__*
	1. Start this Notebook showing how typical graph metrics can be associated to the discrete cascade.
	2. For all the five models, plot the time-series and the responses.  This way, we would plot, for each model and a couple of test networks: 
	- trajectories of individual nodes.
	- pair-wise, node-wise and global responses.
4. Compare networks : **MG: see suggestions in notebook**
    - show how response change with network size and density for a random net
    - normalization for 3 types of nets (random, scale-free, lattice)
5.  Extracting spatio-temporal metrics out of R(t) to compute distances: 
	- time-to-peak / time-to-threshold distances. **MG: global-responses is already in notebook #3**
	- Comparison of TTP for leaky-cascade and the continuous diffusion (as used in Arnaudon's paper).
6. *[WeightedNetworks.ipynb](#)* : Illustrate that we can naturally deal with weighted nets. How changing the weights alters the "topology" of the interactions. Input / output responses, help proper interpretation. **(?) MG: focus on weighted nets, as we already present directed binary network in notebook #2**
7. **???**  Extracting more metrics out of R(t) : 
	- Self responses (returnability).




### Specific examples

Besides the basic tutorials, we can extend the content adding "Use Cases" and "Focus Points" to answer specific questions, specific uses or treat some points in more detail.

Q: Should these go together into the "Tutorial_Notebooks/" folder, or should they have their own?
** MG: tutorials should present the basics and some key use cases**

- USE CASE: *[ComparingNetworks.ipynb](#)* : More tutorial-like notebook than the reproduction of Figure 3 in the Chaos (2024) paper.
- USE CASE: Renormalization for the LeakyCascade and the ContinuousDiffusion models. Show what the non-normalised and the intrinsic responses mean. Then, how they are related to the regressed version of the responses.
- USE CASE: regress or not for measures
- USE CASE: Defining distance as time, detailed explanations. 
	- Theoretical predictions of Matt. 
	- Revise Arnaudon's proposal.
	- What to do if responses do not converge? Time to threshold ?
- FOCUS POINT: A detailed explanation of the eigenvalues of A and of the Jacobian J for different models.
- FOCUS POINT: A detailed explanation of how classical graph metrics arise from the discrete cascade.
- FOCUS POINT(s): Q: Dedicate one specific NB for each canonical model?



### Reproduce paper figures

- Probably, we should have a specific folder for this. 
- A notebook to reproduce results of Fig. 2 in the Chaos (2024) paper.
- (DONE) A notebook to reproduce results of Fig. 3 in the Chaos (2024) paper.
- (DONE) A notebook to reproduce results of Fig. 4 in the Chaos (2024) paper.







#####