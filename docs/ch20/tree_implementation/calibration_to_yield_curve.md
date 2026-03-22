# Calibration to Yield Curve on Tree

The trinomial tree from the previous section discretizes the zero-mean process $x_t$ on a recombining grid. To price derivatives consistently with the market, the tree must reproduce the initial zero-coupon bond curve $P^M(0, T)$ for all maturities. This is achieved by choosing the shift $\alpha_i$ at each time step $t_i$ so that the tree-implied bond prices match the market. The key tool is the Arrow-Debreu price, which propagates through the tree and enables efficient calibration.

## Arrow-Debreu Prices

An Arrow-Debreu (state) price $Q_{ij}$ is the present value at time $0$ of receiving $\$1$ at node $(i, j)$ and nothing elsewhere. These prices encode all discount factor information in the tree.

**Definition.** The Arrow-Debreu price at node $(i, j)$ is

$$
Q_{ij} = \mathbb{E}^{\mathbb{Q}}\!\left[\frac{\mathbf{1}_{\{x_{t_i} = j\Delta x\}}}{M(t_i)}\right]
$$

At the root node, $Q_{0,0} = 1$.

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

The tree calibration of $\alpha_i$ is the discrete-time analogue of the continuous-time fitting formula

$$
\theta(t) = \frac{\partial f^M(0,t)}{\partial t} + \lambda\,f^M(0,t) + \frac{\sigma^2}{2\lambda}\left(1 - e^{-2\lambda t}\right)
$$

As $\Delta t \to 0$, the discrete shift $\alpha_i$ converges to $\tilde{r}(t_i) = f^M(0, t_i) + \frac{\sigma^2}{2\lambda^2}(1 - e^{-\lambda t_i})^2$, the deterministic component of the short rate decomposition.

## Summary

Calibrating the Hull-White trinomial tree to the initial yield curve determines the shift $\alpha_i$ at each time step using Arrow-Debreu prices. The Arrow-Debreu prices propagate forward through the tree via $Q_{i+1,m} = \sum_j Q_{ij}\,p(j \to m)\,e^{-r_{ij}\Delta t}$, and the shift is found from $\alpha_i = (\ln\sum_j Q_{ij}e^{-j\Delta x\Delta t} - \ln P^M(0, t_{i+1}))/\Delta t$. This procedure is exact by construction, matching the market bond curve to machine precision. The calibrated tree is then ready for derivative pricing via backward induction, which is covered in the next section.
