This is a new test markdown file … but I don'T see the markdaonw formatting toolbar :(


### Canonical propagation models

The key for transparent model-based analyses is to provide analysis metrics that can be derived for different propagation models; with each model satisfying diffent sets of assumptions and constraints. Canonical models should be as simple as possible since their aim is data analysis, not to faithfully reproduce the behaviour of real systems. Here the list of current canonical models supported by the *ReNetA* library. See Zamora-López & Gilson, Chaos (2024) for further details:

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







# hi there

lksjdl **yeah** !!

$`x_{i,t} = \sum_{k=1}^n A^t_{ik} x_{k,t-1}`$


$`\dot{\mathbf{x}} = A \mathbf{x} `$
$`\dot{\mathbf{x}} = A \mathbf{x} `$

```math
\begin{eqnarray}
\dot{\mathbf{x}} & = & A \mathbf{x} \\
\dot{\mathbf{x}} &=& A \mathbf{x} \\
\dot{x}_i &=& \sum_{k=1}^n A_{ik} x_k
\end{eqnarray}
```

```math
\textrm{Matrix form:} \; \dot{\mathbf{x}} = A \mathbf{x} \qquad
\textrm{Node-wise:} \; \dot{x}_i = \sum_{k=1}^n A_{ik} x_k
```



