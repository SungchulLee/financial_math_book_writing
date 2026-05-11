# Bond Pricing via Feynman–Kac


An alternative and often more intuitive approach to bond pricing uses the **Feynman–Kac formula**, which expresses prices as expectations of discounted cashflows under the risk-neutral measure.

---

## Risk-neutral valuation


The fundamental pricing relation is

$$
P(t,T) = \mathbb{E}^{\mathbb{Q}}\left[
\exp\left(-\int_t^T r_s ds\right)
\middle| \mathcal{F}_t
\right]
$$



This holds for any arbitrage-free short-rate model under $\mathbb{Q}$.

---

## Feynman–Kac theorem


The Feynman–Kac theorem states that the function

$$
u(t,r) = \mathbb{E}^{\mathbb{Q}}\left[
\exp\left(-\int_t^T r_s ds\right)
\middle| r_t=r
\right]
$$


is the unique solution to the bond pricing PDE with terminal condition $u(T,r)=1$.

Thus:

- expectation formulation and PDE formulation are equivalent,
- the choice is one of perspective and convenience.

---

## Closed-form evaluation


For affine short-rate models:

- the integral $\int_t^T r_s ds$ is Gaussian (Vasicek) or non-central chi-square (CIR),
- expectations can be computed analytically,
- results coincide with exponential-affine formulas.

---

## Monte Carlo interpretation


The Feynman–Kac form enables:

- Monte Carlo pricing of bonds,
- simulation-based pricing of IR derivatives,
- easy extension to path-dependent payoffs.

However, Monte Carlo is usually inefficient for plain bonds compared to closed forms.

---

## Key takeaways


- Bond prices are discounted expectations under $\mathbb{Q}$.
- Feynman–Kac links PDEs and probabilistic pricing.
- Monte Carlo follows naturally from this view.

---

## Further reading


- Karatzas & Shreve, *Brownian Motion and Stochastic Calculus*.
- Björk, *Arbitrage Theory in Continuous Time*.

---

## Exercises

**Exercise 1.** In the Vasicek model, $dr_t = \kappa(\theta - r_t)\,dt + \sigma\,dW_t^{\mathbb{Q}}$, the short rate $r_t$ is Gaussian with conditional mean $\mathbb{E}[r_s | r_t] = \theta + (r_t - \theta)e^{-\kappa(s-t)}$ and conditional variance $\text{Var}(r_s | r_t) = \frac{\sigma^2}{2\kappa}(1 - e^{-2\kappa(s-t)})$. Using the Feynman--Kac representation

$$
P(t, T) = \mathbb{E}^{\mathbb{Q}}\!\left[\exp\!\left(-\int_t^T r_s\,ds\right)\;\middle|\;r_t\right]
$$

explain why the bond price has the exponential-affine form $P(t, T) = e^{A(\tau) - B(\tau)r_t}$ where $\tau = T - t$, and identify the functions $A(\tau)$ and $B(\tau)$.

??? success "Solution to Exercise 1"

    In the Vasicek model, $r_t$ is an Ornstein--Uhlenbeck process, so $r_s$ for $s \in [t,T]$ is jointly Gaussian given $r_t$. The integral $\int_t^T r_s\,ds$ is a linear functional of the Gaussian process $\{r_s\}_{s \in [t,T]}$, hence it is also Gaussian.

    **Computing the integral's mean and variance:**

    The conditional mean of the integral is:

    $$
    \mathbb{E}\!\left[\int_t^T r_s\,ds \;\middle|\; r_t\right] = \int_t^T \mathbb{E}[r_s | r_t]\,ds = \int_t^T \left[\theta + (r_t - \theta)e^{-\kappa(s-t)}\right]ds
    $$

    $$
    = \theta\tau + (r_t - \theta)\frac{1 - e^{-\kappa\tau}}{\kappa} = \theta\tau + (r_t - \theta)B(\tau)
    $$

    where $\tau = T - t$ and $B(\tau) = (1 - e^{-\kappa\tau})/\kappa$.

    Since $\int_t^T r_s\,ds$ is Gaussian with mean $m$ and some variance $v^2$, the moment generating function gives:

    $$
    P(t,T) = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_t^T r_s\,ds} \;\middle|\; r_t\right] = e^{-m + v^2/2}
    $$

    The mean $m$ is linear in $r_t$: $m = \theta\tau + (r_t - \theta)B(\tau) = (\theta\tau - \theta B(\tau)) + B(\tau)r_t$.

    Therefore $P(t,T) = \exp\!\left[-(\theta\tau - \theta B(\tau)) - B(\tau)r_t + v^2/2\right] = e^{A(\tau) - B(\tau)r_t}$, which is exponential-affine in $r_t$.

    The functions are:

    $$
    B(\tau) = \frac{1 - e^{-\kappa\tau}}{\kappa}
    $$

    $$
    A(\tau) = -\theta\tau + \theta B(\tau) + \frac{v^2}{2} = \left(\theta - \frac{\sigma^2}{2\kappa^2}\right)(B(\tau) - \tau) - \frac{\sigma^2}{4\kappa}B(\tau)^2
    $$

    where the last equality follows after computing $v^2 = \text{Var}\!\left(\int_t^T r_s\,ds\right)$ explicitly using the Vasicek covariance structure:

    $$
    v^2 = \frac{\sigma^2}{\kappa^2}\left[\tau - 2B(\tau) + \frac{1 - e^{-2\kappa\tau}}{2\kappa}\right]
    $$

---

**Exercise 2.** Verify the Feynman--Kac equivalence by checking that the function $u(t, r) = e^{A(T-t) - B(T-t)r}$ (the Vasicek bond price) satisfies the bond pricing PDE

$$
\partial_t u + \kappa(\theta - r)\,\partial_r u + \frac{1}{2}\sigma^2\,\partial_{rr} u - r\,u = 0
$$

with terminal condition $u(T, r) = 1$.

??? success "Solution to Exercise 2"

    Let $u(t,r) = e^{A(\tau) - B(\tau)r}$ with $\tau = T - t$. We verify it satisfies the PDE.

    **Partial derivatives:**

    Since $\tau = T - t$, we have $\partial_t \tau = -1$.

    $$
    \partial_t u = (-A'(\tau) + B'(\tau)r)\,u
    $$

    where $A' = dA/d\tau$ and $B' = dB/d\tau$ (the negative sign from $\partial_t\tau = -1$ applied to the chain rule: $\partial_t u = (-A' + B'r)u$).

    $$
    \partial_r u = -B(\tau)\,u, \qquad \partial_{rr}u = B(\tau)^2\,u
    $$

    **Substituting into the PDE:**

    $$
    (-A' + B'r)u + \kappa(\theta - r)(-B)u + \tfrac{1}{2}\sigma^2 B^2 u - ru = 0
    $$

    Dividing by $u$ (which is positive):

    $$
    -A' + B'r - \kappa\theta B + \kappa Br + \tfrac{1}{2}\sigma^2 B^2 - r = 0
    $$

    Collecting the coefficient of $r$:

    $$
    r(B' + \kappa B - 1) + (-A' - \kappa\theta B + \tfrac{1}{2}\sigma^2 B^2) = 0
    $$

    **Coefficient of $r$:** $B'(\tau) + \kappa B(\tau) - 1 = 0$. With $B(\tau) = (1-e^{-\kappa\tau})/\kappa$, we get $B'(\tau) = e^{-\kappa\tau}$, and $e^{-\kappa\tau} + \kappa \cdot (1-e^{-\kappa\tau})/\kappa - 1 = e^{-\kappa\tau} + 1 - e^{-\kappa\tau} - 1 = 0$. Verified.

    **Constant term:** $A'(\tau) = -\kappa\theta B(\tau) + \frac{1}{2}\sigma^2 B(\tau)^2$. This is the ODE that defines $A(\tau)$, so it is satisfied by construction.

    **Terminal condition:** At $\tau = 0$: $A(0) = 0$, $B(0) = 0$, so $u(T,r) = e^0 = 1$. Verified.

    This confirms the Feynman--Kac equivalence: the probabilistic formula and the PDE produce the same bond price.

---

**Exercise 3.** For a short-rate model where $r_t$ is not affine (e.g., the Black--Karasinski model $d\ln r_t = \kappa(\theta(t) - \ln r_t)\,dt + \sigma\,dW_t$), closed-form bond prices are not available. Describe how Monte Carlo simulation based on the Feynman--Kac formula can be used to price a zero-coupon bond. What is the main source of error in this approach?

??? success "Solution to Exercise 3"

    In the Black--Karasinski model, $\ln r_t$ follows an OU process:

    $$
    d\ln r_t = \kappa(\theta(t) - \ln r_t)\,dt + \sigma\,dW_t
    $$

    Since $r_t = e^{\ln r_t}$ is the exponential of a Gaussian process, the integral $\int_t^T r_s\,ds = \int_t^T e^{\ln r_s}\,ds$ is an integral of a log-normal process, which does not have a closed-form distribution. The bond price $P(t,T) = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_t^T r_s\,ds}\right]$ therefore has no analytical formula.

    **Monte Carlo procedure:**

    1. **Discretize time:** Choose a grid $t = t_0 < t_1 < \cdots < t_M = T$ with step $\Delta t_j = t_{j+1} - t_j$.
    2. **Simulate paths of $x_t = \ln r_t$:** For each path $i = 1, \ldots, N$:

        $$
        x_{j+1}^{(i)} = x_j^{(i)} + \kappa(\theta(t_j) - x_j^{(i)})\Delta t_j + \sigma\sqrt{\Delta t_j}\,Z_j^{(i)}
        $$

        where $Z_j^{(i)} \sim N(0,1)$ are independent standard normals.

    3. **Recover $r$:** Set $r_j^{(i)} = e^{x_j^{(i)}}$.
    4. **Approximate the integral** using the trapezoidal rule or rectangle rule:

        $$
        I^{(i)} = \sum_{j=0}^{M-1} r_j^{(i)} \Delta t_j
        $$

    5. **Estimate the bond price:**

        $$
        \hat{P}(t,T) = \frac{1}{N}\sum_{i=1}^{N} e^{-I^{(i)}}
        $$

    **Main sources of error:**

    - **Discretization bias:** The Euler scheme introduces bias of order $O(\Delta t)$. Since $\ln r_t$ is an OU process, the exact transition distribution is known and can be used for exact simulation of $x_t$, reducing this to pure time-integration error.
    - **Statistical (sampling) error:** The Monte Carlo estimator has standard error $\sigma_{\hat{P}}/\sqrt{N}$, where $\sigma_{\hat{P}}$ is the standard deviation of $e^{-I}$. This decreases slowly as $1/\sqrt{N}$.
    - **Time-integration error:** The numerical quadrature of $\int_t^T r_s\,ds$ introduces error even with exact path simulation; this is typically $O(\Delta t^2)$ for the trapezoidal rule.

    The discretization bias is often the dominant error for bond pricing because the exponential discounting amplifies errors in the integral.

---

**Exercise 4.** A digital bond pays \$1 at $T$ if $r_T < K$ and \$0 otherwise. Express the digital bond price using the Feynman--Kac formula:

$$
V(t, r) = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_t^T r_s\,ds}\,\mathbf{1}_{\{r_T < K\}}\;\middle|\;r_t = r\right]
$$

Explain why this requires knowledge of the joint distribution of $\int_t^T r_s\,ds$ and $r_T$, not just the marginal distribution of $r_T$.

??? success "Solution to Exercise 4"

    The digital bond price is:

    $$
    V(t,r) = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_t^T r_s\,ds}\,\mathbf{1}_{\{r_T < K\}} \;\middle|\; r_t = r\right]
    $$

    This expectation involves both the integral $\int_t^T r_s\,ds$ (through the discounting factor) and the terminal value $r_T$ (through the indicator). These two quantities are **not independent** --- knowing $r_T$ tells us something about the path of $r_s$ and hence about $\int_t^T r_s\,ds$.

    **Why the joint distribution is needed:**

    If $\int_t^T r_s\,ds$ and $r_T$ were independent, we could factor the expectation:

    $$
    V(t,r) = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_t^T r_s\,ds}\right] \cdot \mathbb{Q}(r_T < K | r_t = r)
    $$

    But they are correlated. In the Vasicek model, for instance, both $\int_t^T r_s\,ds$ and $r_T$ are jointly Gaussian (as linear functionals of the Gaussian process $\{r_s\}$), with a specific covariance structure. The expectation becomes:

    $$
    V(t,r) = \int_{-\infty}^{K} \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_t^T r_s\,ds} \;\middle|\; r_T = \rho, r_t = r\right] f_{r_T|r_t}(\rho)\,d\rho
    $$

    The conditional expectation inside the integral depends on the joint law of $(r_T, \int_t^T r_s\,ds)$, not just the marginal of $r_T$.

    In the Vasicek model, the joint distribution is bivariate normal, and the digital bond price can be computed using the bivariate normal CDF. In non-Gaussian models (e.g., CIR), the joint distribution is more complex, and numerical methods (Monte Carlo or PDE) are typically required.

---

**Exercise 5.** Compare Monte Carlo pricing of a 10-year zero-coupon bond versus the closed-form Vasicek formula. Using $r_0 = 3\%$, $\kappa = 0.15$, $\theta = 4\%$, $\sigma = 1\%$, simulate 10,000 paths with monthly time steps. Compute the Monte Carlo estimate of $P(0, 10)$ and its standard error. How does the standard error compare to the precision needed for practical pricing?

??? success "Solution to Exercise 5"

    **Parameters:** $r_0 = 0.03$, $\kappa = 0.15$, $\theta = 0.04$, $\sigma = 0.01$, $T = 10$.

    **Exact Vasicek price:**

    $$
    B(10) = \frac{1 - e^{-0.15 \times 10}}{0.15} = \frac{1 - e^{-1.5}}{0.15} = \frac{1 - 0.22313}{0.15} = \frac{0.77687}{0.15} = 5.17911
    $$

    $$
    A(10) = \left(0.04 - \frac{0.01^2}{2 \times 0.15^2}\right)(5.17911 - 10) - \frac{0.01^2}{4 \times 0.15}(5.17911)^2
    $$

    $$
    = \left(0.04 - 0.002222\right)(-4.82089) - \frac{0.0001}{0.6}(26.8232)
    $$

    $$
    = 0.037778 \times (-4.82089) - 0.004471 = -0.18209 - 0.004471 = -0.18656
    $$

    $$
    P_{\text{exact}} = e^{A(10) - B(10) \times 0.03} = e^{-0.18656 - 0.15537} = e^{-0.34194} = 0.71034
    $$

    **Monte Carlo simulation:**

    With monthly time steps ($\Delta t = 1/12$) over 10 years ($M = 120$ steps), simulate $N = 10{,}000$ paths using the exact OU transition:

    $$
    r_{j+1} = \theta + (r_j - \theta)e^{-\kappa\Delta t} + \sigma\sqrt{\frac{1 - e^{-2\kappa\Delta t}}{2\kappa}}\,Z_j
    $$

    For each path, compute $I^{(i)} = \sum_{j=0}^{119} r_j^{(i)}\Delta t$ (rectangle rule) and $\hat{P}^{(i)} = e^{-I^{(i)}}$.

    The Monte Carlo estimate is $\hat{P} = \frac{1}{N}\sum_i \hat{P}^{(i)}$.

    **Standard error estimate:** The standard deviation of $e^{-I}$ is approximately $\text{Std}(I) \cdot P$ for small relative variations. With $\text{Var}(I)$ computable from the Vasicek covariance, a rough estimate gives $\text{Std}(e^{-I}) \approx 0.05$. The standard error is then:

    $$
    \text{SE} = \frac{0.05}{\sqrt{10{,}000}} = 0.0005
    $$

    This corresponds to about 5 basis points on the bond price ($\approx 0.07\%$ relative error).

    **Practical precision:** For pricing purposes, precision of 0.01% to 0.1% is typically needed. The standard error of 0.05 (about 7 bps relative) is marginal. To achieve precision of 0.01% ($\approx 0.07$ basis points), one would need $N \approx 10^6$ to $10^7$ paths. This illustrates why Monte Carlo is inefficient for plain bond pricing --- the closed form gives exact answers instantly.

---

**Exercise 6.** The Feynman--Kac theorem assumes certain regularity conditions on the coefficients of the SDE. Discuss what can go wrong when the volatility function $\sigma(t, r)$ is discontinuous or when the drift $\mu^{\mathbb{Q}}(t, r)$ grows too fast as $r \to \infty$. Give an example of a short-rate model where the Feynman--Kac theorem applies and one where additional care is needed.

??? success "Solution to Exercise 6"

    The Feynman--Kac theorem requires the following regularity conditions on the SDE $dr_t = \mu^{\mathbb{Q}}(t,r_t)\,dt + \sigma(t,r_t)\,dW_t$:

    1. **Lipschitz continuity** of $\mu^{\mathbb{Q}}$ and $\sigma$ in $r$: ensures existence and uniqueness of the SDE solution.
    2. **Linear growth condition**: $|\mu^{\mathbb{Q}}(t,r)| + |\sigma(t,r)| \leq C(1 + |r|)$ for some constant $C$, ensuring the solution does not explode in finite time.
    3. **Polynomial growth of the terminal condition**: the payoff function (here $g(r) = 1$) grows at most polynomially.
    4. **The solution $u(t,r)$ to the PDE must satisfy a growth condition** (at most polynomial in $r$).

    **When $\sigma(t,r)$ is discontinuous:**

    - The SDE may fail to have a unique strong solution. Weak existence may still hold (by Stroock--Varadhan theory) under milder conditions, but uniqueness becomes delicate.
    - The PDE becomes degenerate or has discontinuous coefficients, and classical solutions may not exist. One must work with viscosity solutions.
    - The Feynman--Kac link may still hold in a generalized sense (via viscosity solution theory), but the standard theorem does not directly apply.

    **When $\mu^{\mathbb{Q}}(t,r)$ grows too fast:**

    - If the drift grows super-linearly (e.g., $\mu \sim r^2$), the SDE solution may explode in finite time (reach infinity). In this case, the Feynman--Kac representation breaks down because the process is not well-defined on $[t,T]$.
    - Even if the process does not explode, fast-growing drift can cause the expectation $\mathbb{E}[e^{-\int_t^T r_s\,ds}]$ to be non-finite or the PDE solution to fail the growth condition.

    **Example where Feynman--Kac applies:** The Vasicek model, $dr_t = \kappa(\theta - r_t)\,dt + \sigma\,dW_t$. Both drift and diffusion are Lipschitz and satisfy the linear growth condition. The solution is Gaussian with bounded moments. The theorem applies directly.

    **Example where additional care is needed:** The CIR model, $dr_t = \kappa(\theta - r_t)\,dt + \sigma\sqrt{r_t}\,dW_t$. The diffusion $\sigma\sqrt{r}$ is not Lipschitz at $r = 0$ (its derivative blows up). The standard Feynman--Kac theorem does not directly apply. However, the SDE still has a unique strong solution (by the Yamada--Watanabe theorem for Holder-$1/2$ diffusions), and the Feynman--Kac link can be established by more careful analysis, using the fact that the boundary at $r = 0$ is either inaccessible (Feller condition) or reflecting.
