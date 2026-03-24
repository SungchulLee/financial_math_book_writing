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

---

**Exercise 2.** Explain why the direct Euler scheme $L_i(t + \Delta t) = L_i(t) + \mu_i L_i \Delta t + \sigma_i L_i \sqrt{\Delta t}\,Z_i$ can produce negative forward rates, while the log-Euler scheme cannot. For what values of $Z_i$ does the direct Euler scheme give $L_i(t+\Delta t) < 0$ when $L_i(t) = 2\%$, $\sigma_i = 0.30$, and $\Delta t = 1$?

---

**Exercise 3.** The predictor--corrector method for the LMM drift uses the following two-step procedure: (a) compute a "predicted" rate using the Euler drift at time $t$, (b) recompute the drift at the predicted rate, and (c) average the two drifts for the final update. Write out this procedure explicitly for the terminal-measure drift and explain why it achieves higher-order convergence ($O(\Delta t)$ rather than $O(\sqrt{\Delta t})$).

---

**Exercise 4.** For an LMM with $n = 10$ forward rates and exponential correlation $\rho_{ij} = e^{-0.1|i-j|}$, describe how to generate correlated normal random variables using (a) full Cholesky decomposition and (b) rank-3 factor loading matrix $B \in \mathbb{R}^{10 \times 3}$. Compare the computational cost per time step for each approach.

---

**Exercise 5.** A cap on 3-month LIBOR with 5 years of quarterly caplets is priced by Monte Carlo in the LMM. The simulation uses 10,000 paths with one time step per quarter. Estimate the standard error of the Monte Carlo estimate if the caplet prices are approximately \$0.50 per \$100 notional. Describe how antithetic variates reduce this standard error.

---

**Exercise 6.** The spot measure (rolling money-market numéraire) is preferred for Monte Carlo simulation over the terminal measure. Explain two reasons for this preference: (a) the drift of each forward rate involves only rates with indices up to $i$ (not beyond), and (b) the money-market account provides a natural discounting mechanism. Why does the terminal measure sometimes produce larger discretization errors for short-dated rates?

---

**Exercise 7.** Design a control variate for the Monte Carlo pricing of a Bermudan swaption in the LMM. Specifically, use the analytical approximation (Rebonato's formula) for the corresponding European swaption as the control. Write down the control variate estimator and explain why this can dramatically reduce the variance of the Monte Carlo estimate.
