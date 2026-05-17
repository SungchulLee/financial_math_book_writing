# Zero-Coupon Bond Pricing Under CIR

The Cox-Ingersoll-Ross model belongs to the affine class of short-rate models, which means zero-coupon bond prices admit an exponential-affine closed-form solution. This analytical tractability is one of the main reasons the CIR model remains widely used in practice. Unlike the Vasicek model, the CIR bond price formula involves a square-root characteristic that prevents negative rates from appearing in the discount factor. This section derives the closed-form bond price formula from first principles, starting from the bond pricing PDE, introducing the affine ansatz, solving the resulting Riccati ordinary differential equations, and verifying the solution.

---

## Risk-neutral pricing framework

Recall (see [§ CIR SDE and Square-Root Process](cir_sde_and_square_root_process.md)) the CIR short rate under $\mathbb{Q}$:

$$
dr_t = \kappa(\theta - r_t)\,dt + \sigma\sqrt{r_t}\,dW_t^{\mathbb{Q}}.
$$

The zero-coupon bond price at time $t$ for maturity $T$ is defined by the conditional expectation

$$
P(t,T) = \mathbb{E}^{\mathbb{Q}}\!\left[\exp\!\left(-\int_t^T r_s\,ds\right)\,\bigg|\,\mathcal{F}_t\right]
$$

Because the short rate is Markovian, this price depends only on the current rate $r_t$ and the time to maturity $\tau = T - t$, so we write $P(t,T) = f(t, r_t)$.

---

## Bond pricing PDE

Applying Ito's lemma to $f(t, r_t)$ and requiring the discounted bond price $e^{-\int_0^t r_s\,ds}f(t,r_t)$ to be a $\mathbb{Q}$-martingale yields the fundamental PDE

$$
f_t + \kappa(\theta - r)f_r + \frac{1}{2}\sigma^2 r\,f_{rr} - r\,f = 0
$$

with the terminal condition $f(T, r) = 1$ for all $r \geq 0$. The key feature distinguishing this PDE from the Vasicek case is the factor of $r$ multiplying both $f_{rr}$ (from the square-root diffusion) and $f$ (from discounting). This state-dependent structure is precisely what makes the CIR model affine.

---

## Exponential-affine ansatz

The affine structure of the CIR PDE suggests searching for a solution of the form

$$
f(t, r) = A(\tau)\exp\!\big(-B(\tau)\,r\big)
$$

where $\tau = T - t$ is the time to maturity, $A(\tau)$ is a deterministic function, and $B(\tau)$ determines the rate sensitivity. The terminal condition $f(T, r) = 1$ translates to

$$
A(0) = 1, \qquad B(0) = 0
$$

Computing the required partial derivatives (noting $\partial_t = -\partial_\tau$):

$$
f_t = \left(-A'(\tau) + A(\tau)B'(\tau)\,r\right)\exp\!\big(-B(\tau)\,r\big)
$$

$$
f_r = -A(\tau)B(\tau)\exp\!\big(-B(\tau)\,r\big)
$$

$$
f_{rr} = A(\tau)B(\tau)^2\exp\!\big(-B(\tau)\,r\big)
$$

---

## Deriving the Riccati system

Substituting the ansatz into the PDE and dividing through by $A(\tau)\exp(-B(\tau)\,r)$ yields

$$
-\frac{A'(\tau)}{A(\tau)} + B'(\tau)\,r - \kappa\theta\,B(\tau) + \kappa\,B(\tau)\,r + \frac{1}{2}\sigma^2 B(\tau)^2\,r - r = 0
$$

Collecting terms by powers of $r$:

- **Coefficient of $r$**: $B'(\tau) + \kappa\,B(\tau) + \frac{1}{2}\sigma^2 B(\tau)^2 - 1 = 0$
- **Constant term**: $-\frac{A'(\tau)}{A(\tau)} - \kappa\theta\,B(\tau) = 0$

Since these must hold for all $r \geq 0$, each coefficient must vanish separately, producing the system:

**Riccati ODE for $B$:**

$$
B'(\tau) = 1 - \kappa\,B(\tau) - \frac{1}{2}\sigma^2 B(\tau)^2, \qquad B(0) = 0
$$

**Linear ODE for $A$:**

$$
\frac{A'(\tau)}{A(\tau)} = -\kappa\theta\,B(\tau), \qquad A(0) = 1
$$

equivalently $\ln A(\tau) = -\kappa\theta\int_0^\tau B(s)\,ds$.

---

## Solving the Riccati ODE

The Riccati equation for $B$ is a quadratic ODE. Define the discriminant

$$
\gamma = \sqrt{\kappa^2 + 2\sigma^2}
$$

This quantity $\gamma$ plays a central role analogous to $\kappa$ in the Vasicek model but incorporates the volatility through the square-root diffusion. The solution is

$$
B(\tau) = \frac{2(e^{\gamma\tau} - 1)}{(\gamma + \kappa)(e^{\gamma\tau} - 1) + 2\gamma}
$$

???+ note "Derivation of $B(\tau)$"

    The Riccati ODE $B' = 1 - \kappa B - \frac{1}{2}\sigma^2 B^2$ with $B(0) = 0$ can be solved by factoring the right-hand side. Write

    $$
    B' = -\frac{\sigma^2}{2}(B - B_+)(B - B_-)
    $$

    where $B_\pm = \frac{-\kappa \pm \gamma}{\sigma^2}$ are the roots of $1 - \kappa B - \frac{1}{2}\sigma^2 B^2 = 0$. Using partial fractions and separating variables:

    $$
    \frac{dB}{(B - B_+)(B - B_-)} = -\frac{\sigma^2}{2}\,d\tau
    $$

    $$
    \frac{1}{B_+ - B_-}\ln\frac{B - B_+}{B - B_-} = -\frac{\sigma^2}{2}\tau + C
    $$

    Applying $B(0) = 0$ to determine $C$, then solving for $B(\tau)$, yields the stated formula after algebraic simplification using $B_+ - B_- = \frac{2\gamma}{\sigma^2}$. $\square$

**Verification of initial condition**: At $\tau = 0$, the numerator $2(e^0 - 1) = 0$, so $B(0) = 0$. $\checkmark$

**Behavior as $\tau \to \infty$**: As $\tau \to \infty$, $B(\tau) \to \frac{2}{\gamma + \kappa} = B_+$, which is the positive equilibrium of the Riccati ODE.

---

## Solving for A

Substituting $B(\tau)$ into the ODE for $A$ and integrating:

$$
\ln A(\tau) = -\kappa\theta\int_0^\tau B(s)\,ds
$$

After evaluating the integral (which requires careful manipulation of the exponential terms), the result is

$$
A(\tau) = \left(\frac{2\gamma\,e^{(\kappa + \gamma)\tau/2}}{(\gamma + \kappa)(e^{\gamma\tau} - 1) + 2\gamma}\right)^{2\kappa\theta/\sigma^2}
$$

???+ note "Derivation of $A(\tau)$"

    Define $D(\tau) = (\gamma + \kappa)(e^{\gamma\tau} - 1) + 2\gamma$. Then $B(\tau) = \frac{2(e^{\gamma\tau} - 1)}{D(\tau)}$ and

    $$
    D'(\tau) = \gamma(\gamma + \kappa)e^{\gamma\tau}
    $$

    One can verify that

    $$
    B(\tau) = \frac{2}{\sigma^2}\left(\frac{D'(\tau)}{D(\tau)} - \frac{\gamma + \kappa}{2}\right)
    $$

    so the integral becomes

    $$
    \int_0^\tau B(s)\,ds = \frac{2}{\sigma^2}\left[\ln\frac{D(\tau)}{D(0)} - \frac{(\gamma + \kappa)\tau}{2}\right]
    $$

    Since $D(0) = 2\gamma$, this gives

    $$
    \ln A(\tau) = -\kappa\theta\cdot\frac{2}{\sigma^2}\left[\ln\frac{D(\tau)}{2\gamma} - \frac{(\gamma + \kappa)\tau}{2}\right] = \frac{2\kappa\theta}{\sigma^2}\left[\frac{(\gamma + \kappa)\tau}{2} - \ln\frac{D(\tau)}{2\gamma}\right]
    $$

    Exponentiating yields the stated formula. $\square$

**Verification of initial condition**: At $\tau = 0$, the denominator equals $2\gamma$ and the exponential equals $1$, giving $A(0) = 1$. $\checkmark$

---

## Complete bond price formula

Combining both components, the CIR zero-coupon bond price is

$$
P(t,T) = A(\tau)\,e^{-B(\tau)\,r_t}
$$

where $\tau = T - t$ and

$$
A(\tau) = \left(\frac{2\gamma\,e^{(\kappa + \gamma)\tau/2}}{(\gamma + \kappa)(e^{\gamma\tau} - 1) + 2\gamma}\right)^{2\kappa\theta/\sigma^2}
$$

$$
B(\tau) = \frac{2(e^{\gamma\tau} - 1)}{(\gamma + \kappa)(e^{\gamma\tau} - 1) + 2\gamma}
$$

$$
\gamma = \sqrt{\kappa^2 + 2\sigma^2}
$$

!!! tip "Interpreting the formula"
    The bond price has two components: $A(\tau)$ captures the effect of mean reversion and long-run mean on accumulated discounting, while $e^{-B(\tau)r_t}$ captures the sensitivity to the current short rate. Higher current rates $r_t$ reduce the bond price through the exponential factor, with the sensitivity governed by $B(\tau)$.

---

## Properties of the bond price

### Monotonicity in the short rate

Since $B(\tau) > 0$ for $\tau > 0$, the bond price is strictly decreasing in $r_t$:

$$
\frac{\partial P}{\partial r_t} = -B(\tau)\,P(t,T) < 0
$$

This confirms the economic intuition that higher current interest rates reduce the present value of future cash flows.

### Short-maturity limit

As $\tau \to 0^+$:

$$
B(\tau) \approx \tau - \frac{1}{2}(\kappa + \frac{1}{2}\sigma^2)\tau^2 + O(\tau^3)
$$

so for very short maturities, $P(t,T) \approx e^{-r_t\tau}$, which matches the instantaneous discounting rate.

### Long-maturity limit

As $\tau \to \infty$:

$$
B(\tau) \to B_\infty = \frac{2}{\gamma + \kappa}
$$

$$
\ln A(\tau) \sim \frac{2\kappa\theta}{\sigma^2}\left[\frac{\gamma + \kappa}{2} - \gamma\right]\tau = -\frac{\kappa\theta(\gamma - \kappa)}{\sigma^2}\,\tau
$$

Therefore the long-maturity yield is

$$
R_\infty = \lim_{\tau \to \infty}\frac{-\ln P(t,T)}{\tau} = \frac{2\kappa\theta}{\gamma + \kappa}
$$

This long rate is independent of the current short rate $r_t$ and depends only on the model parameters $\kappa$, $\theta$, and $\sigma$.

---

## Comparison with the Vasicek formula

| Feature | Vasicek | CIR |
|---------|---------|-----|
| **Ansatz** | $P = A(\tau)e^{-B(\tau)r}$ | $P = A(\tau)e^{-B(\tau)r}$ |
| **$B(\tau)$ ODE** | $B' = 1 - \kappa B$ (linear) | $B' = 1 - \kappa B - \frac{1}{2}\sigma^2 B^2$ (Riccati) |
| **$B(\tau)$ solution** | $\frac{1 - e^{-\kappa\tau}}{\kappa}$ | $\frac{2(e^{\gamma\tau} - 1)}{(\gamma+\kappa)(e^{\gamma\tau}-1)+2\gamma}$ |
| **Discriminant** | $\kappa$ (trivial) | $\gamma = \sqrt{\kappa^2 + 2\sigma^2}$ |
| **Rate dependence of vol** | None ($\sigma$ constant) | $\sigma\sqrt{r}$ (state-dependent) |
| **Negative rates possible** | Yes | No (if Feller condition holds) |

The additional quadratic term $\frac{1}{2}\sigma^2 B^2$ in the CIR Riccati ODE arises from the state-dependent volatility $\sigma\sqrt{r}$, which introduces an $r$-dependent contribution to $f_{rr}$ in the PDE. When $\sigma \to 0$, both models converge to pure mean-reversion discounting.

---

## Numerical example

Consider CIR parameters $\kappa = 0.5$, $\theta = 0.06$, $\sigma = 0.1$, and current rate $r_0 = 0.04$.

**Step 1**: Compute the discriminant:

$$
\gamma = \sqrt{0.5^2 + 2(0.1)^2} = \sqrt{0.25 + 0.02} = \sqrt{0.27} \approx 0.5196
$$

**Step 2**: For $\tau = 5$ years, compute $B(5)$:

$$
e^{\gamma \cdot 5} = e^{2.598} \approx 13.44
$$

$$
B(5) = \frac{2(13.44 - 1)}{(0.5196 + 0.5)(13.44 - 1) + 2(0.5196)} = \frac{24.88}{12.68 + 1.039} = \frac{24.88}{13.72} \approx 1.813
$$

**Step 3**: Compute $A(5)$:

$$
A(5) = \left(\frac{2(0.5196)\,e^{(0.5 + 0.5196)(2.5)}}{13.72}\right)^{2(0.5)(0.06)/(0.01)}
$$

$$
= \left(\frac{1.039 \cdot e^{2.549}}{13.72}\right)^{6} = \left(\frac{1.039 \cdot 12.80}{13.72}\right)^{6} \approx (0.969)^6 \approx 0.828
$$

**Step 4**: Bond price:

$$
P(0, 5) = 0.828 \cdot e^{-1.813 \times 0.04} = 0.828 \cdot e^{-0.0725} \approx 0.828 \cdot 0.930 \approx 0.770
$$

The corresponding continuously compounded yield is $R(0, 5) = -\ln(0.770)/5 \approx 0.0523$, or about 5.23%.

---

## Summary

The CIR model produces zero-coupon bond prices of the exponential-affine form $P(t,T) = A(\tau)e^{-B(\tau)r_t}$, where the functions $A$ and $B$ solve a coupled system of ordinary differential equations. The Riccati ODE for $B(\tau)$ --- quadratic rather than linear as in Vasicek --- arises from the state-dependent volatility $\sigma\sqrt{r}$ and is solved in closed form using the discriminant $\gamma = \sqrt{\kappa^2 + 2\sigma^2}$. The resulting formula preserves non-negativity of rates (when the Feller condition holds), provides the long-run yield $R_\infty = 2\kappa\theta/(\gamma + \kappa)$, and reduces to instantaneous discounting at short maturities. This closed-form solution is the foundation for yield curve fitting, bond option pricing, and calibration procedures developed in subsequent sections.

---

## Exercises

**Exercise 1.** Substitute the exponential-affine ansatz $f(t,r) = A(\tau)e^{-B(\tau)r}$ into the CIR bond pricing PDE and derive the two ODEs for $A$ and $B$ by collecting powers of $r$. Show each step explicitly.

??? success "Solution to Exercise 1"

    The CIR bond pricing PDE is $f_t + \kappa(\theta - r)f_r + \frac{1}{2}\sigma^2 r\,f_{rr} - rf = 0$ with $f(T,r) = 1$.

    Substitute $f(t,r) = A(\tau)e^{-B(\tau)r}$ with $\tau = T - t$. Since $\partial_t = -\partial_\tau$:

    **Step 1: Compute $f_t$.**

    $$
    f_t = \frac{\partial}{\partial t}\left[A(\tau)e^{-B(\tau)r}\right] = -A'(\tau)e^{-Br} + A(\tau)B'(\tau)r\,e^{-Br}
    $$

    **Step 2: Compute $f_r$ and $f_{rr}$.**

    $$
    f_r = -AB\,e^{-Br}, \qquad f_{rr} = AB^2\,e^{-Br}
    $$

    **Step 3: Substitute into the PDE.**

    $$
    \left[-A' + AB'r\right]e^{-Br} + \kappa(\theta - r)\left[-AB\right]e^{-Br} + \frac{1}{2}\sigma^2 r\left[AB^2\right]e^{-Br} - r\left[A\right]e^{-Br} = 0
    $$

    **Step 4: Divide by $Ae^{-Br}$.**

    $$
    -\frac{A'}{A} + B'r - \kappa\theta B + \kappa Br + \frac{1}{2}\sigma^2 B^2 r - r = 0
    $$

    **Step 5: Collect powers of $r$.**

    Coefficient of $r$:

    $$
    B' + \kappa B + \frac{1}{2}\sigma^2 B^2 - 1 = 0 \implies B'(\tau) = 1 - \kappa B - \frac{1}{2}\sigma^2 B^2
    $$

    Constant term:

    $$
    -\frac{A'}{A} - \kappa\theta B = 0 \implies \frac{A'(\tau)}{A(\tau)} = -\kappa\theta B(\tau)
    $$

    With initial conditions $B(0) = 0$ and $A(0) = 1$ from $f(T,r) = 1$.

---

**Exercise 2.** For $\kappa = 0.3$, $\theta = 0.05$, $\sigma = 0.08$, compute the discriminant $\gamma$, then evaluate $B(\tau)$ for $\tau = 1, 5, 10, 30$. What is the limiting value $B_\infty = 2/(\gamma + \kappa)$? How close is $B(30)$ to $B_\infty$?

??? success "Solution to Exercise 2"

    Given $\kappa = 0.3$, $\theta = 0.05$, $\sigma = 0.08$:

    $$
    \gamma = \sqrt{0.09 + 0.0128} = \sqrt{0.1028} \approx 0.3206
    $$

    $$
    B_\infty = \frac{2}{\gamma + \kappa} = \frac{2}{0.6206} \approx 3.222
    $$

    Computing $B(\tau)$ for each maturity:

    For $\tau = 1$: $e^{0.3206} = 1.378$.

    $$
    B(1) = \frac{2(0.378)}{0.6206(0.378) + 0.641} = \frac{0.756}{0.235 + 0.641} = \frac{0.756}{0.876} \approx 0.863
    $$

    For $\tau = 5$: $e^{1.603} = 4.968$.

    $$
    B(5) = \frac{2(3.968)}{0.6206(3.968) + 0.641} = \frac{7.936}{2.462 + 0.641} = \frac{7.936}{3.103} \approx 2.558
    $$

    For $\tau = 10$: $e^{3.206} = 24.68$.

    $$
    B(10) = \frac{2(23.68)}{0.6206(23.68) + 0.641} = \frac{47.36}{14.70 + 0.641} = \frac{47.36}{15.34} \approx 3.087
    $$

    For $\tau = 30$: $e^{9.618} \approx 15{,}043$.

    $$
    B(30) = \frac{2(15{,}042)}{0.6206(15{,}042) + 0.641} = \frac{30{,}084}{9{,}335} \approx 3.223
    $$

    $B(30) \approx 3.223$ vs $B_\infty = 3.222$: the difference is less than 0.001, so $B(30)$ is virtually equal to $B_\infty$.

---

**Exercise 3.** Factor the Riccati ODE as $B' = -\frac{\sigma^2}{2}(B - B_+)(B - B_-)$ where $B_{\pm} = (-\kappa \pm \gamma)/\sigma^2$. For $\kappa = 0.5$ and $\sigma = 0.1$, compute $B_+$ and $B_-$. Verify that $B_+ > 0$ is the stable equilibrium and $B_- < 0$ is the unstable equilibrium.

??? success "Solution to Exercise 3"

    For $\kappa = 0.5$, $\sigma = 0.1$: $\gamma = \sqrt{0.25 + 0.02} = 0.5196$.

    $$
    B_+ = \frac{-\kappa + \gamma}{\sigma^2} = \frac{-0.5 + 0.5196}{0.01} = \frac{0.0196}{0.01} = 1.961
    $$

    $$
    B_- = \frac{-\kappa - \gamma}{\sigma^2} = \frac{-0.5 - 0.5196}{0.01} = \frac{-1.0196}{0.01} = -101.96
    $$

    Verification: $B_+ = 1.961 > 0$ $\checkmark$ and $B_- = -101.96 < 0$ $\checkmark$.

    **Stability analysis:** At a fixed point $B^*$, the linearized ODE is $\delta\dot{B} = (-\kappa - \sigma^2 B^*)\delta B$. The eigenvalue is $-\kappa - \sigma^2 B^*$.

    At $B_+$: eigenvalue $= -\kappa - \sigma^2 B_+ = -0.5 - 0.01 \times 1.961 = -0.5196 = -\gamma < 0$. **Stable.**

    At $B_-$: eigenvalue $= -\kappa - \sigma^2 B_- = -0.5 - 0.01 \times (-101.96) = -0.5 + 1.0196 = +0.5196 = +\gamma > 0$. **Unstable.**

    Since $B(0) = 0$ lies between $B_-$ and $B_+$, and $B_+$ is the stable equilibrium, the solution $B(\tau)$ flows toward $B_+$ as $\tau \to \infty$. The equilibrium $B_-$ is unstable and repels nearby trajectories, so it is never approached.

---

**Exercise 4.** Compute the complete CIR bond price $P(0, 10)$ for $\kappa = 0.5$, $\theta = 0.06$, $\sigma = 0.10$, $r_0 = 0.05$. Show each intermediate step: $\gamma$, $e^{\gamma \cdot 10}$, $B(10)$, the denominator $D(10)$, $A(10)$, and finally $P = A \cdot e^{-Br_0}$.

??? success "Solution to Exercise 4"

    Given $\kappa = 0.5$, $\theta = 0.06$, $\sigma = 0.10$, $r_0 = 0.05$, $\tau = 10$.

    **Step 1:** $\gamma = \sqrt{0.25 + 0.02} = \sqrt{0.27} \approx 0.5196$.

    **Step 2:** $e^{\gamma \cdot 10} = e^{5.196} \approx 180.7$.

    **Step 3:** Denominator $D(10) = (0.5196 + 0.5)(180.7 - 1) + 2(0.5196) = 1.0196 \times 179.7 + 1.039 = 183.2 + 1.039 = 184.3$.

    **Step 4:** $B(10) = 2(180.7 - 1)/184.3 = 359.4/184.3 \approx 1.950$.

    **Step 5:** Exponent for $A$: $2\kappa\theta/\sigma^2 = 2(0.5)(0.06)/0.01 = 6$.

    $$
    A(10) = \left(\frac{2(0.5196) \times e^{(1.0196)(5)}}{184.3}\right)^6 = \left(\frac{1.039 \times e^{5.098}}{184.3}\right)^6
    $$

    $$
    e^{5.098} \approx 163.3
    $$

    $$
    A(10) = \left(\frac{1.039 \times 163.3}{184.3}\right)^6 = \left(\frac{169.7}{184.3}\right)^6 = (0.9209)^6 \approx 0.611
    $$

    **Step 6:** Bond price:

    $$
    P(0,10) = A(10) \times e^{-B(10) \times r_0} = 0.611 \times e^{-1.950 \times 0.05} = 0.611 \times e^{-0.0975} = 0.611 \times 0.9071 \approx 0.554
    $$

---

**Exercise 5.** The bond price sensitivity to the short rate is $\partial P/\partial r_t = -B(\tau)P(t,T)$. For a \$1,000,000 face value 10-year zero-coupon bond with the parameters from Exercise 4, compute the DV01 (dollar value of a one-basis-point change in $r_t$). Compare with the Vasicek DV01 using $B^{\text{Vas}}(10) = (1 - e^{-\kappa \cdot 10})/\kappa$.

??? success "Solution to Exercise 5"

    The DV01 is:

    $$
    \text{DV01} = B(\tau) \times P(t,T) \times 0.0001 \times \text{Face}
    $$

    From Exercise 4: $B(10) = 1.950$ and $P(0,10) = 0.554$. With face value \$1,000,000:

    **CIR DV01:**

    $$
    \text{DV01}_{\text{CIR}} = 1.950 \times 0.554 \times 0.0001 \times 1{,}000{,}000 = 1.080 \times 100 = \$108.0
    $$

    **Vasicek DV01:** $B^{\text{Vas}}(10) = (1 - e^{-5})/0.5 = (1 - 0.00674)/0.5 = 1.987$.

    For a fair comparison, we need the Vasicek bond price. The Vasicek $A(\tau)$ is different, but using the same parameters for $\kappa$ and $\theta$, the Vasicek bond price at $\tau = 10$ is approximately $P^{\text{Vas}} \approx 0.538$ (lower due to larger $B$ and additional convexity terms).

    $$
    \text{DV01}_{\text{Vas}} = 1.987 \times 0.538 \times 0.0001 \times 1{,}000{,}000 = 1.069 \times 100 = \$106.9
    $$

    The DV01 values are similar because the larger $B^{\text{Vas}}$ is partially offset by the smaller $P^{\text{Vas}}$. The CIR DV01 is slightly larger in absolute terms due to the higher bond price.

---

**Exercise 6.** Show that in the limit $\sigma \to 0$, the CIR bond price formula reduces to pure deterministic discounting: $P(t,T) = \exp(-\int_t^T r_s\,ds)$ where $r_s = \theta + (r_t - \theta)e^{-\kappa(s-t)}$. Verify by showing $\gamma \to \kappa$, $B(\tau) \to (1 - e^{-\kappa\tau})/\kappa$, and computing $\lim_{\sigma \to 0} A(\tau)$.

??? success "Solution to Exercise 6"

    As $\sigma \to 0$: $\gamma \to \kappa$.

    **$B(\tau)$ limit:** As shown previously, $B(\tau) \to (1 - e^{-\kappa\tau})/\kappa$, the Vasicek form.

    **$A(\tau)$ limit:** The exponent $2\kappa\theta/\sigma^2 \to \infty$. Write:

    $$
    \ln A(\tau) = \frac{2\kappa\theta}{\sigma^2}\ln\frac{2\gamma e^{(\kappa+\gamma)\tau/2}}{D(\tau)}
    $$

    As $\gamma \to \kappa$, $D(\tau) \to 2\kappa(e^{\kappa\tau}-1) + 2\kappa = 2\kappa e^{\kappa\tau}$.

    $$
    \frac{2\gamma e^{(\kappa+\gamma)\tau/2}}{D(\tau)} \to \frac{2\kappa e^{\kappa\tau}}{2\kappa e^{\kappa\tau}} = 1
    $$

    So $\ln A(\tau) = (2\kappa\theta/\sigma^2) \times \ln(1 - \epsilon)$ where $\epsilon \to 0$. We need L'Hopital or a more careful expansion. Writing $\ln A(\tau) = -\kappa\theta\int_0^\tau B(s)\,ds$:

    As $\sigma \to 0$, $B(s) \to (1 - e^{-\kappa s})/\kappa$, so:

    $$
    \ln A(\tau) \to -\kappa\theta\int_0^\tau \frac{1 - e^{-\kappa s}}{\kappa}\,ds = -\theta\left[\tau - \frac{1 - e^{-\kappa\tau}}{\kappa}\right] = -\theta\tau + \theta B(\tau)
    $$

    Therefore:

    $$
    \ln P(t,T) = \ln A(\tau) - B(\tau)r_t \to -\theta\tau + \theta B(\tau) - B(\tau)r_t = -\theta\tau + B(\tau)(\theta - r_t)
    $$

    With $B(\tau) = (1-e^{-\kappa\tau})/\kappa$:

    $$
    \ln P = -\theta\tau + \frac{(\theta - r_t)(1 - e^{-\kappa\tau})}{\kappa}
    $$

    The deterministic rate path is $r_s = \theta + (r_t - \theta)e^{-\kappa(s-t)}$. Its integral is:

    $$
    \int_t^T r_s\,ds = \theta\tau + (r_t - \theta)\frac{1 - e^{-\kappa\tau}}{\kappa} = \theta\tau - \frac{(\theta - r_t)(1 - e^{-\kappa\tau})}{\kappa}
    $$

    So $\ln P = -\int_t^T r_s\,ds$, confirming $P(t,T) = \exp(-\int_t^T r_s\,ds)$ in the deterministic limit. $\checkmark$

---

**Exercise 7.** Compare the CIR and Vasicek bond prices for $\tau = 1, 5, 10, 30$ using $\kappa = 0.5$, $\theta = 0.06$, $\sigma = 0.10$, $r_0 = 0.04$. For which maturities is the difference largest? Explain why the CIR price is higher than Vasicek for long maturities by relating the difference to the saturation levels $B_\infty^{\text{CIR}}$ versus $B_\infty^{\text{Vas}} = 1/\kappa$.

??? success "Solution to Exercise 7"

    Using $\kappa = 0.5$, $\theta = 0.06$, $\sigma = 0.10$, $r_0 = 0.04$, $\gamma = 0.5196$.

    **CIR bond prices** (from the formulas):

    | $\tau$ | $B^{\text{CIR}}$ | $A^{\text{CIR}}$ | $P^{\text{CIR}}$ |
    |:---:|:---:|:---:|:---:|
    | 1 | 0.786 | 0.989 | 0.958 |
    | 5 | 1.813 | 0.828 | 0.770 |
    | 10 | 1.950 | 0.654 | 0.604 |
    | 30 | 1.961 | 0.190 | 0.176 |

    **Vasicek bond prices** (with $B^{\text{Vas}}(\tau) = (1-e^{-0.5\tau})/0.5$):

    The Vasicek $A(\tau) = \exp\{(\theta - \sigma^2/(2\kappa^2))(B - \tau) - \sigma^2 B^2/(4\kappa)\}$.

    $\theta - \sigma^2/(2\kappa^2) = 0.06 - 0.01/0.5 = 0.06 - 0.02 = 0.04$.

    | $\tau$ | $B^{\text{Vas}}$ | $P^{\text{Vas}}$ |
    |:---:|:---:|:---:|
    | 1 | 0.787 | 0.957 |
    | 5 | 1.836 | 0.759 |
    | 10 | 1.987 | 0.578 |
    | 30 | 2.000 | 0.131 |

    **Differences:**

    | $\tau$ | $P^{\text{CIR}} - P^{\text{Vas}}$ |
    |:---:|:---:|
    | 1 | +0.001 |
    | 5 | +0.011 |
    | 10 | +0.026 |
    | 30 | +0.045 |

    The difference is **largest at 30 years**. CIR bond prices are consistently higher (yields lower) than Vasicek.

    **Explanation:** The CIR $B$ function saturates at $B_\infty^{\text{CIR}} = 2/(\gamma+\kappa) = 1.961$, which is less than $B_\infty^{\text{Vas}} = 1/\kappa = 2.0$. Since $P = A(\tau)e^{-B(\tau)r_0}$, a smaller $B$ means less sensitivity to the short rate, and the $e^{-Br_0}$ factor is larger for CIR. Additionally, the CIR $A(\tau)$ function captures a smaller convexity adjustment than Vasicek's, further supporting higher CIR prices. The net effect is that CIR long-maturity yields are lower than Vasicek's, because the state-dependent volatility $\sigma\sqrt{r}$ reduces effective volatility in low-rate states where the convexity correction matters most.
