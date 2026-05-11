# Two-Factor Diffusion Models

Stochastic volatility models extend Black–Scholes by introducing **additional sources of randomness**. The most common framework is a **two-factor diffusion**, where asset price and volatility evolve jointly as a bivariate Markov process. This section develops the general mathematical structure underlying all major stochastic volatility models.

---

## General Structure

### The Canonical Two-Factor SDE System

A generic two-factor stochastic volatility model takes the form:

$$
\begin{aligned}
dS_t &= \mu(t, S_t, V_t)\,S_t\,dt + \sigma(t, S_t, V_t)\,S_t\,dW_t^S \\
dV_t &= a(t, V_t)\,dt + b(t, V_t)\,dW_t^V
\end{aligned}
$$

where:

- $S_t$ is the asset price
- $V_t$ is the **variance** or **volatility factor** (interpretation varies by model)
- $W^S$, $W^V$ are standard Brownian motions
- $\langle W^S, W^V \rangle_t = \rho t$ for correlation $\rho \in [-1, 1]$

The function $\sigma(t, S_t, V_t)$ links the variance factor to instantaneous volatility. Common specifications:

| Model Type | $\sigma(S, V)$ | Interpretation of $V$ |
|------------|----------------|----------------------|
| Variance models | $\sqrt{V}$ | Instantaneous variance |
| Volatility models | $V$ | Instantaneous volatility |
| General | $\sigma(S, V)$ | Latent factor |

### Correlated Brownian Motions

The correlation can be introduced via:

$$
W_t^V = \rho W_t^S + \sqrt{1-\rho^2} W_t^{\perp}
$$

where $W^S$ and $W^{\perp}$ are independent. This decomposition is useful for simulation and analysis.

Alternatively, use the covariance matrix formulation:

$$
\begin{pmatrix} dW_t^S \\ dW_t^V \end{pmatrix} \sim \mathcal{N}\left(\mathbf{0}, \begin{pmatrix} 1 & \rho \\ \rho & 1 \end{pmatrix} dt\right)
$$

---

## Mathematical Properties

### Markov Property

The pair $(S_t, V_t)$ is a **two-dimensional Markov process**. Given $(S_s, V_s)$, the future evolution $(S_t, V_t)_{t \geq s}$ is independent of the past.

This enables:

- PDE pricing via Kolmogorov equations
- Efficient Monte Carlo simulation
- Characteristic function computation

### Infinitesimal Generator

The generator of the two-factor diffusion is:

$$
\mathcal{L} = \frac{1}{2}\sigma^2 S^2 \frac{\partial^2}{\partial S^2} + \rho \sigma b S \frac{\partial^2}{\partial S \partial V} + \frac{1}{2}b^2 \frac{\partial^2}{\partial V^2} + \mu S \frac{\partial}{\partial S} + a \frac{\partial}{\partial V}
$$

For a function $f(t, S, V)$, Itô's lemma gives:

$$
df = \left(\frac{\partial f}{\partial t} + \mathcal{L}f\right)dt + \frac{\partial f}{\partial S}\sigma S\,dW^S + \frac{\partial f}{\partial V}b\,dW^V
$$

### Risk-Neutral Dynamics

Under the risk-neutral measure $\mathbb{Q}$, the drift of $S$ is constrained by no-arbitrage:

$$
dS_t = (r - q)S_t\,dt + \sigma(t, S_t, V_t)\,S_t\,dW_t^{S,\mathbb{Q}}
$$

The volatility process drift changes via Girsanov:

$$
dV_t = a^{\mathbb{Q}}(t, V_t)\,dt + b(t, V_t)\,dW_t^{V,\mathbb{Q}}
$$

where $a^{\mathbb{Q}} = a - \lambda_V b$ and $\lambda_V$ is the market price of volatility risk.

**Key insight:** The diffusion coefficient $b$ is unchanged by measure change; only the drift $a$ is modified.

---

## Prominent Two-Factor Models

### Heston Model (1993)

The most widely used stochastic volatility model:

$$
\begin{aligned}
dS_t &= (r-q)S_t\,dt + \sqrt{V_t}\,S_t\,dW_t^S \\
dV_t &= \kappa(\theta - V_t)\,dt + \xi\sqrt{V_t}\,dW_t^V
\end{aligned}
$$

**Characteristics:**

- $V_t$ is instantaneous variance (non-negative)
- Square-root (CIR) volatility dynamics
- Mean-reverting to $\theta$
- Affine structure enables semi-closed-form pricing

### Hull–White Model (1987)

Lognormal volatility dynamics:

$$
\begin{aligned}
dS_t &= (r-q)S_t\,dt + V_t S_t\,dW_t^S \\
dV_t &= \mu_V V_t\,dt + \xi V_t\,dW_t^V
\end{aligned}
$$

**Characteristics:**

- $V_t$ is instantaneous volatility
- Geometric Brownian motion for volatility
- No mean reversion (can add it)
- No closed-form characteristic function

### Stein–Stein Model (1991)

Ornstein–Uhlenbeck volatility:

$$
\begin{aligned}
dS_t &= (r-q)S_t\,dt + V_t S_t\,dW_t^S \\
dV_t &= \kappa(\theta - V_t)\,dt + \xi\,dW_t^V
\end{aligned}
$$

**Characteristics:**

- Mean-reverting Gaussian volatility
- Can become negative (problematic)
- Simpler dynamics than Heston
- Affine in $(S, V)$

### 3/2 Model

Power-law volatility dynamics:

$$
\begin{aligned}
dS_t &= (r-q)S_t\,dt + \sqrt{V_t}\,S_t\,dW_t^S \\
dV_t &= \kappa V_t(\theta - V_t)\,dt + \xi V_t^{3/2}\,dW_t^V
\end{aligned}
$$

**Characteristics:**

- Higher volatility of volatility at high $V$
- Heavier tails than Heston
- Can match steep short-maturity smiles
- Semi-closed-form characteristic function

### SABR Model (Hagan et al., 2002)

Stochastic alpha-beta-rho model:

$$
\begin{aligned}
dF_t &= \sigma_t F_t^{\beta}\,dW_t^F \\
d\sigma_t &= \nu \sigma_t\,dW_t^{\sigma}
\end{aligned}
$$

**Characteristics:**

- Forward price dynamics (driftless under forward measure)
- $\beta$ controls backbone (normal vs. lognormal)
- No mean reversion
- Asymptotic implied volatility formula available

---

## Economic Interpretation

### The Volatility Factor

The variance/volatility factor $V_t$ represents:

1. **Market uncertainty:** Time-varying risk perception
2. **Information flow:** Varying intensity of news arrival
3. **Aggregate risk:** Economy-wide risk factors
4. **Latent state:** Unobservable market conditions

### Why Volatility is Stochastic

Several mechanisms generate stochastic volatility:

**Microstructure:** Information asymmetry and order flow create volatility clustering.

**Aggregation:** Individual firm-level shocks aggregate to market volatility.

**Feedback effects:** Volatility affects hedging activity, which affects prices, which affects volatility.

**Regime switching:** Economic regimes (expansion/recession) have different volatility characteristics.

### Incompleteness and Risk Premia

Because $V_t$ is not directly traded:

1. The market is **incomplete**
2. Perfect hedging is impossible
3. **Volatility risk premium** emerges as compensation
4. Different models can fit the same smile with different risk premia

---

## Implications for Option Pricing

Two-factor diffusions imply:

### Non-Gaussian Returns

The unconditional distribution of $\log(S_T/S_0)$ is a **mixture of normals**:

$$
\log(S_T/S_0) \big| \int_0^T V_s\,ds \sim \mathcal{N}\left(\mu T - \frac{1}{2}\int_0^T V_s\,ds, \int_0^T V_s\,ds\right)
$$

Integrating over the distribution of integrated variance yields:

- Heavy tails (excess kurtosis)
- Skewness (if $\rho \neq 0$)

### Volatility Clustering

Mean-reverting $V_t$ produces autocorrelated squared returns:

$$
\text{Corr}(r_t^2, r_{t+\tau}^2) \propto e^{-\kappa \tau}
$$

### Implied Volatility Smile

The smile arises because:

- $\rho < 0$ → negative skew
- $\xi > 0$ → smile curvature (convexity)
- Mean reversion → term structure effects

### Path-Dependent Pricing

Option prices depend on the **joint law** of $(S_T, V_T)$ and the path of $V$. For European options:

$$
C(K, T) = e^{-rT}\mathbb{E}^{\mathbb{Q}}\left[(S_T - K)^+\right]
$$

where the expectation is over the full two-dimensional process.

---

## Comparison of Models

| Model | $V$ dynamics | Mean reversion | Closed-form CF | Positivity |
|-------|-------------|----------------|----------------|------------|
| Heston | CIR | Yes | Yes | Yes* |
| Hull–White | GBM | Optional | No | Yes |
| Stein–Stein | OU | Yes | Yes | No |
| 3/2 | Power | Yes | Yes | Yes |
| SABR | GBM | No | Approximate | Yes |

*Under Feller condition $2\kappa\theta \geq \xi^2$

---

## Key Takeaways

- Two-factor diffusions are the canonical stochastic volatility framework
- They generalize Black–Scholes while remaining Markovian
- The correlation $\rho$ and vol-of-vol $\xi$ control smile shape
- Market incompleteness is intrinsic: volatility risk cannot be hedged
- Multiple models exist with different trade-offs between tractability and realism
- Model choice depends on application: pricing, hedging, calibration

---

## Further Reading

- Heston, S. (1993). *A closed-form solution for options with stochastic volatility with applications to bond and currency options*. Review of Financial Studies.
- Hull, J. & White, A. (1987). *The pricing of options on assets with stochastic volatilities*. Journal of Finance.
- Stein, E. & Stein, J. (1991). *Stock price distributions with stochastic volatility*. Review of Financial Studies.
- Lewis, A. (2000). *Option Valuation under Stochastic Volatility*. Finance Press.
- Fouque, J.-P., Papanicolaou, G., & Sircar, R. (2000). *Derivatives in Financial Markets with Stochastic Volatility*. Cambridge University Press.

---

## Exercises

**Exercise 1.** Consider the general two-factor SDE system with correlated Brownian motions $W^S$ and $W^V$. Using the decomposition $W_t^V = \rho W_t^S + \sqrt{1-\rho^2}\,W_t^{\perp}$, rewrite the variance dynamics $dV_t = a(V_t)\,dt + b(V_t)\,dW_t^V$ in terms of the independent Brownian motions $W^S$ and $W^{\perp}$. Explain why this decomposition is useful for Monte Carlo simulation.

??? success "Solution to Exercise 1"
    Substituting the decomposition $W_t^V = \rho W_t^S + \sqrt{1-\rho^2}\,W_t^{\perp}$ into the variance dynamics gives:

    $$
    dV_t = a(V_t)\,dt + b(V_t)\left(\rho\,dW_t^S + \sqrt{1-\rho^2}\,dW_t^{\perp}\right)
    $$

    Expanding:

    $$
    dV_t = a(V_t)\,dt + \rho\,b(V_t)\,dW_t^S + \sqrt{1-\rho^2}\,b(V_t)\,dW_t^{\perp}
    $$

    The full system in terms of independent Brownian motions $W^S$ and $W^{\perp}$ is:

    $$
    \begin{aligned}
    dS_t &= \mu S_t\,dt + \sigma(V_t) S_t\,dW_t^S \\
    dV_t &= a(V_t)\,dt + \rho\,b(V_t)\,dW_t^S + \sqrt{1-\rho^2}\,b(V_t)\,dW_t^{\perp}
    \end{aligned}
    $$

    This decomposition is useful for Monte Carlo simulation because generating paths requires independent random inputs. At each time step, one draws two independent standard normal variates $Z_1, Z_2$ and sets $\Delta W^S = Z_1\sqrt{\Delta t}$ and $\Delta W^{\perp} = Z_2\sqrt{\Delta t}$. The variance increment then uses $\Delta W^V = \rho\,Z_1\sqrt{\Delta t} + \sqrt{1-\rho^2}\,Z_2\sqrt{\Delta t}$, which automatically embeds the correct correlation structure without requiring a Cholesky decomposition at each step.

---

**Exercise 2.** Write down the infinitesimal generator $\mathcal{L}$ for the Heston model:

$$
\begin{aligned}
dS_t &= (r-q)S_t\,dt + \sqrt{V_t}\,S_t\,dW_t^S \\
dV_t &= \kappa(\theta - V_t)\,dt + \xi\sqrt{V_t}\,dW_t^V
\end{aligned}
$$

by identifying the coefficients $\mu S$, $\sigma S$, $a$, and $b$ in the general formula. Show explicitly how the cross-derivative term involves $\rho$.

??? success "Solution to Exercise 2"
    In the Heston model, the coefficients are:

    - Drift of $S$: $\mu S = (r-q)S$, so $\mu = r - q$
    - Diffusion of $S$: $\sigma S = \sqrt{V}\,S$, so $\sigma = \sqrt{V}$
    - Drift of $V$: $a = \kappa(\theta - V)$
    - Diffusion of $V$: $b = \xi\sqrt{V}$

    Substituting into the general generator formula:

    $$
    \mathcal{L} = \frac{1}{2}\sigma^2 S^2 \frac{\partial^2}{\partial S^2} + \rho\sigma b S \frac{\partial^2}{\partial S \partial V} + \frac{1}{2}b^2 \frac{\partial^2}{\partial V^2} + \mu S \frac{\partial}{\partial S} + a \frac{\partial}{\partial V}
    $$

    we obtain:

    $$
    \mathcal{L} = \frac{1}{2}V S^2 \frac{\partial^2}{\partial S^2} + \rho\xi V S \frac{\partial^2}{\partial S \partial V} + \frac{1}{2}\xi^2 V \frac{\partial^2}{\partial V^2} + (r-q)S \frac{\partial}{\partial S} + \kappa(\theta - V) \frac{\partial}{\partial V}
    $$

    The cross-derivative term $\rho\xi V S \,\partial^2/(\partial S\,\partial V)$ arises from the product $\rho \cdot \sigma \cdot b \cdot S = \rho \cdot \sqrt{V} \cdot \xi\sqrt{V} \cdot S = \rho\xi V S$. This term vanishes when $\rho = 0$, confirming that the cross-derivative encodes the correlation between price and volatility shocks.

---

**Exercise 3.** In the Stein–Stein model, volatility follows an Ornstein–Uhlenbeck process $dV_t = \kappa(\theta - V_t)\,dt + \xi\,dW_t^V$. Explain why $V_t$ can become negative. Compute the probability $\mathbb{P}(V_t < 0)$ for $V_0 = 0.2$, $\theta = 0.2$, $\kappa = 1.5$, $\xi = 0.3$, and $t = 1$ year, using the known Gaussian distribution of the OU process. Why is this problematic for a stochastic volatility model?

??? success "Solution to Exercise 3"
    The Ornstein–Uhlenbeck process has the explicit solution:

    $$
    V_t = V_0 e^{-\kappa t} + \theta(1 - e^{-\kappa t}) + \xi \int_0^t e^{-\kappa(t-s)}\,dW_s^V
    $$

    This is Gaussian with:

    $$
    \mathbb{E}[V_t] = V_0 e^{-\kappa t} + \theta(1 - e^{-\kappa t})
    $$

    $$
    \text{Var}(V_t) = \frac{\xi^2}{2\kappa}(1 - e^{-2\kappa t})
    $$

    For $V_0 = 0.2$, $\theta = 0.2$, $\kappa = 1.5$, $\xi = 0.3$, $t = 1$:

    $$
    \mathbb{E}[V_1] = 0.2 \cdot e^{-1.5} + 0.2(1 - e^{-1.5}) = 0.2
    $$

    $$
    \text{Var}(V_1) = \frac{0.09}{3}(1 - e^{-3}) = 0.03 \times 0.9502 = 0.02851
    $$

    $$
    \text{Std}(V_1) = \sqrt{0.02851} \approx 0.1689
    $$

    Since $V_1 \sim \mathcal{N}(0.2, 0.02851)$:

    $$
    \mathbb{P}(V_1 < 0) = \Phi\!\left(\frac{0 - 0.2}{0.1689}\right) = \Phi(-1.184) \approx 0.118
    $$

    There is approximately an 11.8% probability that volatility is negative after one year. This is problematic because volatility must be non-negative for the model to be economically meaningful. If $V_t$ is used as the diffusion coefficient for $S_t$ (as in $dS_t = \dots + V_t S_t\,dW_t^S$), negative values reverse the sign of the exposure to $dW^S$, creating unphysical dynamics.

---

**Exercise 4.** Under a two-factor stochastic volatility model, the unconditional distribution of $\log(S_T/S_0)$ is a mixture of normals conditional on integrated variance. Specifically,

$$
\log(S_T/S_0) \big| \int_0^T V_s\,ds = I \sim \mathcal{N}\!\left((r-q)T - \tfrac{1}{2}I,\; I\right)
$$

when $\rho = 0$. Show that the unconditional kurtosis of $\log(S_T/S_0)$ exceeds 3 whenever $\text{Var}[\int_0^T V_s\,ds] > 0$. (Hint: use the law of total variance and the formula for kurtosis of a variance-mean mixture of normals.)

??? success "Solution to Exercise 4"
    When $\rho = 0$, the log-return conditional on integrated variance $I = \int_0^T V_s\,ds$ is:

    $$
    X = \log(S_T/S_0) \mid I \sim \mathcal{N}(\mu_I, I)
    $$

    where $\mu_I = (r-q)T - I/2$. Define $m = \mathbb{E}[I]$ and use the law of total variance:

    $$
    \text{Var}(X) = \mathbb{E}[\text{Var}(X|I)] + \text{Var}(\mathbb{E}[X|I]) = \mathbb{E}[I] + \frac{1}{4}\text{Var}(I) = m + \frac{1}{4}\text{Var}(I)
    $$

    For the fourth central moment, we use the variance-mean mixture formula. The kurtosis of a normal distribution is 3, and for a variance mixture of normals the excess kurtosis is:

    $$
    \text{Kurt}(X) = 3 + \frac{3\,\text{Var}(I)}{\left(\text{Var}(X)\right)^2} \cdot \left(1 + \frac{\text{Var}(I)}{4(\text{Var}(X))^2}\right)^{-1} \cdot (\dots)
    $$

    More directly, using the law of total cumulants for a normal with random variance $\sigma^2 = I$ and random mean $\mu_I = (r-q)T - I/2$:

    $$
    \mathbb{E}[X^4_c] = 3(\text{Var}(I))(\text{terms involving } \mathbb{E}[I])
    $$

    The cleanest argument proceeds via the fourth central moment. Let $Y = X - \mathbb{E}[X]$. Then:

    $$
    \mathbb{E}[Y^4] = \mathbb{E}[\mathbb{E}[Y^4|I]] = \mathbb{E}[3I^2 + 6I(\mathbb{E}[X|I] - \mathbb{E}[X])^2 + (\mathbb{E}[X|I] - \mathbb{E}[X])^4]
    $$

    Since $\mathbb{E}[X|I] - \mathbb{E}[X] = -(I - m)/2$ and $\text{Var}(X|I) = I$:

    $$
    \mathbb{E}[Y^4] = 3\mathbb{E}[I^2] + \frac{6}{4}\mathbb{E}[I(I-m)^2] + \frac{1}{16}\mathbb{E}[(I-m)^4]
    $$

    Meanwhile, $(\text{Var}(X))^2 = (m + \text{Var}(I)/4)^2$. For a Gaussian variable, kurtosis equals 3, so:

    $$
    \text{Kurt}(X) = \frac{\mathbb{E}[Y^4]}{(\text{Var}(X))^2} > 3
    $$

    whenever $\text{Var}(I) > 0$. The excess kurtosis arises because the random variance creates heavier tails than any single Gaussian. Intuitively, paths with high integrated variance produce wide return distributions, while paths with low integrated variance produce narrow ones. The mixture of these has fatter tails than either component alone.

---

**Exercise 5.** Compare the Heston and 3/2 models in terms of how volatility of volatility scales with the variance level $V$. In Heston, $b(V) = \xi\sqrt{V}$; in the 3/2 model, $b(V) = \xi V^{3/2}$. Compute the ratio $b_{3/2}(V)/b_{\text{Heston}}(V) = \xi V$ and explain why the 3/2 model generates heavier tails and steeper short-maturity smiles when $V$ is large.

??? success "Solution to Exercise 5"
    In the Heston model, the diffusion coefficient for $V$ is $b_{\text{Heston}}(V) = \xi\sqrt{V}$. In the 3/2 model, it is $b_{3/2}(V) = \xi V^{3/2}$.

    The ratio is:

    $$
    \frac{b_{3/2}(V)}{b_{\text{Heston}}(V)} = \frac{\xi V^{3/2}}{\xi \sqrt{V}} = V
    $$

    This means:

    - When $V > 1$: the 3/2 model has strictly higher volatility-of-volatility than Heston
    - When $V < 1$ (which is the typical regime since $V$ represents variance, often around 0.04 for a 20% vol): the 3/2 model has lower absolute vol-of-vol, **but** the scaling is steeper

    The key insight is the **sensitivity** of vol-of-vol to the level of $V$. The elasticity of $b$ with respect to $V$ is:

    $$
    \frac{\partial \log b}{\partial \log V} = \begin{cases} 1/2 & \text{(Heston)} \\ 3/2 & \text{(3/2 model)} \end{cases}
    $$

    In the 3/2 model, when variance spikes upward, the volatility-of-volatility increases much faster (cubic rather than linear scaling in $\sqrt{V}$). This creates a positive feedback: high variance leads to even more volatile variance, which can push variance to extreme values. The result is heavier tails in the return distribution.

    For short-maturity smiles, the curvature is driven by the local behavior of vol-of-vol near the current variance level. The 3/2 model's steeper scaling generates more smile convexity and steeper wings, particularly when the current variance is elevated.

---

**Exercise 6.** The SABR model uses forward-price dynamics $dF_t = \sigma_t F_t^{\beta}\,dW_t^F$ and $d\sigma_t = \nu\sigma_t\,dW_t^{\sigma}$. Explain why there is no drift term in the forward equation (relate to the choice of numeraire). What role does $\beta$ play in determining the backbone of the smile? Contrast the cases $\beta = 0$ (normal), $\beta = 1$ (lognormal), and $\beta = 0.5$.

??? success "Solution to Exercise 6"
    In the SABR model, the forward price $F_t$ satisfies $dF_t = \sigma_t F_t^{\beta}\,dW_t^F$ with no drift term. This is because the model is specified under the **forward measure** $\mathbb{Q}^T$ (associated with the $T$-maturity zero-coupon bond as numeraire).

    Under $\mathbb{Q}^T$, the forward price $F_t = \mathbb{E}^{\mathbb{Q}^T}[S_T | \mathcal{F}_t]$ is a martingale by definition. A martingale has zero drift, hence $dF_t$ contains only the diffusion term.

    The parameter $\beta \in [0, 1]$ controls the **backbone** of the implied volatility smile, determining how the ATM implied volatility scales with the forward level:

    - **$\beta = 0$ (normal model):** $dF_t = \sigma_t\,dW_t^F$. The diffusion coefficient is independent of $F$. This produces a **normal backbone**: ATM implied normal volatility is approximately constant as the forward moves. The implied lognormal volatility scales as $\sigma_{\text{impl}} \propto 1/F$, increasing as the forward falls.

    - **$\beta = 1$ (lognormal model):** $dF_t = \sigma_t F_t\,dW_t^F$. This is a geometric-type diffusion, producing a **lognormal backbone**: ATM implied lognormal volatility is approximately constant as the forward moves.

    - **$\beta = 0.5$ (CIR-like):** $dF_t = \sigma_t \sqrt{F_t}\,dW_t^F$. This produces an intermediate backbone where ATM implied lognormal volatility scales as $\sigma_{\text{impl}} \propto 1/\sqrt{F}$, which often provides a good empirical fit for interest rate markets.

    In practice, $\beta$ is often fixed (e.g., at 0.5 for rates) and the remaining parameters $(\sigma_0, \nu, \rho)$ are calibrated to the smile.

---

**Exercise 7.** Under Girsanov's theorem, the risk-neutral drift of the variance process is $a^{\mathbb{Q}} = a^{\mathbb{P}} - \lambda_V b$. For the Heston model with $a^{\mathbb{P}}(V) = \kappa^{\mathbb{P}}(\theta^{\mathbb{P}} - V)$ and $b(V) = \xi\sqrt{V}$, suppose $\lambda_V = \lambda\sqrt{V}$ (proportional specification). Derive the risk-neutral parameters $\kappa^{\mathbb{Q}}$ and $\theta^{\mathbb{Q}}$ in terms of $\kappa^{\mathbb{P}}$, $\theta^{\mathbb{P}}$, $\lambda$, and $\xi$. Verify that the Feller condition under $\mathbb{Q}$, namely $2\kappa^{\mathbb{Q}}\theta^{\mathbb{Q}} \geq \xi^2$, is preserved if and only if it holds under $\mathbb{P}$.

??? success "Solution to Exercise 7"
    Starting from the risk-neutral drift formula:

    $$
    a^{\mathbb{Q}}(V) = a^{\mathbb{P}}(V) - \lambda_V b(V)
    $$

    Substituting $a^{\mathbb{P}}(V) = \kappa^{\mathbb{P}}(\theta^{\mathbb{P}} - V)$, $b(V) = \xi\sqrt{V}$, and $\lambda_V = \lambda\sqrt{V}$:

    $$
    a^{\mathbb{Q}}(V) = \kappa^{\mathbb{P}}(\theta^{\mathbb{P}} - V) - \lambda\sqrt{V} \cdot \xi\sqrt{V} = \kappa^{\mathbb{P}}\theta^{\mathbb{P}} - \kappa^{\mathbb{P}} V - \lambda\xi V
    $$

    $$
    = \kappa^{\mathbb{P}}\theta^{\mathbb{P}} - (\kappa^{\mathbb{P}} + \lambda\xi)V = (\kappa^{\mathbb{P}} + \lambda\xi)\!\left(\frac{\kappa^{\mathbb{P}}\theta^{\mathbb{P}}}{\kappa^{\mathbb{P}} + \lambda\xi} - V\right)
    $$

    Reading off the risk-neutral parameters:

    $$
    \kappa^{\mathbb{Q}} = \kappa^{\mathbb{P}} + \lambda\xi, \qquad \theta^{\mathbb{Q}} = \frac{\kappa^{\mathbb{P}}\theta^{\mathbb{P}}}{\kappa^{\mathbb{P}} + \lambda\xi}
    $$

    For the Feller condition, note that:

    $$
    2\kappa^{\mathbb{Q}}\theta^{\mathbb{Q}} = 2(\kappa^{\mathbb{P}} + \lambda\xi) \cdot \frac{\kappa^{\mathbb{P}}\theta^{\mathbb{P}}}{\kappa^{\mathbb{P}} + \lambda\xi} = 2\kappa^{\mathbb{P}}\theta^{\mathbb{P}}
    $$

    Therefore:

    $$
    2\kappa^{\mathbb{Q}}\theta^{\mathbb{Q}} = 2\kappa^{\mathbb{P}}\theta^{\mathbb{P}}
    $$

    The product $\kappa\theta$ is invariant under this measure change. Since $\xi$ is unchanged by Girsanov's theorem, the Feller condition $2\kappa\theta \geq \xi^2$ holds under $\mathbb{Q}$ if and only if it holds under $\mathbb{P}$.
