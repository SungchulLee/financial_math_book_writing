# Rough Volatility (Overview)


Empirical evidence suggests that volatility exhibits **rough behavior**, with paths much less smooth than classical diffusion models predict. **Rough volatility models** address this by incorporating fractional dynamics.

---

## Empirical motivation


High-frequency data show that:
- volatility has very low Hölder regularity,
- volatility increments are highly persistent,
- classical diffusions are too smooth.

This motivates models driven by fractional Brownian motion.

---

## Basic rough volatility idea


A prototypical rough volatility model takes the form

\[
\sigma_t = \sigma_0 + \int_0^t K(t-s)\,dW_s,
\]


where the kernel \(K\) behaves like

\[
K(t) \sim t^{H-\frac12}, \quad H \in (0,\tfrac12).
\]



Small Hurst parameter \(H\) implies rough paths.

---

## Consequences for option pricing


Rough volatility models naturally explain:
- steep short-maturity smiles,
- fast decay of ATM skew,
- empirical scaling laws.

These features are difficult to reproduce with classical stochastic volatility.

---

## Practical challenges


- non-Markovian dynamics,
- higher computational cost,
- calibration complexity,
- limited closed-form pricing results.

As a result, rough volatility is often used in simplified or approximated form.

---

## Key takeaways


- Volatility is empirically rough.
- Rough models improve short-maturity behavior.
- Practical use requires approximation or dimension reduction.

---

## Further reading


- Gatheral, Jaisson & Rosenbaum, *Volatility is Rough*.
- Bayer, Friz & Gatheral, rough volatility surveys.

---

## Exercises

**Exercise 1.** The fractional kernel $K(t) = t^{H-1/2}$ with $H = 0.1$ controls the roughness of the volatility process. Compute $K(t)$ at $t = 0.01, 0.1, 1.0, 10.0$ and compare with the exponential kernel $K_{\text{exp}}(t) = e^{-\kappa t}$ with $\kappa = 2$. Which kernel decays faster at short time scales? At long time scales? How does this difference affect the autocorrelation structure of volatility increments?

??? success "Solution to Exercise 1"
    **Fractional kernel** $K(t) = t^{H-1/2} = t^{-0.4}$ for $H = 0.1$:

    | $t$ | $K(t) = t^{-0.4}$ | $K_{\text{exp}}(t) = e^{-2t}$ |
    |-----|-------------------|-------------------------------|
    | 0.01 | $0.01^{-0.4} \approx 6.310$ | $e^{-0.02} \approx 0.980$ |
    | 0.1 | $0.1^{-0.4} \approx 2.512$ | $e^{-0.2} \approx 0.819$ |
    | 1.0 | $1.0^{-0.4} = 1.000$ | $e^{-2} \approx 0.135$ |
    | 10.0 | $10.0^{-0.4} \approx 0.398$ | $e^{-20} \approx 2.1 \times 10^{-9}$ |

    **Short time scales.** The fractional kernel diverges as $t \to 0$ (since $-0.4 < 0$), while the exponential kernel stays near 1. The fractional kernel is much larger at short lags, meaning recent volatility shocks have a disproportionately strong influence on the current level. This creates the "rough" behavior.

    **Long time scales.** The exponential kernel decays exponentially fast, becoming negligible by $t = 10$. The fractional kernel decays as a power law ($t^{-0.4}$), remaining significant even at very long lags. At $t = 10$, the fractional kernel is still $0.398$, whereas the exponential kernel is essentially zero.

    **Autocorrelation structure.** The power-law decay of the fractional kernel produces long memory in volatility: volatility increments over short horizons are highly correlated, and the autocorrelation function of absolute returns decays slowly. The exponential kernel produces short memory with a single decorrelation time $1/\kappa = 0.5$ years. Empirically, realized volatility exhibits power-law autocorrelation decay, supporting the fractional kernel.

---

**Exercise 2.** In the rough Bergomi model, the log-variance is given by

$$
\log V_t = \log V_0 + \eta\int_0^t (t-s)^{H-1/2}\,dW_s - \frac{\eta^2}{2}t^{2H}
$$

For $H = 0.1$, compute the variance of $\log V_t$ at $t = 1/252$ (one day), $t = 1/12$ (one month), and $t = 1$ (one year). How does the scaling $\text{Var}[\log V_t] = \eta^2 t^{2H}/(2H)$ differ from the classical diffusion scaling $\text{Var} \propto t$?

??? success "Solution to Exercise 2"
    The variance of $\log V_t$ in the rough Bergomi model is:

    $$
    \text{Var}[\log V_t] = \eta^2 \int_0^t (t-s)^{2H-1}\,ds = \eta^2 \frac{t^{2H}}{2H}
    $$

    For $H = 0.1$, $2H = 0.2$:

    $$
    \text{Var}[\log V_t] = \frac{\eta^2\,t^{0.2}}{0.2} = 5\eta^2\,t^{0.2}
    $$

    Computing at the three horizons (with $\eta$ as a free parameter):

    | Horizon | $t$ | $t^{0.2}$ | $\text{Var}[\log V_t]$ |
    |---------|-----|-----------|----------------------|
    | 1 day | $1/252 \approx 0.00397$ | $0.00397^{0.2} \approx 0.330$ | $1.65\,\eta^2$ |
    | 1 month | $1/12 \approx 0.0833$ | $0.0833^{0.2} \approx 0.603$ | $3.01\,\eta^2$ |
    | 1 year | $1.0$ | $1.0$ | $5.00\,\eta^2$ |

    **Comparison with classical scaling.** In a classical diffusion, $\text{Var} \propto t$, so the ratio of 1-day to 1-year variance is $1/252 \approx 0.004$. In the rough model, this ratio is $0.330 / 1.0 = 0.330$.

    The rough model produces variance at the daily horizon that is $0.330 / 0.004 \approx 83$ times larger relative to the annual variance than a classical model would predict. This means volatility fluctuates much more at short horizons than classical models suggest, which is precisely the empirical observation that motivates rough volatility. The sublinear scaling $t^{0.2}$ (instead of $t^1$) concentrates variability at short time scales.

---

**Exercise 3.** The ATM implied volatility skew in rough volatility models scales as $T^{H-1/2}$ for short maturities, versus $T^{-1/2}$ in classical models. For $H = 0.1$, compute the ratio of 1-week to 1-year skew under both scaling laws. Which model produces steeper short-maturity skews? This is one of the key empirical signatures of rough volatility.

??? success "Solution to Exercise 3"
    **Rough model skew scaling:** $\text{Skew}(T) \propto T^{H-1/2} = T^{-0.4}$ for $H = 0.1$.

    **Classical model skew scaling:** $\text{Skew}(T) \propto T^{-1/2} = T^{-0.5}$.

    Let $T_{\text{week}} = 1/52$ and $T_{\text{year}} = 1$.

    **Rough model ratio:**

    $$
    \frac{\text{Skew}(T_{\text{week}})}{\text{Skew}(T_{\text{year}})} = \frac{(1/52)^{-0.4}}{1^{-0.4}} = 52^{0.4}
    $$

    $$
    52^{0.4} = e^{0.4 \ln 52} = e^{0.4 \times 3.951} = e^{1.580} \approx 4.86
    $$

    **Classical model ratio:**

    $$
    \frac{\text{Skew}(T_{\text{week}})}{\text{Skew}(T_{\text{year}})} = 52^{0.5} = \sqrt{52} \approx 7.21
    $$

    **Interpretation.** The classical model predicts a 1-week skew that is $7.21$ times the 1-year skew, while the rough model predicts a ratio of $4.86$. At first glance, it appears the classical model produces a steeper short-maturity skew.

    However, the key distinction is the **absolute level**: the rough model exponent $H - 1/2 = -0.4$ is closer to zero than the classical $-0.5$, meaning the skew decays more slowly with maturity. The rough model produces steeper absolute skew at short maturities because the prefactor is calibrated to match the overall skew level, and the slower power-law decay then implies higher skew at all short maturities.

    Empirically, the ATM skew for equity index options blows up at short maturities roughly as $T^{-0.4}$, which is precisely the rough volatility prediction with $H \approx 0.1$. Classical models with $T^{-0.5}$ scaling overestimate the rate of skew explosion, making them inconsistent with observed data.

---

**Exercise 4.** Rough volatility models are non-Markovian because $V_t$ depends on the entire past of the driving Brownian motion. Explain why this makes Monte Carlo simulation more expensive than for Markovian models like Heston. Specifically, if a Heston simulation with $n$ time steps costs $O(n)$, what is the cost of a naive rough volatility simulation, and why?

??? success "Solution to Exercise 4"
    **Markovian simulation cost.** In a Heston model, the state at time $t_{j+1}$ depends only on the state at $t_j$ (Markov property). Generating a path with $n$ time steps requires $O(n)$ operations: at each step, sample two correlated Gaussians and update $(S, V)$.

    **Rough volatility simulation cost.** In a rough volatility model, the variance at time $t_j$ depends on the entire history of the driving Brownian motion:

    $$
    V_{t_j} = V_0 + \int_0^{t_j} K(t_j - s)\,dW_s
    $$

    To compute $V_{t_j}$ exactly, one must evaluate the integral over all past increments $dW_s$ for $s \in [0, t_j]$. At the $j$-th time step, this requires summing contributions from all $j$ previous Brownian increments, each weighted by $K(t_j - t_k)$. So computing $V_{t_j}$ costs $O(j)$ operations.

    The total cost over all $n$ time steps is:

    $$
    \sum_{j=1}^n O(j) = O(n^2)
    $$

    This quadratic cost (versus linear for Heston) makes naive Monte Carlo simulation of rough volatility models significantly more expensive. For $n = 1000$ time steps, the rough model is roughly 1000 times slower.

    **Mitigation strategies** include:

    - Markovian approximations (multi-factor lifts) that reduce cost to $O(n)$ with a larger state space
    - Hybrid simulation schemes that use exact formulas for short-range contributions
    - The "Cholesky" approach that pre-computes the covariance matrix of $(V_{t_1}, \ldots, V_{t_n})$ in $O(n^2)$ but can reuse it across paths

---

**Exercise 5.** Empirical evidence suggests that the Hurst parameter for equity index volatility is approximately $H \approx 0.1$, far below the Markovian value $H = 0.5$. Explain what $H < 0.5$ means in terms of path regularity: are paths smoother or rougher than Brownian motion? What empirical test would you use to estimate $H$ from a time series of realized volatility?

??? success "Solution to Exercise 5"
    **Path regularity and $H$.** The Hurst parameter $H$ controls the Holder regularity of the process. A process driven by the fractional kernel $t^{H-1/2}$ has sample paths that are Holder continuous of order slightly less than $H$:

    - $H = 0.5$: Brownian-type regularity (standard diffusion), paths are Holder-$\alpha$ for $\alpha < 0.5$
    - $H < 0.5$: **Rougher** than Brownian motion, paths are Holder-$\alpha$ for $\alpha < H$
    - $H > 0.5$: Smoother than Brownian motion

    With $H \approx 0.1$, volatility paths are much rougher than Brownian motion. They are Holder continuous of order barely above $0.1$, meaning they exhibit rapid, jagged fluctuations at all time scales. Visually, rough volatility paths look much more irregular than classical CIR or GBM volatility paths.

    **Estimating $H$ from data.** The standard empirical approach uses the **scaling of $m$-th order moments of increments.** For a time series of realized volatility $\hat{\sigma}_t$ sampled at interval $\Delta$:

    1. Compute increments $|\hat{\sigma}_{t+q\Delta} - \hat{\sigma}_t|$ for various lags $q$
    2. Estimate $\mathbb{E}[|\hat{\sigma}_{t+q\Delta} - \hat{\sigma}_t|^m] \propto (q\Delta)^{mH}$ for each $q$
    3. Plot $\log \mathbb{E}[|\Delta_q \hat{\sigma}|^m]$ versus $\log q$ and extract the slope $mH$

    Using $m = 2$ (variogram method): the slope of $\log \mathbb{E}[(\Delta_q\hat{\sigma})^2]$ versus $\log q$ gives $2H$.

    Gatheral, Jaisson, and Rosenbaum (2018) applied this method to realized variance data and consistently found $H \approx 0.1$ across equity indices, confirming the rough volatility hypothesis.

---

**Exercise 6.** A practitioner considers using a rough volatility model for pricing 1-week options and a Heston model for 1-year options. Discuss whether this "hybrid" approach is internally consistent. What problems might arise at intermediate maturities? Would a multi-factor model with fast and slow components be a better compromise?

??? success "Solution to Exercise 6"
    **Internal consistency issues.** Using a rough volatility model for 1-week options and a Heston model for 1-year options creates a fundamental inconsistency: the two models describe different volatility dynamics, so they imply contradictory joint distributions for the underlying.

    **Specific problems at intermediate maturities:**

    - At 1-3 month maturities, which model applies? Any cutoff is arbitrary and creates discontinuities in the implied volatility surface.
    - The two models imply different hedging strategies. A delta-hedged portfolio using rough vol deltas for short-dated and Heston deltas for long-dated options will have unexplained P&L at intermediate maturities.
    - Calendar spread prices require a consistent model across maturities. Pricing a spread between a 1-week and a 1-year option under two different models can produce arbitrage.
    - Risk management requires consistent Greeks across the book. Vega exposure computed under rough vol and Heston will not aggregate coherently.

    **Multi-factor model as a compromise.** A multi-factor model with fast and slow mean-reverting components (e.g., two-factor Heston) provides a single, internally consistent framework that captures both time scales:

    - The fast factor ($\kappa \sim 5{-}10$) generates steep short-maturity skew, mimicking the rough volatility behavior at weekly horizons
    - The slow factor ($\kappa \sim 0.5$) captures the persistent, slowly evolving long-term volatility structure

    While a finite-factor Markovian model cannot exactly reproduce the power-law behavior of rough volatility (which requires infinitely many factors in principle), a well-calibrated 2-3 factor model can closely approximate the surface across all maturities. It maintains full internal consistency, allows coherent hedging, and avoids the computational burden of non-Markovian simulation. This makes multi-factor models an attractive practical compromise between rough volatility realism and Markovian tractability.
