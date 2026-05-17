# The Hull-White Model

The **Hull-White model** (1990) extends Vasicek by introducing a time-dependent drift that enables **exact calibration to the initial yield curve**. This makes it the workhorse model for interest rate derivatives in practice.

Under the risk-neutral measure $\mathbb{Q}$:

$$
dr_t = [\theta(t) - \kappa r_t] \, dt + \sigma \, dW_t^{\mathbb{Q}}
$$

**Key difference from Vasicek:** the drift function $\theta(t)$ is time-dependent, chosen to fit the market term structure exactly while $\kappa$ (mean-reversion) and $\sigma$ (volatility) remain constants calibrated to volatility instruments.

This overview situates Hull-White inside the short-rate framework of this chapter; all detailed derivations and named-function references live in [Chapter 20](../../ch20/index.md).

---

## Where to find each topic

Recall (see [§ General Short-Rate Framework](general_short_rate_framework.md)): the bond pricing PDE and the expectation $P(t,T) = \mathbb{E}^{\mathbb{Q}}_t[\exp(-\int_t^T r_s\,ds)]$ apply to Hull-White as a Markov short-rate model.

Recall (see [§ Affine Term Structure](affine_term_structure.md)): Hull-White is a Gaussian affine model; it shares Vasicek's $B(t,T) = (1 - e^{-\kappa(T-t)})/\kappa$ because $B$ depends only on $\kappa$, while $A(t,T)$ absorbs the time-dependent $\theta(t)$ to encode the market curve.

Recall (see [§ Vasicek Model](vasicek_model.md)): the Gaussian conditional distribution of $r_t$, with variance $v(s,t) = \frac{\sigma^2}{2\kappa}(1 - e^{-2\kappa(t-s)})$, is identical to the Vasicek case.

| Topic | Canonical location |
|-------|--------------------|
| Short-rate SDE solution and HJM-based derivation of $\theta(t)$ | [§20 Short Rate](../../ch20/short_rate/short_rate_solution.md) |
| Exact-fit formula $\theta(t) = \partial_t f(0,t) + \kappa f(0,t) + \frac{\sigma^2}{2\kappa}(1 - e^{-2\kappa t})$ | [§20 Short Rate](../../ch20/short_rate/short_rate_solution.md) |
| Named functions and Hull-White conventions | [§20 Named Functions](../../ch20/named_functions/named_functions_definition.md) |
| Zero-coupon bond price formula and proofs | [§20 Bond Pricing](../../ch20/bond_pricing/bond_price_formula.md) |
| Bond options under the $T$-forward measure | [§20 Bond Options](../../ch20/bond_options/zero_coupon_bond_options.md) |
| Caplet/floorlet as ZCB put options | [§20 Caplet/Floorlet](../../ch20/derivatives_pricing/caplet_floorlet_formula.md) |
| Swaption pricing via Jamshidian | [§20 Swaption Formula](../../ch20/derivatives_pricing/swaption_formula.md) |
| Two-factor Hull-White (G2++) | [§20 Two-Factor Model](../../ch20/two_factor/two_factor_model_definition.md) |

For calibration to caps/swaptions and side-by-side comparison with Vasicek and CIR, see [§ Vasicek vs CIR vs Hull-White](../model_comparison/vasicek_vs_cir_vs_hull_white.md).

---

## Strengths and Limitations

**Strengths:** Exact curve fit by construction. Analytical tractability with closed-form bond and option prices. Industry standard with efficient calibration.

**Limitations:** Gaussian rates allow negative values. No volatility smile/skew. Single-factor model has limited curve dynamics. Time-inhomogeneous $\theta(t)$ must be stored.

---

## Further Reading

- Hull & White (1990), "Pricing Interest-Rate-Derivative Securities"
- Brigo & Mercurio, *Interest Rate Models*, Chapter 3
- Andersen & Piterbarg, *Interest Rate Modeling*, Volume 2

---

## Exercises

**Exercise 1.** Write the Hull-White SDE and identify each component. How does it differ from the Vasicek SDE? What specific role does the time-dependent function $\theta(t)$ play, and why can it not be replaced by a constant if exact yield curve fitting is required?

??? success "Solution to Exercise 1"
    The **Hull-White SDE** under the risk-neutral measure $\mathbb{Q}$ is

    $$
    dr_t = [\theta(t) - \kappa\, r_t]\,dt + \sigma\,dW_t^{\mathbb{Q}}
    $$

    **Components:**

    - $\theta(t)$: time-dependent drift function, calibrated to the market yield curve.
    - $\kappa > 0$: constant mean-reversion speed.
    - $\sigma > 0$: constant volatility.
    - $W_t^{\mathbb{Q}}$: standard Brownian motion under $\mathbb{Q}$.

    **Comparison with Vasicek.** The Vasicek SDE is $dr_t = \kappa(\theta - r_t)\,dt + \sigma\,dW_t$, where $\theta$ is a constant. In Hull-White, the constant $\kappa\theta$ is replaced by the time-dependent function $\theta(t)$.

    **Role of $\theta(t)$.** The function $\theta(t)$ provides enough degrees of freedom to match the entire initial forward rate curve $f(0,t)$ exactly. Specifically, $\theta(t)$ is uniquely determined by the formula

    $$
    \theta(t) = \frac{\partial f(0,t)}{\partial t} + \kappa\, f(0,t) + \frac{\sigma^2}{2\kappa}(1 - e^{-2\kappa t})
    $$

    **Why a constant cannot suffice.** With constant $\theta$, the model-implied initial forward curve has the specific form $f^{\text{model}}(0,T) = \theta - (\theta - r_0)e^{-\kappa T} - \frac{\sigma^2}{2\kappa^2}(1 - e^{-\kappa T})^2$, which is determined by three parameters $(\kappa, \theta, \sigma)$. This is a three-parameter family of curves, which generically cannot match an arbitrary market term structure with many observed maturities. The time-dependent $\theta(t)$ provides a function's worth of degrees of freedom, enabling exact calibration to any smooth initial curve.

---

---

**Exercise 2.** The Hull-White drift function is given by $\theta(t) = f_t(0,t) + \kappa f(0,t) + \frac{\sigma^2}{2\kappa}(1 - e^{-2\kappa t})$, where $f(0,t)$ is the market instantaneous forward rate. For a flat forward rate curve $f(0,t) = 4\%$, compute $\theta(t)$ at $t = 0, 1, 5, 10$ with $\kappa = 0.05$ and $\sigma = 0.01$.

??? success "Solution to Exercise 2"
    For a flat forward rate curve $f(0,t) = 0.04$ for all $t$, we have $\frac{\partial f}{\partial t}(0,t) = 0$. The drift function becomes

    $$
    \theta(t) = 0 + \kappa \times 0.04 + \frac{\sigma^2}{2\kappa}(1 - e^{-2\kappa t})
    $$

    With $\kappa = 0.05$ and $\sigma = 0.01$:

    $$
    \theta(t) = 0.05 \times 0.04 + \frac{0.0001}{0.1}(1 - e^{-0.1t}) = 0.002 + 0.001(1 - e^{-0.1t})
    $$

    **At $t = 0$:**

    $$
    \theta(0) = 0.002 + 0.001(1 - 1) = 0.002
    $$

    **At $t = 1$:** $e^{-0.1} \approx 0.90484$

    $$
    \theta(1) = 0.002 + 0.001(1 - 0.90484) = 0.002 + 0.0000952 \approx 0.002095
    $$

    **At $t = 5$:** $e^{-0.5} \approx 0.60653$

    $$
    \theta(5) = 0.002 + 0.001(1 - 0.60653) = 0.002 + 0.000393 \approx 0.002393
    $$

    **At $t = 10$:** $e^{-1.0} \approx 0.36788$

    $$
    \theta(10) = 0.002 + 0.001(1 - 0.36788) = 0.002 + 0.000632 \approx 0.002632
    $$

    The drift function $\theta(t)$ increases slowly from 0.002 toward its asymptotic value of $0.002 + 0.001 = 0.003$. The time dependence is modest because the flat forward curve implies simple dynamics. The additional term $\frac{\sigma^2}{2\kappa}(1 - e^{-2\kappa t})$ is the convexity correction that accounts for the difference between expected rates and forward rates due to Jensen's inequality.

---

---

**Exercise 3.** Explain why the Hull-White model produces the same $B(\tau) = (1 - e^{-\kappa\tau})/\kappa$ as the Vasicek model, while the $A(t,T)$ function differs. What part of the bond pricing formula absorbs the time-dependent drift?

??? success "Solution to Exercise 3"
    In both Vasicek and Hull-White, the bond price takes the affine form $P(t,T) = A(t,T)e^{-B(t,T)r_t}$. The function $B(t,T)$ comes from the coefficient of $r$ in the bond pricing PDE.

    **Why $B(\tau)$ is the same.** The coefficient-of-$r$ equation from the PDE is

    $$
    \frac{dB}{d\tau} = 1 - \kappa B, \quad B(0) = 0
    $$

    This ODE involves only the mean-reversion parameter $\kappa$, which is the same constant in both models. The time-dependent function $\theta(t)$ does not appear in this equation because $\theta(t)$ multiplies only the constant term (not the $r$-term) in the drift. Therefore

    $$
    B(\tau) = \frac{1 - e^{-\kappa\tau}}{\kappa}
    $$

    is identical for Vasicek and Hull-White.

    **Why $A(t,T)$ differs.** The constant-term equation is

    $$
    \frac{d\ln A}{d\tau} = \theta(t)\,B(\tau) - \frac{1}{2}\sigma^2 B(\tau)^2
    $$

    In Vasicek, $\theta(t) = \kappa\theta$ (constant), so this ODE can be integrated in closed form to give the standard $A(\tau)$ formula. In Hull-White, $\theta(t)$ is a function of calendar time $t = T - \tau$, so $A$ depends on both $t$ and $T$ separately (not just on $\tau = T - t$). The function $A(t,T)$ absorbs all the information about the initial yield curve through $\theta(t)$, which encodes the market forward rates.

    In practice, $A(t,T)$ is expressed in terms of market discount factors $P^M(0,t)$ and $P^M(0,T)$, ensuring exact calibration.

---

---

**Exercise 4.** A trader observes that the Hull-White model can generate negative rates. For $\kappa = 0.03$, $\sigma = 0.01$, and $r_0 = 0.5\%$, compute the conditional distribution of $r_5$ (the rate in 5 years) and find $\mathbb{P}(r_5 < 0)$. Is this probability negligible or material?

??? success "Solution to Exercise 4"
    In the Hull-White model, $r_t$ conditional on $r_0$ is Gaussian:

    $$
    r_t \mid r_0 \sim \mathcal{N}(m(t),\, v(t))
    $$

    where $v(t) = \frac{\sigma^2}{2\kappa}(1 - e^{-2\kappa t})$.

    With $\kappa = 0.03$, $\sigma = 0.01$, $r_0 = 0.005$, $t = 5$:

    **Variance:**

    $$
    v(5) = \frac{0.0001}{0.06}(1 - e^{-0.3}) = \frac{0.0001}{0.06}(1 - 0.74082) = \frac{0.0001}{0.06} \times 0.25918 \approx 0.000432
    $$

    $$
    \text{Std}(r_5) = \sqrt{0.000432} \approx 0.02078
    $$

    **Mean.** For a flat forward curve $f(0,t) = r_0 = 0.005$ (as an approximation), the conditional mean is approximately

    $$
    m(5) \approx f(0,5) + \frac{\sigma^2}{2\kappa^2}(1 - e^{-\kappa \times 5})^2 / (2 \times 5) \approx 0.005 + \text{small convexity correction}
    $$

    More precisely, the conditional mean under Hull-White depends on $\theta(t)$, which depends on the market curve. For a rough calculation, take $m(5) \approx r_0 = 0.005$ (the mean-reversion target is close to $r_0$ for a flat curve).

    **Probability of negative rates:**

    $$
    \mathbb{P}(r_5 < 0) = \Phi\!\left(\frac{0 - m(5)}{\sqrt{v(5)}}\right) \approx \Phi\!\left(\frac{-0.005}{0.02078}\right) = \Phi(-0.2407) \approx 0.405
    $$

    This probability is approximately **40.5%**, which is highly material. With a low initial rate of 0.5% and relatively high volatility (1% annualized) combined with slow mean reversion ($\kappa = 0.03$, half-life $\approx 23$ years), the Gaussian model assigns substantial probability to negative rates. This illustrates the well-known limitation of Gaussian short-rate models in low-rate environments.

---

---

**Exercise 5.** Hull-White preserves the affine structure of Vasicek. Explain why this means that Jamshidian's decomposition applies for swaption pricing. How many zero-coupon bond options would appear in the Jamshidian decomposition of a 2Y-into-5Y annual payer swaption?

??? success "Solution to Exercise 5"
    **Affine structure and Jamshidian's decomposition.** Jamshidian's trick (1989) decomposes a swaption into a portfolio of zero-coupon bond options. The key requirement is that all zero-coupon bond prices $P(t,T_i)$ are **monotone functions of a single state variable** (here $r_t$). In an affine model, $P(t,T_i) = A(t,T_i)e^{-B(t,T_i)r_t}$, which is a decreasing function of $r_t$ since $B > 0$.

    The coupon bond (or swap annuity) $V(t) = \sum_i c_i P(t,T_i)$ is also monotone in $r_t$ (as a sum of decreasing functions with positive coefficients). Therefore there exists a unique $r^*$ such that $V(T_{\text{exp}}, r^*) = K$ (the strike value). The exercise region is $\{r_{T_{\text{exp}}} < r^*\}$ (for a payer swaption) or $\{r_{T_{\text{exp}}} > r^*\}$ (for a receiver).

    Each bond option in the decomposition has its own strike $K_i = P(T_{\text{exp}}, T_i, r^*)$ and can be priced analytically using the Gaussian bond option formula. The swaption price is the sum of these bond option prices.

    **Number of bond options for a 2Y-into-5Y annual payer swaption.** The underlying swap starts at $T_{\text{exp}} = 2$ and has annual payments at $T_1 = 3, T_2 = 4, T_3 = 5, T_4 = 6, T_5 = 7$. Each payment date generates one zero-coupon bond option (four coupon payments plus one principal + coupon payment, all decomposed into puts on ZCBs). Therefore there are **5 zero-coupon bond options** in the Jamshidian decomposition (one for each cash flow date of the 5-year swap).

---

---

**Exercise 6.** Compare the calibration procedures for Hull-White and Black-Karasinski. Both use time-dependent drifts to fit the yield curve. Why can Hull-White extract $\theta(t)$ analytically while Black-Karasinski requires iterative tree-based calibration?

??? success "Solution to Exercise 6"
    **Hull-White calibration.** The Hull-White SDE is $dr_t = [\theta(t) - \kappa r_t]\,dt + \sigma\,dW_t$. Given $\kappa$ and $\sigma$, the drift function is determined analytically:

    $$
    \theta(t) = \frac{\partial f(0,t)}{\partial t} + \kappa\, f(0,t) + \frac{\sigma^2}{2\kappa}(1 - e^{-2\kappa t})
    $$

    This is a closed-form expression involving only the market forward curve and the two parameters $(\kappa, \sigma)$. No iteration is needed to fit the initial yield curve; the formula directly outputs $\theta(t)$ for any $t$.

    **Black-Karasinski calibration.** The Black-Karasinski model is $d\ln r_t = [\theta(t) - a(t)\ln r_t]\,dt + \sigma(t)\,dW_t$. This model is lognormal, so it prevents negative rates, but it is **not affine**. The bond pricing PDE cannot be solved analytically because the drift and diffusion for $r_t$ (as opposed to $\ln r_t$) involve nonlinear terms ($r\ln r$ and $r^2$).

    To calibrate $\theta(t)$:

    1. Build a trinomial tree for $\ln r_t$ with time-dependent parameters.
    2. At each time step $t_i$, adjust $\theta(t_i)$ so that the tree-implied discount factor $P^{\text{tree}}(0, t_i)$ matches the market discount factor $P^{\text{market}}(0, t_i)$.
    3. This is an iterative procedure: at each step, one must search (e.g., by Newton's method or bisection) for the value of $\theta(t_i)$ that prices the $t_i$-maturity bond correctly.

    The iteration is needed because there is no closed-form relationship between $\theta(t)$ and bond prices in the lognormal model. Each evaluation of the bond price at a given $\theta(t_i)$ requires rolling back through the tree, making the calibration $O(N^2)$ in the number of time steps.

---

---

**Exercise 7.** The two-factor Hull-White (G2++) model uses $r_t = x_t + y_t + \phi(t)$ with two correlated OU processes. Explain what additional yield curve dynamics this enables compared to the one-factor model. Why might a single-factor Hull-White fail for pricing a 10Y Bermudan swaption even if it calibrates well to the swaption volatility matrix diagonal?

??? success "Solution to Exercise 7"
    The **G2++ (two-factor Hull-White)** model specifies $r_t = x_t + y_t + \phi(t)$ where

    $$
    dx_t = -a\,x_t\,dt + \sigma_1\,dW_t^1, \quad dy_t = -b\,y_t\,dt + \sigma_2\,dW_t^2
    $$

    with $\langle dW^1, dW^2\rangle = \rho\,dt$ and $\phi(t)$ chosen to fit the initial curve.

    **Additional dynamics compared to one-factor.**

    1. **Imperfect correlation across maturities.** In a one-factor model, all yields move in perfect correlation (driven by a single Brownian motion). With two factors, short-term and long-term yields can move partially independently. The parameters $a$ and $b$ (different mean-reversion speeds) control the decorrelation across the curve.

    2. **Curve reshaping.** The two-factor model can produce steepening, flattening, and twist movements. If $a \gg b$, the first factor $x_t$ affects short maturities more (fast mean reversion) while $y_t$ affects long maturities more (slow mean reversion), enabling realistic relative movements.

    3. **Humped volatility term structure.** The volatility of forward rates as a function of maturity can exhibit a hump (peak at an intermediate maturity), which is commonly observed in cap markets. A single-factor model produces monotonically decreasing forward rate volatility.

    **Why single-factor fails for Bermudan swaptions.** A 10Y Bermudan swaption gives the holder the right to enter a swap at multiple exercise dates. Its value depends critically on:

    - **The correlation between swap rates at different exercise dates.** A one-factor model implies perfect correlation, systematically undervaluing the optionality. In practice, the holder benefits from low correlation: even if the first exercise date is out-of-the-money, a later date may be in-the-money due to an independent curve movement.

    - **Continuation value.** The decision to exercise early depends on whether the remaining optionality (future exercise opportunities) is worth more than immediate exercise. With perfect correlation, future exercises are highly predictable given the current state, reducing the continuation value. With two factors, future exercises carry genuine additional uncertainty, increasing the Bermudan premium.

    Even if the one-factor model matches the diagonal of the swaption volatility matrix (co-terminal swaptions), it imposes incorrect correlation between off-diagonal swaptions and between different parts of the curve, leading to systematic mispricing of the early exercise premium.
