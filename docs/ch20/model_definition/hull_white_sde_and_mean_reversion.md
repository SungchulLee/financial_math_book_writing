# Hull-White SDE and Mean Reversion

The Hull-White model (1990) is the most widely used short-rate model in practice for pricing interest rate derivatives. Its central innovation over the earlier Vasicek model is the introduction of a time-dependent drift function $\theta(t)$ that allows the model to exactly match the initial term structure of interest rates observed in the market. The model retains the analytical tractability of the Ornstein-Uhlenbeck process while gaining the flexibility needed for consistent derivative pricing. This section defines the model, interprets its parameters, and establishes the fundamental properties of mean reversion.

!!! info "Prerequisites"
    - Stochastic calculus: Ito processes, stochastic differential equations
    - Ornstein-Uhlenbeck process and its properties (Chapter 15)
    - Term structure basics: zero-coupon bonds, yield curves, forward rates
    - Vasicek model fundamentals (Chapter 18)

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. State the Hull-White SDE and identify each parameter
    2. Explain the role of $\theta(t)$ in fitting the initial term structure
    3. Interpret the mean-reversion speed $a$ and compute the half-life
    4. Solve the SDE explicitly using the integrating factor method
    5. Characterize the conditional distribution of the short rate

---

## The Hull-White SDE

The Hull-White model specifies the dynamics of the instantaneous short rate $r_t$ under the risk-neutral measure $\mathbb{Q}$.

!!! note "Definition: Hull-White Model"
    The **Hull-White model** (also called the extended Vasicek model) is defined by the stochastic differential equation

    $$
    dr_t = \bigl[\theta(t) - a\, r_t\bigr]\, dt + \sigma\, dW_t^{\mathbb{Q}}
    $$

    where:

    - $r_t$ is the instantaneous short rate at time $t$
    - $\theta(t)$ is a deterministic, time-dependent drift function
    - $a > 0$ is the constant mean-reversion speed
    - $\sigma > 0$ is the constant instantaneous volatility
    - $W_t^{\mathbb{Q}}$ is a standard Brownian motion under $\mathbb{Q}$

The SDE can be rewritten in the equivalent form

$$
dr_t = a\!\left[\frac{\theta(t)}{a} - r_t\right] dt + \sigma\, dW_t^{\mathbb{Q}}
$$

which reveals the structure more clearly: the short rate is pulled toward the time-dependent level $\theta(t)/a$ at speed $a$. This "target" level changes over time, which is precisely what allows the model to reproduce the market-observed term structure.

---

## Interpretation of Parameters

Each parameter in the Hull-White SDE has a direct financial interpretation.

**The drift function** $\theta(t)$ absorbs all the information from the initial yield curve. It is not a free parameter to be estimated but is determined analytically by requiring that the model price of every zero-coupon bond at time zero matches the market price. Explicitly,

$$
\theta(t) = \frac{\partial f(0,t)}{\partial t} + a\, f(0,t) + \frac{\sigma^2}{2a}\bigl(1 - e^{-2at}\bigr)
$$

where $f(0,t)$ is the market instantaneous forward rate at time zero for maturity $t$. This formula is derived in the section on fitting $\theta(t)$ to the yield curve.

**The mean-reversion speed** $a$ controls how quickly the short rate reverts to its time-dependent target. A larger $a$ means faster reversion and hence less persistent deviations from the target. The parameter $a$ is typically estimated from market volatility data (caps or swaptions) and plays a key role in determining the decorrelation between short-term and long-term rates.

**The volatility** $\sigma$ scales the magnitude of random fluctuations in the short rate. It is constant in the basic Hull-White model, though extensions allow $\sigma = \sigma(t)$ to be piecewise constant for better calibration to the volatility term structure.

---

## Mean Reversion and the Half-Life

The mean-reversion mechanism is the defining qualitative feature of the Hull-White model. To build intuition, consider the deterministic part of the SDE (set $\sigma = 0$):

$$
\frac{dr_t}{dt} = \theta(t) - a\, r_t
$$

When $r_t$ is above $\theta(t)/a$, the drift is negative, pushing the rate downward. When $r_t$ is below $\theta(t)/a$, the drift is positive, pulling the rate upward. The strength of this restoring force is proportional to the displacement and to $a$.

!!! note "Definition: Half-Life of Mean Reversion"
    The **half-life** of mean reversion is the time required for the deterministic component of a displacement from the target level to decay by half:

    $$
    t_{1/2} = \frac{\ln 2}{a}
    $$

???+ note "Derivation"
    Consider a displacement $\delta_t = r_t - \theta(t)/a$ from the time-dependent mean level. In the deterministic case ($\sigma = 0$, with $\theta$ approximately constant over short horizons), the displacement satisfies

    $$
    \frac{d\delta_t}{dt} = -a\, \delta_t
    $$

    which has the solution $\delta_t = \delta_0 \, e^{-at}$. Setting $|\delta_t| = |\delta_0|/2$ and solving gives

    $$
    e^{-a t_{1/2}} = \frac{1}{2} \quad \Longrightarrow \quad t_{1/2} = \frac{\ln 2}{a}
    $$

    $\square$

!!! example "Numerical Example: Half-Life"
    For typical market calibrations:

    | Mean-reversion speed $a$ | Half-life $t_{1/2}$ |
    |:---:|:---:|
    | $0.01$ | $69.3$ years |
    | $0.05$ | $13.9$ years |
    | $0.10$ | $6.9$ years |
    | $0.20$ | $3.5$ years |
    | $0.50$ | $1.4$ years |

    Market estimates of $a$ typically fall in the range $0.01$ to $0.10$, implying half-lives of 7 to 70 years. This slow mean reversion is consistent with the observed persistence of interest rate levels.

---

## Explicit Solution via Integrating Factor

The Hull-White SDE is a linear SDE and can be solved explicitly using the integrating factor technique.

!!! note "Theorem: Explicit Solution of the Hull-White SDE"
    The solution of the Hull-White SDE with initial condition $r_s$ at time $s$ is

    $$
    r_t = r_s\, e^{-a(t-s)} + \int_s^t e^{-a(t-u)}\, \theta(u)\, du + \sigma \int_s^t e^{-a(t-u)}\, dW_u^{\mathbb{Q}}
    $$

    for all $t \geq s$.

???+ note "Proof"
    Define the process $Y_t = r_t\, e^{at}$. By the product rule (Ito's formula with $Y_t = r_t \cdot e^{at}$, noting $e^{at}$ is deterministic):

    $$
    dY_t = e^{at}\, dr_t + a\, e^{at}\, r_t\, dt
    $$

    Substituting the Hull-White SDE $dr_t = [\theta(t) - a\, r_t]\, dt + \sigma\, dW_t^{\mathbb{Q}}$:

    $$
    dY_t = e^{at}\bigl[\theta(t) - a\, r_t\bigr]\, dt + \sigma\, e^{at}\, dW_t^{\mathbb{Q}} + a\, e^{at}\, r_t\, dt = \theta(t)\, e^{at}\, dt + \sigma\, e^{at}\, dW_t^{\mathbb{Q}}
    $$

    The $-a\, r_t$ and $+a\, r_t$ terms cancel, leaving a simple expression. Integrating from $s$ to $t$:

    $$
    Y_t - Y_s = \int_s^t \theta(u)\, e^{au}\, du + \sigma \int_s^t e^{au}\, dW_u^{\mathbb{Q}}
    $$

    Since $Y_t = r_t\, e^{at}$ and $Y_s = r_s\, e^{as}$, dividing both sides by $e^{at}$:

    $$
    r_t = r_s\, e^{-a(t-s)} + \int_s^t e^{-a(t-u)}\, \theta(u)\, du + \sigma \int_s^t e^{-a(t-u)}\, dW_u^{\mathbb{Q}}
    $$

    $\square$

The solution has a clear three-part structure:

1. **Decay of initial condition**: $r_s\, e^{-a(t-s)}$ shows the initial rate decaying exponentially toward zero at rate $a$
2. **Deterministic drift integral**: $\int_s^t e^{-a(t-u)}\, \theta(u)\, du$ accumulates the effect of $\theta(u)$ with exponential weighting, giving more weight to recent values
3. **Stochastic integral**: $\sigma \int_s^t e^{-a(t-u)}\, dW_u^{\mathbb{Q}}$ is a Gaussian random variable representing the accumulated effect of volatility shocks

---

## Conditional Distribution

Since the stochastic integral in the solution is a Gaussian random variable (it is an Ito integral of a deterministic function), the conditional distribution of $r_t$ given $\mathcal{F}_s$ is fully characterized by its mean and variance.

!!! note "Theorem: Conditional Distribution of the Short Rate"
    Under the Hull-White model, $r_t$ conditional on $\mathcal{F}_s$ is normally distributed:

    $$
    r_t \mid \mathcal{F}_s \sim \mathcal{N}\!\left(\mu(s,t),\; \Sigma^2(s,t)\right)
    $$

    where the conditional mean and variance are

    $$
    \mu(s,t) = r_s\, e^{-a(t-s)} + \int_s^t e^{-a(t-u)}\, \theta(u)\, du
    $$

    $$
    \Sigma^2(s,t) = \frac{\sigma^2}{2a}\bigl(1 - e^{-2a(t-s)}\bigr)
    $$

???+ note "Proof"
    The conditional mean follows immediately from the explicit solution by taking expectations conditional on $\mathcal{F}_s$:

    $$
    \mathbb{E}^{\mathbb{Q}}[r_t \mid \mathcal{F}_s] = r_s\, e^{-a(t-s)} + \int_s^t e^{-a(t-u)}\, \theta(u)\, du
    $$

    since $\mathbb{E}^{\mathbb{Q}}\!\left[\int_s^t e^{-a(t-u)}\, dW_u^{\mathbb{Q}} \,\Big|\, \mathcal{F}_s\right] = 0$.

    For the variance, apply the Ito isometry:

    $$
    \Sigma^2(s,t) = \sigma^2 \int_s^t e^{-2a(t-u)}\, du = \sigma^2 \left[-\frac{1}{2a}\, e^{-2a(t-u)}\right]_{u=s}^{u=t} = \frac{\sigma^2}{2a}\bigl(1 - e^{-2a(t-s)}\bigr)
    $$

    Since the stochastic integral $\sigma \int_s^t e^{-a(t-u)}\, dW_u^{\mathbb{Q}}$ is a Gaussian random variable (as a stochastic integral of a deterministic integrand against Brownian motion), the conditional distribution is fully Gaussian. $\square$

---

## Asymptotic Behavior of the Variance

The conditional variance $\Sigma^2(s,t) = \frac{\sigma^2}{2a}(1 - e^{-2a(t-s)})$ exhibits two important limiting behaviors.

**Short-time limit.** For $t - s \ll 1/a$, a Taylor expansion gives

$$
\Sigma^2(s,t) = \frac{\sigma^2}{2a}\bigl(1 - e^{-2a(t-s)}\bigr) \approx \frac{\sigma^2}{2a} \cdot 2a(t-s) = \sigma^2(t-s)
$$

which recovers the variance of a Brownian motion with diffusion coefficient $\sigma$. Over short time horizons, mean reversion has negligible effect, and the short rate behaves like arithmetic Brownian motion.

**Long-time limit.** As $t - s \to \infty$:

$$
\Sigma^2(s,t) \to \frac{\sigma^2}{2a}
$$

The variance saturates at $\sigma^2/(2a)$, the stationary variance of the Ornstein-Uhlenbeck process. Mean reversion prevents the variance from growing without bound, unlike in models without mean reversion (such as the Ho-Lee model) where $\text{Var}(r_t) = \sigma^2 t \to \infty$.

!!! warning "Gaussian Limitation"
    Because $r_t$ is normally distributed, the Hull-White model assigns positive probability to negative interest rates. Specifically,

    $$
    \mathbb{P}(r_t < 0 \mid \mathcal{F}_s) = \Phi\!\left(\frac{-\mu(s,t)}{\Sigma(s,t)}\right)
    $$

    where $\Phi$ is the standard normal CDF. For typical parameter values and moderate horizons, this probability is small but nonzero. The Black-Karasinski model $d\ln r_t = [\theta(t) - a \ln r_t]\, dt + \sigma\, dW_t$ addresses this at the cost of losing closed-form bond prices.

---

## The Ornstein-Uhlenbeck Connection

The Hull-White model is a time-inhomogeneous Ornstein-Uhlenbeck (OU) process. The classical OU process

$$
dX_t = -a\, X_t\, dt + \sigma\, dW_t
$$

has a constant long-run mean of zero. The Hull-White model generalizes this by introducing the time-dependent function $\theta(t)$ that shifts the mean level continuously. The decomposition

$$
r_t = \psi(t) + \tilde{r}_t
$$

where $\psi(t) = \mathbb{E}^{\mathbb{Q}}[r_t \mid \mathcal{F}_0]$ is the deterministic conditional mean and $\tilde{r}_t = r_t - \psi(t)$ is the zero-mean stochastic residual, makes this relationship explicit. The residual $\tilde{r}_t$ satisfies the standard OU process

$$
d\tilde{r}_t = -a\, \tilde{r}_t\, dt + \sigma\, dW_t^{\mathbb{Q}}, \quad \tilde{r}_0 = 0
$$

so all the distributional properties of the Hull-White short rate follow from those of the classical OU process, shifted by the deterministic function $\psi(t)$. This decomposition is developed fully in the section on short rate decomposition.

---

## Summary

The Hull-White model $dr_t = [\theta(t) - ar_t]\, dt + \sigma\, dW_t^{\mathbb{Q}}$ is a time-inhomogeneous Ornstein-Uhlenbeck process whose key parameters are the mean-reversion speed $a$, the volatility $\sigma$, and the drift function $\theta(t)$ determined by the initial term structure. The explicit solution via the integrating factor shows the short rate as a sum of a decaying initial condition, a deterministic drift integral, and a Gaussian stochastic integral. The conditional distribution is normal with variance $\sigma^2(1 - e^{-2a\tau})/(2a)$ that saturates at $\sigma^2/(2a)$ for large $\tau$, and the half-life of mean reversion is $\ln 2 / a$. These properties form the foundation for all subsequent derivations of bond prices, option formulas, and calibration procedures in the Hull-White framework.

---

## Exercises

**Exercise 1.** For a mean-reversion speed $a = 0.07$, compute the half-life of mean reversion. If the short rate is currently 200 basis points above its target level, how long does it take for the deterministic displacement to fall below 50 basis points?

??? success "Solution to Exercise 1"
    The half-life of mean reversion is

    $$
    t_{1/2} = \frac{\ln 2}{a} = \frac{\ln 2}{0.07} = \frac{0.6931}{0.07} \approx 9.90 \text{ years}
    $$

    For the deterministic displacement, the decay follows $\delta_t = \delta_0 \, e^{-at}$, where $\delta_0 = 200$ bps. We need the time $t^*$ such that $\delta_{t^*} = 50$ bps:

    $$
    200 \, e^{-0.07 t^*} = 50 \implies e^{-0.07 t^*} = \frac{1}{4} \implies t^* = \frac{\ln 4}{0.07} = \frac{2 \ln 2}{0.07} \approx 19.80 \text{ years}
    $$

    This is exactly twice the half-life, which makes sense: falling from 200 to 50 bps requires two halvings (200 to 100, then 100 to 50).

---

**Exercise 2.** Verify the explicit solution of the Hull-White SDE by substituting $r_t = r_s e^{-a(t-s)} + \int_s^t e^{-a(t-u)}\theta(u)\,du + \sigma\int_s^t e^{-a(t-u)}dW_u^{\mathbb{Q}}$ back into the SDE $dr_t = [\theta(t) - ar_t]\,dt + \sigma\,dW_t^{\mathbb{Q}}$ and confirming that both sides match.

??? success "Solution to Exercise 2"
    Starting from the explicit solution

    $$
    r_t = r_s e^{-a(t-s)} + \int_s^t e^{-a(t-u)}\theta(u)\,du + \sigma\int_s^t e^{-a(t-u)}dW_u^{\mathbb{Q}}
    $$

    we compute $dr_t$ by differentiating each term with respect to $t$.

    **Term 1:** $\frac{d}{dt}\bigl[r_s e^{-a(t-s)}\bigr] = -a\, r_s e^{-a(t-s)}$

    **Term 2:** Using the Leibniz rule for the integral $\int_s^t e^{-a(t-u)}\theta(u)\,du$:

    $$
    \frac{d}{dt}\int_s^t e^{-a(t-u)}\theta(u)\,du = e^{-a(t-t)}\theta(t) + \int_s^t (-a)e^{-a(t-u)}\theta(u)\,du = \theta(t) - a\int_s^t e^{-a(t-u)}\theta(u)\,du
    $$

    **Term 3:** By the Leibniz-Ito rule for the stochastic integral $\sigma\int_s^t e^{-a(t-u)}dW_u$:

    $$
    d\!\left[\sigma\int_s^t e^{-a(t-u)}dW_u\right] = -a\sigma\int_s^t e^{-a(t-u)}dW_u\,dt + \sigma\,dW_t
    $$

    Combining all three contributions:

    $$
    dr_t = \left[-a\,r_s e^{-a(t-s)} + \theta(t) - a\int_s^t e^{-a(t-u)}\theta(u)\,du - a\sigma\int_s^t e^{-a(t-u)}dW_u\right]dt + \sigma\,dW_t
    $$

    The bracketed expression equals $\theta(t) - a\bigl[r_s e^{-a(t-s)} + \int_s^t e^{-a(t-u)}\theta(u)\,du + \sigma\int_s^t e^{-a(t-u)}dW_u\bigr] = \theta(t) - a\,r_t$. Therefore

    $$
    dr_t = [\theta(t) - a\,r_t]\,dt + \sigma\,dW_t^{\mathbb{Q}}
    $$

    which is exactly the Hull-White SDE.

---

**Exercise 3.** Compute the conditional variance $\Sigma^2(0, t)$ for $a = 0.05$ and $\sigma = 0.01$ at $t = 1, 5, 10, 50$. Verify that the short-time approximation $\Sigma^2 \approx \sigma^2 t$ is accurate for $t = 1$ and that the long-time limit $\sigma^2/(2a)$ is nearly reached by $t = 50$.

??? success "Solution to Exercise 3"
    The conditional variance is $\Sigma^2(0,t) = \frac{\sigma^2}{2a}(1 - e^{-2at})$ with $a = 0.05$ and $\sigma = 0.01$.

    First compute the exact values and the short-time approximation $\sigma^2 t = 0.0001\,t$, as well as the long-time limit $\sigma^2/(2a) = 0.0001/0.10 = 0.001$:

    **At $t = 1$:**

    $$
    \Sigma^2(0,1) = \frac{0.0001}{0.10}(1 - e^{-0.10}) = 0.001 \times (1 - 0.9048) = 0.001 \times 0.09516 = 9.516 \times 10^{-5}
    $$

    Short-time approximation: $\sigma^2 t = 0.0001 \times 1 = 1.000 \times 10^{-4}$. The relative error is $(1.000 - 0.9516)/0.9516 \approx 5.1\%$, reasonably accurate.

    **At $t = 5$:**

    $$
    \Sigma^2(0,5) = 0.001 \times (1 - e^{-0.50}) = 0.001 \times 0.3935 = 3.935 \times 10^{-4}
    $$

    **At $t = 10$:**

    $$
    \Sigma^2(0,10) = 0.001 \times (1 - e^{-1.0}) = 0.001 \times 0.6321 = 6.321 \times 10^{-4}
    $$

    **At $t = 50$:**

    $$
    \Sigma^2(0,50) = 0.001 \times (1 - e^{-5.0}) = 0.001 \times 0.99326 = 9.933 \times 10^{-4}
    $$

    The long-time limit is $\sigma^2/(2a) = 1.000 \times 10^{-3}$. At $t = 50$, the variance has reached $99.3\%$ of this limit, confirming saturation.

    | $t$ | $\Sigma^2(0,t)$ (exact) | $\sigma^2 t$ (approx) | $\sigma^2/(2a)$ (limit) |
    |:---:|:---:|:---:|:---:|
    | 1 | $9.52 \times 10^{-5}$ | $1.00 \times 10^{-4}$ | $1.00 \times 10^{-3}$ |
    | 5 | $3.94 \times 10^{-4}$ | $5.00 \times 10^{-4}$ | $1.00 \times 10^{-3}$ |
    | 10 | $6.32 \times 10^{-4}$ | $1.00 \times 10^{-3}$ | $1.00 \times 10^{-3}$ |
    | 50 | $9.93 \times 10^{-4}$ | $5.00 \times 10^{-3}$ | $1.00 \times 10^{-3}$ |

---

**Exercise 4.** The Hull-White model allows negative interest rates. For $\mu(0, 10) = 0.03$ and $\Sigma(0, 10) = 0.02$, compute $\mathbb{P}(r_{10} < 0)$. Discuss whether this probability is acceptable for practical applications.

??? success "Solution to Exercise 4"
    Given $\mu(0,10) = 0.03$ and $\Sigma(0,10) = 0.02$, we compute

    $$
    \mathbb{P}(r_{10} < 0) = \Phi\!\left(\frac{-\mu(0,10)}{\Sigma(0,10)}\right) = \Phi\!\left(\frac{-0.03}{0.02}\right) = \Phi(-1.5)
    $$

    From the standard normal table, $\Phi(-1.5) = 0.0668$, so there is approximately a $6.68\%$ probability of negative rates at the 10-year horizon.

    **Discussion.** A $6.68\%$ probability of negative rates is non-negligible and could be problematic in several contexts:

    - For pricing instruments like caps (which are out-of-the-money when rates are low), this probability directly affects option values.
    - In risk management, a model that assigns nearly 7% probability to negative rates may overstate the likelihood of extreme downward rate scenarios.
    - However, in the post-2008 environment, negative rates have been observed in practice (e.g., European government bonds, Swiss franc LIBOR), so this "defect" may actually be a desirable feature.

    For applications where rate positivity is critical (e.g., modeling emerging market rates at high levels where negative rates are implausible), the Black-Karasinski model or shifted Hull-White model $dr_t = [\theta(t) - a(r_t + \phi)]\,dt + \sigma\,dW_t$ with a shift $\phi$ may be more appropriate.

---

**Exercise 5.** Show that the three-part structure of the Hull-White solution (decaying initial condition, deterministic drift integral, stochastic integral) simplifies to $r_t = \theta_\infty + (r_s - \theta_\infty)e^{-a(t-s)} + \sigma\int_s^t e^{-a(t-u)}dW_u$ when $\theta(t) = a\theta_\infty$ is constant. Identify this as the Vasicek solution.

??? success "Solution to Exercise 5"
    When $\theta(t) = a\theta_\infty$ is constant, the deterministic drift integral becomes

    $$
    \int_s^t e^{-a(t-u)} \theta(u)\,du = a\theta_\infty \int_s^t e^{-a(t-u)}\,du
    $$

    Evaluate the integral:

    $$
    a\theta_\infty \int_s^t e^{-a(t-u)}\,du = a\theta_\infty \left[\frac{1}{a}e^{-a(t-u)}\right]_{u=s}^{u=t} = \theta_\infty\bigl(1 - e^{-a(t-s)}\bigr)
    $$

    Substituting into the three-part solution:

    $$
    r_t = r_s e^{-a(t-s)} + \theta_\infty(1 - e^{-a(t-s)}) + \sigma\int_s^t e^{-a(t-u)}dW_u
    $$

    Rearranging:

    $$
    r_t = \theta_\infty + (r_s - \theta_\infty)e^{-a(t-s)} + \sigma\int_s^t e^{-a(t-u)}dW_u
    $$

    This is exactly the Vasicek solution. The short rate reverts to the constant level $\theta_\infty$ with the initial displacement $(r_s - \theta_\infty)$ decaying at rate $a$, plus a Gaussian stochastic integral. The three-part structure collapses: the "decay of initial condition" and "deterministic drift integral" combine into the familiar $\theta_\infty + (r_s - \theta_\infty)e^{-a(t-s)}$ form of the Ornstein-Uhlenbeck process with constant mean.

---

**Exercise 6.** Derive the conditional covariance $\text{Cov}(r_t, r_s)$ for $t > s > 0$ in the Hull-White model. Show that $\text{Cov}(r_t, r_s) = \frac{\sigma^2}{2a}e^{-a(t-s)}(1 - e^{-2as})$ and interpret the exponential decay with $|t - s|$.

??? success "Solution to Exercise 6"
    Using the explicit solution with $s = 0$:

    $$
    r_t = r_0 e^{-at} + \int_0^t e^{-a(t-u)}\theta(u)\,du + \sigma\int_0^t e^{-a(t-u)}dW_u
    $$

    $$
    r_s = r_0 e^{-as} + \int_0^s e^{-a(s-u)}\theta(u)\,du + \sigma\int_0^s e^{-a(s-u)}dW_u
    $$

    The covariance $\text{Cov}(r_t, r_s)$ arises only from the stochastic integrals (the deterministic parts do not contribute to covariance). For $t > s$:

    $$
    \text{Cov}(r_t, r_s) = \sigma^2\,\text{Cov}\!\left(\int_0^t e^{-a(t-u)}dW_u,\;\int_0^s e^{-a(s-u)}dW_u\right)
    $$

    By the Ito isometry, since both integrals share the common interval $[0, s]$:

    $$
    \text{Cov}(r_t, r_s) = \sigma^2 \int_0^s e^{-a(t-u)} e^{-a(s-u)}\,du = \sigma^2 e^{-a(t+s)} \int_0^s e^{2au}\,du
    $$

    Evaluating the integral:

    $$
    \int_0^s e^{2au}\,du = \frac{e^{2as} - 1}{2a}
    $$

    Therefore:

    $$
    \text{Cov}(r_t, r_s) = \sigma^2 e^{-a(t+s)} \cdot \frac{e^{2as} - 1}{2a} = \frac{\sigma^2}{2a} e^{-a(t-s)}(1 - e^{-2as})
    $$

    **Interpretation.** The covariance has two factors:

    - $e^{-a(t-s)}$: exponential decay with the time separation $|t-s|$, reflecting the fading memory of the mean-reverting process. Rates far apart in time are weakly correlated.
    - $(1 - e^{-2as})$: a factor that grows from 0 (at $s=0$) toward 1 (as $s \to \infty$), reflecting the build-up of stochastic variability from the initial condition. When $s$ is large, this factor saturates and $\text{Cov}(r_t, r_s) \approx \frac{\sigma^2}{2a} e^{-a(t-s)}$, the covariance of the stationary OU process.

---

**Exercise 7.** The Black-Karasinski model $d\ln r_t = [\theta(t) - a\ln r_t]\,dt + \sigma\,dW_t$ guarantees positive rates. Explain what analytical tractability is lost compared to the Hull-White model, and under what market conditions the Gaussian limitation of Hull-White becomes problematic.

??? success "Solution to Exercise 7"
    **Analytical tractability lost in Black-Karasinski:**

    The Black-Karasinski model $d\ln r_t = [\theta(t) - a\ln r_t]\,dt + \sigma\,dW_t$ is an OU process for $x_t = \ln r_t$, so $x_t$ is Gaussian. However, $r_t = e^{x_t}$ is log-normally distributed. This nonlinear transformation destroys the affine structure:

    1. **No closed-form bond prices.** The bond price $P(t,T) = \mathbb{E}^{\mathbb{Q}}[e^{-\int_t^T r_s\,ds}] = \mathbb{E}^{\mathbb{Q}}[e^{-\int_t^T e^{x_s}\,ds}]$ involves the exponential of a Gaussian integral, which does not admit a closed-form solution. Bond prices must be computed numerically (trees or PDEs).

    2. **No affine bond price formula.** Since $P(t,T)$ is not of the form $e^{A(t,T) + B(t,T)r_t}$, there are no Riccati ODEs, and yields are not linear in $r_t$.

    3. **No Black-Scholes-type option formulas.** Without log-normal bond price ratios, bond options, caps, and swaptions require numerical methods. Jamshidian's trick still applies (bond prices are monotone in $r_t$), but each zero-coupon bond option requires numerical pricing.

    4. **Calibration is slower.** Every evaluation of the objective function in calibration requires a numerical solve, making calibration significantly more expensive.

    **When the Gaussian limitation becomes problematic:**

    - In a high-rate environment with steep term structure, the probability of negative rates under Hull-White is negligible, and the model works well.
    - In a low-rate environment (rates near zero, such as post-2008 or the 2020s in many developed economies), the Gaussian distribution assigns significant probability mass to negative rates, distorting option prices and hedge ratios for floors and low-strike caps.
    - For long-horizon simulations (e.g., insurance liabilities with 30+ year horizons), the accumulated probability of negative rates can become substantial.
    - When pricing instruments with payoffs that are sensitive to rate positivity (e.g., mortgage-backed securities, certain structured notes), the Hull-White model's Gaussian limitation may lead to mispricing.
