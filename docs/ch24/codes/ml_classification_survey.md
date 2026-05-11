# Machine Learning Classification Survey

## Background

Ml Classification Survey

Educational script demonstrating ml classification survey concepts.

---

## Code

```python
"""
Ml Classification Survey

Educational script demonstrating ml classification survey concepts.
"""

# ---
# title: "Machine Learning Classification Survey"
# description: >
#   A compact survey of supervised and unsupervised ML methods
#   applied to synthetic financial-style data:
#
#   Unsupervised:
#     - K-Means clustering
#     - Gaussian Mixture Model
#
#   Supervised (binary classification):
#     - Gaussian Naive Bayes
#     - Logistic Regression
#     - Decision Tree (with depth sweep)
#     - Multi-Layer Perceptron (scikit-learn)
#     - Support Vector Machine (with kernel comparison)
#
#   Also covers feature preprocessing (standardisation,
#   min-max scaling, normalisation, binarisation) and
#   train/test splitting for honest accuracy evaluation.
#
# origin: "Adapted from Y. Hilpisch, Python for Finance, 2nd ed."
# ---

import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import make_blobs, make_classification
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn import preprocessing


# ══════════════════════════════════════════════════════════════════
#  Helper: scatter with correct / incorrect markers
# ══════════════════════════════════════════════════════════════════

# ======================================================================

def plot_classification(X, y, pred, title=''):
    """Scatter true-class colours; circles = correct, × = wrong."""
    correct = (y == pred)
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.scatter(X[correct, 0], X[correct, 1], c=y[correct],
               marker='o', cmap='coolwarm', alpha=0.7, label='Correct')
    ax.scatter(X[~correct, 0], X[~correct, 1], c=y[~correct],
               marker='x', cmap='coolwarm', s=80, label='Incorrect')
    ax.set_title(title)
    ax.legend()
    ax.grid(alpha=0.3)
    plt.tight_layout()
    plt.show()


# ══════════════════════════════════════════════════════════════════
#  1. Unsupervised Learning
# ══════════════════════════════════════════════════════════════════

def demo_unsupervised():
    print("=" * 50)
    print("1. Unsupervised Learning")
    print("=" * 50)

    X, y_true = make_blobs(n_samples=250, centers=4,
                           random_state=500, cluster_std=1.25)

    # K-Means
    km = KMeans(n_clusters=4, random_state=0, n_init=10)
    y_km = km.fit_predict(X)

    # Gaussian Mixture
    gm = GaussianMixture(n_components=4, random_state=0)
    y_gm = gm.fit_predict(X)

    print(f"K-Means and GMM agree on all labels: "
          f"{(y_km == y_gm).all()}")

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    ax1.scatter(X[:, 0], X[:, 1], c=y_km, cmap='coolwarm')
    ax1.set_title('K-Means Clustering')
    ax1.grid(alpha=0.3)
    ax2.scatter(X[:, 0], X[:, 1], c=y_gm, cmap='coolwarm')
    ax2.set_title('Gaussian Mixture Model')
    ax2.grid(alpha=0.3)
    plt.tight_layout()
    plt.show()


# ══════════════════════════════════════════════════════════════════
#  2. Supervised Learning
# ══════════════════════════════════════════════════════════════════

def demo_supervised():
    print("\n" + "=" * 50)
    print("2. Supervised Learning")
    print("=" * 50)

    np.random.seed(250)
    X, y = make_classification(n_samples=100, n_features=2,
                               n_informative=2, n_redundant=0,
                               n_repeated=0, random_state=250)

    classifiers = {
        'Gaussian NB': GaussianNB(),
        'Logistic Regression': LogisticRegression(C=1, max_iter=500),
        'Decision Tree (d=3)': DecisionTreeClassifier(max_depth=3),
        'MLP (2×75)': MLPClassifier(
            solver='lbfgs', alpha=1e-5, max_iter=500,
            hidden_layer_sizes=(75, 75), random_state=10),
    }

    print(f"\n{'Classifier':<25s}  {'Accuracy':>8s}")
    print('-' * 36)
    for name, clf in classifiers.items():
        clf.fit(X, y)
        pred = clf.predict(X)
        acc = accuracy_score(y, pred)
        print(f"{name:<25s}  {acc:8.2%}")
        plot_classification(X, y, pred, title=f'{name}  (acc={acc:.2%})')

    # Decision tree depth sweep
    print("\nDecision Tree — depth sweep:")
    print(f"  {'Depth':>5s}  {'Accuracy':>8s}")
    print('  ' + '-' * 16)
    for depth in range(1, 7):
        dt = DecisionTreeClassifier(max_depth=depth)
        dt.fit(X, y)
        acc = accuracy_score(y, dt.predict(X))
        print(f"  {depth:5d}  {acc:8.2%}")


# ══════════════════════════════════════════════════════════════════
#  3. Feature Preprocessing
# ══════════════════════════════════════════════════════════════════

def demo_preprocessing():
    print("\n" + "=" * 50)
    print("3. Feature Preprocessing")
    print("=" * 50)

    np.random.seed(250)
    X, y = make_classification(n_samples=100, n_features=2,
                               n_informative=2, n_redundant=0,
                               n_repeated=0, random_state=250)

    transforms = {
        'Raw': X,
        'StandardScaler': preprocessing.StandardScaler().fit_transform(X),
        'MinMaxScaler': preprocessing.MinMaxScaler().fit_transform(X),
        'Normalizer(L1)': preprocessing.Normalizer(norm='l1').transform(X),
        'Normalizer(L2)': preprocessing.Normalizer(norm='l2').transform(X),
    }

    fig, ax = plt.subplots(figsize=(10, 6))
    markers = ['o', '.', 'x', '^', 'v']
    for (label, Xt), m in zip(transforms.items(), markers):
        ax.scatter(Xt[:, 0], Xt[:, 1], c=y, marker=m,
                   cmap='coolwarm', label=label, alpha=0.6)
    ax.legend()
    ax.set_title('Effect of Feature Transforms')
    ax.grid(alpha=0.3)
    plt.tight_layout()
    plt.show()


# ══════════════════════════════════════════════════════════════════
#  4. Train-Test Split & SVM Kernel Comparison
# ══════════════════════════════════════════════════════════════════

def demo_train_test():
    print("\n" + "=" * 50)
    print("4. Train/Test Split & SVM Kernels")
    print("=" * 50)

    np.random.seed(250)
    X, y = make_classification(n_samples=100, n_features=2,
                               n_informative=2, n_redundant=0,
                               n_repeated=0, random_state=250)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.33, random_state=0)

    print(f"\n{'Kernel':>8s}  {'Train acc':>9s}  {'Test acc':>9s}")
    print('-' * 32)
    for kernel in ['linear', 'poly', 'rbf', 'sigmoid']:
        svc = SVC(C=1, kernel=kernel)
        svc.fit(X_train, y_train)
        tr_acc = accuracy_score(y_train, svc.predict(X_train))
        te_acc = accuracy_score(y_test, svc.predict(X_test))
        print(f"{kernel:>8s}  {tr_acc:9.3f}  {te_acc:9.3f}")

    # Best linear SVM: plot test set
    svc_lin = SVC(C=1, kernel='linear').fit(X_train, y_train)
    pred_test = svc_lin.predict(X_test)
    plot_classification(X_test, y_test, pred_test,
                        title='SVM (linear) — Test Set')


# ══════════════════════════════════════════════════════════════════
#  Main
# ══════════════════════════════════════════════════════════════════

if __name__ == '__main__':
    demo_unsupervised()
    demo_supervised()
    demo_preprocessing()
    demo_train_test()
```

## Exercises

**Exercise 1.**
List four common classification algorithms used in finance and briefly describe each.

??? success "Solution to Exercise 1"

    1. **Logistic regression**: Models the log-odds of the positive class as a linear function of features. Simple, interpretable, and provides probability estimates. Commonly used for credit scoring.
    2. **Random forest**: An ensemble of decision trees, each trained on a bootstrap sample with random feature subsets. Handles nonlinearities and interactions. Used for fraud detection and default prediction.
    3. **Support vector machine (SVM)**: Finds the maximum-margin hyperplane separating classes. Effective in high-dimensional spaces. Used for stock movement prediction.
    4. **Gradient boosted trees (XGBoost/LightGBM)**: Sequential ensemble where each tree corrects the errors of the previous ones. State-of-the-art performance on tabular data. Widely used in credit risk and algorithmic trading.

---

**Exercise 2.**
For a binary classifier predicting loan default, the confusion matrix shows: TP = 80, FP = 20, FN = 30, TN = 870. Compute precision, recall, and F1 score.

??? success "Solution to Exercise 2"
    $$
    \text{Precision} = \frac{TP}{TP + FP} = \frac{80}{100} = 80\%.
    $$

    $$
    \text{Recall} = \frac{TP}{TP + FN} = \frac{80}{110} = 72.7\%.
    $$

    $$
    F_1 = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}} = 2 \times \frac{0.80 \times 0.727}{0.80 + 0.727} = 2 \times \frac{0.5818}{1.527} = 0.762 = 76.2\%.
    $$

---

**Exercise 3.**
Explain why accuracy is a poor metric for imbalanced datasets (e.g., $2\%$ default rate) and suggest a better metric.

??? success "Solution to Exercise 3"
    With a $2\%$ default rate, a naive classifier that predicts "no default" for every loan achieves $98\%$ accuracy. This is misleading because the classifier completely fails to identify any defaults (recall $= 0\%$). Better metrics include:

    - **AUC-ROC**: Measures the classifier's ability to discriminate between classes across all thresholds. A random classifier has AUC $= 0.5$; a perfect one has AUC $= 1.0$.
    - **F1 score**: Balances precision and recall, penalizing classifiers that sacrifice one for the other.
    - **Precision-recall AUC**: More informative than ROC-AUC for highly imbalanced datasets.
    - **Expected cost**: Weights errors by their financial impact (missing a default is typically more costly than a false alarm).

---

**Exercise 4.**
Describe the bias-variance trade-off in the context of a credit risk classification model and how cross-validation helps manage it.

??? success "Solution to Exercise 4"

    - **High bias (underfitting)**: A simple model (logistic regression with few features) may miss important patterns, predicting poorly on both training and test data.
    - **High variance (overfitting)**: A complex model (deep neural network) may fit training data noise, performing well on training but poorly on new data.

    Cross-validation (e.g., $k$-fold) helps by: (1) providing an unbiased estimate of out-of-sample performance; (2) enabling model selection (choose the complexity level that minimizes cross-validation error); (3) detecting overfitting (large gap between training and CV performance). Time-series cross-validation (walk-forward) is essential for financial data to avoid look-ahead bias.
