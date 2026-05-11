# Caps and Floors

**Caps** and **floors** are the most liquid interest rate options. A cap protects against rising rates; a floor protects against falling rates. They are portfolios of individual options called **caplets** and **floorlets**.

---

## Definitions

### Interest Rate Cap

A **cap** is a contract that pays the holder when a floating rate exceeds a strike rate $K$.

**Structure:**

- Notional: $N$
- Strike: $K$
- Reset dates: $T_0, T_1, \ldots, T_{n-1}$
- Payment dates: $T_1, T_2, \ldots, T_n$
- Underlying rate: $L(T_i, T_{i+1})$ (e.g., LIBOR or SOFR)

**Caplet payoff** at $T_{i+1}$:

$$
N \cdot \delta_i \cdot \max(L(T_i, T_{i+1}) - K, 0)
$$

where $\delta_i = T_{i+1} - T_i$ is the accrual fraction (day count adjusted).

### Interest Rate Floor

A **floor** pays when the floating rate falls below $K$:

$$
N \cdot \delta_i \cdot \max(K - L(T_i, T_{i+1}), 0)
$$

### Cap = Sum of Caplets

$$
\text{Cap} = \sum_{i=0}^{n-1} \text{Caplet}_i
$$

Each caplet is valued independently and summed.

---

## Cap-Floor Parity

### Relationship

A long cap and short floor with the same strike and dates equals a payer swap:

$$
\text{Cap} - \text{Floor} = \text{Payer Swap}
$$

**Proof:** For each period:

$$
\max(L - K, 0) - \max(K - L, 0) = L - K
$$

This is the floating-minus-fixed payment of a payer swap.

### Implications

- ATM cap and floor have the same value (since ATM swap has zero value)
- Out-of-the-money cap = In-the-money floor (by parity)
- Provides arbitrage relationship for pricing consistency

---

## Black's Model for Caps

### Model Assumption

Under the $T_{i+1}$-forward measure, the forward rate $F_i(t) = F(t; T_i, T_{i+1})$ is a **martingale** with lognormal dynamics:

$$
\frac{dF_i(t)}{F_i(t)} = \sigma_i \, dW_t^{T_{i+1}}
$$

where $\sigma_i$ is the **caplet volatility** for period $i$.

### Black's Caplet Formula

$$
\boxed{\text{Caplet}_i = N \cdot \delta_i \cdot P(0, T_{i+1}) \cdot [F_i N(d_1) - K N(d_2)]}
$$

where:

$$
d_1 = \frac{\ln(F_i/K) + \frac{1}{2}\sigma_i^2 T_i}{\sigma_i \sqrt{T_i}}
$$

$$
d_2 = d_1 - \sigma_i \sqrt{T_i}
$$

and:

- $F_i = F(0; T_i, T_{i+1})$ is the current forward rate
- $P(0, T_{i+1})$ is the discount factor
- $\sigma_i$ is the Black (lognormal) volatility

### Floorlet Formula

$$
\text{Floorlet}_i = N \cdot \delta_i \cdot P(0, T_{i+1}) \cdot [K N(-d_2) - F_i N(-d_1)]
$$

---

## Caplet Pricing in Short-Rate Models

### Caplet as Bond Put

The caplet paying $\delta \max(L(T_1, T_2) - K, 0)$ at $T_2$ can be rewritten.

At time $T_1$, the floating rate is:

$$
L(T_1, T_2) = \frac{1}{\delta} \left(\frac{1}{P(T_1, T_2)} - 1\right)
$$

So:

$$
\delta \max(L - K, 0) = \max\left(1 - (1 + K\delta)P(T_1, T_2), 0\right)
$$

This is $(1 + K\delta)$ times a **put option** on a zero-coupon bond with strike $K_P = 1/(1 + K\delta)$.

### Caplet Formula (Hull-White)

$$
\text{Caplet} = (1 + K\delta) \cdot \left[K_P P(0, T_1) N(-d_2) - P(0, T_2) N(-d_1)\right]
$$

where:

$$
d_1 = \frac{1}{\sigma_P} \ln \frac{P(0, T_2)}{K_P P(0, T_1)} + \frac{\sigma_P}{2}
$$

$$
\sigma_P = \sigma \cdot B(T_2 - T_1) \cdot \sqrt{\frac{1 - e^{-2\kappa T_1}}{2\kappa}}
$$

---

## Flat Volatility vs. Spot Volatility

### Flat (Cap) Volatility

Market quotes a single volatility $\sigma_{\text{flat}}$ for an entire cap. This is the volatility that, when used for all caplets, reproduces the cap price.

### Spot (Caplet) Volatilities

The **spot volatility** $\sigma_i$ is the individual volatility for caplet $i$. The relationship:

$$
\text{Cap Price} = \sum_i \text{Caplet}_i(\sigma_i)
$$

can also be written:

$$
\text{Cap Price} = \sum_i \text{Caplet}_i(\sigma_{\text{flat}})
$$

### Stripping Spot Volatilities

Given flat volatilities for caps of increasing maturity, **bootstrap** spot volatilities:

1. Start with the shortest cap (1 caplet): $\sigma_1 = \sigma_{\text{flat},1}$
2. For cap with $n$ caplets: solve for $\sigma_n$ given $\sigma_1, \ldots, \sigma_{n-1}$

$$
\text{Cap}_n(\sigma_{\text{flat},n}) = \sum_{i=1}^{n-1} \text{Caplet}_i(\sigma_i) + \text{Caplet}_n(\sigma_n)
$$

Solve for $\sigma_n$.

---

## Normal (Bachelier) Model

### Motivation

With negative rates, lognormal models break down. The **Bachelier model** assumes normal (Gaussian) dynamics:

$$
dF_i(t) = \sigma_i^{(n)} \, dW_t
$$

### Bachelier Caplet Formula

$$
\text{Caplet}_i = N \cdot \delta_i \cdot P(0, T_{i+1}) \cdot \left[(F_i - K) N(d) + \sigma_i^{(n)} \sqrt{T_i} \phi(d)\right]
$$

where:

$$
d = \frac{F_i - K}{\sigma_i^{(n)} \sqrt{T_i}}
$$

### Conversion

For ATM options:

$$
\sigma^{(n)} \approx F \cdot \sigma^{(\text{Black})}
$$

This approximate relationship helps convert between conventions.

---

## Calibration to Caps

### Market Data

The market provides:

- Cap prices (or flat implied volatilities) for various strikes and maturities
- Sometimes explicit caplet volatilities

### Calibration Procedure

**For Black's model:**

- Input: flat vol → strip to spot vols → use for pricing

**For short-rate models (e.g., Hull-White):**

1. Fix $\kappa$ (often from other considerations)
2. Fit $\sigma$ (or $\sigma(t)$) to match market cap prices

**Objective:**

$$
\min_{\sigma} \sum_{i} w_i \left(C_i^{\text{model}}(\sigma) - C_i^{\text{market}}\right)^2
$$

### Term Structure of Volatility

The spot volatility term structure $T \mapsto \sigma(T)$ reveals:

- Humped shape: volatility peaks at intermediate maturities
- Downward sloping: short-term rates more volatile
- Upward sloping: long-term uncertainty dominates

---

## Greeks for Caps

### Cap Delta

Sensitivity to forward rate movements:

$$
\Delta_{\text{cap}} = \sum_i \Delta_{\text{caplet},i}
$$

Each caplet delta:

$$
\Delta_{\text{caplet},i} = N \cdot \delta_i \cdot P(0, T_{i+1}) \cdot N(d_1)
$$

### Cap Vega

Sensitivity to volatility:

$$
\mathcal{V}_{\text{cap}} = \sum_i N \cdot \delta_i \cdot P(0, T_{i+1}) \cdot F_i \sqrt{T_i} \phi(d_1)
$$

### Bucket Deltas

Sensitivity to individual forward rates:

$$
\frac{\partial \text{Cap}}{\partial F_j} = \frac{\partial \text{Caplet}_j}{\partial F_j}
$$

Each caplet depends only on its own forward rate.

---

## ATM Caps and the Normal Approximation

### ATM Strike

The **at-the-money** (ATM) strike is typically defined as the forward swap rate:

$$
K_{\text{ATM}} = \frac{P(0, T_0) - P(0, T_n)}{\sum_{i=1}^{n} \delta_i P(0, T_{i})}
$$

### ATM Cap Value (Approximate)

For ATM caps, a useful approximation:

$$
\text{ATM Cap} \approx \sigma \sqrt{T} \cdot \text{Annuity} \cdot \sqrt{\frac{2}{\pi}}
$$

This "rule of 40" helps with quick sanity checks.

---

## Collar = Cap - Floor

### Definition

A **collar** combines:

- Long cap at strike $K_H$ (high)
- Short floor at strike $K_L$ (low)

where $K_L < K_H$.

### Payoff

The floating rate is effectively bounded:

$$
\text{Effective Rate} = \min(\max(L, K_L), K_H)
$$

### Pricing

$$
\text{Collar} = \text{Cap}(K_H) - \text{Floor}(K_L)
$$

Often structured as **zero-cost collars** where premium paid for cap equals premium received for floor.

---

## Practical Considerations

### Market Conventions

| Item | Convention |
|------|------------|
| Day count | ACT/360 (USD), ACT/365 (GBP) |
| Quote | Flat volatility or price |
| Settlement | Spot or forward-starting |
| Premium | Upfront or amortized |

### Liquidity

- ATM caps are most liquid
- Short-dated caps (1-5 year) more liquid than long-dated
- Cap-floor parity should hold tightly

### Hedging

- Delta-hedge with forwards or futures
- Vega-hedge with other caps or swaptions
- Gamma exposure requires dynamic hedging

---

## Key Takeaways

- Cap = portfolio of caplets; Floor = portfolio of floorlets
- Cap - Floor = Payer Swap (cap-floor parity)
- Black's formula: $\text{Caplet} = N\delta P(0,T_{i+1})[F N(d_1) - K N(d_2)]$
- Caplet = Put on bond (in short-rate models)
- Flat vs. spot volatilities: stripping procedure
- Bachelier model handles negative rates
- Calibration: strip vol or fit model to cap prices

---

## Further Reading

- Hull, *Options, Futures, and Other Derivatives*, Chapters 29-30
- Brigo & Mercurio, *Interest Rate Models*, Chapter 1 and 6
- Rebonato, *Interest Rate Option Models*

---

## Exercises

**Exercise 1.** Consider a 2-year cap with semiannual resets ($\delta = 0.5$), notional $N = \$1{,}000{,}000$, and strike $K = 4\%$. The discount factors are $P(0, 0.5) = 0.9901$, $P(0, 1.0) = 0.9803$, $P(0, 1.5) = 0.9706$, $P(0, 2.0) = 0.9610$, and the forward rates are $F_0 = 4.0\%$, $F_1 = 4.0\%$, $F_2 = 4.0\%$, $F_3 = 4.0\%$. Each caplet has Black volatility $\sigma_i = 20\%$. Compute the price of each caplet and the total cap price using Black's formula.

??? success "Solution to Exercise 1"

    **Given:** $N = 1{,}000{,}000$, $\delta = 0.5$, $K = 0.04$, $\sigma_i = 0.20$ for all $i$, $F_i = 0.04$ for all $i$.

    Since $F_i = K$ (ATM), we have $\ln(F_i/K) = 0$, so:

    $$
    d_1 = \frac{0 + \frac{1}{2}\sigma_i^2 T_i}{\sigma_i\sqrt{T_i}} = \frac{1}{2}\sigma_i\sqrt{T_i}
    $$

    $$
    d_2 = d_1 - \sigma_i\sqrt{T_i} = -\frac{1}{2}\sigma_i\sqrt{T_i}
    $$

    The caplet formula is $\text{Caplet}_i = N\delta P(0,T_{i+1})[F_i N(d_1) - K N(d_2)]$.

    Since $F_i = K = 0.04$: $\text{Caplet}_i = N\delta P(0,T_{i+1}) \cdot 0.04 \cdot [N(d_1) - N(d_2)]$.

    **Caplet 1** ($T_0 = 0$, payment at $T_1 = 0.5$):

    $d_1 = \frac{1}{2}(0.20)\sqrt{0} = 0$, $d_2 = 0$. So $N(d_1) - N(d_2) = 0$.

    $\text{Caplet}_0 = 0$. (The first caplet is typically excluded since $L(0, 0.5)$ is already known; if included with $T_0 = 0$, it has zero time value.)

    **Caplet 2** ($T_1 = 0.5$, payment at $T_2 = 1.0$):

    $d_1 = \frac{1}{2}(0.20)\sqrt{0.5} = 0.1 \times 0.7071 = 0.07071$

    $d_2 = -0.07071$

    $N(0.07071) = 0.5282$, $N(-0.07071) = 0.4718$

    $\text{Caplet}_1 = 1{,}000{,}000 \times 0.5 \times 0.9803 \times 0.04 \times (0.5282 - 0.4718) = 1{,}000{,}000 \times 0.5 \times 0.9803 \times 0.04 \times 0.05640 = 1{,}106.3$

    **Caplet 3** ($T_2 = 1.0$, payment at $T_3 = 1.5$):

    $d_1 = \frac{1}{2}(0.20)\sqrt{1.0} = 0.10$, $d_2 = -0.10$

    $N(0.10) = 0.5398$, $N(-0.10) = 0.4602$

    $\text{Caplet}_2 = 1{,}000{,}000 \times 0.5 \times 0.9706 \times 0.04 \times 0.0796 = 1{,}546.5$

    **Caplet 4** ($T_3 = 1.5$, payment at $T_4 = 2.0$):

    $d_1 = \frac{1}{2}(0.20)\sqrt{1.5} = 0.1 \times 1.2247 = 0.12247$, $d_2 = -0.12247$

    $N(0.12247) = 0.5487$, $N(-0.12247) = 0.4513$

    $\text{Caplet}_3 = 1{,}000{,}000 \times 0.5 \times 0.9610 \times 0.04 \times 0.0975 = 1{,}874.8$

    **Total cap price:**

    $$
    \text{Cap} = 0 + 1{,}106.3 + 1{,}546.5 + 1{,}874.8 \approx \$4{,}527.6
    $$

    (Note: if the first caplet at $T_0 = 0$ is excluded by convention, the cap has 3 caplets with the prices computed above.)

---

**Exercise 2.** Prove cap-floor parity: show that for each period, $\max(L - K, 0) - \max(K - L, 0) = L - K$, and deduce that Cap $-$ Floor $=$ Payer Swap. If the ATM swap rate is 5\% and you observe a 5\%-strike cap trading at 320 bps, what must the 5\%-strike floor be worth?

??? success "Solution to Exercise 2"

    **Proof of the identity:** For any real number $L$:

    $$
    \max(L - K, 0) - \max(K - L, 0) = \begin{cases} L - K & \text{if } L \geq K \\ -(K - L) = L - K & \text{if } L < K \end{cases} = L - K
    $$

    This holds for all $L$, confirming the identity.

    **Deduction:** For each period $i$, the caplet pays $\delta\max(L_i - K, 0)$ and the floorlet pays $\delta\max(K - L_i, 0)$ at time $T_{i+1}$. The difference is $\delta(L_i - K)$, which is exactly the floating-minus-fixed payment of a payer swap for that period. Summing over all periods:

    $$
    \text{Cap} - \text{Floor} = \sum_i \text{Caplet}_i - \sum_i \text{Floorlet}_i = \text{Payer Swap}
    $$

    **Application:** If the ATM swap rate is 5% and the strike is $K = 5\%$, then the payer swap with strike 5% is ATM and has **zero value**. Therefore:

    $$
    \text{Cap}(5\%) - \text{Floor}(5\%) = 0
    $$

    $$
    \text{Floor}(5\%) = \text{Cap}(5\%) = 320 \text{ bps}
    $$

    The 5%-strike floor is worth **320 bps** (same as the cap).

---

**Exercise 3.** Derive the relationship between a caplet and a put option on a zero-coupon bond. Starting from the caplet payoff $\delta \max(L(T_1, T_2) - K, 0)$ paid at $T_2$, substitute the expression for $L(T_1, T_2)$ in terms of $P(T_1, T_2)$ and show that:

$$
\delta \max(L - K, 0) = (1 + K\delta)\max\!\left(\frac{1}{1+K\delta} - P(T_1, T_2), 0\right)
$$

??? success "Solution to Exercise 3"

    Starting from the caplet payoff paid at $T_2$:

    $$
    \delta\max(L(T_1, T_2) - K, 0)
    $$

    The forward rate $L(T_1, T_2)$ is defined by:

    $$
    L(T_1, T_2) = \frac{1}{\delta}\left(\frac{1}{P(T_1, T_2)} - 1\right)
    $$

    Substituting:

    $$
    L - K = \frac{1}{\delta}\left(\frac{1}{P(T_1,T_2)} - 1\right) - K = \frac{1}{\delta}\left(\frac{1}{P(T_1,T_2)} - 1 - K\delta\right) = \frac{1}{\delta}\left(\frac{1 - (1+K\delta)P(T_1,T_2)}{P(T_1,T_2)}\right)
    $$

    Therefore:

    $$
    \delta\max(L-K, 0) = \max\!\left(\frac{1 - (1+K\delta)P(T_1,T_2)}{P(T_1,T_2)}, 0\right)
    $$

    Since $P(T_1,T_2) > 0$, the sign is determined by the numerator:

    $$
    = \frac{1}{P(T_1,T_2)}\max\!\left(1 - (1+K\delta)P(T_1,T_2), 0\right)
    $$

    Now factor out $(1+K\delta)$:

    $$
    = \frac{(1+K\delta)}{P(T_1,T_2)}\max\!\left(\frac{1}{1+K\delta} - P(T_1,T_2), 0\right)
    $$

    This is paid at $T_2$. To value at time 0, we discount by $P(0,T_2)$, which includes the $1/P(T_1,T_2)$ factor. Alternatively, the payoff at $T_1$ (discounting back one period from $T_2$ to $T_1$ using the factor $P(T_1,T_2)$) is:

    $$
    P(T_1,T_2) \times \frac{(1+K\delta)}{P(T_1,T_2)}\max\!\left(\frac{1}{1+K\delta} - P(T_1,T_2), 0\right)
    $$

    $$
    = (1+K\delta)\max\!\left(\frac{1}{1+K\delta} - P(T_1,T_2), 0\right)
    $$

    This is exactly $(1+K\delta)$ times a **put option** on the zero-coupon bond $P(T_1,T_2)$ with strike $K_P = 1/(1+K\delta)$ and expiry $T_1$.

---

**Exercise 4.** A market quotes flat cap volatilities as follows: 1Y cap at 18\%, 2Y cap at 20\%, 3Y cap at 19\%. The caps have annual resets. Bootstrap the spot (caplet) volatilities $\sigma_1$, $\sigma_2$, $\sigma_3$ from these flat volatilities. Explain why the 3Y flat vol can be lower than the 2Y flat vol even though all spot vols are positive.

??? success "Solution to Exercise 4"

    **Bootstrapping spot volatilities from flat volatilities:**

    For annual resets, the cap with maturity $n$ years consists of caplets 1 through $n$ (or $n-1$ depending on convention; here we assume caplets for periods ending at years 1, 2, 3).

    **Year 1 (1Y cap = 1 caplet):**

    The 1Y cap consists of a single caplet with volatility $\sigma_1$. The flat vol equals the spot vol:

    $$
    \sigma_1 = 18\%
    $$

    **Year 2 (2Y cap = 2 caplets):**

    The 2Y cap price equals the sum of two caplet prices:

    $$
    \text{Cap}_2(\sigma_{\text{flat}} = 20\%) = \text{Caplet}_1(\sigma_1) + \text{Caplet}_2(\sigma_2)
    $$

    But also:

    $$
    \text{Cap}_2(20\%) = \text{Caplet}_1(20\%) + \text{Caplet}_2(20\%)
    $$

    We know $\sigma_1 = 18\%$, so we solve for $\sigma_2$ from:

    $$
    \text{Caplet}_1(18\%) + \text{Caplet}_2(\sigma_2) = \text{Caplet}_1(20\%) + \text{Caplet}_2(20\%)
    $$

    Since the flat vol of 20% exceeds the first caplet's spot vol of 18%, the second caplet must have $\sigma_2 > 20\%$ to compensate. Using Black's formula (the exact value depends on forward rates and discount factors), the bootstrapped $\sigma_2$ will be approximately **22%** (higher than the flat vol).

    **Year 3 (3Y cap = 3 caplets):**

    $$
    \text{Cap}_3(19\%) = \text{Caplet}_1(18\%) + \text{Caplet}_2(\sigma_2) + \text{Caplet}_3(\sigma_3)
    $$

    Since the 3Y flat vol (19%) is lower than the 2Y flat vol (20%), the marginal caplet 3 must have a relatively low volatility. Solving:

    $$
    \text{Caplet}_3(\sigma_3) = \text{Cap}_3(19\%) - \text{Caplet}_1(18\%) - \text{Caplet}_2(\sigma_2)
    $$

    This yields $\sigma_3$ below 19% (approximately **16--17%**).

    **Why 3Y flat vol can be below 2Y flat vol:** The flat vol is a weighted average of the spot vols, where the weights depend on caplet prices (and hence on forward rates and discount factors). If the third caplet has a low spot vol, it pulls the weighted average down. The spot vol term structure can be humped (rising then falling) even if the flat vol term structure is monotone, because flat vols smooth out the spot vol curve through averaging.

---

**Exercise 5.** Using the Bachelier (normal) model, price an ATM caplet with $F = K = 3\%$, $\delta = 0.25$, $T = 1$, $P(0, T + \delta) = 0.9926$, normal volatility $\sigma^{(n)} = 60$ bps, and $N = \$10{,}000{,}000$. Compare the result with the approximate conversion formula $\sigma^{(n)} \approx F \cdot \sigma^{(\text{Black})}$ and compute the implied Black volatility.

??? success "Solution to Exercise 5"

    **Given (Bachelier model):** $F = K = 0.03$ (ATM), $\delta = 0.25$, $T = 1$, $P(0, T+\delta) = P(0, 1.25) = 0.9926$, $\sigma^{(n)} = 0.0060$ (60 bps), $N = 10{,}000{,}000$.

    Since $F = K$, we have $d = (F - K)/(\sigma^{(n)}\sqrt{T}) = 0$, so $N(0) = 0.5$ and $\phi(0) = 1/\sqrt{2\pi} = 0.3989$.

    **Bachelier caplet formula:**

    $$
    \text{Caplet} = N \cdot \delta \cdot P(0, T+\delta) \cdot \left[(F - K)N(d) + \sigma^{(n)}\sqrt{T}\,\phi(d)\right]
    $$

    $$
    = 10{,}000{,}000 \times 0.25 \times 0.9926 \times \left[0 + 0.0060 \times 1.0 \times 0.3989\right]
    $$

    $$
    = 10{,}000{,}000 \times 0.25 \times 0.9926 \times 0.002393
    $$

    $$
    = 2{,}481{,}500 \times 0.002393 = \$5{,}938
    $$

    **Implied Black volatility via the conversion formula:**

    $$
    \sigma^{(\text{Black})} \approx \frac{\sigma^{(n)}}{F} = \frac{0.0060}{0.03} = 0.20 = 20\%
    $$

    **Verification using Black's formula (ATM):**

    For ATM with $F = K$: $d_1 = \sigma\sqrt{T}/2 = 0.10$, $d_2 = -0.10$.

    $$
    \text{Caplet}_{\text{Black}} = N\delta P(0,T+\delta) \cdot F \cdot [N(0.10) - N(-0.10)]
    $$

    $$
    = 10{,}000{,}000 \times 0.25 \times 0.9926 \times 0.03 \times [0.5398 - 0.4602]
    $$

    $$
    = 74{,}445 \times 0.0796 = \$5{,}926
    $$

    The two results agree to within \$12 (0.2% relative difference), confirming the approximate conversion $\sigma^{(n)} \approx F \cdot \sigma^{(\text{Black})}$ is accurate for ATM options. The small discrepancy arises because the conversion is exact only in the limit of small $\sigma\sqrt{T}$.

---

**Exercise 6.** A trader constructs a zero-cost collar by buying a cap at $K_H = 5\%$ and selling a floor at $K_L$, both on the same 3-year semiannual floating rate exposure. If the cap costs 180 bps (in running premium) and the floor premium per basis point of strike is approximately 40 bps per 1\% of strike, estimate the floor strike $K_L$ that makes the collar zero-cost. Discuss the risks of this structure.

??? success "Solution to Exercise 6"

    **Given:** Cap costs 180 bps running, floor premium is approximately 40 bps per 1% of strike.

    The floor premium at strike $K_L$ is approximately $40 \times K_L$ bps (where $K_L$ is in percent). For a zero-cost collar:

    $$
    \text{Floor premium} = \text{Cap premium}
    $$

    $$
    40 \times K_L = 180
    $$

    $$
    K_L = \frac{180}{40} = 4.5\%
    $$

    So the floor strike is approximately **$K_L = 4.5\%$**.

    The collar structure: the borrower buys a cap at 5% (protection against rates above 5%) and sells a floor at 4.5% (giving up gains when rates fall below 4.5%). The effective borrowing rate is bounded between 4.5% and 5%.

    **Risks of this structure:**

    1. **Opportunity cost:** If rates fall significantly below 4.5%, the borrower does not benefit --- they are locked into paying at least 4.5% due to the short floor. This is the primary risk.
    2. **Basis risk:** The cap and floor reference rates (e.g., SOFR) may not perfectly match the borrower's actual funding rate.
    3. **Credit risk:** The collar counterparty may default, leaving the borrower without the cap protection.
    4. **Liquidity risk:** Unwinding the collar before maturity may be costly, especially the short floor position.
    5. **Model risk:** The linear premium approximation ($40 \times K_L$) is crude --- the actual floor premium depends nonlinearly on the strike, forward rates, and volatility.
    6. **Mark-to-market risk:** Although zero-cost at inception, the collar can have significant positive or negative value subsequently, creating accounting and margin implications.

---

**Exercise 7.** Compute the cap vega for a 3-year annual cap with $K = 4\%$, $N = \$1{,}000{,}000$, and the following parameters for each caplet: $F_i = 4\%$, $P(0, T_{i+1}) = e^{-0.04 \cdot T_{i+1}}$, $\sigma_i = 22\%$. Verify that the cap vega is the sum of the individual caplet vegas. Which caplet contributes the most vega, and why?

??? success "Solution to Exercise 7"

    **Given:** 3-year annual cap, $K = 0.04$, $N = 1{,}000{,}000$, $F_i = 0.04$ (ATM for each caplet), $\sigma_i = 0.22$, $\delta = 1$ (annual), $P(0, T_{i+1}) = e^{-0.04 T_{i+1}}$.

    **Caplet vega formula:**

    $$
    \mathcal{V}_{\text{caplet},i} = N \cdot \delta \cdot P(0, T_{i+1}) \cdot F_i \sqrt{T_i}\,\phi(d_1)
    $$

    Since $F_i = K$ (ATM), $d_1 = \frac{1}{2}\sigma_i\sqrt{T_i}$ and $d_2 = -d_1$.

    **Caplet 1** ($T_1 = 1$, $T_2 = 2$):

    $d_1 = \frac{1}{2}(0.22)(1) = 0.11$, $\phi(0.11) = 0.3965$

    $P(0,2) = e^{-0.08} = 0.9231$

    $\mathcal{V}_1 = 1{,}000{,}000 \times 1 \times 0.9231 \times 0.04 \times 1.0 \times 0.3965 = 14{,}634$

    **Caplet 2** ($T_2 = 2$, $T_3 = 3$):

    $d_1 = \frac{1}{2}(0.22)\sqrt{2} = 0.11 \times 1.4142 = 0.15556$, $\phi(0.15556) = 0.3939$

    $P(0,3) = e^{-0.12} = 0.8869$

    $\mathcal{V}_2 = 1{,}000{,}000 \times 1 \times 0.8869 \times 0.04 \times 1.4142 \times 0.3939 = 19{,}742$

    **Caplet 3** ($T_3 = 3$, $T_4 = 4$):

    $d_1 = \frac{1}{2}(0.22)\sqrt{3} = 0.11 \times 1.7321 = 0.19053$, $\phi(0.19053) = 0.3918$ (approximately, since $\phi$ is nearly flat near 0)

    $P(0,4) = e^{-0.16} = 0.8521$

    $\mathcal{V}_3 = 1{,}000{,}000 \times 1 \times 0.8521 \times 0.04 \times 1.7321 \times 0.3918 = 23{,}126$

    **Total cap vega:**

    $$
    \mathcal{V}_{\text{cap}} = \mathcal{V}_1 + \mathcal{V}_2 + \mathcal{V}_3 = 14{,}634 + 19{,}742 + 23{,}126 = 57{,}502
    $$

    This confirms that the cap vega is the sum of individual caplet vegas, since the cap price is the sum of caplet prices and each caplet depends on its own volatility parameter.

    **Which caplet contributes the most vega?** Caplet 3 (the longest-dated) contributes the most vega. This is because the vega of an ATM option is proportional to $\sqrt{T}$ (via the $F\sqrt{T}\phi(d_1)$ factor). Longer-dated caplets have more time for volatility to affect the outcome, so they are more sensitive to changes in volatility. The discount factor $P(0,T_{i+1})$ partially offsets this (later caplets are discounted more), but the $\sqrt{T}$ effect dominates.
