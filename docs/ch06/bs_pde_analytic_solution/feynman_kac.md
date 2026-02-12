# Feynman-Kac Formula and the Black-Scholes Solution


The **Feynman-Kac formula** provides a profound connection between **partial differential equations** and **probability theory**. It transforms a parabolic PDE into a probabilistic expectation, enabling the derivation of the Black-Scholes formula through stochastic analysis rather than PDE methods.

This section presents the general Feynman-Kac theorem, applies it rigorously to the Black-Scholes PDE, and derives the closed-form option pricing formulas through detailed probabilistic calculations.

---

## The General Feynman-Kac Theorem


### 1. **Statement**


Consider a stochastic process $X_t$ satisfying the stochastic differential equation:

$$
dX_t = \mu(X_t, t)dt + \sigma(X_t, t)dW_t
$$

Let $u(x,t)$ be a function solving the parabolic PDE:

$$
\frac{\partial u}{\partial t} + \mu(x,t)\frac{\partial u}{\partial x} + \frac{1}{2}\sigma^2(x,t)\frac{\partial^2 u}{\partial x^2} - r(x,t)u + f(x,t) = 0
$$

with terminal condition:
$$
u(x,T) = \Phi(x)
$$

**Then the Feynman-Kac formula states:**

$$
\boxed{u(x,t) = \mathbb{E}\left[\int_t^T e^{-\int_t^s r(X_\tau,\tau)d\tau}f(X_s,s)ds + e^{-\int_t^T r(X_\tau,\tau)d\tau}\Phi(X_T) \mid X_t = x\right]}
$$

### 2. **Interpretation of Terms**


**1. Terminal condition term**:
$$
e^{-\int_t^T r(X_\tau,\tau)d\tau}\Phi(X_T)
$$

This represents the **discounted terminal payoff** at maturity $T$.

**2. Running cost/reward term**:
$$
\int_t^T e^{-\int_t^s r(X_\tau,\tau)d\tau}f(X_s,s)ds
$$

This represents **accumulated discounted cash flows** between $t$ and $T$.

**3. For option pricing**:
- $f \equiv 0$ (no intermediate cash flows for European options)
- $r$ is constant (risk-free rate)
- $\Phi(X_T)$ is the option payoff at maturity

The formula simplifies to:
$$
u(x,t) = \mathbb{E}\left[e^{-r(T-t)}\Phi(X_T) \mid X_t = x\right]
$$

This is the **risk-neutral valuation formula**.

---

## Application to Black-Scholes


### 1. **The Setup**


Under the **risk-neutral measure** $\mathbb{Q}$, the stock price dynamics are:

$$
dS_t = rS_t dt + \sigma S_t dW_t^{\mathbb{Q}}
$$

where:
- $r$ = constant risk-free rate
- $\sigma$ = constant volatility
- $W_t^{\mathbb{Q}}$ = Brownian motion under $\mathbb{Q}$

### 2. **The Black-Scholes PDE**


The option value $V(S,t)$ satisfies:

$$
\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2\frac{\partial^2 V}{\partial S^2} - rV = 0
$$

with terminal condition:
$$
V(S,T) = \Phi(S)
$$

where $\Phi(S)$ is the option payoff:
- European call: $\Phi(S) = (S-K)^+$
- European put: $\Phi(S) = (K-S)^+$

### 3. **Feynman-Kac Representation**


By the Feynman-Kac formula:

$$
\boxed{V(S,t) = e^{-r(T-t)}\mathbb{E}^{\mathbb{Q}}[\Phi(S_T) \mid S_t = S]}
$$

**Interpretation**: The option value is the **expected discounted payoff** under the risk-neutral measure.

This converts the PDE problem into a probabilistic expectation problem.

---

## Rigorous Derivation of Feynman-Kac


We now prove the Feynman-Kac formula rigorously using Itô's lemma and martingale theory.

### 1. **Step 1: Apply Itô's Lemma to $u(X_t, t)$**


For a function $u(X_t, t)$ where $dX_t = \mu dt + \sigma dW_t$, Itô's lemma gives:

$$
du = \frac{\partial u}{\partial t}dt + \frac{\partial u}{\partial x}dX_t + \frac{1}{2}\frac{\partial^2 u}{\partial x^2}(dX_t)^2
$$

Since $(dX_t)^2 = \sigma^2 dt$:

$$
du = \left[\frac{\partial u}{\partial t} + \mu\frac{\partial u}{\partial x} + \frac{1}{2}\sigma^2\frac{\partial^2 u}{\partial x^2}\right]dt + \sigma\frac{\partial u}{\partial x}dW_t
$$

### 2. **Step 2: Introduce Discounting**


Define the **discounted value**:
$$
Y_t = e^{-\int_0^t r(X_s,s)ds}u(X_t,t)
$$

Apply the product rule (Itô's lemma for products):

$$
dY_t = d\left(e^{-\int_0^t r ds}\right) \cdot u + e^{-\int_0^t r ds} \cdot du
$$

The discount factor satisfies:
$$
d\left(e^{-\int_0^t r ds}\right) = -r(X_t,t)e^{-\int_0^t r ds}dt
$$

Therefore:

$$
\begin{aligned}
dY_t &= -re^{-\int_0^t r ds}u \cdot dt + e^{-\int_0^t r ds}\left[\frac{\partial u}{\partial t} + \mu\frac{\partial u}{\partial x} + \frac{1}{2}\sigma^2\frac{\partial^2 u}{\partial x^2}\right]dt \\
&\quad + e^{-\int_0^t r ds}\sigma\frac{\partial u}{\partial x}dW_t
\end{aligned}
$$

Combining:

$$
dY_t = e^{-\int_0^t r ds}\left[\frac{\partial u}{\partial t} + \mu\frac{\partial u}{\partial x} + \frac{1}{2}\sigma^2\frac{\partial^2 u}{\partial x^2} - ru\right]dt + e^{-\int_0^t r ds}\sigma\frac{\partial u}{\partial x}dW_t
$$

### 3. **Step 3: Use the PDE Condition**


If $u$ satisfies the Feynman-Kac PDE (with $f=0$):

$$
\frac{\partial u}{\partial t} + \mu\frac{\partial u}{\partial x} + \frac{1}{2}\sigma^2\frac{\partial^2 u}{\partial x^2} - ru = 0
$$

Then the drift term vanishes:

$$
\boxed{dY_t = e^{-\int_0^t r ds}\sigma\frac{\partial u}{\partial x}dW_t}
$$

**Key observation**: $Y_t$ is a **martingale** (has no $dt$ term, only $dW_t$ term).

### 4. **Step 4: Take Conditional Expectation**


Since $Y_t$ is a martingale:

$$
\mathbb{E}[Y_T \mid \mathcal{F}_t] = Y_t
$$

Expanding:

$$
\mathbb{E}\left[e^{-\int_0^T r ds}u(X_T,T) \mid \mathcal{F}_t\right] = e^{-\int_0^t r ds}u(X_t,t)
$$

Using the terminal condition $u(X_T,T) = \Phi(X_T)$:

$$
e^{-\int_0^t r ds}u(X_t,t) = \mathbb{E}\left[e^{-\int_0^T r ds}\Phi(X_T) \mid \mathcal{F}_t\right]
$$

Multiply both sides by $e^{\int_0^t r ds}$:

$$
u(X_t,t) = \mathbb{E}\left[e^{-\int_t^T r ds}\Phi(X_T) \mid \mathcal{F}_t\right]
$$

**This is the Feynman-Kac representation.**

### 5. **Application to Black-Scholes**


For the Black-Scholes case with constant $r$:
- $X_t = S_t$
- $\mu(S_t, t) = rS_t$
- $\sigma(S_t, t) = \sigma S_t$
- $r(S_t, t) = r$

The Feynman-Kac formula gives:

$$
V(S,t) = e^{-r(T-t)}\mathbb{E}^{\mathbb{Q}}[\Phi(S_T) \mid S_t = S]
$$

with terminal conditions:
- European call: $\Phi(S) = (S-K)^+$
- European put: $\Phi(S) = (K-S)^+$

**Conclusion**: Any solution to the Black-Scholes PDE can be represented as a risk-neutral expectation.

---

## Solving the SDE: Distribution of $S_T$


To evaluate the expectation in the Feynman-Kac formula, we need the distribution of $S_T$.

### 1. **The Stochastic Differential Equation**


Under the risk-neutral measure:
$$
dS_t = rS_t dt + \sigma S_t dW_t^{\mathbb{Q}}
$$

### 2. **Apply Itô's Lemma to $\ln S_t$**


Let $f(S) = \ln S$. Then:
$$
\frac{\partial f}{\partial S} = \frac{1}{S}, \quad \frac{\partial^2 f}{\partial S^2} = -\frac{1}{S^2}
$$

By Itô's lemma:
$$
d(\ln S_t) = \frac{1}{S_t}dS_t - \frac{1}{2}\frac{1}{S_t^2}(dS_t)^2
$$

Substituting $dS_t = rS_t dt + \sigma S_t dW_t$ and $(dS_t)^2 = \sigma^2 S_t^2 dt$:

$$
d(\ln S_t) = \frac{1}{S_t}(rS_t dt + \sigma S_t dW_t) - \frac{1}{2}\frac{1}{S_t^2}\sigma^2 S_t^2 dt
$$

$$
= rdt + \sigma dW_t - \frac{1}{2}\sigma^2 dt
$$

$$
= \left(r - \frac{1}{2}\sigma^2\right)dt + \sigma dW_t^{\mathbb{Q}}
$$

### 3. **Integrate from $t$ to $T$**


$$
\ln S_T - \ln S_t = \left(r - \frac{1}{2}\sigma^2\right)(T-t) + \sigma(W_T^{\mathbb{Q}} - W_t^{\mathbb{Q}})
$$

Since $W_T^{\mathbb{Q}} - W_t^{\mathbb{Q}} \sim \mathcal{N}(0, T-t)$, we can write:
$$
W_T^{\mathbb{Q}} - W_t^{\mathbb{Q}} = \sqrt{T-t} \cdot Z
$$

where $Z \sim \mathcal{N}(0,1)$.

### 4. **Explicit Solution**


$$
\boxed{S_T = S_t \exp\left[\left(r - \frac{1}{2}\sigma^2\right)(T-t) + \sigma\sqrt{T-t} \cdot Z\right]}
$$

### 5. **Distribution of $S_T$**


Define $\tau = T - t$. Then:

$$
\ln S_T \mid S_t \sim \mathcal{N}\left(\ln S_t + \left(r - \frac{1}{2}\sigma^2\right)\tau, \sigma^2\tau\right)
$$

**Log-normal distribution**: $S_T$ is log-normally distributed with:
- Mean of $\ln S_T$: $\mathbb{E}[\ln S_T | S_t] = \ln S_t + (r - \frac{1}{2}\sigma^2)\tau$
- Variance of $\ln S_T$: $\text{Var}[\ln S_T | S_t] = \sigma^2\tau$

The probability density function:

$$
p(S_T \mid S_t) = \frac{1}{S_T\sigma\sqrt{2\pi\tau}}\exp\left[-\frac{\left(\ln(S_T/S_t) - (r-\frac{\sigma^2}{2})\tau\right)^2}{2\sigma^2\tau}\right]
$$

---

## European Call Option: Detailed Derivation


### 1. **The Pricing Formula via Feynman-Kac**


For a European call with payoff $\Phi(S) = (S-K)^+$:

$$
C(S,t) = e^{-r\tau}\mathbb{E}^{\mathbb{Q}}[(S_T - K)^+ \mid S_t = S]
$$

where $\tau = T - t$.

### 2. **Step 1: Rewrite as Integral**


$$
C(S,t) = e^{-r\tau}\int_K^{\infty}(S_T - K)p(S_T \mid S)dS_T
$$

### 3. **Step 2: Split the Integral**


$$
C(S,t) = e^{-r\tau}\left[\int_K^{\infty}S_T p(S_T \mid S)dS_T - K\int_K^{\infty}p(S_T \mid S)dS_T\right]
$$

$$
= e^{-r\tau}\left[I_1 - K \cdot I_2\right]
$$

We need to evaluate two integrals.

### 4. **Step 3: Change to Log-Normal Variable**


Since $\ln S_T \sim \mathcal{N}(m, v^2)$ where:
- $m = \ln S + (r - \frac{\sigma^2}{2})\tau$
- $v = \sigma\sqrt{\tau}$

Set $y = \ln S_T$, so $S_T = e^y$ and $dS_T = e^y dy$.

The density becomes:
$$
p(S_T)dS_T = \frac{1}{v\sqrt{2\pi}}e^{-\frac{(y-m)^2}{2v^2}}dy
$$

Both integrals transform to:

**Integral $I_2$**:
$$
I_2 = \int_K^{\infty}p(S_T)dS_T = \int_{\ln K}^{\infty}\frac{1}{v\sqrt{2\pi}}e^{-\frac{(y-m)^2}{2v^2}}dy
$$

**Integral $I_1$**:
$$
I_1 = \int_K^{\infty}S_T p(S_T)dS_T = \int_{\ln K}^{\infty}e^y \frac{1}{v\sqrt{2\pi}}e^{-\frac{(y-m)^2}{2v^2}}dy
$$

### 5. **Step 4: Evaluate $I_2$ (Probability Term)**


Standardize the integral. Let:
$$
Z = \frac{y - m}{v}
$$

Then $y = m + vZ$ and $dy = v dZ$.

When $y = \ln K$: $Z = \frac{\ln K - m}{v}$

When $y = \infty$: $Z = \infty$

Therefore:
$$
I_2 = \int_{\frac{\ln K - m}{v}}^{\infty}\frac{1}{\sqrt{2\pi}}e^{-\frac{Z^2}{2}}dZ = \mathcal{N}\left(-\frac{\ln K - m}{v}\right) = \mathcal{N}\left(\frac{m - \ln K}{v}\right)
$$

Substituting $m = \ln S + (r - \frac{\sigma^2}{2})\tau$ and $v = \sigma\sqrt{\tau}$:

$$
I_2 = \mathcal{N}\left(\frac{\ln(S/K) + (r - \frac{\sigma^2}{2})\tau}{\sigma\sqrt{\tau}}\right)
$$

Define:
$$
\boxed{d_2 = \frac{\ln(S/K) + (r - \frac{\sigma^2}{2})\tau}{\sigma\sqrt{\tau}}}
$$

Then:
$$
I_2 = \mathcal{N}(d_2)
$$

**Interpretation**: $\mathcal{N}(d_2) = \mathbb{Q}(S_T > K)$ is the **risk-neutral probability** that the option expires in-the-money.

### 6. **Step 5: Evaluate $I_1$ (Stock Term)**


$$
I_1 = \int_{\ln K}^{\infty}e^y \frac{1}{v\sqrt{2\pi}}e^{-\frac{(y-m)^2}{2v^2}}dy
$$

**Key technique**: Complete the square in the exponent.

Combine the exponents:
$$
y - \frac{(y-m)^2}{2v^2} = -\frac{1}{2v^2}\left[(y-m)^2 - 2v^2 y\right]
$$

Expand:
$$
(y-m)^2 - 2v^2 y = y^2 - 2ym + m^2 - 2v^2y = y^2 - 2y(m + v^2) + m^2
$$

Complete the square:
$$
= [y - (m+v^2)]^2 - (m+v^2)^2 + m^2
$$

$$
= [y - (m+v^2)]^2 - 2mv^2 - v^4
$$

Therefore:
$$
y - \frac{(y-m)^2}{2v^2} = -\frac{[y-(m+v^2)]^2}{2v^2} + m + \frac{v^2}{2}
$$

Substituting back:
$$
I_1 = e^{m + \frac{v^2}{2}}\int_{\ln K}^{\infty}\frac{1}{v\sqrt{2\pi}}e^{-\frac{[y-(m+v^2)]^2}{2v^2}}dy
$$

This is a Gaussian integral with mean shifted to $m + v^2$:

$$
I_1 = e^{m + \frac{v^2}{2}} \cdot \mathcal{N}\left(\frac{(m+v^2) - \ln K}{v}\right)
$$

Simplify the exponent. Recall:
- $m = \ln S + (r - \frac{\sigma^2}{2})\tau$
- $v^2 = \sigma^2\tau$

$$
m + \frac{v^2}{2} = \ln S + (r - \frac{\sigma^2}{2})\tau + \frac{\sigma^2\tau}{2} = \ln S + r\tau
$$

Therefore:
$$
e^{m + \frac{v^2}{2}} = e^{\ln S + r\tau} = Se^{r\tau}
$$

For the normal CDF argument:
$$
\frac{(m+v^2) - \ln K}{v} = \frac{\ln S + r\tau + \frac{\sigma^2\tau}{2} - \ln K}{\sigma\sqrt{\tau}} = \frac{\ln(S/K) + (r + \frac{\sigma^2}{2})\tau}{\sigma\sqrt{\tau}}
$$

Define:
$$
\boxed{d_1 = \frac{\ln(S/K) + (r + \frac{\sigma^2}{2})\tau}{\sigma\sqrt{\tau}} = d_2 + \sigma\sqrt{\tau}}
$$

Then:
$$
I_1 = Se^{r\tau}\mathcal{N}(d_1)
$$

### 7. **Step 6: Combine Results**


$$
C(S,t) = e^{-r\tau}[I_1 - KI_2]
$$

$$
= e^{-r\tau}\left[Se^{r\tau}\mathcal{N}(d_1) - K\mathcal{N}(d_2)\right]
$$

$$
\boxed{C(S,t) = S\mathcal{N}(d_1) - Ke^{-r\tau}\mathcal{N}(d_2)}
$$

where:

$$
\boxed{d_1 = \frac{\ln(S/K) + (r + \frac{\sigma^2}{2})\tau}{\sigma\sqrt{\tau}}, \quad d_2 = d_1 - \sigma\sqrt{\tau} = \frac{\ln(S/K) + (r - \frac{\sigma^2}{2})\tau}{\sigma\sqrt{\tau}}}
$$

**This is the Black-Scholes formula for a European call option.**

---

## European Put Option


### 1. **Method 1: Direct Calculation**


For a European put with payoff $\Phi(S) = (K-S)^+$:

$$
P(S,t) = e^{-r\tau}\mathbb{E}^{\mathbb{Q}}[(K - S_T)^+ \mid S_t = S]
$$

$$
= e^{-r\tau}\int_0^K(K - S_T)p(S_T \mid S)dS_T
$$

Following similar calculations (completing the square with reversed integration limits):

$$
\boxed{P(S,t) = Ke^{-r\tau}\mathcal{N}(-d_2) - S\mathcal{N}(-d_1)}
$$

where $d_1$ and $d_2$ are the same as for the call.

### 2. **Method 2: Put-Call Parity**


From the no-arbitrage relationship:
$$
C - P = S - Ke^{-r\tau}
$$

Therefore:
$$
P = C - S + Ke^{-r\tau}
$$

$$
= S\mathcal{N}(d_1) - Ke^{-r\tau}\mathcal{N}(d_2) - S + Ke^{-r\tau}
$$

$$
= S(\mathcal{N}(d_1) - 1) + Ke^{-r\tau}(1 - \mathcal{N}(d_2))
$$

Using $\mathcal{N}(-x) = 1 - \mathcal{N}(x)$:

$$
P = -S\mathcal{N}(-d_1) + Ke^{-r\tau}\mathcal{N}(-d_2)
$$

$$
\boxed{P(S,t) = Ke^{-r\tau}\mathcal{N}(-d_2) - S\mathcal{N}(-d_1)}
$$

Both methods yield the same formula. ✓

---

## Probabilistic Interpretation


### 1. **The Two Terms in the Call Formula**


$$
C = \underbrace{S\mathcal{N}(d_1)}_{\text{Stock term}} - \underbrace{Ke^{-r\tau}\mathcal{N}(d_2)}_{\text{Strike term}}
$$

### 2. **Meaning of $\mathcal{N}(d_2)$**


$$
\boxed{\mathcal{N}(d_2) = \mathbb{Q}(S_T > K \mid S_t = S)}
$$

This is the **risk-neutral probability** that the option expires in-the-money.

**Derivation**: From our calculation of $I_2$, we showed:
$$
\int_K^{\infty}p(S_T)dS_T = \mathbb{Q}(S_T > K) = \mathcal{N}(d_2)
$$

### 3. **Meaning of $\mathcal{N}(d_1)$**


$\mathcal{N}(d_1)$ represents the probability of exercise under the **stock measure** $\mathbb{Q}^S$:

$$
\boxed{\mathcal{N}(d_1) = \mathbb{Q}^S(S_T > K \mid S_t = S)}
$$

**Change of numeraire interpretation**: Under the stock as numeraire, the stock price dynamics shift:

$$
\frac{dS_t}{S_t} = (r + \sigma^2)dt + \sigma dW_t^{\mathbb{Q}^S}
$$

The drift changes by $\sigma^2$ (via Girsanov's theorem), which explains the relationship:
$$
d_1 = d_2 + \sigma\sqrt{\tau}
$$

**Alternative interpretation**: $\mathcal{N}(d_1)$ is also the **delta** (hedge ratio) of the call option:
$$
\Delta_{\text{call}} = \frac{\partial C}{\partial S} = \mathcal{N}(d_1)
$$

### 4. **Decomposition of Call Value**


The call formula can be written as:

$$
C = S \cdot \mathbb{Q}^S(S_T > K) - Ke^{-r\tau} \cdot \mathbb{Q}(S_T > K)
$$

**Interpretation**:
- First term: Expected value of stock received upon exercise (under stock measure)
- Second term: Expected present value of strike paid upon exercise (under risk-neutral measure)

The difference between the two measures accounts for the convexity of the payoff.

---

## Connection to Kolmogorov Equations


### 1. **Backward Equation**


The Black-Scholes PDE is the **Kolmogorov backward equation** for the process $S_t$ under $\mathbb{Q}$:

$$
\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2S^2\frac{\partial^2 V}{\partial S^2} - rV = 0
$$

**"Backward"** because:
- We start from terminal condition $V(S,T) = \Phi(S)$ at time $T$
- We solve backward in time to find $V(S,t)$ for $t < T$
- The PDE describes how the option value evolves as we move backward from maturity

### 2. **Forward Equation (Fokker-Planck)**


The transition density $p(S_T, T \mid S_t, t)$ satisfies the **Kolmogorov forward equation**:

$$
\frac{\partial p}{\partial T} = -\frac{\partial}{\partial S_T}(rS_T p) + \frac{1}{2}\frac{\partial^2}{\partial S_T^2}(\sigma^2 S_T^2 p)
$$

**"Forward"** because:
- Given initial distribution at time $t$
- We evolve forward in time to find distribution at time $T$
- The PDE describes how the probability distribution evolves forward

### 3. **Duality Relationship**


The option value can be expressed as:

$$
V(S,t) = e^{-r\tau}\int_0^{\infty}\Phi(S_T)p(S_T, T \mid S, t)dS_T
$$

**Key insight**:
- The backward equation (PDE for $V$) describes the evolution of functionals
- The forward equation (PDE for $p$) describes the evolution of densities
- They are **dual** to each other through the Feynman-Kac representation

---

## Why Feynman-Kac Works: Deep Intuition


### 1. **The Martingale Property**


Under the risk-neutral measure, the **discounted stock price** is a martingale:

$$
\mathbb{E}^{\mathbb{Q}}[e^{-rt}S_t \mid \mathcal{F}_s] = e^{-rs}S_s \quad \text{for } s \leq t
$$

**Proof**: Since $dS_t = rS_t dt + \sigma S_t dW_t^{\mathbb{Q}}$, we have:
$$
d(e^{-rt}S_t) = e^{-rt}\sigma S_t dW_t^{\mathbb{Q}}
$$

This is a martingale (no drift).

### 2. **Extension to Option Value**


By extension, the **discounted option value** must also be a martingale:

$$
\mathbb{E}^{\mathbb{Q}}[e^{-rT}V(S_T,T) \mid \mathcal{F}_t] = e^{-rt}V(S_t,t)
$$

At maturity: $V(S_T,T) = \Phi(S_T)$

Therefore:

$$
e^{-rt}V(S_t,t) = \mathbb{E}^{\mathbb{Q}}[e^{-rT}\Phi(S_T) \mid \mathcal{F}_t]
$$

Solving for $V$:

$$
V(S_t,t) = e^{-r(T-t)}\mathbb{E}^{\mathbb{Q}}[\Phi(S_T) \mid \mathcal{F}_t]
$$

**This is the Feynman-Kac representation.**

### 3. **No-Arbitrage = Martingale Measure**


The Feynman-Kac formula is the **mathematical manifestation of no-arbitrage pricing**:

**Fundamental Theorem of Asset Pricing**:
- **No arbitrage** ⟺ Existence of equivalent martingale measure $\mathbb{Q}$
- **Completeness** + No arbitrage ⟺ **Unique** martingale measure

The risk-neutral measure $\mathbb{Q}$ is the unique measure under which:
1. Discounted asset prices are martingales
2. All derivatives can be priced consistently

**Economic interpretation**: Feynman-Kac converts the no-arbitrage condition into an explicit pricing formula.

---

## Extensions and Generalizations


### 1. **With Continuous Dividend Yield**


If the stock pays continuous dividends at rate $q$:

$$
dS_t = (r-q)S_t dt + \sigma S_t dW_t^{\mathbb{Q}}
$$

The Black-Scholes formula becomes:

$$
\boxed{C(S,t) = Se^{-q\tau}\mathcal{N}(d_1) - Ke^{-r\tau}\mathcal{N}(d_2)}
$$

where:

$$
d_1 = \frac{\ln(S/K) + (r - q + \frac{\sigma^2}{2})\tau}{\sigma\sqrt{\tau}}, \quad d_2 = d_1 - \sigma\sqrt{\tau}
$$

**Application**: Foreign exchange options (treat foreign interest rate as dividend yield).

### 2. **With Time-Dependent Parameters**


For time-varying $r(t)$, $\sigma(t)$, $q(t)$:

$$
V(S,t) = \mathbb{E}^{\mathbb{Q}}\left[\exp\left(-\int_t^T r(s)ds\right)\Phi(S_T) \mid S_t = S\right]
$$

where:

$$
S_T = S_t\exp\left[\int_t^T\left(r(s)-q(s)-\frac{\sigma^2(s)}{2}\right)ds + \int_t^T\sigma(s)dW_s^{\mathbb{Q}}\right]
$$

The log-return is normally distributed with:
- Mean: $\int_t^T(r(s) - q(s) - \frac{\sigma^2(s)}{2})ds$
- Variance: $\int_t^T\sigma^2(s)ds$

**Modified $d_1$ and $d_2$**: Replace $r\tau$ with $\int_t^T r(s)ds$ and $\sigma^2\tau$ with $\int_t^T\sigma^2(s)ds$.

### 3. **Multi-Dimensional Case**


For basket options with $n$ assets $S_1, \ldots, S_n$:

$$
V(\mathbf{S},t) = e^{-r\tau}\mathbb{E}^{\mathbb{Q}}[\Phi(\mathbf{S}_T) \mid \mathbf{S}_t = \mathbf{S}]
$$

where $\mathbf{S}_T = (S_1^T, \ldots, S_n^T)$ follows a **multivariate log-normal distribution** with correlation matrix $\rho$.

**Example payoffs**:
- Basket call: $\Phi = (\sum_{i=1}^n w_i S_i^T - K)^+$
- Exchange option: $\Phi = (S_1^T - S_2^T)^+$
- Spread option: $\Phi = (S_1^T - S_2^T - K)^+$

**Evaluation**: Typically requires numerical integration or Monte Carlo simulation.

---

## Summary: Why Feynman-Kac is Powerful


The Feynman-Kac formula provides a profound bridge between analysis and probability:

### 1. **Key Advantages**


**1. Converts PDE to probability**: 
- Often easier to compute expectations than solve PDEs
- Enables intuitive economic interpretation

**2. Enables Monte Carlo simulation**:
- Can estimate $\mathbb{E}^{\mathbb{Q}}[\Phi(S_T)]$ by simulating paths
- Particularly useful for high-dimensional problems

**3. Generalizes naturally**:
- Extends to path-dependent options (average, lookback)
- Works for multiple assets with ease
- Handles time-dependent parameters

**4. Economic interpretation**:
- Risk-neutral valuation has clear meaning
- Connects to no-arbitrage and FTAP
- Probabilities $\mathcal{N}(d_1)$, $\mathcal{N}(d_2)$ have financial significance

**5. Theoretical foundation**:
- Links stochastic calculus with classical PDE theory
- Unifies discrete (binomial) and continuous (BS) models
- Foundation for modern derivative pricing

### 2. **The Big Picture**


The Feynman-Kac formula demonstrates that:

**PDE ⟷ Probability ⟷ Stochastic Process**

are three equivalent perspectives on the same mathematical object:

- **PDE**: Black-Scholes equation
- **Probability**: Risk-neutral expectation
- **Stochastic Process**: Geometric Brownian motion

This trinity underlies modern quantitative finance and enables both theoretical insight and practical computation.

---

## Summary


The Feynman-Kac formula establishes the fundamental connection:

$$
\text{PDE Solution} = \text{Probabilistic Expectation}
$$

**For Black-Scholes**:
$$
V(S,t) = e^{-r(T-t)}\mathbb{E}^{\mathbb{Q}}[\Phi(S_T) \mid S_t = S]
$$

**Derivation steps**:
1. Apply Itô's lemma to discounted $u(X_t,t)$
2. Show it becomes a martingale if $u$ satisfies the PDE
3. Take expectation to get probabilistic representation
4. Solve SDE to find distribution of $S_T$ (log-normal)
5. Evaluate expectation by integrating against density
6. Complete the square to obtain $\mathcal{N}(d_1)$ and $\mathcal{N}(d_2)$ terms

**Black-Scholes formulas**:

**Call**: $C = S\mathcal{N}(d_1) - Ke^{-r\tau}\mathcal{N}(d_2)$

**Put**: $P = Ke^{-r\tau}\mathcal{N}(-d_2) - S\mathcal{N}(-d_1)$

where:
$$
d_1 = \frac{\ln(S/K) + (r + \frac{\sigma^2}{2})\tau}{\sigma\sqrt{\tau}}, \quad d_2 = d_1 - \sigma\sqrt{\tau}
$$

**Interpretation**:
- $\mathcal{N}(d_2)$ = Risk-neutral probability of exercise
- $\mathcal{N}(d_1)$ = Delta = Stock-measure probability of exercise

The Feynman-Kac approach reveals that option pricing is fundamentally about computing expectations under the appropriate probability measure—a perspective that generalizes far beyond the simple Black-Scholes model to the entire landscape of derivative pricing.
