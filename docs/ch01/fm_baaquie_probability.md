# Probability Distributions in Finance

!!! info "Source"
    **Quantitative Finance for Physicists: An Introduction** by Belal E. Baaquie, Academic Press, 2004.
    These notes are used for educational purposes.

## Probability Distributions

Chapter 3
Probability Distributions
This chapter begins with the basic notions of mathematical statistics
that form the framework for analysis of financial data (see, e.g.,
[1–3]). In Section 3.2, a number of distributions widely used in statis-
tical data analysis are listed. The stable distributions that have become
popular in Econophysics research are discussed in Section 3.3.
3.1 BASIC DEFINITIONS
Consider the random variable (or variate) X. The probability dens-
ity function P(x) defines the probability to find X between a and b
Pr(a  X  b) ¼
ðb
a
P(x)dx
(3:1:1)
The probability density must be a non-negative function and must
satisfy the normalization condition
ð
Xmax
Xmin
P(x)dx ¼ 1
(3:1:2)
where the interval [Xmin, Xmax] is the range of all possible values of X.
In fact, the infinite limits [1, 1] can always be used since P(x) may
17

be set to zero outside the interval [Xmin, Xmax]. As a rule, the infinite
integration limits are further omitted.
Another way of describing random variable is to use the cumulative
distribution function
Pr(X  b) ¼
ðb
1
P(x)dx
(3:1:3)
Obviously, probability satisfies the condition
Pr(X > b) ¼ 1  Pr(X  b)
(3:1:4)
Two characteristics are used to describe probable values of random
variable X: mean (or expectation) and median. Mean of X is the
average of all possible values of X that are weighed with the prob-
ability density P(x)
m  E[X] ¼
ð
xP(x)dx
(3:1:5)
Median of X is the value, M, for which
Pr(X > M) ¼ Pr(X < M) ¼ 0:5
(3:1:6)
Median is the preferable characteristic of the most probable value for
strongly skewed data samples. Consider a sample of lottery tickets
that has one ‘‘lucky’’ ticket winning one million dollars and 999
‘‘losers.’’ The mean win in this sample is $1000, which does not
realistically describe the lottery outcome. The median zero value is a
much more relevant characteristic in this case.
The expectation of a random variable calculated using some avail-
able information It (that may change with time t) is called conditional
expectation. The conditional probability density is denoted by P(xjIt).
Conditional expectation equals
E[XtjIt] ¼
ð
xP(xjIt)dx
(3:1:7)
Variance, Var, and the standard deviation, s, are the conventional
estimates of the deviations from the mean values of X
Var[X]  s2 ¼
ð
(x  m)2P(x)dx
(3:1:8)
18
Probability Distributions

In financial literature, the standard deviation of price is used to
characterize the price volatility.
The higher-order moments of the probability distributions are
defined as
mn  E[Xn] ¼
ð
xnP(x)dx
(3:1:9)
According to this definition, mean is the first moment (m  m1), and
variance can be expressed via the first two moments, s2 ¼ m2  m2.
Two other important parameters, skewness S and kurtosis K, are
related to the third and fourth moments, respectively,
S ¼ E[(x  m)3]=s3, K ¼ E[(x  m)4]=s4
(3:1:10)
Both parameters, S and K, are dimensionless. Zero skewness implies
that the distribution is symmetrical around its mean value. The posi-
tive and negative values of skewness indicate long positive tails and
long negative tails, respectively. Kurtosis characterizes the distribu-
tion peakedness. Kurtosis of the normal distribution equals three.
The excess kurtosis, Ke ¼ K  3, is often used as a measure of devi-
ation from the normal distribution. In particular, positive excess
kurtosis (or leptokurtosis) indicates more frequent medium and large
deviations from the mean value than is typical for the normal distri-
bution. Leptokurtosis leads to a flatter central part and to so-called
fat tails in the distribution. Negative excess kurtosis indicates frequent
small deviations from the mean value. In this case, the distribution
sharpens around its mean value while the distribution tails decay
faster than the tails of the normal distribution.
The joint distribution of two random variables X and Y is the
generalization of the cumulative distribution (see 3.1.3)
Pr(X  b, Y  c) ¼
ðb
1
ðc
1
h(x, y)dxdy
(3:1:11)
In (3.1.11), h(x, y) is the joint density that satisfies the normalization
condition
ð1
1
ð1
1
h(x, y)dxdy ¼ 1
(3:1:12)
Probability Distributions
19

Two random variables are independent if their joint density function
is simply the product of the univariate density functions: h(x, y) ¼
f (x)g(y). Covariance between two variates provides a measure of their
simultaneous change. Consider two variates, X and Y, that have the
means mX and mY, respectively. Their covariance equals
Cov(x, y)  sXY ¼ E[(x  mX)(y  mY)] ¼ E[xy]  mXmY (3:1:13)
Obviously, covariance reduces to variance if X ¼ Y: sXX ¼ sX2.
Positive covariance between two variates implies that these variates
tend to change simultaneously in the same direction rather than in
opposite directions. Conversely, negative covariance between two
variates implies that when one variate grows, the second one tends
to fall and vice versa. Another popular measure of simultaneous
change is the correlation coefficient
Corr(x, y) ¼ Cov(x:y)=(sX sY)
(3:1:14)
The values of the correlation coefficient are within the range [  1, 1].
In the general case with N variates X1, . . . , XN (where N > 2),
correlations among variates are described with the covariance matrix.
Its elements equal
Cov(xi, xj)  sij ¼ E[(xi  mi)(xj  mj)]
(3:1:15)
3.2 IMPORTANT DISTRIBUTIONS
There are several important probability distributions used in quan-
titative finance. The uniform distribution has a constant value within
the given interval [a, b] and equals zero outside this interval
PU ¼
0, x < a and x > b
1=(b  a), a  x  b

(3:2:1)
The uniform distribution has the following mean and higher-order
moments
mU ¼ 0, s2
U ¼ (b  a)2=12, SU ¼ 0, KeU ¼ 6=5
(3:2:2)
The case with a ¼ 0 and b ¼ 1 is called the standard uniform distribu-
tion. Many computer languages and software packages have a library
function for calculating the standard uniform distribution.
20
Probability Distributions

The binomial distribution is a discrete distribution of obtaining n
successes out of N trials where the result of each trial is true with
probability p and is false with probability q ¼ 1  p (so-called Ber-
noulli trials)
PB(n; N, p) ¼ CNn pnqNn ¼ CNnpn(1  p)Nn, CNn ¼
N!
n!(N  n)!
(3:2:3)
The factor CNn is called the binomial coefficient. Mean and higher-
order moments for the binomial distribution are equal, respectively,
mB ¼ Np, s2B ¼ Np(1  p), SB ¼ (q  p)=sB, KeB ¼ (1  6pq)=sB2
(3:2:4)
In the case of large N and large (N  n), the binomial distribution
approaches the form
PB(n) ¼
1
ffiffiffiffiffiffi
2p
p
sB
exp [(x  mB)2=2s2
B], N ! 1, (N  n) ! 1 (3:2:5)
that coincides with the normal (or Gaussian) distribution (see 3.2.9). In
the case with p  1, the binomial distribution approaches the Poisson
distribution.
The Poisson distribution describes the probability of n successes in
N trials assuming that the fraction of successes n is proportional to
the number of trials: n ¼ pN
PP(n, N) ¼
N!
n!(N  n)!
n
N

n
1  n
N

Nn
(3:2:6)
As the number of trials N becomes very large (N ! 1), equation
(3.2.6) approaches the limit
PP(n) ¼ nnen=n!
(3:2:7)
Mean, variance, skewness, and excess kurtosis of the Poisson distri-
bution are equal, respectively,
mP ¼ s2
P ¼ n, SP ¼ n1=2, KeP ¼ n1
(3:2:8)
The normal (Gaussian) distribution has the form
PN(x) ¼
1ffiffiffiffiffiffi
2p
p
s
exp [(x  m)2=2s2]
(3:2:9)
Probability Distributions
21

It is often denoted N(m, s). Skewness and excess kurtosis of the
normal distribution equals zero. The transform z ¼ (x  m)=s con-
verts the normal distribution into the standard normal distribution
PSN(z) ¼
1ffiffiffiffiffiffi
2p
p
exp [z2=2]
(3:2:10)
Note that the probability for the standard normal variate to assume
the value in the interval [0, z] can be used as the definition of the error
function erf(x)
1ffiffiffiffiffiffi
2p
p
ðz
0
exp (x2=2)dx ¼ 0:5 erf(z=
ffiffi
2
p
)
(3:2:11)
Then the cumulative distribution function for the standard normal
distribution equals
PrSN(z) ¼ 0:5[1 þ erf(z=
ffiffi
2
p
)]
(3:2:12)
According to the central limit theorem, the probability density distri-
bution for a sum of N independent random variables with finite
variances and finite means approaches the normal distribution as N
grows to infinity. Due to exponential decay of the normal distribu-
tion, large deviations from its mean rarely appear. The normal distri-
bution plays an extremely important role in all kinds of applications.
The Box-Miller method is often used for modeling the normal distri-
bution with given uniform distribution [4]. Namely, if two numbers
x1 and x2 are drawn from the standard uniform distribution, then
y1 and y2 are the standard normal variates
y1 ¼ [2 ln x1)]1=2 cos (2px2), y2 ¼ [2 ln x1)]1=2 sin (2px2)
(3:2:13)
Mean and variance of the multivariate normal distribution with N
variates can be easily calculated via the univariate means mi and
covariances sij
mN ¼
X
N
i¼1
mi, s2
N ¼
X
N
i, j¼1
sij
(3:2:14)
The lognormal distribution is a distribution in which the logarithm of a
variate has the normal form
22
Probability Distributions

PLN(x) ¼
1
xs
ffiffiffiffiffiffi
2p
p
exp [( ln x  m)2=2s2]
(3:2:15)
Mean, variance, skewness, and excess kurtosis of the lognormal dis-
tribution can be expressed in terms of the parameters s and m
mLN ¼ exp (m þ 0:5s2),
s2
LN ¼ [ exp (s2)  1] exp (2m þ s2),
SLN ¼ [ exp (s2)  1]1=2[ exp (s2) þ 2],
KeLN ¼ exp (4s2) þ 2 exp (3s2) þ 3 exp (2s2)  6
(3:2:16)
The Cauchy distribution (Lorentzian) is an example of the stable distri-
bution (see the next section). It has the form
PC(x) ¼
b
p[b2 þ (x  m)2]
(3:2:17)
The specific of the Cauchy distribution is that all its moments are
infinite. The case with b ¼ 1 and m ¼ 0 is named the standard Cauchy
distribution
PC(x) ¼
1
p[1 þ x2]
(3:2:18)
Figure 3.1 depicts the distribution of the weekly returns of the ex-
change-traded fund SPDR that replicates the S&P 500 index (ticker
SPY) for 1996–2003 in comparison with standard normal distribution
and the standard Cauchy distributions (see Exercise 3).
The extreme value distributions can be introduced with the Fisher-
Tippett theorem. According to this theorem, if the cumulative distri-
bution function F(x) ¼ Pr(X  x) for a random variable X exists,
then
the
cumulative
distribution
of
the
maximum
values
of
X, Hj(x) ¼ Pr(Xmax  x) has the following asymptotic form
Hj(x) ¼
exp [(1 þ j(x  mmax)=smax)1=j], j 6¼ 0,
exp [ exp ((x  mmax)=smax)],
j ¼ 0
(
(3:2:19)
where 1 þ j(x  mmax)=smax > 0 in the case with j 6¼ 0: In (3.2.19),
mmax and smax are the location and scale parameters, respectively;
j is the shape parameter and 1=j is named the tail index. The
Probability Distributions
23

Fisher-Tippett theorem does not define the values of the parameters
mmax and smax. However, special methods have been developed for
their estimation [5].
It is said that the cumulative distribution function F(x) is in the
domain of attraction of Hj(x). The tail behavior of the distribution
F(x) defines the shape parameter. The Gumbel distribution corres-
ponds to the case with j ¼ 0. Distributions with thin tails, such as
normal, lognormal, and exponential distributions, have the Gumbel
domain of attraction. The case with j > 0 is named the Frechet
distribution. Domain of the Frechet attraction corresponds to distri-
butions with fat tails, such as the Cauchy distribution and the Pareto
distribution (see the next Section). Finally, the case with j < 0 defines
the Weibull distribution. This type of distributions (e.g., the uniform
distribution) has a finite tail.
0
0.1
0.2
0.3
0.4
0.5
−6
−4
−2
0
2
4
SPY
Normal
Cauchy
Figure 3.1 The standardized distribution of the weekly returns of the S&P
500 SPDR (SPY) for 1996–2003 in comparison with the standard normal
and the standard Cauchy distributions.
24
Probability Distributions

3.3 STABLE DISTRIBUTIONS AND SCALE
INVARIANCE
The principal property of stable distribution is that the sum of
variates has the same distribution shape as that of addends (see,
e.g., [6] for details). Both the Cauchy distribution and the normal
distribution are stable. This means, in particular, that the sum of
two normal distributions with the same mean and variance is also the
normal distribution (see Exercise 2). The general definition for
the stable distributions was given by Levy. Therefore, the stable
distributions are also called the Levy distributions.
Consider the Fourier transform F(q) of the probability distribution
function f(x)
F(q) ¼
ð
f(x)eiqxdx
(3:3:1)
The function F(q) is also called the characteristic function of the
stochastic process. It can be shown that the logarithm of the charac-
teristic function for the Levy distribution has the following form
ln FL(q) ¼
imq  gjqja[1  ibd tan (pa=2)],
if a 6¼ 1
imq  gjqj[1 þ 2ibd ln (jqj)=p)],
if a ¼ 1
(
(3:3:2)
In (3.3.2), d ¼ q=jqj and the distribution parameters must satisfy the
following conditions
0 < a  2,  1  b  1, g > 0
(3:3:3)
The parameter m corresponds to the mean of the stable distribution
and can be any real number. The parameter a characterizes the
distribution peakedness. If a ¼ 2, the distribution is normal. The
parameter b characterizes skewness of the distribution. Note that
skewness of the normal distribution equals zero and the parameter
b does not affect the characteristic function with a ¼ 2. For the
normal distribution
ln FN(q) ¼ imq  gq2
(3:3:4)
The non-negative parameter g is the scale factor that characterizes the
spread of the distribution. In the case of the normal distribution,
g ¼ s2=2 (where s2 is variance). The Cauchy distribution is defined
Probability Distributions
25

with the parameters a ¼ 1 and b ¼ 0. Its characteristic function
equals
ln FC(q) ¼ imq  gjqj
(3:3:5)
The important feature of the stable distributions with a < 2 is that
they exhibit the power-law decay at large absolute values of the
argument x
fL(jxj)  jxj(1þa)
(3:3:6)
The distributions with the power-law asymptotes are also named the
Pareto distributions. Many processes exhibit power-law asymptotic
behavior. Hence, there has been persistent interest to the stable distri-
butions.
The power-law distributions describe the scale-free processes. Scale
invariance of a distribution means that it has a similar shape on
different scales of independent variables. Namely, function f(x) is
scale-invariant to transformation x ! ax if there is such parameter
L that
f(x) ¼ Lf(ax)
(3:3:7)
The solution to equation (3.3.7) is simply the power law
f(x) ¼ xn
(3:3:8)
where n ¼ ln (L)= ln (a). The power-law function f(x) (3.3.8) is scale-
free since the ratio f(ax)=f(x) ¼ L does not depend on x. Note that the
parameter a is closely related to the fractal dimension of the function
f(x). The fractal theory will be discussed in Chapter 6.
Unfortunately, the moments of stable processes E[xn] with power-
law asymptotes (i.e., when a < 2) diverge for n  a. As a result, the
mean of a stable process is infinite when a  1. In addition, variance
of a stable process is infinite when a < 2. Therefore, the normal
distribution is the only stable distribution with finite mean and finite
variance.
The stable distributions have very helpful features for data analysis
such as flexible description of peakedness and skewness. However, as it
was mentioned previously, the usage of the stable distributions in
financial applications is often restricted because of their infinite vari-
ance at a < 2. The compromise that retains flexibility of the Levy
26
Probability Distributions

distribution yet yields finite variance is named truncated Levy flight.
This distribution is defined as [2]
fTL(x) ¼
0,
jxj > ‘
CfL(x),
‘  x  ‘

(3:3:9)
In (3.3.9), fL(x) is the Levy distribution ‘ is the cutoff length, and C is
the normalization constant. Sometimes the exponential cut-off is used
at large distances [3]
fTL(x)  exp (  ljxj), l > 0, jxj > ‘
(3:3:10)
Since fTL(x) has finite variance, it converges to the normal distribu-
tion according to the central limit theorem.
3.4 REFERENCES FOR FURTHER READING
The Feller’s textbook is the classical reference to the probability
theory [1]. The concept of scaling in financial data has been advocated
by Mandelbrot since the 1960s (see the collection of his work in [7]).
This problem is widely discussed in the current Econophysics litera-
ture [2, 3, 8].
3.5 EXERCISES
1. Calculate the correlation coefficients between the prices of
Microsoft (MSFT), Intel (INTC), and Wal-Mart (WMT). Use
monthly closing prices for the period 1994–2003. What do you
think of the opposite signs for some of these coefficients?
2. Familiarize yourself with Microsoft Excel’s statistical tools. As-
suming that Z is the standard normal distribution: (a) calculate
Pr(1  Z  3) using the NORMSDIST function; (b) calculate x
such that Pr(Z  x) ¼ 0:95 using the NORMSINV function; (c)
calculate x such that Pr(Z  x) ¼ 0:15; (d) generate 100 random
numbers from the standard normal distribution using Tools/
Data Analysis/Random Number Generation. Calculate the
sample mean and standard variance. How do they differ from
the theoretical values of m ¼ 0 and s ¼ 1, respectively? (e) Do
the same for the standard uniform distribution as in (d).
Probability Distributions
27

(f) Generate 100 normally distributed random numbers x using
the function x ¼ NORMSINV(z) where z is taken from a sample
of the standard uniform distribution. Explain why it is possible.
Calculate the sample mean and the standard deviation. How do
they differ from the theoretical values of m and s, respectively?
3. Calculate mean, standard deviation, excess kurtosis, and skew
for the SPY data sample from Exercise 2.1. Draw the distribu-
tion function of this data set in comparison with the standard
normal distribution and the standard Cauchy distribution.
Compare results with Figure 3.1.
Hint: (1) Normalize returns by subtracting their mean and divid-
ing the results by the standard deviation. (2) Calculate the histo-
gram using the Histogram tool of the Data Analysis menu. (3)
Divide the histogram frequencies with the product of their sum and
the bin size (explain why it is necessary).
4. Let X1 and X2 be two independent copies of the normal distri-
bution X  N(m, s2). Since X is stable, aX1 þ bX2  CX þ D.
Calculate C and D via given m, s, a, and b.
28
Probability Distributions

