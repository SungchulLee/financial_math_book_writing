# Bayesian Model Selection & Estimation

!!! info "Source"
    **Bayesian Methods in Finance** by Svetlozar T. Rachev, John S.J. Hsu, Biliana S. Bagasheva, and Frank J. Fabozzi, Wiley, 2008.
    These notes are used for educational purposes.

## Bayesian Model Selection

Market Efficiency and Return Predictability
173
where F is the sample covariance matrix of factor returns. As in Chapter 7,
the moments of the factor returns, µF and F, could be treated as random
variables, and prior distributions asserted on them in order to reflect the
estimation error contained in them. For the sake of simplicity, here we
assume that µF and F are the true moments.
Consider a diffuse prior for the regression parameters, α, β, and , as
in (9.6), where the mean parameter is E in the restricted case and E0 in the
unrestricted case. Then, the posterior densities of β and  (in the restricted
case) or

α, β

and  (in the unrestricted case) are multivariate normal and
inverted Wishart (as in (9.7) and (9.8), where µ is α + Fβ′ in the unrestricted
case, Fβ′ in the restricted case, and ‘‘hats’’ denote least-squares estimates).
In Chapter 6, we discussed that the predictive distribution of excess
returns is needed to solve the Bayesian portfolio selection problem. Next
period’s excess returns, RT+1, have a multivariate Student t, with T −K −N
degrees of freedom in the unrestricted case and T −K −N + 1 degrees of
freedom in the restricted case (we have one less parameters to estimate,
hence one more degree of freedom).13 Denote next period’s observation of
factor returns by FT+1 (a 1×K vector). The predictive mean and covariance
of future excess returns in the unrestricted case are given, respectively, by
	E = α + FT+1
β′
(9.11)
and
	V =
1
ν −2 S

1 −FT+1

F′F + F′
T+1FT+1
−1F′
T+1
−1
,
(9.12)
where ν is the degrees-of-freedom parameter equal to T−K−N or T−K−
N+1, as explained above, and
S =

R −α + Fβ′′ 
R −α + Fβ′
.
(9.13)
The predictive mean and covariance under the restricted case, 	E0 and
	V0, are obtained by substituting α = 0 in (9.11) and (9.13).
Certainty Equivalent Returns
McCulloch and Rossi (1990) use a negative exponential utility function to
describe investors’ preferences, given by
U

W

= −exp

−AW

,
(9.14)
13See Chapter 3 for the definition of the multivariate Student’s t-distribution.

174
BAYESIAN METHODS IN FINANCE
where A is the coefficient of risk aversion. The end-of-period wealth, W, is
defined as

1 + Rf + Rp

W0, where Rf is the risk-free rate, Rp is the excess
portfolio return (different in the restricted and the unrestricted cases), and
W0 is the initial amount of invested funds. The expected utility can be
shown to be
E

U

W

= −exp

−AW0

1 + Rf + µ

+ A2W2
0
σ 2
2

,
(9.15)
with µ and σ 2 denoting the mean and variance of portfolio return, Rp.
Using the methodology of Chapter 6, we obtain the efficient frontiers in the
unrestricted and the restricted case.
Denote by ω∗and ω∗
0 the vectors of optimal portfolio weights in the
unrestricted and restricted case, respectively. Then, the expected returns
and risks of the optimal portfolio could be computed under the hypothesis
of efficiency (restricted case)—µ∗
0 and σ 2
0
∗—and the hypothesis of ineffi-
ciency (unrestricted case)—µ∗and σ 2∗. To assess the degree of inefficiency,
we compute the difference in certainty equivalent returns under the two
hypotheses,
Rce

α, β, 

−Rce

0, β, 

.
(9.16)
McCulloch and Rossi (1990) construct 10 size-based portfolios, whose
weekly returns for the period January 1967 through December 1987 consti-
tute the T × N matrix R. They use principal components analysis to extract
the factors driving returns14 and examine the evidence for mean-variance
efficiency in one-, three-, and five-factor models. For an initial wealth, W,
and a degree of risk aversion equal to 15/W, McCulloch and Rossi find a
1% annual difference in certainty equivalence for all three-factor models.
A lower degree of risk aversion (2/W) leads to an increase in the difference
in certainty equivalents to around 8% annually for the three models. This
increase is a reflection of the fact that a lower risk aversion leads to greater
riskiness of the optimal portfolio. McCulloch and Rossi observe that the
five-factor model does not imply a larger degree of efficiency than the
one-factor model.
If a certain degree of inefficiency is observed in the market, can it be
exploited to obtain higher returns? In the next section, we explore stock
return predictability in the Bayesian setting.
14The principal components analysis procedure is briefly described in Chapter 14.

Market Efficiency and Return Predictability
175
RETURN PREDICTABILITY
Suppose an empirical investigation has shown that there exists a predictable
component in the returns of a market index. How would this affect the
investor’s optimal portfolio selection? What impact does return predictabil-
ity have on the ability to obtain estimates closer to the true values of the
unknown parameters as we acquire more information with time? In this
section, we discuss the asset allocation problem of a buy-and-hold investor
(i.e., an investor who constructs a portfolio at the beginning of a period and
does not rebalance untill the end of his investment horizon) in the context
of predictability.
The regression employed by most of the predictability studies has the
following form:
Rt = α + βxt−1 + ϵt,
(9.17)
where: Rt = stock’s excess return at time t.
xt−1 = value of a predictive variable at time t −1 (lagged predictor
value).
ϵt = regression’s disturbance.
The predictive variable (predictor) is either the lagged stock return or
variable(s) related to asset prices. For example, the dividend yield (the ratio
of the dividend at time t and the stock price at time t), the book-to-market
ratio (the ratio between the book value per share at time t and the stock price
at time t), and the term premium (the difference in returns on long-term and
short-term Treasury debt obligations) have been found to have predictive
power, at least in in-sample investigations.
It is also assumed that the predictive variable is stochastic and follows
an autoregressive process of order 1 (AR(1)):
xt = θ + γ xt −1 + ut.
(9.18)
Suppose that the predictor in (9.17) is the dividend yield (D/P). Let us
review a few stylized facts about the relationship between stock returns and
predictors (dividend yield, in particular), which will help us gain intuition
about the results discussed later in this section.
■The contemporaneous stock return, Rt is positively related to last
period’s dividend yield, D/Pt −1, that is, β > 0 in (9.17).
■A positive shock to D/Pt leads to a lower contemporaneous return, Rt.
Suppose the simple one-period stock-price valuation model is correct;

176
BAYESIAN METHODS IN FINANCE
that is, the stock price today is equal to the expected discounted cash
flows next period. The discount rate is equal to the internal rate of return;
that is, the expected stock return. The increase in D/Pt pushes up the
expected return at time t + 1, E[Rt + 1] (since β > 0). The future cash flow
is thus discounted at a higher rate, which impacts negatively today’s
price and leads to a decrease in the contemporaneous return, Rt.
■The disturbance, ϵt, in (9.17) is negatively correlated with D/Pt and
ut. The disturbance, ϵt, and D/Pt, are correlated because they are both
impacted by shocks to the stock price. Consider a positive shock to the
stock price at time t. The stock return at time t, Rt, will go up, while the
dividend yield at time t, D/Pt, will go down. Since the shock is by default
unexpected, it had not been incorporated into the expected return, E[Rt],
and the entire increase in Rt will be reflected in the disturbance, ϵt. There-
fore, ϵt and D/Pt are negatively correlated. Consider (9.18): a decrease
in D/Pt impacts negatively the disturbance ut. This implies a negative
correlation between the disturbances in (9.17) and (9.18).
Two competing hypotheses aim to explain predictability; one is in line
with efficiency, the other one is in contradiction to it. The first one contends
that predictability arises as a result of the discount effect explained before.
The second one claims that predictability is the result of irrational bubbles
in stock prices: low D/Pt signals that the price is irrationally high and will
move (in a predictable way) toward its fundamental value. In the rest of this
chapter, we are only concerned with the effects of predictability on portfolio
choice and we leave the discussion of its causes to researchers of financial
theory.
Let us assume the simplest case in which the excess returns on one
risky asset—a widely diversified portfolio such as the value-weighted NYSE
index—are examined for predictability. A single predictor variable, D/P, is
assumed. Then, (9.17) and (9.18) describe the relationship between Rt (the
asset return) and xt (D/P), as well as the evolution of D/P through time.
The framework combining the two equations is called vector autoregressive
(VAR) and explicitly models the dependence of ϵt and D/Pt −1. In vector
notation, we write the model as
Y = WB + E,
(9.19)
or, equivalently,


R1 x1
R2 x2
...
...
RT xT

=


1
x0
1
x1
...
...
1 xT−1


 α′
β′

+


ϵ1 u1
ϵ2 u2
...
...
ϵT uT

,

Market Efficiency and Return Predictability
177
where α =

α θ
′, and β =

β γ
′ and the tth row of Y is given by Y′
t =

Rt, xt

.
Assume that the disturbances, ϵt and ut, are jointly normally distributed
with zero mean vector and covariance matrix, :
 =
 σ 2
ϵ
σϵu
σϵu σ 2
u

,
(9.20)
where, as explained above, σ ϵu<0.
We explore predictability in terms of its effect on the asset selection. As
in the previous section, we solve the Bayesian portfolio problem. However,
instead of the one-period portfolio allocation, we are now interested in
multiperiod allocations and the interplay between predictability and the
investment horizon. In this discussion, we follow Barberis (2000).
Posterior and Predictive Inference
We consider the portfolio allocation problem for a buy-and-hold investor
who constructs his portfolio at time T and does not rebalance until the end
of his investment horizon at time T + T (hence, a static allocation problem).
The investor has return and D/P data available for T periods.
Let us derive the predictive distribution of excess returns T peri-
ods ahead, assuming diffuse prior information for the parameters of the
multivariate regression in (9.19),
B,  ∝||−(N + 1)/2,
where N = 2. The posterior distributions of B and  are normal and inverse
Wishart, respectively:
vec(B) |  ∼N

vec(B),  ⊗

W ′W
−1
(9.21)
 ∼IW

, T −1

,
(9.22)
where:15 B = (W ′W)−1(W ′Y) = least-squares estimate of B.
 = (Y −WB)′(Y −WB)
In (9.21), ‘‘vec’’ is an operator which stacks the columns of a matrix into a
column vector, so that vec(B) is a 4 × 1 vector and ⊗is the notation for the
Kronecker product.16
15See the appendix to this chapter for more details on the notation.
16The Kronecker product between two matrices, A and B, of any dimension, is
A ⊗B =


a11B a12B ··· a1KB
a21B a22B ··· a2KB
···
aL1B aL2B ··· aLKB

.

178
BAYESIAN METHODS IN FINANCE
In previous chapters, our goal has been to find the distribution for
the N × 1 vector of next-period excess returns (at time T + 1). Here, we
generalize this result to the predictive distribution of the N × 1 vector of
excess returns at time T + T. It is important to realize that, in the static,
multiperiod prediction case, we are interested in predicting the cumulative
excess return at the end of the investment period. The cumulative excess
return is the quantity that a rational buy-and-hold investor would aim to
maximize. We take the cumulative excess return, RT,T, to be simply the sum
of the single-period excess returns:
RT,T = RT + RT+1 + · · · + RT+T.
Therefore, we need to derive the predictive distribution of cumulative excess
returns at time T + T. Moreover, since the VAR framework links the
dynamics of the excess returns and the predictive variable, we predict the
future D/P along with future excess returns.
The predictive distribution for YT,T is given by (see (3.19) in Chapter 3)
p

YT,T | Y

=

p (YT,T | B, , Y) p (B,  | Y) dB d,
(9.23)
where we implicitly assume that the distribution (and distributional param-
eters) of Y remains unchanged throughout the T periods ahead. In the
following chapters on volatility models, including regime-switching models,
the assumption of stationarity of the returns distribution is relaxed.
We know that, for T = 1, the distribution of YT+1 is normal. For an
arbitrary value of T, we still have a normal density, since we can simply roll
forward (9.19) an arbitrary number of times. Denote the normal distribution
of YT+1 by N

µT+1, T+1

, the normal distribution of YT+2 by N

µT+2, T+2

,
and so on. Then, using the properties of the normal distribution, we obtain
that YT,T = YT+1 + · · · + YT,T is normally distributed:
p (YT,T | B, , Y) = N

µT + 1 + . . . + µT + T, T + 1 + . . . + T + T

.
To find the means and covariances of each YT + t, t = 1, . . . , T, above,
we use the fact that (9.17) and (9.18) establish a recursive relationship
between returns and D/P. To see this, rewrite (9.19) in the following way.
At time T + 1,
YT+1 = α + β0YT + eT+1,
(9.24)
Note that computing the Kronecker product does not require compatibility of
the matrix dimensions. The appendix to this chapter explains why the Kronecker
product appears in (9.21).

Market Efficiency and Return Predictability
179
where
β0 =
 0 β
0 γ

,
eT+1 =
 ϵT + 1
uT+1

.
It is easy to verify that (9.24) is equivalent to (9.19). Iterating forward
one-period at a time and at each step t substituting the expression for Yt−1,
we obtain
YT + 2 =

α + β0α + β2
0YT

+

β0eT + 1 + eT + 2

YT + 3 =

α + β0α + β2
0α + β3
0YT

+

β2
0eT + 1 + β0eT + 2 + eT + 3

. . .
YT + T =

α + β0α + . . . + β
T−1
0
α + β
T
0 YT

+ β
T−1
0

eT + 1 + · · · + eT + T

,
where βt
0 denotes the tth power of the matrix β0. The first (bracketed) term
in each right-hand-side expression is the mean of the corresponding normal
distribution of YT + t, t = 1, . . . , T. The second term is used to derive the
covariance in the following way:
cov

YT + 2

= β0 β′
0 + 
=

I + β0



I + β0
′,
cov

YT + 3

= β2
0  β2
0
′ + β0  β′
0 + 
=

I + β0 + β2
0



I + β0 + β2
0
′.
and so on, where we use the fact that eT+t has covariance matrix  for each
t = 1, . . . , T.
Finally, we can write out the parameters of the normal distribution of
YT,T, p (YT,T | B, , Y), conditional on α, β, and . The mean is
µT,T = Tα
+
T −1

β0 +
T −2

β2
0 + · · · + β
T−1
0

α
+

β0 + β2
0 + · · · + β
T
0

YT,
(9.25)
and the covariance is
VT,T = 
+

I + β0



I + β0
′
+

I + β0 + β2
0



I + β0 + β2
0
′
(9.26)

180
BAYESIAN METHODS IN FINANCE
+ . . .
+

I + β0 + β2
0 + . . . + β
T−1
0



I + β0 + β2
0 + . . . + β
T−1
0
′.
To sample from the predictive distribution of YT,T in (9.23), we employ
the following sampling scheme:
■Draw  from its inverted Wishart posterior distribution in (9.22).
■Given the draw of , draw B from its normal posterior distribution in
(9.21).
■Given the draws of  and B, compute µT,T and VT,T and sample from
a normal distribution with those parameters to obtain a draw from the
predictive distribution of YT,T =

RT,T, xT,T

.
We perform these steps a large number of times to obtain the simulated
predictive distribution of the cumulative excess return at the end of the
investment horizon, T + T. Now we are ready to compute the optimal
portfolio allocation by maximizing the investor’s expected utility over the
predictive density of cumulative excess return. We do that numerically.
Solving the Portfolio Selection Problem
In Chapters 6 and 7, we assumed that the investor had a quadratic utility,
and computed the optimal portfolio weights using (6.14) in Chapter 6.
Earlier in this chapter, we used the negative exponential utility function.
Here, we consider a power utility, given by17
U

WT + T

=
W1 −A
T + T
1 −A,
(9.27)
where A is the risk-aversion parameter and WT + T is the end-of-horizon
(terminal) wealth. Assuming continuously compounded returns, the terminal
wealth is written as
WT + T = WT

ω exp
TRf + RT,T

+ (1 −ω) exp
TRf

,
17Power utility is also known as iso-elastic utility. It is often taken to be the neutral
(benchmark) utility function in investigations of investor preferences because of its
distinctive property of constant relative risk aversion (CRRA). Intuitively, CRRA
means that the investor’s preferences for risk do not change with his wealth level nor
with the time horizon—the same proportion of wealth is invested in risky assets.
In contrast, the negative exponential function we employed in the previous section
exhibits constant absolute risk aversion, which means that the investor becomes
more risk averse as his wealth increases—he invests the same absolute amount in
risky assets at any wealth level.

Market Efficiency and Return Predictability
181
where: WT = wealth at the time of portfolio construction.
Rf = continuously compounded, risk-free rate.
ω = fraction of the portfolio invested in the risky asset.
Without loss of generality, we could take WT=1. Notice that we add
the cumulative risk-free return, TRf, in the terminal wealth equation since
RT,T is the cumulative excess return.
Taking the expectation of (9.27) with respect to the predictive distribu-
tion of RT,T, we obtain
E

U

WT + T

=

U

WT + T

p

YT,T | B, 

dRT,T.
(9.28)
Since no analytical expression is available for the expectation in (9.28),
we compute the integral numerically (approximate it with a sum) averaging
the utility over the draws of RT,T. For a total number of M draws, that sum
is expressed as
E

U

WT + T

= 1
M
M

m = 1

ω exp
TRf + Rm
T,T

+ (1 −ω) exp
TRf
1−A
1 −A
,
(9.29)
where the superscript of RT,T denotes the mth draw from the predictive
distribution.
Assuming no short selling and no buying on margin, portfolio weights,
ω, can take values between 0 and 0.99.18 We maximize (9.29) with a
constrained optimizer (available in most commercial software packages) or
with the following numerical procedure. We evaluate the right-hand side
in (9.29) over a grid of values of ω and identify the optimal allocation
as the value of ω that produces the greatest value of the expected utility,
E

U

WT+T

. For example, the expected utility could be evaluated on the
grid [0, 0.01, 0.02, . . . ,0.97, 0.98, 0.99].
In order to explore the implication of predictability on optimal alloca-
tions at different horizons, the numerical optimization above is performed
for different values of T.
18The upper bound of the weights range is restricted to 0.99 instead of 1 since,
when ω = 1, expected utility is equal to −∞. The unboundedness of the util-
ity function from below is a result of the heavy-tailedness of the predictive
distribution (the unconditional predictive distribution of RT+T is a multivari-
ate Student’s t-distribution). See Barberis (2000) and Kandel and Stambaugh
(1996).

182
BAYESIAN METHODS IN FINANCE
0
5
10
Horizon
80
60
40
20
Allocation to Stocks (%)
EXHIBIT 9.2
Optimal stock allocation when
returns are predictable
Source: Adapted from Figure 2 in Barberis (2000).
ILLUSTRATION: PREDICTABILITY AND THE INVESTMENT
HORIZON
Exhibit 9.2 presents the optimal allocation, ω, plotted against the investment
horizon from the investigation of Barberis (2000). He uses monthly data
on the NYSE stock index and its dividend yield over the period June 1952
through December 1995. The value of the risk aversion parameter, A, used
to solve for the optimal portfolio is 10. The lines in the exhibit correspond
to two scenarios—predictability with uncertainty taken into account (the
solid line) and predictability with no uncertainty taken into account (the
dashed line). The former scenario is the one discussed earlier in the chapter.
The latter scenario treats the mean and covariance of returns as given; these
parameters are fixed at their posterior mean values and for each length of
the investment horizon, T, the distribution of cumulative returns, RT,T, is
simulated by drawing a sample from N
Tµ, T

, where the ‘‘hats’’ on µ
and  denote posterior moments.
In the absence of uncertainty about the mean and covariance of returns,
predictability causes an increasing-with-horizon allocation to the NYSE
index—investment in stocks becomes more attractive with time. In contrast,
when uncertainty in the parameters is included in the analysis, the effect of
predictability is not strong enough to induce ever-increasing allocation to


## Unit Root and Structural Breaks

Market Efficiency and Return Predictability
183
stocks. As time passes, uncertainty begins to dominate and stock allocation
declines.
SUMMARY
In this chapter, we consider two of the most debated topics in empirical
finance—market efficiency and return predictability. We discuss how to
cast both into the Bayesian framework. Accounting for estimation risk
has tangible implications for a buy-and-hold investor—at short investment
horizons, the effect of predictability dominates the effect of estimation
uncertainty; at longer horizons, however, uncertainty ‘‘wins over, ’’ implying
declining portfolio allocations to stocks.
APPENDIX: VECTOR AUTOREGRESSIVE SETUP
The VAR model considered in the chapter is given by
Y = WB + E,
(9.30)
equivalent to


R1 x1
R2 x2
. . . . . .
RT xT

=


1
x0
1
x1
. . . . . .
1 xT−1


α θ
β γ

+


ϵ1
u1
ϵ2
u2
. . . . . .
ϵT uT.


(9.31)
In the chapter we assumed that each row of E is normally distributed
with zero mean and covariance matrix . For the purposes of distributional
analysis, it is often helpful to vectorize the matrices in (9.31) and represent
it as
y = Zb + e,
(9.32)
where: y = vec(Y)
Z = I2 ⊗W
b = vec(B)
e = vec(E)
The vec operator serves to stack the columns of a matrix into a column
vector, while ⊗is the Kronecker product. The expression in (9.32) is

184
BAYESIAN METHODS IN FINANCE
equivalent to


R1
R2
...
RT
x1
x2
...
xT


=


1
x0
0
0
1
x1
0
0
. . . . . . . . . . . . . .
1 xT−1 0
0
0
0
1
x0
0
0
1
x1
. . . . . . . . . . . . . .
0
0
1 xT−1




α
β
θ
γ

+


ϵ1
ϵ2
...
ϵT
u1
u2
...
uT


.
(9.33)
The covariance matrix of e is now written as
cov(e) =  ⊗IT,
(9.34)
where IT is an identity matrix of dimension T × T. The expression in (9.34)
can be expanded as
cov(e) =


σ 2
ϵ
0
· · ·
0
σϵ u
0
· · ·
0
0
σ 2
ϵ
· · ·
0
0
σϵ u · · ·
0
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
0
0
· · · σ 2
ϵ
0
0
· · · σϵ u
σϵ u
0
· · ·
0
σ 2
u
0
· · ·
0
0
σϵ u · · ·
0
0
σ 2
u
· · ·
0
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
0
0
· · · σϵ u
0
0
· · · σ 2
u


.
(9.35)

CHAPTER10
Volatility Models
An Overview
V
olatility describes the variability of a financial time series, that is, the
magnitude and speed of the time series’ fluctuations. In some sense, it
most clearly conveys the uncertainty in which financial decision making is
accomplished. Volatility is often expressed as the standard deviation of asset
returns and, more generally, when returns are assumed to be nonnormal, as
the scale of the return distribution.1
In financial modeling, volatility is a forward-looking concept. It is
the variance of the yet unrealized asset return conditional on all relevant,
available information. Denote by ℑt−1 the set of information available up to
time t −1. This information set includes, for example, past asset returns and
information about past trading volume. The volatility at time t is given by
σ 2
t|t−1 = var

rt|ℑt−1

= E

rt −µt|t−1
2 | ℑt−1

,
where rt and µt|t−1 are the asset’s return and conditional expected return at
time t, respectively
As the previous equation suggests, the volatility of returns is not constant
through time. In such cases, we say that returns are heteroskedastic. An
important phenomenon, called volatility clustering, is characteristic of the
dynamics of asset returns. Mandelbrot (1963) was one of the first to note
that ‘‘large changes [in asset prices] tend to be followed by large changes—of
either sign—and small changes tend to be followed by small changes.’’ In
other words, volatility clustering describes the tendency of asset returns to
alternate between periods of high volatility and low volatility. The periods
1Measures of risk other than the standard deviation are increasingly popular among
both finance practitioners and academics. We discuss some of them in Chapter 13.
185

186
BAYESIAN METHODS IN FINANCE
of high volatility see large magnitudes of asset returns (both positive and
negative), while in periods of low volatility the market is ‘‘calm’’ and returns
do not fluctuate much. Clearly, this stylized fact about financial time series
contradicts the efficient market hypothesis, which we discussed in Chapter 9.
In an efficient market, investors would react immediately to the arrival of
new information so that its effect is quickly dissipated; changes in asset
returns are independent through time.
Two other empirically observed features of returns are that returns
exhibit skewness and heavier tails (higher kurtosis) than suggested by the
normal distribution and that volatility displays an asymmetric behavior to
positive and negative return shocks—it tends to be higher when the market
falls than when it rises. Volatility models attempt to explain these stylized
facts about asset returns.
Since the volatility (and the expected return) today depends on the volatil-
ity (and the expected return) yesterday, it is clear that today’s asset return is
not independent from yesterday’s asset return. Therefore, we can write an
expression describing the evolution of returns through time—the stochastic
process—incorporating the time-varying conditional volatility. In general,
although asset returns can be thought of as evolving in a continuous fashion,
the return-generating process is often modeled in the discrete time domain.
We can represent the one-period, discretely sampled (e.g., daily) return,
rt, as the sum of a conditional expected return, µt|t−1, and an innovation
(a random component), ut, with zero mean and nonzero conditional vari-
ance, σ 2
t|t−1:
rt = µt|t−1 + ut.
(10.1)
A further decomposition gives
rt = µt|t−1 + σt|t−1ϵt,
(10.2)
where σ t|t−1 is positive. The term ϵt is the building block of all time-series
models. It denotes a white noise process—a sequence of independent and
identically distributed (i.i.d.) random variables with zero mean and variance
equal to one.
The expression in (10.2) is the underlying basis common to the two
major groups of volatility models—the autoregressive conditionally het-
eroskedastic (ARCH) -type models and the stochastic volatility (SV) models.
The conceptual difference between the two lies in the degree of determinacy
of σ t at time t −1. In the simplest ARCH-type model, volatility is described
by a deterministic function of past squared returns; volatility at time t can be
uniquely determined at time t −1. In an SV model, the conditional volatility
is subject to random shocks; the unpredictable component makes it latent and
unobservable. The distinction can be further visualized by considering the set

Volatility Models
187
of available information. The former setting assumes that, when estimating
σ t, all relevant information, embodied in ℑt−1, is available and observable
at time t −1. In contrast, in the latter setting, only a part of ℑt−1 is directly
observable; the ‘‘true’’ volatility thus becomes unobservable or latent.2
In this chapter, we provide an overview of ARCH-type and SV models.
We discuss their Bayesian estimation in the next two chapters. In Chapter
14, we put volatility estimation into perspective and integrate it into the
multifactor-model framework, thus presenting its main applications to risk
management and to portfolio selection.
GARCH MODELS OF VOLATILITY
The analytical tractability of the GARCH-type models has made them
the predominant choice in volatility modeling. Furthermore, the various
extensions to the original ARCH model of Engle (1982) and the GARCH
model of Bollerslev (1986) provide a large degree of flexibility in capturing
empirically observed features of returns.
The volatility updating expression is given by
σ 2
t|t−1 = ω + αu2
t−1 + βσ 2
t−1|t−2,
(10.3)
where ut is a residual defined as ut = rt −µt|t−1 = σ t|t−1ϵt. The parameters
of the GARCH(1,1) process are restricted to be nonnegative, ω > 0,
α ≥0, and β ≥0, in order to ensure that σ 2
t|t−1 is positive for all values of
the white noise process, ϵt. Notice how the information available at time
t −1 impacts the conditional variance at time t, σ 2
t|t−1. The new information
at time t −1 is embodied in the ARCH term, the squared residual, u2
t−1. The
carrier of the old information at time t −1 is the GARCH term, σ 2
t−1|t−2.
Rewriting (10.3) as
σ 2
t|t−1 = (1 −α −β)
ω
1 −α −β + αu2
t−1 + βσ 2
t−1|t−2,
(10.4)
one can see that the GARCH(1,1) model specifies the conditional variance
of returns as a weighted average of three components:
■The long-run (unconditional) variance, ω/(1 −α −β).
■Last period’s predicted variance, σ 2
t−1|t−2.
■The new information at time t −1, u2
t−1.
2See Andersen, Bollerslev, Christoffersen, and Diebold (2005) for this interpretation.

188
BAYESIAN METHODS IN FINANCE
The specification of σ 2
t|t−1 in (10.3), as a function of the lagged squared
innovations, u2
t−1, only corresponds to Engle’s (1982) original ARCH(1)
model.
The expression in (10.3) can be easily extended by including addi-
tional lagged squared innovations and lagged conditional variances to
arrive at higher-order GARCH(p,q) models. It has been found, however,
that the GARCH(1,1) specification generally describes return volatility
sufficiently well.
Certainly, the model in (10.3) is incomplete unless we specify a distri-
butional assumption for the asset return at time t. Since we are modeling
temporally dependent asset returns, our focus naturally lies on the con-
ditional return distribution. The original treatments of the GARCH(1,1)
model by Bollerslev (1986) and Taylor (1986) assumed that returns are
conditionally normally distributed:
rt | ℑt−1 ∼N

µt|t−1, σ 2
t|t−1

.
(10.5)
Before we discuss the properties of the GARCH model and different
distributional assumptions, let us review how the GARCH(1,1) model
defined by (10.2), (10.3), and (10.5) explains some of the known stylized
facts about asset returns.
Stylized Facts about Returns
Volatility Clustering
It is possible, by recursive substitution, to express
(10.3) only in terms of the lagged squared residuals, u2
t−1, u2
t−2, . . . :3
σ 2
t|t−1 =
ω
1 −β + αu2
t−1 + αβu2
t−2 + αβ2u2
t−3 + . . .
=
ω
1 −β + α
∞

j=1
βj−1u2
t−j.
It is easy to see, then, that recent large fluctuations of asset returns
around their conditional means, that is, recent, large squared residuals, u2
t−j,
imply a high value for the conditional variance, σ 2
t|t−1, in period t, since α
≥0 and β ≥0. The result is a cluster of high volatility. Conversely, if the
recent history of returns is one of small fluctuations around the conditional
mean, σ 2
t|t−1 is expected to be small, and a cluster of low volatility occurs.
Nonnormality of Asset Returns
GARCH models can partially explain the
empirically observed heavy tails and high-peakedness of asset returns, even
3Technically, we obtain an ARCH model with an infinite number of lags, ARCH(∞).

Volatility Models
189
with the assumption that returns are conditionally normally distributed.
Consider the expression in (10.2). The unconditional (marginal) distribution
of rt can be represented as a combination of normal distributions; a different
normal distribution corresponds to the different realizations of σ 2
t|t−1 that
could occur. We say that rt is distributed as a mixture of normals. The
tails of the mixture are heavier and the peakedness—higher than these of a
normal distribution.
The GARCH effects, however, are insufficient to account fully for the
nonnormality of returns. Alternative distributional assumptions could thus
be adopted.
Asymmetric Volatility
The ‘‘plain vanilla’’ GARCH(1,1) model above does
not capture the volatility asymmetry observed in practice. Notice that both
positive return shocks (when the return is above its conditional expectation
and ut−1 > 0) and negative return shocks (when the return is below its
conditional expectation and ut−1 < 0) have an identical (symmetric) impact
on the conditional variance, σ 2
t|t−1, since the residual, ut−1, in (10.3) appears
in a squared form.4 Many extensions accounting for the asymmetric effect
exist in the volatility literature. One of them, for example, is the model of
Glosten, Jagannathan, and Runkle (1993) in which the conditional variance
reacts in a different way to positive and negative shocks,
σ 2
t|t−1 = ω + αu2
t−1 + γ u2
t−1I(ut−1<0) + βσ 2
t−1|t−2,
where I(ut−1<0) is an indicator taking a value of 1 if ut−1 < 0 and 0 if ut−1 ≥0.
Another one is Nelson (1991)’s popular exponential GARCH (EGARCH)
model.5
Modeling the Conditional Mean
The mean of returns in (10.2) is often assumed to be a constant when
the goal is modeling the return’s conditional variance. However, there is
no reason why it cannot be specified conditionally as well. For example,
a specification that has been
found to describe the behavior of returns
4Black (1976) put forward the so-called leverage effect as a possible explanation of
the asymmetric response of volatility to stock price movements. Everything else held
constant, declining stock prices lead to decreased market capitalizations and higher
leverage (debt/equity) ratios. This, in turn, implies a higher perceived risk of the
respective stocks and greater volatility. It has been found, however, that the leverage
effect is insufficient to explain the extent of asymmetries in the market.
5See Fornari and Mele (1996) for a comparison of several of the more popular
asymmetric volatility models.

190
BAYESIAN METHODS IN FINANCE
well is the ARMA(1,1)–GARCH(1,1) process, in which an autoregressive
moving average (ARMA) model of returns is combined with the GARCH
specification:6
rt = η0 + η1rt−1 + η2ut−1 + σt|t−1ϵt
(10.6)
σ 2
t|t−1 = ω + αu2
t−1 + βσ 2
t−1|t−2.
The autoregressive parameter, η1, takes values between −1 and 1 and
measures the impact of the last-period return observation, while the moving
average parameter, η2, represents the influence of last period’s return shock.
The parameters of the ARMA (1,1) process are estimated together with the
GARCH(1,1) parameters.
A different conditional mean specification is provided by the ARCH-in-
mean model, relating the expected asset return to the asset risk, represented
by the conditional standard deviation of returns:7
µt|t−1 = λ0 + λ1σt|t−1.
(10.7)
The parameter λ1 can be interpreted as the compensation investors
require (in the form of higher expected return) for an increase in the risk of
the asset, that is, as the price of risk. The parameter λ0 could also be given
an economic interpretation—as the risk-free rate of return (the required
compensation for holding an asset with no risk (σ t|t−1 = 0)).
Although providing increased flexibility, modeling the conditional mean
of returns in an ARCH-type model context is not critical. Nelson and Foster
(1994) show that the measurement error due to a misspecification in
the conditional mean could be trivial in comparison to the measurement
error induced by failure to capture nonnormality of the conditional return
distribution or the effects of asymmetry in the volatility.
Properties and Estimation of the GARCH(1,1) Process
We review three of the most important properties of the GARCH(1,1)
process.
1. The most important property of the GARCH(1,1) process defined in
the previous section is stationarity (more specifically, covariance (or
weak) stationarity). Stationarity of a stochastic process requires that the
process has finite moments (means, variances, and covariances) that do
not change with time. The covariance between any two components
6See Rachev, Stoyanov, Biglova, and Fabozzi (2004).
7See Engle, Lilien, and Robins (1987).

Volatility Models
191
of the process, rt−h and rt, depends only on the distance between
them, h. An obvious implication of this requirement is that, if non-
stationarity is suspect, we cannot assume that the same distribution
governs the return process throughout the time period under consid-
eration.8 Regime-switching models are an extension that deals with
nonstationarity, and we discuss them in the next chapter.
In the setting of normality, the GARCH(1,1) process is stationary if the
sum of its coefficients, α + β, is less than 1. The sum, α + β, is known
as the GARCH process persistence parameter since it determines the
speed of the mean-reversion of volatility (another empirically observed
feature) to its long-term average. A higher value for α + β implies
that the effect of the shocks to volatility, u2
t , dies out slowly. In many
financial applications, the persistence parameter is close to 1.
When a Student’s t-distribution (with ν degrees of freedom) is assumed
for returns, the relevant (covariance) stationarity inequality is given by
α
ν
ν −2 + β < 1.
(10.8)
2. The long-run (unconditional) variance of return is given by
σ 2 =
ω
1 −α −β ,
(10.9)
for 0 ≤α + β < 1. The term 1 −α −β is the weight given to the long-run
variance component of the conditional variance σ t|t−1 (see (10.4)).
3. The autocorrelation of returns is zero, since the autocovariance is
cov

rt−h, rt

= 0.
The autocorrelation of the squared residuals,
corr

u2
t−h, u2
t

=

α + β
h
α

1 −αβ −β2

α + β

1 −2αβ −β2,
is positive but declines as the distance, h, between the time periods
increases.
8Strictly speaking, covariance stationarity guarantees that the distribution remains
unchanged throughout the time period only in the case of normal distribution (since
the normal distribution is completely determined by its first two moments). In all
other cases, a stronger condition, called strict stationarity is needed.

192
BAYESIAN METHODS IN FINANCE
The parameters of the GARCH model are estimated in the classi-
cal framework with the help of maximum likelihood methods. Denote
the parameter vector of the GARCH process by θ =

ω, α, β

and the
information set at the start of the process by ℑ0. The asset return, rt,
depends on σ 2
t|t−1 and, through it, on the volatilities in each of the preceding
time periods (due to the presence of the GARCH component in (10.3)). The
unconditional density function of rt is not available in analytical form, since
it is a mixture of densities depending on the dynamics of σ 2
t|t−1. Therefore,
the likelihood function for θ is written in terms of the conditional densities
of rt for each t, t = 1, 2, . . . , T.
Given ℑ0, the likelihood function L

θ | r1, r2, . . . , rT, ℑ0

can be
represented as the product of conditional densities:9
L

θ | r, ℑ0

= f

r1 | θ, ℑ0

f

r2 | θ, ℑ1

. . . f

rT | θ, ℑT−1

,
(10.10)
where r =

r1, r2, . . . , rT

. Using the distributional assumption in (10.5),
the log-likelihood function becomes
log L

θ | r, ℑ0

=
T

t=1
log f

rt | θ, ℑt−1

(10.11)
= const −1
2
 T

t=1
log(σ 2
t|t−1) +
T

t=1

rt −µt|t−1
2
σ 2
t|t−1

,
where σ 2
t|t−1 is a function of the parameter vector, θ (according to (10.3)).
Since the likelihood function is nonlinear in the parameters, maximization
with respect to θ is accomplished using numerical optimization techniques.
It is necessary to specify starting values for the conditional variance and
the squared residuals. Assuming that the GARCH model is stationary, these
starting values are often taken to be the sample estimates from an earlier
(presample) period.
In (10.11) above, we used the default assumption for the return
distribution. Quite frequently, however, this assumption is contradicted
empirically. Even though, as discussed earlier, the specification of the
GARCH model (with the assumption of normality) itself implies an
unconditional distribution (a mixture of normals10) with tails heavier than
these of the normal distribution, it turns out that we might need different
9To see that, notice that when ℑt is defined as an information set consisting of lagged
asset returns, ℑ1 = ℑ0
 r1, ℑ2 = ℑ1
 r2, etc.
10For more details on mixtures of normals, see Chapter 13.

Volatility Models
193
assumptions for the conditional returns distribution, f(rt | θ, ℑt−1). If
the conditional distribution of the innovations of the true data-generating
process is as given in (10.5), then the empirical distribution of the standard-
ized filtered (fitted) residuals,
	
ϵt|t−1 = rt −µt|t−1

	
σ 2
t|t−1
,
should be approximately standard normal. (The term 	
σ 2
t|t−1 in the expres-
sion above denotes the estimated conditional variance (computed at the
maximum-likelihood estimate of θ).) Instead, when modeling weekly, daily
or higher-frequency financial data, the residuals’ empirical distribution is
found to deviate from normality and exhibit heavy tails and skewness. Alter-
native assumptions for the conditional distribution have been proposed to
adequately model the return process, among them the (a)symmetric Stu-
dent’s t-distribution, the generalized error distribution (GED), the stable
Pareto distribution, and discrete mixtures of normal distributions. (See
Chapter 13 for their definitions.)
Rachev, Stoyanov, Biglova, and Fabozzi (2004) compare the normal-
ity and the stable Paretian assumptions when estimating an ARMA(1,1)–
GARCH(1,1) model for 382 stocks from the S&P 500 index. They examine
the distribution of the standardized filtered residuals and find that normal-
ity is rejected at the 99% confidence level for over 80% of the stocks,
while the stable assumption is rejected for only 6% of the stocks. Mit-
tnik and Paolella (2000) show an almost uniform improvement in the
estimation of an AR(1)–GARCH(1,1) model when using the Student’s
t-distribution instead of a normal distribution, in a study of seven East
Asian currency returns. They also advocate a more general parametrization
of the Student’s t-distribution, which allows for asymmetries in the returns
process.11
In the presence of nonnormality, a modification of the parametrization
of the volatility equation in (10.3) has been found to provide a better fit
than (10.3). Instead of an exponent of two, an exponent of one is used
in (10.3),12
σt|t−1 = ω + α|ut−1| + βσt|t−1.
11For a comprehensive survey of the distributional assumptions for GARCH pro-
cesses, see Palm (1996).
12See Nelson and Foster (1994) and Mittnik and Paolella (2000).

194
BAYESIAN METHODS IN FINANCE
STOCHASTIC VOLATILITY MODELS
Stochastic volatility (SV) models assert that volatility evolves according
to a stochastic process. As mentioned earlier, the main difference between
ARCH-type models and SV models is that in the latter volatility at time t is a
latent, unobservable variable, only partially determined by the information
up to time t, contained in ℑt−1. The motivation for this concept comes
from research linking asset prices to information arrivals, for example
macroeconomic and earnings releases, trading volume, and number of
trades.13 Some of these arrivals are unpredictable and give rise to shocks in
the volatility dynamics.
Stochastic volatility is also directly linked to the ‘‘instantaneous volatil-
ity’’ concept from the area of continuous-time asset pricing. SV models
are discrete-time approximations of the continuous-time processes used in
finance theory.14
In empirical work, the SV models are usually formulated in discrete
time. In line with this tradition, we now turn to a description of the
discrete-time SV model of Taylor (1982, 1986).
Similar to (10.2), the asset return (in excess of its mean which we assume
constant for simplicity) is decomposed as
rt −µ = σtϵt.
(10.12)
Notice that we do not write σ t|t−1 here, since volatility is not fully
determined given r1, r2, . . . , rt−1. We assume that the random variables, ϵt,
are white noise (i.i.d. with zero mean and unit variance).
Taylor (1986) specifies the logarithm of volatility as an autoregressive
process of order 1 (AR(1) process):
log(σ 2
t ) = ρ0 + ρ1 log(σ 2
t−1) + ηt,
(10.13)
where ρ1 is a parameter controlling the persistence of volatility (how slowly
its autocorrelations decay); and −1 < ρ1 < 1. It plays the role of the sum
13See Clark (1973) and Tauchen and Pitts (1983). This is related to the idea of
subordinated stochastic processes. One can consider two different time scales—the
physical, calendar time and the intrinsic time—of the price dynamics. The intrinsic
time is best thought of as the cumulative trading volume up to a point on the
calendar-time scale. The asset price process is then ‘‘directed’’ by the process
governing the trading volume (or, more generally, the information flow). For a
detailed discussion of subordination, see Rachev and Mittnik (2000).
14See, for example, Hull and White (1987). They replace the assumption of constant
volatility in the Black-Scholes option-pricing formula with a stochastic process for
the (instantaneous) volatility.

Volatility Models
195
α + β in the context of GARCH models with normal distributional assump-
tion. The innovations, ηt, are the source of the volatility’s unpredictability
and are assumed to be normally distributed with zero mean and variance
τ 2. The disturbances ϵt and ηt may or may not be independent for all t,
t = 1, . . . , T.
Substituting (10.13) into (10.12), we can see that the dynamics of
the asset return is now governed by two sources of variability—ϵt and
ηt—while only data on a single asset return are available. The unobservable
parameters are as many as the sample size, which, we see next, complicates
model estimation substantially.
Stylized Facts about Returns
SV models explain the same stylized facts about asset returns as GARCH
models. Let us review how:
■Volatility clustering. The empirical estimates of ρ1 are generally close
to 1. Thus, a high value for the log-volatility at time t −1 implies a
high value in the following period as well, leading to a cluster of high
volatility.
■Nonnormality of returns. The mixture-of-distributions argument put
forward in the GARCH case to partially explain the heavy tails (high
kurtosis) of asset returns is valid here as well. Asset return, rt, is dis-
tributed as a mixture with mixing parameter τ 2 (the variance of ηt).
The mixture exhibits heavier tails compared to the normal distribu-
tion.
■Asymmetric volatility. The basic SV model, assuming independence of
ϵt and ηt for all t, does not allow volatility to react in an asymmetric
fashion to return shocks. One way to reflect the empirically observed
asymmetry is to permit negative correlation between the innovation
processes: corr(ϵt, ηt) < 0.
Estimation of the Simple SV Model
The estimation of the parameter vector, θ =

ρ0, ρ1, τ 2
, of the simple
SV model is much less straightforward than estimation of the correspond-
ing parameter vector of the simple GARCH(1,1) model.15 The likelihood
function for θ can be written as the product of conditional densities. The
complicating difference relative to the GARCH case is that the unobserved
15We assume that the mean of returns, µ, is estimated outside of the model.

196
BAYESIAN METHODS IN FINANCE
volatility needs to be integrated out, giving rise to an analytically intractable
expression. We write the likelihood function as
L

θ | r1, r2, . . . , rT

=

f

r1, . . . , rT | σ1, . . . , σT, θ

f

σ 2
1 , . . . , σ 2
T | θ

dσ 2
1 . . . dσ 2
T
=

T

t=1
f

rt | σ 2
t , θ, rt−1

f

σ 2
t | θ, σ 2
−t

dσ 2
1 . . . dσ 2
T,
(10.14)
where rt−1 =

r1,
. . . ,
rt−1

and σ 2
−t =

σ 2
1 , . . . , σ 2
t−1, σ 2
t+1, . . . , σ 2
T

. The
volatility density is denoted by f

σ 2
t | θ, σ 2
t−1

. The T-dimensional inte-
gral in the equation can only be evaluated with the help of numerical
methods.
Shephard (2005) and Ghysels, Harvey, and Renault (1996) offer surveys
of SV models and estimation techniques. Among those estimation techniques
are various methods of moments (MM)16 and quasi-maximum likelihood
(QML).17 MM and QML parameter estimates are generally known to be
inefficient, thus implying increased parameter uncertainty and less reliable
volatility forecasts.
Simulation-based methods are thought to be the most promising path
for estimation of the parameter vector θ because of both the accuracy of
the estimators and the flexibility in dealing with complicated models. We
briefly review now one such method, the Efficient Method of Moments of
Gallant and Tauchen (1996) and explain the Bayesian approach later in
Chapter 12.
Efficient Method of Moments
Consider the return-generating process in
(10.12). As discussed, the likelihood function for the parameter vector,
θ, (the vector of structural parameters, in the terminology of financial
econometrics) is not available in analytical form. Suppose that there is
a (competing) model of returns whose parameters are easy to estimate.
Denote its parameter vector by ζ. The idea of the Efficient Method of
Moments (EMM)18 is to use that model, called the auxiliary model, as a
‘‘special purpose vehicle’’ in estimating θ. Since our purpose is to model
16See Taylor (1986) and Andersen (1994), among others
17See Harvey, Ruiz, and Shephard (1994) for an application to multivariate SV
model estimation.
18We emphasize the practical aspect of EMM estimation here. For its methodological
aspects and the statistical properties of the EMM estimators, see Gallant and Tauchen
(1996). For an application of EMM to SV models, see Chernov, Ghysels, Gallant,
and Tauchen (2003), among others.

Volatility Models
197
volatility, the natural choice of an auxiliary model is a GARCH model.
Then ζ =

ω, α, β

using the notation established earlier in the chapter.
Denote by:
g

rt | σt, ζ

= conditional density of the asset return under the GARCH
(auxiliary) model.
f

rt | σt, θ

= conditional density of the asset return under the SV
model.
Let’s walk through the steps of the EMM estimation procedure.19
1. Estimate, via maximum-likelihood (possibly numerically), the parame-
ter vector, ζ, of the GARCH auxiliary model. Denote the MLE by ζ.
That is, ζ satisfies the first-order condition (the first derivative (score)
of the log-likelihood function evaluated at ρ is zero),
ST
ζ, θ

≡1
T
T

t=1
∂
∂ζ log g

rt | σt,ζ

= 0,
(10.15)
for a sample of size T. The score, ST, is a vector of the same dimension
as ζ.
We suppose that, in some sense, ζ and θ, are close—θ is the ‘‘true’’ set
of parameters that, we believe, generated the data

rt, σt

, while ζ is
the set of parameters of another credible data-generating model. That
is, without claiming a functional correspondence between f and g, we
can write
f

rt | σt, θ

∼g

rt | σt, ζ

.
2. Guess a value for θ and simulate a sample

r∗
(n), σ ∗
(n)

of size N (n = 1, . . . ,
N) from the ‘‘true’’ data-generating process, f

rt|σt, θ

. Then, evoking
the ‘‘closeness’’ of ζ and θ, we could expect that20
SN
ζ, θ

= 1
N
N

n=1
∂
∂ζ log g

r∗
(n)|σ ∗
(n),ζ

≈0.
(10.16)
19We express gratitude to Doug Steigerwald from the Department of Economics at
the University of California, Santa Barbara, for providing consulting assistance on
the topic of EMM estimation.
20The expression in (10.16) is the empirical analog to the GMM moment equation
S
ζ, θ

=

∂
∂ζ log g

rt | σt,ζ

f

rt | σt, θ

dσt.

198
BAYESIAN METHODS IN FINANCE
Note that θ is only implicitly present above (its value determined r∗
(n)
and σ ∗
(n)).
3. Compute the value of the criterion function, , using the MLE, ζ, to
assess the proximity of the score to 0:
 ≡SN
ζ, θ
′I−1
N SN
ζ, θ

.
(10.17)
The weighting matrix, IN, is computed as the covariance matrix
estimator
IN = 1
N
N

n=1
 ∂
∂ζ log g

r∗
(n) | σ ∗
(n),ζ
  ∂
∂ζ log g

r∗
(n) | σ ∗
(n),ζ
′
.
4. Iterate the procedure a large number of times by guessing a different
value for θ, simulating a sample

r∗
(n), σ ∗
(n)

and computing the criterion
function in (10.17).
5. Select as the EMM estimator of θ the parameter vector value for which
the criterion function has minimal value; that is,
θ = arg min
θ
.
(10.18)
ILLUSTRATION: FORECASTING VALUE-AT-RISK
Value-at-risk (VaR) is a measure of the possible maximum loss that could
be incurred (with a given probability) by an investment over a given period
of time. VaR has become the standard tool used by risk managers thanks
in part to its adoption in 1993 by the Basel Committee (at the Bank for
International Settlements) as a technique for assessing capital requirements
of banks.21 We discuss the advantages and deficiencies of VaR as a risk
measure in Chapter 13. Here, we focus on how volatility models could be
used to assess VaR.
In statistical terms, the VaR at significance level α is simply the
1 −α quantile of the return distribution. Volatility model predictions
can be used to compute the VaR, since a distribution’s quantile is a
21VaR models originated with the work of the RiskMetrics Group at JP Mor-
gan (Risk-Metrics Technical Document (1986)). For more on VaR, see Jorion
(2000), Khindanova and Rachev (2000), and Rachev, Khindanova, and Schwartz
(2001).

Volatility Models
199
function of the distribution variance. Consider the model for asset returns
in (10.2) and suppose that the disturbances, ϵt, have a normal distribu-
tion. Then the asset return is distributed conditionally as N

µt|t−1, σ 2
t|t−1

.
(The unconditional distribution is nonnormal and fat-tailed.) The 5%
quantile of the normal return distribution (that is, the return threshold
such that there is 5% chance of occurrences below it) is given by the
expression
µt|t−1 −1.65σt|t−1,
where −1.645 is the 5% quantile of the standard normal distribution.
In Chapter 11, we consider a Student’s t GARCH(1,1) model. The
5% quantile of the return distribution is computed from the expres-
sion
µt|t−1 −1.81
ν
ν −2σt|t−1,
where −1.81 is the 5% quantile of the Student’s t-distribution (with mean
zero and scale 1) with ν degrees of freedom. (While the conditional return
distribution is Student’s t, the unconditional distribution is not and has
tails heavier than those of the Student’s t-distribution.) As an illustration,
consider Exhibit 10.1 in which daily MSCI Canadian (innovations of)
returns, together with the corresponding VaR at the 95% confidence level,
are plotted. (See Chapter 11 for details on that illustration.) While returns
are expected to violate the VaR threshold at the 5% confidence level
about 5% of the time, the violations in this particular illustration are
only 3.4%.
12/94
9/95
6/96
3/97
12/97
9/98
7/99
4/00
10/01
3/02
−0.04
−0.03
−0.02
−0.01
0
0.01
0.02
0.03
0.04
Daily Returns
VaR at 5%
EXHIBIT 10.1
Daily MSCI canadian returns and value-at-risk

200
BAYESIAN METHODS IN FINANCE
AN ARCH-TYPE MODEL OR A STOCHASTIC
VOLATILITY MODEL?
The inevitable question arising in a discussion of volatility estimation is
which type of models, ARCH-type or SV, is a better tool for modeling
asset volatility. A definitive answer is not available. Nevertheless, casting
aside the differences in the difficulty level of model estimation (favoring
ARCH-type models), one could argue that evidence points to an advantage
of the basic SV model over the basic GARCH(1,1) model. For example,
Geweke (1995) performs a comparison of the two with the help of posterior
odds ratios.22 Although the two models, applied to exchange rates dynamics,
fare similarly well in periods of low volatility and sustained volatility, the SV
model provides a superior prediction record in periods of volatility jumps.
In particular, empirically observed volatility jumps are more plausible under
the SV model than under the GARCH model. We should note, however,
that this conclusion is valid under normal distributional assumptions for
both models. Asserting a heavy-tailed return distribution in the GARCH
setting is likely to correct for that deficiency.
In a comparison of a different nature, Jacquier, Polson, and Rossi (1994)
find that the SV model provides a better and more robust description of
the autocorrelation pattern of squared stock returns than a GARCH model,
while some investigations23 have found that the GARCH-filtered residuals
exhibit serial correlation, unlike the SV-filtered residuals.
WHERE DO BAYESIAN METHODS FIT?
In the previous chapters, we explained that the principal motivation for
employing Bayesian methods in estimation of the model parameters is to
account for the intrinsic uncertainty surrounding the estimation process.
Since empirical finance modeling is often ultimately aimed at forecasting,
clearly the plug-in approach where parameter estimates are substituted for
the unknown parameters in the prediction formulas carries the risk of being
the suboptimal approach. These arguments are valid with full force in the
area of volatility estimation and prediction.
A different motivator for the use of Bayesian methods that we have
not previously emphasized explicitly is the formidable power of the Markov
Chain Monte Carlo (MCMC) toolbox in handling complicated models.
22We briefly described the posterior odds ratio in Chapter 3.
23For example, Hsieh (1991).

Volatility Models
201
Even when an analytical expression for the likelihood function is available,
incorporating the various inequality constraints that practical applications
require is often not straightforward in a maximum-likelihood environment.
Moreover, in situations where the likelihood function is nonlinear in the
parameters (virtually all realistic models of financial phenomena), likelihood
optimization could be a prohibitively arduous task, because of the existence
of numerous local optimal points.
Although sometimes computationally complex, the MCMC framework
provides a very flexible avenue for exploring the posterior distributions of
not only the model parameters but functions of them, and to construct the
predictive distribution, all in a single procedure.
In the next two chapters, we discuss the applications of Bayesian
methods to, respectively, ARCH-type models and SV models and their
extensions.

CHAPTER11
Bayesian Estimation of
ARCH-Type Volatility Models
I
n the previous chapter, we provided an overview of the two major
groups of volatility models, the autoregressive conditional heteroskedastic
(ARCH)-type models and the stochastic volatility (SV) models. The purpose
of this chapter is to discuss in detail the Bayesian estimation of the first
group of volatility models.
The Bayesian methodology offers a distinct advantage over the classical
framework in estimating ARCH-type processes. For example, inequality
restrictions, such as a stationarity restriction, are notoriously difficult to
handle within the frequentist setting and straightforward to implement in
the Bayesian one.1 Moreover, in the Bayesian setting, one could easily obtain
the distribution of the measure of stationarity and explore the extent to
which stationarity is supported by the observed data.
Typically, the estimated sum of the parameters capturing the ARCH and
generalized autoregressive conditional heteroskedastic (GARCH) effects2 is
very close to 1, suggesting that shocks to the conditional variance take a
long time to dissipate. Engle and Bollerslev (1986) introduced the integrated
GARCH (IGARCH) process to describe the process when the sum is equal
to one. In that case, shocks to the variance have a permanent effect on future
conditional variances, and the unconditional variance of returns does not
exist. One possible explanation for the high persistence in volatility is that
the ARCH and GARCH parameters vary through time, so that an increase
in the estimated sum is actually an underlying change in the conditional
variance parameters.3
1See, for example, Geweke (1989).
2These two parameters are α and β, respectively, in equation (11.2).
3See, for example, Lamoureux and Lastrapes (1990) and Diebold and Inoue (2001).
202

Bayesian Estimation of ARCH-Type Volatility Models
203
Changes in parameters can be divided into two broad categories:
permanent and reversible. The first type of change takes the form of a
permanent, deterministic shift in the parameter value and is caused by an
exogenous factor, a structural break. Some examples of structural breaks
are stock market crashes, changes in the data-collection and data-processing
practices of data providers, and shifts in the economic paradigm.
It is possible that the time variation of model parameters is due to under-
lying transitions of the data generating process among different regimes
(states of the world). Business cycle fluctuations are an example of such
endogenous factors. The class of models usually employed to describe return
and volatility dynamics in a regime-switching environment is the Markov
(regime-) switching class of models.
In the first part of this chapter, we focus on the simple GARCH(1,1)
model with Student’s t-distributed disturbances. In the second part, in
line with the growing interest among practitioners, we present a Markov
regime-switching extension.
BAYESIAN ESTIMATION OF THE SIMPLE
GARCH(1,1) MODEL
Most of the Bayesian empirical investigations of GARCH processes empha-
size the computational aspects of the models, rather than the choice of prior
distributions for the model parameters. One reason for this is that few, if
any, restrictions exist on the choice of prior distributions since posterior
inference is, without exception, performed numerically. As we discussed
in the previous chapter, since the variance is modeled dynamically, the
unconditional density of rt is not available in closed form and the likelihood
for the GARCH model parameters, L(θ|r, ℑ0) , is represented in terms of the
product of the conditional densities of returns for each period (see (10.8) in
Chapter 10).
In this chapter, in order to reflect the recent trend in the empirical
finance literature, our focus is on the Student’s t distributional assumption
for the return disturbances. (Estimation based on the normal distribution is
performed in a similar way.) This comes at the expense of only a marginal
increase in complexity. Two sampling methods that were discussed in
Chapter 5 are employed to simulate the posterior distribution of the vector
of model parameters, θ, the Metropolis-Hastings algorithm and the Gibbs
sampler.4
4See also Geweke (1989) for an application of importance sampling (discussed in
Chapter 5) to the estimation of ARCH models.

204
BAYESIAN METHODS IN FINANCE
The model we consider is described by the following expressions for the
return and volatility dynamics,
rt = Xtγ + σt|t−1ϵt,
(11.1)
for t = 1, . . . , T, and
σ 2
t|t−1 = ω + αu2
t−1 + βσ 2
t−1|t−2,
(11.2)
where ut−1 = rt −Xtγ . The mean of returns in (11.1) is unconditional and
modeled as a linear combination of K −1 factor returns. If the variance
of returns were constant, (11.1) would have defined a linear regression
model for the return, rt, t = 1, . . . , T, of the type we discussed in Chapter
4.5 The observations of the factor returns at time t are represented by
the 1 × K vector, Xt, whose first element is 1. The K × 1 vector, γ , is
the vector of regression coefficients whose first element is the regression
intercept.
Distributional Setup
Next, we outline the general setup we use in our presentation of the Bayesian
estimation of the GARCH(1,1) model. We modify this setup in the second
half of the chapter, where we discuss regime switching.
Likelihood Function
Denote the observed return data by r = (r1, . . . , rT) and
the model’s parameter vector by θ = (ω, α, β, ν, γ ′). Assuming that ϵt is
distributed with a Student’s t-distribution with ν degrees of freedom, we
write the likelihood function for the model’s parameters as
L

θ | r, ℑ0

∝
T

t=1

(σ 2
t|t−1)−1

1 + 1
ν

rt −Xtγ
2
σ 2
t|t−1
−ν+1
2 
,
(11.3)
where σ 2
0 , is considered as a known constant, for simplicity. Under the
Student’s t assumption for ϵt, the conditional volatility at time t is given by
ν
ν −2σ 2
t ,
for ν greater than 2.
5See also our discussion of modeling the conditional mean in Chapter 10. For
simplicity, it is certainly possible to assume that µt|t−1 is a constant (but unknown)
parameter.

Bayesian Estimation of ARCH-Type Volatility Models
205
Prior Distributions
For simplicity, assume that the conditional variance
parameters have uninformative diffuse prior distributions over their respec-
tive ranges,6
π(ω, α, β) ∝1I{θG},
(11.4)
where I{θG} is an indicator function reflecting the constraints on the condi-
tional variance parameters,
I{θG} =

1
if ω > 0, α > 0, and β > 0,
0
otherwise.
(11.5)
The choice of prior distribution for the degrees-of-freedom parameter,
ν, requires more care. Bauwens and Lubrano (1998) show that if a diffuse
prior for ν is asserted on the interval [0, ∞), the posterior distribution of
ν is not proper. (Its right tail does not decay quickly enough such that
the posterior does not integrate to 1.) Therefore, the prior for ν needs
to be proper. Geweke (1993a) advocates the use of an exponential prior
distribution with density given by
π(ν) = λ exp (−νλ).
(11.6)
The mean of the exponential distribution is given by 1/λ. The parameter
λ can thus be uniquely determined from the prior intuition about ν’s
mean. Another prior option for ν is a uniform prior over an interval
[0, K], where K is some finite number. Empirical research indicates that
the degrees-of-freedom parameter calibrated from financial returns data
(especially of daily and higher frequency) is usually less than 20, so the
upper bound, K, of ν’s range could be fixed at 20, for instance. Bauwens and
Lubrano propose a third prior for ν—the upper half of a Cauchy distribution
centered around zero. In our discussion, we adopt the exponential prior
distribution for ν in (11.6).
Finally, for reasons of convenience, we assume a normal prior for the
regression parameters, γ ,
π(γ ) = N(µγ, γ).
(11.7)
6It is possible to assert a prior distribution for ω, α, and β defined on the whole real
line, for example, a normal distribution. To respect the constraints on the values the
parameters can take, that prior would have to be truncated at the lower bound of
the parameters’ range. In practice, the constraints are enforced during the posterior
simulation as explained further below. Alternatively, one could transform ω, α, and
β by taking the logarithm and assert such a prior on the log-parameters, with no
truncation.

206
BAYESIAN METHODS IN FINANCE
In this chapter, we are not bound by arguments of conjugacy (as in
Chapter 4) and we assert a covariance for γ independent of the return vari-
ance, σ 2
t|t−1. (See Chapter 3 for our discussion of prior parameter elicitation.)
Posterior Distributions
Given the distributional assumptions above, the
posterior distribution of θ is written as
p(θ | r, ℑ0) ∝
T

t=1

(σ 2
t|t−1)−1

1 + 1
ν

rt −Xtγ
2
σ 2
t|t−1
−ν+1
2 

× exp

−νλ

× exp

−1
2(γ −µγ)′−1(γ −µγ)

× I{θG}.
(11.8)
The restrictions on ω, α, and β are enforced during the sampling
procedure by rejecting the draws that violate them. Stationarity can also be
imposed and dealt with in the same way.
The joint posterior density clearly does not have a closed form. As it
turns out, posterior simulations are facilitated if one employs the represen-
tation of the Student’s t-distribution, which we discuss next, before moving
on to sampling algorithms.
Mixture of Normals Representation of the Student’s
t-Distribution
Earlier, we assumed that the asset return has the Student’s t-distribution,
rt | γ , σ 2
t|t−1 ∼tν

Xtγ , σt|t−1

,
(11.9)
where we use the notation for the Student’s t-distribution established in
Chapter 3. It can be shown that the distributional assumption in (11.9) is
equivalent to the assumption that
rt | γ , σ 2
t|t−1, ηt ∼N

Xtγ ,
σ 2
t|t−1
ηt

,
(11.10)
where ηt, the so-called mixing variables, are independently and identically
distributed with a gamma distribution,
ηt | ν ∼Gamma
ν
2, ν
2

,
(11.11)

Bayesian Estimation of ARCH-Type Volatility Models
207
for t = 1, . . . , T. The expressions in (11.10) and (11.11) constitute the
scale mixture of normal distributions (i.e., ‘‘normals’’) representation of
the Student’s t-distribution.7 The benefit of employing this representation
is increased tractability of the posterior distribution because the nonlinear
expression for the model’s likelihood in (11.3) is linearized. Sampling from
the conditional distributions of the remaining parameters is thus greatly
facilitated. This comes at the expense of T additional model parameters,
η =

η1, . . . , ηT
′ , whose conditional posterior distribution needs to be
simulated as well.8
Under the new representation, the parameter vector, θ, is transformed to
θ =

ω, α, β, ν, γ ′, η′
.
(11.12)
The log-likelihood function for θ is simply the normal log-likelihood,
log

L

θ | r, ℑ0

= const −1
2
T

t=1

log

σ 2
t|t−1

−log

ηt

+ ηt(rt −Xtγ )2
σ 2
t|t−1

.
(11.13)
The posterior distribution of θ has an additional term reflecting the
mixing variables’ distribution. The log-posterior is written as
log

p

θ | r, ℑ0

= const −1
2
T

t=1

log

σ 2
t|t−1

−log

ηt

+ ηt(rt −Xtγ )2
σ 2
t|t−1

−1
2

γ −µγ
′−1
γ

γ −µγ

+ Tν
2 log
ν
2

−T log


ν
2

+
ν
2 −1

T

t=1
log (ηt)
7Many heavy-tailed distributions can be represented as (mean-) scale mixtures of
normal distributions. Such representations make estimation based on numerical,
iterative procedures easier. See, for example, Fernandez and Steel (2000) for a
discussion of the Bayesian treatment of regression analysis with mixtures of normals.
In continuous time, the mean and scale mixture of normals models lead to the
so-called subordinated processes, widely used in mathematical and empirical finance.
Rachev and Mittnik (2000) offer an extensive treatment of subordinated processes.
We provide a brief description of mixtures of normal distributions in Chapter 13.
8This is an example of the technique known as data augmentation. It consists
of introducing latent (unobserved) variables to help construct efficient simulation
algorithms. For a (technical) review of data augmentation, see van Dyk and Meng
(2001).

208
BAYESIAN METHODS IN FINANCE
−ν
2
T

t=1
(ηt) −νλ,
for
ω > 0,
α ≥0,
and
β ≥0.
(11.14)
Next, we discuss some strategies for simulating the posterior in (11.14).
GARCH(1,1) Estimation Using the Metropolis-Hastings
Algorithm
In Chapter 5, we explained that the Metropolis-Hastings (M-H) algorithm
could be implemented in two ways. The first way is by sampling the whole
parameter vector, θ, from a proposal distribution (usually a multivariate Stu-
dent’s t-distribution) centered on the posterior mode and scaled by the nega-
tive inverse Hessian (evaluated at the posterior mode). The second way is by
employing a sampling scheme in which the parameter vector is updated com-
ponent by component. Here, we focus on the latter M-H implementation.
Consider the decomposition of the parameter vector θ into four com-
ponents, θ =

θG, ν, γ ′, η′
, where θG =

ω, α, β

. We would like to employ
a scheme of sampling consecutively from the conditional posterior distribu-
tions of the four components given, respectively, by
p (θG | γ , η, ν, r, ℑ0),
p (ν | θG, γ , η, r, ℑ0),
p (γ | θG, η, ν, r, ℑ0),
and
p (η | θG, γ , ν, r, ℑ0).
The scale mixture of normals representation of a Student’s t-distribution
allows us to recognize the conditional posterior distributions of the last
two components, γ and η, as standard distributions. For the first two
components, θ G and ν, whose posterior distributions are not of standard
form, we offer two posterior simulation approaches and mention alternatives
that have been suggested in the literature.
Conditional Posterior Distribution for γ
It can be shown that the full con-
ditional posterior distribution of γ is a normal distribution,
p (γ | θG, η, ν, r, ℑ0) = N (γ ∗, V) .
(11.15)

Bayesian Estimation of ARCH-Type Volatility Models
209
The mean and covariance of that normal distribution are defined as
γ ∗= V

X′D−1Xγ + −1
γ µγ

and
V =

X′D−1X + −1
γ
−1 ,
where:
Dinthediagonalmatrixwithdiagonalelementsσ 2
t|t−1/ηt andoff-diagonal
elements equal to zero,
D =


σ 2
1|0
η1
0
0 ···
0
0
σ 2
2|1
η2
0 ···
0
. . . . . . . . . . . . . . . . . . .
0
0
··· 0
σ 2
T|T−1
ηT


,
(11.16)
where σ 2
1|0
is conditional on the initial variance, σ 2
0
(assumed
known).
γ = least-squares estimates of γ from running the regression rt = Xtγ +
σt|t−1ϵt, t = 1, . . . , T, for fixed values of the conditional variance
parameters. The disturbance, ϵt, has a Student’s t-distribution,
X = T × K matrix whose rows are the observations of the explanatory
variables, Xt, for each time period, t = 1, . . . , T.
Conditional Posterior Distribution for η
The full conditional posterior dis-
tribution for the (independently distributed) mixing parameters, ηt, t =
1, . . . , T, can be shown to be a gamma distribution,
p (ηt | θG, γ , ν, r, ℑ0) = Gamma

ν + 1
2
,

rt −Xtγ
2
2σ 2
t|t−1
+ ν
2

.
(11.17)
Conditional Posterior Distribution for ν
It can be seen, from (11.14) that
the conditional posterior distribution of the degrees-of-freedom parameter,
ν, does not have a standard form. The kernel of the posterior distribution is
given by the expression,
p (ν | θG, γ , η, r, ℑ0) ∝
ν
2
−T ν
2
 Tν
2 exp [νλ∗],
(11.18)

210
BAYESIAN METHODS IN FINANCE
where
λ∗= 1
2
T

t=1

log (ηt) −ηt

−λ.
(11.19)
Geweke (1993b) describes a rejection sampling approach that could be
employed to simulate draws from the conditional posterior distribution of
ν in (11.18). In this chapter, we employ a sampling algorithm called the
griddy Gibbs sampler. The appendix provides details on it.
Proposal Distribution for θ G
The kernel of θ G’s log-posterior distribution is
given by the expression,
log

p

θG | θ−θG, r, ℑ0

= const −1
2
T

t=1

log

σ 2
t|t−1

+ ηt(rt −Xtγ )2
σ 2
t|t−1

,
for
ω > 0,
α ≥0,
and
β ≥0.
where σ 2
t|t−1 , t = 1, . . . , T, is a function of θ G.
We specify a Student’s t proposal distribution for θ G, centered on the
posterior mode of θ G (the value that maximizes (11.20)) and scaled by the
negative inverse Hessian of the posterior kernel, evaluated at the posterior
mode, as explained in Chapter 5. Other approaches for posterior simulation,
for example, the griddy Gibbs sampler, could be employed as well. (In this
case, the components of θ G would be sampled separately.)
Having determined the full conditional posterior distributions for γ
and η, as well as a proposal distribution for θ G and a sampling scheme
for ν, implementing a hybrid M-H algorithm, as explained in Chapter 5, is
straightforward. Its steps are as follows. At iteration m of the algorithm:
1. Draw an observation, θ ∗
G , of the vector of conditional variance param-
eters, θ G, from its proposal distribution.
2. Check whether the parameter restrictions on the components of θ G,i are
satisfied; if not, draw θ ∗
G,i repeatedly until they are satisfied.
3. Compute the acceptance probability in (5.7) in Chapter 5 and accept or
reject θ ∗
G.
4. Draw an observation, γ (m), from the full conditional posterior distribu-
tion, p (γ | θ (m)
G , η(m−1), r, ℑ0), in (11.15).
5. Draw an observation, η(m), from the full conditional posterior distribu-
tion, p

ηt | θ (m)
G , γ (m), r, ℑ0

, in (11.17).
6. Draw an observation, ν(m), from its conditional posterior distribution
with kernel in (11.18) using the griddy Gibbs sampler as explained in
the appendix.

Bayesian Estimation of ARCH-Type Volatility Models
211
At each iteration of the sampling algorithm, the sampling strategy just
described produces a large output consisting of the draws from the model
parameters and the T mixing variables, η. However, since the role of the
mixing parameters is only auxiliary and their conditional distribution is of
no interest, at any iteration of the algorithm above the researcher needs to
store only the latest draw of η.
Illustration: Student’s t GARCH(1,1) Model
Next, we illustrate the GARCH(1,1) model with Student’s t disturbances.
Our data sample consists of the daily return data on the same eight
MSCI World Index constituents we considered in Chapter 8. As dependent
variable, we choose the Canada MSCI index return. We employ principal
component analysis to extract the returns on the five factors with greatest
explanatory power using the observed data of the eight indexes. We use
these factor returns as the explanatory variables in X. We estimate the
GARCH(1,1) model using 1,901 return observations spanning December 1,
1994, to March 18, 2002. The prior parameters of the regression coefficients
are determined using estimates from an earlier time period. (See Chapter 3
for our discussion on prior parameter elicitation.) We set the prior mean
of the degrees-of-freedom parameter, ν, at 5, that is, λ = 0.2 in (11.6). The
initial variance, σ 2
0 , is treated as a known constant and set equal to the
unconditional variance of u = Y −Xγ .
We let the MH algorithm run for 10,000 iterations and use only the
latter 5,000 for posterior inference. Exhibit 11.1 presents histograms of the
posterior draws of the three conditional variance parameters, ω, α, and β.
To explore whether the hypothesis of (covariance) stationarity is sup-
ported by the observed data, we compute the posterior distribution of the
quantity αν/(ν −2) + β (see (10.8) in Chapter 10). The histogram of the
draws from that posterior distribution is presented in part D of Exhibit 11.1.
Only a small fraction of the posterior mass lies above 1, indicating that
the hypothesis of stationarity is largely supported by the data. Further in
the chapter, in our discussion on regime-switching models, we examine the
extent to which that high degree of volatility persistence could be ascribed
to the existence of regimes in the conditional volatility dynamics.
The posterior means and standard errors of all model coefficients
are given in Exhibit 11.2. Notice that the posterior mean of ν is 9.24,
suggesting that normality would have been an inadequate assumption for
the distribution of MSCI Canadian daily returns.
Exhibit 11.3 plots the estimated time series of the (smoothed) volatility
for the sample period, together with the time series of MSCI Canadian
returns and squared return innovations.

212
BAYESIAN METHODS IN FINANCE
0
1
2
3
x 106
0
100
200
300
w
0
0.05
0.1
0.15
0.2
0
100
200
300
a
0.7
0.8
0.9
1
0
100
200
300
b
0.85
0.9
0.95
1
1.05
0
100
200
300
Persistence Measure
EXHIBIT 11.1
Histograms of posterior draws of the conditional variance
parameters and persistence measure
Persistence
Measure
6.77e-7
(2.6e-7)
0.089
(0.018)
0.849
(0.033)
9.240
(1.496)
0.965
(0.017)
1
2
3
4
5
6
−1.48e-4
(8.4e-5)
0.302
(0.004)
−0.083
(0.007)
−0.653
(0.008)
0.056
(0.009)
0.064
(0.012)
w
g
g
g
g
g
g
a
b
n
EXHIBIT 11.2
Posterior means of the parameters in the
simple GARCH(1,1) model
Note: The posterior standard errors are in parentheses.

Bayesian Estimation of ARCH-Type Volatility Models
213
12/94
9/95
6/96
3/97
12/97
9/98
7/99
4/00
10/01
3/02
−0.1
−0.05
0
0.05
0.1
Returns, Rt
Squared Return Innovations, (Rt – Xt g)2
12/94
9/95
6/96
3/97
12/97
9/98
7/99
4/00
10/01
3/02
0
0.5
1
1.5
x 10−4
12/94
9/95
6/96
3/97
12/97
9/98
7/99
4/00
10/01
3/02
0
0.5
1
x 10−3
Estimated Volatility, s2
t / t – 1n / (n –2)
EXHIBIT 11.3
Estimated volatility
Finally, we consider the forecasting power of the simple GARCH(1,1)
model and, in Exhibit 11.4, plot the time series of returns and squared return
innovations for the period March 19, 2002, through December 31, 2003 (467
observations), together with the one-day-ahead volatility forecasts. We can
see that the quality of the volatility forecast is generally very good. How-
ever, it does fail to capture accurately all shocks in the realized return data.
For example, notice that the earlier spike in volatility around February 2003
is overpredicted, while the later spike around the same period is underpre-
dicted. One could notice several more such prediction discrepancies.
The forecasting inaccuracy of the simple model could be ascribed to
the possibility that the volatility dynamics themselves differ in different
periods. Then, volatility forecasts produced by a simple (single-regime)
model are likely to overestimate volatility during periods of low volatility
and underestimate it during periods of high volatility. In the next section,
we discuss a class of models extending the simple GARCH(1,1) model
which could potentially provide more accurate volatility forecasting power.
Regime-switching models incorporate the possibility that the dynamics of
the volatility process evolves through different states of nature (regimes).

214
BAYESIAN METHODS IN FINANCE
3/02
5/02
8/02
10/02
12/02
2/03
5/03
7/03
9/03
11/03
−0.05
0
0.05
Future Returns
3/02
5/02
8/02
10/02
12/02
2/03
5/03
7/03
9/03
11/03
0
2
4
x 10−4
Future Squared Return Innovations
3/02
5/02
8/02
10/02
12/02
2/03
5/03
7/03
9/03
11/03
0
2
4
x 10−5
Predicted Volatility
EXHIBIT 11.4
Volatility forecasts
MARKOV REGIME-SWITCHING GARCH MODELS
The Markov switching (MS) models, introduced by Hamilton (1989),
provide maximal flexibility in modeling transitions of the volatility dynamics
across regimes. They form the class of endogenous regime-switching models
in which transitions between states of nature are governed by parameters
estimated within the model; the number of transitions is not specified a
priori, unlike the number of states. Each volatility state could be revisited
multiple times.9 In our discussion that follows, we use the terms state and
regime interchangeably.
9It is certainly possible to introduce (test for) a deterministic permanent shift in a
model parameter into the regime-switching model. For example, Kim and Nelson
(1999) apply such a model to a Bayesian investigation of business cycle fluctuations.
See also Carlin, Gelfand, and Smith (1992). Wang and Zivot (2000) consider
Bayesian estimation of a heteroskedastic model with structural breaks only. The
variance in that investigation, however, does not evolve according to an ARCH-type
process.

Bayesian Estimation of ARCH-Type Volatility Models
215
Different approaches to introducing regime changes in the GARCH
process have been proposed in the empirical finance literature. Hamilton
and Susmel (1994) incorporate a regime-dependent parameter, gSt, into the
standard deviation (scale) of the returns process in (11.2),
rt = µt|t−1 + √gStσt|t−1ϵt,
where St denotes period t’s regime. Another option, pursued by Cai (1994),
is to include a regime-dependent parameter as part of the constant in the
conditional variance equation (11.2),
σ 2
t|t−1 =

ω + gSt

+
P

p=1
αpu2
t−p.
Both Hamilton and Susmel (1994) and Cai (1994) model the dynamics of
the conditional variance with an ARCH process. The reason, as explained
further on, is that when GARCH term(s) are present in the process, the
regime-dependence makes the likelihood function analytically intractable.
The most flexible approach to introducing regime dependence is to allow
all parameters of the conditional variance equation to vary across regimes.
That approach is offered by Henneke, Rachev, and Fabozzi (2006), who
model jointly the conditional mean as an ARMA(1,1) process in a Bayesian
estimation setting.10 The implication for the dynamics of the conditional vari-
ance is that the manner in which the variance responds to past return shocks
and volatility levels changes across regimes. For example, high-volatility
regimes could be characterized by hypersensitivity of asset returns to return
shocks, and high volatility in one period could have a more lasting effect on
future volatilities compared to low-volatility regimes. This would call for a
different relationship between the parameters α and β in different regimes.
In this section, we discuss the estimation method of Henneke, Rachev,
and Fabozzi (2006), with some modifications.
Preliminaries
Suppose that there are three states the conditional volatility can occupy,
denoted by i, i = 1, 2, 3. We could assign economic interpretation to them
by labeling them ‘‘a low-volatility state,’’ ‘‘a normal-volatility state,’’ and
‘‘a high-volatility state.’’ Denote by π ij the probability of a transition from
10See also Haas, Mittnik, and Paolella (2004), Klaassen (1998), Francq and Zakoian
(2001), and Ghysels, McCulloch, and Tsay (1998), among others.

216
BAYESIAN METHODS IN FINANCE
state i to state j. The transition probabilities, π ij, could be arranged in the
transition probability matrix, ,
 =


π11 π12 π13
π21 π22 π23
π31 π32 π33

,
(11.20)
such that the probabilities in each row sum up to 1. The Markov property
(central to model estimation, as we will see below) that lends its name to the
MS models concerns the memory of the process—which volatility regime
the system visits in a given period depends only on the regime in the previous
period. Analytically, the Markov property is expressed as
P

St | St−1, St−2, . . . , S1

= P

St | St−1

.
(11.21)
Each row of  in (11.20) represents the three-dimensional conditional prob-
ability distribution of St, conditional on the regime realization in the previous
period, St−1. We say that {St}T
t=1
is a three-dimensional (discrete-time)
Markov chain with transition matrix, .
In the regime-switching setting of Henneke, Rachev, and Fabozzi, the
expression for the conditional variance dynamics becomes
σ 2
t|t−1 = ω(St) + α(St)u2
t−1 + β(St)σ 2
t−1|t−2.
(11.22)
For each period t,
(ω(St), α(St), β(St)) =



(ω1, α1, β1)
if St = 1,
(ω2, α2, β2)
if St = 2,
(ω3, α3, β3)
if St = 3.
The presence of the GARCH component in (11.22) complicates the model
estimation substantially. To see this, notice that, via σ 2
t−1|t−2 , the current con-
ditional variance depends on the conditional variances from all preceding
periods and, therefore, on the whole unobservable sequence of regimes up
to time t. A great number of regime paths could lead to the particular condi-
tional variance at time t (the number of possible regime combinations grows
exponentially with the number of time periods), rendering classical estima-
tion very complicated. For that reason, the early treatments of MS models
include only an ARCH component in the conditional variance equation.
The MCMC methodology, however, copes easily with the specification in
(11.22), as we will see below.

Bayesian Estimation of ARCH-Type Volatility Models
217
We adopt the same return decomposition as in (11.1) and note that,
given the regime path, (11.22) represents the same conditional variance
dynamics as (11.2). We return to this point again further below when we
discuss estimation of that MS GARCH(1,1) model.
Next, we outline the prior assumptions for the MS GARCH(1,1) model.
Prior Distributional Assumptions
The parameter vector of the MS GARCH(1,1) model, specified by (11.1),
(11.22), and the Markov chain {St}T
t=1 , is given by
θ =

γ ′, η′, ν, θG,1, θG,2, θG,3, π1, π2, π3, S

,
(11.23)
where, for i = 1, 2, 3,
θG,i = (ωi, αi, βi)
and
πi = (πi1, πi2, πi3) ,
and S is the regime path for all periods,
S = (S1, . . . , ST) .
Our prior specifications for γ , η, and ν remain unchanged from our
earlier discussion: The regression coefficients, γ , the scale mixture of normals
mixing parameters, η, and the degrees-of-freedom parameter, ν, are not
affected by the regime specification in the MS GARCH(1,1) model. We
assert prior distributions for the vector of conditional variance parameters,
θ G,i, under each regime, i, and a prior distribution for each triple of transition
probabilities π i, i = 1, 2, 3.
Prior Distributions for θG,i, i = 1, 2, 3
To reflect our prior intuition about
the effect the three regimes have on the conditional variance parameters, we
assert proper normal priors for θ G,i, i = 1, 2, 3.
θG,i ∼N (µi, i) I{θG,i},
(11.24)
where the indicator function, I{θG,i}, is given in (11.5). As explained earlier
in the chapter, the parameter constraints are imposed during the implemen-
tation of the sampling algorithm.
Prior Distribution for πi, i = 1, 2, 3
In Chapter 2, we explained that a con-
venient prior for the probability parameter in a binomial experiment is the
beta distribution. The analogue of the beta distribution in the multivariate

218
BAYESIAN METHODS IN FINANCE
case is the so-called Dirichlet distribution.11 Therefore, we specify a Dirichlet
prior distribution for each triple of transition probabilities, i = 1, 2, 3,
πi ∼Dirichlet (ai1, ai2, ai3)
(11.25)
To elicit the prior parameters, aij, i, j = 1, 2, 3, it is sufficient that one
express prior intuition about the expected value of each of the transition
probabilities in a triple, then solve the system equations for aij.
Estimation of the MS GARCH(1,1) Model
The evolution of volatility in the MS GARCH model is governed by the
realizations of the unobservable (latent) regime variable, St, t = 1, . . . , T.
Hence, the discrete-time Markov chain, {St}T
t=1 is also called a hidden
Markov process. Earlier, we briefly discussed that the presence of the hidden
Markov process creates a major estimation difficulty in the classical set-
ting. The Bayesian methodology, in contrast, deals with the latent-variable
characteristic in an easy and natural way: The latent variable is simulated
together with the model parameters. In other words, the parameter space is
augmented with St, t = 1, . . . , T, in much the same way as the vector of mix-
ing variables, η, was added to the parameter space in estimating the Student’s
t GARCH(1,1) model. The distribution of S is a multinomial distribution,
p (S | π) =
T−1

t=1
p (St+1 | St, π)
= π n11
11 π n12
12 . . . π n32
32 π n33
33
= π n11
11 π n12
12

1 −π11 −π12
n13 . . . π n32
32

1 −π31 −π32
n33,
(11.26)
11A K-dimensional random variable p = (p1, p2, . . . , pK), where pk ≥0 and
K
k=1 pk = 1 , distributed with a Dirichlet distribution with parameters a = (a1, a2,
. . . , aK), ai > 0, i = 1, . . . , K, has a density function
f(p | a) = (K
k=1 ak)
K
k=1 (ak)
K

k=1
p
ak−1
k
,
where  is the gamma function. The mean and the variance of the Dirichlet
distribution are given, respectively, by E(pk) =
ak
a0
and var(pk) =
ak(a0−ak)
a2
0(a0+1) , where
a0 = K
j=1 aj. The Dirichlet distribution is the conjugate prior distribution for the
parameters of the multinomial distribution. As we see in our discussion on the MS
GARCH estimation, the distribution of the Markov chain, {St}T
t=1, is, in fact, a
multinomial distribution.

Bayesian Estimation of ARCH-Type Volatility Models
219
where nij denotes the number of times the chain transitions from state i to
state j during the span of period 1 through period T. The first equality in
(11.26) follows from the Markov property of {St}T
t=1.
Based on our discussion of the Student’s t GARCH(1,1) model and
the hidden Markov process, as well as the prior distributional assumptions
for π i and θ G,i, i = 1, 2, 3, the joint log-posterior distribution of the MS
GARCH(1,1) model’s parameter vector θ is given by
log (p (θ | r, ℑ0)) = const −1
2
T

t=1

log

σ 2
t|t−1

+ log

ηt

+ ηt(rt −Xtγ )2
σ 2
t|t−1

−1
2

γ −µγ
′−1
γ

γ −µγ

−1
2
3

i=1

θG,i −µi
′ −1
i

θG,i −µi

I{S(t)=i}
+ Tν
2 log
ν
2

−T log


ν
2

+
ν
2 −1

T

t=1
log (ηt)
−ν
2
T

t=1
ηt −νλ
+
3

i=1
3

j=1

aij + nij −1

log

πij

,
(11.27)
for ωi > 0, αi ≥0, and βi ≥0.
Although (11.27) looks very similar to the joint log-posterior in (11.14),
there is a crucial difference. The model’s log-likelihood (given by the
right-hand-side term in the first line of (11.27)) depends on the whole
sequence of regimes, S. Conditional on S, however, it is the same log-
likelihood as in (11.13). We exploit this fact in constructing the posterior
simulation algorithm as an extension of the algorithm for the Student’s t
GARCH(1,1) model estimation.
We now outline the posterior results for π i, S, and θ G,i. The posterior
results for the regression coefficients, γ , the degrees-of-freedom parameter,
ν, and the mixing variables, η, remain unchanged from our earlier discussion.
Conditional Posterior Distribution of π i, i = 1, 2, 3
The conditional log-
posterior distribution of the vector of transition probabilities, π i, i = 1, 2, 3,

220
BAYESIAN METHODS IN FINANCE
is given by
log

p

πi | r, θ−πi

= const +
3

j=1

aij + nij −1

log

πij

,
(11.28)
for i = 1, 2, 3, where θ−πi denotes the vector of all parameters except π i. The
expression in (11.28) is readily recognized as the logarithm of the kernel
of a Dirichlet distribution with parameters

ai1 + ni1, ai2 + ni2, ai3 + ni3

.
The parameters aij are specified a priori, while the parameters nij can be
determined by simply counting the number of times the Markov chain,
{St}T
t=1 , transitions from i to j.
Sampling from the Dirichlet distribution in (11.28) is accomplished
easily in the following way.12
1. For each i, i = 1, 2, 3, sample three independent observations,
yi1 ∼χ 2
2

ai1+ni1
,
yi2 ∼χ 2
2

ai2+ni2
,
yi3 ∼χ 2
2

ai3+ni3
,
2. set
πi1 =
yi1
3
k=1 yik
,
πi2 =
yi2
3
k=1 yik
,
πi3 =
yi3
3
k=1 yik
.
Conditional Posterior Distribution of S
In the three-regime switching setup
of this chapter, the number of regime paths that could have potentially
generated ST, the regime in the final period, is 3T. The level of complexity
makes it impossible to obtain a draw of the whole 1 × T vector, S, at once.
Instead, its components can be drawn one at a time, in a T-step procedure.
In other words, at each step, we sample from the full conditional posterior
density of St given by
p (St = i | r, θ−S, S−t) ,
(11.29)
where θ −S is the parameter vector in (11.23) excluding S and S−t is the
regime path excluding the regime at time t. Applying the rules of conditional
probability, p

St = i | r, θ−St

is written as
p (St = i | r, θ−S, S−t) = p (St = i, S−t, r | θ−S)
p (S−t, r | θ−S)
(11.30)
= p (r | θ−S, S−t, St = i) p (St = i, S−t | θ−S)
p (S−t, r | θ−S)
.
12See Anderson (2003).


## Special Topics in Bayesian Estimation

Bayesian Estimation of ARCH-Type Volatility Models
221
The first term in the numerator, p (r | θ−S, S−t, St = i) , is simply the model’s
likelihood evaluated at a given regime path, in which St = i. The second
term in the numerator, p (St = i, S−t), is given, by the Markov property, by
p (St = i, S−t | θ−S) = p

St = i, St−1 = j, St+1 = k | θ−S

= πj,iπi,k,
(11.31)
while the denominator in (11.30) is expressed as
p (S−t, r | θ−S) =
3

s=1
p (St = s, S−t, r | θ−S) .
(11.32)
Using (11.30), (11.31), and (11.32), we obtain the conditional posterior
distribution of St as
p (St = i | r, θ−S, S−t) =
p (r | θ−S, S−t, St = i) πj,i πi,k
3
s=1 p (r | θ−S, S−t, St = s) πj,s πs,k
,
(11.33)
for i = 1, 2, 3. An observation, S∗
t , from the conditional density in (11.33) is
obtained in the following way:
1. Compute the probability in (11.33) for i = 1, 2, 3.
2. Split the interval (0, 1) into three intervals of lengths proportional to
the probabilities in step (1).
3. Draw an observation, u, from the uniform distribution U[0, 1].
4. Depending on which interval u falls into, set S∗
t = i.
To draw the regime path, S(m), at the mth iteration of the posterior simulation
algorithm:
1. Draw S(m)
1
from p

S1 | r, θ−S1

in (11.33). Update S(m) with S(m)
1 .
2. For t = 2, . . . , T, draw S(m)
t
from p

St | r, θ−St

in (11.33). Update S(m)
with S(m)
t .
Proposal Distribution for θ G,i, i = 1, 2, 3
The posterior distribution of the
vector of conditional variance parameters is not available in closed form
because of the regime dependence of the conditional variance. Since, in
the regime-switching setting, we adopted informative prior distributions for

222
BAYESIAN METHODS IN FINANCE
θ G,i, i = 1, 2, 3, the kernel of the conditional log-posterior distribution is a
bit different from the one in (11.20) and is given by
log

p

θG,i | θ−θG,i, r, ℑ0

= const −1
2
T

t=1

log

σ 2
t|t−1

+ log

ηt

+ ηt(rt −Xtγ )2
σ 2
t|t−1

−1
2
3

i=1

θG,i −µi
′ −1
i

θG,i −µi

I{St=i},
for ω > 0, α ≥0, β ≥0, and i = 1, 2, 3.
For a given regime path, S, the only difference between the posterior ker-
nels in (11.20) and (11.34) is the term reflecting the informative prior of θ G,i.
Therefore, specifying a proposal distribution for θ G,i is in no way different
from the approach in the single-regime Student’s t GARCH(1,1) setting.
Sampling Algorithm for the Parameters of the MS
GARCH(1,1) Model
The sampling algorithm for the MS GARCH(1,1) model parameters consists
of the following steps. At iteration m:
1. Draw π (m)
i
from its posterior density in (11.28), for i = 1, 2, 3.
2. Draw S(m) from (11.33).
3. Draw η(m) from (11.17).
4. Draw ν(m) from (11.18).
5. Draw γ (m) from (11.15).
6. Draw θ ∗
G,i, i = 1, 2, 3, from the proposal distribution, as explained
earlier.
7. Check whether the parameter restrictions on the components of θ G,i are
satisfied; if not, draw θ ∗
G,i repeatedly, until they are satisfied.
8. Compute the acceptance probability in (5.7) in Chapter 5 and accept of
reject θ ∗
G,i , for i = 1, 2, 3.
The parameter vector, θ, is updated as new components are drawn. The
steps above are repeated a large number of times until convergence of the
algorithm.
Illustration: Student’s t MS GARCH(1,1) Model
We continue with our earlier illustration in this chapter and this time
estimate the GARCH(1,1) model in the regime-switching setting. We assert

Bayesian Estimation of ARCH-Type Volatility Models
223
a Dirichlet prior with parameters aij = 1, i, j = 1, 2, 3, which implies uniform
prior beliefs about the transition probabilities, π i,j. We elicit the following
prior means for the conditional variance parameter vector, θ G,i, i = 1, 2, 3,
µ1 =


0.0002
0.1
0.6

,
µ2 =


0.2
0.3
0.4

,
and
µ3 =


2
0.6
0.1

.
Our prior choices are based on the following reasoning: The values of
ωi’s prior means reflect our earlier designation of state 1 as the low-volatility
state, of state 2 as the medium-volatility state, and of state 3 as the
high-volatility state. (Recall the expression for the unconditional variance
in (10.9).) We keep the sum of the prior means of αi and βi fixed but assert
different trade-offs between those two parameters (for each i, i = 1, 2, 3).
One could hypothesize that in periods of high volatility, investors tend to
overreact to unexpected information arrivals and in general, to shocks in
returns, compared to periods of low volatility. Then, the value of α could
be expected to be higher than the value of β in high-volatility states. For
simplicity, we set the prior covariance matrix of θ G,i to be equal to the
identity matrix for i = 1, 2, 3. We note that this choice implies somewhat
strong beliefs for the prior means of ω3 and of αi and βi, i = 1, 2, 3.
We keep the prior distributional assumptions for the rest of the model
parameters.
The posterior parameter estimates for the Student’s t MS GARCH(1,1)
model are provided in Exhibit 11.5. We observe that the posterior means
of the conditional variance parameters roughly comply with our prior
intuition. The persistence of volatility in states 1 and 2 is substantially
lower than that in the simple GARCH(1,1) model considered earlier in the
chapter. There is clear evidence of nonstationarity in state 3. (Its measure of
persistence has a posterior mean of 1.386.)
Exhibit 11.6 presents the posterior probabilities of regimes 1, 2, and
3, as well as the squared return innovations. We could conclude from it
that state 1 is indeed the low-volatility state, state 2 is a medium-to-high

224
BAYESIAN METHODS IN FINANCE
1
1
1
Persistence 
Measure
Regime 1
1.41e-5
(4.7e-6)
0.031
(0.011)
0.048
(0.013)
0.053
(0.034)
2
2
2
Regime 2
8.6e-5
(2.1e-5)
0.074
(0.039)
0.301
(0.073)
0.377
(0.079)
3
3
3
Regime 3
0.531
(0.203)
0.751
(0.227)
0.575
(0.261)
1.386
(0.335)
j,1
j,2
j,3
1,k
0.988
(0.002)
0.007
(0.003)
0.005
(0.004)
2,k
0.030
(0.008)
0.938
(0.022)
0.032
(0.024)
3,k
0.454
(0.098)
0.365
(0.111)
0.181
(0.096)
1
2
3
4
5
6
30.07
(4.61)
–9.2e-5
(9.8e-5)
0.297
(0.005)
–0.078
(0.007)
–0.641
(0.009)
0.056
(0.014)
0.066
(0.015)
w
a
b
w
a
b
w
a
b
p
p
p
p
n
g
g
g
g
g
g
p
p
EXHIBIT 11.5
Posterior means of the parameters in the MS GARCH(1,1) model
Note: The posterior standard errors are in parentheses.
volatility state, while state 3 is a transient state, which ‘‘switches on’’ when
innovation shocks occur. This observations is supported by the posterior
means of the transitional probabilities (see Exhibit 11.5). The volatility
process only rarely visits state 3 and, when it does, it tends to transition to
one of the other two states fairly quickly. Notice, in contrast, the tendency
of state 1 and state 2 to last (the posterior means of π 1,1 and π 2,2 are,
respectively, 0.988 and 0.938).

Bayesian Estimation of ARCH-Type Volatility Models
225
12/94
9/95
6/96
3/97
12/97
9/98
7/99
4/00
10/01
3/02
0
0.5
1
x 10–3
(a)
12/94
9/95
6/96
3/97
12/97
9/98
7/99
4/00
10/01
3/02
0.2
0.6
1
(b)
12/94
9/95
6/96
3/97
12/97
9/98
7/99
4/00
10/01
3/02
0.2
0.6
1
(c)
12/94
9/95
6/96
3/97
12/97
9/98
7/99
4/00
10/01
3/02
0.1
0.3
0.5
(d)
EXHIBIT 11.6
Posterior regime probabilities in the MS GARCH(1,1) model
Note: Panel (A) shows the plot of the squared return innovations. Panels (B), (C),
and (D) contain the plots of the posterior probabilities of regimes 1, 2, and 3,
respectively.
SUMMARY
In this chapter, we discussed the GARCH(1,1) model with Student’s
t-distributed disturbances and the Markov regime-switching GARCH(1,1)
model. Estimation of both is easily handled in the Bayesian setting with
the help of the numerical methods discussed in Chapter 5. Markov
regime-switching models are governed by an unobserved latent variable
(assumed to evolve according to a Markov process). Where a classical
statistician would deal with the regime variable by integrating it out of
the likelihood, the Bayesian practitioner simply simulates it along with the
remaining model parameters.

226
BAYESIAN METHODS IN FINANCE
The regime-switching GARCH(1,1) model we covered in this chapter
provides a bridge to our presentation of stochastic volatility models in the
next chapter. Stochastic volatility models are members of the class of the
so-called state-space models. Volatility is the (unobserved) state variable in
those models and it evolves through time according to an autoregressive
process. Unlike Markov regime-switching models, in which transitions
between regimes (states) occur in a discrete fashion, the volatility’s dynamics
in stochastic volatility models has a source of randomness that may or may
not be correlated with the disturbances of the asset returns. The dynamics
of the transitions between regime switches is time-continuous and driven by
the stochastic volatility process.
Markov switching can be introduced into state-space models, such as
stochastic volatility models. See, for example, Kim and Nelson (1999) for a
detailed exposition.
APPENDIX: GRIDDY GIBBS SAMPLER
In Chapter 5, we discussed that implementation of the Gibbs sampler
requires that parameters’ conditional posterior distributions be known.
Sometimes, however, the conditional posterior distributions have no closed
forms. In these cases, a special form of the Gibbs sampler, called the griddy
Gibbs sampler, can be employed whereby the (univariate) conditional
posterior densities are evaluated on grids of parameter values. The griddy
Gibbs sampler, developed by Ritter and Tanner (1992), is a combination
of the ordinary Gibbs sampler and a numerical routine. In this appendix,
we illustrate the griddy Gibbs sampler with the posterior distribution of the
degrees-of-freedom parameter, ν.
Recall the expression for the kernel of ν’s conditional log-posterior
distribution,
log (p (ν | θ−ν, r, ℑ0)) = const + Tν
2 log
ν
2

−T log


ν
2

+
ν
2 −1

T

t=1
log (ηt) −ν
2
T

t=1
ηt −νλ.
(11.34)
The griddy Gibbs sampler approach to drawing from the conditional
posterior distribution of ν is to recognize that at iteration m we can treat the
latest draws of the remaining parameters as the known parameter values.
Therefore, we can evaluate numerically the conditional posterior density
of ν on a grid of its admissible values. The support of ν is the positive

Bayesian Estimation of ARCH-Type Volatility Models
227
part of the real line. However, a reasonable range for the values of ν in an
application to asset returns could be (2, 30).13
Drawing from the Conditional Posterior Distribution
of ν
Denote the equally spaced grid of values for ν by

ν1, ν2, . . . , νJ

. We outline
the steps for drawing from ν’s conditional posterior distribution at iteration
m of the sampling algorithm. Denote the most recent draws of the remaining
model parameters by θ (m−1)
−ν
. (Note that this notation is not entirely precise
since some of the parameters might have been updated last during the mth
iteration of the sampler but before ν.)
1. Compute the value of ν’s posterior kernel (the exponential of the
expression in (11.34)) at each of the grid nodes and denote the resultant
vector by
p(ν) =

p(ν1), p(ν2), . . . , p(νJ)

.
(11.35)
2. Normalize p(ν) by dividing each vector component in (11.35) by the
quantity J
j=1 p(νj)(ν2 −ν1).14 For convenience of notation, let us rede-
fine p(ν) to denote the vector of (normalized) posterior density values
at each node of ν’s grid.
3. Compute the empirical cumulative distribution function (CDF),
F(ν) =

p(ν1),
2

j=1
p(νj), . . . ,
J

j=1
p(νj)

.
(11.36)
If the grid is adequate, the first element of F(ν) should be nearly 0, while
the last element of F(ν) nearly 1.
1. Draw an observation from the uniform distribution (U[0, 1]) and denote
it by u.
2. Find the element of F(ν) closest to u without exceeding it.
13This is the typical range of the degrees-of-freedom parameter of a Student’s
t-distribution fitted to return data. The higher the data frequency is, the more
heavy-tailed returns are and the lower the value of the degrees-of-freedom parameter.
14Recall that the posterior kernel is the posterior density up to a constant of pro-
portionality. The normalizing constant is the denominator in the Bayes formula (see
Chapter 2) and given by
 
L

θ|r, ℑ0

p(ν|θ−ν, r, ℑ0)dν. This integral is approximated
by the weighted sum J
j=1 p(νj)(ν2 −ν1). The weight, ν2 −ν1, is constant, since the
grid of ν values is equally spaced.

228
BAYESIAN METHODS IN FINANCE
3. The grid node corresponding to the value of F(ν) in the previous step is
the draw of ν from its posterior distribution.
The method above of obtaining a draw from ν’s distribution using its
CDF is called the CDF inversion method.
Constructing an adequate grid is the key to efficient sampling from
ν’s posterior. Since the griddy Gibbs sampling procedure relies on multiple
evaluations of the posterior kernel, two desired characteristics of an adequate
grid are short length and coverage of the parameter support where the
posterior distribution has positive probability mass. A simple example
illustrates this point. Suppose that for a given sample of observed data,
the likely values of ν are in the interval (2, 15). Suppose further that we
construct an equally spaced grid of length 30, with nodes on each integer
from 2 to 30. The value of the posterior kernel at the nodes corresponding to
ν equal to 16 and above would be only marginally different from zero. The
posterior kernel evaluations at those nodes should be avoided, if possible.
If no prior intuition exists about what the likely parameter values are,
one could employ a variable grid instead of a fixed grid. At each iteration of
the sampling algorithm one must analyze the distribution of posterior mass
and adjust the grid, so that the majority of the grid nodes are placed in the
interval of greatest probability mass. Automating this process could involve
some computational effort.

CHAPTER12
Bayesian Estimation of
Stochastic Volatility Models
I
n this chapter, we maintain our focus on volatility modeling and dis-
cuss Bayesian estimation of the second large class of volatility models,
stochastic volatility (SV) models. Continuous SV models have enjoyed a lot
of attention in the literature as a way to generalize the constant-volatility
assumption of the Black-Scholes option pricing formula.1 In empirical
work, the discrete-time SV model of Taylor (1982, 1986) is their natural
counterpart.
The characteristic distinguishing SV models from GARCH models is
the presence of an unobservable shock component in the volatility dynamics
process. Volatility is thus itself latent—its exact value at time t cannot
be known even if all past information is employed to determine it. As
more information becomes available, the volatility in a given past period
could be better evaluated. Both contemporaneous and future information
thus contribute to learning about volatility. In contrast, in the determin-
istic setting of the simple GARCH volatility process, the volatility in a
certain time period is known, given the information from the previous
period.
Together with ARCH-type models, SV models attempt to explain
empirically-observed return characteristics such as time-varying variance
(heteroskedasticity), heavy-tailedness, and volatility clustering. In an ARCH-
type model, the heavy-tailedness of returns is tied solely to their het-
eroskedasticity because the source of volatility variability is volatility
dependence on past volatility (and past return shocks). This is not the
1See Hull and White (1987), Chesney and Scott (1989), and Harvey, Ruiz, and
Shephard (1994), among others.
229

230
BAYESIAN METHODS IN FINANCE
case in SV models. Even if the volatility at time t did not depend on the
volatility in the previous time period, the random component (innovation)
in the SV process itself would induce heavy tails in the unconditional return
distribution.
In this chapter, we present step-by-step the estimation of SV mod-
els within the Bayesian context. Our focus is on two Markov Chain
Monte Carlo (MCMC) approaches. The first approach is the so-called
‘‘single-move sampler,’’ examples of which we have seen already in Chapter
11. It consists of updating the parameter vector a single parameter
at a time.
Some researchers have argued that when parameters are correlated,
particularly in time-series models, that single-move procedure results in
a slower speed of convergence of the Markov chain. Algorithms, called
multimove samplers, updating several variables at a time, could then be a
more efficient sampling alternative.
We conclude the chapter with a description of a jump extension to the
SV model.
PRELIMINARIES OF SV MODEL ESTIMATION
From a practical perspective, the primary goal of a SV model is to provide
inference for (estimate) the sequence of unobserved volatilities and to predict
their values a certain number of periods ahead. MCMC methods offer a
framework both for estimating the parameters of the SV models and for
assessing the latent volatilities. The design of the MCMC procedure is
crucial for the chain’s speed of convergence. Estimation of latent variable
models (SV models, in particular) highlights the importance of the design
because the number of unknown parameters is of the same order as the
sample of data.
Carlin, Polson, and Stoffer (1992) first presented a Bayesian treatment
of state-space models, while Jacquier, Polson, and Rossi (JPR) (1994) offered
the first Bayesian SV model analysis. Since then, the literature of Bayesian
SV estimation has been prolific.
The basic SV model assumes that the dynamics of the logarithm of
volatility is governed by a stationary stochastic process in the form of an
autoregressive process of order 1 (AR(1)). The following two equations
specify the SV model,
rt = exp(ht/2)ϵt
(12.1)
and
ht = ρ0 + ρ1ht−1 + τηt,
(12.2)

Bayesian Estimation of Stochastic Volatility Models
231
where:2 ht = log

σ 2
t

.
rt = asset return observed in period t, t = 1, . . . , T.
ϵt = disturbance of the return process distributed
independently and identically with a standard normal
distribution, t = 1, . . . , T.
ηt = disturbance of the volatility process distributed
independently and identically with a standard normal
distribution, t = 1, . . . , T.
ρ0 and ρ1 = parameters of the volatility process.
τ = scale parameter of the volatility disturbance.
For simplicity, we do not model the conditional mean of returns
and assume it is zero in our discussion. The disturbances, ϵt and ηt,
are assumed independent in the basic SV model. It is, however, possible to
introduce correlation between them and thus model the empirically observed
asymmetric response of volatility to return shocks.3 The volatility process is
stationary if the parameter ρ1 takes values in the open interval (−1, 1).
Likelihood Function
Let us denote the vector of model parameters by θ,
θ =

ρ0, ρ1, τ 2
.
2The model defined by (12.1) and (12.2) is an example of a (nonlinear) state-space
model. A simple Gaussian linear state-space model is defined by the following set of
equations:
yt = at + ϵt
at = at−1 + ηt
for t = 1, . . . , T, where the disturbances are independently distributed as ϵt ∼
N(0, σ 2
ϵ ) and ηt ∼N(0, σ 2
η ). The variable at is unobserved and called the state
variable. Inference about it is usually of interest in state-space models, as it provides
knowledge about the system’s evolution through time. Inference is based on the
values of the observed variable, yt, t = 1, . . . , T. The first equation above is referred
to as the observation equation and the second equation as the state equation. A
widely employed tool in the estimation of state-space models is the Kalman filter, and
later in the chapter we discuss how it can be integrated into an MCMC algorithm.
The Bayesian framework alone can also be employed to deal with state space models,
as we describe in the section on the single-move MCMC algorithm.
3See, for example, Jacquier, Polson, and Rossi (2004) for the Bayesian treatment of
this model extension.

232
BAYESIAN METHODS IN FINANCE
Since the volatility is unobservable, the likelihood function for θ is not
available in a closed form as we explained in Chapter 10. Instead, it is
expressed as an analytically intractable T-dimensional integral with respect
to the T latent volatilities,
L (θ | r) =
T

t=1

f

rt | σ 2
1 , . . . , σ 2
T

f

σ 2
1 , . . . , σ 2
T | θ

dσ 2
1 . . . dσ 2
T,
(12.3)
whereweusethenotationestablishedearlierinthischapterandinChapter10.
The reason for the likelihood intractability above is the same as in the case
of regime-switching models. It is no surprise then that the approach to deal
with the problem is data augmentation, as in the regime-switching setting.
The latent volatilities are simulated together with the rest of the model param-
eters from their conditional distribution. A single algorithm thus helps obtain
the Bayesian parameter estimates and evaluate the volatilities.
Next, we discuss the single-move MCMC approach to SV model esti-
mation of JPR.
THE SINGLE-MOVE MCMC ALGORITHM FOR SV MODEL
ESTIMATION
The single-move MCMC approach to SV model estimation is characterized
by simulating the path of unobserved volatility element by element in the
same way the regime path was simulated in Chapter 11.
Prior and Posterior Distributions
Were the variable ht in (12.2) known, that expression would have defined a
simple linear regression model. Within an MCMC sampling environment,
at each iteration of the algorithm, ht can indeed be treated as known when
sampling the remaining parameters. One can, therefore, assert conjugate
priors for the three parameters ρ0, ρ1, and τ in order to obtain standard-form
posterior distributions for them. The conjugate priors in the normal linear
model are a bivariate normal distribution and an inverted χ 2 distribution
(see Chapter 4),
 ρ0
ρ1

≡β ∼N

β0, τ 2A

,
(12.4)
and
τ 2 ∼Inv-χ 2 
ν0, c2
0

.
(12.5)
The posterior distributions are of the same form as the prior ones.
Sampling from them is straightforward. (See Chapter 4.)

Bayesian Estimation of Stochastic Volatility Models
233
Conditional Distribution of the Unobserved Volatility
To simulate the unobserved volatility component by component, one needs to
obtain the conditional density of the volatility in a given period, σ 2
t , t = 1, . . . ,
T. Denote by σ 2
−t the vector of volatilities for all periods but period t. Using
the Markov property, it can be shown that the conditional density is4
p

σ 2
t | σ 2
−t, θ, r

∝p

σ 2
t | σ 2
t−1

p

σ 2
t+1 | σ 2
t

p

yt | σ 2
t

∝1
σt
exp

−r2
t
2σ 2
t
 1
σ 2
t
exp

−

log

σ 2
t

−at
2
2b2

,
(12.6)
where
at = ρ0(1 −ρ1) + ρ1

log

σ 2
t−1

+ log

σ 2
t+1

1 + ρ2
1
and
b2 =
τ 2
1 + ρ2
1
.
The beginning log-volatility value, h1 = log (σ 2
1 ), can be specified outside
of the model for convenience and considered constant. As an alternative,
JPR suggest that one could use the time-reversibility of the autoregressive
process of order 1 for the log-volatility in (12.2), so that h0 is obtained as a
two-step backward prediction,
h0 = ρ0 + ρ1

ρ0 + ρ1h2

.
(12.7)
The log-volatility value at time T + 1, hT+1 = log (σ 2
T+1), could also be
obtained from the autoregressive dynamics in (12.2); for example, by using
a two-step forward prediction,
hT+1 = ρ0 + ρ1

ρ0 + ρ1hT−1

.
The volatilities σ 2
1 and σ 2
T can then be simulated according to (12.6).5
4The term 1/σ 2
t is the Jacobian of the transformation of σ 2
t to log

σ 2
t

in the density
of σ 2
t in (12.6).
5Yet a third option for specifying the beginning log-volatility value, h1, is to assume
that it is randomly distributed according to the stationary volatility distribution,
h1 ∼N

ρ0
1 −ρ1
,
τ 2
1 −ρ2
1

.

234
BAYESIAN METHODS IN FINANCE
Since the conditional density in (12.6) is not of standard form, numerical
methods are employed to simulate the unobserved volatility path. Various
sampling approaches could be employed. Now, we discuss one based on the
Metropolis-Hastings(MH)algorithm.ThegriddyGibbssamplerexplainedin
Chapter 11 can also be employed for component-by-component simulation.
Simulation of the Unobserved Volatility
As we discussed in earlier chapters, an adequate proposal density ensures
efficient density simulation. Consider the full conditional density in (12.6).
One could notice that it is made up of the kernels of two distributions. The
first one,
1
σt
exp

−r2
t
2σ 2
t

=
 1
σ 2
t
−(1/2−1)
exp

−1
σ 2
t
r2
t
2

,
(12.8)
can be recognized as the kernel of an inverted gamma distribution with a
shape parameter 1/2 and a scale parameter r2
t /2. The second kernel,
1
σ 2
t
exp

−

log

σ 2
t

−at
2
2b2

,
(12.9)
is the kernel of a log-normal distribution, with parameters at and b2.6
The inverted gamma distribution and the log-normal distribution have
the so-called multiplicative property: The product of two or more variables
6Consider a normally distributed random variable, Y, with mean µ and variance s2.
Suppose that Y is transformed as X = exp(Y). Then X is said to be distributed with
the log-normal distribution. Its density is given by
f(x | µ, s2) =
1
xs
√
2π
exp

−(log(x) −µ)2
2s2

.
The mean and the variance of X are functions of µ and s2 given, respectively, by
E(X) = exp

µ + s2
2

and
var(X) =
	
exp
	
s2
−1

exp
	
2µ + s2
.
The log-normal distribution is a very popular distribution in finance. For example,
the assumption that asset returns follow a normal distribution immediately implies
that the underlying asset prices are log-normally distributed, because the asset return
for a given period, 
, and price at time t, Pt, is defined as log (Pt+
/P(t)).

Bayesian Estimation of Stochastic Volatility Models
235
with either distribution preserves the distributional form. Since both dis-
tributions are skewed to the right, one could be approximated with the
other, so that the product has either the form of an inverted gamma or a
log-normal distribution.
JPR choose to approximate the log-normal distribution in (12.9) with
an inverted gamma distribution by matching their means and variances.
Denote the parameters of the approximating inverted gamma distribution
by φ1 and φ2. Then
φ2
φ1 −1 = exp

at + b2
2

and
φ2
2
(φ1 −1)2(φ1 −2) =

exp

b2
−1

exp

2at + b2
.
From these two equations, the values of φ1 and φ2 can be determined as
φ1 = 2 exp(b) −1
exp(b) −1
and
φ2 = exp

at + 3b2/2

exp

b2
−1
.
The product of the inverted gamma distribution in (12.8) and the
approximating one is also an inverted gamma with parameters
φ1 −1
2 + 1
and
φ2 + r2
t
2 .
(12.10)
That inverted gamma distribution with parameters in (12.10) con-
stitutes the proposal distribution for the conditional density in (12.6).
Component-by-component simulation of the unobserved volatilities, σ 2
t ,
t = 1, . . . , T, consists of the following MH algorithm steps. To draw σ 2
t
from its conditional distribution,

236
BAYESIAN METHODS IN FINANCE
1. Draw σ 2
t from an inverted-gamma distribution with parameters given
in (12.10).
2. Compute the acceptance probability by applying the formula in (5.7) in
Chapter 5 and accept or reject σ 2
t , as explained in that chapter.
Illustration
Exhibit 12.1 presents JPR’s estimation results for four series of weekly
returns—a value-weighted index of NYSE stocks, and three portfolios
of stocks sorted according to their market capitalization—for the period
July 1962 through December 1991. Before estimation, JPR remove the
autoregressive and monthly systematic component from weekly returns.
That is, the autoregressive and monthly components are estimated with a
linear regression and the SV model in (12.1) and (12.2) is fitted to the
residuals from that regression.
The variable CV2 in the exhibit is the squared coefficient of variation of
the volatility process, which is a measure of the variability of volatility and
is defined as
CV2 = var(h)
E(h)2 = exp

τ
1 −ρ2
1

−1.
NYSE
P1
P5
P10
−0.39
(0.11)
−0.56
(0.12)
−0.71
(0.36)
−0.56
(0.18)
1
0
−0.95
(0.013)
−0.93
(0.016)
−0.91
(0.046)
−0.93
(0.022)
0.23
(0.026)
0.32
(0.032)
0.32
(0.095)
0.29
(0.056)
CV2
0.8
(0.24)
1.1
(0.28)
0.92
(0.27)
0.93
(0.25)
EXHIBIT 12.1
Single-move SV model estimation: Posterior results
Source: Adapted from Table 1 in Jacquier, Polson, and Rossi (1994). The posterior
standard deviation is in parentheses. P1, P5, and P10 are the portfolios composed of
the NYSE stocks in the first, fifth, and tenth decile, respectively, according to their
market capitalization.

Bayesian Estimation of Stochastic Volatility Models
237
The values of CV2 in the exhibit are the posterior means of the
simulations of the coefficient of variation, computed using the simulations
of ht and τ 2. We could observe that the smallest stocks (of which portfolio
P1 is composed) are more variable than the larger ones, as indicated by CV2,
and all weekly series exhibit a high degree of volatility persistence indicated
by the posterior means of ρ1.
The JPR’s single-move approach is attractive with its conceptual sim-
plicity and ease of implementation. Some researchers have argued, however,
that the successive MCMC parameter draws based on JPR’s algorithm
exhibit high correlations. As we explained in Chapter 5, the correlations’
magnitude affects the speed of convergence (although not the convergence
itself) of the sampling algorithm.
Next, we review an efficient sampling scheme developed by Kim,
Shephard, and Chib (1998).7
THE MULTIMOVE MCMC ALGORITHM FOR
SV MODEL ESTIMATION
We consider the same simple SV model as in (12.1) and (12.2). As a
motivation for the discussion of the multimove sampling algorithm, consider
Exhibit 12.2. It contains the plots of the autocorrelations of the posterior
simulations for ρ1 and τ from the single-move sampler of JPR and the
multimove sampler of Kim, Shephard, and Chib. Simulations using JPR’s
sampling scheme have a higher degree of autocorrelation, indicating that
the MCMC algorithm might take longer to converge.
Prior and Posterior Distributions
As in the earlier discussion, the prior distribution for τ 2 is the conjugate
prior for the variance of normal models, namely, an inverted χ 2 distribution
with parameters α and β.8 Kim, Shephard, and Chib (1998) assert a normal
prior for the intercept, ρ0, in the volatility dynamics equation. The choice
of prior distribution for the persistence parameter, ρ1, is dictated by the
goal of imposing stationarity (i.e., restricting ρ1 within the interval (−1, 1)).
That prior is based on the beta distribution. To obtain the prior, define φ
to be a random variable taking values between 0 and 1, distributed with a
7See also Chib, Nardari, and Shephard (2002), and Mahieu and Schotman (1998)
among others.
8Chib, Nardari, and Shephard (2002) assert a log-normal distribution for τ.

238
BAYESIAN METHODS IN FINANCE
0
0
1
450
900
1350
1800
0
0
1
450
900
1350
1800
0
50
100
0
1
0
50
100
.5
1
1
1
EXHIBIT 12.2
Comparison of the single-move algorithm and the multimove
algorithm
Source: Adapted from Figure 2 and Figure 5 in Kim, Shephard, and Chib (1998).
The plots in the upper row correspond to simulations obtained using the single-move
sampler, while the plots in the lower row correspond to simulations obtained using
the multimove sampler of Kim, Shephard, and Chib.
beta (φ1, φ2) distribution. Let ρ1 = 2φ −1. Then, ρ1’s range is (−1, 1), as
required, and ρ1 has the prior
π(ρ1) = 0.5 (φ1 + φ2)
(φ1)(φ2) (0.5(1 + φ))φ1−1 (0.5(1 −φ))φ2−1 ,
(12.11)
where  is the gamma function.
Since the prior distributions of τ 2 and ρ0 are conjugate to the normal
distribution, their posteriors preserve the prior distributional forms. The
posterior distribution of ρ1, however, is not of a standard form. To see that,
observe that for a fixed sequence h =

h1, . . . , hT

the joint distribution of
the unobserved volatilities represents a likelihood function for ρ0, ρ1, and
τ 2. The log-likelihood function is written as
log

L

ρ0, ρ1, τ 2 | h

∝−T
2 log τ 2 −
T−1
t=1

ht+1 −ρ0 −ρ1ht
2
2τ 2
.
(12.12)

Bayesian Estimation of Stochastic Volatility Models
239
Then the full conditional log-posterior distribution of ρ1 is given by
log

p

ρ1 | h, r, ρ0, τ 2
∝(φ1 −1) log
1 + ρ1
2

+ (φ2 −1) log
1 −ρ1
2

+
T−1
t=1

ht+1 −ρ0 −ρ1ht
2
2τ 2
.
(12.13)
Since the log-posterior density in (12.13) is not standard, one approach
to posterior sampling is to use the MH algorithm. Kim, Shephard, and Chib
use a normal proposal density centered on the least-squares estimate of ρ1
from a regression of ht+1 on ht and scaled according to the variance of
that least-squares estimate. That is, the mean and variance of the normal
proposal are given, respectively, by

ρ1 =
T−1
t=1 ht+1ht
T−1
t=1 h2
t
(12.14)
and
s2
ρ1 =
τ 2
T−1
t=1 h2
t
.
(12.15)
Another approach to posterior simulation from (12.13) could be to
apply the adaptive rejection algorithm of Gilks and Wild (1992). Next, we
discuss the simulation of the unobserved volatilities, h.
Block Simulation of the Unobserved Volatility
The multimove algorithm approaches simulation of h as a block instead of
component-by-component and is based on the methods for estimation of
models in state-space form, to which the simple SV model defined by (12.1)
and (12.2) belongs.9 The Kalman filter is at the core of the methods for
estimation and prediction in a state-space framework. Simulation algorithms
associated with the Kalman filter can be integrated without effort into a
general MCMC sampling setting. While a detailed discussion of filtering
and smoothing are outside of the scope of the book, we present a brief
overview of basic filtering and smoothing in the appendix to this chapter.10
9See West and Harrison (1997), Harvey (1991), and Durbin and Koopman (2001),
among others, for discussion of state-space model estimation.
10For modifications and extensions of the basic Kalman filtering and smoothing
algorithms targeted at achieving greater efficiency in the context of SV models, see,
for example, Mahieu and Schotman (1998), Shephard (2005), Stroud, Muller, and
Polson (2003), and Durbin and Koopman (2002), among others.

240
BAYESIAN METHODS IN FINANCE
For the purpose of estimation, the expression (12.1) (the observation
equation) needs to be transformed, so that the two SV model equations are
linear with respect to the disturbances, ϵt and ηt, as well as the unobserved
log-volatilities, ht. Squaring and taking the natural logarithm of both sides,
we obtain,
r∗
t ≡log

r2
t

= ht + log ϵ∗
t ,
(12.16)
where ϵ∗
t = ϵ2
t . Kim, Shephard, and Chib observe that the log-χ 2 distribution
of log ϵ∗
t can be adequately approximated with a discrete mixture of normal
distributions with seven mixture components, so that11
ϵ∗
t | λt = j ≈N

µλt, v2
λt

P (λt = j) = pj,
(12.17)
for j = 1, 2, . . . , 7. The approximate density of ϵ∗
t is then
g

ϵ∗
t | λt

=
7

j=1
pjfN

ϵ∗
t | µλt, v2
λt

,
where f N is the density function of the normal distribution. The seven
mixture probabilities, pj, as well as the seven pairs of normal means and
variances, µλt and v2
λt, are estimated in a separate (maximum likelihood or
moment-matching) procedure and then considered constants.12
The mixing variable, λt, is treated as an additional (unobservable)
parameter in the SV model and simulated along with the remaining
parameters in the MCMC procedure. Its conditional distribution is given
by
p

λt = j | r∗
t , ht

∝pj exp

−

ϵ∗
t −µλt
2
2v2
λt

,
(12.18)
where ϵ∗
t = r∗
t −ht.
Next, we outline the steps of the MCMC sampling algorithm.
11The number of mixture components is determined empirically. Omori, Chib,
Shephard, and Nakajima (2006) find that a 10-component mixture provides an even
better approximation to the log-χ2 distribution. As explained in Chapter 13, where
we briefly discuss mixtures of normal distributions, an appropriately chosen mixture
of normals could adequately approximate any distribution.
12To correct for the error from employing the discrete mixture approximation in
(12.16), Kim, Shephard, and Chib reweigh the posterior parameter and volatility
draws.

Bayesian Estimation of Stochastic Volatility Models
241
Sampling Scheme
In the simple SV model of the current discussion, the augmented parameter
vector consists of the following components:
■The volatility parameters, θ =

ρ0, ρ1, τ 2
.
■The path of unobservable volatilities, h =

h1, . . . , hT

.
■The mixing parameters, λ = (λ1, . . . , λT).
The parameter components are sampled according to the scheme below.
At iteration m of the algorithm:
■Simulate h using the disturbance smoother algorithm outlined in the
appendix to this chapter.
■Sample ρ0, ρ1, and τ 2 from their posterior distributions outlined earlier.
■Sample λ from its conditional distribution above.
Illustration
Kim, Shephard, and Chib examine the daily GBP/USD returns to estimate
the SV model (with a minor modification). They employ extensions of the
Kalman filter and the smoother we discuss in the appendix. Exhibit 12.3
presents the plot of the GBP/USD absolute returns, as well as the filtered and
smoothed volatility estimates. The filtered estimates characteristically tend to
reflect volatility ‘‘bumps’’ with a delay compared to the smoothed estimates.
JUMP EXTENSION OF THE SIMPLE SV MODEL
In the previous chapter, we discussed in detail the Bayesian estimation of
models allowing for the unobserved volatility to transition through a number
of regimes. Similar Markov switching extensions are certainly possible to
incorporate within SV models as well. For example, So, Lam, and Li (1998)
and Casarin (2003) include a state-dependent parameter in the intercept of
the volatility dynamics process thus scaling up or down the unconditional
volatility of the return series.
Here we briefly outline a jump extension to the simple SV model.
Jumps could be incorporated either in the return dynamics (the observa-
tion equation) in (12.1) or in the volatility dynamics (the state transition
equation) in (12.2). The two have different implications for the return
behavior.
A jump in the return dynamics equation is completely transient in
nature. Its effect is dissipated momentarily and has no impact on the

242
BAYESIAN METHODS IN FINANCE
0
1
2
3
4
5
100
200
300
400
500
600
700
800
900
0
.5
1
1.5
Filtering
Smoothing
100
200
300
400
500
600
700
800
900
EXHIBIT 12.3
Filtered and smoothed volatility estimates in the multimove
algorithm setting
Source: Figure 7 in Kim, Shephard, and Chib (1998).
distribution of returns in the future. Chib, Nardari, and Shephard (2002)
consider such an extension to the simple SV model. The jump component is
integrated into the return process in the following way:
rt = jtqt + eht/2ϵt.
(12.19)
The variable qt takes a value of 1 if a jump occurs at time t and a
value of 0 if a jump does not occur. It is modeled as a Bernoulli-distributed
random variable. The probability of a jump, p ≡P (qt = 1), is, of course,
unknown, and estimated along with the remaining SV model parameters. It
has the meaning of the expectation of the number of jumps in a given period
of time.13 For instance, Andersen, Benzoni, and Lund (2002) estimate that,
for daily S&P return data, the average number of jumps per day is 0.0137,
corresponding to about 3 to 4 jumps per year (assuming 252 business days
in a year). The prior distribution of p is assumed to be a (conjugate) beta
distribution, with hyperparameters fixed to reflect our prior expectation
of p.
13The expectation of a Bernoulli random variable is equal to p.

Bayesian Estimation of Stochastic Volatility Models
243
The size of a jump is represented by jt in (12.19). Chib, Nardari, and
Shephard (2002) model the distribution of jt as
log (1 + jt) ∼N

−0.5δ2, δ2
.
(12.20)
A log-normal distribution is asserted for the parameter, δ.
Incorporating jumps in the volatility dynamics provide a mechanism
to reflect the (persistent) impact of a jump today on the future conditional
volatility. Eraker, Johannes, and Polson (2003) find that jumps in volatility
complement jumps in returns. When both are included in the model, jumps
in returns are less frequent and appear to explain crashlike movements of
the stock market. Moreover, it has been argued that the return-generating
process is modeled more effectively if the volatility jumps and the return
jumps are correlated.
VOLATILITY FORECASTING AND RETURN PREDICTION
Of interest in volatility modeling is, naturally, the model’s capacity to
produce meaningful predictions for the volatility and the return. The sim-
ulations of the volatility path, h, in both the single-move and multimove
simulation scenarios can be readily used for prediction.
Suppose there are a total of M draws of the augmented parameter
vector,

ρ0, ρ1, τ 2, h

. Then, for each period, t, we have available a sample,
h(m)
t , m = 1, . . . , M, from the (smoothed) distribution, p

ht | r, ρ0, ρ1, τ 2
,
of the unobserved volatilities.
Suppose that we would like to predict the volatility at time T + 1. For
each draw
	
ρ(m)
0 , ρ(m)
1 , τ 2(m), h(m)
, m = 1, . . . , M, we generate an observation
using the equation for the volatility dynamics in (12.2),
h(m)
T+1 = ρ(m)
0
+ ρ(m)
1 h(m)
T + τ (m)ηT,
where ηT ∼N (0, 1). Thus, we obtain a sample from the distribution
of predicted volatilities, p

hT+1 | hT, ρ0, ρ1, τ 2
. This is an out-of-sample
forecast, since both

ρ0, ρ1, τ 2
and hT are based on information available
up to time T only.
If we want to predict the return at time T + 1, we can obtain a sample
from the predictive return density by computing
r(m)
T+1 = exp
	
h(m)
T+1/2

ϵT,
for m = 1, . . . , M.

244
BAYESIAN METHODS IN FINANCE
SUMMARY
In this chapter, we discussed Bayesian estimation of the simple SV model.
Two alternative approaches to estimation have been employed in the
literature—a single-move sampling scheme and a multimove sampling
scheme. The first one relies on traditional MCMC techniques to simu-
late the unobserved volatilities component-by-component. The second one
uses the Kalman filter and smoother, state-space model estimation methods.
Recent research efforts have focused on extending and generalizing the
Kalman filter and smoothing algorithms to increase simulation efficiency.
APPENDIX: KALMAN FILTERING AND SMOOTHING
Consider the observation and transition equations of the SV model, given
respectively by (12.1) and (12.2). We want to obtain estimates of the
unobserved volatility, ht, t = 1, . . . , T, given the observed sample of return
data. At time t, one can distinguish between two types of volatility estimates:
1. A filtered volatility estimate at time t is obtained using only return data
observed up to and including time t. Denote the estimate by ht|t.
2. A smoothed volatility estimate at time t is based on information that
became available after time t. Denote it by ht|s, s > t.
The smoothed estimate has a smaller estimation error than the filtered
estimate, since a larger amount of information is used in computing it.
Now, we briefly review the basic filtering and smoothing algorithms in
the context of the SV model estimation.
The Kalman Filter Algorithm
The Kalman filter is a recursive procedure to obtain filtered estimates of
ht = log(σ 2
t ). When applied to a linear model with normal disturbances the
filter produces an optimal estimator (in the sense of having minimal mean
squared error14).
We use the notation established in our discussion on the multimove
algorithm. The Kalman filter process consists of two stages.
14The mean squared error (MSE) of an estimator, ˆθ, is the expected value of
the square of the error from the parameter, θ, E

(θ −θ)2
. The MSE can be
decomposed as
MSE = var
	
ˆθ

+
	
Bias
	
ˆθ


2
,

Bayesian Estimation of Stochastic Volatility Models
245
Prediction Stage
Based on the information available up to time t −1, the
log-volatility at time t is predicted and its variance computed, as follows:
ht | t−1 = ρ0 + ρ1ht−1 | t−1
pt | t−1 ≡var(ht | t−1) = ρ2
1pt−1 | t−1 + τ 2.
(12.21)
The variance of ht|t−1, pt|t−1, is conditional on rt and quantifies the
uncertainty associated with the prediction, ht|t−1.
Notice that we could use ht|t−1 to obtain a prediction for the transformed
return, r∗
t , in (12.15),
r∗
t = ht | t−1 + µλt−1,
(12.22)
where µλt−1 is the mean of the seven-component normal mixture in (12.16)
at time t −1. Since we actually observe the return at time t, we can compute
the prediction error and its variance, respectively, as
Et = r∗
t −ht | t−1 −µλt−1
Ot = pt | t−1 + v2
λt.
(12.23)
Both quantities, Et and Ot, serve to update the log-volatility prediction and
its variance in the updating stage below.
Updating Stage
The predictions made at time t −1 are updated with the
new information made available at time t to obtain the filtered log-volatility
estimate,
ht | t = ht | t−1 + Kt

r∗
t −ht | t−1 −µλt−1

.
(12.24)
The expression in (12.24) is based on the reasoning that the error made
in predicting the transformed return, r∗
t , provides an indication of the error
that might be made in estimating ht. The quantity Kt is called the ‘‘Kalman
gain’’ and is defined as
Kt = ρ1pt | t−1
Ot
.
(12.25)
The higher the variance of the predicted log-volatility, pt|t−1, relative to
the variance of the predicted transformed return error, Ot, the greater the
correction of ht|t−1 at the updating stage. The direction of the correction
depends on the sign of the prediction return error—overprediction of r∗
t at
where the bias of an estimator is the difference between its expected value and the
parameter value.

246
BAYESIAN METHODS IN FINANCE
time t −1 means that ht|t−1 is likely lower than the unobserved ht; therefore,
at time t, ht|t−1 is updated upward, and vice versa.
The updated variance of ht|t is given by
pt | t = pt | t−1 −Ktρ1pt | t−1.
(12.26)
To summarize, for each time step, t = 1, . . . , T, we compute the
quantities in (12.21), (12.25), (12.24), and (12.26) and obtain the series of
filtered log-volatilities, ht|t.
The Smoothing Algorithm
The smoothing algorithm builds on the filtering one and produces smoothed
estimates of the unobserved volatility with smaller variance than the filtered
estimates. The basic smoothing procedure is very similar to the filtering one,
only going in the opposite direction in time, backward. To obtain ht|T, we
compute the following recursive estimates, for t = T −1, . . . , 1,
Dt = ρ1pt | t
pt+1 | t
pt | T = pt | t + D2
t

pt+1 | T −pt+1 | t

ht | T = ht | t + Dt

ht+1 | T −ht+1 | t

.
The initial values of the recursion, pT|T and hT|T, are the filtered estimates
computed using (12.26) and (12.24), respectively.
In the context of SV models, Kim, Shephard and Chib (1998) and Chib,
Nardari, and Shephard (2002), among others, apply extensions of the basic
smoothing algorithm to improve computational efficiency. See De Jong and
Shephard (1995), Koopman (1993), and Durbin and Koopman (2002) for
more details on these smoother extensions.
SsfPack is a free-of-charge software for state-space models estimation
using the Kalman filter. Koopman, Shephard, and Doornik (1999) provide
documentation for using that software.

CHAPTER13
Advanced Techniques for
Bayesian Portfolio Selection
O
n October 19, 1987, the value of the Dow Jones Industrial Average
plummeted by 22%, while the value of the S&P 500 index dropped by
20%. In the history of financial markets that day is referred to as ‘‘Black
Monday.’’ A daily change of that order of magnitude is a nearly impossi-
ble event if one assumes that stock returns are normally distributed. The
frequency of returns exceeding three standard deviations from the mean
is greater than the normal distribution suggests. Moreover, positive and
negative returns do not occur with comparable frequency. These character-
istics of asset returns—heavy-tailedness and asymmetry, respectively—are
well-recognized by academic researchers and making their ways through to
quantitative models employed for practical portfolio construction and risk
management.1
The lack of normality in returns implies that the concept of risk has
a richer content than the standard deviation (the traditionally employed
risk measure) can reflect. The risk of appreciation of the value of one’s
investment is certainly welcome, while any rational investor attempts
to avoid taking or seeks to minimize the risk of losses. The standard
deviation
fails
to
account
for
this
sort
of
asymmetric
investor
preference.
Similarly, the covariance matrix does not necessarily contain all infor-
mation about dependencies across asset returns. To evaluate portfolio risk,
one needs to account, for example, for the stronger dependence across
1Some of the first academic papers focusing on the heavy-tailed characteristics
of returns were published in the 1960s. Among them were Mandelbrot (1963)
and Fama (1965). Some risk analytics providers who incorporate heavy-tailed
return features in their risk-management platforms are FinAnalytica and Advanced
Portfolio Technologies (APT).
247


## MCMC Methods

248
BAYESIAN METHODS IN FINANCE
returns when the market is down than when it is up and for the tendency of
extreme returns to occur simultaneously.
The portfolio paradigm set forth by Markowitz (1952) of minimizing
portfolio risk through assessing the contribution to risk of individual secu-
rities is as insightful today as it was more than half a century ago. However,
the definition of risk has undergone changes and, accordingly, has led to
a modification of the portfolio construction problem. Recent research has
shown that portfolios derived within the classical mean-variance framework
might come short of optimality since failing to recognize the components of
risk related to the nonnormality of returns.2
In this chapter, we present a general setting for portfolio selection in the
presence of atypical (relative to the classical framework) statistical properties
of stock returns.3 Both the frequentist and the Bayesian approaches can be
employed for model estimation. However, since in the absence of normality
analytical results may not be readily available, the Bayesian framework does
offer purely practical advantages (apart from the ones already discussed in
Chapter 6). In the first part of the chapter, we discuss one way to incorporate
higher moments into portfolio selection based on utility maximization. In
the second part, we present an extension of the Black-Litterman model
that, in particular, employs minimization of a risk measure superior to the
standard deviation (in the nonnormal setting).
We start with a brief overview of some distributional alternatives to
normality.
DISTRIBUTIONAL RETURN ASSUMPTIONS ALTERNATIVE
TO NORMALITY
A desirable characteristic of the return distribution is that it is flexible enough
to accommodate varying degrees of tail thickness and asymmetry. The degree
of tail thickness (kurtosis) is considered relative to the tail thickness of the
normal distribution, whose kurtosis has a value of 3. A distribution with
a value for kurtosis that exceeds 3 is considered heavy-tailed (leptokurtic),
whereas kurtosis less than 3 indicates tails thinner than the normal ones (the
distribution is then called platykurtic). The symmetry of a distribution could
2See Rachev, Ortobelli, and Schwartz (2004), Ortobelli, Rachev, Stoyanov, Fabozzi,
and Biglova (2005), and Bertocchi, Giacometti, Ortobelli, and Rachev (2005).
3The empirical features of returns, such as heavy-tailedness, asymmetry, volatility
clustering, and so on are not unique to stock returns, although we focus on
them in our discussion. Instead, they are characteristic of the weekly, daily, and
higher-frequency returns in most major asset classes.

Advanced Techniques for Bayesian Portfolio Selection
249
be captured by various parameters and their particular definition determines
the way asymmetry is measured.
Some groups of distributions that have been proposed to deal with
heavy-tailedness and asymmetry are:
■Mixtures of normal distributions.
■Student’s t-distributions (multiple versions and representations exist).
■Stable (non-Gaussian) distributions.
■Extreme value distributions.
■Other distributions, such as skew-normal and generalized hyperbolic.
Below we review some representatives of each of these groups.
Mixtures of Normal Distributions
Amixtureofnormaldistributions(‘‘mixtureofnormals’’)isobtainedbyvary-
ing the variance (and/or mean) of a normally distributed random variable. For
example, suppose that the variance of a normally distributed random vari-
able is σ 2
1 with probability π and σ 2
2 with probability 1 −π. The resulting
normal distribution is a discrete scale mixture of normal distributions,
X ∼



N

µ, σ 2
1

,
with probability π
N

µ, σ 2
2

,
with probability 1 −π.
(13.1)
The density of X is then given by
f

x | µ, σ 2
1 , σ 2
2

= πfN

µ, σ 2
1

+ (1 −π)fN

µ, σ 2
2

,
(13.2)
where fN

µ, σ 2
denotes the normal density with mean µ and variance σ 2.
Continuous mixtures of normals are usually employed to model asset
returns. The variation of the normal parameter(s) is introduced in two
ways. It is either governed by the realizations of a (unobservable) mixing
continuous variable or some stochastic process is assumed for the dynamics
of the normal mean/variance. When only the normal variance is varied, the
resulting distribution is called a scale mixture of normals, whereas when
both the mean and the variance are varied, the result is a location-scale
mixture of normals.
We have come across mixtures of normals several times in the previous
chapters. For example, as explained in Chapter 10, the distribution of the
asset return in the simple GARCH and SV models is a mixture of normals,
when the return disturbances are normal. Furthermore, in Chapter 11

250
BAYESIAN METHODS IN FINANCE
we discussed that some heavy-tailed distributions can be represented as
mean-scale mixtures of normals and we used that representation of the
Student’s t-distribution for facilitating the Markov Chain Monte Carlo
simulation algorithm.
In general, an appropriately chosen (discrete) mixture of normals could
provide an adequate approximation to most distributions. In Chapter 12,
for example, we discussed that Kim, Shephard, and Chib (1998) use a
seven-component mixture of normals to approximate a chi-square (χ 2)
random variable in their treatment of the SV model.
Asymmetric Student’s t-Distributions
The popularity of the Student’s t-distribution as a heavy-tailed alternative to
the normal distribution has led to the development of asymmetric versions
of it.4 Here we outline the Fernandez and Steel (1998)’s version.
Suppose that a random variable, X, has a symmetric (around zero)
Student’s t-distribution. Denote the Student’s t-density function by t(x).
Then, by introducing a parameter, γ , γ > 0, we can transform t(x) into an
asymmetric Student’s t density in the following way:5
t(x|γ ) =



2
γ + 1
γ t
 x
γ

if X ≥0
2
γ + 1
γ t(xγ )
if X < 0.
(13.4)
The parameter γ determines the probability mass on each side of the
mode (equal to 0) and, therefore, the degree of skewness. The symmetric
case corresponds to γ = 1.
4Asymmetric Student’s t models have been proposed by Jones and Faddy (2003),
Fernandez and Steel (1998), Hansen (1994), Azzalini and Capitanio (2003), and
Rachev and R¨uschendorf (1994) (in the framework of general subordinated (mixing)
model), among others. See also Demarta and McNeil (2004) and Rachev, Mittnik,
Fabozzi, Foccardi, and Jasi′c (2007) for the location-scale mixture of normals
representation of the multivariate skew Student’s t-distribution (a particular case of
the generalized hyperbolic distribution, in which the mixing variable has the inverse
Gaussian distribution).
5This density can be expressed in a more compact way using an indicator function:
t(x|γ ) =
2
γ + 1
γ

t
 x
γ
	
I{X≥0} + t(xγ )I{X<0}

,
(13.3)
where IX≥0 is 1 if X ≥0 and 0 if X < 0.

Advanced Techniques for Bayesian Portfolio Selection
251
The method above can be used to introduce skewness to any symmetric
density.
Stable Distributions
Stable distributions are a class of distributions with very flexible features,
which nests as a special case the normal (Gaussian) distribution.6 The
criticism of stable distributions that has prevented them from becoming
a mainstream distributional choice is the lack of a closed-form density
function (with the exception of the three special cases mentioned below).
While this criticism was valid at one time, the advances in computer power
make their application increasingly accessible today.
The stable distribution of a random variable, X, is defined through its
characteristic function, ϕ(t).7
log (ϕ(t)) =



−σ α|t|α 
1 −iβsign(t) tan πα
2

+ iµt,
for α ̸= 1
−σ|t|

1 −iβsign(t) log (t)

+ iµt,
for α = 1
.
(13.6)
The stable distribution above is denoted by Sα(β, σ, µ) and its four
parameters are defined as follows:
1. α = index of stability or tail parameter. Regulates the thickness of the
tails and takes values between 0 and 2; the lower α is, the heavier the
tails of the distribution.
2. β = skewness parameter. Regulates the degree of asymmetry and takes
values between −1 and 1; the symmetric case is obtained for β = 0.
3. σ = scale parameter.
4. µ = location parameter.
The density function of the stable distribution is available in closed
form in only three special cases. These are
6Stable distributions (both Gaussian and non-Gaussian) possess the property of
stability (sums of stable random variables are themselves stable), which is clearly
appropriate for modeling returns. Moreover, a version of the Central Limit Theorem
governs the asymptotic behavior of sums of stable random variables. Therefore, the
financial modeling framework built around the normal distribution can be extended
to the more general class of stable distributions.
7The characteristic function of a random variable, X, with density f(x) is defined as
ϕ(t) = E

eitX
=

eitX f(x) dx.
(13.5)

252
BAYESIAN METHODS IN FINANCE
1. The Gaussian distribution, N(µ, τ 2), for which α = 2, β = 0, and
τ =
√
2σ 2.
2. The Cauchy distribution for which α = 1 and β = 0.
3. The completely skewed to the left (right) L´evy distribution for which
α = 1/2, β = −1 (α = 1/2 and β = 1).
The symmetric stable distribution (Sα(0, σ, µ)) can be represented as a
mixture of normals. In the next chapter, we employ the asymmetric stable
distribution in the Bayesian estimation of a multifactor model.
Extreme Value Distributions
Extreme value distributions are used to model the far tails of a distribution,
i.e., extreme values (minima or maxima) of large sets of independent identi-
cally distributed (i.i.d.) random variables.8 Suppose that a random variable,
X, has a distribution function F(x). Depending on the behavior of F(x) for
very large values of X (the far right tail of the distribution), three types of
extreme value distributions can be defined for the greatest value of X (the
distribution of the least value can be obtained by replacing X with −X):
Type 1. F(x) behaves approximately like a normal distribution in the
tails (the tails decay exponentially fast),
F(x) = exp (−e−x−η
θ ).
(13.7)
Type 2. F(x) behaves approximately like a Student’s t- or Cauchy
distribution in the tails (the tails decay at the rate of a polynomial),
F(x) =

0
for x < η,
exp (−
 x−η
θ
−k)
for x ≥η.
(13.8)
Type 3. F(x)’s right tail is bounded, that is, the range of X is restricted
from above,
F(x) =

exp

−
 η−x
θ
k
for x ≤η
0
for x > η,
(13.9)
where η, θ, and k are parameters, θ > 0 and η > 0.
8In fact, the extreme value distributions are the limiting distributions (as N →∞) of
the extreme value among N i.i.d. random variables.

Advanced Techniques for Bayesian Portfolio Selection
253
Skew-Normal Distributions
A number of researchers have extended the normal distribution by intro-
ducing skewness to it.9 Sahu, Dey, and Branco (2003) define a skew-normal
random variable, R, as the sum of two normal random variables, one of
them restricted to be positive:
R = X + δZ,
(13.10)
where: X = normal random variable with mean µ and variance σ 2,
X ∼N(µ, σ 2).
Z = standard normal random variable, restricted to take positive
values only, Z ∼N(0, 1)I{Z>0}; that is, its pdf is given by
f(Z) =
2
√
2πσ 2 exp

−Z2
2σ 2
	
I{Z⟩0}.
δ = skewness parameter, which can take any real value; δ = 0
corresponds to the symmetric case and retrieves the original
normal distribution.
Harvey, Liechty, Liechty, and M¨uller (HLLM) (2004) employ the
multivariate skew-normal distribution in their investigation of portfolio
selection with higher moments. The definition above is generalized to the
multivariate case in the following way. Denote by Rt the vector of returns
on the N stocks in a portfolio at time t. Then, assuming that stock returns
follow a skew-normal distribution, we write
Rt = X + Z,
(13.11)
where the N × 1 vector X is distributed as N (µ, ) and the N × 1 vector
Z is distributed as N (0, IN) with density given by
f(Z) =
 2
π
	N/2
||−1/2 exp

−1
2Z′Z
	
N

j=1
I{Zj>0}.
9See Azzalini and Dalla Valle (1996) and Azzalini and Capitanio (1999) for the
original discussions of the skew-normal distribution (skew-elliptical distributions in
general). Various extensions have been offered by Sahu, Dey, and Branco (2003),
Branco and Dey (2001), and Adcock and Schutes (2005), among others.

254
BAYESIAN METHODS IN FINANCE
The diagonal and off-diagonal elements of the (N × N) matrix  in
(13.11) indicate the degree of skewness in the returns of the individual stocks
and coskewness of stocks, respectively. Coskewness is discussed below.10
We denote the skew-normal distribution above as SN(µ, , ).
The Joint Modeling of Returns
At the end of our overview of some heavy-tailed distributions, we briefly
discuss the two conceptual paths extending the univariate modeling setting
to a multivariate one. The first option is to consider the realized returns
in each time period as the realization from a multivariate distribution. An
alternative is to model the return on each asset separately, as following some
univariate distribution, and then impose a dependence structure on returns
using the copula framework.
Traditionally, multivariate distributions extend the univariate concepts
to the class of the so-called ‘‘elliptical distributions’’ suitable to describe
symmetric, unimodal multivariate relationships.11 The most well-known
representatives of the class of elliptical distributions are the multivariate
normal distribution and the multivariate Student’s t-distribution.
Multivariate theory, as applied to risk management, has concentrated
primarily on elliptical distributions because of their analytical tractabil-
ity. Moreover, in the elliptical case, the joint distribution of returns is
determined uniquely by the marginal (univariate) distributions and their
correlation matrix, so extending univariate modeling to the multivariate
case is accomplished in a single step. The definition of elliptical distribu-
tions, however, imposes the restriction of symmetry and efforts have been
devoted to developing asymmetric extensions.
Multivariate relationships could also be modeled through the use
of copulas. The empirical evidence indicates that sometimes the normal
10In the skew-normal distribution formulated by Sahu, Dey, and Branco (2003), 
is diagonal; that is, its off-diagonal elements are zero, thus ignoring coskewness.
11The density function of an N-dimensional random variable, X, belonging to the
class of elliptical distributions has the form
f(x, η, ) = C||−1/2g

(x −η)′−1(x −η)

,
where η is a location parameter,  is a scale matrix, C is a normalizing constant, and g
is a generator function which determines the particular distribution of X (in particular,
the heaviness of its tails). For example, the generator function is g(x) = exp(−x/2)
in the case of the normal distribution. See Lamantia, Ortobelli, and Rachev, (2006a)
and Lamantia, Ortobelli, and Rachev (2006b) for discussions of some applications
of elliptical and nonelliptical distributions to investment management.

Advanced Techniques for Bayesian Portfolio Selection
255
distribution might describe adequately the behavior of a single asset’s
returns. However, when two or more assets are jointly modeled, their
relationship is not described well by a multivariate (elliptical) normal
distribution—there is, for example, a tendency for assets to exhibit coskew-
ness and cokurtosis (concepts explained later in the chapter). The complexity
of the dependence structure between stocks requires tools/measures other
than the covariance to describe it. The use of copulas allows one to assert
any assumptions for the univariate (marginal) distributions of stocks and
then superimpose a dependence structure taking into account the empiri-
cal features of the multivariate data. Copulas are simply functions linking
the univariate distributions with the multivariate one. (We briefly describe
copulas in Appendix C.) Intensive research effort is underway to develop
estimation methods (in the nonelliptical setting) able to handle dimensions
(numbers of securities) of the order encountered in practice. Later in the
chapter, we consider an extension of the Black-Litterman framework, which
employs a copula to model the dependence between returns.
The two approaches for multivariate modeling are not in conflict. In
fact, it can be shown that any multivariate distribution with continuous
marginal distributions has a unique copula representation.
PORTFOLIO SELECTION IN THE SETTING OF
NONNORMALITY: PRELIMINARIES
In Chapter 6, we discussed that there are three ways to select the optimal
portfolio in the mean-variance setting. The corresponding portfolio opti-
mization problems (accompanied by constraints on portfolio weights) are:
■Minimize portfolio’s risk, ω′ω, for a given minimal (required) return.
■Maximize portfolio’s expected return, ω′E(R), for a given maximal risk.
■Maximize investor’s expected utility function, generally taken to be a
quadratic utility function of the type E

U(ω)

= ω′E(R) −λω′ω,
where we employ our usual notation:
ω = vector of portfolio weights.
E(R) = vector of expected returns.
 = covariance matrix of returns.
λ = risk aversion parameter.
These three representations of the portfolio problem are equivalent and
lead to the same mean-variance efficient frontier.12 The efficient frontier is
12See Rockafellar and Uryasev (2002) and Rachev, Ortobelli, and Schwartz (2004).

256
BAYESIAN METHODS IN FINANCE
obtained by computing the optimal portfolios for varying required return,
varying maximal risk, and varying risk-aversion parameter, respectively, in
the three cases above.
The choice of modeling returns with a distribution other than the
normal implies that the traditional definition of risk, the standard deviation
of returns, must be foregone. In general, rational investors perceive as
undesired the possibility of a downside occurrence in returns, unlike the
potential for a return appreciation of equal size. Consequently, investors
would like to minimize the risk from an investment but not necessarily
restrict all of the uncertainty associated with its outcome. We say that they
have a preference for positive skewness and a dislike for negative skewness.
This observation sets the stage for a discussion on the choice of the most
appropriate measure of risk.
For example, Markowitz suggested the use of the semistandard devi-
ation as a measure of risk in order to capture the intrinsic preference for
‘‘good’’ volatility (Markowitz, 1959).13 While we discuss some risk mea-
sures employed in portfolio risk management in Appendix A of this chapter,
here we only note that in the setting of nonnormality, the optimal portfolio
is obtained by modifying the problems above in either of the following
ways:
■Maximize a utility function that includes higher moments in order to
capture the richness of investors’ risk preferences.
■Minimize directly an appropriate risk measure.
Next, we discuss the first approach to portfolio selection in which we
follow HLLM (2004).
MAXIMIZATION OF UTILITY WITH HIGHER MOMENTS
As discussed earlier, properties of the return distribution other than the mean
and the variance (the first two statistical moments) might be important to
13The semistandard deviation measures only the downside potential of returns and
is defined as



 1
T
n

t=1
min{0, rt −µ}2,
where rt is the asset return at time t, µ is the expected return, and T is the number
of return observations.

Advanced Techniques for Bayesian Portfolio Selection
257
describe better the behavior of returns and, consequently, the risks that
investors assume by investing in stocks. Of interest in portfolio construction
are not only the higher moments of individual stock returns, but the
dependence between higher return moments across stocks, especially the
dependence between the third moments, the coskewness.
Coskewness
Coskewness describes the tendency of stocks to have same-sign returns
(either positive or negative). The coskewness between the returns on assets
i and j is defined as
γi,j = E

(Ri −µi)

Rj −µj
2
.
(13.12)
Clearly, this measure is one-sided (not symmetric). It can be symmetrized
as follows:14
γi,j = E

(Ri −µi)

Rj −µj
2
+ E

Rj −µj

(Ri −µi)2
.
(13.13)
As we can see, a stock with a positive coskewness is a desirable addition to
a portfolio because it reduces the portfolio’s likelihood of extreme negative
outcomes.15
14Alternatively, coskewness can be defined as
γi,j = max

E

(Ri −µi)

Rj −µj
2
, E

Rj −µj

(Ri −µi)2
.
15By analogy with the beta of a stock (reflecting the systematic variation component
of a stock’s return), we can define systematic skewness as
γi,M =
E

(Ri −µi) (RM −µM)2

var(Ri)var(RM)
,
where RM and µM are the market return and expected return, respectively. Harvey
and Siddique (2000) replace Ri −µi by ϵi, the residual from a regression of stock
i’s returns on the contemporaneous market return, and var(Ri) by E(ϵ2
i ) in their
extension of the CAPM.
A number of researchers consider the implications of coskewness for asset pricing.
Assets with negative coskewness must have higher expected returns, equivalently
lower prices, than identical assets with positive coskewness in order to be attractive

258
BAYESIAN METHODS IN FINANCE
By analogy with the covariance matrix, we can define the skewness
matrix, S, for the returns on N stocks as the symmetric matrix
S =


γ1,1 γ1,2 ···
γ1,N
. . . . . . . . . . . . . . . . . . .
γN,1 γN,2 ···
γN,N

,
(13.14)
where γ i,i is the skewness of the return on stock i and γ i,j is the coskewness
of the returns on stocks i and j as defined in (13.13).
Utility with Higher Moments
Consider a portfolio made up of N stocks with a portfolio weight vector ω
and skewness matrix, S. The portfolio skewness is defined as
Sp = ω′Sω ⊗ω,
(13.15)
where ⊗denotes the Kronecker product.
To incorporate investors’ preferences for (positive) skewness in the
portfolio problem, we modify the expression for the expected quadratic
utility in (6.4) in Chapter 6 as follows:
E

U(ω′RT+1)

= µp −λσ 2
p + γ Sp,
(13.16)
where the portfolio mean and variance, µp and σ 2
p , are as defined in
Chapter 6, λ is the ‘‘classical’’ risk aversion parameter, and RT+1 is the
vector of next-period returns. The parameter γ measures the investor’s
propensity for skewness.
Recall from our discussion in Chapter 6 that simply plugging in the sam-
ple estimates of µp, σ 2
p , and Sp into the utility function above and maximizing
it results in suboptimal solutions. Instead, portfolio optimization within the
Bayesian framework recognizes and takes into account the uncertainty about
the estimates of the three distributional moments. The ‘‘right ingredients’’
when maximizing the expected utility function in (13.16) are the moments
of the future returns’ distribution—the predictive expected returns, the
predictive covariance, and the predictive (co)skewness of returns.
to investors. Cokurtosis, interpreted as the common sensitivity of returns to extreme
movements, has also been considered. See Rubinstein (1973), Kraus and Litzenberger
(1976), Barone-Adesi (1985), Dittmar (2002), and Ang, Chen, and Xing (2006)
among others.

Advanced Techniques for Bayesian Portfolio Selection
259
Distributional Assumptions and Moments
Denote by R the returns on the N stocks candidates for the optimal port-
folio observed for T periods. Assume that returns follow the skew-normal
distribution in (13.11). Then, R is a (T × N) matrix. Each row of R,
Rt =

R1, t, . . . , RN, t
′, t = 1, . . . , T, is an i.i.d. realization of SN(µ, , ).
The parameters of the skew-normal distribution, µ, , and  are not
the mean, the covariance matrix, and the skewness matrix of R. In fact,
once we depart from the normality assumption, the distribution parameters
rarely carry the interpretation of the statistical moments.16
HLLM provide the mean, covariance, and skewness of the multivariate
skew-normal distribution as functions of the parameters of the skew-normal
distribution, respectively,
m (µ, ) = µ +
 2
π
	1/2
1
(13.17)
V (, ) =  +

1 −2
π
	
′
(13.18)
S (µ, , , Z) = E3 [Z] ′ ⊗′ + 3µ′ ⊗

′

1 −2
π
	
+ 2
π 1 (1)′

+ 3
 2
π
	1/2
(1)′ ⊗

 + µµ′
 
+ 3µ′ ⊗
+ µµ′ ⊗µ′ −3µ′ ⊗V −mm′ ⊗m′,
(13.19)
where 1 is a compatible vector of ones and E3 [Z] is the (N × N2) matrix of
third moments of Z.17
Likelihood, Prior Assumptions, and Posterior
Distributions
The unconditional (with respect to Z) likelihood for the model parameters
does not have a closed form because of the presence of the unobserved mixing
variable Z. The unconditional likelihood is given by the N-dimensional
16See Chapter 13 of Rachev, Menn, and Fabozzi (2005) for a general description of
portfolio optimization with constraints on the skewness and kurtosis.
17Let Z be a zero-mean N × 1 vector. The matrix of third moments of Z is defined
as the N × N2 matrix, E

Z′ ⊗ZZ′
.

260
BAYESIAN METHODS IN FINANCE
integral,
L (µ, ,  | Rt) ∝||−T/2
 ∞
0
exp

−1
2
T

t=1
(Rt −µ −Zt)′−1
× (Rt −µ −Zt)
	
exp

−1
2Z′
tZt
	
dZt,
(13.20)
where Zt is an (N × 1) vector, the realization of the unobserved, mixing
variable, Z, at time t. We estimate the three model parameters, µ, , and
, within the Bayesian framework and, in addition, simulate Z, along
with them. By simulating Z, we avoid performing the multidimensional
integration in (13.20).
The likelihood, conditional on Z, is a multivariate normal likelihood.
Then, evoking the property of conjugacy, we employ a normal and an
inverted Wishart prior distributions and obtain posterior distributions of
the same distributional forms. To reflect lack of particular prior intuition
about the returns’ means, skewness, and covariance, and uncertainty about
the prior parameters, HLLM assert,
µ ∼N (0, 100IN)
(13.21)
vec() ∼N (0, 100IN2)
(13.22)
 ∼IW (NIN, N) ,
(13.23)
where IW denotes the inverted Wishart distribution (see the appendix to
Chapter 3 for its definition), In denotes the n × n identity matrix, and vec is
an operator which stacks the columns of a matrix into a column vector, so
that vec() is a N2 × 1 vector. For convenience, we combine µ and vec()
into a single vector and define the (N + N2) × 1 vector
η =

µ
vec()
	
,
(13.24)
with prior distribution N (0, 100IN+N2).
HLLM (2004) provide the posterior distributions for η and , which
are easy to obtain with some straightforward (but tedious) multivariate
algebra,
η | R, , Z ∼N

E−1e, E−1
 | R, µ, , Z ∼IW (, N + T) ,
(13.25)

Advanced Techniques for Bayesian Portfolio Selection
261
where: E = E = !T
t=1 s′
t−1st +
1
100IN+N2.
e = e = !T
t=1 s′
t−1Rt.
 =  = !T
t=1 (Rt −µ −Zt) (Rt −µ −Zi)′ + NIN.
st = [IN, Zt
′ ⊗IN].
The conditional distribution of the latent variable, Z, is given by
Zt | R, µ, ,  ∼N

A−1a, A−1
I{Zit>0},
(13.26)
for i = 1, . . . , N and t = 1, . . . , T, where
A = IN + ′−1
a =
T

t=1
′−1(Rt −µ).
Notice that the posterior distribution of η in (13.25) is the full con-
ditional distribution and thus depends on . (We came across a similar
situation in Chapter 5, in our discussion of the semiconjugate linear regres-
sion model.) Therefore, direct sampling from the posteriors is not possible.
Instead, employing the Gibbs sampler is straightforward.
Sampling from the Conditional Distribution of Z
Sampling Z as a vector from
its normal conditional distribution is inefficient because the distribution
is truncated at zero. Within the Gibbs sampler one would need to sample
repeatedly from the normal distribution, N

A−1a, A−1
, and reject the draw
each time one of the N components is negative or zero. The rejection rate
of such an algorithm will be high in multidimensional settings.
An alternative sampling approach is to draw Z component by compo-
nent. The full conditional distribution of each component, z, of Z is given
by N (µz, Vz) Iz>0, where µz and Vz are the corresponding elements of Z’s
posterior mean and covariance. This (univariate) normal density is sampled
repeatedly until a nonnegative value for z is obtained.18
18HLLM (2004) employ the so-called ‘‘slice sampler’’ to sample from the distribution
of z. This algorithm has a zero-rejection rate and is clearly advantageous when
sampling efficiency is crucial. See also Damien, Wakefield, and Walker (1999) for
the general methodology and examples of using the slice sampler.

262
BAYESIAN METHODS IN FINANCE
Posterior Moments
To obtain samples from the posterior distributions of η
and , and the conditional distribution of Z, we employ the Gibbs sampler.
As explained in Chapter 5, samples from the posterior distributions of any
functions of η, , and Z are obtained by evaluating the functions at all
posterior draws. In particular, we compute the posterior distributions of
the mean, covariance, and skewness of the skew-normal distributions as
follows:
m(j) = m

µ(j), (j)
V(j) = V

(j), (j)
S(j) = S

µ(j), (j), (j), Z(j)
,
where the subscript, j, denotes the jth posterior draw of the respective
parameter, and µ(j) and (j) are the respective components of η(j).
Predictive Moments and Portfolio Selection
The predictive mean, covariance matrix, and skewness for next-period
returns, as given in HLLM, are
"m = E [m | R]
"V = E [V | R] + cov [m | R]
(13.27)
"S = E [S | R] + 3E [V ⊗m | R] −3E [V | R] ⊗"m
(13.28)
−E [(m −"m)′(m −"m) ⊗(m −"m) | R] ,
(13.29)
where E [· | R] denotes the posterior mean and cov [· | R] denotes the
posterior covariance matrix, computed numerically, as the posterior sample
estimates.
We use the predictive moments to compute the portfolio expected
return, variance, and skewness. Maximization of the expected utility in
(13.16) can then be performed numerically using an optimization soft-
ware.19
19State-of-the-art algorithms, called evolutionary algorithms, have been and are
being developed for optimization in multidimensional problems, where there
are likely many local optima. We just mention two major groups of these
algorithms—genetic algorithms and Bayesian optimization algorithms—and refer
the interested reader to Goldberg (1989) for the former and Pelikan (2005) for the
latter.

Advanced Techniques for Bayesian Portfolio Selection
263
Optimal Allocations
Expected
Utility
GE
Lucent
Cisco
0
g
0.123
0.9e-3
0.1e-3
0.5e-3
0.99
0
0.5
0.109
0.405
0.409
0.186
0
0.5
−1.745
0.784
0.125
0.054
0.037
0.5
0.5
−1.731
0.785
0.129
0.065
0.021
0
0
Sun
l
EXHIBIT 13.1
Expected utility maximization and optimal allocations
Source: Adapted from Tables 4 and 6 in Harvey, Liechty, Liechty, and M¨uller
(2004).
Illustration: HLLM’s Approach
HLLM consider the daily returns on four stocks, General Electric (GE),
Lucent Technologies (Lucent), Cisco Systems (Cisco), and Sun Microsystems
(Sun) for the period from April 1996 to March 2002. Exhibit 13.1 presents
their expected utility and optimal allocation results for different values of
the risk aversion parameter, λ, and the propensity to skewness parameter, γ .
Next, we present an extension of the Black-Litterman (BL) approach,
developed by Meucci (2006a), which takes into account the nonnormality
of asset returns and employs a flexible approach to combining market infor-
mation and portfolio manager’s intuition. Admittedly, Meucci’s framework
cannot be categorized strictly as a Bayesian one. However, it does fit the
Bayesian paradigm conceptually, since it provides the setting for pooling
together information originating from different sources.
EXTENDING THE BLACK-LITTERMAN APPROACH:
COPULA OPINION POOLING
The principal advantage of Meucci’s approach is that it allows a portfolio
manager to express subjective views on quantities he is intimately familiar
with, such as term spreads, implied volatilities, risk factors, prices, and
returns—in general, sources of randomness in the market—instead of
on the distribution parameters. The distribution parameters rarely have
intuitive interpretations, once the normality assumption is replaced, as we
mentioned earlier in this chapter.

264
BAYESIAN METHODS IN FINANCE
Meucci emphasizes that the extended framework is amenable to non-
normality assumptions for the distribution of the sources of randomness. Of
course, the BL model could also be modified to account for nonnormality.
Any resulting lack of analytical tractability can be handled with the MCMC
methods.
One aspect of Meucci’s model facilitates greatly its application in
practice—the straightforward way of expressing (and incorporating) view
confidence. Recall that in the original BL framework the view confidence is
quantified by the corresponding diagonal element of , the view covariance
matrix. There is no agreement, however, as to the most appropriate way of
translating view confidence into view variance. (We presented a backtesting
procedure to do that in Chapter 8.) Meucci’s approach combines the
subjective and objective (market-implied) distributions of each view by
simply taking their weighted average; the weight is the view confidence.
Finally, Meucci’s extension of the BL model boasts a feature providing
additional modeling flexibility: The dependence between views is specified
by means of a copula function.
We review Meucci’s framework next. For the source of randomness in
the market we use stock returns, although, as mentioned already, a different
market random quantity could be employed.
Market-Implied and Subjective Information
Suppose that return data are available on N stocks for T periods; denote
the (T × N) data matrix by R. We assume that each row of R, Rt, is a
realization from a certain multivariate distribution. In the BL model, this
distribution is multivariate normal with mean, µ, and covariance matrix .
To reflect the evidence for nonnormality in R, Meucci (2006a) assumes that
returns follow a multivariate asymmetric Student’s t-distribution.20
As in the BL model, one might want to use market equilibrium as
a center of gravity. Reflecting this equilibrium market information in the
distribution parameters is not always straightforward in a nonnormal
setting. The reasons for that are practical and conceptual. In the BL model,
µ has the interpretation of the vector of expected returns. Its distribution is
then naturally centered on the equilibrium risk premiums, . (See (8.4) in
Chapter 8.) The location parameter in an asymmetric Student’s t-distribution
(or any other heavy-tailed distribution), however, is generally not the mean
(unless the skew parameter is zero). Instead, the mean is a function of a few
20Meucci uses the multivariate asymmetric Student’s t version of Azzalini and
Capitanio (2003) and Azzalini (2005).

Advanced Techniques for Bayesian Portfolio Selection
265
model parameters. It is then not immediately clear how to specify a prior
reflecting the equilibrium information.
The conceptual difficulty originates from the fact that the CAPM
model used to derive the equilibrium risk premiums in the BL framework
assumes that returns are elliptically distributed. This contradicts the moti-
vation for asserting an asymmetric, heavy-tailed distribution for returns
and makes the expression defining  in (8.2) in Chapter 8 inappropriate
to use.
Meucci’s framework is general enough and does not require that equi-
librium arguments be employed.
Views and View Distributions
Suppose that a portfolio manager expresses K views on expected returns.
The views are collected in the K × N view matrix, P, as in Chapter 8. Recall
that a row in P represents a view portfolio—a linear combination of the
assets involved in the particular view.
Using the observed returns in R, we could obtain the returns on the
view portfolios that would have been realized if the view portfolios were
held during the T periods of the sample. That is, the market-implied view
returns are given by the T × K matrix, W,
W = R P′.
(13.30)
From a statistical and financial point of view, the collection of market-
implied returns in W can be analyzed row-wise and column-wise. Tradi-
tionally, W is analyzed row-wise: each row, W t, t = 1, . . . , T, represents the
market-implied returns on the K views in period t. In the BL framework,
W t has a multivariate normal distribution.
Alternatively, one can consider the columns of W. The kth column, W k,
is interpreted as a sample of market-implied returns from the kth view’s
marginal distribution.21
Most multivariate distributions that would be used to describe the
joint behavior of returns have marginal distributions of the same form. For
example, the multivariate normal and asymmetric Student’s t-distributions
have, respectively, normal and asymmetric Student’s t-margins. Therefore,
the marginal view distribution is uniquely identified.22
21This dichotomy reflects the two approaches to the joint modeling of returns on
multiple assets we mentioned earlier in the chapter.
22Meucci (2006b) extends the framework by considering a nonparametric, numerical
approach. In it, there is no need to assume specific forms for the multivariate, nor
marginal distributions.

266
BAYESIAN METHODS IN FINANCE
Let us denote the market-implied distribution of the returns on the kth
view by
π R
Wk.
(13.31)
Portfolio managers’ views need not be expressed as forecasts for the
parameters of a distribution. Instead, managers can, for instance, simply
specify a range for the expected return on a view portfolio. Such prior
information can then be translated into a uniform distribution for the
particular view over the given range. We denote the subjective distribution
of returns on the kth view by
π Wk.
(13.32)
Combining the Market and the Views: The Marginal
Posterior View Distributions
The BL model combines the objective and subjective distributions of
expected returns by means of Bayes’ theorem to obtain their posterior
distribution. A more general framework for combining probability distribu-
tions (and in particular, aggregating information from different sources) is
the so-called opinion pooling framework.23
One of the simplest opinion pool methods is the linear opinion pool,
in which probability distributions are aggregated as linear combinations.
Weights are used to represent the quality of forecasts (sources of infor-
mation). In our problem of combining market-implied and subjective view
distributions opinion pooling is an attractive alternative to a full-blown
Bayesian analysis, since the portfolio manager’s confidence in views can
naturally be employed as a weight.
Denote the cumulative distribution functions corresponding to the
market-implied and subjective view densities, π R
Wk and π Wk, by FR
Wk and
FWk, respectively. Suppose that the manager’s confidence in the kth view is
ck (expressed as a proportion). The posterior distribution of returns on the
kth view is then given by
p Wk = ckπ Wk + (1 −ck) π R
Wk,
(13.33)
for k = 1, . . . , K. As in the BL model, when confidence in a view is zero,
the posterior view distribution coincides with the market-implied prior
view distribution. Conversely, certainty in a view results in the posterior
distribution being the same as the manager’s subjective prior one.
23See, for example, Genest and Zidek (1986) and Cooke (1991) for a review of
opinion pooling approaches and methods.

Advanced Techniques for Bayesian Portfolio Selection
267
Views Dependence Structure: The Joint Posterior View
Distribution
In the BL model, views are a priori assumed to be independent (the
off-diagonal elements of the views’ prior covariance matrix, , in (8.4) in
Chapter 8 are usually set to zero).24 However, a posteriori, after blending
together views and market, the dependence among stock returns is mapped
onto the views. The mechanism of this mapping is implicit in the Bayesian
updating procedure.
In this section’s framework, we make it explicit. What allows us to
do this is our bottom-up approach—market and views are combined at
the univariate level. We extract the pattern of association contained in the
collection of market-implied view returns in W and superimpose it on the
K univariate posterior view distributions in the following way. (We provide
an overview of copulas in Appendix C of this chapter.)
1. Fit a copula to the return data in W, using the market-induced view
distributions in (13.31) as the marginal distributions.
2. Obtain the joint posterior view distribution through mapping the copula
onto the set of subjective marginal view distributions in (13.32) to derive
the joint posterior distribution of the K views. Denote the sample from
this joint posterior distribution by "
W.
Posterior Distribution of the Market Realizations
Finally, notice that our analysis until now has only centered on the returns
of the K assets involved in the manager’s views. One expects that ‘‘twisting’’
(via the views) of some of the stock returns would affect the remaining
returns as well, since all returns are mutually dependent. Below we show
how to reflect this feed-through effect. (In the BL model estimation, this
view propagation is implicit; see Chapter 8.)
We express the market realizations, R, in view coordinates in the
following way:
R ⇒
 RP′
RP′
n
	
.
(13.34)
The first block matrix above, RP′, is W, as defined in (13.30). While W
contains the market realizations of the K view portfolios, we can think of
24Recall from statistical theory that if the random variables X and Y have a bivariate
normal distribution and their covariance is zero, cov(X, Y) = 0, X and Y are
necessarily independent. The result is easily extended to any dimension. (In general,
however, zero correlation does not imply independence.)

268
BAYESIAN METHODS IN FINANCE
the lower block matrix, RPn
′, as the market realizations of the ‘‘non-view’’
portfolios. There are, clearly, a large number of linear combinations of the
N −K market realizations not involved in the views and, accordingly, no
single way to construct the lower block matrix. Meucci assumes that its row
vectors are orthogonal.25
In (13.34) we substitute RP′ with the sample from the joint posterior
view distribution, "
W, and obtain a sample of the posterior distribution of
the market realizations by reverting to the original market coordinates,
"R
d=
 "
W
RP′
n
	  P′
P′
n
	−1
,
(13.35)
All elements of "R are now adjusted according to the views and their
dependence structure. Notice that no analytical expression for the den-
sity of "R is available. This fact, however, does not obstruct portfolio
construction.
In the presence of nonnormality, portfolio construction can be per-
formed by minimization of a risk measure other than the portfolio standard
deviation. (In appendix A of this chapter, we present a brief overview of
some alternative risk measures.)
Portfolio Construction
In Appendix A of this chapter, we explain that the conditional value-at-risk
(CVaR) is a risk measure with a number of desirable properties and can be
used to formulate the portfolio selection problem as follows:
min
ω
CVaRp,
subject to constraints.
This minimization problem is solved numerically. When only a large
number of return scenarios (samples) is available (no analytical expression
for the return density, as in Meucci’s framework), the minimization is
scenario-based. We outline the approach of Rockafeller and Uryasev (2000)
for CVaR minimization in Appendix B.
25More formally, the matrix Pn is a (N −K × N) matrix spanning the null space
of P.

Advanced Techniques for Bayesian Portfolio Selection
269
Prior
Posterior
1.06
1.05
1.04
1.03
1.02
1.01
1.00
0.99
0.98
0.97
0.96
0.049 0.050 0.051 0.052 0.053 0.054 0.055 0.056 0.057 0.058
Expected Shortfall (CVaR)
Target Return x 10−3 
EXHIBIT 13.2
Mean-CVaR efficient frontiers
Source: Figure 4 in Meucci (2006a).
Illustration: Meucci’s Approach
Meucci (2006a) adopts a pragmatic approach in his empirical illustration.
Weekly return data on four international stock indexes are employed. The
indexes are the S&P 500, the FTSE 100, the CAC 40, and the DAX. He
asserts the asymmetric multivariate Student’s t-distribution for the index
returns and estimates its parameters by maximum likelihood by fitting
it to the observed return data. (However, we emphasize that Bayesian
estimation is also possible and even preferable if one would like to account
for parameter uncertainty.)
A large number of simulations are then generated from the asymmetric
Student’s t-distribution (using the parameter estimates). The simulations
make up the T × N matrix R. A single view is expressed—the DAX is
expected to realize between 0% and −2% in the following (one-week)
period. The returns in R are updated according to our earlier discus-
sion and CVaR minimization is employed to determine the optimal index
allocations.
The mean-CVaR efficient frontiers before and after the view on the DAX
index is reflected are plotted in Exhibit 13.2, while the corresponding prior
and posterior optimal allocations are given in Exhibit 13.3. The pessimistic
view on the DAX index worsens the expected return-risk trade-off and
shifts the efficient frontier to the right. As in the BL framework, the view is

270
BAYESIAN METHODS IN FINANCE
Target
Return
Index
0.96
0.99
1.02
1.05
Prior Allocations
S&P 500
45
42
39
37
FTSE 100
43
37
32
26
CAC 40
5
11
13
DAX
7
13
18
24
Posterior Allocations
S&P 500
47
45
39
35
FTSE 100
36
25
17
8
CAC 40
17
30
44
57
DAX
0
0
0
0
8
EXHIBIT 13.3
Prior and posterior optimal
allocations
Source: Adapted from Tables A and B in Meucci
(2006a).
propagated through the returns on the remaining indexes and their optimal
allocations—adjusted accordingly.
EXTENDING THE BLACK-LITTERMAN APPROACH:
STABLE DISTRIBUTION
In the previous section, we discussed that since the CAPM assumes that
returns are elliptically distributed, using it to derive the equilibrium returns,
π, in the presence of nonnormality lacks consistency. When more general
(than normality) distributional assumptions are adopted, it is appropriate to
consider also more general risk measures in obtaining π. Giacometti, Bertoc-
chi, Rachev, and Fabozzi (2007) (GBRF, hereafter) investigate the choice of
return distributions and risk measures in a normal, a Student’s t, and a stable
setting. We discuss their approach to equilibrium return estimation now.
Equilibrium Returns Under Nonnormality
The equilibrium returns, π, can be backed out from the portfolio selection
problem, as mentioned in Chapter 8. Let us see how. Consider the utility

Advanced Techniques for Bayesian Portfolio Selection
271
maximization problem in (6.3) in Chapter 6. We rewrite it below for the
case of a quadratic utility:
max
ω

ω′µ −A
2 ω′ω
	
,
(13.36)
where ω, µ, , and A are the usual notations for the portfolio weights,
expected returns, return covariance matrix, and coefficient of relative risk
aversion. To obtain the equilibrium returns, we assume the market is in
equilibrium and the benchmark’s market capitalization weights are the
optimal weights, ω*. The expression in (13.36) then takes the form
max
ω

ω −A
2 ω′ω
	
,
(13.37)
so that  is obtained as the vector of expected returns that would have
produced ω* in a procedure appropriately termed reverse optimization.
Under the assumption of return normality,  is given by
 = Aω∗,
(13.38)
which is the same expression as the one in equation (8.2) in Chapter 8. In a
general distributional setting, (13.37) is modified as follows:
max
ω

ω −A
2 ρ

ω′r
	
,
(13.39)
where ρ (ω′r) denotes an arbitrary measure of risk of the portfolio return,
ω′r. GBRF investigate three possibilities for ρ (ω′r): the variance, the VaR,
and the CVaR, and show that the equilibrium returns are given, respectively,
by
 =



AVω∗
when ρ (ω′r) = variance
A
2

Vω∗
√
ω∗′Vω∗CVaRα −µ

when ρ (ω′r) = CVaR
A
2

Vω∗
√
ω∗′Vω∗VaRα −µ

when ρ (ω′r) = VaR,
(13.40)

272
BAYESIAN METHODS IN FINANCE
where:
V = dispersion matrix equal to:
•, the covariance matrix, under a normal distributional
assumption.
•S(ν −2)/ν, under a Student’s t distributional
assumption, where S is the scale matrix and ν is the
degrees-of-freedom parameter of the Student’s
t-distribution.
•The dispersion matrix of the multivariate stable
distribution.26
VaRα = value-at-risk for the corresponding distribution.27
CVaRα = conditional value-at-risk for the corresponding
distribution.28
In an examination of the 50 largest constituents of the S&P 500
index, GBRF show that the combination of the stable distributional
assumption and the covariance matrix as a risk measure yields the best esti-
mates of the equilibrium returns, , while the stable distribution together
with the CVaR as a measure of risk produce the second-best estimates
of .
SUMMARY
The heavy-tailedness and asymmetry observed in asset returns could impact
adversely portfolio choice based on the mean-variance framework. Apart
from asserting a flexible nonnormal distribution for returns, one can employ
two approaches for quantitative portfolio selection. The first approach
involves specifying and maximizing an appropriate utility function. We pre-
sented HLLM’s framework, in which the utility function includes explicitly
the portfolio skewness.
The second approach consists of directly minimizing a risk measure,
which implicitly accounts for the heavy-tailedness and asymmetry in the
26See Rachev and Mittnik (2000) for the definition of the multivariate stable
distribution.
27The VaRα for the Student’s t-distribution can be obtained easily, as explained in
Chapter 11. The VaRα for the stable distribution can be computed numerically; see
Rachev and Mittnik (2000) and Lamantia, Ortobelli, and Rachev (2006a).
28See GBRF for the closed-form expression for CVaRα in the case of the Student’s
t-distribution and the integral representation of CVaRα in the case of the stable
distribution.

Advanced Techniques for Bayesian Portfolio Selection
273
return distribution. The CVaR is such a risk measure, whose minimization
can be performed using scenarios generated from the return distribu-
tion.
In the next chapter, we focus on multifactor models and present a
unifying framework for portfolio selection and risk management.
APPENDIX A: SOME RISK MEASURES EMPLOYED IN
PORTFOLIO CONSTRUCTION
The choice of risk measure employed in portfolio selection is not one to
be taken lightly. Minimizing an unsuitable risk measure could produce
suboptimal portfolio weights.29
Some risk measures capture the general uncertainty of returns and
penalize both downside and upside deviations from the mean. Among
them are the standard deviation and the mean absolute deviation. Since
minimizing them limits the potential for growth of the portfolio value,
even if returns have normal distribution (in general elliptical distribution,
such that the first two moments are sufficient to describe it uniquely),
these measures would produce optimal allocations that are not optimal for
investors with preference for very high portfolio returns.
The so-called ‘‘safety risk measures,’’ on the other hand, reflect only the
downside potential of returns—what investors generally perceive as risk.
We review some of them here.30 Denote portfolio return by Rp. (To avoid
some technical difficulties, we assume that Rp has a density.)
Lower Partial Moment
The lower partial moment is a generalization of
the semivariance proposed by Markowitz (1959). It only reflects return
realizations below a certain target return level, R,
LPMq

Rp

=

E

Rp −R
q
IRp<R
1/q
,
(13.41)
where q ≥1. The value of q = 2 corresponds to the semistandard deviation.
Investor’s risk aversion is directly related to the power, q, of the return
deviation—the higher the risk aversion, the higher q.
29See, for example, Ortobelli, Rachev, Stoyanov, Fabozzi, and Biglova (2005).
30For more details on downside risk measures, see Sortino and Satchell (2001).
Ortobelli, Rachev, Stoyanov, Fabozzi, and Biglova (2005) and Rockafellar, Uryasev,
and Zabarankin (2003) discuss the properties of various risk measures applied to
portfolio selection.

274
BAYESIAN METHODS IN FINANCE
MiniMax
The MiniMax of portfolio returns represents the worst outcome
that could occur if the portfolio return falls below a certain threshold, L,
and is defined as31
MM

Rp

= inf
#
L | P

Rp ≤L

= 0
$
.
(13.42)
Value-at-Risk
(VaR) The value-at-risk at the (1 −α) confidence level
(VaR(1−α)) of a portfolio is the maximum loss that could occur such that,
with probability α, this loss is no greater than VaR(1−α). Denote the portfolio
loss by Lp = −Rp. Portfolio p’s VaR is implicitly defined through the
equation
P

Lp > VaR(1−α)(Lp)

= α.
(13.43)
Equivalently, we can write that expression in terms of the portfolio’s
return distribution as
P

Rp < VaRα(Rp)

= α.
(13.44)
That is,VaR(1−α)(Lp) is the (1 −α) quantile of the loss distribution.
(Equivalently, VaRα(Rp) is the α quantile of the return distribution.) Some
values of α used in practice are 0.1, 0.05, and 0.01. Under the assumption
of normality, VaR is a multiple of the standard deviation. In that case, then,
minimization of either risk measure results in the same optimal portfolio.
The threshold, L, in (13.42) is often chosen to be the portfolio VaR(1−α)(Lp).
Conditional Value-at-Risk (CVaR)
The portfolio CVaR is the loss the
portfolio is expected to realize if its loss exceedsVaR(1−α)(Lp),
CVaR(1−α)

Lp

= E

Lp | Lp ≥VaR(1−α)

Lp

.
(13.45)
Equivalently,
CVaR(α)

Rp

= E

Rp | Rp ≤VaR(α)

Rp

.
(13.46)
We now outline a few points of comparison between VaR and CVaR.
These two measures are the focus of our attention because of the popularity
of the first and the advantages of the second. Neither the lower partial
moment nor the MiniMax provide information about the portfolio return
in the left tail of the return distribution, which is of primary interest in
portfolio risk analysis.
31MiniMax is proposed by Young (1998).

Advanced Techniques for Bayesian Portfolio Selection
275
■VaR does not provide information for the distribution of portfolio
losses beyond the α quantile.
■VaR is not subadditive; that is, the VaR of the portfolio return might
be larger than the sum of the VaR’s of the individual assets’ returns
(or sub-portfolio returns). This result is clearly very undesirable as it
contradicts the intuition of portfolio diversification benefits.
■Portfolio optimization based on VaR is much more difficult than the one
based on the CVaR. The reason is that when calculated using scenarios,
the portfolio VaR is not smooth as a function of portfolio positions, is
not convex, and has multiple local extremal points.
All of these shortcomings of VaR are overcome by CVaR. We discuss
the approach to CVaR minimization due to Rockafellar and Uryasev (2000)
in Appendix B.32
How does one compare the performance of portfolios generated through
minimization of various risk measures? The generally accepted approach is
to compare the portfolio return on a risk-adjusted basis by comparing var-
ious performance measures. Performance measures are then closely related
to risk measures and could be discussed in parallel. The most commonly
employed performance measure is the Sharpe ratio, defined as
SRp = E

Rp

−rf
σp
,
(13.47)
where rf is the risk-free rate and σ p is the portfolio standard deviation. The
disadvantages of the Sharpe ratio are directly related to the deficiencies of
the standard deviation as a measure of risk.33
Alternative performance measures corresponding to the risk measures
discussed above have been defined. For example, Sortino (2000) and
Sortino and Satchell (2001) propose the ratio between the portfolio’s
expected return and its lower partial moment. The performance measure
using the MiniMax is suggested by Young (1998). Rachev, Ortobelli, and
Schwartz (2004) propose using the VaR99% (see also Favre and Galeano,
2002), whereas the STARR ratio uses the portfolio’s CVaRα(Rp) to adjust
expected return for risk (Rachev, Martin, Racheva-Iotova, and Stoyanov,
2007).
32For more general constructions and detailed analysis, see Rachev, Stoyanov, and
Fabozzi (2007).
33Moreover, in the case return distributions with infinite variance, such as the stable
distribution, the Sharpe ratio is not defined.

276
BAYESIAN METHODS IN FINANCE
APPENDIX B: CVAR OPTIMIZATION
CVaR has attractive properties as a risk measure compared to VaR—it is
subadditive, a smooth function of portfolio positions, and its optimization
is relatively straightforward. Rockafellar and Uryasev (2000) developed the
CVaR optimization methodology, which we briefly outline here.34
Denote the returns on the N candidates for inclusion in the optimal
portfolio by R and the N × 1 vector of portfolio weights by ω. The portfolio
optimization problem based on the portfolio CVaR is expressed as
min
ω
CVaRα

Rp

,
(13.48)
subject to constraints,
(13.49)
where Rp = ω′R. Institutional portfolio managers face at least the following
two constraints,
ωj ≥0,
j = 1, . . . , N
(13.50)
N

j=1
ωj = 1.
Consider the definition of CVaR in (13.46). The quantity CVaRα

Rp

depends on VaRα

Rp

, which poses difficulties if no analytical expression
for VaRα

Rp

is available.
The insight of Rockafellar and Uryasev is that CVaRα

Rp

can be
substituted by the following simpler function,
Fα (ω, C) = C +
1
1 −α
 
−Rp −C
+ f (R) dR,
(13.51)
where [v]+ = v, when v > 0, and [v]+ = 0, when v ≤0, f (R) is the density
function of R, and C is the VaR defined in (13.43).
Rockafellar and Uryasev show that Fα (ω, C) is convex with respect to
C and
min
C Fα (ω, C) = CVaRα

Rp

.
(13.52)
34For more advanced portfolio risk analysis and optimization techniques, see Rachev,
Ortobelli, Stoyanov, and Fabozzi (2007).

Advanced Techniques for Bayesian Portfolio Selection
277
The implication of (13.52) is that CVaRα

Rp

can be minimized without
knowledge of VaRα

Rp

. Most importantly, minimizing Fα (ω, C) with
respect to all pairs (ω, C) is equivalent to minimizing CVaRα(Rp),
min
ω,C Fα (ω, C) = min
ω
CVaRα

Rp

.
(13.53)
Let (ω *, C*) be the pair, solution to the minimization in (13.53). The
first component, ω* are the portfolio weights that minimize CVaRα

Rp

.
The second component, C *, is generally the corresponding VaRα

Rp

.
Consider the case when no analytical expression for the density of
returns, f(R), exists. Instead, we have available a large number (M) of
scenarios generated from it. Denote the scenarios with superscripts, Rm =

Rm
1 , Rm
2 , . . . , Rm
N

, for m = 1, . . . , M. Then, the function, Fα (ω, C), can be
approximated as
Fα (ω, C) = C +
1
M (1 −α)
M

m=1

−ω′Rm −C
+ .
(13.54)
Rockafellar and Uryasev show that the problem of minimizing Fα (ω, C)
can be reduced to a linear programming (LP) problem. To do that, we
introduce auxiliary variables um such that
um ≥−ω′Rm −C
(13.55)
and
um ≥0,
(13.56)
for m = 1, . . . , M. The minimization problem then becomes
min
ω
%
C +
1
M(1 −α)
M

m=1
um
&
,
(13.57)
subject to constraints (for example, those in (13.50)).
APPENDIX C: A BRIEF OVERVIEW OF COPULAS
Suppose that there are N risk factors, R1, R2, . . . , RN, available. The infor-
mation about their codependence is contained in the collection of all
conditional probabilities of the type
P (Ri < ri | R1 < r1, . . . , Ri−1 < ri−1, Ri+1 < ri+1, . . . , RN < rN) .
(13.58)

278
BAYESIAN METHODS IN FINANCE
Notice that in order to compute these conditional probabilities, we need
to know the marginal distributions of the risk factors. The question is how
we can separate out the pure dependence structure information from the
information about the marginal behavior.
Suppose that the risk factors’ marginal distributions are given by the N
CDFs,
F1 (R1) , F2 (R2) , . . . , FN (RN) .
(13.59)
Since a distribution function takes values only on the range [0, 1],
computing the CDF in effect transforms each risk factor into a uniform
random variable.
The copula function is a multivariate uniform distribution with margins
the univariate uniforms in (13.59),
C (F1 (R1) , F2 (R2) , . . . , FN (RN)) .
(13.60)
Since the copula function contains the pure dependence structure
of the sample of data, we have a mechanism at hand for generating
scenarios—realizations
of
variables
with
certain
codependence
characteristics—from any distribution. We now demonstrate the procedure
to generate scenarios, using a Student’s t-copula (the Student’s t-distribution
is standardized, i.e., it has a mode of zero and a scale of 1).
Suppose that the N risk factors are stock returns and we have observa-
tions from T periods. Denote the T × N data matrix by R.
Copula Estimation
1. Fit a univariate Student’s t-distribution to each asset’s returns (each
column of R). The distributions are fitted independently from each
other. Denote the degrees-of-freedom estimates by 'ν1, . . . , 'ν1.
2. Compute the marginal CDFs, using the degrees-of-freedom estimates,


F1(R11,ˆν1) . . . FN(R1N,ˆνN)
F1(R21,ˆν1) . . . FN(R2N,ˆνN)
. . .
F1(RT1,ˆν1) . . . FN(RTN,ˆνN)


.
(13.61)

Advanced Techniques for Bayesian Portfolio Selection
279
3. Compute the observations of the copula, Ci, i = 1, . . . , T,
Ci =

F1

Ri1,ˆν1

. . . FN

RiN,ˆνN
 
.
(13.62)
4. Assuming that Ci has a N-dimensional Student’s t-distribution, estimate
its parameter, νC.
Scenario Generation
1. Simulate N-dimensional vectors from the copula


V1
1 . . . V1
N
V2
1 . . . V2
N
. . .
VM
1
. . . VM
N


,
(13.63)
where M is the number of scenarios (usually of the order of 10, 000 in
practical applications).
2. Translate the copula scenarios to scenarios of a random variable with a
N-dimensional Student’s t-distribution, using the inverse-fitted univari-
ate CDFs:


T1
1 . . . T1
N
T2
1 . . . T2
N
. . .
TM
1
. . . TM
N


=


F−1
1 (V1
1, ˆν1) . . . F−1
N (V1
N, ˆνN)
F−1
1 (V2
1, ˆν1) . . . F−1
N (V2
N, ˆνN)
. . .
F−1
1 (VM
1 , ˆν1) . . . F−1
N (VM
N , ˆνN)


.
(13.64)
The flexibility of modeling with copulas is clearly seen in the procedure
above. Various copula functions can be used to capture observed patterns
of dependence in the data. Some of the copulas most widely used in port-
folio risk management are Student’s t-copulas (skewed t-copula, grouped
t-copula, etc.).35
35For copula modeling with applications to finance, see McNeil, Frey, and Embrechts
(2005). See Demarta and McNeil (2005) for a discussion of Student’s t-copulas.

CHAPTER14
Multifactor Equity Risk Models
M
ultifactor models of equity returns evolved to address a key defi-
ciency of the capital asset pricing model (CAPM), namely, the implicit
assumption that the comovement of securities’ returns can be explained by
their covariance with the market and, therefore, the bearing of nonmarket
risk is not rewarded. There are pervasive common factors in addition to
the market that drive returns. Investors thus need to be compensated for
bearing this nondiversifiable risk via additional risk premia. Different sets
of factors have been proposed in the asset-pricing literature on this topic.
For example, Fama and French (1992) examine the roles of the market
beta, size, earnings-to-price, leverage and book-to-market equity, while
Chen, Roll and Ross (1986) focus on macroeconomic predictors such as
the spread between long and short interest rates, unexpected inflation, and
industrial production.
Multifactor models play key roles in most stages of the investment
management process. They could be used for security selection, portfolio
construction, assessment of the potential performance of a portfolio, risk
control relative to a benchmark, as well as performance attribution analysis.1
In this chapter, we use the multifactor setting to attempt to unify
the topics of the previous chapters—mean-variance portfolio optimiza-
tion, volatility modeling, advanced methods for portfolio construction, and
Bayesian estimation—and present a simple version for what an integrated
approach to portfolio risk modeling could look like in practice. We review
the three types of multifactor models and then discuss in detail the estima-
tion of a fundamental factor model, focusing on risk estimation and risk
component analysis. We emphasize the application of multifactor models to
returns scenario generation and show how to attribute risk when the condi-
tional value-at-risk (CVaR) is employed as a risk measure. Then, we present
1For details on these applications of multifactor models, see Fabozzi, Jones, and
Vardharaj (2002).
280

Multifactor Equity Risk Models
281
the Bayesian perspective to multifactor equity modeling and conclude with
an illustration of a heavy-tailed multifactor model.
PRELIMINARIES
The multifactor equity risk model is a purely empirical construction. It
does not involve any assumptions regarding investor behavior or market
efficiency, as do equilibrium models such as the CAPM and the arbitrage
pricing theory (APT) model. Multifactor models are simply tools to aid
the investment management process. They offer a parsimonious structure
to model equity returns, through the dynamics of a small number of
variables.
In a multifactor equity model, the return on a stock is decomposed into
return linearly related to the factors and a stock-specific return. The linear
relationship between a stock’s excess return and the risk factors estimated
by any multifactor model is written as
Ri −Rf = αi + βi,1f1 + βi,2f2 + ··· + βi,KfK + ϵi,
(14.1)
where: Ri = rate of return on stock i.
Rf = risk-free rate of return.
f j = rate of return on risk factor j.
βi,j = sensitivity of stock i to risk factor j.
αi = residual return of stock i.
ϵi = specific return on stock i.
Neither the number nor the identity of the factors—pervasive sources
of risk driving stock returns—are specified by theory. Numerous empirical
studies, however, have uncovered factors with explanatory power. Multi-
factor models can be categorized into three groups based on the nature
of the factors employed—statistical factor models, macroeconomic factor
models, and fundamental factor models.2
Statistical Factor Models
Statistical factor models do not require a priori factor identification. On the
contrary, factors (the time series of factor returns) are extracted from the
2Among the risk model vendors using the fundamental model approach are MSCI
Barra and Northfield Information Services. FinAnalytica and Advanced Portfolio
Technology (APT) provide risk models based on all three approaches.

