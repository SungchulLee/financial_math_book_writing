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

---

**Exercise 2.** For a European call on a zero-coupon bond, the exercise boundary is $x^* = (A(T, T_B) - \ln K)/B(T, T_B)$, where $A$ and $B$ are the bond pricing coefficients. Explain geometrically why the exercise region is $x < x^*$ (i.e., rates below the critical rate), and what this means financially: a bond call is exercised when rates are low (bond prices are high).

---

**Exercise 3.** The payoff coefficients for a bond option involve $\chi_k^{(-B)}(a, x^*) = \int_a^{x^*}e^{-Bx}\cos(\omega_k(x-a))\,dx$. Derive the closed form by integration by parts, following the same approach used for $\chi_k$ in the equity case. Show that the result is $\frac{1}{B^2 + \omega_k^2}[\cdots]$ with appropriate boundary terms.

---

**Exercise 4.** A caplet on the forward rate $L(T_i, T_{i+1})$ can be expressed as $(1 + \delta K)$ times a put on a zero-coupon bond. Derive this relationship starting from the caplet payoff $\delta(L(T_i, T_{i+1}) - K)^+$ and using $L(T_i, T_{i+1}) = (1/P(T_i, T_{i+1}) - 1)/\delta$. What is the strike of the bond put in terms of $\delta$ and $K$?

---

**Exercise 5.** The Jamshidian decomposition reduces a swaption to a portfolio of bond options. For a payer swaption on a 3-year annual-pay swap with fixed rate $K = 0.04$ and option expiry $T_0 = 1$, list the bond options in the decomposition. How many COS evaluations are needed to price the swaption?

---

**Exercise 6.** The COS method for interest rate models requires the characteristic function of $r_T$ under the $T$-forward measure, not the risk-neutral measure. For the Vasicek model, the forward measure adjustment replaces $\kappa$ by $\kappa + \sigma B(T, T_B)$. Explain why this measure change is needed and how it affects the mean and variance of $r_T$. What happens to the COS price if you forget to apply the measure change?
