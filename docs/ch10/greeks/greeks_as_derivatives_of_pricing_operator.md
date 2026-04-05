# Greeks as Derivatives of the Pricing Operator


A mathematically clean viewpoint is: pricing is an **operator** that maps a payoff to a function of \((t,S)\), and Greeks are derivatives of that operator with respect to inputs.

---

## Pricing as an operator


For a European payoff \(\Phi(S_T)\) under a risk-neutral model, define the pricing operator


\[
(\mathcal{P}\Phi)(t,S)
:=
\mathbb{E}^{t,S}\!\left[e^{-r(T-t)}\Phi(S_T)\right]
\]



Then the option price is


\[
V(t,S) = (\mathcal{P}\Phi)(t,S)
\]



---

## State derivatives vs parameter derivatives


- **State derivatives**: \(\partial_S(\mathcal{P}\Phi)\), \(\partial_S^2(\mathcal{P}\Phi)\) correspond to \(\Delta,\Gamma\).
- **Parameter derivatives**: \(\partial_\sigma(\mathcal{P}\Phi)\), \(\partial_r(\mathcal{P}\Phi)\) correspond to vega and rho.

This separation matters because:

- state derivatives reflect geometry of \(V\) as a function of \(S\),
- parameter derivatives reflect sensitivity of the law of \(S_T\) to parameter changes.

---

## Differentiation under the expectation


Formally, for a parameter \(\theta\),


\[
\frac{\partial}{\partial \theta}(\mathcal{P}_\theta\Phi)
=
\frac{\partial}{\partial \theta}
\mathbb{E}^{t,S}_\theta\!\left[e^{-r(T-t)}\Phi(S_T)\right]
\]



The derivative can be handled by:

- differentiating the PDE satisfied by \(V\),
- differentiating the stochastic flow \(S_T^{\theta}\) (pathwise differentiation),
- changing measure or using likelihood ratio (score) identities.

Each method leads to a distinct “representation formula” for Greeks.

---

## Functional-analytic analogy


Think of \(\mathcal{P}\) as a linear map (for fixed model) acting on payoffs:


\[
\Phi \mapsto V(\cdot,\cdot)
\]



Greeks are then derivatives of \(\mathcal{P}\Phi\) with respect to:

- the spatial variable \(S\),
- parameters of the operator \(\mathcal{P}\).

---

## What to remember


- The pricing map is an operator \(\mathcal{P}\).
- Greeks are derivatives of \(\mathcal{P}\Phi\) with respect to state variables and model parameters.
- PDE, probabilistic, and measure-theoretic approaches give complementary Greek formulas.

---

## Exercises

**Exercise 1.** Let $\mathcal{P}_\sigma$ denote the pricing operator parameterized by volatility $\sigma$. For a European call payoff $\Phi(S_T) = (S_T - K)^+$, show that vega can be written as $\nu = \frac{\partial}{\partial \sigma}(\mathcal{P}_\sigma \Phi)(t,S)$. Explain why this is a parameter derivative rather than a state derivative.

??? success "Solution to Exercise 1"
    The pricing operator parameterized by volatility $\sigma$ is:

    $$
    (\mathcal{P}_\sigma \Phi)(t,S) = \mathbb{E}^{t,S}\!\left[e^{-r(T-t)}\Phi(S_T)\right]
    $$

    where the expectation is taken under the risk-neutral measure with dynamics $\mathrm{d}S_u = rS_u\,\mathrm{d}u + \sigma S_u\,\mathrm{d}W_u$. The law of $S_T$ depends on $\sigma$ through these dynamics.

    Vega is then:

    $$
    \nu = \frac{\partial}{\partial \sigma}(\mathcal{P}_\sigma \Phi)(t,S)
    $$

    This is a **parameter derivative** rather than a state derivative because:

    - A **state derivative** such as delta ($\partial_S$) differentiates $V(t,S)$ with respect to the current state variable $S$, holding the model fixed. It reflects the geometry of $V$ as a function of spot.
    - A **parameter derivative** such as vega ($\partial_\sigma$) differentiates $V$ with respect to a parameter that enters the dynamics of $S_T$. Changing $\sigma$ changes the entire probability distribution of $S_T$ under $\mathbb{Q}$, and hence changes the operator $\mathcal{P}_\sigma$ itself.

    In the state-derivative case, we perturb the initial condition $(t,S)$ of the process. In the parameter-derivative case, we perturb the law of the process while keeping the initial condition fixed.

---

**Exercise 2.** Consider the pricing operator $\mathcal{P}$ acting on the payoff $\Phi_1(x) = (x - K)^+$ and $\Phi_2(x) = x$. Compute $(\mathcal{P}\Phi_2)(t,S)$ explicitly in the Black--Scholes model and verify that $\Delta = \partial_S(\mathcal{P}\Phi_2) = 1$, as expected for a forward contract.

??? success "Solution to Exercise 2"
    For the payoff $\Phi_2(x) = x$ (a forward contract paying $S_T$ at maturity), the pricing operator gives:

    $$
    (\mathcal{P}\Phi_2)(t,S) = \mathbb{E}^{t,S}\!\left[e^{-r(T-t)} S_T\right]
    $$

    In the Black-Scholes model, $S_T = S \exp\!\left((r - \tfrac{1}{2}\sigma^2)(T-t) + \sigma(W_T - W_t)\right)$. Therefore:

    $$
    \mathbb{E}^{t,S}[S_T] = S \exp\!\left((r - \tfrac{1}{2}\sigma^2)(T-t)\right) \mathbb{E}\!\left[e^{\sigma(W_T - W_t)}\right]
    $$

    Since $W_T - W_t \sim N(0, T-t)$, we have $\mathbb{E}[e^{\sigma(W_T-W_t)}] = e^{\frac{1}{2}\sigma^2(T-t)}$. Thus:

    $$
    \mathbb{E}^{t,S}[S_T] = S e^{r(T-t)}
    $$

    and

    $$
    (\mathcal{P}\Phi_2)(t,S) = e^{-r(T-t)} \cdot S e^{r(T-t)} = S
    $$

    The delta is:

    $$
    \Delta = \frac{\partial}{\partial S}(\mathcal{P}\Phi_2)(t,S) = \frac{\partial S}{\partial S} = 1
    $$

    This confirms that the delta of a forward contract (or equivalently, a position in the underlying itself) is exactly $1$, as expected.

---

**Exercise 3.** The pricing operator $\mathcal{P}$ is linear in the payoff $\Phi$ for a fixed model. Using this linearity, express the price and delta of a straddle (long call + long put at the same strike) in terms of the pricing operator applied to the call and put payoffs individually.

??? success "Solution to Exercise 3"
    Let $\Phi_C(x) = (x - K)^+$ and $\Phi_P(x) = (K - x)^+$ be the call and put payoffs. The straddle payoff is:

    $$
    \Phi_{\text{straddle}}(x) = \Phi_C(x) + \Phi_P(x) = (x - K)^+ + (K - x)^+ = |x - K|
    $$

    By linearity of the pricing operator:

    $$
    (\mathcal{P}\Phi_{\text{straddle}})(t,S) = (\mathcal{P}\Phi_C)(t,S) + (\mathcal{P}\Phi_P)(t,S) = C(t,S) + P(t,S)
    $$

    The **straddle price** is simply the sum of the call and put prices.

    For the **straddle delta**, differentiate with respect to $S$:

    $$
    \Delta_{\text{straddle}} = \frac{\partial}{\partial S}\left[(\mathcal{P}\Phi_C)(t,S) + (\mathcal{P}\Phi_P)(t,S)\right] = \Delta_C + \Delta_P
    $$

    In the Black-Scholes model, $\Delta_C = N(d_1)$ and $\Delta_P = N(d_1) - 1$, so:

    $$
    \Delta_{\text{straddle}} = 2N(d_1) - 1
    $$

    The straddle is delta-neutral when $N(d_1) = 1/2$, i.e., $d_1 = 0$, which corresponds approximately to the at-the-money-forward strike.

---

**Exercise 4.** State derivatives (delta, gamma) and parameter derivatives (vega, rho) respond to different types of perturbations. Describe a market scenario in which parameter derivatives dominate the P&L, and another in which state derivatives dominate. What determines which class is more important for risk management?

??? success "Solution to Exercise 4"
    **Scenario where parameter derivatives dominate.** Consider a portfolio of long-dated options (e.g., $\tau = 2$ years) on a stock with relatively low realized volatility. If the implied volatility surface shifts by several percentage points (e.g., due to a market crisis or a change in monetary policy expectations) while the underlying moves only modestly, then:

    - Vega ($\partial V / \partial \sigma$) and rho ($\partial V / \partial r$) produce large P&L contributions because implied volatility and rate changes are amplified by large $\tau$.
    - Delta and gamma contributions are modest because $\delta S$ is small.

    **Scenario where state derivatives dominate.** Consider a portfolio of short-dated at-the-money options (e.g., $\tau = 1$ week). A sudden large move in the underlying (e.g., earnings surprise causing $\delta S / S = 5\%$) generates:

    - A large delta P&L ($\Delta \cdot \delta S$) and gamma P&L ($\frac{1}{2}\Gamma(\delta S)^2$).
    - Vega is small because $\nu \propto \sqrt{\tau}$ shrinks for short maturities.

    **What determines which class matters most:** The relative importance depends on (1) the magnitudes of the perturbations ($|\delta S|$ vs $|\delta\sigma|$ vs $|\delta r|$), (2) the maturity (longer maturity amplifies parameter sensitivities), and (3) moneyness (ATM options have the largest vega and gamma). For risk management, one must assess the plausible ranges of each perturbation under stress scenarios.

---

**Exercise 5.** Explain how the three methods for computing $\frac{\partial}{\partial \theta}(\mathcal{P}_\theta \Phi)$ --- PDE differentiation, pathwise differentiation, and likelihood ratio --- each handle the derivative. For each method, identify one setting where it is preferred and one where it fails or is impractical.

??? success "Solution to Exercise 5"
    **PDE differentiation.** Differentiate the pricing PDE $\partial_t V + \mathcal{L}_\theta V - rV = 0$ with respect to $\theta$. This yields a new PDE for $\partial_\theta V$ with a source term involving $\frac{\partial \mathcal{L}_\theta}{\partial \theta} V$.

    - *Preferred:* When the PDE is solved numerically on a grid (finite differences), the sensitivity PDE can be solved on the same grid at modest additional cost.
    - *Impractical:* For path-dependent or high-dimensional problems where PDE methods are infeasible (curse of dimensionality).

    **Pathwise (tangent) differentiation.** Differentiate the stochastic flow $S_T(\theta)$ with respect to $\theta$ by interchanging differentiation and expectation: $\frac{\partial}{\partial\theta} \mathbb{E}[e^{-rT}\Phi(S_T)] = \mathbb{E}[e^{-rT}\Phi'(S_T)\frac{\partial S_T}{\partial \theta}]$.

    - *Preferred:* When $\Phi$ is smooth (e.g., a vanilla European option with smooth payoff), this gives low-variance Monte Carlo estimators.
    - *Fails:* When $\Phi$ is discontinuous (e.g., digital options with payoff $\mathbf{1}_{S_T > K}$), since $\Phi'$ does not exist in the classical sense.

    **Likelihood ratio (score function) method.** Instead of differentiating the payoff, differentiate the density: $\frac{\partial}{\partial\theta}\mathbb{E}_\theta[\Phi] = \mathbb{E}_\theta[\Phi \cdot \nabla_\theta \log p_\theta]$.

    - *Preferred:* When the payoff is discontinuous (digital, barrier options), since no differentiation of $\Phi$ is needed.
    - *Impractical:* When the density $p_\theta$ is not known in closed form, or when the estimator has high variance (which is common for multi-step simulations).

---

**Exercise 6.** Consider a pricing operator $\mathcal{P}$ in a local volatility model where $\sigma = \sigma(S,t)$. Is vega still well-defined as $\partial_\sigma(\mathcal{P}\Phi)$? Discuss what "volatility sensitivity" means when $\sigma$ is a function rather than a parameter, and describe how bucket vega addresses this issue.

??? success "Solution to Exercise 6"
    In a local volatility model, $\sigma = \sigma(S,t)$ is a function of both spot and time, not a single scalar parameter. The expression $\partial_\sigma(\mathcal{P}\Phi)$ is **not well-defined** in the usual sense, because there is no single parameter $\sigma$ to differentiate with respect to. One cannot take a partial derivative with respect to an entire function.

    **What "volatility sensitivity" means in this context.** Sensitivity must be defined with respect to specific perturbations of the volatility surface. Common approaches include:

    1. **Parallel shift:** Perturb $\sigma(S,t) \to \sigma(S,t) + \epsilon$ uniformly and compute $\frac{\partial V}{\partial \epsilon}\big|_{\epsilon=0}$. This gives a single aggregate vega but conflates sensitivities across all strikes and maturities.

    2. **Bucket vega.** Partition the $(S,t)$ domain (or equivalently the $(K,T)$ domain of implied volatilities) into "buckets" $B_1, B_2, \ldots, B_n$. Define the $k$-th bucket vega as:

        $$
        \nu_k = \frac{\partial V}{\partial \epsilon_k}\bigg|_{\epsilon_k = 0}
        $$

        where $\sigma(S,t) \to \sigma(S,t) + \epsilon_k \mathbf{1}_{(S,t) \in B_k}$. Each $\nu_k$ captures sensitivity to volatility changes in a localized region of the surface.

    Bucket vega provides a finite-dimensional approximation to the functional derivative $\frac{\delta V}{\delta \sigma(S,t)}$. In practice, traders use bucket vegas organized by expiry and strike to manage smile and term-structure risk.
