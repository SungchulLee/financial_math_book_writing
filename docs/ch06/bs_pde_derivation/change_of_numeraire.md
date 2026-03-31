# Black–Scholes PDE via Change of Numéraire


The Black–Scholes PDE can be derived without any delta-hedging or replication argument. Instead, one chooses the **stock as numéraire**, constructs the associated martingale measure via Girsanov's theorem, and imposes the condition that the normalized option price is a martingale. The PDE then emerges from setting the drift of this martingale to zero.

This derivation is conceptually distinct from the classical approaches (self-financing replication, risk-neutral pricing with the money market numéraire) and demonstrates the power of the [change-of-numéraire framework](../../ch01/fundamental_theorem_of_asset_pricing/numeraire_and_change_of_measure.md). The fact that a different numéraire and a different measure yield the same PDE is a concrete manifestation of pricing invariance.


## Setup


We work in the standard Black–Scholes model. Under the physical measure $\mathbb{P}$:

$$dS_t = \mu S_t\, dt + \sigma S_t\, dW_t$$

with constant parameters $\mu, \sigma > 0$, and a money market account $B_t = e^{rt}$ with constant rate $r$. Under the risk-neutral measure $\mathbb{Q}$ (the $B$-martingale measure):

$$dS_t = rS_t\, dt + \sigma S_t\, dW^{\mathbb{Q}}_t$$

We take the **stock** $S_t$ as numéraire and derive the associated measure $\mathbb{Q}^S$, the stock dynamics under $\mathbb{Q}^S$, and ultimately the Black–Scholes PDE.


## Step 1: Density Process and Girsanov Transformation


### Radon–Nikodym Derivative

By the [change-of-numéraire theorem](../../ch01/fundamental_theorem_of_asset_pricing/numeraire_and_change_of_measure.md), the density process from $\mathbb{Q}$ to $\mathbb{Q}^S$ is

$$Z_t = \frac{d\mathbb{Q}^S}{d\mathbb{Q}}\bigg|_{\mathcal{F}_t} = \frac{S_t / S_0}{B_t / B_0} = \frac{S_t e^{-rt}}{S_0}$$

### Dynamics of Z_t

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

### Verification: B_t / S_t Is a Q^S-Martingale

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


## Step 4: Transform Back to V


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

### Identification with N(d_1) and N(d_2)

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

This derivation is fundamentally different from the replication approach. It begins with measure theory (Girsanov's theorem, Radon–Nikodym derivatives) rather than self-financing portfolios, and obtains the PDE from a martingale condition rather than a hedging argument. The fact that both approaches yield the same equation reflects the deep connection between no-arbitrage pricing and martingale theory established by the [FTAP](../../ch01/fundamental_theorem_of_asset_pricing/fundamental_theorem_of_asset_pricing.md).


## References

- Geman, H., El Karoui, N., and Rochet, J.-C. (1995). *Changes of numéraire, changes of probability measure, and option pricing.* Journal of Applied Probability, 32(2), 443–458.

- Shreve, S. E. (2004). *Stochastic Calculus for Finance II: Continuous-Time Models.* Springer.

- Björk, T. (2009). *Arbitrage Theory in Continuous Time.* 3rd edition, Oxford University Press.

---

## Exercises

**Exercise 1.** Verify that the density process $Z_t = S_t e^{-rt}/S_0$ is a $\mathbb{Q}$-martingale by showing that $dZ_t / Z_t = \sigma \, dW_t^{\mathbb{Q}}$ (i.e., the drift vanishes under $\mathbb{Q}$). Compute $\mathbb{E}^{\mathbb{Q}}[Z_T]$ and confirm it equals 1.

---

**Exercise 2.** Under the stock measure $\mathbb{Q}^S$, the process $u_t = V(t, S_t)/S_t$ is a martingale. Apply Ito's lemma to $u_t$ using the stock dynamics under $\mathbb{Q}^S$ and show that setting the drift of $u_t$ to zero yields the Black-Scholes PDE for $V$.

---

**Exercise 3.** Explain why $d_1 \neq d_2$ in the Black-Scholes formula from the change-of-numeraire perspective. Under $\mathbb{Q}^S$, what is the distribution of $\ln S_T$, and how does it differ from the distribution under $\mathbb{Q}$?

---

**Exercise 4.** The change-of-numeraire approach does not require constructing a self-financing portfolio. Compare the logical structure of this derivation with the delta-hedging derivation. In particular, identify which assumption (no-arbitrage, completeness, or Girsanov's theorem) plays the role that the hedging argument plays in the classical approach.

---

**Exercise 5.** Suppose the stock pays a continuous dividend yield $q$. Repeat the change-of-numeraire derivation with $S_t$ as numeraire and show that the PDE becomes $\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + (r-q)S\frac{\partial V}{\partial S} - rV = 0$.

---

## Solutions

??? success "Solution to Exercise 1"
    Under $\mathbb{Q}$, the stock dynamics are $dS_t = rS_t\, dt + \sigma S_t\, dW_t^{\mathbb{Q}}$. The density process is $Z_t = S_t e^{-rt}/S_0$. Applying the product rule with $e^{-rt}/S_0$ (a deterministic, bounded-variation factor):

    $$dZ_t = \frac{e^{-rt}}{S_0}\, dS_t + \frac{S_t}{S_0}\, d(e^{-rt})$$

    Substituting the dynamics:

    $$dZ_t = \frac{e^{-rt}}{S_0}\bigl(rS_t\, dt + \sigma S_t\, dW_t^{\mathbb{Q}}\bigr) - \frac{rS_t e^{-rt}}{S_0}\, dt$$

    The $r\, dt$ terms cancel exactly:

    $$dZ_t = \frac{\sigma S_t e^{-rt}}{S_0}\, dW_t^{\mathbb{Q}} = \sigma Z_t\, dW_t^{\mathbb{Q}}$$

    Therefore $dZ_t / Z_t = \sigma\, dW_t^{\mathbb{Q}}$, which is driftless under $\mathbb{Q}$, confirming $Z_t$ is a $\mathbb{Q}$-local martingale.

    Solving the SDE: $Z_t = Z_0 \exp\!\bigl(\sigma W_t^{\mathbb{Q}} - \frac{1}{2}\sigma^2 t\bigr)$. Since $Z_0 = S_0 e^0 / S_0 = 1$, we have $Z_t = \exp\!\bigl(\sigma W_t^{\mathbb{Q}} - \frac{1}{2}\sigma^2 t\bigr)$. This is a Doléans-Dade exponential martingale. Computing the expectation:

    $$\mathbb{E}^{\mathbb{Q}}[Z_T] = \mathbb{E}^{\mathbb{Q}}\!\left[\exp\!\left(\sigma W_T^{\mathbb{Q}} - \frac{1}{2}\sigma^2 T\right)\right] = \exp\!\left(-\frac{1}{2}\sigma^2 T\right) \cdot \exp\!\left(\frac{1}{2}\sigma^2 T\right) = 1$$

    where we used the moment generating function $\mathbb{E}[e^{aW_T}] = e^{a^2 T/2}$. Since $\mathbb{E}^{\mathbb{Q}}[Z_T] = 1$, the process $Z_t$ is a true $\mathbb{Q}$-martingale and defines a valid probability measure $\mathbb{Q}^S$.

??? success "Solution to Exercise 2"
    Under $\mathbb{Q}^S$, the stock dynamics are $dS_t = (r + \sigma^2)S_t\, dt + \sigma S_t\, dW_t^S$. The normalized price is $u_t = V(t, S_t)/S_t$. Apply Itô's formula to $u(t, S) = V(t, S)/S$. We need the partial derivatives:

    $$\frac{\partial u}{\partial t} = \frac{1}{S}\frac{\partial V}{\partial t}$$

    $$\frac{\partial u}{\partial S} = \frac{1}{S}\frac{\partial V}{\partial S} - \frac{V}{S^2}$$

    $$\frac{\partial^2 u}{\partial S^2} = \frac{1}{S}\frac{\partial^2 V}{\partial S^2} - \frac{2}{S^2}\frac{\partial V}{\partial S} + \frac{2V}{S^3}$$

    The Itô expansion of $u(t, S_t)$ gives:

    $$du = \left(\frac{\partial u}{\partial t} + (r+\sigma^2)S\frac{\partial u}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 u}{\partial S^2}\right)dt + \sigma S \frac{\partial u}{\partial S}\, dW_t^S$$

    Setting the drift to zero (the martingale condition under $\mathbb{Q}^S$):

    $$\frac{\partial u}{\partial t} + (r+\sigma^2)S\frac{\partial u}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 u}{\partial S^2} = 0$$

    Substituting the derivatives of $u$ in terms of $V$ and multiplying through by $S$:

    $$\frac{\partial V}{\partial t} + (r+\sigma^2)\frac{\partial V}{\partial S} \cdot S - (r+\sigma^2)\frac{V}{S} \cdot S + \frac{1}{2}\sigma^2 S^2\!\left(\frac{1}{S}\frac{\partial^2 V}{\partial S^2} - \frac{2}{S^2}\frac{\partial V}{\partial S} + \frac{2V}{S^3}\right)\! S = 0$$

    Simplifying:

    $$\frac{\partial V}{\partial t} + \bigl[(r+\sigma^2) - \sigma^2\bigr]S\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + \bigl[-(r+\sigma^2) + \sigma^2\bigr]V = 0$$

    The $\sigma^2$ terms cancel in both brackets, yielding:

    $$\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} - rV = 0$$

    This is the Black–Scholes PDE.

??? success "Solution to Exercise 3"
    The quantities $d_1$ and $d_2$ differ because they are computed under different probability measures, $\mathbb{Q}^S$ and $\mathbb{Q}$ respectively, and these measures assign different drifts to $\ln S_T$.

    **Under $\mathbb{Q}$ (risk-neutral measure):** The stock dynamics are $dS_t = rS_t\, dt + \sigma S_t\, dW_t^{\mathbb{Q}}$. By Itô's formula applied to $\ln S_t$:

    $$\ln S_T \mid \mathcal{F}_t \sim \mathcal{N}\!\left(\ln S_t + \left(r - \tfrac{1}{2}\sigma^2\right)\tau,\; \sigma^2\tau\right)$$

    where $\tau = T - t$. The exercise probability under $\mathbb{Q}$ is:

    $$\mathbb{Q}(S_T > K \mid \mathcal{F}_t) = N(d_2), \qquad d_2 = \frac{\ln(S_t/K) + (r - \frac{1}{2}\sigma^2)\tau}{\sigma\sqrt{\tau}}$$

    **Under $\mathbb{Q}^S$ (stock measure):** The stock dynamics are $dS_t = (r + \sigma^2)S_t\, dt + \sigma S_t\, dW_t^S$. Applying Itô's formula to $\ln S_t$:

    $$\ln S_T \mid \mathcal{F}_t \sim \mathcal{N}\!\left(\ln S_t + \left(r + \tfrac{1}{2}\sigma^2\right)\tau,\; \sigma^2\tau\right)$$

    The mean of $\ln S_T$ under $\mathbb{Q}^S$ is shifted upward by $\sigma^2\tau$ compared to $\mathbb{Q}$, because the Itô correction to the log gives $r + \sigma^2 - \frac{1}{2}\sigma^2 = r + \frac{1}{2}\sigma^2$. The exercise probability under $\mathbb{Q}^S$ is:

    $$\mathbb{Q}^S(S_T > K \mid \mathcal{F}_t) = N(d_1), \qquad d_1 = \frac{\ln(S_t/K) + (r + \frac{1}{2}\sigma^2)\tau}{\sigma\sqrt{\tau}} = d_2 + \sigma\sqrt{\tau}$$

    The difference $d_1 - d_2 = \sigma\sqrt{\tau}$ arises because the Radon–Nikodym derivative $d\mathbb{Q}^S/d\mathbb{Q} \propto S_T e^{-rT}$ up-weights paths where the stock ends high, shifting the mean of $\ln S_T$ upward and increasing the in-the-money probability.

??? success "Solution to Exercise 4"
    **Delta-hedging derivation:** Constructs a portfolio $\Pi = V - \Delta S$, applies Itô's formula under $\mathbb{P}$, chooses $\Delta = \partial V / \partial S$ to eliminate the $dW$ term, then invokes the no-arbitrage condition $d\Pi = r\Pi\, dt$. The key ingredients are: (i) a self-financing (or freeze-and-rebalance) portfolio construction, (ii) the ability to trade continuously, and (iii) the no-arbitrage principle.

    **Change-of-numéraire derivation:** Chooses $S_t$ as numéraire, constructs the density process $Z_t = S_t e^{-rt}/S_0$, applies Girsanov's theorem to define $\mathbb{Q}^S$, and requires $V/S$ to be a $\mathbb{Q}^S$-martingale. No portfolio is constructed; the PDE emerges from setting the drift of the normalized price to zero.

    The **key structural difference** is that the hedging argument in the classical approach is replaced by **Girsanov's theorem** in the change-of-numéraire approach. Specifically:

    - In the delta-hedging approach, the choice $\Delta = V_S$ eliminates risk and removes the physical drift $\mu$ from the PDE. The no-arbitrage condition then determines the discount rate.
    - In the change-of-numéraire approach, Girsanov's theorem absorbs the measure change from $\mathbb{Q}$ to $\mathbb{Q}^S$, modifying the stock drift from $r$ to $r + \sigma^2$. The martingale condition on $V/S$ then yields the PDE, and the $\sigma^2$ terms cancel when transforming back to $V$.

    Both approaches implicitly rely on **completeness** (to ensure uniqueness of the pricing measure) and **no-arbitrage** (to ensure existence of the measure). However, the change-of-numéraire approach makes the measure-theoretic structure explicit—Girsanov's theorem is the mathematical tool that plays the role of the hedging argument.

??? success "Solution to Exercise 5"
    With a continuous dividend yield $q$, the stock price satisfies $dS_t = (r - q)S_t\, dt + \sigma S_t\, dW_t^{\mathbb{Q}}$ under the risk-neutral measure $\mathbb{Q}$. The total return process (reinvesting dividends) is $\tilde{S}_t = e^{qt} S_t$, and the money market account is $B_t = e^{rt}$.

    **Density process.** Using $S_t$ as numéraire, the density from $\mathbb{Q}$ to $\mathbb{Q}^S$ is:

    $$Z_t = \frac{\tilde{S}_t / \tilde{S}_0}{B_t / B_0} = \frac{e^{qt} S_t e^{-rt}}{S_0} = \frac{S_t e^{-(r-q)t}}{S_0}$$

    Apply Itô's formula. Since $dS_t = (r-q)S_t\, dt + \sigma S_t\, dW_t^{\mathbb{Q}}$:

    $$dZ_t = \frac{e^{-(r-q)t}}{S_0}\, dS_t - \frac{(r-q)S_t e^{-(r-q)t}}{S_0}\, dt = \sigma Z_t\, dW_t^{\mathbb{Q}}$$

    The $(r-q)\, dt$ terms cancel, so $dZ_t/Z_t = \sigma\, dW_t^{\mathbb{Q}}$ and $Z_t$ is a $\mathbb{Q}$-martingale.

    **Girsanov transformation.** Define $W_t^S = W_t^{\mathbb{Q}} - \sigma t$, which is a $\mathbb{Q}^S$-Brownian motion.

    **Stock dynamics under $\mathbb{Q}^S$.** Substituting $dW_t^{\mathbb{Q}} = dW_t^S + \sigma\, dt$:

    $$dS_t = (r - q)S_t\, dt + \sigma S_t(dW_t^S + \sigma\, dt) = (r - q + \sigma^2)S_t\, dt + \sigma S_t\, dW_t^S$$

    **Martingale condition.** The normalized price $u = V/S$ must be a $\mathbb{Q}^S$-martingale. By Itô's formula, the drift of $u(t, S_t)$ must vanish:

    $$\frac{\partial u}{\partial t} + (r - q + \sigma^2)S\frac{\partial u}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 u}{\partial S^2} = 0$$

    **Transform back to $V$.** Substituting the derivatives of $u = V/S$ in terms of $V$ (identical to the non-dividend case) and multiplying through by $S$:

    $$\frac{\partial V}{\partial t} + \bigl[(r - q + \sigma^2) - \sigma^2\bigr]S\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + \bigl[-(r - q + \sigma^2) + \sigma^2\bigr]V = 0$$

    The $\sigma^2$ terms cancel:

    $$\frac{\partial V}{\partial t} + (r-q)S\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} - rV = 0$$

    This is the Black–Scholes PDE with continuous dividend yield $q$, where the drift coefficient is $r - q$ and the discounting term remains $-rV$.
