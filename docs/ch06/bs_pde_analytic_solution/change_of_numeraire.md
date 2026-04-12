# Change of Numeraire: Alternative Derivation of Black-Scholes


The heat equation and Feynman-Kac sections derived the Black-Scholes formula $C = S\mathcal{N}(d_1) - Ke^{-r\tau}\mathcal{N}(d_2)$ by solving the PDE and computing a risk-neutral expectation. But a question remains: why does the formula split into exactly *two* terms, each involving a normal CDF? The PDE route gives no clear answer --- the split emerges from completing the square in a Gaussian integral.

The **change of numeraire** technique answers this question directly. It shows that each term is a probability under a different measure: $\mathcal{N}(d_2)$ is the risk-neutral probability that $S_T > K$, while $\mathcal{N}(d_1)$ is the same event's probability under the *stock measure*. Unlike the PDE methods developed earlier, this approach is entirely probabilistic --- it uses **measure changes** rather than differential equations. While the standard risk-neutral approach uses the money market account as numeraire, changing to alternative numeraires (e.g., the stock itself) simplifies certain pricing problems and reveals the measure-theoretic structure hidden inside familiar formulas.

---

## Numeraire and Pricing Measures


### 1. **Definition of Numeraire**


A **numeraire** $N_t$ is a strictly positive traded asset used as a unit of account. All asset prices are expressed **relative to the numeraire**:

$$
\text{Relative price} = \frac{S_t}{N_t}
$$



**Key property**: In an arbitrage-free market, there exists a probability measure (called the **numeraire measure** or **$N$-measure**) under which all asset prices relative to $N_t$ are martingales.

### 2. **Standard Risk-Neutral Measure**


In the Black-Scholes framework, the standard numeraire is the **money market account**:

$$
B_t = e^{rt}
$$



Under the risk-neutral measure $\mathbb{Q}$:
- The relative price $S_t/B_t = e^{-rt}S_t$ is a martingale
- This gives the standard BS dynamics: $dS_t = rS_t dt + \sigma S_t dW_t^{\mathbb{Q}}$

**Option pricing formula**:

$$
V_0 = \mathbb{E}^{\mathbb{Q}}\left[\frac{V_T}{B_T}\right] = e^{-rT}\mathbb{E}^{\mathbb{Q}}[V_T]
$$



---

## General Numeraire Change


### 1. **Fundamental Theorem**


> **Numeraire Change Theorem**: Let $N_t$ be any numeraire (strictly positive traded asset). There exists a unique equivalent probability measure $\mathbb{Q}^N$ under which **all asset prices relative to $N_t$ are martingales**.

Specifically, for any traded asset $S_t$:

$$
\frac{S_t}{N_t} = \mathbb{E}^{\mathbb{Q}^N}\left[\frac{S_T}{N_T} \Big| \mathcal{F}_t\right]
$$



### 2. **Radon–Nikodym Derivative**


The measure $\mathbb{Q}^N$ is related to the standard risk-neutral measure $\mathbb{Q}$ via:

$$
\frac{d\mathbb{Q}^N}{d\mathbb{Q}}\Big|_{\mathcal{F}_T} = \frac{N_T/B_T}{\mathbb{E}^{\mathbb{Q}}[N_T/B_T]}
$$



**Intuition**: We reweight paths according to the terminal value of the numeraire (discounted).

### 3. **Girsanov Connection**


The change of numeraire induces a **change of Brownian motion** via Girsanov's theorem. If under $\mathbb{Q}$:

$$
dN_t = \mu_N N_t dt + \sigma_N N_t dW_t^{\mathbb{Q}}
$$



then under $\mathbb{Q}^N$:

$$
dW_t^{\mathbb{Q}^N} = dW_t^{\mathbb{Q}} - \sigma_N dt
$$



Equivalently, $dW_t^{\mathbb{Q}} = dW_t^{\mathbb{Q}^N} + \sigma_N dt$. The drift adjustment reflects the covariance between the asset and the numeraire.

---

## Stock Numeraire and Forward Measure


### 1. **Setup: Stock as Numeraire**


Choose $N_t = S_t$ (the underlying stock itself).

The associated measure $\mathbb{Q}^S$ is called the **stock measure** or **forward measure**.

### 2. **Relative Prices Under Q^S**


Under the stock measure, all assets relative to $S_t$ are martingales.

**Money market account relative to stock**:

$$
\frac{B_t}{S_t} = \mathbb{E}^{\mathbb{Q}^S}\left[\frac{B_T}{S_T} \Big| \mathcal{F}_t\right]
$$



**Strike relative to stock**:

$$
\frac{K}{S_t} = \mathbb{E}^{\mathbb{Q}^S}\left[\frac{K}{S_T} \Big| \mathcal{F}_t\right]
$$



### 3. **Radon–Nikodym Derivative**


The stock measure is related to $\mathbb{Q}$ by:

$$
\frac{d\mathbb{Q}^S}{d\mathbb{Q}}\Big|_{\mathcal{F}_T} = \frac{S_T e^{-rT}}{S_0}
$$



### 4. **Brownian Motion Under Q^S**


If $dS_t = rS_t dt + \sigma S_t dW_t^{\mathbb{Q}}$ under $\mathbb{Q}$, then by Girsanov:

$$
dW_t^{\mathbb{Q}^S} = dW_t^{\mathbb{Q}} - \sigma dt
$$



Substituting $dW_t^{\mathbb{Q}} = dW_t^{\mathbb{Q}^S} + \sigma dt$ into the stock dynamics:

$$
dS_t = rS_t dt + \sigma S_t(dW_t^{\mathbb{Q}^S} + \sigma dt) = (r + \sigma^2)S_t dt + \sigma S_t dW_t^{\mathbb{Q}^S}
$$



**Key property**: The ratio $e^{rt}/S_t$ is a martingale under $\mathbb{Q}^S$, since its drift vanishes.

---

## Black-Scholes via Stock Numeraire


### 1. **Call Option Valuation**


We want to price a European call with payoff $(S_T - K)^+$.

**Step 1: Express payoff in numeraire units**

Divide by $S_T$:

$$
\frac{(S_T - K)^+}{S_T} = \left(1 - \frac{K}{S_T}\right)^+ = \left(1 - \frac{K}{S_T}\right)\mathbf{1}_{\{S_T > K\}}
$$



**Step 2: Change to stock measure**

By the numeraire change theorem:

$$
\frac{C_0}{S_0} = \mathbb{E}^{\mathbb{Q}^S}\left[\frac{C_T}{S_T}\right] = \mathbb{E}^{\mathbb{Q}^S}\left[\left(1 - \frac{K}{S_T}\right)\mathbf{1}_{\{S_T > K\}}\right]
$$



**Step 3: Decompose expectation**


$$
\frac{C_0}{S_0} = \mathbb{E}^{\mathbb{Q}^S}[\mathbf{1}_{\{S_T > K\}}] - K\mathbb{E}^{\mathbb{Q}^S}\left[\frac{1}{S_T}\mathbf{1}_{\{S_T > K\}}\right]
$$



### 2. **First Term: Q^S(S_T > K)**


Under $\mathbb{Q}^S$, the stock dynamics have drift $(r + \sigma^2)$, so by Ito's formula:

$$
S_T = S_0 \exp\left(\left(r + \frac{1}{2}\sigma^2\right)T + \sigma W_T^{\mathbb{Q}^S}\right)
$$



Therefore:

$$
S_T > K \iff \sigma W_T^{\mathbb{Q}^S} > \ln(K/S_0) - \left(r + \frac{1}{2}\sigma^2\right)T
$$



Dividing by $\sigma\sqrt{T}$ and using $W_T^{\mathbb{Q}^S}/\sqrt{T} \sim \mathcal{N}(0,1)$:

$$
S_T > K \iff \frac{W_T^{\mathbb{Q}^S}}{\sqrt{T}} > -\frac{\ln(S_0/K) + \left(r + \frac{1}{2}\sigma^2\right)T}{\sigma\sqrt{T}} = -d_1
$$



where

$$
d_1 = \frac{\ln(S_0/K) + (r + \frac{1}{2}\sigma^2)T}{\sigma\sqrt{T}}
$$



Hence:

$$
\mathbb{Q}^S(S_T > K) = \mathcal{N}(d_1)
$$



### 3. **Second Term: Change to Q**


For the second term, we use:

$$
\mathbb{E}^{\mathbb{Q}^S}\left[\frac{1}{S_T}\mathbf{1}_{\{S_T > K\}}\right] = \mathbb{E}^{\mathbb{Q}}\left[\frac{d\mathbb{Q}^S}{d\mathbb{Q}} \cdot \frac{1}{S_T}\mathbf{1}_{\{S_T > K\}}\right]
$$




$$
= \mathbb{E}^{\mathbb{Q}}\left[\frac{S_T e^{-rT}}{S_0} \cdot \frac{1}{S_T}\mathbf{1}_{\{S_T > K\}}\right] = \frac{e^{-rT}}{S_0}\mathbb{Q}(S_T > K)
$$



Under $\mathbb{Q}$:

$$
\mathbb{Q}(S_T > K) = \mathcal{N}(d_2)
$$



where $d_2 = d_1 - \sigma\sqrt{T}$.

### 4. **Final Result**


Combining:

$$
\frac{C_0}{S_0} = \mathcal{N}(d_1) - K \cdot \frac{e^{-rT}}{S_0}\mathcal{N}(d_2)
$$




$$
\boxed{C_0 = S_0\mathcal{N}(d_1) - Ke^{-rT}\mathcal{N}(d_2)}
$$



This is the **Black-Scholes formula**, derived via stock numeraire.

**Key insight**: The term $\mathcal{N}(d_1)$ arises naturally as the probability under the **stock measure**, not the risk-neutral measure.

---

## Foreign Exchange Options


### 1. **Setup: Quanto Options**


Consider an option on foreign exchange rate $X_t$ (domestic per foreign).

**Two numeraires**:
- Domestic money market: $B_t^d = e^{r_d t}$
- Foreign money market: $B_t^f = e^{r_f t}$

**Exchange rate dynamics** under domestic risk-neutral measure $\mathbb{Q}^d$:

$$
dX_t = (r_d - r_f)X_t dt + \sigma X_t dW_t^{\mathbb{Q}^d}
$$



### 2. **Foreign Numeraire Measure**


Choose numeraire $N_t = X_t B_t^f = X_t e^{r_f t}$ (foreign money market converted to domestic).

The Radon–Nikodym derivative:

$$
\frac{d\mathbb{Q}^f}{d\mathbb{Q}^d}\Big|_{\mathcal{F}_T} = \frac{X_T e^{r_f T - r_d T}}{X_0}
$$



Under $\mathbb{Q}^f$:

$$
dW_t^{\mathbb{Q}^f} = dW_t^{\mathbb{Q}^d} - \sigma dt
$$



Exchange rate becomes:

$$
dX_t = (r_d - r_f + \sigma^2)X_t dt + \sigma X_t dW_t^{\mathbb{Q}^f}
$$



### 3. **Call on FX Rate**


Using the foreign measure:

$$
C_0 = X_0 e^{-r_f T}\mathcal{N}(d_1) - K e^{-r_d T}\mathcal{N}(d_2)
$$



where

$$
d_1 = \frac{\ln(X_0/K) + (r_d - r_f + \frac{1}{2}\sigma^2)T}{\sigma\sqrt{T}}, \quad d_2 = d_1 - \sigma\sqrt{T}
$$



This is the **Garman-Kohlhagen formula** for FX options.

---

## Summary: When to Use Each Numeraire


| Numeraire | Measure | Application | Advantage |
|-----------|---------|-------------|-----------|
| Money market $B_t$ | Risk-neutral $\mathbb{Q}$ | Standard options | Familiar, drift = $r$ |
| Stock $S_t$ | Stock measure $\mathbb{Q}^S$ | Forward contracts | $\mathcal{N}(d_1)$ as probability |
| Zero-coupon bond $P(t,T)$ | Forward measure $\mathbb{Q}^T$ | Interest rate options | Simplifies swap pricing |
| Foreign money market | Foreign measure $\mathbb{Q}^f$ | FX options | Symmetry between currencies |

**General principle**: Choose the numeraire that **eliminates drift** from the payoff-relevant dynamics.

---

## Connection to Other Solution Methods


In the context of solving the Black-Scholes PDE, change of numeraire is:

**Not a PDE technique** (like Fourier or separation of variables), but rather a **probabilistic reinterpretation** that:
- Avoids solving PDEs entirely
- Uses martingale representation instead
- Provides intuition for why certain probabilities appear in formulas

**Relation to Feynman-Kac**: Both express PDE solutions as expectations, but:
- Feynman-Kac uses the **original measure** and discounting
- Numeraire change uses **different measures** without explicit discounting

---

## Summary


The change of numeraire technique provides an elegant alternative to standard risk-neutral pricing:

1. **Key idea**: Price assets relative to any traded numeraire, not just the money market

2. **Mathematical tool**: Radon–Nikodym derivative relating different numeraire measures

3. **Girsanov connection**: Numeraire change induces Brownian motion drift change

4. **Black-Scholes derivation**: Stock numeraire gives $\mathcal{N}(d_1)$ direct probabilistic interpretation

5. **Advantages**: 
   - Conceptual clarity (e.g., $d_1$ as stock-measure probability)
   - Simplifies certain exotic options
   - Natural framework for FX and interest rate derivatives

6. **Limitation**: Requires understanding of measure theory; not always simpler than PDE methods

In the operator framework of the introduction, the change of numeraire expresses the pricing semigroup $\mathcal{P}_\tau$ as an **expectation under a different probability measure**, revealing the structural meaning of each term in the Black--Scholes formula.

---

## Exercises

**Exercise 1.** Let $N_t = e^{rt}$ be the money market account and $\mathbb{Q}$ the associated risk-neutral measure. Verify the Radon–Nikodym derivative formula by showing that $\frac{d\mathbb{Q}^S}{d\mathbb{Q}}\big|_{\mathcal{F}_T} = \frac{S_T e^{-rT}}{S_0}$ has expectation 1 under $\mathbb{Q}$.

??? success "Solution to Exercise 1"
    We need to show that $\mathbb{E}^{\mathbb{Q}}\left[\frac{S_T e^{-rT}}{S_0}\right] = 1$.

    Under $\mathbb{Q}$, the discounted stock price $e^{-rt}S_t$ is a martingale, so:

    $$
    \mathbb{E}^{\mathbb{Q}}[e^{-rT}S_T] = e^{-r \cdot 0}S_0 = S_0
    $$

    Dividing both sides by $S_0$:

    $$
    \mathbb{E}^{\mathbb{Q}}\left[\frac{S_T e^{-rT}}{S_0}\right] = 1
    $$

    Alternatively, using the explicit formula $S_T = S_0 \exp\left((r - \frac{1}{2}\sigma^2)T + \sigma W_T^{\mathbb{Q}}\right)$:

    $$
    \frac{S_T e^{-rT}}{S_0} = \exp\left(-\frac{1}{2}\sigma^2 T + \sigma W_T^{\mathbb{Q}}\right)
    $$

    This is the stochastic exponential $\mathcal{E}(\sigma W^{\mathbb{Q}})_T$. Using the moment generating function of the normal distribution with $W_T^{\mathbb{Q}} \sim \mathcal{N}(0, T)$:

    $$
    \mathbb{E}^{\mathbb{Q}}\left[\exp\left(-\frac{1}{2}\sigma^2 T + \sigma W_T^{\mathbb{Q}}\right)\right] = \exp\left(-\frac{1}{2}\sigma^2 T + \frac{1}{2}\sigma^2 T\right) = 1
    $$

    This confirms that the Radon–Nikodym derivative has unit expectation, as required for a valid change of measure.

---
**Exercise 2.** Under the stock measure $\mathbb{Q}^S$, the discounted bond price $B_t / S_t = e^{rt}/S_t$ is a martingale. Verify this explicitly by computing $d(e^{rt}/S_t)$ using Ito's lemma and the stock dynamics under $\mathbb{Q}^S$, and confirming that the drift vanishes.

??? success "Solution to Exercise 2"
    Under $\mathbb{Q}^S$, the stock dynamics are $dS_t = (r + \sigma^2)S_t \, dt + \sigma S_t \, dW_t^{\mathbb{Q}^S}$.

    Define $Y_t = e^{rt}/S_t$. Apply Ito's lemma to $f(t, S) = e^{rt}/S$.

    For $g(S) = 1/S$, we have $g'(S) = -1/S^2$ and $g''(S) = 2/S^3$. By Ito's lemma:

    $$
    d(1/S_t) = -\frac{1}{S_t^2} \, dS_t + \frac{1}{2} \cdot \frac{2}{S_t^3}(dS_t)^2
    $$

    Substituting $dS_t = (r + \sigma^2)S_t \, dt + \sigma S_t \, dW_t^{\mathbb{Q}^S}$ and $(dS_t)^2 = \sigma^2 S_t^2 \, dt$:

    $$
    d(1/S_t) = \frac{-(r + \sigma^2) + \sigma^2}{S_t} \, dt - \frac{\sigma}{S_t} \, dW_t^{\mathbb{Q}^S} = \frac{-r}{S_t} \, dt - \frac{\sigma}{S_t} \, dW_t^{\mathbb{Q}^S}
    $$

    Therefore:

    $$
    dY_t = \frac{re^{rt}}{S_t} \, dt + e^{rt}\left(\frac{-r}{S_t} \, dt - \frac{\sigma}{S_t} \, dW_t^{\mathbb{Q}^S}\right) = -\sigma Y_t \, dW_t^{\mathbb{Q}^S}
    $$

    The drift vanishes, confirming that $Y_t = e^{rt}/S_t$ is a martingale under $\mathbb{Q}^S$. $\square$

---
**Exercise 3.** Derive the Garman-Kohlhagen formula for a European call on a foreign exchange rate. Starting from the FX dynamics $dX_t = (r_d - r_f)X_t \, dt + \sigma X_t \, dW_t^{\mathbb{Q}^d}$, use the change of numeraire to the foreign money market and show that the call price is $C_0 = X_0 e^{-r_f T}\mathcal{N}(d_1) - Ke^{-r_d T}\mathcal{N}(d_2)$, where $d_1 = \frac{\ln(X_0/K) + (r_d - r_f + \frac{1}{2}\sigma^2)T}{\sigma\sqrt{T}}$.

??? success "Solution to Exercise 3"
    Under $\mathbb{Q}^d$, the FX rate satisfies $dX_t = (r_d - r_f)X_t \, dt + \sigma X_t \, dW_t^{\mathbb{Q}^d}$.

    **Step 1: Choose numeraire.** Take the foreign money market account converted to domestic currency: $N_t = X_t e^{r_f t}$. The Radon–Nikodym derivative is:

    $$
    \frac{d\mathbb{Q}^f}{d\mathbb{Q}^d}\Big|_{\mathcal{F}_T} = \frac{X_T e^{(r_f - r_d)T}}{X_0}
    $$

    **Step 2: Girsanov shift.** Under $\mathbb{Q}^f$: $dW_t^{\mathbb{Q}^f} = dW_t^{\mathbb{Q}^d} - \sigma \, dt$, so $dW_t^{\mathbb{Q}^d} = dW_t^{\mathbb{Q}^f} + \sigma \, dt$.

    Under $\mathbb{Q}^f$, the FX dynamics become:

    $$
    dX_t = (r_d - r_f)X_t \, dt + \sigma X_t(dW_t^{\mathbb{Q}^f} + \sigma \, dt) = (r_d - r_f + \sigma^2)X_t \, dt + \sigma X_t \, dW_t^{\mathbb{Q}^f}
    $$

    **Step 3: Price the call.** The call payoff is $(X_T - K)^+$. Using the numeraire $N_t = X_t e^{r_f t}$:

    $$
    \frac{C_0}{N_0} = \mathbb{E}^{\mathbb{Q}^f}\left[\frac{(X_T - K)^+}{N_T}\right] = \mathbb{E}^{\mathbb{Q}^f}\left[\frac{(X_T - K)^+}{X_T e^{r_f T}}\right]
    $$

    $$
    C_0 = X_0 \mathbb{E}^{\mathbb{Q}^f}\left[\frac{(X_T - K)^+}{X_T e^{r_f T}} \cdot e^{r_f T} \cdot \frac{X_T}{X_0}\right]
    $$

    Alternatively, use the standard risk-neutral approach under $\mathbb{Q}^d$:

    $$
    C_0 = e^{-r_d T}\mathbb{E}^{\mathbb{Q}^d}[(X_T - K)^+]
    $$

    Under $\mathbb{Q}^d$, $\ln X_T \sim \mathcal{N}(\ln X_0 + (r_d - r_f - \frac{1}{2}\sigma^2)T, \sigma^2 T)$. Following the standard Black-Scholes integral evaluation (splitting into two Gaussian integrals and completing the square):

    $$
    C_0 = X_0 e^{-r_f T}\mathcal{N}(d_1) - K e^{-r_d T}\mathcal{N}(d_2)
    $$

    where:

    $$
    d_1 = \frac{\ln(X_0/K) + (r_d - r_f + \frac{1}{2}\sigma^2)T}{\sigma\sqrt{T}}, \quad d_2 = d_1 - \sigma\sqrt{T}
    $$

    This is the Garman-Kohlhagen formula.

---
**Exercise 4.** Consider the exchange option (Margrabe's formula) with payoff $(S_T^{(1)} - S_T^{(2)})^+$ where both assets follow GBM with correlation $\rho$. Using $S_t^{(2)}$ as numeraire, show that the option price is $V_0 = S_0^{(1)}\mathcal{N}(d_1) - S_0^{(2)}\mathcal{N}(d_2)$ and determine the effective volatility $\hat{\sigma}$ that appears in $d_1$ and $d_2$.

??? success "Solution to Exercise 4"
    Let $S_t^{(1)}$ and $S_t^{(2)}$ follow correlated GBMs under $\mathbb{Q}$:

    $$
    dS_t^{(i)} = rS_t^{(i)} \, dt + \sigma_i S_t^{(i)} \, dW_t^{(i)}, \quad d\langle W^{(1)}, W^{(2)}\rangle_t = \rho \, dt
    $$

    **Step 1: Use $S_t^{(2)}$ as numeraire.** The Radon–Nikodym derivative is:

    $$
    \frac{d\mathbb{Q}^{S^{(2)}}}{d\mathbb{Q}}\Big|_{\mathcal{F}_T} = \frac{S_T^{(2)} e^{-rT}}{S_0^{(2)}}
    $$

    **Step 2: Pricing formula.** The exchange option price is:

    $$
    V_0 = e^{-rT}\mathbb{E}^{\mathbb{Q}}[(S_T^{(1)} - S_T^{(2)})^+]
    $$

    Using the numeraire $S_t^{(2)}$:

    $$
    \frac{V_0}{S_0^{(2)}} = \mathbb{E}^{\mathbb{Q}^{S^{(2)}}}\left[\left(\frac{S_T^{(1)}}{S_T^{(2)}} - 1\right)^+\right]
    $$

    **Step 3: Dynamics of the ratio.** Define $R_t = S_t^{(1)}/S_t^{(2)}$. By Ito's lemma:

    $$
    \frac{dR_t}{R_t} = (\sigma_1 \, dW_t^{(1)} - \sigma_2 \, dW_t^{(2)}) + (\sigma_2^2 - \rho\sigma_1\sigma_2) \, dt
    $$

    Under $\mathbb{Q}^{S^{(2)}}$, the Girsanov shift removes the drift from $R_t/1$ (since $R_t = S_t^{(1)}/S_t^{(2)}$ must be a martingale under this measure). The volatility of $R_t$ is:

    $$
    \hat{\sigma} = \sqrt{\sigma_1^2 - 2\rho\sigma_1\sigma_2 + \sigma_2^2}
    $$

    Under $\mathbb{Q}^{S^{(2)}}$, $R_t$ is a driftless geometric Brownian motion with volatility $\hat{\sigma}$.

    **Step 4: Apply Black-Scholes to the ratio.** The problem reduces to pricing a call on $R_T$ with strike 1 in a world with zero interest rate:

    $$
    \frac{V_0}{S_0^{(2)}} = R_0 \mathcal{N}(d_1) - \mathcal{N}(d_2)
    $$

    where $R_0 = S_0^{(1)}/S_0^{(2)}$, and:

    $$
    d_1 = \frac{\ln(S_0^{(1)}/S_0^{(2)}) + \frac{1}{2}\hat{\sigma}^2 T}{\hat{\sigma}\sqrt{T}}, \quad d_2 = d_1 - \hat{\sigma}\sqrt{T}
    $$

    Multiplying by $S_0^{(2)}$:

    $$
    V_0 = S_0^{(1)}\mathcal{N}(d_1) - S_0^{(2)}\mathcal{N}(d_2)
    $$

    This is **Margrabe's formula**. The effective volatility $\hat{\sigma} = \sqrt{\sigma_1^2 - 2\rho\sigma_1\sigma_2 + \sigma_2^2}$ is the volatility of the log-ratio $\ln(S^{(1)}/S^{(2)})$.

---
**Exercise 5.** Explain why the term $\mathcal{N}(d_1)$ in the Black-Scholes call formula is both the delta of the option and the probability of exercise under the stock measure. Is this a coincidence, or does the change-of-numeraire framework make this relationship transparent? Justify your answer.

??? success "Solution to Exercise 5"
    The relationship between $\mathcal{N}(d_1)$ being both the delta and the stock-measure probability of exercise is **not a coincidence** -- it is a direct consequence of the change-of-numeraire framework.

    **Delta as stock-measure probability.** From the Black-Scholes formula $C = S\mathcal{N}(d_1) - Ke^{-rT}\mathcal{N}(d_2)$, differentiating with respect to $S$:

    $$
    \Delta = \frac{\partial C}{\partial S} = \mathcal{N}(d_1) + S\mathcal{N}'(d_1)\frac{\partial d_1}{\partial S} - Ke^{-rT}\mathcal{N}'(d_2)\frac{\partial d_2}{\partial S}
    $$

    Since $\frac{\partial d_1}{\partial S} = \frac{\partial d_2}{\partial S} = \frac{1}{S\sigma\sqrt{T}}$ and $S\mathcal{N}'(d_1) = Ke^{-rT}\mathcal{N}'(d_2)$ (a standard identity), the last two terms cancel, giving $\Delta = \mathcal{N}(d_1)$.

    **Stock-measure probability.** Under the stock measure $\mathbb{Q}^S$, the call price can be written as $C = S_0\mathbb{Q}^S(S_T > K) - Ke^{-rT}\mathbb{Q}(S_T > K)$. Comparing with the Black-Scholes formula:

    $$
    \mathbb{Q}^S(S_T > K) = \mathcal{N}(d_1)
    $$

    **Why this is transparent from the numeraire framework.** Under the numeraire change to the stock, $C_0/S_0 = \mathbb{E}^{\mathbb{Q}^S}[(1 - K/S_T)^+]$. The derivative of $C_0$ with respect to $S_0$ equals the probability under $\mathbb{Q}^S$ that the option expires in the money, because $C_0 = S_0 \cdot \mathbb{Q}^S(S_T > K) - Ke^{-rT}\mathcal{N}(d_2)$ and the first term is linear in $S_0$ (through the dependence of $\mathbb{Q}^S(S_T > K)$ on $S_0$, with the derivative simplifying to $\mathcal{N}(d_1)$). The change-of-numeraire framework makes this relationship structurally transparent: the delta is the hedge ratio, which equals the probability of exercise under the measure where the stock is the numeraire.

---
**Exercise 6.** A zero-coupon bond maturing at time $T$ with price $P(t,T) = e^{-r(T-t)}$ can serve as a numeraire, giving rise to the $T$-forward measure $\mathbb{Q}^T$. Show that under $\mathbb{Q}^T$, the forward price $F(t,T) = S_t / P(t,T)$ is a martingale. Use this to re-derive the Black-Scholes call price starting from $C_0 = P(0,T)\mathbb{E}^{\mathbb{Q}^T}[(F(T,T) - K)^+]$.

??? success "Solution to Exercise 6"
    **Step 1: Show $F(t,T)$ is a martingale under $\mathbb{Q}^T$.** The forward price is:

    $$
    F(t,T) = \frac{S_t}{P(t,T)} = S_t e^{r(T-t)}
    $$

    Under $\mathbb{Q}$, $dS_t = rS_t \, dt + \sigma S_t \, dW_t^{\mathbb{Q}}$. The numeraire is $P(t,T) = e^{-r(T-t)}$ with $dP = rP \, dt$ (deterministic). The Radon–Nikodym derivative:

    $$
    \frac{d\mathbb{Q}^T}{d\mathbb{Q}}\Big|_{\mathcal{F}_T} = \frac{P(T,T)/B_T}{P(0,T)/B_0} = \frac{1/e^{rT}}{e^{-rT}/1} = 1
    $$

    Since the bond is deterministic, $\mathbb{Q}^T = \mathbb{Q}$ and there is no Girsanov shift. Now compute $dF$:

    $$
    dF = d(S_t e^{r(T-t)}) = e^{r(T-t)} \, dS_t + S_t \, d(e^{r(T-t)})
    $$

    $$
    = e^{r(T-t)}(rS_t \, dt + \sigma S_t \, dW_t) - rS_t e^{r(T-t)} \, dt = \sigma F_t \, dW_t^{\mathbb{Q}^T}
    $$

    The drift vanishes, so $F(t,T)$ is a martingale under $\mathbb{Q}^T$.

    **Step 2: Re-derive the call price.** Starting from:

    $$
    C_0 = P(0,T)\mathbb{E}^{\mathbb{Q}^T}[(F(T,T) - K)^+]
    $$

    Note that $F(T,T) = S_T$ and $P(0,T) = e^{-rT}$. Under $\mathbb{Q}^T = \mathbb{Q}$, $F(t,T) = F(0,T)\exp(-\frac{1}{2}\sigma^2 t + \sigma W_t)$ with $F(0,T) = S_0 e^{rT}$.

    So:

    $$
    F(T,T) = S_0 e^{rT} \exp\left(-\frac{1}{2}\sigma^2 T + \sigma W_T\right)
    $$

    The problem is now a standard Black-Scholes pricing with the forward $F_0 = S_0 e^{rT}$ replacing $S_0$, zero interest rate (since discounting is already handled by $P(0,T)$), and the same volatility $\sigma$. By the Black formula:

    $$
    C_0 = e^{-rT}[F_0 \mathcal{N}(d_1) - K\mathcal{N}(d_2)]
    $$

    where:

    $$
    d_1 = \frac{\ln(F_0/K) + \frac{1}{2}\sigma^2 T}{\sigma\sqrt{T}} = \frac{\ln(S_0/K) + rT + \frac{1}{2}\sigma^2 T}{\sigma\sqrt{T}} = \frac{\ln(S_0/K) + (r + \frac{1}{2}\sigma^2)T}{\sigma\sqrt{T}}
    $$

    $$
    d_2 = d_1 - \sigma\sqrt{T}
    $$

    Therefore:

    $$
    C_0 = e^{-rT}[S_0 e^{rT}\mathcal{N}(d_1) - K\mathcal{N}(d_2)] = S_0\mathcal{N}(d_1) - Ke^{-rT}\mathcal{N}(d_2)
    $$

    This recovers the Black-Scholes formula.
