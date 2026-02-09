# The Fundamental Theorem of Asset Pricing


The **Fundamental Theorem of Asset Pricing (FTAP)** is the cornerstone of modern mathematical finance. It establishes a deep equivalence between an economic concept—**no-arbitrage**—and a probabilistic structure—the existence of an **equivalent martingale measure**. This chapter presents the precise setup, states both parts of the theorem, gives a complete proof in the finite-state case, and discusses the extensions required for continuous time.


## Setup and Market Model


Consider a probability space $(\Omega, \mathcal{F}, \mathbb{P})$ with a filtration $\{\mathcal{F}_t\}_{t=0}^T$ representing information flow over a finite horizon $[0, T]$.

**Asset price process.**
We have $d+1$ assets with price processes $S^0_t, S^1_t, \ldots, S^d_t$:

- $S^0_t$: the **numéraire**, a strictly positive traded asset used as the unit of account. The most common choice is the money market account $S^0_t = e^{rt}$, but any strictly positive traded asset is valid (see [Numéraire and Change of Measure](numeraire_and_change_of_measure.md) for a full treatment).

- $S^i_t$ for $i = 1, \ldots, d$: **risky assets**.

**Discounted prices.**
All prices are expressed relative to the numéraire:

$$\tilde{S}^i_t = \frac{S^i_t}{S^0_t}$$

**Trading strategy and self-financing condition.**
A **trading strategy** is a predictable process $\theta_t = (\theta^0_t, \theta^1_t, \ldots, \theta^d_t)$ where $\theta^i_t$ denotes the number of units held in asset $i$ at time $t$. The **portfolio value** is

$$V_t(\theta) = \sum_{i=0}^d \theta^i_t S^i_t$$

The strategy is **self-financing** if all changes in value come from price movements alone:

$$dV_t = \sum_{i=0}^d \theta^i_t \, dS^i_t$$

No exogenous cash is injected or withdrawn.

**Admissibility.**
A self-financing strategy $\theta$ is **admissible** if there exists a constant $a > 0$ such that

$$V_t(\theta) \geq -a \quad \text{almost surely, for all } t \in [0, T]$$

This lower-bound condition excludes pathological strategies such as **doubling strategies** that create arbitrage in otherwise well-behaved markets. In finite-state models every strategy is automatically admissible, but in continuous time the distinction is essential: without admissibility, one can construct self-financing strategies that generate arbitrage even in the Black–Scholes model.


## Key Definitions


**Arbitrage.**
An **arbitrage opportunity** is an admissible self-financing strategy $\theta$ satisfying:

1. $V_0(\theta) = 0$ (zero initial investment),
2. $V_T(\theta) \geq 0$ $\;\mathbb{P}$-almost surely,
3. $\mathbb{P}(V_T(\theta) > 0) > 0$ (strictly positive probability of profit).

In short: a risk-free gain from nothing.

**Equivalent martingale measure (EMM).**
A probability measure $\mathbb{Q}$ on $(\Omega, \mathcal{F})$ is an **equivalent martingale measure** (also called a **risk-neutral measure**) if:

1. $\mathbb{Q} \sim \mathbb{P}$, meaning $\mathbb{Q}(A) = 0 \iff \mathbb{P}(A) = 0$ for all $A \in \mathcal{F}$ (the two measures agree on which events are possible),

2. the discounted price processes $\tilde{S}^i_t$ are $\mathbb{Q}$-martingales for every $i = 1, \ldots, d$:

$$\tilde{S}^i_t = \mathbb{E}^{\mathbb{Q}}[\tilde{S}^i_T \mid \mathcal{F}_t]$$

**Market completeness.**
A market is **complete** if every $\mathcal{F}_T$-measurable contingent claim $\Phi$ satisfying appropriate integrability conditions can be replicated by an admissible self-financing strategy.


## Statement of the Theorem


The FTAP comes in two parts.

### First FTAP: No-Arbitrage $\iff$ EMM Existence

**Theorem 1 (First FTAP, finite case).**
*In a finite-state market, there are no arbitrage opportunities if and only if there exists an equivalent martingale measure $\mathbb{Q}$.*

$$\text{No Arbitrage} \iff \exists\, \mathbb{Q} \sim \mathbb{P} \text{ such that } \tilde{S}^i_t \text{ is a } \mathbb{Q}\text{-martingale for all } i$$


### Second FTAP: Completeness $\iff$ Uniqueness

**Theorem 2 (Second FTAP).**
*Assume no arbitrage. The market is complete if and only if the equivalent martingale measure is unique.*

$$\text{Complete + No Arbitrage} \iff \exists!\, \mathbb{Q} \sim \mathbb{P} \text{ such that } \tilde{S}^i_t \text{ is a } \mathbb{Q}\text{-martingale for all } i$$


!!! note "Remark: NA vs. NFLVR"
    The statement above is exact for finite-state models, where **no-arbitrage (NA)** is the correct condition. In continuous time, NA alone is insufficient to guarantee the existence of an EMM—one needs the stronger condition of **No Free Lunch with Vanishing Risk (NFLVR)**, introduced by Delbaen and Schachermayer (1994). The distinction and the continuous-time version of the theorem are discussed in the section [Extension to Continuous Time](#extension-to-continuous-time) below.


## Proof of the First FTAP (Finite State Space)


We work in a one-period model ($t \in \{0, 1\}$) with finite state space $\Omega = \{\omega_1, \ldots, \omega_n\}$ and $\mathbb{P}(\omega_i) = p_i > 0$ for all $i$. There are $d$ risky assets (the numéraire $S^0$ is normalized to $1$ at both times for simplicity, equivalent to working with pre-discounted prices).

**Payoff matrix.**
Define the $n \times d$ matrix $X$ of discounted excess returns:

$$X_{ij} = S^j_1(\omega_i) - S^j_0, \qquad i = 1, \ldots, n, \quad j = 1, \ldots, d$$

Row $i$ gives the payoff across all assets in state $\omega_i$; column $j$ gives asset $j$'s payoff across all states. A strategy $\theta \in \mathbb{R}^d$ produces the payoff vector $X\theta \in \mathbb{R}^n$, and because $X$ encodes excess returns, this payoff has zero initial cost by construction.

**What we need to show.** An EMM $\mathbb{Q}$ with weights $q_i > 0$, $\sum_i q_i = 1$, satisfies $\mathbb{E}^{\mathbb{Q}}[\tilde{S}^j_1 - S^j_0] = 0$ for all $j$, which in matrix form is $X^T q = 0$. So the first FTAP reduces to:

$$\text{No } \theta \text{ with } X\theta \geq 0, \; X\theta \neq 0 \quad \iff \quad \exists\, q \in \operatorname{int}(\Delta_n) \text{ such that } X^T q = 0$$

where $\operatorname{int}(\Delta_n)$ is the interior of the probability simplex.


### Direction 1: EMM Exists $\Rightarrow$ No Arbitrage

This is the easier direction.

**Proof.** Let $\mathbb{Q}$ be an EMM with weights $q_i > 0$ for all $i$ and $X^T q = 0$. For any strategy $\theta$, the $\mathbb{Q}$-expected payoff is

$$\mathbb{E}^{\mathbb{Q}}[X\theta] = q^T(X\theta) = (X^T q)^T \theta = 0^T \theta = 0$$

Now suppose $\theta$ satisfies $X\theta \geq 0$ (componentwise). Then $(X\theta)_i \geq 0$ for all $i$ and $q_i > 0$ for all $i$, so

$$0 = \sum_{i=1}^n q_i (X\theta)_i \geq 0$$

with each term $q_i(X\theta)_i \geq 0$. For the sum to equal zero, every term must vanish: $q_i(X\theta)_i = 0$ for all $i$. Since $q_i > 0$, this forces $(X\theta)_i = 0$ for all $i$, i.e., $X\theta = 0$.

Therefore, no strategy can produce a non-negative payoff that is strictly positive in any state. No arbitrage exists. $\square$


### Direction 2: No Arbitrage $\Rightarrow$ EMM Exists

This direction uses the separating hyperplane theorem.

**Step 1: Formulate as a geometric question.**

Define the **closed probability simplex**:

$$\bar{\Delta}_n = \left\{q \in \mathbb{R}^n : q_i \geq 0 \text{ for all } i, \;\sum_{i=1}^n q_i = 1\right\}$$

Consider the image of $\bar{\Delta}_n$ under the linear map $q \mapsto X^T q$:

$$\mathcal{S} = \{X^T q : q \in \bar{\Delta}_n\} \subset \mathbb{R}^d$$

The set $\mathcal{S}$ is **convex** (as the image of a convex set under a linear map) and **compact** (as the continuous image of the compact set $\bar{\Delta}_n$).

We will show that if no arbitrage holds, then $0 \in \mathcal{S}$, and moreover the zero can be achieved by a $q$ in the **interior** $\operatorname{int}(\Delta_n) = \{q : q_i > 0\}$.

**Step 2: Proof by contradiction—suppose $0 \notin \mathcal{S}$.**

Assume no $q \in \bar{\Delta}_n$ satisfies $X^T q = 0$. Then $\mathcal{S}$ is a compact convex set not containing the origin, and $\{0\}$ is a (trivially) compact convex set. By the **strict separating hyperplane theorem**, there exists a nonzero vector $\theta \in \mathbb{R}^d$ and a constant $\alpha$ such that

$$\theta^T s < \alpha < \theta^T \cdot 0 = 0 \qquad \text{for all } s \in \mathcal{S}$$

In particular, for every $q \in \bar{\Delta}_n$:

$$\theta^T (X^T q) = (X\theta)^T q < 0$$

**Step 3: Extract componentwise information.**

The standard basis vectors $e_i = (0, \ldots, 1, \ldots, 0)$ lie in $\bar{\Delta}_n$. Evaluating at $q = e_i$:

$$e_i^T (X\theta) = (X\theta)_i < 0 \qquad \text{for each } i = 1, \ldots, n$$

Therefore $X\theta$ has all strictly negative components: $(X\theta)_i < 0$ for every state $\omega_i$.

**Step 4: Construct an arbitrage.**

Consider the strategy $-\theta$. Its payoff vector is $X(-\theta) = -(X\theta)$, which is strictly positive in every state. Since $X$ encodes excess returns (discounted gains from zero-cost positions), the strategy $-\theta$ has zero initial cost and strictly positive payoff in all states. This is an arbitrage—in fact, a stronger form than required, since the payoff is strictly positive everywhere, not merely non-negative with positive probability.

**Step 5: Contradiction.**

We assumed no arbitrage, so the assumption $0 \notin \mathcal{S}$ is false. Hence there exists $q^* \in \bar{\Delta}_n$ with $X^T q^* = 0$.

**Step 6: Upgrade to strict positivity ($q_i^* > 0$).**

The vector $q^*$ found above may have some zero components, meaning it lies on the boundary of the simplex. We need $q_i > 0$ for all $i$ to ensure $\mathbb{Q} \sim \mathbb{P}$ (equivalence). The argument proceeds as follows.

Let $p = (p_1, \ldots, p_n)$ be the physical probability vector with $p_i > 0$ for all $i$. Define the affine combination

$$q_\varepsilon = (1 - \varepsilon)\, q^* + \varepsilon\, p, \qquad \varepsilon \in (0, 1)$$

Then $q_\varepsilon$ has all strictly positive components (since $p_i > 0$), lies in $\bar{\Delta}_n$, and satisfies

$$X^T q_\varepsilon = (1 - \varepsilon)\, X^T q^* + \varepsilon\, X^T p = \varepsilon\, X^T p$$

This is zero only if $X^T p = 0$, which would mean $p$ is itself an EMM and we are done. Otherwise, $X^T q_\varepsilon \neq 0$ for small $\varepsilon$.

The resolution uses a refined version of the argument. Define the set

$$\mathcal{K} = \{q \in \bar{\Delta}_n : X^T q = 0\}$$

This is a non-empty (by Step 5) compact convex set. We claim it intersects $\operatorname{int}(\Delta_n)$. To see this, suppose instead that every $q \in \mathcal{K}$ has some zero component. Partition the states into $I = \{i : q^*_i > 0\}$ and $I^c = \{i : q^*_i = 0\}$ for some extremal $q^* \in \mathcal{K}$. The no-arbitrage condition, restricted to the sub-model on states $I^c$, implies (by the same separation argument applied to the reduced model) that there exists a probability vector supported on $I^c$ that makes the restricted payoff matrix a martingale. Combining this with $q^*$ (supported on $I$) yields a vector in $\mathcal{K}$ with strictly larger support. Repeating finitely many times (since $|\Omega| = n$ is finite), we obtain $q \in \mathcal{K}$ with full support, i.e., $q \in \operatorname{int}(\Delta_n)$. $\square$


### Visual Intuition (for $d = 2$, $n = 3$)

Consider two risky assets ($d = 2$) and three states ($n = 3$). The closed simplex $\bar{\Delta}_3$ is a triangle in $\mathbb{R}^3$. The linear map $q \mapsto X^T q$ projects this triangle into $\mathbb{R}^2$, producing a convex region $\mathcal{S}$.

If $0 \in \mathcal{S}$, some probability weighting makes the expected excess return vanish—an EMM exists. If $0 \notin \mathcal{S}$, a line through the origin (the separating hyperplane, with normal vector $\theta$) separates $\mathcal{S}$ from the origin. The portfolio $\theta$ then has the property that its expected payoff is negative under *every* probability measure on $\Omega$, which forces its payoff to be negative in every state. Flipping the sign gives an arbitrage.


## Proof of the Second FTAP (Completeness $\iff$ Uniqueness)


We continue in the one-period finite-state model.

**Completeness $\Rightarrow$ Uniqueness.**

Suppose the market is complete, so that every contingent claim $\Phi \in \mathbb{R}^n$ can be replicated: for every $\Phi$ there exists $\theta$ with $X\theta = \Phi - c\mathbf{1}$ for some constant $c$ (the initial cost). If $\mathbb{Q}_1$ and $\mathbb{Q}_2$ are both EMMs, then for any claim $\Phi$:

$$\mathbb{E}^{\mathbb{Q}_1}[\Phi] = c = \mathbb{E}^{\mathbb{Q}_2}[\Phi]$$

Since this holds for all $\Phi \in \mathbb{R}^n$, we can take $\Phi = \mathbf{1}_{\{\omega_i\}}$ (the indicator of each state) to get $q^1_i = q^2_i$ for all $i$. Hence $\mathbb{Q}_1 = \mathbb{Q}_2$.

**Uniqueness $\Rightarrow$ Completeness.**

Suppose $\mathbb{Q}$ is the unique EMM. The set of EMMs is

$$\mathcal{K} = \{q \in \operatorname{int}(\Delta_n) : X^T q = 0\} = \operatorname{int}(\Delta_n) \cap \ker(X^T)$$

Uniqueness means $\mathcal{K}$ is a singleton. Since $\ker(X^T) \subset \mathbb{R}^n$ is a linear subspace, the constraint $q \in \operatorname{int}(\Delta_n)$ with $X^T q = 0$ being a singleton requires that $\ker(X^T)$ intersects the affine hyperplane $\{\sum q_i = 1\}$ in exactly one point. This happens precisely when $\dim(\ker(X^T)) = 1$.

Now $\dim(\ker(X^T)) = n - \operatorname{rank}(X)$. So the uniqueness condition gives $\operatorname{rank}(X) = n - 1$. The image of $X$ (the space of attainable payoff vectors) therefore has dimension $n - 1$ in $\mathbb{R}^n$. Since the attainable payoffs also satisfy the constraint $\mathbb{E}^{\mathbb{Q}}[X\theta] = 0$ (a single linear constraint on $\mathbb{R}^n$), the space of zero-cost attainable payoffs is exactly the orthogonal complement of $q$ within $\mathbb{R}^n$. Every claim $\Phi$ can be decomposed as $\Phi = c \cdot \mathbf{1} + X\theta$ for some scalar $c$ and portfolio $\theta$, showing the market is complete. $\square$

!!! note "Remark on dimensions"
    In a model with $n$ states and $d$ risky assets, the rank of $X$ is at most $\min(n, d)$. For $\dim(\ker(X^T)) = 1$ we need $\operatorname{rank}(X) = n - 1$, which requires $d \geq n - 1$. When $d = n - 1$ and $X$ has full column rank, the market is exactly complete. When $d < n - 1$, the market is generically incomplete: there are multiple EMMs, and derivatives have a range of no-arbitrage prices rather than a unique price.


## Extension to Continuous Time


In continuous time the proof requires substantially more sophisticated analysis. The key difficulty is that the strategy space and the payoff space are infinite-dimensional, so finite-dimensional linear algebra (separating hyperplane in $\mathbb{R}^d$) must be replaced by functional analysis.

### From NA to NFLVR

The straightforward condition "no arbitrage" turns out to be too weak in continuous time. Consider a sequence of strategies $\theta_n$ with $V_0(\theta_n) = 0$ and $V_T(\theta_n) \geq -1/n$, converging to a payoff that is non-negative and strictly positive with positive probability. No single strategy is an arbitrage, but the limiting "free lunch" is economically just as problematic.

Delbaen and Schachermayer (1994) introduced the condition **No Free Lunch with Vanishing Risk (NFLVR)**, which closes this loophole:

$$\text{NFLVR} \;:\; \overline{\mathcal{C} - L^0_+} \cap L^\infty_+ = \{0\}$$

where $\mathcal{C} = \{V_T(\theta) : \theta \text{ admissible}, V_0(\theta) = 0\}$ is the set of terminal values of zero-cost admissible strategies, and the closure is in an appropriate topology.

NFLVR is strictly stronger than NA but is the economically natural condition: it excludes both outright arbitrage and approximate arbitrage in the limit.


### The Delbaen–Schachermayer Theorem

**Theorem (First FTAP, continuous time; Delbaen–Schachermayer, 1994).**
*Let $S$ be a bounded semimartingale. Then NFLVR holds if and only if there exists a probability measure $\mathbb{Q} \sim \mathbb{P}$ such that $S$ is a $\sigma$-martingale under $\mathbb{Q}$.*

For locally bounded semimartingales, the conclusion strengthens to $S$ being a **local martingale** under $\mathbb{Q}$, and the measure $\mathbb{Q}$ is called an **equivalent local martingale measure (ELMM)**.

The proof strategy is:

1. Define the convex cone of attainable claims $\mathcal{C} = \{(\theta \cdot S)_T : \theta \text{ admissible}, V_0 = 0\}$.

2. NFLVR ensures the closure $\bar{\mathcal{C}} \cap L^\infty_+$ is trivial.

3. By the **Kreps–Yan theorem** (a functional-analytic extension of the separating hyperplane theorem to $L^\infty$), there exists a strictly positive continuous linear functional $\Lambda$ on $L^\infty$ that vanishes on $\mathcal{C}$.

4. By the **Riesz representation theorem**, $\Lambda$ corresponds to a measure $\mathbb{Q} \in L^1$ with $d\mathbb{Q}/d\mathbb{P} > 0$.

5. The condition $\Lambda(X) = 0$ for all $X \in \mathcal{C}$ translates into the (local/sigma) martingale property for discounted prices under $\mathbb{Q}$.

The reverse direction (ELMM $\Rightarrow$ NFLVR) follows by the same expectation argument as in the finite case: under $\mathbb{Q}$, the discounted wealth process of any admissible strategy is a supermartingale, so a non-negative terminal value with zero initial value must be identically zero.


### Historical Development

The theorem has a rich history spanning several decades:

- **Harrison and Kreps (1979)** established the equivalence in discrete time and introduced the martingale approach to pricing.

- **Harrison and Pliska (1981)** extended the framework to continuous time under restrictive conditions and proved the second FTAP (completeness $\iff$ uniqueness).

- **Dalang, Morton, and Willinger (1990)** proved the first FTAP in full generality for discrete-time models with finitely many periods but possibly infinitely many states.

- **Delbaen and Schachermayer (1994)** proved the definitive continuous-time result, establishing NFLVR $\iff$ existence of an ELMM for general semimartingale models. This required deep results from functional analysis and stochastic calculus.


## Economic Intuition


**Risk-neutral valuation as consensus pricing.**
The EMM $\mathbb{Q}$ can be interpreted as a "consensus probability" under which all assets earn the same expected return (the numéraire rate). Under $\mathbb{Q}$,

$$\tilde{S}^i_t = \mathbb{E}^{\mathbb{Q}}[\tilde{S}^i_T \mid \mathcal{F}_t]$$

This does not mean investors are risk-neutral. It means that risk preferences are fully absorbed into the measure change from $\mathbb{P}$ to $\mathbb{Q}$, allowing us to price by expectation alone.

**Arbitrage as inconsistency.**
Arbitrage represents an internal inconsistency in the price system: some asset is mispriced relative to others. The existence of $\mathbb{Q}$ certifies that all prices are mutually consistent—no such mispricing exists.

**Why equivalence ($\mathbb{Q} \sim \mathbb{P}$) matters.**
Equivalence ensures that $\mathbb{Q}$ and $\mathbb{P}$ agree on which events are possible. We change probabilities, not possibilities. If $\mathbb{Q}$ could assign zero probability to an event that is possible under $\mathbb{P}$, one could construct an arbitrage by betting on that event.

**Completeness as unique pricing.**
When the EMM is unique, every contingent claim has a unique no-arbitrage price and can be perfectly replicated. Multiple EMMs correspond to an incomplete market where derivatives have a range of consistent prices—the endpoints of this range are the super-replication and sub-replication prices.


## Mathematical Intuition


**Duality between strategies and measures.**
The FTAP establishes a fundamental duality:

$$\begin{array}{ccc}
\text{Portfolio strategies } \theta & \longleftrightarrow & \text{Probability measures } \mathbb{Q} \\
\text{Arbitrage opportunities} & \longleftrightarrow & \text{Non-existence of EMM} \\
\text{Market completeness} & \longleftrightarrow & \text{Unique EMM}
\end{array}$$

This is a financial instance of a general principle in convex analysis: feasibility of a primal problem (replication) is dual to feasibility of the dual problem (existence of pricing measures).

**Martingales as fair games.**
A martingale $M_t$ satisfies $\mathbb{E}[M_{t+1} \mid \mathcal{F}_t] = M_t$: the best forecast of tomorrow's value is today's value. The FTAP says that no-arbitrage is equivalent to the existence of a probability measure under which discounted prices are fair games.

**Geometric picture.**
In the finite model, $X\theta$ ranges over a subspace $\mathcal{V} = \operatorname{Im}(X) \subset \mathbb{R}^n$. No-arbitrage says $\mathcal{V}$ does not intersect the positive orthant $\mathbb{R}^n_+ \setminus \{0\}$. Dually, there must exist a strictly positive vector $q$ in the orthogonal complement $\mathcal{V}^\perp$ (after normalization, this is the EMM). The separating hyperplane theorem makes this duality precise.

**Connection to Girsanov theory.**
In continuous time with a single Brownian driver, the measure change takes the form

$$\frac{d\mathbb{Q}}{d\mathbb{P}}\bigg|_{\mathcal{F}_T} = \mathcal{E}\left(-\int_0^T \lambda_s \, dW_s\right) = \exp\left(-\int_0^T \lambda_s \, dW_s - \frac{1}{2}\int_0^T \lambda_s^2 \, ds\right)$$

where $\lambda_t = (\mu_t - r)/\sigma_t$ is the **market price of risk**. By Girsanov's theorem, $W^{\mathbb{Q}}_t = W_t + \int_0^t \lambda_s \, ds$ is a $\mathbb{Q}$-Brownian motion, and under $\mathbb{Q}$ the stock dynamics become $dS_t = rS_t\, dt + \sigma_t S_t\, dW^{\mathbb{Q}}_t$.


## Connection to Black–Scholes


In the Black–Scholes model,

$$dS_t = \mu S_t \, dt + \sigma S_t \, dW_t$$

with constant parameters $\mu, \sigma, r$. The market price of risk is $\lambda = (\mu - r)/\sigma$, and the Radon–Nikodym derivative is

$$\frac{d\mathbb{Q}}{d\mathbb{P}}\bigg|_{\mathcal{F}_T} = \exp\left(-\lambda W_T - \frac{\lambda^2 T}{2}\right)$$

Under $\mathbb{Q}$, the stock follows $dS_t = rS_t\, dt + \sigma S_t\, dW^{\mathbb{Q}}_t$, and the discounted price $e^{-rt}S_t$ is a $\mathbb{Q}$-martingale, confirming the first FTAP. Since there is one source of randomness ($W_t$) and one risky asset, the EMM is **unique** and the market is **complete**, confirming the second FTAP.


## Summary


The FTAP provides the theoretical foundation for all of quantitative finance:

1. **No-arbitrage $\iff$ EMM existence**: prices are consistent if and only if a risk-neutral probability measure exists.

2. **Completeness $\iff$ EMM uniqueness**: every claim can be replicated if and only if the pricing measure is unique.

3. **Pricing formula**: under the EMM, the price of any replicable claim is $V_t = S^0_t \cdot \mathbb{E}^{\mathbb{Q}}[\Phi_T / S^0_T \mid \mathcal{F}_t]$.

4. **Continuous-time refinement**: the correct no-arbitrage condition is NFLVR, and the EMM becomes an equivalent local martingale measure.

The theorem tells us that in an arbitrage-free market, there exists a probability measure under which discounted asset prices are martingales, and pricing reduces to computing expectations in that measure.


## References

- Harrison, J. M. and Kreps, D. M. (1979). *Martingales and arbitrage in multiperiod securities markets.* Journal of Economic Theory, 20(3), 381–408.

- Harrison, J. M. and Pliska, S. R. (1981). *Martingales and stochastic integrals in the theory of continuous trading.* Stochastic Processes and their Applications, 11(3), 215–260.

- Dalang, R. C., Morton, A., and Willinger, W. (1990). *Equivalent martingale measures and no-arbitrage in stochastic securities market models.* Stochastics and Stochastic Reports, 29(2), 185–201.

- Delbaen, F. and Schachermayer, W. (1994). *A general version of the fundamental theorem of asset pricing.* Mathematische Annalen, 300(1), 463–520.

- Föllmer, H. and Schied, A. (2016). *Stochastic Finance: An Introduction in Discrete Time.* 4th edition, de Gruyter.

- Shreve, S. E. (2004). *Stochastic Calculus for Finance II: Continuous-Time Models.* Springer.
