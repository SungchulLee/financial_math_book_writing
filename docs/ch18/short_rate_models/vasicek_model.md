# The Vasicek Model

The Vasicek model (1977) is the foundational mean-reverting short-rate model. Its Gaussian structure yields closed-form bond prices and option formulas, making it a benchmark for understanding more complex models.

---

## Model Specification

### Risk-Neutral Dynamics

Under the risk-neutral measure $\mathbb{Q}$, the short rate follows an **Ornstein-Uhlenbeck (OU) process**:

$$
dr_t = \kappa(\theta - r_t) \, dt + \sigma \, dW_t^{\mathbb{Q}}
$$

where:
- $\kappa > 0$: **mean-reversion speed** (rate of pull toward $\theta$)
- $\theta$: **long-run mean level** (equilibrium rate)
- $\sigma > 0$: **volatility** (instantaneous standard deviation)
- $W_t^{\mathbb{Q}}$: standard Brownian motion under $\mathbb{Q}$

### Physical Dynamics

Under the physical measure $\mathbb{P}$:

$$
dr_t = \kappa(\theta^{\mathbb{P}} - r_t) \, dt + \sigma \, dW_t^{\mathbb{P}}
$$

The relationship between measures:

$$
\theta = \theta^{\mathbb{P}} - \frac{\lambda \sigma}{\kappa}
$$

where $\lambda$ is the market price of interest rate risk.

---

## Solution of the SDE

### Explicit Solution

The Vasicek SDE has the explicit solution:

$$
r_t = r_0 e^{-\kappa t} + \theta(1 - e^{-\kappa t}) + \sigma \int_0^t e^{-\kappa(t-s)} \, dW_s
$$

**Derivation:** 

Let $Y_t = r_t e^{\kappa t}$. Then:

$$
dY_t = e^{\kappa t} dr_t + \kappa e^{\kappa t} r_t \, dt = e^{\kappa t}[\kappa(\theta - r_t) + \kappa r_t] dt + \sigma e^{\kappa t} dW_t = \kappa \theta e^{\kappa t} dt + \sigma e^{\kappa t} dW_t
$$

Integrating:

$$
Y_t = Y_0 + \kappa \theta \int_0^t e^{\kappa s} ds + \sigma \int_0^t e^{\kappa s} dW_s = r_0 + \theta(e^{\kappa t} - 1) + \sigma \int_0^t e^{\kappa s} dW_s
$$

Therefore:

$$
r_t = Y_t e^{-\kappa t} = r_0 e^{-\kappa t} + \theta(1 - e^{-\kappa t}) + \sigma e^{-\kappa t} \int_0^t e^{\kappa s} dW_s
$$

### Distribution of $r_t$

Since $r_t$ is a linear functional of Brownian motion, it is **normally distributed**:

$$
r_t \mid r_0 \sim \mathcal{N}(m(t), v(t))
$$

where:

$$
m(t) = \mathbb{E}[r_t] = r_0 e^{-\kappa t} + \theta(1 - e^{-\kappa t})
$$

$$
v(t) = \text{Var}(r_t) = \frac{\sigma^2}{2\kappa}(1 - e^{-2\kappa t})
$$

### Long-Run Behavior

As $t \to \infty$:

$$
\mathbb{E}[r_t] \to \theta, \quad \text{Var}(r_t) \to \frac{\sigma^2}{2\kappa}
$$

The stationary distribution is:

$$
r_\infty \sim \mathcal{N}\left(\theta, \frac{\sigma^2}{2\kappa}\right)
$$

---

## Key Properties

### Mean Reversion

The drift $\kappa(\theta - r_t)$:
- Pulls $r_t$ **toward** $\theta$ when $r_t \neq \theta$
- Pull strength is proportional to deviation $|r_t - \theta|$
- Half-life of mean reversion: $t_{1/2} = \frac{\ln 2}{\kappa}$

**Example:** If $\kappa = 0.5$, the half-life is approximately 1.4 years.

### Gaussianity

The short rate $r_t$ is normally distributed at all times. This implies:
- **Negative rates are possible:** $\mathbb{P}(r_t < 0) > 0$
- **Simple closed-form results:** Gaussian integrals are tractable
- **Limited smile/skew:** Cannot capture observed volatility patterns

### Time Homogeneity

The Vasicek model has constant parameters $(\kappa, \theta, \sigma)$. This limits flexibility but ensures stability.

---

## Zero-Coupon Bond Pricing

### Affine Structure

The bond price takes the **exponential-affine** form:

$$
\boxed{P(t, T) = A(t, T) \exp(-B(t, T) \cdot r_t)}
$$

where $A(t, T) > 0$ and $B(t, T) > 0$ are deterministic functions.

### Derivation via PDE

The bond price $P(t, T, r)$ satisfies the PDE:

$$
\frac{\partial P}{\partial t} + \kappa(\theta - r) \frac{\partial P}{\partial r} + \frac{1}{2}\sigma^2 \frac{\partial^2 P}{\partial r^2} = rP
$$

with $P(T, T, r) = 1$.

**Ansatz:** Guess $P = A(\tau) e^{-B(\tau) r}$ where $\tau = T - t$ (time to maturity).

Substituting into the PDE:

$$
-A'(\tau) e^{-Br} + A \cdot B'(\tau) r \cdot e^{-Br} + \kappa(\theta - r)(-AB e^{-Br}) + \frac{1}{2}\sigma^2 A B^2 e^{-Br} = r A e^{-Br}
$$

Dividing by $A e^{-Br}$:

$$
-\frac{A'}{A} + B' r - \kappa \theta B + \kappa r B + \frac{1}{2}\sigma^2 B^2 = r
$$

Collecting terms in $r$:

- Coefficient of $r$: $B' + \kappa B = 1$
- Constant term: $-\frac{A'}{A} - \kappa \theta B + \frac{1}{2}\sigma^2 B^2 = 0$

### ODE for $B(\tau)$

$$
\frac{dB}{d\tau} = 1 - \kappa B, \quad B(0) = 0
$$

**Solution:**

$$
\boxed{B(\tau) = \frac{1 - e^{-\kappa \tau}}{\kappa}}
$$

### ODE for $A(\tau)$

$$
\frac{d \log A}{d\tau} = \kappa \theta B - \frac{1}{2}\sigma^2 B^2, \quad A(0) = 1
$$

Integrating:

$$
\log A(\tau) = \kappa \theta \int_0^\tau B(s) \, ds - \frac{\sigma^2}{2} \int_0^\tau B(s)^2 \, ds
$$

After computation:

$$
\boxed{A(\tau) = \exp\left[\left(\theta - \frac{\sigma^2}{2\kappa^2}\right)(B(\tau) - \tau) - \frac{\sigma^2 B(\tau)^2}{4\kappa}\right]}
$$

### Complete Bond Price Formula

$$
P(t, T) = \exp\left[\left(\theta - \frac{\sigma^2}{2\kappa^2}\right)(B(\tau) - \tau) - \frac{\sigma^2 B(\tau)^2}{4\kappa} - B(\tau) r_t\right]
$$

where $\tau = T - t$ and $B(\tau) = \frac{1 - e^{-\kappa \tau}}{\kappa}$.

---

## Yield Curve Analysis

### Zero Rate

The continuously compounded zero rate is:

$$
z(t, T) = -\frac{\log P(t, T)}{\tau} = \frac{B(\tau)}{\tau} r_t + \frac{\tau - B(\tau)}{\tau}\left(\theta - \frac{\sigma^2}{2\kappa^2}\right) + \frac{\sigma^2 B(\tau)^2}{4\kappa \tau}
$$

### Asymptotic Long Rate

As $T \to \infty$ (i.e., $\tau \to \infty$):

$$
B(\tau) \to \frac{1}{\kappa}, \quad \frac{B(\tau)}{\tau} \to 0
$$

The long rate converges to:

$$
z_\infty = \theta - \frac{\sigma^2}{2\kappa^2}
$$

This is the **asymptotic yield**.

### Yield Curve Shapes

The Vasicek model can produce:

| Shape | Condition |
|-------|-----------|
| Upward sloping | $r_0 < z_\infty$ |
| Flat | $r_0 = z_\infty$ |
| Downward sloping | $r_0 > z_\infty$ |
| Humped | Possible for certain parameter combinations |

---

## Option Pricing

### Bond Option Formula

A European call option on a $T_2$-bond with strike $K$, expiring at $T_1 < T_2$, has price:

$$
C(0, T_1, T_2, K) = P(0, T_2) N(d_1) - K P(0, T_1) N(d_2)
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
\sigma_P = \sigma B(T_2 - T_1) \sqrt{\frac{1 - e^{-2\kappa T_1}}{2\kappa}}
$$

### Put Option (Put-Call Parity)

$$
P_{\text{opt}} = K P(0, T_1) N(-d_2) - P(0, T_2) N(-d_1)
$$

### Caps and Floors

A caplet can be viewed as a put option on a bond. The Vasicek model provides closed-form caplet prices, enabling analytic cap pricing.

---

## Limitations

### Negative Rates

The Gaussian distribution implies:

$$
\mathbb{P}(r_t < 0) = \Phi\left(\frac{-m(t)}{\sqrt{v(t)}}\right) > 0
$$

While negative rates are now observed in some markets, the model doesn't constrain their probability.

### Constant Parameters

The basic Vasicek model cannot fit an arbitrary initial yield curve—only specific shapes consistent with the parameters.

### Limited Volatility Structure

- Constant volatility across rates
- Cannot capture volatility smile/skew
- Homoskedastic rate changes

---

## Hull-White Extension

The **Hull-White model** extends Vasicek with time-dependent $\theta(t)$:

$$
dr_t = \kappa(\theta(t) - r_t) \, dt + \sigma \, dW_t
$$

The function $\theta(t)$ is calibrated to match the initial yield curve exactly:

$$
\theta(t) = \frac{1}{\kappa}\frac{\partial f(0, t)}{\partial t} + f(0, t) + \frac{\sigma^2}{2\kappa^2}(1 - e^{-2\kappa t})
$$

where $f(0, t)$ is the initial instantaneous forward rate.

---

## Calibration

### To Initial Yield Curve

For basic Vasicek, minimize:

$$
\sum_{i} \left(P^{\text{model}}(0, T_i; \kappa, \theta, \sigma, r_0) - P^{\text{market}}(0, T_i)\right)^2
$$

Often, exact fit is not achievable without Hull-White extension.

### To Options

Given the yield curve, calibrate $\sigma$ (and possibly $\kappa$) to cap/swaption implied volatilities.

### Parameter Interpretation

| Parameter | Typical Values | Effect |
|-----------|----------------|--------|
| $\kappa$ | 0.01 – 0.5 | Higher = faster mean reversion |
| $\theta$ | 0.02 – 0.08 | Long-run rate level |
| $\sigma$ | 0.005 – 0.02 | Rate volatility |

---

## Key Takeaways

- Vasicek: $dr_t = \kappa(\theta - r_t)dt + \sigma dW_t$ (Ornstein-Uhlenbeck)
- Rates are Gaussian: closed forms but negative rates possible
- Bond prices are exponential-affine: $P = A(\tau)e^{-B(\tau)r}$
- $B(\tau) = \frac{1 - e^{-\kappa\tau}}{\kappa}$, explicit $A(\tau)$ formula
- Hull-White extends with $\theta(t)$ for exact curve fit
- Option pricing via Gaussian formulas

---

## Further Reading

- Vasicek, O. (1977), "An Equilibrium Characterization of the Term Structure"
- Hull & White (1990), "Pricing Interest-Rate-Derivative Securities"
- Brigo & Mercurio, Chapter 3
