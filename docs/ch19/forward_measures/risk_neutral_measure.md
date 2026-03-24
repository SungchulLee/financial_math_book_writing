# Risk-Neutral Measure


The **risk-neutral measure** is the cornerstone of arbitrage-free pricing. Under this measure, discounted asset prices are martingales, allowing derivative prices to be expressed as discounted expectations.

---

## Numéraire and probability measure


Let \(B_t\) denote the money-market account:

\[
dB_t = r_t B_t\,dt, \qquad B_0=1.
\]



A probability measure \(\mathbb{Q}\) is **risk-neutral** if, for any tradable asset with price \(S_t\),

\[
\frac{S_t}{B_t} \text{ is a martingale under } \mathbb{Q}.
\]



---

## Fundamental pricing formula


Under the risk-neutral measure,

\[
V_t = \mathbb{E}^{\mathbb{Q}}\left[
e^{-\int_t^T r_s ds} \, V_T
\middle| \mathcal{F}_t
\right],
\]


where \(V_T\) is the payoff at maturity.

This formula applies to bonds, options, and general derivatives.

---

## Change of measure intuition


The risk-neutral measure:
- absorbs risk premia into the drift,
- leaves diffusion terms unchanged,
- simplifies pricing to expectation of discounted cashflows.

It is not the physical (real-world) probability measure.

---

## Interest-rate context


In interest-rate models:
- the short rate \(r_t\) determines discounting,
- \(\mathbb{Q}\)-dynamics are calibrated to prices,
- physical dynamics are relevant for risk management, not pricing.

---

## Key takeaways


- Risk-neutral measure enforces arbitrage-free pricing.
- Discounted prices are martingales under \(\mathbb{Q}\).
- Pricing reduces to discounted expectation.

---

## Further reading


- Harrison & Pliska, martingale pricing.
- Björk, *Arbitrage Theory in Continuous Time*.

---

## Exercises

**Exercise 1.** Under the risk-neutral measure $\mathbb{Q}$, the short rate follows the Vasicek model $dr_t = a(b - r_t)\,dt + \sigma\,dW_t^{\mathbb{Q}}$. Using the pricing formula

$$
P(t, T) = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_t^T r_s\,ds}\;\middle|\;\mathcal{F}_t\right],
$$

explain why the bond price depends on $r_t$ but not on the physical drift parameters. What role does the risk-neutral drift $a(b - r_t)$ play in determining bond prices?

---

**Exercise 2.** Show that if $S_t$ is a tradable asset (with no dividends) and $B_t = \exp(\int_0^t r_s\,ds)$, then the discounted price $\tilde{S}_t = S_t / B_t$ being a $\mathbb{Q}$-martingale implies that

$$
S_0 = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_0^T r_s\,ds}\,S_T\right]
$$

Verify this identity for the special case where $r_t = r$ is constant and $S_t$ follows geometric Brownian motion.

---

**Exercise 3.** Under the physical (real-world) measure $\mathbb{P}$, a stock follows $dS_t = \mu S_t\,dt + \sigma S_t\,dW_t^{\mathbb{P}}$ with $\mu = 10\%$ and $\sigma = 25\%$. The risk-free rate is $r = 3\%$. Identify the market price of risk $\lambda = (\mu - r)/\sigma$ and write down the stock dynamics under $\mathbb{Q}$. Verify that the discounted stock price is a $\mathbb{Q}$-martingale.

---

**Exercise 4.** Consider a digital option that pays \$1 at time $T$ if $r_T > K$ and nothing otherwise. Express the price as a risk-neutral expectation:

$$
V_0 = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_0^T r_s\,ds}\,\mathbf{1}_{\{r_T > K\}}\right]
$$

Explain why this expectation cannot be simplified by pulling the discount factor outside the indicator function. Contrast this with the simplification possible under the $T$-forward measure.

---

**Exercise 5.** In a two-period binomial model, the risk-free rate is $r = 2\%$ per period, the up factor is $u = 1.10$, and the down factor is $d = 0.92$. Compute the risk-neutral probability $q = (1+r-d)/(u-d)$ and price a European call option with strike $K = 105$ on a stock with $S_0 = 100$. Verify that the discounted stock price is a martingale under $q$.

---

**Exercise 6.** Explain why the risk-neutral measure $\mathbb{Q}$ is unique in a complete market but not unique in an incomplete market. In the context of interest-rate modeling, give an example of a situation where market incompleteness arises and discuss how practitioners resolve the non-uniqueness of $\mathbb{Q}$.
