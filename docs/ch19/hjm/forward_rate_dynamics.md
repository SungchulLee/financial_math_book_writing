# Forward Rate Dynamics


The Heath–Jarrow–Morton (HJM) framework models the **entire forward rate curve** directly. Instead of specifying a short rate, HJM postulates dynamics for instantaneous forward rates.

---

## Instantaneous forward rates


Recall the instantaneous forward rate

$$
f(t,T) := -\partial_T \log P(t,T)
$$


so that

$$
P(t,T) = \exp\left(-\int_t^T f(t,u)\,du\right)
$$



In HJM, $f(t,T)$ for all maturities $T\ge t$ is the state variable.

---

## Stochastic dynamics


Under the risk-neutral measure, HJM postulates

$$
df(t,T) = \alpha(t,T)\,dt + \sum_{i=1}^n \sigma_i(t,T)\,dW_t^i
$$


where:

- $\sigma_i(t,T)$ are volatility functions,
- $W^i$ are Brownian motions,
- $\alpha(t,T)$ is the drift.

Crucially, the drift is *not arbitrary*.

---

## Interpretation


- Volatility structures determine how different maturities move together.
- The model is **infinite-dimensional** because $T$ is continuous.
- Short-rate and market models arise as special cases.

---

## Advantages of forward modeling


- Exact fit to the initial yield curve by construction.
- Transparent no-arbitrage conditions.
- Direct modeling of curve dynamics.

---

## Key takeaways


- HJM models forward rates directly.
- The entire yield curve is the state variable.
- Drift restrictions ensure no-arbitrage.

---

## Further reading


- Heath, Jarrow & Morton (1992).
- Filipović, *Term-Structure Models*.

---

## Exercises

**Exercise 1.** Given the initial forward rate curve $f(0, T) = 0.04 + 0.005\,T - 0.0002\,T^2$ for $T \in [0, 30]$, compute the initial zero-coupon bond prices $P(0, 5)$, $P(0, 10)$, and $P(0, 20)$ using the relation

$$
P(0, T) = \exp\!\left(-\int_0^T f(0, u)\,du\right)
$$

Verify that $P(0, T)$ is a decreasing function of $T$.

??? success "Solution to Exercise 1"

    We are given the initial forward rate curve $f(0, T) = 0.04 + 0.005\,T - 0.0002\,T^2$ and need to compute

    $$
    P(0, T) = \exp\!\left(-\int_0^T f(0, u)\,du\right)
    $$

    **Step 1: Compute the integral.**

    $$
    \int_0^T f(0, u)\,du = \int_0^T \bigl(0.04 + 0.005\,u - 0.0002\,u^2\bigr)\,du = 0.04\,T + 0.0025\,T^2 - \frac{0.0002}{3}\,T^3
    $$

    **Step 2: Evaluate at $T = 5$.**

    $$
    \int_0^5 f(0, u)\,du = 0.04(5) + 0.0025(25) - \frac{0.0002}{3}(125) = 0.2 + 0.0625 - 0.00833 = 0.25417
    $$

    $$
    P(0, 5) = e^{-0.25417} \approx 0.7757
    $$

    **Step 3: Evaluate at $T = 10$.**

    $$
    \int_0^{10} f(0, u)\,du = 0.04(10) + 0.0025(100) - \frac{0.0002}{3}(1000) = 0.4 + 0.25 - 0.06667 = 0.58333
    $$

    $$
    P(0, 10) = e^{-0.58333} \approx 0.5580
    $$

    **Step 4: Evaluate at $T = 20$.**

    $$
    \int_0^{20} f(0, u)\,du = 0.04(20) + 0.0025(400) - \frac{0.0002}{3}(8000) = 0.8 + 1.0 - 0.53333 = 1.26667
    $$

    $$
    P(0, 20) = e^{-1.26667} \approx 0.2817
    $$

    **Step 5: Verify that $P(0, T)$ is decreasing.**

    We have $P(0, 5) \approx 0.7757 > P(0, 10) \approx 0.5580 > P(0, 20) \approx 0.2817$. More generally,

    $$
    \frac{d}{dT} P(0, T) = -f(0, T)\,P(0, T)
    $$

    Since $f(0, T) = 0.04 + 0.005\,T - 0.0002\,T^2 > 0$ for $T \in [0, 30]$ (the discriminant of the quadratic shows $f(0, T) > 0$ on this interval) and $P(0, T) > 0$, we have $\frac{d}{dT} P(0, T) < 0$, confirming that $P(0, T)$ is strictly decreasing.

---

**Exercise 2.** In the one-factor HJM framework with constant volatility $\sigma(t, T) = \sigma_0$, write down the explicit dynamics $df(t, T)$ under the risk-neutral measure (including the drift determined by the no-arbitrage condition). Integrate the SDE to obtain $f(t, T)$ as a function of $f(0, T)$, $\sigma_0$, and the Brownian motion. Identify the resulting short-rate model.

??? success "Solution to Exercise 2"

    **Step 1: Determine the drift from the HJM no-arbitrage condition.**

    With constant volatility $\sigma(t, T) = \sigma_0$, the HJM drift condition gives

    $$
    \alpha(t, T) = \sigma_0 \int_t^T \sigma_0\,du = \sigma_0^2(T - t)
    $$

    **Step 2: Write the forward rate SDE.**

    $$
    df(t, T) = \sigma_0^2(T - t)\,dt + \sigma_0\,dW_t
    $$

    **Step 3: Integrate from 0 to $t$.**

    $$
    f(t, T) = f(0, T) + \int_0^t \sigma_0^2(T - s)\,ds + \sigma_0 W_t
    $$

    Evaluating the deterministic integral:

    $$
    \int_0^t \sigma_0^2(T - s)\,ds = \sigma_0^2 \left[Ts - \frac{s^2}{2}\right]_0^t = \sigma_0^2\left(Tt - \frac{t^2}{2}\right) = \sigma_0^2 t\left(T - \frac{t}{2}\right)
    $$

    Therefore:

    $$
    f(t, T) = f(0, T) + \sigma_0^2\,t\!\left(T - \frac{t}{2}\right) + \sigma_0\,W_t
    $$

    **Step 4: Identify the short-rate model.**

    Setting $T = t$:

    $$
    r_t = f(t, t) = f(0, t) + \frac{\sigma_0^2\,t^2}{2} + \sigma_0\,W_t
    $$

    The short rate is Gaussian with a deterministic drift $\theta(t) = f'(0, t) + \sigma_0^2\,t$ and diffusion $\sigma_0$, i.e., $dr_t = \theta(t)\,dt + \sigma_0\,dW_t$. This is the **Ho--Lee model**, the simplest HJM model with no mean reversion.

---

**Exercise 3.** Consider the forward rate volatility $\sigma(t, T) = \sigma_0\,e^{-\kappa(T-t)}$. Show that the short rate $r_t = f(t, t)$ satisfies a mean-reverting SDE and identify the mean-reversion speed $\kappa$. What well-known short-rate model does this volatility specification correspond to?

??? success "Solution to Exercise 3"

    **Step 1: Compute the HJM drift.**

    With $\sigma(t, T) = \sigma_0\,e^{-\kappa(T-t)}$, the drift condition gives

    $$
    \alpha(t, T) = \sigma_0\,e^{-\kappa(T-t)} \int_t^T \sigma_0\,e^{-\kappa(u-t)}\,du = \sigma_0^2\,e^{-\kappa(T-t)} \cdot \frac{1 - e^{-\kappa(T-t)}}{\kappa}
    $$

    **Step 2: Write and integrate the forward rate SDE.**

    $$
    f(t, T) = f(0, T) + \int_0^t \alpha(s, T)\,ds + \int_0^t \sigma_0\,e^{-\kappa(T-s)}\,dW_s
    $$

    **Step 3: Derive the short rate dynamics.** Setting $T = t$ in $df(t, T)$:

    $$
    r_t = f(t, t)
    $$

    Using the integrated form and differentiating (via Leibniz), or equivalently, applying the Musiela parameterization, one obtains:

    $$
    dr_t = \left[\frac{\partial f(0, t)}{\partial t} + \frac{\sigma_0^2}{2\kappa^2}\bigl(1 - e^{-\kappa t}\bigr)^2 + \kappa\bigl(f(0, t) - r_t\bigr) + \frac{\sigma_0^2}{2\kappa}\bigl(1 - e^{-2\kappa t}\bigr)\right]dt + \sigma_0\,dW_t
    $$

    More compactly, this can be written in the Hull--White form:

    $$
    dr_t = \bigl(\theta(t) - \kappa\,r_t\bigr)\,dt + \sigma_0\,dW_t
    $$

    where $\theta(t)$ is a deterministic function of the initial curve $f(0, \cdot)$ and the parameters $\sigma_0, \kappa$.

    The **mean-reversion speed is $\kappa$**, which is the same parameter appearing in the exponential decay of volatility. This model is the **Hull--White (extended Vasicek) model**. The exponential decay in the forward rate volatility directly translates to mean reversion in the short rate: faster decay ($\kappa$ larger) means stronger mean reversion.

---

**Exercise 4.** Explain why the HJM framework is said to be "infinite-dimensional," whereas short-rate models like Vasicek or CIR are finite-dimensional. In practical terms, what does infinite-dimensionality mean for the computational complexity of Monte Carlo simulation in HJM?

??? success "Solution to Exercise 4"

    **Infinite-dimensionality of HJM:**

    In the HJM framework, the state variable at each time $t$ is the **entire forward rate curve** $T \mapsto f(t, T)$ for all $T \geq t$. This is a function, which lives in a function space (typically $L^2[0, T_{\max}]$ or a weighted Sobolev space). A function has infinitely many degrees of freedom: specifying $f(t, T)$ requires its value at every maturity $T$ on a continuum. Hence the state space is infinite-dimensional.

    By contrast, short-rate models like Vasicek or CIR have a single state variable $r_t \in \mathbb{R}$. Given $r_t$, the entire forward curve $f(t, T)$ is determined by the closed-form bond pricing formula $P(t, T) = e^{A(T-t) - B(T-t)r_t}$. The state space is $\mathbb{R}$ (one-dimensional). Two-factor models live in $\mathbb{R}^2$.

    **Computational implications for Monte Carlo:**

    In a Monte Carlo simulation of HJM, at each time step one must evolve the forward rate $f(t_k, T_j)$ at **every maturity grid point** $T_j$. If the maturity axis is discretized into $N$ points:

    - Each time step requires $O(N)$ random updates (one for each maturity).
    - The drift at each maturity involves an integral $\int_t^{T_j} \sigma(t, u)\,du$, which costs $O(N)$ operations per maturity point, for a total of $O(N^2)$ per time step (or $O(N)$ if cumulative sums are used efficiently).
    - Total cost for $M$ time steps and $P$ paths: $O(P \cdot M \cdot N)$ at best, $O(P \cdot M \cdot N^2)$ at worst.

    For a short-rate model, each time step involves evolving a single scalar, costing $O(1)$ per step per path. This makes short-rate Monte Carlo dramatically cheaper, typically $O(P \cdot M)$.

    The infinite-dimensional nature of HJM therefore imposes a significant computational burden, which motivates the use of finite-factor approximations in practice.

---

**Exercise 5.** Starting from $P(t, T) = \exp\bigl(-\int_t^T f(t, u)\,du\bigr)$, verify that

$$
f(t, T) = -\frac{\partial}{\partial T}\log P(t, T)
$$

and that the short rate satisfies $r_t = f(t, t)$. If $P(t, T) = \exp(-a(T-t) - b(T-t)\,r_t)$ for some functions $a(\cdot)$ and $b(\cdot)$, express $f(t, T)$ in terms of $a'$, $b'$, and $r_t$.

??? success "Solution to Exercise 5"

    **Part 1: Verify $f(t, T) = -\partial_T \log P(t, T)$.**

    Starting from

    $$
    P(t, T) = \exp\!\left(-\int_t^T f(t, u)\,du\right)
    $$

    take the logarithm:

    $$
    \log P(t, T) = -\int_t^T f(t, u)\,du
    $$

    Differentiate with respect to $T$:

    $$
    \frac{\partial}{\partial T}\log P(t, T) = -f(t, T)
    $$

    by the fundamental theorem of calculus. Therefore $f(t, T) = -\frac{\partial}{\partial T}\log P(t, T)$. $\square$

    **Part 2: Verify $r_t = f(t, t)$.**

    By definition, the short rate is $r_t = \lim_{\Delta \to 0} \frac{-\log P(t, t+\Delta)}{\Delta}$. From the formula above,

    $$
    f(t, t) = -\frac{\partial}{\partial T}\log P(t, T)\Big|_{T=t}
    $$

    Since $\log P(t, T) = -\int_t^T f(t, u)\,du$, evaluating at $T = t$ gives $\log P(t, t) = 0$, and

    $$
    -\frac{\partial}{\partial T}\left(-\int_t^T f(t, u)\,du\right)\Big|_{T=t} = f(t, t)
    $$

    This is the instantaneous rate of return on the shortest bond, which is exactly the short rate $r_t$. $\square$

    **Part 3: Express $f(t, T)$ for affine bond prices.**

    Given $P(t, T) = \exp\bigl(-a(T-t) - b(T-t)\,r_t\bigr)$, let $\tau = T - t$. Then:

    $$
    \log P(t, T) = -a(\tau) - b(\tau)\,r_t
    $$

    Differentiating with respect to $T$ (noting $\partial \tau / \partial T = 1$):

    $$
    f(t, T) = -\frac{\partial}{\partial T}\bigl[-a(\tau) - b(\tau)\,r_t\bigr] = a'(\tau) + b'(\tau)\,r_t
    $$

    where $a'$ and $b'$ denote derivatives with respect to $\tau = T - t$. The forward rate is an **affine function of the short rate**, with slope $b'(\tau)$ and intercept $a'(\tau)$.

---

**Exercise 6.** A two-factor HJM model has volatilities $\sigma_1(t, T) = 0.01$ and $\sigma_2(t, T) = 0.008\,e^{-0.3(T-t)}$. The first factor represents parallel shifts and the second represents slope changes. Compute the instantaneous variance of the forward rate $f(t, T)$ as a function of $T - t$ and sketch its term structure. At what time-to-maturity is the variance maximized?

??? success "Solution to Exercise 6"

    **Step 1: Compute the instantaneous variance.**

    For a two-factor model, the instantaneous variance of $df(t, T)$ is

    $$
    \text{Var}(df(t, T)) = \bigl[\sigma_1(t, T)^2 + \sigma_2(t, T)^2\bigr]\,dt
    $$

    With $\sigma_1(t, T) = 0.01$ and $\sigma_2(t, T) = 0.008\,e^{-0.3(T-t)}$, let $\tau = T - t$:

    $$
    v(\tau) := \sigma_1^2 + \sigma_2^2\,e^{-0.6\tau} = (0.01)^2 + (0.008)^2\,e^{-0.6\tau} = 10^{-4} + 6.4 \times 10^{-5}\,e^{-0.6\tau}
    $$

    **Step 2: Analyze the term structure.**

    At $\tau = 0$: $v(0) = 10^{-4} + 6.4 \times 10^{-5} = 1.64 \times 10^{-4}$

    As $\tau \to \infty$: $v(\tau) \to 10^{-4}$

    The function $v(\tau) = 10^{-4} + 6.4 \times 10^{-5}\,e^{-0.6\tau}$ is strictly **decreasing** in $\tau$ since $\frac{dv}{d\tau} = -0.6 \times 6.4 \times 10^{-5}\,e^{-0.6\tau} < 0$.

    **Step 3: Identify the maximum.**

    Since $v(\tau)$ is strictly decreasing, the **variance is maximized at $\tau = 0$** (the shortest maturity), with maximum value $v(0) = 1.64 \times 10^{-4}$.

    **Step 4: Sketch description.**

    The term structure of instantaneous variance starts at $1.64 \times 10^{-4}$ for the shortest maturity and decays exponentially toward the asymptotic value $10^{-4}$ for long maturities. The decay is governed by $e^{-0.6\tau}$, so the second factor's contribution effectively vanishes beyond $\tau \approx 5$--$8$ years. The first factor (parallel shifts) contributes a constant floor $10^{-4}$ at all maturities.

---

**Exercise 7.** The forward rate $R(t, S, T)$ for the period $[S, T]$ is defined by $P(t, T) = P(t, S)\,e^{-R(t,S,T)(T-S)}$. Show that in the limit $S \to T$, $R(t, S, T)$ converges to the instantaneous forward rate $f(t, T)$. For finite $T - S$, express $R(t, S, T)$ as an average of instantaneous forward rates and discuss how a parallel shift in $f(t, \cdot)$ affects $R(t, S, T)$.

??? success "Solution to Exercise 7"

    **Part 1: Show $R(t, S, T) \to f(t, T)$ as $S \to T$.**

    From $P(t, T) = P(t, S)\,e^{-R(t,S,T)(T-S)}$, take logarithms:

    $$
    \log P(t, T) - \log P(t, S) = -R(t, S, T)(T - S)
    $$

    So

    $$
    R(t, S, T) = -\frac{\log P(t, T) - \log P(t, S)}{T - S}
    $$

    In the limit $S \to T$:

    $$
    \lim_{S \to T} R(t, S, T) = -\lim_{S \to T} \frac{\log P(t, T) - \log P(t, S)}{T - S} = -\frac{\partial}{\partial T}\log P(t, T) = f(t, T)
    $$

    by the definition of the derivative. $\square$

    **Part 2: Express $R(t, S, T)$ as an average.**

    Since $\log P(t, T) = -\int_t^T f(t, u)\,du$ and $\log P(t, S) = -\int_t^S f(t, u)\,du$:

    $$
    R(t, S, T) = -\frac{-\int_t^T f(t, u)\,du + \int_t^S f(t, u)\,du}{T - S} = \frac{\int_S^T f(t, u)\,du}{T - S}
    $$

    This shows that $R(t, S, T)$ is the **arithmetic average** of instantaneous forward rates over the period $[S, T]$.

    **Part 3: Effect of a parallel shift.**

    Suppose $f(t, u)$ is shifted to $f(t, u) + c$ for all $u$, where $c$ is a constant. Then:

    $$
    R_{\text{new}}(t, S, T) = \frac{\int_S^T [f(t, u) + c]\,du}{T - S} = \frac{\int_S^T f(t, u)\,du + c(T-S)}{T - S} = R(t, S, T) + c
    $$

    A **parallel shift** of $c$ in the instantaneous forward curve shifts every forward rate $R(t, S, T)$ by exactly $c$, regardless of the interval $[S, T]$. This is consistent with the "parallel shift" interpretation: all rates, whether instantaneous or discrete-tenor, move by the same amount.
