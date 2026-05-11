# LMM Drift in Terminal Measure

The LIBOR Market Model (LMM) is the standard framework for pricing interest rate derivatives across multiple tenors simultaneously. A crucial technical aspect is the drift correction required when changing the numeraire to a specific maturity, enabling efficient calibration and pricing under different term structures.

## Key Concepts

**LIBOR Dynamics in Spot Measure**
Define forward LIBOR $L_k(t)$ for tenor $[T_k, T_{k+1}]$ with accrual $\delta_k$:

$$dL_k(t) = \mu_k^{\text{spot}}(t) dt + \sigma_k(t) dB_k(t)$$

The spot measure uses the rolling bank account as numeraire:

$$N_t^{\text{spot}} = \prod_{j: T_j \leq t} (1 + \delta_j L_j(T_j))$$

**Terminal Measure Change**
The terminal measure uses the zero-coupon bond maturing at time $T_N$ as numeraire:

$$N_t^{N} = P(t, T_N)$$

Under terminal measure:

$$dL_k(t) = \mu_k^N(t) dt + \sigma_k(t) dB_k^N(t)$$

The Brownian motion has changed to $B_k^N$ reflecting the new measure.

**Drift Correction Formula**
The drift correction relates spot and terminal measure drifts:

$$\mu_k^N(t) = \mu_k^{\text{spot}}(t) + \sigma_k(t) \sum_{j=k+1}^{N} \frac{\delta_j \sigma_j(t) \rho_{k,j}}{1 + \delta_j L_j(t)}$$

Key features:

- Correction term is positive (martingale property enforced)
- Depends on instantaneous correlation $\rho_{k,j}$ between rate curves
- Involves future rates for indices $j > k$ in terminal measure

**Intuition**
The drift correction arises because:

1. Zero-coupon bond price depends on all future rates
2. When changing numeraire to $P(t, T_N)$, relative pricing changes
3. Girsanov theorem ensures the SDE coefficient structure remains proportional to $\sigma_k$
4. Only drift changes, volatility structure preserved

**Practical Implementation**
LMM calibration proceeds in terminal measure:

1. Specify volatility structure $\sigma_k(t)$ (typically piecewise constant or deterministic)
2. Specify correlation matrix $\rho_{i,j}$ for all rate pairs
3. Drift is automatically computed from formula
4. Simulate forward rates under terminal measure
5. Compute prices by averaging discounted payoffs

**Efficient Calibration**
Terminal measure enables efficient calibration:

- Caplets/floorlets prices depend on individual rate volatilities $\sigma_k$
- Swaptions prices depend on rate correlation structure
- Two-stage calibration: fit volatilities to caps, correlations to swaptions
- Avoids explicit specification of spot measure drifts

**Connection to Swap Measure**
Alternative: swap measure uses annuity as numeraire

$$N_t^{\text{swap}} = A_t = \sum_{j=k}^{N} \delta_j P(t, T_j)$$

Swap measure drift is different from terminal measure, optimized for swaption pricing.

!!! note "Practical Insights"
    Terminal measure provides:

    - Computational efficiency through direct calibration
    - Intuitive interpretation: numeraire is final cash received
    - Stability in long-dated simulations
    - Effective handling of multiple correlated rates simultaneously

## QuantPie Derivation: LIBOR Market Model Spot Measure

### Definition of LIBOR and Spot Measure

**LIBOR Definition**

$$\begin{array}{ccccccc}
\displaystyle
L_n\left(t\right)P\left(t,T_{n}\right)
=
\frac{1}{\delta}
\left(
P\left(t,T_{n-1}\right)-P\left(t,T_{n}\right)
\right)
&\Rightarrow&\displaystyle
L_n\left(t\right)
=
\frac{1}{\delta}
\left(
\frac{P\left(t,T_{n-1}\right)-P\left(t,T_{n}\right)}{P\left(t,T_{n}\right)}
\right)\\
\end{array}$$

is tradable, where $L_n\left(t\right)P\left(t,T_{n}\right)$ is the value of tradable assets.

### Bank Account (Spot Measure Numeraire)

$$\begin{array}{llllllll}
\displaystyle
M(t)
&:=&
\displaystyle
\frac{P(t,T_{\bar{m}(t)})}{\prod_{k=1}^{\bar{m}(t)}P(T_{k-1},T_k)}\\
\end{array}$$

where

$$
\bar{m}(t)=\text{min}\left(i:t\le T_i\right)
$$

### Bond Price and Accrual

When current time $t$ is $T_0$ or $T_k$:

$$\begin{array}
\displaystyle
B(T_n)=\prod_{i=0}^{n-1}\left(1+\delta L(T_i,T_i)\right)\\
\displaystyle
P(T_0,T_n)=\prod_{i=0}^{n-1}\frac{1}{1+\delta L(T_0,T_i)}\\
\displaystyle
P(T_k,T_n)=\prod_{i=k}^{n-1}\frac{1}{1+\delta L(T_k,T_i)}\\
\end{array}$$

When current time $t$ is $T_{q(t)-1}-\delta<t<T_{q(t)}$:

$$\begin{array}{lll}
\displaystyle
B(t)=P\left(t,T_{q(t)}\right)\prod_{i=0}^{q(t)-1}\left(1+\delta L(T_i,T_i)\right)\\
\displaystyle
P(t,T_n)=P\left(t,T_{q(t)}\right)\prod_{i=q(t)}^{n-1}\frac{1}{1+\delta L\left(T_{q(t)},T_i\right)}\\
\end{array}$$

### Radon–Nikodym Derivative for Spot Measure

$$\begin{array}{llllllll}
\displaystyle
\lambda_M^{\bar{n}(t)}(t)
&=&\displaystyle
\left.\frac{d\mathbb{Q}^{M}}{d\mathbb{Q}^{\bar{n}(t)}}\Big{|}{\cal F}(t)\right)\\
&=&\displaystyle
\frac{M(t)/M(t_0)}{P(t,T_{\bar{n}(t)})/P(t_0,T_{\bar{n}(t)})}\\
&=&\displaystyle
\frac{P(t,T_{\bar{m}(t)})}{P(t,T_{\bar{n}(t)})}
\frac{P(t_0,T_{\bar{n}(t)})}{M(t_0)}
\prod_{k=1}^{\bar{m}(t)}\frac{1}{P(T_{k-1},T_k)}\\
&:=&\displaystyle
\frac{P(t,T_{\bar{m}(t)})}{P(t,T_{\bar{n}(t)})}
\bar{P}\\
\end{array}$$

### Girsanov Transformation to Spot Measure

$$\begin{array}{lllll}
\displaystyle
dW_{\bar{n}(t)}^{M}(t)
&=&\displaystyle
-\frac{\tau_{\bar{n}(t)}\bar{\sigma}_{\bar{n}(t)}(t)}{\tau_{\bar{n}(t)}l_{\bar{n}(t)}(t)+1}dt
+dW_{\bar{n}(t)}^{\bar{n}(t)}(t)\\
\end{array}$$

### LIBOR Drift in Spot Measure

$$\begin{array}{lllll}
\displaystyle
dl_i(t)
&=&\displaystyle
\bar{\sigma}_i(t)\sum_{k=\bar{m}(t)+1}^{i}\frac{\tau_{k}\bar{\sigma}_{k}(t)}{\tau_{k}l_{k}(t)+1}dt
+\bar{\sigma}_i(t)dW_i^{M}(t)\\
\end{array}$$

### Special Case: Spot Measure Equals Forward Measure

**Spot Measure Radon–Nikodym Derivative**

$$\begin{array}{llllll}
\displaystyle
Z_t
:=
\mathbb{E}^{q(t)}\left[\frac{d\mathbb{P}_{S}}{d\mathbb{P}_{q(t)}}\Big{|}{\cal F}_t\right]
=
\frac{B(t)/B(0)}{P\left(t,T_{q(t)}\right)/P\left(0,T_{q(t)}\right)}\\
\end{array}$$

Since $\prod_{i=0}^{q(t)-1}\left(1+\delta L(T_i,T_i,T_{i+1})\right)$ is known at time $t$, let's call this constant $C_1$.

$$\begin{array}{llll}
\displaystyle
\frac{B(t)}{B(0)}
=
P(t,T_{q(t)})\prod_{i=0}^{q(t)-1}\left(1+\delta L(T_i,T_i,T_{i+1})\right)
=
C_1P(t,T_{q(t)})
\end{array}$$

Since $\prod_{i=0}^{q(t)-1}\left(1+\delta L(0,T_i,T_{i+1})\right)$ is known at time $t$,
let's call this constant $C_2$.

$$\begin{array}{llll}
\displaystyle
\frac{P(t,T_{q(t)})}{P(0,T_{q(t)})}
=
P(t,T_{q(t)})\prod_{i=0}^{q(t)-1}\left(1+\delta L(0,T_i,T_{i+1})\right)
=
C_2P(t,T_{q(t)})
\\
\end{array}$$

Since $Z_t$ is a Radon-Nykodym derivative, in particular we have $\mathbb{E}^{q(t)}[Z_t]=1$. Therefore,

$$\begin{array}{llllll}
\displaystyle
Z_t
=
\mathbb{E}^{q(t)}\left[\frac{d\mathbb{P}_{S}}{d\mathbb{P}_{q(t)}}\Big{|}{\cal F}_t\right]
=
\frac{B(t)/B(0)}{P\left(t,T_{q(t)}\right)/P\left(0,T_{q(t)}\right)}=\frac{C_1}{C_2}=1\\
\end{array}$$

This means

$$\begin{array}{lll}
\displaystyle
dW_t^{S}
=
dW_t^{q(t)}
\end{array}$$

### Equivalence of Spot and Forward Measures

$$\begin{array}{lll}
\displaystyle
\mathbb{P}_{S}
=
\mathbb{P}_{q(t)}
\end{array}$$

---

## Exercises

**Exercise 1.** In an LMM with $n$ forward rates and terminal measure $\mathbb{Q}^{T_n}$, the drift of $L_i(t)$ involves a sum over rates $L_{i+1}, \ldots, L_{n-1}$. For $n = 5$ and $i = 1$, write out the drift term explicitly (using constant volatilities $\sigma_k$ and correlation $\rho_{1k}$). How many terms appear in the sum, and which forward rate contributes the largest drift correction?

??? success "Solution to Exercise 1"
    For $n = 5$, $i = 1$, the drift of $L_1(t)$ under $\mathbb{Q}^{T_5}$ is:

    $$
    \mu_1^{(5)}(t) = -\sum_{j=2}^{4}\frac{\delta_j\,\rho_{1j}\,\sigma_1\,\sigma_j\,L_j(t)}{1 + \delta_j\,L_j(t)}
    $$

    Writing the terms explicitly (with constant volatilities $\sigma_k$ and correlations $\rho_{1k}$):

    **Term $j = 2$:**

    $$
    -\frac{\delta_2\,\rho_{12}\,\sigma_1\,\sigma_2\,L_2(t)}{1 + \delta_2\,L_2(t)}
    $$

    **Term $j = 3$:**

    $$
    -\frac{\delta_3\,\rho_{13}\,\sigma_1\,\sigma_3\,L_3(t)}{1 + \delta_3\,L_3(t)}
    $$

    **Term $j = 4$:**

    $$
    -\frac{\delta_4\,\rho_{14}\,\sigma_1\,\sigma_4\,L_4(t)}{1 + \delta_4\,L_4(t)}
    $$

    There are **3 terms** in the sum (for $j = 2, 3, 4$).

    **Which forward rate contributes the largest drift correction?**

    Each term's magnitude is proportional to $\rho_{1j}\,\sigma_j\,\delta_j L_j/(1 + \delta_j L_j)$. The factor $\delta_j L_j/(1 + \delta_j L_j)$ is an increasing function of $L_j$ (bounded between 0 and 1).

    - If all rates, volatilities, and tenors are equal, each term has the same magnitude
    - If correlations decrease with distance ($\rho_{12} > \rho_{13} > \rho_{14}$), the $j = 2$ term (nearest neighbor) contributes the most
    - If volatilities increase with maturity, the $j = 4$ term may dominate despite lower correlation
    - In practice, the **nearest-neighbor rate** ($L_2$) typically contributes the largest correction because the correlation $\rho_{12}$ is highest

---

**Exercise 2.** Explain why the forward rate $L_{n-1}(t)$ (the rate closest to the terminal date) is a martingale under the terminal measure $\mathbb{Q}^{T_n}$, while all other forward rates $L_i(t)$ for $i < n-1$ acquire non-zero drifts. What does this imply about the difficulty of simulating rates far from the terminal date?

??? success "Solution to Exercise 2"
    Under the terminal measure $\mathbb{Q}^{T_n}$, the drift of $L_i(t)$ is:

    $$
    \mu_i^{(n)}(t) = -\sum_{j=i+1}^{n-1}\frac{\delta_j\,\rho_{ij}\,\sigma_i(t)\,\sigma_j(t)\,L_j(t)}{1 + \delta_j\,L_j(t)}
    $$

    **For $i = n-1$:** The sum runs from $j = n$ to $n - 1$, which is an empty sum. Therefore:

    $$
    \mu_{n-1}^{(n)}(t) = 0
    $$

    $L_{n-1}(t)$ is a **martingale** under $\mathbb{Q}^{T_n}$. This is because $L_{n-1}$ is the forward rate for the period $[T_{n-1}, T_n]$, and $P(t, T_n)$ is its natural numéraire. Under $\mathbb{Q}^{T_n}$, $L_{n-1}(t) = \frac{1}{\delta_{n-1}}(P(t, T_{n-1})/P(t, T_n) - 1)$ is a ratio of tradable assets divided by the numéraire, hence a martingale.

    **For $i < n-1$:** The sum contains $n - 1 - i$ terms, and each term is nonzero (assuming positive correlations, rates, and volatilities). The drift is strictly negative.

    **Implication for simulation:**

    Rates far from the terminal date have large drift corrections:

    - $L_0$ has $n - 2$ terms in its drift sum
    - $L_1$ has $n - 3$ terms
    - ...
    - $L_{n-2}$ has 1 term
    - $L_{n-1}$ has 0 terms (martingale)

    This means:

    1. **Short-maturity rates are hardest to simulate accurately** because they accumulate the largest drift corrections, which are state-dependent and can become large
    2. **Discretization error** is most severe for these rates because the Euler approximation of a large drift introduces greater bias
    3. The drift magnitude for early rates scales roughly as $O(n)$ in the number of forward rates, meaning the problem worsens with model dimensionality
    4. **Predictor--corrector schemes** or finer time stepping are most beneficial for the early forward rates

---

**Exercise 3.** The Girsanov drift adjustment from $\mathbb{Q}^{T_{k+1}}$ to $\mathbb{Q}^{T_k}$ involves the term $\frac{\tau_k\,\sigma_k(t)\,L_k(t)}{1 + \tau_k L_k(t)}$. Show that this drift is bounded above by $\sigma_k(t)$ and approaches $\sigma_k(t)$ when $\tau_k L_k(t)$ is large. Interpret this bound financially: what does it mean when the LIBOR rate is much larger than zero?

??? success "Solution to Exercise 3"
    The Girsanov drift adjustment from $\mathbb{Q}^{T_{k+1}}$ to $\mathbb{Q}^{T_k}$ involves the term:

    $$
    \gamma_k(t) = \frac{\tau_k\,\sigma_k(t)\,L_k(t)}{1 + \tau_k\,L_k(t)}
    $$

    **Upper bound:** Define $x = \tau_k L_k(t) \geq 0$. Then:

    $$
    \gamma_k(t) = \sigma_k(t)\frac{x}{1 + x}
    $$

    The function $g(x) = x/(1 + x)$ for $x \geq 0$ satisfies:

    - $g(0) = 0$
    - $g(x) < 1$ for all finite $x$
    - $g(x) \to 1$ as $x \to \infty$
    - $g'(x) = 1/(1+x)^2 > 0$ (strictly increasing)

    Therefore:

    $$
    \gamma_k(t) = \sigma_k(t)\frac{\tau_k L_k(t)}{1 + \tau_k L_k(t)} < \sigma_k(t)
    $$

    The drift term is **bounded above by $\sigma_k(t)$**.

    **Behavior when $\tau_k L_k(t)$ is large:** When $\tau_k L_k(t) \gg 1$:

    $$
    \frac{\tau_k L_k(t)}{1 + \tau_k L_k(t)} \approx 1 - \frac{1}{\tau_k L_k(t)} \to 1
    $$

    so $\gamma_k(t) \to \sigma_k(t)$.

    **Financial interpretation:** The quantity $\tau_k L_k(t)$ is the interest accrued over the period $[T_k, T_{k+1}]$. When this is large (high rates or long tenor):

    - The discount factor $1/(1 + \tau_k L_k)$ is significantly less than 1
    - The bond price ratio $P(t, T_{k-1})/P(t, T_k) = 1 + \tau_k L_k$ is large
    - The forward rate dominates the numéraire ratio, and the measure change has maximum impact

    When rates are near zero ($\tau_k L_k \approx 0$), the drift correction becomes small ($\gamma_k \approx \sigma_k \cdot \tau_k L_k \approx 0$), because the numéraire ratio is approximately 1 regardless of small rate movements.

---

**Exercise 4.** Compare the drift structure under the terminal measure versus the spot (rolling) measure. Under the terminal measure, the drift of $L_i$ involves a sum from $k = i+1$ to $n-1$. Under the spot measure, the drift involves a sum from $k = q(t)$ to $i$, where $q(t)$ is the index of the next reset date. Which measure produces larger absolute drifts for short-maturity forward rates, and why does this matter for simulation accuracy?

??? success "Solution to Exercise 4"
    **Terminal measure drift** of $L_i$:

    $$
    \mu_i^{(n)}(t) = -\sum_{j=i+1}^{n-1}\frac{\delta_j\,\rho_{ij}\,\sigma_i\,\sigma_j\,L_j(t)}{1 + \delta_j\,L_j(t)}
    $$

    The sum has $n - 1 - i$ terms. For short-maturity rates (small $i$), this is a large sum with many terms, potentially producing a large negative drift.

    **Spot measure drift** of $L_i$:

    $$
    \mu_i^{(B)}(t) = \sum_{j=q(t)}^{i}\frac{\delta_j\,\rho_{ij}\,\sigma_i\,\sigma_j\,L_j(t)}{1 + \delta_j\,L_j(t)}
    $$

    The sum has $i - q(t) + 1$ terms. For short-maturity rates (small $i$), this is a small sum with few terms.

    **Comparison for short-maturity rates:**

    Consider $L_1$ in a model with $n = 10$:

    - **Terminal measure:** drift involves $\sum_{j=2}^{9}$ = 8 terms, all negative
    - **Spot measure:** drift involves $\sum_{j=q(t)}^{1}$ = at most 2 terms (for $t < T_1$), all positive

    The terminal measure produces **much larger absolute drift** for short-maturity rates.

    **Why this matters for simulation accuracy:**

    1. Large drifts amplify discretization error in the Euler scheme. The error per step is proportional to $|\mu_i|\Delta t$, so larger drifts require smaller time steps to maintain accuracy.

    2. Under the terminal measure, $L_1$ has a large negative drift that can push the rate toward zero or require aggressive discretization. The frozen drift approximation is less accurate because the drift depends on many forward rates that evolve simultaneously.

    3. Under the spot measure, the drift grows with $i$ (long-maturity rates have more terms), but for any given rate, the correction is moderate because it only sums over lower-indexed rates.

    4. In the spot measure, rates can be updated sequentially ($L_1, L_2, \ldots, L_i$) within a time step, using already-updated values for the drift --- this natural ordering improves accuracy.

    **Conclusion:** The **spot measure** produces smaller absolute drifts for short-maturity forward rates and is generally preferred for simulation.

---

**Exercise 5.** The Radon--Nikodym derivative from the spot measure to the terminal measure involves the ratio of the discretely-compounded money market account to the terminal bond price. Show that this ratio equals $\prod_{j=q(t)}^{n-1}(1 + \tau_j L_j(t))$ (up to a deterministic factor) and explain why the spot and rolling-forward measures coincide when evaluated at discrete tenor dates.

??? success "Solution to Exercise 5"
    The Radon--Nikodym derivative from the spot measure to the $T_n$-forward measure at a tenor date $T_k$ is:

    $$
    \frac{d\mathbb{Q}^{T_n}}{d\mathbb{Q}^B}\bigg|_{\mathcal{F}_{T_k}} = \frac{P(T_k, T_n)/P(0, T_n)}{B(T_k)/B(0)}
    $$

    The money market account at $T_k$ is:

    $$
    B(T_k) = \prod_{j=0}^{k-1}(1 + \tau_j L_j(T_j))
    $$

    The bond price $P(T_k, T_n)$ in terms of forward rates:

    $$
    P(T_k, T_n) = \prod_{j=k}^{n-1}\frac{1}{1 + \tau_j L_j(T_k)}
    $$

    Therefore the ratio:

    $$
    \frac{B(T_k)}{P(T_k, T_n)} = \prod_{j=0}^{k-1}(1 + \tau_j L_j(T_j)) \cdot \prod_{j=k}^{n-1}(1 + \tau_j L_j(T_k))
    $$

    The Radon--Nikodym derivative becomes (up to deterministic initial-value factors):

    $$
    \frac{d\mathbb{Q}^B}{d\mathbb{Q}^{T_n}}\bigg|_{\mathcal{F}_{T_k}} \propto \frac{B(T_k)}{P(T_k, T_n)} \propto \prod_{j=q(t)}^{n-1}(1 + \tau_j L_j(t))
    $$

    For general $t$ between tenor dates, using the rolling bank account $B(t) = P(t, T_{q(t)})\prod_{j=0}^{q(t)-1}(1 + \tau_j L_j(T_j))$:

    $$
    \frac{B(t)}{P(t, T_n)} = \prod_{j=0}^{q(t)-1}(1 + \tau_j L_j(T_j)) \cdot \frac{P(t, T_{q(t)})}{P(t, T_n)} = \prod_{j=0}^{q(t)-1}(1 + \tau_j L_j(T_j)) \cdot \prod_{j=q(t)}^{n-1}(1 + \tau_j L_j(t))
    $$

    Up to a deterministic factor (involving initial bond prices), this is $\prod_{j=q(t)}^{n-1}(1 + \tau_j L_j(t))$.

    **Why spot and rolling-forward measures coincide at tenor dates:**

    At $t = T_k$, the spot measure Radon--Nikodym derivative relative to $\mathbb{Q}^{T_{q(t)}} = \mathbb{Q}^{T_k}$ is:

    $$
    Z_{T_k} = \frac{B(T_k)/B(0)}{P(T_k, T_k)/P(0, T_k)} = \frac{C_1 \cdot P(T_k, T_k)}{C_2 \cdot P(T_k, T_k)} = \frac{C_1}{C_2}
    $$

    where $C_1$ and $C_2$ are products of realized LIBOR fixings and initial forward rates, respectively. Since $\mathbb{E}^{T_k}[Z_{T_k}] = 1$ by construction, and $Z_{T_k}$ is deterministic (constant), we must have $C_1/C_2 = 1$. Therefore, the spot measure equals the current rolling forward measure $\mathbb{Q}^{T_{q(t)}}$ at tenor dates, meaning $dW^B_t = dW^{q(t)}_t$.

---

**Exercise 6.** In a "frozen drift" approximation, the drift of $L_i$ under the terminal measure is evaluated using the initial values $L_k(0)$ rather than the simulated values $L_k(t)$. For the model in Exercise 1, compute the frozen drift and compare it to the exact drift (using current rate values). Under what conditions does the frozen drift approximation fail significantly?

??? success "Solution to Exercise 6"
    **Frozen drift computation for Exercise 1 parameters:**

    Using the setup from Exercise 1 ($n = 5$, $i = 1$, constant volatilities $\sigma_k$, correlations $\rho_{1k}$), the frozen drift replaces $L_j(t)$ with $L_j(0)$:

    $$
    \mu_1^{\text{frozen}} = -\sum_{j=2}^{4}\frac{\delta_j\,\rho_{1j}\,\sigma_1\,\sigma_j\,L_j(0)}{1 + \delta_j\,L_j(0)}
    $$

    This is a constant (time-independent), computed once at the start of the simulation.

    The exact drift uses $L_j(t)$:

    $$
    \mu_1^{\text{exact}}(t) = -\sum_{j=2}^{4}\frac{\delta_j\,\rho_{1j}\,\sigma_1\,\sigma_j\,L_j(t)}{1 + \delta_j\,L_j(t)}
    $$

    **Comparison:** The difference between the exact and frozen drifts arises from the deviation of $L_j(t)$ from $L_j(0)$. Define $f(L) = \delta L/(1 + \delta L)$, which is an increasing, concave function. The drift depends on $f(L_j(t))$, so:

    - If $L_j(t) > L_j(0)$ for most $j$: $f(L_j(t)) > f(L_j(0))$, so the exact drift is more negative than the frozen drift
    - If $L_j(t) < L_j(0)$: the exact drift is less negative

    **Conditions under which the frozen drift approximation fails significantly:**

    1. **Long simulation horizon:** Over long periods, forward rates can deviate substantially from initial values ($L_j(t)$ may differ from $L_j(0)$ by 100+ basis points), making the frozen approximation inaccurate.

    2. **High volatility:** Large $\sigma_j$ causes forward rates to disperse quickly from their initial values, amplifying the difference between $f(L_j(t))$ and $f(L_j(0))$.

    3. **Large tenor spacing $\delta_j$:** The sensitivity $\partial f/\partial L = \delta/(1 + \delta L)^2$ increases with $\delta$, so annual tenors produce larger frozen-drift errors than quarterly tenors.

    4. **Extreme rate scenarios:** When rates move significantly (e.g., during stress tests), the frozen drift may severely understate or overstate the true drift, leading to biased pricing of path-dependent derivatives.

    5. **Many forward rates:** When $n$ is large, the drift sum contains many terms, and the cumulative error from freezing all of them can be substantial.

    In practice, the frozen drift approximation is acceptable for short-dated European options but should not be used for long-dated path-dependent products (Bermudan swaptions, callable range accruals) without at least a predictor--corrector correction.
