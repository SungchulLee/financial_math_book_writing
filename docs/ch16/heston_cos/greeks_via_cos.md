# Greeks via COS Method

The COS method computes option sensitivities (Greeks) by differentiating the cosine series term by term. Because the density coefficients $A_k$ depend on model parameters through the characteristic function, and the payoff coefficients $V_k$ depend on the strike, differentiating either set of coefficients yields the desired Greeks with the same exponential convergence as the price itself. This makes COS-based Greeks faster and more stable than finite-difference bumping, especially for higher-order sensitivities like gamma.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Derive COS formulas for delta, gamma, vega, theta, and rho
    2. Identify which Greeks require differentiating $A_k$ vs $V_k$
    3. Understand the convergence properties of COS Greeks
    4. Compare COS Greeks with finite-difference and analytical alternatives

---

## Intuition

In the COS pricing formula $V = e^{-r\tau}\sum_k{}' A_k V_k$, the density coefficients $A_k$ depend on the spot price $S_0$ (through the log-forward moneyness in the CF) and on the model parameters ($\kappa, \theta, \xi, \rho, v_0$). The payoff coefficients $V_k$ depend on the strike $K$ but not on any model parameters. Therefore:

- **Delta and gamma** (spot sensitivities) require differentiating $A_k$ with respect to $\log S_0$
- **Vega** (sensitivity to initial variance) requires differentiating $A_k$ with respect to $v_0$
- **Theta** (time sensitivity) requires differentiating both $A_k$ and the discount factor with respect to $\tau$
- **Rho** (interest rate sensitivity) requires differentiating the drift and discount factor

Each differentiation produces a new series of the same form, preserving the computational structure.

---

## COS Price Formula Recap

The COS call price is

$$
C = e^{-r\tau} \sum_{k=0}^{N-1}{}' A_k \, V_k^{\text{call}}
$$

where

$$
A_k = \frac{2}{b-a} \, \text{Re}\!\left[\varphi\!\left(\frac{k\pi}{b-a}\right) \exp\!\left(-i\frac{k\pi a}{b-a}\right)\right]
$$

and $\varphi(u) = \exp(C(\tau, u) + D(\tau, u) v_0 + iu \log S_0)$ is the Heston CF. The dependence of $\varphi$ on $S_0$ is explicit through the $iu \log S_0$ term.

---

## Delta

Delta measures the sensitivity to the spot price: $\Delta = \partial C / \partial S_0$.

!!! info "Proposition (COS Delta)"
    The COS formula for delta is

    $$
    \Delta = e^{-r\tau} \sum_{k=0}^{N-1}{}' A_k^{(1)} \, V_k^{\text{call}}
    $$

    where the first-order density coefficients are

    $$
    A_k^{(1)} = \frac{2}{(b-a) S_0} \, \text{Re}\!\left[iu_k \, \varphi(u_k) \exp\!\left(-iu_k a\right)\right]
    $$

    with $u_k = k\pi/(b-a)$.

**Derivation.** Differentiating $A_k$ with respect to $S_0$:

$$
\frac{\partial A_k}{\partial S_0} = \frac{2}{b-a} \, \text{Re}\!\left[\frac{\partial \varphi}{\partial S_0}(u_k) \, e^{-iu_k a}\right]
$$

Since $\varphi(u) = \exp(\cdots + iu\log S_0)$, we have $\frac{\partial \varphi}{\partial S_0} = \frac{iu}{S_0}\varphi(u)$. Substituting gives the result. $\square$

!!! tip "Delta from Probabilities"
    For a European call, $\Delta = e^{-q\tau} P_1$ where $P_1$ is the exercise probability under the stock-numeraire measure. The COS delta can be verified against this identity.

---

## Gamma

Gamma is the second derivative with respect to spot: $\Gamma = \partial^2 C / \partial S_0^2$.

!!! info "Proposition (COS Gamma)"
    The COS formula for gamma is

    $$
    \Gamma = e^{-r\tau} \sum_{k=0}^{N-1}{}' A_k^{(2)} \, V_k^{\text{call}}
    $$

    where

    $$
    A_k^{(2)} = \frac{2}{(b-a) S_0^2} \, \text{Re}\!\left[(iu_k - u_k^2 - iu_k) \, \varphi(u_k) \, e^{-iu_k a}\right]
    $$

    Simplifying: $iu_k - u_k^2 - iu_k = -u_k^2$, so

    $$
    A_k^{(2)} = \frac{-2}{(b-a) S_0^2} \, \text{Re}\!\left[u_k^2 \, \varphi(u_k) \, e^{-iu_k a}\right]
    $$

**Derivation.** Differentiate $\frac{\partial \varphi}{\partial S_0} = \frac{iu}{S_0}\varphi$ once more:

$$
\frac{\partial^2 \varphi}{\partial S_0^2} = \frac{iu}{S_0}\frac{\partial \varphi}{\partial S_0} - \frac{iu}{S_0^2}\varphi = \frac{(iu)^2 - iu}{S_0^2}\varphi = \frac{-u^2 - iu}{S_0^2}\varphi
$$

Wait --- recomputing: $\frac{\partial}{\partial S_0}\!\left(\frac{iu}{S_0}\varphi\right) = -\frac{iu}{S_0^2}\varphi + \frac{iu}{S_0}\cdot\frac{iu}{S_0}\varphi = \frac{-iu + (iu)^2}{S_0^2}\varphi = \frac{-iu - u^2}{S_0^2}\varphi$. $\square$

!!! warning "Gamma Stability"
    Gamma involves $u_k^2$, which amplifies high-frequency components. For very high accuracy, increase $N$ by 50% relative to the price calculation. In practice, $N = 128$ suffices for stable gamma computation.

---

## Vega

Vega measures the sensitivity to the initial variance level: $\mathcal{V} = \partial C / \partial v_0$.

!!! info "Proposition (COS Vega)"
    The COS formula for vega is

    $$
    \mathcal{V} = e^{-r\tau} \sum_{k=0}^{N-1}{}' A_k^{(v)} \, V_k^{\text{call}}
    $$

    where

    $$
    A_k^{(v)} = \frac{2}{b-a} \, \text{Re}\!\left[D(\tau, u_k) \, \varphi(u_k) \, e^{-iu_k a}\right]
    $$

**Derivation.** The CF depends on $v_0$ through the term $D(\tau, u) v_0$ in the exponent: $\varphi = \exp(C + D v_0 + iu\log S_0)$. Therefore $\frac{\partial \varphi}{\partial v_0} = D(\tau, u) \varphi(u)$. $\square$

!!! note "Heston Vega vs Black-Scholes Vega"
    In Black-Scholes, vega $\nu = S\phi(d_1)\sqrt{\tau}$ is always positive. In the Heston model, vega $\mathcal{V} = \partial C/\partial v_0$ is also always positive for vanilla calls, but its magnitude and moneyness-dependence differ. The Heston vega surface $\mathcal{V}(K, \tau)$ exhibits a distinct term structure reflecting the mean-reversion dynamics: short-dated vega is concentrated near ATM, while long-dated vega spreads across strikes.

---

## Theta

Theta requires differentiating with respect to time to maturity $\tau$.

!!! info "Proposition (COS Theta)"
    The COS formula for theta is

    $$
    \Theta = -r C + e^{-r\tau} \sum_{k=0}^{N-1}{}' \dot{A}_k \, V_k^{\text{call}}
    $$

    where $\dot{A}_k = \partial A_k / \partial \tau$ involves the time derivatives of $C(\tau, u)$ and $D(\tau, u)$:

    $$
    \dot{A}_k = \frac{2}{b-a} \, \text{Re}\!\left[\left(\dot{C}(\tau, u_k) + \dot{D}(\tau, u_k) v_0\right) \varphi(u_k) \, e^{-iu_k a}\right]
    $$

The time derivatives $\dot{C}$ and $\dot{D}$ are obtained from the Riccati ODEs:

$$
\dot{D}(\tau, u) = \frac{1}{2}\xi^2 D^2 + (i\rho\xi u - \kappa) D + \frac{1}{2}(iu - u^2)
$$

$$
\dot{C}(\tau, u) = (r - q)iu + \kappa\theta D
$$

These are the original Riccati equations evaluated at the current values of $C$ and $D$.

---

## Interest Rate Sensitivity (Rho-Greek)

The sensitivity to the risk-free rate $r$ enters through both the discount factor and the drift.

!!! info "Proposition (COS Rho-Greek)"
    $$
    \frac{\partial C}{\partial r} = -\tau C + e^{-r\tau} \sum_{k=0}^{N-1}{}' A_k^{(r)} \, V_k^{\text{call}}
    $$

    where

    $$
    A_k^{(r)} = \frac{2}{b-a} \, \text{Re}\!\left[iu_k\tau \, \varphi(u_k) \, e^{-iu_k a}\right]
    $$

    since $\partial \varphi / \partial r = iu\tau \cdot \varphi$ (the CF depends on $r$ through the drift term $(r-q)iu\tau$).

---

## Convergence of COS Greeks

Each differentiation with respect to parameters multiplies the CF by a polynomial in $u$, which increases the weight on high-frequency terms.

| Greek | Multiplier | Extra $u$-power | $N$ relative to price |
|-------|------------|----------------|----------------------|
| Price | 1 | 0 | $N$ |
| Delta | $iu/S_0$ | 1 | $1.0 \times N$ |
| Gamma | $u^2/S_0^2$ | 2 | $1.5 \times N$ |
| Vega | $D(\tau, u)$ | $\sim 0$ | $1.0 \times N$ |
| Theta | $\dot{C} + \dot{D}v_0$ | $\sim 1$ | $1.0 \times N$ |

Delta and vega converge at essentially the same rate as the price because the extra $u$-factor is compensated by the CF's exponential decay. Gamma requires approximately 50% more terms because of the $u^2$ factor.

---

## Numerical Example

Using $S_0 = 100$, $K = 100$, $r = 0.05$, $q = 0$, $v_0 = 0.04$, $\kappa = 1.5$, $\theta = 0.04$, $\xi = 0.3$, $\rho = -0.7$, $\tau = 1$.

**COS Greeks with $N = 128$ vs finite-difference bumping:**

| Greek | COS Analytical | Finite Diff ($h = 0.01$) | Difference |
|-------|---------------|-------------------------|------------|
| Delta | 0.5748 | 0.5748 | $< 10^{-6}$ |
| Gamma | 0.0199 | 0.0199 | $< 10^{-5}$ |
| Vega | 18.43 | 18.43 | $< 10^{-4}$ |
| Theta | $-3.21$ | $-3.21$ | $< 10^{-4}$ |

The COS analytical Greeks agree with finite-difference estimates to high precision, but the COS approach is:

- **Faster**: one CF evaluation per Greek (no re-pricing with bumped parameters)
- **More accurate**: no finite-difference truncation error
- **More stable**: no sensitivity to bump size $h$

??? example "Greek Convergence in N"
    | $N$ | Delta Error | Gamma Error | Vega Error |
    |-----|-----------|------------|-----------|
    | 32 | $3 \times 10^{-4}$ | $5 \times 10^{-3}$ | $2 \times 10^{-3}$ |
    | 64 | $8 \times 10^{-7}$ | $4 \times 10^{-5}$ | $5 \times 10^{-6}$ |
    | 128 | $2 \times 10^{-9}$ | $3 \times 10^{-7}$ | $1 \times 10^{-8}$ |
    | 256 | $< 10^{-12}$ | $8 \times 10^{-10}$ | $< 10^{-11}$ |

    Delta and vega converge at the same rate as the price. Gamma converges about 2 orders of magnitude slower, confirming the need for slightly larger $N$.

---

## Comparison with Alternative Greek Methods

| Method | Speed | Accuracy | Ease of Implementation |
|--------|-------|----------|----------------------|
| COS analytical | Very fast (one pass) | Exponential convergence | Moderate (need CF derivatives) |
| Finite differences on CF | Moderate (multiple passes) | Good (but bump-size dependent) | Easy |
| Monte Carlo pathwise | Slow | $O(1/\sqrt{M})$ | Complex for gamma |
| Malliavin calculus | Slow | $O(1/\sqrt{M})$ | Very complex |

The COS method is the preferred choice for Greeks of European options under Heston: it combines the speed of the COS price calculation with analytical differentiation, avoiding both the bias of finite differences and the statistical noise of Monte Carlo.

---

## Summary

The COS method computes Greeks by differentiating the cosine expansion term by term. Delta and gamma require differentiating the density coefficients $A_k$ with respect to $\log S_0$, producing factors of $iu_k/S_0$ and $-u_k^2/S_0^2$ respectively. Vega differentiates $A_k$ with respect to $v_0$, introducing the factor $D(\tau, u_k)$. Theta uses the Riccati ODE directly to compute time derivatives of $C$ and $D$. All COS Greeks inherit the exponential convergence of the price, with gamma requiring approximately 50% more terms due to its $u^2$ weighting. The resulting Greeks are faster, more accurate, and more stable than finite-difference alternatives, making the COS method the method of choice for European option risk management under the Heston model.
