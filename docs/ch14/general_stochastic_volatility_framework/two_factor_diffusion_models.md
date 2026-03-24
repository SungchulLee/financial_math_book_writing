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

---

**Exercise 2.** Write down the infinitesimal generator $\mathcal{L}$ for the Heston model:

$$
\begin{aligned}
dS_t &= (r-q)S_t\,dt + \sqrt{V_t}\,S_t\,dW_t^S \\
dV_t &= \kappa(\theta - V_t)\,dt + \xi\sqrt{V_t}\,dW_t^V
\end{aligned}
$$

by identifying the coefficients $\mu S$, $\sigma S$, $a$, and $b$ in the general formula. Show explicitly how the cross-derivative term involves $\rho$.

---

**Exercise 3.** In the Stein–Stein model, volatility follows an Ornstein–Uhlenbeck process $dV_t = \kappa(\theta - V_t)\,dt + \xi\,dW_t^V$. Explain why $V_t$ can become negative. Compute the probability $\mathbb{P}(V_t < 0)$ for $V_0 = 0.2$, $\theta = 0.2$, $\kappa = 1.5$, $\xi = 0.3$, and $t = 1$ year, using the known Gaussian distribution of the OU process. Why is this problematic for a stochastic volatility model?

---

**Exercise 4.** Under a two-factor stochastic volatility model, the unconditional distribution of $\log(S_T/S_0)$ is a mixture of normals conditional on integrated variance. Specifically,

$$
\log(S_T/S_0) \big| \int_0^T V_s\,ds = I \sim \mathcal{N}\!\left((r-q)T - \tfrac{1}{2}I,\; I\right)
$$

when $\rho = 0$. Show that the unconditional kurtosis of $\log(S_T/S_0)$ exceeds 3 whenever $\text{Var}[\int_0^T V_s\,ds] > 0$. (Hint: use the law of total variance and the formula for kurtosis of a variance-mean mixture of normals.)

---

**Exercise 5.** Compare the Heston and 3/2 models in terms of how volatility of volatility scales with the variance level $V$. In Heston, $b(V) = \xi\sqrt{V}$; in the 3/2 model, $b(V) = \xi V^{3/2}$. Compute the ratio $b_{3/2}(V)/b_{\text{Heston}}(V) = \xi V$ and explain why the 3/2 model generates heavier tails and steeper short-maturity smiles when $V$ is large.

---

**Exercise 6.** The SABR model uses forward-price dynamics $dF_t = \sigma_t F_t^{\beta}\,dW_t^F$ and $d\sigma_t = \nu\sigma_t\,dW_t^{\sigma}$. Explain why there is no drift term in the forward equation (relate to the choice of numeraire). What role does $\beta$ play in determining the backbone of the smile? Contrast the cases $\beta = 0$ (normal), $\beta = 1$ (lognormal), and $\beta = 0.5$.

---

**Exercise 7.** Under Girsanov's theorem, the risk-neutral drift of the variance process is $a^{\mathbb{Q}} = a^{\mathbb{P}} - \lambda_V b$. For the Heston model with $a^{\mathbb{P}}(V) = \kappa^{\mathbb{P}}(\theta^{\mathbb{P}} - V)$ and $b(V) = \xi\sqrt{V}$, suppose $\lambda_V = \lambda\sqrt{V}$ (proportional specification). Derive the risk-neutral parameters $\kappa^{\mathbb{Q}}$ and $\theta^{\mathbb{Q}}$ in terms of $\kappa^{\mathbb{P}}$, $\theta^{\mathbb{P}}$, $\lambda$, and $\xi$. Verify that the Feller condition under $\mathbb{Q}$, namely $2\kappa^{\mathbb{Q}}\theta^{\mathbb{Q}} \geq \xi^2$, is preserved if and only if it holds under $\mathbb{P}$.
