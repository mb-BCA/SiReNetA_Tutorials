> WARNING: REPOSITORY UNDER CONSTRUCTION !! First complete release expected during May 2024, stay tuned ! Or follow @GZamora_Lopez in Twitter.


&nbsp;
## 2. Canonical propagation models

Introductory paragraph here … 

- why need of canonical models? 
- What is canonical model / when is a model canonical?
- etc.



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


![Illustration of the discrete cascade](#)

**Figure–1:** Write the caption here   
&nbsp;
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


![Illustration of the random walk](#)

**Figure–2:** Write the caption here   
&nbsp;
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


![Illustration of the continuous cascade](#)

**Figure–3:** Write the caption here   
&nbsp;
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



![Illustration of the leaky cascade](#)

**Figure–4:** Write the caption here   
&nbsp;
&nbsp;




**Continuous diffusion model / the heat equation**: Given a (weighted) connectivity matrix $A$, the activity of the system is governed by
```math
\dot{\mathbf{x}}(t) = - D \, \mathbf{x}(t) \,+\, A \, \mathbf{x}(t) \,=\, L\, \mathbf{x} \quad ,
```
where $D$ is the diagonal matrix of node degrees and $`L = - D + A`$ is the Jacobian matrix (graph Laplacian) of the system. If a stimulus of unit amplitude is initially applied in all nodes, initial conditions $`\mathbf{x}^T(0) = \mathbf{1}`$, then the node responses evolve as $`\mathbf{x}(t) = e^{Lt} \, \mathbf{1}`$.

>Assumptions and constraints:
> - Continuous variable.
> - Continuous time.
> - Conservative system. Total activity of the network $`\parallel \mathbf{x}(t) \parallel`$ remains constant over time.
> - Convergent. Solutions $`x_i(t)`$ rapidly converge to a constant with time.


![Illustration of the continuous diffusion model](#)

**Figure–5:** Write the caption here   
&nbsp;
&nbsp;



### What to do next

Read more …

- *[Docs\_3\_xxxxxxxxx](#)* : Short description here.

Or start playing around with SiReNetA …

1. *[GettingStarted.ipynb](1_GettingStarted.ipynb)* : A quick overview of what Stimulus-Response Network Analysis is. Use the sample graph with 8 nodes.
2. *[Fundamentals.ipynb](2_Basics_StimResponses.ipynb)* : Fundamentals of Stimulus-Response Network Analysis. Undertanding the stimulus-responses at all levels (pairs-wise, node-wise and network level).
3. *[Basic_Metrics.ipynb](#)* : Extracting metrics: global-responses, time-to-peak / time-to-threshold distances. Comparison of TTP for leaky-cascade and the continuous diffusion (as used in Arnaudon's paper).
4. An overview of the different canonical models.







#