# Bond Options

**Bond options** are European or American options written on zero-coupon or coupon bonds. They are fundamental interest rate derivatives and serve as building blocks for understanding caps, floors, and swaptions.

---

## European Options on Zero-Coupon Bonds

### Contract Specification

A **European call option** on a zero-coupon bond:
- **Underlying:** $T_B$-maturity zero-coupon bond $P(t, T_B)$
- **Strike:** $K$
- **Expiry:** $T < T_B$

**Payoff at expiry:**

$$
(P(T, T_B) - K)^+
$$

A **European put option** has payoff $(K - P(T, T_B))^+$.

### Pricing Framework

Under the $T$-forward measure $\mathbb{Q}^T$:

$$
C(0) = P(0, T) \cdot \mathbb{E}^{\mathbb{Q}^T}[(P(T, T_B) - K)^+]
$$

The forward bond price $P(T, T_B)$ is a martingale under $\mathbb{Q}^T$.

---

## Pricing in the Vasicek Model

### Setup

In the Vasicek model:
- $P(t, T_B) = A(T_B - t) e^{-B(T_B - t) r_t}$
- $r_T$ is Gaussian given $r_0$

### Bond Price Distribution

At the option expiry $T$:

$$
\log P(T, T_B) = \log A(\tau_B) - B(\tau_B) r_T
$$

where $\tau_B = T_B - T$.

Since $r_T$ is Gaussian, $\log P(T, T_B)$ is also Gaussian (shifted and scaled).

### The Jamshidian Formula

$$
\boxed{C(0) = P(0, T_B) N(d_1) - K P(0, T) N(d_2)}
$$

where:

$$
d_1 = \frac{1}{\sigma_P} \ln \frac{P(0, T_B)}{K P(0, T)} + \frac{\sigma_P}{2}
$$

$$
d_2 = d_1 - \sigma_P
$$

### Bond Price Volatility

$$
\sigma_P = \sigma \cdot B(T_B - T) \cdot \sqrt{\frac{1 - e^{-2\kappa T}}{2\kappa}}
$$

where:
- $\sigma$ is the short-rate volatility
- $B(\tau) = (1 - e^{-\kappa \tau})/\kappa$
- $\kappa$ is the mean-reversion speed

### Put Option

By put-call parity for bond options:

$$
P_{\text{put}}(0) = K P(0, T) N(-d_2) - P(0, T_B) N(-d_1)
$$

---

## Pricing in the Hull-White Model

### The Formula

The Hull-White bond option formula is structurally identical to Vasicek:

$$
C(0) = P(0, T_B) N(d_1) - K P(0, T) N(d_2)
$$

The only difference is in the discount factors $P(0, T)$ and $P(0, T_B)$, which now match the market curve exactly.

### Bond Price Volatility (Hull-White)

$$
\sigma_P = \sigma \cdot \frac{1 - e^{-\kappa(T_B - T)}}{\kappa} \cdot \sqrt{\frac{1 - e^{-2\kappa T}}{2\kappa}}
$$

---

## Pricing in the CIR Model

### Non-Central Chi-Squared Approach

In CIR, bond prices follow:

$$
P(T, T_B) = A(\tau_B) e^{-B(\tau_B) r_T}
$$

where $r_T$ has a non-central chi-squared distribution.

### Option Pricing Formula

The CIR bond option price involves the non-central chi-squared CDF:

$$
C(0) = P(0, T_B) \chi^2(x^*; \nu + 2, \lambda_1) - K P(0, T) \chi^2(x^*; \nu, \lambda_2)
$$

where:
- $\nu = 4\kappa\theta/\sigma^2$ (degrees of freedom)
- $\lambda_1, \lambda_2$ are non-centrality parameters depending on model parameters
- $x^*$ is a threshold determined by the strike

### Computational Notes

The non-central chi-squared CDF can be computed via:
- Series expansion
- Numerical integration
- Library functions (e.g., in Python's scipy)

---

## Options on Coupon Bonds

### Jamshidian's Decomposition

Consider a European call on a coupon bond with cashflows $c_i$ at times $T_i$ (for $i = 1, \ldots, n$), with option expiry $T < T_1$.

**Key insight:** In one-factor models, all bond prices are monotonic in $r_T$.

Define $r^*$ as the short rate at which the coupon bond price equals the strike:

$$
\sum_{i=1}^{n} c_i P(T, T_i, r^*) = K
$$

### Decomposition

The coupon bond option decomposes into a portfolio of zero-coupon bond options:

$$
\text{Call on coupon bond} = \sum_{i=1}^{n} c_i \cdot \text{Call}(P(T, T_i), K_i)
$$

where:

$$
K_i = P(T, T_i, r^*)
$$

### Algorithm

1. **Find $r^*$:** Solve $\sum_i c_i P(T, T_i, r^*) = K$ (root-finding)
2. **Compute strikes:** $K_i = P(T, T_i, r^*)$ for each cashflow
3. **Price each option:** Use zero-coupon bond option formula
4. **Sum:** Total price = $\sum_i c_i \cdot C_i$

### Example

A 5-year bond with annual coupons of 5% and principal of 100:
- Cashflows: $c_1 = 5, c_2 = 5, c_3 = 5, c_4 = 5, c_5 = 105$
- At times: $T_1 = 1, T_2 = 2, T_3 = 3, T_4 = 4, T_5 = 5$
- Option expiry: $T = 0.5$

Jamshidian decomposition converts this to 5 zero-coupon bond options.

---

## Put-Call Parity for Bond Options

### Zero-Coupon Bonds

$$
C(0) - P_{\text{put}}(0) = P(0, T_B) - K P(0, T)
$$

This is the forward price of the bond minus the discounted strike.

### Coupon Bonds

$$
C(0) - P_{\text{put}}(0) = B(0) - K P(0, T)
$$

where $B(0) = \sum_i c_i P(0, T_i)$ is the current bond price.

---

## Greeks for Bond Options

### Delta

Sensitivity to the underlying bond price:

$$
\Delta = \frac{\partial C}{\partial P(0, T_B)} = N(d_1)
$$

### Vega (Interest Rate)

Sensitivity to short-rate volatility:

$$
\mathcal{V} = \frac{\partial C}{\partial \sigma} = P(0, T_B) \phi(d_1) \frac{\partial \sigma_P}{\partial \sigma}
$$

where $\phi(\cdot)$ is the standard normal PDF.

### Theta

Time decay (computed numerically or via the pricing PDE).

### Rho (Kappa)

Sensitivity to mean-reversion parameter $\kappa$ requires differentiating through $B(\tau)$ and $\sigma_P$.

---

## Numerical Methods

### When Closed Forms Don't Apply

Numerical methods are needed for:
- American bond options (early exercise)
- Complex payoffs
- Non-affine models

### Finite Differences

Solve the bond option PDE:

$$
\frac{\partial V}{\partial t} + \mu^{\mathbb{Q}} \frac{\partial V}{\partial r} + \frac{1}{2}\sigma^2 \frac{\partial^2 V}{\partial r^2} - rV = 0
$$

with terminal condition $V(T, r) = (P(T, T_B, r) - K)^+$.

### Trees

Binomial or trinomial trees discretize the short rate and compute option values by backward induction.

### Monte Carlo

Simulate paths of $r_t$, compute bond prices at expiry, and average discounted payoffs:

$$
C(0) \approx \frac{1}{N} \sum_{i=1}^{N} e^{-\int_0^T r_t^{(i)} dt} (P(T, T_B, r_T^{(i)}) - K)^+
$$

---

## Connection to Caps and Floors

### Caplet as Bond Put

A caplet paying $\delta(L(T_1, T_2) - K)^+$ at $T_2$ can be rewritten as a put on a bond:

$$
\text{Caplet} = (1 + K\delta) \cdot \text{Put}(P(T_1, T_2), K_{\text{bond}})
$$

where $K_{\text{bond}} = 1/(1 + K\delta)$.

This connection allows caplet pricing using bond option formulas.

---

## Practical Considerations

### Calibration

Bond option prices are sensitive to:
- Volatility parameter $\sigma$
- Mean-reversion $\kappa$
- Initial yield curve (via discount factors)

### Market Quotes

Bond options are less liquid than caps/swaptions. Often, cap/floor and swaption implied volatilities are used to back out bond option prices.

### Model Risk

- One-factor models produce perfect correlation between bond prices
- Multi-factor models are needed for realistic joint distributions
- Smile/skew effects are absent in Gaussian models

---

## Key Takeaways

- Bond options are European options on zero-coupon or coupon bonds
- Vasicek/Hull-White: Closed-form prices via $C = P(0,T_B)N(d_1) - KP(0,T)N(d_2)$
- CIR: Non-central chi-squared formulas
- Jamshidian decomposition converts coupon bond options to portfolios of zero-coupon bond options
- Bond options are building blocks for caps, floors, and swaptions
- Greeks follow from differentiating the pricing formulas

---

## Further Reading

- Jamshidian (1989), "An Exact Bond Option Formula"
- Brigo & Mercurio, *Interest Rate Models*, Chapter 3
- Hull, *Options, Futures, and Other Derivatives*, Chapter 31

---

## Exercises

**Exercise 1.** In the Vasicek model, the price of a European call on a zero-coupon bond $P(t, T_B)$ with option maturity $T$ and strike $K$ is given by

$$
C = P(0, T_B)\,N(d_1) - K\,P(0, T)\,N(d_2)
$$

where $d_{1,2}$ depend on the integrated variance $v^2 = \sigma^2 B(T_B - T)^2(1 - e^{-2\kappa T})/(2\kappa)$ and $B(\tau) = (1 - e^{-\kappa\tau})/\kappa$. For $\sigma = 0.01$, $\kappa = 0.10$, $T = 2$, $T_B = 7$, $K = 0.82$, $P(0,2) = 0.94$, and $P(0,7) = 0.78$, compute the call option price.

??? success "Solution to Exercise 1"

    **Given:** $\sigma = 0.01$, $\kappa = 0.10$, $T = 2$, $T_B = 7$, $K = 0.82$, $P(0,2) = 0.94$, $P(0,7) = 0.78$.

    **Step 1: Compute $B(T_B - T)$.**

    $$
    B(T_B - T) = B(5) = \frac{1 - e^{-0.10 \times 5}}{0.10} = \frac{1 - e^{-0.5}}{0.10} = \frac{1 - 0.60653}{0.10} = \frac{0.39347}{0.10} = 3.9347
    $$

    **Step 2: Compute the bond price volatility $\sigma_P$.**

    $$
    \sigma_P = \sigma \cdot B(T_B - T) \cdot \sqrt{\frac{1 - e^{-2\kappa T}}{2\kappa}}
    $$

    $$
    = 0.01 \times 3.9347 \times \sqrt{\frac{1 - e^{-0.4}}{0.2}}
    $$

    $$
    = 0.039347 \times \sqrt{\frac{1 - 0.67032}{0.2}} = 0.039347 \times \sqrt{\frac{0.32968}{0.2}}
    $$

    $$
    = 0.039347 \times \sqrt{1.6484} = 0.039347 \times 1.28390 = 0.050520
    $$

    **Step 3: Compute $d_1$ and $d_2$.**

    $$
    d_1 = \frac{1}{\sigma_P}\ln\frac{P(0,T_B)}{K \cdot P(0,T)} + \frac{\sigma_P}{2}
    $$

    $$
    = \frac{1}{0.050520}\ln\frac{0.78}{0.82 \times 0.94} + \frac{0.050520}{2}
    $$

    $$
    = \frac{1}{0.050520}\ln\frac{0.78}{0.7708} + 0.025260
    $$

    $$
    = \frac{\ln(1.01193)}{0.050520} + 0.025260 = \frac{0.01186}{0.050520} + 0.025260
    $$

    $$
    = 0.23477 + 0.025260 = 0.26003
    $$

    $$
    d_2 = d_1 - \sigma_P = 0.26003 - 0.05052 = 0.20951
    $$

    **Step 4: Compute the call price.**

    $$
    N(0.26003) \approx 0.6026, \qquad N(0.20951) \approx 0.5830
    $$

    $$
    C = P(0,T_B)\,N(d_1) - K\,P(0,T)\,N(d_2)
    $$

    $$
    = 0.78 \times 0.6026 - 0.82 \times 0.94 \times 0.5830
    $$

    $$
    = 0.47003 - 0.7708 \times 0.5830 = 0.47003 - 0.44938 = 0.02065
    $$

    The call option price is approximately **\$0.0207** per unit of face value (or 2.07 cents per dollar of notional).

---

**Exercise 2.** Using put--call parity for bond options, derive the price of a European put on the same bond as in Exercise 1 with the same strike and maturity. Verify that $C - P = P(0, T_B) - K\,P(0, T)$.

??? success "Solution to Exercise 2"

    **Put-call parity for bond options:**

    $$
    C - P_{\text{put}} = P(0,T_B) - K\,P(0,T)
    $$

    From Exercise 1: $C = 0.02065$.

    $$
    P(0,T_B) - K\,P(0,T) = 0.78 - 0.82 \times 0.94 = 0.78 - 0.7708 = 0.0092
    $$

    Therefore:

    $$
    P_{\text{put}} = C - (P(0,T_B) - K\,P(0,T)) = 0.02065 - 0.0092 = 0.01145
    $$

    **Verification using the put formula:**

    $$
    P_{\text{put}} = K\,P(0,T)\,N(-d_2) - P(0,T_B)\,N(-d_1)
    $$

    $$
    = 0.7708 \times N(-0.20951) - 0.78 \times N(-0.26003)
    $$

    $$
    = 0.7708 \times 0.4170 - 0.78 \times 0.3974
    $$

    $$
    = 0.32142 - 0.30997 = 0.01145
    $$

    **Verification of parity:**

    $$
    C - P_{\text{put}} = 0.02065 - 0.01145 = 0.00920 = P(0,T_B) - K\,P(0,T) \checkmark
    $$

---

**Exercise 3.** Explain Jamshidian's decomposition for coupon bond options. A 3-year annual coupon bond pays coupons of 5% and par at maturity. An option to buy this bond in 1 year at strike $K_{\text{total}} = 100$ is decomposed into options on individual zero-coupon bonds. If the critical short rate $r^*$ at option expiry makes the bond worth exactly $K_{\text{total}}$, derive the individual strikes $K_j = P(T, T_j; r^*)$ for each coupon date.

??? success "Solution to Exercise 3"

    **Jamshidian's decomposition** exploits the key property of one-factor short-rate models: all bond prices $P(T, T_j, r)$ are **monotonically decreasing** in $r$ (since higher rates mean more discounting). Therefore, the coupon bond price $\sum_j c_j P(T, T_j, r)$ is also monotonically decreasing in $r$.

    **Setup:** A 3-year annual coupon bond with 5% coupons and par 100 has cashflows:

    - $c_1 = 5$ at $T_1 = T + 1$
    - $c_2 = 5$ at $T_2 = T + 2$
    - $c_3 = 105$ at $T_3 = T + 3$

    Option expiry is $T = 1$ year, with total strike $K_{\text{total}} = 100$.

    **Step 1: Find $r^*$.** The critical rate $r^*$ solves:

    $$
    5 \cdot P(1, 2; r^*) + 5 \cdot P(1, 3; r^*) + 105 \cdot P(1, 4; r^*) = 100
    $$

    This is a single nonlinear equation in $r^*$, solved by Newton's method or bisection. Since bond prices decrease in $r$, the left side is strictly decreasing in $r^*$, guaranteeing a unique solution.

    **Step 2: Compute individual strikes.** Once $r^*$ is found:

    $$
    K_1 = P(1, 2; r^*), \qquad K_2 = P(1, 3; r^*), \qquad K_3 = P(1, 4; r^*)
    $$

    Note that $5K_1 + 5K_2 + 105K_3 = 100$ by construction.

    **Step 3: Decomposition.** The call on the coupon bond decomposes as:

    $$
    \text{Call on coupon bond} = 5 \cdot C(P(1,2), K_1) + 5 \cdot C(P(1,3), K_2) + 105 \cdot C(P(1,4), K_3)
    $$

    Each $C(P(1,T_j), K_j)$ is a European call on a zero-coupon bond, priced using the standard Vasicek/Hull-White formula.

    **Why it works:** The coupon bond is in the money (worth more than $K$) precisely when $r_T < r^*$. In this region, each individual zero-coupon bond is worth more than $K_j$, so $\max(\text{coupon bond} - K, 0) = \sum_j c_j \max(P(T,T_j) - K_j, 0)$.

---

**Exercise 4.** In the CIR model, bond option pricing involves the non-central chi-squared distribution rather than the normal distribution. Explain why the CIR model cannot use the same Black-type formula as Vasicek, and describe qualitatively how the non-central chi-squared approach works. What is the main advantage of the CIR model for bond option pricing?

??? success "Solution to Exercise 4"

    **Why CIR cannot use the Black-type formula:**

    In the Vasicek model, $r_T$ is **Gaussian** given $r_0$. Since bond prices are exponential-affine in $r$, $\log P(T, T_B)$ is Gaussian, leading to a Black--Scholes-type formula with the normal CDF $N(\cdot)$.

    In the CIR model, $r_T$ follows a **non-central chi-squared** distribution (specifically, $r_T$ is proportional to a non-central $\chi^2$ random variable). Since $r_T$ is non-negative and positively skewed, $\log P(T, T_B) = \log A(\tau_B) - B(\tau_B) r_T$ is not Gaussian. The distribution is asymmetric and bounded on one side.

    Therefore, the Black-type formula (which relies on the normal distribution) does not apply. Instead, the call price involves the **non-central chi-squared CDF** $\chi^2(\cdot; \nu, \lambda)$:

    $$
    C(0) = P(0, T_B)\,\chi^2(x^*; \nu + 2, \lambda_1) - K\,P(0, T)\,\chi^2(x^*; \nu, \lambda_2)
    $$

    **How it works qualitatively:**

    1. The bond is in the money when $P(T, T_B) > K$, which translates to $r_T < r^*$ for a threshold $r^*$ determined by $A(\tau_B)e^{-B(\tau_B)r^*} = K$.
    2. Under the risk-neutral measure $\mathbb{Q}$ and the $T$-forward measure $\mathbb{Q}^T$, $r_T$ has (shifted) non-central chi-squared distributions with different non-centrality parameters $\lambda_1$ and $\lambda_2$.
    3. The two CDF terms correspond to the exercise probabilities under these two measures.

    **Main advantage of CIR:** The CIR model ensures $r_t \geq 0$ (under the Feller condition), which is economically desirable for nominal interest rates. The Vasicek model allows negative rates, which may be unrealistic in some contexts (though negative rates have been observed in practice). Additionally, the CIR model's volatility $\sigma\sqrt{r}$ scales with the rate level, producing a volatility smile.

---

**Exercise 5.** A one-factor short-rate model implies that all bond prices are perfectly correlated (all driven by a single factor). Explain how this affects the pricing of options on a portfolio of bonds versus options on individual bonds. For a spread option paying $\max(P(T, T_1) - P(T, T_2) - K, 0)$, why does a one-factor model underestimate the option value?

??? success "Solution to Exercise 5"

    In a one-factor model, all bond prices are driven by a single state variable $r_t$. This means:

    $$
    P(T, T_1) = f_1(r_T), \qquad P(T, T_2) = f_2(r_T)
    $$

    where $f_1, f_2$ are deterministic functions (both decreasing in $r$). Consequently, $P(T,T_1)$ and $P(T,T_2)$ are **perfectly (negatively) correlated** as functions of $r_T$ --- knowing one determines the other exactly.

    **Effect on portfolio options vs. individual options:**

    For options on individual bonds, the one-factor model gives reasonable prices because each option depends only on the marginal distribution of $r_T$.

    However, for a **spread option** $\max(P(T,T_1) - P(T,T_2) - K, 0)$, the value depends critically on the **joint distribution** of $P(T,T_1)$ and $P(T,T_2)$, and in particular on their correlation.

    **Why one-factor underestimates spread option value:**

    The spread $P(T,T_1) - P(T,T_2)$ in a one-factor model is a deterministic function of $r_T$: $g(r_T) = f_1(r_T) - f_2(r_T)$. Since both $f_1$ and $f_2$ are decreasing in $r$ (with $f_1$ less sensitive than $f_2$ if $T_1 < T_2$), the spread is a relatively tame function of a single variable.

    In reality, a two-factor model would allow the short end and long end to move somewhat independently. This creates scenarios where $P(T,T_1)$ increases while $P(T,T_2)$ decreases (curve steepening), making the spread $P(T,T_1) - P(T,T_2)$ much larger than in the one-factor case. The spread has **higher volatility** in a multi-factor model, so the option on the spread is worth more.

    Mathematically, with imperfect correlation $\rho < 1$:

    $$
    \text{Var}(P(T,T_1) - P(T,T_2)) = \text{Var}(P_1) + \text{Var}(P_2) - 2\rho\,\text{Std}(P_1)\text{Std}(P_2)
    $$

    When $\rho = 1$ (one-factor), this variance is minimized. When $\rho < 1$, the variance increases, increasing the spread option value.

---

**Exercise 6.** Compute the bond option delta $\Delta = \partial C / \partial P(0, T_B)$ and the bond option vega $\mathcal{V} = \partial C / \partial \sigma$ for the Vasicek bond option formula. Using the parameters from Exercise 1, evaluate these Greeks numerically and interpret their financial meaning.

??? success "Solution to Exercise 6"

    **Delta $\Delta = \partial C / \partial P(0, T_B)$:**

    Starting from $C = P(0,T_B)N(d_1) - KP(0,T)N(d_2)$, note that $d_1$ and $d_2$ depend on $P(0,T_B)$ through $\ln(P(0,T_B)/(KP(0,T)))$. Using the chain rule:

    $$
    \frac{\partial d_1}{\partial P(0,T_B)} = \frac{1}{\sigma_P \cdot P(0,T_B)}, \qquad \frac{\partial d_2}{\partial P(0,T_B)} = \frac{1}{\sigma_P \cdot P(0,T_B)}
    $$

    Differentiating $C$:

    $$
    \Delta = N(d_1) + P(0,T_B)\phi(d_1)\frac{\partial d_1}{\partial P(0,T_B)} - KP(0,T)\phi(d_2)\frac{\partial d_2}{\partial P(0,T_B)}
    $$

    Using the identity $P(0,T_B)\phi(d_1) = KP(0,T)\phi(d_2)$ (which follows from $d_2 = d_1 - \sigma_P$ and the lognormal structure), the last two terms cancel:

    $$
    \boxed{\Delta = N(d_1)}
    $$

    **Vega $\mathcal{V} = \partial C / \partial \sigma$:**

    Since $\sigma_P = \sigma \cdot B(T_B - T) \cdot \sqrt{(1 - e^{-2\kappa T})/(2\kappa)}$, we have $\partial\sigma_P/\partial\sigma = \sigma_P/\sigma$.

    Differentiating $C$ with respect to $\sigma$ (through $\sigma_P$):

    $$
    \mathcal{V} = P(0,T_B)\phi(d_1)\frac{\partial d_1}{\partial\sigma} - KP(0,T)\phi(d_2)\frac{\partial d_2}{\partial\sigma}
    $$

    Using the same identity and $\partial d_1/\partial\sigma_P = -d_2/\sigma_P$, $\partial d_2/\partial\sigma_P = -d_1/\sigma_P$ (standard Black--Scholes vega derivation), the result simplifies to:

    $$
    \mathcal{V} = P(0,T_B)\phi(d_1)\frac{\sigma_P}{\sigma}
    $$

    **Numerical evaluation** with parameters from Exercise 1 ($d_1 = 0.260$, $\sigma_P = 0.0505$, $\sigma = 0.01$):

    $$
    \Delta = N(0.260) \approx 0.603
    $$

    This means a \$0.01 increase in $P(0,7)$ increases the call value by approximately $0.603 \times 0.01 = \$0.00603$.

    $$
    \phi(0.260) = \frac{1}{\sqrt{2\pi}}e^{-0.260^2/2} = 0.3857
    $$

    $$
    \mathcal{V} = 0.78 \times 0.3857 \times \frac{0.0505}{0.01} = 0.78 \times 0.3857 \times 5.05 = 1.519
    $$

    **Interpretation:**

    - **Delta = 0.603:** The option has a 60.3% sensitivity to the underlying bond price. Since $d_1 > 0$, the option is slightly in the money. A \$1 increase in the bond price increases the option value by approximately \$0.603.
    - **Vega = 1.519:** A 1% (100 bp) increase in the short-rate volatility $\sigma$ increases the option price by approximately \$1.519 per unit face. More practically, a 1 bp increase in $\sigma$ increases the call by about \$0.01519. Vega is positive, confirming that higher volatility benefits option holders.
