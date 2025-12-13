# Change of Numeraire: Complete Mathematical Treatment

The change of numeraire technique is **profoundly elegant**—it reveals that option prices are invariant to the choice of "currency" we use to measure value, while the probability measure changes in a precise, calculable way.

---

## **1. Fundamental Theorem of Asset Pricing**

### **Numeraire Definition**

A **numeraire** is a strictly positive tradable asset $N_t > 0$ used as the unit of account. All other asset prices are expressed **relative** to this numeraire.

### **Normalized Prices**

For any asset with price $S_t$ and numeraire $N_t$:
$$\boxed{\tilde{S}_t = \frac{S_t}{N_t}}$$

is the **normalized price** (price in units of the numeraire).

### **First Fundamental Theorem**

A market is **arbitrage-free** if and only if there exists an **equivalent martingale measure** $\mathbb{Q}$ such that all normalized asset prices are martingales:

$$\boxed{\mathbb{E}^{\mathbb{Q}}\left[\frac{S_T}{N_T} \mid \mathcal{F}_t\right] = \frac{S_t}{N_t}}$$

### **Key Insight**

The choice of numeraire $N$ determines the measure $\mathbb{Q}$. Different numeraires → different measures, but **same prices**!

---

## **2. Mathematical Foundations**

### **Radon-Nikodym Derivative**

Given two equivalent probability measures $\mathbb{Q}$ and $\mathbb{Q}^N$ on $(\Omega, \mathcal{F})$:

$$\boxed{\frac{d\mathbb{Q}^N}{d\mathbb{Q}} = \eta_T}$$

where $\eta_T$ is the **Radon-Nikodym derivative** (density process).

### **Change of Measure Formula**

For any $\mathcal{F}_T$-measurable random variable $X$:

$$\boxed{\mathbb{E}^{\mathbb{Q}^N}[X \mid \mathcal{F}_t] = \frac{1}{\eta_t}\mathbb{E}^{\mathbb{Q}}[\eta_T X \mid \mathcal{F}_t]}$$

where:
$$\eta_t = \mathbb{E}^{\mathbb{Q}}[\eta_T \mid \mathcal{F}_t]$$

is the **density process** (a $\mathbb{Q}$-martingale).

### **Girsanov Theorem**

If $W_t^{\mathbb{Q}}$ is a Brownian motion under $\mathbb{Q}$ and:
$$d\eta_t = \eta_t \gamma_t dW_t^{\mathbb{Q}}$$

then under $\mathbb{Q}^N$:
$$\boxed{W_t^{\mathbb{Q}^N} = W_t^{\mathbb{Q}} - \int_0^t \gamma_s ds}$$

is a Brownian motion.

The **market price of risk** $\gamma_t$ determines the measure change.

---

## **3. The Numeraire Change Theorem**

### **Statement**

Let $N_t$ be a numeraire with associated measure $\mathbb{Q}^N$. Then:

1. **The density process is**:
$$\boxed{\eta_t = \frac{N_0/B_t}{N_t/B_t} = \frac{N_0 B_T}{N_T B_t} \cdot \frac{B_t}{B_0}}$$

   where $B_t = e^{\int_0^t r_s ds}$ is the money market account (bank account numeraire).

   Simplifying:
$$\boxed{\frac{d\mathbb{Q}^N}{d\mathbb{Q}}\bigg|_{\mathcal{F}_T} = \frac{N_0}{N_T} \cdot \frac{B_T}{B_0}}$$

2. **Asset prices under the new measure**:
$$\boxed{V_t = N_t \mathbb{E}^{\mathbb{Q}^N}\left[\frac{V_T}{N_T} \mid \mathcal{F}_t\right]}$$

3. **Normalized prices are martingales**:
$$\boxed{\frac{V_t}{N_t} = \mathbb{E}^{\mathbb{Q}^N}\left[\frac{V_T}{N_T} \mid \mathcal{F}_t\right]}$$

### **Proof Sketch**

Under $\mathbb{Q}$, the discounted price $\frac{V_t}{B_t}$ is a martingale:
$$\frac{V_t}{B_t} = \mathbb{E}^{\mathbb{Q}}\left[\frac{V_T}{B_T} \mid \mathcal{F}_t\right]$$

Similarly, $\frac{N_t}{B_t}$ is a martingale:
$$\frac{N_t}{B_t} = \mathbb{E}^{\mathbb{Q}}\left[\frac{N_T}{B_T} \mid \mathcal{F}_t\right]$$

Define the density:
$$\eta_T = \frac{N_T/B_T}{N_0/B_0}$$

Then:
$$V_t = B_t \mathbb{E}^{\mathbb{Q}}\left[\frac{V_T}{B_T} \mid \mathcal{F}_t\right]$$

$$= B_t \mathbb{E}^{\mathbb{Q}}\left[\frac{V_T}{B_T} \cdot \frac{\eta_T}{\eta_t} \cdot \frac{\eta_t}{\eta_T} \mid \mathcal{F}_t\right]$$

$$= B_t \frac{1}{\eta_t}\mathbb{E}^{\mathbb{Q}}\left[\frac{V_T}{B_T} \eta_T \mid \mathcal{F}_t\right]$$

Since $\eta_t = \frac{N_t/B_t}{N_0/B_0}$:

$$= \frac{B_t N_0/B_0}{N_t/B_t}\mathbb{E}^{\mathbb{Q}}\left[\frac{V_T}{B_T} \cdot \frac{N_T/B_T}{N_0/B_0} \mid \mathcal{F}_t\right]$$

$$= N_t \mathbb{E}^{\mathbb{Q}}\left[\frac{V_T}{N_T} \mid \mathcal{F}_t\right] \cdot \frac{N_0/B_0}{N_0/B_0}$$

By change of measure formula:
$$\boxed{V_t = N_t \mathbb{E}^{\mathbb{Q}^N}\left[\frac{V_T}{N_T} \mid \mathcal{F}_t\right]}$$

---

## **4. Classical Example: Risk-Neutral Measure**

### **Money Market Account as Numeraire**

$$B_t = e^{\int_0^t r_s ds}$$

For constant $r$: $B_t = e^{rt}$.

### **The Risk-Neutral Measure $\mathbb{Q}$**

Using $N_t = B_t$:
$$V_t = B_t \mathbb{E}^{\mathbb{Q}}\left[\frac{V_T}{B_T} \mid \mathcal{F}_t\right]$$

$$\boxed{V_t = e^{-r(T-t)}\mathbb{E}^{\mathbb{Q}}[V_T \mid \mathcal{F}_t]}$$

This is the **standard risk-neutral pricing formula**.

### **Stock Dynamics Under $\mathbb{Q}$**

For a stock with physical dynamics:
$$dS_t = \mu S_t dt + \sigma S_t dW_t^{\mathbb{P}}$$

Under $\mathbb{Q}$:
$$\boxed{dS_t = rS_t dt + \sigma S_t dW_t^{\mathbb{Q}}}$$

The **drift equals the risk-free rate** (no arbitrage condition).

---

## **5. Stock as Numeraire**

### **The Stock Measure $\mathbb{Q}^S$**

Choose $N_t = S_t$ (the stock itself as numeraire).

### **Radon-Nikodym Derivative**

$$\boxed{\frac{d\mathbb{Q}^S}{d\mathbb{Q}}\bigg|_{\mathcal{F}_T} = \frac{S_T e^{-rT}}{S_0}}$$

With constant $r$:
$$\boxed{\frac{d\mathbb{Q}^S}{d\mathbb{Q}}\bigg|_{\mathcal{F}_T} = \frac{S_T}{S_0 e^{rT}}}$$

### **Stock Dynamics Under $\mathbb{Q}^S$**

Under $\mathbb{Q}$:
$$dS_t = rS_t dt + \sigma S_t dW_t^{\mathbb{Q}}$$

The density process:
$$\eta_t = \frac{S_t e^{-rt}}{S_0}$$

By Itô's lemma:
$$d\eta_t = \eta_t \sigma dW_t^{\mathbb{Q}}$$

So the market price of risk is $\gamma_t = \sigma$.

By Girsanov:
$$W_t^{\mathbb{Q}^S} = W_t^{\mathbb{Q}} - \sigma t$$

Therefore under $\mathbb{Q}^S$:
$$dS_t = rS_t dt + \sigma S_t(dW_t^{\mathbb{Q}^S} + \sigma dt)$$

$$\boxed{dS_t = (r + \sigma^2)S_t dt + \sigma S_t dW_t^{\mathbb{Q}^S}}$$

The drift increases by $\sigma^2$!

### **Economic Interpretation**

Under the stock measure, investors use **shares** as currency. The stock becomes the "risk-free" asset (with drift $0$ in normalized units), so other assets must have higher drifts.

---

## **6. Deriving Black-Scholes via Stock Numeraire**

### **Call Option Value**

$$C_t = e^{-r(T-t)}\mathbb{E}^{\mathbb{Q}}[(S_T - K)^+ \mid \mathcal{F}_t]$$

### **Splitting the Expectation**

$$C_t = e^{-r\tau}\mathbb{E}^{\mathbb{Q}}[S_T \mathbb{1}_{S_T > K} \mid \mathcal{F}_t] - e^{-r\tau}K\mathbb{E}^{\mathbb{Q}}[\mathbb{1}_{S_T > K} \mid \mathcal{F}_t]$$

where $\tau = T - t$.

### **First Term: Using Stock Numeraire**

For the first term, use the change of numeraire:
$$\mathbb{E}^{\mathbb{Q}}[S_T \mathbb{1}_{S_T > K} \mid \mathcal{F}_t] = S_t \mathbb{E}^{\mathbb{Q}^S}[\mathbb{1}_{S_T > K} \mid \mathcal{F}_t]$$

**Proof**:
$$\mathbb{E}^{\mathbb{Q}}[S_T \mathbb{1}_{S_T > K} \mid \mathcal{F}_t] = \mathbb{E}^{\mathbb{Q}}\left[S_T \mathbb{1}_{S_T > K} \frac{d\mathbb{Q}^S}{d\mathbb{Q}}\bigg|_{\mathcal{F}_T} \cdot \frac{d\mathbb{Q}}{d\mathbb{Q}^S}\bigg|_{\mathcal{F}_T} \mid \mathcal{F}_t\right]$$

$$= \mathbb{E}^{\mathbb{Q}}\left[S_T \mathbb{1}_{S_T > K} \frac{S_T e^{-rT}}{S_0} \cdot \frac{S_0 e^{rT}}{S_T} \mid \mathcal{F}_t\right]$$

Wait, let me redo this more carefully.

Using the change of measure:
$$\mathbb{E}^{\mathbb{Q}}[S_T \mathbb{1}_{S_T > K} \mid \mathcal{F}_t] = \mathbb{E}^{\mathbb{Q}}\left[\frac{S_T}{S_t} S_t \mathbb{1}_{S_T > K} \mid \mathcal{F}_t\right]$$

The key is:
$$\mathbb{E}^{\mathbb{Q}}\left[\frac{S_T}{S_t} \mathbb{1}_{S_T > K} \mid \mathcal{F}_t\right] = e^{r\tau}\mathbb{E}^{\mathbb{Q}^S}[\mathbb{1}_{S_T > K} \mid \mathcal{F}_t]$$

Actually, let me use a cleaner approach:

$$\frac{d\mathbb{Q}^S}{d\mathbb{Q}}\bigg|_{\mathcal{F}_t} = \frac{S_t/B_t}{S_0/B_0}$$

So:
$$\mathbb{E}^{\mathbb{Q}}[S_T \mathbb{1}_{S_T > K} \mid \mathcal{F}_t] = \mathbb{E}^{\mathbb{Q}}\left[S_T \mathbb{1}_{S_T > K} \cdot \frac{S_t B_0}{S_0 B_t} \cdot \frac{S_0 B_T}{S_T B_0} \mid \mathcal{F}_t\right]$$

$$= \frac{S_t B_0}{S_0 B_t}\mathbb{E}^{\mathbb{Q}}\left[\frac{S_0 B_T}{B_0} \mathbb{1}_{S_T > K} \mid \mathcal{F}_t\right]$$

$$= \frac{S_t}{B_t}\mathbb{E}^{\mathbb{Q}}\left[B_T \mathbb{1}_{S_T > K} \mid \mathcal{F}_t\right]$$

$$= S_t e^{r\tau}\mathbb{E}^{\mathbb{Q}^S}[\mathbb{1}_{S_T > K} \mid \mathcal{F}_t]$$

### **Computing Probabilities**

Under $\mathbb{Q}^S$:
$$\ln S_T = \ln S_t + \left(r + \frac{\sigma^2}{2}\right)\tau + \sigma W_\tau^{\mathbb{Q}^S}$$

So:
$$\mathbb{Q}^S(S_T > K \mid \mathcal{F}_t) = \mathbb{Q}^S\left(W_\tau^{\mathbb{Q}^S} > -\frac{\ln(S_t/K) + (r+\frac{\sigma^2}{2})\tau}{\sigma}\right)$$

$$= N\left(\frac{\ln(S_t/K) + (r+\frac{\sigma^2}{2})\tau}{\sigma\sqrt{\tau}}\right) = N(d_1)$$

Under $\mathbb{Q}$:
$$\ln S_T = \ln S_t + \left(r - \frac{\sigma^2}{2}\right)\tau + \sigma W_\tau^{\mathbb{Q}}$$

$$\mathbb{Q}(S_T > K \mid \mathcal{F}_t) = N\left(\frac{\ln(S_t/K) + (r-\frac{\sigma^2}{2})\tau}{\sigma\sqrt{\tau}}\right) = N(d_2)$$

### **Black-Scholes Formula**

$$C_t = e^{-r\tau}[S_t e^{r\tau}N(d_1) - K N(d_2)]$$

$$\boxed{C_t = S_t N(d_1) - Ke^{-r\tau}N(d_2)}$$

where:
$$\boxed{d_1 = \frac{\ln(S/K) + (r + \frac{\sigma^2}{2})\tau}{\sigma\sqrt{\tau}}, \quad d_2 = d_1 - \sigma\sqrt{\tau}}$$

### **Interpretation**

- $N(d_2) = \mathbb{Q}(\text{ITM})$: probability of exercise under risk-neutral measure
- $N(d_1) = \mathbb{Q}^S(\text{ITM})$: probability of exercise under stock measure
- The $\sigma^2$ shift in drift explains why $d_1 = d_2 + \sigma\sqrt{\tau}$

---

## **7. Zero-Coupon Bond as Numeraire (T-Forward Measure)**

### **Setup**

Let $P(t,T)$ be the price at time $t$ of a zero-coupon bond maturing at $T$.

**Numeraire**: $N_t = P(t,T)$

### **T-Forward Measure $\mathbb{Q}^T$**

$$\boxed{\frac{d\mathbb{Q}^T}{d\mathbb{Q}}\bigg|_{\mathcal{F}_T} = \frac{P(0,T)}{B_T}}$$

At maturity: $P(T,T) = 1$.

### **Asset Dynamics Under $\mathbb{Q}^T$**

The normalized price:
$$\tilde{S}_t = \frac{S_t}{P(t,T)}$$

is a $\mathbb{Q}^T$-martingale.

This is the **forward price**:
$$\boxed{F(t,T) = \frac{S_t}{P(t,T)} = \mathbb{E}^{\mathbb{Q}^T}[S_T \mid \mathcal{F}_t]}$$

Under $\mathbb{Q}^T$, forward prices are **driftless**:
$$\boxed{dF(t,T) = \sigma F(t,T) dW_t^{\mathbb{Q}^T}}$$

### **Black's Formula**

For a call on the forward:
$$C_t = P(t,T)\mathbb{E}^{\mathbb{Q}^T}[(S_T - K)^+ \mid \mathcal{F}_t]$$

$$= P(t,T)\mathbb{E}^{\mathbb{Q}^T}[(F(T,T) - K)^+ \mid \mathcal{F}_t]$$

Since $F(t,T)$ is lognormal under $\mathbb{Q}^T$:

$$\boxed{C_t = P(t,T)[F(t,T)N(d_1) - KN(d_2)]}$$

where:
$$d_1 = \frac{\ln(F/K) + \frac{\sigma^2}{2}\tau}{\sigma\sqrt{\tau}}, \quad d_2 = d_1 - \sigma\sqrt{\tau}$$

This is **Black's formula** for forward contracts!

---

## **8. Applications to Exotic Options**

### **Exchange Options (Margrabe Formula)**

Payoff: $(S_T^{(1)} - S_T^{(2)})^+$

**Use $S^{(2)}$ as numeraire**:
$$V_t = S_t^{(2)}\mathbb{E}^{\mathbb{Q}^{S^{(2)}}}\left[\left(\frac{S_T^{(1)}}{S_T^{(2)}} - 1\right)^+ \mid \mathcal{F}_t\right]$$

Define the **relative price**:
$$X_t = \frac{S_t^{(1)}}{S_t^{(2)}}$$

Under $\mathbb{Q}^{S^{(2)}}$, $X_t$ follows GBM with volatility:
$$\sigma_X = \sqrt{\sigma_1^2 + \sigma_2^2 - 2\rho\sigma_1\sigma_2}$$

where $\rho = \text{corr}(dW_1, dW_2)$.

The value is:
$$\boxed{V_t = S_t^{(1)}N(d_1) - S_t^{(2)}N(d_2)}$$

where:
$$d_1 = \frac{\ln(S_t^{(1)}/S_t^{(2)}) + \frac{\sigma_X^2}{2}\tau}{\sigma_X\sqrt{\tau}}, \quad d_2 = d_1 - \sigma_X\sqrt{\tau}$$

**No discounting needed!** The formula is symmetric in the two assets.

### **Quanto Options**

Option on foreign stock $S_t^f$ (in foreign currency) but payoff in domestic currency.

**Dynamics**:
- Foreign stock: $dS^f = r_f S^f dt + \sigma_S S^f dW_S$
- Exchange rate: $dX = (r_d - r_f)X dt + \sigma_X X dW_X$
- Correlation: $d\langle W_S, W_X \rangle = \rho dt$

**Domestic value**: $S_t = X_t S_t^f$

Under the domestic risk-neutral measure, the quanto forward price is:
$$F_{\text{quanto}}(t,T) = S_t^f e^{(r_f - \rho\sigma_S\sigma_X)\tau}$$

The **quanto adjustment** is $-\rho\sigma_S\sigma_X$.

**Call price**:
$$\boxed{C = e^{-r_d\tau}[F_{\text{quanto}}N(d_1) - KN(d_2)]}$$

### **Asian Options**

Payoff depends on the average:
$$A_T = \frac{1}{T}\int_0^T S_t dt$$

**No simple numeraire argument** gives a closed form (average of lognormals is not lognormal).

However, for **discrete averaging**, moment-matching approximations work:
$$A_T \approx \text{Lognormal}(m, v^2)$$

where $m, v^2$ are computed from the forward curve.

---

## **9. Multi-Asset Case**

### **General Setup**

$n$ assets $S_t^{(i)}$ with dynamics under $\mathbb{Q}$:
$$dS_t^{(i)} = rS_t^{(i)}dt + \sigma_i S_t^{(i)}\sum_{j=1}^d \rho_{ij}dW_t^{(j)}$$

where $\rho$ is the correlation matrix.

### **Numeraire Choice**

Choose $N_t = S_t^{(k)}$ for some asset $k$.

### **Dynamics Under $\mathbb{Q}^{S^{(k)}}$**

The relative prices:
$$X_t^{(i)} = \frac{S_t^{(i)}}{S_t^{(k)}}$$

satisfy:
$$dX_t^{(i)} = \sigma_{ik}X_t^{(i)}dt + X_t^{(i)}\sum_{j=1}^d(\rho_{ij} - \rho_{kj})dW_t^{(j)}$$

where:
$$\sigma_{ik} = \sum_{j=1}^d\rho_{ij}\rho_{kj}$$

is the **instantaneous covariance** between assets $i$ and $k$.

### **Basket Options**

For a basket with payoff:
$$\left(\sum_{i=1}^n w_i S_T^{(i)} - K\right)^+$$

Use the basket itself as numeraire if it's tradable (e.g., via an ETF).

Otherwise, use **moment-matching** or **Monte Carlo** under an appropriate measure.

---

## **10. Change of Numeraire and PDEs**

### **The PDE Under Different Numeraires**

Under the risk-neutral measure ($B_t$ numeraire), the Black-Scholes PDE is:
$$\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{\sigma^2}{2}S^2\frac{\partial^2 V}{\partial S^2} - rV = 0$$

### **Under Stock Numeraire**

Define $u(S,t) = \frac{V(S,t)}{S}$ (option value per share).

Then $u$ satisfies:
$$\frac{\partial u}{\partial t} + (r+\sigma^2)S\frac{\partial u}{\partial S} + \frac{\sigma^2}{2}S^2\frac{\partial^2 u}{\partial S^2} = 0$$

The drift changes from $r$ to $r + \sigma^2$, matching our earlier result!

### **Under T-Forward Measure**

The forward price $F(t,T) = S_t/P(t,T)$ satisfies:
$$\frac{\partial V_F}{\partial t} + \frac{\sigma^2}{2}F^2\frac{\partial^2 V_F}{\partial F^2} = 0$$

**No drift term!** This is just the heat equation.

### **General Pattern**

Changing numeraire changes the **drift** but not the **diffusion coefficient**.

$$\text{Drift under } \mathbb{Q}^N = \text{Drift under } \mathbb{Q} + \text{(covariance with numeraire)}$$

---

## **11. Girsanov Theorem in Detail**

### **For Stock Numeraire**

Under $\mathbb{Q}$:
$$dS_t = rS_t dt + \sigma S_t dW_t^{\mathbb{Q}}$$

The Radon-Nikodym density:
$$\eta_t = \frac{S_t e^{-rt}}{S_0}$$

By Itô's lemma:
$$d\eta_t = -re^{-rt}\frac{S_t}{S_0}dt + e^{-rt}\frac{1}{S_0}dS_t$$

$$= -r\eta_t dt + e^{-rt}\frac{1}{S_0}(rS_t dt + \sigma S_t dW_t^{\mathbb{Q}})$$

$$= -r\eta_t dt + r\eta_t dt + \sigma\eta_t dW_t^{\mathbb{Q}}$$

$$\boxed{d\eta_t = \sigma\eta_t dW_t^{\mathbb{Q}}}$$

So $\eta_t$ is a $\mathbb{Q}$-martingale with:
$$\eta_t = \exp\left(\sigma W_t^{\mathbb{Q}} - \frac{\sigma^2 t}{2}\right)$$

By Girsanov:
$$\boxed{dW_t^{\mathbb{Q}^S} = dW_t^{\mathbb{Q}} - \sigma dt}$$

Therefore:
$$dS_t = rS_t dt + \sigma S_t(dW_t^{\mathbb{Q}^S} + \sigma dt)$$

$$\boxed{dS_t = (r + \sigma^2)S_t dt + \sigma S_t dW_t^{\mathbb{Q}^S}}$$

### **Market Price of Risk**

The general formula:
$$\boxed{\gamma_t = \sigma_N}$$

where $\sigma_N$ is the volatility of the numeraire.

For stock: $\sigma_N = \sigma$
For bond: $\sigma_N = 0$ (deterministic)
For forward: depends on the term structure model

---

## **12. Stochastic Interest Rates**

### **Setup**

$$dS_t = rS_t dt + \sigma_S S_t dW_t^S$$
$$dr_t = a(b-r_t)dt + \sigma_r dW_t^r$$

with $d\langle W^S, W^r \rangle = \rho dt$.

### **T-Forward Measure**

The bond price $P(t,T)$ satisfies:
$$dP(t,T) = r_t P(t,T)dt - \sigma_P(t,T)P(t,T)dW_t^r$$

where $\sigma_P(t,T)$ depends on the interest rate model.

Under $\mathbb{Q}^T$:
$$dS_t = S_t[r_t dt + \rho\sigma_S\sigma_P(t,T)dt + \sigma_S dW_t^{S,T}]$$

The **quanto adjustment** now depends on correlation with bond volatility.

### **LIBOR Market Model**

Forward LIBOR rates are **lognormal** under their respective forward measures:
$$dL_i(t) = \sigma_i L_i(t) dW_t^{T_i}$$

This is the **natural measure** for LIBOR-based derivatives.

---

## **13. American Options**

### **Optimal Stopping**

American option value:
$$V_t = \sup_{\tau \in [t,T]}\mathbb{E}^{\mathbb{Q}}[e^{-r(\tau-t)}\Phi(S_\tau) \mid \mathcal{F}_t]$$

### **Change of Numeraire**

Using stock as numeraire:
$$V_t = S_t \sup_{\tau \in [t,T]}\mathbb{E}^{\mathbb{Q}^S}\left[\frac{\Phi(S_\tau)}{S_\tau} \mid \mathcal{F}_t\right]$$

For a put, $\Phi(S) = (K-S)^+$:
$$V_t = S_t \sup_{\tau \in [t,T]}\mathbb{E}^{\mathbb{Q}^S}\left[\left(\frac{K}{S_\tau} - 1\right)^+ \mid \mathcal{F}_t\right]$$

This is a **call on the inverse** $1/S$!

### **Symmetry Relations**

For American puts and calls:
$$P_{\text{Am}}(S,K,r,\sigma,T) = S \cdot C_{\text{Am}}\left(\frac{1}{S}, \frac{1}{K}, 0, \sigma, T\right)$$

This **put-call symmetry** is a consequence of numeraire change.

---

## **14. Dividends and Dividend Yield**

### **Continuous Dividend Yield**

Stock pays continuous dividend at rate $q$:
$$dS_t = (r-q)S_t dt + \sigma S_t dW_t^{\mathbb{Q}}$$

The **tradable asset** is the **total return**:
$$\tilde{S}_t = S_t e^{qt}$$

with dynamics:
$$d\tilde{S}_t = r\tilde{S}_t dt + \sigma\tilde{S}_t dW_t^{\mathbb{Q}}$$

### **Stock Measure with Dividends**

Using $\tilde{S}_t$ as numeraire:
$$\frac{d\mathbb{Q}^{\tilde{S}}}{d\mathbb{Q}}\bigg|_{\mathcal{F}_T} = \frac{\tilde{S}_T e^{-rT}}{\tilde{S}_0}$$

Under $\mathbb{Q}^{\tilde{S}}$:
$$d\tilde{S}_t = (r+\sigma^2)\tilde{S}_t dt + \sigma\tilde{S}_t dW_t^{\mathbb{Q}^{\tilde{S}}}$$

For the actual stock:
$$dS_t = (r - q + \sigma^2)S_t dt + \sigma S_t dW_t^{\mathbb{Q}^{\tilde{S}}}$$

### **Black-Scholes with Dividends**

$$\boxed{C_t = Se^{-q\tau}N(d_1) - Ke^{-r\tau}N(d_2)}$$

where:
$$d_1 = \frac{\ln(S/K) + (r-q+\frac{\sigma^2}{2})\tau}{\sigma\sqrt{\tau}}$$

---

## **15. Connection to Characteristic Functions**

### **Under Different Measures**

The characteristic function of $\ln S_T$ depends on the measure:

**Under $\mathbb{Q}$**:
$$\phi^{\mathbb{Q}}(\omega) = \mathbb{E}^{\mathbb{Q}}[e^{i\omega \ln S_T}] = \exp\left[i\omega\ln S_0 + i\omega(r-\frac{\sigma^2}{2})T - \frac{\sigma^2\omega^2 T}{2}\right]$$

**Under $\mathbb{Q}^S$**:
$$\phi^{\mathbb{Q}^S}(\omega) = \mathbb{E}^{\mathbb{Q}^S}[e^{i\omega \ln S_T}] = \exp\left[i\omega\ln S_0 + i\omega(r+\frac{\sigma^2}{2})T - \frac{\sigma^2\omega^2 T}{2}\right]$$

**Relationship**:
$$\phi^{\mathbb{Q}^S}(\omega) = \phi^{\mathbb{Q}}(\omega) \cdot e^{i\omega\sigma^2 T}$$

The shift by $\sigma^2 T$ reflects the numeraire change!

---

## **16. Abstract Formulation**

### **General Numeraire Change Formula**

For two numeraires $N_t^{(1)}$ and $N_t^{(2)}$ with measures $\mathbb{Q}^{(1)}$ and $\mathbb{Q}^{(2)}$:

$$\boxed{\frac{d\mathbb{Q}^{(2)}}{d\mathbb{Q}^{(1)}}\bigg|_{\mathcal{F}_T} = \frac{N_T^{(2)}/N_0^{(2)}}{N_T^{(1)}/N_0^{(1)}}}$$

### **Multi-Period Extension**

For times $0 < t < T$:
$$\boxed{\frac{d\mathbb{Q}^{(2)}}{d\mathbb{Q}^{(1)}}\bigg|_{\mathcal{F}_t} = \frac{N_t^{(2)}/N_0^{(2)}}{N_t^{(1)}/N_0^{(1)}}}$$

This is the **conditional Radon-Nikodym derivative**.

### **Invariance of Option Prices**

$$V_t = N_t^{(1)}\mathbb{E}^{\mathbb{Q}^{(1)}}\left[\frac{V_T}{N_T^{(1)}} \mid \mathcal{F}_t\right] = N_t^{(2)}\mathbb{E}^{\mathbb{Q}^{(2)}}\left[\frac{V_T}{N_T^{(2)}} \mid \mathcal{F}_t\right]$$

**Same price, different representations!**

---

## **17. Practical Applications**

### **Interest Rate Derivatives**

For **caplets/floorlets**, use the T-forward measure corresponding to the payment date.

For **swaptions**, use the **swap measure** where the numeraire is the annuity factor.

### **Foreign Exchange**

For quanto options, use domestic vs. foreign measures.

The **Siegel paradox**: $\mathbb{E}[X_T] \neq 1/\mathbb{E}[1/X_T]$ due to convexity.

### **Equity Derivatives**

For **variance swaps**, use the stock measure to simplify replication arguments.

For **quanto equity options**, adjust the drift using correlations.

---

## **18. Summary: The Power of Numeraire Change**

| **Aspect** | **Insight** |
|------------|-------------|
| **Conceptual** | Prices are invariant; measures change |
| **Computational** | Choose numeraire to simplify expectations |
| **Theoretical** | Reveals deep symmetries (e.g., put-call) |
| **Practical** | Essential for multi-asset, FX, rates |
| **Elegant** | Converts complex payoffs to simple probabilities |

### **The Master Equations**

$$\boxed{V_t = N_t \mathbb{E}^{\mathbb{Q}^N}\left[\frac{V_T}{N_T} \mid \mathcal{F}_t\right]}$$

$$\boxed{\frac{d\mathbb{Q}^N}{d\mathbb{Q}} = \frac{N_T/B_T}{N_0/B_0}}$$

$$\boxed{dW_t^{\mathbb{Q}^N} = dW_t^{\mathbb{Q}} - \sigma_N dt}$$

These three formulas encode the **entire theory**!

---

## **19. The Philosophy**

Change of numeraire reveals that **there is no "true" probability measure** in finance. The physical measure $\mathbb{P}$ is inaccessible for pricing. Instead:

- We have **infinitely many equivalent martingale measures**
- Each corresponds to a choice of numeraire
- All give the **same prices** (no-arbitrage)
- We choose the most **convenient** for each problem

This is the **fundamental flexibility** of modern derivative pricing!

---

Would you like me to explore:
- Detailed derivations for specific exotic options
- Connection to term structure models (HJM, LMM)
- Variance swaps and volatility derivatives
- Multi-currency derivatives
- The relationship to Feynman-Kac under different numeraires
- Numerical implementation strategies for Monte Carlo under different measures?