# Black–Scholes PDE via Change of Numéraire


The Black–Scholes PDE can be derived without any delta-hedging or replication argument. Instead, one chooses the **stock as numéraire**, constructs the associated martingale measure via Girsanov's theorem, and imposes the condition that the normalized option price is a martingale. The PDE then emerges from setting the drift of this martingale to zero.

This derivation is conceptually distinct from the classical approaches (self-financing replication, risk-neutral pricing with the money market numéraire) and demonstrates the power of the [change-of-numéraire framework](../fundamental_theorem_of_asset_pricing/numeraire_and_change_of_measure.md). The fact that a different numéraire and a different measure yield the same PDE is a concrete manifestation of pricing invariance.


## Setup


We work in the standard Black–Scholes model. Under the physical measure $\mathbb{P}$:

$$dS_t = \mu S_t\, dt + \sigma S_t\, dW_t$$

with constant parameters $\mu, \sigma > 0$, and a money market account $B_t = e^{rt}$ with constant rate $r$. Under the risk-neutral measure $\mathbb{Q}$ (the $B$-martingale measure):

$$dS_t = rS_t\, dt + \sigma S_t\, dW^{\mathbb{Q}}_t$$

We take the **stock** $S_t$ as numéraire and derive the associated measure $\mathbb{Q}^S$, the stock dynamics under $\mathbb{Q}^S$, and ultimately the Black–Scholes PDE.


## Step 1: Density Process and Girsanov Transformation


### Radon–Nikodym Derivative

By the [change-of-numéraire theorem](../fundamental_theorem_of_asset_pricing/numeraire_and_change_of_measure.md#change-of-numéraire-theorem), the density process from $\mathbb{Q}$ to $\mathbb{Q}^S$ is

$$Z_t = \frac{d\mathbb{Q}^S}{d\mathbb{Q}}\bigg|_{\mathcal{F}_t} = \frac{S_t / S_0}{B_t / B_0} = \frac{S_t e^{-rt}}{S_0}$$

### Dynamics of $Z_t$

Apply Itô's product rule to $Z_t = (e^{-rt}/S_0) \cdot S_t$. Since $e^{-rt}$ is of bounded variation (zero quadratic variation), the cross-variation vanishes:

$$dZ_t = \frac{e^{-rt}}{S_0}\, dS_t + \frac{S_t}{S_0}\, d(e^{-rt}) = \frac{e^{-rt}}{S_0}\bigl(rS_t\, dt + \sigma S_t\, dW^{\mathbb{Q}}_t\bigr) - \frac{rS_t e^{-rt}}{S_0}\, dt$$

The $r\, dt$ terms cancel:

$$dZ_t = \frac{\sigma S_t e^{-rt}}{S_0}\, dW^{\mathbb{Q}}_t = \sigma Z_t\, dW^{\mathbb{Q}}_t$$

Therefore

$$\frac{dZ_t}{Z_t} = \sigma\, dW^{\mathbb{Q}}_t$$

This is a driftless geometric Brownian motion: $Z_t = \mathcal{E}(\sigma W^{\mathbb{Q}})_t = \exp(\sigma W^{\mathbb{Q}}_t - \frac{1}{2}\sigma^2 t)$. Since $\mathbb{E}^{\mathbb{Q}}[Z_T] = 1$, the process $Z_t$ is a true martingale and defines a valid probability measure.

### Girsanov Transformation

Since the density process has volatility $\sigma$ (i.e., $dZ_t/Z_t = \sigma\, dW^{\mathbb{Q}}_t$), Girsanov's theorem gives the $\mathbb{Q}^S$-Brownian motion:

$$W^S_t = W^{\mathbb{Q}}_t - \sigma t$$


## Step 2: Dynamics Under the Stock Measure


### Stock Dynamics

Substitute $dW^{\mathbb{Q}}_t = dW^S_t + \sigma\, dt$:

$$dS_t = rS_t\, dt + \sigma S_t\bigl(dW^S_t + \sigma\, dt\bigr) = (r + \sigma^2)S_t\, dt + \sigma S_t\, dW^S_t$$

Under $\mathbb{Q}^S$, the stock drift increases from $r$ to $r + \sigma^2$. This is natural: the density $Z_T \propto S_T e^{-rT}$ up-weights paths where the stock performs well, increasing its expected growth rate.

### Verification: $B_t / S_t$ Is a $\mathbb{Q}^S$-Martingale

The defining property of $\mathbb{Q}^S$ is that all asset prices normalized by $S_t$ are martingales. We verify this for $B_t / S_t$.

Apply Itô's formula to $f(B_t, S_t) = B_t / S_t$, using $dB_t = rB_t\, dt$ and the $\mathbb{Q}^S$-dynamics of $S_t$:

$$d\!\left(\frac{B_t}{S_t}\right) = \frac{1}{S_t}\, dB_t - \frac{B_t}{S_t^2}\, dS_t + \frac{B_t}{S_t^3}\,(dS_t)^2$$

Computing each term:

$$= \frac{rB_t}{S_t}\, dt - \frac{B_t}{S_t}\bigl[(r + \sigma^2)\, dt + \sigma\, dW^S_t\bigr] + \frac{B_t}{S_t}\, \sigma^2\, dt$$

Collecting the drift:

$$\bigl[r - (r + \sigma^2) + \sigma^2\bigr]\frac{B_t}{S_t}\, dt = 0$$

The drift vanishes identically. Therefore

$$d\!\left(\frac{B_t}{S_t}\right) = -\frac{\sigma B_t}{S_t}\, dW^S_t$$

confirming $B_t / S_t$ is a $\mathbb{Q}^S$-martingale. $\checkmark$


## Step 3: The Martingale Condition for the Normalized Price


Let $V(S, t)$ denote the option price as a function of the stock price and time. Under $\mathbb{Q}^S$, the normalized price

$$u(S, t) = \frac{V(S, t)}{S}$$

must be a martingale. By Itô's formula applied to the process $u(S_t, t)$, the martingale condition requires the drift to vanish:

$$\frac{\partial u}{\partial t} + \mathcal{L}^S u = 0$$

where $\mathcal{L}^S$ is the **infinitesimal generator** of $S_t$ under $\mathbb{Q}^S$:

$$\mathcal{L}^S = (r + \sigma^2)S\, \frac{\partial}{\partial S} + \frac{1}{2}\sigma^2 S^2\, \frac{\partial^2}{\partial S^2}$$

This gives the **PDE for the normalized price**:

$$\frac{\partial u}{\partial t} + (r + \sigma^2)S\, \frac{\partial u}{\partial S} + \frac{1}{2}\sigma^2 S^2\, \frac{\partial^2 u}{\partial S^2} = 0 \qquad (\star)$$


## Step 4: Transform Back to $V$


Since $V = S \cdot u$, express the derivatives of $u$ in terms of $V$:

$$\frac{\partial u}{\partial t} = \frac{1}{S}\frac{\partial V}{\partial t}$$

$$\frac{\partial u}{\partial S} = \frac{1}{S}\frac{\partial V}{\partial S} - \frac{V}{S^2}$$

$$\frac{\partial^2 u}{\partial S^2} = \frac{1}{S}\frac{\partial^2 V}{\partial S^2} - \frac{2}{S^2}\frac{\partial V}{\partial S} + \frac{2V}{S^3}$$

Substitute into $(\star)$. We group the contributions of each term:

**First-order term:**

$$(r + \sigma^2)S \cdot \frac{\partial u}{\partial S} = (r + \sigma^2)S\left(\frac{1}{S}\frac{\partial V}{\partial S} - \frac{V}{S^2}\right) = (r + \sigma^2)\frac{\partial V}{\partial S} - (r + \sigma^2)\frac{V}{S}$$

**Second-order term:**

$$\frac{1}{2}\sigma^2 S^2 \cdot \frac{\partial^2 u}{\partial S^2} = \frac{1}{2}\sigma^2 S^2\left(\frac{1}{S}\frac{\partial^2 V}{\partial S^2} - \frac{2}{S^2}\frac{\partial V}{\partial S} + \frac{2V}{S^3}\right) = \frac{1}{2}\sigma^2 S\frac{\partial^2 V}{\partial S^2} - \sigma^2\frac{\partial V}{\partial S} + \frac{\sigma^2 V}{S}$$

**Assemble the PDE** (after multiplying the time-derivative term $\frac{1}{S}\frac{\partial V}{\partial t}$ by $S$, i.e., multiplying the entire equation $(\star)$ through by $S$):

$$\frac{\partial V}{\partial t} + \underbrace{\bigl[(r + \sigma^2) - \sigma^2\bigr]}_{= \, r} S\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2\frac{\partial^2 V}{\partial S^2} + \underbrace{\bigl[-(r + \sigma^2) + \sigma^2\bigr]}_{= \, -r} V = 0$$

The $\sigma^2$ terms from the stock-measure drift and the Itô correction cancel perfectly, leaving:

$$\boxed{\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2\frac{\partial^2 V}{\partial S^2} - rV = 0}$$

This is the **Black–Scholes PDE**—derived without any replication or hedging argument.

!!! note "Pricing invariance"
    The normalized price $u = V/S$ satisfies a PDE with drift coefficient $r + \sigma^2$ (reflecting the stock-measure dynamics), but the option price $V$ itself satisfies the standard Black–Scholes PDE with drift coefficient $r$ (the risk-neutral drift). The cancellation of $\sigma^2$ in the transformation is exact and guaranteed by the change-of-numéraire theorem: different numéraires give different PDEs for the normalized price, but the same PDE for $V$.


## Byproduct: Black–Scholes Formula as Two Probabilities


The stock-numéraire approach also yields an elegant decomposition of the Black–Scholes call price.

### Derivation

For a European call with payoff $(S_T - K)^+$, the stock-numéraire pricing formula gives

$$C_t = S_t\, \mathbb{E}^{\mathbb{Q}^S}\!\left[\frac{(S_T - K)^+}{S_T} \;\bigg|\; \mathcal{F}_t\right] = S_t\, \mathbb{E}^{\mathbb{Q}^S}\!\left[\mathbf{1}_{\{S_T > K\}}\!\left(1 - \frac{K}{S_T}\right) \;\bigg|\; \mathcal{F}_t\right]$$

Splitting the expectation:

$$C_t = S_t\, \mathbb{Q}^S(S_T > K \mid \mathcal{F}_t) - K\, \mathbb{E}^{\mathbb{Q}^S}\!\left[\frac{\mathbf{1}_{\{S_T > K\}}}{S_T} \;\bigg|\; \mathcal{F}_t\right]$$

For the second term, apply the abstract Bayes formula. Since $Z_t = S_t e^{-rt}/S_0$ and $Z_T = S_T e^{-rT}/S_0$:

$$\mathbb{E}^{\mathbb{Q}^S}\!\left[\frac{\mathbf{1}_{\{S_T > K\}}}{S_T} \;\bigg|\; \mathcal{F}_t\right] = \frac{1}{Z_t}\, \mathbb{E}^{\mathbb{Q}}\!\left[Z_T \cdot \frac{\mathbf{1}_{\{S_T > K\}}}{S_T} \;\bigg|\; \mathcal{F}_t\right] = \frac{1}{Z_t} \cdot \frac{e^{-rT}}{S_0}\, \mathbb{Q}(S_T > K \mid \mathcal{F}_t)$$

Substituting $S_0 Z_t = S_t e^{-rt}$:

$$= \frac{e^{-r(T-t)}}{S_t}\, \mathbb{Q}(S_T > K \mid \mathcal{F}_t)$$

Therefore:

$$C_t = S_t\, \mathbb{Q}^S(S_T > K \mid \mathcal{F}_t) - Ke^{-r(T-t)}\, \mathbb{Q}(S_T > K \mid \mathcal{F}_t)$$

### Identification with $N(d_1)$ and $N(d_2)$

Under $\mathbb{Q}$, the stock drift is $r$, so $\ln S_T \mid \mathcal{F}_t \sim \mathcal{N}\!\left(\ln S_t + (r - \tfrac{1}{2}\sigma^2)\tau,\; \sigma^2\tau\right)$ where $\tau = T - t$. Therefore

$$\mathbb{Q}(S_T > K \mid \mathcal{F}_t) = N(d_2), \qquad d_2 = \frac{\ln(S_t/K) + (r - \frac{1}{2}\sigma^2)\tau}{\sigma\sqrt{\tau}}$$

Under $\mathbb{Q}^S$, the stock drift is $r + \sigma^2$, so $\ln S_T \mid \mathcal{F}_t \sim \mathcal{N}\!\left(\ln S_t + (r + \tfrac{1}{2}\sigma^2)\tau,\; \sigma^2\tau\right)$ (the Itô correction gives mean $r + \sigma^2 - \frac{1}{2}\sigma^2 = r + \frac{1}{2}\sigma^2$). Therefore

$$\mathbb{Q}^S(S_T > K \mid \mathcal{F}_t) = N(d_1), \qquad d_1 = \frac{\ln(S_t/K) + (r + \frac{1}{2}\sigma^2)\tau}{\sigma\sqrt{\tau}} = d_2 + \sigma\sqrt{\tau}$$

Combining:

$$\boxed{C_t = S_t\, N(d_1) - Ke^{-r(T-t)}\, N(d_2)}$$

The Black–Scholes formula emerges with a transparent probabilistic interpretation: $N(d_1)$ is the probability of exercise under the stock measure $\mathbb{Q}^S$, and $N(d_2)$ is the probability of exercise under the risk-neutral measure $\mathbb{Q}$.

!!! note "Why $d_1 \neq d_2$"
    The two probabilities differ because they are computed under different measures. Under $\mathbb{Q}^S$, paths where $S_T$ is large are up-weighted (since $Z_T \propto S_T$), shifting the log-normal mean upward by $\sigma^2 \tau$ relative to $\mathbb{Q}$. This increases the exercise probability from $N(d_2)$ to $N(d_1) = N(d_2 + \sigma\sqrt{\tau})$.


## Summary of the Derivation


The logical structure is:

1. **Choose numéraire**: take $N_t = S_t$ (the stock).
2. **Construct the density process**: $Z_t = S_t e^{-rt}/S_0$, verify $dZ_t/Z_t = \sigma\, dW^{\mathbb{Q}}_t$.
3. **Apply Girsanov**: $W^S_t = W^{\mathbb{Q}}_t - \sigma t$ is a $\mathbb{Q}^S$-Brownian motion.
4. **Derive stock dynamics under $\mathbb{Q}^S$**: drift becomes $r + \sigma^2$.
5. **Impose the martingale condition**: $u = V/S$ satisfies $\partial_t u + \mathcal{L}^S u = 0$.
6. **Transform back to $V$**: the $\sigma^2$ terms cancel, yielding the Black–Scholes PDE.

This derivation is fundamentally different from the replication approach. It begins with measure theory (Girsanov's theorem, Radon–Nikodym derivatives) rather than self-financing portfolios, and obtains the PDE from a martingale condition rather than a hedging argument. The fact that both approaches yield the same equation reflects the deep connection between no-arbitrage pricing and martingale theory established by the [FTAP](../fundamental_theorem_of_asset_pricing/fundamental_theorem_of_asset_pricing.md).


## References

- Geman, H., El Karoui, N., and Rochet, J.-C. (1995). *Changes of numéraire, changes of probability measure, and option pricing.* Journal of Applied Probability, 32(2), 443–458.

- Shreve, S. E. (2004). *Stochastic Calculus for Finance II: Continuous-Time Models.* Springer.

- Björk, T. (2009). *Arbitrage Theory in Continuous Time.* 3rd edition, Oxford University Press.
