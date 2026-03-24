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

---

**Exercise 2.** Using $\lambda_1 = 0.01$, $\lambda_2 = 0.1$, $\sigma_1 = 0.005$, $\sigma_2 = 0.008$, $\rho = -0.3$, and a flat market curve at 3\%, compute the two-factor bond price $P(5, 10)$ for factor values $x_5 = 0.002$ and $y_5 = -0.001$. Compare with the initial market discount factor $P^M(0, 10)/P^M(0, 5)$, which is the time-5 bond price under the one-factor model with $x_5 = y_5 = 0$.

---

**Exercise 3.** Show that the consistency condition $P(0, T) = P^M(0, T)$ holds by substituting $x_0 = y_0 = 0$ into the two-factor formula and using $V(0, 0) = 0$. Why is this condition essential for an arbitrage-free term structure model?

---

**Exercise 4.** Compute the total bond price volatility $\sigma_P^{(2)}(t, T)$ for $t = 0$, $T = 5, 10, 20, 30$ using the parameters in Exercise 2. Plot $\sigma_P^{(2)}(0, T)$ as a function of $T$ and compare with the one-factor volatility $\sigma_P^{(1)}(0, T) = |\sigma_1 B_x(0, T)|$. At what maturity does the difference become most pronounced?

---

**Exercise 5.** In the one-factor limit $\sigma_2 \to 0$, verify that $A^{(2)}(t, T) \to A(t, T)$ (one-factor) and $\sigma_P^{(2)} \to |\sigma_1 B_x|$. Show that the cross-correlation terms in $V(t, T)$ vanish and the variance function reduces to the one-factor expression.

---

**Exercise 6.** When $\lambda_1 = \lambda_2 = \lambda$, the two-factor model degenerates. Show that in this case, $r_t = (x_t + y_t) + \varphi(t)$ behaves as a single OU process with effective volatility $\sigma_{\text{eff}} = \sqrt{\sigma_1^2 + \sigma_2^2 + 2\rho\sigma_1\sigma_2}$. What does this imply about the minimum number of distinct mean-reversion speeds needed for the second factor to add value?

---

**Exercise 7.** The two-factor bond pricing PDE involves mixed partial derivatives $\partial^2 P / (\partial x\,\partial y)$ when $\rho \neq 0$. Explain why this cross-derivative term complicates finite-difference solutions. What transformation of variables would eliminate the cross-derivative, and what is the cost of this transformation?
