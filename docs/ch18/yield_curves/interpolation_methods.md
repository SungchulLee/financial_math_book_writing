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

---

## Exercises

**Exercise 1.** Given bootstrapped discount factors at $T = 1, 2, 3, 5, 7, 10$ years, you need $P(0, 4)$. Compare linear interpolation on zero rates versus linear interpolation on log discount factors. Compute both and show they give different answers. Which produces smoother forward rates?

??? success "Solution to Exercise 1"
    Suppose the bootstrapped data gives discount factors at $T = 1, 2, 3, 5, 7, 10$ years. For concreteness, use zero rates: $z_1 = 3.0\%$, $z_2 = 3.3\%$, $z_3 = 3.5\%$, $z_5 = 3.8\%$, $z_7 = 4.0\%$, $z_{10} = 4.1\%$, so the discount factors are $P_i = e^{-z_i T_i}$.

    We need $P(0, 4)$, which lies between $T_3 = 3$ and $T_5 = 5$. Let $\alpha = (4 - 3)/(5 - 3) = 0.5$.

    **Method 1 — Linear interpolation on zero rates:**

    $$
    z(0, 4) = z_3 + \alpha(z_5 - z_3) = 0.035 + 0.5 \times (0.038 - 0.035) = 0.035 + 0.0015 = 0.0365
    $$

    $$
    P_{\text{zero}}(0, 4) = e^{-0.0365 \times 4} = e^{-0.146} \approx 0.86416
    $$

    **Method 2 — Linear interpolation on log discount factors:**

    $$
    \log P_3 = -z_3 \times 3 = -0.105, \quad \log P_5 = -z_5 \times 5 = -0.190
    $$

    $$
    \log P(0, 4) = -0.105 + 0.5 \times (-0.190 - (-0.105)) = -0.105 + 0.5 \times (-0.085) = -0.1475
    $$

    $$
    P_{\text{log}}(0, 4) = e^{-0.1475} \approx 0.86281
    $$

    The two methods give different answers: $0.86416$ versus $0.86281$. This is because interpolating linearly on zero rates is equivalent to $z(0, T) \cdot T$ being a quadratic function of $T$ within the interval, while interpolating on log discounts makes $\log P(0, T)$ a linear function of $T$.

    **Forward rate comparison:** Linear interpolation on log discounts produces a **piecewise constant** forward curve (the forward rate is $f = (\log P_3 - \log P_5)/(5 - 3) = 0.085/2 = 4.25\%$ constant on $[3, 5]$), with jumps at nodes. Linear interpolation on zero rates produces a **piecewise linear continuous** forward curve, which is smoother. Therefore, **linear interpolation on zero rates produces smoother forward rates**.

---

**Exercise 2.** Explain why linear interpolation on discount factors can produce negative forward rates even when all zero rates are positive. Construct a numerical example with two adjacent discount factors that demonstrates this pathology.

??? success "Solution to Exercise 2"
    Linear interpolation directly on discount factors takes the form, for $T \in [T_i, T_{i+1}]$:

    $$
    P(0, T) = P_i + \frac{T - T_i}{T_{i+1} - T_i}(P_{i+1} - P_i)
    $$

    The instantaneous forward rate is:

    $$
    f(0, T) = -\frac{\partial}{\partial T}\log P(0, T) = -\frac{P'(0, T)}{P(0, T)} = -\frac{(P_{i+1} - P_i)/(T_{i+1} - T_i)}{P(0, T)}
    $$

    The numerator of this fraction (i.e., $-P'$) is constant within each interval, but $P(0, T)$ in the denominator decreases. As $P(0, T) \to 0^+$, the forward rate diverges.

    **Numerical example:** Let $T_1 = 9$, $T_2 = 10$, $P_1 = 0.05$, $P_2 = 0.01$. These correspond to high zero rates at long maturities. For $T \in [9, 10]$:

    $$
    P(0, T) = 0.05 + (T - 9)(0.01 - 0.05) = 0.05 - 0.04(T - 9)
    $$

    The forward rate is:

    $$
    f(0, T) = -\frac{-0.04}{0.05 - 0.04(T - 9)} = \frac{0.04}{0.05 - 0.04(T - 9)}
    $$

    At $T = 9$: $f = 0.04/0.05 = 0.80$ (80%). At $T = 9.5$: $f = 0.04/0.03 = 1.33$ (133%). As $T \to 10^-$: $f \to 0.04/0.01 = 4.0$ (400%).

    Even more dramatically, if the linear interpolation crosses zero (e.g., a slightly different setup), the forward rate diverges to $+\infty$ and then becomes negative, which is clearly unphysical. This pathology arises because direct interpolation on discount factors does not respect the exponential structure of the discount function.

---

**Exercise 3.** Cubic spline interpolation on zero rates produces a $C^2$ curve. Describe the boundary conditions (natural, clamped, not-a-knot) and their effect on the forward rate curve near the short and long ends. Which boundary condition is most appropriate for yield curve construction?

??? success "Solution to Exercise 3"
    A natural cubic spline on zero rates $z(0, T)$ fits a piecewise cubic polynomial $S_i(T)$ on each interval $[T_i, T_{i+1}]$ satisfying:

    - **Interpolation:** $S_i(T_i) = z_i$, $S_i(T_{i+1}) = z_{i+1}$
    - **$C^1$ continuity:** $S_i'(T_{i+1}) = S_{i+1}'(T_{i+1})$
    - **$C^2$ continuity:** $S_i''(T_{i+1}) = S_{i+1}''(T_{i+1})$

    The boundary conditions determine behavior at the endpoints $T_1$ and $T_n$:

    **Natural boundary ($z''(T_1) = z''(T_n) = 0$):** This sets the second derivative to zero at both ends, making the spline approach linearity near the boundaries. For the forward curve $f = z + T z'$, this means the forward rate near the short end is approximately $z_1 + T_1 z'(T_1)$, where $z'(T_1)$ is determined by the data. Since $z'' = 0$ at the boundary, the forward curve has zero curvature there, which may cause the short-end forwards to deviate from market expectations. At the long end, the same flatness may produce unrealistic extrapolation.

    **Clamped boundary ($z'(T_1) = d_1$, $z'(T_n) = d_n$):** Specifying the first derivatives at the endpoints gives direct control over the slope of the zero curve (and hence the level of the forward rate) at the boundaries. This is useful if the short-end forward rate is known from overnight rates, or if the long-end slope is constrained by economic views. However, it requires additional information.

    **Not-a-knot boundary:** Enforces $z'''$ continuity at $T_2$ and $T_{n-1}$ (the second and penultimate nodes), effectively merging the first two and last two polynomial segments. This avoids artificial boundary effects and lets the data drive the curve shape near the endpoints.

    **For yield curve construction,** the **not-a-knot** boundary is often most appropriate because it does not impose arbitrary constraints at the endpoints and produces a curve whose behavior at the boundaries is governed by nearby market data rather than an artificial mathematical condition.

---

**Exercise 4.** The monotone convex method ensures positive and stable forward rates. Explain the key idea: interpolate on log discount factors with constraints that prevent the forward curve from becoming negative. What is the trade-off compared to unconstrained cubic splines?

??? success "Solution to Exercise 4"
    The monotone convex method, introduced by Hagan and West (2006), interpolates the function $g(T) = -\log P(0, T) = z(0, T) \cdot T$, which is the integral of the instantaneous forward rate:

    $$
    g(T) = \int_0^T f(0, u)\,du
    $$

    The forward rate is the derivative $f(0, T) = g'(T)$. The key idea is to construct $g(T)$ such that:

    1. **Positivity of forwards:** $g'(T) > 0$ for all $T$, ensuring forward rates are positive. Since $g(T)$ must be increasing (as $-\log P$ increases with maturity under positive rates), the method constrains the interpolant to be strictly increasing.

    2. **Monotonicity within segments:** If the discrete forward rates $f_i^{\text{disc}} = (g(T_{i+1}) - g(T_i))/(T_{i+1} - T_i)$ are increasing (or decreasing) between adjacent intervals, the instantaneous forward rate $f(0, T)$ is constrained to be monotone within each segment. This prevents the oscillations that plague unconstrained cubic splines.

    3. **Locality:** Each segment's interpolant depends only on adjacent data points, so a change at one node does not propagate across the entire curve. This contrasts with global cubic splines, where changing one data point can affect the entire curve.

    **Trade-off compared to unconstrained cubic splines:** The monotone convex method sacrifices some global smoothness — specifically, the forward curve is only $C^1$ (continuous with continuous first derivative) rather than $C^2$ as with cubic splines. The second derivative of the forward curve may have jumps at the knot points. In practice, this loss of smoothness is negligible compared to the benefit of guaranteed positive, non-oscillatory forward rates. Unconstrained cubic splines can produce forward rates that are negative or wildly oscillating, which leads to nonsensical prices for forward-starting instruments and unstable hedging.

---

**Exercise 5.** A hedger computes DV01 by bumping individual input rates and observing the discount factor change. Show that the choice of interpolation method affects the hedging sensitivities, even though the curve passes through the same market points. Why might cubic spline interpolation produce unrealistic hedging buckets?

??? success "Solution to Exercise 5"
    Consider a portfolio with value $V$ depending on the discount curve. The DV01 with respect to input rate $i$ (bucket sensitivity) is computed by bumping rate $z_i$ by 1 basis point and observing the change in $V$:

    $$
    \text{DV01}_i = \frac{\partial V}{\partial z_i} \approx \frac{V(z_i + 0.0001) - V(z_i)}{0.0001}
    $$

    By the chain rule:

    $$
    \frac{\partial V}{\partial z_i} = \int_0^{T_{\max}} \frac{\partial V}{\partial P(0, T)} \cdot \frac{\partial P(0, T)}{\partial z_i}\,dT
    $$

    The critical factor is $\frac{\partial P(0, T)}{\partial z_i}$, which depends on the interpolation method.

    **Linear interpolation (local method):** Bumping $z_i$ affects $P(0, T)$ only for $T \in [T_{i-1}, T_{i+1}]$ (the two adjacent intervals). The Jacobian $\frac{\partial P(0, T)}{\partial z_i}$ is sparse — most entries are zero. This produces clean, localized hedging buckets: each input rate's DV01 reflects sensitivity only from cashflows near that maturity.

    **Cubic spline interpolation (global method):** Bumping $z_i$ potentially affects the spline coefficients on every interval because the spline system is coupled globally (the tridiagonal system for second derivatives links all nodes). The Jacobian $\frac{\partial P(0, T)}{\partial z_i}$ is dense — all entries are nonzero. This means:

    - A 1bp bump to the 2-year rate changes discount factors at 10 years and beyond.
    - Hedging buckets become unrealistic: a 5-year cashflow may show significant sensitivity to the 30-year input rate.
    - Small changes in one part of the curve produce ripple effects in hedging buckets far away.
    - P&L attribution becomes difficult because changes are spread across many buckets.

    In practice, traders prefer local methods (or monotone convex) precisely because they produce intuitive hedging buckets where sensitivities are concentrated near the relevant maturity.

---

**Exercise 6.** Compare piecewise constant forward rates with piecewise linear forward rates. For each method, describe the continuity class of the discount factor curve and the forward rate curve. Which is simpler to implement? Which produces more realistic hedging behavior?

??? success "Solution to Exercise 6"
    **Piecewise constant forward rates:** The instantaneous forward rate $f(0, T) = f_i$ is constant on each interval $(T_i, T_{i+1})$, with jumps at the nodes.

    - **Forward rate curve:** Discontinuous ($C^{-1}$ at nodes); constant between nodes
    - **Discount factor curve:** Since $P(0, T) = \exp\left(-\int_0^T f(0, u)\,du\right)$, and the integral of a piecewise constant function is piecewise linear, $\log P(0, T)$ is piecewise linear and $P(0, T)$ is piecewise exponential-linear. The discount factor curve is $C^0$ (continuous) but not $C^1$ — it has kinks at the nodes.
    - **Zero rate curve:** $z(0, T) = -\log P(0, T)/T$ is continuous.

    **Piecewise linear forward rates:** The forward rate $f(0, T) = f_i + \frac{T - T_i}{T_{i+1} - T_i}(f_{i+1} - f_i)$ varies linearly on each interval, and is continuous at the nodes.

    - **Forward rate curve:** Continuous ($C^0$) but not $C^1$ — it has kinks at the nodes
    - **Discount factor curve:** Since $\log P$ is the integral of a piecewise linear function, it is piecewise quadratic, making $P(0, T)$ a $C^1$ function (continuous with continuous first derivative). The discount factor curve is smoother than in the piecewise constant case.
    - **Zero rate curve:** Continuous and smoother than the piecewise constant case.

    **Simplicity:** Piecewise constant forwards are simpler to implement. Each forward rate is just a ratio of adjacent discount factors, and no interpolation within intervals is needed. The discount factor at any $T$ is computed by accumulating products of $e^{-f_i \Delta_i}$ terms.

    **Hedging behavior:** Piecewise linear forward rates produce more realistic hedging because the forward curve is continuous, meaning hedge ratios do not jump discontinuously as an instrument's maturity crosses a node date. With piecewise constant forwards, a cashflow's sensitivity can change abruptly when it moves from one flat segment to an adjacent one with a very different forward rate. The piecewise linear method distributes this change smoothly, yielding more stable and interpretable hedging buckets.
