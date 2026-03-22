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
