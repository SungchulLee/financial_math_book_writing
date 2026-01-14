# Proof Sketch and Key Ideas


This section outlines the main ideas behind the proof of Girsanov’s theorem,
without dwelling on technical details.

---

## Step 1: Martingale Property of the Density


Applying Itô’s formula to the exponential martingale \(Z_t\) gives

\[
dZ_t = - Z_t \theta_t \, dW_t
\]

There is no \(dt\) term, so \(Z_t\) is a local martingale.
The Novikov condition ensures it is a true martingale with unit expectation.

---

## Step 2: Martingale Property of the Shifted Process


Define

\[
\widetilde W_t = W_t + \int_0^t \theta_s ds
\]

Using the definition of conditional expectation under \(\mathbb{Q}\),
one verifies that \(\widetilde W_t\) has zero conditional drift.

Thus, \(\widetilde W_t\) is a \(\mathbb{Q}\)-martingale.

---

## Step 3: Quadratic Variation


Quadratic variation is a pathwise property and is unaffected by a change of measure.

Since the integral term has finite variation,

\[
\langle \widetilde W \rangle_t = \langle W \rangle_t = t
\]

---

## Step 4: Lévy Characterization


A continuous martingale with quadratic variation \(t\) is a Brownian motion.

Therefore, \(\widetilde W_t\) is a standard Brownian motion under \(\mathbb{Q}\).

---

## Key Insight


The proof shows that:

- drift is removed by reweighting paths,
- volatility and information structure remain unchanged.

This is why Girsanov’s theorem is so powerful in applications.
