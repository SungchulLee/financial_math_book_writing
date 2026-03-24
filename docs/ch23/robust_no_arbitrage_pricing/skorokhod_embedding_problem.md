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

---

**Exercise 2.** For the target measure $\mu = \frac{1}{3}\delta_{-2} + \frac{1}{3}\delta_{0} + \frac{1}{3}\delta_{+2}$, verify that $\mu$ is centered and compute its variance. Then explain why the first exit time from $\{-2, +2\}$ does not embed $\mu$ (since it misses the atom at 0), and describe how Skorokhod's original iterative construction could be adapted to embed this measure.

---

**Exercise 3.** Compute the barycentre function $\psi(x) = \mathbb{E}_\mu[X \mid X \geq x]$ for the distribution $\mu = \frac{1}{2}\delta_{-1} + \frac{1}{2}\delta_{+3}$ (which has mean 1, so start Brownian motion at $B_0 = 1$). Write down the Azema-Yor stopping time $\tau_{AY} = \inf\{t \geq 0 : B_t \leq \psi^{-1}(\overline{B}_t)\}$ explicitly. Verify that $\overline{B}_{\tau_{AY}} = \psi(B_{\tau_{AY}})$ a.s.

---

**Exercise 4.** Prove that among all stopping times $\tau$ embedding the measure $\mu$, the Azema-Yor embedding maximizes $\mathbb{E}[\overline{B}_\tau]$. Use the fact that $\overline{B}_{\tau_{AY}} = \psi(B_{\tau_{AY}})$ and Jensen's inequality to show that for any other embedding $\tau'$:

$$
\mathbb{E}[\overline{B}_{\tau'}] \leq \mathbb{E}[\psi(B_{\tau'})] = \mathbb{E}[\psi(B_{\tau_{AY}})] = \mathbb{E}[\overline{B}_{\tau_{AY}}]
$$

---

**Exercise 5.** State the Dambis-Dubins-Schwarz theorem and explain how it reduces the robust pricing of a lookback option $\Phi = \max_{0 \leq t \leq T} S_t - S_T$ to an optimization over Skorokhod embeddings. Specifically, if $S_t$ is a continuous martingale with $S_T \sim \mu$, show that $\max_{t \leq T} S_t$ has the same law as $S_0 + \overline{W}_\tau$ for some stopping time $\tau$ embedding $\mu$.

---

**Exercise 6.** Consider the Root embedding for $\mu = \frac{1}{2}\delta_{-1} + \frac{1}{2}\delta_{+1}$. Describe the Root barrier $\mathcal{R} = \{(t, x) : t \geq r(x)\}$ qualitatively: for which values of $x$ is $r(x)$ finite, and for which is $r(x) = 0$ or $r(x) = \infty$? Compare the expected stopping time $\mathbb{E}[\tau_R]$ to that of the first exit time embedding from Exercise 1.

---

**Exercise 7.** In a multi-marginal setting with marginals $\mu_1 \preceq_{cx} \mu_2$ observed at times $T_1 < T_2$, explain why adding the constraint $S_{T_1} \sim \mu_1$ tightens the robust upper bound for a lookback call compared to the single-marginal bound. Illustrate with $\mu_1 = \frac{1}{2}\delta_{90} + \frac{1}{2}\delta_{110}$ and $\mu_2 = \frac{1}{4}\delta_{70} + \frac{1}{2}\delta_{100} + \frac{1}{4}\delta_{130}$, with $S_0 = 100$.
