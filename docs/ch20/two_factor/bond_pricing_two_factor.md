# Bond Pricing Under Two-Factor Model

The two-factor Hull-White model preserves the exponential-affine bond price structure of the one-factor model, but with two state variables instead of one. The bond price $P(t, T)$ depends on both factors $x_t$ and $y_t$, and the named functions $B_x$, $B_y$, and $A^{(2)}$ generalize their one-factor counterparts. This section derives the two-factor bond price formula, presents the extended named functions, and verifies consistency with the initial yield curve.

## Two-Factor Bond Price Formula

The zero-coupon bond price in the two-factor Hull-White model is

$$
P(t, T) = \exp\!\bigl(A^{(2)}(t, T) + B_x(t, T)\,x_t + B_y(t, T)\,y_t\bigr)
$$

where the factor loadings are

$$
B_x(t, T) = \frac{e^{-\lambda_1(T-t)} - 1}{\lambda_1}, \qquad B_y(t, T) = \frac{e^{-\lambda_2(T-t)} - 1}{\lambda_2}
$$

and $A^{(2)}(t, T)$ is determined by the no-arbitrage condition.

The factor loadings have the same functional form as the one-factor $B(t,T)$, with each factor contributing through its own mean-reversion speed. Both $B_x$ and $B_y$ are negative (since $e^{-\lambda\tau} < 1$ for $\tau > 0$), so higher values of $x_t$ or $y_t$ reduce the bond price, as expected.

## Derivation via the PDE Approach

The bond pricing PDE for the two-factor model is

$$
\frac{\partial P}{\partial t} - \lambda_1 x\frac{\partial P}{\partial x} - \lambda_2 y\frac{\partial P}{\partial y} + \frac{1}{2}\sigma_1^2\frac{\partial^2 P}{\partial x^2} + \rho\sigma_1\sigma_2\frac{\partial^2 P}{\partial x\,\partial y} + \frac{1}{2}\sigma_2^2\frac{\partial^2 P}{\partial y^2} = (x + y + \varphi(t))\,P
$$

with terminal condition $P(T, T) = 1$.

Substituting the affine ansatz $P = \exp(A + B_x\,x + B_y\,y)$ and collecting terms yields the ODE system (with $\tau = T - t$):

$$
\frac{dB_x}{d\tau} = 1 - \lambda_1 B_x, \quad B_x(0) = 0
$$

$$
\frac{dB_y}{d\tau} = 1 - \lambda_2 B_y, \quad B_y(0) = 0
$$

$$
\frac{dA}{d\tau} = -\varphi(T-\tau) + \frac{1}{2}\sigma_1^2 B_x^2 + \rho\sigma_1\sigma_2 B_x B_y + \frac{1}{2}\sigma_2^2 B_y^2, \quad A(0) = 0
$$

???+ note "Proof"
    The factor loading ODEs $dB_x/d\tau = 1 - \lambda_1 B_x$ with $B_x(0) = 0$ have the solution $B_x(\tau) = (1 - e^{-\lambda_1\tau})/\lambda_1$, which gives $B_x(t,T) = (e^{-\lambda_1(T-t)} - 1)/\lambda_1$ after substituting $\tau = T - t$ (note the sign convention). The $A$ equation integrates to give $A$ as a function of $\tau$, with the deterministic drift $\varphi$ and the volatility terms entering through $B_x$ and $B_y$. $\square$

## The Function A(t, T)

Integrating the ODE for $A$ and expressing in terms of market observables:

$$
A^{(2)}(t, T) = \ln\frac{P^M(0, T)}{P^M(0, t)} + \frac{1}{2}\left[V(t, T) + V(0, t) - V(0, T)\right]
$$

where the integrated variance function is

$$
V(t, T) = \frac{\sigma_1^2}{\lambda_1^2}\left[\tau + \frac{2}{\lambda_1}e^{-\lambda_1\tau} - \frac{1}{2\lambda_1}e^{-2\lambda_1\tau} - \frac{3}{2\lambda_1}\right] + \frac{\sigma_2^2}{\lambda_2^2}\left[\tau + \frac{2}{\lambda_2}e^{-\lambda_2\tau} - \frac{1}{2\lambda_2}e^{-2\lambda_2\tau} - \frac{3}{2\lambda_2}\right] + \frac{2\rho\sigma_1\sigma_2}{\lambda_1\lambda_2}\left[\tau + \frac{e^{-\lambda_1\tau} - 1}{\lambda_1} + \frac{e^{-\lambda_2\tau} - 1}{\lambda_2} - \frac{e^{-(\lambda_1+\lambda_2)\tau} - 1}{\lambda_1+\lambda_2}\right]
$$

with $\tau = T - t$.

!!! tip "Structure of V(t,T)"
    The variance function $V(t,T)$ has three components: two one-factor variance terms (proportional to $\sigma_1^2$ and $\sigma_2^2$) and a cross-correlation term (proportional to $\rho\sigma_1\sigma_2$). Setting $\sigma_2 = 0$ recovers the one-factor variance.

## Extended Named Functions

The two-factor model extends the named function apparatus:

**Factor loadings.**

$$
B_x(\tau) = \frac{e^{-\lambda_1\tau} - 1}{\lambda_1}, \qquad B_y(\tau) = \frac{e^{-\lambda_2\tau} - 1}{\lambda_2}
$$

**Deterministic drift.**

$$
\varphi(t) = f^M(0, t) + \frac{\sigma_1^2}{2\lambda_1^2}\left(1 - e^{-\lambda_1 t}\right)^2 + \frac{\sigma_2^2}{2\lambda_2^2}\left(1 - e^{-\lambda_2 t}\right)^2 + \frac{\rho\sigma_1\sigma_2}{\lambda_1\lambda_2}\left(1 - e^{-\lambda_1 t}\right)\left(1 - e^{-\lambda_2 t}\right)
$$

**Short rate variance.**

$$
\sigma_r^2(t) = \frac{\sigma_1^2}{2\lambda_1}\left(1 - e^{-2\lambda_1 t}\right) + \frac{\sigma_2^2}{2\lambda_2}\left(1 - e^{-2\lambda_2 t}\right) + \frac{2\rho\sigma_1\sigma_2}{\lambda_1 + \lambda_2}\left(1 - e^{-(\lambda_1+\lambda_2)t}\right)
$$

## Consistency with Initial Yield Curve

At $t = 0$, with $x_0 = y_0 = 0$:

$$
P(0, T) = \exp\!\bigl(A^{(2)}(0, T)\bigr) = \exp\!\left(\ln P^M(0, T) + \frac{1}{2}[V(0,T) + V(0,0) - V(0,T)]\right) = P^M(0, T)
$$

since $V(0, 0) = 0$. The model exactly recovers the initial market curve by construction.

## Bond Price Volatility

The dynamics of the zero-coupon bond price under $\mathbb{Q}$ are

$$
\frac{dP(t,T)}{P(t,T)} = r_t\,dt + \sigma_1 B_x(t,T)\,dW_t^{(1)} + \sigma_2 B_y(t,T)\,dW_t^{(2)}
$$

The total bond price volatility is

$$
\sigma_P^{(2)}(t,T) = \sqrt{\sigma_1^2 B_x^2(t,T) + \sigma_2^2 B_y^2(t,T) + 2\rho\sigma_1\sigma_2 B_x(t,T)B_y(t,T)}
$$

For long maturities, $B_x \to -1/\lambda_1$ and $B_y \to -1/\lambda_2$, so the bond volatility saturates. The saturation levels differ for the two factors, creating a richer term structure of volatility compared to the one-factor model.

## Limiting Cases

**One-factor limit** ($\sigma_2 \to 0$): $B_y$ becomes irrelevant, $A^{(2)} \to A$ (one-factor), and the bond price reduces to the one-factor formula $P(t,T) = \exp(A(t,T) + B_x(t,T)\,x_t)$ with $x_t = r_t - \varphi(t)$.

**Uncorrelated factors** ($\rho = 0$): the cross terms vanish from $V(t,T)$, $\varphi(t)$, and $\sigma_r^2(t)$, simplifying all formulas. The two factors contribute independently.

**Equal mean-reversion** ($\lambda_1 = \lambda_2 = \lambda$): the two factors become indistinguishable in their time-decay structure, and the model reduces to a one-factor model with effective volatility $\sigma_{\text{eff}} = \sqrt{\sigma_1^2 + \sigma_2^2 + 2\rho\sigma_1\sigma_2}$. The second factor adds no new information in this limit.

???+ example "Two-Factor Bond Price Computation"
    ```python
    def main():
        hw2 = HullWhite2(
            sigma1=0.002, sigma2=0.002,
            lambd1=0.01, lambd2=0.1,
            rho=-0.2, P=P_market
        )

        # At t=5, with simulated factor values
        x_5 = 0.003
        y_5 = -0.001

        # Compute bond prices for various maturities
        for T in [6, 7, 10, 15, 20, 30]:
            P_val = hw2.compute_ZCB(5, T, x_5, y_5)
            y_val = -np.log(P_val) / (T - 5)
            print(f"P(5,{T:2d}) = {P_val:.6f}, yield = {y_val:.4f}")
    ```

## Summary

The two-factor Hull-White bond price $P(t,T) = \exp(A^{(2)}(t,T) + B_x(t,T)x_t + B_y(t,T)y_t)$ preserves the exponential-affine structure with two factor loadings $B_x = (e^{-\lambda_1\tau}-1)/\lambda_1$ and $B_y = (e^{-\lambda_2\tau}-1)/\lambda_2$. The function $A^{(2)}$ involves an integrated variance $V(t,T)$ with three components: two one-factor terms and a cross-correlation term proportional to $\rho\sigma_1\sigma_2$. The model exactly fits the initial yield curve by construction. The bond price volatility has contributions from both factors, producing a richer volatility term structure than the one-factor model. The extended named functions generalize the one-factor apparatus with cross-terms capturing the factor interaction.

---

## Exercises

**Exercise 1.** Verify that the factor loading ODEs $dB_x/d\tau = 1 - \lambda_1 B_x$ with $B_x(0) = 0$ have the solution $B_x(\tau) = (1 - e^{-\lambda_1\tau})/\lambda_1$. Show that $B_x(\tau) \to 1/\lambda_1$ as $\tau \to \infty$ and $B_x(\tau) \approx \tau$ for small $\tau$. Repeat for $B_y(\tau)$.

??? success "Solution to Exercise 1"
    The ODE is $dB_x/d\tau = 1 - \lambda_1 B_x$ with $B_x(0) = 0$. This is a first-order linear ODE. The integrating factor is $e^{\lambda_1\tau}$:

    $$
    \frac{d}{d\tau}\!\left(e^{\lambda_1\tau}B_x\right) = e^{\lambda_1\tau}
    $$

    Integrating from $0$ to $\tau$:

    $$
    e^{\lambda_1\tau}B_x(\tau) - B_x(0) = \frac{e^{\lambda_1\tau} - 1}{\lambda_1}
    $$

    Since $B_x(0) = 0$:

    $$
    B_x(\tau) = \frac{1 - e^{-\lambda_1\tau}}{\lambda_1}
    $$

    Note that $B_x(t, T) = (e^{-\lambda_1(T-t)} - 1)/\lambda_1 = -(1 - e^{-\lambda_1\tau})/\lambda_1$, which differs by a sign from $B_x(\tau)$ due to the convention $B_x(t,T) = -B_x(\tau)$ where $\tau = T - t$.

    **Limiting behavior as $\tau \to \infty$:** $e^{-\lambda_1\tau} \to 0$, so $B_x(\tau) \to 1/\lambda_1$.

    **Small $\tau$ approximation:** Using $e^{-\lambda_1\tau} \approx 1 - \lambda_1\tau + \frac{1}{2}\lambda_1^2\tau^2 - \cdots$:

    $$
    B_x(\tau) = \frac{1 - (1 - \lambda_1\tau + O(\lambda_1^2\tau^2))}{\lambda_1} = \tau - \frac{\lambda_1\tau^2}{2} + \cdots \approx \tau
    $$

    The same analysis applies to $B_y(\tau) = (1 - e^{-\lambda_2\tau})/\lambda_2$ with $\lambda_2$ replacing $\lambda_1$: $B_y(\tau) \to 1/\lambda_2$ as $\tau \to \infty$ and $B_y(\tau) \approx \tau$ for small $\tau$.

---

**Exercise 2.** Using $\lambda_1 = 0.01$, $\lambda_2 = 0.1$, $\sigma_1 = 0.005$, $\sigma_2 = 0.008$, $\rho = -0.3$, and a flat market curve at 3\%, compute the two-factor bond price $P(5, 10)$ for factor values $x_5 = 0.002$ and $y_5 = -0.001$. Compare with the initial market discount factor $P^M(0, 10)/P^M(0, 5)$, which is the time-5 bond price under the one-factor model with $x_5 = y_5 = 0$.

??? success "Solution to Exercise 2"
    With a flat market curve at 3%, $P^M(0, T) = e^{-0.03T}$, so $P^M(0, 10) = e^{-0.3} \approx 0.7408$ and $P^M(0, 5) = e^{-0.15} \approx 0.8607$.

    The factor loadings at $t = 5$, $T = 10$ (so $\tau = 5$):

    $$
    B_x(5, 10) = \frac{e^{-0.01 \times 5} - 1}{0.01} = \frac{0.9512 - 1}{0.01} = -4.877
    $$

    $$
    B_y(5, 10) = \frac{e^{-0.1 \times 5} - 1}{0.1} = \frac{0.6065 - 1}{0.1} = -3.935
    $$

    For $A^{(2)}(5, 10)$, using the formula:

    $$
    A^{(2)}(5, 10) = \ln\frac{P^M(0, 10)}{P^M(0, 5)} + \frac{1}{2}[V(5, 10) + V(0, 5) - V(0, 10)]
    $$

    $$
    \ln\frac{P^M(0, 10)}{P^M(0, 5)} = \ln e^{-0.3+0.15} = -0.15
    $$

    The $V$ terms involve lengthy expressions, but they represent small convexity corrections. For this exercise, the dominant term is $-0.15$, and the convexity adjustment is of order $O(\sigma^2/\lambda^2) \approx O(10^{-4})$.

    The bond price is:

    $$
    P(5, 10) = \exp(A^{(2)}(5, 10) + B_x(5, 10) \cdot 0.002 + B_y(5, 10) \cdot (-0.001))
    $$

    $$
    \approx \exp(-0.15 + \text{small correction} + (-4.877)(0.002) + (-3.935)(-0.001))
    $$

    $$
    \approx \exp(-0.15 - 0.009754 + 0.003935 + \text{small correction})
    $$

    $$
    \approx \exp(-0.1558) \approx 0.8558
    $$

    The initial market forward discount factor is $P^M(0, 10)/P^M(0, 5) = e^{-0.15} \approx 0.8607$. The two-factor bond price ($\approx 0.856$) is slightly lower because $x_5 = 0.002 > 0$ pushes rates up (lowering bond prices) more than $y_5 = -0.001 < 0$ pushes rates down.

---

**Exercise 3.** Show that the consistency condition $P(0, T) = P^M(0, T)$ holds by substituting $x_0 = y_0 = 0$ into the two-factor formula and using $V(0, 0) = 0$. Why is this condition essential for an arbitrage-free term structure model?

??? success "Solution to Exercise 3"
    At $t = 0$ with $x_0 = y_0 = 0$:

    $$
    P(0, T) = \exp(A^{(2)}(0, T) + B_x(0, T) \cdot 0 + B_y(0, T) \cdot 0) = \exp(A^{(2)}(0, T))
    $$

    Using the formula for $A^{(2)}$:

    $$
    A^{(2)}(0, T) = \ln\frac{P^M(0, T)}{P^M(0, 0)} + \frac{1}{2}[V(0, T) + V(0, 0) - V(0, T)]
    $$

    Since $P^M(0, 0) = 1$, we have $\ln(P^M(0, T)/P^M(0, 0)) = \ln P^M(0, T)$.

    Also, $V(0, 0)$ has $\tau = 0$, and substituting $\tau = 0$ into the $V$ formula: every term contains factors like $(e^{0} - 1) = 0$ or $\tau = 0$, giving $V(0, 0) = 0$.

    Therefore:

    $$
    A^{(2)}(0, T) = \ln P^M(0, T) + \frac{1}{2}[V(0, T) + 0 - V(0, T)] = \ln P^M(0, T)
    $$

    So $P(0, T) = \exp(\ln P^M(0, T)) = P^M(0, T)$.

    This condition is essential because an arbitrage-free term structure model must be consistent with observed market prices at $t = 0$. If $P(0, T) \neq P^M(0, T)$, one could immediately construct an arbitrage by trading the model-implied bond against the market-priced bond. The function $\varphi(t)$ (or equivalently $A^{(2)}$) is the mechanism by which the model absorbs the initial curve, ensuring no-arbitrage at inception.

---

**Exercise 4.** Compute the total bond price volatility $\sigma_P^{(2)}(t, T)$ for $t = 0$, $T = 5, 10, 20, 30$ using the parameters in Exercise 2. Plot $\sigma_P^{(2)}(0, T)$ as a function of $T$ and compare with the one-factor volatility $\sigma_P^{(1)}(0, T) = |\sigma_1 B_x(0, T)|$. At what maturity does the difference become most pronounced?

??? success "Solution to Exercise 4"
    The total bond price volatility is:

    $$
    \sigma_P^{(2)}(0, T) = \sqrt{\sigma_1^2 B_x^2(0, T) + \sigma_2^2 B_y^2(0, T) + 2\rho\sigma_1\sigma_2 B_x(0, T)B_y(0, T)}
    $$

    With $\sigma_1 = 0.005$, $\sigma_2 = 0.008$, $\lambda_1 = 0.01$, $\lambda_2 = 0.1$, $\rho = -0.3$:

    **$T = 5$** ($\tau = 5$): $B_x = (e^{-0.05}-1)/0.01 = -4.877$, $B_y = (e^{-0.5}-1)/0.1 = -3.935$

    $$
    \sigma_P^{(2)} = \sqrt{(0.005)^2(4.877)^2 + (0.008)^2(3.935)^2 + 2(-0.3)(0.005)(0.008)(4.877)(3.935)}
    $$

    $$
    = \sqrt{0.000595 + 0.000991 - 0.000461} = \sqrt{0.001125} \approx 0.0335
    $$

    One-factor: $\sigma_P^{(1)} = |0.005 \times (-4.877)| = 0.0244$

    **$T = 10$**: $B_x = -9.516$, $B_y = (e^{-1}-1)/0.1 = -6.321$

    $$
    \sigma_P^{(2)} = \sqrt{(0.005)^2(9.516)^2 + (0.008)^2(6.321)^2 + 2(-0.3)(0.00004)(9.516)(6.321)}
    $$

    $$
    = \sqrt{0.002264 + 0.002558 - 0.001441} = \sqrt{0.003381} \approx 0.0582
    $$

    One-factor: $\sigma_P^{(1)} = 0.005 \times 9.516 = 0.0476$

    **$T = 20$**: $B_x = (e^{-0.2}-1)/0.01 = -18.127$, $B_y = (e^{-2}-1)/0.1 = -8.647$

    $$
    \sigma_P^{(2)} \approx \sqrt{0.008215 + 0.004781 - 0.003758} \approx \sqrt{0.009238} \approx 0.0961
    $$

    One-factor: $\sigma_P^{(1)} = 0.005 \times 18.127 = 0.0906$

    **$T = 30$**: $B_x = (e^{-0.3}-1)/0.01 = -25.918$, $B_y = (e^{-3}-1)/0.1 = -9.502$

    $$
    \sigma_P^{(2)} \approx \sqrt{0.01680 + 0.005774 - 0.005902} \approx \sqrt{0.01667} \approx 0.1291
    $$

    One-factor: $\sigma_P^{(1)} = 0.005 \times 25.918 = 0.1296$

    The difference between one-factor and two-factor volatilities is most pronounced at intermediate maturities ($T = 5$ to $T = 10$), where the second factor contributes significantly but the negative correlation does not fully offset it. At very long maturities, $B_y$ saturates at $-1/\lambda_2 = -10$ while $B_x$ continues to grow (saturating at $-100$), so the first factor dominates and the two models converge in relative terms.

---

**Exercise 5.** In the one-factor limit $\sigma_2 \to 0$, verify that $A^{(2)}(t, T) \to A(t, T)$ (one-factor) and $\sigma_P^{(2)} \to |\sigma_1 B_x|$. Show that the cross-correlation terms in $V(t, T)$ vanish and the variance function reduces to the one-factor expression.

??? success "Solution to Exercise 5"
    Setting $\sigma_2 = 0$, the cross-correlation terms in $V(t, T)$ (proportional to $\rho\sigma_1\sigma_2$) vanish, and the $\sigma_2^2$ terms also vanish. The remaining expression is:

    $$
    V(t, T) = \frac{\sigma_1^2}{\lambda_1^2}\left[\tau + \frac{2}{\lambda_1}e^{-\lambda_1\tau} - \frac{1}{2\lambda_1}e^{-2\lambda_1\tau} - \frac{3}{2\lambda_1}\right]
    $$

    This is exactly the one-factor integrated variance function.

    For $A^{(2)}(t, T)$:

    $$
    A^{(2)}(t, T) = \ln\frac{P^M(0, T)}{P^M(0, t)} + \frac{1}{2}[V(t, T) + V(0, t) - V(0, T)]
    $$

    with $V$ now being the one-factor expression, this matches $A(t, T)$ of the one-factor model.

    For the bond price volatility:

    $$
    \sigma_P^{(2)}(t, T) = \sqrt{\sigma_1^2 B_x^2 + 0 + 0} = |\sigma_1 B_x(t, T)|
    $$

    which is the one-factor volatility. The $B_y$ term is irrelevant since it multiplies $y_t = 0$ in the bond price and $\sigma_2 = 0$ in the volatility.

    The deterministic drift also simplifies: $\varphi(t) = f^M(0,t) + \sigma_1^2(1 - e^{-\lambda_1 t})^2/(2\lambda_1^2)$, matching the one-factor $\alpha(t)$.

---

**Exercise 6.** When $\lambda_1 = \lambda_2 = \lambda$, the two-factor model degenerates. Show that in this case, $r_t = (x_t + y_t) + \varphi(t)$ behaves as a single OU process with effective volatility $\sigma_{\text{eff}} = \sqrt{\sigma_1^2 + \sigma_2^2 + 2\rho\sigma_1\sigma_2}$. What does this imply about the minimum number of distinct mean-reversion speeds needed for the second factor to add value?

??? success "Solution to Exercise 6"
    When $\lambda_1 = \lambda_2 = \lambda$, define $z_t = x_t + y_t$. Then:

    $$
    dz_t = -\lambda x_t\,dt + \sigma_1\,dW_t^{(1)} - \lambda y_t\,dt + \sigma_2\,dW_t^{(2)} = -\lambda z_t\,dt + \sigma_1\,dW_t^{(1)} + \sigma_2\,dW_t^{(2)}
    $$

    The stochastic part $\sigma_1 dW_t^{(1)} + \sigma_2 dW_t^{(2)}$ has quadratic variation:

    $$
    d\langle\sigma_1 W^{(1)} + \sigma_2 W^{(2)}\rangle_t = (\sigma_1^2 + \sigma_2^2 + 2\rho\sigma_1\sigma_2)\,dt = \sigma_{\text{eff}}^2\,dt
    $$

    By Levy's characterization theorem, $\tilde{W}_t = (\sigma_1 W_t^{(1)} + \sigma_2 W_t^{(2)})/\sigma_{\text{eff}}$ is a standard Brownian motion, and $dz_t = -\lambda z_t\,dt + \sigma_{\text{eff}}\,d\tilde{W}_t$.

    The bond price becomes:

    $$
    P(t, T) = \exp\!\left(A^{(2)}(t,T) + B_x(t,T)x_t + B_y(t,T)y_t\right)
    $$

    Since $\lambda_1 = \lambda_2 = \lambda$, we have $B_x(t,T) = B_y(t,T) = B(t,T)$, so:

    $$
    P(t, T) = \exp\!\left(A^{(2)}(t,T) + B(t,T)(x_t + y_t)\right) = \exp\!\left(A^{(2)}(t,T) + B(t,T)z_t\right)
    $$

    This is a single-factor bond price formula. All bonds at all maturities depend on the same single state variable $z_t$, so the yield curve can only undergo parallel-type shifts (same direction, different magnitudes). The second factor is redundant.

    This implies that for the second factor to add genuine value, the mean-reversion speeds must be distinct ($\lambda_1 \neq \lambda_2$). The minimum requirement is at least two distinct speeds, creating different decay profiles for the factor loadings and enabling non-parallel yield curve movements.

---

**Exercise 7.** The two-factor bond pricing PDE involves mixed partial derivatives $\partial^2 P / (\partial x\,\partial y)$ when $\rho \neq 0$. Explain why this cross-derivative term complicates finite-difference solutions. What transformation of variables would eliminate the cross-derivative, and what is the cost of this transformation?

??? success "Solution to Exercise 7"
    The mixed derivative $\rho\sigma_1\sigma_2\,\partial^2 P/(\partial x\,\partial y)$ complicates finite-difference methods in several ways:

    1. **Standard grid stencils**: The standard five-point stencil for the Laplacian on a rectangular grid naturally handles $\partial^2 P/\partial x^2$ and $\partial^2 P/\partial y^2$, but not $\partial^2 P/\partial x\,\partial y$. The cross-derivative requires a nine-point stencil, increasing computational complexity.

    2. **Stability issues**: Naive discretization of the cross-derivative using central differences can produce negative coefficients in the finite-difference scheme, violating the positivity condition and potentially causing oscillations or instability.

    3. **ADI complications**: Alternating Direction Implicit (ADI) methods, commonly used for 2D PDEs, naturally split the $x$ and $y$ directions. The cross-derivative does not fit into either direction, requiring special treatment (e.g., the Craig-Sneyd or Hundsdorfer-Verwer schemes that handle the mixed term explicitly).

    **Transformation to eliminate the cross-derivative:** The Cholesky decomposition can be used to decorrelate the variables. Define:

    $$
    \tilde{x} = x, \qquad \tilde{y} = \frac{y - \rho x}{\sqrt{1 - \rho^2}}
    $$

    In the new coordinates $(\tilde{x}, \tilde{y})$, the diffusion matrix becomes diagonal, eliminating the cross-derivative term.

    **Cost of the transformation:** The drift terms become coupled -- both $\tilde{x}$ and $\tilde{y}$ appear in the drift of each equation -- complicating the ADI splitting in a different way. Additionally, the boundary conditions in the transformed coordinates become non-standard (rotated boundaries), which can introduce complications for grid construction. The transformation trades one difficulty (cross-derivative) for another (coupled drifts and non-aligned boundaries), and in practice, modern ADI schemes that handle the cross-derivative directly are often preferred.
