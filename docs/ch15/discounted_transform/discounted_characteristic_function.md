# Discounted Characteristic Function

## Theorem (Duffie-Pan-Singleton)

Recall (see [§ Generalized Riccati ODEs](../characteristic_function/generalized_riccati_odes.md) and [§ Extended Riccati System with Discounting](extended_riccati_with_discounting.md)): if $\mathbf{X}_t$ is affine, the discounted characteristic function

$$
\varphi(\mathbf{X}_t,t,T,\mathbf{u}) := \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_t^T r(\mathbf{X}_s)\,ds}\,e^{i\mathbf{u}^T\mathbf{X}_T}\,\big|\,\mathcal{F}_t\right] = e^{A(\mathbf{u},\tau) + \mathbf{B}(\mathbf{u},\tau)^T\mathbf{X}_t}
$$

with $\tau = T-t$. The coefficients $A,\mathbf{B}$ satisfy the DPS Riccati system $\frac{dA}{d\tau} = -r_0 + \mathbf{B}^T a_0 + \tfrac{1}{2}\mathbf{B}^T c_0\mathbf{B}$ and $\frac{d\mathbf{B}}{d\tau} = -r_1 + a_1^T\mathbf{B} + \tfrac{1}{2}\mathbf{B}^T c_1\mathbf{B}$ with initial data $A(\mathbf{u},0)=0$, $\mathbf{B}(\mathbf{u},0) = i\mathbf{u}$. The remainder of this page specializes this result to Black-Scholes as a worked example.


## Example - BS Model

### Discounted Characteristic Function



With the fixed $u$ and $T$,

$$
\begin{array}{lll}
\displaystyle
U(X,t)
:=\varphi(X,t,u,T)
:=e^{-r(T-t)}\mathbb{E^Q}\left[e^{iuX_T}\Big{|}F(t)\right]
=e^{-r(T-t)}\int e^{iuX_T} p(X,t,X_T,T)dX_T
\end{array}
$$

### U(X,t) Satisfies Black-Scholes PDE



Since $e^{-r(T-t)}\int \text{Payoff}(X_T)p(X,t,X_T,T)dX_T$
satisfies the Black-Scholes PDE,
$U(X,t)$ also satisfies the Black-Scholes PDE.
With change of variable $X=\log S$ and $\tau=T-t$,
the Black-Scholes PDE for $U(X,t)$ becomes  

$$
\begin{array}{lll}
\displaystyle
-\frac{\partial U}{\partial \tau}
+\left(r-\frac{1}{2}\sigma^2\right)\frac{\partial U}{\partial X}
+
\frac{1}{2}\sigma^2\frac{\partial^2 U}{\partial X^2}
-rU=0
\end{array}
$$

### Affine Solution



By Duffie-Pan-Singleton, $U(X,t)$ has the following form:

$$
\begin{array}{lll}
\displaystyle
U(X,t)
=e^{A(\tau)+B(\tau)X}
\end{array}
$$

### Riccati Equation



Plugging this to the Black-Scholes PDE, we have

$$
\begin{array}{lll}
\displaystyle
\left(-\frac{\partial A}{\partial \tau}
+\left(r-\frac{1}{2}\sigma^2\right)B
+\frac{1}{2}\sigma^2B^2
-r\right) -\left(\frac{\partial B}{\partial \tau}\right)X=0
\end{array}
$$

or

$$
\begin{array}{lllll}
\text{Collect Rest}&&
\displaystyle
\frac{dA}{d\tau}
=-r+\left(r-\frac{1}{2}\sigma^2\right)B+\frac{1}{2}\sigma^2B^2
&\Rightarrow&
\displaystyle
A=\left[-r+\left(r-\frac{1}{2}\sigma^2\right)iu-\frac{1}{2}\sigma^2u^2\right]\tau
\\
\text{Collect $X$ Term}&&\displaystyle
\frac{dB}{d\tau}
=0&\Rightarrow&
\displaystyle
B=iu\quad(\text{This is from the terminal condition})\\
\end{array}
$$

### Discounted Characteristic Function From BS PDE



$$
\begin{array}{lll}
\displaystyle
\varphi(X_t,t,u,T)
&:=&\displaystyle
\mathbb{E^Q}\left[e^{-\int_t^Tr\left({\bf X}_s\right)ds}e^{i{\bf u}^T{\bf X}_T}\Big{|}F(t)\right]\\
&=&\displaystyle
e^{A(\tau,{\bf u})+{\bf B}^T(\tau,{\bf u}){\bf X}_t}\\
&=&\displaystyle
exp\left(
\left[-r+\left(r-\frac{1}{2}\sigma^2\right)iu-\frac{1}{2}\sigma^2u^2\right]\tau
+
iuX_t\right)
\end{array}
$$

---

## Exercises

**Exercise 1.** Starting from the Duffie-Pan-Singleton formula, verify that setting $\mathbf{u} = \mathbf{0}$ recovers the zero-coupon bond price $P(t,T) = e^{A(\mathbf{0},\tau) + \mathbf{B}(\mathbf{0},\tau)^T \mathbf{X}_t}$. What are the initial conditions for $A$ and $\mathbf{B}$ in the bond pricing case?

??? success "Solution to Exercise 1"
    Setting $\mathbf{u} = \mathbf{0}$ in the Duffie-Pan-Singleton formula gives

    $$
    \varphi(\mathbf{X}_t, t, T, \mathbf{0}) = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_t^T r(\mathbf{X}_{t'})\,dt'} \cdot e^{i \mathbf{0}^T \mathbf{X}_T} \;\middle|\; F(t)\right] = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_t^T r(\mathbf{X}_{t'})\,dt'} \;\middle|\; F(t)\right]
    $$

    The right-hand side is precisely the zero-coupon bond price $P(t, T)$. In the exponential-affine form this becomes

    $$
    P(t, T) = e^{A(\mathbf{0}, \tau) + \mathbf{B}(\mathbf{0}, \tau)^T \mathbf{X}_t}
    $$

    The initial conditions at $\tau = 0$ (i.e., $T = t$) are $A(\mathbf{0}, 0) = 0$ and $\mathbf{B}(\mathbf{0}, 0) = i \mathbf{0} = \mathbf{0}$. This reflects the fact that a bond at maturity pays $\$1$ regardless of the state, so $P(t, t) = e^{0 + \mathbf{0}^T \mathbf{X}_t} = 1$.

---

**Exercise 2.** In the Black-Scholes example, confirm that $B(\tau) = iu$ (constant) satisfies $\frac{dB}{d\tau} = 0$ with initial condition $B(0) = iu$. Then substitute $B = iu$ into the $A$-equation and integrate to verify $A(\tau) = [-r + (r - \frac{1}{2}\sigma^2)iu - \frac{1}{2}\sigma^2 u^2]\tau$.

??? success "Solution to Exercise 2"
    The $B$-equation from the Riccati system is $\frac{dB}{d\tau} = 0$ with initial condition $B(0) = iu$. The unique solution of $\frac{dB}{d\tau} = 0$ is $B(\tau) = B(0) = iu$ for all $\tau$, confirming $B$ is constant.

    Substituting $B = iu$ into the $A$-equation:

    $$
    \frac{dA}{d\tau} = -r + \left(r - \tfrac{1}{2}\sigma^2\right)(iu) + \tfrac{1}{2}\sigma^2(iu)^2 = -r + \left(r - \tfrac{1}{2}\sigma^2\right)iu - \tfrac{1}{2}\sigma^2 u^2
    $$

    Since the right-hand side is constant in $\tau$, integrating from $0$ to $\tau$ with $A(0) = 0$ gives

    $$
    A(\tau) = \left[-r + \left(r - \tfrac{1}{2}\sigma^2\right)iu - \tfrac{1}{2}\sigma^2 u^2\right]\tau
    $$

    which matches the stated result.

---

**Exercise 3.** Using the discounted characteristic function for the Black-Scholes model, compute $\varphi(X_t, t, u, T)$ at $u = -i$ (i.e., evaluate $\mathbb{E}^{\mathbb{Q}}[e^{-r\tau}S_T \mid S_t]$). Verify that you recover $S_t$, confirming that the discounted stock price is a martingale.

??? success "Solution to Exercise 3"
    Setting $u = -i$ in the discounted characteristic function with $B = iu = i(-i) = 1$ and

    $$
    A = \left[-r + (r - \tfrac{1}{2}\sigma^2)i(-i) - \tfrac{1}{2}\sigma^2(-i)^2\right]\tau = \left[-r + (r - \tfrac{1}{2}\sigma^2) + \tfrac{1}{2}\sigma^2\right]\tau = 0
    $$

    Therefore

    $$
    \varphi(X_t, t, -i, T) = e^{0 + 1 \cdot X_t} = e^{X_t} = S_t
    $$

    On the other hand, by definition

    $$
    \varphi(X_t, t, -i, T) = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-r\tau} e^{i(-i)X_T} \;\middle|\; F(t)\right] = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-r\tau} e^{X_T} \;\middle|\; F(t)\right] = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-r\tau} S_T \;\middle|\; F(t)\right]
    $$

    Equating gives $\mathbb{E}^{\mathbb{Q}}[e^{-r\tau} S_T \mid F(t)] = S_t$, confirming that the discounted stock price $e^{-rt}S_t$ is a $\mathbb{Q}$-martingale.

---

**Exercise 4.** For a one-dimensional CIR short-rate model $r_t = X_t$ with $r_0 = 0$ and $r_1 = 1$, write down the extended Riccati equations for the discounted characteristic function. Identify how the $-r_0$ and $-r_1$ terms modify the standard (undiscounted) Riccati system.

??? success "Solution to Exercise 4"
    For the one-dimensional CIR model $dX_t = \kappa(\theta - X_t)\,dt + \xi\sqrt{X_t}\,dW_t$ with $r_t = X_t$, the affine parameters are:

    - Drift: $b_0 = \kappa\theta$, $b_1 = -\kappa$
    - Diffusion: $c_0 = 0$, $c_1 = \xi^2$
    - Discounting: $r_0 = 0$, $r_1 = 1$ (since $r(X) = X$)

    The extended Riccati equations are:

    $$
    \frac{dA}{d\tau} = -r_0 + B \cdot b_0 + \tfrac{1}{2}B^2 c_0 = \kappa\theta B
    $$

    $$
    \frac{dB}{d\tau} = -r_1 + b_1 B + \tfrac{1}{2}c_1 B^2 = -1 - \kappa B + \tfrac{1}{2}\xi^2 B^2
    $$

    Compared to the standard (undiscounted) Riccati system where $\frac{dB}{d\tau} = -\kappa B + \frac{1}{2}\xi^2 B^2$ and $\frac{dA}{d\tau} = \kappa\theta B$, the discounting adds the constant term $-r_1 = -1$ to the $B$-equation and the term $-r_0 = 0$ to the $A$-equation. The $-1$ in the $B$-equation turns the homogeneous Riccati ODE into a full (inhomogeneous) Riccati equation, which is the source of the more complex closed-form solutions seen in CIR bond pricing.

---

**Exercise 5.** Explain why the Black-Scholes PDE for $U(X,t)$ has no $X$-dependent coefficient in the $\frac{dB}{d\tau}$ equation, yielding $B(\tau) = iu$ (constant). Under what conditions on the model would $B(\tau)$ be non-constant?

??? success "Solution to Exercise 5"
    In the Black-Scholes model the drift and volatility coefficients of $X = \log S$ are:

    - Drift: $b(X) = r - \frac{1}{2}\sigma^2$ (constant, no $X$-dependence)
    - Diffusion: $a(X) = \sigma^2$ (constant, no $X$-dependence)

    In affine notation, $b_1 = 0$ and $c_1 = 0$, so the Riccati equation for $B$ becomes

    $$
    \frac{dB}{d\tau} = b_1 B + \tfrac{1}{2}c_1 B^2 = 0
    $$

    The right-hand side vanishes identically, making $B(\tau) = iu$ constant for all $\tau$.

    For $B(\tau)$ to be non-constant, we need $b_1 \neq 0$ or $c_1 \neq 0$, meaning the drift or the diffusion coefficient must depend on $X$. This occurs when:

    - The drift is state-dependent ($b_1 \neq 0$), as in mean-reverting models like Vasicek or CIR
    - The volatility is state-dependent ($c_1 \neq 0$), as in the CIR model where $\sigma(X) = \xi\sqrt{X}$

    In either case the $B$-equation becomes a genuine (possibly nonlinear) ODE with a non-trivial $\tau$-dependent solution.

---

**Exercise 6.** Show that the discounted characteristic function $\varphi(X_t, t, u, T)$ satisfies $|\varphi| \leq e^{A_{\text{re}}(\tau) + B_{\text{re}}(\tau)X_t}$ where subscript "re" denotes the real part. For the BS case, compute $|\varphi|$ explicitly and verify it equals $e^{(-r - \frac{1}{2}\sigma^2 u^2)\tau}$ when $u$ is real.

??? success "Solution to Exercise 6"
    Since $\varphi = e^{A(\tau) + B(\tau)X_t}$ with $A$ and $B$ generally complex-valued, we have

    $$
    |\varphi| = |e^{A + BX_t}| = e^{\operatorname{Re}(A + BX_t)} = e^{A_{\text{re}}(\tau) + B_{\text{re}}(\tau)X_t}
    $$

    where $A_{\text{re}} = \operatorname{Re}(A)$ and $B_{\text{re}} = \operatorname{Re}(B)$. This follows directly from $|e^z| = e^{\operatorname{Re}(z)}$ for any complex number $z$.

    For the Black-Scholes case with real $u$, we have $B = iu$ (purely imaginary), so $B_{\text{re}} = 0$. The real part of $A$ is

    $$
    A_{\text{re}} = \operatorname{Re}\!\left[\left(-r + (r - \tfrac{1}{2}\sigma^2)iu - \tfrac{1}{2}\sigma^2 u^2\right)\tau\right] = \left(-r - \tfrac{1}{2}\sigma^2 u^2\right)\tau
    $$

    since the term $(r - \frac{1}{2}\sigma^2)iu$ is purely imaginary when $u$ is real. Therefore

    $$
    |\varphi| = e^{(-r - \frac{1}{2}\sigma^2 u^2)\tau}
    $$

    This is strictly less than $1$ for $\tau > 0$ (due to both discounting and the oscillatory decay), confirming boundedness of the discounted characteristic function.
