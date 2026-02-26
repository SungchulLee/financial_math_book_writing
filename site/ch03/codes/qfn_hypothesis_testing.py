"""
Hypothesis Testing
==================
Statistical hypothesis testing: z-tests, t-tests, ANOVA, and chi-square tests,
with worked examples covering one-sample, two-sample, one-tailed, and two-tailed
scenarios. Theory follows Chapter 10 of *All of Statistics* (Wasserman, 2004)
and practical examples from Roland (2021).

Source: "quantitative-finance-notebooks" collection
    - Notebook 2.2: Hypothesis Testing
"""

import numpy as np
import scipy.stats as ss

# =============================================================================
# 1. Hypothesis Testing and p-values
# =============================================================================
#
# Suppose we partition the parameter space Theta into two disjoint sets
# Theta_0 and Theta_1 and wish to test:
#
#     H_0 : theta in Theta_0   (null hypothesis)
#     H_1 : theta in Theta_1   (alternative hypothesis)
#
# We find a rejection region R (a subset of outcomes). If the observed
# statistic X falls in R we reject H_0; otherwise we retain H_0.
#
# Typically R = { x : T(x) > c } where T is a test statistic and c is a
# critical value. The p-value is the smallest significance level alpha at
# which the test rejects -- a measure of evidence against H_0:
#
#     p-value < 0.01    => very strong evidence against H_0
#     0.01 <= p < 0.05  => strong evidence against H_0
#     0.05 <= p < 0.10  => weak evidence against H_0
#     p >= 0.10         => little or no evidence against H_0

# =============================================================================
# 2. Statistical Tests
# =============================================================================

# -----------------------------------------------------------------------------
# 2.1 z-Test
# -----------------------------------------------------------------------------
#
# z-tests are used when the population standard deviation sigma is known
# (or when n >= 30 so that the sample std approximates it well).
#
# Conditions: data normally distributed, observations independent,
# equal standard deviations across samples.
#
# One-sample test statistic:
#     z = (x_bar - mu) / (sigma / sqrt(n))
#
# where x_bar = sample mean, mu = population mean, sigma = population std,
# n = sample size.

# --- Example 1: One-sample two-tailed z-test ---
# Does a drug have an impact on IQ?
# Population: mu = 100, sigma = 15
# Sample: n = 100 subjects, sample mean = 96
# Significance level: alpha = 0.05
x_bar = 96                                  # sample mean
mu = 100                                    # population mean
sigma = 15                                  # population standard deviation
n = 100                                     # sample size
z = (x_bar - mu) / (sigma / np.sqrt(n))     # z-test statistic
p_value = 2 * (1 - ss.norm.cdf(abs(z)))     # p-value corresponding to test statistic
alpha = 0.05                                # significance level
c = ss.norm.ppf(1 - alpha / 2)              # critical value for a two-tailed test

# Print result
print(f"z-test statistic = {z:.3f}, critical value = +-{c:.3f} \np-value = {p_value:.4f}, alpha = {alpha:.2f}")
print(f"Reject the null hypothesis!" if p_value < alpha else "Fail to reject the null hypothesis!")

# --- Example 2: Two-sample one-tailed z-test ---
# Two-sample z-statistic (known population variances):
#     z = (x_bar_1 - x_bar_2) / sqrt(sigma_1^2/n_1 + sigma_2^2/n_2)
#
# LED bulb quality comparison between production units A and B.
# H_0: mu_A <= mu_B
# H_1: mu_A > mu_B
x_bar_a = 1001.34                                                    # sample mean of A
x_bar_b = 810.47                                                     # sample mean of B
var_a = 48127                                                        # population variance of A
var_b = 59173                                                        # population variance of B
n_a = 40                                                             # sample size of A
n_b = 44                                                             # sample size of B
z = (x_bar_a - x_bar_b) / np.sqrt((var_a / n_a) + (var_b / n_b))    # z-test statistic
p_value = 1 - ss.norm.cdf(z)                                        # p-value corresponding to test statistic
alpha = 0.05                                                         # significance level
c = ss.norm.ppf(1 - alpha)                                           # critical value for a one-tailed test

# Print result
print(f"\nz-test statistic = {z:.3f}, critical value = {c:.3f} \np-value = {p_value:.4f}, alpha = {alpha:.2f}")
print(f"Reject the null hypothesis!" if p_value < alpha else "Fail to reject the null hypothesis!")

# -----------------------------------------------------------------------------
# 2.2 t-Test
# -----------------------------------------------------------------------------
#
# The t-test is used when the population standard deviation sigma is unknown
# and the sample size is small (n < 30). Uses sample std s instead of sigma.
#
# One-sample test statistic:
#     t = (x_bar - mu) / (s / sqrt(n))
#
# where s is the sample standard deviation.

# --- Example 3: One-sample one-tailed t-test ---
# Has the average score of coaching students increased above 80?
# H_0: mu = 80
# H_1: mu > 80
x = np.array([80, 87, 80, 75, 79, 78, 89, 84, 88])    # sample test scores
x_bar = np.mean(x)                                      # sample mean
mu = 80                                                  # population mean
s = np.std(x, ddof=1)                                    # sample standard deviation
n = len(x)                                               # sample size
dof = n - 1                                              # degrees of freedom (sample size - 1)
t = (x_bar - mu) / (s / np.sqrt(n))                      # t-test statistic
p_value = 1 - ss.t.cdf(t, df=dof)                        # p-value corresponding to test statistic
alpha = 0.05                                             # significance level
c = ss.t.ppf(1 - alpha, df=dof)                          # critical value for a one-tailed test

# Print result
print(f"\nt-test statistic = {t:.3f}, critical value = {c:.3f} \np-value = {p_value:.4f}, alpha = {alpha:.2f}")
print(f"Reject the null hypothesis!" if p_value < alpha else "Fail to reject the null hypothesis!")

# --- Example 4: Two-sample two-tailed t-test ---
# Two-sample t-statistic (unknown population std, small samples):
#     t = (x_bar_1 - x_bar_2) / sqrt(S_p^2 * (1/n_1 + 1/n_2))
#
# where pooled variance S_p^2 = ((n_1-1)*S_1^2 + (n_2-1)*S_2^2) / (n_1+n_2-2)
# and degrees of freedom df = n_1 + n_2 - 2.
#
# Compare average scores at two coaching centres.
# H_0: mu_1 = mu_2
# H_1: mu_1 != mu_2
A = np.array([80, 87, 80, 75, 79, 78, 89, 84, 88])                             # sample scores for A
B = np.array([81, 74, 70, 73, 76, 73, 81, 82, 84])                             # sample scores for B
n_a = len(A)                                                                    # sample size of A
n_b = len(B)                                                                    # sample size of B
x_bar_a = np.mean(A)                                                            # sample mean of A
x_bar_b = np.mean(B)                                                            # sample mean of B
s_a = np.std(A, ddof=1)                                                         # sample standard deviation of A
s_b = np.std(B, ddof=1)                                                         # sample standard deviation of B
dof = n_a + n_b - 2                                                             # degrees of freedom
pool_var = (((n_a - 1) * s_a**2) + ((n_b - 1) * s_b**2)) / (n_a + n_b - 2)     # pooled variance
t = (x_bar_a - x_bar_b) / np.sqrt(pool_var * (1 / n_a + 1 / n_b))              # t-test statistic
p_value = 2 * (1 - ss.t.cdf(abs(t), df=dof))                                   # p-value corresponding to test statistic
alpha = 0.05                                                                    # significance level
c = ss.t.ppf(1 - alpha / 2, df=dof)                                             # critical value for a two-tailed test

# Print result
print(f"\nt-test statistic = {t:.3f}, critical value = {c:.3f} \np-value = {p_value:.4f}, alpha = {alpha:.2f}")
print(f"Reject the null hypothesis!" if p_value < alpha else "Fail to reject the null hypothesis!")
print("\nNote: you can simply use scipy.stats.ttest_ind instead.")

# -----------------------------------------------------------------------------
# 2.3 ANOVA (Analysis of Variance)
# -----------------------------------------------------------------------------
#
# ANOVA compares the means of multiple populations using the F-distribution.
# The F-statistic is the ratio of between-group variation to within-group
# variation:
#
#     F = (variation between sample means) / (variation within the samples)
#
# A high F-statistic means the populations are likely different from each
# other. A one-way ANOVA uses one independent variable; a two-way ANOVA
# uses two.

# --- Example 5: One-way ANOVA ---
# Do yields differ across three fertilizers (A, B, C)?
# H_0: mu_1 = mu_2 = mu_3
# H_1: at least one mean differs
A = np.array([40, 30, 35, 45])       # sample yields for A
B = np.array([45, 35, 55, 25])       # sample yields for B
C = np.array([55, 40, 30, 20])       # sample yields for C
f, p_value = ss.f_oneway(A, B, C)    # F-test statistic and corresponding p-value

# Print result
print(f"\nF-statistic = {f:.3f}, p-value = {p_value:.4f}, alpha = {alpha:.2f}")
print(f"Reject the null hypothesis!" if p_value < alpha else "Fail to reject the null hypothesis!")
print("\nNote: raw calculation is long so used scipy.stats.f_oneway instead.")

# -----------------------------------------------------------------------------
# 2.4 Chi-square Test
# -----------------------------------------------------------------------------
#
# Pearson's chi-square statistic for multinomial data:
#
#     T = sum_j (X_j - n*p_0j)^2 / (n*p_0j)
#       = sum_j (X_j - E_j)^2 / E_j
#
# where E_j = E(X_j) = n*p_0j is the expected count under H_0.

# --- Example 6: Chi-square goodness-of-fit test (Mendel's peas) ---
# Mendel's theory predicts progeny ratios: p_0 = (9/16, 3/16, 3/16, 1/16)
# for (round yellow, wrinkled yellow, round green, wrinkled green).
# In n = 556 trials, observed X = (315, 101, 108, 32).
# H_0: p = p_0
# H_1: p != p_0
n = 556                                    # sample size
X = np.array([315, 101, 108, 32])          # observed frequencies in each category
np_0 = np.array([
    9 / 16 * n,                            # expected frequencies under null hypothesis
    3 / 16 * n,
    3 / 16 * n,
    1 / 16 * n
])
dof = len(X) - 1                           # degrees of freedom (number of categories - 1)
T = np.sum((X - np_0)**2 / np_0)           # chi-square test statistic
p_value = 1 - ss.chi2.cdf(T, df=dof)      # p-value corresponding to test statistic
alpha = 0.05                               # significance level
c = ss.chi2.ppf(1 - alpha, df=dof)         # critical value for a one-tailed test

# Print result
print(f"\nchi-square statistic = {T:.3f}, critical value = {c:.3f} \np-value = {p_value:.4f}, alpha = {alpha:.2f}")
print(f"Reject the null hypothesis!" if p_value < alpha else "Fail to reject the null hypothesis!")

# Note on goodness-of-fit testing:
# If we reject H_0, we conclude the model should not be used. But if we
# fail to reject H_0 we cannot conclude the model is correct -- the test
# may simply lack power. This is why nonparametric methods are preferable
# whenever possible rather than relying on parametric assumptions.
