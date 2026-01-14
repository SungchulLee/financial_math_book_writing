# Forward Smile


The **forward smile** describes the implied volatility surface of forward-start options or, equivalently, the conditional distribution of future returns implied by today’s option prices. It plays a key role in understanding smile dynamics over time.

---

## From spot smile to forward smile


The spot implied volatility smile \(\sigma_{\text{impl}}(K,T)\) reflects the marginal distribution of \(S_T\).
The forward smile captures the distribution of returns over \([T_1,T_2]\) conditional on information at time \(T_1\).

Formally, it is linked to the law of

\[
\log\left(\frac{S_{T_2}}{S_{T_1}}\right) \mid \mathcal{F}_{T_1}.
\]



---

## Forward-start options


Forward smiles can be accessed through **forward-start options**, whose payoff depends on future spot levels:

\[
(S_{T_2} - K S_{T_1})^+.
\]



Their implied volatility surface reveals how today’s model extrapolates smile dynamics into the future.

---

## Model implications


Different models imply different forward smiles:

- **Black–Scholes:** flat forward smile.
- **Local volatility:** forward smile flattens quickly.
- **Stochastic volatility:** persistent forward skew and curvature.

Thus, forward smiles are powerful model discriminators.

---

## Practical relevance


Forward smiles matter for:
- cliquets and forward-start products,
- long-dated exotics,
- assessing dynamic consistency of a volatility model.

---

## Key takeaways


- Forward smiles encode conditional future volatility distributions.
- They are not directly observable but model-implied.
- Forward smile behavior reveals strengths and weaknesses of models.

---

## Further reading


- Bergomi, *Smile Dynamics*.
- Gatheral, *The Volatility Surface*.
