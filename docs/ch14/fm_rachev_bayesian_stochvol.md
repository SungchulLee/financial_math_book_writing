# Bayesian Stochastic Volatility Models

!!! info "Source"
    **Bayesian Methods in Finance** by Svetlozar T. Rachev, John S.J. Hsu, Biliana S. Bagasheva, and Frank J. Fabozzi, Wiley, 2008.
    These notes are used for educational purposes.

## Stochastic Volatility Models (Bayesian)

282
BAYESIAN METHODS IN FINANCE
sample of historical return data with the help of statistical techniques—most
often, principal component analysis. The idea is to obtain, in order of
decreasing importance, the factors that best explain the variability of returns.
Each consecutive factor best explains the variation left unexplained by the
previous factor.3 The stronger the dependence (correlation) between the
return series, the smaller the number of factors needed to explain a large
proportion of variability. Generally, three to five factors are found to account
for about 90% of return variability. After the factor returns are extracted,
time-series regressions, as in (14.1), are run to estimate the sensitivities
(exposures) of stocks to the risk factors.
Macroeconomic Factor Models
Macroeconomic factor models use macroeconomic time series, exogenous
to stock returns, such as inflation, interest rates, industrial production,
and default premiums to represent the common factors governing stock
returns.4 The stocks’ sensitivities to the macroeconomic factors are esti-
mated with time-series regressions as in the case of statistical factor
models.
Fundamental Factor Models
Fundamental factor models attempt to explain a large proportion of return
variability with company-specific variables—company attributes based on
accounting data, such as dividend yield, company size, book-to-market ratio,
as well as industrial and geographical classification. The factor sensitivities
are determined from these observed firm attributes, while factor returns are
estimated via cross-sectional regressions. A fundamental risk factor can be
in fact a combination of several descriptors that capture aspects of the same
company attribute. For example, the risk factor referred to as value might
be designed to combine the book-to-price ratio, the earnings-to-price ratio,
and the price-to-earnings-to-growth ratio, while ‘‘profit’’ might combine
return on equity and cash flow return on equity.5
3More formally, denote the matrix of historical returns by R (each row corresponds
to an observation of returns in a particular period). The matrix of cross products,
R′R, is decomposed into orthogonal factors, whose contribution to the overall
variability of returns is quantified by the matrix’s eigenvalues. The magnitudes of
eigenvalues help determine the number of factors to include in the factor model.
4See Chen, Roll, and Ross (1986).
5In a study by Connor (1995), macroeconomic factor models are found to have
less explanatory power than statistical and fundamental models, while, perhaps
surprisingly, the fundamental model outperforms the statistical one.

Multifactor Equity Risk Models
283
RISK ANALYSIS USING A MULTIFACTOR EQUITY MODEL
A multifactor model facilitates greatly the estimation of the return covariance
matrix. In a mean-variance setting, where portfolio risk is defined through
the covariance matrix, employing a multifactor model means that portfo-
lio risk estimation is made simple—instead of computing the covariances
between all pairs of returns, we consider the covariances between factors,
which are many times fewer than the stocks. Suppose that 1,000 stocks are
candidates for acquisition. The return covariance matrix of the candidate
stocks consists of 1,000 variances and 499,500 (distinct) covariances. Esti-
mating that large a number of parameters is a daunting task. Let us see how
a multifactor model would help reduce the dimensionality of the problem.
Covariance Matrix Estimation
Suppose that our historical data sample consists of the returns on N stocks
that are candidates for inclusion in the portfolio recorded over T periods of
time. Stacking the returns for all stocks at time t, we rewrite (14.1) as
Rt = B f t + ϵt,
(14.2)
where: Rt = N × 1 vector of stock returns at time t.
B = N × K + 1 matrix of risk factor sensitivities.
ft = K + 1 × 1 vector of risk factor returns at time t.
ϵt = N × 1 vector of stock-specific returns at time t.
The first element of ft is 1, while the first column of B consists of the
intercepts αi, i = 1, . . . , N, in (14.1). The expression in (14.2) represents
the cross-sectional regression we might use to estimate a fundamental
multifactor model. Recall that the unknown parameters we estimate in it
are the factor returns, f t, while the risk factor sensitivities, B, are observed.
Simple matrix algebra allows us to express the covariance matrix of
stock returns, , using (14.2) as
 = BfB′ + D,
(14.3)
where: f = covariance matrix of the factor returns.
D = covariance matrix (assumed to be diagonal) of the specific
returns.
In the case of 1,000 candidate stocks and a 13-factor model, computing
 in (14.3) would mean estimating (only) 1,091 quantities (13 factor return

284
BAYESIAN METHODS IN FINANCE
variances, 78 (distinct) factor return covariances, and 1,000 specific return
variances). Clearly, employing a multifactor model makes portfolio risk
estimation a whole lot easier.
To estimate the covariance matrices, f and D, we use as inputs
the estimated factor and specific returns obtained from the cross-sectional
regression in (14.2):
■A T × K matrix of estimated factor returns, denoted by F, in which each
row, f t, corresponds to the estimated factor returns at a point in time.
■A T × N matrix of estimated specific stock returns, denoted by E, in
which each row, et, corresponds to the estimated specific returns at a
point in time Row t of E is obtained as
et = Rt −Bf t.
(14.4)
Different methods are available to obtain the estimates of the factor
covariance matrix, f, and the specific return covariance matrix, D. For
example, f can be estimated using the exponentially weighted forecast
procedure we discussed in Chapter 8 in our coverage of covariance matrix
estimation. The diagonal elements of D could be estimated using expo-
nential weighting as well.6 An ARCH-type model or a stochastic volatility
(SV) model (discussed, respectively, in Chapters 11 and 12) could also be
employed to estimate the specific variances of the stock returns.
Let us assume that we have obtained f, D, and . For the time being,
we take it for granted that portfolio risk is measured by the variance of
portfolio returns. (See the section on scenario generation later in this chapter
for a different take on portfolio risk estimation.) The variance of returns of
a portfolio p with weights ω is given by
σ 2
p = ω′  ω
= b
′
p  bp + ω′ D ω,
(14.5)
where bp is the K × 1 vector of portfolio exposures to the factors in the
model,
bp = ω′B
=
 N

i=1
ωiBi,1 , ··· ,
N

i=1
ωKBi,K

,
6Litterman (2003) suggest shrinking each variance estimate to the average (across
all assets) variance estimate in order to bring extremely high specific variances closer
to the majority of the specific variances.

Multifactor Equity Risk Models
285
and Bi,k is exposure of stock i to factor k. While all the covariance matrices
above are estimates, we suppress the ‘‘hats’’ signifying that for notational
simplicity.
It is certainly of great value to a portfolio manager to be able to identify
the sources of risk for the managed portfolio. We now look at several ways
to decompose portfolio risk, as well as to analyze these sources.7
Risk Decomposition
The expression (14.5) immediately suggests the decomposition of portfolio
risk into a common factor component (given by bp
′  bp) and a specific
component (given by ω′ D ω).
An active portfolio manager manages a portfolio against a benchmark
attempting to produce return in excess of the benchmark (active return)
and, accordingly, bears risk in excess of the benchmark risk (active risk).
Active risk is also called tracking error. Denote the assets’ weights in
the benchmark portfolio by ωb. We define assets’ active weights, ωa, by
the difference between the weights of the manager’s portfolio and the
benchmark weights,
ωa = ω −ωb.
(14.6)
The (squared) active risk of the manager’s portfolio is expressed as
σ 2
p,a = ω′
a  ωa,
(14.7)
which can also be partitioned into common factor and specific components:
σ 2
p,a = b
′
p,a  bp,a + ω′
a D ωa,
(14.8)
where bp,a = B′ ωa.
Detailed risk decomposition is a prerequisite for effective portfolio
management. In a multifactor model framework, a portfolio manager can
assess the contribution of individual stocks and the various factor exposures
(exposures to industries, investment styles, and others) to total (active) risk.
We discuss how to analyze the sources of portfolio total risk.
Denote by ωi the portfolio weight of stock i, by ωi,a the active weight
of stock i, and by bp,k the portfolio exposure to factor k. To obtain the
expressions for the sources of active risk (tracking error), one needs to just
substitute ωi,a for ωi. The marginal contributions of stock i and factor k
are given mathematically by the derivatives of total risk with respect to ωi
and bp,k.
7In the discussion below we follow Grinold and Kahn (2000) and Litterman (2003).

286
BAYESIAN METHODS IN FINANCE
Marginal Contribution of Stock i to Total Risk
The marginal contribution of
stock i to total risk (MCTRi) is given by
MCTRi ≡d σp
d ωi
= 1
2

σ 2
p
−1/2 (ω)i
= (ω)i
2σp
,
(14.9)
where the subscript i denotes the ith element of the vector. MCTRi is
the amount of portfolio risk associated with the holding of stock i.
The percentage marginal contribution of stock i to total risk (PCTR) is
obtained as
PCTRi = ωi
σp
MCTRi.
(14.10)
Marginal Contribution of Factor k to Total Risk
The marginal contribution of
factor k to total risk (MCFTRk) is written as
MCFTRk ≡
d σp
d bp,k
= 1
2

σ 2
p
−1/2 
bp

=

bp

k
2σp
.
(14.11)
The percentage contribution of factor k to total risk (PCFTRk) is
PCFTRk = bp,k
σp
MCFTRk.
(14.12)
If a manager wants to control the risk coming from the exposure to
factor k, he needs to know how each stock contributes to forming this
exposure’s risk. PCFTRk can be broken down even further into stock
contributions to the risk coming from the kth factor exposure of the
portfolio,
PCFTRk, i = ωiBi, k
σp
MCFTRk.
(14.13)
When we define portfolio risk as the CVaR of portfolio return, instead
of the variance of portfolio return, we can perform the same kind of risk
decomposition in order to assess the risk contributions of individual stocks
and factor exposures. In this chapter, we focus on scenario-based (numerical)
computation of CVaR. Next, we present return scenario generation in a
multifactor setting and explain CVaR decomposition further below.

Multifactor Equity Risk Models
287
RETURN SCENARIO GENERATION
In Chapter 13, we discussed some of the new directions for risk manage-
ment and portfolio construction, in particular, the use of risk measures
designed to address the deficiencies of the traditional metric—the stan-
dard deviation—and to provide adequate description of the tails of the
return distribution. We described the modification of the portfolio selection
problem based on one of these risk measures, the CVaR. In nonnormal
settings, where no analytical expressions for densities or risk measures exist,
CVaR minimization takes on an additional point of attraction—it can be
scenario-based, performed on the basis of a large number of simulations
from the returns distribution.
Scenarios of returns can be generated from some multivariate distribu-
tion fitted to the observed data. The reason for employing a multifactor
framework is to take advantage of the risk decomposition this framework
makes possible. We are able to identify the sources of risk, as measured by
CVaR, as a step in a comprehensive risk-management process.
The process of stock return scenario generation has two stages:
1. For each t, t = 1, . . . , T, estimate the cross-sectional regression in (14.2)
and obtain the time series of factor return estimates F, and specific
return estimates E,
F =


f1,1 f1,2 ··· f1,K
. . . . . . . . . . . . . . . .
ft,1 ft,2 ···
ft,K
. . . . . . . . . . . . . . . .
fT,1 fT,2 ··· fT,K


(14.14)
and
E =


e1,1 e1,2 ··· e1,N
. . . . . . . . . . . . . . . .
et,1 et,2 ··· et,N
. . . . . . . . . . . . . . . .
eT,1 eT,2 ··· eT,N


.
(14.15)
respectively.
2. Predict (simulate) the factor returns and stock-specific returns and use
them as drivers to compute scenarios of the stock returns from
R = Bf +e,
(14.16)
where f and e are the predicted (simulated) factor and stock-specific
returns.

288
BAYESIAN METHODS IN FINANCE
Predicting the Factor and Stock-Specific Returns
The factor returns are likely not independent. A small number of suprafac-
tors may govern the behavior of the model’s factors. Therefore, it may be
appropriate to analyze factor returns in a multivariate setting.
Stock-specific returns may or may not be independent across stocks. If
one is confident that the fundamental multifactor model is correctly specified
and the factors adequately represent the common drivers of stock returns,
one could assume that the stock-specific returns are independent. Then, the
time series of each stock-specific return could be treated as a sample from a
univariate distribution. In contrast, if there are one or more factors omitted
from the model in (14.2), the residuals from the cross-sectional regressions
(i.e., the estimated stock-specific returns) are not independent, and it might
be preferable to treat them as coming from a multivariate distribution.8
Two approaches to generating f ande can be followed:
1. Assume a time-invariant behavior of F and E. To simulate the factor
returns, denote the distribution of factor returns by p(f | θ), where f is a
1 × K vector and θ is a parameter vector. Estimate θ using the sample of
factor returns, F and denote the estimate by θ. Generate a large number
of samples from p(f | θ).
To simulate the stock-specific returns, proceed in a similar way, either in
a univariate or in a multivariate setting, as per our discussion thus far.
2. Assume a time-varying behavior of F and E. The types of time series
processes to be fit to F and E depend on the particular situation. In
general, a volatility model would be required to model the dynamics of
the stock-specific returns. Factor returns may be considered to have a
more stable dynamics and are subject to fewer shocks than stock-specific
returns. Therefore, a low-order multivariate autoregressive (AR) struc-
ture, such as a multivariate AR process or a multivariate autoregressive
moving average (ARMA) process may be sufficient to describe their
joint dynamics.
Factor and stock-specific returns are simulated from the respective fitted
time-series models.
Risk Analysis in a Scenario-Based Setting
In a scenario-based setting, the analytical convenience of the risk decompo-
sitions outlined earlier in the chapter is not available. However, portfolio
risk can still be decomposed; in this instance, only numerically.
8The arguments about model specification and missing explanatory variables are,
indeed, valid for any regression model.

Multifactor Equity Risk Models
289
Suppose that the M return scenarios generated as described above
are used to obtain the optimal portfolio in a mean-CVaR setting (see
Chapter 13). Denote the return scenarios by R
m, m = 1, . . . , M, and the
optimal portfolio weights by ω∗. The optimal portfolio return corresponding
to each scenario is
Rm
p = ω∗′R
m,
for m = 1, . . . , M. We thus obtain a sample of size M from the distribution
of the portfolio return and we use it to analyze numerically the risk of the
optimal portfolio.
Recall the definitions of the value-at-risk (VaR) and the CVaR in (13.40)
and (13.42) in Chapter 13, respectively. We next show how the CVaRα
could be computed numerically, for a tail probability α = 0.05.
Step 1. Arrange Rm
p , m = 1, . . . , M, in ascending order,
R(1)
p < R(2)
p < ··· > R(M)
p ,
where R
(j)
p denotes the jth smallest portfolio return, j = 1, . . . , M.
Step 2. Determine the portfolio return smaller than 95% of the portfolio
returns. Denote it by9
R([0.05M])
p
.
That is, VaR0.05(Rp) = R([0.05M])
p
.
Step 3. Compute CVaR0.05(Rp),
CVaR0.05(Rp) =
1
[0.05M]
[0.05M]

j=1
R(j)
p .
Let us now see how portfolio risk, CVaR0.05(Rp), can be decomposed
into its sources.
Conditional Value-at-Risk Decomposition
The quantity CVaR0.05(Rp) as defined above is a measure of total portfolio
risk. It is straightforward, however, to calculate the portfolio active risk
(the equivalent of tracking error, when the standard deviation is used as a
risk measure)—we simply substitute ω∗with the vector of active weights,
ωa (see (14.6)), then compute the sample
of portfolio active returns,
9The square brackets in the superscript of R([0.05M])
p
mean that [0.05M] is equal to
0.05M if that is an integer and to the integer part of 0.05M, if it is not.

290
BAYESIAN METHODS IN FINANCE
Rm
p,a, m = 1, . . . , M, and finally obtain the portfolio active CVaR0.05(Rp,a)
following the three steps in the previous section.
The decomposition of CVaR0.05(Rp) is not difficult since, being an expec-
tation, it is additive and depends in a linear fashion on the stock returns,
weights, and factor exposures. Using the factor-model representation of
stock returns, the portfolio CVaR can be represented as
CVaR0.05(Rp) = E

Rp | Rp < VaR0.05(Rp)

= E

ω′Bf t + ω′et

| Rp > VaR0.05(Rp)

(14.17)
= ω′E

Bf t | Rp < VaR0.05(Rp)

+ ω′E

et | Rp < VaR0.05(Rp)

.
The two terms in the last line above can easily be evaluated numerically
and give us the decomposition of total (active) portfolio risk into a common
factor component and a stock-specific component.
The CVaR decomposition in the scenario-based setting parallels the one
in the analytical setting. Let us see how we compute numerically the risk
components of CVaR0.05(Rp) above. (Active CVaR (CVaR0.05(Rp,a)), as well
as other values of the tail probability, α, are treated in a similar way). We
use the following sets of simulated data:
■The simulated factor returns,f
m, m = 1, . . . , M.
■The simulated stock-specific returns,em, m = 1, . . . , M.
■The portfolio returns, computed for each scenario, Rm
p , m = 1, . . . , M.
We are also mindful of the correspondence among the scenarios of
factor returns, specific returns, stock returns, and portfolio returns.10
Common-Factor Risk Component
To compute the common-factor risk com-
ponent of CVaR, we can use the procedure outlined below:
Step 1. Identify the portfolio returns smaller than VaR0.05(Rp).
Step 2. Identify the simulated factor returns, drivers of the portfolio
returns in step 1, that is, the portfolio returns smaller than R([0.05M])
p
.
Denote these factor returns byf
(j), j = 1, . . . , [0.05M].
10The procedures for computing the common-factor component and specific com-
ponent are inspired by Yamai and Yoshiba (2002). See also Zhang and Rachev
(2006).

Multifactor Equity Risk Models
291
Step 3. Compute the N × 1 vector,
q =
1
[0.05M]
[0.05M]

j=1
Bf
(j).
(14.18)
Step 4. The common factor risk component of total risk, CVaR0.05(Rp),
is then given by
Common factor risk component = ω∗′q.
(14.19)
Stock-Specific Risk Component
The
stock-specific
risk
component
of
CVaR0.05(Rp) is obtained in a manner analogous to the common-factor
risk component.
Step 1. Identify the portfolio returns smaller than VaR0.05(Rp).
Step 2. Identify the simulated stock-specific returns in step 1, that is,
the portfolio returns smaller than R([0.05M])
p
. Denote these specific
returns bye(j), j = 1, . . . , [0.05M].
Step 3. Compute the N × 1 vector,
p =
1
[0.05M]
[0.05M]

j=1
e(j).
(14.20)
Step 4. The stock-specific risk component of total risk, CVaR0.05(Rp),
is then given by
Stock-specific risk component = ω∗′p.
(14.21)
Contribution of Stock i to Portfolio Risk
The marginal contribution of stock i
to portfolio risk, CVaR0.05(Rp), follows the same general idea in the previous
section.11
Step 1. Identify the portfolio losses larger than VaR0.05(Rp).
Step 2. Identify the scenarios of returns corresponding to the portfolio
returns in step 1, that is, the portfolio returns smaller than R([0.05M])
p
.
Denote those scenarios of returns by R(j) =

R
(j)
1 , R
(j)
2 , . . . , R
(j)
N

, j =
1, . . . , [0.05M].
11See Yamai and Yoshiba (2002).

292
BAYESIAN METHODS IN FINANCE
Step 3. Compute the marginal contribution of stock i to total risk,
MCTRi,
MCTRi =
1
[0.05M]
[0.05M]
j=1
R
(j)
i
CVaR0.05(Rp)
.
(14.22)
The percentage marginal contribution of stock i to total risk (PMCTRi)
is computed as
PMCTRi =
ωi
CVaR0.05(Rp)MCTRi.
(14.23)
To assess the impact on risk of a change in the portfolio weight of
stock i, recompute portfolio returns, Rm
p , m = 1, . . . , M, and total risk,
CVaR0.05(Rp), and perform again the calculations in steps 1 through 3.
Contribution of Factor k to Portfolio Risk
The marginal contribution of fac-
tor k to total portfolio risk, CVaR0.05(Rp), is the kth element of q in (14.18).
The percentage marginal contribution of factor k is computed accordingly.
BAYESIAN METHODS FOR MULTIFACTOR MODELS
Casting the multifactor model estimation in a Bayesian setting enjoys the
usual benefits of addressing parameter uncertainty and incorporating prior
knowledge or intuition. The Bayesian setting is, in addition, particularly
amenable to scenario generation—the outputs from the Markov Chain
Monte Carlo (MCMC) computations allow one to simulate the whole dis-
tribution of the parameters. Admittedly, the Bayesian analogue of the model
and risk estimation outlined above is more time consuming and, certainly,
more computationally intensive. Continuous advances in computing power,
however, act to mitigate these drawbacks. Nevertheless, managers who
employ quantitative strategies based on the usual Gaussian assumption for
returns and use the standard deviation as a measure of risk might be better
off with the simpler estimation framework discussed earlier in the chapter.
The Bayesian multifactor framework is for portfolio managers who would
prefer to:
■Incorporate parameter uncertainty (at all stages of the estimation
process).
■Assume non-Gaussian distributions for stock returns, as well as factor
returns.
■Employ sophisticated methods for volatility estimation, for example,
ARCH-type processes or SV processes and their extensions.

Multifactor Equity Risk Models
293
■Optimize portfolios using the advanced techniques discussed in
Chapter 13.
Next we outline the strategy for tackling the multifactor Bayesian
problem.
Cross-Sectional Regression Estimation
Estimation of the cross-sectional regression in (14.2) can, in general, be per-
formed, as explained in Chapter 4. The parameters whose prior distributions
one needs to specify are the factor returns, f t,1, . . . , f t,K, t = 1, . . . , T, and
the parameters of the return distribution. If one assumes that returns follow
a heavy-tailed distribution, it is not unreasonable to assert a heavy-tailed
prior for the factor returns as well. In a nonconjugate setting, one would
most certainly have to resort to Markov Chain Monte Carlo (MCMC)
methods to simulate the posterior distributions.
Posterior Simulations
Denote the sample from the posterior parameter distribution from the
cross-sectional regression at time t by the P × Q matrix, t,
t = (t, Ft) ,
where: 	t = matrix of P posterior draws of the return distribution
parameters.
Ft = matrix of P posterior draws of the factor returns.
P = number of posterior draws after the burn-in sample is
discarded.
Q = total number of model parameters.
For each t, t = 1, . . . , T, we compute the posterior mean and denote it
by t, a 1 × Q vector,
t =

θt, f t

.
(14.24)
The estimated stock-specific returns at time t are given by
et = Rt −Bf t,
where we apply the expression in (14.4) and f t is the vector of posterior
means in (14.24).

294
BAYESIAN METHODS IN FINANCE
Stacking the posterior means of the factor returns and the estimated
stock-specific returns for all time periods, we obtain the time series of
Bayesian estimates:
F = T × K matrix of time series of estimated factor returns.
E = T × N matrix of time series of estimated stock-specific returns.
Return Scenario Generation
To generate scenarios of returns, we first predict (generate scenarios of) the
factor returns and the stock-specific returns, by either fitting time-invariant
distributions or time-series processes to F and E. Either is performed in a
Bayesian setting. Then, the stock return scenarios are generated, as explained
earlier in the chapter.
The Bayesian procedure above is more robust than that in the frequentist
case. The reason is that factor and stock-specific returns are predicted on
the basis of the posterior distributions of the time-series model parameters
instead of the maximum likelihood estimates of these parameters. That
robustness is then passed on to the predicted returns.
Optimal portfolio construction and risk analysis can be carried out in
the manner discussed earlier in this chapter and in Chapter 13.
ILLUSTRATION
We illustrate the estimation of a heavy-tailed, multifactor model. We gather
daily return data for 229 companies from the S&P 500 index (selected
on the basis of completeness of the return and fundamental data history),
for the three-year period January 1, 2001, through December 31, 2003,
a total of 751 return observations. We build the model with six risk
factors—size, success, value, volatility, yield, and profit—and 10 industry
factors.12
We assume a stable distribution for the stock returns in each period
t, t = 1, . . . , T. (A brief introduction to the stable distribution was given
in Chapter 13.) Its four parameters (the tail parameter, α, the asymmetry
parameter, β, the scale parameter σ, and the location parameter, µ) together
with the returns to the 16 factors, f t,1, . . . , f t,16, make up the parameter
12We use the Global Industry Classification Standard (GICS) and take as factors
the following industry sectors: materials, information technology, consumer staples,
health care, utilities, financials, energy, industrials, consumer discretionary, and
telecommunication services.

Multifactor Equity Risk Models
295
vector we need to estimate
θt =

α, β, σ, ft,1, . . . , ft,K

.
The location parameter µ is not a stand alone parameter here but
equals Bf t. The stable distribution does not have a closed-form den-
sity function—all estimation is performed numerically.13 Since analytical
tractability is not an issue here, our choice of prior distribution is only
based on economic rationale. For example, empirical evidence suggests that
stock returns have a tail parameter with a value between 1 and 2. That is,
stock returns exhibit tails heavier than the Gaussian tails (corresponding to
α = 2) but not too heavy (hence, α > 1). Therefore, we assert a uniform
distribution on the interval (1, 2) for α.
The asymmetry parameter, β, takes values between –1 and 1. For lack
of any other prior information, we assert a uniform distribution on [−1,
1] for it. For the scale parameter we assume a gamma distribution and for
factor returns we assume a stable distribution. We use the griddy Gibbs
sampler algorithm, outlined in Chapter 11, for sampling from the posterior
densities.
Exhibit 14.1 presents typical plots of the posterior densities of the
stable parameters, α, β, σ, corresponding to one of the cross-sectional
regressions, while plots of the posterior means from all cross-sectional
Bayesian regressions are in Exhibit 14.2. Return prediction and risk analysis
can be performed as explained earlier.
SUMMARY
This chapter presented an overview of the multifactor model framework.
We described the process of traditional portfolio risk (as measured by the
standard deviation) estimation within the cross-sectional model framework.
Risk attribution can be performed analytically when the standard deviation
is employed as a risk measure. In a nonnormal setting, risk attribution
is simulation based. The Bayesian framework facilitates estimation and
provides the natural simulation environment.
13Shall I give an outline of the density approximation?

296
BAYESIAN METHODS IN FINANCE
1
1.2
1.4
1.6
1.8
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
Tail Parameter,
−0.9
−0.8
−0.7
−0.6
−0.5
−0.4
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
Asymmetry Parameter,
0.01
0.012
0.014
0.01
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
Scale Parameter,
EXHIBIT 14.1
Posterior densities of α, β, and σ
Notes: The knots of the density curves correspond to the grid nodes on which
posterior densities are evaluated.

Multifactor Equity Risk Models
297
1/27/01 9/25/01 6/13/02
3/17/03
12/31/03
−0.015
−0.01
−0.005
0
0.005
0.01
Profit
1/27/01 9/25/01 6/13/02
3/17/03
12/31/03
−0.03
−0.02
−0.01
0
0.01
0.02
Size
1/27/01 9/25/01 6/13/02
3/17/03
12/31/03
−0.02
−0.01
0
0.01
0.02
Success
1/27/01 9/25/01 6/13/02
3/17/03
12/31/03
−0.02
0
0.02
Value
1/27/01 9/25/01 6/13/02
3/17/03
12/31/03
−0.02
0
0.02
Volatility
1/27/01 9/25/01 6/13/02
6/13/02
12/31/03
−0.02
0
0.02
Yield
EXHIBIT 14.2
Posterior means of the factor daily returns in the stable distribution
scenario

References
Adcock, C., and Shutes, K. 2005. An analysis of skewness and skewness persistence
in three emerging markets. Emerging Markets Review, 6(4):396–418.
Barone Adesi, G. Arbitrage equilibrium with skewed asset returns. 1985. Journal of
Financial and Quantitative Analysis, 20(4):299–313.
Aguilar, O. and West, M. 2000. Bayesian dynamic factor models and portfolio
allocation. Journal of Business & Economic Statistics, 18(3):338–357.
Alexander, C. Bayesian methods for measuring operational risk. Discussion Papers
in Finance 2000-02. ISMA Centre, The University of Reading, 2000.
Andersen, T. 1994. Stochastic autoregressive volatility: A framework for volatility
modeling. 1994. Mathematical Finance, 4(2):75–102.
Andersen, T., Benzoni, L., and Lund, J. 2002. An empirical investigation of
continuous-time equity return models. Journal of Finance, 57(3):1239–1284.
Andersen, T., Bollerslev, T., Christoffersen, P., and Diebold, F. Volatility forecast-
ing. National Bureau of Economic Research. Working Paper Series, 2005.
Anderson, T. An Introduction to Multivariate Statistical Analysis. Hoboken, NJ:
John Wiley & Sons, 2003.
Ang, A., Chen, J., and Xing, Y. Downside risk. 2006. Review of Financial Studies,
19(4):1191–1239.
Avramov, D. 2002. Stock return predictability and model uncertainty. Journal of
Financial Economics, 64(3):423–458.
Azzalini, A. 2005. The skew-normal distribution and related multivariate families.
Scandinavian Journal of Statistics, 32(2):159–188.
Azzalini, A., and Capitanio, A. 2003. Distributions generated by a perturbation of
symmetry with emphasis on a multivariate skew t-distribution. Journal of the
Royal Statistical Society, Series B, 65(2):367–389.
Azzalini, A., and Dalla Vale, A. 1996. The multivariate skew normal distribution.
Biometrika, 83(4):715–726.
Baks, K., Metrick, A., and Wachter, J. 2001. Should investors avoid all actively
managed mutual funds? A study in Bayesian performance evaluation. Journal
of Finance, 56(1):45–85.
Barberis, N. 2000. Investing for the long run when returns are predictable. Journal
of Finance, 55(1):225–264.
Bauwens, L., and Lubrano, M. 1998. Bayesian inference on GARCH models using
the Gibbs sampler. Econometrics Journal, 1(2):C23–C46.
Bauwens, L., Lubrano, M., and Richard, J. Bayesian Inference in Dynamic Econo-
metric Models. New York: Oxford University Press, 2000.
Ben-Tal, A., and Nemirovksi, A. Robust convex optimization. Mathematics of
Operations Research, 23(4), 1998.
298

References
299
Ben-Tal, A., and Nemirovksi, A. 1999. Robust solutions of uncertain linear pro-
grams. Operations Research Letters, 25(1):1–13.
Berger, J. Statistical Theory and Bayesian Analysis. Berlin: Springer-Verlag, 1985.
Berger, J. 1990. Robust Bayesian analysis: Sensitivity to the prior. Journal of
statistical planning and inference, 25(3):303–328.
Berger, J. 2006. The case for objective Bayesian analysis. Bayesian Analysis,
1(3):385–402.
Berger, J., and Bernardo, J. 1992. On the development of reference priors. In
J. Bernardo, J. Berger, A. David, and A. Smith (eds.), Bayesian Statistics,
Volume 4, Oxford, Clareton Press, pp. 35–60.
Bernardo, J. Noninformative priors do not exist: A discussion with Jos´e M.
Bernardo. University of Valencia, 2006. Available at http://www.uv.es/∼
bernardo/Dialogue.pdf. 2006.
Bernardo, J., and Smith, A. Bayesian Theory. New York: John Wiley & Sons, 1994.
Bertocchi, M., Giacometti, R., Ortobelli, S., and Rachev, S. 2005. The impact of dif-
ferent distributional hypotheses on returns in asset allocation. Finance Letters,
3(1):17–27.
Best, M., and Grauer, R. 1991. Sensitivity analysis for mean-variance portfolio
problems. Management Science, 37(8):980–989.
Best, M., and Grauer, R. 1992. The analytics of sensitivity analysis for mean-
variance portfolio problems. International Review of Financial Analysis, 1(1):
17–37.
Black, F. 1976. Studies of stock market volatility changes. Proceedings of the
American Statistical Association, Business and Economic Statistics Section,
pp. 177–181.
Black, F., and Litterman, R. Global asset allocation with equities, bonds, and cur-
rencies. Fixed Income Research. Goldman Sachs, 1991.
Black, F., and Litterman, R. 1992. Global portfolio optimization. Financial Analysts
Journal, 48(5):28–43.
Bollerslev, T. 1986. Generalized autoregressive conditional heteroskedasticity. Jour-
nal of Econometrics, 31:307–327.
Bollerslev, T., and Engle, R. 1986. Modelling the persistence of conditional vari-
ances. Econometric Reviews, 5:1–50; 81–87.
Branco, M., and Dey, D. 2001. A general class of multivariate skew elliptical
distributions. Journal of Multivariate Analysis, 79:99–113.
Brockwell, P., and Davis, R. Time Series: Theory and Methods, 2nd ed. Berlin:
Springer, 1998.
Buckle, D. 1995. Bayesian inference for stable distributions. Journal of the American
Statistical Association, 90(2):605–613.
Busse, J., and Irvine, P. 2006. Bayesian alphas and mutual fund persistence. Journal
of Finance, 61(5):2251–2288.
Cai, J. 1994. A Markov model of switching-regime ARCH. Journal of Business and
Economic Statistics, 12(3):309–316.
Carlin, B., Gelfand, A., and Smith, A. 1992. Hierarchical Bayesian analysis of change
point problems. Applied Statistics, 41(2):389–405.

300
REFERENCES
Carlin, B., Polson, N., and Stoffer, D. 1992. A Monte Carlo approach to nonnor-
mal and nonlinear state-space modeling. Journal of the American Statistical
Association, 87(418):493–500.
Casarin, R.
Bayesian
inference
for
generalized
Markov
switching
stochas-
tic volatility models. Working Paper, 2004, CEREMADE. Available at
http://www.citeseer.ist.psu.edu.
Chen, N., Roll, R., and Stephen, R. 1986. Economic forces and the stock market.
Journal of Business, 59(3):383–403.
Chernov, M., Gallant, R., Ghysels, E., and Tauchen, G. 2003. Alternative models
for stock price dynamics. Journal of Econometrics, 116(1–2):225–257.
Chesney, M., and Scott, L. 1989. Pricing European currency options: A comparison
of the modified Black-Scholes model and a random variance model. Journal of
Financial and Quantitative Analysis, 24(3):267–284.
Chib, S., and Greenberg, E. 1995. Understanding the Metropolis-Hastings algo-
rithm. American Statistician, 49(4):327–335.
Chib, S., Nardari, F., and Shephard, N. 2002. Markov Chain Monte Carlo meth-
ods for stochastic stochastic volatility models. Journal of Econometrics,
(108):281–316.
Chopra, V., and Ziemba, W. 1993. The effect of errors in means, variances, and
covariances on optimal portfolio choice. Journal of Portfolio Management,
19(2):6–11.
Chung, K. A Course in Probability Theory Revised, 2nd ed. New York: Academic
Press, 2000.
Clark, P. 1973. A subordinated stochastic process model with finite variance for
speculative prices. Econometrica, 41(1):135–155.
Connor, G. 1995. The three types of factor models: A comparison of their explana-
tory power. Financial Analysts Journal, 51(3):42–46.
Cooke, R. Experts in Uncertainty: Opinion and Subjective Probability in Science.
New York: Oxford University Press, 1991.
Cowles, M., and Carlin, B. 1996. Markov Chain Monte Carlo convergence diag-
nostics: A comparative review. Journal of the American Statistical Association,
91(3):883–904.
Cremers, M. 2002. Stock return predictability: A Bayesian model selection perspec-
tive. Review of Financial Studies, 15(4):1223–1249.
Damien, P., Wakefield, J., and Walker, S. 1999. Gibbs sampling for Bayesian non-
conjugate and hierarchical models by using auxiliary variables. Journal of the
Royal Statistical Society, Series B, 61:331–344.
de Jong, P., and Shephard, N. 1995. The simulation smoother for time series models.
Biometrika, 82(2):339–350.
Demarta, S., and McNeil, A. 2005. The t-copula and related copulas. International
Statistical Review, 73(1):111–129.
Diebold, F., and Inoue, A. 2001. Long memory and regime switching. Journal of
Econometrics, 105(1):131–159.
Dittmar, R. 2002. Nonlinear pricing kernels, kurtosis preference, and evidence from
the cross-section of equity returns. Journal of Finance, 57(1):368–403.

References
301
Durbin, J., and Koopman, S. Time Series Analysis by State Space Methods. New
York: Oxford University Press, 2001.
Durbin, J., and Koopman, S. 2002. A simple and efficient simulation smoother for
state space time series analysis. Biometrika, 89(3):603–615.
El Ghaoui, L., and Lebret, H. 1997. Robust solutions to least-squares prob-
lems with uncertain data. SIAM Journal of Matrix Analysis Applications,
18(4):1035–1064.
Engle, R. 1982. Autoregressive conditional heteroscedasticity with estimates of the
variance of United Kingdom inflation. Econometrica, 50(4):987–1007.
Engle, R., Lilien, D., and Robins, R. 1987. Estimating time-varying risk premia in
the term structure: The ARCH-M model. Econometrica, 55(2):391–407.
Eraker, B., Johannes, M., and Polson, N. 2003. The impact of jumps in equity index
volatility and returns. Journal of Finance, 58(3):1269–1300.
Fabozzi, F., Focardi, S., and Kolm, P. Financial Modeling of the Equity Market:
From CAPM to Cointegration. Hoboken, NJ: John Wiley & Sons, 2006.
Fabozzi, F., Focardi, S., and Kolm, P. 2001. Incorporating trading strategies into the
Black-Litterman framework. Journal of Trading, 1(2):28–37.
Fabozzi, F., Jones, F., and Vardharaj, R. Multi-factor equity risk models. In
F. Fabozzi and H. Markowitz (eds.), The Theory and Practice of Investment
Management. Hoboken, NJ: John Wiley & Sons, 2002.
Fama, E. 1965. The behavior of stock market prices. Journal of Business,
38(1):34–105.
Fama, E. 1970. Efficient capital markets: A review of theory and empirical work.
Journal of Finance, 25(2):383–417.
Fama, E. 1991. Efficient capital markets: II. Journal of Finance, 46(5):1575–1617.
Fama, E., and French, K. 1992. The cross-section of expected stock returns. Journal
of Finance, 47(2):427–465.
Fama, E., and MacBeth, J. 1973. Risk, return, and equilibrium: Empirical tests.
Journal of Political Economy, 81(3):607–636.
Favre, L., and Galeano, J. 2002. Mean-modified value-at-risk with hedge funds.
Journal of Alternative Investments, 5(2):21–25.
Feller, W. An Introduction to Probability Theory and Its Applications, vol 2, 2nd
ed New York: John Wiley & Sons, 1971.
Fernandez, C., and Steel, M. 1998. On Bayesian modeling of fat tails and skewness.
Journal of the American Statistical Association, 93(441):359–371.
Fornari, F., and Mele, A. 1996. Modeling the changing asymmetry of conditional
variances. Economics Letters, 50(2):197–203.
Francq, C., and Zako¨ıan, J.-M. 2001. Stationarity of multivariate Markov-switching
ARMA models. Journal of Econometrics, 102:339–364.
Frost, P., and Savarino, J. 1986. An empirical Bayes approach to efficient portfolio
selection. Journal of Financial and Quantitative Analysis, 21(3):293–305.
Gallant, R., and Tauchen, G. 1996. Which moments to match. Econometric Theory,
12(4):657–681.
Garthwaite, P., Kadane, J., and O’Hagan, A. 2005. Statistical methods for elicit-
ing probability distributions. Journal of the American Statistical Association,
100(470):680–701.

302
REFERENCES
Gelman, A., Roberts, G., and Gilks, W. Efficient Metropolis jumping rules. In
J. Bernardo, J. Berger, A. Dawid, and A. Smith, editors, Bayesian Statistics,
vol. 5, pp. 599–608, 1996.
Gelman, A., and Rubin, D. 1992. Inference from iterative simulation using multiple
sequences. Statistical Science, 7(4):457–472.
Genest, C., and Zidek, J. 1986. Combining probability distributions: A critique and
an annotated bibliography. Statistical Science, 1(1):114–148.
Geweke, J. Bayesian comparison of econometric models. Working Paper 532. Federal
Reserve Bank of Minneapolis. 1994.
Geweke, J. Priors for macroeconomic time series and their application. Working
Paper 64. Federal Reserve Bank of Minneapolis. 1993b.
Geweke, J. 1989. Bayesian inference in econometric models using Monte Carlo
integration. Econometrica, 57(6):1317–1339.
Geweke, J. 1993a. Bayesian treatment of the independent Student’s t linear model.
Supplement: Special Issue on Econometric Inference Using Simulation Tech-
niques. Journal of Applied Econometrics, 8:S19–S40.
Geweke, J. Contemporary Bayesian Econometrics and Statistics. Hoboken NJ: John
Wiley & Sons, 2005.
Geyer, C. 1992. Practical Markov Chain Monte
Carlo. Statistical Science,
7(4):473–481.
Ghysels, E., Harvey, A., and Renault, E. Stochastic volatility. In G. Maddala and
C. Rao (eds.), Statistical Methods in Finance, Handbook of Statistics 14,
pp. 119–191. Amsterdam: Elsevier Science, 1996.
Ghysels, E., McCulloch, R., and Tsay, R. 1998. Bayesian inference for periodic
regime-switching models. Journal of Applied Econometrics, 13(2):129–143.
Giacometti, R., Bertocchi, M., Rachev, S., and Fabozzi, F. Stable distributions in the
Black-Litterman approach to asset allocation. Quantitative Finance, forthcom-
ing. 2007.
Gilks, W., Richardson, S., and Spiegelhalter, D. Markov Chain Monte Carlo in
Practice. Boca Raton, FL: Chapman Hall/CRC, 1996.
Gilks, W. and Wild, P. 1992. Adaptive rejection sampling for Gibbs sampling.
Applied Statistics, 41(2):337–348.
Glosten, L., Jagannathan, R., and Runkle, D. 1993. On the relation between the
expected value and the volatility of the nominal excess return on stocks. Journal
of Finance, 48(5):1779–1801.
Goldberg, D. Genetic Algorithms in Search, Optimization, and Machine Learning.
Boston: Addison-Wesley, 1989.
Goldfarb, D., and Iyengar, G. 2003. Robust portfolio selection problems. Mathe-
matics of Operations Research, 28(1):1–38.
Grinold, R. 1989. The fundamental law of active management. Journal of Portfolio
Management, 15(3):30–37.
Grinold, R., and Kahn, R. Active Portfolio Management: A Quantitative Approach
for Producing Superior Returns and Controlling Risk, 2nd ed. New York:
McGraw-Hill, 2000.
Haas, M., Mittnik, S., and Paolella, M. 2004. A new approach to Markov-switching
GARCH models. Journal of Financial Econometrics, 2(4):493–530.

References
303
Hamilton, J. 1989. A new approach to the economic analysis of nonstationary time
series and the business cycle. Econometrica, 57:357–384.
Hamilton, J., and Susmel, R. 1994. Autoregresive conditional heteroskedasticity and
changes in regime. Journal of Econometrics, 64:307–333.
Hansen, B. 1994. Autoregressive conditional density estimation. International Eco-
nomic Review, 35(3):705-730.
Harvey, A. Forecasting, Structural Time Series Models and the Kalman Filter
(reprint). Cambridge: Cambridge University Press, 1991.
Harvey, A., Ruiz, E., and Shephard, N. 1994. Multivariate stochastic variance mod-
els. Review of Economic Studies, 61(2):247–264.
Harvey, C., Liechty, J., Liechty, M., and M¨uller, P. Portfolio selection with higher
moments. Social Science Research Network. Working Paper Series. 2004.
Available at http://papers.ssrn.com.
Harvey, C., and Siddique, A. 2000. Conditional skewness in asset pricing tests.
Journal of Finance, 55(3):1263–1295.
Harvey, C., and Zhou, G. 1990. Bayesian inference in asset pricing tests. Journal of
Financial Economics, 26:221–254.
Hastings, W. 1970. Monte Carlo sampling methods using Markov chains and their
applications. Biometrika, 57(1):97–109.
He, G., and Litterman, R. The intuition behind Black-Litterman model portfolios.
Social Science Research Network. Working Paper Series, 1999. Available at
http://papers.ssrn.com.
Henneke, J., Rachev, S., and Fabozzi, F. MCMC based estimation of Markov-
switching ARMA-GARCH models. Technical Report. Department of Statistics
and Applied Probability. University of California, Santa Barbara. 2007.
Herold, U. 2003. Portfolio construction with qualitative forecasts. Journal of Port-
folio Management, 30(1):61–72.
Hoeting, J., Madigan, D., Raftery, A., and Volinsky, C. 1999. Bayesian model aver-
aging: A tutorial. Statistical Science, 14(4):382–417.
Holton, G. 2004. Defining risk. Financial Analysts Journal, 60(6):19–25.
Hsieh, D. 1991. Chaos and nonlinear dynamics: Application to financial markets.
Journal of Finance, 46(5):1839–1877.
Hsu, J. 1995. Generalized Laplacian approximations in Bayesian inference. The
Canadian Journal of Statistics, 23(4):399–410.
Hull, J., and White, A. 1987. The pricing of options on assets with stochastic
volatilities. Journal of Finance, 42:281–300.
Hull, J., and White, A. 1987. Pricing of options on assets with stochastic volatilities.
Journal of Finance, 42(2):281–300.
Jacquier, E., Polson, N., and Rossi, P. 1994. Bayesian analysis of stochastic volatility
models. Journal of Business and Economic Statistics, 12(4):371–389.
Jacquier, E., Polson, N., and Rossi, P. 2004. Bayesian analysis of stochastic volatil-
ity models with fat-tails and correlated errors. Journal of Econometrics,
(122):185–212.
Jeffreys, H. Theory of Probability. New York: Oxford University Press, 1961.
Jegadeesh, N., and Titman, S. 1993. Returns to buying winners and selling losers:
Implications for stock market efficiency. Journal of Finance, 48(1):65–91.

304
REFERENCES
Jobson, J., and Korkie, B. 1980. Estimation for Markowitz efficient portfolios.
Journal of the American Statistical Association, 75(371):544–554.
Jobson, J., Korkie, B., and Ratti, V. Improved estimation for Markowitz portfolios
using James-Stein type estimators. Proceedings of the American Statistical
Association, Business and Economic Statistics Section, 1979.
Johnson, N., Kotz, S., and Balakrishnan, N. Continuous Univariate Distributions,
Vol 1. New York: John Wiley & Sons, 2nd ed, 1994.
Johnson, R., and Wichern, D. Applied Multivariate Statistical Analysis. Upper Saddle
River, NJ: Prentice Hall, 2002.
Jones, M., and Faddy, M. 2003. A skew extension of the t distribution, with
applications. Journal of the Royal Statistical Society, Series B, 65:159–174.
Jorion, P. 1986. Bayes-Stein estimation for portfolio analysis. Journal of Financial
and Quantitative Analysis, 21(3):279–292.
Jorion, P. 1991. Bayesian and CAPM estimators of the means: Implications for
portfolio selection. Journal of Banking and Finance, 15(3):717–727.
Jorion, P. 1992. Portfolio optimization in practice. Financial Analysts Journal,
48(1):68–75.
Kandel, S., McCulloch, R., and Stambaugh, R. 1987. Bayesian inference and port-
folio efficiency. Review of Financial Studies, 8(1):1–53.
Kandel, S., and Stambaugh, R. 1996. On the predictability of stock returns: An
asset-allocation perspective. Journal of Finance, 51(2):385–424.
Kass, R., Tierney, L., and Kadane, J. 1989. Approximate methods for assessing
influence and sensitivity in Bayesian analysis. Biometrika, 76(4):663–674.
Kass, R., and Wasserman, L. 1996. The selection of prior distributions by formal
rules. Journal of the American Statistical Association, 91(435):1343–1370.
Khindanova, I., and Rachev, S. Value-at-risk: Recent advances. In G. Anastassiou
(ed.), Handbook of Analytic-Computational Methods in Applied Mathematics,
pp. 801–858. Boca Raton, FL: Chapman & Hall/CRC, 2000.
Kim, C., and Nelson, C. 1999. Has the U.S. economy become more stable? A
Bayesian approach based on a Markov-switching model of the business cycle.
The Review of Economics and Statistics, 81(4):608–616.
Kim, S., Shephard, N., and Chib, S. 1998. Stochastic volatility: Likelihood infer-
ence and comparison with ARCH models. Review of Economic Studies,
65(3):361–393.
Klaassen, F. Improving GARCH volatility forecasts. Social Science Research Net-
work. Working Paper Series, 1998. Available at http://papers.ssrn.com.
Koopman, S. 1993. Disturbance smoother for state space models. Biometrika,
80(1):117–126.
Koopman, S., Shephard, N., and Doornik, J. 1999. Statistical algorithms for models
in state space using SsfPack 2.2. Econometrics Journal, 2:107–160.
Kotz, S., Balakrishnan, N., and Johnson, N. Continuous Multivariate Distributions,
Models and Applications, vol. 1. New York: John Wiley & Sons, 2nd ed.,
2000.
Kraus, A. and Litzenberger, R. 1976. Skewness preferences and the valuation of risk
assets. Journal of Finance, 31(4):1085–1100.

References
305
Lamantia, F., Ortobelli, S., and Rachev, S. 2006. An empirical comparison among
VaR models and time rules with elliptical and stable distributed returns.
Investment Management and Financial Innovations, 3(1):8–29.
Lamantia, F., Ortobelli, S., and Rachev, S. 2006. VaR, CVaR, and time rules with
elliptical and asymmetric stable distributed returns. Investment Management
and Financial Innovations, 4(1):19–39.
Lamoureux, C., and Lastrapes, W. 1990. Persistence in variance, structural change,
and the GARCH model. Journal of Business and Economic Statistics,
8(2):225–234.
Larsen, G., and Resnick, B. 2001. Parameter estimation techniques, optimization
frequency, and portfolio return enhancement. Journal of Portfolio Management,
27(4):27–34.
Ledoit, O., and Wolf, M. 2003. Improved estimation of the covariance matrix of
stock returns with an application to portfolio selection. Journal of Empirical
Finance, 10(5):603–621.
Leonard, T. 1982. Comment on ‘‘A simple predictive density function.’’ Journal of
the American Statistical Association, 77:657–658.
Leonard, T., and Hsu, J. Bayesian Methods: An Analysis for Statisticians and Inter-
disciplinary Researchers. Cambridge: Cambridge University Press, 1999.
Leonard, T., Hsu, J., and Tsui, K. 1989. Bayesian marginal inference. Journal of the
American Statistical Association, 84(408):1051–1058.
Litterman, R., and the Quantitative Resources Group. Goldman Sachs Asset
Management. Modern Investment Management: An Equilibrium Approach.
Hoboken, NJ: John Wiley & Sons, 2003.
Litterman, R., and Winkelmann, K. Estimating covariance matrices. Risk Manage-
ment Series. Goldman Sachs, 1998.
Lo, A., and MacKinlay, A. 1990. Data-snooping biases in tests of financial asset
pricing models. Review of Financial Studies, 3(3):431–468.
Madigan, D., and Raftery, A. 1994. Model selection and accounting for model
uncertainty in graphical models using Occam’s window. Journal of the American
Statistical Association, 89(428):1335–1346.
Mahieu, R., and Schotman, P. 1998. An empirical application of stochastic volatility
models. Journal of Applied Econometrics, 13(4):333–359.
Mandelbrot, B. 1963. The variation of certain speculative prices. Journal of Business,
36(4):394–419.
Markowitz, H. 1952. Portfolio selection. Journal of Finance, 7(1):77–91.
Markowitz, H. Portfolio Selection: Efficient Diversification of Investments. New
York: Blackwell, 1959.
Markowitz, H. Autobiography. In Tore Fr¨angsmyr (ed.), Les Prix Nobel. The Nobel
Prizes 1990. Nobel Foundation, 1991.
Markowitz, H., and Usmen, N. 1996. The likelihood of various stock market return
distributions, part I: Principles of inference. Journal of Risk and Uncertainty,
13:207–219.
McCullagh, P., and Nelder, J. Generalized Linear Models, 2nd ed. Boca Raton, FL:
Chapman and Hall/CRC, 1989.

306
REFERENCES
McCulloch, R.,
and
Rossi, P.
1990.
Posterior,
predictive,
and
utility-based
approaches to testing the Arbitrage Pricing Theory. Journal of Financial Eco-
nomics, 28(1):7–38.
McNeil, A., Frey, R., and Embrechts, P. Quantitative Risk Management: Concepts,
Techniques and Tools. Princeton, NJ: Princeton University Press, 2005.
Merton, R. 1980. An analytic derivation of the efficient portfolio frontier. Journal
of Financial and Quantitative Analysis, 7(4):1851–1872.
Metropolis, N., Rosenbluth, A., Rosenbluth, M., Teller, A., and Teller, E. 1953.
Equation of state calculations by fast computing machines. Journal of Chemical
Physics, 21(6):1087–1092.
Meucci, A. Beyond Black-Litterman in practice: A five-step recipe to input views on
non-normal markets. Working Paper. 2006b. Available at www.symmys.com.
Meucci, A. February 2006b. Beyond Black-Litterman: Views on non-normal mar-
kets. Journal of Risk.
Michaud, R. Efficient Asset Management: A Practical Guide to Stock Portfolio
Optimization. New York: Oxford University Press, 1998.
Mittnik, S., and Paolella, M. 2000. Conditional density and value-at-risk prediction
of Asian currency exchange rates. Journal of Forecasting, 19(4):313–333.
Neil, M., Fenton, N., and Tailor, M. 2005. Using Bayesian networks to model
expected and unexpected operational losses. Risk Analysis, 25(4):963–972.
Nelson, D. 1991. Conditional heteroskedasticity in asset returns: A new approach.
Econometrica, 59(2):347–370.
Nelson, D., and Foster, D. 1994. Asymptotic filtering theory for univariate ARCH
models. Econometrica, 62(1):1–41.
Norris, J. Markov Chains. Cambridge: Cambridge University Press, 1998.
Omori, Y., Chib, S., Shephard, N., and Nakajima, J. Stochastic volatility with lever-
age: Fast and efficient likelihood inference. Journal of Econometrics, 2006.
doi:10.1016/j.jeconom.2006.07.008.
Ortobelli, S., Rachev, S., Stoyanov, S., Fabozzi, F., and Biglova, A. 2005. The proper
use of risk measures in portfolio theory. International Journal of Theoretical
and Applied Finance, 8(8):1107–1133.
Palm, F. GARCH models of volatility. In G. Maddala and C. Rao (eds.), Statistical
Methods in Finance: Handbook of Statistics 14, pp. 209–240. Amsterdam:
Elsevier Science, 1996.
P´astor, L. 2000. Portfolio selection and asset pricing models. Journal of Finance,
55(1):179–223.
P´astor, L. and Stambaugh, R. 1999. Costs of equity capital and model mispricing.
Journal of Finance, 54(1):67–121.
Pelikan, M. Hierarchical Bayesian Optimization Algorithm: Toward a New Gener-
ation of Evolutionary Algorithm. Berlin: Springer, 2005.
Rachev, S., Khindanova, I., and Schwartz, E. 2001. Stable modeling of value-at-risk.
Mathematical and Computer Modeling, 34(9):1223–1259.
Rachev, S., Martin, D., Racheva-Iotova, B., and Stoyanov, S. Stable ETL optimal
portfolios and extreme risk management. In Decisions in Banking and Finance.
Berlin: Springer/Physika, 2007.

References
307
Rachev, S., Menn, C., and Fabozzi, F. Fat-Tailed and Skewed Asset Return Distri-
butions: Implications for Risk Management, Portfolio selection, and Option
Pricing. Hoboken, NJ: John Wiley & Sons, 2005.
Rachev, S., and Mittnik, S. Stable Paretian Models in Finance. New York: John
Wiley & Sons, 2000.
Rachev, S., Mittnik, S., Fabozzi, F., Foccardi, S., and Jasi´c, T. Financial Economet-
rics: From Basics to Advanced Modeling Techniques. Hoboken, NJ: John Wiley
& Sons, 2007.
Rachev, S., Ortobelli, S., and Schwartz, E. The problem of optimal asset allocation
with stable distributed returns. In A. Krinik and R. Swift (eds.), Stochastic
Processes and Functional Analysis: A Volume of Recent Advances in Honor
of M. M. Rao, Lecture Notes in Pure and Applied Mathematics, pp. 295–347.
New York: Marcel Dekker, 2004.
Rachev, S., Ortobelli, S., Stoyanov, S., and Fabozzi, F. Desirable properties of an
ideal risk measure in portfolio theory. International Journal of Theoretical and
Applied Finance, forthcoming (2007).
Rachev, S., and R¨uschendorf, L. 1994. On the Cox, Ross, and Rubinstein model for
option pricing. Theory of Probability and its Applications, 39(1):150–190.
Rachev, S., Stoyanov, S., Biglova, A., and Fabozzi, F. An empirical examination
of daily stock return distributions for U.S. stocks. In D. Baier, R. Decker,
and L. Schmidt-Thieme (eds.), Data Analysis and Decision Support, Studies in
Classification, Data Analysis, and Knowledge Organization. Berlin: Springer,
2005.
Rachev, S., Stoyanov, S., and Fabozzi, F. Advanced Stochastic Models, Risk Assess-
ment, and Portfolio Optimization: The Ideal Risk, Uncertainty, and Perfor-
mance Measures. Hoboken, NJ: John Wiley & Sons, 2007.
Rockafellar, R., and Uryasev, S. 2000. Optimization of conditional value-at-risk.
Journal of Risk, 2(3):21–41.
Rockafellar, R., and Uryasev, S. 2002. Conditional value-at-risk for general loss
distributions. Journal of Banking and Finance, 26(7):1443–1471.
Rockafellar, T., Uryasev, S., and Zabarankin, M. Portfolio analysis with general
deviation measures. Industrial and Systems Engineering Research Report No.
2003-8. University of Florida, 2003.
Roll, R. 1977. A critique of the Asset Pricing Theory’s tests—Part I: On past
and potential testability of the theory. Journal of Financial Economics,
4(1):129–176.
Rouwenhorst, G. 1998. International momentum strategies. Journal of Finance,
53:267–283.
Rubinstein, M. 1973. A comparative static analysis of risk premium. Journal of
Business, 46(2):605–615.
Sahu, S., Dey, D., and Branco, M. 2003. A new class of multivariate skew distribu-
tions with applications to Bayesian regression models. The Canadian Journal
of Statistics, 29(2):125–150.
Satchell, S., and Scowcroft, A. 2000. A demystification of the Black-Litterman
model: Managing quantitative and traditional portfolio construction. Journal
of Asset Management, 1(2):138–150.

308
REFERENCES
Scherer, B. 2002. Portfolio resampling: Review and critique. Financial Analysts
Journal, 58(6):98–109.
Sharpe, W. 1963. A simplified model for portfolio analysis. Management Science,
9:277–293.
Sharpe, W. 1994. The Sharpe ratio. Journal of Portfolio Management, 21(1):49–58.
Shephard, N., editor. Stochastic Volatility: Selected Readings. New York: Oxford
University Press, 2005.
So, M., Lam, K., and Li, W. 1998. A stochastic volatility model with Markov
switching. Journal of Business and Economic Statistics, 16(2):244–253.
Sortino, F. 2000. Upside-potential ratios vary by investment style. Pensions and
Investments, 28:30–35.
Sortino, F., and Satchell, S. (eds). Managing Downside Risk in Financial Markets.
Oxford: Butterworth-Heinemann, 2001.
Stambaugh, R. 1997. Analyzing investments whose histories differ in length. Journal
of Financial Economics, 45(2):285–331.
Stambaugh, R. 1999. Predictive regressions. Journal of Financial Economics,
54(2):375–421.
Stein, J. Inadmissibility of the usual estimator for the mean of a multivariate
distribution. Proceedings of the Third Berkeley Symposium on Mathematics
Statistics and Probability, 1:197–206. University of California Press. 1956.
Stroud, J., M¨uller, P., and Polson, N. 2003. Nonlinear state-space models with
state-dependent variances. Journal of the American Statistical Association,
98(462):377–386.
Tauchen, R., and Pitts, M. 1983. The price variability-volume relationship on spec-
ulative markets. Econometrica, 51(2):485–505.
Taylor, S. Financial returns modeled by the product of two stochastic processes—a
study of daily sugar prices 1961-79. In O. Anderson (ed.), Time Series Analysis:
Theory and Practice I, pp. 203–226. Amsterdam: Elsevier Science, 1982.
Taylor, S. Modeling Financial Time Series. New York: John Wiley & Sons, 1986.
Taylor, S. Asset Price Dynamics, Volatility, and Prediction. Princeton, NJ: Princeton
University Press, 2005.
Tierney, L., and Kadane, J. 1986. Accurate approximations for posterior moments
and marginal densities. Journal of the American Statistical Association,
81(393):82–86.
Treynor, J., and Black, F. 1973. How to use security analysis to improve portfolio
selection. Journal of Business, 46(1):66–86.
van Dyk, D., and Meng, X. 2001. The art of data augmentation (with discussion).
Journal of Computational and Graphical Statistics, 10(1):1–111.
Wang, J., and Zivot, E. 2000. A Bayesian time series model of multiple structural
changes in level, trend, and variance. Journal of Business and Economic
Statistics, 18(3):374–386.
Wang, Z. 1998. Efficiency loss and constraints on portfolio holdings. Journal of
Financial Economics, 48(2):359–375.
West, M., and Harrison, J. Bayesian Forecasting and Dynamic Models, 2nd ed.
Berlin: Springer, 1997.

References
309
Wild, P., and Gilks, W. 1992. Algorithm AS 287: Adaptive rejection sampling from
log-concave density functions. Applied Statistics, 42(4):701–709.
Winkelmann, K. 2004. Improving portfolio efficiency. Journal of Portfolio Manage-
ment, 30(2):23–38.
Yamai, Y., and Yoshiba, T. Comparative analyses of expected shortfall and value-
at-risk: Their estimation, error, decomposition, and optimization. Monetary
and Economic Studies, 87–121, January, 2002.
Young, M. 1998. A minimax portfolio selection rule with linear programming
solution. Management Science, 44(5):673–683.
Yu, B., and Mykland, P. Looking at Markov samplers through cusum path plots:
A simple diagnostic idea. Technical Report No. 413. Department of Statistics.
University of California, Berkeley, 1994.
Zellner, A. An Introduction to Bayesian Inference in Econometrics. New York: John
Wiley & Sons, 1971.
Zhang, Y., and Rachev, S. 2006. Risk attributions and portfolio performance mea-
surements. Journal of Applied Functional Analysis, 4(1):373–402.


Index
Absolute risk aversion, 180n
Active portfolio management,
Black-Litterman model
(relationship), 154–159
After-burn-in simulation, 76
Alpha, 120–121
distribution, posterior moments,
157–158
forecast, 158–159
perspective, 157–158
Arbitrage Price Theory (APT), 118,
163, 281
certainty equivalent returns,
173–174
distributional assumptions,
172–173
posterior distributions, 172–173
predictive distributions, 172–173
testing, 171–174
ARCH. See Autoregressive
conditionally heteroskedastic
ARMA. See Autoregressive moving
average
Asset pricing models, 118
confidence, 123
preliminaries, 119–121
relationship. See Prior beliefs
validity, confidence
(incorporation), 128–129
Asset pricing relationship, validity,
145n
Asset returns
covariance matrix, 143
nonnormality, 188–189
time-series regression, usage,
164–165
Asymmetric Student’s
t-distributions, 250–251
Asymmetric volatility, 189, 195
Asymmetry parameter, 297
AT&T stock, transaction data
(consideration), 16–17
Autocorrelations, impact. See
Convergence
Autoregressive conditionally
heteroskedastic (ARCH)
ARCH-in-mean model, 190
ARCH-type model, 186, 194
selection, 200
ARCH-type volatility models,
Bayesian estimation, 202
distributional setup, 204–206
terms, usage, 187
Autoregressive moving average
(ARMA). See Multivariate
ARMA
ARMA(1,1)-GARCH(1,1) model,
estimation, 193
ARMA(1,1) process, 215
return model, 190
Autoregressive process,
time-reversibility (usage),
233
Auxiliary model, 196–197
Bayesian decisions, Greenspan
outline, 3
Bayesian empirical tests. See
Mean-variance efficiency
311

312
INDEX
Bayesian estimation. See Stochastic
volatility model
Bayesian hypothesis, comparison,
32–34
Bayesian inference process, 22
Bayesian intervals, 32
Bayesian linear regression model, 43
Bayesian methodology, 165
Bayesian methods
application, 4n
introduction, 1
overview, 4–5
selection, 200–201
Bayesian model averaging (BMA),
131–134
methodology, 130–131
portfolio selection, 133–134
posterior model probabilities,
132–133
posterior parameter distributions,
132–133
predictive distribution, 133–134
prior distributions, 131–132
Bayesian numerical computation,
61
Bayesian paradigm, 6
Bayesian portfolio problem, 177
Bayesian portfolio selection,
101–108
advanced techniques, 247
illustration, 106–108
problem, solution, 173
Bayesian predictive inference,
34–35
Bayes’ Theorem, 6, 10–21
classification, relationship, 14–15
continuous version, 19
discrete version, consideration,
11
model selection, relationship, 14
Benchmark efficiency, confidence,
157
Benchmark inefficiency, 156
Benchmark parameters, posterior
distributions, 125–126
Benchmark portfolios, 122
efficiency, 169
Benchmark timing, 156
Berger, James, 12n, 23n, 25n
Bernardo, Jos´e, 12n, 25n
Bernoulli-distributed random
variable, 242
Bernoulli likelihood function, 132n
Beta
definition, 127n
distribution, basis, 237–238
estimation. See Stocks
marginal (unconditional)
distribution, 47
posterior densities, 56e
posterior inference, 55e
Beta conditional, posterior
distribution, 46
Beta-distributed random variable,
25
Beta distribution, 17n
conjugate prior distribution, 20
Beta function, 18
Binary data, analysis, 82n
Binary dependent variable,
Bernoulli distribution, 83
Binomial parameter, prior
distributions (density curves),
18e
Binomial probability
Bayesian inference, 15–21
informative prior elicitation, 25
Black-Litterman (BL) approach,
extension, 263–270
stable distribution, usage,
270–272
Black-Litterman (BL) framework,
extension (consideration), 255

Index
313
Black-Litterman (BL) model, 94,
118
market equilibrium, usage, 264
perspective, 157–158
relationship. See Active portfolio
management
trading strategies, incorporation,
153–154
Black-Litterman (BL) optimal
allocation, illustration,
149–152
Black-Litterman (BL) portfolio
selection framework, 141
absolute view, 144
distributional assumptions,
144–146
investor perspective, 144
market information, 144–145
preliminaries, 142–146
relative view, 144
subjective views, 145–146
values, selection, 147–148
Black-Scholes option-pricing
formula, constant volatility
(assumption), 194n
Block structure M-H algorithm,
72–73
extension, 73
B/M. See Book value to market
value ratio
BMA. See Bayesian model averaging
Book-to-market (BM) ratios, 53,
175, 282
Book-to-market (BM) value, 134
Book value to market value ratio
(B/M), 163
Broad-based index, 165–166
Burn-in fraction, 75. See also
Markov chain
Burn-in simulation. See
After-burn-in simulation
Buy-and-hold investor, 178
Candidate-generating density, 67
Candidate model, likelihood
function, 138–140
Capital Asset Pricing Model
(CAPM), 118, 163
assumptions, 120
deficiency, 280
distributional assumptions,
168–169
empirical analogue, 120
equilibrium pricing model, 166
extension, 257n
implication, 119, 165
inference, usage, 134
posterior distributions, 168–169
testing, inefficiency measures
(usage), 167–171
usage, 128
validity, uncertainty, 129e
Cash flow/total debt ratio, 86
CDF. See Cumulative distribution
function
Certainty-equivalence scenario,
105, 107–108
Certainty equivalent returns. See
Arbitrage Price Theory
Common-factor risk component,
290–291
Conditional densities, product, 192
Conditional distribution. See
Unobserved volatility
expression, 240
sampling, 261
Conditional log-posterior
distribution, kernel, 222
Conditional mean, modeling,
189–190
Conditional posterior distribution.
See Gamma
elicitation, 227–228
obtaining, 221
usage, 209–210, 219–222

314
INDEX
Conditional value-at-risk (CVaR),
268, 274–275
decomposition, 289–292
definition, 289
minimization, usage, 269
optimization, 276–277
usage, 280
Conditional variance parameters
posterior draws, histograms,
212e
vector, prior means (elicitation),
223
Conditional volatility dynamics,
regimes (existence), 211
Confidence
cases, 150–151
cross-sectional momentum
strategy (representation),
154
incorporation. See Asset pricing
models
interval/level, 148
relative views, effect
(comparison). See
High-confidence relative
view
Conjugate prior distributions,
27–28. See also Beta
distribution
Constant relative risk aversion
(CRRA), 180n
Contemporaneous stock return, 175
Contour plot, usage. See Normal
distribution
Convergence
autocorrelations, impact, 74–75
diagnostics, 74–77
illustration, 81e
monitoring. See Cumsum
convergence monitoring;
Parallel chains convergence
monitoring
Copulas. See Student’s t-copulas
estimation, 278–279
opinion pooling, 263–270
overview, 277–279
Corporate defaults, Poisson
distribution, 8
Coskewness, 257–258
definition, 257n
Country index, volatility, 153–154
Covariance
maximum likelihood, 98–99
return matrix, calculation,
172–173
returns, 160
Covariance matrix. See Asset
returns; Maximum likelihood
estimate; Proposal distribution
combined-sample MLE, 115
computation, 159–160
determinant, 58
estimation, 159–161
knowledge, 31
truncate MLE, 113–114
Criterion function, value
(computation), 198
Cross-sectional regression, 165
estimation, 287, 293
CRRA. See Constant relative risk
aversion
Cumsum convergence monitoring,
75
Cumulative distribution function
(CDF)
computation, 227, 278
inversion method, 228
usage. See Inverse-fitted
univariate CDFs
Cumulative excess return,
prediction, 178
Cumulative risk-free return, 181
Current assets/current liabilities
ratio, 86

Index
315
Current assets/net sales ratio, 86
CVaR. See Conditional
value-at-risk
Data-generating process, 130
value, estimation. See True
data-generating process
Data precision, 37
Debt/equity ratios, 189n
Decaying weights, usage, 160
Decision theory, loss functions
(usage), 30n
Decomposition, usage, 186
Default, probability
denotation, 82
predictors, usage, 86
de Finetti, Bruno, 1n
Degrees-of-freedom parameter, 26,
107–108. See also Student’s
t-distribution
calibration, 205
low value, 71
posterior results, 219
prior mean, setting, 211
Density function, term
(usage/assumption), 7n
Dependent simulation, 63
Dependent variables
Bernoulli distribution. See Binary
dependent variable
observations, 44–45
prediction, 50–51
Diffuse improper prior, 46–48
usage, 58–60
Diffuse priors. See Noninformative
priors
Dirichlet distribution, 218n
kernel, logarithm, 220
Dispersion parameter. See Scale
parameter
Distributional assumptions. See
Capital Asset Pricing Model
moments, relationship, 259
Distributional return assumptions,
248–255
Dividend yield (D/P), 163, 175
correlation, 176
Earnings-to-price ratio (E/P), 163
Efficiency, hypothesis, 174
Efficient frontier, 94, 97. See also
Mean-variance efficient frontier
certainty-equivalence setting,
comparison, 107e
illustration, 98e
optimal portfolio, relationship,
105–106
Efficient Market Hypothesis
(EMH), 162
Efficient Method of Moments
(EMM), 196–198
estimation, selection, 198
EGARCH. See Exponential
GARCH
Elliptical distributions, 254, 273
EMH. See Efficient Market
Hypothesis
EMM. See Efficient Method of
Moments
Empirical Bayesian analysis, 28–30
Endogenous regime-switching
models, 214
End-period portfolio value, utility,
96
E/P. See Earnings-to-price ratio
Equilibrium returns, 142–144
nonnormality, impact, 270–272
Ergodic averages, standardization,
79–80
Error, source, 130
Errors-in-variables problem, 165
Estimation error, capture, 93
Estimation risk, 93
consideration, 99

316
INDEX
Euclidean norm, 147n
Evolutionary algorithms, 262n
Ex ante, reference, 121n
Ex ante efficiency, 166n
Excess returns, predictive
distribution (derivation), 177
Excess stock returns, potential
predictors, 131n–132n
Expected equilibrium risk
premiums, 142–143
Expected returns, 271
Expected return-standard deviation
pairs, 108
Explanatory variables
calculation, 83
company-specific characteris-
tics/macroeconomic
variables, 82–83
Exponential distribution, mean, 205
Exponential GARCH (EGARCH),
189
Extra market information, 119
Extreme value distributions, 252
Factors (factor portfolios), 119
covariance matrix, estimates
(obtaining), 285
marginal contribution. See Total
risk
returns
covariance matrix, 283
prediction, 288
sensitivities, estimation, 120–121
Fama and French (FF) three-factor
model, 118
equivalence, 174
inference, 134
Federal Reserve Board, Regulation
T, 169
Filtered volatility estimate, 244
Financial time series, variability,
185
Frequentist statistics, frequentist
interpretation, 1
Full conditional log-posterior
distribution, expression,
239
Fundamental factor models, 282
Future excess returns, predictive
moments, 115–116
Gamma
conditional posterior
distribution, 208–209
distribution, 206
multiplicative property. See
Inverted gamma
distribution
function, 238
Gaussian distribution, 9
Gaussian linear state-space model,
defining, 231n
Gaussian stable distributions, 251n.
See also Non-Gaussian stable
distributions
Generalized autoregressive
heteroscedasticity (GARCH),
160–161. See also Exponential
GARCH
component, presence, 216
effect, 202
GARCH(1,1) estimation, MH
algorithm (usage), 208–211
GARCH(1,1) model
Bayesian estimation. See Simple
GARCH(1,1) model
estimation. See Markov
switching (MS)
GARCH(1,1) model
illustration. See Student’s t
GARCH(1,1) model
GARCH(1,1) process,
properties/estimation,
190–193

Index
317
models. See Markov
regime-switching GARCH
models; Volatility
parameters, 192
Student’s t-distributed
disturbances, 203
SV models, distinguishing, 229
process, changes, 215
process persistence parameter,
191
Generalized error distribution
(GED), 193
Generalized hyperbolic distribution,
250n
Gibbs sampler, 67, 73–74, 203. See
also Griddy Gibbs sampler
posterior summary, 79e
usage, 261
possibility. See Griddy Gibbs
sampler
Global Industry Classification
Standard (GICS), usage,
294n
Global-minimum-variance
portfolio, return, 109–110
Greenspan, Alan, 4n
uncertainty, comment, 2–3
Griddy Gibbs sampler, 226–228
usage, possibility, 210
Half-life, 160
Heavy-tailed multifactor model,
estimation (illustration),
294–297
Heavy-tailed prior distributions,
elicitation, 27
Hessian computation, 70–71
Hessian matrix. See Inverse Hessian
matrix
Heuristic (nonquantitative)
allocation schemes, 141
Hidden Markov process, 219
High-confidence relative view,
low-confidence relative view
(effects, comparison),
151–152
Highest posterior density (HPD),
32n
intervals, 54n
High minus low (HML), 134
High-volatility state, 215–216
Holding period, 154
Hume, David, 1n
Hyperparameters (prior
parameters), 22–23
values
computation, 29
selection, 25n
IC. See Information coefficient
Identity matrix, 122
Importance sampling, 65–66
Independent chain M-H algorithm,
70–72
Independent simulation, 63
Independent variables,
observations, 44–45
matrices, 52
Inefficiency, hypothesis, 174
Inefficiency measures, 167n
distribution, 170e
illustration, 170–171
usage. See Capital Asset Pricing
Model
Information coefficient (IC), 158
Information ratio (IR), 158
Informative prior, 48–50
beliefs, introduction, 106
elicitation, 23. See also Binomial
probability; Location
parameter; Scale parameter
Interval bounds, determined, 32
Intervals, credibility, 54
Intrinsic time, 194n

