# Jump-Diffusion SDE

The Black-Scholes model assumes asset prices follow continuous paths, yet real markets exhibit sudden, discontinuous moves driven by earnings surprises, central bank announcements, and geopolitical shocks. Merton (1976) extended geometric Brownian motion by superimposing a **compound Poisson jump process** onto the diffusion, producing a stochastic differential equation that captures both the day-to-day fluctuations and the occasional large jumps observed in equity returns.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Write down the Merton jump-diffusion SDE and identify each component
    2. Explain the role of the compensator $\lambda \bar{k}$ in ensuring the correct risk-neutral drift
    3. Derive the explicit solution for the log-price process
    4. Compute moments of the jump-diffusion return distribution

---

## Motivation

### Why Pure Diffusion Falls Short

Under geometric Brownian motion, the log-return over any interval $[t, t+\Delta t]$ is normally distributed. This implies that the probability of a move exceeding, say, ten standard deviations is astronomically small. In practice, however, daily equity returns exhibit:

- **Excess kurtosis** of 6--8 for major indices (the normal distribution has kurtosis 3)
- **Negative skewness**, reflecting that large downward moves are more frequent than large upward moves
- **Discontinuous price gaps** at market open following overnight news

A model with continuous paths cannot generate these features regardless of how the volatility parameter is chosen. Adding jumps provides a natural mechanism: between jumps the price diffuses smoothly, but at random Poisson times it experiences an instantaneous multiplicative shock.

### From Black-Scholes to Merton

Recall the Black-Scholes SDE under the risk-neutral measure $\mathbb{Q}$:

$$
\frac{dS_t}{S_t} = r\,dt + \sigma\,dW_t
$$

Merton's extension replaces the right-hand side with three terms: a drift, a continuous diffusion, and a jump component. The resulting model preserves analytical tractability through the Merton series formula while capturing heavy tails and short-maturity implied volatility smiles.

---

## The Merton Jump-Diffusion SDE

### Setup and Notation

Let $(\Omega, \mathcal{F}, \{\mathcal{F}_t\}_{t \geq 0}, \mathbb{Q})$ be a filtered probability space supporting:

- A standard Brownian motion $W = \{W_t\}_{t \geq 0}$
- A Poisson process $N = \{N_t\}_{t \geq 0}$ with constant intensity $\lambda > 0$
- A sequence of independent, identically distributed random variables $\{Y_i\}_{i \geq 1}$ representing jump multipliers

We assume $W$, $N$, and $\{Y_i\}$ are mutually independent. Each $Y_i > 0$ represents the ratio $S_{T_i}/S_{T_i^-}$ at the $i$-th jump time $T_i$, so $Y_i = 1$ means no change and $Y_i < 1$ means a downward jump.

### The SDE

!!! info "Definition: Merton Jump-Diffusion SDE"
    The asset price $S = \{S_t\}_{t \geq 0}$ satisfies

    $$
    \frac{dS_t}{S_{t^-}} = \bigl(r - \lambda\bar{k}\bigr)\,dt + \sigma\,dW_t + dJ_t
    $$

    where:

    - $r \geq 0$ is the risk-free interest rate
    - $\sigma > 0$ is the diffusion volatility
    - $\lambda > 0$ is the jump intensity (expected number of jumps per unit time)
    - $J_t = \sum_{i=1}^{N_t}(Y_i - 1)$ is the compound Poisson jump process
    - $\bar{k} = \mathbb{E}[Y_i - 1]$ is the expected relative jump size
    - $S_{t^-} = \lim_{s \uparrow t} S_s$ denotes the left limit (pre-jump price)

The notation $S_{t^-}$ is essential: at a jump time $T_i$, the price jumps from $S_{T_i^-}$ to $S_{T_i^-} \cdot Y_i$, so the ratio $S_{T_i}/S_{T_i^-} = Y_i$.

### Merton's Jump Size Distribution

Merton chose the jump multiplier $Y_i$ to be log-normally distributed:

$$
\ln Y_i \sim N(\mu_J, \sigma_J^2)
$$

where $\mu_J \in \mathbb{R}$ controls the mean jump direction and $\sigma_J > 0$ controls the dispersion of jump sizes. Under this specification:

$$
\bar{k} = \mathbb{E}[Y_i - 1] = e^{\mu_J + \sigma_J^2/2} - 1
$$

For equity markets, typical calibrated values are $\mu_J < 0$ (jumps are predominantly downward) and $\sigma_J \in (0.1, 0.5)$.

### The Compensator Term

The drift term $r - \lambda\bar{k}$ ensures that the discounted price process $e^{-rt}S_t$ is a $\mathbb{Q}$-martingale. To see why, observe that:

- The diffusion component $\sigma\,dW_t$ has zero expectation
- The compound Poisson component $dJ_t$ has expected increment $\lambda\bar{k}\,dt$ per unit time
- Without compensation, the expected instantaneous return would be $r + \lambda\bar{k}$, exceeding the risk-free rate

Subtracting $\lambda\bar{k}$ from the drift corrects for the average jump contribution, maintaining the no-arbitrage condition.

!!! tip "Equivalent Formulation"
    The SDE is often written using the compensated Poisson process $\tilde{N}_t = N_t - \lambda t$:

    $$
    \frac{dS_t}{S_{t^-}} = r\,dt + \sigma\,dW_t + (Y - 1)\,d\tilde{N}_t + (Y - 1)\lambda\,dt - \lambda\bar{k}\,dt
    $$

    Collecting the predictable terms recovers the original form.

---

## Solution of the SDE

### Log-Price Process

Applying the Ito formula for jump processes (covered in detail in a later section of this chapter), the log-price $X_t = \ln S_t$ satisfies:

$$
X_t = X_0 + \left(r - \lambda\bar{k} - \frac{1}{2}\sigma^2\right)t + \sigma W_t + \sum_{i=1}^{N_t} \ln Y_i
$$

where $X_0 = \ln S_0$. The three components are clearly separated:

1. **Deterministic drift**: $\bigl(r - \lambda\bar{k} - \tfrac{1}{2}\sigma^2\bigr)t$
2. **Continuous martingale**: $\sigma W_t$
3. **Pure jump**: $\sum_{i=1}^{N_t} \ln Y_i$

!!! info "Proposition: Explicit Solution"
    The Merton jump-diffusion SDE has the unique strong solution

    $$
    S_t = S_0 \exp\!\left[\left(r - \lambda\bar{k} - \frac{1}{2}\sigma^2\right)t + \sigma W_t\right] \prod_{i=1}^{N_t} Y_i
    $$

    where the empty product (when $N_t = 0$) equals one.

**Proof sketch.** Define $X_t = \ln S_t$. Between jump times, $S_t$ follows geometric Brownian motion with drift $r - \lambda\bar{k}$, so $dX_t = (r - \lambda\bar{k} - \tfrac{1}{2}\sigma^2)\,dt + \sigma\,dW_t$. At each jump time $T_i$, the price multiplies by $Y_i$, contributing $\ln Y_i$ to $X_t$. Summing the continuous increments and the jump contributions yields the stated formula. Uniqueness follows from Lipschitz and linear growth conditions on the coefficients. $\square$

### Conditional Distribution of the Log-Return

Conditional on $N_t = n$ jumps occurring in $[0, t]$, the log-return $\ln(S_t/S_0)$ is normally distributed:

$$
\ln\frac{S_t}{S_0} \;\Big|\; N_t = n \;\sim\; N\!\left(\left(r - \lambda\bar{k} - \frac{1}{2}\sigma^2 + \frac{n\mu_J}{t}\right)t,\; \sigma^2 t + n\sigma_J^2\right)
$$

This Gaussian mixture structure is the key to the Merton series formula for option pricing.

---

## Moments of the Return Distribution

The unconditional moments of $\ln(S_t/S_0)$ can be computed by iterated expectation over $N_t$.

### Mean

$$
\mathbb{E}\!\left[\ln\frac{S_t}{S_0}\right] = \left(r - \lambda\bar{k} - \frac{1}{2}\sigma^2\right)t + \lambda\mu_J t
$$

The first term is the drift of the diffusion (after compensation), and the second is the average contribution from jumps.

### Variance

$$
\operatorname{Var}\!\left[\ln\frac{S_t}{S_0}\right] = \sigma^2 t + \lambda t(\sigma_J^2 + \mu_J^2)
$$

The total variance has two sources: diffusion variance $\sigma^2 t$ and jump variance $\lambda t(\sigma_J^2 + \mu_J^2)$. The jump component contributes both through the randomness in jump sizes ($\sigma_J^2$) and the randomness in the number of jumps ($\mu_J^2$, via the law of total variance).

### Skewness and Kurtosis

The standardized third and fourth cumulants are:

$$
\text{Skewness} = \frac{\lambda t(\mu_J^3 + 3\mu_J\sigma_J^2)}{[\sigma^2 t + \lambda t(\sigma_J^2 + \mu_J^2)]^{3/2}}
$$

$$
\text{Excess kurtosis} = \frac{\lambda t(\mu_J^4 + 6\mu_J^2\sigma_J^2 + 3\sigma_J^4)}{[\sigma^2 t + \lambda t(\sigma_J^2 + \mu_J^2)]^{2}}
$$

When $\mu_J < 0$, the skewness is negative, matching the empirical observation that large downward moves are more likely. The excess kurtosis is always positive (heavier tails than normal), and it increases as $t$ decreases, which explains why short-maturity implied volatility smiles are steeper.

---

## Worked Example

!!! example "Numerical Illustration"
    Consider a stock with the following Merton jump-diffusion parameters:

    | Parameter | Value | Interpretation |
    |-----------|-------|----------------|
    | $S_0$ | \$100 | Initial price |
    | $r$ | 5% | Risk-free rate |
    | $\sigma$ | 20% | Diffusion volatility |
    | $\lambda$ | 0.5 | Average of 0.5 jumps per year |
    | $\mu_J$ | $-0.10$ | Mean log-jump (downward bias) |
    | $\sigma_J$ | 0.30 | Jump size dispersion |

    **Step 1: Compensator.**

    $$
    \bar{k} = e^{-0.10 + 0.30^2/2} - 1 = e^{-0.055} - 1 \approx -0.0535
    $$

    **Step 2: Adjusted drift.**

    $$
    r - \lambda\bar{k} = 0.05 - 0.5 \times (-0.0535) = 0.05 + 0.0268 = 0.0768
    $$

    **Step 3: Annualized variance of log-returns.**

    $$
    \sigma^2 + \lambda(\sigma_J^2 + \mu_J^2) = 0.04 + 0.5(0.09 + 0.01) = 0.04 + 0.05 = 0.09
    $$

    The total annualized standard deviation is $\sqrt{0.09} = 0.30$, compared to $\sigma = 0.20$ from the diffusion alone. Jumps increase the effective volatility by 50%.

    **Step 4: Excess kurtosis (1-year horizon).**

    $$
    \text{Excess kurtosis} = \frac{0.5(0.01 + 6 \times 0.01 \times 0.09 + 3 \times 0.0081)}{0.09^2} = \frac{0.5(0.01 + 0.0054 + 0.0243)}{0.0081} \approx 2.44
    $$

    This is far from zero (the Gaussian value), confirming that the jump-diffusion produces heavy tails.

---

## Connection to Other Sections

The Merton jump-diffusion SDE introduced here serves as the foundation for the entire chapter:

- The **Poisson process and jump size distribution** are studied in detail in the next section
- The **Ito formula for jump processes** provides the rigorous derivation of the log-price solution
- The **characteristic function** of the log-return enables Fourier-based pricing methods
- The **Merton series formula** exploits the conditional Gaussian structure to express option prices as weighted Black-Scholes sums
- The **PIDE** arises from the standard arbitrage argument applied to jump-diffusion dynamics

---

## Summary

The Merton jump-diffusion SDE extends geometric Brownian motion by adding a compound Poisson jump component. The three building blocks are: a deterministic drift (adjusted by the compensator $\lambda\bar{k}$), a continuous Brownian diffusion, and discrete random jumps arriving at Poisson times. The explicit solution factorizes into an exponential diffusion term and a product of random jump multipliers. The resulting return distribution is a Gaussian mixture that naturally produces negative skewness and excess kurtosis, matching key empirical features of asset returns that the Black-Scholes model cannot capture.

---

## Exercises

**Exercise 1.** Starting from the Merton jump-diffusion SDE $dS_t/S_{t^-} = (r - \lambda\bar{k})\,dt + \sigma\,dW_t + dJ_t$, verify the compensator $\bar{k} = e^{\mu_J + \sigma_J^2/2} - 1$ by computing $\mathbb{E}[Y_i - 1]$ where $\ln Y_i \sim N(\mu_J, \sigma_J^2)$. Show that the drift adjustment ensures $\mathbb{E}^{\mathbb{Q}}[dS_t/S_{t^-}] = r\,dt$.

---

**Exercise 2.** For parameters $S_0 = 100$, $r = 0.05$, $\sigma = 0.15$, $\lambda = 1.0$, $\mu_J = -0.08$, $\sigma_J = 0.25$: (a) Compute $\bar{k}$ and the adjusted drift $r - \lambda\bar{k}$. (b) Compute the annualized variance of log-returns $\sigma^2 + \lambda(\sigma_J^2 + \mu_J^2)$. (c) Compute the excess kurtosis over a one-year horizon and compare with the Gaussian value of zero.

---

**Exercise 3.** The explicit solution of the Merton SDE is $S_t = S_0 \exp[(r - \lambda\bar{k} - \frac{1}{2}\sigma^2)t + \sigma W_t] \prod_{i=1}^{N_t} Y_i$. Verify this by showing that conditional on $N_t = n$, the log-return $\ln(S_t/S_0)$ is normally distributed. State the conditional mean and variance.

---

**Exercise 4.** Explain why the skewness of the Merton log-return distribution scales as $T^{-1/2}$ for small $T$, and why this implies that short-maturity implied volatility smiles are steeper than long-maturity smiles. What does this imply about the term structure of the implied volatility skew?

---

**Exercise 5.** Compare the Merton jump-diffusion model with the Black-Scholes model by listing three empirical features of equity returns that the Merton model captures but Black-Scholes cannot. For each feature, identify which parameter(s) of the Merton model are responsible.
