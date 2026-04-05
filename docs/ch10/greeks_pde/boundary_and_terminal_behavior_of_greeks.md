# Boundary and Terminal Behavior of Greeks


Greeks exhibit characteristic behavior near \(S\to 0\), \(S\to\infty\), and \(t\uparrow T\). This matters for hedging and numerics.

---

## Far-field behavior (vanilla calls)


As \(S\to\infty\), a call behaves like

\[
V(t,S)\sim S - K e^{-r(T-t)},
\]


so

\[
\Delta(t,S)\to 1,
\qquad
\Gamma(t,S)\to 0.
\]

**Quantitative refinement.** More precisely, for large \(S\):

\[
\Delta = 1 - N(-d_1) = 1 - \mathcal{O}\!\left(e^{-d_1^2/2}\right)
\]

\[
\Gamma = \frac{N'(d_1)}{S\sigma\sqrt{\tau}} = \mathcal{O}\!\left(\frac{1}{S}e^{-d_1^2/2}\right)
\]

Since \(d_1 \sim \frac{\ln(S/K)}{\sigma\sqrt{\tau}}\) for large \(S\), the decay is faster than any polynomial.

As \(S\to 0\),

\[
V(t,S)\to 0,
\qquad \Delta(t,S)\to 0,
\qquad \Gamma(t,S)\to 0.
\]

**Quantitative refinement.** For small \(S\):

\[
\Delta = N(d_1) = \mathcal{O}\!\left(e^{-d_1^2/2}\right), \qquad d_1 \to -\infty
\]

\[
\Gamma = \mathcal{O}\!\left(\frac{1}{S}e^{-d_1^2/2}\right)
\]

---

## Near maturity: quantitative asymptotics


At maturity \(V(T,S)=\Phi(S)\). For payoffs with kinks, derivatives at \(T\) are not classical; gamma concentrates near the kink.

**ATM behavior as \(\tau \to 0\).** For \(S = K\) (at-the-money):

\[
\Delta_{\text{ATM}} = N(d_1) \to \frac{1}{2} + \mathcal{O}(\sqrt{\tau})
\]

\[
\Gamma_{\text{ATM}} = \frac{N'(0)}{K\sigma\sqrt{\tau}} = \frac{1}{K\sigma\sqrt{2\pi\tau}} \sim \tau^{-1/2}
\]

\[
\nu_{\text{ATM}} = K\sqrt{\tau}N'(0) = \frac{K\sqrt{\tau}}{\sqrt{2\pi}} \sim \sqrt{\tau}
\]

\[
\Theta_{\text{ATM}} \sim -\frac{K\sigma}{2\sqrt{2\pi\tau}} \sim -\tau^{-1/2}
\]

**Transition layer width.** The region where delta transitions from 0 to 1 has width

\[
\delta S \sim S \cdot \sigma\sqrt{\tau}
\]

in spot space, or equivalently \(\delta x \sim \sigma\sqrt{\tau}\) in log-moneyness \(x = \ln(S/K)\).

---

## OTM and ITM behavior near expiry


**Out-of-the-money call** (\(S < K\)): As \(\tau \to 0\),

\[
\Delta \to 0 \quad \text{exponentially fast: } \Delta \approx \exp\!\left(-\frac{(\ln(K/S))^2}{2\sigma^2\tau}\right)
\]

**In-the-money call** (\(S > K\)): As \(\tau \to 0\),

\[
\Delta \to 1 \quad \text{exponentially fast: } 1 - \Delta \approx \exp\!\left(-\frac{(\ln(S/K))^2}{2\sigma^2\tau}\right)
\]

---

## Numerical boundary conditions


For finite-difference PDE solvers:

| Boundary | Condition for Call |
|:---------|:-------------------|
| \(S = 0\) | \(V = 0\), \(\Delta = 0\), \(\Gamma = 0\) |
| \(S = S_{\max}\) | \(V \approx S - Ke^{-r\tau}\), \(\Delta \approx 1\), \(\Gamma \approx 0\) |
| \(t = T\) | \(V = (S-K)^+\), \(\Delta = \mathbf{1}_{S>K}\) (step), \(\Gamma = \delta(S-K)\) |

---

## What to remember


- Boundary conditions for PDE numerics are guided by far-field Greek limits.
- Near maturity, gamma spikes near the strike with \(\Gamma \sim \tau^{-1/2}\); delta becomes step-like.
- Transition layer has width \(\mathcal{O}(\sigma\sqrt{\tau})\) in log-moneyness.
- Far from the money, Greeks decay exponentially with rate $\sim 1/\tau$.

---

## Exercises

**Exercise 1.** For a European call as $S \to \infty$, the option behaves like $V \approx S - Ke^{-r\tau}$. Using this, verify that $\Delta \to 1$, $\Gamma \to 0$, and $\Theta \to -rKe^{-r\tau}$ in this limit. Interpret these results financially.

??? success "Solution to Exercise 1"
    As $S \to \infty$, the European call behaves like $V \approx S - Ke^{-r\tau}$, since the probability of finishing in-the-money approaches 1. Computing Greeks in this limit:

    **Delta:** Differentiating $V \approx S - Ke^{-r\tau}$ with respect to $S$:

    $$
    \Delta = \frac{\partial V}{\partial S} \to 1
    $$

    This means a deep ITM call moves dollar-for-dollar with the stock. The holder is virtually certain to exercise, so the option behaves like the stock minus a fixed payment.

    **Gamma:** Differentiating again:

    $$
    \Gamma = \frac{\partial^2 V}{\partial S^2} \to 0
    $$

    With delta locked at 1, there is no curvature in the price function. No rebalancing of the hedge is needed.

    **Theta:** From the PDE, $\Theta = -\frac{1}{2}\sigma^2 S^2 \Gamma - rS\Delta + rV$. Substituting $\Gamma \to 0$, $\Delta \to 1$, and $V \to S - Ke^{-r\tau}$:

    $$
    \Theta \to 0 - rS + r(S - Ke^{-r\tau}) = -rKe^{-r\tau}
    $$

    **Financial interpretation.** The theta converges to $-rKe^{-r\tau}$, which is negative. This represents the time value gained from the strike payment being discounted: as time passes, the present value $Ke^{-r\tau}$ of the strike increases (approaches $K$), reducing the option value. The deep ITM call has no optionality value left -- its only time dependence comes from the discounting of the strike. For $r > 0$, the option loses value over time at rate $rKe^{-r\tau}$.

---

**Exercise 2.** The ATM gamma diverges as $\Gamma_{\text{ATM}} \sim (K\sigma\sqrt{2\pi\tau})^{-1}$ when $\tau \to 0$. For $K = 100$ and $\sigma = 0.25$, compute the gamma values at $\tau = 30$, $7$, $1$, and $0.1$ trading days (use $\tau = \text{days}/252$). Plot or tabulate the results.

??? success "Solution to Exercise 2"
    The ATM gamma formula is $\Gamma_{\text{ATM}} = \frac{1}{K\sigma\sqrt{2\pi\tau}}$. With $K = 100$ and $\sigma = 0.25$:

    $$
    \Gamma_{\text{ATM}} = \frac{1}{100 \times 0.25 \times \sqrt{2\pi\tau}} = \frac{1}{25\sqrt{2\pi\tau}}
    $$

    Converting trading days to years using $\tau = \text{days}/252$:

    **30 trading days** ($\tau = 30/252 = 0.1190$):

    $$
    \Gamma = \frac{1}{25\sqrt{2\pi \times 0.1190}} = \frac{1}{25 \times 0.8649} = 0.0462
    $$

    **7 trading days** ($\tau = 7/252 = 0.02778$):

    $$
    \Gamma = \frac{1}{25\sqrt{2\pi \times 0.02778}} = \frac{1}{25 \times 0.4178} = 0.0957
    $$

    **1 trading day** ($\tau = 1/252 = 0.003968$):

    $$
    \Gamma = \frac{1}{25\sqrt{2\pi \times 0.003968}} = \frac{1}{25 \times 0.1579} = 0.2533
    $$

    **0.1 trading days** ($\tau = 0.1/252 = 0.0003968$):

    $$
    \Gamma = \frac{1}{25\sqrt{2\pi \times 0.0003968}} = \frac{1}{25 \times 0.04994} = 0.8010
    $$

    | Days to expiry | $\tau$ | $\Gamma_{\text{ATM}}$ |
    |:---|:---|:---|
    | 30 | 0.1190 | 0.046 |
    | 7 | 0.0278 | 0.096 |
    | 1 | 0.00397 | 0.253 |
    | 0.1 | 0.000397 | 0.801 |

    The $\tau^{-1/2}$ divergence is clearly visible: gamma roughly doubles each time $\tau$ decreases by a factor of 4. This explosive growth near expiry makes delta-hedging extremely costly for short-dated ATM options.

---

**Exercise 3.** The transition layer where delta moves from 0 to 1 has width $\delta S \sim S \cdot \sigma\sqrt{\tau}$ in spot space. For $S = K = 100$, $\sigma = 0.20$, compute the transition width for $\tau = 1$ year, $1$ month, and $1$ day. How does this affect a hedger's rebalancing requirements?

??? success "Solution to Exercise 3"
    The transition width in spot space is $\delta S \sim S\sigma\sqrt{\tau}$. With $S = K = 100$ and $\sigma = 0.20$:

    $$
    \delta S = 100 \times 0.20 \times \sqrt{\tau} = 20\sqrt{\tau}
    $$

    **1 year** ($\tau = 1$):

    $$
    \delta S = 20\sqrt{1} = 20
    $$

    Delta transitions from near 0 to near 1 over a range of roughly $\$80$ to $\$120$ (i.e., $\pm \$20$ around the strike). The hedge ratio changes gradually, and infrequent rebalancing suffices.

    **1 month** ($\tau = 1/12 = 0.0833$):

    $$
    \delta S = 20\sqrt{0.0833} = 20 \times 0.2887 = 5.77
    $$

    The transition zone narrows to roughly $\$94$ to $\$106$. A hedger must rebalance more frequently, since moderate price moves can cause significant changes in delta.

    **1 day** ($\tau = 1/252 = 0.003968$):

    $$
    \delta S = 20\sqrt{0.003968} = 20 \times 0.06299 = 1.26
    $$

    Delta transitions over just $\pm \$1.26$ around the strike. Even small price movements cause large delta swings, requiring near-continuous rebalancing.

    **Impact on hedging.** As the transition width shrinks with $\sqrt{\tau}$, the gamma (which scales as $1/\delta S$) increases correspondingly. A hedger must rebalance more frequently to track the rapidly changing delta. The rebalancing frequency scales as $1/(\delta S)^2 \sim 1/\tau$, meaning costs grow dramatically near expiry. In practice, this makes precise delta-hedging of short-dated ATM options prohibitively expensive, motivating wider hedging bands or the use of option spreads.

---

**Exercise 4.** For a deep OTM call with $S < K$, delta decays as $\Delta \approx \exp\left(-\frac{(\ln(K/S))^2}{2\sigma^2 \tau}\right)$ as $\tau \to 0$. Compute this exponential decay rate for $S = 95$, $K = 100$, $\sigma = 0.20$ at $\tau = 5$ days. At what point does delta become effectively zero (say, less than $10^{-6}$)?

??? success "Solution to Exercise 4"
    For a deep OTM call with $S < K$, the exponential decay rate is:

    $$
    \Delta \approx \exp\!\left(-\frac{(\ln(K/S))^2}{2\sigma^2\tau}\right)
    $$

    With $S = 95$, $K = 100$, $\sigma = 0.20$:

    $$
    \ln(K/S) = \ln(100/95) = \ln(1.0526) = 0.05129
    $$

    At $\tau = 5$ days $= 5/252 = 0.01984$ years:

    $$
    \frac{(\ln(K/S))^2}{2\sigma^2\tau} = \frac{(0.05129)^2}{2 \times (0.20)^2 \times 0.01984} = \frac{0.002631}{0.001587} = 1.658
    $$

    $$
    \Delta \approx e^{-1.658} = 0.190
    $$

    So delta is approximately 0.19 -- still meaningful.

    For delta to fall below $10^{-6}$, we need:

    $$
    \exp\!\left(-\frac{(\ln(K/S))^2}{2\sigma^2\tau}\right) < 10^{-6}
    $$

    $$
    \frac{(\ln(K/S))^2}{2\sigma^2\tau} > 6\ln(10) = 13.816
    $$

    $$
    \tau < \frac{(0.05129)^2}{2 \times 0.04 \times 13.816} = \frac{0.002631}{1.1053} = 0.002381 \text{ years}
    $$

    Converting: $0.002381 \times 252 = 0.600$ trading days, or approximately 14.4 trading hours. So a 5% OTM call becomes effectively zero-delta less than one trading day before expiry. This extremely rapid decay illustrates why OTM options near expiry have negligible delta exposure and essentially no hedging value.

---

**Exercise 5.** A finite-difference PDE solver requires boundary conditions at $S = 0$ and $S = S_{\max}$. For a European put, write down the analogous boundary conditions to those given for the call, including the values of $V$, $\Delta$, and $\Gamma$ at each boundary.

??? success "Solution to Exercise 5"
    For a European put with payoff $\Phi(S) = (K - S)^+$, the boundary conditions are:

    **At $S = 0$:** The put is deep in-the-money. The price approaches the discounted intrinsic value:

    $$
    V(t, 0) = Ke^{-r\tau}
    $$

    The delta is:

    $$
    \Delta(t, 0) = -1
    $$

    (put delta is $N(d_1) - 1 \to -1$ as $S \to 0$). The gamma is:

    $$
    \Gamma(t, 0) = 0
    $$

    (the price is asymptotically linear in $S$ at $S = 0$).

    **At $S = S_{\max}$:** The put is deep out-of-the-money. All values approach zero:

    $$
    V(t, S_{\max}) \approx 0, \qquad \Delta(t, S_{\max}) \approx 0, \qquad \Gamma(t, S_{\max}) \approx 0
    $$

    More precisely, $V = Ke^{-r\tau}N(-d_2) - SN(-d_1) \to 0$ exponentially as $S \to \infty$ since $N(-d_1), N(-d_2) \to 0$.

    **At $t = T$:** The terminal values are:

    $$
    V(T, S) = (K - S)^+, \qquad \Delta(T, S) = -\mathbf{1}_{S < K}, \qquad \Gamma(T, S) = \delta(S - K)
    $$

    Note that the terminal gamma is the same Dirac delta as for the call (same kink location, same second derivative).

    | Boundary | $V$ | $\Delta$ | $\Gamma$ |
    |:---|:---|:---|:---|
    | $S = 0$ | $Ke^{-r\tau}$ | $-1$ | $0$ |
    | $S = S_{\max}$ | $\approx 0$ | $\approx 0$ | $\approx 0$ |
    | $t = T$ | $(K-S)^+$ | $-\mathbf{1}_{S<K}$ (step) | $\delta(S-K)$ |

---

**Exercise 6.** Near maturity, the vega of an ATM option satisfies $\nu_{\text{ATM}} \sim K\sqrt{\tau}/\sqrt{2\pi}$, which vanishes as $\tau \to 0$. Explain why this is consistent with the fact that an option about to expire is insensitive to volatility. What does this imply about hedging vega risk for short-dated options?

??? success "Solution to Exercise 6"
    An option about to expire has its payoff nearly determined by the current spot price. If $\tau$ is very small, the stock price $S_T$ will be very close to $S_t$ regardless of $\sigma$, because the diffusion has almost no time to act: the standard deviation of $\ln(S_T/S_t)$ is $\sigma\sqrt{\tau}$, which vanishes as $\tau \to 0$.

    Quantitatively, for an ATM option:

    $$
    \nu_{\text{ATM}} = K\sqrt{\tau}\,N'(d_1) \approx \frac{K\sqrt{\tau}}{\sqrt{2\pi}} \to 0 \quad \text{as } \tau \to 0
    $$

    The vega vanishes because: (i) the option payoff depends on where $S_T$ ends up, (ii) as $\tau \to 0$, the distribution of $S_T$ collapses to a point mass at $S_t$ regardless of $\sigma$, so changing $\sigma$ has negligible effect on the expected payoff. The $\sqrt{\tau}$ rate of decay reflects the diffusion scaling -- the standard deviation of the stock's log-return is proportional to $\sqrt{\tau}$.

    **Implications for vega hedging.** For short-dated options, the small vega means:

    1. **Low vega exposure per option:** Each short-dated option contributes little vega to a portfolio. To achieve a given vega target, a trader needs many more short-dated options than long-dated ones.

    2. **Unstable vega hedge ratios:** While total vega is small, the vega per unit of gamma can be expressed as $\nu/\Gamma = \sigma S^2 \tau$, which also shrinks with $\tau$. This means that the "vega-to-gamma" ratio deteriorates, making it difficult to hedge vega without taking on excessive gamma.

    3. **Volatility uncertainty less relevant:** Since the option is nearly insensitive to $\sigma$, model risk from volatility misspecification is small for short-dated options. The dominant risk is gamma (spot movement), not vega (volatility movement).

    4. **Practical consequence:** Traders typically hedge vega using longer-dated options and manage gamma with short-dated options, exploiting the natural separation of risk horizons.
