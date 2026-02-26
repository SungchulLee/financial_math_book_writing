# Volatility Inference & Calibration

!!! info "Source"
    **Inside Volatility Arbitrage: The Secrets of Skewness** by Alireza Javaheri, Wiley, 2005.
    These notes are used for educational purposes.

## The Inference Problem

32
INSIDE VOLATILITY ARBITRAGE
It is now possible to integrate the stock process for a given volatility and
end up with an expectation on the volatility process only. We can think of
(1.46) as the limit of a discrete process, while the time step t →0.
For a derivative security f (S0 v0 T ) with a payoff32 G(ST), using the
bivariate normal density for two uncorrelated variables, we can write
f (S0 v0 T ) = e−rTE0[G(ST)]
(1.47)
= e−rT lim
t→0
	 ∞
−∞
...
	 ∞
−∞
G(ST)
T −t

t=0
exp

−1
2

Z2
t + W 2
t
dZtdWt
2π
If we know how to integrate the above over dWtfor a given volatility and
we know the result f ∗(S v T ) (for instance, for a European call option, we
know the Black-Scholes formula (1.6), there are many other cases where we
have closed-form solutions), then we can introduce the auxiliary variables33
Seff = S0eYT = S0 exp

−1
2
	 T
0
ρ2
t σ2
t dt +
	 T
0
ρtσtdZt

(1.48)
and
veff = 1
T
	 T
0

1 −ρ2
t

σ2
t dt
(1.49)
and as Romano and Touzi prove in [209], we will have
f (S0 v0 T ) = E0[f ∗(Seff veff T )]
(1.50)
where this last expectation is being taken on dZt only. Note that in the zero
correlation case discussed by Hull and White [149] we have Seff = S0 and
veff = vT = 1
T
 T
0 σ2
t dt, which makes the expression (1.50) a natural weighted
average.
A One-Factor Monte Carlo Technique
As Lewis suggests, this will enable us to run a single-factor Monte Carlo
simulation on the dZt and apply the known closed form for each simulated
path. The method does suppose, however, that the payoff G(ST) does not
depend on the volatility. Indeed, going back to (1.46) we can do a simulation
on Yt and vt using the random sequence of (Zt); then, after one path is
generated, we can calculate Seff = S0 exp(YT) and veff = 1
T
T −t
t=0 (1−ρ2
t )vtt
32The payoff should not depend on the volatility process.
33Again, all notations are taken from Lewis [177].

The Volatility Problem
33
0
20
40
60
80
100
120
140
160
180
200
950
1000
1050
1100
1150
Call Price
Strike Price
Volatility Smile
Market 1 Month to Maturity
Model
Market 7 Months to Maturity
Model
FIGURE 1.7
Mixing Monte Carlo Simulation with the Square-Root Model for SPX
on February 12, 2002 with Index = $1107.50, 1 month and 7 months to Maturity.
The Powell optimization method was used for least-square calibration. As we can
see, both maturities are fitted fairly well.
and then apply the known closed form (e.g. Black-Scholes for a call or put)
with Seff and veff. Repeating this procedure for a large number of times and
averaging over the paths, as we usually do in Monte-Carlo methods, we will
have f (S0 v0 T ). This will give us a way to calibrate the model parameters
to the market data. For instance, using the square-root model
dvt = (ω −θvt)dt + ξ√vtdZt
we can estimate ω, θ, ξ, and ρ from the market prices via a least-square
estimation applied to theoretical prices obtained from the preceding Monte
Carlo method (Figure 1.7). We can either use a single calibration and sup-
pose we have time-independent parameters or perform one calibration per
maturity. The single calibration method is known to provide a bad fit, hence
the idea of adding jumps to the stochastic volatility process as described by
Matytsin [187]. However, this method will introduce new parameters for
calibration.34
34Eraker et al. [98] claim that a model containing jumps in the return and the
volatility process will fit the options and the underlying data well, and will have no
misspecification left.

34
INSIDE VOLATILITY ARBITRAGE
THE LONG-TERM ASYMPTOTIC CASE
In this section we will discuss the case in which the contract time to maturity
is very large, t →∞. We will focus on the special case of a square-root
process because this is the model we will use in many cases.
The Deterministic Case
We shall start with the case of deterministic volatility and use that for the
more general case of the stochastic volatility.
We know that under the square-root model the variance follows
dvt = (ω −θvt)dt + ξ√vtdZt
As an approximation, we can drop the stochastic term and obtain
dvt
dt = ω −θvt
which is an ordinary differential equation providing us immediately with
vt = ω
θ +

v −ω
θ

e−θt
(1.51)
where v is the initial variance for t = 0.
Using the results from the fundamental transform for a covered call
option and put-call parity, we have for 0 < ki < 1
call(S v τ) = Se−qτ −Ke−rτ 1
2π
	 iki+∞
iki−∞
e−ikX ˆH(k v τ)
k2 −ik dk
(1.52)
where τ = T −t and X = ln

 Se−qτ
Ke−rτ

represent the adjusted moneyness of the
option. For the special “at-the-money”35 case, where X = 0, we have
call(S v τ) = Ke−rτ

1 −1
2π
	 iki+∞
iki−∞
ˆH(k v τ)
k2 −ik dk

(1.53)
As we previously said for a deterministic volatility case, we know the fun-
damental transform
ˆH(k v τ) = exp[−c(k)U(v τ)]
35This is different from the usual definition of at-the-money calls, where S = K .
This vocabulary is borrowed from Alan Lewis.

The Volatility Problem
35
With U(v τ) =
 τ
0 v(t)dt and as before c(k) = 1
2(k2 −ik), which in the
special case of the square-root model (1.51), will provide us with
U(v τ) = ω
θ τ +

v −ω
θ
1 −e−θτ
θ

This shows once again that ˆH(k) is analytic in k over the entire complex
plane.
Now if we let τ →∞, we can write the approximation
call(S v τ)
Ke−rτ
≈1 −1
2π
	 iki+∞
iki−∞
exp

−c(k)ω
θ τ −c(k)1
θ

v −ω
θ

dk
k2 −ik
(1.54)
We can either calculate the above integral exactly using the Black-Scholes
theory, or take the minimum where c′(k0) = 0, meaning k0 = i
2, and perform
a Taylor approximation parallel to the real axis around the point k = kr + i
2,
which will give us
call(S v τ)
Ke−rτ
≈1 −2
π exp

−ω
8θτ

exp

−1
8θ

v −ω
θ
 	 ∞
−∞
exp

−k2
r
ω
2θτ

dkr
the integral being a Gaussian we will get the result
call(S v τ)
Ke−rτ
≈1 −

8θ
πωτ exp

−1
8θ

v −ω
θ

exp

−ω
8θτ

(1.55)
which finishes our deterministic approximation case.
The Stochastic Case
For the stochastic volatility case, Lewis uses the same Taylor expansion. He
notices that for the deterministic case we had
ˆH(k v τ) = exp [−c(k)U(v τ)]≈exp[−λ(k)τ]u(k v)
for τ →∞, where
λ(k) = c(k)ω
θ
and
u(k v) = exp

−c(k)1
θ

v −ω
θ

If we suppose that this identity holds for the stochastic volatility case as
well, we can use the PDE (1.44) and interpret the result as an eigenvalue-
eigenfunction identity with the eigenvalue λ(k) and the eigenfunction u(k v).

36
INSIDE VOLATILITY ARBITRAGE
This assumption is reasonable because the first Taylor approximation term
for the stochastic process is deterministic. Indeed, introducing the operator
	(u) = −1
2a2(v)d2u
dv2 −
˜b(v) −ikρ(v)a(v)√v
 du
dv + c(k)vu
we have
	(u) = λ(k)u
(1.56)
Now the idea would be to perform a Taylor expansion around the min-
imum k0 where λ′(k0) = 0. Lewis shows that such k0 is always situated on
the imaginary axis. This property is referred to as the “ridge” property.
The Taylor expansion along the real axis could be written as
λ(k) = λ(k0 + kr) ≈λ(k0) + 1
2k2
r λ′′(k0)
Note that we are dealing with a minimum, and therefore λ′′(k0) > 0. Using
the above second-order approximation for λ(k), we get
call(S v τ)
Ke−rτ
≈1 −u(k0 v)
k2
0 −ik0
1

2πλ′′(k0)τ
exp[−λ(k0)τ]
We can then move from the special “at-the-money” case to the general case by
reintroducing X = ln

 Se−qτ
Ke−rτ

, and we will finally obtain
call(S v τ)
Ke−rτ
≈eX −u(k0 v)
k2
0 −ik0
1

2πλ′′(k0)τ
exp[−λ(k0)τ −ik0X]
(1.57)
which completes our determination of the asymptotic closed form in the
general case.
For the special case of the square-root model, taking the risk-neutral
case γ = 1, we have36
λ(k) = −ωg∗(k) = ω
ξ2

(θ + ikρξ)2 + (k2 −ik)ξ2−(θ + ikρξ)

which also allows us to calculate λ′′(k). Also
u(k v) = exp[g∗(k)v]
36We
can
go
back
to
the
general
case
γ
≤
1
by
replacing
θ
with

θ2 −γ(1 −γ)ξ2 + (1 −γ)ρξ because this transformation is independent from
k altogether.

The Volatility Problem
37
where we use the notations from (1.45) and we pose
g∗= g −d
The k0 such that λ′(k0) = 0 is
k0 =
i
1 −ρ2
1
2 −ρ
ξ

θ −1
2

4θ2 + ξ2 −4ρθξ

which together with (1.57) provides us with the result for call(S v τ) in the
asymptotic case under the square-root stochastic volatility model.
Note that for ξ →0 and ρ →0, we find again the deterministic result
k0 →i
2.
A Series Expansion on Volatility-of-Volatility
Another asymptotic approach for the stochastic volatility model suggested
by Lewis [177] is a Taylor expansion on the volatility-of-volatility. There are
two possibilities for this: We can perform the expansion either for the option
price or for the implied volatility directly. In what follows, we consider the
former approach. Once again, we use the fundamental transform H(k V  τ)
with H(k V  0) = 1 and
∂H
∂τ = 1
2a2(v)∂2H
∂v2 +

˜b(v) −ikρ(v)a(v)√v
∂H
∂v −c(k)vH
and c(k) = 1
2(k2 −ik). We then pose a(v) = ξη(v) and expand H(k V  τ)on
powers of ξ and finally apply the inverse Fourier transform to obtain an
expansion on the call price.
With our usual notations τ = T −t, X = ln( S
K ) + (r −q)τ and Z(V ) = V τ,
the series will be
C(S V  τ) = cBS(S v τ) + ξτ−1J1 ˜R11
∂cBS(S v τ)
∂V
+ξ2

τ−2J3 ˜R20 + τ−1J4 ˜R12 + 1
2τ−2J 2
1 ˜R22
∂cBS(S v τ)
∂V
+ O(ξ3)
where v(V  τ) is the deterministic variance
v(V  τ) = ω
θ +

V −ω
θ
1 −e−θτ
θτ

and ˜Rpq = Rpq(X v(V  τ) τ) with Rpq given polynomials of (X Z) of degree
four at most, and Jn’s known functions of (V  τ).

38
INSIDE VOLATILITY ARBITRAGE
The explicit expressions for all these functions are given in the third
chapter of the Lewis book [177].
The obvious advantages of this approach are its speed and stability.
The issue of lack of time homogeneity of the parameters  = (ω θ ξ ρ)
could be addressed by performing one calibration per time interval. In this
case, for each time interval [tn tn+1] we will have one set of parameters
n = (ωn θn ξn ρn) and depending on what maturity T we are dealing
with, we will use one or the other parameter set.
We compare the values obtained from this series-based approach with
those from a mixing Monte Carlo method in Figure 1.8. We are taking
the example that Heston studied in [134]. The graph shows the difference
C(S V  τ) −cBS(S V  τ) for a fixed K = $100 and τ = 0.50 year. The other
inputs are ω = 0.02, θ = 2.00, ξ = 0.10, ρ = −0.50, V = 0.01, and r = q = 0.
As we can see, the true value of the call is lower than the Black-Scholes value
for the out-of-the-money (OTM) region. The higher ξ and |ρ| are, the larger
this difference will be.
In Figures 1.9 and 1.10, we reset the correlation ρ to zero to have a symmet-
ric distribution, but we use a volatility-of-volatility of ξ = 0.10 and ξ = 0.20
respectively. As discussed, the parameter ξ is the one creating the leptokur-
–0.15
–0.1
–0.05
0
0.05
0.1
0.15
70
80
90
100
110
120
130
Price Difference
Stock (USD)
Heston Prices via Mixing and Vol-of-Vol Series
Mixing
Vol-of-Vol Series
FIGURE 1.8
Comparing the Volatility-of-Volatility Series Expansion with the Monte
Carlo Mixing Model. The graph shows the price difference C(S V  τ) −cBS(S V  τ).
We are taking ξ = 0.10 and ρ = −0.50. This example was used in the original Heston
paper.

The Volatility Problem
39
–0.03
–0.025
–0.02
–0.015
–0.01
–0.005
0
0.005
0.01
0.015
70
80
90
100
110
120
130
Price Difference
Stock (USD)
Heston Prices via Mixing and Vol-of-Vol Series
Mixing
Vol-of-Vol Series
FIGURE 1.9
Comparing the Volatility-of-Volatility Series Expansion with the Monte
Carlo Mixing Model. The graph shows the price difference C(S V  τ) −cBS(S V  τ).
We are taking ξ = 0.10 and ρ = 0. This example was used in the original Heston
paper.
–0.12
–0.1
–0.08
–0.06
–0.04
–0.02
0
0.02
0.04
0.06
70
80
90
100
110
120
130
Price Difference
Stock (USD)
Heston Prices via Mixing and Vol-of-Vol Series
Mixing
Vol-of-Vol Series
FIGURE 1.10
Comparing the Volatility-of-Volatility Series Expansion with the
Monte Carlo Mixing Model. The graph shows the price difference C(S V  τ)
−cBS(S V  τ). We are taking ξ = 0.20 and ρ = 0. This example was used in the orig-
inal Heston paper.

40
INSIDE VOLATILITY ARBITRAGE
ticity phenomenon. A higher volatility-of-volatility causes higher valuation
for far-from-the-money options.37
Unfortunately, the foregoing series approximation becomes poor as soon
as the volatility-of-volatility becomes larger than 0.40 and the maturity
becomes of the order of 1 year. This case is not unusual at all and there-
fore makes the use of this method limited. This is why the method of choice
remains the inversion of the Fourier transform, as previously described.
PURE-JUMP MODELS
Variance Gamma
An alternative point of view is to drop the diffusion assumption altogether
and replace it with a pure-jump process. Note that this is different from
the jump-diffusion process previously discussed. Madan et al. suggested the
following framework, called variance-gamma (VG) in [182]. We would have
the log-normal-like stock process
d ln St = (µS + ω)dt + X(dt; σ ν θ)
where as before µS is the real-world statistical drift of the stock log return
and ω = 1
ν ln(1 −θν −σ2ν/2).
As for X(dt; σ ν θ), it has the following meaning:
X(dt; σ ν θ) = B(γ(dt 1 ν); θ σ)
where B(dt; θ σ) would be a Brownian motion with drift θ and volatility σ.
In other words
B(dt; θ σ) = θdt + σ
√
dtN(0 1)
and N(0 1) is a standard Gaussian realization.
The time interval at which the Brownian motion is considered is not dt
but γ(dt 1 ν) which is a random realization following a gamma distribution
with a mean 1 and variance rate ν. The corresponding probability density
function is
fν(dt τ) = τ
dtν −1e−τν
ν
dtν 
( dt
ν )
where 
(x) is the usual gamma function.
Note that the stock log-return density could actually be integrated for the
VG model, and the density of ln (St/S0) is known and could be implemented
37Also note that the gap between the closed-form series and the Monte Carlo model
increases with ξ. Indeed, the accuracy of the expansion decreases as ξ becomes larger.

The Volatility Problem
41
via Kα(x), the modified Bessel function of the second kind. Indeed, calling
z = ln(Sk/Sk−1) and h = tk−tk−1 and posing xh = z−µSh−h
ν ln(1−θν−σ2ν/2)
we have
p(z|h) = 2 exp(θxh/σ2)
ν
hν √
2πσ
( h
ν)

x2
h
2σ2/ν + θ2
 h
2ν −1
4
K hν −1
2
 1
σ2

x2
h(2σ2/ν + θ2)

Moreover, as Madan et al. show, the option valuation under VG is fairly
straightforward and admits an analytically tractable closed form that can be
implemented via the above modified Bessel function of second kind and a
degenerate hypergeometric function. All details are available in [182].
Remark on the Gamma Distribution
The gamma cumulative distribution function
(CDF) could be defined as
P (a x) =
1

(a)
	 x
0
e−tta−1dt
Note that with our notations
Fν(h x) = F(h x µ = 1 ν)
with
F(h x µ ν) =
1

( µ2h
ν )
µ
ν
 µ2h
ν 	 x
0
e−µt
ν t
µ2h
ν −1dt
In other words
F(h x µ ν) = P
µ2h
ν  µx
ν

The behavior of this CDF is displayed in Figure 1.11 for different values of
the parameter a > 0 and for 0 < x < +∞.
Using the inverse of this CDF, we can have a simulated data set for the
gamma law:
x(i) = F −1
ν (h U(i)[0 1])
with 1 ≤i ≤Nsims and U(i)[0 1] a uniform random realization between zero
and one.

42
INSIDE VOLATILITY ARBITRAGE
0
0.2
0.4
0.6
0.8
1
0
200
400
600
800
1000
1200
1400
1600
P(a,x)
100x
The Gamma Cumulative Distribution Function
a = 10
a = 3
a = 1
a = 0.5
FIGURE 1.11
The Gamma Cumulative Distribution Function P(a x) for Various
Values of the Parameter a. The implementation is based on code available in Numer-
ical Recipes in C [204].
0
0.5
1
1.5
2
2.5
3
3.5
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
K(x, nu = 0.1)
x
Modified Bessel Function of Second Kind
K(x, nu = 0.1)
FIGURE 1.12
The Modified Bessel Function of Second Kind for a Given Parameter.
The implementation is based on code available in Numerical Recipes in C [204].
Stochastic Volatility vs. Time-Changed processes
As mentioned in [23], this alter-
native formulation leading to time-changed processes is closely related to
the previously discussed stochastic volatility approach in the following way.

The Volatility Problem
43
0.92
0.925
0.93
0.935
0.94
0.945
0.95
0
0.05
0.1
0.15
0.2
K(x = 0.5, nu)
nu
Modified Bessel Function of Second Kind
K(x = 0.5, nu)
FIGURE 1.13
The Modified Bessel Function of Second Kind as a Function of the
Parameter. The implementation is based on code available in Numerical Recipes in
C [204].
Taking the foregoing VG stochastic differential equation
d ln St = (µS + ω)dt + θγ(dt 1 ν) + σ

γ(dt 1 ν)N(0 1)
one could consider σ2γ(t 1 ν) as the integrated variance and define vt(ν),
the instantaneous variance, as
σ2γ(dt 1 ν) = vt(ν)dt
in which case, we would have
d ln St = (µS + ω)dt + (θ/σ2)vt(ν)dt +

vt(ν)dtN(0 1)
= (µS + ω + (θ/σ2)vt(ν))dt +

vt(ν)dZt
where dZt is a Brownian motion. This last expression is a traditional stochas-
tic volatility equation.
Variance Gamma with Stochastic Arrival
An extension of the VG model would be a variance gamma model with
stochastic arrival (VGSA), which would include the volatility clustering effect.
This phenomenon (also represented by GARCH) means that a high (low)
volatility will be followed by a series of high (low) volatilities. In this

44
INSIDE VOLATILITY ARBITRAGE
approach, we replace the dt in the previously defined fν(dt τ) with ytdt,
where yt follows a square-root (CIR) process
dyt = κ(η −yt)dt + λ√ytdWt
where the Brownian motion dWt is independent from other processes in
the model. This is therefore a VG process in which the arrival time itself
is stochastic. The mean reversion of the square-root process will cause the
volatility persistence effect that is empirically observed. Note that (not count-
ing µS) the new model parameter set is  = (κ η λ ν θ σ).
Option Pricing under VGSA
The option pricing could be carried out via a Monte
Carlo simulation algorithm under the risk-neutral measure, where, as before,
µS is replaced with r −q. We first would simulate the path of yt by writing
yk = yk−1 + κ(η −yk−1)t + λ√yk−1
√
tZk
then calculate
YT =
N−1

k=0
ykt
and finally apply one-step simulations
T ∗= F −1
ν
(YT U[0 1])
and38
ln ST = ln S0 + (r −q + ω)T + θT ∗+ σ
√
T ∗Bk
Note that we have two normal random variables Bk, Zk as well as a gamma-
distributed random variable T ∗, and that they are all uncorrelated. Once the
stock price ST is properly simulated, we can calculate the option price as
usual.
The Characteristic Function
As previously discussed, another way to tackle the
option-pricing issue would be to use the characteristic functions. For VG,
the characteristic function is
(u t) = E[eiuX(t)] =

1
1 −i ν
µu
 µ2
ν t
Therefore the log-characteristic function could be written as
ψ(u t) = ln((u t)) = tψ(u 1)
38This means that T in VG is replaced with YT. The rest remains identical.

The Volatility Problem
45
In other words
E[eiuX(t)] = (u t) = exp(tψ(u 1))
Using which, the VGSA characteristic function becomes
E

eiuX(Y(t))
= E[exp(Y(t)ψ(u 1))] = φ(−iψ(u 1))
with φ() the CIR characteristic function, namely
φ(ut) = E[exp(iuYt)] = A(t u) exp(B(t u)y0)
where
A(t u) =
exp(κ2ηt/λ2)
[cosh(γt/2) + κ/γ sinh(γt/2)]
2κη
λ2
B(t u) =
2iu
κ + γ coth(γt/2)
and
γ =

κ2 −2λ2iu
This allows us to determine the VGSA characteristic function, which we can
use to calculate options prices via numeric Fourier inversion as described in
[48] and [51].
Variance Gamma with Gamma Arrival Rate
For the variance gamma with gamma arrival rate (VGG), as before, the stock
process under the risk-neutral framework is
d ln St = (r −q + ω)dt + X(h(dt); σ ν θ)
with ω = 1
ν ln(1 −θν −σ2ν/2) and
X(h(dt); σ ν θ) = B(γ(h(dt) 1 ν); θ σ)
and the general gamma cumulative distribution function for γ(h µ ν) is
F(µ ν; h x) =
1


 µ2h
ν

µ
ν
 µ2h
ν 	 x
0
e−µt
ν t
µ2h
ν −1dt
and here h(dt) = dYt with Yt is also gamma-distributed
dYt = γ(dt µa νa)
The parameter set is therefore  = (µa νa ν θ σ).

CHAPTER 2
The Inference Problem
In applying option pricing models, one always encounters the
difficulty that the spot volatility and the structural parameters are
unobservable.
— Gurdip Bakshi, Charles Cao, and Zhiwu Chen
INTRODUCTION
Regardless of which specific model we are using, it seems that we cannot
avoid the issue of calibration. There are two possible sets of data that we
can use for estimating the model parameters: options prices and historic
stock prices.1
Using options prices via a least-square estimator (LSE) has the obvious
advantage of guaranteeing that we will match the used option market prices
within a certain tolerance. However, the availability of option data is typi-
cally limited, which would force us to use interpolation and extrapolation
methods. These data manipulation approaches might deteriorate the qual-
ity and the smoothness of our inputs. More importantly, matching a set of
plain-vanilla option prices does not necessarily mean that we would obtain
the correct price for an exotic derivative.
Using stock prices has the disadvantage of offering no guarantee of
matching option prices. However, supposing that the model is right, we do
have a great quantity of data input for calibration, which is a powerful
argument in favor of this approach.
It is important, however, to note that in using historic stock prices we
are assuming that our time step t is small enough that we are almost in
1Recently some researchers have also tried to use historic option prices. See, for
instance, Elliott [93] or Van der Merwe [229].
46

The Inference Problem
47
a continuous setting. Further, we are assuming the validity of the Girsanov
theorem, which is applicable to a diffusion-based model. This also means we
are implicitly assuming that the market price of volatility risk is stable and
so are the risk-neutral volatility-drift parameters.
More accurately, having for instance a real-world model
dvt = (ω −θvt)dt + ξvp
t dZt
with p = 0.5 corresponding to the Heston model, we know that the risk-
neutral volatility-drift parameter is
θ(r) = θ + λξvp−1
t
As a result, supposing that θ(r) is a stable (or even constant) parameter
is equivalent to supposing that λ the market-price-of-volatility-risk2 verifies
λ = φv1−p
t
with φ a constant coefficient. The implication of this assumption for a model
with a real-world parameter set  = (ω θ ξ ρ) and a risk-neutral counter-
part (r) = (ω(r) θ(r) ξ(r) ρ(r)) is
ξ = ξ(r)
ρ = ρ(r)
ω = ω(r)
θ = θ(r) −φ
Let us insist on the fact that the above assumption3 is valid only for
a diffusion-based model. For some non-Gaussian pure-jump models, such
as VGG, we lose the comparability between the statistical and the risk-
neutral parameters. We could instead use the stock-price time series to deter-
mine the statistical density p(z) on the one hand, use the options prices to
determine the risk-neutral density q(z) on the other, and calculate the ratio
2Note that many call the market-price-of-volatility-risk the quantity λξvp
t.
3Also as stated by Bakshi, Cao, and Chen [20]: When the risk-aversion coefficient of
the representative agent is bounded within a reasonable range, the parameters of the
true distributions will not differ significantly from their risk-neutral counterparts.
The direct implication of this is θ ≈θ(r). More importantly, for daily data we
have t = o(
√
t) and therefore using either the real-world asset drift µS or the
dividend-adjusted risk-free rate r −q would not make a difference in parameter
estimation. Some [10] even ignore the stock drift term altogether.

48
INSIDE VOLATILITY ARBITRAGE
r(z) = p(z)/q(z) corresponding to the Radon-Nikodym derivative of the
two measures for this model.
The central question of this chapter is therefore the inference of the
parameters embedded in a stochastic volatility model. The logical subdivi-
sions of the problem are summarized as follows.
1. Cross-Sectional vs. Time Series: The former uses options prices at a given
point in time, and the latter a series of the underlying prices for a given
period. As mentioned earlier, the former provides an estimation of the
parameters in the risk-neutral universe and the latter estimation takes
place in the statistical universe.
2. Classical vs. Bayesian: Using time series, one could suppose that there
exists an unknown but fixed set of parameters and try to estimate them
as closely as possible. This is a classical (frequentist) approach. Alterna-
tively, one could use a Bayesian approach, in which the parameters are
supposed to be random variables and have their prior distributions that
one can update via the observations.
3. Learning vs. Likelihood Maximization: Under the classical hypothe-
sis, one could try to estimate the instantaneous variance together with
the fixed parameters, which corresponds to a learning process. A more
robust way would be to estimate the likelihood function and maximize
it over all the possible values of the parameters.
4. Gaussian vs. Non-Gaussian: In any of the preceding approaches, the
stochastic volatility (SV) model could be diffusion based or not. As
we will see further, this will affect the actual estimation methodology.
Among the Gaussian SV models we consider are Heston, GARCH, and
3/2. Among the Non-Gaussian ones are Bates, VGSA, and VGG.
5. State-Space Representation: For each of the above approaches and for
each SV model, we have a number of ways of choosing a state and
represent the instantaneous variance as well as the spot price. Needless
to say, a more parsimonious and lower-dimension state is preferable.
6. Diagnostics and Sampling Distribution: Once the inference process is
finished, one has to verify its accuracy via various tests. Quantities such
as MPE, RMSE, Box-Ljung, or χ2 numbers correspond to some of the
possible diagnostics. Observing the sampling distribution over various
paths is another way of checking the validity of the inference methodol-
ogy.
Finally, it is worth noting that our entire approach is based on parametric
stochastic volatility models. This model class is more restrictive than the non-
or semiparametric; however, it has the advantage of offering the possibility
of a direct interpretation of the resulting parameters.

The Inference Problem
49
USING OPTION PRICES
Using a set of current vanilla option prices, we can perform an LSE and assess
the risk-neutral model parameters. Taking a set of J strike prices Kj’s with
their corresponding option prices Cmkt(Kj ) for a given maturity, we would
try to minimize
J
j=1
(Cmodel(Kj ) −Cmkt(Kj ))2
The minimization4 could, for example, be done via the direction set
(Powell) method, the conjugate gradient (Fletcher-Reeves-Polak-Ribiere)
method, or the Levenberg-Marquardt (LM) method. We will now briefly
describe the Powell optimization algorithm.
Direction Set (Powell) Method
The optimization method we will use later is the direction set (Powell)
method and does not require any gradient or Hessian computation.5 This is a
quadratically convergent method producing mutually conjugate directions.
Most multi dimensional optimization algorithms require a one-dimen-
sional line minimization routine that does the following: Given as input the
vectors P and n and the function f, find the scalar λ that minimizes f(P+λn),
and then replace P with P+λn and n with λn. The idea would be to take a set
of directions that are as noninterfering as possible in order to avoid spoil-
ing one minimization with the subsequent one. This way an interminable
cycling through the set of directions will not occur. This is why we seek con-
jugate directions. Calling the function to be minimized f(x), with x a vector
of dimension N, we can write the second-order Taylor expansion around a
particular point P
f (x) ≈f (P) + ∇f (P)x + 1
2xHx
where Hij =
∂2f
∂xi∂xj is the Hessian matrix of the function at point P. We there-
fore have for the variation of the gradient δ(∇f ) = Hδx, and, in order to
4Some consider that this minimization will give more importance to the ATM
options, and they try therefore to correct by introducing weights into the summa-
tion. There are also entropy-based techniques as discussed in [16] applied to local
volatility models, which are different from our parametric models.
5This is an important feature when the function to be optimized contains disconti-
nuities.

50
INSIDE VOLATILITY ARBITRAGE
have a noninterfering new direction, we choose v such that the motion along
v remains perpendicular to our previous direction u
uδ(∇f ) = uHv = 0
In this case, the directions u and v are said to be conjugate.
Powell suggests a quadratically convergent method that produces a set
of N mutually conjugate directions. The following description is taken from
Press [204], where the corresponding source code could be found as well.
1. Initialize the set of directions ui to the basis vectors for i = 1 ... N
2. Save the starting point as P0
3. Move Pi−1 to the minimum along direction ui and call it Pi
4. Set ui to ui + 1 for i = 1 ... N −1 and set uN to PN −P0
5. Move PN to the minimum along uN and call this point P0, and go back
to Step 2
For a quadratic form, k iterations of this algorithm will produce a set of
directions whose last k members are mutually conjugate. The idea is to repeat
the steps until the function stops decreasing. However, this procedure tends
to produce directions that are linearly dependent and therefore provides us
with the minimum only over a sub space —hence—the idea of discarding the
direction along which f makes the largest decrease. This seems paradoxical;
we are dropping our best direction in the new iteration. However, this is the
best chance of avoiding a buildup of linear dependence.
In what follows we apply the Powell algorithm to SPX options valued
via the mixing Monte Carlo method.
Numeric Tests
We apply the Powell algorithm to SPX options valued via the mixing Monte
Carlo method. The optimization is performed across close-to-the-money
strike prices as of t0
= 05/21/2002 with the index S0 = 1079.88 and
maturities T = 08/17/2002, T = 09/21/2002, T = 12/21/2002, and T
=
03/22/2003 (Figures 2.1 through 2.5).
As we see in Table 2.1, the estimated parameters are fairly stable for
different maturities and therefore the stochastic volatility model seems to be
fairly time homogeneous.
The Distribution of the Errors
Because the parameter set  contains only a few elements and we can have
many options prices, it is clear that the matching of the model and market

The Inference Problem
51
Volatility Surface
700 800 900 100011001200 13001400
1500
Strike Price
0.20.30.40.5
0.6
0.7
0.8
0.9
Time to Maturity
0.1
0.15
0.2
0.25
0.3
0.35
0.4
Implied Volatility
FIGURE 2.1
The S&P 500 Volatility Surface as of 05/21/2002 with Index =
$1079.88. The surface will be used for fitting via the direction set (Powell) opti-
mization algorithm applied to a square-root model implemented with a one-factor
Monte Carlo mixing method.
0
50
100
150
200
250
300
800
850
900
950
1000 1050 1100 1150 1200 1250 1300
Call Price
Strike Price
Volatility Smile Fitting
Market 08/17/2002
Model 08/17/2002
FIGURE 2.2
Mixing Monte Carlo Simulation with the Square-Root Model for SPX
on 05/21/2002 with Index = $1079.88, Maturity 08/17/2002. Powell (direction set)
optimization method was used for least-square calibration. Optimal parameters ˆω =
0.081575, ˆθ = 3.308023, ˆξ = 0.268151, ˆρ = −0.999999.

52
INSIDE VOLATILITY ARBITRAGE
0
50
100
150
200
250
300
350
700
800
900
1000
1100
1200
1300
1400
Call Price
Strike Price
Volatility Smile Fitting
Market 09/21/2002
Model 09/21/2002
FIGURE 2.3
Mixing Monte Carlo Simulation with the Square-Root Model for SPX
on 05/21/2002 with Index = $1079.88, Maturity 09/21/2002. Powell (direction set)
optimization method was used for least-square calibration. Optimal parameters ˆω =
0.108359, ˆθ = 3.798900, ˆξ = 0.242820, ˆρ = −0.999830.
0
50
100
150
200
250
300
350
400
700
800
900
1000
1100
1200
1300
1400
1500
Call Price
Strike Price
Volatility Smile Fitting
Market 12/21/2002
Model 12/21/2002
FIGURE 2.4
Mixing Monte Carlo Simulation with the Square-Root Model for SPX
on 05/21/2002 with Index = $1079.88, Maturity 12/21/2002. Powell (direction
set) optimization method was used for least-square calibration. Optimal parameters
ˆω = 0.126519, ˆθ = 3.473910, ˆξ = 0.222532, ˆρ = −0.999991.

The Inference Problem
53
0
50
100
150
200
250
300
350
400
700
800
900
1000
1100
1200
1300
1400
1500
Call Price
Strike Price
Volatility Smile Fitting
Market 03/22/2003
Model 03/22/2003
FIGURE 2.5
Mixing Monte-Carlo Simulation with the Square-Root Model for SPX
on 05/21/2002 with Index = $1079.88, Maturity 03/22/2003. Powell (direction set)
optimization method was used for least-square calibration. Optimal parameters ˆω =
0.138687, ˆθ = 3.497779, ˆξ = 0.180010, ˆρ = −1.000000.
prices is not perfect. Thus, we observe the distribution of the errors
Cmkt(Kj ) = Cmodel(Kj ˆ) exp

−1
2ϒ2 + ϒN (j) (0 1)

with 1 ≤j ≤J and ϒ the error standard deviation and ˆ the optimal
parameter set. As usual, N(0 1) is the standard normal distribution. Note
that our previously discussed LSE approach is not exactly equivalent to
the maximization of a likelihood function based on the above distribution
TABLE 2.1
The Estimation is Performed for SPX on t = 05/21/2002 with Index
= $1079.88 for Different Maturities T.
T
ˆω
ˆθ
ˆξ
ˆρ
08172002
0.081575
3.308023
0.268151
−0.999999
09212002
0.108359
3.798900
0.242820
−0.999830
12212002
0.126519
3.473910
0.222532
−0.999991
03222003
0.138687
3.497779
0.180010
−1.000000

54
INSIDE VOLATILITY ARBITRAGE
because the latter would correspond to the minimization of the sum of the
squared log returns.
A good bias test would be to check for the predictability of the errors.
For this, one could run a regression of the error
ej = Cmkt(Kj ) −Cmodel(Kj ˆ)
on a few factors corresponding, for instance, to moneyness or maturity. A low
R2 for the regression would prove that the model errors are not predictable
and there is no major bias. For a detailed study, see [182] for instance.
USING STOCK PRICES
The Likelihood Function
If, as in the previous section, we use European options with a given maturity
T and with different strike prices, then we will be estimating
q(ST|S0; )
which corresponds to the risk-neutral density, given a known current stock
price S0 and given a constant parameter set . As discussed, least-squares
estimation (LSE) is used to find the best guess for the unknown ideal param-
eter set. Alternatively, if we use a time series of stock prices (St)0≤t≤T, we
would be dealing with the joint probability
p(S1 ... ST|S0; )
which we can rewrite as
p(S1 ... ST|S0; ) =
T

t=1
p(St|St−1 ... S0; )
It is this joint probability that is commonly referred to as the likelihood
function L0:T(). Maximizing the likelihood over the parameter set  would
provide us with the best parameter set for the statistical density p(ST|S0; ).
Note that we are using a classical (frequentist) approach, in which we
assume that the parameters are unknown but are fixed over [0 T ]. In other
words, we would be dealing with the same parameter set for any of the
p(St|St−1 ... S0; ) with 1 ≤t ≤T.
It is often convenient to work with the log of the likelihood function
since this will produce a sum
ln L0:T() =
T

t=1
ln p(St|St−1 ... S0; )

The Inference Problem
55
The Justification for the MLE
As explained, for instance, in [100], one justifi-
cation of the maximization of the (log) likelihood function comes from the
Kullback-Leibler (KL) distance. The KL distance is defined as6
d(p∗ p) =

p∗(x)

ln p∗(x) −ln p(x)

dx
where p∗(x) is the ideal density, and p(x) is the density under estimation. We
can write
d(p∗ p) = E∗ln

p∗(x)/p(x)

Note that using the Jensen (log convexity) inequality
d(p∗ p) = −E∗ln

p(x)/p∗(x)

≥−ln

E∗(p(x)/p∗(x))

so
d(p∗ p) ≥−ln

p∗(x)p(x)/p∗(x)dx = 0
and d(p p∗) = 0 if and only if p = p∗, which confirms that d(. .) is a distance.
Now minimizing d(p p∗) over p() would be equivalent to minimizing the
term
−

p∗(x) ln p(x)dx
since the rest of the expression depends on p∗() only. This latter expression
could be written in the discrete framework, having T observations S1 ... ST
as
−
T

t=1
ln p(St)
because the observations are by assumption distributed according to the ideal
p∗(). This justifies our maximizing
T

t=1
p(St)
Note that in a pure parameter estimation, this would be the MLE
approach. However, the minimization of the KL distance is more general
and can allow for model identification.
Maximum likelihood estimation has many desirable asymptotic attri-
butes as explained, for example, in [127]. Indeed, ML estimators are consist-
ent and converge to the right parameter set as the number of observations
6Hereafter when the bounds are not specified, the integral is taken on the entire
space of the integrand argument.

56
INSIDE VOLATILITY ARBITRAGE
increases. They actually reach the lower bound for the error, referred to
as the Cramer-Rao bound, which corresponds to the inverse of the Fisher
information matrix.
Calling the first derivative of the log likelihood the score function
h() = ∂ln L0:T()
∂
it is known that MLE could be interpreted as a special case of the general
method of moments (GMM), where the moment g() such that
E[g()] = 0
is simply taken to be the above score function. Indeed we would then have
E[h()] =
 ∂ln L0:T()
∂
L0:T()dz0:T = 0
which means that
 ∂L0:T()
∂
dz0:T = 0
as previously discussed in the MLE.
Note that taking the derivative of the above with respect to the parameter
set (using one-dimensional notations for simplicity)

∂
∂ (h()L0:T()) dz0:T = 0
which will give us
 ∂2 ln L0:T()
∂2
L0:T()dz0:T = −

∂L0:T()
∂
L0:T()
∂L0:T()
∂
dz0:T
= −
 ∂ln L0:T()
∂
	2
L0:T()dz0:T
meaning that
J = −E

∂2 ln L0:T()
∂2

= E
∂ln L0:T()
∂
	2
which is referred to as the information matrix identity. As previously stated,
asymptotically we have for the optimal parameter set ˆ and the ideal ∗
ˆ −∗∼N

0 J −1

The Inference Problem
57
Likelihood Evaluation and Filtering
For GARCH models, the likelihood is known
under an integrated form. Indeed, calling ut the mean-adjusted stock return,
vt the variance, and (Bt) a Gaussian sequence, we have for any GARCH
model
ut = h(vt Bt)
and
vt = f (vt−1 ut−1; )
where f () and h() are two deterministic functions. This will allow us to
directly determine and optimize7
L1:T() ∝−
T

t=1
ln(vt) + u2
t
vt
This is possible because GARCH models have one source of randomness
and there is a time shift between the variance and the spot equations.
Unlike GARCH, most stochastic volatility models have two (imperfectly
correlated) sources of randomness (Bt) and (Zt) and have equations of the
form
ut = h(vt Bt)
vt = f (vt−1 Zt; )
which means that the likelihood function is not directly known under an
integrated form, and we need filtering techniques for its estimation and
optimization.
Another justification for filtering is its application to parameter learning.
As we shall see, in this approach we use the joint distribution of the hidden
state and the parameters. In order to obtain the optimal value of the hidden
state vt given all the observations z1:t, we need to use a filter.
Filtering
The idea here is to use the filtering theory for the estimation of stochastic
volatility model parameters. What we are trying to do is to find the prob-
ability density function (pdf) corresponding to a state xk at time step k given
all the observations z1:k up to that time. Looking for the pdf p(xk|z1:k), we
can proceed in two stages.
7We generally drop constant terms in the likelihood function because they do not
affect the optimal arguments, hence the notation L1:T() ∝....

58
INSIDE VOLATILITY ARBITRAGE
1. First we can write the time update iteration by applying the Chapman-
Kolmogorov equation8
p(xk|z1:k−1) =

p(xk|xk−1 z1:k−1)p(xk−1|z1:k−1)dxk−1
=

p(xk|xk−1)p(xk−1|z1:k−1)dxk−1
by using the Markov property.
2. Following this, for the measurement update we use the Bayes rule
p(xk|z1:k) = p(zk|xk)p(xk|z1:k−1)
p(zk|z1:k−1)
where the denominator p(zk|z1:k−1) could be written as
p(zk|z1:k−1) =

p(zk|xk)p(xk|z1:k−1)dxk
and corresponds to the likelihood function for the time-step k.
Proof:
Indeed we have
p(xk|z1:k) = p(z1:k|xk)p(xk)
p(z1:k)
= p(zk z1:k−1|xk)p(xk)
p(zk z1:k−1)
= p(zk|z1:k−1 xk)p(z1:k−1|xk)p(xk)
p(zk|z1:k−1)p(z1:k−1)
= p(zk|z1:k−1 xk)p(xk|z1:k−1)p(z1:k−1)p(xk)
p(zk|z1:k−1)p(z1:k−1)p(xk)
= p(zk|xk)p(xk|z1:k−1)
p(zk|z1:k−1)
(QED)
Note that we use the fact that at time step k the value of z1:k is perfectly
known.
The Kalman Filter (detailed below) is a special case where the distribu-
tions are normal and could be written as
p(xk|zk−1) = N(ˆx−
k  P −
k )
p(xk|zk) = N(ˆxk Pk)
8See Shreve [218], for instance.

The Inference Problem
59
In the special Gaussian case, each distribution could be entirely charac-
terized via its first two moments. However, it is important to remember that
the Kalman filter (KF) is optimal in the Gaussian linear case. In the nonlinear
case, it will always be suboptimal.
Interpretation of the Kalman Gain
The basic idea behind the KF is the following
observation. Having x a normally distributed random variable with a mean
mx and variance Sxx, having z a normally distributed random variable with
a mean mz and variance Szz, as well as Szx = Sxz the covariance between x
and z, the conditional distribution of x|z is also normal with
mx|z = mx + K(z −mz)
with
K = SxzS−1
zz
Interpreting x as the hidden-state and z as the observation, the above
matrix K would correspond to the Kalman filter in the linear case. We also
have
Sx|z = Sxx −KSxz
An alternative interpretation of the Kalman filter could be based on
linear regression. Indeed, if we knew the time-series of (zk) and (xk), then
the regression could be written as
xk = βzk + α + ϵk
with β the slope, α the intercept, and (ϵk) the residuals. It is known that
under a least-square regression, we have
β = SxzS−1
zz
which again is the expression for the Kalman gain.
We now will describe various nonlinear extensions of the Kalman filter.
The Simple and Extended Kalman Filters
The first algorithms we choose here are the simple and extended Kalman
filters,9 owing to their well-known flexibility and ease of implementation.
The simple or traditional Kalman filter (KF) applies to linear Gaussian cases,
whereas the extended KF (EKF) could be used for nonlinear Gaussian cases
via a first-order linearization. We shall therefore describe EKF and consider
9For a description see, for instance, Welch [233] or Harvey [129].

60
INSIDE VOLATILITY ARBITRAGE
the simple KF as a special case. In order to clarify the notations, let us briefly
rewrite the EKF equations. Given a dynamic process xk following a possibly
nonlinear transition equation
xk = f(xk−1 wk)
(2.1)
we suppose we have a measurement zk via a possibly nonlinear observation
equation
zk = h(xk uk)
(2.2)
where wk and uk are two mutually uncorrelated sequences of temporally
uncorrelated normal random variables with zero means and covariance
matrices Qk, Rk, respectively.10 Moreover, wk is uncorrelated with xk−1 and
uk uncorrelated with xk.
We define the linear a priori process estimate as
ˆx−
k = E[xk]
(2.3)
which is the estimation at time step k −1 prior to measurement. Similarly,
we define the linear a posteriori estimate
ˆxk = E[xk|zk]
(2.4)
which is the estimation at time step k after the measurement.
We also have the corresponding estimation errors e−
k = xk −ˆx−
k and
ek = xk −ˆxk and the estimate error covariances
P−
k = E[e−
k e−t
k ]
(2.5)
Pk = E[eket
k]
(2.6)
where the superscript t corresponds to the transpose operator.
We now define the Jacobian matrices of f with respect to the system
process and the system noise as Ak and Wk respectively. Similarly, we define
the gradient matrices of h with respect to the system process and the meas-
urement noise as Hk and Uk respectively. More accurately, for every row i
and column j we have
Aij =∂fi/∂xj (ˆxk−1 0)
Wij =∂fi/∂wj (ˆxk−1 0)
Hij =∂hi/∂xj (ˆx−
k  0)
Uij =∂hi/∂uj (ˆx−
k  0)
10Some prefer to write xk = f(xk−1 wk−1). Needless to say, the two notations are
equivalent.

The Inference Problem
61
We therefore have the following time update equations
ˆx−
k = f(ˆxk−1 0)
(2.7)
and
P−
k = AkPk−1At
k + WkQk−1Wt
k
(2.8)
We define the Kalman gain as the matrix Kk used in the measurement
update equations
ˆxk = ˆx−
k + Kk(zk −h(ˆx−
k  0))
(2.9)
and
Pk = (I −KkHk)P−
k
(2.10)
where I represents the identity matrix.
The optimal Kalman gain corresponds to the mean of the conditional
distribution of xk upon the observation zk or, equivalently, the matrix that
would minimize the mean square error Pk within the class of linear estima-
tors. This optimal gain is
Kk = P−
k Ht
k(HkP−
k Ht
k + UkRkUt
k)−1
(2.11)
The foregoing equations complete the Kalman filter algorithm.
Another Interpretation of the Kalman Gain
Note that an easy way to observe that
Kk minimizes the a posteriori error covariance Pk is to consider the one-
dimensional linear case
ˆxk = ˆx−
k + Kk(zk −Hk ˆx−
k ) = ˆx−
k + Kk(zk −Hkxk + Hke−
k )
so
ek = xk −ˆxk = e−
k −Kk(uk + Hke−
k )
Therefore
Pk = E(e2
k) = P −
k + K2
k(Rk + H 2
kP −
k + 0) −2KkHkP −
k
and taking the derivative with respect to Kk and setting it to zero, we get
Kk =
P −
k Hk
H 2
kP −
k + Rk
which is the one-dimensional expression for the linear Kalman gain.

62
INSIDE VOLATILITY ARBITRAGE
Residuals, Mean Price Error (MPE) and Root Mean Square Error (RMSE)
In what
follows we shall call the estimated observations ˆz−
k . For the simple and
extended Kalman filters, we have
ˆz−
k = h(ˆx−
k  0)
The residuals are the observation errors, defined as
˜zk = zk −ˆz−
k
Needless to say, the smaller these residuals, the higher the quality of the filter.
Therefore, to measure the performance, we define the mean price error (MPE)
and root mean square error (RMSE) as the mean and standard deviation of
the residuals
MP E = 1
N
N

k=1
˜zk
RMSE =



 1
N
N

k=1
(˜zk −MPE)2
The Unscented Kalman Filter
Recently, Julier and Uhlmann [166] proposed a new extension of the Kalman
filter to nonlinear systems, one that is completely different from the EKF.
They argue that EKF could be difficult to implement and, more importantly,
difficult to tune and that it would be reliable only for systems that are al-
most linear within the update intervals. The new method, called the un-
scented Kalman filter (UKF), will calculate the mean to a higher order of
accuracy than the EKF and the covariance to the same order of accuracy.
Unlike the EKF, this method does not require any Jacobian calculation since
it does not approximate the nonlinear functions of the process and the ob-
servation. Therefore, it uses the true nonlinear models but approximates the
distribution of the state random variable xk by applying an unscented trans-
formation to it. As we will see in the following, we construct a set of sigma
points that capture the mean and covariance of the original distribution and,
when propagated through the true nonlinear system, capture the posterior
mean and covariance accurately to the third order.
Similarly to the EKF, we start with an initial choice for the state vector
ˆx0 = E[x0] and its covariance matrix P0 = E[(x0 −ˆx0)(x0 −ˆx0)t]. We then
concatenate the space vector with the system noise and the observation

The Inference Problem
63
noise11 and create an augmented state vector for each step k greater than
one
xa
k−1 =


xk−1
wk−1
uk−1


and therefore
ˆxa
k−1 =


ˆxk−1
0
0


and
Pa
k−1 =


Pk−1
Pxw(k −1|k −1)
0
Pxw(k −1|k −1)
Pww(k −1|k −1)
0
0
0
Puu(k −1|k −1)


for each iteration k. The augmented state will therefore have a dimension
na = nx + nw + nu.
We then need to calculate the corresponding sigma points through the
unscented transformation:
χa
k−1(0) = ˆxa
k−1
For i = 1 ... na
χa
k−1(i) = ˆxa
k−1 +

(na + λ)Pa
k−1

i
and for i = na + 1 ... 2na
χa
k−1(i) = ˆxa
k−1 −

(na + λ)Pa
k−1

i−na
where the above subscripts i and i −na correspond to the ith and i −nth
a
columns of the square-root matrix.12 This prepares us for the time update
and the measurement update equations, similarly to the EKF.
The time update equations are
χk|k−1(i) = f(χx
k−1(i) χw
k−1(i))
11This space augmentation will not be necessary if we have additive noises as in
xk = f (xk−1) + wk−1 and zk = h(xk) + uk.
12The square-root matrix is calculated via singular value decomposition (SVD) and
Cholesky factorization [204]. In case Pa
k−1 is not positive-definite, one could, for
example, use a truncation procedure.

64
INSIDE VOLATILITY ARBITRAGE
for i = 0 ... 2na + 1 and
ˆx−
k =
2na

i=0
W (m)
i
χk|k−1(i)
and
P−
k =
2na

i=0
W (c)
i
(χk|k−1(i) −ˆx−
k )(χk|k−1(i) −ˆx−
k )t
where the superscripts x and w respectively correspond to the state and
system-noise portions of the augmented state.
The W (m)
i
and W (c)
i
weights are defined as
W (m)
0
=
λ
na + λ
and
W (c)
0
=
λ
na + λ + (1 −α2 + β)
and for i = 1 ... 2na
W (m)
i
= W (c)
i
=
1
2(na + λ)
The scaling parameters α, β, κ and λ = α2(na + κ) −na will be chosen
for tuning.
We also define within the time update equations
Zk|k−1(i) = h(χk|k−1(i) χu
k−1(i))
and
ˆz−
k =
2na

i=0
W (m)
i
Zk|k−1(i)
where the superscript u corresponds to the observation-noise portion of the
augmented state.
As for the measurement update equations, we have
Pzkzk =
2na

i=0
W (c)
i
(Zk|k−1(i) −ˆz−
k )(Zk|k−1(i) −ˆz−
k )t
and
Pxkzk =
2na

i=0
W (c)
i
(χk|k−1(i) −ˆx−
k )(Zk|k−1(i) −ˆz−
k )t

The Inference Problem
65
which gives us the Kalman gain
Kk = PxkzkP−1
zkzk
and we get as before
ˆxk = ˆx−
k + Kk(zk −ˆz−
k )
where again zk is the observation at time (iteration) k. Also, we have
Pk = P−
k −KkPzkzkKt
k
which completes the measurement update equations.
Kushner’s Nonlinear Filter
It would be instructive to compare this algorithm to the nonlinear filter-
ing algorithm based on an approximation of the conditional distribution by
Kushner et al. [174]. In this approach, the authors suggest using a Gaussian
quadrature in order to calculate the integral at the measurement update (or
the time update) step.13 As the Kushner paper indicates, having an
N-dimensional normal random variable X = N(m P), with m and P the
corresponding mean and covariance, for a polynomial G of degree 2M −1,
we can write14
E[G(X)] =
1
(2π)
N
2 |P|
1
2

G(y) exp

−(y −m)tP−1(y −m)
2

dy
which is equal to
E[G(X)] =
M

i1=1
...
M

iN=1
wi1...wiNG

m +
√
Pζ

where ζt = (ζi1 ... ζiN) is the vector of the Gauss-Hermite roots of order
M and wi1 ... wiN are the corresponding weights. Note that even if both
Kushner’s NLF and UKF use Gaussian qadratures, UKF only uses 2N + 1
sigma points, whereas NLF needs MN points for the integral computation.
Kushner and Budhiraja suggest using this technique primarily for the
measurement update (filtering) step. They claim that provided this step is
properly implemented, the time update (prediction) step can be carried out
via a linearization similar to the EKF.
13The analogy between Kushner’s nonlinear filter and the unscented Kalman filter,
has already been studied in Ito & Xiong [151].
14A description of the Gaussian quadrature can be found in Press et al. [204].

66
INSIDE VOLATILITY ARBITRAGE
Details of the Kushner algorithm
Let us use the same notations as for the UKF
algorithm. We therefore have the augmented state xa
k−1 and its covariance
Pa
k−1 as before. Here, for a quadrature order of M on an N-dimensional
variable, the sigma points are defined for j = 1 ... N and ij = 1 ... M as
χa
k−1(i1 ... iN) = ˆxa
k−1 +

Pa
k−1ζ(i1 ... iN)
where the square root here corresponds to the Cholesky factorization, and
again ζ(i1 . . .  iN)[j] = ζij for each j between 1 and the dimension N and
each ij between 1 and the quadrature order M. Similarly to the UKF, we
have the time update equations
χk|k−1(i1 ... iN) = f

χx
k−1(i1 ... iN) χw
k−1(i1 ... iN)

but now
ˆx−
k =
M

i1=1
...
M

iN=1
wi1...wiNχk|k−1(i1 ... iN)
and
P−
k =
M

i1=1
...
M

iN=1
wi1...wiN(χk|k−1(i1 ... iN) −ˆx−
k )(χk|k−1(i1 ... iN) −ˆx−
k )t
Again, we have
Zk|k−1(i1 ... iN) = h

χk|k−1(i1 ... iN) χu
k−1(i1 ... iN)

and
ˆz−
k =
M

i1=1
...
M

iN=1
wi1...wiNZk|k−1(i1 ... iN)
Therefore, the measurement update equations will be
Pzkzk =
M

i1=1
...
M

iN=1
wi1...wiN(Zk|k−1(i1 ... iN) −ˆz−
k )(Zk|k−1(i1 ... iN) −ˆz−
k )t
and
Pxkzk =
M

i1=1
...
M

iN=1
wi1...wiN(χk|k−1(i1 ... iN) −ˆx−
k )(Zk|k−1(i1 ... iN) −ˆz−
k )t

The Inference Problem
67
which gives us the Kalman gain
Kk = PxkzkP−1
zkzk
and we get as before
ˆxk = ˆx−
k + Kk(zk −ˆz−
k )
where again zk is the observation at time (iteration) k.
Also, we have
Pk = P−
k −KkPzkzkKt
k
which completes the measurement update equations.
When N = 1 and λ = 2, the numeric integration in the UKF will corres-
pond to a Gauss-Hermite quadrature of order M = 3. However, in the UKF
we can tune the filter and reduce the higher term errors via the previously
mentioned parameters α and β.
Note that when h(x u) is strongly nonlinear, the Gauss Hermite integra-
tion is not efficient for evaluating the moments of the measurement update
equation, since the term p(zk|xk) contains the exponent zk −h(xk uk). The
iterative methods based on the idea of importance sampling proposed in
[174] correct this problem at the price of a strong increase in computation
time. As suggested in [151], one way to avoid this integration would be to
make the additional hypothesis that xk h(xk uk)|z1:k−1 is Gaussian.
Parameter Learning
One important issue to realize is that the Kalman filter can be used either for
state estimation (filtering) or for parameter estimation (machine learning).
When we have both state estimation and parameter estimation, we are deal-
ing with a dual estimation or a joint estimation. The latter case is the one
concerning us because we are estimating the state volatility as well as the
model parameters. As explained in Haykin’s book [133], in a dual filter we
separate the state vector from the parameters and we apply two intertwined
filters to them. By contrast, in a joint filter, we concatenate the state vector
and the parameters and apply one filter to this augmented state. Note that
in the dual filter we need to compute recurrent derivatives with respect to
parameters, whereas in a joint filter no such step is needed.
It is possible to interpret the joint filter in the following way. In a regular
filter, that is, filtering of the state xk for a fixed set of parameters 0, we are
maximizing the conditional density
p(x1:k|z1:k 0)

68
INSIDE VOLATILITY ARBITRAGE
and as we said, to do that we write
p(x1:k|z1:k 0) = p(z1:k|x1:k 0)p(x1:k|0)
p(z1:k|0)
so we maximize the above with respect to the state xk for a given set of
parameters. This means that the optimal state ˆx1:k for a given parameter set
is given by
ˆx1:k = argmax[p(z1:k x1:k|0)]
As we will see, in an MLE approach we use this optimal state filtering
for each iteration of the likelihood maximization over the parameter set .
In a joint filter, we are directly optimizing the joint conditional density
p(x1:k |z1:k)
which we can also write as
p(x1:k |z1:k) = p(z1:k|x1:k )p(x1:k|)p()
p(z1:k)
given that the denominator is functionally independent of x1:k and , and
given that p() contains no prior information,15 the maximization will be
upon
p(z1:k|x1:k )p(x1:k|) = p(z1:k x1:k|)
That is to say, in a joint filter, the optimal state ˆx1:k and parameter set ˆ
are found by writing
(ˆx1:k ˆ) = argmax [p(z1:k x1:k|)]
In what follows, we apply the joint EKF methodology to a few examples.
An Illustration
Before using this technique for the stochastic volatility model,
let us take a simple example
ξk = ξk−1 + π + 0.10wk
and
zk = ξk + 0.10uk
where π ≈3.14159 and wk, uk are independent Gaussian random variables.
The linear state-space system could be written as
xk =
ξk
πk
	
=
1
1
0
1
	
xk−1 + 0.10
wk
0
	
15Again, we are in a frequentist framework, not Bayesian.

The Inference Problem
69
1.8
2
2.2
2.4
2.6
2.8
3
3.2
3.4
0
2
4
6
8
10
12
14
Observations
Joint Filter
pi[k]
pi
FIGURE 2.6
A Simple Example for the Joint Filter. The convergence toward the con-
stant parameter π happens after a few iterations.
and
zk = (1 0) xk + 0.10uk
We choose the initial values ξ0 = z0 = 0 and π0 = 1.0. We also take Q
= 0.1I2 and R = 0.10. Applying the Kalman filter to an artificially generated
data set, we plot the resulting πk in Figure 2.6. As we can see, the parameter
converges very quickly to its true value.
Even if we associated a noise of 0.10 to the constant parameter π, we can
see that for 5000 observations, taking the mean of the filtered state between
observations 20 and 5000 we get
ˆπ = 3.141390488
which is very close to the value 3.14159 used in data generation process.
Joint Filtering Examples
After going through this simple example, we now
apply the JF technique to our stochastic volatility problem. We shall study a
few examples in order to find the best state-space representation.
Example 1 Our first example would be the square-root stochastic volatil-
ity model
ln Sk = ln Sk−1 +

µS −1
2vk−1
	
t + √vk−1
√
tBk−1
vk = vk−1 + (ω −θvk−1)t + ξ√vk−1
√
tZk−1

70
INSIDE VOLATILITY ARBITRAGE
To simplify we suppose that the value of µS is known. We can now define
the state variable16
xk =


ln Sk
vk
ω
θ
ξ
ρ


and the system noise
wk =
Bk
Zk
	
with its covariance matrix
Qk =
1
ρ
ρ
1
	
and therefore
xk = f(xk−1 wk−1) =


ln Sk−1 + (µS −1
2vk−1)t + √vk−1
√
tBk−1
vk−1 + (ω −θvk−1)t + ξ√vk−1
√
tZk−1
ω
θ
ξ
ρ


and therefore the Jacobian Ak is
Ak =


1
−1
2t
0
0
0
0
0
1 −θt
t
−vk−1t
0
0
0
0
1
0
0
0
0
0
0
1
0
0
0
0
0
0
1
0
0
0
0
0
0
1


and
Wk =


√vk−1
√
t
0
0
ξ√vk−1
√
t
0
0
0
0
0
0
0
0


16In reality we should write the estimation parameters ωk, θk, ξk, and ρk. However,
we drop the indexes for simplifying the notations.

The Inference Problem
71
0
0.5
1
1.5
2
2.5
3
3.5
4
0
200
400
600
800
1000
1200
1400
Omega
Days
Extended Kalman Filter
Historic Parameter
FIGURE 2.7
The EKF Estimation (Example 1) for the Drift Parameter ω. The SPX
index daily close prices were used over five years from 10/01/1996 to 09/28/2001.
The convergence is fairly good.
having the measurement zk = ln Sk we can write
Hk =
1
0
0
0
0
0
and Uk = 0.
We could, however, introduce a measurement noise R corresponding to
the intraday stock price movements and the bid-ask spread, in which case we
would have zk = ln Sk + Rϵk, where ϵk represents a sequence of uncorrelated
standard normal random variables. This means that Rk = R and Uk = 1. We
can then tune the value of R in order to get more stable results (Figures 2.7
through 2.10).
Example 2 The same exact methodology could be used in the GARCH
framework. We define the state variable xt
k = (ln Sk vk ω0 α β c) and take
for observation the logarithm of the actual stock price Sk. The system could
be written as
xk = f(xk−1 wk−1)

72
INSIDE VOLATILITY ARBITRAGE
0
2
4
6
8
10
12
14
0
200
400
600
800
1000
1200
1400
Theta
Days
Extended Kalman Filter
Historic Parameter
FIGURE 2.8
The EKF Estimation (Example 1) for the Drift Parameter θ. The SPX
index daily close prices were used over five years from 10/01/1996 to 09/28/2001.
The convergence is fairly good.
0
0.02
0.04
0.06
0.08
0.1
0.12
0.14
0.16
0.18
0
200
400
600
800
1000
1200
1400
XI
Days
Extended Kalman Filter
Historic Parameter
FIGURE 2.9
The EKF Estimation (Example 1) for the Volatility-of-Volatility Param-
eter ξ. The SPX index daily close prices were used over five years from 10/01/1996
to 09/28/2001. The convergence is rather poor. We shall explain this via the concept
of observability.

The Inference Problem
73
–0.25
–0.2
–0.15
–0.1
–0.05
0
0.05
0.1
0
200
400
600
800
1000
1200
1400
Rho
Days
Extended Kalman Filter
Historic Parameter
FIGURE 2.10
The EKF Estimation (Example 1) for the correlation parameter ρ.
The SPX index daily close prices were used over five years from 10/01/1996 to
09/28/2001. The convergence is rather poor. We shall explain this via the concept of
observability.
with wk = Bk a one-dimensional source of noise with a variance Qk = 1 and
f(xk−1 wk−1) =


ln Sk−1 +

µS −1
2vk−1

+ √vk−1Bk−1
ω0 + βvk−1 + α(Bk−1 −c√vk−1)2
ω0
α
β
c


and the Jacobian
Ak =


1
−1
2
0
0
0
0
0
β + αc2
1
c2vk−1
vk−1
2αcvk−1
0
0
1
0
0
0
0
0
0
1
0
0
0
0
0
0
1
0
0
0
0
0
0
1



74
INSIDE VOLATILITY ARBITRAGE
and
Wk =


√vk−1
−2αc√vk−1
0
0
0
0


The observation zk will be
zk = h(xk) = ln(Sk)
exactly as in the previous example. The rest of the algorithm would therefore
be identical to the one included in Example 1.
Example 3 In Examples 1 and 2, we included all the variables in the
system process and we observed part of the system. It is also possible to
separate the measurement and the system variables as follows.
Taking a general discrete stochastic volatility process as17
ln Sk = ln Sk−1 +

µS −1
2vk
	
t + √vk
√
tBk
vk = vk−1 + b(vk−1)t + a(vk−1)
√
tZk
with Bk and Zk two Normal random sequences with a mean of zero and
variance one, with a correlation equal to ρ.
Posing yk = √vkZk and performing the usual Cholesky factorization
Bk = ρZk +

1 −ρ2Xk, where Zk and Xk are uncorrelated, we can now
take the case of a square-root process and write
xk =


vk
yk
ω
θ
ξ
ρ


and xk = f(xk−1 Zk) with
f(xk−1 Zk) =


vk−1 + (ω −θvk−1)t + ξ√vk−1
√
tZk

vk−1 + (ω −θvk−1)t + ξ√vk−1
√
tZk
1
2 Zk
ω + QZk
θ + QZk
ξ + QZk
ρ + QZk


17Note that the indexing here is slightly different from the previous examples.

The Inference Problem
75
which provides us with the Jacobian
Ak =


1 −θt
0
t
−vk−1t
0
0
0
0
0
0
0
0
0
0
1
0
0
0
0
0
0
1
0
0
0
0
0
0
1
0
0
0
0
0
0
1


and
Wk =


ξ√vk−1
√
t
(vk−1 + (ω −θvk−1)t)
1
2
Q
Q
Q
Q


The measurement equation is
zk = ln
 Sk
Sk−1
	
=

µS −1
2vk
	
t + ρ
√
tyk +

1 −ρ2√vk
√
tXk
and therefore
Hk =

−1
2t
ρ
√
t
0
0
0
0

with uk = Xk and Uk =

1 −ρ2√vk
√
t, which completes our set of equa-
tions. Again we could tune the system noise Q in order to obtain more stable
results.
Observability
From the preceding tests, it seems that the EKF provides us with
a nonrobust calibration methodology. Indeed the results are very sensitive
to the choice of system noise Q and observation noise R. We chose for this
case Q = 10−3 and R ≈0.
This brings to attention the issue of observability. A nonlinear system
with a state vector xk of dimension n is observable if
O =


H
HA
HA2
...
HAn−1


has a full rank of n. For an explanation, refer to Reif et al. [205].

76
INSIDE VOLATILITY ARBITRAGE
It is fairly easy to see that among the foregoing examples, the first and
third (corresponding to the stochastic volatility formulation) have for the
observation matrix O a rank of four and therefore are not observable. This
explains why they do not converge well and are so sensitive to the tuning
parameters Q and R. This means that the choices of the state variables for
Examples 1 and 3 were rather poor. One reason is that in our state-space
choice, we considered
zk = h(vk−1 ...)
and
xk = (... vk ...) = f (xk−1 ...)
which implies that
∂h
∂vk
= 0
We shall see how to correct this in the next section by choosing a more
appropriate state-space representation.
The One-Dimensional State within the Joint Filter
Considering the state equation
vk = vk−1 + (ω −θvk−1)t + ξ√vk−1
√
tZk−1
−ρξ

ln Sk−1 +

µS −1
2vk−1
	
t + √vk−1
√
tBk−1 −ln Sk

posing for every k
˜Zk =
1

1 −ρ2 (Zk −ρBk)
we will have as expected ˜Zk uncorrelated with Bk. Therefore, considering
the augmented state
xk =


vk
ω
θ
ξ
ρ


we will have the state transition equation
f(xk−1 ˜Zk−1)
=


vk−1 + [(ω −ρξµS) −

θ −1
2 ρξ

vk−1]t + ρξ ln

Sk
Sk−1

+ ξ

1 −ρ2√vk−1
√
t ˜Zk−1
ω
θ
ξ
ρ



The Inference Problem
77
and the measurement equation would be
zk = ln Sk+1 = ln Sk +

µS −1
2vk
	
t + √vk
√
tBk
The corresponding EKF Jacobians for this system are
Ak =


1 −

θ −1
2 ρξ

t
t
−vk−1t
ρ

ln

Sk
Sk−1

−

µS −1
2 vk−1

t

ξ

ln

Sk
Sk−1

−

µS −1
2 vk−1

t

0
1
0
0
0
0
0
1
0
0
0
0
0
1
0
0
0
0
0
1


Wk =


ξ

1 −ρ2√vk−1
√
t
0
0
0
0


Hk =

−1
2t
0
0
0
0

Uk = √vk
√
t
It is easy to check that this system is observable since the observation matrix
Ok is of full rank. This shows that our state-space choice is better than the
previous ones.
The UKF would be implemented in a fashion similar to that of the tran-
sition and observation equations above. Again, for the UKF, we would not
need to compute any Jacobians.
An important issue to consider is that of tuning. We could add extra
noise to the observation and hence lower the weight associated with the
observations. In which case, after choosing a tuning parameter R, we would
write
Uk =
√vk
√
t
R

and
UkUt
k = vkt + R2
The choice of the initial conditions and the tuning parameters could make
the algorithm fail or succeed. It therefore seems that there is little robustness
in this procedure.
We consider the example of 5000 data points artificially produced via a
Heston stochastic volatility process with a parameter set
∗= (ω = 0.10 θ = 10.0 ξ = 0.03 ρ = −0.50)

78
INSIDE VOLATILITY ARBITRAGE
0.3
0.4
0.5
0.6
0.7
0.8
0.9
0
500
1000
1500
2000
2500
Days
Joint EKF
omega
FIGURE 2.11
Joint EKF Estimation for the Parameter ω. Prices were simulated with
∗= (0.10 10.0 0.03 −0.50). The convergence remains mediocre. We shall explain
this in the following section.
with a given µS = 0.025 . We then choose a tuning parameter R = 0.10 and
take a reasonable guess for the initial conditions
0 = (ω0 = 0.15 θ0 = 10.0 ξ0 = 0.02 ρ0 = −0.51)
and apply the joint filter. The results are displayed in Figures 2.11 to 2.14.
As we can see, the convergence for ω and θ is better than it was for the two
others. We shall see later why this is.
Allowing a burn-in period of 1000 points, we can calculate the mean
(and the standard deviation) of the generated parameters, after the simula-
tion 1000.
Joint Filters and Time Interval
One difficulty with the application of the joint
filter (JF) to the stochastic volatility problem is the following: Unless we are
dealing with a longer time interval, such as t = 1, the observation error
√vk
√
tBk is too large compared with the sensitivity of the filter with respect
to the state through −0.5vkt. Indeed, for a t = 1/252 we have18
t = o(
√
t)
18Hereafter xh = o(yh) means xh/yh →0 as h →0, or, more intuitively, xh is much
smaller than yh for a tiny h.

The Inference Problem
79
9.965
9.97
9.975
9.98
9.985
9.99
9.995
10
10.005
0
500
1000
1500
2000
2500
Days
Joint EKF
theta
FIGURE 2.12
Joint EKF Estimation for the Parameter θ. Prices were simulated with
∗= (0.10 10.0 0.03 −0.50). The convergence remains mediocre. We shall explain
this in the following section.
-0.01
0
0.01
0.02
0.03
0.04
0.05
0.06
0.07
0.08
0.09
0
500
1000
1500
2000
2500
Days
Joint EKF
xi
FIGURE 2.13
Joint EKF Estimation for the Parameter ξ. Prices were simulated with
∗= (0.10 10.0 0.03 −0.50). The convergence remains mediocre. We shall explain
this in the following section.
A simple Monte Carlo test will allow us to verify this. We simulate
a Heston model and another model in which we multiply both Brownian

80
INSIDE VOLATILITY ARBITRAGE
–0.502
–0.501
–0.5
–0.499
–0.498
–0.497
–0.496
–0.495
–0.494
0
500
1000
1500
2000
2500
Days
Joint EKF
rho
FIGURE 2.14
Joint EKF Estimation for the Parameter ρ. Prices were simulated with
∗= (0.10 10.0 0.03 −0.50). The convergence remains mediocre. We shall explain
this in the following section.
motions by a factor t. This will make the errors smaller by a factor of 252 for
the daily case. We call this model the modified model. After generating 5000
data points with a parameter set (ω∗= 0.10 θ∗= 10.0 ξ∗= 0.03 ρ∗= −0.50)
and a drift µS = 0.025, we suppose we know all parameters except ω.
We then apply the JKF to find the estimate ˆω. We can observe in
Figure 2.15 that the filter diverges when applied to the Heston model but
converges fast when applied to the modified model. However, in reality we
have no control over the observation error, which is precisely the volatility!
In a way, this brings up a more fundamental issue regarding the stochastic
volatility estimation problem: By definition, volatility represents the noise of
the stock process. If we had taken the spot price Sk as the observation and
the variance vk as the state, we would have
Sk = Sk−1 + Sk−1µSt + Sk−1
√vk
√
tBk
we would then have an observation function gradient H = 0 and the system
would be unobservable! It is precisely because we use a Taylor second-order

The Inference Problem
81
–0.5
–0.4
–0.3
–0.2
–0.1
0
0.1
0.2
0.3
0.4
0.5
0
50
100
150
200
0.10
JKF / Heston
JKF / Modified SV
FIGURE 2.15
Joint EKF Estimation for the Parameter ω Applied to the Heston Model
as Well as to a Modified Model Where the Noise is Reduced by a Factor 252. As
we can see, the convergence for the modified model is improved dramatically. This
justifies our comments on large observation error.
expansion
ln(1 + R) ≈R −1
2R2
that we obtain access to vk through the observation function. However, the
error remains dominant as the first order of the expansion.
Some [130] have tried
ln

ln2( Sk
Sk−1
)
	
≈ln(vk) + ln(t) + ln(B2
k)
and
ln(B2
k) ∼−1.27 + π
√
2
N(0 1)
but the latter approximation may or may not be valid depending on the
problem under study.
Parameter Estimation via MLE
As previously stated, one of the principal methods of estimation under the
classical framework is the maximization of the likelihood. Indeed this
estimation method has many desirable asymptotic properties. Therefore,

82
INSIDE VOLATILITY ARBITRAGE
instead of using the filters alone, we could separate the parameter set
 = (ω θ ξ ρ) from the state vector (ln Sk vk) and use the Kalman filter
for state filtering within each MLE iteration19 and estimate the parameters
iteratively.
An Illustration
Let us first consider the case of the previous illustration
ξk = ξk−1 + π + 0.10wk
and
zk = ξk + 0.10uk
where π ≈3.14159 and wk, uk are independent Gaussian random variables.
Here we take
xk = ξk
and
Ak = Hk = 1
Wk = Uk = 0.1
The maximization of the Gaussian likelihood with respect to the parameter
π is equivalent to minimizing
L1:N =
N

k=1

ln(Fk) + ˜z2
k
Fk

with residuals
˜zk = zk −ˆz−
k = zk −ˆx−
k
and
Fk = Pzkzk = HkP −
k H t
k + UkRkU t
k
Note that we used scalar notations here, and in vectorial notations we
would have
L1:N =
N

k=1

ln(|Fk|) + ˜zt
kF−1
k ˜zk

where |Fk| is the determinant of Fk. We use the scalar notations for simplicity
and also because in the stochastic volatility problem we usually deal with
one-dimensional observations (namely, the stock price).
19To be more accurate, since the noise process is conditionally Gaussian, we are
dealing with a quasi-maximum-likelihood (QML) Estimation. More detail can be
found, for instance, in Gourieroux [124].

The Inference Problem
83
The minimization via a direction set (Powell) method over 500 artificially
generated observation points will provide
ˆπ = 3.145953
very quickly.
Stochastic Volatility Examples
For Example 1, the system state vector now
becomes
xk =
ln Sk
vk
	
which means the dimension of our state is now two, and
xk = f(xk−1 wk−1) =
ln Sk−1 +

µS −1
2vk−1

t + √vk−1
√
tBk−1
vk−1 + (ω −θvk−1)t + ξ√vk−1
√
tZk−1
	
The system noise is still
wk =
Bk
Zk
	
and the corresponding covariance matrix is
Qk =
1
ρ
ρ
1
	
We have the measurement zk = ln Sk, and therefore we can write
Hk =
1
0
Now for a given set of parameters (ω θ ξ ρ) we can filter this system with
the EKF (or the UKF) using
Ak =

1
−1
2t
0
1 −θt
	
and
Wk =
√vk−1
√
t
0
0
ξ√vk−1
√
t
	
Note that the observation matrix is
Ok =
1
0
1
−1
2t
	
which is of full rank. Our system is therefore observable.

84
INSIDE VOLATILITY ARBITRAGE
6.66
6.665
6.67
6.675
6.68
6.685
6.69
6.695
6.7
6.705
100
105
110
115
120
Log Stock Price
Days
Market
EKF
UKF
FIGURE 2.16
The SPX Historic Data (1996–2001) is Filtered via EKF and UKF. The
results are very close, however, the estimated parameters
ˆ
 = ( ˆω ˆθ ˆξ ˆρ) differ.
Indeed we find ( ˆω = 0.073028 ˆθ = 1.644488 ˆξ = 0.190461 ˆρ = −1.000000) for
the EKF and ( ˆω = 0.540715 ˆθ = 13.013577 ˆξ = 0.437523 ˆρ = −1.000000) for
the UKF. This might be due to the relative insensitivity of the filters to the parameter
set  or the non-uniqueness of the optimal parameter set. We shall explain this low
sensitivity in more detail.
After filtering for this set of parameters, we calculate the sum to be
minimized
φ(ω θ ξ ρ) =
N

k=1

ln(Fk) + ˜z2
k
Fk

with
˜zk = zk −h(ˆx−
k  0)
and
Fk = HkP−
k Ht
k + UkRkUt
k
The minimization could once again be done via a direction set (Powell)
method, as described previously. This will avoid a calculation of the gra-
dient ∇φ.
It is interesting to observe (cf. Figures 2.16 and 2.17) that the results
of the EKF and UKF are very close and the filter errors are comparable.

The Inference Problem
85
0
1e-05
2e-05
3e-05
4e-05
5e-05
6e-05
7e-05
8e-05
9e-05
0.0001
500
550
600
650
700
Filter Error
Days
EKF
UKF
FIGURE 2.17
EKF and UKF Absolute Filtering-Errors for the Same Time-Series. As
we can see, there is no clear superiority of one algorithm over the other.
However, the estimated parameter set  = (ω θ ξ ρ) can have a different
set of values depending on which filter is actually used.20
This leads us to the question, how sensitive are these filters to ? In
order to answer, we can run an estimation for EKF and use the estimated
parameters in UKF and observe how good a fit we obtain. The results show
that this sensitivity is fairly low. Again, this might be due to the relative
insensitivity of the filters to the parameter set  or the non-uniqueness of
the optimal parameter set. As we will see, the answer to this question also
depends on the sample size.
Optimization Constraints for the Square Root Model
In terms of the optimization
constraints, in addition to the usual
ω ≥0
(2.12)
θ ≥0
ξ ≥0
−1 ≤ρ ≤1
20Note, however, that the values of the resulting long-term volatilities
 ω
θ are rather
close.

86
INSIDE VOLATILITY ARBITRAGE
we need to make sure that the value of the variance remains positive; that is,
vk + (ω −θvk)t + ξ√vk
√
tZk ≥0
for any vk ≥0 and any Gaussian random value Zk. For a Gaussian random
variable Zk and any positive real number Z∗, we can write Zk ≥−Z∗with a
probability P ∗. For instance if Z∗= 4 then P ∗= 0.999968. Therefore, fixing
a choice of Z∗, it is almost always enough for us to have
vk + (ω −θvk)t −ξ√vk
√
tZ∗≥0
for any vk ≥0.
Considering the function f (x) = x + (ω −θx)t −ξ√x
√
tZ∗, it is
fairly easy to see that f (0) = ωt ≥0 by assumption, and for x very large
f (x) ≈(1 −θt)x, which is positive if
θ ≤1
t
(2.13)
This is most of the time realized for a small t such as ours.
Now f (x) being a continuous function and having positive values at
zero and infinity, it would be sufficient to make sure that its one minimum
on [0 +∞] is also positive. A simple derivative computation shows that
xmin = ξ2t(Z∗)2
4(1−θt)2 and therefore the positivity is realized if 21
ξ ≤2
Z∗

ω(1 −θt)
(2.14)
which completes our set of constraints.
An Alternative Implementation
We could also perform the same estimation, but
based on our previous third example. Again we have
ln Sk = ln Sk−1 +

µS −1
2vk
	
t + √vk
√
tBk
vk = vk−1 + (ω −θvk−1)t + ξ√vk−1
√
tZk
with Bk and Zk two normal random sequences with a mean of zero, a variance
of one, and a correlation equal to ρ. However, since for a Kalman filter the
process noise and the measurement noise must be uncorrelated, we introduce
yk = √vkZk
21Naturally we suppose that t > 0.

The Inference Problem
87
and performing the usual Cholesky factorization Bk = ρZk +

1 −ρ2Xk,
where Zk and Xk are uncorrelated, we can write
xk =
vk
yk
	
and xk = f(xk−1 Zk) with
f(xk−1 Zk) =

vk−1 + (ω −θvk−1)t + ξ√vk−1
√
tZk
(vk−1 + (ω −θvk−1)t + ξ√vk−1
√
tZk)
1
2 Zk

which provides us with the Jacobian
Ak =
 1 −θt
0
0
0
	
and
Wk =

ξ√vk−1
√
t
(vk−1 + (ω −θvk−1)t)
1
2

The measurement equation is
zk = ln Sk = ln Sk−1 +

µS −1
2vk
	
t + ρ
√
tyk +

1 −ρ2√vk
√
tXk
and therefore
Hk =

−1
2t
ρ
√
t

with uk = Xk and Uk =

1 −ρ2√vk
√
t which completes our set of equa-
tions. Note that the observation matrix is
Ok =

−1
2t
ρ
√
t
−1
2t(1 −θt)
0
	
which is of full rank. Our system is therefore observable.
The One-Dimensional State
Finally, a simpler way of writing the state-space
system, which will be our method of choice hereafter, would be to subtract
from both sides of the state equation xk = f (xk−1 wk−1) a multiple of the
quantity h(xk−1 uk−1) −zk−1, which is equal to zero. This would allow us to
eliminate the correlation between the system and the measurement noises.
In fact, if the system equation is
ln Sk = ln Sk−1 +

µS −1
2vk−1
	
t + √vk−1
√
tBk−1

88
INSIDE VOLATILITY ARBITRAGE
vk = vk−1 + (ω −θvk−1)t + ξ√vk−1
√
tZk−1
writing
vk = vk−1 + (ω −θvk−1)t + ξ√vk−1
√
tZk−1
−ρξ

ln Sk−1 +

µS −1
2vk−1
	
t + √vk−1
√
tBk−1 −ln Sk

posing for every k
˜Zk =
1

1 −ρ2 (Zk −ρBk)
we will have as expected ˜Zk uncorrelated with Bk and
xk = vk = vk−1 +

(ω −ρξµS) −

θ −1
2ρξ
	
vk−1

t
+ ρξ ln
 Sk
Sk−1
	
+ ξ

1 −ρ2√vk−1
√
t ˜Zk−1
(2.15)
and the measurement equation would be
zk = ln Sk+1 = ln Sk +

µS −1
2vk
	
t + √vk
√
tBk
(2.16)
With this system everything becomes one-dimensional and the computations
become much faster both for the EKF and UKF.
For the EKF we will have
Ak = 1 −

θ −1
2ρξ
	
t
and
Wk = ξ

1 −ρ2√vk−1
√
t
as well as
Hk = −1
2t
and
Uk = √vk
√
t
Again, for the MLE we will try to minimize
φ(ω θ ξ ρ) =
N

k=1

ln(Fk) + ˜z2
k
Fk


The Inference Problem
89
with residuals
˜zk = zk −h(ˆx−
k  0)
and
Fk = HkP−
k Ht
k + UkUt
k
The same time update and measurement update will be used with the UKF.
The ML estimator can be used as usual.
The following is a C++ routine for the implementation of the EKF applied
to the Heston model:
// log_stock_prices
are the log of stock prices
// muS is the real-world stock drift
// n_stock_prices is the number of the above stock prices
// (omega, theta, xi, rho) are the Heston parameters
// u[] is the set of means of observation errors
// v[] is the set of variances of observation errors
// estimates[] are the estimated observations from the filter
void estimate_extended_kalman_parameters_1_dim(
double *log_stock_prices,
double muS,
int n_stock_prices,
double omega,
double theta,
double xi,
double rho,
double *u,
double *v,
double *estimates)
{
int i1;
double
x, x1, W, H, A;
double
P, P1, z, U, K;
double delt=1.0/252.0;
double eps=0.00001;
x = 0.04;
P=0.01;
u[0]=u[n_stock_prices-1]=0.0;
v[0]=v[n_stock_prices-1]=1.0;
estimates[0]=estimates[1]=log_stock_prices[0]+eps;
for (i1=1;i1<n_stock_prices-1;i1++)
{
if (x<0) x=0.00001;

90
INSIDE VOLATILITY ARBITRAGE
x1 = x + ( omega-rho*xi*muS - (theta-0.5*rho*xi) * x) * delt +
rho*xi* (log_stock_prices[i1]-log_stock_prices[i1-1]);
A
= 1.0-(theta-0.5*rho*xi)*delt;
W
= xi*sqrt((1-rho*rho) * x * delt);
P1 = W*W + A*P*A;
if (x1<0) x1=0.00001;
H = -0.5*delt;
U = sqrt(x1*delt);
K = P1*H/( H*P1*H + U*U);
z = log_stock_prices[i1+1];
x = x1 + K * (z - (log_stock_prices[i1] + (muS-0.5*x1)*delt));
u[i1] = z - (log_stock_prices[i1] + (muS-0.5*x1)*delt);
v[i1] = H*P1*H + U*U;
estimates[i1+1] = log_stock_prices[i1] + (muS-0.5*x1)*delt;
P=(1.0-K*H)*P1;
}
}
// Having u[] and v[] we can evaluate the (minus log) Likelihood
as
// the sum of
log(v[i1])+u[i1]*u[i1]/v[i1]
// and minimize the sum in order to obtain the optimal parameters
// the minimization could be done for instance via the direction set
routine
// available in the Numerical Recipes in C
And what follows next is the same routine for the unscented filter.
void estimate_unscented_kalman_parameters_1_dim(
double *log_stock_prices,
double muS,
int n_stock_prices,
double omega,
double theta, double xi,
double rho,
double *u,
double *v,
double *estimates)

The Inference Problem
91
{
int
i1,i2, i3, t1;
int
ret;
int
na=3;
double
x, xa[3];
double
X[7], Xa[3][7];
double
Wm[7], Wc[7], Z[7];
double
x1;
double
prod, prod1;
double
P, P1;
double **Pa, **proda;
double
z, U, Pzz, K;
double
delt=1.0/252.0;
double
a=0.001 , b=0.0, k=0.0, lambda;
double eps=0.00001;
lambda = a*a*(na +k)-na;
proda= new double * [na];
Pa =
new double * [na];
for (i1=0;i1<na;i1++)
{
Pa[i1]= new double [na];
proda[i1]= new double [na];
}
xa[1]=xa[2]=0.0;
x= 0.04;
u[0]=u[n_stock_prices-1]=0.0;
v[0]=v[n_stock_prices-1]=1.0;
estimates[0]=estimates[1]=log_stock_prices[0]+eps;
xa[0]=x;
Pa[0][0]= Pa[1][1]= Pa[2][2] = 1.0;
Pa[1][0]= Pa[0][1]= Pa[1][2]=Pa[2][1]= Pa[0][2]=Pa[2][0]=0;
for (i1=0;i1<na;i1++)
{
for (i2=0;i2<na;i2++)
{
proda[i1][i2]=0.0;
}
}
Wm[0]=lambda/(na+lambda);

92
INSIDE VOLATILITY ARBITRAGE
Wc[0]=lambda/(na+lambda) + (1-a*a+b);
for (i3=1;i3<(2*na+1);i3++)
{
Wm[i3]=Wc[i3]=1/(2*(na+lambda));
}
for (t1=1;t1<n_stock_prices-1;t1++)
{
for (i1=0;i1<na;i1++)
{
Xa[i1][0]= xa[i1];
}
for (i1=0;i1<na;i1++)
{
for (i2=0;i2<na;i2++)
{
if (i1==i2)
{
if (Pa[i1][i2] < 1.0e-10)
Pa[i1][i2]= 1.0e-10;
}
else
{
if (Pa[i1][i2] < 1.0e-10)
Pa[i1][i2]= 0.0;
}
}
}
ret = sqrt_matrix(Pa,proda,na);
for (i3=1;i3<(1+na);i3++)
{
for (i1=0;i1<na;i1++)
{
Xa[i1][i3]= xa[i1] + sqrt(na+lambda) * proda[i1][i3-1];
}
}
for (i3=(1+na);i3<(2*na+1);i3++)
{
for (i1=0;i1<na;i1++)
{
Xa[i1][i3]= xa[i1] - sqrt(na+lambda) * proda[i1][i3-na-1];

The Inference Problem
93
}
}
for (i3=0;i3<(2*na+1);i3++)
{
if (Xa[0][i3]<0) Xa[0][i3]=0.0001;
X[i3]= Xa[0][i3] + (omega-muS*rho*xi
-
(theta-0.5*rho*xi) *Xa[0][i3])*delt +
rho*xi* (log_stock_prices[t1]-log_stock_prices[t1-1]) +
xi*sqrt((1-rho*rho)*delt*Xa[0][i3])*Xa[1][i3];
}
x1 = 0;
for (i3=0;i3<(2*na+1);i3++)
{
x1 += Wm[i3]*X[i3];
}
P1=0.0;
for (i3=0;i3<(2*na+1);i3++)
{
P1 += Wc[i3]*(X[i3]-x1)*(X[i3]-x1);
}
z=0;
for (i3=0;i3<(2*na+1);i3++)
{
if (X[i3]<0) X[i3]=0.00001;
Z[i3] = log_stock_prices[t1] + (muS-0.5*X[i3])*delt +
sqrt(X[i3]*delt)*Xa[2][i3];
z += Wm[i3]*Z[i3];
}
Pzz=0;
for (i3=0;i3<(2*na+1);i3++)
{
Pzz +=
Wc[i3]*(Z[i3]-z)*(Z[i3]-z);
}
prod=0.0;
for (i3=0;i3<(2*na+1);i3++)
{
prod += Wc[i3]*(X[i3]-x1)* (Z[i3]-z);
}

94
INSIDE VOLATILITY ARBITRAGE
K= prod/Pzz;
u[t1] = log_stock_prices[t1+1] - z;
v[t1] = Pzz;
estimates[t1+1] = z;
x = x1 + K*(log_stock_prices[t1+1] - z);
P = P1 - K*K * Pzz;
xa[0]=x;
Pa[0][0] = P;
if (x<0) x=0.0001;
Pa[1][0]= Pa[0][1]= Pa[1][2]=Pa[2][1]= Pa[0][2]=Pa[2][0]=0;
}
for (i1=0;i1<na;i1++)
{
delete [] Pa[i1];
delete [] proda[i1];
}
delete [] Pa;
delete [] proda;
}
// the routine sqrt_matrix() can be constructed via the Cholesly
decomposition
// also available as choldc() in the Numerical Recipes in C
Other stochastic volatility models
It is easy to generalize the above state-space
model to other stochastic volatility approaches. Indeed we could replace the
Heston equation with
vk = vk−1 + (ω −θvk−1)t + ξvp
k−1
√
tZk
where p = 1/2 would naturally correspond to the Heston model, p = 1 to
the GARCH diffusion-limit model, and p = 3/2 to the 3
2 model described in
[177]. This idea will be developed further in the chapter.

The Inference Problem
95
Diagnostics
After having estimated the parameter set , we should test for model mis-
specification. Two important questions are
1. Do the normalized residuals (zk −ˆz−
k )/Fk follow a standard normal
N(0 1) law?
2. Do these residuals have zero auto correlation?
Chi-Square Test
The first question could be answered by performing a chi-
square test. We take a number NB of intervals or “bins” bounded by the
points x0 x1 ... xJ . We then count the number of observations Nj within
each bin [xj  xj+1 ] for j between zero and NB −1. We then compare these
numbers with the theoretical numbers implied by the normal distribution
nj = [(xj+1 ) −(xj )]Nwith  the cumulative normal function and N the
total number of observations. The sum
NB−1

j=0
(Nj −nj )2
nj
asymptotically follows a χ2
ν law with degrees of freedom ν equal to NB −1.
Box-Ljung Test
The second question could be answered with a Box-Ljung test.
We should first calculate a number of autocorrelations
rk =
 N−k
i=1 (˜zi −¯˜z)(˜zi+k −¯˜z)
 N
i=1(˜zi −¯˜z)2
for k between one and a prespecified integer K. Once again, ˜zi = zi −ˆz−
i and
¯˜z corresponds to their mean. We then consider the sum
N(N + 2)
K

k=1
r2
k
N −k
which asymptotically follows a χ2
ν law with degrees of freedom ν equal to
K −p where p = 4 is the numbers of parameters we estimated.
Test Results
In the previously studied SPX examples, we had N = 1256. For
the normality test, we choose NB = 21 and for the Box-Ljung test we take
K = 24; in both cases, we will have to compare the outputs to the crit-
ical threshold χ2
20, which for a confidence of 0.95 is around 31.5. For the

96
INSIDE VOLATILITY ARBITRAGE
0
0.01
0.02
0.03
0.04
0.05
0.06
–10
–8
–6
–4
–2
0
2
4
6
8
10
Centered Data
Histograms
EKF
Normal
FIGURE 2.18
Histogram for Filtered Data via EKF versus the Normal Distribution.
The residuals are fairly normal.
(one-dimensional) EKF, we obtain 27.738862 for the normality test and
0.007889 for the Box-Ljung test. For the (one-dimensional) UKF, we
obtain 22.657545 for the normality test and again 0.016053 for the
Box-Ljung test. This means that there is very little autocorrelation in our
system noise. Also, it seems reasonable to model the noise as approximately
normally distributed. The chi-square test proves that the normality assump-
tion is plausible and the Kalman filter can be used. A visual confirmation of
this could be achieved by plotting the corresponding histograms. As we can
see in Figure 2.18, there are no excessively “fat tails”; however, the central
value at zero is higher than the normal distribution.
Variogram
Similarly to Fouque et al. [104], we can use a variogram to
visualize the volatility behavior of the model. As Galli [110] mentions, the
main reasons to use variograms instead of covariance or correlograms are
that variograms do not need to estimate the mean, and they are interpretable
under wider conditions than are covariances or correlograms.
The expression for the variogram of a process It is
γI (h) = 1
2E[(I(t + h) −I(t))2] ≈
1
2Nhi
Nhi

t=0
(I(t + hi) −I(t))2
where Nhi is the total number of points such that I(t + hi) exists.

The Inference Problem
97
0.9
0.95
1
1.05
1.1
1.15
1.2
1.25
10
20
30
40
50
60
Days
Variograms
EKF
UKF
FIGURE 2.19
Variograms for Filtered Data via EKF and UKF. The input corresponds
to a sequence of independent Gaussian random variables. As we can see, the vari-
ograms are close to one.
For instance, for a sequence of independent Gaussian random variables,
we should have
γI (h) = 1
2E[I 2(t + h)] + 1
2E[I 2(t)] −E[I(t)I(t + h)] = 1
2 + 1
2 −0 = 1
In our case, the process It could be defined, for instance, as
It = zt −ˆz−
t
√Ft
which should correspond to a sequence of independent Gaussian random
variables.
As we can see in Figure 2.19, the variogram is consistent with the Gaus-
sian assumption, which reconfirms what we observed from the histograms.
Another way of expressing the same idea is to build a Brownian motion from
the foregoing sequence. Calling the independent Gaussian random variables
(Bk), we can write
In =
√
t
n

k=0
Bk
and plot the variogram for the Brownian Motion In.

98
INSIDE VOLATILITY ARBITRAGE
0
0.5
1
1.5
2
2.5
0
5
10
15
20
25
30
35
40
45
50
Variograms
Days
x/2
EKF
UKF
FIGURE 2.20
Variograms for Filtered Data via EKF and UKF. The input corresponds
to a Brownian motion. As we can see, the variograms are close to x/2.
For a Brownian motion, it is easy to see that the variogram should be linear
γI (h) = 1
2(t + h) + 1
2t −t = 1
2h
This could indeed be seen in Figure 2.20.
Particle Filtering
A different approach to filtering and parameter estimation has recently
become popular [79], [122], [171]. In this approach, we use Monte Carlo
simulations instead of Gaussian approximations for (xk|zk), as the Kalman
or Kushner filters do. This will precisely allow us to deal with fundamentally
non-Gaussian situations.22
22An existing (but less effective) alternative to the particle filtering method is the
grid-based approximation, such as the one suggested by Kitagawa [170], [108]. The
main advantage of the particle filter is that it will make the grid focus adaptively on
the state-space regions with higher relevance.

The Inference Problem
99
Underlying Theory
The idea is based on the Importance Sampling technique:
We can calculate an expected value
E[f (x0:k)] =

f (x0:k)p(x0:k|z1:k)dx0:k
(2.17)
by using a known and simple proposal distribution q().
More precisely, it is possible to write
E[f (x0:k)] =

f (x0:k) p(x0:k|z1:k)
q(x0:k|z1:k)q(x0:k|z1:k)dx0:k
which could be also written as
E[f (x0:k)] =

f (x0:k)wk(x0:k)
p(z1:k) q(x0:k|z1:k)dx0:k
(2.18)
with
wk(x0:k) = p(z1:k|x0:k)p(x0:k)
q(x0:k|z1:k)
defined as the filtering non-normalized weight as step k.
Proof:
p(x0:k|z1:k)
q(x0:k|z1:k) = p(z1:k|x0:k)p(x0:k)
p(z1:k)q(x0:k|z1:k)
= wk(x0:k)
p(z1:k)
(QED)
We therefore have
E[f (x0:k)] = Eq[wk(x0:k)f (x0:k)]
Eq[wk(x0:k)]
= Eq[ ˜wk(x0:k)f (x0:k)]
(2.19)
with
˜wk(x0:k) =
wk(x0:k)
Eq[wk(x0:k)]
defined as the filtering normalized weight as step k.
Proof:
We write
E[f (x0:k)] =
1
p(z1:k)

f (x0:k)wk(x0:k)q(x0:k|z1:k)dx0:k
=
!
f (x0:k)wk(x0:k)q(x0:k|z1:k)dx0:k
!
p(z1:k|x0:k)p(x0:k) q(x0:k|z1:k)
q(x0:k|z1:k)dx0:k

100
INSIDE VOLATILITY ARBITRAGE
=
!
f (x0:k)wk(x0:k)q(x0:k|z1:k)dx0:k
!
wk(x0:k)q(x0:k|z1:k)dx0:k
which is the ratio of the expectations, as earlier stated. (QED)
Using Monte-Carlo sampling from the distribution q(x0:k|z1:k) we can
write in the discrete framework:
E[f (x0:k)] ≈
Nsims

i=1
˜wk

x(i)
0:k

f

x(i)
0:k

(2.20)
with again
˜wk(x(i)
0:k) =
wk

x(i)
0:k

 Nsims
j=1
wk

x(j)
0:k

Now supposing that our proposal distribution q() satisfies the Markov prop-
erty, it can be shown that wk verifies the recursive identity
w(i)
k = w(i)
k−1
p

zk|x(i)
k

p

x(i)
k |x(i)
k−1

q

x(i)
k |x(i)
0:k−1 z1:k

(2.21)
which completes the sequential importance sampling algorithm.
Proof:
The Markov property just mentioned could be written as
q(x0:k|z1:k) = q(xk|x0:k−1 z1:k)q(x0:k−1|z1:k−1)
(2.22)
We also assume that the state (xk) is a Markov process, meaning
p(xk|x0:k−1) = p(xk|xk−1)
and the observations (zk) are conditionally independent given the states, so
that
p(zk|x0:k) = p(zk|xk)
Finally we use the fact that at time-step k, all previous observations are
perfectly known, and
p(zk|xk z1:k−1) = p(zk|xk)
Therefore
wk(xk) = p(z1:k|x0:k)p(x0:k)
q(x0:k|z1:k)

The Inference Problem
101
= p(zk|xk)p(z1:k−1|x0:k−1)p(xk|xk−1)p(x0:k−1)
q(xk|x0:k−1 z1:k)q(x0:k−1|z1:k−1)
(QED)
It is important to note that what the foregoing means is that the state xk
cannot depend on future observations; that is, we are dealing with filtering
and not smoothing.
Resampling
One major problem with this algorithm is that the variance of
the weights increases randomly over time. In order to solve this, we need to
use a resampling algorithm, which would map our unequally weighted xk’s
to a new set of equally weighted sample points. Various methods have been
suggested for this. See, for instance, Arulampalam [14], [171]. The basic
idea is to compare the cumulative distribution function (CDF) created from
the normalized weights with a CDF constructed from a uniformly simulated
number U[0 1]. We would then eliminate the indices having too small a
weight and repeat those having a sufficiently large weight.
More accurately, at a given time step k, for 1 ≤j ≤Nsims, if
1
Nsims
(U[0 1] + j −1) ≥
i
l=1
˜w(l)
k
then increment and “skip” i; otherwise, take x(i)
k and set its weight to
1
Nsims.
Note that the resampling algorithm could create a situation where the
resulting sample has many repeated points. This is known as sample impov-
erishment and could lead to an extreme case in which all points collapse to
a unique particle after a few iterations. This phenomenon is more likely if
the process noise is small. One possible solution to this problem is to add a
Markov chain Monte Carlo (MCMC) step after the resampling. As will be
described further, a Metropolis-Hastings (MH) sampling algorithm would
be suitable.
Needless to say, the choice of the proposal distribution is crucial. Many
suggest using
q(xk|x0:k−1 z1:k) = p(xk|xk−1)
since it will give us a simple weight identity
w(i)
k = w(i)
k−1p(zk|x(i)
k )
Based on this type of choice, hereafter we shall simplify and write
q(xk|x0:k−1 z1:k) = q(xk|xk−1 z1:k)
without any change to our arguments. However, this choice of the proposal
distribution does not take into account our most recent observation zk at
all and therefore could become inefficient. Hence aries the idea of using a

102
INSIDE VOLATILITY ARBITRAGE
Gaussian approximation for the proposal and, in particular, an approxima-
tion based on the Kalman filter, in order to incorporate the observations. We
therefore will have
q(xk|xk−1 z1:k) = N(ˆxk Pk)
(2.23)
using the same notations as in the section on the Kalman filter. Such filters are
sometimes referred to as the extended particle filter (EPF) or the unscented
particle filter (UPF). This is similar to the iterative gentering algorithm in
Kushner’s NLF.
From here, in order to estimate the parameter set  we can either use
dual/Joint filter, or use an ML estimator. Note that since the particle filter
does not necessarily assume Gaussian noise, the likelihood function to be
maximized has a more general form than the one used in previous sections.
Given the likelihood at step k
lk = p(zk|z1:k−1) =

p(zk|xk)p(xk|z1:k−1)dxk
the total likelihood is the product of the lk’s and therefore the log likelihood
to be maximized is
ln(L1:N) =
N

k=1
ln(lk)
(2.24)
Now lk could be written as
lk =

p(zk|xk) p(xk|z1:k−1)
q(xk|xk−1 z1:k)q(xk|xk−1 z1:k)dxk
and given that by construction the x(i)
k ’s are distributed according to q(), we
can write the Monte Carlo approximation
lk ≈
Nsims

i=1
p

zk|x(i)
k

p

x(i)
k |x(i)
k−1

q

x(i)
k |x(i)
k−1 z1:k

(2.25)
which we already computed for the sequential importance sampling weight
update.
As we shall see in the next paragraph, it is also possible to interpret the
step k likelihood, as a quantity related to the total weight
Nsims

i=1
w(i)
k
Finally, we could interpret the particle filter as follows. We are using a Monte
Carlo simulation (via an importance sampling technique) to calculate the
integral
!
f (xk)p(xk|z1:k)dxk. This is exactly what other filtering techniques

The Inference Problem
103
try to do. The Kushner nonlinear filter (NLF) tries to calculate the integral
via a Gaussian quadrature. Indeed, NLF uses Hermite polynomials because
it treats the distributions as normal.23
Implementation
Given the above theory, the algorithm for an extended or
unscented particle filter could be implemented in the following way:
1. For time step k = 0, choose x0 and P0 > 0.
For i such that 1 ≤i ≤Nsims, take
x(i)
0
= x0 +

P0Z(i)
where Z(i) is a standard Gaussian simulated number. Also take P (i)
0
= P0
and
w(i)
0 =
1
Nsims
While 1 ≤k ≤N
2. For each simulation index i
ˆx(i)
k = KF(x(i)
k−1)
with P (i)
k
the associated a posteriori error covariance matrix. (KF could
be either the EKF or the UKF.)
3. For each i between 1 and Nsims
˜x(i)
k = ˆx(i)
k +

P (i)
k Z(i)
where again Z(i) is a standard Gaussian simulated number.
4. Calculate the associated weights for each i
w(i)
k = w(i)
k−1
p(zk|˜x(i)
k )p(˜x(i)
k |x(i)
k−1)
q(˜x(i)
k |x(i)
k−1 z1:k)
with q() the normal density with mean ˆx(i)
k and variance P (i)
k .
5. Normalize the weights
˜w(i)
k =
w(i)
k
 Nsims
i=1
w(i)
k
6. Resample the points ˜x(i)
k and get x(i)
k and reset w(i)
k = ˜w(i)
k =
1
Nsims.
7. Increment k; go back to Step 2 and Stop at the end of the While loop.
23Other filters cited, for instance, in [79] use the more general Legendre polynomials.

104
INSIDE VOLATILITY ARBITRAGE
From Step 4 we have
¯lk =
Nsims

i=1
p

zk|˜x(i)
k

p

˜x(i)
k |x(i)
k−1

q

˜x(i)
k |x(i)
k−1 z1:k

where ¯lk is a Monte Carlo proxy for the likelihood lk at the step k. As we
saw in the previous section, by minimizing
−
N

k=1
ln(¯lk)
using, for instance, the direction set algorithm, we will be maximizing the
likelihood function and hence we will be obtaining the optimal parameter
set ˆ.
Given the resetting of w(i)
k to a constant
1
Nsims during the resampling step,
we can also replace ¯lk with
˜lk =
Nsims

i=1
w(i)
k
which will provide us with an interpretation of the likelihood as the total
weight.
An Illustration
Let us consider once again the case of the previous illustration
ξk = ξk−1 + π + 0.10wk
and
zk = ξk + 0.10uk
where π ≈3.14159 and wk, uk are independent Gaussian random variables.
We apply the same Kalman filter and then apply the previous algorithm to
the system. Calling
n(x m s) =
1
√
2πs
exp

−(x −m)2
2s2
	
the normal density with mean m and standard deviation s, we will have
q

˜x(i)
k |x(i)
k−1 z1:k

= n

˜x(i)
k  m = ˆx(i)
k  s =

P (i)
k
	
as well as
p

zk|˜x(i)
k

= n

zk m = ˜x(i)
k  s = 0.10


The Inference Problem
105
and
p

˜x(i)
k |x(i)
k−1

= n

˜x(i)
k  m = x(i)
k−1 + π s = 0.10

Taking 100 particles and 500 observation points, the EPF converges very
quickly to ˆπ = 3.148200 . Alternatively, the simple PF (with no Kalman com-
ponent) would converge to ˆπ = 3.140266.
Note that this example is Gaussian and linear, and therefore the particle
filtering is not an improvement over the Kalman filter! Indeed the Kalman
filter is optimal for Gaussian linear cases.
Application to the Heston Model
We could now apply the above particle filtering
algorithm to our one-dimensional state, where xk = vk and zk = ln Sk+1 as
before. Calling
n(x m s) =
1
√
2πs
exp

−(x −m)2
2s2
	
the normal density with mean m and standard deviation s, we will have
q

˜x(i)
k |x(i)
k−1 z1:k

= n

˜x(i)
k  m = ˆx(i)
k  s =

P (i)
k
	
as well as
p

zk|˜x(i)
k

= n

zk m = zk−1 +

µS −1
2 ˜x(i)
k
	
t s =

˜x(i)
k
√
t
	
and
p

˜x(i)
k |x(i)
k−1

=
n

˜x(i)
k  m = x(i)
k−1 +

(ω −ρξµS) −

θ −1
2ρξ
	
x(i)
k−1

t + ρξ(zk−1 −zk−2) s
	
with
s = ξ

1 −ρ2

x(i)
k−1
√
t
which provides us with the densities we need for the filter implementation.
The estimation of the observable state zk is
ˆz−
k =
1
Nsims
Nsims

i=1
ˆz(i)
k
with ˆz(i)
k the estimation of zk from KF(x(i)
k−1).
Following is a C++ routine for the EPF applied to the Heston model;
1000 particles are being used.

106
INSIDE VOLATILITY ARBITRAGE
// log_stock_prices
are the log of stock prices
// muS is the real-world stock drift
// n_stock_prices is the number of the above stock
prices
// (omega, theta, xi, rho) are the Heston parameters
// ll is the value of (negative log) Likelihood
function
// estimates[] are the estimated observations from the
filter
// The function ran2() is from Numerical Recipes in C
// and generates uniform random variables
// The function Normal_inverse() can be found from
many sources
// and is the inverse of the Normal CDF
// Normal_inverse(ran2(.)) generates a set of Normal
random variables
void estimate_particle_extended_kalman_parameters_1_dim(
double *log_stock_prices,
double muS,
int n_stock_prices,
double omega,
double theta,
double xi,
double rho,
double *ll,
double *estimates)
{
int
i1, i2, i3;
double
H, A, x0, P0, z;
int
M=1000;
double
x[1000], xx[1000], x1[1000], x2[1000];
double
P[1000], P1[1000], U[1000], K[1000], W[1000];
double
w[1000],
u[1000], c[1000];
double
q, pz, px, s, m, l;
double
delt=1.0/252.0, x1_sum;
long
idum=-1;
A = 1.0-(theta-0.5*rho*xi)*delt;
H = -0.5*delt;
x0 = 0.04;
P0 = 0.000001;
for (i2=0; i2<M; i2++)

The Inference Problem
107
{
x[i2] = x0 + sqrt(P0)* Normal_inverse(ran2(&idum));
P[i2] = P0;
}
*ll=0.0;
for (i1=1;i1<n_stock_prices-1;i1++)
{
l = 0.0;
x1_sum=0.0;
for (i2=0; i2<M; i2++)
{
/* EKF for the proposal distribution */
if (x[i2]<0) x[i2]=0.00001;
x1[i2] = x[i2] + ( omega-rho*xi*muS - (theta-
0.5*rho*xi) * x[i2]) * delt + rho*xi*
(log_stock_prices[i1]-log_stock_prices[i1-1]);
W[i2]
= xi*sqrt((1-rho*rho) * x[i2] * delt);
P1[i2] = W[i2]*W[i2] + A*P[i2]*A;
if (x1[i2]<0) x1[i2]=0.00001;
U[i2] = sqrt(x1[i2]*delt);
K[i2] = P1[i2]*H/( H*P1[i2]*H + U[i2]*U[i2]);
z = log_stock_prices[i1+1];
x2[i2] = x1[i2] + K[i2] * (z - (log_stock_prices[i1]
+ (muS-0.5*x1[i2])*delt));
x1_sum+= x1[i2];
P[i2]=(1.0-K[i2]*H)*P1[i2];
/* sample */
xx[i2] = x2[i2]+sqrt(P[i2])*Normal_inverse(ran2(&idum));
if (xx[i2]<0) xx[i2]=0.00001;
/* calculate weights */
m = x2[i2];
s = sqrt(P[i2]);
q = 0.39894228/s * exp( - 0.5* (xx[i2] - m)*
(xx[i2] - m)/(s*s) );
m = log_stock_prices[i1] + (muS-0.5*xx[i2])*delt;
s = sqrt(xx[i2]*delt);
pz = 0.39894228/s * exp( - 0.5* (z - m)*(z - m)/(s*s) );
m = x[i2] + ( omega-rho*xi*muS - (theta-0.5*
rho*xi) * x[i2]) * delt + rho*xi*
(log_stock_prices[i1]-log_stock_prices[i1-1]);
s = xi*sqrt((1-rho*rho) * x[i2] * delt);
px = 0.39894228/s * exp( - 0.5* (xx[i2] - m)*
(xx[i2] - m)/(s*s) );

108
INSIDE VOLATILITY ARBITRAGE
w[i2] = pz * px / MAX(q, 1.0e-10);
l += w[i2];
}
*ll += log(l);
estimates[i1+1]= log_stock_prices[i1] +
(muS-0.5*x1_sum/M)*delt;
/* normalize weights */
for (i2=0; i2<M; i2++)
w[i2] /= l;
/* resample and reset weights */
c[0]=0;
for (i2=1; i2<M; i2++)
c[i2] = c[i2-1] + w[i2];
i2=0;
u[0] = 1.0/M * ran2(&idum);
for (i3=0; i3<M; i3++)
{
u[i3] = u[0] + 1.0/M *i3;
while (u[i3] > c[i2])
i2++;
x[i3] = xx[i2];
w[i3] = 1.0/M;
}
}
*ll *= -1.0;
}
// *ll is the value of (negative log) Likelihood
function
// we can minimize it to obtain the optimal
parameter-set
Next is the same routine for the unscented filter.
void estimate_particle_unscented_kalman_parameters_1_dim(
double *log_stock_prices,
double muS,
int n_stock_prices,
double omega,
double theta,
double xi,

The Inference Problem
109
double rho,
double *ll,
double *estimates)
{
int
i1, i2, i3, i4;
int
na=3;
double
x0, P0;
double
Wm[7], Wc[7];
int
M=1000;
double
x[1000], xx[1000], x1[1000], x2[1000],
zz[1000], Z[1000][7];
double
X[1000][7], Xa[1000][3][7];
double
xa[1000][3], prod[1000];
double
P[1000], P1[1000], U[1000], K[1000],
W[1000], Pzz[1000];
double
w[1000],
u[1000], c[1000];
double
***Pa, ***proda;
double
q, pz, px, s, m, l, z;
double
delt=1.0/252.0;
long
idum=-1;
int
ret;
double
a=0.001 , b=0.0, k=0.0, lambda;
proda= new double ** [M];
Pa =
new double ** [M];
for (i2=0;i2<M;i2++)
{
Pa[i2]= new double * [na];
proda[i2]= new double * [na];
for (i1=0;i1<na;i1++)
{
Pa[i2][i1]= new double [na];
proda[i2][i1]= new double [na];
}
}
for (i2=0;i2<M;i2++)
{
for (i1=0;i1<na;i1++)
{
for (i3=0;i3<na;i3++)
{
proda[i2][i1][i3]=0.0;

110
INSIDE VOLATILITY ARBITRAGE
}
}
}
lambda = a*a*(na +k)-na;
Wm[0]=lambda/(na+lambda);
Wc[0]=lambda/(na+lambda) + (1-a*a+b);
for (i3=1;i3<(2*na+1);i3++)
{
Wm[i3]=Wc[i3]=1/(2*(na+lambda));
}
x0 = 0.04;
P0 = 0.000001;
for (i2=0; i2<M; i2++)
{
x[i2] = x0 + sqrt(P0)* Normal_inverse(ran2(&idum));
P[i2] = P0;
xa[i2][0]=x[i2];
xa[i2][1]=xa[i2][2]=0.0;
Pa[i2][0][0]= P[i2];
Pa[i2][1][1]= Pa[i2][2][2] = 1.0;
Pa[i2][1][0]= Pa[i2][0][1]= Pa[i2][1][2] =
Pa[i2][2][1] =
Pa[i2][0][2] = Pa[i2][2][0] = 0.0;
}
*ll=0.0;
for (i1=1;i1<n_stock_prices-1;i1++)
{
l = 0.0;
estimates[i1+1]=0.0;
for (i2=0; i2<M; i2++)
{
/* UKF for the proposal distribution */
for (i3=0;i3<na;i3++)
{
Xa[i2][i3][0]= xa[i2][i3];
}

The Inference Problem
111
for (i3=0;i3<na;i3++)
{
for (i4=0;i4<na;i4++)
{
if (i3==i4)
{
if (Pa[i2][i3][i4] < 1.0e-10)
Pa[i2][i3][i4]= 1.0e-10;
}
else
{
if (Pa[i2][i3][i4] < 1.0e-10)
Pa[i2][i3][i4] = 0.0;
}
}
}
ret = sqrt_matrix(Pa[i2],proda[i2],na);
for (i3=1;i3<(1+na);i3++)
{
for (i4=0;i4<na;i4++)
{
Xa[i2][i4][i3]= xa[i2][i4] + sqrt(na+lambda) *
proda[i2][i4][i3-1];
}
}
for (i3=(1+na);i3<(2*na+1);i3++)
{
for (i4=0;i4<na;i4++)
{
Xa[i2][i4][i3]= xa[i2][i4] - sqrt(na+lambda) *
proda[i2][i4][i3-na-1];
}
}
for (i3=0;i3<(2*na+1);i3++)
{
if (Xa[i2][0][i3]<0) Xa[i2][0][i3]=0.0001;
X[i2][i3]= Xa[i2][0][i3] + (omega-muS*rho*xi
-
(theta-0.5*rho*xi) *Xa[i2][0][i3])*delt +
rho*xi* (log_stock_prices[i1]-

112
INSIDE VOLATILITY ARBITRAGE
log_stock_prices[i1-1]) +
xi*sqrt((1-rho*rho)*delt*Xa[i2][0][i3])*
Xa[i2][1][i3];
}
x1[i2] = 0;
for (i3=0;i3<(2*na+1);i3++)
{
x1[i2] += Wm[i3]*X[i2][i3];
}
P1[i2]=0.0;
for (i3=0;i3<(2*na+1);i3++)
{
P1[i2] += Wc[i3]*(X[i2][i3]-x1[i2])*(X[i2][i3]-
x1[i2]);
}
zz[i2]=0;
for (i3=0;i3<(2*na+1);i3++)
{
if (X[i2][i3]<0) X[i2][i3]=0.00001;
Z[i2][i3] = log_stock_prices[i1] +
(muS-0.5*X[i2][i3])*delt + sqrt(X[i2][i3]*delt)*Xa[i2][2][i3];
zz[i2] += Wm[i3]*Z[i2][i3];
}
Pzz[i2]=0;
for (i3=0;i3<(2*na+1);i3++)
{
Pzz[i2] +=
Wc[i3]*(Z[i2][i3]-zz[i2])*(Z[i2][i3]-
zz[i2]);
}
prod[i2]=0.0;
for (i3=0;i3<(2*na+1);i3++)
{
prod[i2] += Wc[i3]*(X[i2][i3]-x1[i2])* (Z[i2][i3]-
zz[i2]);
}
K[i2]= prod[i2]/Pzz[i2];

The Inference Problem
113
z = log_stock_prices[i1+1];
estimates[i1+1] += zz[i2]/M;
x2[i2] = x1[i2] + K[i2]*(z - zz[i2]);
P[i2] = P1[i2] - K[i2]*K[i2] * Pzz[i2];
xa[i2][0]=x2[i2];
Pa[i2][0][0] = P[i2];
if (x2[i2]<0) x2[i2]=0.0001;
Pa[i2][1][0]= Pa[i2][0][1]= Pa[i2][1][2]
=Pa[i2][2][1]= Pa[i2][0][2]=Pa[i2][2][0]=[0];
/* sample */
xx[i2] = x2[i2] + sqrt(P[i2])*
Normal_inverse(ran2(&idum));
if (xx[i2]<0) xx[i2]=0.00001;
/* calculate weights */
m = x2[i2];
s = sqrt(P[i2]);
q = 0.39894228/s * exp( - 0.5* (xx[i2] - m)*
(xx[i2] - m)/(s*s) );
m= log_stock_prices[i1] + (muS-0.5*xx[i2])*delt;
s= sqrt(xx[i2]*delt);
pz= 0.39894228/s * exp( - 0.5* (z - m)*
(z - m)/(s*s) );
m= x[i2] + ( omega-rho*xi*muS -
(theta-0.5*rho*xi) * x[i2]) * delt +
rho*xi* (log_stock_prices[i1]-
log_stock_prices[i1-1]);
s= xi*sqrt((1-rho*rho) * x[i2] * delt);
px= 0.39894228/s * exp( - 0.5* (xx[i2] - m)*
(xx[i2] - m)/(s*s) );
w[i2]= MAX(pz, 1.0e-10) *
MAX(px, 1.0e-10) / MAX(q, 1.0e-10);
l += w[i2];
}
*ll += log(l);
/* normalize weights */

114
INSIDE VOLATILITY ARBITRAGE
for (i2=0; i2<M; i2++)
w[i2] /= l;
/* resample and reset weights */
c[0]=0;
for (i2=1; i2<M; i2++)
c[i2] = c[i2-1] + w[i2];
i2=0;
u[0] = 1.0/M * ran2(&idum);
for (i3=0; i3<M; i3++)
{
u[i3] = u[0] + 1.0/M *i3;
while (u[i3] > c[i2])
i2++;
x[i3]= xx[i2];
w[i3]=1.0/M;
}
}
*ll *= -1.0;
for (i2=0;i2<M;i2++)
{
for (i1=0;i1<na;i1++)
{
delete [] Pa[i2][i1];
delete [] proda[i2][i1];
}
}
for (i2=0;i2<M;i2++)
{
delete [] Pa[i2];
delete [] proda[i2];
}
delete [] Pa;
delete [] proda;
}
Test Results
The results from an extended particle filter (EPF) are shown
in Figure 2.21. The filter was constructed with the one-dimensional Heston

The Inference Problem
115
1e-05
1.5e-05
2e-05
2.5e-05
3e-05
3.5e-05
4e-05
4.5e-05
5e-05
5.5e-05
0
500
1000
1500
2000
Error
Days
EKF and EPF Errors
EKF
EPF
FIGURE 2.21
Filtering Errors: Extended Kalman Filter and Extended Particle Filter
Are Applied to the One-Dimensional Heston Model. The PF has better performance.
model and was applied to a simulated time series of 5000 points with
∗= (0.40 10.0 0.01 −0.50)
As we can see in the figure, no clear superiority of the EPF is detected. The
optimal parameters found via EPF are
ˆEPF = (0.020331 0.499987 0.040000 0.050026)
which could not be considered as an improvement over
ˆEKF = (0.065886 1.711686 0.180884 0.147660)
Again the long-term-variances ω
θ are close to 0.04 for all cases, which is
consistent with what we had observed.
The next natural step would be to implement and test the unscented
particle filter (UPF), in which everything is done similarly to the EPF except
for the choice of the proposal distribution. The use of the UPF has been
strongly recommended by Wan and Van der Merwe in [231] and [133]. The
authors claim that the filtering error from the UPF is considerably smaller
than that from EKF, UKF, or EPF. As we can see in Figure 2.22, it is true that
the filtering error resulting from UPF is considerably lower than the error
generated from the other filters. However, the optimal parameter set
ˆUPF = (0.020132 0.500031 0.040000 0.050004)

116
INSIDE VOLATILITY ARBITRAGE
1e-05
1.5e-05
2e-05
2.5e-05
3e-05
3.5e-05
4e-05
4.5e-05
5e-05
5.5e-05
400
600
800
1000
1200
1400
1600
1800
2000
Error
Days
Filter Errors
EKF
UKF
EPF
UPF
FIGURE 2.22
Filtering Errors: All Filters Are Applied to the One-Dimensional Hes-
ton Model. The PF’s have better performance.
obtained via UPF is again very different from the original parameter set ∗
used in the data generation. We shall analyze the reasons behind this poor
inference result more closely in the following sections.
Error Size
One possibility is that our time series has too small an error for
the filters to make a significant difference. We thus study another case, where
t = 1 year. Let us take 200 points generated with the parameter set
∗= (0.02 0.5 0.05 −0.5)
We obtain
ˆEKF = (0.036 0.093 0.036 −1.00)
and
ˆUKF = (0.033 0.086 0.033 −0.98)
which shows that UKF results are very close to EKF ones. Using the particle
filters, we get
ˆEPF = (0.019 0.5 0.03 −0.58)

The Inference Problem
117
0
0.002
0.004
0.006
0.008
0.01
0.012
0.014
0.016
20
40
60
80
100
120
140
160
180
Error
Days
Filter Errors
EKF
UKF
EPF
UPF
FIGURE 2.23
Filters Are Applied to the One-Dimensional Heston Model. The time
series has a larger time-step t = 1.0. Naturally, the errors are larger than the case
where t = 1/252.
which is considerably closer to the original set ∗. Therefore EPF did bring
an improvement over the traditional nonlinear filters and seems to be simpler
and more robust24 than its competitors.
As for the filtering errors, it can be seen in Figure 2.23 that the EPF errors
are smaller than (although comparable to) those produced by EKF and UKF,
which is consistent with the particle filtering theory.
As for UPF, we obtain
ˆUPF = (0.019480 0.489375 0.047030 −0.229242)
which is very close to the EPF result. As we can see, the UPF errors are even
smaller than those generated by EPF. In addition to the filters just discussed,
it would be interesting to test a Gauss-Hermite filter (GHF) [151]. We obtain
ˆGHF = (0.020398 0.524215 0.069661 −1.000000)
which is closer to the real parameter set ∗compared with EKF or UKF
results. However, the filtering error is more variable than that of its competi-
tors, as can be seen in Figure 2.24. Note, however, that this would mean that
24This is because for a larger time step the nonlinearity and non-Gaussianity have a
stronger impact.

118
INSIDE VOLATILITY ARBITRAGE
0
0.005
0.01
0.015
0.02
0.025
0.03
20
40
60
80
100
120
140
160
180
Error
Days
Filter Errors
EKF
GHF
FIGURE 2.24
The EKF and GHF Are Applied to the One-Dimensional Heston
Model. The time series has a larger time step t = 1.0. Naturally, the errors are
larger than the case where t = 1/252.
we would have access to 200 years of historic data, which is clearly unreal-
istic.25 This issue will be revisited in the following sections. Also, here we
generated the data via a discrete equation with t = 1. Thus there was no
discretization error from a continuous equation. We cannot apply the same
method to data coming from a continuous process.
As a measure of performance, we can compute the mean price error
(MPE) as well as the root mean square error (RMSE) for each filter. These
correspond respectively to the mean and the standard deviation of the plotted
errors. For the MPEs, we obtain
MPE
RMSE
EKF
0.007484269
0.003422215
UKF
0.007660269
0.003733748
GKF
0.009129157
0.005816919
EPF
0.007620208
0.002269224
UPF
0.007076066
0.001359393
25What is more, the Girsanov theorem would not be valid and (ξρ) would have no
reason to be the same under the risk-neutral and real measures.

The Inference Problem
119
This shows us again that the particle filters outperform the other ones.
Again, let us remember that given 200 points with t = 1 and a true param-
eter set
∗= (0.02 0.5 0.05 −0.5)
we obtained
ˆω
ˆθ
ˆξ
ˆρ
EKF
0.036
0.093
0.036
−1.00
UKF
0.033
0.086
0.033
−0.98
GKF
0.020
0.524
0.070
−1.00
EPF
0.019
0.500
0.033
−0.58
UPF
0.019
0.489
0.047
−0.22
The MH Enhancement
As mentioned earlier, the resampling algorithm helps
with the issue of degeneracy, which means that it will reduce the variance
of the weights. However, it might introduce a sample impoverishment phe-
nomenon, in which all particles will have a tendency to collapse to one. The
Metropolis-Hastings (MH) algorithm could be a solution to this problem
and is implemented as follows. After resampling, Step 6, we obtain a set ˜˜x(i)
1:k.
6-a. Reapply the Kalman filter (extended or unscented) to this set in order
to obtain
x∗(i)
k
= KF

˜˜x(i)
k−1

6-b. Choose between x∗(i)
k
and ˜˜x(i)
k as follows. Define
α = min

1 p(zk|x∗(i)
k
)p(x∗(i)
k
|x(i)
k−1)q(˜˜x(i)
k |x(i)
k−1 z1:k)
p(zk|˜˜x(i)
k )p(˜˜x(i)
k |x(i)
k−1)q(x∗(i)
k
|x(i)
k−1 z1:k)

then sample v from U[0 1] and choose x∗(i)
k
if α > v and choose ˜˜x(i)
k if
α ≤v.
The result is then x(i)
k , and we go to Step 7 as before.
Note that α could be interpreted as the ratio of the non-normalized
weights for the two particles we are choosing from. Indeed
α = α(i)
k = min

1 w(x∗(i)
k
)
w(˜˜x(i)
k )


120
INSIDE VOLATILITY ARBITRAGE
0
0.002
0.004
0.006
0.008
0.01
0.012
0.014
20
40
60
80
100
120
140
160
180
Error
Days
Filter Errors
EPF
EPF-MH
FIGURE 2.25
The EPF Without and with the Metropolis-Hastings Step is Applied to
the One-Dimensional Heston Model. The time series has a time step t = 1.0. The
improvement is hardly visible.
Applied to the same time series as in the previous paragraphs, the EPF with
the MH modification will provide
ˆEPF−MH = (0.019 0.499 0.040 −0.358)
and
MP EEPF−MH = 0.007753
RMSEEPF−MH = 0.001927
compared with the previous EPF
MP EEPF = 0.00762
RMSEEPF = 0.002269
As we can see from these results and Figure 2.25, there is only a marginal
improvement from the introduction of the MH step in the filtering process.
This is in line with the findings in the literature, such as in [231].
Comparing Heston with other Models
We can now apply our inference tools to real market data in order to see
which model matches the true dynamics of the assets more closely, and there-
fore perform model identification.

The Inference Problem
121
The Models
It is easy to generalize the Heston state-space model to other
stochastic volatility approaches. Indeed we could replace the Heston state
equation with
vk = vk−1 + (ω −θvk−1)t + ξvp
k−1
√
tZk−1
(2.26)
where p = 1/2 would naturally correspond to the Heston (square root)
model, p = 1 to the GARCH diffusion-limit model, and p = 3/2 to the 3/2
model. These models have all been described and analyzed in [177]. The new
state transition equation would therefore become
vk = vk−1 +

ω −ρξµSv
p−1
2
k−1 −

θ −1
2ρξv
p−1
2
k−1
	
vk−1

t
+ ρξv
p−1
2
k−1 ln
 Sk
Sk−1
	
+ ξ

1 −ρ2vp
k−1
√
t ˜Zk−1
(2.27)
where the same choice of state space xk = vk is made.
For the EKF, we will have
Ak = 1 −

ρξµS

p −1
2
	
v
p−3
2
k−1 + θ −1
2ρξ

p + 1
2
	
v
p−1
2
k−1

t
+

p −1
2
	
ρξv
p−3
2
k−1 ln
 Sk
Sk−1
	
and
Wk = ξ

1 −ρ2vp
k−1
√
t
as well as
Hk = −1
2t
and
Uk = √vk
√
t
The same time update and measurement update equations could be used
with the UKF or Kushner’s NLF.
We could also apply the particle filtering algorithm to our problem. Using
the same notations as before and calling
n(x m s) =
1
√
2πs
exp

−(x −m)2
2s2
	
the normal density with mean m and standard deviation s, we will have
q(˜x(i)
k |x(i)
k−1 z1:k) = n

˜x(i)
k  m = ˆx(i)
k  s =

P (i)
k
	

122
INSIDE VOLATILITY ARBITRAGE
as well as
p(zk|˜x(i)
k ) = n

zk m = zk−1 +

µS −1
2 ˜x(i)
k
	
t s =

˜x(i)
k
√
t
	
and
p

˜x(i)
k |x(i)
k−1

= n

˜x(i)
k  mx s = ξ

1 −ρ2

x(i)
k−1
p √
t

with
mx = x(i)
k−1 +

ω −ρξµS

x(i)
k−1
p−1
2 −

θ −1
2ρξ

x(i)
k−1
p−1
2
	
x(i)
k−1

t
+ ρξ

x(i)
k−1
p−1
2 (zk−1 −zk−2)
and as before we have
w(i)
k = w(i)
k−1
p

zk|˜x(i)
k

p

˜x(i)
k |x(i)
k−1

q

˜x(i)
k |x(i)
k−1 z1:k

which provides us with what we need for the filter implementation.
The Results
The preceding filters were applied to five years of S&P 500 time
series (1996 to 2001 ), and the filtering errors were considered for the Heston,
the GARCH, and the 3/2 models. Daily index closing prices were used for
this purpose, and the time interval was set to t = 1/252 (see the following
table; Figures 2.26 through 2.32).
Filter and Model
MPE
RMSE
EKF-Heston
3.58207e-05
1.83223e-05
EKF-GARCH
2.78438e-05
1.42428e-05
EKF-3/2
2.63227e-05
1.74760e-05
UKF-Heston
3.00000e-05
1.91280e-05
UKF-GARCH
2.99275e-05
2.58131e-05
UKF-3/2
2.82279e-05
1.55777e-05
EPF-Heston
2.70104e-05
1.34534e-05
EPF-GARCH
2.48733e-05
4.99337e-06
EPF-3/2
2.26462e-05
2.58645e-06
UPF-Heston
2.04000e-05
2.74818e-06
UPF-GARCH
2.63036e-05
8.44030e-07
UPF -3/2
1.73857e-05
4.09918e-06

The Inference Problem
123
0
1e-05
2e-05
3e-05
4e-05
5e-05
6e-05
7e-05
0
200
400
600
800
1000
1200
Errors
Days
EKF Errors for Various SV Models
Heston
GARCH
3/2
FIGURE 2.26
Comparison of EKF Filtering Errors for Heston, GARCH, and 3/2
Models. The latter seems to perform better.
0
2e-05
4e-05
6e-05
8e-05
0.0001
0.00012
0
200
400
600
800
1000
1200
Errors
Days
UKF Errors for Various SV Models
Heston
GARCH
3/2
FIGURE 2.27
Comparison of UKF Filtering Errors for Heston, GARCH, and 3/2
Models. The latter seems to perform better.
Two immediate observations can be made: On one hand, particle filters
have a better performance than do the Gaussian, which reconfirms what one
would anticipate. On the other hand, for most of the filters, the 3/2 model
seems to outperform the Heston model, which is in line with the findings
of Engle & Ishida [95]. Again, this shows that the filtering process could be

124
INSIDE VOLATILITY ARBITRAGE
5e-06
1e-05
1.5e-05
2e-05
2.5e-05
3e-05
3.5e-05
4e-05
4.5e-05
5e-05
5.5e-05
0
200
400
600
800
1000
1200
Errors
Days
EPF Errors for Various SV Models
Heston
GARCH
3/2
FIGURE 2.28
Comparison of EPF Filtering Errors for Heston, GARCH, and 3/2
Models. The latter seems to perform better.
1.2e-05
1.4e-05
1.6e-05
1.8e-05
2e-05
2.2e-05
2.4e-05
2.6e-05
2.8e-05
0
200
400
600
800
1000
1200
Errors
Days
UPF Errors for Various SV Models
Heston
GARCH
3/2
FIGURE 2.29
Comparison of UPF Filtering Errors for Heston, GARCH, and 3/2
Models. The latter seems to perform better.
used not only for parameter estimation but also for model identification. This
suggests further filtering on other existing models, such as jump diffusion
[190]. Clearly, because of the non-Gaussianity of jump-based models, the
particle filtering technique will need to be applied to them.

The Inference Problem
125
0
1e-05
2e-05
3e-05
4e-05
5e-05
6e-05
7e-05
200
400
600
800
1000
1200
Errors
Days
Heston Model Errors for Various Filters
EKF
UKF
EPF
UPF
FIGURE 2.30
Comparison of Filtering Errors for the Heston Model. PFs seem to
perform better.
0
1e-05
2e-05
3e-05
4e-05
5e-05
6e-05
7e-05
8e-05
200
400
600
800
1000
1200
Errors
Days
GARCH Model Errors for Various Filters
EKF
UKF
EPF
UPF
FIGURE 2.31
Comparison of Filtering Errors for the GARCH Model. PFs seem to
perform better.
Parameter Learning Revisited
We tried a joint filter (JF) via the Kalman filter
where the parameters were given a prior distribution. We can now apply
the particle filtering techniques to this framework as in [176] and [224]: We
simulate x(i)
k at time step k from the prior p(xk|x(i)
k−1), and we also simulate

126
INSIDE VOLATILITY ARBITRAGE
0
1e-05
2e-05
3e-05
4e-05
5e-05
6e-05
7e-05
200
400
600
800
1000
1200
Errors
Days
3/2 Model Errors for Various Filters
EKF
UKF
EPF
UPF
FIGURE 2.32
Comparison of Filtering Errors for the 3/2 Model. PFs seem to perform
better.
each parameter ψ(i) from its prior q(ψ) = N(mψ sψ) where these mean and
standard deviations are to be determined.
We then update the priors by incorporating the observation zk
p

x(i)
k |zk

∝p

zk|x(i)
k  ψ(i)
p

x(i)
k |x(i)
k−1

and similarly
p(ψ(i)|zk) ∝p(zk|x(i)
k  ψ(i))p(ψ(i)|x(i)
k−1)
and we obtain the posterior distributions. Calling
w(i)
k =
p

zk|x(i)
k  ψ(i)
w(i)
k−1
 Nsims
i=1
p

zk|x(i)
k  ψ(i)
w(i)
k−1
We now have the posteriors of xk and ψ, and we can simulate them for the
following step via a Metropolis-Hastings (MH) accept/reject technique with
the proposal distribution q(ψ mψ sψ) with
mψ =
Nsims

i=1
w(i)
k ψ(i)
and
sψ =
Nsims

i=1
w(i)
k

ψ(i) −mψ
2

The Inference Problem
127
TABLE 2.2
The True Parameter Set ∗Used for Data Simulation
∗
ω∗= 0.10
θ∗= 10.0
ξ∗= 0.03
ρ∗= −0.50
TABLE 2.3
The Initial Parameter Set 0 Used for the Optimization Process
0
ω0 = 0.15
θ0 = 15.0
ξ0 = 0.02
ρ0 = −0.50
The MH step will consist of the following. We accept the simulation point
˜ψ
(i) from q() with a probability α(ψ(i) ˜ψ
(i)), where ∀i between 1 and Nsims
we have
α

ψ(i) ˜ψ
(i)
= min

1.0
p

˜ψ
(i)|zk

/q

˜ψ
(i)
p

ψ(i)|zk

/q

ψ(i)


In practice, we simulate a uniform random variable u and accept the sim-
ulated point ˜ψ
(i) if α > u, and reject it (and keep ψ(i)) otherwise. We keep
simulating alternatively the state variable and each parameter by incorpo-
rating the observations at each step and wait for the parameters to converge
to their ideal mean.
It is important to note that this joint filtering differs from the usual
MCMC techniques, such as in [156] and [92], where we update the particles
by incorporating all observations at each simulation step.
The Performance of the Inference Tools
We have applied various Gaussian and particle-based filters to daily historic
data. None of the methodologies performed very well at that frequency.26
We now try to analyze the reasons.
A known weakness of optimization algorithms is the following. The
higher the number of parameters, the worse the performance of the algo-
rithm. This means that a one-parameter optimization should perform best.
To test this, we simulate 5000 points27 via the Heston model with a param-
eter set ∗as shown in the following (also see Figure 2.33).
26Note that in this section we are not checking the validity of the assumption that
the real stock market follows a Heston (or another) process. We assume we know
the process exactly and try to recover the embedded parameters.
27We made the 5000 daily simulations directly from the discretized SDE with a
t = 1/252 . We also tried simulating 5 000 000
points with t = 1/252 000
and sampling 5000 daily points from there. Although the second method is more

128
INSIDE VOLATILITY ARBITRAGE
40
60
80
100
120
140
160
180
200
0
500
1000 1500 2000 2500 3000 3500 4000 4500 5000
Simulated Prices via Heston
Stock Price
FIGURE 2.33
Simulated Stock-Price Path via Heston Using ∗. This is an artificial
time series following the Heston model.
We use a drift of µS = 0.025 and a time step t = 1/252 as before. In
order to get the best performance, we fix all parameters except one. For
instance, to obtain ˆω we fix θ = 10.0 ξ = 0.03 ρ = −0.50 µS = 0.025; we
choose a reasonable initial point ω0 and then optimize upon ω only. We
choose an initial parameter set 0 as will be shown. The results are displayed
in Table 2.4.
TABLE 2.4
The Optimal Parameter Set ˆ
. The estimation is performed individually
for each parameter on the artificially generated time series. Particle filters use 1000
simulations.
Filter
ˆω
ˆθ
ˆξ
ˆρ
EKF
0.098212
10.188843
0.052324
−0.873571
UKF
0.107281
10.089381
0.000001
+0.598434
EPF
0.098287
10.130531
0.044437
−0.827729
UPF
0.100581
10.221816
0.051902
−0.487695
correct, the difference in results was small, which means that the Euler discretization
is sufficiently accurate at the daily level. This is in agreement with results found by
Elerian [92].

The Inference Problem
129
–53000
–52000
–51000
–50000
–49000
–48000
–47000
–46000
0
0.2
0.4
0.6
0.8
1
1.2
Omega
Log Likelihood
Log likelihood
Optimum
FIGURE 2.34
f (ω) = L(ω ˆθ ˆξ ˆρ) Has a Good Slope Around ˆω = 0.10.
It is interesting to note that the estimation of the volatility-drift parame-
ters (ω θ) could be done fairly well via EKF.28 This makes sense because the
dependence on these parameters is linear.
The estimation of volatility and correlation parameters (ξ ρ) is not as
straightforward. This could be seen by plotting the likelihood L() as a
function of ω, θ, ξ, and ρ separately. We fix three parameters to their optimal
values and plot L() as a function of the last one. We observe in Figures 2.34
through 2.37 that the likelihood function is fairly easy to optimize for (ω θ).
However, the function is very flat around the optimal ξ and ρ. Therein lies
the difficulty of finding the optimums!
Sample Size
It seems therefore that the estimation is inefficient for the
parameter ξ no matter which filter we use. The issue is that of inefficiency
(large error variance) for this given sample size. This is indeed one of the
shortcomings of maximum likelihood estimators (MLE). For a given sample
size, they can very well be inefficient and even have a bias.29 The choice
of the filter will not solve this problem. However, under minimal regularity
28A joint estimation of (ωθ) based on the same data set with known (ξρ) provides
( ˆω = 0.117889 ˆθ = 11.996760).
29A known and simple example for the bias of MLEs is that of estimating the
variance of a Gaussian sequence of a finite size (x1 ... xN). The ML estimate
for the mean is ˆµN
=
1
N
 N
k=1xk, and the ML estimate for the variance is

130
INSIDE VOLATILITY ARBITRAGE
–52800
–52700
–52600
–52500
–52400
–52300
–52200
–52100
4
6
8
10
12
14
16
Theta
Log Likelihood
log-likelihood
optimum
FIGURE 2.35
f (θ) = L( ˆωθ ˆξ ˆρ) Has a Good Slope Around ˆθ = 10.0.
–52800
–52700
–52600
–52500
–52400
–52300
–52200
–52100
0
0.2
0.4
0.6
0.8
1
1.2
Xi
Log Likelihood
Log likelihood
Optimum
FIGURE 2.36
f (ξ) = L( ˆω ˆθξ ˆρ) Is Flat Around ˆξ = 0.03.
ˆvN =
1
N
 N
k=1(xk −ˆµN)2. The latter ML estimation is biased, and the correct
estimation would be ˆˆvN =
1
N−1
 N
k=1(xk −ˆµN)2. However, it is clear that as
N →+∞we have ˆvN ≈ˆˆvN and the bias gradually disappears.

The Inference Problem
131
–52780
–52775
–52770
–52765
–52760
–52755
–52750
–1
–0.8
–0.6
–0.4
–0.2
0
0.2
0.4
0.6
Rho
Log Likelihood
log-likelihood
optimum
FIGURE 2.37
f (ρ) = L( ˆω ˆθ ˆξρ) Is Flat and Irregular Around ˆρ = −0.50.
conditions, MLEs are consistent and therefore asymptotically converge to
the correct optimum. This means that the sample size is key. To test this, we
can choose larger samples of N = 50 000, N = 100 000, and N = 500 000
points and rerun the simplest filter, namely, the EKF. As expected, the opti-
mum of the likelihood function becomes closer and closer to ξ∗. This can be
seen in Figures 2.38 to 2.41 as well as in Table 2.5. The same exact observa-
tions could be made for the correlation parameter ρ, and the results are also
displayed in Table 2.5. The likelihood graphs are omitted in the interest of
brevity.
As for the drift parameters ω and θ, the convergence was good even for
N = 5000, as previously observed. Unfortunately, in reality we have limited
historic data. Even at a daily frequency, 50 000 points would correspond to
200 years!
One possibility would be to use intra-day data; however, that assumes
that the behavior of the stock price is the same intra-day (which is reasonable
considering we started with a continuous SDE). Moreover, clean intra-day
data is usually not readily available and needs preprocessing. Therefore,
having p parameters in the optimal parameter set ˆN =
 ˆN[j]

1≤j≤p for
a sample size N, we have for each parameter [j]
lim
N→+∞
ˆN[j]
|
"
[k] = ∗[k]; 1 ≤k ≤p; k ̸= j
#
= ∗[j]
(2.28)
What is more, this is true for any valid initial value 0[j], which means the
MLE is robust.

132
INSIDE VOLATILITY ARBITRAGE
–45698
–45697.5
–45697
–45696.5
–45696
–45695.5
–45695
–45694.5
–45694
0.02
0.03
0.04
0.05
0.06
0.07
0.08
0.09
0.1
Xi
Log Likelihood
Log likelihood
FIGURE 2.38
f (ξ) = L( ˆω ˆθξ ˆρ) via EKF for N = 5000 Points. The true value is
ξ∗= 0.03.
TABLE 2.5
The Optimal EKF Parameters ˆξ and ˆρ Given a Sample Size N. The true
parameters are ξ∗= 0.03 and ρ∗= −0.50. The initial values were ξ0 = 0.02 and
ρ0 = −0.40.
N
ˆξ
ˆρ
5000
0.052324
−0.873571
50 000
0.036463
−0.608088
100 000
0.033400
−0.556868
500 000
0.031922
−0.532142
Joint Estimation of the Parameters
Let us now assume that we do not know
any of the parameters; we choose an initial set 0 and test the consistency
of the MLE. We shall apply the EKF to the data and take the same true
parameter set ∗as in the previous section. We assume that µS = 0.025 is
known; otherwise, it could be estimated together with the model parameters.
As previously mentioned, the likelihood function becomes flat and there-
fore harder to maximize under a higher number of parameters. The
convergence of the estimator will therefore be slower. Despite this, we can
observe in Table 2.8 the asymptotic convergence of the estimator even under
the joint estimation of all parameters. We have now
lim
N→+∞
ˆN = ∗
(2.29)

The Inference Problem
133
TABLE 2.6
The True Parameter Set ∗Used for Data Generation
∗
ω∗= 0.10
θ∗= 10.0
ξ∗= 0.03
ρ∗= -0.50
TABLE 2.7
The Initial Parameter Set 0 Used for the Optimization Process
0
ω0 = 0.15
θ0 = 15.0
ξ0 = 0.02
ρ0 = -0.40
TABLE 2.8
The Optimal EKF Parameter Set
ˆ
 Given a Sample Size N. The four
parameters are estimated jointly.
N
ˆω
ˆθ
ˆξ
ˆρ
5000
0.150854
15.294576
0.266175
−0.128835
50 000
0.126387
12.748852
0.020521
−1.000000
100 000
0.136023
13.700906
0.044353
−0.439961
500 000
0.100097
10.030336
0.061688
−0.257305
1 000 000
0.105264
10.548642
0.043818
−0.356234
2 000 000
0.103183
10.334876
0.039767
−0.374677
4 000 000
0.105292
10.538019
0.043288
−0.347562
5 000 000
0.101097
10.118951
0.028588
−0.514346
which corresponds to the generalization of (2.28) in the previous section.
We ran other filters (UKF, EPF, UPF) on the same data set and observed
only marginal improvement. The results are omitted in the interest of brevity.
It therefore seems that the fundamental issue is related to the slow conver-
gence of the MLEs regardless of the filtering method.
A related issue previously mentioned is the size of the observation error
Uk ∝
√
t, which is large compared with the observation function Hk ∝t
for daily observations.
Error Size Revisited
As previously mentioned, this underlines the more fun-
damental problem for the SV estimation: By definition, volatility represents
the noise of the stock process. Indeed if we had taken the spot price Sk as
the observation and the variance vk as the state, we would have
Sk+1 = Sk + SkµSt + Sk
√vk
√
tBk
we would then have an observation function gradient H = 0 and the system
would be unobservable! It is precisely because we use a Taylor second-order

134
INSIDE VOLATILITY ARBITRAGE
–457110
–457109
–457108
–457107
–457106
–457105
–457104
–457103
–457102
–457101
–457100
0.02
0.025
0.03
0.035
0.04
0.045
0.05
Xi
Log Likelihood
Log likelihood
FIGURE 2.39
f (ξ) = L( ˆω ˆθξ ˆρ) via EKF for N = 50 000 Points. The true value is
ξ∗= 0.03.
–914118
–914116
–914114
–914112
–914110
–914108
–914106
–914104
0.02
0.025
0.03
0.035
0.04
0.045
0.05
Xi
Log Likelihood
Log likelihood
FIGURE 2.40
f (ξ) = L( ˆω ˆθξ ˆρ) via EKF for N = 100 000 Points. The true value
is ξ∗= 0.03.

The Inference Problem
135
–4.56816e+06
–4.56816e+06
–4.56815e+06
–4.56814e+06
–4.56814e+06
–4.56814e+06
–4.56813e+06
–4.56812e+06
–4.56812e+06
–4.56812e+06
–4.56811e+06
0.02
0.025
0.03
0.035
0.04
0.045
0.05
Xi
Log Likelihood
Log likelihood
FIGURE 2.41
f (ξ) = L( ˆω ˆθξ ˆρ) via EKF for N = 500 000 Points. The true value
is ξ∗= 0.03.
expansion
ln(1 + x) ≈x −1
2x2
that we obtain access to vk through the observation function. However, in
ln
Sk+1
Sk
	
=

µS −1
2vk
	
t + √vk
√
tBk
the error remains dominant as the first order of the expansion.30 Harvey,
Ruiz, and Shephard [130] use the approximation t = o(
√
t) and take
zk = ln

ln2
Sk+1
Sk
		
≈ln(vk) + ln(t) + ln

B2
k

Note that under this form EKF would blow up because z−
k = h(vk 0) =
−∞. They therefore use the fact that E[ln(B2
k)] = −1.27 and stdev[ln(B2
k)] =
30Note that this is different from a variance Swap where we work with the expected
values. The approximation is perfectly valid if for the return R = S/S we write
E[ln(1 + R) −R] ≈−1
2v
but again, the approximation breaks if we work for one sample path.

136
INSIDE VOLATILITY ARBITRAGE
TABLE 2.9
The Optimal EKF Parameter Set
ˆ
 via the HRS Approximation Given
a Sample Size N. The four parameters are estimated jointly.
N
ˆω
ˆθ
ˆξ
ˆρ
5000
0.722746
71.753861
0.044602
−1.000000
50 000
0.234110
23.575193
0.028056
−1.000000
100 000
0.150512
15.186113
0.017748
−1.000000
500 000
0.109738
11.020391
0.027140
−0.531481
π/
√
2 and consider the Gaussian approximation
ln

B2
k

∼−1.27 + π
√
2
N(0 1)
which may or may not be valid. We call this approximation Harvey-Ruiz-
Shephard (HRS) and apply it to the same case as in the previous paragraphs.
As can be seen in Table 2.9, the approximation seems to be valid for our
example. Note that UKF would not have this problem because we would
work with the real nonlinear function z = h(x u). However, we would still
deal with logs of very small quantities, which could be numerically unstable.
Another way of tackling the same equation would be via a particle filter,
where
zk = ln
ln
Sk+1
Sk
	
	
≈1
2 ln(vk) + 1
2 ln(t) + ln(|Bk|)
and as stated in [10] the density of ln(|Bk|) is
f (x) = 2exn(ex)
with n() the normal density.31
Testing the same data set provides Table 2.10, which does not seem to
improve upon the KF.
It is important to note that even if we took the example of the Heston
model, the same issues are true for any stochastic volatility model of type
vk = vk−1 + (ω −θvk−1) t + ξvp
k−1
√
tZk−1
31It is easy to see that if X is a standard normal variable, then the CDF of ln(|X|) is
F(x) = P(ln(|X|) ≤x) = P

|X| ≤ex
= P

−ex ≤X ≤ex
therefore
F(x) = N

ex
−N

−ex
= 2N(ex) −1
and the density is determined by taking the derivative with respect to x as usual.

The Inference Problem
137
TABLE 2.10
The Optimal PF Parameter Set
ˆ
 Given a Sample Size N. The four
parameters are estimated jointly.
N
ˆω
ˆθ
ˆξ
ˆρ
5000
0.147212
14.999999
0.070407
-0.555263
including the GARCH diffusion and the 3/2 models. As previously men-
tioned, even if the transition equation is different here, the observation equa-
tion remains the same. Applying the EKF, we have the transition matrix and
noise
Ak = 1 −

ρξµS

p −1
2
	
v
p−3
2
k−1 + θ −1
2ρξ

p + 1
2
	
v
p−1
2
k−1

t
+

p −1
2
	
ρξv
p−3
2
k−1 ln
 Sk
Sk−1
	
Wk = ξ

1 −ρ2vp
k−1
√
t
However, we still have the observation matrix and noise
Hk = −1
2t
and
Uk = √vk
√
t
and the same problem of t = o
√
t

still exists at observation level for
any value of p.
Another point that should be mentioned is that even if ξ and ρ are sep-
arately harder to estimate than ω and θ, the product ρξ appears in the equa-
tions at the same level. Indeed, as we just saw, in Ak only the product ρξ is
available. However, at the noise level Wk, we can distinguish the two param-
eters ρ and ξ. For instance, in our previous EKF joint estimation table, we
had for 50 000 points ˆξ ≈0.020521 , ˆρ ≈−1.0000 and again, the individual
estimations of ξ and ρ remained far from their true values. However, we
have ˆξˆρ ≈−0.020521, which is much closer to ξ∗ρ∗= −0.015. Interestingly,
the product ρξ is what we need to determine the skewness of the distribu-
tion.32 However, we do need to determine ξ alone to obtain the distribution
kurtosis.
It is also worth noting that in a GARCH framework, we do not have
this problem of poor observability for the discrete case. In fact, at each
32This remark will be addressed in the following chapter.

138
INSIDE VOLATILITY ARBITRAGE
TABLE 2.11
Real and Optimal Parameter Sets Obtained via NGARCH MLE. The
5000 points were generated via the one-factor NGARCH with daily parameters.
ω
α
β
c
∗
0.00000176
0.0626
0.89760
0.00
ˆ
0.00000200
0.0530
0.89437
0.05
point in time, vk is known exactly as a function of previous observations.
Only later, we go to the two-factor diffusion limit, as Nelson [194] does.
However, we have to bear in mind that this GARCH diffusion limit is a
very special case of the stochastic volatility problem, since it misses the sec-
ond source of randomness in the discrete case. As Corradi [61] explains, a
discrete GARCH model may very well converge toward a one-factor dif-
fusion process without stochastic volatility. Interestingly, when discretizing
the one-factor continuous process, we can recover GARCH, whereas when
discretizing the two-factor continuous process we will not obtain GARCH
but the two-factor discrete process we have been working with.
This explains why GARCH MLE (without filtering) can recover param-
eters used in a simulated time series of length 5000 created via a one-factor
GARCH process, whereas it cannot recover the diffusion-limit parameters
from a time series created via a two-factor stochastic volatility process as
accurately.33 One can see this in Tables 2.11 and 2.12.
This also explains why estimating ω and θ alone works so much better
with 5000 points. After all, if we had ξ = 0 and therefore a deterministic
33Needless to say, whether the equations are written via yearly (stochastic volatility
convention) or daily (GARCH convention) parameters will not change the nature of
the problem. It would be tempting to try to get around the t = o(
√
t) problem
by rewriting the equations via daily parameters µd
S = µSt and vd
k = tvk as well
as ωd = t2ω, θd = tθ and ξd = tξ with ρ remaining unchanged. Dropping the
superscript d for simplifying the notations, we shall have
ln Sk+1 = ln Sk + µS −1
2vk + √vkBk
vk+1 = vk + ω −θvk + ξ√vkZk
which seems to have eliminated the difficulty. However, now we have
vk = o(√vk)
which was not the case with yearly variances, and the same poor observability
problem arises again! We therefore see that the heart of the difficulty is a low
signal-to-noise ratio (SNR) for the problem at hand.

The Inference Problem
139
TABLE 2.12
Real and Optimal Parameter Sets Obtained via NGARCH MLE as well
as EKF. The 5000 points were generated via the two-factor GARCH diffusion limit
with annual parameters.
ω
θ
ξρ
∗
0.100000
10.00
−0.015
ˆGARCH
0.063504
6.84
−0.019
ˆEKF
0.148000
14.48
−0.023
instantaneous variance, we would have no observability problem to talk
about. Indeed, vt would be exactly known at each time step, as is the case in
a GARCH framework.
Finally, we can now see better why the estimation worked fairly well
even with 200 points if t = 1 year—simply because we do not have t =
o(
√
t) and the observability is much more accurate. Nevertheless, with such
a large t, other problems, such as strong nonlinearity and the nonapplica-
bility of the Grisanov theorem arise. Not to mention the fact that 200 points
would correspond to 200 years of data!
High-Frequency Data
Given that the results seem to converge for a large num-
ber of data points, one idea would be to use a higher sampling frequency.
If instead of using daily data we sample every five seconds, then with a
ten-year range we will have 10 × 252 × 6.5 × 60 × 60 ÷ 5 = 11 793 600 data
points, which is very sufficient for our MLEs. For testing the use of high-
frequency data, we can generate via Monte Carlo 5 000 000 points with a
t = 1/252 000 , which corresponds to 20 years. We obtain the results in
Table 2.13. Both rows have reasonable results. It is, however, notable that
the EKF/HRS method seems to perform better than the plain EKF.
It may seem a little surprising that for the same time period [0 T ] div-
iding t by 1000 and multiplying N by 1000 helps us. Why don’t the
TABLE 2.13
The Optimal Parameter Set
ˆ
 for 5 000 000 Data Points. The sam-
pling is performed 1000 times a day and therefore the data set corresponds to 5000
business days. The four parameters are estimated jointly.
ˆω
ˆθ
ˆξ
ˆρ
EKF
0.090280
9.019962
0.042984
−0.283236
EKF/HRS
0.092372
9.224421
0.030951
−0.507763

140
INSIDE VOLATILITY ARBITRAGE
two operations cancel one another? Observing the negative of log-likelihood
function in an EKF framework
φ(ω θ ξ ρ) =
N

k=1

ln(Fk) + ˜z2
k
Fk

with
˜zk = zk −h(ˆx−
k  0)
and
Fk = HkP−
k Ht
k + UkUt
k
We can see that considering first-order terms, dividing t by 1000, or equiva-
lently multiplying it by ϵ = 1/1000 , will cause the transition matrix Ak to be
unchanged, the transition noise Wk to be multiplied by √ϵ , the observation
matrix Hk to be multiplied by ϵ, and the observation noise Uk to be multiplied
by √ϵ. Furthermore, Ak being unchanged will cause P−
k and Pk to remain
unchanged as well. Therefore, ˜zk will be multiplied by √ϵ, the term Fk will
be multiplied by ϵ, and the fraction used in the log-likelihood sum will remain
the same. This causes the sum φ(ω θ ξ ρ) to be higher by a factor 1/ϵ, which
shows that higher frequency does allow us to obtain a higher likelihood
function and therefore better convergence. This is in agreement with what
we observed in the above test.
The Frequency of the Observations
Note that the ideal stochastic differential
equations are supposed to be continuous; however, we only have discrete
observations obtained via an Euler scheme. This introduces a discretization
error that may become important as the time interval t becomes larger.
As mentioned in [92], [164], and [201], the solution would be to fill the
missing data via additional simulations in time: For the observation time
step 1 ≤k ≤N, the simulation 1 ≤i ≤Nsims , and the additional time step
1 ≤j ≤M , we would have the particles
˜x(i)
k+ j
M
= ˜x(i)
k+ j−1
M
+

ω −θ˜x(i)
k+ j−1
M
	 t
M + ξ
$
˜x(i)
k+ j−1
M
$
t
M Z(i)
k+ j
M
and the observation
zk+1 = zk +
M

j=1

µS −1
2 ˜xk+ j
M
	 t
M +




M

j=1
˜xk+ j
M
t
M Bk
where each Z(i)
k+ j
M
has a correlation ρ with Bk. Naturally, the innovations Zl
are mutually uncorrelated. However, as discussed in [164], the discretization
error is small when t = 1/252, which is the case we are dealing with.

The Inference Problem
141
TABLE 2.14
Mean and (Standard Deviation) for the Estimation of Each Parameter
via EKF Over P = 500 Paths of Lengths N = 5000 and N = 50 000. The true values
are (ω∗= 0.10θ∗= 10ξ∗= 0.03ρ∗= −0.50).
ˆω
ˆθ
ˆξ
ˆρ
N = 5000
0.11933899
11.92271488
0.056092146
−0.34321724
(0.098995729) (9.673829518) (0.049741887) (0.297433861)
N = 50 000 0.102554592
10.26233092
0.04383931
−0.351998284
(0.027020734) (2.706564396) (0.013004526) (0.074998408)
Sampling Distribution
Even if in practice we deal with one historic path, we
should determine the distribution of the optimal parameter set as follows.
We simulate P = 500 paths of length N = 5000 and estimate for each path
j the optimal set ˆ(j). We then can estimate
¯ˆ = 1
P
P −1

j=0
ˆ(j)
as well as the variance
V ( ˆ) = 1
P
P −1

j=0
( ˆ(j) −¯ˆ)2
In this way we will know how the estimator performs on average and
how far we could be from this average. The distribution of the parameter set
around its mean is referred to as the sampling distribution [168]. As we can
see in Table 2.14, the average-estimated parameter set is closer to the true set
than the one-path-estimated set we were considering in the previous section.
However, the corresponding standard deviation is quite high and we could
very well get poor results as previously seen.
From Figures 2.42 to 2.45, we can see that for this data length N and
this sample size P the parameters ω and θ are determined via EKF in a
fairly unbiased way. However, the estimator is not efficient and has a large
standard deviation. As for ξ and ρ, we have both bias and inefficiency. This is
not surprising given the results of the previous paragraphs. We obtained good
results for (ω θ) when estimated alone, and not so good results for (ξ ρ). As
mentioned, classical filtering theory works well when the parameters affect
the drift of the observation and not the noise. This causes a slow convergence
problem for all our parameters. But this is doubly true for (ξ ρ) since they

142
INSIDE VOLATILITY ARBITRAGE
0
20
40
60
80
100
120
140
0
0.05
0.1
0.15
0.2
0.25
0.3
Omega
Density
Histogram
FIGURE 2.42
Density for ˆω Estimated from 500 Paths of Length 5000 via EKF. The
true value is ω∗= 0.10. The sampling distribution is fairly unbiased, but is inefficient.
0
20
40
60
80
100
120
140
0
5
10
15
20
25
30
Theta
Density
Histogram
FIGURE 2.43
Density for ˆθ Estimated from 500 Paths of Length 5000 via EKF. The
true value is θ∗= 10 . The sampling distribution is fairly unbiased, but is inefficient.

The Inference Problem
143
0
10
20
30
40
50
60
70
80
0
0.02
0.04
0.06
0.08
0.1
0.12
0.14
0.16
Xi
Density
Histogram
FIGURE 2.44
Density for ˆξ Estimated from 500 Paths of Length 5000 via EKF. The
true value is ξ∗= 0.03 . The sampling distribution is inefficient and even has a bias.
0
50
100
150
200
250
–1
–0.8
–0.6
–0.4
–0.2
0
0.2
0.4
0.6
Rho
Density
Histogram
FIGURE 2.45
Density for ˆρ Estimated from 500 Paths of Length 5000 via EKF. The
true value is ρ∗= −0.50 . The sampling distribution is inefficient and even has a bias.

144
INSIDE VOLATILITY ARBITRAGE
affect the “noise of the noise.” As previously observed, the bias and ineffi-
ciency will disappear as N →+∞, as is the case for any MLE estimator.
The biases and the standard deviations are smaller for N = 50 000 than for
N = 5000 as we can see in Table 2.14.
The Bayesian Approach
Even if our method of choice is the classical one, it is worth going over the
Bayesian philosophy and methodologies, which have some similarities but
also some fundamental differences compared with our point of view. The
MLE methodology is a classical (frequentist) approach, in which we assume
that there is a set of unknown but fixed parameters. Alternatively, in the
Bayesian approach the parameters are considered as random variables with
a given prior distribution. We then use the observations (the likelihood) to
update these distributions and obtain the posterior distributions.
It would seem that in order to be as objective as possible and to use the
observations as much as possible, one should use priors that are noninfor-
mative. However, this sometimes creates degeneracy issues and one should
choose a different prior for this reason.
Markov Chain Monte Carlos (MCMC) include the Gibbs sampler as
well as the Metropolis-Hastings (MH) algorithm. The theoretical justifica-
tion is provided by the Hammersley-Clifford theorem and the ergodic aver-
aging theorem. Details can for instance, be found in [34] or [163].
Briefly, the Hammersley-Clifford theorem states that having a param-
eter set , a state x, and an observation z, we can obtain the joint distri-
bution p( x|z) from p(|x z) and p(x| z), under some mild regularity
conditions. Therefore by applying the theorem iteratively, we can break a
complicated multidimensional estimation problem into many simple one-
dimensional problems. Creating a Markov Chain (i) via a Monte Carlo
process, the ergodic averaging theorem states that the time average of a par-
ameter will converge toward its posterior mean.
The Gibbs Sampler
The Gibbs sampler consists of iterative simulations from
the posterior distributions. Having a parameter set
 = (j )1≤j≤J
a hidden state
x = (xk)1≤k≤N
and an observation set
z = (zk)1≤k≤N

The Inference Problem
145
We proceed as follows: Initialize the state vector and the parameter set
to x(0) and (0), and choose the prior distribution p(ψ). For each simulation
index i between 1 and Nsims, do:
1. Simulate x(i) as
x(i) ∼p(x|z (i−1))
2. Simulate each parameter from its posterior conditional on partially
updated parameters: For each j between 1 and J
(i)
j
∼p(ψ|z x (i)
0  ... (i)
j−1  (i−1)
j+1  ... (i−1)
J
)
with
p(ψ|z x ...) ∝p(z|x ψ ...)p(x|ψ)p(ψ)
3. Go back to Step 1 and stop after i reaches Nsims.
4. Calculate the posterior mean for each parameter after allowing a “burn-
in" period
ˆj =
1
Nsims −i0
Nsims

i=i0+1
(i)
j
with, for instance, i0 = Nsims/10.
It is important to note that in some cases, the prior and the posterior
distributions are the same and only differ in parameters. In this case the
priors are referred to as conjugate priors.
The justification is available for instance in [55] and can be summed up
as follows: Having two random variables (X Y), we can write
E[X] =

xp(x)dx
but
p(x) =

p(x|y)p(y)dy =

p(x|y)

p(y|ξ)p(ξ)dξdy
therefore, we have
p(x) =

p(ξ)h(x ξ)dξ
with
h(x ξ) =

p(x|y)p(y|ξ)dy
which shows that p(x) is a stationary solution for the foregoing integral
equation, and h(x ξ) corresponds to the limit transition density.

146
INSIDE VOLATILITY ARBITRAGE
Similarly, it is possible to show that for a sequence (xk) generated from
a Gibbs Sampler, we have
P (xk|x0) =

P (xk−1|x0)P(xk xk−1)dxk−1
It is therefore possible to see that as k →+∞we have
P (xk|x0) →p(xk)
and
P (xk|xk−1) →h(xk xk−1)
which are the stationary marginal and transition densities.
A Simple Illustration
For a simple illustration, consider a sequence of normally
distributed data points z with an unknown mean µ and an unknown variance
1/λ. The parameter λ is often referred to as the precision of the distribution.
One possible way to proceed is to choose uniform (noninformative) priors
p(µ) and p(λ) ∝1/λ and use the known results [34]
p(µ|z σ) = N( ¯Z σ)
with N(m s) the normal distribution with mean m and standard deviation s
and
¯Z = 1
N
N

k=1
zk
as well as
p(λ|z µ) = G
N
2  S
2
	
with G(a A) the previously described gamma distribution34 and
S =
N

k=1
(zk −µ)2
and again
σ = 1/
√
λ
We therefore know both posterior distributions and can simulate from them
iteratively and perform Gibbs sampling as described above.
34Note that G(a A) = P(a Ax) to use our previous notations.

The Inference Problem
147
9.2
9.4
9.6
9.8
10
10.2
10.4
10.6
0
1000 2000 3000 4000 5000 6000 7000 8000 9000 10000
Simulation
Gibbs Sampler for the Normal Mean
mu
FIGURE 2.46
Gibbs Sampler for µ in N(µσ). The true value is µ∗= 10.0.
For testing this, we generated a time series of 1000 Gaussian points with
a mean of µ∗= 10 and a standard deviation of σ∗= 5. We applied the Gibbs
sampler via Nsims = 10 000 simulations and considered the average between
the 1000th and 10 000th simulations. We chose initial values µ0 = 7.0 and
σ0 = 3.0 and obtained
ˆµ = 9.943416
ˆσ = 4.816300
We ploted the simulations from the posteriors in Figures 2.46 and 2.47.
The Metropolis-Hastings Algorithm
The Gibbs sampler is fast and simple when
the posterior distributions are known and easy to sample from. However, in
practice, and in particular for our stochastic volatility problem, this often is
not the case. We assume for simplicity that we do know the posteriors for
the parameters and therefore can use the Gibbs sampler for them; however,
we cannot do the same for the latent state.
In this case, the Metropolis-Hastings (MH) algorithm approach can be
used for x as follows: Initialize the state vector and the parameter set to
x(0) and (0) and choose the prior distribution p(ψ). Also choose a proposal
distribution q(x|z ) for the state. For each simulation index between 1 and
Nsims do:
1-a. Simulate from the proposal distribution
x(i) ∼q(x|z )

148
INSIDE VOLATILITY ARBITRAGE
4.4
4.6
4.8
5
5.2
5.4
5.6
5.8
0
1000 2000 3000 4000 5000 6000 7000 8000 9000 10000
Simulation
Gibbs Sampler for the Normal Standard Deviation
Sigma
FIGURE 2.47
Gibbs Sampler for σ in N(µσ). The true value is σ∗= 5.0.
1-b. Compare with a randomly generated uniform random variable u the
ratio
α = min

1
p(x(i)|z )/q(x(i)|z )
p(x(i−1)|z )/q(x(i−1)|z )
	
and accept x(i) if α > u; otherwise, reject it and set x(i) = x(i−1).
2. Simulate (i) via a Gibbs sampler.
3. Go back to Step 1-a and continue until i reaches Nsims.
4. Calculate the posterior mean for each parameter after allowing a
“burn-in” period
ˆj =
1
Nsims −i0
Nsims

i=i0+1
(i)
j
with, for instance, i0 = Nsims/10.
Two special cases are worth being mentioned.
■First, if we simulate from the posterior, the MH ratio becomes 1.0 and
every simulation will be accepted. This is therefore a Gibbs sampler.
■Second, if we simulate from the prior, the MH ratio becomes the like-
lihood ratio, which makes the computation simpler. We shall use this
second case extensively in our stochastic volatility inferences.

The Inference Problem
149
The justification for the MH algorithm is available, for instance, in [58]
or [120]. The idea is to find the transition probability from x to y P(x y) such
that for a given target density π we would have the invariant distribution
property
π(dy) =

P (x dy)π(x)dx
It is possible to express the transition probability P(x dy) as
P(x dy) = p(x y)dy +

1 −

p(x z)dz
	
δx(dy)
with δx() the Dirac function. The first term corresponds to the passage prob-
ability from x to a point in dy and the second term to the probability of
staying at x.
Now, if the function p(x y) satisfies the reversibility condition
π(x)p(x y) = π(y)p(y x)
then we can see that π() is the invariant distribution as described previously.
Indeed then calling the rejection probability
r(x) = 1 −

p(x z)dz
we have

P(x A)π(x)dx =
 

A
p(x y)dy + r(x)δx(A)

π(x)dx
=

A


p(x y)π(x)dx

dy +

A
r(x)π(x)dx
=

A


p(y x)π(y)dx

dy +

A
r(x)π(x)dx
=

A
(1 −r(y))π(y)dy +

A
r(x)π(x)dx
=

A
π(y)dy
which proves that π(x) is the invariant distribution for the transition prob-
ability P(x y).
However, in practice, the reversibility condition is hardly ever satisfied,
and therefore we need to construct an MH density that would indeed be
reversible. Taking any proposal density q(x y), we would simply write
pMH(x y) = q(x y)min

1 π(y)/q(x y)
π(x)/q(y x)
	

150
INSIDE VOLATILITY ARBITRAGE
Then pMH(x y) would be reversible and hence admit π(x) as its invariant
distribution.
Proof:
To see why, let us consider the case where π(y)/q(xy)
π(x)/q(yx) > 1, which
means its inverse is smaller than 1. We would then have
pMH(x y)π(x) = q(x y)π(x) = q(y x)π(x)/q(y x)
π(y)/q(x y)π(y) = pMH(y x)π(y)
(QED)
One more point we need to explain is the “blocking” technique. Hav-
ing two random variables X1, X2, the product of the conditional transition
densities, admits the joint distribution π(X1 X2) for invariant distribution.
This is why we can alternate between parameters and hidden states.
Thus
 
P1(x1 dy1|x2)P2(x2 dy2|y1)π(x1 x2)dx1dx2
=

P2(x2 dy2|y1)


P1(x1 dy1|x2)π1|2(x1|x2)dx1

π2(x2)dx2
=

P2(x2 dy2|y1)π1|2(dy1|x2)π2(x2)dx2
=

P2(x2 dy2|y1)π2|1(x2|y1)π1(dy1)dx2
= π1(dy1)

P2(x2 dy2|y1)π2|1(x2|y1)dx2
= π1(dy1)π2|1(dy2|y1) = π(dy1 dy2)
which proves that π(x1 x2) is the invariant distribution for this product tran-
sition probability.
Illustration
We use the same example as for the Gibbs sampler, only this time
we simulate from the priors and use the likelihood ratio to accept or reject
the simulations. We choose the priors
µ ∼N(7.0 3.0)
and
σ ∼
1
√G(1/9.0 1.0)
We obtain after M = 10 000 simulations
ˆµ = 9.989504

The Inference Problem
151
6
7
8
9
10
11
12
13
0
1000 2000 3000 4000 5000 6000 7000 8000 9000 10000
Simulation
MH Sampler for the Normal Mean
mu
FIGURE 2.48
Metropolis-Hastings Algorithm for µ in N(µσ). The true value is
µ∗= 10.0.
and
ˆσ = 4.797105
Naturally, the evaluation of the Markov Chain is different from that of the
Gibbs sampler. This can be seen in Figures 2.48 and 2.49.
A Few Distributions
Here are a few distributions commonly used in MCMC
algorithms.
The student cumulative distribution function
F(x ν) = 1 −I

ν
ν + x2 ν
2 1
2
	
with I(x a b) the incomplete beta function (IBF)
I(x a b) = B(x a b)
B(1 a b)
where
B(x a b) =
 x
0
ta−1(1 −t)b−1dt
with a b two strictly positive parameters. A few plots of the IBF are provided
in Figure 2.50.

152
INSIDE VOLATILITY ARBITRAGE
3
4
5
6
7
8
9
0
1000 2000 3000 4000 5000
6000 7000 8000 9000 10000
Simulation
MH Sampler for the Normal Standard Deviation
Sigma
FIGURE 2.49
Metropolis-Hastings Algorithm for σ in N(µσ). The true value is
σ∗= 5.0.
0
0.2
0.4
0.6
0.8
1
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
I(x,a,b)
x
Incomplete Beta Function
(0.5, 5.0)
(0.5, 0.5)
(5.0, 0.5)
FIGURE 2.50
Plots of the Incomplete Beta Function. Implementation is based on
code from Numerical Recipes in C.
The inverse-gamma (IG) cumulative distribution function IG(a x) could
be defined from that of the previously defined gamma distribution P(a x)
P (a x) =
1
(a)
 x
0
e−tta−1dt

The Inference Problem
153
By definition, if the random variable X is gamma-distributed, Y = 1/X
will be IG-distributed and therefore
IG(a x) = P (Y ≤x) = P

X ≥1
x
	
= 1 −P

a 1
x
	
As for the densities, they are related by
fIG(a x) = 1
x2fG

a 1
x
	
Regression Analysis
We have the following useful results as described in [34]
and [163] using some of the previous distributions. Considering a univariate
regression
Y = βX + ϵ
where
ϵ ∼N

0 σ2
We suppose we know the priors
p(β) = N(a A)
where a corresponds to the mean and A to the variance.
p

σ2
= IG(b B)
with the density
fIG(x b B) =
Bbe−B
x
(b)xb+1
Then we have for the β posterior:
p

β|Y X σ2
∝p

Y|X β σ2
p(β) ∝N(a∗ A∗)
with
a∗=
 1
A + 1
2XtX
	−1  a
A + XtY
σ2
	
A∗=
 1
A + XtX
σ2
	−1
As for the σ2 posterior we have
p(σ2|Y X β) ∝p(Y|X β σ2)p(σ2) ∝IG(b∗ B∗)
with
b∗= T + b
and
B∗= (Y −βX)t(Y −βX) + B

154
INSIDE VOLATILITY ARBITRAGE
Application to Gaussian SV Models (Heston)
Various MCMC approaches have
been suggested for the SV problem. Jacquier, Polson, and Rossi [156] were
first to a apply a hybrid of the Gibbs sampler and the MH algorithm to a log-
SV model. Kim, Shephard, and Chib [169] used a slightly different approach
for the same model.
Here, we describe the method employed by Forbes, Martin, and Wright
(FMW) [103]. Using their notations
dvt = κ(θ −vt)dt + σv
√vtdZt
Obviously our (ω θ ξ ρ) could easily be obtained as (κθ κ σv ρ). The
algorithm becomes as follows.
Initialize v(0) = (v(0)
k )1≤k≤N and choose constant and therefore non
informative priors for the parameter set35
 = (κ θ σv ρ)
1. We simulate the state vt from the Heston prior; we have for any time
step k between 1 and N and simulation i
v(i)
k = v(i)
k−1 + κ(θ −v(i)
k−1)t + σv

v(i)
k−1tZk−1
As previously mentioned, the MH ratio is therefore the likelihood ratio:
α = min

1.0 p(ln S|v(i) )
p(ln S|v(i−1) )
	
where
p(ln S|v ) ∝
N

k=1
1

(1 −ρ2)tvk−1
exp

−
1
2(1 −ρ2)vk−1t(ln Sk −µk)2

with
µk = ln Sk−1 +

µS −1
2vk−1
	
t + ρ
σv
(vk −[θκt + (1 −κt)vk−1])
Any negative variance would be rejected in the MH step.
2. The Heston equation
vk = vk−1 + κ(θ −vk−1)t + σv

vk−1tZk−1
35As before, we assume for simplicity that µS is known. Adding it to the parameter
set would be easy.

The Inference Problem
155
could be rewritten
vk −(1 −κt)vt−1
√vt−1t
= θ
κt
√vt−1t + σvZk−1
which is a linear regression
yk = θxk + ek
with
yk = vk −(1 −κt)vt−1
√vt−1t
xk =
κt
√vt−1t
and
ek ∼N(0 σv)
Hence, taking constant priors, we have
θ|κ σv v ∼N(¯θ σθ)
with
¯θ =
 N
k=1 xkyk
 N
k=1 x2
k
and
σθ = σv/




N

k=1
x2
k
What is more
σ2
v|κ v ∼IG(N −1 s2
v)
with
s2
v =
N

k=1
(yk −¯θxk)2
It is also possible to show that
p(κ|v) ∝St( ¯κ σκ)
 N

k=1
x2
k
−1
2
where St(m s) corresponds to Student’s law of mean m and standard
deviation s. The expressions for these mean and standard deviations
could be found in [103].

156
INSIDE VOLATILITY ARBITRAGE
We can therefore simulate from the priors, except we have an adjustment
factor
 N
k=1 x2
k
−1
2 to multiply the prior by. The MH ratio will therefore
be
α = min

1.0
p(ln S|v κ(i) θ(i) σ(i)
v  ρ)
 N
k=1

x(i)
k
2−1
2
p(ln S|v κ(i−1) θ(i−1) σ(i−1)
v
 ρ)
 N
k=1

x(i−1)
k
2−1
2


3. As for the correlation paramater ρ, we choose a normal proposal distri-
bution and use a constant prior again. Therefore
α = min

1.0 p

ln S|v κ θ σv ρ(i)
/q

ρ(i)|v κ θ σv S

p

ln S|v κ θ σv ρ(i−1)
/q

ρ(i)|v κ θ σv S


with q() the normal distribution with mean
 N
k=1 xkyk
 N
k=1 x2
k
and variance
t
 N
k=1 x2
k
with
xk = vk −κθt −(1 −κt)vk−1
σv√vk−1
yk = ln Sk −ln Sk−1 −

µS −1
2vk−1

t
vk−1
Note that for any of the foregoing parameters if we simulate one that
does not satisfy the usual constraints θ ≥0, κ ≥0, σv ≥0, σv ≤2κθ, and
−1 ≤ρ ≤1, then we simply do not accept them during the MH accept/reject
step. Also note that we update (κ θ σv) in a “block” instead of updating
them one by one. This technique is used by many since it makes the algorithm
faster.
For the actual results, the reader could refer to Forbes et al. [103]. The
authors test their Bayesian estimator against simulated data, and observe
inefficiency. This is in agreement with our observations when applying MLE
techniques to simulated data.

The Inference Problem
157
Using the Characteristic Function
In a recent article [31], the use of the characteristic function has been sug-
gested for the purpose of filtering. In this approach, however, we have to limit
ourselves to the case where F(U V  xt) = E[exp(Uzt+1 + V xt+1)|xt] has a
known form. One natural form would be the affine process, where
F(U V  xt) = E[exp(Uzt+1 + V xt+1)|xt] = exp{C(U V ) + D(U V )xt}
After choosing the initial conditions, the time update equation
p(zt+1 xt+1|t) =

p(zt+1 xt+1|xt)p(xt|t)dxt
becomes in terms of the characteristic function
Fzx|t(U V ) = Et[E (exp(Uzt+1 + V xt+1)|xt)]
= E[exp{C(U V ) + D(U V )xt}|z1:t]
= exp[C(U V )]Gt|t[D(U V )]
where Gt|s(U) = E[exp(Uxt)|z1:s] is the moment-generating function of xt
conditional on the observations up to time s.
The Measurement Update equation
p(xt+1|t + 1) = p(zt+1 xt+1|t)
p(zt+1|t)
becomes in terms of the characteristic function
Gt+1|t+1(V ) =
! +∞
−∞Fzx|t(iU V ) exp (−iUzt+1)dU
! +∞
−∞Fzx|t(iU 0) exp (−iUzt+1)dU
This remarkably gives us a one-step induction expression
Gt+1|t+1(V ) =
! +∞
−∞exp[C(iU V ) −iUzt+1]Gt|t[D(iU V )]dU
! +∞
−∞exp[C(iU 0) −iUzt+1]Gt|t[D(iU 0)]dU
which allows us to determine the a posteriori estimate and errors
ˆxt = G
′
t|t(0)
and
Pt = V art(xt) = G
′′
t|t(0) −

G
′
t|t(0)
2
at each iteration.

158
INSIDE VOLATILITY ARBITRAGE
In this framework, the likelihood function could be written as
L1:T =
T −1

t=0
lt
with
lt = 1
2π
 +∞
−∞
exp[C(iU 0) −iUzt+1]Gt|t[D(iU 0)]dU
which is equivalent to
lt = 1
π
 +∞
0
R
"
exp[C(iU 0) −iUzt+1]Gt|t[D(iU 0)]
#
dU
(2.30)
where R{} corresponds to the real part of a complex number. In order to be
able to calculate the integral, we need to know the value of Gt|t(x) at each
point. For this, Bates [31] suggests making an assumption on the distribution
of the hidden state. For a gamma distribution, we have a moment-generating
function of the form
Gt|t(x) = (1 −κx)−vt
The integral (2.30) can be evaluated numerically; however, when dealing with
“outliers” the density of the observation takes near-zero values, which makes
the integration difficult. Bates suggests scaling transformations equivalent to
the importance sampling technique used in particle filtering.
Independently from this, Dragulescu and Yakovenko, [81] and [219],
derived a semianalytic expression for the likelihood under the Heston model,
by using Fourier inversion. Note that a particle filter calculates this very
integral via Monte Carlo simulations.
It is worth noting that the main advantage of our particle filtering
approach is its complete generality. Indeed the Bates method would work
only for model classes that have an exponentially affine Fourier transform.
It is true that the Heston model falls in this category; however, a VGG (vari-
ance gamma with gamma-distributed arrival rate) process would not, and
therefore could only be analyzed through a simulation-based methodology.
Introducing Jumps
The Model
As in Bates [28], let us introduce a jump process (independent
from Brownian motion) with a given intensity λ and a fixed36 fractional jump
36We could make j a Gaussian random variable without changing the methodology.

The Inference Problem
159
size 0 ≤j < 1 . The number of jumps between t and t + dt will therefore be
dNt . Needless to say, if either the intensity λ = 0 or the jump size j = 0,
then we are back to the pure diffusion case.
The new stochastic differential equation for the stock price in the risk-
neutral framework will be
dSt = (µS + λj)Stdt + √vtStdBt −StjdNt
and applying Ito’s lemma for semi-Martingales
d ln St =

µS −1
2vt + λj
	
dt + √vtdBt + ln(1 −j)dNt
which we can rewrite in the discrete version as
ln Sk+1 = ln Sk +

µS −1
2vk + λj
	
t + √vt
√
tBk + µk
with µ0 = 0 and
µk = δ0(0)e−λt + δ0 (ln(1 −j)) (1 −e−λt)
where δ0() corresponds to the Dirac delta function.37
Also
vk = vk−1 + (ω −θvk−1)t + ξ√vk−1
√
tZk−1
−ρξ

ln Sk−1 +

µS + λj −1
2vk−1
	
t + √vk−1
√
tBk−1 + µk−1 −ln Sk

which completes our set of equations.
It is important to note that the new parameter set is
 = (ω θ ξ ρ λ j)
which effectively gives us two additional degrees of freedom.38
37This means that −∞< µk ≤0 for every k. Note that we are assuming that we
can have at most one jump within [t t + t], which means that t is small enough.
This is completely different from pure-jump models, such as variance gamma.
38A related idea was developed by Hamilton [126] as well as Chourdakis [59]
and Deng [72]. Chourdakis uses the characteristic function for the jump-diffusion
process. Doucet [80] suggests the use of particle filtering for the jump process.
Maheu and McCurdy [184] use a fully integrated GARCH likelihood with Poisson
jumps. Aït-Sahalia [3] uses moments to separate the diffusion parameters from the
jumps. Johannes, Polson, and Stroud [164] use the particle filtering technique as
well, however, in a Bayesian MCMC framework. Finally, Honoré [142] shows that
an MLE approach always works for a constant jump size.

160
INSIDE VOLATILITY ARBITRAGE
The Generic Particle Filter
Since µk is following a Poisson process, we have to
use a non-Gaussian filter. The use of a generic particle filter (GPF) is therefore
natural. In a generic particle filter, the proposal distribution q(xk) is simply
set equal to p(xk|xk−1). The state xk could be chosen as
xk =
 µk
vk
	
and the transition equation becomes
xk =


δ0(0)e−λt +δ0 (ln(1 −j)) (1 −e−λt)
vk−1 + [(ω −ρξ(µS +λj) −(θ −1
2ρξ)vk−1]t +ρξ[ln( Sk
Sk−1 ) −µk−1] +ξ

1 −ρ2√vk−1
√
t ˜Zk−1


It becomes therefore possible to implement a particle filter as follows.
1. Choose v0 and P0 > 0 and set µ0 = 0, so for i in 1 ... Nsims
x(i)
0
=

0
v0 + √P0Z(i)
	
Then for each k with 1 ≤k ≤N do
2. Write the new ˜x(i)
k = (˜µ(i)
k  ˜v(i)
k )t as the result of simulations
˜v(i)
k ∼N

m = v(i)
k−1 +

ω −ρξ(µS + λj) −

θ −1
2ρξ
	
v(i)
k−1

×t + ρξ

ln
 Sk
Sk−1
	
−µ(i)
k−1

 s
	
with s = ξ

1 −ρ2

v(i)
k−1
√
t and
˜µ(i)
k = 0
if U[0 1] ≤e−λt and
˜µ(i)
k = ln(1 −j)
otherwise.
3. Define the weights
w(i)
k = w(i)
k−1p(zk|˜x(i)
k )
with
p(zk|˜x(i)
k ) = n

zk zk−1 +

µS + λj −1
2 ˜v(i)
k
	
t + ˜µ(i)
k 

˜v(i)
k t
	

The Inference Problem
161
4. Normalize the weights
˜w(i)
k =
w(i)
k
 Nsims
i=1
w(i)
k
5. Resample the points ˜x(i)
k
and get x(i)
k
and reset w(i)
k = ˜w(i)
k = 1/Nsims .
This completes the generic particle filtering algorithm.
Note that there is no Kalman filtering here and therefore
ˆz−
k =
1
Nsims
Nsims

i=1
ˆz(i)
k
with ˆz(i)
k the estimation of zk from x(i)
k−1
ˆz(i)
k = zk−1 +

µS + λj −1
2v(i)
k−1
	
t + µ(i)
k−1
and the estimation error is zk −ˆz−
k as before.
The likelihood maximization is not different from the EPF or UPF. We
need to maximize
N

k=1
ln
Nsims

i=1
w(i)
k

where w(i)
k ’s are defined at Step 3.
Extended/Unscented Particle Filters
Using the same model, we can take advan-
tage of the independence of vk and µk and apply the (nonlinear) Gaussian
Kalman filter to the former. In this case, the Steps 2 and 3 should be replaced
with:
2-a. Write ˆx(i)
k =

ˆµ(i)
k  ˆv(i)
k
t
with
ˆv(i)
k = KF(v(i)
k−1)
with P (i)
k
the associated a posteriori error covariance matrix, KF the
extended or unscented Kalman filter, and
ˆµ(i)
k = µ(i)
k−1
2-b. Now take the simulations
˜v(i)
k ∼N

ˆv(i)
k  P (i)
k


162
INSIDE VOLATILITY ARBITRAGE
and
˜µ(i)
k = 0
if U[0 1] ≤e−λt and
˜µ(i)
k = ln(1 −j)
otherwise.
3. Define the weights
w(i)
k = w(i)
k−1
p

zk|˜x(i)
k

p

˜x(i)
k |x(i)
k−1

q

˜x(i)
k |x(i)
k−1 z1:k

with
p

zk|˜x(i)
k

= n

zk zk−1 +

µS + λj −1
2 ˜v(i)
k
	
t + ˜µ(i)
k 

˜v(i)
k t
	
p

˜x(i)
k |x(i)
k−1

= n

˜v(i)
k  m s = ξ

1 −ρ2

v(i)
k−1
√
t
	
p

˜µ(i)
k |µ(i)
k−1

with
m = v(i)
k−1+

ω −ρξ(µS + λj) −

θ −1
2ρξ
	
v(i)
k−1

t+ρξ ln
 Sk
Sk−1
	
−ρξµ(i)
k−1
and
q

˜x(i)
k |x(i)
k−1 z1:k

= n

˜v(i)
k  ˆv(i)
k  P (i)
k

p

˜µ(i)
k |µ(i)
k−1

Note that as for the GPF, the terms p

˜µ(i)
k |µ(i)
k−1

cancel out and need not be
evaluated.
The rest of the algorithm remains the same. This way we will not lose
the information contained in the Kalman gain for the Gaussian dimension.
The following is the C++ code for the application of EPF to the Bates
model.
// log_stock_prices
are the log of stock prices
// muS is the real-world stock drift
// n_stock_prices is the number of the above stock prices
// (omega, theta, xi, rho, lambda, j) are the Bates
parameters
// ll is the value of (negative log) Likelihood function
// estimates[] are the estimated observations from the
filter

The Inference Problem
163
// The function ran2() is from Numerical Recipes in C
// and generates uniform random variables
// The function Normal_inverse() can be found from
many sources
// and is the inverse of the Normal CDF
// Normal_inverse(ran2(.)) generates a set of Normal
random variables
void estimate_particle_jump_diffusion_parameters_1_dim(
double *log_stock_prices,
double muS, int n_stock_prices,
double omega,
double theta,
double xi,
double rho,
double lambda,
double j,
double *ll,
double *estimates)
{
int
i1, i2, i3;
double
H, A, x0, P0, z;
int
M=1000;
double
x[1000], xx[1000], x1[1000], x2[1000];
double
mu[1000], mm[1000], m1[1000], m2[1000];
double
P[1000], P1[1000], U[1000], K[1000], W[1000];
double
w[1000],
u[1000], c[1000];
double
q, pz, px, s, m, l;
double
delt=1.0/252.0, x1_sum, m1_sum;
long
idum=-1;
int
i1_prev=0;
double
u_t=0.0;
int
*jump;
jump= new int [n_stock_prices];
for (i1=0; i1<n_stock_prices; i1++)
jump[i1]=0;
A = 1.0-(theta-0.5*rho*xi)*delt;
H = -0.5*delt;
x0 = 0.04;
P0 = 0.000001;
for (i2=0; i2<M; i2++)
{

164
INSIDE VOLATILITY ARBITRAGE
x[i2] = x0 + sqrt(P0)* Normal_inverse(ran2(&idum));
mu[i2]=0;
P[i2] = P0;
}
*ll=0.0;
for (i1=1;i1<n_stock_prices-1;i1++)
{
l = 0.0;
x1_sum=0.0;
m1_sum=0.0;
for (i2=0; i2<M; i2++)
{
/* EKF for the proposal distribution */
if (x[i2]<0) x[i2]=0.00001;
x1[i2] = x[i2] + ( omega-rho*xi*(muS+lambda*j) -
(theta-0.5*rho*xi) * x[i2]) * delt +
rho*xi* (log_stock_prices[i1]-
log_stock_prices[i1-1]) - rho*xi*mu[i2];
m1[i2]=mu[i2];
W[i2]
= xi*sqrt((1-rho*rho) * x[i2] * delt);
P1[i2] = W[i2]*W[i2] + A*P[i2]*A;
if (x1[i2]<0) x1[i2]=0.00001;
U[i2] = sqrt(x1[i2]*delt);
K[i2] = P1[i2]*H/( H*P1[i2]*H + U[i2]*U[i2]);
z = log_stock_prices[i1+1];
x2[i2] = x1[i2] + K[i2] *
(z - (log_stock_prices[i1] +
(muS+lambda*j-0.5*x1[i2])*delt + m1[i2]));
m2[i2]= m1[i2];
x1_sum+= x1[i2];
m1_sum+= m1[i2];
P[i2]=(1.0-K[i2]*H)*P1[i2];
/* sample */
xx[i2] = x2[i2] + sqrt(P[i2])*
Normal_inverse(ran2(&idum));
if (xx[i2]<0) xx[i2]=0.00001;
if (ran2(&idum) < exp(-lambda*delt))
mm[i2]=0.0;
else
mm[i2]=log(1.0-j);
/* calculate weights */
m = x2[i2];

The Inference Problem
165
s = sqrt(P[i2]);
q = 0.39894228/s * exp( - 0.5* (xx[i2] - m)*
(xx[i2] - m)/(s*s) );
m= log_stock_prices[i1] +
(muS+lambda*j-0.5*xx[i2])*delt + mm[i2];
s= sqrt(xx[i2]*delt);
pz= 0.39894228/s *
exp( - 0.5* (z - m)*(z - m)/(s*s) );
m= x[i2] + ( omega-rho*xi*(muS+lambda*j) -
(theta-0.5*rho*xi) * x[i2]) * delt +
rho*xi* (log_stock_prices[i1]-
log_stock_prices[i1-1]) -rho*xi*mu[i2];
s= xi*sqrt((1-rho*rho) * x[i2] * delt);
px= 0.39894228/s *
exp( - 0.5* (xx[i2] - m)*(xx[i2] - m)/(s*s) );
w[i2]= pz * px / MAX(q, 1.0e-10);
l += w[i2];
}
*ll += log(l);
estimates[i1+1]= log_stock_prices[i1] +
(muS+lambda*j-0.5*x1_sum/M)*delt+m1_sum/M;
/* normalize weights */
for (i2=0; i2<M; i2++)
w[i2] /= l;
/* resample and reset weights */
c[0]=0;
for (i2=1; i2<M; i2++)
c[i2] = c[i2-1] + w[i2];
i2=0;
u[0] = 1.0/M * ran2(&idum);
for (i3=0; i3<M; i3++)
{
u[i3] = u[0] + 1.0/M *i3;
while (u[i3] > c[i2])
i2++;
x[i3]= xx[i2];
mu[i3]=mm[i2];
w[i3]=1.0/M;
}
}
*ll *= -1.0;
delete [] jump;

166
INSIDE VOLATILITY ARBITRAGE
}
// *ll corresponds to the (negative log) Likelihood
// which we will need to minimize to obtain optimal
parameters
The Srivastava Approach
Srivastava [222] suggests the following approach for
simulating the jump component. Instead of allowing a jump at each time
interval [tk tk + t] with a probability 1 −e−λt as we do now, we can flag
the time steps such that
tk−1 < 1
λ ln

1
U[0 1]
	
≤tk
where U[0 1] is a uniform random variable between zero and one, and then
perform a jump of size | ln(1 −j)| on these steps for all paths. We therefore
would first initialize tp = 0 and loop through k’s between 1 and N, and if
e−λ(tk−tp) ≤U[0 1] < e−λ(tk−1−tp)
we flag this k and set tp = tk and resimulate U[0 1] . In the particle filter, we
would set for all indices i’s
˜µ(i)
k = ln(1 −j)
for the flagged k’s, and we would set ˜µ(i)
k = 0 for other indices.
It is important to note that in this approach the simulation for the jump
component is completely “orthogonal” to the diffusion SIS part. Indeed the
index i in the foregoing is irrelevant for the entity ˜µ(i)
k . This means that in
the KF step, the weight calculation and the resampling are independent of
the Jump component altogether.
Numeric results
As a check, we simulate a time series with the parameter set
∗= (ω∗= 0 θ∗= 0 ξ∗= 0 ρ∗= 0 λ∗= 2.52 j ∗= 0.20)
which corresponds to a jump frequency of λt = 0.01 and a jump size of
20 percent. We generated N = 245 points and used M = 1000 particles.
The estimated set via the above EPF is
ˆ = ( ˆω = 0.23 ˆθ = 1.5 ˆξ = 0.34 ˆρ = 0.21 ˆλ = 2.65 ˆj = 0.20)
As we see, the diffusion parameters are not close to the original ones, but this
is probably due to the small t, as previously discussed. The jump parameters
are close to the original ones, which means that the filter is valid for the jump

The Inference Problem
167
0
0.0001
0.0002
0.0003
0.0004
0.0005
0.0006
0
50
100
150
200
250
Errors
Days
Extended Particle Filter for Heston and Heston+Jumps Models
EPF Heston
EPF Heston+Jumps
FIGURE 2.51
Comparison of EPF Results for Heston and Heston+Jumps Models.
The presence of jumps can be seen in the residuals.
6.4
6.5
6.6
6.7
6.8
6.9
7
7.1
0
100
200
300
400
500
Log Stock Price
Days
Simulated versus Estimated Time Series
Original Time Series
Estimated Time Series via EPF
FIGURE 2.52
Comparison of EPF Results for Simulated and Estimated Jump-
Diffusion Time Series. The filtered data matches the real data fairly well.
component. Note that despite the difference in the diffusion parameters, the
estimated and original time series are rather close for a new simulation, as
can be seen in Figures 2.51 and 2.52. This reconfirms our previous remark:
When the parameters affect the drift of the observation (as opposed to its
noise), their estimation is far more accurate and requires fewer data points.

168
INSIDE VOLATILITY ARBITRAGE
The Optimization Algorithm
It is important to realize that the likelihood function
here (owing to the jumps) is not differentiable everywhere, and, therefore,
gradient-based maximization methods could not be applied. The optimiza-
tion could, however, still be carried out via the direction set algorithm as
previously described. Note that as mentioned in [164] so far there has been
no formal proof on the convergence of the discretized jump diffusion equa-
tions toward the continuous ones; however, empirical evidence makes the
convergence assumption plausible.
Pure Jump Models
The variance gamma with stochastic arrival (VGSA) and the variance gamma
with gamma arrival (VGG) models were defined in Chapter 1. These models
are non-Gaussian, and we could apply the particle filtering technique to
them. We are not dealing with diffusion models, and therefore we do not
have the Girsanov theorem. We are estimating the parameter set
 = (µS θ σ ν ...)
In order to make the back-testing simpler, we suppose that we know the
stock drift and try to estimate the other parameters. However, as mentioned
earlier, for a high-frequency data set we have
t = o
√
t

and the drift term has a negligible impact.
VG
The variance gamma model has the advantage of offering an integrated
density, which allows us to calculate the exact likelihood. Calling z =
ln(Sk/Sk−1) and h = tk −tk−1 and posing xh = z−µSh−h
ν ln(1−θν−σ2ν/2),
we have
p(z|h) = 2 exp

θxh/σ2
ν
hν √
2πσ
 h
ν


x2
h
2σ2/ν + θ2
	 h
2ν −1
4
K hν −1
2
 1
σ2

x2
h

2σ2/ν + θ2	
and the likelihood is
L1:N =
N

k=1
p(zk|zk−1 h)
The implementation of this estimation procedure is straightforward and has
already been done in [182].

The Inference Problem
169
One could also back-test the estimation procedure in the following way:
First choose a parameter set (θ σ ν) as well as a drift µS and a time-step
t. Then simulate via Monte Carlo a gamma-distributed random variable
as well as a Gaussian one. Deduce an artificial stock-price time series, apply
the MLE procedure to it, and try to recover the original parameter set.
Using t = 1/252, µ∗
S = 0.05, and
θ∗
=
0.02
σ∗
=
0.2
ν∗
=
0.005
We simulated 500 data points, applied the MLE, and found an optimal par-
ameter set ˆ = (0.018 0.22 0.006), which is close to the original set.
VGSA
Using the same notations as in the previous chapter, the Euler dis-
cretized VGSA process could be written via the auxiliary variable
yk = yk−1 + κ(η −yk−1)t + λ√yk−1
√
tWk−1
and the state
xk = F −1
ν (ykt U[0 1])
as well as the observation zk = ln Sk+1
zk = zk−1 + (µS + ω)t + θxk + σ√xkBk
with ω = 1ν ln(1 −θν −σ2ν/2).
The Filtering Algorithm
The PF algorithm could therefore be written as follows.
1. Initialize the arrival-rate y(j)
0 , the state x(i)
0 , and the weight w(i)
0
for j
between 1 and Msims, and i between 1 and Nsims
While 1 ≤k ≤N
2. Simulate the arrival-rate yk for j between 1 and Msims
y(j)
k
= y(j)
k−1 + κ

η −y(j)
k−1

t + λ

y(j)
k−1
√
tN −1 
U(j) [0 1]

3-a. Simulate the state xk for each y(j)
k
and for i between 1 and Nsims
˜x(i|j)
k
= F −1
ν

y(j)
k t U(i)[0 1]


170
INSIDE VOLATILITY ARBITRAGE
3-b. Compute the unconditional state
˜x(i)
k =

˜x(i)
k (yk)p(yk|yk−1)dyk ≈
1
Msims
Msims

j=1
˜x(i|j)
k
4. Calculate the associated weights for each i
w(i)
k = w(i)
k−1p

zk|˜x(i)
k

with
p

zk|˜x(i)
k

= n(zk m s)
the normal density with mean m = zk−1+(µS +ω)t+θ˜x(i)
k and standard
deviation s = σ

˜x(i)
k
5. Normalize the weights
˜w(i)
k =
w(i)
k
 Nsims
i=1
w(i)
k
6. Resample the points ˜x(i)
k and get x(i)
k and reset w(i)
k = ˜w(i)
k = 1/Nsims.
7. Increment k, go back to Step 2, and Stop at the end of the While loop.
Parameter Estimation
As usual, the log likelihood to be maximized is
ln(L1:N) =
N

k=1
ln
Nsims

i=1
w(i)
k

The maximization takes place over the parameter set  = (κ η λ ν θ σ).
Again, in reality the stock drift µS should be estimated together with the
other parameters; however, with a view to simplifying, we suppose we know
µS in our back-testing procedures.
A More Efficient Algorithm
We could take advantage of the fact that VG pro-
vides an integrated density of stock return. Calling z = ln(Sk/Sk−1) and
h = tk −tk−1, and posing xh = z −µSh −hν ln(1 −θν −σ2ν/2), we have
p(z|h) = 2 exp

θxh/σ2
ν
hν √
2πσ( h
ν)

x2
h
2σ2/ν + θ2
	 h
2ν −1
4
K hν −1
2
 1
σ2

x2
h

2σ2/ν + θ2	
As we can see, the dependence on the gamma distribution is “integrated out”
in the above.

