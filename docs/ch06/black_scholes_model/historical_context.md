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

??? success "Solution to Exercise 1"
    Under Bachelier's ABM with $S_t = S_0 + \sigma W_t$, we have $S_t \sim \mathcal{N}(S_0, \sigma^2 t)$ with $S_0 = 50$ and $\sigma = 10$.

    After $t = 5$ years: $S_5 \sim \mathcal{N}(50, 100 \times 5) = \mathcal{N}(50, 500)$.

    $$
    \mathbb{P}(S_5 < 0) = \Phi\!\left(\frac{0 - 50}{\sqrt{500}}\right) = \Phi\!\left(\frac{-50}{22.36}\right) = \Phi(-2.236) \approx 0.0127
    $$

    Under ABM, there is approximately a 1.27% probability of a negative stock price after 5 years.

    Under GBM with volatility parameter $\sigma_{\text{GBM}} = \sigma/S_0 = 10/50 = 0.20$ and drift $\mu = 0$ (for direct comparison):

    $$
    S_t = 50\exp\!\left(-\frac{1}{2}(0.04)(5) + 0.20 W_5\right) = 50\exp(-0.10 + 0.20 W_5)
    $$

    Since $S_t = S_0 \exp(\cdot) > 0$ always, $\mathbb{P}(S_5 < 0) = 0$ under GBM, for any parameter values. The exponential function guarantees strict positivity of paths.

    This demonstrates the fundamental advantage of GBM over ABM: while both models capture randomness in price evolution, only GBM rules out the economically meaningless scenario of negative stock prices.

---
**Exercise 2.** Bachelier's call pricing formula is $C = (S_0 - K)\Phi\!\left(\frac{S_0 - K}{\sigma\sqrt{T}}\right) + \sigma\sqrt{T}\,\phi\!\left(\frac{S_0 - K}{\sigma\sqrt{T}}\right)$. Derive this formula by computing $\mathbb{E}[(S_T - K)^+]$ directly, using the fact that $S_T \sim \mathcal{N}(S_0, \sigma^2 T)$ under Bachelier's model.

??? success "Solution to Exercise 2"
    Under Bachelier's model, $S_T \sim \mathcal{N}(S_0, \sigma^2 T)$, so $S_T = S_0 + \sigma\sqrt{T}\,Z$ where $Z \sim \mathcal{N}(0,1)$.

    Define $a = \frac{S_0 - K}{\sigma\sqrt{T}}$. Then:

    $$
    \mathbb{E}[(S_T - K)^+] = \mathbb{E}[(S_0 + \sigma\sqrt{T}\,Z - K)^+] = \mathbb{E}[(\sigma\sqrt{T}\,Z + \sigma\sqrt{T}\,a)^+]
    $$

    $$
    = \sigma\sqrt{T}\,\mathbb{E}[(Z + a)^+]
    $$

    Now compute $\mathbb{E}[(Z + a)^+]$:

    $$
    \mathbb{E}[(Z + a)^+] = \int_{-a}^{\infty}(z + a)\phi(z)\,dz
    $$

    $$
    = \int_{-a}^{\infty}z\,\phi(z)\,dz + a\int_{-a}^{\infty}\phi(z)\,dz
    $$

    For the first integral, using the identity $z\,\phi(z) = -\phi'(z)$:

    $$
    \int_{-a}^{\infty}z\,\phi(z)\,dz = [-\phi(z)]_{-a}^{\infty} = \phi(-a) = \phi(a)
    $$

    (using symmetry $\phi(-a) = \phi(a)$). For the second integral:

    $$
    a\int_{-a}^{\infty}\phi(z)\,dz = a\,\Phi(a)
    $$

    Therefore:

    $$
    \mathbb{E}[(Z + a)^+] = \phi(a) + a\,\Phi(a)
    $$

    Substituting back with $a = \frac{S_0 - K}{\sigma\sqrt{T}}$:

    $$
    C = \sigma\sqrt{T}\!\left[\phi(a) + a\,\Phi(a)\right] = \sigma\sqrt{T}\,\phi\!\left(\frac{S_0 - K}{\sigma\sqrt{T}}\right) + (S_0 - K)\,\Phi\!\left(\frac{S_0 - K}{\sigma\sqrt{T}}\right)
    $$

    which is precisely Bachelier's formula. $\square$

---
**Exercise 3.** Boness's formula has $\mu$ where the Black-Scholes formula has $r$. If a stock has expected return $\mu = 12\%$, risk-free rate $r = 4\%$, $S_0 = 100$, $K = 100$, $T = 1$, and $\sigma = 25\%$, compute the call price under both Boness's formula and the Black-Scholes formula. What is the percentage difference? Explain why the Black-Scholes price is the correct arbitrage-free price regardless of $\mu$.

??? success "Solution to Exercise 3"
    The Black-Scholes formula for a European call is $C = S_0\,\Phi(d_1) - Ke^{-rT}\,\Phi(d_2)$ with:

    $$
    d_1 = \frac{\ln(S_0/K) + (r + \frac{1}{2}\sigma^2)T}{\sigma\sqrt{T}}, \quad d_2 = d_1 - \sigma\sqrt{T}
    $$

    Boness's formula: $C_{\text{Boness}} = S_0\,\Phi(d_1^B) - Ke^{-\mu T}\,\Phi(d_2^B)$ with $\mu$ replacing $r$ in the $d_1, d_2$ expressions.

    With $\mu = 0.12$, $r = 0.04$, $S_0 = 100$, $K = 100$, $T = 1$, $\sigma = 0.25$:

    **Black-Scholes**:

    $$
    d_1 = \frac{0 + (0.04 + 0.03125)}{0.25} = \frac{0.07125}{0.25} = 0.285, \quad d_2 = 0.285 - 0.25 = 0.035
    $$

    $$
    C_{\text{BS}} = 100 \times \Phi(0.285) - 100e^{-0.04}\Phi(0.035) = 100(0.6121) - 96.08(0.5140) \approx 61.21 - 49.38 = 11.83
    $$

    **Boness**:

    $$
    d_1^B = \frac{0 + (0.12 + 0.03125)}{0.25} = \frac{0.15125}{0.25} = 0.605, \quad d_2^B = 0.605 - 0.25 = 0.355
    $$

    $$
    C_{\text{Boness}} = 100 \times \Phi(0.605) - 100e^{-0.12}\Phi(0.355) = 100(0.7274) - 88.69(0.6388) \approx 72.74 - 56.64 = 16.10
    $$

    The percentage difference is $(16.10 - 11.83)/11.83 \approx 36\%$. Boness's formula significantly overprices the call.

    **Why the Black-Scholes price is correct**: The Black-Scholes price is the arbitrage-free price because the option can be replicated by a self-financing portfolio of stock and bonds that costs $C_{\text{BS}}$ to set up. The replicating argument shows that the drift $\mu$ cancels when the portfolio is delta-hedged: the hedged portfolio is risk-free and must earn rate $r$ by no-arbitrage. Any price different from $C_{\text{BS}}$ creates an arbitrage opportunity regardless of $\mu$. Boness's formula gives the wrong price because it discounts at $\mu$ instead of $r$, conflating the stock's risk premium with the relevant discount rate for a replicable (and hence risk-free) payoff.

---
**Exercise 4.** The hedging argument shows that in a portfolio $\Pi = V - \Delta S$, choosing $\Delta = \partial V / \partial S$ eliminates the $dW_t$ term. Starting from $dV = \frac{\partial V}{\partial t}dt + \frac{\partial V}{\partial S}dS + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2}dt$, carry out the full derivation to arrive at the Black-Scholes PDE. Identify precisely where the drift $\mu$ cancels and explain the economic reason for this cancellation.

??? success "Solution to Exercise 4"
    Starting from the Ito expansion of the option price:

    $$
    dV = \frac{\partial V}{\partial t}dt + \frac{\partial V}{\partial S}dS + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2}dt
    $$

    Substitute $dS = \mu S\,dt + \sigma S\,dW_t$:

    $$
    dV = \left(\frac{\partial V}{\partial t} + \mu S\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2}\right)dt + \sigma S\frac{\partial V}{\partial S}\,dW_t
    $$

    The portfolio $\Pi = V - \Delta S$ has change:

    $$
    d\Pi = dV - \Delta\,dS = \left(\frac{\partial V}{\partial t} + \mu S\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2}\right)dt + \sigma S\frac{\partial V}{\partial S}\,dW_t - \Delta(\mu S\,dt + \sigma S\,dW_t)
    $$

    Collecting the $dW_t$ terms: $\sigma S(\frac{\partial V}{\partial S} - \Delta)\,dW_t$. Setting $\Delta = \frac{\partial V}{\partial S}$ eliminates all randomness:

    $$
    d\Pi = \left(\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2}\right)dt
    $$

    **This is where $\mu$ cancels**: the $\mu S \frac{\partial V}{\partial S}$ term from $dV$ is exactly offset by $-\Delta \cdot \mu S\,dt = -\frac{\partial V}{\partial S}\mu S\,dt$ from $-\Delta\,dS$. The drift cancels because the hedge eliminates exposure to the stock's directional movement.

    Since $\Pi$ is risk-free, no-arbitrage requires $d\Pi = r\Pi\,dt = r(V - \frac{\partial V}{\partial S}S)\,dt$:

    $$
    \frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} = rV - rS\frac{\partial V}{\partial S}
    $$

    Rearranging:

    $$
    \frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + rS\frac{\partial V}{\partial S} - rV = 0
    $$

    **Economic reason for the cancellation**: Once the portfolio is hedged, its return is deterministic regardless of which direction the stock moves. A risk-free portfolio must earn the risk-free rate $r$ by no-arbitrage. The expected return $\mu$ is irrelevant because the hedge eliminates the stock's risk, and with it, any compensation for bearing that risk.

---
**Exercise 5.** Harrison and Kreps (1979) established that absence of arbitrage is equivalent to the existence of an equivalent martingale measure. In the Black-Scholes market with one stock and one bond, explain why the market is complete (i.e., every contingent claim is replicable) and why this implies the risk-neutral measure $\mathbb{Q}$ is unique. What would change if the market had two independent sources of randomness but only one risky asset?

??? success "Solution to Exercise 5"
    **Implied volatility** is the value of $\sigma$ that, when substituted into the Black-Scholes formula, produces a model price equal to the observed market price. Formally, given a market price $C_{\text{mkt}}$ for a European call with known $S_0, K, T, r$, the implied volatility $\sigma_{\text{imp}}$ solves:

    $$
    C_{\text{BS}}(S_0, K, T, r, \sigma_{\text{imp}}) = C_{\text{mkt}}
    $$

    Since the Black-Scholes price is strictly increasing in $\sigma$ (positive vega), this equation has a unique solution for any valid market price.

    **Inconsistency with constant $\sigma$**: If the true underlying dynamics were GBM with constant $\sigma$, then the Black-Scholes formula would produce correct prices for *all* strikes and maturities using the same $\sigma$. Therefore, the implied volatility obtained by inverting the formula would be the same constant $\sigma$ for every $(K, T)$ pair. A non-flat implied volatility surface --- where $\sigma_{\text{imp}}(K, T)$ varies across strikes and maturities --- demonstrates that the market prices options as if the underlying distribution is *not* log-normal. The smile/skew indicates heavier tails (especially on the downside) than GBM predicts.

    **Two post-1987 models**:

    1. **Heston stochastic volatility model (1993)**: Models volatility as a separate mean-reverting stochastic process ($dv_t = \kappa(\theta - v_t)dt + \xi\sqrt{v_t}dW_t^{(2)}$) correlated with the stock price. The random volatility produces fatter tails in the return distribution, and negative correlation between stock returns and volatility generates the downside skew. Admits a semi-analytical (Fourier-based) pricing formula.

    2. **Dupire local volatility model (1994)**: Replaces constant $\sigma$ with a deterministic function $\sigma(S, t)$ of the stock price and time. The local volatility surface is uniquely determined by the observed market option prices via Dupire's formula. This model exactly reproduces the entire implied volatility surface by construction, but it lacks the dynamics of stochastic volatility (e.g., it does not produce realistic forward smile dynamics).

---
**Exercise 6.** The volatility smile emerged after the 1987 crash. Before the crash, implied volatilities across strikes were approximately flat. Explain what "implied volatility" means in terms of the Black-Scholes formula, and discuss why a non-flat implied volatility surface is inconsistent with the constant-$\sigma$ assumption of GBM. Name two post-1987 models from the table in the text and briefly describe how each addresses the smile phenomenon.

??? success "Solution to Exercise 6"
    Under Bachelier's model, $C = (S_0 - K)\Phi(d) + \sigma\sqrt{T}\,\phi(d)$ where $d = (S_0 - K)/(\sigma\sqrt{T})$.

    Under the Black-Scholes formula, $C = S_0\Phi(d_1) - Ke^{-rT}\Phi(d_2)$.

    **Derivation of Bachelier from $\mathbb{E}[(S_T - K)^+]$**:

    Since Bachelier assumed zero interest rate and zero drift, $S_T = S_0 + \sigma W_T \sim \mathcal{N}(S_0, \sigma^2 T)$, and the call price is simply the undiscounted expectation $\mathbb{E}[(S_T - K)^+]$.

    Writing $S_T = S_0 + \sigma\sqrt{T}Z$ with $Z \sim \mathcal{N}(0,1)$, the payoff is positive when $Z > -(S_0-K)/(\sigma\sqrt{T}) = -d$:

    $$
    C = \int_{-d}^{\infty}(S_0 + \sigma\sqrt{T}z - K)\phi(z)\,dz
    $$

    $$
    = (S_0 - K)\int_{-d}^{\infty}\phi(z)\,dz + \sigma\sqrt{T}\int_{-d}^{\infty}z\,\phi(z)\,dz
    $$

    The first integral gives $(S_0 - K)\Phi(d)$. For the second, use $\int_{-d}^{\infty}z\phi(z)\,dz = \phi(-d) = \phi(d)$. Therefore:

    $$
    C = (S_0 - K)\Phi(d) + \sigma\sqrt{T}\,\phi(d)
    $$

    This confirms Bachelier's formula. The key difference from Black-Scholes is that Bachelier prices under a normal (not log-normal) distribution, uses no discounting ($r = 0$), and the result depends on the preference-free expectation only because Bachelier implicitly assumed that the market price of risk is zero (equivalent to the physical measure coinciding with the risk-neutral measure when $r = 0$ and $\mu = 0$).
