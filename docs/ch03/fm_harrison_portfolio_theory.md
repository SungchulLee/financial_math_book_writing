# Portfolio Theory & the CAPM

!!! info "Source"
    **Mathematical Economics and Finance** by Michael Harrison and Patrick Waldron, 1998.
    These notes are used for educational purposes.

## Portfolio Theory

CHAPTER 5. CHOICE UNDER UNCERTAINTY
103
which implies:
E\[u( ˜W)]
=
u(E\[ ˜W]) + 1
2u′′(E\[ ˜W])σ2( ˜W) + E\[R3]
(5.8.3)
where
E\[R3]
=
∞
X
n=3
1
n!u(n)(E\[ ˜W])mn( ˜W)
(5.8.4)
It follows that the sign of the nth derivative of the utility function determines
the direction of preference for the nth central moment of the probability
distribution of terminal wealth. For example, a positive third derivative im-
plies a preference for greater skewness. It can be shown fairly easily that
an increasing utility function which exhibits non-increasing absolute risk
aversion has a non-negative third derivative.
2. Quadratic utility:
E\[u( ˜W)]
=
E\[ ˜W] −b
2E\[ ˜W 2]
(5.8.5)
=
E\[ ˜W] −b
2

(E\[ ˜W])2 + σ2( ˜W)

(5.8.6)
=
u(E\[ ˜W]) −b
2Var\[ ˜W]
(5.8.7)
3. Normally distributed asset returns.
Note that the expected utility axioms are neither necessary nor sufficient to guar-
antee that the Taylor approximation to n moments is a valid representation of the
utility function. Some counterexamples of both types are probably called for here,
or maybe can be left as exercises.
Extracts from my PhD thesis can be used to talk about signing the first three
coefficients in the Taylor expansion, and to speculate about further extensions to
higher moments.
5.9
The Kelly Strategy
In a multi-period, discrete time, investment framework, investors will be con-
cerned with both growth (return) and security (risk). There will be a trade-off
between the two, and investors will be concerned with finding the optimal trade-
off. This, of course, depends on preferences, but some useful benchmarks exist.
There are three ways of measuring growth:
1. the expected wealth at time t
Revised: December 2, 1998

104
5.10. ALTERNATIVE NON-EXPECTED UTILITY APPROACHES
2. the expected rate of growth of wealth up to time t
3. the expected first passage time to reach a critical level of wealth, say £1m
Likewise, there are three ways of measuring security:
1. the probability of reaching a critical level of wealth, say £1m, by a specific
time t
2. the probability that the wealth process lies above some critical path, say
above bt at time t, t = 1, 2, . . .
3. the probability of reaching some goal U before falling to some low level of
wealth L
It can be shown that the ? strategy both maximises the long run exponential
growth rate and minimises the expected time to reach large goals.
All this is also covered in ? which is reproduced in ?.
5.10
Alternative Non-Expected Utility Approaches
Those not happy with the explanations of choice under uncertainty provided within
the expected utility paradigm have proposed various alternatives in recent years.
These include both vague qualitative waffle about fun and addiction and more for-
mal approaches looking at maximum or minimum possible payoffs, irrational ex-
pectations, etc. Before proceeding, the reader might want to review Section 3.2.
Revised: December 2, 1998

CHAPTER 6. PORTFOLIO THEORY
105
Chapter 6
PORTFOLIO THEORY
6.1
Introduction
Portfolio theory is an important topic in the theory of choice under uncertainty. It
deals with the problem facing an investor who must decide how to distribute an
initial wealth of, say, W0 among a number of single-period investment opportuni-
ties, called securities or assets.
The choice of portfolio will depend on both the investor’s preferences and his
beliefs about the uncertain payoffs of the various securities. A mutual fund is just
a special type of (managed) portfolio.
The chapter begins by considering some issues of definition and measurement.
Section 6.3 then looks at the portfolio choice problem in a general expected utility
context. Section 6.4 considers the same problem from a mean-variance perspec-
tive. This leads on to a discussion of the properties of equilibrium security returns
in Section 6.5.
6.2
Notation and preliminaries
6.2.1
Measuring rates of return
Good background reading for this section is ?.
A rate of interest (growth, inflation, &c.) is not properly defined unless we state
the time period to which it applies and the method of compounding to be used.
2% per annum is very different from 2% per month.
Table 6.1 illustrates what happens to £100 invested at 10% per annum as we
change the interval of compounding. The final calculation in the table uses the
Revised: December 2, 1998

106
6.2. NOTATION AND PRELIMINARIES
Compounded
Annually
£100
→
£110
Semi-annually
£100
→
£100 × (1.05)2 = £110.25
Quarterly
£100
→
£100 × (1.025)4 = £110.381. . .
Monthly
£100
→
£100 ×

1 + .10
12
12 = £110.471. ..
Weekly
£100
→
£100 ×

1 + .10
52
52 = £110.506. ..
Daily
£100
→
£100 ×

1 + .10
365
365 = £110.515. . .
Continuously
£100
→
£100 × e0.10 = £110.517. ..
Table 6.1: The effect of an interest rate of 10% per annum at different frequencies
of compounding.
fact that
lim
n→∞

1 + r
n
n
= er
where e ≈2.7182...
This is sometimes used as the definition of e but others prefer to start with
er ≡1 + r + r2
2! + r3
3! + . . . =
∞
X
j=0
rj
j!
where n! ≡n (n −1) (n −2) . . . 3.2.1 and 0! ≡1 by convention.
There are five concepts which we need to be familiar with:
1. Discrete compounding:
Pt =

1 + r
n
nt
P0.
We can solve this equation for any of five quantities given the other four:
(a) present value
(b) final value
(c) implicit rate of return
(d) time
(e) interval of compounding
Revised: December 2, 1998

CHAPTER 6. PORTFOLIO THEORY
107
2. Continuous compounding:
Pt = ertP0.
We can solve this equation for any of four quantities given the other three
((a)–(d) above).
Note also that the exponential function is its own derivative; that y = 1+r is
the tangent to y = er at r = 0 and hence that er > 1 + r ∀r. In other words,
given an initial value, continuous compounding yields a higher terminal
value than discrete compounding for all interest rates, positive and negative,
with equality for a zero interest rate only. Similarly, given a final value,
continuous discounting yields a higher present value than does discrete.
3. Aggregating and averaging returns across portfolios (˜rw = w⊤˜r) and over
time:
Pt
=
ertP0
Pt+∆t
=
er∆tPt
r
=
ln Pt+∆t −ln Pt
∆t
r(s)
=
d ln Ps
ds
Z t
0 r(s)ds
=
Z t
0 d ln Ps = ln Pt −ln P0
Pt
=
P0e
R t
0 r(s)ds
Discretely compounded rates aggregate nicely across portfolios; continu-
ously compounded rates aggregate nicely across time.
4. The (net) present value (NPV) of a stream of cash flows,
P0, P1, . . . , PT
is
NPV (r) ≡
P0
(1 + r)0 +
P1
(1 + r)1 +
P2
(1 + r)2 + . . . +
PT
(1 + r)T .
5. The internal rate of return (IRR) of the stream of cash flows,
P0, P1, . . . , PT,
is the solution of the polynomial of degree T obtained by setting the NPV
equal to zero:
P0
(1 + r)0 +
P1
(1 + r)1 +
P2
(1 + r)2 + . . . +
PT
(1 + r)T = 0.
Revised: December 2, 1998

108
6.2. NOTATION AND PRELIMINARIES
W0
=
the investor’s initial wealth
W1
=
the investor’s desired expected final wealth
N
=
number of risky assets
rf
=
return on the riskfree asset
˜rj ∈ℜ
=
return on jth risky asset
˜r ∈ℜN
=
(˜r1, . . . , ˜rN)
e = E\[˜r] ∈ℜN
=
vector of expected returns
V ∈ℜN×N
=
variance-covariance matrix of returns
1
=
(1, 1, . . . , 1)
=
N-dimensional vector of 1s
wj ∈ℜ
=
amount invested in jth risky asset
w ∈ℜN
=
(w1, . . . , wn)
˜rw = w⊤˜r
=
return on the portfolio w
µ ≡E\[˜rw] ≡W1
W0 ∈ℜ
=
the investor’s desired expected return
Table 6.2: Notation for portfolio choice problem
In general, the polynomial defining the IRR has T (complex) roots. Condi-
tions have been derived under which there is only one meaningful real root
to this polynomial equation, in other words one corresponding to a positive
IRR.1
Consider a quadratic example.
Simple rates of return are additive across portfolios, so we use them in one period
cross sectional studies, in particular in this chapter.
Continuously compounded rates of return are additive across time, so we use them
in multi-period single variable studies, such as in Chapter 7.
Consider as an example the problem of calculating mortgage repayments.
6.2.2
Notation
The investment opportunity set for the portfolio choice problem will generally
consist of N risky assets. From time to time, we will add a riskfree asset. The
notation used throughout this chapter is set out in Table 6.2. The presentation
is in terms of a single period problem, and the unconditional distribution of re-
turns. The analysis of the multiperiod, infinite horizon, discrete time problem,
concentrating on the conditional distribution of the next period’s returns given
this period’s, is quite similar.2
1These conditions are discussed in ?.
2Make this into an exercise.
Revised: December 2, 1998

CHAPTER 6. PORTFOLIO THEORY
109
Definition 6.2.1 w is said to be a unit cost or normal portfolio if its weights sum
to 1 (w⊤1 = 1).
The portfolio held by an investor with initial wealth W0 can be thought of either
as a w with w⊤1 = W0 or as the corresponding normal portfolio,
1
W0w. It will
hopefully be clear from the context which meaning of ‘portfolio’ is intended.
Definition 6.2.2 w is said to be a zero cost or hedge portfolio if its weights sum
to 0 (w⊤1 = 0).
The vector of net trades carried out by an investor moving from the portfolio w0
to the portfolio w1 can be thought of as the hedge portfolio w1 −w0.
Definition 6.2.3 Short-selling a security means owning a negative quantity of it.
In practice short-selling means promising (credibly) to pay someone the same cash
flows as would be paid by a security that one does not own, always being prepared,
if required, to pay the current market price of the security to end the arrangement.
Thus when short-selling is allowed w can have negative components; if short-
selling is not allowed, then the portfolio choice problem will have non-negativity
constraints, wi ≥0 for i = 1, . . . , N.
A number of further comments are in order at this stage.
1. In the literature, initial wealth is often normalised to unity (W0 = 1), but
the development of the theory will be more elegant if we avoid this.
2. Since we will be dealing on occasion with hedge portfolios, we will in future
avoid the concepts of rate of return and net return, which are usually thought
of as the ratio of profit to initial investment. These terms are meaningless
for a hedge portfolio as the denominator is zero.
Instead, we will speak of the gross return on a portfolio or the portfolio pay-
off. This can be defined unambiguously as follows. There is no ambiguity
about the payoff on one of the original securities, which is just the gross
return per pound invested. The payoff on a unit cost or normal portfolio
is equivalent to the gross return. It is just w⊤˜r. The payoff on a zero cost
portfolio can also be defined as w⊤˜r.
Note that where we initially worked with net rates of return ( P1
P0 −1), we
will deal henceforth with gross rates of return (P1
P0).
Revised: December 2, 1998

110
6.3. THE SINGLE-PERIOD PORTFOLIO CHOICE PROBLEM
6.3
The Single-period Portfolio Choice Problem
6.3.1
The canonical portfolio problem
Unless otherwise stated, we assume that individuals:
1. have von Neumann-Morgenstern (VNM) utilities:
i.e. preferences have the expected utility representation:
v(˜z)
=
E\[u(˜z)]
=
Z
u(z)dF˜z(z)
where v is the utility function for random variables (gambles, lotteries)
and u is the utility function for sure things.
2. prefer more to less
i.e. u is increasing:
u ′(z) > 0 ∀z
(6.3.1)
3. are (strictly) risk-averse
i.e. u is strictly concave:
u ′′(z) < 0 ∀z
(6.3.2)
Date 0 investment:
• wj (pounds) in jth risky asset, j = 1, . . . , N
• (W0 −
P
j wj) in risk free asset
Date 1 payoff:
• wj˜rj from jth risky asset
• (W0 −
P
j wj)rf from risk free asset
It is assumed here that there are no constraints on short-selling or borrowing
(which is the same as short-selling the riskfree security).
The solution is found as follows:
Choose wjs to maximize expected utility of date 1 wealth,
˜W
=
(W0 −
X
j
wj)rf +
X
j
wj˜rj
=
W0rf +
X
j
wj(˜rj −rf)
Revised: December 2, 1998

CHAPTER 6. PORTFOLIO THEORY
111
i.e.
max
{wj} f (w1, . . . , wN) ≡E\[u(W0rf +
X
j
wj(˜rj −rf))]
The first order conditions are:
E\[u′( ˜W)(˜rj −rf)] = 0
∀j.
(6.3.3)
The Hessian matrix of the objective function is:
A ≡E
h
u′′  ˜W

(˜r −rf1) (˜r −rf1)⊤i
.
(6.3.4)
h⊤Ah < 0 ∀h ̸= 0N if and only if u′′ < 0. Since we have assumed that investor
behaviour is risk averse, A is a negative definite matrix and, by Theorem 3.2.4,
f is a strictly concave (and hence strictly quasiconcave) function. Thus, under
the present assumptions, Theorems 3.3.3 and 3.3.4 guarantee that the first order
conditions have a unique solution. The trivial case in which the random returns
are not really random at all can be ignored.
The rest of this section should be omitted until I figure out what is going on.
Another way of writing (6.3.3) is:
E\[u′( ˜W)˜rj] = E\[u′( ˜W)]rf
∀j,
(6.3.5)
or
Cov
h
u′( ˜W), ˜rj
i
+ E\[u′( ˜W)]E\[˜rj] = E\[u′( ˜W)]rf
∀j,
(6.3.6)
or
E\[˜rj −rf] =
Cov
h
u′( ˜W), ˜rj
i
E\[u′( ˜W)]
∀j,
(6.3.7)
Suppose pj is the price of the random payoff ˜xj. Then ˜rj = ˜xj
pj and
pj = E
"
u′( ˜W)
E\[u′( ˜W)]rf
˜xj
#
∀j.
(6.3.8)
In other words, payoffs are valued by taking their expected present value, using
the stochastic discount factor
u′( ˜
W)
E\[u′( ˜
W)]rf , which ends up being the same for all
investors. Practical corporate finance and theoretical asset pricing models to a
large extent are (or should be) concerned with analysing this discount factor.
(We could consider here the explicit example with quadratic utility from the prob-
lem sets.)
Revised: December 2, 1998

112
6.3. THE SINGLE-PERIOD PORTFOLIO CHOICE PROBLEM
6.3.2
Risk aversion and portfolio composition
For the moment, assume only one risky asset (N = 1).
We first consider the concept of local risk neutrality. The optimal investment in
the risky asset is positive
⇐⇒
The objective function is increasing at a = 0
⇐⇒
f ′ (a) > 0
(6.3.9)
⇐⇒
E\[u′ (W0rf) (˜r −rf)] > 0
(6.3.10)
⇐⇒
u′ (W0rf) E\[(˜r −rf)] > 0
(6.3.11)
⇐⇒
E\[˜r] > E\[rf] = rf
This is the property of local risk neutrality — a risk averse investor will always
prefer a little of a risky asset paying a higher expected return than rf to none of
the risky asset.
Definition 6.3.1 Let f: X →ℜ++ be a positive-valued function defined on X ⊆
ℜk
++. Then the elasticity of f with respect to xi at x∗is
x∗
i
f (x)
∂f
∂xi
(x∗) .
Roughly speaking, the elasticity is just
∂ln f
∂ln xi, or the slope of the graph of the
function on log-log graph paper.
A function is said to be inelastic when the absolute value of the elasticity is less
than unity; and elastic when the absolute value of the elasticity is greater than
unity. The borderline case is called a unit elastic function.
One useful application of elasticity is in analysing the behaviour of the total rev-
enue function associated with a particular inverse demand function, P(Q). We
have:
dP (Q) Q
dQ
=
qdP
dQ + P
(6.3.12)
=
P
 
1 + 1
η
!
.
(6.3.13)
Revised: December 2, 1998

CHAPTER 6. PORTFOLIO THEORY
113
Hence, total revenue is constant or maximised or minimised where elasticity equals
−1; increasing when elasticity is less than −1 (demand is elastic); and decreasing
when elasticity is between 0 and −1 (demand is inelastic).
Now consider other properties of asset demands (assuming that E \[˜r] > rf):
• DARA ⇒risky asset normal

da
dW0 > 0

• CARA ⇒

da
dW0 = 0

• IARA ⇒risky asset inferior

da
dW0 < 0

Define the wealth elasticity of demand for the risky asset to be
η = W0
a
da
dW0
.
(6.3.14)
Then we have
d

a
W0

dW0
=
W0
da
dW0 −a
W 2
0
=
a
W 2
0
(η −1) .
Note that
sign
 d a
W0
dW0
!
= sign (η −1)
(6.3.15)
since by assuming a positive expected risk premium on the risky asset we guaran-
tee (by local risk-neutrality) that a is positive.
• DRRA ⇒increasing proportion of wealth invested in the risky asset (η > 1)
• CRRA ⇒constant proportion of wealth invested in the risky asset (η = 1)
• IRRA ⇒decreasing proportion of wealth invested in the risky asset (η < 1)
Theorem 6.3.1 DARA ⇒RISKY ASSET NORMAL
Proof By implicit differentiation of the now familiar first order condition (6.3.3),
which can be written:
E\[u′(W0rf + a(˜r −rf))(˜r −rf)] = 0,
(6.3.16)
we have
da
dW0
= E\[u′′( ˜W)(˜r −rf)]rf
−E\[u′′( ˜W)(˜r −rf)2].
(6.3.17)
Revised: December 2, 1998

114
6.3. THE SINGLE-PERIOD PORTFOLIO CHOICE PROBLEM
By concavity, the denominator is positive. Therefore:
sign (da/dW0) = sign {E\[u′′( ˜W)(˜r −rf)]}
(6.3.18)
We will show that both are positive.
For decreasing absolute risk aversion:3
˜r > rf
⇒
RA( ˜W) < RA(W0rf)
˜r ≤rf
⇒
RA( ˜W) ≥RA(W0rf)
Multiplying both sides of each inequality by −u′( ˜W)(˜r −rf) gives respectively:
u′′( ˜W)(˜r −rf) > −RA(W0rf)u′( ˜W)(˜r −rf)
(6.3.19)
in the event that ˜r > rf, and
u′′( ˜W)(˜r −rf) ≥−RA(W0rf)u′( ˜W)(˜r −rf)
(6.3.20)
(the same result) in the event that ˜r ≤rf
Integrating over both events implies:
E\[u′′( ˜W)(˜r −rf)] > −RA(W0rf)E\[u′( ˜W)(˜r −rf)],
(6.3.21)
provided that ˜r > rf with positive probability.
The RHS of inequality (6.3.21) is 0 at the optimum, hence the LHS is positive as
claimed.
Q.E.D.
The other results are proved similarly (exercise!).
6.3.3
Mutual fund separation
Commonly, investors delegate portfolio choice to mutual fund operators or man-
agers. We are interested in conditions under which large groups of investors will
agree on portfolio composition. For example, all investors with similar utility
functions might choose the same portfolio, or all investors with similar probabil-
ity beliefs might choose the same portfolio. More realistically, we may be able to
define a group of investors whose portfolio choices all lie in a subspace of small
dimension (say 2) of the N-dimensional portfolio space. The first such result is
due to ?.
3Think about whether separating out the case of ˜r = rf is necessary.
Revised: December 2, 1998

CHAPTER 6. PORTFOLIO THEORY
115
Theorem 6.3.2 ∃Two fund monetary separation
i.e. Agents with different wealths (but the same increasing, strictly concave, VNM
utility) hold the same risky unit cost portfolio, p∗say, (but may differ in the mix of
the riskfree asset and risky portfolio)
i.e. ∀portfolios p, wealths W0, ∃λ s.t.
E
h
u

W0rf + λW0p∗⊤(˜r −rf1)
i
≥E
h
u

W0rf + p⊤(˜r −rf1)
i
(6.3.22)
⇐⇒
Risk-tolerance (1/RA(z)) is linear (including constant)
i.e. ∃Hyperbolic Absolute Risk Aversion (HARA, incl. CARA)
i.e. the utility function is of one of these types:
• Extended power: u(z) =
1
(C+1)B(A + Bz)C+1
• Logarithmic: u(z) = ln(A + Bz)
• Negative exponential: u(z) = −A
B exp{Bz}
where A, B and C are chosen to guarantee u′ > 0, u′′ < 0.
i.e. marginal utility satisfies
u′(z) = (A + Bz)C
or
u′(z) = A exp{Bz}
(6.3.23)
where A, B and C are again chosen to guarantee u′ > 0, u′′ < 0.
Proof The proof that these conditions are necessary for two fund separation is
difficult and tedious. The interested reader is referred to ?.
We will show that u′(z) = (A + Bz)C is sufficient for two-fund separation.
The optimal dollar investments wj are the unique solution to the first order condi-
tions:
0
=
E\[u′( ˜W)δ ˜W
δwi
]
(6.3.24)
=
E\[(A + B ˜W)C(˜ri −rf)]
(6.3.25)
=
E\[(A + BW0rf +
X
j
Bwj(˜rj −rf))C(˜ri −rf)],
(6.3.26)
or equivalently to the system of equations
E\[(1 +
X
j
Bwj
A + BW0rf
(˜rj −rf))C(˜ri −rf)] = 0
(6.3.27)
Revised: December 2, 1998

116
6.4. MATHEMATICS OF THE PORTFOLIO FRONTIER
or
E\[(1 +
X
j
xj(˜rj −rf))C(˜ri −rf)] = 0
(6.3.28)
where
xj =
Bwj
A + BW0rf
.
The unique solutions for xj are clearly independent of W0 which does not appear
in (6.3.28).
Since A and B do not appear either, the unique solutions for xj are also indepen-
dent of those parameters.
However, they do depend on C.
But the risky portfolio weights are
wi
P
j wj
=
Bwi/(A + BW0rf)
P
j Bwj/(A + BW0rf)
(6.3.29)
=
xi
P
j xj
(6.3.30)
and so are also independent of initial wealth.
Since the dollar investment in the jth risky asset satisfies:
wj = xj(A
B + W0rf)
(6.3.31)
we also have in this case that the dollar investment in the common risky portfolio
is a linear function of the initial wealth. The other sufficiency proofs are similar
and are left as exercises.
Q.E.D.
Some humorous anecdotes about Cass may now follow.
6.4
Mathematics of the Portfolio Frontier
6.4.1
The portfolio frontier in ℜN:
risky assets only
The portfolio frontier
Definition 6.4.1 The (mean-variance) portfolio frontier is the set of solutions to
the mean-variance portfolio choice problem faced by a (risk-averse) investor with
an initial wealth of W0 who desires an expected final wealth of at least W1 ≡µW0
(or, equivalently, an expected rate of return of µ), but with the smallest possible
variance of final wealth.
Revised: December 2, 1998

CHAPTER 6. PORTFOLIO THEORY
117
The mean-variance frontier can also be called the two-moment portfolio frontier,
in recognition of the fact that the same approach can be extended (with difficulty)
to higher moments.
The mean-variance portfolio frontier is a subset of the portfolio space, which is
just ℜN. However, introductory treatments generally present it (without proof) as
the envelope function, in mean-variance space or mean-standard deviation space
(ℜ+ × ℜ), of the variance minimisation problem.
Definition 6.4.2 w is a frontier portfolio
⇐⇒
its return has the minimum variance among all portfolios that have the same cost,
w⊤1, and the same expected payoff, w⊤e.
We will begin by supposing that all assets are risky. Formally, the frontier port-
folio corresponding to initial wealth W0 and expected return µ (expected terminal
wealth µW0) is the solution to the quadratic programming problem:
min
w w⊤Vw
(6.4.1)
subject to the linear constraints:
w⊤1
=
W0
(6.4.2)
and
w⊤e
≥
W1 = µW0.
(6.4.3)
The first constraint is just the budget constraint, while the second constraint states
that the expected rate of return on the portfolio is at least the desired mean return
µ.
The frontier in this case is the set of solutions for all values of W0 and W1 (or µ) to
this variance minimisation problem, or to the equivalent maximisation problem:
max
w −w⊤Vw
(6.4.4)
subject to the same linear constraints (6.4.2) and (6.4.3).
The properties of this two-moment frontier are well known, and can be found,
for example, in ? or ?. The notation here follows ?. The derivation of the mean-
variance frontier is generally presented in the literature in terms of portfolio weight
vectors or, equivalently, assuming that initial wealth, W0, equals 1. This assump-
tion is not essential and will be avoided.
Revised: December 2, 1998

118
6.4. MATHEMATICS OF THE PORTFOLIO FRONTIER
The solution
The inequality constrained maximisation problem (6.4.4) is just a special case
of the canonical quadratic programming problem considered at the end of Sec-
tion 3.5, except that it has explicitly one equality constraint and one inequality
constraint.
To avoid degeneracies, we require:
1. that not every portfolio has the same expected return, i.e.
e ̸= E\[˜r1]1,
(6.4.5)
and in particular that N > 1.
2. that the variance-covariance matrix, V, is (strictly) positive definite. We
already know from (1.12.4) that V must be positive semi-definite, but we
require this slightly stronger condition. To see why, suppose
∃w ̸= 0N s.t. w⊤Vw = 0
(6.4.6)
Then ∃a portfolio whose return w⊤˜r = ˜rw has zero variance.
This implies that ˜rw = r0 (say) w.p.1 or, essentially, that this portfolio is
riskless.
Arbitrage will force the returns on all riskless assets to be equal in equilib-
rium, so this situation is equivalent economically to the introduction of a
riskless asset later.
In the portfolio problem, the place of the matrix A in the canonical quadratic
programming problem is taken by the (symmetric) negative definite matrix, −V,
which is just the negative of the variance-covariance matrix of asset returns; g1 =
1⊤and α1 = W0; and g2 = e⊤and α2 = W1. (6.4.5) guarantees that the 2 × N
matrix G is of full rank 2.
The parallels are a little fuzzy in the case of the budget constraint since it is really
an equality constraint.
(3.5.39) says that the optimal w is a linear combination of the two columns of the
N × 2 matrix
V−1G⊤
GV−1G⊤−1 ,
with columns weighted by initial wealth W0 and expected final wealth, W1.
We will call these columns g and h and write the solution as
w = W0g + W1h = W0 (g + µh) .
(6.4.7)
Revised: December 2, 1998

CHAPTER 6. PORTFOLIO THEORY
119
The components of g and h are functions of the means and variances of security
returns. Thus the vector of optimal portfolio proportions,
1
W0
w = g + µh,
(6.4.8)
is independent of the initial wealth W0.
It is easy to see the economic interpretation of g and h:
• g is the frontier portfolio corresponding to W0 = 1 and W1 = 0. In other
words, it is the normal portfolio which would be held by an investor whose
objective was to (just) go bankrupt with minimum variance.
• Similarly, h is the frontier portfolio corresponding to W0 = 0 and W1 = 1.
In other words, it is the hedge portfolio which would be purchased by a
variance-minimising investor in order to increase his expected final wealth
by one unit.
Alternatively, (3.5.35) says that the optimal w is a linear combination of the two
columns of the N × 2 matrix
1
2V−1G⊤=

1
2V−11
1
2V−1e

,
with columns weighted by the Lagrange multipliers corresponding to the two con-
straints. We will call the Lagrange multipliers 2γ/C and 2λ/A respectively, where
we define:
A
≡
1⊤V−1e = e⊤V−11
(6.4.9)
B
≡
e⊤V−1e > 0
(6.4.10)
C
≡
1⊤V−11 > 0
(6.4.11)
and
D
≡
BC −A2
(6.4.12)
and the inequalities follow from the fact that V−1 (like V) is positive definite.
This allows the solution to be written as:
w = γ
C (V−11) + λ
A(V−1e).
(6.4.13)
1
C(V−11) and 1
A(V−1e) are both unit portfolios, so γ + λ = W0. We know that
for the portfolio which minimises variance for a given initial wealth, regardless
of expected final wealth, the corresponding Lagrange multiplier, λ = 0. Thus
γ
C(V−11) is the global minimum variance portfolio with cost W0 (which in fact
Revised: December 2, 1998

120
6.4. MATHEMATICS OF THE PORTFOLIO FRONTIER
equals γ in this case) and
1
C(V−11) is the global minimum variance unit cost
portfolio, which we will denote wMVP.
In fact, we can combine (6.4.7) and (6.4.13) and write the solution as:
w = W0

wMVP +

µ −A
C

h

.
(6.4.14)
The details are left as an exercise.4
The set of solutions to this quadratic programming problem for all possible (W0, W1)
combinations (including negative W0) is the vector subspace of the portfolio space,
which is generated either by the vectors g and h or by the vectors wMVP and h (or
by any pair of linearly independent frontier portfolios).
In ℜN, the set of unit cost frontier portfolios is the line passing thru g, parallel to
h.
It follows immediately that the frontier (like any straight line in ℜN) is a convex
set, and can be generated by linear combinations of any pair of frontier portfolios
with weights of the form α and (1 −α).
An important exercise at this stage is to work out the means, variances and co-
variances of the returns on wMVP, g and h. They will drop out of the portfolio
decomposition below.
The portfolio weight vectors g and h are
g
=
1
D\[B(V−11) −A(V−1e)]
(6.4.15)
h
=
1
D\[C(V−1e) −A(V−11)]
(6.4.16)
We have
Var\[˜rg]
=
g⊤Vg = B
D
(6.4.17)
Var\[˜rh]
=
h⊤Vh = C
D
(6.4.18)
from which it follows that D > 0.
Orthogonal decomposition of portfolios
At this stage, we must introduce a scalar product on the portfolio space, namely
that based on the variance-covariance matrix V. Since V is a non-singular, pos-
itive definite matrix, it defines a well behaved scalar product and all the standard
results on orthogonal projection (&c.) from linear algebra are valid.
4At least for now.
Revised: December 2, 1998

CHAPTER 6. PORTFOLIO THEORY
121
Two portfolios w1 and w2 are orthogonal with respect to this scalar product
⇐⇒
w⊤
1 Vw2 = 0
⇐⇒
Cov
h
w⊤
1 ˜r, w⊤
2 ˜r
i
= 0
⇐⇒
the random variables representing the returns on the portfolios are uncorrelated.
Thus, the terms ‘orthogonal’ and ‘uncorrelated’ may legitimately, and shall, be
applied interchangeably to pairs of portfolios. Furthermore, the squared length of
a weight vector corresponds to the variance of its returns.
Note that wMVP and h are orthogonal vectors in this sense. In fact, we have the
following theorem:
Theorem 6.4.1 If w is a frontier portfolio and u is a zero mean hedge portfolio,
then w and u are uncorrelated.
Proof There is probably a full version of this proof lost somewhere but the fol-
lowing can be sorted out.
Since wMVP is collinear with V−11, it is orthogonal to all portfolios w for which
w⊤VV−11 = 0 or in other words to all portfolios for which w⊤1 = 0. But these
are precisely all hedge portfolios, including h.
Similarly, any portfolio collinear with V−1e is orthogonal to all portfolios with
zero expected return, since w⊤VV−1e = 0 or in other words w⊤e = 0.
Q.E.D.
Some pictures are in order at this stage.
For N = 3, in the set of portfolios costing W0 (the W0 simplex), the iso-variance
curves are concentric ellipses, the iso-mean curves are parallel lines, and the solu-
tions for different µs (or W1s) are the tangency points between these ellipses and
lines, which themselves lie on a line orthogonal (in the sense defined above) to
the iso-mean lines. The centre of the concentric ellipses is at the global minimum
variance portfolio corresponding to W0, W0wMVP. A similar geometric interpre-
tation can be applied in higher dimensions.
? has some nice pictures of the frontier in portfolio space, as opposed to mean-
variance space.
At this stage, recall the definition of β in (5.2.2).
We will now derive an orthogonal decomposition of a portfolio q into two frontier
portfolios and a zero-mean zero-cost portfolio and prove that the coefficients on
the two frontier portfolios are the βs of q with respect to those portfolios and sum
to unity.
We can always choose an orthogonal basis for the portfolio frontier.
Revised: December 2, 1998

122
6.4. MATHEMATICS OF THE PORTFOLIO FRONTIER
For any frontier portfolio p ̸= wMVP, there is a unique unit cost frontier portfolio
zp which is orthogonal to p.
Another important exercise is to figure out the relationship between E \[˜rp] and
E
h
˜rzp
i
.
Any two frontier portfolios span the frontier, in particular any unit cost p ̸= wMVP
and zp (or the original basis, wMVP and h).
Any (frontier or non-frontier) portfolio q with non-zero cost W0 can be written in
the form fq + uq where
fq
≡
W0 (g + E\[˜rq]h)
(6.4.19)
=
W0 (βqpp + (1 −βqp)zp) (say)
(6.4.20)
is the frontier portfolio with expected return E\[˜rq] and cost W0 and uq is a hedge
portfolio with zero expected return. Geometrically, this decomposition is equiva-
lent to the orthogonal projection of q onto the frontier.
Theorem 6.4.1 shown that any portfolio sharing these properties of uq is uncorre-
lated with all frontier portfolios.5
If p is a unit cost frontier portfolio (i.e. the vector of portfolio proportions) and
q is an arbitrary unit cost portfolio, then the following decomposition therefore
holds:
q = fq + uq = βqpp + (1 −βqp) zp + uq
(6.4.21)
where the three components (i.e. the vectors p, zp and uq) are mutually orthogo-
nal.
We can extend this decomposition to cover
1. portfolio proportions (orthogonal vectors)
2. portfolio proportions (scalars/components)
3. returns (uncorrelated random variables)
4. expected returns (numbers)
Note again the parallel between orthogonal portfolio vectors and uncorrelated
portfolio returns/payoffs.
We will now derive the relation:
E\[˜rq] −E\[˜rzp] = βqp(E\[˜rp] −E\[˜rzp])
(6.4.22)
5Aside: For the frontier portfolio fq to second degree stochastically dominate the arbitrary
portfolio q, we will need zero conditional expected return on uq, and will have to show that
Cov

˜ruq, ˜rfq

= 0 =⇒E\[˜ruq|˜rfq] = 0
The normal distribution is the only case where this is true.
Revised: December 2, 1998

CHAPTER 6. PORTFOLIO THEORY
123
which may be familiar from earlier courses in financial economics and which is
quite general and neither requires asset returns to be normally distributed nor any
assumptions about preferences.
Since Cov
h
˜ruq, ˜rp
i
= Cov
h
˜rzp, ˜rp
i
= 0, taking covariances with ˜rp in (6.4.21)
gives:
Cov \[˜rq, ˜rp] = Cov
h
˜rfq, ˜rp
i
= βqpVar\[˜rp]
(6.4.23)
or
βqp = Cov \[˜rq, ˜rp]
Var\[˜rp]
(6.4.24)
Thus β in (6.4.21) has its usual definition from probability theory, given by (5.2.2).6
Reversing the roles of p and zp, it can be seen that
βqzp = 1 −βqp
(6.4.25)
Taking expected returns in (6.4.21) yields again:
E\[˜rq] = βqpE\[˜rp] + (1 −βqp)E\[˜rzp],
(6.4.26)
which can be rearranged to obtain (6.4.22).
The Global Minimum Variance Portfolio
Var\[˜rg+µh] = g⊤Vg + 2µ(g⊤Vh) + µ2(h⊤Vh)
(6.4.27)
which has its minimum at
µ = −g⊤Vh
h⊤Vh
(6.4.28)
The latter expression reduces to A/C and the minimum value of the variance is
1/C. The global minimum variance portfolio is denoted MVP.
Cov \[˜rh, ˜rMVP]
=
h⊤V
 
g −g⊤Vh
h⊤Vhh
!
(6.4.29)
=
h⊤Vg −g⊤Vh.h⊤Vh
h⊤Vh
= 0
(6.4.30)
i.e. the returns on the portfolio with weights h and the minimum variance portfolio
are uncorrelated.
6Assign some problems involving the construction of portfolio proportions for various desired
βs. Also problems working from prices for state contingent claims to returns on assets and port-
folios in both single period and multi-period worlds.
Revised: December 2, 1998

124
6.4. MATHEMATICS OF THE PORTFOLIO FRONTIER
Further, if p is any portfolio, the MVP is the minimum variance combination of
itself and p, i.e. a = 0 solves:
min
a
1
2Var\[˜rap+(1−a)MVP]
(6.4.31)
which has necessary and sufficient first order condition:
aVar\[˜rp] + (1 −2a)Cov \[˜rp, ˜rMVP] −(1 −a)Var\[˜rMVP] = 0
(6.4.32)
Hence, setting a = 0:
Cov \[˜rp, ˜rMVP] −Var\[˜rMVP] = 0
(6.4.33)
and the covariance of any portfolio with MVP is 1/C.
6.4.2
The portfolio frontier in mean-variance space:
risky assets only
The portfolio frontier in mean-variance and in mean-standard deviation space
We now move on to consider the mean-variance relationship along the portfolio
frontier.
The mean, µ, and variance, σ2, of the rate of return associated with each point on
the frontier are related by the quadratic equation:
(σ2 −Var\[w⊤
MVP˜r]) = φ(µ −E\[w⊤
MVP˜r])2,
(6.4.34)
where the shape parameter φ = C/D represents the variance of the (gross) return
on the hedge portfolio, h. The two-moment frontier is generally presented as the
graph in mean-variance space of this parabola, showing the most desirable distri-
butions attainable, but the frontier can also be thought of as a plane in portfolio
space or as a line in portfolio weight space. The latter interpretations are far more
useful when it comes to extending the analysis to higher moments.
The equations of the frontier in mean-variance and mean-standard deviation space
can be derived heuristically using the following stylized diagram illustrating the
portfolio decomposition.
Figure 3A goes here.
Applying Pythagoras’ theorem to the triangle with vertices at 0, p and MVP yields:
σ2 = Var\[˜rp] = Var\[˜rMVP] +

µ −A
C
2
Var\[˜rh]
(6.4.35)
Revised: December 2, 1998

CHAPTER 6. PORTFOLIO THEORY
125
Recall from the coordinate geometry of conic sections that
Var\[˜rp] = Var\[˜rMVP] + (µ −E\[˜rMVP])2 Var\[˜rh]
(6.4.36)
or
V (µ) = 1
C + C
D

µ −A
C
2
(6.4.37)
is a quadratic equation in µ.
i.e. the equation of the parabola with vertex at
Var\[˜rp]
=
Var\[˜rMVP] = 1
C
(6.4.38)
µ
=
E\[˜rMVP] = A
C
(6.4.39)
Thus in mean-variance space, the frontier is a parabola.
Figure 3.11.2 goes here: indicate position of g on figure.
Similarly, in mean-standard deviation space, the frontier is a hyperbola. To see
this, recall that:
σ2 = Var\[˜rMVP] +

µ −A
C
2
Var\[˜rh]
(6.4.40)
is the equation of the hyperbola with vertex at
σ
=
q
Var\[˜rMVP] =
s
1
C
(6.4.41)
µ
=
A
C
(6.4.42)
centre at σ = 0, µ = A/C and asymptotes as indicated.
Figure 3.11.1 goes here: indicate position of g on figure.
The other half of the hyperbola (σ < 0) has no economic meaning.
Recall two other types of conic sections:
Var\[˜rh] < 0 (impossible) gives a circle with center (1/C, A/C).
Var\[˜rMVP] = 0 (the presence of a riskless asset) allows the square root to be taken
on both sides:
σ = ±

µ −A
C
 q
Var\[˜rh]
(6.4.43)
i.e. the conic section becomes the pair of lines which are its asymptotes otherwise.
Revised: December 2, 1998

126
6.4. MATHEMATICS OF THE PORTFOLIO FRONTIER
Portfolios on which the expected return, µ, exceeds w⊤
MVPe are termed efficient,
since they maximise expected return given variance; other frontier portfolios min-
imise expected return given variance and are inefficient.
A frontier portfolio is said to be an efficient portfolio iff
its expected return exceeds the minimum variance expected return A/C = E\[˜rMVP].
The set of efficient portfolios in ℜN (or efficient frontier) is the half-line emanat-
ing from MVP in the direction of h, and hence is also a convex set.
Convex combinations (but not all linear combinations with weights summing to
1) of efficient portfolios are efficient.
We now consider zero-covariance (zero-beta) portfolios. In portfolio weight space,
can easily construct a frontier portfolio having zero covariance with any given
frontier portfolio:
Figure 3B goes here.
Algebraically, the expected return µ0 on the zero-covariance frontier portfolio of
a frontier portfolio with expected return µ solves:
Cov \[˜rMVP + (µ −E\[˜rMVP])˜rh, ˜rMVP + (µ0 −E\[˜rMVP])˜rh] = 0
(6.4.44)
or, since ˜rh and ˜rMVP are uncorrelated:
Var\[˜rMVP] + (µ −E\[˜rMVP])(µ0 −E\[˜rMVP])Var\[˜rh] = 0
(6.4.45)
To make this true, we must have
(µ −E\[˜rMVP])(µ0 −E\[˜rMVP]) < 0
(6.4.46)
or µ and µ0 on opposite sides of E\[˜rMVP] as shown.
There is a neat trick which allows zero-covariance portfolios to be plotted in mean-
standard deviation space.
Implicit differentiation of the µ−σ relationship (6.4.35) along the frontier yields:
dµ
dσ =
σ
(µ −E\[˜rMVP])Var\[˜rh]
(6.4.47)
so the tangent at (σ, µ) intercepts the µ axis at
µ −σdµ
dσ
=
µ −
σ2
(µ −E\[˜rMVP])Var\[˜rh]
(6.4.48)
=
µ −
Var\[˜rMVP]
(µ −E\[˜rMVP])Var\[˜rh] −(µ −E\[˜rMVP])
(6.4.49)
=
E\[˜rMVP] −
Var\[˜rMVP]
(µ −E\[˜rMVP])Var\[˜rh]
(6.4.50)
Revised: December 2, 1998

CHAPTER 6. PORTFOLIO THEORY
127
where we substituted for σ2 from the definition of the frontier.
A little rearrangement shows that expression (6.4.50) satisfies the equation (6.4.45)
defining the return on the zero-covariance portfolio.
In mean-standard deviation space the picture is like this:
Figure 3.15.1 goes here.
To find zp in mean-variance space, note that the line joining (σ2, µ) to the MVP
intercepts the µ axis at:
µ −σ2 µ −E\[˜rMVP]
σ2 −Var\[˜rMVP] = µ −σ2
µ −E\[˜rMVP]
(µ −E\[˜rMVP)2Var\[˜rh]
(6.4.51)
After cancellation, this is exactly the first expression (6.4.48) for the zero-covariance
return we had on the previous page.
Figure 3.15.2 goes here.
Alternative derivations
The treatment of the portfolio frontier with risky assets only concludes with some
alternative derivations following closely ?. They should probably be omitted alto-
gether at this stage.
1. The variance minimisation solution from first principles.
It can be seen that w is the solution to:
min
{w,,
} L = 1
2w⊤Vw + λ(µ −w⊤e) + γ(W0 −w⊤1)
(6.4.52)
which has necessary and sufficient first order conditions:
∂L
∂w
=
Vw −λe −γ1 = 0
(6.4.53)
∂L
∂λ
=
µ −w⊤e = 0
(6.4.54)
∂L
∂γ
=
W0 −w⊤1 = 0
(6.4.55)
The solution can be found by premultiplying the FOC (6.4.13) in turn by
e⊤and 1⊤and using the constraints yields:
µ
=
λ(e⊤V−1e) + γ(e⊤V−11)
(6.4.56)
1
=
λ(1⊤V−1e) + γ(1⊤V−11)
(6.4.57)
Revised: December 2, 1998

128
6.4. MATHEMATICS OF THE PORTFOLIO FRONTIER
The solutions for λ and γ are:
λ
=
Cµ −A
D
(6.4.58)
γ
=
B −Aµ
D
(6.4.59)
2. Derivation of (6.4.22).
If we only have frontier portfolio p and interior portfolio q, we get a frontier
(in µ-σ space) entirely within the previous frontier and tangent to it at p.
The frontiers must have the same slope at p:
Figure 3C goes here.
We already saw that the outer frontier has slope
E\[˜rp−˜rzp]
√
Var\[˜rp] .
At the point on the inner frontier with wq invested in q and (1 −wq) in p,
µ
=
E\[˜rp] + wq(E\[˜rq −˜rp])
(6.4.60)
σ2
=
w2
qVar\[˜rq]
+2wq(1 −wq)Cov \[˜rp, ˜rq] + (1 −wq)2Var\[˜rp] (6.4.61)
Differentiating these w.r.t. wq:
dµ
dwq
=
E\[˜rq −˜rp]
(6.4.62)
2σ dσ
dwq
=
2wqVar\[˜rq]
+2(1 −2wq)Cov \[˜rp, ˜rq] −2(1 −wq)Var\[˜rp] (6.4.63)
Taking the ratio and setting wq = 0 gives the slope of the inner frontier at
p:
dµ
dσ =
E\[˜rq −˜rp]
2Cov\[˜rp,˜rq]−2Var\[˜rp]
2√
Var\[˜rp]
(6.4.64)
Equating this to the slope of the outer frontier, setting
βqp = Cov \[˜rp, ˜rq]
Var\[˜rp]
(6.4.65)
and rearranging yields:
E\[˜rq] −E\[˜rzp] = βqp(E\[˜rp] −E\[˜rzp])
(6.4.66)
Revised: December 2, 1998

CHAPTER 6. PORTFOLIO THEORY
129
6.4.3
The portfolio frontier in ℜN:
riskfree and risky assets
We now consider the mathematics of the portfolio frontier when there is a riskfree
asset.
In this case, the frontier portfolio solves:
min
w
1
2 w⊤Vw
(6.4.67)
s.t.
w⊤e + (1 −w⊤1)rf = µ
(6.4.68)
There is no longer a restriction on portfolio weights, and whatever is not invested
in the N risky assets is assumed to be invested in the riskless asset.
The solution (which can be left as an exercise) is by a similar method to the case
where all assets were risky:
wp = V−1(e −rf1)µ −rf
H
(6.4.69)
where
H = (e −1rf)⊤V−1(e −1rf) = B −2Arf + Crf
2 > 0 ∀rf
(6.4.70)
Along the frontier, we have:
σ =



µ−rf
√
H
if µ ≥rf,
−µ−rf
√
H
if µ < rf,
(6.4.71)
6.4.4
The portfolio frontier in mean-variance space:
riskfree and risky assets
We can now establish the shape of the mean-standard deviation frontier with a
riskless asset.
Graphically, in mean-standard deviation space, combining any portfolio p with
the riskless asset in proportions a and (1 −a) gives a portfolio with expected
return
aE\[˜rp] + (1 −a)rf = rf + a(E\[˜rp] −rf)
and standard deviation of returns a
q
Var\[˜rp].
i.e. these portfolios trace out the ray in σ-µ space emanating from (0, rf) and
passing through p.
For each σ the highest return attainable is along the ray from rf which is tangent
to the frontier generated by the risky assets.
Revised: December 2, 1998

130
6.5. MARKET EQUILIBRIUM AND THE CAPM
On this ray, the riskless asset is held in combination with the tangency portfolio t.
This only makes sense for rf < A/C = E\[˜rmvp].
Above t, there is a negative weight on the riskless asset — i.e. borrowing.
Figure 3D goes here.
Limited borrowing
Unlimited borrowing as allowed in the preceding analysis is unrealistic.
Consider what happens
1. with margin constraints on borrowing:
Figure 3E goes here.
The frontier is the envelope of all the finite rays through risky portfolios,
extending as far as the borrowing constraint allows.
2. with differential borrowing and lending rates:
Figure 3F goes here.
There is a range of expected returns over which a pure risky strategy pro-
vides minimum variance;
lower expected returns are achieved by riskless lending;
and higher expected returns are achieved by riskless borrowing.
6.5
Market Equilibrium and the Capital Asset Pric-
ing Model
6.5.1
Pricing assets and predicting security returns
Need more waffle here about prediction and the difficulties thereof and the prop-
erties of equilibrium prices and returns.
We are looking for assumptions concerning probability distributions that lead to
useful and parsimonious asset pricing models. The CAPM restrictions are the
best known. At a very basic level, they can be expressed by saying that every
Revised: December 2, 1998

CHAPTER 6. PORTFOLIO THEORY
131
investor has mean-variance preferences. This can be achieved either by restricting
preferences to be quadratic or the probability distribution of asset returns to be
normal. CAPM is basically a single-period model, but can be extended by assum-
ing that return distributions are stable over time. ? and ? have generalised the
distributional conditions.
Recall also the limiting behaviour of the variance of the return on an equally
weighted portfolio as the number of securities included goes to infinity. If se-
curities are added in such a way that the average of the variance terms and the
average of the covariance terms are stable, then the portfolio variance approaches
the average covariance as a lower bound.
6.5.2
Properties of the market portfolio
Let
mj
=
weight of security j in the market portfolio m
W i
0(> 0)
=
individual i’s initial wealth
wij
=
proportion of individual i’s initial wealth
invested in j-th security
Then total wealth is defined by
Wm0 ≡
I
X
i=1
W i
0
(6.5.1)
and in equilibrium the relation
I
X
i=1
wijW i
0 = mjWm0
∀j
(6.5.2)
must hold. Dividing by Wm0 yields:
I
X
i=1
wij
W i
0
Wm0
= mj
∀j
(6.5.3)
and thus in equilibrium the market portfolio is a convex combination of individual
portfolios.
6.5.3
The zero-beta CAPM
Theorem 6.5.1 (Zero-beta CAPM theorem) If every investor holds a mean-variance
frontier portfolio, then the market portfolio, m, is a mean-variance frontier port-
folio, and hence, ∀q, the CAPM equation
E \[˜rq] = (1 −βqm) E \[˜rzm] + βqmE \[˜rm]
(6.5.4)
holds.
Revised: December 2, 1998

132
6.5. MARKET EQUILIBRIUM AND THE CAPM
Theorem 6.5.2 All strictly risk-averse investors hold frontier portfolios if and
only if
E
h
˜ruq|˜rfq
i
= 0
∀q
(6.5.5)
Note the subtle distinction between uncorrelated returns (in the definition of the
decomposition) and independent returns (in this theorem). They are the same only
for the normal distribution and related distributions.
We can view the market portfolio as a frontier portfolio under two fund separation.
If p is a frontier portfolio, then we showed earlier that for purely mathematical
reasons in the definition of a frontier portfolio:
E\[˜rq] = (1 −βqp)E\[˜rzp] + βqpE\[˜rp]
(6.5.6)
If two fund separation holds, then individuals hold frontier portfolios.
Since the market portfolio is then on the frontier, it follows that:
E\[˜rq] = (1 −βqm)E\[˜rzm] + βqmE\[˜rm]
(6.5.7)
where
˜rm
=
N
X
j=1
mj˜rj
(6.5.8)
βqm
=
Cov \[˜rq, ˜rm]
Var\[˜rm]
(6.5.9)
This implies for any particular security, from the economic assumptions of equi-
librium and two fund separation:
E\[˜rj] = (1 −βjm)E\[˜rzm] + βjmE\[˜rm]
(6.5.10)
This relation is the ?
Zero-Beta version of the Capital Asset Pricing Model
(CAPM).
6.5.4
The traditional CAPM
Now we add the risk free asset, which will allow us to determine the tangency
portfolio, t, and to talk about Capital Market Line (return v. standard deviation)
and the Security Market Line (return v. β).
Normally in equilibrium there is zero aggregate supply of the riskfree asset.
Recommended reading for this part of the course is ?, ?, ? and ?.
Now we can derive the traditional CAPM. Note that by construction
rf = E \[˜rzt] .
(6.5.11)
Revised: December 2, 1998

CHAPTER 6. PORTFOLIO THEORY
133
Theorem 6.5.3 (Separation Theorem) The risky asset holdings of all investors
who hold mean-variance frontier portfolios are in the proportions given by the
tangency portfolio, t.
Theorem 6.5.4 (Traditional CAPM Theorem) If every investor holds a mean-
variance frontier portfolio, then the market portfolio of risky assets, m, is the
tangency portfolio, t, and hence, ∀q, the traditional CAPM equation
E \[˜rq] = (1 −βqm) rf + βqmE \[˜rm]
(6.5.12)
holds.
Theorem 6.5.4 is sometimes known as the Sharpe-Lintner Theorem.
The riskless rate is unique by the No Arbitrage Principle, since otherwise a greedy
investor would borrow an infinite amount at the lower rate and invest it at the
higher rate, which is impossible in equilibrium.
We can also think about what happens the CAPM if there are different riskless
borrowing and lending rates (see ?). If all individuals face this situation in equi-
librium, realism demands that both riskless assets are in zero aggregate supply and
hence that all investors hold risky assets only.
Note that the No Arbitrage Principle also allows us to rule out correlation matri-
ces for risky assets which permit the construction of portfolios with zero return
variance, i.e. synthetic riskless assets.
Assume that a riskless asset exists, with return rf < E\[˜rmvp].
If the distributional conditions for two fund separation are satisfied, then the tan-
gency portfolio, t, must be the market portfolio of risky assets in equilibrium. We
know then that for any portfolio q (with or without a riskless component):
E\[˜rq] −rf = βqm(E\[˜rm] −rf)
(6.5.13)
This is the traditional Sharpe-Lintner version of the CAPM.
Figure 4A goes here.
The next theorem relates to the mean-variance efficiency of the market portfolio.
Theorem 6.5.5 If
1. the distributional conditions for two fund separation are satisfied;
2. risky assets are in strictly positive supply; and
3. investors have strictly increasing (concave) utility functions
then the market/tangency portfolio is efficient.
Revised: December 2, 1998

134
6.5. MARKET EQUILIBRIUM AND THE CAPM
Proof By Jensen’s inequality and monotonicity, the riskless asset dominates any
portfolio with
E\[˜r] < rf
(6.5.14)
for
E\[u(W0(1 + ˜r))]
≤
u(E\[W0(1 + ˜r)])
(6.5.15)
<
u(W0(1 + rf))
(6.5.16)
Hence the expected returns on all individuals’ portfolios exceed rf.
It follows that the expected return on the market portfolio must exceed rf.
Q.E.D.
Now we can calculate the risk premium of the market portfolio.
CAPM gives a relation between the risk premia on individual assets and the risk
premium on the market portfolio.
The risk premium on the market portfolio must adjust in equilibrium to give
market-clearing.
In some situations, the risk premium on the market portfolio can be written in
terms of investors’ utility functions.
Assume there is a riskless asset and returns are multivariate normal (MVN). Recall
the first order conditions for the canonical portfolio choice problem:
0
=
E\[u′
i( ˜Wi)(˜rj −rf)]
∀i, j
(6.5.17)
=
E\[u′
i( ˜Wi)]E\[˜rj −rf] + Cov
h
u′
i( ˜Wi), ˜rj
i
(6.5.18)
=
E\[u′
i( ˜Wi)]E\[˜rj −rf] + E\[u′′
i ( ˜Wi)]Cov
h ˜Wi, ˜rj
i
(6.5.19)
using the definition of covariance and Stein’s lemma for MVN distributions. Re-
arranging:
E\[˜rj −rf]
θi
= Cov
h ˜Wi, ˜rj
i
(6.5.20)
where
θi ≡−E\[u′′
i ( ˜Wi)]
E\[u′
i( ˜Wi)]
(6.5.21)
is the i-th investor’s global absolute risk aversion. Since
˜Wi = W i
0(1 + rf +
N
X
k=1
wik(˜rk −rf))
(6.5.22)
we have, dropping non-stochastic terms,
Cov
h ˜Wi, ˜rj
i
= Cov
"
W i
0
N
X
k=1
wik˜rk, ˜rj
#
(6.5.23)
Revised: December 2, 1998

CHAPTER 6. PORTFOLIO THEORY
135
Hence,
E\[˜rj −rf]
θi
= Cov
"
W i
0
N
X
k=1
wik˜rk, ˜rj
#
(6.5.24)
Summing over i, this gives (since we have
P
i W i
0wik = W m
0 wmk by market-
clearing and
P
k wmk˜rk = ˜rm by definition):
E\[˜rj −rf](
I
X
i=1
θ−1
i )
=
Wm0Cov \[˜rm, ˜rj]
(6.5.25)
or
E\[˜rj −rf]
=
(
I
X
i=1
θ−1
i )−1Wm0Cov \[˜rm, ˜rj]
(6.5.26)
i.e., in equilibrium, the risk premium on the j-th asset is the product of the aggre-
gate relative risk aversion of the economy and the covariance between the return
on the j-th asset and the return on the market.
Now take the average over j weighted by market portfolio weights:
E\[˜rm −rf] = (
I
X
i=1
θ−1
i )−1Wm0Var\[˜(]˜rm)
(6.5.27)
i.e., in equilibrium, the risk premium on the market is the product of the aggre-
gate relative risk aversion of the economy and the variance of the return on the
market. Equivalently, the return to variability of the market equals the aggregate
relative risk aversion.
We conclude with some examples.
1. Negative exponential utility:
ui(z) = −1
ai
exp{−aiz}
ai > 0
(6.5.28)
implies:
(
I
X
i=1
θ−1
i )−1 = (
I
X
i=1
a−1
i )−1 > 0
(6.5.29)
and hence the market portfolio is efficient.
2. Quadratic utility:
ui(z) = aiz −bi
2 z2
ai, bi > 0
(6.5.30)
implies:
(
I
X
i=1
θ−1
i )−1 =
 I
X
i=1
ai
bi
−E\[ ˜Wi]
!−1
(6.5.31)
This result can also be derived without assuming MVN and using Stein’s
lemma.
Revised: December 2, 1998

136
6.5. MARKET EQUILIBRIUM AND THE CAPM
Revised: December 2, 1998

CHAPTER 7. INVESTMENT ANALYSIS
137
Chapter 7
INVESTMENT ANALYSIS
7.1
Introduction
\[To be written.]
7.2
Arbitrage and the Pricing of Derivative Securi-
ties
7.2.1
The binomial option pricing model
This still has to be typed up. It follows very naturally from the stuff in Section 5.4.
7.2.2
The Black-Scholes option pricing model
Fischer Black died in 1995. In 1997, Myron Scholes and Robert Merton were
awarded the Nobel Prize in Economics ‘for a new method to determine the value
of derivatives.’ See
http://www.nobel.se/announcement-97/economy97.html
Black and Scholes considered a world in which there are three assets: a stock,
whose price, ˜St, follows the stochastic differential equation:
d ˜St = µ ˜Stdt + σ ˜Std˜zt,
where {˜zt}T
t=0 is a Brownian motion process; a bond, whose price, Bt, follows the
differential equation:
dBt = rBtdt;
and a call option on the stock with strike price X and maturity date T.
Revised: December 2, 1998

138
7.2. ARBITRAGE AND PRICING DERIVATIVE SECURITIES
They showed how to construct an instantaneously riskless portfolio of stocks and
options, and hence, assuming that the principle of no arbitrage holds, derived the
Black-Scholes partial differential equation which must be satisfied by the option
price.
The option pays (ST −X)+ ≡max {ST −X, 0} at maturity.
Let the price of the call at time t be ˜Ct. Guess that ˜Ct = C( ˜St, t). By Ito’s lemma:
d ˜Ct =
 ∂C
∂t + ∂C
∂S µ ˜St + 1
2
∂2C
∂S2 σ2 ˜S2
t
!
dt + ∂C
∂S σ ˜Std˜zt
The no arbitrage principle yields the partial differential equation:
∂C
∂t + 1
2
∂2C
∂S2 σ2S2 + ∂C
∂S rS −rC = 0
subject to the boundary condition
C(S, T) = (S −X)+.
Let τ = T −t be the time to maturity.
Then we claim that the solution to the Black-Scholes equation is:
C(S, t) = SN (d (S, τ)) −Xe−rτN

d (S, τ) −σ√τ

,
where N (·) is the cumulative distribution function of the standard normal distri-
bution and
d (S, τ)
=
ln S
X +

r −1
2σ2
τ
σ√τ
+ σ√τ
(7.2.1)
=
ln S
X +

r + 1
2σ2
τ
σ√τ
.
(7.2.2)
We can check that this is indeed the solution by calculating the various partial
derivatives and substituting them in the original equation.
Note first that
N (z) ≡
Z z
−∞
1
√
2πe−1
2 t2dt
and hence by the fundamental theorem of calculus
N ′ (z) ≡
1
√
2πe−1
2 z2,
Revised: December 2, 1998

CHAPTER 7. INVESTMENT ANALYSIS
139
which of course is the corresponding probability density function. For the last step
in this proof, we will need the partials of d (S, τ) with respect to S and t, which
are:
∂d (S, τ)
∂t
= −∂d (S, τ)
∂τ
=
−

r + 1
2σ2
2σ√τ
(7.2.3)
and
∂d (S, τ)
∂S
=
1
Sσ√τ .
(7.2.4)
Note also that
N ′ 
d (S, τ) −σ√τ

=
e−1
2σ2τed(S,τ)σ√τN ′ (d (S, τ))
(7.2.5)
=
e−1
2σ2τ
 S
X e(r+ 1
2σ2)τ

N ′ (d (S, τ))
(7.2.6)
=
S
X erτN ′ (d (S, τ)) .
(7.2.7)
Using these facts and the chain rule, we have:
∂C
∂t
=
SN ′ (d (S, τ)) ∂d (S, τ)
∂t
−Xe−rτ×
 
N ′ 
d (S, τ) −σ√τ
  ∂d (S, τ)
∂t
−
σ
2√τ
!
+ rN

d (S, τ) −σ√τ
!
(7.2.8)
=
−SN ′ (d (S, τ))
σ
2√τ −Xe−rτrN

d (S, τ) −σ√τ

(7.2.9)
∂C
∂S
=
SN ′ (d (S, τ)) ∂d (S, τ)
∂S
+ N (d (S, τ))
−Xe−rτN ′ 
d (S, τ) −σ√τ
 ∂d (S, τ)
∂S
(7.2.10)
=
N (d (S, τ))
(7.2.11)
∂2C
∂S2
=
N ′ (d (S, τ)) ∂d (S, τ)
∂S
.
(7.2.12)
Substituting these expressions in the original partial differential equation yields:
∂C
∂t + 1
2
∂2C
∂S2 σ2S2 + ∂C
∂S rS −rC
Revised: December 2, 1998

140
7.3. MULTI-PERIOD INVESTMENT PROBLEMS
=
N (d (S, τ)) (rS −rS) + N ′ (d (S, τ))
 −Sσ
2√τ + 1
2σ2S2∂d (S, τ)
∂S
!
+N

d (S, τ) −σ√τ
 
−Xe−rτr + rXe−rτ
(7.2.13)
=
0.
(7.2.14)
The boundary condition should also be checked. As τ →0, d (S, τ) →±∞
according as S > X or S < X. In the former case, C (S, T) = S −X; and in the
latter case, C (S, T) = 0, so the boundary condition is indeed satisfied.
7.3
Multi-period Investment Problems
In Section 4.2, it was pointed out that the objects of choice can be differentiated
not only by their physical characteristics, but also both by the time at which they
are consumed and by the state of nature in which they are consumed. These
distinctions were suppressed in the intervening sections but are considered again
in this section and in Section 5.4 respectively.
The multi-period model should probably be introduced at the end of Chapter 4
but could also be left until Chapter 7. For the moment this brief introduction is
duplicated in both chapters.
Discrete time multi-period investment problems serve as a stepping stone from
the single period case to the continuous time case.
The main point to be gotten across is the derivation of interest rates from equilib-
rium prices: spot rates, forward rates, term structure, etc.
This is covered in one of the problems, which illustrates the link between prices
and interest rates in a multiperiod model.
7.4
Continuous Time Investment Problems
?
Revised: December 2, 1998

