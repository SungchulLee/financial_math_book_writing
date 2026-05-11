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

### Distribution of r_t

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

### ODE for B(τ)

$$
\frac{dB}{d\tau} = 1 - \kappa B, \quad B(0) = 0
$$

**Solution:**

$$
\boxed{B(\tau) = \frac{1 - e^{-\kappa \tau}}{\kappa}}
$$

### ODE for A(τ)

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

---

## Exercises

**Exercise 1.** Solve the Vasicek SDE $dr_t = \kappa(\theta - r_t)\,dt + \sigma\,dW_t$ by applying Ito's lemma to $e^{\kappa t}r_t$. Show that $r_t = \theta + (r_0 - \theta)e^{-\kappa t} + \sigma\int_0^t e^{-\kappa(t-s)}\,dW_s$.

??? success "Solution to Exercise 1"
    Define $Y_t = e^{\kappa t} r_t$. By Ito's lemma (with $f(t,r) = e^{\kappa t}r$):

    $$
    dY_t = \kappa e^{\kappa t} r_t\,dt + e^{\kappa t}\,dr_t
    $$

    Substituting $dr_t = \kappa(\theta - r_t)\,dt + \sigma\,dW_t$:

    $$
    dY_t = \kappa e^{\kappa t} r_t\,dt + e^{\kappa t}[\kappa(\theta - r_t)\,dt + \sigma\,dW_t]
    $$

    $$
    = \kappa e^{\kappa t} r_t\,dt + \kappa\theta\, e^{\kappa t}\,dt - \kappa e^{\kappa t} r_t\,dt + \sigma e^{\kappa t}\,dW_t
    $$

    The $r_t$ terms cancel:

    $$
    dY_t = \kappa\theta\, e^{\kappa t}\,dt + \sigma e^{\kappa t}\,dW_t
    $$

    Integrating from $0$ to $t$:

    $$
    Y_t - Y_0 = \kappa\theta \int_0^t e^{\kappa s}\,ds + \sigma \int_0^t e^{\kappa s}\,dW_s
    $$

    Since $Y_0 = r_0$ and $\int_0^t e^{\kappa s}\,ds = \frac{e^{\kappa t} - 1}{\kappa}$:

    $$
    e^{\kappa t}r_t = r_0 + \theta(e^{\kappa t} - 1) + \sigma \int_0^t e^{\kappa s}\,dW_s
    $$

    Dividing by $e^{\kappa t}$:

    $$
    r_t = r_0 e^{-\kappa t} + \theta(1 - e^{-\kappa t}) + \sigma \int_0^t e^{-\kappa(t-s)}\,dW_s
    $$

    This can also be written as $r_t = \theta + (r_0 - \theta)e^{-\kappa t} + \sigma\int_0^t e^{-\kappa(t-s)}\,dW_s$, confirming the stated result.

---

---

**Exercise 2.** Show that $r_t$ in the Vasicek model is normally distributed with mean $\mathbb{E}[r_t] = \theta + (r_0 - \theta)e^{-\kappa t}$ and variance $\text{Var}(r_t) = \frac{\sigma^2}{2\kappa}(1 - e^{-2\kappa t})$. What is the stationary distribution as $t \to \infty$?

??? success "Solution to Exercise 2"
    From the solution in Exercise 1, $r_t = \theta + (r_0 - \theta)e^{-\kappa t} + \sigma\int_0^t e^{-\kappa(t-s)}\,dW_s$. The stochastic integral $\int_0^t e^{-\kappa(t-s)}\,dW_s$ is a Gaussian random variable (as a Wiener integral of a deterministic integrand).

    **Mean.** Since $\mathbb{E}[\int_0^t e^{-\kappa(t-s)}\,dW_s] = 0$:

    $$
    \mathbb{E}[r_t] = \theta + (r_0 - \theta)e^{-\kappa t} = r_0 e^{-\kappa t} + \theta(1 - e^{-\kappa t})
    $$

    **Variance.** By the Ito isometry:

    $$
    \text{Var}(r_t) = \sigma^2 \int_0^t e^{-2\kappa(t-s)}\,ds = \sigma^2 \left[\frac{e^{-2\kappa(t-s)}}{2\kappa}\right]_{s=0}^{s=t} = \frac{\sigma^2}{2\kappa}(1 - e^{-2\kappa t})
    $$

    Therefore $r_t \mid r_0 \sim \mathcal{N}(m(t), v(t))$ with

    $$
    m(t) = \theta + (r_0 - \theta)e^{-\kappa t}, \quad v(t) = \frac{\sigma^2}{2\kappa}(1 - e^{-2\kappa t})
    $$

    **Stationary distribution.** As $t \to \infty$, $e^{-\kappa t} \to 0$ and $e^{-2\kappa t} \to 0$, so

    $$
    m(\infty) = \theta, \quad v(\infty) = \frac{\sigma^2}{2\kappa}
    $$

    The stationary distribution is $r_\infty \sim \mathcal{N}\!\left(\theta, \frac{\sigma^2}{2\kappa}\right)$.

---

---

**Exercise 3.** For parameters $\kappa = 0.5$, $\theta = 0.04$, $\sigma = 0.01$, $r_0 = 0.03$, compute the mean and standard deviation of $r_t$ at $t = 1, 5, 10$. What is the probability that $r_{10} < 0$?

??? success "Solution to Exercise 3"
    With $\kappa = 0.5$, $\theta = 0.04$, $\sigma = 0.01$, $r_0 = 0.03$:

    $$
    m(t) = 0.04 + (0.03 - 0.04)e^{-0.5t} = 0.04 - 0.01\,e^{-0.5t}
    $$

    $$
    v(t) = \frac{0.0001}{1.0}(1 - e^{-t}) = 0.0001(1 - e^{-t})
    $$

    **At $t = 1$:** $e^{-0.5} \approx 0.6065$, $e^{-1} \approx 0.3679$

    $$
    m(1) = 0.04 - 0.01(0.6065) = 0.03394
    $$

    $$
    \text{Std}(r_1) = \sqrt{0.0001(1 - 0.3679)} = \sqrt{0.0000632} \approx 0.00795
    $$

    **At $t = 5$:** $e^{-2.5} \approx 0.08209$, $e^{-5} \approx 0.00674$

    $$
    m(5) = 0.04 - 0.01(0.08209) = 0.03918
    $$

    $$
    \text{Std}(r_5) = \sqrt{0.0001(1 - 0.00674)} = \sqrt{0.00009932} \approx 0.00997
    $$

    **At $t = 10$:** $e^{-5} \approx 0.00674$, $e^{-10} \approx 0.0000454$

    $$
    m(10) = 0.04 - 0.01(0.00674) = 0.03993
    $$

    $$
    \text{Std}(r_{10}) = \sqrt{0.0001(1 - 0.0000454)} \approx \sqrt{0.00009999} \approx 0.01000
    $$

    **Probability $r_{10} < 0$:**

    $$
    \mathbb{P}(r_{10} < 0) = \Phi\!\left(\frac{0 - 0.03993}{0.01000}\right) = \Phi(-3.993) \approx 3.3 \times 10^{-5}
    $$

    This is extremely small (about 0.003%), reflecting that $\theta = 4\%$ is about 4 standard deviations above zero.

---

---

**Exercise 4.** Derive the Vasicek bond pricing formula $P(t,T) = e^{A(\tau) - B(\tau)r_t}$ where $\tau = T - t$, $B(\tau) = \frac{1-e^{-\kappa\tau}}{\kappa}$, by computing $\mathbb{E}_t^{\mathbb{Q}}[e^{-\int_t^T r_s\,ds}]$ using the Gaussian distribution of $\int_t^T r_s\,ds$.

??? success "Solution to Exercise 4"
    The bond price is $P(t,T) = \mathbb{E}_t^{\mathbb{Q}}[e^{-\int_t^T r_s\,ds}]$. We need the distribution of $I = \int_t^T r_s\,ds$.

    Using $r_s = \theta + (r_t - \theta)e^{-\kappa(s-t)} + \sigma\int_t^s e^{-\kappa(s-u)}\,dW_u$:

    $$
    I = \int_t^T r_s\,ds = \theta\tau + (r_t - \theta)\int_t^T e^{-\kappa(s-t)}\,ds + \sigma\int_t^T\!\int_t^s e^{-\kappa(s-u)}\,dW_u\,ds
    $$

    where $\tau = T - t$. The deterministic integral gives

    $$
    \int_t^T e^{-\kappa(s-t)}\,ds = \frac{1 - e^{-\kappa\tau}}{\kappa} = B(\tau)
    $$

    Since $I$ is a Gaussian random variable (as a linear functional of Brownian motion), we have $I \sim \mathcal{N}(\mathbb{E}[I], \text{Var}(I))$.

    **Mean:**

    $$
    \mathbb{E}[I \mid r_t] = \theta\tau + (r_t - \theta)B(\tau)
    $$

    **Variance:** By Fubini and the Ito isometry (swapping the order of integration in the double stochastic integral):

    $$
    \text{Var}(I) = \frac{\sigma^2}{\kappa^2}\left[\tau - 2B(\tau) + \frac{1 - e^{-2\kappa\tau}}{2\kappa}\right]
    $$

    Since $e^{-I}$ is the exponential of a Gaussian, we use the moment generating function $\mathbb{E}[e^{-I}] = e^{-\mathbb{E}[I] + \frac{1}{2}\text{Var}(I)}$:

    $$
    P(t,T) = \exp\!\left(-\mathbb{E}[I] + \frac{1}{2}\text{Var}(I)\right)
    $$

    $$
    = \exp\!\left(-\theta\tau - (r_t - \theta)B(\tau) + \frac{\sigma^2}{2\kappa^2}\left[\tau - 2B(\tau) + \frac{1-e^{-2\kappa\tau}}{2\kappa}\right]\right)
    $$

    Rearranging into $e^{A(\tau) - B(\tau)r_t}$ form with $B(\tau) = \frac{1-e^{-\kappa\tau}}{\kappa}$:

    $$
    A(\tau) = \left(\theta - \frac{\sigma^2}{2\kappa^2}\right)(B(\tau) - \tau) - \frac{\sigma^2}{4\kappa}B(\tau)^2
    $$

    This completes the derivation via the expectation (moment generating function) approach.

---

---

**Exercise 5.** Using the parameters from Exercise 3, compute the zero-coupon bond price $P(0, 5)$ and the corresponding 5-year zero rate. Plot the yield curve $R(0, T)$ for $T = 1, 2, \ldots, 30$ and identify whether it is normal, inverted, or humped.

??? success "Solution to Exercise 5"
    Using $\kappa = 0.5$, $\theta = 0.04$, $\sigma = 0.01$, $r_0 = 0.03$, we compute $P(0,5)$ and the 5-year zero rate.

    **$B(5) = \frac{1 - e^{-2.5}}{0.5} = \frac{1 - 0.08209}{0.5} = 1.8358$**

    **$A(5)$:**

    $$
    \ln A(5) = \left(0.04 - \frac{0.0001}{0.5}\right)(1.8358 - 5) - \frac{0.0001 \times 1.8358^2}{2.0}
    $$

    $$
    = 0.0398 \times (-3.1642) - 0.0001685 = -0.12593 - 0.00017 = -0.12610
    $$

    **Bond price:**

    $$
    \ln P(0,5) = -0.12610 - 1.8358 \times 0.03 = -0.12610 - 0.05507 = -0.18117
    $$

    $$
    P(0,5) = e^{-0.18117} \approx 0.8343
    $$

    **5-year zero rate:**

    $$
    R(0,5) = -\frac{\ln P(0,5)}{5} = \frac{0.18117}{5} = 0.03623 = 3.623\%
    $$

    **Yield curve shape.** The asymptotic long rate is

    $$
    z_\infty = \theta - \frac{\sigma^2}{2\kappa^2} = 0.04 - \frac{0.0001}{0.5} = 0.04 - 0.0002 = 0.0398
    $$

    Since $r_0 = 0.03 < z_\infty = 0.0398$, the yield curve is **upward sloping** (normal). Short rates start at 3% and yields rise toward the asymptote of approximately 3.98%. The curve is not humped for these parameters. Computing a few representative points: $R(0,1) \approx 3.05\%$, $R(0,5) \approx 3.62\%$, $R(0,10) \approx 3.81\%$, $R(0,30) \approx 3.97\%$. The curve flattens as maturity increases, approaching $z_\infty$ from below.

---

---

**Exercise 6.** The main criticism of the Vasicek model is that it allows negative interest rates. Compute the probability $\Pr(r_t < 0)$ as a function of $t$ for the parameters in Exercise 3. At what time horizon does this probability exceed 5%? Discuss whether negative rates invalidate the model in the post-2015 era.

??? success "Solution to Exercise 6"
    With $\kappa = 0.5$, $\theta = 0.04$, $\sigma = 0.01$, $r_0 = 0.03$, the probability of negative rates is

    $$
    \mathbb{P}(r_t < 0) = \Phi\!\left(\frac{-m(t)}{\sqrt{v(t)}}\right)
    $$

    where $m(t) = 0.04 - 0.01\,e^{-0.5t}$ and $v(t) = 0.0001(1 - e^{-t})$.

    The ratio is

    $$
    \frac{-m(t)}{\sqrt{v(t)}} = \frac{-(0.04 - 0.01\,e^{-0.5t})}{0.01\sqrt{1 - e^{-t}}}
    $$

    **At $t = 1$:** numerator $= -0.03394$, denominator $= 0.01 \times 0.7953 = 0.007953$, ratio $= -4.27$, so $\Phi(-4.27) \approx 10^{-5}$.

    **At $t = 10$:** numerator $= -0.03993$, denominator $= 0.01 \times 0.99998 \approx 0.01$, ratio $= -3.99$, so $\Phi(-3.99) \approx 3.3 \times 10^{-5}$.

    **At $t = 50$:** numerator $\approx -0.04$, denominator $\approx 0.01$, ratio $= -4.0$, so $\Phi(-4.0) \approx 3.2 \times 10^{-5}$.

    As $t \to \infty$, the ratio converges to $-\theta/\sqrt{\sigma^2/(2\kappa)} = -0.04/0.01 = -4.0$, so the long-run probability is $\Phi(-4) \approx 3.2 \times 10^{-5}$.

    **Time to exceed 5%.** For $\mathbb{P}(r_t < 0) > 0.05$, we need $\Phi^{-1}(0.05) = -1.645$, i.e.,

    $$
    \frac{-m(t)}{\sqrt{v(t)}} > -1.645
    $$

    With these parameters, the ratio starts at $-\infty$ (when $v(0) = 0$) and decreases toward $-4.0$. Since $-4.0 < -1.645$, the probability **never exceeds 5%** for these parameter values. The mean ($\approx 4\%$) is always about 4 standard deviations ($\approx 1\%$) above zero.

    For the probability to exceed 5%, one would need $\theta/\sqrt{\sigma^2/(2\kappa)} < 1.645$, i.e., $\theta < 1.645\sigma/\sqrt{2\kappa}$. With $\sigma = 0.01$ and $\kappa = 0.5$: $\theta < 1.645 \times 0.01 \approx 0.01645$. So the 5% threshold would only be reached for $\theta < 1.645\%$.

    **Post-2015 perspective.** Between 2012 and 2022, several major economies (Eurozone, Japan, Switzerland, Sweden) experienced negative policy rates, with the ECB deposit rate reaching $-0.50\%$. This demonstrates that negative rates are not merely a mathematical artifact but an empirical reality. In this context, the Vasicek model's ability to produce negative rates is arguably a feature rather than a bug. The Gaussian framework correctly captures the possibility of negative rates while maintaining analytical tractability. For pricing in negative-rate environments, the Vasicek/Hull-White framework is often preferred over lognormal models (like Black-Karasinski), which cannot generate negative rates by construction.
