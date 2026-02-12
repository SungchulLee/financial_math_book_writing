# Interpolation Methods for Yield Curves

Bootstrapping produces discount factors at discrete maturities corresponding to market instruments. **Interpolation** extends the curve to arbitrary maturities, enabling pricing of instruments with non-standard dates. The choice of interpolation method significantly affects forward rates and hedging behavior.

---

## The Interpolation Problem

### Given

A set of bootstrapped points:

$$
\{(T_1, P_1), (T_2, P_2), \ldots, (T_n, P_n)\}
$$

where $P_i = P(0, T_i)$ are discount factors at maturities $T_i$.

### Required

A continuous function $P(0, T)$ for all $T \in [0, T_n]$ that:
1. Passes through all given points: $P(0, T_i) = P_i$
2. Produces sensible forward rates
3. Is stable under small perturbations of inputs
4. Supports efficient computation

---

## Interpolation on Different Variables

The choice of **what to interpolate** matters as much as **how to interpolate**.

### Option 1: Interpolate Discount Factors

$$
P(0, T) = \text{Interp}\{(T_i, P_i)\}
$$

- Direct but can violate positivity
- Forward rates derived via differentiation

### Option 2: Interpolate Log-Discount Factors

$$
\log P(0, T) = \text{Interp}\{(T_i, \log P_i)\}
$$

- Ensures positivity: $P(0, T) = e^{\text{Interp}(\cdot)} > 0$
- Linear interpolation here = linear on zero rates

### Option 3: Interpolate Zero Rates

$$
z(0, T) = \text{Interp}\{(T_i, z_i)\}
$$

where $z_i = -\log(P_i)/T_i$

- Intuitive for yield curve analysis
- Recover discount factors: $P(0, T) = e^{-z(0,T) \cdot T}$

### Option 4: Interpolate Forward Rates

$$
f(0, T) = \text{Interp}\{(T_i, f_i)\}
$$

- Direct control over forward curve shape
- Recover discount factors: $P(0, T) = e^{-\int_0^T f(0,u) du}$

---

## Linear Interpolation

### On Zero Rates

For $T \in [T_i, T_{i+1}]$:

$$
z(0, T) = z_i + \frac{T - T_i}{T_{i+1} - T_i}(z_{i+1} - z_i)
$$

**Forward rate:**

$$
f(0, T) = z(0, T) + T \frac{\partial z}{\partial T} = z_i + \frac{T - T_i}{T_{i+1} - T_i}(z_{i+1} - z_i) + T \cdot \frac{z_{i+1} - z_i}{T_{i+1} - T_i}
$$

Simplifying:

$$
f(0, T) = z_{i+1} + \frac{T_i(z_{i+1} - z_i)}{T_{i+1} - T_i}
$$

The forward rate is **constant** within each interval (piecewise flat forwards).

### On Log-Discounts

For $T \in [T_i, T_{i+1}]$:

$$
\log P(0, T) = \log P_i + \frac{T - T_i}{T_{i+1} - T_i}(\log P_{i+1} - \log P_i)
$$

**Forward rate:**

$$
f(0, T) = -\frac{\partial}{\partial T} \log P(0, T) = \frac{\log P_i - \log P_{i+1}}{T_{i+1} - T_i}
$$

This is **piecewise constant**, with jumps at the nodes $T_i$.

### Properties

| Aspect | Linear on Zero Rates | Linear on Log-Discounts |
|--------|---------------------|------------------------|
| Zero curve | Continuous, piecewise linear | Continuous, piecewise linear |
| Forward curve | Continuous, piecewise linear | Discontinuous (jumps at nodes) |
| Simplicity | High | High |
| Hedging stability | Moderate | Poor near nodes |

---

## Cubic Spline Interpolation

### Natural Cubic Spline

A **cubic spline** fits a piecewise cubic polynomial with continuous first and second derivatives.

For $T \in [T_i, T_{i+1}]$:

$$
z(0, T) = a_i + b_i(T - T_i) + c_i(T - T_i)^2 + d_i(T - T_i)^3
$$

subject to:
- Interpolation: $z(0, T_i) = z_i$
- Continuity of $z, z', z''$ at interior nodes
- Natural boundary: $z''(T_1) = z''(T_n) = 0$

### Forward Rate from Cubic Spline

$$
f(0, T) = z(0, T) + T \cdot z'(0, T)
$$

The forward rate is a **quadratic** function within each interval, ensuring smoothness.

### Potential Issues

**Oscillation:** Cubic splines can overshoot between nodes, potentially producing:
- Negative forward rates
- Non-monotonic forwards where monotonicity is expected
- Artifacts near endpoints

**Example of Oscillation:**

If the zero curve has a kink, the cubic spline may introduce "wiggles" in the forward curve.

---

## Monotone Convex Interpolation

### Motivation

Developed by Hagan & West (2006) to address:
- Negative forward rates from naive methods
- Oscillation in forward curves
- Need for local control

### Key Properties

1. **Positivity:** Forward rates are guaranteed positive
2. **Monotonicity:** If inputs are monotone, so is the interpolant
3. **Locality:** Changes at one node affect only adjacent intervals
4. **Continuity:** Forward rates are continuous

### Algorithm Overview

The method interpolates the **integral of the forward rate**:

$$
g(T) = \int_0^T f(0, u) du = -\log P(0, T)
$$

such that:
1. $g(T_i) = -\log P_i$ (matches data)
2. $g'(T) = f(0, T) > 0$ (positive forwards)
3. $g'(T)$ is monotone within each interval (no oscillation)

### Implementation Sketch

For each interval $[T_i, T_{i+1}]$:

1. Compute discrete forward rate:
$$
f_i^{\text{disc}} = \frac{g(T_{i+1}) - g(T_i)}{T_{i+1} - T_i}
$$

2. Choose instantaneous forwards $f(T_i^+)$ and $f(T_{i+1}^-)$ to ensure monotonicity

3. Fit a quadratic or rational function that:
   - Matches values at endpoints
   - Has the correct derivatives
   - Remains positive

---

## Comparison of Methods

### Test Case: Humped Yield Curve

Consider a curve that rises then falls (humped shape).

| Method | Zero Curve | Forward Curve | Artifacts |
|--------|------------|---------------|-----------|
| Linear (zero) | Piecewise linear | Continuous, may be negative | None |
| Linear (log-disc) | Piecewise linear | Piecewise constant, jumps | Step discontinuities |
| Cubic spline | Smooth | Smooth but may oscillate | Possible negative forwards |
| Monotone convex | Smooth | Smooth, positive, controlled | None |

### Visual Intuition

```
Zero Rate:
       *-------*
      /         \
     *           *
    /             \
---*               *---

Forward Rate (various methods):

Linear (log-disc):    |---|   |---|   |---|   (steps)
Cubic spline:        ~~~*~~~*~~~*~~~           (smooth but may dip below zero)
Monotone convex:     ---*---*---*---           (smooth, positive, controlled)
```

---

## Impact on Hedging

### Bucket Sensitivities

The sensitivity of a portfolio to a parallel shift in rate $i$ depends on the interpolation:

$$
\frac{\partial V}{\partial z_i} = \sum_j \frac{\partial V}{\partial P(0, T_j)} \cdot \frac{\partial P(0, T_j)}{\partial z_i}
$$

The term $\frac{\partial P(0, T_j)}{\partial z_i}$ depends on interpolation.

### Local vs. Global Methods

**Local methods** (linear, monotone convex):
- $\frac{\partial P(0, T_j)}{\partial z_i} = 0$ unless $T_j$ is near $T_i$
- Sparse Jacobian, cleaner hedges

**Global methods** (cubic spline):
- All rates can affect all maturities
- Dense Jacobian, complicated hedges

### Hedging Stability

Linear interpolation on log-discounts creates **discontinuities** in forward rates at nodes. This leads to:
- Hedge ratios that jump as instruments approach node dates
- Difficulty in attributing P&L to rate moves

Smoother methods (cubic spline, monotone convex) provide more stable hedging.

---

## Practical Recommendations

### For Trading Desks

| Use Case | Recommended Method |
|----------|-------------------|
| Quick indicative pricing | Linear on zero rates |
| Precise hedging | Monotone convex |
| Risk reporting | Consistent with trading system |
| Stress testing | Method should handle extreme curves |

### For Model Validation

- Test that method reprices bootstrapping instruments exactly
- Verify forward rates are sensible (positive, reasonable magnitude)
- Check stability under small input perturbations
- Compare hedge ratios across methods

### Implementation Tips

1. **Store both** discount factors and zero rates at nodes
2. **Precompute** spline coefficients for efficiency
3. **Validate** that $P(0, 0) = 1$ and $P(0, T) > 0$
4. **Document** the method used—different systems may differ

---

## Advanced Topics

### Tension Splines

Add a "tension" parameter $\tau$ to control smoothness vs. fidelity:

$$
z''(T) - \tau^2 z(T) = 0 \quad \text{(within intervals)}
$$

Higher tension → closer to linear; lower tension → closer to natural spline.

### Rational Interpolation

Use ratios of polynomials:

$$
z(0, T) = \frac{a_0 + a_1 T + a_2 T^2}{1 + b_1 T}
$$

Can better capture certain curve shapes.

### Machine Learning Approaches

Recent work uses neural networks to:
- Learn interpolation from historical curves
- Capture complex dependencies
- Maintain no-arbitrage constraints via architecture

---

## Key Takeaways

- Interpolation extends discrete bootstrapped points to a continuous curve
- The choice of what variable to interpolate (discount, zero, forward) matters significantly
- Linear methods are simple but produce discontinuous or stepped forward rates
- Cubic splines are smooth but may oscillate or produce negative forwards
- Monotone convex methods balance smoothness, positivity, and locality
- Interpolation choice affects hedge ratios and P&L attribution
- Practitioners should understand the implications of their chosen method

---

## Further Reading

- Hagan & West, "Interpolation Methods for Curve Construction" (2006)
- Andersen & Piterbarg, *Interest Rate Modeling*, Volume 1
- Le Floc'h, "Stable Interpolation for the Yield Curve" (2017)
