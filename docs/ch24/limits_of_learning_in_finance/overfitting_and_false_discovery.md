# Overfitting and False Discovery


**Overfitting** and **false discovery** are pervasive risks in financial learning due to noisy data and multiple testing.

---

## Overfitting in finance


Overfitting occurs when a model:
- fits noise rather than signal,
- performs well in-sample,
- fails out-of-sample.

Limited data and heavy noise exacerbate the problem.

---

## Multiple testing and data snooping


Financial research often involves:
- testing many strategies,
- selecting the best-performing ones,
- ignoring failed experiments.

This leads to false discoveries.

---

## Consequences


False discoveries result in:
- spurious trading strategies,
- inflated backtest performance,
- real-world losses when deployed.

They undermine confidence in models.

---

## Mitigation techniques


Common defenses include:
- out-of-sample validation,
- cross-validation adapted to time series,
- statistical corrections for multiple testing,
- economic plausibility checks.

Discipline is crucial.

---

## Key takeaways


- Overfitting is endemic in finance.
- Multiple testing inflates false positives.
- Rigorous validation is essential.

---

## Further reading


- Bailey et al., backtest overfitting.
- Harvey, Liu & Zhu, false discoveries.
