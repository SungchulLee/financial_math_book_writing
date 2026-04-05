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

---

## Exercises

**Exercise 1.** Verify that $\varphi(0) = f(0,0) = r_0$ by substituting $t = 0$ into the formula for $\varphi(t)$. Then show that $r(0) = x(0) + y(0) + \varphi(0) = r_0$ given $x(0) = y(0) = 0$.

??? success "Solution to Exercise 1"
    Substituting $t = 0$ into the formula for $\varphi(t)$:

    $$
    \varphi(0) = f(0,0) + \frac{\sigma_1^2}{2\lambda_1^2}(1 - e^0)^2 + \frac{\sigma_2^2}{2\lambda_2^2}(1 - e^0)^2 + \frac{\rho\sigma_1\sigma_2}{\lambda_1\lambda_2}(1 - e^0)(1 - e^0)
    $$

    Since $e^{-\lambda_i \cdot 0} = e^0 = 1$, every correction term contains $(1 - 1)^2 = 0$ or $(1-1)(1-1) = 0$. Therefore:

    $$
    \varphi(0) = f(0,0) + 0 + 0 + 0 = f(0,0) = r_0
    $$

    where $f(0,0)$ is the instantaneous forward rate at time 0, which equals the initial short rate $r_0$.

    For the short rate at time 0:

    $$
    r(0) = x(0) + y(0) + \varphi(0) = 0 + 0 + r_0 = r_0
    $$

    confirming consistency with the initial condition.

---

**Exercise 2.** For parameters $\lambda_1 = 0.01$, $\lambda_2 = 0.1$, $\sigma_1 = 0.002$, $\sigma_2 = 0.002$, and $\rho = -0.2$ with a flat market forward rate $f(0,t) = 0.03$, compute $\varphi(t)$ at $t = 1, 5, 10$ years. Describe how each of the three correction terms in $\varphi(t)$ contributes to the total.

??? success "Solution to Exercise 2"
    With $f(0,t) = 0.03$ (flat) and the given parameters, we compute $\varphi(t)$ at $t = 1, 5, 10$.

    The three correction terms are:

    - Term 1: $C_1(t) = \frac{\sigma_1^2}{2\lambda_1^2}(1 - e^{-\lambda_1 t})^2 = \frac{(0.002)^2}{2(0.01)^2}(1 - e^{-0.01t})^2 = 0.02(1 - e^{-0.01t})^2$
    - Term 2: $C_2(t) = \frac{\sigma_2^2}{2\lambda_2^2}(1 - e^{-\lambda_2 t})^2 = \frac{(0.002)^2}{2(0.1)^2}(1 - e^{-0.1t})^2 = 0.0002(1 - e^{-0.1t})^2$
    - Term 3: $C_3(t) = \frac{\rho\sigma_1\sigma_2}{\lambda_1\lambda_2}(1 - e^{-\lambda_1 t})(1 - e^{-\lambda_2 t}) = \frac{-0.2 \times 0.002 \times 0.002}{0.01 \times 0.1}(1 - e^{-0.01t})(1 - e^{-0.1t})$

    $C_3(t) = \frac{-0.0000008}{0.001}(1 - e^{-0.01t})(1 - e^{-0.1t}) = -0.0008(1 - e^{-0.01t})(1 - e^{-0.1t})$

    **At $t = 1$:**

    - $C_1(1) = 0.02(1 - 0.99005)^2 = 0.02(0.00995)^2 \approx 0.00000198$
    - $C_2(1) = 0.0002(1 - 0.90484)^2 = 0.0002(0.09516)^2 \approx 0.00000181$
    - $C_3(1) = -0.0008(0.00995)(0.09516) \approx -0.00000076$
    - $\varphi(1) \approx 0.03 + 0.00000198 + 0.00000181 - 0.00000076 \approx 0.03000303$

    **At $t = 5$:**

    - $C_1(5) = 0.02(1 - 0.95123)^2 = 0.02(0.04877)^2 \approx 0.0000476$
    - $C_2(5) = 0.0002(1 - 0.60653)^2 = 0.0002(0.39347)^2 \approx 0.0000310$
    - $C_3(5) = -0.0008(0.04877)(0.39347) \approx -0.0000154$
    - $\varphi(5) \approx 0.03 + 0.0000476 + 0.0000310 - 0.0000154 \approx 0.03006$

    **At $t = 10$:**

    - $C_1(10) = 0.02(1 - 0.90484)^2 = 0.02(0.09516)^2 \approx 0.000181$
    - $C_2(10) = 0.0002(1 - 0.36788)^2 = 0.0002(0.63212)^2 \approx 0.0000799$
    - $C_3(10) = -0.0008(0.09516)(0.63212) \approx -0.0000481$
    - $\varphi(10) \approx 0.03 + 0.000181 + 0.0000799 - 0.0000481 \approx 0.03021$

    The first correction term ($C_1$) dominates because it involves the smaller mean-reversion speed $\lambda_1 = 0.01$, giving a larger denominator $2\lambda_1^2$. The cross-correlation term ($C_3$) is negative due to $\rho = -0.2$, partially offsetting the positive corrections.

---

**Exercise 3.** Show that the two-factor model reduces to the one-factor Hull-White model when $\sigma_2 = 0$. Identify $\varphi(t)$ with the one-factor $\alpha(t)$ and verify that the bond price formula becomes the one-factor formula.

??? success "Solution to Exercise 3"
    Setting $\sigma_2 = 0$, the second factor equation becomes $dy(t) = -\lambda_2 y(t)\,dt$ with $y(0) = 0$, which gives $y(t) = 0$ for all $t$.

    The short rate reduces to $r(t) = x(t) + \varphi(t)$, where with $\sigma_2 = 0$:

    $$
    \varphi(t) = f(0,t) + \frac{\sigma_1^2}{2\lambda_1^2}(1 - e^{-\lambda_1 t})^2
    $$

    This is exactly the one-factor Hull-White $\alpha(t)$ function.

    The factor $x(t)$ satisfies $dx(t) = -\lambda_1 x(t)\,dt + \sigma_1\,dW_1(t)$, which is the one-factor Hull-White dynamics for the centered variable $x(t) = r(t) - \alpha(t)$.

    For the bond price, with $\sigma_2 = 0$ and $y(t) = 0$:

    $$
    P(T_1, T_2) = \exp(A(T_1, T_2) + B_x(T_1, T_2)\,x(T_1) + B_y(T_1, T_2) \cdot 0) = \exp(A(T_1, T_2) + B_x(T_1, T_2)\,x(T_1))
    $$

    The $B_y$ term drops out, and $A^{(2)}(T_1, T_2)$ simplifies: all terms involving $\sigma_2$ or $\rho$ vanish from the integrated variance function $V(t, T)$, leaving only the one-factor variance. This matches the one-factor bond price formula $P = \exp(A + Bx)$ with $B = B_x = (e^{-\lambda_1\tau} - 1)/\lambda_1$.

---

**Exercise 4.** The two-factor ZCB price $P(T_1, T_2) = \exp(A + B_x x + B_y y)$ has two factor loadings $B_x$ and $B_y$ with the same functional form but different mean-reversion speeds. Compute $B_x(0, 10)$ and $B_y(0, 10)$ for the parameters in Exercise 2. Which factor has a larger loading, and why?

??? success "Solution to Exercise 4"
    With $\lambda_1 = 0.01$, $\lambda_2 = 0.1$:

    $$
    B_x(0, 10) = \frac{e^{-0.01 \times 10} - 1}{0.01} = \frac{e^{-0.1} - 1}{0.01} = \frac{0.90484 - 1}{0.01} = -9.516
    $$

    $$
    B_y(0, 10) = \frac{e^{-0.1 \times 10} - 1}{0.1} = \frac{e^{-1} - 1}{0.1} = \frac{0.36788 - 1}{0.1} = -6.321
    $$

    The first factor has a larger loading in magnitude: $|B_x(0, 10)| = 9.516 > |B_y(0, 10)| = 6.321$.

    This is because $\lambda_1 < \lambda_2$: the slower-reverting factor $x$ has a larger impact on long-term bond prices. Intuitively, a permanent shift in $x$ has a more lasting effect on future short rates than the same shift in $y$, because $y$ mean-reverts faster and its effect decays more quickly. Over a 10-year horizon, the fast-reverting factor $y$ (with $\lambda_2 = 0.1$, half-life $\approx 6.9$ years) decays substantially, while the slow factor $x$ (with $\lambda_1 = 0.01$, half-life $\approx 69$ years) barely decays.

    In the limit $\tau \to \infty$: $|B_x| \to 1/\lambda_1 = 100$ and $|B_y| \to 1/\lambda_2 = 10$, so the slow factor dominates long-maturity bond prices by a factor of 10.

---

**Exercise 5.** Explain why the two-factor model can produce non-parallel yield curve shifts while the one-factor model cannot. Illustrate with two specific scenarios: (i) $x$ increases while $y$ stays constant, and (ii) $x$ increases while $y$ decreases.

??? success "Solution to Exercise 5"
    In the one-factor model, the yield at maturity $T$ is a function of a single state variable $r(t)$:

    $$
    y(t, T) = -\frac{\log P(t, T)}{T - t} = -\frac{A(t, T) + B(t, T)(r(t) - \alpha(t))}{T - t} + \text{const}
    $$

    A change in $r(t)$ shifts yields at all maturities in the same direction (since $B(t, T) < 0$ for all $T > t$). The shift magnitudes differ, but the direction is always the same. This means all yield curve movements are parallel-like (same direction, different magnitudes).

    In the two-factor model, the yield depends on two state variables $x(t)$ and $y(t)$:

    $$
    y(t, T) = -\frac{A^{(2)}(t, T) + B_x(t, T)\,x(t) + B_y(t, T)\,y(t)}{T - t}
    $$

    **(i) $x$ increases, $y$ stays constant:** All yields increase (since both $B_x < 0$), with long-maturity yields increasing more (larger $|B_x|$). This produces a roughly parallel shift plus a steepening.

    **(ii) $x$ increases, $y$ decreases:** Short-maturity yields are more sensitive to $y$ (relative to long-maturity yields), because $|B_y(t, T)|$ is relatively larger compared to $|B_x(t, T)|$ for short maturities. An increase in $x$ pushes all yields up, but the decrease in $y$ pushes yields down, especially at shorter maturities where $|B_y|/|B_x|$ is larger. The net effect can be: long yields rise (dominated by $x$ increase) while short yields fall or remain flat (the $y$ decrease partially or fully offsets the $x$ increase). This produces a twist or butterfly movement that the one-factor model cannot generate.

---

**Exercise 6.** The parameter $\rho$ controls the correlation between the driving Brownian motions. Explain the economic interpretation of $\rho < 0$ in terms of yield curve movements. What yield curve shapes are easier to generate with $\rho < 0$ versus $\rho > 0$?

??? success "Solution to Exercise 6"
    When $\rho < 0$ and $\lambda_2 \gg \lambda_1$:

    - Factor $y$ (fast-reverting, large $\lambda_2$) primarily affects the short end of the yield curve.
    - Factor $x$ (slow-reverting, small $\lambda_1$) primarily affects the long end.
    - $\rho < 0$ means positive shocks to $W_1$ (driving $x$ up) tend to coincide with negative shocks to $W_2$ (driving $y$ down), and vice versa.

    When $y$ receives a positive shock (short-end yields rise), $x$ tends to receive a negative shock (long-end yields fall). This creates a **twist** movement: the short and long ends of the yield curve move in opposite directions.

    With $\rho < 0$, the model more easily generates:

    - **Yield curve inversions**: short rates rise while long rates fall
    - **Steepening/flattening**: differential movements across the curve
    - **Butterfly movements**: middle of the curve moves differently from the wings

    With $\rho > 0$, both factors tend to move together, so yield curve movements are more parallel-like. The curve shapes that $\rho > 0$ produces most naturally are **parallel shifts** and **level changes** where all rates move in the same direction. The decorrelation benefit of the second factor is reduced when $\rho > 0$.

---

**Exercise 7.** When $\lambda_1 = \lambda_2$, the two factors have the same mean-reversion speed. Show that the model reduces to an effective one-factor model with volatility $\sigma_{\text{eff}} = \sqrt{\sigma_1^2 + \sigma_2^2 + 2\rho\sigma_1\sigma_2}$. Why does the second factor add no new information in this case?

??? success "Solution to Exercise 7"
    When $\lambda_1 = \lambda_2 = \lambda$, define $z(t) = x(t) + y(t)$. Then:

    $$
    dz(t) = dx(t) + dy(t) = -\lambda x(t)\,dt + \sigma_1\,dW_1(t) - \lambda y(t)\,dt + \sigma_2\,dW_2(t)
    $$

    $$
    = -\lambda(x(t) + y(t))\,dt + \sigma_1\,dW_1(t) + \sigma_2\,dW_2(t) = -\lambda z(t)\,dt + \sigma_1\,dW_1(t) + \sigma_2\,dW_2(t)
    $$

    The process $\sigma_1 W_1(t) + \sigma_2 W_2(t)$ is a Gaussian process with variance:

    $$
    \text{Var}(\sigma_1 W_1(t) + \sigma_2 W_2(t)) = \sigma_1^2 t + \sigma_2^2 t + 2\rho\sigma_1\sigma_2 t = (\sigma_1^2 + \sigma_2^2 + 2\rho\sigma_1\sigma_2)t
    $$

    By Levy's characterization, $\tilde{W}(t) = (\sigma_1 W_1(t) + \sigma_2 W_2(t))/\sigma_{\text{eff}}$ is a standard Brownian motion, where $\sigma_{\text{eff}} = \sqrt{\sigma_1^2 + \sigma_2^2 + 2\rho\sigma_1\sigma_2}$. Therefore:

    $$
    dz(t) = -\lambda z(t)\,dt + \sigma_{\text{eff}}\,d\tilde{W}(t)
    $$

    This is a single OU process. Since $r(t) = z(t) + \varphi(t)$, the model is effectively one-factor.

    The second factor adds no new information because when $\lambda_1 = \lambda_2$, the factor loadings in the bond price formula satisfy $B_x(\tau) = B_y(\tau)$ for all $\tau$. Therefore $P(t, T) = \exp(A + B(\tau)(x + y)) = \exp(A + B(\tau)z)$, which depends on a single state variable $z = x + y$. All bond prices are functions of one variable, exactly as in the one-factor model. For the second factor to add genuinely new information, the two mean-reversion speeds must be distinct ($\lambda_1 \neq \lambda_2$), giving different decay profiles for the two factor loadings.
