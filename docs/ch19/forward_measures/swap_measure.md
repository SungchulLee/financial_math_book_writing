# Swap Measure

The $T$-forward measure simplifies the pricing of derivatives with a single payment date. Many interest rate products, however, involve streams of cashflows over multiple dates --- most notably, interest rate swaps and swaptions. The **swap measure** (also called the **annuity measure**) uses the present value of the annuity stream as numéraire, rendering the forward swap rate a martingale and producing the standard Black formula for swaptions.

---

## Motivation

### From Single to Multiple Payment Dates

Under the $T$-forward measure, the zero-coupon bond $P(t,T)$ is the numéraire. This is natural for payoffs at a single date $T$. For a swaption, however, the payoff at exercise is

$$
\text{Payoff} = \sum_{j=1}^{n} \delta_j P(T_0, T_j)\bigl(S(T_0) - K\bigr)^+ = A(T_0)\bigl(S(T_0) - K\bigr)^+
$$

where $A(T_0) = \sum_{j=1}^{n} \delta_j P(T_0, T_j)$ is the annuity factor. The annuity $A(T_0)$ multiplies the swap rate payoff, suggesting that $A(t)$ is the natural numéraire.

### The Key Insight

If we choose $A(t)$ as the numéraire, the forward swap rate $S(t)$ becomes a martingale. Under lognormal dynamics, this leads directly to Black's formula for swaptions, exactly paralleling how the $T$-forward measure produces Black's caplet formula.

---

## Definition of the Annuity Factor

### Swap Structure

Fix a tenor structure with payment dates $T_1, T_2, \ldots, T_n$ and accrual fractions $\delta_j = T_j - T_{j-1}$. The swap start date is $T_0$.

### Annuity Factor

The **annuity factor** (or **present value of a basis point**, **PVBP**) is

$$
A(t) = \sum_{j=1}^{n} \delta_j \, P(t, T_j)
$$

This represents the time-$t$ value of receiving one unit of currency at each payment date, weighted by the accrual fractions.

### Properties of the Annuity Factor

The annuity factor $A(t)$ is:

- **Strictly positive** for $t < T_1$ (sum of positive bond prices)
- **Tradable** --- it is the price of a portfolio of zero-coupon bonds
- **Self-financing** --- the portfolio is static (fixed bond positions), so no rebalancing is required

These properties qualify $A(t)$ as a valid numéraire.

---

## The Forward Swap Rate

### Definition

The **forward swap rate** at time $t$ for a swap over $[T_0, T_n]$ is the fixed rate $S(t)$ that makes the swap have zero value:

$$
S(t) = \frac{P(t, T_0) - P(t, T_n)}{A(t)} = \frac{P(t, T_0) - P(t, T_n)}{\sum_{j=1}^{n} \delta_j \, P(t, T_j)}
$$

### Derivation

The value of the floating leg at time $t$ is $P(t, T_0) - P(t, T_n)$ (this follows from the telescoping property of forward rates). The value of the fixed leg paying rate $K$ is $K \cdot A(t)$. Setting the two equal and solving for $K$ gives $S(t)$.

### Relationship to Forward LIBOR Rates

The forward swap rate can be expressed as a weighted average of forward LIBOR rates:

$$
S(t) = \sum_{i=0}^{n-1} w_i(t) \, L_i(t)
$$

where the weights are

$$
w_i(t) = \frac{\delta_i \, P(t, T_{i+1})}{A(t)}
$$

and $L_i(t)$ is the forward LIBOR rate for period $[T_i, T_{i+1}]$. The weights sum to one: $\sum_{i=0}^{n-1} w_i(t) = 1$.

---

## The Swap Measure

### Definition

The **swap measure** $\mathbb{Q}^A$ is the probability measure associated with the numéraire $A(t)$. Under $\mathbb{Q}^A$, for any tradable asset $V_t$,

$$
\frac{V_t}{A(t)} \quad \text{is a } \mathbb{Q}^A\text{-martingale}
$$

### Radon--Nikodym Derivative

The change of measure from the risk-neutral measure $\mathbb{Q}$ to the swap measure $\mathbb{Q}^A$ is given by

$$
\frac{d\mathbb{Q}^A}{d\mathbb{Q}}\bigg|_{\mathcal{F}_t} = \frac{A(t) / A(0)}{B_t}
$$

where $B_t = \exp\left(\int_0^t r_s \, ds\right)$ is the money-market account.

### Swap Rate Is a Martingale

**Proposition.** Under $\mathbb{Q}^A$, the forward swap rate $S(t)$ is a martingale.

*Proof.* The numerator $P(t, T_0) - P(t, T_n)$ is the value of a tradable portfolio (long the $T_0$-bond, short the $T_n$-bond). Under $\mathbb{Q}^A$, any tradable asset divided by $A(t)$ is a martingale. Therefore

$$
\frac{P(t, T_0) - P(t, T_n)}{A(t)} = S(t)
$$

is a $\mathbb{Q}^A$-martingale. $\square$

---

## Swaption Pricing Under the Swap Measure

### Payer Swaption

A **payer swaption** with exercise date $T_0$ and strike $K$ gives the right to enter a payer swap. Its payoff at $T_0$ is

$$
V_{T_0} = A(T_0) \max(S(T_0) - K, 0)
$$

### Pricing Formula

Under the risk-neutral measure:

$$
V_0 = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_0^{T_0} r_s \, ds} \, A(T_0) \max(S(T_0) - K, 0)\right]
$$

Switching to the swap measure with numéraire $A(t)$:

$$
V_0 = A(0) \, \mathbb{E}^{\mathbb{Q}^A}\!\left[\max(S(T_0) - K, 0)\right]
$$

The stochastic discount factor and the annuity factor have been absorbed into the numéraire.

### Lognormal Swap Rate Dynamics

Assuming the swap rate follows a geometric Brownian motion under $\mathbb{Q}^A$:

$$
\frac{dS(t)}{S(t)} = \sigma_S(t) \, dW_t^A
$$

where $\sigma_S(t)$ is the instantaneous volatility and $W_t^A$ is a Brownian motion under $\mathbb{Q}^A$. Since $S(t)$ is a martingale, the drift is zero.

### Black's Swaption Formula

The terminal swap rate $S(T_0)$ is lognormally distributed:

$$
\ln S(T_0) \sim N\!\left(\ln S(0) - \tfrac{1}{2}v_S^2, \; v_S^2\right)
$$

where $v_S^2 = \int_0^{T_0} \sigma_S(t)^2 \, dt$. Black's formula gives

$$
\boxed{V_0^{\text{payer}} = A(0)\bigl[S(0) \, N(d_1) - K \, N(d_2)\bigr]}
$$

$$
d_1 = \frac{\ln(S(0)/K) + \tfrac{1}{2} v_S^2}{v_S}, \qquad d_2 = d_1 - v_S
$$

### Receiver Swaption

By put--call parity for swaptions:

$$
\boxed{V_0^{\text{receiver}} = A(0)\bigl[K \, N(-d_2) - S(0) \, N(-d_1)\bigr]}
$$

---

## Girsanov Transformation Details

### From Risk-Neutral to Swap Measure

Under $\mathbb{Q}$, the dynamics of $A(t)$ involve the bond price volatilities. Since

$$
A(t) = \sum_{j=1}^{n} \delta_j P(t, T_j)
$$

the volatility of $A(t)$ is a weighted combination:

$$
\frac{dA(t)}{A(t)} = r_t \, dt + \sigma_A(t) \, dW_t^{\mathbb{Q}}
$$

where

$$
\sigma_A(t) = -\frac{\sum_{j=1}^{n} \delta_j P(t, T_j) \, \Sigma(t, T_j)}{A(t)}
$$

and $\Sigma(t, T_j) = \int_t^{T_j} \sigma(t, u) \, du$ is the bond volatility.

The Girsanov change of measure from $\mathbb{Q}$ to $\mathbb{Q}^A$ is

$$
dW_t^A = dW_t^{\mathbb{Q}} - \sigma_A(t) \, dt
$$

### From T-Forward to Swap Measure

The measure change from $\mathbb{Q}^{T_j}$ to $\mathbb{Q}^A$ involves the ratio $A(t) / P(t, T_j)$:

$$
dW_t^A = dW_t^{T_j} - \bigl[\sigma_A(t) - \Sigma(t, T_j)\bigr] dt
$$

---

## Swap Rate Volatility in the LMM

Recall (see [§ LMM](../lmm/libor_market_model.md)): in the LIBOR Market Model the swap rate $S(t) = \sum_i w_i(t) L_i(t)$ is not exactly lognormal, and **Rebonato's frozen-weight approximation** expresses the Black swaption implied variance as a quadratic form in $(w_i(0) L_i(0)/S(0))$ with kernel $\rho_{ij}\int_0^{T_0}\sigma_i\sigma_j\,dt$. Diagonal terms capture individual forward-rate contributions; off-diagonal terms reflect correlation diversification.

---

## Practical Applications

### ATM Swaption Pricing

At-the-money swaptions have $K = S(0)$, so $d_1 = v_S/2$ and $d_2 = -v_S/2$:

$$
V_0^{\text{ATM}} = A(0) \cdot S(0) \bigl[N(v_S/2) - N(-v_S/2)\bigr] = A(0) \cdot S(0) \bigl[2N(v_S/2) - 1\bigr]
$$

For small volatilities, $V_0^{\text{ATM}} \approx A(0) \cdot S(0) \cdot v_S / \sqrt{2\pi}$.

### Swaption Straddle

A swaption straddle (long payer + long receiver at the same strike) is valued as

$$
V_0^{\text{straddle}} = V_0^{\text{payer}} + V_0^{\text{receiver}}
$$

ATM straddles are pure volatility bets:

$$
V_0^{\text{ATM straddle}} = 2 \, V_0^{\text{ATM payer}} \approx 2 \, A(0) \cdot S(0) \cdot \frac{v_S}{\sqrt{2\pi}}
$$

### Market Conventions

Swaption markets quote in terms of **Black implied volatility** $\sigma_S^{\text{Black}}$ or **normal (Bachelier) implied volatility** $\sigma_S^{(n)}$. The swaption vol cube is organized by:

- **Expiry** ($T_0$): e.g., 1M, 3M, 6M, 1Y, 2Y, 5Y, 10Y
- **Tenor** ($T_n - T_0$): e.g., 1Y, 2Y, 5Y, 10Y, 30Y
- **Strike** offset from ATM: e.g., -200bp, -100bp, ATM, +100bp, +200bp

---

## Key Takeaways

- The **annuity factor** $A(t) = \sum \delta_j P(t, T_j)$ serves as the natural numéraire for swap-related products
- The **swap measure** $\mathbb{Q}^A$ is the probability measure under which the forward swap rate $S(t)$ is a martingale
- Swaption pricing reduces to a Black-type formula: $V_0 = A(0)[S(0)N(d_1) - KN(d_2)]$
- The Radon--Nikodym derivative involves the ratio of the annuity to the money-market account
- In the LMM, the swap rate volatility is approximated via Rebonato's formula, linking forward rate volatilities and correlations to swaption prices
- The swap measure framework extends naturally to receiver swaptions via put--call parity

---

## Further Reading

- Brigo & Mercurio (2006), *Interest Rate Models: Theory and Practice*, Chapter 6 (Swaptions)
- Rebonato (2002), *Modern Pricing of Interest-Rate Derivatives*, Chapter 8
- Jamshidian (1997), "LIBOR and Swap Market Models and Measures"
- Andersen & Piterbarg (2010), *Interest Rate Modeling*, Volume II, Chapter 12

---

## Exercises

**Exercise 1.** Consider a swap with semiannual payments over 3 years ($T_0 = 0$, payment dates $T_1 = 0.5, T_2 = 1.0, \ldots, T_6 = 3.0$). The zero-coupon bond prices are $P(0, 0.5) = 0.985$, $P(0, 1.0) = 0.968$, $P(0, 1.5) = 0.950$, $P(0, 2.0) = 0.930$, $P(0, 2.5) = 0.910$, $P(0, 3.0) = 0.889$. Compute the annuity factor $A(0)$ and the forward swap rate $S(0)$.

??? success "Solution to Exercise 1"

    **Annuity factor.** With semiannual payments ($\delta_j = 0.5$ for all $j$) and 6 payment dates:

    $$
    A(0) = \sum_{j=1}^{6} \delta_j P(0, T_j) = 0.5 \times (0.985 + 0.968 + 0.950 + 0.930 + 0.910 + 0.889)
    $$

    $$
    A(0) = 0.5 \times 5.632 = 2.816
    $$

    **Forward swap rate.** With $T_0 = 0$, we have $P(0, T_0) = P(0, 0) = 1$ and $P(0, T_n) = P(0, 3.0) = 0.889$:

    $$
    S(0) = \frac{P(0, T_0) - P(0, T_n)}{A(0)} = \frac{1 - 0.889}{2.816} = \frac{0.111}{2.816} = 0.03942
    $$

    The forward swap rate is approximately **3.94%**.

---

**Exercise 2.** Using the data from Exercise 1, price a 3-year ATM payer swaption (exercise at $T_0 = 0$, but assume the swaption expires in 1 year with $T_0 = 1$, payment dates $T_1 = 1.5, \ldots, T_4 = 3.0$) with Black implied volatility $\sigma_S = 25\%$. Recompute $A(0)$ and $S(0)$ for this sub-swap and apply Black's swaption formula.

??? success "Solution to Exercise 2"

    **Recompute for the sub-swap.** The swaption expires at $T_0 = 1$ year, and the underlying swap has payment dates $T_1 = 1.5, T_2 = 2.0, T_3 = 2.5, T_4 = 3.0$ with $\delta_j = 0.5$.

    **Annuity factor for the sub-swap:**

    $$
    A(0) = 0.5 \times (P(0, 1.5) + P(0, 2.0) + P(0, 2.5) + P(0, 3.0))
    $$

    $$
    = 0.5 \times (0.950 + 0.930 + 0.910 + 0.889) = 0.5 \times 3.679 = 1.8395
    $$

    **Forward swap rate for the sub-swap:**

    $$
    S(0) = \frac{P(0, T_0) - P(0, T_4)}{A(0)} = \frac{P(0, 1.0) - P(0, 3.0)}{1.8395} = \frac{0.968 - 0.889}{1.8395} = \frac{0.079}{1.8395} = 0.04294
    $$

    So $S(0) \approx 4.294\%$.

    **ATM swaption: $K = S(0) = 0.04294$.** The integrated volatility is

    $$
    v_S = \sigma_S \sqrt{T_0} = 0.25 \times \sqrt{1} = 0.25
    $$

    For ATM, $d_1 = v_S / 2 = 0.125$ and $d_2 = -v_S / 2 = -0.125$.

    Using the standard normal CDF: $N(0.125) \approx 0.5498$ and $N(-0.125) \approx 0.4502$.

    **Payer swaption price:**

    $$
    V_0 = A(0)\left[S(0)\,N(d_1) - K\,N(d_2)\right]
    $$

    Since $K = S(0)$:

    $$
    V_0 = 1.8395 \times 0.04294 \times \left[N(0.125) - N(-0.125)\right]
    $$

    $$
    = 1.8395 \times 0.04294 \times (0.5498 - 0.4502) = 1.8395 \times 0.04294 \times 0.0996
    $$

    $$
    = 1.8395 \times 0.004274 = 0.007863
    $$

    The ATM payer swaption is worth approximately **0.79%** of notional, or about $\$78.63$ per $\$10{,}000$ notional.

---

**Exercise 3.** Prove that the forward swap rate $S(t) = (P(t, T_0) - P(t, T_n))/A(t)$ can be written as a weighted average of forward LIBOR rates

$$
S(t) = \sum_{i=0}^{n-1} w_i(t)\,L_i(t), \qquad w_i(t) = \frac{\delta_i\,P(t, T_{i+1})}{A(t)}
$$

and verify that $\sum_{i=0}^{n-1} w_i(t) = 1$. State what additional assumption is needed for this decomposition to hold exactly.

??? success "Solution to Exercise 3"

    **Express the floating leg using forward LIBOR rates.** The simply-compounded forward LIBOR rate for the period $[T_i, T_{i+1}]$ is

    $$
    L_i(t) = \frac{1}{\delta_i}\left(\frac{P(t, T_i)}{P(t, T_{i+1})} - 1\right)
    $$

    Rearranging: $P(t, T_i) = P(t, T_{i+1})(1 + \delta_i L_i(t))$.

    **Telescoping the floating leg.** The floating leg value is $P(t, T_0) - P(t, T_n)$. Using a telescoping decomposition:

    $$
    P(t, T_0) - P(t, T_n) = \sum_{i=0}^{n-1}\left[P(t, T_i) - P(t, T_{i+1})\right]
    $$

    From the LIBOR rate definition: $P(t, T_i) - P(t, T_{i+1}) = \delta_i L_i(t) P(t, T_{i+1})$. Therefore:

    $$
    P(t, T_0) - P(t, T_n) = \sum_{i=0}^{n-1} \delta_i L_i(t) P(t, T_{i+1})
    $$

    **Dividing by the annuity factor:**

    $$
    S(t) = \frac{P(t, T_0) - P(t, T_n)}{A(t)} = \frac{\sum_{i=0}^{n-1} \delta_i L_i(t) P(t, T_{i+1})}{\sum_{j=1}^{n} \delta_j P(t, T_j)}
    $$

    Since $T_{i+1} = T_{j}$ when $j = i + 1$ (i.e., the payment dates in the numerator and denominator align):

    $$
    S(t) = \sum_{i=0}^{n-1} \frac{\delta_i P(t, T_{i+1})}{A(t)} L_i(t) = \sum_{i=0}^{n-1} w_i(t)\,L_i(t)
    $$

    where $w_i(t) = \frac{\delta_i P(t, T_{i+1})}{A(t)}$.

    **Verifying the weights sum to one.** Note that $A(t) = \sum_{j=1}^{n} \delta_j P(t, T_j) = \sum_{i=0}^{n-1} \delta_i P(t, T_{i+1})$ (re-indexing $j = i+1$, and using $\delta_j = \delta_{j-1}$ only if $\delta_j = T_j - T_{j-1}$ and $\delta_i = T_{i+1} - T_i$, which is the same). Therefore:

    $$
    \sum_{i=0}^{n-1} w_i(t) = \sum_{i=0}^{n-1} \frac{\delta_i P(t, T_{i+1})}{A(t)} = \frac{A(t)}{A(t)} = 1
    $$

    **Additional assumption.** The decomposition holds exactly under the assumption that the accrual fractions in the swap match the LIBOR rate tenors, i.e., $\delta_i = T_{i+1} - T_i$ for all $i$, and that the LIBOR rates are simply-compounded rates over exactly these periods. In practice, day-count conventions may introduce small discrepancies.

---

**Exercise 4.** Using Rebonato's frozen-weight approximation, compute the Black swaption implied volatility for a 2-year into 3-year swaption in an LMM with three annual forward rates. The parameters are: $L_0(0) = 4.0\%$, $L_1(0) = 4.2\%$, $L_2(0) = 4.5\%$; flat volatilities $\sigma_0 = \sigma_1 = \sigma_2 = 20\%$; and exponential correlation $\rho_{ij} = e^{-0.1|i-j|}$. The forward swap rate is $S(0) = 4.23\%$ with weights $w_0 = 0.34$, $w_1 = 0.33$, $w_2 = 0.33$.

??? success "Solution to Exercise 4"

    **Setup.** We have a 2-year into 3-year swaption with three annual forward rates ($n = 3$). Expiry $T_0 = 2$, annual payments at $T_1 = 3, T_2 = 4, T_3 = 5$.

    **Given parameters:**

    - $L_0(0) = 4.0\%$, $L_1(0) = 4.2\%$, $L_2(0) = 4.5\%$
    - $\sigma_0 = \sigma_1 = \sigma_2 = 20\%$ (flat volatilities)
    - $\rho_{ij} = e^{-0.1|i-j|}$: $\rho_{00} = 1$, $\rho_{11} = 1$, $\rho_{22} = 1$, $\rho_{01} = \rho_{10} = e^{-0.1} = 0.9048$, $\rho_{02} = \rho_{20} = e^{-0.2} = 0.8187$, $\rho_{12} = \rho_{21} = e^{-0.1} = 0.9048$
    - $S(0) = 4.23\%$, $w_0 = 0.34$, $w_1 = 0.33$, $w_2 = 0.33$

    **Rebonato's formula.** With flat volatilities and expiry $T_0 = 2$:

    $$
    v_S^2 \cdot T_0 = \sum_{i,j=0}^{2} \frac{w_i(0)\,w_j(0)\,L_i(0)\,L_j(0)}{S(0)^2}\,\rho_{ij}\int_0^{T_0}\sigma_i(t)\,\sigma_j(t)\,dt
    $$

    Since $\sigma_i(t) = 0.20$ for all $i$ and $t$:

    $$
    \int_0^{2} \sigma_i(t)\sigma_j(t)\,dt = 0.04 \times 2 = 0.08
    $$

    This factor is common to all terms. Define $c_i = w_i(0) L_i(0) / S(0)$:

    - $c_0 = 0.34 \times 0.040 / 0.0423 = 0.3216$
    - $c_1 = 0.33 \times 0.042 / 0.0423 = 0.3277$
    - $c_2 = 0.33 \times 0.045 / 0.0423 = 0.3511$

    Then:

    $$
    v_S^2 \cdot T_0 = 0.08 \times \sum_{i,j} c_i\,c_j\,\rho_{ij}
    $$

    Computing the double sum:

    $$
    \sum_{i,j} c_i\,c_j\,\rho_{ij} = c_0^2 + c_1^2 + c_2^2 + 2c_0 c_1 \rho_{01} + 2c_0 c_2 \rho_{02} + 2c_1 c_2 \rho_{12}
    $$

    - $c_0^2 = 0.1034$
    - $c_1^2 = 0.1074$
    - $c_2^2 = 0.1233$
    - $2c_0 c_1 \rho_{01} = 2 \times 0.3216 \times 0.3277 \times 0.9048 = 0.1906$
    - $2c_0 c_2 \rho_{02} = 2 \times 0.3216 \times 0.3511 \times 0.8187 = 0.1849$
    - $2c_1 c_2 \rho_{12} = 2 \times 0.3277 \times 0.3511 \times 0.9048 = 0.2082$

    $$
    \sum_{i,j} c_i\,c_j\,\rho_{ij} = 0.1034 + 0.1074 + 0.1233 + 0.1906 + 0.1849 + 0.2082 = 0.9178
    $$

    Therefore:

    $$
    v_S^2 \cdot T_0 = 0.08 \times 0.9178 = 0.07342
    $$

    $$
    v_S^2 = \frac{0.07342}{2} = 0.03671
    $$

    The Black swaption implied volatility is:

    $$
    \sigma_S^{\text{Black}} = \sqrt{v_S^2 / T_0} = \sqrt{0.03671 / 2} = \sqrt{0.01836} \approx 0.1355 = 13.55\%
    $$

    Alternatively: $v_S = \sqrt{0.07342} = 0.2710$ and $\sigma_S^{\text{Black}} = v_S / \sqrt{T_0} = 0.2710/\sqrt{2} \approx 19.16\%$.

    Wait --- let me recompute more carefully. We have $v_S^2 = \int_0^{T_0}\sigma_S(t)^2\,dt$. Rebonato's formula gives $v_S^2 T_0$ on the left side. Actually, reviewing the formula:

    $$
    v_S^2\,T_0 \approx \sum_{i,j} \frac{w_i w_j L_i L_j}{S(0)^2}\rho_{ij}\int_0^{T_0}\sigma_i(t)\sigma_j(t)\,dt
    $$

    With $\sigma_S^{\text{Black}}$ defined as $v_S = \sigma_S^{\text{Black}}\sqrt{T_0}$, we get $(\sigma_S^{\text{Black}})^2 T_0 = v_S^2$. So:

    $$
    (\sigma_S^{\text{Black}})^2 T_0 \cdot T_0 = v_S^2 \cdot T_0 = 0.07342
    $$

    This gives $(\sigma_S^{\text{Black}})^2 = 0.07342 / T_0^2 = 0.07342 / 4 = 0.01836$, so $\sigma_S^{\text{Black}} = 13.5\%$.

    However, the standard convention is that $v_S^2 = (\sigma_S^{\text{Black}})^2 T_0$, so $(\sigma_S^{\text{Black}})^2 = v_S^2 / T_0 = 0.07342 / 2 = 0.03671$, giving $\sigma_S^{\text{Black}} = \sqrt{0.03671} \approx 19.2\%$.

    The Black swaption implied volatility is approximately **19.2%**.

    Note that this is slightly below the individual forward rate volatility of 20%, reflecting the diversification effect from imperfect correlations ($\rho_{ij} < 1$ for $i \neq j$).

---

**Exercise 5.** Derive the put--call parity relationship for swaptions. Show that the difference between a payer and a receiver swaption with the same strike and expiry equals

$$
V_0^{\text{payer}} - V_0^{\text{receiver}} = A(0)(S(0) - K)
$$

Interpret this result in terms of the value of a forward-starting swap.

??? success "Solution to Exercise 5"

    **Payer swaption payoff:** $V_{T_0}^{\text{payer}} = A(T_0)\max(S(T_0) - K, 0)$

    **Receiver swaption payoff:** $V_{T_0}^{\text{receiver}} = A(T_0)\max(K - S(T_0), 0)$

    **Difference of payoffs.** Using the identity $\max(x, 0) - \max(-x, 0) = x$:

    $$
    V_{T_0}^{\text{payer}} - V_{T_0}^{\text{receiver}} = A(T_0)\left[\max(S(T_0) - K, 0) - \max(K - S(T_0), 0)\right] = A(T_0)(S(T_0) - K)
    $$

    **Pricing both sides.** Under the swap measure $\mathbb{Q}^A$ with numéraire $A(t)$:

    $$
    V_0^{\text{payer}} - V_0^{\text{receiver}} = A(0)\,\mathbb{E}^{\mathbb{Q}^A}\!\left[S(T_0) - K\right]
    $$

    Since $S(t)$ is a $\mathbb{Q}^A$-martingale, $\mathbb{E}^{\mathbb{Q}^A}[S(T_0)] = S(0)$. Therefore:

    $$
    V_0^{\text{payer}} - V_0^{\text{receiver}} = A(0)(S(0) - K)
    $$

    **Financial interpretation.** The right-hand side $A(0)(S(0) - K)$ is the value of a **forward-starting swap** where one pays fixed rate $K$ and receives floating, starting at $T_0$. The forward swap rate $S(0)$ is the break-even fixed rate. If $K < S(0)$, the payer swaption is worth more than the receiver (it is more likely to be exercised), and the difference equals the value of a swap at the off-market rate $K$.

    This is the swaption analogue of the standard put--call parity for European options on stocks: $C - P = S_0 - Ke^{-rT}$, where the forward replaces the stock and the annuity factor replaces the discount factor.

---

**Exercise 6.** An ATM swaption straddle on a 5-year swap has $A(0) = 4.20$, $S(0) = 3.8\%$, and Black implied volatility $\sigma_S = 22\%$ with expiry $T_0 = 2$ years. Using the approximation $V_0^{\text{ATM straddle}} \approx 2A(0)\,S(0)\,v_S/\sqrt{2\pi}$, compute the straddle value and express it as a percentage of the notional.

??? success "Solution to Exercise 6"

    **Given data:** $A(0) = 4.20$, $S(0) = 3.8\% = 0.038$, $\sigma_S = 22\%$, $T_0 = 2$ years.

    **Integrated volatility:**

    $$
    v_S = \sigma_S \sqrt{T_0} = 0.22 \times \sqrt{2} = 0.22 \times 1.4142 = 0.31113
    $$

    **ATM straddle approximation:**

    $$
    V_0^{\text{ATM straddle}} \approx 2\,A(0)\,S(0)\,\frac{v_S}{\sqrt{2\pi}}
    $$

    Computing $v_S / \sqrt{2\pi}$:

    $$
    \frac{v_S}{\sqrt{2\pi}} = \frac{0.31113}{2.5066} = 0.12413
    $$

    Therefore:

    $$
    V_0^{\text{ATM straddle}} \approx 2 \times 4.20 \times 0.038 \times 0.12413 = 2 \times 4.20 \times 0.004717
    $$

    $$
    = 2 \times 0.019811 = 0.039622
    $$

    **As a percentage of notional:** The straddle value is approximately **3.96%** of the notional, or equivalently $\$396$ per $\$10{,}000$ notional.

---

**Exercise 7.** The swap measure $\mathbb{Q}^A$ can be viewed as a weighted combination of individual forward measures. Starting from the Radon--Nikodym derivative

$$
\frac{d\mathbb{Q}^A}{d\mathbb{Q}^{T_j}}\bigg|_{\mathcal{F}_t} = \frac{A(t)\,P(0, T_j)}{P(t, T_j)\,A(0)}
$$

derive the Girsanov drift adjustment $dW_t^A = dW_t^{T_j} - [\sigma_A(t) - \Sigma(t, T_j)]\,dt$, identifying the volatility $\sigma_A(t)$ of the annuity factor in terms of the individual bond volatilities $\Sigma(t, T_k)$.

??? success "Solution to Exercise 7"

    **Starting point.** The Radon--Nikodym derivative from $\mathbb{Q}^{T_j}$ to $\mathbb{Q}^A$ is

    $$
    \frac{d\mathbb{Q}^A}{d\mathbb{Q}^{T_j}}\bigg|_{\mathcal{F}_t} = \frac{A(t)\,P(0, T_j)}{P(t, T_j)\,A(0)} = \frac{A(t)/A(0)}{P(t, T_j)/P(0, T_j)}
    $$

    **Dynamics of the ratio.** Define $R(t) = A(t)/P(t, T_j)$. Under $\mathbb{Q}^{T_j}$, the Radon--Nikodym derivative is $R(t)/R(0)$, which must be a $\mathbb{Q}^{T_j}$-martingale.

    Under $\mathbb{Q}^{T_j}$, the bond $P(t, T_j)$ dynamics have volatility $\Sigma(t, T_j)$, and the annuity factor dynamics have volatility $\sigma_A(t)$. By Itô's quotient rule, the volatility of $R(t)$ is $\sigma_A(t) - \Sigma(t, T_j)$.

    **Identifying $\sigma_A(t)$.** The annuity factor $A(t) = \sum_{k=1}^{n}\delta_k P(t, T_k)$ is a portfolio of bonds. Under $\mathbb{Q}$ (or any equivalent measure), each bond satisfies

    $$
    \frac{dP(t, T_k)}{P(t, T_k)} = (\cdots)\,dt + \Sigma(t, T_k)\,dW_t
    $$

    where $\Sigma(t, T_k) = -\int_t^{T_k}\sigma(t, u)\,du$ is the bond volatility. By the linearity of the portfolio:

    $$
    \frac{dA(t)}{A(t)} = (\cdots)\,dt + \sigma_A(t)\,dW_t
    $$

    where the annuity volatility is the weighted average of bond volatilities:

    $$
    \sigma_A(t) = \sum_{k=1}^{n} \frac{\delta_k P(t, T_k)}{A(t)}\,\Sigma(t, T_k) = -\sum_{k=1}^{n} \frac{\delta_k P(t, T_k)}{A(t)}\int_t^{T_k}\sigma(t, u)\,du
    $$

    The weights $\delta_k P(t, T_k)/A(t)$ are the fractional contributions of each bond to the annuity.

    **Girsanov transformation.** The Radon--Nikodym derivative $R(t)/R(0)$ is an exponential martingale under $\mathbb{Q}^{T_j}$ with volatility $\sigma_A(t) - \Sigma(t, T_j)$. By Girsanov's theorem:

    $$
    dW_t^A = dW_t^{T_j} - \left[\sigma_A(t) - \Sigma(t, T_j)\right]dt
    $$

    This drift adjustment converts a $\mathbb{Q}^{T_j}$-Brownian motion into a $\mathbb{Q}^A$-Brownian motion. The adjustment depends on:

    - $\sigma_A(t)$: the volatility of the entire annuity portfolio (a weighted average over all payment date bond volatilities)
    - $\Sigma(t, T_j)$: the volatility of the specific bond $P(t, T_j)$

    The difference $\sigma_A(t) - \Sigma(t, T_j)$ captures the extent to which the annuity's risk profile differs from that of the single bond $P(t, T_j)$.
