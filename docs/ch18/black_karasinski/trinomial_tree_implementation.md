# Trinomial Tree Implementation

The trinomial tree is the standard numerical method for pricing derivatives under the Black-Karasinski model. Originally developed by Hull and White for their extended Vasicek model, the trinomial tree adapts naturally to the BK setting by constructing the tree in the log-rate space $x = \ln r$, where the dynamics are linear (Ornstein-Uhlenbeck). The tree simultaneously calibrates the time-dependent drift $\theta(t)$ to match the observed term structure and prices derivatives by backward induction. This section presents the complete construction algorithm, derives the branching probabilities, explains the forward-induction calibration procedure, and analyzes convergence.

---

## Tree structure in log-rate space

The tree is built for $x_t = \ln r_t$ rather than $r_t$ directly, because $x_t$ follows the linear OU process

$$
dx_t = [\theta(t) - ax_t]\,dt + \sigma\,dW_t
$$

### Grid parameters

Choose a time step $\Delta t$ and set the log-rate spacing to

$$
\Delta x = \sigma\sqrt{3\Delta t}
$$

This choice ensures that the branching probabilities remain in the interval $[0, 1]$ for the standard trinomial geometry. The time grid is $t_0 = 0, t_1 = \Delta t, \ldots, t_N = N\Delta t$, and at each time step $t_k$, the tree has nodes at

$$
x_j = j\,\Delta x, \qquad j = -j_{\max}, \ldots, -1, 0, 1, \ldots, j_{\max}
$$

where $j_{\max}$ is chosen to cover the range of likely log-rate values (typically $j_{\max} = \lceil 0.184/(a\Delta t) \rceil$, following Hull-White).

---

## Branching geometry

From each node $(t_k, x_j)$, the tree branches to three successor nodes at time $t_{k+1}$. The **standard branching** connects to nodes $x_{j+1}$, $x_j$, and $x_{j-1}$ (up, middle, down). However, when $|j|$ is large, the standard branching may produce negative probabilities. Two alternative geometries handle this:

- **Up branching**: connects to $x_{j+2}$, $x_{j+1}$, $x_j$ (used when $j$ is very negative, i.e., rates are low)
- **Down branching**: connects to $x_j$, $x_{j-1}$, $x_{j-2}$ (used when $j$ is very positive, i.e., rates are high)

The switch criterion: use standard branching if $|j| \leq j_{\max}$; otherwise, use up or down branching as appropriate.

---

## Branching probabilities

At node $(t_k, x_j)$, the probabilities $p_u$, $p_m$, $p_d$ must match the conditional mean and variance of $x_{t_{k+1}}$ given $x_{t_k} = x_j$:

$$
\mathbb{E}[x_{t_{k+1}} - x_j] = [\theta(t_k) - ax_j]\Delta t := \mu_j\,\Delta t
$$

$$
\text{Var}[x_{t_{k+1}} - x_j] = \sigma^2\Delta t
$$

$$
p_u + p_m + p_d = 1
$$

### Standard branching (successor nodes at xⱼ₊₁, xⱼ, xⱼ₋₁)

The three equations yield:

$$
p_u = \frac{1}{6} + \frac{(\mu_j\Delta t)^2}{2\Delta x^2} + \frac{\mu_j\Delta t}{2\Delta x}
$$

$$
p_m = \frac{2}{3} - \frac{(\mu_j\Delta t)^2}{\Delta x^2}
$$

$$
p_d = \frac{1}{6} + \frac{(\mu_j\Delta t)^2}{2\Delta x^2} - \frac{\mu_j\Delta t}{2\Delta x}
$$

With $\Delta x = \sigma\sqrt{3\Delta t}$, these simplify at leading order to:

$$
p_u \approx \frac{1}{6} + \frac{\mu_j\sqrt{\Delta t}}{2\sigma\sqrt{3}}, \qquad p_m \approx \frac{2}{3}, \qquad p_d \approx \frac{1}{6} - \frac{\mu_j\sqrt{\Delta t}}{2\sigma\sqrt{3}}
$$

### Up branching (successor nodes at xⱼ₊₂, xⱼ₊₁, xⱼ)

$$
p_u = \frac{1}{6} + \frac{(\mu_j\Delta t)^2}{2\Delta x^2} - \frac{\mu_j\Delta t}{2\Delta x}
$$

$$
p_m = -\frac{1}{3} - \frac{(\mu_j\Delta t)^2}{\Delta x^2} + \frac{2\mu_j\Delta t}{\Delta x}
$$

$$
p_d = \frac{7}{6} + \frac{(\mu_j\Delta t)^2}{2\Delta x^2} - \frac{3\mu_j\Delta t}{2\Delta x}
$$

(Down branching is analogous with signs reversed.)

!!! note "Probability validity"
    The probabilities must satisfy $0 \leq p_u, p_m, p_d \leq 1$. The choice $\Delta x = \sigma\sqrt{3\Delta t}$ ensures this for standard branching when $|\mu_j\Delta t| \leq \Delta x$. The alternative branchings extend the valid range.

---

## Forward induction: calibrating the time-dependent drift

The function $\theta(t_k)$ is determined at each time step so that the tree reproduces the market discount factors $P^{\text{mkt}}(0, t_{k+1})$.

### Arrow-Debreu prices

Define $Q(k, j)$ as the present value at time $0$ of a security that pays \$1 if node $(t_k, x_j)$ is reached and \$0 otherwise. These **Arrow-Debreu (state) prices** satisfy:

$$
Q(0, 0) = 1 \quad (\text{initial condition})
$$

$$
Q(k+1, j') = \sum_{j \to j'} Q(k, j)\,p_{j \to j'}\,e^{-e^{x_j}\Delta t}
$$

where the sum is over all nodes $j$ at time $t_k$ that branch to $j'$ at time $t_{k+1}$, and $e^{-e^{x_j}\Delta t}$ is the one-period discount factor at node $j$.

### Calibration condition

The model discount factor to time $t_{k+1}$ must equal the market value:

$$
P^{\text{mkt}}(0, t_{k+1}) = \sum_j Q(k+1, j)
$$

Since the Arrow-Debreu prices at step $k+1$ depend on $\theta(t_k)$ (through the branching probabilities), this equation implicitly determines $\theta(t_k)$. The equation is nonlinear in $\theta(t_k)$ (because $\theta$ enters the probabilities, which multiply the state prices), so it must be solved iteratively --- typically by Newton's method or bisection.

### Algorithm

For $k = 0, 1, \ldots, N-1$:

1. Guess $\theta(t_k)$
2. Compute branching probabilities $p_u(j), p_m(j), p_d(j)$ for all nodes $j$ at step $k$
3. Compute Arrow-Debreu prices $Q(k+1, j')$ using the forward formula
4. Check if $\sum_j Q(k+1, j) = P^{\text{mkt}}(0, t_{k+1})$
5. If not, adjust $\theta(t_k)$ and repeat from step 2

This forward-induction procedure determines $\theta(t_k)$ sequentially, one time step at a time.

---

## Backward induction: pricing derivatives

Once the tree is fully calibrated, derivative prices are computed by backward induction.

### Zero-coupon bonds

For a bond maturing at $T = t_N$:

1. Set $V(N, j) = 1$ for all nodes $j$ at time $t_N$
2. For $k = N-1, N-2, \ldots, 0$:

$$
V(k, j) = e^{-e^{x_j}\Delta t}\left[p_u\,V(k+1, j_u) + p_m\,V(k+1, j_m) + p_d\,V(k+1, j_d)\right]
$$

where $j_u, j_m, j_d$ are the successor node indices.

### European options on bonds

For a European call with expiry $t_K$ and strike $K$ on a bond maturing at $T > t_K$:

1. At expiry nodes $(t_K, j)$: compute the bond price $P(t_K, T)$ at each node (by a separate backward induction from $T$ to $t_K$)
2. Set $V(K, j) = \max(P(t_K, T, j) - K, 0)$
3. Roll backward from $t_K$ to $t_0$ using the discounted expectation formula

### American-style options

For Bermudan or American options, add an early exercise check at each exercise date:

$$
V(k, j) = \max\!\left(h(k, j),\;e^{-e^{x_j}\Delta t}\left[p_u\,V(k+1, j_u) + p_m\,V(k+1, j_m) + p_d\,V(k+1, j_d)\right]\right)
$$

where $h(k, j)$ is the exercise payoff at node $(k, j)$.

!!! tip "Trees excel at American-style pricing"
    The ability to check early exercise at every node makes trinomial trees particularly well-suited for Bermudan swaptions and callable bonds. These products are the main practical use case for the BK trinomial tree.

---

## Convergence

The trinomial tree converges to the continuous-time BK bond price as $\Delta t \to 0$. The convergence rate depends on the smoothness of the payoff:

| Payoff | Convergence rate |
|--------|:----------------:|
| Bond price (smooth) | $O(\Delta t)$ |
| European option | $O(\sqrt{\Delta t})$ |
| American option | $O(\sqrt{\Delta t})$ |

Richardson extrapolation can improve the bond-price convergence to $O(\Delta t^2)$ by combining results from two different step sizes $\Delta t$ and $\Delta t / 2$.

A practical tree with $N = 100$ steps per year typically provides 1--2 basis points of accuracy for bond prices and 5--10 basis points for option prices.

---

## Summary

The trinomial tree for the Black-Karasinski model operates in log-rate space, where the OU dynamics yield simple branching probabilities. The tree geometry uses standard, up, or down branching to ensure valid probabilities across the entire rate range. Forward induction calibrates $\theta(t_k)$ at each time step by matching the model discount factor to market data, and backward induction prices derivatives by rolling discounted expectations from maturity to the present. The tree naturally handles American-style exercise, making it the preferred method for Bermudan swaptions and callable bonds under BK. Convergence is first-order in $\Delta t$ for smooth payoffs and can be improved by Richardson extrapolation.

---

## Exercises

**Exercise 1.** Given $\sigma = 0.15$ and $\Delta t = 0.02$ year, compute the log-rate spacing $\Delta x = \sigma\sqrt{3\Delta t}$. If $a = 0.08$, compute $j_{\max} = \lceil 0.184/(a\Delta t) \rceil$. How many total nodes exist at a single time step, and what are the minimum and maximum short rates $r_{\min} = e^{-j_{\max}\Delta x}$ and $r_{\max} = e^{j_{\max}\Delta x}$?

??? success "Solution to Exercise 1"
    With $\sigma = 0.15$ and $\Delta t = 0.02$:

    **Log-rate spacing**:

    $$
    \Delta x = \sigma\sqrt{3\Delta t} = 0.15\sqrt{3 \times 0.02} = 0.15\sqrt{0.06} = 0.15 \times 0.24495 = 0.03674
    $$

    **Maximum node index** with $a = 0.08$:

    $$
    j_{\max} = \left\lceil\frac{0.184}{a\,\Delta t}\right\rceil = \left\lceil\frac{0.184}{0.08 \times 0.02}\right\rceil = \left\lceil\frac{0.184}{0.0016}\right\rceil = \lceil 115 \rceil = 115
    $$

    **Total nodes at a single time step**: $2j_{\max} + 1 = 2 \times 115 + 1 = 231$ nodes.

    **Rate range**: The log-rate at node $j$ is $x_j = j \cdot \Delta x$, so the short rate is $r_j = e^{j \cdot \Delta x}$:

    $$
    r_{\min} = e^{-j_{\max} \cdot \Delta x} = e^{-115 \times 0.03674} = e^{-4.225} = 0.01462 \approx 1.46\%
    $$

    $$
    r_{\max} = e^{+j_{\max} \cdot \Delta x} = e^{+4.225} = 68.37 \approx 6{,}837\%
    $$

    The tree covers an extremely wide range of rates, from about 1.5% to nearly 6,800%, ensuring that even extreme tail events are captured. In practice, most of the probability mass is concentrated in a much narrower range near the central nodes.

---

**Exercise 2.** At a node with $j = 0$ (central node), show that the standard branching probabilities simplify to $p_u = \frac{1}{6} + \frac{\theta(t_k)^2\Delta t^2}{2\Delta x^2} + \frac{\theta(t_k)\Delta t}{2\Delta x}$, $p_m = \frac{2}{3} - \frac{\theta(t_k)^2\Delta t^2}{\Delta x^2}$, and $p_d = \frac{1}{6} + \frac{\theta(t_k)^2\Delta t^2}{2\Delta x^2} - \frac{\theta(t_k)\Delta t}{2\Delta x}$. For $\theta(t_k) = -0.30$, $\Delta t = 0.01$, $\Delta x = 0.03464$, verify these are all positive.

??? success "Solution to Exercise 2"
    At the central node $j = 0$, the conditional drift simplifies because $x_j = 0 \cdot \Delta x = 0$:

    $$
    \mu_0 = \theta(t_k) - a \cdot 0 \cdot \Delta x = \theta(t_k)
    $$

    Substituting into the standard branching formulas:

    $$
    p_u = \frac{1}{6} + \frac{(\theta(t_k)\Delta t)^2}{2\Delta x^2} + \frac{\theta(t_k)\Delta t}{2\Delta x}
    $$

    $$
    p_m = \frac{2}{3} - \frac{(\theta(t_k)\Delta t)^2}{\Delta x^2}
    $$

    $$
    p_d = \frac{1}{6} + \frac{(\theta(t_k)\Delta t)^2}{2\Delta x^2} - \frac{\theta(t_k)\Delta t}{2\Delta x}
    $$

    **Numerical verification** with $\theta(t_k) = -0.30$, $\Delta t = 0.01$, $\Delta x = 0.03464$:

    $$
    \theta \Delta t = -0.003, \qquad (\theta \Delta t)^2 = 9 \times 10^{-6}
    $$

    $$
    \frac{(\theta \Delta t)^2}{2\Delta x^2} = \frac{9 \times 10^{-6}}{2 \times 0.001200} = \frac{9 \times 10^{-6}}{0.002400} = 0.003750
    $$

    $$
    \frac{(\theta \Delta t)^2}{\Delta x^2} = 0.007500
    $$

    $$
    \frac{\theta \Delta t}{2\Delta x} = \frac{-0.003}{0.06928} = -0.04330
    $$

    Computing:

    $$
    p_u = 0.16667 + 0.003750 + (-0.04330) = 0.12712
    $$

    $$
    p_m = 0.66667 - 0.007500 = 0.65917
    $$

    $$
    p_d = 0.16667 + 0.003750 + 0.04330 = 0.21372
    $$

    **Verification**: $p_u + p_m + p_d = 0.12712 + 0.65917 + 0.21372 = 1.00001 \approx 1$ (rounding). All probabilities are positive: $p_u = 0.127 > 0$, $p_m = 0.659 > 0$, $p_d = 0.214 > 0$.

---

**Exercise 3.** Derive the three equations that determine the branching probabilities $p_u$, $p_m$, $p_d$ for standard branching. Specifically, let the successor nodes be at $x_j + \Delta x$, $x_j$, and $x_j - \Delta x$. Write the mean-matching equation, the variance-matching equation, and the probability-summing equation. Solve the $3 \times 3$ system to obtain the formulas given in the text.

??? success "Solution to Exercise 3"
    The three matching equations for standard branching with successor nodes at $x_j + \Delta x$, $x_j$, $x_j - \Delta x$ are:

    **Mean-matching**: The expected displacement must equal the drift times $\Delta t$:

    $$
    p_u(\Delta x) + p_m(0) + p_d(-\Delta x) = \mu_j \Delta t
    $$

    $$
    p_u - p_d = \frac{\mu_j \Delta t}{\Delta x} \tag{1}
    $$

    **Variance-matching**: The second moment must equal $\sigma^2 \Delta t + (\mu_j \Delta t)^2$ (variance plus squared mean):

    $$
    p_u(\Delta x)^2 + p_m(0)^2 + p_d(\Delta x)^2 = \sigma^2 \Delta t + (\mu_j \Delta t)^2
    $$

    $$
    (p_u + p_d)\Delta x^2 = \sigma^2 \Delta t + (\mu_j \Delta t)^2 \tag{2}
    $$

    **Probability sum**:

    $$
    p_u + p_m + p_d = 1 \tag{3}
    $$

    **Solving the system**: From (1), $p_u = p_d + \frac{\mu_j \Delta t}{\Delta x}$. From (2):

    $$
    p_u + p_d = \frac{\sigma^2 \Delta t + (\mu_j \Delta t)^2}{\Delta x^2}
    $$

    With $\Delta x^2 = 3\sigma^2 \Delta t$:

    $$
    p_u + p_d = \frac{\sigma^2 \Delta t + (\mu_j \Delta t)^2}{3\sigma^2 \Delta t} = \frac{1}{3} + \frac{(\mu_j \Delta t)^2}{\Delta x^2}
    $$

    Combining with $p_u - p_d = \mu_j \Delta t / \Delta x$:

    $$
    p_u = \frac{1}{2}\left[\frac{1}{3} + \frac{(\mu_j \Delta t)^2}{\Delta x^2} + \frac{\mu_j \Delta t}{\Delta x}\right] = \frac{1}{6} + \frac{(\mu_j \Delta t)^2}{2\Delta x^2} + \frac{\mu_j \Delta t}{2\Delta x}
    $$

    $$
    p_d = \frac{1}{2}\left[\frac{1}{3} + \frac{(\mu_j \Delta t)^2}{\Delta x^2} - \frac{\mu_j \Delta t}{\Delta x}\right] = \frac{1}{6} + \frac{(\mu_j \Delta t)^2}{2\Delta x^2} - \frac{\mu_j \Delta t}{2\Delta x}
    $$

    From (3):

    $$
    p_m = 1 - p_u - p_d = 1 - \frac{1}{3} - \frac{(\mu_j \Delta t)^2}{\Delta x^2} = \frac{2}{3} - \frac{(\mu_j \Delta t)^2}{\Delta x^2}
    $$

    These match the formulas given in the text.

---

**Exercise 4.** The Arrow-Debreu price $Q(k+1, j')$ is defined recursively. Suppose at time $t_1$ (one step after $t_0$) the standard branching from the root node $(t_0, 0)$ produces nodes $j' \in \{-1, 0, 1\}$ with probabilities $p_d$, $p_m$, $p_u$. With $r_0 = e^{x_0} = 0.05$ and $\Delta t = 0.5$ year, compute $Q(1, -1)$, $Q(1, 0)$, and $Q(1, 1)$, and verify that $\sum_{j'} Q(1, j') = e^{-r_0 \Delta t}$.

??? success "Solution to Exercise 4"
    At time $t_0$, the single root node has Arrow-Debreu price $Q(0, 0) = 1$ and log rate $x_0$ with $r_0 = e^{x_0} = 0.05$. Standard branching from this node produces successor nodes $j' \in \{-1, 0, 1\}$ at time $t_1$.

    The forward propagation formula is

    $$
    Q(1, j') = Q(0, 0) \cdot p_{0 \to j'} \cdot e^{-r_0 \Delta t}
    $$

    The one-period discount factor is

    $$
    e^{-r_0 \Delta t} = e^{-0.05 \times 0.5} = e^{-0.025} = 0.97531
    $$

    The Arrow-Debreu prices at $t_1$ are:

    $$
    Q(1, +1) = 1 \cdot p_u \cdot 0.97531 = 0.97531\,p_u
    $$

    $$
    Q(1, 0) = 1 \cdot p_m \cdot 0.97531 = 0.97531\,p_m
    $$

    $$
    Q(1, -1) = 1 \cdot p_d \cdot 0.97531 = 0.97531\,p_d
    $$

    **Verification**: Summing all Arrow-Debreu prices:

    $$
    \sum_{j'} Q(1, j') = 0.97531(p_u + p_m + p_d) = 0.97531 \times 1 = 0.97531 = e^{-r_0 \Delta t}
    $$

    This confirms the identity: the sum of Arrow-Debreu prices at $t_1$ equals the one-period discount factor from the root, which is the model's one-period bond price. This must equal the market discount factor $P^{\text{mkt}}(0, t_1) = e^{-r_0 \Delta t}$ for the calibration condition to hold at the first step. (At the first step, $\theta(t_0)$ is the only unknown and is chosen to make this equality hold.)

---

**Exercise 5.** Explain why the calibration of $\theta(t_k)$ is a nonlinear root-finding problem. What specifically makes the equation $\sum_j Q(k+1, j) = P^{\text{mkt}}(0, t_{k+1})$ nonlinear in $\theta(t_k)$? Would Newton's method or bisection be more robust for this problem, and why?

??? success "Solution to Exercise 5"
    The calibration equation $\sum_j Q(k+1, j) = P^{\text{mkt}}(0, t_{k+1})$ is nonlinear in $\theta(t_k)$ because the branching probabilities $p_u(j)$, $p_m(j)$, $p_d(j)$ at each node $j$ depend on the drift $\mu_j = \theta(t_k) - ax_j$, and this dependence is **quadratic** in $\theta(t_k)$:

    $$
    p_u = \frac{1}{6} + \frac{(\mu_j \Delta t)^2}{2\Delta x^2} + \frac{\mu_j \Delta t}{2\Delta x}
    $$

    The term $(\mu_j \Delta t)^2 = [(\theta_k - ax_j)\Delta t]^2$ contains $\theta_k^2$, making each probability a quadratic polynomial in $\theta_k$. When these probabilities multiply the Arrow-Debreu prices $Q(k, j)$ and the exponential discount factors $e^{-e^{x_j}\Delta t}$ (which do not depend on $\theta_k$), and the products are summed over $j$, the result is a quadratic function of $\theta_k$.

    **Bisection vs. Newton**: Bisection is more robust because:

    1. It requires only function evaluations (no derivatives), which are straightforward to compute.
    2. The function is monotonically decreasing (as argued in Exercise 4 of the Python implementation section), so bisection is guaranteed to converge given valid brackets.
    3. Newton's method requires the derivative $\partial(\sum_j Q(k+1,j))/\partial\theta_k$, which involves differentiating all branching probabilities with respect to $\theta_k$ --- analytically feasible but more complex to implement.
    4. Newton can fail if the initial guess is poor or if the function has inflection points near the root.

    In practice, Brent's method (as used in `scipy.optimize.brentq`) combines the reliability of bisection with the speed of interpolation, providing superlinear convergence while guaranteeing convergence. This is the standard choice in production implementations.

---

**Exercise 6.** For a European call option on a zero-coupon bond with expiry $t_K = 1$ year, strike $K = 0.95$, on a bond maturing at $T = 2$ years, describe the two-pass backward induction procedure. In the first pass, what terminal condition is set at $T$, and how far back is the induction performed? In the second pass, what values are set at $t_K$, and how is the option payoff computed at each node?

??? success "Solution to Exercise 6"
    The European call on a ZCB requires a **two-pass backward induction**.

    **First pass (bond price computation)**:

    1. At time $T = 2$ years (bond maturity), set $V^{\text{bond}}(T, x_j) = 1$ for all nodes $j$.
    2. Roll backward from $T = 2$ to $t_K = 1$ (option expiry), using

        $$
        V^{\text{bond}}(t_k, x_j) = e^{-e^{x_j}\Delta t}\left[p_u V^{\text{bond}}(t_{k+1}, j_u) + p_m V^{\text{bond}}(t_{k+1}, j_m) + p_d V^{\text{bond}}(t_{k+1}, j_d)\right]
        $$

    3. At $t_K = 1$, store $V^{\text{bond}}(t_K, x_j)$ at each node $j$. This is the bond price $P(1, 2; x_j)$ at each node.

    **Second pass (option pricing)**:

    1. At option expiry $t_K = 1$, compute the option payoff at each node:

        $$
        V^{\text{opt}}(t_K, x_j) = \max\!\left(V^{\text{bond}}(t_K, x_j) - K, 0\right) = \max\!\left(P(1, 2; x_j) - 0.95, 0\right)
        $$

    2. Roll backward from $t_K = 1$ to $t_0 = 0$:

        $$
        V^{\text{opt}}(t_k, x_j) = e^{-e^{x_j}\Delta t}\left[p_u V^{\text{opt}}(t_{k+1}, j_u) + p_m V^{\text{opt}}(t_{k+1}, j_m) + p_d V^{\text{opt}}(t_{k+1}, j_d)\right]
        $$

    3. Read $V^{\text{opt}}(0, x_0)$ as the European call price.

    The first pass rolls backward from $T$ to $t_K$ only (not to time 0), since the bond price is needed only at the option expiry nodes. The second pass rolls backward from $t_K$ to 0, using the option payoff computed from the first-pass bond prices.

---

**Exercise 7.** A Bermudan swaption allows exercise at annual dates $t_1, t_2, \ldots, t_5$ into a 5-year swap. At each exercise date, the holder compares the exercise value (swap value) with the continuation value. Write the backward induction equation that incorporates the early exercise decision. Explain why trinomial trees have an advantage over Monte Carlo for this product, and what role the node-by-node comparison plays in avoiding the need for regression-based continuation value estimation.

??? success "Solution to Exercise 7"
    At each exercise date $t_k \in \{t_1, t_2, \ldots, t_5\}$ and each node $(t_k, x_j)$, the Bermudan swaption holder decides whether to exercise. The backward induction equation is

    $$
    V(t_k, x_j) = \max\!\left(h(t_k, x_j),\; e^{-e^{x_j}\Delta t}\left[p_u V(t_{k+1}, j_u) + p_m V(t_{k+1}, j_m) + p_d V(t_{k+1}, j_d)\right]\right)
    $$

    where $h(t_k, x_j)$ is the exercise value: the value of entering into the underlying swap at node $(t_k, x_j)$. This swap value is computed by a separate backward induction of the swap's fixed and floating legs from the swap maturity back to $t_k$.

    At non-exercise dates (time steps between exercise dates), the standard continuation-only formula applies:

    $$
    V(t_k, x_j) = e^{-e^{x_j}\Delta t}\left[p_u V(t_{k+1}, j_u) + p_m V(t_{k+1}, j_m) + p_d V(t_{k+1}, j_d)\right]
    $$

    **Why trees have an advantage over Monte Carlo**:

    1. **Exact continuation value**: On a tree, the continuation value at each node is computed exactly (to within the tree discretization error) by backward induction. At node $(t_k, x_j)$, the discounted expected value $e^{-r_j\Delta t}[p_u V_{j_u} + p_m V_{j_m} + p_d V_{j_d}]$ uses the already-computed future option values, which are exact on the tree grid. There is no estimation error in the continuation value.

    2. **No regression needed**: Monte Carlo methods for early exercise (e.g., Longstaff-Schwartz) must estimate the continuation value at each exercise date by regressing future discounted payoffs on basis functions of the current state. This regression introduces estimation error, basis function selection risk, and potential bias (the exercise boundary is only approximately optimal). Trees bypass this entirely.

    3. **Node-by-node comparison**: The $\max(h, \text{continuation})$ comparison is performed independently at each node, using exact values on both sides. This produces the optimal exercise policy for the discretized tree. In Monte Carlo, the comparison is between the exact exercise value and an estimated (noisy) continuation value, leading to suboptimal exercise decisions and biased prices (the Longstaff-Schwartz estimator is biased low).

    4. **Computational efficiency**: For a one-factor model like BK, the tree has $O(N)$ nodes per time step, and backward induction is $O(N^2)$ total. Monte Carlo for Bermudan exercise requires $O(M \times N)$ with additional regression cost at each exercise date, and typically requires $M \gg N$ paths for adequate precision. The tree is generally faster and more accurate for one-factor problems.

    The main limitation of trees is dimensionality: for multi-factor models, trees become impractical (exponential growth in nodes), and Monte Carlo with Longstaff-Schwartz becomes necessary. But for the one-factor BK model, the trinomial tree is the natural and preferred method for Bermudan swaptions.
