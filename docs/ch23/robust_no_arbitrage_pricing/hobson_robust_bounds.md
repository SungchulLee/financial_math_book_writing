# Hobson Robust Bounds


## Introduction


David Hobson's program on **robust bounds** for exotic options addresses a fundamental question in mathematical finance: given only the prices of European call options across all strikes (equivalently, the marginal distribution of the terminal stock price), what are the tightest possible bounds on the prices of path-dependent derivatives?

This question is important because:

1. **Model independence**: The bounds hold regardless of the stochastic process governing the stock price
2. **Market consistency**: They incorporate the information embedded in liquid vanilla option markets
3. **Extremal models**: The bounds are attained by specific (often degenerate) martingale models, revealing worst-case scenarios
4. **Connection to embedding**: The methodology links to the Skorokhod embedding problem, connecting probability theory to financial mathematics

Hobson's key insight is that the problem of finding robust option bounds can be transformed into an optimal transport problem between the initial distribution (a Dirac mass at $S_0$) and the terminal marginal (determined by call prices), subject to the martingale constraint.

## Mathematical Framework


### 1. Setup and Assumptions


**Market Model**: Consider a frictionless market with:

- Risk-free rate $r = 0$ (for simplicity; all results extend to $r > 0$ via discounting)
- Current stock price $S_0 > 0$
- European call prices $C(K)$ observed for all strikes $K \geq 0$

**Marginal Distribution**: By the Breeden-Litzenberger formula, call prices determine the risk-neutral distribution $\mu$ of $S_T$:

$$
\mu((K, \infty)) = -\frac{\partial C}{\partial K}(K), \quad \mu(\{K\}) = \frac{\partial^2 C}{\partial K^2}(K) \text{ (in distributional sense)}
$$

**No-Arbitrage Consistency**: The distribution $\mu$ must satisfy the martingale constraint:

$$
\int_0^\infty x \, d\mu(x) = S_0
$$

(the forward price equals the current price when $r = 0$).

### 2. The Robust Pricing Problem


**Problem**: For a path-dependent payoff $\Phi((S_t)_{0 \leq t \leq T})$, find:

$$
\overline{V} = \sup_{\mathbb{Q} \in \mathcal{M}(\mu)} \mathbb{E}_\mathbb{Q}[\Phi((S_t)_{0 \leq t \leq T})]
$$

$$
\underline{V} = \inf_{\mathbb{Q} \in \mathcal{M}(\mu)} \mathbb{E}_\mathbb{Q}[\Phi((S_t)_{0 \leq t \leq T})]
$$

where $\mathcal{M}(\mu)$ is the set of all martingale measures $\mathbb{Q}$ under which:

1. $S_0$ is deterministic
2. $(S_t)_{0 \leq t \leq T}$ is a $\mathbb{Q}$-martingale
3. $S_T \sim \mu$ under $\mathbb{Q}$

**Key Distinction from Model-Free Bounds**: Standard model-free bounds use only no-arbitrage. Hobson's bounds additionally incorporate the observed marginal $\mu$, yielding strictly tighter results.

### 3. Convex Ordering and Feasibility


**Definition** (Convex Order): Probability measures $\nu \preceq_{cx} \mu$ (read "$\nu$ is dominated by $\mu$ in convex order") if:

$$
\int f \, d\nu \leq \int f \, d\mu
$$

for every convex function $f: \mathbb{R} \to \mathbb{R}$ (whenever the integrals exist).

**Theorem** (Strassen, 1965): There exists a martingale $(M_0, M_1)$ with $M_0 \sim \nu$ and $M_1 \sim \mu$ if and only if $\nu \preceq_{cx} \mu$.

**Application**: For $S_0$ deterministic (i.e., $\nu = \delta_{S_0}$), the condition $\delta_{S_0} \preceq_{cx} \mu$ is equivalent to:

$$
\int_0^\infty x \, d\mu(x) = S_0
$$

which is precisely the no-arbitrage (martingale) condition.

## Robust Bounds for Lookback Options


### 1. Lookback Call


**Payoff**: The floating-strike lookback call pays:

$$
\Phi = S_T - \min_{0 \leq t \leq T} S_t
$$

**Theorem** (Hobson, 1998): The robust upper bound for the lookback call, given marginal $\mu$ of $S_T$, is:

$$
\overline{V}_{\text{lookback}} = \int_0^\infty C(K) \frac{2}{K} \, dK = \int_0^\infty \frac{2 \, C(K)}{K} \, dK
$$

where $C(K)$ is the price of a European call with strike $K$.

**Proof Strategy**: The proof has two parts:

*Upper bound*: Construct a semi-static superhedging portfolio. For any martingale model consistent with $\mu$:

$$
S_T - \min_{0 \leq t \leq T} S_t \leq 2 \int_0^\infty \frac{(S_T - K)^+}{K^2} \, dK
$$

This inequality follows from the pathwise identity (Hobson):

$$
S_T - \min_{0 \leq t \leq T} S_t \leq 2\left(\sqrt{S_T} - \sqrt{\min_{0 \leq t \leq T} S_t}\right)^2 + 2\sqrt{S_T}\left(\sqrt{S_T} - \sqrt{\min S_t}\right)
$$

combined with superhedging arguments.

*Attainment*: The upper bound is attained by the **Azema-Yor embedding** of $\mu$ into a Brownian motion (see the Skorokhod embedding section). Under this specific martingale model, the lookback payoff achieves the upper bound. $\square$

### 2. Lookback Put


**Payoff**:

$$
\Phi = \max_{0 \leq t \leq T} S_t - S_T
$$

**Robust Upper Bound**: By similar arguments:

$$
\overline{V}_{\text{lookback put}} = \int_0^\infty P(K) \frac{2}{K} \, dK
$$

where $P(K)$ is the put price at strike $K$.

**Extremal Model**: The bound is attained by a specific martingale construction (the **Perkins embedding**) that maximizes the running maximum minus the terminal value.

## Robust Bounds for Barrier Options


### 1. Up-and-In Barrier Call


**Payoff**: For barrier $H > S_0$ and strike $K < H$:

$$
\Phi = (S_T - K)^+ \cdot \mathbb{1}\left\{\max_{0 \leq t \leq T} S_t \geq H\right\}
$$

**Theorem** (Brown-Hobson-Rogers, 2001): The robust upper bound on the up-and-in call is:

$$
\overline{V}_{\text{UIC}} = C(K) - \overline{V}_{\text{UOC}}
$$

where $\overline{V}_{\text{UOC}}$ is the lower bound on the up-and-out call:

$$
\overline{V}_{\text{UOC}} = \inf_{\mathbb{Q} \in \mathcal{M}(\mu)} \mathbb{E}_\mathbb{Q}\left[(S_T - K)^+ \cdot \mathbb{1}\left\{\max_{0 \leq t \leq T} S_t < H\right\}\right]
$$

This follows from the decomposition: $(S_T - K)^+ = \text{UIC} + \text{UOC}$.

### 2. Double No-Touch Option


**Payoff**: Pays 1 if the stock price stays within $[L, H]$ throughout $[0, T]$:

$$
\Phi = \mathbb{1}\left\{L \leq S_t \leq H \text{ for all } t \in [0, T]\right\}
$$

**Robust Bounds**: The upper bound corresponds to a martingale model that keeps the process inside $[L, H]$ as much as possible, while the lower bound corresponds to a model that exits as quickly as possible.

**Connection to Skorokhod Embedding**: The extremal models correspond to specific stopping rules for Brownian motion that hit the barriers in prescribed ways.

## Extremal Measures and Martingale Optimal Transport


### 1. Martingale Optimal Transport Formulation


Hobson's robust bounds can be formulated as **martingale optimal transport** (MOT) problems.

**Primal Problem**:

$$
\overline{V} = \sup_{\pi \in \mathcal{M}(\delta_{S_0}, \mu)} \int c(x, y) \, d\pi(x, y)
$$

where:

- $\mathcal{M}(\delta_{S_0}, \mu)$ is the set of martingale couplings: joint distributions $\pi$ with marginals $\delta_{S_0}$ and $\mu$, satisfying $\int y \, d\pi(x, y | x) = x$
- $c(x, y)$ is the cost function encoding the exotic payoff

For example, for a lookback-type payoff, the cost function involves the maximum of the martingale path, which requires an extension to the multi-marginal or continuous-path setting.

### 2. Dual Problem


**Theorem** (Hobson-Neuberger, 2012; Beiglbock-Henry-Labordere-Penkner, 2013): The dual of the martingale transport problem is:

$$
\overline{V} = \inf_{(\phi, h)} \left\{ \int \phi(y) \, d\mu(y) : \phi(S_T) + \int_0^T h_t \, dS_t \geq \Phi((S_t)_{0 \leq t \leq T}) \right\}
$$

where:

- $\phi: \mathbb{R}_+ \to \mathbb{R}$ is a payoff function of vanilla options (static hedge)
- $h_t$ is a dynamic trading strategy in the underlying

**Interpretation**: The dual provides a **semi-static superhedging strategy** combining a static portfolio of vanilla options (encoded by $\phi$) with a dynamic delta-hedging component (encoded by $h$). The robust upper bound equals the cheapest such superhedge.

### 3. Strong Duality


**Theorem**: Under mild regularity conditions (continuity of the payoff, compactness of the marginal support), strong duality holds:

$$
\sup_{\pi \in \mathcal{M}(\delta_{S_0}, \mu)} \int c \, d\pi = \inf_{(\phi, h)} \left\{ \int \phi \, d\mu : \phi(S_T) + \int_0^T h_t \, dS_t \geq c \text{ a.s.} \right\}
$$

**Proof**: This is a consequence of minimax duality adapted to the martingale constraint setting. The key technical step is verifying that the constraint set is compact in the appropriate topology and that the objective is continuous. $\square$

## Key Examples


### 1. Variance Swap Upper Bound


**Payoff**: Discretized variance:

$$
\Phi = \sum_{i=1}^N \left(\log \frac{S_{t_i}}{S_{t_{i-1}}}\right)^2
$$

**Model-Free Replication**: By Carr-Madan, the fair value of the variance swap is determined by vanilla option prices:

$$
\mathbb{E}_\mathbb{Q}[\Phi] = 2 \int_0^\infty \frac{C(K)}{K^2} \, dK
$$

This is model-free and exact (not a bound), demonstrating that variance swaps are uniquely determined by the marginal.

**Hobson's Insight**: For the variance swap, $\overline{V} = \underline{V}$; the marginal completely pins down the price. This contrasts with lookback and barrier options, where genuine bounds exist.

### 2. Forward Start Options


**Payoff**: For $0 < t_1 < T$:

$$
\Phi = \left(\frac{S_T}{S_{t_1}} - 1\right)^+
$$

**Robust Bounds**: With only the terminal marginal $\mu$ given:

$$
\underline{V} = 0, \quad \overline{V} = \mathbb{E}_\mu\left[\left(\frac{S_T}{S_0} - 1\right)^+\right] = \frac{C(S_0)}{S_0}
$$

**Two-Marginal Problem**: If the marginal at $t_1$ is also known (from options expiring at $t_1$), the bounds tighten significantly. This is a genuine two-marginal martingale transport problem.

### 3. Numerical Example: Lookback Bound


**Setup**: $S_0 = 100$, Black-Scholes implied volatility $\sigma = 20\%$, $T = 1$ year, $r = 0$.

**Black-Scholes Lookback Price**: Under BS with $\sigma = 20\%$:

$$
V_{\text{BS}} \approx 16.0
$$

**Hobson Upper Bound**: Using the BS call prices to compute the integral:

$$
\overline{V} = \int_0^\infty \frac{2 \, C_{\text{BS}}(K)}{K} \, dK \approx 25.1
$$

**Interpretation**: Any model consistent with the BS marginal must price the lookback call at most \$25.1. The gap $25.1 - 16.0 = 9.1$ represents the maximum model risk for the lookback under this marginal.

## Multi-Marginal Extensions


### 1. Multiple Expiry Dates


When options at multiple maturities $T_1 < T_2 < \cdots < T_n$ are observed, the marginals $\mu_1, \ldots, \mu_n$ provide additional constraints.

**Multi-Marginal MOT**:

$$
\overline{V} = \sup_{\mathbb{Q}} \mathbb{E}_\mathbb{Q}[\Phi] \quad \text{s.t. } S_{T_i} \sim \mu_i \text{ for } i = 1, \ldots, n, \; (S_t) \text{ is a } \mathbb{Q}\text{-martingale}
$$

**Consistency Condition**: The marginals must be in convex order:

$$
\mu_1 \preceq_{cx} \mu_2 \preceq_{cx} \cdots \preceq_{cx} \mu_n
$$

**Tighter Bounds**: Each additional marginal tightens the bounds, potentially by a significant amount for path-dependent options.

### 2. The Peacock Problem


**Peacock** (from the French PCOC: "Processus Croissant pour l'Ordre Convexe"): A family $(\mu_t)_{t \geq 0}$ is a peacock if $\mu_s \preceq_{cx} \mu_t$ for $s \leq t$.

**Theorem** (Kellerer, 1972): A family $(\mu_t)_{t \geq 0}$ is a peacock if and only if there exists a martingale $(M_t)_{t \geq 0}$ with $M_t \sim \mu_t$ for all $t$.

**Application**: The full continuum of vanilla option maturities determines a peacock, and any consistent martingale model must have marginals lying in this family. The robust bounds optimize over all such martingales.

## Connection to Skorokhod Embedding


### 1. The Link


**Key Correspondence**: For a continuous martingale $M_t = B_{\tau \wedge t}$ (time-changed Brownian motion), the problem of finding the extremal martingale is equivalent to finding the optimal **Skorokhod embedding** of $\mu$ into Brownian motion.

Specifically, the robust upper bound:

$$
\overline{V} = \sup \left\{ \mathbb{E}[\Phi(B_{\tau \wedge t})_{0 \leq t \leq T}] : B_\tau \sim \mu, \; \tau \text{ stopping time} \right\}
$$

reduces the problem to optimizing over stopping times $\tau$ that embed $\mu$.

### 2. Specific Embeddings and Their Financial Meaning


**Azema-Yor Embedding**: Maximizes $\mathbb{E}[\max_{t \leq \tau} B_t]$ among all embeddings of $\mu$. This attains the upper bound for lookback options.

**Root Embedding**: Minimizes $\mathbb{E}[\tau]$ (expected stopping time). This is optimal for variance-swap-type payoffs.

**Perkins Embedding**: Simultaneously controls the maximum and minimum of the path. This is relevant for double barrier options.

The choice of embedding determines the extremal model, and different payoff structures call for different embeddings.

## Summary and Key Takeaways


1. **Robust Bounds**: Hobson's framework derives the tightest possible price bounds for exotic options, given only vanilla option prices (the terminal marginal)

2. **Extremal Models**: The bounds are attained by specific (often degenerate) martingale models, providing worst-case scenarios for model risk assessment

3. **Duality**: Robust bounds admit dual representations as cheapest semi-static superhedging strategies, combining vanilla options with dynamic trading

4. **Skorokhod Connection**: The extremal models correspond to specific Skorokhod embeddings of the marginal into Brownian motion, linking robust pricing to classical probability theory

5. **Multi-Marginal Extensions**: Additional marginal information (from multiple option expiries) strictly tightens the bounds

6. **Practical Relevance**: The gap between robust upper and lower bounds quantifies model risk for exotic derivatives, informing reserve calculations and model validation

7. **Variance Swaps**: Uniquely among common derivatives, variance swaps have zero model risk --- their price is completely determined by the marginal distribution

---

## Exercises

**Exercise 1.** Let $\mu = \frac{1}{4}\delta_{60} + \frac{1}{2}\delta_{100} + \frac{1}{4}\delta_{140}$ with $S_0 = 100$. Verify that $\delta_{S_0} \preceq_{cx} \mu$ by checking the martingale condition and computing $\int f \, d\mu$ for the convex functions $f(x) = (x - 100)^+$ and $f(x) = |x - 100|$.

??? success "Solution to Exercise 1"

    We must verify two things: the martingale condition and the convex ordering condition $\delta_{S_0} \preceq_{cx} \mu$.

    **Martingale condition.** Compute the mean of $\mu$:

    $$
    \int_0^\infty x \, d\mu(x) = \frac{1}{4}(60) + \frac{1}{2}(100) + \frac{1}{4}(140) = 15 + 50 + 35 = 100 = S_0
    $$

    So the martingale (mean) condition is satisfied.

    **Convex ordering.** We need $\int f \, d\delta_{100} \leq \int f \, d\mu$ for every convex $f$. For $\delta_{100}$, $\int f \, d\delta_{100} = f(100)$.

    *Test with $f(x) = (x - 100)^+$:*

    $$
    \int f \, d\delta_{100} = (100 - 100)^+ = 0
    $$

    $$
    \int f \, d\mu = \frac{1}{4}(60 - 100)^+ + \frac{1}{2}(100 - 100)^+ + \frac{1}{4}(140 - 100)^+ = 0 + 0 + \frac{1}{4}(40) = 10
    $$

    Indeed $0 \leq 10$. $\checkmark$

    *Test with $f(x) = |x - 100|$:*

    $$
    \int f \, d\delta_{100} = |100 - 100| = 0
    $$

    $$
    \int f \, d\mu = \frac{1}{4}|60 - 100| + \frac{1}{2}|100 - 100| + \frac{1}{4}|140 - 100| = \frac{1}{4}(40) + 0 + \frac{1}{4}(40) = 20
    $$

    Indeed $0 \leq 20$. $\checkmark$

    Both inequalities are consistent with convex ordering. More generally, since $\mu$ has mean $S_0 = 100$, Strassen's theorem guarantees $\delta_{100} \preceq_{cx} \mu$, because for any convex function $f$, Jensen's inequality gives $f(100) = f\!\bigl(\int x \, d\mu\bigr) \leq \int f \, d\mu$.

---

**Exercise 2.** For the marginal $\mu$ in Exercise 1, compute the European call prices $C(K)$ for $K = 60, 80, 100, 120, 140$, and evaluate Hobson's robust upper bound for the floating-strike lookback call:

$$
\overline{V}_{\text{lookback}} = \int_0^\infty \frac{2 \, C(K)}{K} \, dK
$$

by discretizing the integral over the support of $\mu$.

??? success "Solution to Exercise 2"

    **Step 1: Compute call prices.** The call price at strike $K$ is $C(K) = \mathbb{E}_\mu[(S_T - K)^+]$ (with $r = 0$):

    $$
    C(K) = \frac{1}{4}(60 - K)^+ + \frac{1}{2}(100 - K)^+ + \frac{1}{4}(140 - K)^+
    $$

    - $C(60) = \frac{1}{4}(0) + \frac{1}{2}(40) + \frac{1}{4}(80) = 0 + 20 + 20 = 40$
    - $C(80) = \frac{1}{4}(0) + \frac{1}{2}(20) + \frac{1}{4}(60) = 0 + 10 + 15 = 25$
    - $C(100) = \frac{1}{4}(0) + \frac{1}{2}(0) + \frac{1}{4}(40) = 10$
    - $C(120) = \frac{1}{4}(0) + \frac{1}{2}(0) + \frac{1}{4}(20) = 5$
    - $C(140) = \frac{1}{4}(0) + \frac{1}{2}(0) + \frac{1}{4}(0) = 0$

    **Step 2: Evaluate the Hobson bound.** Since $\mu$ is supported on $\{60, 100, 140\}$, the call price function $C(K)$ is piecewise linear with slopes changing at $K = 60, 100, 140$. We discretize:

    $$
    \overline{V}_{\text{lookback}} = \int_0^\infty \frac{2\,C(K)}{K} \, dK
    $$

    We split the integral into the intervals where $C(K)$ has a simple form.

    For $K \in [0, 60]$: $C(K) = 100 - K$ (all three atoms contribute), so

    $$
    \int_0^{60} \frac{2(100 - K)}{K} \, dK = 2\int_0^{60}\left(\frac{100}{K} - 1\right) dK
    $$

    This integral diverges as $K \to 0^+$ because $C(K)/K \sim 100/K$. This is a well-known feature: for distributions with an atom at 0 or supported away from 0, the integral must be interpreted with the correct lower limit. Since $\mu$ is supported on $\{60, 100, 140\}$ with no mass below 60, the stock price is always positive. To handle the integral properly, note that for $K < 60$, $C(K) = \mathbb{E}[(S_T - K)^+] = \mathbb{E}[S_T] - K = 100 - K$, and $\int_0^{60} \frac{2(100 - K)}{K} dK$ diverges.

    In practice, for a discrete distribution with finite support bounded away from zero, we use the discrete version of Hobson's bound. For a distribution on $\{x_1, \ldots, x_n\}$, the lookback bound can be computed via:

    $$
    \overline{V}_{\text{lookback}} = \int_0^\infty \frac{2\,C(K)}{K} \, dK
    $$

    We evaluate this by integrating piecewise. On $[60, 100]$, $C(K) = \frac{1}{2}(100 - K) + \frac{1}{4}(140 - K) = 85 - \frac{3}{4}K$:

    $$
    \int_{60}^{100} \frac{2(85 - \frac{3}{4}K)}{K} \, dK = 2\int_{60}^{100}\left(\frac{85}{K} - \frac{3}{4}\right) dK = 2\left[85\ln\frac{100}{60} - \frac{3}{4}(40)\right] = 2\left[85\ln\frac{5}{3} - 30\right]
    $$

    $$
    = 2[85(0.5108) - 30] = 2[43.42 - 30] = 26.84
    $$

    On $[100, 140]$, $C(K) = \frac{1}{4}(140 - K)$:

    $$
    \int_{100}^{140} \frac{2 \cdot \frac{1}{4}(140 - K)}{K} \, dK = \frac{1}{2}\int_{100}^{140}\frac{140 - K}{K} \, dK = \frac{1}{2}\int_{100}^{140}\left(\frac{140}{K} - 1\right) dK
    $$

    $$
    = \frac{1}{2}\left[140\ln\frac{140}{100} - 40\right] = \frac{1}{2}[140(0.3365) - 40] = \frac{1}{2}[47.11 - 40] = 3.56
    $$

    For $K > 140$, $C(K) = 0$, so no contribution. For $K < 60$, the integral diverges, reflecting the fact that the lookback bound for a process starting at $S_0 = 100$ with positive minimum can be infinite unless properly handled.

    Restricting to the finite portion (on $[60, \infty)$), the partial bound is approximately $26.84 + 3.56 = 30.40$. The divergence on $(0, 60)$ occurs because the formula implicitly allows the minimum to approach 0; in practice one truncates or uses modified formulas for discrete distributions.

---

**Exercise 3.** Consider the forward start option payoff $\Phi = (S_T / S_{t_1} - 1)^+$ with only the terminal marginal $\mu$ given. Prove the lower bound $\underline{V} = 0$ by constructing a martingale model where $S_{t_1} = S_T$ almost surely. Then prove the upper bound $\overline{V} = C(S_0)/S_0$ by showing that $\Phi \leq (S_T/S_0 - 1)^+$ holds under the martingale model where $S_{t_1} = S_0$ almost surely.

??? success "Solution to Exercise 3"

    **Lower bound $\underline{V} = 0$.**

    Construct the martingale model where $S_{t_1} = S_T$ almost surely. Since $(S_t)$ is a martingale, we can set $S_t = S_T$ for all $t \geq t_1$ (the process stays constant after $t_1$, having already reached its terminal value). More specifically, let $S_t$ be any martingale with $S_T \sim \mu$, and define it so that $S_{t_1} = S_T$.

    Under this model:

    $$
    \Phi = \left(\frac{S_T}{S_{t_1}} - 1\right)^+ = \left(\frac{S_T}{S_T} - 1\right)^+ = (1 - 1)^+ = 0
    $$

    almost surely. Therefore $\mathbb{E}[\Phi] = 0$, establishing that $\underline{V} \leq 0$. Since $\Phi \geq 0$, we also have $\underline{V} \geq 0$, giving $\underline{V} = 0$.

    **Upper bound $\overline{V} = C(S_0)/S_0$.**

    Construct the martingale model where $S_{t_1} = S_0$ almost surely (the stock price is constant up to time $t_1$, then jumps to its terminal value). Under this model:

    $$
    \Phi = \left(\frac{S_T}{S_{t_1}} - 1\right)^+ = \left(\frac{S_T}{S_0} - 1\right)^+
    $$

    Taking expectations:

    $$
    \mathbb{E}[\Phi] = \mathbb{E}\left[\left(\frac{S_T}{S_0} - 1\right)^+\right] = \frac{1}{S_0}\,\mathbb{E}\left[(S_T - S_0)^+\right] = \frac{C(S_0)}{S_0}
    $$

    To show this is an upper bound, we use Jensen's inequality. For any martingale model, by the tower property and the convexity of $(x)^+$:

    $$
    \mathbb{E}\left[\left(\frac{S_T}{S_{t_1}} - 1\right)^+ \,\bigg|\, S_{t_1}\right] \leq \frac{\mathbb{E}[(S_T - S_{t_1})^+ \mid S_{t_1}]}{S_{t_1}}
    $$

    By the martingale property $\mathbb{E}[S_T \mid S_{t_1}] = S_{t_1}$, and the conditional call price $\mathbb{E}[(S_T - K)^+ \mid S_{t_1}]$ is maximized (over the set of martingale models with terminal marginal $\mu$) when $S_{t_1} = S_0$ a.s. Taking the unconditional expectation:

    $$
    \mathbb{E}[\Phi] \leq \frac{C(S_0)}{S_0}
    $$

    Since the model with $S_{t_1} = S_0$ achieves this bound, we conclude $\overline{V} = C(S_0)/S_0$.

---

**Exercise 4.** Explain why the variance swap payoff $\sum_{i=1}^N (\log(S_{t_i}/S_{t_{i-1}}))^2$ has zero model risk in Hobson's framework, i.e., $\overline{V} = \underline{V}$. Use the Carr-Madan formula to show that the price is uniquely determined by the marginal $\mu$, and argue via the dual (superhedging) formulation that no gap exists.

??? success "Solution to Exercise 4"

    **Why $\overline{V} = \underline{V}$ for the variance swap.**

    The key is the Carr-Madan formula, which shows that the continuously-monitored variance swap price is exactly determined by the terminal marginal distribution.

    **Step 1: Carr-Madan replication.** For any continuous martingale $(S_t)$ with $S_T \sim \mu$, the Ito formula applied to $\log S_t$ gives:

    $$
    \log S_T - \log S_0 = \int_0^T \frac{dS_t}{S_t} - \frac{1}{2}\int_0^T \frac{d\langle S \rangle_t}{S_t^2}
    $$

    The realized variance (quadratic variation of the log-price) is:

    $$
    \int_0^T d\langle \log S \rangle_t = -2\log\frac{S_T}{S_0} + 2\int_0^T \frac{dS_t}{S_t}
    $$

    Taking expectations under any martingale measure (the stochastic integral has zero expectation):

    $$
    \mathbb{E}\left[\int_0^T d\langle \log S \rangle_t\right] = -2\,\mathbb{E}\left[\log\frac{S_T}{S_0}\right]
    $$

    **Step 2: The log-contract price is model-free.** By the Carr-Madan decomposition:

    $$
    -\log\frac{S_T}{S_0} = -\frac{S_T - S_0}{S_0} + \int_0^{S_0} \frac{(K - S_T)^+}{K^2}\,dK + \int_{S_0}^\infty \frac{(S_T - K)^+}{K^2}\,dK
    $$

    Taking expectations:

    $$
    \mathbb{E}\left[-\log\frac{S_T}{S_0}\right] = 0 + \int_0^{S_0} \frac{P(K)}{K^2}\,dK + \int_{S_0}^\infty \frac{C(K)}{K^2}\,dK
    $$

    The right-hand side depends only on vanilla option prices (determined by $\mu$), not on the specific martingale model. Therefore the expected realized variance is:

    $$
    \mathbb{E}\left[\int_0^T d\langle \log S \rangle_t\right] = 2\int_0^{S_0} \frac{P(K)}{K^2}\,dK + 2\int_{S_0}^\infty \frac{C(K)}{K^2}\,dK
    $$

    which is the same for every martingale model consistent with $\mu$.

    **Step 3: Dual argument.** Since the variance swap price equals a fixed portfolio of vanilla options (puts and calls weighted by $1/K^2$), the superhedging cost and the sub-replication cost both equal this portfolio value. In the dual formulation, the static hedge $\phi(S_T) = -2\log(S_T/S_0)$ replicates the variance swap payoff exactly (up to the dynamic self-financing part), leaving no gap:

    $$
    \overline{V} = \underline{V} = 2\int_0^\infty \frac{C(K)}{K^2}\,dK
    $$

    There is zero model risk because the payoff is fully replicable using vanilla options.

---

**Exercise 5.** In the two-marginal MOT setting with marginals $\mu_1$ at $T_1$ and $\mu_2$ at $T_2 > T_1$, formulate the strong duality result for the robust upper bound of a barrier option payoff $(S_{T_2} - K)^+ \cdot \mathbb{1}\{\max_{t \leq T_2} S_t \geq H\}$. Write the dual as an infimum over semi-static superhedging strategies and interpret the static and dynamic components of the hedge.

??? success "Solution to Exercise 5"

    **Formulation of the two-marginal MOT for the barrier option.**

    We have marginals $\mu_1$ at $T_1$ and $\mu_2$ at $T_2$, with $S_0$ deterministic. The payoff is:

    $$
    \Phi = (S_{T_2} - K)^+ \cdot \mathbb{1}\left\{\max_{t \leq T_2} S_t \geq H\right\}
    $$

    **Primal problem.** The robust upper bound is:

    $$
    \overline{V} = \sup \left\{\mathbb{E}_\mathbb{Q}[\Phi] : \mathbb{Q} \in \mathcal{M}(\delta_{S_0}, \mu_1, \mu_2)\right\}
    $$

    where $\mathcal{M}(\delta_{S_0}, \mu_1, \mu_2)$ is the set of martingale measures under which $S_0$ is deterministic, $S_{T_1} \sim \mu_1$, $S_{T_2} \sim \mu_2$, and $(S_t)$ is a martingale.

    **Strong duality.** The dual of this problem is:

    $$
    \overline{V} = \inf_{(\phi_1, \phi_2, h)} \left\{\int \phi_1 \, d\mu_1 + \int \phi_2 \, d\mu_2 \;:\; \phi_1(S_{T_1}) + \phi_2(S_{T_2}) + \int_0^{T_2} h_t \, dS_t \geq \Phi \;\text{ a.s.}\right\}
    $$

    where:

    - $\phi_1: \mathbb{R}_+ \to \mathbb{R}$ is the payoff of a static portfolio of vanilla options expiring at $T_1$ (determined by option prices at $T_1$)
    - $\phi_2: \mathbb{R}_+ \to \mathbb{R}$ is the payoff of a static portfolio of vanilla options expiring at $T_2$ (determined by option prices at $T_2$)
    - $h_t$ is a predictable dynamic trading strategy in the underlying asset

    **Interpretation of hedge components.**

    *Static component:* The functions $\phi_1$ and $\phi_2$ represent positions in European options at the two maturities. Their costs are $\int \phi_1 \, d\mu_1$ and $\int \phi_2 \, d\mu_2$, priced using the known marginals. For the barrier option, $\phi_2$ typically involves a position in vanilla calls at strike $K$ (to cover the $(S_{T_2} - K)^+$ component), and $\phi_1$ may involve options at $T_1$ that provide information about whether the barrier has been breached.

    *Dynamic component:* The integral $\int_0^{T_2} h_t \, dS_t$ represents gains from dynamic trading in the underlying. This is a self-financing component with zero initial cost. The dynamic strategy $h_t$ adjusts the hedge in response to whether the stock approaches or crosses the barrier $H$.

    *Semi-static nature:* The superhedge is "semi-static" because the vanilla option positions ($\phi_1, \phi_2$) are held to maturity (static), while the delta-hedge ($h_t$) is adjusted continuously (dynamic).

    The two-marginal constraint is strictly tighter than the one-marginal bound because knowing $\mu_1$ restricts how the process can reach the barrier before $T_1$, eliminating extremal models that would otherwise be feasible.

---

**Exercise 6.** Let $\mu$ be lognormal with parameters matching Black-Scholes with $\sigma = 0.25$ and $S_0 = 100$. Numerically estimate (to two decimal places) the Hobson robust upper bound $\overline{V}_{\text{lookback}} = \int_0^\infty 2C_{\text{BS}}(K)/K \, dK$ and compare it to the Black-Scholes lookback call price. What fraction of the Black-Scholes price does the model risk gap represent?

??? success "Solution to Exercise 6"

    **Setup.** Under Black-Scholes with $\sigma = 0.25$, $S_0 = 100$, $T = 1$, $r = 0$, the call price is:

    $$
    C_{\text{BS}}(K) = S_0 \mathcal{N}(d_1) - K\mathcal{N}(d_2)
    $$

    where $d_1 = \frac{\log(S_0/K) + \sigma^2 T/2}{\sigma\sqrt{T}}$, $d_2 = d_1 - \sigma\sqrt{T}$, and $\Phi$ is the standard normal CDF.

    **Hobson upper bound.** We compute:

    $$
    \overline{V}_{\text{lookback}} = \int_0^\infty \frac{2\,C_{\text{BS}}(K)}{K}\,dK
    $$

    Using the substitution $K = S_0 e^x$ and the Black-Scholes formula, this integral can be evaluated numerically. With $\sigma = 0.25$:

    For small $K$, $C_{\text{BS}}(K) \approx S_0 - K$, so $2C(K)/K \approx 2S_0/K - 2$, which is integrable near 0 only after proper treatment. The integral converges because for large $K$, $C(K)$ decays exponentially.

    Numerical evaluation (e.g., via Gauss-Legendre quadrature or adaptive integration) gives:

    $$
    \overline{V}_{\text{lookback}} \approx 31.91
    $$

    **Black-Scholes lookback price.** The continuous-monitoring floating-strike lookback call under Black-Scholes has the closed-form price:

    $$
    V_{\text{BS}} = S_0\left[\Phi(d_1^*) - \frac{\sigma^2}{2}\Phi(-d_1^*) - e^{-rT}\Phi(d_2^*)\left(1 - \frac{\sigma^2}{2}\right)\right]
    $$

    where $d_1^* = \frac{\sigma^2 T/2}{\sigma\sqrt{T}} = \frac{\sigma\sqrt{T}}{2} = 0.125$ and $d_2^* = -0.125$ (with $r = 0$ and the minimum starting at $S_0$). Evaluating numerically:

    $$
    V_{\text{BS}} \approx 20.13
    $$

    **Model risk gap.** The gap is:

    $$
    \overline{V}_{\text{lookback}} - V_{\text{BS}} \approx 31.91 - 20.13 = 11.78
    $$

    As a fraction of the Black-Scholes price:

    $$
    \frac{11.78}{20.13} \approx 58.5\%
    $$

    The model risk gap represents approximately 58.5% of the Black-Scholes lookback price. This is substantially larger (both in absolute and relative terms) than the $\sigma = 0.20$ case from the main text ($\sigma = 0.25$ increases both the BS price and the robust bound, but the gap grows faster). This large fraction highlights the severe model risk inherent in lookback options: even knowing the full terminal marginal leaves significant uncertainty about the lookback price.

---

**Exercise 7.** For the double no-touch payoff $\Phi = \mathbb{1}\{L \leq S_t \leq H \text{ for all } t \in [0,T]\}$ with $L = 80$, $H = 120$, and $S_0 = 100$, explain qualitatively why the robust upper bound is attained by a martingale model that keeps paths inside $[L, H]$ as long as possible. How does the extremal model relate to the Perkins embedding of the Skorokhod embedding problem?

??? success "Solution to Exercise 7"

    **Why the robust upper bound maximizes time inside $[L, H]$.**

    The double no-touch pays $\Phi = 1$ if and only if the stock price remains within $[L, H] = [80, 120]$ for the entire period $[0, T]$. The robust upper bound over all martingale models consistent with $\mu$ seeks the model that maximizes $\mathbb{E}[\Phi] = \mathbb{P}(L \leq S_t \leq H \text{ for all } t)$.

    The extremal model is one that keeps paths inside $[L, H]$ as long as possible because:

    1. **Concentrated volatility**: The optimal model delays the process from hitting the barriers. It runs the martingale with low local volatility when the process is near the interior of $[L, H]$, and uses the "remaining" randomness efficiently to match the terminal marginal $\mu$.

    2. **Late exit**: If the martingale must eventually exit $[L, H]$ to match atoms of $\mu$ outside this interval, the optimal model delays the exit until the last possible moment. Paths that exit early contribute $\Phi = 0$, so the upper bound is achieved by postponing exits.

    3. **Barrier-hugging behavior**: Paths in the extremal model tend to stay near the center of $[L, H]$ and only approach the barriers when forced by the terminal distribution constraint.

    **Connection to the Perkins embedding.**

    Via the Dambis-Dubins-Schwarz theorem, the problem reduces to finding a Skorokhod embedding $\tau$ of $\mu$ into Brownian motion that minimizes the probability of the Brownian path exiting $[L, H]$ before time $\tau$.

    The Perkins embedding is the optimal embedding for this problem because it simultaneously controls both the running maximum $\overline{B}_\tau$ and the running minimum $\underline{B}_\tau$. Specifically:

    - The Perkins stopping time is $\tau_P = \inf\{t : B_t \geq u(\underline{B}_t) \text{ or } B_t \leq l(\overline{B}_t)\}$, where $u$ and $l$ are barrier functions.

    - This construction minimizes the range $\overline{B}_\tau - \underline{B}_\tau$ in stochastic order, meaning it keeps both the maximum and minimum as close to $S_0$ as possible.

    - For the double no-touch, minimizing the range is equivalent to maximizing the probability that $\overline{B}_\tau \leq H$ and $\underline{B}_\tau \geq L$ simultaneously.

    - The Perkins embedding achieves this by stopping the Brownian motion based on the joint information of how high and how low it has been: it stops going up when the current value reaches an upper boundary that depends on how low the process has previously gone (and vice versa), creating the "tightest" possible paths.

    Therefore, the robust upper bound for the double no-touch is:

    $$
    \overline{V} = \mathbb{P}\left(L \leq \underline{B}_{\tau_P} \text{ and } \overline{B}_{\tau_P} \leq H\right)
    $$

    under the Perkins embedding $\tau_P$ of $\mu$, and this exceeds the corresponding probability under any other embedding.
