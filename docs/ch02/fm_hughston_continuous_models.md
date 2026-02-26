# Continuous-Time Models & Stochastic Calculus

!!! info "Source"
    **Financial Mathematics: An Introduction to Derivatives Pricing** by Lane P. Hughston and Christopher J. Hunter, King's College London, 2000.
    These notes are used for educational purposes.

## Continuous-Time Models

11
Continuous Time Models
The binomial model for asset price movements suffers from some defects, of
which the most serious, from our point of view, is that in order for it to be
realistic the model must have a very large number of time steps. While for a
computer this presents less of a problem, actually evaluating the derivative
using equation (7.11) becomes a labourious and time-consuming procedure.
We can alleviate this to a certain extent, by moving from a discrete time
model to one in which time is treated as a continuous variable.
In this chapter we begin by our look at continuous time models of the fi-
nancial markets by introducing an elementary ‘Wiener model’ for asset prices
and exploring a few of its characteristics.
11.1
The Wiener Model
The simplest continuous time model for an asset price is the basic log-normal
or Wiener model. This model can be used to a reasonable approximation
to fit actual asset movements over limited time periods.
The asset price
movements are driven both by a deterministic ‘trend’ or drift, and a random
motion. The strength of the random component of the motion is called the
volatility of the process. From actual asset price data, it is evident that, at
least to a first approximation, the random motions are uncorrelated, that
is, the market has no memory of its previous behaviour. More advanced
models of the financial markets may take into account correlations between
motions of the asset at one time and other, but little is really understood on
this score. The Wiener model has the significant advantage over most other
models in that it is simple enough that in many calculations we can obtain
explicit ‘closed form’ results.
However, we are not going to do anything with only words, so it is now
time to write down some formulae. Analogous to the stochastic processes
that we studied in the discrete time case, we can define a continuous time
stochastic process as a family of random variables indexed by a continuous
time parameter t. In the elementary Wiener model the asset price St is a
stochastic process that evolves in time based on the following formula
St = S0eµteσWt−1
2σ2t.
(11.1)
Here S0, µ and σ are constants: S0 is the initial stock price, µ is the drift
and σ is the volatility. The Wiener process Wt is the source of ‘randomness’
68

or ‘noise’ in the asset price movement. As we shall demonstrate in a later
chapter it can be expressed as the limit of a lattice tree model.
But what is the Wiener process Wt and what are its properties? Well, it
is a stochastic process beginning at time 0 that satisfies
1. The initial value is zero: W0 = 0.
2. At each time t, Wt is a normally distributed random variable with mean
0 and variance t.
3. Wt has independent increments.
That is, for a < b < c < d, the
difference between the values of Wt at two times, such as Wb −Wa and
Wd −Wc, are independent random variables.
If a stochastic process has these three properties, then we say that it is
a Wiener process or, equivalently, it is a simple Brownian motion.
The
Wiener process is a very rich object of mathematical interest, with numerous
important applications in finance.
An example Wiener process is shown in figure 11.1. Note that at any
time Wt has an equal likelihood of being positive or negative, but the spread
(variance) increases over time. If we add to the Wiener process a constant de-
terministic drift of the form µt then the resulting process will have a nonzero
expectation value, as illustrated in figure 11.2.
11.2
The Normal Distribution
Before we try and do too much with the Wiener process it is probably worth
spending some time recalling some facts about the normal distribution. The
probability distribution of a stochastic process at any particular time t is
called the marginal distribution, so we say that a Wiener process has a ‘nor-
mal’ marginal distribution. We refer to any random variable that is normally
distributed with mean m and variance V as an N(m, V ) random variable.
Hence if X is an N(m, V ) random variable we have
Prob[a<X <b] =
1
√
2πV
Z b
a exp
"
−(x −m)2
2V
#
dx.
(11.2)
Since the Wiener process Wt has an N(0, t) marginal distribution, it is char-
acterized by the following probability law:
Prob[a < Wt < b] =
1
√
2πt
Z b
a exp
"
−x2
2t
#
dx.
(11.3)
69

Time
0
0.25
0.5
1.0
Wiener Process
-0.25
0
0.25
0.5
Figure 11.1:
A Wiener process.
Time
0
0.25
0.75
1.0
Wiener Process
-0.25
0
0.25
0.5
0.75
Figure 11.2:
A Wiener process with an added drift term of 25% i.e. of the form Wt+.25t.
The dashed line represents the contribution from the drift term. The underlying Wiener
process is the same in both this figure and figure 11.1.
70

How about the difference between the Wiener process at two different times,
Wa+b −Wb? In the definition of Wt we required that this be an independent
random variable. In fact, it turns out to be a N(0, b) random variable, which
will be very important for some of our calculations.
Exercise 11.1 Verify that Wa+b −Wa is an N(0, b) random variable.
A useful formula to define is the cumulative normal distribution function
N(x)
N(x) =
1
√
2π
Z x
−∞exp
·
−1
2ξ2
¸
dξ.
(11.4)
Later, we will be able to express the price of call and put options in terms of
N(x). For now, we can use the cumulative distribution in order to describe
a Wiener process Wt,
Prob[Wt < b]
=
1
√
2πt
ξ=b
Z
ξ=−∞
e−ξ2
2t dξ
=
1
√
2π
η=b/
√
t
Z
η=−∞
e−1
2 η2dη
=
N(b/
√
t)
(11.5)
where we made the substitution ξ = η
√
t in going from the first to second
line.
We are now in a position where we can, at least heuristically, understand
the drift µ and volatility σ of the Wiener model for an asset price process,
given by equation (11.1). In order to interpret the drift, we need the following
result.
Lemma 11.1 Let X be an N(m, V ) random variable. Then
E[exp(αX)] = exp
µ
αm + 1
2α2V
¶
.
(11.6)
Proof The density function ρm,V (x) for an N(m, V ) random variable is
ρm,V (x) =
1
√
2πV exp
Ã
−(x −m)2
2V
!
.
(11.7)
71

Thus, the expected value is
E[exp(αX)] =
x=∞
Z
x=−∞
1
√
2πV exp
"
αx −(x −m)2
2V
#
dx
(11.8)
A straightforward calculation that involves ‘completing the square’ then gives
the desired result.
An immediate corollary of this result is that
E[exp(σWt)] = exp
µ1
2σ2t
¶
,
(11.9)
from which we conclude that the expected value of the Wiener process is
E[St]
=
E
·
S0 exp
µ
µt −1
2σ2t + σWt
¶¸
=
S0 exp
µ
µt −1
2σ2t
¶
E [exp (σWt)]
=
S0 exp(µt).
(11.10)
Since E[St]/S0 = eµt, we say that µ is the rate of return on an investment
in the asset St with initial price S0. Thus, the drift parameter controls the
expected value of the asset price in the future. However, rather surprisingly,
it will turn out that the call and put option prices that we will derive are
independent of the value of the drift, that is, they do not depend on how we
expect the asset price will move.
The volatility, on the other hand, measures the ‘response’ of St to the
movements in the Wiener process Wt. That is, the larger the volatility, the
more randomness that is introduced into the model, as shown in figures 11.3
and 11.4. It is the volatility which will play the most important role in option
pricing because it controls the randomness that we need to try and eliminate.
Exercise 11.2 Calculate the variance of the asset price process St.
Note that since the logarithm of the asset price is given by
ln St = ln S0 + (µ −1
2σ2)t + σWt,
(11.11)
72


## Stochastic Calculus

Time
0
0.25
0.75
1.0
Asset Price
$100
$150
$200
$250
$300
Figure 11.3:
A Wiener model asset price processes, driven by equation (11.1), with an
initial price of S0 = $100, a drift of µ = 1 and a volatility of σ = 0.5. The dashed is line
is the expected value E[St] = S0eµt.
it follows that ln St is normally distributed with mean ln S0 + (µ −1
2σ2)t and
variance σ2t, which is why our basic model is sometimes called the log-normal
model. This model is also sometimes called ‘geometric Brownian motion with
drift’.
Another useful property of Brownian motion is the fact that
E[(Wt −Ws)2] = t −s,
(11.12)
which as we shall demonstrate below, follows from the independent incre-
ments property. Using W0 = 0, we can write
Wt = (Wt −Ws) + (Ws −W0),
(11.13)
and after squaring both sides we have
W 2
t = (Wt −Ws)2 + (Ws −W0)2 + 2(Wt −Ws)(Ws −W0).
(11.14)
Taking expectations yields
E[W 2
t ] = E[(Wt −Ws)2] + E[W 2
s ] + 0,
(11.15)
73

Time
0
0.5
0.75
1.0
Asset Price
$100
$150
$200
$250
$300
Figure 11.4:
A Wiener model asset price processes, driven by equation (11.1), with
an initial price of S0 = $100, a drift of µ = 1 and a volatility of σ = 1.0. This plot uses
the same Wiener process as figure 11.3, but the volatility is twice as large here. You can
see that the larger volatility causes the deviations from the expected value to be generally
greater. The dashed is line is the expected value E[St] = S0eµt.
where we have used the fact that
E[(Wt −Ws)(Ws −W0)]
=
E[Wt −Ws]E[Ws −W0]
=
0,
(11.16)
since the increments are independent and have zero mean.
Returning to
equation (11.15) we can evaluate the expectations to obtain
t = E[(Wt −Ws)2] + s
(11.17)
as desired.
We could also take conditional expectations of equation (11.14),
Es[W 2
t ]
=
Es[W 2
s ] + Es[(Wt −Ws)2] + 2Es[(Wt −Ws)(Ws −W0)]
=
W 2
s + t −s + 0,
(11.18)
which implies that
Es[W 2
t −t] = W 2
s −s
(11.19)
74

Note that this is the martingale property that we previously examined in the
discrete time case.
Exercise 11.3 Calculate E[Xn] for X normally distributed with mean m
and variance V for n = 1, 2, 3, 4.
Exercise 11.4 Calculate E[eαX] and Var[eαX] for X as above.
Exercise 11.5 Show that if Mt = eαWt−1
2 α2t then
Es[Mt] = Ms.
(11.20)
Exercise 11.6 Show that Mt = cos(βWt)e
1
2β2t satisfies
Es[Mt] = Ms.
(11.21)
75

12
Stochastic Calculus
We are now in a position to begin considering trading in continuous time and
to examine the situation where asset price motions are driven by a Wiener
process rather than by a discrete time model.
The idea is that at each
instant we can look at the Wiener process Wt and study its change dWt at
that instant, which, intuitively can be thought of as moving slightly up or
down with equal probability.
For the asset price St we can hypothesize that the change in its value is
given by a so-called ‘stochastic differential equation’ of the form
dSt
St
= µtdt + σtdWt.
(12.1)
This says that the infinitesimal change dSt in the asset price at time t, as a
percentage of the value St, is given by a drift term µtdt and a ‘fluctuation’
or small movement upwards or downwards given by σtdWt. We call µt the
drift at time t, and σt the volatility at time t. For elementary applications we
take µ and σ to be constant. This is often called the ‘Black-Scholes’ world.
The solution of equation (12.1) is given by the Wiener model that we looked
at in the previous chapter,
St = S0eµt+σWt−1
2 σ2t,
(12.2)
as we shall show later.
Our first goal is to make sense of (12.1) mathematically, and to introduce
the tools necessary to work with such expressions involving the Wiener pro-
cess. This will enable us to see, for example, why (12.2) is the solution of
(12.1). The main tool that we require is the so-called stochastic calculus or
Ito calculus. Our approach will be to build this up in an intuitive way, and
then to backtrack and attend to details and more precise definitions.
A closely related idea to stochastic calculus is the stochastic integral. The
integral of a process with respect to a Brownian motion is defined to be
Z b
a XtdWt = lim
N→∞
N
X
i=0
Xti(Wti+1 −Wti),
(12.3)
where the ti are some partition of the interval [a, b]. The stochastic integral
has a natural interpretation in terms of trading strategies. In particular, if
76

St is an asset price, then a trading strategy φu is a random process that says
what the holding in the asset is at time u. Then
Vt = V0 +
Z t
0 φudSu
(12.4)
represents the value at time t of an investment portfolio based on holdings
in the given asset, where V0 is the initial value of the portfolio, and φu is
the trading strategy. The term φudSu represents the infinitesimal gain (or
loss) the portfolio makes at time u when the asset moves up (or down) by
the amount dSu. More fully, we can write
Vt = V0 +
Z t
0 φuSuµudu +
Z t
0 φuSuσudWu,
(12.5)
where we have substituted the expression for dSu in from equation (12.1).
The trading strategy φu can, in principle, be deterministic, but generally is
itself also a random process, which depends on how events have played out so
far. As in the discrete time case, we will be interested in deriving a hedging
strategy that allows us to eliminate risk and generate a guaranteed return.
The main tool that we require is Ito’s Lemma, which says that if the
random process Xt satisfies
dXt = µtdt + σtdWt
(12.6)
and if f(Xt) has continuous second derivatives as a function f(x), then the
process ft = f(Xt) satisfies
df(Xt) = ∂f
∂Xt
dXt + 1
2
∂2f
∂X2
t
(dXt)2,
(12.7)
where (dXt)2 is interpreted according to the rules
(dt)2 = 0,
dtdWt = 0,
and
(dWt)2 = dt.
(12.8)
Thus (dXt)2 = σ2
t dt, and we have
df(Xt) =
Ã
µt
∂f
∂Xt
+ 1
2σ2
t
∂2f
∂X2
t
!
dt + σt
∂f
∂Xt
dWt.
(12.9)
77

This result has numerous applications. For example, suppose that Xt is a
process that satisfies the stochastic differential equation (12.6). What is the
differential of f(Xt) = exp Xt? According to the Ito rule we have
deXt
=
Ã
µt
∂eXt
∂Xt
+ 1
2σ2
t
∂2eXt
∂X2
t
!
dt + σt
∂eXt
∂Xt
dWt.
=
eXt
·
(µt + 1
2 −sigma2
t)dt + σtdWt
¸
(12.10)
Exercise 12.1 Use Ito’s lemma to show that equation (12.2) is a solution
of (12.1) when µ and σ are constant.
Exercise 12.2 Find the stochastic derivatives of the following processes
1. Xt = W 2
t −t
2. Xt = W 3
t −3tWt
3. Xt = W 4
t −6tW 2
t + 3t2
where Wt is a Wiener process. What do these processes have in common?
Exercise 12.3 Use Ito’s lemma to show that if Zt = XtYt, then
dZt = XtdYt + YtdXt + dXtdYt
(12.11)
Verify this in the case Xt = Wt and Yt = W 2
t where Wt is the Wiener process.
Hint: consider (Xt + Yt)2 −X2
t −Y 2
t .
Exercise 12.4 Use Ito’s lemma to show that for processes Xt, Yt we have
d(X
Y ) = X
Y
"dX
X −dY
Y
+ (dY )2
Y 2
−dXdY
XY
#
(12.12)
78

13
Arbitrage Argument
It is now time to make a first attempt at deriving the Black-Scholes formula
for the value of a call option. In fact, we shall derive the Black-Scholes partial
differential equation, which is valid for any derivative. However, it is only
in specific simple cases, such as that of a call or put option with constant
‘market parameters’, where an explicit solution can be found.
13.1
Derivation of the No-Arbitrage Condition
Consider a financial market that consists of one basic asset and a money
market account. Suppose that the underlying asset has a stochastic price
process St with dynamics
dSt = µtStdt + σtStdWt,
(13.1)
where µt is the drift and σt is the volatility. Later we shall specialize to the
case where µt and σt are constant, but for the moment we shall allow these
processes to be fairly general, depending on the ‘history’ of Wt between 0
and t. The money market account or bond process Bt satisfies the stochastic
differential equation
dBt = rtBtdt,
(13.2)
where rt is the instantaneous risk-free interest rate or ‘short rate’. As in the
case of the drift and volatility, for now we will only assume that the short
rate is adapted to the Brownian motion Wt, but eventually we will take it to
be constant.
In addition to the underlying asset and the bond, we also have an option
on St, with price Ct at time t. In fact, for the moment we may suppose
that Ct is a fairly general European-style derivative. It is therefore entirely
specified by a maturity T and a payofffunction CT. Eventually we shall
calculate the initial price for the payout
C(ST) = max(ST −K, 0),
(13.3)
that is, a call option. The payofffunction of a call option was illustrated in
figure 1.1.
What is the stochastic differential equation satisfied by Ct?
We shall
assume that Ct is ‘driven’ by the same randomness that affects St, that is,
79

the Wiener process Wt. Hence the derivative price has the dynamics
dCt = µC
t Ctdt + σC
t CtdWt,
(13.4)
where µC
t and σC
t are respectively the drift and volatility of the derivative
price.
Note that the stochastic process Ct does not really need to be a
derivative at all! As remarked above, the only condition that we have actually
required is that the random part of the ‘derivative’ motion is driven by the
same Wiener process Wt that generates the randomness in the asset price
process St. It turns out that the drifts and volatilities for any two processes
that are driven by the same Brownian motion are not independent. That this
result follows from an arbitrage argument should not be too surprising—by
going long one process and short the other we can eliminate the common
source of uncertainty and hence generate a guaranteed return. Any portfolio
with a guaranteed return immediately implies that an arbitrage argument is
waiting to happen.
Suppose that an arbitrageur wants to make a risk-free profit (after all,
who doesn’t?) by investing in the asset and derivative. Let φt be the trading
strategy for the underlying asset, that is, φt tells us how much of the asset that
we own at time t. It is the value of the trading strategy that will eventually
be determined by the no arbitrage argument.
A self-financing trading strategy is a trading strategy that has no external
cash-flow. That is, any changes in the value of the portfolio are entirely due
to changes in the value of the underlying assets and not due to money being
put in or taken out of the portfolio in order to fund asset sales or purchases.
For example, if we have a single asset with price process St and trading
strategy φt, then the portfolio value is Vt = φtSt and the change in the value
of the portfolio over a short time interval [t, t + dt] is dVt = φtdSt + Stdφt.
The trading strategy is self-financing only if Stdφt = 0 because this is an
external cash-flow, whereas φtdSt is caused by a change in the value of the
asset price. Consider the constant position φt which buys one unit of stock
at time 0 and then simply holds onto it. The portfolio value is Vt = φtSt and
the change in the value of the portfolio is simply dVt = φtdSt. Hence φt is
self-financing. A trading strategy that is not self-financing is φt = t which
continuously buys stock. The value of the portfolio is Vt = tSt, and hence
the change in its value over a short time interval is dVt = Stdt + tdSt, which
is not equal to φtdSt. The amount Stdt is an external cash-flow that must
be added to the portfolio in order to fund the continual asset purchases.
80

In the next chapter we will look at trading strategies which consist of
positions in both an asset and a bond. In that case the value of a portfolio
with a trading strategy (φt, ψt) is Vt = φtSt + ψtBt. The change in a self-
financing strategy must be entirely due to the change in the asset and bond
prices, that is dVt = φtdSt +ψtdBt. Unlike the single asset case, we no longer
have to require that the change in the trading strategy vanishes, that is, we
can buy and sell assets and bonds, but we do require that the additional
terms that arise from these sales and purchases cancel each other in such
a way that no external cash-flow is required. For example, if we want to
increase our asset holdings φt, then the money to fund this purchase must
come from a correspondingly shorter position ψt in the bond. We can make
the trading strategy φt = t into a self-financing one by adding a bond position
of
ψt = −
Z t
0
Su
Bu
du,
(13.5)
which simply borrows the money from the bond market to pay for the pur-
chases in the asset market, which means that Stdφt + Btdψt = 0.
Self-
financing strategies are very important for arbitrage arguments because we
cannot require a portfolio that starts with no net position to end with sim-
ilarly no net value if there is an external cash-flow which adds or subtracts
money from the position.
Now back to the arbitrage argument. As in our previous examples, the
arbitrageur begins at time t with no money. He then buys one option for
Ct dollars and assumes a short position in φt units of the underlying asset.
Note that we assume that the asset can be bought and sold in any quantity.
Setting up this portfolio costs Vt = Ct −φtSt dollars, which must be funded
by a bank loan. Interest accumulates continuously on this loan at the rate
rt, so that after a small time interval dt the arbitrageur owes an additional
rtVtdt dollars to the bank.
But what is the value of φt, that is, how much of the asset are we short-
ing? Just as in the discrete time case, the ‘arbitrage strategy’ φt is chosen so
that the risk or randomness in holding the option exactly cancels the risk in
holding the asset. This is the only way to ensure the guaranteed return nec-
essary for an arbitrage argument. So what is the return on the arbitrageur’s
portfolio? Well, the value of his position at any time t is
Vt = Ct −φtSt.
(13.6)
Assuming that we do not adjust the value of φt, that is we neither buy nor
81

sell any underlying assets, then the change in the value of the portfolio Vt
over the short time interval [t, t + dt] is
dVt
=
dCt −φtdSt
=
Ct(µC
t dt + σC
t dWt) −φtSt(µtdt + σtdWt)
=
(µC
t Ct −φtµtSt)dt + (σC
t Ct −φtσtSt)dWt,
(13.7)
where we have assumed that the asset and option prices obey equations (13.1)
and (13.4) respectively. We can now fix φt by setting the coefficient of dWt
to zero. This ensures that the arbitrageur’s asset and option portfolio offers
a definite rate of return over the small time interval dt. Hence
φt = σC
t Ct
σtSt
,
(13.8)
and we call this value of φt the arbitrage strategy. We can then calculate the
change in the value of the position when the arbitrage strategy is used,
dVt
=
(µC
t Ct −φtµtSt)dt
=
Ã
µC
t −σC
t µt
σt
!
Ctdt.
(13.9)
But the arbitrageur can make a risk-free profit if the drift in equation (13.9)
yields a monetary gain greater than the interest payment rtVtdt on the loan.
This follows because at time t + dt, the value of the arbitrageur’s asset and
option portfolio is Vt +dVt, while the amount owed to the bank is Vt +rtVtdt.
Hence his net position is the risk-free amount dVt −rtVtdt. Since he started
with no money, the no arbitrage argument tells us that his final position
must also be zero, and thus
dVt = rtVtdt.
(13.10)
This implies that
dVt
=
rt(Ct −φtSt)dt
=
rt
Ã
1 −σC
t
σt
!
Ctdt,
(13.11)
where we have used the value of Vt from equation (13.6), and substituted in
the arbitrage trading strategy φt, as given by equation (13.8).
82


## Risk Analysis

Equating equations (13.9) and (13.11) we get
µC
t −σC
t µt
σt
= rt
Ã
1 −σC
t
σt
!
.
(13.12)
After some rearrangement we obtain the formula
µC
t −rt
σC
t
= µt −rt
σt
.
(13.13)
This is the general relation between µC
t , µt, σC
t , σt and rt that is required if
there is to be no arbitrage between the option and the underlying. We there-
fore call this the no arbitrage condition. Note that we have made no specific
assumptions about the form of the volatility, drift or short-rate processes, or
even what kind of derivative that we are speaking of (except that its value,
like that of St, should be determined by a knowledge of Wt between 0 and
t), so that relation (13.13) is quite general. In fact, Ct does not even need to
be a derivative, but rather it can be any price process that is driven by the
same Brownian motion as St. In economic terms (13.13) says that the rate
of return above the risk-free rate, per unit of risk, that is, volatility, has to
be the same for any two processes governed by the same random motions.
13.2
Derivation of the Black-Scholes Equation
To proceed further, we now assume that at each time t the derivative price
Ct can be specified in terms of a function Ct = C(St, t) of just the asset
price and time. This is true for a call option and many other standard types
of derivatives. The big advantage of this assumption is that it allows us to
apply Ito’s lemma to the derivative price,
dCt
=
∂Ct
∂t dt + ∂Ct
∂St
dSt + 1
2
∂2Ct
∂S2
t
(dSt)2
=
Ã∂Ct
∂t + ∂Ct
∂St
µtSt + 1
2
∂2Ct
∂S2
t
S2
t σ2
t
!
dt + ∂Ct
∂St
StσtdWt. (13.14)
Comparing the terms from this result with the coefficients of dt and dWt in
the original price process (13.4)
dCt = µC
t Ctdt + σC
t Ctdt,
(13.15)
83

we deduce that
µC
t Ct = ∂Ct
∂t + ∂Ct
∂St
µtSt + 1
2
∂2Ct
∂S2
t
S2
t σ2
t ,
(13.16)
and
σC
t Ct = ∂Ct
∂St
Stσt.
(13.17)
If we then use these expressions to substitute for µC
t and σC
t in the no arbi-
trage condition (13.13) obtained earlier, we get
∂C
∂t + ∂C
∂St
µtSt + 1
2
∂2C
∂S2
t
S2
t σ2
t −rtC = (µt −rt) ∂C
∂St
St.
(13.18)
Note that the terms involving µt on the right and left miraculously cancel,
and we are left with the equation
∂C
∂t + 1
2
∂2C
∂S2 S2
t σ2
t = rt
Ã
Ct −∂C
∂S St
!
.
(13.19)
This is the famous Black-Scholes partial differential equation for the price of
a derivative. Note that it is independent of the drift of the asset price and
both the drift and volatility of the derivative price.
Exercise 13.1 We can also derive the Black-Scholes equation in the fol-
lowing equivalent manner. Begin with nothing and take the position Vt =
Ct −φtSt −ψtBt. Then use an arbitrage argument on the value of the port-
folio at time t + dt, where the stock and bond holdings are kept fixed over the
time interval [t, t + dt].
To value a derivative we need to impose a ‘boundary condition’ on the
differential equation (13.19). This will take the form of a specification of the
terminal pay-offfunction of the derivative. In the case of a call option, for
example, we want
CT = max(ST −K, 0).
(13.20)
The idea is to solve for Ct as a function of St and t for values of t less than
T. In particular, we want the value of C0, which is the initial price of the
derivative. The solution of equation (13.19) for constant values of σt, µt, and
rt, subject to the call option boundary condition, is given by
C(St, t) = e−r(T−t)[Ster(T−t)N(h+) −KN(h−)],
(13.21)
84

where
h± = ln(Ster(T−t)/K) ± 1
2σ2(T −t)
σ
√
T −t
,
(13.22)
and N(x) is the cumulative probability function for the N(0, 1) normal dis-
tribution,
N(x) =
1
√
2π
Z x
−∞e−1
2ξ2dξ.
(13.23)
One can verify that (13.21) and (13.22) do indeed solve (13.19) for constant
drift and volatilities, subject to the condition (13.20). This involves quite a
bit of calculation. In fact, there is a quicker way of getting this result, by use
of martingale arguments, which we shall look at later. This by-passes the
need for solving the differential equation (13.19). Nevertheless as a piece of
elegant mathematics it is very instructive to see how (13.19) leads to (13.21).
Form a numerical point of view, the partial differential approach is the best
way to obtain a price for an exotic derivative.
Exercise 13.2 Calculate the price for a 6-month option with a strike of
$115, if the initial cost of the asset is $100, the volatility is 20% per year and
the risk-free interest rate is 5% per year.
85

14
Replication Portfolios
We have seen that if an asset price St moves according to the process dSt =
µtStdt+σtStdWt, and if a derivative based on the asset moves according to the
process dCt = µC
t Ctdt + σC
t CtdWt, and if the money market account process
Bt satisfies dBt = rtBtdt, then to avoid arbitrage the relation (µC
t −rt)/σC
t =
(µt −rt)/σt must hold. This ensures that if we hold a portfolio Vt that is long
one derivative and short φt units of the asset, and φt is chosen so that the
return on the position is riskless, that is φt = σC
t Ct/σtSt, then this riskless
rate of return is equal to the risk-free short-rate rt.
In this chapter we shall demonstrate a complementary result, namely
that a position in the derivative can be replicated by a portfolio composed of
holdings in both the underlying asset and the money market account. Recall
that going long in the money market is equivalent to investing money at the
rate rt, while going short is the same as borrowing money at the same rate
rt.
So, how can we replicate the derivative? We begin by recalling that if
we follow the arbitrage strategy φt, then we obtain a fixed return on the
position Vt, given by dVt = rtVtdt. But this rate of return is equal to the
rate of return obtained by an investment in the money market account, as
required by the no arbitrage argument. So instead of buying the derivative
and selling φt units of the asset, that is taking the position Vt, we could
achieve the same effect by setting up a portfolio ¯Vt which simply invests ψt
in the money market account. Since we want the portfolios to have the same
value at time t, we clearly set
ψt = Vt/Bt.
(14.1)
If we hold our investment in the bond fixed, then the change in the value of
this portfolio between time t and time t + dt is
d¯Vt
=
ψtdBt
=
ψtrtBtdt
=
rtVtdt
=
dVt.
(14.2)
Thus, ¯Vt exactly replicates Vt and the two processes must therefore be equal.
But this means that
ψtBt = Ct −φtSt,
(14.3)
86


## Partial Differential Equations

and hence
Ct = ψtBt + φtSt.
(14.4)
In essence what we have done is first calculated φt using a no arbitrage
argument, and then simply defined ψt by equation (14.4).
Exercise 14.1 We want to show that the trading strategy (φt, ψt) defined by
equations (13.8) and (14.4) is self-financing.
(a) Begin by showing that
d
µCt
Bt
¶
= φtd
µ St
Bt
¶
.
(14.5)
We could, in fact, use this as a defintion of φt.
(b) Next, calculate the change in the bond position, Btdψt.
(c) Finally, use these two results to verify that
dCt = φtdSt + ψtdBt,
(14.6)
which means that the trading strategy is indeed self-financing.
This portfolio consisting of φt units of the underlying asset and ψt units of
the money market account is called the replication portfolio. Its importance
can be seen by considering the risk associated with derivatives.
Suppose
that at time 0 an investment bank sells a derivative to a client at a price C0.
Then at time T it will have to pay the client CT. This involves risk for the
bank, since, depending on the value of CT it might lose money. However, if
the C0 from the sale of the option is immediately invested to synthesize a
replication portfolio, then the value of the replication portfolio at time T will
automatically be CT, which can be paid directly to the client. Thus, there
is no risk that the bank will make a loss. Actually the bank cannot make a
profit either, unless a price somewhat greater than C0 is actually charged for
the derivative.
So, why do we need derivatives at all, if we can replicate them with an
appropriate portfolio? The reason is that the trading strategies φt and ψt
require continuous attention and re-adjustment which the client may wish to
avoid, and indeed may not have the facility to carry out efficiently.
87

The value of φt in equation (13.8) is not very practical since it is defined
in terms of two unknown volatilities σC
t and σt. A more useful expression
can be obtained from equation (14.6),
φt = ∂Ct
∂St
.
(14.7)
This tells you how much stock needs to be held at time t in order to replicate
the ‘risky’ part of the motion of Ct. Intuitively, if the underlying asset moves
by a small amount ∆St, then the first order change in the derivative price
should be (∆St)∂Ct/∂St. Hence if we are long one derivative and short φt
units of stock, then the two changes will cancel one another. The quantity
φt is generally called the ‘Delta’ of the derivative.
What is the value of the bond position in our replicating portfolio? Sub-
stituting equation (14.7) into equation (14.4), which defines ψt, we see that
ψt = 1
Bt
Ã
Ct −∂Ct
∂St
St
!
.
(14.8)
This tells you how much money needs to be invested in the money market
account when you are trying to replicate the derivative.
88

15
Solving the Black-Scholes Equation
We now want to solve the Black-Scholes equation for a general ‘European’
payoff, assuming that the drift, volatility, and interest rates are all constant.
In this case the stochastic asset price process is
dSt = µStdt + σStdWt.
(15.1)
In exercise (12.1) we verified that the solution of this stochastic differential
equation is
St = S0eµt+σWt−1
2 σ2t,
(15.2)
where S0 is the initial price of the asset. If C(St, t) is the value of a derivative
at time t which expires at time T, then in the previous two chapters we
showed that for 0 ≤t ≤T it must satisfy the Black-Scholes partial differential
∂Ct
∂t + 1
2σ2
t S2
t
∂2Ct
∂S2
t
= r
Ã
Ct −∂Ct
∂St
St
!
.
(15.3)
Our goal is to solve this equation subject to the specification of a general
payofffunction C(ST, T) = f(ST) at the expiry time T. In the event that
the derivative is a call option with payoffmax[ST −K, 0], then we can obtain
a nice analytic formula for the initial price, known as the Black-Scholes for-
mula. In the case of a more general derivative we shall demonstrate, just as in
the discrete time case, that the initial price can be expressed as a discounted
expectation of the payofffunction.
To begin with, we note that the Black-Scholes equation (15.3) has a pass-
ing similarity to the more common heat equation
∂A(x, τ)
∂τ
= 1
2σ2∂2A(x, τ)
∂x2
.
(15.4)
In fact, by a series of transformations the Black-Scholes equation can be re-
duced to the heat equation. this means that we can solve for the derivative
price by a two-step method. First, we show how to solve the heat equa-
tion (15.4) subject to a prescribed initial condition A(x, 0) = f(x). Second,
we explicitly demonstrate the transformations needed to convert the Black-
Scholes equation to the heat equation. By combining these two results we
can write down the solution to the Black-Scholes equation for a derivative
with an arbitrary European payoff.
89

15.1
Solution of the Heat Equation
Let Wτ be a standard Brownian motion. If we consider a function f(x+Wτ),
then from Ito’s lemma we see that
df(x + Wτ) = ∂f(x + Wτ)
∂Wτ
dWτ + 1
2
∂2f(x + Wτ)
∂W 2
τ
dτ.
(15.5)
Note that we want to treat x as a parameter rather than a variable, and
hence have ignored it in deriving the stochastic differential equation. If we
integrate this equation with respect to τ then we obtain
f(x + Wτ) = f(x) +
Z τ
0
∂f(x + Ws)
∂Ws
dWs + 1
2
Z τ
0
∂2f(x + Ws)
∂W 2
s
ds,
(15.6)
where we have used the fact that W0 = 0. We then notice that differentiating
f(x + Wτ) with respect to Wτ is the same as differentiating it with respect
to x, that is
∂f(x + Wτ)
∂Wτ
= ∂f(x + Wτ)
∂x
and
∂2f(x + Wτ)
∂W 2
τ
= ∂2f(x + Wτ)
∂x2
. (15.7)
This is useful because we want to derive the heat equation, which involves
derivatives with respect to a real quantity x, rather than a stochastic variable
like Wτ. Substituting these results into the equation for f(x+Wτ) we obtain
f(x + Wτ) = f(x) +
Z τ
0
∂f(x + Ws)
∂x
dWs + 1
2
Z τ
0
∂2f(x + Ws)
∂x2
ds.
(15.8)
If we take an expectation on each side of this equation, then the stochastic
integral vanishes, and we obtain
E[f(x + Wτ)] = f(x) + 1
2
Z τ
0
∂2E[f(x + Ws)]
∂x2
ds.
(15.9)
Exercise 15.1 By using the definition of a stochastic integral show that for
any well-behaved function g(Wt)
E
·Z t
0 g(Ws)dWs
¸
= 0,
(15.10)
and hence we are justified in discarding the expectation of the stochastic in-
tegral in equation (15.9).
90


## Diffusions and Derivatives

If we define the function
A(x, τ) = E[f(x + Wτ)],
(15.11)
then equation (15.9) becomes
A(x, τ) = f(x) + 1
2
Z τ
0
∂2A(x, s)
∂x2
ds.
(15.12)
Differentiating with respect to τ, we see that A(x, τ) satisfies the heat equa-
tion
∂A(x, τ)
∂τ
= 1
2
∂2A(x, τ)
∂x2
.
(15.13)
Furthermore, if we evaluate A(x, τ) at τ = 0 we see that
A(x, 0)
=
E[f(x + W0)]
=
E[f(x)]
=
f(x),
(15.14)
that is, A(x, τ) satisfies the initial condition A(x, 0) = f(x). Thus, we now
have a recipe for solving the heat equation subject to a given initial condition.
Specifically, if A(x, τ) satisfies the heat equation (15.13) and is subject to the
initial condition A(x, 0) = f(x), then
A(x, τ)
=
E[f(x + Wτ)]
=
1
√
2πτ
Z ∞
−∞f(x + ξ)e−ξ2
2τ dξ.
(15.15)
Somewhat more generally, but by an identical argument, we find that
A(x, τ) = E[f(x + σWτ)]
(15.16)
satisfies the equation
∂
∂τ A(x, τ) = 1
2σ2 ∂2
∂x2A(x, τ),
(15.17)
subject to the initial condition A(x, 0) = f(x).
Exercise 15.2 Verify that A(x, τ) as defined by equation (15.16) satisfies
the partial differential equation (15.17).
91

For fixed τ, the random variable Wτ is normally distributed with mean 0
and variance τ. We can therefore rewrite the solution (15.16) as
A(x, τ) = E[f(x + σ√τZ)],
(15.18)
where Z is a standard N(0, 1) random variable. Explicitly writing out the
expectation we have
A(x, τ) =
1
√
2π
Z ∞
−∞f(x + σ√τξ)e−1
2 ξ2dξ.
(15.19)
Once we have transformed the Black-Scholes equation into the heat equation
we will be able to use this result to calculate solutions of the Black-Scholes
equation, and hence derivative prices.
15.2
Reduction of the Black-Scholes Equation to the
Heat Equation
Armed with this result we return to the Black-Scholes equation (15.3) and
make a series of crafty transformations in order to reduce it to the heat
equation (15.17). Proceed as follows:
1. We need to reverse the direction of time, so that the terminal payout
of the Black-Scholes equation becomes the initial condition for the heat equa-
tion. Set C(S, t) = α(S, τ), where τ = T −t is a new time coordinate which
still runs over the same interval [0, T] as t, but in the opposite direction. The
derivative expiry time T is, of course, a constant. The time derivatives of
C(S, t) and α(S, τ) are related by
∂C
∂t = −∂α
∂τ ,
(15.20)
while all the other derivatives remain the same. Hence the Black-Scholes
equation becomes
∂α
∂τ = 1
2σ2S2 ∂2α
∂S2 + rS ∂α
∂S −rα.
(15.21)
This equation now has the ‘right’ sign for the time derivative, and has the
initial condition
α(ST, 0)
=
C(ST, T)
=
F(ST, T).
(15.22)
92

2. We now want to eliminate the rα term. We can do this by introducing a
‘discount factor’ e−rτ explicitly into the equation. Set α(S, τ) = β(S, τ)e−rτ.
The time derivative is then
∂α
∂τ =
Ã∂β
∂τ −rβ
!
e−rτ,
(15.23)
and hence equation (15.21) can be written as
∂β
∂τ = 1
2σ2S2 ∂2β
∂S2 + rS ∂β
∂S .
(15.24)
3. To proceed further, we want to write the equation in terms of the
operator S∂/∂S. This can be easily accomplished by rearranging the second
order term,
∂β
∂τ = 1
2σ2S ∂
∂S
Ã
S ∂β
∂S
!
+ (r −1
2σ2)S ∂β
∂S .
(15.25)
4.
We can simplify the operator S∂/∂S by defining the new variable
Y = ln S, and noting that
S ∂
∂S = ∂
∂Y .
(15.26)
If we then introduce the new function γ(Y, τ) = β(S, τ), we see that the
differential equation (15.25) becomes
∂γ
∂τ = 1
2σ2 ∂2γ
∂Y 2 + (r −1
2σ2) ∂γ
∂Y .
(15.27)
5. Finally, we need to get rid of the first order partial derivative. Define
X = Y + (r −1
2σ2)τ, and set A(X, τ) = γ(Y, τ). The partial derivative of γ
with respect to τ is then given by
∂γ
∂τ
=
∂A
∂τ + ∂A
∂X
∂X
∂τ
=
∂A
∂τ + ∂A
∂X (r −1
2σ2).
(15.28)
However, since
∂γ
∂Y = ∂A
∂X
(15.29)
93

it follows that if we substitute (15.28) and (15.29) into equation (15.27) then
the first order derivatives with respect to X cancel and we obtain
∂A
∂τ = 1
2σ2 ∂2A
∂X2,
(15.30)
which is the heat equation at last!
Now that we have shown that the Black-Scholes equation can be reduced
by a series of transformations to the heat equation, we would like to solve
for the derivative price C(St, t) subject to the terminal condition
C(ST, T) = F(ST),
(15.31)
where F(ST) is a prescribed function, that is, the payofffunction of the
derivative. As noted earlier, t = T corresponds to τ = 0, which is why the
terminal payofffunction of the derivative is actually an initial condition for
A(x, τ). If we follow through the various transformations made above, then
we see that the relation between C(St, t) and A(X, τ) is
C(St, t)
=
α(St, T −t)
=
β(St, T −t)e−r(T−t)
=
γ(log St, T −t)e−r(T−t)
=
A(log St + [r −σ2/2][T −t], T −t)e−r(T−t).
(15.32)
In particular the derivative payofffunction can be written as
F(ST)
=
C(ST, T)
=
A(log ST, 0).
(15.33)
Hence the initial condition on A(x, τ) at τ = 0 is
A(x, 0) = F(ex).
(15.34)
For example, in the case of a call option we have
A(x, 0) = max(ex −K, 0).
(15.35)
We can now appeal to our earlier formula (15.19) for the solution of the heat
equation with the initial condition A(x, 0) = F(ex),
A(x, τ) =
1
√
2π
Z ∞
−∞F(ex+σ√τξ)e−1
2ξ2dξ.
(15.36)
94

Using this value of A(x, τ) and the transformation (15.19) we can then write
the derivative price as
C(St, t)
=
A(log St + [r −σ2/2][T −t], T −t)e−r(T−t)
=
e−r(T−t)
√
2π
Z ∞
−∞F(Ster(T−t)+σ√τξ−1
2 σ2τ)e−1
2 ξ2dξ.
(15.37)
In particular, if we set t = 0, then we obtain the initial price of the derivative
C0 = e−rT
√
2π
Z ∞
−∞F(S0erT+σ
√
Tξ−1
2σ2T)e−1
2 ξ2dξ.
(15.38)
We see that the present value of the derivative depends on the expiry date
T, the initial asset price S0, the volatility σ, the risk-free interest rate r and
the specification of the payofffunction F(ST).
Note that, similar to the discrete case, we can write the derivative price
in terms of an expectation
C0 = e−rTE∗[F(ST)],
(15.39)
where
ST = S0erT+σW ∗
T −1
2 σ2T.
(15.40)
W ∗
T is a random variable that is normally distributed with mean zero and
variance T with respect to some new probability measure P ∗. This is the
‘risk-neutral’ measure, just as in the discrete case.
Before proceeding to the call and ut options, we can begin by pricing the
‘trivial’ derivative that simply delivers ST at time T, that is, F(ST) = ST.
The price of this derivative is
C0
=
e−rTE∗[F(ST)]
=
e−rTE∗[ST]
=
e−rTE∗[S0erT+σW ∗
T −1
2 σ2T]
=
S0e−1
2 σ2TE∗[eσW ∗
T ].
(15.41)
Using lemma 11.1 we can evaluate the expectation as
E∗[eσW ∗
T ] = e
1
2σ2T,
(15.42)
and hence see that the derivative price is imply
C0 = S0,
(15.43)
which is what we should expect.
95

Exercise 15.3 Price a forward contract with strike K. This has a payoff
function F(ST) = ST −K,
96

