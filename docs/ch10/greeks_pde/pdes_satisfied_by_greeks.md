# PDEs Satisfied by Greeks


A clean way to obtain PDEs for Greeks is to treat Greeks as solutions of **sensitivity PDEs**.

---

## Operator form


Define the Black–Scholes operator

\[
\mathcal{A}V
:=
\frac{\partial V}{\partial t}
+\frac{1}{2}\sigma^2 S^2 V_{SS}
+rS V_S
-rV.
\]


Then \(V\) solves \(\mathcal{A}V=0\).

---

## Vega


Let \(\nu=V_\sigma\). Differentiate \(\mathcal{A}V=0\) in \(\sigma\):

\[
\mathcal{A}\nu = -\sigma S^2 V_{SS}.
\]


With payoff independent of \(\sigma\),

\[
\boxed{\nu(T,S)=0.}
\]



---

## Rho


Let \(\rho=V_r\). Differentiating in \(r\) yields

\[
\boxed{
\frac{\partial \rho}{\partial t}
+\frac{1}{2}\sigma^2 S^2 \rho_{SS}
+rS\rho_S
-r\rho
=
V - S V_S,
\qquad \rho(T,S)=0.
}
\]



---

## Theta identity


From the PDE,

\[
\boxed{
\Theta
=
\frac{\partial V}{\partial t}
=
-\frac{1}{2}\sigma^2 S^2 V_{SS} - rS V_S + rV.
}
\]



---

## What to remember


- Vega and rho satisfy inhomogeneous parabolic PDEs with zero terminal data.
- Theta can be computed directly from $V,\Delta,\Gamma$ using the PDE.

---

## Exercises

**Exercise 1.** Starting from $\mathcal{A}V = 0$, differentiate with respect to $\sigma$ to obtain the vega PDE $\mathcal{A}\nu = -\sigma S^2 V_{SS}$. Explain why the right-hand side is always non-positive for a long call (where $V_{SS} = \Gamma > 0$) and what this implies about the behavior of vega.

??? success "Solution to Exercise 1"
    Starting from $\mathcal{A}V = 0$:

    $$
    \frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 V_{SS} + rSV_S - rV = 0
    $$

    Differentiate with respect to $\sigma$. Let $\nu = V_\sigma$. Since $\sigma$ appears only in the diffusion coefficient $\frac{1}{2}\sigma^2 S^2$, we get:

    $$
    \frac{\partial \nu}{\partial t} + \frac{1}{2}\sigma^2 S^2 \nu_{SS} + rS\nu_S - r\nu + \sigma S^2 V_{SS} = 0
    $$

    The term $\sigma S^2 V_{SS}$ comes from $\frac{\partial}{\partial \sigma}(\frac{1}{2}\sigma^2 S^2 V_{SS}) = \sigma S^2 V_{SS} + \frac{1}{2}\sigma^2 S^2 \nu_{SS}$. Rearranging:

    $$
    \mathcal{A}\nu = -\sigma S^2 V_{SS} = -\sigma S^2 \Gamma
    $$

    For a long call, $\Gamma = V_{SS} > 0$ everywhere for $t < T$ (the call price is convex in $S$). Therefore the right-hand side $-\sigma S^2 \Gamma < 0$ is strictly negative.

    The sign of the source term has a direct interpretation. Since $\mathcal{A}\nu < 0$ with $\nu(T,S) = 0$, the maximum principle for parabolic PDEs implies $\nu \geq 0$ for all $t < T$. This confirms that vega is non-negative: increasing volatility increases the call price. Intuitively, the negative source term acts as a "heat source" when solving backward in time, continuously adding positive value to $\nu$ as we move away from maturity.

---

**Exercise 2.** The rho PDE has source term $V - SV_S$. For an ATM call, estimate the sign and magnitude of $V - S\Delta$ and use this to explain whether rho is positive or negative.

??? success "Solution to Exercise 2"
    The rho PDE is:

    $$
    \mathcal{A}\rho = V - SV_S = V - S\Delta
    $$

    For an ATM call ($S = K$), we evaluate $V - S\Delta$ using the Black--Scholes formulas. At the money, $d_1 = \frac{(r + \frac{1}{2}\sigma^2)\tau}{\sigma\sqrt{\tau}}$ and $d_2 = d_1 - \sigma\sqrt{\tau}$.

    The call price is $V = SN(d_1) - Ke^{-r\tau}N(d_2)$, and $\Delta = N(d_1)$, so:

    $$
    V - S\Delta = SN(d_1) - Ke^{-r\tau}N(d_2) - SN(d_1) = -Ke^{-r\tau}N(d_2)
    $$

    Since $N(d_2) > 0$ and $Ke^{-r\tau} > 0$, the source term is:

    $$
    V - S\Delta = -Ke^{-r\tau}N(d_2) < 0
    $$

    For an ATM option, $d_2 \approx 0$ for small $\tau$, so $N(d_2) \approx \frac{1}{2}$, giving $V - S\Delta \approx -\frac{1}{2}Ke^{-r\tau}$.

    Since the source term is negative and $\rho(T,S) = 0$, the maximum principle applied to the backward parabolic PDE gives $\rho > 0$ for $t < T$. Financially, this makes sense: higher interest rates reduce the present value of the strike, making the call more valuable. Using the closed-form expression, $\rho = K\tau e^{-r\tau}N(d_2) > 0$, confirming the analysis.

---

**Exercise 3.** Show that theta is not an independent Greek: it can be computed algebraically from $V$, $\Delta$, and $\Gamma$ using the Black--Scholes PDE. Why does this make theta fundamentally different from delta, gamma, vega, and rho?

??? success "Solution to Exercise 3"
    From the Black--Scholes PDE:

    $$
    \frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 V_{SS} + rSV_S - rV = 0
    $$

    Solving for $\Theta = \frac{\partial V}{\partial t}$:

    $$
    \Theta = -\frac{1}{2}\sigma^2 S^2 \Gamma - rS\Delta + rV
    $$

    This is a purely algebraic relation: given the current values of $V$, $\Delta = V_S$, and $\Gamma = V_{SS}$, theta is determined without solving any additional equation or computing any additional derivative.

    This makes theta fundamentally different from the other Greeks:

    - **Delta** ($V_S$) requires differentiating $V$ with respect to $S$, which involves independent information about how $V$ changes with spot.
    - **Gamma** ($V_{SS}$) is a second spatial derivative, carrying further independent information about curvature.
    - **Vega** ($V_\sigma$) and **rho** ($V_r$) are sensitivities to model parameters, each satisfying their own inhomogeneous PDEs with independent source terms.
    - **Theta** ($V_t$), by contrast, is completely determined by the PDE constraint. It is not an independent degree of freedom but rather the "residual" that ensures the PDE is satisfied.

    In practice, this means theta never needs to be computed separately. A trader who knows $V$, $\Delta$, and $\Gamma$ can immediately compute $\Theta$. This also underlies the well-known theta--gamma trade-off: for a delta-hedged portfolio, $\Theta \approx -\frac{1}{2}\sigma^2 S^2 \Gamma$, showing that positive gamma comes at the cost of negative theta (time decay).

---

**Exercise 4.** The vega PDE $\mathcal{A}\nu = -\sigma S^2 \Gamma$ with $\nu(T,S) = 0$ can be interpreted as a backward heat equation with a source term. Using the Duhamel principle, express $\nu(t,S)$ as an integral over the remaining time involving $\Gamma$. How does this connect to the closed-form formula $\nu = S\sqrt{\tau}N'(d_1)$?

??? success "Solution to Exercise 4"
    The vega PDE is $\mathcal{A}\nu = -\sigma S^2 \Gamma$ with $\nu(T,S) = 0$. This is an inhomogeneous backward parabolic equation. By the Duhamel principle (variation of parameters for PDEs), the solution can be written as a time integral over the source term, propagated by the homogeneous Green's function.

    Let $P(t,S;u,S')$ denote the transition density (Green's function) of the Black--Scholes operator, so that the homogeneous solution with terminal data $f$ at time $u$ is $\int P(t,S;u,S')f(S')\,dS'$. Then:

    $$
    \nu(t,S) = \int_t^T \!\!\int_0^\infty P(t,S;u,S')\,\sigma (S')^2 \Gamma(u,S')\,dS'\,du
    $$

    The sign is positive because the source $-\sigma S^2 \Gamma$ is negative, and the backward-in-time integration reverses the sign.

    Under the risk-neutral measure, this becomes an expectation:

    $$
    \nu(t,S) = \sigma \,\mathbb{E}^{\mathbb{Q}}\!\left[\int_t^T S_u^2 \,\Gamma(u, S_u)\,du \;\Big|\; S_t = S\right]
    $$

    Now, the Black--Scholes gamma satisfies $S^2\Gamma = \frac{S\,N'(d_1)}{\sigma\sqrt{u - t_0}}$ (adjusting time indices), and carrying out the integration yields:

    $$
    \nu(t,S) = S\sqrt{\tau}\,N'(d_1)
    $$

    This is exactly the closed-form vega formula. The Duhamel representation reveals that vega is the time-integrated effect of gamma weighted by the squared stock price -- a beautiful connection showing that vega and gamma are intimately linked through the PDE structure.

---

**Exercise 5.** Derive the PDE satisfied by the second-order Greek $\frac{\partial^2 V}{\partial \sigma^2}$ (volga) by differentiating the vega PDE with respect to $\sigma$. What is the source term, and what is the terminal condition?

??? success "Solution to Exercise 5"
    Start from the vega PDE:

    $$
    \mathcal{A}\nu = -\sigma S^2 \Gamma
    $$

    where $\nu = V_\sigma$. Differentiate both sides with respect to $\sigma$. Let $\mathcal{V} = \frac{\partial^2 V}{\partial \sigma^2}$ (volga). On the left side:

    $$
    \frac{\partial}{\partial \sigma}(\mathcal{A}\nu) = \mathcal{A}\mathcal{V} + \sigma S^2 \nu_{SS}
    $$

    The extra term $\sigma S^2 \nu_{SS}$ arises because $\mathcal{A}$ depends on $\sigma$ through the $\frac{1}{2}\sigma^2 S^2 \partial_{SS}$ term, so $\frac{\partial}{\partial \sigma}(\frac{1}{2}\sigma^2 S^2 \nu_{SS}) = \sigma S^2 \nu_{SS} + \frac{1}{2}\sigma^2 S^2 \mathcal{V}_{SS}$.

    On the right side:

    $$
    \frac{\partial}{\partial \sigma}(-\sigma S^2 \Gamma) = -S^2 \Gamma - \sigma S^2 \frac{\partial \Gamma}{\partial \sigma}
    $$

    Note that $\frac{\partial \Gamma}{\partial \sigma} = \frac{\partial}{\partial \sigma}V_{SS} = \nu_{SS}$. Combining:

    $$
    \mathcal{A}\mathcal{V} + \sigma S^2 \nu_{SS} = -S^2\Gamma - \sigma S^2 \nu_{SS}
    $$

    $$
    \mathcal{A}\mathcal{V} = -S^2\Gamma - 2\sigma S^2 \nu_{SS}
    $$

    The source term is $-S^2\Gamma - 2\sigma S^2 \nu_{SS}$, where $\nu_{SS} = \frac{\partial^3 V}{\partial S^2 \partial \sigma}$ is the "cross-Greek" sometimes called vanna-of-gamma or gamma sensitivity to volatility.

    The terminal condition follows from the fact that the payoff does not depend on $\sigma$:

    $$
    \mathcal{V}(T,S) = \frac{\partial^2 \Phi}{\partial \sigma^2} = 0
    $$

---

**Exercise 6.** In a model where the interest rate $r$ is stochastic, the operator $\mathcal{A}$ itself depends on $r$. Explain qualitatively how the PDE for rho would change, and why the simple identity $\Theta = rV - rS\Delta - \frac{1}{2}\sigma^2 S^2 \Gamma$ may no longer hold.

??? success "Solution to Exercise 6"
    In a stochastic interest rate model, the pricing PDE becomes a multi-dimensional PDE. For example, if $r = r_t$ follows its own SDE (such as in the Hull--White or CIR model), the option price $V(t, S, r)$ satisfies a two-factor PDE:

    $$
    \frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 V_{SS} + \frac{1}{2}\sigma_r^2 V_{rr} + \rho_{Sr}\sigma\sigma_r S\, V_{Sr} + rSV_S + \mu_r V_r - rV = 0
    $$

    where $\sigma_r$ is the rate volatility, $\mu_r$ is the risk-neutral drift of $r$, and $\rho_{Sr}$ is the correlation.

    Differentiating with respect to $r$ to derive the rho PDE becomes much more involved because:

    1. The operator itself depends on $r$ in multiple places: the drift $rS$, the discount $-rV$, and any $r$-dependent terms in $\mu_r$, $\sigma_r$.
    2. Differentiating $rSV_S$ gives $SV_S + rSV_{Sr}$ and differentiating $-rV$ gives $-V - rV_r$. But additionally, $\mu_r$ and $\sigma_r$ may depend on $r$, contributing further terms.
    3. The operator $\mathcal{A}$ now involves mixed partial derivatives $V_{Sr}$, and the rho PDE inherits additional cross-derivative terms.

    The simple theta identity $\Theta = rV - rS\Delta - \frac{1}{2}\sigma^2 S^2\Gamma$ breaks down because the one-factor Black--Scholes PDE is no longer the correct pricing equation. The full PDE includes terms involving $V_r$, $V_{rr}$, and $V_{Sr}$ that contribute to theta:

    $$
    \Theta = rV - rS\Delta - \frac{1}{2}\sigma^2 S^2\Gamma - \frac{1}{2}\sigma_r^2 V_{rr} - \rho_{Sr}\sigma\sigma_r S\,V_{Sr} - \mu_r V_r
    $$

    Theta is no longer determined by $V$, $\Delta$, and $\Gamma$ alone -- it also requires knowledge of rate sensitivities. The clean separation of Greeks that holds in the constant-rate Black--Scholes world is a consequence of the one-dimensional structure and breaks down in multi-factor models.
