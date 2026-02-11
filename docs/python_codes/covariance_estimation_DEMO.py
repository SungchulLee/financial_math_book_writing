import numpy as np
import pandas as pd
from sklearn import covariance

# Generate synthetic data
np.random.seed(0)
z = np.random.normal(size=(1000, 3))
A = np.random.random((3, 3))
x = z @ A

# True covariance matrix
S_true = A.T @ A

# List of covariance estimators from sklearn.covariance
estimators = {
    'EmpiricalCovariance': covariance.EmpiricalCovariance(),
    'EllipticEnvelope': covariance.EllipticEnvelope(),
    'GraphicalLasso': covariance.GraphicalLasso(),
    # 'GraphicalLassoCV': covariance.GraphicalLassoCV(),
    'LedoitWolf': covariance.LedoitWolf(),
    'MinCovDet': covariance.MinCovDet(),
    'OAS': covariance.OAS(),
    'ShrunkCovariance': covariance.ShrunkCovariance()
}

# Function to compute Frobenius norm between estimated and true covariance
def frobenius_norm(estimator, x, S_true):
    try:
        estimator.fit(x)
        S_est = estimator.covariance_
        return np.linalg.norm(S_true - S_est, ord='fro')
    except Exception:
        return np.nan

# Evaluate all estimators
results = {
    'Estimator': [],
    'Frobenius Norm': []
}

for name, estimator in estimators.items():
    norm = frobenius_norm(estimator, x, S_true)
    results['Estimator'].append(name)
    results['Frobenius Norm'].append(norm)

df_results = pd.DataFrame(results).sort_values(by='Frobenius Norm')

# Print the results directly instead of using ace_tools
print(df_results.to_string(index=False))