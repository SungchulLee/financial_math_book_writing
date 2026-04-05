# Similarity Solutions and Scaling Structure

The heat equation and separation of variables sections both transformed the Black-Scholes PDE into standard forms and solved them. But neither explained *why* the final formula depends on the particular combinations $\ln(S/K)/(\sigma\sqrt{\tau})$ and $r\tau$ rather than on $S$, $K$, $\sigma$, $\tau$, and $r$ independently. The answer lies in **scale invariance** and **dimensional analysis**.

Similarity solutions identify combinations of variables that respect the symmetry of a PDE, potentially reducing it to an ODE. Unlike the previous methods, this section does not provide a standalone derivation of the Black-Scholes formula. Instead, it reveals the **structural reason** why the formula takes the form it does: $d_1$ and $d_2$ are modified similarity coordinates, and the dependence on $S/K$, $\sigma\sqrt{\tau}$, and $r\tau$ is forced by dimensional analysis. The naive similarity ansatz does not fully reduce the Black-Scholes PDE to an ODE --- the interest rate $r$ breaks exact self-similarity --- but the scaling structure it uncovers is essential for understanding asymptotic behavior and building intuition.

---

## 1. Dimensional Analysis Foundation

### Physical Dimensions

In the Black-Scholes problem, the dimensional quantities are:

- $S$: stock price $[\$]$
- $K$: strike price $[\$]$
- $t, T$: time $[T]$
- $\sigma$: volatility $[T^{-1/2}]$ (since $dW_t$ scales as $\sqrt{dt}$)
- $r$: interest rate $[T^{-1}]$
- $V$: option value $[\$]$

### Buckingham Pi Theorem

With $n = 6$ variables and $m = 2$ fundamental dimensions ($[\$], [T]$), we get $n - m = 4$ dimensionless groups.

### Dimensionless Variables

Define:

$$
\pi_1 = \frac{S}{K} \quad \text{(moneyness)}
$$

$$
\pi_2 = \sigma\sqrt{T-t} = \sigma\sqrt{\tau} \quad \text{(scaled time)}
$$

$$
\pi_3 = r\tau \quad \text{(discount factor exponent)}
$$

$$
\pi_4 = \frac{V}{K} \quad \text{(normalized value)}
$$

### Dimensional Reduction

The option value must have the form:

$$
V(S,K,t,\sigma,r,T) = K \cdot f\!\left(\frac{S}{K},\, \sigma\sqrt{\tau},\, r\tau\right)
$$

This is the most general form consistent with dimensional analysis.

---

## 2. Scale Invariance of the Black-Scholes PDE

### The PDE

$$
\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{\sigma^2 S^2}{2}\frac{\partial^2 V}{\partial S^2} - rV = 0
$$

### Scaling Transformation

Consider the one-parameter family of transformations:

$$
S \to \lambda S, \quad K \to \lambda K, \quad V \to \lambda V
$$

with $t, \sigma, r$ unchanged.

### Invariance

Substituting into the PDE:

$$
\frac{\partial(\lambda V)}{\partial t} + r(\lambda S)\frac{\partial(\lambda V)}{\partial(\lambda S)} + \frac{\sigma^2(\lambda S)^2}{2}\frac{\partial^2(\lambda V)}{\partial(\lambda S)^2} - r(\lambda V)
$$

$$
= \lambda\left[\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{\sigma^2 S^2}{2}\frac{\partial^2 V}{\partial S^2} - rV\right] = 0
$$

The PDE is **homogeneous of degree 1** in $(S, K, V)$.

### Economic Interpretation

If all dollar amounts scale by $\lambda$ (change of currency), the form of the PDE does not change. This is the **scale invariance** or **homogeneity** of the market.

---

## 3. Similarity Variable for the Black-Scholes PDE

### Log-Moneyness Variable

The most natural similarity variable combines space and time:

$$
\xi = \frac{\ln(S/K)}{\sigma\sqrt{\tau}} = \frac{x}{\sigma\sqrt{\tau}}
$$

where $x = \ln(S/K)$ and $\tau = T - t$.

### Physical Meaning

- Numerator: **log-moneyness** (how far from strike in log terms)
- Denominator: **volatility times the time scale** (uncertainty measure)
- $\xi$: **standardized distance** from strike

For $|\xi| \approx 1$: option is at-the-money over the relevant time scale.
For $|\xi| \gg 1$: option is deep in- or out-of-the-money.

### Alternative Variables

Other common choices:

$$
\eta = \frac{\ln(S/K) + (r \pm \frac{\sigma^2}{2})\tau}{\sigma\sqrt{\tau}} \quad \text{(drift-adjusted)}
$$

$$
\zeta = \frac{S}{Ke^{-r\tau}} \quad \text{(forward moneyness)}
$$

Each has advantages for different problems.

---

## 4. Attempt to Reduce the Black-Scholes PDE to an ODE

### Similarity Ansatz

Seek a solution of the form:

$$
V(S,t) = K \cdot g(\xi) = K \cdot g\!\left(\frac{\ln(S/K)}{\sigma\sqrt{\tau}}\right)
$$

### Computing Derivatives

Partial derivatives of $\xi$:

$$
\frac{\partial\xi}{\partial\tau} = -\frac{\ln(S/K)}{2\sigma\tau^{3/2}} = -\frac{\xi}{2\tau}
$$

$$
\frac{\partial\xi}{\partial S} = \frac{1}{S\sigma\sqrt{\tau}}
$$

$$
\frac{\partial^2\xi}{\partial S^2} = -\frac{1}{S^2\sigma\sqrt{\tau}}
$$

Chain rule:

$$
\frac{\partial V}{\partial t} = -\frac{\partial V}{\partial\tau} = K g'(\xi)\frac{\xi}{2\tau}
$$

$$
\frac{\partial V}{\partial S} = K g'(\xi) \cdot \frac{1}{S\sigma\sqrt{\tau}}
$$

$$
\frac{\partial^2 V}{\partial S^2} = K g''(\xi) \cdot \frac{1}{S^2\sigma^2\tau} - K g'(\xi) \cdot \frac{1}{S^2\sigma\sqrt{\tau}}
$$

### Substituting into the PDE

$$
Kg'(\xi)\frac{\xi}{2\tau} + rS \cdot Kg'(\xi)\frac{1}{S\sigma\sqrt{\tau}} + \frac{\sigma^2 S^2}{2}\!\left[Kg''(\xi)\frac{1}{S^2\sigma^2\tau} - Kg'(\xi)\frac{1}{S^2\sigma\sqrt{\tau}}\right] - rKg(\xi) = 0
$$

Simplifying:

$$
\frac{Kg'(\xi)\xi}{2\tau} + \frac{rKg'(\xi)}{\sigma\sqrt{\tau}} + \frac{Kg''(\xi)}{2\tau} - \frac{Kg'(\xi)}{2\sigma\sqrt{\tau}} - rKg(\xi) = 0
$$

Multiply by $\tau / K$:

$$
\frac{g'(\xi)\xi}{2} + \frac{rg'(\xi)\sqrt{\tau}}{\sigma} + \frac{g''(\xi)}{2} - \frac{g'(\xi)\sqrt{\tau}}{2\sigma} - rg(\xi)\tau = 0
$$

### The Ansatz Fails: Non-Similarity

The presence of $\tau$ prevents complete reduction to an ODE. The interest rate $r$ introduces a **scale** that breaks perfect similarity. This is a key structural observation: the Black-Scholes PDE is not purely self-similar, and no single-variable reduction of the form $V = Kg(\xi)$ eliminates time entirely.

---

## 5. Modified Similarity Variables and the Black-Scholes Structure

### Dimensionless Time

Including the interest rate scaling yields the drift-adjusted similarity variable:

$$
\xi = \frac{\ln(S/K) + (r - \frac{\sigma^2}{2})\tau}{\sigma\sqrt{\tau}}
$$

This is related to $d_2$ in the Black-Scholes formula.

### Modified Ansatz

Instead of a single similarity function, try:

$$
V(S,t) = Se^{-q\tau}h(\xi_1) - Ke^{-r\tau}h(\xi_2)
$$

where:

$$
\xi_1 = \frac{\ln(S/K) + (r + \frac{\sigma^2}{2})\tau}{\sigma\sqrt{\tau}} = d_1
$$

$$
\xi_2 = \frac{\ln(S/K) + (r - \frac{\sigma^2}{2})\tau}{\sigma\sqrt{\tau}} = d_2
$$

This is the **Black-Scholes structure**: the formula decomposes into two terms, each involving a similarity coordinate evaluated through the same function $h$.

### The ODE for h

Both $h(\xi_1)$ and $h(\xi_2)$ satisfy the same second-order ODE:

$$
\frac{d^2h}{d\xi^2} + \xi\frac{dh}{d\xi} = 0
$$

### Solution

Integrate once:

$$
\frac{dh}{d\xi} = Ce^{-\xi^2/2}
$$

Integrate again:

$$
h(\xi) = C_1\int_{-\infty}^{\xi}e^{-s^2/2}\,ds + C_2 = C_1\sqrt{2\pi}\,N(\xi) + C_2
$$

where $N(\xi) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\xi}e^{-s^2/2}\,ds$ is the standard normal CDF. The Black-Scholes formula emerges with $h = N$ (after applying boundary conditions to fix the constants).

---

## 6. Heat Equation Similarity

### Transformed PDE

In variables $x = \ln(S/K)$ and $\tau = T - t$, after removing drift and decay:

$$
\frac{\partial w}{\partial \tau} = \frac{\partial^2 w}{\partial x^2}
$$

This is the heat equation.

### Self-Similar Solution

The fundamental solution (heat kernel) has the form:

$$
w(x,\tau) = \frac{1}{\sqrt{\tau}}\,G\!\left(\frac{x}{\sqrt{\tau}}\right)
$$

where $\eta = x / \sqrt{\tau}$ is the similarity variable.

### Reduction to ODE

Substitute:

$$
\frac{\partial w}{\partial\tau} = -\frac{1}{2\tau^{3/2}}G(\eta) - \frac{\eta}{2\tau^{3/2}}G'(\eta)
$$

$$
\frac{\partial^2 w}{\partial x^2} = \frac{1}{\tau^{3/2}}G''(\eta)
$$

The heat equation becomes:

$$
-\frac{1}{2\tau^{3/2}}G - \frac{\eta}{2\tau^{3/2}}G' = \frac{1}{\tau^{3/2}}G''
$$

Multiply by $\tau^{3/2}$:

$$
G''(\eta) + \frac{\eta}{2}G'(\eta) + \frac{1}{2}G(\eta) = 0
$$

### Solution: Gaussian

The solution is:

$$
G(\eta) = Ce^{-\eta^2/4}
$$

Therefore:

$$
w(x,\tau) = \frac{C}{\sqrt{4\pi\tau}}\,e^{-x^2/(4\tau)}
$$

This is the **heat kernel** (fundamental solution). Unlike the Black-Scholes PDE, the heat equation admits an exact self-similar reduction because there is no interest-rate parameter to break the scaling.

---

## 7. Explicit Example: European Call

### Terminal Condition

$$
V(S,T) = (S - K)^+ = K(e^x - 1)^+
$$

In the similarity variable $\xi = x / (\sigma\sqrt{\tau})$:

$$
V(x,0) = K(e^{\sigma\sqrt{\tau}\,\xi} - 1)^+ \quad \text{at } \tau = 0
$$

### The Terminal Condition Is Not Self-Similar

As $\tau \to 0$, the payoff $(S - K)^+$ does not collapse to a function of $\xi$ alone. The terminal condition is not self-similar, which is another reason the naive similarity ansatz cannot capture the full solution.

### Resolution via Superposition

The full solution is a superposition over the self-similar fundamental solution:

$$
V(x,\tau) = \int_{-\infty}^{\infty}G(x-y,\tau)\,\Phi(y)\,dy
$$

where $G$ is the heat kernel. The self-similar kernel acts as the building block, even though the overall solution is not self-similar.

### Black-Scholes Formula

After transformation and integration:

$$
C(S,t) = SN(d_1) - Ke^{-r\tau}N(d_2)
$$

where $d_1, d_2$ are the modified similarity variables:

$$
d_1 = \frac{\ln(S/K) + (r + \frac{\sigma^2}{2})\tau}{\sigma\sqrt{\tau}}
$$

$$
d_2 = \frac{\ln(S/K) + (r - \frac{\sigma^2}{2})\tau}{\sigma\sqrt{\tau}} = d_1 - \sigma\sqrt{\tau}
$$

The structure $N(d_1), N(d_2)$ reflects the underlying similarity symmetry of the heat equation, adapted to account for the drift introduced by the interest rate.

---

## 8. Asymptotics and Similarity

### Short-Time Asymptotics

As $\tau \to 0$, the similarity variable $\xi = \ln(S/K) / (\sigma\sqrt{\tau})$ becomes:

- $\xi \to +\infty$ if $S > K$ (ITM)
- $\xi \to -\infty$ if $S < K$ (OTM)
- $\xi = O(1)$ if $S \approx K$ (ATM)

### ATM Expansion

For $S \approx K$ (so $\xi = O(1)$):

$$
V \approx K\left[N(d_1) - N(d_2)\right] \approx \frac{K\sigma\sqrt{\tau}}{\sqrt{2\pi}}\left[1 + O(\tau)\right]
$$

This is the **ATM approximation**: $V \sim \sigma\sqrt{\tau}$ (time-value decay).

### Deep OTM and ITM

For $|\xi| \gg 1$:

$$
N(d_i) \approx \begin{cases} 1 & d_i \to +\infty \\ 0 & d_i \to -\infty \end{cases}
$$

Using Mill's ratio:

$$
1 - N(x) \approx \frac{e^{-x^2/2}}{x\sqrt{2\pi}} \quad \text{for } x \gg 1
$$

This gives exponential decay in $\xi$: deep out-of-the-money options have prices that vanish exponentially in the squared similarity variable.

---

## 9. Connection to Probability Theory

### Central Limit Theorem

The heat kernel:

$$
G(x,\tau) = \frac{1}{\sqrt{4\pi\tau}}\,e^{-x^2/(4\tau)}
$$

is the Gaussian density with variance $2\tau$.

The similarity variable:

$$
\xi = \frac{x}{\sqrt{2\tau}}
$$

is the standardized variable for the CLT.

### Large Deviations

For $\tau \to \infty$ with $x/\tau = v$ fixed:

$$
-\frac{1}{\tau}\ln G(x,\tau) \approx \frac{v^2}{4} + \frac{1}{2}\ln(4\pi\tau)
$$

The rate function $I(v) = v^2/4$ governs large deviations.

### Scaling Limits

As $\tau \to 0$ with $\xi = x/\sqrt{\tau}$ fixed, the distribution concentrates on $\{\xi = 0\}$, i.e., $S = K$.

This is the zero-diffusion limit (small-noise asymptotics).

---

## 10. Summary

### Key Insights

1. **Black-Scholes is scale-invariant**: Multiply all dollar amounts by $\lambda$, and the solution scales proportionally.

2. **Natural similarity variable**: $\xi = \ln(S/K) / (\sigma\sqrt{\tau})$ is the standardized log-moneyness.

3. **The naive ansatz fails**: The interest rate $r$ introduces a scale that prevents a pure similarity reduction of the Black-Scholes PDE to a single ODE.

4. **Heat equation succeeds**: After removing drift and discounting, the transformed PDE admits an exact self-similar reduction whose fundamental solution is the Gaussian kernel.

5. **Black-Scholes formula as modified similarity**: The formula $C = SN(d_1) - Ke^{-r\tau}N(d_2)$ decomposes into two terms, each evaluated at a drift-adjusted similarity coordinate. The function $N$ arises from the ODE $h'' + \xi h' = 0$.

### The Similarity Perspective

Similarity solutions reveal that option prices depend on **ratios, not absolutes**:

- Not $S$ and $K$ separately, but $S/K$ (moneyness)
- Not $\tau$ and $\sigma$ separately, but $\sigma\sqrt{\tau}$ (total volatility)
- Not absolute prices, but dimensionless combinations

This is the geometric essence of the Black-Scholes pricing structure. In the operator framework of the introduction, similarity analysis reveals the **invariant structure** of the pricing semigroup $\mathcal{P}_\tau = e^{\tau\mathcal{L}}$: its action depends only on dimensionless combinations of the problem's parameters.

---

## Exercises

**Exercise 1.** Using the Buckingham Pi theorem, show that the Black-Scholes call price must have the form $C = K \cdot f(S/K, \sigma^2\tau, r\tau)$ for some dimensionless function $f$. Verify this by examining the Black-Scholes formula and identifying $f$ explicitly.

??? success "Solution to Exercise 1"

    The Black-Scholes call price depends on the dimensional quantities $S$, $K$, $\tau = T - t$, $\sigma$, and $r$. These involve two fundamental dimensions: currency $[\$]$ and time $[T]$.

    By the Buckingham Pi theorem, any physical law relating $n$ dimensional quantities with $m$ independent dimensions can be expressed in terms of $n - m$ dimensionless groups. Here $n = 6$ (including $C$) and $m = 2$, giving 4 dimensionless groups:

    $$
    \pi_1 = \frac{S}{K}, \quad \pi_2 = \sigma^2 \tau, \quad \pi_3 = r\tau, \quad \pi_4 = \frac{C}{K}
    $$

    The Buckingham Pi theorem requires $\pi_4 = f(\pi_1, \pi_2, \pi_3)$, i.e.,

    $$
    C = K \cdot f\!\left(\frac{S}{K},\, \sigma^2\tau,\, r\tau\right)
    $$

    Now verify with the Black-Scholes formula $C = S\mathcal{N}(d_1) - Ke^{-r\tau}\mathcal{N}(d_2)$. Dividing by $K$:

    $$
    \frac{C}{K} = \frac{S}{K}\mathcal{N}(d_1) - e^{-r\tau}\mathcal{N}(d_2)
    $$

    The arguments $d_1$ and $d_2$ are

    $$
    d_1 = \frac{\ln(S/K) + (r + \sigma^2/2)\tau}{\sigma\sqrt{\tau}}, \quad d_2 = d_1 - \sigma\sqrt{\tau}
    $$

    Both depend only on $S/K$, $\sigma^2\tau$, and $r\tau$. Therefore the dimensionless function is

    $$
    f(x, v, \rho) = x\,\mathcal{N}\!\left(\frac{\ln x + \rho + v/2}{\sqrt{v}}\right) - e^{-\rho}\,\mathcal{N}\!\left(\frac{\ln x + \rho - v/2}{\sqrt{v}}\right)
    $$

    where $x = S/K$, $v = \sigma^2\tau$, $\rho = r\tau$, confirming the Buckingham Pi prediction exactly.

---
**Exercise 2.** The similarity variable for the heat equation is $\xi = x / \sqrt{\tau}$. Show that if $F(x, \tau) = g(\xi)$, then substituting into $\frac{\partial F}{\partial \tau} = \frac{1}{2}\sigma^2 \frac{\partial^2 F}{\partial x^2}$ yields the ODE $-\frac{\xi}{2}g'(\xi) = \frac{\sigma^2}{2}g''(\xi)$. Solve this ODE and relate the solution to the error function.

??? success "Solution to Exercise 2"

    Let $\xi = x / \sqrt{\tau}$ and assume $F(x, \tau) = g(\xi)$. We compute the partial derivatives using the chain rule. Since $\xi = x\tau^{-1/2}$:

    $$
    \frac{\partial \xi}{\partial \tau} = -\frac{x}{2\tau^{3/2}} = -\frac{\xi}{2\tau}, \quad \frac{\partial \xi}{\partial x} = \frac{1}{\sqrt{\tau}}
    $$

    Therefore:

    $$
    \frac{\partial F}{\partial \tau} = g'(\xi)\cdot\left(-\frac{\xi}{2\tau}\right)
    $$

    $$
    \frac{\partial F}{\partial x} = g'(\xi)\cdot\frac{1}{\sqrt{\tau}}, \quad \frac{\partial^2 F}{\partial x^2} = g''(\xi)\cdot\frac{1}{\tau}
    $$

    Substituting into $\frac{\partial F}{\partial \tau} = \frac{1}{2}\sigma^2\frac{\partial^2 F}{\partial x^2}$:

    $$
    -\frac{\xi}{2\tau}g'(\xi) = \frac{\sigma^2}{2\tau}g''(\xi)
    $$

    Multiplying both sides by $\tau$ yields:

    $$
    -\frac{\xi}{2}g'(\xi) = \frac{\sigma^2}{2}g''(\xi)
    $$

    For the standard heat equation with $\sigma = 1$, this becomes $g'' + \xi g' = 0$. To solve, let $h = g'$:

    $$
    h' + \xi h = 0 \implies h(\xi) = A e^{-\xi^2/2}
    $$

    Integrating:

    $$
    g(\xi) = A\int_0^{\xi} e^{-s^2/2}\,ds + B = A\sqrt{\frac{\pi}{2}}\,\mathrm{erf}\!\left(\frac{\xi}{\sqrt{2}}\right) + B
    $$

    For general $\sigma$, the substitution $\eta = \xi/\sigma$ gives $g(\xi) = A\,\mathrm{erf}\!\left(\frac{\xi}{\sigma\sqrt{2}}\right) + B$. This is precisely the **error function** solution. The fundamental solution of the heat equation, $\frac{1}{\sigma\sqrt{2\pi\tau}}e^{-x^2/(2\sigma^2\tau)}$, is recovered by differentiating $g$ with respect to $x$, confirming that the Gaussian kernel arises naturally from the similarity reduction.

---
**Exercise 3.** The Black-Scholes formula depends on $S$ and $K$ only through the ratio $S/K$ (moneyness). Explain this using the scale invariance of GBM: if $S_t$ satisfies the GBM SDE, show that $\lambda S_t$ also satisfies the same SDE with the same $\mu$ and $\sigma$, and conclude that the call price must be homogeneous of degree 1 in $(S, K)$.

??? success "Solution to Exercise 3"

    Let $S_t$ satisfy the GBM SDE under the risk-neutral measure:

    $$
    dS_t = rS_t\,dt + \sigma S_t\,dW_t
    $$

    For any constant $\lambda > 0$, define $\tilde{S}_t = \lambda S_t$. Then:

    $$
    d\tilde{S}_t = \lambda\,dS_t = r(\lambda S_t)\,dt + \sigma(\lambda S_t)\,dW_t = r\tilde{S}_t\,dt + \sigma\tilde{S}_t\,dW_t
    $$

    So $\tilde{S}_t$ satisfies the same GBM SDE with the same drift $r$ and volatility $\sigma$, confirming scale invariance.

    Now consider the European call price $C(S, K, \tau) = e^{-r\tau}\mathbb{E}[(S_T - K)^+]$. For any $\lambda > 0$:

    $$
    C(\lambda S, \lambda K, \tau) = e^{-r\tau}\mathbb{E}[(\lambda S_T - \lambda K)^+] = \lambda\, e^{-r\tau}\mathbb{E}[(S_T - K)^+] = \lambda\, C(S, K, \tau)
    $$

    where we used the fact that $\lambda S_T$ has the same distribution as $S_T$ starting from $\lambda S$ (by scale invariance of GBM), and homogeneity of the payoff.

    This shows $C$ is **homogeneous of degree 1** in $(S, K)$: $C(\lambda S, \lambda K, \tau) = \lambda C(S, K, \tau)$. Setting $\lambda = 1/K$:

    $$
    C(S, K, \tau) = K \cdot C\!\left(\frac{S}{K}, 1, \tau\right)
    $$

    Therefore $C$ depends on $S$ and $K$ only through the moneyness ratio $S/K$. This is a direct consequence of the scale invariance of the underlying GBM dynamics.

---
**Exercise 4.** Show that the Black-Scholes call price satisfies Euler's identity for homogeneous functions: $C = S\frac{\partial C}{\partial S} + K\frac{\partial C}{\partial K}$. Verify this directly using the Black-Scholes formula.

??? success "Solution to Exercise 4"

    Euler's theorem states that if $f$ is homogeneous of degree $k$, then $\sum_i x_i \frac{\partial f}{\partial x_i} = k f$. From Exercise 3, $C(S, K, \tau)$ is homogeneous of degree 1 in $(S, K)$, so:

    $$
    S\frac{\partial C}{\partial S} + K\frac{\partial C}{\partial K} = C
    $$

    We verify directly using the Black-Scholes formula $C = S\mathcal{N}(d_1) - Ke^{-r\tau}\mathcal{N}(d_2)$.

    **Step 1**: Compute $\frac{\partial C}{\partial S}$. Note that $\frac{\partial d_1}{\partial S} = \frac{\partial d_2}{\partial S} = \frac{1}{S\sigma\sqrt{\tau}}$. Then:

    $$
    \frac{\partial C}{\partial S} = \mathcal{N}(d_1) + S\mathcal{N}'(d_1)\frac{1}{S\sigma\sqrt{\tau}} - Ke^{-r\tau}\mathcal{N}'(d_2)\frac{1}{S\sigma\sqrt{\tau}}
    $$

    Using the identity $S\mathcal{N}'(d_1) = Ke^{-r\tau}\mathcal{N}'(d_2)$ (which follows from $d_1 - d_2 = \sigma\sqrt{\tau}$ and the log-normal relationship), the last two terms cancel:

    $$
    \frac{\partial C}{\partial S} = \mathcal{N}(d_1) = \Delta
    $$

    **Step 2**: Compute $\frac{\partial C}{\partial K}$. Since $\frac{\partial d_1}{\partial K} = \frac{\partial d_2}{\partial K} = -\frac{1}{K\sigma\sqrt{\tau}}$:

    $$
    \frac{\partial C}{\partial K} = S\mathcal{N}'(d_1)\!\left(-\frac{1}{K\sigma\sqrt{\tau}}\right) - e^{-r\tau}\mathcal{N}(d_2) - Ke^{-r\tau}\mathcal{N}'(d_2)\!\left(-\frac{1}{K\sigma\sqrt{\tau}}\right)
    $$

    Again using $S\mathcal{N}'(d_1) = Ke^{-r\tau}\mathcal{N}'(d_2)$, the first and third terms cancel:

    $$
    \frac{\partial C}{\partial K} = -e^{-r\tau}\mathcal{N}(d_2)
    $$

    **Step 3**: Verify Euler's identity:

    $$
    S\frac{\partial C}{\partial S} + K\frac{\partial C}{\partial K} = S\mathcal{N}(d_1) - Ke^{-r\tau}\mathcal{N}(d_2) = C
    $$

    This confirms Euler's identity for the degree-1 homogeneous Black-Scholes call price. $\square$

---
**Exercise 5.** The ATM approximation $C \approx 0.4\, S\sigma\sqrt{T}$ can be understood as a similarity scaling. Show that for $S = K$ and $r = 0$, the call price depends on $S$, $\sigma$, and $T$ only through the combination $S\sigma\sqrt{T}$, and determine the proportionality constant from the Black-Scholes formula.

??? success "Solution to Exercise 5"

    Set $S = K$ (ATM) and $r = 0$. The Black-Scholes formula becomes:

    $$
    C = S\mathcal{N}(d_1) - S\mathcal{N}(d_2)
    $$

    where $d_1 = \frac{\sigma\sqrt{T}}{2}$ and $d_2 = -\frac{\sigma\sqrt{T}}{2}$.

    By symmetry of the normal distribution, $\mathcal{N}(-x) = 1 - \mathcal{N}(x)$, so:

    $$
    C = S\mathcal{N}(d_1) - S(1 - \mathcal{N}(d_1)) = S(2\mathcal{N}(d_1) - 1)
    $$

    **Dimensional analysis**: With $r = 0$ and $S = K$, the only remaining dimensional quantities are $S$ $[\$]$, $\sigma$ $[T^{-1/2}]$, and $T$ $[T]$. The unique dimensionless combination from $\sigma$ and $T$ is $\sigma\sqrt{T}$, so $C$ must have the form:

    $$
    C = S \cdot \psi(\sigma\sqrt{T})
    $$

    where $\psi(z) = 2\mathcal{N}(z/2) - 1$.

    **Proportionality constant**: For small $z = \sigma\sqrt{T}$, expand $\mathcal{N}(z/2)$ using $\mathcal{N}(x) \approx \frac{1}{2} + \frac{x}{\sqrt{2\pi}}$ for small $x$:

    $$
    C \approx S\left(2\left(\frac{1}{2} + \frac{\sigma\sqrt{T}}{2\sqrt{2\pi}}\right) - 1\right) = S\cdot\frac{\sigma\sqrt{T}}{\sqrt{2\pi}}
    $$

    Since $\frac{1}{\sqrt{2\pi}} \approx 0.3989 \approx 0.4$:

    $$
    C \approx 0.4\, S\sigma\sqrt{T}
    $$

    This confirms the ATM approximation as a similarity scaling result, with the proportionality constant being exactly $1/\sqrt{2\pi}$. $\square$
