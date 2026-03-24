# Historical Context of Option Pricing Theory


The Black-Scholes model did not emerge in a vacuum. Its development in 1973 was the culmination of over seven decades of intellectual effort, beginning with Louis Bachelier's pioneering work in 1900 and refined through contributions by Paul Samuelson, James Boness, and others. Understanding this historical trajectory illuminates *why* the model takes the form it does and reveals the mathematical problems each generation sought to solve.

This section traces the evolution from Bachelier's arithmetic Brownian motion to the Black-Scholes-Merton framework, emphasizing the mathematical innovations at each stage.

!!! abstract "Learning Objectives"
    After completing this section, you should understand:

    - How Bachelier's 1900 thesis introduced stochastic processes into finance and its mathematical limitations
    - Why Samuelson replaced arithmetic Brownian motion with geometric Brownian motion
    - The key mathematical insight of Black, Scholes, and Merton: risk-neutral pricing via dynamic hedging
    - How the 1973 papers connected option pricing to partial differential equations and martingale theory
    - The subsequent evolution of options markets and extensions of the original framework

---

## Bachelier and the Birth of Mathematical Finance (1900)


### 1. The Thesis

Louis Bachelier's doctoral thesis, *Theorie de la Speculation* (1900), was the first rigorous mathematical treatment of financial markets. Supervised by Henri Poincare at the Sorbonne, Bachelier modeled the price of French government bonds (*rentes*) traded on the Paris Bourse.

Bachelier proposed that asset prices follow what we now call **arithmetic Brownian motion** (ABM). In modern notation, his model for the asset price $S_t$ takes the form

$$
dS_t = \sigma \, dW_t
$$

where $\sigma > 0$ is a volatility parameter and $W_t$ is a standard Brownian motion (Wiener process). The solution is simply

$$
S_t = S_0 + \sigma W_t
$$

so that $S_t \sim \mathcal{N}(S_0, \sigma^2 t)$.

### 2. Bachelier's Option Pricing Formula

Bachelier derived a closed-form expression for the price of an option. For a European call with strike $K$ and maturity $T$, his formula reduces to

$$
C = (S_0 - K)\,\Phi\!\left(\frac{S_0 - K}{\sigma\sqrt{T}}\right) + \sigma\sqrt{T}\,\phi\!\left(\frac{S_0 - K}{\sigma\sqrt{T}}\right)
$$

where $\Phi$ denotes the standard normal CDF and $\phi$ the standard normal PDF. This result is remarkable: Bachelier effectively computed $\mathbb{E}[(S_T - K)^+]$ under the assumption that $S_T$ is normally distributed, anticipating the risk-neutral pricing paradigm by over seventy years.

### 3. Mathematical Limitations

Despite its brilliance, Bachelier's model has a fundamental flaw. Because $S_t = S_0 + \sigma W_t$ is normally distributed, there is a **positive probability of negative prices**:

$$
\mathbb{P}(S_t < 0) = \Phi\!\left(\frac{-S_0}{\sigma\sqrt{t}}\right) > 0 \quad \text{for all } t > 0
$$

For short time horizons and moderate volatility, this probability is small. But for longer horizons, the model predicts economically meaningless negative stock prices. Bachelier also assumed zero interest rates and zero drift, limiting the model's practical applicability.

!!! note "Bachelier's Legacy"
    Bachelier's work predated Einstein's 1905 paper on Brownian motion by five years. His thesis was largely forgotten until it was rediscovered by Leonard Jimmie Savage in the 1950s, who brought it to the attention of Paul Samuelson. Bachelier's core insight---that asset prices can be modeled as stochastic processes---remains the foundation of mathematical finance.

---

## The Samuelson Era: Geometric Brownian Motion (1960s)


### 1. The Problem with Arithmetic Brownian Motion

By the 1960s, economists recognized two fundamental problems with Bachelier's ABM model:

1. **Negative prices**: As shown above, $\mathbb{P}(S_t < 0) > 0$ for any $t > 0$
2. **Non-multiplicative returns**: ABM implies that a \$1 change in a \$10 stock is as likely as a \$1 change in a \$1000 stock, contradicting the empirical observation that **percentage returns** are roughly stationary across price levels

### 2. Samuelson's Geometric Brownian Motion

Paul Samuelson (1965) and several contemporaries proposed replacing ABM with **geometric Brownian motion** (GBM). The key idea is to model **logarithmic returns** as normally distributed rather than price levels. The SDE for GBM is

$$
dS_t = \mu S_t \, dt + \sigma S_t \, dW_t
$$

where $\mu$ is the drift (expected rate of return) and $\sigma$ is the volatility. Applying Ito's lemma to $\ln S_t$ yields

$$
d(\ln S_t) = \left(\mu - \tfrac{1}{2}\sigma^2\right) dt + \sigma \, dW_t
$$

so the solution is

$$
S_t = S_0 \exp\!\left[\left(\mu - \tfrac{1}{2}\sigma^2\right)t + \sigma W_t\right]
$$

Since the exponential function is always positive, GBM guarantees $S_t > 0$ for all $t$, resolving Bachelier's negative-price problem.

### 3. Samuelson's Option Pricing Attempt

Samuelson recognized that the option price should involve an expected value of the payoff, but he computed this expectation under the **physical measure** $\mathbb{P}$:

$$
C_{\text{Samuelson}} = e^{-\alpha T}\,\mathbb{E}^{\mathbb{P}}\!\left[(S_T - K)^+\right]
$$

where $\alpha$ is an "appropriate" discount rate for the option. The fundamental difficulty was that $\alpha$ is **not equal** to the risk-free rate $r$ in general, and determining the correct $\alpha$ requires knowledge of investor risk preferences. Samuelson's formula contained two unknowns---the stock's expected return $\mu$ and the option's discount rate $\alpha$---making it impractical for pricing.

!!! warning "The Missing Insight"
    Samuelson had the correct stochastic model (GBM) but lacked the key insight that would come in 1973: the option can be **replicated** by continuous trading in the stock and bond, so its price is determined by no-arbitrage arguments alone, independent of $\mu$ and $\alpha$.

---

## Precursors to Black-Scholes (1960s--1970s)


Several researchers made partial progress toward the Black-Scholes formula, each contributing an important piece of the puzzle.

### 1. Sprenkle (1961)

Case Sprenkle derived an option pricing formula under GBM but, like Samuelson, required assumptions about investor risk aversion. His formula for a European call was

$$
C_{\text{Sprenkle}} = e^{\mu T} S_0 \,\Phi(d_1) - (1-Z)\,K\,\Phi(d_2)
$$

where $Z$ represents a risk-aversion parameter that could not be determined from market observables alone.

### 2. Boness (1964)

Alan Boness made the important step of discounting the expected stock price at the stock's own expected return $\mu$, arriving at a formula structurally close to Black-Scholes:

$$
C_{\text{Boness}} = S_0 \,\Phi(d_1) - K e^{-\mu T}\,\Phi(d_2)
$$

The formula resembles the Black-Scholes formula but with $\mu$ in place of $r$. Boness was tantalizingly close but could not justify why $\mu$ should be replaced by $r$.

### 3. The Common Obstacle

All pre-1973 approaches shared the same fundamental limitation: they required knowledge of investor preferences (risk aversion, expected returns, or subjective discount rates) to price options. The mathematical challenge was to find a pricing framework that depends only on **observable quantities**: the current stock price $S_0$, the strike $K$, the maturity $T$, the volatility $\sigma$, and the risk-free rate $r$.

---

## The Black-Scholes-Merton Breakthrough (1973)


### 1. The Key Insight: Dynamic Hedging Eliminates Risk

The fundamental innovation of Fischer Black, Myron Scholes, and Robert Merton was the recognition that an option can be **perfectly replicated** by a continuously rebalanced portfolio of the underlying stock and a risk-free bond. This replication argument has two profound consequences:

1. The option price equals the cost of the replicating portfolio (by no-arbitrage)
2. The expected return $\mu$ of the stock **cancels out** of the pricing formula

The mathematical argument proceeds as follows. Consider a portfolio $\Pi$ consisting of one option $V(S_t, t)$ and $-\Delta$ shares of the stock:

$$
\Pi_t = V(S_t, t) - \Delta \, S_t
$$

Applying Ito's lemma to $V(S_t, t)$ and choosing

$$
\Delta = \frac{\partial V}{\partial S}
$$

the stochastic ($dW_t$) terms cancel, leaving a **deterministic** change in portfolio value:

$$
d\Pi_t = \left(\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S_t^2 \frac{\partial^2 V}{\partial S^2}\right) dt
$$

Since the portfolio is risk-free over the infinitesimal interval $dt$, no-arbitrage requires it to earn the risk-free rate:

$$
d\Pi_t = r\,\Pi_t \, dt
$$

Combining these two equations yields the **Black-Scholes partial differential equation**:

$$
\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + rS\frac{\partial V}{\partial S} - rV = 0
$$

### 2. The Disappearance of the Drift

The most striking feature of the Black-Scholes PDE is that the drift $\mu$ does not appear. This occurs because the hedging portfolio eliminates the exposure to the random component $dW_t$, and once the portfolio is risk-free, it must grow at rate $r$ regardless of $\mu$. In the language of the fundamental theorem of asset pricing (Chapter 1), this corresponds to pricing under the unique **risk-neutral measure** $\mathbb{Q}$ in which the stock's drift is replaced by $r$:

$$
dS_t = r\,S_t \, dt + \sigma S_t \, dW_t^{\mathbb{Q}}
$$

### 3. The Black-Scholes Formula

Solving the PDE with the terminal condition $V(S,T) = (S - K)^+$ for a European call yields the celebrated **Black-Scholes formula**:

$$
C(S_0, T) = S_0\,\Phi(d_1) - Ke^{-rT}\,\Phi(d_2)
$$

where

$$
d_1 = \frac{\ln(S_0/K) + (r + \tfrac{1}{2}\sigma^2)T}{\sigma\sqrt{T}}, \qquad d_2 = d_1 - \sigma\sqrt{T}
$$

Compared to the earlier formulas of Sprenkle and Boness, the Black-Scholes formula replaces all subjective parameters ($\mu$, $\alpha$, $Z$) with the single observable quantity $r$. This is the mathematical expression of the no-arbitrage principle applied to continuous-time hedging.

!!! tip "Comparing Historical Formulas"
    The structural similarity between Boness's formula and the Black-Scholes formula is instructive. Replace $\mu$ with $r$ in Boness's expression to recover Black-Scholes. The economic justification for this replacement---that dynamic hedging eliminates risk, so the relevant discount rate is $r$---was the conceptual breakthrough that earned the Nobel Prize.

---

## The Two 1973 Papers


### 1. Black and Scholes (1973)

Fischer Black and Myron Scholes published *"The Pricing of Options and Corporate Liabilities"* in the *Journal of Political Economy* in May 1973. The paper:

- Derived the Black-Scholes PDE via the hedging argument
- Presented closed-form formulas for European calls and puts
- Conducted empirical tests using data from the over-the-counter options market
- Extended the model to options on dividend-paying stocks and warrants

The paper was famously rejected by both the *Journal of Finance* and the *Review of Economics and Statistics* before being accepted at the *Journal of Political Economy*, partly through the intervention of Merton Miller and Eugene Fama.

### 2. Merton (1973)

Robert Merton published *"Theory of Rational Option Pricing"* in the *Bell Journal of Economics and Management Science* in Spring 1973. Merton's paper:

- Provided a rigorous mathematical framework using Ito calculus
- Relaxed several of Black and Scholes's original assumptions
- Introduced the concept of **continuous-time self-financing portfolios** (explored in the next section on self-financing portfolios)
- Derived pricing formulas for options with continuous dividend yields
- Established model-independent bounds on option prices via no-arbitrage arguments

Merton's treatment was more mathematically sophisticated and placed the results in the broader context of continuous-time finance, connecting option pricing to the martingale theory that would later become the standard framework.

---

## The Nobel Prize and Industry Impact


### 1. The 1997 Nobel Memorial Prize

The Royal Swedish Academy of Sciences awarded the 1997 Nobel Memorial Prize in Economic Sciences to **Myron Scholes** and **Robert Merton** for developing

> *"a new method to determine the value of derivatives."*

Fischer Black had passed away in August 1995 and was therefore ineligible for the prize, which is not awarded posthumously. The Nobel committee's citation explicitly recognized Black's contribution.

### 2. The Chicago Board Options Exchange

The timing of the theoretical breakthrough coincided with a practical one. The **Chicago Board Options Exchange (CBOE)** opened on April 26, 1973---the same year the Black-Scholes and Merton papers appeared. The CBOE was the first regulated exchange for trading standardized options contracts. Early CBOE traders reportedly carried printouts of Black-Scholes option prices onto the trading floor.

### 3. Growth of the Derivatives Industry

The Black-Scholes formula catalyzed an explosion in derivatives trading:

- **1973**: CBOE opens; 911 contracts traded on the first day
- **1970s--1980s**: Over-the-counter derivatives markets expand rapidly
- **1990s**: Notional value of global derivatives exceeds \$100 trillion
- **2000s--present**: Notional value reaches approximately \$600 trillion (BIS estimates)

The formula provided a common language for pricing, hedging, and risk management that enabled this growth.

---

## Mathematical Evolution After 1973


### 1. Harrison and Kreps (1979) and Harrison and Pliska (1981)

The most important theoretical advance after Black-Scholes-Merton was the formalization of the **martingale approach to asset pricing**. Harrison and Kreps (1979) proved the first version of the **fundamental theorem of asset pricing**: the absence of arbitrage is equivalent to the existence of an equivalent martingale measure $\mathbb{Q}$.

Harrison and Pliska (1981) extended this to continuous-time models and showed that market completeness corresponds to the **uniqueness** of $\mathbb{Q}$. Under the unique risk-neutral measure, the price of any contingent claim $X$ with maturity $T$ is

$$
V_0 = e^{-rT}\,\mathbb{E}^{\mathbb{Q}}[X]
$$

This result places the Black-Scholes formula in its proper theoretical context: it is a special case of risk-neutral pricing in a complete market driven by a single Brownian motion.

### 2. Extensions of the Black-Scholes Framework

The original model's assumption of constant volatility $\sigma$ was quickly recognized as empirically inadequate. Key extensions include:

| Year | Author(s) | Model | Key Feature |
|------|-----------|-------|-------------|
| 1976 | Merton | Jump-diffusion | Poisson jumps added to GBM |
| 1987 | Hull and White | Stochastic volatility | Volatility follows its own SDE |
| 1993 | Heston | Stochastic volatility | Closed-form with vol of vol |
| 1994 | Dupire | Local volatility | $\sigma = \sigma(S,t)$ calibrated to market |
| 2000s | Gatheral et al. | Rough volatility | Fractional Brownian motion for vol |

Each extension relaxes one or more of the assumptions listed in the preceding section on model assumptions, while preserving the core methodology of no-arbitrage pricing.

### 3. The Volatility Smile

One of the most important empirical challenges to Black-Scholes emerged after the **October 1987 crash**. Before 1987, implied volatilities across different strike prices were approximately flat, consistent with the constant-$\sigma$ assumption. After the crash, implied volatility began exhibiting a persistent **skew** (or "smile"), with out-of-the-money puts carrying higher implied volatility than at-the-money options.

This observation demonstrated that the market prices options *as if* the underlying distribution has fatter left tails than the log-normal distribution---a direct violation of the GBM assumption. The volatility smile motivated the development of local volatility, stochastic volatility, and jump-diffusion models.

---

## Summary


The historical development of option pricing theory proceeded through several distinct phases:

**1. Bachelier (1900)**: Introduced stochastic modeling of asset prices via arithmetic Brownian motion ($dS = \sigma \, dW$). Derived the first option pricing formula but permitted negative prices.

**2. Samuelson (1965)**: Replaced ABM with geometric Brownian motion ($dS = \mu S \, dt + \sigma S \, dW$), ensuring positive prices. Could not eliminate dependence on investor preferences.

**3. Black-Scholes-Merton (1973)**: Showed that dynamic hedging makes the option's replication cost independent of $\mu$. Derived the Black-Scholes PDE and closed-form formula depending only on observables ($S_0, K, T, r, \sigma$).

**4. Harrison-Kreps-Pliska (1979--1981)**: Formalized the martingale approach, proving that no-arbitrage pricing is equivalent to expectation under a risk-neutral measure.

**5. Post-1987 extensions**: Stochastic volatility, local volatility, and jump-diffusion models addressed the empirical inadequacies of constant $\sigma$.

Each stage resolved a specific mathematical limitation of its predecessor while preserving the core principle that derivative prices are determined by no-arbitrage constraints, not by investor preferences about risk and return.

---

## Exercises

**Exercise 1.** Using Bachelier's arithmetic Brownian motion model $S_t = S_0 + \sigma W_t$ with $S_0 = 50$ and $\sigma = 10$ (annualized), compute the probability that the stock price is negative after 5 years. Compare this with the probability under GBM with the same $S_0$ and $\sigma / S_0 = 0.20$ as the volatility parameter.

---

**Exercise 2.** Bachelier's call pricing formula is $C = (S_0 - K)\Phi\!\left(\frac{S_0 - K}{\sigma\sqrt{T}}\right) + \sigma\sqrt{T}\,\phi\!\left(\frac{S_0 - K}{\sigma\sqrt{T}}\right)$. Derive this formula by computing $\mathbb{E}[(S_T - K)^+]$ directly, using the fact that $S_T \sim \mathcal{N}(S_0, \sigma^2 T)$ under Bachelier's model.

---

**Exercise 3.** Boness's formula has $\mu$ where the Black-Scholes formula has $r$. If a stock has expected return $\mu = 12\%$, risk-free rate $r = 4\%$, $S_0 = 100$, $K = 100$, $T = 1$, and $\sigma = 25\%$, compute the call price under both Boness's formula and the Black-Scholes formula. What is the percentage difference? Explain why the Black-Scholes price is the correct arbitrage-free price regardless of $\mu$.

---

**Exercise 4.** The hedging argument shows that in a portfolio $\Pi = V - \Delta S$, choosing $\Delta = \partial V / \partial S$ eliminates the $dW_t$ term. Starting from $dV = \frac{\partial V}{\partial t}dt + \frac{\partial V}{\partial S}dS + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2}dt$, carry out the full derivation to arrive at the Black-Scholes PDE. Identify precisely where the drift $\mu$ cancels and explain the economic reason for this cancellation.

---

**Exercise 5.** Harrison and Kreps (1979) established that absence of arbitrage is equivalent to the existence of an equivalent martingale measure. In the Black-Scholes market with one stock and one bond, explain why the market is complete (i.e., every contingent claim is replicable) and why this implies the risk-neutral measure $\mathbb{Q}$ is unique. What would change if the market had two independent sources of randomness but only one risky asset?

---

**Exercise 6.** The volatility smile emerged after the 1987 crash. Before the crash, implied volatilities across strikes were approximately flat. Explain what "implied volatility" means in terms of the Black-Scholes formula, and discuss why a non-flat implied volatility surface is inconsistent with the constant-$\sigma$ assumption of GBM. Name two post-1987 models from the table in the text and briefly describe how each addresses the smile phenomenon.
