# Jump-Diffusion Models

Jump-diffusion models augment the continuous diffusion of Black-Scholes with **discontinuous jumps**, capturing sudden large moves in asset prices. This produces heavy tails, short-maturity smiles, and more realistic risk profiles for extreme events.

---

## Motivation

### Limitations of Pure Diffusion

1. **No sudden moves**: Diffusions have continuous paths
2. **Short-maturity smile**: Black-Scholes produces flat smile for $T \to 0$
3. **Heavy tails**: Market returns have fatter tails than log-normal
4. **Crash risk**: Large instantaneous drops are impossible in pure diffusion

### Evidence for Jumps

- Flash crashes, earnings announcements, geopolitical events
- Implied volatility smiles steepen dramatically at short maturities
- Option prices imply non-zero probability of large moves

---

## Merton's Jump-Diffusion Model

Recall (see [§ Jump-Diffusion SDE](../merton_jump_diffusion/jump_diffusion_sde.md)): under $\mathbb{Q}$,

$$
\frac{dS_t}{S_{t^-}} = (r - \lambda\kappa)\,dt + \sigma\,dW_t + dJ_t,\qquad \log Y \sim N(\mu_J, \sigma_J^2),\quad \kappa = e^{\mu_J + \sigma_J^2/2} - 1,
$$

where $J_t$ is a compound Poisson process with intensity $\lambda$ and the compensator $-\lambda\kappa$ enforces the martingale condition $\mathbb{E}^{\mathbb{Q}}[dS_t/S_{t^-}] = r\,dt$.

---

## The PIDE and Merton's Series Formula

Recall (see [§ Finite Difference PIDE](../merton_jump_diffusion/finite_difference_pide.md)): the option price satisfies a partial integro-differential equation with a non-local integral term $\lambda\int [V(t,Sy)-V(t,S)]\,\nu(dy)$ added to the Black-Scholes operator.

Recall (see [§ Merton Series Formula](../merton_jump_diffusion/merton_series_formula.md)): for European payoffs,

$$
C_{\text{Merton}} = \sum_{n=0}^\infty \frac{e^{-\lambda'T}(\lambda'T)^n}{n!}\, C_{\text{BS}}(S, K, T, r_n, \sigma_n),
$$

a Poisson-weighted sum of Black-Scholes prices over the number of jumps in $[0,T]$.

---

## Kou's Double-Exponential Model

### Motivation

Log-normal jumps in Merton don't produce enough skew. Asymmetric jumps work better.

### Jump Distribution

$$
f_Y(y) = p \cdot \eta_1 e^{-\eta_1 y}\mathbf{1}_{y>0} + (1-p) \cdot \eta_2 e^{\eta_2 y}\mathbf{1}_{y<0}
$$

- $p$: Probability of upward jump
- $\eta_1 > 1$: Rate of upward jump decay
- $\eta_2 > 0$: Rate of downward jump decay

### Advantages

- Asymmetric jumps capture skew
- Memoryless property enables analytical tractability
- Better fit to equity index options

---

## Calibration

### Parameters

| Parameter | Effect |
|-----------|--------|
| $\sigma$ | ATM volatility (continuous part) |
| $\lambda$ | Overall smile level |
| $\mu_J$ | Skew (asymmetry) |
| $\sigma_J$ | Smile convexity |

### Challenges

1. **Separation of $\sigma$ and $\lambda$**: Both affect total variance
2. **Term structure**: Jumps dominate short maturities, diffusion dominates long
3. **Stability**: Many local minima in optimization

### Typical Approach

1. Fit short-maturity smile to get jump parameters
2. Fit long-maturity level to get $\sigma$
3. Refine jointly

---

## Incomplete Markets

Recall (see [§ Incomplete Market and Measure Choice](../merton_jump_diffusion/incomplete_market_and_measure_choice.md) and [§ Incomplete Markets and Pricing Bounds](incomplete_markets_and_pricing_bounds.md)): jump risk is unhedgeable with the underlying alone, the risk-neutral jump intensity $\lambda^{\mathbb{Q}}$ and size distribution $\nu^{\mathbb{Q}}$ are not pinned down by no-arbitrage, and calibration to option quotes implicitly selects a particular $\mathbb{Q}$.

---

## Numerical Methods and Greeks

For the characteristic function and FFT pricing, recall (see [§ Characteristic Function](../merton_jump_diffusion/characteristic_function.md)). For PIDE discretization, recall (see [§ Finite Difference PIDE](../merton_jump_diffusion/finite_difference_pide.md)). For path simulation, recall (see [§ Monte Carlo Simulation](../merton_jump_diffusion/monte_carlo_simulation.md)). Greek decomposition (delta, gamma, and a vega that splits into diffusion and jump components) is covered in [§ Greeks under Jump Diffusion](../merton_jump_diffusion/greeks_under_jump_diffusion.md).

---

## Extensions

### Stochastic Volatility + Jumps (SVJ)

Combine Heston with Merton:

$$
\begin{aligned}
dS_t &= (r - \lambda\kappa)S_t\,dt + \sqrt{v_t}S_t\,dW_t^{(1)} + S_t\,dJ_t \\
dv_t &= \kappa(\theta - v_t)\,dt + \xi\sqrt{v_t}\,dW_t^{(2)}
\end{aligned}
$$

### Jumps in Volatility

Some models include jumps in the variance process as well (SVJJ models).

### Lévy Processes

Generalize to infinite-activity jump processes (Variance Gamma, CGMY, NIG).

---

## Summary

$$
\boxed{
\frac{dS_t}{S_{t^-}} = (r - \lambda\kappa)\,dt + \sigma\,dW_t + dJ_t
}
$$

| Feature | Description |
|---------|-------------|
| **Jump process** | Compound Poisson with intensity $\lambda$ |
| **Jump size** | Log-normal (Merton) or double-exponential (Kou) |
| **Pricing** | PIDE with integral term |
| **Short-maturity smile** | Captured naturally |
| **Hedging** | Incomplete—jump risk unhedgeable with stock alone |

$$
\boxed{
C_{\text{Merton}} = \sum_{n=0}^\infty \frac{e^{-\lambda'T}(\lambda'T)^n}{n!} C_{\text{BS}}(S, K, T, r_n, \sigma_n)
}
$$

**Jump-diffusion models capture sudden large moves and short-maturity smiles that pure diffusion models cannot, at the cost of market incompleteness and more complex pricing equations.**

---

## Exercises

**Exercise 1.** In Merton's jump-diffusion model, the drift adjustment term is $-\lambda\kappa$ where $\kappa = e^{\mu_J + \sigma_J^2/2} - 1$. (a) Show that this adjustment ensures $\mathbb{E}^{\mathbb{Q}}[dS_t/S_{t^-}] = r\,dt$. (b) For $\lambda = 1$, $\mu_J = -0.05$, $\sigma_J = 0.10$, compute $\kappa$ and the compensated drift $r - \lambda\kappa$ when $r = 0.05$.

??? success "Solution to Exercise 1"
    **(a)** Under $\mathbb{Q}$, the stock dynamics are

    $$
    \frac{dS_t}{S_{t^-}} = (r - \lambda\kappa)\,dt + \sigma\,dW_t + dJ_t
    $$

    Taking expectations under $\mathbb{Q}$:

    $$
    \mathbb{E}^{\mathbb{Q}}\left[\frac{dS_t}{S_{t^-}}\right] = (r - \lambda\kappa)\,dt + 0 + \lambda\kappa\,dt = r\,dt
    $$

    The Brownian motion term has zero expectation. The compound Poisson process $J_t$ has expected increment $\lambda \mathbb{E}[Y-1]\,dt = \lambda\kappa\,dt$ (where $\kappa = \mathbb{E}[Y-1]$ and $\lambda$ is the jump intensity). The compensating drift $-\lambda\kappa$ exactly cancels the expected jump contribution, yielding $\mathbb{E}^{\mathbb{Q}}[dS_t/S_{t^-}] = r\,dt$ as required for the discounted price process to be a martingale.

    **(b)** With $\mu_J = -0.05$ and $\sigma_J = 0.10$:

    $$
    \kappa = e^{\mu_J + \sigma_J^2/2} - 1 = e^{-0.05 + 0.005} - 1 = e^{-0.045} - 1 \approx 0.9560 - 1 = -0.0440
    $$

    The compensated drift with $r = 0.05$ and $\lambda = 1$:

    $$
    r - \lambda\kappa = 0.05 - 1 \times (-0.0440) = 0.05 + 0.0440 = 0.0940
    $$

    The drift is higher than $r$ because the negative expected jump ($\kappa < 0$) must be compensated by a higher continuous drift to ensure the overall expected return equals $r$.

---


**Exercise 2.** Merton's formula expresses the option price as a Poisson-weighted sum of Black-Scholes prices: $C = \sum_{n=0}^{\infty} \frac{e^{-\lambda'T}(\lambda'T)^n}{n!} C_{\text{BS}}(S, K, T, r_n, \sigma_n)$. (a) Interpret this formula: conditioning on $n$ jumps, what is the effective volatility and risk-free rate? (b) In practice, how many terms of the series are needed for convergence? Estimate for $\lambda' T = 3$. (c) Why does this formula not extend to path-dependent options?

??? success "Solution to Exercise 2"
    **(a)** Conditioning on exactly $n$ jumps occurring during $[0, T]$, the total variance of the log-price is

    $$
    \sigma_n^2 T = \sigma^2 T + n\sigma_J^2
    $$

    so the effective volatility is $\sigma_n = \sqrt{\sigma^2 + n\sigma_J^2/T}$, which increases with the number of jumps. The effective risk-free rate is

    $$
    r_n = r - \lambda\kappa + \frac{n(\mu_J + \sigma_J^2/2)}{T}
    $$

    This adjusts the drift to account for the conditional mean of the $n$ jumps. Each term in the sum is exactly the Black-Scholes price for a world where $n$ jumps have occurred, with the appropriately adjusted volatility and rate.

    **(b)** The Poisson weights $w_n = e^{-\lambda'T}(\lambda'T)^n / n!$ decay rapidly. The sum of the first $N$ weights satisfies $\sum_{n=0}^{N} w_n \approx 1$ once $N$ is sufficiently large. For $\lambda'T = 3$, the Poisson distribution has mean 3 and standard deviation $\sqrt{3} \approx 1.73$. By $n = 10$, the cumulative probability exceeds 0.9997. In practice, $N = 10$ to $15$ terms suffice for machine precision convergence, as $w_{10} = e^{-3} \cdot 3^{10}/10! \approx 0.0008$ is already negligible.

    **(c)** Merton's formula relies on conditioning on the number of jumps and then computing the expectation of a European payoff with Gaussian log-returns. For path-dependent options (barriers, lookbacks, Asians), the payoff depends on the entire trajectory $\{S_t : 0 \leq t \leq T\}$, not just the terminal value $S_T$. Knowing the number of jumps does not reduce the path-dependent problem to a Black-Scholes problem because the timing and ordering of jumps along the path matters. Therefore, path-dependent options require Monte Carlo simulation or PIDE methods.

---


**Exercise 3.** Compare the PIDE for jump-diffusion pricing with the standard Black-Scholes PDE. Identify the additional integral term and explain its financial interpretation as the expected change in option value due to jumps. Why does this integral term make the equation non-local?

??? success "Solution to Exercise 3"
    The Black-Scholes PDE is

    $$
    \frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2\frac{\partial^2 V}{\partial S^2} + rS\frac{\partial V}{\partial S} - rV = 0
    $$

    The PIDE for jump-diffusion pricing adds an integral term:

    $$
    \frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2\frac{\partial^2 V}{\partial S^2} + (r - \lambda\kappa)S\frac{\partial V}{\partial S} - rV + \lambda\int_0^\infty [V(t, Sy) - V(t, S)]\nu(dy) = 0
    $$

    The additional integral term $\lambda\int_0^\infty [V(t, Sy) - V(t, S)]\nu(dy)$ represents the expected change in the option value when a jump occurs. Here $\nu(dy)$ is the distribution of the jump multiplier $Y$. The quantity $V(t, Sy) - V(t, S)$ is the change in option value if the stock jumps from $S$ to $Sy$, and the integral averages this over all possible jump sizes weighted by $\nu(dy)$, multiplied by the jump intensity $\lambda$.

    This integral term makes the equation **non-local** because the value of $V$ at point $S$ depends on the values of $V$ at all other points $Sy$ (for every possible jump size $y$). In the standard Black-Scholes PDE, the equation at each point involves only local information (derivatives at that point). The jump integral requires knowledge of $V$ across the entire spatial domain simultaneously, which is why it is called an integro-differential equation and why standard finite difference methods must be augmented with quadrature for the integral.

---


**Exercise 4.** The Kou double-exponential model uses asymmetric jump sizes: upward jumps with parameter $\eta_1$ and downward jumps with parameter $\eta_2$. Explain why this asymmetry is important for fitting equity option markets. How does the ratio $p/(1-p)$ (probability of upward vs. downward jump) affect the implied volatility skew?

??? success "Solution to Exercise 4"
    In equity markets, downward price moves (crashes) tend to be larger and more frequent than upward moves of the same magnitude. The Kou double-exponential model captures this through asymmetric jump parameters:

    - $\eta_1 > 1$ governs the rate of decay for upward jumps (larger $\eta_1$ means smaller upward jumps)
    - $\eta_2 > 0$ governs the rate of decay for downward jumps (smaller $\eta_2$ means larger downward jumps)

    This asymmetry is crucial for fitting equity options because the implied volatility surface exhibits a pronounced **skew**: OTM puts (low strikes) have higher implied volatility than OTM calls (high strikes). This skew reflects the market's assessment that large downward moves are more likely than large upward moves.

    The ratio $p/(1-p)$ controls the relative frequency of upward versus downward jumps. When $p < 0.5$ (more downward jumps), the model produces a steeper negative skew in implied volatility:

    - **Lower $p/(1-p)$** (more downward jumps): Steeper skew, higher OTM put implied volatilities relative to OTM call implied volatilities.
    - **Higher $p/(1-p)$** (more upward jumps): Flatter or positive skew, which may be appropriate for commodity markets where supply shocks cause upward jumps.
    - **$p/(1-p) = 1$** (symmetric jumps): Produces a symmetric smile rather than a skew.

    The combination of asymmetric jump rates ($\eta_1 \neq \eta_2$) and asymmetric probabilities ($p \neq 0.5$) gives the Kou model enough flexibility to match the observed skew across different strikes.

---


**Exercise 5.** Explain why jump-diffusion models lead to incomplete markets. Identify the unhedgeable risk component and describe why delta hedging alone is insufficient. What additional instruments could be used to hedge jump risk, and how does this relate to the non-uniqueness of the risk-neutral measure?

??? success "Solution to Exercise 5"
    Jump-diffusion models lead to incomplete markets because they introduce a source of risk that cannot be hedged with continuous trading in the underlying asset. Specifically:

    **Sources of risk**: The model $dS_t/S_{t^-} = (r - \lambda\kappa)\,dt + \sigma\,dW_t + dJ_t$ has two independent sources of randomness: (1) the Brownian motion $W_t$ (diffusion risk) and (2) the compound Poisson process $J_t$ (jump risk, which includes both the timing and size of jumps).

    **Why delta hedging is insufficient**: Delta hedging constructs a portfolio $\Pi = V - \Delta S$ and chooses $\Delta = \partial V/\partial S$ to eliminate the diffusion risk (the $dW_t$ component). However, when a jump occurs, the stock moves from $S$ to $SY$ instantaneously, and the portfolio value changes by $V(t, SY) - V(t, S) - \Delta(SY - S)$. This jump residual is generally nonzero regardless of the choice of $\Delta$, because a single parameter $\Delta$ cannot simultaneously neutralize both the continuous and discontinuous risks.

    **Additional hedging instruments**: To hedge jump risk, one can trade options on the same underlying. For instance, holding a portfolio of the stock and one option allows matching two risk exposures (diffusion and one aspect of jump risk). More generally, since jump risk involves an entire distribution of possible jump sizes, perfectly hedging all jump risk requires a continuum of traded options. In practice, trading a few liquid options (at different strikes) provides partial jump hedging.

    **Relation to non-uniqueness of $\mathbb{Q}$**: With more risk sources than traded assets, the market price of jump risk is not determined by no-arbitrage. Different choices of the risk-neutral jump intensity $\lambda^{\mathbb{Q}}$ and jump size distribution $\nu^{\mathbb{Q}}$ give different equivalent martingale measures, each consistent with no-arbitrage. Calibration to liquid option prices implicitly selects a particular $\mathbb{Q}$ by fixing $\lambda^{\mathbb{Q}}$ and $\nu^{\mathbb{Q}}$.

---


**Exercise 6.** The SVJ (stochastic volatility plus jumps) model combines Heston dynamics with Merton-style jumps. Write the SDE system for this model and explain which market phenomena each component captures. Why might the SVJ model provide a better fit to the entire implied volatility surface (both short and long maturities) than either Heston or Merton alone?

??? success "Solution to Exercise 6"
    The SVJ model combines Heston stochastic volatility with Merton-style jumps:

    $$
    \begin{aligned}
    dS_t &= (r - \lambda\kappa)S_t\,dt + \sqrt{v_t}S_t\,dW_t^{(1)} + S_t\,dJ_t \\
    dv_t &= \kappa(\theta - v_t)\,dt + \xi\sqrt{v_t}\,dW_t^{(2)}
    \end{aligned}
    $$

    with $\text{Corr}(dW^{(1)}, dW^{(2)}) = \rho$, and $J_t$ is a compound Poisson process with intensity $\lambda$ and log-normal jump sizes $\log Y \sim N(\mu_J, \sigma_J^2)$.

    **Role of each component**:

    - **Stochastic volatility** ($v_t$ process): Captures volatility clustering, mean reversion of volatility, and the leverage effect (via $\rho < 0$). This component is primarily responsible for the **long-maturity** smile and term structure, as the random fluctuation of volatility over long horizons generates a smile that persists over time.
    - **Jump component** ($J_t$): Captures sudden large price moves (crashes, earnings surprises). This component is primarily responsible for the **short-maturity** smile, because at short horizons the probability of a jump creates significant tail risk that produces steep skew and smile.
    - **Diffusion** ($\sigma\,dW^{(1)}$): Provides the baseline continuous price evolution.

    **Why SVJ fits better than either model alone**:

    - **Heston alone**: Produces a good fit to the long-maturity smile but struggles with short-maturity steep skews, because diffusion-based stochastic volatility generates smiles only gradually as $T$ increases.
    - **Merton alone**: Captures short-maturity smiles well (jumps are most impactful at short horizons) but produces a smile that flattens at long maturities (by the CLT, many small jumps average out). It also lacks volatility clustering.
    - **SVJ**: The jumps handle the steep short-maturity skew, while stochastic volatility handles the persistent long-maturity smile. Together, they fit the entire implied volatility surface across both the strike and maturity dimensions.
