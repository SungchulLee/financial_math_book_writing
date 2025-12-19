# Black-Scholes Formula via Heat Equation

The Black-Scholes PDE can be transformed into the **heat equation**, one of the most studied partial differential equations in mathematical physics. This transformation allows us to leverage the well-known fundamental solution (Green's function) to derive the Black-Scholes formula analytically.

This approach reveals the deep connection between option pricing and diffusion processes, demonstrating how financial derivatives can be priced using classical PDE techniques.

---

## 1. The Black-Scholes PDE

### **Standard Form**

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

## 2. Change of Variables

We apply three transformations to reduce the BS PDE to canonical heat equation form.

### **Transformation 1: Time to Maturity**

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

### **Transformation 2: Expected Log-Price**

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

### **Transformation 3: Forward Option Value**

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

## 3. Transformation of Derivatives

### **Time Derivative**

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

### **First Spatial Derivative**

$$
\frac{\partial V}{\partial S} = \frac{\partial V}{\partial x}\frac{\partial x}{\partial S} = \frac{\partial V}{\partial x} \cdot \frac{1}{S}
$$

### **Second Spatial Derivative**

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

## 4. Derivation of the Heat Equation

### **Step 1: Substitute into BS PDE**

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

### **Step 2: Collect Terms**

Grouping by derivative order:

- **Second-order**: $\frac{1}{2}\sigma^2\frac{\partial^2 V}{\partial x^2}$
- **First-order**: $-\left(r - \frac{1}{2}\sigma^2\right)\frac{\partial V}{\partial x} - \frac{1}{2}\sigma^2\frac{\partial V}{\partial x} + r\frac{\partial V}{\partial x} = 0$ (cancels!)
- **Zero-order**: $-\frac{\partial V}{\partial \tau} - rV = 0$

Result:
$$
-\frac{\partial V}{\partial \tau} + \frac{1}{2}\sigma^2\frac{\partial^2 V}{\partial x^2} - rV = 0
$$

### **Step 3: Eliminate $-rV$ Term**

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

## 5. Initial Condition

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

## 6. Green's Function (Fundamental Solution)

### **Definition**

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

### **Explicit Form**

The fundamental solution is:

$$
\boxed{G(x,\tau; z) = \frac{1}{\sqrt{2\pi\sigma^2\tau}}\exp\left(-\frac{(x-z)^2}{2\sigma^2\tau}\right)}
$$

This is a **Gaussian kernel** with:
- Mean: $z$ (centered at source location)
- Variance: $\sigma^2\tau$ (spreads with time)
- Normalization: $\int_{-\infty}^\infty G(x,\tau; z) dx = 1$

### **Verification**

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

### **Intuition**

- At $\tau = 0$: All heat concentrated at point $z$
- As $\tau$ increases: Heat diffuses according to Gaussian spread
- As $\tau \to \infty$: Heat spreads everywhere uniformly

---

## 7. Solution via Superposition

### **Duhamel's Principle**

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

## 8. Application to European Call

### **Setup**

For a call option with $\psi(x) = (e^x - K)^+$:

$$
F(x,\tau) = \int_{-\infty}^\infty (e^z - K)^+ \frac{1}{\sqrt{2\pi\sigma^2\tau}}\exp\left(-\frac{(x-z)^2}{2\sigma^2\tau}\right) dz
$$

Since $(e^z - K)^+ = 0$ for $z \leq \log K$:

$$
F(x,\tau) = \int_{\log K}^\infty (e^z - K) \frac{1}{\sqrt{2\pi\sigma^2\tau}}\exp\left(-\frac{(x-z)^2}{2\sigma^2\tau}\right) dz
$$

### **Split into Two Integrals**

$$
F(x,\tau) = \underbrace{\int_{\log K}^\infty e^z \frac{1}{\sqrt{2\pi\sigma^2\tau}}\exp\left(-\frac{(x-z)^2}{2\sigma^2\tau}\right) dz}_{I_1} - K\underbrace{\int_{\log K}^\infty \frac{1}{\sqrt{2\pi\sigma^2\tau}}\exp\left(-\frac{(x-z)^2}{2\sigma^2\tau}\right) dz}_{I_2}
$$

We evaluate each integral separately.

---

## 9. Evaluation of $I_2$ (Strike Term)

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

## 10. Evaluation of $I_1$ (Stock Term)

$$
I_1 = \int_{\log K}^\infty e^z \frac{1}{\sqrt{2\pi\sigma^2\tau}}\exp\left(-\frac{(x-z)^2}{2\sigma^2\tau}\right) dz
$$

**Key technique**: Complete the square in the exponent.

### **Step 1: Combine Exponents**

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

### **Step 2: Factor Out Constant**

$$
I_1 = e^{x + \frac{\sigma^2\tau}{2}} \int_{\log K}^\infty \frac{1}{\sqrt{2\pi\sigma^2\tau}}\exp\left(-\frac{[z - (x+\sigma^2\tau)]^2}{2\sigma^2\tau}\right) dz
$$

The integral is a Gaussian tail probability with **shifted mean** $x + \sigma^2\tau$:

$$
\int_{\log K}^\infty \frac{1}{\sqrt{2\pi\sigma^2\tau}}\exp\left(-\frac{[z - (x+\sigma^2\tau)]^2}{2\sigma^2\tau}\right) dz = \mathbb{P}(W \geq \log K)
$$

where $W \sim \mathcal{N}(x+\sigma^2\tau, \sigma^2\tau)$.

### **Step 3: Standardize**

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

## 11. Synthesis: Black-Scholes Formula

### **Forward Value**

Combining $I_1$ and $I_2$:
$$
F(x,\tau) = e^{x + \frac{\sigma^2\tau}{2}}\mathcal{N}(d_1) - K\mathcal{N}(d_2)
$$

### **Transform Back to Original Variables**

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

### **Discount Back**

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

## 12. Interpretation

### **Probabilistic Meaning**

$$
C = S_0\mathcal{N}(d_1) - Ke^{-rT}\mathcal{N}(d_2)
$$

**Term 1**: $S_0\mathcal{N}(d_1)$
- Expected stock value **conditional on exercise** under the stock measure
- $\mathcal{N}(d_1)$ is the probability of exercise under a measure where the stock is the numeraire

**Term 2**: $Ke^{-rT}\mathcal{N}(d_2)$
- Expected discounted strike payment
- $\mathcal{N}(d_2)$ is the probability of exercise under the risk-neutral measure

### **Connection to Diffusion**

The heat equation derivation reveals:
- Option pricing ≡ Diffusion of payoff backward in time
- Green's function = Transition density of log-price under Brownian motion
- Black-Scholes formula = Weighted average of terminal payoffs over Gaussian distribution

**Physical analogy**: If the option payoff were a temperature distribution at maturity, the current value is how that temperature has "diffused backward in time."

---

## 13. Summary

The heat equation approach provides a complete analytical derivation of the Black-Scholes formula:

### **Key Steps**

1. **Transform**: BS PDE → Heat equation via change of variables $(S,t) \to (x,\tau)$ and $V \to F$

2. **Recognize**: Heat equation has known Green's function (Gaussian kernel)

3. **Apply superposition**: Solution is convolution of initial condition with Green's function

4. **Evaluate integrals**: Use completing the square for Gaussian integrals

5. **Transform back**: Return to original variables $(S,t)$ and discount

### **Advantages**

- **Explicit solution**: Closed-form formula obtained analytically
- **Clear probabilistic interpretation**: Connection to Brownian motion apparent
- **Classical PDE theory**: Connects to well-studied heat/diffusion equations
- **Generalizable**: Extends to other parabolic PDEs and payoffs

### **Limitations**

- **European options only**: Requires fixed terminal condition
- **Smooth payoffs work best**: Discontinuous payoffs require distribution theory
- **Limited flexibility**: Less adaptable than numerical methods for exotics

### **Theoretical Significance**

This derivation reveals the fundamental triad in quantitative finance:

```
Stochastic Processes (Brownian motion)
         ↕
    PDE Theory (Heat equation)
         ↕
  Probability (Gaussian distributions)
```

The heat equation method demonstrates that these three perspectives are **mathematically equivalent**, each providing complementary insights into derivative pricing.
