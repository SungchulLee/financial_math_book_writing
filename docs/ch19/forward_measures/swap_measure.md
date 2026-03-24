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

### Rebonato's Approximation

In the LIBOR Market Model, the swap rate $S(t) = \sum_i w_i(t) L_i(t)$ is not exactly lognormal. The effective swap rate volatility is approximated by freezing the weights at their initial values:

$$
v_S^2 \, T_0 \approx \sum_{i,j=0}^{n-1} \frac{w_i(0) \, w_j(0) \, L_i(0) \, L_j(0)}{S(0)^2} \, \rho_{ij} \int_0^{T_0} \sigma_i(t) \, \sigma_j(t) \, dt
$$

This is **Rebonato's swaption volatility formula**, which expresses the Black swaption implied volatility in terms of the LMM parameters (forward rate volatilities and correlations).

### Interpretation

- The **diagonal terms** ($i = j$) capture individual forward rate contributions
- The **off-diagonal terms** ($i \neq j$) reflect the impact of correlation between forward rates
- Lower correlation reduces the effective swap rate volatility (diversification effect)

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

---

**Exercise 2.** Using the data from Exercise 1, price a 3-year ATM payer swaption (exercise at $T_0 = 0$, but assume the swaption expires in 1 year with $T_0 = 1$, payment dates $T_1 = 1.5, \ldots, T_4 = 3.0$) with Black implied volatility $\sigma_S = 25\%$. Recompute $A(0)$ and $S(0)$ for this sub-swap and apply Black's swaption formula.

---

**Exercise 3.** Prove that the forward swap rate $S(t) = (P(t, T_0) - P(t, T_n))/A(t)$ can be written as a weighted average of forward LIBOR rates

$$
S(t) = \sum_{i=0}^{n-1} w_i(t)\,L_i(t), \qquad w_i(t) = \frac{\delta_i\,P(t, T_{i+1})}{A(t)}
$$

and verify that $\sum_{i=0}^{n-1} w_i(t) = 1$. State what additional assumption is needed for this decomposition to hold exactly.

---

**Exercise 4.** Using Rebonato's frozen-weight approximation, compute the Black swaption implied volatility for a 2-year into 3-year swaption in an LMM with three annual forward rates. The parameters are: $L_0(0) = 4.0\%$, $L_1(0) = 4.2\%$, $L_2(0) = 4.5\%$; flat volatilities $\sigma_0 = \sigma_1 = \sigma_2 = 20\%$; and exponential correlation $\rho_{ij} = e^{-0.1|i-j|}$. The forward swap rate is $S(0) = 4.23\%$ with weights $w_0 = 0.34$, $w_1 = 0.33$, $w_2 = 0.33$.

---

**Exercise 5.** Derive the put--call parity relationship for swaptions. Show that the difference between a payer and a receiver swaption with the same strike and expiry equals

$$
V_0^{\text{payer}} - V_0^{\text{receiver}} = A(0)(S(0) - K)
$$

Interpret this result in terms of the value of a forward-starting swap.

---

**Exercise 6.** An ATM swaption straddle on a 5-year swap has $A(0) = 4.20$, $S(0) = 3.8\%$, and Black implied volatility $\sigma_S = 22\%$ with expiry $T_0 = 2$ years. Using the approximation $V_0^{\text{ATM straddle}} \approx 2A(0)\,S(0)\,v_S/\sqrt{2\pi}$, compute the straddle value and express it as a percentage of the notional.

---

**Exercise 7.** The swap measure $\mathbb{Q}^A$ can be viewed as a weighted combination of individual forward measures. Starting from the Radon--Nikodym derivative

$$
\frac{d\mathbb{Q}^A}{d\mathbb{Q}^{T_j}}\bigg|_{\mathcal{F}_t} = \frac{A(t)\,P(0, T_j)}{P(t, T_j)\,A(0)},
$$

derive the Girsanov drift adjustment $dW_t^A = dW_t^{T_j} - [\sigma_A(t) - \Sigma(t, T_j)]\,dt$, identifying the volatility $\sigma_A(t)$ of the annuity factor in terms of the individual bond volatilities $\Sigma(t, T_k)$.
