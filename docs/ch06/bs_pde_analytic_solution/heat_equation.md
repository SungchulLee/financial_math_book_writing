# Black-Scholes Formula via Heat Equation


The Black-Scholes PDE can be transformed into the **heat equation**, one of the most studied partial differential equations in mathematical physics. This transformation allows us to leverage the well-known fundamental solution (Green's function) to derive the Black-Scholes formula analytically.

This approach reveals the deep connection between option pricing and diffusion processes, demonstrating how financial derivatives can be priced using classical PDE techniques.

---

## The Black-Scholes PDE


### 1. **Standard Form**


For a European option value $V(S,t)$:

$$
\boxed{\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + rS\frac{\partial V}{\partial S} - rV = 0}
$$

**Terminal condition** (European call):

$$
V(S,T) = \max(S-K, 0)
$$

**Challenge**: The PDE has:
- Variable coefficients ($S^2$ and $S$ terms)
- A zero-order term ($-rV$)
- Terminal condition (not initial)

**Strategy**: Transform into the heat equation, which has constant coefficients and is thoroughly understood.

---

## Change of Variables


We apply three transformations to reduce the BS PDE to canonical heat equation form.

### 1. **Transformation 1: Time to Maturity**


$$
\boxed{\tau = T - t}
$$

**Meaning**: Time remaining until option expiration.

**Example**: If current time is $t = 0.5$ years and expiration is $T = 1$ year:

$$
\tau = 1 - 0.5 = 0.5 \text{ years (6 months remaining)}
$$

**Effect**: Converts terminal condition into initial condition and reverses time direction:

$$
\frac{\partial}{\partial t} = -\frac{\partial}{\partial \tau}
$$

### 2. **Transformation 2: Expected Log-Price**


$$
\boxed{x = \log S + \left(r - \frac{1}{2}\sigma^2\right)\tau}
$$

**Meaning**: This is the **expected log-price** at maturity under the risk-neutral measure.

**Derivation**: Under geometric Brownian motion:

$$
S_T = S_t \exp\left(\left(r - \frac{1}{2}\sigma^2\right)(T-t) + \sigma W_\tau\right)
$$

Taking logarithm and expectation:

$$
\mathbb{E}^{\mathbb{Q}}[\log S_T | S_t] = \log S_t + \left(r - \frac{1}{2}\sigma^2\right)\tau = x
$$

**Example**: For $S = 100$, $r = 5\%$, $\sigma = 20\%$, $\tau = 0.5$:

$$
\begin{aligned}
x &= \log 100 + \left(0.05 - \frac{1}{2}(0.2)^2\right) \cdot 0.5 \\
&= 4.605 + (0.05 - 0.02) \cdot 0.5 \\
&= 4.605 + 0.015 = 4.620
\end{aligned}
$$

**Effect**: Centers the process by removing drift, converting first-order terms to second-order.

### 3. **Transformation 3: Forward Option Value**


$$
\boxed{F(x,\tau) = V(S,t) e^{r\tau}}
$$

**Meaning**: Option value **compounded forward** to expiration at the risk-free rate.

**Intuition**: Under risk-neutral pricing:

$$
V(S,t) = e^{-r\tau}\mathbb{E}^{\mathbb{Q}}[\text{Payoff}]
$$

so

$$
F(x,\tau) = \mathbb{E}^{\mathbb{Q}}[\text{Payoff}]
$$

is the **undiscounted expected payoff**.

**Example**: If current option value is $V = 10$, $r = 5\%$, $\tau = 0.5$:

$$
F = 10 \cdot e^{0.05 \times 0.5} = 10 \cdot e^{0.025} \approx 10.25
$$

**Effect**: Eliminates the $-rV$ term from the PDE.

---

## Transformation of Derivatives


### 1. **Time Derivative**


Using chain rule:

$$
\frac{\partial V}{\partial t} = \frac{\partial V}{\partial x}\frac{\partial x}{\partial t} + \frac{\partial V}{\partial \tau}\frac{\partial \tau}{\partial t}
$$

Since:
- $\frac{\partial x}{\partial t} = -\left(r - \frac{1}{2}\sigma^2\right)$ (from definition of $x$)
- $\frac{\partial \tau}{\partial t} = -1$

We get:

$$
\frac{\partial V}{\partial t} = -\left(r - \frac{1}{2}\sigma^2\right)\frac{\partial V}{\partial x} - \frac{\partial V}{\partial \tau}
$$

### 2. **First Spatial Derivative**


$$
\frac{\partial V}{\partial S} = \frac{\partial V}{\partial x}\frac{\partial x}{\partial S} = \frac{\partial V}{\partial x} \cdot \frac{1}{S}
$$

### 3. **Second Spatial Derivative**


$$
\begin{aligned}
\frac{\partial^2 V}{\partial S^2} &= \frac{\partial}{\partial S}\left(\frac{1}{S}\frac{\partial V}{\partial x}\right) \\
&= \frac{\partial}{\partial x}\left(\frac{1}{S}\frac{\partial V}{\partial x}\right)\frac{\partial x}{\partial S} \\
&= \frac{1}{S}\left[\frac{\partial^2 V}{\partial x^2}\frac{1}{S} + \frac{\partial V}{\partial x}\frac{\partial}{\partial x}\left(\frac{1}{S}\right)\right]
\end{aligned}
$$

**Key observation**: Since $S = e^{x - (r-\frac{1}{2}\sigma^2)\tau}$:

$$
\frac{\partial}{\partial x}\left(\frac{1}{S}\right) = -\frac{1}{S}
$$

Therefore:

$$
\frac{\partial^2 V}{\partial S^2} = \frac{1}{S^2}\left[\frac{\partial^2 V}{\partial x^2} - \frac{\partial V}{\partial x}\right]
$$

---

## Derivation of the Heat Equation


### 1. **Step 1: Substitute into BS PDE**


Starting with:

$$
\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + rS\frac{\partial V}{\partial S} - rV = 0
$$

Substitute transformed derivatives:

$$
\begin{aligned}
&-\left(r - \frac{1}{2}\sigma^2\right)\frac{\partial V}{\partial x} - \frac{\partial V}{\partial \tau} \\
&\quad + \frac{1}{2}\sigma^2\left[\frac{\partial^2 V}{\partial x^2} - \frac{\partial V}{\partial x}\right] \\
&\quad + r\frac{\partial V}{\partial x} - rV = 0
\end{aligned}
$$

### 2. **Step 2: Collect Terms**


Grouping by derivative order:

- **Second-order**: $\frac{1}{2}\sigma^2\frac{\partial^2 V}{\partial x^2}$
- **First-order**: $-\left(r - \frac{1}{2}\sigma^2\right)\frac{\partial V}{\partial x} - \frac{1}{2}\sigma^2\frac{\partial V}{\partial x} + r\frac{\partial V}{\partial x} = 0$ (cancels!)
- **Zero-order**: $-\frac{\partial V}{\partial \tau} - rV = 0$

Result:

$$
-\frac{\partial V}{\partial \tau} + \frac{1}{2}\sigma^2\frac{\partial^2 V}{\partial x^2} - rV = 0
$$

### 3. **Step 3: Eliminate -rV Term**


Since $V = Fe^{-r\tau}$, compute derivatives:

$$
\frac{\partial V}{\partial \tau} = \frac{\partial F}{\partial \tau}e^{-r\tau} - rFe^{-r\tau}
$$

$$
\frac{\partial^2 V}{\partial x^2} = \frac{\partial^2 F}{\partial x^2}e^{-r\tau}
$$

Substitute into the PDE:

$$
-\left[\frac{\partial F}{\partial \tau}e^{-r\tau} - rFe^{-r\tau}\right] + \frac{1}{2}\sigma^2\frac{\partial^2 F}{\partial x^2}e^{-r\tau} - rFe^{-r\tau} = 0
$$

Divide by $e^{-r\tau}$:

$$
-\frac{\partial F}{\partial \tau} + rF + \frac{1}{2}\sigma^2\frac{\partial^2 F}{\partial x^2} - rF = 0
$$

Simplify:

$$
\boxed{\frac{\partial F}{\partial \tau} = \frac{1}{2}\sigma^2\frac{\partial^2 F}{\partial x^2}}
$$

This is the **heat equation** with thermal diffusivity $\kappa = \frac{1}{2}\sigma^2$.

---

## Initial Condition


The terminal condition $V(S,T) = (S-K)^+$ becomes an **initial condition** for $F$.

At $\tau = 0$ (maturity):
- $x = \log S$ (since $\tau = 0$ in the definition of $x$)
- $F(x,0) = V(S,T)e^{r \cdot 0} = V(S,T)$

For a European call:

$$
\boxed{F(x,0) = \psi(x) = \max(e^x - K, 0) = (e^x - K)^+}
$$

This is a piecewise function:

$$
\psi(x) = \begin{cases}
e^x - K & \text{if } x > \log K \\
0 & \text{if } x \leq \log K
\end{cases}
$$

**Summary**: We've transformed the **terminal-value problem** (BS PDE backward in time) into an **initial-value problem** (heat equation forward in time).

---

## Green's Function (Fundamental Solution)


### 1. **Definition**


The **fundamental solution** or **Green's function** of the heat equation is the solution to:

$$
\frac{\partial G}{\partial \tau} = \frac{1}{2}\sigma^2\frac{\partial^2 G}{\partial x^2}
$$

with initial condition:

$$
G(x,0; z) = \delta(x-z)
$$

where $\delta$ is the Dirac delta function (unit point source at $z$).

**Physical interpretation**: $G(x,\tau; z)$ represents the temperature distribution at position $x$ and time $\tau$ resulting from an instantaneous unit heat source placed at position $z$ at time $0$.

### 2. **Explicit Form**


The fundamental solution is:

$$
\boxed{G(x,\tau; z) = \frac{1}{\sqrt{2\pi\sigma^2\tau}}\exp\left(-\frac{(x-z)^2}{2\sigma^2\tau}\right)}
$$

This is a **Gaussian kernel** with:
- Mean: $z$ (centered at source location)
- Variance: $\sigma^2\tau$ (spreads with time)
- Normalization: $\int_{-\infty}^\infty G(x,\tau; z) dx = 1$

### 3. **Verification**


**Property 1** (Satisfies heat equation):

Direct calculation shows:

$$
\frac{\partial G}{\partial \tau} = \frac{1}{2}\sigma^2\frac{\partial^2 G}{\partial x^2}
$$

using standard Gaussian differentiation formulas.

**Property 2** (Initial condition):

$$
\lim_{\tau \to 0^+} G(x,\tau; z) = \delta(x-z)
$$

As $\tau \to 0$, the Gaussian concentrates at $z$.

**Property 3** (Probability conservation):

$$
\int_{-\infty}^\infty G(x,\tau; z) dx = 1 \quad \text{for all } \tau > 0
$$

### 4. **Intuition**


- At $\tau = 0$: All heat concentrated at point $z$
- As $\tau$ increases: Heat diffuses according to Gaussian spread
- As $\tau \to \infty$: Heat spreads everywhere uniformly

---

## Solution via Superposition


### 1. **Duhamel's Principle**


For any initial condition $\psi(x)$, the solution to the heat equation is obtained by **superposition** of fundamental solutions:

$$
\boxed{F(x,\tau) = \int_{-\infty}^\infty \psi(z) G(x,\tau; z) dz}
$$

Explicitly:

$$
F(x,\tau) = \int_{-\infty}^\infty \psi(z) \frac{1}{\sqrt{2\pi\sigma^2\tau}}\exp\left(-\frac{(x-z)^2}{2\sigma^2\tau}\right) dz
$$

**Interpretation**:
- Decompose initial condition $\psi(x)$ into point sources: $\psi(z)\delta(z)$
- Each point source at $z$ evolves according to $G(x,\tau; z)$
- The total solution is the **integral** (continuous sum) of all contributions

**Probabilistic view**: If $X \sim \mathcal{N}(x, \sigma^2\tau)$, then:

$$
F(x,\tau) = \mathbb{E}[\psi(X)] = \int_{-\infty}^\infty \psi(z) \cdot \text{pdf}(z; x, \sigma^2\tau) dz
$$

This connects the PDE solution to **expectation under Brownian motion**.

---

## Application to European Call


### 1. **Setup**


For a call option with $\psi(x) = (e^x - K)^+$:

$$
F(x,\tau) = \int_{-\infty}^\infty (e^z - K)^+ \frac{1}{\sqrt{2\pi\sigma^2\tau}}\exp\left(-\frac{(x-z)^2}{2\sigma^2\tau}\right) dz
$$

Since $(e^z - K)^+ = 0$ for $z \leq \log K$:

$$
F(x,\tau) = \int_{\log K}^\infty (e^z - K) \frac{1}{\sqrt{2\pi\sigma^2\tau}}\exp\left(-\frac{(x-z)^2}{2\sigma^2\tau}\right) dz
$$

### 2. **Split into Two Integrals**


$$
F(x,\tau) = \underbrace{\int_{\log K}^\infty e^z \frac{1}{\sqrt{2\pi\sigma^2\tau}}\exp\left(-\frac{(x-z)^2}{2\sigma^2\tau}\right) dz}_{I_1} - K\underbrace{\int_{\log K}^\infty \frac{1}{\sqrt{2\pi\sigma^2\tau}}\exp\left(-\frac{(x-z)^2}{2\sigma^2\tau}\right) dz}_{I_2}
$$

We evaluate each integral separately.

---

## Evaluation of I_2 (Strike Term)


$$
I_2 = \int_{\log K}^\infty \frac{1}{\sqrt{2\pi\sigma^2\tau}}\exp\left(-\frac{(x-z)^2}{2\sigma^2\tau}\right) dz
$$

This is a **Gaussian tail probability**. Define standard normal variable:

$$
Z = \frac{z - x}{\sigma\sqrt{\tau}} \sim \mathcal{N}(0,1)
$$

Then:

$$
\begin{aligned}
I_2 &= \mathbb{P}(z \geq \log K) \\
&= \mathbb{P}\left(\frac{z-x}{\sigma\sqrt{\tau}} \geq \frac{\log K - x}{\sigma\sqrt{\tau}}\right) \\
&= \mathbb{P}\left(Z \geq \frac{\log K - x}{\sigma\sqrt{\tau}}\right) \\
&= \mathbb{P}\left(Z \leq \frac{x - \log K}{\sigma\sqrt{\tau}}\right) \\
&= \mathcal{N}\left(\frac{x - \log K}{\sigma\sqrt{\tau}}\right)
\end{aligned}
$$

Define:

$$
\boxed{d_2 = \frac{x - \log K}{\sigma\sqrt{\tau}}}
$$

Therefore:

$$
I_2 = \mathcal{N}(d_2)
$$

---

## Evaluation of I_1 (Stock Term)


$$
I_1 = \int_{\log K}^\infty e^z \frac{1}{\sqrt{2\pi\sigma^2\tau}}\exp\left(-\frac{(x-z)^2}{2\sigma^2\tau}\right) dz
$$

**Key technique**: Complete the square in the exponent.

### 1. **Step 1: Combine Exponents**


$$
z - \frac{(x-z)^2}{2\sigma^2\tau} = -\frac{1}{2\sigma^2\tau}\left[(x-z)^2 - 2\sigma^2\tau z\right]
$$

Expand:

$$
(x-z)^2 - 2\sigma^2\tau z = z^2 - 2zx + x^2 - 2\sigma^2\tau z = z^2 - 2z(x + \sigma^2\tau) + x^2
$$

Complete the square:

$$
\begin{aligned}
&= [z - (x + \sigma^2\tau)]^2 - (x + \sigma^2\tau)^2 + x^2 \\
&= [z - (x + \sigma^2\tau)]^2 - 2x\sigma^2\tau - \sigma^4\tau^2
\end{aligned}
$$

Therefore:

$$
z - \frac{(x-z)^2}{2\sigma^2\tau} = -\frac{[z - (x+\sigma^2\tau)]^2}{2\sigma^2\tau} + x + \frac{\sigma^2\tau}{2}
$$

### 2. **Step 2: Factor Out Constant**


$$
I_1 = e^{x + \frac{\sigma^2\tau}{2}} \int_{\log K}^\infty \frac{1}{\sqrt{2\pi\sigma^2\tau}}\exp\left(-\frac{[z - (x+\sigma^2\tau)]^2}{2\sigma^2\tau}\right) dz
$$

The integral is a Gaussian tail probability with **shifted mean** $x + \sigma^2\tau$:

$$
\int_{\log K}^\infty \frac{1}{\sqrt{2\pi\sigma^2\tau}}\exp\left(-\frac{[z - (x+\sigma^2\tau)]^2}{2\sigma^2\tau}\right) dz = \mathbb{P}(W \geq \log K)
$$

where $W \sim \mathcal{N}(x+\sigma^2\tau, \sigma^2\tau)$.

### 3. **Step 3: Standardize**


$$
\begin{aligned}
\mathbb{P}(W \geq \log K) &= \mathbb{P}\left(\frac{W - (x+\sigma^2\tau)}{\sigma\sqrt{\tau}} \geq \frac{\log K - (x+\sigma^2\tau)}{\sigma\sqrt{\tau}}\right) \\
&= \mathbb{P}\left(Z \geq \frac{\log K - x - \sigma^2\tau}{\sigma\sqrt{\tau}}\right) \\
&= \mathcal{N}\left(\frac{x + \sigma^2\tau - \log K}{\sigma\sqrt{\tau}}\right)
\end{aligned}
$$

Define:

$$
\boxed{d_1 = \frac{x + \sigma^2\tau - \log K}{\sigma\sqrt{\tau}} = d_2 + \sigma\sqrt{\tau}}
$$

Therefore:

$$
I_1 = e^{x + \frac{\sigma^2\tau}{2}}\mathcal{N}(d_1)
$$

---

## Synthesis: Black-Scholes Formula


### 1. **Forward Value**


Combining $I_1$ and $I_2$:

$$
F(x,\tau) = e^{x + \frac{\sigma^2\tau}{2}}\mathcal{N}(d_1) - K\mathcal{N}(d_2)
$$

### 2. **Transform Back to Original Variables**


Recall:
- $x = \log S + (r - \frac{1}{2}\sigma^2)\tau$
- $e^x = Se^{(r - \frac{1}{2}\sigma^2)\tau}$

Therefore:

$$
e^{x + \frac{\sigma^2\tau}{2}} = Se^{(r - \frac{1}{2}\sigma^2)\tau + \frac{\sigma^2\tau}{2}} = Se^{r\tau}
$$

Substituting:

$$
F(x,\tau) = Se^{r\tau}\mathcal{N}(d_1) - K\mathcal{N}(d_2)
$$

### 3. **Discount Back**


Since $V = Fe^{-r\tau}$:

$$
\boxed{V(S,t) = S\mathcal{N}(d_1) - Ke^{-r\tau}\mathcal{N}(d_2)}
$$

where $\tau = T - t$ and:

$$
\boxed{d_1 = \frac{\log(S/K) + (r + \frac{1}{2}\sigma^2)\tau}{\sigma\sqrt{\tau}}}
$$

$$
\boxed{d_2 = d_1 - \sigma\sqrt{\tau} = \frac{\log(S/K) + (r - \frac{1}{2}\sigma^2)\tau}{\sigma\sqrt{\tau}}}
$$

This is the **Black-Scholes formula** for a European call option.

---

## Interpretation


### 1. **Probabilistic Meaning**


$$
C = S_0\mathcal{N}(d_1) - Ke^{-rT}\mathcal{N}(d_2)
$$

**Term 1**: $S_0\mathcal{N}(d_1)$
- Expected stock value **conditional on exercise** under the stock measure
- $\mathcal{N}(d_1)$ is the probability of exercise under a measure where the stock is the numeraire

**Term 2**: $Ke^{-rT}\mathcal{N}(d_2)$
- Expected discounted strike payment
- $\mathcal{N}(d_2)$ is the probability of exercise under the risk-neutral measure

### 2. **Connection to Diffusion**


The heat equation derivation reveals:
- Option pricing ≡ Diffusion of payoff backward in time
- Green's function = Transition density of log-price under Brownian motion
- Black-Scholes formula = Weighted average of terminal payoffs over Gaussian distribution

**Physical analogy**: If the option payoff were a temperature distribution at maturity, the current value is how that temperature has "diffused backward in time."

---

## Summary


The heat equation approach provides a complete analytical derivation of the Black-Scholes formula:

### 1. **Key Steps**


1. **Transform**: BS PDE → Heat equation via change of variables $(S,t) \to (x,\tau)$ and $V \to F$

2. **Recognize**: Heat equation has known Green's function (Gaussian kernel)

3. **Apply superposition**: Solution is convolution of initial condition with Green's function

4. **Evaluate integrals**: Use completing the square for Gaussian integrals

5. **Transform back**: Return to original variables $(S,t)$ and discount

### 2. **Advantages**


- **Explicit solution**: Closed-form formula obtained analytically
- **Clear probabilistic interpretation**: Connection to Brownian motion apparent
- **Classical PDE theory**: Connects to well-studied heat/diffusion equations
- **Generalizable**: Extends to other parabolic PDEs and payoffs

### 3. **Limitations**


- **European options only**: Requires fixed terminal condition
- **Smooth payoffs work best**: Discontinuous payoffs require distribution theory
- **Limited flexibility**: Less adaptable than numerical methods for exotics

### 4. **Theoretical Significance**


This derivation reveals the fundamental triad in quantitative finance:

```
Stochastic Processes (Brownian motion)
         ↕
    PDE Theory (Heat equation)
         ↕
  Probability (Gaussian distributions)
```

The heat equation method demonstrates that these three perspectives are **mathematically equivalent**, each providing complementary insights into derivative pricing.

### 5. **What the kernel really is**

The Gaussian kernel $G(x,\tau;z)$ used throughout this derivation is exactly the **transition density** of Brownian motion with drift $(r - \frac{1}{2}\sigma^2)$ and diffusion coefficient $\sigma$. The convolution integral

$$
F(x,\tau) = \int_{-\infty}^{\infty} \psi(z)\, G(x,\tau;z)\, dz
$$

is therefore an **expectation**: the expected payoff under the risk-neutral measure. This is not a coincidence. The Feynman-Kac theorem (developed later in this chapter) establishes that solutions of parabolic PDEs are *always* expressible as such expectations. Put differently: the heat equation approach and the probabilistic approach compute exactly the same object --- the convolution *is* the expectation, and the Green's function *is* the transition density. Recognizing this equivalence is essential, because it means every PDE method in this chapter has a probabilistic counterpart, and vice versa. In the operator language of the introduction, the convolution with $G$ is the **kernel representation** of the pricing semigroup $\mathcal{P}_\tau = e^{\tau\mathcal{L}}$.

---

## Exercises

**Exercise 1.** Verify that the Green's function $G(x,\tau;z) = \frac{1}{\sqrt{2\pi\sigma^2\tau}}\exp\left(-\frac{(x-z)^2}{2\sigma^2\tau}\right)$ satisfies the heat equation $\frac{\partial G}{\partial \tau} = \frac{1}{2}\sigma^2 \frac{\partial^2 G}{\partial x^2}$ by computing both sides explicitly and showing they are equal.

??? success "Solution to Exercise 1"
    The Green's function is $G(x,\tau;z) = \frac{1}{\sqrt{2\pi\sigma^2\tau}}\exp\left(-\frac{(x-z)^2}{2\sigma^2\tau}\right)$.

    **Compute the left side** $\frac{\partial G}{\partial \tau}$. Let $u = \frac{(x-z)^2}{2\sigma^2\tau}$. Then:

    $$
    G = (2\pi\sigma^2\tau)^{-1/2} e^{-u}
    $$

    $$
    \frac{\partial G}{\partial \tau} = -\frac{1}{2\tau}G + G \cdot \frac{(x-z)^2}{2\sigma^2\tau^2} = G\left[-\frac{1}{2\tau} + \frac{(x-z)^2}{2\sigma^2\tau^2}\right]
    $$

    **Compute the right side** $\frac{1}{2}\sigma^2\frac{\partial^2 G}{\partial x^2}$. First:

    $$
    \frac{\partial G}{\partial x} = G \cdot \left(-\frac{x-z}{\sigma^2\tau}\right)
    $$

    $$
    \frac{\partial^2 G}{\partial x^2} = G \cdot \frac{(x-z)^2}{\sigma^4\tau^2} + G \cdot \left(-\frac{1}{\sigma^2\tau}\right) = G\left[\frac{(x-z)^2}{\sigma^4\tau^2} - \frac{1}{\sigma^2\tau}\right]
    $$

    Therefore:

    $$
    \frac{1}{2}\sigma^2\frac{\partial^2 G}{\partial x^2} = G\left[\frac{(x-z)^2}{2\sigma^2\tau^2} - \frac{1}{2\tau}\right]
    $$

    This equals $\frac{\partial G}{\partial \tau}$, confirming that $G$ satisfies the heat equation.

---
**Exercise 2.** Derive the Black-Scholes put formula using the heat equation approach. Start from the initial condition $\psi(x) = (K - e^x)^+$ and evaluate the two resulting Gaussian integrals. Verify that your answer matches the put formula $P = Ke^{-r\tau}\mathcal{N}(-d_2) - S\mathcal{N}(-d_1)$.

??? success "Solution to Exercise 2"
    For the European put, the initial condition is $\psi(x) = (K - e^x)^+ = K - e^x$ for $x < \ln K$ and $0$ for $x \geq \ln K$.

    The superposition integral is:

    $$
    F(x,\tau) = \int_{-\infty}^{\ln K}(K - e^z)\frac{1}{\sqrt{2\pi\sigma^2\tau}}\exp\left(-\frac{(x-z)^2}{2\sigma^2\tau}\right)dz
    $$

    Split into two integrals:

    $$
    F = K\underbrace{\int_{-\infty}^{\ln K}\frac{1}{\sqrt{2\pi\sigma^2\tau}}e^{-(x-z)^2/(2\sigma^2\tau)}dz}_{J_2} - \underbrace{\int_{-\infty}^{\ln K}e^z \frac{1}{\sqrt{2\pi\sigma^2\tau}}e^{-(x-z)^2/(2\sigma^2\tau)}dz}_{J_1}
    $$

    **Integral $J_2$:** With the substitution $Z = (z-x)/(\sigma\sqrt{\tau})$:

    $$
    J_2 = \mathbb{P}\left(Z \leq \frac{\ln K - x}{\sigma\sqrt{\tau}}\right) = \mathcal{N}\left(\frac{\ln K - x}{\sigma\sqrt{\tau}}\right) = \mathcal{N}(-d_2)
    $$

    **Integral $J_1$:** By the same completing-the-square technique as for the call:

    $$
    J_1 = e^{x + \sigma^2\tau/2}\mathcal{N}\left(\frac{\ln K - x - \sigma^2\tau}{\sigma\sqrt{\tau}}\right) = e^{x+\sigma^2\tau/2}\mathcal{N}(-d_1)
    $$

    Therefore:

    $$
    F(x,\tau) = K\mathcal{N}(-d_2) - e^{x+\sigma^2\tau/2}\mathcal{N}(-d_1)
    $$

    Transforming back with $e^{x+\sigma^2\tau/2} = Se^{r\tau}$ and $V = Fe^{-r\tau}$:

    $$
    P(S,t) = Ke^{-r\tau}\mathcal{N}(-d_2) - S\mathcal{N}(-d_1)
    $$

    This matches the standard put formula.

---
**Exercise 3.** In the transformation from the BS PDE to the heat equation, the first-order term cancels. Show this cancellation in detail: substitute the transformed derivatives into the PDE and verify that all $\frac{\partial V}{\partial x}$ terms cancel exactly.

??? success "Solution to Exercise 3"
    The transformed derivatives yield the following first-order terms in the PDE:

    $$
    -\left(r - \frac{1}{2}\sigma^2\right)\frac{\partial V}{\partial x} + r\frac{\partial V}{\partial x} - \frac{1}{2}\sigma^2\frac{\partial V}{\partial x}
    $$

    The first term comes from the time derivative transformation ($\frac{\partial V}{\partial t}$ contribution). The second term comes from the $rS\frac{\partial V}{\partial S} = r\frac{\partial V}{\partial x}$ term. The third term comes from the second-order term: $\frac{1}{2}\sigma^2 S^2\frac{\partial^2 V}{\partial S^2} = \frac{1}{2}\sigma^2\left(\frac{\partial^2 V}{\partial x^2} - \frac{\partial V}{\partial x}\right)$, contributing $-\frac{1}{2}\sigma^2\frac{\partial V}{\partial x}$.

    Summing all first-order coefficients:

    $$
    -r + \frac{1}{2}\sigma^2 + r - \frac{1}{2}\sigma^2 = 0
    $$

    The cancellation is exact. This happens because the transformation $x = \ln S + (r - \frac{1}{2}\sigma^2)\tau$ was specifically designed to incorporate the risk-neutral drift, thereby eliminating the convection (first-order) term from the PDE.

---
**Exercise 4.** The three transformations $(\tau, x, F)$ reduce the BS PDE to the heat equation with diffusivity $\kappa = \frac{1}{2}\sigma^2$. If we instead define $y = x / (\sigma\sqrt{2})$ and $F(y,\tau)$, show that we obtain the standard heat equation $\frac{\partial F}{\partial \tau} = \frac{\partial^2 F}{\partial y^2}$ with unit diffusivity. Express $d_1$ and $d_2$ in terms of $y$ and $\tau$.

??? success "Solution to Exercise 4"
    Define $y = x/(\sigma\sqrt{2})$. Then $x = \sigma\sqrt{2}\,y$ and:

    $$
    \frac{\partial F}{\partial y} = \frac{\partial F}{\partial x}\frac{\partial x}{\partial y} = \sigma\sqrt{2}\frac{\partial F}{\partial x}
    $$

    $$
    \frac{\partial^2 F}{\partial y^2} = 2\sigma^2\frac{\partial^2 F}{\partial x^2}
    $$

    Substituting into $\frac{\partial F}{\partial \tau} = \frac{1}{2}\sigma^2\frac{\partial^2 F}{\partial x^2}$:

    $$
    \frac{\partial F}{\partial \tau} = \frac{1}{2}\sigma^2 \cdot \frac{1}{2\sigma^2}\frac{\partial^2 F}{\partial y^2} = \frac{1}{2} \cdot \frac{1}{2}\frac{\partial^2 F}{\partial y^2}
    $$

    This gives $\frac{\partial F}{\partial \tau} = \frac{1}{4}\frac{\partial^2 F}{\partial y^2}$, not unit diffusivity. To obtain the standard form $\frac{\partial F}{\partial \tau} = \frac{\partial^2 F}{\partial y^2}$, introduce a time rescaling $\tilde{\tau} = \frac{1}{2}\sigma^2\tau$:

    $$
    \frac{\partial F}{\partial \tilde{\tau}} = \frac{1}{\frac{1}{2}\sigma^2}\frac{\partial F}{\partial \tau} = \frac{1}{\frac{1}{2}\sigma^2}\cdot\frac{1}{2}\sigma^2\frac{\partial^2 F}{\partial x^2} = \frac{\partial^2 F}{\partial x^2}
    $$

    So with $y = x$ and $\tilde{\tau} = \frac{1}{2}\sigma^2\tau$, we obtain unit diffusivity. In these variables:

    $$
    d_1 = \frac{x + \sigma^2\tau - \ln K}{\sigma\sqrt{\tau}} = \frac{x + 2\tilde{\tau} - \ln K}{\sqrt{2\tilde{\tau}}}
    $$

    $$
    d_2 = \frac{x - \ln K}{\sigma\sqrt{\tau}} = \frac{x - \ln K}{\sqrt{2\tilde{\tau}}}
    $$

---
**Exercise 5.** Use the superposition integral to price a **digital call** with payoff $\psi(x) = \mathbf{1}_{\{e^x > K\}} = \mathbf{1}_{\{x > \ln K\}}$. Evaluate the resulting Gaussian integral and transform back to original variables to obtain $D_0 = e^{-rT}\mathcal{N}(d_2)$.

??? success "Solution to Exercise 5"
    The digital call payoff is $\psi(x) = \mathbf{1}_{\{x > \ln K\}}$. The superposition integral gives:

    $$
    F(x,\tau) = \int_{\ln K}^{\infty}\frac{1}{\sqrt{2\pi\sigma^2\tau}}\exp\left(-\frac{(x-z)^2}{2\sigma^2\tau}\right)dz
    $$

    This is a standard Gaussian tail probability. With $Z = (z - x)/(\sigma\sqrt{\tau})$:

    $$
    F(x,\tau) = \mathbb{P}\left(Z \geq \frac{\ln K - x}{\sigma\sqrt{\tau}}\right) = \mathcal{N}\left(\frac{x - \ln K}{\sigma\sqrt{\tau}}\right) = \mathcal{N}(d_2)
    $$

    where $d_2 = \frac{x - \ln K}{\sigma\sqrt{\tau}}$.

    Transforming back to original variables: $x = \ln S + (r - \frac{1}{2}\sigma^2)\tau$, so:

    $$
    d_2 = \frac{\ln S + (r - \frac{1}{2}\sigma^2)\tau - \ln K}{\sigma\sqrt{\tau}} = \frac{\ln(S/K) + (r - \frac{1}{2}\sigma^2)\tau}{\sigma\sqrt{\tau}}
    $$

    Since $V = Fe^{-r\tau}$ and $F = \mathcal{N}(d_2)$:

    $$
    D_0 = e^{-rT}\mathcal{N}(d_2)
    $$

    This is the price of a digital (cash-or-nothing) call paying \$1 if $S_T > K$.

---
**Exercise 6.** The heat equation approach requires the initial condition $\psi(x) = (e^x - K)^+$ to be integrable against the Green's function. Discuss what happens if the payoff grows faster than $e^{|x|}$ as $|x| \to \infty$. Give an example of a payoff for which the superposition integral diverges, and explain what this means financially.

??? success "Solution to Exercise 6"
    The superposition integral is $F(x,\tau) = \int_{-\infty}^{\infty}\psi(z)G(x,\tau;z)dz$ where $G$ is the Gaussian kernel with variance $\sigma^2\tau$.

    **Growth condition.** For the integral to converge, we need:

    $$
    \int_{-\infty}^{\infty}|\psi(z)| \cdot \frac{1}{\sqrt{2\pi\sigma^2\tau}}e^{-(x-z)^2/(2\sigma^2\tau)}dz < \infty
    $$

    The Gaussian kernel decays as $e^{-z^2/(2\sigma^2\tau)}$ for large $|z|$, so $\psi(z)$ can grow at most as $e^{cz^2}$ for some $c < 1/(2\sigma^2\tau)$ and the integral still converges. In particular, any payoff growing as $e^{\alpha|z|}$ (polynomial exponential growth) is integrable.

    **Divergent example.** Consider the payoff $\psi(z) = e^{z^2}$ (super-exponential growth). The integral becomes:

    $$
    \int_{-\infty}^{\infty}e^{z^2}\frac{1}{\sqrt{2\pi\sigma^2\tau}}e^{-(x-z)^2/(2\sigma^2\tau)}dz
    $$

    The exponent grows as $z^2 - z^2/(2\sigma^2\tau) = z^2(1 - 1/(2\sigma^2\tau))$. For $\tau > 1/(2\sigma^2)$, the coefficient is positive and the integral diverges.

    **Financial interpretation.** A payoff that grows faster than exponentially in $\ln S$ (i.e., super-polynomially in $S$) cannot be priced using the standard Green's function approach because the expected payoff under the risk-neutral measure is infinite. Such payoffs violate the integrability conditions needed for the risk-neutral pricing formula to hold. Financially, no finite amount of capital can replicate such a payoff, so it has no well-defined arbitrage-free price. The standard call payoff $(e^x - K)^+$ grows only as $e^x$ (linearly in $S$), which is within the allowable growth rate.
