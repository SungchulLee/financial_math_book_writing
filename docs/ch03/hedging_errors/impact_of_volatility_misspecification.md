# Impact of Volatility Misspecification

If the hedger uses \(\hat{\sigma}\) while true volatility is \(\sigma\), replication fails systematically. A classical heuristic term is
\[
\boxed{
\frac{1}{2}\int_0^T \Gamma(t,S_t)\left(\sigma^2-\hat{\sigma}^2\right)S_t^2\,\mathrm{d}t.
}
\]
For \(\Gamma>0\), underestimating volatility tends to lose money and overestimating tends to gain (ignoring other effects).

---

## What to remember

- Gamma converts variance mismatch into systematic hedging P\&L drift.
- This motivates implied-vs-realized volatility trading intuition.
