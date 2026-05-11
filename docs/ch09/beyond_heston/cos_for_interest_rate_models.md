# COS Method for Interest Rate Models

The COS method was originally developed for equity option pricing, but its characteristic-function-based framework extends naturally to interest rate derivatives. When the short rate or forward rate follows an affine process, the bond price is an exponential-affine function of the state variable, and its characteristic function is available in closed form. This enables COS-based pricing of bond options, caps, floors, and swaptions---instruments where closed-form solutions are often unavailable or cumbersome. This section develops the COS pricing framework for interest rate models, focusing on the Vasicek and CIR models for bond options and the extension to swaption pricing.

!!! info "Prerequisites"

    - [COS Pricing Formula](../cos_method/cos_pricing_formula.md) (the COS framework)
    - Short rate models: Vasicek, CIR (affine structure, bond pricing formula)
    - Interest rate derivatives: bond options, caps/floors, swaptions

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Express zero-coupon bond prices as expectations under affine short rate models
    2. Derive the characteristic function of the short rate under Vasicek and CIR models
    3. Apply the COS method to price bond options (European options on zero-coupon bonds)
    4. Extend the framework to cap/floor and swaption pricing
    5. Compare COS-based prices against known closed-form solutions

---

## Affine Short Rate Models

In an affine short rate model, the short rate $r_t$ satisfies

$$
dr_t = \kappa(\theta - r_t)\,dt + \sigma\sqrt{\alpha + \beta r_t}\,dW_t
$$

where the choice of $\alpha$ and $\beta$ distinguishes models:

| Model | $\alpha$ | $\beta$ | Volatility structure |
|---|---|---|---|
| Vasicek | 1 | 0 | Constant ($\sigma$) |
| CIR | 0 | 1 | $\sigma\sqrt{r_t}$ (level-dependent) |

The key property is that the zero-coupon bond price $P(t, T) = \mathbb{E}^Q\!\left[\exp\!\left(-\int_t^T r_s\,ds\right)\bigg|\mathcal{F}_t\right]$ is an exponential-affine function of $r_t$:

$$
P(t, T) = \exp\!\left(A(t, T) - B(t, T)\,r_t\right)
$$

where $A$ and $B$ satisfy Riccati-type ODEs.

---

## Bond Option Pricing as a COS Problem

A European call option on a zero-coupon bond with maturity $T_B$, option expiry $T < T_B$, and strike $K$ has payoff

$$
\Phi = (P(T, T_B) - K)^+
$$

Under the risk-neutral measure, the option value at time $0$ is

$$
V = P(0, T)\,\mathbb{E}^{T}\!\left[(P(T, T_B) - K)^+\right]
$$

where $\mathbb{E}^T$ denotes expectation under the $T$-forward measure. Since $P(T, T_B) = \exp(A(T, T_B) - B(T, T_B)\,r_T)$, the payoff depends on $r_T$ through an exponential-affine transformation.

!!! note "Definition: COS Pricing of Bond Options"
    Let $X = r_T$ be the short rate at option expiry. The bond option price is

    $$
    V = P(0, T)\,e^{A(T,T_B)}\sum_{k=0}^{N-1}{}' F_k\, V_k
    $$

    where $F_k$ are the cosine coefficients of the density of $r_T$ under the $T$-forward measure, and $V_k$ are the payoff coefficients for the bond option payoff.

The payoff in terms of $x = r_T$ is

$$
\Phi(x) = (e^{A(T,T_B) - B(T,T_B)x} - K)^+
$$

This is a decreasing exponential function of $x$ (higher rates mean lower bond prices), so the exercise region is $x < x^*$ where $x^* = (A(T,T_B) - \ln K)/B(T,T_B)$.

---

## Characteristic Function of the Short Rate

To apply the COS method, we need the characteristic function of $r_T$ under the appropriate measure.

**Vasicek model.** Under the risk-neutral measure, $r_T | r_0$ is normally distributed:

$$
r_T \sim N\!\left(\theta + (r_0 - \theta)e^{-\kappa T},\; \frac{\sigma^2}{2\kappa}(1 - e^{-2\kappa T})\right)
$$

The characteristic function is:

$$
\phi_{\text{Vas}}(u) = \exp\!\left(iu\mu_r - \frac{\sigma_r^2 u^2}{2}\right)
$$

where $\mu_r = \theta + (r_0 - \theta)e^{-\kappa T}$ and $\sigma_r^2 = \frac{\sigma^2}{2\kappa}(1 - e^{-2\kappa T})$.

**CIR model.** Under the risk-neutral measure, $r_T | r_0$ follows a scaled noncentral chi-squared distribution. The characteristic function is:

$$
\phi_{\text{CIR}}(u) = \frac{\exp\!\left(\frac{\kappa^2\theta T/\sigma^2}{1 + \gamma \coth(\gamma T/2)/(2iu)}\right)}{(\cosh(\gamma T/2) + \frac{\kappa}{2\gamma}\sinh(\gamma T/2))^{2\kappa\theta/\sigma^2}} \cdot \exp\!\left(\frac{iu\, r_0 e^{-\kappa T/2}}{\cosh(\gamma T/2) + (\kappa/(2\gamma))\sinh(\gamma T/2)}\right)
$$

where $\gamma = \sqrt{\kappa^2 - 2\sigma^2 iu}$. A more compact form uses the Riccati solution:

$$
\phi_{\text{CIR}}(u) = \exp\!\left(\bar{A}(u, T) + \bar{B}(u, T)r_0\right)
$$

with $\bar{A}$ and $\bar{B}$ satisfying affine ODEs in $T$.

!!! tip "Forward Measure Adjustment"
    For bond option pricing, the density of $r_T$ under the $T$-forward measure differs from the risk-neutral density by a Radon--Nikodym derivative proportional to $P(T, T_B)/P(0, T_B)$. For affine models, this amounts to shifting the parameters in the characteristic function (replacing $\kappa$ by $\kappa + \sigma B(T, T_B)$ in the Vasicek case).

---

## Payoff Coefficients for Bond Options

The payoff coefficients for the bond option require integrating

$$
V_k = \int_a^b (e^{A - Bx} - K)^+\cos\!\left(\frac{k\pi(x-a)}{b-a}\right)dx
$$

where $A = A(T, T_B)$ and $B = B(T, T_B)$. The exercise region is $x \in [a, x^*]$ where $x^* = (A - \ln K)/B$.

This splits into:

$$
V_k = e^A\int_a^{x^*}e^{-Bx}\cos\!\left(\frac{k\pi(x-a)}{b-a}\right)dx - K\int_a^{x^*}\cos\!\left(\frac{k\pi(x-a)}{b-a}\right)dx
$$

Both integrals are of the same form as the equity case (exponential times cosine, and pure cosine), with closed-form solutions via the auxiliary functions $\chi_k$ and $\psi_k$ from the COS pricing formula section:

$$
V_k = e^A\,\chi_k^{(-B)}(a, x^*) - K\,\psi_k(a, x^*)
$$

where $\chi_k^{(-B)}$ denotes the $\chi_k$ integral with the exponential $e^{-Bx}$ instead of $e^x$.

---

## Example: Vasicek Bond Option

!!! example "COS Pricing of a Vasicek Bond Option"
    Parameters: $r_0 = 0.05$, $\kappa = 0.3$, $\theta = 0.05$, $\sigma = 0.01$, $T = 1$ (option expiry), $T_B = 5$ (bond maturity), $K = 0.90$ (strike on ZCB).

    **Closed-form (Jamshidian, 1989):** Under the Vasicek model, European bond options have a closed-form solution using the Jamshidian decomposition. The call price is $V_{\text{exact}} = 0.01234$ (illustrative).

    **COS method:** The short rate $r_T$ is Gaussian with known mean and variance. The characteristic function is elementary. With $N = 64$ and $[a, b]$ chosen as $[\mu_r - 10\sigma_r, \mu_r + 10\sigma_r]$:

    $$
    V_{\text{COS}} = 0.01234
    $$

    Agreement with the closed form to $10^{-10}$, as expected for a Gaussian distribution (super-exponential convergence).

---

## Extension to Caps and Floors

A caplet (the building block of a cap) is a call option on a forward rate, which can be related to a put option on a zero-coupon bond:

$$
\text{Caplet}(T_i, T_{i+1}) = (1 + \delta K) \cdot \text{Put on ZCB}(T_i, T_{i+1}, \text{strike } = 1/(1+\delta K))
$$

where $\delta = T_{i+1} - T_i$ is the accrual period and $K$ is the cap rate. Each caplet is priced independently using the COS bond option formula, and the full cap price is the sum over caplets.

---

## Extension to Swaption Pricing

Swaption pricing is more complex because the underlying swap value depends on multiple bond prices simultaneously. Under affine models, the Jamshidian (1989) decomposition reduces a swaption to a portfolio of bond options when the short rate is one-dimensional:

!!! note "Proposition: Jamshidian Decomposition"
    For a payer swaption on a swap with payment dates $T_1, \ldots, T_n$ and fixed rate $K$, the swaption value equals

    $$
    V_{\text{swaption}} = \sum_{i=1}^n c_i\, \text{Put}(T_0, T_i, K_i)
    $$

    where $c_i = \delta K$ for $i < n$ and $c_n = 1 + \delta K$, and the strike $K_i = P(r^*, T_i)$ with $r^*$ the critical rate solving $\sum_{i=1}^n c_i P(r^*, T_i) = 1$.

Each bond put is priced independently using the COS method, so the total swaption cost is $n$ COS evaluations.

!!! warning "Multi-Factor Models"
    The Jamshidian decomposition requires a one-dimensional state variable. For multi-factor models (e.g., two-factor Hull--White, Gaussian HJM), the decomposition does not apply, and the COS method must be adapted to two-dimensional Fourier expansions, which is considerably more complex.

---

## Summary

The COS method extends to interest rate derivatives by substituting the appropriate characteristic function:

| Derivative | State variable | CF needed | Payoff coefficients |
|---|---|---|---|
| Bond option | $r_T$ under forward measure | $\phi_{r_T}(u)$ | $\chi_k^{(-B)}$ and $\psi_k$ integrals |
| Caplet | $r_{T_i}$ under forward measure | Same as bond option | Via cap-bond option parity |
| Swaption (1-factor) | $r_{T_0}$ | Same | Jamshidian decomposition + bond options |

**The COS method's characteristic-function-based framework extends directly to interest rate derivatives under affine short rate models, providing efficient pricing of bond options, caps, floors, and swaptions with the same exponential convergence enjoyed by equity options.**

---

## Exercises

**Exercise 1.** For the Vasicek model with $r_0 = 0.05$, $\kappa = 0.3$, $\theta = 0.05$, $\sigma = 0.01$, and $T = 1$, compute the mean and variance of $r_T$: $\mu_r = \theta + (r_0 - \theta)e^{-\kappa T}$ and $\sigma_r^2 = \frac{\sigma^2}{2\kappa}(1 - e^{-2\kappa T})$. Write down the characteristic function $\phi_{\text{Vas}}(u) = \exp(iu\mu_r - \sigma_r^2 u^2/2)$ and evaluate it at $u = 0, 1, 10$.

??? success "Solution to Exercise 1"
    With $r_0 = 0.05$, $\kappa = 0.3$, $\theta = 0.05$, $\sigma = 0.01$, and $T = 1$:

    **Mean:**

    $$
    \mu_r = \theta + (r_0 - \theta)e^{-\kappa T} = 0.05 + (0.05 - 0.05)e^{-0.3} = 0.05
    $$

    Since $r_0 = \theta$, the mean stays at the long-run level regardless of $T$.

    **Variance:**

    $$
    \sigma_r^2 = \frac{\sigma^2}{2\kappa}(1 - e^{-2\kappa T}) = \frac{0.0001}{0.6}(1 - e^{-0.6}) = \frac{0.0001}{0.6}(1 - 0.54881) = \frac{0.0001 \times 0.45119}{0.6} \approx 7.520 \times 10^{-5}
    $$

    So $\sigma_r \approx 0.008672$.

    **Characteristic function:** $\phi_{\text{Vas}}(u) = \exp(iu\mu_r - \sigma_r^2 u^2 / 2) = \exp(0.05iu - 3.760 \times 10^{-5}u^2)$.

    **At $u = 0$:**

    $$
    \phi_{\text{Vas}}(0) = \exp(0) = 1
    $$

    This is the normalization condition satisfied by all characteristic functions.

    **At $u = 1$:**

    $$
    \phi_{\text{Vas}}(1) = \exp(0.05i - 3.760 \times 10^{-5}) = e^{-3.760 \times 10^{-5}}(\cos 0.05 + i\sin 0.05)
    $$

    $$
    \approx 0.99996(0.99875 + 0.04998i) \approx 0.99871 + 0.04997i
    $$

    **At $u = 10$:**

    $$
    \phi_{\text{Vas}}(10) = \exp(0.5i - 3.760 \times 10^{-3}) = e^{-0.003760}(\cos 0.5 + i\sin 0.5)
    $$

    $$
    \approx 0.99625(0.87758 + 0.47943i) \approx 0.87429 + 0.47763i
    $$

    Note that $|\phi(u)|$ decreases with $u$ due to the Gaussian damping factor $e^{-\sigma_r^2 u^2/2}$, which reflects the smoothness of the Gaussian density.

---

**Exercise 2.** For a European call on a zero-coupon bond, the exercise boundary is $x^* = (A(T, T_B) - \ln K)/B(T, T_B)$, where $A$ and $B$ are the bond pricing coefficients. Explain geometrically why the exercise region is $x < x^*$ (i.e., rates below the critical rate), and what this means financially: a bond call is exercised when rates are low (bond prices are high).

??? success "Solution to Exercise 2"
    The bond price is $P(T, T_B) = \exp(A(T, T_B) - B(T, T_B)\,r_T)$, which is a **decreasing** function of $r_T$ because $B(T, T_B) > 0$ for $T_B > T$. Geometrically, the mapping from $r_T$ to bond price is a downward-sloping exponential curve.

    The call payoff is $(P(T, T_B) - K)^+ = (\exp(A - Br_T) - K)^+$. This is positive when:

    $$
    \exp(A - Br_T) > K \iff A - Br_T > \ln K \iff r_T < \frac{A - \ln K}{B} = x^*
    $$

    So the exercise region is $r_T < x^*$, i.e., rates below the critical rate $x^*$.

    **Financial interpretation:** A bond call option is a bet that bond prices will be high (equivalently, that interest rates will be low) at expiry. When $r_T < x^*$, the short rate is low enough that the zero-coupon bond price exceeds the strike, making the call in-the-money. This is the opposite of an equity call, where exercise occurs when the price is high. The duality arises because bond prices and interest rates move inversely.

    Geometrically, plotting the payoff $(e^{A - Bx} - K)^+$ as a function of $x = r_T$: it equals zero for $x > x^*$ and curves upward exponentially as $x$ decreases below $x^*$.

---

**Exercise 3.** The payoff coefficients for a bond option involve $\chi_k^{(-B)}(a, x^*) = \int_a^{x^*}e^{-Bx}\cos(\omega_k(x-a))\,dx$. Derive the closed form by integration by parts, following the same approach used for $\chi_k$ in the equity case. Show that the result is $\frac{1}{B^2 + \omega_k^2}[\cdots]$ with appropriate boundary terms.

??? success "Solution to Exercise 3"
    We need to compute $\chi_k^{(-B)}(a, x^*) = \int_a^{x^*} e^{-Bx}\cos(\omega_k(x - a))\,dx$ where $\omega_k = k\pi/(b-a)$.

    Use the standard integral formula. Let $I = \int e^{-Bx}\cos(\omega_k(x-a))\,dx$. Write $\cos(\omega_k(x-a)) = \operatorname{Re}[e^{i\omega_k(x-a)}]$, so:

    $$
    I = \operatorname{Re}\!\left[\int e^{-Bx + i\omega_k(x-a)}\,dx\right] = \operatorname{Re}\!\left[e^{-i\omega_k a}\int e^{(-B + i\omega_k)x}\,dx\right]
    $$

    $$
    = \operatorname{Re}\!\left[\frac{e^{-i\omega_k a}\,e^{(-B+i\omega_k)x}}{-B + i\omega_k}\right]
    $$

    Multiply numerator and denominator by $(-B - i\omega_k)$:

    $$
    I = \operatorname{Re}\!\left[\frac{(-B - i\omega_k)\,e^{-Bx + i\omega_k(x-a)}}{B^2 + \omega_k^2}\right]
    $$

    Expanding the real part:

    $$
    I = \frac{e^{-Bx}}{B^2 + \omega_k^2}\left[-B\cos(\omega_k(x-a)) + \omega_k\sin(\omega_k(x-a))\right]
    $$

    Evaluating at the limits $x = a$ and $x = x^*$:

    $$
    \chi_k^{(-B)}(a, x^*) = \frac{1}{B^2 + \omega_k^2}\bigg[e^{-Bx^*}\big(-B\cos(\omega_k(x^*-a)) + \omega_k\sin(\omega_k(x^*-a))\big) - e^{-Ba}(-B)\bigg]
    $$

    This simplifies to:

    $$
    \chi_k^{(-B)}(a, x^*) = \frac{1}{B^2 + \omega_k^2}\bigg[e^{-Bx^*}\big(-B\cos(\omega_k(x^*-a)) + \omega_k\sin(\omega_k(x^*-a))\big) + Be^{-Ba}\bigg]
    $$

    Note the $1/(B^2 + \omega_k^2)$ prefactor, which is the same structure as the equity case with $B$ replacing $1$. For $k = 0$ ($\omega_0 = 0$), the integral reduces to $\chi_0^{(-B)} = (e^{-Ba} - e^{-Bx^*})/B$.

---

**Exercise 4.** A caplet on the forward rate $L(T_i, T_{i+1})$ can be expressed as $(1 + \delta K)$ times a put on a zero-coupon bond. Derive this relationship starting from the caplet payoff $\delta(L(T_i, T_{i+1}) - K)^+$ and using $L(T_i, T_{i+1}) = (1/P(T_i, T_{i+1}) - 1)/\delta$. What is the strike of the bond put in terms of $\delta$ and $K$?

??? success "Solution to Exercise 4"
    Starting from the caplet payoff at $T_{i+1}$, discounted to $T_i$:

    $$
    \text{Caplet payoff at } T_i = P(T_i, T_{i+1})\,\delta\,(L(T_i, T_{i+1}) - K)^+
    $$

    Using the definition of the simply compounded forward rate:

    $$
    L(T_i, T_{i+1}) = \frac{1}{\delta}\left(\frac{1}{P(T_i, T_{i+1})} - 1\right)
    $$

    Substituting:

    $$
    \delta(L - K)^+ = \delta\left(\frac{1}{\delta}\left(\frac{1}{P(T_i, T_{i+1})} - 1\right) - K\right)^+ = \left(\frac{1}{P(T_i, T_{i+1})} - 1 - \delta K\right)^+
    $$

    $$
    = \frac{1}{P(T_i, T_{i+1})}\left(1 - (1 + \delta K)P(T_i, T_{i+1})\right)^+
    $$

    Therefore, the caplet value at $T_i$ is:

    $$
    P(T_i, T_{i+1}) \cdot \frac{1}{P(T_i, T_{i+1})}\left(1 - (1+\delta K)P(T_i, T_{i+1})\right)^+
    $$

    $$
    = \left(1 - (1 + \delta K)P(T_i, T_{i+1})\right)^+
    $$

    $$
    = (1 + \delta K)\left(\frac{1}{1+\delta K} - P(T_i, T_{i+1})\right)^+
    $$

    This is $(1 + \delta K)$ times the payoff of a **put option on the zero-coupon bond** $P(T_i, T_{i+1})$ with strike:

    $$
    K_{\text{put}} = \frac{1}{1 + \delta K}
    $$

    So a caplet with cap rate $K$ is equivalent to $(1 + \delta K)$ put options on the ZCB with strike $1/(1 + \delta K)$.

---

**Exercise 5.** The Jamshidian decomposition reduces a swaption to a portfolio of bond options. For a payer swaption on a 3-year annual-pay swap with fixed rate $K = 0.04$ and option expiry $T_0 = 1$, list the bond options in the decomposition. How many COS evaluations are needed to price the swaption?

??? success "Solution to Exercise 5"
    For a payer swaption on a 3-year annual-pay swap with fixed rate $K = 0.04$ and option expiry $T_0 = 1$, the swap has payment dates $T_1 = 2$, $T_2 = 3$, $T_3 = 4$ (annual payments starting one year after option expiry), with accrual period $\delta = 1$.

    The Jamshidian decomposition gives:

    $$
    V_{\text{swaption}} = \sum_{i=1}^{3} c_i \cdot \text{Put}(T_0, T_i, K_i)
    $$

    The cash flow weights are:

    - $c_1 = \delta K = 1 \times 0.04 = 0.04$ (coupon at $T_1 = 2$)
    - $c_2 = \delta K = 0.04$ (coupon at $T_2 = 3$)
    - $c_3 = 1 + \delta K = 1.04$ (principal + coupon at $T_3 = 4$)

    The strikes $K_i = P(r^*, T_i)$ are determined by finding the critical rate $r^*$ that solves:

    $$
    0.04\,P(r^*, T_1) + 0.04\,P(r^*, T_2) + 1.04\,P(r^*, T_3) = 1
    $$

    This is a single nonlinear equation in $r^*$ (under Vasicek or CIR, $P$ is exponential-affine in $r^*$), solved by Newton's method or bisection.

    The bond options in the decomposition are:

    1. Put on ZCB maturing at $T_1 = 2$, with notional 0.04 and strike $K_1 = P(r^*, 2)$, expiring at $T_0 = 1$
    2. Put on ZCB maturing at $T_2 = 3$, with notional 0.04 and strike $K_2 = P(r^*, 3)$, expiring at $T_0 = 1$
    3. Put on ZCB maturing at $T_3 = 4$, with notional 1.04 and strike $K_3 = P(r^*, 4)$, expiring at $T_0 = 1$

    **Number of COS evaluations:** $n = 3$ independent COS evaluations (one per bond put), plus the one-time cost of solving for $r^*$. Each COS evaluation is $O(N)$, so the total cost is $O(3N)$, which is negligible.

---

**Exercise 6.** The COS method for interest rate models requires the characteristic function of $r_T$ under the $T$-forward measure, not the risk-neutral measure. For the Vasicek model, the forward measure adjustment replaces $\kappa$ by $\kappa + \sigma B(T, T_B)$. Explain why this measure change is needed and how it affects the mean and variance of $r_T$. What happens to the COS price if you forget to apply the measure change?

---

??? success "Solution to Exercise 6"
    **Why the measure change is needed:** The bond option value is:

    $$
    V = \mathbb{E}^Q\!\left[e^{-\int_0^T r_s\,ds}(P(T, T_B) - K)^+\right]
    $$

    The stochastic discount factor $e^{-\int_0^T r_s\,ds}$ is correlated with $r_T$ (since $r_T$ is part of the integral), making the expectation difficult to compute directly. The change to the $T$-forward measure eliminates the stochastic discounting:

    $$
    V = P(0, T)\,\mathbb{E}^T\!\left[(P(T, T_B) - K)^+\right]
    $$

    Under $\mathbb{E}^T$, the density of $r_T$ is different from the risk-neutral density. The Radon--Nikodym derivative is:

    $$
    \frac{d\mathbb{Q}^T}{d\mathbb{Q}} = \frac{e^{-\int_0^T r_s\,ds}}{P(0,T)}
    $$

    **Effect on Vasicek parameters:** For the Vasicek model, the forward measure dynamics are:

    $$
    dr_t = (\kappa\theta - (\kappa + \sigma B(t, T))r_t)\,dt + \sigma\,dW_t^T
    $$

    This is equivalent to replacing $\kappa$ with $\tilde{\kappa} = \kappa + \sigma B(T, T_B)$ (note: the adjustment uses $B$ evaluated for the bond maturity relevant to the pricing) and $\theta$ with $\tilde{\theta} = \kappa\theta / \tilde{\kappa}$.

    **Effect on mean and variance:**

    - The variance $\sigma_r^2 = \frac{\sigma^2}{2\tilde{\kappa}}(1 - e^{-2\tilde{\kappa}T})$ changes because $\tilde{\kappa} > \kappa$ (assuming $B > 0$), so the variance under the forward measure is **smaller** than under $\mathbb{Q}$---the rate has stronger mean reversion under the forward measure.
    - The mean $\mu_r = \tilde{\theta} + (r_0 - \tilde{\theta})e^{-\tilde{\kappa}T}$ shifts because $\tilde{\theta} < \theta$ (the long-run mean is pulled down) and the rate of convergence $\tilde{\kappa}$ is faster.

    **Consequence of forgetting the measure change:** If the risk-neutral CF is used instead of the forward-measure CF, the COS method computes $\mathbb{E}^Q[(P(T, T_B) - K)^+]$ instead of $\mathbb{E}^T[(P(T, T_B) - K)^+]$. Multiplying by $P(0, T)$ then gives:

    $$
    P(0, T)\,\mathbb{E}^Q[(P(T, T_B) - K)^+] \neq P(0, T)\,\mathbb{E}^T[(P(T, T_B) - K)^+] = V_{\text{correct}}
    $$

    The error is a systematic bias: the wrong density assigns incorrect probabilities to the exercise region, producing a bond option price that does not satisfy no-arbitrage conditions. For typical parameters, this error is small when the volatility $\sigma$ is small (the two measures are similar) but can be substantial for high-volatility or long-maturity scenarios.
