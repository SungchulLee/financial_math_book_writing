# Discounted Characteristic Function

## Theorem (Duffie-Pann-Singleton)



If ${\bf X}_t$ is affine, the discounted characteristic function (ChF) has the following affine form:

$$
\begin{array}{lll}
\displaystyle
\varphi({\bf X}_t,t,T,{\bf u})
:=
\mathbb{E^Q}\left[e^{-\int_t^Tr\left({\bf X}_{t'}\right)dt'}e^{i{\bf u}^T{\bf X}_T}\Big{|}F(t)\right]
=
e^{A({\bf u},\tau)+{\bf B}({\bf u},\tau)^T{\bf X}_t}
\end{array}
$$

where $\tau=T−t$. Furthermore,
The coefficients $A$ and ${\bf B}$ satisfy the following Riccati Equation:

$$\begin{array}{lll}
\displaystyle
\frac{dA}{d\tau}
&=&\displaystyle
-r_0+{\bf B}^Ta_0+\frac{1}{2}{\bf B}^Tc_0{\bf B}\\
\displaystyle
\frac{d{\bf B}}{d\tau}
&=&\displaystyle
-r_1+a_1^T{\bf B}+\frac{1}{2}{\bf B}^Tc_1{\bf B}\\
\end{array}$$

with the initial condition

$$\begin{array}{lll}
\displaystyle
A({\bf u},0)
&=&\displaystyle
0\\
\displaystyle
{\bf B}({\bf u},0)
&=&\displaystyle
i{\bf u}^T\\
\end{array}$$


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

---

**Exercise 2.** In the Black-Scholes example, confirm that $B(\tau) = iu$ (constant) satisfies $\frac{dB}{d\tau} = 0$ with initial condition $B(0) = iu$. Then substitute $B = iu$ into the $A$-equation and integrate to verify $A(\tau) = [-r + (r - \frac{1}{2}\sigma^2)iu - \frac{1}{2}\sigma^2 u^2]\tau$.

---

**Exercise 3.** Using the discounted characteristic function for the Black-Scholes model, compute $\varphi(X_t, t, u, T)$ at $u = -i$ (i.e., evaluate $\mathbb{E}^{\mathbb{Q}}[e^{-r\tau}S_T \mid S_t]$). Verify that you recover $S_t$, confirming that the discounted stock price is a martingale.

---

**Exercise 4.** For a one-dimensional CIR short-rate model $r_t = X_t$ with $r_0 = 0$ and $r_1 = 1$, write down the extended Riccati equations for the discounted characteristic function. Identify how the $-r_0$ and $-r_1$ terms modify the standard (undiscounted) Riccati system.

---

**Exercise 5.** Explain why the Black-Scholes PDE for $U(X,t)$ has no $X$-dependent coefficient in the $\frac{dB}{d\tau}$ equation, yielding $B(\tau) = iu$ (constant). Under what conditions on the model would $B(\tau)$ be non-constant?

---

**Exercise 6.** Show that the discounted characteristic function $\varphi(X_t, t, u, T)$ satisfies $|\varphi| \leq e^{A_{\text{re}}(\tau) + B_{\text{re}}(\tau)X_t}$ where subscript "re" denotes the real part. For the BS case, compute $|\varphi|$ explicitly and verify it equals $e^{(-r - \frac{1}{2}\sigma^2 u^2)\tau}$ when $u$ is real.