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
