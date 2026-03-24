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

---

**Exercise 2.** In the inner-region scaling $x = \sigma\sqrt{\tau}\,z$ where $x = \ln(S/K)$, show that $\Delta \approx N(z) + \mathcal{O}(\sqrt{\tau})$. At what value of $z$ does $\Delta = 0.9$? Convert this back to a spot price $S$ for $K = 100$, $\sigma = 0.20$, $\tau = 1$ day.

---

**Exercise 3.** Explain the concept of "pin risk" for an option seller when $S \approx K$ at expiry. If a trader is short 1000 call contracts (each on 100 shares) with strike $K = 50$ and $S = 50.10$ at expiry, how many shares must be delivered? What happens if $S$ drops to $49.90$ in the last minute of trading?

---

**Exercise 4.** The connection between call delta and digital call price states that both converge to $\mathbf{1}_{S > K}$ as $\tau \to 0$. For finite $\tau$, the call delta is $N(d_1)$ while the digital call price is $e^{-r\tau}N(d_2)$. Show that the difference $N(d_1) - e^{-r\tau}N(d_2) \to 0$ as $\tau \to 0$ at the money.

---

**Exercise 5.** A trader is delta-hedging a short ATM call with 1 day to expiry. The discrete hedging error per step is approximately $\frac{1}{2}\Gamma(\Delta S)^2$. Using $\Gamma \sim 1/(S\sigma\sqrt{2\pi\tau})$, estimate the hedging error from a single $1\%$ move in $S$ when $S = 100$, $\sigma = 0.20$, $\tau = 1/252$.

---

**Exercise 6.** For a European put, delta transitions from $-1$ to $0$ as $S$ increases through $K$, with the same transition width $\sim \sigma\sqrt{\tau}$. Using put-call parity, verify that $\Delta_{\text{call}} - \Delta_{\text{put}} = 1$ for all $\tau > 0$, and explain why both deltas have the same gamma profile.
