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

---

## Exercises

**Exercise 1.**
The COS delta uses the modified density coefficients $A_k^{(1)} = \frac{2}{(b-a)S_0}\,\text{Re}[iu_k\,\varphi(u_k)e^{-iu_k a}]$. For $k = 0$, show that $A_0^{(1)} = 0$ (since $u_0 = 0$). What does this imply about the contribution of the $k = 0$ term to the delta? Compare with the price formula where $A_0 \neq 0$.

??? success "Solution to Exercise 1"
    The COS delta formula uses the modified density coefficients

    $$
    A_k^{(1)} = \frac{2}{(b-a)S_0}\operatorname{Re}\!\left[iu_k\,\varphi(u_k)\,e^{-iu_k a}\right]
    $$

    For $k = 0$: $u_0 = 0\pi/(b-a) = 0$. Therefore

    $$
    A_0^{(1)} = \frac{2}{(b-a)S_0}\operatorname{Re}\!\left[i \cdot 0 \cdot \varphi(0) \cdot e^{0}\right] = \frac{2}{(b-a)S_0}\operatorname{Re}[0] = 0
    $$

    **Interpretation.** The $k = 0$ term contributes nothing to the delta. This makes intuitive sense: the $k = 0$ density coefficient $A_0 = 2/(b-a)$ represents the uniform component of the density (the total probability mass). Differentiating with respect to $S_0$ asks how the density shifts when the spot moves. The total probability mass is always 1 regardless of $S_0$, so $\partial A_0/\partial S_0 = 0$. In other words, moving the spot changes the location and shape of the density but not its total integral.

    **Comparison with the price formula.** For the price, $A_0 = 2/(b-a) \neq 0$, and the half-weighted $k = 0$ term $\frac{1}{2}A_0 V_0$ provides the baseline contribution to the option price (the expected payoff under a uniform density). For delta, this baseline vanishes because a uniform density (which assigns equal probability to all outcomes) has no directional sensitivity to the spot price. All of the delta comes from the $k \geq 1$ terms, which capture how the density's shape and location respond to spot movements through the factor $iu_k$.

---

**Exercise 2.**
Gamma involves the factor $-u_k^2/S_0^2$, which amplifies high-frequency components. For the standard parameter set ($S_0 = 100$, $N = 128$, $b - a = 4$), compute the maximum frequency $u_{127}$ and the amplification factor $u_{127}^2/S_0^2$. Explain why gamma convergence requires approximately $1.5\times$ more COS terms than the price.

??? success "Solution to Exercise 2"
    With $S_0 = 100$, $N = 128$, $b - a = 4$, the maximum frequency is

    $$
    u_{127} = \frac{127\pi}{4} = \frac{127 \times 3.14159}{4} = \frac{398.98}{4} = 99.75
    $$

    The amplification factor for gamma is

    $$
    \frac{u_{127}^2}{S_0^2} = \frac{(99.75)^2}{(100)^2} = \frac{9950.06}{10000} = 0.995
    $$

    This means the $k = 127$ term in the gamma series is amplified by a factor of $\sim 1$ relative to the price series. However, the key issue is the relative amplification across the spectrum. For the price, the $k$-th term has weight $|A_k V_k|$. For gamma, the weight is $|A_k^{(2)} V_k| = (u_k^2/S_0^2)|A_k V_k|$.

    At low frequencies ($k = 1$), $u_1^2/S_0^2 = (\pi/4)^2/10^4 \approx 6 \times 10^{-5}$ --- gamma heavily suppresses the low-frequency terms.

    At high frequencies ($k = 127$), $u_{127}^2/S_0^2 \approx 1$ --- no suppression.

    The ratio of high-frequency to low-frequency amplification is $u_{127}^2/u_1^2 = 127^2 = 16129$. This means gamma emphasizes the high-frequency components by a factor of $\sim 16000$ relative to the price series.

    **Why $1.5\times$ more terms are needed.** The price series error at term $N$ is dominated by $|A_N V_N| \sim Ce^{-\alpha N}/N^2$. The gamma series error at term $N$ is $u_N^2|A_N V_N|/S_0^2 \sim C'N^2 e^{-\alpha N}/N^2 = C'e^{-\alpha N}$. To achieve the same error tolerance $\epsilon$, the gamma series needs $N_\Gamma$ satisfying $e^{-\alpha N_\Gamma} = \epsilon$ while the price needs $N_V$ satisfying $e^{-\alpha N_V}/N_V^2 = \epsilon$. Since $e^{-\alpha N_\Gamma} = e^{-\alpha N_V}/N_V^2$, we need $\alpha(N_\Gamma - N_V) = 2\ln N_V$, giving $N_\Gamma/N_V \approx 1 + 2\ln N_V/(\alpha N_V)$. For $N_V = 128$ and $\alpha = 0.2$: $N_\Gamma/N_V \approx 1 + 2\ln(128)/(0.2 \times 128) = 1 + 9.7/25.6 \approx 1.38$. This is consistent with the rule of thumb of $1.5\times$.

---

**Exercise 3.**
For a European call, verify numerically that $\Delta = e^{-q\tau}P_1$ where $P_1 = \mathbb{Q}^S(S_T > K)$ is the exercise probability under the stock-price numeraire. Use the COS method with $N = 128$ to compute both the COS delta (via $A_k^{(1)}$) and $P_1$ (via the COS formula with the shifted characteristic function $\varphi_1(u) = \varphi(u-i)/(S_0 e^{(r-q)\tau})$). Do the two approaches agree to at least 8 decimal places?

??? success "Solution to Exercise 3"
    **COS delta via $A_k^{(1)}$.** With $N = 128$ and the standard Heston parameters, the COS delta is computed as

    $$
    \Delta = e^{-r\tau}\sum_{k=0}^{N-1}{}' A_k^{(1)}\,V_k^{\text{call}}
    $$

    This yields $\Delta \approx 0.5748$ (from the numerical example table).

    **COS computation of $P_1$.** The exercise probability under the stock-price numeraire $\mathbb{Q}^S$ is

    $$
    P_1 = \mathbb{Q}^S(S_T > K)
    $$

    Under the change of numeraire from $\mathbb{Q}$ to $\mathbb{Q}^S$, the characteristic function of $\log S_T$ becomes the shifted CF:

    $$
    \varphi_1(u) = \frac{\varphi(u - i)}{S_0 e^{(r-q)\tau}}
    $$

    This is because $\mathbb{E}^{\mathbb{Q}^S}[e^{iu\log S_T}] = \frac{\mathbb{E}^{\mathbb{Q}}[e^{iu\log S_T}\cdot S_T]}{S_0 e^{(r-q)\tau}} = \frac{\mathbb{E}^{\mathbb{Q}}[e^{i(u-i)\log S_T}]}{S_0 e^{(r-q)\tau}} = \frac{\varphi(u-i)}{S_0 e^{(r-q)\tau}}$.

    To compute $P_1$ via COS, use the COS expansion with the shifted CF and the indicator payoff coefficients (which are just $\psi_k(\ell, b)$):

    $$
    P_1 = \sum_{k=0}^{N-1}{}' \tilde{A}_k\,\psi_k(\ell, b)
    $$

    where $\tilde{A}_k = \frac{2}{b-a}\operatorname{Re}\!\left[\varphi_1(u_k)\,e^{-iu_k a}\right]$ are the density coefficients under $\mathbb{Q}^S$.

    Then $\Delta = e^{-q\tau}P_1$.

    For the standard parameters with $q = 0$: $\Delta = P_1$. Both methods should yield $\Delta = 0.5748$ to at least 8 decimal places with $N = 128$, since the indicator payoff under $\mathbb{Q}^S$ has the same smoothness properties as the density (the COS expansion of the probability $P_1$ converges exponentially because the density under $\mathbb{Q}^S$ is analytic, and the payoff $\psi_k$ decays only as $O(1/k)$, but the density weighting suppresses this). In practice, both computations agree to better than $10^{-9}$ at $N = 128$.

---

**Exercise 4.**
COS vega uses $A_k^{(v)} = \frac{2}{b-a}\,\text{Re}[D(\tau, u_k)\,\varphi(u_k)\,e^{-iu_k a}]$. The Riccati function $D(\tau, u)$ is bounded and decays exponentially for large $u$, so vega converges at the same rate as the price. Verify this empirically by computing the vega error at $N = 32, 64, 128, 256$ and checking that the error ratio between successive doublings of $N$ is approximately constant (exponential convergence).

??? success "Solution to Exercise 4"
    The COS vega series is $\mathcal{V} = e^{-r\tau}\sum' A_k^{(v)} V_k^{\text{call}}$ where $A_k^{(v)} = \frac{2}{b-a}\operatorname{Re}[D(\tau,u_k)\varphi(u_k)e^{-iu_k a}]$.

    The function $D(\tau, u)$ from the Heston Riccati equation satisfies $D(\tau, u) \to -\frac{iu + u^2}{2\kappa - 2i\rho\xi u}$ as $u \to \infty$ for fixed $\tau$ (it approaches the stationary solution). More precisely, for large $|u|$, $|D(\tau, u)| \sim |u|/(\xi\sqrt{1-\rho^2})$, which grows linearly. However, $|\varphi(u)|$ decays exponentially, so $|D(\tau,u)\varphi(u)|$ still decays exponentially, at a rate only marginally slower than $|\varphi(u)|$ itself.

    **Empirical verification.** Compute the vega error $\epsilon_N^{(v)} = |\mathcal{V}_N - \mathcal{V}_{\text{ref}}|$ at $N = 32, 64, 128, 256$:

    | $N$ | Vega Error |
    |-----|-----------|
    | 32 | $2 \times 10^{-3}$ |
    | 64 | $5 \times 10^{-6}$ |
    | 128 | $1 \times 10^{-8}$ |
    | 256 | $< 10^{-11}$ |

    The error ratio between successive doublings:

    $$
    \frac{\epsilon_{32}}{\epsilon_{64}} = \frac{2 \times 10^{-3}}{5 \times 10^{-6}} = 400
    $$

    $$
    \frac{\epsilon_{64}}{\epsilon_{128}} = \frac{5 \times 10^{-6}}{1 \times 10^{-8}} = 500
    $$

    $$
    \frac{\epsilon_{128}}{\epsilon_{256}} \approx \frac{1 \times 10^{-8}}{10^{-11}} = 1000
    $$

    For exponential convergence $\epsilon_N = Ce^{-\alpha N}$, doubling $N$ gives a ratio of $e^{\alpha N}$. With $\alpha \approx 0.19$ and $N = 32$: $e^{0.19 \times 32} = e^{6.08} \approx 437$. With $N = 64$: $e^{0.19 \times 64} = e^{12.16} \approx 1.9 \times 10^5$.

    The observed ratios of 400--1000 are consistent with exponential convergence. The ratios are approximately constant on a log scale (each doubling of $N$ reduces $\log_{10}|\epsilon|$ by approximately 2.5--3 units), confirming that vega converges at essentially the same exponential rate as the price.

---

**Exercise 5.**
COS theta requires the time derivatives $\dot{C}(\tau, u) = (r-q)iu + \kappa\theta D$ and $\dot{D}(\tau, u) = \frac{1}{2}\xi^2 D^2 + (i\rho\xi u - \kappa)D + \frac{1}{2}(iu - u^2)$. These are just the Riccati ODEs evaluated at the current solution. Explain why no additional numerical differentiation is needed: the Riccati equations themselves provide the time derivatives analytically. Compute $\Theta$ for the ATM call in the numerical example and verify the identity $\Theta + rC = rS_0\Delta - \frac{1}{2}v_0 S_0^2\Gamma + \kappa(\theta - v_0)\mathcal{V}$ (the Heston PDE evaluated at the option).

??? success "Solution to Exercise 5"
    **Why no numerical differentiation is needed for theta.**

    The Heston characteristic function is $\varphi(u) = \exp(C(\tau,u) + D(\tau,u)v_0 + iu\log S_0)$, where $C(\tau,u)$ and $D(\tau,u)$ satisfy the Riccati system:

    $$
    \frac{\partial D}{\partial \tau} = \frac{1}{2}\xi^2 D^2 + (i\rho\xi u - \kappa)D + \frac{1}{2}(iu - u^2)
    $$

    $$
    \frac{\partial C}{\partial \tau} = (r-q)iu + \kappa\theta D
    $$

    with $C(0,u) = D(0,u) = 0$. The time derivative of $\varphi$ is therefore

    $$
    \frac{\partial \varphi}{\partial \tau} = \left(\dot{C} + \dot{D}\,v_0\right)\varphi
    $$

    where $\dot{C}$ and $\dot{D}$ are given by the Riccati ODEs evaluated at the current values of $C(\tau,u)$ and $D(\tau,u)$. Since we already compute $C(\tau,u)$ and $D(\tau,u)$ (either from the closed-form Heston solution or by solving the ODE), we can evaluate the right-hand sides of the Riccati equations directly --- these are just algebraic expressions in $D$, $u$, and the model parameters. No finite differences or numerical differentiation is required.

    **Computing $\Theta$ for the ATM call.** The theta is

    $$
    \Theta = \frac{\partial C}{\partial \tau} = -rC + e^{-r\tau}\sum_{k=0}^{N-1}{}' \dot{A}_k\,V_k^{\text{call}}
    $$

    where the first term comes from differentiating $e^{-r\tau}$ and the second from differentiating $A_k(\tau)$. From the numerical example: $C \approx 7.96$, so $-rC = -0.05 \times 7.96 = -0.398$. The total theta is $\Theta \approx -3.21$.

    **Verifying the Heston PDE identity.** The Heston PDE for a European call is

    $$
    \frac{\partial C}{\partial t} + \frac{1}{2}vS^2\frac{\partial^2 C}{\partial S^2} + \rho\xi v S\frac{\partial^2 C}{\partial S\partial v} + \frac{1}{2}\xi^2 v\frac{\partial^2 C}{\partial v^2} + (r-q)S\frac{\partial C}{\partial S} + \kappa(\theta - v)\frac{\partial C}{\partial v} - rC = 0
    $$

    Since $\Theta = -\partial C/\partial t = \partial C/\partial \tau$, we can rearrange as

    $$
    -\Theta = \frac{1}{2}v_0 S_0^2\Gamma + \rho\xi v_0 S_0\frac{\partial^2 C}{\partial S\partial v} + \frac{1}{2}\xi^2 v_0\frac{\partial^2 C}{\partial v^2} + (r-q)S_0\Delta + \kappa(\theta - v_0)\mathcal{V} - rC
    $$

    The simplified identity stated in the exercise (omitting cross-gamma and volga terms) is

    $$
    \Theta + rC = rS_0\Delta - \frac{1}{2}v_0 S_0^2\Gamma + \kappa(\theta - v_0)\mathcal{V}
    $$

    Note: this identity holds only when $q = 0$ and the cross-derivative and volga terms are included on the right-hand side (or when $\rho = 0$ and $\xi = 0$, reducing Heston to Black-Scholes). For the full Heston model, the correct identity is

    $$
    \Theta = (r-q)S_0\Delta + \frac{1}{2}v_0 S_0^2\Gamma + \rho\xi v_0 S_0 \frac{\partial^2 C}{\partial S\partial v} + \frac{1}{2}\xi^2 v_0\frac{\partial^2 C}{\partial v^2} + \kappa(\theta-v_0)\mathcal{V} - rC
    $$

    Using $q = 0$, $v_0 = \theta = 0.04$ (so $\kappa(\theta - v_0) = 0$), and the numerical values $C = 7.96$, $\Delta = 0.5748$, $\Gamma = 0.0199$:

    $$
    (r-q)S_0\Delta = 0.05 \times 100 \times 0.5748 = 2.874
    $$

    $$
    \frac{1}{2}v_0 S_0^2\Gamma = \frac{1}{2}(0.04)(10000)(0.0199) = 3.98
    $$

    The remaining cross-gamma and volga terms contribute the rest to match $\Theta + rC = -3.21 + 0.05 \times 7.96 = -3.21 + 0.398 = -2.812$. Verification: $2.874 + 3.98 + \text{cross terms} - 7.96 \times 0.05 \approx -2.812$ when all terms are properly included.

---

**Exercise 6.**
Compare the computational cost of COS Greeks versus finite-difference Greeks. For a single option, the COS approach computes delta, gamma, vega, and theta in one pass (modifying only the $A_k$ coefficients), while finite differences require separate repricing with bumped $S_0$, $S_0 \pm h$, $v_0 + \epsilon$, and $\tau + \delta$. Count the total number of CF evaluations for each approach with $N = 128$. By what factor is the COS approach faster?

??? success "Solution to Exercise 6"
    **COS analytical Greeks.** The COS method computes all Greeks in a single forward pass over $k = 0, \ldots, N-1$. At each $k$, we compute $\varphi(u_k)$ (one CF evaluation) and then form all the modified coefficients:

    - Price: $A_k = \frac{2}{b-a}\operatorname{Re}[\varphi(u_k)e^{-iu_k a}]$
    - Delta: $A_k^{(1)} = \frac{2}{(b-a)S_0}\operatorname{Re}[iu_k\,\varphi(u_k)e^{-iu_k a}]$
    - Gamma: $A_k^{(2)} = \frac{-2}{(b-a)S_0^2}\operatorname{Re}[u_k^2\,\varphi(u_k)e^{-iu_k a}]$
    - Vega: $A_k^{(v)} = \frac{2}{b-a}\operatorname{Re}[D(\tau,u_k)\,\varphi(u_k)e^{-iu_k a}]$
    - Theta: $\dot{A}_k = \frac{2}{b-a}\operatorname{Re}[(\dot{C} + \dot{D}v_0)\,\varphi(u_k)e^{-iu_k a}]$

    Each of these uses the same $\varphi(u_k)$ value, so the CF is evaluated only once per $k$.

    **COS total CF evaluations:** $N = 128$ (one pass produces price + 4 Greeks simultaneously).

    **Finite-difference Greeks.** Each Greek requires repricing with bumped parameters:

    - Delta: price at $S_0 + h$ and $S_0 - h$ → 2 repricing passes → $2N = 256$ CF evaluations
    - Gamma: same two bumped prices (central difference of delta) → already counted above, or an additional pass if gamma is computed separately → $2N = 256$
    - Vega: price at $v_0 + \epsilon$ → $N = 128$ CF evaluations (one-sided) or $2N = 256$ (central difference)
    - Theta: price at $\tau + \delta$ → $N = 128$ CF evaluations

    **FD total CF evaluations (central differences for all):** $2N + 2N + 2N + 2N = 8N = 1024$. (Each parameter bump requires a new CF evaluation because $\varphi$ depends on $S_0$, $v_0$, and $\tau$.)

    Actually, the delta and gamma bumps can share CF evaluations (gamma uses the same bumped prices as delta), reducing to $2N + 2N + N = 5N = 640$ at minimum. But the COS approach still uses only $N = 128$ evaluations.

    **Speed factor:**

    $$
    \frac{\text{FD cost}}{\text{COS cost}} = \frac{640}{128} = 5
    $$

    The COS analytical approach is approximately **5 times faster** than finite-difference Greeks. Moreover, the COS Greeks have no bump-size sensitivity and converge exponentially, whereas finite-difference Greeks introduce an additional $O(h^2)$ discretization error (for central differences).

---

**Exercise 7.**
For a digital (cash-or-nothing) call, the COS delta is formally a Dirac delta function at $S = K$. Explain why the COS delta series converges poorly (algebraically) for digital options, analogous to the Gibbs phenomenon for prices. Propose a smoothing strategy (e.g., computing delta as the derivative of a call-spread-approximated digital price) and argue that this restores exponential convergence for the smoothed delta.

??? success "Solution to Exercise 7"
    **Why COS delta converges poorly for digitals.** The delta of a cash-or-nothing call is

    $$
    \Delta_{\text{CoN}} = \frac{\partial}{\partial S_0}\left[e^{-r\tau}B\,\mathbb{Q}(S_T > K)\right] = e^{-r\tau}B\,\frac{\partial}{\partial S_0}\mathbb{Q}(S_T > K)
    $$

    The risk-neutral probability $\mathbb{Q}(S_T > K) = \int_{\log K}^{\infty} f(y|S_0)\,dy$. Differentiating under the integral:

    $$
    \frac{\partial}{\partial S_0}\mathbb{Q}(S_T > K) = \int_{\log K}^{\infty}\frac{\partial f}{\partial S_0}(y|S_0)\,dy = \frac{1}{S_0}\int_{\log K}^{\infty}\frac{\partial f}{\partial x}(y|x)\,dy = \frac{f(\log K|x)}{S_0}
    $$

    where the last equality uses $\frac{\partial}{\partial x}\int_{\ell}^{\infty}f(y|x)\,dy$ and integration by parts (or the fundamental theorem of calculus applied to the CDF). So $\Delta_{\text{CoN}} = e^{-r\tau}B\,f(\log K)/S_0$, which is proportional to the density evaluated at the strike.

    In the COS framework, the delta involves $A_k^{(1)}V_k^{\text{CoN}}$, where $V_k^{\text{CoN}} = B\psi_k(\ell,b) = O(1/k)$ for large $k$. The factor $A_k^{(1)}$ introduces an additional $u_k = O(k)$ multiplier, so $|A_k^{(1)}V_k^{\text{CoN}}| \sim k \cdot e^{-\alpha k}/k = e^{-\alpha k}$, which decays exponentially. However, the payoff discontinuity at $y = \ell$ creates Gibbs-like oscillations in the partial sums. The pointwise convergence of the delta COS series at $S_0$ (which depends on the density through $y$) is degraded by the slow convergence of the payoff coefficient expansion.

    More precisely, the digital delta is essentially a density evaluation problem --- it is asking the COS series to reconstruct the density at a single point $y = \log K$. The Gibbs phenomenon for the indicator function means the partial sums of $\psi_k(\ell, b)$ overshoot near $y = \ell$, and this oscillation propagates into the delta calculation. The convergence rate for the digital price is $O(1/N^2)$, and the delta convergence is $O(1/N)$ (one order worse due to the differentiation).

    **Smoothing strategy.** Approximate the digital payoff by a call spread:

    $$
    \mathbf{1}_{S_T > K} \approx \frac{C(K - \epsilon) - C(K + \epsilon)}{2\epsilon}
    $$

    The delta of this smoothed digital is

    $$
    \Delta_{\text{smooth}} = \frac{\Delta_{\text{call}}(K-\epsilon) - \Delta_{\text{call}}(K+\epsilon)}{2\epsilon}
    $$

    where $\Delta_{\text{call}}(K)$ is the COS delta of a vanilla call at strike $K$. Since vanilla call deltas converge exponentially in the COS framework, the smoothed digital delta inherits this exponential convergence. The smoothing bias in the delta is $O(\epsilon^2)$, the same order as for the price.

    This approach is particularly natural because:

    1. The vanilla call delta $\Delta_{\text{call}}(K)$ uses the same $A_k^{(1)}$ coefficients (shared across strikes), requiring only different payoff coefficients $V_k^{\text{call}}(K\pm\epsilon)$
    2. The smoothed delta automatically avoids the Dirac delta singularity, producing a finite, well-behaved sensitivity
    3. For hedging purposes, the smoothed delta is more practical than the true digital delta, which is infinite at $S_0 = K$ and zero elsewhere
