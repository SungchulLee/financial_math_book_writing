# Bond Pricing via Feynman–Kac


An alternative and often more intuitive approach to bond pricing uses the **Feynman–Kac formula**, which expresses prices as expectations of discounted cashflows under the risk-neutral measure.

---

## Risk-neutral valuation


The fundamental pricing relation is

\[
P(t,T) = \mathbb{E}^{\mathbb{Q}}\left[
\exp\left(-\int_t^T r_s ds\right)
\middle| \mathcal{F}_t
\right].
\]



This holds for any arbitrage-free short-rate model under \(\mathbb{Q}\).

---

## Feynman–Kac theorem


The Feynman–Kac theorem states that the function

\[
u(t,r) = \mathbb{E}^{\mathbb{Q}}\left[
\exp\left(-\int_t^T r_s ds\right)
\middle| r_t=r
\right]
\]


is the unique solution to the bond pricing PDE with terminal condition \(u(T,r)=1\).

Thus:
- expectation formulation and PDE formulation are equivalent,
- the choice is one of perspective and convenience.

---

## Closed-form evaluation


For affine short-rate models:
- the integral \(\int_t^T r_s ds\) is Gaussian (Vasicek) or non-central chi-square (CIR),
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


- Bond prices are discounted expectations under \(\mathbb{Q}\).
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
P(t, T) = \mathbb{E}^{\mathbb{Q}}\!\left[\exp\!\left(-\int_t^T r_s\,ds\right)\;\middle|\;r_t\right],
$$

explain why the bond price has the exponential-affine form $P(t, T) = e^{A(\tau) - B(\tau)r_t}$ where $\tau = T - t$, and identify the functions $A(\tau)$ and $B(\tau)$.

---

**Exercise 2.** Verify the Feynman--Kac equivalence by checking that the function $u(t, r) = e^{A(T-t) - B(T-t)r}$ (the Vasicek bond price) satisfies the bond pricing PDE

$$
\partial_t u + \kappa(\theta - r)\,\partial_r u + \frac{1}{2}\sigma^2\,\partial_{rr} u - r\,u = 0
$$

with terminal condition $u(T, r) = 1$.

---

**Exercise 3.** For a short-rate model where $r_t$ is not affine (e.g., the Black--Karasinski model $d\ln r_t = \kappa(\theta(t) - \ln r_t)\,dt + \sigma\,dW_t$), closed-form bond prices are not available. Describe how Monte Carlo simulation based on the Feynman--Kac formula can be used to price a zero-coupon bond. What is the main source of error in this approach?

---

**Exercise 4.** A digital bond pays \$1 at $T$ if $r_T < K$ and \$0 otherwise. Express the digital bond price using the Feynman--Kac formula:

$$
V(t, r) = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_t^T r_s\,ds}\,\mathbf{1}_{\{r_T < K\}}\;\middle|\;r_t = r\right]
$$

Explain why this requires knowledge of the joint distribution of $\int_t^T r_s\,ds$ and $r_T$, not just the marginal distribution of $r_T$.

---

**Exercise 5.** Compare Monte Carlo pricing of a 10-year zero-coupon bond versus the closed-form Vasicek formula. Using $r_0 = 3\%$, $\kappa = 0.15$, $\theta = 4\%$, $\sigma = 1\%$, simulate 10,000 paths with monthly time steps. Compute the Monte Carlo estimate of $P(0, 10)$ and its standard error. How does the standard error compare to the precision needed for practical pricing?

---

**Exercise 6.** The Feynman--Kac theorem assumes certain regularity conditions on the coefficients of the SDE. Discuss what can go wrong when the volatility function $\sigma(t, r)$ is discontinuous or when the drift $\mu^{\mathbb{Q}}(t, r)$ grows too fast as $r \to \infty$. Give an example of a short-rate model where the Feynman--Kac theorem applies and one where additional care is needed.
