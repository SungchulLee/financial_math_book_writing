# Girsanov's Theorem: Statement, Proof, and Application to Black-Scholes

Girsanov's theorem is the fundamental tool for **changing probability measures** while preserving the Brownian motion structure. It's the bridge between the **physical world** (actual probabilities) and the **risk-neutral world** (pricing probabilities).

## Statement of Girsanov's Theorem

### Version 1: Cameron-Martin-Girsanov Theorem

**Theorem (Girsanov):** Let $(\Omega, \mathcal{F}, \{\mathcal{F}_t\}_{t \geq 0}, \mathbb{P})$ be a filtered probability space, and let $W_t$ be a $\mathbb{P}$-Brownian motion. Let $\theta_t$ be an $\{\mathcal{F}_t\}$-adapted process satisfying the **Novikov condition**:

$$\mathbb{E}^{\mathbb{P}}\left[\exp\left(\frac{1}{2}\int_0^T \theta_s^2 \, ds\right)\right] < \infty$$

Define the process:

$$Z_t = \exp\left(-\int_0^t \theta_s \, dW_s - \frac{1}{2}\int_0^t \theta_s^2 \, ds\right)$$

Then:

1. **$Z_t$ is a martingale** under $\mathbb{P}$ with $\mathbb{E}^{\mathbb{P}}[Z_t] = 1$ for all $t \in [0, T]$

2. Define a new probability measure $\mathbb{Q}$ on $\mathcal{F}_T$ by:

$$\frac{d\mathbb{Q}}{d\mathbb{P}}\bigg|_{\mathcal{F}_T} = Z_T$$

Under $\mathbb{Q}$, the process:

$$\boxed{\tilde{W}_t = W_t + \int_0^t \theta_s \, ds}$$

is a **$\mathbb{Q}$-Brownian motion**.

### The Exponential Martingale (Doléans-Dade Exponential)

The process $Z_t$ can be written using the **stochastic exponential** notation:

$$Z_t = \mathcal{E}\left(-\int_0^{\cdot} \theta_s \, dW_s\right)_t$$

where $\mathcal{E}(X)_t$ solves the SDE:

$$d\mathcal{E}(X)_t = \mathcal{E}(X)_t \, dX_t$$

For our case:

$$dZ_t = -Z_t \theta_t \, dW_t$$

with $Z_0 = 1$, where 

$$
X = -\int_0^{\cdot} \theta_s \, dW_s
$$

## Proof of Girsanov's Theorem

The proof has three main steps:
1. Show $Z_t$ is a martingale
2. Show $Z_T$ defines a valid probability measure
3. Show $\tilde{W}_t$ is a Brownian motion under $\mathbb{Q}$

### Step 1: $Z_t$ is a Martingale

The process $Z_t$ satisfies the SDE:

$$dZ_t = -Z_t \theta_t \, dW_t$$

This is a **driftless** SDE, so by Itô's formula, $Z_t$ is a **local martingale**.

To show it's a **true martingale**, we use the **Novikov condition**:

$$\mathbb{E}^{\mathbb{P}}\left[\exp\left(\frac{1}{2}\int_0^T \theta_s^2 \, ds\right)\right] < \infty$$

This condition is **sufficient** (but not necessary) to ensure:

$$\mathbb{E}^{\mathbb{P}}[Z_t] = Z_0 = 1 \quad \text{for all } t \in [0, T]$$

**Proof of martingale property:**

Define $M_t = \int_0^t \theta_s \, dW_s$. Then:

$$Z_t = \exp\left(-M_t - \frac{1}{2}\langle M \rangle_t\right) = \exp\left(-M_t - \frac{1}{2}\int_0^t \theta_s^2 \, ds\right)$$

By Itô's lemma for $f(M, t) = \exp(-M - \frac{1}{2}\int_0^t \theta_s^2 \, ds)$:

$$dZ_t = Z_t \left[-dM_t - \frac{1}{2}\theta_t^2 \, dt + \frac{1}{2}(dM_t)^2\right]$$

Since $dM_t = \theta_t \, dW_t$ and $(dM_t)^2 = \theta_t^2 \, dt$:

$$dZ_t = Z_t \left[-\theta_t \, dW_t - \frac{1}{2}\theta_t^2 \, dt + \frac{1}{2}\theta_t^2 \, dt\right] = -Z_t \theta_t \, dW_t$$

The **drift vanishes**, so $Z_t$ is a local martingale.

Under Novikov's condition, we can show that $Z_t$ is **uniformly integrable**, hence a true martingale with:

$$\mathbb{E}^{\mathbb{P}}[Z_T | \mathcal{F}_t] = Z_t$$

### Step 2: $\mathbb{Q}$ is a Valid Probability Measure

Define:

$$\mathbb{Q}(A) = \int_A Z_T \, d\mathbb{P} \quad \text{for } A \in \mathcal{F}_T$$

**Verification:**

1. **Non-negativity:** $Z_T \geq 0$ by construction (exponential is always positive) ✓

2. **Normalization:** $\mathbb{Q}(\Omega) = \mathbb{E}^{\mathbb{P}}[Z_T] = 1$ (using the martingale property and $Z_0 = 1$) ✓ 

3. **Equivalence:** $\mathbb{Q} \sim \mathbb{P}$ because
$Z_T > 0$ and hence $\mathbb{Q}(A) = 0 \iff \mathbb{P}(A) = 0$ ✓

So $\mathbb{Q}$ is an **equivalent probability measure**.

### Step 3: $\tilde{W}_t$ is a $\mathbb{Q}$-Brownian Motion

Define:

$$\tilde{W}_t = W_t + \int_0^t \theta_s \, ds$$

We need to verify three properties:

**Property 1: $\tilde{W}_0 = 0$** ✓ (obvious)

**Property 2: $\tilde{W}_t$ has continuous paths** ✓ (sum of continuous processes)

**Property 3: $\tilde{W}_t$ is a $\mathbb{Q}$-martingale with quadratic variation $t$**

This is the **key step**. We'll use the **martingale characterization of Brownian motion** (Lévy's theorem):

> A continuous adapted process $M_t$ with $M_0 = 0$ and $\langle M \rangle_t = t$ is a Brownian motion.

**Proof that $\tilde{W}_t$ is a $\mathbb{Q}$-martingale:**

For $s < t$, we need:

$$\mathbb{E}^{\mathbb{Q}}[\tilde{W}_t | \mathcal{F}_s] = \tilde{W}_s$$

By the definition of expectation under $\mathbb{Q}$:

$$\mathbb{E}^{\mathbb{Q}}[\tilde{W}_t | \mathcal{F}_s] = \frac{\mathbb{E}^{\mathbb{P}}[Z_T \tilde{W}_t | \mathcal{F}_s]}{\mathbb{E}^{\mathbb{P}}[Z_T | \mathcal{F}_s]} = \frac{\mathbb{E}^{\mathbb{P}}[Z_T \tilde{W}_t | \mathcal{F}_s]}{Z_s}$$

We need to show this equals $\tilde{W}_s$.

**Key computation:** Consider the process $Z_t \tilde{W}_t$. By Itô's product rule:

$$d(Z_t \tilde{W}_t) = \tilde{W}_t \, dZ_t + Z_t \, d\tilde{W}_t + dZ_t \cdot d\tilde{W}_t$$

We have:
- $dZ_t = -Z_t \theta_t \, dW_t$
- $d\tilde{W}_t = dW_t + \theta_t \, dt$

Therefore:

$$dZ_t \cdot d\tilde{W}_t = (-Z_t \theta_t \, dW_t) \cdot (dW_t + \theta_t \, dt) = -Z_t \theta_t \, dt$$

So:

$$\begin{array}{lll}
\displaystyle d(Z_t \tilde{W}_t) 
&=&\displaystyle \tilde{W}_t(-Z_t \theta_t \, dW_t) + Z_t(dW_t + \theta_t \, dt) - Z_t \theta_t \, dt\\
&=&\displaystyle -Z_t \tilde{W}_t \theta_t \, dW_t + Z_t \, dW_t + Z_t \theta_t \, dt - Z_t \theta_t \, dt\\
&=&\displaystyle Z_t(1 - \tilde{W}_t \theta_t) \, dW_t
\end{array}$$

This is a **driftless** process! Therefore $Z_t \tilde{W}_t$ is a $\mathbb{P}$-martingale.

Hence:

$$\mathbb{E}^{\mathbb{P}}[Z_T \tilde{W}_T | \mathcal{F}_s] = Z_s \tilde{W}_s$$

Dividing by $Z_s$:

$$\mathbb{E}^{\mathbb{Q}}[\tilde{W}_T | \mathcal{F}_s] = \tilde{W}_s$$

So $\tilde{W}_t$ is a $\mathbb{Q}$-martingale. ✓

**Quadratic variation:**

$$\langle \tilde{W} \rangle_t = \langle W + \int_0^{\cdot} \theta_s \, ds \rangle_t = \langle W \rangle_t = t$$

(since the bounded variation term contributes nothing to quadratic variation)

By **Lévy's theorem**, $\tilde{W}_t$ is a $\mathbb{Q}$-Brownian motion. ✓

This completes the proof of Girsanov's theorem. $\square$

## Intuition Behind Girsanov's Theorem

### What Does It Do?

Girsanov's theorem allows us to **change the drift** of a diffusion process by changing the probability measure:

**Under $\mathbb{P}$:**

$$dX_t = \mu_t \, dt + \sigma_t \, dW_t$$

**Under $\mathbb{Q}$ (with $\theta_t = -\frac{\mu_t}{\sigma_t}$):**

$$dX_t = 0 \, dt + \sigma_t \, d\tilde{W}_t = \sigma_t \, d\tilde{W}_t$$

The process becomes **driftless** (a martingale) under the new measure!

### The Radon-Nikodym Derivative

The "cost" of changing measures is encoded in:

$$Z_T = \exp\left(-\int_0^T \theta_s \, dW_s - \frac{1}{2}\int_0^T \theta_s^2 \, ds\right)$$

**Interpretation:**
- Events with $Z_T$ large → Higher probability under $\mathbb{Q}$
- Events with $Z_T$ small → Lower probability under $\mathbb{Q}$
- The exponential form ensures $Z_T > 0$ and $\mathbb{E}[Z_T] = 1$

### Why the Correction Term $-\frac{1}{2}\int \theta_s^2 \, ds$?

This comes from **Itô's lemma**. When we write:

$$\log Z_t = -\int_0^t \theta_s \, dW_s - \frac{1}{2}\int_0^t \theta_s^2 \, ds$$

and apply Itô to get $dZ_t$, the $\frac{1}{2}\theta_t^2$ term exactly cancels the Itô correction from $(dW_t)^2 = dt$, leaving a **driftless** SDE.

Without this term, $Z_t$ would not be a martingale, and $\mathbb{E}[Z_T] \neq 1$.

## Application to Black-Scholes: Physical to Risk-Neutral Measure

Now let's apply Girsanov's theorem to derive the risk-neutral measure in the Black-Scholes model.

### Setup Under Physical Measure $\mathbb{P}$

The stock price follows:

$$dS_t = \mu S_t \, dt + \sigma S_t \, dW_t$$

where:

- $\mu$ = **actual expected return** (what you observe in historical data)

- $\sigma$ = volatility

- $W_t$ = $\mathbb{P}$-Brownian motion

The **discounted stock price** is:

$$\tilde{S}_t = e^{-rt} S_t$$

By Itô's lemma:

$$\begin{array}{lll}
\displaystyle d\tilde{S}_t 
&=&\displaystyle  e^{-rt}[-rS_t \, dt + dS_t]\\
&=&\displaystyle  e^{-rt}[-rS_t + \mu S_t] \, dt + e^{-rt} \sigma S_t \, dW_t\\
&=&\displaystyle  \tilde{S}_t[(\mu - r) \, dt + \sigma \, dW_t]
\end{array}$$


Under $\mathbb{P}$, the discounted price has **drift** $(\mu - r)$, so it's **not a martingale** (unless $\mu = r$, which is generally not true).

### Goal: Find $\mathbb{Q}$ Such That $\tilde{S}_t$ is a Martingale

We want to find a measure $\mathbb{Q} \sim \mathbb{P}$ such that:

$$d\tilde{S}_t = \tilde{S}_t \sigma \, d\tilde{W}_t$$

(driftless, hence a martingale)

This requires changing $dW_t$ to $d\tilde{W}_t$ in a way that **removes the drift** $(\mu - r)$.

### Step 1: Identify the Market Price of Risk

From $d\tilde{S}_t = \tilde{S}_t[(\mu - r) \, dt + \sigma \, dW_t]$, we want to remove the drift $(\mu - r)dt$.

Define the **market price of risk** (also called **Sharpe ratio**):

$$\boxed{\lambda = \frac{\mu - r}{\sigma}}$$

**Economic interpretation:**

- $\lambda$ = excess return per unit of risk

- Measures how much extra return investors demand for bearing one unit of volatility

### Step 2: Apply Girsanov's Theorem

We want to apply Girsanov with constant $\theta_t = \lambda = \frac{\mu - r}{\sigma}$.

Define:

$$Z_t = \exp\left(-\lambda W_t - \frac{\lambda^2 t}{2}\right) = \exp\left(-\frac{\mu - r}{\sigma} W_t - \frac{(\mu-r)^2}{2\sigma^2} t\right)$$

By Girsanov's theorem, under the new measure $\mathbb{Q}$ defined by:

$$\frac{d\mathbb{Q}}{d\mathbb{P}}\bigg|_{\mathcal{F}_t} = Z_t$$

the process:

$$\boxed{W^{\mathbb{Q}}_t = W_t + \lambda t = W_t + \frac{\mu - r}{\sigma} t}$$

is a $\mathbb{Q}$-Brownian motion.

### Step 3: Stock Dynamics Under $\mathbb{Q}$

Substitute $W_t = W^{\mathbb{Q}}_t - \lambda t$ into the stock SDE:


$$\begin{array}{lll}
dS_t 
&=&\displaystyle \mu S_t \, dt + \sigma S_t \, dW_t\\
&=&\displaystyle \mu S_t \, dt + \sigma S_t \, d(W^{\mathbb{Q}}_t - \lambda t)\\
&=&\displaystyle \mu S_t \, dt + \sigma S_t(dW^{\mathbb{Q}}_t - \lambda \, dt)\\
&=&\displaystyle \mu S_t \, dt - \sigma S_t \lambda \, dt + \sigma S_t \, dW^{\mathbb{Q}}_t\\
&=&\displaystyle (\mu - \sigma \lambda) S_t \, dt + \sigma S_t \, dW^{\mathbb{Q}}_t
\end{array}$$

Now substitute $\lambda = \frac{\mu - r}{\sigma}$:

$$\mu - \sigma \lambda = \mu - \sigma \cdot \frac{\mu - r}{\sigma} = \mu - (\mu - r) = r$$

Therefore:

$$\boxed{dS_t = r S_t \, dt + \sigma S_t \, dW^{\mathbb{Q}}_t}$$

**The drift has changed from $\mu$ to $r$!**

### Step 4: Verify Discounted Price is a Martingale

Under $\mathbb{Q}$, the discounted stock price satisfies:

$$
d\tilde{S}_t 
= e^{-rt}[-rS_t \, dt + dS_t]
= e^{-rt}[-rS_t + rS_t] \, dt + e^{-rt} \sigma S_t \, dW^{\mathbb{Q}}_t
$$

$$\boxed{d\tilde{S}_t = \tilde{S}_t \sigma \, dW^{\mathbb{Q}}_t}$$

**No drift!** Therefore $\tilde{S}_t$ is a $\mathbb{Q}$-martingale:

$$\tilde{S}_t = \mathbb{E}^{\mathbb{Q}}[\tilde{S}_T | \mathcal{F}_t]$$

or equivalently:

$$\boxed{S_t = \mathbb{E}^{\mathbb{Q}}[e^{-r(T-t)} S_T | \mathcal{F}_t]}$$

This is the **fundamental asset pricing formula** under the risk-neutral measure!

## Why Does the Drift Change From $\mu$ to $r$?

### Economic Explanation

**Under $\mathbb{P}$ (physical measure):**
- Investors are **risk-averse**
- They demand a risk premium: $\mu - r > 0$
- The stock must grow faster than the risk-free rate on average to compensate for risk
- This is what you observe in **historical data**

**Under $\mathbb{Q}$ (risk-neutral measure):**
- We've **transformed probabilities** to make pricing easier
- Under these transformed probabilities, investors "act as if" they're risk-neutral
- Risk-neutral investors are indifferent between stocks and bonds
- Therefore, **all assets earn the risk-free rate** $r$ on average under $\mathbb{Q}$

**Key insight:** We're not saying investors ARE risk-neutral. We're constructing artificial probabilities under which we can price as if they were.

### Mathematical Explanation

The measure change:

$$dW^{\mathbb{Q}}_t = dW_t + \frac{\mu - r}{\sigma} dt$$

adds a **deterministic drift** that exactly cancels the excess return $\mu - r$:

$$\begin{array}{lll}
dS_t 
&=&\displaystyle \mu S_t \, dt + \sigma S_t \, dW_t\\
&=&\displaystyle r S_t \, dt + \sigma S_t \, \left[dW_t + \frac{\mu - r}{\sigma} dt\right]\\
&=&\displaystyle r S_t \, dt + \sigma S_t \, dW^{\mathbb{Q}}_t
\end{array}$$

The transformation **absorbs the risk premium** into the measure change.

### The Radon-Nikodym Derivative

$$\frac{d\mathbb{Q}}{d\mathbb{P}}\bigg|_{\mathcal{F}_T} = \exp\left(-\frac{\mu-r}{\sigma}W_T - \frac{(\mu-r)^2}{2\sigma^2}T\right)$$

**Interpretation:**
- Paths where $W_T$ is large (stock goes up a lot) → Lower weight under $\mathbb{Q}$
- Paths where $W_T$ is small (stock goes down) → Higher weight under $\mathbb{Q}$

This reweighting **reduces the average growth rate** from $\mu$ to $r$.

Think of it as changing from "physical probabilities" to "pricing probabilities" that incorporate risk aversion.

## Why Are Discounted Prices Martingales Under $\mathbb{Q}$?

This is the heart of **risk-neutral pricing theory**.

### The No-Arbitrage Argument

**Claim:** If markets are arbitrage-free and complete, then there exists a unique measure $\mathbb{Q}$ such that discounted prices are martingales.

**Proof sketch:**
1. Consider a self-financing portfolio with value $V_t$
2. If $\frac{V_t}{B_t}$ is not a martingale, it has predictable drift
3. We can exploit this drift to make risk-free profit (arbitrage)
4. By no-arbitrage, discounted prices must be martingales

### The Fundamental Pricing Formula

If $\tilde{S}_t = e^{-rt}S_t$ is a $\mathbb{Q}$-martingale:

$$e^{-rt}S_t = \mathbb{E}^{\mathbb{Q}}[e^{-rT}S_T | \mathcal{F}_t]$$

Therefore:

$$\boxed{S_t = \mathbb{E}^{\mathbb{Q}}[e^{-r(T-t)}S_T | \mathcal{F}_t]}$$

For a derivative with payoff $\Phi(S_T)$:

$$\boxed{V(t, S_t) = \mathbb{E}^{\mathbb{Q}}[e^{-r(T-t)}\Phi(S_T) | \mathcal{F}_t]}$$

**This is the cornerstone of derivative pricing!**

### Connection to Delta Hedging

The martingale property under $\mathbb{Q}$ is **equivalent** to the existence of a replicating portfolio:

**Martingale approach:** 

$$V_t = \mathbb{E}^{\mathbb{Q}}[e^{-r(T-t)}\Phi(S_T) | \mathcal{F}_t]$$

**Hedging approach:** 

$$V_t = \Delta_t S_t + \beta_t B_t$$

where $\Delta_t = \frac{\partial V}{\partial S}$ is chosen to make the portfolio risk-free.

Both give the same price!

## Verification: Computing Option Prices

### European Call Option

Under $\mathbb{Q}$:

$$C(t, S_t) = \mathbb{E}^{\mathbb{Q}}[e^{-r(T-t)}(S_T - K)^+ | \mathcal{F}_t]$$

Since $dS_t = rS_t \, dt + \sigma S_t \, dW^{\mathbb{Q}}_t$:

$$S_T = S_t \exp\left[\left(r - \frac{\sigma^2}{2}\right)(T-t) + \sigma(W^{\mathbb{Q}}_T - W^{\mathbb{Q}}_t)\right]$$

With $W^{\mathbb{Q}}_T - W^{\mathbb{Q}}_t \sim \mathcal{N}(0, T-t)$, we can compute:

$$C = S_t \Phi(d_1) - Ke^{-r(T-t)}\Phi(d_2)$$

This is the **Black-Scholes formula**, derived purely from the risk-neutral expectation!

### Key Observations

1. **$\mu$ disappeared!** The option price depends only on $r$ and $\sigma$, not on $\mu$

2. **Volatility matters:** Even though drift changed, volatility $\sigma$ stayed the same under both measures

3. **No risk preferences needed:** We don't need to know investor risk aversion to price options

## Summary of the Measure Change

### The Complete Picture

```
Physical World (ℙ)              Risk-Neutral World (ℚ)
─────────────────────────────────────────────────────
Stock: dS = μS dt + σS dW       dS = rS dt + σS dW^ℚ

Disc. stock: drift = (μ-r)      drift = 0 (martingale!)

Investor: risk-averse           "acts" risk-neutral
          demands μ > r          expects all assets → r

Probabilities: actual           pricing probabilities
               observable        constructed

Purpose: describe reality       price derivatives
```

### The Transformation

$$W^{\mathbb{Q}}_t = W_t + \underbrace{\frac{\mu - r}{\sigma}}_{\text{Sharpe ratio}} t$$

$$\frac{d\mathbb{Q}}{d\mathbb{P}} = \exp\left(-\frac{\mu-r}{\sigma}W_T - \frac{(\mu-r)^2}{2\sigma^2}T\right)$$

### Why This Works

1. **Girsanov's theorem** guarantees $W^{\mathbb{Q}}_t$ is a valid Brownian motion under $\mathbb{Q}$

2. The specific choice $\theta = \frac{\mu-r}{\sigma}$ removes the excess return, making drift = $r$

3. Under $\mathbb{Q}$, discounted prices are martingales, enabling easy pricing via expectations

4. The measure $\mathbb{Q}$ encodes all risk aversion into the measure itself, so we can price "as if" investors were risk-neutral

### The Philosophical Point

> **"Risk-neutral pricing doesn't mean investors are risk-neutral. It means we've found clever probabilities that absorb risk preferences, allowing us to price as if investors were risk-neutral."**

The genius of Black-Scholes-Merton was recognizing that through **replication** (delta hedging), derivative prices are **independent of risk preferences** and can be computed using this artificial $\mathbb{Q}$ measure where everything grows at rate $r$.

Girsanov's theorem is the mathematical machinery that makes this transformation rigorous and shows exactly how to change measures to eliminate risk premia from pricing formulas.
