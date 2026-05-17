# Stochastic Volatility Models

Stochastic volatility models introduce a **second random factor** to capture the empirical observation that volatility itself fluctuates randomly over time. This creates volatility smile/skew, term structure effects, and volatility clustering.

---

### Motivation

#### Empirical Evidence

1. **Volatility clustering**: High volatility tends to follow high volatility
2. **Mean reversion**: Volatility reverts to a long-term average
3. **Leverage effect**: Negative correlation between returns and volatility
4. **Fat tails**: Return distributions have heavier tails than normal
5. **Smile persistence**: The volatility smile persists over time

#### Limitations of Local Volatility

Local volatility models fit the smile but predict it will flatten—contrary to market behavior. Stochastic volatility produces more realistic dynamics.

---

### General Framework

#### Two-Factor Model

Under the risk-neutral measure $\mathbb{Q}$:

$$
\boxed{
\begin{aligned}
dS_t &= rS_t\,dt + \sqrt{v_t}S_t\,dW_t^{(1)} \\
dv_t &= \alpha(t, v_t)\,dt + \beta(t, v_t)\,dW_t^{(2)} \\
d\langle W^{(1)}, W^{(2)}\rangle_t &= \rho\,dt
\end{aligned}
}
$$

where:

- $v_t$ is the **instantaneous variance** (or volatility squared)
- $\alpha(t, v)$ is the variance drift
- $\beta(t, v)$ is the **vol-of-vol** (volatility of volatility)
- $\rho$ is the correlation (typically negative for equities)

#### The Leverage Effect

When $\rho < 0$:

- Stock falls → volatility rises
- Creates negative skew in the smile
- Observed empirically: $\rho \approx -0.7$ for equity indices

---

### The Heston Model

#### Model Specification

$$
\boxed{
\begin{aligned}
dS_t &= rS_t\,dt + \sqrt{v_t}S_t\,dW_t^{(1)} \\
dv_t &= \kappa(\theta - v_t)\,dt + \xi\sqrt{v_t}\,dW_t^{(2)}
\end{aligned}
}
$$

**Parameters**:

- $\kappa > 0$: Speed of mean reversion
- $\theta > 0$: Long-term variance level
- $\xi > 0$: Vol-of-vol
- $\rho \in [-1, 1]$: Correlation
- $v_0$: Initial variance

#### Feller Condition

To ensure $v_t > 0$ (variance stays positive):

$$
\boxed{
2\kappa\theta \geq \xi^2
}
$$

If violated, variance can hit zero (but is reflected).

#### Affine Structure

Heston is an **affine** model: the characteristic function has exponential-affine form, enabling semi-analytical pricing via Fourier methods.

---

### Pricing in Stochastic Volatility

#### The 2D PDE

For option price $V(t, S, v)$:

$$
\boxed{
\frac{\partial V}{\partial t} + \frac{1}{2}vS^2\frac{\partial^2 V}{\partial S^2} + \rho\xi vS\frac{\partial^2 V}{\partial S\partial v} + \frac{1}{2}\xi^2 v\frac{\partial^2 V}{\partial v^2} + rS\frac{\partial V}{\partial S} + \kappa(\theta - v)\frac{\partial V}{\partial v} - rV = 0
}
$$

**Note**: The mixed derivative $\partial_{Sv}$ term arises from correlation.

#### Characteristic Function Method

For Heston, the log-price characteristic function is:

$$
\phi(u) = \mathbb{E}^{\mathbb{Q}}[e^{iu\log S_T} | S_t, v_t] = e^{C(T-t, u) + D(T-t, u)v_t + iu\log S_t}
$$

where $C$ and $D$ satisfy Riccati ODEs with known solutions.

#### Fourier Pricing

European call prices via inverse Fourier transform:

$$
C(K) = S_0 - \frac{Ke^{-rT}}{\pi}\int_0^\infty \text{Re}\left[\frac{e^{-iu\log K}\phi(u-i)}{iu}\right]du
$$

**Advantages**: Fast and accurate for vanilla options.

---

### Calibration

#### Parameters to Calibrate

| Parameter | Effect |
|-----------|--------|
| $v_0$ | Current ATM volatility level |
| $\theta$ | Long-term volatility level |
| $\kappa$ | Term structure shape |
| $\xi$ | Smile convexity (vol-of-vol) |
| $\rho$ | Smile skew |

#### Typical Procedure

1. Fix $v_0$ from ATM short-term options
2. Calibrate $\rho$ and $\xi$ from smile shape
3. Calibrate $\kappa$ and $\theta$ from term structure
4. Refine jointly via optimization

#### Identifiability Issues

- $\kappa$ and $\theta$ are often difficult to separate
- Multiple parameter sets can produce similar fits
- Regularization may be needed

---

### Incomplete Markets

Recall (see [§ Incomplete Markets and Pricing Bounds](incomplete_markets_and_pricing_bounds.md)): two Brownian motions $(W^{(1)},W^{(2)})$ with only $S$ traded leaves the volatility risk premium $\lambda(t,v_t)$ undetermined by no-arbitrage; under $\mathbb{P}$, $dv_t = [\kappa(\theta-v_t)-\lambda(t,v_t)]\,dt+\xi\sqrt{v_t}\,dW_t^{(2),\mathbb{P}}$, and calibration to option quotes selects a particular $\mathbb{Q}$.

---

### Other Stochastic Volatility Models

#### SABR Model

Popular for interest rate and FX options:

$$
\begin{aligned}
dF_t &= \sigma_t F_t^\beta\,dW_t^{(1)} \\
d\sigma_t &= \alpha\sigma_t\,dW_t^{(2)}
\end{aligned}
$$

**Asymptotic formula** for implied volatility (Hagan et al.):

$$
\sigma_{\text{imp}}(K) \approx \frac{\alpha}{(FK)^{(1-\beta)/2}}\left[1 + \frac{(1-\beta)^2}{24}\log^2\frac{F}{K} + \cdots\right] \times \frac{z}{x(z)}
$$

#### Hull-White Model

$$
dv_t = \mu v_t\,dt + \xi v_t\,dW_t^{(2)}
$$

Log-normal variance process.

#### 3/2 Model

$$
dv_t = \kappa v_t(\theta - v_t)\,dt + \xi v_t^{3/2}\,dW_t^{(2)}
$$

Higher vol-of-vol at high variance levels.

---

### Comparison: Local vs Stochastic Volatility

Recall (see [§ Local Volatility Models](local_volatility_models.md)): local vol is 1-factor, complete, fits the smile exactly but flattens the forward smile and hedges poorly; stochastic vol is 2-factor, incomplete, fits approximately but produces persistent forward smiles and more reliable exotic prices.

---

### Numerical Methods

#### Monte Carlo

```python
# Euler discretization for Heston
for i in range(N):
    dW1 = sqrt(dt) * randn()
    dW2 = rho * dW1 + sqrt(1 - rho**2) * sqrt(dt) * randn()
    
    v[i+1] = max(v[i] + kappa*(theta - v[i])*dt + xi*sqrt(v[i])*dW2, 0)
    S[i+1] = S[i] * exp((r - 0.5*v[i])*dt + sqrt(v[i])*dW1)
```

**Note**: Need to handle $v_t < 0$ (truncation, reflection, or better schemes).

#### PDE Methods

- ADI (Alternating Direction Implicit) for 2D PDE
- Finite differences on $(S, v)$ grid
- Careful boundary conditions at $v = 0$ and $v \to \infty$

---

### Summary

$$
\boxed{
\begin{aligned}
dS_t &= rS_t\,dt + \sqrt{v_t}S_t\,dW_t^{(1)} \\
dv_t &= \kappa(\theta - v_t)\,dt + \xi\sqrt{v_t}\,dW_t^{(2)}
\end{aligned}
}
$$

| Feature | Description |
|---------|-------------|
| **Key innovation** | Variance is a random process |
| **Smile generation** | Correlation $\rho$ creates skew |
| **Term structure** | Mean reversion $\kappa$ shapes it |
| **Market completeness** | Incomplete (2 factors, 1 asset) |
| **Pricing** | Fourier methods or 2D PDE |

**Stochastic volatility models capture realistic smile dynamics at the cost of market incompleteness, leading to more reliable exotic pricing and hedging than local volatility.**

---

## Exercises

**Exercise 1.** In the Heston model, the variance process $dv_t = \kappa(\theta - v_t)\,dt + \xi\sqrt{v_t}\,dW_t^{(2)}$ is a CIR process. (a) Verify the Feller condition $2\kappa\theta \geq \xi^2$ for the parameter set $\kappa = 2$, $\theta = 0.04$, $\xi = 0.3$. (b) When the Feller condition is violated, what happens to the variance process at $v = 0$? (c) Compute the long-run mean and variance of $v_t$ in terms of $\kappa$, $\theta$, and $\xi$.

??? success "Solution to Exercise 1"
    **(a)** The Feller condition requires $2\kappa\theta \geq \xi^2$. For $\kappa = 2$, $\theta = 0.04$, $\xi = 0.3$:

    $$
    2\kappa\theta = 2 \times 2 \times 0.04 = 0.16
    $$

    $$
    \xi^2 = 0.3^2 = 0.09
    $$

    Since $0.16 \geq 0.09$, the Feller condition is **satisfied**.

    **(b)** When the Feller condition is violated ($2\kappa\theta < \xi^2$), the variance process $v_t$ can reach zero. At $v = 0$, the drift term is $\kappa\theta > 0$ (pushing variance upward), but the diffusion term $\xi\sqrt{v_t}\,dW_t^{(2)}$ vanishes. The process touches zero but is immediately reflected back into the positive domain by the positive drift. Technically, zero becomes an **accessible** boundary that is **instantaneously reflecting**: the process hits $v = 0$ with positive probability but spends zero Lebesgue time there and bounces back. When the Feller condition holds, zero is **inaccessible** -- the process never reaches it because the drift dominates the diffusion near zero.

    **(c)** The CIR process $dv_t = \kappa(\theta - v_t)\,dt + \xi\sqrt{v_t}\,dW_t^{(2)}$ has the following stationary distribution properties. The long-run mean is obtained by taking expectations in the stationary state ($\mathbb{E}[dv_t] = 0$):

    $$
    \mathbb{E}[v_\infty] = \theta
    $$

    For the long-run variance, the CIR process has a Gamma stationary distribution with shape $\alpha = 2\kappa\theta/\xi^2$ and rate $\beta = 2\kappa/\xi^2$. The variance of this distribution is:

    $$
    \text{Var}(v_\infty) = \frac{\alpha}{\beta^2} = \frac{2\kappa\theta/\xi^2}{(2\kappa/\xi^2)^2} = \frac{\theta\xi^2}{2\kappa}
    $$

---


**Exercise 2.** The Heston PDE for option price $V(t, S, v)$ contains a mixed derivative term $\rho\xi v S \frac{\partial^2 V}{\partial S \partial v}$. (a) Explain the financial origin of this term in terms of the correlation between stock and volatility shocks. (b) Why does this term vanish when $\rho = 0$? (c) Describe the computational challenge this mixed derivative introduces for finite difference methods and how ADI (Alternating Direction Implicit) schemes address it.

??? success "Solution to Exercise 2"
    **(a)** The mixed derivative term $\rho\xi v S \frac{\partial^2 V}{\partial S \partial v}$ arises from the covariation between the stock price and variance processes. By Ito's lemma applied to $V(t, S_t, v_t)$:

    $$
    dV = \cdots + \frac{\partial^2 V}{\partial S \partial v} d\langle S, v\rangle_t
    $$

    The quadratic covariation is $d\langle S, v\rangle_t = \rho\xi v_t S_t\,dt$ (from $dS_t$ having diffusion $\sqrt{v_t}S_t\,dW_t^{(1)}$ and $dv_t$ having diffusion $\xi\sqrt{v_t}\,dW_t^{(2)}$ with $d\langle W^{(1)}, W^{(2)}\rangle_t = \rho\,dt$). This term captures how the option price changes due to simultaneous movements in both the stock price and the variance. Financially, it reflects the fact that when the stock drops and volatility rises simultaneously (for $\rho < 0$), the option value responds to this correlated movement in a way that cannot be decomposed into separate stock and volatility effects.

    **(b)** When $\rho = 0$, the Brownian motions $W^{(1)}$ and $W^{(2)}$ are independent, so $d\langle S, v\rangle_t = 0$. The stock price movements and variance movements are uncorrelated, and the option value's response to each can be computed independently. The 2D PDE then separates into terms involving only $S$-derivatives and only $v$-derivatives, with no cross term.

    **(c)** The mixed derivative $\partial_{Sv}V$ introduces a **cross-diffusion** term that couples the $S$ and $v$ directions. Standard finite difference methods for 2D PDEs (like simple explicit or implicit schemes) handle terms in each direction separately. The mixed derivative creates off-diagonal entries in the discretization matrix that prevent straightforward tridiagonal factorization. **ADI (Alternating Direction Implicit)** schemes address this by splitting each time step into sub-steps: one implicit in the $S$-direction (treating $v$ explicitly) and one implicit in the $v$-direction (treating $S$ explicitly). The mixed derivative is handled either by adding it to one of the sub-steps explicitly or by using a specialized splitting (e.g., the Craig-Sneyd or Hundsdorfer-Verwer schemes) that distributes the cross term appropriately. This preserves the efficiency of solving tridiagonal systems while maintaining stability.

---


**Exercise 3.** The Heston model has five parameters: $v_0, \kappa, \theta, \xi, \rho$. Describe the effect of each parameter on the implied volatility surface. Specifically: (a) Which parameter controls the ATM volatility level? (b) Which parameter controls the skew? (c) Which parameter controls the smile convexity (curvature)? (d) Which parameters determine the term structure?

??? success "Solution to Exercise 3"
    **(a) ATM volatility level**: $v_0$ (the initial variance) primarily determines the current ATM implied volatility. At short maturities, ATM implied vol $\approx \sqrt{v_0}$. The long-term level $\theta$ also affects ATM volatility for longer maturities (ATM vol tends toward $\sqrt{\theta}$ as $T \to \infty$).

    **(b) Skew**: $\rho$ (correlation) controls the skew of the implied volatility smile. Negative $\rho$ produces a downward-sloping skew (higher implied vol for low strikes, lower for high strikes), which is typical for equity markets. The more negative $\rho$ is, the steeper the skew.

    **(c) Smile convexity (curvature)**: $\xi$ (vol-of-vol) controls the convexity or curvature of the smile. Larger $\xi$ means more randomness in the variance, which increases the probability of extreme variance realizations. This fattens both tails of the return distribution, producing a more pronounced smile (higher implied vol for both deep OTM puts and deep OTM calls). When $\xi = 0$, the variance is deterministic, and the smile disappears.

    **(d) Term structure**: $\kappa$ (mean-reversion speed) and $\theta$ (long-run variance) jointly determine the term structure. $\kappa$ controls how quickly the variance reverts to $\theta$. A high $\kappa$ means the smile flattens rapidly with maturity (fast mean reversion erases the effect of $v_0 \neq \theta$). A low $\kappa$ means the smile shape persists across maturities. $\theta$ sets the level to which the term structure converges for long maturities.

---


**Exercise 4.** Explain why stochastic volatility models lead to incomplete markets. Specifically, identify the two sources of randomness and the single traded asset. What is the volatility risk premium $\lambda(t, v_t)$, and why is it not determined by no-arbitrage alone? Describe how calibration to option prices implicitly selects a specific risk-neutral measure.

??? success "Solution to Exercise 4"
    **Sources of randomness**: The Heston model has two Brownian motions, $W^{(1)}$ (driving the stock) and $W^{(2)}$ (driving the variance). These represent two independent sources of risk.

    **Traded asset**: Only the stock $S$ (and the risk-free bond) is traded. There is no traded instrument that directly tracks the variance process.

    **Why the market is incomplete**: To form a risk-free portfolio, one needs to hedge both sources of randomness. With one risky asset, one can construct a portfolio $\Pi = V - \Delta S$ and choose $\Delta = \partial V/\partial S$ to eliminate the $dW^{(1)}$ risk. However, the residual exposure to $dW^{(2)}$ (variance risk) remains unhedged. Since we cannot trade the variance directly, this risk cannot be eliminated, and perfect replication of arbitrary claims is impossible.

    **Volatility risk premium**: Under the physical measure $\mathbb{P}$, the variance dynamics are

    $$
    dv_t = [\kappa(\theta - v_t) - \lambda(t, v_t)]\,dt + \xi\sqrt{v_t}\,dW_t^{(2),\mathbb{P}}
    $$

    The function $\lambda(t, v_t)$ is the market price of volatility risk. It represents the compensation investors require for bearing variance risk. Since variance risk cannot be hedged, no-arbitrage alone does not determine $\lambda$; it is a free function.

    **Calibration selects a measure**: When we calibrate the Heston model to market option prices, we determine the $\mathbb{Q}$-drift $\kappa(\theta - v_t)$. This implicitly fixes $\lambda$ through the relationship between $\mathbb{P}$ and $\mathbb{Q}$ dynamics. Different option price datasets (or different calibration objectives) can lead to different $\lambda$ functions, corresponding to different equivalent martingale measures. Each such measure is consistent with no-arbitrage but produces potentially different prices for non-vanilla derivatives.

---


**Exercise 5.** Compare local volatility and stochastic volatility models by filling in a comparison table covering: (a) number of risk factors, (b) market completeness, (c) quality of smile fit, (d) forward smile behavior, (e) calibration stability, and (f) hedging performance. Explain why the forward smile behavior is a critical distinguishing factor for pricing exotic options.

??? success "Solution to Exercise 5"
    | Aspect | Local Volatility | Stochastic Volatility |
    |--------|-----------------|----------------------|
    | **(a) Risk factors** | 1 (single Brownian motion) | 2 (stock + variance Brownian motions) |
    | **(b) Market completeness** | Complete (unique EMM) | Incomplete (multiple EMMs) |
    | **(c) Quality of smile fit** | Exact (by construction via Dupire) | Approximate (depends on calibration) |
    | **(d) Forward smile** | Flattens (sticky strike) | Persists (closer to sticky delta) |
    | **(e) Calibration stability** | Unstable (sensitive to input noise) | More stable (parametric, fewer degrees of freedom) |
    | **(f) Hedging performance** | Poor (smile dynamics are wrong) | Better (more realistic dynamics) |

    **Why forward smile behavior is critical for exotics**: Many exotic derivatives have payoffs that depend on the future implied volatility surface, not just the current one. For example:

    - **Forward-starting options**: The strike is set at a future date as a fraction of the then-prevailing spot. The price depends on the smile at that future date.
    - **Cliquets**: A sequence of forward-starting options with periodic resets. Their value depends on the smile at each reset date.
    - **Barrier options**: The probability of hitting a barrier depends on the distribution of paths, which is influenced by how volatility evolves as the spot moves.

    Local volatility predicts that the forward smile flattens, so it underprices options whose value increases with forward smile richness (like cliquets). Stochastic volatility preserves the forward smile because the future variance is random: there is always uncertainty about future volatility, maintaining the smile's shape. This makes stochastic volatility more reliable for exotic pricing, even though its vanilla fit may be slightly less precise.

---


**Exercise 6.** Write pseudocode for an Euler discretization of the Heston model. Generate correlated Brownian increments $dW_1$ and $dW_2$ from independent standard normals. Discuss the issue of negative variance and compare the truncation scheme $v_{i+1} = \max(v_{i+1}, 0)$ with the reflection scheme $v_{i+1} = |v_{i+1}|$. Which scheme introduces less bias?

??? success "Solution to Exercise 6"
    **Pseudocode for Euler discretization of the Heston model**:

    ```
    Input: S0, v0, r, kappa, theta, xi, rho, T, N_steps, N_paths
    dt = T / N_steps

    For each path p = 1 to N_paths:
        S[0] = S0
        v[0] = v0

        For i = 0 to N_steps - 1:
            # Generate independent standard normals
            Z1 = standard_normal()
            Z2 = standard_normal()

            # Create correlated Brownian increments
            dW1 = sqrt(dt) * Z1
            dW2 = sqrt(dt) * (rho * Z1 + sqrt(1 - rho^2) * Z2)

            # Update variance (Euler step)
            v_temp = v[i] + kappa * (theta - v[i]) * dt + xi * sqrt(v[i]) * dW2

            # Apply truncation or reflection (see below)
            v[i+1] = max(v_temp, 0)        # Truncation
            # OR: v[i+1] = abs(v_temp)      # Reflection

            # Update stock price (log-Euler step)
            S[i+1] = S[i] * exp((r - 0.5 * v[i]) * dt + sqrt(v[i]) * dW1)

    Output: S[N_steps] for each path
    ```

    Note that $dW_2 = \rho\,dW_1 + \sqrt{1-\rho^2}\sqrt{dt}\,Z_2$ ensures $\text{Corr}(dW_1, dW_2) = \rho$.

    **The negative variance issue**: The Euler scheme can produce $v_{i+1} < 0$ because the discrete update $v[i] + \kappa(\theta - v[i])dt + \xi\sqrt{v[i]}dW_2$ can be negative when $dW_2$ is sufficiently negative. This occurs more frequently when $\xi$ is large relative to $\kappa\theta$ (i.e., the Feller condition is violated or barely satisfied) and when $v[i]$ is close to zero.

    **Truncation** ($v_{i+1} = \max(v_{i+1}, 0)$): Sets negative variance to zero. This introduces a positive bias because it replaces negative values with zero instead of their true (positive) reflected values. The process "sticks" at zero momentarily, reducing the average variance and underestimating volatility.

    **Reflection** ($v_{i+1} = |v_{i+1}|$): Reflects negative variance to its absolute value. This is motivated by the continuous-time behavior where the CIR process reflects at zero. The reflected value $|v_{i+1}|$ is symmetric about zero, which better approximates the reflecting boundary condition.

    **Which introduces less bias?** The reflection scheme generally introduces less bias than truncation. The reason is that the true CIR process, when it approaches zero, is reflected by the positive drift $\kappa\theta > 0$. Reflection at zero in the discrete scheme mimics this behavior more faithfully. Truncation systematically underestimates the variance because it maps all negative values to zero rather than to their positive reflected counterparts. Empirical studies (e.g., Lord, Koekkoek, and Van Dijk, 2010) confirm that reflection produces smaller bias in option prices. However, both schemes have $O(\sqrt{dt})$ weak convergence, and more sophisticated schemes (e.g., the QE scheme of Andersen, 2008) achieve better accuracy by using moment-matched approximations near zero.
