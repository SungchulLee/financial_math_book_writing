# Scaling Laws for Greeks


This section provides a unified framework for understanding how Greeks scale with time-to-maturity $\tau$ and moneyness.

---

## Near-the-money ATM scaling table


For at-the-money options ($S \approx K$) in Black–Scholes:

| Greek | ATM Formula | Scaling in $\tau$ | Behavior as $\tau \to 0$ |
|:------|:------------|:--------------------|:---------------------------|
| $\Delta$ | $N(d_1) \approx \frac{1}{2}$ | $\mathcal{O}(1)$ | $\to \frac{1}{2}$ |
| $\Gamma$ | $\frac{1}{S\sigma\sqrt{2\pi\tau}}$ | $\tau^{-1/2}$ | $\to \infty$ |
| $\Theta$ | $-\frac{S\sigma}{2\sqrt{2\pi\tau}}$ | $\tau^{-1/2}$ | $\to -\infty$ |
| $\nu$ (Vega) | $\frac{S\sqrt{\tau}}{\sqrt{2\pi}}$ | $\tau^{1/2}$ | $\to 0$ |
| $\rho$ | $\frac{K\tau}{2}e^{-r\tau}$ | $\tau$ | $\to 0$ |

---

## Theta-Gamma relationship


A fundamental identity links theta and gamma for delta-hedged positions:

$$
\boxed{\Theta + \frac{1}{2}\sigma^2 S^2 \Gamma = rV - rS\Delta}
$$

For ATM options where $\Delta \approx \frac{1}{2}$ and $V \approx \frac{S\sigma\sqrt{\tau}}{\sqrt{2\pi}}$:

$$
\Theta \approx -\frac{1}{2}\sigma^2 S^2 \Gamma + \mathcal{O}(\sqrt{\tau})
$$

This shows that **time decay and gamma are two sides of the same coin**: options with high gamma (convexity benefit) must pay for it through time decay.

---

## Dimensional analysis


Greeks can be understood through dimensional analysis. Let $[X]$ denote the dimension of $X$:

| Quantity | Dimension |
|:---------|:----------|
| $V$ (price) | $\$$ |
| $S$ (spot) | $\$$ |
| $\tau$ (time) | $T$ |
| $\sigma$ (volatility) | $T^{-1/2}$ |

Then:

- $\Delta = \partial V/\partial S$ is dimensionless
- $\Gamma = \partial^2 V/\partial S^2$ has dimension $\$^{-1}$
- $\Theta = \partial V/\partial t$ has dimension $\$/T$
- $\nu = \partial V/\partial \sigma$ has dimension $\$ \cdot T^{1/2}$

The ATM scalings follow from $V_{\text{ATM}} \sim S\sigma\sqrt{\tau}$:

$$
\Gamma_{\text{ATM}} \sim \frac{V}{S^2} \cdot \frac{1}{\sigma\sqrt{\tau}} \sim \frac{1}{S\sigma\sqrt{\tau}}
$$

---

## Far from the money: exponential decay


For OTM options with log-moneyness $x = \ln(K/S)$:

| Greek | OTM decay rate |
|:------|:---------------|
| $\Delta$ | $\exp(-x^2/(2\sigma^2\tau))$ |
| $\Gamma$ | $\frac{1}{S}\exp(-x^2/(2\sigma^2\tau))$ |
| $\nu$ | $S\sqrt{\tau}\exp(-x^2/(2\sigma^2\tau))$ |

The characteristic scale separating ATM from OTM is $|x| \sim \sigma\sqrt{\tau}$.

---

## Unified asymptotic expansion


For options near ATM as $\tau \to 0$, all Greeks can be expanded in powers of $\sqrt{\tau}$:

**Price:**

$$
V = V_0 + V_1 \sqrt{\tau} + V_2 \tau + \mathcal{O}(\tau^{3/2})
$$

where $V_0 = (S-K)^+$ (intrinsic), $V_1 = \frac{S\sigma}{\sqrt{2\pi}}\mathbf{1}_{\text{ATM}}$ (ATM time value).

**Greeks:**

$$
\Gamma = \frac{1}{S\sigma\sqrt{2\pi\tau}} + \mathcal{O}(1)
$$

$$
\Theta = -\frac{S\sigma}{2\sqrt{2\pi\tau}} + \mathcal{O}(1)
$$

$$
\nu = \frac{S\sqrt{\tau}}{\sqrt{2\pi}} + \mathcal{O}(\tau)
$$

---

## Medium maturity: vega dominance


For moderate maturities ($\tau \sim 1$ year), vega often dominates portfolio risk:

- Vega is maximized around $\tau \sim 1/(2r)$ for typical interest rates
- Gamma remains bounded: $\Gamma \sim \frac{1}{S\sigma}$
- Theta-vega ratio: $\Theta/\nu \sim -\sigma/(2\tau)$

---

## Long maturity asymptotics


For $\tau \to \infty$:

**Call price:** $C \to S$ (assuming no dividends)

**Greeks:**

- $\Delta \to 1$
- $\Gamma \to 0$ as $\tau^{-1/2}$
- $\nu \to S\sqrt{\tau}N'(d_1) \sim S\sqrt{\tau}/\sqrt{2\pi}$ grows without bound
- $\rho \to K\tau e^{-r\tau}N(d_2)$ grows then decays

---

## Practical implications


1. **Short-dated options**: Large gamma, unstable delta hedging, high theta decay
2. **Medium-dated options**: Vega dominance, sensitivity to implied vol changes
3. **Long-dated options**: Low gamma, stable delta, model risk concerns

---

## Greeks scaling summary


$$
\boxed{
\begin{aligned}
&\text{ATM, short maturity:} & \Gamma &\sim \tau^{-1/2}, & \nu &\sim \tau^{1/2}, & \Theta &\sim -\tau^{-1/2} \\
&\text{OTM, any maturity:} & \text{All} &\sim \exp(-x^2/(2\sigma^2\tau))
\end{aligned}
}
$$

---

## What to remember


- Short-dated ATM options: large gamma ($\tau^{-1/2}$), unstable higher Greeks
- Vega scales as $\sqrt{\tau}$, peaking at moderate maturities
- Theta and gamma are linked: $\Theta \approx -\frac{1}{2}\sigma^2 S^2 \Gamma$ for ATM
- Extreme strikes: tail-dominated sensitivities with exponential decay
- Dimensional analysis provides quick scaling estimates

---

## Exercises

**Exercise 1.** Using the dimensional analysis framework, verify that $\Gamma_{\text{ATM}} \sim 1/(S\sigma\sqrt{\tau})$ has dimension $\$^{-1}$ and that $\Theta_{\text{ATM}} \sim -S\sigma/(2\sqrt{\tau})$ has dimension $\$/T$. Check that the theta-gamma identity $\Theta + \frac{1}{2}\sigma^2 S^2 \Gamma = r(V - S\Delta)$ is dimensionally consistent.

??? success "Solution to Exercise 1"
    **Checking $\Gamma_{\text{ATM}}$:** The dimension of $\Gamma = \partial^2 V / \partial S^2$ is $[\$] / [\$]^2 = \$^{-1}$.

    For $\Gamma_{\text{ATM}} \sim 1/(S\sigma\sqrt{\tau})$: the dimension of the denominator is $[\$] \cdot [T^{-1/2}] \cdot [T^{1/2}] = [\$]$, so $\Gamma_{\text{ATM}}$ has dimension $\$^{-1}$. Confirmed.

    **Checking $\Theta_{\text{ATM}}$:** The dimension of $\Theta = \partial V / \partial t$ is $[\$]/[T]$.

    For $\Theta_{\text{ATM}} \sim -S\sigma/(2\sqrt{\tau})$: the dimension is $[\$] \cdot [T^{-1/2}] / [T^{1/2}] = [\$] / [T]$. Confirmed.

    **Checking the theta-gamma identity** $\Theta + \frac{1}{2}\sigma^2 S^2 \Gamma = r(V - S\Delta)$:

    - Left side, first term: $[\Theta] = \$/T$
    - Left side, second term: $[\sigma^2 S^2 \Gamma] = [T^{-1}][\$^2][\$^{-1}] = \$/T$. Consistent.
    - Right side: $[r(V - S\Delta)] = [T^{-1}][\$] = \$/T$. Consistent.

    All three terms have dimension $\$/T$, so the identity is dimensionally consistent.

---

**Exercise 2.** For an OTM call with log-moneyness $x = \ln(K/S) = 0.10$ (roughly 10% OTM), $\sigma = 0.20$, and $\tau = 0.25$ years, compute the exponential decay factor $\exp(-x^2/(2\sigma^2\tau))$. How does this compare to the ATM vega at the same maturity?

??? success "Solution to Exercise 2"
    With $x = 0.10$, $\sigma = 0.20$, and $\tau = 0.25$:

    $$
    \sigma^2\tau = 0.04 \times 0.25 = 0.01
    $$

    $$
    \frac{x^2}{2\sigma^2\tau} = \frac{0.01}{0.02} = 0.5
    $$

    $$
    \exp\!\left(-\frac{x^2}{2\sigma^2\tau}\right) = e^{-0.5} \approx 0.6065
    $$

    The ATM vega at the same maturity is $\nu_{\text{ATM}} \approx S\sqrt{\tau}/\sqrt{2\pi} = 100 \times 0.5 / 2.507 \approx 19.95$.

    The OTM vega is approximately $\nu_{\text{OTM}} \approx 19.95 \times 0.6065 \approx 12.10$.

    So the 10% OTM option retains about $61\%$ of the ATM vega. This is because $|x|/(\sigma\sqrt{\tau}) = 0.10/0.10 = 1$, meaning the option is only one characteristic width away from ATM. At this moderate distance, vega is reduced but far from negligible.

---

**Exercise 3.** The theta-gamma relationship states that for ATM options, $\Theta \approx -\frac{1}{2}\sigma^2 S^2 \Gamma$. Verify this numerically for $S = K = 100$, $\sigma = 0.20$, $r = 0.05$, $\tau = 0.5$ by computing both sides using the closed-form Black--Scholes formulas.

??? success "Solution to Exercise 3"
    Using the Black-Scholes formulas with $S = K = 100$, $\sigma = 0.20$, $r = 0.05$, $\tau = 0.5$:

    $$
    d_1 = \frac{\ln(1) + (0.05 + 0.02) \times 0.5}{0.20\sqrt{0.5}} = \frac{0.035}{0.1414} = 0.2475
    $$

    $$
    d_2 = d_1 - 0.20\sqrt{0.5} = 0.2475 - 0.1414 = 0.1061
    $$

    $$
    N'(d_1) = \frac{1}{\sqrt{2\pi}}e^{-d_1^2/2} = \frac{1}{2.5066}e^{-0.0306} = 0.3988 \times 0.9698 = 0.3868
    $$

    **Computing $\Gamma$:**

    $$
    \Gamma = \frac{N'(d_1)}{S\sigma\sqrt{\tau}} = \frac{0.3868}{100 \times 0.20 \times 0.7071} = \frac{0.3868}{14.14} = 0.02736
    $$

    **Computing $\Theta$:** The exact Black-Scholes theta for a call is

    $$
    \Theta = -\frac{S\sigma N'(d_1)}{2\sqrt{\tau}} - rKe^{-r\tau}N(d_2)
    $$

    $$
    = -\frac{100 \times 0.20 \times 0.3868}{2 \times 0.7071} - 0.05 \times 100 \times e^{-0.025} \times N(0.1061)
    $$

    $$
    = -\frac{7.736}{1.4142} - 5 \times 0.9753 \times 0.5422 = -5.472 - 2.644 = -8.116
    $$

    **Left side of identity:** $-\frac{1}{2}\sigma^2 S^2 \Gamma = -\frac{1}{2}(0.04)(10000)(0.02736) = -5.472$.

    **Right side:** $r(V - S\Delta)$. We need $V$ and $\Delta$:

    $$
    \Delta = N(d_1) = N(0.2475) \approx 0.5977
    $$

    $$
    V = SN(d_1) - Ke^{-r\tau}N(d_2) = 100(0.5977) - 100(0.9753)(0.5422) = 59.77 - 52.89 = 6.88
    $$

    $$
    r(V - S\Delta) = 0.05(6.88 - 59.77) = 0.05(-52.89) = -2.645
    $$

    **Checking:** $\Theta + \frac{1}{2}\sigma^2 S^2\Gamma = -8.116 + 5.472 = -2.644 \approx -2.645 = r(V - S\Delta)$.

    The identity is verified numerically, confirming $\Theta \approx -\frac{1}{2}\sigma^2 S^2\Gamma$ up to the correction term $r(V - S\Delta)$.

---

**Exercise 4.** A portfolio manager holds ATM options at three maturities: $\tau = 0.08$ (1 month), $\tau = 0.5$ (6 months), and $\tau = 2$ (2 years). Using the scaling laws, rank these positions by: (a) gamma exposure, (b) vega exposure, (c) daily theta bleed. Which maturity dominates each risk?

??? success "Solution to Exercise 4"
    Using the ATM scaling formulas with $S = K = 100$, $\sigma = 0.20$:

    **(a) Gamma exposure** ($\Gamma \sim 1/(S\sigma\sqrt{2\pi\tau})$):

    - $\tau = 0.08$: $\Gamma \approx 1/(100 \times 0.20 \times \sqrt{2\pi \times 0.08}) = 1/(20 \times 0.7090) = 0.0706$
    - $\tau = 0.5$: $\Gamma \approx 1/(20 \times 1.7725) = 0.0283$
    - $\tau = 2$: $\Gamma \approx 1/(20 \times 3.5449) = 0.0141$

    Ranking (highest to lowest gamma): 1-month $>$ 6-month $>$ 2-year.

    **(b) Vega exposure** ($\nu \sim S\sqrt{\tau}/\sqrt{2\pi}$):

    - $\tau = 0.08$: $\nu \approx 100 \times 0.2828 / 2.5066 = 11.28$
    - $\tau = 0.5$: $\nu \approx 100 \times 0.7071 / 2.5066 = 28.21$
    - $\tau = 2$: $\nu \approx 100 \times 1.4142 / 2.5066 = 56.42$

    Ranking (highest to lowest vega): 2-year $>$ 6-month $>$ 1-month.

    **(c) Daily theta bleed** ($\Theta \sim -S\sigma/(2\sqrt{2\pi\tau})$, converted to daily):

    - $\tau = 0.08$: $\Theta/365 \approx -(100 \times 0.20)/(2 \times 0.7090 \times 365) = -20/517.6 = -0.0387$ per day
    - $\tau = 0.5$: $\Theta/365 \approx -20/(2 \times 1.7725 \times 365) = -20/1293.9 = -0.0155$ per day
    - $\tau = 2$: $\Theta/365 \approx -20/(2 \times 3.5449 \times 365) = -20/2587.8 = -0.00773$ per day

    Ranking (highest daily theta bleed): 1-month $>$ 6-month $>$ 2-year.

    **Summary:** Short-dated options dominate gamma and theta risk, while long-dated options dominate vega risk. This reflects the fundamental scaling: gamma and theta scale as $\tau^{-1/2}$ (growing as maturity shrinks) while vega scales as $\tau^{1/2}$ (growing with maturity).

---

**Exercise 5.** The characteristic scale separating ATM from OTM is $|x| \sim \sigma\sqrt{\tau}$. For $\sigma = 0.30$ and $\tau = 1$ month, compute this scale in both log-moneyness units and as a percentage of spot price. An option with $K = 105$ when $S = 100$ --- is it effectively ATM or OTM at this maturity?

??? success "Solution to Exercise 5"
    With $\sigma = 0.30$ and $\tau = 1/12$ (1 month):

    $$
    \sigma\sqrt{\tau} = 0.30 \times \sqrt{1/12} = 0.30 \times 0.2887 = 0.08660
    $$

    This is the scale in log-moneyness units (dimensionless).

    As a percentage of spot price: since $|x| = |\ln(S/K)| \approx |S - K|/S$ for small deviations, the characteristic scale is about $8.66\%$ of spot.

    For $K = 105$ and $S = 100$:

    $$
    |x| = |\ln(105/100)| = \ln(1.05) \approx 0.04879
    $$

    The ratio of this log-moneyness to the characteristic scale is:

    $$
    \frac{|x|}{\sigma\sqrt{\tau}} = \frac{0.04879}{0.08660} \approx 0.564
    $$

    Since this ratio is less than 1, the $K = 105$ option is well within one characteristic width of ATM. At this maturity, the option is **effectively ATM** --- its Greeks (delta, gamma, vega) will be only modestly reduced from their peak ATM values. The exponential decay factor is $\exp(-0.564^2/2) = e^{-0.159} \approx 0.853$, so Greeks are at about $85\%$ of their ATM levels.

---

**Exercise 6.** In the long-maturity regime ($\tau \to \infty$), vega grows as $S\sqrt{\tau}/\sqrt{2\pi}$ while gamma decays as $1/(S\sigma\sqrt{2\pi\tau})$. Show that the ratio $\nu/\Gamma = \sigma S^2 \tau$ grows linearly with $\tau$. What does this imply about the relative importance of vega versus gamma hedging for long-dated options?

??? success "Solution to Exercise 6"
    Using the ATM scaling formulas:

    $$
    \nu_{\text{ATM}} \approx \frac{S\sqrt{\tau}}{\sqrt{2\pi}}, \qquad \Gamma_{\text{ATM}} \approx \frac{1}{S\sigma\sqrt{2\pi\tau}}
    $$

    Taking the ratio:

    $$
    \frac{\nu}{\Gamma} = \frac{S\sqrt{\tau}/\sqrt{2\pi}}{1/(S\sigma\sqrt{2\pi\tau})} = \frac{S\sqrt{\tau}}{\sqrt{2\pi}} \times S\sigma\sqrt{2\pi\tau} = \sigma S^2 \tau
    $$

    This grows linearly with $\tau$, confirming the claim.

    **Implications for hedging long-dated options:** As $\tau$ increases, vega grows much faster relative to gamma. For a portfolio of long-dated options:

    - A $1\%$ change in implied volatility ($\Delta\sigma = 0.01$) causes P&L of $\nu \times 0.01 \sim S\sqrt{\tau}/\sqrt{2\pi} \times 0.01$, which grows with $\sqrt{\tau}$.
    - A $1\%$ move in spot ($\Delta S = 0.01 S$) causes gamma P&L of $\frac{1}{2}\Gamma(\Delta S)^2 \sim S/(2\sigma\sqrt{2\pi\tau}) \times (0.01)^2$, which decays with $\sqrt{\tau}$.

    For long-dated options ($\tau \gg 1$), vega dominates portfolio risk by a factor proportional to $\tau$. Therefore, **vega hedging is far more important than gamma hedging for long-dated positions**. This is why traders managing long-dated books focus primarily on volatility surface risk rather than delta-gamma risk.
