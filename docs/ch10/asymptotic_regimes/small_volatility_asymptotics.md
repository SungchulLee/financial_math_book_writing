# Small-Volatility Asymptotics


Consider \(\sigma\downarrow 0\). Randomness vanishes and prices approach deterministic limits.

---

## Deterministic limit


As \(\sigma\to 0\),


\[
\mathrm{d}S_t=rS_t\,\mathrm{d}t+\sigma S_t\,\mathrm{d}W_t
\to
\dot{S}_t=rS_t,
\]



so \(S_T\to S e^{r\tau}\).

---

## OTM becomes exponentially small


If \(K>S e^{r\tau}\) (OTM call in the deterministic limit),


\[
C(t,S;K)\approx \exp\!\left(-\frac{c}{2\sigma^2}\right) \cdot (\text{polynomial prefactor})
\]

**Rate function identification.** The constant \(c\) is the squared geodesic distance in the log-moneyness metric:

\[
\boxed{c = \frac{(\ln(K/S) - r\tau)^2}{\tau}}
\]

This represents the squared "distance" the asset must travel (in log-space) from its deterministic trajectory to reach the strike.

**Derivation.** For small \(\sigma\), using \(d_2 = \frac{\ln(S/K) + (r - \frac12\sigma^2)\tau}{\sigma\sqrt{\tau}}\):

\[
d_2 \approx \frac{\ln(S/K) + r\tau}{\sigma\sqrt{\tau}} + \mathcal{O}(\sigma)
\]

For OTM calls, \(\ln(S/K) + r\tau < 0\), so \(d_2 \to -\infty\) as \(\sigma \to 0\).

Using the Gaussian tail:
\[
N(d_2) \approx \frac{1}{|d_2|\sqrt{2\pi}}e^{-d_2^2/2} \approx \exp\!\left(-\frac{(\ln(K/S) - r\tau)^2}{2\sigma^2\tau}\right)
\]

---

## Large deviations interpretation


The small-\(\sigma\) asymptotics connect to Varadhan's lemma: for the diffusion \(S_t\),

\[
-\sigma^2 \log \mathbb{P}(S_T \in A) \to \inf_{s \in A} I(s)
\]

where \(I(s)\) is the rate function (action functional):

\[
I(s) = \frac{1}{2\tau}\left(\ln\frac{s}{S} - r\tau\right)^2
\]

This is the cost of deviating from the deterministic path.

---

## ITM call in small volatility


For ITM calls (\(K < Se^{r\tau}\)):

\[
C \to Se^{-q\tau}N(d_1) - Ke^{-r\tau}N(d_2) \to S - Ke^{-r\tau}
\]

The call converges to its intrinsic value plus carry.

---

## ATM call in small volatility


For ATM forward (\(K = Se^{r\tau}\)):

\[
d_1 = \frac{\sigma\sqrt{\tau}}{2}, \quad d_2 = -\frac{\sigma\sqrt{\tau}}{2}
\]

\[
C_{\text{ATM}} = S(N(d_1) - N(d_2)) \approx \frac{S\sigma\sqrt{\tau}}{\sqrt{2\pi}}
\]

The price is linear in \(\sigma\) at leading order.

---

## Greeks in small volatility


**Vega dominates ATM risk:**
\[
\nu = S\sqrt{\tau}N'(d_1) \approx \frac{S\sqrt{\tau}}{\sqrt{2\pi}} \quad \text{(nearly constant)}
\]

**Gamma for ATM:**
\[
\Gamma = \frac{N'(d_1)}{S\sigma\sqrt{\tau}} \approx \frac{1}{S\sigma\sqrt{2\pi\tau}} \to \infty \quad \text{as } \sigma \to 0
\]

**Delta transition:**
As \(\sigma \to 0\), delta becomes a step function:
\[
\Delta \to \begin{cases} 1 & S > Ke^{-r\tau} \\ \frac{1}{2} & S = Ke^{-r\tau} \\ 0 & S < Ke^{-r\tau} \end{cases}
\]

---

## Connection to heat kernel expansion


The Black–Scholes equation in log-coordinates is a heat equation. The small-\(\sigma^2\) expansion corresponds to the small-time expansion of the heat kernel:

\[
p(x,y;t) \sim \frac{1}{\sqrt{2\pi t}} \exp\!\left(-\frac{(y-x)^2}{2t}\right) \cdot \sum_{n=0}^\infty a_n(x,y) t^n
\]

The leading exponential term gives the rate function; corrections appear as polynomial prefactors.

---

## Laplace principle


The small-\(\sigma\) limit can be analyzed via Laplace's method:

\[
\mathbb{E}[e^{-r\tau}(S_T - K)^+] = \int_K^\infty e^{-r\tau}(s-K) p(s) \, ds
\]

where \(p(s)\) concentrates near \(Se^{r\tau}\). For OTM options, the integral is over the tail, giving exponential decay.

---

## What to remember


- OTM prices shrink exponentially in \(1/\sigma^2\) with rate \(c = (\ln(K/S) - r\tau)^2/\tau\).
- The rate function is the squared geodesic distance from the deterministic trajectory.
- These asymptotics connect to large deviations and Laplace principles.
- Delta becomes step-like; gamma diverges as \(\sigma \to 0\) for ATM options.
- Heat kernel small-time expansion provides the mathematical framework.
