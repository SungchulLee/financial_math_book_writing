# Girsanov’s Theorem 


Girsanov’s theorem describes how a change of probability measure modifies the drift
of a stochastic process while preserving its Brownian structure.

---

## Setting


Let \((\Omega, \mathcal{F}, \{\mathcal{F}_t\}, \mathbb{P})\) be a filtered probability space
supporting a standard Brownian motion \(W_t\).

Let \(\theta_t\) be an adapted process satisfying the Novikov condition

\[
\mathbb{E}^{\mathbb{P}}\!\left[
\exp\!\left(\frac12 \int_0^T \theta_s^2 ds\right)
\right] < \infty
\]

---

## Exponential Martingale


Define

\[
Z_t
=
\exp\!\left(
-\int_0^t \theta_s\, dW_s
-\frac12 \int_0^t \theta_s^2 ds
\right)
\]

Then \(Z_t\) is a strictly positive \(\mathbb{P}\)-martingale with
\(\mathbb{E}^{\mathbb{P}}[Z_t] = 1\).

---

## Measure Change


Define a new probability measure \(\mathbb{Q}\) on \(\mathcal{F}_T\) by

\[
\frac{d\mathbb{Q}}{d\mathbb{P}}\Big|_{\mathcal{F}_T} = Z_T
\]

---

## Theorem (Girsanov)


Under the measure \(\mathbb{Q}\), the process

\[
\widetilde W_t := W_t + \int_0^t \theta_s ds
\]

is a standard Brownian motion.

---

## Interpretation


- Under \(\mathbb{P}\): \(W_t\) is Brownian, \(\widetilde W_t\) has drift
- Under \(\mathbb{Q}\): \(\widetilde W_t\) is Brownian

The drift has been transferred from the process to the probability measure.
