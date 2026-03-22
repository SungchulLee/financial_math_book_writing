# Cap and Floor Pricing

Interest rate caps and floors are among the most actively traded OTC derivatives. A cap protects a floating-rate borrower against rising rates by paying the difference whenever the reference rate exceeds a strike, while a floor protects a lender against falling rates. Since a cap is a portfolio of individual caplets, and each caplet in the Hull-White model reduces to a put on a zero-coupon bond, the entire cap can be priced analytically. This section derives the cap and floor pricing formulas and compares the Hull-White result with Black's formula.

## Cap and Floor Structure

An interest rate cap on a notional $N$ with strike $K$ and payment dates $T_1, T_2, \ldots, T_n$ consists of $n$ individual caplets. Each caplet pays at $T_k$ based on the floating rate observed at $T_{k-1}$.

!!! info "Definition: Cap and Floor"
    $$\begin{array}{lllll}
    \displaystyle
    \text{Cap}(t_0) &=& \displaystyle\sum_{k=1}^{n} \text{Caplet}_k(t_0)
    \\[8pt]
    \displaystyle
    \text{Floor}(t_0) &=& \displaystyle\sum_{k=1}^{n} \text{Floorlet}_k(t_0)
    \end{array}$$

    where each caplet and floorlet has payoff at $T_k$:

    $$\begin{array}{lllll}
    \displaystyle
    \text{Caplet}_k(T_k) &=& N\tau_k\max(l_k(T_{k-1}) - K,\; 0)
    \\[4pt]
    \displaystyle
    \text{Floorlet}_k(T_k) &=& N\tau_k\max(K - l_k(T_{k-1}),\; 0)
    \end{array}$$

    Here $\tau_k = T_k - T_{k-1}$ is the accrual fraction and $l_k(T_{k-1}) = l(T_{k-1}; T_{k-1}, T_k)$ is the simply compounded forward rate set at $T_{k-1}$.

## Hull-White Caplet as a ZCB Put

The key insight for pricing individual caplets in the Hull-White model is that each caplet is equivalent to a put option on a zero-coupon bond. This equivalence allows direct application of the Hull-White ZCB option formula.

!!! info "Theorem: Caplet-ZCB Put Equivalence"
    A caplet with reset date $T_{k-1}$, payment date $T_k$, strike $K$, and notional $N$ equals

    $$
    \text{Caplet}_k(t_0) = \hat{N}\,V_p^{\text{ZCB}}\!\left(t_0,\, T_{k-1},\, T_k;\, \hat{K}\right)
    $$

    where $\hat{N} = N(1 + \tau_k K)$ and $\hat{K} = \frac{1}{1 + \tau_k K}$.

???+ note "Proof"

    Starting from the risk-neutral pricing formula:

    $$\begin{array}{lllll}
    \displaystyle
    \text{Caplet}_k(t_0)
    &=&\displaystyle
    \mathbb{E}^{\mathbb{Q}}\!\left[\frac{M(t_0)}{M(T_k)}\,N\tau_k\max(l_k(T_{k-1}) - K, 0)\,\Big|\,\mathcal{F}(t_0)\right]
    \end{array}$$

    Using the tower property and the relation $l_k(T_{k-1}) = \frac{1}{\tau_k}\!\left(\frac{1}{P(T_{k-1}, T_k)} - 1\right)$:

    $$\begin{array}{lllll}
    \displaystyle
    &=&\displaystyle
    \mathbb{E}^{\mathbb{Q}}\!\left[\frac{M(t_0)}{M(T_{k-1})}\,N\max\!\left(\frac{1}{P(T_{k-1}, T_k)} - (1 + \tau_k K),\; 0\right)P(T_{k-1}, T_k)\,\Big|\,\mathcal{F}(t_0)\right]
    \end{array}$$

    Rearranging:

    $$\begin{array}{lllll}
    \displaystyle
    &=&\displaystyle
    \mathbb{E}^{\mathbb{Q}}\!\left[\frac{M(t_0)}{M(T_{k-1})}\,N(1 + \tau_k K)\max\!\left(\frac{1}{1 + \tau_k K} - P(T_{k-1}, T_k),\; 0\right)\,\Big|\,\mathcal{F}(t_0)\right]
    \\[6pt]
    &=&\displaystyle
    \hat{N}\,V_p^{\text{ZCB}}(t_0,\, T_{k-1},\, T_k;\, \hat{K})
    \end{array}$$

    $\square$

Similarly, a floorlet equals a scaled ZCB call:

$$
\text{Floorlet}_k(t_0) = \hat{N}\,V_c^{\text{ZCB}}\!\left(t_0,\, T_{k-1},\, T_k;\, \hat{K}\right)
$$

## Hull-White Cap Formula

Combining the caplet decomposition with the Hull-White ZCB option pricing formula, the cap price is:

$$
\text{Cap}(t_0) = \sum_{k=1}^{n} \hat{N}_k\,V_p^{\text{ZCB}}\!\left(t_0,\, T_{k-1},\, T_k;\, \hat{K}_k\right)
$$

where for each caplet $k$:

$$\begin{array}{lllll}
\hat{N}_k &=& N(1 + \tau_k K)
\\[4pt]
\hat{K}_k &=& \frac{1}{1 + \tau_k K}
\end{array}$$

Each ZCB put $V_p^{\text{ZCB}}$ uses the Hull-White closed-form formula with option maturity $T_{k-1}$, bond maturity $T_k$, and strike $\hat{K}_k$.

!!! tip "Implementation Note"
    Unlike Jamshidian's trick for coupon bond options, no root-finding for $r^*$ is needed. Each caplet is independently priced as a ZCB put, and the cap price is simply the sum.

## Cap-Floor Parity

The difference between a cap and a floor with the same strike equals the value of a payer swap:

$$
\text{Cap}(t_0) - \text{Floor}(t_0) = N\!\left(P(t_0, T_0) - P(t_0, T_n) - K\sum_{k=1}^{n}\tau_k\,P(t_0, T_k)\right) = \text{IRS}^{\text{Payer}}(t_0)
$$

???+ note "Proof"

    For each reset period, the caplet-floorlet parity gives

    $$
    \text{Caplet}_k - \text{Floorlet}_k = N\tau_k\,P(t_0, T_k)\,(l_k(t_0) - K)
    $$

    Summing over all periods:

    $$\begin{array}{lllll}
    \displaystyle
    \text{Cap} - \text{Floor}
    &=&\displaystyle
    N\sum_{k=1}^{n}\tau_k\,P(t_0, T_k)(l_k(t_0) - K)
    \;=\;
    N\!\left(P(t_0, T_0) - P(t_0, T_n)\right) - NK\sum_{k=1}^{n}\tau_k\,P(t_0, T_k)
    \end{array}$$

    This is the payer swap value. $\square$

## Comparison with Black's Formula

In the market convention, caplets are quoted using Black's formula with an implied volatility $\sigma_k^{\text{Black}}$:

$$
\text{Caplet}_k^{\text{Black}}(t_0) = N\tau_k\,P(t_0, T_k)\!\left[l_k(t_0)\,\Phi(d_1) - K\,\Phi(d_2)\right]
$$

where

$$\begin{array}{lllll}
\displaystyle
d_1 &=& \displaystyle\frac{\log(l_k(t_0)/K) + \frac{1}{2}v_k^2}{v_k}
\\[8pt]
\displaystyle
d_2 &=& d_1 - v_k
\\[4pt]
v_k &=& \sigma_k^{\text{Black}}\sqrt{T_{k-1} - t_0}
\end{array}$$

Black's formula assumes the forward rate $l_k(t)$ is lognormal under $\mathbb{Q}^{T_k}$, while the Hull-White model produces a Gaussian (normal) short rate distribution. The two approaches give different implied volatility structures:

- **Black's formula**: Constant implied volatility across strikes produces a flat volatility smile.
- **Hull-White**: Since bond prices are exponential in the Gaussian $r$, the model generates implied volatilities that vary with strike, producing a volatility skew.

!!! info "Proposition: Hull-White Implied Volatility"
    For at-the-money caplets, the Hull-White and Black formulas produce similar prices. Away from ATM, the Hull-White model generates a systematic skew because the lognormal distribution (Black) and the distribution implied by the exponential of a Gaussian (Hull-White) have different tail behavior.

## Flat Volatility vs Spot Volatility

Cap prices are often quoted using two volatility conventions:

- **Flat (running) volatility**: A single volatility $\sigma^{\text{flat}}$ applied uniformly to all caplets in the cap. The flat vol equates the cap price to $\sum_k \text{Caplet}_k^{\text{Black}}(\sigma^{\text{flat}})$.

- **Spot volatility**: Each caplet $k$ uses its own volatility $\sigma_k^{\text{spot}}$. These are stripped from market cap quotes.

The Hull-White model with parameters $(\lambda, \sigma)$ implies a term structure of spot volatilities that is typically monotonically decreasing with maturity, consistent with the empirical pattern of a downward-sloping cap volatility curve.

## Numerical Example

Consider a 5-year annual cap with $N = \$1{,}000{,}000$, strike $K = 0.04$, annual resets at $T_0 = 0, T_1 = 1, \ldots, T_5 = 5$, and Hull-White parameters $\lambda = 0.05$, $\sigma = 0.01$.

For each caplet, $\hat{N}_k = 1{,}000{,}000 \times (1 + 0.04) = 1{,}040{,}000$ and $\hat{K}_k = 1/1.04 \approx 0.9615$.

The cap price equals the sum of five ZCB put prices:

$$
\text{Cap}(0) = \sum_{k=1}^{5} 1{,}040{,}000 \times V_p^{\text{ZCB}}(0,\, T_{k-1},\, T_k;\, 0.9615)
$$

Each ZCB put is priced using the Hull-White closed-form formula. The total cap price can then be backed out to a flat Black volatility for quoting purposes.

```python
def price_cap(hw, N, K, T_reset_dates, T_payment_dates):
    """Price an interest rate cap in the Hull-White model."""
    cap_price = 0.0
    for T_reset, T_pay in zip(T_reset_dates, T_payment_dates):
        tau_k = T_pay - T_reset
        N_hat = N * (1 + tau_k * K)
        K_hat = 1.0 / (1 + tau_k * K)
        zbp = hw.compute_ZCB_Option_Price(
            K_hat, T_reset, T_pay, CP=OptionType.PUT
        )
        cap_price += N_hat * zbp
    return cap_price
```

---

## Summary

Interest rate caps and floors are portfolios of caplets and floorlets. In the Hull-White model, each caplet reduces to a put on a zero-coupon bond via the equivalence $\text{Caplet}_k = \hat{N}\,V_p^{\text{ZCB}}(t_0, T_{k-1}, T_k; \hat{K})$, enabling fully analytic pricing. The cap-floor parity $\text{Cap} - \text{Floor} = \text{Payer Swap}$ holds model-independently. Compared to Black's formula, the Hull-White model generates a volatility skew due to its Gaussian short rate distribution, providing a richer structure than the flat smile implied by lognormal forward rates.
