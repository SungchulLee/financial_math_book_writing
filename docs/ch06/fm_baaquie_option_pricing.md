# Option Pricing for Physicists

!!! info "Source"
    **Quantitative Finance for Physicists: An Introduction** by Belal E. Baaquie, Academic Press, 2004.
    These notes are used for educational purposes.

## Option Pricing

Chapter 9
Option Pricing
This chapter begins with an introduction of the notion of financial
derivative in Section 9.1. The general properties of the stock options
are described in Section 9.2. Furthermore, the option pricing theory is
presented using two approaches: the method of the binomial trees
(Section 9.3) and the classical Black-Scholes theory (Section 9.4).
A paradox related to the arbitrage free portfolio paradigm on which
the Black-Scholes theory is based is described in the Appendix section.
9.1 FINANCIAL DERIVATIVES
In finance, derivatives1 are the instruments whose price depends
on the value of another (underlying) asset [1]. In particular, the
stock option is a derivative whose price depends on the underlying
stock price. Derivatives have also been used for many other assets,
including but not limited to commodities (e.g., cattle, lumber,
copper), Treasury bonds, and currencies.
An example of a simple derivative is a forward contract that obliges
its owner to buy or sell a certain amount of the underlying asset at a
specified price (so-called forward price or delivery price) on a specified
date (delivery date or maturity). The party involved in a contract as a
buyer is said to have a long position, while a seller is said to have a short
position. A forward contract is settled at maturity when the seller
93

delivers the asset to the buyer and the buyer pays the cash amount at
the delivery price. At maturity, the current (spot) asset price, ST, may
differ from the delivery price, K. Then the payoff from the long
position is ST  K and the payoff from the short position is K  ST.
Future contracts are the forward contracts that are traded on
organized exchanges, such as the Chicago Board of Trade (CBOT)
and the Chicago Mercantile Exchange (CME). The exchanges deter-
mine the standardized amounts of traded assets, delivery dates, and
the transaction protocols.
In contrast to the forward and future contracts, options give an
option holder the right to trade an underlying asset rather than the
obligation to do this. In particular, the call option gives its holder the
right to buy the underlying asset at a specific price (so-called exercise
price or strike price) by a certain date (expiration date or maturity).
The put option gives its holder the right to sell the underlying asset at a
strike price by an expiration date. Two basic option types are the
European options and the American options.2 The European options
can be exercised only on the expiration date while the American
options can be exercised any time up to the expiration date. Most of
the current trading options are American. Yet, it is often easier to
analyze the European options and use the results for deriving proper-
ties of the corresponding American options.
The option pricing theory has been an object of intensive research
since the pioneering works of Black, Merton, and Scholes in the
1970s. Still, as we shall see, it poses many challenges.
9.2 GENERAL PROPERTIES OF STOCK OPTIONS
The stock option price is determined with six factors:
. Current stock price, S
. Strike price, K
. Time to maturity, T
. Stock price volatility, s
. Risk-free interest rate,3 r
. Dividends paid during the life of the option, D.
Let us discuss how each of these factors affects the option price
providing all other factors are fixed. Longer maturity time increases
94
Option Pricing

the value of an American option since its holders have more time to
exercise it with profit. Note that this is not true for a European option
that can be exercised only at maturity date. All other factors, how-
ever, affect the American and European options in similar ways.
The effects of the stock price and the strike price are opposite for
call options and put options. Namely, payoff of a call option increases
while payoff of a put option decreases with rising difference between
the stock price and the strike price.
Growing volatility increases the value of both call options and put
options: it yields better chances to exercise them with higher payoff.
In the mean time, potential losses cannot exceed the option price.
The effect of the risk-free rate is not straightforward. At a fixed
stock price, the rising risk-free rate increases the value of the call
option. Indeed, the option holder may defer paying for shares and
invest this payment into the risk-free assets until the option matures.
On the contrary, the value of the put option decreases with the risk-
free rate since the option holder defers receiving payment from selling
shares and therefore cannot invest them into the risk-free assets.
However, rising interest rates often lead to falling stock prices,
which may change the resulting effect of the risk-free rate.
Dividends effectively reduce the stock prices. Therefore, dividends
decrease value of call options and increase value of put options.
Now, let us consider the payoffs at maturity for four possible
European option positions. The long call option means that the in-
vestor buys the right to buy an underlying asset. Obviously, it makes
sense to exercise the option only if S > K. Therefore, its payoff is
PLC ¼ max [S  K, 0]
(9:2:1)
The short call option means that the investor sells the right to buy an
underlying asset. This option is exercised if S > K, and its payoff is
PSC ¼ min [K  S, 0]
(9:2:2)
The long put option means that the investor buys the right to sell an
underlying asset. This option is exercised when K > S, and its payoff
is
PLP ¼ max [K  S, 0]
(9:2:3)
The short put option means that the investor sells the right to sell an
underlying asset. This option is exercised when K > S, and its payoff is
Option Pricing
95

PSP ¼ min [S  K, 0]
(9:2:4)
Note that the option payoff by definition does not account for the
option price (also named option premium). In fact, option writers sell
options at a premium while option buyers pay this premium. There-
fore, the option seller’s profit is the option payoff plus the option
price, while the option buyer’s profit is the option payoff minus the
option price (see examples in Figure 9.1).
The European call and put options with the same strike price
satisfy the relation called put-call parity. Consider two portfolios.
Portfolio I has one European call option at price c with the strike
price K and amount of cash (or zero-coupon bond) with the present
value Kexp[r(T  t)]. Portfolio II has one European put option at
price p and one share at price S. First, let us assume that share does
not pay dividends. Both portfolios at maturity have the same value:
max (ST, K). Hence,
c þ Kexp[r(T  t)] ¼ p þ S
(9:2:5)
Dividends affect the put-call parity. Namely, the dividends D being
paid during the option lifetime have the same effect as the cash future
value. Thus,
c þ D þ K exp [r(T  t)] ¼ p þ S
(9:2:6)
Because the American options may be exercised before maturity, the
relations between the American put and call prices can be derived
only in the form of inequalities [1].
Options are widely used for both speculation and risk hedging.
Consider two examples with the IBM stock options. At market
closing on 7-Jul-03, the IBM stock price was $83.95. The (American)
call option price at maturity on 3-Aug-03 was $2.55 for the strike
price of $85. Hence, the buyer of this option at market closing on 7-
Jul-03 assumed that the IBM stock price would exceed $(85 þ 2.55) ¼
$87.55 before or on 3-Aug-03. If the IBM share price would reach say
$90, the option buyer will exercise the call option to buy the share for
$85 and immediately sell it for $90. The resulting profit4 is
$(9087.55) ¼ $2.45. Thus, the return on exercising this option equals
2:45=2:55100% ¼ 96%. Note that the return on buying an IBM
share in this case would only be (90  83:95)=83:95100% ¼ 7:2%.
96
Option Pricing

−20
−15
−10
−5
0
5
10
15
20
0
5
10
15
20
25
30
35
40
Stock price
Profit
Short Call
Long Call
(a)
Stock price
Profit
Short Put
Long Put
(b)
−20
−15
−10
−5
0
5
10
15
20
0
5
10
15
20
25
30
35
40
Figure 9.1 The option profits for the strike price of $25 and the option
premium of $5: (a) calls, (b) puts.
Option Pricing
97

If, however, the IBM share price stays put through 3-Aug-03, an
option buyer incurs losses of $2.45 (i.e., 100%). In the mean time, a
share buyer has no losses and may continue to hold shares, hoping
that their price will grow in future.
At market closing on 7-Jul-03, the put option for the IBM share
with the strike price of $80 at maturity on 3-Aug-03 was $1.50. Hence,
buyers of this put option bet on price falling below $(801.50) ¼
$78.50. If, say the IBM stock price falls to $75, the buyer of the put
option has a gain of $(78:50  75) ¼ $3.50.
Now, consider hedging in which the investor buys simultaneously
one share for $83.95 and a put option with the strike price of $80 for
$1.50. The investor has gains only if the stock price rises above
$(83:95 þ 1:50) ¼$85:45. However, if the stock price falls to say $75,
the investor’s loss is $(80  85:45) ¼ $5:45 rather than the loss of
$(75  83:95) ¼ $8:95 incurred without hedging with the put
option. Hence, in the given example, the hedging expense of $1.50
allows the investor to save $(5:45 þ 8:95) ¼$3:40.
9.3 BINOMIAL TREES
Let us consider a simple yet instructive method for option pricing
that employs a discrete model called the binomial tree. This model is
based on the assumption that the current stock price S can change at
the next moment only to either the higher value Su or the lower value
Sd (where u > 1 and d < 1). Let us start with the first step of the
binomial tree (see Figure 9.2). Let the current option price be equal to
F and denote it with Fu or Fd at the next moment when the stock price
moves up or down, respectively. Consider now a portfolio that con-
sists of D long shares and one short option. This portfolio is risk-free
if its value does not depend on whether the stock price moves up or
down, that is,
SuD  Fu ¼ SdD  Fd
(9:3:1)
Then the number of shares in this portfolio equals
D ¼ (Fu  Fd)=(Su  Sd)
(9:3:2)
The risk-free portfolio with the current value (SD  F) has the future
value (SuD  Fu) ¼ (SdD  Fd). If the time interval is t and the risk-
98
Option Pricing

free interest rate is r, the relation between the portfolio’s present value
and future value is
(SD  F) exp(rt) ¼ SuD  Fu
(9:3:3)
Combining (9.3.2) and (9.3.3) yields
F ¼ exp(rt)[pFu þ (1  p)Fd]
(9:3:4)
where
p ¼ [ exp (rt)  d]=(u  d)
(9:3:5)
The factors p and (1  p) in (9.3.4) have the sense of the probabilities
for the stock price to move up and down, respectively. Then, the
expectation of the stock price at time t is
E[S(t)] ¼ E[pSu þ (1  p)Sd] ¼ S exp (rt)
(9:3:6)
This means that the stock price grows on average with the risk-free
rate. The framework within which the assets grow with the risk-free
rate is called risk-neutral valuation. It can be discussed also in terms of
the arbitrage theorem [4]. Indeed, violation of the equality (9.3.3)
Su2
Fuu
Su
Fu
Sud
S
F
Fud
Sd
Fd
Sd2
Fdd
Figure 9.2 Two-step binomial pricing tree.
Option Pricing
99

implies that the arbitrage opportunity exists for the portfolio. For
example, if the left-hand side of (9.3.3) is greater than its right-hand
side, one can immediately make a profit by selling the portfolio and
buying the risk-free asset.
Let us proceed to the second step of the binomial tree. Using
equation (9.3.4), we receive the following relations between the option
prices on the first and second steps
Fu ¼ exp (rt)[pFuu þ (1  p)Fud]
(9:3:7)
Fd ¼ exp (rt)[pFud þ (1  p)Fdd]
(9:3:8)
The combination of (9.3.4) with (9.3.7) and (9.3.8) yields the current
option price in terms of the option prices at the next step
F ¼ exp (2rt)[p2Fuu þ 2p(1  p)Fud þ (1  p)2Fdd]
(9:3:9)
This approach can be generalized for a tree with an arbitrary number
of steps. Namely, first the stock prices at every node are calculated
by going forward from the first node to the final nodes. When the
stock prices at the final nodes are known, we can determine the
option prices at the final nodes by using the relevant payoff relation
(e.g., (9.2.1) for the long call option). Then we calculate the option
prices at all other nodes by going backward from the final nodes to
the first node and using the recurrent relations similar to (9.3.7) and
(9.3.8).
The factors that determine the price change, u and d, can be
estimated from the known stock price volatility [1]. In particular, it
is generally assumed that prices follow the geometric Brownian
motion
dS ¼ mSdt þ sSdW
(9:3:10)
where m and s are the drift and diffusion parameters, respectively, and
dW is the standard Wiener process (see Section 4.2). Hence, the price
changes within the time interval [0, t] are described with the lognor-
mal distribution
ln S(t) ¼ N( ln S0 þ (m  s2=2)t, s
ffiffi
t
p
)
(9:3:11)
In (9.3.11), S0 ¼ S(0), N(m, s) is the normal distribution with mean
m and standard deviation s. It follows from equation (9.3.11) that the
expectation of the stock price and its variance at time t equal
100
Option Pricing

E[S(t)] ¼ S0 exp (mt)
(9:3:12)
Var[S(t)] ¼ S0
2 exp (2mt)[ exp (s2t)  1]
(9:3:13)
In addition, equation (9.3.6) yields
exp (rt) ¼ pu þ (1  p)d
(9:3:14)
Using (9.3.13) and (9.3.14) in the equality (y) ¼ E[y2]  E[y]2, we
obtain the relation
exp (2rt þ s2t) ¼ pu2 þ (1  p)d2
(9:3:15)
The equations (9.3.14) and (9.3.15) do not suffice to define the three
parameters d, p, and u. Usually, the additional condition
u ¼ 1=d
(9:3:16)
is employed. When the time interval Dt is small, the linear approxi-
mation to the system of equations (9.3.14) through (9.3.16) yields
p ¼ [ exp (rDt)  d]=(u  d), u ¼ 1=d ¼ exp [s(Dt)1=2]
(9:3:17)
The binomial tree model can be generalized in several ways [1]. In
particular, dividends and variable interest rates can be included. The
trinomial tree model can also be considered. In the latter model, the
stock price may move upward or downward, or it may stay the same.
The drawback of the discrete tree models is that they allow only for
predetermined innovations of the stock price. Moreover, as it was
described above, the continuous model of the stock price dynamics
(9.3.10) is used to estimate these innovations. It seems natural then to
derive the option pricing theory completely within the continuous
framework.
9.4 BLACK-SCHOLES THEORY
The basic assumptions of the classical option pricing theory are
that the option price F(t) at time t is a continuous function of time
and its underlying asset’s price S(t)
F ¼ F(S(t), t)
(9:4:1)
and that price S(t) follows the geometric Brownian motion (9.3.10) [5,
6]. Several other assumptions are made to simplify the derivation of
the final results. In particular,
Option Pricing
101

. There are no market imperfections, such as price discreteness,
transaction costs, taxes, and trading restrictions including those
on short selling.
. Unlimited risk-free borrowing is available at a constant rate, r.
. There are no arbitrage opportunities.
. There are no dividend payments during the life of the option.
Now, let us derive the classical Black-Scholes equation. Since it is
assumed that the option price F(t) is described with equation (9.4.1)
and price of the underlying asset follows equation (9.3.10), we can use
the Ito’s expression (4.3.5)
dF(S, t) ¼ mS @F
@S þ @F
@t þ s2
2 S2 @2F
@S2


dt þ sS @F
@S dW(t)
(9:4:2)
Furthermore, we build a portfolio P with eliminated random contri-
bution dW. Namely, we choose 1 (short) option and @F
@S shares of
the underlying asset,5
P ¼ F þ @F
@S S
(9:4:3)
The change of the value of this portfolio within the time interval dt
equals
dP ¼ dF þ @F
@S dS
(9:4:4)
Since there are no arbitrage opportunities, this change must be equal to
the interest earned by the portfolio value invested in the risk-free asset
dP ¼ rP dt
(9:4:5)
The combination of equations (9.4.2)–(9.4.5) yields the Black-Scholes
equation
@F
@t þ rS @F
@S þ s2
2 S2 @2F
@S2  rF ¼ 0
(9:4:6)
Note that this equation does not depend on the stock price drift
parameter m, which is the manifestation of the risk-neutral valuation.
In other words, investors do not expect a portfolio return exceeding
the risk-free interest.
102
Option Pricing

The Black-Scholes equation is the partial differential equation with
the first-order derivative in respect to time and the second-order de-
rivative in respect to price. Hence, three boundary conditions deter-
mine the Black-Scholes solution. The condition for the time variable is
defined with the payoff at maturity. The other two conditions for the
price variable are determined with the asymptotic values for the zero
and infinite stock prices. For example, price of the put option equals
the strike price when the stock price is zero. On the other hand, the put
option price tends to be zero if the stock price approaches infinity.
The Black-Scholes equation has an analytic solution in some
simple cases. In particular, for the European call option, the Black-
Scholes solution is
c(S, t) ¼ N(d1)S(t)  KN(d2) exp[r(T  t)]
(9:4:7)
In (9.4.7), N(x) is the standard Gaussian cumulative probability
distribution
d1 ¼ [ ln (S=K) þ (r þ s2=2)(T  t)]=[s(T  t)1=2],
d2 ¼ d1  (T  t)1=2
(9:4:8)
The Black-Scholes solution for the European put option is
p(S, t) ¼ K exp[r(T  t)] N(d2)  S(t)N(d1)
(9:4:9)
The value of the American call option equals the value of the Euro-
pean call option. However, no analytical expression has been found
for the American put option. Numerical methods are widely used for
solving the Black-Scholes equation when analytic solution is not
available [1–3].
Implied volatility is an important notion related to BST. Usually,
the stock volatility used in the Block-Scholes expressions for the
option prices, such as (9.4.7), is calculated with the historical stock
price data. However, formulation of the inverse problem is also
possible. Namely, the market data for the option prices can be used
in the left-hand side of (9.4.7) to recover the parameter s. This
parameter is named the implied volatility. Note that there is no
analytic expression for implied volatility. Therefore, numerical
methods must be employed for its calculation. Several other functions
related to the option price, such as Delta, Gamma, and Theta (so-
called Greeks), are widely used in the risk management:
Option Pricing
103

D ¼ @F
@S , G ¼ @2F
@S2 , Q ¼ @F
@t
(9:4:10)
The Black-Scholes equation (9.4.6) can be rewritten in terms of
Greeks
Q þ rSD þ s2
2 S2G  rF ¼ 0
(9:4:11)
Similarly, Greeks can be defined for the entire portfolio. For example,
the portfolio’s Delta is @P
@S. Since the share’s Delta
@S
@S


equals unity,
Delta of the portfolio (9.4.3) is zero. Portfolios with zero Delta are
called delta-neutral. Since Delta depends on both price and time,
maintenance of delta-neutral portfolios requires periodic rebalancing,
which is also known as dynamic hedging. For the European call and
put options, Delta equals, respectively
Dc ¼ N(d1), Dp ¼ N(d1)  1
(9:4:12)
Gamma characterizes the Delta’s sensitivity to price variation. If
Gamma is small, rebalancing can be performed less frequently.
Adding options to the portfolio can change its Gamma. In particular,
delta-neutral portfolio with Gamma G can be made gamma-neutral if
it is supplemented with n ¼ G=GF options having Gamma GF.
Theta characterizes the time decay of the portfolio price. In add-
ition, two other Greeks, Vega and Rho, are used to measure the
portfolio sensitivity to its volatility and risk-free rate, respectively
y ¼ @P
@s , r ¼ @P
@r
(9:4:13)
Several assumptions that are made in BST can be easily relaxed. In
particular, dividends can be accounted. Also, r and s can be treated as
time-dependent parameters. BST has been expanded in several ways
(see [1–3, 7, 8] and references therein). One of the main directions
addresses so-called volatility smile. The problem is that if all charac-
teristics of the European option besides the strike price are fixed, its
implied volatility derived from the Black-Scholes expression is con-
stant. However, real market price volatilities do depend on the strike
price, which manifests in ‘‘smile-like’’ graphs. Several approaches
have been developed to address this problem. One of them is introdu-
cing the time dependencies into the interest rates or/and volatilities
104
Option Pricing

(so-called term structure). In a different approach, the lognormal
stock price distribution is substituted with another statistical distri-
bution. Also, the jump-diffusion stochastic processes are sometimes
used instead of the geometric Brownian motion.
Other directions for expanding BST address the market imperfec-
tions, such as transaction costs and finite liquidity. Finally, the option
price in the current option pricing theory depends on time and price
of the underlying asset. This seemingly trivial assumption was ques-
tioned in [9]. Namely, it was shown that the option price might
depend also on the number of shares of the underlying asset in the
arbitrage-free portfolio. Discussion of this paradox is given in the
Appendix section of this chapter.
9.5 REFERENCES FOR FURTHER READING
Hull’s book is the classical reference for the first reading on finan-
cial derivatives [1]. A good introduction to mathematics behind the
option theory can be found in [4]. Detailed presentation of the option
theory, including exotic options and extensions to BST, is given in
[2, 3].
9.6 APPENDIX: THE INVARIANT
OF THE ARBITRAGE-FREE PORTFOLIO
As we discussed in Section 9.4, the option price F(S, t) in BST is a
function of the stock price and time. The arbitrage-free portfolio in
BST consists of one share and of a number of options (M0) that hedge
this share [5]. BST can also be derived with the arbitrage-free port-
folio consisting of one option and of a number of shares M1
0
(see,
e.g., [1]). However, if the portfolio with an arbitrary number of shares
N is considered, and N is treated as an independent variable, that is,
F ¼ F(S, t, N)
(9:6:1)
then a non-zero derivative, @F=@N, can be recovered within the
arbitrage-free paradigm [9]. Since options are traded independently
from their underlying assets, the relation (9.6.1) may look senseless to
the practitioner. How could this dependence ever come to mind?
Option Pricing
105

Recall the notion of liquidity discussed in Section 2.1. If a market
order exceeds supply of an asset at current ‘‘best’’ price, then the
order is executed within a price range rather than at a single price. In
this case within continuous presentation,
S ¼ S(t, N)
(9:6:2)
and the expense of buying N shares at time t equals
ðN
0
S(t, x)dx
(9:6:3)
The liquidity effect in pricing derivatives has been addressed in [10,
11] without proposing (9.6.1). Yet, simply for mathematical general-
ity, one could assume that (9.6.1) may hold if (9.6.2) is valid. Surpris-
ingly, the dependence (9.6.1) holds even for infinite liquidity. Indeed,
consider the arbitrage-free portfolio P with an arbitrary number of
shares N at price S and M options at price F:
P(S, t, N) ¼ NS(t) þ MF(S, t, N)
(9:6:4)
Let us assume that N is an independent variable and M is a parameter
to be defined from the arbitrage-free condition, similar to M0 in BST.
As in BST, the asset price S ¼ S(t) is described with the geometric
Brownian process
dS ¼ mSdt þ sSdW:
(9:6:5)
In (9.6.5), m and s are the price drift and volatility, and W is the
standard Wiener process. According to the Ito’s Lemma,
dF ¼ @F
@t dt þ @F
@S dS þ s2
2 S2 @2F
@S2 dt þ @F
@N dN
(9:6:6)
It follows from (9.6.4) that the portfolio dynamic is
dP ¼ MdF þ NdS þ SdN
(9:6:7)
Substituting equation (9.6.6) into equation (9.6.7) yields
dP ¼ [M @F
@S þ N]dS þ [M @F
@N þ S]dN þ M @F
@t þ s2
2 S2 @2F
@S2


dt
(9:6:8)
106
Option Pricing

As within BST, the arbitrage-free portfolio grows with the risk-free
interest rate, r
dP ¼ rPdt
(9:6:9)
Then the combination of equation (9.6.8) and equation (9.6.9)
yields
[M @F
@S þ N]dS þ [M @F
@t þ s2
2 MS2 @2F
@S2  rMF  rNS]dtþ
[M @F
@N þ S]dN ¼ 0
(9:6:10)
Since equation (9.6.10) must be valid for arbitrary values of dS, dt
and dN, it can be split into three equations
M @F
@S þ N ¼ 0
(9:6:11)
M @F
@t þ s2
2 S2 @2F
@S2  rF


 rNS ¼ 0
(9:6:12)
M @F
@N þ S ¼ 0
(9:6:13)
Let us present F(S, t, N) in the form
F(S, t, N) ¼ F0(S, t)Z(N)
(9:6:14)
where Z(N) satisfies the condition
Z(1) ¼ 1
(9:6:15)
Then it follows from equation (9.6.11) that
M ¼ N= Z @F0
@S


:
(9:6:16)
This transforms equation (9.6.15) and equation (9.6.16), respectively,
to
@F0
@t þ rS @F0
@S þ s2
2 S2 @2F0
@S2  rF0 ¼ 0
(9:6:17)
dZ
dN ¼ (S=F0) @F0
@S (Z=N),
(9:6:18)
Option Pricing
107

Equation (9.6.17) is the classical Black-Scholes equation (cf. with
(9.4.6)) while equations (9.6.16) and (9.6.18) define the values of M
and Z(N). Solution to equation (9.6.18) that satisfies the condition
(9.6.15) is
Z(N) ¼ Na
(9:6:19)
where a ¼ (S=F0)D, D ¼ @F0
@S ¼ M1
0 . Equation (9.6.13) and equa-
tion (9.6.16) yield
M ¼ N1a=D ¼ N1aM0
(9:6:20)
Hence, the option price in the arbitrage-free portfolio with N shares
equals
F(S, t, N) ¼ F0(S, t)Na
(9:6:21)
It coincides with the BST solution F0(S, t) only if N ¼ 1, that is when
the portfolio has one share. However, the total expense of hedging N
shares in the arbitrage-free portfolio
Q ¼ MF ¼ (N=D)F0 ¼ NM0F0
(9:6:22)
is the same as within BST. Therefore, Q is the true invariant of the
arbitrage-free portfolio.
Invariance of the hedging expense is easy to understand using the
dimensionality analysis. Indeed, the arbitrage-free condition (9.6.9) is
given in units of the portfolio and therefore can only be used for
defining part of the portfolio. Namely, the arbitrage-free condition
can be used for defining the hedging expense Q ¼ MF but not for
defining both factors M and F. Similarly, the law of energy conser-
vation can be used for defining the kinetic energy of a body,
K ¼ 0:5mV2. Yet, this law alone cannot be used for calculating the
body’s mass, m, and velocity, V. Note, however, that if a body has
unit mass (m ¼ 1), then the energy conservation law effectively yields
the body’s velocity. Similarly, the arbitrage-free portfolio with one
share does not reveal dependence of the option price on the number of
shares in the portfolio.
108
Option Pricing

9.7 EXERCISES
1. (a) Calculate the Black-Scholes prices of the European call and
put options with six-month maturity if the current stock
price is $20 and grows with average rate of m ¼ 10%, vola-
tility is 20%, and risk-free interest rate is 5%. The strike price
is: (1) $18; (2) $22.
(b) How will the results above change if m ¼ 5%?
2. Is there an arbitrage opportunity with the following assets: the
price of the XYZ stock with no dividends is $100; the European
put options at $98 with six-month maturity are sold for $3.50;
the European call options at $98 with the same maturity are sold
for $8; T-bills with the same maturity are sold for $98. Hint:
Check the put-call parity.
**3. Compare the Ito’s and Stratonovich’s approaches for derivation
of the Black-Scholes equation (consult [12]).
Option Pricing
109

This page intentionally left blank 

