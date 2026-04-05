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

---

## Exercises

**Exercise 1.** For an OTM call with $K = 110$, $S = 100$, $r = 0.03$, $\tau = 1$ year, compute the rate function $c = (\ln(K/S) - r\tau)^2/\tau$ and the exponential decay factor $\exp(-c/(2\sigma^2))$ for $\sigma = 0.10$ and $\sigma = 0.05$. By how many orders of magnitude does the price decrease when volatility halves?

??? success "Solution to Exercise 1"
    First compute $\ln(K/S) = \ln(110/100) = \ln(1.1) = 0.09531$ and $r\tau = 0.03 \times 1 = 0.03$.

    The rate function is

    $$
    c = \frac{(\ln(K/S) - r\tau)^2}{\tau} = \frac{(0.09531 - 0.03)^2}{1} = (0.06531)^2 = 0.004265
    $$

    **For $\sigma = 0.10$:**

    $$
    \exp\!\left(-\frac{c}{2\sigma^2}\right) = \exp\!\left(-\frac{0.004265}{2 \times 0.01}\right) = \exp(-0.2133) = 0.8082
    $$

    **For $\sigma = 0.05$:**

    $$
    \exp\!\left(-\frac{c}{2\sigma^2}\right) = \exp\!\left(-\frac{0.004265}{2 \times 0.0025}\right) = \exp(-0.8530) = 0.4261
    $$

    The ratio of decay factors is $0.4261 / 0.8082 = 0.5272$. In log terms:

    $$
    \log_{10}(0.4261) - \log_{10}(0.8082) = -0.3704 - (-0.0925) = -0.2779
    $$

    So the price decreases by about $0.28$ orders of magnitude (roughly a factor of 1.9) when volatility halves. The key insight is that the decay scales as $1/\sigma^2$, so halving $\sigma$ quadruples the exponent. The effect becomes much more dramatic for larger values of $c$ (further OTM options).

---

**Exercise 2.** For the ATM forward strike $K = Se^{r\tau}$, verify that $d_1 = \sigma\sqrt{\tau}/2$ and $d_2 = -\sigma\sqrt{\tau}/2$. Show that $C_{\text{ATM}} \approx \frac{S\sigma\sqrt{\tau}}{\sqrt{2\pi}}$ to leading order in $\sigma$, confirming linearity in $\sigma$.

??? success "Solution to Exercise 2"
    For the ATM forward strike $K = Se^{r\tau}$, we have $\ln(S/K) = -r\tau$. Substituting into the $d_1$ formula:

    $$
    d_1 = \frac{-r\tau + (r + \frac{1}{2}\sigma^2)\tau}{\sigma\sqrt{\tau}} = \frac{\frac{1}{2}\sigma^2\tau}{\sigma\sqrt{\tau}} = \frac{\sigma\sqrt{\tau}}{2}
    $$

    $$
    d_2 = d_1 - \sigma\sqrt{\tau} = \frac{\sigma\sqrt{\tau}}{2} - \sigma\sqrt{\tau} = -\frac{\sigma\sqrt{\tau}}{2}
    $$

    Now the call price is $C = SN(d_1) - Ke^{-r\tau}N(d_2)$. Since $Ke^{-r\tau} = S$:

    $$
    C = S[N(d_1) - N(d_2)] = S[N(d_1) - N(-d_1)] = S[2N(d_1) - 1]
    $$

    For small $\sigma$, $d_1 = \sigma\sqrt{\tau}/2$ is small, so we expand $N(z) \approx \frac{1}{2} + \frac{z}{\sqrt{2\pi}}$:

    $$
    C \approx S\left[2\left(\frac{1}{2} + \frac{\sigma\sqrt{\tau}/2}{\sqrt{2\pi}}\right) - 1\right] = S \cdot \frac{\sigma\sqrt{\tau}}{\sqrt{2\pi}}
    $$

    This confirms $C_{\text{ATM}} \approx \frac{S\sigma\sqrt{\tau}}{\sqrt{2\pi}}$, which is linear in $\sigma$ at leading order. Higher-order corrections are $\mathcal{O}(\sigma^3)$.

---

**Exercise 3.** As $\sigma \to 0$, delta becomes the step function $\Delta \to \mathbf{1}_{S > Ke^{-r\tau}}$. For $K = 100$, $r = 0.05$, $\tau = 0.5$, compute the critical spot level $S^* = Ke^{-r\tau}$ where the step occurs. Plot (or sketch) delta as a function of $S$ for $\sigma = 0.30$, $0.10$, and $0.01$ to illustrate the convergence to a step function.

??? success "Solution to Exercise 3"
    The critical spot level where the step occurs is

    $$
    S^* = Ke^{-r\tau} = 100 \times e^{-0.05 \times 0.5} = 100 \times e^{-0.025} = 100 \times 0.9753 = 97.53
    $$

    The delta of a call is $\Delta = N(d_1)$ where $d_1 = \frac{\ln(S/K) + (r + \frac{1}{2}\sigma^2)\tau}{\sigma\sqrt{\tau}}$.

    At $S = S^* = 97.53$: $\ln(S/K) = -r\tau = -0.025$, so $d_1 = \frac{\sigma^2\tau/2}{\sigma\sqrt{\tau}} = \frac{\sigma\sqrt{\tau}}{2}$.

    - For $\sigma = 0.30$: $d_1 = 0.30\sqrt{0.5}/2 = 0.1061$, $\Delta = N(0.1061) = 0.5423$
    - For $\sigma = 0.10$: $d_1 = 0.10\sqrt{0.5}/2 = 0.0354$, $\Delta = N(0.0354) = 0.5141$
    - For $\sigma = 0.01$: $d_1 = 0.01\sqrt{0.5}/2 = 0.00354$, $\Delta = N(0.00354) = 0.5014$

    As $\sigma \to 0$, delta at $S^*$ converges to $1/2$ (the midpoint of the step). Away from $S^*$, the convergence to 0 or 1 is rapid. For example, at $S = 95$ (below $S^*$):

    - $\sigma = 0.30$: $d_1 \approx -0.63$, $\Delta \approx 0.26$
    - $\sigma = 0.01$: $d_1 \approx -36.4$, $\Delta \approx 0$

    The transition from $\Delta \approx 0$ to $\Delta \approx 1$ becomes infinitely sharp as $\sigma \to 0$, confirming convergence to the step function $\mathbf{1}_{S > S^*}$.

---

**Exercise 4.** The gamma formula $\Gamma = N'(d_1)/(S\sigma\sqrt{\tau})$ diverges as $\sigma \to 0$ for ATM options. Show that $\Gamma \to \infty$ at rate $1/\sigma$ when $S = Ke^{-r\tau}$. What physical interpretation does this have --- why is the option's convexity infinite in the zero-volatility limit?

??? success "Solution to Exercise 4"
    At $S = Ke^{-r\tau}$ (ATM forward), we have $d_1 = \sigma\sqrt{\tau}/2$ and

    $$
    \Gamma = \frac{N'(d_1)}{S\sigma\sqrt{\tau}} = \frac{1}{S\sigma\sqrt{2\pi\tau}} \exp\!\left(-\frac{\sigma^2\tau}{8}\right)
    $$

    For small $\sigma$, $\exp(-\sigma^2\tau/8) \to 1$, so

    $$
    \Gamma \approx \frac{1}{S\sigma\sqrt{2\pi\tau}}
    $$

    This diverges as $1/\sigma$ when $\sigma \to 0$, confirming the claimed rate.

    **Physical interpretation.** In the zero-volatility limit, the call payoff $(S_T - K)^+$ as a function of $S_0$ becomes a kink: zero for $S_0 < Ke^{-r\tau}$ and $S_0 - Ke^{-r\tau}$ for $S_0 > Ke^{-r\tau}$. The second derivative of this payoff (with respect to $S_0$) is a Dirac delta at $S_0 = Ke^{-r\tau}$.

    For any finite $\sigma > 0$, diffusion smooths this kink into a curve, but the curvature near the kink grows without bound as $\sigma \to 0$. Gamma measures this curvature, so it diverges. Practically, this means delta-hedging becomes infinitely sensitive to small spot moves near ATM when volatility is very low --- the hedger must adjust the position dramatically for tiny price changes.

---

**Exercise 5.** The large deviations rate function $I(s) = \frac{1}{2\tau}(\ln(s/S) - r\tau)^2$ describes the cost of the diffusion reaching level $s$ from $S$. Compute $I(s)$ for $S = 100$, $r = 0.03$, $\tau = 1$, at $s = 80, 100, 120, 150$. Which of these levels is "cheapest" to reach?

??? success "Solution to Exercise 5"
    With $S = 100$, $r = 0.03$, $\tau = 1$, we have $r\tau = 0.03$:

    $$
    I(s) = \frac{1}{2\tau}\left(\ln\frac{s}{S} - r\tau\right)^2 = \frac{1}{2}\left(\ln\frac{s}{100} - 0.03\right)^2
    $$

    **At $s = 80$:** $\ln(80/100) = -0.2231$

    $$
    I(80) = \frac{1}{2}(-0.2231 - 0.03)^2 = \frac{1}{2}(0.2531)^2 = \frac{0.06406}{2} = 0.03203
    $$

    **At $s = 100$:** $\ln(100/100) = 0$

    $$
    I(100) = \frac{1}{2}(0 - 0.03)^2 = \frac{0.0009}{2} = 0.00045
    $$

    **At $s = 120$:** $\ln(120/100) = 0.1823$

    $$
    I(120) = \frac{1}{2}(0.1823 - 0.03)^2 = \frac{1}{2}(0.1523)^2 = \frac{0.02320}{2} = 0.01160
    $$

    **At $s = 150$:** $\ln(150/100) = 0.4055$

    $$
    I(150) = \frac{1}{2}(0.4055 - 0.03)^2 = \frac{1}{2}(0.3755)^2 = \frac{0.1410}{2} = 0.07050
    $$

    The minimum occurs at $s = Se^{r\tau} = 100 \times e^{0.03} = 103.05$, where $I = 0$. Among the given levels, $s = 100$ is cheapest ($I = 0.00045$), being closest to the deterministic forward price. The level $s = 150$ is the most expensive to reach, consistent with it being the farthest from the drift trajectory.

---

**Exercise 6.** The heat kernel expansion $p(x,y;t) \sim \frac{1}{\sqrt{2\pi t}}\exp(-\frac{(y-x)^2}{2t}) \sum_{n=0}^\infty a_n(x,y)t^n$ provides systematic corrections to the leading-order Gaussian. In the Black--Scholes log-coordinate, what is the leading correction $a_1(x,y)$, and how does it relate to the drift term $(r - \frac{1}{2}\sigma^2)$?

??? success "Solution to Exercise 6"
    In log-coordinates $X_t = \ln S_t$, the Black--Scholes SDE becomes

    $$
    dX_t = \left(r - \frac{1}{2}\sigma^2\right)dt + \sigma\,dW_t
    $$

    Rescaling to unit diffusion via $Y = X/\sigma$, the transition density satisfies a heat equation. The exact transition density in log-coordinates is

    $$
    p(x, y; \sigma^2\tau) = \frac{1}{\sigma\sqrt{2\pi\tau}} \exp\!\left(-\frac{(y - x - (r - \frac{1}{2}\sigma^2)\tau)^2}{2\sigma^2\tau}\right)
    $$

    Comparing with the heat kernel expansion $p(x,y;t) \sim \frac{1}{\sqrt{2\pi t}}\exp(-\frac{(y-x)^2}{2t})\sum_n a_n t^n$ where $t = \sigma^2\tau$:

    The leading Gaussian has center $y - x$ with no drift. The drift $\mu = r - \frac{1}{2}\sigma^2$ enters through rewriting

    $$
    \exp\!\left(-\frac{(y - x - \mu\tau)^2}{2\sigma^2\tau}\right) = \exp\!\left(-\frac{(y-x)^2}{2\sigma^2\tau}\right) \exp\!\left(\frac{\mu(y-x)}{\sigma^2} - \frac{\mu^2\tau}{2\sigma^2}\right)
    $$

    Expanding the correction factor in powers of $t = \sigma^2\tau$:

    $$
    \exp\!\left(\frac{\mu(y-x)}{\sigma^2} - \frac{\mu^2\tau}{2\sigma^2}\right) = 1 + \frac{\mu(y-x)}{\sigma^2} + \mathcal{O}(t)
    $$

    The leading correction coefficient is therefore

    $$
    a_0 = 1, \quad a_1 = \frac{\mu(y-x)}{\sigma^2} - \frac{\mu^2}{2\sigma^4} + \frac{\mu^2(y-x)^2}{2\sigma^4}
    $$

    More precisely, collecting terms at order $t = \sigma^2\tau$: the $a_1$ correction encodes how the drift $\mu = r - \frac{1}{2}\sigma^2$ shifts the center of the Gaussian away from $y - x$. In the Black--Scholes case with constant coefficients, the expansion terminates because the exact density is Gaussian. For models with state-dependent volatility, $a_1$ involves curvature of the metric and is genuinely non-trivial.
