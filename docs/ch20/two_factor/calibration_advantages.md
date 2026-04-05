# Calibration Advantages of Two Factors

The one-factor Hull-White model produces perfectly correlated yield changes across all maturities, limiting its ability to fit the swaption volatility matrix. The two-factor extension, with five parameters $(\lambda_1, \lambda_2, \sigma_1, \sigma_2, \rho)$, provides sufficient flexibility to capture the decorrelation between short and long rates observed in the market. This section quantifies the two-factor model's calibration advantages, focusing on the swaption matrix fit, the decorrelation across tenors, and the pricing implications for exotic derivatives.

## Swaption Matrix Fit: One Factor vs Two Factor

The one-factor model with constant $(\lambda, \sigma)$ generates a swaption volatility matrix with a rigid structure: for fixed expiry, swaption volatilities decrease monotonically with tenor at a rate determined solely by $\lambda$. With two parameters, the model cannot independently control the expiry and tenor dimensions.

The two-factor model has three additional degrees of freedom ($\lambda_2, \sigma_2, \rho$) that act primarily on the tenor dimension:

- $\lambda_2$ controls the decay rate of the second factor's contribution to bond volatility
- $\sigma_2$ controls the magnitude of the second factor's contribution
- $\rho$ controls the cross-correlation between factors

**Proposition.** The two-factor swaption volatility for an $m \times n$ swaption (expiry $m$, tenor $n$) is

$$
(\sigma_S^{(2)})^2 m \approx \sum_{i,j} w_i\,w_j\left[\sigma_1^2 B_x(m, T_i)B_x(m, T_j) + \sigma_2^2 B_y(m, T_i)B_y(m, T_j) + \rho\sigma_1\sigma_2\bigl(B_x(m, T_i)B_y(m, T_j) + B_x(m, T_j)B_y(m, T_i)\bigr)\right]\frac{1-e^{-2\lambda_{\text{eff}}m}}{2\lambda_{\text{eff}}}
$$

where $w_i$ are annuity weights and $T_i$ are the swap payment dates. The additional terms involving $\sigma_2$ and $\rho$ allow independent fitting of the tenor dimension.

## Decorrelation Across Tenors

The key calibration advantage manifests in the off-diagonal swaptions (those where expiry $+$ tenor is not constant). The one-factor model constrains all entries through a single mean-reversion parameter, while the two-factor model can fit:

- **Co-terminal swaptions** (constant $m + n$): primarily constrained by $\lambda_1$ and $\sigma_1$, similar to the one-factor model
- **Constant-expiry swaptions** (fixed $m$, varying $n$): the tenor dependence is enriched by $\lambda_2$ and $\sigma_2$
- **Constant-tenor swaptions** (varying $m$, fixed $n$): the expiry dependence benefits from the interplay of both factors

!!! tip "Typical Market Observation"
    Market swaption volatilities exhibit a hump in the expiry dimension (peaking around 2--5 years) and a gentle decline in the tenor dimension. The one-factor model produces a strictly declining pattern in both dimensions. The two-factor model can capture the hump by assigning appropriate values to $\sigma_1$, $\sigma_2$, and $\rho$.

## Quantitative Comparison

Consider a representative swaption matrix with entries at expiries $\{1, 2, 5, 10\}$ years and tenors $\{1, 2, 5, 10\}$ years (16 entries total).

**One-factor model** ($\lambda, \sigma$, 2 parameters):

$$
\text{RMSE}_{\text{1F}} = \sqrt{\frac{1}{16}\sum_{m,n}\left(\sigma_{m\times n}^{\text{1F}} - \sigma_{m\times n}^{\text{market}}\right)^2} \approx 1\text{--}3\%
$$

The one-factor model typically achieves an RMSE of 1--3 percentage points (in volatility units), with systematic biases along the tenor dimension.

**Two-factor model** ($\lambda_1, \lambda_2, \sigma_1, \sigma_2, \rho$, 5 parameters):

$$
\text{RMSE}_{\text{2F}} = \sqrt{\frac{1}{16}\sum_{m,n}\left(\sigma_{m\times n}^{\text{2F}} - \sigma_{m\times n}^{\text{market}}\right)^2} \approx 0.2\text{--}0.5\%
$$

The two-factor model reduces the RMSE by a factor of 3--10, with residual errors that are unsystematic rather than following a pattern.

## Pricing Implications for Bermudan Swaptions

The swaption matrix fit has direct consequences for Bermudan swaption pricing. A Bermudan swaption on an $n$-year swap with annual exercise depends on the entire co-terminal column of the swaption matrix: the $1 \times (n-1)$, $2 \times (n-2)$, ..., $(n-1) \times 1$ swaptions.

If the model misfits these co-terminal swaptions (as the one-factor model often does for long-tenor swaps), the Bermudan price inherits the bias. The two-factor model's better fit to co-terminal swaptions translates directly to more accurate Bermudan swaption pricing.

**Proposition.** The early exercise premium (EEP) of a Bermudan swaption depends on the correlation between swap rates at different exercise dates. Under the one-factor model, these swap rates are perfectly correlated, underestimating the EEP. Under the two-factor model, the imperfect correlation increases the EEP by 10--30\%, bringing it closer to market-implied values.

## Cap Calibration: Marginal Improvement

For cap calibration, the two-factor model provides a smaller relative improvement. Caps depend on caplet volatilities, which are functions of the short rate distribution at individual reset dates. Since the short rate distribution involves both factors additively:

$$
\text{Var}(r_{T_k}) = \frac{\sigma_1^2}{2\lambda_1}(1 - e^{-2\lambda_1 T_k}) + \frac{\sigma_2^2}{2\lambda_2}(1 - e^{-2\lambda_2 T_k}) + \frac{2\rho\sigma_1\sigma_2}{\lambda_1+\lambda_2}(1 - e^{-(\lambda_1+\lambda_2)T_k})
$$

the two-factor model has more flexibility to fit the caplet volatility term structure, but the additional parameters primarily affect the tenor dimension (which caplets do not probe). The improvement over the one-factor model is typically modest: 20--50\% reduction in RMSE.

## When Is the Second Factor Necessary

The second factor is most valuable when:

1. **Pricing Bermudan swaptions**: the exercise decision depends on the correlation between rate movements at different maturities
2. **Pricing CMS products**: constant maturity swaps depend on the convexity of the swap rate, which is sensitive to correlation
3. **Risk management of large swaption books**: accurate Greeks require a model that fits the volatility surface, not just individual instruments
4. **Joint cap-swaption calibration**: the additional parameters resolve the tension between cap and swaption fitting

The second factor is less necessary when:

- Pricing vanilla caps/floors with short maturities
- Working with a single swaption at a specific expiry/tenor
- Computational speed is critical (two-factor trees have $O(N^2)$ nodes per time step)

???+ example "One-Factor vs Two-Factor Swaption Fit"
    ```python
    def main():
        hw1 = HullWhite(sigma=0.01, lambd=0.05, P=P_market)
        hw2 = HullWhite2(
            sigma1=0.005, sigma2=0.008,
            lambd1=0.02, lambd2=0.3,
            rho=-0.5, P=P_market
        )

        expiries = [1, 2, 5, 10]
        tenors = [1, 2, 5, 10]

        print("Expiry x Tenor | Market | 1F    | 2F    | 1F err | 2F err")
        for m in expiries:
            for n in tenors:
                s_mkt = market_swaption_vol(m, n)
                s_1f = hw1.swaption_vol(m, n)
                s_2f = hw2.swaption_vol(m, n)
                print(f"  {m:2d} x {n:2d}      | {s_mkt:.3f} | "
                      f"{s_1f:.3f} | {s_2f:.3f} | "
                      f"{abs(s_1f-s_mkt):.3f} | {abs(s_2f-s_mkt):.3f}")
    ```

## Summary

The two-factor Hull-White model provides substantial calibration advantages over the one-factor model, primarily in fitting the swaption volatility matrix. The additional parameters $(\lambda_2, \sigma_2, \rho)$ control decorrelation across tenors, reducing the swaption RMSE by a factor of 3--10. The improvement is most significant for off-diagonal swaptions and directly impacts Bermudan swaption pricing, where the early exercise premium depends on cross-maturity rate correlations that the one-factor model sets to unity. For caps, the improvement is more modest. The second factor is most valuable for Bermudan swaptions, CMS products, and risk management of large swaption books.

---

## Exercises

**Exercise 1.** The one-factor Hull-White model with constant $(\sigma, \lambda)$ has 2 free parameters to fit a $4 \times 4$ swaption volatility matrix (16 entries). The two-factor model has 5 parameters. Compute the degrees of freedom (entries minus parameters) for each model. Explain why having more degrees of freedom does not guarantee a worse fit but indicates the model is more constrained.

??? success "Solution to Exercise 1"
    The one-factor model has 2 parameters and 16 swaption entries, giving $16 - 2 = 14$ degrees of freedom (constraints that the model cannot satisfy independently).

    The two-factor model has 5 parameters and 16 entries, giving $16 - 5 = 11$ degrees of freedom.

    Having **more** degrees of freedom (i.e., fewer parameters relative to data points) means the model is **more constrained**, not less. A model with 14 degrees of freedom must satisfy 14 constraints with no free parameters left to adjust, so any structural mismatch between the model's functional form and the market data is directly reflected in the fitting error.

    The two-factor model, with only 11 degrees of freedom, has more flexibility (5 parameters vs. 2) to adjust the fit. However, more parameters do not automatically guarantee a better fit -- they only help if the model's functional form is better aligned with the data. In this case, the two-factor model's ability to decorrelate different tenors addresses a genuine structural limitation of the one-factor model, so the additional parameters do produce a substantially better fit.

    Note: even with 5 parameters, the two-factor model is still heavily over-determined (11 degrees of freedom), so overfitting is not a concern for a $4 \times 4$ matrix.

---

**Exercise 2.** Explain why the one-factor model produces monotonically decreasing swaption volatilities as a function of tenor for fixed expiry. Start from the swaption volatility formula and show that the one-factor bond price volatility $\sigma_P(T_0, T_i) = (\sigma/\lambda)(1 - e^{-\lambda(T_i - T_0)})$ saturates for large $T_i - T_0$. How does this limiting behavior affect the swap rate volatility?

??? success "Solution to Exercise 2"
    In the one-factor model, the swaption volatility for a swap starting at $T_0$ with payment dates $T_1, \ldots, T_n$ depends on the bond price volatilities $\sigma_P(T_0, T_i) = (\sigma/\lambda)(1 - e^{-\lambda(T_i - T_0)})$.

    For large tenor $T_i - T_0$:

    $$
    \sigma_P(T_0, T_i) = \frac{\sigma}{\lambda}(1 - e^{-\lambda(T_i - T_0)}) \to \frac{\sigma}{\lambda} \quad \text{as } T_i - T_0 \to \infty
    $$

    The bond volatility saturates at $\sigma/\lambda$. This means that for long tenors, all payment dates contribute essentially the same bond volatility $\sigma/\lambda$ to the swaption variance.

    The swap rate volatility is approximately a weighted average of the bond volatilities:

    $$
    \sigma_S^2 \approx \frac{1}{A_0^2}\sum_{i,j} w_i w_j\,\sigma_P(T_0, T_i)\,\sigma_P(T_0, T_j)\,\text{corr}
    $$

    Since all bond volatilities converge to the same constant $\sigma/\lambda$ and the one-factor model has perfect correlation, increasing the tenor beyond the saturation point barely changes $\sigma_S$. However, for shorter tenors where the bond volatilities are still increasing, adding more payment dates with slightly higher $\sigma_P$ values increases the average, so $\sigma_S$ decreases as tenor grows (the annuity weight normalization $A_0$ grows faster than the variance sum). This produces the monotonically decreasing pattern in the tenor dimension.

---

**Exercise 3.** The RMSE for the one-factor model is 1--3\% while the two-factor model achieves 0.2--0.5\%. For a 5Y-into-10Y ATM swaption with annuity $A_0 = 7.5$ and forward swap rate $S_0 = 3.5\%$, estimate the pricing error (in basis points of annuity value) that a 2\% volatility error implies. Is this error economically significant for a \$100M notional trade?

??? success "Solution to Exercise 3"
    The swaption price in a Black-type formula is approximately:

    $$
    V_{\text{swaption}} \approx A_0 \cdot S_0 \cdot \sigma_S \sqrt{T_m} \cdot N'(0) = A_0 \cdot S_0 \cdot \sigma_S \sqrt{T_m} \cdot \frac{1}{\sqrt{2\pi}}
    $$

    for an ATM swaption (using the leading-order approximation).

    A volatility error of $\Delta\sigma = 2\% = 0.02$ translates to a pricing error of approximately:

    $$
    \Delta V \approx A_0 \cdot S_0 \cdot \Delta\sigma \cdot \sqrt{T_m} \cdot \frac{1}{\sqrt{2\pi}}
    $$

    With $A_0 = 7.5$, $S_0 = 0.035$, $\Delta\sigma = 0.02$, $T_m = 5$:

    $$
    \Delta V \approx 7.5 \times 0.035 \times 0.02 \times \sqrt{5} \times 0.3989 \approx 7.5 \times 0.035 \times 0.02 \times 2.236 \times 0.3989
    $$

    $$
    \approx 7.5 \times 0.035 \times 0.01784 \approx 0.004685
    $$

    In basis points of annuity value, this is $\Delta V / A_0 \approx 0.004685/7.5 \approx 0.000625 = 6.25$ basis points.

    For a \$100M notional trade:

    $$
    \text{Pricing error} = 100{,}000{,}000 \times 0.004685 = \$468{,}500
    $$

    This is economically significant -- nearly half a million dollars. For a large trading desk with many such positions, systematic model-driven pricing errors of this magnitude would materially affect P&L and risk management.

---

**Exercise 4.** A Bermudan swaption exercisable annually on a 10-year swap depends on the co-terminal European swaptions: $1 \times 9$, $2 \times 8$, ..., $9 \times 1$. If the one-factor model overstates the $1 \times 9$ vol by 1.5\% and understates the $9 \times 1$ vol by 1\%, explain qualitatively how these errors affect the Bermudan exercise boundary and the resulting Bermudan price. Would the one-factor model overprice or underprice the Bermudan?

??? success "Solution to Exercise 4"
    The one-factor model overstates the $1 \times 9$ vol (short expiry, long tenor) and understates the $9 \times 1$ vol (long expiry, short tenor). Consider the effects:

    **Impact on early exercise dates** (near the $1 \times 9$ end): The model overstates the volatility of the swap rate at early exercise dates. This makes early exercise options appear more valuable than they actually are, biasing the exercise boundary toward earlier exercise.

    **Impact on late exercise dates** (near the $9 \times 1$ end): The model understates the volatility at late exercise dates, making late exercise options appear less valuable than they are.

    **Net effect on the Bermudan price:** The Bermudan value is the maximum over all exercise strategies. The one-factor model overvalues early exercise (overstated early vols) and undervalues late exercise (understated late vols). The net effect depends on which error dominates.

    In practice, the Bermudan is most often exercised at intermediate dates, and the exercise premium depends on the **difference** in value between exercising now versus waiting. Since the one-factor model produces perfect correlation between swap rates at different dates, it underestimates the optionality of waiting (imperfect correlation means waiting has more value since rates might move favorably). The one-factor model therefore tends to **underprice** the Bermudan swaption because it underestimates the early exercise premium, despite overstating some individual co-terminal vols.

---

**Exercise 5.** The proposition states that the early exercise premium (EEP) is 10--30\% higher under the two-factor model than the one-factor model. Explain the economic mechanism: how does imperfect correlation between swap rates at different exercise dates increase the option value of early exercise?

??? success "Solution to Exercise 5"
    The early exercise premium (EEP) represents the additional value of being able to exercise before the final date compared to a European option at that date. The EEP depends on the option value of **waiting** versus exercising immediately.

    Under the **one-factor model**, swap rates at different exercise dates are perfectly correlated. This means that if the current swap rate makes exercise profitable, the future swap rate will almost surely move in the same direction. There is little benefit to waiting because the situation is unlikely to change qualitatively -- rates either stay favorable or unfavorable across all exercise dates simultaneously.

    Under the **two-factor model**, swap rates at different exercise dates are imperfectly correlated ($\text{Corr} < 1$). This creates scenarios where:

    - The swap rate is currently marginal (near the exercise boundary), and the holder benefits from waiting because future rate movements are not perfectly predictable from the current state.
    - The swap rate may be unfavorable now but could become favorable later due to the independent component of rate movements (driven by the second factor).
    - The decorrelation between short and long rates means that the swap rate at one exercise date provides incomplete information about the swap rate at a later date.

    This increased uncertainty about future exercise values raises the **continuation value** -- the option to wait is worth more when future outcomes are less predictable. Since the Bermudan price is $\max(\text{exercise value}, \text{continuation value})$, a higher continuation value raises the overall Bermudan price, increasing the EEP by 10--30% relative to the one-factor model.

---

**Exercise 6.** For cap calibration, the short rate variance is

$$
\text{Var}(r_{T_k}) = \frac{\sigma_1^2}{2\lambda_1}(1 - e^{-2\lambda_1 T_k}) + \frac{\sigma_2^2}{2\lambda_2}(1 - e^{-2\lambda_2 T_k}) + \frac{2\rho\sigma_1\sigma_2}{\lambda_1+\lambda_2}(1 - e^{-(\lambda_1+\lambda_2)T_k})
$$

Show that for $T_k \to \infty$, the stationary variance depends on all five parameters. For typical two-factor parameters $\lambda_1 = 0.02$, $\lambda_2 = 0.3$, which terms dominate the short-horizon caplet variance ($T_k = 0.5$) and which dominate the long-horizon caplet variance ($T_k = 10$)?

??? success "Solution to Exercise 6"
    As $T_k \to \infty$, each exponential term converges: $e^{-2\lambda_1 T_k} \to 0$, $e^{-2\lambda_2 T_k} \to 0$, $e^{-(\lambda_1+\lambda_2)T_k} \to 0$. The stationary variance is:

    $$
    \text{Var}(r_\infty) = \frac{\sigma_1^2}{2\lambda_1} + \frac{\sigma_2^2}{2\lambda_2} + \frac{2\rho\sigma_1\sigma_2}{\lambda_1+\lambda_2}
    $$

    This depends on all five parameters $(\sigma_1, \sigma_2, \lambda_1, \lambda_2, \rho)$.

    **Short-horizon caplet variance ($T_k = 0.5$):** Using Taylor expansions $e^{-2\lambda T_k} \approx 1 - 2\lambda T_k$:

    $$
    \frac{\sigma_i^2}{2\lambda_i}(1 - e^{-2\lambda_i T_k}) \approx \frac{\sigma_i^2}{2\lambda_i} \cdot 2\lambda_i T_k = \sigma_i^2 T_k
    $$

    With $\lambda_1 = 0.02$, $\lambda_2 = 0.3$, and $T_k = 0.5$:

    - Factor 1: $\frac{\sigma_1^2}{2\lambda_1}(1 - e^{-0.02}) \approx \sigma_1^2 \times 0.5 = 0.5\sigma_1^2$
    - Factor 2: $\frac{\sigma_2^2}{2\lambda_2}(1 - e^{-0.3}) \approx \frac{\sigma_2^2}{0.6}(0.2592) = 0.432\sigma_2^2$

    Both factors contribute roughly equally (proportional to $\sigma_i^2$) at short horizons, since the mean reversion has not had time to act.

    **Long-horizon caplet variance ($T_k = 10$):**

    - Factor 1: $\frac{\sigma_1^2}{2\lambda_1}(1 - e^{-0.4}) = \frac{\sigma_1^2}{0.04}(0.3297) = 8.24\sigma_1^2$
    - Factor 2: $\frac{\sigma_2^2}{2\lambda_2}(1 - e^{-6}) \approx \frac{\sigma_2^2}{0.6}(0.9975) = 1.663\sigma_2^2$

    At long horizons, the first factor (slow mean reversion) dominates because its variance accumulates more before saturating. The ratio of factor 1 to factor 2 contribution is $8.24\sigma_1^2 / (1.663\sigma_2^2)$. With comparable $\sigma_1$ and $\sigma_2$, the slow factor dominates by a factor of about 5.

---

**Exercise 7.** A risk manager must decide whether to use a one-factor or two-factor Hull-White model for a book containing caps, European swaptions, and Bermudan swaptions. For each product type, assess whether the two-factor model provides a material improvement. Under what circumstances would the computational cost of the two-factor model (roughly $10 \times$ for trees) not be justified?

??? success "Solution to Exercise 7"
    **Caps:** The two-factor model provides a **marginal improvement** (20--50% RMSE reduction). Caps depend on the marginal distribution of the short rate at each reset date, which involves both factors additively. The additional flexibility in fitting the caplet term structure is modest because caps do not probe the correlation structure across maturities. **Recommendation:** The one-factor model is often adequate for a cap-only book.

    **European swaptions:** The two-factor model provides a **significant improvement** (3--10x RMSE reduction). Swaptions depend on the joint distribution of bond prices across the swap tenor, making them sensitive to the cross-maturity correlation structure. The one-factor model's perfect correlation leads to systematic biases in the tenor dimension. **Recommendation:** The two-factor model is strongly preferred for a swaption book, especially when fitting across multiple tenors.

    **Bermudan swaptions:** The two-factor model provides the **most critical improvement**. The early exercise premium depends on the correlation between swap rates at different exercise dates. The one-factor model underestimates this premium by 10--30%. Since Bermudans are typically the most complex and largest-notional products in an interest rate book, pricing accuracy is paramount. **Recommendation:** The two-factor model is essential for Bermudan swaptions.

    **When the two-factor model is NOT justified:**

    - A book consisting entirely of **short-dated caps/floors** (maturities under 2 years), where the second factor has minimal impact.
    - **Intraday risk monitoring** where speed is critical and approximate Greeks suffice -- the $10\times$ computational cost may be prohibitive for real-time P&L.
    - **Simple hedging** of a single European swaption at one specific expiry/tenor, where the one-factor model can be locally calibrated to that single instrument.
    - When the **parameter stability** of the two-factor model is poor -- with 5 parameters and noisy market data, the calibration can be unstable, and the additional parameters may introduce more noise than signal into hedging ratios.
