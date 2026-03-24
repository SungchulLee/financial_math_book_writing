# CEV Backbone and Boundary Behavior

The CEV (Constant Elasticity of Variance) backbone is the deterministic skeleton of the SABR model, obtained by setting the vol-of-vol $\nu = 0$. Understanding the CEV process is essential for two reasons: first, it determines how ATM implied volatility responds to changes in the forward level --- the so-called **backbone** --- which is the single most important feature for hedging; second, the boundary behavior at $F = 0$ for $\beta < 1$ raises subtle questions about absorption, probability mass, and the martingale property that directly affect option pricing. This section analyzes both aspects in detail.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Define the CEV process and identify it as the $\nu = 0$ limit of SABR
    2. Derive the backbone formula relating ATM implied volatility to the forward level
    3. Classify the boundary at $F = 0$ using Feller's boundary classification
    4. Explain the difference between absorption and reflection at zero
    5. Quantify the probability of the forward reaching zero and its pricing implications

---

## The CEV Process

### Definition

When the vol-of-vol vanishes ($\nu = 0$), the volatility $\sigma_t$ remains at its initial value $\alpha$ for all time, and the SABR system reduces to a single SDE:

$$
dF_t = \alpha F_t^{\beta}\,dW_t, \qquad F_0 > 0
$$

This is the **CEV model** introduced by Cox (1975). The parameter $\beta \in [0, 1]$ determines the elasticity of the local volatility function $\sigma_{\text{loc}}(F) = \alpha F^{\beta}$ with respect to the forward level.

The term "constant elasticity of variance" refers to the fact that the elasticity of the instantaneous variance $\alpha^2 F^{2\beta}$ with respect to $F$ is the constant $2\beta$:

$$
\frac{\partial \log(\alpha^2 F^{2\beta})}{\partial \log F} = 2\beta
$$

### Special Cases

The CEV model interpolates between two fundamental dynamics:

**Normal model** ($\beta = 0$): The forward follows arithmetic Brownian motion $dF_t = \alpha\,dW_t$. The local volatility is constant (independent of $F$). The forward can become negative, which is appropriate for interest rates in negative-rate environments. The transition density is Gaussian:

$$
F_T \sim \mathcal{N}(F_0,\, \alpha^2 T)
$$

**Lognormal model** ($\beta = 1$): The forward follows geometric Brownian motion $dF_t = \alpha F_t\,dW_t$. The local volatility is proportional to $F$, so percentage returns have constant volatility. The forward is strictly positive. The transition density is lognormal:

$$
\ln F_T \sim \mathcal{N}\!\left(\ln F_0 - \frac{\alpha^2}{2}T,\, \alpha^2 T\right)
$$

**Intermediate cases** ($0 < \beta < 1$): The local volatility $\alpha F^{\beta}$ increases with $F$ but less than proportionally. This produces a negative relationship between the forward level and the implied volatility --- a feature that helps generate skew even without stochastic volatility.

---

## The Backbone

### ATM Implied Volatility vs. Forward Level

The **backbone** of the SABR model describes how the ATM implied volatility changes as the forward moves. For the CEV model ($\nu = 0$), the Black implied volatility at the money is approximately:

$$
\sigma_{\text{ATM}}^{\text{Black}}(F) \approx \frac{\alpha}{F^{1-\beta}}
$$

This formula shows that:

- When $\beta = 1$: $\sigma_{\text{ATM}} = \alpha$, independent of $F$. The backbone is **flat**.
- When $\beta = 0$: $\sigma_{\text{ATM}} \approx \alpha / F$. The backbone is **steeply negative** --- ATM vol rises sharply as $F$ falls.
- When $0 < \beta < 1$: The backbone has an intermediate negative slope.

The backbone slope is:

$$
\frac{\partial \sigma_{\text{ATM}}}{\partial F} = -\frac{(1-\beta)\alpha}{F^{2-\beta}} < 0 \quad \text{for } \beta < 1
$$

!!! tip "Backbone and Delta Hedging"
    The backbone directly affects delta hedging. When a trader hedges a swaption using the SABR model, the delta depends on how the implied volatility moves with the forward. A model with the wrong backbone produces hedges that systematically over- or under-react to forward moves. This is the primary reason the SABR model displaced local volatility models in interest rate markets: SABR produces the correct backbone dynamics by construction.

### Normal Implied Volatility Backbone

For normal (Bachelier) implied volatility, the backbone relationship is:

$$
\sigma_{\text{ATM}}^{\text{Normal}}(F) \approx \alpha F^{\beta}
$$

This has the opposite sign convention:

- When $\beta = 0$: $\sigma_{\text{ATM}}^{\text{Normal}} = \alpha$, a flat backbone in normal vol
- When $\beta = 1$: $\sigma_{\text{ATM}}^{\text{Normal}} \approx \alpha F$, normal vol rises with $F$

The choice between Black and normal backbone interpretation depends on market conventions.

### Backbone in the Full SABR Model

In the full SABR model ($\nu > 0$), the backbone is modified by the stochastic volatility. The ATM Black implied volatility is approximately:

$$
\sigma_{\text{ATM}}^{\text{Black}}(F) \approx \frac{\alpha}{F^{1-\beta}}\left[1 + \left(\frac{(1-\beta)^2 \alpha^2}{24 F^{2(1-\beta)}} + \frac{\rho \beta \nu \alpha}{4 F^{1-\beta}} + \frac{2 - 3\rho^2}{24}\nu^2\right)T\right]
$$

The leading-order behavior $\alpha / F^{1-\beta}$ is still the CEV backbone, but the correction terms introduce dependence on $\rho$ and $\nu$. In practice, the backbone remains the dominant determinant of how ATM vol moves with the forward.

---

## Boundary Behavior at F = 0

### Why Boundaries Matter

For $\beta < 1$, the local volatility $\alpha F^{\beta} \to 0$ as $F \to 0$. This raises the question: can the forward actually reach zero in finite time? If so, what happens afterwards? These questions are not merely academic --- they directly affect:

- The martingale property of $F_t$ (and hence the no-arbitrage condition)
- The probability assigned to deep OTM puts
- The behavior of the transition density near $F = 0$

### Feller's Boundary Classification

The boundary behavior of the CEV process at $F = 0$ is determined by Feller's classification for one-dimensional diffusions. For the SDE $dF = \alpha F^{\beta}\,dW$, the relevant quantities are the **scale function** $s(F)$ and the **speed measure** $m(F)$.

For $F > 0$, the scale function satisfies $s'(F) = \text{const}$ (since there is no drift), so:

$$
s(F) = F
$$

The speed measure density is:

$$
m(F) = \frac{1}{\alpha^2 F^{2\beta}}
$$

The boundary at $F = 0$ is classified by the integrability of these functions near zero.

!!! info "Theorem: Boundary Classification for CEV"
    For the CEV process $dF = \alpha F^{\beta}\,dW$ with $F > 0$:

    1. If $\beta \geq 1$: The boundary $F = 0$ is **not attainable**. The forward never reaches zero.
    2. If $1/2 \leq \beta < 1$: The boundary $F = 0$ is **attainable** and is an **exit boundary**. The forward can reach zero in finite time with positive probability, and once there, it is absorbed.
    3. If $0 \leq \beta < 1/2$: The boundary $F = 0$ is **attainable** and is a **regular boundary**. A boundary condition must be specified (absorbing or reflecting).

**Proof sketch.** The classification depends on the integrals:

$$
\int_0^{\epsilon} s(x)\,m(x)\,dx = \int_0^{\epsilon} \frac{x}{\alpha^2 x^{2\beta}}\,dx = \frac{1}{\alpha^2}\int_0^{\epsilon} x^{1-2\beta}\,dx
$$

This integral converges if and only if $1 - 2\beta > -1$, i.e., $\beta < 1$. Convergence means the boundary is attainable. The distinction between exit and regular boundaries depends on further integrability conditions involving the scale function alone:

$$
\int_0^{\epsilon} s(x)\,dx = \int_0^{\epsilon} x\,dx < \infty \quad \text{always}
$$

For $\beta \geq 1/2$, the speed measure integral $\int_0^{\epsilon} m(x)\,dx$ diverges, making the boundary an exit (absorbing) boundary. For $\beta < 1/2$, both integrals converge, giving a regular boundary where absorption or reflection must be specified. $\square$

### Probability of Absorption

When $\beta < 1$ and an absorbing boundary is imposed at $F = 0$, there is a positive probability that the forward reaches zero before maturity $T$. Let $p_0(T)$ denote this absorption probability. For the CEV process, the exact formula involves the complementary non-central chi-squared distribution:

$$
p_0(T) = \Phi_{\chi^2}\!\left(x_0;\, \delta,\, \lambda\right)
$$

where $\Phi_{\chi^2}$ is the CDF of the non-central chi-squared distribution with:

$$
\delta = \frac{1}{1 - \beta}, \qquad \lambda = \frac{F_0^{2(1-\beta)}}{(1-\beta)^2 \alpha^2 T}, \qquad x_0 = 0
$$

Key properties of the absorption probability:

- $p_0(T) \to 0$ as $T \to 0$ (short maturities: negligible)
- $p_0(T) \to 1$ as $T \to \infty$ (long maturities: absorption is certain)
- $p_0(T)$ increases as $\beta$ decreases (lower $\beta$ makes absorption more likely)
- $p_0(T)$ increases as $\alpha$ increases (higher volatility drives $F$ toward zero faster)

!!! warning "Probability Mass Leakage"
    When absorption occurs, the expected value $\mathbb{E}[F_T]$ is strictly less than $F_0$, because some paths are absorbed at zero. This means $F_t$ is a **strict local martingale** rather than a true martingale. The "missing" probability mass is:

    $$
    F_0 - \mathbb{E}[F_T] = F_0 \cdot p_0(T) \cdot \frac{\mathbb{E}[F_T \mid F_T = 0]}{F_0}
    $$

    In practice, this mass leakage is small for typical SABR parameters and maturities up to 10 years, but it becomes significant for very low forwards, high volatility, or very long maturities. The arbitrage-free SABR extensions (discussed in a later section) address this issue.

### CEV Transition Density

The transition density of the CEV process with an absorbing boundary at zero can be expressed in terms of **modified Bessel functions**. For $\beta < 1$, let $p = 1/(2(1-\beta))$ and define the transformed variables:

$$
u = \frac{F_0^{2(1-\beta)}}{2(1-\beta)^2 \alpha^2 T}, \qquad v = \frac{F_T^{2(1-\beta)}}{2(1-\beta)^2 \alpha^2 T}
$$

Then the transition density is:

$$
p(F_T, T \mid F_0) = \frac{F_T^{-2\beta}}{(1-\beta)\alpha^2 T} \left(\frac{v}{u}\right)^{p/2} \exp\!\left(-(u+v)\right) I_p\!\left(2\sqrt{uv}\right)
$$

where $I_p$ is the modified Bessel function of the first kind of order $p$.

This density has a **point mass at zero** (from absorption) plus a continuous part on $(0, \infty)$.

---

## Practical Implications

### Choice of Beta and Market Conventions

The choice of $\beta$ has direct consequences for model behavior:

| $\beta$ | Boundary at 0 | Backbone | Market Convention |
|---------|----------------|----------|-------------------|
| 0 | $F$ can go negative | Flat (normal vol) | EUR, JPY swaptions |
| 0.5 | Absorbing | Moderate | Traditional rates |
| 1 | Not attainable | Flat (Black vol) | Equity, FX |

### Impact on Put Pricing

For deep OTM puts (low strikes), the boundary behavior matters significantly:

- With $\beta < 1$ and absorption, the put price includes a contribution from the probability mass at $F = 0$
- The CEV put price at strike $K$ with absorption is:

$$
P_{\text{CEV}}(K) = K \cdot p_0(T) + P_{\text{cont}}(K)
$$

where $P_{\text{cont}}(K)$ is the contribution from the continuous part of the density. The first term represents the payoff from paths absorbed at zero.

---

## Summary

The CEV backbone, defined by the relationship $\sigma_{\text{ATM}} \approx \alpha / F^{1-\beta}$, is the dominant feature controlling how the SABR smile moves with the forward level. The parameter $\beta$ determines both this backbone slope and the boundary behavior at $F = 0$: for $\beta < 1$, the forward can be absorbed at zero with positive probability, creating probability mass leakage that reduces $\mathbb{E}[F_T]$ below $F_0$. The boundary classification follows from Feller's theory, and the transition density involves modified Bessel functions. These analytical properties inform the choice of $\beta$ in practice and motivate the arbitrage-free extensions developed in subsequent sections.

---

## Further Reading

- Cox, J. C. (1975). *Notes on option pricing I: Constant elasticity of variance diffusions*. Unpublished note, Stanford University.
- Schroder, M. (1989). *Computing the constant elasticity of variance option pricing formula*. Journal of Finance, 44(1), 211--219.
- Hagan, P. et al. (2002). *Managing smile risk*. Wilmott Magazine, 1, 84--108.
- Andersen, L. & Piterbarg, V. (2010). *Interest Rate Modeling*, Volume I. Atlantic Financial Press.

---

## Exercises

**Exercise 1.** For the CEV process $dF_t = \alpha F_t^\beta\,dW_t$ with $\beta = 0.5$, $\alpha = 0.04$, and $F_0 = 0.03$, compute the local volatility $\sigma_{\text{loc}}(F) = \alpha F^{0.5}$ at $F = 0.01, 0.03, 0.05$. Verify that the elasticity of the instantaneous variance with respect to $F$ is the constant $2\beta = 1$.

---

**Exercise 2.** The backbone formula $\sigma_{\text{ATM}} \approx \alpha/F^{1-\beta}$ predicts how ATM implied volatility changes with the forward. For $\alpha = 0.04$, plot (or compute) $\sigma_{\text{ATM}}$ as a function of $F \in [0.01, 0.05]$ for $\beta = 0, 0.5, 1.0$. Which $\beta$ produces the steepest response? Explain why the backbone contributes to the skew even when $\rho = 0$.

---

**Exercise 3.** Using Feller's boundary classification, the boundary at $F = 0$ is absorbing for $\beta < 1$ and unattainable for $\beta \geq 1$. Explain intuitively why: as $F \to 0$, the diffusion coefficient $\alpha F^\beta$ vanishes, but the drift is zero. For $\beta = 0.5$, is the "pull" from the diffusion toward zero strong enough to reach it? Compare with $\beta = 0$ (normal model) where $F = 0$ is attained with positive probability.

---

**Exercise 4.** The probability of absorption at zero for the CEV process has important pricing implications: if $\mathbb{P}(F_T = 0) = p > 0$, then $\mathbb{E}[F_T] = F_0(1-p) < F_0$ (mass leakage). For a European put with strike $K$, the put price includes a contribution $Ke^{-rT}\mathbb{P}(F_T = 0)$ from the absorbed mass. Explain why ignoring absorption leads to systematic underpricing of deep OTM puts.

---

**Exercise 5.** Compare the CEV model ($\nu = 0$) with the full SABR model ($\nu > 0$). The CEV model produces skew through the backbone but no smile curvature. Show that for $\beta = 0.5$, $\alpha = 0.04$, $F = 0.03$, the CEV implied volatility is a monotonically decreasing function of strike $K$ when $\beta < 1$. Explain why adding stochastic volatility ($\nu > 0$) is necessary to produce curvature (both wings lifting).

---

**Exercise 6.** The scaling property of SABR states that if $(F_t, \sigma_t)$ is a solution with forward $F_0$ and initial vol $\alpha$, then $(\lambda F_t, \lambda^{1-\beta}\sigma_t)$ is a solution with forward $\lambda F_0$ and vol $\lambda^{1-\beta}\alpha$. Verify this by substituting into the SDE. What does this imply about the implied volatility smile as a function of log-moneyness $\ln(K/F)$?
