# Hull-White Zero Bond Pricing

## Hull-White ZB Dynamics

$$\begin{array}{lllll}
\displaystyle
\frac{dP(t,T)}{P(t,T)}
=
r(t)dt+\sigma_P(t,T)dW^{\mathbb{Q}}_t
\end{array}$$

where

$$\begin{array}{lllll}
\displaystyle
\sigma_P(t,T)
=
-\frac{\sigma}{\lambda}
\left(1-e^{-\lambda(T-t)}\right)
\end{array}$$

## Zero Bond Price

$$
\displaystyle
P(t,T)=A(t,T)e^{-B(t,T)r(t)}
$$

where

$$\begin{array}{lllll}
\displaystyle
A(t,T)
&=&\displaystyle
\frac{P^M(0,T)}{P^M(0,t)}
\text{exp}\left\{B(t,T)f^M(0,t)-\frac{\sigma^2}{4\lambda}B(t,T)^2\right\}
\\
\displaystyle
B(t,T)
&=&\displaystyle
\frac{1}{\lambda}\left[1-e^{-\lambda(T-t)}\right]
\end{array}$$

???+ note "Proof (Expectation)"

    $$
    \displaystyle
    \int_t^Tr(t')dt'\Big|{\cal F}(t)
    \sim{\cal N}\left(
        B(t,T)[r(t)-\alpha(t)]+\log\frac{P^M(0,t)}{P^M(0,T)}+\frac{1}{2}[V(0,T)-V(0,t)],
        V(t,T)
    \right)
    $$

    where

    $$\begin{array}{lllll}
    \displaystyle
    V(t,T)
    &=&\displaystyle
    \frac{\sigma^2}{\lambda^2}\left[T-t+\frac{2}{\lambda}e^{-\lambda(T-t)}-\frac{1}{2\lambda}e^{-2\lambda(T-t)}-\frac{3}{2\lambda}\right]
    \end{array}$$

???+ note "Proof (PDE)"

    Recall (see [HW SDE](../model_definition/hull_white_sde_and_mean_reversion.md)) the short rate dynamics $dr=\lambda(\theta(t)-r)dt+\sigma dW^{\mathbb{Q}}(t)$. The ZCB PDE becomes

    $$
    \displaystyle
    \frac{\partial P}{\partial t}
    +\lambda\left(\theta(t)-r\right)\frac{\partial P}{\partial r}+\frac{1}{2}\sigma^2\frac{\partial^2 P}{\partial r^2}=rP
    $$

    Substituting the affine ansatz $P(t,T)=e^{A(\tau)+B(\tau)r(t)}$ with $\tau=T-t$ leads to the Riccati ODEs for $A$ and $B$.

## Hull-White Model Recovers Market ZB Curve

The Hull-White model, by construction, exactly recovers the market zero-coupon bond curve $P^M(0,T)$:

```python
def main():
    hw = HullWhite(sigma=0.01, lambd=0.01, P=P_market)
    t, R, M = hw.generate_sample_paths(
        num_paths=20_000, num_steps=100, T=30, seed=42
    )

    # Monte Carlo ZCB prices
    P_MC = []
    for T_i in T_grid:
        idx = int(T_i / dt)
        P_mc = np.mean(1.0 / M[:, idx])
        P_MC.append(P_mc)

    # Compare with analytic formula
    r0 = compute_r0(P_market)
    P_analytic = [hw.compute_ZCB(0, T_i, r0) for T_i in T_grid]

    # Both should match P_market(T_i)
```

## Hull-White Yield Curve Simulation

The Hull-White model can simulate future yield curves by computing $P(t_i, T)$ for a range of maturities $T$ at each simulated time $t_i$:

```python
def main():
    hw = HullWhite(sigma=0.01, lambd=0.01, P=P_market)
    t, R, M = hw.generate_sample_paths(
        num_paths=7, num_steps=100, T=10, seed=42
    )

    # For each path, compute yield curve at T = 10
    for path_idx in range(7):
        r_T = R[path_idx, -1]
        yields = []
        for tau in tau_grid:
            P_val = hw.compute_ZCB(10, 10 + tau, r_T)
            y = -np.log(P_val) / tau
            yields.append(y)
        plt.plot(tau_grid, yields)
```

---

## Exercises

**Exercise 1.** Verify that the bond volatility $\sigma_P(t,T) = -\frac{\sigma}{\lambda}(1 - e^{-\lambda(T-t)})$ is negative for $T > t$. Explain the economic intuition: why does a bond price decrease when the short rate increases?

??? success "Solution to Exercise 1"
    The bond volatility is $\sigma_P(t,T) = -\frac{\sigma}{\lambda}(1 - e^{-\lambda(T-t)})$. For $T > t$, the time to maturity $\tau = T - t > 0$, so $e^{-\lambda\tau} \in (0,1)$, which gives $1 - e^{-\lambda\tau} > 0$. Since $\sigma > 0$ and $\lambda > 0$, the entire expression is negative:

    $$
    \sigma_P(t,T) = -\frac{\sigma}{\lambda}\underbrace{(1 - e^{-\lambda\tau})}_{> 0} < 0
    $$

    **Economic intuition:** When the short rate $r(t)$ increases, future discount factors $e^{-\int_t^T r(s)ds}$ decrease on average, reducing the present value of the bond's unit payoff at maturity. The negative bond volatility reflects this inverse relationship: a positive shock to the Brownian motion $dW^{\mathbb{Q}}$ raises the short rate (through $dr = \cdots + \sigma\,dW^{\mathbb{Q}}$), which decreases bond prices. This is the standard interest rate risk mechanism -- bond prices fall when rates rise.

---

**Exercise 2.** Show that in the limit $\lambda \to 0$, the function $B(t,T)$ reduces to $T - t$ and the bond price formula recovers the Ho-Lee model form. What happens to $A(t,T)$ in this limit?

??? success "Solution to Exercise 2"
    **Limit of $B(t,T)$:** Taylor expand the exponential for small $\lambda$:

    $$
    e^{-\lambda\tau} = 1 - \lambda\tau + \frac{(\lambda\tau)^2}{2} - \cdots
    $$

    Therefore:

    $$
    B(t,T) = \frac{1}{\lambda}[1 - e^{-\lambda\tau}] = \frac{1}{\lambda}\left[\lambda\tau - \frac{(\lambda\tau)^2}{2} + \cdots\right] = \tau - \frac{\lambda\tau^2}{2} + \cdots
    $$

    In the limit $\lambda \to 0$, we obtain $B(t,T) \to T - t$, which is the Ho-Lee duration function.

    **Limit of $A(t,T)$:** From the formula:

    $$
    A(t,T) = \frac{P^M(0,T)}{P^M(0,t)}\exp\left\{B(t,T)f^M(0,t) - \frac{\sigma^2}{4\lambda}B(t,T)^2(1 - e^{-2\lambda t})\right\}
    $$

    As $\lambda \to 0$, we have $B(t,T) \to \tau$ and $\frac{1 - e^{-2\lambda t}}{4\lambda} \to \frac{2t}{4} = \frac{t}{2}$. Therefore:

    $$
    \log A(t,T) \to \log\frac{P^M(0,T)}{P^M(0,t)} + \tau\,f^M(0,t) - \frac{\sigma^2}{2}\tau^2 t
    $$

    This is the Ho-Lee deterministic factor. The convexity correction becomes $-\frac{\sigma^2}{2}\tau^2 t$, which grows with $t$ and $\tau^2$ without the dampening provided by mean reversion.

---

**Exercise 3.** Consider a Hull-White model with $\sigma = 0.01$, $\lambda = 0.03$, and a flat forward curve $f^M(0,t) = 0.05$. Compute $P(0, 10)$ using the bond price formula and verify that it equals the market discount factor $e^{-0.05 \times 10}$.

??? success "Solution to Exercise 3"
    Given: $\sigma = 0.01$, $\lambda = 0.03$, $f^M(0,t) = 0.05$ (flat), and $r(0) = f^M(0,0) = 0.05$.

    **Step 1: Compute $B(0,10)$.**

    $$
    B(0,10) = \frac{1}{0.03}[1 - e^{-0.03 \times 10}] = \frac{1 - e^{-0.3}}{0.03} = \frac{1 - 0.7408}{0.03} = \frac{0.2592}{0.03} \approx 8.6394
    $$

    **Step 2: Compute $A(0,10)$.**

    With a flat forward curve, $P^M(0,T) = e^{-0.05T}$:

    $$
    \log A(0,10) = \log\frac{P^M(0,10)}{P^M(0,0)} + B(0,10) \cdot f^M(0,0) - \frac{\sigma^2}{4\lambda}B(0,10)^2(1 - e^{0})
    $$

    At $t = 0$: $P^M(0,0) = 1$, and $1 - e^{-2\lambda \cdot 0} = 0$, so the convexity term vanishes:

    $$
    \log A(0,10) = -0.5 + 8.6394 \times 0.05 = -0.5 + 0.43197 = -0.06803
    $$

    Wait -- let us be more careful. Since $t = 0$:

    $$
    \log A(0,10) = \log P^M(0,10) + B(0,10) \cdot r(0) - 0 = -0.5 + 0.43197
    $$

    **Step 3: Compute $P(0,10)$.**

    $$
    P(0,10) = A(0,10) \cdot e^{-B(0,10) \cdot r(0)} = e^{\log A(0,10) - B(0,10) \cdot r(0)}
    $$

    $$
    = e^{-0.5 + 0.43197 - 0.43197} = e^{-0.5} \approx 0.6065
    $$

    The market discount factor is $P^M(0,10) = e^{-0.05 \times 10} = e^{-0.5} \approx 0.6065$. They match exactly, confirming that the Hull-White model recovers the market discount curve at $t = 0$.

---

**Exercise 4.** Starting from the affine ansatz $P(t,T) = e^{A(\tau) + B(\tau)r(t)}$ with $\tau = T - t$, substitute into the PDE

$$
\frac{\partial P}{\partial t} + \lambda(\theta(t) - r)\frac{\partial P}{\partial r} + \frac{1}{2}\sigma^2 \frac{\partial^2 P}{\partial r^2} = rP
$$

and derive the Riccati ODE for $B(\tau)$.

??? success "Solution to Exercise 4"
    Starting from the affine ansatz $P(t,T) = e^{A(\tau) + B(\tau)r(t)}$ with $\tau = T - t$, compute the partial derivatives:

    $$
    \frac{\partial P}{\partial t} = \left(-A'(\tau) - B'(\tau)r\right)P, \quad \frac{\partial P}{\partial r} = B(\tau)P, \quad \frac{\partial^2 P}{\partial r^2} = B(\tau)^2 P
    $$

    Substituting into the PDE $\frac{\partial P}{\partial t} + \lambda(\theta(t) - r)\frac{\partial P}{\partial r} + \frac{1}{2}\sigma^2\frac{\partial^2 P}{\partial r^2} = rP$ and dividing by $P > 0$:

    $$
    -A'(\tau) - B'(\tau)r + \lambda(\theta(t) - r)B(\tau) + \frac{1}{2}\sigma^2 B(\tau)^2 = r
    $$

    Collecting terms proportional to $r$:

    $$
    \left[-B'(\tau) - \lambda B(\tau) - 1\right]r + \left[-A'(\tau) + \lambda\theta(t)B(\tau) + \frac{1}{2}\sigma^2 B(\tau)^2\right] = 0
    $$

    Since this must hold for all $r$, the coefficient of $r$ must vanish:

    $$
    B'(\tau) = -\lambda B(\tau) - 1, \qquad B(0) = 0
    $$

    This is the Riccati ODE for $B(\tau)$. It is a first-order linear ODE with constant coefficients. Using the integrating factor $e^{\lambda\tau}$:

    $$
    \frac{d}{d\tau}[e^{\lambda\tau}B(\tau)] = -e^{\lambda\tau}
    $$

    Integrating from $0$ to $\tau$ with $B(0) = 0$:

    $$
    B(\tau) = -\frac{1 - e^{-\lambda\tau}}{\lambda}
    $$

    In the positive-$B$ convention used in the bond price formula $P = A\,e^{-B\,r}$, we write $B(t,T) = \frac{1}{\lambda}(1 - e^{-\lambda\tau})$.

---

**Exercise 5.** Explain why the Hull-White model exactly recovers the market zero-coupon bond curve $P^M(0,T)$ for every maturity $T$. Which parameter in the model is responsible for this calibration, and how is it determined?

??? success "Solution to Exercise 5"
    The Hull-White model recovers $P^M(0,T)$ because the time-dependent drift function $\theta(t)$ is explicitly calibrated to the market term structure.

    **Which parameter:** The function $\theta(t)$ (the time-dependent mean reversion level) is responsible for exact calibration. Unlike the Vasicek model where the mean reversion target $b$ is a constant, Hull-White promotes $b$ to a deterministic function $\theta(t)$.

    **How it is determined:** Setting $P(0,T) = P^M(0,T)$ for all $T$ and using the bond price formula at $t = 0$:

    $$
    A(0,T)e^{-B(0,T)r(0)} = P^M(0,T)
    $$

    Since $A(0,T)$ depends on $\theta(\cdot)$ through the integral $\int_0^T \theta(u)B(u,T)du$, this equation implicitly defines $\theta(t)$. Differentiating twice with respect to $T$ and solving yields:

    $$
    \theta(t) = f^M(0,t) + \frac{1}{\lambda}\frac{\partial f^M(0,t)}{\partial t} + \frac{\sigma^2}{2\lambda^2}(1 - e^{-2\lambda t})
    $$

    This formula expresses $\theta(t)$ entirely in terms of market observables ($f^M(0,t)$ and its derivative) and model parameters ($\lambda$, $\sigma$). The function $\theta(t)$ acts as a free function that absorbs the entire initial term structure, ensuring perfect calibration at $t = 0$.

---

**Exercise 6.** In the Monte Carlo verification code, the expected value $\mathbb{E}^{\mathbb{Q}}[1/M(T)]$ is estimated by $\frac{1}{N}\sum_{i=1}^{N} 1/M_i(T)$. Show that this estimator is unbiased for $P(0,T)$ and discuss the sources of Monte Carlo error (discretization bias vs. sampling error).

??? success "Solution to Exercise 6"
    The estimator is $\hat{P}(0,T) = \frac{1}{N}\sum_{i=1}^N \frac{1}{M_i(T)}$ where $M_i(T) = e^{\int_0^T r^{(i)}(s)ds}$ is the money market account along path $i$.

    **Unbiasedness:** By the risk-neutral pricing formula:

    $$
    P(0,T) = \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_0^T r(s)ds}\right] = \mathbb{E}^{\mathbb{Q}}\left[\frac{1}{M(T)}\right]
    $$

    Since the paths $M_1(T), \ldots, M_N(T)$ are i.i.d. draws under $\mathbb{Q}$:

    $$
    \mathbb{E}^{\mathbb{Q}}[\hat{P}(0,T)] = \frac{1}{N}\sum_{i=1}^N \mathbb{E}^{\mathbb{Q}}\left[\frac{1}{M_i(T)}\right] = \mathbb{E}^{\mathbb{Q}}\left[\frac{1}{M(T)}\right] = P(0,T)
    $$

    So the estimator is unbiased.

    **Sources of error:**

    1. *Sampling error (statistical):* The finite sample mean $\frac{1}{N}\sum 1/M_i$ deviates from the true expectation with standard error $\text{std}(1/M)/\sqrt{N}$. This decreases as $\sqrt{N}$ and is the dominant error source for large $N$.

    2. *Discretization bias (systematic):* The short rate paths are simulated using discrete time steps (e.g., Euler scheme), so $\int_0^T r(s)ds$ is approximated by $\sum_k r(t_k)\Delta t$. This introduces a systematic bias that does not vanish with more paths $N$ but decreases with smaller time steps $\Delta t$. For the Hull-White model, the exact distribution of $r$ is known (Gaussian), so exact simulation is possible, eliminating discretization bias entirely.

---

**Exercise 7.** The yield curve simulation code computes future yield curves $R(T, T+\tau)$ for different short rate realizations $r(T)$. Prove that all simulated yield curves must pass through the same long-maturity asymptote as $\tau \to \infty$, regardless of $r(T)$.

??? success "Solution to Exercise 7"
    The yield at maturity $\tau$ from the simulated curve at time $T$ is:

    $$
    R(T, T+\tau) = -\frac{\log A(T, T+\tau)}{\tau} + \frac{B(T, T+\tau)}{\tau}r(T) = a(\tau, T) + b(\tau)\,r(T)
    $$

    where $b(\tau) = \frac{1 - e^{-\lambda\tau}}{\lambda\tau}$.

    As $\tau \to \infty$:

    $$
    b(\tau) = \frac{1 - e^{-\lambda\tau}}{\lambda\tau} \to \frac{1}{\lambda\tau} \to 0
    $$

    Therefore the $r(T)$-dependent term vanishes:

    $$
    \lim_{\tau \to \infty} R(T, T+\tau) = \lim_{\tau \to \infty} a(\tau, T)
    $$

    This limit is deterministic -- it depends only on the market curve $P^M(0,\cdot)$ and the model parameters $\lambda, \sigma$, but not on the realization $r(T)$. Explicitly:

    $$
    a(\tau, T) = -\frac{1}{\tau}\left[\log\frac{P^M(0,T+\tau)}{P^M(0,T)} + B(T,T+\tau)f^M(0,T) - \frac{\sigma^2}{4\lambda}B(T,T+\tau)^2(1-e^{-2\lambda T})\right]
    $$

    As $\tau \to \infty$, $B(T,T+\tau) \to 1/\lambda$ (bounded), so the $B^2$ correction term divided by $\tau$ vanishes, and the dominant term is $-\frac{1}{\tau}\log P^M(0,T+\tau)$, which converges to the asymptotic forward rate $\bar{f} = \lim_{T\to\infty} f^M(0,T)$.

    Hence all simulated yield curves share the same long-maturity asymptote $\bar{f}$, regardless of the realized short rate $r(T)$. This is a direct consequence of the single-factor structure and the boundedness of $B(t,T)$ under mean reversion.
