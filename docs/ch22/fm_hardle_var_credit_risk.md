# Value at Risk & Credit Risk Models

!!! info "Source"
    **Applied Quantitative Finance** edited by Wolfgang Härdle, Torsten Kleinow, and Gerhard Stahl, Springer, 2002.
    These notes are used for educational purposes.

## Value at Risk Methods

Part I
Value at Risk


1 Approximating Value at Risk in
Conditional Gaussian Models
Stefan R. Jaschke and Yuze Jiang
1.1
Introduction
1.1.1
The Practical Need
Financial institutions are facing the important task of estimating and control-
ling their exposure to market risk, which is caused by changes in prices of
equities, commodities, exchange rates and interest rates. A new chapter of risk
management was opened when the Basel Committee on Banking Supervision
proposed that banks may use internal models for estimating their market risk
(Basel Committee on Banking Supervision, 1995). Its implementation into na-
tional laws around 1998 allowed banks to not only compete in the innovation
of financial products but also in the innovation of risk management methodol-
ogy. Measurement of market risk has focused on a metric called Value at Risk
(VaR). VaR quantifies the maximal amount that may be lost in a portfolio over
a given period of time, at a certain confidence level. Statistically speaking, the
VaR of a portfolio is the quantile of the distribution of that portfolio’s loss over
a specified time interval, at a given probability level.
The implementation of a firm-wide risk management system is a tremendous
job. The biggest challenge for many institutions is to implement interfaces to
all the different front-office systems, back-office systems and databases (poten-
tially running on different operating systems and being distributed all over the
world), in order to get the portfolio positions and historical market data into a
centralized risk management framework. This is a software engineering prob-
lem. The second challenge is to use the computed VaR numbers to actually

4
1
Approximating Value at Risk in Conditional Gaussian Models
control risk and to build an atmosphere where the risk management system
is accepted by all participants. This is an organizational and social problem.
The methodological question how risk should be modeled and approximated
is – in terms of the cost of implementation – a smaller one. In terms of im-
portance, however, it is a crucial question. A non-adequate VaR-methodology
can jeopardize all the other efforts to build a risk management system. See
(Jorion, 2000) for more on the general aspects of risk management in financial
institutions.
1.1.2
Statistical Modeling for VaR
VaR methodologies can be classified in terms of statistical modeling decisions
and approximation decisions. Once the statistical model and the estimation
procedure is specified, it is a purely numerical problem to compute or approx-
imate the Value at Risk. The modeling decisions are:
1. Which risk factors to include. This mainly depends on a banks’ business
(portfolio). But it may also depend on the availability of historical data.
If data for a certain contract is not available or the quality is not sufficient,
a related risk factor with better historical data may be used. For smaller
stock portfolios it is customary to include each stock itself as a risk factor.
For larger stock portfolios, only country or sector indexes are taken as
the risk factors (Longerstaey, 1996). Bonds and interest rate derivatives
are commonly assumed to depend on a fixed set of interest rates at key
maturities. The value of options is usually assumed to depend on implied
volatility (at certain key strikes and maturities) as well as on everything
the underlying depends on.
2. How to model security prices as functions of risk factors, which is usually
called “the mapping”. If Xi
t denotes the log return of stock i over the
time interval [t −1, t], i.e., Xi
t = log(Si
t) −log(Si
t−1), then the change in
the value of a portfolio containing one stock i is
∆Si
t = Si
t−1(eXi
t −1),
where Si
t denotes the price of stock i at time t. Bonds are first decomposed
into a portfolio of zero bonds. Zero bonds are assumed to depend on
the two key interest rates with the closest maturities. How to do the
interpolation is actually not as trivial as it may seem, as demonstrated

1.1
Introduction
5
by Mina and Ulmer (1999). Similar issues arise in the interpolation of
implied volatilities.
3. What stochastic properties to assume for the dynamics of the risk factors
Xt. The basic benchmark model for stocks is to assume that logarith-
mic stock returns are joint normal (cross-sectionally) and independent in
time. Similar assumptions for other risk factors are that changes in the
logarithm of zero-bond yields, changes in log exchange rates, and changes
in the logarithm of implied volatilities are all independent in time and
joint normally distributed.
4. How to estimate the model parameters from the historical data. The usual
statistical approach is to define the model and then look for estimators
that have certain optimality criteria. In the basic benchmark model the
minimal-variance unbiased estimator of the covariance matrix Σ of risk
factors Xt is the “rectangular moving average”
ˆΣ =
1
T −1
T
X
t=1
(Xt −µ)(Xt −µ)⊤
(with µ
def
= E[Xt]). An alternative route is to first specify an estimator
and then look for a model in which that estimator has certain optimality
properties. The exponential moving average
ˆΣT = (eλ −1)
T −1
X
t=−∞
e−λ(T −t)(Xt −µ)(Xt −µ)⊤
can be interpreted as an efficient estimator of the conditional covariance
matrix ΣT of the vector of risk factors XT , given the information up to
time T −1 in a very specific GARCH model.
While there is a plethora of analyses of alternative statistical models for market
risks (see Barry Schachter’s Gloriamundi web site), mainly two classes of models
for market risk have been used in practice:
1. iid-models, i.e., the risk factors Xt are assumed to be independent in time,
but the distribution of Xt is not necessarily Gaussian. Apart from some
less common models involving hyperbolic distributions (Breckling, Eber-
lein and Kokic, 2000), most approaches either estimate the distribution

6
1
Approximating Value at Risk in Conditional Gaussian Models
of Xt completely non-parametrically and run under the name “histori-
cal simulation”, or they estimate the tail using generalized Pareto dis-
tributions (Embrechts, Kl¨uppelberg and Mikosch, 1997, “extreme value
theory”).
2. conditional Gaussian models, i.e., the risk factors Xt are assumed to be
joint normal, conditional on the information up to time t −1.
Both model classes can account for unconditional “fat tails”.
1.1.3
VaR Approximations
In this paper we consider certain approximations of VaR in the conditional
Gaussian class of models. We assume that the conditional expectation of Xt,
µt, is zero and its conditional covariance matrix Σt is estimated and given at
time t −1. The change in the portfolio value over the time interval [t −1, t] is
then
∆Vt(Xt) =
n
X
i=1
wi∆Si
t(Xt),
where the wi are the portfolio weights and ∆Si
t is the function that “maps” the
risk factor vector Xt to a change in the value of the i-th security value over the
time interval [t −1, t], given all the information at time t −1. These functions
are usually nonlinear, even for stocks (see above). In the following, we will
drop the time index and denote by ∆V the change in the portfolio’s value over
the next time interval and by X the corresponding vector of risk factors.
The only general method to compute quantiles of the distribution of ∆V is
Monte Carlo simulation.
From discussion with practitioners “full valuation
Monte Carlo” appears to be practically infeasible for portfolios with securi-
ties whose mapping functions are first, extremely costly to compute – like for
certain path-dependent options whose valuation itself relies on Monte-Carlo
simulation – and second, computed inside complex closed-source front-office
systems, which cannot be easily substituted or adapted in their accuracy/speed
trade-offs. Quadratic approximations to the portfolio’s value as a function of
the risk factors
∆V (X) ≈∆⊤X + 1
2X⊤ΓX,
(1.1)
have become the industry standard since its use in RiskMetrics (Longerstaey,
1996). (∆and Γ are the aggregated first and second derivatives of the indi-
vidual mapping functions ∆Si w.r.t. the risk factors X. The first version of

1.1
Introduction
7
RiskMetrics in 1994 considered only the first derivative of the value function,
the “delta”. Without loss of generality, we assume that the constant term in
the Taylor expansion (1.1), the “theta”, is zero.)
1.1.4
Pros and Cons of Delta-Gamma Approximations
Both assumptions of the Delta-Gamma-Normal approach – Gaussian innova-
tions and a reasonably good quadratic approximation of the value function V
– have been questioned. Simple examples of portfolios with options can be
constructed to show that quadratic approximations to the value function can
lead to very large errors in the computation of VaR (Britton-Jones and Schae-
fer, 1999). The Taylor-approximation (1.1) holds only locally and is question-
able from the outset for the purpose of modeling extreme events. Moreover,
the conditional Gaussian framework does not allow to model joint extremal
events, as described by Embrechts, McNeil and Straumann (1999). The Gaus-
sian dependence structure, the copula, assigns too small probabilities to joint
extremal events compared to some empirical observations.
Despite these valid critiques of the Delta-Gamma-Normal model, there are good
reasons for banks to implement it alongside other models. (1) The statistical
assumption of conditional Gaussian risk factors can explain a wide range of
“stylized facts” about asset returns like unconditional fat tails and autocor-
relation in realized volatility. Parsimonious multivariate conditional Gaussian
models for dimensions like 500-2000 are challenging enough to be the subject of
ongoing statistical research, Engle (2000). (2) First and second derivatives of
financial products w.r.t. underlying market variables (= deltas and gammas)
and other “sensitivities” are widely implemented in front office systems and
routinely used by traders. Derivatives w.r.t. possibly different risk factors used
by central risk management are easily computed by applying the chain rule
of differentiation. So it is tempting to stay in the framework and language of
the trading desks and express portfolio value changes in terms of deltas and
gammas. (3) For many actual portfolios the delta-gamma approximation may
serve as a good control-variate within variance-reduced Monte-Carlo methods,
if it is not a sufficiently good approximation itself. Finally (4), is it extremely
risky for a senior risk manager to ignore delta-gamma models if his friendly
consultant tells him that 99% of the competitors have it implemented.
Several methods have been proposed to compute a quantile of the distribution
defined by the model (1.1), among them Monte Carlo simulation (Pritsker,
1996), Johnson transformations (Zangari, 1996a; Longerstaey, 1996), Cornish-

8
1
Approximating Value at Risk in Conditional Gaussian Models
Fisher expansions (Zangari, 1996b; Fallon, 1996), the Solomon-Stephens ap-
proximation (Britton-Jones and Schaefer, 1999), moment-based approxima-
tions motivated by the theory of estimating functions (Li, 1999), saddle-point
approximations (Rogers and Zane, 1999), and Fourier-inversion (Rouvinez,
1997; Albanese, Jackson and Wiberg, 2000). Pichler and Selitsch (1999) com-
pare five different VaR-methods: Johnson transformations, Delta-Normal, and
Cornish-Fisher-approximations up to the second, fourth and sixth moment.
The sixth-order Cornish-Fisher-approximation compares well against the other
techniques and is the final recommendation. Mina and Ulmer (1999) also com-
pare Johnson transformations, Fourier inversion, Cornish-Fisher approxima-
tions, and partial Monte Carlo. (If the true value function ∆V (X) in Monte
Carlo simulation is used, this is called “full Monte Carlo”. If its quadratic ap-
proximation is used, this is called “partial Monte Carlo”.) Johnson transforma-
tions are concluded to be “not a robust choice”. Cornish-Fisher is “extremely
fast” compared to partial Monte Carlo and Fourier inversion, but not as robust,
as it gives “unacceptable results” in one of the four sample portfolios.
The main three methods used in practice seem to be Cornish-Fisher expansions,
Fourier inversion, and partial Monte Carlo, whose implementation in XploRe
will be presented in this paper. What makes the Normal-Delta-Gamma model
especially tractable is that the characteristic function of the probability distri-
bution, i.e. the Fourier transform of the probability density, of the quadratic
form (1.1) is known analytically. Such general properties are presented in sec-
tion 1.2. Sections 1.3, 1.4, and 1.5 discuss the Cornish-Fisher, Fourier inversion,
and partial Monte Carlo techniques, respectively.
1.2
General Properties of Delta-Gamma-Normal
Models
The change in the portfolio value, ∆V , can be expressed as a sum of indepen-
dent random variables that are quadratic functions of standard normal random
variables Yi by means of the solution of the generalized eigenvalue problem
CC⊤= Σ,
C⊤ΓC = Λ.

1.2
General Properties of Delta-Gamma-Normal Models
9
This implies
∆V =
m
X
i=1
(δiYi + 1
2λiY 2
i )
(1.2)
=
m
X
i=1
(
1
2λi
 δi
λi
+ Yi
2
−δ2
i
2λi
)
with X = CY , δ = C⊤∆and Λ = diag(λ1, . . . , λm). Packages like LAPACK
(Anderson, Bai, Bischof, Blackford, Demmel, Dongarra, Croz, Greenbaum,
Hammarling, McKenney and Sorensen, 1999) contain routines directly for the
generalized eigenvalue problem. Otherwise C and Λ can be computed in two
steps:
1. Compute some matrix B with BB⊤= Σ. If Σ is positive definite, the
fastest method is Cholesky decomposition. Otherwise an eigenvalue de-
composition can be used.
2. Solve the (standard) symmetric eigenvalue problem for the matrix B⊤ΓB:
Q⊤B⊤ΓBQ = Λ
with Q−1 = Q⊤and set C
def
= BQ.
The decomposition is implemented in the quantlet
npar= VaRDGdecomp(par)
uses a generalized eigen value decomposition to do a suitable co-
ordinate change. par is a list containing Delta, Gamma, Sigma on
input. npar is the same list, containing additionally B, delta,
and lambda on output.
The characteristic function of a non-central χ2
1 variate ((Z +a)2, with standard
normal Z) is known analytically:
Eeit(Z+a)2 = (1 −2it)−1/2 exp
 a2it
1 −2it

.
This implies the characteristic function for ∆V
Eeit∆V =
Y
j
1
√
1 −iλjt
exp{−1
2δ2
j t2/(1 −iλjt)},
(1.3)

10
1
Approximating Value at Risk in Conditional Gaussian Models
which can be re-expressed in terms of Γ and B
Eeit∆V = det(I −itB⊤ΓB)−1/2 exp{−1
2t2∆⊤B(I −itB⊤ΓB)−1B⊤∆}, (1.4)
or in terms of Γ and Σ
Eeit∆V = det(I −itΓΣ)−1/2 exp{−1
2t2∆⊤Σ(I −itΓΣ)−1∆}.
(1.5)
Numerical Fourier-inversion of (1.3) can be used to compute an approximation
to the cumulative distribution function (cdf) F of ∆V .
(The α-quantile is
computed by root-finding in F(x) = α.) The cost of the Fourier-inversion is
O(N log N), the cost of the function evaluations is O(mN), and the cost of the
eigenvalue decomposition is O(m3). The cost of the eigenvalue decomposition
dominates the other two terms for accuracies of one or two decimal digits and
the usual number of risk factors of more than a hundred. Instead of a full
spectral decomposition, one can also just reduce B⊤ΓB to tridiagonal form
B⊤ΓB = QTQ⊤. (T is tridiagonal and Q is orthogonal.) Then the evaluation
of the characteristic function in (1.4) involves the solution of a linear system
with the matrix I−itT, which costs only O(m) operations. An alternative route
is to reduce ΓΣ to Hessenberg form ΓΣ = QHQ⊤or do a Schur decomposition
ΓΣ = QRQ⊤. (H is Hessenberg and Q is orthogonal. Since ΓΣ has the same
eigenvalues as B⊤ΓB and they are all real, R is actually triangular instead of
quasi-triangular in the general case, Anderson et al. (1999). The evaluation of
(1.5) becomes O(m2), since it involves the solution of a linear system with the
matrix I −itH or I −itR, respectively. Reduction to tridiagonal, Hessenberg,
or Schur form is also O(m3), so the asymptotics in the number of risk factors
m remain the same in all cases. The critical N, above which the complete
spectral decomposition + fast evaluation via (1.3) is faster than the reduction
to tridiagonal or Hessenberg form + slower evaluation via (1.4) or (1.5) remains
to be determined empirically for given m on a specific machine.
The computation of the cumulant generating function and the characteristic
function from the diagonalized form is implemented in the following quantlets:

1.2
General Properties of Delta-Gamma-Normal Models
11
z= VaRcgfDG(t,par)
Computes the cumulant generating function (cgf) for the class of
quadratic forms of Gaussian vectors.
z= VaRcharfDG(t,par)
Computes the characteristic function for the class of quadratic
forms of Gaussian vectors.
t is the complex argument and par the parameter list generated by
VaRDGdecomp.
The advantage of the Cornish-Fisher approximation is that it is based on the
cumulants, which can be computed without any matrix decomposition:
κ1 = 1
2
X
i
λi
= 1
2 tr(ΓΣ),
κr = 1
2
X
i
{(r −1)!λr
i + r!δ2
i λr−2
i
} = 1
2(r −1)! tr((ΓΣ)r)
+ 1
2r!∆⊤Σ(ΓΣ)r−2∆
(r ≥2). Although the cost of computing the cumulants needed for the Cornish-
Fisher approximation is also O(m3), this method can be faster than the eigen-
value decomposition for small orders of approximation and relatively small
numbers of risk factors.
The computation of all cumulants up to a certain order directly from ΓΣ is im-
plemented in the quantlet VaRcumulantsDG, while the computation of a single
cumulant from the diagonal decomposition is provided by VaRcumulantDG:
vec= VaRcumulantsDG(n,par)
Computes the first n cumulants for the class of quadratic forms
of Gaussian vectors. The list par contains at least Gamma and
Sigma.
z= VaRcumulantDG(n,par)
Computes the n-th cumulant for the class of quadratic forms of
Gaussian vectors. The parameter list par is to be generated with
VaRDGdecomp.

12
1
Approximating Value at Risk in Conditional Gaussian Models
Partial Monte-Carlo (or partial Quasi-Monte-Carlo) costs O(m2) operations
per sample. (If Γ is sparse, it may cost even less.) The number of samples
needed is a function of the desired accuracy. It is clear from the asymptotic
costs of the three methods that partial Monte Carlo will be preferable for
sufficiently large m.
While Fourier-inversion and Partial Monte-Carlo can in principal achieve any
desired accuracy, the Cornish-Fisher approximations provide only a limited
accuracy, as shown in the next section.
1.3
Cornish-Fisher Approximations
1.3.1
Derivation
The Cornish-Fisher expansion can be derived in two steps. Let Φ denote some
base distribution and φ its density function. The generalized Cornish-Fisher
expansion (Hill and Davis, 1968) aims to approximate an α-quantile of F in
terms of the α-quantile of Φ, i.e., the concatenated function F −1 ◦Φ. The key
to a series expansion of F −1◦Φ in terms of derivatives of F and Φ is Lagrange’s
inversion theorem. It states that if a function s 7→t is implicitly defined by
t = c + s · h(t)
(1.6)
and h is analytic in c, then an analytic function f(t) can be developed into a
power series in a neighborhood of s = 0 (t = c):
f(t) = f(c) +
∞
X
r=1
sr
r! Dr−1[f ′ · hr](c),
(1.7)
where D denotes the differentation operator. For a given probability c = α,
f = Φ−1, and h = (Φ −F) ◦Φ−1 this yields
Φ−1(t) = Φ−1(α) +
∞
X
r=1
(−1)r sr
r! Dr−1[((F −Φ)r/φ) ◦Φ−1](α).
(1.8)
Setting s = 1 in (1.6) implies Φ−1(t) = F −1(α) and with the notations x =
F −1(α), z = Φ−1(α) (1.8) becomes the formal expansion
x = z +
∞
X
r=1
(−1)r 1
r!Dr−1[((F −Φ)r/φ) ◦Φ−1](Φ(z)).

1.3
Cornish-Fisher Approximations
13
With a = (F −Φ)/φ this can be written as
x = z +
∞
X
r=1
(−1)r 1
r!D(r−1)[ar](z)
(1.9)
with D(r) = (D+ φ′
φ )(D+2 φ′
φ ) . . . (D+r φ′
φ ) and D(0) being the identity operator.
(1.9) is the generalized Cornish-Fisher expansion. The second step is to choose a
specific base distribution Φ and a series expansion for a. The classical Cornish-
Fisher expansion is recovered if Φ is the standard normal distribution, a is
(formally) expanded into the Gram-Charlier series, and the terms are re-ordered
as described below.
The idea of the Gram-Charlier series is to develop the ratio of the moment
generating function of the considered random variable (M(t) = Eet∆V ) and
the moment generating function of the standard normal distribution (et2/2)
into a power series at 0:
M(t)e−t2/2 =
∞
X
k=0
cktk.
(1.10)
(ck are the Gram-Charlier coefficients. They can be derived from the moments
by multiplying the power series for the two terms on the left hand side.) Com-
ponentwise Fourier inversion yields the corresponding series for the probability
density
f(x) =
∞
X
k=0
ck(−1)kφ(k)(x)
(1.11)
and for the cumulative distribution function (cdf)
F(x) = Φ(x) −
∞
X
k=1
ck(−1)k−1φ(k−1)(x).
(1.12)
(φ und Φ are now the standard normal density and cdf. The derivatives of
the standard normal density are (−1)kφ(k)(x) = φ(x)Hk(x), where the Her-
mite polynomials Hk form an orthogonal basis in the Hilbert space L2(R, φ)
of the square integrable functions on R w.r.t. the weight function φ.
The
Gram-Charlier coefficients can thus be interpreted as the Fourier coefficients
of the function f(x)/φ(x) in the Hilbert space L2(R, φ) with the basis {Hk}
f(x)/φ(x) = P∞
k=0 ckHk(x).) Plugging (1.12) into (1.9) gives the formal Cornish-
Fisher expansion, which is re-grouped as motivated by the central limit theo-
rem.

14
1
Approximating Value at Risk in Conditional Gaussian Models
Assume that ∆V is already normalized (κ1 = 0, κ2 = 1) and consider the
normalized sum of independent random variables ∆Vi with the distribution F,
Sn =
1
√n
Pn
i=1 ∆Vi. The moment generating function of the random variable
Sn is
Mn(t) = M(t/√n)n = et2/2(
∞
X
k=0
cktkn−k/2)n.
Multiplying out the last term shows that the k-th Gram-Charlier coefficient
ck(n) of Sn is a polynomial expression in n−1/2, involving the coefficients ci up
to i = k. If the terms in the formal Cornish-Fisher expansion
x = z +
∞
X
r=1
(−1)r 1
r!D(r−1)
" 
−
∞
X
k=1
ck(n)Hk−1
!r#
(z)
(1.13)
are sorted and grouped with respect to powers of n−1/2, the classical Cornish-
Fisher series
x = z +
∞
X
k=1
n−k/2ξk(z)
(1.14)
results. (The Cornish-Fisher approximation for ∆V results from setting n = 1
in the re-grouped series (1.14).)
It is a relatively tedious process to express the adjustment terms ξk correpond-
ing to a certain power n−k/2 in the Cornish-Fisher expansion (1.14) directly
in terms of the cumulants κr, see (Hill and Davis, 1968).
Lee developed a
recurrence formula for the k-th adjustment term ξk in the Cornish-Fisher ex-
pansion, which is implemented in the algorithm AS269 (Lee and Lin, 1992; Lee
and Lin, 1993). (We write the recurrence formula here, because it is incorrect
in (Lee and Lin, 1992).)
ξk(H) = akH∗(k+1) −
k−1
X
j=1
j
k (ξk−j(H) −ξk−j) ∗(ξj −ajH∗(j+1)) ∗H,
(1.15)
with ak =
κk+2
(k+2)!. ξk(H) is a formal polynomial expression in H with the usual
algebraic relations between the summation “+” and the “multiplication” “∗”.
Once ξk(H) is multiplied out in ∗-powers of H, each H∗k is to be interpreted
as the Hermite polynomial Hk and then the whole term becomes a polynomial
in z with the “normal” multiplication “·”. ξk denotes the scalar that results
when the “normal” polynomial ξk(H) is evaluated at the fixed quantile z, while
ξk(H) denotes the expression in the (+, ∗)-algebra.

1.3
Cornish-Fisher Approximations
15
This formula is implemented by the quantlet
q = CornishFisher (z, n, cum)
Cornish-Fisher expansion for arbitrary orders for the standard
normal quantile z, order of approximation n, and the vector of
cumulants cum.
The following example prints the Cornish-Fisher approximation for increasing
orders for z=2.3 and cum=1:N:
XFGcofi.xpl
Contents of r
[1,]
2
4.2527
[2,]
3
5.3252
[3,]
4
5.0684
[4,]
5
5.2169
[5,]
6
5.1299
[6,]
7
5.1415
[7,]
8
5.255
1.3.2
Properties
The qualitative properties of the Cornish-Fisher expansion are:
+ If Fm is a sequence of distributions converging to the standard normal dis-
tribution Φ, the Edgeworth- and Cornish-Fisher approximations present
better approximations (asymptotically for m →∞) than the normal ap-
proximation itself.
−The approximated functions ˜F and ˜F −1◦Φ are not necessarily monotone.
−˜F has the “wrong tail behavior”, i.e., the Cornish-Fisher approximation
for α-quantiles becomes less and less reliable for α →0 (or α →1).
−The Edgeworth- and Cornish-Fisher approximations do not necessarily
improve (converge) for a fixed F and increasing order of approximation,
k.

16
1
Approximating Value at Risk in Conditional Gaussian Models
For more on the qualitative properties of the Cornish-Fisher approximation
see (Jaschke, 2001). It contains also an empirical analysis of the error of the
Cornish-Fisher approximation to the 99%-VaR in real-world examples as well
as its worst-case error on a certain class of one- and two-dimensional delta-
gamma-normal models:
+ The error for the 99%-VaR on the real-world examples - which turned
out to be remarkably close to normal - was about 10−6σ, which is more
than sufficient. (The error was normalized with respect to the portfolio’s
standard deviation, σ.)
−The (lower bound on the) worst-case error for the one- and two-dimensional
problems was about 1.0σ, which corresponds to a relative error of up to
100%.
In summary, the Cornish-Fisher expansion can be a quick approximation with
sufficient accuracy in many practical situations, but it should not be used
unchecked because of its bad worst-case behavior.
1.4
Fourier Inversion
1.4.1
Error Types in Approximating the Quantile through
Fourier Inversion
Let f
denote a continuous, absolutely integrable function and φ(t)
=
R ∞
−∞eitxf(x)dx its Fourier transform. Then, the inversion formula
f(x) = 1
2π
Z ∞
−∞
e−itxφ(t)dt
(1.16)
holds.
The key to an error analysis of trapezoidal, equidistant approximations to the
integral (1.16)
˜f(x, ∆t, t)
def
= ∆t
2π
∞
X
k=−∞
φ(t + k∆t)e−i(t+k∆t)x
(1.17)

1.4
Fourier Inversion
17
is the Poisson summation formula
˜f(x, ∆t, t) =
∞
X
j=−∞
f(x + 2π
∆t
j)e2πitj/∆t,
(1.18)
see (Abate and Whitt, 1992, p.22). If f(x) is approximated by ˜f(x, ∆t, 0), the
residual
ea(x, ∆t, 0) =
X
j̸=0
f(x + 2π
∆t
j)
(1.19)
is called the aliasing error, since different “pieces” of f are aliased into the
window (−π/∆t, π/∆t). Another suitable choice is t = ∆t/2:
˜f(x, ∆t, ∆t/2) =
∞
X
j=−∞
f(x + 2π
∆t
j)(−1)j.
(1.20)
If f is nonnegative, ˜f(x, ∆t, 0) ≥f(x). If f(x) is decreasing in |x| for |x| >
π/∆t, then ˜f(x, ∆t, ∆t/2) ≤f(x) holds for |x| < π/∆t. The aliasing error
can be controlled by letting ∆t tend to 0. It decreases only slowly when f has
“heavy tails”, or equivalently, when φ has non-smooth features.
It is practical to first decide on ∆t to control the aliasing error and then decide
on the cut-offin the sum (1.17):
˜˜f(x, T, ∆t, t) = ∆t
2π
X
|t+k∆t|≤T
φ(t + k∆t)e−i(t+k∆t)x.
(1.21)
Call et(x, T, ∆t, t)
def
= ˜˜f(x, T, ∆t, t) −˜f(x, ∆t, t) the truncation error.
For practical purposes, the truncation error et(x, T, ∆t, t) essentially depends
only on (x, T) and the decision on how to choose T and ∆t can be decoupled.
et(x, T, ∆t, t) converges to
et(x, T)
def
=
1
2π
T
Z
−T
e−itxφ(t)dt −f(x)
(1.22)
for ∆t ↓0.
Using
1
2π
R π
−π e−itxdt =
sin(πx)
πx
def
= sinc(x) and the convolution
theorem, one gets
1
2π
π/∆x
Z
−π/∆x
e−itxφ(t)dt =
Z ∞
−∞
f(y∆x) sinc(x/∆x −y)dy,
(1.23)

18
1
Approximating Value at Risk in Conditional Gaussian Models
which provides an explicit expression for the truncation error et(x, T) in terms
of f. It decreases only slowly with T ↑∞(∆x ↓0) if f does not have infinitely
many derivatives, or equivalently, φ has “power tails”. The following lemma
leads to the asymptotics of the truncation error in this case.
LEMMA 1.1 If limt→∞α(t) = 1, ν > 0, and
R ∞
T α(t)t−νeitdt exists and is
finite for some T, then
Z ∞
T
α(t)t−νeitxdt ∼
(
1
ν−1T −ν+1
if x = 0
i
xT −νeixT
if x ̸= 0
(1.24)
for T →∞.
PROOF:
Under the given conditions, both the left and the right hand side converge to 0,
so l’Hospital’s rule is applicable to the ratio of the left and right hand sides.
□
THEOREM 1.1 If the asymptotic behavior of a Fourier transform φ of a
function f can be described as
φ(t) = w|t|−νeib sign(t)+ix∗tα(t)
(1.25)
with limt→∞α(t) = 1, then the truncation error (1.22)
et(x, T) = −1
π ℜ
Z ∞
T
φ(t)e−itxdt

where ℜdenotes the real part, has the asymptotic behavior
∼
( wT −ν+1
π(1−ν) cos(b)
if x = x∗
−
wT −ν
π(x∗−x) cos(b + π
2 + (x∗−x)T)
if x ̸= x∗
(1.26)
for T →∞at all points x where
1
2π
R T
−T φ(t)e−itx converges to f(x). (If in the
first case cos(b) = 0, this shall mean that limT →∞et(x; T)T ν−1 = 0.)

1.4
Fourier Inversion
19
PROOF:
The previous lemma is applicable for all points x where the Fourier inversion
integral converges.
□
The theorem completely characterizes the truncation error for those cases,
where f has a “critical point of non-smoothness” and has a higher degree of
smoothness everywhere else. The truncation error decreases one power faster
away from the critical point than at the critical point. Its amplitude is inversely
proportional to the distance from the critical point.
Let ˜F be a (continuous) approximation to a (differentiable) cdf F with f =
F ′ > 0. Denote by ϵ ≥| ˜F(x) −F(x)| a known error-bound for the cdf. Any
solution ˜q(x) to ˜F(˜q(x)) = F(x) may be considered an approximation to the
true F(x)-quantile x. Call eq(x) = ˜q(x) −x the quantile error. Obviously, the
quantile error can be bounded by
|eq(x)| ≤
ϵ
infy∈U f(y),
(1.27)
where U is a suitable neighborhood of x. Given a sequence of approximations
˜Fϵ with supx | ˜Fϵ(x) −F(x)| = ϵ →0,
eq(x) ∼F(x) −˜Fϵ(x)
f(x)
(ϵ →0)
(1.28)
holds.
FFT-based Fourier inversion yields approximations for the cdf F on equidistant
∆x-spaced grids. Depending on the smoothness of F, linear or higher-order
interpolations may be used. Any monotone interpolation of {F(x0 + ∆xj)}j
yields a quantile approximation whose interpolation error can be bounded by
∆x. This bound can be improved if an upper bound on the density f in a
suitable neighborhood of the true quantile is known.

20
1
Approximating Value at Risk in Conditional Gaussian Models
1.4.2
Tail Behavior
If λj = 0 for some j, then |φ(t)| = O(e−δ2
j t2/2). In the following, we assume
that |λi| > 0 for all i. The norm of φ(t) has the form
|φ(t)| =
m
Y
i=1
(1 + λ2
i t2)−1/4 exp

−δ2
i t2/2
1 + λ2
i t2

,
(1.29)
|φ(t)| ∼w∗|t|−m/2
|t| →∞
(1.30)
with
w∗
def
=
m
Y
i=1
|λi|−1/2 exp

−1
2(δi/λi)2

.
(1.31)
The arg has the form
arg φ(t) = θt +
m
X
i=1
1
2 arctan(λit) −1
2δ2
i t2
λit
1 + λ2
i t2
	
,
(1.32)
arg φ(t) ∼θt +
m
X
i=1
π
4 sign(λit) −δ2
i t
2λi
)

(1.33)
(for |t| →∞). This motivates the following approximation for φ:
˜φ(t)
def
= w∗|t|−m/2 exp

iπ
4 m∗sign(t) + ix∗t
	
(1.34)
with
m∗
def
=
m
X
i=1
sign(λi),
(1.35)
x∗
def
= θ −1
2
m
X
i=1
δ2
i
λi
.
(1.36)
x∗is the location and w∗the “weight” of the singularity. The multivariate
delta-gamma-distribution is C∞except at x∗, where the highest continuous
derivative of the cdf is of order [(m −1)/2].
Note that
α(t)
def
= φ(t)/˜φ(t) =
Y
j
(1 −(iλjt)−1)−1/2 exp{1
2
δ2
j
λ2
j
(1 −iλjt)−1}
(1.37)
and α meets the assumptions of theorem 1.1.

1.4
Fourier Inversion
21
1.4.3
Inversion of the cdf minus the Gaussian Approximation
Assume that F is a cdf with mean µ and standard deviation σ, then
F(x) −Φ(x; µ, σ) = 1
2π
Z ∞
−∞
e−ixt i
t(φ(t) −eiµt−σ2t2/2) dt
(1.38)
holds, where Φ(.; µ, σ) is the normal cdf with mean µ and standard deviation
σ and eiµt−σ2t2/2 its characteristic function. (Integrating the inversion formula
(1.16) w.r.t. x and applying Fubini’s theorem leads to (1.38).) Applying the
Fourier inversion to F(x) −Φ(x; µ, σ) instead of F(x) solves the (numerical)
problem that
i
tφ(t) has a pole at 0.
Alternative distributions with known
Fourier transform may be chosen if they better approximate the distribution
F under consideration.
The moments of the delta-gamma-distribution can be derived from (1.3) and
(1.5):
µ =
X
i
(θi + 1
2λi) = θ⊤11 + 1
2 tr(ΓΣ)
and
σ2 =
X
i
(δ2
i + 1
2λ2
i ) = ∆⊤Σ∆+ 1
2 tr((ΓΣ)2).
Let ψ(t)
def
=
i
t(φ(t)−eiµt−σ2t2/2). Since ψ(−t) = ψ(t), the truncated sum (1.21)
can for t = ∆t/2 and T = (K −1
2)∆t be written as
˜˜F(xj; T, ∆t, t) −Φ(xj) = ∆t
π ℜ
 K−1
X
k=0
ψ((k + 1
2)∆t)e−i((k+ 1
2 )∆t)xj
!
,
which can comfortably be computed by a FFT with modulus N ≥K:
= ∆t
π ℜ
 e−i ∆t
2 xj
K−1
X
k=0
ψ((k + 1
2)∆t)e−ik∆tx0e−2πikj/N
,
(1.39)
with ∆x∆t = 2π
N and the last N −K components of the input vector to the
FFT are padded with zeros.
The aliasing error of the approximation (1.20) applied to F −N is
ea(x, ∆t, ∆t/2) =
X
j̸=0

F(x + 2π
∆t
j) −Φ(x + 2π
∆t
j)

(−1)j.
(1.40)

22
1
Approximating Value at Risk in Conditional Gaussian Models
The cases (λ, δ, θ) = (±
√
2, 0, ∓
√
2/2) are the ones with the fattest tails and
are thus candidates for the worst case for (1.40), asymptotically for ∆t →0. In
these cases, (1.40) is eventually an alternating sequence of decreasing absolute
value and thus
F(−π/∆t) + 1 −F(π/∆t) ≤
r
2
πee−1
2
√
2π/∆t
(1.41)
is an asymptotic bound for the aliasing error.
The truncation error (1.22) applied to F −N is
et(x; T) = −1
π ℜ
Z ∞
T
i
t
 φ(t) −eiµt−σ2t2/2
dt

.
(1.42)
The Gaussian part plays no role asymptotically for T →∞and Theorem 1.1
applies with ν = m/2 + 1.
The quantile error for a given parameter ϑ is
˜q(ϑ) −q(ϑ) ∼−eϑ
a(q(ϑ); ∆t) + eϑ
t (q(ϑ); T)
f ϑ(q(ϑ))
,
(1.43)
asymptotically for T →∞and ∆t →0. (q(ϑ) denotes the true 1%-quantile
for the triplet ϑ = (θ, ∆, Γ).) The problem is now to find the right trade-off
between “aliasing error” and “truncation error”, i.e., to choose ∆t optimally
for a given K.
Empirical observation of the one- and two-factor cases shows that (λ, δ, θ) =
(−
√
2, 0,
√
2/2) has the smallest density (≈0.008) at the 1%-quantile. Since
(λ, δ, θ) = (−
√
2, 0,
√
2/2) is the case with the maximal “aliasing error” as well,
it is the only candidate for the worst case of the ratio of the “aliasing error”
over the density (at the 1%-quantile).
The question which ϑ is the worst case for the ratio of the “truncation error”
over the density (at the 1%-quantile) is not as clear-cut. Empirical observation
shows that the case (λ, δ, θ) = (−
√
2, 0,
√
2/2) is also the worst case for this
ratio over a range of parameters in one- and two-factor problems. This leads to
the following heuristic to choose ∆t for a given K (T = (K −0.5)∆t). Choose
∆t such as to minimize the sum of the aliasing and truncation errors for the
case (λ, δ, θ) = (−
√
2, 0,
√
2/2), as approximated by the bounds (1.41) and
lim sup
T →∞
|et(x, T)|T 3/2 =
w
π|x∗−x|
(1.44)

1.4
Fourier Inversion
23
with w = 2−1/4, x∗=
√
2/2, and the 1%-quantile x ≈−3.98. (Note that this
is suitable only for intermediate K, leading to accuracies of 1 to 4 digits in the
quantile. For higher K, other cases become the worst case for the ratio of the
truncation error over the density at the quantile.)
Since F −N has a kink in the case m = 1, λ ̸= 0, higher-order interpolations
are futile in non-adaptive methods and ∆x =
2π
N∆t is a suitable upper bound
for the interpolation error. By experimentation, N ≈4K suffices to keep the
interpolation error comparatively small.
K = 26 evaluations of φ (N = 28) suffice to ensure an accuracy of 1 digit in the
approximation of the 1%-quantile over a sample of one- and two-factor cases.
K = 29 function evaluations are needed for two digits accuracy. The XploRe
implementation of the Fourier inversion is split up as follows:
z= VaRcharfDGF2(t,par)
implements the function ψ(t)
def
=
i
t(φ(t)−eiµt−σ2t2/2) for the com-
plex argument t and the parameter list par.
z= VaRcorrfDGF2(x,par)
implements the correction term Φ(x, µ, σ2) for the argument x
and the parameter list par.
vec= gFourierInversion(N,K,dt,t0,x0,charf,par)
implements a generic Fourier inversion like in (1.39). charf is a
string naming the function to be substituted for ψ in (1.39). par
is the parameter list passed to charf.
gFourierInversion can be applied to VaRcharfDG, giving the density, or to
VaRcharfDGF2, giving the cdf minus the Gaussian approximation. The three
auxiliary functions are used by

24
1
Approximating Value at Risk in Conditional Gaussian Models
l= VaRcdfDG(par,N,K,dt)
to approximate the cumulative distribution function (cdf) of the
distribution from the class of quadratic forms of Gaussian vectors
with parameter list par. The output is a list of two vectors x and
y, containing the cdf-approximation on a grid given by x.
q= cdf2quant(a,l)
approximates the a-quantile from the list l, as returned from
VaRcdfDG.
q= VaRqDG(a,par,N,K,dt)
calls VaRcdfDG and cdf2quant to approximate an a-quantile for
the distribution of the class of quadratic forms of Gaussian vectors
that is defined by the parameter list par.
The following example plots the 1%-quantile for a one-parametric family of the
class of quadratic forms of one- and two-dimensional Gaussian vectors:
XFGqDGtest.xpl
1.5
Variance Reduction Techniques in
Monte-Carlo Simulation
1.5.1
Monte-Carlo Sampling Method
The partial Monte-Carlo method is a Monte-Carlo simulation that is performed
by generating underlying prices given the statistical model and then valuing
them using the simple delta-gamma approximation. We denote X as a vector
of risk factors, ∆V as the change in portfolio value resulting from X, L as
−∆V , α as a confidence level and l as a loss threshold.
We also let
• ∆= first order derivative with regard to risk factors
• Γ = second order derivative with regard to risk factors

1.5
Variance Reduction Techniques in Monte-Carlo Simulation
25
• ΣX = covariance matrix of risk factors
Equation 1.1 defines the class of Delta-Gamma normal methods. The detailed
procedures to implement the partial Monte-Carlo method are as follows
1. Generate N scenarios by simulating risk factors X1, ..., XN according to
ΣX;
2. Revalue the portfolio and determine the loss in the portfolio values L1, ..., LN
using the simple delta-gamma approximation;
3. Calculate the fraction of scenarios in which losses exceed l:
N −1
N
X
i=1
1(Li > l),
(1.45)
where 1(Li > l) = 1 if Li > l and 0 otherwise.
The partial Monte-Carlo method is flexible and easy to implement. It provides
the accurate estimation of the VaR when the loss function is approximately
quadratic. However, one drawback is that for a large number of risk factors,
it requires a large number of replications and takes a long computational time.
According to Boyle, Broadie and Glasserman (1998), the convergence rate of
the Monte-Carlo estimate is 1/
√
N. Different variance reduction techniques
have been developed to increase the precision and speed up the process. In
the next section, we will give a brief overview of different types of variance
reduction techniques, Boyle et al. (1998).
1. Antithetic Method
We assume Wi = f(zi), where zi ∈Rm are independent samples from the
standard normal distribution. In our case, the function f is defined as
f(zi) = I(Li > l) = I[−
m
X
i=1
(δizi + 1
2λiz2
i ) > l].
(1.46)
Based on N replications, an unbiased estimator of the µ = E(W) is given
by
ˆµ = 1
N
N
X
i=1
Wi = 1
N
N
X
i=1
f(zi).
(1.47)

26
1
Approximating Value at Risk in Conditional Gaussian Models
In this context, the method of antithetic variates is based on the obser-
vation that if zi has a standard normal distribution, then so does −zi.
Similarly, each
˜µ = 1
N
N
X
i=1
f(−zi)
(1.48)
is also an unbiased estimator of µ. Therefore,
ˆµAV = ˆµ + ˜µ
2
(1.49)
is an unbiased estimator of µ as well.
The intuition behind the antithetic method is that the random inputs
obtained from the collection of antithetic pairs (zi, −zi) are more regularly
distributed than a collection of 2N independent samples. In particular,
the sample mean over the antithetic pairs always equals the population
mean of 0, whereas the mean over finitely many independent samples is
almost surely different from 0.
2. Control Variates
The basic idea of control variates is to replace the evaluation of an un-
known expectation with the evaluation of the difference between the un-
known quantity and another expectation whose value is known.
The
standard Monte-Carlo estimate of µ = E[Wi] = E[f(zi)] is
1
N
PN
i=1 Wi.
Suppose we know ˜µ = E[g(zi)]. The method of control variates uses the
known error
1
N
N
X
i=1
˜
Wi −˜µ
(1.50)
to reduce the unknown error
1
N
N
X
i=1
Wi −µ.
(1.51)
The controlled estimator has the form
1
N
N
X
i=1
Wi −β( 1
N
N
X
i=1
˜
Wi −˜µ).
(1.52)
Since the term in parentheses has expectation zero, equation (1.52) pro-
vides an unbiased estimator of µ as long as β is independent. In practice,

1.5
Variance Reduction Techniques in Monte-Carlo Simulation
27
if the function g(zi) provides a close approximation of f(zi), we usually
set β = 1 to simplify the calculation.
3. Moment Matching Method
Let zi, i = 1, ..., n, denote an independent standard normal random vec-
tor used to drive a simulation. The sample moments will not exactly
match those of the standard normal. The idea of moment matching is to
transform the zi to match a finite number of the moments of the underly-
ing population. For example, the first and second moment of the normal
random number can be matched by defining
˜zi = (zi −˜z)σz
sz
+ µz, i = 1, .....n
(1.53)
where ˜z is the sample mean of the zi, σz is the population standard devi-
ation, sz is the sample standard deviation of zi, and µz is the population
mean.
The moment matching method can be extended to match covariance and
higher moments as well.
4. Stratified Sampling
Like many variance reduction techniques, stratified sampling seeks to
make the inputs to simulation more regular than the random inputs. In
stratified sampling, rather than drawing zi randomly and independent
from a given distribution, the method ensures that fixed fractions of the
samples fall within specified ranges. For example, we want to generate
N m-dimensional normal random vectors for simulation input. The em-
pirical distribution of an independent sample (z1, . . . , zN) will look only
roughly like the true normal density; the rare events - which are im-
portant for calculating the VaR - will inevitably be underrepresented.
Stratified sampling can be used to ensure that exactly one observation
zk
i lies between the (i −1)/N and i/N quantiles (i = 1, ..., N) of the k-th
marginal distribution for each of the m components. One way to imple-
ment that is to generate Nm independent uniform random numbers uk
i
on [0, 1] (k = 1, . . . , m, i = 1, . . . , N) and set
˜zk
i = Φ−1[(i + uk
i −1)/N], i = 1, ...., N
(1.54)
where Φ−1 is the inverse of the standard normal cdf. (In order to achieve
satisfactory sampling results, we need a good numerical procedure to cal-
culate Φ−1.) An alternative is to apply the stratification only to the most

28
1
Approximating Value at Risk in Conditional Gaussian Models
important components (directions), usually associated to the eigenvalues
of largest absolute value.
5. Latin Hypercube Sampling
The Latin Hypercube Sampling method was first introduced by McKay,
Beckman and Conover (1979). In the Latin Hypercube Sampling method,
the range of probable values for each component uk
i is divided into N seg-
ments of equal probability. Thus, the m-dimensional space, consisting of
k parameters, is partitioned into N m cells, each having equal probability.
For example, for the case of dimension m = 2 and N = 10 segments, the
parameter space is divided into 10 × 10 cells. The next step is to choose
10 cells from the 10 × 10 cells. First, the uniform random numbers are
generated to calculate the cell number. The cell number indicates the
segment number the sample belongs to, with respect to each of the pa-
rameters. For example, a cell number (1,8) indicates that the sample
lies in the segment 1 with respect to first parameter, segment 10 with
respect to second parameter. At each successive step, a random sample
is generated, and is accepted only if it does not agree with any previous
sample on any of the segment numbers.
6. Importance sampling
The technique builds on the observation that an expectation under one
probability measure can be expressed as an expectation under another
through the use of a likelihood ratio. The intuition behind the method is
to generate more samples from the region that is more important to the
practical problem at hand. In next the section, we will give a detailed
description of calculating VaR by the partial Monte-Carlo method with
importance sampling.
1.5.2
Partial Monte-Carlo with Importance Sampling
In the basic partial Monte-Carlo method, the problem of sampling changes in
market risk factors Xi is transformed into a problem of sampling the vector z of
underlying standard normal random variables. In importance sampling, we will
change the distribution of z from N(0, I) to N(µ, Σ). The key steps proposed
by Glasserman, Heidelberger and Shahabuddin (2000) are to calculate
P(L > l) = Eµ,Σ[θ(z)I(L > l)]
(1.55)

1.5
Variance Reduction Techniques in Monte-Carlo Simulation
29
Expectation is taken with z sampled from N(µ, Σ) rather than its original
distribution N(0, I). To correct for this change of distribution, we weight the
loss indictor I(L > l) by the likelihood ratio
θ(z) = |Σ|1/2e−1
2 µ⊤Σ−1µe−1
2 [z⊤(I−Σ−1)z−2µ⊤Σ−1z],
(1.56)
which is simply the ratio of N[0, I] and N[µ, Σ] densities evaluated at z.
The next task is to choose µ and Σ so that the Monte-Carlo estimator will have
minimum variance. The key to reducing the variance is making the likelihood
ratio small when L > l. Equivalently, µ and Σ should be chosen in the way
to make L > l more likely under N(µ, Σ) than under N(0, I). The steps of the
algorithm are following:
1. Decomposition Process
We follow the decomposition steps described in the section 1.2 and find
the cumulant generating function of L given by
κ(ω) =
m
X
i=1
1
2[ (ωδi)2
1 −ωλi
−log(1 −ωλi)]
(1.57)
2. Transform N(0, I) to N(µ, Σ)
If we take the first derivative of κ(ω) with respect to ω, we will get:
d
dω κ(ω) = Eµ(ω),Σ(ω)[L] = l
(1.58)
where Σ(ω) = (I −ωΛ)−1 and µ(ω) = ωΣ(ω)δ. Since our objective is
to estimate P(L > l), we will choose ω to be the solution of equation
(1.58). The loss exceeding scenarios (L > l), which were previously rare
under N(0, I), are typical under N(µ, Σ), since the expected value of the
approximate value L is now l. According to Glasserman et al. (2000), the
effectiveness of this importance sampling procedure is not very sensitive
to the choice of ω.
After we get N(µ(ω), Σ(ω)), we can follow the same steps in the basic
partial Monte-Carlo simulation to calculate the VaR. The only difference
is that the fraction of scenarios in which losses exceed l is calculated by:
1
N
N
X
i=1
[exp(−ωLi + κ(ω))I(Li > l)]
(1.59)

30
1
Approximating Value at Risk in Conditional Gaussian Models
An important feature of this method is that it can be easily added to an
existing implementation of partial Monte-Carlo simulation. The impor-
tance sampling algorithm differs only in how it generates scenarios and
in how it weights scenarios as in equation (1.59).
1.5.3
XploRe Examples
VaRMC = VaRestMC (VaRdelta, VaRgamma, VaRcovmatrix,
smethod, opt)
Partial Monte-Carlo method to calculate VaR based on Delta-
Gamma Approximation.
The function VaRestMC uses the different types of variance reduction to calcu-
late the VaR by the partial Monte-Carlo simulation. We employ the variance
reduction techniques of moment matching, Latin Hypercube Sampling and im-
portance sampling.
The output is the estimated VaR. In order to test the
efficiency of different Monte-Carlo sampling methods, we collect data from the
MD*BASE and construct a portfolio consisting of three German stocks (Bayer,
Deutsche Bank, Deutsche Telekom) and corresponding 156 options on these un-
derlying stocks with maturity ranging from 18 to 211 days on May 29, 1999.
The total portfolio value is 62,476 EUR. The covariance matrix for the stocks
is provided as well. Using the Black-Scholes model, we also construct the ag-
gregate delta and aggregate gamma as the input to the Quantlet. By choosing
the importance sampling method, 0.01 confidence level, 1 days forecast horizon
and 1,000 times of simulation, the result of the estimation is as follows.
XFGVaRMC.xpl
Contents of VaRMC
[1,]
771.73
It tells us that we expect the loss to exceed 771.73 EUR or 1.24% of portfolio
value with less than 1% probability in 1 day. However, the key question of
the empirical example is that how much variance reduction is achieved by the
different sampling methods. We run each of the four sampling methods 1,000

1.5
Variance Reduction Techniques in Monte-Carlo Simulation
31
times and estimated the standard error of the estimated VaR for each sampling
method. The table (1.1) summarizes the results.
Estimated VaR
Standard Error
Variance Reduction
Plain-Vanilla
735.75
36.96
0%
Moment Matching
734.92
36.23
1.96%
Latin Hypercube
757.83
21.32
42.31%
Importance Sampling
761.75
5.66
84.68%
Table 1.1. Variance Reduction of Estimated VaR for German Stock
Option Portfolio
As we see from the table (1.1), the standard error of the importance sampling
is 84.68% less than those of plain-vanilla sampling and it demonstrates that
approximately 42 times more scenarios would have to be generated using the
plain-vanilla method to achieve the same precision obtained by importance
sampling based on Delta-Gamma approximation. These results clearly indicate
the great potential speed-up of estimation of the VaR by using the importance
sampling method. This is why we set the importance sampling as the default
sampling method in the function VaRestMC. However, the Latin Hypercube
sampling method also achieved 42.31% of variance reduction. One advantage
of the Latin Hypercube sampling method is that the decomposition process is
not necessary. Especially when the number of risk factors (m) is large, the
decomposition (O(m3)) dominates the sampling (O(m)) and summation O(1)
in terms of computational time. In this case, Latin Hypercube sampling may
offer the better performance in terms of precision for a given computational
time.
Bibliography
Abate, J. and Whitt, W. (1992). The Fourier-series method for inverting trans-
forms of probability distributions, Queuing Systems Theory and Applica-
tions 10: 5–88.
Albanese, C., Jackson, K. and Wiberg, P. (2000). Fast convolution method for
VaR and VaR gradients, http://www.math-point.com/fconv.ps.
Anderson, E., Bai, Z., Bischof, C., Blackford, S., Demmel, J., Dongarra,
J., Croz, J. D., Greenbaum, A., Hammarling, S., McKenney, A. and

32
1
Approximating Value at Risk in Conditional Gaussian Models
Sorensen, D. (1999). LAPACK Users’ Guide, third edn, SIAM. http:
//www.netlib.org/lapack/lug/.
Basel Committee on Banking Supervision (1995). An internal model-based ap-
proach to market risk capital requirements, http://www.bis.org/publ/
bcbsc224.pdf.
Boyle, P., Broadie, M. and Glasserman, P. (1998). Monte Carlo methods for
security pricing, Journal of Economic Dynamics and Control 3: 1267–
1321.
Breckling, J., Eberlein, E. and Kokic, P. (2000). A tailored suit for risk man-
agement: Hyperbolic model, in J. Franke, W. H¨ardle and G. Stahl (eds),
Measuring Risk in Complex Stochastic Systems, Vol. 147 of Lecture Notes
in Statistics, Springer, New York, chapter 12, pp. 198–202.
Britton-Jones, M. and Schaefer, S. (1999). Non-linear Value-at-Risk, European
Finance Review 2: 161–187.
Embrechts, P., Kl¨uppelberg, C. and Mikosch, T. (1997). Modelling extremal
events, Springer-Verlag, Berlin.
Embrechts, P., McNeil, A. and Straumann, D. (1999). Correlation and depen-
dence in risk management: Properties and pitfalls, http://www.math.
ethz.ch/~strauman/preprints/pitfalls.ps.
Engle, R. (2000). Dynamic conditional correlation - a simple class of multivari-
ate GARCH models, http://weber.ucsd.edu/~mbacci/engle/.
Fallon, W. (1996).
Calculating Value at Risk, http://wrdsenet.wharton.
upenn.edu/fic/wfic/papers/96/9649.pdf. Wharton Financial Institu-
tions Center Working Paper 96-49.
Glasserman, P., Heidelberger, P. and Shahabuddin, P. (2000). Efficient monte
carlo methods for value at risk, http://www.research.ibm.com/people/
b/berger/papers/RC21723.pdf. IBM Research Paper RC21723.
Hill, G. W. and Davis, A. W. (1968). Generalized asymptotic expansions of
Cornish-Fisher type, Ann. Math. Statist. 39: 1264–1273.
Jaschke, S. (2001).
The Cornish-Fisher-expansion in the context of delta-
gamma-normal approximations, http://www.jaschke-net.de/papers/
CoFi.pdf. Discussion Paper 54, Sonderforschungsbereich 373, Humboldt-
Universit¨at zu Berlin.

1.5
Variance Reduction Techniques in Monte-Carlo Simulation
33
Jorion, P. (2000). Value at Risk: The New Benchmark for Managing Financial
Risk, McGraw-Hill, New York.
Lee, Y. S. and Lin, T. K. (1992).
Higher-order Cornish Fisher expansion,
Applied Statistics 41: 233–240.
Lee, Y. S. and Lin, T. K. (1993). Correction to algorithm AS269 : Higher-order
Cornish Fisher expansion, Applied Statistics 42: 268–269.
Li, D. (1999). Value at Risk based on the volatility, skewness and kurtosis,
http://www.riskmetrics.com/research/working/var4mm.pdf.
Risk-
Metrics Group.
Longerstaey, J. (1996).
RiskMetrics technical document, Technical Report
fourth edition, J.P.Morgan. originally from http://www.jpmorgan.com/
RiskManagement/RiskMetrics/, now http://www.riskmetrics.com.
McKay, M. D., Beckman, R. J. and Conover, W. J. (1979). A comparison
of three methods for selecting values of input variables in the analysis of
output from a computer code, Technometrics 21(2): 239–245.
Mina, J. and Ulmer, A. (1999).
Delta-gamma four ways, http://www.
riskmetrics.com.
Pichler, S. and Selitsch, K. (1999). A comparison of analytical VaR method-
ologies for portfolios that include options, http://www.tuwien.ac.at/
E330/Research/paper-var.pdf. Working Paper TU Wien.
Pritsker, M. (1996). Evaluating Value at Risk methodologies: Accuracy versus
computational time, http://wrdsenet.wharton.upenn.edu/fic/wfic/
papers/96/9648.pdf.
Wharton Financial Institutions Center Working
Paper 96-48.
Rogers, L. and Zane, O. (1999). Saddle-point approximations to option prices,
Annals of Applied Probability 9(2): 493–503. http://www.bath.ac.uk/
~maslcgr/papers/.
Rouvinez, C. (1997). Going greek with VaR, Risk 10(2): 57–65.
Zangari, P. (1996a). How accurate is the delta-gamma methodology?, Risk-
Metrics Monitor 1996(third quarter): 12–29.
Zangari, P. (1996b). A VaR methodology for portfolios that include options,
RiskMetrics Monitor 1996(first quarter): 4–12.


2 Applications of Copulas for the
Calculation of Value-at-Risk
J¨orn Rank and Thomas Siegl
We will focus on the computation of the Value-at-Risk (VaR) from the perspec-
tive of the dependency structure between the risk factors. Apart from historical
simulation, most VaR methods assume a multivariate normal distribution of
the risk factors. Therefore, the dependence structure between different risk
factors is defined by the correlation between those factors. It is shown in Em-
brechts, McNeil and Straumann (1999) that the concept of correlation entails
several pitfalls. The authors therefore propose the use of copulas to quantify
dependence.
For a good overview of copula techniques we refer to Nelsen (1999). Copulas
can be used to describe the dependence between two or more random variables
with arbitrary marginal distributions. In rough terms, a copula is a function
C : [0, 1]n →[0, 1] with certain special properties. The joint multidimensional
cumulative distribution can be written as
P(X1 ≤x1, . . . , Xn ≤xn)
=
C (P(X1 ≤x1), . . . , P(Xn ≤xn))
=
C (F1(x1), . . . , Fn(xn)) ,
where F1, . . . , Fn denote the cumulative distribution functions of the n random
variables X1, . . . , Xn. In general, a copula C depends on one or more cop-
ula parameters p1, . . . , pk that determine the dependence between the random
variables X1, . . . , Xn. In this sense, the correlation ρ(Xi, Xj) can be seen as a
parameter of the so-called Gaussian copula.
Here we demonstrate the process of deriving the VaR of a portfolio using the
copula method with XploRe, beginning with the estimation of the selection
of the copula itself, estimation of the copula parameters and the computation
of the VaR. Backtesting of the results is performed to show the validity and
relative quality of the results. We will focus on the case of a portfolio containing

36
2
Applications of Copulas for the Calculation of Value-at-Risk
two market risk factors only, the FX rates USD/EUR and GBP/EUR. Copulas
in more dimensions exist, but the selection of suitable n-dimensional copulas
is still quite limited. While the case of two risk factors is still important for
applications, e.g. spread trading, it is also the case that can be best described.
As we want to concentrate our attention on the modelling of the dependency
structure, rather than on the modelling of the marginal distributions, we re-
strict our analysis to normal marginal densities. On the basis of our backtesting
results, we find that the copula method produces more accurate results than
“correlation dependence”.
2.1
Copulas
In this section we summarize the basic results without proof that are necessary
to understand the concept of copulas. Then, we present the most important
properties of copulas that are needed for applications in finance. In doing so,
we will follow the notation used in Nelsen (1999).
2.1.1
Definition
DEFINITION 2.1 A 2-dimensional copula is a function C : [0, 1]2 →[0, 1]
with the following properties:
1. For every u ∈[0, 1]
C(0, u) = C(u, 0) = 0 .
(2.1)
2. For every u ∈[0, 1]
C(u, 1) = u
and
C(1, u) = u .
(2.2)
3. For every (u1, u2), (v1, v2) ∈[0, 1] × [0, 1] with u1 ≤v1 and u2 ≤v2:
C(v1, v2) −C(v1, u2) −C(u1, v2) + C(u1, u2) ≥0 .
(2.3)
A function that fulfills property 1 is also said to be grounded. Property 3 is
the two-dimensional analogue of a nondecreasing one-dimensional function. A
function with this feature is therefore called 2-increasing.
The usage of the name ”copula” for the function C is explained by the following
theorem.

2.1
Copulas
37
2.1.2
Sklar’s Theorem
The distribution function of a random variable R is a function F that assigns
all r ∈R a probability F(r) = P(R ≤r). In addition, the joint distribution
function of two random variables R1, R2 is a function H that assigns all r1, r2 ∈
R a probability H(r1, r2) = P(R1 ≤r1, R2 ≤r2).
THEOREM 2.1 (Sklar’s theorem) Let H be a joint distribution function
with margins F1 and F2. Then there exists a copula C with
H(x1, x2) = C(F1(x1), F2(x2))
(2.4)
for every x1, x2 ∈R. If F1 and F2 are continuous, then C is unique. Otherwise,
C is uniquely determined on Range F1 × Range F2. On the other hand, if C is
a copula and F1 and F2 are distribution functions, then the function H defined
by (2.4) is a joint distribution function with margins F1 and F2.
It is shown in Nelsen (1999) that H has margins F1 and F2 that are given by
F1(x1)
def
= H(x1, +∞) and F2(x2)
def
= H(+∞, x2), respectively. Furthermore,
F1 and F2 themselves are distribution functions. With Sklar’s Theorem, the
use of the name “copula” becomes obvious.
It was chosen by Sklar (1996)
to describe “a function that links a multidimensional distribution to its one-
dimensional margins” and appeared in mathematical literature for the first
time in Sklar (1959).
2.1.3
Examples of Copulas
Product Copula
The structure of independence is especially important for
applications.
DEFINITION 2.2 Two random variables R1 and R2 are independent if and
only if the product of their distribution functions F1 and F2 equals their joint
distribution function H,
H(r1, r2) = F1(r1) · F2(r2)
for all
r1, r2 ∈R .
(2.5)
Thus, we obtain the independence copula C = Π by
Π(u1, . . . , un) =
n
Y
i=1
ui ,

38
2
Applications of Copulas for the Calculation of Value-at-Risk
which becomes obvious from the following theorem:
THEOREM 2.2 Let R1 and R2 be random variables with continuous distri-
bution functions F1 and F2 and joint distribution function H. Then R1 and
R2 are independent if and only if CR1R2 = Π.
From Sklar’s Theorem we know that there exists a unique copula C with
P(R1 ≤r1, R2 ≤r2) = H(r1, r2) = C(F1(r1), F2(r2)) .
(2.6)
Independence can be seen using Equation (2.4) for the joint distribution func-
tion H and the definition of Π,
H(r1, r2) = C(F1(r1), F2(r2)) = F1(r1) · F2(r2) .
(2.7)
Gaussian Copula
The second important copula that we want to investigate
is the Gaussian or normal copula,
CGauss
ρ
(u, v)
def
=
Z Φ−1
1
(u)
−∞
Z Φ−1
2
(v)
−∞
fρ(r1, r2)dr2dr1 ,
(2.8)
see Embrechts, McNeil and Straumann (1999). In (2.8), fρ denotes the bivariate
normal density function with correlation ρ for n = 2. The functions Φ1, Φ2
in (2.8) refer to the corresponding one-dimensional, cumulated normal density
functions of the margins.
In the case of vanishing correlation, ρ = 0, the Gaussian copula becomes
CGauss
0
(u, v)
=
Z Φ−1
1
(u)
−∞
f1(r1)dr1
Z Φ−1
2
(v)
−∞
f2(r2)dr2
=
u v
(2.9)
=
Π(u, v)
if
ρ = 0 .
Result (2.9) is a direct consequence of Theorem 2.2.
As Φ1(r1), Φ2(r2) ∈[0, 1], one can replace u, v in (2.8) by Φ1(r1), Φ2(r2). If
one considers r1, r2 in a probabilistic sense, i.e. r1 and r2 being values of two
random variables R1 and R2, one obtains from (2.8)
CGauss
ρ
(Φ1(r1), Φ2(r2)) = P(R1 ≤r1, R2 ≤r2) .
(2.10)
In other words: CGauss
ρ
(Φ1(r1), Φ2(r2)) is the binormal cumulated probability
function.

2.1
Copulas
39
Gumbel-Hougaard Copula
Next, we consider the Gumbel-Hougaard family of
copulas, see Hutchinson (1990). A discussion in Nelsen (1999) shows that Cθ
is suited to describe bivariate extreme value distributions. It is given by the
function
Cθ(u, v)
def
= exp
n
−

(−ln u)θ + (−ln v)θ1/θo
.
(2.11)
The parameter θ may take all values in the interval [1, ∞).
For θ = 1, expression (2.11) reduces to the product copula, i.e. C1(u, v) =
Π(u, v) = u v. For θ →∞one finds for the Gumbel-Hougaard copula
Cθ(u, v)
θ→∞
−→min(u, v)
def
= M(u, v).
It can be shown that M is also a copula. Furthermore, for any given copula C
one has C(u, v) ≤M(u, v), and M is called the Fr´echet-Hoeffding upper bound.
The two-dimensional function W(u, v)
def
= max(u+v−1, 0) defines a copula with
W(u, v) ≤C(u, v) for any other copula C. W is called the Fr´echet-Hoeffding
lower bound.
2.1.4
Further Important Properties of Copulas
In this section we focus on the properties of copulas. The theorem we will
present next establishes the continuity of copulas via a Lipschitz condition on
[0, 1] × [0, 1]:
THEOREM 2.3 Let C be a copula. Then for every u1, u2, v1, v2 ∈[0, 1]:
|C(u2, v2) −C(u1, v1)| ≤|u2 −u1| + |v2 −v1| .
(2.12)
From (2.12) it follows that every copula C is uniformly continuous on its do-
main. A further important property of copulas concerns the partial derivatives
of a copula with respect to its variables:
THEOREM 2.4 Let C be a copula. For every u ∈[0, 1], the partial derivative
∂C/∂v exists for almost every v ∈[0, 1]. For such u and v one has
0 ≤∂
∂v C(u, v) ≤1 .
(2.13)
The analogous statement is true for the partial derivative ∂C/∂u.
In addition, the functions u →Cv(u)
def
= ∂C(u, v)/∂v and v →Cu(v)
def
=
∂C(u, v)/∂u are defined and nondecreasing almost everywhere on [0,1].

40
2
Applications of Copulas for the Calculation of Value-at-Risk
To give an example of this theorem, we consider the partial derivative of the
Gumbel-Hougaard copula (2.11) with respect to u,
Cθ,u(v) = ∂
∂uCθ(u, v) = exp
n
−

(−ln u)θ + (−ln v)θ1/θo
×

(−ln u)θ + (−ln v)θ−θ−1
θ
(−ln u)θ−1
u
. (2.14)
Note that for u ∈(0, 1) and for all θ ∈R where θ > 1, Cθ,u is a strictly
increasing function of v. Therefore the inverse function C−1
θ,u is well defined.
However, as one might guess from (2.14), C−1
θ,u can not be calculated analytically
so that some kind of numerical algorithm has to be used for this task. As Cθ
is symmetric in u and v, the partial derivative of Cθ with respect to v shows
an identical behaviour for the same set of parameters.
We will end this section with a statement on the behaviour of copulas under
strictly monotone transformations of random variables.
THEOREM 2.5 Let R1 and R2 be random variables with continuous distri-
bution functions and with copula CR1R2. If α1 and α2 are strictly increasing
functions on Range R1 and Range R2, then Cα1(R1) α2(R2) = CR1R2. In other
words: CR1R2 is invariant under strictly increasing transformations of R1 and
R2.
2.2
Computing Value-at-Risk with Copulas
Now that we have given the most important properties of copulas, we turn to
the practical question of how to compute the Value-at-Risk of a portfolio using
copulas. The following steps need to be performed:
2.2.1
Selecting the Marginal Distributions
The copula method works with any given marginal distribution, i.e. it does
not restrict the choice of margins. However, we will use normal margins for
simplicity and in order to allow a comparison with standard VaR methods.

2.2
Computing Value-at-Risk with Copulas
41
2.2.2
Selecting a Copula
A wide variety of copulas exists, mainly for the two dimensional case (Nelsen
(1999)).
In our numerical tests, we will use some of the copulas presented
in Table 4.1 of Nelsen (1999) in our experiments for comparison which are
implemented in the function
C = VaRcopula(uv,theta,0,copula)
returns Cθ(u, v) for copula copula with parameter θ = theta. uv
is a n × 2 vector of coordinates, where the copula is calculated.
For easy reference the implemented copulas are given in Table 2.1.
2.2.3
Estimating the Copula Parameters
After selecting a copula we fit the copula to a time series
s = s(1), . . . , s(T ) with s(t) = (s(t)
1 , . . . , s(t)
n )
for t ∈1, . . . , T. For simplicity we assume that the s(t) are realizations of i.i.d.
random variables S(t). The first step will be to determine the parameters of
the marginal distributions. In the numerical example we will use the normal
distribution N(0, σ2
i ), and estimate the volatility σi using an equally weighted
volatility estimator ˆσ2
i =
1
T −1
PT
t=2(r(t)
i )2 of the returns r(t)
i
= log(s(t)
i /s(t−1)
i
)
for simplicity.
The marginal distributions of the risk factors are then log-
normal.
The remaining task is to estimate the copula parameters.
In the
XploRe VaR quantlib this is done by the function
res = VaRfitcopula(history,copula,method)
fits the copula to the history using fitting function method.
The result res is a list containing the estimates of the copula
parameter together with there standard deviations.
Least Square Fit
The main idea of the least square fit is that the cumulative
distribution function F (C)
θ
(x) defined by the copula C should fit the sample

42
2
Applications of Copulas for the Calculation of Value-at-Risk
#
Cθ(u, v) =
θ ∈
1
max

[u−θ + v−θ −1]−1/θ, 0

[−1, ∞)\{0}
2
max

1 −[(1 −u)θ + (1 −v)θ −1]1/θ, 0

[1, ∞)
3
uv
1−θ(1−u)(1−v)
[−1, 1)
4
exp
 −[(−ln u)θ + (−ln v)θ]1/θ
[1, ∞)
5
−1
θ ln

1 + (e−θu−1)(e−θv−1)
e−θ−1

(−∞, ∞)\{0}
6
1 −
h
(1 −u)θ + (1 −v)θ −(1 −u)θ(1 −v)θ)
i1/θ
[1, ∞)
7
max
h
θuv + (1 −θ)(u + v −1), 0
i
(0, 1]
8
max
h
θ2uv−(1−u)(1−v)
θ2−(θ−1)2(1−u)(1−v), 0
i
(0, 1]
9
uv exp(−θ ln u ln v)
(0, 1]
10
uv/
h
1 + (1 −uθ)(1 −vθ)
i1/θ
(0, 1]
11
max
h
uθvθ −2(1 −uθ)(1 −vθ)
i1/θ
, 0

(0, 1/2]
12

1 +
h
(u−1 −1)θ + (v−1 −1)θi1/θ−1
[1, ∞)
13
exp

1 −
h
(1 −ln u)θ + (1 −ln v)θ −1
i1/θ
(0, ∞)
14

1 +
h
(u−1/θ −1)θ + (v−1/θ −1)θi1/θ−θ
[1, ∞)
15
max
n
1 −
h
(1 −u1/θ)θ + (1 −v1/θ)θi1/θoθ
, 0

[1, ∞)
16
1
2

S +
√
S2 + 4 θ

[0, ∞)
,→S = u + v −1 −θ

1
u + 1
v −1

21
1 −

1 −

max(S(u) + S(v) −1, 0)
	θ 1
θ
[1, ∞)
,→S(u) =
h
1 −(1 −u)θi1/θ
Table 2.1. Copulas implemented in the VaR quantlib.
distribution function S(x) =
1
T
PT
t=1 1(s(t)
1
≤x1, . . . , s(t)
n
≤xn) as close as
possible in the mean square sense. The function 1(A) is the indicator function
of the event A. In order to solve the least square problem on a computer, a
discretization of the support of F (C)
θ
is needed, for which the sample set s(t)

2.2
Computing Value-at-Risk with Copulas
43
seems to be well suited. The copula parameter estimators are therefore the
solution of the following minimization problem:
min
T
X
t=1

F (c)
θ (s(t)) −S(s(t)) + 1
2T
2
subject to θ ∈DC .
using the Newton method on the first derivative (method = 1). The addition of
1
2T avoids problems that result from the 1
T jumps at the sample points. While
this method is inherently numerically stable, it will produce unsatisfactory
results when applied to risk management problems, because the minimization
will fit the copula best where there are the most datapoints, and not necessarily
at the extreme ends of the distribution. While this can be somewhat rectified
by weighting schemes, the maximum likelihood method does this directly.
Maximum Likelihood
The likelihood function of a probability density func-
tion f (C)
θ
(x) evaluated for a time series s is given by l(θ) = QT
t=1 f (C)
θ
(st).
The maximum likelihood method states that the copula parameters at which l
reaches its maximum are good estimators of the “real” copula parameters. In-
stead of the likelihood function, it is customary to maximize the log-likelihood
function
max
T
X
t=1
log

f (C)
θ
(x(t))

s.t. θ ∈DC .
Maximization can be performed on the copula function itself by the Newton
method on the first derivative (method=2) or by an interval search (method=3).
The true maximum likelihood method is implemented in method=4 using an
interval search.
Depending on the given copula it may not be possible to
maximize the likelihood function (i.e. if f (C)
θ
(s(t))) = 0 for some t and all θ. In
this case the least square fit may be used as a fallback.
2.2.4
Generating Scenarios - Monte Carlo Value-at-Risk
Assume now that the copula C has been selected. For risk management pur-
poses, we are interested in the Value-at-Risk of a position. While analytical
methods for the computation of the Value-at-Risk exist for the multivariate
normal distribution (i.e.
for the Gaussian copula), we will in general have
to use numerical simulations for the computation of the VaR. To that end,
we need to generate pairs of random variables (X1, X2) ∼F (C), which form

44
2
Applications of Copulas for the Calculation of Value-at-Risk
scenarios of possible changes of the risk factor. The Monte Carlo method gen-
erates a number N of such scenarios, and evaluates the present value change of
a portfolio under each scenario. The sample α−quantile is then the one period
Value-at-Risk with confidence α.
Our first task is to generate pairs (u, v) of observations of U(0, 1) distributed
random variables U and V whose joint distribution function is C(u, v). To
reach this goal we use the method of conditional distributions. Let cu denote
the conditional distribution function for the random variable V at a given value
u of U,
cu(v)
def
= P(V ≤v, U = u) .
(2.15)
From (2.6) we have
cu(v) = lim
∆u→0
C(u + ∆u, v) −C(u, v)
∆u
= ∂
∂uC(u, v) = Cu(v) ,
(2.16)
where Cu is the partial derivative of the copula. From Theorem 2.4 we know
that cu(v) is nondecreasing and exists for almost all v ∈[0, 1].
For the sake of simplicity, we assume from now on that cu is strictly increasing
and exists for all v ∈[0, 1]. If these conditions are not fulfilled, one has to
replace the term “inverse” in the remaining part of this section by “quasi-
inverse”, see Nelsen (1999).
With result (2.16) at hand we can now use the method of variable transforma-
tion to generate the desired pair (u, v) of pseudo random numbers (PRN). The
algorithm consists of the following two steps:
• Generate two independent uniform PRNs u, w ∈[0, 1]. u is already the
first number we are looking for.
• Compute the inverse function of cu. In general, it will depend on the
parameters of the copula and on u, which can be seen, in this context,
as an additional parameter of cu. Set v = c−1
u (w) to obtain the second
PRN.
It may happen that the inverse function cannot be calculated analytically. In
this case one has to use a numerical algorithm to determine v. This situation
occurs for example when Gumbel-Hougaard copulas are used.

2.3
Examples
45
v = VaRcopula(uv,theta,-1,copula)
returns inverse v = c−1
u
such that res = cu(u, v) for copula copula
with parameter θ = theta. uv is a n × 2 vector of coordinates,
where the copula is calculated.
Finally we determine x1 = Φ−1
1 (u) and x2 = Φ−1
2 (v) to obtain one pair (x1, x2)
of random variables with the desired copula dependence structure. For a Monte
Carlo simulation, this procedure is performed N times to yield a sample X =
(x(1), . . . , x(N)).
X = VaRsimcopula(N, sigma 1, sigma 2, theta, copula)
returns a sample of size N for the copula copula with parameter
θ = theta and normal distributions with standard deviations
σ1 = sigma 1, σ2 = sigma 2.
If we assume a linear position a with holdings a1, . . . , an in each of the risk
factors, the change in portfolio value is approximately Pn
i=1 ai · xi. Using a
first order approximation, this yields a sample Value-at-Risk with confidence
level α.
VaR = VaRestMCcopula(history,a,copula,opt)
fits the copula copula to the history history and returns the
N-sample Monte Carlo Value-at-Risk with confidence level α =
alpha for position a. N and alpha are contained in list opt.
2.3
Examples
In this section we show possible applications for the Gumbel-Hougaard copula,
i.e. for copula = 4. First we try to visualize C4(u, v) in Figure 2.1.
XFGaccvar1.xpl

46
2
Applications of Copulas for the Calculation of Value-at-Risk
0.2
0.5
0.8
0.2
0.5
0.8
0.2
0.5
0.8
(0.0,0.0,0.0)
(1.0,0.0,0.0)
(0.0,1.0,0.0)
 
(0.0,0.0,1.0)
 
 
 
u
v
C(u,v)
Figure 2.1. Plot of C4(u, v) for θ = 3
In the next Figure 2.2 we show an example of copula sampling for fixed pa-
rameters σ1 = 1, σ2 = 1, θ = 3 for copulas numbered 4, 5, 6, and 12, see Table
2.1.
XFGaccvar2.xpl
In order to investigate the connection between the Gaussian and Copula based
dependency structure we plot θ against correlation ρ in Figure 2.3. We assume
that tmin and tmax hold the minimum respectively maximum possible θ val-
ues. Those can also be obtained by tmin=VaRcopula(0,0,0,8,copula) and
tmax=VaRcopula(0,0,0,9,copula). Care has to be taken that the values are
finite, so we have set the maximum absolute θ bound to 10.
XFGaccvar3.xpl

2.4
Results
47
Copula4
-4
-2
0
2
u
-2
0
2
v
Copula6
-3
-2
-1
0
1
2
3
u
-2
0
2
v
Copula5
-2
0
2
u
-2
0
2
v
Copula12
-3
-2
-1
0
1
2
u
-3
-2
-1
0
1
2
3
v
Figure 2.2. 10000-sample output for σ1 = 1, σ2 = 1, θ = 3
2.4
Results
To judge the effectiveness of a Value-at-Risk model, it is common to use back-
testing. A simple approach is to compare the predicted and empirical number
of outliers, where the actual loss exceeds the VaR. We implement this test in
a two risk factor model using real life time series, the FX rates USD/EUR
and GBP/EUR, respectively their DEM counterparts before the introduction
of the Euro. Our backtesting investigation is based on a time series ranging
from 2 Jan. 1991 until 9 Mar. 2000 and simple linear portfolios i = 1, . . . , 4:
Value(ai, t)[EUR] = ai,1 × USDt −ai,2 × GBPt .
(2.17)

48
2
Applications of Copulas for the Calculation of Value-at-Risk
2
4
6
8
10
theta
0
0.5
1
Correlation
Figure 2.3. Plot of θ against correlation ρ for C4.
The Value-at-Risk is computed with confidence level 1−αi (α1 = 0.1, α2 = 0.05,
and α3 = 0.01) based on a time series for the statistical estimators of length
T = 250 business days. The actual next day value change of the portfolio is
compared to the VaR estimate. If the portfolio loss exceeds the VaR estimate,
an outlier has occurred. This procedure is repeated for each day in the time
series.
The prediction error as the absolute difference of the relative number of out-
liers ˆα to the predicted number α is averaged over different portfolios and con-
fidence levels. The average over the portfolios (a1 = (−3, −2) a2 = (+3, −2)
a3 = (−3, +2) a4 = (+3, +2)) uses equal weights, while the average over the
confidence levels i emphasizes the tails by a weighting scheme wi (w1 = 1,
w2 = 5, w3 = 10). Based on the result, an overall error and a relative ranking
of the different methods is obtained (see Table 2.2).
As benchmark methods for Value-at-Risk we use the variance-covariance (vcv)
method and historical simulation (his), for details see Deutsch and Eller (1999).
The variance covariance method is an analytical method which uses a multi-
variate normal distribution. The historical simulation method not only includes

2.4
Results
49
the empirical copula, but also empirical marginal distributions. For the cop-
ula VaR methods, the margins are assumed to be normal, the only difference
between the copula VaR’s is due to different dependence structures (see Table
2.1). Mainly as a consequence of non-normal margins, the historical simulation
has the best backtest results. However, even assuming normal margins, certain
copulas (5, 12–14) give better backtest results than the traditional variance-
covariance method.
Copula as in Table 2.1
α= a= his vcv
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
21
.10 a1 .103 .084 .111 .074 .100 .086 .080 .086 .129 .101 .128 .129 .249 .090 .087 .084 .073 .104 .080
.05 a1 .053 .045 .066 .037 .059 .041 .044 .040 .079 .062 .076 .079 .171 .052 .051 .046 .038 .061 .041
.01 a1 .015 .019 .027 .013 .027 .017 .020 .016 .032 .027 .033 .034 .075 .020 .022 .018 .015 .027 .018
.10 a2 .092 .078 .066 .064 .057 .076 .086 .062 .031 .049 .031 .031 .011 .086 .080 .092 .085 .065 .070
.05 a2 .052 .044 .045 .023 .033 .041 .049 .031 .012 .024 .012 .013 .003 .051 .046 .054 .049 .039 .032
.01 a2 .010 .011 .016 .002 .007 .008 .009 .006 .002 .002 .002 .002 .001 .015 .010 .018 .025 .011 .005
.10 a3 .099 .086 .126 .086 .064 .088 .096 .073 .032 .054 .033 .031 .016 .094 .086 .105 .133 .070 .086
.05 a3 .045 .048 .093 .047 .032 .052 .050 .040 .017 .026 .017 .016 .009 .049 .047 .058 .101 .034 .050
.01 a3 .009 .018 .069 .018 .012 .018 .016 .012 .007 .009 .006 .006 .002 .018 .015 .018 .073 .013 .020
.10 a4 .103 .090 .174 .147 .094 .095 .086 .103 .127 .094 .129 .127 .257 .085 .085 .085 .136 .088 .111
.05 a4 .052 .058 .139 .131 .056 .060 .058 .071 .084 .068 .084 .085 .228 .053 .054 .051 .114 .053 .098
.01 a4 .011 .020 .098 .108 .017 .025 .025 .035 .042 .056 .041 .042 .176 .016 .017 .016 .087 .015 .071
.10 Avg .014 .062 .145 .123 .085 .055 .052 .082 .193 .104 .194 .194 .478 .045 .061 .045 .110 .082 .075
.05 Avg .011 .021 .154 .124 .051 .030 .016 .060 .134 .080 .132 .136 .387 .006 .012 .017 .127 .041 .075
.01 Avg .007 .029 .169 .117 .028 .031 .032 .036 .065 .071 .065 .067 .249 .029 .025 .029 .160 .026 .083
Avg Avg .009 .028 .163 .120 .039 .032 .028 .047 .095 .076 .094 .096 .306 .022 .023 .026 .147 .034 .080
Rank
1
6
18
16
9
7
5
10
14
11
13
15
19
2
3
4
17
8
12
Table 2.2. Relative number of backtest outliers ˆα for the VaR with
confidence 1 −α, weighted average error |ˆα −α| and error ranking.
XFGaccvar4.xpl
Bibliography
H.-P. Deutsch, R. Eller (1999). Derivatives and Internal Models. Macmillan
Press.
T. P. Hutchinson, C. D. Lai (1990). Continuous Bivariate Distributions, Em-
phasising Applications. Rumsby Scientific Publishing, Adelaide.
P. Embrechts, A. McNeil, D. Straumann (1999).Correlation: Pitfalls and Al-
ternatives. RISK, May, pages 69-71.
P. Embrechts, A. McNeil, D. Straumann (1999).Correlation and Dependence
in Risk Management: Properties and Pitfalls. Preprint ETH Z¨urich.

50
2
Applications of Copulas for the Calculation of Value-at-Risk
R. B. Nelsen (1999). An Introduction to Copulas. Springer, New York.
A. Sklar (1959). Fonctions de r´epartition `a n dimensions et leurs marges. Publ.
Inst. Statist. Univ. Paris 8, pages 229-231.
A. Sklar (1996). Random Variables, Distribution Functions, and Copulas – a
Personal Look Backward and Forward published in Distributions with
Fixed Marginals and Related Topics, edited by L. R¨uschendorf, B.
Schweizer, and M.D. Taylor, Institute of Mathematical Statistics, Hay-
ward, CA, pages 1-14.

3 Quantification of Spread Risk by
Means of Historical Simulation
Christoph Frisch and Germar Kn¨ochlein
3.1
Introduction
Modeling spread risk for interest rate products, i.e., changes of the yield differ-
ence between a yield curve characterizing a class of equally risky assets and a
riskless benchmark curve, is a challenge for any financial institution seeking to
estimate the amount of economic capital utilized by trading and treasury activ-
ities. With the help of standard tools this contribution investigates some of the
characteristic features of yield spread time series available from commercial
data providers. From the properties of these time series it becomes obvious
that the application of the parametric variance-covariance-approach for esti-
mating idiosyncratic interest rate risk should be called into question. Instead
we apply the non-parametric technique of historical simulation to synthetic
zero-bonds of different riskiness, in order to quantify general market risk and
spread risk of the bond. The quality of value-at-risk predictions is checked by a
backtesting procedure based on a mark-to-model profit/loss calculation for the
zero-bond market values. From the backtesting results we derive conclusions
for the implementation of internal risk models within financial institutions.
3.2
Risk Categories – a Definition of Terms
For the analysis of obligor-specific and market-sector-specific influence on bond
price risk we make use of the following subdivision of “price risk”, Gaumert
(1999), Bundesaufsichtsamt f¨ur das Kreditwesen (2001).

52
3
Quantification of Spread Risk by Means of Historical Simulation
1. General market risk: This risk category comprises price changes of a
financial instrument, which are caused by changes of the general mar-
ket situation. General market conditions in the interest rate sector are
characterized by the shape and the moves of benchmark yield curves,
which are usually constructed from several benchmark instruments. The
benchmark instruments are chosen in such a way so that they allow for a
representative view on present market conditions in a particular market
sector.
2. Residual risk: Residual risk characterizes the fact that the actual price
of a given financial instrument can change in a way different from the
changes of the market benchmark (however, abrupt changes which are
caused by events in the sphere of the obligor are excluded from this risk
category). These price changes cannot be accounted for by the volatility
of the market benchmark. Residual risk is contained in the day-to-day
price variation of a given instrument relative to the market benchmark
and, thus, can be observed continuously in time. Residual risk is also
called idiosyncratic risk.
3. Event risk: Abrupt price changes of a given financial instrument relative
to the benchmark, which significantly exceed the continuously observable
price changes due to the latter two risk categories, are called event risk.
Such price jumps are usually caused by events in the sphere of the obligor.
They are observed infrequently and irregularly.
Residual risk and event risk form the two components of so-called specific price
risk or specific risk — a term used in documents on banking regulation, Bank for
International Settlements (1998a), Bank for International Settlements (1998b)
— and characterize the contribution of the individual risk of a given financial
instrument to its overall risk.
The distinction between general market risk and residual risk is not unique but
depends on the choice of the benchmark curve, which is used in the analysis
of general market risk: The market for interest rate products in a given cur-
rency has a substructure (market-sectors), which is reflected by product-specific
(swaps, bonds, etc.), industry-specific (bank, financial institution, retail com-
pany, etc.) and rating-specific (AAA, AA, A, BBB, etc.) yield curves. For the
most liquid markets (USD, EUR, JPY), data for these sub-markets is available
from commercial data providers like Bloomberg.
Moreover, there are addi-
tional influencing factors like collateral, financial restrictions etc., which give

3.3
Descriptive Statistics of Yield Spread Time Series
53
rise to further variants of the yield curves mentioned above. Presently, however,
hardly any standardized data on these factors is available from data providers.
The larger the universe of benchmark curves a bank uses for modeling its
interest risk, the smaller is the residual risk.
A bank, which e.g. only uses
product-specific yield curves but neglects the influence of industry- and rating-
specific effects in modelling its general market risk, can expect specific price
risk to be significantly larger than in a bank which includes these influences
in modeling general market risk. The difference is due to the consideration of
product-, industry- and rating-specific spreads over the benchmark curve for
(almost) riskless government bonds. This leads to the question, whether the
risk of a spread change, the spread risk, should be interpreted as part of the
general market risk or as part of the specific risk. The uncertainty is due to
the fact that it is hard to define what a market-sector is. The definition of
benchmark curves for the analysis of general market risk depends, however,
critically on the market sectors identified.
We will not further pursue this question in the following but will instead inves-
tigate some properties of this spread risk and draw conclusions for modeling
spread risk within internal risk models. We restrict ourselves to the continuous
changes of the yield curves and the spreads, respectively, and do not discuss
event risk. In this contribution different methods for the quantification of the
risk of a fictive USD zero bond are analyzed. Our investigation is based on
time series of daily market yields of US treasury bonds and US bonds (banks
and industry) of different credit quality (rating) and time to maturity.
3.3
Descriptive Statistics of Yield Spread Time
Series
Before we start modeling the interest rate and spread risk we will investigate
some of the descriptive statistics of the spread time series. Our investigations
are based on commercially available yield curve histories.
The Bloomberg
dataset we use in this investigation consists of daily yield data for US trea-
sury bonds as well as for bonds issued by banks and financial institutions with
ratings AAA, AA+/AA, A+, A, A−(we use the Standard & Poor‘s naming
convention) and for corporate/industry bonds with ratings AAA, AA, AA−,
A+, A, A−, BBB+, BBB, BBB−, BB+, BB, BB−, B+, B, B−. The data we
use for the industry sector covers the time interval from March 09 1992 to June
08 2000 and corresponds to 2147 observations. The data for banks/financial

54
3
Quantification of Spread Risk by Means of Historical Simulation
institutions covers the interval from March 09 1992 to September 14 1999 and
corresponds to 1955 observations. We use yields for 3 and 6 month (3M, 6M)
as well as 1, 2, 3, 4, 5, 7, and 10 year maturities (1Y, 2Y, 3Y, 4Y, 5Y, 7Y, 10Y).
Each yield curve is based on information on the prices of a set of representative
bonds with different maturities. The yield curve, of course, depends on the
choice of bonds. Yields are option-adjusted but not corrected for coupon pay-
ments. The yields for the chosen maturities are constructed by Bloomberg’s
interpolation algorithm for yield curves. We use the USD treasury curve as a
benchmark for riskless rates and calculate yield spreads relative to the bench-
mark curve for the different rating categories and the two industries. We correct
the data history for obvious flaws using complementary information from other
data sources. Some parts of our analysis in this section can be compared with
the results given in Kiesel, Perraudin and Taylor (1999).
3.3.1
Data Analysis with XploRe
We store the time series of the different yield curves in individual files. The file
names, the corresponding industries and ratings and the names of the matrices
used in the XploRe code are listed in Table 3.2. Each file contains data for
the maturities 3M to 10Y in columns 4 to 12. XploRe creates matrices from
the data listed in column 4 of Table 3.2 and produces summary statistics for
the different yield curves. As example files the data sets for US treasury and
industry bonds with rating AAA are provided. The output of the summarize
command for the INAAA curve is given in Table 3.1.
Contents of summ
Minimum
Maximum
Mean
Median
Std.Error
----------------------------------------------------------------
3M
3.13
6.93
5.0952
5.44
0.95896
6M
3.28
7.16
5.2646
5.58
0.98476
1Y
3.59
7.79
5.5148
5.75
0.95457
2Y
4.03
8.05
5.8175
5.95
0.86897
3Y
4.4
8.14
6.0431
6.1
0.79523
4Y
4.65
8.21
6.2141
6.23
0.74613
5Y
4.61
8.26
6.3466
6.36
0.72282
7Y
4.75
8.3
6.5246
6.52
0.69877
10Y
4.87
8.36
6.6962
6.7
0.69854
Table
3.1.
Output
of
summarize
for
the
INAAA
curve.
XFGsummary.xpl
The long term means are of particular interest. Therefore, we summarize them
in Table 3.3. In order to get an impression of the development of the treasury

3.3
Descriptive Statistics of Yield Spread Time Series
55
Industry
Rating
File Name
Matrix Name
Government
riskless
USTF
USTF
Industry
AAA
INAAA
INAAA
Industry
AA
INAA2.DAT
INAA2
Industry
AA-
INAA3.DAT
INAA3
Industry
A+
INA1.DAT
INA1
Industry
A
INA2.DAT
INA2
Industry
A-
INA3.DAT
INA3
Industry
BBB+
INBBB1.DAT
INBBB1
Industry
BBB
INBBB2.DAT
INBBB2
Industry
BBB-
INBBB3.DAT
INBBB3
Industry
BB+
INBB1.DAT
INBB1
Industry
BB
INBB2.DAT
INBB2
Industry
BB-
INBB3.DAT
INBB3
Industry
B+
INB1.DAT
INB1
Industry
B
INB2.DAT
INB2
Industry
B-
INB3.DAT
INB3
Bank
AAA
BNAAA.DAT
BNAAA
Bank
AA+/AA
BNAA12.DAT
BNAA12
Bank
A+
BNA1.DAT
BNA1
Bank
A
BNA2.DAT
BNA2
Bank
A-
BNA3.DAT
BNA3
Table 3.2. Data variables
yields in time, we plot the time series for the USTF 3M, 1Y, 2Y, 5Y, and 10Y
yields.
The results are displayed in Figure 3.1,
XFGtreasury.xpl.
The
averaged yields within the observation period are displayed in Figure 3.2 for
USTF, INAAA, INBBB2, INBB2 and INB2,
XFGyields.xpl.
In the next step we calculate spreads relative to the treasury curve by sub-
tracting the treasury curve from the rating-specific yield curves and store them
to variables SINAAA, SINAA2, etc.
For illustrative purposes we display time
series of the 1Y, 2Y, 3Y, 5Y, 7Y, and 10Y spreads for the curves INAAA, INA2,
INBBB2, INBB2, INB2 in Figure 3.3,
XFGseries.xpl.
We run the summary statistics to obtain information on the mean spreads.
Our results, which can also be obtained with the mean command, are collected
in Table 3.4,
XFGmeans.xpl.

56
3
Quantification of Spread Risk by Means of Historical Simulation
Curve
3M
6M
1Y
2Y
3Y
4Y
5Y
7Y
10Y
USTF
4.73
4.92
5.16
5.50
5.71
5.89
6.00
6.19
6.33
INAAA
5.10
5.26
5.51
5.82
6.04
6.21
6.35
6.52
6.70
INAA2
5.19
5.37
5.59
5.87
6.08
6.26
6.39
6.59
6.76
INAA3
5.25
-
5.64
5.92
6.13
6.30
6.43
6.63
6.81
INA1
5.32
5.50
5.71
5.99
6.20
6.38
6.51
6.73
6.90
INA2
5.37
5.55
5.76
6.03
6.27
6.47
6.61
6.83
7.00
INA3
-
-
5.84
6.12
6.34
6.54
6.69
6.91
7.09
INBBB1
5.54
5.73
5.94
6.21
6.44
6.63
6.78
7.02
7.19
INBBB2
5.65
5.83
6.03
6.31
6.54
6.72
6.86
7.10
7.27
INBBB3
5.83
5.98
6.19
6.45
6.69
6.88
7.03
7.29
7.52
INBB1
6.33
6.48
6.67
6.92
7.13
7.29
7.44
7.71
7.97
INBB2
6.56
6.74
6.95
7.24
7.50
7.74
7.97
8.34
8.69
INBB3
6.98
7.17
7.41
7.71
7.99
8.23
8.46
8.79
9.06
INB1
7.32
7.53
7.79
8.09
8.35
8.61
8.82
9.13
9.39
INB2
7.80
7.96
8.21
8.54
8.83
9.12
9.37
9.68
9.96
INB3
8.47
8.69
8.97
9.33
9.60
9.89
10.13
10.45
10.74
BNAAA
5.05
5.22
5.45
5.76
5.99
6.20
6.36
6.60
6.79
BNAA12
5.14
5.30
5.52
5.83
6.06
6.27
6.45
6.68
6.87
BNA1
5.22
5.41
5.63
5.94
6.19
6.39
6.55
6.80
7.00
BNA2
5.28
5.47
5.68
5.99
6.24
6.45
6.61
6.88
7.07
BNA3
5.36
5.54
5.76
6.07
6.32
6.52
6.68
6.94
7.13
Table 3.3. Long term mean for different USD yield curves
Now we calculate the 1-day spread changes from the observed yields and store
them to variables DASIN01AAA, etc. We run the descriptive routine to cal-
culate the first four moments of the distribution of absolute spread changes.
Volatility as well as skewness and kurtosis for selected curves are displayed in
Tables 3.5, 3.6 and 3.7.
XFGchange.xpl
For the variable DASIN01AAA[,12] (the 10 year AAA spreads) we demonstrate
the output of the descriptive command in Table 3.8.
Finally we calculate 1-day relative spread changes and run the descriptive
command. The results for the estimates of volatility, skewness and kurtosis are
summarized in Tables 3.9, 3.10 and 3.11.
XFGrelchange.xpl

3.3
Descriptive Statistics of Yield Spread Time Series
57
US Treasury Yields (3M, 1Y, 2Y, 5Y, 10Y)
0
500
1000
1500
2000
Day
3
4
5
6
7
8
Yield in %
Figure 3.1. US Treasury Yields.
XFGtreasury.xpl
Yields for Different Risk Levels
5
10
Time to Maturity in Years
5
6
7
8
Average Yield in %
Figure 3.2. Averaged Yields.
XFGyields.xpl

58
3
Quantification of Spread Risk by Means of Historical Simulation
1Y-Spread (AAA, A2, BBB2, BB2, B2)
0
5
10
15
20
Day*E2
0
1
2
3
4
5
Spread in %
2Y-Spread (AAA, A2, BBB2, BB2, B2)
0
5
10
15
20
Day*E2
0
1
2
3
4
Spread in %
3Y-Spread (AAA, A2, BBB2, BB2, B2)
0
5
10
15
20
Day*E2
0
1
2
3
4
5
Spread in %
5Y-Spread (AAA, A2, BBB2, BB2, B2)
0
5
10
15
20
Day*E2
0
1
2
3
4
5
Spread in %
7Y-Spread (AAA, A2, BBB2, BB2, B2)
0
5
10
15
20
Day*E2
0
1
2
3
4
5
Spread in %
10Y-Spread (AAA, A2, BBB2, BB2, B2)
0
5
10
15
20
Day*E2
0
1
2
3
4
5
6
Spread in %
Figure 3.3. Credit Spreads.
XFGseries.xpl
3.3.2
Discussion of Results
Time Development of Yields and Spreads: The time development of US trea-
sury yields displayed in Figure 3.1 indicates that the yield curve was steeper
at the beginning of the observation period and flattened in the second half.
However, an inverse shape of the yield curve occurred hardly ever. The long
term average of the US treasury yield curve, the lowest curve in Figure 3.2,
also has an upward sloping shape.
The time development of the spreads over US treasury yields displayed in Fig-
ure 3.3 is different for different credit qualities. While there is a large variation
of spreads for the speculative grades, the variation in the investment grade sec-
tor is much smaller. A remarkable feature is the significant spread increase for
all credit qualities in the last quarter of the observation period which coincides
with the emerging market crises in the late 90s. The term structure of the long
term averages of the rating-specific yield curves is also normal. The spreads
over the benchmark curve increase with decreasing credit quality.
Mean Spread: The term structure of the long term averages of the rating-
specific yield curves, which is displayed in Figure 3.3, is normal (see also Ta-
ble 3.4). The spreads over the benchmark curve increase with decreasing credit
quality. For long maturities the mean spreads are larger than for intermediate
maturities as expected. However, for short maturities the mean spreads are

3.3
Descriptive Statistics of Yield Spread Time Series
59
Curve
3M
6M
1Y
2Y
3Y
4Y
5Y
7Y
10Y
INAAA
36
35
35
31
33
31
35
33
37
INAA2
45
45
43
37
37
36
40
39
44
INAA3
52
-
48
42
42
40
44
44
49
INA1
58
58
55
49
49
49
52
53
57
INA2
63
63
60
53
56
57
62
64
68
INA3
-
-
68
62
63
64
69
72
76
INBBB1
81
82
78
71
72
74
79
83
86
INBBB2
91
91
87
80
82
82
87
90
94
INBBB3
110
106
103
95
98
98
104
110
119
INBB1
160
156
151
142
141
140
145
151
164
INBB2
183
182
179
173
179
185
197
215
236
INBB3
225
225
225
221
228
233
247
259
273
INB1
259
261
263
259
264
271
282
294
306
INB2
306
304
305
304
311
322
336
348
363
INB3
373
377
380
382
389
400
413
425
441
BNAAA
41
39
38
33
35
35
41
43
47
BNAA12
50
47
45
40
42
42
49
52
56
BNA1
57
59
57
52
54
54
59
64
68
BNA2
64
65
62
57
59
60
65
71
75
BNA3
72
72
70
65
67
67
72
76
81
Table 3.4. Mean spread in basis points p.a.
larger compared with intermediate maturities.
Volatility: The results for the volatility for absolute 1-day spread changes in
basis points p.a. are listed in Table 3.5. From short to intermediate maturities
the volatilities decrease. For long maturities a slight volatility increase can be
observed compared to intermediate maturities. For equal maturities volatility
is constant over the investment grade ratings, while for worse credit qualities a
significant increase in absolute volatility can be observed. Volatility for relative
spread changes is much larger for short maturities than for intermediate and
long maturities. As in the case of absolute spread changes, a slight volatility
increase exists for the transition from intermediate to long maturities. Since
absolute spreads increase more strongly with decreasing credit quality than
absolute spread volatility, relative spread volatility decreases with decreasing
credit quality (see Table 3.9).
Skewness: The results for absolute 1-day changes (see Table 3.6) are all close to
zero, which indicates that the distribution of changes is almost symmetric. The
corresponding distribution of relative changes should have a positive skewness,

60
3
Quantification of Spread Risk by Means of Historical Simulation
Curve
3M
6M
1Y
2Y
3Y
4Y
5Y
7Y
10Y
INAAA
4.1
3.5
3.3
2.3
2.4
2.2
2.1
2.2
2.5
INAA2
4.0
3.5
3.3
2.3
2.4
2.2
2.2
2.2
2.5
INAA3
4.0
-
3.3
2.2
2.3
2.2
2.2
2.2
2.5
INA1
4.0
3.7
3.3
2.3
2.4
2.2
2.2
2.2
2.6
INA2
4.1
3.7
3.3
2.4
2.4
2.1
2.2
2.3
2.5
INA3
-
-
3.4
2.4
2.4
2.2
2.2
2.3
2.6
INBBB1
4.2
3.6
3.2
2.3
2.3
2.2
2.1
2.3
2.6
INBBB2
4.0
3.5
3.4
2.3
2.4
2.1
2.2
2.3
2.6
INBBB3
4.2
3.6
3.5
2.4
2.5
2.2
2.3
2.5
2.9
INBB1
4.8
4.4
4.1
3.3
3.3
3.1
3.1
3.9
3.4
INBB2
4.9
4.6
4.5
3.8
3.8
3.8
3.7
4.3
4.0
INBB3
5.5
5.1
4.9
4.3
4.4
4.2
4.1
4.7
4.3
INB1
6.0
5.2
4.9
4.5
4.5
4.4
4.4
4.9
4.6
INB2
5.6
5.2
5.2
4.8
4.9
4.8
4.8
5.3
4.9
INB3
5.8
6.1
6.4
5.1
5.2
5.1
5.1
5.7
5.3
BNAAA
3.9
3.5
3.3
2.5
2.5
2.3
2.2
2.3
2.6
BNAA12
5.4
3.6
3.3
2.4
2.3
2.2
2.1
2.3
2.6
BNA1
4.1
3.7
3.2
2.1
2.2
2.1
2.0
2.2
2.6
BNA2
3.8
3.5
3.1
2.3
2.2
2.0
2.1
2.2
2.5
BNA3
3.8
3.5
3.2
2.2
2.2
2.1
2.1
2.2
2.5
Table 3.5. volatility for absolute spread changes in basis points p.a.
Curve
3M
6M
1Y
2Y
3Y
4Y
5Y
10Y
INAAA
0.1
0.0
-0.1
0.6
0.5
0.0
-0.5
0.6
INAA2
0.0
-0.2
0.0
0.4
0.5
-0.1
-0.2
0.3
INA2
0.0
-0.3
0.1
0.2
0.4
0.1
-0.1
0.4
INBBB2
0.2
0.0
0.2
1.0
1.1
0.5
0.5
0.9
INBB2
-0.2
-0.5
-0.4
-0.3
0.3
0.5
0.4
-0.3
Table 3.6. Skewness for absolute 1-day spread changes (in σ3).
which is indeed the conclusion from the results in Table 3.10.
Kurtosis: The absolute 1-day changes lead to a kurtosis, which is significantly
larger than 3 (see Table 3.6). Thus, the distribution of absolute changes is
leptokurtic. There is no significant dependence on credit quality or maturity.
The distribution of relative 1-day changes is also leptokurtic (see Table 3.10).
The deviation from normality increases with decreasing credit quality and de-
creasing maturity.

3.3
Descriptive Statistics of Yield Spread Time Series
61
Curve
3M
6M
1Y
2Y
3Y
4Y
5Y
10Y
INAAA
12.7
6.0
8.1
10.1
16.8
9.1
11.2
12.8
INAA2
10.5
6.4
7.8
10.1
15.8
7.8
9.5
10.0
INA2
13.5
8.5
9.2
12.3
18.2
8.2
9.4
9.8
INBBB2
13.7
7.0
9.9
14.5
21.8
10.5
13.9
14.7
INBB2
11.2
13.0
11.0
15.8
12.3
13.2
11.0
11.3
Table 3.7. Kurtosis for absolute spread changes (in σ4).
=========================================================
Variable 10Y
=========================================================
Mean
0.000354147
Std.Error
0.0253712
Variance
0.000643697
Minimum
-0.18
Maximum
0.2
Range
0.38
Lowest cases
Highest cases
1284:
-0.18
1246:
0.14
1572:
-0.14
1283:
0.14
1241:
-0.13
2110:
0.19
1857:
-0.11
1062:
0.19
598:
-0.1
2056:
0.2
Median
0
25% Quartile
-0.01
75% Quartile
0.01
Skewness
0.609321
Kurtosis
9.83974
Observations
2146
Distinct observations
75
Total number of {-Inf,Inf,NaN}
0
=========================================================
Table 3.8. Output of descriptive for the 10 years AAA spread.
We visualize symmetry and leptokursis of the distribution of absolute spread
changes for the INAAA 10Y data in Figure 3.4, where we plot the empirical dis-
tribution of absolute spreads around the mean spread in an averaged shifted
histogram and the normal distribution with the variance estimated from his-
torical data.
XFGdist.xpl

62
3
Quantification of Spread Risk by Means of Historical Simulation
Curve
3M
6M
1Y
2Y
3Y
4Y
5Y
7Y
10Y
INAAA
36.0
19.2
15.5
8.9
8.4
8.0
6.4
7.8
10.4
INAA2
23.5
13.1
11.2
7.2
7.4
6.4
5.8
6.2
7.6
INAA3
13.4
-
9.0
5.8
6.2
5.3
5.0
5.8
6.4
INA1
13.9
9.2
7.7
5.7
5.6
4.7
4.5
4.6
5.7
INA2
11.5
8.1
7.1
5.1
4.9
4.3
4.0
4.0
4.5
INA3
-
-
6.4
4.6
4.3
3.8
3.5
3.5
4.1
INBBB1
8.1
6.0
5.4
3.9
3.7
3.3
3.0
3.2
3.8
INBBB2
7.0
5.3
5.0
3.3
3.3
2.9
2.8
2.9
3.3
INBBB3
5.7
4.7
4.4
3.2
3.0
2.7
2.5
2.6
2.9
INBB1
4.3
3.8
3.4
2.5
2.4
2.2
2.1
2.5
2.2
INBB2
3.7
3.3
3.0
2.2
2.1
2.0
1.8
2.0
1.7
INBB3
3.2
2.8
2.5
2.0
1.9
1.8
1.6
1.8
1.5
INB1
3.0
2.4
2.1
1.7
1.7
1.6
1.5
1.6
1.5
INB2
2.3
2.1
1.9
1.6
1.6
1.5
1.4
1.5
1.3
INB3
1.8
2.2
2.3
1.3
1.3
1.2
1.2
1.3
1.1
BNAAA
37.0
36.6
16.9
9.8
9.0
8.2
6.1
5.9
6.5
BNAA12
22.8
9.7
8.3
7.0
6.3
5.8
4.6
4.8
5.5
BNA1
36.6
10.1
7.9
5.6
4.8
4.4
3.8
3.9
4.4
BNA2
17.8
8.0
6.6
4.5
4.1
3.6
3.4
3.3
3.7
BNA3
9.9
6.9
5.6
3.7
3.6
3.3
3.1
3.1
3.4
Table 3.9. Volatility for relative spread changes in %
Curve
3M
6M
1Y
2Y
3Y
4Y
5Y
10Y
INAAA
2.3
4.6
4.3
2.2
2.3
2.1
0.6
4.6
INAA2
5.4
2.6
3.7
1.6
2.0
0.6
0.8
1.8
INA2
7.6
1.5
1.2
0.9
1.6
0.8
0.9
0.8
INBBB2
5.5
0.7
0.8
0.8
1.4
0.8
0.7
0.8
INBB2
0.8
0.4
0.6
0.3
0.4
0.5
0.3
-0.2
Table 3.10. Skewness for relative spread changes (in σ3).
We note that by construction the area below both curves is normalized to
one. We calculate the 1%, 10%, 90% and 99% quantiles of the spread distribu-
tion with the quantile command. Those quantiles are popular in market risk
management. For the data used to generate Figure 3.4 the results are 0.30%,
0.35%, 0.40%, and 0.45%, respectively.
The corresponding quantiles of the
plotted normal distribution are 0.31%, 0.34%, 0.41%, 0.43%. The differences
are less obvious than the difference in the shape of the distributions. However,
in a portfolio with different financial instruments, which is exposed to different

3.4
Historical Simulation and Value at Risk
63
Curve
3M
6M
1Y
2Y
3Y
4Y
5Y
10Y
INAAA
200.7
54.1
60.1
27.8
28.3
33.9
16.8
69.3
INAA2
185.3
29.5
60.5
22.1
27.4
11.0
17.5
23.0
INA2
131.1
22.1
18.0
13.9
26.5
16.4
18.5
13.9
INBBB2
107.1
13.9
16.9
12.0
20.0
14.0
16.6
16.7
INBB2
16.3
11.9
12.9
12.4
11.0
10.1
10.2
12.0
Table 3.11. Kurtosis for relative spread changes (in σ4).
Historical vs. Normal Distribution
0.2
0.3
0.4
0.5
Absolute Spread Change
0
10
20
30
Density Function
Figure 3.4. Historical distribution and estimated normal distribution.
XFGdist.xpl
risk factors with different correlations, the difference in the shape of the distri-
bution can play an important role. That is why a simple variance-covariance
approach, J.P. Morgan (1996) and Kiesel et al. (1999), seems not adequate to
capture spread risk.
3.4
Historical Simulation and Value at Risk
We investigate the behavior of a fictive zero-bond of a given credit quality
with principal 1 USD, which matures after T years. In all simulations t = 0
denotes the beginning and t = T the end of the lifetime of the zero-bond. The
starting point of the simulation is denoted by t0, the end by t1. The observation

64
3
Quantification of Spread Risk by Means of Historical Simulation
period, i.e., the time window investigated, consists of N ≥1 trading days and
the holding period of h ≥1 trading days. The confidence level for the VaR is
α ∈[0, 1]. At each point in time 0 ≤t ≤t1 the risky yields Ri(t) (full yield
curve) and the riskless treasury yields Bi(t) (benchmark curve) for any time to
maturity 0 < T1 < · · · < Tn are contained in our data set for 1 ≤i ≤n, where
n is the number of different maturities. The corresponding spreads are defined
by Si(t) = Ri(t) −Bi(t) for 1 ≤i ≤n.
In the following subsections 3.4.1 to 3.4.5 we specify different variants of the
historical simulation method which we use for estimating the distribution of
losses from the zero-bond position. The estimate for the distribution of losses
can then be used to calculate the quantile-based risk measure Value-at-Risk.
The variants differ in the choice of risk factors, i.e., in our case the compo-
nents of the historical yield time series. In Section 3.6 we describe how the
VaR estimation is carried out with XploRe commands provided that the loss
distribution has been estimated by means of one of the methods introduced
and can be used as an input variable.
3.4.1
Risk Factor: Full Yield
1. Basic Historical Simulation:
We consider a historical simulation, where the risk factors are given by the
full yield curve, Ri(t) for i = 1, . . . , n.
The yield R(t, T −t) at time t0 ≤
t ≤t1 for the remaining time to maturity T −t is determined by means of
linear interpolation from the adjacent values Ri(t) = R(t, Ti) and Ri+1(t) =
R(t, Ti+1) with Ti ≤T −t < Ti+1 (for reasons of simplicity we do not consider
remaining times to maturity T −t < T1 and T −t > Tn):
R(t, T −t) = [Ti+1 −(T −t)]Ri(t) + [(T −t) −Ti]Ri+1(t)
Ti+1 −Ti
.
(3.1)
The present value of the bond PV (t) at time t can be obtained by discounting,
PV (t) =
1

1 + R(t, T −t)
T −t ,
t0 ≤t ≤t1.
(3.2)
In the historical simulation the relative risk factor changes
∆(k)
i
(t) = Ri
 t −k/N

−Ri
 t −(k + h)/N

Ri
 t −(k + h)/N

,
0 ≤k ≤N −1,
(3.3)

3.4
Historical Simulation and Value at Risk
65
are calculated for t0 ≤t ≤t1 and each 1 ≤i ≤n. Thus, for each scenario k we
obtain a new fictive yield curve at time t + h, which can be determined from
the observed yields and the risk factor changes,
R(k)
i
(t + h) = Ri(t)

1 + ∆(k)
i
(t)

,
1 ≤i ≤n,
(3.4)
by means of linear interpolation. This procedure implies that the distribution of
risk factor changes is stationary between t−(N −1+h)/N and t. Each scenario
corresponds to a drawing from an identical and independent distribution, which
can be related to an i.i.d. random variable εi(t) with variance one via
∆i(t) = σiεi(t).
(3.5)
This assumption implies homoscedasticity of the volatility of the risk factors,
i.e., a constant volatility level within the observation period. If this were not the
case, different drawings would originate from different underlying distributions.
Consequently, a sequence of historically observed risk factor changes could not
be used for estimating the future loss distribution.
In analogy to (3.1) for time t + h and remaining time to maturity T −t one
obtains
R(k)(t + h, T −t) = [Ti+1 −(T −t)]R(k)
i
(t) + [(T −t) −Ti]R(k)
i+1(t)
Ti+1 −Ti
for the yield. With (3.2) we obtain a new fictive present value at time t + h:
PV (k)(t + h) =
1

1 + R(k)(t + h, T −t)
T −t .
(3.6)
In this equation we neglected the effect of the shortening of the time to maturity
in the transition from t to t + h on the present value. Such an approximation
should be refined for financial instruments whose time to maturity/time to
expiration is of the order of h, which is not relevant for the constellations
investigated in the following.
Now the fictive present value PV (k)(t + h) is compared with the present value
for unchanged yield R(t + h, T −t) = R(t, T −t) for each scenario k (here the
remaining time to maturity is not changed, either).
PV (t + h) =
1

1 + R(t + h, T −t)
	T −t .
(3.7)

66
3
Quantification of Spread Risk by Means of Historical Simulation
The loss occurring is
L(k)(t + h) = PV (t + h) −PV (k)(t + h)
0 ≤k ≤N −1,
(3.8)
i.e., losses in the economic sense are positive while profits are negative. The
VaR is the loss which is not exceeded with a probability α and is estimated as
the [(1 −α)N + 1]-th-largest value in the set
{L(k)(t + h) | 0 ≤k ≤N −1}.
This is the (1 −α)-quantile of the corresponding empirical distribution.
2. Mean Adjustment:
A refined historical simulation includes an adjustment for the average of those
relative changes in the observation period which are used for generating the
scenarios according to (3.3). If for fixed 1 ≤i ≤n the average of relative
changes ∆(k)
i
(t) is different from 0, a trend is projected from the past to the
future in the generation of fictive yields in (3.4). Thus the relative changes are
corrected for the mean by replacing the relative change ∆(k)
i
(t) with ∆(k)
i
(t) −
∆i(t) for 1 ≤i ≤n in (3.4):
∆i(t) = 1
N
N−1
X
k=0
∆(k)
i
(t),
(3.9)
This mean correction is presented in Hull (1998).
3. Volatility Updating:
An important variant of historical simulation uses volatility updating Hull
(1998). At each point in time t the exponentially weighted volatility of rel-
ative historical changes is estimated for t0 ≤t ≤t1 by
σ2
i (t) = (1 −γ)
N−1
X
k=0
γk
∆(k)
i
(t)
	2,
1 ≤i ≤n.
(3.10)
The parameter γ ∈[0, 1] is a decay factor, which must be calibrated to generate
a best fit to empirical data. The recursion formula
σ2
i (t) = (1 −γ)σ2
i (t −1/N) + γ

∆(0)
i (t)
	2,
1 ≤i ≤n,
(3.11)
is valid for t0 ≤t ≤t1. The idea of volatility updating consists in adjusting the
historical risk factor changes to the present volatility level. This is achieved by

3.4
Historical Simulation and Value at Risk
67
a renormalization of the relative risk factor changes from (3.3) with the corre-
sponding estimation of volatility for the observation day and a multiplication
with the estimate for the volatility valid at time t.
Thus, we calculate the
quantity
δ(k)
i
(t) = σi(t) ·
∆(k)
i
(t)
σi(t −(k + h)/N),
0 ≤k ≤N −1.
(3.12)
In a situation, where risk factor volatility is heteroscedastic and, thus, the
process of risk factor changes is not stationary, volatility updating cures this
violation of the assumptions made in basic historical simulation, because the
process of re-scaled risk factor changes ∆i(t)/σi(t)) is stationary. For each k
these renormalized relative changes are used in analogy to (3.4) for the deter-
mination of fictive scenarios:
R(k)
i
(t + h) = Ri(t)

1 + δ(k)
i
(t)
	
,
1 ≤i ≤n,
(3.13)
The other considerations concerning the VaR calculation in historical simula-
tion remain unchanged.
4. Volatility Updating and Mean Adjustment:
Within the volatility updating framework, we can also apply a correction for
the average change according to 3.4.1(2). For this purpose, we calculate the
average
δi(t) = 1
N
N−1
X
k=0
δ(k)
i
(t),
(3.14)
and use the adjusted relative risk factor change δ(k)
i
(t) −δi(t) instead of δ(k)
i
(t)
in (3.13).
3.4.2
Risk Factor: Benchmark
In this subsection the risk factors are relative changes of the benchmark curve
instead of the full yield curve.
This restriction is adequate for quantifying
general market risk, when there is no need to include spread risk. The risk
factors are the yields Bi(t) for i = 1, . . . , n. The yield B(t, T −t) at time t for

68
3
Quantification of Spread Risk by Means of Historical Simulation
remaining time to maturity T −t is calculated similarly to (3.1) from adjacent
values by linear interpolation,
B(t, T −t) = {Ti+1 −(T −t)}Bi(t) + {(T −t) −Ti}Bi+1(t)
Ti+1 −Ti
.
(3.15)
The generation of scenarios and the interpolation of the fictive benchmark curve
is carried out in analogy to the procedure for the full yield curve. We use
∆(k)
i
(t) = Bi
 t −k/N

−Bi
 t −(k + h)/N

Bi
 t −(k + h)/N

,
0 ≤k ≤N −1,
(3.16)
and
B(k)
i
(t + h) = Bi(t)

1 + ∆(k)
i
(t)

,
1 ≤i ≤n.
(3.17)
Linear interpolation yields
B(k)(t + h, T −t) = {Ti+1 −(T −t)}B(k)
i
(t) + {(T −t) −Ti}B(k)
i+1(t)
Ti+1 −Ti
.
In the determination of the fictive full yield we now assume that the spread
remains unchanged within the holding period. Thus, for the k-th scenario we
obtain the representation
R(k)(t + h, T −t) = B(k)(t + h, T −t) + S(t, T −t),
(3.18)
which is used for the calculation of a new fictive present value and the corre-
sponding loss. With this choice of risk factors we can introduce an adjustment
for the average relative changes or/and volatility updating in complete analogy
to the four variants described in the preceding subsection.
3.4.3
Risk Factor: Spread over Benchmark Yield
When we take the view that risk is only caused by spread changes but not
by changes of the benchmark curve, we investigate the behavior of the spread
risk factors Si(t) for i = 1, . . . , n. The spread S(t, T −t) at time t for time to
maturity T −t is again obtained by linear interpolation. We now use
∆(k)
i
(t) = Si
 t −k/N

−Si
 t −(k + h)/N

Si
 t −(k + h)/N

,
0 ≤k ≤N −1,
(3.19)


## Credit Risk Modeling

3.4
Historical Simulation and Value at Risk
69
and
S(k)
i
(t + h) = Si(t)

1 + ∆(k)
i
(t)
	
,
1 ≤i ≤n.
(3.20)
Here, linear interpolation yields
S(k)(t + h, T −t) = {Ti+1 −(T −t)}S(k)
i
(t) + {(T −t) −Ti}S(k)
i+1(t)
Ti+1 −Ti
.
Thus, in the determination of the fictive full yield the benchmark curve is
considered deterministic and the spread stochastic. This constellation is the
opposite of the constellation in the preceding subsection. For the k-th scenario
one obtains
R(k)(t + h, T −t) = B(t, T −t) + S(k)(t + h, T −t).
(3.21)
In this context we can also work with adjustment for average relative spread
changes and volatility updating.
3.4.4
Conservative Approach
In the conservative approach we assume full correlation between risk from the
benchmark curve and risk from the spread changes. In this worst case scenario
we add (ordered) losses, which are calculated as in the two preceding sections
from each scenario. From this loss distribution the VaR is determined.
3.4.5
Simultaneous Simulation
Finally, we consider simultaneous relative changes of the benchmark curve and
the spreads. For this purpose (3.18) and (3.21) are replaced with
R(k)(t + h, T −t) = B(k)(t + h, T −t) + S(k)(t, T −t),
(3.22)
where, again, corrections for average risk factor changes or/and volatility up-
dating can be added.
We note that the use of relative risk factor changes
is the reason for different results of the variants in subsection 3.4.1 and this
subsection.

70
3
Quantification of Spread Risk by Means of Historical Simulation
3.5
Mark-to-Model Backtesting
A backtesting procedure compares the VaR prediction with the observed loss.
In a mark-to-model backtesting the observed loss is determined by calculation
of the present value before and after consideration of the actually observed risk
factor changes. For t0 ≤t ≤t1 the present value at time t+h is calculated with
the yield R(t + h, T −t), which is obtained from observed data for Ri(t + h)
by linear interpolation, according to
PV (t) =
1

1 + R(t + h, T −t)
	T −t .
(3.23)
This corresponds to a loss L(t) = PV (t) −PV (t + h), where, again, the short-
ening of the time to maturity is not taken into account.
The different frameworks for the VaR estimation can easily be integrated into
the backtesting procedure. When we, e.g., only consider changes of the bench-
mark curve, R(t+h, T −t) in (3.23) is replaced with B(t+h, T −t)+S(t, T −t).
On an average (1 −α) · 100 per cent of the observed losses in a given time in-
terval should exceed the corresponding VaR (outliers). Thus, the percentage of
observed losses is a measure for the predictive power of historical simulation.
3.6
VaR Estimation and Backtesting with XploRe
In this section we explain, how a VaR can be calculated and a backtesting can
be implemented with the help of XploRe routines. We present numerical results
for the different yield curves. The VaR estimation is carried out with the help
of the VaRest command. The VaRest command calculates a VaR for historical
simulation, if one specifies the method parameter as ”EDF” (empirical distri-
bution function). However, one has to be careful when specifying the sequence
of asset returns which are used as input for the estimation procedure. If one
calculates zero-bond returns from relative risk factor changes (interest rates or
spreads) the complete empirical distribution of the profits and losses must be
estimated anew for each day from the N relative risk factor changes, because
the profit/loss observations are not identical with the risk factor changes.
For each day the N profit/loss observations generated with one of the methods
described in subsections 3.4.1 to 3.4.5 are stored to a new row in an array PL.
The actual profit and loss data from a mark-to-model calculation for holding

3.6
VaR Estimation and Backtesting with XploRe
71
period h are stored to a one-column-vector MMPL. It is not possible to use a
continuous sequence of profit/loss data with overlapping time windows for the
VaR estimation. Instead the VaRest command must be called separately for
each day. The consequence is that the data the VaRest command operates
on consists of a row of N + 1 numbers: N profit/loss values contained in the
vector (PL[t,])’, which has one column and N rows followed by the actual
mark-to-model profit or loss MMPL[t,1] within holding period h in the last row.
The procedure is implemented in the quantlet XFGpl which can be downloaded
from quantlet download page of this book.
VaR timeplot
5
10
15
time*E2
-10
-5
0
5
10
15
returns*E-2
Figure
3.5.
VaR
time
plot
basic
historical
simulation.
XFGtimeseries.xpl
The result is displayed for the INAAA curve in Figures. 3.5 (basic historical
simulation) and 3.6 (historical simulation with volatility updating). The time
plots allow for a quick detection of violations of the VaR prediction. A striking
feature in the basic historical simulation with the full yield curve as risk fac-
tor is the platform-shaped VaR prediction, while with volatility updating the
VaR prediction decays exponentially after the occurrence of peak events in the
market data. This is a consequence of the exponentially weighted historical

72
3
Quantification of Spread Risk by Means of Historical Simulation
VaR timeplot
5
10
15
time*E2
-15
-10
-5
0
5
10
15
returns*E-2
Figure 3.6. VaR time plot historical simulation with volatility updating.
XFGtimeseries2.xpl
volatility in the scenarios. The peak VaR values are much larger for volatility
updating than for the basic historical simulation.
In order to find out, which framework for VaR estimation has the best predictive
power, we count the number of violations of the VaR prediction and divide it
by the number of actually observed losses. We use the 99% quantile, for which
we would expect an violation rate of 1% for an optimal VaR estimator. The
history used for the drawings of the scenarios consists of N = 250 days, and the
holding period is h = 1 day. For the volatility updating we use a decay factor of
γ = 0.94, J.P. Morgan (1996). For the simulation we assume that the synthetic
zero-bond has a remaining time to maturity of 10 years at the beginning of
the simulations. For the calculation of the first scenario of a basic historical
simulation N + h −1 observations are required. A historical simulation with
volatility updating requires 2(N + h −1) observations preceding the trading
day the first scenario refers to. In order to allow for a comparison between
different methods for the VaR calculation, the beginning of the simulations
is t0 = [2(N + h −1)/N]. With these simulation parameters we obtain 1646

3.7
P-P Plots
73
observations for a zero-bond in the industry sector and 1454 observations for a
zero-bond in the banking sector.
In Tables 3.12 to 3.14 we list the percentage of violations for all yield curves
and the four variants of historical simulation V1 to V4 (V1 = Basic Historical
Simulation; V2 = Basic Historical Simulation with Mean Adjustment; V3 =
Historical Simulation with Mean Adjustment; V4 = Historical Simulation with
Volatility Updating and Mean Adjustment). In the last row we display the
average of the violations of all curves. Table 3.12 contains the results for the
simulation with relative changes of the full yield curves and of the yield spreads
over the benchmark curve as risk factors. In Table 3.13 the risk factors are
changes of the benchmark curves. The violations in the conservative approach
and in the simultaneous simulation of relative spread and benchmark changes
are listed in Table 3.14.
XFGexc.xpl
3.7
P-P Plots
The evaluation of the predictive power across all possible confidence levels
α ∈[0, 1] can be carried out with the help of a transformation of the empirical
distribution {L(k) | 0 ≤k ≤N −1}. If F is the true distribution function
of the loss L within the holding period h, then the random quantity F(L) is
(approximately) uniformly distributed on [0, 1]. Therefore we check the values
Fe

L(t)

for t0 ≤t ≤t1, where Fe is the empirical distribution. If the prediction
quality of the model is adequate, these values should not differ significantly from
a sample with size 250 (t1 −t0 + 1) from a uniform distribution on [0, 1].
The P-P plot of the transformed distribution against the uniform distribution
(which represents the distribution function of the transformed empirical distri-
bution) should therefore be located as closely to the main diagonal as possible.
The mean squared deviation from the uniform distribution (MSD) summed
over all quantile levels can serve as an indicator of the predictive power of a
quantile-based risk measure like VaR. The
XFGpp.xpl quantlet creates a P-P
plot and calculates the MSD indicator.

74
3
Quantification of Spread Risk by Means of Historical Simulation
Full yield
Spread curve
Curve
V1
V2
V3
V4
V1
V2
V3
V4
INAAA
1,34
1,34
1,09
1,28
1,34
1,34
1,34
1,34
INAA2
1,34
1,22
1,22
1,22
1,46
1,52
1,22
1,22
INAA3
1,15
1,22
1,15
1,15
1,09
1,09
0,85
0,91
INA1
1,09
1,09
1,46
1,52
1,40
1,46
1,03
1,09
INA2
1,28
1,28
1,28
1,28
1,15
1,15
0,91
0,91
INA3
1,22
1,22
1,15
1,22
1,15
1,22
1,09
1,15
INBBB1
1,28
1,22
1,09
1,15
1,46
1,46
1,40
1,40
INBBB2
1,09
1,15
0,91
0,91
1,28
1,28
0,91
0,91
INBBB3
1,15
1,15
1,09
1,09
1,34
1,34
1,46
1,52
INBB1
1,34
1,28
1,03
1,03
1,28
1,28
0,97
0,97
INBB2
1,22
1,22
1,22
1,34
1,22
1,22
1,09
1,09
INBB3
1,34
1,28
1,28
1,22
1,09
1,28
1,09
1,09
INB1
1,40
1,40
1,34
1,34
1,52
1,46
1,09
1,03
INB2
1,52
1,46
1,28
1,28
1,34
1,40
1,15
1,15
INB3
1,40
1,40
1,15
1,15
1,46
1,34
1,09
1,15
BNAAA
1,24
1,38
1,10
1,10
0,89
0,89
1,03
1,31
BNAA1/2
1,38
1,24
1,31
1,31
1,03
1,10
1,38
1,38
BNA1
1,03
1,03
1,10
1,17
1,03
1,10
1,24
1,24
BNA2
1,24
1,31
1,24
1,17
0,76
0,83
1,03
1,03
BNA3
1,31
1,24
1,17
1,10
1,03
1,10
1,24
1,17
Average
1,27
1,25
1,18
1,20
1,22
1,24
1,13
1,15
Table 3.12. Violations full yield and spread curve (in %)
Curve
V1
V2
V3
V4
INAAA, INAA2, INAA3, INA1, INA2,
INA3,
INBBB1,
INBBB2,
INBBB3,
INBB1,
INBB2,
INBB3,
INB1,
INB2,
INB3
1,52
1,28
1,22
1,15
BNAAA, BNAA1/2, BNA1, BNA2, BNA3
1,72
1,44
1,17
1,10
Average
1,57
1,32
1,20
1,14
Table 3.13. Violations benchmark curve (in %)
3.8
Q-Q Plots
With a quantile plot (Q-Q plot) it is possible to visualize whether an ordered
sample is distributed according to a given distribution function.
If, e.g., a
sample is normally distributed, the plot of the empirical quantiles vs.
the

3.9
Discussion of Simulation Results
75
conservative approach
simultaneous simulation
Curve
V1
V2
V3
V4
V1
V2
V3
V4
INAAA
0,24
0,24
0,30
0,30
1,22
1,28
0,97
1,03
INAA2
0,24
0,30
0,36
0,30
1,22
1,28
1,03
1,15
INAA3
0,43
0,36
0,30
0,30
1,22
1,15
1,09
1,09
INA1
0,36
0,43
0,55
0,55
1,03
1,03
1,03
1,09
INA2
0,49
0,43
0,49
0,49
1,34
1,28
0,97
0,97
INA3
0,30
0,36
0,30
0,30
1,22
1,15
1,09
1,09
INBBB1
0,43
0,49
0,36
0,36
1,09
1,09
1,03
1,03
INBBB2
0,49
0,49
0,30
0,30
1,03
1,03
0,85
0,79
INBBB3
0,30
0,30
0,36
0,36
1,15
1,22
1,03
1,03
INBB1
0,36
0,30
0,43
0,43
1,34
1,34
1,03
0,97
INBB2
0,43
0,36
0,43
0,43
1,40
1,34
1,15
1,09
INBB3
0,30
0,30
0,36
0,36
1,15
1,15
0,91
0,91
INB1
0,43
0,43
0,43
0,43
1,34
1,34
0,91
0,97
INB2
0,30
0,30
0,30
0,30
1,34
1,34
0,97
1,03
INB3
0,30
0,30
0,36
0,30
1,46
1,40
1,22
1,22
BNAAA
0,62
0,62
0,48
0,48
1,31
1,31
1,10
1,03
BNAA1/2
0,55
0,55
0,55
0,48
1,24
1,31
1,10
1,17
BNA1
0,62
0,62
0,55
0,55
0,96
1,03
1,10
1,17
BNA2
0,55
0,62
0,69
0,69
0,89
1,96
1,03
1,03
BNA3
0,55
0,55
0,28
0,28
1,38
1,31
1,03
1,10
Average
0,41
0,42
0,41
0,40
1,22
1,22
1,03
1,05
Table 3.14. Violations in the conservative approach and simultaneous
simulation(in %)
quantiles of a normal distribution should result in an approximately linear
plot. Q-Q plots vs. a normal distribution can be generated with the following
command:
VaRqqplot(matrix(N,1)|MMPL,VaR,opt)
3.9
Discussion of Simulation Results
In Figure 3.7 the P-P plots for the historical simulation with the full yield curve
(INAAA) as risk factor are displayed for the different variants of the simulation.
From the P-P plots it is apparent that mean adjustment significantly improves
the predictive power in particular for intermediate confidence levels (i.e., for
small risk factor changes).

76
3
Quantification of Spread Risk by Means of Historical Simulation
Basic Simulation
0
0.5
1
Uniform Distribution
0
0.5
1
Empirical Distribution
Volatility Updating
0
0.5
1
Uniform Distribution
0
0.5
1
Empirical Distribution
Mean Adjustment
0
0.5
1
Uniform Distribution
0
0.5
1
Empirical Distribution
Volatility Updating & Mean Adjustment
0
0.5
1
Uniform Distribution
0
0.5
1
Empirical Distribution
Figure 3.7. P-P Plots variants of the simulation.
XFGpp.xpl
Figure 3.8 displays the P-P plots for the same data set and the basic historical
simulation with different choices of risk factors. A striking feature is the poor
predictive power for a model with the spread as risk factor. Moreover, the
over-estimation of the risk in the conservative approach is clearly reflected by
a sine-shaped function, which is superposed on the ideal diagonal function.
In Figs. 3.9 and 3.10 we show the Q-Q plots for basic historic simulation and
volatility updating using the INAAA data set and the full yield curve as risk
factors. A striking feature of all Q-Q plots is the deviation from linearity (and,
thus, normality) for extreme quantiles. This observation corresponds to the
leptokurtic distributions of time series of market data changes (e.g.
spread
changes as discussed in section 3.3.2).

3.9
Discussion of Simulation Results
77
Benchmark Curve
0
0.5
1
Uniform Distribution
0
0.5
1
Empirical Distribution
Conservative Approach
0
0.5
1
Uniform Distribution
0
0.5
1
Empirical Distribution
Spread Curve
0
0.5
1
Uniform Distribution
0
0.5
1
Empirical Distribution
Simultaneous Simulation
0
0.5
1
Uniform Distribution
0
0.5
1
Empirical Distribution
Figure 3.8. P-P Plots choice of risk factors.
XFGpp.xpl
3.9.1
Risk Factor: Full Yield
The results in Table 3.12 indicate a small under-estimation of the actually
observed losses. While volatility updating leads to a reduction of violations,
this effect is not clearly recognizable for the mean adjustment. The positive
results for volatility updating are also reflected in the corresponding mean
squared deviations in Table 3.15. Compared with the basic simulation, the
model quality can be improved. There is also a positive effect of the mean
adjustment.

78
3
Quantification of Spread Risk by Means of Historical Simulation
VaR reliability plot
-4
-2
0
2
4
normal quantiles
-4
-2
0
2
4
L/VaR quantiles
Figure 3.9. Q-Q Plot for basic historical simulation.
3.9.2
Risk Factor: Benchmark
The results for the number of violations in Table 3.13 and the mean squared
deviations in Table 3.16 are comparable to the analysis, where risk factors are
changes of the full yield. Since the same relative changes are applied for all
yield curves, the results are the same for all yield curves. Again, the application
of volatility updating improves the predictive power and mean adjustment also
has a positive effect.
3.9.3
Risk Factor: Spread over Benchmark Yield
The number of violations (see Table 3.12) is comparable to the latter two
variants. Volatility updating leads to better results, while the effect of mean

3.9
Discussion of Simulation Results
79
VaR reliability plot
-4
-2
0
2
4
normal quantiles
-4
-2
0
2
4
L/VaR quantiles
Figure 3.10. Q-Q plot for volatility updating.
adjustment is only marginal. However, the mean squared deviations (see Ta-
ble 3.15) in the P-P plots are significantly larger than in the case, where the
risk factors are contained in the benchmark curve. This can be traced back to a
partly poor predictive power for intermediate confidence levels (see Figure 3.8).
Mean adjustment leads to larger errors in the P-P plots.
3.9.4
Conservative Approach
From Table 3.14 the conclusion can be drawn, that the conservative approach
significantly over-estimates the risk for all credit qualities. Table 3.17 indicates
the poor predictive power of the conservative approach over the full range of
confidence levels.

80
3
Quantification of Spread Risk by Means of Historical Simulation
full yield
spread curve
Curve
V1
V2
V3
V4
V1
V2
V3
V4
INAAA
0,87
0,28
0,50
0,14
8,13
22,19
8,14
16,15
INAA2
0,45
0,36
0,32
0,16
6,96
21,41
7,25
15,62
INAA3
0,54
0,41
0,43
0,23
7,91
21,98
7,97
15,89
INA1
0,71
0,27
0,41
0,13
7,90
15,32
8,10
8,39
INA2
0,50
0,39
0,42
0,17
9,16
15,15
9,51
6,19
INA3
0,81
0,24
0,58
0,24
9,53
12,96
9,61
7,09
INBBB1
0,71
0,29
0,54
0,13
9,59
15,71
9,65
11,13
INBBB2
0,33
0,34
0,26
0,12
11,82
14,58
11,59
10,72
INBBB3
0,35
0,59
0,40
0,34
7,52
11,49
7,78
6,32
INBB1
0,31
0,95
0,26
0,28
4,14
4,57
3,90
1,61
INBB2
0,52
0,49
0,36
0,19
6,03
3,63
5,89
2,12
INBB3
0,53
0,41
0,36
0,17
3,11
3,65
3,09
1,67
INB1
0,51
0,29
0,38
0,15
3,59
1,92
2,85
1,16
INB2
0,51
0,48
0,31
0,22
4,29
2,31
3,41
1,42
INB3
0,72
0,38
0,32
0,16
3,70
2,10
2,99
3,02
BNAAA
0,59
0,19
0,48
0,56
10,13
17,64
9,74
11,10
BNAA1/2
0,54
0,21
0,45
0,46
5,43
13,40
5,73
7,50
BNA1
0,31
0,12
0,29
0,25
8,65
17,19
8,09
8,21
BNA2
0,65
0,19
0,57
0,59
6,52
12,52
6,95
6,45
BNA3
0,31
0,19
0,32
0,29
6,62
9,62
6,59
3,80
Average
0,54
0,35
0,40
0,25
7,04
11,97
6,94
7,28
Table 3.15.
MSD P-P Plot for the full yield and the spread
curve(×10 000)
The mean squared deviations are the worst of all approaches. Volatility updat-
ing and/or mean adjustment does not lead to any significant improvements.
3.9.5
Simultaneous Simulation
From Tables 3.14 and 3.17 it is apparent that simultaneous simulation leads to
much better results than the model with risk factors from the full yield curve,
when volatility updating is included. Again, the effect of mean adjustment
does not in general lead to a significant improvement. These results lead to
the conclusion that general market risk and spread risk should be modeled
independently, i.e., that the yield curve of an instrument exposed to credit
risk should be modeled with two risk factors: benchmark changes and spread
changes.

3.10
XploRe for Internal Risk Models
81
Curve
V1
V2
V3
V4
INAAA, INAA2, INAA3
0,49
0,23
0,26
0,12
INA1
0,48
0,23
0,26
0,12
INA2, INA3, INBBB1, INBBB2, INBBB3,
INBB1, INBB2
0,49
0,23
0,26
0,12
INBB3
0,47
0,23
0,25
0,12
INB1
0,49
0,23
0,26
0,12
INB2
0,47
0,23
0,25
0,12
INB3
0,48
0,23
0,26
0,12
BNAAA, BNAA1/2
0,42
0,18
0,25
0,33
BNA1
0,41
0,18
0,23
0,33
BNA2
0,42
0,18
0,25
0,33
BNA3
0,41
0,18
0,24
0,33
Average
0,47
0,22
0,25
0,17
Table 3.16. MSD P-P-Plot benchmark curve (×10 000)
3.10
XploRe for Internal Risk Models
In this contribution it is demonstrated that XploRe can be used as a tool in
the analysis of time series of market data and empirical loss distributions. The
focus of this contribution is on the analysis of spread risk. Yield spreads are
an indicator of an obligor’s credit risk. The distributions of spread changes are
leptokurtic with typical fat tails, which makes the application of conventional
variance-covariance risk models problematic. That is why in this contribution
we prefer the analysis of spread risk by means of historical simulation. Since
it is not a priori clear, how spread risk should be integrated in a risk model
for interest rate products and how it can be separated from general market
risk, we investigate several possibilities, which include modelling the full yield
curve (i.e., consideration of only one risk factor category, which covers both
benchmark and spread risk) as well as separately modelling spread risk and
benchmark risk. The aggregation of both risk categories is carried out in a
conservative way (addition of the risk measure for both risk categories) as well
as coherently (simultaneous simulation of spread and benchmark risk). More-
over, in addition to the basic historical simulation method we add additional
features like mean adjustment and volatility updating. Risk is quantified by
means of a quantile-based risk measure in this contribution - the VaR. We
demonstrate the differences between the different methods by calculating the
VaR for a fictive zero-bond.

82
3
Quantification of Spread Risk by Means of Historical Simulation
conservative approach
simultaneous simulation
Curve
V1
V2
V3
V4
V1
V2
V3
V4
INAAA
14,94
14,56
14,00
13,88
1,52
0,64
0,75
0,40
INAA2
13,65
13,51
14,29
14,31
0,79
0,38
0,40
0,23
INAA3
14,34
13,99
13,66
13,44
0,79
0,32
0,49
0,27
INA1
15,39
15,60
15,60
15,60
0,95
0,40
0,52
0,29
INA2
13,95
14,20
14,32
14,10
0,71
0,55
0,50
0,39
INA3
14,73
14,95
14,45
14,53
0,94
0,30
0,59
0,35
INBBB1
13,94
14,59
14,05
14,10
1,00
0,33
0,43
0,17
INBBB2
13,74
13,91
13,67
13,73
0,64
0,52
0,45
0,29
INBBB3
13,68
14,24
14,10
14,09
0,36
0,78
0,31
0,31
INBB1
19,19
20,68
18,93
19,40
0,73
1,37
0,52
0,70
INBB2
13,21
14,17
14,79
15,15
0,30
0,82
0,35
0,51
INBB3
15,19
16,47
15,40
15,67
0,55
0,65
0,15
0,21
INB1
15,47
15,64
15,29
15,51
0,53
0,44
0,19
0,26
INB2
14,47
14,93
15,46
15,77
0,24
0,55
0,24
0,24
INB3
14,78
14,67
16,77
17,03
0,38
0,44
0,27
0,22
BNAAA
14,80
15,30
16,30
16,64
1,13
0,33
0,99
0,96
BNAA1/2
13,06
13,45
14,97
15,43
0,73
0,16
0,57
0,50
BNA1
11,95
11,83
12,84
13,08
0,52
0,26
0,44
0,41
BNA2
13,04
12,58
14,31
14,56
0,78
0,13
0,51
0,58
BNA3
12,99
12,70
15,19
15,42
0,34
0,18
0,58
0,70
Average
14,33
14,60
14,92
15,07
0,70
0,48
0,46
0,40
Table 3.17. MSD P-P Plot for the conservative approach and the si-
multaneous simulation(×10 000)
The numerical results indicate, that the conservative approach over-estimates
the risk of our fictive position, while the simulation results for the full yield as
single risk factor are quite convincing. The best result, however, is delivered
by a combination of simultaneous simulation of spread and benchmark risk
and volatility updating, which compensates for non-stationarity in the risk
factor time series. The conclusion from this contribution for model-builders
in the banking community is, that it should be checked, whether the full yield
curve or the simultaneous simulation with volatility updating yield satisfactory
results for the portfolio considered.

3.10
XploRe for Internal Risk Models
83
Bibliography
Bank for International Settlements (1998a). Amendment to the Capital Accord
to incorporate market risks, www.bis.org. (January 1996, updated to April
1998).
Bank for International Settlements (1998b). Overview of the Amendment to
the Capital Accord to incorporate market risk, www.bis.org.
(January
1996, updated to April 1998).
Bundesaufsichtsamt f¨ur das Kreditwesen (2001). Grundsatz I/Modellierung des
besonderen Kursrisikos, Rundschreiben 1/2001, www.bakred.de.
Gaumert,
U. (1999).
Zur Diskussion um die Modellierung besonderer
Kursrisiken in VaR-Modellen, Handbuch Bankenaufsicht und Interne
Risikosteuerungsmodelle, Sch¨affer-Poeschel.
Hull, J. C. (1998). Integrating Volatility Updating into the Historical Simula-
tion Method for Value at Risk, Journal of Risk .
J.P. Morgan (1996). RiskMetrics, Technical report, J.P. Morgan, New York.
Kiesel, R., Perraudin, W. and Taylor, A. (1999). The Structure of Credit Risk.
Working Paper, London School of Economics.


Part II
Credit Risk


4 Rating Migrations
SteffiH¨ose, Stefan Huschens and Robert Wania
The bond rating is one of the most important indicators of a corporation’s
credit quality and therefore its default probability. It was first developed by
Moody’s in 1914 and by Poor’s Corporation in 1922 and it is generally assigned
by external agencies to publicly traded debts. Apart from the external ratings
by independent rating agencies, there are internal ratings by banks and other
financial institutions, Basel Committee on Banking Supervision (2001). Exter-
nal rating data by agencies are available for many years, in contrast to internal
ratings. Their short history in most cases does not exceed 5–10 years. Both
types of ratings are usually recorded on an ordinal scale and labeled alphabeti-
cally or numerically. For the construction of a rating system see Crouhy, Galai,
and Mark (2001).
A change in a rating reflects the assessment that the company’s credit quality
has improved (upgrade) or deteriorated (downgrade). Analyzing these rating
migrations including default is one of the preliminaries for credit risk models
in order to measure future credit loss. In such models, the matrix of rating
transition probabilities, the so called transition matrix, plays a crucial role. It
allows to calculate the joint distribution of future ratings for borrowers that
compose a portfolio, Gupton, Finger, and Bhatia (1997).
An element of a
transition matrix gives the probability that an obligor with a certain initial
rating migrates to another rating by the risk horizon.
For the econometric
analysis of transition data see Lancaster (1990).
In a study by Jarrow, Lando, and Turnbull (1997) rating transitions were mod-
eled as a time-homogeneous Markov chain, so future rating changes are not
affected by the rating history (Markov property). The probability of chang-
ing from one rating to another is constant over time (homogeneous), which
is assumed solely for simplicity of estimation.
Empirical evidence indicates
that transition probabilities are time-varying. Nickell, Perraudin, and Varotto
(2000) show that different transition matrices are identified across various fac-

88
4
Rating Migrations
tors such as the obligor’s domicile and industry and the stage of business cycle.
Rating migrations are reviewed from a statistical point of view throughout this
chapter using XploRe. The way from the observed data to the estimated one-
year transition probabilities is shown and estimates for the standard deviations
of the transition rates are given. In further extension, dependent rating migra-
tions are discussed. In particular, the modeling by a threshold normal model
is presented.
Time stability of transition matrices is one of the major issues for credit risk
estimation. Therefore, a chi-square test of homogeneity for the estimated rating
transition probabilities is applied. The test is illustrated by an example and
is compared to a simpler approach using standard errors. Further, assuming
time stability, multi-period rating transitions are discussed. An estimator for
multi-period transition matrices is given and its distribution is approximated
by bootstrapping. Finally, the change of the composition of a credit portfolio
caused by rating migrations is considered. The expected composition and its
variance is calculated for independent migrations.
4.1
Rating Transition Probabilities
In this section, the way from raw data to estimated rating transition prob-
abilities is described. First, migration events of the same kind are counted.
The resulting migration counts are transformed into migration rates, which are
used as estimates for the unknown transition probabilities. These estimates are
complemented with estimated standard errors for two cases, for independence
and for a special correlation structure.
4.1.1
From Credit Events to Migration Counts
We assume that credits or credit obligors are rated in d categories ranging from
1, the best rating category, to the category d containing defaulted credits. The
raw data consist of a collection of migration events. The n observed migration
events form a n × 2 matrix with rows
(ei1, ei2) ∈{1, . . . , d −1} × {1, . . . , d},
i = 1, . . . , n.
Thereby, ei1 characterizes the rating of i-th credit at the beginning and ei2 the
rating at the end of the risk horizon, which is usually one year. Subsequently,

4.1
Rating Transition Probabilities
89
migration events of the same kind are aggregated in a (d −1) × d matrix C of
migration counts, where the generic element
cjk
def
=
n
X
i=1
1{(ei1, ei2) = (j, k)}
is the number of migration events from j to k. Clearly, their total sum is
d−1
X
j=1
d
X
k=1
cjk = n.
4.1.2
Estimating Rating Transition Probabilities
We assume that each observation ei2 is a realization of a random variable ˜ei2
with conditional probability distribution
pjk = P(˜ei2 = k|˜ei1 = j),
d
X
k=1
pjk = 1,
where pjk is the probability that a credit migrates from an initial rating j to
rating k. These probabilities are the so called rating transition (or migration)
probabilities. Note that the indicator variable 1{˜ei2 = k} conditional on ˜ei1 = j
is a Bernoulli distributed random variable with success parameter pjk,
1{˜ei2 = k} | ˜ei1 = j ∼Ber(pjk).
(4.1)
In order to estimate these rating transition probabilities we define the number
of migrations starting from rating j as
nj
def
=
d
X
k=1
cjk,
j = 1, . . . , d −1
(4.2)
and assume nj > 0 for j = 1, . . . , d−1. Thus, (n1, . . . , nd−1) is the composition
of the portfolio at the beginning of the period and


d−1
X
j=1
cj1, . . . ,
d−1
X
j=1
cjd


(4.3)

90
4
Rating Migrations
is the composition of the portfolio at the end of the period, where the last
element is the number of defaulted credits. The observed migration rate from
j to k,
ˆpjk
def
= cjk
nj
,
(4.4)
is the natural estimate of the unknown transition probability pjk.
If the migration events are independent, i. e., the variables ˜e12, . . . , ˜en2 are
stochastically independent, cjk is the observed value of the binomially dis-
tributed random variable
˜cjk ∼B(nj, pjk),
and therefore the standard deviation of ˆpjk is
σjk =
s
pjk(1 −pjk)
nj
,
which may be estimated by
ˆσjk =
s
ˆpjk(1 −ˆpjk)
nj
.
(4.5)
The estimated standard errors must be carefully interpreted, because they are
based on the assumption of independence.
4.1.3
Dependent Migrations
The case of dependent rating migrations raises new problems. In this context,
˜cjk is distributed as sum of nj correlated Bernoulli variables, see (4.1), indicat-
ing for each credit with initial rating j a migration to k by 1. If these Bernoulli
variables are pairwise correlated with correlation ρjk, then the variance σ2
jk
of the unbiased estimator ˆpjk for pjk is (Huschens and Locarek-Junge, 2000,
p. 44)
σ2
jk = pjk(1 −pjk)
nj
+ nj −1
nj
ρjkpjk(1 −pjk).
The limit
lim
nj→∞σ2
jk = ρjkpjk(1 −pjk)
shows that the sequence ˆpjk does not obey a law of large numbers for ρjk > 0.
Generally, the failing of convergence in quadratic mean does not imply the

4.1
Rating Transition Probabilities
91
failing of convergence in probability. But in this case all moments of higher
order exist since the random variable ˆpjk is bounded and so the convergence
in probability implies the convergence in quadratic mean. For ρjk = 0 the law
of large numbers holds. Negative correlations can only be obtained for finite
nj. The lower boundary for the correlation is given by ρjk ≥−
1
nj−1, which
converges to zero when the number of credits nj grows to infinity.
The law of large numbers fails also if the correlations are different with ei-
ther a common positive lower bound, or non vanishing positive average cor-
relation or constant correlation blocks with positive correlations in each block
(Finger, 1998, p. 5). This failing of the law of large numbers may not sur-
prise a time series statistician, who is familiar with mixing conditions to ensure
mean ergodicity of stochastic processes (Davidson, 1994, chapter 14). In sta-
tistical words, in the case of non-zero correlation the relative frequency is not
a consistent estimator of the Bernoulli parameter.
The parameters ρjk may be modeled in consistent way in the framework of a
threshold normal model with a single parameter ρ (Basel Committee on Bank-
ing Supervision, 2001; Gupton et al., 1997; Kim, 1999).
This model speci-
fies a special dependence structure based on a standard multinormal distri-
bution for a vector (R1, . . . , Rn) with equicorrelation matrix (Mardia, Kent,
and Bibby, 1979, p. 461), where Ri (i = 1, . . . , n) is the standardized asset
return and n is the number of obligors. The parameter ρ > 0 may be inter-
preted as a mean asset return correlation. In this model each pair of variables
(X, Y ) = (Ri, Ri′) with i, i′ = 1, . . . , n and i ̸= i′ is bivariate normally dis-
tributed with density function
ϕ(x, y; ρ) =
1
2π
p
1 −ρ2 exp

−x2 −2ρxy + y2
2(1 −ρ2)

.
The probability P[(X, Y ) ∈(a, b)2] is given by
β(a, b; ρ) =
Z b
a
Z b
a
ϕ(x, y; ρ) dx dy.
(4.6)
Thresholds for rating j are derived from pj1, . . . , pj,d−1 by
zj0
def
= −∞, zj1
def
= Φ−1(pj1), zj2
def
= Φ−1(pj1 + pj2), . . . , zjd
def
= +∞,
where Φ is the distribution function of the standardized normal distribution
and Φ−1 it’s inverse. Each credit in category j is characterized by a normally
distributed variable Z which determines the migration events by
pjk = P(Z ∈(zj,k−1, zjk)) = Φ(zjk) −Φ(zj,k−1).

92
4
Rating Migrations
The simultaneous transition probabilities of two credits i and i′ from category
j to k are given by
pjj:kk = P(˜ei2 = ˜ei′2 = k|˜ei1 = ˜ei′1 = j) = β(zj,k−1, zjk; ρ),
i.e., the probability of simultaneous default is
pjj:dd = β(zj,d−1, zjd; ρ).
For a detailed example see Saunders (1999, pp. 122-125). In the special case of
independence we have pjj:kk = p2
jk. Defining a migration from j to k as suc-
cess we obtain correlated Bernoulli variables with common success parameter
pjk, with probability pjj:kk of a simultaneous success, and with the migration
correlation
ρjk =
pjj:kk −p2
jk
pjk(1 −pjk).
Note that ρjk = 0 if ρ = 0.
Given ρ ≥0 we can estimate the migration correlation ρjk ≥0 by the restricted
Maximum-Likelihood estimator
ˆρjk = max
(
0;
β(ˆzj,k−1, ˆzjk; ρ) −ˆp2
jk
ˆpjk(1 −ˆpjk)
)
(4.7)
with
ˆzjk = Φ−1
 k
X
i=1
ˆpji
!
.
(4.8)
The estimate
ˆσjk =
s
ˆpjk(1 −ˆpjk)
nj
+ nj −1
nj
ˆρjk ˆpjk(1 −ˆpjk)
(4.9)
of the standard deviation
σjk =
s
pjk(1 −pjk)
nj
+ nj −1
nj
ρjkpjk(1 −pjk)
is used. The estimator in (4.9) generalizes (4.5), which results in the special
case ρ = 0.

4.1
Rating Transition Probabilities
93
4.1.4
Computation and Quantlets
counts = VaRRatMigCount (d, e)
computes migration counts from migration events
The quantlet VaRRatMigCount can be used to compute migration counts from
migration events, where d is the number of categories including default and e
is the n × 2 data matrix containing n migration events. The result is assigned
to the variable counts, which is the (d −1) × d matrix of migration counts.
XFGRatMig1.xpl
b = VaRRatMigRate (c, rho, s)
computes migration rates and related estimated standard errors
The quantlet VaRRatMigRate computes migration rates and related estimated
standard errors for m periods from an input matrix of migration counts and
a given correlation parameter. Here, c is a (d −1) × d × m array of m-period
migration counts and rho is a non-negative correlation parameter as used in
(4.6). For rho = 0 the independent case is computed.
The calculation uses stochastic integration in order to determine the probability
β from (4.6). The accuracy of the applied Monte Carlo procedure is controlled
by the input parameter s. For s > 0 the sample size is at least n ≥(2s)−2.
This guarantees that the user-specified value s is an upper bound for the stan-
dard deviation of the Monte Carlo estimator for β. Note that with increasing
accuracy (i. e. decreasing s) the computational effort increases proportional to
n.
The result is assigned to the variable b, which is a list containing:
• b.nstart
the (d −1) × 1 × m array of portfolio weights before migration
• b.nend
the d × 1 × m array portfolio weights after migration
• b.etp
the (d −1) × d × m array of estimated transition probabilities

94
4
Rating Migrations
• b.etv
the (d −1) × (d −1) × m array of estimated threshold values
• b.emc
the (d −1) × d × m array of estimated migration correlations
• b.esd
the (d −1) × d × m array of estimated standard deviations
The matrices b.nstart and b.nend have components given by (4.2) and (4.3).
The matrices b.etp, b.emc, and b.esd contain the ˆpjk, ˆρjk, and ˆσjk from
(4.4), (4.7), and (4.9) for j = 1, . . . , d −1 and k = 1, . . . , d. The estimates ˆρjk
are given only for ˆpjk > 0. The matrix b.etv contains the ˆzjk from (4.8) for
j, k = 1, . . . , d −1. Note that zj0 = −∞and zjd = +∞.
XFGRatMig2.xpl
4.2
Analyzing the Time-Stability of Transition
Probabilities
4.2.1
Aggregation over Periods
We assume that migration data are given for m periods. This data consist in m
matrices of migration counts C(t) for t = 1, . . . , m each of type (d−1)×d. The
generic element cjk(t) of the matrix C(t) is the number of migrations from j to
k in period t. These matrices may be computed from m data sets of migration
events.
An obvious question in this context is whether the transition probabilities can
be assumed to be constant in time or not. A first approach to analyze the
time-stability of transition probabilities is to compare the estimated transition
probabilities per period for m periods with estimates from pooled data.
The aggregated migration counts from m periods are
c+
jk
def
=
m
X
t=1
cjk(t)
(4.10)

4.2
Analyzing the Time-Stability of Transition Probabilities
95
which are combined in the matrix
C+ def
=
m
X
t=1
C(t)
of type (d −1) × d. The migration rates computed per period
ˆpjk(t)
def
= cjk(t)
nj(t) ,
t = 1, . . . , m
(4.11)
with
nj(t)
def
=
d
X
k=1
cjk(t)
have to be compared with the migration rates from the pooled data. Based on
the aggregated migration counts the estimated transition probabilities
ˆp+
jk
def
=
c+
jk
nj+
(4.12)
with
n+
j
def
=
d
X
k=1
c+
jk =
m
X
t=1
nj(t),
j = 1, . . . , d −1
can be computed.
4.2.2
Are the Transition Probabilities Stationary?
Under the assumption of independence for the migration events the vector
of migration counts (cj1(t), . . . cjd(t)) starting from j is in each period t a
realization from a multinomial distributed random vector
(˜cj1(t), . . . , ˜cjd(t)) ∼Mult(nj(t); pj1(t), . . . , pjd(t)),
where pjk(t) denotes the transition probability from j to k in period t. For
fixed j ∈{1, . . . , d −1} the hypothesis of homogeneity
H0 : pj1(1) = . . . = pj1(m), pj2(1) = . . . = pj2(m), . . . , pjd(1) = . . . = pjd(m)
may be tested with the statistic
X2
j =
d
X
k=1
m
X
t=1
h
˜cjk(t) −nj(t)ˆp+
jk
i2
nj(t)ˆp+
jk
.
(4.13)

96
4
Rating Migrations
This statistic is asymptotically χ2-distributed with (d−1)(m−1) degrees of free-
dom under H0. H0 is rejected with approximative level α if the statistic com-
puted from the data is greater than the (1 −α)-quantile of the χ2-distribution
with (d −1)(m −1) degrees of freedom.
The combined hypothesis of homogeneity
H0 : pjk(t) = pjk(m),
t = 1, . . . , m −1,
j = 1, . . . , d −1,
k = 1, . . . , d
means that the matrix of transition probabilities is constant over time. There-
fore, the combined null hypothesis may equivalently be formulated as
H0 : P(1) = P(2) = . . . = P(m),
where P(t) denotes the transition matrix at t with generic element pjk(t). This
hypothesis may be tested using the statistic
X2 =
d−1
X
j=1
X2
j ,
(4.14)
which is under H0 asymptotically χ2-distributed with (d−1)2(m−1) degrees of
freedom. The combined null hypothesis is rejected with approximative level α if
the computed statistic is greater than the (1−α)-quantile of the χ2-distribution
with (d −1)2(m −1) degrees of freedom (Bishop, Fienberg, and Holland, 1975,
p. 265).
This approach creates two problems. Firstly, the two tests are based on the as-
sumption of independence. Secondly, the test statistics are only asymptotically
χ2-distributed. This means that sufficiently large sample sizes are required. A
rule of thumb given in the literature is nj(t)ˆp+
jk ≥5 for all j and k which is
hardly fulfilled in the context of credit migrations.
The two χ2-statistics in (4.13) and (4.14) are of the Pearson type. Two other
frequently used and asymptotically equivalent statistics are the corresponding
χ2-statistics of the Neyman type
Y 2
j =
d
X
k=1
m
X
t=1
h
˜cjk(t) −nj(t)ˆp+
jk
i2
˜cjk(t)
,
Y 2 =
d−1
X
j=1
Y 2
j
and the χ2-statistics
G2
j = 2
d
X
k=1
m
X
t=1
˜cjk(t) ln
"
˜cjk(t)
nj(t)ˆp+
jk
#
,
G2 =
d−1
X
j=1
G2
j,

4.2
Analyzing the Time-Stability of Transition Probabilities
97
which results from Wilks log-likelihood ratio.
Considering the strong assumptions on which these test procedures are based
on, one may prefer a simpler approach complementing the point estimates
ˆpjk(t) by estimated standard errors
ˆσjk(t) =
s
ˆpjk(t)(1 −ˆpjk(t))
nj(t)
for each period t ∈{1, . . . , m}. For correlated migrations the estimated stan-
dard deviation is computed analogously to (4.9).
This may graphically be
visualized by showing
ˆp+
jk,
ˆpjk(t),
ˆpjk(t) ± 2ˆσjk(t),
t = 1, . . . , m
(4.15)
simultaneously for j = 1, . . . , d −1 and k = 1, . . . , d.
4.2.3
Computation and Quantlets
The quantlet
XFGRatMig3.xpl computes aggregated migration counts,
estimated transition probabilities and χ2-statistics.
The call is out =
XFGRatMig3(c, rho, s), where c is a (d −1) × d × m array of counts for
m periods and rho is a non-negative correlation parameter. For rho = 0 the
independent case is computed, compare Section 4.1.4. The last input parameter
s controls the accuracy of the computation, see Section 4.1.4.
The result is assigned to the variable out, which is a list containing:
• out.cagg
the (d −1) × d matrix with aggregated counts
• out.etpagg
the (d −1) × d matrix with estimated aggregated transition probabilities
• out.esdagg
the (d −1) × d matrix with estimated aggregated standard deviations
• out.etp
the (d−1)×d×m array with estimated transition probabilities per period
• out.esd
the (d −1) × d × m array with estimated standard deviations per period

98
4
Rating Migrations
• out.chi
the 3 × d matrix with χ2-statistics, degrees of freedom and p-values
The matrices out.cagg, out.etpagg and out.etp have components given by
(4.10), (4.12) and (4.11).
The elements of out.esdagg and out.esd result
by replacing ˆpjk in (4.9) by ˆp+
jk or ˆpjk(t), respectively. The matrix out.chi
contains in the first row the statistics from (4.13) for j = 1, . . . , d −1 and
(4.14). The second and third row gives the corresponding degrees of freedom
and p-values.
The quantlet
XFGRatMig4.xpl (XFGRatMig4(etp, esd, etpagg)) graphs
migration rates per period with estimated standard deviations and migration
rates from pooled data. The inputs are:
• etp
the (d−1)×d×m array with estimated transition probabilities per period
• esd
the (d −1) × d × m array with estimated standard deviations per period
• etpagg
the (d −1) × d matrix with estimated aggregated transition probabilities
The output consists of (d −1)d graphics for j = 1, . . . , d −1 and k = 1, . . . , d.
Each graphic shows t = 1, . . . , m at the x-axis versus the four variables from
(4.15) at the y-axis.
4.2.4
Examples with Graphical Presentation
The following examples are based on transition matrices given by Nickell et al.
(2000, pp. 208, 213). The data set covers long-term bonds rated by Moody’s
in the period 1970–1997. Instead of the original matrices of type 8 × 9 we
use condensed matrices of type 3 × 4 by combining the original data in the
d = 4 basic rating categories A, B, C, and D, where D stands for the category
of defaulted credits.
The aggregated data for the full period from 1970 to 1997 are
C =


21726
790
0
0
639
21484
139
421
0
44
307
82

,
ˆP =


0.965
0.035
0
0
0.028
0.947
0.006
0.019
0
0.102
0.709
0.189

,

4.2
Analyzing the Time-Stability of Transition Probabilities
99
where C is the matrix of migration counts and ˆP is the corresponding matrix
of estimated transition probabilities. These matrices may be compared with
corresponding matrices for three alternative states of the business cycles:
C(1) =


7434
277
0
0
273
7306
62
187
0
15
94
33

,
ˆP(1) =


0.964
0.036
0
0
0.035
0.933
0.008
0.024
0
0.106
0.662
0.232

,
for the through of the business cycle,
C(2) =


7125
305
0
0
177
6626
35
147
0
15
92
24

,
ˆP(2) =


0.959
0.041
0
0
0.025
0.949
0.005
0.021
0
0.115
0.702
0.183

,
for the normal phase of the business cycle, and
C(3) =


7167
208
0
0
189
7552
42
87
0
14
121
25

,
ˆP(3) =


0.972
0.028
0
0
0.024
0.960
0.005
0.011
0
0.088
0.756
0.156

,
for the peak of the business cycle. The three categories depend on whether
real GDP growth in the country was in the upper, middle or lower third of the
growth rates recorded in the sample period (Nickell et al., 2000, Sec. 2.4).
In the following we use these matrices for illustrative purposes as if data from
m = 3 periods are given. Figure 4.1 gives a graphical presentation for d = 4
rating categories and m = 3 periods.
In order to illustrate the testing procedures presented in Section 4.2.2 in
the following the hypothesis is tested that the data from the three periods
came from the same theoretical transition probabilities.
Clearly, from the
construction of the three periods we may expect, that the test rejects the null
hypothesis. The three χ2-statistics with 6 = 3(3 −1) degrees of freedom for
testing the equality of the rows of the transition matrices have p-values 0.994,
> 0.9999, and 0.303. Thus, the null hypothesis must be clearly rejected for
the first two rows at any usual level of confidence while the test for the last
row suffers from the limited sample size. Nevertheless, the χ2-statistic for the
simultaneous test of the equality of the transition matrices has 18 = 32 ·(3−1)
degrees of freedom and a p-value > 0.9999. Consequently, the null hypothesis
must be rejected at any usual level of confidence.
XFGRatMig3.xpl
A second example is given by comparing the matrix ˆP based on the whole data
with the matrix ˆP(2) based on the data of the normal phase of the business

100
4
Rating Migrations
1
1.5
2
2.5
3
Periods
5
10
15
20
25
0.95+Y*E-2
1
1.5
2
2.5
3
Periods
5
10
15
20
25
0.015+Y*E-2
1
1.5
2
2.5
3
Periods
-1
-0.5
0
0.5
1
Y
1
1.5
2
2.5
3
Periods
5
10
15
20
25
0.02+Y*E-2
1
1.5
2
2.5
3
Periods
1
2
3
4
0.92+Y*E-2
1
1.5
2
2.5
3
Periods
5
10
15
Y*E-2
1
1.5
2
2.5
3
Periods
-1
-0.5
0
0.5
1
Y
1
1.5
2
2.5
3
Periods
2
4
6
8
0.002+Y*E-2
1
1.5
2
2.5
3
Periods
5
10
15
20
25
0.55+Y*E-2
1
1.5
2
2.5
3
Periods
-1
-0.5
0
0.5
1
Y
1
1.5
2
2.5
3
Periods
5
10
15
20
0.005+Y*E-2
1
1.5
2
2.5
3
Periods
5
10
15
20
25
0.05+Y*E-2
Figure 4.1. Example for
XFGRatMig4.xpl
cycle. In this case a test possibly may not indicate that differences between
P and P(2) are significant. Indeed, the χ2-statistics for testing the equality
of the rows of the transition matrices with 3 degrees of freedom have p-values
0.85, 0.82, and 0.02. The statistic of the simultaneous test with 9 degrees of
freedom has a p-value of 0.69.

4.3
Multi-Period Transitions
101
4.3
Multi-Period Transitions
In the multi-period case, transitions in credit ratings are also characterized by
rating transition matrices. The m-period transition matrix is labeled P(m).
Its generic element p(m)
jk
gives the rating transition probability from rating
j to k over the m ≥1 periods.
For the sake of simplicity the one-period
transition matrix P(1) is shortly denoted by P in the following. This transition
matrix is considered to be of type d × d. The last row contains (0, 0, . . . , 0, 1)
expressing the absorbing default state. Multi-period transition matrices can be
constructed from one-period transition matrices under the assumption of the
Markov property.
4.3.1
Time Homogeneous Markov Chain
Let {X(t)}t≥0 be a discrete-time stochastic process with countable state space.
It is called a first-order Markov chain if
P [(X(t + 1) = x(t + 1)|X(t) = x(t), . . . , X(0) = x(0)]
= P [X(t + 1) = x(t + 1)|X(t) = x(t)]
(4.16)
whenever both sides are well-defined. Further, the process is called a homoge-
neous first-order Markov chain if the right-hand side of (4.16) is independent
of t (Br´emaud, 1999).
Transferred to rating transitions, homogeneity and the Markov property imply
constant one-period transition matrices P independent of the time t, i. e. P
obeys time-stability. Then the one-period d × d transition matrix P contains
the non-negative rating transition probabilities
pjk = P(X(t + 1) = k|X(t) = j).
They fulfill the conditions
d
X
k=1
pjk = 1
and
(pd1, pd2, . . . , pdd) = (0, . . . , 0, 1).
The latter reflects the absorbing boundary of the transition matrix P.

102
4
Rating Migrations
The two-period transition matrix is then calculated by ordinary matrix mul-
tiplication, P(2) = PP. Qualitatively, the composition of the portfolio after
one period undergoes the same transitions again. Extended for m periods this
reads as
P(m) = P(m−1)P = Pm
with non-negative elements
p(m)
jk
=
d
X
i=1
p(m−1)
ji
pik.
The recursive scheme can also be applied for non-homogeneous transitions, i.e.
for one-period transition matrices being not equal, which is the general case.
4.3.2
Bootstrapping Markov Chains
The one-period transition matrix P is unknown and must be estimated. The
estimator ˆP is associated with estimation errors which consequently influence
the estimated multi-period transition matrices. The traditional approach to
quantify this influence turns out to be tedious since it is difficult to obtain
the distribution of (ˆP −P), which could characterize the estimation errors.
Furthermore, the distribution of (ˆP
(m) −P(m)), with
ˆP
(m) def
= ˆP
m,
(4.17)
has to be discussed in order to address the sensitivity of the estimated tran-
sition matrix in the multi-period case. It might be more promising to apply
resampling methods like the bootstrap combined with Monte Carlo sampling.
For a representative review of resampling techniques see Efron and Tibshirani
(1993) and Shao and Tu (1995), for bootstrapping Markov chains see Athreya
and Fuh (1992) and H¨ardle, Horowitz, and Kreiss (2001).
Assuming a homogeneous first-order Markov chain {X(t)}t≥0, the rating tran-
sitions are generated from the unknown transition matrix P. In the spirit of
the bootstrap method, the unknown transition matrix P is substituted by the
estimated transition matrix ˆP, containing transition rates. This then allows to
draw a bootstrap sample from the multinomial distribution assuming indepen-
dent rating migrations,
(˜c∗
j1, . . . , ˜c∗
jd) ∼Mult(nj; ˆpj1, . . . , ˆpjd),
(4.18)

4.3
Multi-Period Transitions
103
for all initial rating categories j = 1, . . . , d−1. Here, ˜c∗
jk denotes the bootstrap
random variable of migration counts from j to k in one period and ˆpjk is the
estimated one-period transition probability (transition rate) from j to k.
Then the bootstrap sample {c∗
jk}j=1,...,d−1,k=1,...,d is used to estimate a boot-
strap transition matrix ˆP
∗with generic elements ˆp∗
jk according
ˆp∗
jk =
c∗
jk
nj
.
(4.19)
Obviously, defaulted credits can not upgrade. Therefore, the bootstrap is not
necessary for obtaining the last row of ˆP
∗, which is (ˆp∗
d1, . . . , ˆp∗
dd) = (0, . . . , 0, 1).
Then matrix multiplication gives the m-period transition matrix estimated
from the bootstrap sample,
ˆP
∗(m) = ˆP
∗m,
with generic elements ˆp∗(m)
jk
.
We can now access the distribution of ˆP
∗(m) by Monte Carlo sampling, e. g. B
samples are drawn and labeled ˆP
∗(m)
b
for b = 1, . . . , B. Then the distribution of
ˆP
∗(m) estimates the distribution of ˆP
(m). This is justified since the consistency
of this bootstrap estimator has been proven by Basawa, Green, McCormick,
and Taylor (1990).
In order to characterize the distribution of ˆP
∗(m), the
standard deviation Std

ˆp∗(m)
jk

which is the bootstrap estimator of Std

ˆp(m)
jk

,
is estimated by
d
Std

ˆp∗(m)
jk

=
v
u
u
t
1
B −1
B
X
b=1
h
ˆp∗(m)
jk,b −ˆE

ˆp∗(m)
jk
i2
(4.20)
with
ˆE

ˆp∗(m)
jk

= 1
B
B
X
b=1
ˆp∗(m)
jk,b
for all j = 1, . . . , d −1 and k = 1, . . . , d. Here, ˆp∗(m)
jk,b is the generic element of
the b-th m-period bootstrap sample ˆP
∗(m)
b
. So (4.20) estimates the unknown
standard deviation of the m-period transition rate Std

ˆp(m)
jk

using B Monte
Carlo samples.

104
4
Rating Migrations
4.3.3
Computation and Quantlets
For time homogeneity, the m-period rating transition matrices are obtained
by the quantlet
XFGRatMig5.xpl (q = XFGRatMig5(p, m)). It computes all
t = 1, 2, . . . , m multi-period transition matrices given the one-period d×d matrix
p. Note that the output q is a d×d×m array, which can be directly visualized
by
XFGRatMig6.xpl (XFGRatMig6(q)) returning a graphical output. To vi-
sualize t-period transition matrices each with d2 elements for t = 1, . . . , m, we
plot d2 aggregated values
j −1 +
k
X
l=1
p(t)
jl ,
j, k = 1, . . . , d
(4.21)
for all t = 1, . . . , m periods simultaneously.
A typical example is shown in Figure 4.2 for the one-year transition matrix
given in Nickell et al. (2000, p. 208), which uses Moody’s unsecured bond
ratings between 31/12/1970 and 31/12/1997.
According (4.21), aggregated
values are plotted for t = 1, . . . , 10. Thereby, the transition matrix is condensed
for simplicity to 4 × 4 with only 4 basic rating categories, see the example in
Section 4.2.4. Again, the last category stands for defaulted credits. Estimation
errors are neglected in Figure 4.2.
out = VaRRatMigRateM (counts, m, B)
bootstraps m-period transition probabilities
Bootstrapping is performed by the quantlet VaRRatMigRateM. It takes as input
counts, the (d −1) × d matrix of migration counts, from which the bootstrap
sample is generated.
Further, m denotes the number of periods and B the
number of generated bootstrap samples. The result is assigned to the variable
out, which is a list of the following output:
• out.btm
the (d−1)×d×B array of bootstrapped m-period transition probabilities
• out.etm
the (d −1) × d matrix of m-period transition rates
• out.stm
the (d −1) × d matrix of estimated standard deviations of the m-period
transition rates

4.3
Multi-Period Transitions
105
2
4
6
8
10
Periods
0
0.5
1
1.5
2
2.5
3
3.5
4
4.5
Aggregations
Figure 4.2. Example for
XFGRatMig6.xpl:
Aggregated values of multi-period transition matrices.
The components of the matrices out.btm are calculated according (4.18) and
(4.19). The matrices out.etm and out.stm have components given by (4.17)
and (4.20).

106
4
Rating Migrations
To k
From j
1
2
3
4
5
6
Default
nj
1
0.51
0.40
0.09
0.00
0.00
0.00
0.00
35
2
0.08
0.62
0.19
0.08
0.02
0.01
0.00
103
3
0.00
0.08
0.69
0.17
0.06
0.00
0.00
226
4
0.01
0.01
0.10
0.64
0.21
0.03
0.00
222
5
0.00
0.01
0.02
0.19
0.66
0.12
0.00
137
6
0.00
0.00
0.00
0.02
0.16
0.70
0.12
58
Default
0.00
0.00
0.00
0.00
0.00
0.00
1.00
0
Table 4.1. German rating transition matrix (d = 7) and the number of
migrations starting from rating j = 1, . . . , d
4.3.4
Rating Transitions of German Bank Borrowers
In the following the bootstrapping is illustrated in an example. As estimator
ˆP we use the 7×7 rating transition matrix of small and medium-sized German
bank borrowers from Machauer and Weber (1998, p. 1375), shown in Table 4.1.
The data cover the period from January 1992 to December 1996.
With the quantlet VaRRatMigRateM the m-period transition probabilities are
estimated by ˆp(m)
jk
and the bootstrap estimators of their standard deviations
are calculated. This calculations are done for 1, 5 and 10 periods and B = 1000
Monte Carlo steps.
A part of the resulting output is summarized in Table
4.2, only default probabilities are considered. Note that the probabilities in
Table 4.1 are rounded and the following computations are based on integer
migration counts cjk ≈njpjk.
XFGRatMig7.xpl
4.3.5
Portfolio Migration
Based on the techniques presented in the last sections we can now tackle the
problem of portfolio migration, i. e. we can assess the distribution of n(t) credits
over the d rating categories and its evolution over periods t ∈{1, . . . m}. Here,
a stationary transition matrix P is assumed. The randomly changing number
of credits in category j at time t is labeled by ˜nj(t) and allows to define non-

4.3
Multi-Period Transitions
107
From j
ˆp(1)
jd
d
Std

ˆp∗(1)
jd

ˆp(5)
jd
d
Std

ˆp∗(5)
jd

ˆp(10)
jd
d
Std

ˆp∗(10)
jd

1
0.00
0.000
0.004
0.003
0.037
0.015
2
0.00
0.000
0.011
0.007
0.057
0.022
3
0.00
0.000
0.012
0.005
0.070
0.025
4
0.00
0.000
0.038
0.015
0.122
0.041
5
0.00
0.000
0.079
0.031
0.181
0.061
6
0.12
0.042
0.354
0.106
0.465
0.123
Table 4.2. Estimated m-period default probabilities and the bootstrap
estimator of their standard deviations for m = 1, 5, 10 periods
negative portfolio weights
˜wj(t)
def
= ˜nj(t)
n(t) ,
j = 1, . . . , d,
which are also random variables.
They can be related to migration counts
˜cjk(t) of period t by
˜wk(t + 1) =
1
n(t)
d
X
j=1
˜cjk(t)
(4.22)
counting all migrations going from any category to the rating category k. Given
the weights ˜wj(t) = wj(t) at t, the migration counts ˜cjk(t) are binomially
distributed
˜cjk(t)| ˜wj(t) = wj(t) ∼B (n(t) wj(t), pjk) .
(4.23)
The non-negative weights are aggregated in a row vector
˜w(t) = ( ˜w1(t), . . . , ˜wd(t))
and sum up to one
d
X
j=1
wj(t) = 1.
In the case of independent rating migrations, the expected portfolio weights at
t + 1 given the weights at t result from (4.22) and (4.23) as
E[ ˜w(t + 1)| ˜w(t) = w(t)] = w(t)P

108
4
Rating Migrations
and the conditional covariance matrix V [ ˜w(t + 1)| ˜w(t) = w(t)] has elements
vkl
def
=





1
n(t)
Pd
j=1 wj(t)pjk(1 −pjk)
k = l
for
−
1
n(t)
Pd
j=1 wj(t)pjkpjl
k ̸= l.
(4.24)
For m periods the multi-period transition matrix P(m) = Pm has to be used,
see Section 4.3.1. Hence, (4.22) and (4.23) are modified to
˜wk(t + m) =
1
n(t)
d
X
j=1
˜c(m)
jk (t)
and
˜c(m)
jk (t)| ˜wj(t) = wj(t) ∼B

n(t) wj(t), p(m)
jk

.
Here, c(m)
jk (t) denotes the number of credits migrating from j to k over m
periods starting in t. The conditional mean of the portfolio weights is now
given by
E[ ˜w(t + m)| ˜w(t) = w(t)] = w(t)P(m)
and the elements of the conditional covariance matrix V [ ˜w(t+m)| ˜w(t) = w(t)]
result by replacing pjk and pjl in (4.24) by p(m)
jk
and p(m)
jl .
Bibliography
Athreya, K. B. and Fuh, C. D. (1992).
Bootstrapping Markov chains, in
R. LePage and L. Billard (eds), Exploring the Limits of Bootstrap, Wi-
ley, New York, pp. 49–64.
Basawa, I. V., Green, T. A., McCormick, W. P., and Taylor, R. L. (1990).
Asymptotic bootstrap validity for finite Markov chains, Communications
in Statistics A 19: 1493–1510.
Basel Committee on Banking Supervision (2001). The Internal Ratings-Based
Approach. Consultative Document.
Bishop, Y. M. M., Fienberg, S. E., and Holland, P. W. (1975). Discrete Multi-
variate Analysis: Theory and Practice, MIT Press, Cambridge.

4.3
Multi-Period Transitions
109
Br´emaud, P. (1999). Markov Chains: Gibbs Fields, Monte Carlo Simulation,
and Queues, Springer, New York.
Crouhy, M., Galai, D., and Mark, R. (2001). Prototype risk rating system,
Journal of Banking & Finance 25: 47–95.
Davidson, J. (1994). Stochastic Limit Theory, Oxford University Press, Oxford.
Efron, B. and Tibshirani, R. J. (1993).
An Introduction to the Bootstrap,
Chapman & Hall, New York.
Finger, C. C. (1998). Extended ”constant correlations” in CreditManager 2.0,
CreditMetrics Monitor pp. 5–8. 3rd Quarter.
Gupton, G. M., Finger, C. C., and Bhatia, M. (1997). CreditMetrics - Technical
Document, J.P. Morgan.
H¨ardle, W., Horowitz, J., and Kreiss, J. P. (2001). Bootstrap Methods for
Time Series, SFB Discussion Paper, 59.
Huschens, S. and Locarek-Junge, H. (2000). Konzeptionelle und statistische
Grundlagen der portfolioorientierten Kreditrisikomessung, in A. Oehler
(ed.), Kreditrisikomanagement - Portfoliomodelle und Derivate, Sch¨affer-
Poeschel Verlag, Stuttgart, pp. 25–50.
Jarrow, R. A., Lando, D., and Turnbull, S. M. (1997). A Markov model for
the term structure of credit risk spreads, The Review of Financial Studies
10(2): 481–523.
Kim, J. (1999). Conditioning the transition matrix, Risk: Credit Risk Special
Report, October: 37–40.
Lancaster, T. (1990). The Econometric Analysis of Transition Data, Cambridge
University Press.
Machauer, A. and Weber, M. (1998). Bank behavior based on internal credit
ratings of borrowers, Journal of Banking & Finance 22: 1355–1383.
Mardia, K. V., Kent, J. T., and Bibby, J. M. (1979). Multivariate Analysis,
Academic Press, London.
Nickell, P., Perraudin, W., and Varotto, S. (2000). Stability of rating transi-
tions, Journal of Banking & Finance 24: 203–227.

110
4
Rating Migrations
Saunders, A. (1999). Credit Risk Measurement: New Approaches to Value at
Risk and Other Paradigms, Wiley, New York.
Shao, J. and Tu, D. (1995). The Jackknife and Bootstrap, Springer, New York.

5 Sensitivity analysis of credit
portfolio models
R¨udiger Kiesel and Torsten Kleinow
To assess the riskiness of credit-risky portfolios is one of the most challenging
tasks in contemporary finance. The decision by the Basel Committee for Bank-
ing Supervision to allow sophisticated banks to use their own internal credit
portfolio risk models has further highlighted the importance of a critical eval-
uation of such models. A crucial input for a model of credit-risky portfolios
is the dependence structure of the underlying obligors. We study two widely
used approaches, namely a factor structure and the direct specification of a
copula, within the framework of a default-based credit risk model. Using the
powerful simulation tools of XploRe we generate portfolio default distributions
and study the sensitivity of commonly used risk measures with respect to the
approach in modelling the dependence structure of the portfolio.
5.1
Introduction
Understanding the principal components of portfolio credit risk and their in-
teraction is of considerable importance. Investment banks use risk-adjusted
capital ratios such as risk-adjusted return on capital (RAROC) to allocate eco-
nomic capital and measure performance of business units and trading desks.
The current attempt by the Basel Committee for Banking Supervision in its
Basel II proposals to develop an appropriate framework for a global financial
regulation system emphasizes the need for an accurate understanding of credit
risk; see BIS (2001). Thus bankers, regulators and academics have put con-
siderable effort into attempts to study and model the contribution of various
ingredients of credit risk to overall credit portfolio risk. A key development
has been the introduction of credit portfolio models to obtain portfolio loss
distributions either analytically or by simulation. These models can roughly

112
5
Sensitivity analysis of credit portfolio models
be classified as based on credit rating systems, on Merton’s contingent claim
approach or on actuarial techniques; see Crouhy, Galai and Mark (2001) for
exact description and discussion of the various models.
However, each model contains parameters that effect the risk measures pro-
duced, but which, because of a lack of suitable data, must be set on a judge-
mental basis. There are several empirical studies investigating these effects:
Gordy (2000) and Koyluoglu and Hickmann (1998) show that parametrisation
of various models can be harmonized, but use only default-driven versions (a
related study with more emphasis on the mathematical side of the models is
Frey and McNeil (2001)). Crouhy, Galai and Mark (2000) compare models
on benchmark portfolio and find that the highest VaR estimate is 50 per cent
larger than the lowest. Finally, Nickell, Perraudin and Varotto (1998) find that
models yield too many exceptions by analyzing VaRs for portfolios over rolling
twelve-month periods.
Despite these shortcomings credit risk portfolio models are regarded as valu-
able tools to measure the relative riskiness of credit risky portfolios – not least
since measures such as e.g. the spread over default-free interest rate or default
probabilities calculated from long runs of historical data suffer from other in-
trinsic drawbacks – and are established as benchmark tools in measuring credit
risk.
The calculation of risk capital based on the internal rating approach, currently
favored by the Basel Supervisors Committee, can be subsumed within the class
of ratings-based models. To implement such an approach an accurate under-
standing of various relevant portfolio characteristics within such a model is
required and, in particular, the sensitivity of the risk measures to changes in
input parameters needs to be evaluated. However, few studies have attempted
to investigate aspects of portfolio risk based on rating-based credit risk models
thoroughly. In Carey (1998) the default experience and loss distribution for
privately placed US bonds is discussed. VaRs for portfolios of public bonds,
using a bootstrap-like approach, are calculated in Carey (2000). While these
two papers utilize a ”default-mode” (abstracting from changes in portfolio value
due to changes in credit standing), Kiesel, Perraudin and Taylor (1999) employ
a ”mark-to-market” model and stress the importance of stochastic changes in
credit spreads associated with market values – an aspect also highlighted in
Hirtle, Levonian, Saidenberg, Walter and Wright (2001).
The aim of this chapter is to contribute to the understanding of the performance
of rating-based credit portfolio models.
Our emphasis is on comparing the
effect of the different approaches to modelling the dependence structure of

5.2
Construction of portfolio credit risk models
113
the individual obligors within a credit-risky portfolio. We use a default-mode
model (which can easily be extended) to investigate the effect of changing
dependence structure within the portfolio. We start in Section 5.2 by reviewing
the construction of a rating-based credit portfolio risk model. In Section 5.3 we
discuss approaches to modelling dependence within the portfolio. In Section
5.4 we comment on the implementation in XploRe and present results from our
simulations.
5.2
Construction of portfolio credit risk models
To construct a credit risk model we have to consider individual risk elements
such as
(1i) Default Probability: the probability that the obligor or counterparty will
default on its contractual obligations to repay its debt,
(2i) Recovery Rates: the extent to which the face value of an obligation can
be recovered once the obligor has defaulted,
(3i) Credit Migration: the extent to which the credit quality of the obligor or
counterparty improves or deteriorates;
and portfolio risk elements
(1p) Default and Credit Quality Correlation: the degree to which the default
or credit quality of one obligor is related to the default or credit quality
of another,
(2p) Risk Contribution and Credit Concentration: the extent to which an indi-
vidual instrument or the presence of an obligor in the portfolio contributes
to the totality of risk in the overall portfolio.
From the above building blocks a rating-based credit risk model is generated
by
(1m) the definition of the possible states for each obligor’s credit quality, and
a description of how likely obligors are to be in any of these states at the
horizon date, i.e. specification of rating classes and of the corresponding
matrix of transition probabilities (relating to (1i) and (3i)).

114
5
Sensitivity analysis of credit portfolio models
(2m) quantifying the interaction and correlation between credit migrations of
different obligors (relating to (1p)).
(3m) the re-evaluation of exposures in all possible credit states, which in case of
default corresponds to (2i) above; however, for non-default states a mark-
to-market or mark-to-model (for individual assets) procedure is required.
During this study we will focus on the effects of default dependence modelling.
Furthermore, we assume that on default we are faced with a zero recovery rate.
Thus, only aspects (1i) and (1p) are of importance in our context and only
two rating classes – default and non-default – are needed. A general discussion
of further aspects can be found in any of the books Caouette, Altman and
Narayanan (1998), Ong (1999), Jorion (2000) and Crouhy et al. (2001). For
practical purposes we emphasize the importance of a proper mark-to-market
methodology (as pointed out in Kiesel et al. (1999)). However, to study the
effects of dependence modelling more precisely, we feel a simple portfolio risk
model is sufficient.
As the basis for comparison we use Value at Risk (VaR) – the loss which will
be exceeded on some given fractions of occasions (the confidence level) if a
portfolio is held for a particular time (the holding period).
5.3
Dependence modelling
To formalize the ratings-based approach, we characterize each exposure j ∈
{1, . . . , n} by a four-dimensional stochastic vector
(Sj, kj, lj, π(j, kj, lj)),
where for obligor j
(1) Sj is the driving stochastic process for defaults and rating migrations,
(2) kj, lj represent the initial and end-of-period rating category,
(3) π(.) represents the credit loss (end-of-period exposure value).
In this context Sj (which is, with reference to the Merton model, often in-
terpreted as a proxy of the obligor’s underlying equity) is used to obtain the
end-of-period state of the obligor. If we assume N rating classes, we obtain

5.3
Dependence modelling
115
cut-offpoints −∞= zk,0, zk,1, zk,2, . . . , zk,N−1, zk,N = ∞using the matrix of
transition probabilities together with a distributional assumption on Sj. Then,
obligor j changes from rating k to rating l if the variable Sj falls in the range
[zk,l−1, zkl]. Our default-mode framework implies two rating classes, default
resp. no-default, labeled as 1 resp. 0 (and thus only a single cut-offpoint
obtained from the probability of default). Furthermore, interpreting π(•) as
the individual loss function, π(j, 0, 0) = 0 (no default) and according to our
zero recovery assumption π(j, 0, 1) = 1. To illustrate the methodology we plot
in Figure 5.1 two simulated drivers S1 and S2 together with the corresponding
cut-offpoints z1,1 and z2,1.
0.62
0.96
1.30
1.64
50.00
100.00
150.00
200.00
250.00
Figure 5.1.
Two simulated driver Sj and the corresponding cut-off
points for default.
XFGSCP01.xpl
5.3.1
Factor modelling
In a typical credit portfolio model dependencies of individual obligors are mod-
elled via dependencies of the underlying latent variables S = (S1, . . . , Sn)⊤. In
the typical portfolio analysis the vector S is embedded in a factor model, which
allows for easy analysis of correlation, the typical measure of dependence. One
assumes that the underlying variables Sj are driven by a vector of common

116
5
Sensitivity analysis of credit portfolio models
factors. Typically, this vector is assumed to be normally distributed (see e.g.
JP Morgan (1997)).
Thus, with Z ∼N(0, Σ) a p-dimensional normal vec-
tor and ϵ = (ϵ1, . . . , ϵn)⊤independent normally distributed random variables,
independent also from Z, we define
Sj =
p
X
i=1
ajiZi + σjϵj, j = 1, . . . n.
(5.1)
Here aji describes the exposure of obligor j to factor i, i.e. the so-called factor
loading, and σj is the volatility of the idiosyncratic risk contribution. In such
a framework one can easily interfere default correlation from the correlation of
the underlying drivers Sj. To do so, we define default indicators
Yj = 1(Sj ≤Dj),
where Dj is the cut-offpoint for default of obligor j. The individual default
probabilities are
πj = P(Yj = 1) = P(Sj ≤Dj),
and the joint default probability is
πij = P(Yi = 1, Yj = 1) = P(Si ≤Di, Sj ≤Dj).
If we denote by ρij = Corr(Si, Sj) the correlation of the underlying latent
variables and by ρD
ij = Corr(Yi, Yj) the default correlation of obligors i and j,
then we obtain for the default correlation the simple formula
ρD
ij =
πij −πiπj
p
πiπj(1 −πi)(1 −πj)
.
(5.2)
Under the assumption that (Si, Sj) are bivariate normal, we obtain for the joint
default probability
πij =
Z Di
−∞
Z Dj
−∞
ϕ(u, v; ρij)dudv,
where ϕ(u, v; ρ) is bivariate normal density with correlation coefficient ρ. Thus,
asset (factor) correlation influences default correlation by entering in joint de-
fault probability. Within the Gaussian framework we can easily evaluate the
above quantities, see (5.1). We see, that under our modelling assumption de-
fault correlation is of an order of magnitude smaller than asset correlation
(which is also supported by empirical evidence).

5.3
Dependence modelling
117
Asset correlation
Default correlation
0.1
0.0094
0.2
0.0241
0.3
0.0461
Table 5.1. Effect of asset correlation on default correlation
5.3.2
Copula modelling
As an alternative approach to the factor assumption, we can model each of the
underlying variables independently and subsequently use a copula to generate
the dependence structure. (For basic facts on copulae we refer the reader to
Chapter 2 and the references given there.)
So, suppose we have specified the individual distributions Fj of the variables
Sj and a copula C for the dependence structure. Then, for any subgroup of
obligors {j1, . . . , jm}, we have for the joint default probability
P (Yj1 = 1, . . . , Yjm = 1)
=
P (Sj1 ≤Dj1, . . . , Sjm ≤Djm)
=
Cj1,...,jm {Fj1(Dj1), . . . , Fjm(Djm)} ,
where we denote by Cj1,...,jm the m-dimensional margin of C. In particular,
the joint default probability of two obligors is now
πij = Ci,j {Fi(Di), Fj(Dj)} .
To study the effect of different copulae on default correlation, we use the fol-
lowing examples of copulae (further details on these copulae can be found in
Embrechts, Lindskog and McNeil (2001)).
1. Gaussian copula:
CGauss
R
(u) = Φn
R(Φ−1(u1), . . . , Φ−1(un)).
Here Φn
R denotes the joint distribution function of the n-variate normal
with linear correlation matrix R, and Φ−1 the inverse of the distribution
function of the univariate standard normal.

118
5
Sensitivity analysis of credit portfolio models
2. t-copula:
Ct
ν,R(u) = tn
ν,R(t−1
ν (u1), . . . , t−1
ν (un)),
where tn
ν,R denotes the distribution function of an n-variate t-distributed
random vector with parameter ν > 2 and linear correlation matrix R.
Furthermore, tν is the univariate t-distribution function with parameter
ν.
3. Gumbel copula:
CGumbel
θ
(u) = exp
n
−[(−log u1)θ + . . . + (−log un)θ]1/θo
,
where θ ∈[1, ∞).
This class of copulae is a sub-class of the class of
Archimedean copulae. Furthermore, Gumbel copulae have applications
in multivariate extreme-value theory.
In Table 5.2 joint default probabilities of two obligors are reported using three
types of obligors with individual default probabilities roughly corresponding
to rating classes A,B,C. We assume that underlying variables S are univariate
normally distributed and model the joint dependence structure using the above
copulae.
Copula
Default probability
class A (×10−6)
class B (×10−4)
class C (×10−4)
Gaussian
6.89
3.38
52.45
Ct
10
46.55
7.88
71.03
Ct
4
134.80
15.35
97.96
Gumbel, C2
57.20
14.84
144.56
Gumbel, C4
270.60
41.84
283.67
Table 5.2. Copulae and default probabilities
The computation shows that t and Gumbel copulae have higher joint default
probabilities than the Gaussian copula (with obvious implication for default
correlation, see equation (5.2)). To explain the reason for this we need the
concept of tail dependence:
DEFINITION 5.1 Let X and Y be continuous random variables with distri-
bution functions F and G. The coefficient of upper tail dependence of X and
Y is
lim
u→1 P[Y > G−1(u)|X > F −1(u)] = λU
(5.3)

5.4
Simulations
119
provided that the limit λU ∈[0, 1] exists. If λU ∈(0, 1], X and Y are said to
be asymptotically dependent in the upper tail; if λU = 0, X and Y are said to
be asymptotically independent in the upper tail.
For continuous distributions F and G one can replace (5.3) by a version involv-
ing the bivariate copula directly:
lim
u→1
1 −2u + C(u, u)
1 −u
= λU.
(5.4)
Lower tail dependence, which is more relevant to our current purpose, is defined
in a similar way. Indeed, if
lim
u→0
C(u, u)
u
= λL
(5.5)
exists, then C exhibits lower tail dependence if λL ∈(0, 1], and lower tail
independence if λL = 0.
It can be shown that random variables linked by Gaussian copulae have no
tail-dependence, while the use of tν and the Gumbel copulae results in tail-
dependence. In fact, in case of the tν copula, we have increasing tail dependence
with decreasing parameter ν, while for the Gumbel family tail dependence
increases with increasing parameter θ.
5.4
Simulations
The purpose here is to generate portfolios with given marginals (normal) and
the above copulae. We focus on the Gaussian and t-copula case.
5.4.1
Random sample generation
For the generation of an n-variate Normal with linear correlation matrix R,
(x1, . . . , xn)⊤∼N(0, R), we apply the quantlet gennorm. To obtain realizations
from a Gaussian copula we simply have to transform the marginals:
• Set ui = Φ(xi), i = 1, . . . , n.
• (u1, . . . , un)⊤∼CGauss
R
.

120
5
Sensitivity analysis of credit portfolio models
To generate random variates from the t-copula Ct
ν,R we recall that if the random
vector X admits the stochastic representation
X = µ +
r ν
Z Y
(in distribution),
(5.6)
with µ ∈Rn, Z ∼χ2
ν and Y ∼N(0, Σ), where Z and Y are independent, then
X is tν distributed with mean µ and covariance matrix
ν
ν−2Σ. Here we assume
as above, that ν > 2. While the stochastic representation (5.6) is still valid, the
interpretation of the parameters has to change for ν ≤2. Thus, the following
algorithm can be used (this is Algorithm 5.2 in Embrechts et al. (2001)):
• Simulate x = (x1, . . . , xn)⊤∼N(0, R) using gennorm.
• Simulate a random variate z from χ2
ν independent of y1, . . . , yn.
• Set x = p ν
z .
• Set ui = tν(xi), i = 1, . . . , n.
• (u1, . . . , un)⊤∼Ct
ν,R.
Having obtained the t-copula Ct
ν,R, we only need to replace the ui with Φ−1(ui)
in order to have a multivariate distribution with t-copula and normal marginals.
The implementation of these algorithms in XploRe is very straightforward. In-
deed, using the quantlet normal we can generate normally distributed random
variables. Naturally all the distribution functions needed are also implemented,
cdfn, cdft etc.
5.4.2
Portfolio results
We simulate standard portfolios of size 500 with all obligors belonging to one
rating class.
We use three rating classes, named A,B,C with default prob-
abilities 0.005, 0.05, 0.15 roughly corresponding to default probabilities from
standard rating classes, Ong (1999), p. 77.
For our first simulation exercise we assume that the underlying variables Sj
are normally distributed within a single factor framework, i.e. p = 1 in (5.1).
The factor loadings aj1 in (5.1) are constant and chosen so that the correlation
for the underlying latent variables Sj is ρ = 0.2, which is a standard baseline

5.4
Simulations
121
value for credit portfolio simulations, Kiesel et al. (1999). To generate different
degrees of tail correlation, we link the individual assets together using a Gaus-
sian, a t10 and a t4-copula as implemented in VaRcredN and VaRcredTcop.
out = VaRcredN (d, p, rho, opt)
simulates the default distribution for a portfolio of d homogeneous
obligors assuming a Gaussian copula.
out = VaRcredTcop (d, p, rho, df, opt)
simulates the default distribution for a portfolio of d homogeneous
obligors assuming a t-copula with df degrees of freedom.
The default driver Sj are normal for all obligors j in both quantlets. p de-
notes the default probability πj of an individual obligor and rho is the asset
correlation ρ. opt is an optional list parameter consisting of opt.alpha, the
significance level for VaR estimation and opt.nsimu, the number of simula-
tions. Both quantlets return a list containing the mean, the variance and the
opt.alpha-quantile of the portfolio default distribution.
VaR
Portfolio
Copula
α = 0.95
α = 0.99
A
Normal
10
22
t10
14
49
t4
10
71
B
Normal
77
119
t10
95
178
t4
121
219
C
Normal
182
240
t10
198
268
t4
223
306
Table 5.3. Effect of different copulae
XFGSCP02.xpl
The most striking observation from Table 5.3 is the effect tail-dependence has
on the high quantiles of highly-rated portfolios: the 99%-quantile for the t4-
copula is more than 3-times larger than the corresponding quantile for the
Gaussian copula. The same effect can be observed for lower rated portfolios

122
5
Sensitivity analysis of credit portfolio models
although not quite with a similar magnitude.
To assess the effects of increased correlation within parts of the portfolio, we
change the factor loading within parts of our portfolio. We assume a second
factor, i.e. p = 2 in (5.1), for a sub-portfolio of 100 obligors increasing the
correlation of the latent variables Sj within the sub-portfolio to 0.5. In the
simulation below, the quantlets VaRcredN2 and VaRcredTcop2 are used.
out = VaRcredN2 (d1, d2, p, rho1, rho2, opt)
simulates the default distribution for a portfolio consisting of two
homogeneous subportfolios using a Gaussian copula.
out = VaRcredTcop2 (d1, d2, p, rho1, rho2, df, opt)
simulates the default distribution for a portfolio consisting of two
homogeneous subportfolios using a t-copula with df degrees of
freedom.
The number of obligors in the first (second) subportfolio is d1 (d2).
rho1
(rho2) is the asset correlation generated by the first (second) factor. The other
parameters correspond to the parameters in VaRcredN and VaRcredTcop.
Such a correlation cluster might be generated by a sector or regional exposure
for a real portfolio. Again, degrees of tail correlation are generated by using
a Gaussian, a t10 and a t4-copula. As expected the results in Table 5.4 show
a slight increase in the quantiles due to the increased correlation within the
portfolio. However, comparing the two tables we see that the sensitivity of the
portfolio loss quantiles is far higher with regard to the underlying copula – and
its corresponding tail dependence – than to the correlation within the portfolio.
Our simulation results indicate that the degree of tail dependence of the un-
derlying copula plays a major role as a credit risk characteristicum.
Thus,
while analysis of the driving factors for the underlying variables (obligor eq-
uity, macroeconomic variables, ..) remains an important aspect in modelling
credit risky portfolio, the copula linking the underlying variables together is of
crucial importance especially for portfolios of highly rated obligors.

5.4
Simulations
123
VaR
Portfolio
Copula
α = 0.95
α = 0.99
A
Normal
10
61
t10
9
61
t4
5
60
B
Normal
161
318
t10
157
344
t4
176
360
C
Normal
338
421
t10
342
426
t4
350
432
Table 5.4. Effect of correlation cluster
XFGSCP03.xpl
Bibliography
BIS (2001). Overview of the new Basel capital accord, Technical report, Basel
Committee on Banking Supervision.
Caouette, J., Altman, E. and Narayanan, P. (1998). Managing Credit Risk, The
Next Great Financial Challenge, Wiley Frontiers in Finance, Vol. Wiley
Frontiers in Finance, Wiley & Sons, Inc, New York.
Carey, M. (1998). Credit risk in private debt portfolios, Journal of Finance
53(4): 1363–1387.
Carey, M. (2000). Dimensions of credit risk and their relationship to economic
capital requirements. Preprint, Federal Reserve Board.
Crouhy, M., Galai, D. and Mark, R. (2000). A comparative analysis of current
credit risk models, Journal of Banking and Finance 24(1-2): 59–117.
Crouhy, M., Galai, D. and Mark, R. (2001). Risk management, McGraw Hill.
Embrechts, P., Lindskog, F. and McNeil, A. (2001). Modelling dependence
with copulas and applications to risk management. Working paper, ETH
Z¨urich.
Frey, R. and McNeil, A. (2001). Modelling dependent defaults. Working paper,
ETH Z¨urich.

124
5
Sensitivity analysis of credit portfolio models
Gordy, M. (2000). A comparative anatomy of credit risk models, Journal of
Banking and Finance 24: 119–149.
Hirtle, B., Levonian, M., Saidenberg, M., Walter, S. and Wright, D. (2001). Us-
ing credit risk models for regulartory capital: Issues and options, FRBNY
Economic Policy Review 6(2): 1–18.
Jorion, P. (2000). Value at Risk, 2nd. edn, McGraw-Hill, New York.
JP Morgan (1997). Creditmetrics-Technical Document, JP Morgan, New York.
Kiesel, R., Perraudin, W. and Taylor, A. (1999). The structure of credit risk.
Preprint, Birkbeck College.
Koyluoglu, H. and Hickmann, A. (1998). A generalized framework for credit
portfolio models. Working Paper, Oliver, Wyman & Company.
Nickell, P., Perraudin, W. and Varotto, S. (1998). Ratings-versus equity-based
credit risk models: An empirical investigation. unpublished Bank of Eng-
land mimeo.
Ong, M. (1999). Internal Credit Risk Models. Capital Allocation and Perfor-
mance Measurement, Risk Books, London.

Part III
Implied Volatility


6 The Analysis of Implied
Volatilities
Matthias R. Fengler, Wolfgang H¨ardle and Peter Schmidt
The analysis of volatility in financial markets has become a first rank issue in
modern financial theory and practice: Whether in risk management, portfolio
hedging, or option pricing, we need to have a precise notion of the market’s
expectation of volatility. Much research has been done on the analysis of real-
ized historic volatilities, Roll (1977) and references therein. However, since it
seems unsettling to draw conclusions from past to expected market behavior,
the focus shifted to implied volatilities, Dumas, Fleming and Whaley (1998).
To derive implied volatilities the Black and Scholes (BS) formula is solved for
the constant volatility parameter σ using observed option prices. This is a more
natural approach as the option value is decisively determined by the market’s
assessment of current and future volatility. Hence implied volatility may be
used as an indicator for market expectations over the remaining lifetime of the
option.
It is well known that the volatilities implied by observed market prices exhibit
a pattern that is far different from the flat constant one used in the BS formula.
Instead of finding a constant volatility across strikes, implied volatility appears
to be non flat, a stylized fact which has been called ”smile”effect.
In this
chapter we illustrate how implied volatilites can be analyzed. We focus first
on a static and visual investigation of implied volatilities, then we concentrate
on a dynamic analysis with two variants of principal components and interpret
the results in the context of risk management.

128
6
The Analysis of Implied Volatilities
6.1
Introduction
Implied volatilities are the focus of interest both in volatility trading and in
risk management.
As common practice traders directly trade the so called
”vega”, i.e. the sensitivity of their portfolios with respect to volatility changes.
In order to establish vega trades market professionals use delta-gamma neutral
hedging strategies which are insensitive to changes in the underlying and to time
decay, Taleb (1997). To accomplish this, traders depend on reliable estimates
of implied volatilities and - most importantly - their dynamics.
One of the key issues in option risk management is the measurement of the
inherent volatility risk, the so called ”vega” exposure. Analytically, the ”vega”
is the first derivative of the BS formula with respect to the volatility parameter
σ, and can be interpreted as a sensitivity of the option value with respect to
changes in (implied) volatility. When considering portfolios composed out of
a large number of different options, a reduction of the risk factor space can
be very useful for assessing the riskiness of the current position. H¨ardle and
Schmidt (2002) outline a procedure for using principal components analysis
(PCA) to determine the maximum loss of option portfolios bearing vega expo-
sure. They decompose the term structure of DAX implied volatilities ”at the
money” (ATM) into orthogonal factors. The maximum loss, which is defined
directly in the risk factor space, is then modeled by the first two factors.
Our study on DAX options is organized as follows: First, we show how to de-
rive and to estimate implied volatilities and the implied volatility surface. A
data decription follows. In section 6.3.2, we perfom a standard PCA on the co-
variance matrix of VDAX returns to identify the dominant factor components
driving term structure movements of ATM DAX options. Section 6.3.3 intro-
duces a common principal components approach that enables us to model not
only ATM term structure movements of implied volatilities but the dynamics
of the ”smile” as well.

