# Stopping Times and Enlargement of Filtration

Credit risk models often represent default as a **random time**. To incorporate default into a stochastic framework, one must understand stopping times and the enlargement of filtrations.

---

## 1. Filtrations and information flow

A filtration \((\mathcal{F}_t)_{t \ge 0}\) represents the information available up to time \(t\).
In default-free models, \(\mathcal{F}_t\) typically contains information about market factors such as prices and rates.

Introducing default requires expanding this information set.

---

## 2. Default time as a stopping time

A random time \(\tau\) is a **stopping time** with respect to a filtration \((\mathcal{G}_t)\) if
\[
\{\tau \le t\} \in \mathcal{G}_t \quad \text{for all } t.
\]

Interpreting default as a stopping time ensures that the occurrence of default is observable when it happens.

---

## 3. Enlargement of filtration

To model default, we enlarge the default-free filtration \((\mathcal{F}_t)\) to a larger filtration \((\mathcal{G}_t)\) such that:
- \(\tau\) is a stopping time in \((\mathcal{G}_t)\),
- \(\mathcal{F}_t \subseteq \mathcal{G}_t\).

This process is known as **enlargement of filtration**.

---

## 4. Financial interpretation

Enlargement formalizes:
- the arrival of default information,
- the distinction between pre-default and post-default dynamics,
- consistency of pricing and hedging with observed default events.

---

## 5. Key takeaways

- Default is modeled as a random time \(\tau\).
- To observe default, the filtration must be enlarged.
- Filtration enlargement formalizes new information arrival.

---

## Further reading

- Jeanblanc, Yor & Chesney, *Mathematical Methods for Financial Markets*.
- Bielecki & Rutkowski, *Credit Risk*.
