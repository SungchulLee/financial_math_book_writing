# Interest Rate Models: Short Rate, HJM & LIBOR

!!! info "Source"
    **Mathematical Finance: Theory, Modeling, Implementation** by Christian Fries, Wiley, 2007.
    These notes are used for educational purposes.

## Interest Rate Theory and Models

CHAPTER 16
Pricing Path Dependent Options in a
Backward Algorithm
A backward algorithm - e.g. as given by a model implemented as a lattice - allows the calcula-
tion of the conditional expectation
V(Ti−1) = N(Ti−1) · EQN  V(Ti)
N(Ti) | FTi−1
!
,
and thus defines induction steps Ti →Ti−1 backward in time. Path-dependent quantities cannot
be considered directly. One way of allowing for path-dependent quantities in a backward
algorithm is to eliminate the path-dependency by extending the state space.
16.1. State Space Extension
Let V denote a product whose time Ti value depends on a quantity Ci given by an update rule
Ci = f(Ti,Ci−1, Xi),
C0 = constant,
(16.1)
were Xi is a random variable that is a function of the time Ti values of the model primitives,
i.e. non-path dependent. Thus Xi and hence Ci are FTi measurable. Equation (16.1) constitutes
the path-dependency of Ci; it may not be written as a function of the time Ti values of the
model primitives. It depends on the past since it depends on the previous value Ci−1.
To remove the path-depency in V we add Ci as an additional state. We consider the time Ti
value of V as a function of Ci
V(Ti) = V(Ti,Ci),
i = 0, 1, . . . , n.
Then backward algorithm is:
• Given V(Ti,Ci).
• Apply the update rule to define
˜V(Ti,Ci−1, Xi) := V(Ti, f(Ci−1, Xi))
(16.2)
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
209
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

CHAPTER 16. PRICING PATH DEPENDENT OPTIONS IN A BACKWARD ALGORITHM
• Define
V(Ti−1,Ci−1) := N(Ti−1) · EQN  ˜V(Ti,Ci−1, Xi)
N(Ti)
| FTi−1
!
.
(16.3)
Note that conditional to FTi−1 the state Ci−1 is a constant.
Interpretation (State Space Extension):
The method is called state space
extension because the discrete stochastic process Ti 7→C(Ti) := Ci can be inter-
preted as an additional state of the model and (16.1) defines the evolution of this
process. Seen over this extended space the product is non-path dependent.
◁|
16.2. Implementation
In order to implement the state space extension we discretize the additional state random vari-
ables Ci into ki state values
Ci ∈{ci,1, . . . , ci,ki}.
For the implementation of the update rule (16.2) an interpolation has to be used, e.g. a linear
interpolation
˜V(Ti, ci−1, j, Xi) ≈
f(ci−1, j, Xi) −ci,l j
ci,l j+1 −ci,l j
V(Ti, ci,l j+1) +
ci,l j+1 −f(ci−1,j, Xi+1)
ci,l j+1 −ci,l j
V(Ti, ci,l j),
where l j is such that ci,l j ≤f(ci−1,j, Xi) < ci,l j+1.
Then the conditional expectation (16.3) is calculated for each state realization ci−1, j giving
V(Ti−1, ci−1,1), . . . , V(Ti−1, ci−1,ki).
Remark 209:
For some products the value V(Ti, c) is linear in c. In such cases two states
are sufficient and the approximation of the update rule by the linear interpolation is exact.
Examples are zero structures, where the additional state is the accrued notional; the value of
the future cashflow is linear in the notional.
16.3. Examples
We illustrate the method of state space extension for the valuation of a Snowball / Memory
(Definition 164) and for the evaluation of a Flexi-Cap (Definition 169).
16.3.1. Evaluation of a Snowball in a Backward Algorithm
A Snowball / Memory pays a coupon Ci in Ti+1 which depends on the previous coupon. The
coupon Ci is given by an update rule
Ci = f(Ti,Ci−1, Xi)
with an FTi-measurable Xi (the index), i.e. Ci is path-dependent.
We add the value of the coupon Ci as an additional state and write the product value as a
function of this state.
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
210
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

16.3. EXAMPLES
The backward induction from 16.1 gives the product value V(T0,C0) as a function of the
initial (or past) coupon C0, which is known.
Remark 210 (In Arrears Fixing):
Note that we assumed that the index Xi is a function
of the time Ti values of the model primitives and thus FTi-measurable. If the index Xi−1 is a
function of the time Ti values of the model primitives, i.e. fixed in arrears, then the additional
state variable is the value of the previous coupon.
16.3.2. Evaluation of a Flexi Cap in a Backward Algorithm
An Auto Cap pays at time Ti+1 the amount
Xi := N · max (Li(Ti) −Ki , 0) · (Ti+1 −Ti)
·
( 1
if |{ j : j < i and Lj(T j) −K j > 0}| < nmaxEx
0
else,
where Li(t) := L(Ti, Ti+1; t) denotes the forward rate for the period [Ti, Ti+1] seen in t ≤Ti.
As a function of the processes Li the payoffXi is path-dependent since the payofffunction is
not given by the random variables Lk(Ti) alone, but also by the past realizations of the processes
Lk (entering though Lj(T j), j < i).
We extend the model by the stochastic process
η(t) : Ω→{0, . . . , n −1},
ω 7→
{Lj(T j) −K > 0 | T j ≤t, j = 1, . . . , n −1}
.
Given Li, η the payoffs Xi are a function of the realizations Li(Ti), η(Ti):
Xi := N · max (Li(Ti) −Ki , 0) · (Ti+1 −Ti) ·
( 1
if η(T j) < nmaxEx
0
else.
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
211
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

CHAPTER 16. PRICING PATH DEPENDENT OPTIONS IN A BACKWARD ALGORITHM
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
212
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

CHAPTER 17
Sensitivities (Partial Derivatives) of
Monte-Carlo Prices
17.1. Introduction
The technique of risk-neutral pricing, i.e. the change towards the martingale measure, allows
us to calculate the cost of a (self-financing) replication portfolio, to be expressed as an expecta-
tion. Determination of the replication portfolio itself is not necessary. However, once a pricing
formula or pricing algorithm (e.g. a Monte-Carlo simulation) has been derived, the replication
portfolio can be given in terms of the partial derivatives of the price with respect to current
model parameters (like the initial values of the underlyings).1 The partial derivatives of the
price with respect to the model parameters are also called sensitivities or Greeks. They are
important to assess the risk of a financial product, see also Chapter 7.
For complex products, like Bermudan options, an analytic pricing formula is usually not
available. The pricing has to be done numerically. Under a high-dimensional model, like the
LIBOR market model, the numerical method of choice is usually a Monte-Carlo simulation.
Given that, we will investigate the numerical calculation of sensitivities (partial derivatives) of
Monte-Carlo prices.
The simplest way of calculating a derivative is by applying finite differences. Unfortunately,
this can lead to a Monte-Carlo algorithm giving unstable or inaccurate results.
17.2. Problem Description
Let us consider a pricing algorithm that uses Monte-Carlo simulation to calculate a price of a
financial product as the expectation of the num´eraire-relative value under an equivalent mar-
tingale measure Q
V(t0) = N(t0) · EQ
 V(T)
N(T)
Ft0
!
.
We are interested in the calculation of a partial derivative of V(t0) with respect to some model
parameter, e.g. the initial values of the underlying (→delta), the volatility (→vega), etc.
1 Note that all market parameters enter into model parameters via the calibration of the model.
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
213
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

CHAPTER 17. SENSITIVITIES (PARTIAL DERIVATIVES) OF MONTE-CARLO PRICES
Since we treat this problem as a general numerical problem, not necessarily related to deriva-
tive pricing, we do not adopt a specific model but use a notation that is slightly more general.
To fix notation, let us restate Monte-Carlo pricing first:
17.2.1. Pricing using Monte-Carlo Simulation
Assume that our model is given as a stochastic process X, for example an Itˆo process
dX = µdt + σ · dW(t)
modeling our model primitives like functions of the underlyings (e.g. financial products
(stocks) or rates (forward rates, swap rates, fx rates)). For example, for the Black-Scholes
model we would have X = (log(S ), log(B)). Let X∗(ti) denote an approximation of X(ti) gener-
ated by some (time-)discretization scheme, e.g. an Euler scheme
X∗(ti+1) = X∗(ti) + µ(ti)∆ti + σ(ti) · ∆W(ti)
or one of the more advanced schemes2. We assume that our financial product depends only on
realizations of X at a finite number of time points, i.e. we assume that the risk-neutral pricing of
the financial product may be expressed as the expectation (with respect to the pricing measure)
of a function f of some realizations Y := (X(t0), X(t1), . . . , X(tm)). This is true for many
products (e.g. Bermudan options). If these are approximated through the realizations of the
numerical scheme we have:
E(f(Y)|Ft0) ≈E(f(Y∗)|Ft0) = E(f((X∗(t0), X∗(t1), . . . , X∗(tm)))|Ft0).
Here f denotes the num´eraire-relative payofffunction.
The Monte-Carlo pricing consists of the averaging over some (often equidistributed) sample
paths ωi, i = 1, . . . , n
E(f(Y∗)|Ft0) ≈ˆE(f(Y∗)|Ft0) := 1
n
n
X
i=1
f(Y∗(ωi)).
To summarize: we have two approximation steps involved: The first one approximates the
time-continuous process by a time-discrete process. The second one approximates the expec-
tation by a Monte-Carlo simulation of n sample paths. This is the minimum requirement to
have the pricing implemented as a Monte-Carlo simulation.
17.2.2. Sensitivities from Monte-Carlo Pricing
Assume that θ denotes some model parameter3 or a parametrization of a generic market data
movement and let Yθ denote the model realizations dependent on that parameter. Let us further
assume that φYθ denotes the probability density of Yθ. Then the analytic calculation of the
sensitivity is given by
∂
∂θE(f(Yθ)|Ft0) = ∂
∂θ
Z
Rm f(y)φYθ(y)dy.
2 For alternative schemes see e.g. [66, 21]
3 So for delta θ is an initial value X(0), for vega θ denotes a volatility, etc.
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
214
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

17.2. PROBLEM DESCRIPTION
While the payofff may be discontinuous, the density in general is a smooth function of θ. in
which case the expectation E(f(Yθ)|Ft0) (the price) is a smooth function of θ, too. The price
inherits the smoothness of φYθ.
The calculation of sensitivities using finite differences on a Monte-Carlo based pricing algo-
rithm is known to exhibit instabilities, if the payofffunction is not smooth enough, e.g. if the
payoffexhibits discontinuities as for a digital option. The difficulties arise when we consider
the Monte-Carlo approximation. It inherits the regularity of the payofff, not that of the density
φ:
ˆE(f(Yθ)|Ft0) = 1
n
n
X
i=1
f(Yθ(ωi)).
So while E(f(Yθ)|Ft0) may be smooth in θ, the Monte-Carlo approximation ˆE( f(Yθ)|Ft0) may
have discontinuities. In this case a finite difference approximation of the derivative applied to
the Monte-Carlo pricing will perform poorly.
17.2.3. Example: The Linear and the Discontinuous Payout
The challenge in calculating Monte-Carlo sensitivities becomes obvious if we consider two
very simple examples:
17.2.3.1. Linear Payout
First consider a linear payout, say
f(X(T)) = a · X(T) + b.
The (discounted) payout depends only on the time T realization of X (as one would have for
a European option). Let Yθ(ω) := X(T, ω, θ), where θ denotes some model parameter. The
partial derivative of the Monte-Carlo value of the payout with respect to θ is
∂
∂θ
ˆE(f(Yθ)|Ft0) = 1
n
n
X
i=1
∂
∂θ f(Yθ(ωi)) = 1
n
n
X
i=1
a · ∂
∂θYθ(ωi)
Obviously the accuracy of the Monte-Carlo approximation depends on the variance of ∂Yθ
∂θ only.
When
∂
∂θYθ(ωi) does not depend on ωi, then the Monte-Carlo approximation gives the exact
value of the partial derivative, even if we use only a single path.
17.2.3.2. Discontinuous Payout
Next, consider a discontinuous payout, say
f(X(T)) =

1
if X(T) > K
0
else.
Analytically we know from Yθ+h = Yθ + ∂Yθ
∂θ · h + O(h2) and
EQ(f(Yθ+h) | Ft0) = Q({Yθ > K −∂Yθ
∂θ · h −O(h2)}) =
Z ∞
K−∂Yθ
∂θ ·h−O(h2)
φYθ(y)dy
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
215
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

CHAPTER 17. SENSITIVITIES (PARTIAL DERIVATIVES) OF MONTE-CARLO PRICES
that
lim
h→0
1
2h(EQ(f(Yθ+h) | Ft0) −EQ(f(Yθ−h) | Ft0)) = φYθ(K) · ∂Yθ
∂θ .
However, the partial derivative of the Monte-Carlo value of the payout is
∂
∂θ
ˆE( f(Yθ)|Ft0) = 1
n
n
X
i=1
∂
∂θ f(Yθ(ωi)) = 0 assuming that Yθ(ωi) , K for all i.
Thus, here, the partial derivative of the Monte-Carlo value is always wrong.
17.2.4. Example: Trigger Products
The two simple examples above suggest that a finite difference approximation of a Monte-
Carlo price works well, if the payout is smooth, but fails if the payout exhibits discontinuities.
The problem becomes a bit more subtle if we consider products where the discontinuous be-
haviour is just one part of the payout which, in addition, may also be of more complex nature.
Consider for example the auto cap. For given times T1, . . . , Tn the auto cap pays at each pay-
ment date Ti+1 the payout of a caplet max (L(Ti, Ti+1; Ti) −Ki , 0)·(Ti+1 −Ti), but does so only
if the number of non-zero payments up to Ti is less than some nmaxEx. This latter condition rep-
resents a trigger which makes the otherwise continuous payoffdiscontinuous, see Figure 17.1.
17.3. Generic Sensitivities: Bumping the Model
The finite difference approximation calculates the sensitivity by
∂
∂θE(f(Yθ)|Ft0) ≈E(f(Yθ+h)|Ft0) −E(f(Yθ−h)|Ft0)
2h
.
This brute-force finite difference calculation of sensitivities is sometimes referred to as bump-
ing the model. Bumping the model has a charming advantage: If you keep your model and
your pricing code separated (a design pattern one should always consider) then you may im-
plement a generic code for generating sensitivities by feeding the pricing code with differently
bumped models. In other words:
Once the pricing code is written, all sensitivities are available.
(17.1)
It seems as if you get sensitivities almost for free (i.e. without any effort in modeling and
implementation) and the only price you pay is a doubling of calculation time compared to
pricing. However, it is known that applying such a finite difference approximation to a Monte-
Carlo implementation will often result in extremely large Monte-Carlo errors. Especially if the
payout function of the derivative is discontinuous, this Monte-Carlo error tends to infinity as h
tends to zero. And discontinuous payout is present whenever a trigger feature is present.
Sensitivities in Monte-Carlo are known as a challenge. Numerous methods have been pro-
posed for calculating sensitivities in Monte-Carlo, among them the likelihood ratio [55] and
the application of Malliavin calculus, which has attracted increased attention recently, [63].
These methods improve the robustness of sensitivities, but require more information.
It appears as if the measures you have to take to improve Monte-Carlo sensitivities will
lose the advantage (17.1) of bumping the model. Later, we will present a method (which is
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
216
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

17.3. GENERIC SENSITIVITIES: BUMPING THE MODEL
T1
T2
T0
T3
(a)
T1
T2
T0
T3
(c)
T1
T2
T0
T3
(b)
Figure 17.1.: The payoffof an auto cap paying a maximum of two out of three caplets, considered under
a parallel shift of the interest rate curve (black line). The strike rate is depicted by a blue dot, a positive
payout is marked in green: In scenarios a) and b) the first caplet does not lead to a positive payout while
the second and third caplet do generate a positive payout. The shift of the interest rate curve from a) to
b) changes the payout continuously. In scenario c) the first caplet leads to a positive payout. Since the
auto cap is limited to two positive payouts the payout of the third caplet is lost as soon as the first caplet
pays a positive amount. Thus, from scenario b) to c) the payout of the auto cap changes discontinuously.
Jump due to change
in exercise strategy
Sensitivity of the
underlying caplets
Figure 17.2.: The value of an auto cap as a function of the shift size of a parallel shift of the interest
rate curve. Using only a small number of paths, a small shift does not lead to a change of the exercise
strategy. The price change is driven by the sensitivity of the underlying caplets. Thus, for small shifts one
might be tempted to call the sensitivity stable. For a larger shift the exercise strategy changes on some
paths, leading to a jump in payoff.
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
217
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

CHAPTER 17. SENSITIVITIES (PARTIAL DERIVATIVES) OF MONTE-CARLO PRICES
also an implementation design pattern) that makes it possible to calculate sensitivities through
bumping the model while providing the accuracy and robustness achieved by the likelihood
ratio or Malliavin calculus approach. The method is essentially a likelihood ratio reconsidered
on the level of the numerical scheme.
There are basically two different methods for calculating sensitivities in Monte-Carlo:
• the pathwise method, which differentiates the payout on every simulation path, see 17.5
• the likelihood ratio method, which differentiates the probability density, see 17.6.
Numerically, these two methods may be realized as
• (traditional) finite differences, see 17.4
• finite differences applied to a proxy simulation scheme.
However, a proxy simulation scheme is a much more powerful design, see Chapter 18. It is
also possible to mix the two approaches by considering a partial proxy simulation scheme, see
Section 18.4.
In the following we will present the different methods for calculating sensitivities in Monte-
Carlo simulations. Each section starts with a short description of the approximating formula
and gives the method requirements and properties as bullet points. We assume that a Monte-
Carlo pricing algorithm has been implemented and we mention only requirements additional
to the pricing.
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
218
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

17.4. SENSITIVITIES BY FINITE DIFFERENCES
17.4. Sensitivities by Finite Differences
The finite difference approximation is given by
∂
∂θEQ(f(Yθ) | Ft0) ≈
1
2h
 EQ(f(Yθ+h) | Ft0) −EQ(f(Yθ−h) | Ft0)
≈
1
2h
 ˆEQ(f(Yθ+h) | Ft0) −ˆEQ(f(Yθ−h) | Ft0)
= 1
n
n
X
i=1
1
2h
  f(Yθ+h(ωi) −f(Yθ−h(ωi)
Requirements
• No additional information from the model sde X
• No additional information from the simulation scheme X∗(ti+1)
• No additional information from the payout f
• No additional information on the nature of θ (⇒generic sensitivities)
Properties
• Biased derivative for large h due to finite difference of order h
• Extremely large variance for discontinuous payouts and small h (order h−1)
The most important feature of finite differences is their genericity. Once the pricing code
has been written, all kinds of sensitivities may be calculated.
For smooth payouts, the finite difference approximation converges to the derivative for
h →0. Thus, if the payout is smooth, small shift sizes h are favourable. Using large h the
approximation of the derivative is biased.
For discontinuous payouts, as h →0 the finite difference of the Monte-Carlo price does
not converge to the derivative of the Monte-Carlo price. The reason is that for discontinuous
payouts the Monte-Carlo approximation (n →∞) and the approximation of the derivative
(h →0) are not interchangeable.
For discontinuous payouts finite differences with a fixed, small shift size h perform poorly.
The contribution of a discontinuity to the sensitivity may be calculated analytically. It is the
jump size multiplied by the probability density at the discontinuity. Finite differences resolve
this contribution only through those sample paths which fall into a neighbourhood around the
discontinuity, having the width of the shift size. Thus, if the shift size is small, the discontinuity
is resolved by a few points, ultimately resulting in a large Monte-Carlo error. For discontin-
uous payouts large shift sizes are preferable. However, if the shift size is large, the derivative
becomes biased by second order effects (if present).
Since finite difference does not require anything more than a given pricing algorithm, we
are tempted to apply it to any product for which a Monte-Carlo pricing may be calculated. If
the product exhibits discontinuities in the payout, the finite difference approximation tends to
be unreliable, and a careful analysis of the Monte-Carlo error for a given shift size h has to be
performed.
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
219
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

CHAPTER 17. SENSITIVITIES (PARTIAL DERIVATIVES) OF MONTE-CARLO PRICES
17.4.1. Example: Finite Differences applied to Smooth and
Discontinuous Payout
Let us consider a finite difference approximation of the partial derivative for the case of the
linear payout f(X(T)) = a · X(T) + b from Section 17.2.3.1. We have
∂
∂θEQ(f(Yθ) | Ft0) ≈
1
2h
 EQ(f(Yθ+h) | Ft0) −EQ(f(Yθ−h) | Ft0)
≈
1
2h
 ˆEQ(f(Yθ+h) | Ft0) −ˆEQ(f(Yθ−h) | Ft0)
= 1
n
n
X
i=1
1
2h
 f(Yθ+h(ωi) −f(Yθ−h(ωi)
= 1
n
n
X
i=1
a · 1
2h(Yθ+h(ωi) −Yθ−h(ωi)),
which is a good approximation, if
∂
∂θYθ(ωi)) ≈
1
2h(Yθ+h(ωi) −Yθ−h(ωi)). This is usually the
case and throughout this chapter we assume that the model is such, that its realizations Yθ(ωi)
are smooth in the model parameters θ.
For the discontinuous payout f(X(T)) = 1 if X(T) > K and f(X(T)) = 0 else, considered in
Section 17.2.3.2, we have
∂
∂θEQ(f(Yθ) | Ft0) ≈
1
2h
 EQ(f(Yθ+h) | Ft0) −EQ(f(Yθ−h) | Ft0)
≈
1
2h
 ˆEQ(f(Yθ+h) | Ft0) −ˆEQ(f(Yθ−h) | Ft0)
= 1
n
n
X
i=1
1
2h
  f(Yθ+h(ωi)) −f(Yθ−h(ωi))
= 1
n
n
X
i=1
1
2h

1
if Yθ−h(ωi) < K < Yθ+h(ωi)
−1
if Yθ−h(ωi) > K > Yθ+h(ωi)
0
else.
This is a valid approximation, but it has a large Monte-Carlo variance, since the true value is
sampled by 0 and 1
2h occurring in the appropriate frequency. If h gets smaller, then we have to
represent true value by a sampling of 0 and a very large constant.
Simplified Example:
Assume for simplicity that Yθ is linear in θ, i.e. we have Yθ+h =
Yθ + ∂Yθ
∂θ · h and thus
f(Yθ+h(ωi)) −f(Yθ−h(ωi))
2h
=

1
2h
if Yθ−h(ωi) < K < Yθ+h(ωi)
−1
2h
if Yθ−h(ωi) > K > Yθ+h(ωi)
0
else.

=

sign ∂Yθ
∂θ
2h
if Yθ(ωi) ∈[K −ϵ, K + ϵ]
0
else.
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
220
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

17.5. SENSITIVITIES BY PATHWISE DIFFERENTIATION
where ϵ :=
 ∂Yθ
∂θ
 · h. For the probability we have
q := Q(Yθ ∈[K −ϵ, K + ϵ]) ≈φYθ(K) · 2ϵ = φYθ(K) ·

∂Yθ
∂θ
 · 2h.
In other words: We are sampling the partial derivative of the expectation by a binomial exper-
iment:
sign ∂Yθ
∂θ
2h
with probability q
and
0
with probability 1 −q.
The expectation of this binomial experiment is
sign ∂Yθ
∂θ
2h
· q + 0 · (1 −q) ≈φYθ(K) · ∂Yθ
∂θ ,
which is the desired analytic value for the finite difference approximation as h →0. The
variance of the binomial experiment is
 1
2h
!2
· q · (1 −q) ≈φYθ(K) · ∂Yθ
∂θ · (1 −q) · 1
2h = O
 1
2h
!
,
which explodes as h →0.
17.5. Sensitivities by Pathwise Differentiation
The pathwise differentiation method is given by
∂
∂θEQ(f(Y(θ)) | Ft0) =
∂
∂θ
Z
Ω
f(Y(ω, θ)) dQ(ω) =
Z
Ω
∂
∂θ f(Y(ω, θ)) dQ(ω)
=
Z
Ω
f ′(Y(ω, θ)) · ∂Y(ω, θ)
∂θ
dQ(ω) = EQ(f ′(Y(θ)) · ∂Y(θ)
∂θ
| Ft0)
f smooth
≈
ˆEQ(f ′(Y(θ)) · ∂Y(θ)
∂θ
| Ft0) = 1
n
n
X
i=1
f ′(Y(ωi, θ)) · ∂Y(ωi, θ)
∂θ
Requirements
• Additional information on the model sde X
• No additional information on the simulation scheme X(ti+1)
• Additional information on the payout f (derivative of f must be known)
• Additional information on the nature of θ (⇒no generic sensitivities)
Properties
• Unbiased derivative
• Discontinuous payouts may be dealt with (interpret f ′ as distribution, see below)
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
221
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

CHAPTER 17. SENSITIVITIES (PARTIAL DERIVATIVES) OF MONTE-CARLO PRICES
The pathwise method requires the knowledge of the derivative of the payout f ′ and the
derivative of the process realizations with respect to the parameter θ, i.e. ∂Y(ωi,θ)
∂θ
. It is thus
only applicable for a restricted class of models and model parameters, where ∂Y(ωi,θ)
∂θ
may be
calculated analytically.
It seems as if a discontinuity in the payout cannot be dealt with, since we require f ′ to exist.
However, the impact of a discontinuity can be calculated analytically, see 17.5.2.
It is a major disadvantage of the method that it requires special knowledge of the payout
function and of model realizations.
17.5.1. Example: Delta of a European Option under a
Black-Scholes Model
We consider a Black-Scholes Model
S (t) = S (0) · exp(¯rt −1
2 ¯σ2t + ¯σW(t)),
S (0) = S 0
B(t) = B(0) · exp(¯rt)
(17.2)
In this case we have, e.g.
∂
∂S 0
S (T) = S (T)
S 0
.
Using the notation above, our model primitive is X = (S, B). We assume that the payout of
our derivative depends on Y = X(T) = (S (T), B(T)) only, i.e. we are considering a European
option. Then we have
∂
∂S 0
EQ(f(S (T)) | Ft0) = EQ(f ′(S (T)) · S (T)
S 0
| Ft0)
≈ˆEQ(f ′(S (T)) · S (T)
S 0
| Ft0)
= 1
n
n
X
i=1
f ′(S (T, ωi)) · S (T, ωi)
S 0
17.5.2. Pathwise Differentiation for Discontinuous Payouts
In case that the payout f exhibits discontinuities the pathwise method may be applied, provided
that f allows for a decomposition
f = g +
X
i
αi1({Y(θ) > yi}),
with g being smooth. In this case we have
∂
∂θEQ(f(Y(θ)) | FT0) =
∂
∂θ
Z
Ω
f(Y(ω, θ)) dQ(ω) =
Z
Ω
∂
∂θ f(Y(ω, θ)) dQ(ω)
=
Z
Ω
f ′(Y(ω, θ)) · ∂Y(ω, θ)
∂θ
dQ(ω) = EQ(f ′(Y(θ)) · ∂Y(θ)
∂θ
| FT0)
g smooth
≈
ˆEQ(g′(Y(θ)) · ∂Y(θ)
∂θ
| FT0) +
X
i
αi · φ(yi) · ∂Y(θ)
∂θ |Y(θ)=yi
See [79, 88] for examples of how to use pathwise differentiation with discontinuous payouts
(there in the context of nth to default swaps, CDOs).
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
222
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

17.6. SENSITIVITIES BY LIKELIHOOD RATIO WEIGHTING
17.6. Sensitivities by Likelihood Ratio Weighting
The pathwise method differentiates the path value Y(θ) of the underlying process realizations
Y. Provided there is a probability density φY(θ) of Y(θ) we may write the expectation as a
convolution with the density. The likelihood ratio weighting [53, 55, 16] is then given by
∂
∂θEQ(f(Y(θ)) | Ft0) =
∂
∂θ
Z
Ω
f(Y(ω, θ)) dQ(ω) =
∂
∂θ
Z
Rm f(y) · φY(θ)(y) dy
=
Z
Rm f(y) ·
∂
∂θφY(θ)(y)
φY(θ)(y) · φY(θ)(y) dy = EQ(f(Y) · w(θ) | Ft0)
≈ˆEQ(f(Y) · w(θ) | Ft0) = 1
n
n
X
i=1
f(Y(ωi)) · w(θ, ωi),
where w(θ) :=
∂
∂θ φY(θ)(Y(θ))
φY(θ)(Y(θ)) .
Requirements
• Additional information on the model sde X (→φY(θ))
• No additional information on the simulation scheme X(ti+1)
• No additional information on the payout f
• Additional information on the nature of θ (⇒no generic sensitivities)
Properties
• Unbiased derivative
• Discontinuous payouts may be dealt with.
The Likelihood Ratio method requires no additional information on the payout function.
This is an advantage compared to the pathwise differentiation. However, it requires that the
density of the model sde’s realizations X(t) is known and furthermore, that its derivative is
known analytically with respect to the parameter θ. This is rarely the case and thus a major
drawback of the method.
The likelihood ratio method does not require the payout to be smooth. The method works
very well for calculating the impact of a discontinuity in the payout. However, the method has
its problems with smooth payouts: the Monte-Carlo error of the approximation using Likeli-
hood Ratio is larger than the Monte-Carlo error of the finite-difference approximation. We give
a simple example of this effect next.
17.6.1. Example: Delta of a European Option under a
Black-Scholes Model using Pathwise Derivative
Let us look again at a European Option using the Black-Schloes model (17.2). Since B is
deterministic we need to consider the probability density of S . Since log(S (T)) is normally
distributed, see Chapter 4, we have for the density of S (T)
φS (T)(s) =
φstd.norm.
 1
¯σ
√
T (log(s) + ¯r(T) −1
2 ¯σ(T)2 −log(S 0))
s
,
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
223
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

CHAPTER 17. SENSITIVITIES (PARTIAL DERIVATIVES) OF MONTE-CARLO PRICES
where φstd.norm.(x) =
1
√
2π exp(−x2/2) is the density of the standard normal distribution.
Thus, the delta of a European option with (num´eraire-rebased) payout f(S (T), B(T)), calcu-
lated by the likelihood ratio method, is given by
EQ
f(S (T), B(T)) ·
∂
∂S 0 φS (T)(S (T))
φS (T)(S (T))
 F0
.
17.6.2. Example: Variance Increase of the Sensitivity when using
Likelihood Ratio Method for Smooth Payouts
For some smooth payouts, the Likelihood Ratio method may perform less accurately than the
pathwise method 17.5 or its finite difference approximation 17.4. A simple example illustrates
this effect: Consider constant payout f(S (T), B(T)) = b. Then, the likelihood ratio method
gives the delta of this option as
EQ
f(S (T), B(T)) ·
∂
∂S 0 φS (T)(S (T))
φS (T)(S (T))
 F0
=
Z
R
f(s, B(T)) ·
∂
∂S 0
φS (T)(s) ds
f=b=const.
=
b ·
Z
R
∂
∂S 0
φS (T)(s) ds
and indeed (using substituation y = log(s), dy = 1
sds) we see that the delta is zero:
=
Z
R
∂
∂S 0
φ()dy = 0
The Monte-Carlo approximation is
EQ
f(S (T), B(T)) ·
∂
∂S 0 φS (T)(S (T))
φS (T)(S (T))
 F0

≈1
n
n
X
i=1
f(S (T, ωi), B(T)) ·
∂
∂S 0 φ(S (T, ωi))
φ(S (T, ωi))
= 1
n
n
X
i=1
b ·
∂
∂S 0 φ(S (T, ωi))
φ(S (T, ωi)) ,
which is in general non zero. It is an approximation of zero, having some variance.
On the other hand, note that the pathwise method and even a finite difference approximation
thereof would give a delta of zero with zero Monte-Carlo variance.
17.7. Sensitivities by Malliavin Weighting
The Malliavin weighting is similar to the Likelihood Ratio method: the sensitivity is expressed
as the expectation of a weighted payout function.
∂
∂θEQ(f(Y(θ)) | Ft0) = EQ(f(Y(θ)) · w(θ) | Ft0)
≈ˆEQ(f(Y(θ)) · w(θ) | Ft0) = 1
n
n
X
i=1
f(Y(θ, ωi)) · w(θ, ωi)
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
224
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

17.8. PROXY SIMULATION SCHEME
Requirements
• Additional information on the model sde X (→w)
• No additional information on the simulation scheme X(ti+1)
• No additional information on the payout f
• Additional information on the nature of θ (⇒no generic sensitivities)
Properties
• Unbiased derivative
• Discontinuous payouts may be dealt with.
Benhamou [47] showed that the Likelihood Ratio corresponds to the Malliavin weights
with minimal variance and may be expressed as a conditional expectation of all corresponding
Malliavin weights (we thus view the Likelihood Ratio as an example of the Malliavin weight-
ing method).
However, here the weights are derived directly through Malliavin calculus which makes this
method more general and applicable even if the density is not known. The derivation of the
Malliavin weights requires in-depth knowledge of the underlying continuous process X and it
is heavily dependent on the nature of θ.
17.8. Proxy Simulation Scheme
The proxy simulation scheme defines a design of a Monte-Carlo pricing engine that has the
remarkable properties that the application of finite differences to the pricing will result in Like-
lihood Ratio weighted sensitivities without actually the need to know the density φ analytically.
Thus it combines the robustness of Likelihood Ratio or Malliavin weighting with the genericity
of finite differences.
Since the proxy simulation scheme method is not solely devoted to the calculation of sen-
sitivities it will be discussed in an own chapter in 18. For a detailed discussion of the proxy
simulation scheme see also [65, 66]. Here, we will summarize the key properties.
The Monte-Carlo sensitivity under a proxy simulation scheme is given by
∂
∂θEQ(f(Y∗(θ)) | Ft0) ≈
1
2h
 EQ(f(Y∗(θ + h)) | Ft0) −EQ(f(Y∗(θ −h)) | Ft0)
=
∂
∂θ
Z
Rm f(y) · 1
2h(φY∗(θ+h)(y) −φY∗(θ−h)(y)) dy
=
Z
Rm f(y) ·
1
2h(φY∗(θ+h)(y) −φY∗(θ−h)(y))
φY◦(y)
· φY◦(y) dy
≈1
n
n
X
i=1
f(Y◦(ωi)) · 1
2h(w(θ + h, ωi) −w(θ −h, ωi))
Requirements
• No additional information on the model sde X
• Additional information on the simulation scheme X∗(ti+1), X◦(ti+1)
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
225
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

CHAPTER 17. SENSITIVITIES (PARTIAL DERIVATIVES) OF MONTE-CARLO PRICES
• No additional information on the payout f
• No additional information on the nature of θ (⇒generic sensitivities)
Properties
• Biased derivative (but small shift h possible!)
• Discontinuous payouts may be dealt with.
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
226
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

CHAPTER 18
Proxy Simulation Schemes for
Monte-Carlo Sensitivities and
Importance Sampling
In this chapter we describe the proxy simulation scheme technique as it is given in [66] and
[65].
18.1. Full Proxy Simulation Scheme
We take the notation of the previous chapter, see 17.2 and 17.3 and consider two time-discrete
schemes for the stochastic process X:
X∗
ti 7→X∗(ti)
i = 0, 1, 2, . . .
time discretization scheme of X
→target scheme
X◦
ti 7→X◦(ti)
i = 0, 1, 2, . . .
any other time-discrete stochastic process (as-
sumed to be close to X∗)
→proxy scheme
Let φY◦(y) denote the density of Y◦and φY∗(y) the density of Y∗. We require
∀y : φY◦(y) = 0 ⇒φY∗(y) = 0.
(18.1)
Using the additional scheme X◦the pricing of a payout function f is now performed
in the following way: Let Y = (X(t1), . . . , X(tm)),
Y∗= (X∗(t1), . . . , X∗(tm)),
Y◦=
(X◦(t1), . . . , X◦(tm)). We have EQ(f(Y(θ)) | Ft0) ≈EQ(f(Y∗(θ)) | Ft0) and furthermore
EQ(f(Y∗(θ)) | Ft0) =
Z
Ω
f(Y∗(ω, θ)) dQ(ω) =
Z
Rm f(y) · φY∗(θ)(y) dy
=
Z
Rm f(y) · φY∗(θ)(y)
φY◦(y) · φY◦(y) dy = EQ(f(Y◦) · w(θ) | Ft0,
where w(θ) = φY∗(θ)(y)
φY◦(y) .
For the Monte-Carlo approximation this implies that the sample paths are generated from
the scheme X◦while the probability densities are corrected towards the target scheme X∗.
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
227
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

CHAPTER 18. PROXY SIMULATION SCHEMES FOR MONTE-CARLO SENSITIVITIES AND IMPORTANCE SAMPLING
Notes
• For X◦= X∗we have w(θ) = 1, and in this case the proxy simulation scheme corresponds
to the ordinary Monte-Carlo simulation of X∗.
• The proxy scheme X◦and thus its realization vector Y◦are seen as being independent of
θ. This has important implications on the calculation of sensitivities, see Section 18.2.
• The requirement ∀y : φY◦(y) = 0 ⇒φY∗(y) = 0 corresponds to the non-degeneracy
condition of the diffusion matrix as it appears in the application of the likelihood ratio
and Malliavin weights. However, here this requirement is far less restrictive since we
are free to choose the proxy scheme X◦.
18.1.1. Calculation of Monte-Carlo weights
For the most common numerical schemes the densities φY◦, φY∗and thus the Monte-Carlo
weights may be calculated numerically. Consider for example the schemes
target scheme:
X∗(ti+1) = X∗(ti) + µX∗(ti)∆ti + Σ(ti) · Γ(ti) · ∆U(ti)
proxy scheme:
X◦(ti+1) = X◦(ti) + µX◦(ti)∆ti + Σ◦(ti) · Γ◦(ti) · ∆U(ti)
where Σ denotes an invertible volatility matrix and Γ denotes a projection matrix, the factor
matrix which defines the correlation structure R = ΓΓT.
Assume for simplicity that µX∗(ti) depends on X∗(ti), X∗(ti+1) only (and similar for µX◦(ti))
(this holds for, e.g. Euler Scheme, Predictor Corrector), then we have for the transition proba-
bility densities
φX∗(ti, X∗
i ; ti+1, X∗
i+1) =
1
(2Π∆ti)n/2 exp

−
1
2∆ti
 Λ−1/2FTΣ−1 X∗
i+1 −X∗
i −µX∗(ti)∆ti
2
φX◦(ti, X◦
i ; ti+1, X◦
i+1) =
1
(2Π∆ti)n/2 exp

−
1
2∆ti
 Λ◦−1/2F◦TΣ◦−1 X◦
i+1 −X◦
i −µX◦(ti)∆ti
2
.
And the proxy scheme weights are given by
w(ti+1) |Ftk =
iY
j=k
φX∗(t j, X◦
j; t j+1, X◦
j+1)
φX◦(tj, X◦
j; t j+1, X◦
j+1),
see [66] for details.
Notes
• We used the factor decomposition (PCA) Γ = F ·
√
Λ where Λ = diag(λ1, . . . , λm) are
the non-zero eigenvalues of Γ · ΓT.
• A change of market data / calibration affects only the transition probabilities.
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
228
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

18.2. SENSITIVITIES BY FINITE DIFFERENCES ON A PROXY SIMULATION SCHEME
18.2. Sensitivities by Finite Differences on a Proxy
Simulation Scheme
∂
∂θEQ(f(Y∗(θ)) | Ft0) ≈
1
2h
 EQ(f(Y∗(θ + h)) | Ft0) −EQ(f(Y∗(θ −h)) | Ft0)
=
∂
∂θ
Z
Rm f(y) · 1
2h(φY∗(θ+h)(y) −φY∗(θ−h)(y)) dy
=
Z
Rm f(y) ·
1
2h(φY∗(θ+h)(y) −φY∗(θ−h)(y))
φY◦(y)
· φY◦(y) dy
≈1
n
n
X
i=1
f(Y◦(ωi)) · 1
2h(w(θ + h, ωi) −w(θ −h, ωi))
Requirements
• No additional information on the model sde X
• Additional information on the simulation scheme X∗(ti+1), X◦(ti+1)
• No additional information on the payout f
• No additional information on the nature of θ (⇒generic sensitivities)
Properties
• Biased derivative (but small shift h possible!)
• Discontinuous payouts may be dealt with.
Notes
We noted above that additional information on the simulation scheme is required, that is, the
densities of the two schemes. Note however that we require these densities to setup the pricing
algorithm. For the sensitivity calculation no additional information is needed. Note also that
the required densities are densities of numerical schemes, which can usually be calculated from
known transition probability densities (see Section 18.1.1).
18.2.1. Localization
If the payout function f is smooth then ordinary finite differences perform better than the
weighting techniques. The latter shows an increase in Monte-Carlo variance of the sensitivity.
This effect is not only visible for smooth payouts f, but also for large finite difference shifts.
A solution that has been proposed in [63] is localization. Here the weighting is applied only
to a region where the payoffis discontinuous.
Let g denote the localization function, i.e. a smooth function 0 ≤g ≤1 such that g = 1 at
discontinuities of f. Consider the decomposition
f = (1 −g) · f + g · f.
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
229
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

CHAPTER 18. PROXY SIMULATION SCHEMES FOR MONTE-CARLO SENSITIVITIES AND IMPORTANCE SAMPLING
We define the pricing of the payout f as
E( f(Y∗)|Ft0) = E((1 −g(Y∗)) · f(Y∗)|Ft0) + E(g(Y◦) · f(Y◦) · φY∗
φY◦|Ft0).
In other words: We use a pricing based on a proxy simulation scheme for g · f and a pricing
based on direct simulation for (1 −g) · f.
It should be noted that localization is carried out by a redefinition of the payout. The product
is split into two parts, where one is priced by a direct simulation scheme and the other is priced
by a proxy simulation scheme method. This allows us to implement localization on the product
level, completely independent of the actual simulation properties. In addition, localization does
not reduce the ability to calculate generic sensitivities.
18.2.2. Object-Oriented Design
The proxy scheme simulation method may in part also be viewed as an implementation design.
In Figure 18.1(a) we depict the object-oriented design of a standard Monte-Carlo simulation
where a change in market data results in a change of simulation path. In Figure 18.1(b) we
contrast the proxy scheme simulation method where a change in market data results in a change
of Monte-Carlo weights. In practice, we propose that the model driving the generation of the
proxy schemes paths is calibrated to market data used for pricing while a market data scenario
used for sensitivity calculation, i.e. by bumping the model, only impacts the Monte-Carlo
weights. A method should be offered to reset the proxy simulation’s market data to the target
simulation’s market data.
18.3. Importance Sampling
The key idea of importance sampling is to generate the paths according to their importance
to the application, not according to their probability law, and in doing so, adjust towards their
probability by a suitable Monte-Carlo weight (the change of measure).
Using a proxy simulation scheme, the paths are generated according to the proxy scheme
while a Monte-Carlo weight adjusts their probability towards the target scheme. Actually,
once the proxy simulation scheme framework has been established, the Monte-Carlo weights
are calculated automatically from the two numerical schemes.
Thus, choosing the proxy scheme such that it creates paths according to their importance to
the application is a form of importance sampling. It has the advantage that specifying a suitable
process might come easier than calculating the optimal sampling and the corresponding Monte-
Carlo weights.
18.3.1. Example
Let us look at the pricing of an out-of-the-money option under a lognormal model (like the
Black-Scholes model or the LIBOR market model):
Log Euler Scheme:
d log(X)(t j+1) = log(X)(t j+1) + µ(t)dt + σdW
OTM option:
max(X(T) −K, 0),
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
230
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

18.3. IMPORTANCE SAMPLING
Calibrated Model 
Parameters
Model
Market Data θ+h
InputData
Sensitivity as Finite 
Difference
Market Data θ-h
InputData
Price
Price
Product
∑ f(Y(ωi)) • ⅟n
Equally weighted
Paths of Simulation Scheme
Simulation
(a) Standard Monte-Carlo Simulation
Calibrated Model 
Parameters
Model
Market Data θ+h
InputData
LR like Sensitivity as 
Finite Difference
Market Data θ-h
InputData
Price
Price
Model Parameters
Proxy Model
Product
∑ f(Y(ωi)) • wi
Monte Carlo weights
Paths of Proxy Scheme
Simulation
(b) Proxy Scheme Monte-Carlo Simulation
Figure 18.1.: Object-oriented design of the Monte-Carlo pricing engine: We depict the impact of a
change of different market data scenarios θ + h and θ −h on the pricing code of a standard Monte-Carlo
simulation and a proxy scheme simulation.
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
231
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

CHAPTER 18. PROXY SIMULATION SCHEMES FOR MONTE-CARLO SENSITIVITIES AND IMPORTANCE SAMPLING
where X(0) = X0 and K >> X0. The drift of the model is determined by the specific pricing
measure. However, in our application we would prefer that the mean of X(T) is close to the
option strike K rather than being exp   log X0 +
R T
0 µ(t)dt. To achieve this, simply use a proxy
scheme with artificial drift:
Proxy Scheme:
d log(X)(t j+1) = log(X)(t j+1) + log(K) −log(X0)
T
dt + σidW
Target Scheme:
d log(X)(t j+1) = log(X)(t j+1) + µ(t)dt + σdW
This will bring the paths to the region that is important for the pricing of the option, while
the proxy simulation scheme framework automatically adjusts probabilities accordingly. Fig-
ure 18.2 shows a comparison of distribution of Monte-Carlo prices obtained from direct sim-
ulation compared to the prices obtained from importance adjusted proxy scheme simulation.
Importance Sampling using Proxy Simulation Scheme
Standard Euler Scheme
Proxy Scheme with Importance Adjusted Drift
0,000000
0,000025
0,000050
0,000075
0,000100
0,000125
Prices
0,00
0,05
0,10
0,15
0,20
Frequency
Figure 18.2.: Importance sampling using a drift adjusted proxy scheme. The example was created using
a LIBOR market model to price a caplet with strike K = 0.3, the initial forward rate being X0 = Li(0) =
0.1.
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
232
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

18.4. PARTIAL PROXY SIMULATION SCHEMES
18.4. Partial Proxy Simulation Schemes
The (full) proxy simulation scheme method requires the density of the target scheme realization
to be zero if the density of the proxy scheme is zero, (18.1). In other words, it is required
that the paths simulated under the proxy scheme comprise all paths possible under the target
scheme. If the property is violated, then the Monte-Carlo expectation using the weighted paths
of the proxy scheme will leave out some mass. This limits the application of the full proxy
simulation scheme. For the calculation of sensitivities the limitation means that we cannot
calculate the sensitivity with respect to all possible perturbations.
However, in order to improve the calculation of sensitivities of trigger products it is not
necessary to keep all underlying quantities rigid (as for a full proxy simulation); it is sufficient
to keep the quantity that induces the discontinuity rigid. This gives rise to the notion of a partial
proxy simulation scheme, [65].
Let K0 denote the unperturbed scheme and K∗some perturbation of K0, e.g. a scheme with
different initial data. We will call K0 the reference scheme and K∗the target scheme.
The usual procedure of bump-and-revalue for computing Greeks would simulate paths of
K∗having Monte-Carlo weight 1
n. The proxy simulation schemes would simulate paths of K0
using Monte-Carlo weights 1
n · φ∗
φ0 . Instead, here we consider a third scheme K1, the (partial)
proxy simulation scheme where paths are such that the path-wise values of some (but not all)
components of K1 (or a function thereof) agree with the corresponding pathwise quantities
under K0.
18.4.1. Linear Proxy Constraint
Let Π(ti) denote a projection operator of rank k. Let v(ti) be defined as
v(ti) := (Π · Γ(ti))−1 · (Π · K∗(ti+1) −Π · K0(ti+1)),
(18.2)
where (Π · Γ(ti))−1 is the quasi inverse of Π · Γ(ti), i.e. v is the solution of
∥Π · K0(ti+1) −Π · (K∗(ti+1) −ΠΓ(ti)v(ti))∥L2 →min .
(18.3)
We define the k-dimensional partial proxy scheme K1 as:
K1(t0) := K∗(t0)
K1(ti+1) := K∗(ti+1) −Γ(ti) · v(ti).
(18.4)
The scheme K1 has the following properties:
• It coincides with K0 on the k-dimensional sub-manifold defined by Π, i.e. Π · K1(ti) =
Π · K0(ti).
• It is given through a mean shift v(ti) on the Brownian increment ∆W(ti) of the target
scheme K∗.
Consequently, the Monte-Carlo weight of the partial proxy scheme is given by
w(ti) = φK∗(ti, K1(ti); ti+1, K1(ti+1))
φK1(ti, K1(ti); ti+1, K1(ti+1)).
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
233
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

CHAPTER 18. PROXY SIMULATION SCHEMES FOR MONTE-CARLO SENSITIVITIES AND IMPORTANCE SAMPLING
In the case of a linear proxy constraint, the mean shift v(ti) is Fti measurable.1 Then, using
simple Euler schemes, the transition probabilities are
φK1(ti, K1(ti); ti+1, K1(ti+1)) = φW(ti, W(ti), ti+1, W(ti+1))
φK∗(ti, K1(ti); ti+1, K1(ti+1)) = φW(ti, W(ti), ti+1, W(ti+1) −v(ti)).
(18.5)
From this we can derive w(ti) as a simple analytic formula, see Section 18.4.4.2.
We would like to note that in (18.3) we may replace the projection operator by a general non-
linear function, if necessary. We will discuss this case in Section 18.4.3 and we will consider
this case in our example in Section 18.4.7.
18.4.2. Comparison to Full Proxy Scheme Method
The proxy simulation scheme proposed in [66] corresponds to K1 = K0. Thus, it is a special
case of (18.2), (18.4) if Π is the identity and if
Γ(ti)v(ti) := K∗(ti+1) −K0(ti+1)
(18.6)
has a solution v(ti) (not only in the sense of a closest approximation). If however (18.6) has no
solution, v(ti) from (18.2) still defines a valid mean shift for the scheme K∗. The scheme K1
will be the closest approximation to K0 fulfilling the measure continuity condition with respect
to K∗.
A major advantage of the partial proxy scheme is that the projection Π may be chosen such
that (18.2) has an exact solution with respect to the sub-manifold defined by Π, so K1 and
K0 coincide on a k-dimensional sub-manifold. We will make use of this in our example in
Section 18.4.6.
18.4.3. Non-Linear Proxy Constraint
An obvious (and commonly required) generalization is to replace the linear projection operator
Π by a general, possibly non-linear function f : Rn →Rk and define v(ti) as the solution of
f(ti+1, K0(ti+1)) = f(ti+1, K∗(ti+1) −Γ(ti) · v(ti)).
(18.7)
Thus we have f(ti+1, K0(ti+1)) = f(ti+1, K1(ti+1)). An example of an application of this gen-
eralization is a LIBOR Market Model, where f represents a certain swap rate or function of
swap rates (e.g. a CMS spread). The condition will then ensure that the path values of the swap
rate(s) are the same under K0 and K1.
18.4.3.1. Linearization of the Proxy Constraint
While a constraint like (18.7) will be the general application, its numerical implementation
may be expensive, since one has to solve the non-linear equation on every path in every time-
step. However, if K∗(ti+1) is a small perturbation of K0(ti+1), we may linearize Equation 18.7.
In other words we would set
Π := f ′(K0(ti+1)).
(18.8)
Note that the proxy simulation method is constructed such that a finite difference using small
perturbation will remain stable, i.e. K∗(ti+1) may be chosen to be arbitrarily close to K0(ti+1).
1 We will later consider the general case of non-linear proxy constraints and Fti measurable mean shifts, see Sec-
tion 18.4.3 and 18.4.4.
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
234
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

18.4. PARTIAL PROXY SIMULATION SCHEMES
18.4.3.2. Finite Difference Approximation of the Non-Linear Proxy Constraint
The linearization (18.8) of f may still result in relatively large computational costs, because
the projection operator has to be calculated on every path. Note that we linearize around
K0(ti+1, ω). Thus the quasi-inverse of ΠΓ has to be calculated on every path in every time-step.
If we want to implement a faster calculation of the mean shift v(ti, ωj) we can calculate an
approximate solution of (18.7) by guessing the directional shift ˜v(ti) and finite differences to
determine the shift size:
Assume we knew that the directional shift ˜v(ti) does not lie in Kernf ′Γ. Then for some ϵ > 0
calculate
∆−ϵΓ˜v(ti) f := 1
ϵ (f(ti+1, K∗(ti+1) −ϵ · Γ(ti) · ˜v(ti)) −f(ti+1, K0(ti+1)))
(18.9)
and set
Γ · v(ti) := (∆−ϵ˜v(ti))−1 · ˜v(ti)
(18.10)
in the definition of the partial proxy scheme K1, (18.4).
This solution has the desirable property, that its implementation allows the constraint func-
tion f to be specified exogenously by the user; this constraint function may vary with the
application.
Example:
If K is the log of the forward rates under a LIBOR Market Model and f is a swap
rate, i.e. we would like to keep a swap rate rigid, then we can achieve this by modifying the first
factor. This corresponds to ˜v(ti) = (1, 0, . . . , 0). From (18.9) we can calculate the impact of a
shift of the first factor on the swap rate; from (18.10) we can calculate the required magnitude
of this shift (it is scalar equation with a scalar unknown v1(ti)).
We will consider a constraint like (18.7) next, in our benchmark application, a trigger option
on an index like a CMS swap rate considered under the LIBOR Market Model.
18.4.4. Transition Probability from a Nonlinear Proxy Constraint
18.4.4.1. The Proxy Constraint Revisited
There is subtle but crucial detail in the definition of the mean shift v(ti): It is defined by
comparing K∗(ti+1) to K0(ti+1)
f(ti+1, K0(ti+1)) = f(ti+1, K∗(ti+1) −Γ(ti) · v(ti)),
(18.11)
not by comparing K∗(ti) to K0(ti). Thus, in general, v(ti) is a Fti+1-measurable random variable,
but not Fti+1-measurable.2 If we would define v(ti) through
f(ti+1, K0(ti)) = f(ti+1, K∗(ti) −Γ(ti) · v(ti)),
then it is not guaranteed that
f(ti+1, K0(ti+1)) = f(ti+1, K∗(ti+1) −Γ(ti) · v(ti)),
2 In the following we will say v(ti) is Fti+1-measurable only, if it is Fti+1-measurable but not Fti-measurable.
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
235
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

CHAPTER 18. PROXY SIMULATION SCHEMES FOR MONTE-CARLO SENSITIVITIES AND IMPORTANCE SAMPLING
holds, after the drift and the diffusion from ti to ti+1 has been applied. To account for the drift
we could define v(ti) through
f(ti+1, K0(ti) + µ0(ti)∆ti) = f(ti+1, K∗(ti) + µ∗(ti)∆ti −Γ(ti) · v(ti)),
(18.12)
which makes v(ti) a Fti-measurable random variable, but there is still no guarantee that the
proxy constraint holds after the diffusion has been applied. However, it will be the case for
linear constraints.
From this consideration it becomes obvious that for the linearization of the proxy constraint,
we would have to linearize around K0(ti+1) and not around K0(ti). As a solution of this lin-
earization v(ti) will be Fti+1-measurable only.
If the mean shift v(ti) is defined by (18.11) as a Fti+1-measurable random variable it means -
using Euler schemes - that v(ti) depends non-linearily on the increment ∆W(ti) and the formula
for the corresponding transition probability involves inverting this dependence. Here are two
examples:
18.4.4.2. Transition Probabilities for General Proxy Constraints
If the proxy constraint on time ti+1 is linear, then it may be realized by an Fti measurable
mean-shift v(ti). In this case the calculation of the transition probabilities that form the Monte-
Carlo weight leads to very simple formulas. From (18.5) we find that for an Fti-measurable
mean-shift
w(ti) =
m
Y
k=1
exp
−(xk −vk(ti))2 + x2
k
2∆ti

where xk := ∆Wk(ti).
(18.13)
If the mean shift v(ti) is only Fti+1-measurable, then it is still possible to obtain a simple an-
alytic formula for the transition probability; however, this formula requires the differentiation
of the functional dependence of v(ti) on the increment ∆W(ti).
Consider the general case where the mean shift v(ti) depends on the Brownian increment
∆W(ti), i.e.
v(ti) = v(ti, ∆W(ti)).
Define ˜x = g(x) := x −v(ti, x). Obviously we have
φ(˜x)d˜x
˜x=g(x)
=
φ(g(x))det
 ∂v(ti, x)
∂x
!
dx =
φ(g(x))det
 ∂g(x)
∂x

φ(x)
φ(x)dx.
(18.14)
Here x denotes the (realization of the) Brownian increment ∆W and φ denotes its probability
density. Evaluating functions of ˜x = g(x) corresponds to pricing under the partial proxy scheme
K1; evaluating functions of x corresponds to the pricing under the target scheme K∗. From
(18.14) we can read offthe Monte-Carlo weights for the pricing under the scheme K1 as
w(ti) = det
 
I −∂v(ti, x)
∂x
!
·
m
Y
k=1
exp
−(xk −vk(ti))2 + x2
k
2∆ti

where xk := ∆Wk(ti).
(18.15)
Obviously this result is not limited to the case of Euler schemes. The only requirement with
respect to the scheme is that it is generated by the Brownian increments ∆W(ti) (e.g. as for a
Milstein scheme). We summarise our result in a theorem:
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
236
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

18.4. PARTIAL PROXY SIMULATION SCHEMES
Lemma (partial proxy):
Let K∗(ti), i = 0, 1, 2, . . ., denote a numerical scheme generated
from the Brownian increments ∆W(ti), i = 0, 1, 2, . . . (target scheme), i.e.
K∗(ti+1) = K∗(ti+1, K∗(ti), ∆W(ti) −v(ti))
Let K0(ti), i = 0, 1, 2, . . . denote another numerical scheme, also generated from the Brownian
increments ∆W(ti) and close to K∗.
For a given function f (the proxy constraint) let v(ti) denote a solution of
f(ti+1, K∗(ti+1, K∗(ti), ∆W(ti) −v(ti))) = f(ti+1, K1(ti+1))
and - assuming a solution exists - define the scheme K1 by
K1(ti+1) := K∗(ti+1, K∗(ti), ∆W(ti) −v(ti)).
Then the Monte-Carlo pricing under the scheme K∗is, in the Monte-Carlo limit, equivalent to
the pricing under the scheme K1 using the Monte-Carlo weights Q wi with wi given by (18.15).
We call the scheme K1 the (partial) proxy scheme satisfying the proxy constraint
f(ti+1, K1(ti+1)) = f(ti+1, K0(ti+1)).
18.4.4.3. Example
Since we desire an implementation that is both generic and fast, we would like to discuss
a special case, sufficiently general for all our applications and simple enough to give direct
formulas for the transition probabilities:
Assume that v(ti) is linearly dependent on the increment ∆W(ti), i.e.
v(ti) := A(ti) · ∆W(ti) + b(ti),
with A and b being Fti-measurable. Then we have for the mean-shifted diffusion
∆W(ti) −v(ti) = (1 −A(ti)) ·  ∆W(ti) −b(ti).
Thus the corresponding transition probability is normal distributed with mean b(ti) and stan-
dard deviation (1 −A(ti)) √∆ti. Note that if the target scheme is a small perturbation of the
reference scheme, then A(ti) is small and (1 −A(ti)) is non singular.
So here, the Fti+1-measurable mean shift is given by an Fti-measurable mean shift b and a
scaling of the “factor” ∆W. We will make use of this in our next example: A proxy constraint
stabilizing the calculation of vega, the sensitivity with respect to a change in the diffusion
coefficient.
18.4.4.4. Approximating an Fti+1-measurable proxy constraint by an
Fti-measurable proxy constraint
To allow rapid calculation of the transition probability we propose to approximate the proxy
constraint (18.11) by (18.12). Thus v(ti) is a Fti-measurable mean-shift and the ratio of the
transition probabilities is given by (18.13).
In addition we propose to linearize this constraint around K0(ti) + µ0(ti)∆ti, defining the
linear proxy constraint by Π := f ′(K0(ti) + µ0(ti)∆ti).
All of our benchmark examples are based on the approximative constraint (18.12) or its
linearization.
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
237
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

CHAPTER 18. PROXY SIMULATION SCHEMES FOR MONTE-CARLO SENSITIVITIES AND IMPORTANCE SAMPLING
18.4.5. Sensitivity with respect to the Diffusion Coefficients –
Vega
If we consider only an Fti-measurable mean shift applied to the Brownian increment ∆W(ti),
then the method is not applicable to the calculation of a sensitivity with respect to the diffusion
coefficient Γ(ti) - a.k.a. vega. The reason is simple: There is no Fti-measurable mean shift that
will ensure that the proxy constraint holds at ti+1 after a different (Fti+1-measurable) diffusion
has been applied – not even if the proxy constraint is a linear equation. Neglecting the Brown-
ian increment, as suggested in 18.4.4.4, is a step in the wrong direction, since we are interested
in the sensitivity with respect to the diffusion coefficient.
Of course, in our general formulation (18.11), a Fti+1-measurable mean shift applied to the
diffusion ∆W(ti) will ensure that the proxy constraint holds at time ti+1, even if the diffusion
coefficient has changed. However, to obtain a simple formula for the transition probability and
thus the Monte-Carlo weight w(ti), it is helpful to take an alternative view to the problem: The
idea is similar to what is done in the case of a full proxy scheme (see [66]): We modify the
diffusion of the proxy scheme to match the diffusion of the reference scheme and calculate the
corresponding change of measure. In other words, we use the unperturbed diffusion coefficient
for the (partial) proxy scheme. This adjustment is made prior to the calculation of the mean
shift v(ti) for the corresponding proxy constraint, which will correct additional differences in
the drift, if any.
From the previous section it is clear that this is equivalent to specifying a Fti+1-measurable
mean shift, being linear in the Brownian increment ∆W(ti).
18.4.6. Example: LIBOR Target Redemption Note
We are going to calculate delta and gamma for a TARN swap. The coupon for the period
[Ti, Ti+1] is an inverse floater max(K −2 · L(Ti, Ti+1), 0) and it is swapped against floating rate
L(Ti, Ti+1) until the accumulated coupon reaches a given target coupon. If the accumulated
coupon does not reach the target coupon, then the difference to the target coupon is paid at
maturity.
Thus the coupon of the tarn is linked to a trigger feature, similar to the digital caplet. How-
ever, here, the trigger depends on more than one rate, so it is not sufficient to set up a proxy
constraint for a single forward rate, unlike for the digital caplet.
Our unperturbed scheme is the LIBOR market model with the initial yield curve, evolving
the log-LIBOR with an Euler scheme. The natural perturbed scheme is then the same, except
for a different initial condition. We will use the following proxy constraint:
L1(T j, T j+1; t) = L0(T j, T j+1; t)
∀t ∈(T j−1, T j],
for all periods of the model to obtain the preferred proxy scheme. The constraint is realized by
a mean shift of the diffusion of the first factor, and since the forward rate follows a lognormal
process, we have v = (v1, 0, . . . , 0) with
v1(t) = log(L0(T j, T j+1; t)) −log(L1(T j, T j+1; t))
f1, j
,
where f1,j denotes the j-th component of the first factor. We assume here that f1,j , 0. A
non-zero factor loading exists as long as the forward rate L(T j, T j+1 has a non-zero volatility.
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
238
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

18.4. PARTIAL PROXY SIMULATION SCHEMES
The results can be improved if the factor having the largest absolute factor loading is chosen
(factor-pivoting).
Figure 18.3 shows the delta and gamma of a TARN swap for different shift sizes of finite
differences applied to standard re-simulation and partial proxy scheme simulation. For this
example the interest rate curve was upward sloping from 2% to 10% and for the TARN we
took K = 10% and a target coupon of 10%.
Gamma of TARN Swap (5000 paths)
0,0
5,0
10,0 15,0 20,0 25,0 30,0 35,0 40,0 45,0 50,0
shift in basis points
-40,00
-30,00
-20,00
-10,00
0,00
10,00
gamma
Figure 18.3.: Dependence of the TARN gamma on the shift size of the finite difference approximation.
Finite difference is applied to a direct simulation (red) and to a (partial) proxy scheme simulation (green).
Each dot corresponds to one Monte-Carlo simulation with the stated number of paths. The red and green
corridors represent the corresponding standard deviation.
The proxy scheme simulation shows no variance increase for small shift sizes while giving stable expected
values for the sensitivity.
With small shifts the variance of the delta and gamma calculated under full re-evaluation
increases and the mean becomes unstable, while the mean for delta and gamma calculated
under partial proxy scheme remains stable and the variance small. For increasing shift size
full re-evaluation stabilizes, but higher order effects give a significant bias. Very high shift
increases the Monte-Carlo variance of the likelihood ratio and thus increases the variance of
the delta and gamma calculated under the partial proxy scheme simulation.
18.4.7. Example: CMS Target Redemption Note
Next we will kook at a target redemption note with a coupon max(K −2 · I(Ti), 0), where the
index I(Ti) is a constant maturity swaprate, i.e. I(Ti) = S i,i+k(Ti) with
S i,i+k =
P(Ti) −P(Ti+k)
Pk−1
j=i (T j+1 −T j)P(T j+1)
=
P(Ti)
P(Ti+k) −1
Pk−1
j=i (T j+1 −T j) P(T j+1)
P(Ti+k)
=
Qi+k−1
l=i
(1 + L(Tl)(Tl+1 −Tl)) −1
Pk−1
j=i (T j+1 −T j) Qi+k−1
l=j+1(1 + L(Tl)(Tl+1 −Tl))
The swaprate S i,i+k(t) is a non-linear function of the forward rate curve L j(t), j = i, . . . , i +
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
239
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

CHAPTER 18. PROXY SIMULATION SCHEMES FOR MONTE-CARLO SENSITIVITIES AND IMPORTANCE SAMPLING
k −1 which we denote by S :
S i,i+k(t) = S (Li(t), . . . , Li+k−1(t)).
From the proxy simulation scheme we require S under L1 to match S under the reference
scheme L0. Our proxy constraint is therefore
S (L1
i (t), . . . , L1
i+k−1(t)) = S (L0
i (t), . . . , L0
i+k−1(t)).
We solve this equation by modifying the first factor, i.e. in each time step t j we determine a
single scalar v1(t j) such that
S (L∗
i (tj+1) + v1(t j) · f1,i, . . . , L∗
i+k−1(tj+1) + v1(t j) · f1,i+k−1)
= S (L0
i (tj+1), . . . , L0
i+k−1(tj+1))
(18.16)
and define L1
i (t j+1) := L∗
i (tj+1) + v1(t j) · f1,i.
To simplify and speed up the calculation, we (numerically) linearize equation (18.16) and
get an explicit (first order) formula for v1, see (18.10).
18.4.7.1. Delta and Gamma of a CMS TARN
The result of the calculation of delta and gamma is depicted in Figure 18.4. Using the simple
linearized proxy constraint we see a small increase in Monte-Carlo variance for the gamma
with very small shifts.
Gamma of CMS TARN Swap (5000 paths)
0,0
5,0
10,0 15,0 20,0 25,0 30,0 35,0 40,0 45,0 50,0
shift in basis points
-30,00
-25,00
-20,00
-15,00
-10,00
-5,00
0,00
5,00
10,00
gamma
Figure 18.4.: Dependence of the CMS TARN gamma on the shift size of the finite difference approxima-
tion. Finite difference is applied to a direct simulation (red) and to a (partial) proxy scheme simulation
(green). The proxy constraint used was a simple (numerical) linearization of (18.16).
The linearized constraint remains stable for small shifts. However, using a few Newton
iterations on the linearization solves the non-linear constraint and further improves the result
for the gamma, see Figure 18.5.
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
240
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

18.4. PARTIAL PROXY SIMULATION SCHEMES
Gamma of CMS TARN Swap (5000 paths)
0,0
5,0
10,0 15,0 20,0 25,0 30,0 35,0 40,0 45,0 50,0
shift in basis points
-25,00
-20,00
-15,00
-10,00
-5,00
0,00
5,00
gamma
Figure 18.5.: Dependence of the CMS TARN gamma on the shift size of the finite difference approxima-
tion. Finite difference is applied to a direct simulation (red) and to a (partial) proxy scheme simulation
(green). The proxy constraint is given by applying a few Newton iterations to the (numerical) lineariza-
tion of (18.16).
18.4.7.2. Vega of a CMS TARN
We will calculate the vega of a CMS TARN, i.e. the sensitivity of the CMS TARN with respect
to a parallel shift of all instantaneous volatilities. The result is depicted in Figure 18.6. For
medium and large shift size the vega calculated from finite differences applied to a partial proxy
is similar to the vega calculated from finite differences applied to direct simulation. However,
note that for very small shift sizes (around 1 bp), the vega calculated from finite differences
applied to direct simulation converges to an incorrect value and that this result occurs with a
very small Monte-Carlo variance.
The reason for this effect is that the shifts are too small to trigger a change in the exercise
strategy. Hence, the vega calculated is the sensitivity conditional on no change in exercise
strategy, which is of course a different thing, see Section 17.2.4.
This effect is also present for delta and gamma and for all trigger products, but it has not
been visible in the figures so far due to the scale of the shift sizes and the number of paths used
there.
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
241
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

CHAPTER 18. PROXY SIMULATION SCHEMES FOR MONTE-CARLO SENSITIVITIES AND IMPORTANCE SAMPLING
Vega of CMS TARN Swap (5000 paths)
0,0
1,0
2,0
3,0
4,0
5,0
6,0
7,0
8,0
9,0
10,0
shift in basis points
-0,60%
-0,50%
-0,40%
-0,30%
-0,20%
-0,10%
0,00%
0,10%
0,20%
vega
Figure 18.6.: Dependence of the CMS TARN vega on the shift size of the finite difference approximation.
Finite difference is applied to a direct simulation (red) and to a (partial) proxy scheme simulation (green).
The proxy constraint was given by applying a few Newton iterations to the (numerical) linearization of
(18.16).
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
242
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

Part V.
Pricing Models for Interest Rate
Derivatives
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
243
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book


CHAPTER 19
Market Models
The pure and simple truth
is rarely pure and never simple.
Oscar Wilde
The Importance of Being Earnest, [39].
Up until now we have been considering models of a single scalar stochastic process and
options on it: The Black-Scholes model for a stock S , or the Black model for a forward rate
L. The true challenge in evaluation of interest rate products lies in the modeling of the whole
interest rate curve (instead of a scalar) and in the evaluation of complex derivatives, which
depend on the whole curve.
Historically the path to modeling the interest rate curve started with the modeling of the short
rate, from which we may calculate the whole interest rate curve, see Remark 104. The initial
motivation for considering the short rate derived from the wish to model a scalar quantity, thus
to be able to apply familiar numerical methods from stock models, e.g. binomial trees.
For didactic reasons we are not going to present things chronologically. Instead, we con-
sider the LIBOR Market Model first. It is a high dimensional model, which discretizes the
interest rate curve into a finite number of forward rates. It is highly flexibly due to its huge
number of free parameters. It will allow us to study model properties like mean reversion,
number of factors (Chapter 24), instantaneous volatility, instantaneous and terminal correla-
tion (Chapter 20). Despite its presumed complexity, the LIBOR Market Model is essentially a
very simple model: It is nothing more than the simultaneous consideration of multiple Black
models under a common measure. So we are carrying on from Chapter 10.
For the Short Rate models the modeled quantity is the short rate, a quantity not directly
observable. Here we model quantities which are observable as market quotes, like the LIBOR
or the Swaprate. The class of models that model quantities which are directly observable on
the market are called “Market Models”. We will look at the LIBOR Market Model first:
19.1. LIBOR Market Model
We assume a time discretization (tenor structure)
0 = T0 < T1 < . . . < Tn.
We model the forward rates Li := L(Ti, Ti+1) for i = 0, . . . , n −1, see Definition 99. This
represents a discretization of the interest rate curve, where the continuum of maturities has
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
245
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

CHAPTER 19. MARKET MODELS
been discretized.1
The LIBOR market model assumes a lognormal dynamic for LIBORs Li := L(Ti, Ti+1), i.e.2
dLi(t)
Li(t) = µP
i (t)dt + σi(t)dWP
i (t)
for i = 0, . . . , n −1, under P,
(19.1)
with initial conditions
Li(0) = Li,0,
with Li,0 ∈[0, ∞), i = 0, . . . , n −1,
where WP
i denote (possibly instantaneously correlated) P-Brownian motions with
dWP
i (t)dWP
j (t) = ρi,j(t)dt.
Let σi : [0, T] 7→R and ρi, j : [0, T] 7→R be deterministic functions and µi the Drift as
Ft-adapted process. By R(t) := (ρi,j(t))i,j=0,...,n−1 we denote the correlation matrix.
Motivation:
Equation (19.1) is a lognormal model for the forward rates Li. If
we consider only a single equation, i.e. fix i ∈{1, . . . , n−1}, it represents the Black
model considered in Section 10: Equation (19.1) is identical with Equation (10.1).
If we change the measure such that Li is drift-free (see Section 10), we see that
the terminal distribution of Li is lognormal.
Thus, the LIBOR market model is equivalent to the consideration of n Black models under
a unified measure.
As was discussed in Section 10, to evaluate a caplet under this model it is not relevant that
σi is time dependent (we have assumed time-dependency of σi in Section 10 for didactical
reasons). However, for the value of complex derivatives the time dependency matters. A fur-
ther degree of freedom introduced in (19.1) is the instantaneous correlation ρi, j of the driving
Brownian motions. For the value of a caplet the instantaneous correlation is insignificant (in-
deed, it does not enter in the Black model). For the evaluation of Swaptions the correlation of
the forward rates is significant.
For further generalizations of the model, consider non-deterministic σi, i.e. stochastic
volatility models. In this case the terminal LIBOR distributions no longer correspond to the
Black model ones, which is, of course, intended. Equation (19.1) is to be seen as a starting
point of a whole model family. The model (19.1) has been chosen as the starting point, because
(historically) the lognormal (Black) model is well understood, especially by traders.3
◁|
Remark 211 (Interest Rate Structure):
Equation (19.1) models the evolution of the LIBOR
L(Ti, Ti+1). Without further interpolation assumption, these are the shortest forward rates that
can be considered in our time discretization (tenor structure). The equation system (19.1) thus
determines the evolution of all bond prices with maturities Ti and all forward rates for the
1 In practice it is normal to model semi-annual or quarterly rates Ti+1 −Ti = 0.25 and to consider these up to a
maturity of 20 or 30 years, giving 80 or 120 interest rates to model.
2 We denote the simulation time parameter of the stochastic process by t.
3 Caplet prices are quoted by traders by the implied Black volatility. This is of course just another unit of the price,
since the Black model is a one-to-one map from price to implied volatility.
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
246
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

19.1. LIBOR MARKET MODEL
periods [Ti, Tk], since
1 + L(Ti, Tk)(Tk −Ti) = P(Ti)
P(Tk) =
k−1
Y
j=i
P(T j)
P(T j+1)
=
k−1
Y
j=i
(1 + L(T j, T j+1)(T j+1 −T j)).
To shorten notation we write δi := Ti+1 −Ti, i = 0, . . . , n −1 for the period length.
19.1.1. Derivation of the Drift Term
As in Chapters 10 and 11, our first step is to choose some num´eraire N and derive the drift under
a martingale measure QN. If the processes have been derived under the martingale measure
QN, then the (discretized) interest rate curve may be simulated numerically and a derivative V
may be prices through V(0) = N(0)EQN( V
N |FT0) (see Chapter 13).
We fix a num´eraire N. Let the assumptions of Theorem 74 hold, such that there exists a
corresponding equivalent martingale measure QN such that N-relative prices are martingales.
From Theorem 58 under QN the process (19.1) has a changed drift, namely
dLi(t)
Li(t) = µQN
i (t)dt + σi(t)dWQN
i
(t)
for i = 0, . . . , n −1.
(19.2)
19.1.1.1. Derivation of the Drift Term under the Terminal Measure
We fix the Tn-Bond N(t) = P(Tn; t) as num´eraire. From Theorem 58 under QP(Tn) the process
(19.1) has a changed drift:
dLi(t)
Li(t) = µQP(Tn)
i
(t)dt + σi(t)dWQP(Tn)
i
(t)
for i = 0, . . . , n −1.
(19.3)
We need to determine µQP(Tn)
i
. The martingale measure QP(Tn) corresponding to N(t) = P(Tn; t)
is also called terminal measure (since Tn is the time horizon of our time discretization).
As in Chapter 10, we will construct relative prices with respect to P(Tn) and obtain equations
from which we will derive the drifts µi. From Definition 99
n−1
Y
k=i
(1 + δkLk)
|      {z      }
=
P(Tk)
P(Tk+1)
=
n−1
Y
k=i
P(Tk)
P(Tk+1) = P(Ti)
P(Tn)
for i = 0, . . . , n −1.
(19.4)
Since we have a P(Tn)–relative price of a traded product on the right hand side in (19.4), we
have for the drifts:
Drift
QP(Tn)

n−1
Y
k=i
(1 + δkLk)
= 0,
i = 0, . . . , n −1.
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
247
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

CHAPTER 19. MARKET MODELS
We apply Theorem 47 and obtain ∀i = 0, . . . , n −1
d

n−1
Y
k=i
(1 + δkLk)
=
n−1
X
j=i
n−1
Y
k=i
k, j
(1 + δkLk) · δ jdLj +
n−1
X
j,l=i
l> j
n−1
Y
k=i
k, j,l
(1 + δkLk) · δ jdLjδldLl
=
n−1
Y
k=i
(1 + δkLk) ·

n−1
X
j=i
δ jdLj
(1 + δjLj) +
n−1
X
j,l=i
l>j
δ jdLj
(1 + δjLj) ·
δldLl
(1 + δlLl)

=
n−1
Y
k=i
(1 + δkLk) ·
n−1
X
j=i

δ jdLj
(1 + δjLj) +
X
l≥j+1
l≤n−1
δjdLj
(1 + δ jLj) ·
δldLl
(1 + δlLl)

.
Since ∀i = 0, . . . , n −1
Drift
QP(Tn)

n−1
Y
k=i
(1 + δkLk)
= 0
(19.5)
it follows that ∀i = 0, . . . , n −1
n−1
X
j=i
Drift
QP(Tn)

δ jdLj
(1 + δ jLj) +
X
l≥j+1
l≤n−1
δjdLj
(1 + δ jLj) ·
δldLl
(1 + δlLl)

= 0
(19.6)
and thus ∀j = 0, . . . , n −1
Drift
QP(Tn)

δ jdLj
(1 + δ jLj) +
X
l≥j+1
l≤n−1
δjdLj
(1 + δ jLj) ·
δldLl
(1 + δlLl)

= 0
(19.7)
If we now use
dL j = LjµQP(Tn)
j
dt + Ljσ jdWQP(Tn)
j
and
dLj · dLl = LjLlσ jσlρj,ldt
in (19.7), then we have
µQP(Tn)
j

δjLj
(1 + δ jLj) +
X
l≥j+1
l≤n−1

δ jLj
(1 + δ jLj) ·
δlLl
(1 + δlLl) · σjσlρj,l = 0,
i.e.
µQP(Tn)
j
(t) = −
X
l≥j+1
l≤n−1
δlLl(t)
(1 + δlLl(t)) · σ j(t)σl(t)ρj,l(t).
(19.8)
The procedure above may be summarized as follows: To derive the n drifts we write down
n independent traded assets as a function of the model quantities. By considering the drifts of
their relative prices we obtain n equations for the drifts of the modeled quantities.
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
248
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

19.1. LIBOR MARKET MODEL
19.1.1.2. Derivation of the Drift Term under the Spot LIBOR Measure
We fix the rolled over one period bond as num´eraire, i.e. the investment of 1 at time T0 into
the T1-Bond and after its maturity the reinvestment of the proceeds into the bond of the next
period, i.e. in T j the reinvestment inf the T j+1-Bond. It is
N(t) := P(Tm(t)+1; t)
m(t)+1
Y
j=1
1
P(T j; T j−1)
|        {z        }
z                                              }|                                              {
= P(T j−1; T j−1)
P(T j; T j−1) = (1 + L j−1(T j−1)δ j−1)
= P(Tm(t)+1; t)
m(t)
Y
j=0
(1 + Lj(T j) · δ j),
(19.9)
m(t) := max{i : Ti ≤t} and δj := T j+1 −T j The corresponding equivalent martingale measure
QN is called the spot measure.
As before, we consider the processes of N-relative prices of traded products (from which we
know that they have drift 0 under QN). We consider the N-relative prices of the bonds P(Ti).
It is
P(Ti; t)
N(t)
=
P(Ti; t)
P(Tm(t)+1; t) ·
m(t)
Y
j=0
(1 + Lj(T j)δ j)−1
=
i−1
Y
j=m(t)+1
(1 + L j(t)δ j)−1 ·
m(t)
Y
j=0
(1 + Lj(T j)δj)−1,
(19.10)
thus
Drift
QN

i−1
Y
k=m(t)+1
(1 + Lkδk)−1
= 0.
(19.11)
Since
d

i−1
Y
j=m(t)+1
(1 + L j(t)δj)−1 ·
m(t)
Y
j=0
(1 + Lj(T j)δ j)−1

= d

i−1
Y
j=m(t)+1
(1 + Lj(t)δj)−1
·
m(t)
Y
j=0
(1 + Lj(T j)δ j)−1
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
249
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

CHAPTER 19. MARKET MODELS
we consider
d

i−1
Y
k=m(t)+1
1
(1 + δkLk)

=
i−1
X
j=m(t)+1
i−1
Y
k=m(t)+1
k, j
1
(1 + δkLk) ·

−δ jdLj
(1 + δjLj)2 +
δ2
jdLjdLj
(1 + δ jLj)3

+
i−1
X
j,l=m(t)+1
l< j
i−1
Y
k=m(t)+1
k,j,l
1
(1 + δkLk) ·

δjdLj
(1 + δ jLj)2 +
δ2
jdLjdLj
(1 + δ jLj)3


δldLl
(1 + δlLl)2 +
δ2
l dLldLl
(1 + δlLl)3

=
i−1
Y
k=m(t)+1
1
(1 + δkLk) ·

i−1
X
j=m(t)+1
−δ jdLj
(1 + δjLj) +
δ2
jdLjdLj
(1 + δ jLj)2 +
i−1
X
j,l=m(t)+1
l<j
−δ jdLj
(1 + δ jLj) ·
−δldLl
(1 + δlLl)

=
i−1
Y
k=m(t)+1
1
(1 + δkLk) ·
i−1
X
j=m(t)+1
−
δ jdLj
(1 + δjLj) +
j
X
l=m(t)+1
δ jdLj
(1 + δjLj) ·
δldLl
(1 + δlLl)
.
With (19.11) we have ∀i = 0, . . . , n −1
i−1
X
j=m(t)+1
Drift
QN
−
δ jdL j
(1 + δjL j) +
j
X
l=m(t)+1
δ jdL j
(1 + δjLj) ·
δldLl
(1 + δlLl)
= 0
and thus ∀j = 0, . . . , n −1
Drift
QN

−δ jdL j
(1 + δjL j) +
j
X
l=m(t)+1
δ jdL j
(1 + δjLj) ·
δldLl
(1 + δlLl)
= 0
(19.12)
If we now use
dLj = L jµQN
j dt + Ljσ jdWj
and
dL j · dLl = L jLlσjσlρj,ldt
in (19.7), then we have4
−µQN
j 
δ jLj
(1 + δjL j) +
j
X
l=m(t)+1
δ jL j
(1 + δ jLj) ·
δlLl
(1 + δlLl) · σ jσlρj,l = 0,
i.e.
µQN
j (t) =
j
X
l=m(t)+1
δlLl(t)
1 + δlLl(t)σ j(t)σl(t)ρ j,l(t).
19.1.1.3. Derivation of the Drift Term under the Tk-Forward Measure
Exercise: (Drift under the Tk-forward measure) Consider
N(t) :=

P(Tk; t) ,
t ≤Tk
P(Tm(t)+1; t)
m(t)+1
Y
j=k+1
1
P(T j; T j−1) ,
t > Tk,
where m(t) := max{i : Ti ≤t}.
4 Since the coefficient of dt equals 0.
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
250
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

19.1. LIBOR MARKET MODEL
1. Give an interpretation of N(t) as traded product.
2. Derive the drift of the model (19.1) under the QN measure with the num´eraire N.
Solution:
µj(t) = −
k−1
X
l= j+1
δlLl
(1 + δlLl)σ jσlρj,l
for j < k −1
and t ≤Tk
µj(t) = 0
for j = k −1
and t ≤Tk
µj(t) =
j
X
l=k
δlLl
(1 + δlLl)σ jσlρj,l
for j ≥k
and t ≤Tk
µj(t) =
j
X
l=m(t)+1
δlLl
(1 + δlLl)σ jσlρj,l
for t > Tk.
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
251
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

CHAPTER 19. MARKET MODELS
19.1.2. The Short Period Bond P(Tm(t)+1; t)
For t < {T1, . . . , Tn} neither the num´eraire N(t) of the terminal measure nor the num´eraire of the
spot measure is not fully described by the processes Li(t). The unspecified bond P(Tm(t)+1; t)
occurs in both num´eraires. We will now discuss the relevance of P(Tm(t)+1; t).
19.1.2.1. Role of the short bond in a LIBOR Market Model
For the modeling of the forward rates Li(t) := L(Ti, Ti+1; t) on the tenor periods [Ti, Ti+1], i =
0, . . . , n the specification of P(m(t) + 1; t) is irrelevant. For the derivation of the corresponding
drift terms it was not relevant to specify the stochastic of P(Tm(t)+1; t), since the term canceled
for the relative prices considered.
Conversely, the LIBOR Market Model does not describe the stochastic of the short bond
P(Tm(t)+1; t), since it is not given as a function of the processes Li(t).
19.1.2.2. Link to continuous time tenors
The specification of the short bond P(Tm(t)+1; t) becomes relevant if the model has to de-
scribe interest rates of interest rate periods which are not part of the tenor structure. The
specification of P(m(t) + 1; t) will determine how the fractional forward rates L(Ts, Te; t) with
Ts < {T1, . . . , Tn} and/or Te < {T1, . . . , Tn} will evolve (see Section 19.1.5). It is the link from
a model with discrete tenors (LIBOR Market Model) to a model with continuous time tenors
(Heath-Jarrow-Morton Framework). In the special case where P(m(t)+1; t) has zero volatility,
the LIBOR Market Model under spot measure coincides with a Heath-Jarrow-Morton Frame-
work with a special volatility structure under the risk-neutral measure (see Section 23.2).
19.1.2.3. Drift of the short bond in a LIBOR Market Model
Within the LIBOR Market Model there is no constraint on the drift of P(m(t) + 1; t), because
in P(m(t)+1;t)
N(t)
the term cancels out. The relative price P(m(t)+1;t)
N(t)
is always a martingale for any
choice of P(m(t) + 1; t). This might come as a surprise, but we have already encountered this
behavior: In the Black-Scholes model the drift r of B(t) is a free parameter, because it is the
drift of the num´eraire. The parameter r is determined by calibration to a market interest rate.
In a short rate model the drift is a free parameter. It is determined by calibration to the market
interest rate curve, see Section 22. Here, similarly, P(m(t) + 1; t) determines the interpolation
of the initial interest rate curve.
The trivial fact that the num´eraire relative price of the num´eraire, i.e. N(t)
N(t), is always a mar-
tingale plays a role in Markov functional models. There, the num´eraire is postulated to be a
functional of some Markov process.
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
252
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

19.1. LIBOR MARKET MODEL
19.1.3. Discretization and (Monte-Carlo) Simulation
In this section we will discuss the discretization and implementation of the model. Let us there-
fore assume that the free parameters σi, ρi, j and Li,0 (i, j = 1, . . . , n) are given. Together with
the drift formula obtained in the previous section the model is fully specified. In Section 19.1.4
will then discuss how the parameters Li,0, σi, ρi,j are obtained.
19.1.3.1. Generation of the (time-discrete) Forward Rate Process
As discussed in Chapter 13, we choose the Euler discretization of the Itˆo process of log(Li).
From Lemma 49 we have
d(log(Li(t))) =  µQN
i (t) −1
2σ2
i (t)dt + σi(t)dWQN
i
(t)
(19.13)
and the corresponding Euler scheme of (19.13) is
log( ˜Li(t + ∆t)) = log( ˜Li(t)) + (µi(t) −1
2σ2
i (t))∆t + σi(t)∆Wi(t),.
(19.14)
Applying the exponential gives us the discretization scheme of Li as
˜Li(t + ∆t) = ˜Li(t) · exp  (µi(t) −1
2σ2
i (t))∆t + σi(t)∆Wi(t).
(19.15)
In the special case that the process Li is considered under the measure QP(Ti+1), i.e. µQP(Ti+1)
i
(t) =
0, and that the given σi(t) is a known deterministic function, then we may use the exact solution
for a discretization scheme:
Li(t + ∆t) = Li(t) · exp   −1
2 ¯σi
2(t, t + ∆t)∆t + ¯σi(t, t + ∆t)∆Wi
,
where
¯σi(t, t + ∆t) :=
s
1
∆t
Z t+∆t
t
σ2
i (τ)dτ.
In the case where Li is not drift-free, we choose instead of (19.15) the discretization scheme
Li(t + ∆t) = Li(t) · exp  (µi(t) −1
2 ¯σi(t, t + ∆t)2)∆t + ¯σi(t, t + ∆t)∆Wi(t)
(19.16)
(we write L in place of ˜L, although (19.16) is an approximation of (19.1)). The diffusion dW
is discretized by exact solution; the drift dt is discretized by an Euler scheme. The discretiza-
tion error of this scheme stems from the discretization of the stochastic drift µi only. This
discretization error results in a violation of the no-arbitrage requirement of the model (the dis-
cretized model does not have the correct, arbitrage-free drift). Methods which do not exhibit
an arbitrage due to a discretization error are called arbitrage-free discretization, see [69]).
The volatility functions σi are usually assumed to be piecewise constant functions on
[T j, T j+1), such that ¯σi(t, t + ∆t) may be calculated analytically. It is ¯σi(t, t + ∆t) = σi(t).
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
253
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

CHAPTER 19. MARKET MODELS
19.1.3.2. Generation of the Sample Paths
Equipped with the time discretization (19.16), realizations of the process are calculated for
a given number of paths ω1, ω2, ω3, . . ..
To do so, normal distributed random numbers
∆Wi(tj)(ωk), correlated according to R = (ρi, j), are generated (see Appendix A.2 and A.3).
These are used in the scheme (19.16). The result is a three dimensional tensor Li(t j, ωk)
parametrized by
i : Index of the interest rate period (tenor structure),
j : Index of the simulation time,
k : Index of the simulation path.
19.1.3.3. Generation of the Num´eraire
Given a simulated interest rate curve Li(tj, ωk), we can calculate the num´eraire. Of course we
have to use the num´eraire that was chosen for the martingale measure under which the process
was simulated (form of the drift in (19.13)). For the terminal measure we would calculate
N(Ti, ωk) =
n−1
Y
j=i
(1 + Lj(Ti, ωk) · (T j+1 −T j))−1.
Note: The num´eraire is given only at the tenor times t = Ti, since for t , Ti we did not define
the short period bond P(Tm(t)+1; t).5 An interpolation is possible, see Section 19.1.5 and [90].
19.1.4. Calibration - Choice of the free Parameters
We are now going to explain how the free parameters of the model can be chosen. The free
parameters are
• the initial conditions Li,0,
i = 0, . . . , n −1,
• the volatility functions or volatility processes6 σi,
i = 1, . . . , n −1,
• the (instantaneous) correlation ρi, j,
i, j = 1, . . . , n −1.
The determination of the free parameters is also called calibration of the model.
Motivation (Reproduction of Market Prices versus Historical Estima-
tion):
With the LIBOR Market Model we have a high-dimensional model
framework. The main task is the derivation or estimation of the huge amount of
free parameters. Two approaches are possible:
• Reproduction of Market Prices: The parameters are chosen such that the model repro-
duces given market prices.
• Historical Estimation: The parameters are estimated from historical data, e.g. time
series of interest rate fixings.
5 See Section 19.1.2.
6 The parameters σi may well be stochastic processes. In this cases σi is called a stochastic volatility model.
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
254
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

19.1. LIBOR MARKET MODEL
It may be surprising at first, but the second approach is not meaningful, being in the context
of risk-neutral evaluation. The model is considered under the martingale measure QN and
its aim is the evaluation and hedging (!) of derivatives. An expectation of the relative value
under the martingale measure corresponds to the relative value of the replication portfolio.
This replication portfolio has to be setup from traded products, traded at current (!) market
prices. If the model did not replicate current market prices, then it would not possible to buy
the replication portfolio of a derivative at the model price of the derivative. The model price
would inevitably be wrong.
This remark applies to all free model parameters. In practice, however, it may be difficult
or impossible to derive all parameters from market prices. This could be because for a specific
product no reliable price is known (low liquidity). It could also be that a corresponding product
does not exist. This is often the case for correlation sensitive products from which we would
like to derive the correlation parameters. If a parameter cannot be derived from a market price
a historical estimate becomes an option. If in such a case complete hedge is not possible, the
residual risk has to be considered, e.g. by a conservative estimate of the parameter.
For the LIBOR market model a parameter reduction is usually applied first, based on his-
torical estimates of rough market assessment. An example of such parameter reduction is the
assumption of a family of functional forms for the volatility σi(t) or the correlation ρi,j(t). The
remaining degrees of freedom are then derived from market prices.
◁|
19.1.4.1. Choice of the Initial Conditions
Reproduction of Bond Market Prices
Let PMarket(Ti) ∈[0, 1] denote a market observed
(i.e. given) price of a Ti-bond. If we set
Li,0 := PMarket(Ti) −PMarket(Ti+1)
PMarket(Ti+1)(Ti+1 −Ti) ,
then the model reproduces the given market prices of the bonds PMarket. This is ensured by the
model having the “right” drift and it is independent of the other parameters.
19.1.4.2. Choice of the Volatilities
Reproduction of Caplet Market Prices
We assume here that the σi’s are deterministic
functions (i.e. not random variables or stochastic processes). The forward rate Li follows the
Itˆo process
dLi(t) = µQ
i (t)Li(t)dt + σi(t)Li(t)dWQ
i (t)
under Q := QN.
Thus the model corresponds to the Black model discussed in Chapter 10. Under QP(Ti+1) we
have µQP(Ti+1)
i
= 0, the distribution of Li(Ti) is lognormal and there exists an analytic evaluation
formula for caplets. The only model parameters that enter the caplet price are L0(Ti) and
σBlack,Model
i
:=   1
Ti
Z Ti
0
σ2
i (t)dt1/2.
(19.17)
If the market price VMarket
Caplet,i of a caplet on the forward rate Li(Ti) is given, then the corresponding
implied Black volatility σBlack,Market
i
may be calculated by inverting7 Equation (10.2). If then
7 For inversion of pricing formula we may use a simple numerical algorithm. For the Black formula (10.2) the price
is increasing strictly monotone in the volatility.
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
255
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

CHAPTER 19. MARKET MODELS
σi(t) is chosen such that
σBlack,Model
i
= σBlack,Market
i
,
(19.18)
then the model reproduces the given caplet price VMarket
Caplet,i. A possible trivial choice is, e.g.,
σi(t) = σBlack,Market
i
∀t.
Remark 212 (Caplet Smile Modeling):
The fact that the LIBOR Market Model calibrates to
the cap market by a simple boundary condition is one reason for its initial popularity. However,
since the model restricted to a single LIBOR is a Black model, the implied volatility does not
depend on the strike of an option. Thus, in this form, the model may calibrate to a single caplet
per maturity only. It cannot render a caplet smile, yet.
For extensions of the model that try to remove this restriction see [23].
Reproduction of Swaption Market Prices
If the correlation R = (ρi,j) is given and
fixed, then we influence swaption prices through the time structure of the volatility function
t 7→σi. We consider swaptions that correspond to our tenor structure, i.e. option on the
Swaprates
S (Ti, . . . , T j; Ti),
0 < i < j ≤n.
From the definition of the swap and swap rate it is obvious that the price of a corresponding
swaption with exercise date on or before Ti and periods [Ti, Ti+1], . . . , [T j−1, T j] depends only
on the behavior of the forward rates Li(t), . . . , L j−1(t) until the fixing t ≤Ti, see Figure 19.1.
T0
Ti
Ti+1
Swap(Ti,...Tj)
Ti+2
Tj-1
Ti+3
Tj
T1
Lj-1
Li+2
Li+1
Li
Figure 19.1.:
Swaption as a function of the forward rates:
The swap with periods
[Ti, Ti+1], . . . , [T j−1, T j] is a function of the forward rates L(Ti, Ti+1; Ti), . . . , L(T j−1, T j; Ti) (all with fixing
in Ti). The corresponding swaption depends only on the joint distribution of these forward rates. Under
our model, with given initial conditions Li,0 and correlation R = (ρi,j), the swaption price depends on
σi(t), . . . , σ j−1(t), t ∈[0, Ti] only. The dynamic of these forward rated beyond the t > Ti and all other
forward rates do not influence the swaption price.
If we discretize the volatility function corresponding to the tenor structure and define
σk,l :=  1
Tl+1 −Tl
Z Tl+1
Tl
σ2
k(t)dt1/2,
the price of an option on the swap rate S (Ti, . . . , T j; Ti) depends only on σk,l for k = i, . . . , j−1
and l = 0, . . . , i −1. This allows an iterative calculation of σk,l from given swaption market
prices:
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
256
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

19.1. LIBOR MARKET MODEL
For i = 1, . . . , n −1:
For j = i + 1, . . . , n:
Calculate σ j−1,i−1 from the price of an option on S (Ti, . . . , T j; Ti) by consider-
ing the already calculated σk,l with k = i, . . . , j −1 and l = 0, . . . , i −2 from
the previous iterations.
To derive σ j−1,i−1 from the market price Vmarket
swaption(Ti, . . . , T j) we have to invert the mapping
σ j−1,i−1 7→Vmodel
swaption(Ti, . . . , T j).
In principle this mapping may be realized by a Monte-Carlo evaluation of the swaption. To al-
low for faster pricing, and thus faster calibration, analytic approximation formulas for swaption
prices within a LIBOR Market Model have been derived, see also Section 19.1.4.4.
Remark 213 (Bootstrapping):
The above procedure of calculating a piecewise constant
instantaneous volatility from swaption prices is called volatility bootstrapping.
Remark 214 (Review: Overfitting): The calculation of a piecewise constant volatility func-
tion σi, j from swaption prices bears the risk of an overfitting of the model. Note that if this
procedure is applied, then we accept completely the validity of every single given swaption
price, i.e. that the prices are of sufficiently good quality with respect to topicality (fixing time
of the price) and liquidity. If not all prices are of the same quality, then some have to be
interpolated, smoothed or corrected by hand. In this case, the calibration problem has been
replaced by an interpolation problem. If the interpolation and maintenance of the market data
is not done with care, a calibration that fits to these prices exactly may be useless. See for
example Chapter 6.
In addition, the bootstrapping of the instantaneous volatility from swaption prices does not
allow for a weighting of the swaption prices according to their importance.
A solution to this is the reduction of the free parameters by a reduction of the family of
admissible volatility functions with consequent loss of the perfect fit.
Functional Forms
To reduce the risk of overfitting, the admissible volatility functions may
be restricted to a parametrized family of volatility functions. For example, a functional which
is empirically motivated by the historical shapes of the volatility and which is common in
practice is
σi(t) := (a + b · (Ti −t)) · exp(−c · (Ti −t)) + d.
Given a functional form, the calibration of the model consists of a selection of (liquid)
market prices of caps and swaptions and an optimization of the remaining parameters (e.g. a,
b, c, d above) to fit the model prices to the market prices.
For a detailed discussions of a robust calibration to cap and swaption prices we refer to the
literature, especially [8, 30].
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
257
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

CHAPTER 19. MARKET MODELS
19.1.4.3. Choice of the Correlations
Factors
We assumed in (19.1) a model in which (potentially) each forward rate Li Brownian
motion Wi. The model is driven by an n-dimensional8 Brownian motion
W =

W0
W1
. . .
Wn−1

.
The effective number of factors, i.e. the number of independent Brownian motions, that are
driving the model is determined by the correlation
ρi,j(t)dt = dWi(t) · dWj(t).
By an eigenvector decomposition (PCA) of the correlation matrix R = (ρi, j)i,j=1...n we may
represent dW as
dW(t) = F(t)dU(t),
where U := (U1, . . . , Um)T and U1, . . . , Um denote independent Brownian motions and F =
(fi,j) denotes a n × m-matrix. In other words, we have
dWi(t) =
m
X
j=1
fi, j(t)dU j(t),
ρi,j(t) =
m
X
k=1
fi,k(t) · f j,k(t).
A proof of this representation is in the Appendix A.3. Note that here we can have m < n. The
columns of the matrix F are called factors.
Functional Forms
A full rank correlation matrix R is hard to derive from market instru-
ments. As before a common procedure is to reduce the family of admissible correlation ma-
trixes R. One ansatz consists of functional forms, for example
ρi,j(t) := exp(−α · |i −j|).
(19.19)
Factor Reduction
The specification of the correlation matrix as a functional form is usu-
ally followed by a reduction of the number of factors. This is done in what is known as factor
reduction (PCA, Principal Component Analysis). There only the eigenvectors corresponding
to the largest eigenvalues of R are considered and a new correlation matrix is formed from
these selected factors. For a discussion of the factor reduction see Appendix A.4.
The advantage of the factor reduction is that afterwards only an m-dimensional Brownian
motion has to be simulated (and not an n-dimensional Brownian motion). Often n ≥40 is
required (e.g. a 20 year interest rate curve with semi-annual periods), however often m ≤5
is sufficient. The choice of the actual number m of factors depends on the application, see
Chapter 24.
8 An n −1-dimensional Brownian motion is sufficient here, since we can choose W0 = 0, because the forward rate
L0 is not stochastic. It is fixed in T0 = 0. Formally we achieve this by setting σ0 ≡0.
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
258
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

19.1. LIBOR MARKET MODEL
Calibration
The correlation model, e.g. the free parameter a in (19.19), may be chosen such
that the fit of model prices to given market prices is improved. Alternatively it may be chosen
to give more realistic interest rate correlations. See also Remark 214.
It should be stressed that we calibrate the instantaneous correlation, i.e. the correlation of the
Brownian increments dW, and not the terminal correlation, i.e. the correlations of the distribu-
tion of the interest rates at a fixed time. We will consider the relation of the two in Chapter 20.
19.1.4.4. Covariance Matrix, Calibration by Parameter Optimization
In the previous sections we considered volatility and correlation separately. This is not neces-
sary, as both can be considered together in the form of the correlation matrix (σiσ jρi,j). Thus
the calibration problem consists of the calculation of the (market implied) covariance matrix
(or covariance matrix function).
Defining the parametrized functional forms for volatility and correlation, e.g. as
σi(t) := (a + b · (Ti −t)) · exp(−c · (Ti −t)) + d,
ρi, j(t) := exp(−α · |i −j|)
reduces the number of degrees of freedom of the covariance model and thus the possible num-
ber of products for which an exact fit is possible. This might be a desired feature, e.g. to avoid
an overfitting. A disadvantage is the lack of transparency of the parameters. To derive the pa-
rameters a numerical optimization has normally to be used, e.g. the minimization of a suitable
norm of the error vector of some selected product prices as a function of the model parameters.
The optimization of volatility parameters and correlation parameters may occur jointly, i.e. we
consider a functional form of the covariance structure.
19.1.4.5. Analytic Evaluation of Caplets and Swaptions
To calculate the calibration error we need to calculate the corresponding model prices. Since
a numerical calculation of the model price (e.g. by a full Monte-Carlo simulation) is time
consuming, and since the optimization requires many calculation of model prices, there is a
need for fast analytical pricing formulas of specific calibration products.
Analytic Evaluation of a Caplet in the LIBOR Market Model
The analytic evaluation
of caplets in the LIBOR market model by the Black formula (10.2) using (19.17) to calculate
the Black volatility.
Analytic Evaluation of a Swaption in the LIBOR Market Model
The analytic evalu-
ation of swaption in the LIBOR market model is possible by an approximation formula only.
An approximation formula can be derived by expressing the volatility of the swap rate as a
function of the volatility and correlation of the forward rates. Assuming a lognormal model
for the swap rate, which is already an approximation, we can then apply the Black formula for
Swaptions.9 Corresponding approximation formulas may be found in [8].
19.1.5. Interpolation of Forward Rates in the LIBOR Market Model
9 Assuming lognormal processes for the forward rates, the swap rate is not a lognormal process in general.
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
259
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

CHAPTER 19. MARKET MODELS
Motivation:
An implementation of the LIBOR Market Model (e.g. as Monte-
Carlo simulation) allows us to calculate the forward rate L(T j, Tk; ti) for interest
rate periods [T j, Tk], T j < Tk and fixing times ti.10 Using these rates we can
evaluate almost all interest rate derivatives that can be represented as a function
of these rates.
The discretization of the simulation time {ti} determines at which times we may have inter-
est rates fixings. The discretization of the tenor structure {T j} determines for which periods
forward rates are available and, since the num´eraire is only defined at t = T j, it determines at
which times we may have payment dates. The tenor structure imposes a significant restriction
since a change of the tenor structure is essentially a change of the model.
In practice, it is desired to calculate as many financial products as possible with the same
model. First, the aggregation of risk measures, i.e. of sensitivities11 of products to the sen-
sitivity of a portfolio, is correct only if the product sensitivities have been calculated unsing
the same model. Second, the setup of a pricing model (calibration, generation of Monte-Carlo
paths) usually requires much more calculation time than the evaluation of a product, i.e., is is
possibly efficient to reuse a model.
Thus, it is desirable to know how to calculate from a given LIBOR market model the quan-
tities L(T s, T e; t) for T s, T e < {T0, T1, . . . , Tn} (unaligned period) and / or t < {t0, t1, . . . , tn}
(unaligned fixing).
◁|
19.1.5.1. Interpolation of the Tenor Structure {Ti}
Let us look at how to interpolate the tenor structure.
We will derive an expression for
L(T s, T e; t) for T s < {T0, T1, . . . , Tn} and/or T e < {T0, T1, . . . , Tn}. Let T s < T e.
The forward rates L(T s, T e; t) may be derived from corresponding bonds P(T; t). We have
1 + L(T s, T e; t) · (T e −T s) = P(T s; t)
P(T e; t)
For arbitrary T > t the bond P(T; t) is given by
P(T; t) = N(t) · EQN  
1
N(T)
Ft
!
.
The definition of the num´eraire of the LIBOR Market Model shows that the specification of
the short period bond P(Tm(t)+1; t) is sufficient (and necessary) to determine all bonds P(T; t)
and thus all forward rates.12
Assumption 1: No stochastic shortly before maturity.
We assume that P(Tm(t)+1; t)
is a FTm(t)-measurable random variable, i.e. the bond has no volatility at time t with Tm(t) ≤t ≤
Tm(t)+1, i.e. shortly before its maturity. With other words: t 7→P(Tm(t)+1; t) is a deterministic
interpolation functions on quantities known at the period start Tm(t). In this case for the bond
10 In a Monte-Carlo Simulation the rates carry, of course, an approximation error of the time discretization scheme.
11 A sensitivity is a partial derivative of the product price by a model- or product-parameter (e.g. volatility or strike).
12 Note that the considerations on interpolation given in this section do not assume a LIBOR Market Model. They
are valid in general.
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
260
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

19.1. LIBOR MARKET MODEL
with maturity t, seen at time s with Tm(t) ≤s ≤t ≤Tm(t)+1 we have:
P(t; s) = N(s)EQN( 1
N(t)|Fs)
= N(s)EQN(P(Tm(t)+1; t)
N(t)
·
1
P(Tm(t)+1; t)|Fs)
= N(s)EQN(P(Tm(t)+1; t)
N(t)
|Fs) ·
1
P(Tm(t)+1; t) = P(Tm(t)+1; s)
P(Tm(t)+1; t)
(19.20)
Especially for s = Tm(t)
P(t; Tm(t)) = P(Tm(t)+1; Tm(t))
P(Tm(t)+1; t)
.
(19.21)
Thus we see that (under Assumption 1), the interpolation function t 7→P(t; Tm(t)) (interpo-
lation of the maturity t) is derived directly from the interpolation function t 7→P(Tm(t)+1; t)
(interpolation of the evaluation time t) and vice versa. The functions are reciprocal.
Assumption 2: Linearity shortly before maturity.
If the chosen interpolation function
T 7→P(T; Tm(t)) is linear, then the interpolation of bond prices P(T; s) seen in s < Tm(t) is linear
too. This follows directly from the linearity of the expectation:
P(T; s) = N(s)EQN(P(T; Tm(t))
N(Tm(t)) |Fs).
(19.22)
In this way the linear interpolation takes a distinct role.
With P(Tm(t); Tm(t)) = 1
and
P(Tm(t)+1; Tm(t)) =
1
1+LTm(t)(Tm(t))·(Tm(t)+1−Tm(t))
the linear interpolation of t 7→P(t; Tm(t)) follows
as
P(t; Tm(t)) =
Tm(t)+1 −t
Tm(t)+1 −Tm(t)
P(Tm(t); Tm(t)) +
t −Tm(t)
Tm(t)+1 −Tm(t)
P(Tm(t)+1; Tm(t))
=
1 + LTm(t)(Tm(t)) · (Tm(t)+1 −t)
1 + LTm(t)(Tm(t)) · (Tm(t)+1 −Tm(t)).
(19.23)
The corresponding interpolation for the short period bond P(Tm(t)+1; t) thus with (19.21)
P(Tm(t)+1; t) :=
1
1 + LTm(t)(Tm(t)) · (Tm(t)+1 −t).
Applying (19.22) to the (in t) linear interpolation (19.23) we find for all s ≤Tm(t)
P(t; s)
P(Tm(t); s) =
1 + LTm(t)(s) · (Tm(t)+1 −t)
1 + LTm(t)(s) · (Tm(t)+1 −Tm(t)),
and thus
P(t; s)
P(Tm(t)+1; s) = 1 + LTm(t)(s) · (Tm(t)+1 −t).
From (19.20) we have for Tm(t) ≤s ≤t
P(t; s) = 1 + LTm(t)(Tm(t)) · (Tm(t)+1 −t)
1 + LTm(t)(Tm(t)) · (Tm(t)+1 −s).
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
261
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

CHAPTER 19. MARKET MODELS
We summarize this result in a theorem:
Theorem 215 (Interpolation of Forward Rates on unaligned Periods):
Given a tenor
structure T0 < T1 < T2 < . . .}. For all t let the short bond P(Tm(t)+1; t) be given by the
interpolation
P(Tm(t)+1; t) :=
1
1 + LTm(t)(Tm(t)) · (Tm(t)+1 −t).
(19.24)
Then we have for arbitrary t ≤T with k = m(t), l = m(T)
P(T; t) = P(Tk+1; t) ·
lY
j=k+1
P(T j+1)
P(T j) ·
P(T; t)
P(Tl+1; t)
=
1
1 + Lk(Tk) · (Tk+1 −t) ·
lY
j=k+1
1
1 + L j(t) · (T j+1 −T j) · (1 + Ll(t∗) · (Tl+1 −T)),
where t∗= min(t, Tl). For Ts ≤Te with Tk < Ts ≤Tk+1 and Tl ≤Te < Tl+1 we have
1 + L(Ts, Te; t) · (Te −Ts)
= P(Ts; t)
P(Te; t) =
P(Ts; t)
P(Tk+1; t) ·
lY
i=k+1
P(Ti; t)
P(Ti+1; t) · P(Tl+1; t)
P(Te; t)
= (1 + Lk(t∗) · (Tk+1 −Ts)) ·
lY
i=k+1
(1 + Li(t) · (Ti+1 −Ti)) ·
1
1 + Ll(t∗) · (Tl+1 −Te).
(19.25)
Experiment:
At http://www.christian-fries.de/finmath/
applets/LMMPricing.html several interest rate products can be priced us-
ing a LIBOR market model.
◁|
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
262
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

19.2. OBJECT ORIENTED DESIGN
19.2. Object Oriented Design
Figure 19.2 and 19.3 shows an object-oriented design of a Monte-Carlo LIBOR Market Model.
The following important aspects are considered in the design:
• Reuse of Implementation
• Separation of Product and Model
• Abstraction of Model Parameters
• Abstraction of Calibration
We will describe these aspects in the following.
getPrice(monteCarloStockProcessModel)
maturity
strike
Caplet
getBrownianIncrement(timeIndex, path, factor)
BrownianMotion
getProcessValue(timeIndex, component)
getInitialValue(component)
getDrift(timeIndex, component)
getFactorLoading(time, component, factor)
LogNormalProcess
getLIBOR(timeIndex, liborIndex)
getNumeraire(timeIndex)
«interface»
AbstractLIBORMarketModel
getPrice(AbstractLIBORMarketModel model)
maturity
Bond
getPrice(monteCarloStockProcessModel)
maturity
strike
Caplet
getPrice(AbstractLIBORMarketModel model)
maturity
strike
Caplet
getInitialValue(component)
getDrift(timeIndex, component)
getFactorLoading(time, component, factor)
SimpleLIBORMarketModel
Figure 19.2.:
UML Diagram: Evaluation of LIBOR related products in a LIBOR Market Model via
Monte-Carlo Simulation.
19.2.1. Reuse of Implementation
For the Monte-Carlo simulation of the lognormal process we use the same classes as in the
example of the Black-Scholes model, see Figure 13.4 on Page 168. To do so the classes B-
Mand LNPwere from the beginning designed for vector-valued,
i.e. multi-factorial processes, although the Black-Scholes model does not require it. Improve-
ments to the classes BMand LNPwill result in improvement of
both applications.
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
263
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

CHAPTER 19. MARKET MODELS
19.2.2. Separation of Product and Model
The interface ALIBORMMdefines how LIBOR related products communi-
cate with a Monte-Carlo LIBOR model. Through this interface the model serves to make the
process of the underlyings (the forward rates) and the num´eraire available to the product as a
Monte-Carlo simulation. All corresponding Monte-Carlo evaluations of interest rate products
expect this interface. All corresponding Monte-Carlo LIBOR models implement this interface.
This realizes a separation of product and model. The specific LIBOR Market Model is realized
through the class SLIBORMM. Model extensions may be introduced without
the need to change classes that realize LIBOR related Monte-Carlo products.
19.2.3. Abstraction of Model Parameters
getCovariance(time, component1, component2)
getFactorLoading(time, component, factor)
getFactorLoadingQuasiInverse(time, factor,component)
LIBORCovarianceModelXXX
getCovariance(time, component1, component2)
getFactorLoading(time, component, factor)
getFactorLoadingQuasiInverse(time, factor,component)
setCalibrationData(calibrationData)
LIBORCovarianceModel
getInitialValue(component)
getDrift(timeIndex, component)
getFactorLoading(time, component, factor)
SimpleLIBORMarketModel
Figure 19.3.:
UML Diagram: LIBOR Market Model: Abstraction of model parameters.
The model parameters, i.e. the covariance structure, are encapsulated in their own classes.
The model parameter classes implement a simple interface LIBORCM. A spe-
cific covariance model (i, j, t) 7→γi, j(t) = σi(t)σj(t)ρi,j(t) is realized through a class that im-
plements the interface LIBORCM. This class is then served to the model. The
interfaces are designed such that (i, j, t) 7→γi,j(t) may be stochastic.13 See Figure 19.3.
This abstraction of model parameters makes it easy to exchange different modelings of co-
variance, i.e. volatility and correlation.
Warning:
In cases where the covariance structure is modeled by volatility
and correlation it seems reasonable to define corresponding interfaces LIBOR-
VMand LIBORCM.
A simple class LIBORC-
MFVACcalculates the factor loadings and covariances
from given volatility and correlation models. See Figure 19.4. However, the separation of
volatility and correlation into their own classes will bring some disadvantages for a joint cali-
bration and general covariance modeling. The corresponding code may become over-designed.
13 A stochastic volatility model would result in a stochastic covariance model.
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
264
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

19.2. OBJECT ORIENTED DESIGN
getInitialValue(component)
getDrift(timeIndex, component)
getFactorLoading(time, component, factor)
SimpleLIBORMarketModel
getVolatility(time, component)
LIBORVolatilityModel
getVolatility(time, component)
LIBORVolatilityModelXxx
getCorrelation(time, component1, component2)
LIBORCorrelationModel
getCorrelation(time, component1, component2)
LIBORCorrelationModelXxx
getCovariance(time, component1, component2)
getFactorLoading(time, component, factor)
getFactorLoadingPsydoInverse(time, factor,component)
setCalibrationData(calibrationData)
LIBORCovarianceModel
getCovariance(time, component1, component2)
getFactorLoading(time, component, factor)
getFactorLoadingPsydoInverse(time, factor,component)
LIBORCovarianceModelFromVolatiltiyAndCorrelation
Figure 19.4.: UML Diagram: LIBOR Market Model: Abstraction of model parameters as volatility and
correlation. Introducing separate classes for volatility and correlation has some disadvantages for joint
calibration and general covariance modeling. The design above might be considered over-designed.
The design in Figure 19.4 would make sense if one whished to explore many combinations of
different volatility and correlation models.
◁|
19.2.4. Abstraction of Calibration
The abstraction of model parameters allows for the abstraction of calibration. The algorithm
calibrating the covariance model is clearly a part of the covariance model. Thus each co-
variance model object can carry calibration data (e.g. market data) that, once set, is used to
calibrate the model. The calibration data itself may be anything from given correlation and
volatility parameters to a list of products with associated target values.
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
265
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

CHAPTER 19. MARKET MODELS
getInitialValue(component)
getDrift(timeIndex, component)
getFactorLoading(time, component, factor)
SimpleLIBORMarketModel
getCovariance(time, component1, component2)
getFactorLoading(time, component, factor)
getFactorLoadingQuasiInverse(time, factor,component)
setCalibrationData(calibrationData)
LIBORCovarianceModel
getParameters()
setParameters(parameters)
LIBORCovarianceModelParametric
getCovariance(time, component1, component2)
getFactorLoading(time, component, factor)
getFactorLoadingQuasiInverse(time, factor,component)
getParameters()
setParameters(parameters)
LIBORCovarianceModelVolHumpAndCorExpDecay
Figure 19.5.:
UML Diagram: LIBOR Market Model: Abstraction of model parameters: Parametric
covariance models.
19.3. Swap Rate Market Models (Jamshidian 1997)
Motivation:
The LIBOR Market Model postulates as lognormal dynamic for
the forward rate Li := L(Ti, Ti+1). In other words, each single forward rate follows
a Black model. This allows an easy calibration of the IBOR market model to
Caplet prices. We only have to fulfill condition (19.18).
If, however, swap options (i.e. swaption or swaption related products like Bermudan swap-
tions) are in the focus, then a model that simulates the swap rate directly might be a better
choice.14 If, for example, the swap rate follows a lognormal process, then the corresponding
swaptions may be calibrated by a simple condition involving the implied Black-Volatility of
the swap rate.
◁|
Instead of a lognormal dynamic for the forward rate L(Ti, Ti+1), which is the starting point
of the LIBOR Market Model, we postulate here a lognormal dynamic of the swap rate
S i,k(t) := S (Ti, Tk; t) :=
P(Ti; t) −P(Tk; t)
Pk−1
j=i (T j+1 −T j) · P(T j+1; t)
,
k > i.
(19.26)
Since the set of swap rates defined for a given tenor structure T0 < T1 < . . . < Tn is a two
parametric family of (n−1)·n
2
rates which are related by functional dependencies, a meaningful
14 Later, we will explain why a forward rate based model might be the choice even for swap rate related products,
see Remark 217.
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
266
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

19.3. SWAP RATE MARKET MODELS (JAMSHIDIAN 1997)
dynamic can be given only for a subset of swap rates.15
When choosing a system of swap rates S i,k, for which we wish to specify the dynamics, we
have to take care that the system is neither over-determined or, with respect to the given tenor
structure, under-determined. The system of rates has to consist of n swap rates since on the
tenor structure 0 = T0 < T1 < . . . < Tn we have n degrees of freedom in terms of bond prices.
Two common variants are given by the set of co-sliding swap rates and co-terminal swap
rates, see Table 19.1. When specifying co-sliding swap rates it is necessary to close the system.
Co-Sliding:
S i,min(i+k,n)
i = 0, 1, . . . , n −1
Co-Terminal:
S i,n
i = 0, 2, . . . , n −1
Table 19.1.: co-sliding and co-terminal swap rates
Our definition achieves this by first considering the swap rates S i,i+k with k periods (co-sliding,
i < n −1 −k) and starting with i = n −k we consider co-terminal swap rates.
If the selection of swap rates is made, we model each S i,k from the selection as a lognormal
process:
dS i,k(t) = µP
i,k(t)S i,k(t)dt + σi,k(t)S i,k(t)dWP
i,k(t)
under P,
(19.27)
with initial conditions
S i,k(0) = S i,k,0.
Interpretation:
The modeling of co-terminal swap rates is a suitable choice
if, e.g., we have to price Bermudan swaptions, which have these swap rates as
underlying. The modeling of co-sliding swap rates is a suitable choice if we
have to price products relying on swap rates with constant time to maturity (CMS
rate16).
◁|
19.3.1. The Swap Measure
If we consider the Definition of the swap rate in (19.26), it is apparent that S i,k is a martingale
under the martingale measure QN corresponding to the num´eraire
N(t) := A(Ti, . . . , Tk; t) :=
k−1
X
j=i
(T j+1 −T j) · P(T j+1; t),
k > i, t ≤Ti+1.
(19.28)
The right hand side in (19.28) is a portfolio of zero bonds and thus a traded product and the
swap rate is the N-relative price of a traded product.
Definition 216 (Swap Measure, Swap Annuity):
⌝
The equivalent martingale measure QN corresponding to the num´eraire N in (19.28) is called
15 For example, the swap rate S i,i+4 is a function of the swap rates S i,i+2 and S i+2,i+4, which in turn are functional for
the swap rates S i,i+1, . . . S i+3,i+4. The swap rates with one period are forward rates Li = S i,i+1.
16 See Definition 160.
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
267
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

CHAPTER 19. MARKET MODELS
swap measure corresponding to the swap rate S (T1, . . . , Tk). The expression on the right hand
side in (19.28) is also called swap annuity.
⌟
The num´eraire is, so far, defined for t ≤Ti+1 only, since at t = Ti+1 the first bond P(Ti+1) is at
its maturity and we have to specify how its payment has to be reinvested.17 A continuation of
the num´eraire definition to t > Ti+1 can be given by a re-investment into the next swap annuity.
This is the analog to the num´eraire (19.9) of the Spot Measures. For i = 1, . . . , k −1 we have
N(t) = A(Ti, . . . , Tk; t) ·
i−1
Y
j=1
A(T j, . . . , Tk; T j+1)
A(T j+1, . . . , Tk; T j+1),
Ti−1 ≤t < Ti
where T0 := 0. The swap rates we are considering here are co-terminal. Of course we may
consider co-sliding swaps in a similar way, using the swap annuities A(T j, . . . , T j+k; t). The
corresponding num´eraire of re-investment in co-sliding swap annuities, i.e. a rolling co-sliding
swap annuity then is
N(t) = A(Ti, . . . , Ti+k; t) ·
i−1
Y
j=1
A(T j, . . . , T j+k; T j+1)
A(T j+1, . . . , T j+1+k; T j+1),
Ti−1 ≤t < Ti.
For k = i + 1 this corresponds to (19.9).
19.3.2. Derivation of the Drift Term
For the swap rate market model we have multiple sets of swap rates, which may be modeled
and (as in the LIBOR Market Model) multiple possible choices of num´eraires. This section
does not give a detailed derivation of the drift terms. The derivation is done similarly to the
derivation of the drift in the LIBOR Market Model by expressing a martingale through the
elementary swap rate processes S i, j. If for example Ak,l is the num´eraire, we consider the
QAk,l-martingale  S i,j · Ai,j
Ak,l
.
19.3.3. Calibration - Choice of the free Parameters
19.3.3.1. Choice of the Initial Conditions
Reproduction of Bond Market Prices or Swap Market Prices
If we set t to the
preset time in the definition of the swap rate (19.26), i.e. t = 0 following our convention, then
we get an equation relating today’s bond prices to today’s swap rates S i,k(0) and the latter are
just the initial conditions of the chosen swap rate processes. Thus the initial conditions of the
processes are given by (19.26) with t = 0 and today’s bond prices, i.e. today’s interest rate
curve.
Although we regard the family of zero bonds as the natural description of the interest rate
curve and we see swap rates and swap prices as derived quantities, it is in this case natural to
calculate today’s swap rates directly from today’s swap prices (assuming they are given). In
this case the initial conditions are given by today’s swap prices. With this choice, the model
will reproduce these prices.
17 The reinvestment determines the evolution of the num´eraire for t > Ti+1: For example, if we compare the
investment of the paid 1 in
1
P(Tk;Ti+1) parts of a Tk-bond with the investment in
1
P(Tk+1;Ti+1) parts of a Tk+1-
bonds, then the evolution of the num´eraire will differ by the evolution of the Tk forward rate, i.e. by the factor
P(Tk;t)
P(Tk;Ti+1)/
P(Tk+1;t)
P(Tk+1;Ti+1) =
1+L(Tk,Tk+1;t)·(Tk+1−Tk)
1+L(Tk,Tk+1;Ti+1)·(Tk+1−Tk).
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
268
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

19.3. SWAP RATE MARKET MODELS (JAMSHIDIAN 1997)
19.3.3.2. Choice of the Volatilities
Reproduction of Swaption Market Prices
The calibration of the model to swaption
prices is analog to the calibration of the LIBOR Market Model to caplet prices. Let the dynamic
of the swap rate S i,k be given by (19.27). Furthermore let σBlack,Market
i,k
denote the market prices
of an option on S i,k given as implied Black-volatility. If we calculate
σBlack,Model
i,k
:=   1
Ti
Z Ti
0
σ2
i,k(t)dt1/2,
then the model reproduces the given swaption market prices if
σBlack,Model
i,k
= σBlack,Market
i,k
.
This statement is trivial since, if we consider only a single swap rate S i,k, then (19.27) is
a Black model for this swap rate and under this model the implied volatility is defined by
inverting the pricing formula. The inversion of the pricing formula is what a calibration should
achieve.
Remark 217 (LIBOR Market Model versus Swaprate Market Model):
The question of
whether one should choose a LIBOR Market Model or a Swaprate Market Model seems to
depend on the application only, to be precise, on whether the model should calibrate to caplets
or swaptions - and whether or not one sees a lognormal forward rate or a lognormal swap rate
as realistic model.18
Therefore, the criterion that defines the choice of the model thus is the quality of the model
calibration to the specific application.
However, the swap rate market model has a disadvantage compared to the LIBOR market
model: If we calculate a forward rate Li in a swap rate market model, then the forward rate
tends to suffer from numerical instabilities. Conversely the calculation of a swap rate from
forward rates models in a LIBOR Market Model is generally much more stable.
Interpretation:
The reason lies in the representation of the swap rate as a
convex combination of the forward rates. From Lemma 123 we have
S i, j =
j−1
X
k=i
αi, j
k Lk,
with
αi,j
k ≥0
and
j−1
X
k=i
αi,j
k = 1,
with αi,j
k :=
P(Tk+1)·(Tk+1−Tk)
Pj−1
k=i P(Tk+1)·(Tk+1−Tk).
If we calculate a forward rate Li froms (e.g. co-terminal) swap rates S j,n we have
Li =
1
αi,n
i
S i,n −
1
αi+1,n
i
S i+1,n+1
=
1
αi,n
i
 S i,n −S i+1,n
 +   1
αi,n
i
−
1
αi+1,n
i
S i+1,n.
18 In general both assumptions cannot hold and it is necessary to modify the models with respect to their distribution
assumption. Such a modification of the model is called smile modeling.
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
269
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

CHAPTER 19. MARKET MODELS
Assuming for simplicity αi,n
j =
1
n−i−1, which is with Pn−1
j=i αi,n
j = 1 plausible19, then we have
S i,n =
1
n −i −1
n−1
X
k=i
Lk
Li = (n −i −1) · (S i,n −S i+1,n) + S i+1,n.
This shows:
• The calculation of a swap rate S i,n from forward rates Lk corresponds to the calculation
of an average (rate) - the swap rate can be interpreted as an integral of the forward rates.
Errors in Lk are averaged and thus smoothed. The variance of an unsystematic error is
reduced.
• The calculation of a forward rate Li from swap rates S i,n, S i+1,n consists of a finite dif-
ference term - this part of the forward rate may be interpreted as a derivative. The
calculation of a difference is very sensitive to errors in the swap rates (e.g. small jumps)
and the error is scaled up by the factor (n −i −1) for n large and i small. Thus forward
rates for short periods in a model of long period swap rates have a tendency to numerical
instability.
◁|
Tip:
If there is no strong reason for a swap rate market model, a generic LIBOR
Market Model with calculation of the corresponding swap rates from forward
rates is preferable. This provides a single, thus consistent model for multiple
applications (products), which allows the aggregation of risk parameters (Delta,
Gamma). The difference in the distributional properties is often negligible (see [8]).
◁|
Further Reading:
The original articles on the LIBOR market model are [50]
and [84]; for the swap rate market model see [77]; for the calibration of the LI-
BOR Market Model see [8, 30]; for the arbitrage-free discretization see [69]; for
the interpolation of forward rates see [90]. The evaluation of Bermudan options
in Monte-Carlo is considered in Chapter 15; see also [44, 45].
We will use the LIBOR Market model as foundation for further investigations into general
interest rate model properties. In Chapter 20 we will investigate the instantaneous correlation
ρi, j and volatility σi and their effect on terminal correlation. In Chapter 24 we will investigate
the mean reversion and multi-factoriality on the shape of interest rate curve.
◁|
19 Indeed we have
1
αi,n
i
= P(Ti+2)(Ti+2−Ti+1)
P(Ti+1)(Ti+1−Ti)
 1
αi+1,n
i
+ 1.
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
270
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

CHAPTER 20
Excursus: Instantaneous Correlation
and Terminal Correlation
In this chapter we will use the LIBOR Market Model to discuss the influence of instantaneous
volatility and instantaneous correlation on option prices. Although our study is based on the
LIBOR market model, the intuition gained from our experiments is universally valid.
We will experiment with different (extreme) parameter configurations and we will see how a
single-factor model, in which all interest rates L(Ti, Ti+1) move (instantaneously) perfectly cor-
related may, however, exhibit at time t > 0 (terminal) perfectly de-correlated random variables
L(T j, T j+1; t), L(Tk, Tk+1; t).
We will start by repeating some basic concepts:
20.1. Definitions
Definition 218 (Covariance, Correlation):
⌝
Let X, Y denote two (numeric) random variables, ¯X = E(X), ¯Y = E(Y). Then
Cov(X, Y) := E((X −¯X) · (Y −¯Y))
is called the covariance of X and Y, Var(X) := Cov(X, X) is called the variance of X and
Cor(X, Y) := E((X −¯X) · (Y −¯Y))
√Var(X) · √Var(Y)
is called the correlation of X and Y.
⌟
Let L = (L1, . . . , Ln) denote an n-dimensional m-factorial Itˆo-process of the form
dLi = µidt + σidWi,
where
dWi =
m
X
k=1
fi,kdUk
(20.1)
and Uk denote independent Brownian motions. Furthermore, let fi,k such that
R :=

ρi, j(t)

i,j=1,...,n =

m
X
k=1
fi,k fj,k

i,j=1,...,n
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
271
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

CHAPTER 20. EXCURSUS: INSTANTANEOUS CORRELATION AND TERMINAL CORRELATION
is a correlation matrix (i.e. Pm
k=1 f 2
i,k = 1). We have
< dW(t), dW(t) > = R dt.
Definition 219 (Instantaneous Covariance, Instantaneous Correlation):
⌝
With the notation above we call
ρi,j,
defined by
ρi, j(t) :=

m
X
k=1
fi,k f j,k

i, j=1,...,n
,
the instantaneous correlation of the processes Li and Lj, and we call σiσ jρi, j the instantaneous
covariance of the processes Li and Lj.
⌟
Definition 220 (Terminal Covariance, Terminal Correlation):
⌝
With the notation above we call
ρTerm
i,j
,
defined by
ρTerm
i,j
(t) := Cor(Li(t), L j(t)),
the terminal correlation of the processes Li and Lj.
Correspondingly we call t
7→
Cov(Li(t), L j(t)) the terminal covariance of the processes Li and Lj.
⌟
20.2. Terminal Correlation examined in a LIBOR
Market Model Example
We are considering a LIBOR Market Model with semi-annual tenor structure Ti := 0.5 · i and
investigating the behaviour of the two rates L10 = L(5.0, 5.5) and L11 = L(5.5, 6.0). Under the
num´eraire N = P(T12) = P(6.0) we have for the dynamic of these rates (see (19.3), (19.8))
dLi(t) = µi(t)Li(t)dt + σi(t)Li(t)dWQN
i
(t)
(i = 10, 11)
(20.2)
µ10 = −
δ11L11(t)
(1 + δ11L11(t)) · σ10(t) · σ11(t) · ρ10,11(t),
δ11 := T11 −T10
µ11 = 0.
If we neglect the drift (i.e. set µ10 = 0) and assume a constant instantaneous covariance
σ10σ11ρ10,11 = const., then it follows from (20.1) that the terminal correlation is
ρTerm
i,j
(t) = ρ10,11
∀t.
As one might have expected, the terminal correlation is given by the choice of the instantaneous
correlation. In this case, to achieve a terminal correlation different from zero we need at least
a two-factor model. Figure 20.1 shows a scatter plot for a one-factor and a five-factor model1
of the interest rates L10(t), L11(t) at time t = T10 = 5.0.
1 The exact model specification is: Li,0 = 0.1, σi = 0.1, and ρi,j = exp(−0.5|i −j|), followed by a factor reduction
as given in Section A.4. For the five-factor model we have ρ10,11 = 0.94.
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
272
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

20.2. TERMINAL CORRELATION EXAMINED IN A LIBOR MARKET MODEL EXAMPLE
 0%
 2%
 5%
 8%
 10%
 12%
 15%
 18%
 20%
LIBOR(5.5,6.0)
 0%
 5%
 10%
 15%
 20%
LIBOR(5.0,5.5)
 0%
 5%
 10%
 15%
 20%
LIBOR(5.0,5.5)
Figure 20.1.: The two (adjacent) rates L10 = L(5.0, 5.5) and L11 = L(5.5, 6.0) in a one- and a multi-
factor model for constant instantaneous volatility σ10(t) = σ11(t) = const. In a one-factor model both
random variables are perfectly correlated (left). In a five-factor model both random variables show a
correlation different from 1. This is a consequence of the instantaneous correlation ρ10,11 being different
from 1.
 0%
 2%
 5%
 8%
 10%
 12%
 15%
 18%
 20%
LIBOR(5.5,6.0)
 0%
 5%
 10%
 15%
 20%
LIBOR(5.0,5.5)
 0%
 5%
 10%
 15%
 20%
LIBOR(5.0,5.5)
Figure 20.2.: The two (adjacent) rates L10 = L(5.0, 5.5) and L11 = L(5.5, 6.0) in a one-factor model.
Left: The two random variables exhibit a correlation close to 0 (perfect de-correlation). Right: The two
random variables exhibit a very different variances. The covariance is close to zero since the variance
of L11 is close to 0. Both scenarios are the consequence of a very special choice for the instantaneous
volatility.
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
273
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

CHAPTER 20. EXCURSUS: INSTANTANEOUS CORRELATION AND TERMINAL CORRELATION
20.2.1. De-correlation in a One-Factor Model
It is possible to achieve a terminal de-correlation for processes which have perfect instanta-
neous correlation. Consider
σ10(t)

> 0
for t < 2.5,
= 0
for t ≥2.5,
σ11(t)

= 0
for t < 2.5,
> 0
for t ≥2.5,
(20.3)
i.e. the processes receive the Brownian increment dW(t) at different times t, thus the increments
received are independent. Since in this case we have µ10 = µ11 = 0 in (20.2), the two random
variables L10(5.0), L11(5.0) are given by
log(L10)(5.0) = −1
2 ¯σ2
10 · 2.5 + ¯σ10(W10(2.5) −W10(0))
log(L11)(5.0) = −1
2 ¯σ2
11 · 2.5 + ¯σ11(W11(5.0) −W11(2.5)),
where ¯σ2
10 =
1
2.5
R 2.5
0
σ2
10(t) dt and ¯σ2
11 =
1
2.5
R 5.0
2.5 σ2
11(t) dt.
Since, even for a one-factor model, the increments (W(2.5) −W(0)), (W(5) −W(2.5)) are
independent, L10(5.0), L11(5.0) are independent as well, see Figure 20.2, left.
20.2.2. Impact of the Time Structure of the Instantaneous
Volatility on Caplet and Swaption Prices
The previous example of the de-correlation of the rates L10, L11 in a one-factor model shows the
importance of the time structure of the instantaneous volatility for the (terminal) distribution
of (L10, L11) at time t = 5.0. Now we will look at the corresponding caplets and a swaption
with maturity 5.0 and payment dates 5.5, 6.0, which is dependent on L10 and L11:
Scenario
σi(t)
ρ10,11
Caplet
5.0-5.5
Caplet
5.5-6.0
Swaption
5.0-6.0
1
0.1
1.0
0.26%
0.26%
0.51%
2
0.1
0.94
0.26%
0.26%
0.50%
3
as in (20.3)
1.0
0.26%
0.26%
0.36%
4
0.7 exp(4.9(Ti −t))
1.0
0.26%
0.26%
0.27%
Table 20.1.: Caplet and swaption prices for different instantaneous correlations and volatilities.
In all scenarios we have
R Ti
0 σi(t)2 dt = 0.05 for i = 10, thus all caplet prices are the same.2
The Figures 20.1, 20.2 are generated with these parameters.
20.2.3. The Swaption Value as a Function of Forward Rates
To interpret these results we analyze the dependency of the swaption value from the rates L10,
L11.
2 We have
TiR
0
 b · exp(−c · (Ti −t))2 dt = b2
2c (1 −exp(−2 · c · Ti)). For Ti = 5.0, b = 0.7, c = 4.9 we thus have
R Ti
0
σi(t)2 dt = 0.05(1 −exp(−49)) = 0.05(1 −5 · 10−22).
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
274
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

20.2. TERMINAL CORRELATION EXAMINED IN A LIBOR MARKET MODEL EXAMPLE
For the value of a swaption VSwaption(T0) with fixed swap rate (strike) K we have
VSwaption(T0) = N(0)EQN(max(S (Ti) −K, 0) · A(Ti)
N(Ti)
| FT0)
with
A(Ti) =
n−1
X
j=i
(T j+1 −T j)P(T j+1; Ti)
(swap annuity)
S (Ti) = 1 −P(Tn; Ti)
A(Ti)
(par swap rate).
With the num´eraire N = P(Tn) we have
A(Ti)
N(Ti) =
A(Ti)
P(Tn; Ti) =
n−1
X
j=i
(T j+1 −T j)P(T j+1; Ti)
P(Tn; Ti)
=
n−1
X
j=i
(T j+1 −T j)
n−1
Y
k=j+1
(1 + Lk(Ti)(Tk+1 −Tk))
and
S (Ti) A(Ti)
N(Ti) = 1 −P(Tn; Ti)
P(Tn; Ti)
=
n−1
Y
j=i
(1 + L j(Ti)(T j+1 −T j)) −1,
i.e. it is
VSwaption(T0) =P(Tn; T0)EQP(Tn)(max((S (Ti) −K) · A(Ti)
P(Tn; Ti)
, 0) | FT0)
with
(S (Ti) −K) · A(Ti)
P(Tn; Ti)
=
n−1
Y
j=i
(1 + L j(Ti)(T j+1 −T j)) −1−
K ·
n−1
X
j=i
(T j+1 −T j)
n−1
Y
k=j+1
(1 + Lk(Ti)(Tk+1 −Tk)).
If we apply this to the special case of a swaption with a two period tenor {Ti, . . . , Tn} =
{T10, T11, T12} = {5.0, 5.5, 6.0} we get
max(S (Ti) −K · A(Ti)
P(Tn; Ti)
, 0)
= max((1 + L10∆T)(1 + L11∆T) −K(∆T(1 + L11∆T) + ∆T), 0)
= max((L10 −K)∆T + (L11 −K)∆T + L11(L10 −K)(∆T)2), 0).
(20.4)
From (20.4) we can derive the following observations for the value of the swaption:
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
275
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

CHAPTER 20. EXCURSUS: INSTANTANEOUS CORRELATION AND TERMINAL CORRELATION
• If L11(T10) = K, then the value of the swaption corresponds to the value of a caplet
paying max(L10 −K, 0). If L11 has at time T10 no or small variance and if L11(T10) is
close to K, then the value of the swaption is close to the value of a caplet with payoff
max(L10 −K, 0).
• Neglecting the term L11(T10)(L10(T10) −K)(∆T)2, which is justified for small rates and
short periods ∆T, and considering thus only
(L10(T10) −K)∆T + (L11(T10) −K)∆T
= (L10(T10) + L11(T10) −2K)∆T,
we see that the option price is determined by the variance of L10(T10) + L11(T10). For
this we have
Var(L10(T10) + L11(T10))
= Var(L10(T10)) + Var(L11(T10)) + 2 · Cov(L10(T10), L11(T10))
• From the previous we know that the option value is maximal for ρTerm
10,11(T10) = 1 and
minimal (even 0) for ρTerm
10,11(T10) = −1 (still neglecting the term L11(T10)(L10(T10) −
K)∆T 2).
From these remarks the results in table 20.1 become plausible.
In Scenario 4 the rate
L11(T10) has a negligible small variance (compare Figure 20.2, right). The swaption value
is close to the caplet value. The caplet on the period [T11, T12] however has the same price as
in the other scenarios, since the high instantaneous volatility for t ∈[T10, T11] will give the rate
L11(T11) the required (terminal) variance.
While for the swaption the rate L11(T10) is relevant, for the caplet it is the rate L11(T10).
Experiment:
The influence of the instantaneous volatility and instantaneous
correlation on terminal correlation, caplet and swaption prices may be investi-
gated at
http://www.christian-fries.de/finmath/applets/
LMMCorrelation.html.
◁|
20.3. Terminal Correlation is dependent on the
Equivalent Martingale Measure
The terminal correlation is dependent on the martingale measure and thus the num´eraire used.
The whole (terminal) probability density is of course measure dependent, see also Lemma 81 in
Chapter 5. Thus an interpretation of terminal correlation and other terminal quantities should
be made with caution.
How the chosen martingale measure influences the terminal distribution, especially the ter-
minal correlation, may easily be seen in a LIBOR Market Model. Consider the processes
Li = L(Ti, Ti+1) and Li+1 = L(Ti+1, Ti+2), i.e. two adjacent forward rates, under the martingale
measure QP(Tn) corresponding to the num´eraire P(Tn) (terminal measure). It is
d log(Li) = −
X
i< j<n
δ jLj(t)
(1 + δjL j(t)) · σi(t)σj(t)ρi, j(t)dt + 1
2σi(t)2dt + σi(t)dWQP(Tn)
i
.
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
276
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

20.3. TERMINAL CORRELATION IS DEPENDENT ON THE EQUIVALENT MARTINGALE MEASURE
With dKj(t) :=
δjL j(t)
(1+δjLj(t))dt we thus have
d log(Li) = σi ·

−σi+1ρi,i+1dKi+1 −
P
i+1<j<n
σjρi+1, jdKj + 1
2σi(t)dt + dWQP(Tn)
i

d log(Li+1) = σi+1 ·

−
P
i+1<j<n
σjρi+1, jdKj + 1
2σi+1dt + dWQP(Tn)
i+1

.
The terminal correlation is influenced by the common drift term P
i+1<j<n dK j and this influence
can be increased arbitrarily through the factor σj in front of Kj. If and how this term is present
depends on the chosen martingale measure: For n = i + 2 the sum is empty and the term is
= 0, for n > i + 2 the term is > 0. In theory it might be possible that Li and Li+1 appear almost
perfectly correlated under QP(Ti+3) and perfectly uncorrelated under QP(Ti+2).
20.3.1. Dependence of the Terminal Density on the Martingale
Measure
How the chosen martingale measure influences the terminal distribution function is shown in
the following examples. In Figure 20.3 we look at the density of a forward rate under a one-
factor LIBOR Market model with constant instantaneous volatility, equal for all rates. Under
different martingale measures (spot measure, terminal measure) the distribution is slightly dif-
ferent. If, however, the volatility of the other rates is increased, then, depending on the chosen
martingale measure, the distribution will change, see Figure 20.4. As before, the change in
the distribution function stems from the drift of the LIBOR Market Model.
Terminal distribution of L(5.0,5.5) seen at t=5.0 (fixing)
Terminal measure T=20.0
Terminal measure T=10.0
Terminal measure T=5.5
Spot measure
- 4,0
- 3,5
- 3,0
- 2,5
- 2,0
- 1,5
- 1,0
- 0,5
 0,0
Log of Forward Rate
 0,0%
 0,5%
 1,0%
 1,5%
 2,0%
 2,5%
 3,0%
Frequency
Figure 20.3.: The terminal distribution function of a forward rate under different martingale measures.
Shown is the rate L(5.0, 5.5) upon its fixing at t = 5.0. All rates are simulated in a one-factor LIBOR
market model with constant instantaneous volatility σ = 10%.
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
277
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

CHAPTER 20. EXCURSUS: INSTANTANEOUS CORRELATION AND TERMINAL CORRELATION
Terminal distribution of L(5.0,5.5) seen at t=5.0 (fixing)
Terminal measure T=20.0
Terminal measure T=10.0
Terminal measure T=5.5
Spot measure
- 4,0
- 3,5
- 3,0
- 2,5
- 2,0
- 1,5
- 1,0
- 0,5
 0,0
Log of Forward Rate
 0,0%
 0,5%
 1,0%
 1,5%
 2,0%
 2,5%
 3,0%
Frequency
Figure 20.4.: The terminal distribution function of a forward rate under different martingale measures.
Shown is the rate L(5.0, 5.5) upon its the at fixing t = 5.0. In contrast to Figure 20.3 the rates L(Ti, Ti+1)
for Ti < 5.0 are simulated differently. They are simulated with a high volatility of 150%. All other rates
are simulated as in Figure 20.3 with volatility σ = 10%. The change of the simulation of the other rates
has an significant impact on the distribution of L(5.0, 5.5) under the spot measure.
Tip (Terminal Quantities Independent of the Martingale Measure):
In
place of martingale measure dependent quantities, like the terminal distribution
of the terminal correlation, we can define meaningful alternatives. The implied
(Black-)volatility is an example of a martingale measure independent quantity.
Apart from the scaling with the square root of the maturity √Tk it corresponds to the terminal
standard deviation under the Tk+1-forward measure. If, for example,
d log(Li(t)) = (. . .)dt + σi(t)dWi(t)
d log(L j(t)) = (. . .)dt + σ j(t)dWj(t)
are given processes, then the integrated instantaneous covariance
Z T
0
d log(Li(t))d log(Lj(t)) =
Z T
0
σi(t)σj(t)ρi,j(t)dt
is independent of the chosen martingale measure.3 It would correspond to the covariance of
log(Li(t)) and log(Lj(t)), if both were martingales.
◁|
3 This is clear, because a change of martingale measure is a change of drift only.
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
278
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

CHAPTER 21
Heath-Jarrow-Morton Framework:
Foundations
The Heath-Jarrow-Morton Framework [74] postulates an Itˆo process as a model for the instan-
taneous forward rate1:
d f(t, T) = αP(t, T)dt + σ(t, T) · dWP(t)
f(0, T) = f0(T)
(21.1)
for 0 ≤t < T, where WP = (WP
1 , . . . , WP
m) is an m-dimensional P-Brownian motion
with instantaneously uncorrelated components.2
Furthermore we assume that σ(t, T) =
(σ1(t, T), . . . , σm(t, T)) and αP(t, T) are adapted processes.
In case of its existence, let Q denote the risk-neutral measure, i.e. the martingale measure
Q = QB corresponding to the num´eraire B with
B(t) := exp
 Z t
0
f(τ, τ)dτ

= exp
 Z t
0
r(τ)dτ

,
(21.2)
where r denotes the short rate - see Definition 103.
Girsanov’s Theorem (Theorem 58), gives the process (21.1) under Q as
df(t, T) = αQ(t, T)dt + σ(t, T) · dWQ(t)
f(0, T) = f0(T).
(21.3)
Equation (21.3) represents a family of stochastic processes parametrized by T, which give
a complete description of the interest rate curve: From Definition (101) we have f(t, T) =
−∂log(P(T;t))
∂T
, i.e.
P(T; t) = exp   −
Z T
0
f(t, τ)dτ.
Apart from the requirement that the processes are Itˆo processes, we do not consider a specific
model or its implementation. A specific model would be given, if we had specified the form
of (t, T) 7→σ(t, T). With a specific choice of σ(t, T) (21.3) may become a known short rate
model or the LIBOR market model, see Chapter 23.
In this chapter we will discuss the no-arbitrage conditions of (21.3) and discuss how other
models fit into this framework.
1 Definition 101 on Page 118.
2 I.e. that dWT · dW = Idt, see Section 2.7.
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
279
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

CHAPTER 21. HEATH-JARROW-MORTON FRAMEWORK: FOUNDATIONS
21.1. Short Rate Process in the HJM Framework
The specification of the families of processes f(·, T) implies a process for the short rate r. We
write Equation (21.3) in integral form3
f(t, T) = f0(T) +
Z t
0
α(s, T)ds +
Z t
0
σ(s, T) · dW(s).
(21.4)
With T →t we find for the short rate r(t) := lim
T↘t f(t, T) that
r(t) = f(t, t) = f0(t) +
Z t
0
α(s, t)ds +
Z t
0
σ(s, t) · dW(s)
(21.5)
and thus the short rate process is in differential notation given as
dr(t) =

∂f0
∂T (t) + α(t, t) +
t
Z
0
∂α
∂T (s, t)ds +
t
Z
0
∂σ
∂T (s, t) · dW(s)
dt
+σ(t, t)·dW(t).
(21.6)
Remark 221 (Notation):
Equation (21.6) follows from (21.5) by differentiating with respect
to t. Since t enters into the second argument of α and σ, we have to calculate the partial
derivative of α and σ with respect to their second argument. In accordance with the notation
in (21.1) we denote the partial derivative of α with respect to its second argument by ∂α
∂T and
the partial derivative of σ with respect to its second argument by ∂σ
∂T . Likewise we denote the
(partial) derivative of f0 with respect to its argument by ∂f0
∂T .
21.2. The HJM Drift Condition
Theorem 222 (Heath, Jarrow, Morton - HJM Drift Condition):
For the family of bond
price processes P(T) the following holds: The B-relative price P(T)
B
is a QB-martingale, if and
only if
Z T
s
α(s, S )dS = 1
2
Z T
s
σ(s, S )dS ·
Z T
s
σ(s, S )dS .
From this we have: All bond price processes of the bond curve T 7→P(T) are QB-martingales,
i.e. the model is arbitrage-free, if and only if
αQB(t, T) = σ(t, T) ·
Z T
t
σ(t, τ) dτ
∀T.
(21.7)
Equation (21.7) is called the HJM drift condition.
3 We are dropping the superscript QB on the drift α and the diffusion W for a while.
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
280
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

21.2. THE HJM DRIFT CONDITION
Proof (of the HJM drift condition):
Let T denote a fixed maturity.
With B(t) =
exp(
R t
0 r(s)ds) and P(T; t) = exp(−
R T
t
f(t, S )dS ) it follows for the B-relative price of the bond
P(T) that:
P(T; t)
B(t)
= exp(X(t))
with
X(t) = −
Z T
t
f(t, S ) dS −
Z t
0
r(s)ds.
From (21.4) and (21.5) follows
X(t) = −
Z T
t
f(t, S ) dS −
Z t
0
r(s)ds
= −
Z T
t
f0(S )dS −
Z T
t
Z t
0
α(s, S )dsdS −
Z T
t
Z t
0
σ(s, S )dW(s)dS
−
Z t
0
f0(S )dS −
Z t
0
Z u
0
α(s, u)dsdu −
Z t
0
Z u
0
σ(s, u)dW(s)du.
With
R t
0
R u
0 dW(s)du =
R t
0
R t
s dudW(s) and the interchange of the integrals this is
= −
Z T
t
f0(S )dS −
Z t
0
Z T
t
α(s, S )dS ds −
Z t
0
Z T
t
σ(s, S )dS dW(s)
−
Z t
0
f0(S )dS −
Z t
0
Z t
s
α(s, u)duds −
Z t
0
Z t
s
σ(s, u)dudW(s)
= −
Z T
0
f0(S )dS −
Z t
0
Z T
s
α(s, S )dS ds −
Z t
0
Z T
s
σ(s, S )dS dW(s)
=X(0) +
Z t
0
A(s)ds +
Z t
0
Σ(s)dW(s),
thus
dX(t) = A(t)dt + Σ(t)dW(t),
where
X(0) = −
Z T
0
f0(S )dS
A(s) = −
Z T
s
α(s, S )dS
Σ(s) = −
Z T
s
σ(s, S )dS .
Let the B-relative price of P(T) be a martingale under QB, i.e. the process exp(X(t)) is drift-
free. From Itˆo’s Lemma we have d exp(X(t)) = X(t)dX(t) + 1
2X(t)dX(t)dX(t), i.e.
d exp(X(t)) = X(t) ·  (A(s) + 1
2Σ(s)Σ(s))dt + Σ(t)dW(t).
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
281
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

CHAPTER 21. HEATH-JARROW-MORTON FRAMEWORK: FOUNDATIONS
That exp(X(t)) is drift-free thus implies A(s) + 1
2Σ(s)Σ(s) = 0, i.e.
Z T
s
α(s, S )dS = 1
2
Z T
s
σ(s, S )dS ·
Z T
s
σ(s, S )dS .
If this equation is valid for all T, we get by differentiation
∂
∂T the HJM drift condition
α(t, T) = σ(t, T) ·
Z T
t
σ(t, S )dS .
□|
Interpretation (Bond Volatility):
The expression Σ(t) = −
R T
t σ(t, S )dS
corresponds to the volatility of the bond price process P(T) at time t (bond volatil-
ity), since we have
dP(T; t) = d B(t) exp(X(t)) = B(t)d exp  X(t)
= B(t) exp  X(t) ·  dX(t) + 1
2dX(t) · dX(t)
= P(T; t) ·  (. . .)dt + Σ(t) · dW(t))
= P(T; t) · (. . .)dt + P(T; t) · Σ(t) · dW(t).
◁|
Motivation
(Embedding other Models):
If an interest rate model is
arbitrage-free and if the processes of the instantaneous forward rates f(·, T) are
Itˆo processes, then the model has to fulfill the HJM drift condition (21.7). Thus,
these interest rate models may be derived as a special case of the HJM framework.
Since the volatility structure (t, T) 7→σ(t, T) and the initial conditions f(0, T) are the only free
parameters of the HJM framework, this embedding of arbitrage-free interest rate models can
be achieved by choosing the HJM volatility structure and the initial interest rate curve. We will
show in Chapter 23 how short rate models and the LIBOR market model can be interpreted as
special HJM volatility structures.
◁|
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
282
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

CHAPTER 22
Short Rate Models
22.1. Introduction
At a fixed point t in time the short rate is given by
r(t) := −∂P(T; t)
∂T
T=t,
see Definition 103. Thus r : t 7→r(t) is a real valued stochastic process. We make the following
assumptions:
1. Given is a model for r (short rate model), e.g. in the form of an Itˆo process
dr = µP(t, r)dt + σ(t, r)dWP(t),
r(0) = r0,
(22.1)
where P denote the real probability measure.
2. The continuously compounding money market account B(t) ,
dB(t) = r(t)B(t)dt,
B(0) = 1,
d.h
B(t) = exp   Z t
0
r(τ)dτ,
is a traded asset.1
3. Corresponding to the num´eraire N(t) = B(t) there exists a martingale measure Q = QB
equivalent to P.
From the Girsanov’s Theorem2 the process of r under Q is
dr = µQ(t, r)dt + σ(t, r)dWQ(t),
r(0) = r0.
(22.2)
with µQ(t, r) = µP(t, r) + C(t). Since under Q all B-relative prices of traded assets are martin-
gales, all bond prices are given by
P(T; t) = B(t)EQ 1
B(T) | Ft
 = EQ  exp(−
Z T
t
r(τ)dτ) | Ft
.
1 The short rate r is, as an interest rate for an infinitesimal period dt, an idealized quantity. Correspondingly the
product B is an idealized quantity: The continuous re-investment of an initial value of 1 over infinitesimal periods
[t, t + dt] with rate r(t).
2 Theorem 58 on page 45.
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
283
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

CHAPTER 22. SHORT RATE MODELS
From the bond prices P(T; t) we can calculate all derived quantities such as forward rates or
swap rates, see Section 8.2. Thus, the short rate model (22.2) gives a complete description of
the interest rate curve dynamic.
Short rate models were and are popular, since the underlying stochastic process r is one-
dimensional (i.e. scalar valued). Thus many techniques that are known from the modeling of
(also one-dimensional) stock price processes can be used (e.g. finite difference implementa-
tions). Depending on the specific model (i.e. the form of µQ and σ), analytic formulas for bond
prices or simple European interest rate options may be derived, similar to the Black-Scholes
formula for European stock options under a Black-Scholes model.
Instead of specifying the model (22.1) of the short rate process under the real measure P
and applying the measure transformation to Q, is is usual to specify the model (22.2) directly
under Q and calibrate given model parameters.
22.2. The Market Price of Risk
Consider a bond with maturity T. Under a short rate model its price price process P(T) : t 7→
P(T; t) is a function of (t, r(t)) and if Itˆo’s Lemma is applicable we have3
dP(T) = αP
T(t, r)P(T)dt + σT(t, r)P(T)dWP(t),
(22.3)
where the price process is considered under the real measure P.
Let P(T1) and P(T2) denote two bonds with different maturities T1 , T2. We construct a
portfolio process (φ0, φ1) for a self-financing portfolio of B and P(T1), which replicates P(T2).
The portfolio process (φ0, φ1) has to satisfy the following equations:
φ0B + φ1P(T1) = P(T2)
(“replicating”)
(22.4)
d φ0B + φ1P(T1) = φ0dB + φ1dP(T1)
(“self-financing”).
(22.5)
From (22.4) we find dP(T2) = d(φ0B + φ1P(T1)) and with
d φ0B + φ1P(T1) (22.5)
=
(φ0rB + φ1αP
T1P(T1))dt + φ1σT1P(T1)dWP(t)
dP(T2)
(22.3)
=
αP
T2P(T2)dt + σT2P(T2)dWP(t).
we have, by comparing coefficients,
αP
T2P(T2) = φ0rB + φ1αP
T1P(T1)
(22.6)
σT2P(T2) = φ1σT1P(T1).
(22.7)
While (22.7) and (22.4) uniquely determine the portfolio process (φ0, φ1), (22.6) is a con-
sistency condition for r, αT1 and αT2. If (22.6) were violated, then the model would not be
3 At this point, it is not obvious that Itˆo’s Lemma is applicable, especially if the functional dependence of P(T; t)
from r(t) is sufficiently smooth. However, for the short rate models presented this is the case. From Itˆo’s Lemma
we then have αT =
∂
∂t P(T)+µ ∂
∂r P(T)+ 1
2 σ2 ∂2
∂r2 P(T)
P(T)
and σT =
σ ∂
∂r P(T)
P(T)
= σ ∂
∂r log(P(T)).
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
284
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

22.3. OVERVIEW: SOME COMMON MODELS
arbitrage-free. We rewrite the consistency condition (22.6) as:
⇔
αP
T2 · P(T2) = φ0 · r · B + φ1 · αP
T1 · P(T1)
⇔
αP
T2 · P(T2) = φ0 · r · B + φ1 · r · P(T1) + φ1 · (αP
T1 −r) · P(T1)
(22.4)
⇔
αP
T2 · P(T2) = r · P(T2) + φ1 · (αP
T1 −r) · P(T1)
⇔
(αP
T2 −r) · P(T2) = φ1 · (αP
T1 −r) · P(T1)
(22.7)
⇔
αP
T2 −r
σT2
=
αP
T1 −r
σT1
.
It follows that there exists a λP, such that for all bond price processes
dP(T) = αP
T(t, r) · P(T) · dt + σT(t, r) · P(T) · dWP(t)
we have
αP
T −r
σT
=: λP.
Since αP is the local rate of return of the bond, we may interpret λP as the local excess return
rate over r per risk unit σT.
Definition 223 (Market Price of Risk):
⌝
The quantity λP :=
αP
T −r
σT , which is independent of T, is called the Market Price of Risk.
⌟
If we consider the bond price process
dP(T) = αQ
T (t)P(T)dt + σT(t)P(T)dWQ(t)
under the measure Q, it is obvious that αQ
T = r for all T, since all B-relative prices are Q-
martingales. Thus, under Q the Price of Risk λQ = 0. It follows that
µQ
T = λQ · σT + r = 0 + r = λP · σT + r −λP · σT = µP
T −λP · σT,
and we find that Market Price of Risk λP appears in the change of drift to the measure Q, i.e. we
have C(t) = −λP · σT in Theorem 58.
Definition 224 (Risk Neutral Measure):
⌝
Let r(t) denote the short rate. The martingale measure QB corresponding to the num´eraire
B(t) = exp   R t
0 r(τ)dτ is called the risk-neutral measure.
⌟
Remark 225 (Risk Neutral Measure):
The continuously compounding money market ac-
count B is locally risk free, since the process dB(t) = r(t)B(t)dt does not exhibit a dW(t) term.
However, r(t) may be stochastic. If r were not stochastic, then B would be globally risk free.
22.3. Overview: Some Common Models
Table 22.3 gives a selection of the most common short rate models.
The Hull-White model is sometimes called extended Vasicek model. The Vasicek, Hull-
White and Ho-Lee models allow for negative short rates. The Black-Derman-Toy (BDT) and
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
285
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

CHAPTER 22. SHORT RATE MODELS
Name
Model
Vasicek Model
dr = (b −ar)dt + σdWQ
Hull-White Model
dr = (φ(t) −ar)dt + σ(t)dWQ
Ho-Lee Model
dr = a(t)dt + σ(t)dWQ
Dothan Model
dr = ardt + σrdWQ
Black-Derman-Toy Model
d ln(r) = φ(t)dt + σ(t)dWQ
Black-Karasinski Model
d ln(r) = (φ(t) −a ln(r))dt + σ(t)dWQ
Cox-Ingersoll-Ross Model
dr = (b −ar)dt + σ(t) √rdWQ
Table 22.1.: Selection of Short Rate Models
Black-Karansinski (BK) models use a lognormal process and the Cox-Ingersoll-Ross model
uses a square-root process. Neither of these two processes allow for negative rates.4
22.4. Implementations
22.4.1. Monte-Carlo Implementation of Short-Rate Models
A short-rate model gives a description of the dynamic of the short rate. To obtain a complete
interest rate curve at a given simulation time t, we have to calculate the bond prices from (22.1)
as conditional expectation. To calculate a conditional expectation in a Monte-Carlo simulation
numerically requires additional, numerically expensive methods, see Chapter 15. To obtain a
Monte-Carlo simulation of the full interest rate curve from a Monte-Carlo simulation of the
short rate, analytic formulas for bond-prices are indispensable. The popularity of short rate
models is thus partly due to the need for a simple and efficient implementation.
For a fast calibration to a given interest rate curve it is also required to calculate bond prices
analytically.
22.4.2. Lattice Implementation of Short-Rate Models
If the short rate model is Markovsch in low dimensions, then it is best to implement the short
rate model on a lattice, allowing for a backward algorithm.5 Depending on the model, imple-
mentations using binomial or trinomial trees or general finite differences for pde’s are used.
See [35] for a detailed discussion.
Further Reading:
Bj¨org’s book [7] contains a discussion of short rate model
with affine term structure. Tavella and Randal’s book [35] gives an introduction
to finite difference methods, also with applications to interest rate models.
◁|
4 This result holds for the time-continuous process. A time-discretization of the process may allow for negative
rates. See for example Section 13.1.2.
5 See Section 13.3.2.
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
286
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

CHAPTER 23
Heath-Jarrow-Morton Framework:
Immersion of Short Rate Models and
LIBOR Market Model
You’re going to find that many of the truths we cling to
depend greatly on our own point of view.
Obi-Wan Kenobi / George Lucas
Star Wars: Episode VI, (Wikiquote).
23.1. Short Rate Models in the HJM Framework
The Heath-Jarrow-Morton framework
d f(t, T) = α(t, T)dt + σ(t, T)dW(t)
f(0, T) = f0(T)
(was 21.3)
implies the short rate process
dr(t) =

∂f0
∂T (t) + α(t, t) +
t
Z
0
∂α
∂T (s, t)ds +
t
Z
0
∂σ
∂T (s, t)dW(s)
dt
+σ(t, t)dW(t),
(was 21.6)
both under the measure QB - see (21.3), (21.4), (21.5), (21.6) on Page 280. The short rate
model is thus given by the specific choice of the HJM volatility structure σ(t, t) (→short rate
volatility) and initial conditions f0 (→short rate drift).
23.1.1. Example: The Ho-Lee Model in the HJM Framework
Consider the simple case of a constant volatility function
σ(t, T) = σ = const.
From (21.7) we have α(t, T) = σ ·
R T
t σ dτ = σ2 · (T −t), i.e.
d f(t, T) = σ2 · (T −t)dt + σdW(t),
f(0, T) = f0(T).
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
287
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

CHAPTER 23. HEATH-JARROW-MORTON FRAMEWORK: IMMERSION OF SHORT RATE MODELS AND LIBOR MARKET MODEL
For the short rate it follows that
r(t) = f(t, t) = f0(t) +
Z t
0
σ2 · (T −s)ds
T=t
+
Z t
0
σdW(s)
= f0(t) + 1
2σ2t2 + σW(t),
i.e.
dr(t) =
df0
dT (t) + σ2t

dt + σdW(t).
Using the notation from the Ho-Lee model, dr(t) = φ(t)dt + σdW(t), it is
φ(t) = d f0
dT (t) + σ2t.
Interpretation:
The Equation (23.1.1) allows a calibration of the Ho-Lee
model to a given curve of bond prices P(T) by setting φ(t) = −d2 log(P(T))
dT 2
(t) + σ2t.
With this choice the model reproduces the given bond prices.
If we consider the interest rate curve fT1(T) := f(T1, T1 + T), T ≥0 at a later
time T1 > 0, then from
d fT1
dT (t) + σ2t = φ(T1 + t) = df0
dT (T1 + t) + σ2(T1 + t),
we find that fT1(t) = fT1(0) + f0(T1 + t) −f0(t) + σ2(T1 · t + 1
2t2).
So to summarize, the model reproduces all bond prices, but in the evolution the interest rate
curve gets steeper and steeper - a rather unrealistic behavior.
◁|
23.1.2. Example: The Hull-White Model in the HJM Framework
Consider the case of an exponentially volatility function
σ(t, T) = σ · e−a·(T−t),
(a > 0).
Then we have ∂σ
∂T (t, T) = −a · σ · e−a·(T−t) = −aσ(t, T).
For the drift µ(t) of the short rate
process dr(t) = µ(t)dt + σ(t, t)dW(t) we get
µ(t)
(21.6)
=
∂f0
∂T (t) + α(t, t) +
Z t
0
∂α
∂T (s, t)ds +
Z t
0
∂σ
∂T (s, t)dW(s)
=
∂f0
∂T (t) + α(t, t) +
Z t
0
∂α
∂T (s, t)ds −
Z t
0
a · σ(s, t)dW(s)
(21.5)
=
∂f0
∂T (t) + α(t, t) +
Z t
0
∂α
∂T (s, t)ds −a · r(t) + a · f0(t) +
Z t
0
aα(s, t)ds,
i.e.
dr(t) = (φ(t) −ar(t)) dt + σdW(t)
with
φ(t) = ∂f0
∂T (t) + a · f0(t) + α(t, t) +
Z t
0
∂α
∂T (s, t)ds +
Z t
0
a · α(s, t)ds.
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
288
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

23.2. LIBOR MARKET MODEL IN THE HJM FRAMEWORK
With the HJM drift condition (21.7) it follows that α(t, T) = σ2 · e−a·(T−t) · 1
a
 1 −e−a·(T−t) =
σ2 · 1
a
 e−a·(T−t) −e−2a·(T−t) and thus
φ(t) = ∂f0
∂T (t) + a · f0(t) + α(t, t) +
Z t
0
∂α
∂T (s, t)ds +
Z t
0
a · α(s, t)ds
= ∂f0
∂T (t) + a · f0(t) +
Z t
0
σ2e−2a·(t−s)ds
= ∂f0
∂T (t) + a · f0(t) + σ2
2a
 1 −e−2a·t.
Altogether we have
dr(t) =
 ∂f0
∂T (t) + a · f0(t) + σ2
2a
 1 −e−2a·t −ar(t)
!
dt + σdW(t).
Note that this equation allows a calibration of the Hull-White model to a given curve of bond
prices. From the bond price curve we can calculate ∂f0
∂T (t) + a · f0(t).
Interpretation (Mean Reversion):
The derivation of a Hull-White model
from a Heath-Jarrow-Morton model gives an important insight to the relevance
of the timer structure of the volatility function:
A volatility function of the instantaneous forward rate f(t, T), which is exponentially
decaying in (T −t) (time to maturity), i.e. σ(t, T) = exp(−a(T −t)), corresponds to a
mean reversion term for the short rate process r(t) with mean reversion speed a.
Correspondingly, this effect is visible in the LIBOR Market Model, see Chapter 24.
◁|
23.2. LIBOR Market Model in the HJM Framework
23.2.1. HJM Volatility Structure of the LIBOR Market Model
In the specification (19.1) of the LIBOR Market Model dW denoted the increment of a n-
dimensional Brownian motion with instantaneous correlation R. In the specification (21.3) of
the HJM Framework dW denoted the increment of a m-dimensional Brownian motion with
instantaneous uncorrelated components. To resolve this conflict we employ the notation of
Section 2.7: Let U denote an m-dimensional Brownian motion with instantaneous uncorrelated
components and W denote an n-dimensional Brownian motion with dW(t) = F(t) · dU(t),
i.e. the instantaneous correlation of W is R := FFT. Consider the HJM model
d f(t, T) = αQ(t, T)dt + σ(t, T)dUQ(t)
f(0, T) = f0(T)
(23.1)
with dU = (dU1, . . . , dUm). From
P(T; t) = exp   −
Z T
t
f(t, τ)dτ.
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
289
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

CHAPTER 23. HEATH-JARROW-MORTON FRAMEWORK: IMMERSION OF SHORT RATE MODELS AND LIBOR MARKET MODEL
(see Remark 102) it follows that the forward Rate Li(t) := L(Ti, Ti+1; t) is given by
1 + Li(t) · ∆Ti =
P(Ti; t)
P(Ti+1; t) = exp   Z Ti+1
Ti
f(t, τ)dτ.
Note that for X(t) :=
R Ti+1
Ti
f(t, τ)dτ we have by the linearity of the integral that dX =
R Ti+1
Ti
d f(t, τ)dτ, thus we find from Itˆo’s Lemma that within the HJM framework the process
of the forward rate Li(t) is
dLi(t) · ∆Ti = d exp(X) = exp(X) ·  dX + 1
2dX · dX
= exp   Z Ti+1
Ti
f(t, τ)dτ ·
"Z Ti+1
Ti
(d f(t, τ))dτ
+1
2
Z Ti+1
Ti
(df(t, τ))dτ ·
Z Ti+1
Ti
(df(t, τ))dτ
#
= (1 + Li(t) · ∆Ti) ·
h
(A(t) + 1
2Σ(t) · Σ(t))dt + Σ · dUQi
where A(t) =
R Ti+1
Ti
αQ(t, τ)dτ und Σ(t) =
R Ti+1
Ti
σ(t, τ)dτ.
dLi(t) = 1 + Li(t) · ∆Ti
∆Ti
·

(A(t) + 1
2Σ(t) · Σ(t))dt +
Z Ti+1
Ti
σ(t, τ)dτdUQ(t)

(23.2)
We will now choose the volatility structure such that (23.2) corresponds to the process of a
LIBOR market model: Let W = (W1, . . . , Wn) denote an n-dimensional Brownian motion as
given in Section 2.7.
dW(t) = F(t) · dU(t),
with correlation matrix R := FFT,
i.e.
dWi(t) = Fi(t) · dU(t),
with F =

F1
...
Fn

.
Let the volatility structure be chosen as
σ(t, τ) =

Li(t)
1+Li(t)∆Ti σi(t) · Fi(t)
for t ≤Ti
(0, . . . , 0)
for t > Ti,
(23.3)
where i is such that τ ∈[Ti, Ti+1). Then we have
1 + Li(t) · ∆Ti
∆Ti
·
Z Ti+1
Ti
σ(t, τ)dτdU =

Li(t)σi(t)dW(t)
for t ≤Ti,
0
for t > Ti,
The forward rate then follows the process
dLi = µQB
i (t)Li(t)dt + σi(t)Li(t)dWi(t),
where
µQB
i
= 1 + Li(t) · ∆Ti
Li(t)∆Ti
·  Ti+1
Z
Ti
αQ(t, τ)dτ + 1
2
Ti+1
Z
Ti
σ(t, τ)dτ ·
Ti+1
Z
Ti
σ(t, τ)dτ.
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
290
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

23.2. LIBOR MARKET MODEL IN THE HJM FRAMEWORK
Interpretation (LIBOR Market Model as HJM Framework with discrete
Tenor Structure):
Apart from the factor
Li(t)
1+Li(t)∆Ti , (23.3) gives the volatility
structure σ(t, T) of f(t, T) as piecewise constant in T. The factor Li(t) results from
the requirement to have a lognormal process for Li. The factor
1
1+Li(t)∆Ti results
from the discretization of the tenor structure. This shows that the LIBOR Market Model can
be interpreted as HJM framework with discrete tenor structure. In the limit ∆Ti →0 the factor
1
1+Li(t)∆Ti vanishes and we obtain (apart from the restriction to a lognormal model) the HJM
framework.
◁|
23.2.2. LIBOR Market Model Drift under the QB Measure
The HJM drift condition states that
αQB(t, T) = σ(t, T) ·
Z T
t
σ(t, τ)dτ.
Since for fixed t σ(t, T) is a piecewise constant function in T - namely constant on [Ti, Ti+1) -,
we have for T ∈[Ti, Ti+1)
αQB(t, T) = σ(t, Ti) ·   σ(t, t)(Tm(t)+1 −t)
|                {z                }
=0
+
i−1
X
j=m(t)+1
σ(t, T j)∆T j + σ(t, Ti)(T −Ti)
where m(t) := max{i : Ti ≤t}. Thus we have
Z Ti+1
Ti
αQB(t, τ)dτ = σ(t, Ti)∆Ti ·  i−1
X
j=m(t)+1
σ(t, T j)∆T j + 1
2σ(t, Ti)∆Ti
.
With σ(t, Ti) · σ(t, T j) =
σiLi
1+Li∆Ti
σjL j
1+L j∆T j ρi,j we find
µQB
i
= 1 + Li(t) · ∆Ti
Li(t)∆Ti
·

Ti+1
Z
Ti
αQB(t, τ)dτ + 1
2
Ti+1
Z
Ti
σ(t, τ)dτ ·
Ti+1
Z
Ti
σ(t, τ)dτ

= 1 + Li(t) · ∆Ti
Li(t)∆Ti
· σiLi∆Ti
1 + Li∆Ti
·  i−1
X
j=m(t)+1
σ jLj∆T j
1 + Lj∆T j
ρi,j + σiLi∆Ti
1 + Li∆Ti

= 1 + Li(t) · ∆Ti
Li(t)∆Ti
· σiLi∆Ti
1 + Li∆Ti
·  iX
j=m(t)+1
σ jLj∆T j
1 + Lj∆T j
ρi,j

= σi ·  iX
j=m(t)+1
σ jLj∆T j
1 + L j∆T j
ρi, j
.
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
291
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

CHAPTER 23. HEATH-JARROW-MORTON FRAMEWORK: IMMERSION OF SHORT RATE MODELS AND LIBOR MARKET MODEL
Interpretation:
Surprisingly, we find that the drift under QB is identical to the
drift under the spot LIBOR measure (see Section 19.1.1.2))
N(t) = P(Tm(t)+1; t)
m(t)
Y
j=0
(1 + L j(T j) · ∆T j),
(Spot LIBOR Measure, s. 19.9)
The reason is simple: Under the assumed volatility structure the num´eraires B(t) and N(t) are
identical. To be precise, it is the assumption
σ(t, T) = 0
for Tm(t) ≤t ≤T < Tm(t)+1
(23.4)
which implies that the two num´eraires coincide. By this the HJM drift implies
αQB(t, T) = 0
for Tm(t) ≤t ≤T < Tm(t)+1
and thus for Tm(t) ≤T < Tm(t)+1:
f(t, T) = f(Tm(t), T) +
Z t
Ti
αQB(τ, T)dτ
|             {z             }
=0
+
Z t
Ti
σ(τ, T)dWQB(τ)
|                   {z                   }
=0
.
From f(t, T) = f(Tm(t), T) we have
B(t)
B(Tm(t)) = exp   Z t
Tm(t)
f(τ, τ)dτ = exp   Z t
Tm(t)
f(Ti, τ)dτ
=
P(Tm(t)+1; t)
P(Tm(t)+1; Tm(t)) =
N(t)
N(Tm(t)),
with B(0) = N(0) = 1 i.e. B(t) = N(t).
◁|
We will summarize this result as a theorem:
Theorem 226 (Equivalence of the risk-neutral measure and the spot LIBOR measure):
Given a tenor structure 0 = T0 < T1 < . . . < Tn. Under the assumption the Ti+1-bond P(Ti+1; t)
has volatility 0 on t ∈[Ti, Ti+1] for all i = 0, 1, 2, . . ., we have
B(t) = N(t)
for B(t) as in (21.2) and N(t) as in (19.9).
Proof:
The claim follows from the considerations above, since the assumption in the theorem
is equivalent to (23.4).
□|
23.2.3. LIBOR Market Model as a Short Rate Model
In 23.2.1 we have given the volatility structure for (t, T) 7→f(t, T) under which the for-
ward rates Li evolve as in a LIBOR market model. Since the short rate is given as r(t) :=
limT↘t f(t, T), the volatility structure also implies a short rate model.
Furthermore, the
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
292
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

23.2. LIBOR MARKET MODEL IN THE HJM FRAMEWORK
num´eraire B(t) = exp(
R t
0 r(τ)dτ) is fully determined by the short rate, thus the short rate process
under QB gives a complete description of all bond prices (and all derivatives):
P(T; t) = B(t)EQB 1
B(T)|Ft
.
The short rate process r implied by the volatility structure (23.3) generates a LIBOR market
model. The short rate process under QB is given by (21.6):
dr(t) =

∂f0
∂T (t) + αQB(t, t) +
t
Z
0
∂αQB
∂T (s, t)ds +
t
Z
0
∂σ
∂T (s, t)dWQB(s)
dt
+σ(t, t)dWQB(t),
(was 21.6)
The drift of this short rate model is, as a function of {r(s)|0 ≤s ≤t}, path-dependent. Only
in high dimensions, namely as a function of {Li(t)|i = 0, . . . , n}, will the model be Markovian
(i.e. the drift is no longer path-dependent).
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
293
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

CHAPTER 23. HEATH-JARROW-MORTON FRAMEWORK: IMMERSION OF SHORT RATE MODELS AND LIBOR MARKET MODEL
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
294
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

CHAPTER 24
Excursus: Shape of the Interest Rate
Curve under Mean Reversion and a
Multi-Factor Model
In this chapter we are considering the influence of model properties like mean reversion, num-
ber of factors, instantaneous correlation und instantaneous volatility on the possible future
shapes of the interest rate curve.
As in Chapter 20, which discussed the relation of instantaneous correlation and instanta-
neous volatility to the terminal correlation, our goal is to develop an understanding of the
significance of the model properties rather than looking at them rigorously in abstract math-
ematical terms. We thus pose the question of how the interest rate curve differs qualitatively
under different model configurations.
24.1. Model
As a model framework we will use the LIBOR Market Model. Due to its many parameters it
gives us enough freedom to play with. We will restrict the set of parameters and concentrate
on three (important) parameters that are sufficient to create the interesting phenomena we are
interested in.
Let us restrict the model to a simple volatility structure, namely
σi(t) = σ∗· exp   −a · (Ti −t)
(24.1)
with σ∗= 0.1 and a = 0.05.
We will choose an equally simple correlation model, namely
dWidWj = ρi,jdt with
ρi,j = exp(−r · |Ti −T j|).
(24.2)
To this correlation model we apply a factor reduction (Principal Component Analysis), see
Appendix A.4. The number of factors is the number of independent Brownian motions (effec-
tively) entering the model, see Definition 50. Upon a factor reduction the m largest eigenvalues
of the correlation matrix are determined. Together with the corresponding eigenvectors a new
correlation matrix is constructed, having at most m non-zero eigenvalues. This process guar-
antees that the resulting correlation model defines a valid correlation matrix.
We simulate under the terminal measure and start with an initially flat interest rate curve
Li(0) = 0.1, i = 0, 1, 2, . . ..
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
295
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

CHAPTER 24. EXCURSUS: SHAPE OF THE INTEREST RATE CURVE UNDER MEAN REVERSION AND A MULTI-FACTOR MODEL
To summarize, our model framework consists of three degrees of freedom which will be
varied in our analysis:
Parameter
Effect
a
Damping of the exponentially decaying,
time-homogenous volatility
r
Damping of the exponentially decaying in-
stantaneous correlation
m
Number of factors extracted from the cor-
relation matrix
Table 24.1.: Free parameters of the LIBOR Market Model considered.
24.2. Interpretation of the Figures
The Figures 24.1, 24.2, 24.3 and 24.4 show 100 paths of a Monte-Carlo simulation of the
interest rate curve. The simulation was frozen at a fixed point in time (t = 7.5 in 24.2, 24.3 and
24.4 and t = 17.5 in 24.1). To the left of this point the forward rates Li(Ti) are shown, each
upon their individual maturity, - this is a discrete analog of the short rate. To the right of this
point the future forward rate curve L j(t) is drawn.
The figures differ only in the parameters used to generate the paths. The same random
numbers are used, thus the simulated paths depend smoothly on a and r.
To improve the visibility of the individual paths, each path is given a different color, where
the hue of the color depends smoothly on the level of the last rate Ln(t).1 This makes its it
very easy to check if the interest rate curves are parallel or exhibit some regular structure, see
Figure 24.2.
24.3. Mean Reversion
We will consider the example of a simple one-factor Brownian motion (ρi, j = 1, i.e. r = 0).
Figure 24.1 shows the simulated forward rates for different parameters a in (24.1).
From the derivation of the Hull-White-Model from the HJM-Framework it became obvious
that an exponentially decreasing volatility structure of the forward rate corresponds to a mean
reversion of the short rate, see page 289. We rediscover this property qualitatively here. Fig-
ure 24.1 shows 100 paths of a Monte-Carlo simulation of a LIBOR market model with different
values for the parameter a: a = 0, a = 0.05 in the upper and a = 0.1, a = 0.15 in the lower
row (left to right). Observe the fixed rates Li(Ti) left from the simulation time. They may be
interpreted as a direct analog of the short rate. In Figure 24.1 it becomes obvious that with an
increasing parameter a the paths develop a tendency to revert to the mean (mean reversion).
1 The choice of the last rate is arbitrary.
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
296
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

24.4. FACTORS
LIBOR Market Model forward rate curves
 0,0
 5,0
 10,0
 15,0
 20,0
time (fixing date of forward rate)
 0%
 2%
 5%
 8%
 10%
 12%
 15%
 18%
 20%
forward rate
LIBOR Market Model forward rate curves
 0,0
 5,0
 10,0
 15,0
 20,0
time (fixing date of forward rate)
 0%
 2%
 5%
 8%
 10%
 12%
 15%
 18%
 20%
forward rate
LIBOR Market Model forward rate curves
 0,0
 5,0
 10,0
 15,0
 20,0
time (fixing date of forward rate)
 0%
 2%
 5%
 8%
 10%
 12%
 15%
 18%
 20%
forward rate
LIBOR Market Model forward rate curves
 0,0
 5,0
 10,0
 15,0
 20,0
time (fixing date of forward rate)
 0%
 2%
 5%
 8%
 10%
 12%
 15%
 18%
 20%
forward rate
Figure 24.1.:
Shape of the fixed rates Li(Ti) and the interest rate curve for different instantaneous
volatilities (corresponds to different mean reversion) frozen at time t = 17.5 using a one-factor mode. We
used a = 0 (upper left), a = 0.05 (upper right), a = 0.10 (lower left) and a = 0.15 (lower right). For
interpretation see Section 24.3.
24.4. Factors
Figure 24.2 shows a Monte-Carlo simulation with the parameters above and varying numbers
of factors m. The possible shapes of the interest rate curve are given by combinations of the
factors parallel shift, tilt, bend and oscillations with increasing frequencies, see also Figure A.1
on Page 364.
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
297
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

CHAPTER 24. EXCURSUS: SHAPE OF THE INTEREST RATE CURVE UNDER MEAN REVERSION AND A MULTI-FACTOR MODEL
LIBOR Market Model forward rate curves
 0,0
 5,0
 10,0
 15,0
 20,0
time (fixing date of forward rate)
 0%
 2%
 5%
 8%
 10%
 12%
 15%
 18%
 20%
forward rate
LIBOR Market Model forward rate curves
 0,0
 5,0
 10,0
 15,0
 20,0
time (fixing date of forward rate)
 0%
 2%
 5%
 8%
 10%
 12%
 15%
 18%
 20%
forward rate
LIBOR Market Model forward rate curves
 0,0
 5,0
 10,0
 15,0
 20,0
time (fixing date of forward rate)
 0%
 2%
 5%
 8%
 10%
 12%
 15%
 18%
 20%
forward rate
LIBOR Market Model forward rate curves
 0,0
 5,0
 10,0
 15,0
 20,0
time (fixing date of forward rate)
 0%
 2%
 5%
 8%
 10%
 12%
 15%
 18%
 20%
forward rate
Figure 24.2.:
Shape of the interest rate curve with different factor configurations, seen at time t = 7.5:
One, two, three and five factors (from upper left to lower right). For interpretation see Section 24.4.
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
298
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

24.5. EXPONENTIAL VOLATILITY FUNCTION
24.5. Exponential Volatility Function
LIBOR Market Model forward rate curves
 0,0
 5,0
 10,0
 15,0
 20,0
time (fixing date of forward rate)
 0%
 2%
 5%
 8%
 10%
 12%
 15%
 18%
 20%
forward rate
LIBOR Market Model forward rate curves
 0,0
 5,0
 10,0
 15,0
 20,0
time (fixing date of forward rate)
 0%
 2%
 5%
 8%
 10%
 12%
 15%
 18%
 20%
forward rate
LIBOR Market Model forward rate curves
 0,0
 5,0
 10,0
 15,0
 20,0
time (fixing date of forward rate)
 0%
 2%
 5%
 8%
 10%
 12%
 15%
 18%
 20%
forward rate
LIBOR Market Model forward rate curves
 0,0
 5,0
 10,0
 15,0
 20,0
time (fixing date of forward rate)
 0%
 2%
 5%
 8%
 10%
 12%
 15%
 18%
 20%
forward rate
Figure 24.3.:
Shape of the fixed rates Li(Ti) and the interest rate curve with different instantaneous
volatilities (corresponds to mean reversion) at time t = 7.5 in a one-factor model (upper row and lower
left) with a = 0.0, a = 0.05 and a = 0.1 and a three-factor model (lower right) with a = 0.1. For
interpretation see Section 24.5.
As in Figure 24.1 we consider the Monte-Carlo simulation under different parameters a.
First a = 0, a = 0.05 and a = 0.1 in a one-factor model (r = 0, m = 1), and last a = 0.1 in a
three-factor model. We are observing this at simulation time t = 7.5 and concentrate here on
the section right of the simulation time, i.e. the interest rate curve Lj(t) for j > m(t).
It is apparent that the curve {Lj(t) | j > m(t)} shows a shape similar to an exponential in j,
depending on the parameter a, see Figure 24.3, lower left (a = 0.1) to the right of the simulation
time. If we consider a one-factor model (as used in the figure), we have:
Lj(t) = Lj(0) · exp

Z t
0
µj(τ)dτ +
sZ t
0
σ j(τ)dτ · W(t)
.
For a fixed point in time t (and a state (path) ω) the interest rate curve shows the following
dependence on j
j 7→Lj(0) · exp
 Z t
0
µj(τ, ω)dτ
!
· exp
k ·
sZ t
0
σ2
j(τ)dτ

where k := W(t, ω).
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
299
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

CHAPTER 24. EXCURSUS: SHAPE OF THE INTEREST RATE CURVE UNDER MEAN REVERSION AND A MULTI-FACTOR MODEL
For the volatility structure (24.1) particularly, we find
Z t
0
σ2
j(τ) =
Z t
0
exp(−2a(T j −τ))dτ
= 1
2a
  exp(−2a(T j −t)) −exp(−2a(T j −0))
= 1
2a · (exp(2a · t) −1) · exp(−2aT j)
i 7→Lj(0) · exp
 Z t
0
µj(τ, ω)dτ
!
· exp
˜k · exp(−aT j)

,
(24.3)
where ˜k = k ·
q
1
2a(exp(2a · t) −1).
The drift
R t
0 µj(τ, ω)dτ is monotone increasing in j, see (19.8). This explains the shape of
the interest rate curve in Figure 24.3 upper left. With increasing parameter a the interest rate
curve is multiplied by the double exponential (24.3) with increasing steepness. This explains
the shape of the interest rate curve in Figure 24.3 upper right and lower left. Only the addition
of more driving factors allows for a richer family of possible curves. If the parallel movement
(level) remains the dominant factor, then the shape (24.3) still dominates the interest rate curve,
Figure 24.3 lower right.
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
300
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

24.6. INSTANTANEOUS CORRELATION
24.6. Instantaneous Correlation
LIBOR Market Model forward rate curves
 0,0
 5,0
 10,0
 15,0
 20,0
time (fixing date of forward rate)
 0%
 2%
 5%
 8%
 10%
 12%
 15%
 18%
 20%
forward rate
LIBOR Market Model forward rate curves
 0,0
 5,0
 10,0
 15,0
 20,0
time (fixing date of forward rate)
 0%
 2%
 5%
 8%
 10%
 12%
 15%
 18%
 20%
forward rate
LIBOR Market Model forward rate curves
 0,0
 5,0
 10,0
 15,0
 20,0
time (fixing date of forward rate)
 0%
 2%
 5%
 8%
 10%
 12%
 15%
 18%
 20%
forward rate
LIBOR Market Model forward rate curves
 0,0
 5,0
 10,0
 15,0
 20,0
time (fixing date of forward rate)
 0%
 2%
 5%
 8%
 10%
 12%
 15%
 18%
 20%
forward rate
Figure 24.4.:
Shape of the fixed rates Li(Ti) and the interest rate curve with different instantaneous
correlations, seen at time t = 7.5. We used a correlation matrix with (all) 40 factors and r = 0.01 (upper
left, high correlation), r = 0.1 (upper right) and r = 1.0 (lower left, high de-correlation). In the lower
right we used a correlation matrix with r = 1.0 (the same as in lower left), but reduced the number of
factors to three. For interpretation see Section 24.6.
We fix a slightly decreasing volatility structure (24.1) with a = 0.1 and vary the parameter r
of the correlation function (24.2). We do not apply a factor reduction, thus keep all 40 factors.
The parameter r = 0.01 corresponds to an almost perfect correlation of the processes. Thus
the possible shapes of the curve are almost parallel, the curve is very smooth since we started
from a smooth (namely flat) curve. If the correlation parameter is increased to r = 1.0, then the
distribution of rates within the curve is almost independent. See Figure 24.4 upper left, upper
right and lower left.
It should be noted that this (terminal) de-correlation is also achievable under r = 0.01 by an
appropriate choice of the volatility structure, see Chapter 20. The instantaneous de-correlation
introduces an additional terminal de-correlation. The statement that a model with perfect
instantaneous correlation exhibits perfect terminal de-correlation of the forward rates is wrong.
Finally we have chosen in Figure 24.4 lower right the parameter r = 1.0 again (as for the
lower left with strong de-correlation), but have applied a reduction to the three largest factors.
It is obvious that this strongly reduces the possibility of de-correlation. The three factors only
allow that the beginning, the middle and the end of the curve attain different values. Adjacent
rates are still on similar levels.
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
301
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

CHAPTER 24. EXCURSUS: SHAPE OF THE INTEREST RATE CURVE UNDER MEAN REVERSION AND A MULTI-FACTOR MODEL
Experiment:
At http://www.christian-fries.de/finmath/
applets/LMMSimulation.html a simulation of an interest rate curve with
the model framework above is to be found. The parameters may be chosen at will
to study the different shapes of the interest rate curve.
◁|
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
302
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

CHAPTER 25
Markov Functional Models
25.1. Introduction
Motivation:
From Chapter 5 we have a relation between the prices of European
options and the probability distribution function (or probability density) of the
underlying (under the martingale measure). If we consider a European option on
some underlying, say the forward rate Li := L(Ti, Ti+1; Ti) (i.e. a caplet), then
Lemma 81 allows us to calculate the probability density of Li from the given market prices. It
seems as if this allows perfect calibration of a “model” to a continuum of given market prices.
However, the terminal distribution alone does not determine a pricing model. What is missing
is the specification of the dynamics, i.e. the specification of transition probabilities, and, of
course, the specification of the num´eraire. This is the motivation for the Markov functional
modeling. There we postulate a simple Markov process, e.g. dx = σ(t)dW(t) for which the
distribution function ξ 7→P(x(T) ≤ξ) is known analytically. Then we require the underlying
Li to be a function of x(Ti). Let us denote this function by gi, i.e. let Li(ω) = gi(x(Ti, ω)) for
all paths ω. If the functional gi is strictly monotone, then with K = gi(ξ)
FLi(K) := P(Li ≤K) = P(gi(x(T)) ≤K)
= P(x(T) ≤ξ) =: Fx(Ti)(ξ) = Fx(Ti)(g−1
i (K)).
With a given distribution function FLi of Li (e.g. extracted from market prices through
Lemma 81), the choice of the functional gi allows the calibration to the distribution of Li,
while the process x (and the sequence of functionals {gi}) describe the dynamics. To achieve a
fully specified pricing model we further require the specification of the num´eraire as function
of the Markov process x. To achieve this we may use Theorem 79, if
• x is given under the equivalent martingale measure Q and
• x generates the filtration.
◁|
Given a filtered probability space (R, B(R), Q, {Ft}). Consider a time-discretization 0 = T0 <
T1 < . . . < Tn. Financial products beyond Tn are not considered.
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
303
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

CHAPTER 25. MARKOV FUNCTIONAL MODELS
Let t 7→N(t) denote the price process of a traded asset, which we choose as num´eraire and
let Q denote the corresponding equivalent martingale measure. Then for any replicable asset
price process V(t) (see Definition 73 and Theorem 79)
V(Ti)
N(Ti) = EQN  V(Tk)
N(Tk)|FTi
.
In particular for every zero coupon bond P(Tk), paying 1 in Tk
P(Tk; Ti)
N(Ti)
= EQN 1
N(Tk)|FTi
, d.h.
P(Tk; Ti) = N(Ti)EQN 1
N(Tk)|FTi
.
Let x denote a Ft-adapted stochastic process with
dx(t) = σ(t)dW(t)
,
x(0) = x0.
The filtration should be generated by x. On this space we consider time-discrete stochastic
processes, namely those for which their Ti-realization is a function of (x(T0), . . . , x(Ti)) , for
all i. We particularly consider processes for which their time Ti-realization is a function of
x(Ti) alone (i.e. independent of the process’s history).
25.1.1. The Markov Functional Assumption (independent of the
model considered)
We assume that the time Ti-realization of the num´eraire process is a function of x(Ti), i.e.
N(Ti, ω) = N(Ti, x(Ti, ω)),
(25.1)
where we use the same letter N for the (deterministic) functional ξ 7→N(Ti, ξ).
Then, for any payoffV(Tk) that is itself a function of x(Tk) for some k, the value process
V(Ti) for i ≤k is
V(Ti) = N(Ti)E
 V(Tk)
N(Tk)|FTi
!
= N(Ti, x(Ti))E
 V(Tk, x(Tk))
N(Tk, x(Tk))|σ(x(Ti))
!
.
Thus, the time Ti realization of the value process V(Ti) is also a functional of x(Ti) which we
denote by the same letter V. The functional ξ 7→V(Ti, ξ) of the value process is
ξ 7→N(Ti, ξ)E
 V(Tk, x(Tk))
N(Tk, x(Tk))|{x(Ti) = ξ}
!
.
Note: The markov functional assumption (25.1) may be relaxed such that the num´eraire is
allowed to depend on x(T0), . . . , x(Ti)). This relaxation is used in the LIBOR Markov Func-
tional Model in spot measure.
25.1.2. Outline of this Chapter
In 25.2 we consider a Markov Functional Model for a stock (or any other non-interest rate
related (single) asset). In 25.3 we will then consider a Markov Functional Model for the for-
ward rate L(Ti, Ti+1; Ti), which may be viewed as a time-discrete analog of the short rate. Both
sections are essentially independent of each other. In Section 25.4 we will discuss how to
implement a Markov functional model using a lattice in the state space.
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
304
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

25.2. EQUITY MARKOV FUNCTIONAL MODEL
25.2. Equity Markov Functional Model
25.2.1. Markov Functional Assumption
Consider a simple one-dimensional Markov process, e.g.
dx(t) = σ(t) · dWQ(t),
x(0) = x0,
(25.2)
where σ is a deterministic function and WQ denotes a Q-Brownian motion. Without loss of
generality we may assume x0 = 0. Equation (25.2) is the most simple choice of a Markovian
driver process. We will consider the addition of a drift term to (25.2) in our discussion of
model dynamics in Section 25.2.5.
Let S (t) denote the time t value of some asset for which we assume that we have a continuum
of European option prices. Let x and S be adapted stochastic processes defined on (Ω, Q, Ft),
where {Ft} denotes the filtration generated by WQ.
We assume that the time t value of the asset S is a function of x(t), i.e. we assume the
existence of a functional (t, ξ) 7→S (t, ξ) such that
S (t, ω) = S (t, x(t, ω)),
where the left hand side denotes our asset value at time t on path ω and the right hand side
denotes some functional of our Markovian driver x, which we ambiguously name S . We allow
some ambiguity in notation here. From here on S will also denote a deterministic mapping
(the functional)
(t, ξ) 7→S (t, ξ).
It will be clear from the arguments of S if we speak of the functional (t, ξ) 7→S (t, ξ) or of the
process t 7→S (t).
For t1 < t2 we trivially have that
S (t1)
S (t1) = EQ(S (t2)
S (t2) | Ft1).
We now postulate that Q is the equivalent martingale measure with respect to the Num´eraire S
and that a universal pricing theorem holds for all other traded products, i.e. that their S relative
price is a Q-martingale.
This implies that the zero coupon bond P(T; t) having maturity T and being observed in
t < T fulfills
P(T; t)
S (t)
= EQ(
1
S (T) | Ft).
Using the functional representation of S we find that P(T; t) is represented as a functional of
x(t) too, namely
(t, ξ) 7→P(T; t)
with
P(T; t, ξ)
S (t, ξ)
= EQ(
1
S (T, x(T)) | {x(t) = ξ}).
(25.3)
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
305
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

CHAPTER 25. MARKOV FUNCTIONAL MODELS
25.2.2. Example: The Black-Scholes Model
Let us assume a Markovian driver with constant instantaneous volatility σ(t) = σ. For the
Black-Scholes Model we have
S (t, ξ) = S (0) · exp  r · t + 1
2σ2
BSt + σBS
σ · ξ,
(25.4)
where σBS denotes the (constant) Black-Scholes volatility. Plugging this into (25.3) we find
P(T; t, ξ) = exp(−r(T −t)),
so that interest rates are indeed deterministic here.
This is the Black-Scholes model: From the definition of the Markovian driver we have
1
σ · x(t) = W(t) and thus
S (t, x(t)) = S (0) · exp  r · t + 1
2σ2
BSt + σBS · W(t).
In other words, the Q dynamics of S is1
dS (t) = rS (t)dt + σ2
BSS (t)dt + σBSS (t) · dWQ(t).
Introducing a new Num´eraire
dB(t) = rB(t)dt,
B(0) = 1
we find for the change of Num´eraire process S
B that
dS
B = σ2
BSS (t)dt + σBSS (t) · dWQ(t).
For S
B to be a martingale under QB it has to be dWQ(t) = dWQB −σ2
BSdt and thus
dS (t) = rS (t)dt + σBS · S (t) · dWQB(t)
dB(t) = rB(t)dt.
Note: dWQ(t) is a Q Brownian motion, where Q is the equivalent martingale measure with re-
spect to the Num´eraire S , while dWQB(t) is a QB Brownian motion, where QB is the equivalent
martingale measure with respect to the Num´eraire B.
25.2.3. Numerical Calibration to a Full Two-Dimensional European
Option Smile Surface
As for the interest rate Markov functional model we are able to calculate the functionals nu-
merically from a given two-dimensional smile surface. Our approach here is similar to the
approach for the one-dimensional LIBOR Markov functional model under spot measure, [67].
Consider the following time T payout:
V(T, K; T) :=

S (T)
if S (T) > K
0
otherwise.
(25.5)
1 Note that Q is the equivalent martingale measure with respect to the Num´eraire S .
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
306
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

25.2. EQUITY MARKOV FUNCTIONAL MODEL
Obviously
V(T, K; T) = max(S (T) −K, 0) + K ·

1
if S (T) > K
0
else,
i.e. the value of V is given by the value of a portfolio of one call option and K digital options,
all having strike K. This is our calibration product.
25.2.3.1. Market Price
Let ¯σBS(T, K) denote the Black-Scholes implied volatility surface given by market prices.
Then the market price of V is
Vmarket(T, K; 0) = S (0)Φ(d+) −exp(−rT)KΦ(d−)
|                                  {z                                  }
call option part
+ K exp(−rT)(Φ(d−) + S (0)
√
TΦ′(d+)∂¯σBS(T, K)
∂K
)
|                                                         {z                                                         }
digital part
= S (0)Φ(d+) + KS (0)
√
TΦ′(d+)∂¯σBS(T, K)
∂K
,
where Φ(x) :=
1
√
2π
R x
−∞exp(−y2
2 )dy and d± =
ln( exp(rT)S (0)
K
)± 1
2 ¯σ2
BS(T,K)T
¯σBS(T,K)
√
T
.
25.2.3.2. Model Price
Within our model the price of the product (25.5) is
Vmodel(T, K; 0) = S (0) · EQ S (T, x(T)) · 1{S (T,x(T))>K}
S (T)
| {x(0) = x0}
= S (0) · EQ 1{S (T,x(T))>K} | {x(0) = x0}
Assuming that our functional (T, ξ) 7→S (T, ξ) is monotonely increasing in ξ we may write
Vmodel(T, K; 0) = S (0) · EQ 1{x(T)>x∗} | {x(0) = x0},
(25.6)
where x∗is the (unique) solution of S (T, x∗) = K. Note that (25.6) depends on x∗and the
probability distribution of x(T) only and that x(T) is known due to the simple form of our
Markovian driver. It does not depend on the functional S ! Thus for given x∗we can calculate
Vmodel(T, x∗; 0) := S (0) · EQ 1{x(T)>x∗} | {x(0) = x0}.
25.2.3.3. Solving for the Functional
For given x∗we now solve the equation
Vmarket(T, K∗; 0) = Vmodel(T, x∗; 0)
to find S (T, x∗) = K∗and thus the functional form (T, ξ) 7→S (T, ξ). This can be done very
efficiently using fast one-dimensional root finders, e.g. Newton’s method.
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
307
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

CHAPTER 25. MARKOV FUNCTIONAL MODELS
25.2.4. Interest Rates
25.2.4.1. A Note on Interest Rates and the No-Arbitrage Requirement
Functional models for equity option pricing have been investigated before, see e.g. [57] and
references therein. However, the approach considered there chooses deterministic interest rates
and the bank account as Num´eraire. As suggested in Section 25.2.2, this will impose a very
strong self-similarity requirement on the functionals (which is fulfilled by the Black-Scholes
model). Such models may calibrate only to a one-dimensional sub-manifold of a given implied
volatility surface, see [58]. For the Markov functional model this follows directly from (25.3).
Assuming that the Markovian driver x is given and that the interest rate dynamic P(T; t, ξ) is
given, we find from (25.3) that
S (t, ξ) =
P(T; t, ξ)
EQ(
1
S (T,x(T)) | {x(t) = ξ})
.
So once a terminal time T functional ξ 7→S (T, ξ) has been defined, all other functionals are
implied by the interest rate dynamics P and the dynamics of the Markovian driver.
Sticking to prescribed interest rates, the only way to allow for more general functional is to
violate the no-arbitrage requirement (25.3) or change the Markovian driver. The latter will be
considered in Section 25.2.5.
25.2.4.2. Where are the Interest Rates?
Our model calibrates to a continuum of options on S . We do not even specify interest rates.
This is not necessary, since the specification of the interest rates is already contained in the
specification of a continuum of options on S . Consider options on S (T), i.e. options with
maturity T. First note that from a continuum K 7→Vmarket
call
(T, K; 0) of market prices for call
option payouts
Vmarket
call
(T, K; T) = max(S (T) −K, 0)
we obtain prices for the corresponding digital payouts
Vmarket
digital (T, K; T) =

1
S (T) > K
0
else
by
Vmarket
digital (T, K; 0) = −∂
∂K Vmarket
call
(T, K; 0).
Thus the value of the zero coupon bond with maturity T is
P(T; 0) = lim
K↘0 Vmarket
digital (T, K; 0) = −lim
K↘0
∂
∂K Vmarket
call
(T, K; 0).
(25.7)
Note that this argument is model-independent.
Within the functional model, Equation (25.7) holds locally in each state. Given that we are
at time t in state x(t) = ξ we have for the corresponding bond
P(T; t, ξ) = lim
K↘0 Vmodel
digital(T, K; t, ξ).
This work is licensed under a
Creative Commons License.
http://creativecommons.org/licenses/by-nc-nd/2.5/deed.en
308
Comments welcome.
©2004, 2005, 2006, 2007 Christian Fries
Version 1.4.18 [build 20070403]- 1st May 2007
http://www.christian-fries.de/finmath/book

