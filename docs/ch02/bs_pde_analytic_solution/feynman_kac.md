# Feynman-Kac Formula: Deep Dive

Let me give you a comprehensive treatment of the Feynman-Kac formula and its application to Black-Scholes.

---

## **1. The General Feynman-Kac Theorem**

### **Statement**

Consider a stochastic process $X_t$ satisfying:

$$dX_t = \mu(X_t, t)dt + \sigma(X_t, t)dW_t$$



Let $u(x,t)$ solve the parabolic PDE:

$$\frac{\partial u}{\partial t} + \mu(x,t)\frac{\partial u}{\partial x} + \frac{1}{2}\sigma^2(x,t)\frac{\partial^2 u}{\partial x^2} - r(x,t)u + f(x,t) = 0$$



with terminal condition $u(x,T) = \Phi(x)$.

**Then the solution is:**

$$u(x,t) = \mathbb{E}\left[\int_t^T e^{-\int_t^s r(X_\tau,\tau)d\tau}f(X_s,s)ds + e^{-\int_t^T r(X_\tau,\tau)d\tau}\Phi(X_T) \mid X_t = x\right]$$



### **Interpretation**

- The term $e^{-\int_t^T r(X_\tau,\tau)d\tau}\Phi(X_T)$ is the **discounted terminal payoff**
- The integral $\int_t^T e^{-\int_t^s r(X_\tau,\tau)d\tau}f(X_s,s)ds$ represents **discounted running costs/rewards**
- For option pricing: $f \equiv 0$ and $r$ is constant

---

## **2. Application to Black-Scholes**

### **The Setup**

Stock price dynamics under **risk-neutral measure** $\mathbb{Q}$:

$$dS_t = rS_t dt + \sigma S_t dW_t^{\mathbb{Q}}$$



The Black-Scholes PDE:

$$\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2\frac{\partial^2 V}{\partial S^2} - rV = 0$$



with $V(S,T) = \Phi(S)$.

### **Feynman-Kac Formula**


$$V(S,t) = e^{-r(T-t)}\mathbb{E}^{\mathbb{Q}}[\Phi(S_T) \mid S_t = S]$$



This is the **risk-neutral valuation formula**: the option value is the expected discounted payoff under the risk-neutral measure.

---

## **3. Rigorous Derivation of Feynman-Kac**

### **Step 1: Apply Itô's Lemma**

For $u(X_t, t)$ where $dX_t = \mu dt + \sigma dW_t$:


$$du = \frac{\partial u}{\partial t}dt + \frac{\partial u}{\partial x}dX_t + \frac{1}{2}\frac{\partial^2 u}{\partial x^2}(dX_t)^2$$




$$= \left[\frac{\partial u}{\partial t} + \mu\frac{\partial u}{\partial x} + \frac{1}{2}\sigma^2\frac{\partial^2 u}{\partial x^2}\right]dt + \sigma\frac{\partial u}{\partial x}dW_t$$



### **Step 2: Add Discounting**

Consider the discounted value $Y_t = e^{-\int_0^t r(X_s,s)ds}u(X_t,t)$.

By the product rule and Itô:

$$dY_t = d(e^{-\int_0^t r ds})u + e^{-\int_0^t r ds}du + d(e^{-\int_0^t r ds})du$$




$$= -re^{-\int_0^t r ds}u \cdot dt + e^{-\int_0^t r ds}\left[\frac{\partial u}{\partial t} + \mu\frac{\partial u}{\partial x} + \frac{1}{2}\sigma^2\frac{\partial^2 u}{\partial x^2}\right]dt + e^{-\int_0^t r ds}\sigma\frac{\partial u}{\partial x}dW_t$$




$$= e^{-\int_0^t r ds}\left[\frac{\partial u}{\partial t} + \mu\frac{\partial u}{\partial x} + \frac{1}{2}\sigma^2\frac{\partial^2 u}{\partial x^2} - ru\right]dt + e^{-\int_0^t r ds}\sigma\frac{\partial u}{\partial x}dW_t$$



### **Step 3: Use the PDE**

If $u$ satisfies the PDE (with $f=0$):

$$\frac{\partial u}{\partial t} + \mu\frac{\partial u}{\partial x} + \frac{1}{2}\sigma^2\frac{\partial^2 u}{\partial x^2} - ru = 0$$



Then:

$$dY_t = e^{-\int_0^t r ds}\sigma\frac{\partial u}{\partial x}dW_t$$



This is a **martingale** (no drift term)!

### **Step 4: Take Expectation**

Since $Y_t$ is a martingale:

$$\mathbb{E}[Y_T \mid \mathcal{F}_t] = Y_t$$




$$\mathbb{E}\left[e^{-\int_0^T r ds}u(X_T,T) \mid \mathcal{F}_t\right] = e^{-\int_0^t r ds}u(X_t,t)$$



With $u(X_T,T) = \Phi(X_T)$:

$$e^{-\int_0^t r ds}u(X_t,t) = \mathbb{E}\left[e^{-\int_0^T r ds}\Phi(X_T) \mid \mathcal{F}_t\right]$$




$$u(X_t,t) = \mathbb{E}\left[e^{-\int_t^T r ds}\Phi(X_T) \mid \mathcal{F}_t\right]$$



**This is the Feynman-Kac representation!**

---

## **4. Explicit Solution for Lognormal Process**

### **Solving the SDE**

Under $\mathbb{Q}$:

$$dS_t = rS_t dt + \sigma S_t dW_t^{\mathbb{Q}}$$



Applying Itô to $\ln S_t$:

$$d(\ln S_t) = \left(r - \frac{\sigma^2}{2}\right)dt + \sigma dW_t^{\mathbb{Q}}$$



Integrating from $t$ to $T$:

$$\ln S_T - \ln S_t = \left(r - \frac{\sigma^2}{2}\right)(T-t) + \sigma(W_T^{\mathbb{Q}} - W_t^{\mathbb{Q}})$$




$$S_T = S_t \exp\left[\left(r - \frac{\sigma^2}{2}\right)(T-t) + \sigma\sqrt{T-t} \cdot Z\right]$$



where $Z \sim N(0,1)$.

### **Key Distribution**


$$\ln\left(\frac{S_T}{S_t}\right) \sim N\left[\left(r - \frac{\sigma^2}{2}\right)(T-t), \sigma^2(T-t)\right]$$



Let $\tau = T-t$. Then:

$$\ln S_T \mid S_t \sim N\left(\ln S_t + \left(r - \frac{\sigma^2}{2}\right)\tau, \sigma^2\tau\right)$$



The density is:

$$p(S_T \mid S_t) = \frac{1}{S_T\sigma\sqrt{2\pi\tau}}\exp\left[-\frac{\left(\ln(S_T/S_t) - (r-\frac{\sigma^2}{2})\tau\right)^2}{2\sigma^2\tau}\right]$$



---

## **5. European Call Option**

### **Payoff and Expectation**

Payoff: $\Phi(S) = (S-K)^+ = \max(S-K, 0)$


$$C(S,t) = e^{-r\tau}\mathbb{E}^{\mathbb{Q}}[(S_T - K)^+ \mid S_t = S]$$




$$= e^{-r\tau}\int_K^{\infty}(S_T - K)p(S_T \mid S)dS_T$$




$$= e^{-r\tau}\left[\int_K^{\infty}S_T p(S_T \mid S)dS_T - K\int_K^{\infty}p(S_T \mid S)dS_T\right]$$



### **Computing the Integrals**

**Define:**

$$d_1 = \frac{\ln(S/K) + (r + \frac{\sigma^2}{2})\tau}{\sigma\sqrt{\tau}}, \quad d_2 = d_1 - \sigma\sqrt{\tau} = \frac{\ln(S/K) + (r - \frac{\sigma^2}{2})\tau}{\sigma\sqrt{\tau}}$$



**First Integral** (using change of variables $y = \ln S_T$):


$$\int_K^{\infty}S_T p(S_T \mid S)dS_T = S \cdot N(d_1)$$



where $N(\cdot)$ is the standard normal CDF.

**Derivation:** Let $y = \ln S_T$, then:

$$\int_{\ln K}^{\infty}e^y \cdot \frac{1}{\sigma\sqrt{2\pi\tau}}\exp\left[-\frac{(y - \ln S - (r-\frac{\sigma^2}{2})\tau)^2}{2\sigma^2\tau}\right]dy$$



Complete the square in the exponent:

$$-\frac{(y - \ln S - (r-\frac{\sigma^2}{2})\tau)^2}{2\sigma^2\tau} + y = -\frac{(y - \ln S - (r+\frac{\sigma^2}{2})\tau)^2}{2\sigma^2\tau} + \ln S + r\tau$$



This gives:

$$e^{\ln S + r\tau}\int_{\ln K}^{\infty}\frac{1}{\sigma\sqrt{2\pi\tau}}\exp\left[-\frac{(y - \ln S - (r+\frac{\sigma^2}{2})\tau)^2}{2\sigma^2\tau}\right]dy = Se^{r\tau}N(d_1)$$



**Second Integral:**

$$\int_K^{\infty}p(S_T \mid S)dS_T = \mathbb{Q}(S_T > K \mid S_t = S) = N(d_2)$$



### **Black-Scholes Call Formula**


$$C(S,t) = e^{-r\tau}\left[Se^{r\tau}N(d_1) - KN(d_2)\right]$$




$$\boxed{C(S,t) = SN(d_1) - Ke^{-r\tau}N(d_2)}$$



where:

$$\boxed{d_1 = \frac{\ln(S/K) + (r + \frac{\sigma^2}{2})\tau}{\sigma\sqrt{\tau}}, \quad d_2 = d_1 - \sigma\sqrt{\tau}}$$



---

## **6. European Put Option**

### **Method 1: Direct Calculation**


$$P(S,t) = e^{-r\tau}\mathbb{E}^{\mathbb{Q}}[(K - S_T)^+ \mid S_t = S]$$




$$= e^{-r\tau}\int_0^K(K - S_T)p(S_T \mid S)dS_T$$



Following similar calculations:


$$\boxed{P(S,t) = Ke^{-r\tau}N(-d_2) - SN(-d_1)}$$



### **Method 2: Put-Call Parity**

From the arbitrage-free relationship:

$$C - P = S - Ke^{-r\tau}$$



Therefore:

$$P = C - S + Ke^{-r\tau} = SN(d_1) - Ke^{-r\tau}N(d_2) - S + Ke^{-r\tau}$$




$$= S(N(d_1) - 1) + Ke^{-r\tau}(1 - N(d_2))$$




$$= -SN(-d_1) + Ke^{-r\tau}N(-d_2)$$



using $N(-x) = 1 - N(x)$.

---

## **7. Probabilistic Interpretation**

### **The Two Terms**

For the call: $C = SN(d_1) - Ke^{-r\tau}N(d_2)$

- **$N(d_2)$**: Probability that option expires in-the-money under $\mathbb{Q}$

  $$N(d_2) = \mathbb{Q}(S_T > K \mid S_t = S)$$



- **$N(d_1)$**: Delta-weighted probability under the **stock measure** $\mathbb{Q}^S$

  $$N(d_1) = \mathbb{Q}^S(S_T > K \mid S_t = S)$$



### **Change of Numeraire Interpretation**

Under the stock as numeraire:

$$\frac{dS_t}{S_t} = (r + \sigma^2)dt + \sigma dW_t^{\mathbb{Q}^S}$$



The drift changes by $\sigma^2$ (Girsanov), which explains why $d_1 = d_2 + \sigma\sqrt{\tau}$.

The call formula becomes:

$$C = S \cdot \mathbb{Q}^S(S_T > K) - Ke^{-r\tau} \cdot \mathbb{Q}(S_T > K)$$



---

## **8. Connection to Kolmogorov Equations**

### **Backward Equation**

The Black-Scholes PDE is the **Kolmogorov backward equation** for the process $S_t$ under $\mathbb{Q}$:


$$\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2S^2\frac{\partial^2 V}{\partial S^2} - rV = 0$$



"Backward" because we're going backwards in time from $T$ to $t$.

### **Forward Equation (Fokker-Planck)**

The transition density $p(S_T, T \mid S_t, t)$ satisfies the **Kolmogorov forward equation**:


$$\frac{\partial p}{\partial T} = -\frac{\partial}{\partial S_T}(rS_T p) + \frac{1}{2}\frac{\partial^2}{\partial S_T^2}(\sigma^2 S_T^2 p)$$



This describes how the probability distribution evolves forward in time.

### **Relationship**


$$V(S,t) = e^{-r\tau}\int_0^{\infty}\Phi(S_T)p(S_T, T \mid S, t)dS_T$$



The backward equation (PDE for $V$) and forward equation (PDE for $p$) are **dual** to each other.

---

## **9. Why Feynman-Kac Works: Deep Intuition**

### **The Martingale Property**

Under the risk-neutral measure, the **discounted stock price** is a martingale:

$$\mathbb{E}^{\mathbb{Q}}[e^{-rt}S_t \mid \mathcal{F}_s] = e^{-rs}S_s$$



By extension, the **discounted option value** must also be a martingale:

$$\mathbb{E}^{\mathbb{Q}}[e^{-rT}V(S_T,T) \mid \mathcal{F}_t] = e^{-rt}V(S_t,t)$$



At maturity: $V(S_T,T) = \Phi(S_T)$

Therefore:

$$e^{-rt}V(S_t,t) = \mathbb{E}^{\mathbb{Q}}[e^{-rT}\Phi(S_T) \mid \mathcal{F}_t]$$




$$V(S_t,t) = e^{-r(T-t)}\mathbb{E}^{\mathbb{Q}}[\Phi(S_T) \mid \mathcal{F}_t]$$



### **No-Arbitrage = Martingale Measure**

The Feynman-Kac formula is the **mathematical manifestation of no-arbitrage pricing**. The existence of an equivalent martingale measure $\mathbb{Q}$ is equivalent to the absence of arbitrage (First Fundamental Theorem of Asset Pricing).

---

## **10. Extensions and Generalizations**

### **With Dividends**

If $dS_t = (r-q)S_t dt + \sigma S_t dW_t^{\mathbb{Q}}$ (continuous dividend yield $q$):


$$C(S,t) = Se^{-q\tau}N(d_1) - Ke^{-r\tau}N(d_2)$$



where:

$$d_1 = \frac{\ln(S/K) + (r - q + \frac{\sigma^2}{2})\tau}{\sigma\sqrt{\tau}}$$



### **Time-Dependent Parameters**

For $r(t), \sigma(t), q(t)$:


$$V(S,t) = \mathbb{E}^{\mathbb{Q}}\left[\exp\left(-\int_t^T r(s)ds\right)\Phi(S_T) \mid S_t = S\right]$$



with:

$$S_T = S_t\exp\left[\int_t^T(r(s)-q(s)-\frac{\sigma^2(s)}{2})ds + \int_t^T\sigma(s)dW_s^{\mathbb{Q}}\right]$$



### **Multi-Dimensional**

For basket options with $n$ assets:

$$V(\mathbf{S},t) = e^{-r\tau}\mathbb{E}^{\mathbb{Q}}[\Phi(\mathbf{S}_T) \mid \mathbf{S}_t = \mathbf{S}]$$



where $\mathbf{S}_T$ follows a multivariate lognormal distribution with correlation matrix $\rho$.

---

## **Summary: Why Feynman-Kac is Powerful**

1. **Converts PDE to probability**: Often easier to compute expectations than solve PDEs
2. **Provides economic interpretation**: Risk-neutral valuation has clear meaning
3. **Enables Monte Carlo**: Can simulate $S_T$ to estimate $\mathbb{E}[\Phi(S_T)]$
4. **Generalizes easily**: Works for path-dependent options, multiple assets, etc.
5. **Deep connection**: Links analysis (PDEs) with probability theory

The Feynman-Kac formula is the **bridge between the PDE world and the probabilistic world** of modern finance!

Would you like to explore any particular aspect deeper? For example:
- The proof of Feynman-Kac using martingale theory
- Connection to the Fundamental Theorems of Asset Pricing
- Applications to exotic options
- Multi-dimensional cases
