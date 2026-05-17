# Hull-White Short Rate

## Hull-White Model

Recall (see [§ HW model definition](../model_definition/hull_white_sde_and_mean_reversion.md)): the Hull-White SDE is

$$
dr(t)=\lambda\left(\theta^\mathbb{Q}(t)-r(t)\right) dt+\sigma dW^{\mathbb{Q}}(t)
$$

with $\theta^\mathbb{Q}(t)=f^M(0,t)+\frac{1}{\lambda}\partial_t f^M(0,t)+\frac{\sigma^2}{2\lambda^2}(1-e^{-2\lambda t})$ derived from the HJM no-arbitrage drift condition.

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

    Apply the integrating factor $e^{\lambda t}$ to the linear SDE (Recall (see [§ OU SDE](../../ch03/ito_lemma/ito_calculus_applications.md))). With $y(t)=r(t)e^{\lambda t}$:

    $$
    dy(t)=\lambda\theta(t)e^{\lambda t} dt+\sigma e^{\lambda t} dW^{\mathbb{Q}}(t)
    $$

    Integrating from $s$ to $t$ and dividing by $e^{\lambda t}$ yields the stated solution. The Gaussian mean and variance follow by taking expectation and applying the Ito isometry to $\sigma\int_s^t e^{-\lambda(t-t')}dW^{\mathbb{Q}}(t')$. Note $\mathbb{Var}=-\frac{1}{2}\sigma^2 B(2(t-s))$ with $B$ from [§ named functions](../named_functions/named_functions_definition.md).

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

??? success "Solution to Exercise 1"
    Starting from the Hull-White SDE:

    $$
    dr(t) = \lambda(\theta^{\mathbb{Q}}(t) - r(t))\,dt + \sigma\,dW^{\mathbb{Q}}(t)
    $$

    **Step 1: Apply the integrating factor.** Multiply both sides by $e^{\lambda t}$:

    $$
    e^{\lambda t}\,dr(t) + \lambda r(t) e^{\lambda t}\,dt = \lambda\theta^{\mathbb{Q}}(t) e^{\lambda t}\,dt + \sigma e^{\lambda t}\,dW^{\mathbb{Q}}(t)
    $$

    **Step 2: Recognize the product rule.** The left side is $d(r(t)e^{\lambda t})$ by the product rule for Ito processes (since $e^{\lambda t}$ is deterministic, there is no Ito correction). Define $y(t) = r(t)e^{\lambda t}$, so:

    $$
    dy(t) = \lambda\theta^{\mathbb{Q}}(t)e^{\lambda t}\,dt + \sigma e^{\lambda t}\,dW^{\mathbb{Q}}(t)
    $$

    **Step 3: Integrate from $s$ to $t$.** Integrating both sides:

    $$
    y(t) - y(s) = \lambda\int_s^t \theta^{\mathbb{Q}}(t')e^{\lambda t'}\,dt' + \sigma\int_s^t e^{\lambda t'}\,dW^{\mathbb{Q}}(t')
    $$

    **Step 4: Substitute back.** Since $y(t) = r(t)e^{\lambda t}$ and $y(s) = r(s)e^{\lambda s}$:

    $$
    r(t)e^{\lambda t} = r(s)e^{\lambda s} + \lambda\int_s^t \theta^{\mathbb{Q}}(t')e^{\lambda t'}\,dt' + \sigma\int_s^t e^{\lambda t'}\,dW^{\mathbb{Q}}(t')
    $$

    **Step 5: Divide by $e^{\lambda t}$:**

    $$
    r(t) = r(s)e^{-\lambda(t-s)} + \lambda\int_s^t \theta^{\mathbb{Q}}(t')e^{-\lambda(t-t')}\,dt' + \sigma\int_s^t e^{-\lambda(t-t')}\,dW^{\mathbb{Q}}(t')
    $$

    This is the explicit solution. The first term shows exponential decay of the initial condition, the second is the deterministic mean driven by $\theta^{\mathbb{Q}}$, and the third is the stochastic contribution filtered by the mean-reversion kernel.

---

**Exercise 2.** Verify that $\alpha(t) = f^M(0,t) + \frac{\sigma^2}{2\lambda^2}(1 - e^{-\lambda t})^2$ satisfies $\alpha(0) = r_0 = f^M(0,0)$. Then show that $\alpha(t)$ is the conditional mean $\mathbb{E}^{\mathbb{Q}}[r(t) | \mathcal{F}(0)]$.

??? success "Solution to Exercise 2"
    **Checking $\alpha(0)$:** Substituting $t = 0$:

    $$
    \alpha(0) = f^M(0,0) + \frac{\sigma^2}{2\lambda^2}(1 - e^0)^2 = f^M(0,0) + 0 = f^M(0,0) = r_0
    $$

    since the instantaneous forward rate at time zero equals the spot rate.

    **Showing $\alpha(t) = \mathbb{E}^{\mathbb{Q}}[r(t) | \mathcal{F}(0)]$:** From the explicit solution with $s = 0$:

    $$
    \mathbb{E}^{\mathbb{Q}}[r(t) | \mathcal{F}(0)] = r(0)e^{-\lambda t} + \lambda\int_0^t \theta^{\mathbb{Q}}(t')e^{-\lambda(t-t')}\,dt'
    $$

    Using $\theta^{\mathbb{Q}}(t) = f^M(0,t) + \frac{1}{\lambda}\frac{\partial f^M(0,t)}{\partial t} + \frac{\sigma^2}{2\lambda^2}(1 - e^{-2\lambda t})$, one can verify by direct integration (using integration by parts on the $f^M$ terms) that:

    $$
    r(0)e^{-\lambda t} + \lambda\int_0^t \theta^{\mathbb{Q}}(t')e^{-\lambda(t-t')}\,dt' = f^M(0,t) + \frac{\sigma^2}{2\lambda^2}(1 - e^{-\lambda t})^2 = \alpha(t)
    $$

    Alternatively, one can verify that $\alpha(t)$ satisfies the ODE $\alpha'(t) = \lambda(\theta^{\mathbb{Q}}(t) - \alpha(t))$ with $\alpha(0) = r_0$, which is exactly the equation for the conditional mean (obtained by taking expectations in the SDE). Since the ODE has a unique solution, $\alpha(t) = \mathbb{E}^{\mathbb{Q}}[r(t) | \mathcal{F}(0)]$.

---

**Exercise 3.** For $\lambda = 0.05$, $\sigma = 0.01$, $r(0) = 0.03$, and a flat forward curve $f^M(0,t) = 0.03$, compute $\mathbb{E}[r(t) | \mathcal{F}(0)]$ and $\text{Var}[r(t) | \mathcal{F}(0)]$ at $t = 1, 10, 50$. Plot the mean and the 95% confidence band.

??? success "Solution to Exercise 3"
    With a flat forward curve $f^M(0,t) = 0.03$, we have $\alpha(t) = 0.03 + \frac{(0.01)^2}{2(0.05)^2}(1 - e^{-0.05t})^2 = 0.03 + 0.02(1 - e^{-0.05t})^2$.

    The conditional mean and variance are:

    $$
    \mathbb{E}[r(t) | \mathcal{F}(0)] = \alpha(t) = 0.03 + 0.02(1 - e^{-0.05t})^2
    $$

    $$
    \text{Var}[r(t) | \mathcal{F}(0)] = \frac{\sigma^2}{2\lambda}(1 - e^{-2\lambda t}) = \frac{(0.01)^2}{0.10}(1 - e^{-0.10t}) = 0.001(1 - e^{-0.10t})
    $$

    **At $t = 1$:**

    $$
    \mu_1 = 0.03 + 0.02(1 - e^{-0.05})^2 = 0.03 + 0.02(0.04877)^2 \approx 0.03005
    $$

    $$
    \sigma_1^2 = 0.001(1 - e^{-0.10}) = 0.001 \times 0.09516 \approx 9.516 \times 10^{-5}, \quad \sigma_1 \approx 0.00976
    $$

    **At $t = 10$:**

    $$
    \mu_{10} = 0.03 + 0.02(1 - e^{-0.5})^2 = 0.03 + 0.02(0.3935)^2 \approx 0.03309
    $$

    $$
    \sigma_{10}^2 = 0.001(1 - e^{-1.0}) = 0.001 \times 0.6321 \approx 6.321 \times 10^{-4}, \quad \sigma_{10} \approx 0.02514
    $$

    **At $t = 50$:**

    $$
    \mu_{50} = 0.03 + 0.02(1 - e^{-2.5})^2 = 0.03 + 0.02(0.9179)^2 \approx 0.04685
    $$

    $$
    \sigma_{50}^2 = 0.001(1 - e^{-5.0}) = 0.001 \times 0.99326 \approx 9.933 \times 10^{-4}, \quad \sigma_{50} \approx 0.03152
    $$

    The 95% confidence band is $\mu_t \pm 1.96\sigma_t$. Note that the mean drifts upward due to the convexity correction, and the variance saturates at $\sigma^2/(2\lambda) = 0.001$ as $t \to \infty$.

---

**Exercise 4.** Show that the conditional variance $\frac{\sigma^2}{2\lambda}(1 - e^{-2\lambda(t-s)})$ can also be written as $-\frac{1}{2}\sigma^2 B(2(t-s))$ where $B(\tau) = (e^{-\lambda\tau} - 1)/\lambda$. Interpret the relationship between the variance and the bond price function $B$.

??? success "Solution to Exercise 4"
    Recall $B(\tau) = \frac{e^{-\lambda\tau} - 1}{\lambda} = -\frac{1 - e^{-\lambda\tau}}{\lambda}$. Substituting $\tau = 2(t-s)$:

    $$
    -\frac{1}{2}\sigma^2 B(2(t-s)) = -\frac{1}{2}\sigma^2 \cdot \frac{e^{-2\lambda(t-s)} - 1}{\lambda} = \frac{\sigma^2}{2\lambda}(1 - e^{-2\lambda(t-s)})
    $$

    This is exactly the conditional variance $\text{Var}(r(t) | \mathcal{F}(s))$.

    **Interpretation:** The function $B(\tau)$ appears in the affine bond price formula $P(t,T) = e^{A(\tau) + B(\tau)r(t)}$ where it measures the duration-like sensitivity of the bond price to $r(t)$. The variance of $r(t)$ can be expressed through $B$ evaluated at twice the time horizon because:

    - The variance involves $\int_s^t e^{-2\lambda(t-t')}\,dt'$, which has the same structure as $B$ but with $2\lambda$ replacing $\lambda$
    - The factor of $-\frac{1}{2}\sigma^2$ is a scaling that connects the diffusion coefficient $\sigma$ to the second moment
    - This relationship reflects the deep connection between the affine structure of the model (which produces exponential bond price functions) and the Gaussian distribution of the short rate

---

**Exercise 5.** The sample path code uses `hw.generate_sample_paths` to simulate 20 paths over 30 years. Describe the Euler-Maruyama discretization used for this simulation and explain why exact simulation (using the transition density) would be preferable.

??? success "Solution to Exercise 5"
    **Euler-Maruyama discretization:** Partition $[0, T]$ into $N$ steps with $\Delta t = T/N$. The scheme is:

    $$
    r(t_{k+1}) = r(t_k) + \lambda(\theta^{\mathbb{Q}}(t_k) - r(t_k))\Delta t + \sigma\sqrt{\Delta t}\,Z_k, \quad Z_k \sim \mathcal{N}(0,1)
    $$

    This introduces discretization error of order $O(\Delta t)$ in the weak sense and $O(\sqrt{\Delta t})$ in the strong sense.

    **Exact simulation:** Since the transition density is known in closed form:

    $$
    r(t_{k+1}) | r(t_k) \sim \mathcal{N}\!\left(r(t_k)e^{-\lambda\Delta t} + \alpha(t_{k+1}) - \alpha(t_k)e^{-\lambda\Delta t},\; \frac{\sigma^2}{2\lambda}(1 - e^{-2\lambda\Delta t})\right)
    $$

    one can simulate exactly:

    $$
    r(t_{k+1}) = \mu(t_k, t_{k+1}) + \Sigma(t_k, t_{k+1})\,Z_k
    $$

    **Why exact simulation is preferable:**

    - **No discretization error:** Euler-Maruyama accumulates error over each step; exact simulation gives the correct distribution regardless of step size
    - **Larger time steps:** With exact simulation, one can use $\Delta t = 1$ year (or even jump directly to maturity) without loss of accuracy, whereas Euler-Maruyama requires small $\Delta t$ for accuracy
    - **Computational savings:** Fewer steps means fewer random number generations and arithmetic operations
    - **Exact variance:** The Euler scheme slightly distorts the variance for finite $\Delta t$, while exact simulation preserves it exactly

---

**Exercise 6.** Derive the autocovariance function $\text{Cov}(r(t), r(t+h))$ for $h > 0$ in the Hull-White model. Show that it decays exponentially with lag $h$.

??? success "Solution to Exercise 6"
    From the explicit solution starting at $s = 0$:

    $$
    r(t) = r(0)e^{-\lambda t} + \lambda\int_0^t \theta^{\mathbb{Q}}(t')e^{-\lambda(t-t')}\,dt' + \sigma\int_0^t e^{-\lambda(t-t')}\,dW^{\mathbb{Q}}(t')
    $$

    The stochastic part is $X(t) = \sigma\int_0^t e^{-\lambda(t-t')}\,dW^{\mathbb{Q}}(t')$. Since the deterministic parts do not contribute to the covariance:

    $$
    \text{Cov}(r(t), r(t+h)) = \text{Cov}(X(t), X(t+h))
    $$

    Expanding:

    $$
    X(t+h) = \sigma\int_0^{t+h} e^{-\lambda(t+h-t')}\,dW^{\mathbb{Q}}(t') = \sigma\int_0^t e^{-\lambda(t+h-t')}\,dW^{\mathbb{Q}}(t') + \sigma\int_t^{t+h} e^{-\lambda(t+h-t')}\,dW^{\mathbb{Q}}(t')
    $$

    The second integral is independent of $\mathcal{F}(t)$, hence independent of $X(t)$. For the first integral, note $e^{-\lambda(t+h-t')} = e^{-\lambda h}e^{-\lambda(t-t')}$. Therefore:

    $$
    \text{Cov}(X(t), X(t+h)) = e^{-\lambda h}\,\text{Cov}\!\left(X(t),\, \sigma\int_0^t e^{-\lambda(t-t')}\,dW^{\mathbb{Q}}(t')\right) = e^{-\lambda h}\,\text{Var}(X(t))
    $$

    Using the Ito isometry:

    $$
    \text{Var}(X(t)) = \sigma^2\int_0^t e^{-2\lambda(t-t')}\,dt' = \frac{\sigma^2}{2\lambda}(1 - e^{-2\lambda t})
    $$

    Therefore:

    $$
    \text{Cov}(r(t), r(t+h)) = \frac{\sigma^2}{2\lambda}(1 - e^{-2\lambda t})\,e^{-\lambda h}
    $$

    The autocovariance decays exponentially with lag $h$ at rate $\lambda$. As $t \to \infty$, the stationary autocovariance is $\frac{\sigma^2}{2\lambda}e^{-\lambda h}$, which is the autocovariance of the stationary Ornstein-Uhlenbeck process.
