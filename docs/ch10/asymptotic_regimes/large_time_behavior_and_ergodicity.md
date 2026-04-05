# Large-Time Behavior and Ergodicity


Large-time limits depend on whether the model admits a stationary distribution. The behavior of option prices and Greeks as \(T \to \infty\) differs fundamentally between ergodic and non-ergodic models.

---

## Non-ergodic Black–Scholes


Geometric Brownian motion has no stationary distribution in \(S\). Under the risk-neutral measure,

\[
S_T = S_0 \exp\!\left[\left(r - \frac{\sigma^2}{2}\right)T + \sigma W_T\right]
\]

As \(T \to \infty\):

- \(\log S_T\) has variance \(\sigma^2 T \to \infty\), so the distribution of \(S_T\) spreads without bound.
- The call price grows like \(S_0\) (bounded below by intrinsic value) while the put price converges to \(Ke^{-rT} \to 0\).

More precisely, for a European call:

\[
C(S_0, K, T) \to S_0 \quad \text{as } T \to \infty
\]

since \(N(d_1) \to 1\) and \(Ke^{-rT}N(d_2) \to 0\).

---

## Large-time behavior of Greeks in Black–Scholes


As \(T \to \infty\) (equivalently \(\tau \to \infty\)):

\[
\Delta_{\text{call}} = N(d_1) \to 1, \quad \Gamma \to 0, \quad \nu \to 0
\]

The option behaves increasingly like the underlying itself. This is intuitive: with enough time, any OTM call becomes ATM in expectation, and the option's optionality premium vanishes relative to the forward price.

For theta:

\[
\Theta_{\text{call}} \to rKe^{-rT}N(d_2) \to 0
\]

So time decay vanishes for very long-dated options — they are dominated by their delta exposure.

---

## Ergodic factors in multi-factor models


In multi-factor models, mean-reverting factors (e.g., variance in Heston-type models) may be ergodic with invariant measure \(\pi\). For a CIR-type variance process \(v_t\) satisfying

\[
dv_t = \kappa(\bar{v} - v_t)\,dt + \xi\sqrt{v_t}\,dW_t
\]

the process is ergodic when the Feller condition \(2\kappa\bar{v} > \xi^2\) holds, and for suitable functions \(f\):

\[
\frac{1}{T}\int_0^T f(v_s)\,\mathrm{d}s \xrightarrow{a.s.} \int f\,\mathrm{d}\pi
\]

where \(\pi\) is the Gamma distribution with shape \(\alpha = 2\kappa\bar{v}/\xi^2\) and rate \(\beta = 2\kappa/\xi^2\).

---

## Implications for long-dated option pricing


In stochastic volatility models with ergodic variance:

**Effective volatility convergence.** The time-averaged variance converges to the long-run mean:

\[
\frac{1}{T}\int_0^T v_s\,ds \xrightarrow{a.s.} \bar{v} \quad \text{as } T \to \infty
\]

This suggests that long-dated options are approximately priced by Black–Scholes with \(\sigma = \sqrt{\bar{v}}\), plus corrections that decay with maturity.

**Implied volatility term structure.** As \(T \to \infty\), implied volatility for ATM options converges to

\[
\sigma_{\text{implied}}(T) \to \sqrt{\bar{v}} + \mathcal{O}(T^{-1})
\]

The rate of convergence depends on the speed of mean reversion \(\kappa\).

---

## Large deviations and tail behavior


For non-ergodic components (like \(\log S\) itself), large-time behavior is governed by **large deviations theory**. The probability that the log-return deviates from its drift satisfies

\[
\mathbb{P}\!\left(\frac{\log(S_T/S_0)}{T} \notin [a,b]\right) \sim e^{-T \cdot I}
\]

where \(I\) is a rate function determined by the model. In Black–Scholes:

\[
I(x) = \frac{(x - \mu)^2}{2\sigma^2}
\]

with \(\mu = r - \sigma^2/2\) under the risk-neutral measure. This connects to the exponential decay of deep OTM option prices at long maturities.

---

## Practical relevance


Long-time asymptotics matter for:

- **LEAPS and long-dated warrants**: pricing and hedging options with maturities of several years.
- **Insurance-linked products**: equity-indexed annuities and variable annuity guarantees often have 10–30 year horizons.
- **Model calibration**: the long end of the implied volatility term structure constrains the ergodic properties of the variance process.
- **Risk management**: long-horizon VaR and expected shortfall calculations depend on whether variance factors are mean-reverting.

---

## What to remember


- Black–Scholes is not ergodic in \(S\); long-horizon option prices are dominated by drift and the option degenerates toward the underlying.
- Mean-reverting factors (e.g., stochastic variance) can be ergodic, and their long-run averages determine the effective volatility for long-dated options.
- Long-time asymptotics are model-dependent and linked to large deviations or ergodicity of latent factors.
- The rate of convergence to ergodic limits is governed by the mean-reversion speed.

---

## Exercises

**Exercise 1.** For a European call in Black--Scholes, show that $C(S_0, K, T) \to S_0$ as $T \to \infty$ by verifying that $N(d_1) \to 1$ and $Ke^{-rT}N(d_2) \to 0$. What is the economic interpretation of this limit?

??? success "Solution to Exercise 1"
    In Black--Scholes, $C = S_0 N(d_1) - Ke^{-rT}N(d_2)$ where

    $$
    d_1 = \frac{\ln(S_0/K) + (r + \frac{1}{2}\sigma^2)T}{\sigma\sqrt{T}}, \quad d_2 = d_1 - \sigma\sqrt{T}
    $$

    **Step 1: Show $d_1 \to +\infty$.** For fixed $S_0, K, r, \sigma > 0$:

    $$
    d_1 = \frac{\ln(S_0/K)}{\sigma\sqrt{T}} + \frac{(r + \frac{1}{2}\sigma^2)\sqrt{T}}{\sigma}
    $$

    The first term is $\mathcal{O}(T^{-1/2}) \to 0$ and the second grows as $\sqrt{T} \to +\infty$. Therefore $d_1 \to +\infty$, so $N(d_1) \to 1$.

    **Step 2: Show $Ke^{-rT}N(d_2) \to 0$.** We have $d_2 = d_1 - \sigma\sqrt{T}$. Similarly:

    $$
    d_2 = \frac{\ln(S_0/K)}{\sigma\sqrt{T}} + \frac{(r - \frac{1}{2}\sigma^2)\sqrt{T}}{\sigma}
    $$

    If $r > \sigma^2/2$, then $d_2 \to +\infty$ and $N(d_2) \to 1$, but $Ke^{-rT} \to 0$, so the product vanishes.

    If $r < \sigma^2/2$, then $d_2 \to -\infty$, so $N(d_2) \to 0$, and $Ke^{-rT}N(d_2) \to 0$.

    If $r = \sigma^2/2$, then $d_2 \to 0$, $N(d_2) \to 1/2$, but $Ke^{-rT} \to 0$ still dominates.

    In all cases, $Ke^{-rT}N(d_2) \to 0$.

    **Conclusion:** $C \to S_0 \times 1 - 0 = S_0$.

    **Economic interpretation.** With infinite time, the forward price $S_0 e^{rT} \to \infty$, so any finite strike $K$ becomes deeply in the money. The discounted strike $Ke^{-rT}$ vanishes, so paying $K$ at expiry costs nothing in present-value terms. The call effectively becomes the stock itself --- you are certain to exercise, and the present value of the strike payment is zero.

---

**Exercise 2.** In the CIR variance process $dv_t = \kappa(\bar{v} - v_t)\,dt + \xi\sqrt{v_t}\,dW_t$, the stationary distribution is Gamma with shape $\alpha = 2\kappa\bar{v}/\xi^2$ and rate $\beta = 2\kappa/\xi^2$. For $\kappa = 2$, $\bar{v} = 0.04$, $\xi = 0.3$, compute $\alpha$ and $\beta$ and verify that the Feller condition $2\kappa\bar{v} > \xi^2$ is satisfied.

??? success "Solution to Exercise 2"
    With $\kappa = 2$, $\bar{v} = 0.04$, $\xi = 0.3$:

    $$
    \alpha = \frac{2\kappa\bar{v}}{\xi^2} = \frac{2 \times 2 \times 0.04}{0.09} = \frac{0.16}{0.09} = 1.778
    $$

    $$
    \beta = \frac{2\kappa}{\xi^2} = \frac{2 \times 2}{0.09} = \frac{4}{0.09} = 44.44
    $$

    **Feller condition:** $2\kappa\bar{v} = 0.16$ and $\xi^2 = 0.09$, so $2\kappa\bar{v} = 0.16 > 0.09 = \xi^2$. The Feller condition is satisfied.

    **Verification.** The stationary Gamma distribution has mean $\alpha/\beta = 1.778/44.44 = 0.04 = \bar{v}$ and variance $\alpha/\beta^2 = 1.778/1975 = 0.0009$, giving a standard deviation of $0.03$. Since the mean is $0.04$ and the standard deviation is $0.03$, the coefficient of variation is $0.75$, indicating significant variance fluctuation around the long-run mean.

    The Feller condition ensures $v_t > 0$ almost surely, which is necessary for the process to be well-defined and ergodic.

---

**Exercise 3.** The implied volatility for long-dated ATM options converges to $\sqrt{\bar{v}}$ with corrections of order $T^{-1}$. For the parameters in Exercise 2, compute $\sqrt{\bar{v}}$ and explain why the speed of convergence depends on $\kappa$. What happens to the implied vol term structure when $\kappa$ is very small?

??? success "Solution to Exercise 3"
    From Exercise 2, $\bar{v} = 0.04$, so

    $$
    \sqrt{\bar{v}} = \sqrt{0.04} = 0.20
    $$

    This is the long-run implied volatility: as $T \to \infty$, ATM implied vol converges to $20\%$.

    **Dependence on $\kappa$.** The implied volatility term structure satisfies

    $$
    \sigma_{\text{implied}}(T) \approx \sqrt{\bar{v}} + \frac{c(v_0 - \bar{v})}{\kappa T} + \mathcal{O}(T^{-2})
    $$

    where $c$ is a constant and $v_0$ is the initial variance. The correction decays as $1/(\kappa T)$, so:

    - **Large $\kappa$:** Fast mean reversion. The variance quickly reaches its stationary distribution, and implied vol converges to $\sqrt{\bar{v}}$ at shorter maturities. The term structure flattens quickly.
    - **Small $\kappa$:** Slow mean reversion. The current variance $v_0$ influences pricing for a long time. If $v_0 \neq \bar{v}$, the term structure takes a long time to flatten.

    **When $\kappa$ is very small:** The variance process is nearly a martingale (very slow reversion). The time-averaged variance $\frac{1}{T}\int_0^T v_s\,ds$ converges extremely slowly to $\bar{v}$. The implied vol term structure shows a strong slope: if $v_0 < \bar{v}$, the term structure is upward-sloping (higher vol for longer maturities), and vice versa. In the extreme case $\kappa \to 0$, ergodicity is lost and the term structure never flattens --- it depends on $v_0$ at all horizons.

---

**Exercise 4.** For a European put in Black--Scholes, show that $P(S_0, K, T) \to 0$ as $T \to \infty$. Explain why the put price vanishes but the call price does not, and relate this to the asymmetry of the payoff functions.

??? success "Solution to Exercise 4"
    The put price is $P = Ke^{-rT}N(-d_2) - S_0 N(-d_1)$.

    From Exercise 1, $d_1 \to +\infty$ as $T \to \infty$, so $N(-d_1) \to 0$, giving $S_0 N(-d_1) \to 0$.

    For the first term, regardless of the behavior of $N(-d_2)$ (which is bounded between 0 and 1):

    $$
    0 \leq Ke^{-rT}N(-d_2) \leq Ke^{-rT} \to 0 \quad \text{as } T \to \infty
    $$

    Therefore $P \to 0 - 0 = 0$.

    **Why call and put behave differently.** The asymmetry comes from the payoff structure and discounting:

    - **Call payoff** $(S_T - K)^+$: The upside is unbounded. As $T \to \infty$, $\mathbb{E}[S_T] = S_0 e^{rT} \to \infty$, so the expected payoff grows without bound. Discounting at rate $r$ exactly offsets the forward growth, leaving $C \to S_0$.
    - **Put payoff** $(K - S_T)^+$: The upside is bounded by $K$. As $T \to \infty$, the probability $\mathbb{P}(S_T < K)$ does not vanish (in fact, $\mathbb{P}(S_T < K) \to 1$ under the real-world measure if $\mu < \sigma^2/2$), but the present value of receiving at most $K$ in the far future is $Ke^{-rT} \to 0$.

    Alternatively, put-call parity gives $P = C - S_0 + Ke^{-rT} \to S_0 - S_0 + 0 = 0$, consistent with the direct calculation.

---

**Exercise 5.** The large deviations rate function in Black--Scholes is $I(x) = (x - \mu)^2/(2\sigma^2)$ with $\mu = r - \sigma^2/2$. For $r = 0.05$, $\sigma = 0.20$, compute $I(x)$ at $x = 0$ (no growth), $x = \mu$ (drift), and $x = 2\mu$ (double the drift). Which deviation costs the most probability?

??? success "Solution to Exercise 5"
    The rate function is $I(x) = \frac{(x - \mu)^2}{2\sigma^2}$ with $\mu = r - \sigma^2/2 = 0.05 - 0.02 = 0.03$ and $\sigma = 0.20$.

    **At $x = 0$ (no growth):**

    $$
    I(0) = \frac{(0 - 0.03)^2}{2 \times 0.04} = \frac{0.0009}{0.08} = 0.01125
    $$

    **At $x = \mu = 0.03$ (drift):**

    $$
    I(0.03) = \frac{(0.03 - 0.03)^2}{0.08} = 0
    $$

    **At $x = 2\mu = 0.06$ (double the drift):**

    $$
    I(0.06) = \frac{(0.06 - 0.03)^2}{0.08} = \frac{0.0009}{0.08} = 0.01125
    $$

    The deviation $x = \mu$ costs zero --- this is the most likely growth rate (mode of the large deviations principle). Both $x = 0$ and $x = 2\mu$ deviate equally from $\mu$ and incur the same cost $I = 0.01125$.

    The probability of observing annualized log-return $x$ over horizon $T$ decays as $\exp(-TI(x))$. For $T = 20$ years and $x = 0$:

    $$
    \mathbb{P}\!\left(\frac{\log(S_T/S_0)}{T} \approx 0\right) \sim e^{-20 \times 0.01125} = e^{-0.225} \approx 0.80
    $$

    This shows that even over long horizons, the Gaussian rate function is not very penalizing for moderate deviations. The cost $I(x) = 0.01125$ is small because the drift is small relative to $\sigma^2$. The deviation that "costs the most" among the three is a tie between $x = 0$ and $x = 2\mu$, both with $I = 0.01125$.

---

**Exercise 6.** A pension fund holds equity-linked guarantees with a 20-year horizon. Using the large-time asymptotics framework, explain why the choice between a stochastic volatility model (with ergodic variance) and a constant-volatility Black--Scholes model matters significantly for pricing these guarantees. Which model features are most important to calibrate for long-dated products?

??? success "Solution to Exercise 6"
    **Why model choice matters for long-dated guarantees:**

    In a constant-volatility Black--Scholes model, the total variance over $T = 20$ years is $\sigma^2 T = 0.04 \times 20 = 0.80$ (using $\sigma = 0.20$). This is deterministic, so the distribution of terminal wealth is exactly log-normal.

    In a stochastic volatility model with ergodic variance (e.g., Heston), the total integrated variance $\int_0^T v_s\,ds$ is random. By ergodicity, $\frac{1}{T}\int_0^T v_s\,ds \to \bar{v}$ a.s., so the average variance is approximately $\bar{v}$. However:

    1. **Variance of integrated variance.** Even though the average converges, the fluctuation around $\bar{v}$ over 20 years is not negligible. The variance of $\frac{1}{T}\int_0^T v_s\,ds$ decays as $\mathcal{O}(1/(\kappa T))$, so slow mean reversion ($\kappa$ small) keeps uncertainty high.

    2. **Fat tails in returns.** Random variance creates a mixture of Gaussians, producing heavier tails than log-normal. For guarantees that pay in tail scenarios (e.g., minimum return guarantees), this dramatically affects pricing.

    3. **Volatility-of-volatility risk.** The parameter $\xi$ (vol-of-vol) determines how much the integrated variance can deviate from $\bar{v}T$, directly affecting guarantee costs.

    4. **Correlation effects.** In stochastic vol models, correlation between spot and variance ($\rho < 0$ typically) creates skewness in the return distribution, making downside guarantees more expensive than a symmetric model would suggest.

    **Most important features to calibrate:**

    - **Long-run variance $\bar{v}$:** Determines the baseline volatility level for the guarantee horizon.
    - **Mean reversion speed $\kappa$:** Controls how quickly the term structure flattens; slow reversion means current conditions persist and the model departs significantly from Black--Scholes.
    - **Vol-of-vol $\xi$:** Drives the fatness of tails and the cost of tail guarantees; underfitting $\xi$ can severely underprice guarantees.
    - **Spot-vol correlation $\rho$:** Affects skewness of long-horizon returns; critical for directional guarantees (e.g., minimum return floors).
    - **Feller condition ($2\kappa\bar{v} > \xi^2$):** Must be verified to ensure the model is well-behaved and truly ergodic over the guarantee horizon.
