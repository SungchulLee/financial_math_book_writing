# Fokker-Planck for Financial Models

The Fokker-Planck equation describes the evolution of probability density functions for diffusion processes. It is the forward equation counterpart to the backward Kolmogorov equation and provides crucial insights into the probability distribution of asset prices under various financial models.

## Key Concepts

See [Kolmogorov Forward Equation](kolmogorov_forward.md) for the definition and
derivation of the Fokker-Planck equation, and
[Transition Densities for Standard SDEs](transition_densities_standard_sdes.md) for
explicit densities of BM, OU, GBM, and CIR. The present page focuses on
finance-specific interpretation, calibration, and risk applications.

**Finance-specific interpretations:**

- **Geometric Brownian Motion (GBM)**: the log-price is Gaussian, which underpins the
  Black-Scholes distribution of terminal stock prices.
- **Cox-Ingersoll-Ross (CIR)**: the transition density is non-central chi-square under
  suitable parameter conditions, enabling analytic bond pricing.
- **Mean-reverting processes (OU, CIR)**: stationary densities encode long-run
  behavior and are the starting point for calibration to historical distributions.

!!! note "Practical Significance"
    Fokker-Planck equations enable:

    - Analytical computation of option prices (no boundary conditions needed unlike PDEs)
    - Calibration of model parameters to observed density features
    - Risk management through understanding the distribution of future asset values
    - Construction of transition probability matrices for discrete approximations

For the forward-vs-backward duality, see
[Forward–Backward Duality](forward_backward_duality.md).

---

## Calibration and Risk Applications

This page focuses purely on **financial uses** of Fokker-Planck densities. Derivations of the underlying PDE and explicit transition densities live elsewhere; here we keep only the application layer.

Recall (see [§ Kolmogorov Forward Equation](kolmogorov_forward.md)): for $dX_t = \mu(X_t,t)\,dt + \sigma(X_t,t)\,dW_t$, the transition density satisfies $\partial_t p = \mathcal{L}^* p$.

Recall (see [§ Transition Densities for Standard SDEs](transition_densities_standard_sdes.md)): GBM has lognormal transition density; OU has Gaussian; CIR has scaled non-central $\chi^2$ with Gamma stationary law.

**Three uses of the density in finance:**

1. **Pricing**: $V(0, s_0) = e^{-rT}\int g(S)\,p^{\mathbb{Q}}(T, S \mid 0, s_0)\,dS$ — integrate the payoff against the risk-neutral density.
2. **Calibration**: fit model parameters by matching $p$ (or its moments / quantiles) to observed market densities, e.g. recovered from option implied volatilities via the Breeden–Litzenberger formula.
3. **Risk**: VaR, ES, and stress measures read off $p(\cdot, T \mid \cdot, 0)$ directly when the density is closed-form.

---

## Exercises

**Exercise 1.**
The Breeden-Litzenberger formula recovers the risk-neutral density from European call prices: $p^{\mathbb{Q}}(T, K \mid 0, s_0) = e^{rT}\partial_K^2 C(K, T)$. Explain why this density is exactly the terminal-time slice of the Fokker-Planck solution for the risk-neutral SDE $dS_t = rS_t\,dt + \sigma S_t\,dW_t$, and describe how a practitioner uses the recovered density to calibrate a local-volatility model.

??? success "Solution to Exercise 1"
    Under the risk-neutral measure, the call price is $C(K, T) = e^{-rT}\int_K^{\infty}(S - K)\,p^{\mathbb{Q}}(T, S \mid 0, s_0)\,dS$. Differentiating twice in $K$:

    $$
    \partial_K C = -e^{-rT}\int_K^{\infty} p^{\mathbb{Q}}\,dS, \qquad \partial_K^2 C = e^{-rT} p^{\mathbb{Q}}(T, K \mid 0, s_0)
    $$

    so $p^{\mathbb{Q}}(T, K \mid 0, s_0) = e^{rT}\partial_K^2 C(K, T)$. The density on the left is the terminal slice $t = T$ of the Fokker-Planck solution starting from $\delta(\cdot - s_0)$ at $t = 0$ under the risk-neutral SDE.

    **Calibration usage**: A practitioner reads $C(K, T)$ off the option chain, fits a smooth surface, and computes $\partial_K^2 C$ numerically. Inverting the Dupire formula $\sigma^2_{\text{loc}}(K, T) = \frac{2(\partial_T C + rK\partial_K C)}{K^2 \partial_K^2 C}$ yields the local-volatility function $\sigma_{\text{loc}}(S, t)$ that exactly reproduces the observed prices. Plugging $\sigma_{\text{loc}}$ into the SDE and solving the Fokker-Planck equation forward recovers the implied market densities at all maturities consistent with quoted vanillas.

---

**Exercise 2.**
A trader believes short rates follow the Vasicek model $dr_t = \kappa(\theta - r_t)\,dt + \sigma\,dW_t$. Using the OU stationary density $r_\infty \sim N(\theta, \sigma^2/(2\kappa))$, write down the 99% one-sided VaR for the long-run rate distribution. Explain why this Gaussian stationary density makes Vasicek unsuitable for nominal rates in a near-zero regime but acceptable for real rates or spreads.

??? success "Solution to Exercise 2"
    Recall (see [§ Transition Densities for Standard SDEs](transition_densities_standard_sdes.md)): the OU stationary law is $N(\theta, \sigma^2/(2\kappa))$.

    The 99% one-sided VaR (upper tail) for $r_\infty$ is the quantile $q_{0.99}$:

    $$
    q_{0.99} = \theta + \Phi^{-1}(0.99)\sqrt{\frac{\sigma^2}{2\kappa}} \approx \theta + 2.326\sqrt{\frac{\sigma^2}{2\kappa}}
    $$

    where $\Phi^{-1}$ is the inverse standard normal CDF.

    **Why Vasicek is unsuitable for nominal rates near zero**: A Gaussian stationary density places positive mass on $r < 0$. When the policy rate is already near zero, this implies a non-trivial probability of deeply negative nominal rates, contradicting the zero lower bound (or only modestly violated lower bound) observed empirically. For nominal rates a square-root model like CIR (Gamma stationary law on $[0,\infty)$) or a shadow-rate model is preferred.

    **Why it remains acceptable for real rates / spreads**: Real interest rates and credit spreads can legitimately go negative, so the Gaussian support of OU is not a liability there. The mean-reversion + closed-form Gaussian density still delivers analytic bond and swaption prices, which is why Vasicek-style dynamics survive in those applications.

---

**Exercise 3.**
Suppose stochastic variance follows the Heston dynamics $dv_t = \kappa(\theta - v_t)\,dt + \xi\sqrt{v_t}\,dW_t$ (CIR). The Feller condition $2\kappa\theta \geq \xi^2$ controls whether the variance can touch zero. State the financial consequence for option pricing if calibration produces parameters that violate Feller, and describe one numerical safeguard practitioners use when simulating Heston paths in that regime.

??? success "Solution to Exercise 3"
    Recall (see [§ Transition Densities for Standard SDEs](transition_densities_standard_sdes.md)): the CIR transition density behaves like $x^q$ near zero with $q = 2\kappa\theta/\xi^2 - 1$. When $2\kappa\theta < \xi^2$ (Feller violated), $q < 0$ and probability mass piles up near $v = 0$.

    **Financial consequence**: A variance process that visits zero with positive probability produces option-price surfaces with very flat implied-vol smiles for short maturities and instabilities in vega/vanna hedges. Vanilla call prices remain finite, but path-dependent derivatives (barriers, variance swaps, cliquets) become extremely sensitive to behaviour near $v = 0$, and the standard Heston characteristic-function pricer can experience branch-cut issues.

    **Numerical safeguard**: Practitioners use the **full truncation** or **reflection** scheme for Euler discretization of CIR: replace each negative simulated value of $v_t$ with $\max(v_t, 0)$ (or $|v_t|$) before computing the next increment. Better yet, use Andersen's QE scheme, which matches the first two moments of the exact non-central $\chi^2$ transition law and is unconditionally positivity-preserving — essential when Feller fails.

---

**Exercise 4.**
A risk manager wants to compute the 1-day 99% VaR of a stock position under GBM dynamics $dS_t = \mu S_t\,dt + \sigma S_t\,dW_t$. Using the lognormal transition density, derive a closed-form expression for the VaR of the loss $L = s_0 - S_{\Delta t}$ at horizon $\Delta t$.

??? success "Solution to Exercise 4"
    Recall (see [§ Transition Densities for Standard SDEs](transition_densities_standard_sdes.md)): under GBM, $\log(S_{\Delta t}/s_0) \sim N((\mu - \sigma^2/2)\Delta t,\, \sigma^2\Delta t)$.

    The 99% VaR of the loss is the level $L^*$ such that $\mathbb{P}(L > L^*) = 0.01$, i.e. $\mathbb{P}(S_{\Delta t} < s_0 - L^*) = 0.01$. Writing $S_{\Delta t} = s_0 \exp(Y)$ with $Y \sim N((\mu - \sigma^2/2)\Delta t, \sigma^2\Delta t)$:

    $$
    \mathbb{P}(S_{\Delta t} < s_0 - L^*) = \Phi\!\left(\frac{\ln(1 - L^*/s_0) - (\mu - \sigma^2/2)\Delta t}{\sigma\sqrt{\Delta t}}\right) = 0.01
    $$

    Solving:

    $$
    L^* = s_0\left[1 - \exp\!\left((\mu - \sigma^2/2)\Delta t + \sigma\sqrt{\Delta t}\,\Phi^{-1}(0.01)\right)\right]
    $$

    Since $\Phi^{-1}(0.01) \approx -2.326$, the exponent is negative, giving $L^* > 0$. For $\Delta t = 1$ day, $\mu \approx 0$, this simplifies to $L^* \approx s_0(1 - e^{-2.326\sigma\sqrt{\Delta t}}) \approx 2.326\,s_0\sigma\sqrt{\Delta t}$, which is the familiar parametric VaR formula.

---

**Exercise 5.**
For pricing a European call versus computing the terminal distribution of the underlying, which Kolmogorov equation is appropriate for each task? Connect the two via the identity $\mathbb{E}^{\mathbb{Q}}[g(S_T)] = \int g(S)\,p^{\mathbb{Q}}(T, S \mid 0, s_0)\,dS$ and explain the practitioner's preference in each setting.

??? success "Solution to Exercise 5"
    Recall (see [§ Forward–Backward Duality](forward_backward_duality.md)): the two approaches compute the same expectation but solve different PDEs.

    - **Pricing one payoff at many spots**: solve the backward PDE $\partial_t V + \mathcal{L}V - rV = 0$ with $V(T, S) = g(S)$; the value $V(0, \cdot)$ is read off at every spot $S_0$ from a single PDE solve. This is the Black-Scholes PDE — see [§ Kolmogorov Backward Equation](kolmogorov_backward.md).
    - **Many payoffs at one spot**: solve the forward PDE $\partial_t p = \mathcal{L}^* p$ with $p(0, \cdot) = \delta(\cdot - s_0)$ once, then integrate any payoff $g$ against $p(T, \cdot)$.

    For exotic books with hundreds of strikes on a single name, practitioners prefer the forward approach (build $p^{\mathbb{Q}}$ once, integrate many payoffs). For a delta/gamma book of a single vanilla across many underlyings, the backward approach is preferred (one PDE gives the price surface). The Breeden–Litzenberger inversion of Exercise 1 is the link: market quotes give the forward density, which can then re-price every payoff coherently.

---

**Exercise 6.**
Explain why a stationary distribution for OU exists but not for standard Brownian motion, in language a risk manager would use. Why does this distinction matter for choosing between a Vasicek-style model and a random-walk model when stress-testing a portfolio over multi-decade horizons?

??? success "Solution to Exercise 6"
    Recall (see [§ Kolmogorov Forward Equation](kolmogorov_forward.md)): a stationary density exists when $\mathcal{L}^* p_\infty = 0$ has an integrable solution.

    - **OU**: the mean-reverting drift $-\kappa(x - \theta)$ continuously pulls the process back toward $\theta$; long-run variance is capped at $\sigma^2/(2\kappa)$. A risk manager can quote a **steady-state distribution** for the variable — stress scenarios are bounded.
    - **Brownian motion**: no mean reversion; variance grows linearly in $t$. Over a 30-year horizon, the marginal distribution of $W_T$ has standard deviation $\sqrt{T}$ that swamps any starting value. There is no steady state — every percentile of the loss distribution diverges as $T$ grows.

    **Stress-testing consequence**: For variables that must remain economically bounded (real interest rates, FX deviations from PPP, credit spreads, vol-of-vol), choosing a random-walk specification will yield catastrophic-looking tail scenarios that are pure modeling artefacts. A mean-reverting Vasicek-style model gives stationary tail quantiles consistent with economic intuition and historical experience. Conversely, for quantities that are genuinely non-stationary (nominal price levels, cumulative wealth), a random-walk-with-drift specification is appropriate.
