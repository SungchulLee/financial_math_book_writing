# Numéraire and Change of Measure


The [Fundamental Theorem of Asset Pricing](../fundamental_theorem_of_asset_pricing/fundamental_theorem_of_asset_pricing.md) guarantees the existence of an equivalent martingale measure (EMM) relative to a chosen numéraire. This chapter develops the **numéraire framework** in full: we define what a numéraire is, state and prove the **change of numéraire theorem**, and show through worked examples how choosing the right numéraire can dramatically simplify derivative pricing.

The central message is that **prices are invariant under numéraire changes**. Different numéraires give different martingale measures but identical arbitrage-free prices. This is not merely a theoretical curiosity—it is one of the most powerful computational tools in quantitative finance.


## Numéraire: Definition and Requirements


**Definition.**
A **numéraire** is any traded asset $N_t$ satisfying $N_t > 0$ almost surely for all $t \in [0, T]$.

Strict positivity is the only mathematical requirement: it ensures that division $S^i_t / N_t$ is always well-defined.

Common choices of numéraire include the risk-free money market account $N_t = e^{rt}$, a zero-coupon bond $N_t = P(t, T)$, a risky stock, or even a portfolio of traded assets. There is **no requirement** that the numéraire be risk-free or deterministic. The widespread use of the money market account is a pedagogical convention, not a mathematical necessity.


## Normalized Prices and the Numéraire FTAP


Given a numéraire $N_t$, define the **normalized price** of each traded asset $S^i_t$ as

$$\tilde{S}^i_t = \frac{S^i_t}{N_t}$$

The FTAP, stated in its numéraire-general form, reads:

**Theorem (Numéraire FTAP).**
*The market is arbitrage-free if and only if there exists a probability measure $\mathbb{Q}^N \sim \mathbb{P}$ under which all normalized prices $\tilde{S}^i_t = S^i_t / N_t$ are martingales:*

$$\frac{S^i_t}{N_t} = \mathbb{E}^{\mathbb{Q}^N}\!\left[\frac{S^i_T}{N_T} \;\bigg|\; \mathcal{F}_t\right] \qquad \text{for all } i \text{ and } 0 \leq t \leq T$$

The measure $\mathbb{Q}^N$ is called the **$N$-martingale measure** or the **numéraire-associated measure**.


## General Pricing Formula


Let $\Phi_T$ be an $\mathcal{F}_T$-measurable contingent claim. Under the numéraire $N_t$, the arbitrage-free price process is

$$\boxed{V_t = N_t \cdot \mathbb{E}^{\mathbb{Q}^N}\!\left[\frac{\Phi_T}{N_T} \;\bigg|\; \mathcal{F}_t\right]}$$

This is the **master pricing formula**. Every standard pricing expression is a special case:

- Money market numéraire ($N_t = e^{rt}$): $V_t = e^{-r(T-t)} \mathbb{E}^{\mathbb{Q}}[\Phi_T \mid \mathcal{F}_t]$.
- Zero-coupon bond numéraire ($N_t = P(t,T)$): $V_t = P(t,T) \cdot \mathbb{E}^{\mathbb{Q}^T}[\Phi_T \mid \mathcal{F}_t]$.


## Change of Numéraire Theorem


The following theorem is the central result of this chapter.

**Theorem (Change of Numéraire).**
*Let $N_t$ and $M_t$ be two numéraires with associated martingale measures $\mathbb{Q}^N$ and $\mathbb{Q}^M$. Then:*

**(a) Radon–Nikodym derivative.** *The two measures are related by*

$$\frac{d\mathbb{Q}^M}{d\mathbb{Q}^N}\bigg|_{\mathcal{F}_t} = \frac{M_t / M_0}{N_t / N_0}$$

**(b) Pricing invariance.** *For any contingent claim $\Phi_T$,*

$$N_t \cdot \mathbb{E}^{\mathbb{Q}^N}\!\left[\frac{\Phi_T}{N_T} \;\bigg|\; \mathcal{F}_t\right] = M_t \cdot \mathbb{E}^{\mathbb{Q}^M}\!\left[\frac{\Phi_T}{M_T} \;\bigg|\; \mathcal{F}_t\right]$$


### Proof

**Part (a).**
Under $\mathbb{Q}^N$, the normalized price $M_t / N_t$ is a martingale (since $M_t$ is a traded asset). Define the process

$$L_t = \frac{M_t / N_t}{M_0 / N_0} = \frac{M_t / M_0}{N_t / N_0}$$

Then $L_t$ is a positive $\mathbb{Q}^N$-martingale with $L_0 = 1$ and $\mathbb{E}^{\mathbb{Q}^N}[L_T] = 1$ (by the martingale property). It therefore defines a probability measure $\mathbb{Q}^M$ via

$$\frac{d\mathbb{Q}^M}{d\mathbb{Q}^N}\bigg|_{\mathcal{F}_t} = L_t$$

We must verify that under $\mathbb{Q}^M$, the ratio $S^i_t / M_t$ is a martingale for every traded asset $S^i$. By the **abstract Bayes formula**, for any $\mathcal{F}_T$-measurable random variable $X$,

$$\mathbb{E}^{\mathbb{Q}^M}[X \mid \mathcal{F}_t] = \frac{\mathbb{E}^{\mathbb{Q}^N}[L_T X \mid \mathcal{F}_t]}{L_t}$$

Apply this to $X = S^i_T / M_T$:

$$\mathbb{E}^{\mathbb{Q}^M}\!\left[\frac{S^i_T}{M_T} \;\bigg|\; \mathcal{F}_t\right] = \frac{1}{L_t} \cdot \mathbb{E}^{\mathbb{Q}^N}\!\left[\frac{M_T / M_0}{N_T / N_0} \cdot \frac{S^i_T}{M_T} \;\bigg|\; \mathcal{F}_t\right] = \frac{N_0}{M_0 L_t} \cdot \mathbb{E}^{\mathbb{Q}^N}\!\left[\frac{S^i_T}{N_T} \;\bigg|\; \mathcal{F}_t\right]$$

Since $S^i_t / N_t$ is a $\mathbb{Q}^N$-martingale, the expectation on the right equals $S^i_t / N_t$. Substituting $L_t = (M_t / M_0)/(N_t / N_0)$:

$$\mathbb{E}^{\mathbb{Q}^M}\!\left[\frac{S^i_T}{M_T} \;\bigg|\; \mathcal{F}_t\right] = \frac{N_0}{M_0} \cdot \frac{N_t / N_0}{M_t / M_0} \cdot \frac{S^i_t}{N_t} = \frac{S^i_t}{M_t}$$

This confirms that $\mathbb{Q}^M$ is the $M$-martingale measure. $\square$

**Part (b).**
Pricing invariance follows immediately from the abstract Bayes formula. Starting from the $\mathbb{Q}^N$-price:

$$V_t = N_t \cdot \mathbb{E}^{\mathbb{Q}^N}\!\left[\frac{\Phi_T}{N_T} \;\bigg|\; \mathcal{F}_t\right]$$

Apply the Bayes formula with $X = \Phi_T / M_T$ and $L_T = (M_T/M_0)/(N_T/N_0)$:

$$\mathbb{E}^{\mathbb{Q}^M}\!\left[\frac{\Phi_T}{M_T} \;\bigg|\; \mathcal{F}_t\right] = \frac{1}{L_t} \cdot \mathbb{E}^{\mathbb{Q}^N}\!\left[L_T \cdot \frac{\Phi_T}{M_T} \;\bigg|\; \mathcal{F}_t\right] = \frac{N_0}{M_0 L_t} \cdot \mathbb{E}^{\mathbb{Q}^N}\!\left[\frac{\Phi_T}{N_T} \;\bigg|\; \mathcal{F}_t\right]$$

Multiplying both sides by $M_t$ and substituting $M_0 L_t = M_t N_0 / N_t$:

$$M_t \cdot \mathbb{E}^{\mathbb{Q}^M}\!\left[\frac{\Phi_T}{M_T} \;\bigg|\; \mathcal{F}_t\right] = N_t \cdot \mathbb{E}^{\mathbb{Q}^N}\!\left[\frac{\Phi_T}{N_T} \;\bigg|\; \mathcal{F}_t\right] = V_t$$

$\square$


## Connection to Girsanov's Theorem


In continuous-time models driven by Brownian motion, the abstract change-of-measure machinery takes a concrete form via Girsanov's theorem.

Suppose under $\mathbb{Q}^N$ the numéraire ratio $M_t / N_t$ follows

$$d\!\left(\frac{M_t}{N_t}\right) = \frac{M_t}{N_t}\bigl(\cdots\, dt + \eta_t \cdot dW^N_t\bigr)$$

where $W^N_t$ is a $\mathbb{Q}^N$-Brownian motion and $\eta_t$ is the volatility of the ratio process. Since $M_t/N_t$ is a $\mathbb{Q}^N$-martingale, the drift term vanishes and the Radon–Nikodym process is

$$L_t = \frac{M_t/N_t}{M_0/N_0} = \mathcal{E}\!\left(\int_0^t \eta_s \cdot dW^N_s\right)$$

where $\mathcal{E}$ denotes the stochastic exponential. By Girsanov's theorem, the process

$$W^M_t = W^N_t - \int_0^t \eta_s\, ds$$

is a Brownian motion under $\mathbb{Q}^M$. The drift adjustment $\eta_t$ encodes the difference between the two martingale measures.


## Examples


### Example 1: Money Market Account

Choose $N_t = e^{rt}$ (deterministic). This is the standard **risk-neutral measure** $\mathbb{Q}$. The pricing formula becomes

$$V_t = e^{-r(T-t)}\, \mathbb{E}^{\mathbb{Q}}[\Phi_T \mid \mathcal{F}_t]$$

Under $\mathbb{Q}$, all assets earn the risk-free rate in expectation: $\mathbb{E}^{\mathbb{Q}}[dS_t / S_t] = r\, dt$. The numéraire is deterministic, so the Radon–Nikodym derivative from the physical measure $\mathbb{P}$ to $\mathbb{Q}$ depends only on the market price of risk.


### Example 2: Zero-Coupon Bond and Forward Measure

Let $N_t = P(t, T)$, the price of a zero-coupon bond maturing at $T$. Since $P(T, T) = 1$, the pricing formula simplifies to

$$V_t = P(t, T) \cdot \mathbb{E}^{\mathbb{Q}^T}[\Phi_T \mid \mathcal{F}_t]$$

The expectation is taken directly over the payoff $\Phi_T$ without any discounting—the discount factor has been absorbed into the numéraire.

Under $\mathbb{Q}^T$, the **forward price** $F(t, T) = S_t / P(t, T)$ is a martingale:

$$F(t, T) = \mathbb{E}^{\mathbb{Q}^T}[S_T \mid \mathcal{F}_t]$$

This is the measure of choice for pricing interest-rate derivatives. For example, in the LIBOR market model, each caplet on the forward rate $L(T_{i-1}, T_i)$ is priced under the $T_i$-forward measure, where $L(T_{i-1}, T_i)$ is a martingale. This eliminates the need to model the drift of forward rates—a major computational simplification.

The Radon–Nikodym derivative from the risk-neutral measure $\mathbb{Q}$ to the $T$-forward measure $\mathbb{Q}^T$ is

$$\frac{d\mathbb{Q}^T}{d\mathbb{Q}}\bigg|_{\mathcal{F}_t} = \frac{P(t, T) / P(0, T)}{e^{rt} / 1} = \frac{P(t, T)}{P(0, T)\, e^{rt}}$$


### Example 3: Stock as Numéraire

Choosing a risky stock $S^j_t$ as numéraire, all relative prices $S^i_t / S^j_t$ are martingales under the associated measure $\mathbb{Q}^j$:

$$\frac{S^i_t}{S^j_t} = \mathbb{E}^{\mathbb{Q}^j}\!\left[\frac{S^i_T}{S^j_T} \;\bigg|\; \mathcal{F}_t\right]$$

This is useful for pricing options on ratios and exchange options.


### Example 4: Margrabe's Formula via Change of Numéraire

As a worked example of the computational power of numéraire changes, consider an **exchange option** with payoff

$$\Phi_T = (S^1_T - S^2_T)^+$$

the right to exchange asset 2 for asset 1 at maturity.

**Direct approach.** Under the risk-neutral measure, one must evaluate $e^{-rT}\, \mathbb{E}^{\mathbb{Q}}[(S^1_T - S^2_T)^+]$ with two correlated lognormal variables—a two-dimensional integral.

**Numéraire approach.** Choose $N_t = S^2_t$ as numéraire. Then

$$V_0 = S^2_0 \cdot \mathbb{E}^{\mathbb{Q}^2}\!\left[\left(\frac{S^1_T}{S^2_T} - 1\right)^{\!+}\right]$$

Under $\mathbb{Q}^2$, the ratio $R_t = S^1_t / S^2_t$ is a martingale. If both assets follow geometric Brownian motion, $R_t$ is itself a geometric Brownian motion (with volatility $\sigma_R = \sqrt{\sigma_1^2 - 2\rho\sigma_1\sigma_2 + \sigma_2^2}$). The expectation is now a **one-dimensional** Black–Scholes-type integral:

$$V_0 = S^2_0 \bigl[R_0\, \mathcal{N}(d_1) - \mathcal{N}(d_2)\bigr]$$

where $R_0 = S^1_0 / S^2_0$ and

$$d_1 = \frac{\ln(R_0) + \frac{1}{2}\sigma_R^2 T}{\sigma_R \sqrt{T}}, \qquad d_2 = d_1 - \sigma_R\sqrt{T}$$

Substituting $S^2_0 R_0 = S^1_0$:

$$\boxed{V_0 = S^1_0\, \mathcal{N}(d_1) - S^2_0\, \mathcal{N}(d_2)}$$

This is **Margrabe's formula** (1978). The change of numéraire reduced a two-dimensional problem to a one-dimensional one.


## Connection to Black–Scholes


In the Black–Scholes model $dS_t = \mu S_t\, dt + \sigma S_t\, dW_t$ with money market numéraire $N_t = e^{rt}$, the risk-neutral dynamics are

$$dS_t = rS_t\, dt + \sigma S_t\, dW^{\mathbb{Q}}_t$$

Now consider using the **stock itself** as numéraire ($N_t = S_t$). The bond price normalized by $S_t$ is

$$\frac{e^{rt}}{S_t}$$

Under the stock measure $\mathbb{Q}^S$, this ratio is a martingale. By Girsanov's theorem, the $\mathbb{Q}^S$-Brownian motion is $W^S_t = W^{\mathbb{Q}}_t - \sigma t$ (the drift adjustment equals the stock's volatility), and the normalized bond evolves as

$$d\!\left(\frac{e^{rt}}{S_t}\right) = \frac{e^{rt}}{S_t}\bigl(-\sigma\, dW^S_t\bigr)$$

confirming it is a driftless process (martingale) under $\mathbb{Q}^S$.

Since the Black–Scholes model has a single source of randomness and one risky asset, the market is complete and the EMM is unique regardless of the numéraire choice. Changing the numéraire from the money market to the stock changes the measure and the Brownian motion, but produces the same option prices.


## Interpretation and Significance


**Choice of units.** The numéraire is a choice of "unit of account" for the economy. Expressing all prices in terms of the numéraire is analogous to choosing a coordinate system in physics—the underlying reality (prices) is invariant, but the representation may be more or less convenient.

**Gauge freedom.** The invariance of prices under numéraire changes is sometimes called **gauge invariance** by analogy with physics. Just as physical laws are unchanged by a choice of reference frame, arbitrage-free prices are unchanged by the choice of numéraire.

**Computational tool.** In practice, the numéraire is chosen to simplify the expectation that must be computed. The forward measure eliminates discounting from interest-rate derivative pricing. The stock measure reduces exchange option pricing to a one-dimensional problem. The art of derivative pricing often lies in choosing the right numéraire.

**No privileged risk-free rate.** In markets with funding constraints, multiple collateral rates, or credit risk, there may be no single "risk-free" rate. The numéraire framework accommodates this naturally: each funding arrangement corresponds to a different numéraire and its associated measure.


## Summary


The numéraire framework shows that arbitrage-free pricing is invariant under the choice of reference asset. Any strictly positive traded asset may serve as numéraire, and each choice produces a corresponding martingale measure related to any other by a Radon–Nikodym derivative. The change-of-numéraire theorem, proved via the abstract Bayes formula, is the formal statement of this invariance. In practice, the technique is indispensable for pricing interest-rate derivatives (forward measure), exchange options (stock numéraire), and multi-currency products (foreign money market numéraire).


## References

- Geman, H., El Karoui, N., and Rochet, J.-C. (1995). *Changes of numéraire, changes of probability measure, and option pricing.* Journal of Applied Probability, 32(2), 443–458.

- Margrabe, W. (1978). *The value of an option to exchange one asset for another.* Journal of Finance, 33(1), 177–186.

- Brigo, D. and Mercurio, F. (2006). *Interest Rate Models—Theory and Practice.* 2nd edition, Springer.

- Shreve, S. E. (2004). *Stochastic Calculus for Finance II: Continuous-Time Models.* Springer.

- Björk, T. (2009). *Arbitrage Theory in Continuous Time.* 3rd edition, Oxford University Press.

---

## Exercises

**Exercise 1.** In the Black-Scholes model with $r = 0.05$, $\sigma = 0.3$, and $S_0 = 100$, compute the Radon–Nikodym derivative $d\mathbb{Q}^T / d\mathbb{Q}$ at time $T = 1$ when the numéraire changes from the money market account $e^{rt}$ to the zero-coupon bond $P(t, T)$. Express the result in terms of $P(0, T)$ and $e^{rT}$.

??? success "Solution to Exercise 1"
    In the Black--Scholes model with deterministic interest rates, $P(t, T) = e^{-r(T-t)}$. The Radon--Nikodym derivative from $\mathbb{Q}$ (money market numéraire $N_t = e^{rt}$) to $\mathbb{Q}^T$ (zero-coupon bond numéraire $M_t = P(t, T)$) is

    $$
    \frac{d\mathbb{Q}^T}{d\mathbb{Q}}\bigg|_{\mathcal{F}_t} = \frac{M_t / M_0}{N_t / N_0} = \frac{P(t, T) / P(0, T)}{e^{rt} / 1} = \frac{P(t, T)}{P(0, T) \, e^{rt}}
    $$

    At $t = T$:

    $$
    \frac{d\mathbb{Q}^T}{d\mathbb{Q}}\bigg|_{\mathcal{F}_T} = \frac{P(T, T)}{P(0, T) \, e^{rT}} = \frac{1}{P(0, T) \, e^{rT}}
    $$

    Since $P(0, T) = e^{-rT}$ in the deterministic rate model:

    $$
    \frac{d\mathbb{Q}^T}{d\mathbb{Q}}\bigg|_{\mathcal{F}_T} = \frac{1}{e^{-rT} \cdot e^{rT}} = \frac{1}{1} = 1
    $$

    With $r = 0.05$ and $T = 1$: $P(0, 1) = e^{-0.05}$ and $e^{rT} = e^{0.05}$, so the Radon--Nikodym derivative is $1/(e^{-0.05} \cdot e^{0.05}) = 1$.

    This result makes sense: when interest rates are deterministic, the zero-coupon bond is a deterministic function of time, so $P(t, T)/e^{rt}$ is deterministic. The change of numéraire from a deterministic money market account to a deterministic bond does not alter the measure. In the general expression, $d\mathbb{Q}^T/d\mathbb{Q} = 1/(P(0,T) \cdot e^{rT})$, valid for any $r$ and $T$.

---

**Exercise 2.** Two stocks follow geometric Brownian motion under the risk-neutral measure: $dS^1_t = r S^1_t\, dt + 0.2\, S^1_t\, dW^1_t$ and $dS^2_t = r S^2_t\, dt + 0.3\, S^2_t\, dW^2_t$, with $\text{Corr}(W^1, W^2) = 0.5$. Use Margrabe's formula to price the exchange option $(S^1_T - S^2_T)^+$ at $T = 0.5$, given $S^1_0 = 50$, $S^2_0 = 48$, and $r = 0.03$.

??? success "Solution to Exercise 2"
    The effective volatility for Margrabe's formula is

    $$
    \sigma_R = \sqrt{\sigma_1^2 - 2\rho\sigma_1\sigma_2 + \sigma_2^2} = \sqrt{0.04 - 2(0.5)(0.2)(0.3) + 0.09} = \sqrt{0.04 - 0.06 + 0.09} = \sqrt{0.07}
    $$

    The ratio of initial prices is $R_0 = S^1_0 / S^2_0 = 50/48$. With $T = 0.5$:

    $$
    d_1 = \frac{\ln(50/48) + \frac{1}{2}(0.07)(0.5)}{\sqrt{0.07} \cdot \sqrt{0.5}} = \frac{\ln(1.04167) + 0.0175}{\sqrt{0.035}}
    $$

    Computing: $\ln(1.04167) \approx 0.04082$ and $\sqrt{0.035} \approx 0.18708$. Therefore

    $$
    d_1 = \frac{0.04082 + 0.0175}{0.18708} = \frac{0.05832}{0.18708} \approx 0.3118
    $$

    $$
    d_2 = d_1 - \sigma_R\sqrt{T} = 0.3118 - 0.18708 \approx 0.1247
    $$

    Using the standard normal CDF: $\Phi(0.3118) \approx 0.6224$ and $\Phi(0.1247) \approx 0.5496$.

    Margrabe's formula gives:

    $$
    V_0 = S^1_0 \, \mathcal{N}(d_1) - S^2_0 \, \mathcal{N}(d_2) = 50 \times 0.6224 - 48 \times 0.5496 = 31.12 - 26.38 \approx 4.74
    $$

    Note that no discounting or risk-free rate appears in Margrabe's formula -- the exchange option price depends only on the initial prices, the relative volatility $\sigma_R$, and the time to maturity.

---

**Exercise 3.** Verify the pricing invariance formula directly for a simple one-period model. Let $\Omega = \{\omega_1, \omega_2\}$ with two assets: a bond paying 1.05 in both states and a stock with $S_0 = 10$, $S_1(\omega_1) = 14$, $S_1(\omega_2) = 8$. Compute the price of a call with payoff $\Phi = (\max(S_1 - 10, 0))$ using (a) the money market as numéraire and (b) the stock as numéraire. Verify both give the same answer.

??? success "Solution to Exercise 3"
    **Setup.** The bond pays $B_1 = 1.05$ in both states. The stock has $S_0 = 10$, $S_1(\omega_1) = 14$, $S_1(\omega_2) = 8$. The call payoff is $\Phi(\omega_1) = \max(14 - 10, 0) = 4$ and $\Phi(\omega_2) = \max(8 - 10, 0) = 0$.

    **(a) Money market as numéraire.**
    The numéraire is $N_0 = 1$, $N_1 = 1.05$. Discounted stock prices: $\tilde{S}_0 = 10$ and $\tilde{S}_1(\omega_1) = 14/1.05 = 40/3$, $\tilde{S}_1(\omega_2) = 8/1.05 = 160/21$.

    The martingale condition $\mathbb{E}^{\mathbb{Q}^N}[\tilde{S}_1] = \tilde{S}_0$ gives:

    $$
    q_1 \cdot \frac{40}{3} + (1 - q_1) \cdot \frac{160}{21} = 10
    $$

    $$
    q_1 \left(\frac{40}{3} - \frac{160}{21}\right) = 10 - \frac{160}{21} = \frac{210 - 160}{21} = \frac{50}{21}
    $$

    $$
    q_1 \cdot \frac{280 - 160}{21} = q_1 \cdot \frac{120}{21} = \frac{50}{21} \implies q_1 = \frac{50}{120} = \frac{5}{12}
    $$

    The call price is:

    $$
    V_0 = \frac{1}{1.05} \mathbb{E}^{\mathbb{Q}^N}[\Phi] = \frac{1}{1.05}\left(\frac{5}{12} \cdot 4 + \frac{7}{12} \cdot 0\right) = \frac{1}{1.05} \cdot \frac{20}{12} = \frac{20}{12.6} = \frac{100}{63}
    $$

    **(b) Stock as numéraire.**
    The numéraire is $M_t = S_t$, so $M_0 = 10$, $M_1(\omega_1) = 14$, $M_1(\omega_2) = 8$. The normalized bond: $B_1/S_1(\omega_1) = 1.05/14 = 3/40$ and $B_1/S_1(\omega_2) = 1.05/8 = 21/160$.

    The martingale condition for the normalized bond: $\mathbb{E}^{\mathbb{Q}^M}[B_1/S_1] = B_0/S_0 = 1/10$.

    $$
    q'_1 \cdot \frac{3}{40} + (1 - q'_1) \cdot \frac{21}{160} = \frac{1}{10}
    $$

    $$
    q'_1 \left(\frac{12}{160} - \frac{21}{160}\right) = \frac{1}{10} - \frac{21}{160} = \frac{16 - 21}{160} = -\frac{5}{160}
    $$

    $$
    q'_1 \cdot \left(-\frac{9}{160}\right) = -\frac{5}{160} \implies q'_1 = \frac{5}{9}
    $$

    The call price under the stock numéraire is:

    $$
    V_0 = S_0 \cdot \mathbb{E}^{\mathbb{Q}^M}\!\left[\frac{\Phi}{S_1}\right] = 10 \left(\frac{5}{9} \cdot \frac{4}{14} + \frac{4}{9} \cdot \frac{0}{8}\right) = 10 \cdot \frac{5}{9} \cdot \frac{2}{7} = 10 \cdot \frac{10}{63} = \frac{100}{63}
    $$

    Both numéraires give the same price $V_0 = 100/63 \approx 1.587$, confirming pricing invariance.

---

**Exercise 4.** Show that if $N_t$ is a numéraire (strictly positive traded asset) and $M_t / N_t$ is a $\mathbb{Q}^N$-martingale, then the Radon–Nikodym process $L_t = (M_t / M_0) / (N_t / N_0)$ satisfies $L_0 = 1$ and $\mathbb{E}^{\mathbb{Q}^N}[L_T] = 1$. Why are these two properties necessary and sufficient for $L_T$ to define a change of measure?

??? success "Solution to Exercise 4"
    **Showing $L_0 = 1$:** By definition,

    $$
    L_t = \frac{M_t / M_0}{N_t / N_0}
    $$

    At $t = 0$: $L_0 = (M_0/M_0)/(N_0/N_0) = 1/1 = 1$.

    **Showing $\mathbb{E}^{\mathbb{Q}^N}[L_T] = 1$:** Since $M_t/N_t$ is a $\mathbb{Q}^N$-martingale (both $M_t$ and $N_t$ are traded assets and $N_t$ is the numéraire), we have

    $$
    \mathbb{E}^{\mathbb{Q}^N}\!\left[\frac{M_T}{N_T}\right] = \frac{M_0}{N_0}
    $$

    Therefore

    $$
    \mathbb{E}^{\mathbb{Q}^N}[L_T] = \mathbb{E}^{\mathbb{Q}^N}\!\left[\frac{M_T/M_0}{N_T/N_0}\right] = \frac{N_0}{M_0} \cdot \mathbb{E}^{\mathbb{Q}^N}\!\left[\frac{M_T}{N_T}\right] = \frac{N_0}{M_0} \cdot \frac{M_0}{N_0} = 1
    $$

    **Why these two properties are necessary and sufficient:**

    - $L_0 = 1$ ensures that the total probability under the new measure equals 1 at time 0 (normalization).
    - $\mathbb{E}^{\mathbb{Q}^N}[L_T] = 1$ ensures that $\mathbb{Q}^M$ defined by $d\mathbb{Q}^M = L_T \, d\mathbb{Q}^N$ is a probability measure: $\mathbb{Q}^M(\Omega) = \mathbb{E}^{\mathbb{Q}^N}[L_T] = 1$.
    - Together with $L_T > 0$ a.s. (which follows from $M_T > 0$ and $N_T > 0$), these conditions make $L_T$ a valid Radon--Nikodym derivative that defines an equivalent probability measure $\mathbb{Q}^M \sim \mathbb{Q}^N$.

---

**Exercise 5.** In the context of interest rate modeling, explain why the $T$-forward measure is the natural choice for pricing a caplet on the LIBOR rate $L(T_{i-1}, T_i)$. What simplification does this numéraire choice provide compared to using the money market account?

??? success "Solution to Exercise 5"
    Under the money market numéraire $e^{rt}$, pricing a caplet on $L(T_{i-1}, T_i)$ requires computing

    $$
    V_0 = e^{-rT_i} \, \mathbb{E}^{\mathbb{Q}}\!\left[(L(T_{i-1}, T_i) - K)^+ \cdot \delta\right]
    $$

    where $\delta = T_i - T_{i-1}$ is the accrual period. Under $\mathbb{Q}$, the forward rate $L(T_{i-1}, T_i)$ is **not** a martingale -- it has a non-trivial drift that depends on the entire term structure of volatilities and correlations. This drift must be computed and modeled, making the expectation difficult to evaluate.

    Under the $T_i$-**forward measure** $\mathbb{Q}^{T_i}$ (with numéraire $P(t, T_i)$), the pricing formula becomes

    $$
    V_0 = P(0, T_i) \, \mathbb{E}^{\mathbb{Q}^{T_i}}\!\left[(L(T_{i-1}, T_i) - K)^+ \cdot \delta\right]
    $$

    The key simplification is that $L(T_{i-1}, T_i)$ is a **martingale** under $\mathbb{Q}^{T_i}$. This is because the forward LIBOR rate can be written as

    $$
    L(t, T_{i-1}, T_i) = \frac{1}{\delta}\left(\frac{P(t, T_{i-1})}{P(t, T_i)} - 1\right)
    $$

    and the ratio $P(t, T_{i-1})/P(t, T_i)$ is a $\mathbb{Q}^{T_i}$-martingale (as the ratio of a traded asset to the numéraire). Since $L$ is a martingale under $\mathbb{Q}^{T_i}$, it is driftless, and if modeled as lognormal, the caplet price is given directly by a Black-type formula with no drift correction needed. This is the foundation of the LIBOR market model (BGM model).

---

**Exercise 6.** Consider an exchange option $(S^1_T - S^2_T)^+$ in the Black-Scholes setting with $\sigma_1 = \sigma_2 = \sigma$ and $\rho = 1$ (perfect correlation). Show that Margrabe's formula reduces to $V_0 = \max(S^1_0 - S^2_0, 0)$. Interpret this result: why does the option have no time value when the two assets are perfectly correlated with the same volatility?

??? success "Solution to Exercise 6"
    With $\sigma_1 = \sigma_2 = \sigma$ and $\rho = 1$, the effective volatility in Margrabe's formula is

    $$
    \sigma_R = \sqrt{\sigma_1^2 - 2\rho\sigma_1\sigma_2 + \sigma_2^2} = \sqrt{\sigma^2 - 2\sigma^2 + \sigma^2} = \sqrt{0} = 0
    $$

    With $\sigma_R = 0$, the quantities $d_1$ and $d_2$ become:

    - If $R_0 = S^1_0/S^2_0 > 1$: $d_1 = d_2 = \ln(R_0)/(0) = +\infty$, so $\mathcal{N}(d_1) = \mathcal{N}(d_2) = 1$

    - If $R_0 < 1$: $d_1 = d_2 = -\infty$, so $\mathcal{N}(d_1) = \mathcal{N}(d_2) = 0$

    - If $R_0 = 1$: $d_1 = d_2 = 0/0$, which by continuity gives $\mathcal{N}(d_1) = \mathcal{N}(d_2) = 1/2$

    Applying Margrabe's formula $V_0 = S^1_0 \mathcal{N}(d_1) - S^2_0 \mathcal{N}(d_2)$:

    - If $S^1_0 > S^2_0$: $V_0 = S^1_0 - S^2_0$
    - If $S^1_0 < S^2_0$: $V_0 = 0$
    - If $S^1_0 = S^2_0$: $V_0 = S^1_0/2 - S^2_0/2 = 0$

    Therefore $V_0 = \max(S^1_0 - S^2_0, 0)$, which is just the intrinsic value with zero time value.

    **Interpretation:** When $\rho = 1$ and $\sigma_1 = \sigma_2$, the two assets are driven by the same Brownian motion with the same volatility, so $S^1_t/S^2_t$ is deterministic (it equals $S^1_0/S^2_0$ for all $t$). The ratio never changes, so there is no uncertainty about the relative value at maturity. The option is either surely in the money (if $S^1_0 > S^2_0$) or surely out of the money (if $S^1_0 \leq S^2_0$), and its value is simply the present value of the certain payoff. Since the exchange option payoff involves only the difference $S^1_T - S^2_T$ and both assets grow at the same rate, no discounting is needed, and the time value is exactly zero.
