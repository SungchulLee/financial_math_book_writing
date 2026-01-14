# Reflection Principle



## Introduction



In **Brownian Motion Foundations**, we briefly introduced the reflection principle (Theorem 1.3.19) and established that:

$$\mathbb{P}\left(\max_{0 \le s \le t} W_s \ge a\right) = 2\mathbb{P}(W_t \ge a)$$



This elegant result exploits the **symmetric structure** of Brownian motion to evaluate probabilities of path-dependent events—such as hitting a barrier or attaining a maximum—by constructing cleverly reflected sample paths.

The reflection principle is one of the most powerful tools in Brownian motion theory, with applications spanning:
- **Barrier options** in mathematical finance (knock-in, knock-out options)
- **First passage time distributions** for risk management
- **Survival probabilities** in credit risk modeling
- **Drawdown analysis** for portfolio risk assessment

This section provides a comprehensive treatment:
1. **Geometric reflection arguments** for maximum and joint events
2. **First passage time distribution** (Lévy distribution)
3. **Alternative proof via exponential martingales** and Laplace transforms
4. **Joint distribution** of maximum and endpoint $(M_t, W_t)$
5. **Applications to mathematical finance**

Throughout, we include Python visualizations that illustrate the geometric intuition behind the reflection principle.

## Reflection Principle



### 1. Statement Geometr



Let $W_t$ be standard Brownian motion and $a > 0$. Define the **maximum up to time $t$**:

$$M_t := \sup_{0 \le s \le t} W_s$$



**Theorem 1.6.1** (Reflection Principle for Maximum)

For any $t > 0$ and $a > 0$:

$$\boxed{
\mathbb{P}(M_t \ge a) = 2\mathbb{P}(W_t \ge a)
}$$



**Geometric Idea:**

The proof constructs a **pathwise bijection** between two sets of paths:
1. **Set A**: Paths that hit level $a$ before time $t$ and end below $a$
2. **Set B**: Paths that hit level $a$ before time $t$ and end above $a$

The bijection works by **reflecting** the portion of the path after the first hitting time $\tau_a$ across the level $a$.

### 2. Detailed Proof



**Proof:**

Define the **first hitting time** of level $a$:

$$\tau_a := \inf\{s \ge 0 : W_s = a\}$$



We partition the event $\{M_t \ge a\}$ based on where the path ends:

$$\{M_t \ge a\} = \{M_t \ge a, W_t \ge a\} \cup \{M_t \ge a, W_t < a\}$$



**Step 1: Event where path ends above $a$.**

By symmetry of Brownian motion (since $W_t$ and $-W_t$ have the same distribution):

$$\mathbb{P}(M_t \ge a, W_t \ge a) = \mathbb{P}(W_t \ge a)$$



**Step 2: Event where path ends below $a$.**

For paths that hit $a$ at time $\tau_a < t$ but end at $W_t < a$, we construct the **reflected path**:

$$\tilde{W}_s = \begin{cases}
W_s & \text{if } s \le \tau_a \\
2a - W_s & \text{if } s > \tau_a
\end{cases}$$



**Key observation:** By the **strong Markov property**, after hitting $a$, the process $W_{\tau_a + s} - a$ is a Brownian motion independent of $\mathcal{F}_{\tau_a}$. The reflection $2a - W_s$ has the same distribution as $W_s$ for $s > \tau_a$.

Therefore, the **reflected endpoint** is:

$$\tilde{W}_t = 2a - W_t$$



**Bijection:** The map $W \mapsto \tilde{W}$ establishes a bijection:

$$\{M_t \ge a, W_t < a\} \leftrightarrow \{M_t \ge a, W_t > a\}$$



Each path ending at $W_t = x < a$ corresponds to a reflected path ending at $\tilde{W}_t = 2a - x > a$.

**Step 3: Combine.**


$$\mathbb{P}(M_t \ge a, W_t < a) = \mathbb{P}(M_t \ge a, W_t > a) = \mathbb{P}(W_t > a)$$



(The second equality uses the fact that if the reflected path ends above $a$, the original path must have hit $a$.)

Therefore:

$$\mathbb{P}(M_t \ge a) = \mathbb{P}(M_t \ge a, W_t \ge a) + \mathbb{P}(M_t \ge a, W_t < a)$$



$$= \mathbb{P}(W_t \ge a) + \mathbb{P}(W_t > a) = 2\mathbb{P}(W_t \ge a) \quad \square$$



### 3. Explicit Formula



Since $W_t \sim \mathcal{N}(0, t)$:

$$\mathbb{P}(M_t \ge a) = 2\mathbb{P}(W_t \ge a) = 2\left[1 - \Phi\left(\frac{a}{\sqrt{t}}\right)\right] = 2\Phi\left(-\frac{a}{\sqrt{t}}\right)$$



where $\Phi$ is the standard normal CDF.

### 4. Python Visualizat



The following code visualizes the reflection principle by showing an original path that hits level $a$ and its reflected counterpart.

```python
import matplotlib.pyplot as plt
import numpy as np

# Parameters
a = 2
T = 5
num_steps = 1000
dt = T / num_steps

# Search valid path
np.random.seed(0)
found = False
seed = 0

while not found:
    np.random.seed(seed)
    dW = np.random.normal(0, np.sqrt(dt), size=num_steps)
    path = np.cumsum(np.insert(dW, 0, 0))
    t = np.linspace(0, T, num_steps + 1)
    
    hits_a = np.where(path >= a)[0]
    if len(hits_a) > 0:
        hit_index = hits_a[0]
        found = True
    else:
        seed += 1

# Reflect path after
reflected_path = path.copy()
reflected_path[hit_index + 1:] = 2 * a - path[hit_index + 1:]

# Plotting
fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(t, path, label='Original Path', lw=3, alpha=0.4, color="blue")
ax.plot(t, reflected_path, linestyle='-', lw=1.5, label=f'Reflected Path (after hitting {a})', 
        color="red")

# Markers
ax.scatter(t[hit_index], path[hit_index], s=100, color='green', zorder=5, 
           label=f'First hit at level {a}')
ax.scatter(t[-1], path[-1], s=100, color='blue', zorder=5, 
           label=f'Original endpoint: {path[-1]:.2f}')
ax.scatter(t[-1], reflected_path[-1], s=100, color='red', zorder=5, 
           label=f'Reflected endpoint: {reflected_path[-1]:.2f}')

# Reference line
ax.axhline(a, color='black', linestyle='--', linewidth=2, label=f'Barrier level {a}')

# Formatting
ax.set_title(f'Reflection Principle: Path Hitting Level {a}', fontsize=14, fontweight='bold')
ax.set_xlabel('Time', fontsize=12)
ax.set_ylabel('Value', fontsize=12)
ax.legend(loc='upper left', fontsize=10)
ax.grid(alpha=0.3)

plt.tight_layout()
plt.show()

print(f"Original path ends at: {path[-1]:.4f}")
print(f"Reflected path ends at: {reflected_path[-1]:.4f}")
print(f"Sum: {path[-1] + reflected_path[-1]:.4f} (should be close to {2*a})")
```

**Interpretation:**
- Blue path: Original Brownian motion that hits $a$ at the green dot
- Red path: Reflected version after hitting $a$
- Note: $W_t + \tilde{W}_t = 2a$ (the endpoints are symmetric about level $a$)
- Exactly one of the original or reflected path ends above level $a$

## Joint Distribution



### 1. Statement



**Theorem 1.6.2** (Reflection Principle for Joint Events)

For $a > 0$ and $b < a$:

$$\boxed{
\mathbb{P}(M_t \ge a, W_t \le b) = \mathbb{P}(W_t \ge 2a - b)
}$$



**Proof:**

The same reflection argument applies. For paths that hit level $a$ at time $\tau_a$ and end at $W_t \le b < a$, reflect the portion after $\tau_a$:

$$\tilde{W}_t = 2a - W_t \ge 2a - b > a$$



The bijection maps:

$$\{M_t \ge a, W_t \le b\} \leftrightarrow \{W_t \ge 2a - b\}$$



Therefore:

$$\mathbb{P}(M_t \ge a, W_t \le b) = \mathbb{P}(W_t \ge 2a - b) \quad \square$$



### 2. Explicit Formula



Since $W_t \sim \mathcal{N}(0, t)$:

$$\boxed{
\mathbb{P}(M_t \ge a, W_t \le b) = 1 - \Phi\left(\frac{2a - b}{\sqrt{t}}\right) = \Phi\left(\frac{b - 2a}{\sqrt{t}}\right)
}$$



### 3. Python Visualizat



This code shows a path that hits $a$ and ends below $b < a$, along with its reflection.

```python
import matplotlib.pyplot as plt
import numpy as np

# Parameters
a = 2.0
b = -1.5
T = 5
num_steps = 1000
dt = T / num_steps

# Search valid path
np.random.seed(0)
found = False
seed = 0

while not found:
    np.random.seed(seed)
    dW = np.random.normal(0, np.sqrt(dt), size=num_steps)
    path = np.cumsum(np.insert(dW, 0, 0))
    t = np.linspace(0, T, num_steps + 1)
    
    hits_a = np.where(path >= a)[0]
    if len(hits_a) > 0 and path[-1] < b:
        hit_index = hits_a[0]
        found = True
    else:
        seed += 1

# Reflect path after
reflected_path = path.copy()
reflected_path[hit_index + 1:] = 2 * a - path[hit_index + 1:]

# Plotting
fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(t, path, label='Original Path', lw=3, alpha=0.4, color="blue")
ax.plot(t, reflected_path, linestyle='-', lw=1.5, 
        label=f'Reflected Path (after hitting {a})', color="red")

# Markers
ax.scatter(t[hit_index], path[hit_index], s=100, color='green', zorder=5, 
           label=f'First hit at level {a}')
ax.scatter(t[-1], path[-1], s=100, color='blue', zorder=5, 
           label=f'Original endpoint < {b}')
ax.scatter(t[-1], reflected_path[-1], s=100, color='red', zorder=5, 
           label=f'Reflected endpoint > {2*a - b:.1f}')

# Reference lines
ax.axhline(a, color='green', linestyle='--', linewidth=2, label=f'Upper barrier: {a}')
ax.axhline(b, color='blue', linestyle='--', linewidth=2, label=f'Lower threshold: {b}')
ax.axhline(2*a - b, color='red', linestyle='--', linewidth=2, 
           label=f'Reflection level: {2*a - b:.1f}')

# Formatting
ax.set_title(f'Reflection Principle: Hit {a}, End Below {b}', fontsize=14, fontweight='bold')
ax.set_xlabel('Time', fontsize=12)
ax.set_ylabel('Value', fontsize=12)
ax.legend(loc='upper left', fontsize=9)
ax.grid(alpha=0.3)

plt.tight_layout()
plt.show()

print(f"Original path ends at: {path[-1]:.4f} (below {b})")
print(f"Reflected path ends at: {reflected_path[-1]:.4f} (above {2*a - b:.1f})")
```

**Interpretation:**
- Original path (blue) hits upper barrier $a$ and ends below lower level $b$
- Reflected path (red) ends above the mirror level $2a - b$
- This bijection proves $\mathbb{P}(M_t \ge a, W_t \le b) = \mathbb{P}(W_t \ge 2a - b)$

## Passage Time



### 1. Distribution via



Define the **first passage time** (first hitting time) to level $a > 0$:

$$\tau_a := \inf\{t \ge 0 : W_t = a\}$$



**Theorem 1.6.3** (CDF of First Passage Time)

The cumulative distribution function of $\tau_a$ is:

$$\mathbb{P}(\tau_a \le t) = 2\Phi\left(-\frac{a}{\sqrt{t}}\right)$$



where $\Phi$ is the standard normal CDF.

**Proof:**

The event $\{\tau_a \le t\}$ is equivalent to $\{M_t \ge a\}$ (the maximum reaches $a$ by time $t$).

By the reflection principle (Theorem 1.6.1):

$$\mathbb{P}(\tau_a \le t) = \mathbb{P}(M_t \ge a) = 2\mathbb{P}(W_t \ge a) = 2\left[1 - \Phi\left(\frac{a}{\sqrt{t}}\right)\right] = 2\Phi\left(-\frac{a}{\sqrt{t}}\right) \quad \square$$



### 2. Probability Densi



**Theorem 1.6.4** (PDF of First Passage Time - Lévy Distribution)

The probability density function of $\tau_a$ is:

$$\boxed{
f_{\tau_a}(t) = \frac{a}{\sqrt{2\pi t^3}} \exp\left(-\frac{a^2}{2t}\right), \quad t > 0
}$$



This is called the **Lévy distribution** (or inverse Gaussian with zero drift).

**Proof:**

Differentiate the CDF with respect to $t$:

$$f_{\tau_a}(t) = \frac{d}{dt}\left[2\Phi\left(-\frac{a}{\sqrt{t}}\right)\right]$$



Using the chain rule and $\Phi'(x) = \phi(x) = \frac{1}{\sqrt{2\pi}}e^{-x^2/2}$:

$$= 2\phi\left(-\frac{a}{\sqrt{t}}\right) \cdot \frac{d}{dt}\left(-\frac{a}{\sqrt{t}}\right)$$



$$= \frac{2}{\sqrt{2\pi}} \exp\left(-\frac{a^2}{2t}\right) \cdot \frac{a}{2t^{3/2}}$$



$$= \frac{a}{\sqrt{2\pi t^3}} \exp\left(-\frac{a^2}{2t}\right) \quad \square$$



### 3. Properties First



**Proposition 1.6.5**

The first passage time $\tau_a$ satisfies:
1. $\mathbb{P}(\tau_a < \infty) = 1$ (recurrence of Brownian motion)
2. $\mathbb{E}[\tau_a] = \infty$ (infinite expected hitting time)
3. $\text{Var}(\tau_a) = \infty$ (infinite variance)

**Proof of (2):**

The tail behavior of the density is:

$$f_{\tau_a}(t) \sim \frac{a}{\sqrt{2\pi}} t^{-3/2} \quad \text{as } t \to \infty$$



The integral:

$$\mathbb{E}[\tau_a] = \int_0^\infty t \cdot f_{\tau_a}(t) dt \sim \int_0^\infty t \cdot t^{-3/2} dt = \int_0^\infty t^{-1/2} dt = \infty$$



The exponent $-1/2$ is marginally non-integrable at infinity. $\square$

**Remark:** This paradoxical result—certain to hit, but taking infinite time on average—reflects the heavy-tailed nature of the Lévy distribution.

## Alternative



### 1. Laplace Transform



We now derive the distribution of $\tau_a$ using **exponential martingales** and optional stopping.

**Theorem 1.6.6** (Laplace Transform of $\tau_a$)

For $\alpha > 0$:

$$\boxed{
\mathbb{E}[e^{-\alpha \tau_a}] = e^{-a\sqrt{2\alpha}}
}$$



**Proof:**

**Step 1: Exponential martingale.**

For any $\lambda \in \mathbb{R}$, the process:

$$M_t := \exp\left(\lambda W_t - \frac{1}{2}\lambda^2 t\right)$$


is a martingale with respect to the natural filtration $\mathcal{F}_t = \sigma(W_s : s \le t)$.

**Step 2: Optional stopping.**

Fix $\lambda > 0$. By the **optional stopping theorem** applied to $\tau_a \wedge T$:

$$\mathbb{E}[M_{\tau_a \wedge T}] = M_0 = 1$$



At time $\tau_a \wedge T$:

$$M_{\tau_a \wedge T} = \exp\left(\lambda W_{\tau_a \wedge T} - \frac{1}{2}\lambda^2 (\tau_a \wedge T)\right)$$



**Step 3: Split the expectation.**


$$1 = \mathbb{E}\left[\exp\left(\lambda a - \frac{1}{2}\lambda^2 \tau_a\right) \mathbf{1}_{\{\tau_a \le T\}}\right] + \mathbb{E}\left[\exp\left(\lambda W_T - \frac{1}{2}\lambda^2 T\right) \mathbf{1}_{\{\tau_a > T\}}\right]$$



The second term is non-negative, so:

$$1 \ge \mathbb{E}\left[\exp\left(\lambda a - \frac{1}{2}\lambda^2 \tau_a\right) \mathbf{1}_{\{\tau_a \le T\}}\right]$$



**Step 4: Let $T \to \infty$.**

By monotone convergence (since $\mathbb{P}(\tau_a < \infty) = 1$):

$$1 = \mathbb{E}\left[\exp\left(\lambda a - \frac{1}{2}\lambda^2 \tau_a\right)\right] = e^{\lambda a} \mathbb{E}\left[e^{-\frac{1}{2}\lambda^2 \tau_a}\right]$$



Therefore:

$$\mathbb{E}\left[e^{-\frac{1}{2}\lambda^2 \tau_a}\right] = e^{-\lambda a}$$



**Step 5: Change variables.**

Let $\alpha = \frac{1}{2}\lambda^2$, so $\lambda = \sqrt{2\alpha}$:

$$\mathbb{E}[e^{-\alpha \tau_a}] = e^{-a\sqrt{2\alpha}} \quad \square$$



### 2. Moments via Lapla



**Corollary 1.6.7**

Differentiating the Laplace transform:

$$\mathbb{E}[\tau_a e^{-\alpha \tau_a}] = \frac{a}{\sqrt{2\alpha}} e^{-a\sqrt{2\alpha}}$$



Taking $\alpha \to 0$:

$$\lim_{\alpha \to 0} \mathbb{E}[\tau_a e^{-\alpha \tau_a}] = \lim_{\alpha \to 0} \frac{a}{\sqrt{2\alpha}} e^{-a\sqrt{2\alpha}} = \infty$$



This confirms $\mathbb{E}[\tau_a] = \infty$.

**Proof:**


$$\frac{d}{d\alpha}\mathbb{E}[e^{-\alpha \tau_a}] = -\mathbb{E}[\tau_a e^{-\alpha \tau_a}]$$




$$\frac{d}{d\alpha} e^{-a\sqrt{2\alpha}} = e^{-a\sqrt{2\alpha}} \cdot \left(-\frac{a}{\sqrt{2\alpha}}\right)$$



Therefore:

$$\mathbb{E}[\tau_a e^{-\alpha \tau_a}] = \frac{a}{\sqrt{2\alpha}} e^{-a\sqrt{2\alpha}} \quad \square$$



## Joint Distribution



We now derive the complete **joint density** $f_{M_t, W_t}(m, w)$.

### 1. Main Result



**Theorem 1.6.8** (Joint PDF of Maximum and Endpoint)

For $m > 0$ and $w \le m$:

$$\boxed{
f_{M_t, W_t}(m, w) = \frac{2(2m - w)}{t\sqrt{2\pi t}} \exp\left(-\frac{(2m - w)^2}{2t}\right)
}$$



### 2. Derivation



**Step 1: CDF via reflection.**

From Theorem 1.6.2, for $w < m$:

$$\mathbb{P}(M_t \ge m, W_t \le w) = \mathbb{P}(W_t \ge 2m - w)$$



Therefore:

$$\mathbb{P}(M_t \le m, W_t \le w) = \mathbb{P}(W_t \le w) - \mathbb{P}(W_t \ge 2m - w)$$



$$= \Phi\left(\frac{w}{\sqrt{t}}\right) - \left[1 - \Phi\left(\frac{2m - w}{\sqrt{t}}\right)\right]$$



$$= \Phi\left(\frac{w}{\sqrt{t}}\right) + \Phi\left(\frac{2m - w}{\sqrt{t}}\right) - 1$$



**Step 2: Differentiate to get the joint PDF.**


$$f_{M_t, W_t}(m, w) = \frac{\partial^2}{\partial m \partial w} \mathbb{P}(M_t \le m, W_t \le w)$$



First, differentiate with respect to $w$:

$$\frac{\partial}{\partial w}\left[\Phi\left(\frac{w}{\sqrt{t}}\right) + \Phi\left(\frac{2m - w}{\sqrt{t}}\right) - 1\right]$$



$$= \phi\left(\frac{w}{\sqrt{t}}\right) \cdot \frac{1}{\sqrt{t}} - \phi\left(\frac{2m - w}{\sqrt{t}}\right) \cdot \frac{1}{\sqrt{t}}$$



where $\phi(x) = \frac{1}{\sqrt{2\pi}}e^{-x^2/2}$.

Now differentiate with respect to $m$:

$$\frac{\partial}{\partial m}\left[-\phi\left(\frac{2m - w}{\sqrt{t}}\right) \cdot \frac{1}{\sqrt{t}}\right]$$



$$= -\frac{1}{\sqrt{t}} \cdot \phi'\left(\frac{2m - w}{\sqrt{t}}\right) \cdot \frac{2}{\sqrt{t}}$$



Using $\phi'(x) = -x\phi(x)$:

$$= -\frac{2}{t} \cdot \left(-\frac{2m - w}{\sqrt{t}}\right) \phi\left(\frac{2m - w}{\sqrt{t}}\right)$$



$$= \frac{2(2m - w)}{t\sqrt{t}} \cdot \frac{1}{\sqrt{2\pi}} e^{-(2m-w)^2/(2t)}$$



$$= \frac{2(2m - w)}{t\sqrt{2\pi t}} \exp\left(-\frac{(2m - w)^2}{2t}\right) \quad \square$$



### 3. Conditional Distr



**Corollary 1.6.9** (Conditional PDF of Maximum Given Endpoint)

Given $W_t = w$, the conditional density of $M_t$ is:

$$f_{M_t | W_t}(m | w) = \frac{f_{M_t, W_t}(m, w)}{f_{W_t}(w)} = \frac{2(2m - w)}{t} \exp\left(-\frac{2m(m - w)}{t}\right)$$



for $m \ge w$.

**Proof:**


$$f_{W_t}(w) = \frac{1}{\sqrt{2\pi t}} e^{-w^2/(2t)}$$




$$f_{M_t | W_t}(m | w) = \frac{f_{M_t, W_t}(m, w)}{f_{W_t}(w)} = \frac{\frac{2(2m-w)}{t\sqrt{2\pi t}} e^{-(2m-w)^2/(2t)}}{\frac{1}{\sqrt{2\pi t}} e^{-w^2/(2t)}}$$



Simplify the exponentials:

$$\frac{-(2m-w)^2/(2t) + w^2/(2t)}{1} = \frac{-4m^2 + 4mw - w^2 + w^2}{2t} = \frac{-4m^2 + 4mw}{2t} = -\frac{2m(m-w)}{t}$$



Therefore:

$$f_{M_t | W_t}(m | w) = \frac{2(2m - w)}{t} e^{-2m(m-w)/t} \quad \square$$



## Applications



### 1. Application 1 Bar



A **knock-out barrier option** pays off only if the underlying asset never crosses a barrier $B > S_0$ before maturity.

Under the Black-Scholes model:

$$S_t = S_0 e^{(r - \sigma^2/2)t + \sigma W_t}$$



The asset hits the barrier if:

$$\max_{0 \le s \le T} S_s \ge B \iff \max_{0 \le s \le T} W_s \ge \frac{\log(B/S_0) - (r - \sigma^2/2)T}{\sigma} =: a$$



By the reflection principle:

$$\mathbb{P}(\text{knock-out}) = \mathbb{P}(M_T < a) = 1 - 2\Phi\left(-\frac{a}{\sqrt{T}}\right)$$



### 2. Application 2 Sur



In **credit risk**, the default time can be modeled as the first passage of a log-asset value to a default boundary.

If default occurs when the firm value hits level $D$:

$$\tau_D = \inf\{t \ge 0 : V_t = D\}$$



The survival probability is:

$$\mathbb{P}(\tau_D > T) = 1 - 2\Phi\left(-\frac{D}{\sqrt{T}}\right)$$



### 3. Application 3 Dra



The **maximum drawdown** from peak to trough is:

$$DD_t = M_t - W_t$$



The joint distribution $f_{M_t, W_t}(m, w)$ allows computation of drawdown probabilities for portfolio risk management.

### 4. Application 4 Per



For a **perpetual American put** with strike $K$, the optimal exercise boundary $b^*$ satisfies:

$$\mathbb{E}[e^{-r\tau_b}(K - S_{\tau_b})^+]$$



Using the Laplace transform $\mathbb{E}[e^{-\alpha \tau_a}] = e^{-a\sqrt{2\alpha}}$, one can derive the optimal stopping rule.

## Summary



The reflection principle is a fundamental tool for analyzing path-dependent properties of Brownian motion:

1. **Maximum distribution**: $\mathbb{P}(M_t \ge a) = 2\mathbb{P}(W_t \ge a)$
2. **First passage time**: $f_{\tau_a}(t) = \frac{a}{\sqrt{2\pi t^3}} e^{-a^2/(2t)}$ (Lévy distribution)
3. **Laplace transform**: $\mathbb{E}[e^{-\alpha \tau_a}] = e^{-a\sqrt{2\alpha}}$
4. **Joint distribution**: $f_{M_t, W_t}(m, w) = \frac{2(2m-w)}{t\sqrt{2\pi t}} e^{-(2m-w)^2/(2t)}$

**Key insights:**
- **Geometric reflection** exploits symmetry to create path bijections
- **Exponential martingales** provide alternative derivations via optional stopping
- Applications span barrier options, credit risk, and portfolio management

**Looking ahead:**
- **Girsanov theorem** (Chapter 1.8): Change of measure for barrier options
- **Optimal stopping** (advanced): American option pricing
- **Local time** (advanced): Fine structure of hitting times

## Exercises



1. Verify that $\int_0^\infty f_{\tau_a}(t) dt = 1$ for the Lévy distribution.

2. Show that $\mathbb{P}(\tau_a \le t, \tau_b \le t) = 0$ for $a, b > 0$ with $a \neq b$.

3. Compute $\mathbb{E}[M_T | W_T = w]$ using the conditional density.

4. For a knock-in barrier option, derive the payoff probability using the reflection principle.

5. Verify the Laplace transform formula by integrating $\int_0^\infty e^{-\alpha t} f_{\tau_a}(t) dt$ directly.

6. Show that the joint density integrates to 1: $\int_0^\infty \int_{-\infty}^m f_{M_t, W_t}(m, w) dw \, dm = 1$.

## References



- Karatzas, I., & Shreve, S. E. (1991). *Brownian Motion and Stochastic Calculus*, 2nd ed. Springer. (Chapter 3, Section 6)
- Revuz, D., & Yor, M. (1999). *Continuous Martingales and Brownian Motion*, 3rd ed. Springer. (Chapter VI)
- Mörters, P., & Peres, Y. (2010). *Brownian Motion*. Cambridge University Press. (Chapter 3)
- Shreve, S. E. (2004). *Stochastic Calculus for Finance II: Continuous-Time Models*. Springer. (Chapter 7 - Barrier Options)
