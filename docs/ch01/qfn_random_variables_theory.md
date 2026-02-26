# Random Variables I: Discrete & Continuous Distributions

!!! info "Source"
    **Quantitative Finance Notebooks** — educational notebooks on mathematical concepts in quantitative finance.

## 0. Introduction

The purpose of this notebook is to explore random variables with reference to chapter 2 from *All of Statistics* (Wasserman, 2004) and [this GitHub page](https://github.com/CodeRabbitHub/Statistics-and-Probability-For-Data-Science/blob/main/05.%20Probability%20distributions.ipynb) (Roland, 2021).

## 1. Understanding Random Variables and Probability Distributions

To comprehend probability distributions, it's essential to begin with random variables, which serve as models for probability distributions in statistical analysis.

A random variable represents a numerical outcome of a random process or a function that assigns values to each outcome of an experiment. Typically denoted by the symbol $X$, random variables are categorized as follows:

1. **Discrete Random Variables**: These variables can assume a finite, countable number of values. For instance, the result of a dice roll can be $1, 2, 3, 4, 5, \text{ or } 6$.

2. **Continuous Random Variables**: These variables can take an infinite number of values. Examples include measurements like temperature, height, and weight.

$X$ is discrete if it takes countably many values $\{x_1, x_2, \ldots \}$ and the **Probability Mass Function (PMF)** yields the probability of the variable assuming a particular discrete value. We define the PMF for $X$ by

$$ f_X(x) = \mathbb{P} (X = x). $$

The **Cumulative Distribution Function (CDF)** provides the probability of a random variable being less than or equal to a specified value. It effectively contains all the information about the random variable. More formally, it is the function $F_X : \mathbb{R} \rightarrow [0, 1]$ defined by

$$ F_X(x) = \mathbb{P}(X \leq x). $$

For continuous variables, determining $\mathbb{P} (X = x)$ is impractical since the number of possible outcomes is infinite. Consider weight as an example. The weight of a person can take an infinite number of values, such as $25.0001$ kg, $25.0000003$ kg, and so on. Hence, it is not possible to calculate the absolute probability of a person's weight being exactly $25$ kg, which would result in zero.

To overcome this limitation, we use the **Probability Density Function (PDF)** for continuous variables, which serves the same purpose as the PMF for discrete variables. The PDF represents the probability that the value of a continuous random variable falls within a given range of values.

A random variable $X$ is continuous if there exists a function $f_X$ such that $f_X(x) \geq 0$ for all $x$, $\int_{-\infty}^{\infty} f_X(x) \, dx = 1$ and for every $a \leq b$,

$$ \mathbb{P}(a < X < b) = \int_a^b f_X(x) \, dx. $$

The function $f_X$ is called the PDF. We have that

$$ F_X(x) = \int_{-\infty}^x f_X(t) \, dt $$

and $ f_X(x) = F'_X(x) $ at all points $x$ at which $ F_X $ is differentiable.

<center><img src="../figures/pdf_cdf.png"/></center>

## 2. Discrete Probability Distributions

**Warning About Notation!** It is traditional to write $X \sim F$ to indicate that $X$ has distribution $F$. This is unfortunate notation since the symbol $\sim$ is also used to denote an approximation. The notation $X \sim F$ is so pervasive that we are stuck with it. Read $X \sim F$ as "$X$ has distribution $F$" not as "$X$ is approximately $F$".

### 2.1 Uniform Distribution

The uniform distribution is a probability distribution in which every value between an interval from $a$ to $b$ is equally likely to occur.

If a random variable $X$ follows a uniform distribution, then the probability that $X$ takes on a value between $x_1$ and $x_2$ can be found by the following formula:

$$ \mathbb{P}(x_1 < X < x_2) = \frac{(x_2 – x_1)}{(b – a)} $$

where:

> $x_1$: the lower value of interest. 

> $x_2$: the upper value of interest.  

> $a$: the minimum possible value.  

> $b$: the maximum possible value.  

For example, suppose the weight of monkeys is uniformly distributed between $20$ kg and $40$ kg.

If we randomly select a monkey at random, we can use the formula above to determine the probability that the chosen monkey will weigh between $30$ and $35$ kg:

$P(30 < X < 35) = (35 – 30) / (40 – 20) = 0.25$

<center><img src="../figures/uni_dist.png" width="300" height="200"/></center>

### 2.2 Binomial Distribution

A binomial distribution describes the likelihood of obtaining a specified number of successes in a set number of trials of a binomial experiment.

A binomial experiment is an experiment that follows these properties:

1. The experiment consists of $n$ repeated trials.
2. Each trial has two possible outcomes.
3. The probability of success ($p$) and failure ($1-p$) is the same for each trial.
4. Each trial is independent of one another.  

For example, consider tossing an unbiased coin $n$ times. In this example, the probability that the outcome could be heads can be considered equal to $p$, while $1-p$ is the probability of tails. Each time the coin is tossed, the outcome is independent of all other trials.

If a random variable $X$ follows a binomial distribution, the probability that $X$ will equal $k$ successes can be found by the following formula:
  
$$ \mathbb{P}(X=k) = {}^nC_k p^k (1-p)^{n-k} $$  
  
where:  
  
> $p$ is the probability of success,  $(1-p)$ is the probability of failure.

> $n$ is the number of trials.  

Let's randomly sample $n=12$ households. Let $X$ denote the number of households in the sample that own a pet. The probability of a household owning a pet is $30\%$. What is the probability that exactly $5$ of the $12$ sampled own a pet?

$$ \mathbb{P}(X=5) = {}^{12}C_5 \cdot (0.3)^5 \cdot (0.7)^{12 - 5} = 0.16. $$

```python
import numpy as np
import scipy.stats as ss
```

```python
# Solve in python
n = 12                          # number sampled
k = 5                           # number of successes
p = 0.3                         # probability of success
prob = ss.binom.pmf(k, n, p)    # probability mass function

# Print result
print(f"Probability that exactly 5 out of 12 sampled own a pet is: {prob:.2f}")
```

What is the probability that at most one of those sampled owns a pet. That is, we need to find

$$ \mathbb{P}(X \leq 1) = \mathbb{P}(X=0) + \mathbb{P}(X=1). $$

Using the probability mass function for a binomial random variable with $n=12$ and $p=0.3$, we have

$$ {}^{12}C_0 (0.3)^{0}(0.7)^{12} + {}^{12}C_1 (0.3)^{1}(0.7)^{11} = 0.09$$

```python
# Solve in python
n = 12                          # number sampled
k = 1                           # number of successes
p = 0.3                         # probability of success
prob = ss.binom.cdf(k, n, p)    # cumulative distribution function

# Print result
print(f"Probability that at most one of those sampled owns a pet is: {prob:.2f}")
```

The **Bernoulli distribution** is a special case of the binomial distribution where a single trial is conducted (so $n$ would be $1$ for such a binomial distribution). It is also a special case of the two-point distribution, for which the possible outcomes need not be $0$ and $1$.

$$ \mathbb{P}(n) = \mathbb{P}^n (1-\mathbb{P})^{1-n}. $$

### 2.3 Geometric distribution

The geometric distribution describes the probability of experiencing a certain amount of failures before experiencing the first success in a series of Bernoulli trials. A Bernoulli trial is an experiment with only two possible outcomes – "success" or "failure" – and the probability of success is the same each time the experiment is conducted. An example of a Bernoulli trial is a coin flip. The coin can only land on two sides (we could call heads a "success" and tails a "failure") and the probability of success on each flip is $0.5$, assuming the coin is fair.

If a random variable $X$ follows a geometric distribution, then the probability of experiencing $k$ failures before experiencing the first success can be found by the following formula:

$$ \mathbb{P}(X=k) = (1-p)^kp. $$

where:

> $k$ is number of failures before first success.

> $p$ is probability of success on each trial.

For example, suppose we want to know how many times we would have to flip a fair coin until it lands on heads. We can use the formula above to determine the probability of experiencing $0, 1, 2, 3$ failures, etc. before the coin lands on heads:

**Note:** The coin can experience 0 "failure" if it lands on heads on the first flip.

$ \mathbb{P}(X=0) = (1-0.5)^0(0.5) = 0.5 $

$ \mathbb{P}(X=1) = (1-0.5)^1(0.5) = 0.25 $

$ \mathbb{P}(X=2) = (1-0.5)^2(0.5) = 0.125 $

$ \mathbb{P}(X=3) = (1-0.5)^3(0.5) = 0.0625 $

### 2.4 Poisson distribution

A Poisson experiment is an experiment that has the following properties:

1. The number of successes in the experiment can be counted.
2. The mean number of successes that occurs during a specific interval of time (or space) is known.
3. Each outcome is independent.
4. The probability that a success will occur is proportional to the size of the interval

If a random variable $X$ follows a Poisson distribution, then the probability that $X = k$ successes can be found by the following formula:  

$$ \mathbb{P}(x=k)=\frac{\lambda^k e^{-\lambda}}{k!}. $$  

where $\mathbb{P}(x=k)$ is the probability of the event occurring $k$ number of times, $k$ is the number of occurrences of the event, and $\lambda$ represents the mean number of event that occur during a specific interval.

Properties of a Poisson distribution:
1. Mean=variance=$\lambda$. In a Poisson distribution, the mean and variance have the same numeric values.  
2. The events are independent, random, and cannot occur at the same time.  

<center><img src="../figures/poisson_dist.png"/></center>

The horizontal axis is the index $k$, the number of occurrences. $\lambda$ is the expected rate of occurrences. The vertical axis is the probability of $k$ occurrences given $\lambda$. The function is defined only at integer values of $k$; the connecting lines are only guides for the eye.

At a train station, the average number of ticket machines out of operation is three. Assuming that the number of machines out of operation follows a Poisson distribution, calculate the probability that at a given point in time exactly five machines are out of operation.

```python
# Solve in python
k = 5                           # number of successes
mu = 3                          # mean of event
prob = ss.poisson.pmf(k, mu)    # probability mass function

# Print result
print(f"Probability that at a given point in time exactly five machines are out of operation: {prob:.2f}")
```

Calculate the probability that at a given point in time more than two machines are out of operation.

```python
# Solve in python
k = 2                               # number of successes
mu = 3                              # mean of event
prob = 1 - ss.poisson.cdf(k, mu)    # cumulative distribution function

# Print result
print(f"Probability that at a given point in time more than two machines are out of operation: {prob:.2f}")
```

## 3. Continuous Probability Distributions

### 3.1 Normal Distribution 
A normal distribution is a symmetrical bell-shaped curve, defined by its mean ($\mu$) and standard deviation ($\sigma$). If a random variable $X$ follows a normal distribution we write $X \sim N(\mu, \sigma^2)$. The formula for the PDF of the normal distribution is:

$$ f(x) = \frac{1}{\sqrt{2 \pi \sigma^2}} \exp \left\{- \frac{(x - \mu)^2}{2 \sigma^2}\right\}. $$

Characteristics of a normal distribution: 
1. The central value ($\mu$) is also the mode and the median for a normal distribution
2. Checking for normality: In a normal distribution, the difference between the 75th percentile value ($Q_3$) and the 50th percentile value (median or $Q_2$) equals the difference between the median ($Q_2$) and the 25th percentile($Q_1$). In other words,  

$$ Q_3 - Q_2 = Q_2 - Q_1. $$

If the distribution is skewed, this equation does not hold. In a right-skewed distribution, $(Q_3 − Q_2)> (Q_2 - Q_1)$. In a left-skewed distribution, $(Q_2 - Q_1) > (Q_3 - Q_2)$.

### 3.2 Standard Normal Distribution

We say that $X$ has a standard normal distribution if $\mu = 0$ and $\sigma = 1$. Tradition dictates that a standard normal random variable is denoted by $Z$. The PDF and CDF of a standard normal are denoted by $\phi(z)$ and $\Phi(z)$.

Any normal distribution can be converted into standard normal distribution using the following formula:

$$ z = \frac {x - \mu}{\sigma} $$  

where $\mu$ and $\sigma$ are the mean and variance of the original normal distribution.

**$z$-score** (also called a **standard score**) gives you an idea of how far from the mean a data point is.

In a standard normal distribution: 
> 68.2% of the values lie within 1 standard deviation of the mean

> 95.4% of the values lie between 2 standard deviations of the mean

> 99.8% lie within 3 standard deviations of the mean

The area under the standard normal distribution between any two points represents the proportion of values that lies between these two points. For instance, the area under the curve on either side of the mean is $0.5$. In other words, $50\%$ of the values lie on either side of the mean.

<center><img src="../figures/norm_dist.png"/></center>

Every $z$-score has an associated $p$-value that tells you the probability of all values below or above that $z$-score occuring. This is the area under the curve left or right of that $z$-score.

<center><img src="../figures/z_score.png"/></center>

Suppose that $X \sim N(3, 5)$. Find $\mathbb{P}(X \geq 1)$. The solution is: 

$$ \mathbb{P}(X > 1) = 1 - \mathbb{P}(X < 1) = 1 - \mathbb{P}\left(Z < \frac{1 - 3}{\sqrt{5}}\right) = 1 - \Phi(-0.8944) = 0.81. $$

```python
# Solve in python
x = 1                               # x value
mu = 3                              # mean
sigma = np.sqrt(5)                  # standard deviation
z = (x - mu) / sigma                # standardize the x value
prob = 1 - ss.norm.cdf(z)           # cumulative distribution function
 
# Print result
print(f"Probability that X is greater than or equal to 1: {prob:.2f}")
```

Now find $q = \Phi^{-1}(0.2)$. 

This means we have to find $q$ such that $\mathbb{P}(X < q) = 0.2$. We solve this by writing

$$ 0.2 = \mathbb{P}(X < q) = \mathbb{P}\left(Z < \frac{q - \mu}{\sigma}\right) = \Phi\left(\frac{q - \mu}{\sigma}\right). $$

From the normal table, $\Phi(−0.8416) = 0.2$. Therefore,

$$ -0.8416 = \frac{q - \mu}{\sigma} = \frac{q - 3}{\sqrt{5}} $$

and hence $q = 3 − 0.8416 \sqrt{5} = 1.1181$. 

```python
# Solve in python
z = ss.norm.ppf(0.2)    # inverse of the CDF of the standard normal distribution at 0.2, which gives z
q = mu + z * sigma      # calculate q using the z-score formula

# Print result
print(f"q: {q:.4f}")
```

### 3.3 Exponential Distribution

$X$ has an Exponential distribution with a rate parameter $\lambda$, denoted by $X \sim \exp(\lambda)$, if

$$ f(x) = \lambda e^{-\lambda x}, \quad x \geq 0 $$

where $\lambda > 0$. The exponential distribution is used to model the lifetimes of electronic components and the waiting times between rare events.

<center><img src="../figures/exp_dist.png"/></center>

The exponential distribution is sometimes parameterized in terms of the scale parameter $\beta = 1 / \lambda$, denoted by $X \sim \exp(\beta)$, if

$$ f(x) = \frac{1}{\beta} e^{-x/\beta}, \quad x \geq 0 $$

where $\beta > 0$.

### 3.4 Gamma Distribution

For $\alpha > 0$, the Gamma function is defined by $\Gamma(\alpha) = \int_{0}^{\infty} y^{\alpha - 1} e^{-y} \, dy$. $X$ has a Gamma distribution with parameters $\alpha$ and $\beta$, denoted by $X \sim \text{Gamma}(\alpha, \beta)$, if

$$ f(x) = \frac{1}{\beta^\alpha \Gamma(\alpha)} x^{\alpha - 1} e^{-x / \beta}, \quad x > 0 $$

where $\alpha, \beta > 0$. 

The exponential distribution is just a $\text{Gamma}(1, \beta)$ distribution. If $X_i \sim \text{Gamma}(\alpha_i, \beta)$ are independent, then $\sum_{i=1}^n X_i \sim \text{Gamma}\left(\sum_{i=1}^n \alpha_i, \beta\right)$.

<center><img src="../figures/gamma_dist.png"/></center>

### 3.5 Beta Distribution

$X$ has a Beta distribution with parameters $\alpha > 0$ and $\beta > 0$, denoted by $X \sim \text{Beta}(\alpha, \beta)$, if

$$ f(x) = \frac{\Gamma(\alpha + \beta)}{\Gamma(\alpha)\Gamma(\beta)} x^{\alpha - 1} (1 - x)^{\beta - 1}, \quad 0 < x < 1. $$

<center><img src="../figures/beta_dist.png"/></center>

### 3.6 $t$ Distribution

$X$ has a $t$ distribution with $\nu$ degrees of freedom, written $X \sim t_{\nu}$, if

$$ f(x) = \frac{\Gamma\left(\frac{\nu + 1}{2}\right)}{\Gamma\left(\frac{\nu}{2}\right)} \frac{1}{(1 + \frac{x^2}{\nu})^{(\nu + 1) / 2}}. $$

The $t$ distribution is similar to a normal distribution but it has thicker tails. In fact, the normal corresponds to a $t$ with $\nu = \infty$.

<center><img src="../figures/t_dist.png"/></center>

### 3.7 $\chi^2$ Distribution

$X$ has a $\chi^2$ distribution with $p$ degrees of freedom, written $X \sim \chi^2_p$, if

$$ f(x) = \frac{1}{\Gamma (p/2) 2^{p/2}} x^{(p/2) - 1} e^{-x / 2}, \quad x > 0. $$

If $Z_1, \ldots, Z_p$ are independent standard Normal random variables, then $\sum_{i=1}^p Z_i^2 \sim \chi^2_p$.

<center><img src="../figures/chi2_dist.png"/></center>
