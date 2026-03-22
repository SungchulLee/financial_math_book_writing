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
C(0, T_0, T_1, K) = P(0, T_1)\,\Phi(d_1) - K\,P(0, T_0)\,\Phi(d_2)
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
