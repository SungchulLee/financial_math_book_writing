# Numéraire Techniques


**Numéraire techniques** provide a unified framework for changing probability measures and simplifying derivative pricing by choosing an appropriate reference asset.

---

## What is a numéraire?


A **numéraire** is a strictly positive tradable asset \(N_t\) used to measure value.
Prices expressed in units of \(N_t\) are

\[
\tilde S_t = \frac{S_t}{N_t}.
\]



---

## Fundamental theorem of numéraire change


For any admissible numéraire \(N_t\), there exists a probability measure \(\mathbb{Q}^N\) such that

\[
\frac{S_t}{N_t} \text{ is a martingale under } \mathbb{Q}^N.
\]



This generalizes the risk-neutral measure concept.

---

## Examples of numeraires


Common choices include:
- money-market account \(B_t\) → risk-neutral measure,
- zero-coupon bond \(P(t,T)\) → T-forward measure,
- swap annuity → swap measure.

Each choice simplifies pricing of specific products.

---

## Pricing with numéraires


If payoff \(V_T\) is measurable at \(T\),

\[
V_t = N_t\,\mathbb{E}^{\mathbb{Q}^N}\left[
\frac{V_T}{N_T} \middle| \mathcal{F}_t
\right].
\]



Choosing \(N_t\) wisely can remove discounting or complex drifts.

---

## Key takeaways


- Numéraire choice determines the pricing measure.
- Forward measures are special cases of numéraire techniques.
- Proper numéraire selection simplifies valuation and dynamics.

---

## Further reading


- Geman, El Karoui & Rochet, numéraire theory.
- Brigo & Mercurio, change of measure methods.

---

## Exercises

**Exercise 1.** Let $N_t^{(1)} = B_t$ (money-market account) and $N_t^{(2)} = P(t, T)$ (zero-coupon bond). Write down the Radon--Nikodym derivative $d\mathbb{Q}^{(2)}/d\mathbb{Q}^{(1)}|_{\mathcal{F}_t}$ and verify that it defines a valid density process (i.e., it is a positive martingale under $\mathbb{Q}^{(1)}$ with initial value 1).

??? success "Solution to Exercise 1"

    **Radon--Nikodym derivative.** Let $N_t^{(1)} = B_t$ and $N_t^{(2)} = P(t, T)$. The general numéraire change formula gives

    $$
    \frac{d\mathbb{Q}^{(2)}}{d\mathbb{Q}^{(1)}}\bigg|_{\mathcal{F}_t} = \frac{N_t^{(2)} / N_0^{(2)}}{N_t^{(1)} / N_0^{(1)}} = \frac{P(t, T) / P(0, T)}{B_t / 1} = \frac{P(t, T)}{P(0, T) \, B_t}
    $$

    **Verification of positivity.** Since $P(t, T) > 0$ (bond prices are strictly positive for $t < T$), $P(0, T) > 0$, and $B_t > 0$, the density is strictly positive.

    **Verification of initial value.** At $t = 0$:

    $$
    \frac{P(0, T)}{P(0, T) \cdot B_0} = \frac{P(0, T)}{P(0, T) \cdot 1} = 1
    $$

    **Verification of the martingale property under $\mathbb{Q}^{(1)}$.** We need to show that $L_t = P(t, T)/(P(0, T) B_t)$ is a $\mathbb{Q}^{(1)}$-martingale. Note that $L_t = \frac{1}{P(0,T)} \cdot \frac{P(t,T)}{B_t}$.

    Under $\mathbb{Q}^{(1)} = \mathbb{Q}$ (the risk-neutral measure with numéraire $B_t$), the discounted price of any tradable asset is a martingale. Since $P(t, T)$ is the price of a tradable asset (the zero-coupon bond), $P(t, T)/B_t$ is a $\mathbb{Q}$-martingale. Multiplying by the positive constant $1/P(0, T)$ preserves the martingale property.

    Therefore $L_t$ is a positive $\mathbb{Q}^{(1)}$-martingale with $L_0 = 1$, confirming it is a valid Radon--Nikodym density process.

---

**Exercise 2.** A derivative pays $V_T = S_T^2$ at time $T$, where $S_t$ follows geometric Brownian motion $dS_t = rS_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}}$ under the risk-neutral measure with numéraire $B_t$. Compute $\mathbb{E}^{\mathbb{Q}}[e^{-rT}S_T^2]$ directly. Then choose $N_t = S_t$ as the numéraire and compute the same price as $S_0\,\mathbb{E}^{\mathbb{Q}^S}[S_T]$, verifying that the two approaches agree. What are the dynamics of $S_t$ under the measure $\mathbb{Q}^S$?

??? success "Solution to Exercise 2"

    **Direct computation under $\mathbb{Q}$.** Under $\mathbb{Q}$, $S_t = S_0 \exp((r - \sigma^2/2)t + \sigma W_t^{\mathbb{Q}})$, so

    $$
    S_T^2 = S_0^2 \exp\!\left((2r - \sigma^2)T + 2\sigma W_T^{\mathbb{Q}}\right)
    $$

    $$
    \mathbb{E}^{\mathbb{Q}}[e^{-rT}S_T^2] = S_0^2 e^{-rT} \exp\!\left((2r - \sigma^2)T\right) \mathbb{E}^{\mathbb{Q}}\!\left[\exp(2\sigma W_T^{\mathbb{Q}})\right]
    $$

    Since $W_T^{\mathbb{Q}} \sim N(0, T)$, $\mathbb{E}[\exp(2\sigma W_T^{\mathbb{Q}})] = \exp(2\sigma^2 T)$. Therefore:

    $$
    \mathbb{E}^{\mathbb{Q}}[e^{-rT}S_T^2] = S_0^2 \exp\!\left(-rT + 2rT - \sigma^2 T + 2\sigma^2 T\right) = S_0^2 \exp\!\left((r + \sigma^2)T\right)
    $$

    **Computation using $N_t = S_t$ as numéraire.** The pricing formula gives

    $$
    V_0 = S_0 \, \mathbb{E}^{\mathbb{Q}^S}\!\left[\frac{S_T^2}{S_T}\right] = S_0 \, \mathbb{E}^{\mathbb{Q}^S}[S_T]
    $$

    **Dynamics under $\mathbb{Q}^S$.** The Radon--Nikodym derivative is

    $$
    \frac{d\mathbb{Q}^S}{d\mathbb{Q}}\bigg|_{\mathcal{F}_t} = \frac{S_t / S_0}{B_t} = \frac{S_t}{S_0 e^{rt}}
    $$

    Since $S_t/B_t$ has volatility $\sigma$, Girsanov's theorem gives $dW_t^S = dW_t^{\mathbb{Q}} - \sigma\,dt$, where $W_t^S$ is a Brownian motion under $\mathbb{Q}^S$.

    Under $\mathbb{Q}^S$, substituting $dW_t^{\mathbb{Q}} = dW_t^S + \sigma\,dt$:

    $$
    dS_t = rS_t\,dt + \sigma S_t(dW_t^S + \sigma\,dt) = (r + \sigma^2)S_t\,dt + \sigma S_t\,dW_t^S
    $$

    Therefore $S_T = S_0 \exp((r + \sigma^2/2)T + \sigma W_T^S)$ and

    $$
    \mathbb{E}^{\mathbb{Q}^S}[S_T] = S_0 \exp\!\left((r + \sigma^2/2)T\right) \exp(\sigma^2 T/2) = S_0 \exp\!\left((r + \sigma^2)T\right)
    $$

    **Final price:**

    $$
    V_0 = S_0 \cdot S_0 \exp\!\left((r + \sigma^2)T\right) = S_0^2 \exp\!\left((r + \sigma^2)T\right)
    $$

    Both methods agree.

---

**Exercise 3.** Suppose there are two tradable assets $N_t^{(1)}$ and $N_t^{(2)}$ with associated measures $\mathbb{Q}^{(1)}$ and $\mathbb{Q}^{(2)}$. Show that the Radon--Nikodym derivative for the composite change $\mathbb{Q}^{(1)} \to \mathbb{Q}^{(2)}$ is

$$
\frac{d\mathbb{Q}^{(2)}}{d\mathbb{Q}^{(1)}}\bigg|_{\mathcal{F}_t} = \frac{N_t^{(2)} / N_0^{(2)}}{N_t^{(1)} / N_0^{(1)}}
$$

and verify that this is consistent with the individual changes from a common reference measure $\mathbb{Q}$.

??? success "Solution to Exercise 3"

    **From a common reference measure.** Let $\mathbb{Q}$ be any reference measure. The changes from $\mathbb{Q}$ to $\mathbb{Q}^{(k)}$ (for $k = 1, 2$) are given by

    $$
    \frac{d\mathbb{Q}^{(k)}}{d\mathbb{Q}}\bigg|_{\mathcal{F}_t} = \frac{N_t^{(k)} / N_0^{(k)}}{B_t}
    $$

    where $B_t$ is the numéraire for $\mathbb{Q}$.

    **Composite change.** The chain rule for Radon--Nikodym derivatives gives

    $$
    \frac{d\mathbb{Q}^{(2)}}{d\mathbb{Q}^{(1)}}\bigg|_{\mathcal{F}_t} = \frac{d\mathbb{Q}^{(2)}/d\mathbb{Q}|_{\mathcal{F}_t}}{d\mathbb{Q}^{(1)}/d\mathbb{Q}|_{\mathcal{F}_t}}
    $$

    Substituting:

    $$
    \frac{d\mathbb{Q}^{(2)}}{d\mathbb{Q}^{(1)}}\bigg|_{\mathcal{F}_t} = \frac{N_t^{(2)} / N_0^{(2)} / B_t}{N_t^{(1)} / N_0^{(1)} / B_t} = \frac{N_t^{(2)} / N_0^{(2)}}{N_t^{(1)} / N_0^{(1)}}
    $$

    The common reference numéraire $B_t$ cancels, confirming the formula is independent of the choice of $\mathbb{Q}$.

    **Verification.** At $t = 0$: $\frac{N_0^{(2)}/N_0^{(2)}}{N_0^{(1)}/N_0^{(1)}} = \frac{1}{1} = 1$. The density starts at 1.

    The ratio $\frac{N_t^{(2)}/N_0^{(2)}}{N_t^{(1)}/N_0^{(1)}} = \frac{1}{N_0^{(2)}/N_0^{(1)}} \cdot \frac{N_t^{(2)}}{N_t^{(1)}}$ is the ratio of two positive tradable assets (up to a constant), so it is positive. Under $\mathbb{Q}^{(1)}$, the process $N_t^{(2)}/N_t^{(1)}$ is a martingale (since $\mathbb{Q}^{(1)}$ makes any tradable asset divided by $N_t^{(1)}$ a martingale). Multiplying by a positive constant preserves the martingale property. Hence the density process is a valid positive $\mathbb{Q}^{(1)}$-martingale with initial value 1.

---

**Exercise 4.** Explain why the money-market account $B_t = \exp(\int_0^t r_s\,ds)$ is a valid numéraire even when the short rate $r_t$ is stochastic, whereas a zero-coupon bond $P(t, T)$ is only useful as a numéraire for pricing payoffs at or before time $T$. What goes wrong if you try to use $P(t, T)$ to price a payoff at time $T' > T$?

??? success "Solution to Exercise 4"

    **Why $B_t$ is always a valid numéraire:**

    1. **Strict positivity:** $B_t = \exp(\int_0^t r_s\,ds) > 0$ for all $t \geq 0$, regardless of whether $r_t$ is stochastic or even negative (the exponential of any real number is positive).
    2. **Tradability:** $B_t$ represents the value of continuously rolling over at the instantaneous short rate, which is a self-financing strategy.
    3. **No maturity constraint:** $B_t$ is defined for all $t \geq 0$, so it can serve as a numéraire for payoffs at any time $T$.

    **Why $P(t, T)$ is limited to payoffs at or before $T$:**

    1. **Numéraire at payment date:** For the pricing formula $V_0 = N_0\,\mathbb{E}^{\mathbb{Q}^N}[V_{T'}/N_{T'}]$, the numéraire $N_{T'}$ must be well-defined and strictly positive at the payment date $T'$.
    2. **At maturity:** $P(T, T) = 1 > 0$, so $P(t, T)$ works perfectly for payoffs at time $T$.
    3. **Before maturity:** For $T' < T$, $P(T', T) > 0$ is still well-defined, so $P(t, T)$ also works.

    **What goes wrong for $T' > T$:**

    For a payoff at $T' > T$, the pricing formula requires

    $$
    V_0 = P(0, T)\,\mathbb{E}^{\mathbb{Q}^T}\!\left[\frac{V_{T'}}{P(T', T)}\right]
    $$

    But $P(T', T)$ for $T' > T$ is not the price of the zero-coupon bond (which has already matured at $T$). After maturity, $P(T, T) = 1$ and the bond ceases to exist as a tradable asset for $t > T$. One would need to define how the proceeds are reinvested after $T$, which brings us back to the money-market account. Formally, the process $P(t, T)$ for $t > T$ would need to be extended as $P(t, T) = B_t / B_T$ (reinvesting at the short rate), but this is just the money-market account renormalized, defeating the purpose of using the bond as numéraire.

    In summary, the bond numéraire naturally "expires" at $T$, while the money-market account is perpetual.

---

**Exercise 5.** A foreign-exchange option pays $\max(X_T - K, 0)$ in domestic currency at time $T$, where $X_t$ is the spot exchange rate. The domestic and foreign money-market accounts are $B_t^d$ and $B_t^f$. Show that $X_t B_t^f / B_t^d$ is a martingale under the domestic risk-neutral measure, and use this to identify the natural numéraire for pricing this option. What is the drift of $X_t$ under the domestic measure?

??? success "Solution to Exercise 5"

    **Martingale property of $X_t B_t^f / B_t^d$.** Under the domestic risk-neutral measure $\mathbb{Q}^d$ (with numéraire $B_t^d$), every tradable asset denominated in domestic currency, discounted by $B_t^d$, is a martingale.

    Consider holding one unit of foreign currency. At time $t$, its domestic value is $X_t$ (the exchange rate). By investing this foreign currency in the foreign money-market account, the value at time $t$ of an initial investment made at time $0$ is $X_t B_t^f$ in domestic currency. This is a tradable strategy (buy foreign currency, invest at foreign short rate). Therefore

    $$
    \frac{X_t B_t^f}{B_t^d}
    $$

    must be a $\mathbb{Q}^d$-martingale.

    **Drift of $X_t$ under $\mathbb{Q}^d$.** Let $dX_t = \mu_X X_t\,dt + \sigma_X X_t\,dW_t^d$. The discounted foreign investment is

    $$
    \frac{X_t B_t^f}{B_t^d} = X_t \exp\!\left(\int_0^t (r_s^f - r_s^d)\,ds\right)
    $$

    For this to be a martingale, applying Itô's formula (with constant rates for simplicity):

    $$
    d\!\left(\frac{X_t B_t^f}{B_t^d}\right) = \frac{B_t^f}{B_t^d}\left[(\mu_X + r^f - r^d)X_t\,dt + \sigma_X X_t\,dW_t^d\right]
    $$

    Setting the drift to zero: $\mu_X + r^f - r^d = 0$, so

    $$
    \mu_X = r^d - r^f
    $$

    The exchange rate dynamics under $\mathbb{Q}^d$ are

    $$
    dX_t = (r^d - r^f) X_t\,dt + \sigma_X X_t\,dW_t^d
    $$

    This is the **interest rate parity** relation in continuous time: the drift of the exchange rate equals the interest rate differential.

    **Natural numéraire for the FX option.** The payoff $\max(X_T - K, 0)$ is in domestic currency at time $T$. The natural numéraire is $B_t^d$ (domestic money-market account) with the domestic risk-neutral measure $\mathbb{Q}^d$:

    $$
    V_0 = e^{-r^d T}\,\mathbb{E}^{\mathbb{Q}^d}[\max(X_T - K, 0)]
    $$

    Under $\mathbb{Q}^d$, $X_t$ is a GBM with drift $r^d - r^f$, so $X_T$ is lognormal and the Garman--Kohlhagen formula (the FX analogue of Black--Scholes) applies:

    $$
    V_0 = X_0 e^{-r^f T} N(d_1) - K e^{-r^d T} N(d_2)
    $$

    where $d_1 = \frac{\ln(X_0/K) + (r^d - r^f + \sigma_X^2/2)T}{\sigma_X\sqrt{T}}$ and $d_2 = d_1 - \sigma_X\sqrt{T}$.

---

**Exercise 6.** Consider a stock $S_t$ paying a continuous dividend yield $q$. The reinvested stock price $\hat{S}_t = S_t e^{qt}$ is a valid numéraire. Derive the Radon--Nikodym derivative from $\mathbb{Q}$ (money-market numéraire) to $\mathbb{Q}^{\hat{S}}$ (stock numéraire) and show that under $\mathbb{Q}^{\hat{S}}$, the process $B_t/\hat{S}_t$ is a martingale. Use this to price a European put option with payoff $\max(K - S_T, 0)$.

??? success "Solution to Exercise 6"

    **Setup.** Under $\mathbb{Q}$, the stock with continuous dividends satisfies $dS_t = (r - q)S_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}}$. The reinvested stock price $\hat{S}_t = S_t e^{qt}$ satisfies

    $$
    d\hat{S}_t = e^{qt}(dS_t + qS_t\,dt) = e^{qt}[(r - q)S_t + qS_t]\,dt + e^{qt}\sigma S_t\,dW_t^{\mathbb{Q}}
    $$

    $$
    = r\hat{S}_t\,dt + \sigma\hat{S}_t\,dW_t^{\mathbb{Q}}
    $$

    So $\hat{S}_t$ grows at rate $r$ under $\mathbb{Q}$, confirming it is a valid numéraire ($\hat{S}_t/B_t$ is a $\mathbb{Q}$-martingale).

    **Radon--Nikodym derivative.** From $\mathbb{Q}$ to $\mathbb{Q}^{\hat{S}}$:

    $$
    \frac{d\mathbb{Q}^{\hat{S}}}{d\mathbb{Q}}\bigg|_{\mathcal{F}_t} = \frac{\hat{S}_t / \hat{S}_0}{B_t} = \frac{S_t e^{qt}}{S_0 e^{rt}}
    $$

    Since $S_t = S_0\exp((r - q - \sigma^2/2)t + \sigma W_t^{\mathbb{Q}})$:

    $$
    \frac{d\mathbb{Q}^{\hat{S}}}{d\mathbb{Q}}\bigg|_{\mathcal{F}_t} = \exp\!\left(-\frac{\sigma^2}{2}t + \sigma W_t^{\mathbb{Q}}\right)
    $$

    This is the standard exponential martingale.

    **Girsanov transformation.** By Girsanov's theorem:

    $$
    dW_t^{\hat{S}} = dW_t^{\mathbb{Q}} - \sigma\,dt
    $$

    is a Brownian motion under $\mathbb{Q}^{\hat{S}}$.

    **$B_t/\hat{S}_t$ is a $\mathbb{Q}^{\hat{S}}$-martingale.** Under $\mathbb{Q}^{\hat{S}}$, any tradable asset divided by $\hat{S}_t$ is a martingale. Since $B_t$ is tradable, $B_t/\hat{S}_t$ is a $\mathbb{Q}^{\hat{S}}$-martingale.

    We can verify directly: $B_t/\hat{S}_t = e^{rt}/(S_t e^{qt}) = e^{(r-q)t}/S_t$. Under $\mathbb{Q}^{\hat{S}}$, using $dW_t^{\mathbb{Q}} = dW_t^{\hat{S}} + \sigma\,dt$:

    $$
    dS_t = (r - q)S_t\,dt + \sigma S_t(dW_t^{\hat{S}} + \sigma\,dt) = (r - q + \sigma^2)S_t\,dt + \sigma S_t\,dW_t^{\hat{S}}
    $$

    By Itô's formula for $1/S_t$:

    $$
    d(1/S_t) = -(r - q + \sigma^2)/S_t\,dt - \sigma/S_t\,dW_t^{\hat{S}} + \sigma^2/S_t\,dt
    $$

    $$
    = -(r - q)/S_t\,dt - \sigma/S_t\,dW_t^{\hat{S}}
    $$

    Then $d(e^{(r-q)t}/S_t) = e^{(r-q)t}[(r-q)/S_t\,dt + d(1/S_t)] = -\sigma e^{(r-q)t}/S_t\,dW_t^{\hat{S}}$, which is driftless, confirming the martingale property.

    **Pricing the European put.** The put payoff is $\max(K - S_T, 0) = K\max(1 - S_T/K, 0)$. Using numéraire $\hat{S}_t$:

    $$
    P_0 = \hat{S}_0\,\mathbb{E}^{\mathbb{Q}^{\hat{S}}}\!\left[\frac{\max(K - S_T, 0)}{\hat{S}_T}\right] = S_0\,\mathbb{E}^{\mathbb{Q}^{\hat{S}}}\!\left[\frac{K\max(1 - S_T/K, 0)}{S_T e^{qT}}\right]
    $$

    $$
    = S_0 K e^{-qT}\,\mathbb{E}^{\mathbb{Q}^{\hat{S}}}\!\left[\frac{\max(1 - S_T/K, 0)}{S_T}\right]
    $$

    Alternatively, using the standard approach, the put price under $\mathbb{Q}$ is

    $$
    P_0 = e^{-rT}\mathbb{E}^{\mathbb{Q}}[\max(K - S_T, 0)] = Ke^{-rT}N(-d_2) - S_0 e^{-qT}N(-d_1)
    $$

    where

    $$
    d_1 = \frac{\ln(S_0/K) + (r - q + \sigma^2/2)T}{\sigma\sqrt{T}}, \qquad d_2 = d_1 - \sigma\sqrt{T}
    $$

    To use the stock numéraire more cleanly, write the put as $\max(K - S_T, 0) = K\max(K^{-1}S_T^{-1}(K - S_T), 0) \cdot S_T/1$... The most elegant numéraire approach for the put is to decompose:

    $$
    P_0 = K\,e^{-rT}\,\mathbb{Q}(S_T < K) - S_0\,e^{-qT}\,\mathbb{Q}^{\hat{S}}(S_T < K)
    $$

    Under $\mathbb{Q}$: $\ln S_T \sim N(\ln S_0 + (r - q - \sigma^2/2)T,\;\sigma^2 T)$, so $\mathbb{Q}(S_T < K) = N(-d_2)$.

    Under $\mathbb{Q}^{\hat{S}}$: $\ln S_T \sim N(\ln S_0 + (r - q + \sigma^2/2)T,\;\sigma^2 T)$, so $\mathbb{Q}^{\hat{S}}(S_T < K) = N(-d_1)$.

    Therefore:

    $$
    P_0 = Ke^{-rT}N(-d_2) - S_0 e^{-qT}N(-d_1)
    $$

    This is the Black--Scholes put formula with continuous dividends, derived via the numéraire change.
