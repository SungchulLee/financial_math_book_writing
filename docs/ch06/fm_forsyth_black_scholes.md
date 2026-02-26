# The Black-Scholes Equation & Risk-Neutral Pricing

!!! info "Source"
    **An Introduction to Computational Finance Without Agonizing Pain** by Peter Forsyth, 2007.
    These notes are used for educational purposes.

## The Black-Scholes Equation

Stock Price = $20
Stock Price = $22
Option Price = $1
Stock Price  = $18
Option  Price = $0
Figure 2.1: A simple case where the stock value can either be $22 or $18, with a European call option, K =
$21.
2.2
Definitions
Let’s consider some simple European put/call options. At some time T in the future (the expiry or exercise
date) the holder has the right, but not the obligation, to
• Buy an asset at a prescribed price K (the exercise or strike price). This is a call option.
• Sell the asset at a prescribed price K (the exercise or strike price). This is a put option.
At expiry time T, we know with certainty what the value of the option is, in terms of the price of the
underlying asset S,
Payoff
=
max(S −K, 0) for a call
Payoff
=
max(K −S, 0) for a put
(2.1)
Note that the payofffrom an option is always non-negative, since the holder has a right but not an obligation.
This contrasts with a forward contract, where the holder must buy or sell at a prescribed price.
2.3
A Simple Example: The Two State Tree
This example is taken from Options, futures, and other derivatives, by John Hull. Suppose the value of a
stock is currently $20. It is known that at the end of three months, the stock price will be either $22 or $18.
We assume that the stock pays no dividends, and we would like to value a European call option to buy the
stock in three months for $21. This option can have only two possible values in three months: if the stock
price is $22, the option is worth $1, if the stock price is $18, the option is worth zero. This is illustrated in
Figure 2.1.
In order to price this option, we can set up an imaginary portfolio consisting of the option and the stock,
in such a way that there is no uncertainty about the value of the portfolio at the end of three months. Since
the portfolio has no risk, the return earned by this portfolio must be the risk-free rate.
Consider a portfolio consisting of a long (positive) position of δ shares of stock, and short (negative) one
call option. We will compute δ so that the portfolio is riskless. If the stock moves up to $22 or goes down
to $18, then the value of the portfolio is
Value if stock goes up
=
$22δ −1
Value if stock goes down
=
$18δ −0
(2.2)
So, if we choose δ = .25, then the value of the portfolio is
Value if stock goes up
=
$22δ −1 = $4.50
Value if stock goes down
=
$18δ −0 = $4.50
(2.3)
So, regardless of whether the stock moves up or down, the value of the portfolio is $4.50. A risk-free portfolio
must earn the risk free rate. Suppose the current risk-free rate is 12%, then the value of the portfolio today
must be the present value of $4.50, or
4.50 × e−.12×.25
=
4.367
The value of the stock today is $20. Let the value of the option be V . The value of the portfolio is
20 × .25 −V
=
4.367
→
V = .633
2.4
A hedging strategy
So, if we sell the above option (we hold a short position in the option), then we can hedge this position in
the following way. Today, we sell the option for $.633, borrow $4.367 from the bank at the risk free rate (this
means that we have to pay the bank back $4.50 in three months), which gives us $5.00 in cash. Then, we
buy .25 shares at $20.00 (the current price of the stock). In three months time, one of two things happens
• The stock goes up to $22, our stock holding is now worth $5.50, we pay the option holder $1.00, which
leaves us with $4.50, just enough to pay offthe bank loan.
• The stock goes down to $18.00. The call option is worthless. The value of the stock holding is now
$4.50, which is just enough to pay offthe bank loan.
Consequently, in this simple situation, we see that the theoretical price of the option is the cost for the seller
to set up portfolio, which will precisely pay offthe option holder and any bank loans required to set up the
hedge, at the expiry of the option. In other words, this is price which a hedger requires to ensure that there
is always just enough money at the end to net out at zero gain or loss. If the market price of the option
was higher than this value, the seller could sell at the higher price and lock in an instantaneous risk-free
gain. Alternatively, if the market price of the option was lower than the theoretical, or fair market value, it
would be possible to lock in a risk-free gain by selling the portfolio short. Any such arbitrage opportunities
are rapidly exploited in the market, so that for most investors, we can assume that such opportunities are
not possible (the no arbitrage condition), and therefore that the market price of the option should be the
theoretical price.
Note that this hedge works regardless of whether or not the stock goes up or down. Once we set up this
hedge, we don’t have a care in the world. The value of the option is also independent of the probability that
the stock goes up to $22 or down to $18. This is somewhat counterintuitive.
2.5
Brownian Motion
Before we consider a model for stock price movements, let’s consider the idea of Brownian motion with drift.
Suppose X is a random variable, and in time t →t + dt, X →X + dX, where
dX = αdt + σdZ
(2.4)
where αdt is the drift term, σ is the volatility, and dZ is a random term. The dZ term has the form
dZ = φ
√
dt
(2.5)
where φ is a random variable drawn from a normal distribution with mean zero and variance one (φ ∼N(0, 1),
i.e. φ is normally distributed).
If E is the expectation operator, then
E(φ) = 0
E(φ2) = 1 .
(2.6)
Now in a time interval dt, we have
E(dX)
=
E(αdt) + E(σdZ)
=
αdt ,
(2.7)
and the variance of dX, denoted by V ar(dX) is
V ar(dX)
=
E([dX −E(dX)]2)
=
E([σdZ]2)
=
σ2dt .
(2.8)
Let’s look at a discrete model to understand this process more completely. Suppose that we have a
discrete lattice of points. Let X = X0 at t = 0. Suppose that at t = ∆t,
X0
→
X0 + ∆h ;
with probability p
X0
→
X0 −∆h ;
with probability q
(2.9)
where p + q = 1. Assume that
• X follows a Markov process, i.e. the probability distribution in the future depends only on where it is
now.
• The probability of an up or down move is independent of what happened in the past.
• X can move only up or down ∆h.
At any lattice point X0 + i∆h, the probability of an up move is p, and the probability of a down move is q.
The probabilities of reaching any particular lattice point for the first three moves are shown in Figure 2.2.
Each move takes place in the time interval t →t + ∆t.
Let ∆X be the change in X over the interval t →t + ∆t. Then
E(∆X)
=
(p −q)∆h
E([∆X]2)
=
p(∆h)2 + q(−∆h)2
=
(∆h)2,
(2.10)
so that the variance of ∆X is (over t →t + ∆t)
V ar(∆X)
=
E([∆X]2) −[E(∆X)]2
=
(∆h)2 −(p −q)2(∆h)2
=
4pq(∆h)2 .
(2.11)
Now, suppose we consider the distribution of X after n moves, so that t = n∆t. The probability of j up
moves, and (n −j) down moves (P(n, j)) is
P(n, j)
=
n!
j!(n −j)!pjqn−j
(2.12)
X0
X0 - ∆h
X0 - 2∆h
X0 + 2∆h
X0 + ∆h
p
q
p
q
q
p
2pq
3p
2q
3pq
X0 + 3∆h
X0 - 3∆h
Figure 2.2: Probabilities of reaching the discrete lattice points for the first three moves.
which is just a binomial distribution. Now, if Xn is the value of X after n steps on the lattice, then
E(Xn −X0)
=
nE(∆X)
V ar(Xn −X0)
=
nV ar(∆X) ,
(2.13)
which follows from the properties of a binomial distribution, (each up or down move is independent of
previous moves). Consequently, from equations (2.10, 2.11, 2.13) we obtain
E(Xn −X0)
=
n(p −q)∆h
=
t
∆t(p −q)∆h
V ar(Xn −X0)
=
n4pq(∆h)2
=
t
∆t4pq(∆h)2
(2.14)
Now, we would like to take the limit at ∆t →0 in such a way that the mean and variance of X, after a
finite time t is independent of ∆t, and we would like to recover
dX
=
αdt + σdZ
E(dX)
=
αdt
V ar(dX)
=
σ2dt
(2.15)
as ∆t →0. Now, since 0 ≤p, q ≤1, we need to choose ∆h = Const
√
∆t. Otherwise, from equation (2.14)
we get that V ar(Xn −X0) is either 0 or infinite after a finite time. (Stock variances do not have either of
these properties, so this is obviously not a very interesting case).
Let’s choose ∆h = σ
√
∆t, which gives (from equation (2.14))
E(Xn −X0)
=
(p −q) σt
√
∆t
V ar(Xn −X0)
=
t4pqσ2
(2.16)
Now, for E(Xn −X0) to be independent of ∆t as ∆t →0, we must have
(p −q) = Const.
√
∆t
(2.17)
If we choose
p −q
=
α
σ
√
∆t
(2.18)
we get
p
=
2[1 + α
σ
√
∆t]
q
=
2[1 −α
σ
√
∆t]
(2.19)
Now, putting together equations (2.16-2.19) gives
E(Xn −X0)
=
αt
V ar(Xn −X0)
=
tσ2(1 −α2
σ2 ∆t)
=
tσ2 ;
∆t →0 .
(2.20)
Now, let’s imagine that X(tn) −X(t0) = Xn −X0 is very small, so that Xn −X0 ≃dX and tn −t0 ≃dt, so
that equation (2.20) becomes
E(dX)
=
α dt
V ar(dX)
=
σ2 dt .
(2.21)
which agrees with equations (2.7-2.8). Hence, in the limit as ∆t →0, we can interpret the random walk for
X on the lattice (with these parameters) as the solution to the stochastic differential equation (SDE)
dX
=
α dt + σ dZ
dZ = φ
√
dt.
(2.22)
Consider the case where α = 0, σ = 1, so that dX = dZ =≃Z(ti) −Z(ti−1) = Zi −Zi−1 = Xi −Xi−1.
Now we can write
Z t
dZ
=
lim
∆t→0
X
i
(Zi+1 −Zi) = (Zn −Z0) .
(2.23)
From equation (2.20) (α = 0, σ = 1) we have
E(Zn −Z0)
= 0
V ar(Zn −Z0)
=
t .
(2.24)
Now, if n is large (∆t →0), recall that the binomial distribution (2.12) tends to a normal distribution. From
equation (2.24), we have that the mean of this distribution is zero, with variance t, so that
(Zn −Z0)
∼
N(0, t)
=
Z t
dZ .
(2.25)
In other words, after a finite time t,
R t
0 dZ is normally distributed with mean zero and variance t (the limit
of a binomial distribution is a normal distribution).
Recall that have that Zi −Zi−1 =
√
∆t with probability p and Zi −Zi−1 = −
√
∆t with probability q.
Note that (Zi −Zi−1)2 = ∆t, with certainty, so that we can write
(Zi −Zi−1)2 ≃(dZ)2 = ∆t .
(2.26)
To summarize
• We can interpret the SDE
dX
=
α dt + σ dZ
dZ = φ
√
dt.
(2.27)
as the limit of a discrete random walk on a lattice as the timestep tends to zero.
• V ar(dZ) = dt, otherwise, after any finite time, the V ar(Xn −X0) is either zero or infinite.
• We can integrate the term dZ to obtain
Z t
dZ
=
Z(t) −Z(0)
∼
N(0, t) .
(2.28)
Going back to our lattice example, note that the total distance traveled over any finite interval of time
becomes infinite,
E(|∆X|)
=
∆h
(2.29)
so that the the total distance traveled in n steps is
n∆h
=
t
∆t∆h
=
tσ
√
∆t
(2.30)
which goes to infinity as ∆t →0. Similarly,
∆x
∆t
=
±∞.
(2.31)
Consequently, Brownian motion is very jagged at every timescale. These paths are not differentiable, i.e. dx
dt
does not exist, so we cannot speak of
E(dx
dt )
(2.32)
but we can possibly define
E(dx)
dt
.
(2.33)
2.6
Geometric Brownian motion with drift
Of course, the actual path followed by stock is more complex than the simple situation described above.
More realistically, we assume that the relative changes in stock prices (the returns) follow Brownian motion
with drift. We suppose that in an infinitesimal time dt, the stock price S changes to S + dS, where
dS
S = µdt + σdZ
(2.34)
0
4
8
12
Time (years)
100
300
500
700
900
1000
Asset Price ($)
Risk Free
Return
Low Volatility Case
σ = .20 per year
2
6
10
Time (years)
100
300
500
700
900
1000
Asset Price ($)
Risk Free
Return
High Volatility Case
σ = .40 per year
Figure 2.3: Realizations of asset price following geometric Brownian motion. Left: low volatility case; right:
high volatility case. Risk-free rate of return r = .05.
where µ is the drift rate, σ is the volatility, and dZ is the increment of a Wiener process,
dZ
=
φ
√
dt
(2.35)
where φ ∼N(0, 1).
Equations (2.34) and (2.35) are called geometric Brownian motion with drift.
So,
superimposed on the upward (relative) drift is a (relative) random walk. The degree of randomness is given
by the volatility σ. Figure 2.3 gives an illustration of ten realizations of this random process for two different
values of the volatility. In this case, we assume that the drift rate µ equals the risk free rate.
Note that
E(dS)
=
E(σSdZ + µSdt)
=
µSdt
since E(dZ) = 0
(2.36)
and that the variance of dS is
V ar[dS]
=
E(dS2) −[E(dS)]2
=
E(σ2S2dZ2)
=
σ2S2dt
(2.37)
so that σ is a measure of the degree of randomness of the stock price movement.
Equation (2.34) is a stochastic differential equation. The normal rules of calculus don’t apply, since for
example
dZ
dt
=
φ 1
√
dt
→∞as dt →0 .
The study of these sorts of equations uses results from stochastic calculus. However, for our purposes, we
need only one result, which is Ito’s Lemma (see Derivatives: the theory and practice of financial engineering,
by P. Wilmott). Suppose we have some function G = G(S, t), where S follows the stochastic process equation
(2.34), then, in small time increment dt, G →G + dG, where
dG
=

µS ∂G
∂S + σ2S2
∂2G
∂S2 + ∂G
∂t

dt + σS ∂G
∂S dZ
(2.38)
An informal derivation of this result is given in the following section.
2.6.1
Ito’s Lemma
We give an informal derivation of Ito’s lemma (2.38). Suppose we have a variable S which follows
dS = a(S, t)dt + b(S, t)dZ
(2.39)
where dZ is the increment of a Weiner process.
Now since
dZ2
=
φ2dt
(2.40)
where φ is a random variable drawn from a normal distribution with mean zero and unit variance, we have
that, if E is the expectation operator, then
E(φ) = 0
E(φ2) = 1
(2.41)
so that the expected value of dZ2 is
E(dZ2) = dt
(2.42)
Now, it can be shown (see Section 6) that in the limit as dt →0, we have that φ2dt becomes non-stochastic,
so that with probability one
dZ2 →dt
as dt →0
(2.43)
Now, suppose we have some function G = G(S, t), then
dG = GSdS + Gtdt + GSS
dS2
+ ...
(2.44)
Now (from (2.39) )
(dS)2
=
(adt + b dZ)2
=
a2dt2 + ab dZdt + b2dZ2
(2.45)
Since dZ = O(
√
dt) and dZ2 →dt, equation (2.45) becomes
(dS)2 = b2dZ2 + O((dt)3/2)
(2.46)
or
(dS)2 →b2dt as dt →0
(2.47)
Now, equations(2.39,2.44,2.47) give
dG
=
GSdS + Gtdt + GSS
dS2
+ ...
=
GS(a dt + b dZ) + dt(Gt + GSS
b2
2 )
=
GSb dZ + (aGS + GSS
b2
2 + Gt)dt
(2.48)
So, we have the result that if
dS = a(S, t)dt + b(S, t)dZ
(2.49)
and if G = G(S, t), then
dG = GSb dZ + (a GS + GSS
b2
2 + Gt)dt
(2.50)
Equation (2.38) can be deduced by setting a = µS and b = σS in equation (2.50).
2.6.2
Some uses of Ito’s Lemma
Suppose we have
dS = µdt + σdZ .
(2.51)
If µ, σ = Const., then this can be integrated (from t = 0 to t = t) exactly to give
S(t) = S(0) + µt + σ(Z(t) −Z(0))
(2.52)
and from equation (2.28)
Z(t) −Z(0)
∼
N(0, t)
(2.53)
Note that when we say that we solve a stochastic differential equation exactly, this means that we have
an expression for the distribution of S(T).
Suppose instead we use the more usual geometric Brownian motion
dS = µSdt + σSdZ
(2.54)
Let F(S) = log S, and use Ito’s Lemma
dF
=
FSSσdZ + (FSµS + FSS
σ2S2
+ Ft)dt
=
(µ −σ2
2 )dt + σdZ ,
(2.55)
so that we can integrate this to get
F(t) = F(0) + (µ −σ2
2 )t + σ(Z(t) −Z(0))
(2.56)
or, since S = eF ,
S(t) = S(0) exp[(µ −σ2
2 )t + σ(Z(t) −Z(0))] .
(2.57)
Unfortunately, these cases are about the only situations where we can exactly integrate the SDE (constant
σ, µ).
2.6.3
Some more uses of Ito’s Lemma
We can often use Ito’s Lemma and some algebraic tricks to determine some properties of distributions. Let
dX
=
a(X, t) dt + b(X, t) dZ ,
(2.58)
then if G = G(X), then
dG
=

aGX + Gt + b2
2 GXX

dt + GXb dZ .
(2.59)
If E[X] = ¯X, then (b(X, t) and dZ are independent)
E[dX]
=
d E[S] = d ¯X
=
E[a dt] + E[b] E[dZ]
=
E[a dt] ,
(2.60)
so that
d ¯X
dt
=
E[a] = ¯a
¯X = E
Z t
a dt

.
(2.61)
Let ¯G = E[(X −¯X)2] = var(X), then
d ¯G
=
E [dG]
=
E[2(X −¯X)a −2(X −¯X)¯a + b2] dt + E[2b(X −¯X)]E[dZ]
=
E[b2 dt] + E[2(X −¯X)(a −¯a) dt] ,
(2.62)
which means that
¯G = var(X) = E
Z t
b2 dt

+ E
Z t
2(a −¯a)(X −¯X) dt

.
(2.63)
In a particular case, we can sometimes get more useful expressions. If
dS
=
µS dt + σS dZ
(2.64)
with µ, σ constant, then
E[dS]
=
d ¯S = E[µS] dt
=
µ ¯S dt ,
(2.65)
so that
d ¯S
=
µ ¯S dt
¯S
=
S0eµt .
(2.66)
Now, let G(S) = S2, so that E[G] = ¯G = E[S2], then (from Ito’s Lemma)
d ¯G
=
E[2µS2 + σ2S2] dt + E[2S2σ]E[dZ]
=
E[2µS2 + σ2S2] dt
=
(2µ + σ2) ¯G dt ,
(2.67)
so that
¯G
=
¯G0e(2µ+σ2)t
E[S2] = S2
0e(2µ+σ2)t .
(2.68)
From equations (2.66) and (2.68) we then have
var(S)
=
E[S2] −(E[S])2
=
E[S2] −¯S2
=
S2
0e2µt(eσ2t −1)
=
¯S2(eσ2t −1) .
(2.69)
One can use the same ideas to compute the skewness, E[(S −¯S)3]. If G(S) = S3 and ¯G = E[G(S)] = E[S3],
then
d ¯G
=
E[µS · 3S2 + σ2S2/2 · 3 · 2S] dt + E[3S2σS]E[dZ]
=
E[3µS3 + 3σ2S3]
=
3(µ + σ2) ¯G ,
(2.70)
so that
¯G
=
E[S3]
=
S3
0e3(µ+σ2)t .
(2.71)
We can then obtain the skewness from
E[(S −¯S)3]
=
E[S3 −2S2 ¯S −2S ¯S2 + ¯S3]
=
E[S3] −2 ¯SE[S2] −¯S3 .
(2.72)
Equations (2.66, 2.68, 2.71) can then be substituted into equation (2.72) to get the desired result.
2.7
The Black-Scholes Analysis
Assume
• The stock price follows geometric Brownian motion, equation (2.34).
• The risk-free rate of return is a constant r.
• There are no arbitrage opportunities, i.e. all risk-free portfolios must earn the risk-free rate of return.
• Short selling is permitted (i.e. we can own negative quantities of an asset).
Suppose that we have an option whose value is given by V = V (S, t). Construct an imaginary portfolio,
consisting of one option, and a number of (−(αh)) of the underlying asset. (If (αh) > 0, then we have sold
the asset short, i.e. we have borrowed an asset, sold it, and are obligated to give it back at some future
date).
The value of this portfolio P is
P = V −(αh)S
(2.73)
In a small time dt, P →P + dP,
dP = dV −(αh)dS
(2.74)
Note that in equation (2.74) we not included a term (αh)SS. This is actually a rather subtle point, since
we shall see (later on) that (αh) actually depends on S. However, if we think of a real situation, at any
instant in time, we must choose (αh), and then we hold the portfolio while the asset moves randomly. So,
equation (2.74) is actually the change in the value of the portfolio, not a differential. If we were taking a
true differential then equation (2.74) would be
dP = dV −(αh)dS −Sd(αh)
but we have to remember that (αh) does not change over a small time interval, since we pick (αh), and
then S changes randomly. We are not allowed to peek into the future, (otherwise, we could get rich without
risk, which is not permitted by the no-arbitrage condition) and hence (αh) is not allowed to contain any
information about future asset price movements. The principle of no peeking into the future is why Ito
stochastic calculus is used. Other forms of stochastic calculus are used in Physics applications (i.e. turbulent
flow).
Substituting equations (2.34) and (2.38) into equation (2.74) gives
dP = σS
VS −(αh)

dZ +

µSVS + σ2S2
VSS + Vt −µ(αh)S

dt
(2.75)
We can make this portfolio riskless over the time interval dt, by choosing (αh) = VS in equation (2.75). This
eliminates the dZ term in equation (2.75). (This is the analogue of our choice of the amount of stock in the
riskless portfolio for the two state tree model.) So, letting
(αh) = VS
(2.76)
then substituting equation (2.76) into equation (2.75) gives
dP =

Vt + σ2S2
VSS

dt
(2.77)
Since P is now risk-free in the interval t →t + dt, then no-arbitrage says that
dP = rPdt
(2.78)
Therefore, equations (2.77) and (2.78) give
rPdt =

Vt + σ2S2
VSS

dt
(2.79)
Since
P = V −(αh)S = V −VSS
(2.80)
then substituting equation (2.80) into equation (2.79) gives
Vt + σ2S2
VSS + rSVS −rV = 0
(2.81)
which is the Black-Scholes equation. Note the rather remarkable fact that equation (2.81) is independent of
the drift rate µ.
Equation (2.81) is solved backwards in time from the option expiry time t = T to the present t = 0.
2.8
Hedging in Continuous Time
We can construct a hedging strategy based on the solution to the above equation. Suppose we sell an option
at price V at t = 0. Then we carry out the following
• We sell one option worth V . (This gives us V in cash initially).
• We borrow (S ∂V
∂S −V ) from the bank.
• We buy ∂V
∂S shares at price S.
At every instant in time, we adjust the amount of stock we own so that we always have ∂V
∂S shares. Note
that this is a dynamic hedge, since we have to continually rebalance the portfolio. Cash will flow into and
out of the bank account, in response to changes in S. If the amount in the bank is positive, we receive the
risk free rate of return. If negative, then we borrow at the risk free rate.
So, our hedging portfolio will be
• Short one option worth V .
• Long ∂V
∂S shares at price S.
• V −S ∂V
∂S cash in the bank account.
At any instant in time (including the terminal time), this portfolio can be liquidated and any obligations
implied by the short position in the option can be covered, at zero gain or loss, regardless of the value of S.
Note that given the receipt of the cash for the option, this strategy is self-financing.
2.9
The option price
So, we can see that the price of the option valued by the Black-Scholes equation is the market price of the
option at any time. If the price was higher then the Black-Scholes price, we could construct the hedging
portfolio, dynamically adjust the hedge, and end up with a positive amount at the end. Similarly, if the price
was lower than the Black-Scholes price, we could short the hedging portfolio, and end up with a positive
gain. By the no-arbitrage condition, this should not be possible.
Note that we are not trying to predict the price movements of the underlying asset, which is a random
process. The value of the option is based on a hedging strategy which is dynamic, and must be continuously
rebalanced. The price is the cost of setting up the hedging portfolio. The Black-Scholes price is not the
expected payoff.
The price given by the Black-Scholes price is not the value of the option to a speculator, who buys and
holds the option. A speculator is making bets about the underlying drift rate of the stock (note that the
drift rate does not appear in the Black-Scholes equation). For a speculator, the value of the option is given
by an equation similar to the Black-Scholes equation, except that the drift rate appears. In this case, the
price can be interpreted as the expected payoffbased on the guess for the drift rate. But this is art, not
science!
2.10
American early exercise
Actually, most options traded are American options, which have the feature that they can be exercised at
any time. Consequently, an investor acting optimally, will always exercise the option if the value falls below
the payoffor exercise value. So, the value of an American option is given by the solution to equation (2.81)
with the additional constraint
V (S, t)
≥

max(S −K, 0)
for a call
max(K −S, 0)
for a put
(2.82)
Note that since we are working backwards in time, we know what the option is worth in future, and therefore
we can determine the optimal course of action.
In order to write equation (2.81) in more conventional form, define τ = T −t, so that equation (2.81)
becomes
Vτ
=
σ2S2
VSS + rSVS −rV
V (S, τ = 0)
=

max(S −K, 0)
for a call
max(K −S, 0)
for a put
V (0, τ)
→
Vτ = −rV
V (S = ∞, τ)
→

≃S
for a call
≃0
for a put
(2.83)
If the option is American, then we also have the additional constraints
V (S, τ)
≥

max(S −K, 0)
for a call
max(K −S, 0)
for a put
(2.84)
Define the operator
LV ≡Vτ −(σ2S2
VSS + rSVS −rV )
(2.85)
and let V (S, 0) = V ∗. More formally, the American option pricing problem can be stated as
LV
≥
V −V ∗
≥
(V −V ∗)LV
=
(2.86)


## Risk-Neutral Pricing

3
The Risk Neutral World
Suppose instead of valuing an option using the above no-arbitrage argument, we wanted to know the expected
value of the option. We can imagine that we are buying and holding the option, and not hedging. If we
are considering the value of risky cash flows in the future, then these cash flows should be discounted at an
appropriate discount rate, which we will call ρ (i.e. the riskier the cash flows, the higher ρ).
Consequently the value of an option today can be considered to the be the discounted future value. This
is simply the old idea of net present value. Regard S today as known, and let V (S + dS, t + dt) be the value
of the option at some future time t + dt, which is uncertain, since S evolves randomly. Thus
V (S, t)
=
1 + ρdtE(V (S + dS, t + dt))
(3.1)
where E(...) is the expectation operator, i.e. the expected value of V (S + dS, t + dt) given that V = V (S, t)
at t = t. We can rewrite equation (3.1) as (ignoring terms of o(dt), where o(dt) represents terms that go to
zero faster than dt )
ρdtV (S, t) = E(V (S, t) + dV ) −V (S, t) .
(3.2)
Since we regard V as the expected value, so that E[V (S, t)] = V (S, t), and then
E(V (S, t) + dV ) −V (S, t)
=
E(dV ) ,
(3.3)
so that equation (3.2) becomes
ρdtV (S, t) = E(dV ) .
(3.4)
Assume that
dS
S = µdt + σdZ .
(3.5)
From Ito’s Lemma (2.38) we have that
dV
=

Vt + σ2S2
VSS + µSVS

dt + σSVS dZ .
(3.6)
Noting that
E(dZ)
=
(3.7)
then
E(dV )
=

Vt + σ2S2
VSS + µSVS

dt .
(3.8)
Combining equations (3.4-3.8) gives
Vt + σ2S2
VSS + µSVS −ρV = 0 .
(3.9)
Equation (3.9) is the PDE for the expected value of an option. If we are not hedging, maybe this is the
value that we are interested in, not the no-arbitrage value. However, if this is the case, we have to estimate
the drift rate µ, and the discount rate ρ. Estimating the appropriate discount rate is always a thorny issue.
Now, note the interesting fact, if we set ρ = r and µ = r in equation (3.9) then we simply get the
Black-Scholes equation (2.81).
This means that the no-arbitrage price of an option is identical to the expected value if ρ = r and µ = r.
In other words, we can determine the no-arbitrage price by pretending we are living in a world where all
assets drift at rate r, and all investments are discounted at rate r. This is the so-called risk neutral world.
This result is the source of endless confusion. It is best to think of this as simply a mathematical fluke.
This does not have any reality. Investors would be very stupid to think that the drift rate of risky investments
is r. I’d rather just buy risk-free bonds in this case. There is in reality no such thing as a risk-neutral world.
Nevertheless, this result is useful for determining the no-arbitrage value of an option using a Monte Carlo
approach. Using this numerical method, we simply assume that
dS = rSdt + σSdZ
(3.10)
and simulate a large number of random paths. If we know the option payoffas a function of S at t = T,
then we compute
V (S, 0) = e−rT EQ(V (S, T))
(3.11)
which should be the no-arbitrage value.
Note the EQ in the above equation. This makes it clear that we are taking the expectation in the risk
neutral world (the expectation in the Q measure). This contrasts with the real-world expectation (the P
measure).
Suppose we want to know the expected value (in the real world) of an asset which pays V (S, t = T) at
t = T in the future. Then, the expected value (today) is given by solving
Vt + σ2S2
VSS + µSVS = 0 .
(3.12)
where we have dropped the discounting term. In particular, suppose we are going to receive V = S(t = T),
i.e. just the asset at t = T. Assume that the solution to equation (3.12) is V = Const. A(t)S, and we find
that
V
=
Const. Seµ(T −t) .
(3.13)
Noting that we receive V = S at t = T means that
V
=
Seµ(T −t) .
(3.14)
Today, we can acquire the asset for price S(t = 0). At t = T, the asset is worth S(t = T). Equation (3.14)
then says that
E[V (S(t = 0), t = 0)]
=
E[S(t = 0)] = S(t = 0)eµ(T )
(3.15)
In other words, if
dS
=
Sµ dt + Sσ dZ
(3.16)
then (setting t = T)
E[S] = Seµt .
(3.17)
Recall that the exact solution to equation (3.16) is (equation (2.57))
S(t) = S(0) exp[(µ −σ2
2 )t + σ(Z(t) −Z(0))] .
(3.18)
So that we have just shown that E[S] = Seµt by using a simple PDE argument and Ito’s Lemma. Isn’t this
easier than using brute force statistics? PDEs are much more elegant.
4
Monte Carlo Methods
This brings us to the simplest numerical method for computing the no-arbitrage value of an option. Suppose
that we assume that the underlying process is
dS
S = rdt + σdZ
(4.1)
then we can simulate a path forward in time, starting at some price today S0, using a forward Euler
timestepping method (Si = S(ti))
Si+1
=
Si + Si(r∆t + σφi√
∆t)
(4.2)
where ∆t is the finite timestep, and φi is a random number which is N(0, 1). Note that at each timestep,
we generate a new random number. After N steps, with T = N∆t, we have a single realized path. Given
the payofffunction of the option, the value for this path would be
V alue
=
Payoff(SN) .
(4.3)
For example, if the option was a European call, then
V alue
=
max(SN −K, 0)
K = Strike Price
(4.4)
Suppose we run a series of trials, m = 1, ..., M, and denote the payoffafter the m′th trial as payoff(m).
Then, the no-arbitrage value of the option is
Option V alue
=
e−rT E(payoff)
≃
e−rT 1
M
m=M
X
m=1
payoff(m) .
(4.5)
Recall that these paths are not the real paths, but are the risk neutral paths.
Now, we should remember that we are
1. approximating the solution to the SDE by forward Euler, which has O(∆t) truncation error.
2. approximating the expectation by the mean of many random paths. This Monte Carlo error is of size
O(1/
√
M), which is slowly converging.
There are thus two sources of error in the Monte Carlo approach: timestepping error and sampling error.
The slow rate of convergence of Monte Carlo methods makes these techniques unattractive except when
the option is written on several (i.e. more than three) underlying assets. As well, since we are simulating
forward in time, we cannot know at a given point in the forward path if it is optimal to exercise or hold an
American style option. This is easy if we use a PDE method, since we solve the PDE backwards in time, so
we always know the continuation value and hence can act optimally. However, if we have more than three
factors, PDE methods become very expensive computationally. As well, if we want to determine the effects
of discrete hedging, for example, a Monte Carlo approach is very easy to implement.
The error in the Monte Carlo method is then
Error
=
O

max(∆t,
√
M
)

∆t = timestep
M = number of Monte Carlo paths
(4.6)
Now, it doesn’t make sense to drive the Monte Carlo error down to zero if there is O(∆t) timestepping error.
We should seek to balance the timestepping error and the sampling error. In order to make these two errors
the same order, we should choose M = O(
(∆t)2 ). This makes the total error O(∆t). We also have that
Complexity
=
O
 M
∆t

=
O

(∆t)3

∆t
=
O

(Complexity)−1/3
(4.7)
and hence
Error
=
O

( Complexity)1/3

.
(4.8)
In practice, the convergence in terms of timestep error is often not done. People just pick a timestep,
i.e. one day, and increase the number of Monte Carlo samples until they achieve convergence in terms of
sampling error, and ignore the timestep error. Sometimes this gives bad results!
Note that the exact solution to Geometric Brownian motion (2.57) has the property that the asset value
S can never reach S = 0 if S(0) > 0, in any finite time. However, due to the approximate nature of our
Forward Euler method for solving the SDE, it is possible that a negative or zero Si can show up. We can
do one of three things here, in this case
• Cut back the timestep at this point in the simulation so that S is positive.
• Set S = 0 and continue. In this case, S remains zero for the rest of this particular simulation.
• Use Ito’s Lemma, and determine the SDE for log S, i.e. if F = log S, then, from equation (2.55), we
obtain (with µ = r)
dF
=
(r −σ2
2 )dt + σdZ ,
(4.9)
so that now, if F < 0, there is no problem, since S = eF , and if F < 0, this just means that S is very
small. We can use this idea for any stochastic process where the variable should not go negative.
Usually, most people set S = 0 and continue. As long as the timestep is not too large, this situation is
probably due to an event of low probability, hence any errors incurred will not affect the expected value very
much. If negative S values show up many times, this is a signal that the timestep is too large.
In the case of simple Geometric Brownian motion, where r, σ are constants, then the SDE can be solved
exactly, and we can avoid timestepping errors (see Section 2.6.2). In this case
S(T) = S(0) exp[(r −σ2
2 )T + σφ
√
T]
(4.10)
where φ ∼N(0, 1). I’ll remind you that equation (4.10) is exact. For these simple cases, we should always
use equation (4.10). Unfortunately, this does not work in more realistic situations.
Monte Carlo is popular because
• It is simple to code. Easily handles complex path dependence.
• Easily handles multiple assets.
The disadvantages of Monte Carlo methods are
• It is difficult to apply this idea to problems involving optimal decision making (e.g. American options).
• It is hard to compute the Greeks (VS, VSS), which are the hedging parameters, very accurately.
• MC converges slowly.
4.1
Monte Carlo Error Estimators
The sampling error can be estimated via a statistical approach. If the estimated mean of the sample is
ˆµ
=
e−rT
M
m=M
X
m=1
payoff(m)
(4.11)
and the standard deviation of the estimate is
ω
=
M −1
m=M
X
m=1
(e−rT payoff(m) −ˆµ)2
!1/2
(4.12)
then the 95% confidence interval for the actual value V of the option is
ˆµ −1.96ω
√
M
< V < ˆµ + 1.96ω
√
M
(4.13)
Note that in order to reduce this error by a factor of 10, the number of simulations must be increased by
100.
The timestep error can be estimated by running the problem with different size timesteps, comparing the
solutions.
4.2
Random Numbers and Monte Carlo
There are many good algorithms for generating random sequences which are uniformly distributed in [0, 1].
See for example, (Numerical Recipies in C++., Press et al, Cambridge University Press, 2002). As pointed
out in this book, often the system supplied random number generators, such as rand in the standard C
library, and the infamous RANDU IBM function, are extremely bad. The Matlab functions appear to be
quite good. For more details, please look at (Park and Miller, ACM Transactions on Mathematical Software,
31 (1988) 1192-1201). Another good generator is described in (Matsumoto and Nishimura, “The Mersenne
Twister: a 623 dimensionally equidistributed uniform pseudorandom number generator,” ACM Transactions
on Modelling and Computer Simulation, 8 (1998) 3-30.) Code can be downloaded from the authors Web
site.
However, we need random numbers which are normally distributed on [−∞, +∞], with mean zero and
variance one (N(0, 1)).
Suppose we have uniformly distributed numbers on [0, 1], i.e. the probability of obtaining a number
between x and x + dx is
p(x)dx
=
dx ;
0 ≤x ≤1
=
0 ;
otherwise
(4.14)
Let’s take a function of this random variable y(x). How is y(x) distributed? Let ˆp(y) be the probability
distribution of obtaining y in [y, y + dy]. Consequently, we must have (recall the law of transformation of
probabilities)
p(x)|dx|
=
ˆp(y)|dy|
or
ˆp(y)
=
p(x)

dx
dy
 .
(4.15)
Suppose we want ˆp(y) to be normal,
ˆp(y)
=
e−y2/2
√
2π
.
(4.16)
If we start with a uniform distribution, p(x) = 1 on [0, 1], then from equations (4.15-4.16) we obtain
dx
dy
=
e−y2/2
√
2π
.
(4.17)
Now, for x ∈[0, 1], we have that the probability of obtaining a number in [0, x] is
Z x
dx′
=
x ,
(4.18)
but from equation (4.17) we have
dx′
=
e−(y′)2/2
√
2π
dy′ .
(4.19)
So, there exists a y such that the probability of getting a y′ in [−∞, y] is equal to the probability of getting
x′ in [0, x],
Z x
dx′
=
Z y
−∞
e−(y′)2/2
√
2π
dy′ ,
(4.20)
or
x
=
Z y
−∞
e−(y′)2/2
√
2π
dy′ .
(4.21)
So, if we generate uniformly distributed numbers x on [0, 1], then to determine y which are N(0, 1), we do
the following
• Generate x
• Find y such that
x
=
√
2π
Z y
−∞
e−(y′)2/2dy′ .
(4.22)
We can write this last step as
y = F(x)
(4.23)
where F(x) is the inverse cumulative normal distribution.
4.3
The Box-Muller Algorithm
Starting from random numbers which are uniformly distributed on [0, 1], there is actually a simpler method
for obtaining random numbers which are normally distributed.
If p(x) is the probability of finding x ∈[x, x + dx] and if y = y(x), and ˆp(y) is the probability of finding
y ∈[y, y + dy], then, from equation (4.15) we have
|p(x)dx|
=
|ˆp(y)dy|
(4.24)
or
ˆp(y)
=
p(x)

dx
dy
 .
(4.25)
Now, suppose we have two original random variables x1, x2, and let p(xi, x2) be the probability of
obtaining (x1, x2) in [x1, x1 + dx1] × [x2, x2 + dx2]. Then, if
y1
=
y1(x1, x2)
y2
=
y2(x1, x2)
(4.26)
and we have that
ˆp(y1, y2)
=
p(x1, x2)

∂(x1, x2)
∂(y1, y2)

(4.27)
where the Jacobian of the transformation is defined as
∂(x1, x2)
∂(y1, y2)
=
det

∂x1
∂y1
∂x1
∂y2
∂x2
∂y1
∂x2
∂y2

(4.28)
Recall that the Jacobian of the transformation can be regarded as the scaling factor which transforms dx1 dx2
to dy1 dy2, i.e.
dx1 dx2
=

∂(x1, x2)
∂(y1, y2)
 dy1 dy2 .
(4.29)
Now, suppose that we have x1, x2 uniformly distributed on [0, 1] × [0, 1], i.e.
p(x1, x2)
=
U(x1)U(x2)
(4.30)
where
U(x)
=
;
0 ≤x ≤1
=
0 ;
otherwise .
(4.31)
We denote this distribution as x1 ∼U[0, 1] and x2 ∼U[0, 1].
If p(x1, x2) is given by equation (4.30), then we have from equation (4.27) that
ˆp(y1, y2)
=

∂(x1, x2)
∂(y1, y2)

(4.32)
Now, we want to find a transformation y1 = y1(x1, x2), y2 = y2(x1, x2) which results in normal distributions
for y1, y2. Consider
y1
=
p
−2 log x1 cos 2πx2
y2
=
p
−2 log x1 sin 2πx2
(4.33)
or solving for (x2, x2)
x1
=
exp
−1
2 (y2
1 + y2
2)

x2
=
2π tan−1
y2
y1

.
(4.34)
After some tedious algebra, we can see that (using equation (4.34))

∂(x1, x2)
∂(y1, y2)

=
√
2π e−y2
1/2
√
2π e−y2
2/2
(4.35)
Now, assuming that equation (4.30) holds, then from equations (4.32-4.35) we have
ˆp(y1, y2)
=
√
2π e−y2
1/2
√
2π e−y2
2/2
(4.36)
so that (y1, y2) are independent, normally distributed random variables, with mean zero and variance one,
or
y1 ∼N(0, 1)
;
y2 ∼N(0, 1) .
(4.37)
This gives the following algorithm for generating normally distributed random numbers (given uniformly
distributed numbers):
Box Muller Algorithm
Repeat
Generate u1 ∼U(0, 1), u2 ∼U(0, 1)
θ = 2πu2, ρ = √−2 log u1
z1 = ρ cos θ; z2 = ρ sin θ
End Repeat
(4.38)
This has the effect that Z1 ∼N(0, 1) and Z2 ∼N(0, 1).
Note that we generate two draws from a normal distribution on each pass through the loop.
4.3.1
An improved Box Muller
The algorithm (4.38) can be expensive due to the trigonometric function evaluations.
We can use the
following method to avoid these evaluations. Let
U1 ∼U[0, 1]
;
U2 ∼U[0, 1]
V1 = 2U1 −1
;
V2 = 2U2 −1
(4.39)
which means that (V1, V2) are uniformly distributed in [−1, 1] × [−1, 1]. Now, we carry out the following
procedure
Rejection Method
Repeat
If ( V 2
1 + V 2
2 < 1 )
Accept
Else
Reject
Endif
End Repeat
(4.40)
which means that if we define (V1, V2) as in equation (4.39), and then process the pairs (V1, V2) using
algorithm (4.40) we have that (V1, V2) are uniformly distributed on the disk centered at the origin, with
radius one, in the (V1, V2) plane. This is denoted by
(V1, V2)
∼
D(0, 1) .
(4.41)


## More on Ito's Lemma

What is the meaning of a no-arbitrage tree? If we are sitting at node Sn
j , and assuming that there are
only two possible future states
Sn
j
→
Sn+1
j+1
;
with probability p
Sn
j
→
Sn+1
j
;
with probability q
then using (αh) from equation (5.15) guarantees that the hedging portfolio has the same value in both future
states.
But let’s be a bit more sensible here. Suppose we are hedging a portfolio of RIM stock. Let ∆t = one
day. Suppose the price of RIM stocks is $10 today. Do we actually believe that tomorrow there are only two
possible prices for Rim stock
Sup
=
10eσ
√
∆t
Sdown
=
10e−σ
√
∆t ?
(5.19)
Of course not. This is obviously a highly simplified model. The fact that there is no-arbitrage in the context
of the simplified model does not really have a lot of relevance to the real-world situation. The best that
can be said is that if the Black-Scholes model was perfect, then we have that the portfolio hedging ratios
computed using either pr, qr or pr∗, qr∗are both correct to O(∆t).
More on Ito’s Lemma
In Section 2.6.1, we mysteriously made the infamous comment
...it can be shown that dZ2 →dt as dt →0
In this Section, we will give some justification this remark. For a lot more details here, we refer the
reader to Stochastic Differential Equations, by Bernt Oksendal, Springer, 1998.
We have to go back here, and decide what the statement
dX
=
αdt + cdZ
(6.1)
really means. The only sensible interpretation of this is
X(t) −X(0)
=
Z t
α(X(s), s)ds +
Z t
c(X(s), s)dZ(s) .
(6.2)
where we can interpret the integrals as the limit, as ∆t →0 of a discrete sum. For example,
Z t
c(X(s), s)dZ(s)
=
lim
∆t→0
j=N−1
X
j=0
cj∆Zj
cj = c(X(Zj), tj)
Zj = Z(tj)
∆Zj = Z(tj+1) −Z(tj)
∆t = tj+1 −tj
N = t/(∆t)
(6.3)
In particular, in order to derive Ito’s Lemma, we have to decide what
Z t
c(X(s), s) dZ(s)2
(6.4)
means. Replace the integral by a sum,
Z t
c(X(s), s) dZ(s)2
=
lim
∆t→0
j=N−1
X
j=0
c(Xj, tj)∆Z2
j .
(6.5)
Note that we have evaluated the integral using the left hand end point of each subinterval (the no peeking
into the future principle).
From now on, we will use the notation
X
j
≡
j=N−1
X
j=0
.
(6.6)
Now, we claim that
Z t
c(X(s), s)dZ2(s)
=
Z t
c(X(s), s)ds
(6.7)
or
lim
∆t→0

X
j
cj∆Z2
j


=
lim
∆t→0
X
j
cj∆t
(6.8)
which is what we mean by equation (6.7). i.e. we can say that dZ2 →dt as dt →0.
Now, let’s consider a finite ∆t, and consider the expression
E



X
j
cj∆Z2
j −
X
j
cj∆t


2

(6.9)
If equation (6.9) tends to zero as ∆t →0, then we can say that (in the mean square limit)
lim
∆t→0

X
j
cj∆Z2
j


=
lim
∆t→0
X
j
cj∆t
=
Z t
c(X(s), s) ds
(6.10)
so that in this sense
Z t
c(X, s) dZ2
=
Z t
c(X, s) ds
(6.11)
and hence we can say that
dZ2 →dt
(6.12)
with probability one as ∆t →0.
Now, expanding equation (6.9) gives
E



X
j
cj∆Z2
j −
X
j
cj∆t


2

=
X
ij
E

cj(∆Z2
j −∆t)ci(∆Z2
i −∆t)

.
(6.13)
Now, note the following
• The increments of Brownian motion are uncorrelated, i.e. Cov \[∆Zi ∆Zj] = 0, i ̸= j, which means
that Cov

∆Z2
i ∆Z2
j

= 0, or E

(∆Z2
j −∆t)(∆Z2
i −∆t)

= 0, i ̸= j.
• ci = c(ti, X(Zi)), and ∆Zi are independent.
It then follows that for i < j
E

cj(∆Z2
j −∆t)ci(∆Z2
i −∆t)

=
E\[cicj(∆Z2
i −∆t)]E\[(∆Z2
j −∆t)]
=
0 .
(6.14)
Similarly, if i > j
E

cj(∆Z2
j −∆t)ci(∆Z2
i −∆t)

=
E\[cicj(∆Z2
j −∆t)]E\[(∆Z2
i −∆t)]
=
0 .
(6.15)
So that in all cases
E

cj(∆Z2
j −∆t)ci(∆Z2
i −∆t)

=
δijE

c2
i (∆Z2
i −∆t)2
.
(6.16)
It also follows from the above properties that
E\[c2
j(∆Z2
j −∆t)2]
=
E\[c2
j] E\[(∆Z2
j −∆t)2]
(6.17)
since cj and (∆Z2
j −∆t) are independent.
Using equations (6.16-6.17), then equation (6.13) becomes
X
ij
E

cj(∆Z2
j −∆t) ci(∆Z2
i −∆t)

=
X
i
E\[c2
i ] E

(∆Z2
i −∆t)2
.
(6.18)
Now,
X
i
E\[c2
i ] E

(∆Z2
i −∆t)2
=
X
i
E\[c2
i ]
E

∆Z4
i

−2∆tE

∆Z2
i

+ (∆t)2
.
(6.19)
Recall that (∆Z)2 is N(0, ∆t) ( normally distributed with mean zero and variance ∆t) so that
E

(∆Zi)2
=
∆t
E

(∆Zi)4
=
3(∆t)2
(6.20)
so that equation (6.19) becomes
E

∆Z4
i

−2∆tE

∆Z2
i

+ (∆t)2
=
2(∆t)2
(6.21)
and
X
i
E\[c2
i ] E

(∆Z2
i −∆t)2
=
X
i
E\[c2
i ](∆t)2
=
2∆t
 X
i
E\[c2
i ]∆t
!
=
O(∆t)
(6.22)
so that we have
E



X
cj∆Z2
j −
X
j
cj∆t


2

=
O(∆t)
(6.23)

