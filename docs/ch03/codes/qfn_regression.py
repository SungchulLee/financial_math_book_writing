"""
Linear and Logistic Regression
===============================

Exploration of linear and logistic regression methods with reference to
Chapter 13 from 'All of Statistics' (Wasserman, 2004). Covers simple linear
regression via least squares and maximum likelihood estimation, properties
of estimators, prediction intervals, multiple regression in matrix form,
model selection criteria (AIC, BIC, cross-validation), and logistic regression
for binary outcomes.

Source: "quantitative-finance-notebooks" collection by S. Couch
        (Notebook 2.4 - Linear and Logistic Regression)
"""

import numpy as np
import scipy.stats as ss
import scipy.optimize as opt
import matplotlib.pyplot as plt
import statsmodels.api as sm

# ============================================================================
# 1. Simple Linear Regression
# ============================================================================
#
# Regression studies the relationship between a response variable Y and a
# covariate X through the regression function:
#
#   r(x) = E(Y | X = x) = integral of y * f(y|x) dy
#
# The simple linear regression model assumes r(x) is linear:
#
#   Y_i = beta_0 + beta_1 * X_i + epsilon_i
#
# where E(epsilon_i | X_i) = 0 and V(epsilon_i | X_i) = sigma^2.
#
# The least squares estimates minimize the residual sum of squares (RSS):
#
#   beta_1_hat = sum((X_i - X_bar)(Y_i - Y_bar)) / sum((X_i - X_bar)^2)
#   beta_0_hat = Y_bar - beta_1_hat * X_bar
#
# An unbiased estimate of sigma^2 is:
#
#   sigma_hat^2 = (1 / (n - 2)) * sum(epsilon_hat_i^2)

# Generate synthetic data
n = 100
X = ss.uniform.rvs(loc=0, scale=10, size=n, random_state=42)
true_beta0, true_beta1 = 2, 3
true_var = 1
epsilon = ss.norm.rvs(loc=0, scale=np.sqrt(true_var), size=n, random_state=42)
Y = true_beta0 + true_beta1 * X + epsilon

# Compute least squares estimates
X_mean, Y_mean = np.mean(X), np.mean(Y)
ols_beta1 = np.sum((X - X_mean) * (Y - Y_mean)) / np.sum((X - X_mean)**2)
ols_beta0 = Y_mean - ols_beta1 * X_mean

# Compute fitted values and residuals
ols_Y = ols_beta0 + ols_beta1 * X
ols_resids = Y - ols_Y
ols_RSS = np.sum(ols_resids**2)
ols_var_hat = (1 / (n - 2)) * ols_RSS

# Print results
print(f"True β0 = {true_beta0}, Estimated β0 = {ols_beta0:.3f}")
print(f"True β1 = {true_beta1}, Estimated β1 = {ols_beta1:.3f}")
print(f"Residual Sum of Squares (RSS) = {ols_RSS:.3f}")
print(f"True σ² = {true_var}, Unbiased estimate of σ² = {ols_var_hat:.3f}")

# Plot the data and the fitted line
plt.figure(figsize=(5, 3))
plt.scatter(X, Y, label='Data points')
plt.plot(X, ols_Y, color='red', label='Regression line')
plt.xlabel('X'), plt.ylabel('Y')
plt.legend()
plt.show()

# ============================================================================
# 2. Least Squares and Maximum Likelihood
# ============================================================================
#
# Under normality assumption epsilon_i | X_i ~ N(0, sigma^2), i.e.
#
#   Y_i | X_i ~ N(mu_i, sigma^2),  where mu_i = beta_0 + beta_1 * X_i
#
# The conditional log-likelihood is:
#
#   l(beta_0, beta_1, sigma) = -n * log(sigma)
#       - (1 / (2 * sigma^2)) * sum((Y_i - (beta_0 + beta_1 * X_i))^2)
#
# Maximizing the likelihood is equivalent to minimizing the RSS, so under
# normality the least squares estimator is also the MLE.
#
# The MLE of sigma^2 is:
#
#   sigma_hat^2_MLE = (1/n) * sum(epsilon_hat_i^2)
#
# which is similar to, but not identical to, the unbiased estimator.


# Define the negative log-likelihood function
def negative_log_likelihood(params, X, Y):
    beta0, beta1, sigma = params
    mu = beta0 + beta1 * X
    n = len(Y)
    resids = Y - mu
    log_likelihood = -n * np.log(sigma) - (1 / (2 * sigma**2)) * np.sum(resids**2)
    return -log_likelihood


# Optimize the negative log-likelihood function
result = opt.minimize(negative_log_likelihood, x0=[0, 0, 1], args=(X, Y),
                      bounds=[(None, None), (None, None), (1e-10, None)])
mle_beta0, mle_beta1, mle_sigma = result.x

# Compute fitted values and residuals
mle_Y = mle_beta0 + mle_beta1 * X
mle_resids = Y - mle_Y
mle_RSS = np.sum(mle_resids**2)
mle_var_hat = (1 / n) * mle_RSS

# Print results
print(f"True β0 = {true_beta0}, Estimated β0 = {mle_beta0:.3f}")
print(f"True β1 = {true_beta1}, Estimated β1 = {mle_beta1:.3f}")
print(f"Residual Sum of Squares (RSS) = {mle_RSS:.3f}")
print(f"True σ² = {true_var}, MLE estimate of σ² = {mle_var_hat:.3f}")

# ============================================================================
# 3. Properties of the Least Squares Estimators
# ============================================================================
#
# Let beta_hat = (beta_0_hat, beta_1_hat)^T denote the least squares
# estimators. Then:
#
#   E(beta_hat | X^n) = (beta_0, beta_1)^T
#
#   V(beta_hat | X^n) = (sigma^2 / (n * s_X^2)) *
#       [[  (1/n) * sum(X_i^2),   -X_bar  ],
#        [       -X_bar,             1     ]]
#
# where s_X^2 = (1/n) * sum((X_i - X_bar)^2).
#
# The estimated standard errors are obtained by taking square roots of
# the diagonal of V(beta_hat | X^n), replacing sigma with sigma_hat.

# Compute standard errors
s_X2 = np.mean((X - X_mean)**2)
var_cov_matrix = (ols_var_hat / (n * s_X2)) * np.array([[np.mean(X**2), -X_mean], [-X_mean, 1]])
se_ols_beta0 = np.sqrt(var_cov_matrix[0, 0])
se_ols_beta1 = np.sqrt(var_cov_matrix[1, 1])

# Print results
print(f"Standard Error of β0: {se_ols_beta0:.3f}")
print(f"Standard Error of β1: {se_ols_beta1:.3f}")

# Confirm our results using statsmodels.api.OLS
X_with_const = sm.add_constant(X)
ols = sm.OLS(Y, X_with_const)
ols_result = ols.fit()
ols_result.summary()

# ============================================================================
# 4. Prediction
# ============================================================================
#
# For a new observation X = x_*, the predicted value is:
#
#   Y_hat_* = beta_0_hat + beta_1_hat * x_*
#
# The prediction interval accounts for both estimation uncertainty and noise:
#
#   xi_n^2 = sigma_hat^2 * (sum((X_i - x_*)^2) / (n * sum((X_i - X_bar)^2)) + 1)
#
# An approximate (1 - alpha) prediction interval for Y_* is:
#
#   Y_hat_* +/- z_{alpha/2} * xi_n

# Compute prediction for a new x value
x_star = 7
Y_star = ols_beta0 + ols_beta1 * x_star
xi_n_squared = ols_var_hat * ((np.sum((X - x_star)**2) / (n * np.sum((X - X_mean)**2))) + 1)
se_Y_star = np.sqrt(xi_n_squared)
alpha = 0.05
z_alpha = ss.norm.ppf(1 - alpha / 2)
pred_int = (Y_star - z_alpha * se_Y_star, Y_star + z_alpha * se_Y_star)

print(f"Predicted Y = {Y_star:.3f} for x = {x_star}")
print(f"95% Prediction Interval for Y = ({pred_int[0]:.3f}, {pred_int[1]:.3f})")

# ============================================================================
# 5. Multiple Regression
# ============================================================================
#
# For a k-dimensional covariate X_i = (X_{i1}, ..., X_{ik}), the model is:
#
#   Y_i = sum_{j=1}^{k} beta_j * X_{ij} + epsilon_i
#
# In matrix notation:
#
#   Y = X * beta + epsilon
#
# where X is an (n x k) matrix. Setting X_{i1} = 1 includes an intercept.
#
# The least squares estimate (assuming X^T X is invertible):
#
#   beta_hat = (X^T X)^{-1} X^T Y
#
#   V(beta_hat | X^n) = sigma^2 * (X^T X)^{-1}
#
#   beta_hat ~ approx N(beta, sigma^2 * (X^T X)^{-1})
#
# An unbiased estimate of sigma^2 is:
#
#   sigma_hat^2 = (1 / (n - k)) * sum(epsilon_hat_i^2)
#
# An approximate (1 - alpha) confidence interval for beta_j is:
#
#   beta_j_hat +/- z_{alpha/2} * se_hat(beta_j_hat)

# ============================================================================
# 6. Model Selection
# ============================================================================
#
# Stepwise regression builds a model by adding/removing predictors step by
# step until a pre-set significance level is met ("forward selection" and
# "backward selection").
#
# AIC (Akaike Information Criterion) and BIC (Bayesian Information Criterion):
#
#   AIC = n * ln(RSS / n) + 2 * (k + 1)
#   BIC = n * ln(RSS / n) + (k + 1) * ln(n)
#
# Both balance fit and complexity, but BIC imposes a stricter penalty for
# larger sample sizes.
#
# k-fold cross-validation divides data into k groups, fits the model on
# k-1 groups, predicts on the held-out group, and averages the risk
# estimate sum((Y_i - Y_hat_i)^2) across all folds.

# ============================================================================
# 7. Logistic Regression
# ============================================================================
#
# When Y_i in {0, 1} is binary, logistic regression models:
#
#   p_i = P(Y_i = 1 | X = x) = exp(beta_0 + sum beta_j * x_ij)
#                                / (1 + exp(beta_0 + sum beta_j * x_ij))
#
# Equivalently:
#
#   logit(p_i) = log(p_i / (1 - p_i)) = beta_0 + sum beta_j * x_ij
#
# The data are Bernoulli: Y_i | X_i ~ Bernoulli(p_i), so the likelihood is:
#
#   L(beta) = prod p_i^{Y_i} * (1 - p_i)^{1 - Y_i}
#
# The MLE beta_hat is obtained by numerical maximization. Standard errors
# come from the Fisher information matrix I; se(beta_j_hat) is the (j,j)
# element of J = I^{-1}. Model selection uses the AIC score.

# Logistic regression code example
n_samples, n_features = 100, 3
X = ss.norm.rvs(size=(n_samples, n_features), random_state=42)
true_beta = np.array([0.5, -1.0, 0.75])

p = sm.families.links.Logit().inverse(X @ true_beta)              # compute probabilities using logistic function
Y = ss.bernoulli.rvs(p, random_state=42)                          # generate binary outcomes using scipy.stats.bernoulli
X_with_intercept = sm.add_constant(X)                              # add constant (intercept) to features matrix
logit_model = sm.Logit(Y, X_with_intercept)                        # fit logistic regression model using statsmodels
result = logit_model.fit()

# Print result
print(result.summary())

# Compute the Fisher Information Matrix and its inverse
fisher_info = result.cov_params()
std_errors = np.sqrt(np.diag(fisher_info))
aic = result.aic

# Print results
print(f"Standard errors = {std_errors}")
print(f"AIC = {aic:.3f}")
