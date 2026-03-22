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
