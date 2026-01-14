# How to Check SDE Solutions


## Introduction


Given a stochastic differential equation (SDE) and a proposed solution, we need to verify whether the solution indeed satisfies the SDE. This verification process is fundamental in stochastic calculus and quantitative finance, as it confirms the correctness of analytical solutions before using them in applications.

## General Framework


### 1. The SDE Problem


Consider a general SDE of the form:

$$
dX_t = \mu(X_t, t) dt + \sigma(X_t, t) dW_t
$$

where:
- $X_t$ is the stochastic process
- $\mu(X_t, t)$ is the drift coefficient
- $\sigma(X_t, t)$ is the diffusion coefficient
- $W_t$ is a standard Brownian motion

### 2. Verification Strategy


To verify that a proposed solution $X_t = f(W_t, t)$ satisfies the SDE, we:

1. Compute $dX_t$ using **Itô's lemma**
2. Compare the result with the original SDE
3. Check if the drift and diffusion coefficients match

## Itô's Lemma


**Theorem (Itô's Lemma):** Let $X_t$ be an Itô process satisfying:

$$
dX_t = \mu_t dt + \sigma_t dW_t
$$

and let $f(x, t) \in C^{2,1}(\mathbb{R} \times [0, T])$. Then $Y_t = f(X_t, t)$ is also an Itô process with:

$$
df(X_t, t) = \left(\frac{\partial f}{\partial t} + \mu_t \frac{\partial f}{\partial x} + \frac{1}{2}\sigma_t^2 \frac{\partial^2 f}{\partial x^2}\right) dt + \sigma_t \frac{\partial f}{\partial x} dW_t
$$

**Special Case:** When $X_t = W_t$ (standard Brownian motion), we have $\mu_t = 0$ and $\sigma_t = 1$, so:

$$
df(W_t, t) = \left(\frac{\partial f}{\partial t} + \frac{1}{2}\frac{\partial^2 f}{\partial x^2}\right) dt + \frac{\partial f}{\partial x} dW_t
$$

## Example 1: Geometric Brownian Motion (Stock Price Model)


### 1. The SDE


The geometric Brownian motion (GBM) model for stock prices is:

$$
dS_t = \mu S_t dt + \sigma S_t dW_t
$$

where $\mu$ is the drift rate and $\sigma$ is the volatility.

### 2. Proposed Solution


The analytical solution is claimed to be:

$$
S_t = S_0 \exp\left[\left(\mu - \frac{\sigma^2}{2}\right)t + \sigma W_t\right]
$$

### 3. Verification


Let $f(x, t) = S_0 \exp\left[\left(\mu - \frac{\sigma^2}{2}\right)t + \sigma x\right]$ where $x = W_t$.

**Step 1:** Compute partial derivatives.

$$
\frac{\partial f}{\partial t} = S_0 \exp\left[\left(\mu - \frac{\sigma^2}{2}\right)t + \sigma x\right] \cdot \left(\mu - \frac{\sigma^2}{2}\right) = S_t \left(\mu - \frac{\sigma^2}{2}\right)
$$

$$
\frac{\partial f}{\partial x} = S_0 \exp\left[\left(\mu - \frac{\sigma^2}{2}\right)t + \sigma x\right] \cdot \sigma = \sigma S_t
$$

$$
\frac{\partial^2 f}{\partial x^2} = S_0 \exp\left[\left(\mu - \frac{\sigma^2}{2}\right)t + \sigma x\right] \cdot \sigma^2 = \sigma^2 S_t
$$

**Step 2:** Apply Itô's lemma.

$$
\begin{align}
dS_t &= \left(\frac{\partial f}{\partial t} + \frac{1}{2}\frac{\partial^2 f}{\partial x^2}\right) dt + \frac{\partial f}{\partial x} dW_t \\
&= \left(S_t \left(\mu - \frac{\sigma^2}{2}\right) + \frac{1}{2}\sigma^2 S_t\right) dt + \sigma S_t dW_t \\
&= S_t \left(\mu - \frac{\sigma^2}{2} + \frac{\sigma^2}{2}\right) dt + \sigma S_t dW_t \\
&= \mu S_t dt + \sigma S_t dW_t
\end{align}
$$

**Conclusion:** The solution matches the original SDE. ✓

### 4. Interpretation


The presence of the $-\frac{\sigma^2}{2}$ term in the exponent is the **Itô correction**, which arises from the second-order term in Itô's lemma. This is a fundamental difference from ordinary calculus and reflects the quadratic variation of Brownian motion.

## Example 2: Ornstein-Uhlenbeck Process


### 1. The SDE


The Ornstein-Uhlenbeck (OU) process describes mean-reverting behavior:

$$
dX_t = \theta(\mu - X_t) dt + \sigma dW_t
$$

where:
- $\theta > 0$ is the speed of mean reversion
- $\mu$ is the long-term mean
- $\sigma$ is the volatility

### 2. Proposed Solution


The solution is:

$$
X_t = X_0 e^{-\theta t} + \mu(1 - e^{-\theta t}) + \sigma \int_0^t e^{-\theta(t-s)} dW_s
$$

### 3. Verification


Define $Y_t = X_t - \mu$, so the SDE becomes:

$$
dY_t = -\theta Y_t dt + \sigma dW_t
$$

The proposed solution for $Y_t$ is:

$$
Y_t = Y_0 e^{-\theta t} + \sigma \int_0^t e^{-\theta(t-s)} dW_s
$$

**Method 1: Direct differentiation using integration by parts**

Let $Z_t = \int_0^t e^{-\theta(t-s)} dW_s$. We can write:

$$
Z_t = e^{-\theta t} \int_0^t e^{\theta s} dW_s
$$

Applying Itô's lemma to $f(x, t) = e^{-\theta t} x$ where $x = \int_0^t e^{\theta s} dW_s$:

$$
\frac{\partial f}{\partial t} = -\theta e^{-\theta t} x, \quad \frac{\partial f}{\partial x} = e^{-\theta t}, \quad \frac{\partial^2 f}{\partial x^2} = 0
$$

Since $dx = e^{\theta t} dW_t$, we have:

$$
dZ_t = -\theta e^{-\theta t} x \, dt + e^{-\theta t} \cdot e^{\theta t} dW_t = -\theta Z_t dt + dW_t
$$

Therefore:

$$
\begin{align}
dY_t &= d(Y_0 e^{-\theta t}) + \sigma dZ_t \\
&= -\theta Y_0 e^{-\theta t} dt + \sigma(-\theta Z_t dt + dW_t) \\
&= -\theta(Y_0 e^{-\theta t} + \sigma Z_t) dt + \sigma dW_t \\
&= -\theta Y_t dt + \sigma dW_t
\end{align}
$$

**Conclusion:** The solution is verified. ✓

## Example 3: Vasicek Model (Interest Rate)


### 1. The SDE


The Vasicek model for short-term interest rates is:

$$
dr_t = a(b - r_t) dt + \sigma dW_t
$$

where:
- $a > 0$ is the speed of mean reversion
- $b$ is the long-term mean level
- $\sigma$ is the volatility

This is structurally identical to the OU process.

### 2. Proposed Solution


$$
r_t = r_0 e^{-at} + b(1 - e^{-at}) + \sigma \int_0^t e^{-a(t-s)} dW_s
$$

### 3. Verification


Following the same approach as the OU process, let $Y_t = r_t - b$:

$$
Y_t = (r_0 - b) e^{-at} + \sigma \int_0^t e^{-a(t-s)} dW_s
$$

Then:

$$
dY_t = -a Y_t dt + \sigma dW_t
$$

which gives:

$$
dr_t = dY_t = -a(r_t - b) dt + \sigma dW_t = a(b - r_t) dt + \sigma dW_t
$$

**Conclusion:** Verified. ✓

### 4. Properties of the Solution


**Conditional Mean:**

$$
\mathbb{E}[r_t | r_0] = r_0 e^{-at} + b(1 - e^{-at})
$$

**Conditional Variance:**

$$
\text{Var}[r_t | r_0] = \frac{\sigma^2}{2a}(1 - e^{-2at})
$$

**Long-term behavior:**

$$
\lim_{t \to \infty} \mathbb{E}[r_t | r_0] = b, \quad \lim_{t \to \infty} \text{Var}[r_t | r_0] = \frac{\sigma^2}{2a}
$$

## Example 4: Cox-Ingersoll-Ross (CIR) Model


### 1. The SDE


The CIR model extends Vasicek by making volatility state-dependent:

$$
dr_t = a(b - r_t) dt + \sigma \sqrt{r_t} dW_t
$$

where $a, b, \sigma > 0$ and the **Feller condition** $2ab \geq \sigma^2$ ensures $r_t \geq 0$.

### 2. Proposed Solution via Transformation


The CIR model doesn't have a simple closed-form solution like GBM or Vasicek. However, we can verify transformations.

**Claim:** Let $X_t = \sqrt{r_t}$. Then under certain conditions, we can derive the SDE for $X_t$.

**Verification:** Apply Itô's lemma to $f(r) = \sqrt{r}$.

$$
\frac{\partial f}{\partial r} = \frac{1}{2\sqrt{r}}, \quad \frac{\partial^2 f}{\partial r^2} = -\frac{1}{4r^{3/2}}
$$

Therefore:

$$
\begin{align}
dX_t &= \left[a(b - r_t) \cdot \frac{1}{2\sqrt{r_t}} + \frac{1}{2}\sigma^2 r_t \cdot \left(-\frac{1}{4r_t^{3/2}}\right)\right] dt + \sigma\sqrt{r_t} \cdot \frac{1}{2\sqrt{r_t}} dW_t \\
&= \left[\frac{a(b - r_t)}{2\sqrt{r_t}} - \frac{\sigma^2}{8\sqrt{r_t}}\right] dt + \frac{\sigma}{2} dW_t \\
&= \left[\frac{ab - ar_t - \sigma^2/4}{2\sqrt{r_t}}\right] dt + \frac{\sigma}{2} dW_t \\
&= \left[\frac{ab - \sigma^2/4}{2X_t} - \frac{a}{2}X_t\right] dt + \frac{\sigma}{2} dW_t
\end{align}
$$

This transformation is useful for numerical methods and analytical approximations.

### 3. Alternative: Non-central Chi-squared Distribution


For the CIR model, the solution at time $t$ conditional on $r_0$ is not explicit but follows a scaled non-central chi-squared distribution:

$$
r_t \sim \frac{\sigma^2(1-e^{-at})}{4a} \chi^2_{d}\left(\frac{4a e^{-at}}{\sigma^2(1-e^{-at})}r_0\right)
$$

where $d = \frac{4ab}{\sigma^2}$ is the degrees of freedom.

**Verification approach:** One would check that this distribution satisfies the Fokker-Planck (forward Kolmogorov) equation associated with the CIR SDE:

$$
\frac{\partial p}{\partial t} = -\frac{\partial}{\partial r}[a(b-r)p] + \frac{1}{2}\frac{\partial^2}{\partial r^2}[\sigma^2 r p]
$$

where $p(r, t)$ is the probability density function.

## Example 5: Black-Scholes with Dividends


### 1. The SDE


A stock paying continuous dividends at rate $q$ follows:

$$
dS_t = (\mu - q) S_t dt + \sigma S_t dW_t
$$

### 2. Proposed Solution


$$
S_t = S_0 \exp\left[\left(\mu - q - \frac{\sigma^2}{2}\right)t + \sigma W_t\right]
$$

### 3. Verification


Let $f(x, t) = S_0 \exp\left[\left(\mu - q - \frac{\sigma^2}{2}\right)t + \sigma x\right]$.

$$
\frac{\partial f}{\partial t} = S_t\left(\mu - q - \frac{\sigma^2}{2}\right)
$$

$$
\frac{\partial f}{\partial x} = \sigma S_t
$$

$$
\frac{\partial^2 f}{\partial x^2} = \sigma^2 S_t
$$

Applying Itô's lemma:

$$
\begin{align}
dS_t &= \left[S_t\left(\mu - q - \frac{\sigma^2}{2}\right) + \frac{1}{2}\sigma^2 S_t\right] dt + \sigma S_t dW_t \\
&= (\mu - q) S_t dt + \sigma S_t dW_t
\end{align}
$$

**Conclusion:** Verified. ✓

## Example 6: Change of Measure (Risk-Neutral Pricing)


### 1. Physical vs. Risk-Neutral Measure


Under the physical measure $\mathbb{P}$:

$$
dS_t = \mu S_t dt + \sigma S_t dW_t^\mathbb{P}
$$

Under the risk-neutral measure $\mathbb{Q}$:

$$
dS_t = r S_t dt + \sigma S_t dW_t^\mathbb{Q}
$$

where $r$ is the risk-free rate.

### 2. Girsanov's Theorem


The two Brownian motions are related by:

$$
W_t^\mathbb{Q} = W_t^\mathbb{P} + \frac{\mu - r}{\sigma}t
$$

### 3. Verification


The market price of risk is $\lambda = \frac{\mu - r}{\sigma}$. Under $\mathbb{Q}$:

$$
dW_t^\mathbb{P} = dW_t^\mathbb{Q} - \lambda dt
$$

Substituting into the original SDE:

$$
\begin{align}
dS_t &= \mu S_t dt + \sigma S_t dW_t^\mathbb{P} \\
&= \mu S_t dt + \sigma S_t (dW_t^\mathbb{Q} - \lambda dt) \\
&= (\mu - \sigma\lambda) S_t dt + \sigma S_t dW_t^\mathbb{Q} \\
&= (\mu - \sigma \cdot \frac{\mu - r}{\sigma}) S_t dt + \sigma S_t dW_t^\mathbb{Q} \\
&= r S_t dt + \sigma S_t dW_t^\mathbb{Q}
\end{align}
$$

**Conclusion:** The change of measure is verified. ✓

## General Verification Checklist


When verifying an SDE solution, follow these steps:

### 1. Identify the Structure


- Write down the SDE explicitly: $dX_t = \mu(X_t, t) dt + \sigma(X_t, t) dW_t$
- Identify the proposed solution: $X_t = f(W_t, t)$ or $X_t = f(Y_t, t)$ for some process $Y_t$

### 2. Compute Partial Derivatives


For $f(x, t)$, compute:
- $\frac{\partial f}{\partial t}$
- $\frac{\partial f}{\partial x}$
- $\frac{\partial^2 f}{\partial x^2}$

### 3. Apply Itô's Lemma


If $X_t$ depends on Brownian motion directly:

$$
dX_t = \left(\frac{\partial f}{\partial t} + \frac{1}{2}\frac{\partial^2 f}{\partial x^2}\right) dt + \frac{\partial f}{\partial x} dW_t
$$

If $X_t = f(Y_t, t)$ where $dY_t = \mu_Y dt + \sigma_Y dW_t$:

$$
dX_t = \left(\frac{\partial f}{\partial t} + \mu_Y \frac{\partial f}{\partial y} + \frac{1}{2}\sigma_Y^2 \frac{\partial^2 f}{\partial y^2}\right) dt + \sigma_Y \frac{\partial f}{\partial y} dW_t
$$

### 4. Match Coefficients


Compare the computed $dX_t$ with the original SDE:
- **Drift coefficient:** The $dt$ terms must match
- **Diffusion coefficient:** The $dW_t$ terms must match

### 5. Check Initial/Boundary Conditions


Verify that $X_0 = f(W_0, 0) = f(0, 0)$ matches the specified initial condition.

## Common Pitfalls


### 1. Forgetting the Itô Correction


The $\frac{1}{2}\sigma^2 \frac{\partial^2 f}{\partial x^2}$ term is essential and distinguishes stochastic from ordinary calculus.

### 2. Incorrect Chain Rule Application


Remember that $(dW_t)^2 = dt$ in Itô calculus, leading to second-order terms.

### 3. Sign Errors in Mean Reversion


In mean-reverting models, ensure the sign of $\theta(X_t - \mu)$ vs. $\theta(\mu - X_t)$ is correct.

### 4. Mismatched Measures


When working with risk-neutral pricing, ensure consistency between physical and risk-neutral measures.

## Advanced Topics


### 1. Multi-dimensional SDEs


For a system of SDEs:

$$
dX_t^i = \mu^i(X_t, t) dt + \sum_{j=1}^d \sigma^{ij}(X_t, t) dW_t^j
$$

Itô's lemma extends to:

$$
df = \frac{\partial f}{\partial t} dt + \sum_{i=1}^n \frac{\partial f}{\partial x^i} dX_t^i + \frac{1}{2}\sum_{i,j=1}^n \frac{\partial^2 f}{\partial x^i \partial x^j} dX_t^i dX_t^j
$$

where $dX_t^i dX_t^j = \sum_{k=1}^d \sigma^{ik}\sigma^{jk} dt$ (using $dW_t^k dW_t^l = \delta_{kl} dt$).

### 2. Jump-Diffusion Models


For SDEs with jumps (e.g., Merton model):

$$
dS_t = \mu S_t dt + \sigma S_t dW_t + S_t dJ_t
$$

where $J_t$ is a jump process, verification requires extended Itô's lemma with jump terms.

## Conclusion


Verifying SDE solutions is a fundamental skill in stochastic calculus and quantitative finance. The key tool is **Itô's lemma**, which accounts for the quadratic variation of Brownian motion through the second-order correction term. By systematically:

1. Computing partial derivatives
2. Applying Itô's lemma
3. Matching drift and diffusion coefficients

we can rigorously confirm that a proposed solution satisfies the governing SDE. This verification process is essential for:

- Validating analytical solutions before use in pricing and risk management
- Developing intuition for stochastic processes
- Ensuring correctness in model implementation
- Understanding the relationship between SDEs and their solutions

The examples provided—from geometric Brownian motion to CIR models—illustrate the technique across various applications in quantitative finance, each highlighting different aspects of stochastic calculus and its subtleties.
