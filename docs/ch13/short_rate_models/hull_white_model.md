# The Hull-White Model

The **Hull-White model** (1990) extends Vasicek by introducing a time-dependent drift that enables **exact calibration to the initial yield curve**. This makes it the workhorse model for interest rate derivatives in practice.

---

## Model Specification

### Risk-Neutral Dynamics

Under the risk-neutral measure $\mathbb{Q}$:

$$
dr_t = [\theta(t) - \kappa r_t] \, dt + \sigma \, dW_t^{\mathbb{Q}}
$$

or equivalently:

$$
dr_t = \kappa[\bar{\theta}(t) - r_t] \, dt + \sigma \, dW_t^{\mathbb{Q}}
$$

where $\bar{\theta}(t) = \theta(t)/\kappa$.

**Key difference from Vasicek:** The function $\theta(t)$ (or $\bar{\theta}(t)$) is time-dependent, chosen to match market data.

### Parameters

- $\kappa > 0$: mean-reversion speed (constant)
- $\theta(t)$: time-dependent drift function (calibrated)
- $\sigma > 0$: volatility (constant or time-dependent $\sigma(t)$)

---

## Exact Fit to the Initial Yield Curve

### The Calibration Requirement

For the model to reprice all observed discount bonds exactly:

$$
P^{\text{model}}(0, T) = P^{\text{market}}(0, T) \quad \text{for all } T
$$

This determines $\theta(t)$ uniquely.

### Derivation of $\theta(t)$

The initial instantaneous forward rate is:

$$
f(0, T) = -\frac{\partial}{\partial T} \log P(0, T)
$$

The Hull-White model requires:

$$
\boxed{\theta(t) = \frac{\partial f(0, t)}{\partial t} + \kappa f(0, t) + \frac{\sigma^2}{2\kappa}(1 - e^{-2\kappa t})}
$$

**Derivation sketch:**

1. The model-implied forward rate at time 0 for maturity $T$ must equal market forward rate
2. Differentiating the bond price formula and matching to $f(0, T)$
3. Solving for $\theta(t)$

### Interpretation

The function $\theta(t)$ adjusts the drift so that:
- At short horizons, the model matches the short-end of the curve
- At long horizons, the model matches the long-end
- The adjustment accounts for convexity effects (the $\sigma^2$ term)

---

## Solution of the SDE

### Explicit Solution

Given $r_s$ at time $s$, the short rate at time $t > s$ is:

$$
r_t = r_s e^{-\kappa(t-s)} + \int_s^t e^{-\kappa(t-u)} \theta(u) \, du + \sigma \int_s^t e^{-\kappa(t-u)} dW_u
$$

### Distribution

$r_t$ remains **Gaussian** conditional on $r_s$:

$$
r_t \mid r_s \sim \mathcal{N}(m(s, t), v(s, t))
$$

where:

$$
m(s, t) = r_s e^{-\kappa(t-s)} + \int_s^t e^{-\kappa(t-u)} \theta(u) \, du
$$

$$
v(s, t) = \frac{\sigma^2}{2\kappa}(1 - e^{-2\kappa(t-s)})
$$

The variance formula is identical to Vasicek.

---

## Zero-Coupon Bond Pricing

### Affine Structure

Bond prices remain exponential-affine:

$$
P(t, T) = A(t, T) \exp(-B(t, T) \cdot r_t)
$$

### The Function $B(t, T)$

$$
B(t, T) = \frac{1 - e^{-\kappa(T-t)}}{\kappa}
$$

This is identical to Vasicek!

### The Function $A(t, T)$

$$
\log A(t, T) = \log \frac{P(0, T)}{P(0, t)} - B(t, T) f(0, t) - \frac{\sigma^2}{4\kappa}(1 - e^{-2\kappa t}) B(t, T)^2
$$

Alternatively:

$$
A(t, T) = \frac{P(0, T)}{P(0, t)} \exp\left[-B(t, T) f(0, t) - \frac{\sigma^2}{4\kappa} B(t, T)^2 (1 - e^{-2\kappa t})\right]
$$

### Verification of Initial Fit

At $t = 0$:

$$
P(0, T) = A(0, T) e^{-B(0, T) r_0}
$$

By construction, $A(0, T)$ is chosen so this equals the market price.

---

## Forward Rate Dynamics

### Model-Implied Forward Rate

The instantaneous forward rate at time $t$ for maturity $T$ is:

$$
f(t, T) = -\frac{\partial}{\partial T} \log P(t, T) = f(0, T) + \frac{\sigma^2}{2\kappa^2}(1 - e^{-\kappa(T-t)})^2 - \frac{\sigma^2}{2\kappa^2}(1 - e^{-\kappa T})^2 e^{-\kappa t} + \sigma_f(t, T) \cdot Z_t
$$

where $Z_t$ is a standard normal and $\sigma_f(t, T)$ is the forward rate volatility.

### Forward Rate Volatility

$$
\sigma_f(t, T) = \sigma \cdot e^{-\kappa(T-t)}
$$

This decays exponentially with time-to-maturity—short forwards are more volatile than long forwards.

---

## Option Pricing

### European Bond Options

A call option on a $T_2$-bond with strike $K$, expiring at $T_1 < T_2$:

$$
\boxed{C(0) = P(0, T_2) N(d_1) - K P(0, T_1) N(d_2)}
$$

where:

$$
d_1 = \frac{1}{\sigma_P} \log \frac{P(0, T_2)}{K P(0, T_1)} + \frac{\sigma_P}{2}
$$

$$
d_2 = d_1 - \sigma_P
$$

and the **bond price volatility** is:

$$
\sigma_P = \sigma \cdot B(T_1, T_2) \cdot \sqrt{\frac{1 - e^{-2\kappa T_1}}{2\kappa}}
$$

### Put Options

$$
P_{\text{opt}}(0) = K P(0, T_1) N(-d_2) - P(0, T_2) N(-d_1)
$$

---

## Cap and Floor Pricing

### Caplet Pricing

A caplet paying $\max(L(T_1, T_2) - K, 0)$ at $T_2$ can be viewed as a put option on a bond.

**Caplet price:**

$$
\text{Caplet} = (1 + K\delta) \cdot P(0, T_1) N(-d_2) - P(0, T_2) N(-d_1)
$$

where $\delta = T_2 - T_1$ is the accrual fraction.

### Cap Pricing

A cap is a portfolio of caplets:

$$
\text{Cap} = \sum_{i=1}^{n} \text{Caplet}_i
$$

Hull-White provides closed-form caplet prices, making cap calibration efficient.

---

## Swaption Pricing

### Jamshidian's Trick

For a payer swaption (option to enter a payer swap), the payoff at expiry $T_0$ is:

$$
\max\left(\sum_{i=1}^{n} c_i P(T_0, T_i) - 1, 0\right)
$$

where $c_i$ are the swap cashflows (fixed leg).

**Key insight:** Since bond prices are monotonic in $r$, there exists a unique $r^*$ such that:

$$
\sum_{i=1}^{n} c_i P(T_0, T_i, r^*) = 1
$$

### Decomposition into Bond Options

The swaption can be decomposed into a portfolio of bond options:

$$
\text{Swaption} = \sum_{i=1}^{n} c_i \cdot \text{Put}(P(T_0, T_i), K_i = P(T_0, T_i, r^*))
$$

Each put option has an analytical formula, so the swaption price is semi-analytical.

---

## Trinomial Tree Implementation

### Why Trees?

While analytical formulas exist for European options, American options and path-dependent payoffs require numerical methods. Trinomial trees are standard.

### Tree Construction

1. **Discretize time:** $\Delta t = T/N$
2. **Short rate grid:** $r_j = r_{\min} + j \cdot \Delta r$
3. **Transition probabilities:** From each node, three branches (up, middle, down) with probabilities $(p_u, p_m, p_d)$

### Hull-White Tree Specifics

- The mean-reverting drift determines the "central" branch
- Probabilities are adjusted to match the first two moments
- The function $\theta(t)$ is incorporated via node positions

---

## Calibration Procedure

### Step 1: Fit the Initial Curve

Given market discount factors $P(0, T_i)$, compute:

1. Forward rates: $f(0, T) = -\partial_T \log P(0, T)$
2. $\theta(t)$ from the formula above

This is **automatic** once $\kappa$ and $\sigma$ are fixed.

### Step 2: Calibrate to Volatility Instruments

Fit $\kappa$ and $\sigma$ (or $\sigma(t)$) to:
- Cap implied volatilities
- Swaption implied volatilities

**Objective function:**

$$
\min_{\kappa, \sigma} \sum_{i} w_i \left(\sigma^{\text{model}}_i(\kappa, \sigma) - \sigma^{\text{market}}_i\right)^2
$$

### Typical Results

| Instrument | Typical Fit Quality |
|------------|---------------------|
| ATM caps | Good |
| ATM swaptions | Good |
| OTM options | Limited (no smile) |

---

## Extensions

### Time-Dependent Volatility

Allow $\sigma(t)$ to vary:

$$
dr_t = [\theta(t) - \kappa r_t] \, dt + \sigma(t) \, dW_t
$$

This adds flexibility to fit the volatility term structure.

### Two-Factor Hull-White (G2++)

Add a second factor:

$$
r_t = x_t + y_t + \phi(t)
$$

where $x_t$ and $y_t$ are correlated Ornstein-Uhlenbeck processes. This allows richer yield curve dynamics.

---

## Strengths and Limitations

### Strengths

- **Exact curve fit:** Matches any initial yield curve by construction
- **Analytical tractability:** Closed-form bond and option prices
- **Industry standard:** Widely implemented and understood
- **Efficient calibration:** Fast numerical procedures

### Limitations

- **Gaussian rates:** Negative rates possible (though now less problematic)
- **No smile:** Cannot capture volatility smile/skew
- **Single factor:** Limited curve dynamics
- **Time-inhomogeneous:** $\theta(t)$ function must be stored

---

## Key Takeaways

- Hull-White: $dr_t = [\theta(t) - \kappa r_t]dt + \sigma dW_t$
- $\theta(t)$ calibrated to match initial yield curve exactly
- Bond prices remain exponential-affine with same $B(\tau)$ as Vasicek
- Closed-form European option prices via Gaussian formulas
- Swaption pricing via Jamshidian decomposition
- Standard choice for practical interest rate modeling

---

## Further Reading

- Hull & White (1990), "Pricing Interest-Rate-Derivative Securities"
- Brigo & Mercurio, *Interest Rate Models*, Chapter 3
- Andersen & Piterbarg, *Interest Rate Modeling*, Volume 2
