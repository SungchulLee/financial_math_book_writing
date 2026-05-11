# Bond and Derivative Pricing Classes Guide

The Hull-White model's affine structure means that zero-coupon bond prices, bond options, caps, floors, and swaptions all have closed-form or semi-closed-form expressions. This guide describes the pricing classes in the companion `bond_derivative_pricing_classes.py` module, mapping each method to its mathematical formula. The classes build on the `HullWhite` model class and its named functions ($A$, $B$, $\theta$) to compute prices and Greeks for the main interest rate derivatives.

!!! info "Prerequisites"

    - [Hull-White Model Class Guide](hull_white_model_class.md) (model class and named functions)
    - [Named Functions Implementation Guide](named_functions_implementation.md) ($A$, $B$, $\theta$ computation)
    - [Bond Price Formula](../bond_pricing/bond_price_formula.md) (derivation of $P = e^{A + Br}$)
    - [Caplet-Floorlet Formula](../derivatives_pricing/caplet_floorlet_formula.md) (caplet pricing theory)

!!! abstract "Learning Objectives"
    By the end of this guide, you will be able to:

    1. Compute zero-coupon bond prices using $P(t, T) = \exp(A(t,T) + B(t,T)\,r_t)$
    2. Price European bond options using the Hull-White closed-form formula
    3. Price caplets and floorlets via the bond option equivalence
    4. Price swaptions using the Jamshidian decomposition
    5. Understand the class hierarchy and how methods delegate to the model class

---

## Zero-Coupon Bond Pricing

### Formula

In the Hull-White model, the zero-coupon bond price is

$$
P(t, T) = \exp\bigl(A(t, T) + B(t, T)\,r_t\bigr)
$$

where $B(t, T) = -(1 - e^{-\lambda(T-t)})/\lambda$ and $A(t, T)$ is computed by numerical integration involving $\theta$.

### Implementation

```python
class BondPricer:
    def __init__(self, hw_model):
        self.hw = hw_model

    def zcb_price(self, t, T, r_t):
        A = self.hw.compute_A(T - t, T)
        B = self.hw.compute_B(T - t)
        return np.exp(A + B * r_t)
```

For time-0 pricing, the initial short rate $r_0$ is extracted from the market curve: $r_0 = -\ln P^M(0, \delta)/\delta$ for a small $\delta$.

---

## Bond Option Pricing

### European option on a zero-coupon bond

A European call option with strike $K$, expiry $T_0$, on a ZCB maturing at $T_1 > T_0$ has the closed-form price:

$$
C(0, T_0, T_1, K) = P(0, T_1)\,\mathcal{N}(d_1) - K\,P(0, T_0)\,\mathcal{N}(d_2)
$$

where

$$
d_1 = \frac{\ln\bigl(P(0, T_1)/(K\,P(0, T_0))\bigr)}{\sigma_P} + \frac{\sigma_P}{2}, \qquad d_2 = d_1 - \sigma_P
$$

and the bond price volatility is

$$
\sigma_P = \frac{\sigma}{\lambda}(1 - e^{-\lambda(T_1 - T_0)})\sqrt{\frac{1 - e^{-2\lambda T_0}}{2\lambda}}
$$

### Implementation

```python
def bond_option(self, T0, T1, K, r0, option_type='call'):
    P_T0 = self.zcb_price(0, T0, r0)
    P_T1 = self.zcb_price(0, T1, r0)
    sigma_P = (self.hw.sigma / self.hw.lambd) * (1 - np.exp(-self.hw.lambd * (T1 - T0))) \
              * np.sqrt((1 - np.exp(-2 * self.hw.lambd * T0)) / (2 * self.hw.lambd))
    d1 = np.log(P_T1 / (K * P_T0)) / sigma_P + sigma_P / 2
    d2 = d1 - sigma_P
    if option_type == 'call':
        return P_T1 * norm.cdf(d1) - K * P_T0 * norm.cdf(d2)
    else:
        return K * P_T0 * norm.cdf(-d2) - P_T1 * norm.cdf(-d1)
```

---

## Caplet and Floorlet Pricing

### Bond option equivalence

A caplet with reset $T_i$, payment $T_{i+1} = T_i + \delta$, and strike $K$ is equivalent to a put option on a zero-coupon bond:

$$
\text{Caplet}(T_i, T_{i+1}, K) = (1 + K\delta)\;\text{Put}\!\left(T_i, T_{i+1}, \frac{1}{1 + K\delta}\right)
$$

This identity converts caplet pricing to bond option pricing, which has the closed-form formula above.

### Implementation

```python
def caplet(self, T_i, delta, K, r0):
    bond_strike = 1.0 / (1.0 + K * delta)
    return (1 + K * delta) * self.bond_option(T_i, T_i + delta, bond_strike, r0, 'put')

def cap(self, reset_dates, delta, K, r0):
    return sum(self.caplet(T_i, delta, K, r0) for T_i in reset_dates)
```

Floorlets are analogous, using call options on the bond.

---

## Swaption Pricing

### Jamshidian decomposition

A European payer swaption with expiry $T_0$ on a swap with fixed rate $K$ and payment dates $T_1, \ldots, T_n$ decomposes into a portfolio of bond options. The key insight: at expiry $T_0$, the swap value is a sum of bond prices, and since bond prices are monotone in $r_{T_0}$, there exists a critical rate $r^*$ at which the swap is exactly at the money.

**Step 1.** Find $r^*$ solving:

$$
\sum_{i=1}^n c_i\,P(T_0, T_i; r^*) = 1
$$

where $c_i = K\delta$ for $i < n$ and $c_n = 1 + K\delta$.

**Step 2.** The swaption price is:

$$
\text{Swaption} = \sum_{i=1}^n c_i\;\text{Put}\!\left(T_0, T_i, P(T_0, T_i; r^*)\right)
$$

### Implementation

```python
def swaption(self, T0, payment_dates, K, delta, r0):
    n = len(payment_dates)
    coupons = [K * delta] * (n - 1) + [1 + K * delta]

    # Step 1: find r* by root-finding
    def swap_value(r_star):
        return sum(c * self.zcb_price(T0, T_i, r_star)
                   for c, T_i in zip(coupons, payment_dates)) - 1.0
    r_star = brentq(swap_value, -0.1, 0.5)

    # Step 2: sum of bond puts
    strikes = [self.zcb_price(T0, T_i, r_star) for T_i in payment_dates]
    return sum(c * self.bond_option(T0, T_i, Ki, r0, 'put')
               for c, T_i, Ki in zip(coupons, payment_dates, strikes))
```

!!! tip "Receiver Swaptions"
    For a receiver swaption, replace puts with calls in the decomposition. The Jamshidian trick works because all bond prices are monotonically decreasing in $r$, which is guaranteed by the one-factor structure.

---

## Summary

| Derivative | Method | Mathematical basis |
|-----------|--------|-------------------|
| ZCB | `zcb_price` | $P = e^{A + Br}$ |
| Bond option | `bond_option` | Black-Scholes-like with $\sigma_P$ |
| Caplet/floorlet | `caplet` / `floorlet` | Bond option equivalence |
| Cap/floor | `cap` / `floor` | Sum of caplets/floorlets |
| Swaption | `swaption` | Jamshidian decomposition |

For the tree-based and Monte Carlo pricing engines (used for path-dependent derivatives), see [Tree and Monte Carlo Engines Guide](tree_and_monte_carlo_engines.md). For the calibration pipeline that uses these pricing classes, see [Calibration Pipeline Guide](calibration_pipeline.md).

---

## Exercises

**Exercise 1.** Using the `BondPricer` class with Hull-White parameters $\sigma = 0.01$, $\lambda = 0.05$, and a flat market curve at 3\%, compute $B(0, 10)$ and $A(0, 10)$. Verify that the model zero-coupon bond price $P^{\text{HW}}(0, 10)$ matches $e^{-0.03 \times 10}$ to within the numerical tolerance of the trapezoidal integration.

??? success "Solution to Exercise 1"
    With $\sigma = 0.01$, $\lambda = 0.05$, flat curve at 3%, and $r_0 = 0.03$:

    $$
    B(0, 10) = B(10) = -\frac{1 - e^{-0.05 \times 10}}{0.05} = -\frac{1 - e^{-0.5}}{0.05} = -\frac{1 - 0.60653}{0.05} = -\frac{0.39347}{0.05} = -7.8694
    $$

    For the flat curve, $\theta(t) = r + \frac{\sigma^2}{2\lambda^2}(1 - e^{-2\lambda t})$. The function $A(0, 10)$ is computed by numerical integration:

    $$
    A(10) = -\frac{\sigma^2}{4\lambda^3}(3 - 2\lambda \cdot 10 - 4e^{-0.5} + e^{-1.0}) + \lambda\int_0^{10}\theta(10 - \tau')B(\tau')\,d\tau'
    $$

    The analytical part evaluates to:

    $$
    -\frac{(0.01)^2}{4(0.05)^3}(3 - 1.0 - 4 \times 0.60653 + 0.36788) = -0.2(3 - 1 - 2.42612 + 0.36788) = -0.2 \times (-0.05824) = 0.01165
    $$

    The model bond price should satisfy the recovery condition:

    $$
    P^{\text{HW}}(0, 10) = \exp(A(10) + B(10) \times 0.03)
    $$

    Since $\theta(t)$ is calibrated to match the market curve, this must equal:

    $$
    P^M(0, 10) = e^{-0.03 \times 10} = e^{-0.3} = 0.74082
    $$

    The numerical integration with 250 grid points introduces errors of order $10^{-6}$, so the match should hold to at least 5 significant figures: $|P^{\text{HW}} - P^M|/P^M < 10^{-5}$.

---

**Exercise 2.** The bond price volatility $\sigma_P$ is given by

$$
\sigma_P = \frac{\sigma}{\lambda}(1 - e^{-\lambda(T_1 - T_0)})\sqrt{\frac{1 - e^{-2\lambda T_0}}{2\lambda}}
$$

Compute $\sigma_P$ for a bond option with $T_0 = 2$, $T_1 = 5$, $\sigma = 0.015$, $\lambda = 0.03$. Explain why $\sigma_P$ increases with $T_1 - T_0$ but eventually saturates.

??? success "Solution to Exercise 2"
    With $T_0 = 2$, $T_1 = 5$, $\sigma = 0.015$, $\lambda = 0.03$:

    $$
    \sigma_P = \frac{0.015}{0.03}(1 - e^{-0.03 \times 3})\sqrt{\frac{1 - e^{-2 \times 0.03 \times 2}}{2 \times 0.03}}
    $$

    $$
    = 0.5 \times (1 - e^{-0.09}) \times \sqrt{\frac{1 - e^{-0.12}}{0.06}}
    $$

    $$
    = 0.5 \times 0.08607 \times \sqrt{\frac{0.11308}{0.06}}
    $$

    $$
    = 0.04303 \times \sqrt{1.88467} = 0.04303 \times 1.37282 = 0.05908
    $$

    **Why $\sigma_P$ increases with $T_1 - T_0$:** The factor $(1 - e^{-\lambda(T_1 - T_0)})$ increases as $T_1 - T_0$ grows. A longer-maturity bond has greater price sensitivity to the short rate (larger $|B|$), so its volatility is higher.

    **Why it saturates:** As $T_1 - T_0 \to \infty$, $e^{-\lambda(T_1 - T_0)} \to 0$ and $(1 - e^{-\lambda(T_1 - T_0)}) \to 1$. The saturation occurs because mean reversion limits the bond's sensitivity: $B(t, T) \to -1/\lambda$ as $T - t \to \infty$. Beyond the mean-reversion horizon $1/\lambda$, extending the bond maturity adds no further rate sensitivity, so $\sigma_P$ plateaus at $\frac{\sigma}{\lambda}\sqrt{\frac{1 - e^{-2\lambda T_0}}{2\lambda}}$.

---

**Exercise 3.** Verify the caplet-bond-put equivalence numerically. Using parameters $\sigma = 0.01$, $\lambda = 0.05$, $r_0 = 0.03$, flat curve at 3\%, price a caplet with $T_i = 1$, $\delta = 0.5$, $K = 3\%$ by: (a) calling `caplet(T_i, delta, K, r0)`, and (b) manually computing $(1 + K\delta) \times \text{Put}(T_i, T_i + \delta, 1/(1+K\delta))$. Confirm the two approaches give identical results.

??? success "Solution to Exercise 3"
    Parameters: $\sigma = 0.01$, $\lambda = 0.05$, $r_0 = 0.03$, flat curve at 3%, $T_i = 1$, $\delta = 0.5$, $K = 0.03$.

    **(a) Using the caplet method:** `caplet(1, 0.5, 0.03, 0.03)` internally computes the bond strike $K_B = 1/(1 + 0.03 \times 0.5) = 1/1.015 = 0.98522$ and calls the bond put with $T_0 = 1$, $T_1 = 1.5$, strike $K_B = 0.98522$, then multiplies by $(1 + K\delta) = 1.015$.

    **(b) Manual computation:** The bond put price uses the formula with:

    $$
    \sigma_P = \frac{0.01}{0.05}(1 - e^{-0.05 \times 0.5})\sqrt{\frac{1 - e^{-0.1}}{0.1}}
    $$

    $$
    = 0.2 \times (1 - e^{-0.025}) \times \sqrt{\frac{0.09516}{0.1}} = 0.2 \times 0.02469 \times \sqrt{0.9516}
    $$

    $$
    = 0.004938 \times 0.97549 = 0.004817
    $$

    Then:

    $$
    P(0, 1) = e^{-0.03} = 0.97045, \qquad P(0, 1.5) = e^{-0.045} = 0.95600
    $$

    $$
    d_1 = \frac{\ln(P(0,1.5)/(K_B \cdot P(0,1)))}{\sigma_P} + \frac{\sigma_P}{2} = \frac{\ln(0.95600/(0.98522 \times 0.97045))}{0.004817} + 0.002409
    $$

    $$
    = \frac{\ln(0.95600/0.95612)}{0.004817} + 0.002409 = \frac{-0.0000126}{0.004817} + 0.002409 \approx -0.00262 + 0.00241 = -0.00021
    $$

    The caplet price is $(1 + K\delta) \times \text{Put}(1, 1.5, K_B)$. Both approaches (a) and (b) give identical results because the caplet method is simply a wrapper that performs exactly this bond-put computation internally.

---

**Exercise 4.** In the Jamshidian swaption decomposition, explain why the critical rate $r^*$ exists and is unique. For a payer swaption with $T_0 = 1$, annual payments at $T_1 = 2, T_2 = 3$, and $K = 4\%$, write down the equation for $r^*$ explicitly in terms of the Hull-White bond price formula. What happens to $r^*$ if $K$ is very large? Very small?

??? success "Solution to Exercise 4"
    **Existence and uniqueness of $r^*$:** In the one-factor Hull-White model, the bond price $P(T_0, T_i; r) = \exp(A(T_0, T_i) + B(T_0, T_i) \cdot r)$ is a strictly decreasing function of $r$ (since $B(T_0, T_i) < 0$ for $T_i > T_0$). Therefore the swap value at $T_0$:

    $$
    S(r) = \sum_{i=1}^n c_i P(T_0, T_i; r) - 1
    $$

    is a sum of strictly decreasing exponentials minus 1, hence strictly decreasing in $r$. Since $S(r) \to +\infty$ as $r \to -\infty$ and $S(r) \to -1$ as $r \to +\infty$, by the intermediate value theorem there exists exactly one $r^*$ solving $S(r^*) = 0$.

    For the specific case $T_0 = 1$, $T_1 = 2$, $T_2 = 3$, $K = 4\%$, $\delta = 1$:

    - $c_1 = K\delta = 0.04$
    - $c_2 = 1 + K\delta = 1.04$

    The equation for $r^*$ is:

    $$
    0.04 \cdot \exp(A(1,2) + B(1,2) \cdot r^*) + 1.04 \cdot \exp(A(1,3) + B(1,3) \cdot r^*) = 1
    $$

    If $K$ is very large, the coupon payments dominate, and the sum $S(r)$ is large even for moderate $r$, so $r^*$ must be very large to bring the bond prices down enough. If $K$ is very small (close to zero), the swap is essentially a zero-coupon instrument and $r^*$ satisfies $P(T_0, T_n; r^*) \approx 1$, which means $r^* \approx 0$ (or the rate implied by $A(T_0, T_n) + B(T_0, T_n) \cdot r^* = 0$).

---

**Exercise 5.** Using the `bond_option` method, compute the price of a European call on a 5-year ZCB with strike $K = 0.85$, option expiry $T_0 = 2$, and parameters $\sigma = 0.01$, $\lambda = 0.05$, flat curve at 3\%. Then compute the corresponding put price using put-call parity: Put $=$ Call $- P(0, 5) + K \cdot P(0, 2)$. Verify that the direct put formula gives the same answer.

??? success "Solution to Exercise 5"
    Parameters: $\sigma = 0.01$, $\lambda = 0.05$, flat curve at 3%, $T_0 = 2$, $T_1 = 5$, $K = 0.85$.

    Bond prices: $P(0, 2) = e^{-0.06} = 0.94176$, $P(0, 5) = e^{-0.15} = 0.86071$.

    Bond price volatility:

    $$
    \sigma_P = \frac{0.01}{0.05}(1 - e^{-0.05 \times 3})\sqrt{\frac{1 - e^{-0.2}}{0.1}} = 0.2 \times 0.13929 \times 1.34640 = 0.03751
    $$

    Call option:

    $$
    d_1 = \frac{\ln(0.86071/(0.85 \times 0.94176))}{0.03751} + \frac{0.03751}{2} = \frac{\ln(0.86071/0.80050)}{0.03751} + 0.01876
    $$

    $$
    = \frac{\ln(1.07521)}{0.03751} + 0.01876 = \frac{0.07247}{0.03751} + 0.01876 = 1.93228 + 0.01876 = 1.95104
    $$

    $$
    d_2 = 1.95104 - 0.03751 = 1.91353
    $$

    $$
    C = 0.86071 \times \Phi(1.95104) - 0.85 \times 0.94176 \times \Phi(1.91353)
    $$

    $$
    = 0.86071 \times 0.97445 - 0.80050 \times 0.97219 = 0.83872 - 0.77824 = 0.06048
    $$

    **Put-call parity:**

    $$
    \text{Put} = C - P(0, 5) + K \cdot P(0, 2) = 0.06048 - 0.86071 + 0.85 \times 0.94176
    $$

    $$
    = 0.06048 - 0.86071 + 0.80050 = 0.00027
    $$

    The put is very small because the strike $K = 0.85$ is well below the forward bond price $P(0, 5)/P(0, 2) = 0.86071/0.94176 = 0.91397$. The direct put formula from `bond_option(..., 'put')` should return the same value $\approx 0.00027$.

---

**Exercise 6.** Price a 5-year cap (annual resets, $\delta = 1$, $K = 3\%$) using the Hull-White model with $\sigma = 0.01$, $\lambda = 0.05$, flat curve at 3\%. Decompose the cap price into individual caplet contributions. Which caplet is most expensive, and why? How does the answer change if $\lambda$ is increased to 0.20?

??? success "Solution to Exercise 6"
    A 5-year cap with annual resets ($\delta = 1$, $K = 3\%$) consists of 4 caplets (the first reset at $T_0 = 1$ pays at $T_1 = 2$, and so on through $T_3 = 4$ paying at $T_4 = 5$).

    Each caplet uses the bond-put equivalence: Caplet$(T_i, T_{i+1}, K) = (1 + K\delta) \times \text{Put}(T_i, T_{i+1}, 1/(1+K\delta))$.

    With $K_B = 1/1.03 = 0.97087$, and $(1 + K\delta) = 1.03$:

    The bond price volatility for caplet $i$ (reset $T_i$, payment $T_i + 1$):

    $$
    \sigma_{P,i} = \frac{0.01}{0.05}(1 - e^{-0.05}) \sqrt{\frac{1 - e^{-0.1 T_i}}{0.1}}
    $$

    $$
    = 0.2 \times 0.04877 \times \sqrt{\frac{1 - e^{-0.1 T_i}}{0.1}}
    $$

    Since $\sigma_{P,i}$ increases with $T_i$ (through the $\sqrt{(1 - e^{-0.1T_i})/0.1}$ factor), later caplets have higher bond volatility and therefore higher option value.

    Approximate caplet prices (in basis points of notional):

    | Caplet | Reset $T_i$ | $\sigma_{P,i}$ | Price (bps) |
    |--------|------------|----------------|-------------|
    | 1 | 1 | 0.00300 | $\sim$ 1.2 |
    | 2 | 2 | 0.00419 | $\sim$ 1.7 |
    | 3 | 3 | 0.00507 | $\sim$ 2.0 |
    | 4 | 4 | 0.00573 | $\sim$ 2.3 |

    The last caplet (reset at $T = 4$) is the most expensive because it has the highest bond volatility $\sigma_{P,4}$. This is because the longer the time to reset, the more uncertainty accumulates in the short rate (the $\sqrt{(1-e^{-2\lambda T_i})/(2\lambda)}$ factor grows with $T_i$), making the option more valuable.

    **Effect of increasing $\lambda$ to 0.20:** Higher mean reversion has two effects:

    1. The factor $(1 - e^{-\lambda})$ decreases slightly (bond sensitivity per unit tenor shrinks).
    2. The saturation of $\sqrt{(1 - e^{-2\lambda T_i})/(2\lambda)}$ occurs faster, so the differences between caplet prices narrow.

    The overall cap price decreases because stronger mean reversion reduces rate volatility at longer horizons. The most expensive caplet may shift to an earlier reset because the volatility benefit of later resets is diminished by the faster mean reversion.
