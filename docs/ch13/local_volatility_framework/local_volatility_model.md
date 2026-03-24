# Local Volatility Model

The Black-Scholes model assumes constant volatility, yet market option prices exhibit a rich structure of implied volatility smiles and skews that flatly contradict this assumption. The local volatility model, introduced independently by Dupire (1994) and Derman-Kani (1994), resolves this tension by allowing the instantaneous volatility to be a deterministic function of the current asset price and time. This apparently simple generalization has profound consequences: the resulting one-factor diffusion is the unique Markovian model consistent with a given arbitrage-free implied volatility surface, and it provides the natural bridge between observed market prices and the underlying risk-neutral dynamics.

!!! abstract "Learning Objectives"
    After completing this section, you should be able to:

    - Formulate the local volatility model as a one-factor diffusion with state-dependent volatility
    - Explain Dupire's insight connecting the local volatility function to the call price surface
    - Derive the relationship between local volatility and the risk-neutral transition density
    - Prove that the local volatility model is complete and admits unique option prices
    - Compare the local volatility framework with Black-Scholes and stochastic volatility models

## Motivation: Beyond Constant Volatility

### The Empirical Failure of Black-Scholes

Under the Black-Scholes model, the asset price follows a geometric Brownian motion with constant volatility $\sigma$:

$$
dS_t = (r - q)S_t \, dt + \sigma S_t \, dW_t^{\mathbb{Q}}
$$

If this model were correct, the implied volatility computed from market prices of European options at different strikes and maturities would be the same constant $\sigma$. Instead, practitioners observe systematic patterns:

- **Volatility skew**: For equity indices, implied volatility decreases as the strike $K$ increases, reflecting the market's pricing of downside crash risk.
- **Volatility smile**: For FX options, implied volatility exhibits a U-shaped pattern symmetric around the at-the-money strike, reflecting excess kurtosis.
- **Term structure**: Implied volatility varies with maturity, typically mean-reverting from short-term levels toward a long-run average.

These patterns imply that the risk-neutral distribution of $S_T$ is not lognormal. The challenge is to construct a diffusion model that is consistent with the entire observed option surface.

### The Key Idea

Dupire's insight is to replace the constant $\sigma$ with a deterministic function $\sigma_{\text{loc}}(S, t)$ that depends on the current spot price $S$ and time $t$. If this function is chosen correctly, the resulting model reproduces all observed European option prices simultaneously. The local volatility function encodes the market's view of how the instantaneous volatility depends on the price level and time, distilled from the collective information in all traded options.

## Model Specification

### The Local Volatility Diffusion

**Definition 13.1.1** (Local Volatility Model).
Under the risk-neutral measure $\mathbb{Q}$, the asset price $S_t$ follows the stochastic differential equation:

$$
dS_t = (r - q)S_t \, dt + \sigma_{\text{loc}}(S_t, t) S_t \, dW_t^{\mathbb{Q}}
$$

where:

- $r \geq 0$ is the constant risk-free interest rate
- $q \geq 0$ is the constant continuous dividend yield
- $W_t^{\mathbb{Q}}$ is a standard Brownian motion under $\mathbb{Q}$
- $\sigma_{\text{loc}}: (0, \infty) \times [0, T^*] \to (0, \infty)$ is a deterministic function called the **local volatility function**

The function $\sigma_{\text{loc}}(S, t)$ specifies the instantaneous volatility the asset will have if it reaches level $S$ at time $t$. Once this function is specified, the entire dynamics of $S_t$ are determined.

### Comparison with Other Models

The local volatility model sits in a natural hierarchy of diffusion models:

| Model | Volatility | Factors | Complete |
|-------|-----------|---------|----------|
| Black-Scholes | $\sigma$ (constant) | 1 | Yes |
| Local volatility | $\sigma_{\text{loc}}(S, t)$ (deterministic function) | 1 | Yes |
| Stochastic volatility | $\sigma_t$ (random process) | 2 | No |

The crucial distinction is that in the local volatility model, volatility is a known function of observables $(S, t)$, not a separate random variable. This makes the model Markovian in a single state variable $S_t$ and keeps the market complete.

### Existence and Uniqueness of Solutions

**Theorem 13.1.1** (Well-Posedness).
Suppose $\sigma_{\text{loc}}: (0, \infty) \times [0, T^*] \to (0, \infty)$ satisfies:

1. **Local Lipschitz condition**: For each compact set $K \subset (0, \infty) \times [0, T^*]$, there exists $L_K > 0$ such that

    $$
    |\sigma_{\text{loc}}(S_1, t) S_1 - \sigma_{\text{loc}}(S_2, t) S_2| \leq L_K |S_1 - S_2|
    $$

    for all $(S_1, t), (S_2, t) \in K$.

2. **Linear growth condition**: There exists $C > 0$ such that

    $$
    |\sigma_{\text{loc}}(S, t) S| \leq C(1 + S)
    $$

    for all $(S, t) \in (0, \infty) \times [0, T^*]$.

Then the SDE admits a unique strong solution $S_t > 0$ for all $t \in [0, T^*]$.

*Proof.* The drift coefficient $\mu(S) = (r - q)S$ and diffusion coefficient $\sigma(S, t) = \sigma_{\text{loc}}(S, t)S$ satisfy the standard conditions for existence and uniqueness of strong solutions to SDEs (see Karatzas and Shreve, Theorem 5.2.9). Positivity follows from the fact that $S = 0$ is a natural boundary: the diffusion coefficient vanishes at $S = 0$, and the drift is zero, so the process cannot reach zero in finite time. $\square$

## Connection to the Risk-Neutral Density

### The Breeden-Litzenberger Formula

The price of a European call option with strike $K$ and maturity $T$ is:

$$
C(K, T) = e^{-rT} \mathbb{E}^{\mathbb{Q}}[(S_T - K)^+] = e^{-rT} \int_K^{\infty} (S - K) p(S, T) \, dS
$$

where $p(S, T)$ is the risk-neutral transition density of $S_T$ given $S_0$. Differentiating twice with respect to the strike:

$$
\frac{\partial C}{\partial K} = -e^{-rT} \int_K^{\infty} p(S, T) \, dS = -e^{-rT} \mathbb{Q}(S_T > K)
$$

$$
\frac{\partial^2 C}{\partial K^2} = e^{-rT} p(K, T)
$$

This is the **Breeden-Litzenberger formula**: the risk-neutral density is proportional to the butterfly spread (the second derivative of the call price with respect to strike). The formula is model-free -- it holds for any model that generates the call price surface $C(K, T)$.

### Local Volatility Determines the Density

The transition density $p(S, T)$ satisfies the **forward Kolmogorov (Fokker-Planck) equation**:

$$
\frac{\partial p}{\partial T} = -\frac{\partial}{\partial S}\bigl[(r - q)S \, p\bigr] + \frac{1}{2}\frac{\partial^2}{\partial S^2}\bigl[\sigma_{\text{loc}}^2(S, T) S^2 \, p\bigr]
$$

with initial condition $p(S, 0) = \delta(S - S_0)$. The local volatility function $\sigma_{\text{loc}}(S, T)$ enters the diffusion term and determines how the density spreads over time. Different local volatility surfaces produce different density evolutions and hence different option prices.

**Proposition 13.1.1** (Dupire's Insight).
The local volatility at $(K, T)$ is determined by the ratio of the time decay of the call price to the convexity with respect to strike:

$$
\sigma_{\text{loc}}^2(K, T) = \frac{\dfrac{\partial C}{\partial T} + (r - q)K\dfrac{\partial C}{\partial K} + qC}{\dfrac{1}{2}K^2 \dfrac{\partial^2 C}{\partial K^2}}
$$

The numerator captures the rate at which optionality increases with maturity (adjusted for drift and dividends), while the denominator is proportional to the risk-neutral density at the strike. The local variance is therefore the rate of probability diffusion per unit density at each point $(K, T)$.

*Proof.* This follows from the Fokker-Planck equation applied to the call price integral. The detailed derivation is presented in the section on Dupire Formula Derivation. $\square$

### Intuitive Interpretation

The Dupire formula admits a clean financial interpretation:

- **Numerator** $\partial_T C + (r-q)K \partial_K C + qC$: This is the **forward theta** -- the total sensitivity of the option price to a small increase in maturity, after adjusting for the drift of the forward price. It measures how much additional optionality is created by extending the maturity by $dT$.
- **Denominator** $\frac{1}{2}K^2 \partial_{KK} C$: This is proportional to the risk-neutral density $p(K, T)$ at the strike. It measures the concentration of probability mass near the strike level.
- **Ratio**: The local variance equals the rate at which optionality accumulates per unit probability density. Where the density is high (near the forward price), even moderate local volatility generates substantial optionality. In the tails, the density is low, so the local volatility must be larger to generate the same amount of optionality.

## Market Completeness

### One Factor Implies Completeness

**Theorem 13.1.2** (Market Completeness).
Under the local volatility model, the market consisting of the riskless bond and the asset $S_t$ is complete. Every European contingent claim $H = h(S_T)$ admits a unique replicating portfolio and a unique arbitrage-free price.

*Proof.* The local volatility model is a one-factor diffusion:

$$
dS_t = (r - q)S_t \, dt + \sigma_{\text{loc}}(S_t, t) S_t \, dW_t^{\mathbb{Q}}
$$

There is a single source of randomness $W_t^{\mathbb{Q}}$, and the diffusion coefficient $\sigma_{\text{loc}}(S_t, t) S_t > 0$ is non-degenerate (since $\sigma_{\text{loc}} > 0$ and $S_t > 0$). By the martingale representation theorem, every $\mathcal{F}_T$-measurable, square-integrable random variable can be written as a stochastic integral with respect to $W_t^{\mathbb{Q}}$.

Specifically, let $V_t = e^{-rt}\mathbb{E}^{\mathbb{Q}}[e^{-r(T-t)}h(S_T) \mid \mathcal{F}_t]$ be the discounted option price process. By Ito's representation theorem, there exists a predictable process $\phi_t$ such that:

$$
dV_t = \phi_t \, dW_t^{\mathbb{Q}}
$$

Defining the hedge ratio $\Delta_t = \phi_t / (\sigma_{\text{loc}}(S_t, t) S_t)$, the portfolio consisting of $\Delta_t$ shares of the asset and the remainder in the riskless bond replicates the claim $h(S_T)$. $\square$

!!! warning "Completeness vs Correctness"
    Market completeness means every payoff has a unique price within the model. It does **not** mean the model correctly describes reality. The local volatility model provides unique prices, but these prices for path-dependent options may differ significantly from those produced by stochastic volatility models that fit the same vanilla surface.

### The Pricing PDE

By Ito's lemma and the no-arbitrage condition, the price $V(S, t)$ of any European derivative satisfies the **backward Kolmogorov equation**:

$$
\frac{\partial V}{\partial t} + (r - q)S \frac{\partial V}{\partial S} + \frac{1}{2}\sigma_{\text{loc}}^2(S, t) S^2 \frac{\partial^2 V}{\partial S^2} - rV = 0
$$

with terminal condition $V(S, T) = h(S)$. This PDE is the analogue of the Black-Scholes PDE with $\sigma$ replaced by $\sigma_{\text{loc}}(S, t)$. It can be solved by finite difference methods using the calibrated local volatility surface.

## The Dupire Surface and Its Properties

### From Call Prices to Local Volatility

Given a complete, arbitrage-free call price surface $C(K, T)$ for all $K > 0$ and $T > 0$, the Dupire formula:

$$
\sigma_{\text{loc}}^2(K, T) = \frac{\partial_T C + (r - q)K \, \partial_K C + qC}{\frac{1}{2}K^2 \, \partial_{KK} C}
$$

produces a unique local volatility surface. The arbitrage-free conditions on $C$ ensure that:

- $\partial_{KK} C > 0$ (positive risk-neutral density), so the denominator is positive
- $\partial_T C + (r-q)K \, \partial_K C + qC \geq 0$ (non-negative forward theta), so the numerator is non-negative
- Therefore $\sigma_{\text{loc}}^2(K, T) \geq 0$, as required

**Theorem 13.1.3** (Uniqueness of Local Volatility).
Given an arbitrage-free European call price surface $C(K, T)$ that is $C^1$ in $T$ and $C^2$ in $K$, there exists a unique local volatility function $\sigma_{\text{loc}}(S, t) > 0$ such that the local volatility model reproduces $C(K, T)$ exactly.

*Proof.* Existence follows from the Dupire formula, which constructs $\sigma_{\text{loc}}$ directly from $C$. For uniqueness, suppose two local volatility functions $\sigma_1$ and $\sigma_2$ both reproduce $C$. Then the corresponding transition densities $p_1$ and $p_2$ satisfy the same Fokker-Planck equation with the same initial condition. By the Breeden-Litzenberger formula, $p_1(K, T) = p_2(K, T)$ for all $K, T$. Substituting into the Dupire formula, $\sigma_1^2(K, T) = \sigma_2^2(K, T)$ for all $K, T$. $\square$

### Typical Features of the Surface

For equity index options, the local volatility surface typically exhibits:

1. **Decreasing in spot**: $\partial_S \sigma_{\text{loc}} < 0$, reflecting the leverage effect. As the stock price falls, the firm's equity becomes riskier relative to its debt, and volatility increases.
2. **Mean-reverting term structure**: The surface flattens for longer maturities as the effect of the initial smile diminishes.
3. **Steeper smile than implied**: The local volatility smile is approximately twice as steep as the implied volatility smile. Near the at-the-money level for short maturities:

$$
\sigma_{\text{loc}}(K, T) \approx \sigma_{\text{imp}}(K, T) + (K - S_0) \frac{\partial \sigma_{\text{imp}}}{\partial K} + T \frac{\partial \sigma_{\text{imp}}}{\partial T} + \cdots
$$

The local volatility skew is steeper because $\sigma_{\text{loc}}$ is the instantaneous volatility at a point, while $\sigma_{\text{imp}}$ is an average along a path.

## Worked Example

??? example "Local Volatility from a Flat Smile"

    **Setup.** Suppose the implied volatility surface is flat: $\sigma_{\text{imp}}(K, T) = 0.20$ for all $K, T$, with $r = 0.05$, $q = 0$, $S_0 = 100$.

    Since $\partial_T \sigma_{\text{imp}} = 0$, $\partial_K \sigma_{\text{imp}} = 0$, and $\partial_{KK} \sigma_{\text{imp}} = 0$, the Dupire formula in implied volatility form gives:

    $$
    \sigma_{\text{loc}}^2(K, T) = \frac{\sigma_{\text{imp}}^2 + 0 + 0}{(1 + 0)^2 + 0} = \sigma_{\text{imp}}^2 = 0.04
    $$

    Therefore $\sigma_{\text{loc}}(K, T) = 0.20$ for all $(K, T)$. When the implied volatility surface is flat, the local volatility surface is also flat and equals the implied volatility. This confirms that Black-Scholes is a special case of the local volatility model.

??? example "Local Volatility with Linear Skew"

    **Setup.** Suppose the implied volatility surface exhibits a linear skew:

    $$
    \sigma_{\text{imp}}(K, T) = 0.20 - 0.001(K - 100)
    $$

    with $r = 0.05$, $q = 0$, $S_0 = 100$, $T = 0.5$.

    The relevant derivatives are:

    $$
    \frac{\partial \sigma_{\text{imp}}}{\partial K} = -0.001, \quad \frac{\partial^2 \sigma_{\text{imp}}}{\partial K^2} = 0, \quad \frac{\partial \sigma_{\text{imp}}}{\partial T} = 0
    $$

    At $K = 100$ (ATM), $\sigma_{\text{imp}} = 0.20$, $d_1 = (0 + 0.02 \cdot 0.5)/(0.20 \cdot \sqrt{0.5}) \approx 0.0707$.

    The denominator of the Dupire formula becomes:

    $$
    \bigl(1 + 100 \cdot 0.0707 \cdot \sqrt{0.5} \cdot (-0.001)\bigr)^2 + 0 = (1 - 0.005)^2 \approx 0.990
    $$

    The numerator is:

    $$
    0.04 + 2 \cdot 0.20 \cdot 0.5 \cdot 0 + 2 \cdot 0.05 \cdot 100 \cdot 0.20 \cdot 0.5 \cdot (-0.001) = 0.04 - 0.001 = 0.039
    $$

    So $\sigma_{\text{loc}}^2(100, 0.5) \approx 0.039 / 0.990 \approx 0.0394$, giving $\sigma_{\text{loc}}(100, 0.5) \approx 0.1985$.

    The local volatility is slightly below the implied volatility at ATM, and the local volatility skew is steeper than the implied volatility skew.

## Connection to Subsequent Sections

The local volatility model establishes the foundation for the remainder of this chapter:

- **Dupire Formula Derivation** provides the rigorous proof of Proposition 13.1.1 via both the Fokker-Planck equation and Tanaka's formula.
- **Gyongy's Theorem** explains why any stochastic volatility model has a local volatility "shadow" that matches its vanilla prices, with $\sigma_{\text{loc}}^2(K, t) = \mathbb{E}[\sigma_t^2 \mid S_t = K]$.
- **Relationship to Implied Volatility** develops the asymptotic expansions connecting $\sigma_{\text{loc}}$ and $\sigma_{\text{imp}}$, including the Berestycki-Busca-Florent formula.
- **Smile Dynamics** and **Limitations** explore the model's systematic failure to capture the dynamic behavior of the smile, motivating the transition to stochastic volatility.

## Summary

The local volatility model extends Black-Scholes by allowing volatility to be a deterministic function $\sigma_{\text{loc}}(S, t)$ of spot and time. The key results are:

1. **Model specification**: The SDE $dS_t = (r-q)S_t \, dt + \sigma_{\text{loc}}(S_t, t) S_t \, dW_t^{\mathbb{Q}}$ defines a one-factor Markov diffusion.
2. **Dupire's formula**: The local volatility is uniquely determined by the call price surface through $\sigma_{\text{loc}}^2 = (\partial_T C + (r-q)K\partial_K C + qC) / (\frac{1}{2}K^2 \partial_{KK} C)$.
3. **Connection to density**: The denominator of Dupire's formula is the risk-neutral density (Breeden-Litzenberger), so local volatility measures the rate of probability diffusion per unit density.
4. **Completeness**: The model has one source of randomness, so every European claim can be replicated, yielding unique arbitrage-free prices.
5. **Uniqueness**: Given an arbitrage-free call surface, the local volatility function is unique.

---

## Exercises

**Exercise 1.** The local volatility model SDE is $dS_t = (r-q)S_t\,dt + \sigma_{\text{loc}}(S_t, t)S_t\,dW_t^{\mathbb{Q}}$. (a) Show that if $\sigma_{\text{loc}}(S,t) = \sigma_0$ (constant), this reduces to the Black-Scholes geometric Brownian motion. (b) Write down the corresponding backward Kolmogorov PDE for a European call price $V(S,t)$ in the general local volatility case. (c) Explain why this PDE requires specifying $\sigma_{\text{loc}}(S,t)$ on the entire domain $(0,\infty)\times[0,T]$, not just at the current spot $S_0$.

---

**Exercise 2.** The existence and uniqueness theorem (Theorem 13.1.1) requires a local Lipschitz condition on the diffusion coefficient $\sigma_{\text{loc}}(S,t)S$. (a) Verify that $\sigma_{\text{loc}}(S,t)S = \sigma_0 S$ satisfies the local Lipschitz condition with constant $L_K = \sigma_0$. (b) Give an example of a function $\sigma_{\text{loc}}(S,t)$ that violates the local Lipschitz condition. (c) Why does the linear growth condition $|\sigma_{\text{loc}}(S,t)S| \leq C(1+S)$ prevent the solution from exploding in finite time?

---

**Exercise 3.** The Breeden-Litzenberger formula states $\partial^2 C / \partial K^2 = e^{-rT}p(K,T)$. (a) Verify this by differentiating $C(K,T) = e^{-rT}\int_K^\infty (S-K)p(S,T)\,dS$ twice with respect to $K$. (b) The denominator of the Dupire formula is $\frac{1}{2}K^2 \partial_{KK}C$. Express this in terms of the risk-neutral density $p(K,T)$. (c) What happens to the Dupire formula when $p(K,T) \to 0$ (deep out-of-the-money)? Discuss the numerical challenges this creates.

---

**Exercise 4.** The local volatility surface is typically steeper than the implied volatility surface. Consider the approximation near ATM:

$$
\sigma_{\text{loc}}(K, T) \approx \sigma_{\text{imp}}(K, T) + (K - S_0)\frac{\partial \sigma_{\text{imp}}}{\partial K}
$$

If the implied volatility skew at ATM is $\partial \sigma_{\text{imp}}/\partial K = -0.001$ per strike unit, with $\sigma_{\text{imp}}(100, 0.5) = 0.20$ and $S_0 = 100$, compute $\sigma_{\text{loc}}(90, 0.5)$ and $\sigma_{\text{loc}}(110, 0.5)$ using this approximation. Compare with the implied volatility values at these strikes.

---

**Exercise 5.** Market completeness under the local volatility model follows from the existence of a single Brownian driver. (a) State the martingale representation theorem and explain how it guarantees replication. (b) For a European call with payoff $(S_T - K)^+$, the hedge ratio is $\Delta_t = \partial V / \partial S$. In the local volatility model, $\Delta_t$ depends on $\sigma_{\text{loc}}(S,t)$. Explain why the hedge ratio is different from the Black-Scholes delta even when both models are calibrated to the same ATM volatility. (c) Under stochastic volatility, why does market completeness fail?

---

**Exercise 6.** The Dupire formula in the presence of dividends is

$$
\sigma_{\text{loc}}^2(K,T) = \frac{\partial_T C + (r-q)K\,\partial_K C + qC}{\frac{1}{2}K^2\,\partial_{KK}C}
$$

(a) Show that the $qC$ term in the numerator arises from the dividend-adjusted forward drift $(r-q)S_t$. (b) For an asset with $q > r$, is it possible for the numerator to be negative? If so, what economic interpretation would this have? (c) Verify that setting $q = 0$ recovers the standard Dupire formula.

---

**Exercise 7.** Two models are calibrated to the same arbitrage-free call price surface $C(K,T)$: a local volatility model and a Heston stochastic volatility model. (a) By Theorem 13.1.3, the local volatility surface is unique. How is this consistent with the Heston model also matching $C(K,T)$? (b) State Gyongy's theorem relating the Heston instantaneous variance to the local volatility function. (c) Give an example of a derivative whose price differs between the two models despite identical vanilla calibration.
