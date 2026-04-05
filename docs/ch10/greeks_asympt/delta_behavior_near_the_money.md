# Delta Behavior Near the Money


As \(\tau\downarrow 0\), delta approaches a step function across the strike. This transition from smooth sensitivity to discontinuous payoff creates severe hedging challenges in the final hours before expiry.

---

## Boundary layer


For a European call, \(\Delta = N(d_1)\) where

\[
d_1 = \frac{\ln(S/K) + (r + \frac{1}{2}\sigma^2)\tau}{\sigma\sqrt{\tau}}
\]

As \(\tau \to 0\):

- \(S > K \Rightarrow d_1 \to +\infty \Rightarrow \Delta \to 1\)
- \(S < K \Rightarrow d_1 \to -\infty \Rightarrow \Delta \to 0\)
- \(S = K \Rightarrow d_1 \to (r + \frac{1}{2}\sigma^2)\sqrt{\tau}/\sigma \to 0 \Rightarrow \Delta \to \frac{1}{2}\)

The transition from 0 to 1 occurs in a narrow region around \(S = K\) whose width shrinks with \(\tau\).

---

## Width of transition


In log-moneyness \(x = \ln(S/K)\), the dominant term in \(d_1\) is

\[
d_1 \approx \frac{x}{\sigma\sqrt{\tau}} + \mathcal{O}(\sqrt{\tau})
\]

The transition from \(\Delta \approx 0\) to \(\Delta \approx 1\) occurs when \(|d_1| \lesssim 2\), i.e., when

\[
|x| \lesssim 2\sigma\sqrt{\tau}
\]

In terms of spot price, the transition width is approximately

\[
\Delta S \approx K \cdot 2\sigma\sqrt{\tau}
\]

For example, with \(K = 100\), \(\sigma = 0.20\), and \(\tau = 1/252\) (one trading day):

\[
\Delta S \approx 100 \times 2 \times 0.20 \times \sqrt{1/252} \approx 2.52
\]

So delta transitions from 0 to 1 over roughly a \$2.50 band around the strike.

---

## Connection to gamma blow-up


The steepness of the delta transition is directly related to gamma. Since \(\Gamma = \partial\Delta/\partial S\), the fact that delta transitions from 0 to 1 over a width \(\sim \sigma\sqrt{\tau}\) implies

\[
\Gamma_{\text{peak}} \sim \frac{1}{S\sigma\sqrt{\tau}}
\]

which diverges as \(\tau \to 0\). The delta step function in the limit has a Dirac-delta derivative, reflecting infinite gamma at expiry for ATM options (see *Blow-Up of Gamma Near Expiry*).

---

## Exact asymptotic expansion


For \(\tau\) small and \(x = \ln(S/K)\) of order \(\sigma\sqrt{\tau}\), write \(x = \sigma\sqrt{\tau}\,z\) for \(z = \mathcal{O}(1)\). Then

\[
\Delta = N\!\left(z + \frac{(r + \frac{1}{2}\sigma^2)\sqrt{\tau}}{\sigma}\right) = N(z) + \mathcal{O}(\sqrt{\tau})
\]

This shows that in the **inner region** near the strike, delta is approximately the normal CDF evaluated at the rescaled log-moneyness \(z = x/(\sigma\sqrt{\tau})\). The function transitions smoothly through this inner layer but appears step-like on the scale of \(x\) itself.

---

## Put delta near the money


For a European put, \(\Delta_{\text{put}} = N(d_1) - 1\), so:

- \(S > K \Rightarrow \Delta_{\text{put}} \to 0\)
- \(S < K \Rightarrow \Delta_{\text{put}} \to -1\)
- \(S = K \Rightarrow \Delta_{\text{put}} \to -\frac{1}{2}\)

The transition has the same width \(\sim \sigma\sqrt{\tau}\) and the same gamma profile, consistent with put-call parity: \(\Delta_{\text{call}} - \Delta_{\text{put}} = 1\).

---

## Hedging implications


The near-expiry delta behavior creates several practical challenges:

**Pin risk.** When the underlying is near the strike at expiry, the option writer faces uncertainty about whether the option will be exercised. Delta oscillates between 0 and 1 with small price moves, requiring massive hedge adjustments.

**Rebalancing frequency.** As delta changes rapidly (high gamma), the hedger must rebalance more frequently to maintain a delta-neutral position. Transaction costs from frequent rebalancing can exceed the option premium collected.

**Discrete hedging error.** With rebalancing interval \(\Delta t\), the expected squared hedging error scales as \(\Gamma^2 S^4 \sigma^2 \Delta t\). Near expiry with \(\Gamma \sim 1/(S\sigma\sqrt{\tau})\), this becomes \(\sim S^2 \sigma / \tau \cdot \Delta t\), which grows as \(\tau \to 0\).

**Practical response.** Traders managing near-expiry ATM options typically either close positions before expiry, accept the pin risk as a cost of doing business, or hedge with other options rather than the underlying alone.

---

## Digital option limit


In the limit \(\tau \to 0\), the call delta formally approaches

\[
\Delta \to \mathbf{1}_{S > K}
\]

This is exactly the payoff of a **digital (binary) call** option. The connection is not coincidental: the digital call price \(e^{-r\tau}N(d_2)\) has delta that also concentrates near the strike, and the standard call delta \(N(d_1)\) and digital call price \(N(d_2)\) converge to the same step function as \(\tau \to 0\).

---

## What to remember


- Delta becomes step-like near maturity, with the transition layer shrinking like \(\sigma\sqrt{\tau}\) in log-moneyness.
- The steepness of the transition is the flip side of gamma blow-up.
- Near-expiry ATM options create pin risk and hedging difficulties that are fundamental, not merely practical inconveniences.
- The inner-layer scaling $x = \sigma\sqrt{\tau}\,z$ provides a unified asymptotic description of all near-expiry Greeks.

---

## Exercises

**Exercise 1.** For $S = 100$, $K = 100$, $\sigma = 0.30$, compute the transition width $\Delta S \approx K \cdot 2\sigma\sqrt{\tau}$ at $\tau = 5$ days, $1$ day, and $2$ hours ($\tau$ in years). Over how many dollars does delta transition from near-zero to near-one in each case?

??? success "Solution to Exercise 1"
    We use the formula $\Delta S \approx K \cdot 2\sigma\sqrt{\tau}$ with $K = 100$ and $\sigma = 0.30$.

    **Case 1: $\tau = 5$ days.** Converting to years: $\tau = 5/252 \approx 0.01984$.

    $$
    \Delta S \approx 100 \times 2 \times 0.30 \times \sqrt{5/252} \approx 60 \times 0.1409 \approx 8.45
    $$

    Delta transitions from near-zero to near-one over roughly $\$8.45$.

    **Case 2: $\tau = 1$ day.** $\tau = 1/252 \approx 0.003968$.

    $$
    \Delta S \approx 100 \times 2 \times 0.30 \times \sqrt{1/252} \approx 60 \times 0.06300 \approx 3.78
    $$

    The transition band is roughly $\$3.78$.

    **Case 3: $\tau = 2$ hours.** There are approximately $6.5$ trading hours per day, so $\tau = 2/(252 \times 6.5) \approx 0.001221$.

    $$
    \Delta S \approx 100 \times 2 \times 0.30 \times \sqrt{2/1638} \approx 60 \times 0.03495 \approx 2.10
    $$

    The transition band is roughly $\$2.10$.

    The transition width shrinks as $\sqrt{\tau}$: as maturity approaches, delta becomes increasingly step-like. The ratio of widths confirms the scaling: $8.45 / 3.78 \approx 2.24 \approx \sqrt{5}$, consistent with the $\sqrt{\tau}$ dependence.

---

**Exercise 2.** In the inner-region scaling $x = \sigma\sqrt{\tau}\,z$ where $x = \ln(S/K)$, show that $\Delta \approx N(z) + \mathcal{O}(\sqrt{\tau})$. At what value of $z$ does $\Delta = 0.9$? Convert this back to a spot price $S$ for $K = 100$, $\sigma = 0.20$, $\tau = 1$ day.

??? success "Solution to Exercise 2"
    Starting from $d_1 = \frac{\ln(S/K) + (r + \frac{1}{2}\sigma^2)\tau}{\sigma\sqrt{\tau}}$ and substituting $x = \ln(S/K) = \sigma\sqrt{\tau}\,z$:

    $$
    d_1 = \frac{\sigma\sqrt{\tau}\,z + (r + \frac{1}{2}\sigma^2)\tau}{\sigma\sqrt{\tau}} = z + \frac{(r + \frac{1}{2}\sigma^2)\sqrt{\tau}}{\sigma}
    $$

    The second term is $\mathcal{O}(\sqrt{\tau})$, so $d_1 = z + \mathcal{O}(\sqrt{\tau})$. Since $N$ is Lipschitz (with $|N'| \leq 1/\sqrt{2\pi}$):

    $$
    \Delta = N(d_1) = N(z + \mathcal{O}(\sqrt{\tau})) = N(z) + \mathcal{O}(\sqrt{\tau})
    $$

    For $\Delta = 0.9$, we need $N(z) = 0.9$, which gives $z = N^{-1}(0.9) \approx 1.2816$.

    Converting back to spot price with $K = 100$, $\sigma = 0.20$, $\tau = 1/252$:

    $$
    x = \sigma\sqrt{\tau}\,z = 0.20 \times \sqrt{1/252} \times 1.2816 \approx 0.20 \times 0.06300 \times 1.2816 \approx 0.01615
    $$

    Since $x = \ln(S/K)$, we get $S = K e^x = 100 \times e^{0.01615} \approx 101.63$.

    So delta reaches $0.9$ when $S$ is only about $\$1.63$ above the strike, illustrating the narrow transition band near expiry.

---

**Exercise 3.** Explain the concept of "pin risk" for an option seller when $S \approx K$ at expiry. If a trader is short 1000 call contracts (each on 100 shares) with strike $K = 50$ and $S = 50.10$ at expiry, how many shares must be delivered? What happens if $S$ drops to $49.90$ in the last minute of trading?

??? success "Solution to Exercise 3"
    **Pin risk** arises when the underlying price is very close to the strike at expiry. The option writer does not know whether the option will expire in or out of the money, making it uncertain how many shares will need to be delivered.

    **Scenario with $S = 50.10$:** All 1000 call contracts expire in the money. Each contract covers 100 shares, so the trader must deliver $1000 \times 100 = 100{,}000$ shares at $K = 50$.

    **If $S$ drops to $49.90$:** All 1000 contracts expire out of the money and are not exercised. The trader delivers zero shares.

    A $\$0.20$ move (only $0.4\%$ of the stock price) in the final minutes flips the position from delivering $100{,}000$ shares to delivering none. This means the trader's delta swings from approximately $-100{,}000$ to $0$, a massive change from a tiny price move. This is the essence of pin risk: near expiry, when $S \approx K$, the option writer faces binary exposure that cannot be smoothly hedged. In practice, traders manage this by closing or rolling positions before expiry or by accepting the pin risk as a cost of the strategy.

---

**Exercise 4.** The connection between call delta and digital call price states that both converge to $\mathbf{1}_{S > K}$ as $\tau \to 0$. For finite $\tau$, the call delta is $N(d_1)$ while the digital call price is $e^{-r\tau}N(d_2)$. Show that the difference $N(d_1) - e^{-r\tau}N(d_2) \to 0$ as $\tau \to 0$ at the money.

??? success "Solution to Exercise 4"
    At the money ($S = K$), we have $\ln(S/K) = 0$, so:

    $$
    d_1 = \frac{(r + \frac{1}{2}\sigma^2)\tau}{\sigma\sqrt{\tau}} = \frac{(r + \frac{1}{2}\sigma^2)\sqrt{\tau}}{\sigma}
    $$

    $$
    d_2 = d_1 - \sigma\sqrt{\tau} = \frac{(r - \frac{1}{2}\sigma^2)\sqrt{\tau}}{\sigma}
    $$

    As $\tau \to 0$, both $d_1 \to 0$ and $d_2 \to 0$, so $N(d_1) \to N(0) = \frac{1}{2}$ and $N(d_2) \to \frac{1}{2}$.

    Now consider the difference:

    $$
    N(d_1) - e^{-r\tau}N(d_2) = N(d_1) - N(d_2) + N(d_2)(1 - e^{-r\tau})
    $$

    For the first term, by the mean value theorem:

    $$
    N(d_1) - N(d_2) = N'(\xi)(d_1 - d_2) = N'(\xi)\sigma\sqrt{\tau}
    $$

    for some $\xi$ between $d_1$ and $d_2$. Since $N'(\xi) \leq 1/\sqrt{2\pi}$, this term is $\mathcal{O}(\sqrt{\tau}) \to 0$.

    For the second term, $N(d_2) \to \frac{1}{2}$ and $1 - e^{-r\tau} = r\tau + \mathcal{O}(\tau^2)$, so:

    $$
    N(d_2)(1 - e^{-r\tau}) = \frac{1}{2}r\tau + \mathcal{O}(\tau^{3/2}) \to 0
    $$

    Therefore $N(d_1) - e^{-r\tau}N(d_2) \to 0$ as $\tau \to 0$ at the money, confirming that call delta and digital call price converge to the same step function.

---

**Exercise 5.** A trader is delta-hedging a short ATM call with 1 day to expiry. The discrete hedging error per step is approximately $\frac{1}{2}\Gamma(\Delta S)^2$. Using $\Gamma \sim 1/(S\sigma\sqrt{2\pi\tau})$, estimate the hedging error from a single $1\%$ move in $S$ when $S = 100$, $\sigma = 0.20$, $\tau = 1/252$.

??? success "Solution to Exercise 5"
    Using $\Gamma \sim \frac{1}{S\sigma\sqrt{2\pi\tau}}$ with $S = 100$, $\sigma = 0.20$, and $\tau = 1/252$:

    $$
    \Gamma \approx \frac{1}{100 \times 0.20 \times \sqrt{2\pi \times 1/252}} = \frac{1}{20 \times \sqrt{0.02494}} = \frac{1}{20 \times 0.15794} \approx \frac{1}{3.159} \approx 0.3166
    $$

    A $1\%$ move in $S$ means $\Delta S = 1.00$.

    The hedging error per step is:

    $$
    \text{Error} \approx \frac{1}{2}\Gamma(\Delta S)^2 = \frac{1}{2} \times 0.3166 \times (1.00)^2 \approx 0.1583
    $$

    This is approximately $\$0.16$ per option. For context, the ATM option with 1 day to expiry has a price of approximately:

    $$
    C_{\text{ATM}} \approx \frac{S\sigma\sqrt{\tau}}{\sqrt{2\pi}} = \frac{100 \times 0.20 \times \sqrt{1/252}}{\sqrt{2\pi}} \approx \frac{1.260}{2.507} \approx 0.502
    $$

    So a single $1\%$ move creates a hedging error that is about $31\%$ of the option's value, illustrating why discrete hedging is extremely challenging for near-expiry ATM options.

---

**Exercise 6.** For a European put, delta transitions from $-1$ to $0$ as $S$ increases through $K$, with the same transition width $\sim \sigma\sqrt{\tau}$. Using put-call parity, verify that $\Delta_{\text{call}} - \Delta_{\text{put}} = 1$ for all $\tau > 0$, and explain why both deltas have the same gamma profile.

??? success "Solution to Exercise 6"
    **Verifying $\Delta_{\text{call}} - \Delta_{\text{put}} = 1$:**

    Put-call parity states $C - P = S - Ke^{-r\tau}$ for all $\tau > 0$. Differentiating both sides with respect to $S$:

    $$
    \frac{\partial C}{\partial S} - \frac{\partial P}{\partial S} = 1
    $$

    $$
    \Delta_{\text{call}} - \Delta_{\text{put}} = 1
    $$

    This holds for all $\tau > 0$ and all $S$, not just near-the-money. The result follows directly because $Ke^{-r\tau}$ is independent of $S$.

    **Same gamma profile:** Differentiating the identity $\Delta_{\text{call}} - \Delta_{\text{put}} = 1$ with respect to $S$:

    $$
    \Gamma_{\text{call}} - \Gamma_{\text{put}} = 0
    $$

    So $\Gamma_{\text{call}} = \Gamma_{\text{put}}$ for all $S$ and $\tau$. This means calls and puts with the same strike and maturity have identical gamma profiles. Intuitively, gamma measures the curvature of the option price as a function of $S$, and since call and put prices differ by the linear function $S - Ke^{-r\tau}$, their second derivatives are identical. Consequently, the transition width $\sim \sigma\sqrt{\tau}$ and the peak gamma $\sim 1/(S\sigma\sqrt{\tau})$ are the same for both.
