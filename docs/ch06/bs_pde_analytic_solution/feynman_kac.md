# Feynman-Kac Formula and the Black-Scholes Solution

Everything in this subsubsection follows from one sentence:

> **The discounted conditional expectation of a payoff is exactly the solution of a backward parabolic PDE.**

The preceding subsubsections derived the Black–Scholes formula by manipulating the PDE — into the heat equation, into frequency space, or by exploiting scaling structure. Feynman–Kac is the reverse direction: it shows that the very same answer is obtained as a *probabilistic expectation*, with no PDE manipulation. The two pictures are not parallel calculations of the same number; they are the **same calculation viewed in two notations**, related by a single elementary averaging identity.

We build the picture in the same order a reader naturally builds intuition: a discrete random walk first (where the averaging is visible by inspection), then the general continuous-time theorem, and only then the Black–Scholes specifics.

---

## 1. Why Expectations Solve PDEs? A Random-Walk Toy

Before any Itô integral or stochastic calculus, work the simplest possible averaging problem on a discrete lattice. The Feynman–Kac formula will appear in miniature, with no analytic machinery needed.

### 1.1 Setup: A Symmetric Random Walk

Let $X_n$ be a symmetric random walk on the integer lattice $\mathbb{Z}$: at each step $X_{n+1} = X_n \pm 1$ with probability $1/2$ each. Fix a terminal time $N$ and a terminal payoff $g(x)$. Define the **conditional-expectation function**

$$
u_n(x) := \mathbb{E}\bigl[g(X_N) \mid X_n = x\bigr]
$$

— what we expect to receive at time $N$, given that we are at position $x$ at time $n$. This is exactly the "value function" that option pricing computes, in the simplest possible setting.

### 1.2 The Averaging Identity

Condition on the next step. From $x$ at time $n$ the walk lands at $x \pm 1$ at time $n + 1$ with equal probability, and from there the expected payoff is $u_{n+1}(x \pm 1)$. Linearity of expectation gives

$$
u_n(x) = \tfrac{1}{2}\, u_{n+1}(x + 1) + \tfrac{1}{2}\, u_{n+1}(x - 1)
$$

**The function $u$ at $(x, n)$ equals the average of its neighbors at $(x \pm 1, n + 1)$.** That is the entire mechanism — no integrals, no Itô, just an averaging identity.

### 1.3 The Averaging Identity Is a Discrete Heat Equation

Subtract $u_{n+1}(x)$ from both sides:

$$
u_n(x) - u_{n+1}(x) = \tfrac{1}{2}\, \bigl[u_{n+1}(x + 1) - 2\, u_{n+1}(x) + u_{n+1}(x - 1)\bigr]
$$

The right-hand side is the **discrete spatial second difference** $\Delta_{xx} u_{n+1}(x)$. The left-hand side is the **negative discrete time difference** $-(u_{n+1}(x) - u_n(x)) = -\Delta_t u_n(x)$. Rewriting:

$$
-\Delta_t u_n(x) = \tfrac{1}{2}\, \Delta_{xx} u_{n+1}(x)
$$

This is a **backward discrete heat equation**. The conditional-expectation function $u_n(x) = \mathbb{E}[g(X_N) \mid X_n = x]$ literally *is* its solution.

### 1.4 The Continuum Limit

Send the lattice spacing to zero with the **diffusive scaling** $\Delta x = \sqrt{\Delta t}$ — the unique scaling that keeps the variance of a step bounded as $\Delta t \to 0$. The discrete time difference $\Delta_t / \Delta t$ becomes $\partial_t$, the discrete second difference $\Delta_{xx} / (\Delta x)^2$ becomes $\partial_{xx}$, and the symmetric random walk converges (Donsker's invariance principle) to standard Brownian motion $W_t$. The discrete identity becomes

$$
-\frac{\partial u}{\partial t} = \frac{1}{2}\, \frac{\partial^2 u}{\partial x^2}
$$

— the **backward heat equation**. Its solution is the conditional expectation

$$
u(x, t) = \mathbb{E}\bigl[g(W_T) \mid W_t = x\bigr]
$$

**The PDE is just the continuum-limit averaging identity.**

### 1.5 Adding a Discount Rate

In option pricing, future cashflows are discounted at rate $r$. The natural modification: each lattice step contributes a discount factor $e^{-r\Delta t}$, so the recursion becomes

$$
u_n(x) = e^{-r\Delta t}\, \bigl[\tfrac{1}{2}\, u_{n+1}(x + 1) + \tfrac{1}{2}\, u_{n+1}(x - 1)\bigr]
$$

Expanding $e^{-r\Delta t} \approx 1 - r\Delta t$ contributes an extra $-r u$ term, and the continuum limit becomes

$$
\frac{\partial u}{\partial t} + \tfrac{1}{2}\, \frac{\partial^2 u}{\partial x^2} - r u = 0
$$

— the discounted backward heat equation. Its solution is the **discounted conditional expectation**

$$
u(x, t) = \mathbb{E}\bigl[e^{-r(T - t)}\, g(W_T) \mid W_t = x\bigr]
$$

### 1.6 What Carries Forward to Black–Scholes

Two ingredients lift to the general Feynman–Kac theorem without modification:

- **The averaging identity becomes the generator of the diffusion.** Replace the symmetric next-step distribution with a general drift-diffusion $dX_t = \mu(X_t, t)\, dt + \sigma(X_t, t)\, dW_t$. By the same conditioning argument, the discrete recursion gives a continuum-limit PDE with second-order operator $\tfrac{1}{2}\sigma^2 \partial_{xx} + \mu \partial_x$ — the **infinitesimal generator** of $X_t$.
- **The discount rate becomes a $-r u$ term in the PDE.** This generalizes to a state-dependent discount $r(X_t)$ or to source terms $f(X_t)$ via the obvious lattice modification.

The result is the Feynman–Kac formula in its full generality, which §2 below states precisely.

!!! tip "Core principle"
    The **Feynman–Kac formula** is the rigorous form of an elementary averaging identity: *value at $(x, t)$ = discounted average of value at $(x', t + \Delta t)$ across the next-step distribution of the underlying process.* In the continuum limit this averaging-plus-discounting identity becomes a backward parabolic PDE generated by the process; the conditional expectation and the PDE solution are the *same function*.

This is the mechanism. Black–Scholes is the application: the GBM stock dynamics under $\mathbb{Q}$ play the role of the underlying process, the discount rate is the risk-free rate, and the payoff $\Phi(S_T)$ replaces $g$.

---

## 2. The General Feynman-Kac Theorem

Recall (see [§ Feynman-Kac Formula](../../ch05/feynman_kac/feynman_kac_formula.md) and [§ Discounted Feynman-Kac](../../ch05/feynman_kac/discounted_feynman_kac.md)): for a diffusion $dX_t = \mu(X_t,t)\,dt + \sigma(X_t,t)\,dW_t$ and a function $u$ solving the parabolic PDE 

$$
u_t + \mu u_x + \tfrac{1}{2}\sigma^2 u_{xx} - r u + f = 0
$$ 

with terminal data $u(\cdot,T) = \Phi$,

$$
u(x,t) = \mathbb{E}\left[\int_t^T e^{-\int_t^s r\,d\tau}f(X_s,s)\,ds + e^{-\int_t^T r\,d\tau}\Phi(X_T) \,\Big|\, X_t = x\right].
$$

For option pricing ($f \equiv 0$, constant $r$) this reduces to the **risk-neutral valuation formula** $u(x,t) = \mathbb{E}[e^{-r(T-t)}\Phi(X_T) \mid X_t = x]$ (see also [§ Risk-Neutral Valuation Principle](../../ch04/risk_neutral/risk_neutral_valuation_principle.md)).

---

## 3. Application to Black-Scholes


### 1. **The Setup**


Under the **risk-neutral measure** $\mathbb{Q}$, the stock price dynamics are:

$$
dS_t = rS_t dt + \sigma S_t dW_t^{\mathbb{Q}}
$$

where:

- $r$ = constant risk-free rate
- $\sigma$ = constant volatility
- $W_t^{\mathbb{Q}}$ = Brownian motion under $\mathbb{Q}$

### 2. **The Black-Scholes PDE**


The option value $V(S,t)$ satisfies:

$$
\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2\frac{\partial^2 V}{\partial S^2} - rV = 0
$$

with terminal condition:

$$
V(S,T) = \Phi(S)
$$

where $\Phi(S)$ is the option payoff:

- European call: $\Phi(S) = (S-K)^+$
- European put: $\Phi(S) = (K-S)^+$

### 3. **Feynman-Kac Representation**


By the Feynman-Kac formula:

$$
\boxed{V(S,t) = e^{-r(T-t)}\mathbb{E}^{\mathbb{Q}}[\Phi(S_T) \mid S_t = S]}
$$

**Interpretation**: The option value is the **expected discounted payoff** under the risk-neutral measure.

**Semigroup viewpoint.** Let $\mathcal{L}$ denote the Black-Scholes generator

$$
\mathcal{L} = rS\frac{\partial}{\partial S} + \frac{1}{2}\sigma^2 S^2\frac{\partial^2}{\partial S^2} - r
$$

and write $\tau = T - t$. Then the solution to the Black-Scholes PDE with terminal data $\Phi$ admits the **operator-exponential** representation

$$
V(\cdot, t) = e^{\tau\mathcal{L}}\Phi
$$

and the Feynman-Kac formula

$$
\left(e^{\tau\mathcal{L}}\Phi\right)(S) = e^{-r\tau}\mathbb{E}^{\mathbb{Q}}[\Phi(S_T) \mid S_t = S]
$$

is precisely the **probabilistic representation of the pricing semigroup** $\mathcal{P}_\tau = e^{\tau\mathcal{L}}$ acting on the terminal payoff. This is the same semigroup obtained in [§ Heat Equation](heat_equation.md) (as a Gaussian convolution operator) and in [§ Fourier Transform](fourier_transform.md) (as a Fourier multiplier); Feynman-Kac realises it as an expectation. The operator-exponential viewpoint is the unifying theme of this chapter, and Feynman-Kac is its probabilistic incarnation.

This converts the PDE problem into a probabilistic expectation problem.

---

## 4. Rigorous Derivation of Feynman-Kac

Recall (see [§ Feynman-Kac Proof Sketch](../../ch05/feynman_kac/feynman_kac_proof_sketch.md)): apply Itô's lemma to the discounted value $Y_t = e^{-\int_0^t r\,ds}u(X_t,t)$; if $u$ satisfies the parabolic PDE the drift vanishes and $Y_t$ is a martingale, so $\mathbb{E}[Y_T \mid \mathcal{F}_t] = Y_t$ yields the Feynman-Kac representation. (Exercise 7 below repeats this argument specialised to Black-Scholes for self-containment.)

For Black-Scholes ($X_t = S_t$, $\mu = rS$, $\sigma_X = \sigma S$, constant $r$), the formula gives

$$
V(S,t) = e^{-r(T-t)}\mathbb{E}^{\mathbb{Q}}[\Phi(S_T) \mid S_t = S]
$$

with $\Phi(S) = (S-K)^+$ (call) or $(K-S)^+$ (put). Any solution of the Black-Scholes PDE has this risk-neutral expectation representation.

---

## 5. Solving the SDE: Distribution of S_T

Recall (see [§ Solving the SDE](../../ch03/sde/solving_sde.md) and [§ Itô Lemma](../../ch03/ito_lemma/ito_lemma.md)): applying Itô's lemma to $\ln S_t$ under $dS_t = rS_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}}$ gives $d(\ln S_t) = (r - \tfrac{1}{2}\sigma^2)\,dt + \sigma\,dW_t^{\mathbb{Q}}$, so

$$
\boxed{S_T = S_t \exp\left[(r - \tfrac{1}{2}\sigma^2)(T-t) + \sigma\sqrt{T-t}\,Z\right], \qquad Z \sim \mathcal{N}(0,1).}
$$

Equivalently, with $\tau = T - t$,

$$
\ln S_T \mid S_t \sim \mathcal{N}\bigl(\ln S_t + (r - \tfrac{1}{2}\sigma^2)\tau,\ \sigma^2\tau\bigr).
$$

The corresponding lognormal transition density $p(S_T \mid S_t)$ is the Gaussian kernel of [§ Heat Equation](heat_equation.md) expressed in $(S,t)$ coordinates rather than transformed $(x,\tau)$ coordinates.

**Canonical role.** This subsubsection is the canonical home in the chapter for the probabilistic form of $(d_1, d_2)$ derived below; later subsubsections (change of numéraire, dividends, characteristic-function methods) reference back to these calculations rather than repeating them.

---

## 6. European Call Option: Detailed Derivation


### 1. **The Pricing Formula via Feynman-Kac**


For a European call with payoff $\Phi(S) = (S-K)^+$:

$$
C(S,t) = e^{-r\tau}\mathbb{E}^{\mathbb{Q}}[(S_T - K)^+ \mid S_t = S]
$$

where $\tau = T - t$.

### 2. **Step 1: Rewrite as Integral**


$$
C(S,t) = e^{-r\tau}\int_K^{\infty}(S_T - K)p(S_T \mid S)dS_T
$$

### 3. **Step 2: Split the Integral**


$$
C(S,t) = e^{-r\tau}\left[\int_K^{\infty}S_T p(S_T \mid S)dS_T - K\int_K^{\infty}p(S_T \mid S)dS_T\right]
$$

$$
= e^{-r\tau}\left[I_1 - K \cdot I_2\right]
$$

We need to evaluate two integrals.

### 4. **Step 3: Change to Log-Normal Variable**


Since $\ln S_T \sim \mathcal{N}(m, v^2)$ where:

- $m = \ln S + (r - \frac{\sigma^2}{2})\tau$
- $v = \sigma\sqrt{\tau}$

Set $y = \ln S_T$, so $S_T = e^y$ and $dS_T = e^y dy$.

The density becomes:

$$
p(S_T)dS_T = \frac{1}{v\sqrt{2\pi}}e^{-\frac{(y-m)^2}{2v^2}}dy
$$

Both integrals transform to:

**Integral $I_2$**:

$$
I_2 = \int_K^{\infty}p(S_T)dS_T = \int_{\ln K}^{\infty}\frac{1}{v\sqrt{2\pi}}e^{-\frac{(y-m)^2}{2v^2}}dy
$$

**Integral $I_1$**:

$$
I_1 = \int_K^{\infty}S_T p(S_T)dS_T = \int_{\ln K}^{\infty}e^y \frac{1}{v\sqrt{2\pi}}e^{-\frac{(y-m)^2}{2v^2}}dy
$$

### 5. **Step 4: Evaluate I_2 (Probability Term)**


Standardize the integral. Let:

$$
Z = \frac{y - m}{v}
$$

Then $y = m + vZ$ and $dy = v dZ$.

When $y = \ln K$: $Z = \frac{\ln K - m}{v}$

When $y = \infty$: $Z = \infty$

Therefore:

$$
I_2 = \int_{\frac{\ln K - m}{v}}^{\infty}\frac{1}{\sqrt{2\pi}}e^{-\frac{Z^2}{2}}dZ = \mathcal{N}\left(-\frac{\ln K - m}{v}\right) = \mathcal{N}\left(\frac{m - \ln K}{v}\right)
$$

Substituting $m = \ln S + (r - \frac{\sigma^2}{2})\tau$ and $v = \sigma\sqrt{\tau}$:

$$
I_2 = \mathcal{N}\left(\frac{\ln(S/K) + (r - \frac{\sigma^2}{2})\tau}{\sigma\sqrt{\tau}}\right)
$$

Define:

$$
\boxed{d_2 = \frac{\ln(S/K) + (r - \frac{\sigma^2}{2})\tau}{\sigma\sqrt{\tau}}}
$$

Then:

$$
I_2 = \mathcal{N}(d_2)
$$

**Interpretation**: $\mathcal{N}(d_2) = \mathbb{Q}(S_T > K)$ is the **risk-neutral probability** that the option expires in-the-money.

### 6. **Step 5: Evaluate I_1 (Stock Term)**


$$
I_1 = \int_{\ln K}^{\infty}e^y \frac{1}{v\sqrt{2\pi}}e^{-\frac{(y-m)^2}{2v^2}}dy
$$

**Key technique**: Complete the square in the exponent --- the same Gaussian-integration manoeuvre used in [§ Heat Equation](heat_equation.md). Combining the linear term $y$ with the quadratic $-(y-m)^2/(2v^2)$ and reorganising as a perfect square in $y$ around the shifted mean $m + v^2$ gives

$$
y - \frac{(y-m)^2}{2v^2} = -\frac{[y-(m+v^2)]^2}{2v^2} + m + \frac{v^2}{2}
$$

(The full step-by-step algebra is carried out in Exercise 2 below.) Substituting back:

$$
I_1 = e^{m + \frac{v^2}{2}}\int_{\ln K}^{\infty}\frac{1}{v\sqrt{2\pi}}e^{-\frac{[y-(m+v^2)]^2}{2v^2}}dy
$$

This is a Gaussian integral with mean shifted to $m + v^2$:

$$
I_1 = e^{m + \frac{v^2}{2}} \cdot \mathcal{N}\left(\frac{(m+v^2) - \ln K}{v}\right)
$$

Simplify the exponent. Recall:

- $m = \ln S + (r - \frac{\sigma^2}{2})\tau$
- $v^2 = \sigma^2\tau$

$$
m + \frac{v^2}{2} = \ln S + (r - \frac{\sigma^2}{2})\tau + \frac{\sigma^2\tau}{2} = \ln S + r\tau
$$

Therefore:

$$
e^{m + \frac{v^2}{2}} = e^{\ln S + r\tau} = Se^{r\tau}
$$

For the normal CDF argument:

$$
\frac{(m+v^2) - \ln K}{v} = \frac{\ln S + r\tau + \frac{\sigma^2\tau}{2} - \ln K}{\sigma\sqrt{\tau}} = \frac{\ln(S/K) + (r + \frac{\sigma^2}{2})\tau}{\sigma\sqrt{\tau}}
$$

Define:

$$
\boxed{d_1 = \frac{\ln(S/K) + (r + \frac{\sigma^2}{2})\tau}{\sigma\sqrt{\tau}} = d_2 + \sigma\sqrt{\tau}}
$$

Then:

$$
I_1 = Se^{r\tau}\mathcal{N}(d_1)
$$

### 7. **Step 6: Combine Results**


$$
C(S,t) = e^{-r\tau}[I_1 - KI_2]
$$

$$
= e^{-r\tau}\left[Se^{r\tau}\mathcal{N}(d_1) - K\mathcal{N}(d_2)\right]
$$

$$
\boxed{C(S,t) = S\mathcal{N}(d_1) - Ke^{-r\tau}\mathcal{N}(d_2)}
$$

where:

$$
\boxed{d_1 = \frac{\ln(S/K) + (r + \frac{\sigma^2}{2})\tau}{\sigma\sqrt{\tau}}, \quad d_2 = d_1 - \sigma\sqrt{\tau} = \frac{\ln(S/K) + (r - \frac{\sigma^2}{2})\tau}{\sigma\sqrt{\tau}}}
$$

**This is the Black-Scholes formula for a European call option.**

---

## 7. European Put Option


### 1. **Method 1: Direct Calculation**


For a European put with payoff $\Phi(S) = (K-S)^+$:

$$
P(S,t) = e^{-r\tau}\mathbb{E}^{\mathbb{Q}}[(K - S_T)^+ \mid S_t = S]
$$

$$
= e^{-r\tau}\int_0^K(K - S_T)p(S_T \mid S)dS_T
$$

Following similar calculations (completing the square with reversed integration limits):

$$
\boxed{P(S,t) = Ke^{-r\tau}\mathcal{N}(-d_2) - S\mathcal{N}(-d_1)}
$$

where $d_1$ and $d_2$ are the same as for the call.

### 2. **Method 2: Put-Call Parity**


From the no-arbitrage relationship:

$$
C - P = S - Ke^{-r\tau}
$$

Therefore:

$$
P = C - S + Ke^{-r\tau}
$$

$$
= S\mathcal{N}(d_1) - Ke^{-r\tau}\mathcal{N}(d_2) - S + Ke^{-r\tau}
$$

$$
= S(\mathcal{N}(d_1) - 1) + Ke^{-r\tau}(1 - \mathcal{N}(d_2))
$$

Using $\mathcal{N}(-x) = 1 - \mathcal{N}(x)$:

$$
P = -S\mathcal{N}(-d_1) + Ke^{-r\tau}\mathcal{N}(-d_2)
$$

$$
\boxed{P(S,t) = Ke^{-r\tau}\mathcal{N}(-d_2) - S\mathcal{N}(-d_1)}
$$

Both methods yield the same formula. ✓

---

## 8. Probabilistic Interpretation


### 1. **The Two Terms in the Call Formula**


$$
C = \underbrace{S\mathcal{N}(d_1)}_{\text{Stock term}} - \underbrace{Ke^{-r\tau}\mathcal{N}(d_2)}_{\text{Strike term}}
$$

### 2. **Meaning of N(d_2)**


$$
\boxed{\mathcal{N}(d_2) = \mathbb{Q}(S_T > K \mid S_t = S)}
$$

This is the **risk-neutral probability** that the option expires in-the-money.


### 3. **Meaning of N(d_1)**


$\mathcal{N}(d_1)$ represents the probability of exercise under the **stock measure** $\mathbb{Q}^S$:

$$
\boxed{\mathcal{N}(d_1) = \mathbb{Q}^S(S_T > K \mid S_t = S)}
$$

---

## 9. Connection to Kolmogorov Equations

Recall (see [§ Understanding SDE Solutions](../../ch03/sde/understanding_sde_solutions.md) and [§ Feynman-Kac Applications](../../ch05/feynman_kac/feynman_kac_applications.md)): the Black-Scholes PDE is the **Kolmogorov backward equation** for $S_t$ under $\mathbb{Q}$ (solved backward from terminal data $\Phi$), and the transition density $p(S_T,T \mid S_t,t)$ satisfies the dual **Kolmogorov forward (Fokker-Planck) equation** $\partial_T p = -\partial_{S_T}(rS_T p) + \tfrac{1}{2}\partial_{S_T S_T}(\sigma^2 S_T^2 p)$. Feynman-Kac is precisely the bridge $V(S,t) = e^{-r\tau}\int \Phi(S_T)\,p(S_T,T \mid S,t)\,dS_T$.

---

## 10. Why Feynman-Kac Works: Deep Intuition


The rigorous derivation in the previous subsubsections established that the discounted value $e^{-\int_0^t r\,ds}\,u(X_t,t)$ is a martingale whenever $u$ satisfies the Feynman-Kac PDE. In the Black-Scholes setting this takes a particularly transparent form.

### 1. **The Martingale Property**


Under the risk-neutral measure, $d(e^{-rt}S_t) = e^{-rt}\sigma S_t\,dW_t^{\mathbb{Q}}$, which has no drift. Hence the discounted stock price is a martingale, and by the same argument the discounted option value $e^{-rt}V(S_t,t)$ is a martingale whenever $V$ satisfies the Black-Scholes PDE. This immediately yields the Feynman-Kac representation $V(S_t,t) = e^{-r(T-t)}\mathbb{E}^{\mathbb{Q}}[\Phi(S_T) \mid \mathcal{F}_t]$.

### 2. **No-Arbitrage = Martingale Measure**


The Feynman-Kac formula is the **mathematical manifestation of no-arbitrage pricing**:

**Fundamental Theorem of Asset Pricing**:

- **No arbitrage** $\Longleftrightarrow$ Existence of equivalent martingale measure $\mathbb{Q}$
- **Completeness** + No arbitrage $\Longleftrightarrow$ **Unique** martingale measure

The risk-neutral measure $\mathbb{Q}$ is the unique measure under which:

1. Discounted asset prices are martingales
2. All derivatives can be priced consistently

**Economic interpretation**: Feynman-Kac converts the no-arbitrage condition into an explicit pricing formula.

---

## 11. Extensions and Generalizations


### 1. **With Continuous Dividend Yield**


If the stock pays continuous dividends at rate $q$:

$$
dS_t = (r-q)S_t dt + \sigma S_t dW_t^{\mathbb{Q}}
$$

The Black-Scholes formula becomes:

$$
\boxed{C(S,t) = Se^{-q\tau}\mathcal{N}(d_1) - Ke^{-r\tau}\mathcal{N}(d_2)}
$$

where:

$$
d_1 = \frac{\ln(S/K) + (r - q + \frac{\sigma^2}{2})\tau}{\sigma\sqrt{\tau}}, \quad d_2 = d_1 - \sigma\sqrt{\tau}
$$

**Application**: Foreign exchange options (treat foreign interest rate as dividend yield).

### 2. **With Time-Dependent Parameters**


For time-varying $r(t)$, $\sigma(t)$, $q(t)$:

$$
V(S,t) = \mathbb{E}^{\mathbb{Q}}\left[\exp\left(-\int_t^T r(s)ds\right)\Phi(S_T) \mid S_t = S\right]
$$

where:

$$
S_T = S_t\exp\left[\int_t^T\left(r(s)-q(s)-\frac{\sigma^2(s)}{2}\right)ds + \int_t^T\sigma(s)dW_s^{\mathbb{Q}}\right]
$$

The log-return is normally distributed with:

- Mean: $\int_t^T(r(s) - q(s) - \frac{\sigma^2(s)}{2})ds$
- Variance: $\int_t^T\sigma^2(s)ds$

**Modified $d_1$ and $d_2$**: Replace $r\tau$ with $\int_t^T r(s)ds$ and $\sigma^2\tau$ with $\int_t^T\sigma^2(s)ds$.

### 3. **Multi-Dimensional Case**


For basket options with $n$ assets $S_1, \ldots, S_n$:

$$
V(\mathbf{S},t) = e^{-r\tau}\mathbb{E}^{\mathbb{Q}}[\Phi(\mathbf{S}_T) \mid \mathbf{S}_t = \mathbf{S}]
$$

where $\mathbf{S}_T = (S_1^T, \ldots, S_n^T)$ follows a **multivariate log-normal distribution** with correlation matrix $\rho$.

**Example payoffs**:

- Basket call: $\Phi = (\sum_{i=1}^n w_i S_i^T - K)^+$
- Exchange option: $\Phi = (S_1^T - S_2^T)^+$
- Spread option: $\Phi = (S_1^T - S_2^T - K)^+$

**Evaluation**: Typically requires numerical integration or Monte Carlo simulation.

---

## 12. Summary


The Feynman-Kac formula establishes the fundamental connection:

$$
\text{PDE Solution} = \text{Probabilistic Expectation}
$$

**For Black-Scholes**:

$$
V(S,t) = e^{-r(T-t)}\mathbb{E}^{\mathbb{Q}}[\Phi(S_T) \mid S_t = S]
$$

**Derivation steps**:

1. Apply Ito's lemma to discounted $u(X_t,t)$
2. Show it becomes a martingale if $u$ satisfies the PDE
3. Take expectation to get probabilistic representation
4. Solve SDE to find distribution of $S_T$ (log-normal)
5. Evaluate expectation by integrating against density
6. Complete the square to obtain $\mathcal{N}(d_1)$ and $\mathcal{N}(d_2)$ terms

**Black-Scholes formulas**:

**Call**: $C = S\mathcal{N}(d_1) - Ke^{-r\tau}\mathcal{N}(d_2)$

**Put**: $P = Ke^{-r\tau}\mathcal{N}(-d_2) - S\mathcal{N}(-d_1)$

where:

$$
d_1 = \frac{\ln(S/K) + (r + \frac{\sigma^2}{2})\tau}{\sigma\sqrt{\tau}}, \quad d_2 = d_1 - \sigma\sqrt{\tau}
$$

**Interpretation**:

- $\mathcal{N}(d_2)$ = Risk-neutral probability of exercise
- $\mathcal{N}(d_1)$ = Delta = Stock-measure probability of exercise

**Why Feynman-Kac is powerful**:

- **Converts PDE to probability**: expectations are often easier to compute than solving PDEs, and carry intuitive economic meaning
- **Enables Monte Carlo simulation**: particularly useful for high-dimensional and path-dependent problems
- **Generalizes naturally**: extends to time-dependent parameters, multiple assets, and exotic payoffs
- **Theoretical foundation**: links stochastic calculus with classical PDE theory and the Fundamental Theorem of Asset Pricing

The formula demonstrates that **PDE**, **probability**, and **stochastic process** are three equivalent perspectives on the same mathematical object --- a trinity that underlies modern quantitative finance and enables both theoretical insight and practical computation.

### The three core methods are one object

The expectation $\mathbb{E}^{\mathbb{Q}}[\Phi(S_T) \mid S_t = S]$ is a convolution of the payoff with the transition density of $\ln S_T$ --- exactly the Green's function integral derived in the heat equation subsubsection. The heat equation *convolution* and the Feynman-Kac *expectation* are the same integral; the Green's function and the transition density are the same function. Conversely, writing the expectation as $\mathbb{E}^{\mathbb{Q}}[e^{i\omega \ln S_T}]$ in frequency space yields the **characteristic function** $\phi_T(\omega)$ that drives Fourier methods. The three core approaches of this chapter are therefore not independent techniques. They compute the same object --- the pricing semigroup $\mathcal{P}_\tau = e^{\tau\mathcal{L}}$ applied to the payoff --- in three coordinate systems:

| Method | Coordinate system | Key object |
|---|---|---|
| Heat equation | Spatial $(x, \tau)$ | Green's function (Gaussian kernel) |
| Feynman-Kac | Probabilistic | Transition density / expectation |
| Fourier | Spectral $(\omega)$ | Characteristic function |

---

## Exercises

**Exercise 1.** Verify the Feynman-Kac formula for the trivial case $\Phi(S) = S$ (the stock itself). Show that $V(S,t) = S$ satisfies both the Black-Scholes PDE and the expectation $e^{-r(T-t)}\mathbb{E}^{\mathbb{Q}}[S_T \mid S_t = S]$.

??? success "Solution to Exercise 1"
    We need to verify that $V(S,t) = S$ satisfies both the Black-Scholes PDE and the Feynman-Kac representation.

    **PDE verification.** With $V = S$: $\frac{\partial V}{\partial t} = 0$, $\frac{\partial V}{\partial S} = 1$, $\frac{\partial^2 V}{\partial S^2} = 0$. Substituting:

    $$
    0 + rS \cdot 1 + \frac{1}{2}\sigma^2 S^2 \cdot 0 - rS = rS - rS = 0
    $$

    The PDE is satisfied.

    **Feynman-Kac verification.** We need $e^{-r(T-t)}\mathbb{E}^{\mathbb{Q}}[S_T \mid S_t = S] = S$.

    Under $\mathbb{Q}$, $S_T = S \exp\left((r - \frac{1}{2}\sigma^2)(T-t) + \sigma(W_T - W_t)\right)$. Taking the expectation:

    $$
    \mathbb{E}^{\mathbb{Q}}[S_T \mid S_t = S] = S \exp\left((r - \frac{1}{2}\sigma^2)(T-t)\right) \cdot \mathbb{E}\left[\exp(\sigma(W_T - W_t))\right]
    $$

    Since $W_T - W_t \sim \mathcal{N}(0, T-t)$:

    $$
    \mathbb{E}[\exp(\sigma(W_T - W_t))] = \exp\left(\frac{1}{2}\sigma^2(T-t)\right)
    $$

    Therefore:

    $$
    \mathbb{E}^{\mathbb{Q}}[S_T \mid S_t = S] = S \exp\left((r - \frac{1}{2}\sigma^2 + \frac{1}{2}\sigma^2)(T-t)\right) = Se^{r(T-t)}
    $$

    Discounting: $e^{-r(T-t)} \cdot Se^{r(T-t)} = S$. Both representations agree.

---
**Exercise 2.** Carry out the "completing the square" step in the evaluation of $I_1$ in full detail. Starting from the combined exponent $y - \frac{(y-m)^2}{2v^2}$, show every algebraic step leading to the factorization into $e^{m + v^2/2}$ times a Gaussian integral with shifted mean $m + v^2$.

??? success "Solution to Exercise 2"
    Starting from the combined exponent $y - \frac{(y-m)^2}{2v^2}$, we proceed step by step.

    **Step 1: Write as a single fraction.**

    $$
    y - \frac{(y-m)^2}{2v^2} = \frac{2v^2 y - (y-m)^2}{2v^2}
    $$

    **Step 2: Expand the numerator.**

    $$
    2v^2 y - (y-m)^2 = 2v^2 y - y^2 + 2ym - m^2
    $$

    $$
    = -y^2 + 2y(m + v^2) - m^2
    $$

    **Step 3: Complete the square in $y$.**

    $$
    -y^2 + 2y(m+v^2) - m^2 = -\left[y^2 - 2y(m+v^2)\right] - m^2
    $$

    $$
    = -\left[(y - (m+v^2))^2 - (m+v^2)^2\right] - m^2
    $$

    $$
    = -(y - (m+v^2))^2 + (m+v^2)^2 - m^2
    $$

    **Step 4: Simplify the constant.**

    $$
    (m+v^2)^2 - m^2 = m^2 + 2mv^2 + v^4 - m^2 = 2mv^2 + v^4
    $$

    **Step 5: Substitute back.**

    $$
    y - \frac{(y-m)^2}{2v^2} = \frac{-(y-(m+v^2))^2 + 2mv^2 + v^4}{2v^2}
    $$

    $$
    = -\frac{(y-(m+v^2))^2}{2v^2} + m + \frac{v^2}{2}
    $$

    **Step 6: Factor out the constant.** Therefore:

    $$
    \exp\left(y - \frac{(y-m)^2}{2v^2}\right) = \exp\left(m + \frac{v^2}{2}\right) \cdot \exp\left(-\frac{(y-(m+v^2))^2}{2v^2}\right)
    $$

    The second factor is the kernel of a Gaussian with mean $m + v^2$ and variance $v^2$, confirming that $I_1 = e^{m+v^2/2} \cdot \mathcal{N}\left(\frac{(m+v^2) - \ln K}{v}\right)$.

---
**Exercise 3.** Use the Feynman-Kac representation to derive the price of a **power option** with payoff $\Phi(S_T) = S_T^2$ at maturity. Compute $e^{-r(T-t)}\mathbb{E}^{\mathbb{Q}}[S_T^2 \mid S_t = S]$ using the log-normal distribution of $S_T$.

??? success "Solution to Exercise 3"
    The payoff is $\Phi(S_T) = S_T^2$. By Feynman-Kac:

    $$
    V(S,t) = e^{-r\tau}\mathbb{E}^{\mathbb{Q}}[S_T^2 \mid S_t = S]
    $$

    where $\tau = T - t$.

    Under $\mathbb{Q}$, $S_T = S\exp\left((r - \frac{1}{2}\sigma^2)\tau + \sigma\sqrt{\tau}Z\right)$ with $Z \sim \mathcal{N}(0,1)$. Therefore:

    $$
    S_T^2 = S^2 \exp\left(2(r - \frac{1}{2}\sigma^2)\tau + 2\sigma\sqrt{\tau}Z\right)
    $$

    Taking the expectation:

    $$
    \mathbb{E}[S_T^2] = S^2 \exp\left(2(r - \frac{1}{2}\sigma^2)\tau\right) \cdot \mathbb{E}[\exp(2\sigma\sqrt{\tau}Z)]
    $$

    Using $\mathbb{E}[e^{aZ}] = e^{a^2/2}$ for $Z \sim \mathcal{N}(0,1)$:

    $$
    \mathbb{E}[\exp(2\sigma\sqrt{\tau}Z)] = \exp(2\sigma^2\tau)
    $$

    Therefore:

    $$
    \mathbb{E}[S_T^2] = S^2 \exp\left(2r\tau - \sigma^2\tau + 2\sigma^2\tau\right) = S^2 \exp\left((2r + \sigma^2)\tau\right)
    $$

    Discounting:

    $$
    V(S,t) = e^{-r\tau} \cdot S^2 e^{(2r+\sigma^2)\tau} = S^2 e^{(r+\sigma^2)\tau}
    $$

    One can verify this satisfies the Black-Scholes PDE: with $V = S^2 e^{(r+\sigma^2)\tau}$, computing $V_t = -(r+\sigma^2)V$, $V_S = 2Se^{(r+\sigma^2)\tau}$, $V_{SS} = 2e^{(r+\sigma^2)\tau}$, and substituting into $V_t + rSV_S + \frac{1}{2}\sigma^2 S^2 V_{SS} - rV = 0$ confirms the identity.

---
**Exercise 4.** The Kolmogorov backward equation for Black-Scholes governs $V(S,t)$, while the forward equation governs the transition density $p(S_T, T \mid S, t)$. Starting from the Black-Scholes backward equation, write down the corresponding forward (Fokker-Planck) equation and verify that the log-normal density $p(S_T, T \mid S, t)$ satisfies it.

??? success "Solution to Exercise 4"
    **Backward equation** (Black-Scholes PDE for $V(S,t)$):

    $$
    \frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2\frac{\partial^2 V}{\partial S^2} - rV = 0
    $$

    **Deriving the forward equation.** The transition density $p(S_T, T \mid S, t)$ satisfies the Kolmogorov forward (Fokker-Planck) equation with respect to $(S_T, T)$:

    $$
    \frac{\partial p}{\partial T} = -\frac{\partial}{\partial S_T}(rS_T \, p) + \frac{1}{2}\frac{\partial^2}{\partial S_T^2}(\sigma^2 S_T^2 \, p)
    $$

    **Verification.** The log-normal density is:

    $$
    p(S_T, T \mid S, t) = \frac{1}{S_T \sigma\sqrt{2\pi\tau}}\exp\left(-\frac{(\ln(S_T/S) - (r - \frac{\sigma^2}{2})\tau)^2}{2\sigma^2\tau}\right)
    $$

    Let $y = \ln S_T$, $m = \ln S + (r - \frac{\sigma^2}{2})\tau$, $v^2 = \sigma^2\tau$. The density in $y$-space is Gaussian: $q(y) = \frac{1}{\sqrt{2\pi v^2}}e^{-(y-m)^2/(2v^2)}$.

    Taking derivatives of $q$ with respect to $T$ (noting $m$ and $v^2$ both depend on $T$), one can verify by direct computation that the forward equation is satisfied. The key steps involve:

    - $\frac{\partial m}{\partial T} = r - \frac{\sigma^2}{2}$ and $\frac{\partial v^2}{\partial T} = \sigma^2$
    - Converting derivatives with respect to $S_T$ to derivatives with respect to $y$ using $\frac{\partial}{\partial S_T} = \frac{1}{S_T}\frac{\partial}{\partial y}$
    - Expanding the forward equation terms and verifying cancellation

---
**Exercise 5.** Using the Feynman-Kac formula with time-dependent volatility $\sigma(t)$, show that the Black-Scholes call price takes the same functional form as the constant-volatility case, but with $\sigma^2 T$ replaced by $\int_t^T \sigma^2(s) \, ds$. Define the effective volatility $\bar{\sigma}$ and express $d_1$ and $d_2$ in terms of $\bar{\sigma}$.

??? success "Solution to Exercise 5"
    With time-dependent volatility $\sigma(t)$, the SDE under $\mathbb{Q}$ is:

    $$
    dS_s = rS_s \, ds + \sigma(s) S_s \, dW_s^{\mathbb{Q}}
    $$

    By Ito's lemma applied to $\ln S$:

    $$
    \ln S_T = \ln S_t + \int_t^T \left(r - \frac{\sigma^2(s)}{2}\right)ds + \int_t^T \sigma(s) \, dW_s
    $$

    The stochastic integral $\int_t^T \sigma(s) \, dW_s$ is Gaussian with mean 0 and variance $\int_t^T \sigma^2(s) \, ds$.

    Define the **effective (total) variance**:

    $$
    \Sigma^2 = \int_t^T \sigma^2(s) \, ds
    $$

    and the **effective volatility**:

    $$
    \bar{\sigma} = \sqrt{\frac{1}{\tau}\int_t^T \sigma^2(s) \, ds}
    $$

    so that $\Sigma^2 = \bar{\sigma}^2 \tau$.

    The distribution of $\ln S_T$ is:

    $$
    \ln S_T \mid S_t \sim \mathcal{N}\left(\ln S_t + r\tau - \frac{\Sigma^2}{2}, \, \Sigma^2\right)
    $$

    This is identical to the constant-volatility case with $\sigma^2\tau$ replaced by $\Sigma^2 = \int_t^T \sigma^2(s) \, ds$. The call price therefore takes the same functional form:

    $$
    C = S\mathcal{N}(d_1) - Ke^{-r\tau}\mathcal{N}(d_2)
    $$

    with:

    $$
    d_1 = \frac{\ln(S/K) + r\tau + \frac{1}{2}\bar{\sigma}^2\tau}{\bar{\sigma}\sqrt{\tau}} = \frac{\ln(S/K) + r\tau + \frac{1}{2}\Sigma^2}{\Sigma}
    $$

    $$
    d_2 = d_1 - \bar{\sigma}\sqrt{\tau} = d_1 - \Sigma
    $$

---
**Exercise 6.** Consider a European option with payoff $\Phi(S_T) = \ln(S_T)$ (a log contract). Use the Feynman-Kac representation to compute its price $V(S,t) = e^{-r\tau}\mathbb{E}^{\mathbb{Q}}[\ln S_T \mid S_t = S]$. Show that the result is $V = e^{-r\tau}[\ln S + (r - \frac{1}{2}\sigma^2)\tau]$, and verify that this satisfies the Black-Scholes PDE.

??? success "Solution to Exercise 6"
    The payoff is $\Phi(S_T) = \ln(S_T)$. By Feynman-Kac:

    $$
    V(S,t) = e^{-r\tau}\mathbb{E}^{\mathbb{Q}}[\ln S_T \mid S_t = S]
    $$

    Under $\mathbb{Q}$:

    $$
    \ln S_T = \ln S + (r - \frac{1}{2}\sigma^2)\tau + \sigma\sqrt{\tau}Z
    $$

    Taking the expectation ($\mathbb{E}[Z] = 0$):

    $$
    \mathbb{E}^{\mathbb{Q}}[\ln S_T \mid S_t = S] = \ln S + (r - \frac{1}{2}\sigma^2)\tau
    $$

    Therefore:

    $$
    V(S,t) = e^{-r\tau}\left[\ln S + (r - \frac{1}{2}\sigma^2)\tau\right]
    $$

    **PDE verification.** Let $\tau = T - t$ and compute derivatives:

    $$
    \frac{\partial V}{\partial t} = re^{-r\tau}\left[\ln S + (r - \frac{1}{2}\sigma^2)\tau\right] + e^{-r\tau}(r - \frac{1}{2}\sigma^2)(-1)
    $$

    Since $\frac{\partial \tau}{\partial t} = -1$:

    $$
    \frac{\partial V}{\partial t} = re^{-r\tau}\left[\ln S + (r-\frac{1}{2}\sigma^2)\tau\right] - e^{-r\tau}(r - \frac{1}{2}\sigma^2)
    $$

    $$
    \frac{\partial V}{\partial S} = \frac{e^{-r\tau}}{S}, \quad \frac{\partial^2 V}{\partial S^2} = -\frac{e^{-r\tau}}{S^2}
    $$

    Substituting into the BS PDE:

    $$
    re^{-r\tau}[\ln S + (r-\frac{1}{2}\sigma^2)\tau] - e^{-r\tau}(r-\frac{1}{2}\sigma^2) + rS \cdot \frac{e^{-r\tau}}{S} + \frac{\sigma^2 S^2}{2}\cdot\left(-\frac{e^{-r\tau}}{S^2}\right) - re^{-r\tau}[\ln S + (r-\frac{1}{2}\sigma^2)\tau]
    $$

    Factoring out $e^{-r\tau}$:

    $$
    -(r-\frac{1}{2}\sigma^2) + r - \frac{1}{2}\sigma^2 = -r + \frac{1}{2}\sigma^2 + r - \frac{1}{2}\sigma^2 = 0
    $$

    The PDE is satisfied.

---
**Exercise 7.** The discounted option value $e^{-rt}V(S_t, t)$ is a martingale under $\mathbb{Q}$. Use Ito's lemma to compute $d(e^{-rt}V)$ and show that the drift vanishes if and only if $V$ satisfies the Black-Scholes PDE. This provides an alternative proof of the Feynman-Kac connection.

??? success "Solution to Exercise 7"
    Let $Y_t = e^{-rt}V(S_t, t)$. Apply the product rule (Ito's lemma for products):

    $$
    dY_t = -re^{-rt}V \, dt + e^{-rt} \, dV
    $$

    Apply Ito's lemma to $V(S_t, t)$:

    $$
    dV = \frac{\partial V}{\partial t} \, dt + \frac{\partial V}{\partial S} \, dS_t + \frac{1}{2}\frac{\partial^2 V}{\partial S^2}(dS_t)^2
    $$

    Under $\mathbb{Q}$, $dS_t = rS_t \, dt + \sigma S_t \, dW_t$ and $(dS_t)^2 = \sigma^2 S_t^2 \, dt$. Substituting:

    $$
    dV = \left[\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2\frac{\partial^2 V}{\partial S^2}\right]dt + \sigma S\frac{\partial V}{\partial S} \, dW_t
    $$

    Therefore:

    $$
    dY_t = e^{-rt}\left[\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2\frac{\partial^2 V}{\partial S^2} - rV\right]dt + e^{-rt}\sigma S\frac{\partial V}{\partial S} \, dW_t
    $$

    For $Y_t$ to be a martingale, the $dt$ coefficient (drift) must vanish:

    $$
    \frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2\frac{\partial^2 V}{\partial S^2} - rV = 0
    $$

    This is exactly the Black-Scholes PDE. Conversely, if $V$ satisfies the PDE, then:

    $$
    dY_t = e^{-rt}\sigma S_t\frac{\partial V}{\partial S}(S_t, t) \, dW_t
    $$

    which has no drift, so $Y_t = e^{-rt}V(S_t,t)$ is a local martingale (and a martingale under standard integrability conditions). This provides an alternative derivation of the Feynman-Kac representation.
