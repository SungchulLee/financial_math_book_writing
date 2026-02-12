# Two-Factor Hull-White Model

## Model Specification

The two-factor Hull-White model introduces a second stochastic factor to capture richer yield curve dynamics:

$$\begin{array}{lllll}
\displaystyle
r(t)=x(t)+y(t)+\varphi(t)
\end{array}$$

where

$$\begin{array}{lllll}
dx(t)&=&-\lambda_1 x(t)dt+\sigma_1 dW_1(t),\quad x(0)=0\\
dy(t)&=&-\lambda_2 y(t)dt+\sigma_2 dW_2(t),\quad y(0)=0\\
dW_1(t)dW_2(t)&=&\rho\, dt
\end{array}$$

and $\varphi(t)$ is a deterministic function chosen to fit the initial term structure:

$$
\varphi(t)=f(0,t)
+\frac{\sigma_1^2}{2\lambda_1^2}\left(1-e^{-\lambda_1 t}\right)^2
+\frac{\sigma_2^2}{2\lambda_2^2}\left(1-e^{-\lambda_2 t}\right)^2
+\frac{\rho\sigma_1\sigma_2}{\lambda_1\lambda_2}\left(1-e^{-\lambda_1 t}\right)\left(1-e^{-\lambda_2 t}\right)
$$

## Two-Factor ZCB Price

$$\begin{array}{lllll}
P(T_1,T_2)=\exp\left(A(T_1,T_2)+B_x(T_1,T_2)x(T_1)+B_y(T_1,T_2)y(T_1)\right)
\end{array}$$

where

$$\begin{array}{lllll}
B_x(T_1,T_2)&=&\displaystyle\frac{e^{-\lambda_1(T_2-T_1)}-1}{\lambda_1}\\
B_y(T_1,T_2)&=&\displaystyle\frac{e^{-\lambda_2(T_2-T_1)}-1}{\lambda_2}
\end{array}$$

and $A(T_1,T_2)$ is determined by no-arbitrage to fit the initial curve.

## Two-Factor Hull-White Recovers Market ZCB Curve and Yield Curve

```python
def main():
    hw2 = HullWhite2(
        sigma1=0.002, sigma2=0.002,
        lambd1=0.01, lambd2=0.1,
        rho=-0.2, P=P_market
    )

    num_paths = 20_000
    num_steps = 100
    T = 39

    t, X, Y, R, M = hw2.generate_sample_paths(num_paths, num_steps, T)

    # Monte Carlo ZCB prices
    P_MC = []
    for T_i in T_grid:
        idx = int(T_i / (T / num_steps))
        P_mc = np.mean(1.0 / M[:, idx])
        P_MC.append(P_mc)

    # Compare with market curve
    P_market_vals = [P_market(T_i) for T_i in T_grid]
```

## Two-Factor Hull-White Yield Curve Simulation

The two-factor model produces richer yield curve dynamics than the one-factor model, including twists and butterfly shifts:

```python
def main():
    hw1 = HullWhite(sigma=0.002, lambd=0.01, P=P_market)
    hw2 = HullWhite2(
        sigma1=0.002, sigma2=0.002,
        lambd1=0.01, lambd2=0.1,
        rho=-0.2, P=P_market
    )

    num_paths = 7
    num_steps = 100
    T = 10.0

    # Simulate short rates up to T = 10
    # Compute yield curve of 40 years spanning from T
    t1, R1, M1 = hw1.generate_sample_paths(num_paths, num_steps, T)
    t2, X2, Y2, R2, M2 = hw2.generate_sample_paths(num_paths, num_steps, T)

    # For each path, compute yield curve at T
    for path_idx in range(num_paths):
        # One-factor yield curves
        r1_T = R1[path_idx, -1]
        yields_1f = [-np.log(hw1.compute_ZCB(T, T+tau, r1_T))/tau
                     for tau in tau_grid]

        # Two-factor yield curves
        x_T = X2[path_idx, -1]
        y_T = Y2[path_idx, -1]
        yields_2f = [-np.log(hw2.compute_ZCB(T, T+tau, x_T, y_T))/tau
                     for tau in tau_grid]
```

The two-factor model generates more diverse yield curve shapes, particularly the ability to produce non-parallel shifts and changes in curvature that the one-factor model cannot capture.
