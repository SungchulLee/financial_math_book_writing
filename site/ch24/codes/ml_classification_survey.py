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
