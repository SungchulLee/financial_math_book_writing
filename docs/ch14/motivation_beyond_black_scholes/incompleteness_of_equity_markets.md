# Incompleteness of Equity Markets

The Black–Scholes model assumes a **complete market**, where all risks can be perfectly hedged using traded instruments. Empirically and structurally, equity markets are incomplete, which fundamentally limits the model's applicability and introduces risk premia for unhedgeable factors.

---

## Market Completeness in Black–Scholes

In the Black–Scholes framework, a market is **complete** if every contingent claim can be replicated by a self-financing trading strategy in the underlying assets.

**Formal definition:** A market is complete if the replicating portfolio $\Pi_t$ satisfies:

$$
\Pi_T = \Phi(S_T) \quad \text{a.s.}
$$

for any payoff $\Phi$, where $\Pi_t$ is constructed from holdings in $S_t$ and the risk-free bond.

**Black–Scholes completeness requires:**

1. **Single source of randomness:** One Brownian motion drives $S_t$
2. **Continuous trading:** Portfolio can be rebalanced continuously
3. **No frictions:** No transaction costs, no constraints
4. **Constant parameters:** $\sigma$, $r$, $q$ are known constants

Under these conditions, the delta-hedging strategy:

$$
\Delta_t = \frac{\partial C}{\partial S}(t, S_t)
$$

replicates any European payoff exactly.

---

## Sources of Incompleteness

Real markets violate the completeness conditions in multiple ways:

### 1. Stochastic Volatility

When volatility is random:

$$
\begin{aligned}
dS_t &= \mu S_t\,dt + \sqrt{V_t} S_t\,dW_t^S \\
dV_t &= a(V_t)\,dt + b(V_t)\,dW_t^V
\end{aligned}
$$

there are **two sources of randomness** ($W^S$, $W^V$) but only **one traded asset** ($S$). The volatility shock $dW_t^V$ cannot be hedged by trading $S$ alone.

**Dimension count:**

- Risk factors: 2 (price, volatility)
- Traded instruments: 1 (underlying) + 1 (bond) = 2
- But bond provides no volatility exposure → effective instruments for volatility: 0

### 2. Jumps and Discontinuities

If prices can jump:

$$
dS_t = \mu S_t\,dt + \sigma S_t\,dW_t + S_{t^-}(e^{J_t} - 1)\,dN_t
$$

where $N_t$ is a Poisson process, then:

- Jump timing is unpredictable
- Jump size may be random
- Continuous hedging cannot eliminate jump risk

Even with deterministic jump sizes, the number of jump states can exceed the number of traded instruments.

### 3. Discrete Trading

In practice, portfolios are rebalanced at discrete times $t_0 < t_1 < \cdots < t_n$. Between rebalancing:

$$
d\Pi_t = \Delta_{t_i}\,dS_t + (r\,dt)\times\text{(cash)}
$$

but $\Delta_{t_i}$ is stale. The **hedging error** accumulates:

$$
\text{Hedging error} = \int_0^T (\Delta_t^{\text{true}} - \Delta_t^{\text{used}})\,dS_t \neq 0
$$

### 4. Transaction Costs

With proportional transaction costs $\epsilon$, frequent rebalancing incurs costs:

$$
\text{Cost} = \epsilon \sum_{i} |S_{t_i}||\Delta_{t_i} - \Delta_{t_{i-1}}|
$$

The trade-off between hedging error and transaction costs introduces irreducible uncertainty.

### 5. Trading Constraints

- Short-selling restrictions
- Position limits
- Margin requirements
- Liquidity constraints

Each constraint reduces the set of feasible hedging strategies.

---

## Consequences for Pricing

In incomplete markets, the fundamental theorem of asset pricing takes a different form:

### Non-Uniqueness of Prices

**Complete market:** Unique no-arbitrage price = replication cost

**Incomplete market:** A range of no-arbitrage prices exists:

$$
\underline{C} \leq C \leq \overline{C}
$$

where:

- $\underline{C}$ = subhedging price (price of cheapest super-replicating portfolio)
- $\overline{C}$ = superhedging price

Any price in $[\underline{C}, \overline{C}]$ is consistent with no-arbitrage.

### Multiple Equivalent Martingale Measures

By the Second Fundamental Theorem of Asset Pricing:

$$
\text{Market complete} \iff \text{Unique EMM } \mathbb{Q}
$$

In incomplete markets, there exists a **family** of equivalent martingale measures $\{\mathbb{Q}_\lambda\}$. Each measure gives a different price:

$$
C_\lambda = e^{-rT}\mathbb{E}^{\mathbb{Q}_\lambda}[\Phi(S_T)]
$$

The selection of $\mathbb{Q}$ requires additional criteria (utility, equilibrium, market price of risk).

### Risk Preferences Matter

In complete markets, prices are preference-free (determined by replication). In incomplete markets:

- Risk-averse agents demand compensation for bearing unhedgeable risk
- Supply and demand equilibrium determines prices
- Different investors may have different valuations

---

## Volatility as a Non-Traded Risk

Volatility occupies a special role in incomplete markets:

### Volatility Cannot Be Directly Traded

While volatility derivatives exist (variance swaps, VIX options), in many markets:

- Volatility is not a directly tradeable asset
- Delta hedging eliminates only price risk, not volatility risk
- Vega exposure remains after delta hedging

### Market Price of Volatility Risk

The change from physical to risk-neutral measure involves a **market price of volatility risk** $\lambda_V$:

$$
dW_t^{V,\mathbb{Q}} = dW_t^{V,\mathbb{P}} - \lambda_V(t, S_t, V_t)\,dt
$$

Under $\mathbb{P}$: volatility dynamics reflect actual evolution
Under $\mathbb{Q}$: volatility dynamics are risk-adjusted for pricing

The difference $\lambda_V$ is not uniquely determined by no-arbitrage—it reflects market equilibrium and risk preferences.

### Volatility Risk Premium

Empirically, volatility risk carries a **negative premium**: sellers of volatility (e.g., variance swap receivers) earn positive expected returns.

$$
\mathbb{E}^{\mathbb{P}}[\text{RV}^2] < \mathbb{E}^{\mathbb{Q}}[\text{RV}^2] = \text{Variance swap rate}
$$

This premium compensates for:

- Jump risk
- Volatility-of-volatility risk
- Correlation with market downturns (volatility spikes when markets crash)

---

## Quantifying Incompleteness

### Variance Optimal Hedge

The mean-variance optimal hedge minimizes:

$$
\min_{\Delta} \mathbb{E}\left[(H - V_T^{\Delta})^2\right]
$$

where $H$ is the claim payoff and $V_T^{\Delta}$ the hedged portfolio value.

The **residual variance** measures incompleteness:

$$
\text{Residual var} = \min_{\Delta} \text{Var}[H - V_T^{\Delta}] > 0
$$

### Minimal Entropy Martingale Measure

Among all EMMs, the **minimal entropy** measure $\mathbb{Q}^*$ minimizes:

$$
\mathbb{Q}^* = \arg\min_{\mathbb{Q}} H(\mathbb{Q} | \mathbb{P}) = \arg\min_{\mathbb{Q}} \mathbb{E}^{\mathbb{Q}}\left[\log\frac{d\mathbb{Q}}{d\mathbb{P}}\right]
$$

This provides a principled way to select among EMMs.

### Utility Indifference Pricing

An agent with utility $U$ values a claim at the **indifference price** $p$:

$$
\sup_{\pi} \mathbb{E}[U(X_T^{\pi})] = \sup_{\pi} \mathbb{E}[U(X_T^{\pi} + H - p)]
$$

where $\pi$ ranges over admissible trading strategies.

---

## Practical Implications

### Hedging in Incomplete Markets

Since perfect replication is impossible:

1. **Partial hedging:** Reduce but don't eliminate risk
2. **Variance swaps:** Trade volatility risk directly when available
3. **Options on options:** Use the smile to hedge smile risk
4. **Robust hedging:** Minimize worst-case loss across models

### Model Selection

Different models imply different:

- Risk-neutral dynamics
- Volatility risk premia
- Hedging strategies
- Price ranges

Model selection is a form of specifying risk preferences.

### P&L Attribution

In incomplete markets, hedging P&L decomposes as:

$$
\text{P\&L} = \underbrace{\text{Gamma P\&L}}_{\text{hedgeable}} + \underbrace{\text{Vega P\&L}}_{\text{partially hedgeable}} + \underbrace{\text{Volga/Vanna P\&L}}_{\text{higher-order}} + \underbrace{\text{Unexplained}}_{\text{model error}}
$$

---

## Key Takeaways

- Equity markets are incomplete: not all risks can be hedged
- Sources include stochastic volatility, jumps, discrete trading, and frictions
- Incompleteness implies non-unique prices and multiple EMMs
- Volatility risk is the primary unhedgeable factor in equity markets
- Risk premia emerge naturally for bearing unhedgeable risks
- Model selection and measure choice reflect risk preferences

---

## Further Reading

- Harrison, J.M. & Kreps, D. (1979). *Martingales and arbitrage in multiperiod securities markets*. Journal of Economic Theory.
- Harrison, J.M. & Pliska, S. (1981). *Martingales and stochastic integrals in the theory of continuous trading*. Stochastic Processes and Applications.
- Duffie, D. (2001). *Dynamic Asset Pricing Theory*, 3rd ed. Princeton University Press.
- Föllmer, H. & Schied, A. (2016). *Stochastic Finance: An Introduction in Discrete Time*, 4th ed. De Gruyter.
- Cont, R. (2006). *Model uncertainty and its impact on the pricing of derivative instruments*. Mathematical Finance.

---

## Exercises

**Exercise 1.** Consider a market with two sources of randomness ($W^S$, $W^V$) but only one risky asset $S$ and a risk-free bond. Using a dimension-counting argument, explain why this market is incomplete. How many additional traded instruments would be needed to restore completeness?

??? success "Solution to Exercise 1"
    **Dimension-counting argument:**

    In this market the sources of randomness (risk factors) are:

    - $W^S$: the Brownian motion driving the stock price
    - $W^V$: the Brownian motion driving volatility

    This gives **2 independent sources of risk**.

    The traded instruments available for hedging are:

    - The risky asset $S$ (provides exposure to $W^S$ and, via correlation, partially to $W^V$)
    - The risk-free bond (provides no exposure to either $W^S$ or $W^V$)

    This gives **1 effective instrument** for hedging stochastic risk (the bond only determines the risk-free rate).

    For a market to be complete, we need at least as many linearly independent traded instruments (excluding the numeraire) as there are independent sources of randomness. Here we have 2 risk factors but only 1 risky instrument, so:

    $$
    \text{Number of risk factors} = 2 > 1 = \text{Number of risky traded instruments}
    $$

    The market is therefore **incomplete**. The component of risk driven by $W^V$ that is orthogonal to $W^S$ cannot be replicated by any portfolio of $S$ and the bond.

    **To restore completeness:** We need **one additional traded instrument** whose price depends on $W^V$ in a linearly independent way from $S$. Examples include:

    - A traded option on $S$ (whose price depends on $V_t$ through vega)
    - A variance swap on $S$
    - A VIX futures contract

    With two risky instruments and two risk factors, the market becomes (generically) complete.

---

**Exercise 2.** In a stochastic volatility model, two equivalent martingale measures $\mathbb{Q}_1$ and $\mathbb{Q}_2$ give call option prices $C_1 = 5.20$ and $C_2 = 5.80$ for the same strike and maturity. What can you conclude about the no-arbitrage bounds $[\underline{C}, \overline{C}]$? Explain why, unlike in the Black–Scholes model, additional economic assumptions are needed to select a unique price.

??? success "Solution to Exercise 2"
    **No-arbitrage bounds:** Since both $\mathbb{Q}_1$ and $\mathbb{Q}_2$ are valid equivalent martingale measures, the prices $C_1 = 5.20$ and $C_2 = 5.80$ are both consistent with no-arbitrage. Therefore:

    $$
    \underline{C} \leq 5.20 < 5.80 \leq \overline{C}
    $$

    The no-arbitrage bounds satisfy $\overline{C} - \underline{C} \geq 5.80 - 5.20 = 0.60$. The true bounds may be wider, since other EMMs may produce prices outside $[5.20, 5.80]$.

    **Why additional assumptions are needed:** In the Black–Scholes model, the market is complete, so the EMM is unique and the price is determined solely by no-arbitrage (it equals the replication cost). In a stochastic volatility model:

    1. Multiple EMMs exist because the market price of volatility risk $\lambda_V$ is not pinned down by no-arbitrage alone
    2. Each choice of $\lambda_V$ selects a different $\mathbb{Q}$, giving a different price
    3. To select a unique price, one must impose additional economic criteria such as:
        - Equilibrium arguments (supply and demand)
        - Utility maximization (indifference pricing)
        - Calibration to other traded derivatives (e.g., matching vanilla option prices to pin down $\lambda_V$)
        - Minimum entropy or variance-optimal criteria

---

**Exercise 3.** The market price of volatility risk $\lambda_V$ transforms the volatility Brownian motion from $\mathbb{P}$ to $\mathbb{Q}$ via

$$
dW_t^{V,\mathbb{Q}} = dW_t^{V,\mathbb{P}} - \lambda_V\,dt
$$

If the physical-measure volatility dynamics are $dV_t = \kappa(\theta - V_t)\,dt + \xi\sqrt{V_t}\,dW_t^V$, write the risk-neutral dynamics under $\mathbb{Q}$ explicitly. Identify the risk-neutral mean-reversion speed and long-run variance level in terms of $\kappa$, $\theta$, $\xi$, and $\lambda_V$ (assuming $\lambda_V$ is constant).

??? success "Solution to Exercise 3"
    Under the physical measure $\mathbb{P}$, the volatility dynamics are:

    $$
    dV_t = \kappa(\theta - V_t)\,dt + \xi\sqrt{V_t}\,dW_t^{V,\mathbb{P}}
    $$

    Applying the Girsanov transformation $dW_t^{V,\mathbb{Q}} = dW_t^{V,\mathbb{P}} - \lambda_V\,dt$, we substitute $dW_t^{V,\mathbb{P}} = dW_t^{V,\mathbb{Q}} + \lambda_V\,dt$:

    $$
    dV_t = \kappa(\theta - V_t)\,dt + \xi\sqrt{V_t}\,(dW_t^{V,\mathbb{Q}} + \lambda_V\,dt)
    $$

    $$
    dV_t = [\kappa(\theta - V_t) + \xi\lambda_V\sqrt{V_t}]\,dt + \xi\sqrt{V_t}\,dW_t^{V,\mathbb{Q}}
    $$

    For the common parameterization where $\lambda_V = \lambda_0 \sqrt{V_t}$ (i.e., the market price of risk is proportional to $\sqrt{V_t}$, which keeps the CIR structure), we can write $\lambda_V \sqrt{V_t} \to \lambda_0 V_t$ and obtain:

    $$
    dV_t = [\kappa\theta - (\kappa - \xi\lambda_0)V_t]\,dt + \xi\sqrt{V_t}\,dW_t^{V,\mathbb{Q}}
    $$

    $$
    dV_t = \kappa^{\mathbb{Q}}(\theta^{\mathbb{Q}} - V_t)\,dt + \xi\sqrt{V_t}\,dW_t^{V,\mathbb{Q}}
    $$

    where the **risk-neutral parameters** are:

    - Risk-neutral mean-reversion speed: $\kappa^{\mathbb{Q}} = \kappa - \xi\lambda_0$
    - Risk-neutral long-run variance: $\theta^{\mathbb{Q}} = \dfrac{\kappa\theta}{\kappa - \xi\lambda_0} = \dfrac{\kappa\theta}{\kappa^{\mathbb{Q}}}$

    If instead $\lambda_V$ is a constant (not proportional to $\sqrt{V_t}$), the drift becomes $\kappa(\theta - V_t) + \xi\lambda_V\sqrt{V_t}$, which does not have a simple CIR form and requires numerical treatment.

---

**Exercise 4.** The variance risk premium is defined as $VRP = \mathbb{E}^{\mathbb{Q}}[\sigma^2] - \mathbb{E}^{\mathbb{P}}[\sigma^2]$. Suppose the variance swap rate (risk-neutral expected variance) for a 1-month horizon is $(18\%)^2$ and the expected realized variance under $\mathbb{P}$ is $(15\%)^2$. Compute the VRP in variance terms and explain why a negative risk premium for variance sellers (positive $VRP$) is economically consistent with the leverage effect.

??? success "Solution to Exercise 4"
    **Variance risk premium computation:**

    $$
    VRP = \mathbb{E}^{\mathbb{Q}}[\sigma^2] - \mathbb{E}^{\mathbb{P}}[\sigma^2] = (0.18)^2 - (0.15)^2 = 0.0324 - 0.0225 = 0.0099
    $$

    In percentage-squared terms: $VRP = 99$ variance points (i.e., $0.99\%$ in variance terms).

    Converting to volatility terms for intuition: $\sqrt{0.0324} - \sqrt{0.0225} = 18\% - 15\% = 3\%$ volatility points.

    **Economic consistency with the leverage effect:**

    A positive $VRP$ means variance swap sellers (who receive the swap rate and pay realized variance) earn a positive expected profit:

    $$
    \text{Expected P\&L} = \mathbb{E}^{\mathbb{Q}}[\sigma^2] - \mathbb{E}^{\mathbb{P}}[\sigma^2] = 0.0099 > 0
    $$

    This is a **negative risk premium for variance buyers** (they pay more than the expected realized variance) and a **positive expected return for variance sellers**. This is economically consistent because:

    1. **Leverage effect link:** Volatility spikes coincide with market downturns. Selling variance is equivalent to providing insurance against crashes
    2. **Negative correlation with wealth:** Variance sellers lose precisely when markets are falling and investors' marginal utility of wealth is highest
    3. **Risk compensation:** The positive $VRP$ compensates sellers for bearing this systematic, unhedgeable risk — variance is high exactly when additional losses are most painful
    4. **Insurance analogy:** Just as insurance premiums exceed expected losses, the variance swap rate exceeds expected realized variance

---

**Exercise 5.** A trader holds a delta-hedged short call position. Decompose the hedging P&L into gamma, vega, and higher-order components:

$$
\text{P\&L} = \text{Gamma P\&L} + \text{Vega P\&L} + \text{Volga/Vanna P\&L} + \text{Unexplained}
$$

Explain which components are hedgeable using only the underlying stock, and which require additional instruments such as options. Why does market incompleteness make it impossible to eliminate all components simultaneously?

??? success "Solution to Exercise 5"
    **Gamma P&L (hedgeable):** This component arises from the convexity of the option value with respect to the underlying price. It is proportional to $\frac{1}{2}\Gamma(\Delta S)^2$ and can be hedged by dynamically adjusting the delta position using the underlying stock. In a complete market with known constant volatility, gamma P&L is fully captured by delta hedging.

    **Vega P&L (partially hedgeable):** This component arises from changes in implied volatility. It equals approximately $\mathcal{V} \cdot \Delta\sigma_{\text{impl}}$, where $\mathcal{V}$ is the option's vega. The underlying stock has zero vega, so **vega P&L cannot be hedged using only the stock**. It requires trading other options (which have non-zero vega) to offset this exposure.

    **Volga/Vanna P&L (requires additional instruments):**

    - **Volga** (sensitivity of vega to volatility): requires options at different strikes to hedge
    - **Vanna** (sensitivity of delta to volatility, or equivalently sensitivity of vega to the underlying): requires options to hedge since the stock cannot provide volatility exposure

    These higher-order terms require a portfolio of options across multiple strikes to manage.

    **Unexplained (model error):** This residual captures P&L from model misspecification, discretization error, and other effects not captured by the Greek decomposition.

    **Why incompleteness prevents simultaneous elimination:** With only one risky asset $S$, the trader has a single instrument to hedge multiple risk factors (price risk, volatility risk, vol-of-vol risk). Each option added to the hedge portfolio provides one additional degree of freedom. To eliminate all components simultaneously, one would need:

    - The underlying $S$ (for delta/gamma)
    - At least one option (for vega)
    - Additional options at different strikes (for volga/vanna)

    In practice, even with multiple options, model error and discrete rebalancing leave a residual, reflecting the fundamental incompleteness of the market.

---

**Exercise 6.** In utility indifference pricing, an agent with exponential utility $U(x) = -e^{-\gamma x}$ values a claim at the price $p$ satisfying

$$
\sup_{\pi} \mathbb{E}[U(X_T^{\pi})] = \sup_{\pi} \mathbb{E}[U(X_T^{\pi} + H - p)]
$$

Explain intuitively why this price depends on the risk aversion parameter $\gamma$. What happens to the indifference price as $\gamma \to 0$ (risk-neutral agent)? As $\gamma \to \infty$ (infinitely risk-averse agent)?

??? success "Solution to Exercise 6"
    **Intuition for $\gamma$-dependence:** The indifference price $p$ is the amount the agent would accept (or pay) such that their maximum expected utility is the same with or without the claim $H$. The claim introduces unhedgeable risk, and the agent's valuation of that risk depends on their risk aversion:

    - A more risk-averse agent ($\gamma$ large) demands more compensation for bearing the unhedgeable component of $H$
    - A less risk-averse agent ($\gamma$ small) is less concerned about residual risk

    **As $\gamma \to 0$ (risk-neutral agent):**

    The exponential utility $U(x) = -e^{-\gamma x}$ approaches linearity: $U(x) \approx -1 + \gamma x$ for small $\gamma$. A risk-neutral agent values any claim at its expected discounted payoff under a martingale measure. In the incomplete market setting, the indifference price converges to the price under the **minimal entropy martingale measure**, which lies within the no-arbitrage bounds:

    $$
    p \to \mathbb{E}^{\mathbb{Q}^{\text{ME}}}[e^{-rT}H]
    $$

    **As $\gamma \to \infty$ (infinitely risk-averse agent):**

    An infinitely risk-averse agent demands compensation for the worst-case scenario. The indifference price for a buyer converges to the **subhedging price** $\underline{C}$, and for a seller converges to the **superhedging price** $\overline{C}$:

    - **Buyer's price:** $p \to \underline{C}$ (will only buy at the lowest no-arbitrage price)
    - **Seller's price:** $p \to \overline{C}$ (will only sell at the highest no-arbitrage price)

    This is because an infinitely risk-averse agent requires a strategy that covers the claim in all scenarios, which is exactly super-replication.

---

**Exercise 7.** Consider a jump-diffusion model where the stock follows

$$
dS_t = \mu S_t\,dt + \sigma S_t\,dW_t + S_{t^-}(e^J - 1)\,dN_t
$$

with $N_t$ a Poisson process with intensity $\lambda = 2$ per year and $J \sim \mathcal{N}(-0.05, 0.1^2)$. Even if $\sigma$ is constant, explain why the market is still incomplete. What additional instrument(s) could partially complete the market?

??? success "Solution to Exercise 7"
    **Why the market is incomplete even with constant $\sigma$:**

    The model has the following sources of randomness:

    1. The continuous Brownian motion $W_t$ (diffusion risk)
    2. The Poisson process $N_t$ (jump timing risk)
    3. The random jump size $J$ (jump magnitude risk)

    With only one traded risky asset $S$ and the risk-free bond, there are **three sources of randomness but only one risky instrument**. Even though $\sigma$ is constant (so there is no stochastic volatility), the jump component introduces two additional risk factors:

    - **Jump timing:** The Poisson process $N_t$ introduces discontinuous risk that cannot be hedged by continuous delta adjustments. Between jumps, delta hedging works, but at the instant of a jump, the stock price gaps and the hedge fails
    - **Jump size:** Even if the jump timing were known, the random magnitude $J \sim \mathcal{N}(-0.05, 0.1^2)$ creates additional uncertainty

    Formally, the martingale representation theorem fails because the filtration is generated by both $W_t$ and the compound Poisson process. A portfolio of $S$ and the bond can only span the $W_t$-generated risk.

    **Additional instruments to partially complete the market:**

    - **One option** (e.g., an OTM put) would add exposure to jump risk, allowing hedging of the "average" jump impact. This partially completes the market if jump sizes are deterministic
    - **Multiple options at different strikes** are needed if jump sizes are random, since each strike provides information about a different region of the jump-size distribution
    - **Credit default swaps** or **catastrophe bonds** could provide direct exposure to jump risk
    - In the limit, a continuum of European options across all strikes would fully span the jump-size distribution (via the Breeden–Litzenberger result), restoring completeness
