# Progressive vs Initial Enlargement

There are two main ways to enlarge a filtration to include a default time: **progressive enlargement** and **initial enlargement**. They differ in how information about default is revealed.

---

## 1. Progressive enlargement

In **progressive enlargement**, information about default is revealed only when it occurs.

The enlarged filtration is
\[
\mathcal{G}_t = \mathcal{F}_t \vee \sigma(\tau \wedge t).
\]

Properties:
- default time \(\tau\) becomes a stopping time,
- market participants do not know \(\tau\) in advance,
- this is the standard approach in reduced-form credit models.

---

## 2. Initial enlargement

In **initial enlargement**, the default time is known from time 0:
\[
\mathcal{G}_t = \mathcal{F}_t \vee \sigma(\tau).
\]

This is mathematically convenient but financially unrealistic for default modeling.

---

## 3. Financial interpretation

- Progressive enlargement reflects surprise default.
- Initial enlargement corresponds to insider information.
- Pricing and hedging results differ substantially between the two.

---

## 4. Modeling implications

Most credit risk models assume progressive enlargement because:
- it preserves causality,
- it matches observed market behavior,
- it supports intensity-based default modeling.

Initial enlargement is mainly used for theoretical analysis.

---

## 5. Key takeaways

- Progressive enlargement reveals default information gradually.
- Initial enlargement assumes full knowledge of default time.
- Credit models almost always use progressive enlargement.

---

## Further reading

- Jeulin & Yor, enlargement of filtrations.
- Bielecki & Rutkowski, credit risk frameworks.
