# Geometric Brownian Motion as Asset Price Model


As discussed in the preceding section on historical context, the arithmetic Brownian motion model of Bachelier (1900) permits negative prices---a fundamental deficiency for modeling limited-liability securities. Geometric Brownian motion (GBM) resolves this problem by modeling **multiplicative** rather than additive fluctuations, ensuring that prices remain strictly positive. GBM is the stochastic process that underlies the Black-Scholes framework.

This section defines GBM, derives its closed-form solution using Ito's lemma, characterizes the resulting log-normal distribution, computes its moments, and examines the model's empirical limitations.

!!! abstract "Learning Objectives"
    After completing this section, you should be able to:

    - State the GBM stochastic differential equation and interpret its drift and diffusion coefficients
    - Derive the closed-form solution for $S_t$ by applying Ito's lemma to $\ln S_t$
    - Characterize the log-normal distribution of $S_t$ and compute its mean, variance, and higher moments
    - Explain why GBM guarantees positive prices and produces independent multiplicative returns
    - Identify the key empirical limitations of GBM as a model for real asset prices

---

## The GBM Stochastic Differential Equation


### 1. Motivation

Consider an asset whose **percentage return** over a small time interval $[t, t + dt]$ consists of a deterministic component proportional to $dt$ and a random component proportional to $dW_t$. Writing this as

$$
\frac{dS_t}{S_t} = \mu \, dt + \sigma \, dW_t
$$

and multiplying both sides by $S_t$ yields the GBM stochastic differential equation.

### 2. Definition

!!! info "Definition: Geometric Brownian Motion"
    A stochastic process $\{S_t\}_{t \geq 0}$ is a **geometric Brownian motion** with drift $\mu \in \mathbb{R}$ and volatility $\sigma > 0$ if it satisfies the SDE

    $$
    dS_t = \mu S_t \, dt + \sigma S_t \, dW_t, \qquad S_0 > 0
    $$

    where $W_t$ is a standard Brownian motion on a filtered probability space $(\Omega, \mathcal{F}, \{\mathcal{F}_t\}, \mathbb{P})$.

The parameters have the following interpretations:

- $\mu$ is the **instantaneous expected rate of return** (drift), measured per unit time
- $\sigma$ is the **instantaneous volatility**, measuring the magnitude of random fluctuations per unit time
- $S_0 > 0$ is the initial (known) asset price

The SDE is of **multiplicative noise** type: both the drift coefficient $\mu S_t$ and the diffusion coefficient $\sigma S_t$ are proportional to the current price level. This ensures that a \$100 stock fluctuates ten times as much in absolute terms as a \$10 stock, while their **percentage** fluctuations have the same distribution.

---

## Solution via Ito's Lemma


### 1. Setup

To solve the GBM SDE, apply Ito's lemma to the function $f(x) = \ln x$. For $x > 0$, we have

$$
f'(x) = \frac{1}{x}, \qquad f''(x) = -\frac{1}{x^2}
$$

### 2. Application of Ito's Lemma

By Ito's lemma, for a process $S_t$ satisfying $dS_t = \mu S_t \, dt + \sigma S_t \, dW_t$, the process $Y_t = \ln S_t$ satisfies

$$
dY_t = f'(S_t)\,dS_t + \frac{1}{2}\,f''(S_t)\,(dS_t)^2
$$

Substituting and using the Ito multiplication rules ($dt \cdot dt = 0$, $dW_t \cdot dt = 0$, $dW_t \cdot dW_t = dt$):

$$
dY_t = \frac{1}{S_t}\left(\mu S_t \, dt + \sigma S_t \, dW_t\right) + \frac{1}{2}\left(-\frac{1}{S_t^2}\right)\sigma^2 S_t^2 \, dt
$$

Simplifying:

$$
dY_t = \left(\mu - \frac{1}{2}\sigma^2\right) dt + \sigma \, dW_t
$$

### 3. Integration

Since the coefficients are constant, $Y_t = \ln S_t$ is an arithmetic Brownian motion (with drift). Integrating from $0$ to $t$:

$$
\ln S_t - \ln S_0 = \left(\mu - \frac{1}{2}\sigma^2\right)t + \sigma W_t
$$

Exponentiating both sides yields the **closed-form solution**:

$$
\boxed{S_t = S_0 \exp\!\left[\left(\mu - \frac{1}{2}\sigma^2\right)t + \sigma W_t\right]}
$$

!!! warning "The Ito Correction Term"
    The factor $-\frac{1}{2}\sigma^2$ in the exponent is the **Ito correction** (sometimes called the "convexity adjustment"). It arises from the second-order term in Ito's lemma and distinguishes stochastic calculus from ordinary calculus. Without this correction, $\mathbb{E}[S_t]$ would not equal $S_0 e^{\mu t}$. The Ito correction ensures consistency between the SDE drift $\mu$ and the expected growth rate of the price.

---

## The Log-Normal Distribution


### 1. Distributional Characterization

Since $W_t \sim \mathcal{N}(0, t)$, the log-return $\ln(S_t / S_0)$ is normally distributed:

$$
\ln\!\left(\frac{S_t}{S_0}\right) \sim \mathcal{N}\!\left(\left(\mu - \frac{1}{2}\sigma^2\right)t,\; \sigma^2 t\right)
$$

Equivalently, $S_t$ has a **log-normal distribution**:

$$
S_t \sim \text{LogNormal}\!\left(\ln S_0 + \left(\mu - \frac{1}{2}\sigma^2\right)t,\; \sigma^2 t\right)
$$

The probability density function of $S_t$ is

$$
f_{S_t}(s) = \frac{1}{s\,\sigma\sqrt{2\pi t}}\exp\!\left[-\frac{\left(\ln s - \ln S_0 - (\mu - \frac{1}{2}\sigma^2)t\right)^2}{2\sigma^2 t}\right], \quad s > 0
$$

### 2. Key Properties of the Log-Normal Distribution

The log-normal distribution has several properties that make it suitable for modeling asset prices:

- **Positivity**: $S_t > 0$ almost surely for all $t > 0$
- **Right skewness**: The distribution has a long right tail, consistent with the observation that extreme positive returns are possible
- **Multiplicative structure**: If $S_t$ and $S_{t+h}/S_t$ are log-normally distributed, then $S_{t+h}$ is also log-normal

---

## Moments of GBM


### 1. Mean

To compute $\mathbb{E}[S_t]$, use the moment generating function of the normal distribution. Since $\ln S_t = \ln S_0 + (\mu - \frac{1}{2}\sigma^2)t + \sigma W_t$ and $W_t \sim \mathcal{N}(0,t)$:

$$
\mathbb{E}[S_t] = S_0 \exp\!\left[\left(\mu - \frac{1}{2}\sigma^2\right)t\right] \cdot \mathbb{E}\!\left[e^{\sigma W_t}\right]
$$

Using the fact that if $Z \sim \mathcal{N}(0,1)$, then $\mathbb{E}[e^{aZ}] = e^{a^2/2}$, and writing $W_t = \sqrt{t}\,Z$:

$$
\mathbb{E}\!\left[e^{\sigma W_t}\right] = e^{\sigma^2 t / 2}
$$

Therefore:

$$
\boxed{\mathbb{E}[S_t] = S_0\,e^{\mu t}}
$$

The expected price grows at rate $\mu$, confirming that $\mu$ is the instantaneous expected rate of return. The Ito correction $-\frac{1}{2}\sigma^2$ in the exponent of the solution is exactly offset by the convexity of the exponential function.

### 2. Variance

For the second moment:

$$
\mathbb{E}[S_t^2] = S_0^2 \exp\!\left[2\left(\mu - \frac{1}{2}\sigma^2\right)t\right] \cdot \mathbb{E}\!\left[e^{2\sigma W_t}\right] = S_0^2\,e^{(2\mu + \sigma^2)t}
$$

The variance is therefore:

$$
\boxed{\text{Var}(S_t) = S_0^2\,e^{2\mu t}\!\left(e^{\sigma^2 t} - 1\right)}
$$

The coefficient of variation (standard deviation divided by mean) is:

$$
\text{CV}(S_t) = \sqrt{e^{\sigma^2 t} - 1}
$$

which depends only on $\sigma$ and $t$, not on $\mu$ or $S_0$.

### 3. Higher Moments

The $n$-th moment of $S_t$ is

$$
\mathbb{E}[S_t^n] = S_0^n \exp\!\left[n\mu t + \frac{n^2 - n}{2}\sigma^2 t\right]
$$

From this, the **skewness** and **excess kurtosis** of $S_t$ can be derived. Writing $v = e^{\sigma^2 t} - 1$ for brevity:

$$
\text{Skewness}(S_t) = (v + 3)\sqrt{v}
$$

$$
\text{Excess Kurtosis}(S_t) = v^4 + 2v^3 + 3v^2 - 3
$$

Both quantities are strictly positive for $\sigma > 0$ and $t > 0$, confirming that the log-normal distribution is **right-skewed** and **leptokurtic** (heavier right tail than the normal distribution).

---

## Independent Multiplicative Returns


### 1. Non-Overlapping Returns

A key property of GBM is that returns over non-overlapping intervals are **independent**. For $0 \leq s < t$, the return ratio is

$$
\frac{S_t}{S_s} = \exp\!\left[\left(\mu - \frac{1}{2}\sigma^2\right)(t-s) + \sigma(W_t - W_s)\right]
$$

Since $W_t - W_s$ is independent of $\mathcal{F}_s$ (the independent increments property of Brownian motion), the ratio $S_t / S_s$ is independent of $\{S_u : u \leq s\}$.

### 2. The Markov Property

GBM is a **Markov process**: the conditional distribution of $S_t$ given the entire history $\{S_u : u \leq s\}$ depends only on $S_s$:

$$
S_t \mid S_s \sim \text{LogNormal}\!\left(\ln S_s + \left(\mu - \frac{1}{2}\sigma^2\right)(t-s),\; \sigma^2(t-s)\right)
$$

This Markov property is essential for the Black-Scholes framework, where the option price $V(S_t, t)$ depends on the current price and time, not on the entire price history.

### 3. Stationarity of Log-Returns

The continuously compounded return over a period of length $h$ is

$$
r_{t,h} = \ln\!\left(\frac{S_{t+h}}{S_t}\right) = \left(\mu - \frac{1}{2}\sigma^2\right)h + \sigma(W_{t+h} - W_t)
$$

This return is:

- **Normally distributed** with mean $(\mu - \frac{1}{2}\sigma^2)h$ and variance $\sigma^2 h$
- **Independent** of returns over non-overlapping periods
- **Stationary**: its distribution depends on the interval length $h$ but not on the starting time $t$

These three properties---normality, independence, and stationarity of log-returns---are the defining empirical predictions of the GBM model.

---

## Empirical Limitations of GBM


While GBM provides a mathematically elegant and tractable framework, empirical evidence reveals several systematic departures from its predictions.

### 1. Fat Tails and Excess Kurtosis

Real asset returns exhibit **heavier tails** than the normal distribution predicts. Large moves (both positive and negative) occur far more frequently than a Gaussian model implies. For example, the October 19, 1987 crash saw the S&P 500 fall approximately 20% in a single day---an event with probability less than $10^{-50}$ under GBM with typical parameters.

Formally, if log-returns were truly normal, the excess kurtosis of daily returns would be zero. Empirically, equity index returns typically have excess kurtosis of 5--50, depending on the asset and sampling frequency.

### 2. Volatility Clustering

GBM assumes constant volatility $\sigma$. In reality, asset return volatility exhibits **clustering**: periods of high volatility tend to be followed by further high volatility, and periods of low volatility tend to persist. This phenomenon is captured by GARCH models (Engle, 1982; Bollerslev, 1986) and stochastic volatility models (Heston, 1993).

### 3. The Leverage Effect

Empirically, volatility tends to **increase when prices fall** and decrease when prices rise. This negative correlation between returns and volatility changes is called the **leverage effect** (Black, 1976). GBM, with its constant $\sigma$, cannot capture this asymmetry.

### 4. Jumps

Asset prices occasionally exhibit **discontinuous movements** (jumps) due to earnings announcements, geopolitical events, or sudden shifts in market sentiment. GBM produces continuous sample paths almost surely, so it assigns zero probability to such discontinuities. Merton's (1976) jump-diffusion model addresses this limitation by adding a Poisson jump component:

$$
\frac{dS_t}{S_t} = (\mu - \lambda \bar{k})\,dt + \sigma\,dW_t + J_t\,dN_t
$$

where $N_t$ is a Poisson process with intensity $\lambda$, $J_t$ is the random jump size, and $\bar{k} = \mathbb{E}[J_t]$.

### 5. Mean Reversion and Long Memory

Some asset classes (interest rates, commodities, volatility indices) exhibit **mean reversion**: prices tend to drift back toward a long-run equilibrium level. GBM has no such mechanism. Additionally, some return series exhibit **long memory** (slowly decaying autocorrelations), which is inconsistent with the independent increments of Brownian motion.

!!! tip "GBM as a Benchmark Model"
    Despite these limitations, GBM remains the standard benchmark model in quantitative finance for several reasons: it guarantees positive prices, it admits closed-form solutions for many derivative pricing problems, and departures from GBM are typically measured *relative to it* (e.g., implied volatility is defined by inverting the Black-Scholes formula). Understanding GBM thoroughly is a prerequisite for working with more sophisticated models.

---

## Summary


Geometric Brownian motion provides the stochastic foundation for the Black-Scholes model. The key results are:

**1. The SDE**: $dS_t = \mu S_t \, dt + \sigma S_t \, dW_t$ models multiplicative fluctuations proportional to the price level.

**2. Closed-form solution**: Applying Ito's lemma to $\ln S_t$ yields $S_t = S_0 \exp[(\mu - \frac{1}{2}\sigma^2)t + \sigma W_t]$, where the $-\frac{1}{2}\sigma^2$ term is the Ito correction.

**3. Log-normal distribution**: $S_t$ is log-normally distributed, guaranteeing positive prices and producing right-skewed returns.

**4. Moments**: $\mathbb{E}[S_t] = S_0 e^{\mu t}$ and $\text{Var}(S_t) = S_0^2 e^{2\mu t}(e^{\sigma^2 t} - 1)$.

**5. Independent returns**: Non-overlapping log-returns are independent and normally distributed (the i.i.d. Gaussian return assumption).

**6. Limitations**: Real returns exhibit fat tails, volatility clustering, leverage effects, and jumps---all absent from GBM. These limitations motivate the extensions discussed in later chapters.

The next section on self-financing portfolios builds directly on the GBM dynamics developed here, showing how to construct trading strategies that replicate derivative payoffs through continuous rebalancing.

---

## Exercises

**Exercise 1.** Let $S_t$ follow GBM with $S_0 = 50$, $\mu = 0.08$, and $\sigma = 0.30$. Compute $\mathbb{E}[S_2]$, $\text{Var}(S_2)$, and the probability $\mathbb{P}(S_2 > 75)$.

---

**Exercise 2.** Starting from the GBM SDE $dS_t = \mu S_t \, dt + \sigma S_t \, dW_t$, apply Ito's lemma to $f(S_t) = S_t^n$ (for integer $n \geq 2$) to derive the SDE satisfied by $S_t^n$. Use this to verify the formula for $\mathbb{E}[S_t^n]$ given in the text.

---

**Exercise 3.** The coefficient of variation $\text{CV}(S_t) = \sqrt{e^{\sigma^2 t} - 1}$ depends only on $\sigma$ and $t$. Compute the CV for $\sigma = 0.20$ and $t \in \{0.25, 1, 5, 10\}$. At what time horizon $t^*$ does the CV equal 1 (i.e., the standard deviation equals the mean)? Express $t^*$ in terms of $\sigma$.

---

**Exercise 4.** Show that under GBM, the median of $S_t$ is $S_0 \exp[(\mu - \frac{1}{2}\sigma^2)t]$, which is strictly less than the mean $\mathbb{E}[S_t] = S_0 e^{\mu t}$ whenever $\sigma > 0$. Explain intuitively why the mean exceeds the median for a log-normally distributed random variable.

---

**Exercise 5.** A common critique of GBM is that it cannot produce the "volatility clustering" observed in real data. Explain precisely what property of the GBM log-returns $r_{t,h} = \ln(S_{t+h}/S_t)$ rules out volatility clustering. Propose a minimal modification to the GBM framework that could accommodate this phenomenon, and describe how it would alter the distribution of $S_t$.

---

**Exercise 6.** Consider two stocks, $S_t^{(1)}$ and $S_t^{(2)}$, each following independent GBMs with the same parameters $\mu$ and $\sigma$ but different initial prices $S_0^{(1)} = 100$ and $S_0^{(2)} = 200$. Define the ratio $R_t = S_t^{(1)} / S_t^{(2)}$. Apply Ito's lemma to show that $R_t$ is also a GBM, determine its drift and volatility, and compute $\mathbb{E}[R_1]$.

---

**Exercise 7.** On October 19, 1987, the S&P 500 fell approximately 20% in a single day. Assuming GBM with $\sigma = 0.20$ (annualized) and using $\Delta t = 1/252$ for one trading day, compute the probability of a daily log-return less than $\ln(0.80)$. Express your answer in terms of standard deviations from the mean. What does this imply about the adequacy of the GBM model for tail-risk assessment?

---

## Solutions

??? success "Solution to Exercise 1"
    With $S_0 = 50$, $\mu = 0.08$, $\sigma = 0.30$, and $t = 2$:

    **Expected value**:

    $$
    \mathbb{E}[S_2] = S_0 e^{\mu t} = 50 \cdot e^{0.08 \times 2} = 50 \cdot e^{0.16} \approx 50 \times 1.1735 = 58.67
    $$

    **Variance**:

    $$
    \text{Var}(S_2) = S_0^2 e^{2\mu t}(e^{\sigma^2 t} - 1) = 2500 \cdot e^{0.32}(e^{0.18} - 1)
    $$

    $$
    = 2500 \times 1.3771 \times 0.1972 \approx 678.9
    $$

    **Probability $\mathbb{P}(S_2 > 75)$**: Since $\ln S_2 \sim \mathcal{N}(\ln 50 + (0.08 - 0.045) \times 2, 0.09 \times 2) = \mathcal{N}(3.9820 , 0.18)$:

    $$
    \mathbb{P}(S_2 > 75) = \mathbb{P}(\ln S_2 > \ln 75) = 1 - \Phi\!\left(\frac{\ln 75 - 3.9820}{\sqrt{0.18}}\right)
    $$

    $$
    = 1 - \Phi\!\left(\frac{4.3175 - 3.9820}{0.4243}\right) = 1 - \Phi(0.7907)
    $$

    $$
    \approx 1 - 0.7854 = 0.2146
    $$

    There is approximately a 21.5% probability that the stock price exceeds 75 after two years.

??? success "Solution to Exercise 2"
    Let $f(S_t) = S_t^n$. We compute the derivatives: $f'(x) = nx^{n-1}$ and $f''(x) = n(n-1)x^{n-2}$.

    Applying Ito's lemma to $Y_t = S_t^n$:

    $$
    dY_t = f'(S_t)\,dS_t + \frac{1}{2}f''(S_t)(\sigma S_t)^2\,dt
    $$

    $$
    = nS_t^{n-1}(\mu S_t\,dt + \sigma S_t\,dW_t) + \frac{1}{2}n(n-1)S_t^{n-2}\sigma^2 S_t^2\,dt
    $$

    $$
    = nS_t^n\mu\,dt + nS_t^n\sigma\,dW_t + \frac{1}{2}n(n-1)\sigma^2 S_t^n\,dt
    $$

    $$
    = S_t^n\!\left[\left(n\mu + \frac{n(n-1)}{2}\sigma^2\right)dt + n\sigma\,dW_t\right]
    $$

    Therefore $Y_t = S_t^n$ satisfies a GBM-type SDE with drift coefficient $n\mu + \frac{n(n-1)}{2}\sigma^2$ and diffusion coefficient $n\sigma$.

    Taking expectations (using $\mathbb{E}[dW_t] = 0$):

    $$
    \frac{d}{dt}\mathbb{E}[S_t^n] = \left(n\mu + \frac{n(n-1)}{2}\sigma^2\right)\mathbb{E}[S_t^n]
    $$

    This ODE has solution:

    $$
    \mathbb{E}[S_t^n] = S_0^n \exp\!\left[\left(n\mu + \frac{n(n-1)}{2}\sigma^2\right)t\right] = S_0^n \exp\!\left[n\mu t + \frac{n^2 - n}{2}\sigma^2 t\right]
    $$

    which agrees with the formula in the text. $\square$

??? success "Solution to Exercise 3"
    The coefficient of variation is $\text{CV}(S_t) = \sqrt{e^{\sigma^2 t} - 1}$.

    With $\sigma = 0.20$ (so $\sigma^2 = 0.04$):

    | $t$ | $\sigma^2 t$ | $e^{\sigma^2 t}$ | $\text{CV}(S_t)$ |
    |-----|-------------|-----------------|------------------|
    | 0.25 | 0.01 | 1.01005 | $\sqrt{0.01005} \approx 0.1003$ |
    | 1 | 0.04 | 1.04081 | $\sqrt{0.04081} \approx 0.2020$ |
    | 5 | 0.20 | 1.22140 | $\sqrt{0.22140} \approx 0.4705$ |
    | 10 | 0.40 | 1.49182 | $\sqrt{0.49182} \approx 0.7013$ |

    Setting $\text{CV} = 1$:

    $$
    \sqrt{e^{\sigma^2 t^*} - 1} = 1 \implies e^{\sigma^2 t^*} = 2 \implies t^* = \frac{\ln 2}{\sigma^2}
    $$

    For $\sigma = 0.20$: $t^* = \frac{0.6931}{0.04} = 17.33$ years.

    In general, $t^* = \frac{\ln 2}{\sigma^2}$. This shows that the standard deviation equals the mean only at very long horizons for typical equity volatilities, reflecting the exponential growth of GBM uncertainty over time.

??? success "Solution to Exercise 4"
    The median of a log-normal random variable $X$ with $\ln X \sim \mathcal{N}(m, v^2)$ is $e^m$ (since $\mathbb{P}(\ln X \leq m) = \Phi(0) = 0.5$).

    For $S_t$ under GBM, $\ln S_t \sim \mathcal{N}(\ln S_0 + (\mu - \frac{1}{2}\sigma^2)t, \sigma^2 t)$, so:

    $$
    \text{Median}(S_t) = \exp\!\left[\ln S_0 + \left(\mu - \frac{1}{2}\sigma^2\right)t\right] = S_0 e^{(\mu - \frac{1}{2}\sigma^2)t}
    $$

    The mean is $\mathbb{E}[S_t] = S_0 e^{\mu t}$. The ratio is:

    $$
    \frac{\text{Median}(S_t)}{\mathbb{E}[S_t]} = e^{-\frac{1}{2}\sigma^2 t} < 1 \quad \text{for all } \sigma > 0, t > 0
    $$

    so the median is strictly less than the mean.

    **Intuition**: The log-normal distribution is right-skewed. A small number of very large outcomes (in the heavy right tail) pull the mean upward without affecting the median. More than half the sample paths end up below the mean, while the average is inflated by the few paths that reach very high values. This is the continuous-time manifestation of the asymmetry in compounding: the arithmetic mean return exceeds the geometric mean return, and most individual paths grow at the geometric rate $\mu - \frac{1}{2}\sigma^2$.

??? success "Solution to Exercise 5"
    Under GBM, the log-returns $r_{t,h} = \ln(S_{t+h}/S_t) = (\mu - \frac{1}{2}\sigma^2)h + \sigma(W_{t+h} - W_t)$ are **independent** across non-overlapping intervals and have **constant variance** $\sigma^2 h$.

    Volatility clustering means that the magnitude of returns (or squared returns) is positively autocorrelated: a large $|r_{t,h}|$ tends to be followed by another large $|r_{t+h,h}|$. Under GBM, since returns over non-overlapping intervals are independent, the autocorrelation of $r_{t,h}^2$ is exactly zero:

    $$
    \text{Corr}(r_{t,h}^2, r_{t+h,h}^2) = 0
    $$

    This **independence of increments** is the specific property that rules out volatility clustering. In GBM, knowing that today's return was large gives no information about whether tomorrow's return will be large or small.

    **Minimal modification**: Replace the constant volatility $\sigma$ with a stochastic process $\sigma_t$ that has its own dynamics. The simplest such model is the Heston (1993) stochastic volatility model:

    $$
    dS_t = \mu S_t\,dt + \sqrt{v_t}\,S_t\,dW_t^{(1)}
    $$

    $$
    dv_t = \kappa(\theta - v_t)\,dt + \xi\sqrt{v_t}\,dW_t^{(2)}
    $$

    where $v_t = \sigma_t^2$ is the instantaneous variance, $\kappa$ is the mean-reversion speed, $\theta$ is the long-run variance, $\xi$ is the volatility of volatility, and $W_t^{(1)}, W_t^{(2)}$ are (possibly correlated) Brownian motions. This model produces volatility clustering because $v_t$ is persistent (mean-reverting with autocorrelation), so periods of high variance tend to be followed by high variance. The distribution of $S_t$ is no longer log-normal; instead, it has fatter tails and the conditional distribution depends on the current volatility level.

??? success "Solution to Exercise 6"
    Let $S_t^{(1)} = S_0^{(1)} e^{(\mu - \frac{1}{2}\sigma^2)t + \sigma W_t^{(1)}}$ and $S_t^{(2)} = S_0^{(2)} e^{(\mu - \frac{1}{2}\sigma^2)t + \sigma W_t^{(2)}}$, where $W_t^{(1)}$ and $W_t^{(2)}$ are independent Brownian motions.

    Define $R_t = S_t^{(1)} / S_t^{(2)}$. Then:

    $$
    R_t = \frac{S_0^{(1)}}{S_0^{(2)}} \exp\!\left[\sigma(W_t^{(1)} - W_t^{(2)})\right]
    $$

    To find the SDE for $R_t$, apply Ito's lemma to $R_t = f(S_t^{(1)}, S_t^{(2)}) = S_t^{(1)}/S_t^{(2)}$.

    The partial derivatives are: $f_1 = 1/S^{(2)}$, $f_2 = -S^{(1)}/(S^{(2)})^2$, $f_{11} = 0$, $f_{22} = 2S^{(1)}/(S^{(2)})^3$, $f_{12} = -1/(S^{(2)})^2$.

    By the multidimensional Ito formula (using independence so the cross-variation $d\langle S^{(1)}, S^{(2)}\rangle = 0$):

    $$
    dR_t = \frac{1}{S_t^{(2)}}dS_t^{(1)} - \frac{S_t^{(1)}}{(S_t^{(2)})^2}dS_t^{(2)} + \frac{1}{2}\cdot\frac{2S_t^{(1)}}{(S_t^{(2)})^3}(\sigma S_t^{(2)})^2\,dt
    $$

    Substituting the GBM dynamics:

    $$
    dR_t = R_t\!\left[\mu\,dt + \sigma\,dW_t^{(1)}\right] - R_t\!\left[\mu\,dt + \sigma\,dW_t^{(2)}\right] + \sigma^2 R_t\,dt
    $$

    $$
    = R_t\!\left[\sigma^2\,dt + \sigma\,dW_t^{(1)} - \sigma\,dW_t^{(2)}\right]
    $$

    Define $\tilde{W}_t = \frac{1}{\sqrt{2}}(W_t^{(1)} - W_t^{(2)})$, which is a standard Brownian motion (since $W_t^{(1)} - W_t^{(2)}$ has variance $2t$). Then:

    $$
    dR_t = \sigma^2 R_t\,dt + \sigma\sqrt{2}\,R_t\,d\tilde{W}_t
    $$

    This is a GBM with drift $\sigma^2$ and volatility $\sigma\sqrt{2}$.

    The expected value of $R_1$ is:

    $$
    \mathbb{E}[R_1] = R_0\,e^{\sigma^2 \cdot 1} = \frac{100}{200}\,e^{\sigma^2} = 0.5\,e^{\sigma^2}
    $$

    Note that $\mathbb{E}[R_1] = 0.5\,e^{\sigma^2} > 0.5 = R_0$, so the expected ratio grows over time due to the convexity effect (Jensen's inequality).

??? success "Solution to Exercise 7"
    Under GBM, the daily log-return over $\Delta t = 1/252$ is:

    $$
    r_{\text{daily}} = \ln\!\left(\frac{S_{t+\Delta t}}{S_t}\right) \sim \mathcal{N}\!\left(\left(\mu - \frac{1}{2}\sigma^2\right)\Delta t,\; \sigma^2 \Delta t\right)
    $$

    The daily standard deviation is $\sigma\sqrt{\Delta t} = 0.20 / \sqrt{252} \approx 0.01260$.

    The mean daily log-return is $(\mu - \frac{1}{2}\sigma^2)/252$, which is negligibly small relative to the standard deviation (on the order of $10^{-4}$), so we approximate the mean as zero.

    A 20% drop corresponds to a log-return of $\ln(0.80) = -0.22314$.

    The number of standard deviations from the mean:

    $$
    z = \frac{-0.22314}{0.01260} \approx -17.71
    $$

    This is approximately a **17.7-sigma event**. The probability of a standard normal variable being below $-17.7$ is astronomically small, far less than $10^{-50}$.

    To put this in context, a 5-sigma event has probability about $3 \times 10^{-7}$ (once in several million days), and a 6-sigma event is roughly $10^{-9}$. A 17.7-sigma event is so improbable under the normal distribution that it should essentially never occur in the lifetime of the universe.

    **Implication**: The GBM model is fundamentally inadequate for tail-risk assessment. The 1987 crash was a real event, yet the model assigns it essentially zero probability. This demonstrates that real market returns have much heavier tails than the normal distribution predicts. Models incorporating jumps (Merton jump-diffusion), stochastic volatility (Heston), or heavy-tailed distributions (Student's $t$) are necessary for realistic tail-risk analysis and extreme event modeling.
