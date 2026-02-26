# The Black-Scholes Model & Risk-Neutral Valuation

!!! info "Source"
    **Financial Mathematics: An Introduction to Derivatives Pricing** by Lane P. Hughston and Christopher J. Hunter, King's College London, 2000.
    These notes are used for educational purposes.

## The Black-Scholes Model

16
Call and Put Option Prices
Formula (15.38) is a great breakthrough.
It says that by performing an
integral we can price any European derivative with a payofffunction that
depends only on the final asset price.
Note that it does not allow us to
calculate prices for either American exercise or path-dependent derivatives.
However, there are still plenty of examples for us to consider. In this chapter
we want to calculate the initial prices of the two of the most widely traded
derivatives–call and put options.
16.1
Call Option
Recall that the call option payoffis
F(ST) = max(ST −K, 0).
(16.1)
Hence the initial price of the derivative is
C0
=
e−rT
√
2π
Z ∞
−∞F
µ
S0 exp
·
rT + σ
√
Tξ −1
2σ2T
¸¶
exp
·
−1
2ξ2
¸
=
e−rT
√
2π
Z ∞
−∞max
µ
S0 exp
·
rT + σ
√
Tξ −1
2σ2T
¸
−K, 0
¶
× exp
·
−1
2ξ2
¸
dξ.
(16.2)
In order to evaluate the integral we need to remove the max function. This
can easily be accomplished because it will be nonzero only when
S0 exp
·
rT + σ
√
Tξ −1
2σ2T
¸
−K > 0,
(16.3)
which is equivalent to
exp
·
rT + σ
√
Tξ −1
2σ2T
¸
> K/S0.
(16.4)
Taking logarithms of both sides we obtain
rT + σ
√
Tξ −1
2σ2T > log(K/S0).
(16.5)
97

We then want to isolate the integration variable ξ. This will allow us to
discover the integration region where the max function is nonzero. We find
that
ξ > log(K/S0) −(rT −1
2σ2T)
σ
√
T
.
(16.6)
If we define the critical value ξ∗to be
ξ∗= log(K/S0) −(rT −1
2σ2T)
σ
√
T
,
(16.7)
then the max function can be written as
max
µ
S0 exp
·
rT + σ
√
Tξ −1
2σ2T
¸
−K, 0
¶
=
(
S0erT+σ
√
Tξ−1
2σ2T −K
ξ > ξ∗
0
ξ < ξ∗.
(16.8)
Since the integrand vanishes for ξ < ξ∗, we only need to integrate over the
region where ξ > ξ∗and the max function takes on a positive value. Hence
the derivative price becomes
C0 = e−rT
√
2π
Z ∞
ξ∗
µ
S0 exp
·
rT + σ
√
Tξ −1
2σ2T
¸
−K
¶
exp
·
−1
2ξ2
¸
dξ. (16.9)
This integral involves two terms, and it is easiest to evaluate them separately.
If we define
I1
=
e−rT
√
2π
Z ∞
ξ∗S0 exp
·
rT + σ
√
Tξ −1
2σ2T
¸
exp
·
−1
2ξ2
¸
dξ
=
1
√
2π
Z ∞
ξ∗S0 exp
·
−1
2ξ2 + σ
√
Tξ −1
2σ2T
¸
(16.10)
and
I2 = −K e−rT
√
2π
Z ∞
ξ∗exp
·
−1
2ξ2
¸
dξ,
(16.11)
then the derivative price is simply the sum of the two integrals, C0 = I1 +I2.
The second integral is easier, so we shall calculate it first. Before we do this,
consider the following result
1
√
2π
Z ∞
x
e−1
2 ξ2dξ
=
1
√
2π
Z −x
−∞e−1
2u2du
=
N(−x),
(16.12)
98

where we made the substitution u = −ξ in the first line and N(x) is the
standard normal cumulative probability density function, previously defined
in equation (11.4). Using this result, we see that
I2
=
−K e−rT
√
2π
Z −ξ∗
−∞e−1
2 ξ2dξ
=
−Ke−rTN(−ξ∗).
(16.13)
However, the standard way of writing the Black-Scholes formula is not in
terms of ξ∗, but rather in terms of two new constants h+ and h−, defined to
be
h± = log( ˜S/K) ± 1
2σ2T
σ
√
T
,
(16.14)
where ˜S is the forward price S0erT. If we then rewrite −ξ∗as
−ξ∗
=
−log(K/S0) −(rT −1
2σ2T)
σ
√
T
=
log(S0/K) + rT −1
2σ2T
σ
√
T
=
log(S0erT/K) −1
2σ2T
σ
√
T
,
(16.15)
we see that
−ξ∗= h−
and
−ξ∗+ √σT = h+.
(16.16)
Hence we can write the integral I2 as
I2 = −e−rTKN(h−).
(16.17)
We now want to calculate the slightly more complicated integral I1. We
begin by ‘completing the square’ in the exponential,
I1
=
1
√
2π
Z ∞
ξ∗S0 exp
·
−1
2ξ2 + σ
√
Tξ −1
2σ2T
¸
dξ
=
S0
√
2π
Z ∞
ξ∗exp
·
−1
2(ξ −σ
√
T)2
¸
dξ.
(16.18)
We then want to make a change of integration variable to η = ξ −σ
√
T. In
this case dξ = dη, and the lower limit of integration ξ = ξ∗, becomes the new
99

lower limit η = ξ∗−σ
√
T = −h+. Hence the integral becomes
I1 =
S0
√
2π
Z η=∞
η=−h+ e−1
2 η2dη.
(16.19)
We can then use the result (C.237) to write the integral in terms of N(x),
I1 = S0N(h+).
(16.20)
If we then sum the values of the integrals I1 and I2 we obtain
C0 = e−rT[S0erTN(h+) −KN(h−)],
(16.21)
which is the famous Black-Scholes formula for the initial value of a call option.
The price and payout function for a call option are plotted in figure 16.1.
Asset Price
$50
$75
$100
$125
$150
Option Price
$0
$15
$30
$45
Figure 16.1:
This figure shows the price for a European call option as a function of the
initial asset price S0, for a maturity of T = 1, an interest rate of r = 0.05, a volatility of
σ = 0.2 and a strike of K = 100. The dashed line is the payofffunction for the option.
Exercise 16.1 Calculate and plot the following derivatives of the option
price at time 0
100

(a) ∆= ∂C0
∂S0
(b) Γ = ∂2C0
∂S2
0
(c) V = ∂C0
∂σ
(d) θ = −∂C0
∂T
(e) ρ = ∂C0
∂r
16.2
Put Option
We recall that a European put option is a derivative that allows the holder
to sell an asset at some time T in the future for a fixed strike price K. Hence
the put option has a payofffunction
F(ST) = max[K −ST, 0].
(16.22)
In other words, this is the net profit that would result if at maturity time
T the holder of the option buys a unit of stock for ST dollars and then sells
it for K dollars, according to the terms of the contract. Clearly the holder
would only do this if K > ST. If K < ST then the option expires worthless.
We can value the put option in an identical manner to how we dealt with
the call option—by using the general formula (15.38). The initial price of
the put option is therefore
P0
=
e−rT
√
2π
Z ∞
−∞F
µ
S0 exp
·
rT + σ
√
Tξ −1
2σ2T
¸¶
exp
·
−1
2ξ2
¸
dξ
=
e−rT
√
2π
Z ∞
−∞max
µ
K −S0 exp
·
rT + σ
√
Tξ −1
2σ2T
¸
, 0
¶
× exp
·
−1
2ξ2
¸
dξ.
(16.23)
As in the call option calculation, we first need to calculate the integration
region on which the integrand is non-zero. This requires
K −S0 exp
·
rT + σ
√
Tξ −1
2σ2T
¸
> 0,
(16.24)
which implies that
K/S0 > exp
·
rT + σ
√
Tξ −1
2σ2T
¸
.
(16.25)
101

Taking logarithms we see that
log(K/S0) −(rT −1
2σ2T)
σ
√
T
> ξ.
(16.26)
However, the left hand side of the inequality is simply the critical value ξ∗
defined in equation (C.232). Since the max function is only non-zero when the
integration variable is less than the critical value ξ∗, we can restrict the range
of integration in equation (16.23) to −∞< ξ < ξ∗. Thus we can eliminate
the max function from our expression for the price of the put option,
P0
=
e−rT
√
2π
Z ξ∗
−∞
µ
K −S0 exp
·
rT + σ
√
Tξ −1
2σ2T
¸¶
× exp
·
−1
2ξ2
¸
dξ.
(16.27)
As before, we have two integrals to calculate,
I1 = K e−rT
√
2π
Z ξ∗
−∞exp
·
−1
2ξ2
¸
dξ,
(16.28)
and
I2
=
−S0
e−rT
√
2π
Z ξ=ξ∗
ξ=−∞exp
·
rT + σ
√
Tξ −1
2σ2T
¸
exp
·
−1
2ξ2
¸
dξ,
=
−S0
1
√
2π
Z ξ=ξ∗
ξ=−∞exp
·
−1
2ξ2 + σ
√
Tξ −1
2σ2T
¸
dξ,
(16.29)
where the put option price is the sum of the two, P0 = I1 + I2. The integral
I1 is trivial to evaluate,
I1 = e−rTKN(ξ∗),
(16.30)
or in terms of the constants h± defined in equation (C.239),
I1 = e−rTKN(−h−).
(16.31)
We can now evaluate the second integral by completing the square in the
exponential,
I2
=
−S0
1
√
2π
Z ξ=ξ∗
ξ=−∞exp
·
−1
2ξ2 + σ
√
Tξ −1
2σ2T
¸
dξ,
=
−S0
√
2π
Z ξ=ξ∗
ξ=−∞exp
·
−1
2(ξ −σ
√
T)2
¸
dξ.
(16.32)
102


## The Black-Scholes Formula

If we then change the integration variable to η = ξ −σ
√
T, then the upper
limit of integration ξ = ξ∗, corresponds to η = ξ∗−σ
√
T = −h+, and we
have
I2 = −S0
√
2π
Z η=−h+
η=−∞e−1
2η2dη.
(16.33)
This is may readily be expressed in terms of N(x),
I2 = −S0N(−h+).
(16.34)
Summing the values of I1 and I2 yields
P0 = e−rT[KN(−h−) −S0erTN(−h+)],
(16.35)
which is the Black-Scholes formula for the initial value of a put option. This
is plotted in figure (16.2).
Asset Price
$0
$50
$100
$150
Option Price
$0
$25
$50
$75
$100
Figure 16.2:
This figure shows the price for a European put option as a function of the
initial asset price S0, for a maturity of T = 1, an interest rate of r = 0.05, a volatility of
σ = 0.2 and a strike of K = 100. The dashed line is the payofffunction for the option.
103

17
More Topics in Option Pricing
In this chapter we want to look at a few applications of the derivative pricing
formula that we derived. We begin by considering European binary options,
which are derivatives that pay offa constant amount only when the final
asset price is above a fixed strike price—otherwise they pay nothing. We
then discuss the partial derivatives of a portfolio, known as the Greeks, and
see how they are used in hedging. Finally we look at put-call parity which
relates the put and call option prices to the forward price of the asset.
17.1
Binary Options
A derivative which pays offone dollar if the share price is above the strike
price at maturity, and pays nothing otherwise is called a binary call option.
If it pays offone dollar when the share price is below the strike and zero if
it is above then this is called a binary put option. We can define the payoff
function in terms of the Heaviside function
H(x) =
(
1
x > 0
0
x < 0 .
(17.1)
Hence the payofffunction for a binary call with strike K is BCT(ST) =
H(ST −K), while for a binary put with strike K it is BPT(ST) = H(K −ST).
Suppose that we want to calculate the price for a binary call option. Using
equation (15.38), we see that
BC0
=
e−rTE∗[BCT(ST)]
=
e−rT
√
2πT
Z ∞
−∞H(ST −K)e−ξ2/2Tdξ
=
e−rT
√
2πT
Z ∞
−∞H (S0 exp[ (r −1
2σ2)T + σξ ]−K) e−ξ2/2Tdξ
=
e−rT
√
2π
Z ∞
−∞H (S0 exp[ (r −1
2σ2)T + σ
√
Tη ]−K) e−η2/2dη,(17.2)
where we made the substitution η = ξ/
√
T in the final integral. The Heavi-
side function is non-zero only when
S0 exp
·
(r −1
2σ2)T + σ
√
Tη
¸
> K.
(17.3)
104

Taking logarithms and isolating η yields
(r −1
2σ2)T + σ
√
Tη
>
−log(S/K)
η
>
−log(S/K) + (r −1
2σ2)Tσ
√
T
η
>
−h−.
(17.4)
Thus the integral simplifies to
BC0
=
e−rT
√
2π
Z ∞
−h−e−η2/2dη
=
e−rTN(h−) .
(17.5)
Exercise 17.1 Calculate the value of the binary put option with payofffunc-
tion H(K −ST).
17.2
‘Greeks’ and Hedging
In chapter 15 we constructed a no arbitrage argument using a portfolio Vt(St)
consisting of a long position in a derivative Ct(St) and a short position in φt
units of the asset St. Suppose that we consider the portfolio as a stochastic
process. Then by Ito’s lemma the change in the value of the portfolio between
times t and t + dt is
dVt = ∂Vt
∂t dt + ∂Vt
∂St
dSt + 1
2
∂2Vt
∂S2
t
dS2
t .
(17.6)
We were able to eliminate uncertainty in this value by setting
∂Vt
∂St
= 0.
(17.7)
A portfolio that satisfies this is known as Delta neutral or Delta hedged be-
cause ∂Vt
∂St is called the Delta of the portfolio.
The Gamma of a portfolio is the second derivative of its value with respect
to the asset price
Γ = ∂2Vt
∂S2
t
.
(17.8)
In order to construct the no arbitrage argument we do not need Γ to vanish
because it only contributes to the deterministic part of the portfolio return.
105

However, the no arbitrage argument assumes that we are continuously able
to rehedge our position such that ∆is always zero. In the context of our
no arbitrage construction, this means that the share holding φt must be
continuously adjusted such that it is always equal to −∂Ct/∂St. In order
to do this we have to be continually buying or selling small amounts of the
underlying asset. However, this is not realistic because there are transaction
costs associated with each trade which make constant rehedging prohibitively
expensive.
So what really happens is that we start with a Delta neutral
position which quickly becomes no longer Delta hedged as the share price
moves around. We then rehedge our position, that is, make it Delta neutral
again, from time to time to reduce the possibility of losing substantial sums
of money.
Is there any way that we can reduce the frequency with which we need to
rehedge our position? Well, we have to adjust our holdings when the value of
Delta becomes too large and sizeable losses can result from small movements
in the underlying asset. If we set Gamma equal to zero, then Delta should
remain small for asset prices near its current value, and hence we will need
to rehedge less often. This is the rationale behind Gamma hedging.
In order to Gamma hedge, assuming that we are also Delta hedging, our
portfolio must consist of at least three instruments that depend on the same
underlying asset. Suppose that we are short a derivative with price process
Ft(St). We can hedge this by taking a position in both the underlying St and
a call option Ct(St). The value of the portfolio is
Vt = −Ft + φtSt + κtCt
(17.9)
The Delta and Gamma of the portfolio are
∆= −∂Ft
∂St
+ φt + κt
∂Ct
∂St
and
Γ = −∂2Ft
∂S2
t
+ κt
∂2Ct
∂S2
t
.
(17.10)
We can set Γ to zero by choosing
κt =
∂2Ft
∂S2
t
∂2Ct
∂S2
t
,
(17.11)
which allows us to set ∆equal to zero if we take
φt = ∂Ft
∂St
−
∂2Ft
∂S2
t
∂2Ct
∂S2
t
∂Ct
∂St
.
(17.12)
106

For example, we could Gamma hedge a short position in a binary call option
by holding both the underlying asset and a call option on it.
Exercise 17.2 Construct a Gamma hedged position for a portfolio which is
short a binary call option with a strike price of $110 using the underlying
asset which has a price of $100 and a call option with a strike price of $120.
Assume that r = 0.05, σ = 0.20 and that both options have a maturity of
T = 1.0.
Exercise 17.3 Can you Gamma hedge a short position in a call option with
strike K by using the underlying and a call option of a different strike? Give
a specific example.
17.3
Put-Call Parity
There is an interesting and useful relationship between the value of a call
option and the value of the corresponding put option, that is, the put option
with the same maturity and strike price on the same underlying. Consider a
position which is long the call and short the put. The payofffunction is
F(ST)
=
C(ST) −P(ST)
=
max[ST −K, 0] −max[K −ST, 0]
=
max[ST −K, 0] + min[ST −K, 0]
=
ST −K.
(17.13)
But this is simply the payofffunction for a forward contract with strike
K.
We have previously shown that the value of the forward contract is
S0 −Ke−rT.
Hence the initial prices of the call and put portfolio must
simply equal this value
C0 −P0 = S0 −Ke−rT.
(17.14)
This is the put-call parity relation.
Exercise 17.4 Derive the put-call relation when St is the price of sterling in
dollars and the interest rates are r and ρ for dollars and pounds respectively.
107

We can also derive a put-call relation for the binary options. Consider
a portfolio which is long both a put and call option with the same strike K
and maturity T. The payofffunction is
F(ST)
=
BCT(ST) + BPT(ST)
=
H(ST −K) + H(K −ST)
=
1.
(17.15)
Hence the payoffis always one dollar. The initial price of a dollar is simply
e−rT, and hence
BC0 + BP0 = e−rT.
(17.16)
Exercise 17.5 Using the Black-Scholes formulae for the put and call option
prices verify the put-call relation.
108


## Continuous Dividend Model

18
Continuous Dividend Model
There is a relatively simple but important adjustment that must be made to
the Black-Scholes formula in order to take into account the fact that stocks
pay dividends. These are typically relatively small payments made from time
to time to the shareholders. The fact that dividends are paid to the owner
of a stock means that the no arbitrage argument for pricing a derivative on
the stock has to be modified. For simplicity, we shall assume that dividends
are paid continuously over time at a rate δtSt. In other words, the holder of
the share at time t receives a dividend δtStdt in the time interval from t to
t + dt.
The situation is similar with a foreign currency. If St denotes the value
of a foreign currency at time t, say, the price of one pound sterling in dollars,
then the holder of that currency, assuming it is kept in a money market
account, is paid interest on it. The amount of interest paid in the interval t
to t + dt is δtStdt, where δt is the foreign interest rate. Note that in many
circumstances interest really is paid on a continuous basis, whereas dividends
are certainly not. If the underlying is taken to be a stock index, then the
approximation of continuous dividends is more valid.
We begin our work on the dividend model by calculating the cost of a
forward contract to buy one share for K dollars at time T, assuming that
the dividend yield δ is constant. The initial cost of the contract is F0 dollars
and the final payoffis FT(ST) = ST −K. We can replicate this payoffby
buying a portfolio which is long e−δT shares and short Ke−rT bonds. The
initial value of this position is
V0 = S0e−δT −Ke−rT
(18.1)
We want to continuously reinvest the dividends back into shares. Thus the
share holding ψt satisfies the differential equation
dψt = δdt
(18.2)
since we receive δStdt dollars in each small time interval and this can be
used to buy δdt more shares, which each cost St. Hence the share holding is
ψt = ψ0eδt. Thus the final value of the portfolio is
VT = ST −K,
(18.3)
109

which is the payofffrom the forward contract. Since the final payoffs are the
same, the initial values of the two positions must also be the same, and so
F0 = S0e−δT −Ke−rT.
(18.4)
The forward price ˜S is the value of the strike price for which the initial cost
of the forward contract is zero. It is easy to see that
˜S = S0e(r−δ)T.
(18.5)
Exercise 18.1 What is the put-call relation for the constant dividend yield
model?
Now let us consider a local arbitrage argument that will eventually lead us
to a generalisation of the Black-Scholes equation. Assume that the underlying
asset price process is given by the usual stochastic differential equation
dSt
St
= µtdt + σtdWt,
(18.6)
where the drift µt, the volatility σt, the dividend rate (or foreign interest
rate) δt and the ‘domestic’ interest rate rt are all ‘adapted’ to the Brownian
motion Wt.
Suppose that we also have a derivative with price Ct at time t, with drift
µC
t , volatility σC
t and that it satisfies the dynamics
dCt
Ct
= µC
t dt + σC
t dWt.
(18.7)
Our goal is to discover the no-arbitrage relation between St and Ct, which
will take the form of a relation between µt, σt, δt, rt, µC
t and σC
t .
Note
that as in the previous case, Ct does not actually have to be a derivative of
St, but merely must be driven by the same Brownian motion Wt. For the
sake of symmetry, let us also suppose that the derivative pays a continuous
dividend, at the rate δC
t , which we also assume to be adapted to Wt. It might
be thought that too many processes are being adapted to the same source
Brownian motion. This defect will be cured later when we consider multiple
assets and multiple sources of randomness.
This time we shall present the arbitrage argument from the point of view
of a ‘dealer’, who ‘sells’ the derivative to a client for the price Ct, and wants
to hedge his risk by buying φt units of stock at price St. Thus, the dealer
proceeds as follows:
110

• First, he borrows φtSt −Ct dollars from a bank, at the continuously
compounded interest rate rt.
• Next, the derivative is sold to the client for Ct.
• Finally, φt units of stock are bought, for φtSt dollars.
The value of the dealer’s position (long the stock and short the derivative)
is thus
Vt = φtSt −Ct.
(18.8)
In other words, to ‘close down’ the position the dealer would have to sell φt
units of stock, and buy back the derivative, giving a total value Vt, which
might be negative. The change in the value of the position over the small
time interval from t to t + dt is given by
dVt = φtdSt −dCt + δφtStdt −δCCtdt.
(18.9)
The last two terms appear because the dealer has had to pay a small div-
idend δC
t Ctdt to the holder of the derivative, but at the same time gets a
dividend δtφtStdt on the shares. Substituting in for dSt and dCt from the
price processes for the stock and the derivative, we obtain
dVt = φt(µtStdt+σtStdWt)+φtStδdt−(µC
t Ctdt+σC
t CtdWt)−CtδC
t dt. (18.10)
More explicitly, gathering terms together we have
dVt = (φtµtSt + φtδtSt −µC
t Ct −δC
t Ct)dt + (φtσtSt −σC
t Ct)dWt.
(18.11)
To ensure a definite rate of return on the hedged position, the dealer must
ensure that the coefficient of dWt is made to vanish in this expression, so
that the hedge ratio φt is given by
φt = σC
t Ct
σtSt
.
(18.12)
Note that the inclusion of dividends does not affect the formula for the hedge
ratio, which agrees with the result calculated previously in equation (14.1).
Thus the change in the hedged position dVt, obtained by substituting the
hedge ratio (18.12) into (18.11), is given by
dVt = [(µt + δt)σC
t
σt
−(µC
t + δC
t )]Ctdt,
(18.13)
111

whereas the value Vt = φtSt −Ct of the dealer’s position is
Vt =
ÃσC
σ −1
!
Ct.
(18.14)
For no arbitrage, the gains on the dealer’s risk-free position must be equal to
the corresponding gains one would earn from a bank account with interest
rate rt, so
dVt = rVtdt.
(18.15)
It follows by substitution that
(µt + δt)σC
t
σt
+ (µC
t + δC
t ) = rt
ÃσC
t
σt
−1
!
,
(18.16)
which therefore implies
µt + δt −rt
σt
= µC
t + δC
t −rt
σC
t
.
(18.17)
This is the no arbitrage relation in the presence of dividends. Or equivalently,
if we interpret St as the price of a foreign currency (in units of domestic cur-
rency) then δt has the interpretation of a foreign interest rate, and (18.17)
is the no arbitrage condition for derivatives based on that currency. The fi-
nancial interpretation of this relation is that the total excess return (‘capital’
gains plus dividends) above the risk-free interest rate, per unit of risk (volatil-
ity), is the same for both the underlying asset and the derivative, or more
generally, for any two instruments driven by the same Brownian motion.
18.1
Modified Black-Scholes Equation
Let us see what implications the inclusions of dividends has for the Black-
Scholes equation. As in the previous derivation we assume that Ct = C(St, t).
Ito’s lemma then implies that
µC = 1
Ct
"∂C
∂t + µS ∂C
∂S + 1
2σ2S2∂2C
∂S2
#
,
(18.18)
and
σC = 1
Ct
"
σS ∂C
∂S
#
.
(18.19)
112

Here, to simplify the notation slightly, we temporarily drop the time sub-
scripts on the processes µt, σt, δt, rt, µC
t , σC
t and δC
t . As a consequence of
the no-arbitrage relation (18.17) we have
(µ + δ −r)σC
σ Ct = (µC + δC −r)Ct,
(18.20)
which follows by multiplying equation (18.17) by σCCt. Substituting in the
expressions for µC and σC obtained above, we see therefore that
(µ + δ −r)St
∂C
∂S = ∂C
∂t + µS ∂C
∂S + 1
2σ2S2∂2C
∂S2 + (δC −r)Ct.
(18.21)
Note that once again the terms involving µ cancel, and we are left with
∂Ct
∂t + 1
2σ2S2
t
∂2Ct
∂S2
t
= (r −δC)Ct −(r −δ)St
∂Ct
∂St
.
(18.22)
This is the Black-Scholes equation as modified for the inclusion of dividends.
Exercise 18.2 Using an argument similar to that in exercise 13.1 derive the
modified Black-Scholes equation.
18.2
Call and Put Option Prices
Now suppose that we specialize to the case when µ, σ, δ, r and δC are
constant. Then by careful comparison with the transformations used earlier
to convert the Black-Scholes equation to the heat equation, we find that the
solutions are essentially the same as before, except that we use Ft = S0e(r−δ)t
for the forward price, while the overall discount factor is e−(r−δC)t. Thus the
solution is
C0 = e−(r−δC)T
√
2π
Z ∞
−∞F(S0e(r−δ)T+σ
√
Tξ−1
2 σ2T)e−1
2 ξ2dξ
(18.23)
for a general European-style derivative with payoffF(ST) at time T. Note
that the presence of the continuous dividend δC paid out on the derivative
holding itself makes the value of C0 at time 0 greater than it would be oth-
erwise, since, in addition to the final payoff, the investor also gets all the
dividends.
113

Exercise 18.3 Show that (18.23) solves (18.22) with the required boundary
conditions.
For the Black-Scholes formula based on a dividend paying stock in the
case of a basic call option, with no dividends paid on the option itself, we
obtain
C0 = e−rT[S0e(r−δ)TN(h+) −KN(h−)],
(18.24)
where
h± = ln( ˜ST/K) ± 1
2σ2T)
σ
√
T
.
(18.25)
Here ˜ST = S0e(r−δ)T is the no arbitrage forward price for the dividend paying
stock or interest paying foreign currency at time T.
Exercise 18.4 Derive (18.24) from (18.23) in the case of a call option.
Exercise 18.5 Calculate the initial cost of a binary call option.
114


## Risk-Neutral Valuation

19
Risk Neutral Valuation
So far we have considered the situation where there are just two assets—
the basic asset with price St, and the money market account with price Bt.
The ‘economy’ is driven by a single Brownian motion Wt. In this formalism
a derivative is viewed as an additional ‘special’ asset with price Ct that is
inserted into the economy, subject to a no arbitrage condition that relates
its dynamics to those of the basic asset and the money market account.
A more flexible approach is to introduce at the outset an economy based
on a number of assets with prices Si
t(i = 1, . . . , n). These assets can include
derivatives, but now the derivatives are not treated any differently from the
underlying assets on which they are based. Since there must be additional
sources of randomness in the market, we want the entire system to be driven
by a multi-dimensional Brownian motion W α
t (α = 1, . . . , N). Typically, we
want n ≥N. This is a complicated area of research that we shall only touch
only briefly in the final two chapters of the book. In order to prepare for this
and develop the necessary mathematics, we shall first re-examine the single
asset model using the ‘martingale’ method.
19.1
Single Asset Case
Recall that the stochastic differential equation for the share price in the single
asset model is
dSt
St
= µtdt + σtdWt,
(19.1)
where µt and σt are adapted processes, that is, they depend only on the
‘history’ of the Brownian motion from time 0 to time t, and no other ‘source
of randomness’. In the case where µ, σ are constant, the solution of (19.1) is
given by
St = S0 exp
µ
µt + σWt −1
2σ2t
¶
.
(19.2)
How do we solve this equation?
Perhaps the easiest way is to make the
variable substitution Xt = log St. The stochastic differential equation for Xt
can then be calculated using Ito’s lemma,
dXt
=
∂Xt
∂St
dSt + 1
2
∂2Xt
∂S2
t
dS2
t
=
dSt
St
−1
2
dS2
t
S2
t
115

=
µtdt + σtdWt −1
2σ2
t dt
(19.3)
In the case of constant coefficients µ and σ we can integrate the equation to
obtain
Xt = X0 + µt + σWt −1
2σ2t.
(19.4)
But since St = eXt, we see that
St = S0 exp
µ
µt + σWt −1
2σ2t
¶
.
(19.5)
We shall call this the Black-Scholes model for a single asset.
However, suppose that we do not want to restrict ourselves to the constant
coefficient case. We could still integrate equation (19.3) to obtain
Xt = X0 +
Z t
0 µsds +
Z t
0 σsdWs −1
2
Z t
0 σ2
sds,
(19.6)
which then yields the more general solution
St = S0 exp
·Z t
0 µsds +
Z t
0 σsdWs −1
2
Z t
0 σ2
sds
¸
.
(19.7)
If µ and σ are constant, then formula (19.7) reduces to (19.2). We shall call
(19.7) the basic model for a single asset.
Now that we have defined and solved for the asset price, we want to
consider the money market account Bt. Its stochastic differential equation is
dBt
Bt
= rtdt,
(19.8)
where rt is the short term interest rate. In the Black-Scholes model, where
all the coefficients are constant, this has the solution
Bt = B0ert.
(19.9)
In the basic model we place no constraints on the interest rate, and hence
have the more general solution
Bt = B0 exp
·Z t
0 rsds
¸
.
(19.10)
From now on we shall assume that B0 = 1.
116

We now want to introduce a new stochastic process that we shall call the
risk premium or market price of risk process λt, and defined by the equation
µt = rt + λtσt.
(19.11)
The risk premium is the ‘extra’ rate of return, above the short term rate,
per unit of risk, as measured by the volatility. Then equation (19.1) can be
written in the form
dSt
St
= (rt + λtσt)dt + σtdWt,
(19.12)
or equivalently,
dSt
St
= rtdt + σt(λtdt + dWt).
(19.13)
More specifically the asset price process (19.7) can be written as
St
=
S0 exp
·Z t
0 rsds +
Z t
0 σs(dWs + λsds) −1
2
Z t
0 σ2
sds
¸
St
=
S0Bt exp
·Z t
0 σs(dWs + λsds) −1
2
Z t
0 σ2
sds
¸
,
(19.14)
where we have substituted in the value of Bt from equation (19.10). Thus
for the ratio St/Bt we have
St
Bt
= S0 exp
·Z t
0 σs(dWs + λsds) −1
2
Z t
0 σ2
sds
¸
.
(19.15)
Now suppose that we define the process ρt by
ρt = exp
·
−
Z t
0 λsdWs −1
2
Z t
0 λ2
sds
¸
.
(19.16)
By use of Ito’s Lemma, is is straightforward to verify that the stochastic
differential of ρt is given by
dρt = −ρtλtdWt,
(19.17)
and hence is driftless, and thus ρt is a martingale. Now let us consider the
product
Πt = ρtSt
Bt
.
(19.18)
117

This is given, in more explicit terms, by
Πt
=
S0 exp
·
−
Z t
0 λsdWs −−
Z t
0 λ2
sds
¸
exp
·Z t
0 σs(dWs + λsds) −1
2
Z t
0 σ2
sds
¸
=
S0 exp
·Z t
0 (σs −λs)dWs +
Z t
0 (−1
2λ2
s + σsλs −1
2σ2
s)ds
¸
=
S0 exp
·Z t
0 (σs −λs)dWs
¸
exp
·
−1
2
Z t
0 (λs −σs)2ds
¸
.
(19.19)
The stochastic differential of Πt is thus given by
dΠt = (σt −λt)ΠtdWt,
(19.20)
and since it is driftless, it follows that Πt is also a martingale.
Exercise 19.1 Show that if Xt is a stochastic process such that
dXt = f(Xt, t)dWt
(19.21)
then Xt is a martingale.
The martingale property for Πt can be written
Es
·
ρt
St
Bt
¸
= ρs
Ss
Bs
(19.22)
Now for any random variable Zt, adapted to the history of Wt from 0 to t,
we can define a new probability measure P ∗with expectation
E∗
s[Zt] ≡Es[ρtZt]
ρs
.
(19.23)
This is called a ‘change of measure’ and the idea is basic to finance. The
positive martingale ρt defining the change of measure is called the density
martingale.
In the present situation the new measure is called the risk-neutral mea-
sure. The significance of E∗
s is that from (19.22) we have
E∗
s
· St
Bt
¸
= Ss
Bs
,
(19.24)
118

which shows that the ratio St/Bt is a martingale in this measure.
This is completely analogous to the discrete time situation, in which the
risk-neutral probabilities are those for which the ratio of the asset price to
the money market account is a martingale.
Now suppose that Ct is the price of a derivative based on St, with payoff
CT at time T, where CT is a random variable adapted to the history of
the Brownian motion up to time T. Then for the process Ct we have the
stochastic equation
dCt
Ct
= µC
t dt + σC
t dWt.
(19.25)
We have shown already that the no arbitrage condition is given by
µC
t −rt
σC
t
= µt −rt
σt
,
(19.26)
which, since λt = (µt −rt)/σt, implies that
µC
t = rt + λtσC
t ,
(19.27)
and thus
dCt
Ct
= rtdt + σC
t (dWt + λtdt).
(19.28)
This is formally identical in structure to (19.13) so we can conclude that
ρtCt/Bt is a martingale, and hence
E∗
s
·Ct
Bt
¸
= Cs
Bs
.
(19.29)
That is to say, the process Ct/Bt is a martingale in the risk-neutral measure.
Thus, the initial value of the derivative is simply
E∗
0
·CT
BT
¸
= C0.
(19.30)
Note that nothing in this derivation used the fact that Ct is a derivative based
on the asset St. Hence it will hold for any financial instrument that is subject
to the same Brownian motion as St. Thus, in the risk-neutral measure, the
ratio of the price of any tradable asset to the price of the money market
account is always a martingale.
119

Exercise 19.2 What are the stochastic equations satisfied by
St
Bt
and
ρtSt
Bt
?
(19.31)
Exercise 19.3 Show that
ρt = 1 −
Z t
0 λsρsdWs.
(19.32)
Exercise 19.4 Suppose λ is constant and Xt = Wt.
Find E∗
s[Wt] and
E∗
s[W 2
t ].
Exercise 19.5 Show that ΠC
t is indeed a martingale under the measure E∗
s.
120


## Girsanov Transformation

20
Girsanov Transformation
Now we shall attempt to interpret more clearly the meaning of the risk-
neutral measure. We have shown that if the asset St satisfies
dSt
St
= rtdt + σt(dWt + λtdt),
(20.1)
where rt is the short-term interest rate, σt is the volatility, and λt is the risk
premium, all adapted, then
Πt = ρt
St
Bt
(20.2)
is a martingale. Here
Bt = exp
·Z t
0 rsds
¸
(20.3)
is the unit-initialised money market account and
ρt = exp
·
−
Z t
0 λsdWs −1
2
Z t
0 λ2
sds
¸
(20.4)
is the change of measure density martingale. Thus, Es[Πt] = Πs, and hence
E∗
s
· St
Bt
¸
= Ss
Bs
(20.5)
Here E∗
s is the (conditional) risk-neutral expectation operator, defined by
E∗
s[Xt] = Es[ρtXt]
ρs
(20.6)
for any random variable Xt adapted to the filtration of information available
up to time t.
If Ct is the value of a derivative based on the same information set, e.g.
with a payoffCT that depends on ST, then the process for Ct is, necessarily
of the form
dCt
Ct
= rtdt + σC
t (dWt + λtdt),
(20.7)
from which it follows that
ΠC
t = ρt
Ct
Bt
(20.8)
121

is also a martingale with repect to Es, and hence Ct/Bt is a martingale with
respect to the risk-neutral expectation E∗
s,
E∗
s
·Ct
Bt
¸
= Cs
Bs
.
(20.9)
Thus, for derivatives valuation we can write
C0 = E∗
0
·CT
BT
¸
.
(20.10)
In particular, if CT = F(ST), as in the case of a call option, then we have
C0 = E∗
0[F(ST)/BT]
(20.11)
where the terminal value of the asset ST is given by the random variable
ST = S0BT exp
"Z T
0 σs(dWS + λsds) −1
2
Z T
0 σ2
sds
#
.
(20.12)
20.1
Change of Drift
These formulae can all be simplified in an illuminating way by defining a new
random process W ∗
t ,
W ∗
t = Wt +
Z t
0 λsds,
(20.13)
which will turn out to be a Brownian motion with respect to the risk-neutral
measure. The stochastic differential of W ∗
t is given by
dW ∗
t = dWt + λtdt,
(20.14)
and thus for the asset process (19.1) we can write
dSt
St
= rtdt + σtdW ∗
t ,
(20.15)
while for Ct we have
dCt
Ct
= rtdt + σC
t dW ∗
t .
(20.16)
Hence the final asset price (20.12) is given by
ST = S0BT exp
"Z T
0 σsdW ∗
S −1
2
Z T
0 σ2
s
#
ds.
(20.17)
122

Now we shall outline an important result, known as Girsanov’s theorem,
which plays an important role in finance. We start with the process W ∗
t =
Wt +
R t
0 λsds, which can be interpreted as a general Brownian motion with
drift. We shall show that with respect to the new system of probabilities
governed by the measure E∗, the process W ∗
t satsfies the axioms of standard
Brownian motion. In other words, with respect to E∗, the process W ∗
t is
normally distributed, has independent increments, and the variance of W ∗
t is
t. To derive this result we need the following useful lemmas.
Lemma 20.1 A random variable X is normally distributed, with mean m
and variance V , if and only if its characteristic function φ(z) = E[eizX]
satisfies
E[eizX] = eizm−1
2 z2V .
(20.18)
Lemma 20.2
Two random variables X, Y are independent with respect to E[−] if and only
if their joint characteristic function factorises:
E[eiz1X+iz2Y ] = E[eiz1X]E[eiz2Y ]
(20.19)
We shall show first that with respect to E∗[−], the process W ∗
t , as given
by (20.13) is normally distributed, with mean zero and variance t. Consider
first the density martingale ρt. Since ρt is a martingale with initial value
unity, we have
E[ρt] = E
·
exp
µ
−
Z t
0 λsdWs −1
2
Z t
0 λ2
sds
¶¸
= ρ0 = 1.
(20.20)
Now suppose that we replace λs with λs −iz, where z is a (real) parameter,
and i = √−1. Then one can use Ito’s lemma to verify that dρt is still driftless,
hence we still have a martingale, and thus
E
·
exp
½
−
Z t
0 (λs −iz)dWs −1
2
Z t
0 (λs −iz)2ds
¾¸
= 1.
(20.21)
Expanding this expression we get
E
·
exp
½
−
Z t
0 λsdWs −1
2
Z t
0 λ2
sds
¾
× exp
½
iz(
Z t
0 dWs +
Z t
0 λsds)
¾
exp
½1
2
Z t
0 z2ds
¾¸
= 1,
(20.22)
123

which simplifies to the equation
E
·
ρt exp
½
iz(
Z t
0 dWs +
Z t
0 λsds)
¾¸
= exp
½
−1
2
Z t
0 z2ds
¾
(20.23)
or, equivalently,
E∗[eizW ∗
t ] = e−1
2 z2t.
(20.24)
Hence by lemma 20.1, we see that W ∗
t is indeed normally distributed with
respect to the measure E∗, with mean zero and variance t.
In order to show that the process W ∗
t has independent increments, we
need the idea of the indicator function, Is(a, b) for an interval [a, b].
We
define
Is(a, b) =
(
1
for
a ≤s ≤b
0
otherwise
(20.25)
Thus if 0 ≤a ≤b ≤t, then
Z t
0 Is(a, b)ds = b −a.
(20.26)
Now let us look at (20.20) again, this time making the substitution
λs →λs −iz1Is(a, b) −iz2Is(c, d)
(20.27)
where z1 and z2 are real parameters. Here we assume that 0 ≤a ≤b ≤c ≤
d ≤t. Then we know that
E[eXt] = 1,
(20.28)
where
Xt
=
−
Z t
0 [λs −iz1Is(a, b) −iz2Is(c, d)] dWs
−1
2
Z t
0 [λs −iz1Is(a, b) −iz2Is(c, d)]2 ds.
(20.29)
after some simplification this expression reduces to
Xt
=
−
Z t
0 λsdWs −1
2
Z t
0 λ2
sds + iz1
Z t
0 Is(a, b)[dWs + λsds] +
iz2
Z t
0 Is(c, d)[dWs + λsds] + 1
2z2
1
Z t
0 Is(a, b)ds
+1
2z2
1
Z t
0 Is(a, b)ds.
(20.30)
124

Then we can evaluate the integrals involving the indicator functions to obtain
Xt
=
−
Z t
0 λsdWs −1
2
Z t
0 λ2
sds + iz1( ˜Wb −˜Wb) + iz2( ˜Wd −˜Wc)
+1
2z2
1(b −a) + 1
2z2
1(b −a).
(20.31)
Substituting this back into (20.28), we get
E
h
ρt exp
n
iz1( ˜Wb −˜Wa)
+iz2( ˜Wd −˜Wc)
oi
=
exp
½
−1
2z2
1(b −a)
¾
× exp
½
−1
2z2
1(b −a)
¾
.
(20.32)
By lemma 20.2, this shows that with respect to the expectation E∗[−] =
E[ρt−], the increments W ∗
b −W ∗
a and W ∗
d −W ∗
c are independent random
variables, and each is normally distributed.
Thus, we have shown that W ∗
s is a Brownian motion with respect to
the expectation E∗[−]. That explains why the process (20.15) is called ‘risk
neutral’ with respect to E∗[−].
Now suppose that we let r and σ be constant. Then
ST = S0erT+σW ∗
T −1
2 σ2T
(20.33)
and
C0
=
E∗[CT
BT
]
=
e−rTE∗[F(S0erT+σW ∗
T −1
2σ2T)],
(20.34)
which is the formula we derived previously, by solving the Black-Scholes
equation, for valuing general European derivatives. Note that W ∗
T is normally
distributed with respect to E∗.
125

