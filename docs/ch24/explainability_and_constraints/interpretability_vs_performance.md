# Interpretability vs Performance


In financial machine learning, there is a persistent tension between **model interpretability** and **predictive performance**. Managing this trade-off is central to responsible model deployment.

---

## What is interpretability?


Interpretability refers to the ability to:
- understand how inputs affect outputs,
- explain model decisions to stakeholders,
- diagnose errors and instability.

Linear and sparse models are typically highly interpretable.

---

## Performance-driven models


High-performance models include:
- deep neural networks,
- ensemble methods,
- highly nonlinear learners.

They often achieve superior predictive accuracy but operate as black boxes.

---

## Financial and regulatory context


In finance:
- models affect capital, pricing, and risk limits,
- regulators require explainability,
- senior management must understand model behavior.

Pure black-box approaches are often unacceptable.

---

## Practical trade-offs


Institutions balance:
- slightly lower accuracy for higher transparency,
- model simplicity for robustness,
- explainability for governance and trust.

Interpretability is a form of risk control.

---

## Key takeaways


- Interpretability and performance often conflict.
- Finance prioritizes explainability and stability.
- Model choice reflects governance constraints.

---

## Further reading


- Rudin, interpretable machine learning.
- Molnar, *Interpretable Machine Learning*.

---

## Exercises

**Exercise 1.** A bank evaluates two models for credit scoring: a logistic regression (AUC = 0.78, fully interpretable) and a gradient-boosted tree ensemble (AUC = 0.83, limited interpretability). The regulatory framework requires explanations for adverse credit decisions. Discuss the tradeoffs and propose a deployment strategy that balances accuracy and explainability. Under what circumstances would you recommend the simpler model despite its lower AUC?

---

**Exercise 2.** Define interpretability at three levels: (a) global interpretability (understanding the overall model behavior), (b) local interpretability (explaining a single prediction), and (c) feature importance (ranking input contributions). For a deep neural network predicting VaR, discuss which level of interpretability is most critical for (i) the risk manager, (ii) the regulator, and (iii) the model validator.

---

**Exercise 3.** A model validator must choose between a simple linear factor model with 5 features and a deep network with 200 features for predicting portfolio returns. The deep network achieves 15% lower out-of-sample MSE. Discuss: (a) what additional validation burden the complex model creates, (b) how overfitting risk differs between the two, and (c) whether the 15% improvement justifies the loss of interpretability in a risk management context.

---

**Exercise 4.** Explain how post-hoc explanation methods (e.g., SHAP, LIME) can make black-box models partially interpretable without sacrificing predictive performance. What are the limitations of these approaches? Can a post-hoc explanation faithfully represent the model's true decision process, or might it be misleading?

---

**Exercise 5.** The concept of "right to explanation" in financial regulation (e.g., ECOA in the US, GDPR in the EU) requires that individuals affected by automated decisions receive meaningful explanations. For a neural network credit model that denies a loan application, describe what constitutes a "meaningful explanation." How does this requirement practically constrain model choice?

---

**Exercise 6.** Argue that interpretability can be viewed as a form of regularization. A highly interpretable model (e.g., sparse linear) has fewer effective parameters and thus lower variance. Provide a concrete example where an interpretable model outperforms a complex model on out-of-sample data due to overfitting of the complex model. How does this challenge the assumption that performance and interpretability always conflict?

---

**Exercise 7.** A quantitative hedge fund has no regulatory interpretability requirements and values only predictive alpha. Discuss whether interpretability still matters in this context. Consider: (a) debugging model failures, (b) understanding regime changes, (c) building intuition for risk management, and (d) communicating with investors. Argue that even in unregulated settings, some degree of model understanding is essential for robust operation.
