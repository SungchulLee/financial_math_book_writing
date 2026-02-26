# Hypothesis Testing

!!! info "Source"
    **Quantitative Finance Notebooks** — educational notebooks on mathematical concepts in quantitative finance.

## 0. Introduction

The purpose of this notebook is to explore hypothesis testing with reference to chapter 10 from *All of Statistics* (Wasserman, 2004) and [this GitHub page](https://github.com/CodeRabbitHub/Statistics-and-Probability-For-Data-Science/blob/main/12.%20Z-test.ipynb) (Roland, 2021).

## 1. Hypothesis Testing and p-values

Suppose that we partition the parameter space $\Theta$ into two disjoint sets $\Theta_0$ and $\Theta_1$ and that we wish to test

$$ H_0 : \theta \in \Theta_0 \quad \text{versus} \quad H_1 : \theta \in \Theta_1. $$

We call $H_0$ the **null hypothesis** and $H_1$ the **alternative hypothesis**. 

Let $X$ be a random variable and let $\mathcal{X}$ be the range of $X$. We test a hypothesis by finding an appropriate subset of outcomes $R \subset \mathcal{X}$ called the **rejection region**. If $X \in R$ we reject the null hypothesis; otherwise, we do not reject the null hypothesis:

$$
\begin{aligned}
X \in R &\implies \text{reject } H_0 \\
X \notin R &\implies \text{retain (do not reject) } H_0.
\end{aligned}
$$

Usually, the rejection region $R$ is of the form

$$ R = \Big\{ x : T(x) > c \Big\} $$

where $T$ is a **test statistic** and $c$ is a **critical value**. The problem in hypothesis testing is to find an appropriate test statistic $T$ and an  appropriate critical value $c$.

Reporting "reject $H_0$" or "retain $H_0$" is not very informative. Instead, we could ask, for every $\alpha$, whether the test rejects at that level. Generally, if the test rejects at level $\alpha$ it will also reject at level $\alpha' > \alpha$. Hence, there is a smallest $\alpha$ at which the test rejects and we call this number the $p$-value.

Informally, the $p$-value is a measure of the evidence against $H_0$: the smaller the $p$-value, the stronger the evidence against $H_0$. Typically, researchers use
the following evidence scale:

<center><img src="../figures/p_value.png" width="300" height="250"/></center>

## 2. Statistical Tests

### 2.1 $z$-Test

$z$-tests are a statistical way of testing a hypothesis when we know the population standard deviation $\sigma$. We use them when we wish to compare the sample mean $\bar{x}$ to the population mean $\mu$. However, if your sample size is large, $n \geq 30$, then you can still use $z$-tests without knowing the population standard deviation. Instead, you may use the sample standard deviation as an estimate of the population standard deviation.

The conditions for using this type of test are that the data must be **normally distributed**; all data points must be **independent**; and for each sample the **standard deviations must be equal**.

The test statistic is computed using the formula:

$$ z = \frac{\bar{x} - \mu}{\frac{\sigma}{\sqrt{n}}} $$

where $\bar{x}$ denotes the sample mean, $\mu$ is the population mean, $\sigma$ is the population standard deviation, and $n$ is the sample size.

Let's consider an example of a $z$-test on a one-sample two-tailed distribution from Roland (2021). Suppose we aim to investigate whether a drug has an impact on IQ. Assuming our population mean $\mu = 100$ and population standard deviation $\sigma = 15$, we conduct a study involving a sample of $100$ subjects. Upon analysis, we discover that the mean IQ of the sample is $96$. Determine whether the drug has a significant influence on IQ values at a significance level of $\alpha = 0.05$.

```python
import numpy as np
import scipy.stats as ss
```

```python
# Solve in python
x_bar = 96                                 # sample mean
mu = 100                                   # population mean
sigma = 15                                 # population standard deviation
n = 100                                    # sample size
z = (x_bar - mu) / (sigma / np.sqrt(n))    # z-test statistic
p_value = 2 * (1 - ss.norm.cdf(abs(z)))    # p-value corresponding to test statistic
alpha = 0.05                               # significance level
c = ss.norm.ppf(1 - alpha / 2)             # critical value for a two-tailed test

# Print result
print(f"z-test statistic = {z:.3f}, critical value = +-{c:.3f} \np-value = {p_value:.4f}, alpha = {alpha:.2f}")
print(f"Reject the null hypothesis!" if p_value < alpha else "Fail to reject the null hypothesis!")
```

<center><img src="../figures/z_test.png"/></center>

Often, we need to compare the means from two samples and we use the $z$-statistic for when we know the population variances.

$$ z = \frac{\overline{x}_1 - \overline{x}_2} {\sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}}}. $$

Let's consider another example from Roland (2021). An organisation manufactures LED bulbs in two production units, $A$ and $B$. The quality control team believes that the quality of production at unit $A$ is better than that of $B$. Quality is measured by how long a bulb works. The team takes samples from both units to test this. The mean life of LED bulbs at units $A$ and $B$ are $1001.34$ and $810.47$, respectively. The sample sizes are $40$ and $44$. The population variances are known: $\sigma_A^2 = 48127$ and $\sigma_B^2 = 59173$.

Conduct the appropriate test, at a $5\%$ significance level, to verify the claim of the quality control team.

**Null hypothesis** $(H_0): \mu_A ≤ \mu_B$  
**Alternate hypothesis** $(H_1): \mu_A > \mu_B$

```python
# Solve in python
x_bar_a = 1001.34                                                    # sample mean of A
x_bar_b = 810.47                                                     # sample mean of B
var_a = 48127                                                        # population variance of A
var_b = 59173                                                        # population variance of B
n_a = 40                                                             # sample size of A
n_b = 44                                                             # sample size of B
z = (x_bar_a - x_bar_b) / np.sqrt((var_a / n_a) + (var_b / n_b))     # z-test statistic
p_value = 1 - ss.norm.cdf(z)                                         # p-value corresponding to test statistic
alpha = 0.05                                                         # significance level
c = ss.norm.ppf(1 - alpha)                                           # critical value for a one-tailed test

# Print result
print(f"z-test statistic = {z:.3f}, critical value = {c:.3f} \np-value = {p_value:.4f}, alpha = {alpha:.2f}")
print(f"Reject the null hypothesis!" if p_value < alpha else "Fail to reject the null hypothesis!")
```

### 2.2 $t$-Test

The $t$-test is very similar to a $z$-test; however, you do not know the value of the population standard deviation $\sigma$ and so you must use a modified version of the test above. This statistical test is applicable to cases where **the sample size is small** $(< 30)$.

The test statistic is computed using the formula:

$$ t = \frac{\overline{x} - \mu}{\frac{s}{\sqrt{n}}} $$

where $\overline{x}$ is the sample mean, $\mu$ is the population mean, $s$ is the sample standard deviation, and $n$ is the sample size.

Let's consider a $t$-test on a one-sample one-tailed distribution example from Roland (2021). A coaching institute, preparing students for an exam, has $200$ students, and the average score of the students in the practice tests is $80$. It takes a sample of nine students and records their scores; it seems that the average score has now increased. These are the scores of these nine students: $80, 87, 80, 75, 79, 78, 89, 84, 88$. Conduct a hypothesis test at a $5\%$ significance level to verify if there is a significant increase in the average score.

**Null hypothesis** $(H_0): \mu = 80$  
**Alternative hypothesis** $(H_1): \mu > 80$

```python
# Solve in python
x = np.array([80, 87, 80, 75, 79, 78, 89, 84, 88])    # sample test scores
x_bar = np.mean(x)                                    # sample mean
mu = 80                                               # population mean
s = np.std(x, ddof=1)                                 # sample standard deviation
n = len(x)                                            # sample size
dof = n-1                                             # degrees of freedom (sample size - 1)
t = (x_bar - mu) / (s / np.sqrt(n))                   # t-test statistic
p_value = 1 - ss.t.cdf(t, df=dof)                     # p-value corresponding to test statistic
alpha = 0.05                                          # significance level
c = ss.t.ppf(1 - alpha, df=dof)                       # critical value for a one-tailed test

# Print result
print(f"Chi-square statistic = {t:.3f}, critical value = {c:.3f} \np-value = {p_value:.4f}, alpha = {alpha:.2f}")
print(f"Reject the null hypothesis!" if p_value < alpha else "Fail to reject the null hypothesis!")
```

A two-sample t-test is used when we take samples from two populations, where both the sample sizes are less than 30, and both the population standard deviations are unknown. The formula is:

$$ t = \frac{\overline x_1 - \overline x_2}{\sqrt{S_p^2(\frac{1}{n_1}+\frac{1}{n_2})}} $$

where $x_1$ and $x_2$ are the sample means. The degrees of freedom: $df=n_1 + n_2 − 2$. The pooled variance $S_p^2 = \frac{(n_1 -1)S_1^2 + (n_2-1)S_2^2}{n_1+n_2-2}$  

Let's consider another example from Roland (2021). A coaching institute has centres in two different cities. It takes a sample of ten students from each centre and records their
scores: 

Centre A = $\{80, 87, 80, 75, 79, 78, 89, 84, 88 \}$ 

Centre B:  $\{81, 74, 70, 73, 76, 73, 81, 82, 84\}$
 
Conduct a hypothesis test at a $5\%$ significance level, and verify if there a significant difference in the average scores of the
students in these two centres.

**Null hypothesis** $(H_0): \mu_1 = \mu_2$   
**Alternative hypothesis** $(H_1): \mu_1 != \mu_2$

```python
# Solve in python
A = np.array([80, 87, 80, 75, 79, 78, 89, 84, 88])                            # sample scores for A
B = np.array([81, 74, 70, 73, 76, 73, 81, 82, 84])                            # sample scores for B
n_a = len(A)                                                                  # sample size of A
n_b = len(B)                                                                  # sample size of B
x_bar_a = np.mean(A)                                                          # sample mean of A
x_bar_b = np.mean(B)                                                          # sample mean of B
s_a = np.std(A, ddof=1)                                                       # sample standard deviation of A
s_b = np.std(B, ddof=1)                                                       # sample standard deviation of B
dof = n_a + n_b - 2                                                           # degrees of freedom
pool_var = (((n_a - 1) * s_a**2) + ((n_b - 1) * s_b**2)) / (n_a + n_b - 2)    # pooled variance
t = (x_bar_a - x_bar_b) / np.sqrt(pool_var * (1 / n_a + 1 / n_b))             # t-test statistic
p_value = 2 * (1 - ss.t.cdf(abs(t), df=dof))                                  # p-value corresponding to test statistic
alpha = 0.05                                                                  # significance level
c = ss.t.ppf(1 - alpha / 2, df=dof)                                           # critical value for a two-tailed test

# Print result
print(f"t-test statistic = {t:.3f}, critical value = {c:.3f} \np-value = {p_value:.4f}, alpha = {alpha:.2f}")
print(f"Reject the null hypothesis!" if p_value < alpha else "Fail to reject the null hypothesis!")
print("\nNote: you can simply use scipy.stats.ttest_ind instead.")
```

### 2.3 ANOVA

ANOVA (Analysis of Variance) is a statistical method used for comparing the means of multiple populations. Previously, we have considered only a single population or at most two populations. A one-way ANOVA uses one independent variable, while a two-way ANOVA uses two independent variables. The statistical distribution used in ANOVA is the $F$-distribution:

<center><img src="../figures/f_dist.png"/></center>

The $F$-statistic, which is the critical statistic in ANOVA, is the ratio of variation between the sample means to the variation within the samples. The formula is as follows:

$$ F = \frac{\text{variation between sample means}}{\text{variation within the samples}}. $$

The different populations are referred to as treatments. A high value of the $F$-statistic implies that the variation between samples is considerable compared to the variation within the samples. In other words, the populations or treatments from which the samples are drawn are actually different from one another. Random variations between treatments are more likely to occur when the variation within the sample is considerable.

Let's consider a one-way-ANOVA example from Roland (2021). A few agricultural research scientists have planted a new variety of cotton. They have used three different fertilizers – $A$, $B$, and $C$ – for three separate plots of this variety. The researchers want to find out if the yield varies with the type of fertilizer used. Yields in bushels per acre are mentioned in the below table. Conduct an ANOVA test at a $5\%$ level of significance to see if the researchers can conclude that there is a difference in yields.

| Fertilizer A | Fertilizer b | Fertilizer c |
|--------------|--------------|--------------|
|     40       |     45       |     55       |
|     30       |     35       |     40       |
|     35       |     55       |     30       |
|     45       |     25       |     20       |

**Null hypothesis** $(H_0): \mu_1 = \mu_2 = \mu_3$  
**Alternative hypothesis** $(H_1): \mu_1 ! = \mu_2 ! = \mu_3$

```python
# Solve in python
A = np.array([40, 30, 35, 45])       # Sample yields for A
B = np.array([45, 35, 55, 25])       # Sample yeilds for B
C = np.array([55, 40, 30, 20])       # Sample yeilds for C
f, p_value = ss.f_oneway(A, B, C)    # f-test stastistic and corresponding p-value

# Print result
print(f"p-value = {p_value:.4f}, alpha = {alpha:.2f}")
print(f"Reject the null hypothesis!" if p_value < alpha else "Fail to reject the null hypothesis!")
print("\nNote: raw calculation is long so used scipy.stats.f_oneway instead.")
```

### 2.4. $\chi^2$ Test

Pearson's $\chi^2$ statistic for multinomial data is

$$ T = \sum_{j=1}^{k} \frac{(X_j - np_{0j})^2}{np_{0j}} = \sum_{j=1}^{k} \frac{(X_j - E_j)^2}{E_j} $$

where $E_j = \mathbb{E}(X_j) = np_{0j}$ is the expected value of $X_j$ under $H_0$.

Let's consider an example from Wasserman (2004). Mendel bred peas with round yellow seeds and wrinkled green seeds. There are four types of progeny: round yellow, wrinkled yellow, round green, and wrinkled green. The number of each type is multinomial with probability $p = (p_1, p_2, p_3, p_4)$. His theory of inheritance predicts that $p$ is equal to

$$ p_0 \equiv \left( \frac{9}{16}, \frac{3}{16}, \frac{3}{16}, \frac{1}{16} \right). $$

In $n = 556$ trials he observed $X = (315, 101, 108, 32)$. We will test $H_0 : p = p_0$ versus $H_1 : p \neq p_0$. Since $np_{01} = 312.75$, $np_{02} = np_{03} = 104.25$, and $np_{04} = 34.75$, the test statistic is 

$$ \chi^2 = \frac{(315 - 312.75)^2}{312.75} + \frac{(101 - 104.25)^2}{104.25} + \frac{(108 - 104.25)^2}{104.25} + \frac{(32 - 34.75)^2}{34.75} = 0.47. $$

The $\alpha = 0.05$ value for a $\chi^2_3$ is $7.815$. Since $0.47$ is not larger than $7.815$, we do not reject the null hypothesis. The p-value is

$$ \text{p-value} = \mathbb{P}(\chi^2_3 > 0.47) = 0.93 $$

which is not evidence against $H_0$. Hence, the data do not contradict Mendel's theory.

```python
# Solve in python
n = 556                                   # sample size
X = np.array([315, 101, 108, 32])         # observed frequencies in each category
np_0 = np.array([
    9 / 16 * n,                           # expected frequencies in each category under null hypothesis
    3 / 16 * n, 
    3 / 16 * n, 
    1 / 16 * n
])
dof = len(X) - 1                          # degrees of freedom (number of categories - 1)
T = np.sum((X - np_0)**2 / np_0)          # chi-square test statistic
p_value = 1 - ss.chi2.cdf(T, df=dof)      # p-value corresponding to test statistic
alpha = 0.05                              # significance level
c = ss.chi2.ppf(1 - alpha, df=dof)        # critical value for a one-tailed test

# Print result
print(f"chi-square statistic = {T:.3f}, critical value = {c:.3f} \np-value = {p_value:.4f}, alpha = {alpha:.2f}")
print(f"Reject the null hypothesis!" if p_value < alpha else "Fail to reject the null hypothesis!")
```

<center><img src="../figures/chi2_test.png"/></center>

It is worth noting that goodness-of-fit testing has some serious limitations. If we reject $H_0$ then we conclude we should not use the model. But if we do not reject $H_0$ we cannot conclude that the model is correct. We may have failed to reject simply because the test did not have enough power. This is why it is better to use nonparametric methods whenever possible rather than relying on parametric assumptions.
