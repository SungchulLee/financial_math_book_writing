# Numéraire and Change of Measure


The [Fundamental Theorem of Asset Pricing](fundamental_theorem_of_asset_pricing.md) guarantees the existence of an equivalent martingale measure (EMM) relative to a chosen numéraire. This chapter develops the **numéraire framework** in full: we define what a numéraire is, state and prove the **change of numéraire theorem**, and show through worked examples how choosing the right numéraire can dramatically simplify derivative pricing.

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

$$V_0 = S^2_0 \bigl[R_0\, \Phi(d_1) - \Phi(d_2)\bigr]$$

where $R_0 = S^1_0 / S^2_0$ and

$$d_1 = \frac{\ln(R_0) + \frac{1}{2}\sigma_R^2 T}{\sigma_R \sqrt{T}}, \qquad d_2 = d_1 - \sigma_R\sqrt{T}$$

Substituting $S^2_0 R_0 = S^1_0$:

$$\boxed{V_0 = S^1_0\, \Phi(d_1) - S^2_0\, \Phi(d_2)}$$

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
