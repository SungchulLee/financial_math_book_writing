# Physical vs Risk-Neutral World

Every derivative price in this book ultimately rests on a single formula:
$V_0 = \mathbb{E}^{\mathbb{Q}}[e^{-rT}X_T]$. The expectation is taken not
under the probability measure that governs real-world returns, but under a
different measure $\mathbb{Q}$ constructed specifically for pricing. The
distinction between these two measures---the physical measure $\mathbb{P}$ and
the risk-neutral measure $\mathbb{Q}$---is the most important conceptual
boundary in quantitative finance. Confusing them leads to pricing errors,
flawed risk estimates, and deep misunderstandings of what models actually say.

This page establishes what each measure is, why they differ, and how
Girsanov's theorem connects them. A worked example derives the Black--Scholes
formula directly from $\mathbb{Q}$-dynamics.

---

## The Physical Measure ℙ

When we observe market prices, estimate returns from historical data, or
simulate future portfolio values for risk management, we are working under the
physical measure $\mathbb{P}$. This is the measure that governs how asset
prices actually evolve in the real world.

Under $\mathbb{P}$, a stock modeled by geometric Brownian motion satisfies

$$
dS_t = \mu S_t\,dt + \sigma S_t\,dW_t^{\mathbb{P}}
$$

where $\mu$ is the physical drift (expected return) and $\sigma$ is the
volatility. The drift $\mu$ reflects economic fundamentals: growth prospects,
risk premia demanded by investors, and the compensation required for bearing
uncertainty. Different assets carry different drifts because investors require
different compensation for different risks.

The physical measure is the right tool for:

- **Forecasting**: estimating where prices will be in the future
- **Risk management**: computing Value-at-Risk, expected shortfall, and
  stress-test scenarios
- **Portfolio optimization**: maximizing expected utility of terminal wealth

What $\mathbb{P}$ is *not* suited for is pricing derivatives. The reason is
subtle but fundamental: a derivative's price must be consistent with
no-arbitrage, and no-arbitrage imposes constraints that the physical measure
does not automatically satisfy.

---

## The Risk-Neutral Measure ℚ

The risk-neutral measure $\mathbb{Q}$ is not a description of how prices
actually evolve---it is a mathematical device engineered so that derivative
prices can be computed as discounted expectations. Its construction is the
central achievement of the no-arbitrage pricing theory.

The defining property of $\mathbb{Q}$ is the **martingale condition**:
discounted asset prices are martingales under $\mathbb{Q}$. For a stock $S_t$
and money market account $B_t = e^{rt}$, this means

$$
\mathbb{E}^{\mathbb{Q}}\!\left[\frac{S_T}{B_T}\,\Big|\,\mathcal{F}_t\right] = \frac{S_t}{B_t}
$$

This condition has an immediate and powerful consequence. For any contingent
claim with payoff $X_T$ at maturity $T$, the no-arbitrage price at time $0$
is

$$
\boxed{V_0 = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-rT}X_T\right]}
$$

This is the **risk-neutral valuation formula**---the heart of Section 4. The
proof follows from the martingale property: if the discounted value process
$e^{-rt}V_t$ is a $\mathbb{Q}$-martingale, then evaluating at $t = 0$ gives

$$
V_0 = e^{-r \cdot 0}V_0 = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-rT}V_T\,|\,\mathcal{F}_0\right] = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-rT}X_T\right]
$$

since $V_T = X_T$ at maturity. The entire problem of pricing a derivative
reduces to computing an integral under the right measure.

Under $\mathbb{Q}$, the stock dynamics become

$$
dS_t = rS_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}}
$$

Every traded asset drifts at the risk-free rate $r$, regardless of its
physical drift $\mu$. The volatility $\sigma$ is unchanged. This is not a
statement about investor beliefs---it is a consequence of the no-arbitrage
requirement built into the measure.

---

## Same Paths, Different Weights

A crucial point is that $\mathbb{P}$ and $\mathbb{Q}$ are **equivalent
measures**: they agree on which events are possible and which are impossible.
Formally, $\mathbb{P}(A) = 0$ if and only if $\mathbb{Q}(A) = 0$ for every
measurable event $A$. The set of sample paths $\omega \in \Omega$ is the same
under both measures---the stock can reach the same prices, follow the same
trajectories, and produce the same extreme outcomes.

What changes is the *weighting* of those paths. The Radon--Nikodym derivative

$$
\frac{d\mathbb{Q}}{d\mathbb{P}}\bigg|_{\mathcal{F}_T} = Z_T = \exp\!\left(-\theta W_T^{\mathbb{P}} - \frac{1}{2}\theta^2 T\right)
$$

where $\theta = (\mu - r)/\sigma$ is the market price of risk, reweights
each path $\omega$. Paths where the stock performs well (high $W_T^{\mathbb{P}}$
values) are downweighted by $Z_T$; paths where the stock performs poorly are
upweighted. The effect is precisely to remove the risk premium from the drift.

!!! note "Equivalence is essential"
    If $\mathbb{Q}$ assigned zero probability to an event that $\mathbb{P}$
    considers possible, a contingent claim paying off only in that event would
    be priced at zero yet could deliver a positive payoff---a free lunch. The
    fundamental theorem of asset pricing requires equivalence to prevent such
    arbitrage.

---

## Why Drift Disappears

Readers familiar with
[Girsanov's theorem](../girsanov/girsanov_theorem.md) will recognize the
mechanism immediately; here is a short self-contained reminder of why the
physical drift $\mu$ vanishes from derivative prices.

Under $\mathbb{P}$, the stock satisfies

$$
dS_t = \mu S_t\,dt + \sigma S_t\,dW_t^{\mathbb{P}}
$$

The market price of risk is $\theta = (\mu - r)/\sigma$, and Girsanov's
theorem defines a new Brownian motion under $\mathbb{Q}$:

$$
W_t^{\mathbb{Q}} = W_t^{\mathbb{P}} + \theta t
$$

Substituting $dW_t^{\mathbb{P}} = dW_t^{\mathbb{Q}} - \theta\,dt$ into the
stock dynamics:

$$
dS_t = \mu S_t\,dt + \sigma S_t\!\left(dW_t^{\mathbb{Q}} - \theta\,dt\right) = (\mu - \sigma\theta)S_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}}
$$

Since $\mu - \sigma\theta = \mu - (\mu - r) = r$, the $\mathbb{Q}$-dynamics
are

$$
dS_t = rS_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}}
$$

The risk premium $\mu - r$ has been absorbed into the measure change. Two
observations are worth emphasizing:

1. **Volatility is unchanged.** The diffusion coefficient $\sigma$ is
   identical under both measures. This is because quadratic variation is a
   path-by-path property---it depends only on the realized trajectory, not on
   the probability measure used to weight trajectories.

2. **The physical drift $\mu$ is irrelevant for pricing.** It enters the
   Radon--Nikodym derivative $Z_T$ but cancels out of any
   $\mathbb{Q}$-expectation. Derivative prices depend on $r$, $\sigma$,
   $S_0$, $K$, and $T$, but not on $\mu$.

For the full decomposition $\mu = r + \sigma\theta$ and its financial
interpretation, see
[Risk Premium Decomposition](risk_premium_decomposition.md).

---

## Example: European Call Pricing

The risk-neutral valuation formula transforms derivative pricing into a
calculation. Here we derive the Black--Scholes formula for a European call
option with strike $K$ and maturity $T$, starting from the
$\mathbb{Q}$-dynamics established above.

**Step 1: Terminal stock price under $\mathbb{Q}$.**
Applying Ito's lemma to $\ln S_t$ under $\mathbb{Q}$ gives

$$
S_T = S_0\exp\!\left[\left(r - \tfrac{1}{2}\sigma^2\right)T + \sigma W_T^{\mathbb{Q}}\right]
$$

Since $W_T^{\mathbb{Q}} \sim N(0, T)$ under $\mathbb{Q}$, we can write
$W_T^{\mathbb{Q}} = \sqrt{T}\,Z$ where $Z \sim N(0,1)$.

**Step 2: Apply the pricing formula.**
The call price is

$$
C_0 = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-rT}(S_T - K)^+\right]
$$

The payoff $(S_T - K)^+$ is positive when $S_T > K$, i.e., when

$$
Z > -\frac{\ln(S_0/K) + (r - \sigma^2/2)T}{\sigma\sqrt{T}} = -d_2
$$

where we define

$$
d_1 = \frac{\ln(S_0/K) + (r + \sigma^2/2)T}{\sigma\sqrt{T}}, \qquad d_2 = d_1 - \sigma\sqrt{T}
$$

**Step 3: Evaluate the expectation.**
Splitting the expectation and completing the square (the standard Gaussian
integral calculation) yields the **Black--Scholes formula**:

$$
\boxed{C_0 = S_0\,N(d_1) - Ke^{-rT}N(d_2)}
$$

where $N(\cdot)$ is the standard normal CDF.

The formula depends on five inputs---$S_0$, $K$, $T$, $r$, $\sigma$---but
not on the physical drift $\mu$. This is the signature of risk-neutral
pricing: the measure change has absorbed all information about expected
returns into $\mathbb{Q}$, and the resulting price depends only on
volatility and the risk-free rate.

!!! tip "Consistency check"
    Setting $K = 0$ in the formula gives $C_0 = S_0$ (since $N(d_1) \to 1$
    and $Ke^{-rT}N(d_2) \to 0$), confirming that the model correctly prices
    the stock itself.

---

## Why ℚ Is Not "Believed"

The risk-neutral measure is one of the most misunderstood objects in
quantitative finance. Because every asset earns the risk-free rate under
$\mathbb{Q}$, it is tempting to interpret $\mathbb{Q}$ as describing a world
of risk-neutral investors. This interpretation is misleading in several ways.

**$\mathbb{Q}$ is not a forecast.** Risk-neutral probabilities do not predict
future prices. If a stock has a 60% physical probability of rising and a 45%
risk-neutral probability of rising, the 45% figure carries no information
about what will actually happen.

**$\mathbb{Q}$ does not reflect beliefs.** No market participant believes
that all assets earn $r$. The measure $\mathbb{Q}$ is a mathematical
construction---a change of variables that converts pricing into an expectation
calculation.

**$\mathbb{Q}$ does encode risk preferences---indirectly.** The
Radon--Nikodym derivative $Z_T = d\mathbb{Q}/d\mathbb{P}$ depends on the
market price of risk $\theta$, which measures the compensation investors
demand for bearing uncertainty. In a truly risk-neutral world, $\mathbb{P}$
would already satisfy the martingale property and $\mathbb{Q} = \mathbb{P}$.
The fact that $\mathbb{Q} \neq \mathbb{P}$ is precisely the signature of
risk aversion. At a deeper level, the measure change is equivalent to
introducing a **stochastic discount factor** that reweights outcomes by
marginal utility---see [Stochastic Discount Factor](sdf.md).

**The correct framing:** $\mathbb{Q}$ is the unique measure (in complete
markets) that makes discounted prices martingales and thereby enforces
no-arbitrage pricing. It is a pricing tool, not a worldview.

---

## Practical Implications

The P/Q distinction is not merely philosophical---it has direct consequences
for how quantitative work is organized. Using the wrong measure for a given
task produces systematic errors that no amount of calibration can fix.

| Task | Measure | Why |
|---|---|---|
| Derivative pricing | $\mathbb{Q}$ | No-arbitrage requires martingale discounting |
| Hedging ratios (Greeks) | $\mathbb{Q}$ | Greeks are derivatives of $\mathbb{Q}$-prices |
| Value-at-Risk | $\mathbb{P}$ | VaR measures real-world loss probabilities |
| Expected shortfall | $\mathbb{P}$ | Tail risk is a physical-measure concept |
| Portfolio optimization | $\mathbb{P}$ | Expected returns matter for allocation |
| Model calibration | $\mathbb{Q}$ | Market prices are $\mathbb{Q}$-expectations |
| Backtesting | $\mathbb{P}$ | Historical returns are $\mathbb{P}$-realizations |

!!! warning "A common error"
    Using risk-neutral probabilities for risk management overstates the
    likelihood of adverse outcomes (because $\mathbb{Q}$ upweights bad
    states). Using physical probabilities for pricing violates no-arbitrage
    consistency. The two measures answer different questions and must not be
    interchanged.

---

## Exercises

**Exercise 1.**
A stock follows geometric Brownian motion under $\mathbb{P}$ with
$\mu = 0.12$, $\sigma = 0.30$, and the risk-free rate is $r = 0.04$.
Compute the market price of risk $\theta$, write down the stock dynamics
under $\mathbb{Q}$, and verify explicitly that the risk premium
$\mu - r$ is absorbed into the measure change.

??? success "Solution to Exercise 1"
    The market price of risk is

    $$
    \theta = \frac{\mu - r}{\sigma} = \frac{0.12 - 0.04}{0.30} = \frac{0.08}{0.30} \approx 0.2667
    $$

    Girsanov's theorem defines $W_t^{\mathbb{Q}} = W_t^{\mathbb{P}} + \theta t$, so $dW_t^{\mathbb{P}} = dW_t^{\mathbb{Q}} - \theta\,dt$. Substituting into the $\mathbb{P}$-dynamics:

    $$
    dS_t = \mu S_t\,dt + \sigma S_t\,dW_t^{\mathbb{P}} = \mu S_t\,dt + \sigma S_t(dW_t^{\mathbb{Q}} - \theta\,dt)
    $$

    $$
    = (\mu - \sigma\theta)S_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}}
    $$

    Since $\sigma\theta = 0.30 \times 0.2667 = 0.08 = \mu - r$, the drift becomes

    $$
    \mu - \sigma\theta = 0.12 - 0.08 = 0.04 = r
    $$

    The risk-neutral dynamics are

    $$
    dS_t = 0.04\,S_t\,dt + 0.30\,S_t\,dW_t^{\mathbb{Q}}
    $$

    The risk premium $\mu - r = 0.08$ has been entirely absorbed into the measure change via the term $\sigma\theta\,dt$. The volatility $\sigma = 0.30$ is unchanged because quadratic variation is invariant under equivalent measure changes.

---

**Exercise 2.**
A European call option has $S_0 = 100$, $K = 105$, $T = 0.5$,
$r = 0.03$, and $\sigma = 0.20$. Compute the Black--Scholes price $C_0$.
Then verify the consistency check $C_0 \to S_0$ as $K \to 0$.

??? success "Solution to Exercise 2"
    First compute $d_1$ and $d_2$:

    $$
    d_1 = \frac{\ln(100/105) + (0.03 + 0.02)  \times 0.5}{0.20\sqrt{0.5}} = \frac{\ln(0.9524) + 0.025}{0.1414} = \frac{-0.04879 + 0.025}{0.1414} = \frac{-0.02379}{0.1414} \approx -0.1683
    $$

    $$
    d_2 = d_1 - \sigma\sqrt{T} = -0.1683 - 0.1414 \approx -0.3097
    $$

    Using the standard normal CDF:

    $$
    N(d_1) = N(-0.1683) \approx 0.4332, \qquad N(d_2) = N(-0.3097) \approx 0.3785
    $$

    The Black--Scholes price is

    $$
    C_0 = 100 \times 0.4332 - 105 \times e^{-0.03 \times 0.5} \times 0.3785
    $$

    $$
    = 43.32 - 105 \times 0.9851 \times 0.3785 = 43.32 - 39.14 \approx \$4.18
    $$

    For the consistency check: as $K \to 0$, the call becomes certain to finish in the money. We have $d_1 = [\ln(S_0/K) + (r + \sigma^2/2)T]/(\sigma\sqrt{T}) \to +\infty$ and $d_2 \to +\infty$, so $N(d_1) \to 1$ and $N(d_2) \to 1$. Then

    $$
    C_0 \to S_0 \cdot 1 - 0 \cdot e^{-rT} \cdot 1 = S_0
    $$

    confirming the formula correctly prices a zero-strike call at $S_0$.

---

**Exercise 3.**
Prove that the volatility $\sigma$ is the same under $\mathbb{P}$ and
$\mathbb{Q}$. Specifically, show that the quadratic variation
$\langle \ln S \rangle_t = \sigma^2 t$ is invariant under the measure change
from $\mathbb{P}$ to $\mathbb{Q}$.

??? success "Solution to Exercise 3"
    Under $\mathbb{P}$, Ito's formula gives

    $$
    d\ln S_t = \left(\mu - \tfrac{1}{2}\sigma^2\right)dt + \sigma\,dW_t^{\mathbb{P}}
    $$

    Under $\mathbb{Q}$, the same calculation gives

    $$
    d\ln S_t = \left(r - \tfrac{1}{2}\sigma^2\right)dt + \sigma\,dW_t^{\mathbb{Q}}
    $$

    The quadratic variation of $\ln S$ is determined by the diffusion coefficient alone:

    $$
    \langle \ln S \rangle_t = \int_0^t \sigma^2\,ds = \sigma^2 t
    $$

    under both measures. The key insight is that quadratic variation is a **pathwise** property---it depends only on the realized sample path $\omega$, not on how paths are weighted. Formally, quadratic variation is defined as

    $$
    \langle \ln S \rangle_t = \lim_{n \to \infty} \sum_{k=0}^{n-1} \left(\ln S_{t_{k+1}} - \ln S_{t_k}\right)^2
    $$

    where the limit is taken along partitions of $[0, t]$. Since $\mathbb{P}$ and $\mathbb{Q}$ are equivalent measures (they agree on which paths have probability zero), the limit is the same path-by-path, and hence the quadratic variation is identical under both measures.

    This is why derivative prices depend on $\sigma$ (a path property) but not on $\mu$ (a measure-dependent property): $\sigma$ is observable from the path, while $\mu$ is absorbed into the measure change. $\square$

---

**Exercise 4.**
A risk manager computes that a portfolio has a 3% physical probability of
losing more than \$2 million over the next quarter. A pricing quant reports
that the risk-neutral probability of the same event is 8%. Explain why these
numbers differ. If a third analyst uses the 8% figure in a VaR report, what
error does this introduce and in which direction?

??? success "Solution to Exercise 4"
    The two probabilities differ because they are computed under different measures that serve fundamentally different purposes.

    The physical probability $\mathbb{P}(\text{loss} > \$2\text{M}) = 3\%$ reflects actual market dynamics---empirical return distributions, risk premia, and historical correlations. This is the correct input for risk management.

    The risk-neutral probability $\mathbb{Q}(\text{loss} > \$2\text{M}) = 8\%$ comes from the pricing measure, which reweights scenarios to enforce the martingale property. The measure change from $\mathbb{P}$ to $\mathbb{Q}$ removes the positive risk premium from asset drifts, effectively lowering expected returns. This tilts the distribution toward adverse outcomes: losses become more probable under $\mathbb{Q}$ than under $\mathbb{P}$.

    The third analyst's error is using the risk-neutral probability for risk management. Since $\mathbb{Q}$ upweights bad states (to compensate for the removed risk premium), the 8% figure **overstates** the actual likelihood of the loss event. The VaR threshold would be set too conservatively: the analyst would report that the portfolio exceeds the \$2M loss with probability 8% rather than the true 3%, leading to excessive capital reserves or unnecessarily restrictive position limits.

    The correct practice: use $\mathbb{P}$ for risk (VaR, expected shortfall, stress testing) and $\mathbb{Q}$ for pricing (derivative valuation, calibration). The two measures answer different questions and must not be interchanged.

---

**Exercise 5.**
Suppose $\mathbb{Q} = \mathbb{P}$ for a particular asset (the physical and
risk-neutral measures coincide). What does this imply about the asset's
expected return under $\mathbb{P}$? What does it imply about investor risk
preferences with respect to this asset? Prove your claims using the
relationship $\theta = (\mu - r)/\sigma$.

??? success "Solution to Exercise 5"
    If $\mathbb{Q} = \mathbb{P}$, the Radon--Nikodym derivative is $Z_T = d\mathbb{Q}/d\mathbb{P} = 1$ almost surely. Since

    $$
    Z_T = \exp\!\left(-\theta W_T^{\mathbb{P}} - \frac{1}{2}\theta^2 T\right) = 1
    $$

    this requires $\theta = 0$ (since $W_T^{\mathbb{P}}$ is a non-degenerate random variable, the exponent must vanish identically). From $\theta = (\mu - r)/\sigma = 0$, we conclude

    $$
    \mu = r
    $$

    The asset's expected return under $\mathbb{P}$ equals the risk-free rate. Investors demand no compensation beyond $r$ for holding this asset, meaning the risk premium is zero.

    This implies that investors are **risk-neutral** with respect to this asset---they are indifferent between the risky asset and a risk-free bond with the same expected return. In a world where all investors are truly risk-neutral (not just with respect to one asset, but universally), $\mathbb{Q} = \mathbb{P}$ for all traded assets, and the physical measure itself would satisfy the martingale property for discounted prices.

    The contrapositive is equally important: whenever $\mu \neq r$ (which is the empirically relevant case for equities), we have $\theta \neq 0$ and $\mathbb{Q} \neq \mathbb{P}$. The gap $\mu - r$ is the risk premium, and the fact that $\mathbb{Q} \neq \mathbb{P}$ is the mathematical signature of risk aversion. $\square$

---

**Exercise 6.**
A colleague claims: "Under $\mathbb{Q}$, all stocks earn the risk-free rate,
so a stock with $\mu = 0.15$ is overpriced relative to its $\mathbb{Q}$-return
of $r = 0.04$." Identify every error in this statement and explain the
correct interpretation of risk-neutral expected returns.

??? success "Solution to Exercise 6"
    The colleague's reasoning contains several fundamental errors.

    **Error 1: Confusing $\mathbb{Q}$-returns with valuation signals.** Under $\mathbb{Q}$, every traded asset has an expected return of $r$. This is a mathematical property of the risk-neutral measure by construction---it is not a signal of mispricing. If this logic were correct, *every* stock in the market would be "overpriced," which is absurd.

    **Error 2: Comparing $\mu$ against $r$ in the wrong framework.** The physical expected return $\mu = 0.15$ and the risk-neutral expected return $r = 0.04$ are computed under different measures. Comparing them directly is meaningless---they answer different questions. The quantity $\mu - r = 0.11$ is the risk premium: the compensation investors earn for bearing the stock's risk. It is a feature of the market, not evidence of mispricing.

    **Error 3: Treating $\mathbb{Q}$ as a belief or forecast.** The risk-neutral measure is not a prediction about future returns. It is a mathematical tool that reweights probabilities to enforce the martingale property. Saying the stock "earns only $r$ under $\mathbb{Q}$" is like saying a rotated coordinate system assigns different coordinates to the same point---it is a change of representation, not a change of reality.

    **Correct interpretation:** The fact that $\mu > r$ means investors require a positive risk premium to hold the stock, reflecting risk aversion. The measure change from $\mathbb{P}$ to $\mathbb{Q}$ removes this premium by downweighting favorable outcomes and upweighting unfavorable ones. The resulting $\mathbb{Q}$-expectation gives the correct no-arbitrage price, which is $S_0$---exactly the current market price. The stock is fairly priced by construction; the role of $\mathbb{Q}$ is to ensure pricing consistency, not to assess whether assets are cheap or expensive.
