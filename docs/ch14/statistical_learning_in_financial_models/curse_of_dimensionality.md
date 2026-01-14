# Curse of Dimensionality


The **curse of dimensionality** describes the exponential growth in data requirements and computational complexity as the number of input dimensions increases.

---

## What is the curse?


In high dimensions:
- data becomes sparse,
- distances lose meaning,
- local methods degrade rapidly.

This affects most nonparametric learning methods.

---

## Manifestations


Key consequences include:
- slow convergence rates,
- unstable estimates,
- need for exponentially more data.

Even moderate dimensions can be problematic.

---

## Financial data challenges


In finance:
- many risk factors are observed,
- effective sample sizes are small,
- dependencies are complex.

This makes naive high-dimensional learning unreliable.

---

## Mitigation strategies


Common approaches include:
- dimensionality reduction (PCA, factors),
- regularization and sparsity,
- domain-informed feature selection.

Structure is essential to overcome dimensionality.

---

## Key takeaways


- High dimensionality severely degrades learning.
- Data requirements grow exponentially.
- Structure and regularization are essential.

---

## Further reading


- Bellman, curse of dimensionality.
- Fan et al., high-dimensional statistics.
