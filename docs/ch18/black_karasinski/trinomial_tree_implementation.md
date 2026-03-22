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

### Standard branching (successor nodes at $x_{j+1}$, $x_j$, $x_{j-1}$)

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

### Up branching (successor nodes at $x_{j+2}$, $x_{j+1}$, $x_j$)

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
