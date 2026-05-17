# Self-Financing Portfolios

In the discrete-time binomial model (Chapter 1), a replicating portfolio is rebalanced at each time step without injecting or withdrawing funds. The continuous-time analogue is the **self-financing condition**, which forms the trading-strategy infrastructure underlying the Black-Scholes hedging argument. This page collects the minimum needed to read the BS PDE derivations; the full development lives in [§ Self-Financing Replication](../bs_pde_derivation/replication.md).

!!! abstract "Learning Objectives"
    After completing this section, you should be able to:

    - State the self-financing condition in continuous time
    - Write the wealth dynamics of a portfolio of one stock and one bond
    - Recognize the discounted wealth as a $\mathbb{Q}$-local martingale
    - Connect self-financing replication to risk-neutral pricing

---

## Toy: Self-Financing in Two Periods

Before stating the continuous-time condition, see what it means in a tiny discrete example.

At date $0$, hold $\phi_0$ shares and $\psi_0$ bonds; wealth is $X_0 = \phi_0 S_0 + \psi_0 B_0$. At date $1$, after observing $(S_1, B_1)$, rebalance to $(\phi_1, \psi_1)$. Self-financing means the new position costs exactly what the old one is now worth:

$$
\phi_0 S_1 + \psi_0 B_1 = \phi_1 S_1 + \psi_1 B_1
$$

Equivalently, $(\phi_1 - \phi_0) S_1 + (\psi_1 - \psi_0) B_1 = 0$: the dollars spent buying extra shares are paid for entirely by selling bonds (or vice versa). No outside cash arrives, no dividend leaks out.

Two facts fall straight out of this toy:

- **Wealth changes only through asset moves.** Between rebalancings, $X$ moves because $S$ and $B$ move, not because the holdings change. Differencing,

    $$
    X_1 - X_0 = \phi_0(S_1 - S_0) + \psi_0(B_1 - B_0)
    $$

- **Rebalancing is invisible in $X$.** Even though $(\phi, \psi)$ changes at date $1$, $X$ has no jump at that instant.

The continuous-time self-financing condition $dX_t = \phi_t\,dS_t + \psi_t\,dB_t$ is the infinitesimal version of both facts at once: increments in $X$ come from the assets, and rebalancing leaves $X$ continuous. Everything in this page is the apparatus needed to make that infinitesimal statement rigorous when $(\phi, \psi)$ is rebalanced at every instant.

---

## The Market Model

Recall (see [§ Assumptions](assumptions.md) and [§ GBM as Asset-Price Model](gbm_as_asset_price_model.md)): the Black-Scholes market consists of a risk-free bond $dB_t = rB_t\,dt$ (so $B_t = e^{rt}$) and a risky stock $dS_t = \mu S_t\,dt + \sigma S_t\,dW_t$ on a filtered probability space $(\Omega, \mathcal{F}, \{\mathcal{F}_t\}, \mathbb{P})$.

A **trading strategy** is a pair of predictable processes $(\phi_t, \psi_t)$ specifying the number of shares of the stock and bond held at time $t$, with the standard $L^2$ integrability requirements that make the stochastic integrals well defined.

---

## Self-Financing Condition

The **wealth process** is $X_t = \phi_t S_t + \psi_t B_t$.

!!! info "Definition: Self-Financing Portfolio"
    A trading strategy $(\phi_t, \psi_t)$ is **self-financing** if

    $$
    dX_t = \phi_t\,dS_t + \psi_t\,dB_t
    $$

    equivalently (assuming the cross term $d\phi_t\,dS_t$ vanishes), $S_t\,d\phi_t + B_t\,d\psi_t = 0$: rebalancing is cost-neutral.

Recall (see [§ Self-Financing Replication](../bs_pde_derivation/replication.md)): the integral form, the role of the cross-variation term $d[\alpha, S]_t$, and the equivalence with the no-external-cashflow interpretation are developed there in full.

---

## Wealth Dynamics

Substituting $\psi_t = (X_t - \phi_t S_t)/B_t$ into the self-financing condition and using $dB_t = rB_t\,dt$:

$$
\boxed{dX_t = rX_t\,dt + \phi_t(dS_t - rS_t\,dt)}
$$

The wealth grows at the risk-free rate $r$ plus an **excess-return** term from the stock position. Substituting GBM dynamics:

$$
dX_t = rX_t\,dt + \phi_t S_t\left[(\mu - r)\,dt + \sigma\,dW_t\right]
$$

so $\mu - r$ is the **equity risk premium** and $\phi_t S_t$ is the dollar amount invested in stock.

---

## Discounted Wealth and Risk-Neutral Pricing

The **discounted wealth** $\tilde{X}_t = e^{-rt}X_t$ satisfies

$$
d\tilde{X}_t = \phi_t\,d\tilde{S}_t, \qquad \tilde{S}_t = e^{-rt}S_t
$$

Recall (see [§ Risk-Neutral Measure](../bs_pde_derivation/risk_neutral_measure.md)): Girsanov's theorem provides a measure $\mathbb{Q}$ under which $d\tilde{S}_t = \sigma\tilde{S}_t\,dW_t^{\mathbb{Q}}$ is a $\mathbb{Q}$-martingale, hence $\tilde{X}_t$ is a $\mathbb{Q}$-local martingale. Under standard integrability and admissibility ($X_t \geq -a$ for some $a > 0$), $\tilde{X}_t$ is a true martingale, and any replicable claim $H = h(S_T)$ has price

$$
V_0 = e^{-rT}\,\mathbb{E}^{\mathbb{Q}}[H]
$$

The explicit replicating strategy for a European derivative — $\phi_t = \partial V/\partial S$ (the delta) and $\psi_t = (V - \phi_t S_t)/B_t$ — is constructed in [§ Self-Financing Replication](../bs_pde_derivation/replication.md), where the martingale-representation theorem identifies $\phi_t$ uniquely.

---

## Summary

**1. Self-financing**: $dX_t = \phi_t\,dS_t + \psi_t\,dB_t$ — rebalancing without external cashflows.
**2. Wealth decomposition**: $dX_t = rX_t\,dt + \phi_t(dS_t - rS_t\,dt)$.
**3. Discounted wealth**: $d\tilde{X}_t = \phi_t\,d\tilde{S}_t$ is a $\mathbb{Q}$-local martingale.
**4. Pricing**: replicable claims satisfy $V_0 = e^{-rT}\mathbb{E}^{\mathbb{Q}}[H]$.

Full derivations, admissibility, doubling-strategy obstructions, completeness, and the MRT identification of the hedge ratio are in [§ Self-Financing Replication](../bs_pde_derivation/replication.md) and [§ Risk-Neutral Measure](../bs_pde_derivation/risk_neutral_measure.md).

---

## Exercises

**Exercise 1.** Let $\phi_t = 1$ (hold one share of stock) and $X_0 = S_0 + B$ for some constant $B > 0$. Determine the bond position $\psi_t$ and verify directly that the strategy is self-financing by checking that $S_t \, d\phi_t + B_t \, d\psi_t = 0$.

??? success "Solution to Exercise 1"
    With $\phi_t = 1$ (one share) and $X_0 = S_0 + B$ for some constant $B > 0$:

    The bond position is $\psi_t = (X_t - \phi_t S_t)/B_t = (X_t - S_t)/e^{rt}$.

    At $t = 0$: $\psi_0 = (S_0 + B - S_0)/1 = B$.

    Since $\phi_t = 1$ is constant, $d\phi_t = 0$, and we need to verify $S_t\,d\phi_t + B_t\,d\psi_t = 0$.

    The first term is $S_t \cdot 0 = 0$. For the second term, we compute $\psi_t$ explicitly.

    The wealth dynamics with $\phi_t = 1$ are:

    $$
    dX_t = rX_t\,dt + 1 \cdot (dS_t - rS_t\,dt) = rX_t\,dt + dS_t - rS_t\,dt
    $$

    The bond wealth is $\psi_t B_t = X_t - S_t$. Compute its differential:

    $$
    d(\psi_t B_t) = dX_t - dS_t = rX_t\,dt + dS_t - rS_t\,dt - dS_t = r(X_t - S_t)\,dt = r\psi_t B_t\,dt
    $$

    Since $d(\psi_t B_t) = \psi_t\,dB_t + B_t\,d\psi_t = r\psi_t B_t\,dt + B_t\,d\psi_t$, we get:

    $$
    B_t\,d\psi_t = r\psi_t B_t\,dt - r\psi_t B_t\,dt = 0
    $$

    Therefore $d\psi_t = 0$, meaning $\psi_t = \psi_0 = B$ for all $t$. Both the stock holding and bond holding are constant, confirming:

    $$
    S_t\,d\phi_t + B_t\,d\psi_t = 0 + 0 = 0 \quad \checkmark
    $$

    The strategy is self-financing. The portfolio simply holds one share and $B$ units of the bond, with both positions unchanged over time. $\square$

---
**Exercise 2.** Consider a self-financing portfolio with wealth dynamics $dX_t = rX_t \, dt + \phi_t(dS_t - rS_t \, dt)$. Suppose the trader invests a constant fraction $\pi$ of wealth in the stock, so $\phi_t S_t = \pi X_t$. Show that the wealth process satisfies

$$
dX_t = X_t\left[(r + \pi(\mu - r))\,dt + \pi\sigma\,dW_t\right]
$$

and solve this SDE explicitly for $X_t$.

??? success "Solution to Exercise 2"
    Given $\phi_t S_t = \pi X_t$ (constant fraction $\pi$ of wealth in stock), substitute into the wealth dynamics:

    $$
    dX_t = rX_t\,dt + \phi_t(dS_t - rS_t\,dt)
    $$

    Since $\phi_t = \pi X_t / S_t$, the excess return term becomes:

    $$
    \phi_t(dS_t - rS_t\,dt) = \frac{\pi X_t}{S_t}(dS_t - rS_t\,dt)
    $$

    Substituting $dS_t = \mu S_t\,dt + \sigma S_t\,dW_t$:

    $$
    = \frac{\pi X_t}{S_t}\left[(\mu - r)S_t\,dt + \sigma S_t\,dW_t\right] = \pi X_t\left[(\mu - r)\,dt + \sigma\,dW_t\right]
    $$

    Therefore:

    $$
    dX_t = rX_t\,dt + \pi X_t(\mu - r)\,dt + \pi X_t\sigma\,dW_t = X_t\left[(r + \pi(\mu - r))\,dt + \pi\sigma\,dW_t\right]
    $$

    This is a GBM with drift $r + \pi(\mu - r)$ and volatility $\pi\sigma$. The solution is:

    $$
    X_t = X_0\exp\!\left[\left(r + \pi(\mu - r) - \frac{1}{2}\pi^2\sigma^2\right)t + \pi\sigma W_t\right]
    $$

    This is the **Merton portfolio** result. The log-return is normally distributed with mean $(r + \pi(\mu - r) - \frac{1}{2}\pi^2\sigma^2)t$ and variance $\pi^2\sigma^2 t$. The optimal $\pi$ that maximizes the expected log-wealth growth rate is $\pi^* = (\mu - r)/\sigma^2$ (the Kelly criterion).

---
**Exercise 3.** Prove that if two self-financing portfolios $X_t$ and $Y_t$ satisfy $X_T = Y_T$ almost surely, then $X_t = Y_t$ for all $t \in [0,T]$ almost surely. Use the martingale property of the discounted wealth under $\mathbb{Q}$. Explain why this result is essential for the uniqueness of derivative prices.

??? success "Solution to Exercise 3"
    Suppose $X_t$ and $Y_t$ are both self-financing portfolios with $X_T = Y_T$ a.s.

    Define $Z_t = X_t - Y_t$. Then $Z_t$ is also a self-financing portfolio (the self-financing condition is linear), and $Z_T = 0$ a.s.

    The discounted wealth $\tilde{Z}_t = e^{-rt}Z_t$ is a local martingale under $\mathbb{Q}$ (since both $\tilde{X}_t$ and $\tilde{Y}_t$ are local martingales under $\mathbb{Q}$, and their difference is also a local martingale).

    Assuming both strategies are admissible (bounded credit), $\tilde{Z}_t$ is bounded below by some constant $-a$. A local martingale bounded below is a supermartingale. Similarly, $-\tilde{Z}_t$ is bounded below, so $-\tilde{Z}_t$ is also a supermartingale, which means $\tilde{Z}_t$ is a submartingale.

    A process that is both a supermartingale and a submartingale is a martingale. Therefore $\tilde{Z}_t$ is a true $\mathbb{Q}$-martingale.

    For a martingale with terminal value $\tilde{Z}_T = 0$:

    $$
    \tilde{Z}_t = \mathbb{E}^{\mathbb{Q}}[\tilde{Z}_T \mid \mathcal{F}_t] = \mathbb{E}^{\mathbb{Q}}[0 \mid \mathcal{F}_t] = 0 \quad \text{for all } t \in [0, T]
    $$

    Therefore $Z_t = e^{rt}\tilde{Z}_t = 0$ for all $t$, so $X_t = Y_t$ for all $t \in [0, T]$ a.s. $\square$

    **Importance for uniqueness**: This result guarantees that if a contingent claim $H$ is replicable, then the replication cost is unique. If two different self-financing strategies both replicate $H$ (i.e., $X_T = Y_T = H$), they must have the same initial cost $X_0 = Y_0$ and indeed the same value at all intermediate times. This ensures a unique arbitrage-free price for every replicable claim.

---
**Exercise 4.** Define the doubling strategy informally and explain how it appears to generate arbitrage in continuous time. Then explain precisely how the admissibility condition $X_t \geq -a$ prevents this strategy from being used.

??? success "Solution to Exercise 4"
    **The doubling strategy** (informally): Start with initial wealth 0. At each step, bet on the outcome of a fair coin flip, doubling the stake after each loss. Specifically, bet \$1; if you lose, bet \$2; if you lose again, bet \$4; and so on. The first win recovers all previous losses plus a \$1 profit. Since you eventually win with probability 1, this appears to generate a sure profit from nothing.

    In continuous time, this can be formalized: construct a self-financing strategy that starts with $X_0 = 0$ and achieves $X_T > 0$ with positive probability and $X_T \geq 0$ almost surely. This would constitute an arbitrage.

    **How it works mechanically**: The strategy invests increasingly large amounts in the risky asset after losses, funded by borrowing. The wealth process $X_t$ can become arbitrarily negative at intermediate times (the trader accumulates potentially enormous debts before the "winning" trade occurs).

    **How admissibility prevents it**: The admissibility condition requires $X_t \geq -a$ for some finite constant $a$ and all $t \in [0, T]$. This bounds the maximum allowable loss. The doubling strategy requires $X_t \to -\infty$ along certain paths (when the "winning" trade is delayed), which violates $X_t \geq -a$ for any finite $a$.

    Mathematically, admissibility ensures that the discounted wealth $\tilde{X}_t$ is a supermartingale under $\mathbb{Q}$ (not merely a local martingale). For a supermartingale starting at $\tilde{X}_0 = 0$:

    $$
    \mathbb{E}^{\mathbb{Q}}[\tilde{X}_T] \leq \tilde{X}_0 = 0
    $$

    Combined with $X_T \geq 0$ (no-bankruptcy at maturity), this forces $X_T = 0$ a.s. --- no profit is possible. The admissibility condition thus closes the loophole that makes the doubling strategy appear to work.

---
**Exercise 5.** For a European call with Black-Scholes price $V(S_t, t) = S_t \mathcal{N}(d_1) - Ke^{-r(T-t)}\mathcal{N}(d_2)$, write down the replicating portfolio $(\phi_t, \psi_t)$ explicitly. Verify that at $t = 0$ the portfolio value equals $V(S_0, 0)$, and at $t = T$ the portfolio value equals $(S_T - K)^+$.

??? success "Solution to Exercise 5"
    The Black-Scholes call price is $V(S_t, t) = S_t\mathcal{N}(d_1) - Ke^{-r(T-t)}\mathcal{N}(d_2)$ where:

    $$
    d_1 = \frac{\ln(S_t/K) + (r + \frac{1}{2}\sigma^2)(T-t)}{\sigma\sqrt{T-t}}, \quad d_2 = d_1 - \sigma\sqrt{T-t}
    $$

    **Replicating portfolio**:

    $$
    \phi_t = \frac{\partial V}{\partial S}(S_t, t) = \mathcal{N}(d_1)
    $$

    $$
    \psi_t = \frac{V(S_t, t) - \phi_t S_t}{B_t} = \frac{S_t\mathcal{N}(d_1) - Ke^{-r(T-t)}\mathcal{N}(d_2) - \mathcal{N}(d_1)S_t}{e^{rt}} = \frac{-Ke^{-r(T-t)}\mathcal{N}(d_2)}{e^{rt}}
    $$

    $$
    = -Ke^{-rT}\mathcal{N}(d_2)
    $$

    **Verification at $t = 0$**: The portfolio value is:

    $$
    \phi_0 S_0 + \psi_0 B_0 = \mathcal{N}(d_1^0)S_0 + (-Ke^{-rT}\mathcal{N}(d_2^0)) \cdot 1 = S_0\mathcal{N}(d_1^0) - Ke^{-rT}\mathcal{N}(d_2^0) = V(S_0, 0) \quad \checkmark
    $$

    **Verification at $t = T$**: As $t \to T^-$, there are two cases:

    - If $S_T > K$: Then $d_1, d_2 \to +\infty$, so $\mathcal{N}(d_1) \to 1$ and $\mathcal{N}(d_2) \to 1$. The portfolio value is $1 \cdot S_T + (-K \cdot 1) = S_T - K = (S_T - K)^+$. $\checkmark$

    - If $S_T < K$: Then $d_1, d_2 \to -\infty$, so $\mathcal{N}(d_1) \to 0$ and $\mathcal{N}(d_2) \to 0$. The portfolio value is $0 \cdot S_T + 0 = 0 = (S_T - K)^+$. $\checkmark$

    In both cases, $X_T = (S_T - K)^+$, confirming exact replication. $\square$

---
**Exercise 6.** Show that the discounted stock price $\tilde{S}_t = e^{-rt}S_t$ satisfies

$$
d\tilde{S}_t = (\mu - r)\tilde{S}_t \, dt + \sigma \tilde{S}_t \, dW_t
$$

under the physical measure $\mathbb{P}$. Explain why $\tilde{S}_t$ is not a martingale under $\mathbb{P}$ (assuming $\mu \neq r$) and identify the Girsanov change of measure that makes it a martingale.

??? success "Solution to Exercise 6"
    Apply the product rule to $\tilde{S}_t = e^{-rt}S_t$:

    $$
    d\tilde{S}_t = e^{-rt}\,dS_t + S_t\,d(e^{-rt}) = e^{-rt}\,dS_t - rS_te^{-rt}\,dt
    $$

    $$
    = e^{-rt}(\mu S_t\,dt + \sigma S_t\,dW_t) - re^{-rt}S_t\,dt
    $$

    $$
    = (\mu - r)e^{-rt}S_t\,dt + \sigma e^{-rt}S_t\,dW_t
    $$

    $$
    = (\mu - r)\tilde{S}_t\,dt + \sigma\tilde{S}_t\,dW_t \quad \square
    $$

    **Why $\tilde{S}_t$ is not a martingale under $\mathbb{P}$**: A martingale must have zero drift. Under $\mathbb{P}$, $\tilde{S}_t$ has drift $(\mu - r)\tilde{S}_t$, which is nonzero when $\mu \neq r$. Consequently:

    $$
    \mathbb{E}^{\mathbb{P}}[\tilde{S}_t \mid \mathcal{F}_s] = \tilde{S}_s\,e^{(\mu - r)(t - s)} \neq \tilde{S}_s
    $$

    so the martingale property fails.

    **Girsanov change of measure**: Define the market price of risk $\theta = (\mu - r)/\sigma$ and the new Brownian motion:

    $$
    dW_t^{\mathbb{Q}} = dW_t + \theta\,dt = dW_t + \frac{\mu - r}{\sigma}\,dt
    $$

    Under the risk-neutral measure $\mathbb{Q}$, defined by the Radon–Nikodym derivative:

    $$
    \frac{d\mathbb{Q}}{d\mathbb{P}}\bigg|_{\mathcal{F}_t} = \exp\!\left(-\theta W_t - \frac{1}{2}\theta^2 t\right)
    $$

    the process $W_t^{\mathbb{Q}}$ is a standard Brownian motion (by Girsanov's theorem), and:

    $$
    d\tilde{S}_t = (\mu - r)\tilde{S}_t\,dt + \sigma\tilde{S}_t\,(dW_t^{\mathbb{Q}} - \theta\,dt)
    $$

    $$
    = (\mu - r)\tilde{S}_t\,dt + \sigma\tilde{S}_t\,dW_t^{\mathbb{Q}} - \sigma\theta\tilde{S}_t\,dt
    $$

    $$
    = (\mu - r)\tilde{S}_t\,dt - (\mu - r)\tilde{S}_t\,dt + \sigma\tilde{S}_t\,dW_t^{\mathbb{Q}} = \sigma\tilde{S}_t\,dW_t^{\mathbb{Q}}
    $$

    The drift vanishes, so $\tilde{S}_t$ is a local martingale (and, by standard integrability arguments for GBM, a true martingale) under $\mathbb{Q}$. $\square$
