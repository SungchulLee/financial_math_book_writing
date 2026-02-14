# Pricing a European Call Option Using Girsanov's Theorem

We price a **European call option** on a stock whose price follows a geometric Brownian motion. We apply **Girsanov's theorem** to change from the real-world measure $\mathbb{P}$ to the risk-neutral measure $\mathbb{Q}$ under which the discounted asset price is a martingale.

---

## 1 Model Setup

Let the stock price $S_t$ evolve under the real-world measure $\mathbb{P}$ as:

$$
dS_t = \mu S_t\, dt + \sigma S_t\, dW_t, \quad S_0 > 0
$$

Let:

- $K > 0$ be the strike price,
- $T > 0$ be the maturity,
- $r > 0$ be the risk-free interest rate,
- $\sigma > 0$ the volatility,
- $\mu$ the drift (real-world expected return).

The **European call option payoff** at time $T$ is:

$$
\max(S_T - K, 0) = (S_T - K)^+
$$

Our goal is to compute:

$$
C_0 := \mathbb{E}^{\mathbb{Q}} \left[ e^{-rT} (S_T - K)^+ \right]
$$

---

## 2 Step 1: Change of Measure Using Girsanov

We define the **market price of risk**:

$$
\theta := \frac{\mu - r}{\sigma}
$$

Girsanov's theorem tells us that under the new measure $\mathbb{Q}$ defined by:

$$
\left. \frac{d\mathbb{Q}}{d\mathbb{P}} \right|_{\mathcal{F}_T} = Z_T = \exp\left( -\theta W_T - \frac{1}{2} \theta^2 T \right)
$$

the process:

$$
\tilde{W}_t := W_t + \theta t
$$

is a **Brownian motion under $\mathbb{Q}$**, and under $\mathbb{Q}$ the stock price satisfies:

$$
dS_t = r S_t\, dt + \sigma S_t\, d\tilde{W}_t
$$

This is the **risk-neutral dynamic**. The drift has been shifted from $\mu$ to $r$, while the volatility $\sigma$ remains unchanged.

---

## 3 Step 2: Explicit Distribution of $S_T$ under $\mathbb{Q}$

Solving the SDE under $\mathbb{Q}$:

$$
S_T = S_0 \exp\left( \left(r - \tfrac{1}{2} \sigma^2\right) T + \sigma \tilde{W}_T \right)
$$

Since $\tilde{W}_T \sim N(0, T)$ under $\mathbb{Q}$, we have:

$$
\log S_T \sim N\left( \log S_0 + \left(r - \tfrac{1}{2} \sigma^2\right)T,\; \sigma^2 T \right)
$$

---

## 4 Step 3: Compute the Call Option Price

Define:

$$
d_1 := \frac{\log(S_0/K) + (r + \frac{1}{2} \sigma^2)T}{\sigma \sqrt{T}}, \quad
d_2 := d_1 - \sigma \sqrt{T}
$$

Then the **Black–Scholes formula** gives:

$$
C_0 = S_0 \Phi(d_1) - K e^{-rT} \Phi(d_2)
$$

where $\Phi(\cdot)$ is the standard normal cumulative distribution function.

### Interpretation of the Terms

- $\Phi(d_2) = \mathbb{Q}(S_T > K)$: the risk-neutral probability that the option expires in the money.
- $\Phi(d_1) = \mathbb{Q}^S(S_T > K)$: the probability under the **stock numéraire measure** that the option expires in the money.

### Derivation Sketch

From risk-neutral pricing:

$$
\begin{aligned}
C_0 &= e^{-rT} \mathbb{E}^{\mathbb{Q}}[(S_T - K)^+] \\
&= e^{-rT} \int_K^\infty (s - K)\, f_{S_T}^{\mathbb{Q}}(s)\, ds \\
&= S_0 \Phi(d_1) - K e^{-rT} \Phi(d_2)
\end{aligned}
$$

The integral is evaluated by substituting $S_T = S_0 e^{(r - \sigma^2/2)T + \sigma\sqrt{T}\, Z}$ with $Z \sim N(0,1)$, completing the square, and recognizing the resulting expressions as normal CDF evaluations.

---

## 5 Final Result

The **European call price** under Girsanov (risk-neutral pricing) is:

$$
\boxed{
C_0 = S_0 \Phi(d_1) - K e^{-rT} \Phi(d_2)
}
$$

where:

$$
d_1 = \frac{\log(S_0/K) + (r + \frac{1}{2} \sigma^2)T}{\sigma \sqrt{T}}, \quad
d_2 = d_1 - \sigma \sqrt{T}
$$

---

## 6 Summary of the Logic

1. **Start under $\mathbb{P}$**: $dS_t = \mu S_t\, dt + \sigma S_t\, dW_t$

2. **Use Girsanov** to define $\mathbb{Q}$ via the exponential martingale:

$$
Z_T = \exp\left( -\theta W_T - \frac{1}{2} \theta^2 T \right), \quad \theta = \frac{\mu - r}{\sigma}
$$

3. **Under $\mathbb{Q}$**: the drift becomes $r$ instead of $\mu$, giving the risk-neutral SDE.

4. **Price the option** via risk-neutral expectation: $C_0 = e^{-rT}\,\mathbb{E}^{\mathbb{Q}}[(S_T - K)^+]$.

5. **Evaluate the expectation** using the lognormal distribution of $S_T$ under $\mathbb{Q}$ to obtain the Black–Scholes formula.

!!! note "Key Insight"
    The real-world drift $\mu$ does **not** appear in the final pricing formula. Girsanov's theorem absorbs the drift difference $\mu - r$ into the change of measure, so that option prices depend only on $r$, $\sigma$, $S_0$, $K$, and $T$.

---

## QuantPie Derivation via Feynman-Kac

### Connection to the Black-Scholes PDE

The **Black-Scholes PDE** and risk-neutral pricing are connected through the Feynman-Kac formula. For a European option with payoff $\Phi(S_T)$:

$$
\begin{array}{lcc}
\text{Black-Scholes Equation} & & \displaystyle \frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2\frac{\partial^2 V}{\partial S^2} + rS\frac{\partial V}{\partial S} - rV = 0\\
\\
\text{Terminal Condition} & & \displaystyle V(T, S_T) = \Phi(S_T)\\
\\
\text{Risk-Neutral SDE} & & \displaystyle dS = rS\,dt + \sigma S\,dB^{\mathbb{Q}}\\
\\
\text{Feynman-Kac Result} & & \displaystyle V(t, S) = e^{-r(T-t)}\mathbb{E}^{\mathbb{Q}}[\Phi(S_T) | S_t = S]
\end{array}
$$

### Verification via Itô's Lemma

**Starting from the PDE**, assume $V$ satisfies:
$$
\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2\frac{\partial^2 V}{\partial S^2} + rS\frac{\partial V}{\partial S} - rV = 0
$$

**Apply Itô's Lemma** to $V(t, S_t)$ under the risk-neutral dynamics:

$$
dV = V_t dt + V_S dS + \frac{1}{2}V_{SS}(dS)^2
$$

$$
= V_t dt + V_S(rS\,dt + \sigma S\,dB^{\mathbb{Q}}) + \frac{1}{2}V_{SS}\sigma^2 S^2 dt
$$

$$
= \left(V_t + rSV_S + \frac{1}{2}\sigma^2S^2V_{SS}\right)dt + \sigma SV_S dB^{\mathbb{Q}}
$$

**Substituting the PDE constraint** ($V_t + rSV_S + \frac{1}{2}\sigma^2S^2V_{SS} = rV$):

$$
dV = rV\,dt + \sigma SV_S dB^{\mathbb{Q}}
$$

### Discounted Value is a Martingale

Define the **discounted option value:**

$$
\tilde{V}(t) = \frac{V(t, S_t)}{e^{rt}}
$$

**Computing the differential:**

$$
d\tilde{V} = \frac{dV}{e^{rt}} - r\frac{V}{e^{rt}}dt = \frac{rV\,dt + \sigma SV_S dB^{\mathbb{Q}}}{e^{rt}} - r\frac{V}{e^{rt}}dt
$$

$$
= \frac{\sigma SV_S}{e^{rt}}dB^{\mathbb{Q}} = \sigma S\left(\frac{V_S}{e^{rt}}\right)dB^{\mathbb{Q}}
$$

**The drift term vanishes!** Therefore $\tilde{V}(t)$ is a **martingale under** $\mathbb{Q}$.

### Martingale Property Implies Risk-Neutral Pricing

Since $\tilde{V}(t)$ is a martingale:

$$
\tilde{V}(t) = \mathbb{E}^{\mathbb{Q}}[\tilde{V}(T) | \mathcal{F}_t]
$$

$$
\frac{V(t, S_t)}{e^{rt}} = \mathbb{E}^{\mathbb{Q}}\left[\frac{V(T, S_T)}{e^{rT}} \,\Big|\, \mathcal{F}_t\right]
$$

$$
\frac{V(t, S_t)}{e^{rt}} = \mathbb{E}^{\mathbb{Q}}\left[\frac{\Phi(S_T)}{e^{rT}} \,\Big|\, S_t = S\right]
$$

$$
\boxed{V(t, S) = e^{-r(T-t)}\mathbb{E}^{\mathbb{Q}}[\Phi(S_T) | S_t = S]}
$$

### Why the Real-World Drift Doesn't Matter

Under the real-world measure $\mathbb{P}$:
$$
dS = \mu S\,dt + \sigma S\,dW
$$

Under the risk-neutral measure $\mathbb{Q}$ defined by Girsanov:
$$
dS = rS\,dt + \sigma S\,d\tilde{W}^{\mathbb{Q}}
$$

**The change of measure** via the Radon-Nikodym derivative:
$$
\frac{d\mathbb{Q}}{d\mathbb{P}}\Big|_{\mathcal{F}_T} = \exp\left(-\frac{\mu - r}{\sigma}W_T - \frac{1}{2}\left(\frac{\mu-r}{\sigma}\right)^2 T\right)
$$

**Key observation:** The martingale property of $\tilde{V}(t)$ holds under $\mathbb{Q}$, not $\mathbb{P}$. The drift $\mu$ appears in the Radon-Nikodym derivative but not in the final formula because we compute the expectation under $\mathbb{Q}$.

This is why option prices are **drift-neutral**: they depend only on the volatility $\sigma$, the risk-free rate $r$, and the option structure, not on traders' expectations ($\mu$) about future stock returns.
