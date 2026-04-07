# Cost of Carry

**Key idea**: The forward price reflects the net cost of holding the asset until maturity, not expectations of where the price will be.

The previous sections established that the no-arbitrage forward price of a non-dividend-paying asset is $F_0 = S_0 e^{rT}$. In practice, assets generate income, require storage, or offer convenience to their holders. The **cost-of-carry model** captures all of these factors in a single exponential adjustment. The general formula is

$$
F_0 = S_0 \, e^{(r - q + u - y)T}
$$

where $r$ is the risk-free rate, $q$ is the continuous dividend yield, $u$ is the continuous storage cost rate, and $y$ is the continuous convenience yield. Each term has a clear economic interpretation: carrying the asset costs $r + u$ (financing plus storage) and earns $q + y$ (income plus convenience). The net cost of carry is $c = r - q + u - y$, so the forward price reflects $F_0 = S_0 \, e^{cT}$.

---

## Equity Index Futures

For an equity index paying a continuous dividend yield $q$, there are no storage costs and no convenience yield. The cost-of-carry formula reduces to

$$
F_0 = S_0 \, e^{(r - q)T}
$$

**Example.** Suppose the S&P 500 index stands at $S_0 = 4{,}500$, the risk-free rate is $r = 5\%$, the continuous dividend yield is $q = 1.8\%$, and the contract matures in $T = 0.5$ years. Then

$$
F_0 = 4{,}500 \, e^{(0.05 - 0.018) \times 0.5} = 4{,}500 \, e^{0.016} \approx 4{,}572.58
$$

The forward price exceeds the spot price because the financing cost ($r = 5\%$) exceeds the dividend yield ($q = 1.8\%$).

---

## Discrete Dividends

When an individual stock pays known discrete dividends during the life of the contract, the forward price is computed by subtracting the present value of those dividends from the spot price before applying the risk-free growth:

$$
F_0 = \bigl(S_0 - \mathrm{PV}(D)\bigr) \, e^{rT}
$$

Here $\mathrm{PV}(D) = \sum_{i} D_i \, e^{-r t_i}$ is the present value of all dividends $D_i$ paid at times $t_i$ before maturity.

**Example.** A stock trades at $S_0 = \$80$. It will pay a dividend of \$1.50 in 2 months and \$1.50 in 5 months. The risk-free rate is $r = 4\%$ and the forward matures in $T = 6$ months. The present value of dividends is

$$
\mathrm{PV}(D) = 1.50 \, e^{-0.04 \times 2/12} + 1.50 \, e^{-0.04 \times 5/12} \approx 1.4900 + 1.4752 = 2.9652
$$

so the forward price is

$$
F_0 = (80 - 2.9652)\, e^{0.04 \times 0.5} \approx 77.0348 \times 1.02020 \approx \$78.59
$$

---

## Commodities: Storage Costs and Convenience Yield

Physical commodities introduce two additional factors.

**Storage costs** ($u$). Holding physical gold, grain, or natural gas requires warehousing, insurance, and handling. These costs are borne by the holder and increase the cost of carry. For a commodity with continuous storage cost rate $u$ and no income:

$$
F_0 = S_0 \, e^{(r + u)T}
$$

**Example (gold).** Spot gold is $S_0 = \$2{,}000$/oz, $r = 5\%$, $u = 0.5\%$, $T = 1$ year:

$$
F_0 = 2{,}000 \, e^{(0.05 + 0.005) \times 1} = 2{,}000 \, e^{0.055} \approx \$2{,}113.14
$$

**Convenience yield** ($y$). Some commodities — especially those with tight supply, like crude oil during a shortage — provide a non-monetary benefit to the holder: the ability to keep production running or meet unexpected demand. This **convenience yield** acts as implicit income, reducing the cost of carry:

$$
F_0 = S_0 \, e^{(r + u - y)T}
$$

When the convenience yield is large enough that $y > r + u$, the forward price falls below the spot price.

**Example (oil).** Spot crude oil is $S_0 = \$85$/barrel, $r = 5\%$, $u = 2\%$, $y = 10\%$, $T = 1$ year:

$$
F_0 = 85 \, e^{(0.05 + 0.02 - 0.10) \times 1} = 85 \, e^{-0.03} \approx \$82.49
$$

The forward price is below the spot price because the convenience yield dominates the financing and storage costs.

---

## Contango and Backwardation

The relationship between the forward price and the spot price defines the shape of the **forward curve**:

- **Contango** ($F_0 > S_0$): the net cost of carry is positive. This is the normal situation for financial assets and storable commodities with ample supply. Forward curves slope upward.
- **Backwardation** ($F_0 < S_0$): the net cost of carry is negative, typically because the convenience yield is high. Supply shortages or strong immediate demand push the spot price above the forward price. Forward curves slope downward.

Contango and backwardation are not permanent conditions — they shift as supply, demand, and interest rates change.

---

## Summary of Cost-of-Carry Cases

| Underlying | Formula | Key parameters |
|---|---|---|
| Non-dividend asset | $F_0 = S_0 \, e^{rT}$ | $r$ only |
| Equity index (continuous yield) | $F_0 = S_0 \, e^{(r-q)T}$ | $r, \, q$ |
| Stock (discrete dividends) | $F_0 = (S_0 - \mathrm{PV}(D))\, e^{rT}$ | $r, \, D_i, \, t_i$ |
| Commodity (storage, no convenience) | $F_0 = S_0 \, e^{(r+u)T}$ | $r, \, u$ |
| Commodity (storage + convenience) | $F_0 = S_0 \, e^{(r+u-y)T}$ | $r, \, u, \, y$ |
| General cost of carry | $F_0 = S_0 \, e^{(r - q + u - y)T}$ | $r, \, q, \, u, \, y$ |

---

## Exercises

**Exercise 1.** An equity index is at $S_0 = 3{,}200$. The risk-free rate is $r = 4\%$ and the continuous dividend yield is $q = 2.5\%$. Compute the 9-month forward price.

??? success "Solution to Exercise 1"
    Using $F_0 = S_0 \, e^{(r - q)T}$ with $T = 0.75$:

    $$
    F_0 = 3{,}200 \, e^{(0.04 - 0.025) \times 0.75} = 3{,}200 \, e^{0.01125} \approx 3{,}236.20
    $$

---

**Exercise 2.** A stock trades at $S_0 = \$120$. It will pay dividends of \$2 in 3 months and \$2 in 9 months. The risk-free rate is $r = 6\%$ and the forward matures in $T = 1$ year. Compute the forward price.

??? success "Solution to Exercise 2"
    First compute the present value of dividends:

    $$
    \mathrm{PV}(D) = 2 \, e^{-0.06 \times 0.25} + 2 \, e^{-0.06 \times 0.75} = 2(0.98511) + 2(0.95600) \approx 1.97022 + 1.91200 = 3.88222
    $$

    Then

    $$
    F_0 = (120 - 3.88222)\, e^{0.06 \times 1} = 116.11778 \times 1.06184 \approx \$123.30
    $$

---

**Exercise 3.** Spot silver is $S_0 = \$25$/oz. The risk-free rate is $r = 5\%$, the continuous storage cost is $u = 1\%$, and there is no convenience yield. Compute the 6-month forward price. Now suppose a supply disruption introduces a convenience yield of $y = 8\%$. Recompute the forward price and state whether the market is in contango or backwardation.

??? success "Solution to Exercise 3"
    Without convenience yield ($y = 0$):

    $$
    F_0 = 25 \, e^{(0.05 + 0.01) \times 0.5} = 25 \, e^{0.03} \approx \$25.76
    $$

    This is contango since $F_0 > S_0$.

    With convenience yield $y = 8\%$:

    $$
    F_0 = 25 \, e^{(0.05 + 0.01 - 0.08) \times 0.5} = 25 \, e^{-0.01} \approx \$24.75
    $$

    Now $F_0 < S_0$, so the market is in **backwardation**. The convenience yield exceeds the financing and storage costs, pulling the forward price below the spot price.

---

**Exercise 4.** A commodity has spot price $S_0$, risk-free rate $r$, storage cost $u$, and convenience yield $y$. Show that the forward price satisfies $F_0 < S_0$ if and only if $y > r + u$. Explain why very high convenience yields correspond to supply shortages.

??? success "Solution to Exercise 4"
    From the cost-of-carry formula with no dividend yield:

    $$
    F_0 = S_0 \, e^{(r + u - y)T}
    $$

    Since $S_0 > 0$ and $T > 0$, we have $F_0 < S_0$ if and only if $e^{(r + u - y)T} < 1$, which holds if and only if $r + u - y < 0$, i.e., $y > r + u$. $\square$

    When supply is scarce, holders of the physical commodity gain a large implicit benefit: they can continue production, fulfill contractual obligations, or sell into a tight spot market at elevated prices. This benefit is the convenience yield. As the shortage intensifies, the convenience yield rises, eventually surpassing $r + u$ and pushing the forward price below the spot price (backwardation). In this regime, the market prices immediate delivery at a premium over future delivery, reflecting the urgency of current demand.
