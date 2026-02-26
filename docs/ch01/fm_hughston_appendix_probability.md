# Appendix: Probability Theory Reminders

!!! info "Source"
    **Financial Mathematics** by Hughston & Hunter. Appendix D: Probability Theory.
    These notes are used for educational purposes.

## Probability Theory Reminders

D
Some Reminders of Probability Theory
(by R.F. Streater)
D.1
Events, random variables and distributions
An event A is a subset of a space (the sample space Ω); more exactly, A is a
measurable subset. We are given the probability p(A) for all events A ⊆Ω;
it is nonnegative, and p(Ω) = 1. We say that two events, A ⊆Ωand B ⊆Ω,
are independent if
p(A ∩B) = p(A)p(B).
(D.1)
A random variable is a function f : Ω→R; more exactly, it is a measurable
function. We shall sometimes write r.v. for random variable. If f takes
discrete values {x1.x2, . . .} then we can define the distribution function of f,
according to
pf(j) = Prob{f = xj} = p{ω : f(ω) = xj}.
(D.2)
If f takes continuous values, then the probability that f takes a particular
real value might be zero; in that case we can define the cumulative distribution
function
Pf(x) = Prob{f ≤x} = p{ω : −∞< f(ω) ≤x}.
(D.3)
We say that a random variable f “has a probability density” if its cumulative
distribution is differentiable; we then define its density to be
pf(x) := dPf(x)
dx
;
(D.4)
and to first order in dx,
pf(x)dx = Prob{x ≤f ≤x + dx}
(D.5)
and
Prob{a ≤f ≤b} =
Z b
a pf(x) dx
(D.6)
The cumulative distribution of the standard normal distribution is denoted
Erf(x), or N(x) in this course.
194

D.2
Expectation, moments and generating functions
The expectation of the random variable f, defined abstractly by
E[f] :=
Z
f(ω)p(dω)
(D.7)
in terms of the measure p, reduces when the space Ωis discrete, to
E[f] =
X
ω
f(ω)p(ω).
(D.8)
Exercise D.1 Show that when Ωis discrete, the mean can be found in terms
of the probability distribution pf of f and the values xj of f according to
E[f] =
X
j
xjpf(j).
(D.9)
In the continuous case, it can be shown that
E[f] =
Z ∞
−∞xpf(x) dx.
(D.10)
The n-th moment, mn(f) of the r.v. f, is defined to be
mn(f) := E[f n]
(D.11)
which in the discrete case gives
mn =
X
ω
(f(ωj))n p(ω) =
X
j
xn
j pf(j);
(D.12)
in the continuous case we get
mn = E[f n] =
Z ∞
−∞xnpf(x) dx.
(D.13)
It is clear that m1(f) is the expectation of f; it is not hard to show
Exercise D.2 The variance of f, defined by
V [f] := E[(f −m1)2],
(D.14)
is given by V [f] = m2 −m2
1.
195

The moment generating function is defined as
M(θ) :=
∞
X
n=0
θn
n! mn =
X
n
E[f n]θn/n! = E[eθf].
(D.15)
This definition is only possible when the series converges, say for |θ| small.
In that case, by Taylor’s theorem, M determines the moments:
mn = dnM
dθn
θ=0
.
(D.16)
It can be shown that M also determines the probability distribution of f;
indeed, mn is determined by pf(x), according to eqs. (D.12,D.13); in the
latter case, M is the Laplace transform of pf:
M(θ) =
Z ∞
−∞eθxpf(x) dx;
(D.17)
(if the integral converges); it follows that pf(x) is the inverse Laplace trans-
form of M.
Exercise D.3 Let f be N(m, V ); that is,
pf(x) =
1
(2πV )1/2 exp{−(x −m)2
2V
};
(D.18)
Show that m is the expectation (the first moment) and that V is the variance
of f.
Exercise D.4 Find the n-th moments of a standard normal r.v., with dis-
tribution N(0, 1).
D.3
Several random variables
In terms of the sample space, Ω, two random variables f, and g, are just two
functions on Ω. Given a probability on Ω, each will have its own distribution,
pf and pg.
In order to discuss the correlation between these, we should
consider the joint distribution.
In the case of r.v.
with discrete values,
{xj}, {yk}, say, the joint distribution of f and g is defined as
pf,g(j, k) = Prob{ω : f(ω) = xj and g(ω) = yk}.
(D.19)
196

We say that two r.v., f and g, are independent if the pairs of events, A and
B, of the form
A
=
{ω ∈Ω: a < f(ω) ≤b}
(D.20)
B
=
{ω ∈Ω: c < g(ω) ≤d}
(D.21)
are independent for all real numbers a, b, c, d; see eq. (D.1).
Exercise D.5 Show that if both f and g take discrete values, then they are
independent if and only if
pf,g(j, k) = pf(j)pg(k), for all j, k.
(D.22)
If both f and g take continuous values, we can define the joint cumulative
distribution function Pf,g to be
Pf,g(x, y) := Prob{ω ∈Ω: f(ω) ≤x and g(ω) ≤y}.
(D.23)
If Pf,g is differentiable with respect to x and y, we say that f and g have a
joint density function, which is defined to be
pf,g(x, y) := ∂2Pf,g
∂x∂y .
(D.24)
Then the probability that f lies between x and x + dx, and simultaneously
g lies between y and y + dy, is, to second order
Prob{ω ∈Ω: x ≤f(ω) ≤x + dx and y ≤g(ω) ≤y + dy} = pf,g(x, y)dx dy.
(D.25)
Again, f and g are independent if and only if
pf,g(x, y) = pf(x)pg(y)
for all x, y.
(D.26)
The correlation between f and g is defined as
C(f, g) = E[fg] −E[f]E[g].
(D.27)
Exercise D.6 If f and g have discrete values, and are independent, show
that the correlation between them is zero. Show the same, if f and g have a
joint density.
197

It is not in general true that uncorrelated r.v. are independent. However, if
f and g are jointly normal, then they are independent if and only if they are
uncorrelated. We say that the r.v. f and g are jointly normal if they have a
joint density, and it is given by a function of the form
pf,g(x, y) = const. exp{−αx2 + βxy −γy2 + ax + by}.
(D.28)
Here, α > 0, γ > 0, and β must be such that the quadratic expression tends
to zero at infinity in all directions; a and b are any real numbers, and the
constant is such that the total integral over R2 is unity.
The joint n, r moment of f and g is defined to be
mn,r = E[f ngr], n = 0, 1, 2 . . . ; r = 0, 1, 2, . . . .
(D.29)
¿From this we can define the joint moment generating function to be
Mf,g(θ1, θ2) =
∞
X
n,r=0
θn
1θr
2/(n!r!)mn,r.
(D.30)
Exercise D.7 Suppose that f and g are independent, with either discrete
values, or with a joint density. Show that
Mf,g(θ1, θ2) = Mf(θ1)Mg(θ2)
for all
θ1, θ2.
(D.31)
Also, show the converse.
Exercise D.8 Let f and g be independent, with either discrete value or a
joint density. Show that the r.v f + g has generating function Mf+g given by
Mf+g(θ) = Mf(θ)Mg(θ).
(D.32)
Exercise D.9 Show that the joint moment generating function of the jointly
normal r.v. f and g is the exponential of a quadratic function of θ1 and θ2;
conversely, if the joint moment generating function is the exponential of a
quadratic function of θ1 and θ2, then the r.v. are jointly normal.
Exercise D.10 Let S be the sum f + g of jointly normal r.v f and g; show
that S is normal.
198

We can consider n random variables f1, . . . , fn, with joint probability density
p1,...n(x1, . . . , xn). This means that each fj takes continuous values, and that
Prob{ω ∈Ω: a1
≤
f1(ω) ≤b1 and . . . and an ≤fn(ω) ≤bn}
=
Z b1
a1
. . .
Z bn
an
p1...n(x1, . . . , xn)dx1 . . . dxn.
We say that {fk} are jointly normal if the density has the form
p(x1, . . . , xn) = const. exp{−1
2x.A.x
T + x.c
T }
(D.33)
for some positive definite n×n matrix A, and some row vector c = (c1, . . . , cn).
Here we have written x as a 1 × n row vector, and x
T is its transpose, the
column vector.
Exercise D.11 Let fk, k = 1, . . . , n be n jointly normal r.v. Show that the
joint moment generating function
M(θ1, . . . , θn) := E[eθ1f1+...+θnfn]
(D.34)
is the exponential of a quadratic expression in {θk}. [Hint: Show first that
by a suitable choice of α1, . . . , αn we can change the variable of integration
from x1, . . . xn to y1 = x1 + α1, . . . , yn = xn + αn, in such a way that the new
density, as a function of {yk}, has the form
p(y) = const. exp{y.A.y
T }.
(D.35)
Then, write A = SS
T in terms of suitable matrices S, and change the variable
of integration to z = yS.]
D.4
Conditional probability and expectation
Suppose that Ωis the sample space, and p a given probability on Ω, so that
p(A) is given for every event A ⊆Ω. Suppose that we are told that the
outcome ω lies in some subset B, but we are told no further information.
Bayes said the probability that ω lies in the set A ⊆Ωis modified by the
information we have obtained; p(A) should be replaced by the conditional
probability, given B, written p(A|B), where
p(A|B) := p(A ∩B)/p(B).
(D.36)
199

The definition requires that p(B) ̸= 0. Notice that p(A|B) is itself a proba-
bility on Ω; that is, for A ⊆Ω, we have
p(A|B)
≥
0
(D.37)
p(Ω|B)
=
1
(D.38)
p(A1 ∪A2|B)
=
p(A1|B) + p(A2|B) −p(A1 ∩A2|B)
(D.39)
By restricting, p(ω|B) is a probability on B.
If it happen that A and B are independent, then p(A ∩B) = p(A)p(B),
and from eq. (D.36) we see that p(A|B) = p(B).
Thus in this case no
information about A is contained in the occurrence of the event B, and it
makes no difference to the probability of A whether we know B or not.
Another case of interest is when A ⊆B; then A ∩B = A, and we see:
p(A|B) = p(A)/p(B)
(D.40)
which obviously gives
p(A) = p(A|B)p(B).
(D.41)
This product structure does not express the independence of A and B; indeed,
in this case A implies B, so they cannot be independent.
We have in mind that Ωconsists of the set of price histories from t = 0,
and we are given the price at some later time, say t = 1. This information,
not available at t = 0, increases our information and modifies the probability
we assign to the remaining possibilities. Suppose that we have two time-
steps, as in the figure:
S ©©©©
* S0
p0
HHHH
j S1
p1




B

©©©©
* S00
˜p00
HHHH
j S01
˜p01
©©©©
* S10
˜p10
HHHH
j S11
˜p11
(D.42)
The possible paths can be labelled by the symbols {S00, S01, S10, S11} as
usual.
Remember that there are four possible price histories, even if nu-
merically S01 = S10, as in the binomial model. For this reason, we keep the
200

symbols distinct. Thus, Ω= {00, 01, 10, 11}, and has four elements. Suppose
we learn that at time t = 1 the price went up to S0, rather that going down to
S1. Then only the paths S00 and S01 are possible. Thus, this information on
the price at t = 1 means that the outcome must lie in the set B = {00, 01},
shown, and our new probabilities are
p({00}|S0) = p00,
say
(D.43)
p({01}|S0) = p01,
say.
(D.44)
The two possible outcomes, {00} and {01} are subsets of B, the given event;
the original probability, p, at t = 0 before we had any info, can then got from
eq. (D.41), and is thus:
p(ω = 00)
=
p(S0)p(00|S0) = p0p00
(D.45)
p(ω = 01)
=
p(S0)p(01|S0) = p0p01.
(D.46)
In the same way, if we knew that S1 occurred at t = 1 we introduce the
conditional probabilities
p({10}|S1)
=
p10
say
(D.47)
p({11}|S1)
=
p11
say;
(D.48)
then the original probabilities of 10 and 11 are given by eq. (D.41):
p(ω = 10)
=
p(S1)p(10|S1) = p1p10
(D.49)
p(ω = 11)
=
p(S1)p(11|S1) = p1p11.
(D.50)
These are the formulae we used to find the probability of the prices at time
t = 2.
Consider now three steps of the time. If we are given that the price-
history went through S0 at time t = 1, and were also told the step taken at
time t = 2, the later info must be compatible with that earlier. Thus the
position at time t = 2 must be either 00 or 01. Say it is 00. Then the info at
time t = 1 is summarised by saying that ω ∈B in the figure below, and the
info at time t = 2 further restricts the path to lies in the set C ⊆B. Then
we see that A ∩C = A ∩B ∩C, and so for any event A,
201

S ©©©©
* S0
HHHH
j S1
©©©©
* S00
HHHH
j S01
©©©©
* S10
HHHH
j S11




C
©
©

#
"
 
!
B

©©©©
* S000
- S001
©©©©
* S010
- S011
- S100
HHHH
j S101
- S110
HHHH
j S111
(D.51)
p(A|C)
=
p(A ∩B ∩C)/p(C) = p(A ∩B ∩C))/p(B)p(C|B)
=
p(A ∩C|B)/p(C|B) = p((A|B)|C)
(D.52)
The last expression, p((A|B)|C), is the conditioning of the (conditional)
probability p(•|B), by the info ω ∈C.
We see from it that if B = C,
p((A|B)|B) = p(A|B), so the giving of known info does not alter the proba-
bility. More generally, we see that we get the same result, p(A|C), whether
we feed the info in two steps, conditioning as we go, or just use the full info
in one step.
The conditional expectation E[f|B] of a r.v. f, given B, is just the ex-
pectation of f using a conditional probability p(ω|B). Thus, in the discrete
case,
E[f|B] =
X
ω
f(ω)p(ω|B) =
X
j
xj
X
ω:f(ω)=xj
p(ω|B).
(D.53)
The expression
pf(j|B) :=
X
ω:f(ω)=xj
p(ω|B)
(D.54)
is called the conditional probability distribution of f, given B. It enables us
to compute all the conditional moments of f.
In the above example, we determined the set B, on which we condition,
by giving the value of the r.v. S1, and we got the set C by giving the values
of the two r.v. S1 and S2. More generally, we can condition a probability p
202

by giving the values of a collection of random variables f1, . . . , fN. Thus, in
the discrete case,
p(ω|f1 = x1, f2 = x2, . . . , fN = xN) =
p(ω)
P
ω:f1(ω)=x1...fN (ω)=xN p(ω)
(D.55)
if ω obeys the condition, and is zero otherwise. As before, we get the same
result whether we use this definition, or condition p in stages, using the info
one bit at a time in any order. In the discrete case this is just limiting the
sum on the r.h.s. of eq. (D.55) a bit at a time.
In the continuous case, we talk of conditional density functions. If we have
a joint probability density p(x1, x2, . . . , xn) for n random variables f1, . . . , fn,
with continuous values, then a condition such as f1 = X1 leads to the condi-
tional density, which is obtained by putting x1 = X1 in the joint density p,
and dividing by a normalising factor:
p(x2, x3, . . . , xn|f1 = X1) =
p(X1, x2, . . . , xn)
R p(X1, x2, . . . , xn)dx2dx3 . . . dxn.
(D.56)
Similarly, we can condition on any subcollection of f1, . . . , fn.
The conditional expectation E[f|f1 = X1, f2 = X2, . . . , fN], written
E[f|{fi}], is clearly a function of X1, . . . , XN. These must be possible values
of these r.v.; that is, there must be a point ω ∈Ωsuch that fk(ω) = Xk for
k = 1 . . . N. As we vary ω, we get different conditionings. From this point
of view, we can leave the values open, and consider the conditional expec-
tation E[f|f1, . . . , fN] as a function of ω. That is, it is a random variable!
As we vary f too, we get different random variables for E[f|f1, . . . , fN]. So,
E[•|{fi}] is an operator that takes the random variable f to the random vari-
able E[f|{fi}]. It is clear that the map f 7→E[f|{fi}] is linear in the variable
f; it is also true that E[g|{fi}] = g, for all g in the span of {fi} (exercise).
We have seen that the giving of known info does not alter a probability al-
ready conditioned to it. This leads to the nice result that the conditional
expectation relative to a given set of functions is a projection: applied twice
to a random variable it gives the same result as applying it once (exercise).
Moreover, applying it twice, once with a large amount of info, and then with
a smaller amount, is the same as applying it with the smaller amount. This is
because E is the projection onto the algebra generated by the functions listed
in the conditions. In particular, the ordinary expectation can be thought of
as E[f|1], where 1 is the non-random function 1; clearly, E[f] is the trivial
function of ω. Thus
203

Exercise D.12 Suppose that Ωis discrete, and that f and f1, . . . , fn are
random variables on Ω. Show that for any probability p, we have
E[E[f|{fi}]] = E[f].
(D.57)
D.5
Filtrations and martingales
Most of this section will be new to you.
The prices of various stocks, S, and of currencies, and gold, and of bonds,
and other assets, become known to us, first at t = 1, then at t = 2, up to
the present time, t = t. It is clear that as t increases, we are in possession
of an increasing amount of info. According to Bayes, we should condition
our probability as we go. We have seen that we do not in general know the
actual probability that the share will go up, or down; but the correct price
of a derivative has been seen to be expressible in terms of the risk-neutral
probabilities, rather than the actual market probabilities. So we shall find it
useful to develop the theory of conditioning for various probabilities on the
sample space, any of which is to be modified by the info we have at any given
time.
Let us limit our info to the price of a single share, S, and consider the
binomial model up to time T. Then the number of distinct price-histories
is 2T. So Ωhas 2T points. Let p be any probability on Ω. Suppose that at
time t, with t < T, we have the price-history of S up to time t. This means
that we can calculate the actual value of any derivative stock option that
depends only on the past values. Such a derivative will be a function F of
S0, S1, . . . , St. And for such a function, the conditional expectation relative
to p(ω|S0, . . . , St), using all the information, must be the actual value:
E[F|S0, S1, . . . , St] = F(S0, S1, . . . , St).
(D.58)
Thus E[•|S0, . . . , St] leaves invariant not only the random variables S0, . . . , St,
but all functions of these; this is because we have full information about all
such functions. The set of all (measurable) functions of S0, . . . , St is an al-
gebra; that is, we can add and multiply such functions, and multiply them
by real numbers, to get further functions in the set. These are all functions
of ω, since each r.v. S0 . . . is itself a function of ω. Let us call this set Ft.
Now, a function F1 say, of the variables S0, . . . , St−1 is also a function of
S0, . . . , St−1, St, which happens not to depend on the last variable. So such
204

a function is in Ft. Thus we have that Ft−1 ⊆Ft, and more generally,
if s ≤t we have Fs ⊆Ft.
(D.59)
This increasing family of function algebras, Ft, is called the filtration gen-
erated by the process St. Sometimes it is more convenient to consider the
indicator functions in the family. An indicator function is one that takes
only two values, 0 or 1. The set on which it is equal to 1 is a subset of ω,
that is, an event, and knowing the value of this function (as we do by the
time t) tells us whether this event has happened. Conversely, any function
in Ft can be written as a sum of indicator functions, with real coefficients.
The information in the filtration can be regarded as a family of events whose
occurence (or not) is known by the time t. This family of events is sometimes
also called the filtration, and is denoted by Ft as well. It is likewise an in-
creasing family, as time increases. In either case, the conditional expectation
of a random variable, f given all the information up to time t, is denoted
E[f|Ft].
Martingales
Suppose that Ωis a sample space, and p a probability on Ω.
Let Ft
be the filtration generated by a process St. Let Xt be a process adapted to
the filtration, that is, at any time t Xt is known if the price-history of St
is known; this is nothing other than the condition that Xt ∈Ft for any t.
Thus, Xt is some derivative based on the share price of Ss, involving only
s ≤t. We say that Xt is a martingale if it obeys
E[Xt|Fs] = Xs, for all s ≤t.
(D.60)
This says in a way that the present value of the derivative Xs is the expected
value at any t in the future, given the known past history up to time s of
the share S on which the derivative is based. As an example of a martingale,
let Y be any random variable.
Then put Xt = E[Y |Ft].
If s ≤t, the
family Fs is smaller than the family F t, (or the same); then we may use the
principle that double conditioning, as given by eq. (D.57), gives the same as
one conditioning onto the smaller algebra; indeed, eq. (D.57) is true whatever
the initial probability was, so we may use it starting with the conditioned
probability at time s; then we see that Xt is a martingale:
E[Xt|Fs] = E[E[Y |Ft]|Fs] = E[Y |Fs] = Xs.
(D.61)
205
