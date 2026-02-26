# Analytic Methods for Option Pricing

!!! info "Source"
    **Computational Finance: Numerical Methods** by Clewlow and Strickland.
    These notes are used for educational purposes.

## Analytic Methods and Single Asset European Options

Chapter 8
Introduction
8.1
AN INTRODUCTION TO OPTIONS AND DERIVATIVES
In general, an option (also called a derivative, or contingent claim) is a contract
whose value depends on the future values that specified underlying quantities take
over a given time span. One use of options is as a means of providing insurance
against certain events which may happen in the future. For instance an airport, which
wants to insure against climatic risk, takes out a weather option. The contract for this
option may pay out a given amount of cash when the outside temperature either
exceeds or goes below certain prescribed levels.
This part of the book is concerned with financial options; that is options that
are based on the future value of various financial quantities that can be deter-
mined from the financial markets. A put option is an agreement to sell an asset in
the future for a fixed price the strike price, and a call is an agreement to buy an
asset in the future for a given price. Furthermore European options can only be
exercised at option maturity, whereas American options have greater flexibility and
can be exercised at any time up to option maturity.
Here we will discuss options whose value depends on the future prices of various
stocks and shares; these are called equity options. There are many different types of
equity options, see Hull (1997) for more detail.
If we want to buy or sell an equity option it is very important to determine its fair
value today. This will depend on the expected future values of the underlying stock
values, based on our current (and historical) information.
To do this it is necessary to model how the stock value changes with time. In Part II
of this book we will consider valuation models that are based on the assumption that the
asset price can be described by Brownian motion. In Part III we consider more complex
time series models for the asset price changes.
We will mainly be concerned with vanilla put and call options, however we do
provide some detailed coverage of barrier options. In most cases it should not be too
difficult to value more exotic options by modifying the supplied code.
We will consider the following computational methods for pricing options:
. Analytic methods and analytic approximations.
. Finite-difference lattices.

. Finite-difference grids.
. Simulation: Monte Carlo, using pseudorandom and quasirandom numbers.
We will discuss Brownian Motion and derive the Black–Scholes formula which is
used for pricing European options. We will also derive formulae for the value of
some commonly used European barrier options.
The value of a standard vanilla option depends on:
. The volatility of the underlying stock.
. The time to maturity.
. The strike price.
. The riskless interest rate.
. The dividends.
. Current value of the stock.
In the Black–Scholes setting the asset prices are assumed to follow a lognormal
process. This means that the logarithm of the asset prices has a Gaussian distribu-
tion, and the asset returns can be modelled as a Brownian process.
8.2
BROWNIAN MOTION
Brownian motion is named after the botanist Robert Brown who used a microscope
to study the fertilization mechanism of flowering plants. He first observed the
random motion of pollen particles (obtained from the American species Clarkia
pulchella) suspended in water, and wrote:
The fovilla or granules fill the whole orbicular disk but do not extend to the projecting
angles. They are not spherical but oblong or nearly cylindrical, and the particles have
manifest motion. This motion is only visible to my lens which magnifies 370 times. The
motion is obscure yet certain (Robert Brown, 12 June 1827; see Ramsbottom, 1932)
It appears that Brown considered this motion no more than a curiosity (he believed
that the particles were alive) and continued undistracted with his botanical research.
The full significance of his observations only became apparent about eighty years
later when it was shown, Einstein (1905), that the motion is caused by the collisions
that occur between the pollen grains and the water molecules. In 1908 Perrin, see
Perrin (1909), was finally able to confirm Einstein’s predictions experimentally. His
work was made possible by the development of the ultramicroscope by Zsigmondy
and Siedentopf in 1903. He was able to work out from his experimental results and
Einstein’s formula the size of the water molecule and a precise value for Avogadro’s
number. His work established the physical theory of Brownian motion and ended the
skepticism about the existence of atoms and molecules as actual physical entities.
Many of the fundamental properties of Brownian motion were discovered by Levy
(1939, 1948), and the first mathematically rigorous treatment was provided by
Wiener (1923, 1924). Karatzas and Shreve (1988) is an excellent text book on the
theoretical properties of Brownian motion, while Shreve et al. (1997) provides much
useful information concerning the use of Brownian processes within finance.
78
Pricing Assets

Brownian motion is also called a random walk, a Wiener process, or sometimes
(more poetically) the drunkards walk.
In formal terms a process Z ¼ (Zt : t  0) is (one-dimensional) Brownian motion if:
(i)
Zt is continuous, and Z0 ¼ 0
(ii)
Zt  N(0, t)
(iii) The increment dZdt ¼ Ztþdt  Zt is normally distributed as, dZdt  N(0, dt), so
E[dZdt] ¼ 0 and Var(dZdt) ¼ dt. The increment dZdt is also independent of the
history of the process up to time t.
From (iii) we can further state that, since the increments dZdt are independent of past
values Zt, a Brownian process is also a Markov process. In addition we shall now
show that Brownian process is also a Martingale process.
In a Martingale process Pt, t  0, the conditional expectation E(Ptþdt|F t) ¼ Pt,
where F t is called the filtration generated by the process and contains the information
learned by observing the process up to time t. Since for Brownian motion we have
EðZtþdtjF tÞ ¼ EððZtþdt  ZtÞ þ ZtjF tÞ ¼ EðZtþdt  ZtÞ þ Zt ¼ EðdZtþdtÞ þ Zt ¼ Zt
where we have used the fact that E[dZtþdt] ¼ 0. Since E(ZtþdtjF t) ¼ Zt, the Brownian
motion Z is a Martingale process.
We will now consider the Brownian increments over the time interval dt in more
detail. Over the time interval dt we have:
dXdt ¼ dZdt
ð8:1Þ
where dZdt is a random variable drawn from a normal distribution with mean zero
and variance dt, which we denote as dZdt  N(0, dt). Equation 8.1 can also be
written in the equivalent form:
dXdt ¼
ffiffiffiffi
dt
p

ð8:2Þ
where  is a random variable drawn from a standard normal distribution (that is a
normal distribution with zero mean and unit variance), and we use the notation
  N(0, 1).
Equations 8.1 and 8.2 give the incremental change in the value of X over the time
interval dt for standard Brownian motion.
We shall now generalize these equations slightly by introducing the extra (volatil-
ity) parameter  which controls the variance of the process. We now have:
dXdt ¼ dZdt
ð8:3Þ
where dZdt  N(0, dt), and dXdt  N(0, 2dt). Equation 8.3 can also be written in the
equivalent form:
dXdt ¼ 
ffiffiffiffi
dt
p
i;
i  Nð0; 1Þ
ð8:4Þ
Introduction
79

or equivalently
dXdt ¼
ffiffiffiffi
dt
p
0
i;
0
i  Nð0; 2Þ
ð8:5Þ
We are now in a position to provide a mathematical description of the movement
of the pollen grains in water observed by Robert Brown in 1827. We will start by
assuming that the container of water is perfectly level. This will ensure that there is no
drift of the pollen grains in any particular direction. Let us denote the position of a
particular pollen grain at time t by Xt, and set the position at t ¼ 0, X0, to zero. The
statistical distribution of the grain’s position, XT, at some later time t ¼ T, can be
found as shown below.
We divide the time T into n equal intervals dt ¼ T=n. Since the position of the
particle changes by the amount dXi ¼ 
ffiffiffiffi
dt
p
i over the ith time interval dt, the final
position XT is given by:
XT ¼
X
n
i¼1

ffiffiffiffi
dt
p
i


¼ 
ffiffiffiffi
dt
p
X
n
i¼1
i
Since i  N(0, 1), by the Law of Large numbers, see Appendix F.1, we have that the
expected value of position XT is:
E½XT ¼ 
ffiffiffiffi
dt
p
E
X
n
i¼1
i
"
#
¼ 0
The variance of the position XT is:
Var½XT ¼ Var 
ffiffiffiffi
dt
p
X
n
i¼1
i
"
#
¼ 2 dt Var
X
n
i¼1
i
"
#
ð8:6Þ
Using the fact that Var½i ¼ 1 and that
Var
X
n
i¼1
Xi
"
#
¼
X
n
i¼1
Var Xi
½
;
see Appendix F.3, we have:
Var½XT ¼ 2dt
X
n
i¼1
Var½i ¼ 2 dt
X
n
i¼1
1
ð8:7Þ
which gives:
Var½XT ¼ 2n dt ¼ T2
ð8:8Þ
So, at time T, the position of the pollen grain, XT is distributed as XT  N(0, T2).
If the water container is not perfectly level then the pollen grains will exhibit drift
in a particular direction. We can modify Equation 8.4 to take this into account as
follows:
dXdt ¼ dt þ 
ffiffiffiffi
dt
p
;
i  Nð0; 1Þ
ð8:9Þ
80
Pricing Assets

or equivalently
dXdt ¼ dt þ dZt;
dZt  Nð0; dtÞ
ð8:10Þ
where we have included the constant drift . Proceeding in a similar manner to that
for the case of zero drift Brownian motion we have:
XT ¼
X
n
i¼1
dt þ 
ffiffiffiffi
dt
p
i


¼ 
X
n
i¼1
dt þ 
ffiffiffiffi
dt
p
X
n
i¼1
i ¼ T þ 
ffiffiffiffi
dt
p
X
n
i¼1
i
which gives
E½XT ¼ E T þ 
ffiffiffiffi
dt
p
X
n
i¼1
i
"
#
¼ T þ 
ffiffiffiffi
dt
p
E
X
n
i¼1
i
"
#
¼ T
The variance of the position XT is:
Var½XT ¼ Var T þ 
ffiffiffiffi
dt
p
X
n
i¼1
i
"
#
¼ Var 
ffiffiffiffi
dt
p
X
n
i¼1
i
"
#
Here we have used the fact (see Appendix F.3) that Var½a þ bX ¼ b2Var½X, where
a ¼ T, and b ¼ 1. From Equations 8.6 to 8.8 we have:
Var½XT ¼ Var 
ffiffiffiffi
dt
p
X
n
i¼1
i
"
#
¼ T2
So, at time T, the position of the pollen grain, XT is distributed as XT  N(T, T2).
8.3
A BROWNIAN MODEL OF ASSET PRICE MOVEMENTS
In the previous section we showed how Brownian motion can be used to describe
the random motion of small particles suspended in a liquid. The first attempt at
using Brownian motion to describe financial asset price movements was provided
by Bachelier (1900). This however only had limited success because the significance
of a given absolute change in asset price depends on the original asset price. For
example a £1 increase in the value of a share originally worth £1.10 is much more
significant than a £1 increase in the value of a share originally worth £100. It is for
this reason that asset price movements are generally described in terms of relative
or percentage changes. For example if the £1.10 share increases in value by
11 pence and the £100 share increases in value by £10, then both of these price
changes have the same significance, and correspond to a 10 per cent increase in
value. The idea of relative price changes in the value of a share can be formalized
by defining a quantity called the return, Rt, of a share at time t. The return Rt is
defined as follows:
Rt ¼ Stþdt  St
St
¼ dSt
St
ð8:11Þ
Introduction
81

where Stþdt is the value of the share at time t þ dt, St is the value of the share at time t,
and dSt is the change in value of the share over the time interval dt. The percentage
return R, over the time interval dt is simply defined as R ¼ 100  Rt.
We are now in a position to construct a simple Brownian model of asset price
movements, further information on Brownian motion within finance can be found in
Shreve et al. (1997).
The asset return at time t is now given by:
Rt ¼ dSt
St
¼ dt þ dZt;
dZt  Nð0; dtÞ
ð8:12Þ
or equivalently:
dSt ¼ Stdt þ StdZt
ð8:13Þ
The process given in Equations 8.11 and 8.12 is termed Geometric Brownian
Motion; which we will abbreviate as GBM. This is because the relative (rather than
absolute) price changes follow Brownian motion.
We will now use Ito’s lemma (see Section 8.4) which allows us to write down the
process followed by the function (S, t), if the asset price S follows GBM. Ito’s
formula states, see Equation 8.21, that:
d ¼
S @
@S þ @
@t þ 2S2
2
@2
@S2


dt þ @
@S SdZ
where d denotes the increment in the function (S, t) over the time interval dt. This
means that if we choose (S, t) ¼ log (S), then we have:
@
@S ¼ @ logðSÞ
@S
¼ 1
S ;
@2
@S2 ¼ @
@S
@ logðSÞ
@S


¼ @
@S
1
S
 
¼  1
S2
@
@t ¼ @ logðSÞ
@t
¼ 0
Therefore if we let Y ¼ log (S) we have:
dY ¼ log Stþdt
St


¼ logðStþdtÞ  logðStÞ ¼
  2
2


dt þ dZ;
dZ  Nð0; dtÞ
or equivalently
dY  N
  1
2 2
	

dt; 2dt


If we now substitute the riskless interest rate, r, for the drift in the asset price, , we
obtain the following two equations:
log Stþdt
St


¼
r  2
2


dt þ dZ;
dZ  Nð0; dtÞ
ð8:14Þ
and
dY  N
r  1
2 2
	

dt; 2dt


ð8:15Þ
82
Pricing Assets

We have therefore shown that if the asset price follows GBM, then the logarithm
of the asset price Y follows standard Brownian motion. Another way of stating this is
that, over the time interval dt, the change in the logarithm of the asset price is a
Gaussian distribution with mean (r  2=2)dt and variance 2dt.
This is a very important result and will be referred to in later sections of the book.
8.4
ITO’S LEMMA IN ONE DIMENSION
In this section we will derive Ito’s formula, a more rigorous treatment can be found in
Shreve (1988).
Let us consider the stochastic process X:
dX ¼ adt þ bdZ ¼ adt þ b
ffiffiffiffi
dt
p
;
  Nð0; 1Þ;
dZ  Nð0; dtÞ
ð8:16Þ
where a and b are constants. We want to find the process followed by a function of
the stochastic variable X, that is (X, t). This can be done by applying a Taylor
expansion, up to second order, in the two variables X and t as follows:
 ¼  þ @
@X dX þ @
@t dt þ 1
2
@2
@X2 dX2 þ 1
2
@2
@t2 dt2 þ
@
@X@t dX dt
ð8:17Þ
where  is used to denote the value (X+dX, t+dt), and  denotes the value
(X, t). We will now consider the magnitude of the terms dX2, dX dt, and dt2 as
dt ! 0. First
dX2 ¼ ðadt þ b
ffiffiffiffi
dt
p
Þðadt þ b
ffiffiffiffi
dt
p
Þ ¼ a2dt2 þ 2ab dt3=2  þ b2dt2
then
dX dt ¼ adt2 þ b dt3=2 
So as dt ! 0, and ignoring all terms in dt of order greater than 1, we have:
dX2  b2dt 2;
dt2  0,
and
dXdt  0
If we now replace dX2 by its expected value E½dX2 we then have:
dX2  E½dX2 ¼ E½b2dt 2 ¼ b2dtE½2 ¼ b2dt
where we have used the fact that, since   N(0, 1), the variance of , E½2, is by
definition equal to 1. Using these values in Equation 8.17 and substituting for dX
from Equation 8.16, we obtain:
d ¼ @
@X adt þ bdZ
ð
Þ þ @
@t dt þ b2
2
@2
@X2 dt
ð8:18Þ
Introduction
83

where d ¼   . This gives Ito’s formula
d ¼
a @
@X þ @
@t þ b2
2
@2
@X2


dt þ @
@X bdZ
ð8:19Þ
In particular if we consider the Geometric Brownian process:
dS ¼ Sdt þ SdZ
ð8:20Þ
where  and  are constants then substituting X ¼ S, a ¼ S, and b ¼ S into
Equation 8.19 yields:
d ¼
S @
@S þ @
@t þ 2S2
2
@2
@S2


dt þ @
@S SdZ
ð8:21Þ
Equation 8.21 describes the change in value of a function (S, t) over the time
interval dt, when the stochastic variable S follows GBM. This result has very
important applications in the pricing of financial derivatives. Here the function
(S, t) is taken as the price of a financial derivative, f (S, t), that depends on the
value of an underlying asset S, which is assumed to follow GBM. In Section 9.3 we
will use Equation 8.21 to derive the (Black–Scholes) partial differential equation that
is satisfied by the price of a financial derivative.
8.5
ITO’S LEMMA IN MANY DIMENSIONS
We will now consider the n-dimensional stochastic process:
dXi ¼ aidt þ bi
ffiffiffiffi
dt
p
i ¼ aidt þ bidZi;
i ¼ 1; . . . ; n
ð8:22Þ
or in vector form:
dX ¼ Adt þ B
ffiffiffiffi
dt
p
E ¼ Adt þ BdZ
ð8:23Þ
where A and B are n element vectors respectively containing the constants,
ai, i ¼ 1, . . . , n and bi, i ¼ 1, . . . , n. The stochastic vector X contains the n stochastic
variables Xi, i ¼ 1, . . . , n, the vector E contains the n shocks i, i ¼ 1, . . . , n, and the
vector dZ contains the n shocks
ffiffiffiffi
dt
p
i, i ¼ 1, . . . , n.
We will assume that the random vector E is drawn from a multivariate normal
distribution with zero mean and covariance matrix C. That is we can write:
E  Nð0; CÞ
and
dZ  Nð0; dt CÞ
Since the diagonal elements of C are all unity
Cii ¼ E½2
i  ¼ 1;
i ¼ 1; . . . ; n
the matrix C is in fact a correlation matrix with off-diagonal elements given by:
Cij ¼ E½i j ¼ 	i; j;
i ¼ 1; . . . ; n;
j ¼ 1; . . . ; n;
i 6¼ j
where 	ij is the correlation coefficient between the ith and jth variates.
84
Pricing Assets

As in Section 8.4 we want to find the process followed by a function of the
stochastic vector X, that is the process followed by (X, t). This can be done by
applying any n-dimensional Taylor expansion, up to second order, in the variables X
and t as follows:
 ¼  þ
X
n
i¼1
@
@Xi
dXi þ @
@t dt þ 1
2
X
n
i¼1
X
n
j¼1
@2
@Xi@Xj
dXidXj þ 1
2
@2
@t2 dt2
þ
X
n
i¼1
@
@Xi@t dXidt
ð8:24Þ
where  is used to denote the value (X+dX, t+dt), and  denotes the value (X, t).
We will now consider the magnitude of the terms dXidXj, dXidt, and dt2 as dt ! 0.
Expanding the terms dXidXj and dXidt we have:
dXidXj ¼ ðaidt þ bi
ffiffiffiffi
dt
p
iÞðajdt þ bj
ffiffiffiffi
dt
p
jÞ
;dXidXj ¼ aiajdt2 þ aibj dt3=2j þ ajbi dt3=2i þ bibj dti j
dXidt ¼ aidt2 þ bidt3=2i
ð8:25Þ
So as dt ! 0, and ignoring all terms in dt of order greater than 1, we have:
dXidt  0
and
dXidXj  bibjdti j
If we now replace dXidXj by its expected value E½dXidXj we then have:
E½dXidXj ¼ E½bibjdtij ¼ bibjdt ¼ E½i j ¼ bibj	ijdt
where 	ij is the correlation coefficient between the ith and jth assets.
Using these values in Equation 8.24, and substituting for dXi from Equation 8.22,
we obtain:
d ¼
X
n
i¼1
@
@Xi
aidt þ bidZi
ð
Þ þ @
@t dt þ 1
2
X
n
i¼1
X
n
j¼1
bibj	ijdt
@2
@Xi@Xj
ð8:26Þ
where we have used d ¼   . This gives Ito’s n-dimensional formula:
d ¼
@
@t þ
X
n
i¼1
ai @
@Xi
þ 1
2
X
n
i¼1
X
n
j¼1
bibj	ij
@2
@Xi@Xj
(
)
dt þ
X
n
i¼1
@
@Xi
bidZi
ð8:27Þ
In particular if we consider the GBM:
dSi ¼ iSidt þ iSidZi;
i ¼ 1; . . . ; n
Introduction
85

where i is the constant drift of the ith asset and i is the constant volatility of the ith
asset, then substituting Xi ¼ Si, ai ¼ iSi, and bi ¼ iSi into Equation 8.27 then
yields:
d ¼
@
@t þ
X
n
i¼1
iSi @
@Si
þ 1
2
X
n
i¼1
X
n
j¼1
ijSiSj	ij
@2
@Si@Sj
(
)
dt
þ
X
n
i¼1
@
@Si
iSidZi
ð8:28Þ
86
Pricing Assets

Chapter 9
Analytic methods and single asset European
options
9.1
INTRODUCTION
A European option taken out at current time t gives the owner the right (but no
obligation) to do something when the option matures at time T. This could for
example be the right to buy or sell stocks at a particular strike price. The option
would of course only be exercised if it was in the owner’s interest to do so. For
example a single asset European vanilla put option, with strike price E and expiry
time T, gives the owner the right at time T to sell a particular asset for E. If the
asset is worth ST at maturity then the value of the put option at maturity,
known as the payoff, is thus max (E  ST, 0). By contrast a single asset European
vanilla call option, with strike price E and expiry time T, gives the owner the
right at time T to buy an asset for E; the payoff at maturity for a call option
is max (ST  E, 0).
The owner of an American option has the right (but no obligation) to exercise the
option at any time from current time t to option maturity. These options are more
difficult to value than European options because of this extra flexibility. Even
the simple single asset American vanilla put has no analytic solution and requires
finite-difference or lattice methods to estimate its value. Many European options on
the other hand take the form of a relatively easy definite integral from which it is
possible to compute a closed form solution. The valuation of multiasset European
options, dependent on a large number of underlying assets, is more complicated but
can conveniently be achieved by using Monte Carlo simulation to compute the
required multidimensional definite integral.
The expected current value of a single asset European vanilla option will depend on
the current asset price at time t, S, the duration of the option,  ¼ T  t, the strike
price, E, the riskless interest rate, r, and the probability density function of the
underlying asset price at maturity, p(ST). The fair price (expected current value) of
a vanilla call is thus:
cðS; E; ; r; pðSTÞÞ ¼ expðrÞE½maxðST  E; 0Þ
ð9:1Þ
¼ expðrÞ
Z 1
1
pðSTÞ maxðE  ST; 0ÞdST
ð9:2Þ

and that of the put is:
pðS; E; ; r; pðSTÞÞ ¼ expðrÞE½maxðE  ST; 0Þ
ð9:3Þ
¼ expðrÞ
Z 1
1
pðSTÞ maxðE  ST; 0ÞdST
ð9:4Þ
It can be seen from Equations 9.1 to 9.4 that the fair price of a European option is
its payoff, at time T, discounted by the riskless interest rate, r, to current time t.
Since we assume that r is constant throughout the duration of the option and also
that the underlying asset has a given distribution (usually lognormal), we will denote
the value of a European vanilla call option by c(S, E, ), and that of a European put
option by p(S, E, ).
In this section we will consider:
. The put–call parity relationship for European options.
. The differential equation obeyed by single asset and multiasset European options.
. The Black–Scholes option pricing formula for a single asset European option.
. The pricing formulae for some European barrier options.
The notation used will be that which we have previously outlined.
9.2
PUT–CALL PARITY
9.2.1
Discrete dividends
Here we consider single asset European put and call options, and derive the following
relationship between their values in the presence of cash dividends:
cðS; E; Þ þ E expðrÞ þ D ¼ pðS; E; Þ þ S
ð9:5Þ
where D is the present value of the dividends that are paid during the life of the
option. That is:
D ¼
X
n
k¼1
Dk expðrðtk  tÞÞ
with Dk the kth cash dividend paid at time tk; the other symbols have already been
defined in the section introduction.
This result can be proved by considering the following two investments:
Portfolio A
One European call, c(S, E, ), and cash of value E exp (r) þ D.
Portfolio B
One European put, p(S, E, ), and one share of value S.
At option maturity, time T, the value of the call and put are c(ST, E, 0) and
p(ST, E, 0) respectively; also at time T the value of the dividends paid during the life
of the option is D exp (r).
88
Pricing Assets

We now consider the value of both portfolios at option maturity, time T, under all
possible conditions.
If ST 	 E
Portfolio A is worth:
maxðST  E; 0Þ þ expðrÞ E expðrÞ þ D
f
g ¼ ST  E þ E þ D expðrÞ
¼ ST þ D expðrÞ
Portfolio B is worth:
maxðE  ST; 0Þ þ ST þ D expðrÞ ¼ 0 þ ST þ D expðrÞ ¼ ST þ D expðrÞ
If ST < E
Portfolio A is worth:
maxðST  E; 0Þ þ expðrÞ E expðrÞ þ D
f
g ¼ 0 þ E þ D expðrÞ ¼ E þ D expðrÞ
Portfolio B is worth:
maxðE  ST; 0Þ þ ST þ D expðrÞ ¼ E  ST þ ST þ D expðrÞ ¼ E þ D expðrÞ
We have therefore shown that under all conditions the value of portfolio A is the
same as that of portfolio B.
9.2.2
Continuous dividends
Here we consider single asset European put and call options, and derive the following
relationship:
cðS; E; Þ þ E expðrÞ ¼ pðS; E; Þ þ S expðqÞ
ð9:6Þ
where q is the asset’s continuous dividend yield that is paid during the life of the
option. The result can be proved by considering the following two investments:
Portfolio A
One European call, c(S, E, ), and cash of value E exp (r).
Portfolio B
One European put, p(S, E, ), and one share of value S exp (q).
At option expiry, time t, the value of the call and put are c(ST, E, 0) and
p(ST, E, 0) respectively. Also, if the value of the share at time t is denoted by
S, the combined value of shares and dividends at time T is S exp (q). Note that q
is treated in a similar manner to the continuously compounded riskless interest
rate r.
As in Section 9.2.1 we will now consider the value of portfolios A and B at time T
under all possible conditions:
Analytic methods and single asset European options
89

If ST 	 E
Portfolio A is worth:
maxðST  E; 0Þ þ expðrÞE expðrÞ ¼ ST  E þ E ¼ ST
Portfolio B is worth:
maxðE  ST; 0Þ þ ST expðqÞ expðqÞ ¼ 0 þ ST ¼ ST
where ST exp (q) exp (q) is the combined value of the shares and dividends at
option maturity.
If ST < E
Portfolio A is worth:
maxðST  E; 0Þ þ expðrÞE expðrÞ ¼ 0 þ E ¼ E
Portfolio B is worth:
maxðE  ST; 0Þ þ ST expðqÞ expðqÞ ¼ E  ST þ ST ¼ E
We have therefore shown that under all conditions the value of portfolio A is the
same as that of portfolio B.
9.3
VANILLA OPTIONS AND THE BLACK–SCHOLES MODEL
9.3.1
The option pricing partial differential equation
In this section we will derive the (Black–Scholes) partial differential equation that is
obeyed by options written on a single asset.
Previously, in Sections 8.4 and 8.5, we derived Ito’s lemma, which provides an
expression for the change in value of the function (X, t), where X is a stochastic
variable. When the stochastic variable, X, follows GBM, the change in the value of 
was shown to be given by Equation 8.21. Here we will assume that the function (S, t) is
the value of a financial option and that the price of the underlying asset, S, follows GBM.
If we denote the value of the financial derivative by f, then its change, df, over the
time interval dt is given by:
df ¼
S @f
@S þ @f
@t þ 2S2
2
@2f
@S2


dt þ @f
@S SdZ;
dZ  Nð0; dtÞ
The discretized version of this equation is:
f ¼ t S @f
@S þ @f
@t þ 2S2
2
@2f
@S2


þ @f
@S SdZ;
dZ  Nð0; tÞ
ð9:7Þ
where the time interval is now t and the change in derivative value is f .
If we assume that the asset price, S, follows GBM we also have:
S ¼ St þ SZ;
Z  Nð0; tÞ
ð9:8Þ
where  is the constant drift and the definition of the other symbols is as before. Let us
now consider a portfolio consisting of 1 derivative and @f =@S units of the underlying
90
Pricing Assets

stock. In other words we have gone short (that is sold) a derivative on an asset and have
@f =@S stocks of the (same) underlying asset. The value of the portfolio, , is therefore:
 ¼ f þ @f
@S S
ð9:9Þ
and the change, , in the value of the portfolio over time t is:
 ¼ f þ @f
@S S
ð9:10Þ
Substituting Equations 9.7 and 9.8 into Equation 9.10 we obtain:
 ¼  S @f
@S þ @f
@t þ 1
2 2S2 @2f
@S2


t  SZ @f
@S þ @f
@S St þ SZ
f
g
; ¼ St @f
@S  t @f
@t  1
2 t2S2 @2f
@S2  SZ @f
@S
þ St @f
@S þ SZ @f
@S
ð9:11Þ
Cancelling terms we obtain:
 ¼ t @f
@t þ 1
2 2S2 @2f
@S2


ð9:12Þ
If this portfolio is risk neutral then it grows at the riskless interest rate, r and we have:
rt ¼ 
So we have that:
rt ¼ t @f
@t þ 1
2 2S2 @2f
@S2


ð9:13Þ
Substituting for  and we obtain:
rt
f  S @f
@S


¼ t @f
@t þ 1
2 2S2 @2f
@S2


ð9:14Þ
On rearranging we have:
The Black–Scholes partial differential equation
@f
@t þ S @f
@S þ 1
2 2S2 @2f
@S2 ¼ rf
ð9:15Þ
Let us now consider put and call options on the same underlying asset. If we let c be
the value of a European call option and p that of a European put option then we have
the following equations:
@p
@t þ S @p
@S þ 1
2 2S2 @2p
@S2 ¼ rp
ð9:16Þ
Analytic methods and single asset European options
91

and
@c
@t þ S @c
@S þ 1
2 2S2 @2c
@S2 ¼ rc
ð9:17Þ
If we now form a linear combination of put and call options,  ¼ a1c þ a2p, where
both a1 and a2 are constants, then  also obeys the Black–Scholes equation:
@
@t þ S @
@S þ 1
2 2S2 @2
@S2 ¼ r
ð9:18Þ
We will now prove that  satisfies Equation 9.15.
First we rewrite Equation 9.15 as:
@ða1c þ a2pÞ
@t
þ S @ða1c þ a2pÞ
@S
þ 1
2 2S2 @2ða1c þ a2pÞ
@S2
¼ rða1c þ a2pÞ
ð9:19Þ
and use the following results from elementary calculus:
@ða1c þ a2pÞ
@t
¼ a1 @c
@t þ a2 @p
@t
@ða1c þ a2pÞ
@S
¼ a1 @c
@S þ a2 @p
@S
and
@2ða1c þ a2pÞ
@S2
¼ a1 @2c
@S2 þ a2 @2p
@S2
If we denote the left hand side of Equation 9.15 by LHS, then we have:
LHS ¼ a1
@c
@t þ S @c
@S þ 1
2 2S2 @2c
@S2


þ a2
@p
@t þ S @p
@S þ 1
2 2S2 @2p
@S2


ð9:20Þ
We now use Equations 9.13 and 9.14 to substitute for the values in the curly
brackets in Equation 9.19, and we obtain:
LHS ¼ a1rc þ a2rp
ð9:21Þ
which is just the LHS of Equation 9.21; so we have proved the result. It should be
noted that this result is also true for American options, since they also obey the
Black–Scholes equation.
The above result can be generalized to include a portfolio consisting of n single
asset options. Here we have:
 ¼
X
n
j¼1
aj fj;
j ¼ 1; . . . ; n
where fj represents the value of the jth derivative and aj is the number of units of the
jth derivative. To prove that  follows the Black–Scholes equation we simply parti-
tion the portfolio into sectors whose options depend on the same underlying asset.
We then proceed as before by showing that the value of each individual sector obeys
the Black–Scholes equation and thus the value of the complete portfolio (the sum
of the values of all the sectors) obeys the Black–Scholes equation. It should be
92
Pricing Assets

mentioned that this result applies for both American and European options and it
doesn’t matter whether we have bought or sold the options.
In Section 10.3.2 we will use the fact that the difference between the value of a
European option and the equivalent American option obeys the Black–Scholes
equation. We can see this immediately by considering the following portfolios that
are long in an American option and short (that is have sold) a European option:
p ¼ P  p;
c ¼ C  c
where P and C are the values of American put and call options. p and c both obey
the Black–Scholes equations, and are the respective differences in value of American/
European put options and American/European call options.
9.3.2
The multiasset option pricing partial differential equation
In this section we will derive the multiasset (Black–Scholes) partial differential equation
that is obeyed by options written on n assets. Proceeding as in Section 9.3.1 we will use
the n-dimensional version of Ito’s lemma to find the process followed by the the value of
a multiasset financial derivative. We will denote the value of this derivative by f (S, t),
where S is a n element stochastic vector containing the prices of the underlying assets,
Si, i ¼ 1, . . . , n. If we assume that S follows n-dimensional GBM then the change in the
value of the derivative, df, is (see Section 8.5, Equation 8.28) given by:
df ¼
@f
@t þ
X
n
i¼1
iSi @f
@Si
þ 1
2
X
n
i¼1
X
n
j¼1
ijSiSj
ij
@2f
@Si@Sj
(
)
dt þ
X
n
i¼1
@f
@Si
iSidZi
ð9:22Þ
The discretized version of this equation is:
f ¼
@f
@t þ
X
n
i ¼ 1
iSi @f
@Si
þ 1
2
X
n
i ¼ 1
X
n
j ¼ 1
ijSiSj
ij
@2f
@Si@Sj
(
)
t þ
X
n
i ¼ 1
@f
@Si
iSiZi ð9:23Þ
where the time interval is now t and the change in derivative value is f .
Let us now consider a portfolio consisting of 1 derivative and @f =@Si units of the
ith underlying stock. In other words we have gone short (that is sold) a derivative that
depends on the price, Si, i ¼ 1, . . . , n, of n underlying assets, and have @f =@Si units of
the ith asset. The value of the portfolio, , is therefore:
 ¼ f þ
X
n
i ¼ 1
@f
@Si
Si
ð9:24Þ
and the change, , in the value of the portfolio over the time interval t is:
 ¼ f þ
X
n
i ¼ 1
@f
@Si
Si
ð9:25Þ
Since the stochastic variables Si, i ¼ 1, . . . , n follow n-dimensional GBM the change
in the ith asset price, Si over the time interval t is given by:
Si ¼ iSit þ iSiZi;
i ¼ 1; . . . ; n
ð9:26Þ
Analytic methods and single asset European options
93

where Zi ¼ i
ffiffiffiffiffiffi
t
p
and, as in Section 8.5, we write:
E½2
i  ¼ 1;
i ¼ 1; . . . ; n
and
E½i j ¼ 
i; j;
i ¼ 1; . . . ; n;
j ¼ 1; . . . ; n;
i 6¼ j
Substituting Equations 9.23 and 9.26 into Equation 9.25 we obtain:
 ¼ 
@f
@t þ
X
n
i ¼ 1
iSi @f
@Si
þ 1
2
X
n
i ¼ 1
X
n
j ¼ 1
ij
ijSiSj
@2f
@Si@Sj
(
)
t

X
n
i ¼ 1
iSiZi @f
@Si
þ
X
n
i ¼ 1
@f
@Si
fiSit þ SiZig
; ¼ 
X
n
i ¼ 1
iSit @f
@Si
 t @f
@t  1
2 t
X
n
i ¼ 1
X
n
j ¼ 1
ij
ijSiSj
@2f
@Si@Sj

X
n
i ¼ 1
iSiZi @f
@Si
þ
X
n
i ¼ 1
iSit @f
@Si
þ
X
n
i ¼ 1
iSiZi @f
@Si
ð9:27Þ
Cancelling terms we obtain:
 ¼ t @f
@t þ 1
2
X
n
i ¼ 1
X
n
j ¼ 1
ij
ijSiSj
@2f
@Si@Sj
(
)
ð9:28Þ
If this portfolio is to grow at the riskless interest rate, r we have:
rt ¼ 
So from Equation 9.28 we have that:
rt ¼ t @f
@t þ 1
2
X
n
i ¼ 1
X
n
j ¼ 1
ij
ijSiSj
@2f
@Si@Sj
(
)
ð9:29Þ
Substituting for  and we obtain:
rt
f 
X
n
i ¼ 1
Si @f
@Si
(
)
¼ t
@f
@t þ 1
2
X
n
i ¼ 1
X
n
j ¼ 1
ij
ijSiSj
@2f
@Si@Sj
(
)
ð9:30Þ
94
Pricing Assets

Rearranging Equation 9.30 gives:
The n-dimensional Black–Scholes partial differential equation
@f
@t þ
X
n
i ¼ 1
Si @f
@Si
þ 1
2
X
n
i ¼ 1
X
n
j ¼ 1
ij
ijSiSj
@2f
@Si@Sj
¼ rf
ð9:31Þ
9.3.3
The Black–Scholes formula
In this section we will derive the Black–Scholes formula for pricing European put and
call options on a single asset which follows GBM. The approach we will adopt here is
to first derive an expression for the value of a European call option, and then use the
put/call parity relationships of Section 9.2 to obtain the value of the corresponding
European put option. If we denote the current time by t and the expiry time of the
option by T, then the duration of the option is  ¼ T  t. Since the asset is assumed
to follow GBM we can use a discretized version of Equations 8.14 and 8.15 in Section
8.3 to write:
log Stþt
St


 N
r  1
2 2


t; 2t


ð9:32Þ
Here we use the following notation:
t ¼ ;
St ¼ S,
and
Stþt ¼ ST
where S is the asset value at the current time t, and ST is the asset value at option
maturity. We will now introduce the variable X which we define as follows:
X ¼ log ST
S


or equivalently
ST ¼ S expðXÞ
From Equation 9.32 we have that
X  Nððr  2=2Þ; 2Þ
The probability density function of X, f (X ), is thus the Gaussian:
f ðXÞ ¼
1

ffiffiffi
p
ffiffiffiffiffi
2
p
exp  ðX  ðr  2=2ÞÞ2
22


The value of a European call option, c(S, E, ), with strike price E, is the expected
value of the option’s payoff at maturity discounted to the current time by the riskless
interest rate r. That is:
cðS; E; Þ ¼ expðrÞE½ST  E
Analytic methods and single asset European options
95

This can be rewritten in terms of the probability density function of ST as follows:
cðS; E; Þ ¼ expðrÞ
Z 1
ST ¼ E
f ðSTÞðST  EÞdST
ð9:33Þ
Instead of integrating over values of ST, as above, we will use ST ¼ S exp (X) and
then integrate over X. Equation 9.33 then becomes:
cðS; E; Þ ¼ expðrÞ

ffiffiffi
p
ffiffiffiffiffi
2
p
Z 1
X ¼ logðE=SÞ
S expðXÞ  E
ð
Þ
 exp  ðX  ðr  2=2ÞÞ2
22


dX
ð9:34Þ
where we have used S exp (X) ¼ E, giving X ¼ log (E=S), to obtain the lower limit of
the integral. This integral is evaluated by splitting it into the two parts:
cðS; E; Þ ¼ IA  IB
ð9:35Þ
where
IA ¼ S expðrÞ

ffiffiffi
p
ffiffiffiffiffi
2
p
Z 1
X ¼ logðE=SÞ
expðXÞ exp  X  ðr  2=2Þ

2
22
 
!
dX
ð9:36Þ
and
IB ¼ E expðrÞ

ffiffiffi
p
ffiffiffiffiffi
2
p
Z 1
X ¼ logðE=SÞ
exp  fX  ðr  2=2Þg2
22


EdX
ð9:37Þ
To evaluate these integrals we will make use of the fact that the univariate
cumulative normal function N1(x) is:
N1ðxÞ ¼
1ffiffiffiffiffi
2
p
Z x
u ¼ 1
exp  u2
2


du
by symmetry we have N1(x) ¼ 1  N1(x) and
1ffiffiffiffiffi
2
p
Z 1
x
exp  u2
2


du ¼
1ffiffiffiffiffi
2
p
Z x
1
exp  u2
2


du ¼ N1ðxÞ
We will first consider IB, which is the easier of the two integrals.
IB ¼ E expðrÞ

ffiffiffi
p
ffiffiffiffiffi
2
p
Z 1
X ¼ logðE=SÞ
exp  X  ðr  2=2Þ

2
22
 
!
dX
If we let u ¼ (X  (r  2=2))=
ffiffi
p
then
dX ¼ 
ffiffi
p du. So
IB ¼ E expðrÞ
ffiffiffi
p

ffiffiffiffiffi
2
p
ffiffiffi
p
Z 1
u ¼ k2
exp  u2
2


du
where the lower integration limit is k2 ¼ ( log (E=S) (r  2=2))=
ffiffiffi
p .
96
Pricing Assets

We therefore have:
IB ¼ E expðrÞN1ðk2Þ
ð9:38Þ
We will now consider the integral IA.
IA ¼ S expðrÞ

ffiffiffi
p
ffiffiffiffiffi
2
p
Z 1
X ¼ logðE=SÞ
expðXÞ exp  X  ðr  2=2Þ

2
22
 
!
dX
Rearranging the integrand:
IA ¼ expðrÞ

ffiffiffi
p
ffiffiffiffiffi
2
p
Z 1
X ¼ logðE=SÞ
exp  X  ðr  2=2Þ

2 22X
22
 
!
dX
ð9:39Þ
Expanding the terms in the exponential:
X  ðr  2=2Þ

2 22X ¼ X2  2 ðr  2=2Þ


X þ ðr  2=2Þ

2 22X
¼ X2  2 ðr þ 2=2Þ


X þ ðr  2=2Þ

2
¼
X  ðr þ 2=2Þ

2þ ðr  2=2Þ

2 ðr þ 2=2Þ

2
which results in:
X  ðr  2=2Þ

2 22X ¼
X  ðr þ 2=2Þ

2 22r2
ð9:40Þ
Substituting Equation 9.47 into the integrand of Equation 9.45 we have:
expðXÞ exp  X  ðr  2=2Þ

2
22
 
!
¼ expðrÞ exp  X  ðr þ 2=2Þ

2
22
 
!
The integral IA can therefore be expressed as:
IA ¼ S expðrÞ expðrÞ

ffiffiffiffiffi
2
p
Z 1
X ¼ logðE=SÞ
exp  X  ðr þ 2=2Þ

2
22
 
!
dX
If we let u ¼ (X  (r þ 2=2))=
ffiffiffi
p
then
dX ¼ 
ffiffiffi
p du. So
IA ¼
S
ffiffiffi
p

ffiffiffiffiffi
2
p
ffiffiffi
p
Z 1
u ¼ k1
exp  u2
2


du
where the lower limit of integration is k1 ¼ ( log (E=S)  (r þ 2=2))=
ffiffiffi
p .
We therefore have:
IA ¼ SN1ðk1Þ
ð9:41Þ
Therefore the value of a European call is:
cðS; E; Þ ¼ SN1ðk1Þ  E expðrÞN1ðk2Þ
Analytic methods and single asset European options
97

which gives the usual form of the Black–Scholes formula for a European call as:
The Black–Scholes formula for a European call
cðS; E; Þ ¼ SN1ðd1Þ  E expðrÞN1ðd2Þ
ð9:42Þ
where
d1 ¼ logðS=EÞ þ ðr þ 2=2Þ

ffiffiffi
p
and
d2 ¼ logðS=EÞ þ ðr  2=2Þ

ffiffiffi
p
¼ d1  
ffiffiffi
p
ð9:43Þ
To gain some insight into the meaning we will rewrite the above equation in the
following form:
cðS; E; Þ ¼ expðrÞ SN1ðd1Þ expðrÞ  EN1ðd2Þ
f
g
ð9:44Þ
The term N1(d2) is the probability that the option will be exercised in a risk-neutral
world, so that EN1(d2) is the strike price multiplied by the probability that the strike
price will be paid. The term SN1(d1) exp (r) is the expected value of a variable, in a
risk neutral world, that equals ST if ST > E and is otherwise zero.
The corresponding formula for a put can be shown using put–call parity, see
Section 9.2, to be:
The Black–Scholes formula for a European put
pðS; E; Þ ¼ E expðrÞN1ðd2Þ  SN1ðd1Þ
ð9:45Þ
where
d1 ¼ logðS=EÞ þ ðr þ 2=2Þ

ffiffiffi
p
and
d2 ¼ logðS=EÞ þ ðr  2=2Þ

ffiffiffi
p
¼ d1  
ffiffiffi
p
ð9:46Þ
or equivalently, using N1(x) ¼ 1  N1(x) we have
pðS; E; Þ ¼ E expðrÞ 1  N1ðd2Þ
f
g  S 1  N1ðd1Þ
f
g
ð9:47Þ
The inclusion of continuous dividends
The effect of dividends on the value of a European option can be dealt with by
assuming that the asset price is the sum of a riskless component involving known
dividends that will be paid during the life of the option, and a risky (stochastic)
component; see Hull (1997).
98
Pricing Assets

As dividends are paid the stock price is reduced by the same amount, and by the
time the European option matures, all the dividends will have been paid leaving only
the risky component of the asset price.
This means that, in the case of a continuous dividend yield q, European put/call
options can be priced using Equations 9.42 and 9.45 but with S replaced by
S exp (q).
This results in:
The Black–Scholes formula with continuous dividends
cðS; E; Þ ¼ S expðqÞN1ðd1Þ  E expðrÞN1ðd2Þ
ð9:48Þ
and the corresponding formula for a put can be shown (using put–call parity) to
be:
pðS; E; Þ ¼ E expðrÞN1ðd2Þ  S expðqÞN1ðd1Þ
ð9:49Þ
or equivalently, using N1(x) ¼ 1  N1(x), we have
pðS; E; Þ ¼ E expðrÞ 1  N1ðd2Þ
f
g  S expðqÞ 1  N1ðd1Þ
f
g
ð9:50Þ
where
d1 ¼ logðS=EÞ þ ðr  q þ 2=2Þ

ffiffiffi
p
and
d2 ¼ logðS=EÞ þ ðr  q  2=2Þ

ffiffiffi
p
¼ d1  
ffiffiffi
p
The above values of d1 and d2 are obtained by simply substituting S ¼ S exp ( q)
into Equation 9.43 as follows:
d1 ¼ logðS expðqÞ=EÞ þ ðr þ 2=2Þ

ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
ðT  tÞ
p
¼ logðS=EÞ  q þ ðr þ 2=2Þ

ffiffiffi
p
d2 ¼ logðS expðqÞ=EÞ þ ðr  2=2Þ

ffiffiffi
p
¼ logðS=EÞ  q þ ðr  2=2Þ

ffiffiffi
p
The inclusion of discrete dividends
Here we consider n discrete cash dividends Di, i ¼ 1, . . . , n, paid at times ti,
i ¼ 1, . . . , n during the life of the option. In these circumstances the Black–Scholes
formula can be used to price European options, but with the current asset value S
reduced by the present value of the cash dividends.
This means that instead of S we use the quantity SD which is computed as
SD ¼ S 
X
n
i¼1
Di expðrtiÞ
Analytic methods and single asset European options
99

where r is the (in this case constant) riskless interest rate. The formulae for European
puts and calls are then
cðS; E; Þ ¼ SDN1ðd1Þ  E expðrÞN1ðd2Þ
ð9:51Þ
pðS; E; Þ ¼ E expðrÞ 1  N1ðd2Þ
f
g  SD 1  N1ðd1Þ
f
g
ð9:52Þ
where
d1 ¼ logðSD=EÞ þ ðr þ 2=2Þ

ffiffiffi
p
and
d2 ¼ logðSD=EÞ þ ðr  2=2Þ

ffiffiffi
p
¼ d1  
ffiffiffi
p
ð9:53Þ
In Section 10.2.3 we give results for perpetual European options.
The greeks
Now that we have derived formulae to price European vanilla puts and calls it is
possible to work out their partial derivatives (hedge statistics). We will now merely
quote expressions for the Greeks (hedge statistics) for European options. Here the
subscript c refers to a European call, and the subscript p refers to a European put.
Complete derivations of these results can be found in Appendix C.
Gamma
c ¼ @2c
@S2 ¼ p ¼ @2p
@S2 ¼ expðqÞ nðd1Þ
S
ffiffiffi
p
ð9:54Þ
Delta
c ¼ @c
@S ¼ expðqÞN1ðd1Þ;
p ¼ @p
@S ¼ expðqÞ N1ðd1Þ  1
f
g
ð9:55Þ
Theta
c ¼ @c
@t ¼ qexpðqÞSN1ðd1ÞrE expðrÞN1ðd2ÞSnðd1ÞexpðqÞ
2
ffiffiffi
p
p ¼ @p
@t ¼ qexpðqÞSN1ðd1ÞþrE expðrÞN1ðd2ÞSnðd1ÞexpðqÞ
2
ffiffiffi
p
ð9:56Þ
Rho

c ¼ @c
@r ¼ EN1ðd2Þ;

p ¼ @p
@r ¼ EN1ðd2Þ
ð9:57Þ
Vega
Vc ¼ @c
@ ¼ Vp ¼ @p
@ ¼ S expðqÞnðd1Þ
ffiffiffi
p
ð9:58Þ
where n(x) ¼ (1=
ffiffiffiffiffi
2
p
) exp (x2=2).
100
Pricing Assets

We now present, in Code excerpt 9.1, a computer program to calculate the Black–
Scholes option value and Greeks given in Equations 9.54 to 9.57. The routine uses the
NAG C library macro X02AJC to identify whether the arguments are too small, and
also the NAG C library function s15abc to compute the cumulative normal
distribution function.
void black_scholes(double *value, double greeks[], double s0, double x,
double sigma, double t, double r, double q, Integer put, Integer *iflag)
{
/* Input parameters:
s0
—
the current price of the underlying asset
x
—
the strike price
sigma
—
the volatility
t
—
the time to maturity
r
—
the interest rate
q
—
the continuous dividend yield
put
Output parameters:
value
—
the value of the option
greeks[]
—
the hedge statistics output as follows: greeks[0] is gamma, greeks[1] is delta
greeks[2] is theta, greeks [3] is rho, and greeks[4] is vega
iflag
—
an error indicator
*/
double one¼1.0,two¼2.0,zero¼0.0;
double eps,d1,d2,temp,temp1,temp2,pi,np;
eps ¼ X02AJC;
if( (x < eps) || (sigma < eps) || (t < eps) ) { /* Check if any of the the input
arguments are too small */
*iflag ¼ 2;
return;
}
temp ¼ log(s0/x);
d1 ¼ tempþ(rqþ(sigma*sigma/two))*t;
d1 ¼ d1/(sigma*sqrt(t));
d2 ¼ d1sigma*sqrt(t);
/* evaluate the option price */
if (put¼¼0)
*value ¼ (s0*exp(q*t)*s15abc(d1)  x *exp (r *t) *s15abc (d2));
else
*value ¼ (s0*exp(q*t)*s15abc(d1)
þ x*exp(r*t)*s15abc (d2));
if (greeks){/* then calculate the greeks */
temp1 ¼ d1*d1/two;
d2 ¼ d1sigma*sqrt(t);
pi ¼ X01AAC;
np ¼ (one/sqrt(two*pi)) * exp(temp1);
if (put¼¼0) { /* a call option */
greeks[1] ¼ (s15abc(d1))*exp(q*t); /* delta */
greeks[2] ¼ s0*exp(q*t)*np*sigma/(two*sqrt(t))
þ q*s0*s15abc(d1)*exp(q*t)  r*x*exp(r*t) *s15abc (d2);/* theta */
greeks[3] ¼ x*t*exp(r*t)*s15abc(d2); /* rho */
}
else { /* a put option */
greeks[1] ¼ (s15abc(d1)  one)*exp(q*t); /* delta */
greeks[2] ¼ s0*exp(q*t)*np*sigma/(two*sqrt(t)) 
q*s0*s15abc(d1)*exp(q*t) þ r*x*exp(r*t)*s15abc (d2); /* theta */
greeks[3] ¼ x*t*exp(r*t)*s15abc(d2); /* rho */
}
greeks[0] ¼ np*exp(q*t)/(s0*sigma*sqrt(t)); /* gamma */
greeks[4] ¼ s0*sqrt(t)*np*exp(q*t); /* vega */
}
return;
}
Code excerpt 9.1
Function to compute the Black–Scholes value for European options
Analytic methods and single asset European options
101

It can be seen in Tables 9.1 and 9.2 that the values for gamma and vega are the
same for both puts and calls. We can also demonstrate that the option values are
consistent by using put–call parity.
cðS; E; Þ þ E expðrÞ ¼ pðS; E; Þ þ S expðqÞ
For example when  ¼ 1:0, we have c(S, E, ) ¼ 12:952 and P(S, E, T) ¼ 9.260.
So: c(S, E, ) þ E exp (r) ¼ 12:952 þ 100  exp (0:1) ¼ 103:436 and p(S, E, ) þ
S exp (q) ¼ 9:260 þ 100  exp (0:06) ¼ 103:436.
9.3.4
Historical and implied volatility
Obtaining the best estimate of the volatility parameter, , in the Black–Scholes
formula is of crucial importance. There are many different approaches to volatility
estimation. These include:
. Historical estimation
. Implied volatility
. Time series methods.
Table 9.1
European put: option values and greeks. The parameters are: S ¼ 100.0,
E ¼ 100.0, r ¼ 0.10,  ¼ 0.30, q ¼ 0.06

Value
Delta
Gamma
Theta
Vega
Rho
0.100
3.558
0:462
0.042
16:533
12.490
4:971
0.200
4.879
0:444
0.029
10:851
17.487
9:860
0.300
5.824
0:431
0.024
8:298
21.204
14:663
0.400
6.571
0:419
0.020
6:758
24.241
19:377
0.500
7.191
0:408
0.018
5:698
26.832
24:004
0.600
7.720
0:399
0.016
4:909
29.100
28:544
0.700
8.179
0:390
0.015
4:292
31.118
32:997
0.800
8.582
0:381
0.014
3:792
32.935
37:364
0.900
8.940
0:373
0.013
3:377
34.585
41:646
1.000
9.260
0:366
0.012
3:025
36.093
45:843
Table 9.2
European call: option values and greeks. The parameters are: S ¼ 100.0,
E ¼ 100.0, r ¼ 0.10,  ¼ 0.30, q ¼ 0.06

Value
Delta
Gamma
Theta
Vega
Rho
0.100
3.955
0.532
0.042
20:469
12.490
4.929
0.200
5.667
0.544
0.029
14:724
17.487
9.744
0.300
6.996
0.552
0.024
12:109
21.204
14.451
0.400
8.121
0.558
0.020
10:508
24.241
19.054
0.500
9.113
0.562
0.018
9:387
26.832
23.557
0.600
10.007
0.566
0.016
8:539
29.100
27.962
0.700
10.826
0.569
0.015
7:863
31.118
32.271
0.800
11.584
0.572
0.014
7:305
32.935
36.485
0.900
12.290
0.574
0.013
6:832
34.585
40.608
1.000
12.952
0.576
0.012
6:422
36.093
44.640
102
Pricing Assets

Here we will consider both historical and implied volatility estimation. Part III of
this book deals with the more complex issues connected with time series volatility
estimation.
Historical volatility
In this method we calculate the volatility using n þ 1 historical asset prices,
Si, i ¼ 0, . . . , n, and we assume that the asset prices are observed at the regular time
interval, d. Since the asset prices are assumed to follow GBM, the volatility is
computed as the annualized standard deviation of the n continuously compounded
returns, ui, i ¼ 1, . . . , n, where
Si ¼ Si1 expðuiÞ
or
ui ¼ log
Si
Si1


We already know, see Section 8.3, Equation 8.15, that the expected stand-
ard deviation of the asset returns over the time interval is 
ffiffiffiffiffi
d
p
. This means that
we obtain the following expression for ^, the estimated volatility
^
ffiffiffiffiffi
d
p
¼
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
1
n  1
X
n
i¼1
ðui  uÞ2
s
ð9:59Þ
or
^ ¼
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
1
ðn  1Þd
X
n
i¼1
ðui  uÞ2
s
ð9:60Þ
The estimated standard error in ^ is, see for example Hull (1997), given by
^std ¼ ^
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
1
2ðn  1Þ
s
ð9:61Þ
A computer program to perform these calculation is given below in Code excerpt 9.2.
void hist_vol(double *sigma, double *err, double data[], Integer n, double dt, Integer *ifail)
{
/*Input parameters:
data[]
— the data, which consists of n asset prices
n
— the number of data points
dt
— the (constant) time spacing between the data points (in years)
Output parameters:
sigma
— the computed historical volatility
err
— the standard error in the volatility estimate sigma
iflag
— an error indicator
*/
#define DATA(I) data[(I)1]
double mean¼0.0,sum¼0.0;
Analytic methods and single asset European options
103

double temp,tn;
Integer i;
for(i ¼ 2; i <¼ n; þþi)
mean ¼ mean þ log(DATA(i))log(DATA(i1));
mean ¼ mean/(double)(n1);
for(i ¼ 2; i <¼ n; þþi) {
temp ¼ log(DATA(i))log(DATA(i1));
sum ¼ sum þ (tempmean)*(tempmean);
}
sum ¼ sum/(double)(n2);
*sigma ¼ sqrt(sum/dt);
tn ¼ (double)(2*(n1));
*err ¼ *sigma/sqrt(tn);
return;
}
Code excerpt 9.2
Function to compute the historical volatility from asset data
Implied volatility
The implied volatility of a European option is the volatility which, when substituted
into the Black–Scholes formula, yields the market value quoted for the same option.
The routine provided in Code excerpt 9.2 uses Newton’s method to calculate the
implied volatility for a European option from its market price. We will now illustrate
this technique for a European call option with market value opt value. The
implied volatility, , is then that value which satisfies:
KðÞ ¼ cðS; E; ; Þ  opt value ¼ 0
where c(S, E, , ) represents the value of the European call and the other symbols
have their usual meaning.
From Newton’s method we have:
iþ1 ¼ i  FðiÞ
F 0ðiÞ
where
F 0ðiÞ ¼ @F
@ ¼ @cðS; E; ; Þ
@
¼ Vc
Therefore the iterative procedure is
iþ1 ¼ i  cðS; E; ; Þ  optvalue
Vc
where 0 is the initial estimate, and iþ1 is the improved estimate of the implied
volatility based on the ith estimate i. Termination of this iteration occurs when
ABS(iþ1  i) < tol, for a specified tolerance, tol.
It can be seen that as  ! 0, d1 ! 1, d2 ! 1 and, from Equation 9.58 we have
Vc ! 0. Under these circumstances Newton’s method fails.
The same procedure can be used to compute the implied volatility for a European
put, in this can we just replace c(S, E, , ) by p(S, E, , ), the value of a European
put; from Equation 9.58 Vc ¼ Vp.
104
Pricing Assets

void implied_volatility(double value, double s0, double x, double sigma[],
double t, double r, double q, Integer put, Integer *iflag)
{
/* Input parameters:
value
— the current value of the option
s0
— the current price of the underlying asset
x
— the strike price
sigma[]
— the input bounds on the volatility: sigma[0], the lower bound and, sigma[1], the upper bound
t
— the time to maturity
r
— the interest rate
q
— the continuous dividend yield
put
— if put is 0 then a call option, otherwise a put option
Output parameters:
sigma[]
— the element sigma[0] contains the estimated implied volatility
iflag
— an error indicator
*/
double zero¼0.0;
double fx, sig1, sig2;
double val,tolx;
double temp,eps,epsqrt,temp1,v1;
Integer max_iters, i, ind, ir;
double greeks[5],c[20],sig,vega;
Boolean done;
eps ¼ X02AJC;
tolx ¼ eps;
epsqrt ¼ sqrt(eps);
if(put ¼¼ 0)
/* a call option */
temp1 ¼ MAX(s0*exp(q*t)x*exp(r*t),zero);
else
/* a put option */
temp1 ¼ MAX(x*exp(r*t)s0*exp(q*t),zero);
v1 ¼ FABS(valuetemp1);
if (v1 <¼ epsqrt){
/* the volatility is too small */
*iflag ¼ 3;
return;
}
*iflag ¼ 0;
i ¼ 0;
max_iters ¼ 50;
done ¼ FALSE;
sig ¼ sigma[0];
/* initial estimate */
val ¼ value;
while ((i < max_iters) && (!done)){
/* Newton iteration */
black_scholes(&val,greeks,s0,x,sig,t,r,q,put,iflag);
/*computetheBlack—Scholesoptionvalue,val */
vega ¼ greeks[4];
/* and vega. */
sig1 ¼ sig  ((val  value)/vega);
/* compute the new estimate of sigma
using Newton’s method */
done ¼ (tolx > FABS ((sig1  sig)/sig1));
/* check whether the specified accuracy has been
reached */
sig ¼ sig1;
/* up date sigma */
þþi;
}
sigma[0] ¼ sig1;
/* return the estimate for sigma */
return;
}
Code expert 9.3
Function to compute the implied volatility of European options
If the implied volatility of American options is required, the procedure is exactly
the same. However, instead of using the Black–Scholes formula to compute both the
option value and Vega, we use a binomial lattice to do this. The use of binomial
lattices to obtain option prices and the Greeks is described in Section 10.4.
Below, in Code excerpt 9.4, is provided a simple test program which illustrates the
use of the function implied_volatility; the results are presented in Table 9.3.
double X, value, S, sigma[2], sigmat, T, r, q;
long i, ifail, put;
ifail
¼ 0;
Analytic methods and single asset European options
105

S
¼ 10.0;
X
¼ 10.5;
r
¼ 0.1;
sigmat
¼ 0.1;
q
¼ 0.04;
put
¼ 0;
printf (‘‘ Time option value implied volatility (Error)\n’’);
for(i ¼ 1;i < 6; þþi){
T ¼ (double)i*0.5;
black_scholes(&value,NULL,S,X,sigmat,T,r,q,put,&flag);
sigma[0] ¼ 0.05;
sigma[1] ¼ 1.0;
implied_volatility(value,S,X,sigmat,T,r,q,put,&flag);
printf(‘‘%8.4f
%15.4f
%15.4f (%8.4e)\n’’,T,value,sigma[0], FABS(sigmatsigma[0]));
sigmat ¼ sigmat þ 0.1;
}
Code excerpt 9.4
Simple test program for function implied_volatility
9.3.5
Pricing options with Microsoft Excel
In this section we show how the Visual Basic within Excel can be used to create
powerful derivative pricing applications based on the Black–Scholes formula. We
will explain how Excel’s Visual Basic can be used to create an application that prices
a selection of simple European put and call options at the press of a button.
In Section 9.3.3 we derived the Black–Scholes formula:
cðS; E; Þ ¼ SN1ðd1Þ  erEN1ðd2Þ and pðS; E; Þ ¼ SN1ðd1Þ þ erEN1ðd2Þ
where
d1 ¼ logðS=EÞðr  2=2Þ

ffiffiffi
p
¼ d1  
ffiffiffi
p
where S is the current value of the asset and  is the volatility of the asset, and
N1ðxÞ ¼
1ffiffiffiffiffi
2
p
Z x
1
ex2=2dx
The univariate cumulative standard normal distribution, N1(x), can be evaluated
in Excel by using its built in function NORMDIST. The definition of this function is
as follows:
NORMDISTðx; mean; standarddev; cumulativeÞ
This function returns the normal cumulative distribution for the specified mean and
standard deviation.
Table 9.3
Calculated option values and implied volatilities from Code excerpt 9.4
Time (in years)
Option value
True 
Error in estimated 
0.5
0.1959
0.1
2:7756  1016
1.0
0.8158
0.2
2:2204  1016
1.5
1.5435
0.3
3:8858  1016
2.0
2.3177
0.4
5:5511  1017
2.5
3.1033
0.5
1:1102  1016
106
Pricing Assets

Function parameters
x, is the value for which you want the distribution; mean, is the arithmetic mean of
the distribution; standard_dev, is the standard deviation of the distribution;
cumulative, is a logical value that determines the form of the function. If cumulative
is TRUE, NORMDIST returns the cumulative distribution function; if FALSE, it
returns the probability density function.
If mean ¼ 0 and standard_dev = 1, NORMDIST returns the standard normal
distribution.
This function can be used to create the following Visual Basic function to calculate
European option values within Excel.
Function bs_opt(S0 As Double, _
ByVal X As Double, sigma As Double, T As Double, _
r As Double, q As Double, ByVal putcall As Long) As Double
’ Visual Basic Routine to calculate the value of
’ either a European Put or European Call option.
Dim temp As Double
Dim d1 As Double
Dim d2 As Double
Dim SQT As Double
Dim value As Double
temp ¼ Log(S0 / X)
d1 ¼ temp þ (r  q þ (sigma * sigma / 2#)) * T
SQT ¼ Sqr(T)
d1 ¼ d1 / (sigma * SQT)
d2 ¼ d1  sigma * SQT
If (putcall ¼ 0) Then
’ a call option
value ¼ S0 * Exp(q * T) * WorksheetFunction.NormDist (d1, 0#, 1#, True)_
WorksheetFunction.NormDist(d2, 0#, 1#, True) * X * Exp(r * T)
Else
’ a put option
value ¼ S0 * Exp(q * T) * WorksheetFunction.NormDist(d1, 0#, 1#, True) þ _
X * WorksheetFunction.NormDist(d2, 0#, 1#, True) * Exp(r * T)
End If
bs_opt ¼ value
End Function
Code excerpt 9.5
Visual Basic code to price European options using the Black–Scholes formula
Once the function has been defined it can be accessed interactively using the Paste
Function facility within Excel as shown in Figure 9.1.
The function bs_opt can also be incorporated into other Visual Basic code within
Excel. To illustrate, if the following Visual Basic subroutine is defined:
Private Sub MANY_EUROPEANS_Click()
Dim i As Long
Dim putcall As Long
Dim S0 As Double
Dim q As Double
Dim sigma As Double
Dim T As Double
Dim r As Double
q ¼ 0#
T ¼ 1.5
Analytic methods and single asset European options
107

r ¼ 0.1
sigma ¼ 0.2
For i ¼ 1 To 22
S0 ¼ Sheet1.Cells(i þ 1, 1).value
X ¼ Sheet1.Cells(i þ 1, 2).value
putcall ¼ Sheet1.Cells(i þ 1, 3).value
Sheet1.Cells(i þ 1, 4).value ¼ bs_opt(S0, X, sigma, T, r, q, putcall)
Next i
End Sub
Code excerpt 9.6
Visual Basic code that uses the function bs_opt
When the button labelled ‘CALCULATE OPTIONS’ is clicked, the values of 22
European options will be calculated using the data in columns 1–3 on worksheet 1.
This is shown in Figures 9.2 and 9.3.
The cumulative standard normal distribution can also be used to provide analytic
solutions for a range of other exotic options such as: Barrier options, Exchange
options, Lookback options, Binary options, etc. A quick reference guide of the
formulae for various options is included in Appendix B.
Figure 9.1
Using the function bsopt interactively within Excel. Here a call option is priced with the
following parameters: S ¼ 10:0, X ¼ 9:0, q ¼ 0:0, T ¼ 1:5, r ¼ 0:1, and  ¼ 0:2
108
Pricing Assets

Figure 9.2
Excel worksheet before calculation of the European option values
Figure 9.3
Excel worksheet after calculation of the European option values
Analytic methods and single asset European options
109

9.4
BARRIER OPTIONS
9.4.1
Introduction
Barrier options are derivatives where the payoff depends on whether the asset price
reaches a given barrier level, B. Knockout options become worthless (cease to exist) if
the asset price reaches the barrier, whereas knockin options come into existence when
the asset price hits the barrier. We will consider the following single asset barrier
options:
. Down and out call: A knockout vanilla call option, value cdo(S, B, E, ), which
ceases to exist when the asset price reaches or goes below the barrier level.
. Up and out call: A knockout vanilla call option, value cuo(S, B, E, ), which ceases
to exist when the asset price reaches, or goes above the barrier level.
. Down and in call: A knockin vanilla call option, value cdi(S, B, E, ), which comes
into existence when the asset prices reaches or goes below the barrier level.
. Up and in call: A knockin vanilla call option, value cui(S, B, E, ), which comes into
existence when the asset price reaches or goes above the barrier level.
Since the following expressions must be true:
cðS; E; Þ ¼ cuoðS; B; E; Þ þ cuiðS; B; E; Þ
ð9:62Þ
cðS; E; Þ ¼ cdoðS; B; E; Þ þ cdiðS; B; E; Þ
ð9:63Þ
we need to only derive expressions for both the knockout options, and then use the
above equations to calculate the value of the corresponding knockin options.
The notation that we will use is as follows: E is the strike price, S is the current value of
the asset, B the barrier level, the symbol t represents the current time, T represents the
time at which the option matures and  ¼ T  t, the duration of the option. The symbol
s, with constraint t  s  T, is any intermediate time during which the option is alive.
9.4.2
Down and out call
If we consider Brownian motion (with zero drift) Xs  N(0, (s  t)2), t  s  T
which starts at Xt ¼ 0 and, after time  ¼ T  t, ends at the point XT ¼ X then (e.g.
Freedman, 1983) the probability density function for this motion not to exceed the
value X ¼ b (where b > 0) during time  is given by:
f ðb 	 X max
s
; XÞ ¼ 	
ffiffiffi
2

r
exp 2bðX  bÞ
2


exp  X2
22


ð9:64Þ
where
for
convenience
we
have
used
	 ¼ (2b  X)=33=2,
and
Xmax
s
¼
max (Xs, t  s  T ).
Since Xs is Brownian motion without drift, and volatility  then Xs is identical
Brownian motion. Therefore by substituting X ! X, and b ! b in the above
equation we obtain:
f ðb  X min
s
; XÞ ¼ 	
ffiffiffi
2

r
exp 2bðX  bÞ
2


exp  X2
22


ð9:65Þ
110
Pricing Assets

where we have used Xmin
s
¼ min (Xs, t  s  T). Equation 9.65 is the probability
density function of Xs staying above the value X ¼ b, where b < 0. These results
can be generalized to include drift (e.g. Musiela and Rutkowski, 1998, p. 212), so
that Xs  N((r  2=2)(s  t), (s  t)), for t  s  T. We now have the following
results:
f ðb 	 Xmax
s
; XÞ ¼ 	
ffiffiffi
2

r
exp 2bðX  bÞ
2


exp  ðX  ðr  2=2ÞÞ2
22


ð9:66Þ
f ðb  Xmin
s
; XÞ ¼ 	
ffiffiffi
2

r
exp 2bðX  bÞ
2


exp  ðX  ðr  2=2ÞÞ2
22


ð9:67Þ
A European down and out barrier option with maturity  and a barrier at
X ¼ B will cease to exist (become worthless) if at any time Xs  B, for t  s  T.
The probability density function that the barrier option will continue to exist at
time T if the end point is X is therefore:
f ðX > BÞ ¼ 
ffiffiffi
2

r Z b¼x
b¼logðB=SÞ
	 exp 2bðX  bÞ
2


 exp  X  ðr  2=2Þ

2
22
 
!
db
ð9:68Þ
or
f ðX > BÞ ¼ 
ffiffiffi
2

r
exp  X  ðr  2=2Þ

2
22
 
!

Z b¼X
b¼logðB=SÞ
	 exp 2bðX  bÞ
2


db
ð9:69Þ
where we have integrated over all possible values of b (i.e. B < b < X ) that keep the
option alive. Recalling that:

Z b¼X
b¼logðB=SÞ
	 exp 2bðX  bÞ
2


db ¼
Z b¼X
b¼logðB=SÞ
ðX  2bÞ
33=2
exp 2bðX  bÞ
2


db
and noting that:
@
@b exp 2bðX  bÞ
2


¼ 2ðX  2bÞ
2
exp 2bðX  bÞ
2


we have:
Z b¼X
b¼logðB=SÞ
2ðX  2bÞ
2
exp 2bðX  bÞ
2


db ¼ exp 2bðX  bÞ
2



b¼X
b¼logðB=SÞ
¼
1  exp 2 logðB=SÞðX  logðB=SÞÞ
2




Analytic methods and single asset European options
111

So the value of the option is given by:
f ðX > BÞ ¼
1

ffiffiffi
p
ffiffiffiffiffi
2
p
exp  X  ðr  2=2Þ

2
22
 
!

1  exp 2 logðB=SÞðX  logðB=SÞÞ
2




This integral is evaluated in Appendix G.1; here we merely state the result.
Down and out call option
cdo ¼ S
N1ðd1Þ  N1ðd4Þ B
S

2r=2þ1
 
!
 E expðrÞ N1ðd2Þ  N1ðd3Þ B
S
 2r=21
 
!
ð9:70Þ
where S is the current asset value, E the strike price, B the barrier level,  the
volatility, r the riskless interest rate,  the duration of the option, and:
d1 ¼ logðS=EÞ þ ðr þ 2=2Þ

ffiffiffi
p
;
d2 ¼ logðS=EÞ þ ðr  2=2Þ

ffiffiffi
p
;
d3 ¼ logðB2=SEÞ þ ðr  2=2ÞÞ

ffiffiffi
p
;
and
d4 ¼ logðB2=ESÞ þ ðr þ 2=2Þ

ffiffiffi
p
In Code excerpt 9.7 below we provide the function bs_opt_barrier_downout_
call which uses Equation 9.70 to price a down and out European call option.
This routine will be used in Sections 10.6.3 and 10.6.6 to measure the accuracy
achieved by using various finite-difference grid techniques to solve the Black–Scholes
equation.
void bs_opt_barrier_downout_call(double *value, double barrier_level,
double s0, double x, double sigma, double t, double r, Integer *iflag)
{
/* Input parameters:
barrier_level
—
the level of the barrier
s0
—
the current price of the underlying asset
x
—
the strike price
sigma
—
the volatility
t
—
the time to maturity
r
—
the interest rate
Output parameters:
value
—
the value of the option
iflag
—
an error indicator
*/
double one¼1.0,two¼2.0,zero¼0.0;
double eps,temp,temp1,temp2,a,b,d1,d2,d3,d4,d5,d6,d7,d8;
double fac;
112
Pricing Assets

eps ¼ X02AJC;
if(x < eps) {/* then strike price (X) is too small */
printf (‘‘ERROR X is too small nn’’);
return;
}
if (sigma < eps){/* then volatility (sigma) is too small */
printf (‘‘ERROR sigma is too small nn’’);
return;
}
if (t < eps){/* then time to expiry (t) is too small */
*ifail ¼ 3;
printf (‘‘ERROR option maturity is too small nn ’’);
return;
}
if (barrier_level ¼¼ 0){printf (‘‘ERROR barrier must be > zero nn’’);
fac ¼ sigma*sqrt(t);
temp1 ¼ oneþ(two*r/(sigma*sigma));
temp2 ¼ barrier_level/s0;
a ¼ pow(temp2,temp1);
temp1 ¼ oneþ(two*r/(sigma*sigma));
b ¼ pow(temp2,temp1);
if (x > barrier_level){
d1 ¼ (log(s0/x)þ(r þ 0.5*sigma*sigma)*t)/fac;
d2 ¼ (log(s0/x)þ(r  0.5*sigma*sigma)*t)/fac;
temp ¼(s0*x)/(barrier_level*barrier_level);
d7 ¼ (log(temp)(r  0.5*sigma*sigma)*t)/fac;
d8 ¼ (log(temp)(r þ 0.5*sigma*sigma)*t)/fac;
temp1 ¼ s0*(s15abc(d1)b*(ones15abc(d8)));
temp2 ¼ x*exp(r*t)*(s15abc(d2)a*(ones15abc(d7)));
*value ¼ temp1temp2;
}
else{/* x < ¼ barrier_level */
d3¼(log(s0/barrier_level)þ(r 0.5*sigma*sigma)*t)/fac;
d6¼ (log(s0/barrier_level)(r 0.5*sigma*sigma)*t)/fac;
d4 ¼ (log(s0/barrier_level)þ(rþ 0.5*sigma*sigma)*t)/fac;
d5 ¼ (log(s0/barrier_level)(rþ 0.5*sigma*sigma)*t)/fac;
temp1 ¼ s0*(s15abc(d3) b*(ones15abc(d6)));
temp2¼ x*exp(r*t)*(s15abc(d4)a*(ones15abc(d5)));
*value ¼ temp1temp2;
}
return;
}
Code excerpt 9.7
Function to compute the value for European down and out call options
9.4.3
Up and out call
Here we will obtain an expression for an up and out European call option in a similar
manner to that used in Section 9.3.5 for the down and out European call option. A
European up and out barrier option with maturity  and a barrier at X ¼ B will cease to
exist (become worthless) if at any time Xs 	 B, for t  s  T. The probability density
function that the barrier option will continue to exist at time T if the end point is X is
therefore:
f ðX < BÞ ¼
ffiffiffi
2

r Z B¼S expðbÞ
b¼X
	 exp 2bðX  bÞ
2t


 exp  X  ðr  2=2Þ

2
22
 
!
db
ð9:71Þ
Analytic methods and single asset European options
113

or
f ðX < BÞ ¼
ffiffiffi
2

r
exp  X  ðr  2=2Þ

2
22
 
!

Z b¼logðB=SÞ
b¼X
	 exp 2bðX  bÞ
2


db
ð9:72Þ
where as in Section 9.3.5 we have used 	 ¼ (2b  X)/33/2 and have integrated
overall possible values of b (i.e. B > b > X) that keep the option alive. Recalling that:
Z b¼logðB=SÞ
b¼X
	 exp 2bðX  bÞ
2


db ¼
Z b¼logðB=SÞ
b¼X
ð2b  XÞ
33=2
exp 2bðX  bÞ
2


db
and noting:
 @
@b exp 2bðX  bÞ
2


¼ 2ðX  2bÞ
2
exp 2bðX  bÞ
2


ð9:73Þ
we have:
Z b¼logðB=SÞ
b¼X
2ð2b  XÞ
2
exp 2bðX  bÞ
2


db ¼  exp 2bðX  bÞ
2



b¼logðB=SÞ
b¼X
¼
1  exp 2 logðB=SÞðX  logðB=SÞÞ
2




Therefore:
f ðX < BÞ ¼
1

ffiffiffi
p
ffiffiffiffiffi
2
p
ffiffiffi
2

r
exp  X  ðr  2=2Þ

2
22
 
!

1  exp 2 logðB=SÞðX  logðB=SÞÞ
2




ð9:74Þ
We will now derive the formula for an up and out call option when E < B. In fact
if E > B then the option is worthless, since at the current time t the call option’s
payout, max (St  E, 0) ¼ 0, and if St > E then the option will be knocked out.
cuo ¼ expðrÞ

ffiffiffi
p
ffiffiffiffiffi
2
p
Z 1
X¼logðE=SÞ
S expðXÞ  E
f
gf ðX < BÞdX
ð9:75Þ
Taking into account the fact the option becomes worthless when S exp (X) > B, (i.e.
X > log (B=S)) we have:
cuo ¼ expðrÞ

ffiffiffi
p
ffiffiffiffiffi
2
p
Z logðB=SÞ
X¼logðE=SÞ
S expðXÞ  E
f
gf ðX < BÞdX
ð9:76Þ
114
Pricing Assets

This integral is evaluated in Appendix G.2, and the value of the up and out call
option cuo is:
Up and out call option
cuo ¼ fN1ðk7Þ  N1ðk8ÞgS B
S
 2r=2þ1
 fexpðrÞN1ðk5Þ  N1ðk6ÞgE B
S
 2r=21
þ SfN1ðk2Þ  N1ðk1Þg  E expðrÞfN1ðk4Þ  N1ðk3Þg
ð9:77Þ
where S is the current asset value, E the strike price, B the barrier level,  the
volatility, r the riskless interest rate,  the duration of the option, and:
k1 ¼ logðE=SÞ  ðr þ 2=2ÞÞ

ffiffiffi
p
;
k2 ¼ logðB=SÞ  ðr þ 2=2Þ
ffiffiffi
p
k3 ¼ logðE=SÞ  ðr  2=2Þ

ffiffiffi
p
;
k4 ¼ logðB=SÞ  ðr  2=2Þ

ffiffiffi
p
k5 ¼ logðES=B2Þ  ðr  2=2ÞÞ

ffiffiffi
p
;
k6 ¼ logðS=BÞ  ðr  2=2ÞÞ

ffiffiffi
p
k7 ¼ logðES=B2Þ  ðr þ 2=2Þ

ffiffiffi
p
and k8 ¼ logðS=BÞ  ðr þ 2=2Þ

ffiffiffi
p
Analytic methods and single asset European options
115

Chapter 10
Numeric methods and single asset American
options
10.1
INTRODUCTION
In Chapter 9 we discussed single asset European options and the analytic formulae
which can be used to price them. Here we will consider the valuation of single asset
American style options using both numeric methods and analytic formulae; in
addition we will discuss the use of numerical techniques to value certain European
options. The coverage in this section is as follows:
. Analytic methods applied to perpetual European and American options.
. Analytic approximation techniques for the valuation of American options.
. Binomial lattice techniques used for the valuation of American and European
options.
. The valuation of American and European vanilla and barrier options using finite-
difference grids.
. The valuation of American options via Monte Carlo simulation.
It should be mentioned that although much of the discussion here concerns the
valuation of vanilla European and American puts and calls, the techniques used can
be modified without much difficulty to include more exotic options with customized
payoffs and early exercise features.
10.2
PERPETUAL OPTIONS
10.2.1
The perpetual American put
Here we derive the value, P(S, E), for a perpetual American put with strike price E on
an asset of current value S. This option can be exercised at any time, and so there is no
expiry date. Since the option is perpetual its payoff is time independent (see Merton
(1973)) and the Black–Scholes equation reduces to the following second order ordinary
differential equation:
2S2
2
d2V
dS2 þ ðr  qÞS dV
dS  rV ¼ 0
ð10:1Þ
where as usual S is the asset price, V is the option value,  is the volatility of the asset,
r is the riskless interest rate and q is the continuous dividend yield.

