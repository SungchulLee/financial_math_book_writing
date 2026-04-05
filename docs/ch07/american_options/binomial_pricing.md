# Binomial Model for American Options

### Introduction

The **binomial tree** is the most natural numerical framework for American option pricing. Its node-by-node structure allows the early-exercise decision to be evaluated at every point in the tree via **backward induction with a maximum condition**.

This section develops the full binomial pricing algorithm for American options, demonstrates convergence, and shows how the method naturally identifies the early-exercise boundary.

!!! info "Prerequisites"
    - [Multi-Period Binomial Model](../../ch01/binomial_model/multi_period_binomial_model.md) (backward induction)
    - [Risk-Neutral Measure](../../ch01/binomial_model/risk_neutral_measure.md) (binomial risk-neutral pricing)
    - [Early Exercise](early_exercise.md) (when exercise is optimal)

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:
    
    1. Implement backward induction with early-exercise checks
    2. Compare American and European option values on the same tree
    3. Identify the early-exercise boundary from the tree
    4. Analyze convergence as the number of steps increases

---

### European Pricing: Recap

In the CRR binomial model with $N$ time steps:

$$
\Delta t = \frac{T}{N}, \quad u = e^{\sigma\sqrt{\Delta t}}, \quad d = \frac{1}{u}, \quad q = \frac{e^{r\Delta t} - d}{u - d}
$$

For a **European** option, backward induction gives:

$$
V_{n,j} = e^{-r\Delta t}\left[q \, V_{n+1,j+1} + (1 - q) \, V_{n+1,j}\right]
$$

starting from terminal payoffs $V_{N,j} = \Phi(S_{N,j})$.

---

### American Pricing: The Maximum Condition

For an **American** option, at each node $(n, j)$ we compare the **continuation value** with the **immediate exercise value**:

$$
\boxed{
V_{n,j} = \max\left(\Phi(S_{n,j}), \; e^{-r\Delta t}\left[q \, V_{n+1,j+1} + (1 - q) \, V_{n+1,j}\right]\right)
}
$$

where:

- $\Phi(S_{n,j})$ is the intrinsic value (e.g., $K - S_{n,j}$ for a put)
- The discounted expectation is the continuation value
- The $\max$ operator enforces the early-exercise constraint

#### Algorithm

!!! note "Backward Induction with Early Exercise"
    **Step 1.** Build the stock price tree: $S_{n,j} = S_0 \cdot u^j \cdot d^{n-j}$
    
    **Step 2.** Set terminal values: $V_{N,j} = \Phi(S_{N,j})$ for $j = 0, 1, \ldots, N$
    
    **Step 3.** For $n = N-1$ down to $0$, for $j = 0, 1, \ldots, n$:
    
    $$
    \begin{aligned}
    \text{Continuation} &= e^{-r\Delta t}\left[q \, V_{n+1,j+1} + (1-q) \, V_{n+1,j}\right] \\
    \text{Exercise} &= \Phi(S_{n,j}) \\
    V_{n,j} &= \max(\text{Exercise}, \text{Continuation})
    \end{aligned}
    $$
    
    **Step 4.** The American option price is $V_{0,0}$.

---

### Implementation: American Put

#### Efficient Array-Based Algorithm

Rather than storing the full tree, we can work with a single array that is updated backward in time.

**`american_put_binomial.py`**

```python
import numpy as np

def american_put_binomial(S, K, T, r, sigma, N):
    """
    Price an American put option using the CRR binomial tree.

    Parameters
    ----------
    S : float — Current stock price
    K : float — Strike price
    T : float — Time to maturity (years)
    r : float — Risk-free rate (continuous)
    sigma : float — Volatility
    N : int — Number of time steps

    Returns
    -------
    float — American put option price
    """
    dt = T / N
    u = np.exp(sigma * np.sqrt(dt))
    d = 1 / u
    q = (np.exp(r * dt) - d) / (u - d)

    # Terminal stock prices
    ST = np.array([S * (u ** j) * (d ** (N - j)) for j in range(N + 1)])

    # Terminal payoff
    P = np.maximum(K - ST, 0)

    # Backward induction with early-exercise check
    for i in range(N - 1, -1, -1):
        # Continuation value (discounted expectation)
        P = np.exp(-r * dt) * (q * P[1:i + 2] + (1 - q) * P[0:i + 1])

        # Stock prices at time step i
        ST = np.array([S * (u ** j) * (d ** (i - j)) for j in range(i + 1)])

        # Early exercise check
        P = np.maximum(K - ST, P)

    return P[0]


# === Example ===
if __name__ == "__main__":
    S, K, T, r, sigma = 100, 100, 1.0, 0.05, 0.20

    for N in [50, 100, 200, 500, 1000]:
        price = american_put_binomial(S, K, T, r, sigma, N)
        print(f"  N = {N:5d}:  American Put = {price:.4f}")
```

!!! example "Sample Output"
    ```
      N =    50:  American Put = 6.0860
      N =   100:  American Put = 6.0781
      N =   200:  American Put = 6.0826
      N =   500:  American Put = 6.0808
      N =  1000:  American Put = 6.0814
    ```
    The price converges to approximately $6.08$ as $N$ increases.

---

### Comparing American and European Puts

The difference between American and European put prices is the **early exercise premium**:

```python
from scipy.stats import norm

def european_put_bs(S, K, T, r, sigma):
    """Black-Scholes European put price."""
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)

S, K, T, r, sigma = 100, 100, 1.0, 0.05, 0.20

P_am = american_put_binomial(S, K, T, r, sigma, 500)
P_eu = european_put_bs(S, K, T, r, sigma)

print(f"European Put:          {P_eu:.4f}")
print(f"American Put:          {P_am:.4f}")
print(f"Early Exercise Premium: {P_am - P_eu:.4f}")
```

---

### Identifying the Early-Exercise Boundary

At each node, the tree reveals **whether exercise is optimal**. By collecting nodes where $\Phi(S_{n,j}) > \text{Continuation Value}$, we can trace the exercise boundary.

```python
import matplotlib.pyplot as plt

def early_exercise_boundary(S, K, T, r, sigma, N):
    """
    Compute the early-exercise boundary from a binomial tree.
    Returns arrays of (time, stock_price) where exercise is optimal.
    """
    dt = T / N
    u = np.exp(sigma * np.sqrt(dt))
    d = 1 / u
    q = (np.exp(r * dt) - d) / (u - d)

    # Build full tree
    tree_S = np.zeros((N + 1, N + 1))
    tree_V = np.zeros((N + 1, N + 1))

    for n in range(N + 1):
        for j in range(n + 1):
            tree_S[j, n] = S * (u ** j) * (d ** (n - j))

    # Terminal payoff
    tree_V[:, N] = np.maximum(K - tree_S[:, N], 0)

    boundary = []

    # Backward induction
    for n in range(N - 1, -1, -1):
        for j in range(n + 1):
            continuation = np.exp(-r * dt) * (
                q * tree_V[j + 1, n + 1] + (1 - q) * tree_V[j, n + 1]
            )
            exercise = K - tree_S[j, n]
            tree_V[j, n] = max(continuation, exercise)

            if exercise > continuation and exercise > 0:
                boundary.append((n * dt, tree_S[j, n]))

    return np.array(boundary)


# === Plot the boundary ===
S, K, T, r, sigma, N = 100, 100, 1.0, 0.05, 0.20, 200

bd = early_exercise_boundary(S, K, T, r, sigma, N)

plt.figure(figsize=(10, 6))
plt.scatter(bd[:, 0], bd[:, 1], s=3, alpha=0.5, color="steelblue")
plt.axhline(K, color="gray", linestyle="--", linewidth=0.8, label=f"Strike K = {K}")
plt.xlabel("Time (years)")
plt.ylabel("Stock Price at Exercise")
plt.title("Early-Exercise Boundary for American Put (Binomial Tree)")
plt.gca().invert_xaxis()
plt.legend()
plt.tight_layout()
plt.show()
```

The boundary shows:

- Early exercise occurs at **low stock prices** (deep ITM for puts)
- The boundary $S^*(t)$ **rises toward** $K$ as maturity approaches
- At $t = T$, the boundary equals $K$ (exercise whenever ITM at expiry)

---

### Convergence Analysis

The CRR binomial tree converges to the continuous-time American option price, but with **oscillatory behavior** due to the discrete grid:

$$
V_{\text{binomial}}(N) = V_{\text{American}} + O\left(\frac{1}{\sqrt{N}}\right) + \text{oscillatory terms}
$$

#### Richardson Extrapolation

To accelerate convergence, use prices from two step sizes:

$$
V_{\text{extrapolated}} = 2 \, V(2N) - V(N)
$$

This eliminates the leading error term and often yields fourth-decimal accuracy with moderate $N$.

#### Convergence Behavior

| Steps $N$ | American Put Price | Change |
|---|---|---|
| 50 | 6.0860 | — |
| 100 | 6.0781 | $-0.0079$ |
| 200 | 6.0826 | $+0.0045$ |
| 500 | 6.0808 | $-0.0018$ |
| 1000 | 6.0814 | $+0.0006$ |

---

### Summary

$$
\boxed{
V_{n,j} = \max\left(\Phi(S_{n,j}), \; e^{-r\Delta t}\left[q \, V_{n+1,j+1} + (1-q) \, V_{n+1,j}\right]\right)
}
$$

| Aspect | Description |
|---|---|
| Method | Backward induction with $\max$ operator |
| Complexity | $O(N^2)$ time, $O(N)$ space (array method) |
| Convergence | $O(1/\sqrt{N})$ with oscillation |
| Boundary | Naturally identified from exercise decisions |
| Strength | Simple, robust, handles dividends and exotics |

**The binomial tree remains the workhorse method for American option pricing: intuitive, flexible, and easily extended to handle dividends, time-varying parameters, and path-dependent features.**

---

## Exercises

**Exercise 1.** Price an American put with $S_0 = 100$, $K = 100$, $r = 5\%$, $\sigma = 30\%$, $T = 1$ using a 3-step CRR binomial tree. At each node, show the stock price, the European put value, and the American put value. Identify the nodes where early exercise is optimal.

??? success "Solution to Exercise 1"
    With $S_0 = 100$, $K = 100$, $r = 0.05$, $\sigma = 0.30$, $T = 1$, and $N = 3$:

    $$
    \Delta t = \frac{1}{3}, \quad u = e^{0.30\sqrt{1/3}} = e^{0.1732} \approx 1.1892, \quad d = \frac{1}{u} \approx 0.8410
    $$

    $$
    q = \frac{e^{0.05/3} - 0.8410}{1.1892 - 0.8410} = \frac{1.01681 - 0.8410}{0.3482} \approx \frac{0.1758}{0.3482} \approx 0.5050
    $$

    **Stock price tree** ($S_{n,j} = S_0 u^j d^{n-j}$):

    | Node | $n=0$ | $n=1$ | $n=2$ | $n=3$ |
    |---|---|---|---|---|
    | $j=3$ | | | | $168.20$ |
    | $j=2$ | | | $141.40$ | $118.91$ |
    | $j=1$ | | $118.92$ | $100.00$ | $84.10$ |
    | $j=0$ | $100.00$ | $84.10$ | $70.72$ | $59.47$ |

    **Terminal payoffs** ($n=3$): $(K - S)^+ = (100 - 168.20)^+ = 0$, $(100 - 118.91)^+ = 0$, $(100 - 84.10)^+ = 15.90$, $(100 - 59.47)^+ = 40.53$.

    **European put values** (backward induction without early exercise):

    At $n = 2$:

    $$
    V_{2,2}^{\text{Eu}} = e^{-0.05/3}[0.505 \cdot 0 + 0.495 \cdot 0] = 0
    $$

    $$
    V_{2,1}^{\text{Eu}} = e^{-0.05/3}[0.505 \cdot 0 + 0.495 \cdot 15.90] \approx 0.9834 \cdot 7.87 \approx 7.74
    $$

    $$
    V_{2,0}^{\text{Eu}} = e^{-0.05/3}[0.505 \cdot 15.90 + 0.495 \cdot 40.53] \approx 0.9834 \cdot 28.10 \approx 27.63
    $$

    At $n = 1$:

    $$
    V_{1,1}^{\text{Eu}} = e^{-0.05/3}[0.505 \cdot 0 + 0.495 \cdot 7.74] \approx 0.9834 \cdot 3.83 \approx 3.77
    $$

    $$
    V_{1,0}^{\text{Eu}} = e^{-0.05/3}[0.505 \cdot 7.74 + 0.495 \cdot 27.63] \approx 0.9834 \cdot 17.59 \approx 17.30
    $$

    At $n = 0$: $V_{0,0}^{\text{Eu}} = e^{-0.05/3}[0.505 \cdot 3.77 + 0.495 \cdot 17.30] \approx 0.9834 \cdot 10.47 \approx 10.30$.

    **American put values** (with early-exercise check $V_{n,j} = \max(\text{payoff}, \text{continuation})$):

    At $n = 2$: $V_{2,2}^{\text{Am}} = \max(0, 0) = 0$; $V_{2,1}^{\text{Am}} = \max(0, 7.74) = 7.74$; $V_{2,0}^{\text{Am}} = \max(29.28, 27.63) = 29.28$ (early exercise optimal since $K - 70.72 = 29.28 > 27.63$).

    At $n = 1$: $V_{1,1}^{\text{Am}} = \max(0, e^{-0.05/3}[0.505 \cdot 0 + 0.495 \cdot 7.74]) = \max(0, 3.77) = 3.77$; $V_{1,0}^{\text{Am}} = \max(15.90, e^{-0.05/3}[0.505 \cdot 7.74 + 0.495 \cdot 29.28]) = \max(15.90, 0.9834 \cdot 18.40) = \max(15.90, 18.10) = 18.10$.

    At $n = 0$: $V_{0,0}^{\text{Am}} = \max(0, e^{-0.05/3}[0.505 \cdot 3.77 + 0.495 \cdot 18.10]) = \max(0, 0.9834 \cdot 10.87) = 10.69$.

    **Early exercise is optimal** at node $(n=2, j=0)$ where $S = 70.72$ and the intrinsic value $29.28$ exceeds the continuation value $27.63$.

---


**Exercise 2.** In the binomial tree for an American put, the value at each node is $V = \max\left(\text{payoff}, \, e^{-r\Delta t}[pV_u + (1-p)V_d]\right)$. Explain the role of the $\max$ operation and why it is absent in European option pricing. What would happen if you omitted it?

??? success "Solution to Exercise 2"
    In European option pricing, the value at each node is simply the discounted risk-neutral expectation of future values:

    $$
    V_{n,j}^{\text{Eu}} = e^{-r\Delta t}\left[q V_{n+1,j+1} + (1-q) V_{n+1,j}\right]
    $$

    For American options, the $\max$ operator is added:

    $$
    V_{n,j}^{\text{Am}} = \max\left(\Phi(S_{n,j}), \; e^{-r\Delta t}\left[q V_{n+1,j+1} + (1-q) V_{n+1,j}\right]\right)
    $$

    **Role of the $\max$:** At each node, the holder decides between exercising immediately (receiving the intrinsic value $\Phi(S_{n,j})$) and continuing to hold (receiving the continuation value). The $\max$ ensures the holder always makes the optimal choice. This encodes the optimal stopping problem at the discrete level.

    **Why it is absent for European options:** European options can only be exercised at maturity, so there is no exercise decision at intermediate nodes. The holder must continue regardless.

    **What happens if $\max$ is omitted:** Omitting the $\max$ from the American pricing formula would compute the European price instead. The resulting value would be lower than the true American price because it ignores the early-exercise right. Specifically, at nodes where $\Phi(S_{n,j})$ exceeds the continuation value, the algorithm would assign the smaller continuation value, missing the additional early-exercise premium.

---


**Exercise 3.** The convergence of the binomial tree to the continuous-time price is $O(1/\sqrt{N})$ but oscillatory. Explain the source of these oscillations for American puts and describe the Richardson extrapolation technique that can improve convergence.

??? success "Solution to Exercise 3"
    **Source of oscillations:** The CRR tree imposes a recombining lattice with nodes at $S_0 u^j d^{n-j}$. For a given $N$, the strike $K$ generally does not fall exactly on a node at any time step. Whether the nearest node is slightly above or below $K$ affects the computed payoff and exercise decisions, causing the price to oscillate between odd and even $N$.

    More precisely, the binomial tree discretizes space non-uniformly. When $N$ is odd, the central node at maturity is $S_0 u d^{(N-1)/2} \cdot u^{(N-1)/2}$, which differs from the central node when $N$ is even. The option's sensitivity is highest near the strike, so small shifts in the grid near $K$ produce disproportionate price changes. This is sometimes called the **even-odd effect**.

    The convergence rate is $O(1/\sqrt{N})$, slower than the $O(1/N)$ rate of finite difference methods, due to the non-smooth payoff at $S = K$.

    **Richardson extrapolation:** Given prices $V(N)$ and $V(2N)$, the leading error term can be eliminated by:

    $$
    V_{\text{extrap}} = 2V(2N) - V(N)
    $$

    This works because if $V(N) = V_{\text{true}} + c/\sqrt{N} + O(1/N)$, then:

    $$
    2V(2N) - V(N) = 2\left(V_{\text{true}} + \frac{c}{\sqrt{2N}}\right) - \left(V_{\text{true}} + \frac{c}{\sqrt{N}}\right) + O(1/N) = V_{\text{true}} + c\left(\frac{2}{\sqrt{2}} - 1\right)\frac{1}{\sqrt{N}} + O(1/N)
    $$

    In practice, Richardson extrapolation using the same-parity values (e.g., $V(N)$ and $V(2N)$) significantly reduces oscillation and typically yields fourth-decimal accuracy with $N \sim 100$--$200$.

---


**Exercise 4.** Modify the binomial tree to price an American call on a stock paying a discrete dividend $D$ at time $t_d$. Explain the adjustment to the stock price at the ex-dividend node and how early exercise just before the dividend date is handled.

??? success "Solution to Exercise 4"
    **Discrete dividend adjustment:** Suppose the stock pays a dividend $D$ at time $t_d$, which falls at step $n_d$ in the tree. At the ex-dividend date, the stock price drops by $D$:

    $$
    S_{n_d,j}^{\text{ex}} = S_{n_d,j}^{\text{cum}} - D
    $$

    where $S^{\text{cum}}$ is the cum-dividend price and $S^{\text{ex}}$ is the ex-dividend price.

    **Tree construction:** Build the tree normally up to step $n_d$. At step $n_d$, subtract $D$ from all stock prices. Then continue building the tree from the adjusted prices. Note that after the dividend, the tree is no longer perfectly recombining (since $S_{n_d,j} - D$ does not factor neatly with $u$ and $d$), which requires either interpolation or a non-recombining tree.

    **Early exercise handling:** At the node just before the ex-dividend date ($n_d - 1$), the American call holder compares:

    - **Exercise now:** Receive $S_{n_d-1,j} - K$ and capture the upcoming dividend $D$
    - **Continue:** Hold the option through the dividend, after which the stock drops by $D$

    Exercise is potentially optimal just before the ex-dividend date if:

    $$
    D > K\left(1 - e^{-r\Delta t}\right)
    $$

    where $\Delta t$ is the remaining time to maturity after $t_d$. This is because by exercising, the holder pays $K$ early (losing interest $K(1 - e^{-r\Delta t})$) but gains the dividend $D$. When $D$ exceeds this interest cost, early exercise may be optimal.

    At all other nodes, the standard backward induction with the $\max$ operator applies unchanged.

---


**Exercise 5.** From your 3-step binomial tree in Exercise 1, extract the early exercise boundary by identifying the critical stock price $S^*$ at each time step below which exercise is optimal. Plot these values and comment on whether the boundary is increasing or decreasing in time to maturity.

??? success "Solution to Exercise 5"
    Using the results from Exercise 1 (3-step tree with $S_0 = 100$, $K = 100$, $r = 0.05$, $\sigma = 0.30$, $T = 1$):

    At each time step $n$, the critical stock price $S^*(n\Delta t)$ is the highest stock price at which early exercise is optimal (i.e., where intrinsic value exceeds continuation value).

    From the American put tree:

    - **$n = 2$ ($t = 2/3$):** Exercise is optimal at $S = 70.72$ (intrinsic $= 29.28 >$ continuation $= 27.63$) but not at $S = 100$ (intrinsic $= 0$) or $S = 141.40$ (intrinsic $= 0$). So $S^*(2/3) \approx 70.72$.
    - **$n = 1$ ($t = 1/3$):** Exercise is not optimal at $S = 84.10$ (intrinsic $= 15.90 <$ continuation $= 18.10$) or $S = 118.92$ (intrinsic $= 0$). No early exercise at this step, so $S^*(1/3) < 84.10$ (the boundary is below the lowest node reached).
    - **$n = 0$ ($t = 0$):** Exercise is not optimal at $S = 100$ (intrinsic $= 0$).

    The boundary $S^*(t)$ is **increasing** as time approaches maturity (i.e., as time to maturity decreases, $S^*(t)$ rises toward $K$). At maturity, $S^*(T) = K = 100$, and for earlier times the boundary is lower. This makes economic sense: with more time remaining, the option has greater time value, so the stock must be deeper in the money (lower $S$) to justify early exercise. As maturity approaches, even moderately in-the-money puts should be exercised because the remaining time value is small.

---


**Exercise 6.** Compare the American put price from an $N$-step binomial tree with the European put price (from the same tree) for $N = 10, 50, 100, 500$. Compute the early exercise premium $\epsilon_N = V_{\text{Am}}^{(N)} - V_{\text{Eu}}^{(N)}$ and discuss how it behaves as $N$ increases.

??? success "Solution to Exercise 6"
    Using the CRR binomial tree for both American and European puts with $S_0 = 100$, $K = 100$, $r = 0.05$, $\sigma = 0.20$, $T = 1$:

    The European put price on the binomial tree is computed by the same backward induction without the $\max$ operator. As $N$ increases, both prices converge to their continuous-time limits.

    | $N$ | $V_{\text{Am}}^{(N)}$ | $V_{\text{Eu}}^{(N)}$ | $\epsilon_N$ |
    |---|---|---|---|
    | 10 | $\approx 6.16$ | $\approx 5.60$ | $\approx 0.56$ |
    | 50 | $\approx 6.09$ | $\approx 5.57$ | $\approx 0.52$ |
    | 100 | $\approx 6.08$ | $\approx 5.57$ | $\approx 0.51$ |
    | 500 | $\approx 6.08$ | $\approx 5.57$ | $\approx 0.51$ |

    **Behavior of $\epsilon_N$ as $N$ increases:** The early exercise premium converges to a positive limit $\epsilon_\infty = V_{\text{Am}} - V_{\text{Eu}} \approx 0.51$. Both the American and European prices oscillate as $N$ increases (due to the discrete grid), but their difference $\epsilon_N$ stabilizes faster because the oscillations are correlated and partially cancel.

    The positive limit reflects the genuine value of the early-exercise right. For puts, this premium is always positive because deep-in-the-money puts benefit from immediate exercise (earning interest on the strike cash). The premium depends on the interest rate $r$, volatility $\sigma$, moneyness, and time to maturity.
