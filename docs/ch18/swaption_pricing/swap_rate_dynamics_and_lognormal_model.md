# Swap Rate Dynamics and Lognormal Model

!!! tip "Key Idea"
    The Black swaption formula requires an assumption about the dynamics of the swap rate. The simplest and most widely used assumption is that the swap rate follows a lognormal process under the annuity measure.

---

## Motivation

From the annuity measure framework, swaption pricing reduces to:

$$
V(t) = N A(t)\,
\mathbb{E}^{\mathbb{Q}^A}
\left[(S(T_m) - K)^+\right]
$$

To compute this expectation, we need a model for the evolution of the swap rate $S(t)$.

---

## Modeling the Swap Rate Directly

Instead of modeling:

- short rates
- entire yield curve

we model the **swap rate itself**.

This is similar to:

- modeling forward prices in Black's formula

---

## Lognormal Model

Assume that under the annuity measure:

$$
dS(t) = \sigma_S\, S(t)\, dW_t^A
$$

where:

- $\sigma_S$: constant volatility
- $W_t^A$: Brownian motion under $\mathbb{Q}^A$

---

## Key Properties

- No drift term (martingale under $\mathbb{Q}^A$)
- Lognormal distribution
- Always positive (when $S(t) > 0$)

---

## Solution

The solution to this SDE is:

$$
S(T_m) = S(t)
\exp\left(
-\frac{1}{2}\sigma_S^2 (T_m - t)

+ \sigma_S \sqrt{T_m - t}\, Z
\right)
$$

where $Z \sim N(0,1)$.

---

## Distribution

Thus:

$$
\ln S(T_m) \sim \mathcal{N}
\left(
\ln S(t) - \frac{1}{2}\sigma_S^2 (T_m - t),
\;
\sigma_S^2 (T_m - t)
\right)
$$

---

## Why Lognormal?

The lognormal assumption is used because:

1. Consistency with Black model
2. Analytical tractability
3. Positive rates (in classical settings)

---

## Limitations

- Cannot handle negative rates well
- Implies constant volatility
- Cannot reproduce volatility smile

---

!!! tip "Key Idea"
    The lognormal model is not realistic, but it provides a tractable approximation that leads to closed-form pricing formulas.

---

## Alternative: Normal Model

In modern markets, especially with low or negative rates, a normal model is often used:

$$
dS(t) = \sigma\, dW_t
$$

This leads to the **Bachelier formula** instead of Black.

---

## Connection to Black Formula

Given lognormal dynamics:

- payoff = call option on $S(T_m)$
- distribution = lognormal

Thus, pricing reduces to evaluating:

$$
\mathbb{E}[(S(T_m) - K)^+]
$$

which yields the Black formula.

---

## Interpretation

The modeling assumption transforms:

- a general pricing problem
→ into a tractable option pricing problem

This mirrors the role of geometric Brownian motion in Black–Scholes.

---

!!! note "Big Picture"
    Swaption pricing combines:

    1. No-arbitrage framework (annuity measure)
    2. Modeling assumption (lognormal dynamics)
    3. Analytical formula (Black)

    Each step is essential:

    - measure → removes drift
    - model → specifies distribution
    - formula → computes price

---

## Bridge to More Advanced Models

More realistic models include:

- SABR (stochastic volatility)
- LIBOR Market Model (LMM)
- Hull–White model

These relax the assumptions of the lognormal model.

---

## Exercises

**Exercise 1.** Starting from the lognormal SDE $dS(t) = \sigma_S S(t)\, dW_t^A$, derive the explicit solution for $S(T)$ in terms of $S(t)$, $\sigma_S$, and a standard normal random variable. Clearly state any lemma or formula you use.

??? success "Solution"

    Apply Ito's lemma to $f(S) = \ln S$. We have $f'(S) = 1/S$ and $f''(S) = -1/S^2$, so:

    $$
    d\ln S(t) = \frac{1}{S}\,dS - \frac{1}{2}\frac{1}{S^2}\,(\sigma_S S)^2\,dt = \sigma_S\,dW_t^A - \frac{1}{2}\sigma_S^2\,dt
    $$

    Integrating from $t$ to $T$:

    $$
    \ln S(T) - \ln S(t) = -\frac{1}{2}\sigma_S^2(T - t) + \sigma_S\bigl(W_T^A - W_t^A\bigr)
    $$

    Since $W_T^A - W_t^A \sim N(0, T - t)$, we write $W_T^A - W_t^A = \sqrt{T - t}\,Z$ with $Z \sim N(0,1)$. Exponentiating:

    $$
    S(T) = S(t)\exp\!\left(-\frac{1}{2}\sigma_S^2(T - t) + \sigma_S\sqrt{T - t}\,Z\right)
    $$

    $\square$

---

**Exercise 2.** Under the lognormal model $dS(t) = \sigma_S S(t)\,dW_t^A$, compute $\mathbb{E}^{\mathbb{Q}^A}[S(T)]$ and $\operatorname{Var}^{\mathbb{Q}^A}[\ln S(T)]$.

??? success "Solution"

    **Expected value.** Since the SDE has no drift, $S(t)$ is a martingale under $\mathbb{Q}^A$. Therefore:

    $$
    \mathbb{E}^{\mathbb{Q}^A}[S(T)] = S(t)
    $$

    This can also be verified directly from the explicit solution using the moment-generating function of the normal distribution.

    **Variance of the log.** From the explicit solution:

    $$
    \ln S(T) = \ln S(t) - \frac{1}{2}\sigma_S^2(T - t) + \sigma_S\sqrt{T - t}\,Z
    $$

    The only random term is $\sigma_S\sqrt{T - t}\,Z$, so:

    $$
    \operatorname{Var}^{\mathbb{Q}^A}[\ln S(T)] = \sigma_S^2(T - t)
    $$

    The quantity $\sigma_S\sqrt{T - t}$ is the total standard deviation of the log-swap-rate, often called the **total implied volatility**.

    $\square$

---

**Exercise 3.** Explain why the lognormal model $dS = \sigma_S S\,dW$ cannot accommodate negative swap rates. Describe a concrete market scenario where this limitation becomes problematic and state what alternative model resolves the issue.

??? success "Solution"

    In the lognormal model the solution is:

    $$
    S(T) = S(t)\exp\!\left(-\tfrac{1}{2}\sigma_S^2(T-t) + \sigma_S\sqrt{T-t}\,Z\right)
    $$

    The exponential function is strictly positive for all real arguments. If the initial swap rate satisfies $S(t) > 0$, then $S(T) > 0$ almost surely. The model therefore assigns zero probability to the event $\{S(T) \le 0\}$.

    **Market scenario.** During the European sovereign-debt crisis and the post-2014 ECB negative-rate regime, EUR swap rates for short maturities fell below zero. Swaptions referencing these rates had positive market prices for strikes $K < 0$, yet the lognormal Black formula produces a price of zero for any negative strike because $S(T) > 0$ a.s.

    **Resolution.** The **normal (Bachelier) model** $dS = \sigma\,dW$ allows $S(T)$ to be negative (it is Gaussian). This model leads to the Bachelier pricing formula, which is well-defined for all real strikes and has become the market-standard quotation convention for interest-rate swaptions.

    $\square$

---

**Exercise 4.** Consider an at-the-money (ATM) payer swaption with $K = S(t) = S_0$. Write the ATM price under both the lognormal (Black) model and the normal (Bachelier) model, and show that they are approximately equal when $\sigma_{\text{LN}} S_0 \approx \sigma_N$.

??? success "Solution"

    **Lognormal (Black) ATM price.** When $K = S_0$ the Black formula simplifies. The log-moneyness is zero, so $d_1 = \tfrac{1}{2}\sigma_{\text{LN}}\sqrt{\tau}$ and $d_2 = -\tfrac{1}{2}\sigma_{\text{LN}}\sqrt{\tau}$ where $\tau = T_m - t$. The price per unit notional and annuity is:

    $$
    C_{\text{Black}} = S_0\bigl[\mathcal{N}(d_1) - \mathcal{N}(d_2)\bigr] = S_0\bigl[2\Phi(\tfrac{1}{2}\sigma_{\text{LN}}\sqrt{\tau}) - 1\bigr]
    $$

    For small $\sigma_{\text{LN}}\sqrt{\tau}$, using $\Phi(x) \approx \tfrac{1}{2} + \tfrac{x}{\sqrt{2\pi}}$:

    $$
    C_{\text{Black}} \approx S_0 \cdot \frac{\sigma_{\text{LN}}\sqrt{\tau}}{\sqrt{2\pi}} = \frac{\sigma_{\text{LN}} S_0 \sqrt{\tau}}{\sqrt{2\pi}}
    $$

    **Normal (Bachelier) ATM price.** The Bachelier ATM formula gives:

    $$
    C_{\text{Bach}} = \sigma_N \sqrt{\frac{\tau}{2\pi}}
    $$

    **Comparison.** Setting the two ATM prices equal:

    $$
    \frac{\sigma_{\text{LN}} S_0 \sqrt{\tau}}{\sqrt{2\pi}} \approx \frac{\sigma_N \sqrt{\tau}}{\sqrt{2\pi}}
    $$

    which yields the conversion rule $\sigma_N \approx \sigma_{\text{LN}} S_0$. This relationship is widely used in practice to convert between lognormal and normal implied volatilities for ATM swaptions. It becomes exact in the limit $\sigma_{\text{LN}}\sqrt{\tau} \to 0$.

    $\square$
