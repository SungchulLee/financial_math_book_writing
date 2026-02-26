# Multiple Asset Models & Exchange Options

!!! info "Source"
    **Financial Mathematics: An Introduction to Derivatives Pricing** by Lane P. Hughston and Christopher J. Hunter, King's College London, 2000.
    These notes are used for educational purposes.

## Multiple Asset Models

21
Multiple Asset Models
Until now we have considered a financial market that consists of a single basic
asset together with a money market account and derivatives based on these
two assets. This market is driven by a single source of randomness. Needless
to say, for a more realistic financial market we have to consider a larger num-
ber of assets and more sources of randomness. So in this chapter, we analyse
markets with both multiple assets and sources of uncertainty. For simplicity,
we shall begin by assuming that these are non-dividend paying assets, but
later we will extend our results to the case when continuous dividends are
paid on shares, or equivalently, interest is paid on foreign currencies.
21.1
The Basic Model
We want a market that has more than a single basic asset.
Consider a
situation where there are n assets, with prices Si
t (i = 1, . . . , n). We also
want a market where there is more than one source of uncertainty. So as-
sume that the assets are driven by an N-dimensional Brownian motion W α
t
(α = 1, . . . , N). In order for everything to run smoothly we require n ≥N.
Otherwise we are led to a so-called incomplete market situation.
How are the movements of the n asset prices related? This can be for-
malised by introducing the idea of an instantaneous covariance matrix for the
asset price dynamics. Let us proceed as follows. We assume the Brownian
motions are independent, in the sense that the Ito rule is given by
dW α
t dW β
t = δαβdt,
(21.1)
where δαβ is the identity matrix.
Thus dW 1dW 1 = dt, dW 2dW 2 = dt,
dW 1dW 2 = 0, and so on. As before, we also have dW αdt = 0 for all α.
Thus the multi-dimensional Ito rule is a straight-forward generalization of
the one-dimensional case.
Now that we have clarified the nature of the multi-dimensional Brownian
motions, we can return to the asset price changes. The basic model for n
asset prices is given by the following dynamics:
dSi
t
Si
t
= µi
tdt +
X
α
σiα
t dW α
t .
(21.2)
Here µi
t and σiα
t
are adapted processes, in the sense that they depend, in a
general way, only on the history of the multi-dimensional Brownian motion
126

W α
t
from time 0 to time t. The n × N matrix σiα, for i = 1, . . . , n and
α = 1, . . . , N, is called the volatility matrix. It measures the sensitivity of
asset number i to Brownian motion number α. The processes W α
t can be
thought of intuitively as representing ‘independent’ sources of randomness,
or uncertainty, in the markets.
Exercise 21.1 Consider a simple 2-dimensional Black-Scholes world, with
asset price processes,
dS1
t /S1
t
=
µ1dt + σ11dW 1
t + σ12dW 2
t
dS2
t /S2
t
=
µ2dt + σ21dW 1
t + σ22dW 2
t
(21.3)
where the vector µi and the matrix σij are both constant. Solve these equations
for S1
t and S2
t .
Now let us investigate the volatility matrix more closely. To this end, we
consider the following product:
dSi
Si
dSj
Sj
=
(µi
tdt +
X
α
σiα
t dW α
t )(µj
tdt +
X
β
σjβ
t dW β
t )
=
X
α
σiα
t dW α
t
X
β
σjβ
t dW β
t
=
X
α
X
β
σiα
t σjβ
t dW α
t dW β
t
=
X
α
X
β
σiα
t σjβ
t δαβdt
=
X
α
σiα
t σjα
t dt.
(21.4)
The matrix
Cij
t =
X
α
σiα
t σjα
t
(21.5)
that arises here is called the instantaneous covariance matrix of the set of
assets under consideration.
Exercise 21.2 Calculate the instantaneous covariance matrix for the 2-dimensional
Black-Scholes market given in exercise (21.1).
In the case i = j, we have
ÃdSi
Si
!2
= Cii
t ,
(21.6)
127

where
Cii
t =
X
α
(σiα
t )2
(21.7)
is the instantaneous variance (squared volatility) for the asset i. Note that
in the case when there is only a single asset with dS1/S1 = µi +σ1dW 1, then
C11
t
= (σ1)2, as expected. If we write
σi =
sX
α
σiασiα
(21.8)
for the volatility of asset i, then the matrix
ρij = Cij
σiσj
(21.9)
is called the instananeous correlation in the motion of asset i and asset j.
Exercise 21.3 Calculate the correlation matrix for the 2-dimensional Black-
Scholes market. What are the volatilities of the two assets?
We note that the covariance matrix Cij is non-negative in the sense that
for any ‘vector’ of numbers θi (i = 1, . . . n) we have
X
ij
Cijθiθj ≥0.
(21.10)
This result can be given a financial interpretation. Suppose that we form a
portfolio of assets, holding asset Si in the quantity φi. Thus φi is the number
of shares one holds of asset i, which has price Si. The the total value of the
portfolio is clearly
P
i φiSi. Note that some of the φi’s can be negative, in
the case of short positions. Now suppose we define
θi =
φiSi
P
j φjSj .
(21.11)
Then θi is the percentage of the total value of the portfolio that is held in
asset i. With this in mind, we can look at the change in the value of the
portfolio as the market moves. If
Vt =
X
i
φiSi
t
(21.12)
128

is the value of the portfolio at time t, then
dV =
X
i
φidSi,
(21.13)
is the instantaneous change in the value of the portfolio, for the given holding
defined by φi, when the asset price changes are given by dSi. Therefore, by
the Ito rules we have
(dV )2
=
X
ij
φiφjdSidSj
=
X
ij
φiφjSiSjCijdt.
(21.14)
So, for the percentage change in the value of the portfolio, we have
ÃdV
V
!2
=
X
ij
φiSi
V
φjSj
V
Cijdt
=
X
ij
θiθjCijdt,
(21.15)
where we have used the fact that θi = φiSi/V . Thus,
P
ij θiθjCij represents
the instantaneous variance in the portfolio value at time t. But clearly the
variance of the portfolio must be non-negative. Thus equation (21.10) can
be interpreted as saying that the variance of any portfolio has to be non-
negative. These ideas can be developed further, and lead to the concepts of
portfolio theory, which is an important branch of finance theory.
21.2
No Arbitrage and the Zero Volatility Portfolio
Here, we shall consider one particular aspect of portfolio analysis that is of
great significance to derivatives pricing. Suppose we consider the problem
of choosing a portfolio weighting such that the portfolio has instantaneously
zero volatility. Then, over the next short period, this portfolio would offer
a definite rate of return. By the no arbitrage condition, this rate of return
would have to be the money market interest rate rt.
We have seen from (21.15) that with a holding weight of θi in asset i, the
portfolio variance vanishes if and only if
X
ij
θiθjCij = 0.
(21.16)
129

But, we can express this sum in the form
X
ij
θiθjCij
=
X
α
X
i
X
j
θiθjσiασjα
=
X
α
ξαξα,
(21.17)
where ξα = P
i θiσiα. Now, since (21.17) is given by a sum of squares, clearly
(21.16) holds if and only if ξα = 0 for each value of α. In other words, the
portfolio variance (risk) vanishes at time t if and only if θi is chosen so that
X
i
θiσiα = 0.
(21.18)
Now let us return to the expression for the change in the portfolio value,
(21.13), and note that
dV
V
=
P
i φidSi
V
=
P
i φiSi(µidt +
P
α σiαdW α)
P
i φiSi
=
X
i
θiµidt +
X
α
ÃX
i
θiσiα
!
dW α.
(21.19)
Clearly the volatility of the portfolio value V vanishes at time t if and only
if the condition (21.18) holds at that time.
We require that
P
i θiµi = rt if and only if θiσiα = 0. In other words,
we want the rate of return on the portfolio to be the short rate (i.e. the
money market interest rate) if and only if the portfolio volatility vanishes.
This implies that there must exist a set of numbers λα (α = 1, . . . , N) such
that
X
i
θiµi = rt +
X
α
λα
ÃX
i
θiσiα
!
.
(21.20)
However, since P
i θi = 1, this relation can be written in the form
X
i
θiµi =
X
i
θir +
X
i
θi(
X
α
λασiα),
(21.21)
which has to hold for any choice of θi. Hence it follows that
µi = rt +
X
α
λασiα.
(21.22)
130

This is the no arbitrage condition for n assets driven by N Brownian motions,
when there are no dividends.
Note that the ‘vector’ λα can be interpreted as the market risk premium
for factor α. In other words, λα is the excess rate of return, attributable to
factor α, per unit of volatility in that factor.
For example, suppose that we have two assets, but just a single random
factor (i = 1, 2 α = 1) Then, suppressing α, we have
µ1 = r + λσ1
and
µ2 = r + λσ2 .
(21.23)
Eliminating λ, we obtain
µ1 −r
σ1
= µ2 −r
σ2
,
(21.24)
which is equivalent to the no arbitrage condition that we derived earlier in
connection with a share-price and an option. Thus we see that the two assets
have a common risk premium, given by λ.
21.3
Market Completeness
Now let us consider the risk premium vector λα further. For no arbitrage, we
know that (21.22) has to be satisfied. But if λα satisfies (21.22) is there any
other vector, say ¯λα that also satisfies (21.22)? If so, then their difference,
λα −¯λα would have to satisfy
X
α
(λα −¯λα)σiα = 0.
(21.25)
We say that a set of assets Si (i = 1, . . . , n), or market, is complete with
respect to the Brownian motion W t
α if there exists no non-vanishing vector
ξα such that
P
α ξασiα = 0. This market completeness condition is equivalent
to a requirement that the matrix σiα should be of maximum rank (N). If the
assets Si are complete, then any derivative adapted to W α
t , can be hedged
with a portfolio of positions in these assets.
131

22
Multiple Asset Models Continued
22.1
Dividends
Now let us consider the situation when dividends are paid in the multi-asset
case. This leads to a simple modification of formula (21.22). In particular,
suppose that there is a dividend (or interest) paid continuously at the rate δi
t
for asset i. This means that during the short interval dt, the holder of asset
i receives a payment of δiSidt. Thus, if the portfolio has value V = P
i φiSi,
then the total gain (or loss) to the holder over the interval dt is given by
R = dV +
X
i
φiSiδidt,
(22.1)
i.e., it is the change in value of the portfolio, plus all the dividends (or
interest). In percentage terms, this is
R
V
=
dV + P
i φiSiδidt
V
=
dV
V +
X
i
θiδidt,
(22.2)
since θi = φiSi/V . But, we calculated the percentage change in the portofolio
value in (21.19), so
R
V =
X
i
θi(µi + δi)dt +
X
iα
θiσi,αdW α.
(22.3)
Thus, if we eliminate the randomness by applying condition (21.18), then
the no arbitrage condition tells us that
P
i θi(µi +δi) = rt when
P
i θiσiα = 0.
This implies that there must exist λα such that
µi + δi = r +
X
α
λασiα.
(22.4)
This is the general no arbitrage condition for n assets which pay continuous
dividends (or interest).
Now we can take formula (22.4) for the drift, and reinsert it into the asset
dynamical equation to obtain
dSi
Si = (r −δi)dt +
X
α
σiα(dW α + λαdt).
(22.5)
132

This is the general dynamical equation for n dividend paying assets under
the condition of no arbitrage. We see that the only modification required is
to subtract offthe dividend rate (or foreign interest rate) from the ‘domestic’
interest rate r.
22.2
Martingales and the Risk-Neutral Measure
We have seen, in the case of multiple assets with no dividends, that the no-
arbitrage requirement is equivalent to the condition (21.22) on the drift of
the assets,
µi = r +
X
α
λασiα,
(22.6)
where r is the short rate of interest, λα is the market price of risk vector, and
σiα is the volatility matrix. The no-arbitrage condition is both necessary and
sufficient for the existence of the market risk premium vector λα, which for
each factor can be interpreted as the excess rate of return (above the short
rate) per unit of volatility risk. If we substitute (21.22) into the asset price
process (21.2), then we obtain
dSi
Si = rdt +
X
α
σiα(dW α + λαdt).
(22.7)
Here, for convenience, we occasionally suppress the subscript t, writing Si
for Si
t; but remember that all processes are adapted, i.e. they depend in a
general way on the history of W α
s for 0 ≤s ≤t. In addition to the assets Si
(i = 1, . . . , n) we also have the money market account Bt. We want to assume
market completeness, that is, that σiα has maximal rank N, the dimension
of the Brownian motion). This ensures that the market-risk premium vector
λα is unique. Also, it ensures that when W α
t moves at least one of the market
prices Si moves. In that sense, market completeness implies that every move
in W α
t implies some move in the prices Si, so that W α
t is ‘fully expressed’ in
the given asset changes. Otherwise, the market is ‘incomplete’.
Our next step is to form a multi-asset density martingale ρt,
ρt = exp
"
−
Z t
0
X
α
λα
s dW α
s −1
2
Z t
0
X
α
(λα
s )2ds
#
,
(22.8)
where α = 1, . . . , N. This expression is, in fact, given by the product of
the corresponding density martingales for the various components of λα. In
133

other words,
ρt =
N
Y
α=1
ρα
t ,
(22.9)
where
ρα
t = exp
·
−
Z t
0 λα
s dW α
s −1
2
Z t
0 (λα
s )2ds
¸
.
(22.10)
The following facts emerge:
1. The process ρt is a martingale with respect to the measure defined by
the expectation Es.
2. For each value of i, the ratio ρtSi
t/Bt is a martingale with respect to
the measure Es.
3. If we define the risk-neutral measure E∗
s according to the scheme
E∗
s[Xt] = Es[ρtXt]
ρs
(22.11)
for any adapted random variable Xt, then the process W ∗α
t
defined by
W ∗α
t
= W α
t +
Z t
0 λα
s ds
(22.12)
is a standard N-dimensional Brownian motion with respect to E∗
s. That
is, with respect to E∗
s, the process W ∗α
t
is normally distributed for each
value of α, with mean 0 and variance t, has independent increments,
and furthermore W ∗α
t
and W ∗β
t
are independent for α ̸= β.
These results can be established by analogy with the corresponding results
in the single asset case. Thus, for the asset process we can write
dSi
Si = rtdt +
X
α
σiαdW ∗α
t ,
(22.13)
where W ∗α
t
is a standard Brownian motion with respect to the risk-neutral
measure.
Moreover, since the ratio ρtSi
t/Bt is a martingale, we have
ρsSi
s
Bs
= Es
"ρtSi
t
Bt
#
,
(22.14)
134

and thus
Si
s
Bs
=
Es
h
ρt( Si
t
Bt)
i
ρs
,
(22.15)
which by the definition of the risk-neutral measure gives
Si
s
Bs
= E∗
s
"Si
t
Bt
#
.
(22.16)
Thus, the absence of arbitrage ensures the existence of a unique risk-neutral
measure such that the ratio of any asset price to the money market account
is a martingale. This generalises the analogous result that we obtained in
the single asset case.
22.3
Derivatives
Now suppose that we have a derivative with payout CT at time T. We assume
that the payout is adapted to W α
s for 0 ≤s ≤T. For example, CT can be
a function of the values of the various assets Si
s for various times between 0
and T. Let Ct denote the value of the derivative at time t. Then since the
derivative is also an asset, we can use the martingale condition (22.16) to
infer that
Ct
Bt
= E∗
t
·CT
BT
¸
,
(22.17)
or equivalently
Ct = BtE∗
t
·CT
BT
¸
.
(22.18)
This gives us a formula for the price process of the derivative, and, in par-
ticular, allows us to compute its value today, C0. Since the money market
account Bt is given by
Bt = exp{
Z t
0 rsds}
(22.19)
it is worth noting that (22.18) can be written in the form
Ct = E∗
t
"
exp{−
Z T
t
rsds}CT
#
.
(22.20)
Thus if rs is non-random, or more generally if it is independent of the payoff
CT, then (22.20) can be further simplified.
135

Formula (22.20) is, of course, not the end of the story, but really is just
the beginning. Given (22.20), we can compute the hedge ratios φi
t needed in
order to construct a portfolio in the Si
t’s and Bt to replicate the derivative.
If n > N, then the hedge portfolio can be constructed with some flexibility.
In my end is my beginning.
—T.S. Eliot, Four Quartets.
136

A
Glossary
American option An option that can be exercised at any time up to the
expiration date.
arbitrage
at the money A call or put option with a strike price equal to the current
share price is said to be ‘at the money’.
Call option A derivative that gives its owner the right to buy an asset at
a fixed price, called the strike price.
discount factor Something related to the time-value of money.
European option An option that can only be exercised at a fixed expira-
tion date.
expectation The expectation of a discrete random variable X with proba-
bility distribution p(xi) = Prob[X = Xi] is
E[X] =
X
i
xip(xi)
It gives the ‘average’ value of X.
The expectation of a continuous
random variable X with probability density function ρ(x) is given by
E[X] =
Z ∞
−∞xp(x)dx
in the money An option is said to be ‘in the money’ if it would have a
positive payoffif it were exercised immediately.
interest rate The rate at which you pay interest.
long position The position created by possession of an asset.
137


## Multiple Asset Models Continued

martingale
out of the money An option is said to be ‘out of the money’ if it would
have have a negative payoffif it were exercised immediately.
probability density function Similarly, the probability density function
ρ(x) of a continuous random variable X, if it exists, is a function ρ(x)
such that
Prob[a ≤X ≤b] =
Z b
a ρ(x)dx
put-call parity A relation holding between the values of call and put op-
tions with common strikes, in the absence of dividends.
put option An option that gives the owner the right, but not the obliga-
tion, to sell an asset at a pre-specified price.
random variable A random variable X is a function that maps each pos-
sible outcome from an experiment to a real number.
risk-free Guaranteed, sure.
sample space The sample space can be thought of as the set of all possible
outcomes of an experiment or trial. The sample space is discrete if the
elements of the sample space can be indexed by the integers (i.e., it is
countable).
short position A negative position in an asset; the position in an asset
created when an asset is sold, but before the asset has been actually
delivered; an American style derivative, whose payoffis minus the value
of the underlying asset at the time of exercise, and whose price today
is equal to minus the value of the asset today.
standard deviation The standard deviation σ(x) of a random variable X
is defined by σ(X) = [V (X)]1/2, where V (x) is the variance.
stock A part ownership of a company.
138

strike price The amount of money needed to exercise an option, usually
denoted K.
time value of money The fact that money now is worth more than money
in the future.
underlying asset A stock or whatever on which a derivative is based.
variance The variance of a random variable X, if it exists, is defined by
V [X] = E[(X −E[X])2] = E[X2] −E[X]2
Wiener process Brownian motion with drift.
139

B
Some useful formulae and definitions
B.1
Definitions of a Normal Variable
The N(m, V ) probability density function is
ρm,V (x) =
1
√
2πV exp
"
−(x −m)2
2V
#
.
(B.21)
The cumulative normal function is defined to be
N(x) =
1
√
2π
Z x
−∞exp
"
−ξ2
2
#
dx.
(B.22)
B.2
Moments of the Standard Normal Distribution
For even moments,
1
√
2π
Z ∞
−∞x2n exp
"
−x2
2
#
dx = (2n)!
n!2n ,
(B.23)
while for odd moments,
1
√
2π
Z ∞
−∞x2n+1 exp
"
−x2
2
#
dx = 0.
(B.24)
The first few even moments are
1
√
2π
Z ∞
−∞exp
"
−x2
2
#
dx = 1
(B.25)
1
√
2π
Z ∞
−∞x2 exp
"
−x2
2
#
dx = 1
(B.26)
1
√
2π
Z ∞
−∞x4 exp
"
−x2
2
#
dx = 3.
(B.27)
140

B.3
Moments of a Normal Distribution
1
√
2πV
Z ∞
−∞x exp
"
−(x −m)2
2V
#
dx = m
(B.28)
1
√
2πV
Z ∞
−∞x2 exp
"
−(x −m)2
2V
#
dx = m2 + V
(B.29)
1
√
2πV
Z ∞
−∞x3 exp
"
−(x −m)2
2V
#
dx = m3 + 3mV
(B.30)
1
√
2πV
Z ∞
−∞x4 exp
"
−(x −m)2
2V
#
dx = m4 + 6V m2 + 3V 2
(B.31)
B.4
Other Useful Integrals
For a > 0,
1
√
2π
Z ∞
−∞exp
"
−ax2
2
+ bx + c
#
=
1
√a exp
" b2
4a + c
#
.
(B.32)
Z ∞
0
e−λxdx = λ
for
λ > 0
(B.33)
If X is an N(m, V ) random variable,
E[eαX] = eαm+ 1
2 α2V .
(B.34)
B.5
Ito’s Lemma
If Xt satisfies
dXt = µtdt + σtdWt
(B.35)
and F(x) is a twice differentiable function, then
dF(Xt) = ∂F(Xt)
∂Xt
dXt + 1
2
∂2F(Xt)
∂X2
t
dX2
t ,
(B.36)
where
dt2 = 0,
dtdWt = 0
and
dW 2
t = dt.
(B.37)
141

B.6
Geometric Brownian Motion
dSt = St(µdt + σdWt)
(B.38)
has solution
St = S0 exp
·
(µ −1
2σ2)dt + σWt
¸
.
(B.39)
B.7
Black-Scholes Formulae
The Black-Scholes equation for a derivative C(St, t) is
∂C
∂t + 1
2
∂2C
∂S2
t
S2
t σ2 = r
Ã
C −∂C
∂St
St
!
.
(B.40)
For a call option with payofffunction C(ST, T) = max[ST −K, 0], it has
solution
C0 = e−rT[S0erTN(h+) −KN(h−)].
(B.41)
A put option with payofffunction P(ST, T) = max[K −ST, 0], it has
P0 = e−rT[KN(−h−) −S0erTN(−h+)],
(B.42)
where
h± ≡ln( S0erT
K ) ± 1
2σ2T
σ
√
T
.
(B.43)
The payofffor a call option with dividends is
C0 = e−(r−δC)T
√
2π
Z ∞
−∞F(S0e(r−δ)T+σ
√
Tξ−1
2σ2T)e−1
2 ξ2dξ
(B.44)
For the Black-Scholes formula we then obtain, in the case of a call option
(with no dividends paid on the option itself):
C0 = e−rT[S0e(r−δ)TN(h+) −KN(h−)],
(B.45)
where
h± = ln(
˜ST
K ) ± 1
2σ2T)
σ
√
T
.
(B.46)
We still need to derive the formula in the case of a put option with dividends.
Put-call parity says that
C0 = S0 −e−rTK + P0.
(B.47)
142

B.8
Bernoulli Distribution
The simplest nontrivial discrete probability distribution is the Bernoulli dis-
tribution. There are only two points in the sample space Ω= {u, d}. The
probability distribution is then
Prob[X = u] = p
Prob[X = d] = 1 −p
(B.48)
The expectation of the random variable X is E[X] = pu + (1 −p)d; the
variance is V [X] = p(1 −p)(u −d)2.
B.9
Binomial Distribution
This distribution is obtained by the consideration of n indepentant, identical
Bernoulli trials. Let X be the random variable which counts the total number
of u’s in n trials. We can obtain this by setting u = 1, d = 0, and summing
over n independent Bernoulli trials Yi. The binomial distribution is then
given by
Prob[X = x] =





Ã
n
x
!
pxi(1 −p)n−xi
forxi = 0, 1, . . . , n
0
otherwise
(B.49)
The expectation of X is E[X] = np; the variance of X is V [X] = np(1 −p).
Here the combinatorial function
Ã
n
x
!
, sometimes denoted Cn
x (‘n choose
x’) is defined by
Ã
n
x
!
=
n!
x!(n −x)!.
(B.50)
B.10
Central Limit Theorem
Let Xi (i = 1, . . . , n) be a set of n independent, identically distributed ran-
dom variables, each with mean m and variance V . Define
Zn =
Pn
i=1(Xi −m)
√n
.
(B.51)
Then the limit
Z = lim
n→∞Zn
(B.52)
143


## Exchange Options

exists, and is normally distributed with mean 0 and variance V . Equivalently,
we can assert that
lim
n→∞Prob


n
X
i=1
(Xi −m) < λ
v
u
u
tV ar[
n
X
i=1
(Xi −m)]

= N(λ),
(B.53)
where N(λ) is the normal distribution function.
We can use the Central Limit Theorem to analyze the behaviour of the
random variable Zn in equation (B.51). We can rewrite Zn in terms of the
average ¯Xn of n Bernoulli trials,
Zn = 2√n( ¯Xn −1
2),
(B.54)
where
¯Xn = 1
n
n
X
i=1
Xi.
(B.55)
Thus, by the Central Limit theorem Zn approaches a normal distribution.
Moreover, we can calculate the mean and variance of ¯X as E[ ¯Xn] = 1/2 and
V [ ¯Xn] = n/4, from which it follows that E[Zn] = 0, and V [Zn] = 1.
144

C
Solutions
Section 1
1. Why do bond prices fall when the interest rate of the money market account rises?
This is easiest to see by considering an example. Suppose that the initial value of
the money market interest rate is 5%, and that at some time it increases to 6%.
Before the interest rate rise, how much would you be willing to pay for a one-year
bond with a notional of $100 and an annual interest rate of 7%? This means that
you pay an amount B0 for the bond now, and receive $107 dollars in one year’s
time. We can determine B0 using arbitrage.
Suppose that we start with nothing. In order to invest in the bond, we need to
borrow B0 dollars from the money market account. Then in one year’s time, we
receive $107 for the bond, but owe B0e0.05 dollars for the loan. Since we started
with nothing, we must end with nothing, and hence
107 −B0e0.05 = 0
(C.1)
which tells us that B0 is 107e−.05 = 101.78 dollars. This is how we can price bonds
using arbitrage.
Now suppose that we repeat the argument when the money market interest rate
is 6% instead of 5%. The new price of the bond is 107e−0.06 = 100.77 dollars,
which is less than the previous price. The price of the bond drops because the no
arbitrage condition requires an investment in the bond to have the same return as
an investment in the money market account. Because the interest rate on the bond
is fixed, this is only possible if the bond price falls.
Why does the value of a bond rise if the credit quality improves? This question
is a little more difficult to quantify, since we have no exact mathematical way of
describing loan default. However, suppose that we have two bonds which have the
exact same characteristics, except that one is more likely to default than the other.
Which are you willing to pay more for?
Obviously the one which is less likely
to default, that is, the one with the better credit rating. We now want to apply
this argument to a single bond—but before and after an improvement in the credit
quality. If the credit quality improves, and since all other properties of the bonds
are the same, then by the above argument you should be willing to pay more for
the bond after its credit rating has improved. This is why a bond price increases
when credit quality improves.
2. We want to calculate the effective continuously compound interest rate earned on
an account which has an annual interest rate of r = 6.1% which is paid on a monthly
compounded basis. Begin by assuming that we have B0 dollars in the bank. At the
end of one month, the interest paid on this amount is B0r/12. That is, after one
month, the amount that we have in the bank is
B1 = B0(1 + r/12).
(C.2)
How about after the second month? Well, we earn an amount of interest equal to
B1r/12, so
B2
=
B1(1 + r/12)
=
B0(1 + r/12)2.
(C.3)
145

By induction, you should see that for m ≤12,
Bm = B0(1 + r/12)m,
(C.4)
and hence after a year
B12 = B0(1 + r/12)12.
(C.5)
What is the effective continuously compounded interest rate ρ? We can calculate
this by noting that after one year, an initial investment of B0 dollars would be
worth B0eρ dollars. Equating the two results we see that
B0(1 + r/12)12 = B0eρ,
(C.6)
or
ρ
=
12 log(1 + r/12)
=
0.0608,
(C.7)
and hence the effective continuosly compounded rate is 6.08%.
Note that if we divide the year up into n equal periods and repeat the above
argument, then the amount of money in the bank account at the end of the year is
Bn = B0(1 + r/n)n.
(C.8)
As we take n very large, we see that
lim
n→∞Bn = B0er,
(C.9)
which is the continuously compounded limit.
3. If we are paying interest into a money market account at a constant rate of r dollars
per unit time, then the change dBt in the amount of money in the bank account
over the time interval [t, t + dt] is equal to the amount of interest paid, which is
rBtdt. Thus, the differential equation is
dBt
dt = rBt.
This has solution
Bt = B0ert.
This relation will be used throughout the book to describe the time evolution of a
money market account.
4. The most money that you can lose by buying an option is the purchase price that
you paid for it. You never lose more because if the payoffof the option is negative
(the derivative is out of the money), then you simply do not ‘exercise your option’
and the option expires unused. This should be contrasted with a forward contract
on an asset, which is a strict obligation – you must buy the asset at the strike price,
whether it is beneficial to you or not.
146

Option Type
Strike
Market Value
Intrinsic Value
American Call
6000
£1265
£850
American Put
6000
£295
£0
European Call
6025
£1085
£600
European Put
6025
£340
£0
5. For the call and put options specified in the text, the market and intrinsic (if the
option were exercised immediately) values are given below.
The market values are greater than the intrinsic values because they take into
account the fact that the value of the index may achieve higher values before it
expires, and hence pay out more than its current intrinsic value. The buyer of the
option must pay for this potential gain, which is why the market value is larger
than the intrinsic value. A reverse argument also may be applied, that the index
may go down and the payoffbe less, however from a purely heuristic point of view,
the total possible drop in the payoffis less than the total possible gain in the payoff
(which is unlimited).
6. A bank with a large number of fixed-rate loans or mortgages has a great deal of
interest-rate risk. If the interest rate rises, then the bank will be receiving less
than the market rate for its investments. In essence, it will be losing money. A
company that sells products domestically, but buys supplies, for example timber,
from a foreign nation, has a foreign-exchange risk. The price of timber will become
more expensive if the foreign currency appreciates against the local currency, but
the income from domestic sales is unaffected. Thus, the company will effectively be
losing money.
7. Suppose a dealer sells a put with strike K. If the value of the stock ST is lower
than the strike when the put is exercised, then the dealer must pay the owner
of the option this difference. If the value of the stock is higher than the strike
price, then the dealer does not have to pay anything. Thus, the payofffunction is
−max[K −St, 0] = min[St −K, 0], which is shown in figure A.1.
Consider a portfolio which is long a call with strike K, and short a put with the
same strike. The payofffunction for this portfolio is
VT
=
max[ST −K, 0] + min[ST −K, 0]
=
ST −K,
(C.10)
which is the same as the payofffor a forward contract. Graphically, you can see
that by adding the payoffs from figures 1.1 and C.1 you obtain the payoffin figure
1.3. The fact that the payofffor a basic call option is equal to the payofffor a put
option plus a forward contract is known as put-call parity.
8. Figure 1.4 is known as a ‘call spread’. It can be reconstructed by buying a call struck
at $50 and selling one struck at $100. In Figure 1.5 we have given an example of a
‘butterfly option’, which consists of a long position in a call with strike $50, a short
position in two calls with strike $100 and another long position in a call with strike
$150
147

Asset Price
$0
$50
$100
$150
$200
Payoff
-$100
-$50
$0
Figure C.1:
The payofffunction of a short position in a put with a strike of $100 as a
function of the price of the underlying asset.
Section 2
1. We want to show that if a dealer offers a forward rate of Ft < ˜St then an arbitrageur
can make a sure profit. To this end, in figure C.2 an analogous trading strategy to
the one given for the case Ft > ˜St is described. The strategy allows an arbitrageur to
start with nothing, but to end with a guaranteed positive amount in a sterling bank
account. The final value of the sterling bank account is greater than zero, which
implies that an arbitrageur following this strategy can make a risk-free profit.
2. We want to calculate the forward exchange rate for an initial rate of $1.60, and
interest rates of r = 10% and ρ = 8%. From equation (2.4), we see that that the
forward exchange rate is
˜St
=
$(1.60) exp[(0.1 −0.08)2]
=
$1.67.
(C.12)
3. We want to calculate the forward rate for a situation where the sterling interest rate
follows the time dependent relation ρ(t) = a + bt. However, we can proceed just as
in the time independent case, and simply equate the results obtained by following
the dollar investment and forward buying strategies of chapter 2. Starting with n
units of sterling, the dollar investment route yields nS0 exp(rt) dollars, while the
forward buying route has a final value of n ˜St exp(at + bt2/2) dollars. Equating the
two yields
˜St = S0e(r−a)t−1
2 bt2.
(C.13)
148

Arbitrage Strategy II:
1. Borrow n units of sterling.
2. Convert the sterling at the spot rate S0 into nS0 dollars. Place
these dollars into a dollar bank account, earning interest at the rate
r. Contract to sell nS0ert dollars forward at time t at the rate Ft
(assumed < ˜St).
3. At time t, the value of the dollar bank account is nS0ert, while
the sterling position is −neρt.
4. Sell nS0ert dollars at the contracted forward rate Ft, which gives
nS0ert/Ft pounds. After the arbitrageur repays the sterling loan,
with interest, the balance in the sterling account is
nS0ert
Ft
−neρt
=
neρt
Ft
(S0e(r−ρ)t −Ft)
=
neρt
Ft
( ˜St −Ft)
(C.11)
Figure C.2:
Arbitrage Strategy II
For a two-year forward purchase, we see that
˜S2 = $(1.60) exp[(0.1 −0.8)2 −1
20.0122] = $1.63
Note that this is lower than the forward exchange rate of exercise 2.2. For the
four-year forward purchase, the rate is
˜S4 = $(1.60) exp[(0.1 −0.8)4 −1
20.0142] = $1.6
which is coincidentally the initial rate.
Section 3
1. We want to use a simple arbitrage argument to show that the basic stake S0 and
the payoffvalues U and D satisfy U > S0 > D. Without loss of generality we can
assume that U > D. If U = D, then there is no point tossing the coin, and hence no
point betting. If S0 ≥U, then by placing a short bet an arbitrageur could guarantee
to not lose any money and to potentially make some, since the two possible payoffs,
S0 −U and S0 −D, are both non-negative. Similarly if S0 ≤D, then the payoffs
from a standard bet, U −S0 and D −S0 are both greater than or equal to zero, and
hence the arbitrageur would not have anything to lose by betting. Thus, we must
have D < S0 < U.
149

