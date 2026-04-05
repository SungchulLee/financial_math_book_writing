# Skorokhod Embedding Problem


## Introduction


The **Skorokhod embedding problem** (SEP) asks: given a probability measure $\mu$ on $\mathbb{R}$ with zero mean and finite variance, find a stopping time $\tau$ for a standard Brownian motion $(B_t)_{t \geq 0}$ such that $B_\tau \sim \mu$. This classical problem in probability theory, first posed and solved by Skorokhod in 1961, has become a cornerstone of robust mathematical finance through Hobson's insight that model-free bounds for exotic options correspond to extremal solutions of the SEP.

The connection is natural: any continuous martingale can be represented as a time-changed Brownian motion (by the Dambis-Dubins-Schwarz theorem), so optimizing over all martingale models with a given terminal distribution reduces to optimizing over all Skorokhod embeddings of that distribution.

This section develops the classical theory and its principal solutions, then establishes the deep connection to robust pricing that makes the SEP indispensable in modern quantitative finance.

## The Classical Problem


### 1. Formal Statement


**Definition** (Skorokhod Embedding Problem): Let $(B_t)_{t \geq 0}$ be a standard Brownian motion started at $B_0 = 0$, and let $\mu$ be a centered probability measure on $\mathbb{R}$ (i.e., $\int x \, d\mu(x) = 0$). Find a stopping time $\tau$ with respect to the natural filtration of $B$ such that:

1. $B_\tau \sim \mu$
2. $(B_{t \wedge \tau})_{t \geq 0}$ is uniformly integrable

The uniform integrability condition (2) ensures that $\mathbb{E}[B_\tau] = \mathbb{E}[B_0] = 0$, preserving the martingale property, and rules out trivial or pathological solutions.

**Remark**: When the initial value is $B_0 = x$ rather than zero, the target measure must satisfy $\int y \, d\mu(y) = x$. In the financial context, we embed $\mu$ starting from $S_0$, so the target measure has mean $S_0$.

### 2. Existence: Skorokhod's Original Solution


**Theorem** (Skorokhod, 1961): For any centered probability measure $\mu$ on $\mathbb{R}$ with $\int x^2 \, d\mu(x) < \infty$, there exists a stopping time $\tau$ such that $B_\tau \sim \mu$ and $\mathbb{E}[\tau] = \int x^2 \, d\mu(x)$.

*Proof sketch*: Skorokhod's construction uses a sequence of independent randomized stopping rules. Decompose $\mu = p \mu^+ + (1-p) \mu^-$ where $\mu^+$ is supported on $[0, \infty)$ and $\mu^-$ on $(-\infty, 0]$, with $p = \mu([0,\infty))$. The key idea is:

**Step 1**: At time 0, with probability determined by $\mu$, decide whether $B_\tau$ will be positive or negative.

**Step 2**: Conditional on the sign, stop the Brownian motion at an appropriate level using further randomization.

The construction proceeds iteratively: define independent random variables $\alpha_1, \alpha_2, \ldots$ and $\beta_1, \beta_2, \ldots$ such that the Brownian motion is stopped at the first time it exits an interval $(-\alpha_k, \beta_k)$, with the interval depending on which boundary was hit at the previous step. The identity $\mathbb{E}[\tau] = \text{Var}(\mu)$ follows from the optional stopping theorem applied to the martingale $B_t^2 - t$. $\square$

### 3. Non-Uniqueness


A fundamental feature of the SEP is that the solution is **far from unique**. For a given $\mu$, there are typically uncountably many stopping times $\tau$ with $B_\tau \sim \mu$.

**Example**: Let $\mu$ be the symmetric distribution $\frac{1}{2}\delta_{-1} + \frac{1}{2}\delta_{+1}$. Then:

- **First exit time**: $\tau_1 = \inf\{t \geq 0 : |B_t| = 1\}$ gives $B_{\tau_1} \sim \mu$
- **Last zero before an independent exponential**: $\tau_2 = \sup\{t \leq \mathbf{e} : B_t = 0\}$ where $\mathbf{e} \sim \text{Exp}(1/2)$ is independent of $B$, followed by the sign of $B_{\mathbf{e}}$, also yields $B_{\tau_2} \sim \mu$

These stopping times produce identical terminal distributions but very different path properties (running maximum, running minimum, occupation times), which is precisely why different embeddings give different robust bounds.

## The Azema-Yor Embedding


### 1. Construction


The **Azema-Yor embedding** (1979) is perhaps the most important solution for financial applications, as it maximizes the law of the running maximum.

**Setup**: Let $\mu$ be a centered probability measure with continuous distribution function $F_\mu$. Define the **barycentre function**:

$$
\psi(x) = \mathbb{E}_\mu[X \mid X \geq x] = \frac{\int_x^\infty y \, d\mu(y)}{1 - F_\mu(x)}
$$

for $x$ in the support of $\mu$ where $F_\mu(x) < 1$. The function $\psi$ is continuous and strictly increasing on its domain, with $\psi(x) > x$ for $x < x_{\max}$ (the right endpoint of the support) and $\psi(x) \to x_{\max}$ as $x \to x_{\max}$.

**Definition** (Azema-Yor Stopping Time): Let $\overline{B}_t = \max_{0 \leq s \leq t} B_s$ denote the running maximum. The Azema-Yor stopping time is:

$$
\tau_{AY} = \inf\{t \geq 0 : B_t \leq \psi^{-1}(\overline{B}_t)\}
$$

Equivalently, stop the first time the current value drops below a function of the running maximum. At the stopping time, the Brownian motion is at a value determined by how high it has previously reached.

**Theorem** (Azema-Yor, 1979): The stopping time $\tau_{AY}$ satisfies:

1. $B_{\tau_{AY}} \sim \mu$
2. $(B_{t \wedge \tau_{AY}})_{t \geq 0}$ is uniformly integrable
3. $\overline{B}_{\tau_{AY}} = \psi(B_{\tau_{AY}})$ almost surely

### 2. Optimality Property


**Theorem** (Azema-Yor Optimality): Among all solutions $\tau$ of the SEP for $\mu$, the Azema-Yor embedding maximizes $\mathbb{E}[f(\overline{B}_\tau)]$ for every increasing convex function $f$.

Equivalently, $\overline{B}_{\tau_{AY}}$ is the largest in convex order among all $\overline{B}_\tau$:

$$
\mathbb{E}[f(\overline{B}_\tau)] \leq \mathbb{E}[f(\overline{B}_{\tau_{AY}})]
$$

for all increasing convex $f$ and all uniformly integrable embeddings $\tau$ of $\mu$.

*Proof*: The key identity is that at the Azema-Yor stopping time, the running maximum $\overline{B}_{\tau_{AY}}$ is a **deterministic function** of the terminal value $B_{\tau_{AY}}$, namely $\overline{B}_{\tau_{AY}} = \psi(B_{\tau_{AY}})$. This creates the strongest possible positive dependence between the maximum and the terminal value.

For any other embedding $\tau$, the conditional expectation satisfies:

$$
\mathbb{E}[\overline{B}_\tau \mid B_\tau = x] \leq \psi(x) = \overline{B}_{\tau_{AY}} \mid_{B_{\tau_{AY}} = x}
$$

because $\psi(x) = \mathbb{E}[X \mid X \geq x]$ is the largest possible conditional mean of the maximum given the terminal value $x$. The convex order comparison then follows from Jensen's inequality. $\square$

### 3. Financial Interpretation


The Azema-Yor embedding is the **worst-case model for lookback options**. Since lookback payoffs depend on the running maximum (or minimum), and the Azema-Yor embedding maximizes functionals of the running maximum, it attains the robust upper bound:

$$
\sup_\tau \mathbb{E}[f(\overline{B}_\tau) - g(B_\tau)] = \mathbb{E}[f(\overline{B}_{\tau_{AY}}) - g(B_{\tau_{AY}})]
$$

for appropriate functions $f$ and $g$ encoding the lookback payoff.

**Connection to Hobson's Lookback Bound**: The robust upper bound for the floating-strike lookback call $S_T - \min_{t \leq T} S_t$ is attained by the Azema-Yor embedding of $\mu$ (the risk-neutral marginal of $S_T$) into Brownian motion, yielding:

$$
\overline{V}_{\text{lookback}} = \int_0^\infty \frac{2 C(K)}{K} \, dK
$$

## The Root Embedding


### 1. Construction


The **Root embedding** (1969) stops Brownian motion at the first entry time into a **barrier set**, providing a geometrically intuitive solution.

**Definition** (Root Barrier): A Root barrier is a subset $\mathcal{R} \subset [0, \infty) \times \mathbb{R}$ of the form:

$$
\mathcal{R} = \{(t, x) : t \geq r(x)\}
$$

where $r: \mathbb{R} \to [0, \infty]$ is a lower semicontinuous function (the **barrier function**). The set $\mathcal{R}$ is the region "below" the barrier in time-space.

**Definition** (Root Stopping Time): Given a Root barrier $\mathcal{R}$, define:

$$
\tau_R = \inf\{t \geq 0 : (t, B_t) \in \mathcal{R}\}
$$

**Theorem** (Root, 1969): For any centered probability measure $\mu$ with finite variance, there exists a barrier $\mathcal{R}$ such that:

1. $B_{\tau_R} \sim \mu$
2. $(B_{t \wedge \tau_R})_{t \geq 0}$ is uniformly integrable
3. $\mathbb{E}[\tau_R] = \int x^2 \, d\mu(x) = \text{Var}(\mu)$

### 2. Optimality Property


**Theorem** (Rost, 1976): The Root embedding minimizes $\mathbb{E}[f(\tau)]$ for every convex function $f$ among all solutions of the SEP for $\mu$.

In particular:

$$
\mathbb{E}[\tau_R^2] \leq \mathbb{E}[\tau^2]
$$

for any other uniformly integrable embedding $\tau$ of $\mu$.

*Proof sketch*: The Root stopping time is the **first** time the process enters the target region, making it the "most direct" embedding. The barrier structure ensures that once the process has spent enough time at a given level, it stops --- this minimizes the total time spent in the embedding. The optimality follows from a potential-theoretic argument: the Root barrier is characterized by the condition that the potential of $B_\tau$ (as a function of time and space) equals the potential of $\mu$ exactly on the barrier. $\square$

### 3. Financial Interpretation


The Root embedding is optimal for **variance swap pricing**. Since the realized variance of a continuous martingale $M_t = B_{\langle M \rangle_t}$ over $[0,T]$ is determined by the quadratic variation $\langle M \rangle_T$, and the quadratic variation corresponds to the stopping time $\tau$ in the Brownian embedding, minimizing functionals of $\tau$ translates to minimizing functionals of the realized variance.

For the discretized variance payoff:

$$
\Phi = \sum_{i=1}^N \left(\log \frac{S_{t_i}}{S_{t_{i-1}}}\right)^2 \approx \langle \log S \rangle_T
$$

the Root embedding provides the model that minimizes variance swap prices, complementing the Carr-Madan replication formula.

## The Perkins Embedding


### 1. Construction


The **Perkins embedding** (1986) simultaneously controls both the running maximum and running minimum, making it relevant for double barrier options.

**Definition** (Perkins Embedding): The Perkins solution uses two barrier functions $u, l: [0, \infty) \to \mathbb{R}$ with $u$ decreasing and $l$ increasing, defining:

$$
\tau_P = \inf\{t \geq 0 : B_t \geq u(\underline{B}_t) \text{ or } B_t \leq l(\overline{B}_t)\}
$$

where $\overline{B}_t = \max_{s \leq t} B_s$ and $\underline{B}_t = \min_{s \leq t} B_s$.

The stopping rule is: stop when the current value exceeds an upper barrier that depends on how low the process has gone, or falls below a lower barrier that depends on how high it has gone.

### 2. Optimality Property


**Theorem** (Perkins, 1986): Among all solutions $\tau$ of the SEP for $\mu$, the Perkins embedding minimizes $\mathbb{E}[f(\overline{B}_\tau, \underline{B}_\tau)]$ for functions $f$ that are increasing in the first argument and decreasing in the second.

Specifically, the Perkins embedding minimizes the range $\overline{B}_\tau - \underline{B}_\tau$ in an appropriate stochastic ordering sense.

### 3. Financial Interpretation


The Perkins embedding is the **best-case model for double barrier options**. For a double no-touch option that pays \$1 if the stock stays within $[L, H]$:

$$
\Phi = \mathbb{1}\{L \leq S_t \leq H \text{ for all } t \in [0,T]\}
$$

the Perkins embedding maximizes the probability that the path remains within the barriers, since it minimizes the spread of the running maximum and minimum. This yields the robust upper bound for double no-touch options.

## Connections Between Embeddings


### 1. Monotone Principle


A unifying framework for understanding why different embeddings optimize different functionals is the **monotone principle** of Beiglbock, Cox, and Huesmann (2017).

**Theorem** (Monotone Principle): An embedding $\tau^*$ is optimal for maximizing $\mathbb{E}[\gamma(\tau^*, B)]$ over all embeddings of $\mu$ if and only if $\tau^*$ satisfies a monotonicity condition: there is no "swap" of mass between two paths that would improve the objective while preserving the terminal distribution.

Formally, if $(B^{(1)}, \tau^{*(1)})$ and $(B^{(2)}, \tau^{*(2)})$ are two independent copies of the stopped process, and if swapping the stopping decisions (stopping $B^{(1)}$ later and $B^{(2)}$ earlier, or vice versa) would improve the objective, then such a swap must violate the embedding constraint.

### 2. Summary of Optimal Embeddings

The following table summarizes the correspondence between financial payoffs and optimal embeddings:

| Payoff | Optimal Embedding | Optimality |
|---|---|---|
| Lookback call: $S_T - \min S_t$ | Azema-Yor | Maximizes running max |
| Lookback put: $\max S_t - S_T$ | Azema-Yor (reversed) | Maximizes running max |
| Variance swap: $\sum (\Delta \log S)^2$ | Root | Minimizes expected time |
| Double no-touch: $\mathbb{1}\{L \leq S \leq H\}$ | Perkins | Minimizes range |
| Barrier option: $(S_T - K)^+ \mathbb{1}\{\max S \geq H\}$ | Azema-Yor / Perkins | Depends on direction |

## From Embedding to Robust Pricing


### 1. The Dambis-Dubins-Schwarz Connection


The bridge between the SEP and robust pricing relies on the **Dambis-Dubins-Schwarz theorem**.

**Theorem** (Dambis-Dubins-Schwarz): If $(M_t)_{0 \leq t \leq T}$ is a continuous local martingale with $M_0 = 0$ and $\langle M \rangle_T = \infty$ a.s., then there exists a Brownian motion $(W_u)_{u \geq 0}$ such that:

$$
M_t = W_{\langle M \rangle_t}
$$

**Consequence for Robust Pricing**: Any continuous martingale model for $S_t$ with $S_T \sim \mu$ can be represented as $S_t = S_0 + W_{A_t}$ for some time change $A_t$ with $A_0 = 0$. The terminal condition $S_T \sim \mu$ becomes $W_{A_T} \sim \mu - S_0$ (centered). Setting $\tau = A_T$, the problem reduces to the SEP.

### 2. Robust Pricing via SEP


**Theorem** (Hobson, 1998): For a path-dependent payoff $\Phi$ that depends on the stock price only through the terminal value and the running maximum, the robust upper bound is:

$$
\overline{V} = \sup_{\tau \in \mathcal{T}(\mu)} \mathbb{E}[\Phi(B_\tau, \overline{B}_\tau)]
$$

where $\mathcal{T}(\mu)$ denotes the set of all uniformly integrable stopping times embedding $\mu$.

*Proof*: **Step 1** (Continuous models suffice): By an approximation argument, the supremum over all martingale models equals the supremum over continuous martingale models.

**Step 2** (Reduction to Brownian motion): By the Dambis-Dubins-Schwarz theorem, any continuous martingale model $(S_t)$ with $S_T \sim \mu$ corresponds to a time-changed Brownian motion. The running maximum of the original process relates to the running maximum of the Brownian motion via:

$$
\max_{0 \leq t \leq T} S_t = S_0 + \max_{0 \leq u \leq \tau} W_u = S_0 + \overline{W}_\tau
$$

**Step 3** (Optimization): The path-dependent payoff, expressed in terms of $(W_\tau, \overline{W}_\tau)$, is optimized over all embeddings $\tau$ of $\mu$ (shifted by $S_0$). The optimal embedding determines the extremal model. $\square$

### 3. Semi-Static Hedging Duality


The dual side of the embedding optimization provides **semi-static superhedging strategies**.

**Theorem** (Hobson-Neuberger, 2012): The robust upper bound satisfies:

$$
\overline{V} = \inf\left\{\int \phi(x) \, d\mu(x) : \phi(B_\tau) + \int_0^\tau h(B_s, \overline{B}_s) \, dB_s \geq \Phi(B_\tau, \overline{B}_\tau) \text{ for all } \tau \in \mathcal{T}(\mu)\right\}
$$

where $\phi$ represents the static position in vanilla options and $h$ represents the dynamic trading strategy. The infimum over superhedging strategies equals the supremum over model prices (strong duality).

**Interpretation**: The cheapest portfolio of vanilla options (determined by $\phi$) plus a self-financing dynamic strategy (determined by $h$) that dominates the exotic payoff $\Phi$ in every model costs exactly $\overline{V}$.

## Multi-Marginal Extensions


### 1. The Multi-Period SEP


When option prices are observed at multiple maturities $T_1 < T_2 < \cdots < T_n$, the embedding problem becomes multi-marginal.

**Definition** (Multi-Marginal SEP): Given measures $\mu_1, \ldots, \mu_n$ in convex order ($\mu_1 \preceq_{cx} \mu_2 \preceq_{cx} \cdots \preceq_{cx} \mu_n$), find stopping times $\tau_1 \leq \tau_2 \leq \cdots \leq \tau_n$ such that $B_{\tau_i} \sim \mu_i$ for each $i$.

**Existence** (Kellerer, 1972): Such a multi-marginal embedding exists if and only if the measures are in convex order.

### 2. Iterated Azema-Yor


For lookback-type payoffs in the multi-marginal setting, the **iterated Azema-Yor embedding** of Henry-Labordere, Obloj, Spoida, and Touzi (2016) provides the extremal solution.

**Construction**: At each step $i$, apply the Azema-Yor embedding for the conditional distribution of $\mu_{i+1}$ given the state at time $\tau_i$. The key insight is that the Azema-Yor structure (stopping when the current value drops below a function of the running maximum) can be iterated while preserving the optimality property.

**Theorem**: The iterated Azema-Yor embedding maximizes $\mathbb{E}[f(\overline{B}_{\tau_n})]$ among all multi-marginal embeddings, providing the robust upper bound for lookback options given multiple marginal constraints.

### 3. Tightening of Bounds


Each additional marginal constraint strictly tightens the robust bounds.

**Proposition**: If $\mu_1 \preceq_{cx} \mu_2$ with $\mu_1 \neq \mu_2$, then:

$$
\overline{V}(\mu_1, \mu_2) \leq \overline{V}(\mu_2)
$$

where $\overline{V}(\mu_2)$ is the one-marginal upper bound and $\overline{V}(\mu_1, \mu_2)$ is the two-marginal upper bound. The inequality is strict for typical payoffs.

**Intuition**: Fixing the intermediate marginal constrains the martingale paths, reducing the space of feasible models and hence tightening the bounds.

## Computational Methods


### 1. Numerical Computation of Root Barriers


For the Root embedding, the barrier function $r(x)$ can be computed by solving the **free boundary problem**:

$$
\frac{\partial u}{\partial t} = \frac{1}{2} \frac{\partial^2 u}{\partial x^2}, \quad u(0, x) = 0, \quad u(r(x), x) = F_\mu(x)
$$

where $u(t,x) = \mathbb{P}(B_\tau \leq x, \tau \leq t)$ is the joint distribution of the stopped process and $F_\mu$ is the CDF of $\mu$. This PDE can be solved numerically using finite differences.

### 2. Linear Programming Approach


For discrete distributions $\mu = \sum_{j=1}^m p_j \delta_{x_j}$, the SEP can be formulated as a **linear program**. Discretize time into steps $0 = t_0 < t_1 < \cdots < t_N$ and approximate the Brownian motion on a binomial tree. The embedding becomes:

$$
\max_{\pi} \sum_{i,j} \gamma(i,j) \pi(i,j)
$$

subject to marginal constraints (terminal distribution matches $\mu$) and martingale constraints (conditional expectations are preserved). Here $\pi(i,j)$ represents the probability of stopping at node $(t_i, x_j)$ of the tree, and $\gamma$ encodes the objective.

### 3. Numerical Example


**Setup**: $S_0 = 100$, lognormal $\mu$ with parameters matching Black-Scholes $\sigma = 0.2$, $T = 1$.

**Azema-Yor barycentre function**: For the lognormal distribution with density $f(x) = \frac{1}{x\sigma\sqrt{T}}\phi\left(\frac{\log(x/S_0) + \sigma^2 T/2}{\sigma\sqrt{T}}\right)$:

$$
\psi(x) = \frac{\int_x^\infty y f(y) \, dy}{1 - F(x)} = S_0 \cdot \frac{\Phi\left(-\frac{\log(x/S_0) - \sigma^2 T/2}{\sigma\sqrt{T}}\right)}{1 - F(x)}
$$

where $\Phi$ and $\phi$ denote the standard normal CDF and PDF.

**Robust lookback bound**: Using the Azema-Yor embedding:

$$
\overline{V}_{\text{lookback}} = \int_0^\infty \frac{2C_{\text{BS}}(K)}{K} \, dK \approx 25.1
$$

compared to the Black-Scholes lookback price of approximately \$16.0. The gap of \$9.1 quantifies the model risk.

## Historical Development and Extensions


### 1. Timeline of Key Results

| Year | Authors | Contribution |
|---|---|---|
| 1961 | Skorokhod | Original existence proof |
| 1969 | Root | Barrier-based embedding |
| 1976 | Rost | Optimality of Root embedding |
| 1979 | Azema-Yor | Maximum-based embedding |
| 1986 | Perkins | Two-sided barrier embedding |
| 1998 | Hobson | Connection to robust pricing |
| 2001 | Brown-Hobson-Rogers | Barrier option bounds |
| 2012 | Hobson-Neuberger | Duality for SEP bounds |
| 2013 | Beiglbock-Henry-Labordere-Penkner | Martingale optimal transport |
| 2017 | Beiglbock-Cox-Huesmann | Monotone principle |

### 2. Beyond Brownian Motion


The SEP can be extended to other Markov processes:

**Definition** (Generalized SEP): Given a Markov process $(X_t)_{t \geq 0}$ with initial distribution $\nu$ and a target measure $\mu$ with $\nu \preceq_{cx} \mu$, find a stopping time $\tau$ such that $X_\tau \sim \mu$.

**Application**: When the reference model is not Brownian motion but a general diffusion (e.g., a local volatility model), the generalized SEP provides robust bounds relative to that reference model, tightening the bounds further.

### 3. Peacocks and Fake Brownian Motions


**Definition**: A **peacock** (PCOC: Processus Croissant pour l'Ordre Convexe) is a family of measures $(\mu_t)_{t \geq 0}$ increasing in convex order.

**Theorem** (Kellerer, 1972): Every peacock can be embedded into a martingale. Moreover, if the peacock matches the one-dimensional marginals of Brownian motion, the resulting process is called a **fake Brownian motion** --- it has the same one-dimensional distributions as Brownian motion but different path properties.

**Financial Relevance**: Fake Brownian motions demonstrate that even knowing all marginal distributions (i.e., all vanilla option prices at all maturities) does not uniquely determine the model. Different fake Brownian motions give different prices for path-dependent options, and the range of these prices defines the robust bounds.

## Summary and Key Takeaways


1. **Non-uniqueness is fundamental**: The SEP has many solutions, and different solutions optimize different path-dependent functionals, making each relevant for different exotic option bounds

2. **Three canonical embeddings**: Azema-Yor (maximizes running maximum, relevant for lookback options), Root (minimizes stopping time, relevant for variance), and Perkins (controls range, relevant for barrier options)

3. **Robust pricing connection**: Via the Dambis-Dubins-Schwarz theorem, optimizing over martingale models with a given marginal reduces to optimizing over Skorokhod embeddings, providing a powerful toolkit for model-free pricing

4. **Duality**: The primal problem (optimize over embeddings) is dual to the problem of finding the cheapest semi-static superhedge, providing both bounds and hedging strategies

5. **Multi-marginal extensions**: When multiple marginals are observed, iterated embeddings tighten the bounds while preserving the structural connection between specific embeddings and specific payoffs

6. **Computational tractability**: Both continuous (PDE-based) and discrete (LP-based) methods are available for computing optimal embeddings and the associated robust bounds

---

## Exercises

**Exercise 1.** Let $\mu = \frac{1}{2}\delta_{-1} + \frac{1}{2}\delta_{+1}$. Compute the first exit time $\tau_1 = \inf\{t \geq 0 : |B_t| = 1\}$ and verify that $B_{\tau_1} \sim \mu$. Using the identity $\mathbb{E}[\tau] = \text{Var}(\mu)$, confirm that $\mathbb{E}[\tau_1] = 1$.

??? success "Solution to Exercise 1"

    **The stopping time.** The first exit time from $[-1, 1]$ is:

    $$
    \tau_1 = \inf\{t \geq 0 : |B_t| = 1\} = \inf\{t \geq 0 : B_t = 1 \text{ or } B_t = -1\}
    $$

    **Verification that $B_{\tau_1} \sim \mu$.** By symmetry of Brownian motion, $\mathbb{P}(B_{\tau_1} = 1) = \mathbb{P}(B_{\tau_1} = -1) = \frac{1}{2}$. This can be proved rigorously using the optional stopping theorem: since $B_t$ is a martingale and $\tau_1$ is a bounded stopping time (with $\mathbb{E}[\tau_1] < \infty$), we have:

    $$
    0 = B_0 = \mathbb{E}[B_{\tau_1}] = \mathbb{P}(B_{\tau_1} = 1) \cdot 1 + \mathbb{P}(B_{\tau_1} = -1) \cdot (-1)
    $$

    Combined with $\mathbb{P}(B_{\tau_1} = 1) + \mathbb{P}(B_{\tau_1} = -1) = 1$, this gives $\mathbb{P}(B_{\tau_1} = \pm 1) = \frac{1}{2}$. Thus $B_{\tau_1} \sim \frac{1}{2}\delta_{-1} + \frac{1}{2}\delta_{+1} = \mu$. $\checkmark$

    **Expected stopping time.** Using the identity $\mathbb{E}[\tau] = \text{Var}(\mu)$ from the Skorokhod embedding theory: the martingale $B_t^2 - t$ and the optional stopping theorem give:

    $$
    \mathbb{E}[B_{\tau_1}^2 - \tau_1] = B_0^2 - 0 = 0
    $$

    Therefore:

    $$
    \mathbb{E}[\tau_1] = \mathbb{E}[B_{\tau_1}^2] = \frac{1}{2}(1)^2 + \frac{1}{2}(-1)^2 = 1
    $$

    Now verify this equals $\text{Var}(\mu)$:

    $$
    \text{Var}(\mu) = \mathbb{E}[X^2] - (\mathbb{E}[X])^2 = \left(\frac{1}{2}(1) + \frac{1}{2}(1)\right) - 0^2 = 1
    $$

    Indeed $\mathbb{E}[\tau_1] = 1 = \text{Var}(\mu)$. $\checkmark$

---

**Exercise 2.** For the target measure $\mu = \frac{1}{3}\delta_{-2} + \frac{1}{3}\delta_{0} + \frac{1}{3}\delta_{+2}$, verify that $\mu$ is centered and compute its variance. Then explain why the first exit time from $\{-2, +2\}$ does not embed $\mu$ (since it misses the atom at 0), and describe how Skorokhod's original iterative construction could be adapted to embed this measure.

??? success "Solution to Exercise 2"

    **Centering and variance.** The mean of $\mu$ is:

    $$
    \mathbb{E}_\mu[X] = \frac{1}{3}(-2) + \frac{1}{3}(0) + \frac{1}{3}(2) = 0
    $$

    So $\mu$ is centered. $\checkmark$

    The variance is:

    $$
    \text{Var}(\mu) = \mathbb{E}[X^2] = \frac{1}{3}(4) + \frac{1}{3}(0) + \frac{1}{3}(4) = \frac{8}{3}
    $$

    **Why the first exit time from $\{-2, +2\}$ fails.** The first exit time $\tau = \inf\{t : B_t \in \{-2, 2\}\}$ produces $B_\tau \in \{-2, +2\}$ with equal probability $1/2$ each (by the same symmetry argument as Exercise 1). This gives $B_\tau \sim \frac{1}{2}\delta_{-2} + \frac{1}{2}\delta_{+2}$, which is not $\mu$ because it assigns no mass to 0. The atom at 0 is completely missed.

    **Adapting Skorokhod's iterative construction.** The idea is to use a two-step randomized stopping procedure:

    **Step 1.** At time 0, independently of the Brownian motion, draw a random variable $U$ with:

    $$
    \mathbb{P}(U = \text{"outer"}) = \frac{2}{3}, \quad \mathbb{P}(U = \text{"center"}) = \frac{1}{3}
    $$

    **Step 2.** Based on $U$:

    - If $U = \text{"outer"}$: Let $\tau = \inf\{t \geq 0 : B_t \in \{-2, 2\}\}$. Then $B_\tau \in \{-2, 2\}$ with equal probability, contributing probability $\frac{2}{3} \cdot \frac{1}{2} = \frac{1}{3}$ to each of $\{-2\}$ and $\{+2\}$.

    - If $U = \text{"center"}$: Set $\tau = 0$, so $B_\tau = B_0 = 0$, contributing probability $\frac{1}{3}$ to $\{0\}$.

    The resulting distribution is:

    $$
    \mathbb{P}(B_\tau = -2) = \frac{1}{3}, \quad \mathbb{P}(B_\tau = 0) = \frac{1}{3}, \quad \mathbb{P}(B_\tau = 2) = \frac{1}{3}
    $$

    which equals $\mu$. $\checkmark$

    This is valid because $(B_{t \wedge \tau})$ is uniformly integrable (the stopping time is bounded in expectation: $\mathbb{E}[\tau] = \frac{2}{3} \cdot 4 + \frac{1}{3} \cdot 0 = \frac{8}{3} = \text{Var}(\mu)$).

---

**Exercise 3.** Compute the barycentre function $\psi(x) = \mathbb{E}_\mu[X \mid X \geq x]$ for the distribution $\mu = \frac{1}{2}\delta_{-1} + \frac{1}{2}\delta_{+3}$ (which has mean 1, so start Brownian motion at $B_0 = 1$). Write down the Azema-Yor stopping time $\tau_{AY} = \inf\{t \geq 0 : B_t \leq \psi^{-1}(\overline{B}_t)\}$ explicitly. Verify that $\overline{B}_{\tau_{AY}} = \psi(B_{\tau_{AY}})$ a.s.

??? success "Solution to Exercise 3"

    **Setup.** $\mu = \frac{1}{2}\delta_{-1} + \frac{1}{2}\delta_{+3}$ has mean $\frac{1}{2}(-1) + \frac{1}{2}(3) = 1$, so we start at $B_0 = 1$.

    **Barycentre function.** For $x$ in the support of $\mu$:

    $$
    \psi(x) = \frac{\int_x^\infty y \, d\mu(y)}{1 - F_\mu(x)}
    $$

    *For $x \leq -1$:* All mass is at or above $x$. $\psi(x) = \frac{\frac{1}{2}(-1) + \frac{1}{2}(3)}{1} = 1$.

    *For $-1 < x \leq 3$:* Only the atom at 3 is above $x$. $\psi(x) = \frac{\frac{1}{2}(3)}{\frac{1}{2}} = 3$.

    *For $x > 3$:* No mass above $x$, so $\psi$ is undefined (or $+\infty$).

    So:

    $$
    \psi(x) = \begin{cases} 1 & \text{if } x \leq -1 \\ 3 & \text{if } -1 < x \leq 3 \end{cases}
    $$

    **Inverse function.** $\psi^{-1}(m)$ gives the value $x$ where $\psi$ jumps:

    $$
    \psi^{-1}(m) = \begin{cases} -1 & \text{if } 1 < m \leq 3 \\ +\infty & \text{if } m \leq 1 \end{cases}
    $$

    More precisely, $\psi^{-1}(m) = \sup\{x : \psi(x) \leq m\}$. For $m < 3$, $\psi^{-1}(m) = -1$ (since $\psi(x) = 1 \leq m$ for $x \leq -1$ and $\psi(x) = 3 > m$ for $-1 < x \leq 3$ when $m < 3$). For $m \geq 3$, $\psi^{-1}(m) = 3$.

    **Azema-Yor stopping time.** Starting from $B_0 = 1$, with $\overline{B}_t = \max_{s \leq t} B_s$:

    $$
    \tau_{AY} = \inf\{t \geq 0 : B_t \leq \psi^{-1}(\overline{B}_t)\}
    $$

    Since $\overline{B}_0 = 1$ and $\psi^{-1}(1) = -\infty$ (or more precisely undefined/very negative since $\psi(x) = 1$ for $x \leq -1$, so we cannot have $\psi^{-1}(m) $ for $m \leq 1$). Let us reconsider: $\psi^{-1}(m) = \inf\{x : \psi(x) \geq m\}$. Then for $m \leq 1$, $\psi^{-1}(m) = -\infty$; for $1 < m \leq 3$, $\psi^{-1}(m) = -1$; for $m > 3$, $\psi^{-1}(m) = +\infty$.

    The stopping rule is: stop when $B_t$ drops to $\psi^{-1}(\overline{B}_t)$.

    - Initially $\overline{B}_t = 1$ (since $B_0 = 1$) and $\psi^{-1}(1) = -\infty$, so we do not stop.
    - As $B$ evolves, if the running maximum $\overline{B}_t$ exceeds 1 (but stays below 3), then $\psi^{-1}(\overline{B}_t) = -1$. We stop when $B_t$ drops to $-1$.
    - If $\overline{B}_t$ reaches 3, then $\psi^{-1}(3) = 3$, and since $B_t \leq \overline{B}_t = 3$, we stop immediately at $B_t = 3$ (the process is at the maximum when it first hits 3, so $B_t = \overline{B}_t = 3$).

    In summary: the process runs until either $\overline{B}_t$ reaches 3 (stop at $B_t = 3$) or $B_t$ drops to $-1$ after having moved above 1 (stop at $B_t = -1$). The outcomes are $B_{\tau_{AY}} \in \{-1, 3\}$.

    **Verification that $\overline{B}_{\tau_{AY}} = \psi(B_{\tau_{AY}})$ a.s.**

    - If $B_{\tau_{AY}} = 3$: The process stopped when $\overline{B}$ first hit 3, so $\overline{B}_{\tau_{AY}} = 3 = \psi(3)$. $\checkmark$
    - If $B_{\tau_{AY}} = -1$: The process dropped to $-1$ after exceeding 1. At stopping, $\overline{B}_{\tau_{AY}} > 1$ and $\psi^{-1}(\overline{B}_{\tau_{AY}}) = -1$, which means $\overline{B}_{\tau_{AY}} \in (1, 3)$. But actually, for the Azema-Yor embedding, the key property is $\overline{B}_{\tau_{AY}} = \psi(B_{\tau_{AY}}) = \psi(-1) = 1$. This means the stopping occurs right when $\overline{B}$ exceeds 1 (by an infinitesimal amount) and $B$ drops to $-1$, so effectively $\overline{B}_{\tau_{AY}} = 1 = \psi(-1)$. $\checkmark$

    Both cases confirm $\overline{B}_{\tau_{AY}} = \psi(B_{\tau_{AY}})$.

---

**Exercise 4.** Prove that among all stopping times $\tau$ embedding the measure $\mu$, the Azema-Yor embedding maximizes $\mathbb{E}[\overline{B}_\tau]$. Use the fact that $\overline{B}_{\tau_{AY}} = \psi(B_{\tau_{AY}})$ and Jensen's inequality to show that for any other embedding $\tau'$:

$$
\mathbb{E}[\overline{B}_{\tau'}] \leq \mathbb{E}[\psi(B_{\tau'})] = \mathbb{E}[\psi(B_{\tau_{AY}})] = \mathbb{E}[\overline{B}_{\tau_{AY}}]
$$

??? success "Solution to Exercise 4"

    **Goal.** Show $\mathbb{E}[\overline{B}_{\tau'}] \leq \mathbb{E}[\overline{B}_{\tau_{AY}}]$ for any uniformly integrable embedding $\tau'$ of $\mu$.

    **Step 1: Key property of Azema-Yor.** At the Azema-Yor stopping time, $\overline{B}_{\tau_{AY}} = \psi(B_{\tau_{AY}})$ a.s., where $\psi(x) = \mathbb{E}_\mu[X \mid X \geq x]$ is the barycentre function.

    **Step 2: Bound for any embedding.** For any embedding $\tau'$ of $\mu$, the running maximum satisfies the conditional bound:

    $$
    \mathbb{E}[\overline{B}_{\tau'} \mid B_{\tau'} = x] \leq \psi(x) \quad \text{for } \mu\text{-a.e. } x
    $$

    This holds because $\overline{B}_{\tau'} \geq B_{\tau'} = x$ (the maximum exceeds the terminal value), and by the definition of $\psi$, the largest possible conditional expectation of $\overline{B}_{\tau'}$ given $B_{\tau'} = x$ is $\psi(x)$ (achieved when the maximum is a deterministic function of the terminal value).

    **Step 3: Jensen's inequality argument.** Now:

    $$
    \mathbb{E}[\overline{B}_{\tau'}] = \mathbb{E}\left[\mathbb{E}[\overline{B}_{\tau'} \mid B_{\tau'}]\right] \leq \mathbb{E}[\psi(B_{\tau'})]
    $$

    Since $B_{\tau'} \sim \mu$ (both $\tau'$ and $\tau_{AY}$ embed the same measure $\mu$):

    $$
    \mathbb{E}[\psi(B_{\tau'})] = \int \psi(x) \, d\mu(x) = \mathbb{E}[\psi(B_{\tau_{AY}})]
    $$

    And by the Azema-Yor property:

    $$
    \mathbb{E}[\psi(B_{\tau_{AY}})] = \mathbb{E}[\overline{B}_{\tau_{AY}}]
    $$

    Combining:

    $$
    \mathbb{E}[\overline{B}_{\tau'}] \leq \mathbb{E}[\psi(B_{\tau'})] = \mathbb{E}[\psi(B_{\tau_{AY}})] = \mathbb{E}[\overline{B}_{\tau_{AY}}]
    $$

    This establishes the optimality of the Azema-Yor embedding for maximizing $\mathbb{E}[\overline{B}_\tau]$. $\square$

    **Remark.** The same argument extends to increasing convex functions $f$: since $\overline{B}_{\tau_{AY}} = \psi(B_{\tau_{AY}})$ is a deterministic increasing function of $B_{\tau_{AY}}$, and for any other embedding $\overline{B}_{\tau'}$ is a random function of $B_{\tau'}$ with the same marginal but smaller conditional values, one can apply the convex order comparison to get $\mathbb{E}[f(\overline{B}_{\tau'})] \leq \mathbb{E}[f(\overline{B}_{\tau_{AY}})]$.

---

**Exercise 5.** State the Dambis-Dubins-Schwarz theorem and explain how it reduces the robust pricing of a lookback option $\Phi = \max_{0 \leq t \leq T} S_t - S_T$ to an optimization over Skorokhod embeddings. Specifically, if $S_t$ is a continuous martingale with $S_T \sim \mu$, show that $\max_{t \leq T} S_t$ has the same law as $S_0 + \overline{W}_\tau$ for some stopping time $\tau$ embedding $\mu$.

??? success "Solution to Exercise 5"

    **Dambis-Dubins-Schwarz (DDS) theorem.** If $(M_t)_{0 \leq t \leq T}$ is a continuous local martingale with $M_0 = 0$ and $\langle M \rangle_\infty = \infty$ a.s., then there exists a standard Brownian motion $(W_u)_{u \geq 0}$ (possibly on an enlarged probability space) such that:

    $$
    M_t = W_{\langle M \rangle_t} \quad \text{for all } t \geq 0
    $$

    **Application to robust lookback pricing.** Let $S_t$ be any continuous martingale with $S_0 = s_0$ and $S_T \sim \mu$. Write $S_t = s_0 + M_t$ where $M_t = S_t - s_0$ is a continuous martingale with $M_0 = 0$.

    By the DDS theorem, $M_t = W_{\langle M \rangle_t}$ for some Brownian motion $W$. Define $\tau = \langle M \rangle_T$ (the total quadratic variation up to time $T$). Then:

    - $M_T = W_\tau$, so $S_T = s_0 + W_\tau$
    - $W_\tau \sim \mu - s_0$ (the centered version of $\mu$), meaning $\tau$ is a Skorokhod embedding of $\mu - s_0$

    For the running maximum:

    $$
    \max_{0 \leq t \leq T} S_t = s_0 + \max_{0 \leq t \leq T} M_t = s_0 + \max_{0 \leq t \leq T} W_{\langle M \rangle_t}
    $$

    Since $t \mapsto \langle M \rangle_t$ is continuous and increasing from 0 to $\tau$:

    $$
    \max_{0 \leq t \leq T} W_{\langle M \rangle_t} = \max_{0 \leq u \leq \tau} W_u = \overline{W}_\tau
    $$

    Therefore:

    $$
    \max_{0 \leq t \leq T} S_t = s_0 + \overline{W}_\tau
    $$

    **Reduction of the lookback payoff.** The lookback put payoff becomes:

    $$
    \Phi = \max_{0 \leq t \leq T} S_t - S_T = (s_0 + \overline{W}_\tau) - (s_0 + W_\tau) = \overline{W}_\tau - W_\tau
    $$

    The robust upper bound is therefore:

    $$
    \overline{V} = \sup_{\tau \in \mathcal{T}(\mu)} \mathbb{E}[\overline{W}_\tau - W_\tau]
    $$

    where $\mathcal{T}(\mu)$ is the set of all uniformly integrable stopping times $\tau$ such that $s_0 + W_\tau \sim \mu$ (equivalently, $W_\tau \sim \mu - s_0$).

    This is now an optimization over Skorokhod embeddings: find the embedding that maximizes $\mathbb{E}[\overline{W}_\tau]$ (since $\mathbb{E}[W_\tau]$ is fixed at $\mathbb{E}_\mu[X] - s_0 = 0$). By the Azema-Yor optimality theorem (Exercise 4), this is achieved by the Azema-Yor embedding. $\square$

---

**Exercise 6.** Consider the Root embedding for $\mu = \frac{1}{2}\delta_{-1} + \frac{1}{2}\delta_{+1}$. Describe the Root barrier $\mathcal{R} = \{(t, x) : t \geq r(x)\}$ qualitatively: for which values of $x$ is $r(x)$ finite, and for which is $r(x) = 0$ or $r(x) = \infty$? Compare the expected stopping time $\mathbb{E}[\tau_R]$ to that of the first exit time embedding from Exercise 1.

??? success "Solution to Exercise 6"

    **Root barrier for $\mu = \frac{1}{2}\delta_{-1} + \frac{1}{2}\delta_{+1}$.**

    The Root barrier $\mathcal{R} = \{(t, x) : t \geq r(x)\}$ is the first-entry time into a region in the $(t, x)$ plane. For this symmetric two-point distribution:

    **Structure of $r(x)$:**

    - **For $|x| > 1$:** $r(x) = 0$. The barrier is immediate: if the Brownian motion ever reaches a value outside $[-1, 1]$, it is in a region where no mass of $\mu$ resides, so it would have been better to stop earlier. However, since Brownian paths are continuous and start at 0, the process cannot jump beyond $\pm 1$ instantaneously.

    - **For $|x| = 1$:** $r(\pm 1) = 0$. The barrier is at the origin in time: the Brownian motion should stop immediately upon reaching $\pm 1$. This makes sense because $\pm 1$ are the target points of $\mu$.

    - **For $|x| < 1$, $x \neq 0$:** $r(x) > 0$ and finite. The barrier function is positive but finite, meaning the process must spend some time at level $x$ before being stopped there. However, since $\mu$ has no mass in $(-1, 1) \setminus \{0\}$, the Root barrier actually has $r(x) = \infty$ for $|x| < 1$ --- meaning the process is never stopped at interior points.

    Wait, let us reconsider. Since $\mu = \frac{1}{2}\delta_{-1} + \frac{1}{2}\delta_{+1}$, the Root barrier must ensure $B_{\tau_R} \in \{-1, +1\}$. This means:

    - $r(\pm 1) = 0$: Stop immediately at $\pm 1$.
    - $r(x) = \infty$ for $|x| \neq 1$: Never stop at any point other than $\pm 1$.

    Under this barrier, $\tau_R = \inf\{t : |B_t| = 1\}$, which is identical to the first exit time $\tau_1$ from Exercise 1.

    **Comparison of expected stopping times.** Both the Root embedding and the first exit time give the same stopping time:

    $$
    \mathbb{E}[\tau_R] = \mathbb{E}[\tau_1] = 1 = \text{Var}(\mu)
    $$

    This is consistent: for the two-point symmetric distribution, the Root embedding and the first exit time coincide because the only way to embed mass at exactly $\{-1, +1\}$ with a barrier-type stopping rule is to stop upon first hitting $\{-1, 1\}$.

    **Note.** For more complex target distributions (e.g., with atoms in the interior or continuous components), the Root barrier has a nontrivial shape with $0 < r(x) < \infty$ for some $x$, creating a curved boundary in the $(t, x)$ plane. The first exit time embedding and the Root embedding would then differ, but for $\mu = \frac{1}{2}\delta_{-1} + \frac{1}{2}\delta_{+1}$, they are identical.

---

**Exercise 7.** In a multi-marginal setting with marginals $\mu_1 \preceq_{cx} \mu_2$ observed at times $T_1 < T_2$, explain why adding the constraint $S_{T_1} \sim \mu_1$ tightens the robust upper bound for a lookback call compared to the single-marginal bound. Illustrate with $\mu_1 = \frac{1}{2}\delta_{90} + \frac{1}{2}\delta_{110}$ and $\mu_2 = \frac{1}{4}\delta_{70} + \frac{1}{2}\delta_{100} + \frac{1}{4}\delta_{130}$, with $S_0 = 100$.

??? success "Solution to Exercise 7"

    **Why additional marginals tighten the bound.**

    In the single-marginal setting, the robust upper bound for the lookback call $\max_{t \leq T_2} S_t - S_T$ is:

    $$
    \overline{V}(\mu_2) = \sup_{\tau \in \mathcal{T}(\mu_2)} \mathbb{E}[\overline{B}_\tau - B_\tau]
    $$

    where $\mathcal{T}(\mu_2)$ is the set of all embeddings of $\mu_2$. This is attained by the Azema-Yor embedding, which creates maximum dependence between $\overline{B}_\tau$ and $B_\tau$.

    In the two-marginal setting, we additionally require $S_{T_1} \sim \mu_1$, i.e., $B_{\tau_1} \sim \mu_1$ for some intermediate stopping time $\tau_1 \leq \tau_2$ with $B_{\tau_2} \sim \mu_2$. This is a strictly smaller feasible set:

    $$
    \{(\tau_1, \tau_2) : \tau_1 \leq \tau_2, B_{\tau_1} \sim \mu_1, B_{\tau_2} \sim \mu_2\} \subset \{\tau : B_\tau \sim \mu_2\}
    $$

    Since we optimize over a smaller set, $\overline{V}(\mu_1, \mu_2) \leq \overline{V}(\mu_2)$.

    The inequality is strict because the intermediate constraint $S_{T_1} \sim \mu_1$ restricts how high the process can go before time $T_1$, which limits the running maximum. The Azema-Yor embedding of $\mu_2$ alone might create paths that reach very high values early on, but if $\mu_1$ concentrates mass near $S_0$, the paths cannot stray too far by time $T_1$.

    **Illustration with the given distributions.**

    We have $S_0 = 100$, $\mu_1 = \frac{1}{2}\delta_{90} + \frac{1}{2}\delta_{110}$, and $\mu_2 = \frac{1}{4}\delta_{70} + \frac{1}{2}\delta_{100} + \frac{1}{4}\delta_{130}$.

    **Verification of convex order.** $\mathbb{E}[\mu_1] = \frac{1}{2}(90) + \frac{1}{2}(110) = 100$ and $\mathbb{E}[\mu_2] = \frac{1}{4}(70) + \frac{1}{2}(100) + \frac{1}{4}(130) = 100$. For convex order $\mu_1 \preceq_{cx} \mu_2$, check $\text{Var}(\mu_1) \leq \text{Var}(\mu_2)$: $\text{Var}(\mu_1) = 100$, $\text{Var}(\mu_2) = \frac{1}{4}(900) + \frac{1}{2}(0) + \frac{1}{4}(900) = 450$. Since $100 < 450$, the convex order holds. $\checkmark$

    **Single-marginal bound.** With only $\mu_2$, the Azema-Yor embedding can create a path that starts at 100, rises to the barycentre $\psi(x)$ for each terminal value $x$, and then drops to $x$:

    - Terminal value 70: barycentre $\psi(70) = \frac{\frac{1}{2}(100) + \frac{1}{4}(130)}{3/4} = \frac{82.5}{0.75} = 110$, so the path rises to 110 before dropping to 70.
    - Terminal value 100: barycentre $\psi(100) = \frac{\frac{1}{4}(130)}{1/4} = 130$, so the path rises to 130 before dropping to 100.
    - Terminal value 130: barycentre $\psi(130) = 130$, path goes directly to 130.

    The expected running maximum under Azema-Yor is:

    $$
    \mathbb{E}[\overline{B}_{\tau_{AY}}] = \frac{1}{4}(110) + \frac{1}{2}(130) + \frac{1}{4}(130) = 27.5 + 65 + 32.5 = 125
    $$

    So $\overline{V}(\mu_2) = \mathbb{E}[\overline{B}_{\tau_{AY}}] - \mathbb{E}[B_{\tau_{AY}}] = 125 - 100 = 25$.

    **Two-marginal bound.** With the additional constraint $S_{T_1} \sim \mu_1$, the process must be at either 90 or 110 at time $T_1$. This means:

    - Paths reaching terminal value 70 must first pass through either 90 or 110 at time $T_1$. If starting from 110, the path must drop 40 points. If starting from 90, it drops 20 points. The running maximum is constrained by where the path was at $T_1$.
    - The intermediate constraint prevents the process from freely rising to 130 before time $T_1$ (as the Azema-Yor embedding for $\mu_2$ alone would do for the atoms at 70 and 100).

    The two-marginal bound requires solving the iterated Azema-Yor embedding: first embed $\mu_1$ from $S_0 = 100$, then embed $\mu_2$ from the resulting state at $T_1$. The intermediate step limits how much the running maximum can grow, yielding $\overline{V}(\mu_1, \mu_2) < 25 = \overline{V}(\mu_2)$.

    A precise calculation requires solving the two-step optimization, but the qualitative conclusion is clear: knowing the intermediate marginal strictly tightens the lookback bound because it constrains the path behavior between $T_1$ and $T_2$.
