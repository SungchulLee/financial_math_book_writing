# Delta, Gamma, Vega, Theta, Rho


Let an option price be written as a function


$$
V = V(t,S;\sigma,r,\dots)
$$



where $t\in[0,T]$ is time, $S>0$ is the underlying price, $\sigma>0$ is volatility, and $r\in\mathbb{R}$ is the short rate (constant in Black–Scholes).

The **Greeks** are partial derivatives of the pricing map $V$ with respect to state variables and model parameters. They quantify first- and second-order sensitivities and form the basis of risk measurement and hedging, independently of any particular pricing model.


---

## Delta



$$
\boxed{\Delta(t,S) := \frac{\partial V}{\partial S}(t,S)}
$$



Delta measures first-order sensitivity of the option value to small changes in $S$.

---

## Gamma



$$
\boxed{\Gamma(t,S) := \frac{\partial^2 V}{\partial S^2}(t,S)}
$$



Gamma measures convexity with respect to $S$. It controls second-order error in delta hedging and is central for hedging error asymptotics.

---

## Vega



$$
\boxed{\nu(t,S) := \frac{\partial V}{\partial \sigma}(t,S)}
$$



Vega measures sensitivity to volatility. In Black–Scholes, $\nu$ is typically largest near-the-money and for moderate maturities.

---

## Theta


There are multiple sign conventions. Here we define **calendar-time theta**


$$
\boxed{\Theta(t,S) := \frac{\partial V}{\partial t}(t,S)}
$$



Since many PDEs are written backward in time, some texts define $-\partial_t V$ as theta. Be explicit about convention whenever using theta in P\&L decompositions.

---

## Rho



$$
\boxed{\rho(t,S) := \frac{\partial V}{\partial r}(t,S)}
$$



Rho measures sensitivity to changes in interest rates.

---

## A second-order Taylor expansion viewpoint


For a small perturbation $(\delta S,\delta\sigma,\delta r)$ (ignoring cross-terms for clarity),


$$
V(t,S+\delta S;\sigma+\delta\sigma,r+\delta r)
\approx
V(t,S;\sigma,r)
+\Delta\,\delta S
+\nu\,\delta\sigma
+\rho\,\delta r
+\frac{1}{2}\Gamma\,(\delta S)^2
$$



This is the conceptual basis for “Greek-based” risk decomposition and hedging heuristics.

---

## What to remember


- Greeks are derivatives of a pricing map $V(t,S;\theta)$ with respect to state and parameters.
- Gamma is the curvature term that dominates short-time hedging error.
- Theta conventions vary; define yours explicitly.
- In the next section, these abstract definitions are specialized to the
**Black–Scholes model**, where the Greeks can be computed explicitly in
closed form.

---

## Exercises

**Exercise 1.** A European call option has price $V = 12.50$, with $\Delta = 0.62$, $\Gamma = 0.035$, and $\nu = 18.5$. If the underlying moves from $S = 100$ to $S = 103$ while volatility increases from $\sigma = 0.20$ to $\sigma = 0.22$, estimate the new option price using the second-order Taylor expansion.

??? success "Solution to Exercise 1"
    Using the second-order Taylor expansion:

    $$
    V(t, S + \delta S; \sigma + \delta\sigma, r + \delta r) \approx V + \Delta\,\delta S + \nu\,\delta\sigma + \rho\,\delta r + \frac{1}{2}\Gamma\,(\delta S)^2
    $$

    We have $V = 12.50$, $\Delta = 0.62$, $\Gamma = 0.035$, $\nu = 18.5$, $\delta S = 3$, $\delta\sigma = 0.02$, and $\delta r = 0$. Substituting:

    - First-order delta term: $\Delta\,\delta S = 0.62 \times 3 = 1.86$
    - Vega term: $\nu\,\delta\sigma = 18.5 \times 0.02 = 0.37$
    - Second-order gamma term: $\frac{1}{2}\Gamma\,(\delta S)^2 = \frac{1}{2} \times 0.035 \times 9 = 0.1575$

    The estimated new option price is:

    $$
    V_{\text{new}} \approx 12.50 + 1.86 + 0.37 + 0.1575 = 14.8875
    $$

    The approximate new option price is $\$14.89$.

---

**Exercise 2.** Explain why gamma is the same for a European call and a European put with the same strike and maturity, while delta and rho differ. Use put-call parity to justify your answer.

??? success "Solution to Exercise 2"
    **Put-call parity** states that $C - P = S - Ke^{-r\tau}$, where the right-hand side is a linear function of $S$.

    **Gamma.** Since $\Gamma = \frac{\partial^2 V}{\partial S^2}$, differentiating both sides of put-call parity twice with respect to $S$ gives:

    $$
    \frac{\partial^2 C}{\partial S^2} - \frac{\partial^2 P}{\partial S^2} = \frac{\partial^2}{\partial S^2}(S - Ke^{-r\tau}) = 0
    $$

    Therefore $\Gamma_{\text{call}} = \Gamma_{\text{put}}$. The second derivative of a linear function vanishes, so any Greek that involves a second (or higher) derivative with respect to $S$ is identical for calls and puts.

    **Delta.** Differentiating put-call parity once with respect to $S$:

    $$
    \Delta_{\text{call}} - \Delta_{\text{put}} = 1
    $$

    So $\Delta_{\text{put}} = \Delta_{\text{call}} - 1$. They differ because the first derivative of $S - Ke^{-r\tau}$ with respect to $S$ is $1$, not zero.

    **Rho.** Differentiating with respect to $r$:

    $$
    \rho_{\text{call}} - \rho_{\text{put}} = K\tau e^{-r\tau}
    $$

    They differ because $\frac{\partial}{\partial r}(-Ke^{-r\tau}) = K\tau e^{-r\tau} \neq 0$.

    In summary, any Greek obtained by differentiating with respect to a variable in which $S - Ke^{-r\tau}$ is nonlinear (or has nonzero derivative) will differ between calls and puts.

---

**Exercise 3.** Consider a portfolio consisting of $n_1$ calls and $n_2$ puts on the same underlying, all with the same strike and maturity. Write the portfolio Greeks $\Delta_\pi$, $\Gamma_\pi$, $\nu_\pi$, $\Theta_\pi$, $\rho_\pi$ in terms of $n_1$, $n_2$, and the individual option Greeks. Under what conditions is the portfolio delta-neutral?

??? success "Solution to Exercise 3"
    Let $C_i$ and $P_i$ denote the call and put option prices respectively. The portfolio value is:

    $$
    \Pi = n_1 C + n_2 P
    $$

    Since Greeks are partial derivatives and differentiation is linear, the portfolio Greeks are:

    - $\Delta_\pi = n_1 \Delta_C + n_2 \Delta_P$
    - $\Gamma_\pi = n_1 \Gamma_C + n_2 \Gamma_P = (n_1 + n_2)\Gamma$ (since $\Gamma_C = \Gamma_P$)
    - $\nu_\pi = n_1 \nu_C + n_2 \nu_P = (n_1 + n_2)\nu$ (since $\nu_C = \nu_P$)
    - $\Theta_\pi = n_1 \Theta_C + n_2 \Theta_P$
    - $\rho_\pi = n_1 \rho_C + n_2 \rho_P$

    **Delta-neutral condition.** Setting $\Delta_\pi = 0$:

    $$
    n_1 \Delta_C + n_2 \Delta_P = 0
    $$

    Using put-call parity, $\Delta_P = \Delta_C - 1$, so:

    $$
    n_1 \Delta_C + n_2(\Delta_C - 1) = 0 \implies \Delta_C = \frac{n_2}{n_1 + n_2}
    $$

    provided $n_1 + n_2 \neq 0$. If $n_1 + n_2 = 0$ (i.e., $n_2 = -n_1$), then $\Delta_\pi = n_1(\Delta_C - \Delta_P) = n_1$, which is zero only if $n_1 = 0$. So for a nontrivial portfolio, delta-neutrality requires balancing the number of calls and puts according to the current delta of the call.

---

**Exercise 4.** Show that the second-order Taylor expansion for the option price can be written in vector-matrix form as

$$
\delta V \approx \mathbf{g}^T \delta \mathbf{x} + \frac{1}{2} \delta \mathbf{x}^T \mathbf{H} \, \delta \mathbf{x}
$$

where $\mathbf{g}$ is the gradient vector of first-order Greeks and $\mathbf{H}$ is the Hessian of second-order Greeks. Identify the entries of $\mathbf{g}$ and $\mathbf{H}$ for variables $(S, \sigma, r)$.

??? success "Solution to Exercise 4"
    We write the option price as a function $V(t, \mathbf{x})$ where $\mathbf{x} = (S, \sigma, r)^T$. The second-order Taylor expansion is:

    $$
    \delta V = V(t, \mathbf{x} + \delta\mathbf{x}) - V(t, \mathbf{x}) \approx \mathbf{g}^T \delta\mathbf{x} + \frac{1}{2}\delta\mathbf{x}^T \mathbf{H}\,\delta\mathbf{x}
    $$

    The **gradient vector** of first-order Greeks is:

    $$
    \mathbf{g} = \begin{pmatrix} \partial V / \partial S \\ \partial V / \partial \sigma \\ \partial V / \partial r \end{pmatrix} = \begin{pmatrix} \Delta \\ \nu \\ \rho \end{pmatrix}
    $$

    The **Hessian matrix** of second-order Greeks is the $3 \times 3$ symmetric matrix:

    $$
    \mathbf{H} = \begin{pmatrix} \frac{\partial^2 V}{\partial S^2} & \frac{\partial^2 V}{\partial S \partial \sigma} & \frac{\partial^2 V}{\partial S \partial r} \\ \frac{\partial^2 V}{\partial \sigma \partial S} & \frac{\partial^2 V}{\partial \sigma^2} & \frac{\partial^2 V}{\partial \sigma \partial r} \\ \frac{\partial^2 V}{\partial r \partial S} & \frac{\partial^2 V}{\partial r \partial \sigma} & \frac{\partial^2 V}{\partial r^2} \end{pmatrix} = \begin{pmatrix} \Gamma & \text{Vanna} & \frac{\partial \Delta}{\partial r} \\ \text{Vanna} & \text{Volga} & \frac{\partial \nu}{\partial r} \\ \frac{\partial \Delta}{\partial r} & \frac{\partial \nu}{\partial r} & \frac{\partial^2 V}{\partial r^2} \end{pmatrix}
    $$

    where Vanna $= \partial^2 V / \partial S \partial \sigma$ and Volga $= \partial^2 V / \partial \sigma^2$. The off-diagonal entries are the cross-Greeks. In practice, many of these second-order cross-terms are small and only $\Gamma$ (the $(1,1)$ entry) is routinely included.

---

**Exercise 5.** Why does theta have ambiguous sign conventions in the literature? If one defines $\Theta_1 = \partial V / \partial t$ and $\Theta_2 = -\partial V / \partial t$, explain which is negative for a long call position and why. How does the convention affect the P&L decomposition formula?

??? success "Solution to Exercise 5"
    **Why the ambiguity arises.** The Black-Scholes PDE is naturally a backward equation in $t$, but practitioners often think in terms of time-to-maturity $\tau = T - t$, which decreases as $t$ increases. Since $\frac{\partial}{\partial t} = -\frac{\partial}{\partial \tau}$, the two conventions differ by a sign.

    **Convention 1:** $\Theta_1 = \frac{\partial V}{\partial t}$ (calendar-time theta).

    **Convention 2:** $\Theta_2 = -\frac{\partial V}{\partial t} = \frac{\partial V}{\partial \tau}$ (time-to-maturity theta).

    For a long European call, the option loses value as time passes (time decay). As $t$ increases, $V$ decreases, so:

    - $\Theta_1 = \frac{\partial V}{\partial t} < 0$ (negative)
    - $\Theta_2 = -\frac{\partial V}{\partial t} > 0$ (positive)

    The **P&L decomposition** takes the form:

    $$
    \delta V \approx \Theta_1 \,\delta t + \Delta\,\delta S + \frac{1}{2}\Gamma\,(\delta S)^2
    $$

    under convention 1. Under convention 2, the same decomposition reads:

    $$
    \delta V \approx -\Theta_2 \,\delta t + \Delta\,\delta S + \frac{1}{2}\Gamma\,(\delta S)^2
    $$

    The time decay term must always reduce the option value for long positions (all else equal), so the sign in front of the theta term depends on which convention is adopted. The mathematical content is the same; only the sign bookkeeping changes.

---

**Exercise 6.** Suppose a trader holds a delta-neutral portfolio with $\Gamma = 0.04$ and $\nu = 15$. She observes a simultaneous move $\delta S = +2$ and $\delta \sigma = -0.01$. Compute the approximate change in portfolio value. Which effect dominates, and under what conditions would the other dominate instead?

??? success "Solution to Exercise 6"
    Since the portfolio is delta-neutral ($\Delta = 0$), the first-order spot term vanishes. The approximate P&L is:

    $$
    \delta V \approx \frac{1}{2}\Gamma\,(\delta S)^2 + \nu\,\delta\sigma
    $$

    Substituting $\Gamma = 0.04$, $\delta S = 2$, $\nu = 15$, and $\delta\sigma = -0.01$:

    - Gamma effect: $\frac{1}{2}(0.04)(4) = 0.08$
    - Vega effect: $15 \times (-0.01) = -0.15$

    Total: $\delta V \approx 0.08 - 0.15 = -0.07$.

    The **vega effect dominates** in this scenario. The portfolio loses approximately $\$0.07$ because the volatility drop hurts more than the gamma convexity gain.

    The gamma effect would dominate instead when:

    - The spot move $|\delta S|$ is larger (gamma contribution grows quadratically in $\delta S$)
    - The volatility change $|\delta\sigma|$ is smaller
    - The portfolio has larger $\Gamma$ relative to $\nu$

    Quantitatively, gamma dominates when $\frac{1}{2}\Gamma(\delta S)^2 > |\nu\,\delta\sigma|$, i.e., when $|\delta S| > \sqrt{2|\nu\,\delta\sigma|/\Gamma}$. Here that threshold is $|\delta S| > \sqrt{2 \times 0.15 / 0.04} = \sqrt{7.5} \approx 2.74$.
