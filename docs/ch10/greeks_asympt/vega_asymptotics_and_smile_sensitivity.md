# Vega Asymptotics and Smile Sensitivity


Vega concentrates near the money and vanishes as maturity shrinks. In models with a volatility smile, the concept of vega generalizes from a single scalar to a multi-dimensional surface sensitivity.

---

## Black–Scholes vega: closed form

**Recall** (see [§ Greeks in the Black–Scholes Model](../greeks/greeks_in_black_scholes_model.md)): for both calls and puts,

$$
\nu = S\sqrt{\tau}\,N'(d_1),
$$

with $d_1$ as defined there. Vega is always non-negative: higher volatility increases the value of a vanilla option.

---

## Near-the-money scaling


When $S \approx K$ (ATM), we have $d_1 \approx \frac{(r + \frac{1}{2}\sigma^2)\sqrt{\tau}}{\sigma} = \mathcal{O}(\sqrt{\tau})$, so $N'(d_1) \approx \frac{1}{\sqrt{2\pi}}$. Therefore

$$
\boxed{\nu_{\text{ATM}} \approx \frac{S\sqrt{\tau}}{\sqrt{2\pi}} \sim S\sqrt{\tau}}
$$

Key observations:

- Vega scales as $\sqrt{\tau}$ for ATM options: it vanishes at expiry but slowly.
- For fixed $\tau$, vega peaks at-the-money and decays as the option moves OTM or deep ITM.
- The peak vega value grows with maturity, making long-dated ATM options most sensitive to volatility.

---

## Away-from-the-money decay


For $|x| = |\ln(S/K)| \gg \sigma\sqrt{\tau}$, the Gaussian factor dominates:

$$
\nu \sim S\sqrt{\tau}\,\exp\!\left(-\frac{x^2}{2\sigma^2\tau}\right)
$$

This shows vega decays **exponentially** in the square of log-moneyness, normalized by $\sigma^2\tau$. Deep ITM and OTM options have negligible vega for short maturities.

---

## Short-maturity asymptotics


As $\tau \to 0$ with fixed moneyness:

$$
\nu \to 0 \quad \text{for all } S \neq K
$$

The rate of decay depends on moneyness:

- **ATM** ($S = K$): $\nu \sim \sqrt{\tau}$, slow decay.
- **OTM/ITM**: $\nu \sim \sqrt{\tau}\exp(-x^2/(2\sigma^2\tau))$, exponentially fast decay.

In the rescaled variable $z = x/(\sigma\sqrt{\tau})$, vega has the inner-layer form

$$
\nu \approx \frac{S\sqrt{\tau}}{\sqrt{2\pi}}\exp\!\left(-\frac{z^2}{2}\right)
$$

showing that vega concentrates on a band of width $\sigma\sqrt{\tau}$ in log-moneyness — the same boundary layer that governs delta and gamma near expiry.

---

## Vega and the theta-gamma relationship


From the Black–Scholes PDE, there is a direct link between vega and gamma:

$$
\nu = \sigma S^2 \tau \,\Gamma
$$

This identity shows that vega and gamma are proportional (in Black–Scholes), with the proportionality factor $\sigma S^2 \tau$. Consequently:

- Vega risk and gamma risk are not independent in Black–Scholes.
- Hedging gamma automatically hedges vega in this model (but not in stochastic volatility models).

---

## Smile models: generalized vega


With an implied volatility surface $\Sigma(T,K)$, the Black–Scholes vega measures sensitivity to a **parallel shift** of the entire surface. In practice, the surface deforms non-uniformly, motivating several generalizations:

**Bucket vega.** Partition the surface into regions (buckets) by maturity and strike, and compute sensitivity to a shift in each bucket independently:

$$
\nu_{ij} = \frac{\partial V}{\partial \Sigma_{ij}}
$$

where $\Sigma_{ij}$ is the implied vol in bucket $(T_i, K_j)$. This gives a **vega matrix** rather than a single number.

**Vega by maturity (term structure vega).** For portfolios of options at different maturities, compute sensitivity to shifts in each maturity slice:

$$
\nu(T_i) = \sum_{j} \frac{\partial V_j}{\partial \sigma(T_i)}
$$

**Model vega.** In parametric models (Heston, SABR), vega can be defined with respect to each model parameter. For the Heston model with parameters $(\bar{v}, \kappa, \xi, \rho, v_0)$:

$$
\frac{\partial V}{\partial v_0}, \quad \frac{\partial V}{\partial \bar{v}}, \quad \frac{\partial V}{\partial \xi}
$$

each measure a different aspect of volatility sensitivity.

---

## Vega convexity (volga/vomma)


The second derivative of the option price with respect to volatility is called **volga** (or vomma):

$$
\text{Volga} = \frac{\partial^2 V}{\partial \sigma^2} = \frac{\partial \nu}{\partial \sigma}
$$

In Black–Scholes:

$$
\text{Volga} = \nu \cdot \frac{d_1 d_2}{\sigma}
$$

Volga is positive for OTM/ITM options ($d_1 d_2 > 0$) and negative for ATM options ($d_1 d_2 < 0$ when $d_1$ and $d_2$ have opposite signs). Volga matters for:

- Pricing convexity adjustments in smile models.
- Understanding the P&L of vega-hedged positions when volatility moves substantially.

---

## Practical implications


**Vega exposure management.** A portfolio's aggregate vega determines its first-order exposure to implied volatility shifts. Vega-neutral portfolios combine long and short options to achieve $\sum_i \nu_i = 0$.

**Maturity mismatch.** Hedging a long-dated option's vega with short-dated options requires more contracts (since short-dated vega $\sim \sqrt{\tau_{\text{short}}}$ is smaller) and introduces term structure risk.

**Vega and P&L attribution.** For a portfolio with vega $\nu$, an implied vol move of $\Delta\sigma$ generates approximate P&L:

$$
\Delta V \approx \nu \cdot \Delta\sigma + \frac{1}{2}\text{Volga}\cdot(\Delta\sigma)^2
$$

---

## What to remember


- Short-maturity vega vanishes but localizes sharply near ATM, scaling as $\sqrt{\tau}$.
- In Black–Scholes, vega is proportional to gamma via $\nu = \sigma S^2 \tau \Gamma$.
- In smile models, vega is multi-dimensional (surface risk), requiring bucket vegas or model-parameter sensitivities.
- Volga (vega convexity) matters for large vol moves and smile pricing adjustments.

---

## Exercises

**Exercise 1.** For an ATM call with $S = K = 100$, $\sigma = 0.20$, compute vega at $\tau = 1$ year, $\tau = 3$ months, and $\tau = 1$ week. Verify that the ratio of vegas approximately follows the $\sqrt{\tau}$ scaling.

??? success "Solution to Exercise 1"
    Using $\nu_{\text{ATM}} \approx S\sqrt{\tau}/\sqrt{2\pi}$ with $S = K = 100$ and $\sigma = 0.20$:

    - **$\tau = 1$ year:** $\nu = 100\sqrt{1}/\sqrt{2\pi} = 100/2.5066 \approx 39.89$
    - **$\tau = 3$ months ($0.25$ years):** $\nu = 100\sqrt{0.25}/\sqrt{2\pi} = 100 \times 0.5/2.5066 \approx 19.95$
    - **$\tau = 1$ week ($1/52 \approx 0.01923$ years):** $\nu = 100\sqrt{0.01923}/\sqrt{2\pi} = 100 \times 0.1387/2.5066 \approx 5.53$

    **Verifying $\sqrt{\tau}$ scaling:** The ratios should satisfy $\nu(\tau_1)/\nu(\tau_2) = \sqrt{\tau_1/\tau_2}$:

    $$
    \frac{\nu(1)}{\nu(0.25)} = \frac{39.89}{19.95} \approx 2.00 = \sqrt{1/0.25} = \sqrt{4} = 2.00
    $$

    $$
    \frac{\nu(0.25)}{\nu(1/52)} = \frac{19.95}{5.53} \approx 3.61 \approx \sqrt{0.25/0.01923} = \sqrt{13} \approx 3.61
    $$

    The $\sqrt{\tau}$ scaling is confirmed. Note that these are approximate values using the leading-order ATM formula; exact Black-Scholes values would include small corrections from the $d_1^2/2$ term in the exponent.

---

**Exercise 2.** Using the formula $\text{Volga} = \nu \cdot d_1 d_2 / \sigma$, determine the sign of volga for: (a) an ATM option with $d_1 > 0$, $d_2 < 0$; (b) a deep ITM option with $d_1 \gg 0$, $d_2 \gg 0$; (c) a deep OTM option with $d_1 \ll 0$, $d_2 \ll 0$. Which options benefit most from volatility-of-volatility?

??? success "Solution to Exercise 2"
    Using $\text{Volga} = \nu \cdot d_1 d_2 / \sigma$:

    **(a) ATM option with $d_1 > 0$, $d_2 < 0$:** The product $d_1 d_2 < 0$, so $\text{Volga} < 0$. ATM options have negative volga --- their vega decreases when volatility rises. This means ATM options are concave in volatility.

    **(b) Deep ITM option with $d_1 \gg 0$, $d_2 \gg 0$:** The product $d_1 d_2 > 0$, so $\text{Volga} > 0$. Deep ITM options have positive volga --- their vega increases when volatility rises.

    **(c) Deep OTM option with $d_1 \ll 0$, $d_2 \ll 0$:** The product $d_1 d_2 > 0$ (both negative), so $\text{Volga} > 0$. Deep OTM options also have positive volga.

    **Which options benefit most from volatility-of-volatility?** Options with large positive volga benefit from vol-of-vol because the convexity effect means they gain more from upward vol moves than they lose from downward moves. Deep OTM and deep ITM options (wings) have the largest positive volga, and therefore benefit most. This is why the volatility smile (higher implied vol for wings) can be partly explained by the "vanna-volga" framework: the market charges more for wing options to compensate for their positive convexity exposure to volatility uncertainty.

---

**Exercise 3.** The identity $\nu = \sigma S^2 \tau \Gamma$ links vega and gamma in Black--Scholes. Verify this identity numerically for a call with $S = 100$, $K = 110$, $\sigma = 0.25$, $r = 0.03$, $\tau = 0.5$. Why does this relationship break down in stochastic volatility models?

??? success "Solution to Exercise 3"
    **Numerical verification with** $S = 100$, $K = 110$, $\sigma = 0.25$, $r = 0.03$, $\tau = 0.5$:

    $$
    d_1 = \frac{\ln(100/110) + (0.03 + 0.03125) \times 0.5}{0.25\sqrt{0.5}} = \frac{-0.09531 + 0.03063}{0.17678} = \frac{-0.06469}{0.17678} = -0.3659
    $$

    $$
    N'(d_1) = \frac{1}{\sqrt{2\pi}}\exp(-d_1^2/2) = 0.39894 \times \exp(-0.06693) = 0.39894 \times 0.93525 = 0.3731
    $$

    **Computing vega:**

    $$
    \nu = S\sqrt{\tau}\,N'(d_1) = 100 \times 0.7071 \times 0.3731 = 26.38
    $$

    **Computing gamma:**

    $$
    \Gamma = \frac{N'(d_1)}{S\sigma\sqrt{\tau}} = \frac{0.3731}{100 \times 0.25 \times 0.7071} = \frac{0.3731}{17.678} = 0.02111
    $$

    **Checking $\nu = \sigma S^2 \tau \Gamma$:**

    $$
    \sigma S^2 \tau \Gamma = 0.25 \times 10000 \times 0.5 \times 0.02111 = 1250 \times 0.02111 = 26.39
    $$

    This matches $\nu = 26.38$ (the tiny difference is rounding).

    **Why this breaks down in stochastic volatility models:** The identity $\nu = \sigma S^2 \tau \Gamma$ relies on the Black-Scholes assumption that volatility $\sigma$ is a constant. It is derived from the fact that a change in $\sigma$ is equivalent to a rescaling of the diffusion, which can be absorbed into gamma. In stochastic volatility models (e.g., Heston), volatility follows its own random process with additional parameters (vol-of-vol, mean reversion, correlation). Vega then measures sensitivity to the entire volatility path, not just a single parameter, and the proportionality to gamma breaks. In particular, gamma hedging no longer automatically hedges vega, and the two risks become genuinely independent.

---

**Exercise 4.** A trader holds a portfolio with vega $\nu = 500$ and volga $= 2000$. If implied volatility increases from $20\%$ to $23\%$, estimate the portfolio P&L using both the first-order approximation ($\nu \cdot \Delta\sigma$) and the second-order approximation ($\nu \cdot \Delta\sigma + \frac{1}{2}\text{Volga}\cdot(\Delta\sigma)^2$). How significant is the volga correction?

??? success "Solution to Exercise 4"
    Given $\nu = 500$, $\text{Volga} = 2000$, and $\Delta\sigma = 0.23 - 0.20 = 0.03$:

    **First-order approximation:**

    $$
    \Delta V \approx \nu \cdot \Delta\sigma = 500 \times 0.03 = 15.0
    $$

    **Second-order approximation:**

    $$
    \Delta V \approx \nu \cdot \Delta\sigma + \frac{1}{2}\text{Volga} \cdot (\Delta\sigma)^2 = 500 \times 0.03 + \frac{1}{2} \times 2000 \times (0.03)^2
    $$

    $$
    = 15.0 + 1000 \times 0.0009 = 15.0 + 0.9 = 15.9
    $$

    **Significance of the volga correction:** The second-order term adds $\$0.90$ to the P&L estimate, which is $0.9/15.0 = 6\%$ of the first-order estimate. For a 3 percentage point vol move, this is modest but not negligible. The volga correction becomes increasingly important for larger vol moves: for $\Delta\sigma = 0.05$ (a 5-point move), the correction would be $\frac{1}{2}(2000)(0.0025) = 2.5$, which is $2.5/25 = 10\%$ of the first-order term. For stress scenarios or vol-of-vol-sensitive portfolios, omitting volga leads to material P&L misestimates.

---

**Exercise 5.** Explain why bucket vega is more informative than scalar vega for a portfolio containing options at multiple maturities. If a portfolio has positive vega for 1-month options and negative vega for 1-year options, is the portfolio "long vega" or "short vega"? How could implied volatility move to cause a loss?

??? success "Solution to Exercise 5"
    **Why bucket vega is more informative:** Scalar vega measures sensitivity to a uniform parallel shift of the entire implied volatility surface. In reality, short-dated and long-dated implied volatilities move independently (or even in opposite directions). Bucket vega decomposes the sensitivity by maturity (and strike), revealing the portfolio's exposure to each region of the surface separately.

    **Portfolio with positive 1-month vega and negative 1-year vega:** This portfolio is simultaneously long short-dated volatility and short long-dated volatility. Whether it is "long" or "short" vega depends on the aggregation. The scalar vega could be near zero (if the exposures offset) even though the portfolio has substantial term-structure risk.

    **How implied volatility could move to cause a loss:** If the term structure of implied volatility steepens --- specifically, if short-dated vol falls and long-dated vol rises --- both legs lose:

    - The long 1-month vega position loses from the drop in short-dated vol.
    - The short 1-year vega position loses from the rise in long-dated vol.

    This "bear steepener" in the vol term structure would cause losses even if the average level of vol does not change. A scalar vega of zero would entirely miss this risk, while the bucket vega representation would immediately flag the opposing exposures and the vulnerability to term-structure moves.

---

**Exercise 6.** For a far OTM option with $|x| = |\ln(S/K)| = 0.20$ and $\sigma\sqrt{\tau} = 0.10$, compute the vega decay factor $\exp(-x^2/(2\sigma^2\tau))$. How does this compare to the ATM vega? What implications does this have for hedging the vega of a portfolio with many OTM options?

??? success "Solution to Exercise 6"
    With $|x| = 0.20$ and $\sigma\sqrt{\tau} = 0.10$:

    $$
    \frac{x^2}{2\sigma^2\tau} = \frac{(0.20)^2}{2(0.10)^2} = \frac{0.04}{0.02} = 2
    $$

    $$
    \exp\!\left(-\frac{x^2}{2\sigma^2\tau}\right) = e^{-2} \approx 0.1353
    $$

    The OTM option's vega is only about $13.5\%$ of the ATM vega at the same maturity. In terms of the rescaled variable, $|z| = |x|/(\sigma\sqrt{\tau}) = 0.20/0.10 = 2$, meaning this option is two characteristic widths from ATM.

    **Implications for hedging OTM portfolios:** Since OTM options have sharply reduced vega, hedging a portfolio with many OTM options requires attention to several issues:

    - **Many contracts needed:** Each OTM option contributes little vega, so achieving a given vega target requires far more OTM contracts than ATM contracts.
    - **Moneyness sensitivity:** The vega of OTM options changes rapidly with spot moves (through the exponential factor), so a portfolio's aggregate vega can shift significantly as the underlying moves. An OTM option that currently has small vega can become an ATM option (with large vega) if spot moves toward its strike.
    - **Smile effects:** At $|z| = 2$, the option is in the wing region where the volatility smile matters most. The Black-Scholes vega may not accurately capture the true sensitivity to implied vol changes, and bucket or model vegas are essential for proper hedging.
