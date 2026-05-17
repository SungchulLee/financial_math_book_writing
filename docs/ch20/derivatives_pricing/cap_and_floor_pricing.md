# Cap and Floor Pricing

Interest rate caps and floors are among the most actively traded OTC derivatives. Since a cap is a portfolio of individual caplets, and each caplet in the Hull-White model reduces to a put on a zero-coupon bond, the entire cap can be priced analytically. This section derives the cap and floor pricing formulas and compares the Hull-White result with Black's formula.

## Cap and Floor Structure

Recall (see [§ Interest Rate Products](../../ch18/interest_rate_products/coupon_bond_and_frn.md)): a cap (resp. floor) is the sum $\text{Cap}(t_0)=\sum_k \text{Caplet}_k(t_0)$ (resp. $\text{Floor}(t_0)=\sum_k \text{Floorlet}_k(t_0)$) of caplets/floorlets with payoffs at $T_k$ given by $N\tau_k\max(l_k(T_{k-1})-K,0)$ and $N\tau_k\max(K-l_k(T_{k-1}),0)$, where $\tau_k=T_k-T_{k-1}$ and $l_k(T_{k-1})=l(T_{k-1};T_{k-1},T_k)$.

## Hull-White Caplet as a ZCB Put

Recall (see [§ HW Caplet/Floorlet Formula](caplet_floorlet_formula.md)): a caplet equals a scaled ZCB put,

$$
\text{Caplet}_k(t_0) = \hat{N}\,V_p^{\text{ZCB}}\!\left(t_0,\, T_{k-1},\, T_k;\, \hat{K}\right), \qquad \hat{N} = N(1 + \tau_k K),\quad \hat{K} = \frac{1}{1 + \tau_k K},
$$

and a floorlet equals a scaled ZCB call $\text{Floorlet}_k(t_0)=\hat{N}\,V_c^{\text{ZCB}}(t_0,T_{k-1},T_k;\hat{K})$. The ZCB option pricing is the closed-form formula from [§ HW Bond Options](../bond_options/zero_coupon_bond_options.md).

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

Recall (see [§ Black's Caplet Formula](../../ch19/lmm/caplet_pricing_black_formula.md)): caplets are market-quoted via Black's formula with implied volatility $\sigma_k^{\text{Black}}$, which assumes $l_k(t)$ is lognormal under $\mathbb{Q}^{T_k}$. The Hull-White model instead produces a Gaussian short rate distribution. The two approaches give different implied volatility structures:

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

---

## Exercises

**Exercise 1.** For a 3-year annual cap with $N = \$1{,}000{,}000$, $K = 0.05$, compute $\hat{N}_k$ and $\hat{K}_k$ for each of the three caplets. Describe the ZCB put that needs to be priced for each caplet.

??? success "Solution to Exercise 1"
    For a 3-year annual cap with $N = \$1{,}000{,}000$, $K = 0.05$, the payment dates are $T_1 = 1$, $T_2 = 2$, $T_3 = 3$ with reset dates $T_0 = 0$, $T_1 = 1$, $T_2 = 2$. Each accrual fraction is $\tau_k = 1$.

    **Caplet 1** (reset at $T_0 = 0$, pay at $T_1 = 1$):

    $$
    \hat{N}_1 = 1{,}000{,}000 \times (1 + 1 \times 0.05) = 1{,}050{,}000
    $$

    $$
    \hat{K}_1 = \frac{1}{1 + 1 \times 0.05} = \frac{1}{1.05} \approx 0.95238
    $$

    This caplet requires pricing a ZCB put with option maturity $T_0 = 0$, bond maturity $T_1 = 1$, and strike $0.95238$.

    **Caplet 2** (reset at $T_1 = 1$, pay at $T_2 = 2$):

    $$
    \hat{N}_2 = 1{,}050{,}000, \quad \hat{K}_2 = 0.95238
    $$

    ZCB put with option maturity $T_1 = 1$, bond maturity $T_2 = 2$, strike $0.95238$.

    **Caplet 3** (reset at $T_2 = 2$, pay at $T_3 = 3$):

    $$
    \hat{N}_3 = 1{,}050{,}000, \quad \hat{K}_3 = 0.95238
    $$

    ZCB put with option maturity $T_2 = 2$, bond maturity $T_3 = 3$, strike $0.95238$.

    Since $\tau_k$ and $K$ are the same for all three caplets, $\hat{N}_k$ and $\hat{K}_k$ are identical. Each caplet is priced via the Hull-White ZCB put formula with the appropriate option and bond maturities.

---

**Exercise 2.** Derive the floorlet-ZCB call equivalence: show that $\text{Floorlet}_k(t_0) = \hat{N}\,V_c^{\text{ZCB}}(t_0, T_{k-1}, T_k; \hat{K})$ by starting from the floorlet payoff and applying the same algebra as the caplet derivation.

??? success "Solution to Exercise 2"
    The floorlet payoff at $T_k$ is $N\tau_k\max(K - l_k(T_{k-1}), 0)$. Starting from the risk-neutral pricing formula:

    $$
    \text{Floorlet}_k(t_0) = \mathbb{E}^{\mathbb{Q}}\!\left[\frac{M(t_0)}{M(T_k)}\,N\tau_k\max(K - l_k(T_{k-1}), 0)\,\Big|\,\mathcal{F}(t_0)\right]
    $$

    Using the tower property to condition on $\mathcal{F}(T_{k-1})$ and the relation $\mathbb{E}^{\mathbb{Q}}\!\left[\frac{1}{M(T_k)}\Big|\mathcal{F}(T_{k-1})\right] = \frac{P(T_{k-1},T_k)}{M(T_{k-1})}$:

    $$
    = \mathbb{E}^{\mathbb{Q}}\!\left[\frac{M(t_0)}{M(T_{k-1})}\,N\tau_k\max(K - l_k(T_{k-1}), 0)\,P(T_{k-1},T_k)\,\Big|\,\mathcal{F}(t_0)\right]
    $$

    Substituting $l_k(T_{k-1}) = \frac{1}{\tau_k}\!\left(\frac{1}{P(T_{k-1},T_k)} - 1\right)$:

    $$
    N\tau_k\max\!\left(K - \frac{1}{\tau_k}\!\left(\frac{1}{P(T_{k-1},T_k)} - 1\right), 0\right)P(T_{k-1},T_k) = N\max\!\left((1+\tau_k K)P(T_{k-1},T_k) - 1, 0\right)
    $$

    Factoring:

    $$
    = N(1+\tau_k K)\max\!\left(P(T_{k-1},T_k) - \frac{1}{1+\tau_k K}, 0\right) = \hat{N}\max(P(T_{k-1},T_k) - \hat{K}, 0)
    $$

    Therefore:

    $$
    \text{Floorlet}_k(t_0) = \hat{N}\,\mathbb{E}^{\mathbb{Q}}\!\left[\frac{M(t_0)}{M(T_{k-1})}\max(P(T_{k-1},T_k) - \hat{K}, 0)\,\Big|\,\mathcal{F}(t_0)\right] = \hat{N}\,V_c^{\text{ZCB}}(t_0, T_{k-1}, T_k; \hat{K})
    $$

    which is $\hat{N}$ times a European call on the ZCB.

---

**Exercise 3.** Verify the cap-floor parity $\text{Cap} - \text{Floor} = \text{IRS}^{\text{Payer}}$ by summing the individual caplet-floorlet parities. Explain why this relationship is model-independent (holds for any arbitrage-free model).

??? success "Solution to Exercise 3"
    **Verification:** For each $k$, the caplet-floorlet parity is:

    $$
    \text{Caplet}_k - \text{Floorlet}_k = N\tau_k\,P(t_0, T_k)(l_k(t_0) - K)
    $$

    This follows from $\max(x,0) - \max(-x,0) = x$ applied to $x = l_k(T_{k-1}) - K$, plus the forward measure pricing. Summing over $k = 1, \ldots, n$:

    $$
    \text{Cap} - \text{Floor} = N\sum_{k=1}^n \tau_k\,P(t_0, T_k)(l_k(t_0) - K)
    $$

    Using $\tau_k l_k(t_0) = \frac{P(t_0,T_{k-1})}{P(t_0,T_k)} - 1$, so $\tau_k P(t_0,T_k) l_k(t_0) = P(t_0,T_{k-1}) - P(t_0,T_k)$:

    $$
    = N\sum_{k=1}^n\!\left(P(t_0,T_{k-1}) - P(t_0,T_k)\right) - NK\sum_{k=1}^n \tau_k P(t_0,T_k)
    $$

    The first sum telescopes: $\sum_{k=1}^n (P(t_0,T_{k-1}) - P(t_0,T_k)) = P(t_0,T_0) - P(t_0,T_n)$.

    $$
    \text{Cap} - \text{Floor} = N(P(t_0,T_0) - P(t_0,T_n)) - NK\sum_{k=1}^n \tau_k P(t_0,T_k) = \text{IRS}^{\text{Payer}}(t_0)
    $$

    **Model independence:** The identity $\max(x,0) - \max(-x,0) = x$ holds pathwise for every realization. Therefore the parity involves only the unconditional forward value of $l_k(T_{k-1}) - K$, which equals $l_k(t_0) - K$ under any arbitrage-free model (by the martingale property of $l_k$ under $\mathbb{Q}^{T_k}$). No distributional assumptions are needed.

---

**Exercise 4.** The Hull-White model implies a decreasing term structure of cap volatilities. Explain why: as the caplet maturity increases, what happens to the effective volatility of the underlying forward rate in the Hull-White model?

??? success "Solution to Exercise 4"
    In the Hull-White model, the conditional variance of $r(T_{k-1})$ given $r(t_0)$ is:

    $$
    v_r^2(t_0, T_{k-1}) = \frac{\sigma^2}{2\lambda}(1 - e^{-2\lambda(T_{k-1} - t_0)})
    $$

    The effective volatility of the bond price $P(T_{k-1}, T_k) = e^{A(\tau_k) + B(\tau_k)r(T_{k-1})}$ depends on $|B(\tau_k)|\,v_r(t_0, T_{k-1})$. While $v_r$ increases with $T_{k-1}$, the mean reversion causes it to saturate at $\sqrt{\sigma^2/(2\lambda)}$ for large maturities.

    The key effect is that the forward LIBOR volatility is proportional to $|B(\tau_k)|\,v_r / l_k(t_0)$ in relative terms. As maturity increases:

    1. The variance $v_r^2$ grows but saturates due to mean reversion.
    2. The forward rate $l_k(t_0)$ remains at a similar level (determined by the yield curve).

    The result is that the Black implied volatility, which measures relative (percentage) volatility of the forward rate, decreases with maturity. For short maturities, $v_r^2 \approx \sigma^2(T_{k-1} - t_0)$ grows linearly, but for long maturities the saturation effect dominates. This produces the empirically observed decreasing term structure of cap volatilities.

---

**Exercise 5.** Explain the difference between flat (running) volatility and spot volatility for cap pricing. Given a flat cap volatility of 20% for a 5-year cap, describe how you would strip the individual spot volatilities $\sigma_k^{\text{spot}}$ for each caplet.

??? success "Solution to Exercise 5"
    **Flat (running) volatility** $\sigma^{\text{flat}}$ is a single number applied to all caplets in a cap simultaneously. The flat vol is defined implicitly by:

    $$
    \text{Cap}^{\text{market}}(t_0) = \sum_{k=1}^n \text{Caplet}_k^{\text{Black}}(\sigma^{\text{flat}})
    $$

    This is a convenient quoting convention but does not reflect the different volatilities of individual forward rates.

    **Spot volatility** $\sigma_k^{\text{spot}}$ is specific to each caplet $k$, so that $\text{Caplet}_k^{\text{market}} = \text{Caplet}_k^{\text{Black}}(\sigma_k^{\text{spot}})$.

    **Stripping procedure for spot volatilities from a flat vol of 20% for a 5-year cap:**

    1. The 1-year cap consists of a single caplet. Its flat vol equals its spot vol: $\sigma_1^{\text{spot}} = \sigma^{\text{flat}}_{1Y}$.
    2. For the 2-year cap, $\text{Cap}_{2Y} = \text{Caplet}_1(\sigma_1^{\text{spot}}) + \text{Caplet}_2(\sigma_2^{\text{spot}})$. Since $\sigma_1^{\text{spot}}$ is known, solve for $\sigma_2^{\text{spot}}$.
    3. Continue bootstrapping: at each step $k$, the first $k-1$ spot vols are known. Solve for $\sigma_k^{\text{spot}}$ from the $k$-year cap price.

    In practice, with only the 5-year flat vol of 20%, one needs additional market data (caps at intermediate maturities) to uniquely strip all five spot volatilities. With a single flat vol, an assumption about the term structure shape (e.g., flat or interpolated from other cap quotes) is required.

---

**Exercise 6.** Using the Python code provided, modify the `price_cap` function to also return the individual caplet prices. For Hull-White parameters $\lambda = 0.05$ and $\sigma = 0.01$ with $K = 0.04$, which caplet contributes the most to the total cap value?

??? success "Solution to Exercise 6"
    Modify the function to return both total price and individual prices:

    ```python
    def price_cap_detailed(hw, N, K, T_reset_dates, T_payment_dates):
        """Price an interest rate cap, returning total and individual caplet prices."""
        caplet_prices = []
        for T_reset, T_pay in zip(T_reset_dates, T_payment_dates):
            tau_k = T_pay - T_reset
            N_hat = N * (1 + tau_k * K)
            K_hat = 1.0 / (1 + tau_k * K)
            zbp = hw.compute_ZCB_Option_Price(
                K_hat, T_reset, T_pay, CP=OptionType.PUT
            )
            caplet_prices.append(N_hat * zbp)
        return sum(caplet_prices), caplet_prices
    ```

    For Hull-White parameters $\lambda = 0.05$, $\sigma = 0.01$, $K = 0.04$:

    - **Short-dated caplets** (e.g., $k = 1$) have small variance $v_r^2$ because $T_{k-1} - t_0$ is small, leading to small ZCB put prices.
    - **Intermediate caplets** (e.g., $k = 3$ or $k = 4$) have the largest prices because $v_r^2$ has grown substantially but the ZCB option is still well within the range where the Gaussian distribution produces significant probability mass beyond the strike.
    - **Long-dated caplets** see diminishing marginal increases in $v_r^2$ due to mean reversion saturation.

    Typically, for moderate mean reversion ($\lambda = 0.05$), the caplet contributing the most is an intermediate-maturity one (around year 3-4 for a 5-year cap), because the variance has grown enough to make the option valuable, but saturation has not yet fully kicked in.

---

**Exercise 7.** Compare the cap prices produced by the Hull-White model versus Black's formula for at-the-money and deep out-of-the-money strikes. At which strikes do the two models diverge most, and why?

??? success "Solution to Exercise 7"
    **At-the-money (ATM) strikes:** When $K \approx l_k(t_0)$ (the current forward rate), both models produce very similar prices. At ATM, option prices are dominated by at-the-money volatility, and the differences between the lognormal (Black) and Gaussian-exponential (Hull-White) distributions are minimized. The two distributions agree well near their central values.

    **Deep out-of-the-money (OTM) strikes:** For $K \gg l_k(t_0)$, the caplet price depends on the upper tail of the forward rate distribution. The lognormal distribution (Black) has a heavier right tail than the distribution implied by the Hull-White model. Conversely, for $K \ll l_k(t_0)$ (deep in-the-money caplets or equivalently deep OTM floorlets), the lower tails differ.

    The two models diverge most at strikes far from ATM because:

    1. **Tail behavior differs:** The lognormal distribution has a right-skewed, heavy-tailed shape, while the Hull-White distribution of $l_k$ (being a function of a Gaussian variable) has different tail characteristics.
    2. **Symmetry vs asymmetry:** The Gaussian $r$ produces a distribution of $1/P$ that is right-skewed but in a different way from the lognormal. For low strikes, the Hull-White model may assign more probability (since $r$ can go negative, making $P > 1$ and $l_k < 0$ possible), while Black's formula confines $l_k > 0$.

    In practice, the largest price differences appear at deep OTM strikes where the tail probabilities are most sensitive to the distributional assumption.
