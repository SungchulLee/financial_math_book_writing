# Copula Methods: Estimation, Credit Risk & Option Pricing

!!! info "Source"
    **Copula Methods in Finance** by Umberto Cherubini, Elisa Luciano, and Walter Vecchiato, Wiley, 2004.
    These notes are used for educational purposes.

## Estimation and Calibration from Market Data

150
Copula Methods in Finance
As a consequence of the previous theorem, we can give the following:
Definition 4.14
Let ϕ be a strict generator, with ϕ−1 completely monotonic on [0, ∞].
Then an n-variate Archimedean copula is the function
C(u1, u2, . . . , un) = ϕ−1(ϕ(u1) + ϕ(u2) + · · · + ϕ(un))
As in the bi-dimensional case, an important source of generators for Archimedean n-copulas
consists of the inverses of the Laplace transforms of c.d.f.s, as proved by the following
theorem:
Theorem 4.11 (Feller, 1971)
A function ϕ on [0, ∞] is the Laplace transform of a c.d.f.
F if and only if ϕ is completely monotonic and ϕ (0) = 1.
It is fairly simple to generate multivariate Archimedean copulas according to the previous
definition: however, they have the limit that there are only one or two parameters to capture
the dependence structure.3
Gumbel n-copula
The generator is given by ϕ(u) = (−ln(u))α, hence ϕ−1(t) = exp(−t
1
α ); it is completely
monotonic if α > 1. The Gumbel n-copula is therefore:
C(u1, u2, . . . , un) = exp


−
 n

i=1
(−ln ui)α
! 1
α



with α > 1
(4.15)
Clayton n-copula
The generator is given by ϕ(u) = u−α −1, hence ϕ−1(t) = (t + 1)−1
α ; it is completely
monotonic if α > 0. The Clayton n-copula is therefore:
C(u1, u2, . . . , un) =
 n

i=1
u−α
i
−n + 1
!−1
α
with α > 0
(4.16)
Frank n-copula
The generator is given by
ϕ(u) = ln
exp (−αu) −1
exp (−α) −1

hence
ϕ−1(t) = −1
α ln

1 + et(e−α −1)
	
3 A more general definition, overcoming this restriction, could also be given.

Multivariate Copulas
151
it is completely monotonic if α > 0. The Frank n-copula is given by:
C(u1, u2, . . . , un) = −1
α ln



1 +
n

i=1

e−αui −1
	

e−α −1
	n−1



with α > 0 when n ⩾3
(4.17)


5
Estimation and Calibration from Market Data
5.1
STATISTICAL INFERENCE FOR COPULAS
From a statistical point of view, a copula function is basically a very simple expression of
a multivariate model and, as for most multivariate statistical models, much of the classical
statistical inference theory is not applicable. The only theory that can be applied is the
asymptotic maximum likelihood estimation (MLE). In addition, there are other possible
ad hoc estimation methods that were proposed for overwhelming the hard computational
efforts to get exact MLEs. These methods share, and also mix, concepts from non-parametric
statistical inference and simulation techniques.
This section is devoted to statistical inference theory applied to copula models. We first
describe the Exact Maximum Likelihood Estimator and introduce some deviations from
that. Now, we would like to observe that every estimation method that we are going to
describe often requires a numerical optimization of the objective function, because a copula
is intrinsically a multivariate model and its likelihood involves mixed derivatives.
Copulas represent a powerful tool for tackling the problem of how to describe a joint
distribution because, as evidenced in Chapter 2, they let the researcher deal separately with
the needs of marginal and joint distribution modeling. Thus, one can choose for each data
series the marginal distribution that best fits the sample, and afterwards put everything
together using a copula function with some desirable properties. A potential problem comes
from the simple fact that the number of combinations that can be made has virtually no
limit, and one can easily get lost looking for the best combination of the marginals and
the copula. This is why we will present some non-parametric methods to model both the
margins and the copula. It is required that they have enough data since every non-parametric
method performs much better when data are not scarce, and the main advantage is to let
the dataset express the copula without any subjective choice.
In this chapter we will focus on continuous random variables. It should be noted that the
assumption of continuity is not always required, but it simplifies some of the presentation.
As in the previous chapters, we will denote throughout the cumulative distribution function
(or c.d.f.) of a random variable (or r.v.) using an uppercase letter, and the corresponding
probability density function (or p.d.f.) using a lowercase letter. We will still consider all
r.v.s to be distributed in the extended real line.
When we extend this framework in a time series context, especially when we present some
empirical application to financial time series, we will consider a strictly stationary stochastic
process {Yt, t ∈Z} taking values in Rn and assume that our data consist in a realization of
n-dimensional real vectors {Yt, t = 1, 2, . . . , T }. These data, for example, may correspond
to observed returns of n financial assets, say stock indexes, at different dates.
We denote by f (y), F(y), respectively, the (joint) p.d.f. and the (joint) c.d.f. of Yt =
(Y1t, Y2t, . . . , Ynt)′ at point y = (y1, y2, . . . , yn)′.
The marginal (univariate) p.d.f. and c.d.f. of each element Yjt at point yj with j =
1, 2, . . . ., n will be denoted by fj(yj) and Fj(yj), respectively.
In the following we will consider the case where the marginals Fj are continuous.

154
Copula Methods in Finance
5.2
EXACT MAXIMUM LIKELIHOOD METHOD
Before introducing this important estimation method it is worth recalling the following
canonical representation presented in Chapter 4:
f (x1, x2, . . . , xn) = c(F1(x1), F2(x2), . . . , Fn(xn)) ·
n

j=1
fj(xj)
(5.1)
where
c(F1(x1), F2(x2), . . . , Fn(xn)) = ∂n(C(F1(x1), F2(x2), . . . , Fn(xn)))
∂F1(x1)∂F2(x2) . . . ∂Fn(xn)
(5.2)
is the nth mixed partial derivative of the copula C, c is the copula density and f is the
standard univariate probability density function.
This canonical representation for the multivariate density function permits us to say that,
in general, a statistical modeling problem for copulas could be decomposed into two steps:
• identification of the marginal distributions;
• definition of the appropriate copula function.
This is an important point, to begin with, for estimation issues as we will see below.
Let ℵ= {x1t, x2t, . . . , xnt}T
t=1 be the sample data matrix. Thus, the expression for the
log-likelihood function is
l(θ) =
T

t=1
ln c(F1(x1t), F2(x2t), . . . , Fn(xnt)) +
T

t=1
n

j=1
ln fj(xjt)
(5.3)
where θ is the set of all parameters of both the marginals and the copula.
Hence, given a set of marginal p.d.f.s and a copula the previous log-likelihood may be
written, and by maximization we obtain the maximum likelihood estimator:
ˆθMLE = max
θ∈ l(θ)
(5.4)
Throughout this section, we assume that the usual regularity conditions (see Serfling,
1980 and Shao, 1999) for asymptotic maximum likelihood theory hold for the multivari-
ate model (i.e. the copula) as well as for all of its margins (i.e. the univariate p.d.f.s).
Under these regularity conditions the maximum likelihood estimator exists and it is con-
sistent and asymptotically efficient; also, it verifies the property of asymptotically normal,
and we have:
√
T (ˆθMLE −θ0) →N(0, ℑ−1 (θ0))
(5.5)
with ℑ(θ0) the usual Fisher’s information matrix and θ0 the usual true value.

Estimation and Calibration from Market Data
155
The covariance matrix of ˆθMLE (Fisher’s information matrix) may be estimated by the
inverse of the negative Hessian matrix of the likelihood function.
5.2.1
Examples
Example 5.1 [Multivariate Gaussian copula]
Let R be a symmetric, positive definite mat-
rix with diag(R) = (1, 1, . . . , 1)′, R the standardized multivariate normal distribution with
correlation matrix R and let  denote the c.d.f. of a standard Gaussian or normal variable.
The MGC, as defined in the previous chapter, is as follows:
C(u1, u2, . . . , un; R) = R(−1(u1), −1(u2), . . . , −1(un))
(5.6)
with density:
1
(2π)
n
2 |R|
1
2
exp(−1
2x′R−1x) = c((x1), (x2), . . . , (xn)) ·
n
j=1

1
√
2π exp(−1
2x2
j )

(5.7)
We deduce that:
c((x1), (x2), . . . , (xn)) =
1
(2π)
n
2 |R|
1
2
exp(−1
2x′R−1x)
n
j=1

1
√
2π exp(−1
2x2
j )

(5.8)
Let uj = (xj), so xj = −1(uj) and we can rewrite as follows:
c(u1, u2, . . . , un) =
1
|R|
1
2
exp(−1
2ς′(R−1 −I)ς)
(5.9)
where ς =

−1(u1), −1(u2), . . . , −1(un)
′.
In this case, let ℵ= {x1t, x2t, . . . , xnt}T
t=1 be the sample data matrix, and the expression
for the log-likelihood function is:
l(θ) = −T
2 ln |R| −1
2
T

t=1
ς′
t(R−1 −I)ςt
(5.10)
where θ is the set of all parameters: R and ςt =

−1(u1t), −1(u2t), . . . , −1(unt)
′.
The MLE of R is given by (refer to Magnus & Neudecker, 1980):
ˆRMLE = 1
T
T

t=1
ς′
tςt
(5.11)

156
Copula Methods in Finance
Example 5.2 [Multivariate dispersion copula with Weibull margins]
As recalled in Chap-
ter 4, let µ = (µ1, µ2, . . . , µn)′ be a position parameter, σ 2 =

σ 2
1 , σ 2
2 , . . . , σ 2
n
′ a disper-
sion parameter and R a correlation matrix.
We say that X ∼MDC(µ, σ 2, R) if
f (y; µ, σ 2, R) =
1
|R|
1
2
exp(−1
2ς′(R−1 −I)ς)
n
j=1
fj(yj; µj, σ 2
j )
(5.12)
where
ςj = −1(Fj(yj; µj, σ 2
j ))
for j = 1, 2, . . . , n
and
fj(yj; µj, σ 2
j ) =
∂Fj(yj; µj, σ 2
j )
∂yj
for every set of c.d.f. Fj

yj; µj, σ 2
j

Assuming Weibull margins, we saw in Chapter 4 that we obtain the MDC density:
f (x1, x2, . . . , xn) =
1
|R|
1
2
exp(−1
2ς′(R−1 −I)ς)
n

j=1
αjx
αj −1
j
βj
exp

−

x
αj
j
βj
		
(5.13)
where ςj = −1

1 −exp

−
x
αj
j
βj

.
In this case the log-likelihood function may be easily derived:
l(R, α, β) = −T
2 ln |R| −1
2
T

t=1
ς′
t(R−1 −I)ςt +
T

t=1
n

j=1
ln

αjx
αj −1
jt
βj
exp

−
x
αj
jt
βj
	

(5.14)
with ςjt = −1

1 −exp

−
x
αj
jt
βj

.
This log-likelihood function has to be maximized with respect to all parameters (R, α,
β) by using a numerical optimization method.
5.3
IFM METHOD
The maximum likelihood method, previously shown, could be very computationally inten-
sive, especially in the case of a high dimension, because it is necessary to estimate jointly
the parameters of the marginal distributions and the parameters of the dependence structure
represented by the copula. But, if the readers look more closely at the log-likelihood func-
tion, they will note that it is composed by two positive terms: one term involving the copula
density and its parameters, and one term involving the margins and all parameters of the
copula density. For that reason, Joe and Xu (1996) proposed that these set of parameters
should be estimated in two steps:

Estimation and Calibration from Market Data
157
1. As a first step, they estimate the margins’ parameters θ1 by performing the estimation
of the univariate marginal distributions:
ˆθ1 = ArgMaxθ 1
T

t=1
n

j=1
ln fj(xjt; θ1)
(5.15)
2. As a second step, given ˆθ1, they perform the estimation of the copula parameter θ2:
ˆθ2 = ArgMaxθ2
T

t=1
ln c(F1(x1t), F2(x2t), . . . , Fn(xnt); θ2, ˆθ1)
(5.16)
This method is called inference for the margins or IFM. The IFM estimator is defined as
the vector:
ˆθIFM =

ˆθ1, ˆθ2
′
(5.17)
We call l the entire log-likelihood function, lj the log-likelihood of the jth marginal, and
lc the log-likelihood for the copula itself. Hence, the IFM estimator is the solution of:

 ∂l1
∂θ11
, ∂l2
∂θ12
, . . . , ∂ln
∂θ1n
, ∂lc
∂θ2

= 0′
(5.18)
while the MLE comes from solving

 ∂l
∂θ11
, ∂l
∂θ12
, . . . , ∂l
∂θ1n
, ∂l
∂θ2

= 0′
(5.19)
so, the equivalence of the two estimators, in general, does not hold.
The readers can note that for MGC with correlation matrix R and univariate N(µj, σ 2
j )
margins, the two estimators coincide.
It is simple to see that the IFM estimator provides a good starting point for obtaining an
exact MLE.
Since it is computationally easier to obtain the IFM estimator than the MLE, it is worth
addressing a question about the IFM asymptotic efficiency compared with the MLE. Thus,
one has to compare the asymptotic covariance matrix of the two estimators.
The IFM theory is a special case of using a set of appropriate inference equations to
estimate a vector of parameters. In this case each equation is a score function (i.e. its left
side is the partial derivative of the log-likelihood of each marginal density).
Joe (1997) proves that, like the MLE, the IFM estimator verifies, under regular conditions,
the property of asymptotic normality, and we have:
√
T

ˆθIFM −θ0

→N

0, G¸ −1 (θ0)

(5.20)
with G¸ (θ0) the Godambe information matrix.

158
Copula Methods in Finance
Thus, if we define a score function
s(θ) =

 ∂l1
∂θ11
, ∂l2
∂θ12
, . . . , ∂ln
∂θ1n
, ∂lc
∂θ2
′
splitting the log-likelihood in two parts l1, l2, . . . , ln for each margin and lc for the copula,
the Godambe information matrix takes the following form:
G¸ (θ0) = D−1V (D−1)′
(5.21)
with
D = E
∂s(θ)
∂θ

and
V = E

s(θ)s(θ)′
The estimation of this covariance matrix requires us to compute many derivatives. Joe
(1997) then suggests the use of the jacknife method or other bootstrap methods to estimate
it. In a time series context, it may be useful to adopt a block-bootstrap, especially when the
time series in hand show a low autocorrelation (see Efron & Tibshirani, 1993 and Shao &
Tu, 1995, for a deeper and more formal explanation of these concepts).
Joe (1997) points out that the IFM method is highly efficient compared with the ML
method. It is worth noting that the IFM method may be viewed as a special case of the
generalized method of moments (GMM) with an identity weight matrix (Davidson & Mac-
Kinnon, 1993).
5.3.1
Application: estimation of the parametric copula for market data
In this section we present an empirical application1 of parametric copula modeling to the
following five assets: DAX 30 index, S&P 500 index, 10-year total return index for the US
bond market, 10-year total return index for the German bond market, and the DEM/USD
exchange rate.
We use weekly (average) data from January 1992 to June 2001; in total we have a
sample of 248 observations. Table 5.1 reports some descriptive statistics for each weekly
return series. JB is the Jarque–Bera Gaussianity test statistic.
Table 5.1
Dax30
S&P500
Ger10y
USA10y
DEM/$
Mean
0.53
0.43
0.30
0.27
0.16
Std
3.56
2.68
0.90
1.04
2.04
Skew
−0.40
−0.45
−0.55
−0.18
0.13
Kurtosis
3.22
4.00
3.44
2.75
3.38
JB Statistics
0.0288
0.0000
0.0007
0.3879
0.3204
1 This example is borrowed from Cazzulani, Meneguzzo and Vecchiato (2001). The data have already been used
in the previous chapters in order to compute some concordance measures. In the following, this example will be
extended for further comments and more detailed discussions.

Estimation and Calibration from Market Data
159
Results for the mean and standard deviations are reported in the table in percentage
points. The Jarque–Bera test is the best-known normality test. Our strategy will be to
model the joint dependence using a Frank copula because it is a simple Archimedean
copula and, in the bivariate case, allows for both positive and negative dependence. As for
the marginal behavior, we can consider the use of a Student t in order to capture a high
kurtosis. Unfortunately the Student t is a symmetric distribution and it would fail to capture
the negative skewness. At first sight, it may seem more appropriate then to use a non-central
Student t, so that we can allow for a negative skewness. We present its p.d.f. below:
f (x) =
(υ)υ/2 exp

−δ2/2

(υ/2)π1/2(υ + x2)(υ+1)/2 ·
∞

i=0


υ + i + 1
2
 
xδ
i!
i 
2
υ + x2
i/2
(5.22)
where  is the Euler function.
We, indeed, choose to adopt a non-central t density for a more general setting due to
asymmetry and kurtosis sample characteristics.
Here δ is the non-centrality parameter, which can range between −∞and +∞; and υ is
the usual parameter for the degrees of freedom. It is worth noting that a Student t distribution
converges to the standard normal distribution when the degrees of freedom tend to infinity. We
standardize our returns so that they have zero mean and unit standard deviation. We then fit a
normal distribution, a Student’s t and a non-central t distribution to these normalized data.
Table 5.2 gives the parameter estimates for the margins via MLE, first considering a non-
central t and then considering a (central) standard t. All estimates, except δ, are statistically
significant.
As can be seen in the table, the difference in the estimated degrees of freedom is small
due to almost zero estimates for the non-centrality parameter. All degrees of freedom imply
a marginal behavior close to normal.
We now turn our attention to the copula modeling, and, following the IFM estimation
technique, we have estimated the relevant parameters for the marginal distributions (refer
to Table 5.2), and we now estimate the Frank copula via maximum likelihood.
The optimization problem is as follows:
max
α
L(α) =
T

t=1
2 log

1 −e−α −(1 −e−αϝ(x1t,υ1,δ1))(1 −e−αϝ(x2t,υ2,δ2))

−log(α(1 −e−α)) −α [ϝ(x1t, υ1, δ1) + ϝ(x2t, υ2, δ2)]
(5.23)
Table 5.2
Marginal estimation – standardized returns
DAX
S&P 500
GER10y
USA10y
DEM/USD
NC Student t
υ
78.10
20.10
44.79
300.00
41.01
δ
0.00
0.01
0.00
0.00
−0.01
Student t
υ
78.79
20.23
45.40
300.00
41.06

160
Copula Methods in Finance
Table 5.3
Estimated α for the Frank copula with NC-t marginals
DAX 30
S&P 500
GER10y
USA10y
DEM/USD
DAX 30
−
S&P 500
5.12
−
GER10y
1.17
1.03
−
USA10y
0.23
1.32
3.72
−
DEM/USD
2.05
1.28
0.44
−1.10
−
where x1t and x2t are the returns on the first and second asset considered, α is the copula
parameter, ϝ is the non-central t c.d.f., υ1, υ2, δ1, δ2 are respectively the degrees of freedom
and non-centrality parameters for the two marginal distributions.
We report, in Table 5.3, the MLE estimates for the α parameter for the Frank copula. We
draw the readers’ attention to the substantial stability of these estimates between central and
non-central Student t distributions. All estimates are statistically significant.
5.4
CML METHOD
We wish to remark that the copula parameters may be estimated without specifying the
marginals. In fact, another estimation method consists in transforming the sample data
{x1t, x2t, . . . , xnt}T
t=1 into uniform variates {u1t, u2t, . . . , unt}T
t=1 and then estimating the
copula parameters. This method may be described as follows:
1. First estimate the marginals using the empirical distributions (without assumptions on
the parametric form for each of them), i.e. ˆFi(xit) with i = 1, . . . , n.
2. Estimate via MLE the copula parameters
ˆθ2 = ArgMaxθ2
T

t=1
ln c( ˆF1(x1t), ˆF2(x2t), . . . , ˆFn(xnt); θ2)
(5.24)
This method is called the Canonical Maximum Likelihood or CML. In this case, the CML
estimator could be viewed as an MLE, given the observed margins.
5.4.1
Application: estimation of the correlation matrix for a Gaussian copula
Using the dataset of the previous example, we wish to estimate the correlation matrix
parameter of the Gaussian copula (MGC) with the CML method. We proceed as follows.
1. Transform the original data into Gaussian data:
(i) estimate the empirical distribution functions (uniform transformation) using order
statistics;
(ii) generate Gaussian values by applying the inverse of the normal distribution to the
empirical distribution functions.
2. Compute the correlation matrix of the transformed data.
The estimated correlation matrix is shown in Table 5.4.

Estimation and Calibration from Market Data
161
Table 5.4
Estimated correlation matrix via CML method for MGC
DAX 30
DEM/USD
GER10y
S&P 500
USA10y
DAX 30
1
DEM/USD
0.3035
1
GER10y
0.1998
0.0551
1
S&P 500
0.6494
0.1501
0.1941
1
USA10y
0.0019
−0.2144
0.4850
0.1585
1
5.5
NON-PARAMETRIC ESTIMATION
In this section we no longer assume a particular parametric copula. Our interest is in
modeling the dependence structure with consistency to find, for example, an appropriate
non-parametric method to estimate the copula form that is going to converge (in a certain
formal probabilistic sense) to the underlying dependence structure.
5.5.1
The empirical copula
Here we present the notion of the empirical copula introduced by Deheuvels (1979, 1981).
Let Xt = (X1t, X2t, . . . , Xnt) ∈ℜn be an i.i.d. sequence with (continuous) c.d.f. F and
(continuous) margins Fj. Let {x(t)
1 , x(t)
2 , . . . , x(t)
n } be the order statistic and let {r(t)
1 , r(t)
2 , . . . ,
r(t)
n } be the rank statistic of the sample, which are linked by the relationship x(rt
n)
n
= xnt,
t = 1, 2, . . . , T .
Definition 5.1 [Deheuvels’ empirical copula]
The empirical copula defined on the lattice
ℓ=

t1
T , t2
T , . . . , tn
T

: 1 ⩽j ⩽n, tj = 0, 1, . . . , T

(5.25)
is the following function:
ˆC

t1
T , t2
T , . . . , tn
T

= 1
T
T

t=1
n

j=1
1

rt
j ⩽tj

(5.26)
where 1 is the indicator function that takes value equal to 1 when its argument condition is
satisfied.
Deheuvels (1978, 1981) proves that the empirical copula converges uniformly to the
underlying copula.
The analog of the Radon–Nikodym density for the empirical copula is the following
empirical copula frequency, as defined by Nelsen (1999):
ˆc

t1
T , t2
T , . . . , tn
T

=
2

i1=1
2

i2=1
. . .
2

in=1
(−1)
n
j=1 ij
× ˆC

t1 −i1 + 1
T
, t2 −i2 + 1
T
, . . . , tn −in + 1
T

(5.27)

162
Copula Methods in Finance
Nelsen (1999) notes that the concept of empirical copula permits us to define the sample
version of many dependence measures and, also, the sample version of other concepts
expressed in terms of copulas. Besides that, empirical copulas may also be used to construct
non-parametric tests for independence (Deheuvels, 1981).
Polynomial approximation for copula
It is possible to use certain polynomial approximations that lead to a stronger convergence
than uniform convergence in order to estimate the underlying dependence structure. For
example, by using the Bernstein polynomial
Bi,n (x) =

n
i

xi(1 −x)n−i
(5.28)
we can define a Bernstein copula as follows:
BT (C)(u1, u2, . . . , un) =
n

t1=1
n

t2=1
. . .
n

tn=1
Bt1,T (u1) · Bt2,T (u2) · · · · · Btn,T (un)
× ˆC

t1
T , t2
T , . . . , tn
T

(5.29)
The Bernstein copula uniformly converges to the underlying copula (refer to Li et al., 1997).
5.5.2
Kernel copula
In statistics a lot of non-parametric estimation methods are based on a kernel structure (see
Hardle, 1990, for a further explanation). Kernel means a functional form, usually chosen
for its smooth properties, that is used as the building block to get the desired estimator.
Scaillet (2000) proposes a kernel-based approach to apply to a copula setup, that has
the advantage of providing a smooth differentiable estimate of the copula function without
assuming any particular parametric a priori on the dependence structure between marginals.
The approach is developed in the context of multivariate stationary processes satisfying
strong mixing conditions (see Serfling, 1980 and Shao, 1999). Once estimates of copulas
(and their derivatives) are available, other concepts expressed in terms of copulas may be
empirically analyzed. The most important point is the need for differentiability that dictates
the choice of a kernel approach.
Non-parametric estimators of copulas may also lead to testing procedures for inde-
pendence between margins in the same spirit as kernel-based methods to test for serial
dependence for a univariate stationary time series (see Tjostheim, 1996).
Estimating a copula is indeed estimating values taken by a c.d.f. at m distinct points in
ℜn by the formula:
C(u1, u2, . . . , un) = F(F −1
1 (u1), F −1
2 (u2), . . . , F −1
n (un))
(5.30)
where F −1
1 , F −1
2 , . . . , F −1
n
are quasi-inverses of F1, F2, . . . , Fn.

Estimation and Calibration from Market Data
163
For given uij ∈(0, 1) , i = 1, 2, . . . , m; j = 1, 2, . . . , n, we assume that the c.d.f. Fj of
Yjt is such that equation Fj (y) = uij admits a unique solution denoted by ξij. As commonly
known, kernels are real bounded and symmetric functions kij(x) on ℜsuch that

ℜ
kij(x) dx = 1,
i = 1, 2, . . . , m;
j = 1, 2, . . . , n
(5.31)
and
Ki (x; h) =
n

j=1
kij

 xj
hj

,
i = 1, 2, . . . , m
(5.32)
where the bandwidth h is a diagonal matrix with elements {hj}j=1,2,...,n and determinant
|h|, while the individual bandwidth hj are positive functions of T such that
|h| +
1
T |h| →0 as T →∞
(5.33)
The p.d.f. of Yjt at yij, i.e. fj(yij), will be estimated by
ˆfj

yij

=
1
T hj
T

t=1
kij

yij −Yjt
hj

(5.34)
while the joint p.d.f. of Yt at yi = (yi1, yi2, . . . , yin)′ will be estimated by
ˆf (yi) =
1
T |h|
T

t=1
Ki (yi −Yt; h) =
1
T |h|
T

t=1
n

j=1
kij

yij −Yjt
hj

(5.35)
Hence, the estimator of the c.d.f. of Yjt at distinct points yij is obtained as
ˆFj

yij

=
 yij
−∞
ˆfj (x) dx
(5.36)
while estimators of the c.d.f. of Yt at yi = (yi1, yi2, . . . , yin)′ will be obtained as
ˆF(yi) =
 yi1
−∞
 yi2
−∞
. . .
 yin
−∞
ˆf (x) dx
(5.37)
If a single Gaussian kernel kij (x) = ϕ(x) =
1
√
2π exp

−x2
2

is adopted, we get
ˆFj

yij

=
1
T hj
T

t=1


yij −Yjt
hj

(5.38)

164
Copula Methods in Finance
and
ˆF(yj) =
1
T |h|
T

t=1
n

j=1


yij −Yjt
hj

(5.39)
where ϕ and  denote, respectively, the p.d.f. and c.d.f. of a standard Gaussian variable.
In order to estimate the copula at distinct points ui, i = 1, 2, . . . , m with uij < ulj for
i < l, we use a “plug-in” method as follows:
ˆC(ui) = ˆF

ˆξi

(5.40)
where
ˆξi =

ˆξi1, ˆξi2, ˆξi3, . . . , ˆξin
′
and
ˆξij = infy∈ℜ

y : ˆFj (y) ⩾uij

The estimate ˆξij corresponds to a kernel estimate of the quantile of Yjt with probability
level uij.
Scaillet (2000), following Robinson (1983), derives the asymptotic distribution (asymp-
totic normality), under regularity conditions, for these kernel estimators, and also derives
the asymptotic distribution of kernel estimators of some bivariate dependence measures.
Indeed, Kendall’s τ, Spearman’s ρ, Gini’s γ , Blomqvist’s β have been written in copula
terms in Chapter 3. Also Schweitzer–Wolff’s σ and Hoeffding’s φ may be expressed in
terms of copula as follows:
σ = 12

I2 |C(u1, u2) −u1u2| du1 du2
(5.41)
φ = 3

10

I2(C(u1, u2) −u1u2)2 du1 du2
(5.42)
Other dependence concepts may also be expressed in terms of copula: as we saw in
Chapter 3, positive quadrant dependency, the left tail decreasing property and upper tail
dependency.
Once a copula is empirically estimated, it is easy to compute the kernel counterpart of
all of these dependence measures, and all other properties may be checked at least locally.
Scaillet (2000) proves, under regular conditions (Robinson, 1983), that kernel estimators
of Spearman’s rho, Gini’s gamma and Blomqvist’s beta are asymptotically independent
standard normal random variables.
Finally, we note that this non-parametric method may be combined with other parametric
methods for estimating a copula and margins (commonly known as mixed estimators).
Application to equity market data
We are going to use this approach to estimate the copula using the previous sample dataset.
Our finding is that this approach provides a better fit to the data and is also more flexible.

Estimation and Calibration from Market Data
165
−12
−10
−8
−6
−4
−2
0
2
4
6
8
−2
−1
0
1
2
3
Contours of Estimated Copula - 1% 5% 25% 50% 75% 80%
S&P 500
10-Year US Bond
Figure 5.1
Contours for the non-parametric copula (contours of S&P 500–US bond 10y)
−12
−10
−8
−6
−4
−2
0
2
4
6
8
−10
−5
0
5
10
Contours of Estimated Copula - 1% 5% 25% 50% 75% 80%
S&P 500
DAX
Figure 5.2
Contours for the non-parametric copula (contours of S&P 500–DAX)
The kernel approach requires a long series of data but it permits a more efficient estimate
of the copula structure implied by the sample observations.
Figures 5.1 and 5.2 show the level curves from a copula estimated non-parametrically. It
can be seen that while the estimated dependence between the two equity indexes is fairly
regular, the dependence between total return on bonds and stock index is more irregular. An
interesting point to be noted is that the normal distribution approximates well the middle of
the distribution but performs very poorly on the tails; this point may be seen by looking at
the lower contour and its irregular form.

166
Copula Methods in Finance
Table 5.5
Spearman’s rho calculated using non-parametric copula
DAX 30
S&P 500
GER10y
USA10y
DEM/USD
DAX 30
−
S&P 500
0.54
−
GER10y
0.14
0.11
−
USA10y
0.02
0.16
0.43
−
DEM/USD
0.26
0.17
0.01
−0.15
−
In Table 5.5 we compute Spearman’s rho implied by the non-parametric estimated copula.
Readers will note that there are very small differences between the implied measures and
their sample counterparts.2
In the following we report the graphs for the estimation of the PQD measures, the implied
c.d.f.s for maximum and minimum, and also some other results such as the left tail decreasing
property described in Chapter 3 (Figures 5.3–5.6). We also present the trace of a copula,
defined as a function C(u, u) = h(u) of a single variable u ∈[0, 1].
We note that, at first sight, the form of each copula may seem similar, but the readers
should observe that each copula extends to different interval values for each axis. So, a
given region in the plane has different probability induced by each estimated kernel copula,
though their form is similar.
The same argument applies to all other diagrams.
We also report a trace of the non-parametric estimate for a copula for a trivariate case
(S&P 500, 10-year US bond and 10-year German bond) whose values are reported in
Figure 5.7.
Application to value at risk for an asset portfolio
Given these preliminary results we move on to estimate the value at risk, given a confidence
level θ, for a portfolio of n assets. For instance, we consider a portfolio of two assets. Let
x1 and x2 be their respective returns, and β ∈(0, 1) the allocation weight, so the portfolio
return is given by zt = βx1t + (1 −β) x2t where, omitting the subscript t,
F(x1, x2) = Pr(X1 ⩽x1, X2 ⩽x2)
= Pr(F1 (X1) ⩽F1 (x1) , F2 (X2) ⩽F2 (x2)) = C(F1 (x1) , F2 (x2))
and by derivation, we express in term of p.d.f.s:
f (x1, x2) = c(F1(x1), F2(x2)) ·
2

j=1
fj(xj)
where c is the copula-density and f is the standard univariate probability density function.
2 We discuss the sample dependence measure in the next section by introducing another useful estimation method.

Estimation and Calibration from Market Data
167
(a)
(b)
(c)
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
u
C (u,u)
Trace C (u, u)
−12
−10
−8
−6
−4
−2
0
2
4
6
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
a
FMIN(a)
Distribution of min
−12
−10
−8
−6
−4
−2
0
2
4
6
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
a
FMAX(a)
Distribution of max
1
0.8
0.6
y2
C(F1(y1),F2(y2))
y1
u2
u1
Left Tail Dependence of Y1 in Y2
Positive Quadrant Dependence
Estimated Copula
0.4
0.2
0
10
0.1
0.08
0.06
C(F1(y1),F2(y2))-(F1(y1)F2(y2)
C(u1,u2)/u2-dC(u1,u2)/du2
0.04
0.02
0
0
0
0
0
1
1
0.2
0.2
0.4
0.6
0.8
0.4
0.5
0.6
0.8
10
10
10
−20
−20
−15
−15
−10
−10
−10
−10
−5
−5
5
5
0
0
0
Figure 5.3
Estimated kernel copula for DAX and SPX
Measure of association implied by the copula
Spearman’s Rho
Blomqvist’s Beta
Gini’s Gamma
0.5396
0.3737
0.4324

168
Copula Methods in Finance
(a)
(b)
(c)
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
u
C (u,u)
Trace C (u, u)
−2.5 −2 −1.5 −1 −0.5
0
0.5
1
1.5
2
2.5
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
a
FMIN(a)
Distribution of min
−2.5 −2 −1.5 −1 −0.5
0
0.5
1
1.5
2
2.5
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
a
FMAX(a)
Distribution of max
1
0.8
0.6
y2
C(F1(y1),F2(y2))
y1
y2
y1
u2
u1
Left Tail Dependence of Y1 in Y2
Positive Quadrant Dependence
Estimated Copula
0.4
0.2
0
4
0.06
0.04
0.02
C(F1(y1),F2(y2))-(F1(y1)F2(y2)
C(u1,u2)/u2-dC(u1,u2)/du2
0
−0.0
0
2
0
0
1
1
0.2
−0.5
−1
−2
−1.5
0
0.5
0.4
0.5
0.6
0.8
4
10
10
−4
−4
−15
−15
−10
−10
−2
−2
−5
−5
5
5
0
0
2
0
Figure 5.4
Estimated kernel copula for SPX and 10-year US bonds
Measure of association implied by the copula
Spearman’s Rho
Blomqvist’s Beta
Gini’s Gamma
0.1595
0.1711
0.1517

Estimation and Calibration from Market Data
169
(a)
(b)
(c)
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
u
C (u,u)
Trace C (u, u)
−2
−1.5
−1
−0.5
0
0.5
1
1.5
2
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
a
FMIN(a)
Distribution of min
−2
−1.5
−1
−0.5
0
0.5
1
1.5
2
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
a
FMAX(a)
Distribution of max
1
0.8
0.6
y2
C(F1(y1),F2(y2))
y1
y2
y1
u2
u1
Left Tail Dependence of Y1 in Y2
Positive Quadrant Dependence
Estimated Copula
0.4
0.2
0
4
0.1
0.08
0.06
0.04
0.02
C(F1(y1),F2(y2))-(F1(y1)F2(y2)
C(u1,u2)/u2-dC(u1,u2)/du2
0
0
2
0
0
1
1
0.2
−0.5
−1
−2
−1.5
0
0.5
0.4
0.5
0.6
0.8
4
4
4
−4
−4
−4
−4
−2
−2
−2
−2
2
2
0
0
2
0
Figure 5.5
Estimated kernel copula for 10-year German bonds and 10-year US bonds
Measure of association implied by the copula
Spearman’s Rho
Blomqvist’s Beta
Gini’s Gamma
0.4304
0.3402
0.3692

170
Copula Methods in Finance
(a)
(b)
(c)
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
u
C (u,u)
Trace C (u, u)
−4
−3
−2
−1
0
1
2
3
4
5
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
a
FMIN(a)
Distribution of min
−4
−3
−2
−1
0
1
2
3
4
5
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
a
FMAX(a)
Distribution of max
1
0.8
0.6
y2
C(F1(y1),F2(y2))
y1
y2
y1
u2
u1
Left Tail Dependence of Y1 in Y2
Positive Quadrant Dependence
Estimated Copula
0.4
0.2
0
10
0.05
0.04
0.03
0.02
0.01
C(F1(y1),F2(y2))-(F1(y1)F2(y2)
C(u1,u2)/u2-dC(u1,u2)/du2
0
−0.01
0
0
0
1
1
0.2
−0.2
−0.4
0.2
0
0.4
0.4
0.5
0.6
0.8
10
10
10
−20 −10
−10
−20
−10
−10
−5
−5
5
5
0
0
0
Figure 5.6
Estimated kernel copula for DEM/USD and SPX
Measure of association implied by the copula
Spearman’s Rho
Blomqvist’s Beta
Gini’s Gamma
0.1692
0.1470
0.1606

Estimation and Calibration from Market Data
171
spx10
usbond10
ger10
spx10
usbond10
ger10
u1
u2
u3
C(u1,u2,u3)
u1
u2
u3
C(u1,u2,u3)
0.01
0.01
0.01
0.0000
0.51
0.51
0.51
0.1619
0.02
0.02
0.02
0.0000
0.52
0.52
0.52
0.1715
0.03
0.03
0.03
0.0000
0.53
0.53
0.53
0.1834
0.04
0.04
0.04
0.0001
0.54
0.54
0.54
0.1895
0.05
0.05
0.05
0.0002
0.55
0.55
0.55
0.1984
0.06
0.06
0.06
0.0004
0.56
0.56
0.56
0.2067
0.07
0.07
0.07
0.0006
0.57
0.57
0.57
0.2181
0.08
0.08
0.08
0.0009
0.58
0.58
0.58
0.2284
0.09
0.09
0.09
0.0016
0.59
0.59
0.59
0.2358
0.10
0.10
0.10
0.0019
0.60
0.60
0.60
0.2477
0.11
0.11
0.11
0.0022
0.61
0.61
0.61
0.2578
0.12
0.12
0.12
0.0028
0.62
0.62
0.62
0.2681
0.13
0.13
0.13
0.0039
0.63
0.63
0.63
0.2785
0.14
0.14
0.14
0.0044
0.64
0.64
0.64
0.2933
0.15
0.15
0.15
0.0056
0.65
0.65
0.65
0.3039
0.16
0.16
0.16
0.0067
0.66
0.66
0.66
0.3186
0.17
0.17
0.17
0.0084
0.67
0.67
0.67
0.3287
0.18
0.18
0.18
0.0099
0.68
0.68
0.68
0.3469
0.19
0.19
0.19
0.0112
0.69
0.69
0.69
0.3553
0.20
0.20
0.20
0.0142
0.70
0.70
0.70
0.3699
0.21
0.21
0.21
0.0146
0.71
0.71
0.71
0.3884
0.22
0.22
0.22
0.0178
0.72
0.72
0.72
0.3970
0.23
0.23
0.23
0.0189
0.73
0.73
0.73
0.4098
0.24
0.24
0.24
0.0218
0.74
0.74
0.74
0.4283
0.25
0.25
0.25
0.0239
0.75
0.75
0.75
0.4486
0.26
0.26
0.26
0.0267
0.76
0.76
0.76
0.4575
0.27
0.27
0.27
0.0299
0.77
0.77
0.77
0.4818
0.28
0.28
0.28
0.0339
0.78
0.78
0.78
0.4979
0.29
0.29
0.29
0.0368
0.79
0.79
0.79
0.5134
0.30
0.30
0.30
0.0406
0.80
0.80
0.80
0.5284
0.31
0.31
0.31
0.0440
0.81
0.81
0.81
0.5523
0.32
0.32
0.32
0.0473
0.82
0.82
0.82
0.5774
0.33
0.33
0.33
0.0516
0.83
0.83
0.83
0.5908
0.34
0.34
0.34
0.0568
0.84
0.84
0.84
0.6032
0.35
0.35
0.35
0.0614
0.85
0.85
0.85
0.6228
0.36
0.36
0.36
0.0657
0.86
0.86
0.86
0.6569
0.37
0.37
0.37
0.0728
0.87
0.87
0.87
0.6740
0.38
0.38
0.38
0.0766
0.88
0.88
0.88
0.6938
0.39
0.39
0.39
0.0797
0.89
0.89
0.89
0.7167
0.40
0.40
0.40
0.0878
0.90
0.90
0.90
0.7425
0.41
0.41
0.41
0.0921
0.91
0.91
0.91
0.7680
0.42
0.42
0.42
0.1002
0.92
0.92
0.92
0.7919
0.43
0.43
0.43
0.1036
0.93
0.93
0.93
0.8180
0.44
0.44
0.44
0.1125
0.94
0.94
0.94
0.8505
0.45
0.45
0.45
0.1190
0.95
0.95
0.95
0.8669
0.46
0.46
0.46
0.1236
0.96
0.96
0.96
0.9064
0.47
0.47
0.47
0.1309
0.97
0.97
0.97
0.9226
0.48
0.48
0.48
0.1456
0.98
0.98
0.98
0.9462
0.49
0.49
0.49
0.1464
0.99
0.99
0.99
0.9872
0.50
0.50
0.50
0.1538
Figure 5.7
Trace of the non-parametric copula for a trivariate case
Hence, the c.d.f. for the portfolio return Z is given by:
H(z) = Pr (Z ⩽z) = Pr(βX1 + (1 −β) X2 ⩽z)
 +∞
−∞

1
β z−1−β
β x2
−∞
c(F1(x1), F2(x2))f1 (x1) dx1

f2(x2) dx2
which is equivalent to the expression in section 2.5 of Chapter 2.
As recalled there, the VaR for the portfolio, at a confidence level θ ∈(0, 1) and for a
given weight β ∈(0, 1), is the solution z∗of the equation H(z∗) = θ. This result may be
extended straight to an n-variate case with the constraint that the n weights sum to 1.
We calculate the VaR both using the standard assumption that returns are distributed
jointly as a normal and returns are jointly distributed as implied by our non-parametrically
estimated copula.
We first estimate the copula using 250 days and with the same sample we estimate the
VarCov matrix needed to calculate the normal VaR. From the copula we calculate the VaR.
We then repeat the operation rolling the sample.

172
Copula Methods in Finance
0
100
200
300
400
500
600
700
800
900
1000
−2
−1.5
−1
−0.5
0
0.5
1
1.5
2
2.5
Copula
Normal
Ptf return
Figure 5.8
VaR with copulas (VaR at 99% for portfolio composed of 30% S&P 500, 70% US
bond 10y)
We decided to use daily data because, to give to this exercise reasonable reliability, we
need to perform the calculations on many samples. Using daily data we have a total of 1000
subsamples from August 18, 1997 to June 15, 2001.
Some graphical results are displayed in Figures 5.8, 5.9 and 5.10. It can be seen from
these diagrams that the VaR calculated from the copula is able to capture the tail fatness
and other non-normality features found in the data and, as expected, is overperformed with
respect to the standard normal VaR.
The results we found point in the direction that, as we add in the portfolio more of the
leptokurtotic asset and as we require a greater confidence level, the VaR based on the copula
function performs better than the one calculated under normality.
5.6
CALIBRATION METHOD BY USING SAMPLE
DEPENDENCE MEASURES
We introduce an idea pointed out by Genest and MacKay (1986) to calibrate an Archimedean
copula, i.e. how to estimate the parameter α once a particular Archimedean copula has been
chosen. This method is very simple compared with the previous ones, but it is limited to a
bivariate setting because it makes inference on the dependence structure of the multivariate
model from a chosen dependence coefficient.
First, sum up all sample information in the consistent estimator of Kendall’s τ obtained
from the two series S1t and S2t with t = 1, . . . , T as follows:
ˆτ =
2
T (T −1)

i<j
sgn

S1i −S1j
 
S2i −S2j

(5.43)
where the sign function is defined as in the list of symbols.

Estimation and Calibration from Market Data
173
0
100
200
300
400
500
600
700
800
900
1000
−4
−3
−2
−1
0
1
2
3
Copula
Normal
Ptf return
Figure 5.9
VaR with copulas (VaR at 99% for portfolio composed of 50% S&P 500, 50% US
bond 10y)
0
100
200
300
400
500
600
700
800
900
1000
−6
−5
−4
−3
−2
−1
0
1
2
3
4
Copula
Normal
Ptf return
Figure 5.10
VaR with copulas (VaR at 99% for portfolio composed of 80% S&P 500, 20% US
bond 10y)


## Simulation of Market Scenarios

174
Copula Methods in Finance
Since we are considering a one-parameter family of Archimedean copulas, we use the
relationship between α and τ in order to infer an estimate for the copula parameter α.
We also can check for different Archimedean copulas how each of them fits the data by
comparison with the empirical copula. This fitting test is performed through an (unobserved)
auxiliary variable, W = F(S1, S2), where F is the (unknown) joint distribution function of
the two variables S1 and S2. We use the following algorithm based on Genest and Rivest
(1993) (also described by Frees & Valdez, 1998):
• Denote by K(w) the distribution of W, K(w) : [0, 1] →[0, 1] and that for Archimedean
copulas whose generator is indicated by ψα
K(w) = w −
1
(∂ln ψα(w))/∂w
(5.44)
hence, for each one-parameter Archimedean copula, construct an estimate of K substi-
tuting the estimate, previously obtained, for α.
• Define
Zi = Card

S1j, S2j

: S1j < S1i, S2j < S2i
 
T −1
(5.45)
and construct an empirical version of K(w) as:
KT (w) =
T
i=1 1(w −Zi)
T
(5.46)
where 1 is the commonly known indicator function.
• Finally, compare KT and Kˆα (w) graphically and via mean-square error.3
This method is simple to use and very easy to perform. Its main disadvantage is that it
sums up all data information in the empirical, though consistent, estimator of the chosen
association measure. Obviously, besides neglecting all other potential sources of statistical
information that come from the data, it is strongly dependent on the particular associative
measure chosen.
This method may be considered an estimation criteria based on sample dependence mea-
sures.
5.7
APPLICATION
Now we want to compare the empirical estimates of some dependence measures for the
five series considered in our dataset. The readers should refer to Gibbons (1992) Chap. 12
for a formal definition and a more extensive explanation of measures of association for
bivariate samples (sample estimates, large sample distribution, important relation between
these measures, etc.); and to Chap. 13 for an extension in multiple classification.
3 This method has been extended to the n-variate case for Archimedean copulas by Barbe et al. (1996), Frees and
Valdez (1998) as reported by Durrleman, Nikeghbali and Roncalli (2000a).

Estimation and Calibration from Market Data
175
Table 5.6
Sample Spearman’s rho
DAX 30
S&P 500
GER10y
USA10y
DEM/USD
DAX 30
−
S&P 500
0.67
−
GER10y
0.20
0.18
−
USA10y
0.04
0.13
0.49
−
DEM/USD
0.31
0.19
0.06
−0.22
−
Table 5.7
Spearman’s rho calculated from Frank copula with NC Student t margins
DAX 30
S&P 500
GER10y
USA10y
DEM/USD
DAX 30
−
S&P 500
0.60
−
GER10y
0.09
0.07
−
USA10y
−0.08
0.12
0.46
−
DEM/USD
0.24
0.11
−0.04
−0.08
−
Using the same data as in the previous examples (sections 3.1 and 5.2.1), we compute
the sample Spearman’s rho, and obtain the values given in Table 5.6. We also report in
Table 5.7 the same index based on the estimated α from the Frank copula function. More
precisely the relation that we use is
ρS =
12
α D2(−α) −D1(−α)

−1
(5.47)
where D denotes the Debye function.4 Rho depends, via a one-to-one relationship, on the
Frank copula parameter α that we estimated via maximum likelihood. The copula is fitted
for each pair of assets and the rho coefficient is then calculated. Most of the time this
measure is quite close to the sample counterparty, but there are two notable exceptions: the
correlation between the DAX index and the 10-year US bond is estimated to be negative
when the copula is used, while the sample counterparty is (slightly) positive. The same can
be said of the correlation between the 10-year German bond and the exchange rate.
Like above, we report in Table 5.8 some results obtained for Kendall’s tau. Also, Kendall’s
tau (Table 5.9) is linked to α from the Frank copula, as recalled in Chapter 3:
τ = 4
α {1 −D1(−α)} −1
(5.48)
In this case the estimated τ coefficient is closer to its sample counterparty than previously
happened for Spearman’s rho.
For the sake of completeness we also report the Pearson’s correlation matrix in Table 5.10.
The readers may note that this “correlation matrix” is very close to that estimated via the
CML method, assuming a Gaussian copula.
4 The Debye functions are defined in Chapter 3.

176
Copula Methods in Finance
Table 5.8
Sample Kendall’s tau
DAX 30
S&P 500
GER10y
USA10y
DEM/USD
DAX 30
−
S&P 500
0.44
−
GER10y
0.13
0.12
−
USA10y
0.03
0.14
0.35
−
DEM/$
0.22
0.13
0.05
−0.11
−
Table 5.9
Kendall’s tau implied by α from Frank copula
DAX 30
S&P 500
GER10y
USA10y
DEM/USD
DAX 30
−
S&P 500
0.47
−
GER10y
0.13
0.12
−
USA10y
0.03
0.15
0.38
−
DEM/USD
0.23
0.14
0.05
−0.13
−
Table 5.10
Pearson correlation
DAX 30
S&P 500
GER10y
USA10y
DEM/USD
DAX 30
−
S&P 500
0.67
−
GER10y
0.18
0.13
−
USA10y
−0.02
0.13
0.50
−
DEM/USD
0.30
0.14
0.06
−0.21
−
5.8
EVALUATION CRITERIA FOR COPULAS
Modeling a copula function means modeling both marginals and the joint distribution.
Hence, measures of goodness of fit are important for evaluating the fit of a proposed copula
and for testing the specification of the marginal distributions. As discussed above, the copula
evaluation is a special case of the more general issue of evaluating multivariate density
models. For such a problem, some methods have been proposed in the literature, and no
single method has emerged as best (see Diebold et al., 1998, 1999).
This evaluation issue may be split into two distinct problems. First, one should evaluate
the goodness of fit for each margin and then the overall goodness of fit given by the copula.
The former problem may be easily faced by using the probability integral transform, thus,
it has been shown that for the time series framework the sequence of probability integral
transforms of the data will be i.i.d. Uniform (0, 1) if the sequence of densities is correct.
It is worth noting that instead of testing, for each margin, whether its probability integral
transform series {ut}T
t=1 be i.i.d. Uniform (0, 1), it is equivalently possible to test that the
transformed series

zt = −1(ut)
 T
t=1 be i.i.d. Normal (0, 1). The latter procedure is the
most used in practice due to the large number of tests of normality available. Diebold et al.

Estimation and Calibration from Market Data
177
(1998, 1999) propose some tests to check the independence of the transformed series by
using the Kolmogorov–Smirnov test (see Shao, 1999, for the theory underlying this test)
and other ad hoc tests by using their first moments. Diebold, Hahn and Tay (1999) extend
the results of Diebold, Gunther and Tay (1998) to the evaluation of bivariate density models
by testing the conditional c.d.f.s of X and Y.
As pointed out by the same authors, the issue to evaluate the joint c.d.f., such as the
copula fitting, is much more difficult.
Patton (2001) proposes, for a bivariate case, an extension of the “Hit” regression of
Christoffersen (1998) and Engle and Manganelli (1999) for evaluating interval forecasts,
such as VaR forecasts (for an empirical application and a discussion about such statisti-
cal tests refer to Meneguzzo & Vecchiato, 2000). Briefly, the author builds up a test by
decomposing the density model into a set of region models (interval models in the basic
univariate case), each of which should be correctly specified under the null hypothesis that
the entire multivariate density is correctly specified. The evaluation problem is so recon-
ducted to test whether the model is adequately specified in each of the regions individually
via tests of each binomial hypothesis (i.e. each hit or indicator function is a Bernoulli r.v.).
Patton (2001) uses logistic regression, which yields more efficient parameter estimates, to
test equivalent null hypothesis i.i.d. Bernoulli or Multinomial r.v.s. Following his method
it is possible to build up a family of tests to evaluate if the model is correctly specified in
a set of regions where it is defined.
5.9
CONDITIONAL COPULA
In econometric theory much attention has been reserved to conditional distribution modeling,
i.e. conditional to all past information. This is mainly due to forecasting and fitting purposes
(see Davidson & MacKinnon, 1993, for a further explanation).
For the bivariate case, Patton (2001) extends the standard definition of copula to the
conditional case. Thus, he introduces the copula theory to model the time-varying conditional
dependence. His interest consists in taking into account the well-known heteroskedastic
pattern, widely reported in the financial literature, for the volatility of any financial return
time series (see Engle, 1996, for an excellent survey). Further, there are many situations
where the entire conditional joint density is required, such as the pricing of financial options
with multiple underlying assets (see Rosemberg, 2000), or in the calculation of portfolio
VaR, as previously discussed (also refer to Hull & White, 1998).
The extension to the conditional copula consists in expressing the Sklar’s theorem for
conditional c.d.f., i.e. conditional to a sigma algebra ℑgenerated by all past information.
For example, in a time series context
ℑt = σ {x1t−1, x2t−1, . . . , xnt−1, x1t−2, x2t−2, . . . , xnt−2, . . . .}
for t = 1, . . . , T
(5.49)
represents the past information up to time t. Hence, Sklar’s theorem may be extended as
follows:
Ft(x1t, x2t, . . . , xnt | ℑt) = Ct(F1t(x1t | ℑt), F2t(x2t | ℑt), . . . , Fnt(xnt | ℑt) | ℑt)
(5.50)
where Ct has to be a copula function at all times t.
It is worth noting that the joint distribution of (X1t, X2t, . . . , Xnt) may differ from the
joint distribution of (X1t−1, X2t−1, . . . , Xnt−1), and so on. Thus a sample data matrix ℵ=

178
Copula Methods in Finance
{x1t, x2t, . . . , xnt}T
t=1 may not represent T observations of the same joint distribution, but
T observations from T different joint distributions. Besides that, note that the conditioning
set for each marginal and for the conditional copula is the same; hence, each transformed
variable must be independent of the information in the conditioning set of its marginal
distribution. This condition allows us to build statistical tests.
Obviously, without assuming some functional structure it is impossible to estimate the
form of each joint distribution. So, for example, one is forced to assume that the distributions
remain constant over time, while some of their parameters vary according to some finite
difference equation.
Patton (2001), in modeling the marginal distributions, assumes that the conditional means
evolve according to an autoregressive process, and that the conditional variances evolve
according to a GARCH(1, 1) process.
Similarly the evolution of Ct has to be assumed. Its possible paths may be the degenerate
case (i.e. it does not vary at all), the time-varying parameters case (i.e. the functional form of
the conditional copula is fixed, but its parameters evolve through time), or the complete time-
varying structure (i.e. time variation involves changes in both the form of the conditional
copula and its parameters). Nelsen (1999) shows that any convex linear combination of
copulas is also a copula, and so a time-varying functional form for the conditional copula
could be set to a convex sum (even with time-varying weights) of various types of copulas
(even time-varying parameter copulas, as previously defined).
5.9.1
Application to an equity portfolio
We consider two sets of equity daily (last) price data (General Motors and IBM). In spec-
ifying the model for the bivariate density of the General Motors and the IBM stocks it is
necessary to specify three models: two models for the marginal distributions of each stock
and one model for the conditional copula.
The model that we choose for the marginal distributions is a GARCH(1, 1) with normal
innovations, because it is the most frequently used model in the literature of applied financial
econometrics (refer to Engle, 1996, for a survey) and is defined as:
Xt = εt
(5.51)
hx
t = ωx + βxhx
t−1 + αxε2
t−1
(5.52)
εt
!
hx
t
⇝N(0, 1)
(5.53)
where Xt represents the log-difference of the stock price.
In our particular case it happens that we only need univariate models for the two marginal
distributions due to the fact that no lags of the other variables appear in the regression. This
will not always be so.
In Tables 5.11 and 5.12 we present the results we have obtained using the GARCH(1, 1)
model.
After having estimated the marginal distributions it is necessary to define the copula
function in order to obtain the joint distribution of the two stocks. In this example we
consider the Gaussian copula. We also assume that the correlation parameter of the copula,

Estimation and Calibration from Market Data
179
Table 5.11
Results for the marginal distributions
IBM stock
ωx
βx
αx
0.0000
0.9302
0.0613
Standard error
0.0000
0.0000
0.0000
Robust standard error∗
0.0000
0.0001
0.0001
∗Quasi-likelihood standard errors which are robust to some forms of
mis-specification (refer to White, 1984).
Table 5.12
GM Stock
ωx
βx
αx
0.0000
0.9134
0.0611
std. error
0.0000
0.0000
0.0000
robust std. error
0.0000
0.0001
0.0001
Rho
0
0.2
0.4
0.6
0.8
1
1.2
Figure 5.11
Time-varying conditional correlation in the normal copula
Results for the Gaussian copula
ωρ
βρ
αρ
0.010731
−2.090770
−0.043261
ρ, varies according to the following evolution equation:
ρt = 

ωρ + βρρt−1 + αρ
1
p
p

j=1
−1(ut−j)−1(vt−j)


(5.54)
where (x) is the modified logistic (also known as hyperbolic tangent) function 1−e−x
1+e−x
necessary to keep ρt belonging to the interval (−1, 1).

180
Copula Methods in Finance
The regression (5.53) includes the term ρt−1 in order to capture the persistence in the
dependence parameter, and the average sum
1
p
p

j=1
−1(ut−j)−1(vt−j)
in order to capture any variation in dependence.
We choose to allow a time-varying correlation coefficient, instead of a constant one, for
a more general setting.
In this empirical application, according to the data we are analyzing, we set p equal to 1
in the equation (5.54) and we report the results for the Gaussian copula below Figure 5.11
and in Figure 5.11 for the time varying correlation.
All estimates are statistically significant.

6
Simulation of Market Scenarios
6.1
MONTE CARLO APPLICATION WITH COPULAS
Simulation is a widely used tool for generating draws from a lot of stochastic models. In
the following we describe some useful techniques in order to generate random scenarios
from the copula set up. We start with the elliptical copulas – the Gaussian and Student t
copulas – where the simulations are obtained easily even if their copula is not in closed form.
As for other copulas, like the Archimedean ones, we describe the conditional method. This
method may be applied for every chosen copula. Besides that, for some Archimedean copu-
las, a simple method proposed by Marshall and Olkin (1998) allows us to get simulations
easily. We offer some illustrative examples.
Generally, once a copula has been decided upon, we may draw multivariate random
samples.
6.2
SIMULATION METHODS FOR ELLIPTICAL COPULAS
Our attention is dedicated to the Gaussian and T copula because they are the most widely
known and applied copulas to Empirical Finance. As we have seen previously, the form of
their copula is not closed and easy to write down, but the simulation draws are very easy
to obtain.
We provide the following algorithm in order to generate random variates from the Gaus-
sian n-copula CN
R :
• Find the Cholesky decomposition A of R
• Simulate n independent random variates z = (z1, z2, . . . , zn)′ from N(0, 1)
• Set x = Az
• Set ui = (xi) with i = 1, 2, . . . , n and where  denotes the univariate standard normal
distribution function
• (u1, . . . , un)′ = (F1(t1), . . . , Fn(tn))′ where Fi denotes the ith margin
The Student T copula is also easy to simulate. We provide the following algorithm in
order to generate random variates from the n-copula TR,υ:
• Find the Cholesky decomposition A of R
• Simulate n i.i.d. z = (z1, z2, . . . , zn)′ from N(0, 1)
• Simulate a random variate s from χ2
υ independent of z
• Set y = Az
• Set x = √(υ/s)y
• Set ui = Tυ(xi) with i = 1, 2, . . . , n and where Tυ denotes the univariate Student t dis-
tribution function
• (u1, . . . , un)′ = (F1(t1), . . . , Fn(tn))′ where Fi denotes the ith margin

182
Copula Methods in Finance
6.3
CONDITIONAL SAMPLING
A general method to simulate draws from a chosen copula is formulated by using a con-
ditional approach (conditional sampling). Just to explain this concept in a simple way, let
us assume a bivariate copula in which all of its parameters are known (fixed or estimated
with some statistical methods). The task is to generate pairs (u, v) of observations of [0, 1]
uniformly distributed r.v.s U and V whose joint distribution function is C. To reach this
goal we will use the conditional distribution
cu(v) = Pr(V ⩽v|U = u)
(6.1)
for the r.v. V at a given value u of U.
Basically, we know that
cu(v) = Pr(F2 ⩽v|F1 = u) = lim
u→0
C(u + u, v) −C (u, v)
u
= ∂C
∂u = Cu(v)
(6.2)
where Cu(v) is the partial derivative of the copula. We know that cu(v) is a non-decreasing
function and exists for almost all v ∈[0, 1].
With this result at hand, we generate the desired pair (u, v) in the following way:
• Generate two independent uniform r.v.s (u, w) ∈[0, 1]. u is the first draw we are looking
for.
• Compute the (quasi-)inverse function of cu(v). This will depend on the parameters of the
copula and on u, which can be seen, in this context, as an additional parameter of cu(v).
Set v = c−1
u (w) to obtain the second desired draw.1
The general procedure in a multivariate setting is as follows:
• Define Ci = C(F1, F2, . . . , Fi, 1, 1, . . . , 1) for i = 2, 3, . . . , n.
• Draw F1 from the uniform distribution U(0, 1).
• Next, draw F2 from C2(F2|F1).
• More generally, draw Fn from Cn(Fn|F1, . . . , Fn−1).
Putting it differently, let us consider the general setting for an n-copula C = C(u1, u2, . . . , un)
and let Ck(u1, u2, . . . , uk, 1, . . . , 1) for k = 2, . . . , n −1 denote the k-dimensional margins
of C, with C1(u1) = u1 and Cn(u1, u2, . . . , un) = C(u1, u2, . . . , un).
Since U1, U2, . . . , Un have joint distribution function C, then the conditional distribution
of Uk, given the values of U1, . . . , Uk−1, is given by
Ck(uk|u1, . . . , uk−1) = Pr(Uk ⩽uk|U1 = u1, . . . , Uk−1 = uk−1)
=
[∂k−1Ck(u1, . . . , uk)]/[∂u1 . . . ∂uk−1]
[∂k−1Ck−1(u1, . . . , uk−1)]/[∂u1 . . . ∂uk−1]
(6.3)
with k = 2, . . . , n. Obviously we assume that both the numerator and the denominator exist
and that the denominator is not zero. Hence the algorithm may be rewritten as:
1 Nelsen (1999, p. 35) calls this function the quasi-inverse of cu.

Simulation of Market Scenarios
183
• Simulate a random variate u1 from U(0, 1)
• Simulate a random variate u2 from C2(·|u1)
• . . .
• Simulate a random variate un from Cn(·|u1, . . . , un−1)
In order to simulate a value uk from Ck(·|u1, . . . , uk−1) one has to draw v from U(0, 1)
from which uk = C−1
k (v|u1, . . . , uk−1) can be obtained through the equation v =
Ck(uk|u1, . . . , uk−1) by numerical rootfinding.2
The conditional approach is very elegant but it may not be possible to calculate the
inverse function analytically. In this case one has to use a numerical algorithm to determine
the desired draw. Obviously, this procedure may be computationally intensive.
In the case of Archimedean copulas this method may be rewritten as the following theorem
states.
Theorem 6.1
Let C (u1, u2, . . . , un) = ϕ−1 (ϕ (u1) + ϕ (u2) + · · · + ϕ (un)) be an Archi-
medean n-variate copula with generator ϕ (·), then for k = 2, . . . , n
Ck(uk|u1, . . . , uk−1) =
ϕ−1(k−1) (ϕ (u1) + ϕ (u2) + · · · + ϕ (uk))
ϕ−1(k−1) (ϕ (u1) + ϕ (u2) + · · · + ϕ (uk−1))
(6.4)
Proof :
Since by definition ϕ(1) = 0 then, for k = 2, . . . , n −1,
Ck(u1, . . . , uk) = C(u1, . . . , uk, 1, . . . , 1) = ϕ−1 (ϕ (u1) + ϕ (u2) + · · · + ϕ (uk))
(6.5)
Besides C1(u1) = ϕ−1(ϕ(u1)) = u1 and
Cn(u1, . . . , un) = C (u1, u2, . . . , un) = ϕ−1 (ϕ (u1) + ϕ (u2) + · · · + ϕ (un))
(6.6)
Moreover
Ck(uk|u1, . . . , uk−1) =
[∂k−1Ck(u1, . . . , uk)]/[∂u1 . . . ∂uk−1]
[∂k−1Ck−1(u1, . . . , uk−1)]/[∂u1 . . . ∂uk−1]
(6.7)
and by derivation we have
∂k−1Ck−1(u1, . . . , uk)
∂u1 . . . ∂uk−1
= ∂k−1 ϕ−1 (ϕ (u1) + ϕ (u2) + · · · + ϕ (uk−1))
∂u1 . . . ∂uk−1
= ϕ−1(k−1) (ϕ (u1) + ϕ (u2) + · · · + ϕ (uk−1)) ·
k−1

j=1
ϕ(1) 
uj

(6.8)
2 For a detailed description of simulation procedures, see Genest (1987), Genest and Rivest (1993), Lee (1993),
Frees and Valdez (1998), Marshall and Olkin (1988), and Embrechts, Lindskog and McNeil (2001).

184
Copula Methods in Finance
and
∂k−1Ck(u1, . . . , uk)
∂u1 . . . ∂uk−1
= ∂k−1ϕ−1 (ϕ (u1) + ϕ (u2) + · · · + ϕ (uk))
∂u1 . . . ∂uk−1
= ϕ−1(k−1) (ϕ (u1) + ϕ (u2) + · · · + ϕ (uk)) ·
k−1

j=1
ϕ(1) 
uj

(6.9)
hence we obtain the following result
Ck(uk|u1, . . . , uk−1) =
ϕ−1(k−1) (ck)
ϕ−1(k−1) (ck−1)
(6.10)
where ck = k
j=1 ϕ(uj) and with k = 2, . . . , n.
□
Now we would like to apply this important result to the most used Archimedean copulas.
We present, in full detail, the particular cases for the Frank copula and for the Clayton
copula, because they are the most frequently used and best known Archimedean copulas in
empirical applications.
6.3.1
Clayton n-copula
The generator is given by ϕ(u) = u−α −1, hence ϕ−1(t) = (t + 1)−1
α . The Clayton n-
copula, also known as Cook and Johnson’s (1981) family, is given by:
C(u1, u2, . . . , un) =
 n

i=1
u−α
i
−n + 1
−1
α
with α > 0
(6.11)
Let us compute the derivatives of the function ϕ−1(t). We have
ϕ−1(1)(t) = −1
α (t + 1)−1
α −1,
ϕ−1(2) = 1
α
α + 1
α
(t + 1)−1
α −2 , . . . ,
ϕ−1(k)(t) = (−1)k (α + 1) (α + 2) · · · · · (α + k −1)
αk
(t + 1)−1
α −k
(6.12)
Hence, by applying the previous theorem, the following algorithm generates a random
variate (u1, u2, . . . , un)′ from the Clayton copula:
• Simulate n independent random variables (v1, v2, . . . , vn)′ from U(0, 1)
• Set u1 = v1
• Set v2 = C2(u2|v1), hence
v2 = ϕ−1(1)(c2)
ϕ−1(1)(c1)
with c1 = ϕ(u1) = u−α
1
−1 and c2 = ϕ (u1) + ϕ (u2)
= u−α
1
+ u−α
2
−2

Simulation of Market Scenarios
185
so
v2 =

u−α
1
+ u−α
2
−1
u−α
1
	−1
α −1
Finally
u2 =

v−α
1

v
−
α
α+1
2
−1

+ 1
−1
α
(6.13)
• Set
v3 = C3(u3|u1, u2) = ϕ−1(2) (c3)
ϕ−1(2) (c2) =

u−α
1
+ u−α
2
+ u−α
3
−2
u−α
1
+ u−α
2
−1
	−1
α −2
and solve it in u3
• . . .
• Solve in un the equation
vn =

u−α
1
+ u−α
2
+ · · · + u−α
n
−n + 1
u−α
1
+ u−α
2
+ · · · + u−α
n−1 −n + 2
	−1
α −n+1
so we have:
un =

u−α
1
+ u−α
2
+ · · · + u−α
n−1 −n + 2

·

v
α
α(1−n)−1
n
−1

+ 1
−1
α
(6.14)
6.3.2
Gumbel n-copula
The generator is given by ϕ(u) = (−ln(u))α, hence ϕ−1(t) = exp(−t
1
α ). The Gumbel n-
copula is given by:
C(u1, u2, . . . , un) = exp


−
 n

i=1
(−ln ui)α
 1
α



with α > 1
(6.15)
Let w = t
1
α →t = wα, so we have
ϕ−1(w) = exp(−w)
and
∂w
∂t = 1
α t
1
α −1 = 1
α w1−α
Hence we have
ϕ−1(1) (t) = ∂ϕ−1
∂w
∂w
∂t = −e−w 1
α w1−α and
ϕ−1(2)(t) = ∂ϕ−1(1)
∂w
∂w
∂t = 1
α2 e−ww1−2α(w −1 + α)
and so on. Unfortunately this is not a recursive formula.

186
Copula Methods in Finance
The following algorithm generates a random variate (u1, u2, . . . , un)′ from the Gumbel
copula:
• Simulate n independent random variables (v1, v2, . . . , vn)′ from U(0, 1)
• Set u1 = v1
• Set v2 = C2(u2|v1), hence
v2 = ϕ−1(1)(c2)
ϕ−1(1)(c1)
with c1 = ϕ(u1) = (−ln(u1))α
and
c2 = ϕ (u1) + ϕ (u2) = (−ln(u1))α + (−ln(u2))α
This equation has to be solved with respect to u2.
• Set
v3 = C3(u3|u1, u2) = ϕ−1(2) (c3)
ϕ−1(2) (c2)
and solve it in u3
• . . .
6.3.3
Frank n-copula
The generator is given by ϕ(u) = ln

exp(−αu)−1
exp(−α)−1

, hence
ϕ−1(t) = −1
α ln

1 + et(e−α −1)

The Frank n-copula is given by:
C(u1, u2, . . . , un) = −1
α ln

1 +
n
i=1

e−αui −1


e−α −1
n−1

with α > 0 when n ⩾3
(6.16)
We will soon see why higher dimensions allow only positive dependence (α > 0).
As for derivatives of ϕ−1(t), we have ϕ−1(1) (t) = −1
α
et(e−α−1)
1+et(e−α−1).
Let w =
et(e−α−1)
1+et(e−α−1) so we have
∂w
∂t = −w(w −1)
and
ϕ−1(1) (t) = −1
α w
Hence,
ϕ−1(2) (t) = ∂
∂t

ϕ−1(1) (t)

= ∂
∂w

ϕ−1(1) ∂w
∂t = 1
α w(w −1)
analogously
ϕ−1(3) (t) = ∂
∂w

ϕ−1(2) ∂w
∂t = −1
α w(w −1)(2w −1)

Simulation of Market Scenarios
187
In general we obtain:
ϕ−1(1) (t) = −1
α g1(w)
where g1(w) = w
(6.17)
and
ϕ−1(k) (t) = (−1)k 1
α gk(w)
where gk(w) = w(w −1)g(1)
k−1(w)
(6.18)
with g(1)
k−1(w) = ∂gk−1
∂w
and k ⩾2.
In such a way one can proceed to higher order derivatives.3
Finally, we give the following algorithm in order to generate a random variate (u1, u2, . . . ,
un)′ from the Frank copula:
• Simulate n independent random variables (v1, v2, . . . , vn)′ from U(0, 1)
• Set u1 = v1
• Set v2 = C2(u2|v1) hence
v2 = ϕ−1(1)(c2)
ϕ−1(1)(c1)
with c1 = ϕ(u1) = ln

exp (−αu1) −1
exp (−α) −1

and
c2 = ϕ (u1) + ϕ (u2) = ln

(exp (−αu1) −1) (exp (−αu2) −1)
(exp (−α) −1)2

Hence
v2 = e−αu1
exp (−αu2) −1
exp (−α) −1 + (exp (−αu1) −1) (exp (−αu2) −1)
has to be solved with respect to u2. We obtain:
u2 = −1
α ln

1 +
v2

1 −e−α
v2

e−αu1 −1

−e−αu1

(6.19)
3 From these expressions it is also possible to see that the Kimberling theorem may be invoked for higher dimensions
if and only if α > 0 in order to have a generator completely monotone. This means that the generators suitable for
extension to arbitrary dimensions of Archimedean 2-copulas correspond to copulas that can model only positive
dependence. In fact the readers may note that gk is a polynomial of degree k with the leading term of positive
sign. For w < 0 (hence α > 0) the polynomials are positive for even k and negative for odd k. When α < 0, then
0 < w < 1, and it is easily verified that ϕ−1(3)(t) fails to be negative for all t.
Alternatively refer to Schweizer and Sklar (1983), Chap. 6, where it is proven that the inverse of a strict generator
of an Archimedean n-copula C is completely monotone, then C > , where  is the product (or independent)
n-copula.

188
Copula Methods in Finance
• Set
v3 = C3(u3|u1, u2) = ϕ−1(2) (c3)
ϕ−1(2) (c2)
with c2 = ln

(exp (−αu1) −1) (exp (−αu2) −1)
(exp (−α) −1)2

and
c3 = ln

(exp (−αu1) −1) (exp (−αu2) −1) (exp (−αu3) −1)
(exp (−α) −1)3

Hence,
v3 = (e−α −1)[(e−α −1) + (e−αu1 −1)(e−αu2 −1)]2
×
e−αu3 −1
[(e−α −1)2 + (e−αu1 −1)(e−αu2 −1)(e−αu3 −1)]2
(6.20)
We obtain a polynomial equation of order 2 in the variable x = e−αu3 −1 that has to be
solved with respect to u3
• And so on, obtaining each variate uk involves solving a polynomial equation of degree
k −1.
6.4
MARSHALL AND OLKIN’S METHOD
We present a simulation algorithm proposed by Marshall and Olkin (1988) for the compound
construction of copulas. This is a construction method of copulas involving the Laplace
transform and its inverse function. Recall that the Laplace transform of a positive random
variable γ is defined by:
τ(s) = Eγ (e−sγ ) =
 +∞
0
e−stdFγ (t)
(6.21)
where Fγ is the distribution function of γ . This is also the moment generating function
evaluated at −s; thus, knowledge of τ(s) determines the distribution. Laplace transforms
have well-defined inverses. We saw that the inverse function τ −1 serves as the generator
for an Archimedean copula.
Marshall and Olkin’s (1988) method for constructing copulas may be described as follows.
Suppose that Xi is a r.v. whose conditional, given a positive latent variable γi, distribu-
tion function is specified by Hi(x|γi) = Hi(x)γi, where Hi(.) is some baseline distribution
function, for i = 1, 2, . . . , n.
Marshall and Olkin (1988) considered multivariate distribution functions of the form:
F(x1, x2, . . . , xn) = E

K(H1(x)γ1, H2(x)γ2, . . . , Hn(x)γn)

(6.22)
where K is a c.d.f. with uniform marginals, and the expectation is taken over γ1, γ2, . . . , γn.

Simulation of Market Scenarios
189
As a special case, we consider all latent variables equal to one another so that γ1 = γ2 =
· · · = γn = γ and use c.d.f.s corresponding to independent marginals. Marshall and Olkin
(1988) show that:
F(x1, x2, . . . , xn) = E(H1(x)γ1 · H2(x)γ2 · · · · · Hn(x)γn)
= τ(τ −1(F1(x1)) + τ −1(F2(x2)) + · · · + τ −1(Fn(xn)))
(6.23)
where Fi is the ith marginal c.d.f. of the joint c.d.f. F, and τ(.) is the Laplace transform
of γ .
Generating outcomes from a compound copula
To generate X1, X2, . . . , Xn having a distribution (6.23), Frees and Valdez (1998) propose
the following algorithm:
• Generate a (latent) r.v. γ having Laplace transform τ
• Independently of the previous step, generate U1, U2, . . . , Un independent Uniform (0, 1)
r.v.s
• For k = 1, 2, . . . , n, calculate Xk = F −1
k
(U∗
k ) where
U∗
k = τ

−1
γ ln Uk

(6.24)
This algorithm is straightforward for most copulas of interest that are generated by the
compounding method. It can easily be implemented for high dimension. The only disadvan-
tage is that it is necessary to simulate an additional r.v., γ . Needless to say, this additional
variable is not always easy to simulate.
For example, if we recall that a generator for a strict Archimedean copula is the Laplace
transform of some positive random variable, we may see that for the Clayton copula γ is a
Gamma(1, 1/α) r.v., that is very easy to simulate; for the Gumbel copula γ is a (1/α)-stable
r.v.; and for the Frank copula γ is a logarithmic series r.v. defined on all natural numbers
(see Marshall & Olkin, 1988). In the last case the simulation with this technique is not easy,
and the conditional sampling should be preferred.
We report on how to obtain draws by using this method for the Clayton and the Gumbel
copula, alternatively, to the conditional sampling technique previously discussed.
Clayton case
• Generate a r.v. γ Gamma(1, 1/α) (hence, γ has Laplace transform τ(s) = (1 + s)−1
α )
• Independently of the previous step, generate U1, U2, . . . , Un independent Uniform (0, 1)
r.v.s
• For k = 1, 2, . . . , n calculate Xk = F −1
k
(U∗
k ) where
U∗
k = τ

−1
γ ln Uk


190
Copula Methods in Finance
Gumbel case
• Generate a r.v. γ Stable(1, 0, 0) with parameter 1/α (hence, γ has Laplace transform
τ(s) = exp{−s
1
α })4;
• Independently of the previous step, generate U1, U2, . . . , Un independent Uniform (0, 1)
r.v.s
• For k = 1, 2, . . . , n calculate Xk = F −1
k
(U∗
k ) where
U∗
k = τ

−1
γ ln Uk

A common procedure to obtain a draw from a Stable(1, 0, 0) with parameter β r.v. is based
on the following result (Samorodnitsky & Taqqu, 1995, p. 42):
• Let υ be uniform on

−π
2 , π
2

and let ξ be exponential with mean 1 independently drawn.
Then
κ = sin (βυ)
(cos υ)
1
β
·
cos ((1 −β) υ)
ξ
 1−β
β
(6.25)
is Stable(1, 0, 0) with parameter β.
In Figure 6.1 we present an example of 10 000 simulated draws, following the above
algorithms, from a Gumbel copula with α = 2. As can be seen, there is evidence of upper
tail dependence.
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
0
0.2
0.4
0.6
0.8
1
0
0.2
0.4
0.6
0.8
1
u1
u2
u3
Gumbel Copula alpha = 2
Figure 6.1
Gumbel copula with α = 2
4 For a detailed description of stable r.v.s and their properties we refer readers to the excellent book of Samorod-
nitsky and Taqqu (1995).

Simulation of Market Scenarios
191
6.5
EXAMPLES OF SIMULATIONS
In this section we apply the previous algorithms to simulate some trivariate copulas. In
Figure 6.2 we show the simulated Student t copula with 4 d.o.f. and correlation matrix given
by daily equity series. We used daily returns series for ABN Amro, Bayer AG, Renault SA
(January 2, 2001–July 30, 2002) having estimated their robust positive definite correlation
matrix (by means of the Spearman’s rho ρS), a univariate t-GARCH(1, 1) process for each
series, and the T copula d.o.f. is found statistically significant around 4.
Using the conditional sampling technique, we simulate the trivariate Clayton and Frank
copula with different values for the α parameter for the same data set. This parameter was
estimated via the IFM technique, equal respectively to 0.53 for the Clayton copula and 1.61
for the Frank copula.
We remark that the α parameter in the Archimedean copulas is the only driver of
the dependence. Indeed, we show in Figures 6.3–6.8 how different values for α induce
stronger dependence. It can be seen from these figures that, in the Clayton copula, the
lower tail dependence is much stronger than in the Frank copula, where there is no tail
dependence.
0
0.2
0.4
0.6
0.8
1
0
0.5
1
0
0.2
0.4
0.6
0.8
1
ABN Amro
Bayer
Renault
Student Copula simulated u1, u2, u3 with d.f. = 4
Figure 6.2
Scatter plot Student t copula with 4 d.o.f. for ABN Amro, Bayer AG, Renault SA

192
Copula Methods in Finance
0
0.2
0.4
0.6
0.8
1
0
0.5
1
0
0.2
0.4
0.6
0.8
1
ABN Amro
Bayer AG
Renault
Clayton Copula simulated u1, u2, u3 with alfa = 0.53
Figure 6.3
Clayton copula with α = 0.53
0
0.2
0.4
0.6
0.8
1
0
0.5
1
0
0.2
0.4
0.6
0.8
1
ABN Amro
Bayer
Renault
Clayton Copula simulated u1, u2, u3 with alfa = 5
Figure 6.4
Clayton copula with α = 5


## Credit Risk Applications

Simulation of Market Scenarios
193
0
0.2
0.4
0.6
0.8
1
0
0.5
1
0
0.2
0.4
0.6
0.8
1
ABN Amro
Bayer
Renault
Clayton Copula simulated u1, u2, u3 with alfa = 15
Figure 6.5
Clayton copula with α = 15
0
0.2
0.4
0.6
0.8
1
0
0.5
1
0
0.2
0.4
0.6
0.8
1
ABN Amro
Bayer
Renault
Frank Copula simulated u1, u2, u3 with alfa = 1.61
Figure 6.6
Frank copula with α = 1.61

194
Copula Methods in Finance
0
0.2
0.4
0.6
0.8
1
0
0.5
1
0
0.2
0.4
0.6
0.8
1
ABN Amro
Bayer
Renault
Frank Copula simulated u1, u2, u3 with alfa = 5
Figure 6.7
Frank copula with α = 5
0
0.2
0.4
0.6
0.8
1
0
0.5
1
0
0.2
0.4
0.6
0.8
1
ABN Amro
Bayer
Renault
Frank simulated u1, u2, u3 with alfa = 15
Figure 6.8
Frank copula with α = 15

7
Credit Risk Applications
7.1
CREDIT DERIVATIVES
Credit derivatives are financial contracts that allow the transfer of credit risk from one
market participant to another. In such a way, they facilitate greater efficiency in the pricing
and distribution of credit risk among financial market participants.
Credit derivatives attracted attention through the use of credit default swaps in the early
1990s. Credit default swaps – the basic credit derivatives products – allow banks to hedge
their credit risk associated with their loan and interest rate derivatives books without selling
or otherwise transferring the underlying asset.
In recent years credit derivatives have become the main tool for transferring and hedging
risk. The credit derivatives market has grown rapidly both in volume and in the type of
instruments it offers. Innovations in this market have been growing at an unprecedented
rate, and will likely persist in the near future.
Credit derivatives have experienced a lot of applications, ranging from hedging default
risk, freeing up credit lines, reducing the regulatory capital requirements, to hedging dynamic
credit exposure driven by market variables and diversifying financial portfolios by gaining
access to otherwise unavailable credits.
As evidence of the huge growth of this market, the outstanding balance of credit deriva-
tives contracts has increased from an estimated USD 50 billion in 1996 to almost USD 500
billion at the end of 2000. Volumes are continuing to grow: according to the latest survey
by Risk magazine (Patel, 2003), the volume of the credit derivatives market has reached an
outstanding notional of more than USD 2 trillion in February 2003. An extensive discussion
of the credit derivatives market and the evolution of the market can be found in the J. P.
Morgan “Guide to credit derivatives” (2000) and in Davies, Hewer and Rivett (2001).
The market is also developing outside the United States. According to a survey by the
British Bankers’ Association (BBA), the global credit derivatives market is estimated to
be at least twice as large as the US market. The exact size of the global credit derivatives
markets, however, is difficult to estimate, given the potential for overcounting when contracts
involve more than one counterparty, and also that notional amounts outstanding considerably
overstate the net exposure associated with those contracts.
Nowadays many new financial securities are being developed. Among the most com-
plicated of these instruments are the multiple underlying ones. These are instruments with
pay-offs that are contingent on the default realization in a portfolio of obligors. Default risk
at the level of an individual security has been extensively modeled using both the structural
and the reduced form approach.1 However, default risk at the portfolio level is not as well
understood. Default dependencies among many obligors in a large portfolio play a crucial
role in the quantification of a portfolio’s credit risk exposure for the effects caused by
1 See the structural models of Merton (1974), Geske (1977), Leland (1994), Longstaff and Schwartz (1995), and
the reduced form models of Duffie and Singleton (1999), Madan and Unal (1999), among others. We refer the
reader also to Arvanitis and Gregory (2001) for an extensive survey of credit risk.

196
Copula Methods in Finance
simultaneous defaults and by the joint dependency between them. This dependency may be
due to both macroeconomic (the overall economy) and microeconomic (sectoral and even
firm specific) aspects. These latter factors are referred to in the literature as credit contagion.
As reported in Jarrow and Yu (2001) there has been evidence of credit contagion in the
recent financial crisis in East Asia and in the USA where the downfall of a small number
of firms had an economy-wide impact.
Recently the credit derivatives market offers more and more innovative products. From the
simple single name credit default swaps, the market has proposed total return swaps, credit-
linked notes, credit spread options, and multiple underlying products. This last category
contains probably the most complex products to price and hedge, because their structure
is linked to a portfolio of underlying credits and, hence, their pay-offs depend on the joint
behavior of the underlying securities. Typical multiple underlying products are basket default
swaps (BDSs) and collateralized debt obligations (CDOs).
The main users of credit derivatives are large financial institutions and banks, followed by
securities firms and insurance companies. While banks and securities firms act both as sellers
and buyers of protection, insurance companies, which have reportedly increased their market
participation substantially in recent years, are primarily protection sellers, presumably using
their expertise at evaluating risk. Corporate firms have increasingly come to the market, but
primarily to buy protection to hedge their exposure in vendor financial deals. Hedge funds
are also relatively active participants, arbitraging perceived mispricing between the cash and
derivatives markets, and thus participating on both sides. Other participants include pension
funds and mutual funds, although their participation in the market is very limited.
7.2
OVERVIEW OF SOME CREDIT DERIVATIVES PRODUCTS
We give an overview of some credit derivatives products. We refer interested readers to the
recent guide provided by Davies, Hewer and Rivett (2001).
7.2.1
Credit default swap
A credit default swap is a bilateral contract where one counterparty buys default protection
with respect to a reference entity. The contract has a given maturity, but will terminate early
if the credit event occurs. In this contract one party, the protection seller, receives a premium
(expressed in basis points per annum on the notional amount and received every quarter)
from another party, the protection buyer, who will receive a payment upon the occurrence
of the credit event in respect of the reference entity. The protection seller is buying credit
risk while the protection buyer is selling credit risk. Since no asset is transferred, there is
no need to fund the position.
A specific asset (i.e. bond or loan) may be cited for determining the occurrence of the
credit event and payment upon default. If this is not so, there will be a deliverable option
for the protection buyer in case of default. This is the main difference between a credit
default swap and an asset default swap: in the latter case a specific asset has to be specified
and in the former case there is the so-called deliverable option.
Normally, the default payment is given by the notional amount minus the recovery amount
(net loss).
This contract allows a credit risky asset to be transformed into a credit risk-free asset by
purchasing default protection referenced to this credit.

Credit Risk Applications
197
Usually, there are two methods of settlement: physical delivery and cash settlement. With
physical delivery, the protection buyer delivers the defaulted asset in return for a payment
equal to the notional value of that asset. With cash settlement, the protection seller pays the
protection buyer an amount that is equal to the difference between the notional amount and
the price of the defaulted reference asset. The recovery rate is commonly determined by a
dealer survey.
In a digital binary default swap, the default payment is equal to a prespecified notional,
irrespective of the recovery value.
The credit event, which triggers the payment of the amount due to the protection seller
from the protection buyer, is defined in the documentation. The potential credit events are
usually based on those specified in the new 2003 ISDA Credit Derivatives Definitions: i.e.
bankruptcy, failure to pay (principal or interest), obligation default, obligation acceleration,
repudiation/moratorium, and restructuring.
The most common methodology for the valuation of a credit default swap may be found
in Arvanitis and Gregory (2001) Chap. 5 and in the excellent survey of Roncalli (2003).
Let us indicate the default time with the greek letter τ. S(t) represents the survival
function at time t
F(t) = S(t) = Pr(τ > t) = E [1 {τ > t}]
where F(t) is the c.d.f. of τ.
For the sake of completeness, when we need to refer to an origin time t0 we will indicate
with S(t0, t) = Pr (τ > t|τ > t0) = St0(t) the survival function between (t0, t).
The protection buyer pays the premium (fixed) leg to the protection seller who will pay
the default (floating) leg in the case of default. The premium leg is expressed as a margin
on the notional amount of the contract. Let t1, t2, . . . , tM be the payment dates for the
premium leg. Since the margin is not paid after default, the present value of the premium
leg is given by2
PL(t) =

tm⩾t
W · N(tm −tm−1) · E[B(t, tm) · 1{τ > tm}]
where T = tM is the maturity of the credit default swap, W is the premium (also called
the margin or the annuity), N is the notional amount of the contract, B(t, tm) indicates the
discount factor between (t, tm) , m = 2, . . . , M.
The present value of the default leg is given by
DL(t) = N · E [(1 −R (θ, τ)) · B(t, τ) · 1 {τ ⩽T }]
where R(θ, τ) indicates the recovery value, which may depend on default time τ and some
other parameters θ related to both macroeconomic (the entire economy) and microeco-
nomic (firm/business specific) factors. We assume independency between default times and
recovery rates.
In the following we suppose that the recovery value is independent of the default time.3
2 This expression is justified under a tm-survival measure P m as defined in Sch¨onbucher (2000).
3 Generally the mark to market procedures used by many large banks fix the recovery value to 30% for accounting
evaluations.

198
Copula Methods in Finance
We may express the present value of the credit default swap as the difference between
the two legs. Hence, the fair (premium) spread is given by
W =
(1 −R) · E [B(t, τ) · 1 {τ ⩽T }]

tm⩾t
(tm −tm−1) · B(t, tm) · E [1 {τ > tm}]
In the real activity, traders know the market quote of the premium for each tradable
reference entity. Hence, the mark to market evaluation of a credit default swap may be
obtained through a bootstrapping procedure in order to get the survival probabilities at each
payment date (or analogously constant-wise hazard rates) implied by the market spread
curve for that reference entity.
7.2.2
Basket default swap
A basket default swap is a contract similar to a credit default swap, except that it is indexed
to a basket of reference entities rather than a single reference asset. This contract will
provide default protection on a number of entities in the basket of credits (typically from
three to five names). Typically it is as follows.
• First to default: offers protection against the first default only (i.e. the contract triggers at
the first default occurrence)
• Second to default: offers protection against the second to default only
• First k out of n to default: offers protection against the first k defaults
• Last j out of n to default: offers protection against the last j defaults
In the particular case of a first-to-default basket (1st to Def), it is the first credit in a basket
of reference obligors whose default triggers a payment to the protection buyer. As in the
case of a (single name) default swap, this payment may be cash settled. More commonly,
it will involve physical delivery of the defaulted asset in return for a payment of the par
amount in cash.
In return for protection against the 1st to Def, the protection buyer pays a basket spread
to the protection seller as a set of regular accruing cash flows. As with a default swap, these
payments terminate following the first credit event.
Similarly other credit products may be defined such as a second-to-default basket which
triggers a credit event after two or more obligors have defaulted, and so on from the
nth-to-default basket until the last-to-default basket.
Basket trades can permit substitutions whereby the reference obligations in the basket are
not fixed and can be swapped in and out by the protection buyer. Normally, the protection
buyer is only permitted to switch similar assets thereby maintaining, for example, a portfolio-
weighted rating, industry or geographical concentration limits. Besides, there are usually
some constraints on that if any default occurs.
This characteristic is usually pertained to the so-called percentage loss or first (or second,
and so on) loss. In these cases the exposure is to a percentage of the notional amount of
the underlying pool of reference obligations or up to a pre-agreed set amount, after which
the contract will terminate.

Credit Risk Applications
199
7.2.3
Other credit derivatives products
A credit spread option has a strike price based on a credit spread above the risk-free rate.
The option will be exercised if the credit spread of the underlying reference entity moves
above or below this strike spread, depending on whether the contract is a put or a call option
respectively. Credit spread options are not commonly traded and are privately negotiated.
In a step-up credit default swap, the premium paid by the protection buyer to the protection
seller increases after an agreed term. At the step-up date, the protection buyer has the option
of terminating the contract. If the contract is not terminated at the step-up date, the premium
paid to the protection seller is increased significantly. These types of transactions have been
used to reduce capital charges.
A total return swap, also known as the total rate of return swap, is an agreement under
which one party (“the total return payer”) transfers the economic risks and rewards associated
with an underlying asset to another counterparty (“the total return receiver”). The transfer
of risks and rewards is effected by way of an exchange of cash flows pertaining to any
change in the value and any income derived from the underlying asset (i.e. the total return).
All total return swap contracts are over-the-counter contracts and currently there are no
standard contractual definitions specific to the product.
In contrast to a credit default swap, a total return swap transfers both the credit risk and
the market risk associated with an underlying asset. The economic effect for a total return
receiver is the same as that derived from owning the asset.
A credit linked note is an instrument under which one party (“the issuer”) issues a note
to another party (“the investor”) in return for consideration equal to the principal value
(assuming that the note is issued at par) of the note. The coupon and the redemption of the
note are linked both to the credit quality of the issuer and to an obligation (“the reference
obligation”) of a third party (“the reference entity”).
Credit linked notes are often listed on a stock exchange. The issuer of a credit linked note
is equivalent to the protection buyer in a fully funded credit default swap. The investor in
a credit linked note is equivalent to the protection seller.
7.2.4
Collateralized debt obligation (CDO)
At a very simple level, a collateralized debt obligation (CDO) is a security backed by a
pool of assets (loans, bonds, credit default swaps, etc.) which are packaged together as a
portfolio and then tranched.
A CDO comprises a pool of underlying instruments (called collateral) against which
notes of debt are issued with varying cash flow priority. These notes vary in credit quality
depending on the subordination level. At inception when each note is issued, it usually
receives a rating from an independent agency (Moody’s, S&P, Fitch, etc.). The collateral of
a CDO is typically a portfolio of corporate bonds (or sovereign bonds, emerging markets
bonds as well) or bank loans or other types of financial facilities (residential or commercial
mortgages, leasing, lending, revolving facilities, even other credit derivatives, etc.).
In such a way, CDOs create a customized asset class by allowing various investors to
share the risk and return of an underlying pool of debt obligations. Hence, a CDO consists
of a set of assets (its collateral portfolio) and a set of liabilities (the issued notes).
A CDO cash flow structure allocates interest income and principal repayment from a col-
lateral pool of different debt instruments to a prioritized collection of securities notes, which

200
Copula Methods in Finance
are commonly called tranches. A standard prioritizing structure is a simple subordination,
i.e. senior CDO notes are paid before mezzanine and lower subordinated notes are paid,
with any residual cash flow, to an equity piece. The tranches are ordered so that losses
in interest or principal of the collateral are absorbed first by the lowest level tranche and
then in order to the next tranche, and so on. The lowest tranche is the riskiest one, and
because it has to respond immediately to the incurred losses it is called the equity tranche.
The mechanism for distributing the losses to the various tranches is called the waterfall.
Losses occur when there is a certain kind of credit event, explicitly defined in the offering
circular. A credit event is usually either a default of the collateral, or a failure to pay off
the collateral or other specified event according to the latest ISDA agreements.4 In either
case, the market value of the collateral drops; and, consequently, the issued related notes
are usually hit by a credit downgrade and by a market value slump.
Obviously, credit events are not independent, and their number is uncertain too. Clearly,
a diversification helps to manage investors’ risk and return profile, and an investor in a
particular tranche would like to know the probability distribution of losses to the underly-
ing pool of debt. The probability distribution depends on both the probability of a credit
event and on the relationship between two or more credit events (the relationship between
the default behavior of different obligors is called hidden linkage). Hence, the underlying
dependence structure is fundamental for any quantitative analysis on potential losses.
In the financial markets there are many kinds of CDOs. The most well-known types of
CDO are the cash flow CDOs, the market-value CDOs and the synthetic CDOs.
A cash flow CDO is one for which the collateral portfolio is not subject to active trading
by the CDO manager. The uncertainty concerning the interest and principal repayments is
determined by the number and timing of the collateral assets that default. Losses due to
defaults are the main source of risk.
A market-value CDO is one in which the CDO tranches receive payments based essen-
tially on the mark to market return of the collateral pool, as determined largely by the
trading performance of the CDO manager. A potential investor needs to evaluate the ability
of the manager and his or her institutional structure.
A synthetic CDO is one whose notes are synthetic, so the collateral portfolio is created
synthetically (i.e. it is not held by the structure but remains in the originator’s book). Each
note pays a fixed spread (commonly, in these structures, the spread is a fixed premium
added to a predetermined market floating rate, i.e. LIBOR rate).
Synthetic CDOs are very common in the so-called SuperSenior transactions. In this case
the higher protected tranche in the reference CDO (called SuperSenior because its credit
quality has to be higher than Aaa at inception) is the reference entity in a credit default
swap contract. In this contract one counterparty buys default protection with respect to this
SuperSenior tranche. The contract has a given maturity, but, obviously, it will terminate
early if the credit event occurs. The protection seller receives a premium (expressed in basis
points per annum on the notional amount) from the protection buyer that will receive a
payment upon the occurrence of the credit event in respect of the reference entity, i.e. the
SuperSenior tranche in the CDO structure. Normally, the default payment is given by the
notional amount minus the recovery amount (net loss). Since no asset is transferred, there
is no need to fund the position. For this reason these transactions are unfunded.
4 We refer readers to the J. P. Morgan “Guide to credit derivatives” (2000), and to O’Kane (2001) and Davies,
Hewer and Rivett (2001) for an extensive discussion of these concepts.

Credit Risk Applications
201
We are interested here in synthetic or cash flow CDOs, thus avoiding an analysis of the
trading behavior of CDO managers, because, otherwise, the analysis would take into account
microeconomic utility functions and invoke other concepts from Game Theory.
Basket default swaps (BDSs) and CDOs are essentially default correlation products; hence,
the main aspect for pricing and risk monitoring is to model the joint default dependency.
The modeling of dependent defaults is difficult because there is very little historical data
available about joint defaults and because the prices of these instruments are not quoted
(i.e. there are usually no reliable quotes in the market). Therefore, the models cannot be
calibrated, neither to defaults nor to prices.
Duffie and Garleanu (2001) address the risk analysis and market valuation of CDOs in a
jump-diffusion setting for correlated default intensities. They capture the default dependence
by assuming that each intensity process is given by the sum of two affine processes. One
process models the common aspect of different obligors, and the other concerns the idiosyn-
cratic default risk specific to each obligor. Their framework is theoretically appealing but
there are some disadvantages: the default correlation that can be reached with this approach
is typically too low when compared with empirical default correlations, and, furthermore,
it is not easy to analyze the resulting default dependency structure.
An extension of this approach are the infectious default models by Davis and Lo (2001)
and Jarrow and Yu (2001), which give more realistic default correlations. The major task
in these models is undoubtedly the estimation and calibration to historical data.
Copula methods are emerging as the favored pricing approach due to the simplicity in
simulation and calibration. Li (2000) proposes a methodology for the pricing of multi-names
contingent securities. Li proposed the Gaussian copula to capture the joint default depen-
dency in the collateral portfolio. Li’s methodology has been implemented into RiskMetrics
CDO Manager software, and may be seen as an extended version of the CreditMetrics
framework.5 Nowadays this product is well known in the financial environment and many
financial institutions around the world use it for pricing and risk monitoring CDOs. Also
Frey and McNeil (2001) analyze the effect of the choice of different copulas on the resulting
return distribution of a loan portfolio, and Mashal and Zeevi (2002) investigate comovements
between financial assets by introducing a T-copula structure and comparing this copula with
the Gaussian one with a likelihood ratio test.
Sch¨onbucher and Schubert (2001) present a method to incorporate dynamic default depen-
dency in intensity-based default risk models. They use a copula for the times of default,
which is combined with the individual intensity-based models for the defaults of the oblig-
ors. The authors do not offer an empirical comparison in order to select an appropriate
copula function.
In this chapter, we would like to provide a framework that allows us to price these
multiple underlying credit securities, and, also, to manage their risk. This approach is a
reduced-form approach as it avoids an accurate definition of the underlying stochastic default
process, concentrating instead on the dependence structure between pool obligors from a
statistical perspective. Since these products are correlation products, i.e. investors are buying
correlation risk, the dependence structure in the pool is essential for pricing, hedging and
risk managing purposes. Our approach is to use an adequate measure of dependence for
the collateralized portfolio, then to adopt multivariate survival and copulas frameworks to
5 CreditMetrics is a widely used portfolio-based credit methodology. Refer to the Credit Metrics Guide. RiskMetrics
Group http://www.riskmetrics.com.

202
Copula Methods in Finance
define an underlying dependence structure. The model incorporates the clustering of default
over time due to default correlation. By revisiting statistical survival analysis, it is possible
to construct a model for correlated times until default that has to be simulated. Finally, our
methodology allows us to price CDOs (and basket default swaps or percentage loss as well)
and to manage their risk by applying the appropriate pay-off functions to each series of
simulated times until default.
7.3
COPULA APPROACH
One of the main issues concerning credit risk is without doubt the modeling of joint dis-
tributions between default times. Li (2000) suggests that a Gaussian copula could be a
suitable tool for such a problem. The key issue of this framework is to shift the focus from
modeling the dependency between default events up to a fixed time horizon (i.e. discrete
variables) to the dependency between default times which are continuous random variables
and do not depend on an arbitrarily chosen time horizon.
We introduce the topic by briefly reviewing the survival time approach to single default
modeling and its calibration, and then examining the joint ones.
7.3.1
Review of single survival time modeling and calibration
Li (2000) describes a default by a survival function S(t) = Pr(τ > t), which indicates the
probability that a security will attain age t, in the spirit of the reduced form models of
Chapter 1. The survival time τ is called the time until default, or default time. If S is
differentiable, by defining the hazard rate or intensity h(u) = −S′(u)/S(u), the survival
function can be expressed in terms of the hazard rate function
S(t) = exp

−
 t
0
h(u) du

and the default arrival is an inhomogeneous Poisson process.
A typical assumption is that the hazard rate is a constant, h. In this case, the survival
time follows an exponential distribution with parameter h and the default arrival follows a
homogeneous Poisson process.
The survival time distribution may be easily generalized by assuming a Weibull distribution.
Duffie and Singleton (1998) and Lando (1998) consider h as a (non-negative, continuous,
adapted) stochastic process: in this case the process of default arrivals, as we recalled in
Chapter 1, is a Cox process. Under a Cox process the default time τ can be equivalently
characterized in one of the following ways:
τ := inf

t :
 t
0
hs ds ⩾θ

where θ is an exponential r.v. of parameter 1, independent of the intensity process, or:
τ := inf

t ⩾0 : ˇN > 0
	
where ˇN is the Cox process.
Under the Cox assumption, modeling a default process is equivalent to modeling the
intensity process. As there are many similarities between the hazard and the short rate,

Credit Risk Applications
203
many short rate processes may be borrowed to model the hazard rate. The affine class is
particularly appealing (see Chapter 1).
In both the Poisson and Cox cases, the hazard rate function used to characterize the
distribution of the survival time can be obtained for a given credit in many ways:
• From historical default rates provided by rating agencies;
• By using the Merton approach (refer to Delianedis & Geske, 1998);
• Extracting default probabilities by using market observable information, such as asset
swap spread, credit default swap spread or corporate bond prices (refer to Li, 1998).
In the first case one obtains the intensity or intensity process under the historical measure,
while in the second and third cases it is obtained under the risk neutral measure.
It is shown under the Duffie and Singleton (1998) approach that a defaultable instrument
can be valued as if it were a default-free instrument by discounting the defaultable cash
flow at a credit risk adjusted factor, as follows: let Y be a cash flow (random payment)
contingent on no default occurrence before T . Its value at time t is under zero recovery
E

exp

−
 T
t
rs ds

1{r>T }Y|ςt

= E

exp

−
 T
t
(rs + hs) ds

Y|Ft

(7.1)
where the expectation is taken, as usual, under a risk-neutral probability
• ςt is the market filtration, ςt = Ft ∨Ht
• Ht is the filtration generated by defaults: Ht = σ(τi ∧s, s ⩽t, i = 1, 2, . . . , I)
• Ft is the default-free filtration
and Y is FT -measurable.
Formula (7.1) is crucial in two respects. First, loosely speaking, increasing the short rate
by the intensity rate permits us to take default into account, and keep using the standard rule:
take as fair value the expected discounted value of the final pay-off. Second, the replacement
of the enlarged filtration ςt with the default-free one turns out to be of particular usefulness
in practical applications, for obvious reasons.
In addition, if the underlying factors affecting default and those affecting the interest
rate are independent, the credit risk adjusted discount factor is the product of the risk-free
discount factor, E[exp(−
 T
t rs ds)], and the pure credit discount factor, E[exp(−
 T
t hs ds)].
Under this framework, and the assumption of a piecewise constant hazard rate function
(extracted from some market data, i.e. asset swap spread or credit default swap spread at
different maturities), it is possible to specify the distribution of the survival time.
Our interest will be a credit portfolio of n assets and, in the following application, we will
price some multi-name credit derivatives. Therefore, we need to analyze the corresponding
multivariate problem and the joint survival times distribution.
7.3.2
Multiple survival times: modeling
Suppose you have I different firms, each with a Cox default arrival process, and define the
default time or survival time of the ith firm, τi, together with its intensity at time s, hi
s, and

204
Copula Methods in Finance
its threshold, θi. These quantities are related by the fact that
τi := inf

t :
 t
0
hi
s ds ⩾θi

Multiple default times and their association can be introduced in three different ways.
First, one can correlate directly the intensity processes of the I firms, hi
s, i = 1, . . . , I.
However, as Jouanin et al. (2001) show, correlating intensities does not permit us to obtain
high dependence between default times.
Second, one can adopt the approach of Li (2000): the joint survival function of the I firms,
S(t1, t2, . . . , tI) = Pr(τ1 > t1, τ2 > t2, . . . , τI > tI)
has, by the version of Sklar’s theorem in section 2.6, Chapter 2, a (survival) copula repre-
sentation,
S(t1, t2, . . . , tI) = Cτ1,τ2,...,τI (S1(t1), S2(t2), . . . , SI(tI))
Li models C directly using a Gaussian assumption.
Third, one can correlate the thresholds θi by assuming a specific copula for them:
S(m1, m2, . . . , mI) = Pr(θ1 > m1, θ2 > m2, . . . , θI > mI)
= Cθ1,θ2,...,θI (S1(m1), S2(m2), . . . , SI(mI))
where Si is the survival function of θi, S is their joint one. This is the so-called threshold
approach of Giesecke (2001) and Sch¨onbucher and Schubert (2001). In this framework,
one can derive the (survival) copula between the default times from the threshold one as
follows:
Cτ1,τ2,...,τI (S1(t1), . . . , SI(t1))
= E

Cθ1,θ2,...,θI

exp

−
 t1
0
h1
s ds

, . . . , exp

−
 tI
0
hI
s ds

In what follows we will not discuss which of the second and third approaches is “the better”,
since we will assume deterministic intensities, under which they coincide6:
Cτ1,τ2,...,τI = Cθ1,θ2,...,θI
In particular, we will refer to Li’s approach, which can be specified as follows: the
author extends the CreditMetrics model to a Gaussian copula model capturing the timing
risk of default. In this setup the pairwise default correlation of survival times is taken by the
pairwise asset correlation (refer to the CreditMetrics user manual). Each survival time for
6 However, a comparison between the two approaches is given in Jouanin et al. (2001).

Credit Risk Applications
205
the ith credit in the portfolio, τi, has a distribution function, Fi(t). Using a normal copula
we obtain the joint distribution of the survival times as:
F(t1, t2, . . . , tn) = n(−1 (F1 (t1)) , −1 (F2 (t2)) , . . . , −1 (Fn (tn)))
where n is the n-dimensional normal cumulative function with correlation matrix  (given
by the asset correlation matrix).
In order to simulate correlated survival times we introduce another series of random
variables Y1, Y2, . . . , Yn such that
Yi = −1 (Fi (ti))
for i = 1, 2, . . . , n
There is a one-to-one mapping between Y and τ. Li (2000) sums up in the following
scheme:
• Simulate Y1, Y2, . . . , Yn from an n-dimensional normal distribution with correlation matrix
given by the asset correlation of the underlying credit.
• Obtain τ1, τ2, . . . , τn using the relation τi = F −1
i
((Yi)) for i = 1, 2, . . . , n.
With each simulation run it is possible to generate survival times for all credits in the
portfolio. With this information one can price any credit derivatives structure written on the
portfolio.
As for risk monitoring, one has to look at the distribution of losses and take its percentiles.
Obviously, the simulation allows us to determine this distribution easily by taking into
account the CDO’s waterfall scheme and the simulated losses.
The ability to measure risk and assess prices relies on the details of each deal’s liability
structure (this point is very important, especially when one has to analyze a cash flow CDO
where, sometimes, the waterfall structure is particularly tailored to the deal, and may involve
a certain kind of overcollateralization test to be performed and other particularities that have
to be taken into account).
This approach may be extended to other copula functions by applying the sampling
algorithms described in Chapter 5.
7.3.3
Multiple defaults: calibration
If one could rely on no-arbitrage pricing of some multi-name credit derivative, it would
be possible to infer the implied default correlation (or concordance measure, in general),
in the same way as one could do with derivatives on multiple underlyings. However, we
have already remarked that the multi-name credit derivatives market is – at the present
stage – very illiquid. Therefore the relevant copulas can be calibrated in one of the follow-
ing ways:
• Estimating discrete default correlations, i.e. the correlations between the default indicators
at a given horizon, from historical joint default occurrences (see, for instance, Nagpal &
Bahar, 2001, Erturk, 2000, and the joint default probabilities in Carty, 1997): this method
is quite unsatisfactory, since the margins are Bernoulli r.v.s.

206
Copula Methods in Finance
• Estimating from the same observations the survival time correlations, i.e. the correlations
between the times to default, which are not Bernoulli.
• Using Moody’s diversity score, as in Jouanin et al. (2001) or Giesecke (2001).
• “Approximating” them through equity correlation, in the spirit of structural models.
We will take the last approach, as in most market practice (see, for instance, CreditMetricT M
and KMV’s Portfolio ManagerT M).
This approach may be extended to other copula functions by applying the sampling
algorithms described in Chapter 5. Obviously for multiple underlying credit instruments the
simulations from elliptical copulas, such as Gaussian and the Student t, are much easier
than what happens for other copulas because it is often really difficult to derive recursive
formulas to get the desired draws within a general n-variate setting.
In the following subsections we explain the pricing and risk monitoring for CDOs and
BDSs. We follow the approach and notation explained in the factor copula approach (i.e.
marginal distributions independent given a common latent factor) of Laurent and Gregory
(2002).
7.3.4
Loss distribution and the pricing of CDOs
Our aim is to compute the fair price at time 0 as the expected pay-off at time 0 for a standard
CDO. For simplicity, we also assume independence between default dates and interest rates,
since the most important issue we address is the modeling of dependence between default
dates. Similarly we assume that the recovery rates on the underlying assets are independent
of default times and interest rates; hence, we would like to proceed as conditioned to the
joint determination of the interest rates and recovery rates.
We consider n reference obligors with a nominal amount Ai and a recovery rate Ri with
i = 1, 2, . . . , n. Li = (1 −Ri)Ai will denote the loss given default (or net loss) for the
ith credit. Let τi be the default time of the ith name and Ni (t) = 1{τi<t} be the counting
process which jumps from 0 to 1 at the default time of name i. Finally L(t) will denote the
cumulative loss on the collateral portfolio at time t:
L(t) =
n

i=1
LiNi (t)
(7.2)
which is thus a pure jump process.
Let us consider a tranche of a CDO, where the default payment leg pays all losses that
occur on the collateral portfolio above a threshold C and below a threshold D, where
0 ⩽C ⩽D ⩽n
i=1 Ai.
When C = 0 we consider the equity tranche; if C > 0 and D < n
i=1 Ai we speak of the
mezzanine tranches, and when D = n
i=1 Ai we consider senior or SuperSenior tranches.
Let M(t) be the cumulative losses on a given tranche, hence
M(t) =



0
if L(t) ⩽C
L(t) −C
if C ⩽L(t) ⩽D
D −C
if L(t) ⩾D
(7.3)

Credit Risk Applications
207
or equivalently:
M(t) = (L(t) −C)1{C,D}(L(t)) + (D −C)1{D,n
i=1 Ai}(L(t))
We notice that as L(t), M(t) is a pure jump process. By using this framework the default
payments are the increments on M(t). Hence there is a payment on every jump of M(t).
Since M(t) is an increasing process, we can define Stieltjes integrals with respect to
M(t). But, M(t) is constant apart from jump times, so any Stieltjes integral with respect to
M(t) turns out to be a discrete sum with respect to every jump time.
Let B(0, t) be the discount factor for the maturity t, and let T denote the maturity of the
CDO. Hence, we can write the price of the default payment leg of the given tranche as:
EP

 T
0
B(0, t) dM(t)

where P denotes a risk-neutral probability measure.7
The term within the square brackets is the sum of the discounted default payments on
the tranche. By using the integration by parts and Fubini’s theorem we have:
EP

 T
0
B(0, t) dM(t)

= B(0, T )EP [M(T )] +
 T
0
f (0, t)B(0, t)EP [M(t)] dt
(7.4)
where f (0, t) denotes the instantaneous forward rate:
f (0, t)B(0, t) = −dB(0, t)
dt
The default leg may be discretized as follows8:


i=1
B(0, ti)

M(ti) −M(ti−1)

where t0 = 0 and t = T ,  indicates the number of payment dates between successive
defaults by the maturity T .
We would like to remark that we only need the first moment of the cumulative loss on
the tranche. This can be computed when the distribution of total losses has been simulated
via a pure Monte Carlo approach.
The fair spread (or equivalently the fair premium) of that tranche has to be found by
putting into an equivalence the default leg with the premium leg.
7 We observe that the risk-neutral measure P is not likely to be unique, since the market is incomplete in this
setup without further assumptions on the structure of the market. What we have in mind, and what we need here,
is that the market chooses some P that we take as given. The same observation will apply many times in what
follows.
8 We assume that the net default payments occur at  discrete dates between 0 and T .

208
Copula Methods in Finance
In this discrete time case the premium leg may be written as:
EP
 m

i=1
i−1,i · W · B(0, ti) · [D −C] · 1(L(t)⩽C)
+
m

i=1
i−1,i · W · B(0, ti) · [D −L(t)] · 1(C⩽L(t)⩽D)

where D −C is the tranche size at inception, and where m denotes all premium payment
dates, ti denotes the premium payment date, i−1,i denotes the tenor between successive
premium payment dates which takes into account the day count convention, W is the
fair spread, D −L(t) is the outstanding tranche notional at time t ∈[0, T ] and, clearly,
0 ⩽M(t) ⩽D −C since 0 ⩽L(t) ⩽n
i=1 Ai for all t.
This formula may be written also as:
EP
 m

i=1
i−1,i · W · B(0, ti) min {max [D −L(t), 0] , D −C}

(7.5)
In a continuous time setting, if we suppose that the premium is paid instantaneously, we
may express the discounted value at time 0 of the premium leg of a CDO as
W · EP

 T
0
B(0, t)g(L(t)) dt

where g(L(t)) = min {max [D −L(t), 0] , D −C}.
Hence, the fair (equilibrium) instantaneous spread (or premium) W is given by
W =
EP  T
0 B(0, t) dM(t)

EP
 T
0 B(0, t)g(L(t)) dt

We remark that the only thing we need in order to price each CDO tranche is to obtain
the simulated counting process via the chosen copula framework.
Moreover we stress that we model the copula of the times to default of the different
obligors, without considering the possible stochastic dynamics of the default intensities;
since our default intensities are assumed to be deterministic functions of the time, i.e.
constant stepwise functions where each step is given by the corresponding single name
credit default swap at the analysis date (refer to section 7.5, Technical Appendix, for more
details).
7.3.5
Loss distribution and the pricing of homogeneous basket default swaps
We consider the pricing of a basket default swap. In a first-to-default swap there is a default
payment at the first-to-default time. In a k out of n basket default swap (k ⩽n), where
n denotes the number of obligors, there is a default payment at the kth default time. The
payment corresponds to the non-recovered part of the defaulted asset.

Credit Risk Applications
209
If the notional amounts of all credits in the basket are equal then we refer to a homoge-
neous basket, i.e. Ai = A for every i = 1, 2, . . . , n.
As before, we compute separately the price of the premium leg and of the default leg.
The basket premium is such that the prices of the two legs are equal.
We make the same assumptions as in the previous chapter for the interest rates and the
recovery rates. Moreover, for simplicity, we do not take into account accrued premium
payments between payment dates.
We use the same notation as before.
N(t) = n
i=1 Ni(t) denotes the counting process indicating the total number of defaults
in the basket. If N(t) ⩾k the basket payments are exhausted. If 0 ⩽N(t) < k the premium
is paid on the outstanding notional for the ith underlying credit A for a homogeneous basket.
The discounted expectation of premium payment is given by:
EP


m

j=1
j−1,j · W · B(0, tj) · A · 1{N(t)<k}


(7.6)
The homogeneity assumption allows us to compute the price of the default payment leg
knowing the distribution of the number of defaults only.
We denote by Sk(t) = P (N(t) < k) the survival function of the kth default time τ(k), i.e.
Sk(t) = P (N(t) < k) = P (τ(k) > t) = 1 −Fk(t); hence dSk(t) = Sk(t + dt) −Sk(t) is the
probability that the kth default time occurs in [t, t + dt).
Under previous assumptions on interest rates and recovery rates (for simplicity we assume
that the recovery rate is the same for all names), we can then write the price of the kth-to-
default payment leg as:
EP [(1 −R) · A · B(0, τk) · 1(0⩽τ(k)⩽T)] = (1 −R) · A
 T
0
B(0, t) dFk(t)
(7.7)
where T is the maturity of the homogeneous k out of n default basket.
The default leg in brackets may also be written as follows:
−(1 −R) · A
 T
0
B(0, t) dSk(t)
= (1 −R) · A

1 −Sk(T )B(0, T ) +
 T
0
Sk(t) dB(0, t)

= (1 −R) · A

1 −Sk(T )B(0, T ) −
 T
0
f (0, t)B(0, t)Sk(t) dt

where, as before, f (0, t) denotes the instantaneous forward rate:
f (0, t)B(0, t) = −dB(0, t)
dt
In the following empirical application we simulate via the copula framework the distri-
bution of the times to default number and the distribution of each kth default time with
k = 1, 2, . . . , n.

210
Copula Methods in Finance
Table 7.1
Collateral portfolio description
Initial portfolio par value
500 000 000 euros
Number of obligors
50
Moody’s diversity score
29.25
Maturity date
18/05/2006
Table 7.2
Tranches of the CDO
Tranche name
Notional in euros
SS
437 500 000
A
11 000 000
B
19 500 000
C
20 000 000
Equity
12 000 000
As before, in a continuous time setting, we have:
W =
EP 
(1 −R)
 T
0 B(0, t) dFk(t)

EP
 T
0 B(0, t)Fk(t) dt

7.4
APPLICATION: PRICING AND RISK MONITORING A CDO
7.4.1
Dow Jones EuroStoxx50 CDO
In this section we extend the empirical example shown in Meneguzzo and Vecchiato (2004).
This empirical application, as far as we know, is the first application to a real market CDO
and a real market basket default swap (BDS).
We consider a synthetic CDO called EuroStoxx50 because it is composed by 50 single
name credit default swaps on 50 credits that belong to the DJ EuroStoxx50 equity index.
Each reference credit has a notional equal to 10 million euros, hence the collateral portfolio
has a nominal amount equal to 500 million euros. The inception date of this CDO was May
18, 2001, and it lasts 5 years with a maturity on May 18, 2006. This CDO is composed
by five tranches with the standard prioritized scheme. The riskiest tranche is the equity
tranche, which did not have a Moody’s rating at inception, then, in order, we have four
other tranches respectively rated at inception Baa3, Aa2, AAA and, finally, the less risky
tranche called SuperSenior (SS). Tables 7.1 and 7.2 report the CDO structure. Up to now
this CDO has not experienced any default.
The analysis date is set on August 30, 2002. We report some pictures depicting the
collateral by rating at the analysis date, and the collateral description by industry sector (see
Figures 7.1 and 7.2).
7.4.2
Application: basket default swap
The description of the basket default swap we are going to analyze may be found in
Tables 7.3 and 7.4.

Credit Risk Applications
211
Collateral by Rating
12%
8%
8%
4%
12%
34%
4%
8%
8%
2%
A1
A2
A3
Aa1
Aa2
Aa3
Aaa
Baa1
Baa2
Baa3
Figure 7.1
Collateral description by rating
Collateral by Industry
4%
20%
4%
6%
14%
4%
2%
6%
6%
2%
2%
12%
8%
10%
Auto Manufacturers 
Bank
Beverages
Chemicals
Communications Technology 
Electric Components & Equipment 
Diversified Financial
Food
Health Care Providers 
Consumer & Household Products & Services
Industrial-Diversified
Insurance
Oilfield Equipment & Services 
Water Utilities 
Figure 7.2
Collateral description by industry sector
Table 7.3
Basket default swap
Initial par value
40 000 000 euros
Number of obligors
4
Moody’s diversity score
3.25
Maturity date
30/08/2007

212
Copula Methods in Finance
Table 7.4
Basket default swap at August 30, 2002
Name
Amount (euros)
5y CDS spread
Country – Industry sector
ABN Amro
10 000 000
40
NL – Banking & Finance
Bayer AG
10 000 000
45
DE – Pharmaceutical
Renault
10 000 000
110
FR – Automotive
Telecom Italia
10 000 000
155
IT – Telecommunication
In this contract the first-to-default swap stated (contractual) spread has been fixed to
270 bps.
7.4.3
Empirical application for the EuroStoxx50 CDO
We follow the IFM method by using the corresponding equity prices for each obligor both
in the CDO and in the default basket. Obviously this is a trick solution because, as may
be seen, one cannot observe a time to default series, so one is compelled to use alternative
proxies to get the desired parameter both for the marginals and for the copula itself. As
always in the financial market, the equity prices are the best proxies for such a task.
In the following we report some graphs regarding the behavior of such equity returns.
Daily equity returns for each reference credit go from September 1, 2000 to August 30,
2002 (Figures 7.3 and 7.4).
As can be seen, the returns pattern shows evidence of heteroskedasticity behavior common
to all daily equity returns. We decide to overcome this fact by taking a GARCH(1, 1) filter
with Student t error term in order to capture the fatness of the return series tails. For the
sake of completeness we report this model as follows:
yt = σtεt
σ 2
t = α + βy2
t−1 + γ σ 2
t−1
where εt ∼i.i.d. tυ (0, 1).
The estimation method is the standard QMLE. We report some results in Table 7.5. These
results (except Renault) are for the obligors that belong both to the EuroStoxx50 CDO and
to the basket default swap.
−0.1
−0.08
−0.06
−0.04
−0.02
0
0.02
0.04
0.06
0.08
0.1
04/09/00
04/10/00
04/11/00
04/12/00
04/01/01
04/02/01
04/03/01
04/04/01
04/05/01
04/06/01
04/07/01
04/08/01
04/09/01
04/10/01
04/11/01
04/12/01
04/01/02
04/02/02
04/03/02
04/04/02
04/05/02
04/06/02
04/07/02
04/08/02
Figure 7.3
Daily equity returns: Telecom Italia

Credit Risk Applications
213
−0.15
−0.1
−0.05
0
0.05
0.1
0.15
0.2
0.25
04/09/00
04/10/00
04/11/00
04/12/00
04/01/01
04/02/01
04/03/01
04/04/01
04/05/01
04/06/01
04/07/01
04/08/01
04/09/01
04/10/01
04/11/01
04/12/01
04/01/02
04/02/02
04/03/02
04/04/02
04/05/02
04/06/02
04/07/02
04/08/02
Figure 7.4
Daily equity returns: Bayer AG
Table 7.5
Estimated GARCH(1, 1) parameters and standard errors
ABN Amro
Bayer AG
Renault
Telecom Italia
α
0.00002
0.00003
0.00005
0.00003
Std err.
0.00000
0.00000
0.00000
0.00000
β
0.15757
0.13798
0.10433
0.07372
Std err.
0.00092
0.00174
0.00037
0.00033
γ
0.81121
0.80056
0.83082
0.87794
Std err.
0.00061
0.00147
0.00032
0.00014
υ
7.67061
8.02422
6.25853
5.39743
Std err.
0.09881
0.06757
0.05987
0.06566
As expected, all GARCH parameters in Table 7.5 are statistically significant.
As for the joint behavior, we consider the normal, the Student t and two Archimedean
copulas.
When we adopt the normal copula we only need to identify the variance–covariance
matrix. An important point is to determine a robust estimate of that matrix. As noted by
Lindskog (2000), the Pearson correlation estimator is not robust for heavy tailed distribu-
tions, so the author recommends the use of Kendall’s tau, especially when the dimensionality
increases. In our case, we have 50 dimensions, and all the equity prices show fatness in
the tails. Hence, we adopt an estimation for the variance–covariance matrix obtained by
computing the empirical Kendall tau coefficient between each pair of equity series.
The empirical Kendall’s tau is computed as presented in section 7.5.
We report the scatter plot for some reference entities where it is possible to see more
dispersion in the tails (Figures 7.5 and 7.6). For such a reason we consider a Student t copula.
When we use the Student t copula we need to identify the degrees of freedom parameter.
We choose to estimate it by the IFM method since, previously, we had estimated all marginal
distributions (Student t c.d.f. is applied to the standardized residuals obtained from the
Student t –GARCH(1, 1) processes in order to map them on [0, 1]n).
Figure 7.7 presents the graph of the likelihood function for different degrees of freedom.
As can be seen, the MLE for the degrees of freedom parameter is approximately equal to 8.

214
Copula Methods in Finance
0.1
0.08
0.06
0.04
0.02
0
−0.02
−0.04
−0.06
−0.08
−0.1
−0.15
−0.1
−0.05
0
0.05
Telecom Italia
Bayer AG
0.15
0.1
0.2
Figure 7.5
Scatter plot: Bayer AG–Telecom Italia
0.15
0.1
0.05
0
−0.05
−0.1
−0.15
−0.2
−0.15
−0.1
−0.05
0
0.05
ABN Amro
Bayer AG
0.15
0.1
0.2
Figure 7.6
Scatter plot: ABN Amro–Bayer AG
We find statistical significance for this parameter by using a statistical bootstrap procedure
(refer to Efron & Tibshirani, 1993).
The same approach has been applied to the Clayton copula after having determined its
copula density (see section 7.5 for a formal derivation).

Credit Risk Applications
215
Likelihood Student Copula
−15000
−10000
−5000
0
5000
10000
15000
Degree of Freedom
Likelihood Student Copula
Likelihood Student Copula −10793 9955 10200 10067 9940 9823 9720 9630 9533 9465 9404 9350 9290 9247 9208 9172 9139 9101 9074
1
5
9
14
18
22
26
30
35
39
43
47
52
56
60
64
68
73
77
Figure 7.7
Student copula likelihood
6000
Likelihood Clayton Copula
Likelihood Clayton Copula
Alfa
4000
2000
0
0
0.5
1
1.5
−2000
−4000
−6000
−8000
Figure 7.8
Clayton copula likelihood
As before we adopt the IFM method to obtain an estimate for the Archimedean copula
parameter. In Figure 7.8 we present the form of the log-likelihood function.
The IFM estimator for alpha is equal to 0.48. As before, its significance is supported by
a bootstrap procedure. In order to get the simulations for each obligor’s time to default, we
assume a marginal density for each obligor’s time to default, according to an exponential
density for which the hazard term has been derived by the credit default swap curve at

216
Copula Methods in Finance
August 30, 2002, for each obligor in the collateral (see Table 7.6). Each hazard term is
assumed as follows:
ht =
St
1 −R
where the recovery rate R is fixed to 30%, as is common practice, in order to price the
credit default swap contract, and St represents the credit default swap spread at a given
term t.
In Table 7.6 we report for each obligor the credit default swap curve as at August 30,
2002 (the analysis date).
We would like to refer the readers to section 7.5 for a more extensive discussion and
further details about the time to default derivation, given the hazard rate.
We also present some histograms in order to show the simulated time to default distribu-
tion for some reference credit in the collateral (Table 7.7).
Since, for pricing purposes, we are interested in the number of defaults that may occur
prior to maturity of the CDO, we report in Table 7.8 the percentage of these times, for some
obligors, in 10 000 simulations before maturity, expressed in annual points (3.77 years).
7.4.4
EuroStoxx50 pricing and risk monitoring
In our empirical application we generate, for each reference credit in the collateral portfolio,
an exogenous recovery rate from an independent, Beta distribution9 that is across all obligors
and independent from the times to default and the interest rates.
We report the results for each chosen copula in Tables 7.9, 7.10 and 7.11. The fair spread
is computed by equaling the premium leg and the default leg of the contract for each chosen
copula. Clearly, this is related to the expected loss as shown previously.
The loss statistics for each copula are reported in Tables 7.12, 7.13 and 7.14.
In the previous tables each level of VaR was computed from the percentile of each
tranche’s cumulative losses distribution. As can be seen, results from the elliptical copulas
are close to each other. The Student copula is able to capture more fatness in the tail.
The results from the Clayton copula do not appear to be useful, because this copula
is not able to capture the upper tail dependence. Tail dependence is important to obtain
more simulated times to default before the deal matures. We will return to this point in the
following basket default swap empirical analysis.
Finally, we present the Box–Wishart plot for the collateral losses. As can be seen, the
Student copula gives more losses than any other simulated copula (Figure 7.9).
9 The Beta distribution has a range 0 ⩽x ⩽1 and shape parameters v > 0 , ω > 0. Its density is given by:
xv−1(1 −x)ω−1
B(v, ω)
where B(v, ω) =
 1
0 uv−1(1 −u)ω−1du.
Its mean is equal to v/(v + ω) and its variance is equal to vω/[(v + ω)2(v + ω + 1)].
We choose the parameters v, ω by fixing the mean equal to 50% and variance equal to 30% (these data are
reported in a latest Moody’s study on recoveries from defaulted corporate bonds).

Table 7.6
Collateral obligors and mid-market CDS 1-, 3- and 5-year spreads at August 30, 2002
Obligors
1 yr
3 yr
5 yr
Obligors
1 yr
3 yr
5 yr
ABN Amro
20
30
40
Generali
40
55
60
Aegon NV
150
230
230
HypoVereinsbank
20
25
32
Ahold
140
150
160
ING Groep
30
35
49
Air Liquide
35
50
50
LVMH
170
180
195
Alcatel SA
1500
1500
1500
L’Oreal
15
22
30
Allianz AG
40
50
75
Munich Re
50
70
75
Aventis
25
40
45
Nokia
100
140
140
Axa
130
200
200
Philips
130
160
170
Basf
15
30
30
Pinault-Printemps
420
420
420
Bayer AG
27
35
45
Repsol YPF
525
525
525
BBVA
25
40
45
Royal Dutch Petrol.
10
20
25
BNP Paribas
20
25
30
Royal KPN NV
250
290
315
BSCH
45
60
65
RWE
30
45
65
Carrefour
40
50
65
San Paolo-IMI
20
25
40
DaimlerChrysler
110
140
155
Sanofi-Synthelabo
30
40
50
Danone
15
30
30
Siemens
45
60
70
Deutsche Bank
22
35
40
Soci´et´e Generale
25
30
38
Deutsche Telecom
300
345
335
SUEZ
50
70
95
Dresdner Bank
20
30
40
Telecom Italia
135
155
155
E.on
35
60
60
Telefonica
160
170
205
Endesa SA
75
100
100
TotalFinaElf
10
15
25
Enel Spa
40
50
60
Unicredito
20
30
37
ENI
15
25
32
Unilever
25
35
45
Fortis
30
40
45
Vivendi Universal
975
1150
1150
France Telecom
435
460
470
Volkswagen
50
65
78

218
Copula Methods in Finance
Table 7.7
Histogram of simulated default times for Bayer AG and Air Liquide
Gaussian copula (Bayer AG)
1600
1400
1200
1000
800
600
400
200
0
2000
1800
1600
1400
1200
1000
800
600
400
200
00
500
1000
1500
2500
2000
3000
1800
1600
1400
1200
1000
800
600
400
200
00
200
400
600
800 1000 1200 1400 1600 1800 3000
1800
1600
1400
1200
1000
800
600
400
200
00
500
1000
1500
2000
2500
2000
1800
1600
1400
1200
1000
800
600
400
200
00
500
1000
1500
2500
2000
1600
1000
500
0
0
200
400
600
800
1000
1200
1400
1600
0
500
1000
1500
2000
2500
Gaussian copula (Air Liquide)
Student copula (Bayer AG)
Student copula (Air Liquide)
Clayton copula (Bayer AG)
Clayton copula (Air Liquide)

Credit Risk Applications
219
Table 7.8
Percentage of default times before CDO maturity
Gaussian
Student
Clayton
Air Liquide
0.0154%
0.0177%
0.0137%
Pinault-Printemps
0.1968%
0.1983%
0.1415%
Bayer AG
0.0133%
0.0137%
0.0106%
BNP Paribas
0.0101%
0.0108%
0.0094%
Table 7.9
Results: Gaussian copula
Tranche
Fair spread
Expected loss
SS
0.03%
496 364
A
0.77%
346 588
B
1.93%
1 509 068
C
6.97%
5 142 699
Equity
23.07%
7 607 209
Table 7.10
Results: Student copula 8 d.o.f.
Tranche
Fair spread
Expected loss
SS
0.04%
795 313
A
0.97%
430 133
B
2.10%
1 628 398
C
6.61%
4 893 133
Equity
22.04%
7 474 042
Table 7.11
Clayton copula α = 0.48
Tranche
Fair spread
Expected loss
SS
0.00%
3,523
A
0.04%
16 350
B
0.34%
281 028
C
4.04%
3 267 464
Equity
18.53%
7 224 680
Table 7.12
Loss statistics: Gaussian copula
Statistics
SS
A
B
C
Equity
Median
0
0
0
0
9 858 666
Mean
496 364
346 588
1 509 068
5 142 699
7 607 209
Std. dev.
4 165 898
1 833 116
4 676 705
7 453 992
4 934 804
Min
0
0
0
0
0
Max
89 465 261
11 000 000
19 500 000
20 000 000
12 000 000
95% VaR
0
0
16 618 167
20 000 000
12 000 000
99% VaR
20 072 488
11 000 000
19 500 000
20 000 000
12 000 000

220
Copula Methods in Finance
Table 7.13
Loss statistics: Student copula 8 d.o.f.
Statistics
SS
A
B
C
Equity
Median
0
0
0
0
9 360 774
Mean
795 313
430 133
1 628 398
4 893 133
7 474 042
Std. dev.
6 432 416
2 044 136
4 918 527
7 407 938
4 916 958
Min
0
0
0
0
0
Max
133 924 467
11 000 000
19 500 000
20 000 000
12 000 000
95% VaR
0
0
19 045 358
20 000 000
12 000 000
99% VaR
28 117 222
11 000 000
19 500 000
20 000 000
12 000 000
Table 7.14
Loss statistics: Clayton copula α = 0.48
Statistics
SS
A
B
C
Equity
Median
0
0
0
0
8 717 641
Mean
3 523
16 350
281 028
3 267 464
7 224 680
Std. dev.
184 585
350 643
1 810 103
5 706 847
4 884 579
Min
0
0
0
0
0
Max
13 951 110
11 000 000
19 500 000
20 000 000
12 000 000
95% VaR
0
0
0
18 434 870
12 000 000
99% VaR
0
0
10 689 314
20 000 000
12 000 000
1
2
3
0
2
4
6
8
10
12
14
16
18
20
x 107
Values
Column Number
Figure 7.9
Collateral losses: 1. Gaussian 2. Student t 3. Clayton

Credit Risk Applications
221
7.4.5
Pricing and risk monitoring of the basket default swaps
Many previous discussions may be tailored to the basket default swap case. As before we
report in Tables 7.15, 7.16 and 7.17 the results obtained for each chosen copula. Due to its
smaller dimensions we also introduce the Frank copula in the analysis. In section 7.5 we
derive the Frank copula density (Table 7.18 reports the results) in order to get the MLE of
its parameter.
As for the loss statistics we report the results in Tables 7.19–7.22.
In Figures 7.10, 7.11 and 7.12 we show the likelihood function for each estimated copula
from the corresponding equity series returns. We estimated that the d.o.f. of the Student t
Table 7.15
Gaussian copula
Tranche
Fair spread
Last-to-default
0.00%
3rd-to-default
0.01%
2nd-to-default
0.12%
1st-to-default
2.34%
Table 7.16
T -copula 4 d.o.f.
Tranche
Fair spread
Last-to-default
0.00%
3rd-to-default
0.00%
2nd-to-default
0.14%
1st-to-default
2.53%
Table 7.17
Clayton copula α = 0.53
Tranche
Fair spread
Last-to-default
0.00%
3rd-to-default
0.00%
2nd-to-default
0.07%
1st-to-default
1.93%
Table 7.18
Frank copula α = 1.61
Tranche
Fair spread
Last-to-default
0.00%
3rd-to-default
0.00%
2nd-to-default
0.09%
1st-to-default
2.03%

222
Copula Methods in Finance
Table 7.19
Gaussian copula
Statistics
First-to-default
Median
0
Mean
1 111 719
Std. dev.
2 604 153
Min
0
Max
10 000 000
95% VaR
8 253 625
99% VaR
10 000 000
Table 7.20
Student copula 4 d.o.f.
Statistics
First-to-default
Median
0
Mean
1 190 738
Std. dev.
2 680 928
Min
0
Max
10 000 000
95% VaR
8 398 548
99% VaR
10 000 000
Table 7.21
Clayton copula α = 0.53
Statistics
First-to-default
Median
0
Mean
951 800
Std. dev.
2 411 352
Min
0
Max
10 000 000
95% VaR
7 666 130
99% VaR
10 000 000
Table 7.22
Frank copula α = 1.61
Statistics
First-to-default
Median
0
Mean
1 002 489
Std. dev.
2 479 172
Min
0
Max
10 000 000
95% VaR
7 919 957
99% VaR
10 000 000

Credit Risk Applications
223
300
−300
200
−200
100
−100
0
0
10
20
30
40
Degree of Freedom
Likelihood Student Copula
Likelihood Student Copula
50
60
70
80
Figure 7.10
Log-likelihood Student t copula
500
0
0
0.5
1
1.5
Alfa
Likelihood Clayton Copula
Likelihood Clayton Copula
2
2.5
3
−500
−1000
−1500
−2000
−2500
−3000
Figure 7.11
Log-likelihood Clayton copula
copula was approximately equal to 4; the alpha for the Clayton copula was equal to 0.53,
and the alpha for the Frank copula was equal to 1.61. All estimates, as before, are significant.
All comments previously made still apply.
In Figure 7.13 we show the scatter plot implied by the Gaussian copula with Kendall’s
tau dependence matrix for ABN Amro, Bayer AG and Renault SA; the Student t copula for
the same companies can be seen in Figure 7.14.
We conclude this application stressing that there is no standard way to model multiple
defaults. We have considered a pure Monte Carlo approach by using a copula framework

224
Copula Methods in Finance
5
0
0
0.5
1
1.5
2
2.5
Alfa
Likelihood Frank Copula
Likelihood Frank Copula
3
3.5
4
4.5
5
−5
−10
−15
−20
Figure 7.12
Log-likelihood Frank copula
1
0.8
0.6
0.4
0.2
0
1
0
0
0.2
0.4
ABM Amro
Gaussian Copula simulated u1, u2, u3
Bayer
Renault
0.6
0.8
1
0.5
Figure 7.13
Gaussian copula for ABN Amro, Bayer AG, Renault SA
as the choice of the copula function is crucial for pricing, hedging and risk monitoring. As
for credit risk purposes, the copula has often to be assumed, so we propose to select the
copula that allows us to obtain results closer to those found in the real market activity. In
such a way, we found that the choice of a Student t copula allows us to obtain more reliable
results.

Credit Risk Applications
225
1
0.8
0.6
0.4
0.2
0
1
0
0
0.2
0.4
ABM Amro
Student Copula simulated u1, u2, u3 with d.f. = 4
Bayer
Renault
0.6
0.8
1
0.5
Figure 7.14
Student t copula with 4 d.o.f. for ABN Amro, Bayer AG, Renault SA
7.5
TECHNICAL APPENDIX
7.5.1
Derivation of a multivariate Clayton copula density
An n-variate Clayton copula is given by:
C(u1, u2, . . . , un) =
 n

i=1
u−α
i
−n + 1
−1
α
where α > 0.
The Clayton copula density is given by:
∂nC
∂u1∂u2 . . . ∂un
= αn 

1
α + n



1
α

 n

i=1
u−α−1
i
  n

i=1
u−α
i
−n + 1
−1
α −n
where  indicates the usual Euler  function.
The derivation is very easy because it offers a recursive formula.
In the 4-variate case, as is necessary for the empirical application to the basket default
swap we have considered, we have the following density:
(1 + α)(1 + 2α)(1 + 3α)u−α−1
1
u−α−1
2
u−α−1
3
u−α−1
4

u−α
1
+ u−α
2
+ u−α
3
+ u−α
4
−3
 −1
α −4

226
Copula Methods in Finance
7.5.2
Derivation of a 4-variate Frank copula density10
A 4-variate Frank copula is given by:
C(u1, u2, u3, u4) = −1
α ln
!
1 + w1w2w3w4

e−α −1
 3
"
where α > 0 and wi = e−αui −1 for i = 1, 2, 3, 4.
We have:
∂wi
∂ui
= −αe−αui = −α (wi + 1)
for i = 1, 2, 3, 4
and
∂C
∂w1
= −1
α

e−α −1
 3

e−α −1
 3 + w1w2w3w4
·
w2w3w4

e−α −1
 3
hence
∂C
∂u1
=
(w1 + 1) w2w3w4

e−α −1
 3 + w1w2w3w4
Continuing by derivation:
∂2C
∂u1∂u2
=
∂
∂u2
 ∂C
∂u1

= −α (w1 + 1) (w2 + 1) w3w4 ·

e−α −1
 3

e−α −1
 3 + w1w2w3w4
2
and
∂3C
∂u1∂u2∂u3
=
∂
∂u3
 ∂2C
∂u1∂u2

= α2 (w1 + 1) (w2 + 1) (w3 + 1) w4

e−α −1
 3
·

e−α −1
 3 −w1w2w3w4


e−α −1
 3 + w1w2w3w4
3
Finally the copula density is given by:
∂4C
∂u1∂u2∂u3∂u4
= ∂
∂u4

∂3C
∂u1∂u2∂u3

=−α3 (w1+1) (w2+1) (w3+1) (w4+1)

e−α−1
 3
·

e−α −1
 6 −4

e−α −1
 3 w1w2w3w4 + w2
1w2
2w2
3w2
4


e−α −1
 3 + w1w2w3w4
4
It is really cumbersome to write down but it is easily maximized w.r. α.
The derivation of a general n-variate Frank copula may be obtained as previously done
for the 4-variate case, though it requires an overweight algebra.
10 W. Vecchiato would like to thank Lanhua Yu (Imperial College, London UK) for pointing out some imperfections
in a earlier version of this derivation.

Credit Risk Applications
227
7.5.3
Correlated default times
In our applications we do not focus on whether default occurs over the risk horizon (i.e.
the time to maturity of the credit derivatives contract), but on the precise time when the
default occurs. We are not concerned with rating migrations, but only with defaults. For
each credit in the collateral portfolio we have to determine its default time probability
distribution function. We choose to specify the default time distribution from the hazard
rates implied by the observed credit default swap (CDS) for terms of 1 year, 3 years and
5 years, at the analysis date, for each underlying single name credit. We choose this way
because the credit spreads can be observed from both the CDS market and the asset swap
market. With the explosive growth in the credit derivatives markets, the movement of the
credit spreads reflects more timely the market-based assessments of credit quality and the
market perception of both market and credit risk of each specific credit.
We can derive hazard rates from credit spreads as follows:
ht =
St
1 −R
where ht is the hazard rate, St is the CDS spread at term t and R is a recovery rate.
To understand the relationship presented we have to consider the cash flows exchanged
during a CDS. A fair valuation requires that the total amount of payment received by the
protection seller should equal the expected loss the seller has to pay the buyer when a
credit event (i.e. for simplicity the default) occurs (adjusting everything by the probability
of occurrence and discounting). This means that the expected payments have to be equal to
the expected loss.
First we discuss the payment (or premium) leg. Let Wt be a given CDS spread as a
function of time, hence the amount the protection seller receives in each tiny interval is
Wt dt. The probability that this payment will be received is equal to the probability that the
underlying credit has not defaulted by time t, i.e. 1 −F(t). Discounting by the risk-free
factor B(0, t) and integrating over the whole time T of the deal, we obtain the total expected
payment to the protection seller:
 T
0
B(0, t)Wt [1 −F(t)] dt
Now we examine the other side of the equation, i.e. the expected loss. Let R be a given
exogenous default rate. In each tiny interval of time the amount of money the protection
seller would pay to the protection buyer if the default occurs is equal to (1 −R) dt. The
probability that this payment will be due is equal to the unconditional probability that
the underlying credit defaults between time t and time t + dt, hence F(t + dt) −F(t). Dis-
counting and integrating as before, we arrive at the total expected loss of the protection seller:
(1 −R)
 T
0
B(0, t) [F(t + dt) −F(t)] dt = (1 −R)
 T
0
B(0, t)ht [1 −F(t)] dt
where ht is the hazard rate given by dF(t)/[1 −F(t)].
Thus, for any given time t, the relationship ht(1 −R) = Wt holds.11
11 It holds for any non-degenerate case.


## Option Pricing with Copulas

228
Copula Methods in Finance
Moreover, it is well known that the relation between the hazard rate and the cumulative
default probability (c.d.p.) is given by:
F(t) = 1 −exp

−
 t
0
h(s) ds

In the real world we do not have observations of the hazard rate for all periods of time,
but for only a finite set of times. In our application we have three observed points implied
by the single name credit default swap premium at terms of 1 year, 3 years and 5 years. In
general, we can have N points in time t1, t2, . . . , tN. Hence, we consider a stepwise constant
function of the time for each hazard rate by using the observable values of h. We can then
rewrite the continuous form of the c.d.f. for each obligor’s time to default into:
F(t) = 1 −exp

−
k

j=1
hjj


where hj = h

tj
 
, j = tj −tj−1 and
k =



1
if t ⩽t1
2
if t1 < t ⩽t2
...
N
if t > tN−1
This methodology has been used for each reference credit in the collateral portfolio in
order to obtain the draws for each time to default, after having generated draws from the
chosen copula.
These marginals may be easily extended to Weibull distributions by inserting a shape
parameter.
7.5.4
Variance–covariance robust estimation
As is well known for elliptical distributions, linear correlation is a natural measure of
dependence. However, a linear correlation estimator such as the Pearson standard correla-
tion estimator has shown a very poor performance for heavier tailed or contaminated data.
Therefore, robust estimators are needed – where “robust” means to be insensitive to contam-
ination and to maintain a high efficiency for heavier tailed elliptical distributions as well as
for multivariate normal distributions. Lindskog (2000) gives an overview of techniques for
a robust linear correlation estimation and for comparing contaminated and uncontaminated
elliptical distributions. Moreover, he shows that Kendall’s tau has the necessary robustness
properties and is an efficient (low variance) estimator for all elliptical distributions. For this
reason, in our application, we choose to adopt the empirical Kendall’s tau matrix (after
having checked that positive definiteness holds) instead of the standard Pearson variance–
covariance matrix estimator. We determine this matrix from the equity return data for each
obligor in the collateral portfolio, and we adopt it to obtain draws from each elliptical copula
we have considered.

Credit Risk Applications
229
For the sake of completeness we present the empirical Kendall’s tau for a chosen pair of
variables.
The consistent estimator of Kendall’s τ obtained from the two series S1t and S2t with
t = 1, . . . , T is defined as follows:
ˆτ =
2
T (T −1)

i<j
sgn

S1i −S1j
 
S2i −S2j
 
(7.8)
where the sign function is defined as commonly known:
sgn(x) =

1
if x ⩾0
−1
if x < 0
Another robust dependence measure is Spearman’s rho, also called rank correlation, which
may be seen to be the standard Pearson’s linear correlation between the ranks of two series.
Let X and Y be r.v.s with c.d.f. respectively FX and FY and joint c.d.f. F. Spearman’s
rho is given by
ρS(X, Y) = ρP(FX(X), FY (Y))
where ρP is the standard Pearson linear correlation.
The generalization of ρS to n > 2 dimensions can be done analogously to that of lin-
ear correlation. In such a way we obtain a Spearman’s correlation matrix that is positive
definite by construction, without applying the so-called eigenvalue method, i.e. the nega-
tive eigenvalue has to be replaced by an arbitrary small positive number (see Rousseuw &
Molenberghs, 1993), as must be done for a high-dimensional extension of Kendall’s tau.
A consistent estimator of Spearman’s rho may be obtained by the use of the standard
empirical correlation coefficient between the sample ranks of each series, hence
ˆρS = ˆρP

ˆFX(xi), ˆFY(yi)

7.5.5
Interest rates and foreign exchange rates in the analysis
One of the inputs used in the application is the par swap rate term structures for all currencies
involved in the CDO and in the BDS. Using the par swap rates it is possible to derive
discount factors for every maturity (i.e. commonly this procedure is termed as bootstrapping).
After deriving discount factors, one can determine forward interest rates for any needed
period and maturity. Since our focus is on effects due to collateral default, we do not
simulate interest rate and/or foreign exchange rates. But, one can choose to make these
simulations by calibrating the chosen models to observed variables for use in Monte Carlo
analysis. For example, one can assume that short-term forward interest rates follow a log-
normal process over time, and when simulating interest rates across multiple currencies one
has to find estimates for the correlations between the interest rates of different currencies;
it is important to assume that these processes are exogenous from the copula framework,
otherwise this task would involve higher and higher dimensionality problems.


8
Option Pricing with Copulas
8.1
INTRODUCTION
In this chapter we show how to use copula functions to solve the pricing problem of
multivariate contingent claims. The purpose is to derive pricing formulas which are valid
for very general distribution settings, beyond the standard Black and Scholes framework
under which closed form solutions are available for almost all the pricing problems. We
know that the assumptions on the basis of the Black–Scholes model have been challenged on
the grounds of two major arguments. The first is non-normality of returns, as implied by the
smile and term structure effects of implied volatility. The second is market incompleteness,
and the difficulty of providing exact replication strategies for all the contingent claims and a
unique pricing kernel for their prices. Both of these problems are amplified in a multivariate
setting. On the one hand, non-normality of the returns implies that the standard linear
correlation figure that has been currently used to recover the price is a biased tool; and as
shown in Chapter 3, in the presence of smile effects, linear correlation may turn out to be
smaller than 1 even in the case of perfect dependence between the markets. On the other
hand, market incompleteness in a multivariate setting is made more involved because of
the difficulty of recovering implied information concerning the dependence structure among
the assets. So, evaluating multivariate contingent claims in incomplete markets poses a
two-stage problem: choosing a pricing kernel for each and every asset in the underlying
basket and picking out the copula function representing the dependence structure among
them. Nowadays, multivariate contingent claims are widely used by financial institutions,
particularly to design structured finance products: on the one hand, it is all the more usual
to find multi-asset features in index-linked bonds and digital notes, providing the investor
with a diversified product; on the other hand, multicurrency options have been around for
a long time and have represented a relevant risk management service provided by banks to
corporate borrowers and investors.
The increasing trend in structured finance has highlighted the relevance of the multivariate
contingent claim pricing problem through a second important channel. In the structured
finance business, the financial institutions face the problem of hedging a large variety of
different risks, connected to derivative products which are often exotic and written on
underlying assets that might not be actively traded on liquid markets. As a result, the hedging
activity may heavily rely on transactions on the OTC market, where the counterparty risk
component can be relevant. Notice that accounting for counterparty risk in a derivative
transaction directly casts the problem in a multivariate setting. Intuitively, in fact, the value
of the derivative contract depends on two events: the first, that the contract ends in the
money; the second, that the counterparty survives until the contract is exercised. Taking
into consideration both the marginal probability of these two events and their dependence
structure may make both the evaluation and the hedging strategy of these products more
accurate and safe, and it is not difficult to foresee that copula functions can be of great help
to reach this goal.

232
Copula Methods in Finance
8.2
PRICING BIVARIATE OPTIONS IN COMPLETE MARKETS
Let us consider a derivative contract that is written on two underlying assets, which
we denote as S1 and S2. The information structure is represented in the usual way by
a filtered probability space {, ℑt, P } generated by the stochastic processes S1(t) and
S2(t), t ∈[0, T ]. Throughout the discussion, we will assume that S1(t), S2(t) are con-
tinuous random variables with non-negative support. If, for the sake of simplicity, we take
the bivariate derivative to be European, its pay-off may be written in full generality as
G(S1(T ), S2(T ), T ), a function defined ℜ3
+ →ℜ. Our problem is to recover a pricing func-
tion g(S1(t), S2(t), t) which would rule out arbitrage opportunities in the market. In the
case in which the market is complete, we know that this product, as any other one, can be
exactly replicated, and its price is uniquely determined. This unique price also corresponds
to a unique risk-neutral probability distribution Q(S1, S2 | ℑt), whose density function is
denoted q(S1, S2 | ℑt), which represents the pricing kernel of the economy. The price of
the bivariate contingent claim can then be represented in integral form as
g(S1(t), S2(t), t)
= B (t, T )
 ∞
0
 ∞
0
G(S1(T ), S2(T ), T )q(S1(T ), S2(T ) | ℑt) dS1(T ) dS2(T )
where B (t, T ) is the risk-free discount factor. Throughout the analysis the risk-free rate is
assumed to be non-stochastic or independent of the underlying assets. The extension to the
more general case is, however, straightforward if we change the measure to the forward
risk-neutral one, as described in Chapter 1.
Let us denote by Q1(S1 | ℑt) and Q2(S2 | ℑt) the marginal conditional distributions of
S1 and S2 respectively, with densities q1(S1 | ℑt) and q2(S2 | ℑt). They are also derived
from the bivariate pricing kernel by definition
q1(S1 | ℑt) =
 ∞
0
q(S1(T ), S2(T ) | ℑt) dS2(T )
q2(S2 | ℑt) =
 ∞
0
q(S1(T ), S2(T ) | ℑt) dS1(T )
Prices of univariate contingent claims are obtained as discounted expected values under
the relevant marginal risk-neutral distribution. So, if G(S1(T ), S2(T ), T ) = G(S1(T ), T ),
so that a contingent claim is written on asset S1 only we have
g(S1(t), t) = B (t, T )
 ∞
0
G(S1(T ), T )
 ∞
0
q(S1(T ), S2(T ) | ℑt) dS1(T ) dS2(T )
= B (t, T )
 ∞
0
G(S1(T ), T )q1(S1(T ) | ℑt) dS1(T )
8.2.1
Copula pricing kernels
In this complete market setting it is quite easy to write the pricing relationship of bivariate
contingent claims in terms of copula functions and marginal distributions. We only need the
extension of Sklar’s theorem to conditional distributions.

Option Pricing with Copulas
233
Theorem 8.1
For any joint conditional distribution Q(S1, S2 | ℑt) there exists a copula
function C(u, v) such that
Q(S1, S2 | ℑt) = C (Q1(S1 | ℑt), Q2(S2 | ℑt))
and, conversely, given two conditional distributions Q1(S1 | ℑt) and Q2(S2 | ℑt) and a
copula function C(u, v) the function C (Q1(S1 | ℑt), Q2(S2 | ℑt)) is a joint conditional
distribution function.
The proof is in Patton (2001). Notice that the result holds if the conditioning information
ℑt is the same for both marginal distribution and joint distributions. The copula obtained in
this way corresponds to the dependence structure in the risk-neutral probability distribution,
and is the risk-neutral copula.
Using copula functions enables us to separate the effects of the marginal pricing kernels
and the dependence structure of the underlying assets. This is very important because it
makes it possible to check the consistency of prices of multivariate and univariate contingent
claims, particularly with respect to the no-arbitrage requirement. As a simple example, let
us take digital options, as in the examples presented in Chapter 2. Remember that digital
options pay a fixed sum, which we may set equal to one unit of currency without loss of
generality, if some event takes place. The event may be that the price of the underlying
asset is higher than some strike level (call digital option). A put digital option instead pays
a unit of value if the value of the underlying asset is lower than a strike level. So, in a
complete market, the prices of univariate digital options, that is options written on a single
asset, are equal to the discounted values of risk-neutral probability distributions.
Call digital options DCi written on our assets S1 and S2 are priced as
DC1 (K1) = B (t, T ) Q1 (K1 | ℑt) ,
DC2 (K2) = B (t, T ) Q2 (K2 | ℑt)
where we recall that Qi (u) ≡1 −Qi (u). Of course, the corresponding put digital options
are priced by arbitrage as DPi = B −DCi. Consider now the case of bivariate digital
options paying one unit of currency if both assets S1 and S2 are higher than strike prices K1
and K2 respectively. Options like these are sometimes used in particular structured finance
products such as digital bivariate notes. Denoting DHH this digital option, we can write it
as a copula function taking the forward values of univariate digital options as arguments:
DHH(K1, K2) = B (t, T ) CHH
 DC1
B (t, T ),
DC2
B (t, T )

where CHH(u, v) is a copula function: in particular, this is the survival copula discussed in
Chapter 2. Once such a copula function has been chosen, the other digital options for the
same strikes are determined by arbitrage. For example, the digital option DHL paying one
unit if S1 > K1 and S2 ⩽K2 is determined by the relation
DHL(K1, K2) = DC1 −DHH(K1, K2)
= DC1 −B (t, T ) CHH
DC1
B , DC2
B


234
Copula Methods in Finance
We remind the reader (see Chapter 2) that if CHH(u, v) is a copula function, then
CHL(u, 1 −v) = u−CHH(u, v) is also a copula function, representing the probability that
the first uniform marginal be higher than u and the second be lower than v. The price of
the digital option DHL can then be written as
DHL(K1, K2) = B (t, T )
DC1(K1)
B (t, T ) −CHH
DC1(K1)
B (t, T ) , DC2(K2)
B (t, T )

= B (t, T ) CHL
DC1(K1)
B (t, T ) , DP2(K2)
B (t, T )

where we have exploited DP2 = B (t, T ) −DC2. By the same token, we have
DLH(K1, K2) = DC2(K2) −DHH(K1, K2)
= B (t, T ) CLH
DP1(K1)
B
, DC2(K2)
B

with CLH(1 −u, v) = v −CHH(u, v) representing the joint probability that the first marginal
be lower than u and the second be higher than v. Finally, the put bivariate digital, paying
one unit if S1 ⩽K2 and S2 ⩽K2 is obtained by arbitrage from
DLL(K1, K2) = B (t, T ) −DHL(K1, K2) −DLH(K1, K2) −DHH(K1, K2)
= B (t, T ) −DC1(K1) −DC2(K2) + DHH(K1, K2)
Again, remembering that CLL(1 −u, 1 −v) = 1 −u −v+ CHH(u, v) is a copula function
we have
DLL(K1, K2) = B(t, T )

1 −DC1(K1)
B (t, T ) −DC2(K2)
B (t, T ) + CHH
DC1(K1)
B (t, T ) , DC2(K2)
B (t, T )

= BCLL
DP1(K1)
B (t, T ) , DP2(K2)
B (t, T )

All of this proves that, just as in the univariate case, digital options paying under some
events are linked to those paying under the complement, and this induces a no-arbitrage
relation among copula functions. These relationships will be particularly useful in some of
the applications that we cover in the rest of this chapter. For the time being, this result
states that the requirement that a bivariate pricing kernel be a copula function is necessary
but not sufficient. Moreover, in general the shape of copulas CHH, CHL, CLH and CLL will
be different. We say in general because it is not difficult to find a counterexample: we leave
the readers to verify that the product copula CHH (u, v) = uv is such a case.
Representing the bivariate pricing kernel by a copula function enables us to specify the
dependence structure of the underlying assets and to gauge its effect on the price of the
bivariate contingent claim. Sticking to the simplest case of the bivariate digital option, we

Option Pricing with Copulas
235
have that
B (t, T ) C−
DC1(K1)
B (t, T ) , DC2(K2)
B (t, T )

⩽DHH(K1, K2)
⩽B (t, T ) C+
DC1(K1)
B (t, T ) , DC2(K2)
B (t, T )

where C−and C+ represent the Fr´echet bounds of copulas corresponding to the cases of
perfect negative and positive dependence respectively. Using such bounds we obtain
max (DC1(K1) + DC2(K2) −B (t, T ) , 0) ⩽DHH(K1, K2)
⩽min (DC1(K1), DC2(K2))
So, the price of a bivariate call digital option reaches its maximum value in the case
of perfect positive dependence, in which case it is worth the minimum of the univariate
digital options. Going back to the arbitrage arguments above, readers may verify that if
the value of such an option is maximum, i.e. DHH = min (DC1, DC2), the price of the
digital option DHL, i.e. the option paying if S1 > K1 and S2 ⩽K2, is minimum: DHL =
max (DC1 + DP2 −1, 0). On the question of the bivariate digital put option, paying one
unit if S1 ⩽K1 and S2 ⩽K2, we leave the simple answer to the readers.
8.2.2
Alternative pricing techniques
In the previous analysis we showed that a pricing kernel may be written in terms of copula
functions. In a complete market setting, the argument follows in quite a straightforward
way from the unique probability measure and an extension of Sklar’s theorem to the case
of conditional distributions. The same result obviously applies to incomplete market models
in which a specific probability measure is selected to compute the price. Throughout the
following sections, we will see whether the result carries over to more general pricing
models in an incomplete setting. Prior to that, we would like to explore the techniques that
can be applied to make the copula pricing kernel approach most effective. These approaches
will then represent the set of tools among which to choose the most effective to solve the
specific pricing problems that will be addressed at the end of this chapter.
The probability density approach
The most straightforward way to represent the price of a contingent claim is to use the
standard integral representation involving the joint conditional density q(S1, S2 | ℑt). The
representation can be written in terms of copulas, remembering the relationship
q(S1, S2 | ℑt) = c (Q1, Q2 | ℑt) q1 (S1 | ℑt) q2 (S2 | ℑt)
where we recall that c (v, z) is the density associated to the copula function. In other words,
the joint density is equal to the cross-derivative of the copula function times the marginal

236
Copula Methods in Finance
densities. Using this result we have that the price g(S1, S2, t) of our bivariate contingent
claim can be written
g(S1(t), S2(t), t) = B (t, T )
 ∞
0
 ∞
0
G(S1(T ), S2(T ), T )c (Q1, Q2 | ℑt)
× q1 (S1(T ) | ℑt) q2(S2(T ) | ℑt) dS1(T ) dS2(T )
Unfortunately, this representation of price does not lead to any simplification of the price
representation, as in most cases the formula for the cross-derivative of the copula function
turns out to be quite involved and difficult to handle, so that computing the double integral
may not come as an easy task. So, this representation can only be useful in cases in which
such cross-derivative is very easy to calculate, such as in the case of the product copula,
for which we have C12 = 1.
The probability distribution approach
An alternative to the integral representation above can be of some help in many cases. To
introduce this approach, it may be useful to go back to the univariate setting for a short
digression. Consider the case of a European option written on the underlying asset Z, for
strike price K and exercise date T . Let us denote CALL(Z, t; K, T ) the price of the option
at time t. We recall the famous result due to Breeden and Litzenberger (1978), discussed in
Chapter 1
−∂CALL (Z, t; K, T )
∂K
1
B (t, T ) = QZ (K | ℑt)
so that the derivative of the price of the call option with respect to the strike divided by the
discount factor is equal to the risk-neutral probability of exercising the option (apart from
a change in sign). Integrating both sides from K to infinity we may write the price of the
option as
CALL (Z, t; K, T ) = B (t, T )
 ∞
K
QZ(u | ℑt) du
Likewise, for put options we have
∂PUT (Z, t; K, T )
∂K
1
B (t, T ) = QZ (K | ℑt)
and, integrating from zero to K, we get
PUT (Z, t; K, T ) = B (t, T )
 K
0
QZ(u | ℑt) du
Notice that in the representations above the prices of call and put options are obtained
by computing the integral of the distribution function, rather than the density function.

Option Pricing with Copulas
237
Let us now go back to a bivariate problem. Assume, for example, that the pay-off function
of a contingent claim is of the kind
G(S1(T ), S2(T ), T ) = max

f (S1(T ), S2(T ), T ) −K, 0

and set Z(T ) = f (S1(T ), S2(T )). We may then use the integral representation above to
recover the price of this contingent claim as
CALL (S1(t), S2(t), t; K, T ) = B (t, T )
 ∞
K
Pr (f (S1(T ), S2(T ), T ) > u | ℑt) du
where the probability is computed under the risk-neutral measure Q.
Likewise, for pay-off functions of the put type
G(S1(T ), S2(T ), T ) = max

K −f (S1(T ), S2(T ), T ), 0

we may write the price of the contingent claim as
PUT (S1(t), S2(t), t; K, T ) = B (t, T )
 K
0
Pr (f (S1(T ), S2(T ), T ) ⩽u | ℑt) du
The pricing representations reported above may be particularly useful in all cases in
which the probability distribution of f (S1(T ), S2(T ), T ) is easy to handle analytically or
by simulation. Below, we will show some cases in which such a function is in fact a copula
function. Here we show a different example just to fix ideas.
Compo option. Take an option in which the value of the pay-off and the strike price are
denoted in a currency that is different from that of the underlying asset. An example is an
option written on Vodaphone stocks denominated in British pounds with a strike price in
euros. The pay-off of this option, say a call, is then written as
G(S(T ), e(T ), T ) = max [S(T )e(T ) −K, 0]
where S is the price of the underlying asset (Vodaphone in our case) denominated in foreign
currency and e is the exchange rate, determining the number of euros to be exchanged for one
pound. So, the method described above can be applied setting f (S(T ), e(T )) = S(T )e(T ).
We have
CALL (S(t), e(t), t; K, T ) = B
 ∞
K
Pr(S(T )e(T ) > u | ℑt) du
In cases in which the distribution of the product of the two variables is known or easy
to simulate, the above formula can be used. For example, we know that if S and e are log-
normally distributed, their product will also have log-normal distribution: it is not surprising
that the integral will have a closed form solution of the type of the Black–Scholes formula.
Unfortunately, beyond this case there are not many general results available for the product of
random variables, and the distribution will generally have to be reconstructed by simulation.

238
Copula Methods in Finance
The conditional distribution approach
A third approach to the pricing of bivariate contingent claims consists in evaluating the
contingent claim conditional on one of the two variables and integrating the result with
respect to the other one. As an example, consider again the case in which the pay-off
function is of the kind: max[f (S1(T ), S2(T )) −K, 0]. Intuitively the idea is quite simple.
Assuming that one knows the value of one of the two variables, say S2(T ) = s, one is able
to recover the value of the derivative. We have, for example
CALL (S1(t), t; S2(T ) = s, K, T ) = B (t, T )
 ∞
K
Pr(f (S1(T ), s) > u | ℑt) du
Then the price of the bivariate contingent claim can be recovered by integrating this
“conditional” price over the whole domain of S2. We then have
CALL (S1(t), S2(t), t; K, T ) = B (t, T )
 ∞
0
CALL (S1(t), t; S2(T ), K, T )
× q2(S2(T ) | ℑt) dS2(T )
Even in this case the use of copula functions can be of some help. We recall in fact from
Chapter 2 that
Q(S1 | S2 = s, ℑt) = ∂C (Q1, Q2 (s))
∂Q2 (s)
and the probability distribution of one of the two variables, conditional on a given value
of the other, is equal to the derivative of the copula function with respect to the marginal
distribution of the latter evaluated at that value.
Stochastic volatility. As an example, assume a pricing model in which both the price and
the volatility of the underlying asset are stochastic. The use of copulas may be particularly
useful to account for the dependence structure between price and volatility. Denote by
QS and Qσ the marginal probability distributions of the price of the underlying asset
and its volatility. The joint conditional distribution can then be written as Q(S, σ | ℑt) =
C(QS, Qσ | ℑt). Consider the problem of pricing a put option for strike K and exercise T .
It is clear that, conditional on a given value of volatility, σ = s, the value of the option
could be written
PUT (S(t), t; σ(T ) = s, K, T ) = B (t, T )
 K
0
Pr(S(T ) ⩽u | σ(T ) = s, ℑt) du
Using the copula function representation we could write
PUT (S(t), t; σ(T ) = s, K, T ) = B (t, T )
 K
0
∂C (Q1, Qσ (s) | ℑt)
∂Qσ (s | ℑt)
du
The price of the put option would then be
PUT (S(t), t, σ(t); K, T ) = B (t, T )
 ∞
0
 K
0
∂C (Q1, Qσ (s) | ℑt)
∂Qσ (s | ℑt)
du

qσ(s | ℑt) ds

Option Pricing with Copulas
239
The model is then able to capture the dependence structure between volatility and price
of the underlying asset. From this point of view, it may be checked that it is an extension
of the Hull–White model. In fact, if we take QS to be the log-normal distribution and
C(u, v) = uv the product copula, we obtain
PUT (S(t), t, σ(t); K, T ) =
 ∞
0
PUTBS (S, t; σ(t) = s, K, T ) qσ(s | ℑt) ds
where PUTBS(.) is the Black–Scholes pricing formula for put options.
8.3
PRICING BIVARIATE OPTIONS IN INCOMPLETE
MARKETS
We begin by recalling the terms of the incomplete market problem. In this setting, a general
contingent claim g(S, t), with pay-off G(S, T ), where S is a univariate variable, can be
priced computing
g (S, t) = B (t, T ) EQ

G (S, T ) ; Q ∈℘| ℑt

where EQ represents the expectation with respect to a risk-neutral measure Q. The set ℘
contains the risk-neutral measures and describes the information available on the underlying
asset. If it is very precise, and the set ℘contains a single probability measure, we are in the
standard complete market pricing setting tackled above. In the case in which we do not have
precise information – for example, because of limited liquidity of the underlying asset – we
have the problem of choosing a single probability measure, or some pricing strategy. So, in
order to price the contingent claim g in this incomplete market setting, we have to define:
(i) the set of probability measures ℘and (ii) a set of rules describing a strategy to select
the appropriate measure and price. One could resort to expected utility to give a preference
rank for the probabilities in the set, picking out the optimal one. As an alternative, or prior
to that, one could instead rely on some more conservative strategy, selecting a range of
prices: the bounds of this range would yield the highest and lowest price consistent with
the no-arbitrage assumption, and the replicating strategies corresponding to these bounds
are known as super-replicating portfolios. In this case we have
g−(S, t) = B inf EQ

G (S, T ) ; Q ∈℘

g+ (S, t) = B sup EQ

G (S, T ) ; Q ∈℘

As we have discussed in Chapter 1, the market incompleteness issue emerges as a problem
that is very involved even at the one-dimension level. We have seen that the solution can
also involve non-additive pricing kernels, technically known as capacities (more precisely,
the subset of convex capacities). The copula pricing result which, as we saw, is fairly
straightforward in a complete market setting, has to be derived carefully in a setting in
which even at the univariate level the pricing kernel may not be represented by probability
measures. Following Cherubini and Luciano (2002a), we are going to show that the same
results that were obtained for a complete market setting carry over easily to the case in
which the market is incomplete, both at the univariate and multivariate levels. Moreover,
deriving the pricing kernel result without reference to probability arguments will help to
highlight the arbitrage arguments.

240
Copula Methods in Finance
8.3.1
Fr´echet pricing: super-replication in two dimensions
We are now going to discuss how the same approach can be generalized to the bivariate
pricing problem. As we did in the complete market setting, we start with the bivariate digital
products. This time, however, we are going to drop any reference to Sklar’s theorem as well
as to any other probability theory argument. Our only guideline will be to check that the
pricing relationships rule out arbitrage opportunities. We now focus our discussion on the
properties that are to be imposed on the pricing kernel to achieve this task.
In financial terms, modeling the pricing kernel means recovering the forward value of a
digital option, i.e. an option that pays one unit of value if some event occurs. Likewise, in
our bivariate setting, recovering the pricing kernel amounts to pricing a digital option that
pays one unit if two events take place. So, our problem is to find a replicating strategy for
the bivariate digital option. An interesting question is whether it is possible to use univariate
digital options to hedge the bivariate one.
In order to focus on the bivariate feature of the pricing problem, we assume that we may
replicate and price two univariate digital options with the same exercise date T written on
the underlying markets S1 and S2 for strikes K1 and K2 respectively. Our problem is then
to use these products to replicate a bivariate option which pays one unit if S1 > K1 and
S2 > K2 and zero otherwise.
As a starting point, it is quite natural to break the sample space into the four relevant
regions and to construct a map that could facilitate the proofs of some static arbitrage
relationship (Table 8.1).
So, a bivariate call digital option pays one unit only if both of the assets are in state H,
that is, in the upper left cell of the table. The single digital options written on assets 1 and
2 pay in the first row and the first column respectively. In Table 8.2 below we sum up the
pay-offs of these different assets and determine which prices are observed in the market.
We recall that DC1, DC2 and B (t, T ) denote the prices of the univariate digital options
and the risk-free asset respectively.
Our problem is to use no-arbitrage arguments to recover information on the price of the
bivariate digital option. In particular, we may begin to investigate the pricing bounds for
the bivariate digital, that is its super-replication portfolio. To this aim, some interesting
Table 8.1
Breaking down the sample space for the digital
option
State H
State L
State H
S1 ⩾K1, S2 ⩾K2
S1 ⩾K1, S2 < K2
State L
S1 < K1, S2 ⩾K2
S1 < K1, S2 < K2
Table 8.2
Prices and pay-offs for digital options
Price
HH
HL
LH
LL
Digital option asset 1
DC1
1
1
0
0
Digital option asset 2
DC2
1
0
1
0
Risk-free asset
B (t, T )
1
1
1
1
Bivariate digital option
?
1
0
0
0

Option Pricing with Copulas
241
no-arbitrage implications can easily be obtained by comparing its pay-off with that of
portfolios of the univariate digital options and the risk-free asset. The following proposition
states such bounds for the price.
Proposition 8.1
The no-arbitrage price DHH(K1, K2) of a bivariate digital option is bound-
ed by the inequality
max(DC1 + DC2 −B (t, T ) , 0) ⩽DHH(K1, K2) ⩽min(DC1, DC2)
Proof :
Assume first that the right hand side of the inequality is violated. Say that,
without loss of generality, it is DHH(K1, K2) > DC1; in this case selling the bivariate
digital option and buying the single digital option would allow a free lunch in the state
[S1 > K1, S2 ⩽K2]. As for the left hand side of the inequality, it is straightforward to see
that D must be non-negative. There is also a bound DC1 + DC2 −B (t, T ). Assume in
fact that DC1 + DC2 −B (t, T ) > DHH(K1, K2); in this case buying the bivariate digital
option and a risk-free asset and selling the two univariate digital options would allow a free
lunch in the current date with non-negative pay-off in the future (actually, the pay-off could
even be positive if state [S1 ⩽K1, S2 ⩽K2] occurred).
□
The proposition exploits a static super-replication strategy for the bivariate digital option:
the lower and upper bounds have a direct financial meaning, as they describe the pricing
bounds for long and short positions in the bivariate options. The result may sound even
more suggestive if we use forward prices. As we know, the forward prices are defined as
DHH(K1, K2)/B (t, T ), DC1/B (t, T ) and DC2/B (t, T ) for the double and single digital
options respectively. We have then
max
 DC1
B (t, T ) +
DC2
B (t, T ) −1, 0

⩽DHH(K1, K2)
B (t, T )
⩽min
 DC1
B (t, T ),
DC2
B (t, T )

and it is easy to recognize that the two bounds constraining the forward price of the double
digital option are the Fr´echet bounds taking the forward prices of the single digital options
as arguments. Let us observe and stress that these bounds emerged from no-arbitrage consid-
erations only. Furthermore, it must be recalled that the Fr´echet bounds fulfill the conditions
defining copula functions, suggesting that this arbitrage-based result could hide a more
general finding that is going to be proved in the following section.
8.3.2
Copula pricing kernel
We now take one step further and investigate the features of the no-arbitrage forward price
of the bivariate digital option. From our previous findings of Fr´echet-like pricing bounds,
we are naturally led to conjecture that such a bivariate kernel is a copula function, i.e. a
function of the kind
DHH(K1, K2)/B (t, T ) = C(DC1/B (t, T ) , DC2/B (t, T ))
The following proposition proves that this conjecture is true.

242
Copula Methods in Finance
Proposition 8.2
The bivariate pricing kernel is a function CHH(v, z) taking the univariate
pricing kernels as arguments. In order to rule out arbitrage opportunities the function must
fulfill the following requirements:
• it is defined in I 2 = [0, 1] × [0, 1] and takes values in I = [0, 1]
• for every v and z of I 2, CHH(v, 0) = 0 = C(0, z), CHH(v, 1) = v, CHH(1, z) = z
• for every rectangle [v1, v2] × [z1, z2] in I 2, with v1 ⩽v2 and z1 ⩽z2
CHH(v2, z2) −CHH(v2, z1) −CHH(v1, z2) + CHH(v1, z1) ⩾0
Proof :
The first condition is trivial: the prices of the digital options cannot be higher
than the risk-free asset B, implying that the forward prices of both the univariate and
bivariate digital are bounded in the unit interval. The second condition follows directly
from the no-arbitrage inequality in Proposition 8.2, by substituting the values 0 and 1 for
v = DC1/B (t, T ) or z = DC2/B (t, T ). As for the last requirement, consider taking two
different strike prices K11 > K12 for the first security, and K21 > K22 for the second. Denote
with v1 the forward price of the first digital corresponding to the strike K11 – with v2 that
of the first digital for the strike K12 – and use an analogous notation for the second security.
Then, the third condition above can be rewritten as
DHH(K12, K22) −DHH(K12, K21) −DHH(K11, K22) + DHH(K11, K21) ⩾0
As such, it implies that a spread position in bivariate options paying one unit if the two
underlying assets end in the region [K12, K11] × [K22, K21] cannot have negative value.
□
To sum up our results, we may match the two propositions above with the mathematical
definitions given in Chapter 2, so giving a characterization of the requirements that have to
be imposed on the bivariate pricing kernel in order to rule out arbitrage opportunities.
Proposition 8.3
The arbitrage-free pricing kernel of a bivariate contingent claim is a cop-
ula function taking the univariate pricing kernels as arguments
DHH(K1, K2)
B(t, T )
= CHH
DC1(K1)
B(t, T ) , DC2(K2)
B(t, T )

and the corresponding super-replication strategies are represented by the Fr´echet bounds:
max
DC1(K1)
B (t, T ) + DC2(K2)
B (t, T ) −1, 0

⩽CHH
DC1(K1)
B (t, T ) , DC2(K2)
B (t, T )

⩽min
DC1(K1)
B (t, T ) , DC2(K2)
B (t, T )

It must be stressed again that in order to prove the result we did not rely on any assumption
concerning the probabilistic nature of the arguments of the pricing function: these are only
required to be no-arbitrage prices of single digital options. In this respect, our results carry
over to the more general incomplete market pricing models based on the use of convex
capacities, that we discussed above.

Option Pricing with Copulas
243
It is worth while noticing how the market incompleteness question is complicated in a
bivariate setting, and in a multivariate setting in general. We may say that we have a market
incompleteness problem in one dimension, which has to do with the issues discussed above
and may lead to pricing bounds for the digital options. So, we may have, for example,
B (t, T ) Q−
i (Ki | ℑt) ⩽DCi (Ki) ⩽B (t, T ) Q+
i (Ki | ℑt)
for i = 1, 2. There is then a second dimension of the market incompleteness problem for
bivariate and, in general, multivariate claims, beyond that of the univariate problem. The
problem of selecting prices for the univariate products is compounded by the choice of
copula function, which has to do with the dependence structure of the underlying assets.
At this level, the Fr´echet bounds represent the natural choice if the conservative pricing
strategy is selected. In this case we have
B[max(Q−
1 + Q−
2 −1, 0)] ⩽DHH(K1, K2) ⩽B min(Q+
1 , Q+
2 )
where, for the sake of simplicity, we omitted the arguments of the probability bounds.
8.4
PRICING VULNERABLE OPTIONS
The massive growth of the structured finance, and the increasing practice of financial insti-
tutions to resort to the OTC market to hedge the derivatives exposures incurred to supply
these products, has made counterparty risk in derivatives a major reason of concern. When
a derivative contract is negotiated in the OTC market, one has to account for the possibility
that the counterparty could go bust during the life of the contract. This poses a problem
both to the risk management of the position and the pricing of the contract. As for risk
management, the institution has to take into account that some capital must be allocated to
hedge the risk connected to default of the counterparties. As for pricing, the evaluation of
each derivative contract has to take into account the credit standing of the counterparty, as
well as the dependence between its default and the dynamics of the underlying asset.
Copula functions are particularly well suited to address the pricing and hedging problem
of vulnerable derivatives – that is, contracts in which the counterparty may not be able
to make good its obligation. In fact, evaluating vulnerable derivatives is an intrinsically
bivariate problem, as the pay-off is conditional on two events: the first is that the derivative
ends up in the money, the second is survival of the counterparty, as well as dependence
between its default and the dynamics of the underlying asset. The approach proposed in
Cherubini and Luciano (2002b), which we follow here, exploits copula functions to yield
a flexible framework, extending and encompassing the specific models proposed in the
literature. Well-known models such as Johnson and Stulz (1987), Hull and White (1995)
and Klein (1996), for example, are built under the assumption of the log-normal distribution
of the underlying asset and a structural model for the credit risk of the counterparty. Other
papers, such as Jarrow and Turnbull (1995) and Barone, Barone-Adesi and Castagna (1998),
deal with counterparty risk in bond options applying different term structure models, and
both prefer a reduced form specification for counterparty risk. We are going to show that
copula functions enable us to choose the most suitable specification for both market and
counterparty risk, as well as a flexible representation of the dependence structure between
the two risks.

244
Copula Methods in Finance
8.4.1
Vulnerable digital options
We start our analysis from the simplest products, that is digital options. This will both
make the building blocks of the application clearer and open the way to more complex
applications, that will follow. We remind the reader that from the previous section we
denote as DCi(Ki) the default-free price of a call digital option, i.e. a contract paying one
unit if and only if at the exercise date T we observe Si ⩾Ki for a given strike Ki. Assume
now that a digital option is written by a counterparty A, which is subject to default risk: the
option will pay one unit under the joint event of the option ending in the money and survival
of the counterparty A; it will be worth RA, the recovery rate for maturity T , if it expires in
the money and counterparty A defaults; it will be worth zero otherwise. We will denote this
option as V-DCi(Ki). Our task is to characterize the arbitrage-free value of such an option.
We assume we are able to observe or estimate the value of a defaultable zero-coupon bond
issued by counterparty A, or by some issuer of the same risk class, for the same maturity
T. We denote its market value by PA (t, T ). The value of the default-free zero-coupon bond
for the same maturity is denoted by B (t, T ), as above. We also define some quantities that
are often used by practitioners to assess the credit risk of a debt issue, and that will be
useful in this analysis. In particular, we define DelA the discounted expected loss on the
zero-coupon issued by A for maturity T , computed as DelA = B (t, T ) −PA (t, T ) , and
the corresponding expected loss ElA = DelA/B (t, T ). We may also define the loss given
default figure LgdA = 1 −RA: throughout the analysis, we will assume that this figure is
non-stochastic (or independent of the events of exercise of the option and default of the
counterparty).
To recover the price of the vulnerable option we first partition the sample space at the
expiration time T into the states shown in Table 8.3, and we may write down the pay-off
matrix (Table 8.4) for all the products defined above.
Notice that the framework of the analysis is similar to that used in the previous section to
price bivariate digital options. In order to apply that analysis, we can easily pivot the pay-off
matrix in the following way. Let us build the following two portfolios: the first consists in
a long and a short position in 1/(1 −RA) units of the default-free and defaultable bond
respectively; the second is made up by a long and a short position in 1/(1 −RA) units
Table 8.3
Breaking down the sample space for the vulnerable dig-
ital option
State H
State L
State H
Si ⩾Ki and A survives
Si ⩾Ki and A defaults
State L
Si < Ki and A survives
Si < Ki and A defaults
Table 8.4
Prices and pay-offs for bonds and digital options
Price
HH
HL
LH
LL
Defaultable bond company A
PA (t, T )
1
RA
1
RA
Risk-free asset
B (t, T )
1
1
1
1
Univariate digital option
DCi(Ki)
1
1
0
0
Vulnerable digital option
V-DCi(Ki)
1
RA
0
0

Option Pricing with Copulas
245
Table 8.5
Prices and pay-offs for portfolios of assets in Table 8.4
Price
HH
HL
LH
LL
[B(t, T ) −PA(t, T )]/(1 −RA)
0
1
0
1
B (t, T )
1
1
1
1
DCi(Si ⩾Ki)
1
1
0
0
[DVi(Ki) −V-Di(Ki)]/(1 −RA)
0
1
0
0
of the default-free and vulnerable digital option. Including these portfolios in the pay-off
matrix we get the values shown in Table 8.5.
The pricing problem is now exactly the same as that of a bivariate digital option, and
we can apply the results in the propositions above. The arbitrage-free price of the second
portfolio described above (long the default-free option and short the vulnerable one) has
to be equal to the discounted value of a copula function taking the forward values of
the default-free digital option and the first portfolio as arguments. Rearranging terms, it is
straightforward to show
Corollary 8.1
The price of a vulnerable call digital option, V-DCi, is given by
V-DCi(Ki) = DCi(Ki) −B (t, T ) (1 −RA)CHL
DCi(Ki)
B (t, T ) , B (t, T ) −PA (t, T )
B (t, T ) (1 −RA)

where CHL (x, y) is a copula function.
The corollary allows us to split the vulnerable digital price into the non-vulnerable digital
price, Di(Ki), minus counterparty risk:
B(t, T )(1 −RA)CHL
DCi(Ki)
B(t, T ) , B(t, T ) −PA(t, T )
B(t, T )(1 −RA)

= B(t, T )LgdA
× CHL
DCi(Ki)
B(t, T ) , ElA
LgdA

Denoting by QA (T | ℑt) the default probability of counterparty A by time T , conditional
on the information available at time t, we have that ElA = LgdA ∗QA (T | ℑt). The price
of the vulnerable call option can then be written
V-DCi(Ki) = DCi(Ki) −B(t, T )LgdACHL(Qi(Ki), QA(T ) | ℑt)
and it is clear why the price involves a copula function, taking the risk-neutral probability
of exercise of the option and the risk-neutral probability of default of the counterparty as
arguments.
By the same argument, the price of a defaultable digital put option can be priced as
V-DPi(Ki) = DPi(Ki) −B(t, T )LgdACLL(Qi(Ki), QA(T ) | ℑt)

246
Copula Methods in Finance
Notice that using the relationship between copulas
CLL(Qi(Ki), QA(T )) = QA(T | ℑt) −CHL(Qi(Ki), QA(T ) | ℑt)
we may rewrite
V-DPi(Ki) = DPi(Ki) −B (t, T ) LgdACLL (Qi (Ki) , QA (T ) | ℑt)
= DPi(Ki) −B (t, T ) LgdA

QA (T | ℑt) −CHL(Qi (Ki) , QA (T ) | ℑt)

= B (t, T ) −DCi(Ki) + CHL(Qi (Ki) , QA (T ) | ℑt)
−B (t, T ) LgdAQA (T | ℑt)
= B (t, T ) −V-DCi(Ki) −B (t, T ) LgdAQA (T | ℑt)
= B (t, T )

1 −LgdAQA (T | ℑt)

−V-DCi(Ki)
= PA (t, T ) −V-DCi(Ki)
where we have used DCi(Ki) + DPi(Ki) = B (t, T ). In this way we recovered an obvious
put–call parity relationship between vulnerable digital options. Buying a digital call and a
digital put from the same counterparty amounts to buying a defaultable zero-coupon bond
issued by the counterparty:
DCi(Ki) + DPi(Ki) = PA (t, T )
8.4.2
Pricing vulnerable call options
We now use the results obtained above for digital options to evaluate counterparty risk in a
typical derivative contract such as a European option. As suggested above, we resort to the
Breeden and Litzenberger (1978) idea of considering an option as an integral sum of digital
contracts. We recall that according to their approach, the value at time t of a default-free
call option written on Si with time to expiration T and strike K may be written as
CALL(Si, t : K, T ) =
 ∞
K
DCi(u) du = B (t, T )
 ∞
K
Qi(u) du
This representation can be easily extended to the vulnerable case, and it is natural to use the
results obtained in the previous section, concerning the vulnerable pricing kernel, to recover
V-CALL(Si, t : K, T ) =
 ∞
K
V-DCi(u) du
=
 ∞
K

DCi (u) −B (t, T ) LgdACHL
DCi (u)
B
, ElA
LgdA

du
where V-CALL denotes the vulnerable call option. Using the no-arbitrage pricing relation-
ship Di (u) = B (t, T ) Q(u), it is now straightforward to obtain the following:

Option Pricing with Copulas
247
Proposition 8.4
The no-arbitrage price of a vulnerable call option is given by
V-CALL(Si, t : K, T ) = CALL(Si, t : K, T )−B (t, T ) LgdA
 ∞
K
CHL

Qi(u), ElA
LgdA

du
where CHL(x, y) is a copula function.
So, computing counterparty risk, which is now
B (t, T ) LgdA
 ∞
K
CHL

Qi(u), ElA
LgdA

du
requires to evaluate an integral of the copula function, with respect to the first argument,
that is the pricing kernel. This integral is not generally available in closed form. Three
interesting cases, however, represent notable exceptions, as we show below.
• The case of independence between the underlying asset and default of the counterparty
is computed directly using the product copula, which enables us to exploit factorization
of the terms in the integral to yield
V-CALL (Si, t; K, T ) = CALL (Si, t; K, T ) (1 −ElA)
Notice that in the case of independence the loss given default figure is dropped from the
formula, and all we need is the aggregate expected loss figure, which is typically provided
by the rating agencies.
• The second relevant case is perfect positive dependence. It is noticeable to observe that
even in this instance we may recover a closed form solution, whenever a closed form
solution exists for the corresponding default-free option price
V-CALL (Si, t; K, T ) = CALL (Si, t; K, T ) −max

K∗−K, 0
	
× DelA −LgdACALL

Si, t; max

K, K∗	
, T
	
where K∗= Qi
−1 (ElA/LgdA), that is the strike of a call option whose exercise prob-
ability is equal to the default probability of the counterparty.1 For practical purposes,
it is useful to notice that K∗corresponds to a far out-of-the-money option: as a result,
the value of the corresponding default-free option is usually very close to zero. Since in
1 It may be worthwhile to discuss how this formula is recovered. When K < K∗the problem is to compute
BLgdA
 ∞
K
min

Q(η), ElA
LgdA

dη = BLgdA

 K∗
K
ElA
LgdA
dη +
 ∞
K∗Q(η) dη

= (K∗−K)DelA + LgdAC(Si, t; K∗, T )
where the last equality uses the definition of discounted expected loss and the integral representation for the call
option discussed above. Consideration of the case K∗< K is trivial, and immediately leads to the formula in
the text.

248
Copula Methods in Finance
most applications we have K∗⩾K, counterparty risk in the case of perfect dependence
will be effectively approximated by the quantity (K∗−K)DelA, which is very easy to
compute. If K∗< K the value of the vulnerable option is simply RAC (Si, t; K, T ) and
credit risk tends to zero with the option value.
• The case of perfect negative dependence may also be easily computed using the same
strategy to get
V-CALL (Si, t; K, T ) = (1 −LgdA) CALL (Si, t; K, T )
+ LgdACALL

Si, t; max

K, K∗∗	
, T
	
−max

K∗∗−K, 0
	
(B (t, T ) LgdA −DelA)
with K∗∗= Q
−1
i
(1 −(ElA/LgdA)), that is the strike of a very deep-in-the-money option,
whose exercise probability is equal to the survival probability of the counterparty. It is
straightforward to check that if (as in most practical applications) K∗∗⩽K, the value
of the vulnerable option is the same as that of the corresponding default-free contract. In
the case K < K∗∗counterparty risk is instead evaluated as
LgdA

CALL (Si, t; K, T ) −CALL

Si, t; K∗∗, T
	
+

K∗∗−K
	 
B (t, T ) −DelA
LgdA

The formulas above provide very straightforward hedging strategies for the counterparty risk
in a vulnerable call option. In the case of perfect positive dependence, the hedging strategy
would call for being long max (K∗−K, 0) of a default put and LgdA of a call with strike
max (K∗, K). Since usually, as we argued above, the value of this option is very close to
zero, the credit derivative is a sufficient hedge. Correspondingly, under perfect negative
dependence and with K < K∗∗the hedge consists of being long LgdA call spreads written
on strikes K and K∗∗, long (K∗∗−K) RA of the riskless bonds and short (K∗∗−K) of
PA. These hedging strategies refer to extreme dependence cases, and represent the super-
replication strategies corresponding to the Fr´echet bounds discussed above.
8.4.3
Pricing vulnerable put options
The same approach can be applied to evaluate vulnerable put options. In this case, the
starting point is given by the representation
V-PUT(Si, t : K, T ) =
 K
0
V-DPi(u) du
=
 K
0

DPi (u) −B (t, T ) LgdACLL
DPi (u)
B (t, T ), ElA
LgdA

du
= PUT(Si, t : K, T ) −B (t, T )
 K
0
LgdACLL

Qi(u), ElA
LgdA

du
(8.1)

Option Pricing with Copulas
249
where V-PUT denotes the vulnerable put price, and the second addendum in (8.1) represents
counterparty risk. Using the same strategy as before we can compute the value of the option
in closed form for the three benchmark cases. Namely, we get
V-PUT (Si, t; K, T ) = PUT (Si, t; K, T ) (1 −ElA)
for the independence case,
V-PUT (Si, t; K, T ) = PUT (Si, t; K, T ) −max

K −K∗∗, 0
	
× DelA −LgdAPUT(Si, t; min

K∗∗, K
	
, T )
for perfect positive dependence, and finally
V-PUT (Si, t; K, T ) = (1 −LgdA) PUT (Si, t; K, T )
+ LgdAPUT

Si, t; min

K, K∗	
, T
	
−max

K −K∗, 0
	
(BLgdA −DelA)
for perfect negative correlation. Notice that the values K∗and K∗∗are the same as in the
call option case above.
As for the case of vulnerable digital options, we can use the no-arbitrage relationship
derived for digital call and put options to write
CLL

Q(u), ElA
LgdA

= ElA
LgdA
−CHL

Q(u), ElA
LgdA

and to recover a relationship between the price of vulnerable call and put options as in the
following.
Proposition 8.5 [Vulnerable put–call parity]
In order to rule out arbitrage opportunities,
the relationship between vulnerable call and put options must be
V-PUT(Si, t : K, T ) + Si(t) = V-CALL(Si, t : K, T ) + KPA (t, T )
+ B (t, T ) LgdA
 ∞
0
CHL

Q(u), ElA
LgdA

du
Proof :
V-PUT(Si, t : K, T ) + Si(t) = PUT(Si, t : K, T )
+ Si(t) −B (t, T ) LgdA
 K
0
CLL

Q(u), ElA
LgdA

du
= CALL(Si, t : K, T ) + KB (t, T )
−B (t, T ) LgdA
 K
0
 ElA
LgdA
−CHL

Q(u), ElA
LgdA

du

250
Copula Methods in Finance
= CALL(Si, t : K, T ) + K(B (t, T ) −DelA)
+ B (t, T ) LgdA
 K
0
CHL

Q(u), ElA
LgdA

du
= V-CALL(Si, t : K, T ) + KPA (t, T )
+ B (t, T ) LgdA
 ∞
0
CHL

Q(u), ElA
LgdA

du
□
8.4.4
Pricing vulnerable options in practice
We now report some concrete examples of copula pricing applications to vulnerable options.
Let us first notice that the approach guarantees the maximum flexibility concerning the
choice of: (i) the option pricing model; (ii) the credit evaluation approach; and (iii) the
dependence structure. As for the first choice, we stick here to the standard Black–Scholes
for a matter of illustration of the approach. The credit assessment choice is, of course,
crucial: one can choose either a structural approach based on the stock market value and
volatility of the counterparty or a reduced form based on corporate bonds or credit derivatives
information. Having firm specific information is obviously preferable if one wants to have
some idea on the dependence between default risk of the counterparty and dynamics of
the underlying asset of the vulnerable contract. If such information is not available, one
could rely on figures from the rating agencies and assume some scenario concerning the
dependence structure. Finally, a good choice to gauge the relevance of the dependence
structure for counterparty risk is to resort to the Fr´echet family of copulas. As these copulas
are obtained as linear combinations of the perfect positive and negative dependence and the
product one, it follows that they can be priced in closed form using the formulas derived in
the paragraph above for each of these cases. In particular, it is very useful to use mixture
copulas based on the perfect dependence and the independence cases.
The effect of counterparty risk on the prices of options
In Figure 8.1 we report the counterparty risk figure in a one-year digital option for a Baa3
rated counterparty, as a function of the Kendall’s tau statistic. Use is made of the mixture
copula described above. The relationship is reported for different levels of the probability
of exercise, i.e. for different levels of moneyness. Based on Moody’s data, the issuer has
expected loss (ElA) equal to 0.231% and a recovery rate (RA) of 55%. For the sake of
simplicity, we select a 20% constant value of volatility of the underlying asset and zero
risk-free rate. It may be checked that the relationship between counterparty risk and the
dependence statistics is increasing.
The prices of vulnerable call options are obtained by integration of the pricing kernel
depicted above, and vulnerable put options are recovered by arbitrage. Figures 8.2 and 8.3
present the counterparty risk in vulnerable call and put options respectively. The current
price of the underlying asset is assumed to be equal to 1 and the relationship is reported for
levels of the strike ranging from 0.6 through 1.4. As before, we assume a time of one year
to expiration, a 20% constant volatility and zero risk-free rate. As for the counterparty, we

Option Pricing with Copulas
251
0
0.0005
0.001
0.0015
0.002
0.0025
−1
−0.8
−0.6
−0.4
−0.2
0
0.2
0.4
0.6
0.8
1
Moneyness = 1
Moneyness = 1.2
Moneyness = 15
Moneyness = 100
Moneyness = 0.5
Moneyness = 0.2
Figure 8.1
Counterpart risk in digital options
Vulnerable Call Options-Mixture Copulas
0
0.0005
0.001
0.0015
0.002
0.0025
0.003
−1
−0.8
−0.6
−0.4
−0.2
0
0.2
0.4
0.6
0.8
1
Kendall's Tau
K = 0.6
K = 0.8
K = 1
K = 1.2
K = 1.4
Figure 8.2
Counterpart risk in call options
consider an expected loss figure of 0.231%, corresponding to a Baa3 writer of the option. As
a consequence, the values K∗and K∗∗used to represent positive and negative dependence
turned out to be 1.727 and 0.556 respectively.
As for call options, the schedules of the relationship are shifted upwards as the strike price
decreases. Concerning the amounts involved, we reckon that, for any billion of underlying

252
Copula Methods in Finance
Counterpart Risk for Put Options-Mixture Copulas
0
0.0005
0.001
0.0015
0.002
0.0025
−1
−0.8
−0.6
−0.4
−0.2
0
0.2
0.4
0.6
0.8
1
Kendall's Tau
K = 0.6
K = 0.8
K = 1
K = 1.2
K = 1.4
Figure 8.3
Counterpart risk in put options
Table 8.6
Counterpart risk as a percentage of the value of option
Kendall τ
AAA
Aaa3
A3
Baa3
Ba3
B3
Caa3
1
0.00117%
0.02700%
0.27620%
2.24963%
10.88450%
30.93574%
59.66535%
0.75
0.00094%
0.02200%
0.22594%
1.85151%
9.04262%
26.09492%
53.42897%
0.50
0.00069%
0.01639%
0.16946%
1.40410%
6.97275%
20.65490%
46.42065%
0.25
0.00040%
0.00984%
0.10365%
0.88277%
4.56084%
14.31590%
38.25417%
0
0.00003%
0.00166%
0.02137%
0.23100%
1.54550%
6.39100%
28.04461%
−0.25
0.00002%
0.00112%
0.01447%
0.15642%
1.04650%
4.32750%
18.98969%
−0.50
0.00001%
0.00070%
0.00895%
0.09676%
0.64735%
2.67694%
11.74680%
−0.75
0.00001%
0.00033%
0.00421%
0.04556%
0.30481%
1.26046%
5.53108%
−1
0.00000%
0.00000%
0.00000%
0.00000%
0.00000%
0.00000%
0.00000%
assets, in the case of independence counterparty risk is worth 924 603, 184 005 and 10 396 for
deep-in-the-money (K = 0.6), at-the-money and far-out-of-the-money (K = 1.4) contracts.
The figures increase with dependence up to 2 715 961, 1 791 961 and 867 961 respectively;
counterparty risk tends to zero with perfect negative dependence, since the strike is higher
than the upper level K∗= 1.727.
Finally, to have an idea concerning the effect of dependence for different rating classes
of the counterparty we report, in Table 8.6, the value of counterparty risk as a percentage
of the value of the corresponding default-free call option. The option is assumed to be
at-the-money, with one year to the exercise date and a volatility parameter of 20%.

Option Pricing with Copulas
253
Hedging counterparty risk in options
Notice that in the analysis above for the particular cases of independence and perfect
dependence the evaluation of vulnerable options only calls for knowledge of the pricing
formulas for the corresponding default-free products. More precisely, in the case of perfect
dependence, counterparty risk is represented by a short position in the spread B(t, T ) −
PA(t, T ) = Del, that can be traded in the market using a credit derivative contract, i.e. a
default put option, and a short position in a default-free option. The same structure applies
for put options. On the other hand, in the case of independence we have that the amount
of the position in the spread turns out to be equal to the CALL(.)/B(t, T ), i.e. the forward
value of the default-free call option. This suggests very straightforward hedging strategies
for extreme dependence scenarios, that is the super-hedging strategies. The hedging strategy
in the independence case is immediate. Instead, under the worst case scenario of perfect
dependence, the counterparty risk of a call option can be hedged by entering a long posi-
tion in default put options for an amount equal to max (K∗−K, 0) and by buying Lgd
call options with strike K∗. By the same token, the super-hedging strategy for put options
involves long positions in max (K −K∗∗, 0) default put options and Lgd put options with
strike K∗∗.
To make a concrete example, consider a 1 million euro position in one of the call options
studied above. Say it is at-the-money, exercised in one year, and is issued by a Baa3
counterparty. We recall that the one-year default probability is 0.231% and the recovery rate
is 55%. Furthermore, the value K∗was found equal to 1.727. For the sake of simplicity, we
assume the risk-free rate to be equal to zero. The perfect positive dependence super-hedge
consists of
• buying protection for a 727 000 nominal exposure to the counterparty for an up-front
payment equal to 755.72 euros;
• buying 450 000 default-free call options with strike equal to 1.727 against an up-front
payment of 122.80 euros.
The total cost of the hedge is then 878.52 out of a default-free value of the option position
of 79 655.79.
The independence super-hedge requires instead buying protection for a nominal value of
79 655.79 for a cost of 82.80 euros. Taking linear combinations of the extreme cases enables
us to account for imperfect positive dependence. For example, corresponding to a Spearman
ρS figure equal to 50%, the cost of the hedge is (0.5 × 878.52) + (0.5 × 82.80) = 480.66.
8.5
PRICING RAINBOW TWO-COLOR OPTIONS
Rainbow options are multivariate contingent claims whose underlying asset is the maximum
or minimum in a set of assets. So, the typical pay-off for a bivariate, or two-color, rainbow
option is
G(S1(T ), S2(T ), T ) = max [min(S1(T ), S2(T )) −K, 0]
which is the call option on the minimum between two assets, or
G(S1(T ), S2(T ), T ) = max [K −max(S1(T ), S2(T )), 0]

254
Copula Methods in Finance
that is, the put option on the maximum between two assets. Once these options are priced, the
evaluation of other similar products, such as call options on the maximum and put options
on the minimum of two assets, can be recovered by arbitrage, as pointed out by Stulz (1982).
His paper also provided closed form solutions for these options in a Black–Scholes world.
We will see here that the use of copula functions enables us to extend these results quite
naturally to a more general setting. In fact, we are going to show that the price of the two
options described above has a straightforward interpretation in terms of copula functions,
and that these representations easily lead to analytical super-replication hedges.
8.5.1
Call option on the minimum of two assets
The basic argument that allows us to write down, in terms of copulas, the price of a call
option on the minimum of two underlying assets is quite easy to understand by exploiting
the analogy with the univariate plain vanilla option. We know that, in that case,
CALL (Z, t; K, T ) = B (t, T )
 ∞
K
QZ(u | ℑt) du
Applying the probability distribution technique described above, with Z = f (S1, S2) =
min(S1, S2) we may write
CALL (S1, S2, t; K, T ) = B (t, T )
 ∞
K
Pr(min (S1 (T ) , S2 (T )) > u | ℑt) du
where probability is computed under the risk-neutral measure. So, the relevant pricing kernel
is that of the minimum of the two risky assets S1 and S2. Consider their joint survival
probability, for any threshold u: Pr (S1 (T ) > u, S2 (T ) > u | ℑt) . Obviously, stating that,
at time T , both of the prices will be higher than u is equivalent to saying that the lower of
the two will be above that threshold. So, the price of the option becomes
CALL (S1, S2, t; K, T ) = B (t, T )
 ∞
K
Pr(S1 (T ) > u, S2 (T ) > u | ℑt) du
= B (t, T )
 ∞
K
Q (u, u | ℑt) du
It is now easy to check that the copula function approach can be particularly useful to give
a flexible representation of this kind of product. In fact, using the general result discussed
above for bivariate digital options
DHH (u, u) = B (t, T ) Q (u, u | ℑt)
= B (t, T ) CHH(Q1 (u) , Q2 (u) | ℑt)
we may write
CALL (S1, S2, t; K, T ) = B (t, T )
 ∞
K
CHH(Q1 (u) , Q2 (u) | ℑt) du

Option Pricing with Copulas
255
In this way, we are able to separate the marginal distributions, and thus the marginal
pricing kernels, from the dependence structure, which is represented by the copula function
CHH.
Using the copula function representation we may also check how the problem of market
incompleteness is compounded in a multidimensional setting. First, the market for each
underlying asset may have incompleteness problems. In this case we would have
CALL (S1, S2, t; K, T ) = B (t, T )
 ∞
K
CHH(Q−
1 (u) , Q−
2 (u) | ℑt) du
Second, even if the market for each underlying asset is complete, so that the marginal
distributions are uniquely determined, it may be the case that the dependence structure cannot
be precisely identified. In other words, it may happen (and it happens often) that the joint
pricing kernel cannot be uniquely determined. We know that if the marginal pricing kernels
are continuous, each candidate joint pricing kernel can be associated to a specific copula
function. So, solving the pricing problem in an incomplete market amounts to selecting a
specific copula function. As in the univariate approach, one could then select one specific
copula, following some strategy of choice. Alternatively, or prior to that, one could follow a
conservative approach, and evaluate pricing bounds, corresponding to extreme dependence
assumptions, and the corresponding copula functions. As we are going to show, by using
Fr´echet copulas it is also easy to design super-replication portfolios corresponding to these
conservative scenarios.
Dependence structure and super-replicating portfolios
We now try to recover the pricing bounds of the call option on the minimum between two
underlying assets. In order to focus the analysis on the dependence structure issue, we may
assume that the markets of each of the underlying assets are complete, so that the marginal
pricing kernels are uniquely identified. Then, the only source of market incompleteness has
to do with the dependence structure between the two assets. We may then apply the Fr´echet
bounds for copulas
max(Q1 (u) + Q2 (u) −1, 0 | ℑt) ⩽CHH(Q1 (u) , Q2 (u) | ℑt)
⩽min(Q1 (u) , Q2 (u) | ℑt)
Substituting in the pricing formula above we obtain
CALL+ (S1, S2, t; K, T ) = B (t, T )
 ∞
K
min(Q1 (u) , Q2 (u) | ℑt) du
as the upper bound for the price, corresponding to perfect positive dependence of the under-
lying assets. We also obtain
CALL−(S1, S2, t; K, T ) = B (t, T )
 ∞
K
max(Q1 (u) + Q2 (u) −1, 0 | ℑt) du
as the lower price corresponding to perfect negative dependence.

256
Copula Methods in Finance
These pricing bounds are particularly useful because they can be computed analyti-
cally and can be expressed in terms of univariate call options. In such a way, they are
directly referred to specific super-replication strategies for the product. Let us start with
the upper bound CALL+. To compute the integral we first recover a strike price K∗such
that Q1 (K∗) = Q2 (K∗). Assume, without loss of generality, that for u < K∗we have
Q1 (u) < Q2 (u). Then we have two cases. If K ⩾K∗the joint pricing kernel will coincide
with the marginal pricing kernel Q2 (u), which will be lower than Q1 (u) for any u > K.
As a result, the price of the call option on the minimum will be the same as that of a
univariate plain vanilla call option written on S2. If instead we have K < K∗the integral
can be split in two yielding a call spread on asset S1 and a call option on S2 with a higher
strike. Analytically we have
CALL+ (S1, S2, t; K, T ) = 1{K∗⩾K}B (t, T )
 K∗
K
(Q1 (u) | ℑt) du
+ B (t, T )
 ∞
max[K,K∗]
(Q2 (u) | ℑt) du
where 1{K∗⩾K} is the indicator function assigning a value of 1 to the case K ⩾K∗. As for
the financial meaning of the formula, the first term is a call spread on asset S1 for strike
prices K and K∗; the second term is a call option on asset S2 for strike price equal to
max[K, K∗]. So, the super-replication portfolio for the call option on the maximum is
CALL+(S1, S2, t; K, T ) = 1{K∗⩾K}[CALL(S1, t; K, T ) −CALL(S1, t; K∗, T )]
+ CALL(S2, t; max[K, K∗], T )
Following the same strategy we can compute the lower bound of the price, and the
corresponding super-replication portfolio. In this case, we define a strike price K∗∗such
that Q1 (K∗∗) + Q2 (K∗∗) = 1. Of course, as both Q1 (u) and Q2 (u) are strictly decreasing,
we would have that Q1 (u) + Q2 (u) ⩽1 for any u ⩾K∗∗. So, remembering that the joint
pricing kernel is max[Q1 (u) + Q2 (u) −1, 0] it will be equal to zero for any such u ⩾K∗∗.
Now consider two cases. If it is K ⩾K∗∗the value of the option will be identically zero.
If instead we have K < K∗∗the integral can again be split in two yielding
CALL−(S1, S2, t; K, T ) = 1{K∗∗⩾K}B (t, T )

 K∗∗
K
(Q1 (u) | ℑt) du
+
 K∗∗
K
(Q2 (u) | ℑt) du −[K∗∗−K]

Notice that in this case we have two call spreads in the two assets S1 and S2, both with
strike prices K∗∗and K, plus a debt position for an amount equal to K∗∗−K. In other
words, we have
CALL−(S1, S2, t; K, T ) = 1{K∗∗⩾K}[CALL(S1, t; K, T ) −CALL(S1, t; K∗∗, T )
+ CALL(S2, t; K, T ) −CALL(S2, t; K∗∗, T )
−B(t, T )[K∗∗−K]]

Option Pricing with Copulas
257
For some pair of assets, the assumption that they can be negatively dependent may be an
implausible assumption. In this case it may be useful to limit the analysis to the positive
dependence orthant, so that the relevant lower bound will be the independence case. We
would have, in this case,
CALL⊥(S1, S2, t; K, T ) = B (t, T )
 ∞
K
(Q1 (u) Q2 (u) | ℑt) du
Unfortunately, however, the solution is not directly available in closed form, apart from
very special cases.
8.5.2
Call option on the maximum of two assets
The call option on the maximum of two assets can be recovered by arbitrage as suggested
in Stulz (1982). Define this call option by the pay-off
G (S1 (T ) , S2 (T ) , T ) = max [max (S1 (T ) , S2 (T )) −K, 0]
It is easy to see that this pay-off can be exactly replicated by
max [max (S1 (T ) , S2 (T )) −K, 0] = max [S1 (T ) −K, 0] + max [S2 (T ) −K, 0]
−max [min (S1 (T ) , S2 (T )) −K, 0]
In fact, if we have S1 (T ) > S2 (T ) > K the option is worth S1 (T ) −K, while in the
case S2 (T ) > S1 (T ) > K we get S2 (T ) −K. Checking equivalence of the pay-off in the
other cases is trivial.
In order to rule out arbitrage opportunities, we must then have
CALL (S1, S2, t; K, T ) = CALL (S1, t; K, T ) + CALL (S2, t; K, T )
−CALL (S1, S2, t; K, T )
Remark 8.1
Notice that the call option on the maximum of two assets can also be written
using the dual of the survival copula CHH. In fact, applying the definition given in Chapter 2
we have
CALL (S1, S2, t; K, T ) = B (t, T )
 ∞
K
(Q1 (u) | ℑt) du + B (t, T )
 ∞
K
(Q2 (u) | ℑt) du
−B (t, T )
 ∞
K
CHH(Q1 (u) , Q2 (u) | ℑt) du
= B (t, T )
 ∞
K
[(Q1 (u) | ℑt) + (Q2 (u) | ℑt)
−CHH(Q1 (u) , Q2 (u) | ℑt)] du
= B (t, T )
 ∞
K

CHH(Q1 (u) , Q2 (u) | ℑt) du

258
Copula Methods in Finance
Alternatively, it is easy to check that the price could also be written in terms of the
co-copula of copula CLL. In fact, as shown in Chapter 2, the dual of a survival copula CHH
generated by a copula CLL corresponds to the co-copula of the latter copula. This enables us
to use the discussion in Chapter 2 to spell the basic intuition behind this result. The pricing
kernel of the call option on the maximum of two assets is the risk-neutral probability that
either S1 or S2 at time T is greater than a threshold value u:
CALL (S1, S2, t; K, T ) = B (t, T )
 ∞
K
Pr(S1 (T ) or S2 (T ) > u, | ℑt) du
8.5.3
Put option on the maximum of two assets
We now approach the symmetric problem of two-color put options. In particular, symmetry
suggests to start from the put option written on the maximum of two assets, whose pay-off
is written as
G(S1(T ), S2(T ), T ) = max [K −max(S1(T ), S2(T ), 0]
Along the same lines followed for the case of the call option, we obtain
PUT (S1, S2, t; K, T ) = B (t, T )
 K
0
Pr(max (S1 (T ) , S2 (T )) ⩽u | ℑt) du
Again, saying that the maximum price of the underlying assets is lower than a given
threshold u is the same as stating that both the prices are below that threshold. Analytically,
we can write
Pr (max (S1 (T ) , S2 (T )) ⩽u | ℑt) = Pr (S1 (T ) ⩽u, S2 (T ) ⩽u | ℑt)
so that we have
PUT (S1, S2, t; K, T ) = B (t, T )
 K
0
Pr(S1 (T ) ⩽u, S2 (T ) ⩽u | ℑt) du
Going back again to the general results obtained for bivariate digital options
DLL (u, u) = B (t, T ) Q (u, u | ℑt)
= B (t, T ) CLL (Q1 (u) , Q2 (u) | ℑt)
we may write
PUT (S1, S2, t; K, T ) = B (t, T )
 K
0
CLL(Q1 (u) , Q2 (u) | ℑt) du
and the price of the put option is the integral of a copula function. We could obviously
apply the same techniques shown above to recover closed form solutions for the pricing
bounds of this rainbow put option and the corresponding super-replication portfolios. While
leaving this development to the readers, we want to focus attention on the fact that the

Option Pricing with Copulas
259
copula function in the put option formula is different from that appearing in the call price
representation. A closer inspection of the formula suggests, however, a precise relationship
between the two functions, which we are going to explore in more detail in the next section.
Rainbow put/call parity
Let us restate in financial terms the results recovered for rainbow options of the call and put
type. In sum, we applied to these options the same principle that Breeden and Litzenberger
(1978) suggested for univariate options. Call options on the minimum between two assets
can then be represented as the integral of bivariate digital call options, the integral being
computed from the strike K to infinity. Symmetrically, the price of a put option on the
maximum of two assets is the integral of bivariate digital put options, the integral running
from zero to the strike K. We saw at the beginning of this chapter that bivariate digital call
and put options are linked by precise arbitrage relationships. Intuitively, building on these
findings must be possible to recover arbitrage relationships between call and put rainbow
options.
We remind the readers that bivariate call and put digital options are linked by the no-
arbitrage relationship
DLL(K1, K2) = B (t, T ) −DC1(K1) −DC2(K2) + DHH(K1, K2)
which corresponds to the relationship between one copula and its survival:
CLL(1 −u, 1 −v) = 1 −u −v + CHH(u, v)
So, in our case we have
CLL (Q1 (S1 (T ) ⩽u) , Q2 (S2 (T ) ⩽u) | ℑt)
= 1 −Q1 (S1 (T ) > u | ℑt) −Q2 (S2 (T ) > u | ℑt)
+ CHH (S1 (T ) > u, S2 (T ) > u | ℑt)
Based on this relationship it is now straightforward to derive a no-arbitrage link between
the put option on the maximum and the call option on the minimum.
Proposition 8.6 [Rainbow put–call parity]
A put option on the maximum of two assets
with strike price K and exercise date T is linked to the call option on the minimum of the
same assets, with the same strike and exercise date by the relationship
PUT (S1, S2, t; K, T ) + S1 + S2 = CALL (S1, S2, t; K, T ) + B (t, T ) K
+ CALL (S1, S2, t; 0, T )
Proof :
Adding and subtracting 1 to the right-hand side of the relationship between CLL
and its survival copula and considering 1 −Qi (u | ℑt) = Qi (u | ℑt) we have
CLL (Q1 (u) , Q2 (⩽u) | ℑt) = Q1 (u | ℑt) + Q2 (u | ℑt)
−1 + CHH(Q1 (u) , Q2 (u) | ℑt)

260
Copula Methods in Finance
We now compute
PUT (S1, S2, t; K, T ) = B (t, T )
 K
0
CLL(Q1 (u) , Q2 (u) | ℑt) du
=
 K
0
B (t, T ) Q1 (u | ℑt) du +
 K
0
B (t, T ) Q2(u | ℑt) du
−
 K
0
B(t, T ) du +
 K
0
B (t, T ) CHH(u, u | ℑt) du
=
 K
0
B (t, T ) Q1 (u | ℑt) du +
 K
0
B (t, T ) Q2(u | ℑt) du
−
 K
0
B(t, T ) du +
 ∞
0
BCHH(Q1 (u) , Q2 (u) | ℑt) du
−
 ∞
K
BCHH(Q1 (u) , Q2 (u) | ℑt) du
= PUT (S1, t; K, T ) + PUT (S2, t; K, T ) −KB (t, T )
+ CALL (S1, S2, t; 0, T ) −CALL (S1, S2, t; K, T )
If we now use the univariate put–call parity
PUT (Si, t; K, T ) + Si = CALL (Si, t; K, T ) + KB
and we reorder terms, we have
PUT (S1, S2, t; K, T ) + S1 + S2 = CALL (S1, t; K, T ) + CALL (S2, t; K, T ) + BK
+ CALL (S1, S2, t; 0, T ) −CALL (S1, S2, t; K, T )
Finally, if we consider the relationship proved in the previous section
CALL (S1, S2, t; K, T ) = CALL (S1, t; K, T ) + CALL (S2, t; K, T )
−CALL (S1, S2, t; K, T )
we obtain the result in the proposition.
□
Remark 8.2
Notice that using the same relationship between call options on the maximum
and minimum between two assets and the fact that
CALL (Si, t; 0, T ) = Si (t)
for i = 1, 2 the put–call parity relationship in the proposition can be written as
PUT (S1, S2, t; K, T ) = CALL (S1, S2, t; K, T ) + B (t, T ) K
−CALL (S1, S2, t; 0, T )
as in Stulz (1982), page 167.

Option Pricing with Copulas
261
8.5.4
Put option on the minimum of two assets
Finally, let us come to evaluate the put option on the minimum between two assets. The
pay-off of the option is
G (S1 (T ) , S2 (T ) , T ) = max [K −min (S1 (T ) , S2 (T )) , 0]
Again by arbitrage arguments, it is easy to check that the same parity relationship above
holds, and by symmetry we have
PUT (S1, S2, t; K, T ) = CALL (S1, S2, t; K, T ) + B (t, T ) K
−CALL (S1, S2, t; 0, T )
However, it may be instructive to derive the result directly by using copula duality.
Intuitively, this put option may end up in the money if either S1 (T ) ⩽K or S2 (T ) ⩽K.
It is then natural to write the price as
PUT (S1, S2, t; K, T ) = B (t, T )
 K
0
Pr(S1 ⩽u or S2 ⩽u | ℑt) du
where the probability is computed under the risk-neutral measure Q. Remember that
Pr (S1 ⩽u, S2 ⩽u | ℑt) = CLL (Q1 (u) , Q2 (u) | ℑt)
and from Chapter 2
Pr (S1 ⩽u or S2 ⩽u | ℑt) = 
CLL (Q1 (u) , Q2 (u) | ℑt)
= Q1 (u | ℑt) + Q2 (u | ℑt) −CLL (Q1 (u) , Q2 (u) | ℑt)
where 
CLL is the dual of copula CLL. Using this we obtain a relationship between put
options on the minimum and the maximum between two assets
PUT (S1, S2, t; K, T ) = B (t, T )
 K
0

CLL(Q1 (u) , Q2 (u) | ℑt) du
= B (t, T )
 K
0
[Q1 (u | ℑt) + Q2 (u | ℑt)
−CLL (Q1 (u) , Q2 (u) | ℑt)] du
= PUT (S1, t; K, T ) + PUT (S2, t; K, T ) −PUT (S1, S2, t; K, T )
Substituting put–call parities we finally have
PUT (S1, S2, t; K, T ) = 2B (t, T ) K −S1 (t) −S2 (t)
+ CALL (S1, t; K, T ) + CALL (S2, t; K, T )
+ S1 (t) + S2 (t) −CALL (S1, S2, t; K, T )
−CALL (S1, S2, t; 0, T ) −B (t, T ) K
= B (t, T ) K −CALL (S1, S2, t; 0, T )
+ CALL (S1, S2, t; K, T )

262
Copula Methods in Finance
where again we used the relationship between call options on the maximum and minimum
between two assets.
8.5.5
Option to exchange
The price of the option to exchange one asset for another was originally derived – for
log-normal distributions – by Margrabe (1978). It can be considered as a portfolio of one
underlying asset and a zero-strike call option on the minimum. Consider the option to
exchange the first asset for the second, for instance.2 The pay-off of this exchange option is
G(S1(T ), S2(T ), T ) = max(S1(T ) −S2(T ), 0)
which can be rewritten as
G(S1(T ), S2(T ), T ) = S1(T ) −max(min(S1, S2), 0)
Recalling that the risk-neutral expected value of the underlying asset at maturity is the
forward price, it follows that the exchange option price (OEX) is the current value of the
first underlying asset minus the price of the option on the minimum between the two, with
strike equal to zero. So,
OEX (S1, S2, t; T ) = S1 (t) −CALL (S1, S2, t; 0, T )
It is then straightforward to design super-replication bounds for this product. The bounds
used in the call option on the minimum simplify substantially, at least in notation, because
we obviously have K∗∗⩾K = 0. In fact, the upper bound is
OEX+ (S1, S2, t; T ) = S1 (t) −CALL−(S1, S2, t; 0, T )
= S1 (t) −

CALL (S1, t; 0, T ) −CALL

S1, t; K∗∗, T
	
+ CALL (S2, t; 0, T )−CALL

S2, t; K∗∗, T
	
−B (t, T )

K∗∗−0

= S1 (t) −S1 (t) + CALL

S1, t; K∗∗, T
	
−S2 (t)
+ CALL

S2, t; K∗∗, T
	
+ B (t, T ) K∗∗
= CALL

S1, t; K∗∗, T
	
+ CALL

S2, t; K∗∗, T
	
+ BK∗∗−S2 (t)
= CALL

S1, t; K∗∗, T
	
+ PUT

S2, t; K∗∗, T
	
where we recall that a strike price K∗∗is such that Q1 (K∗∗) + Q2 (K∗∗) = 1. On the other
hand, the lower bound turns out to be
OEX−(S1, S2, t; T ) = S1 (t) −CALL+ (S1, S2, t; 0, T )
= S1 (t) −

CALL (S1, t; 0, T ) −CALL

S1, t; K∗, T
	
−CALL

S2, t, K∗, T
	
2 It is also a particular case of the spread option, with K = 0.

Option Pricing with Copulas
263
= S1 (t) −S1 (t) + CALL

S1, t; K∗, T
	
+ CALL

S2, t; , K∗, T
	
= CALL

S1, t; K∗, T
	
+ CALL

S2, t; , K∗, T
	
with K∗defined in such a way that Q1 (K∗) = Q2 (K∗).
Summing up, the super-replication bounds of the option to exchange are represented by
CALL

S1, t; K∗, T
	
−CALL

S2, t; , K∗, T
	
⩽OEX (S1, S2, t; T )
⩽CALL

S1, t; K∗∗, T
	
+ PUT

S2, t; K∗∗, T
	
8.5.6
Pricing and hedging rainbows with smiles: Everest notes
Consider a concrete example of an index-linked product whose coupon is linked to the
minimum or maximum return of two assets measured over the investment horizon from t to
T , provided this figure is higher than some assigned threshold K. The value of the coupon
is then, for example,
max

min
S1 (T )
S1 (t) , S2 (T )
S2 (t)

, K

= K + max

min
S1 (T )
S1 (t) , S2 (T )
S2 (t)

−K, 0

and the problem involves the evaluation of a call option on the minimum of two assets.
For example, setting K = 1 we ensure against the possibility of a negative coupon. Our
task is to provide a solution to the problem that could be sufficiently general to account
for different shapes of the risk-adjusted distributions of the two assets or indexes involved
and for a general dependence structure. We are particularly interested in checking extreme
dependence scenarios and the corresponding super-replication strategies. Our example uses
information on the Italian blue chip index, Mib 30 and the Japanese index, Nikkei 225.
We apply the following procedure. We first estimate the implied risk-neutral distribution
from option data. We then compute the super-replication strategies and the pricing bounds
for the product. We finally show how to construct a mixture copula to account for imperfect
dependence and maintain a closed form solution for the hedging strategy and the price.
Retrieving the implied probability from market prices
We start by extracting the risk-neutral distributions from the option data taken from Bloom-
berg. The implied volatility smile for both the markets was fitted using a quadratic inter-
polation technique as suggested by Shimko (1994). The fitted smile curves are presented
in Figure 8.4. The strikes were normalized by the observed value of the underlying index
on the day of evaluation, so that the value 1 on the horizontal axis corresponds to the
at-the-money volatility.
Volatility interpolation is used to reconstruct call spreads approximating the implied
cumulative risk-neutral distributions. The resulting probability distributions are given in
Figure 8.5. For any level of one underlying asset, which is again normalized by its current
value, we depict the probabilities that over the next six months that market is growing
more than or less than the threshold. Using the previous notation, the decreasing sched-
ules are referred to the decumulative distributions Qi and the increasing ones describe the
cumulative probabilities Qi.

264
Copula Methods in Finance
0.15
0.2
0.25
0.3
0.35
0.4
0.45
0.8
0.85
0.9
0.95
1
1.05
1.1
MIB30
Nikkei
Figure 8.4
Smiles of Nikkei 225 and Mib 30
0
0.2
0.4
0.6
0.8
1
1.2
0.85
0.9
0.95
1
1.05
1.1
1.15
1.2
Figure 8.5
Probability distributions of Nikkei and Mib 30
We notice that both distributions give negligible value to the event of a decrease of the
markets 15% below the current value. Furthermore, the probability of the Mib 30 index
increasing or falling by a given percentage is always lower than the corresponding proba-
bility for the Nikkei 225 index (first-order stochastic dominance). This implies, of course,
min(QMib (K) , QNikkei (K)) = QNikkei (K)

Option Pricing with Copulas
265
for any threshold return K and the perfect positive dependence pricing kernel for call options
coincides with that of the Nikkei.
In order to recover the perfect negative dependence pricing kernel we notice instead
that the cumulative distribution of returns on the Mib 30 index crosses the decumulative
distribution of the Nikkei slightly above the current values of the indexes. More precisely,
we have
QMib (1.00676) = QNikkei (1.00676)
In other terms, the risk-neutral probability of the Italian index to grow less than 67.6
basis points is equal to the probability of the Japanese index growing more than the same
figure. We have then that K∗∗= 1.00676, and the lower bound of the pricing kernel is zero
beyond that level.
Pricing the rainbow option
We are now in a position to price and hedge the rainbow option and the index-linked product.
Based on the above analysis, we have that the upper bound pricing kernel corresponds to
the Nikkei pricing kernel. The lower pricing kernel for strike prices K < 1.00676 is instead
equal to two call spreads on the strike prices K and K∗∗= 1.00676 and a debt position
equal to K∗∗−K, while it is equal to zero for all the other prices. The pricing kernels are
depicted in Figure 8.6.
In the figure we also report linear combinations of the upper and lower pricing kernels,
which are consistent with imperfect dependence between the markets: the corresponding
copula functions are special cases of the Fr´echet family of copulas.
Finally, in Figure 8.7 we present the pricing schedules of the index-linked product with
respect to different return protection rates, i.e. for different strikes of the rainbow option.
0
0.2
0.4
0.6
0.8
1
1.2
0.85
0.9
0.95
1
1.05
1.1
1.15
1.2
Upper
Lower
Alpha 0.75
Alpha 0.50
Alpha 0.25
Figure 8.6
Pricing kernel of the rainbow option

266
Copula Methods in Finance
0.99
1
1.01
1.02
1.03
1.04
1.05
1.06
1.07
0
20
40
60
80
100
120
140
160
180
200
Upper
Alpha 0.25
Alpha 0.50
Alpha 0.75
Lower
Figure 8.7
Price of the rainbow equity-linked note
−0.1
0
0.1
0.2
0.3
0.4
0.5
0.6
0
20
40
60
80
100
120
140
160
180
200
Upper
Alpha 0.25
Alpha 0.50
Alpha 0.75
Lower
Figure 8.8
Delta of the rainbow equity-linked note
The pricing schedules are reported for the different pricing kernels depicted above. The
pricing schedules look almost linear and increase with the degree of dependence between
the markets. To give a figure, the cost of providing zero return protection on a 1 million
investment in the product (K = 1) is almost worthless if the two markets are perfectly nega-
tively dependent (it is 24 cents), while it amounts to 51 546.31 in the case of perfect positive
dependence. In the case of independence the cost is about half that, scoring 25 773.27.

Option Pricing with Copulas
267
To conclude, we report in Figure 8.8 the value of the delta of the contracts with respect
to movements of the two markets. The sensitivity to the market increases with dependence
and decreases with moneyness, that is, with the increase in the protection threshold offered.
8.6
PRICING BARRIER OPTIONS
Barrier options are contingent claims in which the exercise is conditional on the event that
the value of the underlying asset has been above or below a given value over a given
reference period. In the standard plain vanilla cases, barrier options are classified according
to whether an option is activated (knocked-in) or deactivated (knocked-out) if some upper
or lower barrier level is reached over the whole life of the option. We may then have
down-and-out, up-and-out, down-and-in and up-and-in options both of the call and put type.
Typically, a fixed payment R may be given to the holder of the option if it is not activated:
this payment is called “rebate”. These options have closed form solutions under the standard
Black–Scholes setting, and the readers are referred to the standard option pricing literature
for these results.
Here we want to show how to apply the copula function pricing technique for a general
treatment of barrier options, accounting for more complex cases. In fact, the pricing prob-
lem of barrier options may get involved if some of the assumptions concerning either the
dynamics of the underlying asset are made more general or the structure of the contract
is made more complex than in the standard plain vanilla case. The first problem has to
do with the fact that while closed form solutions for barrier options are available under
the standard Black–Scholes assumption of constant volatility, the reality of markets shows
clear evidence against such hypotheses of normally distributed returns. So, even for standard
options one would like to cast the pricing problem in a more general setting in order to
account for models in which the conditional distribution of the underlying asset can be cho-
sen to be consistent with some stochastic volatility dynamics. As barriers are generally used
to reduce the cost of the option for the buyer and the premium earned by the counterparty
who writes it, it is particularly relevant for the counterparty to assess the risk of this option
under realistic dynamics of the underlying asset.
A general setting would also enable one to address the case of complex barrier option
contracts. A simple example is given by barriers in options with exotic pay-offs. Consider
the case of rainbow or basket options or path-dependent contingent claims including barriers:
in all of these cases the closed form solutions obtained under the standard Black–Scholes
setting can only be taken as arbitrary approximations to the “fair value” of the contract.
The structure of the barrier can also be much more sophisticated than it is in the standard
cases. A first source of complexity can be represented by the fact that the barrier may
be referred to a variable which is different from the underlying asset: this is the case, for
example, of barrier swaptions, whose underlying asset we recall is the forward swap rate,
with barriers referred to the LIBOR rate. In cases like these the important question is how
the dependence structure between the underlying asset and the barrier variable (the swap
rate and the LIBOR rate in the example above) impacts on the determination of the joint
probability that the option ends in the money and the barrier is hit or not. Another source
of complexity could be represented by the way in which the event of reaching or crossing
a barrier is linked to activation or deactivation of the contingent claim. In some cases the
option may be knocked-out or knocked-in only if the reference variable has been below
or above some given barrier for a period of time longer than a given interval. Such an

268
Copula Methods in Finance
interval can be referred to the whole length of the time to exercise, as in the so-called
parisian options, or it may be itself stochastic, and referred to the time difference between
the exercise date and the date on which the barrier is crossed (caution time), as in the
so-called edokko options. Furthermore, the period the reference variable has been below or
above the barrier can be computed as the length of time it has continuously been beyond the
barrier or the overall time spent in that region: the latter case is called cumulative parisian
or edokko option. The idea behind these structures is to make manipulation of the trigger
variable market more difficult.
To understand how copula functions can be usefully employed to price barrier options,
consider that, from a fully general perspective, a barrier option can be seen as a contingent
claim that provides a positive pay-off if two events take place. Beside the standard event
that the option ends up in the money at the time of exercise, there is a second event which
acts as a “trigger” to activate and deactivate the option. In a broad sense, pricing a barrier
option involves the evaluation of the joint probability of the exercise and the trigger event,
and that is where copula functions can help.
8.6.1
Pricing call barrier options with copulas: the general framework
As a first example, consider a European call option written on asset S with strike K and
exercise time T which can be exercised if some trigger event h occurs, and provides a rebate
R otherwise. For the sake of simplicity we assume that the rebate is paid at the exercise
date. Considering the rebate to be paid at the time the trigger event occurs would only make
the treatment more involved, calling for a specification of the probability density of the
time when it takes place. Say, the trigger variable is a boolean variable taking value 1 if the
event takes place and 0 otherwise. The relevant pricing kernel in this case is represented
by the joint probability Q(u, 1) = Pr(S(T ) > u, h = 1). Using the probability distribution
approach we may write the price of the option as
CALL (S(t), t; K, T, h = 1, R) = B
 ∞
K
Q(u, 1 | ℑt) du + B (t, T ) Qh(ℑt)R
where Qh is the marginal conditional probability of the trigger event h = 0 and we recall that
Qh = 1 −Qh is the probability of the complement. This bivariate distribution interpretation
is well suited for the application of copula functions. We have in fact
CALL (S(t), t; K, T, h = 1, R) = B (t, T )
 ∞
K
CHH[QS

u), Qh | ℑt
	
] du
+ B (t, T ) Qh(ℑt)R
The same technique could be applied to price a call option with the same strike and
exercise date, but with exercise conditioned on the event that the trigger is not activated. In
this case the option can be exercised if h = 0 and the rebate R is paid otherwise. The price
will be
CALL (S(t), t; K, T, h = 0, R) = B (t, T )
 ∞
K
CHL[QS (u), Qh | ℑt)] du
+ B (t, T ) Qh(ℑt)R

Option Pricing with Copulas
269
We may again verify that no-arbitrage requires the relationship CHL(u, 1 −v) = u−
CHH(u, v), so that
CALL (S(t), t; K, T, h = 0, R)
= B (t, T )
 ∞
K
[QS(u) −CHH(QS (u) , Qh | ℑt)] du + B (t, T ) Qh(ℑt)R
= CALL (S(t), t; K, T ) −CALL (S(t), t; K, T, h = 1, R) + B (t, T ) R
In fact, buying a barrier option that can be exercised under some set of states of the
world, i.e. some trigger condition, and an equal option whose exercise is conditioned on the
complement set, amounts to removing the effect of the barrier. So, the result is the same as
to buy an option that can be exercised irrespective of the condition plus a fixed sum, the
rebate, which is received for sure.
CALL (S(t), t; K, T, h = 0, R) + CALL (S(t), t; K, T, h = 1, R)
= CALL (S(t), t; K, T ) + B (t, T ) R
Remark 8.3
It is worthwhile checking what would happen if the rebate were paid at the
time the trigger event takes place. Notice that in this case there would be an asymmetry
in the treatment. In fact, for the option conditioned on the event h = 1, the rebate could
only be paid at expiration (it is a knock-in barrier option). On the contrary, the option
conditioned on the event that the trigger is not activated, that is h = 0, would typically
pay a rebate at the time in which the event actually takes place (it is a knock-out barrier
option). Let us define θ = inf (s; h (s) = 1, s ⩾t) the time of the trigger event and B (t, θ)
the corresponding risk-free discount factor. In this case the value of the rebate would be
EQ

B (t, θ) 1{t⩽θ⩽T }
	
R. Accordingly, in the relationship between knock-in and knock-out
options we would recover
B (t, T ) Qh(ℑt)R + EQ

B (t, θ) 1{t⩽θ⩽T }
	
R
instead of B (t, T ) R. Substituting this term for B (t, T ) R would not, however, change the
proofs reported below.
Before going on it may be worth considering a very special case that will be useful in the
development of this discussion. Take the case of a barrier call option with a strike K = 0.
We have
CALL (S(t), t; 0, T, h = 1, R) = B (t, T )
 ∞
0
CHH

QS

u), Qh | ℑt
	
du
+ B (t, T ) Qh(ℑt)R
CALL (S(t), t; 0, T, h = 0, R) = B (t, T )
 ∞
0
CHL [QS (u), Qh | ℑt)] du
+ B (t, T ) Qh(ℑt)R
and
CALL (S(t), t; 0, T, h = 0, R) + CALL (S(t), t; 0, T, h = 1, R) = S (t) + B (t, T ) R

270
Copula Methods in Finance
It is clear that the value of a barrier call option with strike equal to zero is an option
delivering the asset at exercise date T if the trigger event occurs, and the rebate R if it does
not. If the rebate is assumed to be zero, this contingent claim is known as digital, or one
touch, asset-or-nothing (AoN) option. So, we define
DCAoN (S(t), t; T, h = 0) = CALL (S(t), t; 0, T, h = 0, 0)
DCAoN (S(t), t; T, h = 1) = CALL (S(t), t; 0, T, h = 1, 0)
By the same token, imagine a contract that pays a unit of cash at the exercise time
T if the trigger event occurs. We may call this contingent claim a digital, or one touch,
cash-or-nothing (CoN) option, and we may define
DCCoN (S(t), t; T, h = 0, 0) = B (t, T ) Qh(ℑt)
DCCoN (S(t), t; T, h = 1, 0) = B (t, T ) Qh(ℑt)
8.6.2
Pricing put barrier option: the general framework
We are now going to show that the copula arbitrage relationship also enables us to establish
a relationship between call and put options. Consider a put option with strike K and exercise
time T . The exercise is again conditioned on the trigger h = 1 with rebate R. The price is
PUT (S(t), t; K, T, h = 1, R) = B (t, T )
 K
0
CLH [QS (u), Qh | ℑt)] du
+ B (t, T ) Qh(ℑt)R
Using the no-arbitrage relationship, CLH(1 −u, v) = v−CHH(u, v), we have
PUT(S(t), t; K, T, h=1, R) = B(t, T )
 K
0
[Qh(ℑt) −CHH[QS(u), Qh | ℑt)]] du
+ B(t, T )Qh(ℑt)R
= B(t, T )KQh(ℑt) −B(t, T )
 K
0
CHH[QS(u), Qh | ℑt)] du
+ B(t, T )Qh(ℑt)R
= B(t, T )KQh(ℑt) −B(t, T )
 ∞
0
CHH[QS(u), Qh | ℑt)] du
+ B(t, T )
 ∞
K
CHH[QS(u), Qh | ℑt)] + B(t, T )Qh(ℑt)R
= B(t, T )KQh(1 | ℑt) + CALL(S(t), t; K, T, h = 1, R)
−B(t, T )
 ∞
0
CHH[QS(u), Qh(1) | ℑt)]du

Option Pricing with Copulas
271
We now turn to the case in which the put option, with the same strike and time to
exercise, is subject to the trigger h = 0 with rebate R. As in the case of call options, ruling
out arbitrage opportunities requires
PUT (S(t), t; K, T, h = 0, R) + PUT (S(t), t; K, T, h = 1, R)
= PUT (S(t), t; K, T ) + B (t, T ) R
Using the put–call parity relationships we have finally
PUT (S(t), t; K, T, h = 0, R) = PUT (S(t), t; K, T ) + B (t, T ) R
−PUT (S(t), t; K, T, h = 1, R)
= CALL (S(t), t; K, T ) + B (t, T ) K −S (t)
+ B (t, T ) R −PUT (S(t), t; K, T, h = 1, R)
= CALL (S(t), t; K, T ) + B (t, T ) K −S (t) + B (t, T ) R
−B (t, T ) KQh(ℑt) −CALL (S(t), t; K, T, h = 1, R)
+ B (t, T )
 ∞
0
CHH[QS (u), Qh | ℑt)] du
= B (t, T ) KQh(ℑt)
+ CALL (S(t), t; K, T, h = 0, R)
−B (t, T )
 ∞
0
CHL[QS (u), Qh | ℑt)] du
The final step is obtained using the no-arbitrage relationships between the barrier call
options and the martingale property. In fact, we in turn exploit
CALL (S(t), t; K, T, h = 0, R) = CALL (S(t), t; K, T )
+ B (t, T ) R −CALL (S(t), t; K, T, h = 1, R)
and
B (t, T )
 ∞
0
CHH [QS (u), Qh(1) | ℑt)] du
+
 ∞
0
CHL [QS (u), 1 −Qh(1) | ℑt)] du

= S (t)
If the readers remember our definitions of digital asset-or-nothing and cash-or-nothing
options, it is then immediate to obtain that the relationship between barrier put and call
options can be summarized in very general terms as follows:

272
Copula Methods in Finance
Proposition 8.7 [Barrier options put–call parity]
Denote by CALL (S(t), t; K, T, h, R)
the price of a barrier call option with strike K, exercise time T , trigger event h and rebate
R. Then the barrier put option with the same terms is priced by
PUT (S(t), t; K, T, h, R) + DCAoN (S(t), t; T, h)
= CALL (S(t), t; K, T, h, R) + KDCCoN (S(t), t; T, h)
Let us note that the put–call parity for barrier options closely resembles the relationship
between plain vanilla options, apart from the fact that the underlying asset and the dis-
counted strike are substituted by digital asset-or-nothing and cash-or-nothing respectively.
Furthermore, the relationship is very general and extends from standard barrier options to
the more complex cases, such as parisian options.
8.6.3
Specifying the trigger event
We now relate the general approach above to special cases of barrier options. Of course the
approach is not useful in cases in which the joint distribution of the exercise and trigger
events are known in closed form. Unfortunately, this is true only for geometric brownian
motions (BMs), and in general for standard products. The approach can instead be fruitfully
applied to cases in which this joint distribution is not known or is not easily computed. As
in the other applications the advantage of the approach lies in the possibility of modeling
the marginal distributions of the two events separately from the dependence structure. In
barrier option applications, however, a word of caution is in order. Indeed, the flexibility
of the approach may turn into a flaw and lead to inconsistent results. The basic problem
is that the dependence structure between the trigger event and the exercise event must be
consistent with the dependence structure of the reference variable of the trigger event and
the underlying asset. To understand the point, assume that we apply an arbitrary copula
to the evaluation of a standard barrier option, in which the underlying asset is also the
reference variable of the trigger event, and assume that it follows a geometric BM. This is
a case in which the flexibility of the approach would result in a wrong price. While in this
example the inconsistency shows up very clearly, mostly because we can compute the price
in closed form, the same basic problem may be found in every barrier option application.
Getting the copula function choice right is then particularly relevant in such applications.
In the following section we suggest some techniques that may be applied to estimate the
marginal distribution of the trigger event and the dependence relationship with the exercise
event.
Marginal probability of the trigger event
The trigger event is activated when the reference variable hits a prespecified level or stays
beyond that level longer than a given period of time. Consider the case in which the reference
variable is assumed to follow a geometric BM under the risk-neutral measure, that is
dS = rS dt + σS dz
where z is a Wiener process, and r and σ are constant parameters. In this case, the marginal
probability of the trigger event may be known in closed form. Take the simplest example

Option Pricing with Copulas
273
in which the trigger event is defined as the case in which an upper or lower barrier H
(H ∈ℜ+) is hit. It may be useful to briefly review the basic principles behind the proof,
because the same ideas will be used to extend the application to more complex cases for
which the closed form solution cannot be obtained and must be computed by simulation.
First, we introduce the ratio process S (t) /H and change the stochastic process into an
arithmetic BM defining X (t) = ln (S (t) /H). We have
dX = υ dt + σ dz
with υ = r −σ 2/2 and X (0) = ln (S (0) /H). It is clear that evaluating the probability that
the process S (t) will or will not hit the barrier H by a certain time T is the same as
assessing the probability that an arithmetic BM starting at X (0) will hit the zero barrier.
That is, if for example S (t) > H
S (t) ⩾H ⇐⇒X (0) +
 t
0
υ du +
 t
0
σz (u) ⩾0
⇐⇒
 t
0
υ du +
 t
0
σz (u) ⩾−X (0)
for all t > 0. By the same token, the event that the barrier will be attained from below,
starting from S (t) < H, is equivalent to
S (t) ⩽H ⇐⇒X (0) +
 t
0
υ du +
 t
0
σz (u) ⩽0
⇐⇒
 t
0
υ du +
 t
0
σz (u) ⩽−X (0)
We introduce two processes MX and mX denoting, respectively, the running maximum
and minimum of the stochastic process X, i.e.
MX (t) ≡{max X (u) ; 0 ⩽u ⩽t}
mX (t) ≡{min X (u) ; 0 ⩽u ⩽t}
It is clear that the event of an upper or lower barrier H not being hit (h = 0) by time T
may then be characterized as
h = 0 ⇐⇒MX (T ) ⩽y
h = 0 ⇐⇒mX (T ) ⩾y
with y = −X (0). The probability that the barrier will not be hit is then given by the formulas
Qh = Q (MX (T ) ⩽y) = N
y −υt
σ√t

−exp
2υy
σ 2

N
−y −υt
σ√t

Qh = Q (mX (T ) ⩾y) = N
−y + υt
σ√t

−exp
2υy
σ 2

N
y + υt
σ√t


274
Copula Methods in Finance
and the probability of the complement (h = 1) is of course
Qh = 1 −Qh = N
−y + υt
σ√t

+ exp
2υy
σ 2

N
−y −υt
σ√t

Qh = 1 −Qh = N
y −υt
σ√t

+ exp
2υy
σ 2

N
y + υt
σ√t

Remark 8.4
The formulas are obtained by, first, changing the measure in such a way as
to transform the stochastic process followed by X (t) into a standard BM (i.e. with no drift),
and then applying the reflection principle. This principle determines the joint probability
that a standard BM will hit a barrier y and will end above a given value k.
Pricing barrier options
Substituting y = −X (t) = ln (H/S (t)) we may reconduct the probabilities above to the
probability of the trigger event under the original geometric BM, and compute the prices of
digital contracts representing the event of the barrier being hit (one touch) or not (no-touch).
For example, the risk-neutral exercise probability of a no-touch, i.e. an option that pays
one unit of currency if an upper or lower barrier is not reached, is given by
Q (S (θ) ⩽H; t ⩽θ ⩽T | ℑt) = N
ln (H/S (t)) −υ (T −t)
σ
√
T −t

−
H
S (t) exp
2υ
σ 2

N
ln (S (t) /H) −υ (T −t)
σ
√
T −t

Q (S (θ) ⩾H; t ⩽θ ⩽T | ℑt) = N
ln (S (t) /H) + υ (T −t)
σ
√
T −t

−
H
S (t) exp
2υ
σ 2

N
ln (H/S (t)) + υ (T −t)
σ√T −t

(8.2)
The corresponding price is obtained if we multiply by the discount factor B(t, T ).
If one wants to price the corresponding digital put or call option, which pays one unit
of currency if the upper or lower barrier is reached and the underlying asset is below or
above a fixed strike, an analogous procedure must be followed. Consider, for instance, the
down-and-out digital, which pays if and only if the minimum of the underlying process
S does not go below the barrier H and the underlying asset is not below the strike K at
maturity. The risk-neutral probability needed is
Q (mS(T ) ⩾H, S(T ) ⩾K | ℑt) = N
ln (S (t) /K) + υ (T −t)
σ
√
T −t

−
H
S (t) exp
2υ
σ 2

N

ln

H 2/KS (t)
	
+ υ (T −t)
σ√T −t

(8.3)

Option Pricing with Copulas
275
Let us use the usual notation
d2(K) = ln (S (t) /K) + υ (T −t)
σ√T −t
which implies
ln

H 2/KS (t)
	
+ υ (T −t)
σ
√
T −t
= d2(K) −2ln(S(t)/H)
σ
√
T −t
and note that
H
S (t) exp
2υ
σ 2

= exp
2υ
σ 2 ln H
S (t)

=
 H
S(t)
a−1
where a = 2r/σ 2. Probability (8.3) can be written, in a more concise way, as
N (d2(K)) −
 H
S(t)
a−1
N

d2(K) −2ln(S(t)/H)
σ
√
T −t

(8.4)
Knowing the digital price one can, in turn, reconstruct the down-and-out call price, following
the procedure used several times before.
So far we have described the case of a standard barrier option, whose pay-off may be
described as
1min S(θ;t⩽θ⩽T )>H max (S (T ) −K, 0)
where we refer to a down-and-out call option as an example. More complex trigger events
could be given by the general form
f

τ −	
max (S (T ) −K, 0)
where τ −is the amount of time during the option life that the underlying price was lower
than a barrier H. This general approach was suggested by Linetsky (1999) as a way to
address a large class of exotic barrier options. In particular, he proposes the use of standard
linear or exponential discount functions, such as
exp

−δτ −	
max (S (T ) −K, 0)
where δ is a prespecified discount intensity. These products are called step options and
include standard plain vanilla options and standard barrier options as extreme examples.
Another choice would be instead
1τ −<α(T −t) max (S (T ) −K, 0)
This option is called a cumulative parisian option by Chesney et al. (1997). For all of
these options, the probability distribution of the amount of time spent below (or above) a

276
Copula Methods in Finance
given barrier, technically called “occupation time”, can be recovered in closed form for the
arithmetic and geometric BM cases. In cases in which the reference variable is represented
by the underlying asset, we are also able to recover closed form solutions for the option
price. Knowing the probability distribution of the occupation time, however, enables us to
use the copula function approach for more general applications.
8.6.4
Calibrating the dependence structure
In order to provide a flexible characterization of the price of barrier options, defined in a
broad sense, it may be useful to analyze the case in which the underlying and the trigger
variable coincide and are represented by a geometric BM. Indeed, we are going to show that
this case enables us to construct a new kind of copula, linked to the closed form solutions
originating from the reflection principle. This dependence structure will be called a reflection
copula and it will permit us to extend the pricing technique to more complex problems.
Let us look at two examples: (i) the case of an option written on a variable different from
that used as a trigger, and (ii) the case in which the underlying asset is not described by
a geometric BM, while the trigger variable is. In cases like these, it may be intuitively
appealing to use this copula to represent the dependence structure between the underlying
and the triggering variable.
8.6.5
The reflection copula
We know that under the standard assumption of a process following a geometric BM, closed
formulas for standard barrier options are available: from these one can extract the implied
information concerning the dependence structure between the trigger event and the exercise
of the option. In order to do this, we focus without loss of generality on the down-and-out
case: from the no-arbitrage price of such options, we want to extract, for given variance of
the underlying and riskless rate, the implied correlation between a geometric BM S and its
running minimum, mS(T ).
We start by rewriting the probability of the joint event {mS(T ) ⩾H, S(T ) ⩾K}, which
characterizes the down-and-out digital price, in terms of a copula function: assuming a com-
plete market, Sklar’s theorem can be applied, allowing us to state that the joint probability
in (8.4) is a copula, written in the marginal probabilities of the events {S(T ) ⩾K} and
{mS(T ) ⩾H}. The latter can be easily evaluated:
Pr(S(T ) ⩾K | ℑt) = N(d2(K))
(8.5)
and
Pr(mS(T ) ⩾H | ℑt) = N(d2(H)) −
 H
S(t)
a−1
N

d2(H) −2ln(S(t)/H)
σ
√
T −t

(8.6)
For the sake of simplicity, let us denote as l(H) the function
l(H) = d2(H) −2ln(S(t)/H)
σ
√
T −t

Option Pricing with Copulas
277
Sklar’s theorem allows us to state that there exists a unique (due to the continuity of S)
implied copula, i.e. a unique function CHH which gives (8.4) in terms of the marginals:
N(d2(K)) −
 H
S(t)
a−1
N

d2(K) −2ln(S(t)/H)
σ
√
T −t

= CHH

N(d2(K)), N(d2(H)) −
 H
S(t)
a−1
N (l(H))

One can verify that the unique copula involved is
CHH(v, z) = v + z −N(d2(h(z)))
N(l(h(z)))
N

d2(g(v)) −2ln(S(t)/h(z))
σ
√
T −t

(8.7)
where the functions H = h(z) and K = g(v) represent H and K as functions of the marginal
probabilities z and v. They are obtained from the inverses, v = g−1(K) and z = h−1(H),
where
z = h−1(H) = N(d2(H)) −
 H
S(t)
a−1
N(l(H))
v = N(d2(K))
or K = d−1
2 (N−1(v)), since both N and d2 are monotone.
In turn, one can verify that the function CHH satisfies the definition of a copula function
given in Chapter 2.
Figure 8.9 presents the copula (8.7) for the case S(t) = 1, K = 1.1, r = 5%, σ = 20%,
T −t = 1, H = 1
2.
Implied correlation
Once we have extracted the reflection copula implied in a down-and-out price (8.7), we can
use it in order to reconstruct the Spearman correlation between S(T ) and mS(T ), which, as
1
0.5
Figure 8.9
The reflection copula

