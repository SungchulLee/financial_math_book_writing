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

??? success "Solution to Exercise 1"
    **(a)** If $\sigma_{\text{loc}}(S, t) = \sigma_0$ (constant), the SDE becomes:

    $$
    dS_t = (r - q)S_t\,dt + \sigma_0 S_t\,dW_t^{\mathbb{Q}}
    $$

    This is the standard geometric Brownian motion of the Black-Scholes model. The drift is $(r-q)S_t$ (risk-neutral drift), the diffusion coefficient is $\sigma_0 S_t$ (proportional volatility), and the solution is:

    $$
    S_T = S_0 \exp\!\left[\left(r - q - \tfrac{\sigma_0^2}{2}\right)T + \sigma_0 W_T\right]
    $$

    which is the standard lognormal dynamics.

    **(b)** The backward Kolmogorov PDE for a European derivative with price $V(S, t)$ is:

    $$
    \frac{\partial V}{\partial t} + (r - q)S\frac{\partial V}{\partial S} + \frac{1}{2}\sigma_{\text{loc}}^2(S, t)S^2\frac{\partial^2 V}{\partial S^2} - rV = 0
    $$

    with terminal condition $V(S, T) = (S - K)^+$ for a European call. This is the generalized Black-Scholes PDE with $\sigma$ replaced by $\sigma_{\text{loc}}(S, t)$.

    **(c)** The PDE requires $\sigma_{\text{loc}}(S, t)$ on the entire domain $(0, \infty) \times [0, T]$ because the solution $V(S, t)$ depends on the future evolution of the process from any state $(S, t)$. Even though the process starts at $S_0$, computing the option price requires solving the PDE backward from terminal time $T$, which involves the local volatility at all possible future values of $S$. The process may visit any price level $S > 0$ before maturity, and the hedge ratio at each state depends on the local volatility there. In a finite-difference numerical scheme, the PDE is solved on a grid spanning a wide range of $S$ values, and $\sigma_{\text{loc}}$ must be specified at every grid point.

---

**Exercise 2.** The existence and uniqueness theorem (Theorem 13.1.1) requires a local Lipschitz condition on the diffusion coefficient $\sigma_{\text{loc}}(S,t)S$. (a) Verify that $\sigma_{\text{loc}}(S,t)S = \sigma_0 S$ satisfies the local Lipschitz condition with constant $L_K = \sigma_0$. (b) Give an example of a function $\sigma_{\text{loc}}(S,t)$ that violates the local Lipschitz condition. (c) Why does the linear growth condition $|\sigma_{\text{loc}}(S,t)S| \leq C(1+S)$ prevent the solution from exploding in finite time?

??? success "Solution to Exercise 2"
    **(a)** For $\sigma_{\text{loc}}(S, t) = \sigma_0$ (constant), the diffusion coefficient is $b(S) = \sigma_0 S$. The Lipschitz condition requires:

    $$
    |b(S_1) - b(S_2)| = |\sigma_0 S_1 - \sigma_0 S_2| = \sigma_0|S_1 - S_2| \leq L_K|S_1 - S_2|
    $$

    This holds globally (not just locally) with $L_K = \sigma_0$. The condition is satisfied.

    **(b)** An example violating the local Lipschitz condition: $\sigma_{\text{loc}}(S, t) = S^{-1/2}$. Then the diffusion coefficient is $b(S) = S^{-1/2} \cdot S = S^{1/2}$. Near $S = 0$:

    $$
    |S_1^{1/2} - S_2^{1/2}| = \frac{|S_1 - S_2|}{S_1^{1/2} + S_2^{1/2}}
    $$

    As $S_1, S_2 \to 0$, the ratio $|b(S_1) - b(S_2)|/|S_1 - S_2| \to \infty$, so no finite Lipschitz constant exists on any compact set containing $S = 0$. This is the square-root diffusion case (CIR/Feller process), which requires separate analysis.

    **(c)** The linear growth condition $|\sigma_{\text{loc}}(S, t)S| \leq C(1 + S)$ ensures the diffusion coefficient does not grow faster than linearly in $S$. Without this condition, the process could reach infinity in finite time (explosion). Intuitively, if the volatility $\sigma_{\text{loc}}(S, t)S$ grows superlinearly (say like $S^{1+\epsilon}$), the process experiences increasingly large random shocks as it grows, potentially accelerating to infinity. The linear growth bound ensures that the expected magnitude of the increments remains controlled, preventing finite-time blow-up by standard comparison arguments for SDEs.

---

**Exercise 3.** The Breeden-Litzenberger formula states $\partial^2 C / \partial K^2 = e^{-rT}p(K,T)$. (a) Verify this by differentiating $C(K,T) = e^{-rT}\int_K^\infty (S-K)p(S,T)\,dS$ twice with respect to $K$. (b) The denominator of the Dupire formula is $\frac{1}{2}K^2 \partial_{KK}C$. Express this in terms of the risk-neutral density $p(K,T)$. (c) What happens to the Dupire formula when $p(K,T) \to 0$ (deep out-of-the-money)? Discuss the numerical challenges this creates.

??? success "Solution to Exercise 3"
    **(a)** Starting from $C(K, T) = e^{-rT}\int_K^\infty (S - K)p(S, T)\,dS$:

    **First differentiation:**

    $$
    \frac{\partial C}{\partial K} = e^{-rT}\left[-(K-K)p(K,T) + \int_K^\infty (-1)p(S,T)\,dS\right] = -e^{-rT}\int_K^\infty p(S,T)\,dS
    $$

    **Second differentiation:**

    $$
    \frac{\partial^2 C}{\partial K^2} = -e^{-rT}\cdot(-p(K,T)) = e^{-rT}p(K,T)
    $$

    This confirms the Breeden-Litzenberger formula.

    **(b)** The denominator of the Dupire formula is:

    $$
    \frac{1}{2}K^2\frac{\partial^2 C}{\partial K^2} = \frac{1}{2}K^2 e^{-rT}p(K,T)
    $$

    This is $\frac{1}{2}K^2$ times the discounted risk-neutral density evaluated at $S_T = K$.

    **(c)** When $p(K, T) \to 0$ (deep OTM, either very high or very low strikes), the denominator $\frac{1}{2}K^2 C_{KK} \to 0$. If the numerator approaches zero at a different rate, $\sigma_{\text{loc}}^2$ can diverge or become indeterminate.

    Numerical challenges include:

    - **Division by near-zero:** Small denominators amplify any noise in the numerator, producing unreliable or extreme local volatility values
    - **Noise amplification:** In the wings, option prices are small and subject to large relative bid-ask spreads. Computing $C_{KK}$ from noisy data in low-density regions amplifies errors quadratically
    - **Ill-conditioning:** The ratio of two small numbers is inherently unstable numerically
    - **Mitigation:** Practitioners extrapolate the wings using parametric models (SVI, power-law tails), cap local volatility at reasonable bounds, or use regularization

---

**Exercise 4.** The local volatility surface is typically steeper than the implied volatility surface. Consider the approximation near ATM:

$$
\sigma_{\text{loc}}(K, T) \approx \sigma_{\text{imp}}(K, T) + (K - S_0)\frac{\partial \sigma_{\text{imp}}}{\partial K}
$$

If the implied volatility skew at ATM is $\partial \sigma_{\text{imp}}/\partial K = -0.001$ per strike unit, with $\sigma_{\text{imp}}(100, 0.5) = 0.20$ and $S_0 = 100$, compute $\sigma_{\text{loc}}(90, 0.5)$ and $\sigma_{\text{loc}}(110, 0.5)$ using this approximation. Compare with the implied volatility values at these strikes.

??? success "Solution to Exercise 4"
    Using $\sigma_{\text{loc}}(K, T) \approx \sigma_{\text{imp}}(K, T) + (K - S_0)\frac{\partial \sigma_{\text{imp}}}{\partial K}$ with $\frac{\partial \sigma_{\text{imp}}}{\partial K} = -0.001$, $\sigma_{\text{imp}}(100, 0.5) = 0.20$, and $S_0 = 100$:

    **Implied volatilities at the off-ATM strikes (linear skew):**

    $$
    \sigma_{\text{imp}}(90, 0.5) = 0.20 - 0.001 \times (90 - 100) = 0.20 + 0.01 = 0.21
    $$

    $$
    \sigma_{\text{imp}}(110, 0.5) = 0.20 - 0.001 \times (110 - 100) = 0.20 - 0.01 = 0.19
    $$

    **Local volatilities:**

    $$
    \sigma_{\text{loc}}(90, 0.5) \approx 0.20 + (90 - 100)(-0.001) = 0.20 + 0.01 = 0.21
    $$

    $$
    \sigma_{\text{loc}}(110, 0.5) \approx 0.20 + (110 - 100)(-0.001) = 0.20 - 0.01 = 0.19
    $$

    **Comparison:** At this level of approximation, $\sigma_{\text{loc}}(K) \approx \sigma_{\text{imp}}(K)$. However, this first-order approximation understates the true steepness of the local volatility skew. A more accurate approximation (accounting for second-order terms) gives a local volatility skew approximately twice as steep as the implied volatility skew. The reason is that implied volatility represents a path-averaged quantity, so to produce an implied vol skew of slope $-0.001$, the instantaneous local volatility must have a steeper slope, roughly $-0.002$. The first-order formula above captures only the leading-order effect.

---

**Exercise 5.** Market completeness under the local volatility model follows from the existence of a single Brownian driver. (a) State the martingale representation theorem and explain how it guarantees replication. (b) For a European call with payoff $(S_T - K)^+$, the hedge ratio is $\Delta_t = \partial V / \partial S$. In the local volatility model, $\Delta_t$ depends on $\sigma_{\text{loc}}(S,t)$. Explain why the hedge ratio is different from the Black-Scholes delta even when both models are calibrated to the same ATM volatility. (c) Under stochastic volatility, why does market completeness fail?

??? success "Solution to Exercise 5"
    **(a)** The **martingale representation theorem** states: In a complete market driven by a single Brownian motion $W_t^{\mathbb{Q}}$, every square-integrable $\mathcal{F}_T$-measurable random variable $X$ can be written as:

    $$
    X = \mathbb{E}^{\mathbb{Q}}[X] + \int_0^T \phi_t\,dW_t^{\mathbb{Q}}
    $$

    for some predictable process $\phi_t$. Since the discounted option price $\tilde{V}_t = e^{-rt}V_t$ is a $\mathbb{Q}$-martingale, it has the representation $d\tilde{V}_t = \phi_t\,dW_t^{\mathbb{Q}}$. The hedge ratio $\Delta_t = \phi_t / (\sigma_{\text{loc}}(S_t, t)S_t)$ defines a self-financing portfolio that replicates any contingent claim, guaranteeing completeness.

    **(b)** In the local volatility model, the delta $\Delta_t = \partial V / \partial S$ depends on $\sigma_{\text{loc}}(S, t)$ through the PDE solution. Since $\sigma_{\text{loc}}(S, t)$ varies with $S$, the option price surface $V(S, t)$ has different curvature than the Black-Scholes price with constant $\sigma$. Even if both models agree at the current spot (same ATM IV), the local volatility model recognizes that volatility will change as the spot moves (creating "convexity in vol"), while Black-Scholes assumes volatility stays constant. This produces different deltas: the local vol delta incorporates the anticipated change in volatility, while the Black-Scholes delta does not. This difference is sometimes called the "skew delta" or "smile delta" correction.

    **(c)** Under stochastic volatility, the asset dynamics involve two Brownian motions ($dW_t^S$ for the asset, $dW_t^v$ for volatility). The single tradeable asset $S_t$ can only hedge against $dW_t^S$. The second source of randomness $dW_t^v$ creates unhedgeable volatility risk, making the market incomplete. There are infinitely many risk-neutral measures (parameterized by the market price of volatility risk), and contingent claims generally have a range of arbitrage-free prices rather than a unique price.

---

**Exercise 6.** The Dupire formula in the presence of dividends is

$$
\sigma_{\text{loc}}^2(K,T) = \frac{\partial_T C + (r-q)K\,\partial_K C + qC}{\frac{1}{2}K^2\,\partial_{KK}C}
$$

(a) Show that the $qC$ term in the numerator arises from the dividend-adjusted forward drift $(r-q)S_t$. (b) For an asset with $q > r$, is it possible for the numerator to be negative? If so, what economic interpretation would this have? (c) Verify that setting $q = 0$ recovers the standard Dupire formula.

??? success "Solution to Exercise 6"
    **(a)** With continuous dividend yield $q$, the risk-neutral drift is $(r-q)S_t$ rather than $rS_t$. The call price satisfies $C = e^{-rT}\mathbb{E}^{\mathbb{Q}}[(S_T - K)^+]$, and the underlying has the cost-of-carry $(r-q)$. When deriving the Dupire formula via the Fokker-Planck equation, the drift term $\partial_S[(r-q)Sp]$ produces:

    $$
    C_T = -qC - (r-q)KC_K + \frac{1}{2}\sigma_{\text{loc}}^2 K^2 C_{KK}
    $$

    The $qC$ term arises because the call price includes the present value of dividends paid during the option's life. The continuous dividend yield reduces the forward price growth rate from $r$ to $r-q$, and the $qC$ correction accounts for the difference between discounting at $r$ and the forward drift at $r-q$. Rearranging gives the Dupire formula with $qC$ in the numerator.

    **(b)** If $q > r$, the forward drift $(r-q)$ is negative, meaning the forward price is declining. The numerator of Dupire's formula is $C_T + (r-q)KC_K + qC$. Since $C_K < 0$, the term $(r-q)KC_K = (r-q)K \cdot (\text{negative}) > 0$ when $r - q < 0$. Together with $C_T \geq 0$ and $qC > 0$, the numerator remains non-negative for arbitrage-free prices. It is **not** possible for the numerator to be negative if the call price surface is arbitrage-free, because a negative numerator would imply $\sigma_{\text{loc}}^2 < 0$, which contradicts the existence of a diffusion model.

    **(c)** Setting $q = 0$ in $\sigma_{\text{loc}}^2 = (C_T + (r-q)KC_K + qC)/(\frac{1}{2}K^2 C_{KK})$ gives:

    $$
    \sigma_{\text{loc}}^2(K,T) = \frac{C_T + rKC_K}{\frac{1}{2}K^2 C_{KK}}
    $$

    This is the standard Dupire formula without dividends.

---

**Exercise 7.** Two models are calibrated to the same arbitrage-free call price surface $C(K,T)$: a local volatility model and a Heston stochastic volatility model. (a) By Theorem 13.1.3, the local volatility surface is unique. How is this consistent with the Heston model also matching $C(K,T)$? (b) State Gyongy's theorem relating the Heston instantaneous variance to the local volatility function. (c) Give an example of a derivative whose price differs between the two models despite identical vanilla calibration.

??? success "Solution to Exercise 7"
    **(a)** The uniqueness in Theorem 13.1.3 states: given $C(K, T)$, there is a unique **local volatility function** $\sigma_{\text{loc}}(S, t)$ such that the **one-factor diffusion** $dS_t = (r-q)S_t\,dt + \sigma_{\text{loc}}(S_t, t)S_t\,dW_t$ reproduces $C(K, T)$.

    The Heston model is **not** a local volatility model -- it is a two-factor stochastic volatility model. It reproduces the same call prices $C(K, T)$ through a completely different mechanism: the randomness in the variance process $v_t$ generates the smile, whereas in the local vol model the deterministic function $\sigma_{\text{loc}}(S, t)$ generates the smile. These are different models that agree on vanilla option prices but differ on path-dependent derivatives.

    There is no contradiction because the uniqueness theorem applies only within the class of one-factor Markovian diffusions. The Heston model lies outside this class.

    **(b)** **Gyongy's theorem** (1986): Let $(S_t)$ be a general Ito process (e.g., the Heston model). There exists a Markovian diffusion $(\hat{S}_t)$ with the same marginal distributions as $(S_t)$ at every time $t$. The local volatility of this Markovian "projection" is:

    $$
    \sigma_{\text{loc}}^2(K, t) = \mathbb{E}[v_t \mid S_t = K]
    $$

    where $v_t$ is the instantaneous variance in the Heston model. That is, the local volatility at level $K$ and time $t$ is the conditional expectation of the Heston instantaneous variance, conditioned on the spot price being at $K$. This is how the local volatility model "compresses" the two-dimensional Heston state space $(S_t, v_t)$ into a single dimension while preserving marginal distributions.

    **(c)** A **barrier option**, such as a down-and-out call with barrier $B < S_0$, is an example whose price differs between the two models. The barrier option depends on the entire path of $S_t$ (whether it hits $B$ before $T$), not just the terminal distribution $S_T$. The local volatility model and the Heston model generate different path distributions: the Heston model produces more realistic clustering of volatility (periods of high and low vol), while the local vol model has deterministic volatility. As a result, the probability of hitting the barrier differs between the two models, leading to different barrier option prices even though vanilla prices are identical.
