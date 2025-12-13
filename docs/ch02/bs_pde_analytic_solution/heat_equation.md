# Heat Equation Transformation: Complete Mathematical Treatment

This is one of the most elegant approaches to solving the Black-Scholes PDE—transforming it into the standard heat equation through a sequence of clever variable changes.

---

## **1. The Black-Scholes PDE**

Starting point for a European option $V(S,t)$:

$$\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} - rV = 0$$

**Terminal condition**: $V(S,T) = \Phi(S)$ (payoff function)

**Goal**: Transform this into the heat equation:
$$\frac{\partial u}{\partial \tau} = \frac{\partial^2 u}{\partial x^2}$$

---

## **2. First Transformation: Logarithmic Variables**

### **Step 1: Change Independent Variables**

Define:
$$x = \ln\left(\frac{S}{K}\right), \quad \tau = \frac{\sigma^2}{2}(T - t)$$

**Rationale**: 
- $x$ transforms the multiplicative stock price to additive log-returns
- $\tau$ is "time-to-expiry" scaled by variance
- At expiry: $\tau = 0$, and as $t \to -\infty$, $\tau \to \infty$

### **Step 2: Compute Partial Derivatives**

Chain rule for $V(S,t) = V(S(x), t(\tau))$:

$$\frac{\partial V}{\partial S} = \frac{\partial V}{\partial x}\frac{\partial x}{\partial S} = \frac{1}{S}\frac{\partial V}{\partial x}$$

$$\frac{\partial^2 V}{\partial S^2} = \frac{\partial}{\partial S}\left(\frac{1}{S}\frac{\partial V}{\partial x}\right) = -\frac{1}{S^2}\frac{\partial V}{\partial x} + \frac{1}{S}\frac{\partial}{\partial S}\left(\frac{\partial V}{\partial x}\right)$$

$$= -\frac{1}{S^2}\frac{\partial V}{\partial x} + \frac{1}{S^2}\frac{\partial^2 V}{\partial x^2}$$

For time:
$$\frac{\partial V}{\partial t} = \frac{\partial V}{\partial \tau}\frac{\partial \tau}{\partial t} = -\frac{\sigma^2}{2}\frac{\partial V}{\partial \tau}$$

### **Step 3: Substitute into PDE**

$$-\frac{\sigma^2}{2}\frac{\partial V}{\partial \tau} + rS \cdot \frac{1}{S}\frac{\partial V}{\partial x} + \frac{1}{2}\sigma^2 S^2 \left(\frac{1}{S^2}\frac{\partial^2 V}{\partial x^2} - \frac{1}{S^2}\frac{\partial V}{\partial x}\right) - rV = 0$$

$$-\frac{\sigma^2}{2}\frac{\partial V}{\partial \tau} + r\frac{\partial V}{\partial x} + \frac{\sigma^2}{2}\frac{\partial^2 V}{\partial x^2} - \frac{\sigma^2}{2}\frac{\partial V}{\partial x} - rV = 0$$

Multiply by $-\frac{2}{\sigma^2}$:

$$\frac{\partial V}{\partial \tau} = \frac{\partial^2 V}{\partial x^2} + \left(k-1\right)\frac{\partial V}{\partial x} - kV$$

where we define:
$$\boxed{k = \frac{2r}{\sigma^2}}$$

### **Step 4: Dimensionless Form**

To make $V$ dimensionless, set:
$$u(x,\tau) = \frac{V(S,t)}{K}$$

Then:
$$\boxed{\frac{\partial u}{\partial \tau} = \frac{\partial^2 u}{\partial x^2} + (k-1)\frac{\partial u}{\partial x} - ku}$$

**Terminal condition** ($\tau = 0$, i.e., $t = T$):
$$u(x,0) = \frac{\Phi(Ke^x)}{K} = \phi(x)$$

For a call: $\phi(x) = \max(e^x - 1, 0)$

---

## **3. Second Transformation: Eliminating First-Order Term**

The equation still has drift and decay terms. We eliminate these through an exponential transformation.

### **Ansatz**

Seek a solution of the form:
$$u(x,\tau) = e^{\alpha x + \beta \tau}w(x,\tau)$$

where $\alpha, \beta$ are constants to be determined.

### **Computing Derivatives**

$$\frac{\partial u}{\partial \tau} = e^{\alpha x + \beta \tau}\left(\frac{\partial w}{\partial \tau} + \beta w\right)$$

$$\frac{\partial u}{\partial x} = e^{\alpha x + \beta \tau}\left(\frac{\partial w}{\partial x} + \alpha w\right)$$

$$\frac{\partial^2 u}{\partial x^2} = e^{\alpha x + \beta \tau}\left(\frac{\partial^2 w}{\partial x^2} + 2\alpha \frac{\partial w}{\partial x} + \alpha^2 w\right)$$

### **Substituting into the PDE**

$$e^{\alpha x + \beta \tau}\left(\frac{\partial w}{\partial \tau} + \beta w\right) = e^{\alpha x + \beta \tau}\left[\frac{\partial^2 w}{\partial x^2} + 2\alpha \frac{\partial w}{\partial x} + \alpha^2 w + (k-1)\left(\frac{\partial w}{\partial x} + \alpha w\right) - kw\right]$$

Divide by $e^{\alpha x + \beta \tau}$:

$$\frac{\partial w}{\partial \tau} + \beta w = \frac{\partial^2 w}{\partial x^2} + [2\alpha + (k-1)]\frac{\partial w}{\partial x} + [\alpha^2 + (k-1)\alpha - k]w$$

### **Choosing $\alpha$ and $\beta$**

To obtain the standard heat equation, we need:

1. **Coefficient of $\frac{\partial w}{\partial x}$ equals zero**:
$$2\alpha + (k-1) = 0 \quad \Rightarrow \quad \boxed{\alpha = -\frac{k-1}{2}}$$

2. **Coefficient of $w$ equals zero**:
$$\beta = \alpha^2 + (k-1)\alpha - k$$

Substituting $\alpha = -\frac{k-1}{2}$:
$$\beta = \frac{(k-1)^2}{4} - \frac{(k-1)^2}{2} - k = -\frac{(k-1)^2}{4} - k$$

$$= -\frac{(k-1)^2 + 4k}{4} = -\frac{k^2 - 2k + 1 + 4k}{4} = -\frac{k^2 + 2k + 1}{4}$$

$$\boxed{\beta = -\frac{(k+1)^2}{4}}$$

### **The Standard Heat Equation**

With these choices:
$$\boxed{\frac{\partial w}{\partial \tau} = \frac{\partial^2 w}{\partial x^2}}$$

This is the **standard diffusion equation**!

### **Transformation Summary**

$$\boxed{u(x,\tau) = e^{-\frac{k-1}{2}x - \frac{(k+1)^2}{4}\tau}w(x,\tau)}$$

or equivalently:

$$\boxed{w(x,\tau) = e^{\frac{k-1}{2}x + \frac{(k+1)^2}{4}\tau}u(x,\tau)}$$

---

## **4. Initial/Terminal Condition for $w$**

At $\tau = 0$ (expiry):
$$w(x,0) = e^{\frac{k-1}{2}x}u(x,0) = e^{\frac{k-1}{2}x}\phi(x)$$

**For a call option**: $\phi(x) = (e^x - 1)^+$

$$w(x,0) = \begin{cases}
e^{\frac{k-1}{2}x}(e^x - 1) = e^{\frac{k+1}{2}x} - e^{\frac{k-1}{2}x} & \text{if } x > 0 \\
0 & \text{if } x \leq 0
\end{cases}$$

**For a put option**: $\phi(x) = (1 - e^x)^+$

$$w(x,0) = \begin{cases}
e^{\frac{k-1}{2}x}(1 - e^x) = e^{\frac{k-1}{2}x} - e^{\frac{k+1}{2}x} & \text{if } x < 0 \\
0 & \text{if } x \geq 0
\end{cases}$$

---

## **5. Solution of the Heat Equation**

### **Fundamental Solution (Green's Function)**

The heat equation $\frac{\partial w}{\partial \tau} = \frac{\partial^2 w}{\partial x^2}$ with initial condition $w(x,0) = f(x)$ has solution:

$$w(x,\tau) = \int_{-\infty}^{\infty} G(x-y,\tau)f(y)dy$$

where the **fundamental solution** is:

$$\boxed{G(x,\tau) = \frac{1}{\sqrt{4\pi\tau}}e^{-\frac{x^2}{4\tau}}}$$

This is the **heat kernel** or **Gaussian kernel**.

### **Verification**

We can verify $G$ satisfies the heat equation:

$$\frac{\partial G}{\partial \tau} = \frac{1}{\sqrt{4\pi}}\frac{\partial}{\partial \tau}\left(\tau^{-1/2}e^{-\frac{x^2}{4\tau}}\right)$$

$$= \frac{1}{\sqrt{4\pi}}\left[-\frac{1}{2}\tau^{-3/2}e^{-\frac{x^2}{4\tau}} + \tau^{-1/2}e^{-\frac{x^2}{4\tau}}\frac{x^2}{4\tau^2}\right]$$

$$= G\left[-\frac{1}{2\tau} + \frac{x^2}{4\tau^2}\right] = G\frac{x^2 - 2\tau}{4\tau^2}$$

$$\frac{\partial^2 G}{\partial x^2} = \frac{\partial}{\partial x}\left(G \cdot \frac{-x}{2\tau}\right) = G\frac{x^2}{4\tau^2} - G\frac{1}{2\tau}$$

Indeed: $\frac{\partial G}{\partial \tau} = \frac{\partial^2 G}{\partial x^2}$ ✓

### **Initial Condition Property**

$$\lim_{\tau \to 0^+}G(x-y,\tau) = \delta(x-y)$$

where $\delta$ is the Dirac delta function. This gives:
$$\lim_{\tau \to 0^+}w(x,\tau) = f(x)$$

---

## **6. Explicit Solution for Call Option**

### **Setup**

For the call, we need:
$$w(x,\tau) = \int_0^{\infty}\left[e^{\frac{k+1}{2}y} - e^{\frac{k-1}{2}y}\right]G(x-y,\tau)dy$$

$$= \int_0^{\infty}e^{\frac{k+1}{2}y}G(x-y,\tau)dy - \int_0^{\infty}e^{\frac{k-1}{2}y}G(x-y,\tau)dy$$

Define:
$$I_n = \int_0^{\infty}e^{ny}G(x-y,\tau)dy = \int_0^{\infty}e^{ny}\frac{1}{\sqrt{4\pi\tau}}e^{-\frac{(x-y)^2}{4\tau}}dy$$

### **Evaluating $I_n$**

$$I_n = \frac{1}{\sqrt{4\pi\tau}}\int_0^{\infty}\exp\left[ny - \frac{(x-y)^2}{4\tau}\right]dy$$

**Complete the square** in the exponent:
$$ny - \frac{(x-y)^2}{4\tau} = -\frac{1}{4\tau}\left[(x-y)^2 - 4n\tau y\right]$$

$$= -\frac{1}{4\tau}\left[y^2 - 2xy + x^2 - 4n\tau y\right]$$

$$= -\frac{1}{4\tau}\left[y^2 - 2(x+2n\tau)y + x^2\right]$$

$$= -\frac{1}{4\tau}\left[(y - (x+2n\tau))^2 - (x+2n\tau)^2 + x^2\right]$$

$$= -\frac{(y - (x+2n\tau))^2}{4\tau} + \frac{2nx + 4n^2\tau}{4\tau}$$

$$= -\frac{(y - (x+2n\tau))^2}{4\tau} + nx + n^2\tau$$

Therefore:
$$I_n = \frac{e^{nx + n^2\tau}}{\sqrt{4\pi\tau}}\int_0^{\infty}\exp\left[-\frac{(y - (x+2n\tau))^2}{4\tau}\right]dy$$

**Change of variables**: $z = \frac{y - (x+2n\tau)}{\sqrt{4\tau}}$

When $y = 0$: $z = \frac{-(x+2n\tau)}{\sqrt{4\tau}} = -\frac{x+2n\tau}{2\sqrt{\tau}}$

When $y \to \infty$: $z \to \infty$

$$I_n = \frac{e^{nx + n^2\tau}}{\sqrt{\pi}}\int_{-\frac{x+2n\tau}{2\sqrt{\tau}}}^{\infty}e^{-z^2}dz$$

Using $\int_{-a}^{\infty}e^{-z^2}dz = \sqrt{\pi}\left[\frac{1}{2} + \frac{1}{2}\text{erf}(a)\right] = \sqrt{\pi}N(a\sqrt{2})$:

$$\boxed{I_n = e^{nx + n^2\tau}N\left(\frac{x+2n\tau}{2\sqrt{\tau}}\right)}$$

where $N$ is the standard normal CDF.

### **Computing $w(x,\tau)$**

$$w(x,\tau) = I_{\frac{k+1}{2}} - I_{\frac{k-1}{2}}$$

$$= e^{\frac{k+1}{2}x + \frac{(k+1)^2}{4}\tau}N\left(\frac{x+(k+1)\tau}{2\sqrt{\tau}}\right) - e^{\frac{k-1}{2}x + \frac{(k-1)^2}{4}\tau}N\left(\frac{x+(k-1)\tau}{2\sqrt{\tau}}\right)$$

---

## **7. Back-Transformation to Get Black-Scholes Formula**

### **Recall the Transformations**

$$u(x,\tau) = e^{-\frac{k-1}{2}x - \frac{(k+1)^2}{4}\tau}w(x,\tau)$$

$$V(S,t) = Ku(x,\tau)$$

$$x = \ln(S/K), \quad \tau = \frac{\sigma^2}{2}(T-t)$$

### **Substitute**

$$u(x,\tau) = e^{-\frac{k-1}{2}x - \frac{(k+1)^2}{4}\tau}\left[e^{\frac{k+1}{2}x + \frac{(k+1)^2}{4}\tau}N(d_1') - e^{\frac{k-1}{2}x + \frac{(k-1)^2}{4}\tau}N(d_2')\right]$$

where:
$$d_1' = \frac{x+(k+1)\tau}{2\sqrt{\tau}}, \quad d_2' = \frac{x+(k-1)\tau}{2\sqrt{\tau}}$$

Simplifying:
$$u(x,\tau) = e^{x}N(d_1') - e^{-k\tau}N(d_2')$$

$$V(S,t) = K\left[e^{\ln(S/K)}N(d_1') - e^{-k\tau}N(d_2')\right]$$

$$= S N(d_1') - Ke^{-k\tau}N(d_2')$$

### **Converting $d_1'$ and $d_2'$**

Recall $k = \frac{2r}{\sigma^2}$ and $\tau = \frac{\sigma^2}{2}(T-t)$:

$$k\tau = \frac{2r}{\sigma^2} \cdot \frac{\sigma^2}{2}(T-t) = r(T-t)$$

$$d_1' = \frac{\ln(S/K) + (k+1)\tau}{2\sqrt{\tau}} = \frac{\ln(S/K) + k\tau + \tau}{2\sqrt{\tau}}$$

$$= \frac{\ln(S/K) + r(T-t) + \frac{\sigma^2}{2}(T-t)}{2\sqrt{\frac{\sigma^2}{2}(T-t)}} = \frac{\ln(S/K) + (r + \frac{\sigma^2}{2})(T-t)}{\sigma\sqrt{T-t}}$$

$$d_2' = \frac{\ln(S/K) + (k-1)\tau}{2\sqrt{\tau}} = \frac{\ln(S/K) + r(T-t) - \frac{\sigma^2}{2}(T-t)}{\sigma\sqrt{T-t}}$$

$$= d_1' - \sigma\sqrt{T-t}$$

### **Black-Scholes Formula**

$$\boxed{C(S,t) = SN(d_1) - Ke^{-r(T-t)}N(d_2)}$$

where:
$$\boxed{d_1 = \frac{\ln(S/K) + (r + \frac{\sigma^2}{2})(T-t)}{\sigma\sqrt{T-t}}, \quad d_2 = d_1 - \sigma\sqrt{T-t}}$$

**We've recovered the Black-Scholes formula through pure PDE methods!**

---

## **8. Put Option via Heat Equation**

For the put, the initial condition is:
$$w(x,0) = \begin{cases}
e^{\frac{k-1}{2}x} - e^{\frac{k+1}{2}x} & x < 0 \\
0 & x \geq 0
\end{cases}$$

Following similar calculations:
$$w(x,\tau) = \int_{-\infty}^0\left[e^{\frac{k-1}{2}y} - e^{\frac{k+1}{2}y}\right]G(x-y,\tau)dy$$

This gives:
$$\boxed{P(S,t) = Ke^{-r(T-t)}N(-d_2) - SN(-d_1)}$$

Alternatively, use **put-call parity**:
$$P = C - S + Ke^{-r(T-t)}$$

---

## **9. Properties of the Heat Kernel**

### **Self-Similarity**

The heat kernel exhibits **scaling invariance**:
$$G(x,\tau) = \frac{1}{\sqrt{\tau}}g\left(\frac{x}{\sqrt{\tau}}\right)$$

where $g(\xi) = \frac{1}{\sqrt{4\pi}}e^{-\xi^2/4}$.

This is why the solution depends on $\frac{x}{\sqrt{\tau}}$ — the **similarity variable**.

### **Semigroup Property**

$$\int_{-\infty}^{\infty}G(x-y,\tau_1)G(y-z,\tau_2)dy = G(x-z,\tau_1+\tau_2)$$

The heat equation generates a **diffusion semigroup**.

### **Maximum Principle**

If $w(x,0) \geq 0$, then $w(x,\tau) \geq 0$ for all $\tau > 0$.

This ensures option prices remain non-negative.

### **Smoothing Property**

Even if $w(x,0)$ is discontinuous (like the call payoff), $w(x,\tau)$ is **infinitely differentiable** for $\tau > 0$.

This is why option values are smooth even though payoffs have kinks.

---

## **10. Connection to Similarity Solutions**

### **Similarity Variable**

Define:
$$\xi = \frac{x}{\sqrt{4\tau}}$$

The heat equation becomes an ODE:
$$\frac{d^2 g}{d\xi^2} + 2\xi\frac{dg}{d\xi} = 0$$

Integrating:
$$\frac{dg}{d\xi} = Ce^{-\xi^2}$$

$$g(\xi) = C_1\int_{-\infty}^{\xi}e^{-s^2}ds + C_2 = C_1\sqrt{\pi}\text{erf}(\xi) + C_2$$

This connects to the error function structure in Black-Scholes!

### **In Original Variables**

With $\xi = \frac{\ln(S/K) + (r \pm \frac{\sigma^2}{2})(T-t)}{\sigma\sqrt{T-t}}$, we get:

$$C \propto \text{erf}(d_1) - \text{erf}(d_2) = N(d_1) - N(d_2)$$

(up to normalizations and transformations).

---

## **11. Why This Transformation Works: Deep Insight**

### **Geometric Brownian Motion → Arithmetic Brownian Motion**

The logarithmic change $x = \ln(S/K)$ converts:
- **GBM**: $dS = \mu S dt + \sigma S dW$
- **ABM**: $dx = (\mu - \frac{\sigma^2}{2})dt + \sigma dW$

ABM has **constant coefficients**, making it amenable to Fourier/heat equation methods.

### **Time Reversal**

The transformation $\tau = T - t$ reverses time, converting:
- **Backward parabolic PDE** (initial value problem)
- **Forward parabolic PDE** (Cauchy problem)

Standard heat equation theory solves forward problems.

### **Exponential Transformation Removes Drift/Decay**

The ansatz $u = e^{\alpha x + \beta \tau}w$ is a **similarity transformation** that:
- Removes the first-order drift term (setting $\alpha$)
- Removes the zeroth-order decay term (setting $\beta$)

This is analogous to "changing to the moving frame" in wave equations.

### **Universal Heat Kernel**

All parabolic PDEs with constant coefficients reduce to the heat equation, which has a **universal solution** — the Gaussian kernel. This is why:

$$\text{Option Pricing} \leftrightarrow \text{Gaussian Integrals}$$

---

## **12. Extensions**

### **Time-Dependent Volatility**

If $\sigma = \sigma(t)$, define:
$$\tau = \frac{1}{2}\int_t^T \sigma^2(s)ds$$

The transformation still works with **integrated variance**.

### **Dividends**

Replace $r$ with $r - q$ throughout. The parameter becomes:
$$k = \frac{2(r-q)}{\sigma^2}$$

### **Barrier Options**

For knock-out barriers, add **boundary conditions** to the heat equation:
$$w(x_B, \tau) = 0$$

Use the **method of images** or **eigenfunction expansion**.

### **American Options**

The **free boundary problem** becomes:
$$\max\left\{\frac{\partial w}{\partial \tau} - \frac{\partial^2 w}{\partial x^2}, w - g(x,\tau)\right\} = 0$$

This is a **Stefan problem** in heat equation theory.

---

## **13. Numerical Advantages**

The heat equation transformation enables:

### **Finite Difference Schemes**

Discretize on uniform $(x, \tau)$ grid:
- **Explicit**: $w_j^{n+1} = w_j^n + \lambda(w_{j+1}^n - 2w_j^n + w_{j-1}^n)$
- **Implicit (Crank-Nicolson)**: More stable, unconditionally convergent

### **Spectral Methods**

Expand in Hermite polynomials (natural basis for heat equation):
$$w(x,\tau) = \sum_{n=0}^{\infty}c_n(\tau)H_n(x)e^{-x^2/2}$$

where $H_n$ are Hermite polynomials.

### **Fast Fourier Transform**

Since solution is a convolution with Gaussian kernel:
$$w(x,\tau) = G * f$$

Use FFT for $O(N\log N)$ computation instead of $O(N^2)$.

---

## **Summary: The Transformation Chain**

$$\begin{align}
&\text{Black-Scholes PDE in } (S,t) \\
&\quad\downarrow \quad x = \ln(S/K), \tau = \frac{\sigma^2}{2}(T-t) \\
&\text{Modified heat equation with drift/decay} \\
&\quad\downarrow \quad u = e^{\alpha x + \beta\tau}w \\
&\text{Standard heat equation: } \frac{\partial w}{\partial \tau} = \frac{\partial^2 w}{\partial x^2} \\
&\quad\downarrow \quad \text{Convolution with heat kernel} \\
&w(x,\tau) = \int G(x-y,\tau)f(y)dy \\
&\quad\downarrow \quad \text{Gaussian integrals} \\
&w(x,\tau) = e^{\cdots}N(d_1) - e^{\cdots}N(d_2) \\
&\quad\downarrow \quad \text{Reverse transformations} \\
&\boxed{C(S,t) = SN(d_1) - Ke^{-r(T-t)}N(d_2)}
\end{align}$$

This method reveals that **Black-Scholes is fundamentally a heat diffusion problem** in logarithmic price space!

Would you like me to explore:
- Detailed finite difference implementation of the heat equation
- Method of images for barrier options
- Eigenfunction expansion for exotic payoffs
- Connection to Fourier transforms and characteristic functions?