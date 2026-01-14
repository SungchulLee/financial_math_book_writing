# Entropy Penalization


**Entropy penalization** provides a smooth alternative to max–min preferences by penalizing deviations from a reference probability measure.

---

## Motivation


Pure max–min preferences can be:
- overly conservative,
- difficult to calibrate,
- unstable in practice.

Entropy penalties soften worst-case behavior.

---

## Relative entropy


The relative entropy (KL divergence) between \(\mathbb{Q}\) and \(\mathbb{P}\) is

\[
H(\mathbb{Q} \mid \mathbb{P})
= \mathbb{E}_{\mathbb{Q}}\left[
\log \frac{d\mathbb{Q}}{d\mathbb{P}}
\right].
\]



It measures statistical distance between models.

---

## Penalized objective


Preferences are defined by

\[
\max_{\pi} \; \min_{\mathbb{Q}}
\left\{
\mathbb{E}_{\mathbb{Q}}[U(X^{\pi})]
+ \lambda H(\mathbb{Q} \mid \mathbb{P})
\right\}.
\]



The parameter \(\lambda\) controls ambiguity aversion.

---

## Financial interpretation


Entropy penalization:
- favors models close to the reference,
- allows tractable optimization,
- connects to exponential utility and risk-sensitive control.

---

## Key takeaways


- Entropy penalties soften worst-case preferences.
- Ambiguity aversion is tunable.
- The approach is mathematically tractable.

---

## Further reading


- Hansen & Sargent, entropy methods.
- Dupuis & Ellis, risk-sensitive control.
