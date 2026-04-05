# LMM Simulation and Discretization

The LIBOR Market Model typically requires **Monte Carlo simulation** for pricing path-dependent and multi-exercise derivatives. Since the continuous-time SDE for forward rates has state-dependent drift (under all common measures except the individual forward measures), careful discretization is essential. This section develops the Euler and log-Euler discretization schemes, examines the drift approximation problem (frozen drift vs. predictor--corrector), and discusses the choice of simulation measure.

---

## Continuous-Time Dynamics

### Terminal Measure Dynamics

Under the terminal measure $\mathbb{Q}^{T_n}$ (numéraire $P(t, T_n)$), the forward rate $L_i(t)$ satisfies

$$
\frac{dL_i(t)}{L_i(t)} = \mu_i^{(n)}(t)\,dt + \sigma_i(t)\,dW_i^{T_n}(t)
$$

with drift

$$
\mu_i^{(n)}(t) = -\sum_{j=i+1}^{n-1} \frac{\delta_j \rho_{ij} \sigma_i(t) \sigma_j(t) L_j(t)}{1 + \delta_j L_j(t)}
$$

### Spot Measure Dynamics

Under the spot (rolling) measure $\mathbb{Q}^B$ (numéraire: discretely-compounded bank account), the drift reverses sign:

$$
\mu_i^{(B)}(t) = \sum_{j=\eta(t)}^{i} \frac{\delta_j \rho_{ij} \sigma_i(t) \sigma_j(t) L_j(t)}{1 + \delta_j L_j(t)}
$$

where $\eta(t) = \min\{k : T_k > t\}$.

### Key Feature

In both cases, the drift depends on the **current values** of all forward rates in the summation range. This state-dependence prevents closed-form solutions and necessitates simulation.

---

## Euler Discretization

### Direct Euler Scheme

The simplest discretization of $dL_i / L_i = \mu_i \, dt + \sigma_i \, dW_i$ is

$$
L_i(t + \Delta t) = L_i(t) + L_i(t) \, \mu_i(t) \, \Delta t + L_i(t) \, \sigma_i(t) \, \sqrt{\Delta t} \, Z_i
$$

where $Z_i$ are correlated standard normals with $\text{Corr}(Z_i, Z_j) = \rho_{ij}$.

**Problem:** This scheme can produce **negative forward rates** because the increment $L_i(t)\mu_i(t)\Delta t + L_i(t)\sigma_i(t)\sqrt{\Delta t}\,Z_i$ can exceed $L_i(t)$ in magnitude.

### Log-Euler Scheme

A better approach discretizes $\ln L_i(t)$ instead. From Itô's lemma:

$$
d\ln L_i(t) = \left(\mu_i(t) - \frac{1}{2}\sigma_i(t)^2\right)dt + \sigma_i(t)\,dW_i(t)
$$

Discretizing:

$$
\boxed{\ln L_i(t + \Delta t) = \ln L_i(t) + \left(\mu_i(t) - \frac{1}{2}\sigma_i(t)^2\right)\Delta t + \sigma_i(t)\sqrt{\Delta t}\,Z_i}
$$

Equivalently:

$$
L_i(t + \Delta t) = L_i(t) \exp\!\left[\left(\mu_i(t) - \frac{1}{2}\sigma_i(t)^2\right)\Delta t + \sigma_i(t)\sqrt{\Delta t}\,Z_i\right]
$$

The log-Euler scheme **preserves positivity** of forward rates, since the exponential is always positive.

---

## Generating Correlated Normals

### Cholesky Decomposition

To generate the correlated normal vector $Z = (Z_1, \ldots, Z_{n-1})$ with covariance matrix $\rho$:

1. Compute the Cholesky factor $L$ such that $LL^\top = \rho$
2. Generate independent standard normals $\xi = (\xi_1, \ldots, \xi_{n-1})$
3. Set $Z = L\xi$

Then $\text{Cov}(Z_i, Z_j) = (LL^\top)_{ij} = \rho_{ij}$.

### Rank-Reduced Decomposition

When using a rank-$d$ approximation $\rho \approx BB^\top$ with $B \in \mathbb{R}^{n \times d}$, only $d$ independent normals are needed:

$$
Z_i = \sum_{k=1}^{d} B_{ik} \, \xi_k
$$

This reduces the cost from $O(n^2)$ to $O(nd)$ per time step, which is significant for $n \gg d$.

---

## Drift Approximation Methods

### The Drift Problem

The drift $\mu_i(t)$ depends on the current forward rates $L_j(t)$, which are themselves being simulated. At time $t + \Delta t$, the drift should use forward rate values between $t$ and $t + \Delta t$, but these are unknown.

### Frozen Drift Approximation

The simplest approach "freezes" the drift at time $t$:

$$
\mu_i^{\text{frozen}} = \mu_i(t) \quad \text{(uses } L_j(t) \text{)}
$$

This is a standard Euler approximation. It introduces bias of order $O(\Delta t)$ in the drift, leading to overall weak convergence of order $O(\Delta t^{1/2})$.

### Predictor--Corrector Method

The predictor--corrector scheme improves accuracy by using the drift at the average of the beginning and end of the time step:

**Step 1 (Predict):** Compute a preliminary value using the frozen drift:

$$
\tilde{L}_i(t + \Delta t) = L_i(t) \exp\!\left[\left(\mu_i(t) - \frac{1}{2}\sigma_i^2\right)\Delta t + \sigma_i\sqrt{\Delta t}\,Z_i\right]
$$

**Step 2 (Correct):** Re-evaluate the drift using the predicted values:

$$
\tilde{\mu}_i = \mu_i\bigl(\tilde{L}(t + \Delta t)\bigr)
$$

**Step 3 (Average):** Use the averaged drift for the final update:

$$
L_i(t + \Delta t) = L_i(t) \exp\!\left[\left(\frac{\mu_i(t) + \tilde{\mu}_i}{2} - \frac{1}{2}\sigma_i^2\right)\Delta t + \sigma_i\sqrt{\Delta t}\,Z_i\right]
$$

The predictor--corrector achieves $O(\Delta t)$ weak convergence, allowing larger time steps.

### Drift Interpolation (Glasserman--Zhao)

An intermediate approach evaluates the drift at the midpoint of the time step:

$$
\mu_i^{\text{mid}} \approx \mu_i\!\left(\sqrt{L(t) \cdot \tilde{L}(t + \Delta t)}\right)
$$

using the geometric mean of beginning and predicted ending values.

---

## Choice of Simulation Measure

### Terminal Measure

Under $\mathbb{Q}^{T_n}$, all forward rates have **negative drift** corrections (for $i < n-1$). The last forward rate $L_{n-1}$ is a martingale (zero drift).

**Advantage:** The drift sum goes from $i+1$ to $n-1$, so shorter-maturity rates have larger drift corrections but the summation is bounded.

**Disadvantage:** Negative drifts can cause numerical issues for early forward rates when many terms accumulate.

### Spot Measure

Under $\mathbb{Q}^B$, all forward rates have **positive drift** corrections. The drift sum goes from $\eta(t)$ to $i$.

**Advantage:** Positive drifts; natural for pricing products involving the rolling bank account.

**Disadvantage:** The drift sum grows as $i$ increases, so long-maturity rates have larger corrections.

### Practical Recommendation

The spot measure is generally preferred for production implementations because:

- Positive drifts are more numerically stable
- The rolling bank account is the natural numéraire for discounting
- The drift sum only includes "live" forward rates (those not yet expired)

---

## Time-Stepping Strategy

### Step Size Selection

The natural time grid is the tenor structure $\{T_0, T_1, \ldots, T_n\}$. Between tenor dates, the volatilities and correlations are typically constant (piecewise constant specification), so **one step per tenor period** suffices.

For time-homogeneous or continuous volatilities, finer sub-stepping may be needed:

$$
\Delta t = \frac{T_{k+1} - T_k}{M}
$$

where $M$ is the number of sub-steps per tenor period. Typical values are $M = 1$ (coarse) to $M = 4$ (fine).

### Adaptive Stepping

Near-expiry caplets require finer stepping because the drift corrections become large as forward rates approach their fixing dates.

### Dimension Reduction Over Time

As simulation advances, expired forward rates ($L_i$ for $T_i < t$) no longer need to be evolved. The effective dimension decreases from $n-1$ at $t = 0$ to $0$ at $t = T_{n-1}$.

---

## Variance Reduction

### Antithetic Variates

For each path with random draws $Z$, simulate a mirror path with $-Z$. The estimator

$$
\hat{V} = \frac{1}{2}\bigl(V(Z) + V(-Z)\bigr)
$$

reduces variance when the payoff is monotone in the forward rates.

### Control Variates

Use the analytically known caplet prices as control variates:

$$
\hat{V}^{\text{CV}} = \hat{V}^{\text{MC}} - c\bigl(\hat{C}^{\text{MC}} - C^{\text{exact}}\bigr)
$$

where $C$ is a caplet price and $c$ is chosen to minimize variance.

### Importance Sampling

Shift the drift to increase the probability of exercise for deep out-of-the-money options. This requires computing the Radon--Nikodym derivative for the measure shift.

---

## Algorithm Summary

The complete LMM simulation algorithm for pricing under the spot measure proceeds as follows:

1. **Initialize:** Set $L_i(0)$ for $i = 0, \ldots, n-1$ from the market forward curve
2. **For each time step** $t_k \to t_{k+1}$:
    - Generate $d$ independent normals $\xi_1, \ldots, \xi_d$
    - Compute correlated normals $Z_i = \sum_{j=1}^{d} B_{ij}\xi_j$
    - **For each live forward rate** $L_i$ (with $T_i > t_k$):
        - Compute drift $\mu_i^{(B)}$ using current forward rates
        - Update: $\ln L_i \leftarrow \ln L_i + (\mu_i - \frac{1}{2}\sigma_i^2)\Delta t + \sigma_i\sqrt{\Delta t}\,Z_i$
    - (Optional) Predictor--corrector: recompute drift and average
3. **Compute payoff** from the simulated forward rate paths
4. **Discount** using the simulated bank account: $\text{Price} = \mathbb{E}[\text{Payoff}/B_T]$
5. **Repeat** for $N_{\text{paths}}$ paths and average

---

## Key Takeaways

- The **log-Euler scheme** is preferred over direct Euler because it preserves positivity of forward rates
- **Drift approximation** is the main source of discretization error: frozen drift gives $O(\sqrt{\Delta t})$ convergence, predictor--corrector gives $O(\Delta t)$
- Correlated normals are generated via **Cholesky decomposition** or, more efficiently, via rank-reduced factor loadings
- The **spot measure** is preferred for production because of positive drifts and natural discounting
- **One step per tenor period** typically suffices for piecewise constant volatilities
- **Variance reduction** (antithetic, control variates) is essential for computational efficiency

---

## Further Reading

- Glasserman (2003), *Monte Carlo Methods in Financial Engineering*, Chapter 8
- Andersen & Piterbarg (2010), *Interest Rate Modeling*, Volume II, Chapters 13--14
- Brigo & Mercurio (2006), *Interest Rate Models: Theory and Practice*, Chapter 7
- Hunter, Jäckel & Joshi (2001), "Getting the Drift: LMM Simulation"

---

## Exercises

**Exercise 1.** In the log-Euler scheme for the LMM, the forward rate is updated as

$$
\ln L_i(t + \Delta t) = \ln L_i(t) + \left(\mu_i(t) - \frac{1}{2}\sigma_i^2\right)\Delta t + \sigma_i\sqrt{\Delta t}\,Z_i
$$

where $Z_i$ are correlated standard normals. For $L_i(t) = 4\%$, $\mu_i(t) = -0.001$, $\sigma_i = 0.20$, and $\Delta t = 0.25$, generate one sample of $L_i(t + \Delta t)$ using $Z_i = 0.75$. Verify that the result is positive regardless of the value of $Z_i$.

??? success "Solution to Exercise 1"
    **Given:** $L_i(t) = 0.04$, $\mu_i(t) = -0.001$, $\sigma_i = 0.20$, $\Delta t = 0.25$, $Z_i = 0.75$.

    The log-Euler update formula is:

    $$
    \ln L_i(t + \Delta t) = \ln L_i(t) + \left(\mu_i(t) - \frac{1}{2}\sigma_i^2\right)\Delta t + \sigma_i\sqrt{\Delta t}\,Z_i
    $$

    **Step 1: Compute $\ln L_i(t)$.**

    $$
    \ln L_i(t) = \ln(0.04) = -3.2189
    $$

    **Step 2: Compute the drift-adjusted term.**

    $$
    \mu_i - \frac{1}{2}\sigma_i^2 = -0.001 - \frac{1}{2}(0.04) = -0.001 - 0.02 = -0.021
    $$

    $$
    \left(\mu_i - \frac{1}{2}\sigma_i^2\right)\Delta t = -0.021 \times 0.25 = -0.00525
    $$

    **Step 3: Compute the diffusion term.**

    $$
    \sigma_i\sqrt{\Delta t}\,Z_i = 0.20 \times \sqrt{0.25} \times 0.75 = 0.20 \times 0.50 \times 0.75 = 0.075
    $$

    **Step 4: Update.**

    $$
    \ln L_i(t + \Delta t) = -3.2189 + (-0.00525) + 0.075 = -3.2189 - 0.00525 + 0.075 = -3.14915
    $$

    $$
    L_i(t + \Delta t) = e^{-3.14915} = 0.04287 = 4.287\%
    $$

    **Positivity verification:** The log-Euler scheme updates $\ln L_i$, and since $L_i(t + \Delta t) = \exp(\ln L_i(t + \Delta t))$, the result is always positive regardless of $Z_i$. Even for $Z_i = -10$ (an extreme negative draw):

    $$
    \ln L_i(t + \Delta t) = -3.2189 - 0.00525 + 0.20 \times 0.50 \times (-10) = -3.2189 - 0.00525 - 1.0 = -4.22415
    $$

    $$
    L_i(t + \Delta t) = e^{-4.22415} = 0.01463 > 0
    $$

    The exponential function maps any real number to a positive number, so $L_i > 0$ always holds.

---

**Exercise 2.** Explain why the direct Euler scheme $L_i(t + \Delta t) = L_i(t) + \mu_i L_i \Delta t + \sigma_i L_i \sqrt{\Delta t}\,Z_i$ can produce negative forward rates, while the log-Euler scheme cannot. For what values of $Z_i$ does the direct Euler scheme give $L_i(t+\Delta t) < 0$ when $L_i(t) = 2\%$, $\sigma_i = 0.30$, and $\Delta t = 1$?

??? success "Solution to Exercise 2"
    **Direct Euler scheme:**

    $$
    L_i(t + \Delta t) = L_i(t) + \mu_i L_i(t)\Delta t + \sigma_i L_i(t)\sqrt{\Delta t}\,Z_i
    $$

    $$
    = L_i(t)\bigl(1 + \mu_i\Delta t + \sigma_i\sqrt{\Delta t}\,Z_i\bigr)
    $$

    This is negative when the factor in parentheses is negative:

    $$
    1 + \mu_i\Delta t + \sigma_i\sqrt{\Delta t}\,Z_i < 0
    $$

    $$
    Z_i < -\frac{1 + \mu_i\Delta t}{\sigma_i\sqrt{\Delta t}}
    $$

    **For the given parameters:** $L_i(t) = 0.02$, $\sigma_i = 0.30$, $\Delta t = 1$, and assuming $\mu_i = 0$ for simplicity:

    $$
    Z_i < -\frac{1 + 0}{0.30 \times 1} = -\frac{1}{0.30} = -3.33
    $$

    Any draw $Z_i < -3.33$ produces a negative forward rate. The probability is:

    $$
    P(Z < -3.33) = N(-3.33) \approx 0.043\%
    $$

    This is small but nonzero, and over many paths and time steps, negative rates will occur.

    **Why the log-Euler scheme avoids this:** The log-Euler scheme updates $\ln L_i$:

    $$
    \ln L_i(t + \Delta t) = \ln L_i(t) + \left(\mu_i - \frac{1}{2}\sigma_i^2\right)\Delta t + \sigma_i\sqrt{\Delta t}\,Z_i
    $$

    Since $L_i(t + \Delta t) = \exp(\ln L_i(t + \Delta t))$, and the exponential function is always positive for any real argument, $L_i(t + \Delta t) > 0$ for all values of $Z_i$. The log transformation maps the real line to $(0, \infty)$, inherently preserving positivity.

    **Note on large $\sigma$ or $\Delta t$:** The direct Euler scheme becomes increasingly problematic as $\sigma\sqrt{\Delta t}$ grows. For $\sigma = 0.30$ and $\Delta t = 1$, $\sigma\sqrt{\Delta t} = 0.30$, which gives a 3.33-sigma threshold. For $\sigma = 0.50$ and $\Delta t = 1$, the threshold drops to $-2.0$, giving $P \approx 2.3\%$ --- much more frequent negative rates.

---

**Exercise 3.** The predictor--corrector method for the LMM drift uses the following two-step procedure: (a) compute a "predicted" rate using the Euler drift at time $t$, (b) recompute the drift at the predicted rate, and (c) average the two drifts for the final update. Write out this procedure explicitly for the terminal-measure drift and explain why it achieves higher-order convergence ($O(\Delta t)$ rather than $O(\sqrt{\Delta t})$).

??? success "Solution to Exercise 3"
    **Predictor--corrector for the terminal measure drift:**

    The drift under $\mathbb{Q}^{T_n}$ is:

    $$
    \mu_i^{(n)}(t) = -\sum_{j=i+1}^{n-1}\frac{\delta_j\,\rho_{ij}\,\sigma_i\,\sigma_j\,L_j(t)}{1 + \delta_j\,L_j(t)}
    $$

    **Step 1 (Predict):** Using the drift at time $t$ (with current rates $L_j(t)$):

    $$
    \mu_i^{(n),\text{pred}} = -\sum_{j=i+1}^{n-1}\frac{\delta_j\,\rho_{ij}\,\sigma_i\,\sigma_j\,L_j(t)}{1 + \delta_j\,L_j(t)}
    $$

    Compute preliminary values:

    $$
    \tilde{L}_i(t + \Delta t) = L_i(t)\exp\left[\left(\mu_i^{(n),\text{pred}} - \frac{1}{2}\sigma_i^2\right)\Delta t + \sigma_i\sqrt{\Delta t}\,Z_i\right]
    $$

    Do this for all $i$ to obtain $\tilde{L}_0, \ldots, \tilde{L}_{n-1}$.

    **Step 2 (Correct):** Recompute the drift using the predicted rates $\tilde{L}_j(t + \Delta t)$:

    $$
    \mu_i^{(n),\text{corr}} = -\sum_{j=i+1}^{n-1}\frac{\delta_j\,\rho_{ij}\,\sigma_i\,\sigma_j\,\tilde{L}_j(t + \Delta t)}{1 + \delta_j\,\tilde{L}_j(t + \Delta t)}
    $$

    **Step 3 (Average):** Use the averaged drift for the final update:

    $$
    \bar{\mu}_i = \frac{1}{2}\left(\mu_i^{(n),\text{pred}} + \mu_i^{(n),\text{corr}}\right)
    $$

    $$
    L_i(t + \Delta t) = L_i(t)\exp\left[\left(\bar{\mu}_i - \frac{1}{2}\sigma_i^2\right)\Delta t + \sigma_i\sqrt{\Delta t}\,Z_i\right]
    $$

    **Why this achieves higher-order convergence:**

    The frozen (Euler) drift approximation uses $\mu_i(t)$ throughout $[t, t+\Delta t]$, introducing an error of order $O(\Delta t)$ in the drift (since $\mu_i(t + \Delta t) - \mu_i(t) = O(\sqrt{\Delta t})$ due to the Brownian increments, and the integrated drift error over $\Delta t$ is $O(\Delta t^{3/2})$).

    The predictor--corrector uses $\frac{1}{2}(\mu_i(t) + \mu_i(t + \Delta t))$, which is a trapezoidal approximation to $\int_t^{t+\Delta t}\mu_i(s)\,ds$. The trapezoidal rule has error $O(\Delta t^3)$ for smooth integrands, but since the drift is stochastic, the effective error is $O(\Delta t^2)$ in the integrated drift.

    For the SDE discretization:

    - **Frozen drift (Euler):** weak convergence order $O(\Delta t^{1/2})$ (or $O(\Delta t)$ for the drift contribution alone, but the overall weak order is $1/2$ due to the interaction of drift error with the diffusion)
    - **Predictor--corrector:** weak convergence order $O(\Delta t)$ --- the drift error is reduced by one order, allowing the use of larger time steps without sacrificing accuracy

---

**Exercise 4.** For an LMM with $n = 10$ forward rates and exponential correlation $\rho_{ij} = e^{-0.1|i-j|}$, describe how to generate correlated normal random variables using (a) full Cholesky decomposition and (b) rank-3 factor loading matrix $B \in \mathbb{R}^{10 \times 3}$. Compare the computational cost per time step for each approach.

??? success "Solution to Exercise 4"
    **Setting:** $n = 10$ forward rates, exponential correlation $\rho_{ij} = e^{-0.1|i-j|}$.

    **(a) Full Cholesky decomposition:**

    1. Compute the $10 \times 10$ correlation matrix $\rho$
    2. Perform Cholesky factorization: $\rho = LL^\top$, where $L$ is lower triangular. Cost: $O(n^3/3) \approx 333$ operations (done once)
    3. At each time step, generate 10 independent standard normals $\xi_1, \ldots, \xi_{10}$
    4. Compute $Z = L\xi$: matrix-vector multiply, cost $O(n^2/2) = 50$ multiplications per step

    **Total cost per time step:** $O(n^2) = O(100)$ operations for the correlated normals, plus $O(n^2) = O(100)$ for drift computation.

    **(b) Rank-3 factor loading matrix:**

    1. Compute eigendecomposition of $\rho$: find eigenvalues $\lambda_1 \geq \lambda_2 \geq \lambda_3$ and eigenvectors $v_1, v_2, v_3$
    2. Form $B = [v_1\sqrt{\lambda_1}, v_2\sqrt{\lambda_2}, v_3\sqrt{\lambda_3}] \in \mathbb{R}^{10 \times 3}$
    3. Normalize rows to unit length (for unit diagonal)
    4. At each time step, generate only 3 independent standard normals $\xi_1, \xi_2, \xi_3$
    5. Compute $Z_i = \sum_{k=1}^3 B_{ik}\xi_k$ for each $i$: cost $O(nd) = O(30)$ per step

    **Cost comparison per time step:**

    | Operation | Full Cholesky | Rank-3 |
    |---|---|---|
    | Random number generation | 10 normals | 3 normals |
    | Correlated normals | $O(n^2) = 100$ ops | $O(nd) = 30$ ops |
    | Drift computation | $O(n^2) = 100$ ops | $O(n^2) = 100$ ops (same) |
    | **Total** | **~200 ops** | **~130 ops** |

    The rank-3 approach saves about 35% per step for $n = 10$. The savings become much more significant for large $n$: for $n = 120$ (30-year quarterly), the correlated normals cost drops from $O(14{,}400)$ to $O(360)$, a 40x speedup.

    **Accuracy:** For the exponential correlation with $\beta = 0.1$, the first 3 eigenvalues capture approximately 95--97% of the total correlation structure, so the rank-3 approximation introduces minimal pricing error for most products.

---

**Exercise 5.** A cap on 3-month LIBOR with 5 years of quarterly caplets is priced by Monte Carlo in the LMM. The simulation uses 10,000 paths with one time step per quarter. Estimate the standard error of the Monte Carlo estimate if the caplet prices are approximately \$0.50 per \$100 notional. Describe how antithetic variates reduce this standard error.

??? success "Solution to Exercise 5"
    **Setting:** 5-year cap with quarterly caplets (20 caplets), priced by Monte Carlo with 10,000 paths.

    Each caplet pays approximately \$0.50 per \$100 notional. The cap price is:

    $$
    C = \sum_{i=1}^{20}\text{Caplet}_i \approx 20 \times 0.50 = \$10.00
    $$

    **Standard error estimate:**

    The standard error of the cap price estimate is $\text{SE} = \text{std}(\hat{C})/\sqrt{N}$, where $\hat{C}$ is the per-path cap payoff.

    Assuming each caplet payoff has standard deviation roughly proportional to its mean (a common feature of option payoffs), say $\text{std}(\text{Caplet}_i) \approx 2 \times \text{mean}(\text{Caplet}_i) = \$1.00$. Since the caplets are correlated (driven by correlated forward rates), the total cap payoff has:

    $$
    \text{std}(\hat{C}) \approx \sqrt{\sum_{i,j}\text{Cov}(\text{Caplet}_i, \text{Caplet}_j)}
    $$

    As a rough estimate, with moderate correlation: $\text{std}(\hat{C}) \approx \$8$--$\$15$.

    $$
    \text{SE} = \frac{15}{\sqrt{10{,}000}} = \frac{15}{100} = \$0.15
    $$

    This is about 1.5% of the cap price --- acceptable but not highly precise.

    **How antithetic variates reduce standard error:**

    For each path with random draws $Z = (Z_1, \ldots, Z_{20})$, simulate a mirror path with $-Z$. The antithetic estimator is:

    $$
    \hat{C}^{\text{anti}} = \frac{1}{2}\bigl(C(Z) + C(-Z)\bigr)
    $$

    Variance reduction occurs because:

    $$
    \text{Var}(\hat{C}^{\text{anti}}) = \frac{1}{4}\bigl(\text{Var}(C(Z)) + \text{Var}(C(-Z)) + 2\text{Cov}(C(Z), C(-Z))\bigr)
    $$

    $$
    = \frac{1}{2}\text{Var}(C(Z)) + \frac{1}{2}\text{Cov}(C(Z), C(-Z))
    $$

    Since the cap payoff $C(Z)$ is a monotonically increasing function of the forward rates (which increase with $Z$), $C(Z)$ and $C(-Z)$ are negatively correlated: $\text{Cov}(C(Z), C(-Z)) < 0$.

    This negative covariance reduces the variance of $\hat{C}^{\text{anti}}$ compared to the standard estimator. In practice, antithetic variates can reduce variance by 50--80% for cap pricing, effectively reducing the standard error by a factor of $\sqrt{2}$ to $\sqrt{5}$.

---

**Exercise 6.** The spot measure (rolling money-market numéraire) is preferred for Monte Carlo simulation over the terminal measure. Explain two reasons for this preference: (a) the drift of each forward rate involves only rates with indices up to $i$ (not beyond), and (b) the money-market account provides a natural discounting mechanism. Why does the terminal measure sometimes produce larger discretization errors for short-dated rates?

??? success "Solution to Exercise 6"
    **Two reasons the spot measure is preferred for Monte Carlo simulation:**

    **(a) Forward-looking drift structure:**

    Under the **spot measure**, the drift of $L_i$ involves only rates with indices up to $i$:

    $$
    \mu_i^{(B)}(t) = \sum_{j=\eta(t)}^{i}\frac{\delta_j\,\rho_{ij}\,\sigma_i\,\sigma_j\,L_j(t)}{1 + \delta_j\,L_j(t)}
    $$

    This means the drift of $L_i$ depends only on $L_{\eta(t)}, \ldots, L_i$ --- rates that have already been updated (or are being updated) at the current time step. Rates can be evolved **in order** from $L_{\eta(t)}$ to $L_{n-1}$, using the most current values.

    Under the **terminal measure**, the drift of $L_i$ involves rates $L_{i+1}, \ldots, L_{n-1}$, which have **not yet been updated** at the current step if processing in forward order. This creates an inconsistency that the predictor--corrector addresses but cannot fully eliminate.

    **(b) Natural discounting mechanism:**

    Under the spot measure, the money market account is the numéraire:

    $$
    B(T_k) = \prod_{j=0}^{k-1}(1 + \delta_j L_j(T_j))
    $$

    This is computed directly from the simulated path. The price of any derivative is:

    $$
    V_0 = \mathbb{E}^B\left[\frac{\text{Payoff}}{B(T_{\text{pay}})}\right]
    $$

    No additional bond price simulation is needed --- the bank account path provides the discount factor. Under the terminal measure, one would need to compute $P(t, T_n)$ for discounting, which involves all forward rates and is more complex.

    **Why the terminal measure produces larger discretization errors for short-dated rates:**

    Under the terminal measure, $L_1$ (the shortest-maturity rate) has a drift involving $n - 2$ terms, all depending on rates $L_2, \ldots, L_{n-1}$. This drift can be large in absolute value, especially for high-dimensional models. Large drifts mean:

    - The Euler discretization error is proportional to $|\mu_i|\Delta t$, so larger drifts require smaller steps
    - The frozen drift approximation is less accurate because the drift depends on many evolving rates
    - Numerical instability can arise if the negative drift pushes the rate toward zero

    Under the spot measure, $L_1$ has only 1--2 terms in its drift, producing much smaller corrections and better-behaved simulation.

---

**Exercise 7.** Design a control variate for the Monte Carlo pricing of a Bermudan swaption in the LMM. Specifically, use the analytical approximation (Rebonato's formula) for the corresponding European swaption as the control. Write down the control variate estimator and explain why this can dramatically reduce the variance of the Monte Carlo estimate.

??? success "Solution to Exercise 7"
    **Control variate design for Bermudan swaption pricing:**

    Let $V^{\text{Berm}}$ denote the Bermudan swaption price and $V^{\text{Euro}}$ the corresponding European swaption price (with the same strike and the most natural exercise date, e.g., the first exercise opportunity).

    **Analytical approximation:** Using Rebonato's formula, compute the European swaption price analytically:

    $$
    V^{\text{Euro, Reb}} = A(0)\bigl[S(0)N(d_1) - KN(d_2)\bigr]
    $$

    where $\sigma_S$ comes from Rebonato's formula.

    **Monte Carlo estimator without control variate:**

    $$
    \hat{V}^{\text{Berm}} = \frac{1}{N}\sum_{k=1}^{N}\text{Payoff}^{\text{Berm}}(\omega_k)
    $$

    **Control variate estimator:**

    On each Monte Carlo path, also compute the European swaption payoff. Define:

    $$
    \hat{V}^{\text{CV}} = \hat{V}^{\text{Berm}} - c\left(\hat{V}^{\text{Euro, MC}} - V^{\text{Euro, Reb}}\right)
    $$

    where:

    - $\hat{V}^{\text{Euro, MC}} = \frac{1}{N}\sum_{k=1}^N \text{Payoff}^{\text{Euro}}(\omega_k)$ is the Monte Carlo estimate of the European swaption
    - $V^{\text{Euro, Reb}}$ is the analytically computed price (Rebonato's formula)
    - $c$ is the optimal control variate coefficient, estimated by regression:

    $$
    c^* = \frac{\text{Cov}(\text{Payoff}^{\text{Berm}}, \text{Payoff}^{\text{Euro}})}{\text{Var}(\text{Payoff}^{\text{Euro}})}
    $$

    **Why this dramatically reduces variance:**

    1. **High correlation:** The Bermudan and European swaption payoffs are strongly correlated because they depend on the same underlying forward rates. The Bermudan value is always at least as large as the European value (since the Bermudan has more exercise opportunities), and both respond similarly to rate movements. Typical correlation: $\rho > 0.95$.

    2. **Variance reduction formula:** The variance of the control variate estimator is:

        $$
        \text{Var}(\hat{V}^{\text{CV}}) = \text{Var}(\hat{V}^{\text{Berm}})(1 - \rho^2)
        $$

        For $\rho = 0.98$: $(1 - 0.98^2) = 0.0396$, giving a **96% variance reduction** (equivalently, a 5x reduction in standard error).

    3. **Nearly free computation:** The European swaption payoff is computed as a by-product of the Bermudan simulation (it uses the same forward rate paths), so the additional computational cost is negligible.

    4. **Analytical benchmark:** Rebonato's formula provides a nearly exact price for the European swaption (accurate to within a few basis points), so $V^{\text{Euro, Reb}}$ is an excellent approximation of the true $\mathbb{E}[\text{Payoff}^{\text{Euro}}]$, ensuring the control variate has near-zero bias.
