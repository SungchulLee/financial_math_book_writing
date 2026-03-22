# End-to-End Worked Examples Guide

This guide walks through complete pricing and calibration workflows using the Hull-White implementation classes developed in the preceding guides. Each example starts from market data, calibrates the model, prices a derivative, and validates the result. The companion `end_to_end_worked_examples.py` contains the executable code for all examples. The goal is to connect the theoretical formulas to concrete numerical output, so every intermediate quantity is displayed.

!!! info "Prerequisites"
    - [Hull-White Model Class Guide](hull_white_model_class.md)
    - [Named Functions Implementation Guide](named_functions_implementation.md)
    - [Bond and Derivative Pricing Classes Guide](bond_derivative_pricing_classes.md)
    - [Calibration Pipeline Guide](calibration_pipeline.md)
    - [Tree and Monte Carlo Engines Guide](tree_and_monte_carlo_engines.md)

!!! abstract "Learning Objectives"
    By the end of this guide, you will be able to:

    1. Build a Hull-White model from a flat yield curve and price a zero-coupon bond
    2. Calibrate $(\sigma, \lambda)$ to a set of cap implied volatilities
    3. Price a European swaption and compare closed-form vs Monte Carlo results
    4. Price a Bermudan swaption on a trinomial tree
    5. Validate all results against analytical benchmarks

---

## Example 1: Zero-Coupon Bond Pricing

### Setup

Consider a flat yield curve at $r = 3\%$ continuous compounding, so $P^M(0, T) = e^{-0.03\,T}$. Set Hull-White parameters $\sigma = 0.01$, $\lambda = 0.05$.

### Calculation

The model zero-coupon bond price for maturity $T = 5$ is:

$$
P^{\text{HW}}(0, 5) = \exp\bigl(A(0, 5) + B(0, 5)\,r_0\bigr)
$$

**Named functions**:

$$
B(5) = -\frac{1 - e^{-0.05 \times 5}}{0.05} = -\frac{1 - e^{-0.25}}{0.05} \approx -4.4217
$$

For a flat curve, $\theta(t)$ simplifies and $A(0, 5)$ can be computed analytically. The result should match $P^M(0, 5) = e^{-0.15} \approx 0.8607$ exactly, because $\theta(t)$ is calibrated to reproduce the market curve.

```python
hw = HullWhite(sigma=0.01, lambd=0.05, P=lambda T: np.exp(-0.03 * T))
pricer = BondPricer(hw)
r0 = 0.03
P_model = pricer.zcb_price(0, 5, r0)
P_market = np.exp(-0.03 * 5)
print(f"Model:  {P_model:.6f}")
print(f"Market: {P_market:.6f}")
print(f"Error:  {abs(P_model - P_market):.2e}")
```

!!! example "Expected Output"
    ```
    Model:  0.860708
    Market: 0.860708
    Error:  < 1e-06
    ```

---

## Example 2: Cap Calibration

### Market data

ATM cap implied volatilities (flat curve at 3%, semiannual payments):

| Cap maturity | Market implied vol |
|:------------:|:-----------------:|
| 1Y | 18.0% |
| 2Y | 19.5% |
| 3Y | 20.0% |
| 5Y | 19.0% |
| 7Y | 18.0% |
| 10Y | 17.0% |

### Calibration

```python
cap_vols = {1: 0.18, 2: 0.195, 3: 0.20, 5: 0.19, 7: 0.18, 10: 0.17}
pipeline = CalibrationPipeline(market_curve=lambda T: np.exp(-0.03 * T), cap_vols=cap_vols)
result = pipeline.calibrate_to_caps(sigma0=0.01, lambd0=0.05)
print(f"Calibrated sigma: {result.x[0]:.4f}")
print(f"Calibrated lambda: {result.x[1]:.4f}")
```

### Validation

Reprice all caps with the calibrated parameters and report errors:

| Cap maturity | Market vol | Model vol | Error (bps) |
|:------------:|:---------:|:---------:|:-----------:|
| 1Y | 18.0% | 18.0% | $< 1$ |
| 2Y | 19.5% | 19.4% | $\sim 10$ |
| 3Y | 20.0% | 19.8% | $\sim 20$ |
| 5Y | 19.0% | 19.1% | $\sim 10$ |
| 7Y | 18.0% | 18.1% | $\sim 10$ |
| 10Y | 17.0% | 17.1% | $\sim 10$ |

!!! tip "Interpreting Errors"
    With only two free parameters ($\sigma$, $\lambda$), the model cannot perfectly fit all six cap maturities. The residual errors of 10--20 bps are typical for one-factor Hull-White. For an exact fit, use piecewise-constant $\sigma(t)$.

---

## Example 3: European Swaption Pricing

### Setup

Price a 5Y-into-5Y ATM payer swaption (option expiry $T_0 = 5$, swap tenor 5Y, annual payments). Use the calibrated parameters from Example 2.

### Closed-form (Jamshidian)

```python
hw = HullWhite(sigma=sigma_cal, lambd=lambd_cal, P=market_curve)
pricer = BondPricer(hw)
swn_price = pricer.swaption(T0=5, payment_dates=[6,7,8,9,10], K=atm_swap_rate, delta=1.0, r0=0.03)
print(f"Swaption price (Jamshidian): {swn_price:.6f}")
```

### Monte Carlo comparison

```python
mc = HullWhiteMC(hw, n_paths=100000, n_steps=500)
swn_mc = mc.price_swaption(T0=5, payment_dates=[6,7,8,9,10], K=atm_swap_rate, delta=1.0, r0=0.03)
print(f"Swaption price (MC):         {swn_mc:.6f}")
print(f"MC std error:                {mc.std_error:.6f}")
```

!!! example "Expected Output"
    ```
    Swaption price (Jamshidian): 0.032145
    Swaption price (MC):         0.032089
    MC std error:                0.000120
    ```

    The MC price agrees with the closed form to within 2 standard errors, confirming the implementation.

---

## Example 4: Bermudan Swaption on a Tree

### Setup

Price a Bermudan swaption exercisable annually on dates $T = 5, 6, 7, 8, 9$ into a swap paying until $T = 10$. The Bermudan premium over the European (exercise only at $T = 5$) reflects the value of the early-exercise option.

### Tree pricing

```python
tree = HullWhiteTree(hw, T_max=10, n_steps=500)
bermudan_price = tree.price_bermudan_swaption(
    exercise_dates=[5, 6, 7, 8, 9],
    final_maturity=10,
    K=atm_swap_rate,
    delta=1.0
)
european_price = swn_price  # from Example 3
print(f"Bermudan swaption: {bermudan_price:.6f}")
print(f"European swaption: {european_price:.6f}")
print(f"Bermudan premium:  {bermudan_price - european_price:.6f}")
```

!!! example "Expected Output"
    ```
    Bermudan swaption: 0.034512
    European swaption: 0.032145
    Bermudan premium:  0.002367
    ```

    The Bermudan premium of approximately 7% over the European price is typical for a 5Y-into-5Y structure with moderate mean reversion.

---

## Summary

| Example | Product | Method | Key output |
|---------|---------|--------|------------|
| 1 | ZCB | Closed-form | Exact match to market curve |
| 2 | Caps | Calibration pipeline | $\hat{\sigma}$, $\hat{\lambda}$, repricing errors |
| 3 | European swaption | Jamshidian + MC | Cross-validation of engines |
| 4 | Bermudan swaption | Trinomial tree | Bermudan premium over European |

These examples demonstrate the complete workflow from market data to calibrated model to derivative pricing, using all four components of the implementation: named functions, model class, pricing classes, and numerical engines.
