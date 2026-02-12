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

    Since the Hull-White short rate dynamics is

    $$\begin{array}{lllll}
    \displaystyle
    dr=\lambda\left(\theta(t)-r\right) dt+\sigma dW^{\mathbb{Q}}(t)
    \end{array}$$

    the ZCB PDE becomes

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
