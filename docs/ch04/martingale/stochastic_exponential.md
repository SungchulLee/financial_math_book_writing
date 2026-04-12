# The Stochastic Exponential

In the [unifying framework](unifying_principle.md) of this section, the stochastic exponential is the **transformation enabling control** — it converts additive local martingales into multiplicative densities for measure change.

The **stochastic exponential** (or **Doléans-Dade exponential**) is the stochastic analogue of the ordinary exponential function. It is the fundamental tool for constructing Radon–Nikodym derivatives in measure change, and therefore central to Girsanov's theorem and risk-neutral pricing.

!!! info "Prerequisites"
    This section assumes familiarity with:
    
    - [Itô's Lemma](../../ch03/ito_lemma/ito_lemma.md)
    - [Quadratic Variation](../../ch03/ito_integral/quadratic_variation.md)
    - [Local Martingales](local_martingale.md)

---

## Definition

### SDE Definition

For a general semimartingale $X_t$ adapted to a filtration $\{\mathcal{F}_t\}$, the **stochastic exponential** $\mathcal{E}(X)_t$ is the unique solution to:

$$
\boxed{
d\mathcal{E}(X)_t = \mathcal{E}(X)_{t-}\,dX_t, \quad \mathcal{E}(X)_0 = 1
}
$$

Here $\mathcal{E}(X)_{t-} = \lim_{s \uparrow t}\mathcal{E}(X)_s$ denotes the **left limit**, which is needed because $X$ may have jumps and the integrand in a stochastic integral must be **predictable** (known just before time $t$).

In the **continuous case**, left and right limits coincide ($\mathcal{E}(X)_{t-} = \mathcal{E}(X)_t$), so the SDE simplifies to:

$$
\boxed{
d\mathcal{E}(X)_t = \mathcal{E}(X)_t\,dX_t, \quad \mathcal{E}(X)_0 = 1
}
$$

Note that the initial condition is always $\mathcal{E}(X)_0 = 1$, regardless of the value of $X_0$.

### Explicit Formula

For **continuous** semimartingales, the stochastic exponential has a clean closed form:

$$
\boxed{
\mathcal{E}(X)_t = \exp\left(X_t - X_0 - \frac{1}{2}\langle X \rangle_t\right)
}
$$

where $\langle X \rangle_t$ is the **quadratic variation** of $X$. When $X_0 = 0$ (the most common case in applications), this simplifies to:

$$
\mathcal{E}(X)_t = \exp\left(X_t - \frac{1}{2}\langle X \rangle_t\right)
$$

For a **general** semimartingale with jumps $\Delta X_s = X_s - X_{s-}$, the formula becomes:

$$
\mathcal{E}(X)_t = \exp\!\left(X_t - X_0 - \frac{1}{2}\langle X^c \rangle_t\right) \prod_{0 < s \leq t}(1 + \Delta X_s)\,e^{-\Delta X_s}
$$

where $X^c$ is the continuous martingale part of $X$. Each jump contributes a multiplicative factor $(1 + \Delta X_s)\,e^{-\Delta X_s}$, which reduces to 1 when there are no jumps, recovering the continuous formula. For $\mathcal{E}(X)_t$ to remain positive, one needs $\Delta X_s > -1$ for all $s$.

In most financial applications, $X_t$ will be a **continuous local martingale**, in which case the jump terms vanish and the exponential admits the simplified closed form. The discussion below primarily focuses on this continuous setting unless otherwise stated.

---

## Why "Stochastic Exponential"?

### Analogy with Ordinary Exponential

For a deterministic function $x(t)$, the ordinary exponential $e^{x(t)}$ satisfies:

$$
\frac{d}{dt}e^{x(t)} = e^{x(t)} \cdot \frac{dx(t)}{dt}
$$

In differential form: $d(e^{x}) = e^x\,dx$.

### The Stochastic Version

The stochastic exponential satisfies the same multiplicative structure:

$$
d\mathcal{E}(X)_t = \mathcal{E}(X)_t\,dX_t
$$

### The Crucial Difference

In ordinary calculus: $e^{x(t)} = \exp\left(\int_0^t dx(s)\right) = \exp(x(t) - x(0))$

In stochastic calculus: $\mathcal{E}(X)_t = \exp\left(X_t - X_0 - \frac{1}{2}\langle X \rangle_t\right)$

The term $-\frac{1}{2}\langle X \rangle_t$ is the **Itô correction** arising from quadratic variation. This correction is essential: without it, the exponential would have a drift term and fail to be a local martingale.

---

## Derivation via Itô's Lemma

**Goal**: Verify that $Z_t = \exp(X_t - X_0 - \frac{1}{2}\langle X \rangle_t)$ satisfies $dZ_t = Z_t\,dX_t$.

### Setup

Let $X_t$ be a continuous local martingale with $dX_t = \sigma_t\,dW_t$. Then $d\langle X \rangle_t = \sigma_t^2\,dt$.

Define $Z_t = \exp(X_t - X_0 - \frac{1}{2}\langle X \rangle_t)$.

### Apply Itô's Lemma

Using the Itô formula with $f(x) = e^x$ and the process $Y_t = X_t - X_0 - \frac{1}{2}\langle X \rangle_t$:

$$
dZ_t = Z_t\,dY_t + \frac{1}{2}Z_t\,(dY_t)^2
$$

Now compute $dY_t$ and $(dY_t)^2$:

$$
dY_t = dX_t - \frac{1}{2}d\langle X \rangle_t = \sigma_t\,dW_t - \frac{1}{2}\sigma_t^2\,dt
$$

$$
(dY_t)^2 = (\sigma_t\,dW_t)^2 = \sigma_t^2\,dt = d\langle X \rangle_t
$$

(using the Itô multiplication rules: $(dW_t)^2 = dt$, $dt \cdot dW_t = 0$, $(dt)^2 = 0$)

### Substitute

$$\begin{array}{lll}
dZ_t 
&=&\displaystyle Z_t\left(\sigma_t\,dW_t - \frac{1}{2}\sigma_t^2\,dt\right) + \frac{1}{2}Z_t \cdot \sigma_t^2\,dt\\
&=&\displaystyle Z_t\,\sigma_t\,dW_t - \frac{1}{2}Z_t\,\sigma_t^2\,dt + \frac{1}{2}Z_t\,\sigma_t^2\,dt\\
&=&\displaystyle Z_t\,\sigma_t\,dW_t\\
&=&\displaystyle Z_t\,dX_t
\end{array}$$

The correction terms **cancel exactly**, leaving no drift. $\square$

---

## Key Properties

### Property 1: Positivity

$$
\mathcal{E}(X)_t > 0 \quad \text{for all } t \geq 0
$$

The stochastic exponential is always strictly positive (exponential of a real number).

### Property 2: Local Martingale Property

If $X_t$ is a local martingale, then $\mathcal{E}(X)_t$ is also a **local martingale**.

**Proof**: From $d\mathcal{E}(X)_t = \mathcal{E}(X)_t\,dX_t$, we see there is no $dt$ term—the SDE has zero drift. $\square$

### Property 3: Multiplication Rule

For two continuous semimartingales $X$ and $Y$:

$$
\boxed{\mathcal{E}(X)_t \cdot \mathcal{E}(Y)_t = \mathcal{E}(X + Y + \langle X, Y \rangle)_t}
$$

Compare to the ordinary rule: $e^x \cdot e^y = e^{x+y}$. The stochastic version has an extra covariation term.

**Proof**: Let $Z_t = \mathcal{E}(X)_t$ and $W_t = \mathcal{E}(Y)_t$. By the Itô product rule:

$$
d(ZW) = Z\,dW + W\,dZ + d\langle Z, W \rangle
$$

Since $dZ = Z\,dX$ and $dW = W\,dY$:

$$
d(ZW) = ZW\,dY + ZW\,dX + ZW\,d\langle X, Y \rangle = ZW\,(dX + dY + d\langle X, Y \rangle)
$$

This shows $ZW = \mathcal{E}(X)\mathcal{E}(Y)$ satisfies the SDE for $\mathcal{E}(X + Y + \langle X, Y \rangle)$. $\square$

### Property 4: Reciprocal

The reciprocal of a stochastic exponential is:

$$
\boxed{\frac{1}{\mathcal{E}(X)_t} = \exp\left(-X_t + X_0 + \frac{1}{2}\langle X \rangle_t\right)}
$$

Importantly, the reciprocal is **not** generally itself a stochastic exponential of the form $\mathcal{E}(Y)$ for some simple process $Y = -X$. We have:

$$
\frac{1}{\mathcal{E}(X)_t} = \mathcal{E}(-X)_t \cdot \exp(\langle X \rangle_t)
$$

This distinction is important in measure-change arguments, where reciprocal densities do not automatically retain martingale properties. In particular, the inverse density $1/Z_T$ that appears when reversing a measure change is not a stochastic exponential in the simple sense, and its status as a true martingale must be verified separately.

This follows from direct computation:

$$
\mathcal{E}(-X)_t = \exp\left(-X_t + X_0 - \frac{1}{2}\langle X \rangle_t\right)
$$

so

$$
\mathcal{E}(-X)_t \cdot \exp(\langle X \rangle_t) = \exp\left(-X_t + X_0 + \frac{1}{2}\langle X \rangle_t\right) = \frac{1}{\mathcal{E}(X)_t}
$$

### Property 5: Unit Expectation (Under Conditions)

If $\mathcal{E}(X)$ is a **true martingale** (not just a local martingale):

$$
\mathbb{E}[\mathcal{E}(X)_t] = \mathcal{E}(X)_0 = 1
$$

This property is essential for measure changes but requires verification via Novikov or Kazamaki conditions.

---

## Special Cases

### Case 1: X_t = σ W_t (Constant Volatility)

For $\sigma \in \mathbb{R}$ constant:

$$
\mathcal{E}(\sigma W)_t = \exp\left(\sigma W_t - \frac{\sigma^2 t}{2}\right)
$$

This is the fundamental **exponential martingale**. It satisfies $\mathbb{E}[\mathcal{E}(\sigma W)_t] = 1$ for all $t$ (Novikov is trivially satisfied since $\sigma$ is constant).

### Case 2: X_t = ∫_0^t σ_s dW_s (Stochastic Integrand)

$$
\mathcal{E}(X)_t = \exp\left(\int_0^t \sigma_s\,dW_s - \frac{1}{2}\int_0^t \sigma_s^2\,ds\right)
$$

This is the general form used in Girsanov's theorem. Whether it's a true martingale depends on $\sigma$—see [Novikov and Kazamaki Conditions](novikov_kazamaki_conditions.md).

### Case 3: Geometric Brownian Motion

The solution to $dS_t = \mu S_t\,dt + \sigma S_t\,dW_t$ with $S_0 > 0$ is:

$$
S_t = S_0 \exp\left(\left(\mu - \frac{\sigma^2}{2}\right)t + \sigma W_t\right)
$$

This can be written as:

$$
S_t = S_0\, e^{\mu t} \cdot \mathcal{E}(\sigma W)_t
$$

The term $\mu - \frac{\sigma^2}{2}$ is the **drift-adjusted growth rate**—the Itô correction $-\frac{\sigma^2}{2}$ appears naturally.

---

## Connection to Girsanov's Theorem

The stochastic exponential is the **Radon–Nikodym derivative** for measure change.

### Measure Change Setup

To change from measure $\mathbb{P}$ to measure $\mathbb{Q}$:

$$
\frac{d\mathbb{Q}}{d\mathbb{P}}\bigg|_{\mathcal{F}_T} = Z_T
$$

where the **density process** is:

$$
Z_t = \mathcal{E}\left(\int_0^\cdot \theta_s\,dW_s\right)_t = \exp\left(\int_0^t \theta_s\,dW_s - \frac{1}{2}\int_0^t \theta_s^2\,ds\right)
$$

Here $\theta_t$ is the **Girsanov kernel** (market price of risk in finance).

### Girsanov's Result

Under $\mathbb{Q}$, the process:

$$
\tilde{W}_t = W_t - \int_0^t \theta_s\,ds
$$

is a standard Brownian motion.

**Validity**: For this measure change to be valid (i.e., $\mathbb{Q}$ is a probability measure equivalent to $\mathbb{P}$), we need $Z_t$ to be a **true martingale** with $\mathbb{E}^{\mathbb{P}}[Z_T] = 1$. This is guaranteed by Novikov's or Kazamaki's condition.

See [Girsanov's Theorem](../girsanov/girsanov_theorem.md) for the complete treatment.

---

## Why the Correction Term Matters

### Without Correction: e^W_t Has Drift

If we naively define $Z_t = e^{W_t}$, then by Itô's lemma:

$$
dZ_t = e^{W_t}dW_t + \frac{1}{2}e^{W_t}dt = Z_t\,dW_t + \frac{1}{2}Z_t\,dt
$$

This has a **positive drift term** $\frac{1}{2}Z_t\,dt$. The process $e^{W_t}$ is a **submartingale**, not a martingale:

$$
\mathbb{E}[e^{W_t}] = e^{t/2} > 1 = e^{W_0}
$$

### With Correction: E(W)_t Is a Martingale

$$
\mathcal{E}(W)_t = e^{W_t - t/2}
$$

Then:

$$
d\mathcal{E}(W)_t = \mathcal{E}(W)_t\,dW_t
$$

**No drift term**—this is a true martingale with $\mathbb{E}[\mathcal{E}(W)_t] = 1$.

The correction $-\frac{1}{2}\langle X \rangle_t$ precisely removes the drift introduced by Itô's lemma.

---

## When Is E(X) a True Martingale?

The stochastic exponential of a local martingale is always a local martingale, but may be a **strict local martingale** (local martingale that is not a true martingale).

### Sufficient Conditions

**Novikov's Condition**: If

$$
\mathbb{E}\left[\exp\left(\frac{1}{2}\langle X \rangle_T\right)\right] < \infty
$$

then $\mathcal{E}(X)$ is a true martingale on $[0,T]$.

**Kazamaki's Condition** (weaker): If $\mathcal{E}(X/2)$ is a submartingale, then $\mathcal{E}(X)$ is a true martingale.

For details and proofs, see [Novikov and Kazamaki Conditions](novikov_kazamaki_conditions.md).

### When Conditions Fail

If neither condition holds, $\mathcal{E}(X)$ may satisfy $\mathbb{E}[\mathcal{E}(X)_T] < 1$. In finance, this corresponds to **asset price bubbles**. See [Local Martingales](local_martingale.md) for examples.

---

## Applications in Finance

### 1. Risk-Neutral Measure Construction

The density process for the risk-neutral measure $\mathbb{Q}$:

$$
Z_t = \mathcal{E}\left(-\int_0^\cdot \frac{\mu - r}{\sigma}\,dW_s\right)_t
$$

where $(\mu - r)/\sigma$ is the **market price of risk** (Sharpe ratio).

### 2. Change of Numéraire

When changing from numéraire $M$ to numéraire $N$:

$$
\frac{d\mathbb{Q}^N}{d\mathbb{Q}^M}\bigg|_{\mathcal{F}_T} = \frac{N_T/N_0}{M_T/M_0}
$$

This ratio involves stochastic exponentials of the volatility difference between the two numéraires.

### 3. Forward Measure

The $T$-forward measure uses the zero-coupon bond $P(t,T)$ as numéraire. The density involves stochastic exponentials of bond volatilities.

See [Forward Measure](../risk_neutral/forward_measure.md) for details.

---

## Summary

$$
\boxed{
\mathcal{E}(X)_t = \exp\left(X_t - X_0 - \frac{1}{2}\langle X \rangle_t\right)
}
$$

| Property | Statement |
|----------|-----------|
| **Definition** | Unique solution to $d\mathcal{E} = \mathcal{E}\,dX$, $\mathcal{E}_0 = 1$ |
| **Positivity** | $\mathcal{E}(X)_t > 0$ always |
| **Local martingale** | If $X$ is a continuous local martingale, so is $\mathcal{E}(X)$ |
| **Multiplication** | $\mathcal{E}(X)\mathcal{E}(Y) = \mathcal{E}(X + Y + \langle X,Y\rangle)$ |
| **True martingale** | Requires Novikov or Kazamaki condition |
| **Finance application** | Radon–Nikodym derivative for measure change |

!!! summary "Key Takeaway"
    The stochastic exponential is the "correct" way to exponentiate stochastic processes, accounting for the Itô correction term $-\frac{1}{2}\langle X \rangle_t$. This correction removes the drift that would otherwise arise, making $\mathcal{E}(X)$ a local martingale. The stochastic exponential is essential for all measure-change arguments in mathematical finance.

---

## Exercises

**Exercise 1.**
Compute the stochastic exponential $\mathcal{E}(\sigma W)_t$ explicitly for $\sigma = 2$. Verify that $\mathbb{E}[\mathcal{E}(2W)_t] = 1$ using the moment generating function of the normal distribution. What is $\mathrm{Var}(\mathcal{E}(2W)_t)$?

??? success "Solution to Exercise 1"
    For $\sigma = 2$:

    $$
    \mathcal{E}(2W)_t = \exp\left(2W_t - \frac{4t}{2}\right) = \exp(2W_t - 2t)
    $$

    To verify $\mathbb{E}[\mathcal{E}(2W)_t] = 1$: since $W_t \sim N(0, t)$, we have $2W_t \sim N(0, 4t)$. Using the MGF of a normal, $\mathbb{E}[e^{aW_t}] = e^{a^2 t/2}$:

    $$
    \mathbb{E}[\mathcal{E}(2W)_t] = \mathbb{E}[e^{2W_t - 2t}] = e^{-2t}\mathbb{E}[e^{2W_t}] = e^{-2t} \cdot e^{4t/2} = e^{-2t} \cdot e^{2t} = 1
    $$

    For the variance, first compute $\mathbb{E}[\mathcal{E}(2W)_t^2]$:

    $$
    \mathbb{E}[\mathcal{E}(2W)_t^2] = \mathbb{E}[e^{4W_t - 4t}] = e^{-4t}\mathbb{E}[e^{4W_t}] = e^{-4t} \cdot e^{16t/2} = e^{-4t} \cdot e^{8t} = e^{4t}
    $$

    Therefore:

    $$
    \mathrm{Var}(\mathcal{E}(2W)_t) = \mathbb{E}[\mathcal{E}(2W)_t^2] - (\mathbb{E}[\mathcal{E}(2W)_t])^2 = e^{4t} - 1
    $$

---

**Exercise 2.**
Let $X_t = \int_0^t \sigma_s\,dW_s$ with $\sigma_s = s$. Write the explicit formula for $\mathcal{E}(X)_t$ and compute its quadratic variation $\langle \mathcal{E}(X) \rangle_t$. Verify Novikov's condition for finite $T$ and conclude that $\mathcal{E}(X)$ is a true martingale on $[0, T]$.

??? success "Solution to Exercise 2"
    With $X_t = \int_0^t s\,dW_s$, the quadratic variation is:

    $$
    \langle X \rangle_t = \int_0^t s^2\,ds = \frac{t^3}{3}
    $$

    The stochastic exponential is:

    $$
    \mathcal{E}(X)_t = \exp\left(\int_0^t s\,dW_s - \frac{t^3}{6}\right)
    $$

    The quadratic variation of $\mathcal{E}(X)$ is computed from $d\mathcal{E}(X)_t = \mathcal{E}(X)_t\,dX_t = \mathcal{E}(X)_t \cdot t\,dW_t$:

    $$
    \langle \mathcal{E}(X) \rangle_t = \int_0^t \mathcal{E}(X)_s^2 \cdot s^2\,ds
    $$

    **Novikov verification**: For finite $T$:

    $$
    \mathbb{E}\left[\exp\left(\frac{1}{2}\langle X \rangle_T\right)\right] = \exp\left(\frac{T^3}{6}\right) < \infty
    $$

    Since $\sigma_s = s$ is deterministic, $\langle X \rangle_T = T^3/3$ is deterministic, and the exponential moment is trivially finite. By Novikov's theorem, $\mathcal{E}(X)$ is a true martingale on $[0, T]$ for any finite $T$.

---

**Exercise 3.**
Apply Itô's lemma to $Z_t = e^{W_t}$ (without the correction) and show that $dZ_t = Z_t\,dW_t + \frac{1}{2}Z_t\,dt$. Then apply Itô's lemma to $\mathcal{E}(W)_t = e^{W_t - t/2}$ and show that the $dt$ term vanishes. Explain why the Itô correction $-\frac{1}{2}\langle W \rangle_t = -t/2$ is exactly what is needed to remove the drift.

??? success "Solution to Exercise 3"
    **Without correction**: Let $Z_t = e^{W_t}$. By Itô's lemma with $f(x) = e^x$:

    $$
    dZ_t = f'(W_t)\,dW_t + \frac{1}{2}f''(W_t)\,dt = e^{W_t}\,dW_t + \frac{1}{2}e^{W_t}\,dt = Z_t\,dW_t + \frac{1}{2}Z_t\,dt
    $$

    The $\frac{1}{2}Z_t\,dt$ drift makes $Z_t$ a submartingale (systematically increasing in expectation).

    **With correction**: Let $\mathcal{E}(W)_t = e^{W_t - t/2}$. Define $Y_t = W_t - t/2$, so $\mathcal{E}(W)_t = e^{Y_t}$. By Itô's lemma:

    $$
    d\mathcal{E}(W)_t = e^{Y_t}\,dY_t + \frac{1}{2}e^{Y_t}(dY_t)^2
    $$

    Now $dY_t = dW_t - \frac{1}{2}\,dt$ and $(dY_t)^2 = (dW_t)^2 = dt$. Substituting:

    $$
    d\mathcal{E}(W)_t = e^{Y_t}\left(dW_t - \frac{1}{2}\,dt\right) + \frac{1}{2}e^{Y_t}\,dt = e^{Y_t}\,dW_t - \frac{1}{2}e^{Y_t}\,dt + \frac{1}{2}e^{Y_t}\,dt = \mathcal{E}(W)_t\,dW_t
    $$

    The $dt$ terms cancel exactly. The Itô correction $-\frac{1}{2}\langle W \rangle_t = -t/2$ compensates precisely for the second-order term $\frac{1}{2}f''(W_t)\,dt$ in Itô's formula, removing the drift and producing a martingale.

---

**Exercise 4.**
Prove the multiplication rule $\mathcal{E}(X)_t \cdot \mathcal{E}(Y)_t = \mathcal{E}(X + Y + \langle X, Y \rangle)_t$ by applying the Itô product rule to $Z_t = \mathcal{E}(X)_t$ and $U_t = \mathcal{E}(Y)_t$. Identify where the covariation term $\langle X, Y \rangle$ enters.

??? success "Solution to Exercise 4"
    Let $Z_t = \mathcal{E}(X)_t$ and $U_t = \mathcal{E}(Y)_t$. By the Itô product rule:

    $$
    d(Z_t U_t) = Z_t\,dU_t + U_t\,dZ_t + d\langle Z, U \rangle_t
    $$

    Since $dZ_t = Z_t\,dX_t$ and $dU_t = U_t\,dY_t$:

    $$
    d(Z_t U_t) = Z_t U_t\,dY_t + U_t Z_t\,dX_t + d\langle Z, U \rangle_t
    $$

    For the covariation: $d\langle Z, U \rangle_t = Z_t U_t\,d\langle X, Y \rangle_t$ (since the diffusion coefficients of $Z$ and $U$ are $Z_t$ times $dX_t$ and $U_t$ times $dY_t$).

    Therefore:

    $$
    d(Z_t U_t) = Z_t U_t\,(dX_t + dY_t + d\langle X, Y \rangle_t)
    $$

    This means $Z_t U_t$ solves the SDE $d\mathcal{E} = \mathcal{E}\,d(X + Y + \langle X, Y \rangle)$ with initial condition $Z_0 U_0 = 1$. By uniqueness of the stochastic exponential SDE:

    $$
    \mathcal{E}(X)_t \cdot \mathcal{E}(Y)_t = \mathcal{E}(X + Y + \langle X, Y \rangle)_t
    $$

    The covariation $\langle X, Y \rangle$ enters through the cross-term $d\langle Z, U \rangle_t$ in the Itô product rule — this is the stochastic calculus analogue of the fact that the product of two exponentials involves the sum of exponents, but with an additional correction from quadratic covariation.

---

**Exercise 5.**
In the Black-Scholes model, the stock price is $S_t = S_0 e^{(\mu - \sigma^2/2)t + \sigma W_t} = S_0 e^{\mu t} \mathcal{E}(\sigma W)_t$. Show that the discounted price $e^{-rt}S_t$ can be written as $S_0 e^{(\mu - r)t}\mathcal{E}(\sigma W)_t$ and explain why this is a martingale under $\mathbb{Q}$ but not under $\mathbb{P}$ (unless $\mu = r$).

??? success "Solution to Exercise 5"
    The stock price is $S_t = S_0 e^{(\mu - \sigma^2/2)t + \sigma W_t} = S_0 e^{\mu t}\mathcal{E}(\sigma W)_t$. The discounted price is:

    $$
    e^{-rt}S_t = S_0 e^{(\mu - r)t}\mathcal{E}(\sigma W)_t
    $$

    Under $\mathbb{P}$: The factor $e^{(\mu - r)t}$ introduces a deterministic drift. Since $\mathcal{E}(\sigma W)_t$ is a $\mathbb{P}$-martingale with $\mathbb{E}^{\mathbb{P}}[\mathcal{E}(\sigma W)_t] = 1$:

    $$
    \mathbb{E}^{\mathbb{P}}[e^{-rt}S_t] = S_0 e^{(\mu - r)t} \neq S_0 \quad (\text{unless } \mu = r)
    $$

    So $e^{-rt}S_t$ is not a $\mathbb{P}$-martingale when $\mu \neq r$.

    Under $\mathbb{Q}$: Girsanov's theorem replaces $W_t$ by $W_t^{\mathbb{Q}} - \frac{\mu - r}{\sigma}t$, so $\sigma W_t = \sigma W_t^{\mathbb{Q}} - (\mu - r)t$. Then:

    $$
    e^{-rt}S_t = S_0 e^{(\mu - r)t}\exp\left(\sigma W_t^{\mathbb{Q}} - (\mu - r)t - \frac{\sigma^2 t}{2}\right) = S_0\mathcal{E}(\sigma W^{\mathbb{Q}})_t
    $$

    The factor $e^{(\mu-r)t}$ cancels with $e^{-(\mu-r)t}$ from the Girsanov shift, and the discounted price becomes $S_0\mathcal{E}(\sigma W^{\mathbb{Q}})_t$, which is a $\mathbb{Q}$-martingale with unit expectation.

---

**Exercise 6.**
For the Radon–Nikodym derivative $Z_t = \mathcal{E}(-\int_0^{\cdot}\theta_s\,dW_s)_t$, show that $1/Z_t$ is not equal to $\mathcal{E}(\int_0^{\cdot}\theta_s\,dW_s)_t$ in general. Compute the ratio explicitly and identify the extra multiplicative factor involving $\langle M \rangle_t$ where $M_t = \int_0^t \theta_s\,dW_s$.

??? success "Solution to Exercise 6"
    Let $M_t = -\int_0^t \theta_s\,dW_s$, so $Z_t = \mathcal{E}(M)_t = \exp(M_t - \frac{1}{2}\langle M \rangle_t)$ and $\langle M \rangle_t = \int_0^t \theta_s^2\,ds$.

    The reciprocal is:

    $$
    \frac{1}{Z_t} = \exp(-M_t + \frac{1}{2}\langle M \rangle_t) = \exp\left(\int_0^t \theta_s\,dW_s + \frac{1}{2}\int_0^t \theta_s^2\,ds\right)
    $$

    On the other hand, $\mathcal{E}(-M)_t = \mathcal{E}(\int_0^\cdot \theta_s\,dW_s)_t = \exp(\int_0^t \theta_s\,dW_s - \frac{1}{2}\int_0^t \theta_s^2\,ds)$.

    Comparing:

    $$
    \frac{1}{Z_t} = \mathcal{E}(-M)_t \cdot \exp(\langle M \rangle_t) = \mathcal{E}\left(\int_0^\cdot \theta_s\,dW_s\right)_t \cdot \exp\left(\int_0^t \theta_s^2\,ds\right)
    $$

    The extra factor is $\exp(\langle M \rangle_t) = \exp(\int_0^t \theta_s^2\,ds)$, which is always $\geq 1$. So $1/Z_t > \mathcal{E}(-M)_t$ unless $\theta \equiv 0$. This discrepancy arises because the reciprocal operation interacts with the Itô correction term: flipping the sign of $M$ changes the sign of the first-order term but not the sign of the quadratic variation, creating an asymmetry.

---

**Exercise 7.**
Consider two independent Brownian motions $W_t^1$ and $W_t^2$ and define $X_t = \sigma_1 W_t^1 + \sigma_2 W_t^2$. Compute $\langle X \rangle_t$ and write $\mathcal{E}(X)_t$ explicitly. Then verify using the multiplication rule that $\mathcal{E}(\sigma_1 W^1)_t \cdot \mathcal{E}(\sigma_2 W^2)_t = \mathcal{E}(\sigma_1 W^1 + \sigma_2 W^2)_t$ (since $\langle W^1, W^2 \rangle = 0$).

??? success "Solution to Exercise 7"
    With $X_t = \sigma_1 W_t^1 + \sigma_2 W_t^2$ and $W^1, W^2$ independent:

    $$
    \langle X \rangle_t = \sigma_1^2\langle W^1 \rangle_t + 2\sigma_1\sigma_2\langle W^1, W^2 \rangle_t + \sigma_2^2\langle W^2 \rangle_t = \sigma_1^2 t + 0 + \sigma_2^2 t = (\sigma_1^2 + \sigma_2^2)t
    $$

    The stochastic exponential is:

    $$
    \mathcal{E}(X)_t = \exp\left(\sigma_1 W_t^1 + \sigma_2 W_t^2 - \frac{(\sigma_1^2 + \sigma_2^2)t}{2}\right)
    $$

    Now verify the multiplication rule. With $\langle \sigma_1 W^1, \sigma_2 W^2 \rangle_t = \sigma_1\sigma_2\langle W^1, W^2 \rangle_t = 0$ (independence):

    $$
    \mathcal{E}(\sigma_1 W^1)_t \cdot \mathcal{E}(\sigma_2 W^2)_t = \mathcal{E}(\sigma_1 W^1 + \sigma_2 W^2 + \langle \sigma_1 W^1, \sigma_2 W^2 \rangle)_t = \mathcal{E}(\sigma_1 W^1 + \sigma_2 W^2)_t
    $$

    Explicitly:

    $$
    \mathcal{E}(\sigma_1 W^1)_t \cdot \mathcal{E}(\sigma_2 W^2)_t = \exp\left(\sigma_1 W_t^1 - \frac{\sigma_1^2 t}{2}\right) \cdot \exp\left(\sigma_2 W_t^2 - \frac{\sigma_2^2 t}{2}\right)
    $$

    $$
    = \exp\left(\sigma_1 W_t^1 + \sigma_2 W_t^2 - \frac{(\sigma_1^2 + \sigma_2^2)t}{2}\right) = \mathcal{E}(X)_t
    $$

    The key point is that when the cross-covariation vanishes ($\langle W^1, W^2 \rangle = 0$), the multiplication rule reduces to the ordinary exponential identity $e^a \cdot e^b = e^{a+b}$.

---

**Exercise 8.**
Suppose $Z_T = d\mathbb{Q}/d\mathbb{P}|_{\mathcal{F}_T}$ is given by a stochastic exponential $Z_t = \mathcal{E}(X)_t$ that is a true martingale. A candidate claims: "Then $1/Z_T$ is also a stochastic exponential and therefore automatically a martingale under $\mathbb{Q}$." What is wrong with this reasoning?

??? success "Solution to Exercise 8"
    The reciprocal of a stochastic exponential is **not** a stochastic exponential in the naive sense. If $Z_t = \mathcal{E}(X)_t$, then

    $$
    \frac{1}{Z_t} = \mathcal{E}(-X)_t \cdot \exp(\langle X \rangle_t)
    $$

    The extra factor $\exp(\langle X \rangle_t)$ means $1/Z_t \neq \mathcal{E}(-X)_t$ in general.

    Therefore $1/Z_t$ does not automatically inherit the martingale property from $Z_t$. Whether $1/Z_t$ is a $\mathbb{Q}$-martingale requires a separate verification — typically by checking a Novikov-type condition under $\mathbb{Q}$ for the reversed Girsanov kernel. This subtlety is important when reversing measure changes (e.g., going from $\mathbb{Q}$ back to $\mathbb{P}$).
