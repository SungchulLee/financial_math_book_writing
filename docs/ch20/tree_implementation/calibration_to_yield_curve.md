# Calibration to Yield Curve on Tree

The trinomial tree from the previous section discretizes the zero-mean process $x_t$ on a recombining grid. To price derivatives consistently with the market, the tree must reproduce the initial zero-coupon bond curve $P^M(0, T)$ for all maturities. This is achieved by choosing the shift $\alpha_i$ at each time step $t_i$ so that the tree-implied bond prices match the market. The key tool is the Arrow-Debreu price, which propagates through the tree and enables efficient calibration.

## Arrow-Debreu Prices

Recall (see [§ risk-neutral](../../ch04/risk_neutral/martingale_and_no_arbitrage.md)) that an Arrow-Debreu (state) price is the present value of a digital claim paying $\$1$ in one state. For the tree,

$$
Q_{ij} = \mathbb{E}^{\mathbb{Q}}\!\left[\frac{\mathbf{1}_{\{x_{t_i} = j\Delta x\}}}{M(t_i)}\right], \quad Q_{0,0} = 1.
$$

## Forward Propagation

Arrow-Debreu prices propagate forward through the tree. If node $(i, j)$ connects to nodes $(i+1, j+k_1)$, $(i+1, j+k_2)$, $(i+1, j+k_3)$ with probabilities $p_u, p_m, p_d$ (where $k_1, k_2, k_3$ depend on the branching pattern), then node $(i, j)$ contributes to the Arrow-Debreu prices at time $t_{i+1}$:

$$
Q_{i+1, j+k_\ell} \mathrel{+}= Q_{ij}\,p_\ell\,e^{-r_{ij}\,\Delta t}
$$

for $\ell = 1, 2, 3$ (up, middle, down), where $r_{ij} = \alpha_i + j\,\Delta x$ is the short rate at node $(i, j)$ and the discount factor $e^{-r_{ij}\Delta t}$ accounts for the time value of money over one step.

The full propagation from time $t_i$ to $t_{i+1}$ is

$$
Q_{i+1, m} = \sum_{j} Q_{ij}\,p(j \to m)\,e^{-(\alpha_i + j\,\Delta x)\,\Delta t}
$$

where $p(j \to m)$ is the transition probability from node $j$ to node $m$ (zero if not connected).

## Fitting the Initial Yield Curve

The tree-implied zero-coupon bond price for maturity $t_{i+1}$ is the sum of all Arrow-Debreu prices at time $t_{i+1}$, discounted by the final step. Equivalently, using the Arrow-Debreu prices at time $t_i$:

$$
P^{\text{tree}}(0, t_{i+1}) = \sum_{j} Q_{ij}\,e^{-(\alpha_i + j\,\Delta x)\,\Delta t}
$$

Setting this equal to the market price:

$$
P^M(0, t_{i+1}) = e^{-\alpha_i\,\Delta t} \sum_{j} Q_{ij}\,e^{-j\,\Delta x\,\Delta t}
$$

Solving for $\alpha_i$:

$$
\alpha_i = \frac{1}{\Delta t}\left[\ln\!\left(\sum_{j} Q_{ij}\,e^{-j\,\Delta x\,\Delta t}\right) - \ln P^M(0, t_{i+1})\right]
$$

**Proposition.** The shift $\alpha_i$ is uniquely determined by the market bond price $P^M(0, t_{i+1})$ and the Arrow-Debreu prices $\{Q_{ij}\}$ at time $t_i$. The formula requires only the Arrow-Debreu prices at the current time slice, not the entire tree history.

???+ note "Proof"
    The function $f(\alpha) = e^{-\alpha\Delta t}\sum_j Q_{ij}e^{-j\Delta x\Delta t}$ is strictly decreasing in $\alpha$ (since $Q_{ij} > 0$ and $\Delta t > 0$), continuous, with $f(\alpha) \to \infty$ as $\alpha \to -\infty$ and $f(\alpha) \to 0$ as $\alpha \to \infty$. Therefore, for any $P^M(0, t_{i+1}) > 0$, there exists a unique $\alpha_i$ solving $f(\alpha_i) = P^M(0, t_{i+1})$. The explicit formula follows by taking logarithms. $\square$

## Calibration Algorithm

The complete calibration procedure is:

**Algorithm (Hull-White Tree Calibration).**

1. Set $Q_{0,0} = 1$ and choose $\alpha_0 = r_0 = f^M(0,0)$ (the initial short rate)
2. For $i = 0, 1, \ldots, N-1$:
    - (a) Compute $\alpha_i$ from the Arrow-Debreu prices at time $t_i$:

$$
\alpha_i = \frac{1}{\Delta t}\left[\ln\!\left(\sum_{j} Q_{ij}\,e^{-j\,\Delta x\,\Delta t}\right) - \ln P^M(0, t_{i+1})\right]
$$

   - (b) Set the short rate at each node: $r_{ij} = \alpha_i + j\,\Delta x$
   - (c) Propagate Arrow-Debreu prices to time $t_{i+1}$:

$$
Q_{i+1,m} = \sum_{j} Q_{ij}\,p(j \to m)\,e^{-r_{ij}\,\Delta t}
$$

!!! tip "Efficiency"
    The calibration is performed in a single forward pass through the tree, with $O(j_{\max})$ work per time step. The total cost is $O(N \cdot j_{\max})$, the same as constructing the tree itself.

## Consistency Verification

After calibration, the tree-implied bond prices should match the market curve to machine precision:

$$
P^{\text{tree}}(0, t_i) = \sum_{j} Q_{ij} \approx \sum_{j} Q_{i-1,j}\,e^{-r_{i-1,j}\,\Delta t} = P^M(0, t_i)
$$

for all $i = 1, \ldots, N$. The first equality holds because Arrow-Debreu prices are themselves discounted state prices summing to the bond price. Any discrepancy indicates a bug in the implementation.

???+ example "Three-Step Calibration Example"
    Consider $\lambda = 0.1$, $\sigma = 0.01$, $\Delta t = 1$, with market bond prices $P^M(0,1) = 0.97$, $P^M(0,2) = 0.94$, $P^M(0,3) = 0.91$.

    **Step 0**: $Q_{0,0} = 1$, $\Delta x = 0.01\sqrt{3} \approx 0.01732$.

    **Step 1** ($i = 0$): $\alpha_0 = -\ln(0.97)/1 \approx 0.03046$.

    Rates: $r_{0,0} = 0.03046$. Propagate:

    - $Q_{1,1} = 1 \cdot p_u \cdot e^{-0.03046} = (1/6) \cdot 0.97 \approx 0.1617$
    - $Q_{1,0} = 1 \cdot p_m \cdot e^{-0.03046} = (2/3) \cdot 0.97 \approx 0.6467$
    - $Q_{1,-1} = 1 \cdot p_d \cdot e^{-0.03046} = (1/6) \cdot 0.97 \approx 0.1617$

    **Step 2** ($i = 1$): Compute $\alpha_1$ from $\sum_j Q_{1,j}e^{-j\Delta x} = 0.1617 e^{-0.01732} + 0.6467 + 0.1617 e^{0.01732}$. Solve $\alpha_1$ to match $P^M(0,2) = 0.94$.

    The procedure continues iteratively for each time step.

## Relationship to Continuous-Time Calibration

Recall (see [§ HW model](../model_definition/hull_white_sde_and_mean_reversion.md)) the continuous-time $\theta(t)$ formula and (see [§ HW short rate](../short_rate/short_rate_solution.md)) the decomposition $\alpha(t) = f^M(0,t) + \frac{\sigma^2}{2\lambda^2}(1 - e^{-\lambda t})^2$. As $\Delta t \to 0$, the discrete shift $\alpha_i \to \alpha(t_i)$.

## Summary

Calibrating the Hull-White trinomial tree to the initial yield curve determines the shift $\alpha_i$ at each time step using Arrow-Debreu prices. The Arrow-Debreu prices propagate forward through the tree via $Q_{i+1,m} = \sum_j Q_{ij}\,p(j \to m)\,e^{-r_{ij}\Delta t}$, and the shift is found from $\alpha_i = (\ln\sum_j Q_{ij}e^{-j\Delta x\Delta t} - \ln P^M(0, t_{i+1}))/\Delta t$. This procedure is exact by construction, matching the market bond curve to machine precision. The calibrated tree is then ready for derivative pricing via backward induction, which is covered in the next section.

---

## Exercises

**Exercise 1.** Explain the financial meaning of an Arrow-Debreu price $Q_{ij}$. Why is $Q_{0,0} = 1$? Show that $\sum_j Q_{ij} = P^{\text{tree}}(0, t_i)$ by interpreting the sum as the price of a zero-coupon bond maturing at $t_i$.

??? success "Solution to Exercise 1"
    The Arrow-Debreu price $Q_{ij}$ represents the present value at time $0$ of a security that pays \$1 if the process reaches node $(i, j)$ at time $t_i$ and pays nothing otherwise. Financially, it is the price of a digital claim on a specific state of the world at time $t_i$.

    **Why $Q_{0,0} = 1$:** At time $0$, the tree starts at the single root node $(0, 0)$ with certainty. A claim paying \$1 at node $(0,0)$ is a sure payment of \$1 right now, so its present value is $1$.

    **Sum equals bond price:** A zero-coupon bond maturing at $t_i$ pays \$1 regardless of which node is reached at $t_i$. This payoff can be replicated by holding one unit of every Arrow-Debreu security for time $t_i$:

    $$
    P^{\text{tree}}(0, t_i) = \sum_{j} Q_{ij} \cdot 1 = \sum_{j} Q_{ij}
    $$

    This holds because Arrow-Debreu prices partition the total bond price across all possible states: $Q_{ij}$ is the contribution from state $j$ to the bond price.

---

**Exercise 2.** In the three-step calibration example, complete Step 2: compute $\alpha_1$ explicitly from the Arrow-Debreu prices $Q_{1,1} \approx 0.1617$, $Q_{1,0} \approx 0.6467$, $Q_{1,-1} \approx 0.1617$ with $\Delta x \approx 0.01732$ and $P^M(0,2) = 0.94$. Then propagate the Arrow-Debreu prices to time step 2.

??? success "Solution to Exercise 2"
    With $Q_{1,1} \approx 0.1617$, $Q_{1,0} \approx 0.6467$, $Q_{1,-1} \approx 0.1617$, $\Delta x \approx 0.01732$, and $\Delta t = 1$:

    First compute $\sum_j Q_{1,j}\,e^{-j\,\Delta x\,\Delta t}$:

    $$
    S = Q_{1,1}\,e^{-0.01732} + Q_{1,0}\,e^{0} + Q_{1,-1}\,e^{0.01732}
    $$

    $$
    S = 0.1617 \times 0.98283 + 0.6467 \times 1 + 0.1617 \times 1.01747
    $$

    $$
    S \approx 0.15890 + 0.64670 + 0.16452 = 0.97012
    $$

    Now solve for $\alpha_1$:

    $$
    \alpha_1 = \frac{1}{1}\left[\ln(0.97012) - \ln(0.94)\right] = \ln(0.97012) - \ln(0.94)
    $$

    $$
    \alpha_1 \approx (-0.03033) - (-0.06188) = 0.03155
    $$

    The short rates at time step 1 are $r_{1,j} = 0.03155 + j \times 0.01732$:

    - $r_{1,1} = 0.04887$
    - $r_{1,0} = 0.03155$
    - $r_{1,-1} = 0.01423$

    Propagating Arrow-Debreu prices to time step 2 (using normal branching with $p_u = 1/6$, $p_m = 2/3$, $p_d = 1/6$ at $j = 0$ and the appropriate probabilities at $j = \pm 1$):

    For $j = 0$: $p_u = 1/6$, $p_m = 2/3$, $p_d = 1/6$. Each contribution is $Q_{1,0}\,p_\ell\,e^{-r_{1,0}}$.

    For $j = \pm 1$: the probabilities include the $j\lambda\Delta t$ corrections.

    Each node at time step 2 receives contributions from the (up to three) nodes at time step 1 that connect to it, weighted by the respective transition probabilities and discount factors $e^{-r_{1,j}}$.

---

**Exercise 3.** The calibration formula $\alpha_i = \frac{1}{\Delta t}[\ln(\sum_j Q_{ij}e^{-j\Delta x\Delta t}) - \ln P^M(0,t_{i+1})]$ requires the function $f(\alpha) = e^{-\alpha\Delta t}\sum_j Q_{ij}e^{-j\Delta x\Delta t}$ to be strictly decreasing. Prove this monotonicity property and explain why it guarantees uniqueness of $\alpha_i$.

??? success "Solution to Exercise 3"
    The function $f(\alpha) = e^{-\alpha\Delta t}\sum_j Q_{ij}\,e^{-j\,\Delta x\,\Delta t}$ can be written as

    $$
    f(\alpha) = e^{-\alpha\Delta t} \cdot S
    $$

    where $S = \sum_j Q_{ij}\,e^{-j\,\Delta x\,\Delta t}$ is a positive constant (independent of $\alpha$, since $Q_{ij} > 0$ for all nodes $j$ reachable at time $t_i$).

    Taking the derivative with respect to $\alpha$:

    $$
    f'(\alpha) = -\Delta t\,e^{-\alpha\Delta t}\,S < 0
    $$

    since $\Delta t > 0$, $S > 0$. Therefore $f$ is strictly decreasing.

    For uniqueness: since $f$ is continuous, strictly decreasing, with $\lim_{\alpha \to -\infty} f(\alpha) = +\infty$ and $\lim_{\alpha \to +\infty} f(\alpha) = 0$, the intermediate value theorem guarantees that for any target value $P^M(0, t_{i+1}) > 0$, there exists exactly one $\alpha_i$ satisfying $f(\alpha_i) = P^M(0, t_{i+1})$. Strict monotonicity rules out multiple solutions.

---

**Exercise 4.** After calibration, verify that $\sum_j Q_{i,j} = P^M(0, t_i)$ for each time step $i$. Explain why any discrepancy indicates a bug and describe how to diagnose common implementation errors (sign errors, off-by-one indexing, incorrect branching probabilities).

??? success "Solution to Exercise 4"
    After calibration, the identity $\sum_j Q_{i,j} = P^M(0, t_i)$ must hold at every time step $i$ by construction:

    - At $i = 0$: $Q_{0,0} = 1 = P^M(0, 0)$ trivially.
    - At $i = 1$: $\sum_j Q_{1,j} = Q_{0,0}\,e^{-r_{0,0}\Delta t}\sum_\ell p_\ell = e^{-\alpha_0\Delta t}$, and $\alpha_0$ is chosen so that $e^{-\alpha_0\Delta t} = P^M(0, t_1)$.
    - Inductively, $\alpha_i$ ensures that $\sum_j Q_{i+1,j} = P^M(0, t_{i+1})$ at each step.

    Any discrepancy signals a bug. Common implementation errors include:

    - **Sign errors in $\alpha_i$:** Using $+\alpha_i$ instead of $-\alpha_i$ in the discount factor $e^{-r_{ij}\Delta t}$, or a sign error in the calibration formula.
    - **Off-by-one indexing:** Propagating Arrow-Debreu prices to the wrong time step, or using $Q_{i+1,j}$ where $Q_{i,j}$ is intended.
    - **Incorrect branching probabilities:** Using normal branching at nodes where non-normal branching should apply (i.e., not switching at $|j| > j_{\max}$), or using wrong successor indices for up/down branching.
    - **Missing contributions:** Not summing over all predecessor nodes when propagating $Q_{i+1,m}$, especially at boundary nodes where branching patterns differ.

    Diagnosing: check $\sum_j Q_{i,j}$ at each time step and identify the first $i$ where the error appears.

---

**Exercise 5.** As $\Delta t \to 0$, the discrete shift $\alpha_i$ converges to $f^M(0,t_i) + \frac{\sigma^2}{2\lambda^2}(1 - e^{-\lambda t_i})^2$. Verify this for $i = 0$ by showing that $\alpha_0 = -\ln P^M(0,\Delta t)/\Delta t \to f^M(0,0) = r_0$ as $\Delta t \to 0$.

??? success "Solution to Exercise 5"
    At $i = 0$, the calibration formula gives

    $$
    \alpha_0 = \frac{1}{\Delta t}\left[\ln(Q_{0,0}\,e^{-0 \cdot \Delta x \cdot \Delta t}) - \ln P^M(0, \Delta t)\right] = \frac{1}{\Delta t}\left[\ln 1 - \ln P^M(0, \Delta t)\right]
    $$

    $$
    \alpha_0 = -\frac{\ln P^M(0, \Delta t)}{\Delta t}
    $$

    As $\Delta t \to 0$, using the relationship between bond prices and instantaneous forward rates:

    $$
    P^M(0, \Delta t) = \exp\!\left(-\int_0^{\Delta t} f^M(0, s)\,ds\right) \approx \exp(-f^M(0, 0)\,\Delta t)
    $$

    for small $\Delta t$. Therefore

    $$
    \alpha_0 \approx -\frac{-f^M(0, 0)\,\Delta t}{\Delta t} = f^M(0, 0) = r_0
    $$

    This confirms that $\alpha_0 \to r_0$ as $\Delta t \to 0$, consistent with the continuous-time limit $\alpha(0) = f^M(0, 0) + \frac{\sigma^2}{2\lambda^2}(1 - e^0)^2 = f^M(0, 0) = r_0$.

---

**Exercise 6.** The forward propagation formula $Q_{i+1,m} = \sum_j Q_{ij}p(j \to m)e^{-r_{ij}\Delta t}$ has the same cost as one time step of backward induction. Explain why the total calibration cost is $O(N \cdot j_{\max})$ and compare this to the cost of calibrating a non-recombining tree.

??? success "Solution to Exercise 6"
    At each time step $i$, the forward propagation computes

    $$
    Q_{i+1, m} = \sum_{j} Q_{ij}\,p(j \to m)\,e^{-r_{ij}\Delta t}
    $$

    For each node $j$ at time $t_i$, there are exactly 3 successor nodes, so the work per source node is $O(1)$. The number of nodes at time step $i$ is at most $2j_{\max} + 1$, so the work per time step is $O(j_{\max})$. Over $N$ time steps, the total cost is $O(N \cdot j_{\max})$.

    This is the same cost as one pass of backward induction, because the structure of the computation is identical: at each time step, each node contributes to (or receives from) exactly 3 neighbors.

    **Comparison to non-recombining tree:** A non-recombining tree has $3^i$ nodes at time step $i$. Calibrating such a tree requires visiting all nodes, so the total cost is $\sum_{i=0}^{N} 3^i = O(3^N)$, which is exponential in $N$. For $N = 100$ time steps, this is computationally infeasible. The recombining property reduces the cost from exponential to linear in $N$ (for fixed $j_{\max}$).

---

**Exercise 7.** Describe how you would modify the calibration algorithm if the market provides bond prices $P^M(0,T_k)$ at irregularly spaced maturities $T_1, T_2, \ldots$ that do not coincide with the tree time steps. What interpolation method would you use, and what are the risks of interpolation error?

??? success "Solution to Exercise 7"
    When market bond prices are available only at irregularly spaced maturities $T_1 < T_2 < \cdots < T_K$ that do not coincide with the tree time steps $t_0, t_1, \ldots, t_N$, the calibration algorithm requires $P^M(0, t_{i+1})$ at each tree time step. The modification involves two steps:

    **Step 1: Interpolate the market curve.** Construct a smooth discount curve from the observed bond prices. Common methods include:

    - **Log-linear interpolation on discount factors:** Interpolate $\ln P^M(0, T)$ linearly in $T$, which ensures positivity of discount factors and corresponds to piecewise constant forward rates.
    - **Cubic spline on zero rates:** Fit a cubic spline to $y(T) = -\ln P^M(0,T)/T$, giving smooth zero rates and forward rates.
    - **Nelson-Siegel or Svensson parametric models:** Fit a parsimonious functional form to the zero curve.

    **Step 2: Use interpolated values in calibration.** At each tree time step $t_{i+1}$, evaluate $P^M(0, t_{i+1})$ from the interpolated curve and apply the standard calibration formula for $\alpha_i$.

    **Risks of interpolation error:**

    - Interpolated forward rates may exhibit unphysical oscillations (especially with cubic splines), leading to oscillatory $\alpha_i$ values.
    - Between market maturities, the interpolated curve is unconstrained by data, so the tree may price instruments at non-observed maturities inaccurately.
    - Non-smooth interpolation (e.g., piecewise linear on discount factors) produces discontinuous forward rates, which can cause instability in $\alpha_i$.
    - The calibration is only as accurate as the interpolation: systematic interpolation bias translates directly into systematic pricing error for all derivatives.
