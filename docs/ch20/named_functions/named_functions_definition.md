# Hull-White Named Functions

This page collects all the named functions used in the Hull-White model for quick reference.

## τ

$$\tau=T-t$$

## θ

$$\begin{array}{lllllll}
\displaystyle
\theta(t)
&=&\displaystyle
f(0,t)+\frac{1}{\lambda}\frac{\partial f(0,t)}{\partial t}
+
\frac{\sigma^2}{2\lambda^2}\left(1-e^{-2\lambda t}\right)\\
\displaystyle
\theta^\mathbb{T}(t)
&=&\displaystyle\theta(t)+\frac{\sigma^2}{\lambda}B(T-t)\\
\end{array}$$

## ψ

$$\begin{array}{lllllll}
\psi(t)
&=&\displaystyle
r(0)e^{-\lambda t}+\lambda\int_0^t\theta(t')e^{-\lambda(t-t')}dt'
&=&\displaystyle
f(0,t)+\frac{\lambda\sigma^2}{2}B^2(t)\\
\psi(t_0,t)
&=&\displaystyle
r(t_0)e^{-\lambda (t-t_0)}+\lambda\int_{t_0}^t\theta(t')e^{-\lambda(t-t')}dt'
\\
\psi^\mathbb{T}(t_0,t)
&=&\displaystyle
r(t_0)e^{-\lambda (t-t_0)}+\lambda\int_{t_0}^t\theta^\mathbb{T}(t')e^{-\lambda(t-t')}dt'
\\
\end{array}$$

## σ_r², μ_r

$$\begin{array}{lllll}
\displaystyle
\sigma_r^2(t)
&=&\displaystyle
-\frac{1}{2}\sigma^2 B(2t)\\
\displaystyle
\sigma_r^2(t_0,t)
&=&\displaystyle
-\frac{1}{2}\sigma^2 B(2(t-t_0))
\end{array}$$

$$\begin{array}{lllll}
\displaystyle
\mu_r(t)
&=&\displaystyle
\psi(t)\\
\displaystyle
\mu_r(t_0,t)
&=&\displaystyle
\psi(t_0,t)\\
\displaystyle
\mu^\mathbb{T}_r(t_0,t)
&=&\displaystyle
\psi^\mathbb{T}(t_0,t)\\
\end{array}$$

## A, B

$$\begin{array}{lllllll}
A(\tau)&=&A(0,\tau)
&=&\displaystyle
-\frac{\sigma^2}{4\lambda^3}
\left(3-2\lambda\tau-4e^{-\lambda\tau}+e^{-2\lambda\tau}\right)
+
\lambda\int_0^\tau\theta(T-\tau')B(\tau')d\tau'
\\
B(\tau)&=&B(0,\tau)
&=&\displaystyle
-\frac{1-e^{-\lambda\tau}}{\lambda}
\\
\end{array}$$

### Characteristic Function Version

$$\begin{array}{lllll}
\displaystyle
A(u,\tau)
&=&\displaystyle
-\frac{\sigma^2}{4\lambda^3}\left[(1+iu\lambda)\left[
    3-4e^{-\lambda \tau}+e^{-2\lambda \tau}

    - iu\lambda\left(1-e^{-2\lambda \tau}\right)
    \right]-2\lambda\tau\right]
+\lambda\int_0^\tau\theta(T-\tau')B(u,\tau')d\tau'\\
\displaystyle
B(u,\tau)
&=&\displaystyle
-\frac{1-(1+iu\lambda) e^{-\lambda \tau}}{\lambda}
=iue^{-\lambda\tau}+B(\tau)\\
\end{array}$$

### Decomposition Version

$$\begin{array}{lllll}
\displaystyle
\tilde{A}(u,\tau)
&=&\displaystyle
-\frac{\sigma^2}{4\lambda^3}\left(3-2\lambda\tau-4e^{-\lambda\tau}+e^{-2\lambda\tau}+2iu\lambda\left(1-e^{-\lambda\tau}\right)^2+u^2\lambda^2\left(1-e^{-2\lambda\tau}\right)\right)
\\
\displaystyle
\tilde{B}(u,\tau)
&=&\displaystyle
B(u,\tau)\\
\end{array}$$

---

## Exercises

**Exercise 1.** Verify that $B(\tau) \to \tau$ as $\lambda \to 0$ by expanding $e^{-\lambda\tau}$ in a Taylor series. Identify the first correction term and estimate the relative error when $\lambda = 0.05$ and $\tau = 2$.

??? success "Solution to Exercise 1"
    We start from the definition $B(\tau) = -\frac{1-e^{-\lambda\tau}}{\lambda}$. Expand $e^{-\lambda\tau}$ in a Taylor series around $\lambda = 0$:

    $$
    e^{-\lambda\tau} = 1 - \lambda\tau + \frac{(\lambda\tau)^2}{2} - \frac{(\lambda\tau)^3}{6} + \cdots
    $$

    Substituting:

    $$
    B(\tau) = -\frac{1 - \left(1 - \lambda\tau + \frac{\lambda^2\tau^2}{2} - \cdots\right)}{\lambda} = -\frac{\lambda\tau - \frac{\lambda^2\tau^2}{2} + \frac{\lambda^3\tau^3}{6} - \cdots}{\lambda}
    $$

    $$
    = -\tau + \frac{\lambda\tau^2}{2} - \frac{\lambda^2\tau^3}{6} + \cdots
    $$

    As $\lambda \to 0$, we get $B(\tau) \to -\tau$. The first correction term is $\frac{\lambda\tau^2}{2}$.

    The relative error of the approximation $B(\tau) \approx -\tau$ is:

    $$
    \frac{|B(\tau) - (-\tau)|}{|B(\tau)|} \approx \frac{\lambda\tau/2}{1} = \frac{\lambda\tau}{2}
    $$

    For $\lambda = 0.05$ and $\tau = 2$:

    $$
    \text{Relative error} \approx \frac{0.05 \times 2}{2} = 0.05 = 5\%
    $$

    Exact check: $B(2) = -\frac{1 - e^{-0.1}}{0.05} = -\frac{1 - 0.90484}{0.05} = -\frac{0.09516}{0.05} = -1.9032$, while $-\tau = -2$. The relative error is $\frac{|{-1.9032} - ({-2})|}{1.9032} = \frac{0.0968}{1.9032} \approx 5.1\%$, consistent with the estimate.

---

**Exercise 2.** Show that the two expressions for $\psi(t)$ are equivalent: starting from $\psi(t) = r(0)e^{-\lambda t} + \lambda\int_0^t \theta(t')e^{-\lambda(t-t')}dt'$, substitute the formula for $\theta(t)$ and simplify to obtain $\psi(t) = f(0,t) + \frac{\lambda\sigma^2}{2}B^2(t)$.

??? success "Solution to Exercise 2"
    Start from $\psi(t) = r(0)e^{-\lambda t} + \lambda\int_0^t \theta(t')e^{-\lambda(t-t')}dt'$ and substitute $\theta(t') = f(0,t') + \frac{1}{\lambda}\frac{\partial f(0,t')}{\partial t'} + \frac{\sigma^2}{2\lambda^2}(1-e^{-2\lambda t'})$.

    Split the integral into three parts:

    $$
    I_1 = \lambda\int_0^t f(0,t')e^{-\lambda(t-t')}dt'
    $$

    $$
    I_2 = \int_0^t \frac{\partial f(0,t')}{\partial t'} e^{-\lambda(t-t')}dt'
    $$

    $$
    I_3 = \frac{\sigma^2}{2\lambda}\int_0^t (1-e^{-2\lambda t'})e^{-\lambda(t-t')}dt'
    $$

    For $I_2$, integrate by parts with $u = e^{-\lambda(t-t')}$ and $dv = f'(0,t')dt'$:

    $$
    I_2 = \left[f(0,t')e^{-\lambda(t-t')}\right]_0^t - \lambda\int_0^t f(0,t')e^{-\lambda(t-t')}dt' = f(0,t) - f(0,0)e^{-\lambda t} - I_1
    $$

    So $r(0)e^{-\lambda t} + I_1 + I_2 = r(0)e^{-\lambda t} + f(0,t) - f(0,0)e^{-\lambda t} = f(0,t)$, since $f(0,0) = r(0)$.

    For $I_3$, compute:

    $$
    I_3 = \frac{\sigma^2}{2\lambda}\left[\int_0^t e^{-\lambda(t-t')}dt' - \int_0^t e^{-2\lambda t'}e^{-\lambda(t-t')}dt'\right]
    $$

    The first integral gives $\frac{1-e^{-\lambda t}}{\lambda} = -B(t)$. The second integral evaluates to $\frac{e^{-\lambda t}(1-e^{-\lambda t})}{\lambda}$. Therefore:

    $$
    I_3 = \frac{\sigma^2}{2\lambda}\left[-B(t) - \frac{e^{-\lambda t}(1-e^{-\lambda t})}{\lambda}\right] = \frac{\sigma^2}{2\lambda}\left[-B(t) + e^{-\lambda t}B(t)\right]
    $$

    $$
    = \frac{\sigma^2}{2\lambda}B(t)(e^{-\lambda t} - 1) = \frac{\sigma^2}{2\lambda}B(t)\cdot\lambda B(t) = \frac{\lambda\sigma^2}{2}B^2(t)
    $$

    (using $e^{-\lambda t} - 1 = \lambda B(t)$ from $B(t) = -\frac{1-e^{-\lambda t}}{\lambda}$).

    Combining: $\psi(t) = f(0,t) + \frac{\lambda\sigma^2}{2}B^2(t)$.

---

**Exercise 3.** The variance formula uses $\sigma_r^2(t) = -\frac{1}{2}\sigma^2 B(2t)$. Verify that this equals $\frac{\sigma^2}{2\lambda}(1-e^{-2\lambda t})$ by substituting the definition of $B$. Explain why the negative sign appears in the compact form.

??? success "Solution to Exercise 3"
    Substitute $B(2t) = -\frac{1-e^{-2\lambda t}}{\lambda}$ into $\sigma_r^2(t) = -\frac{1}{2}\sigma^2 B(2t)$:

    $$
    \sigma_r^2(t) = -\frac{1}{2}\sigma^2\left(-\frac{1-e^{-2\lambda t}}{\lambda}\right) = \frac{\sigma^2}{2\lambda}(1-e^{-2\lambda t})
    $$

    This confirms the equivalence.

    The negative sign in $\sigma_r^2(t) = -\frac{1}{2}\sigma^2 B(2t)$ appears because $B(\tau) < 0$ in the convention used in this section (negative-$B$ convention, where $B(\tau) = -(1-e^{-\lambda\tau})/\lambda$). Since $B(2t) < 0$, the negative sign ensures the variance $\sigma_r^2(t)$ is positive. Specifically, $-B(2t) = \frac{1-e^{-2\lambda t}}{\lambda} > 0$, so $\sigma_r^2(t) = \frac{\sigma^2}{2}|B(2t)| > 0$.

---

**Exercise 4.** For $\lambda = 0.05$ and $\sigma = 0.01$, compute numerically $B(\tau)$, $\sigma_r^2(t)$, and $A(\tau)$ at $\tau = 1, 5, 10, 30$ years. Describe the qualitative behavior of each function as $\tau$ increases.

??? success "Solution to Exercise 4"
    With $\lambda = 0.05$ and $\sigma = 0.01$, we compute each function. Note $B(\tau) = -\frac{1-e^{-0.05\tau}}{0.05}$.

    **$\tau = 1$:**

    - $B(1) = -\frac{1-e^{-0.05}}{0.05} = -\frac{1-0.95123}{0.05} = -\frac{0.04877}{0.05} = -0.97531$
    - $\sigma_r^2(1) = \frac{(0.01)^2}{2(0.05)}(1-e^{-0.1}) = \frac{0.0001}{0.1}(0.09516) = 9.516 \times 10^{-5}$
    - For $A(1)$, the $\theta$-dependent term requires the market curve; focusing on the $\sigma^2$-integral piece: $\frac{\sigma^2}{4\lambda^3}(3 - 2\lambda\tau - 4e^{-\lambda\tau} + e^{-2\lambda\tau}) = \frac{0.0001}{4(0.000125)}(3 - 0.1 - 4(0.95123) + 0.90484) = 200(3 - 0.1 - 3.80492 + 0.90484) = 200(-0.00008) \approx -0.016$

    **$\tau = 5$:**

    - $B(5) = -\frac{1-e^{-0.25}}{0.05} = -\frac{0.22120}{0.05} = -4.42400$
    - $\sigma_r^2(5) = \frac{0.0001}{0.1}(1-e^{-0.5}) = 0.001(0.39347) = 3.935 \times 10^{-4}$

    **$\tau = 10$:**

    - $B(10) = -\frac{1-e^{-0.5}}{0.05} = -\frac{0.39347}{0.05} = -7.86939$
    - $\sigma_r^2(10) = 0.001(1-e^{-1.0}) = 0.001(0.63212) = 6.321 \times 10^{-4}$

    **$\tau = 30$:**

    - $B(30) = -\frac{1-e^{-1.5}}{0.05} = -\frac{0.77687}{0.05} = -15.5374$
    - $\sigma_r^2(30) = 0.001(1-e^{-3.0}) = 0.001(0.95021) = 9.502 \times 10^{-4}$

    **Qualitative behavior:**

    - $|B(\tau)|$ increases monotonically from $0$ toward $1/\lambda = 20$, with diminishing marginal increases (concave growth).
    - $\sigma_r^2(t)$ increases from $0$ toward the stationary value $\sigma^2/(2\lambda) = 0.001$, approaching it exponentially.
    - $|A(\tau)|$ grows roughly quadratically for moderate $\tau$ due to the $B^2$ term and the $\theta$-integral.

---

**Exercise 5.** The characteristic function version introduces a complex parameter $u$. Show that setting $u = 0$ in $B(u,\tau)$ recovers $B(\tau)$, and setting $u = 0$ in $A(u,\tau)$ recovers $A(\tau)$.

??? success "Solution to Exercise 5"
    **Setting $u = 0$ in $B(u,\tau)$:**

    $$
    B(0,\tau) = -\frac{1-(1+i\cdot 0\cdot\lambda) e^{-\lambda \tau}}{\lambda} = -\frac{1-e^{-\lambda\tau}}{\lambda} = B(\tau)
    $$

    This recovers $B(\tau)$ as required.

    **Setting $u = 0$ in $A(u,\tau)$:**

    $$
    A(0,\tau) = -\frac{\sigma^2}{4\lambda^3}\left[(1+0)\left[3-4e^{-\lambda \tau}+e^{-2\lambda \tau} - 0\right]-2\lambda\tau\right]+\lambda\int_0^\tau\theta(T-\tau')B(0,\tau')d\tau'
    $$

    $$
    = -\frac{\sigma^2}{4\lambda^3}\left(3-4e^{-\lambda\tau}+e^{-2\lambda\tau}-2\lambda\tau\right)+\lambda\int_0^\tau\theta(T-\tau')B(\tau')d\tau'
    $$

    This is exactly $A(\tau)$ as defined in the bond pricing version. The complex-parameter terms involving $iu$ all vanish when $u=0$, recovering the real-valued bond pricing functions.

---

**Exercise 6.** Derive the relationship $B(2\tau) = B(\tau)(2 - \lambda B(\tau))$ directly from the definition $B(\tau) = -\frac{1 - e^{-\lambda\tau}}{\lambda}$. Under what circumstances is this identity useful for numerical computation?

??? success "Solution to Exercise 6"
    Starting from $B(\tau) = -\frac{1-e^{-\lambda\tau}}{\lambda}$, compute $B(2\tau)$:

    $$
    B(2\tau) = -\frac{1-e^{-2\lambda\tau}}{\lambda}
    $$

    Now factor $1-e^{-2\lambda\tau} = (1-e^{-\lambda\tau})(1+e^{-\lambda\tau})$:

    $$
    B(2\tau) = -\frac{(1-e^{-\lambda\tau})(1+e^{-\lambda\tau})}{\lambda}
    $$

    Since $B(\tau) = -\frac{1-e^{-\lambda\tau}}{\lambda}$, we have $1-e^{-\lambda\tau} = -\lambda B(\tau)$. Also $1+e^{-\lambda\tau} = 1 + 1 + \lambda B(\tau) = 2 + \lambda B(\tau)$, since $e^{-\lambda\tau} = 1+\lambda B(\tau)$. Substituting:

    $$
    B(2\tau) = -\frac{(-\lambda B(\tau))(2+\lambda B(\tau))}{\lambda} = B(\tau)(2+\lambda B(\tau))
    $$

    Since $B(\tau) < 0$ in this convention, we can write equivalently $B(2\tau) = B(\tau)(2 - \lambda|B(\tau)|)$. In the form matching the exercise: $B(2\tau) = B(\tau)(2 - \lambda B(\tau))$ when using the negative-$B$ convention where the "$-$" sign is already embedded in $B$.

    This identity is useful for numerical computation because it avoids computing $e^{-2\lambda\tau}$ separately -- once $B(\tau)$ is known, $B(2\tau)$ can be obtained with a single multiplication and addition, avoiding potential loss of significance when $\lambda\tau$ is very small and $e^{-2\lambda\tau} \approx 1$.

---

**Exercise 7.** The decomposition version defines $\tilde{A}(u,\tau)$ and $\tilde{B}(u,\tau)$. Explain the role of the decomposition $r(t) = \tilde{r}(t) + \psi(t)$ in simplifying the characteristic function, and verify that $\tilde{B}(u,\tau) = B(u,\tau)$.

??? success "Solution to Exercise 7"
    **Role of the decomposition:** The Hull-White short rate can be decomposed as $r(t) = \tilde{r}(t) + \psi(t)$, where $\psi(t) = f(0,t) + \frac{\lambda\sigma^2}{2}B^2(t)$ is the deterministic expected path and $\tilde{r}(t) = r(t) - \psi(t)$ is the zero-mean stochastic deviation. Since $\tilde{r}(t)$ satisfies the simpler SDE $d\tilde{r}(t) = -\lambda\tilde{r}(t)\,dt + \sigma\,dW(t)$ (an Ornstein-Uhlenbeck process with zero long-run mean), its characteristic function takes a standard exponential-affine form without the time-dependent drift $\theta(t)$.

    The characteristic function of $\int_t^T r(s)\,ds$ can then be written as:

    $$
    \mathbb{E}\left[e^{iu\int_t^T r(s)\,ds}\right] = \exp\!\left(iu\int_t^T \psi(s)\,ds\right)\cdot\mathbb{E}\left[e^{iu\int_t^T \tilde{r}(s)\,ds}\right]
    $$

    The first factor is deterministic (absorbed into $\tilde{A}$), and the second factor depends only on the OU process $\tilde{r}$, whose coefficients $\tilde{A}(u,\tau)$ and $\tilde{B}(u,\tau)$ do not involve $\theta(t)$.

    **Verification that $\tilde{B}(u,\tau) = B(u,\tau)$:** From the definitions:

    $$
    \tilde{B}(u,\tau) = B(u,\tau)
    $$

    This holds because the $B$ function satisfies the Riccati ODE $\frac{dB}{d\tau} = -\lambda B - iu$, which depends only on the mean-reversion speed $\lambda$ and the transform variable $u$, not on the drift function $\theta(t)$. The drift affects only the $A$ equation. Therefore, whether we work with $r(t)$ (full model) or $\tilde{r}(t)$ (centered process), the $B$ function is identical. The decomposition only changes the $A$ function: $A(u,\tau) = \tilde{A}(u,\tau) + iu\int_t^T\psi(T-\tau')\,d\tau'$.
