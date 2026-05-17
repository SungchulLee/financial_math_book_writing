# Yield Curve Dynamics


Pricing interest-rate derivatives requires understanding not only today’s yield curve but also how the **entire curve evolves over time**. Yield curve dynamics are central to term-structure modeling.

---

## From static curves to dynamics


A static yield curve specifies $P(0,T)$ or $f(0,T)$.
A dynamic model specifies how these quantities evolve:

$$
T \mapsto P(t,T), \quad t>0
$$



Short-rate models induce dynamics for the full curve through the evolution of $r_t$.

---

## Curve dynamics under short-rate models


Given $r_t$, bond prices evolve as

$$
P(t,T) = P(t,T,r_t)
$$



Consequences:

- the curve moves in a low-dimensional way,
- all maturities are driven by the same state variable(s),
- this limits flexibility but ensures consistency.

---

## Drift restrictions and no-arbitrage

Recall (see [§ HJM Framework](../hjm/forward_rate_dynamics.md)): no-arbitrage forces bond-price drifts to be determined by volatility, tying together the evolution across all maturities.

---

## Implications for derivative pricing


Yield curve dynamics determine:

- swap and FRA pricing,
- cap/floor and swaption dynamics,
- hedging behavior across maturities.

Model choice affects which curve moves are possible.

---

## Key takeaways


- Yield curve dynamics are essential for IR derivative pricing.
- Short-rate models generate low-dimensional curve movements.
- No-arbitrage tightly constrains curve evolution.

---

## Further reading


- Heath, Jarrow & Morton (HJM).
- Filipovic, *Term-Structure Models*.

---

## Exercises

**Exercise 1.** In the Vasicek model $dr_t = \kappa(\theta - r_t)\,dt + \sigma\,dW_t$, the bond price is $P(t, T) = e^{A(T-t) + B(T-t)\,r_t}$. Show that all bond prices are driven by the single state variable $r_t$, and explain why the yield curve can only undergo "parallel-like" shifts (up to the $B(\tau)$ weighting). What types of yield curve movements are impossible in this model?

??? success "Solution to Exercise 1"
    In the Vasicek model, the bond price has the affine form $P(t, T) = e^{A(\tau) + B(\tau)\,r_t}$ where $\tau = T - t$ and

    $$
    B(\tau) = \frac{1 - e^{-\kappa \tau}}{\kappa}, \qquad A(\tau) = \left(\theta - \frac{\sigma^2}{2\kappa^2}\right)(B(\tau) - \tau) - \frac{\sigma^2}{4\kappa}B(\tau)^2
    $$

    Since both $A(\tau)$ and $B(\tau)$ are deterministic functions of $\tau$ alone, the only source of randomness in $P(t, T)$ is $r_t$. All bond prices across all maturities $T$ are driven by the single state variable $r_t$.

    The yield is $y(t, T) = -\ln P(t, T)/\tau = -A(\tau)/\tau - B(\tau)\,r_t/\tau$. When $r_t$ changes by $\Delta r$, the yield at maturity $T$ changes by $-B(\tau)\,\Delta r / \tau$. The factor $B(\tau)/\tau$ is a deterministic, maturity-dependent weight that starts at $1$ for short maturities and decays toward $1/\kappa$ for long maturities. All yield changes are proportional to $\Delta r$, so the curve undergoes "parallel-like" shifts modulated by the $B(\tau)/\tau$ weighting.

    **Impossible movements:** Because the entire curve is governed by a single factor, the model cannot produce independent movements in the short end and the long end. In particular, it cannot generate pure slope changes (short rates up while long rates down) or curvature changes (butterfly movements) without also changing the level. Any yield curve twist or butterfly requires at least two independent factors.

---

**Exercise 2.** Starting from a flat yield curve $P(0, T) = e^{-r_0 T}$ with $r_0 = 5\%$, suppose the Vasicek parameters are $\kappa = 0.1$, $\theta = 5\%$, $\sigma = 1\%$. Compute $P(0, T)$ for $T = 1, 5, 10, 30$ years using the Vasicek formula. Plot the initial yield curve $y(0, T) = -\ln P(0, T)/T$ and discuss its shape.

??? success "Solution to Exercise 2"
    With $\kappa = 0.1$, $\theta = 0.05$, $\sigma = 0.01$, and $r_0 = 0.05$, we compute $B(\tau)$ and $A(\tau)$ for each maturity $\tau = T$:

    $$
    B(\tau) = \frac{1 - e^{-0.1\tau}}{0.1}
    $$

    $$
    A(\tau) = \left(0.05 - \frac{0.0001}{0.02}\right)(B(\tau) - \tau) - \frac{0.0001}{0.4}B(\tau)^2 = (0.05 - 0.005)(B(\tau) - \tau) - 0.00025\,B(\tau)^2
    $$

    For $\tau = 1$: $B(1) = (1 - e^{-0.1})/0.1 \approx 0.9516$, $A(1) \approx 0.045 \times (0.9516 - 1) - 0.00025 \times 0.9516^2 \approx -0.00218 - 0.000226 \approx -0.00241$. So $P(0,1) = e^{-0.00241 + 0.9516 \times 0.05} \approx e^{-0.04999} \approx 0.9513$ and $y(0,1) \approx 5.00\%$.

    For $\tau = 5$: $B(5) \approx 3.935$, and a similar calculation gives $y(0,5) \approx 4.99\%$.

    For $\tau = 10$: $B(10) \approx 6.321$, giving $y(0,10) \approx 4.97\%$.

    For $\tau = 30$: $B(30) \approx 9.502$, giving $y(0,30) \approx 4.88\%$.

    Since $r_0 = \theta = 5\%$, the yield curve is nearly flat but slightly downward sloping at long maturities. The small downward slope arises from the **convexity adjustment** $-\sigma^2 B(\tau)^2/(4\kappa\tau)$, which increases (in absolute value) with maturity. This is a distinctive feature of the Vasicek model: even when $r_0 = \theta$, the yield curve is not perfectly flat due to Jensen's inequality applied to the exponential bond pricing formula.

---

**Exercise 3.** Explain the difference between a **static** yield curve $\{P(0, T)\}_{T \geq 0}$ and **dynamic** yield curve evolution $\{P(t, T)\}_{t \leq T}$. Why is the static curve insufficient for pricing interest rate derivatives such as caps and swaptions?

??? success "Solution to Exercise 3"
    A **static** yield curve $\{P(0, T)\}_{T \geq 0}$ specifies today's prices of zero-coupon bonds for all maturities. It encodes the market's current term structure of interest rates as a snapshot at time $t = 0$.

    A **dynamic** yield curve evolution $\{P(t, T)\}_{t \leq T}$ specifies how bond prices evolve over time as a stochastic process. It describes the joint distribution of future yield curves, including how different maturities co-move.

    The static curve is insufficient for pricing interest rate derivatives because:

    1. **Caps and floors** depend on the distribution of future rates $r_t$ or LIBOR rates $L(t, t+\delta)$. The payoff $(L(T_i, T_{i+1}) - K)^+$ requires knowing the probability distribution of future rates, not just today's forward rates.

    2. **Swaptions** give the right to enter a swap at a future date. Their value depends on the distribution of the future swap rate, which requires modeling how the entire yield curve moves.

    3. **Path-dependent derivatives** (e.g., range accruals, callable bonds) depend on the trajectory of rates, which requires a full dynamic model.

    In short, the static curve determines today's forward rates $f(0, T)$, but derivatives depend on the volatility and correlation structure of future rates, which only a dynamic model can provide.

---

**Exercise 4.** In HJM theory, the drift of the instantaneous forward rate $f(t, T)$ under the risk-neutral measure is fully determined by the volatility function $\sigma_f(t, T)$. State the HJM drift condition without proof. Explain why this condition implies that specifying the yield curve dynamics is equivalent to specifying the volatility structure.

??? success "Solution to Exercise 4"
    The **HJM drift condition** states that under the risk-neutral measure $\mathbb{Q}$, the instantaneous forward rate $f(t, T)$ satisfies

    $$
    df(t, T) = \alpha(t, T)\,dt + \sigma_f(t, T)\,dW_t
    $$

    where the drift is fully determined by the volatility:

    $$
    \alpha(t, T) = \sigma_f(t, T) \int_t^T \sigma_f(t, u)\,du
    $$

    This condition arises from requiring the discounted bond prices $e^{-\int_0^t r_s\,ds} P(t, T)$ to be martingales under $\mathbb{Q}$.

    **Why volatility determines dynamics:** Since the drift $\alpha(t, T)$ is a deterministic functional of $\sigma_f(t, T)$, specifying the volatility structure $\sigma_f(t, T)$ completely determines the risk-neutral dynamics of the entire forward curve. The initial curve $f(0, T)$ provides the starting condition, and the volatility function governs all subsequent evolution. There is no additional freedom in choosing the drift -- it is locked in by the no-arbitrage requirement. Thus, the entire modeling problem reduces to choosing an appropriate volatility specification.

---

**Exercise 5.** Consider a two-factor short-rate model where $r_t = x_t + y_t + \varphi(t)$, with $x_t$ and $y_t$ independent OU processes with different mean-reversion speeds. Explain how this model generates richer yield curve dynamics than a one-factor model. What additional yield curve movements (beyond level shifts) become possible?

??? success "Solution to Exercise 5"
    In the two-factor model $r_t = x_t + y_t + \varphi(t)$, where

    $$
    dx_t = -\kappa_x\,x_t\,dt + \sigma_x\,dW_t^x, \qquad dy_t = -\kappa_y\,y_t\,dt + \sigma_y\,dW_t^y
    $$

    with $\kappa_x \neq \kappa_y$ (say $\kappa_x < \kappa_y$), the two factors mean-revert at different speeds.

    **Richer dynamics:** The yield at maturity $\tau$ takes the form

    $$
    y(t, T) = -\frac{A(\tau)}{\tau} - \frac{B_x(\tau)}{\tau}\,x_t - \frac{B_y(\tau)}{\tau}\,y_t
    $$

    where $B_x(\tau) = (1 - e^{-\kappa_x \tau})/\kappa_x$ and $B_y(\tau) = (1 - e^{-\kappa_y \tau})/\kappa_y$. Since $\kappa_x < \kappa_y$, the factor $x_t$ mean-reverts slowly and affects long maturities more (large $B_x(\tau)/\tau$), while $y_t$ mean-reverts quickly and affects short maturities more (small $B_y(\tau)/\tau$ at long maturities).

    **Additional movements:** Beyond level shifts, the two-factor model can generate:

    - **Slope changes (steepening/flattening):** If $x_t$ rises while $y_t$ falls (or vice versa), the long end moves differently from the short end.
    - **Independent short-end and long-end movements:** The fast-reverting factor $y_t$ drives short-term rate fluctuations that decay quickly along the curve, while $x_t$ drives persistent level shifts.

    However, with only two factors, the model still cannot produce arbitrary curvature (butterfly) movements independently of level and slope changes. A third factor would be needed for fully independent level-slope-curvature dynamics.

---

**Exercise 6.** Suppose the yield curve at time $t$ is described by a Nelson-Siegel parameterization:

$$
y(t, T) = \beta_0(t) + \beta_1(t)\frac{1 - e^{-\alpha(T-t)}}{\alpha(T-t)} + \beta_2(t)\left(\frac{1 - e^{-\alpha(T-t)}}{\alpha(T-t)} - e^{-\alpha(T-t)}\right)
$$

Identify $\beta_0$, $\beta_1$, $\beta_2$ as level, slope, and curvature factors. Discuss whether making $\beta_0(t)$, $\beta_1(t)$, $\beta_2(t)$ stochastic necessarily produces an arbitrage-free model.

??? success "Solution to Exercise 6"
    In the Nelson-Siegel parameterization, the three factors have the following interpretations:

    - $\beta_0(t)$: **Level factor.** As $\tau \to \infty$, both loading functions $(1 - e^{-\alpha\tau})/(\alpha\tau)$ and $(1 - e^{-\alpha\tau})/(\alpha\tau) - e^{-\alpha\tau}$ converge to $0$, so $y(t, T) \to \beta_0(t)$. This is the long-run yield level.

    - $\beta_1(t)$: **Slope factor.** The loading $(1 - e^{-\alpha\tau})/(\alpha\tau)$ starts at $1$ for $\tau = 0$ and decays to $0$. It captures the difference between short-term and long-term yields.

    - $\beta_2(t)$: **Curvature factor.** The loading $(1 - e^{-\alpha\tau})/(\alpha\tau) - e^{-\alpha\tau}$ starts at $0$, increases to a hump at intermediate maturities, and decays to $0$. It captures the curvature (concavity/convexity) of the yield curve.

    **Arbitrage-free?** Making $\beta_0(t)$, $\beta_1(t)$, $\beta_2(t)$ stochastic does **not** automatically produce an arbitrage-free model. The Nelson-Siegel form imposes a specific functional relationship between yields at different maturities, and when the factors evolve stochastically, the resulting bond price dynamics may violate the HJM drift condition. Christensen, Diebold, and Rudebusch (2011) showed that the standard dynamic Nelson-Siegel model is not arbitrage-free, and proposed the "Arbitrage-Free Nelson-Siegel" (AFNS) model, which adds deterministic correction terms to $A(\tau)$ to restore the no-arbitrage condition. The key issue is that an arbitrary factor model for yields must satisfy specific drift restrictions (from HJM theory) to be arbitrage-free, and the Nelson-Siegel loadings do not automatically satisfy these restrictions.
