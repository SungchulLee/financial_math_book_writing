# Time Series Analysis & Fractals

!!! info "Source"
    **Quantitative Finance for Physicists: An Introduction** by Belal E. Baaquie, Academic Press, 2004.
    These notes are used for educational purposes.

## Time Series Analysis

Chapter 5
Time Series Analysis
Time series analysis has become an indispensable theoretical tool in
financial and economic research. Section 5.1 is devoted to the com-
monly used univariate autoregressive and moving average models.
The means for modeling trends and seasonality effects are described
in Section 5.2. The processes with non-stationary variance (condi-
tional heteroskedasticity) are discussed in Section 5.3. Finally,
the specifics of the multivariate time series are introduced in
Section 5.4.
5.1 AUTOREGRESSIVE AND MOVING AVERAGE
MODELS
5.1.1 AUTOREGRESSIVE MODEL
First, we shall consider a univariate time series y(t) for a process
that is observed at moments t ¼ 0, 1, . . . , n (see, e.g., [1, 2]). The time
series in which the observation at moment t depends linearly on
several lagged observations at moments t  1, t  2, . . . , t  p
y(t) ¼ a1y(t  1) þ a2y(t  2) þ . . . þ apy(t  p) þ e(t), t > p (5:1:1)
is called the autoregressive process of order p, or AR(p). The term e(t) in
(5.1.1) is the white noise that satisfies the conditions (4.2.6). The lag
43

operator Lp ¼ y(t  p) is often used for describing time series. Note that
L0 ¼ y(t). Equation (5.1.1) in terms of the lag operator has the form
Ap(L)y(t) ¼ e(t)
(5:1:2)
where
Ap(L) ¼ 1  a1L  a2L2  . . .  apLp
(5:1:3)
The operator Ap(L) is called the AR polynomial in lag operator of
order p. Let us consider AR(1) that starts with a random shock. Its
definition implies that
y(0) ¼ e(0), y(1) ¼ a1y(0) þ e(1),
y(2) ¼ a1y(1) þ e(2) ¼ a1
2e(0) þ a1e(1) þ e(2), . . .
Hence, by induction,
y(t) ¼
X
t
i¼0
a1
ie(t  i)
(5:1:4)
Mean and variance of AR(1) equal, respectively
E[y(t)] ¼ 0, Var[y(t)] ¼ s2=(1  a1
2),
(5:1:5)
Obviously, the contributions of the ‘‘old’’ noise converge with time to
zero when ja1j < 1. As a result, this process does not drift too far from
its mean. This feature is named mean reversion.
The process with a1 ¼ 1 is called the random walk
y(t) ¼ y(t  1) þ e(t)
(5:1:6)
In this case, equation (5.1.4) reduces to
y(t) ¼
X
t
i¼0
e(t  i)
The noise contributions to the random walk do not weaken with time.
Therefore, the random walk does not exhibit mean reversion. Now,
consider the process that represents the first difference
x(t) ¼ y(t)  y(t  1) ¼ e(t)
(5:1:7)
Obviously, past noise has only transitory character for the process
x(t). Therefore, x(t) is mean-reverting. Some processes must be
44
Time Series Analysis

differenced several times in order to exclude non-transitory noise
shocks. The processes differenced d times are named integrated of
order d and denoted as I(d). The differencing operator is used for
describing an I(d) process
Di
d ¼ (1  Li)d, j, d ¼ . . . , 2, 1, 0, 1, 2 . . .
(5:1:8)
If an I(d) process can be reduced to AR(p) process while applying the
differencing operator, it is named ARI(p, d) process and has the form:
D1
dy(t)  a1D1
dy(t  1)  . . .  apD1
dy(t  p) ¼ e(t), t  p þ d
(5:1:9)
Note that differencing a time series d times reduces the number of
independent variables by d, so that the total number of independent
variables in ARI(p, d) within the sample with n observations equals
n  p  d.
The unit root is another notion widely used for discerning perman-
ent and transitory effects of random shocks. It is based on the roots of
the characteristic polynomial for the AR(p) model. For example,
AR(1) has the characteristic polynomial
1  a1z ¼ 0
(5:1:10)
If a1 ¼ 1, then z ¼ 1 and the characteristic polynomial has the
unit root. In general, the characteristic polynomial roots can have
complex values. The solution to equation (5.1.10) is outside the unit
circle (i.e., z > 1) when a1 < 1. It can be shown that all solutions for
AR(p) are outside the unit circle when
1  a1z  a2z2  . . .  apzp ¼ 0
(5:1:11)
5.1.2 MOVING AVERAGE MODELS
A model more general than AR(p) contains both lagged observa-
tions and lagged noise
y(t) ¼ a1y(t  1) þ a2y(t  2) þ . . . þ apy(t  p) þ e(t)
þ b1e(t  1) þ b2e(t  2) þ . . . þ bqe(t  q)
(5:1:12)
This model is called autoregressive moving average model of order
(p,q), or simply ARMA(p,q). Sometimes modeling of empirical data
Time Series Analysis
45

requires AR(p) with a rather high number p. Then, ARMA(p, q) may
be more efficient in that the total number of its terms (p þ q) needed
for given accuracy is lower than the number p in AR(p). ARMA(p, q)
can be expanded into the integrated model, ARIMA(p, d, q), similar
to the expansion of AR(p) into ARI(p, d). Neglecting the autoregres-
sive terms in ARMA(p, q) yields a ‘‘pure’’ moving average model
MA(q)
y(t) ¼ e(t) þ b1e(t  1) þ b2e(t  2) þ . . . þ bqe(t  q)
(5:1:13)
MA(q) can be presented in the form
y(t) ¼ Bq(L)e(t)
(5:1:14)
where Bq(L) is the MA polynomial in lag operator
Bq(L) ¼ 1 þ b1L þ b2L2 þ . . . þ bqLq
(5:1:15)
The moving average model does not depend explicitly on the lagged
values of y(t). Yet, it is easy to show that this model implicitly
incorporates the past. Consider, for example, the MA(1) model
y(t) ¼ e(t) þ b1e(t  1)
(5:1:16)
with e(0) ¼ 0. For this model,
y(1) ¼ e(1), y(2) ¼ e(2) þ b1e(1) ¼ e(2) þ b1y(1),
y(3) ¼ e(3) þ b1e(2) ¼ e(3) þ b1(y(2)  b1y(1)), . . .
Thus, the general result for MA(1) has the form
y(t)(1  b1L þ b1L2  b1L3 þ . . . ) ¼ e(t)
(5:1:17)
Equation (5.1.17) can be viewed as the AR(1) process, which illus-
trates that the MA model does depend on past.
The MA(q) model is invertible if it can be transformed into an
AR(1) model. It can be shown that MA(q) is invertible if all solu-
tions to the equation
1 þ b1z þ b2z2 þ . . . þ bqzq ¼ 0
(5:1:18)
are outside the unit circle. In particular, MA(1) is invertible if
jb1j < 1. If the process y(t) has a non-zero mean value m, then the
AR(1) model can be presented in the following form
46
Time Series Analysis

y(t)  m ¼ a1[y(t  1)  m] þ e(t) ¼ c þ a1y(t  1) þ e(t)
(5:1:19)
In (5.1.19), intercept c equals:
c ¼ m(1  a1)
(5:1:20)
The general AR(p) model with a non-zero mean has the following
form
Ap(L)y(t) ¼ c þ e(t), c ¼ m(1  a1  . . . ap)
(5:1:21)
Similarly, the intercept can be included into the general moving
average model MA(q)
y(t) ¼ c þ Bp(L)e(t), c ¼ m
(5:1:22)
Note that mean of the MA model coincides with its intercept because
mean of the white noise is zero.
5.1.3 AUTOCORRELATION AND FORECASTING
Now, let us introduce the autocorrelation function (ACF) for pro-
cess y(t)
r(k) ¼ g(k)=g(0)
(5:1:23)
where g(k) is the autocovariance of order k
g(k) ¼ E[y(t)  m)(y(t  k)  m)]
(5:1:24)
The autocorrelation functions may have some typical patterns, which
can be used for identification of empirical time series [2]. The obvious
properties of ACF are
r(0) ¼ 1,  1 < r(k) < 1 for k 6¼ 0
(5:1:25)
ACF is closely related to the ARMA parameters. In particular, for
AR(1)
r(1) ¼ a1
(5:1:26)
The ACF of the first order for MA(1) equals
r(1) ¼ b1=(b1
2 þ 1)
(5:1:27)
The right-hand side of the expression (5.1.27) has the same value for
the inverse transform b1 ! 1=b1. For example, two processes
Time Series Analysis
47

x(t) ¼ e(t) þ 2e(t  1)
y(t) ¼ e(t) þ 0:5e(t  1)
have the same r(1). Note, however, that y(t) is an invertible process
while x(t) is not.
ARMA modeling is widely used for forecasting. Consider a fore-
cast of a variable y(t þ 1) based on a set of n variables x(t) known at
moment t. This
set can be
just past values of y,
that is,
y(t), y(t  1), . . . , y(t  n þ 1). Let us denote the forecast with
^y(t þ 1jt). The quality of forecast is usually defined with the some
loss function. The mean squared error (MSE) is the conventional loss
function in many applications
MSE(^y(t þ 1jt)) ¼ E[(y(t þ 1)^y(t þ 1jt))2]
(5:1:28)
The forecast that yields the minimum of MSE turns out to be the
expectation of y(t þ 1) conditioned on x(t)
^y(t þ 1jt) ¼ E[y(t þ 1)jx(t)]
(5:1:29)
In the case of linear regression
y(t þ 1) ¼ b0x(t) þ e(t)
(5:1:30)
MSE is reduced to the ordinary least squares (OLS) estimate for b.
For a sample with T observations,
b ¼
X
T
t¼1
x(t)y(t þ 1)=
X
T
t¼1
x(t)x0(t)
(5:1:31)
Another important concept in the time series analysis is the maximum
likelihood estimate (MLE) [2]. Consider the general ARMA model
(5.1.12) with the white noise (4.2.6). The problem is how to estimate
the ARMA parameters on the basis of given observations of y(t). The
idea
of
MLE
is
to
find
such
a
vector
r0 ¼ (a1, . . . , ap, . . . ,
b1, . . . , bq, s2) that maximizes the likelihood function for given ob-
servations (y1, y2, . . . , yT)
f1, 2, . . . , T(y1, y2, . . . , yT; r0)
(5:1:32)
The likelihood function (5.1.32) has the sense of probability of ob-
serving the data sample (y1, y2, . . . , yT). In this approach, the ARMA
model and the probability distribution for the white noise should be
48
Time Series Analysis

specified first. Often the normal distribution leads to reasonable
estimates even if the real distribution is different. Furthermore, the
likelihood function must be calculated for the chosen ARMA model.
Finally, the components of the vector r0 must be estimated. The latter
step may require sophisticated numerical optimization technique.
Details of implementation of MLE are discussed in [2].
5.2 TRENDS AND SEASONALITY
Finding trends is an important part of the time series analysis.
Presence of trend implies that the time series has no mean reversion.
Moreover, mean and variance of a trending process depend on the
sample. The time series with trend is named non-stationary. If a
process y(t) is stationary, its mean, variance, and autocovariance are
finite and do not depend on time. This implies that autocovariance
(5.1.24) depends only on the lag parameter k. Such a definition of
stationarity is also called covariance-stationarity or weak stationarity
because it does not impose any restrictions on the higher moments of
the process. Strict stationarity implies that higher moments also do
not depend on time. Note that any MA process is covariance-station-
ary. However, the AR(p) process is covariance-stationary only if the
roots of its polynomial are outside the unit circle.
It is important to discern deterministic trend and stochastic trend.
They have a different nature yet their graphs may look sometimes
very similar [1]. Consider first the AR(1) model with the deterministic
trend
y(t)  m  ct ¼ a1(y(t  1)  m  c(t  1)) þ e(t)
(5:2:1)
Let us introduce z(t) ¼ y(t)  m  ct. Then equation (5.2.1) has the
solution
z(t) ¼ a1
t z(0) þ
X
t
i¼1
a1
tie(t)
(5:2:2)
where z(0) is a pre-sample starting value of z. Obviously, the random
shocks are transitory if ja1j < 1. The trend incorporated in the defin-
ition of z(t) is deterministic when ja1j < 1. However, if a1 ¼ 1, then
equation (5.2.1) has the form
Time Series Analysis
49

y(t) ¼ c þ y(t  1) þ e(t)
(5:2:3)
The process (5.2.3) is named the random walk with drift. In this case,
equation (5.2.2) is reduced to
z(t) ¼ z(0) þ
X
t
i¼1
e(t)
(5:2:4)
The sum of non-transitory shocks in the right-hand side of equation
(5.2.4) is named stochastic trend. Consider, for example, the determin-
istic trend model with m ¼ 0 and e(t) ¼ N(0, 1)
y(t) ¼ 0:1t þ e(t)
(5:2:5)
and the stochastic trend model
y(t) ¼ 0:1 þ y(t  1) þ e(t), y(0) ¼ 0
(5:2:6)
As it can be seen from Figure 5.1, both graphs look similar. In
general, however, the stochastic trend model can deviate from the
deterministic trend for a long time.
Stochastic trend implies that the process is I(1). Then the lag
polynomial (5.1.3) can be represented in the form
y(t)
0
1
2
3
4
5
6
7
0
10
20
30
40
t
B
A
Figure 5.1 Deterministic and stochastic trends: A - equation (5.2.5), B -
equation (5.2.6).
50
Time Series Analysis

Ap(L) ¼ (1  L)Ap1(L)
(5:2:7)
Similarly, the process I(2) has the lag polynomial
Ap(L) ¼ (1  L)2Ap2(L)
(5:2:8)
and so on. The standard procedure for testing presence of the unit
root in time series is the Dickey-Fuller method [1, 2]. This method is
implemented in major econometric software packages (see the Section
5.5).
Seasonal effects may play an important role in the properties of time
series. Sometimes, there is a need to eliminate these effects in order to
focus on the stochastic specifics of the process. Various differencing
filters can be used for achieving this goal [2]. In other cases, seasonal
effect itself may be the object of interest. The general approach for
handling seasonal effects is introducing dummy parameters D(s, t)
where s ¼ 1, 2, . . . , S; S is the number of seasons. For example,
S ¼ 12 is used for modeling the monthly effects. Then the parameter
D(s, t) equals 1 at a specific season s and equals zero at all other
seasons. The seasonal extension of an ARMA(p,q) model has the
following form
y(t) ¼ a1y(t  1) þ a2y(t  2) þ . . . þ apy(t  p) þ e(t)
þb1e(t  1) þ b2e(t  2) þ . . . þ bqe(t  q) þ
X
S
s¼1
dsD(s, t)
(5:2:9)
Note that forecasting with the model (5.2.9) requires estimating
(p þ q þ S) parameters.
5.3 CONDITIONAL HETEROSKEDASTICITY
So far, we considered random processes with the white noise (4.2.6)
that are characterized with constant unconditional variance. Condi-
tional variance has not been discussed so far. In general, the processes
with unspecified conditional variance are named homoskedastic.
Many random time series are not well described with the IID process.
In particular, there may be strong positive autocorrelation in squared
asset returns. This means that large returns (either positive or nega-
tive) follow large returns. In this case, it is said that the return
Time Series Analysis
51

volatility is clustered. The effect of volatility clustering is also called
autoregressive conditional heteroskedasticity (ARCH). It should be
noted that small autocorrelation in squared returns does not neces-
sarily mean that there is no volatility clustering. Strong outliers that
lead to high values of skewness and kurtosis may lower autocorrela-
tion. If these outliers are removed from the sample, volatility cluster-
ing may become apparent [3].
Several models in which past shocks contribute to the current
volatility have been developed. Generally, they are rooted in the
ARCH(m) model where the conditional variance is a weighed sum
of m squared lagged returns
s2(t) ¼ v þ a1e2(t  1) þ a2e2(t  2) þ . . . þ ame2(t  m)
(5:3:1)
In (5.3.1), e(t)  N(0, s2(t)), v > 0, a1, . . . , am  0. Unfortunately,
application of the ARCH(m) process to modeling the financial time
series often requires polynomials with high order m. A more efficient
model is the generalized ARCH (GARCH) process. The GARCH
(m, n) process combines the ARCH(m) process with the AR(n) pro-
cess for lagged variance
s2(t) ¼ v þ a1e2(t  1) þ a2e2(t  2) þ . . . þ ame2(t  m)
þ b1s2(t  1) þ b2s2(t  2) þ . . . þ bns2(t  n)
(5:3:2)
The simple GARCH(1, 1) model is widely used in applications
s2(t) ¼ v þ ae2(t  1) þ bs2(t  1)
(5:3:3)
Equation (5.3.3) can be transformed into
s2(t) ¼ v þ (a þ b)s2(t  1) þ a[e2(t)  s2(t  1)]
(5:3:4)
The last term in equation (5.3.4) is conditioned on information avail-
able at time (t  1) and has zero mean. This term can be treated as a
shock to volatility. Therefore, the unconditional expectation of vola-
tility for the GARCH(1, 1) model equals
E[s2(t)] ¼ v=(1  a  b)
(5:3:5)
This implies that the GARCH(1, 1) process is weakly stationary when
a þ b < 1. The advantage of the stationary GARCH(1, 1) model is
that it can be easily used for forecasting. Namely, the conditional
expectation of volatility at time (t þ k) equals [4]
52
Time Series Analysis

E[s2(t þ k)] ¼ (a þ b)k[s2(t)  v=(1  a  b)] þ v=(1  a  b)
(5:3:6)
The GARCH(1, 1) model (5.3.4) can be rewritten as
s2(t) ¼ v=(1  b) þ a(e2(t  1) þ be2(t  2) þ b2e2(t  3) þ . . . ) (5:3:7)
Equation (5.3.7) shows that the GARCH(1, 1) model is equivalent to
the infinite ARCH model with exponentially weighed coefficients.
This explains why the GARCH models are more efficient than the
ARCH models.
Several GARCH models have been described in the econometric
literature [1–3]. One popular GARCH(1, 1) model with a þ b ¼ 1 is
called integrated GARCH (IGARCH). It has the autoregressive unit
root. Therefore volatility of this process follows random walk and can
be easily forecasted
E[s2(t þ k)] ¼ s2(t) þ kv
(5:3:8)
IGARCH can be presented in the form
s2(t) ¼ v þ (1  l)e2(t  1) þ ls2(t  1)
(5:3:9)
where 0 < l < 1. If v ¼ 0, IGARCH coincides with the exponentially
weighed moving average (EWMA)
s2(t) ¼ (1  l)
X
n
i¼1
li1e2(t  i)
(5:3:10)
Indeed, the n-period EWMA for a time series y(t) is defined as
z(t) ¼ [y(t  1) þ ly(t  2) þ l2y(t  3) þ . . .þ
ln1y(t  n)]=(1 þ l þ . . . þ ln)
(5:3:11)
where 0 < l < 1. For large n, the denominator of (5.3.11) converges
to 1=(1  l). Then for z(t) ¼ s2(t) and y(t) ¼ e2(t), equation (5.3.11) is
equivalent to equation (5.3.7) with v ¼ 0.
The GARCH models discussed so far are symmetric in that the
shock sign does not affect the resulting volatility. In practice, how-
ever, negative price shocks influence volatility more than the positive
shocks. A noted example of the asymmetric GARCH model is the
exponential GARCH (EGARCH) (see, e.g., [3]). It has the form
log [s2(t)] ¼ v þ b log [s2(t  1)] þ lz(t  1)þ
g(jz(t  1)j 
ffiffiffiffiffiffiffiffi
2=p
p
)
(5:3:12)
Time Series Analysis
53

where z(t) ¼ e(t)=s(t). Note that E[z(t)] ¼
ffiffiffiffiffiffiffiffi
2=p
p
. Hence, the last term
in (5.3.12) is the mean deviation of z(t). If g > 0 and l < 0, negative
shocks lead to higher volatility than positive shocks.
5.4 MULTIVARIATE TIME SERIES
Often the current value of a variable depends not only on its past
values, but also on past and/or current values of other variables.
Modeling of dynamic interdependent variables is conducted with
multivariate time series. The multivariate models yield not only new
implementation problems but also some methodological difficulties.
In particular, one should be cautious with simple regression models
y(t) ¼ ax(t) þ e(t)
(5:4:1)
that may lead to spurious results. It is said that (5.4.1) is a simultan-
eous equation as both explanatory (x) and dependent (y) variables are
present at the same moment of time. A notorious example for spuri-
ous inference is the finding that the best predictor in the United
Nations database for the Standard & Poor’s 500 stock index is
production of butter in Bangladesh [5].
A statistically sound yet spurious relationship is named data
snooping. It may appear when the data being the subject of research
are used to construct the test statistics [4]. Another problem with
simultaneous equations is that noise can be correlated with the ex-
planatory variable, which leads to inaccurate OLS estimates of the
regression coefficients. Several techniques for handling this problem
are discussed in [2].
A multivariate time series y(t) ¼ (y1(t), y2(t), . . . , yn(t))0 is a vector
of n processes that have data available for the same moments of time.
It is supposed also that all these processes are either stationary or
have the same order of integration. In practice, the multivariate
moving average models are rarely used due to some restrictions [1].
Therefore, we shall focus on the vector autoregressive model (VAR)
that is a simple extension of the univariate AR model to multivariate
time series. Consider a bivariate VAR(1) process
y1(t) ¼ a10 þ a11y1(t  1) þ a12y2(t  1) þ e1(t)
y2(t) ¼ a20 þ a21y1(t  1) þ a22y2(t  1) þ e2(t)
(5:4:2)
54
Time Series Analysis

that can be presented in the matrix form
y(t) ¼ a0 þ Ay(t  1) þ «(t)
(5:4:3)
In (5.4.3), y(t) ¼ (y1(t), y2(t))0, a0 ¼ (a10, a20)0, «(t) ¼ (e1(t), e2(t))0,
and A ¼
a11
a12
a21
a22


.
The right-hand sides in example (5.4.2) depend on past values only.
However, dependencies on current values can also be included (so-
called simultaneous dynamic model [1]). Consider the modification of
the bivariate process (5.4.2)
y1(t) ¼ a11y1(t  1) þ a12y2(t) þ e1(t)
y2(t) ¼ a21y1(t) þ a22y2(t  1) þ e2(t)
(5:4:4)
The matrix form of this process is
1
a12
a21
1


y1(t)
y2(t)


¼
a11
0
0
a22


y1(t  1)
y2(t  1)


þ
e1(t)
e2(t)


(5:4:5)
Multiplying both sides of (5.4.5) with the inverse of the left-hand
matrix yields
y1(t)
y2(t)


¼ (1  a12a21)1
a11
a12a22
a11a21
a22

 y1(t  1)
y2(t  1)


þ (1  a12a21)1
1
a12
a21
1

 e1(t)
e2(t)


(5:4:6)
Equation (5.4.6) shows that the simultaneous dynamic models can
also be represented in the VAR form.
In the general case of n-variate time series, VAR(p) has the form [2]
y(t) ¼ a0 þ A1y(t  1) þ . . . þ Apy(t  p) þ «(t)
(5:4:7)
where y(t), a0, and «(t) are n-dimensional vectors and Ai(i ¼ 1, . . . , p)
are n x n matrices. Generally, the white noises «(t) are mutually
independent. Let us introduce
Ap(L) ¼ In  A1L  . . .  ApLp
(5:4:8)
where In is the n-dimensional unit vector. Then equation (5.4.7) can
be presented as
Time Series Analysis
55

Ap(L)y(t) ¼ a0 þ «(t)
(5:4:9)
Two covariance-stationary processes x(t) and y(t) are jointly covar-
iance-stationary if their covariance Cov(x(t), y(t  s)) depends on lag
s only. The condition for the covariance-stationary VAR(p) is the
generalization of (5.1.11) for AR(p). Namely, all values of z satisfying
the equation
jIn  A1z  . . .  Apzpj ¼ 0
(5:4:10)
must lie outside the unit circle. Equivalently, all solutions of the
equation
jInlp  A1lp1  . . .  Apj ¼ 0
(5:4:11)
must satisfy the condition jlj < 1.
The problem of whether the lagged values of process y can improve
prediction of process x (so-called Granger causality) is often posed in
forecasting. It is said that if y fails to Granger-cause x, then the
following condition holds for all s > 0
MSE(E[x(t þ s)jx(t), x(t  1), . . . ]) ¼
MSE(E[x(t þ s)jx(t), x(t  1), . . . , y(t), y(t  1), . . . ])
(5:4:12)
In this case, y is called exogenous variable with respect to x. For
example, y2(t) is exogenous with respect to y1(t) in (5.4.2) if a12 ¼ 0.
General methods for testing the Granger causality are described in [2].
The last notion that is introduced in this section is cointegration.
Two processes are cointegrated if they both have unit roots (i.e., they
both are I(1) ), but some linear combination of these processes is
stationary (i.e., is I(0) ). This definition can be extended to an arbi-
trary number of processes. As an example, consider a bivariate model
y1(t) ¼ ay2(t) þ e1(t)
y2(t) ¼ y2(t  1) þ e2(t)
(5:4:13)
Both processes y1(t) and y2(t) are random walks. However the process
z(t) ¼ y1(t)  ay2(t)
(5:4:14)
is stationary. Details of testing the integration hypothesis are de-
scribed in [2]. Implications of cointegration in financial data analysis
are discussed in [3].
56
Time Series Analysis

5.5 REFERENCES FOR FURTHER READING
AND ECONOMETRIC SOFTWARE
A good concise introduction into the time series analysis is given by
Franses [1]. The comprehensive presentation of the subject can be
found in monographs by Hamilton [2] and Green [6]. Important
specifics of time series analysis in finance, particularly for analysis
and forecasting of volatility, are discussed by Alexander in [3]. In this
chapter, only time series on homogenous grids were considered. Spe-
cifics of analysis of tick-by-tick data on non-homogenous grids are
discussed in [7]. It should be noted that the exercises with the econo-
metric software packages are very helpful for learning the subject.
Besides the generic scientific software such as SAS, Splus, and Matlab
that have modules for the time series analysis, several econometric
software packages are available: PCGive, RATS, Shazam, and TSP.
While these packages may have the trial and student versions, Easy-
Reg offered by H. J. Bierens5 has sufficient capability for an intro-
ductory course and is free of charge.
5.6 EXERCISES
1. Verify equations (5.1.25)–(5.1.27).
2. Verify
if
the
process
y(t) ¼ 1:2y(t  1)  0:32y(t  2) þ e(t)
(where e(t) is IID) is covariance-stationary.
3. Estimate the linear dividend growth rate from the dividends
paid in the last years (verify these data on the AMEX website:
http://www.amex.com): 2000 – $1.51, 2001 – $1.42, 2002 – $1.50,
and 2003 – $1.63.
4. Verify equation (5.4.6) for the processes (5.4.4).
Time Series Analysis
57

This page intentionally left blank 


## Fractals

Chapter 6
Fractals
In short, fractals are the geometric objects that are constructed by
repeating geometric patterns at a smaller and smaller scale. The
fractal theory is a beautiful theory that describes beautiful objects.
Development of the fractal theory and its financial applications has
been greatly influenced by Mandelbrot [1]. In this chapter, a short
introduction to the fractal theory relevant to financial applications is
given. In Section 6.1, the basic definitions of the fractal theory are
provided. Section 6.2 is devoted to the concept of multifractals that
has been receiving a lot of attention in the recent research of the
financial time series.
6.1 BASIC DEFINITIONS
Self-similarity is the defining property of fractals. This property
implies that the geometric patterns are isotropic, meaning shape
transformations along all coordinate axes are the same. If the geo-
metric patterns are not isotropic, say the object is contracted along
the y-axis with a scale different from that of along the x-axis, it is said
that the object is self-affine. The difference between self-similarity and
self-affinity is obvious for geometric objects. However, only self-
affinity is relevant for the graphs of financial time series [1]. Indeed,
since time and prices are measured with different units, their scaling
factors cannot be compared.
59

If the geometric pattern used in fractal design is deterministic, the
resulting object is named a deterministic fractal. Consider an example
in path (a) of Figure 6.1 where a square is repeatedly divided into nine
small squares and four of them that have even numbers are deleted
(the squares are numerated along rows). If four squares are deleted at
random, one obtains a random fractal (one of such fractals is depicted
in path (b) of Figure 6.1). While the deterministic and stochastic
fractals in Figure 6.1 look quite different, they have the same fractal
dimension. Let us outline the physical sense of this notion.
Consider a jagged line, such as a coastline. It is embedded into a
plane. Thus, its dimension is lower than two. Yet, the more zigzagged
the line is, the greater part of plane it covers. One may then expect
that the dimension of a coastline is higher than one and it depends on
a measure of jaggedness. Another widely used example is a crumpled
paper ball. It is embedded in three-dimensional space. Yet, the
(a)
(b)
Figure 6.1 Deterministic (a) and stochastic (b) fractals with the same
fractal dimension D ¼ ln(5)/ln(3).
60
Fractals

volume of a paper ball depends on the sizes of its creases. Therefore,
its dimension is expected to be in the range of two to three. Thus, we
come to the notion of the fractal (non-integer) dimension for objects
that cannot be accurately described within the framework of Eucli-
dian geometry.
There are several technical definitions for the fractal dimension [2].
The most popular one is the box-counting dimension. It implies map-
ping the grid boxes of size h (e.g., squares and cubes for the two-
dimensional and the three-dimensional spaces, respectively) onto the
object of interest. The number of boxes that fill the object is
N(h)  hD. The fractal dimension D is then the limit
D ¼ lim
h!0 [ ln N(h)= ln (1=h)]
(6:1:1)
The box-counting dimension has another equivalent definition with
the fixed unit size of the grid box and varying object size L
D ¼ lim
L!1 [ ln N(L)= ln (L)]
(6:1:2)
The fractal dimension for both deterministic and stochastic fractals in
Figure 6.1 equals D ¼ ln (5)= ln (3)  1:465. Random fractals exhibit
self-similarity only in a statistical sense. Therefore, the scale invari-
ance is a more appropriate concept for random fractals than self-
similarity.
The iterated function systems are commonly used for generating
fractals. The two-dimensional iterated function algorithm for N fixed
points can be presented as
X(k þ 1) ¼ rX(k) þ (1  r)XF(i)
Y(k þ 1) ¼ rY(k) þ (1  r)YF(i)
(6:1:3)
In (6.1.3), r is the scaling parameter; XF(i) and YF(i) are the coordin-
ates of the fixed point i; i ¼ 1, 2, . . . N. The fixed point i is selected at
every iteration at random. A famous example with N ¼ 3, the Sier-
pinski triangle, is shown in Figure 6.2.
Now, let us turn to the random processes relevant to financial time
series. If a random process X(t) is self-affine, then it satisfies the
scaling rule
X(ct) ¼ cHX(t)
(6:1:4)
Fractals
61

The parameter H is named the Hurst exponent. Let us introduce the
fractional Brownian motion BH(t). This random process satisfies
the following conditions for all t and T [1]
E[BH(t þ T)  BH(t)] ¼ 0,
(6:1:5)
E[BH(t þ T)  BH(t)]2 ¼ T2H
(6:1:6)
When H ¼ 1⁄2, the fractional Brownian motion is reduced to the
regular Brownian motion. For the Brownian motion, the correlation
between the past average E[BH(t)  BH(t  T)]=T and the future aver-
age E[BH(t þ T) BH(t)]=T equals
C ¼ 22H1  1
(6:1:7)
Obviously, this correlation does not depend on T. If 1⁄2 < H < 1, then
C > 0 and it is said that BH(t) is a persistent process. Namely, if BH(t)
grew in the past, it will most likely grow in the immediate future.
Figure 6.2 The Sierpinski triangle with r ¼ 0:5.
62
Fractals

Conversely, if BH(t) decreased in the past, it will most probably
continue to fall. Thus, persistent processes maintain trend. In the
opposite case (0 < H < 1⁄2, C < 0), the process is named anti-persist-
ent. It is said also that anti-persistent processes are mean reverting; for
example, if the current process innovation is positive, then the next
one will most likely be negative, and vice versa. There is a simple
relationship between the box-counting fractal dimension and the
Hurst exponent
D ¼ 2  H
(6:1:8)
The fractal dimension of a time series can be estimated using the
Hurst’s rescaled range (R/S) analysis [1, 3]. Consider the data set
xi(i ¼ 1, . . . N) with mean mN and the standard deviation sN. To
define the rescaled range, the partial sums Sk must be calculated
Sk ¼
X
k
i¼1
(xi  mN), 1  k  N
(6:1:9)
The rescaled range equals
R=S ¼ [ max (Sk)  min (Sk)]=sN, 1  k  N
(6:1:10)
The value of R/S is always greater than zero since max (Sk) > 0 and
min (Sk) < 0. For given R/S, the Hurst exponent can be estimated
using the relation
R=S ¼ (aN)H
(6:1:11)
where a is a constant. The R/S analysis is superior to many other
methods of determining long-range dependencies. But this approach
has a noted shortcoming, namely, high sensitivity to the short-range
memory [4].
6.2 MULTIFRACTALS
Let us turn to the generic notion of multifractals (see, e.g., [5]).
Consider the map filled with a set of boxes that are used in the box-
counting fractal dimension. What matters for the fractal concept is
whether the given box belongs to fractal. The basic idea behind the
notion of multifractals is that every box is assigned a measure m
that characterizes some probability density (e.g., intensity of color
Fractals
63

between the white and black limits). The so-called multiplicative
process (or cascade) defines the rule according to which measure is
fragmented when the object is partitioned into smaller components.
The fragmentation ratios that are used in this process are named
multipliers. The multifractal measure is characterized with the Ho¨lder
exponent a
a ¼ lim
h!0 [ ln m(h)= ln (h)]
(6:2:1)
where h is the box size. Let us denote the number of boxes with given
h and a via Nh(a). The distribution of the Ho¨lder exponents in the
limit h ! 0 is sometimes called the multifractal spectrum
f(a) ¼  lim
h!0 [ ln Nh(a)= ln (h)]
(6:2:2)
The distribution f(a) can be treated as a generalization of the fractal
dimension for the multifractal processes.
Let us describe the simplest multifractal, namely the binomial
measure m on the interval [0, 1] (see [5] for details). In the binomial
cascade, two positive multipliers, m0 and m1, are chosen so that
m0 þ m1 ¼ 1. At the step k ¼ 0, the uniform probability measure
for mass distribution, m0 ¼ 1, is used. At the next step (k ¼ 1), the
measure m1 uniformly spreads mass in proportion m0=m1 on the
intervals [0, 1⁄2 ] and [1⁄2 , 1], respectively. Thus, m1[0, 1⁄2 ] ¼ m0 and
m1[ 1⁄2 , 1] ¼ m1. In the next steps, every interval is again divided into
two subintervals and the mass of the interval is distributed between
subintervals in proportion m0=m1. For example, at k ¼ 2: m2[0, 1⁄4]
¼ m0m0, m2[ 1⁄4, 1⁄2] ¼ m2[1⁄2, 3⁄4] ¼ m0m1, m2[3⁄4, 1] ¼ m1m1 and so on.
At the kth iteration, mass is partitioned into 2k intervals of length 2k.
Let us introduce the notion of the binary expansion 0:b1b2 . . . bk for
the
point
x ¼ b121 þ b222 þ bk2k
where
0  x  1
and
0 < bk < 1. Then the measure for every dyadic interval I0b1b2 : : : bk of
length 2k equals
m0b1b2 : : : bk ¼
Y
k
i¼1
mbi ¼ m0nm1kn
(6:2:3)
where n is the number of digits 0 in the address 0_b1b2 . . . bk of the
interval’s left end, and (k  n) is the number of digits 1. Since the
subinterval mass is preserved at every step, the cascade is called
64
Fractals

conservative or microcanonical. The first five steps of the binomial
cascade with m0 ¼ 0:6 are depicted in Figure 6.3.
The multifractal spectrum of the binomial cascade equals
f(a) ¼  amax  a
amax  amin
log2
amax  a
amax  amin



a  amin
amax  amin
log2
a  amin
amax  amin


(6:2:4)
The distribution (6.2.4) is confined with the interval [amin, amax]. If
m0  0:5, then amin ¼  log2 (m0) and amax ¼  log2 (1  m0). The
binomial cascade can be generalized in two directions. First, one
can introduce a multinomial cascade by increasing the number of
subintervals to N > 2. Note that the condition
X
N1
0
mi ¼ 1
(6:2:5)
(a)
0
0.5
1
1.5
2
2.5
3
1 3 5 7 9 1113151719212325272931
3 5 7 9 11 13 15 17 19 21 23 25 27 29
1
31
(b)
0
0.5
1
1.5
2
2.5
3
(c)
0
0.5
1
1.5
2
2.5
3
1 4
7
10 13 16 19 22 25
28 31
1
4
7
10 13 16 19 22 25 28 31
(d)
0
0.5
1
1.5
2
2.5
3
3 5 7 9 11 13 15 17 19 21 23 25 27 29
1
31
(e)
0
0.5
1
1.5
2
2.5
3
(f)
0
0.5
1
1.5
2
2.5
3
1 3 5 7 9 1113151719212325272931
Figure 6.3 Binomial cascade with m0 ¼ 0.6: a) k ¼ 0, b) k ¼ 1, c) k ¼ 2, d)
k ¼ 3, e) k ¼ 4, f) k ¼ 5.
Fractals
65

is needed for preserving the conservative character of the cascade.
Secondly, the values of mi can be randomized rather than assigned
fixed values. A cascade with randomized mi is called canonical. In this
case, the condition (6.2.5) is satisfied only on average, that is
E
X
N1
0
mi
"
#
¼ 1
(6:2:6)
An example of the randomized cascade that has an explicit expres-
sion for the multifractal spectrum is the lognormal cascade [6]. In this
process, the multiplier that distributes the mass of the interval, M, is
determined with the lognormal distribution (i.e., log2 (M) is drawn
from the Gaussian distribution). If the Gaussian mean and variance
are l and s, respectively, then the conservative character of the
cascade E[M] ¼ 0.5 is preserved when
s2 ¼ 2(l  1)= ln (2)
(6:2:7)
The multifractal spectrum of the lognormal cascade that satisfies
(6.2.7) equals
f(a) ¼ 1  (a  l)2
4(l  1)
(6:2:8)
Note that in contrast to the binomial cascade, the lognormal
cascade may yield negative values of f(a), which requires interpret-
ation of f(a) other than the fractal dimension.
Innovation of multifractal process, DX ¼ X(t þ Dt)  X(t), is de-
scribed with the scaling rule
E[ (DX)
j
jq] ¼ c(q)(Dt)t(q)þ1
(6:2:9)
where c(q) and t(q) (so-called scaling function) are deterministic func-
tions of q. It can be shown that the scaling function t(q) is always
concave. Obviously, t(0) ¼ 1. A self-affine process (6.1.4) can be
treated as a multifractal process with t(q) ¼ Hq  1. In particular, for
the Wiener processes, H ¼ 1⁄2 and tw(q) ¼ q=2  1. The scaling func-
tion of the binomial cascade can be expressed in terms of its multi-
pliers
t(q) ¼ log2(m0
q þ m1
q)
(6:2:10)
66
Fractals

The scaling function t(q) is related to the multifractal spectrum f(a)
via the Legendre transformation
t(q) ¼ min
a [qa  f(a)]
(6:2:11)
which is equivalent to
f(a) ¼ arg min
q [qa  t(q)]
(6:2:12)
Note that f(a) ¼ q(a  H) þ 1 for the self-affine processes.
In practice, the scaling function of a multifractal process X(t) can
be calculated using so-called partition function
Sq(T, Dt) ¼
X
N1
i ¼ 0
X(t þ Dt)  X(t)
j
jq
(6:2:13)
where the sample X(t) has N points within the interval [0, T] with the
mesh size Dt. It follows from (6.2.9) that
log {E[Sq(T, Dt)]} ¼ t(q) log (Dt) þ c(q) log T
(6:2:14)
Thus, plotting log {E[Sq(T, Dt)]} against log (Dt) for different values
of q reveals the character of the scaling function t(q). Multifractal
models have become very popular in analysis of the financial time
series. We shall return to this topic in Section 8.2
6.3 REFERENCES FOR FURTHER READING
The Mandelbrot’s work on scaling in the financial time series is
compiled in the collection [1]. Among many excellent books on frac-
tals, we choose [2] for its comprehensive material that includes a
description of relations between chaos and fractals and an important
chapter on multifractals [5].
6.4 EXERCISES
*1. Implement an algorithm that draws the Sierpinski triangle with
r ¼ 0:5 (see Figure 6.2).
Hint: Choose the following fixed points: (0, 0), (0, 100), (100,
0). Use the following method for the randomized choice of the
Fractals
67

fixed point: i ¼ [10 rand()] %3 where rand() is the uniform
distribution within [0, 1] and % is modulus (explain the ration-
ale behind this method). Note that at least 10000 iterations are
required for a good-quality picture.
*2. Reproduce the first five steps of the binomial cascade with
m0 ¼ 0:6 (see Figure 6.3). How will this cascade change if
m0 ¼ 0:8?
68
Fractals


## Nonlinear Dynamical Systems

Chapter 7
Nonlinear Dynamical Systems
7.1 MOTIVATION
It is well known that many nonlinear dynamical systems, including
seemingly simple cases, can exhibit chaotic behavior. In short, the
presence of chaos implies that very small changes in the initial condi-
tions or parameters of a system can lead to drastic changes in its
behavior. In the chaotic regime, the system solutions stay within the
phase space region named strange attractor. These solutions never
repeat themselves; they are not periodic and they never intersect.
Thus, in the chaotic regime, the system becomes unpredictable. The
chaos theory is an exciting and complex topic. Many excellent books
are devoted to the chaos theory and its applications (see, e.g., refer-
ences in Section 7.7). Here, I only outline the main concepts that may
be relevant to quantitative finance.
The first reason to turn to chaotic dynamics is a better understand-
ing of possible causes of price randomness. Obviously, new infor-
mation coming to the market moves prices. Whether it is a
company’s performance report, a financial analyst’s comments, or a
macroeconomic event, the company’s stock and option prices may
change, thus reflecting the news. Since news usually comes unexpect-
edly, prices change in unpredictable ways.1 But is new information the
only source reason for price randomness? One may doubt this while
observing the price fluctuations at times when no relevant news is
69

released. A tempting proposition is that the price dynamics can be
attributed in part to the complexity of financial markets. The possi-
bility that the deterministic processes modulate the price variations
has a very important practical implication: even though these pro-
cesses can have the chaotic regimes, their deterministic nature means
that prices may be partly forecastable. Therefore, research of chaos in
finance and economics is accompanied with discussion of limited
predictability of the processes under investigation [1].
There have been several attempts to find possible strange attractors
in the financial and economic time series (see, e.g., [1–3] and refer-
ences therein). Discerning the deterministic chaotic dynamics from a
‘‘pure’’ stochastic process is always a non-trivial task. This problem is
even more complicated for financial markets whose parameters may
have non-stationary components [4]. So far, there has been little (if
any) evidence found of low-dimensional chaos in financial and eco-
nomic time series. Still, the search of chaotic regimes remains an
interesting aspect of empirical research.
There is also another reason for paying attention to the chaotic
dynamics. One may introduce chaos inadvertently while modeling
financial or economic processes with some nonlinear system. This
problem is particularly relevant in agent-based modeling of financial
markets where variables generally are not observable (see Chapter
12). Nonlinear continuous systems exhibit possible chaos if their
dimension exceeds two. However, nonlinear discrete systems (maps)
can become chaotic even in the one-dimensional case. Note that the
autoregressive models being widely used in analysis of financial time
series (see Section 5.1) are maps in terms of the dynamical systems
theory. Thus, a simple nonlinear expansion of a univariate autore-
gressive map may lead to chaos, while the continuous analog of this
model is perfectly predictable. Hence, understanding of nonlinear
dynamical effects is important not only for examining empirical
time series but also for analyzing possible artifacts of the theoretical
modeling.
This chapter continues with a widely popular one-dimensional
discrete model, the logistic map, which illustrates the major concepts
in the chaos theory (Section 7.2). Furthermore, the framework for the
continuous systems is introduced in Section 7.3. Then the three-
dimensional Lorenz model, being the classical example of the low-
70
Nonlinear Dynamical Systems

dimensional continuous chaotic system, is described (Section 7.4).
Finally, the main pathways to chaos and the chaos measures are
outlined in Section 7.5 and Section 7.6, respectively.
7.2 DISCRETE SYSTEMS: THE LOGISTIC MAP
The logistic map is a simple discrete model that was originally used
to describe the dynamics of biological populations (see, e.g., [5] and
references therein). Let us consider a variable number of individuals
in a population, N. Its value at the k-th time interval is described with
the following equation
Nk ¼ ANk1  BNk1
2
(7:2:1)
Parameter A characterizes the population growth that is determined
by such factors as food supply, climate, etc. Obviously, the popula-
tion grows only if A > 1. If there are no restrictive factors (i.e., when
B ¼ 0), the growth is exponential, which never happens in nature for
long. Finite food supply, predators, and other causes of mortality
restrict the population growth, which is reflected in factor B. The
maximum value of Nk equals Nmax ¼ A=B. It is convenient to intro-
duce the dimensionless variable Xk ¼ Nk=Nmax. Then 0  Xk  1,
and equation (7.2.1) has the form
Xk ¼ AXk1(1  Xk1)
(7:2:2)
A generic discrete equation in the form
Xk ¼ f(Xk1)
(7:2:3)
is called an (iterated) map, and the function f(Xk1) is called the
iteration function. The map (7.2.2) is named the logistic map. The
sequence of values Xk that are generated by the iteration procedure
is called a trajectory. Trajectories depend not only on the iteration
function but also on the initial value X0. Some initial points turn out
to be the map solution at all iterations. The value X that satisfies the
equation
X ¼ f(X)
(7:2:4)
is named the fixed point of the map. There are two fixed points for the
logistic map (7.2.2):
Nonlinear Dynamical Systems
71

X
1 ¼ 0, and X
2 ¼ (A  1)=A
(7:2:5)
If A  1, the logistic map trajectory approaches the fixed point X
1
from any initial value 0  X0  1. The set of points that the trajec-
tories tend to approach is called the attractor. Generally, nonlinear
dynamical systems can have several attractors. The set of initial values
from which the trajectories approach a particular attractor are called
the basin of attraction. For the logistic map with A < 1, the attractor
is X
1 ¼ 0, and its basin is the interval 0  X0  1.
If 1 < A < 3, the logistic map trajectories have the attractor
X
2 ¼ (A  1)=A and its basin is also 0  X0  1. In the mean time,
the point X
1 ¼ 0 is the repellent fixed point, which implies that any
trajectory that starts near X
1 tends to move away from it.
A new type of solutions to the logistic map appears at A > 3.
Consider the case with A ¼ 3:1: the trajectory does not have a single
attractor but rather oscillates between two values, X  0:558 and
X  0:764. In the biological context, this implies that the growing
population overexerts its survival capacity at X  0:764. Then the
population shrinks ‘‘too much’’ (i.e., to X  0:558), which yields
capacity for further growth, and so on. This regime is called period-
2. The parameter value at which solution changes qualitatively is
named the bifurcation point. Hence, it is said that the period-doubling
bifurcation occurs at A ¼ 3. With a further increase of A, the oscilla-
tion amplitude grows until A approaches the value of about 3.45. At
higher values of A, another period-doubling bifurcation occurs
(period-4). This implies that the population oscillates among four
states with different capacities for further growth. Period doubling
continues with rising A until its value approaches 3.57. Typical tra-
jectories for period-2 and period-8 are given in Figure 7.1. With
further growth of A, the number of periods becomes infinite, and
the system becomes chaotic. Note that the solution to the logistic map
at A > 4 is unbounded.
Specifics of the solutions for the logistic map are often illustrated
with the bifurcation diagram in which all possible values of X are
plotted against A (see Figure 7.2). Interestingly, it seems that there is
some order in this diagram even in the chaotic region at A > 3:6. This
order points to the fractal nature of the chaotic attractor, which will
be discussed later on.
72
Nonlinear Dynamical Systems

0.25
0.35
0.45
0.55
0.65
0.75
0.85
0.95
1
11
21
31
41
k
Xk
A = 2.0
A = 3.1
A = 3.6
Figure 7.1 Solution to the logistic map at different values of the
parameter A.
0
X
3
A
4
1
Figure 7.2 The bifurcation diagram of the logistic map in the parameter
region 3  A < 4.
Nonlinear Dynamical Systems
73

Another manifestation of universality that may be present in cha-
otic processes is the Feigenbaum’s observation of the limiting rate at
which the period-doubling bifurcations occur. Namely, if An is the
value of A at which the period-2n occurs, then the ratio
dn ¼ (An  An1)=(Anþ1  An)
(7:2:6)
has the limit
lim
n!1 dn ¼ 4:669 . . . :
(7:2:7)
It turns out that the limit (7.2.7) is valid for the entire family of maps
with the parabolic iteration functions [5].
A very important feature of the chaotic regime is extreme sensitiv-
ity of trajectories to the initial conditions. This is illustrated with
Figure 7.3 for A ¼ 3:8. Namely, two trajectories with the initial
conditions X0 ¼ 0:400 and X0 ¼ 0:405 diverge completely after 10
0
0.2
0.4
0.6
0.8
1
1
11
21
k
Xk
X0 = 0.4
X0 = 0.405
Figure 7.3 Solution to the logistic map for A ¼ 3.8 and two initial condi-
tions: X0 ¼ 0:400 and X0 ¼ 0:405.
74
Nonlinear Dynamical Systems

iterations. Thus, the logistic map provides an illuminating example of
complexity and universality generated by interplay of nonlinearity
and discreteness.
7.3 CONTINUOUS SYSTEMS
While the discrete time series are the convenient framework for
financial data analysis, financial processes are often described using
continuous presentation [6]. Hence, we need understanding of the
chaos specifics in continuous systems. First, let us introduce several
important notions with a simple model of a damped oscillator (see,
e.g., [7]). Its equation of motion in terms of the angle of deviation
from equilibrium, u, is
d2u
dt2 þ g du
dt þ v2u ¼ 0
(7:3:1)
In (7.3.1), g is the damping coefficient and v is the angular frequency.
Dynamical systems are often described with flows, sets of coupled
differential equations of the first order. These equations in the vector
notations have the following form
dX
dt ¼ F(X(t)), X ¼ (X1, X2, . . . XN)0
(7:3:2)
We shall consider so-called autonomous systems for which the func-
tion F in the right-hand side of (7.3.2) does not depend explicitly on
time. A non-autonomous system can be transformed into an autono-
mous one by treating time in the function F(X, t) as an additional
variable, XNþ1 ¼ t, and adding another equation to the flow
dXNþ1
dt
¼ 1
(7:3:3)
As a result, the dimension of the phase space increases by one. The
notion of the fixed point in continuous systems differs from that of
discrete systems (7.2.4). Namely, the fixed points for the flow (7.3.2)
are the points X at which all derivatives in its left-hand side equal
zero. For the obvious reason, these points are also named the equilib-
rium (or stationary) points: If the system reaches one of these points,
it stays there forever.
Nonlinear Dynamical Systems
75

Equations with derivatives of order greater than one can be also
transformed into flows by introducing additional variables. For
example, equation (7.3.1) can be transformed into the system
du
dt ¼ w, dw
dt ¼ gw  v2u
(7:3:4)
Hence, the damped oscillator may be described in the two-dimen-
sional phase space (w, u). The energy of the damped oscillator, E,
E ¼ 0:5(w2 þ v2u2)
(7:3:5)
evolves with time according to the equation
dE
dt ¼ gw2
(7:3:6)
It follows from (7.3.6) that the dumped oscillator dissipates energy
(i.e., is a dissipative system) at g > 0. Typical trajectories of the
dumped oscillator are shown in Figure 7.4. In the case g ¼ 0, the
trajectories are circles centered at the origin of the phase plane. If
g > 0, the trajectories have a form of a spiral approaching the origin
of plane.2 In general, the dissipative systems have a point attractor in
the center of coordinates that corresponds to the zero energy.
Chaos is usually associated with dissipative systems. Systems with-
out energy dissipation are named conservative or Hamiltonian
−2.5
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
−1.5
−0.5
0.5
1.5
FI
PSI
−2.5
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
−1.5
−1
−0.5
0
0.5
1
1.5
FI
PSI
a)
b)
Figure 7.4 Trajectories of the damped oscillator with v ¼ 2: (a) g ¼ 2; (b)
g ¼ 0.
76
Nonlinear Dynamical Systems

systems. Some conservative systems may have the chaotic regimes,
too (so-called non-integrable systems) [5], but this case will not be
discussed here. One can easily identify the sources of dissipation in
real physical processes, such as friction, heat radiation, and so on. In
general, flow (7.3.2) is dissipative if the condition
div(F) 
X
N
i ¼ 1
@F
@Xi
< 0
(7:3:7)
is valid on average within the phase space.
Besides the point attractor, systems with two or more dimensions
may have an attractor named the limit cycle. An example of such an
attractor is the solution of the Van der Pol equation. This equation
describes an oscillator with a variable damping coefficient
d2u
dt2 þ g[(u=u0)2  1] du
dt þ v2u ¼ 0
(7:3:8)
In (7.3.8), u0 is a parameter. The damping coefficient is positive at
sufficiently high amplitudes u > u0, which leads to energy dissipation.
However, at low amplitudes (u < u0), the damping coefficient be-
comes negative. The negative term in (7.3.8) has a sense of an energy
source that prevents oscillations from complete decay. If one intro-
duces u0
ffiffiffiffiffiffiffiffi
v=g
p
as the unit of amplitude and 1=v as the unit of time,
then equation (7.3.8) acquires the form
d2u
dt2 þ (u2  e2) du
dt þ u ¼ 0
(7:3:9)
where e ¼ g=v is the only dimensionless parameter that defines the
system evolution. The flow describing the Van der Pol equation has
the following form
du
dt ¼ w, dw
dt ¼ (e2  u2) w  u
(7:3:10)
Figure 7.5 illustrates the solution to equation (7.3.1) for e ¼ 0:4.
Namely, the trajectories approach a closed curve from the initial
conditions located both outside and inside the limit cycle. It should
be noted that the flow trajectories never intersect, even though
their graphs may deceptively indicate otherwise. This property
follows from uniqueness of solutions to equation (7.3.8). Indeed, if the
Nonlinear Dynamical Systems
77

trajectories do intersect, say at point P in the phase space, this implies
that the initial condition at point P yields two different solutions.
Since the solution to the Van der Pol equation changes qualita-
tively from the point attractor to the limit cycle at e ¼ 0, this point is a
bifurcation. Those bifurcations that lead to the limit cycle are named
the Hopf bifurcations.
In three-dimensional dissipative systems, two new types of attractors
appear. First, there are quasi-periodic attractors. These trajectories are
associated with two different frequencies and are located on the surface
of a torus. The following equations describe the toroidal trajectories
(see Figure 7.6)
x(t) ¼ (R þ r sin (wrt)) cos (wRt)
y(t) ¼ (R þ r sin (wrt)) sin (wRt)
z(t) ¼ r cos (wrt)
(7:3:11)
In (7.3.11), R and r are the external and internal torus radii, respect-
ively; wR and wr are the frequencies of rotation around the external
−1.5
−1
−0.5
0
0.5
1
1.5
−1.2
−0.8
−0.4
0
0.4
0.8
1.2
1.6
2
FI
PSI
M1
M2
Figure 7.5 Trajectories of the Van der Pol oscillator with e ¼ 0:4. Both
trajectories starting at points M1 and M2, respectively, end up on the same
limit circle.
78
Nonlinear Dynamical Systems

and internal radii, respectively. If the ratio wR=wr is irrational, it is
said that the frequencies are incommensurate. Then the trajectories
(7.3.11) never close on themselves and eventually cover the entire
torus surface. Nevertheless, such a motion is predictable, and thus it
is not chaotic. Another type of attractor that appears in three-dimen-
sional systems is the strange attractor. It will be introduced using the
famous Lorenz model in the next section.
7.4 LORENZ MODEL
The Lorenz model describes the convective dynamics of a fluid
layer with three dimensionless variables:
dX
dt ¼ p(Y  X)
dY
dt ¼ XZ þ rX  Y
dZ
dt ¼ XY  bZ
(7:4:1)
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
10
12
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
10
12
Figure 7.6 Toroidal trajectories (7.3.11) in the X-Y plane for R ¼ 10, r ¼ 1,
wR ¼ 100, wr ¼ 3.
Nonlinear Dynamical Systems
79

In (7.4.1), the variable X characterizes the fluid velocity distribution,
and the variables Y and Z describe the fluid temperature distribution.
The dimensionless parameters p, r, and b characterize the thermo-
hydrodynamic and geometric properties of the fluid layer. The Lorenz
model, being independent of the space coordinates, is a result of signifi-
cant simplifications of the physical process under consideration [5, 7].
Yet, this model exhibits very complex behavior. As it is often done in
the literature, we shall discuss the solutions to the Lorenz model for
the fixed parameters p ¼ 10 and b ¼ 8=3. The parameter r (which is the
verticaltemperaturedifference)willbetreatedasthecontrolparameter.
At small r  1, any trajectory with arbitrary initial conditions ends
at the state space origin. In other words, the non-convective state at
X ¼ Y ¼ Z ¼ 0 is a fixed point attractor and its basin is the entire
phase space. At r > 1, the system acquires three fixed points. Hence,
the point r ¼ 1 is a bifurcation. The phase space origin is now repel-
lent. Two other fixed points are attractors that correspond to the
steady convection with clockwise and counterclockwise rotation, re-
spectively (see Figure 7.7). Note that the initial conditions define
−8
−6
−4
−2
0
2
4
6
8
10
−8
−6
−4
−2
0
2
4
6
8
A : X-Y, Y(0) = −1
B : X-Z, Y(0) = −1
C : X-Y, Y(0) =   1
D : X-Z, Y(0) =   1
X
Y
Z
A
B
C
D
Figure 7.7 Trajectories of the Lorenz model for p ¼ 10, b ¼ 8/3, r ¼ 6, X(0)
¼ Z(0) ¼ 0, and different Y(0).
80
Nonlinear Dynamical Systems

which of the two attractors is the trajectory’s final destination. The
locations of the fixed points are determined by the stationary solution
dX
dt ¼ dY
dt ¼ dZ
dt ¼ 0
(7:4:2)
Namely,
Y ¼ X, Z ¼ 0:5X2, X ¼ 
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
b(r  1)
p
(7:4:3)
When the parameter r increases to about 13.93, the repelling
regions develop around attractors. With further growth of r, the
trajectories acquire the famous ‘‘butterfly’’ look (see Figure 7.8). In
this region, the system becomes extremely sensitive to initial condi-
tions. An example with r ¼ 28 in Figure 7.9 shows that the change of
Y(0) in 1% leads to completely different trajectories Y(t). The system
is then unpredictable, and it is said that its attractors are ‘‘strange.’’
With further growth of the parameter r, the Lorenz model reveals
new surprises. Namely, it has ‘‘windows of periodicity’’ where the
trajectories may be chaotic at first but then become periodic. One of
the largest among such windows is in the range 144 < r < 165. In this
parameter region, the oscillation period decreases when r grows. Note
−30
−20
−10
0
10
20
30
40
50
60
−20
−15
−10
−10
−5
−5
0
5
10
15
20
25
X-Y
X-Z
X
Y
Z
Figure 7.8 Trajectories of the Lorenz model for p ¼ 10, b ¼ 8/3 and r ¼ 28.
Nonlinear Dynamical Systems
81

that this periodicity is not described with a single frequency, and the
maximums of its peaks vary. Finally, at very high values of
r (r > 313), the system acquires a single stable limit cycle. This fascin-
ating manifold of solutions is not an exclusive feature of the Lorenz
model. Many nonlinear dissipative systems exhibit a wide spectrum of
solutions including chaotic regimes.
7.5 PATHWAYS TO CHAOS
A number of general pathways to chaos in nonlinear dissipative
systems have been described in the literature (see, e.g., [5] and refer-
ences therein). All transitions to chaos can be divided into two major
groups: local bifurcations and global bifurcations. Local bifurcations
occur in some parameter range, but the trajectories become chaotic
when the system control parameter reaches the critical value. Three
types of local bifurcations are discerned: period-doubling, quasi-peri-
odicity, and intermittency. Period-doubling starts with a limit cycle at
some value of the system control parameter. With further change of
40
20
0
−20
−40
0
2
4
6
8
10
12
14
t
Y(t)
Y(0) = 1.00
Y(0) = 1.01
Figure 7.9 Sensitivity of the Lorenz model to the initial conditions for p ¼
10, b ¼ 8/3 and r ¼ 28.
82
Nonlinear Dynamical Systems

this parameter, the trajectory period doubles and doubles until it
becomes infinite. This process was proposed by Landau as the main
turbulence mechanism. Namely, laminar flow develops oscillations at
some sufficiently high velocity. As velocity increases, another (incom-
mensurate) frequency appears in the flow, and so on. Finally, the
frequency spectrum has the form of a practically continuous band. An
alternative mechanism of turbulence (quasi-periodicity) was proposed
by Ruelle and Takens. They have shown that the quasi-periodic
trajectories confined on the torus surface can become chaotic due to
high sensitivity to the input parameters. Intermittency is a broad
category itself. Its pathway to chaos consists of a sequence of periodic
and chaotic regions. With changing the control parameter, chaotic
regions become larger and larger and eventually fill the entire
space.
In the global bifurcations, the trajectories approach simple attract-
ors within some control parameter range. With further change of the
control parameter, these trajectories become increasingly complicated
and in the end, exhibit chaotic motion. Global bifurcations are parti-
tioned into crises and chaotic transients. Crises include sudden
changes in the size of chaotic attractors, sudden appearances of the
chaotic attractors, and sudden destructions of chaotic attractors and
their basins. In chaotic transients, typical trajectories initially behave
in an apparently chaotic manner for some time, but then move to
some other region of the phase space. This movement may asymptot-
ically approach a non-chaotic attractor.
Unfortunately, there is no simple rule for determining the condi-
tions at which chaos appears in a given flow. Moreover, the same
system may become chaotic in different ways depending on its par-
ameters. Hence, attentive analysis is needed for every particular
system.
7.6 MEASURING CHAOS
As it was noticed in in Section 7.1, it is important to understand
whether randomness of an empirical time series is caused by noise or
by the chaotic nature of the underlying deterministic process. To
address this problem, let us introduce the Lyapunov exponent. The
major property of a chaotic attractor is exponential divergence of its
Nonlinear Dynamical Systems
83

nearby trajectories. Namely, if two nearby trajectories are separated
by distance d0 at t ¼ 0, the separation evolves as
d(t) ¼ d0 exp (lt)
(7:6:1)
The parameter l in (7.6.1) is called the Lyapunov exponent. For the
rigorous definition, consider two points in the phase space, X0 and
X0 þ Dx0, that generate two trajectories with some flow (7.3.2). If the
function Dx(X0, t) defines evolution of the distance between these
points, then
l ¼ lim 1
t ln jDx(X0, t)j
jDx0j
, t ! 1, Dx0 ! 0
(7:6:2)
When l < 0, the system is asymptotically stable. If l ¼ 0, the system
is conservative. Finally, the case with l > 0 indicates chaos since the
system trajectories diverge exponentially.
The practical receipt for calculating the Lyapunov exponent is as
follows. Consider n observations of a time series x(t): x(tk)¼xk, k¼1,
. . . , n. First, select a point xi and another point xj close to xi. Then
calculate the distances
d0 ¼ jxi  xjj, d1 ¼ jxiþ1  xjþ1j, . . . , dn ¼ jxiþn  xjþnj
(7:6:3)
If the distance between xiþn and xjþn evolves with n accordingly with
(7.6.1), then
l(xi) ¼ 1
n ln dn
d0
(7:6:4)
The value of the Lyapunov exponent l(xi) in (7.6.4) is expected to be
sensitive to the choice of the initial point xi. Therefore, the average
value over a large number of trials N of l(xi) is used in practice
l ¼ 1
N
X
N
i ¼ 1
l(xi)
(7:6:5)
Due to the finite size of empirical data samples, there are limitations
on the values of n and N, which affects the accuracy of calculating the
Lyapunov exponent. More details about this problem, as well as other
chaos quantifiers, such as the Kolmogorov-Sinai entropy, can be
found in [5] and references therein.
84
Nonlinear Dynamical Systems

The generic characteristic of the strange attractor is its fractal
dimension. In fact, the non-integer (i.e., fractal) dimension of an
attractor can be used as the definition of a strange attractor. In
Chapter 6, the box-counting fractal dimension was introduced.
A computationally simpler alternative, so-called correlation dimen-
sion, is often used in nonlinear dynamics [3, 5].
Consider a sample with N trajectory points within an attractor. To
define the correlation dimension, first the relative number of points
located within the distance R from the point i must be calculated
pi(R) ¼
1
N  1
X
N
j ¼ 1, j 6¼ i
u(R  jxj  xij)
(7:6:6)
In (7.6.6), the Heaviside step function u equals
u ¼
0,
x < 0
1,
x  0

(7:6:7)
Then the correlation sum that characterizes the probability of finding
two trajectory points within the distance R is computed
C(R) ¼ 1
N
X
N
i¼1
pi(R)
(7:6:8)
It is assumed that C(R)  RDc. Hence, the correlation dimension Dc
equals
Dc ¼ lim
R!0 [ ln C(R)= ln R]
(7:6:9)
There is an obvious problem of finding the limit (7.6.9) for data
samples on a finite grid. Yet, plotting ln[C(R)] versus ln(R) (which
is expected to yield a linear graph) provides an estimate of the
correlation dimension.
An interesting question is whether a strange attractor is always
chaotic, in other words, if it always has a positive Lyapunov expo-
nent. It turns out there are rare situations when an attractor may be
strange but not chaotic. One such example is the logistic map at the
period-doubling points: Its Lyapunov exponent equals zero while the
fractal dimension is about 0.5. Current opinion, however, holds that
the strange deterministic attractors may appear in discrete maps
rather than in continuous systems [5].
Nonlinear Dynamical Systems
85

7.7 REFERENCES FOR FURTHER READING
Two popular books, the journalistic report by Gleick [8] and the
‘‘first-hand’’ account by Ruelle [9], offer insight into the science of
chaos and the people behind it. The textbook by Hilborn [5] provides
a comprehensive description of the subject. The interrelations be-
tween the chaos theory and fractals are discussed in detail in [10].
7.8 EXERCISES
1. Consider the quadratic map Xk ¼ Xk12 þ C, where C > 0.
(a) Prove that C ¼ 0:25 is a bifurcation point.
(b) Find fixed points for C ¼ 0:125. Define what point is an
attractor and what is its attraction basin for X > 0.
2. Verify the equilibrium points of the Lorenz model (7.4.3).
*3. Calculate the Lyapunov exponent of the logistic map as a
function of the parameter A.
*4. Implement the algorithm for simulating the Lorenz model.
(a) Reproduce the ‘‘butterfly’’ trajectories depicted in Figure
7.8.
(b) Verify existence of the periodicity window at r ¼ 150.
(c) Verify existence of the limit cycle at r ¼ 350.
Hint: Use a simple algorithm: Xk ¼ Xk1 þ tF(Xk1, Yk1, Zk1)
where the time step t can be assigned 0.01.
86
Nonlinear Dynamical Systems


## Scaling in Financial Time Series

Chapter 8
Scaling in Financial Time
Series
8.1 INTRODUCTION
Two well-documented findings motivate further analysis of financial
time series. First, the probability distributions of returns often deviate
significantly from the normal distribution by having fat tails and excess
kurtosis. Secondly, returns exhibit volatility clustering. The latter effect
has led to the development of the GARCH models described in Section
5.3.1 In this chapter, we shall focus on scaling in the probability distri-
butions of returns, the concept that has attracted significant attention
from economists and physicists alike.
Alas, as the leading experts in Econophysics, H. E. Stanley and
R. Mantegna acknowledged [2]:
‘‘No model exists for the stochastic process describing the
time evolution of the logarithm of price that is accepted by
all researchers.’’
There are several reasons for the status quo.2 First, different financial
time series may have varying non-stationary components. Indeed, the
stock price reflects not only the current value of a company’s assets
but also the expectations of the company’s growth. Yet, there is no
general pattern for evolution of a business enterprise.3 Therefore,
87

empirical research often concentrates on the average economic in-
dexes, such as the S&P 500. Averaging over a large number of
companies certainly smoothes noise. Yet, the composition of these
indicators is dynamic: Companies may be added to or dropped from
indexes, and the company’s contribution to the economic index usu-
ally depends on its ever-changing market capitalization.
Foreign exchange rates are another object frequently used in empir-
ical research.4 Unfortunately, many of the findingsaccumulated during
the 1990s have become somewhat irrelevant, as several European cur-
rencies ceased toexist after the birth of the Euro in 1999. In any case, the
foreign exchange rates, being a measure of relative currency strength,
may have statistical features that differ among themselves and in com-
parison with the economic indicators of single countries.
Another problem is data granularity. Low granularity may under-
estimate the contributions of market rallies and crashes. On the other
hand, high-frequency data are extremely noisy. Hence, one may
expect that universal properties of financial time series (if any exist)
have both short-range and long-range time limitations.
The current theoretical framework might be too simplistic to ac-
curately describe the real world. Yet, important advances in under-
standing of scaling in finance have been made in recent years. In the
next section, the asymptotic power laws that may be recovered from
the financial time series are discussed. In Section 8.3, the recent
developments including the multifractal approach are outlined.
8.2 POWER LAWS IN FINANCIAL DATA
Theimportanceoflong-rangedependenciesinthefinancialtimeseries
wasshownfirstbyB.Mandelbrot[6].UsingtheR/Sanalysis(seeSection
6.1), Mandelbrot and others have found multiple deviations of the
empirical probability distributions from the normal distribution [7].
Early research of universality in the financial time series [6] was
based on the stable distributions (see Section 3.3). This approach,
however, has fallen out of favor because the stable distributions have
infinite volatility, which is unacceptable for many financial applica-
tions [8]. The truncated Levy flights that satisfy the requirement for
finite volatility have been used as a way around this problem [2, 9, 10].
One disadvantage of the truncated Levy flights is that the truncating
88
Scaling in Financial Time Series

distance yields an additional fitting parameter. More importantly,
the recent research by H. Stanley and others indicates that the asymp-
totic probability distributions of several typical financial time series
resemble the power law with the index a close to three [11–13]. This
means that the probability distributions examined by Stanley’s team
are not stable at all (recall that the stable distributions satisfy the
condition 0 < a  2). Let us provide more details about these interest-
ing findings.
In [11], returns of the S&P 500 index were studied for the period
1984–1996 with the time scales Dt varying from 1 minute to 1 month.
It was found that the probability distributions at Dt < 4 days were
consistent with the power-law asymptotic behavior with the index
a  3. At Dt > 4 days, the distributions slowly converge to the
normal distribution. Similar results were obtained for daily returns
of the NIKKEI index and the Hang-Seng index. These results are
complemented by another work [12] where the returns of several
thousand U.S. companies were analyzed for Dt in the range from
five minutes to about four years. It was found that the returns of
individual companies at Dt < 16 days are also described with the
power-law distribution having the index a  3. At longer Dt, the
probability distributions slowly approach the normal form. It was
also shown that the probability distributions of the S&P 500 index
and of individual companies have the same asymptotic behavior due
to the strong cross-correlations of the companies’ returns. When these
cross-correlations were destroyed with randomization of the time
series, the probability distributions converged to normal at a much
faster pace.
The theoretical model offered in [13] may provide some explan-
ation to the power-law distribution of returns with the index a  3.
This model is based on two observations: (a) the distribution of the
trading volumes obeys the power law with an index of about 1.5; and
(b) the distribution of the number of trades is a power law with an
index of about three (in fact, it is close to 3.4). Two assumptions were
made to derive the index a of three. First, it was assumed that the
price movements were caused primarily by the activity of large mutual
funds whose size distribution is the power law with index of one (so-
called Zipf’s law [4]). In addition, it was assumed that the mutual fund
managers trade in an optimal way.
Scaling in Financial Time Series
89

Another model that generates the power law distributions is the
stochastic Lotka-Volterra system (see [14] and references therein).
The generic Lotka-Volterra system is used for describing different
phenomena, particularly the population dynamics with the predator-
prey interactions. For our discussion, it is important that some agent-
based models of financial markets (see Chapter 12) can be reduced to
the Lotka-Volterra system [15]. The discrete Lotka-Volterra system
has the form
wi(t þ 1) ¼ l(t)wi(t)  aW(t)  bwi(t)W(t), W(t) ¼ 1
N
X
N
i ¼ 1
wi(t)
(8:2:1)
where wi is an individual characteristic (e.g., wealth of an investor i;
i ¼ 1, 2, . . . , N), a and b are the model parameters, and l(t) is a
random variable. The components of this system evolve spontan-
eously into the power law distribution f(w, t)  w(1þa). In the
mean time, evolution of W(t) exhibits intermittent fluctuations that
can be parameterized using the truncated Levy distribution with the
same index a [14].
Seeking universal properties of the financial market crashes is
another interesting problem explored by Sornette and others (see
[16] for details). The main idea here is that financial crashes are
caused by collective trader behavior (dumping stocks in panic),
which resembles the critical phenomena in hierarchical systems.
Within this analogy, the asymptotic behavior of the asset price S(t)
has the log-periodic form
S(t) ¼ A þ B(tc  t)a{1 þ C cos [w ln (tc  t)  w]}
(8:2:2)
where tc is the crash time; A, B, C, w, a, and w are the fitting
parameters. There has been some success in describing several market
crashes with the log-periodic asymptotes [16]. Criticism of this ap-
proach is given in [17] and references therein.
8.3 NEW DEVELOPMENTS
So, do the findings listed in the preceding section solve the problem
of scaling in finance? This remains to be seen. First, B. LeBaron has
shown how the price distributions that seem to have the power-law
form can be generated by a mix of the normal distributions with
90
Scaling in Financial Time Series

different time scales [18]. In this work, the daily returns are assumed
to have the form
R(t) ¼ exp [gx(t) þ m]e(t)
(8:3:1)
where e(t) is an independent random normal variable with zero mean
and unit variance. The function x(t) is the sum of three processes with
different characteristic times
x(t) ¼ a1y1(t) þ a2y2(t) þ a3y3(t)
(8:3:2)
The first process y1(t) is an AR(1) process
y1(t þ 1) ¼ r1y1(t) þ Z1(t þ 1)
(8:3:3)
where r1 ¼ 0:999 and Z1(t) is an independent Gaussian adjusted so
that var[y1(t)] ¼ 1. While AR(1) yields exponential decay, the chosen
value of r1 gives a long-range half-life of about 2.7 years. Similarly,
y2(t þ 1) ¼ r2y2(t) þ Z2(t þ 1)
(8:3:4)
where
Z2(t)
is
an
independent
Gaussian
adjusted
so
that
var[y2(t)] ¼ 1. The chosen value r2 ¼ 0:95 gives a half-life of about
2.5 weeks. The process y3(t) is an independent Gaussian with unit
variance and zero mean, which retains volatility shock for one day.
The normalization rule is applied to the coefficients ai
a1
2 þ a2
2 þ a3
2 ¼ 1:
(8:3:5)
The parameters a1, a2, g, and m are chosen to adjust the empirical data.
This model was used for analysis of the Dow returns for 100 years
(from 1900 to 2000). The surprising outcome of this analysis is retrieval
of the power law with the index in the range of 2.98 to 3.33 for the data
aggregation ranges of 1 to 20 days. Then there are generic comments by
T. Lux on spurious scaling laws that may be extracted from finite
financial data samples [19]. Some reservation has also been expressed
about the graphical inference method widely used in the empirical
research. In this method, the linear regression equations are recovered
from the log - log plots. While such an approach may provide correct
asymptotes, at times it does not stand up to more rigorous statistical
hypothesis testing. A case in point is the distribution in the form
f(x) ¼ xaL(x)
(8:3:6)
where L(x) is a slowly-varying function that determines behavior of
the distribution in the short-range region. Obviously, the ‘‘universal’’
Scaling in Financial Time Series
91

scaling exponent a ¼ log [f(x)]= log (x) is as accurate as L(x) is close
to a constant. This problem is relevant also to the multifractal scaling
analysis that has become another ‘‘hot’’ direction in the field.
The multifractal patterns have been found in several financial time
series (see, e.g., [20, 21] and references therein). The multifractal
framework has been further advanced by Mandelbrot and others.
They proposed compound stochastic process in which a multifractal
cascade is used for time transformations [22]. Namely, it was assumed
that the price returns R(t) are described as
R(t) ¼ BH[u(t)]
(8:3:7)
where BH[] is the fractional Brownian motion with index H and u(t) is
a distribution function of multifractal measure (see Section 6.2). Both
stochastic components of the compound process are assumed inde-
pendent. The function u(t) has a sense of ‘‘trading time’’ that reflects
intensity of the trading process. Current research in this direction
shows some promising results [23–26]. In particular, it was shown
that both the binomial cascade and the lognormal cascade embedded
into the Wiener process (i.e., into BH[] with H ¼ 0:5) may yield a more
accurate description of several financial time series than the GARCH
model [23]. Nevertheless, this chapter remains ‘‘unfinished’’ as new
findings in empirical research continue to pose new challenges for
theoreticians.
8.4 REFERENCES FOR FURTHER READING
Early research of scaling in finance is described in [2, 6, 7, 9, 17].
For recent findings in this field, readers may consult [10–13, 23–26].
8.5 EXERCISES
**1. Verify how a sum of Gaussians can reproduce a distribution
with the power-law tails in the spirit of [18].
**2. Discuss the recent polemics on the power-law tails of stock
prices [27–29].
**3. Discuss the scaling properties of financial time series reported
in [30].
92
Scaling in Financial Time Series

