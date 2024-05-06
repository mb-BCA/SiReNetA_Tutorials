> WARNING: REPOSITORY UNDER CONSTRUCTION !! First complete release expected during May 2024, stay tuned ! Or follow @GZamora_Lopez in Twitter.

# SiReNetA – Tutorials
### Stimulus-Response Network Analysis (SRNA) …


… is a generalised perspective for the study of graphs and complex networks from the viewpoint of dynamical systems, instead of the traditional combinatorial approach. Many existing graph and network metrics are based on different assumptions of how information, particles, agents or signals may propagate along a network. However, for many of these, the underlying dynamical model and its assumptions are hidden, or have been ignored. *SRNA* is a paradigm shift in the way we study complex networks and interpret their results: from a data-driven (combinatorial) tradition to a (dynamical) model-based data analysis perspective. The goal is to take full advantage of model-based network analyses with transparency at the front. To encompass existing metrics into an integrated methodology and to provide analysis tools in which the underlying assumptions are recognized from the beginning, thus favouring the interpretability of results.



### WHAT WILL YOU FIND HERE

This repository is the entry point for interested users of *Stimulus-Response Network Analysis (SRNA)* and its corresponding Python library *[SiReNetA](https://github.com/mb-BCA/SiReNetA)* . Here we provide a set of tutorials and examples––in the form of Jupyter notebooks––to help interested users walk through the basics and specific examples.

#### Introductory documentation

1. *[1\_Whatis_Sireneta](1_Whatis_Sireneta.md)* : A short overview of the main ideas and goals of stimulus-response network analysis.
2. *[2\_Canonical_Models](2_Canonical_Models.md)* : Description of simple (canonical) models for various classes of dynamical propagation on networks, following a variety of assumptions and constraints. 
2. …

#### Tutorial notebooks

1. *[Getting Started and Overview](Notebooks_Tutorials/1_GettingStarted.ipynb)* : A quick overview of what Stimulus-Response Network Analysis is.
2. *[Response to Stimulus and Calculating Metrics](Notebooks_Tutorials/2_Basics_StimRespMetrics.ipynb)* : Fundamentals of Stimulus-Response Network Analysis. Undertanding the stimulus-responses at all levels (pair-wise, node-wise and network level). Illustration and interpretation of pair-wise responses for undirected and directed chains. Global-responses, time-to-peak / time-to-saturation distances. **NOT THERE YET, BUT NEEDED??? Comparison of TTP for leaky-cascade and the continuous diffusion (as used in Arnaudon's paper).**
3. *[Canonical Models](Notebooks_Tutorials/3_Basics_CanonModels.ipynb)* : Presentation of the different canonical models (Fig. 2 of the Chaos paper).
4. *[Comparing Networks](Notebooks_Tutorials/4_UseCase_CompareNets.ipynb)* : Use case to compare networks by aligning the global response for the leaky cascade (Fig. 3 of the Chaos paper).
5. *[Network Distance](Notebooks_Tutorials/5_UseCase_NetDist.ipynb)* : Use case with "redefinition" of the geodesic graph distance using the leaky cascade via the time-to-peak (Fig. 4 of Chaos paper).
6. *[Weighted Networks](Notebooks_Tutorials/6_UseCase_WeightedNets.ipynb)* : Use case to illustrate that the framework naturally deals with weighted networks, with a focus on the doscrete and leaky cascades. How changing the weights alters the "topology" of the interactions.

#### Code to reproduce papers

See resources in folder [Reproduce_Papers/](Reproduce_Papers).


&nbsp;
### GETTING FURTHER DOCUMENTATION

The documentation of the *SiReNetA* library can be accessed 'online' as usual for other python packages. Typing either `help(module_name)` or `module_name?` in an IPython interactive session will display the docstring of the module. Equally, `module_name.func_name?` will show the usage instructions for each function.



&nbsp;
### REFERENCES AND CITATION

- G. Zamora-López and M. Gilson *[An integrative dynamical perspective for graph theory and the analysis of complex networks.](https://doi.org/10.1063/5.0202241)* Chaos 34, 041501 (2024).
- M. Gilson, N. Kouvaris, et al. *[Network analysis of whole-brain fMRI
dynamics: A new framework based on dynamic communicability.](https://doi.org/10.1016/j.neuroimage.2019.116007)* NeuroImage 201, 116007 (2019).
- M. Gilson, N. Kouvaris, G. Deco & G.Zamora-Lopez "*[Framework based on communicability and flow to analyze complex networks](https://doi.org/10.1103/PhysRevE.97.052301)*" Phys. Rev. E 97, 052301 (2018).



&nbsp;
### NOTES

List of recommendations and further topics that should be covered in the tutorials.

- How to properly interpret the concepts and the metrics.
