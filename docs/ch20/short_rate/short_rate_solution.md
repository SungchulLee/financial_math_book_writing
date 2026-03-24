# Hull-White Short Rate

## Hull-White Model

$$\begin{array}{lllll}
\displaystyle
dr(t)=\lambda\left(\theta^\mathbb{Q}(t)-r(t)\right) dt+\sigma dW^{\mathbb{Q}}(t)
\end{array}$$

where

$$
\displaystyle
\theta^\mathbb{Q}(t)
=
f^M(0,t)
+\frac{1}{\lambda}\frac{\partial f^M(0,t)}{\partial t}
+\frac{\sigma^2}{2\lambda^2}\left(1-e^{-2\lambda t}\right)
$$

???+ note "Proof"

    $$\begin{array}{lllll}
    \displaystyle
    \sigma(t)=\sigma(t,t)=\sigma
    \end{array}$$

    $$\begin{array}{lllll}
    \displaystyle
    \mu(t)
    &=&\displaystyle
    \mu(t,t)+
    \frac{\partial f(0,t)}{\partial t}
    +\int_0^t\frac{\partial \mu(t',t)}{\partial t}dt'
    +\int_0^t\frac{\partial \sigma(t',t)}{\partial t}dW^{\mathbb{Q}}(t')\\
    &=&\displaystyle
    \frac{\partial f(0,t)}{\partial t}
    +\int_0^t\left[2\sigma^2e^{-2\lambda(t-t')}
    -\sigma^2e^{-\lambda(t-t')}\right]dt'
    -\lambda \int_0^t\sigma(t',t)dW^{\mathbb{Q}}(t')\\
    &=&\displaystyle
    \frac{\partial f(0,t)}{\partial t}
    +\frac{\sigma^2}{\lambda}e^{-2\lambda t}\left(e^{\lambda t}-1\right)-\lambda \int_0^t\sigma(t',t)dW^{\mathbb{Q}}(t')\\
    \end{array}$$

    **Handling the stochastic integral term:**

    $$\begin{array}{l}
    \displaystyle
    r(t)
    =
    f(t,t)
    =
    f(0,t)+\int_0^t\mu(t',t)dt'+\int_0^t\sigma(t',t)dW^{\mathbb{Q}}(t')
    \end{array}$$

    implies

    $$\begin{array}{llllllll}
    \displaystyle
    \int_0^t\sigma(t',t)dW^{\mathbb{Q}}(t')
    &=&\displaystyle
    r(t)-f(0,t)-\frac{\sigma^2}{2\lambda^2}e^{-2\lambda t}\left(e^{\lambda t}-1\right)^2
    \end{array}$$

    Substituting back:

    $$\begin{array}{lllll}
    \displaystyle
    \mu(t)
    &=&\displaystyle
    \lambda\left(
    f(0,t)
    +\frac{1}{\lambda}\frac{\partial f(0,t)}{\partial t}
    +\frac{\sigma^2}{2\lambda^2}\left(1-e^{-2\lambda t}\right)
    -r(t)
    \right)\\
    &:=&\displaystyle
    \lambda\left(
    \theta(t)
    -r(t)
    \right)\\
    \end{array}$$

## Hull-White Model Solution

$$\begin{array}{lllll}
\displaystyle
r(t)
&=&\displaystyle
r(s)e^{-\lambda (t-s)}+ \lambda\int_{s}^t\theta^\mathbb{Q}(t')e^{-\lambda (t-t')} dt'+\sigma \int_{s}^t e^{-\lambda (t-t')} dW^{\mathbb{Q}}(t')\\
&=&\displaystyle
r(s)e^{-\lambda (t-s)}+ \alpha(t)-\alpha(s)e^{-\lambda(t-s)}+\sigma \int_{s}^t e^{-\lambda (t-t')} dW^{\mathbb{Q}}(t')\\
\end{array}$$

where

$$
\displaystyle
\alpha(t)=f^M(0,t)+\frac{\sigma^2}{2\lambda^2}\left(1-e^{-\lambda t}\right)^2
$$

Therefore, $r(t)$ conditional on ${\cal F}(s)$ is normally distributed with mean and variance:

$$\begin{array}{lllll}
\displaystyle
\mathbb{E}\left(r(t)|{\cal F}(s)\right)
&=&\displaystyle
r(s)e^{-\lambda (t-s)}+ \alpha(t)-\alpha(s)e^{-\lambda(t-s)}\\
\mathbb{Var}\left(r(t)|{\cal F}(s)\right)
&=&\displaystyle
\frac{\sigma^2}{2\lambda}\left(1-e^{-2\lambda(t-s)}\right)
\end{array}$$

???+ note "Proof"

    $$\begin{array}{lllll}
    \displaystyle
    &&dr(t)=\lambda\left(\theta(t)-r(t)\right) dt+\sigma dW^{\mathbb{Q}}(t)\\
    \\
    &\Rightarrow&
    \displaystyle
    e^{\lambda t}dr(t) + \lambda r(t)e^{\lambda t}  dt=\lambda\theta(t)e^{\lambda t}  dt+\sigma e^{\lambda t} dW^{\mathbb{Q}}(t)\quad(y(t)=r(t)e^{\lambda t})\\
    \\
    &\Rightarrow&
    \displaystyle
    dy(t)=\lambda\theta(t)e^{\lambda t} dt+\sigma e^{\lambda t} dW^{\mathbb{Q}}(t)\\
    \\
    &\Rightarrow&
    \displaystyle
    r(t)
    =
    r(0)e^{-\lambda t}+ \lambda\int_0^t\theta(t')e^{-\lambda (t-t')} dt'+\sigma \int_0^t e^{-\lambda (t-t')} dW^{\mathbb{Q}}(t')\\
    \end{array}$$

    Therefore,

    $$\begin{array}{lllll}
    \displaystyle
    \mathbb{E}^\mathbb{Q}\left(r(t)\big|{\cal F}(0)\right)
    =
    r(0)e^{-\lambda t}+ \lambda\int_0^t\theta(t')e^{-\lambda (t-t')} dt'
    =
    \psi(t)\\
    \end{array}$$

    $$\begin{array}{lllll}
    \displaystyle
    \mathbb{Var}^\mathbb{Q}\left(r(t)\big|{\cal F}(0)\right)
    =
    \sigma^2 \int_0^t e^{-2\lambda (t-t')} dt'
    =
    \frac{\sigma^2}{2\lambda} \left(1-e^{-2\lambda t}\right)
    =-\frac{1}{2}\sigma^2 B(2t)
    \end{array}$$

## Hull-White Short Rate Sample Path

```python
import matplotlib.pyplot as plt

def main():
    hw = HullWhite(sigma=0.01, lambd=0.01, P=P_market)
    t, R, M = hw.generate_sample_paths(
        num_paths=20, num_steps=100, T=30, seed=42
    )

    plt.figure(figsize=(10, 4))
    plt.title("Hull-White Short Rate Sample Paths")
    for i in range(20):
        plt.plot(t, R[i, :], alpha=0.3, lw=0.5)
    plt.plot(t, R.mean(axis=0), 'k--', lw=2, label='Mean')
    plt.xlabel("Time")
    plt.ylabel("r(t)")
    plt.legend()
    plt.show()
```

---

## Exercises

**Exercise 1.** Starting from the Hull-White SDE $dr(t) = \lambda(\theta^{\mathbb{Q}}(t) - r(t))\,dt + \sigma\,dW^{\mathbb{Q}}(t)$, derive the explicit solution using the integrating factor $e^{\lambda t}$. Show every step of the derivation.

---

**Exercise 2.** Verify that $\alpha(t) = f^M(0,t) + \frac{\sigma^2}{2\lambda^2}(1 - e^{-\lambda t})^2$ satisfies $\alpha(0) = r_0 = f^M(0,0)$. Then show that $\alpha(t)$ is the conditional mean $\mathbb{E}^{\mathbb{Q}}[r(t) | \mathcal{F}(0)]$.

---

**Exercise 3.** For $\lambda = 0.05$, $\sigma = 0.01$, $r(0) = 0.03$, and a flat forward curve $f^M(0,t) = 0.03$, compute $\mathbb{E}[r(t) | \mathcal{F}(0)]$ and $\text{Var}[r(t) | \mathcal{F}(0)]$ at $t = 1, 10, 50$. Plot the mean and the 95% confidence band.

---

**Exercise 4.** Show that the conditional variance $\frac{\sigma^2}{2\lambda}(1 - e^{-2\lambda(t-s)})$ can also be written as $-\frac{1}{2}\sigma^2 B(2(t-s))$ where $B(\tau) = (e^{-\lambda\tau} - 1)/\lambda$. Interpret the relationship between the variance and the bond price function $B$.

---

**Exercise 5.** The sample path code uses `hw.generate_sample_paths` to simulate 20 paths over 30 years. Describe the Euler-Maruyama discretization used for this simulation and explain why exact simulation (using the transition density) would be preferable.

---

**Exercise 6.** Derive the autocovariance function $\text{Cov}(r(t), r(t+h))$ for $h > 0$ in the Hull-White model. Show that it decays exponentially with lag $h$.
