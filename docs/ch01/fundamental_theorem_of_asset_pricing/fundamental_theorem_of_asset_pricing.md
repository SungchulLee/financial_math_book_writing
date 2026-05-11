# The Fundamental Theorem of Asset Pricing


The **Fundamental Theorem of Asset Pricing (FTAP)** is the cornerstone of modern mathematical finance. This chapter shows that arbitrage-free pricing is equivalent to the existence of a martingale measure, that unique pricing is equivalent to completeness, and that both remain invariant under changes of numéraire.


## Chapter Roadmap

The chapter develops one forced progression: economic constraint → geometric separation → martingale measure → pricing structure.

``` mermaid
flowchart LR
A[No-Arbitrage] --> B[Separating Hyperplane]
B --> C[Equivalent Martingale Measure]
C --> D[Completeness / Uniqueness]
D --> E[Examples]
E --> F[Numéraire Change]
```

| Section | Role | Main idea |
|---|---|---|
| [FTAP](#statement-of-the-theorem) (this page) | Core theorem | no-arbitrage ↔ equivalent martingale measure |
| [Separating Hyperplane](separating_hyperplane_theorem.md) | Proof tool | geometric separation produces a pricing functional |
| [Complete Markets and Uniqueness](complete_markets_and_uniqueness.md) | Second FTAP | uniqueness of EMM ↔ replicability |
| [Finite Market Examples](../numeraire_and_change_of_measure/finite_market_examples.md) | Concrete intuition | complete, incomplete, and arbitrage cases |
| [Numéraire and Change of Measure](../numeraire_and_change_of_measure/numeraire_and_change_of_measure.md) | Extension | pricing is invariant under choice of numéraire |

This chapter is the bridge between the earlier discrete pricing chapters and the later continuous-time theory: it formalizes no-arbitrage as the organizing principle, identifies when martingale measures exist and are unique, and prepares the move to change of measure and continuous-time stochastic calculus.


## Setup and Market Model


Consider a probability space $(\Omega, \mathcal{F}, \mathbb{P})$ with a filtration $\{\mathcal{F}_t\}_{t=0}^T$ representing information flow over a finite horizon $[0, T]$.

**Asset price process.**
We have $d+1$ assets with price processes $S^0_t, S^1_t, \ldots, S^d_t$:

- $S^0_t$: the **numéraire**, a strictly positive traded asset used as the unit of account. The most common choice is the money market account $S^0_t = e^{rt}$, but any strictly positive traded asset is valid (see [Numéraire and Change of Measure](../numeraire_and_change_of_measure/numeraire_and_change_of_measure.md) for a full treatment).

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

### First FTAP: No-Arbitrage ⟺ EMM Existence

**Theorem 1 (First FTAP, finite case).**
*In a finite-state market, there are no arbitrage opportunities if and only if there exists an equivalent martingale measure $\mathbb{Q}$.*

$$\text{No Arbitrage} \iff \exists\, \mathbb{Q} \sim \mathbb{P} \text{ such that } \tilde{S}^i_t \text{ is a } \mathbb{Q}\text{-martingale for all } i$$


### Second FTAP: Completeness ⟺ Uniqueness

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


### Direction 1: EMM Exists ⇒ No Arbitrage

This is the easier direction.

**Proof.** Let $\mathbb{Q}$ be an EMM with weights $q_i > 0$ for all $i$ and $X^T q = 0$. For any strategy $\theta$, the $\mathbb{Q}$-expected payoff is

$$\mathbb{E}^{\mathbb{Q}}[X\theta] = q^T(X\theta) = (X^T q)^T \theta = 0^T \theta = 0$$

Now suppose $\theta$ satisfies $X\theta \geq 0$ (componentwise). Then $(X\theta)_i \geq 0$ for all $i$ and $q_i > 0$ for all $i$, so

$$0 = \sum_{i=1}^n q_i (X\theta)_i \geq 0$$

with each term $q_i(X\theta)_i \geq 0$. For the sum to equal zero, every term must vanish: $q_i(X\theta)_i = 0$ for all $i$. Since $q_i > 0$, this forces $(X\theta)_i = 0$ for all $i$, i.e., $X\theta = 0$.

Therefore, no strategy can produce a non-negative payoff that is strictly positive in any state. No arbitrage exists. $\square$


### Direction 2: No Arbitrage ⇒ EMM Exists

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


### Visual Intuition (for d = 2, n = 3)

Consider two risky assets ($d = 2$) and three states ($n = 3$). The closed simplex $\bar{\Delta}_3$ is a triangle in $\mathbb{R}^3$. The linear map $q \mapsto X^T q$ projects this triangle into $\mathbb{R}^2$, producing a convex region $\mathcal{S}$.

If $0 \in \mathcal{S}$, some probability weighting makes the expected excess return vanish—an EMM exists. If $0 \notin \mathcal{S}$, a line through the origin (the separating hyperplane, with normal vector $\theta$) separates $\mathcal{S}$ from the origin. The portfolio $\theta$ then has the property that its expected payoff is negative under *every* probability measure on $\Omega$, which forces its payoff to be negative in every state. Flipping the sign gives an arbitrage.


## Proof of the Second FTAP (Completeness ⟺ Uniqueness)


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

---

## Exercises

**Exercise 1.** Consider a one-period market with $n = 3$ states and $d = 2$ risky assets. The payoff matrix of discounted excess returns is

$$
X = \begin{pmatrix} 5 & 2 \\ 0 & -1 \\ -3 & 1 \end{pmatrix}
$$

Find all probability vectors $q = (q_1, q_2, q_3)$ with $q_i > 0$ and $\sum q_i = 1$ satisfying $X^T q = 0$. Is the market arbitrage-free? Is it complete?

??? success "Solution to Exercise 1"
    We need $q = (q_1, q_2, q_3)$ with $q_i > 0$, $\sum q_i = 1$, and $X^T q = 0$. The system $X^T q = 0$ gives two equations:

    $$
    5q_1 + 0 \cdot q_2 - 3q_3 = 0 \quad \Longrightarrow \quad q_1 = \frac{3}{5}q_3
    $$

    $$
    2q_1 - q_2 + q_3 = 0 \quad \Longrightarrow \quad q_2 = 2q_1 + q_3 = \frac{6}{5}q_3 + q_3 = \frac{11}{5}q_3
    $$

    From the normalization $q_1 + q_2 + q_3 = 1$:

    $$
    \frac{3}{5}q_3 + \frac{11}{5}q_3 + q_3 = \frac{3 + 11 + 5}{5}q_3 = \frac{19}{5}q_3 = 1 \quad \Longrightarrow \quad q_3 = \frac{5}{19}
    $$

    Therefore:

    $$
    q_1 = \frac{3}{19}, \qquad q_2 = \frac{11}{19}, \qquad q_3 = \frac{5}{19}
    $$

    All components are strictly positive, so the market is **arbitrage-free**. The EMM is unique (the two equations from $X^T q = 0$ plus normalization fully determine three unknowns), so the market is **complete**.

    Verification: $\operatorname{rank}(X) = 2 = n - 1 = 3 - 1$, confirming completeness by the rank condition.

---

**Exercise 2.** Prove the easy direction of the First FTAP in detail: if an equivalent martingale measure $\mathbb{Q}$ exists, then no arbitrage opportunity exists. Your proof should explicitly use the strict positivity of the Radon–Nikodym derivative $d\mathbb{Q}/d\mathbb{P}$.

??? success "Solution to Exercise 2"
    Let $\mathbb{Q}$ be an EMM with Radon--Nikodym derivative $Z = d\mathbb{Q}/d\mathbb{P}$, so $Z(\omega) > 0$ for all $\omega$ (since $\mathbb{Q} \sim \mathbb{P}$). The discounted price process $\tilde{S}^i_t = S^i_t / S^0_t$ is a $\mathbb{Q}$-martingale, meaning for any strategy $\theta$:

    $$
    \mathbb{E}^{\mathbb{Q}}[\tilde{V}_T(\theta)] = \tilde{V}_0(\theta)
    $$

    where $\tilde{V}_t(\theta)$ is the discounted portfolio value. For a zero-cost strategy ($V_0(\theta) = 0$), this gives $\mathbb{E}^{\mathbb{Q}}[\tilde{V}_T(\theta)] = 0$.

    Now suppose $\theta$ is an arbitrage: $V_0(\theta) = 0$, $V_T(\theta) \geq 0$ a.s., and $\mathbb{P}(V_T(\theta) > 0) > 0$. Since $S^0_T > 0$, the discounted terminal value $\tilde{V}_T(\theta) = V_T(\theta)/S^0_T$ satisfies $\tilde{V}_T(\theta) \geq 0$ a.s.

    Since $\mathbb{Q} \sim \mathbb{P}$, the event $\{V_T(\theta) > 0\}$ has $\mathbb{Q}$-probability strictly positive: $\mathbb{Q}(V_T(\theta) > 0) > 0$. This uses exactly the equivalence $\mathbb{Q} \sim \mathbb{P}$, which means $\mathbb{P}(A) > 0 \iff \mathbb{Q}(A) > 0$.

    Therefore $\tilde{V}_T(\theta) \geq 0$ $\mathbb{Q}$-a.s. with $\mathbb{Q}(\tilde{V}_T(\theta) > 0) > 0$, which gives

    $$
    \mathbb{E}^{\mathbb{Q}}[\tilde{V}_T(\theta)] > 0
    $$

    But the martingale property requires $\mathbb{E}^{\mathbb{Q}}[\tilde{V}_T(\theta)] = 0$. This is a contradiction, so no arbitrage can exist. $\square$

---

**Exercise 3.** In the proof of the First FTAP (Direction 2), the argument constructs a vector $q^* \in \bar{\Delta}_n$ with $X^T q^* = 0$ but possibly $q^*_i = 0$ for some $i$. Explain why the convex combination $q_\varepsilon = (1 - \varepsilon) q^* + \varepsilon p$ does not immediately solve the problem, and describe the iterative refinement used to upgrade $q^*$ to an interior point of the simplex.

??? success "Solution to Exercise 3"
    The convex combination $q_\varepsilon = (1 - \varepsilon)q^* + \varepsilon p$ has all strictly positive components (since $p_i > 0$ and $\varepsilon > 0$), but it satisfies

    $$
    X^T q_\varepsilon = (1 - \varepsilon) X^T q^* + \varepsilon X^T p = \varepsilon X^T p
    $$

    This equals zero only if $X^T p = 0$, meaning the physical measure $p$ is already an EMM. In general, $X^T p \neq 0$, so $q_\varepsilon$ fails the martingale condition $X^T q = 0$ for any $\varepsilon > 0$. The perturbation fixes the positivity problem but breaks the martingale property.

    The **iterative refinement** works as follows. Let $q^* \in \mathcal{K} = \{q \in \bar{\Delta}_n : X^T q = 0\}$ with support $I = \{i : q^*_i > 0\}$. If $I \neq \{1, \ldots, n\}$, consider the complementary states $I^c$. Restrict the no-arbitrage condition to the sub-market on states $I^c$: the restricted payoff matrix $X_{I^c}$ (rows indexed by $I^c$) must also admit no arbitrage (otherwise the original market would have an arbitrage). By applying the separation argument to this restricted model, there exists a probability vector $\hat{q}$ supported on $I^c$ with $X^T_{I^c} \hat{q} = 0$.

    Extend $\hat{q}$ to all $n$ states by setting $\hat{q}_i = 0$ for $i \in I$. Then $X^T \hat{q} = 0$, and $\hat{q}$ is supported on $I^c$. The convex combination

    $$
    q^{**} = \frac{1}{2} q^* + \frac{1}{2} \hat{q}
    $$

    satisfies $X^T q^{**} = 0$ and has support $I \cup I^c$, which is strictly larger than $I$. If $q^{**}$ still has zero components, repeat the procedure. Since $|\Omega| = n$ is finite, after at most $n$ iterations the support covers all states, yielding $q \in \operatorname{int}(\Delta_n)$ with $X^T q = 0$.

---

**Exercise 4.** In the Black-Scholes model with $dS_t = \mu S_t\, dt + \sigma S_t\, dW_t$ and constant risk-free rate $r$, compute the market price of risk $\lambda = (\mu - r)/\sigma$. Show that $W^{\mathbb{Q}}_t = W_t + \lambda t$ is a $\mathbb{Q}$-Brownian motion and verify that $e^{-rt}S_t$ is a $\mathbb{Q}$-martingale.

??? success "Solution to Exercise 4"
    In the Black--Scholes model, $dS_t = \mu S_t \, dt + \sigma S_t \, dW_t$ with constant $\mu$, $\sigma$, and risk-free rate $r$. The market price of risk is

    $$
    \lambda = \frac{\mu - r}{\sigma}
    $$

    Define the Radon--Nikodym derivative process

    $$
    Z_t = \exp\left(-\lambda W_t - \frac{\lambda^2}{2} t\right)
    $$

    By Girsanov's theorem, the process $W^{\mathbb{Q}}_t = W_t + \lambda t$ is a Brownian motion under the measure $\mathbb{Q}$ defined by $d\mathbb{Q}/d\mathbb{P}|_{\mathcal{F}_T} = Z_T$.

    Rewriting the stock dynamics in terms of $W^{\mathbb{Q}}_t$: since $W_t = W^{\mathbb{Q}}_t - \lambda t$,

    $$
    dS_t = \mu S_t \, dt + \sigma S_t (dW^{\mathbb{Q}}_t - \lambda \, dt) = (\mu - \sigma\lambda) S_t \, dt + \sigma S_t \, dW^{\mathbb{Q}}_t
    $$

    Substituting $\lambda = (\mu - r)/\sigma$:

    $$
    \mu - \sigma\lambda = \mu - \sigma \cdot \frac{\mu - r}{\sigma} = \mu - (\mu - r) = r
    $$

    So under $\mathbb{Q}$: $dS_t = r S_t \, dt + \sigma S_t \, dW^{\mathbb{Q}}_t$.

    Now consider the discounted price $\tilde{S}_t = e^{-rt} S_t$. By Ito's lemma:

    $$
    d\tilde{S}_t = e^{-rt}(dS_t - rS_t \, dt) = e^{-rt} \sigma S_t \, dW^{\mathbb{Q}}_t = \sigma \tilde{S}_t \, dW^{\mathbb{Q}}_t
    $$

    The process $\tilde{S}_t$ is a driftless Ito process (a local martingale) under $\mathbb{Q}$. Since $\tilde{S}_t = S_0 \exp(\sigma W^{\mathbb{Q}}_t - \sigma^2 t/2)$, it is a geometric Brownian motion with zero drift, which is a true martingale (as it is a positive exponential martingale with $\mathbb{E}^{\mathbb{Q}}[\tilde{S}_t] = S_0$ for all $t$). This confirms that $e^{-rt} S_t$ is a $\mathbb{Q}$-martingale.

---

**Exercise 5.** A one-period market has $n = 4$ states and $d = 2$ risky assets. What is the dimension of $\ker(X^T)$? How many free parameters does the set of EMMs have? How many additional risky assets (with linearly independent payoffs) would be needed to make the market complete?

??? success "Solution to Exercise 5"
    The payoff matrix $X$ is $n \times d = 4 \times 2$. The kernel of $X^T$ has dimension

    $$
    \dim(\ker(X^T)) = n - \operatorname{rank}(X) = 4 - \operatorname{rank}(X)
    $$

    Since $d = 2$, we have $\operatorname{rank}(X) \leq 2$. Generically (assuming the two columns are linearly independent), $\operatorname{rank}(X) = 2$, so

    $$
    \dim(\ker(X^T)) = 4 - 2 = 2
    $$

    The set of EMMs is the intersection of this 2-dimensional kernel with the affine hyperplane $\{\sum q_i = 1\}$ and the positivity constraints $q_i > 0$. The affine constraint reduces the dimension by 1, so the EMM set is generically a 1-dimensional family (a line segment in the interior of the 4-simplex). This means there is **one free parameter** in the set of EMMs.

    For completeness, we need $\operatorname{rank}(X) = n - 1 = 3$, which requires $d \geq 3$. Since we currently have $d = 2$, we need

    $$
    3 - 2 = 1
    $$

    additional risky asset with a payoff vector that is linearly independent of the existing two columns. This would bring $\operatorname{rank}(X) = 3 = n - 1$, making $\dim(\ker(X^T)) = 1$ and the EMM unique.

---

**Exercise 6.** Explain the distinction between "no arbitrage" (NA) and "no free lunch with vanishing risk" (NFLVR) in continuous-time models. Why is NFLVR strictly stronger than NA? Provide an intuitive description of a "free lunch with vanishing risk" that is not an outright arbitrage.

??? success "Solution to Exercise 6"
    **No Arbitrage (NA)** requires that no single admissible self-financing strategy $\theta$ can achieve $V_0(\theta) = 0$, $V_T(\theta) \geq 0$ a.s., and $\mathbb{P}(V_T(\theta) > 0) > 0$. This rules out exact risk-free profits.

    **No Free Lunch with Vanishing Risk (NFLVR)** is strictly stronger. It requires that there is no sequence of admissible strategies $(\theta_n)$ with $V_0(\theta_n) = 0$ and payoffs $f_n = V_T(\theta_n)$ such that $f_n \geq -\varepsilon_n$ (with $\varepsilon_n \to 0$) and $f_n$ converges (in an appropriate sense) to some $f \geq 0$ with $\mathbb{P}(f > 0) > 0$.

    **Why NFLVR is strictly stronger:** NFLVR rules out not only outright arbitrage but also **approximate arbitrage** that becomes arbitrarily close to risk-free. NA only checks individual strategies; NFLVR checks limits of strategy sequences.

    **Intuitive example of a free lunch with vanishing risk that is not an outright arbitrage:** Consider a sequence of zero-cost strategies where the $n$-th strategy produces a payoff satisfying $V_T(\theta_n) \geq -1/n$ (the downside risk vanishes) and $V_T(\theta_n) \to 1$ in probability. No single strategy is an arbitrage because each has a small potential loss of up to $1/n$. But the sequence approximates a riskless profit of $1$ with losses that shrink to zero. An investor who follows strategy $\theta_n$ for large $n$ takes negligible risk for a near-certain profit -- economically indistinguishable from arbitrage.

    In finite-state models, NA and NFLVR are equivalent (every convergent sequence of payoffs in a finite-dimensional space has its limit attained). The distinction matters only in infinite-dimensional continuous-time models, where the strategy space is rich enough for limiting arguments to produce "free lunches" that individual strategies cannot.
