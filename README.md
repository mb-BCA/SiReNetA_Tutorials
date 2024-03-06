# SiReNetA – Tutorials


## 1. What is Response Network Analysis?

<!-- Graph theory constitutes a widely used and established field providing powerful tools for the characterization of complex networks. However, the diversity of complex networks studied nowadays overcomes the capabilities of graph theory (originally developed for binary adjacency matrices) to understand networks and their function. In the recent years plenty of alternative metrics have been proposed which are–one way or another–based on dynamical phenomena happening on networks.
-->

It is a generalised perspective for the study of graphs and complex networks from the viewpoint of dynamical systems. Existing graph and network metrics are based on different assumptions of how information may propagate along a network. However, for many of these metrics the underlying dynamical model and its assumptions are hidden, or have been ignored. Other approaches made use of propagation phenomena to define network metrics but were introduced with a sense of universality; "*as if*" they were useful and interpretable in any network despite their specific underlying assumptions.

*Stimulus-Response Network Analysis* (SRNA) is a paradigm shift in the way we study complex networks and interpret their results: from a data-driven (model-free) tradition to a model-based data analysis perspective. The goal is to take full advantage of model-based network analyses with transparency at the front. To encompass existing metrics into an integrated methodology and to provide network analysis tools in which the underlying assumptions are recognized from the beginning, thus favouring the interpretability of results.

The core idea behind SRNA is to reveal the properties of networks by probing how the nodes of a network respond to small, localised perturbations (e.g., a stimulus of unit amplitude). Imagine a rectangular brick of an unknown material as in Fig. 1A. Imagine that we softly bang one of its sides with a small hammer and measure the resulting responses (e.g., vibrations or displacement) at sites of the brick away from the impact site. The manner in which the "kick" propagates throughout the brick–and consequently the responses observed–depends on the material the brick is made of. A wooden rod will tend to show a displacement, a metallic brick may start vibrating and a brick made of soft rubber will attenuate the propagation of the perturbation. By carefully studying the responses at differnt sites, we can derive the properties of the brick and its internal composition.


![Stimulus-Response Diagram](#)

Analogously, *SRNA* aims at investigating the properties of a network by applying a stimulus in one node and observing how the rest of the nodes respond, as illustrated in Fig. 1B. In our case, the dynamical propagation model of choice resembles the "material" of which the brick is made of, since it is this model which determines how the stimulus propagates. Unlike in the case of the brick, in *RSNA* canonical propagation model is repleceable, thus allowing to investigate the properties of a network "made of different materials." 


##### References and Citation

- G. Zamora-López and M. Gilson "*[An integrative dynamical perspective for graph theory and the analysis of complex networks](#)*" Chaos, (*in press*).  [Preprint](https://doi.org/10.48550/arXiv.2307.02449).


### Working pipeline in Stimulus-Response Network Analysis

1. **Identify the key constraints** of the real system investigated. For example, the user may need to question whether the networked system is discrete or continuous, whether it is conservative or non-conservative, whether it follows divergent or convergent behavior, whether it is diffusively coupled or not.
2. **Choose a canonical propagation propagation model** that satisfies those assumptions and constraints. We propose initially five linear canonical models of propagation and diffusion, but users may consider other canonical models if required by the nature of the real system.
3. **Compute the pair-wise network responses** $\mathcal{R}(t)$ of the network, for the chosen canonical model. The elements $\mathcal{R}_{ij}(t)$ are the temporal responses of node $i$ to a stimulus applied at node $j$ at time $t=0$. It is usually calculated as the *propagator* (for time-continuous systems) or the *Green's function* (for time-continuous cases) of the propagation dynamics on a network.
4. Extract information out of $\mathcal{R}(t)$ in the form of **spatio-temporal network metrics**. For example, the global network response $r(t)$, the time-to-peak distance $D^{ttp}$ and the in-/out-responses $r_i(t)$ of the nodes.


### Canonical propagation models

The key for transparent model-based analyses is to provide analysis metrics that can be derived for different propagation models; with each model satisfying diffent sets of assumptions and constraints. Canonical models should be as simple as possible since their aim is data analysis, not to faithfully reproduce the behaviour of real systems. Here the list of current canonical models supported by the *SiReNetA* library. See Zamora-López & Gilson, Chaos (2024) for further details:

**Discrete cascade**: Given adjancency matrix $A$, the number of particles in node $i$ at time $t$, $x_{i,t}$, evolves as
```math
\mathbf{x}_t = A \, \mathbf{x}_{t-1} \quad .
```
If one particle is seed at each node at time $`t=0`$, initial conditions $`\mathbf{x}^T_0 = \mathbf{1} = [1, 1, \ldots, 1]`$, then $`\mathbf{x}_t = A^t \, \mathbf{1}`$.

>Assumptions and constraints:
> - Discrete variables. If $A$ is a binary adjacency matrix, then $`x_{i,t} \in \mathbb{N}`$ is the number of particles.
> - Discrete time-steps.
> - Non-conservative system. Total number of particles in the network $`\parallel \mathbf{x}_t \parallel`$ changes with time.
> - Divergent. If $`A`$ is positive definite, solutions $`x_i`$ rapidly grow to infinity.


&nbsp;

**Simple random walk**: Given $T$ is the transition probability matrix of (weighted) connectivity $A$, the simple random walk is
```math
\mathbf{x}_t = T \, \mathbf{x}_{t-1} \quad ,
```
where $`x_{i,t}`$ is the expected number of walkers found in node $i$ at time $t$. If one walker is seeded at each node at time $t=0$, initial conditions $`\mathbf{x}^T_0 = \mathbf{1} = [1, 1, \ldots, 1]`$, then $`\mathbf{x}_t = T^t \, \mathbf{1}`$.

>Assumptions and constraints:
> - Discrete system but continuous variable. The number of walkers is discrete but $x_{i,t}$ represent expectation values from probabilities $T_{ij}$.
> - Discrete time-steps.
> - Conservative system. The number of walkers is the same over time: $`\parallel \mathbf{x}_t \parallel \,=\, \parallel \mathbf{x}_0 \parallel`$.
> - Convergent. Number of walkers remains finite.


&nbsp;

**Continuous cascade**: Given a (weighted) connectivity matrix $A$, the activity of the system is represented by
```math
\dot{\mathbf{x}}(t) = A \, \mathbf{x}(t) \quad .
```
If a stimulus of unit amplitude is applied in all nodes, initial conditions $`\mathbf{x}^T(0) = \mathbf{1} = [1, 1, \ldots, 1]`$, then the activity of the nodes evolves as $`\mathbf{x}(t) = e^{At} \, \mathbf{1}`$.

>Assumptions and constraints:
> - Continuous variable: $`x_i(t) \in \mathbb{R}`$.
> - Continuous time.
> - Non-conservative system. The total activity of the network $`\parallel \mathbf{x}(t) \parallel`$ changes with time.
> - Divergent. If $`A`$ is positive definite, solutions $`x_i(t)`$ rapidly grow to infinity.


&nbsp;

**Leaky cascade**:  Given a (weighted) connectivity matrix $A$ and leakage time-constant $\tau$, the activity of the system is
```math
\dot{\mathbf{x}}(t) = - \frac{1}{\tau} \mathbf{x}(t) \,+\, A \, \mathbf{x}(t) \quad .
```
If a stimulus of unit amplitude is initially applied in all nodes, initial conditions $`\mathbf{x}^T(0) = \mathbf{1}`$, then the node responses evolve as $`\mathbf{x}(t) = e^{Jt} \, \mathbf{1}`$ with $`J = - \mathbf{I} / \tau + A`$ is the Jacobian of the system.

>Assumptions and constraints:
> - Continuous variable: $`x_i(t) \in \mathbb{R}`$.
> - Continuous time.
> - Non-conservative system. The total activity of the network $`\parallel \mathbf{x}(t) \parallel`$ changes with time.
> - Given that $\lambda_{max}$ is the spectral radius of (positive definite) $A$, then if $`\tau < 1 / \lambda_{max}`$ the system is convergent and solutions $`x_i(t) \to 0`$.


&nbsp;

**Continuous diffusion model**: Given a (weighted) connectivity matrix $A$, the activity of the system is governed by
```math
\dot{\mathbf{x}}(t) = - D \, \mathbf{x}(t) \,+\, A \, \mathbf{x}(t) \,=\, L\, \mathbf{x} \quad ,
```
where $D$ is the diagonal matrix of node degrees and $`L = - D + A`$ is the Jacobian matrix (graph Laplacian) of the system. If a stimulus of unit amplitude is initially applied in all nodes, initial conditions $`\mathbf{x}^T(0) = \mathbf{1}`$, then the node responses evolve as $`\mathbf{x}(t) = e^{Lt} \, \mathbf{1}`$.

>Assumptions and constraints:
> - Continuous variable.
> - Continuous time.
> - Conservative system. Total activity of the network $`\parallel \mathbf{x}(t) \parallel`$ remains constant over time.
> - Convergent. Solutions $`x_i(t)`$ rapidly converge to a constant with time.



&nbsp;
## 2. What will you find here

This repository is the entry point for users of *SRNA* and the Python library *SiReNetA* to carry out the analyses. There is no official documentation for either *SiReNetA* but a set of tutorials and examples (in the form of Jupyter notebooks) will walk the users through the basics and specific examples.

#### List of Tutorial notebooks

1. *[GettingStarted.ipynb](#)*: A quick overview of what Stimulus-Response Network Analysis is. Use the sample graph with 8 nodes.
2. *[Fundamentals.ipynb](#)*: Fundamentals of Stimulus-Response Network Analysis. Undertanding the stimulus-responses at all levels (pairs, nodes and network). Illustration and interpretation of pair-wise responses. Examples: directed and undirected chains. Validity in weighted networks.
4. Extracting metrics: global-responses, time-to-peak / time-to-threshold distances. Comparison of TTP for leaky-cascade and the continuous diffusion (as used in Arnaudon's paper).
5. An overview of the different canonical models.


#### List of examples and code to reproduce papers

- Comparison of canonical models, *[Examples_CanonicalModels.ipynb](#)*
- Validation of time-to-peak distance with graph distance.
- Network comparison under Stimulus-Response Network Analysis.


&nbsp;
## NOTES

List of recommendations and further topics that should be covered in the tutorials.

- How to properly interpret the concepts and the metrics.
