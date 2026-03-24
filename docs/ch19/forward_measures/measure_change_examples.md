# Measure Change Examples

The abstract machinery of numéraire change and Girsanov's theorem becomes concrete through worked examples. This section applies the general framework to the two most important cases in interest rate derivatives: the **$T$-forward measure** for pricing bond options and the **annuity (swap) measure** for pricing swaptions. Each example follows the same pattern --- identify the natural numéraire, compute the Radon--Nikodym derivative, transform the dynamics, and evaluate the resulting expectation.

---

## Recap of the General Framework

### Numéraire Change Formula

For any strictly positive numéraire $N_t$ with associated measure $\mathbb{Q}^N$, the price of a derivative with payoff $V_T$ at time $T$ is

$$
V_t = N_t \, \mathbb{E}^{\mathbb{Q}^N}\!\left[\frac{V_T}{N_T} \;\middle|\; \mathcal{F}_t\right]
$$

The Radon--Nikodym derivative connecting the risk-neutral measure $\mathbb{Q}$ (numéraire $B_t$) to $\mathbb{Q}^N$ is

$$
\frac{d\mathbb{Q}^N}{d\mathbb{Q}}\bigg|_{\mathcal{F}_t} = \frac{N_t / N_0}{B_t / B_0}
$$

### Girsanov's Theorem

If $W_t^{\mathbb{Q}}$ is a Brownian motion under $\mathbb{Q}$, then under $\mathbb{Q}^N$,

$$
W_t^N = W_t^{\mathbb{Q}} - \int_0^t \sigma_N(s) \, ds
$$

is a Brownian motion, where $\sigma_N(t)$ is the volatility of the numéraire process: $dN_t / N_t = (\cdots)\,dt + \sigma_N(t)\,dW_t^{\mathbb{Q}}$.

---

## Example 1: Bond Option Under the T-Forward Measure

### Setup

Consider a European call option on a zero-coupon bond $P(t, T_B)$ with:

- Option maturity $T$ (with $T < T_B$)
- Strike price $K$
- Payoff at time $T$: $\max(P(T, T_B) - K, 0)$

Under the risk-neutral measure $\mathbb{Q}$, the option price is

$$
C_0 = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_0^T r_s \, ds} \max(P(T, T_B) - K, 0)\right]
$$

The stochastic discount factor $e^{-\int_0^T r_s \, ds}$ and the bond price $P(T, T_B)$ are correlated, making this expectation difficult to evaluate directly.

### Step 1: Choose the Numéraire

Choose $N_t = P(t, T)$, the zero-coupon bond maturing at the option expiry $T$. The associated measure is the $T$-forward measure $\mathbb{Q}^T$.

### Step 2: Apply the Pricing Formula

$$
C_0 = P(0, T) \, \mathbb{E}^{\mathbb{Q}^T}\!\left[\max(P(T, T_B) - K, 0)\right]
$$

Since $P(T, T) = 1$, the numéraire at maturity equals one, and the stochastic discount factor disappears. The expectation is now over the terminal bond price alone.

### Step 3: Identify the Martingale

Under $\mathbb{Q}^T$, the forward bond price

$$
F(t) = \frac{P(t, T_B)}{P(t, T)}
$$

is a martingale. This is the forward price of the $T_B$-bond for settlement at $T$.

### Step 4: Derive Dynamics of the Forward Bond Price

Under $\mathbb{Q}$, the bond price dynamics are

$$
\frac{dP(t, T_B)}{P(t, T_B)} = r_t \, dt - \Sigma(t, T_B) \, dW_t^{\mathbb{Q}}
$$

$$
\frac{dP(t, T)}{P(t, T)} = r_t \, dt - \Sigma(t, T) \, dW_t^{\mathbb{Q}}
$$

where $\Sigma(t, U) = \int_t^U \sigma(t, u) \, du$ is the bond volatility.

By Itô's quotient rule, the forward bond price satisfies

$$
\frac{dF(t)}{F(t)} = \bigl[\Sigma(t, T) - \Sigma(t, T_B)\bigr] \bigl[\Sigma(t, T) \, dt - dW_t^{\mathbb{Q}}\bigr]
$$

Under the Girsanov change $dW_t^T = dW_t^{\mathbb{Q}} + \Sigma(t, T) \, dt$, this simplifies to

$$
\frac{dF(t)}{F(t)} = \sigma_F(t) \, dW_t^T
$$

where the forward bond price volatility is

$$
\sigma_F(t) = \Sigma(t, T_B) - \Sigma(t, T) = \int_T^{T_B} \sigma(t, u) \, du
$$

The forward bond price is indeed a driftless diffusion (martingale) under $\mathbb{Q}^T$.

### Step 5: Evaluate the Option Price

Since $F(t)$ follows a geometric Brownian motion under $\mathbb{Q}^T$ with zero drift, $P(T, T_B) = F(T) \cdot P(T, T) = F(T)$ is lognormally distributed. The call option price follows the Black formula:

$$
\boxed{C_0 = P(0, T)\bigl[F(0) \, N(d_1) - K \, N(d_2)\bigr]}
$$

where $F(0) = P(0, T_B) / P(0, T)$ and

$$
d_1 = \frac{\ln(F(0)/K) + \tfrac{1}{2} v^2}{v}, \qquad d_2 = d_1 - v
$$

with the integrated forward bond price variance

$$
v^2 = \int_0^T \sigma_F(t)^2 \, dt
$$

### Worked Calculation: Vasicek Model

In the Vasicek model, $\sigma(t, T) = \sigma \, e^{-\kappa(T - t)}$, so

$$
\Sigma(t, U) = \frac{\sigma}{\kappa}\bigl(1 - e^{-\kappa(U - t)}\bigr)
$$

The forward bond price volatility is

$$
\sigma_F(t) = \Sigma(t, T_B) - \Sigma(t, T) = \frac{\sigma}{\kappa}\bigl(e^{-\kappa(T - t)} - e^{-\kappa(T_B - t)}\bigr)
$$

The integrated variance is

$$
v^2 = \int_0^T \left[\frac{\sigma}{\kappa}\bigl(e^{-\kappa(T - t)} - e^{-\kappa(T_B - t)}\bigr)\right]^2 dt
$$

Denoting $B(\tau) = (1 - e^{-\kappa \tau})/\kappa$, one obtains

$$
v^2 = \sigma^2 \, B(T_B - T)^2 \cdot \frac{1 - e^{-2\kappa T}}{2\kappa}
$$

??? example "Numerical Example"

    **Parameters:** $\sigma = 0.01$, $\kappa = 0.1$, $T = 1$, $T_B = 5$, $K = 0.85$, $P(0,1) = 0.97$, $P(0,5) = 0.82$.

    **Step 1:** Forward bond price: $F(0) = 0.82 / 0.97 = 0.8454$.

    **Step 2:** $B(4) = (1 - e^{-0.4})/0.1 = 3.2968$.

    **Step 3:** $v^2 = 0.01^2 \times 3.2968^2 \times (1 - e^{-0.2})/0.2 = 0.0001 \times 10.8689 \times 0.9063 = 0.000985$.

    **Step 4:** $v = 0.0314$.

    **Step 5:** $d_1 = [\ln(0.8454/0.85) + 0.5 \times 0.000985]/0.0314 = (-0.00543 + 0.000493)/0.0314 = -0.157$.

    **Step 6:** $d_2 = -0.157 - 0.0314 = -0.189$.

    **Step 7:** $C_0 = 0.97 \times [0.8454 \times N(-0.157) - 0.85 \times N(-0.189)] = 0.97 \times [0.8454 \times 0.4376 - 0.85 \times 0.4251] = 0.97 \times [0.3700 - 0.3613] = 0.97 \times 0.0087 = 0.0084$.

    The bond option is worth approximately \$0.84 per \$100 notional.

---

## Example 2: Caplet Under the Forward Measure

### Setup

A caplet pays $\delta \max(L(T_i) - K, 0)$ at time $T_{i+1}$, where $L(T_i)$ is the LIBOR rate fixing at $T_i$ for the period $[T_i, T_{i+1}]$ and $\delta = T_{i+1} - T_i$.

### Natural Numéraire

Choose $N_t = P(t, T_{i+1})$, so the pricing measure is $\mathbb{Q}^{T_{i+1}}$.

### Forward LIBOR as Martingale

The forward LIBOR rate $L_i(t)$ is a martingale under $\mathbb{Q}^{T_{i+1}}$ because

$$
L_i(t) = \frac{1}{\delta}\left(\frac{P(t, T_i)}{P(t, T_{i+1})} - 1\right)
$$

is a ratio of bond prices normalized by $P(t, T_{i+1})$ (up to constants). Under lognormal dynamics:

$$
\frac{dL_i(t)}{L_i(t)} = \sigma_i(t) \, dW_i^{T_{i+1}}(t)
$$

### Caplet Price

$$
\text{Caplet} = P(0, T_{i+1}) \, \mathbb{E}^{\mathbb{Q}^{T_{i+1}}}\!\left[\delta \max(L_i(T_i) - K, 0)\right]
$$

Since $L_i(T_i)$ is lognormally distributed under $\mathbb{Q}^{T_{i+1}}$:

$$
\boxed{\text{Caplet} = \delta \, P(0, T_{i+1})\bigl[L_i(0) \, N(d_1) - K \, N(d_2)\bigr]}
$$

$$
d_1 = \frac{\ln(L_i(0)/K) + \tfrac{1}{2} v_i^2}{v_i}, \qquad d_2 = d_1 - v_i, \qquad v_i^2 = \int_0^{T_i} \sigma_i(t)^2 \, dt
$$

The measure change has eliminated the need for stochastic discounting and produced the standard Black caplet formula.

---

## Example 3: Swaption Under the Annuity Measure

### Setup

A **payer swaption** gives the right to enter a payer swap (pay fixed, receive floating) at time $T_0$ with payment dates $T_1, T_2, \ldots, T_n$. The payoff at $T_0$ is

$$
\text{Payoff} = A(T_0) \max(S(T_0) - K, 0)
$$

where $S(t)$ is the forward swap rate and $A(t) = \sum_{j=1}^{n} \delta_j P(t, T_j)$ is the annuity factor.

### Why the Annuity Measure?

Under the risk-neutral measure, the swaption price is

$$
V_0 = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_0^{T_0} r_s \, ds} \, A(T_0) \max(S(T_0) - K, 0)\right]
$$

The product of the stochastic discount factor with $A(T_0)$ makes direct evaluation complicated. The annuity measure eliminates this difficulty.

### Step 1: Choose the Numéraire

Set $N_t = A(t)$, the present value of the annuity stream. The associated measure is the **swap (annuity) measure** $\mathbb{Q}^A$.

### Step 2: Apply the Pricing Formula

$$
V_0 = A(0) \, \mathbb{E}^{\mathbb{Q}^A}\!\left[\max(S(T_0) - K, 0)\right]
$$

### Step 3: Swap Rate as Martingale

The forward swap rate is

$$
S(t) = \frac{P(t, T_0) - P(t, T_n)}{A(t)}
$$

Under the annuity measure $\mathbb{Q}^A$, the swap rate $S(t)$ is a martingale because the numerator $P(t, T_0) - P(t, T_n)$ is the value of the floating leg, and dividing by the numéraire $A(t)$ produces a martingale.

### Step 4: Dynamics Under the Swap Measure

Assuming lognormal dynamics for the swap rate under $\mathbb{Q}^A$:

$$
\frac{dS(t)}{S(t)} = \sigma_S(t) \, dW_t^A
$$

The swap rate is a driftless geometric Brownian motion under the annuity measure.

### Step 5: Swaption Price (Black's Formula)

Since $S(T_0)$ is lognormally distributed:

$$
\boxed{V_0 = A(0)\bigl[S(0) \, N(d_1) - K \, N(d_2)\bigr]}
$$

$$
d_1 = \frac{\ln(S(0)/K) + \tfrac{1}{2} v_S^2}{v_S}, \qquad d_2 = d_1 - v_S, \qquad v_S^2 = \int_0^{T_0} \sigma_S(t)^2 \, dt
$$

### Radon--Nikodym Derivative

The explicit Radon--Nikodym derivative from $\mathbb{Q}$ to $\mathbb{Q}^A$ is

$$
\frac{d\mathbb{Q}^A}{d\mathbb{Q}}\bigg|_{\mathcal{F}_t} = \frac{A(t) / A(0)}{B_t}
$$

where $B_t = \exp\left(\int_0^t r_s \, ds\right)$.

The Girsanov drift adjustment from $\mathbb{Q}$ to $\mathbb{Q}^A$ involves the volatility of the annuity factor, which depends on all the bond price volatilities $\Sigma(t, T_j)$ weighted by the annuity contributions.

??? example "Numerical Example"

    **Parameters:** 2-year into 3-year payer swaption ($T_0 = 2$, annual payments at $T_1 = 3, T_2 = 4, T_3 = 5$), strike $K = 4\%$, $\sigma_S = 20\%$.

    **Market data:** $P(0,2) = 0.94$, $P(0,3) = 0.91$, $P(0,4) = 0.87$, $P(0,5) = 0.83$.

    **Step 1:** Annuity factor: $A(0) = 1 \times (0.91 + 0.87 + 0.83) = 2.61$.

    **Step 2:** Forward swap rate: $S(0) = (0.94 - 0.83)/2.61 = 0.0421 = 4.21\%$.

    **Step 3:** Integrated variance: $v_S = 0.20 \times \sqrt{2} = 0.2828$.

    **Step 4:** $d_1 = [\ln(0.0421/0.04) + 0.5 \times 0.08]/0.2828 = [0.0513 + 0.04]/0.2828 = 0.323$.

    **Step 5:** $d_2 = 0.323 - 0.2828 = 0.040$.

    **Step 6:** $V_0 = 2.61 \times [0.0421 \times N(0.323) - 0.04 \times N(0.040)] = 2.61 \times [0.0421 \times 0.6267 - 0.04 \times 0.5160] = 2.61 \times [0.02638 - 0.02064] = 2.61 \times 0.00574 = 0.01498$.

    The swaption is worth approximately 1.50% of notional, or \$150 per \$10,000 notional.

---

## Summary of Measure Changes

The following table summarizes the standard measure changes used in interest rate derivative pricing:

| Derivative | Numéraire $N_t$ | Measure | Martingale Rate | Formula Type |
|---|---|---|---|---|
| Bond option | $P(t, T)$ | $\mathbb{Q}^T$ | Forward bond price | Black |
| Caplet/Floorlet | $P(t, T_{i+1})$ | $\mathbb{Q}^{T_{i+1}}$ | Forward LIBOR $L_i(t)$ | Black |
| Swaption | Annuity $A(t)$ | $\mathbb{Q}^A$ | Forward swap rate $S(t)$ | Black |
| FRA | $P(t, T_{i+1})$ | $\mathbb{Q}^{T_{i+1}}$ | Forward LIBOR $L_i(t)$ | Linear |

### Common Pattern

Every example follows the same logic:

1. **Identify the payoff structure:** Which rate or price appears in the payoff?
2. **Choose the natural numéraire:** Pick the numéraire that makes the relevant rate a martingale.
3. **Apply Girsanov:** Transform the Brownian motion and verify the drift vanishes.
4. **Evaluate the expectation:** With a driftless lognormal process, Black's formula applies directly.

!!! tip "Choosing the Right Measure"
    The "natural" measure for a derivative is the one that makes the rate appearing in the payoff a martingale. For products paying at $T$, use the $T$-forward measure. For swap-like products with annuity weighting, use the swap measure. The wrong measure choice does not produce wrong prices, but it does produce unnecessary complexity in the drift.

---

## Connections Between Forward and Swap Measures

### Measure Change Between Forward Measures

Moving from $\mathbb{Q}^{T_j}$ to $\mathbb{Q}^{T_i}$ (for $j > i$), the Girsanov drift adjustment involves the bond volatility difference:

$$
dW_t^{T_i} = dW_t^{T_j} + \bigl[\Sigma(t, T_j) - \Sigma(t, T_i)\bigr] dt
$$

### Swap Measure as a Weighted Average

The swap measure can be viewed as a weighted combination of individual forward measures. The Radon--Nikodym derivative from $\mathbb{Q}^{T_j}$ to $\mathbb{Q}^A$ involves

$$
\frac{d\mathbb{Q}^A}{d\mathbb{Q}^{T_j}}\bigg|_{\mathcal{F}_t} = \frac{A(t) \cdot P(0, T_j)}{P(t, T_j) \cdot A(0)}
$$

The weights in the annuity combine contributions from each payment date, reflecting the fact that the swap measure "averages" over the individual forward measures at each payment date.

---

## Key Takeaways

- The $T$-forward measure uses $P(t,T)$ as numéraire and makes forward prices and forward rates martingales, eliminating stochastic discounting for payoffs at time $T$
- The annuity (swap) measure uses $A(t) = \sum \delta_j P(t, T_j)$ as numéraire and makes the forward swap rate a martingale, leading directly to Black's swaption formula
- Every standard interest rate option formula arises from choosing the natural measure, obtaining lognormal dynamics, and applying the Black formula
- The Radon--Nikodym derivative between measures encodes the volatility of the numéraire ratio, and the Girsanov drift adjustment is determined by this volatility

---

## Further Reading

- Brigo & Mercurio (2006), *Interest Rate Models: Theory and Practice*, Chapter 1 (Change of Numéraire)
- Björk (2009), *Arbitrage Theory in Continuous Time*, Chapter 26 (Forward Measures)
- Rebonato (2002), *Modern Pricing of Interest-Rate Derivatives*, Chapters 7--8
- Jamshidian (1997), "LIBOR and Swap Market Models and Measures"

---

## Exercises

**Exercise 1.** Consider a European put option on a zero-coupon bond $P(t, T_B)$ with maturity $T < T_B$ and strike $K$. Using the $T$-forward measure with numéraire $P(t, T)$, derive the put price formula analogous to the call formula in Example 1. Express the result in terms of the forward bond price $F(0) = P(0, T_B)/P(0, T)$, the integrated variance $v^2$, and $K$.

---

**Exercise 2.** In the Vasicek model with $\sigma = 0.008$, $\kappa = 0.15$, the zero-coupon bond prices are $P(0,2) = 0.94$ and $P(0,7) = 0.76$. Price a European call option on $P(t, 7)$ with maturity $T = 2$ and strike $K = 0.80$. Carry out the full calculation: compute the forward bond price, the integrated variance using

$$
v^2 = \sigma^2 \, B(T_B - T)^2 \cdot \frac{1 - e^{-2\kappa T}}{2\kappa},
$$

then apply Black's formula.

---

**Exercise 3.** A caplet on 6-month LIBOR has fixing date $T_i = 3$, payment date $T_{i+1} = 3.5$, strike $K = 4\%$, and notional \$1 million. The forward LIBOR rate is $L_i(0) = 4.5\%$, the Black implied volatility is $\sigma_i = 20\%$, and $P(0, 3.5) = 0.87$. Compute the caplet price using the $T_{i+1}$-forward measure. Verify that the intrinsic value (replacing $N(d_1), N(d_2)$ with 1 for deep in-the-money) gives an upper bound for the price.

---

**Exercise 4.** Explain why the forward swap rate $S(t) = (P(t, T_0) - P(t, T_n))/A(t)$ is a martingale under the annuity measure $\mathbb{Q}^A$ but not under the risk-neutral measure $\mathbb{Q}$. Identify the drift of $S(t)$ under $\mathbb{Q}$ in terms of the volatilities of the bond prices and the annuity factor.

---

**Exercise 5.** A 1-year into 2-year receiver swaption (the right to enter a receiver swap: receive fixed, pay floating) has strike $K = 3.5\%$, with annual payments at $T_1 = 2$ and $T_2 = 3$. The market data are $P(0,1) = 0.97$, $P(0,2) = 0.935$, $P(0,3) = 0.90$, and the swaption implied volatility is $\sigma_S = 18\%$. Compute the annuity factor, the forward swap rate, and the receiver swaption price using Black's formula under the annuity measure.

---

**Exercise 6.** Starting from the Radon--Nikodym derivative $d\mathbb{Q}^{T_i}/d\mathbb{Q}^{T_j} = (P(t,T_i)/P(0,T_i))/(P(t,T_j)/P(0,T_j))$ for $j > i$, derive the Girsanov drift adjustment that converts a Brownian motion $W^{T_j}$ into a Brownian motion $W^{T_i}$. Express the drift in terms of the bond volatility functions $\Sigma(t, T_i)$ and $\Sigma(t, T_j)$.

---

**Exercise 7.** A floorlet on 3-month LIBOR pays $\delta \max(K - L_i(T_i), 0)$ at $T_{i+1}$. Using put-call parity for the caplet and floorlet (both priced under $\mathbb{Q}^{T_{i+1}}$), show that

$$
\text{Caplet} - \text{Floorlet} = \delta \, P(0, T_{i+1})(L_i(0) - K)
$$

Verify this identity numerically using $L_i(0) = 5\%$, $K = 4.5\%$, $\sigma_i = 22\%$, $T_i = 2$, $\delta = 0.25$, and $P(0, T_{i+1}) = 0.91$.
