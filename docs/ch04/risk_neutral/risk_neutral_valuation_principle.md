# Risk-Neutral Valuation Principle

This page carries out **Level 2** of the
[FTAP Ladder](martingale_and_no_arbitrage.md#summary-three-levels-of-no-arbitrage-and-pricing):
once local martingales have been upgraded to true martingales under $\mathbb{Q}$,
pricing reduces to computing expectations.

!!! info "Prerequisites"
    This section assumes familiarity with:
    
    - [Martingales](../../ch02/filtration_and_martingale/martingale.md)
    - [Girsanov's Theorem](../girsanov/girsanov_theorem.md)
    - [Fundamental Theorem of Asset Pricing](../../ch01/fundamental_theorem_of_asset_pricing/fundamental_theorem_of_asset_pricing.md)

---

## The Fundamental Pricing Formula

This formula works because control succeeded: local martingales have been upgraded to true martingales under $\mathbb{Q}$, so the conditional expectation below is well-defined and yields a unique price. In an arbitrage-free market, the time-$t$ price of a contingent claim with payoff $\Phi(X_T)$ at maturity $T$ is:

$$
\boxed{
V_t = \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^T r_s\,ds}\Phi(X_T) \;\middle|\; \mathcal{F}_t\right]
}
$$

where:

- $\mathbb{Q}$ is the **risk-neutral** (equivalent martingale) measure
- $r_s$ is the instantaneous risk-free rate
- $\mathcal{F}_t$ is the information available at time $t$

For constant interest rate $r$:

$$
V_t = e^{-r(T-t)}\mathbb{E}^{\mathbb{Q}}[\Phi(X_T) \mid \mathcal{F}_t]
$$

---

## Why This Works

By the [Fundamental Theorem of Asset Pricing](martingale_and_no_arbitrage.md),
no-arbitrage implies the existence of $\mathbb{Q}$ under which discounted prices are
martingales. For any replicable claim with price $V_t$, the discounted price
$\tilde{V}_t = e^{-\int_0^t r_s\,ds}V_t$ is also a $\mathbb{Q}$-martingale.
The martingale property at terminal time gives the pricing formula.

See [Construction of Q](construction.md) for how $\mathbb{Q}$ is built and
[Market Price of Risk](market_price_of_risk.md) for the economic content of the
measure change.


---

## What Changes Under Q

Under $\mathbb{Q}$, discounted prices are martingales — see
[Construction of Q](construction.md) for the mechanism.

---

## Summary

$$
\boxed{
V_t = \mathbb{E}^{\mathbb{Q}}\left[e^{-r(T-t)}\Phi(X_T) \mid \mathcal{F}_t\right]
}
$$

| Aspect | Description |
|--------|-------------|
| **What it says** | Price = discounted expected payoff under $\mathbb{Q}$ |
| **Foundation** | Fundamental Theorem of Asset Pricing (no-arbitrage ⟺ $\mathbb{Q}$ exists) |
| **Why $\mathbb{Q}$** | Ensures no-arbitrage; unique prices in complete markets |
| **What changes** | Drift becomes $r$; volatility unchanged |
| **PDE equivalence** | Same as solving Black–Scholes PDE (Feynman–Kac) |
| **Limitations** | Incomplete markets → non-unique prices; model dependence |

!!! abstract "Key Takeaway"
    The risk-neutral valuation principle transforms the economic problem of pricing into a mathematical problem of computing expectations. The measure $\mathbb{Q}$ is not about beliefs—it encodes the no-arbitrage constraints from traded asset prices. In complete markets, this gives unique derivative prices; in incomplete markets, it gives bounds.

---

## Exercises

**Exercise 1.**
A stock follows $dS_t = rS_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}}$ under the risk-neutral measure with $r = 0.05$, $\sigma = 0.30$, $S_0 = 100$, and $T = 0.5$. Compute the risk-neutral price of a European put option with strike $K = 95$ using the Black-Scholes formula. Verify that put-call parity holds.

??? success "Solution to Exercise 1"
    With $r = 0.05$, $\sigma = 0.30$, $S_0 = 100$, $T = 0.5$, $K = 95$:

    $$
    d_1 = \frac{\ln(100/95) + (0.05 + 0.09/2)(0.5)}{0.30\sqrt{0.5}} = \frac{\ln(1.05263) + 0.0475 \cdot 0.5}{0.2121} = \frac{0.05129 + 0.02375}{0.2121} = \frac{0.07504}{0.2121} \approx 0.3539
    $$

    $$
    d_2 = d_1 - \sigma\sqrt{T} = 0.3539 - 0.2121 = 0.1418
    $$

    The call price is:

    $$
    C = S_0\mathcal{N}(d_1) - Ke^{-rT}\mathcal{N}(d_2) = 100\Phi(0.3539) - 95e^{-0.025}\Phi(0.1418)
    $$

    $$
    = 100(0.6383) - 92.63(0.5564) = 63.83 - 51.53 \approx 12.30
    $$

    The put price via put-call parity is:

    $$
    P = C - S_0 + Ke^{-rT} = 12.30 - 100 + 92.63 = 4.93
    $$

    **Verification of put-call parity**: $C - P = 12.30 - 4.93 = 7.37$ and $S_0 - Ke^{-rT} = 100 - 92.63 = 7.37$. The parity holds.

---

**Exercise 2.**
A digital (binary) call option pays $\$1$ if $S_T > K$ and nothing otherwise. Derive its price under risk-neutral valuation and show that it equals $e^{-rT}\mathcal{N}(d_2)$. What happens to the price as $\sigma \to 0$?

??? success "Solution to Exercise 2"
    The digital call pays $\Phi_{\text{digital}} = \mathbf{1}_{S_T > K}$. By risk-neutral valuation:

    $$
    V_0 = e^{-rT}\mathbb{E}^{\mathbb{Q}}[\mathbf{1}_{S_T > K}] = e^{-rT}\mathbb{Q}(S_T > K)
    $$

    Under $\mathbb{Q}$, $\ln S_T = \ln S_0 + (r - \sigma^2/2)T + \sigma\sqrt{T}\,Z$ where $Z \sim N(0,1)$. Therefore:

    $$
    \mathbb{Q}(S_T > K) = \mathbb{Q}\left(Z > \frac{\ln(K/S_0) - (r - \sigma^2/2)T}{\sigma\sqrt{T}}\right) = \mathbb{Q}(Z > -d_2) = \mathcal{N}(d_2)
    $$

    Hence:

    $$
    V_0 = e^{-rT}\mathcal{N}(d_2)
    $$

    **As $\sigma \to 0$**: The stock becomes deterministic with $S_T = S_0 e^{rT}$. If $S_0 e^{rT} > K$ (i.e., the option is in-the-money at the forward), then $d_2 \to +\infty$ and $\mathcal{N}(d_2) \to 1$, giving $V_0 \to e^{-rT}$. If $S_0 e^{rT} < K$, then $d_2 \to -\infty$ and $V_0 \to 0$. If $S_0 e^{rT} = K$, $d_2 \to 0$ and $V_0 \to e^{-rT}/2$. The price converges to the discounted deterministic payoff.

---

**Exercise 3.**
Explain why the risk-neutral valuation formula uses $\mathbb{Q}$ rather than $\mathbb{P}$. Specifically, show that computing $e^{-rT}\mathbb{E}^{\mathbb{P}}[\Phi(S_T)]$ does not in general yield a no-arbitrage price. Under what special condition on the payoff $\Phi$ would the two computations agree?

??? success "Solution to Exercise 3"
    Under $\mathbb{P}$, $S_T = S_0 \exp((\mu - \sigma^2/2)T + \sigma W_T^{\mathbb{P}})$, so:

    $$
    e^{-rT}\mathbb{E}^{\mathbb{P}}[\Phi(S_T)]
    $$

    uses the physical drift $\mu$, not $r$, in the distribution of $S_T$. If $\Phi(x) = x$ (the payoff is the stock itself), then:

    $$
    e^{-rT}\mathbb{E}^{\mathbb{P}}[S_T] = e^{-rT} S_0 e^{\mu T} = S_0 e^{(\mu - r)T} \neq S_0
    $$

    unless $\mu = r$. This violates no-arbitrage since the discounted stock price should have expectation $S_0$ under the pricing measure, not $S_0 e^{(\mu-r)T}$.

    The fundamental issue is that $\mathbb{P}$-expectations do not account for the market price of risk. The $\mathbb{Q}$-expectation correctly prices by eliminating risk premia from the drift.

    The two computations agree when $\Phi$ is a **constant** payoff: $\Phi(S_T) = c$. Then $e^{-rT}\mathbb{E}^{\mathbb{Q}}[c] = e^{-rT}\mathbb{E}^{\mathbb{P}}[c] = ce^{-rT}$, since a constant is independent of the measure. More generally, the two agree if $\Phi(S_T)$ is $\mathcal{F}_0$-measurable (deterministic payoff), so the expectation does not depend on the probability measure at all.

---

**Exercise 4.**
Derive the risk-neutral valuation formula from no-arbitrage in five steps: (i) apply the FTAP to get the martingale property of discounted prices, (ii) extend to derivative prices, (iii) apply the martingale property, (iv) use the terminal condition, and (v) rearrange. At which step does the assumption of market completeness enter?

??? success "Solution to Exercise 4"
    **(i)** The FTAP states that NFLVR holds if and only if there exists $\mathbb{Q} \sim \mathbb{P}$ such that the discounted traded asset $\tilde{S}_t = e^{-\int_0^t r_s\,ds}S_t$ is a $\mathbb{Q}$-martingale.

    **(ii)** If the derivative with price $V_t$ can be replicated by a self-financing strategy in the traded assets, then $\tilde{V}_t = e^{-\int_0^t r_s\,ds}V_t$ must also be a $\mathbb{Q}$-martingale. If it were not, an arbitrage would exist between the derivative and its replicating portfolio.

    **(iii)** The martingale property gives: $\tilde{V}_t = \mathbb{E}^{\mathbb{Q}}[\tilde{V}_T \mid \mathcal{F}_t]$.

    **(iv)** At maturity $V_T = \Phi(X_T)$, so $\tilde{V}_T = e^{-\int_0^T r_s\,ds}\Phi(X_T)$. Substituting: $\tilde{V}_t = \mathbb{E}^{\mathbb{Q}}[e^{-\int_0^T r_s\,ds}\Phi(X_T) \mid \mathcal{F}_t]$.

    **(v)** Since $\tilde{V}_t = e^{-\int_0^t r_s\,ds}V_t$, multiply both sides by $e^{\int_0^t r_s\,ds}$:

    $$
    V_t = \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^T r_s\,ds}\Phi(X_T) \;\middle|\; \mathcal{F}_t\right]
    $$

    **Market completeness enters at step (ii)**: the argument that $\tilde{V}_t$ is a $\mathbb{Q}$-martingale requires the derivative to be **replicable**. In an incomplete market, the claim may not be replicable, and different equivalent martingale measures give different prices. Completeness (equivalently, uniqueness of $\mathbb{Q}$) ensures a unique no-arbitrage price.

---

**Exercise 5.**
Consider a stochastic interest rate model where $r_t$ follows the Vasicek process. The price of a zero-coupon bond is $P(t, T) = \mathbb{E}^{\mathbb{Q}}[\exp(-\int_t^T r_s\,ds) | \mathcal{F}_t]$. Explain why this is a direct application of the risk-neutral valuation principle with payoff $\Phi = 1$. Why is the discount factor inside the expectation rather than outside when $r_t$ is stochastic?

??? success "Solution to Exercise 5"
    A zero-coupon bond pays $\Phi = 1$ at time $T$. The risk-neutral valuation formula gives:

    $$
    P(t,T) = \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^T r_s\,ds} \cdot 1 \;\middle|\; \mathcal{F}_t\right] = \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^T r_s\,ds} \;\middle|\; \mathcal{F}_t\right]
    $$

    This is indeed the risk-neutral valuation formula with constant payoff $\Phi = 1$.

    The discount factor $e^{-\int_t^T r_s\,ds}$ must be **inside** the expectation because it is **random** when $r_t$ is stochastic. The integral $\int_t^T r_s\,ds$ depends on the future path of $r_s$, which is unknown at time $t$. If we wrote $e^{-r(T-t)}\mathbb{E}^{\mathbb{Q}}[1]$, we would be treating the discount factor as deterministic, which is only valid when $r$ is constant.

    Under the Vasicek model, $r_t$ is an Ornstein–Uhlenbeck process under $\mathbb{Q}$, and $\int_t^T r_s\,ds$ is Gaussian (as a linear functional of a Gaussian process). The expectation can be computed in closed form, yielding the affine bond price formula $P(t,T) = \exp(A(T-t) - B(T-t)r_t)$ for explicit functions $A$ and $B$.

---

**Exercise 6.**
In an incomplete market, two equivalent martingale measures $\mathbb{Q}_1$ and $\mathbb{Q}_2$ both exist. For a non-traded claim with payoff $\Phi(X_T)$, show that the two measures can give different prices $V_0^{(1)} \neq V_0^{(2)}$, both consistent with no-arbitrage. Explain the economic meaning of the pricing interval $[\underline{V}, \overline{V}]$.

??? success "Solution to Exercise 6"
    Let $\mathbb{Q}_1$ and $\mathbb{Q}_2$ be two equivalent martingale measures. The two prices are:

    $$
    V_0^{(1)} = \mathbb{E}^{\mathbb{Q}_1}[e^{-rT}\Phi(X_T)], \quad V_0^{(2)} = \mathbb{E}^{\mathbb{Q}_2}[e^{-rT}\Phi(X_T)]
    $$

    Both are valid no-arbitrage prices because both measures make discounted traded-asset prices into martingales. However, since $\Phi(X_T)$ is a **non-traded** claim, different measures assign different expectations.

    To see $V_0^{(1)} \neq V_0^{(2)}$ in general, note that $\mathbb{Q}_1 \neq \mathbb{Q}_2$ means they differ on some events. If $\Phi$ is non-constant and depends on the unhedgeable risk, then the difference in measure weighting leads to different expectations.

    The pricing interval $[\underline{V}, \overline{V}]$ is defined as:

    $$
    \underline{V} = \inf_{\mathbb{Q} \in \mathcal{M}} \mathbb{E}^{\mathbb{Q}}[e^{-rT}\Phi(X_T)], \quad \overline{V} = \sup_{\mathbb{Q} \in \mathcal{M}} \mathbb{E}^{\mathbb{Q}}[e^{-rT}\Phi(X_T)]
    $$

    where $\mathcal{M}$ is the set of all equivalent martingale measures. Any price within $[\underline{V}, \overline{V}]$ is consistent with no-arbitrage. The bounds $\underline{V}$ and $\overline{V}$ correspond to superhedging prices: $\overline{V}$ is the minimum cost to super-replicate $\Phi(X_T)$ (seller's price), and $\underline{V}$ is the maximum price a buyer would pay while maintaining no-arbitrage (buyer's price).

---

**Exercise 7.**
Show that the Black-Scholes PDE

$$
\frac{\partial V}{\partial t} + rx\frac{\partial V}{\partial x} + \frac{1}{2}\sigma^2 x^2\frac{\partial^2 V}{\partial x^2} - rV = 0
$$

is equivalent to the risk-neutral valuation formula via the Feynman-Kac theorem. Identify the generator $\mathcal{L}^{\mathbb{Q}}$, the discount rate, and the terminal condition. Explain why the PDE contains $r$ (not $\mu$) in the drift term.

??? success "Solution to Exercise 7"
    The Black-Scholes PDE is:

    $$
    \frac{\partial V}{\partial t} + rx\frac{\partial V}{\partial x} + \frac{1}{2}\sigma^2 x^2\frac{\partial^2 V}{\partial x^2} - rV = 0
    $$

    with terminal condition $V(T,x) = \Phi(x)$.

    **Identifying components for Feynman–Kac**:

    - **Generator**: $\mathcal{L}^{\mathbb{Q}} = rx\frac{\partial}{\partial x} + \frac{1}{2}\sigma^2 x^2\frac{\partial^2}{\partial x^2}$. This is the infinitesimal generator of geometric Brownian motion under $\mathbb{Q}$: $dS_t = rS_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}}$.
    - **Discount rate**: $r$ (the coefficient of $-V$ in the PDE).
    - **Terminal condition**: $V(T,x) = \Phi(x)$.

    The Feynman–Kac theorem states that the solution to $\frac{\partial V}{\partial t} + \mathcal{L}^{\mathbb{Q}}V - rV = 0$ with $V(T,x) = \Phi(x)$ is:

    $$
    V(t,x) = \mathbb{E}^{\mathbb{Q}}[e^{-r(T-t)}\Phi(S_T) \mid S_t = x]
    $$

    where $S$ follows the $\mathbb{Q}$-dynamics. This is exactly the risk-neutral valuation formula.

    The PDE contains $r$ (not $\mu$) because the generator $\mathcal{L}^{\mathbb{Q}}$ corresponds to the **risk-neutral dynamics** $dS = rS\,dt + \sigma S\,dW^{\mathbb{Q}}$. The measure change from $\mathbb{P}$ to $\mathbb{Q}$ via Girsanov replaces the physical drift $\mu$ with $r$. The PDE is derived by requiring that the discounted option price be a $\mathbb{Q}$-martingale, which forces the drift to be $r$.

---

**Exercise 8.**
A candidate prices a derivative using $V_t = e^{-r(T-t)}\,\mathbb{E}^{\mathbb{P}}[\Phi(S_T) \mid \mathcal{F}_t]$ instead of the risk-neutral expectation under $\mathbb{Q}$. In what sense is this wrong, and is there any scenario where it accidentally gives the correct price?

??? success "Solution to Exercise 8"
    This is wrong in general because $\mathbb{P}$ incorporates risk premia. Under $\mathbb{P}$, the stock drift is $\mu \neq r$, so the discounted price $e^{-rt}S_t$ is **not** a $\mathbb{P}$-martingale. The formula $e^{-r(T-t)}\mathbb{E}^{\mathbb{P}}[\Phi(S_T)]$ does not correspond to a replicating strategy cost and violates no-arbitrage pricing.

    The correct formula uses $\mathbb{Q}$:

    $$
    V_t = e^{-r(T-t)}\,\mathbb{E}^{\mathbb{Q}}[\Phi(S_T) \mid \mathcal{F}_t]
    $$

    The $\mathbb{P}$-formula accidentally gives the correct price only when $\mu = r$ (risk-neutral and physical measures coincide) or when the payoff $\Phi$ is a constant (independent of $S_T$). In all other cases, the $\mathbb{P}$-based price will be systematically biased — typically too high for call-like payoffs (because $\mu > r$ inflates the expected stock price) and too low for put-like payoffs.

    The key distinction: **pricing is not forecasting**. The risk-neutral measure removes the drift premium so that the discounted price process is a martingale, which is the mathematical content of no-arbitrage pricing.
