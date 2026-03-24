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
