# General Equilibrium & Asset Pricing

!!! info "Source"
    **Mathematical Economics and Finance** by Michael Harrison and Patrick Waldron, 1998.
    These notes are used for educational purposes.

## Consumption and Investment Theory

60
3.6. DUALITY
Revised: December 2, 1998

61
Part II
APPLICATIONS
Revised: December 2, 1998


CHAPTER 4. CHOICE UNDER CERTAINTY
63
Chapter 4
CHOICE UNDER CERTAINTY
4.1
Introduction
[To be written.]
4.2
Definitions
There are two possible types of economy which we could analyse:
• a pure exchange economy, in which households are endowed directly with
goods, but there are no firms, there is no production, and economic activity
consists solely of pure exchanges of an initial aggregate endowment; and
• a production economy, in which households are further indirectly endowed
with, and can trade, shares in the profit or loss of firms, which can use part
of the initial aggregate endowment as inputs to production processes whose
outputs are also available for trade and consumption.
Economies of these types comprise:
• H households or consumers or agents or (later) investors or, merely, indi-
viduals, indexed by the subscript1 h;
• N goods or commodities, indexed by the superscript n; and
• (in the case of a production economy only) F firms, indexed by f.
1Notation in what follows is probably far from consistent in regard to superscripts and sub-
scripts and in regard to ith or nth good and needs fixing.
Revised: December 2, 1998

64
4.2. DEFINITIONS
This chapter concentrates on the theory of optimal consumer choice and of equi-
librium in a pure exchange economy. The theory of optimal production decisions
and of equilibrium in an economy with production is mathematically similar.
Goods can be distinguished from each other in many ways:
• obviously, by intrinsic physical characteristics, e.g. apples or oranges.
• by the time at which they are consumed, e.g. an Easter egg delivered before
Easter Sunday or an Easter egg delivered after Easter Sunday. (While all
trading takes place simultaneously in the model, consumption can be spread
out over many periods.)
• by the state of the world in which they are consumed, e.g. the service pro-
vided by an umbrella on a wet day or the service which it provides on a dry
day. (Typically, the state of the world can be any point ω in a sample space
Ω.)
The important characteristics of household h are that it is faced with the choice of
a consumption vector or consumption plan or consumption bundle, xh =

x1
h, . . . , xN
h

,
from a (closed, convex) consumption set, Xh. Typically, Xh = ℜN
+. More gener-
ally, consumer h’s consumption set might require a certain subsistence consump-
tion of some commodities, such as water, and rule out points of ℜN
+ not meeting
this requirement. The household’s endowments are denoted eh ∈ℜN
+ and can be
traded.
In a production economy, the shareholdings of households in firms are denoted
ch ∈ℜF,
A consumer’s net demand is denoted zh ≡xh −eh ∈ℜN.
Each consumer is assumed to have a preference relation or (weak) preference
ordering which is a binary relation on the consumption set Xh (?, Chapter 7).
Since each household will have different preferences, we should really denote
household h’s preference relation ⪰h, but the subscript will be omitted for the
time being while we consider a single household. Similarly, we will assume for
the time being that each household chooses from the same consumption set, X,
although this is not essential.
Recall (see ?) that a binary relation R on X is just a subset R of X × X or a
collection of pairs (x, y) where x ∈X and y ∈X.
If (x, y) ∈R, we usually just write xRy.
Thus x ⪰y means that either x is preferred to y or the consumer is indifferent
between the two (i.e. that x is at least as good as y).
The following properties of a general relation R on a general set X are often of
interest:
Revised: December 2, 1998

CHAPTER 4. CHOICE UNDER CERTAINTY
65
1. A relation R is reflexive
⇐⇒
xRx ∀x ∈X
2. A relation R is symmetric
⇐⇒
xRy ⇒yRx
3. A relation R is transitive
⇐⇒
xRy, yRz =⇒xRz
4. A relation R is complete
⇐⇒
∀x, y ∈X either xRy or yRx (or both) (in other words a complete relation
orders the whole set)
An indifference relation, ∼, and a strict preference relation, ≻, can be derived
from every preference relation:
1. x ≻y means x ⪰y but not y ⪰x
2. x ∼y means x ⪰y and y ⪰x.
The utility function u : X →ℜrepresents the preference relation ⪰if
u(x) ≥u(y) ⇐⇒x ⪰y.
If f: ℜ→ℜis a monotonic increasing function and u represents the preference
relation ⪰, then f ◦u also represents ⪰, since
f (u(x)) ≥f (u(y)) ⇐⇒u(x) ≥u(y) ⇐⇒x ⪰y.
If X is a countable set, then there exists a utility function representing any pref-
erence relation on X. To prove this, just write out the consumption plans in X in
order of preference, and assign numbers to them, assigning the same number to
any two or more consumption plans between which the consumer is indifferent.
If X is an uncountable set, then there may not exist a utility function representing
every preference relation on X.
Revised: December 2, 1998

66
4.3. AXIOMS
4.3
Axioms
We now consider six axioms which it are frequently assumed to be satisfied by
preference relations when considering consumer choice under certainty. (Note
that symmetry would not be a very sensible axiom!) Section 5.5.1 will consider
further axioms that are often added to simplify the analysis of consumer choice
under uncertainty. After the definition of each axiom, we will give a brief ratio-
nale for its use.
Axiom 1 (Completeness) A (weak) preference relation is complete.
Completeness means that the consumer is never agnostic.
Axiom 2 (Reflexivity) A (weak) preference relation is reflexive.
Reflexivity means that each bundle is at least as good as itself.
Axiom 3 (Transitivity) A (weak) preference relation is transitive.
Transitivity means that preferences are rational and consistent.
Axiom 4 (Continuity) The preference relation ⪰is continuous i.e. for all con-
sumption plans y ∈X the sets By ≡{x ∈X : x ⪰y} and Wy = {x ∈X : y ⪰
x} are closed sets.
Consider the picture when N = 2:
We will see shortly that By, the set of consumption plans which are better than or
as good as y, and Wy, the set of consumption plans which are worse than or as
good as y, are just the upper contour sets and lower contour sets respectively of
utility functions, if such exist.
E.g. consider lexicographic preferences:
Lexicographic preferences violate the continuity axiom. A consumer with such
preference prefers more of commodity 1 regardless of the quantities of other com-
modities, more of commodity 2 if faced with a choice between two consumption
plans having the same amount of commodity 1, and so on.
In the picture, the consumption plan y lies in the lower contour set Wx∗but Bϵ (y)
never lies completely in Wx∗for any ϵ. Thus, lower contour sets are not open, and
upper contour sets are not closed.
Theorems on the existence of continuous utility functions have been proven by
Gerard Debreu, Nobel laureate, whose proof used Axioms 1–4 only (see ? or ?)
and by Hal Varian, whose proof was simpler by virtue of adding an additional
axiom (see ?).
Revised: December 2, 1998

CHAPTER 4. CHOICE UNDER CERTAINTY
67
Theorem 4.3.1 (Debreu) If X is a closed and convex set and ⪰is a complete,
reflexive, transitive and continuous preference relation on X, then ∃a continuous
utility function u: X →ℜrepresenting ⪰.
Proof For the proof of this theorem, see ?.
Q.E.D.
Axiom 5 (Greed) Greed is incorporated into consumer behaviour by assuming
either
1. Strong monotonicity:
If X = ℜN
+, then ⪰is said to be strongly monotonic iff whenever xn ≥yn∀n
but x ̸= y, x ≻y. [x = (x1, . . . , xN) &c.]; or
2. Local non-satiation:
∀x ∈X, ϵ > 0, ∃x′ ∈Bϵ (x) s.t. x′ ≻x
The strong monotonicity axiom is a much stronger restriction on preferences than
local non-satiation; however, it greatly simplifies the proof of existence of utility
functions.
We will prove the existence, but not the continuity, part of the following weaker
theorem.
Theorem 4.3.2 (Varian) If X = ℜN
+ and ⪰is a complete, reflexive, transitive,
continuous and strongly monotonic preference relation on X, then ∃a continuous
utility function u: X →ℜrepresenting ⪰.
Proof (of existence only (?, p.97))
Pick a benchmark consumption plan, e.g. 1 ≡(1, 1, . . . , 1).
The idea is that the utility of x is the multiple of the benchmark consumption plan
to which x is indifferent.
By strong monotonicity, the sets {t ∈ℜ: t1 ⪰x} and {t ∈ℜ: x ⪰t1} are both
non-empty.
By continuity of preferences, both are closed (intersection of a ray through the
origin and a closed set); and by completeness, they cover ℜ.
By connectedness of ℜ, they intersect in at least one point, u(x) say, and x ∼
u(x)1.
Now
x ⪰y
⇐⇒
u(x)1 ⪰u(y)1
⇐⇒
u(x) ≥u(y)
where the first equivalence follows from transitivity of preferences and the second
from strong monotonicity.
The assumption that preferences are reflexive is not used in establishing existence
of the utility function, so it can be inferred that it is required to establish continuity.
Revised: December 2, 1998

68
4.3. AXIOMS
Q.E.D.
The rule which the consumer will follow is to choose the most preferred bundle
from the set of affordable alternatives (budget set), in other words the bundle at
which the utility function is maximised subject to the budget constraint, if one
exists.
We know that an optimal choice will exist if the utility function is continuous and
the budget set is closed and bounded.
If the utility function is differentiable, we can go further and use calculus to find
the maximum.
So we usually assume differentiability.
If u is a concave utility function, then f ◦u, which also represents the same prefer-
ences, is not necessarily a concave function (unless f itself is a convex function).
In other words, concavity of a utility function is a property of the particular repre-
sentation and not of the underlying preferences. Notwithstanding this, convexity
of preferences is important, as indicated by the use of one or other of the follow-
ing axioms, each of which relates to the preference relation itself and not to the
particular utility function chosen to represent it.
Axiom 6 (Convexity) There are two versions of this axiom:
1. Convexity:
The preference relation ⪰is convex ⇐⇒
x ⪰y =⇒λx + (1 −λ) y ⪰y.
2. Strict convexity:
The preference relation ⪰is strictly convex ⇐⇒
x ⪰y =⇒λx + (1 −λ) y ≻y.
The difference between the two versions of the convexity axiom basically amounts
to ruling out linear segments in indifference curves in the strict case.
Theorem 4.3.3 The preference relation ⪰is (strictly) convex if and only if every
utility function representing ⪰is a (strictly) quasiconcave function.
Proof In either case, both statements are equivalent to saying that
u(x) ≥u(y) =⇒u (λx + (1 −λ) y) ≥(>)u(y).
(4.3.1)
Revised: December 2, 1998

CHAPTER 4. CHOICE UNDER CERTAINTY
69
Q.E.D.
Theorem 4.3.4 All upper contour sets of a utility function representing convex
preferences are convex sets (i.e. indifference curves are convex to the origin for
convex preferences).
It can be seen that convexity of preferences is a generalisation of the two-good
assumption of a diminishing marginal rate of substitution.
Axiom 7 (Inada Condition) This axiom seems to be relegated to some other cat-
egory in many existing texts and its attribution to Inada is also difficult to trace. It
is not easy to see how to express it in terms of the underlying preference relation
so perhaps it cannot be elevated to the status of an axiom. Should it be expressed
as:
lim
xi→0
∂u
∂xi
= ∞
or as
lim
xi→∞
∂u
∂xi
= 0?
The Inada condition will be required to rule out corner solutions in the consumer’s
problem. Intuitively, it just says that indifference curves may be asymptotic to the
axes but never reach them.
4.4
Optimal Response Functions:
Marshallian and Hicksian Demand
4.4.1
The consumer’s problem
A consumer with consumption set Xh, endowment vector eh ∈Xh, sharehold-
ings ch ∈ℜF and preference ordering ⪰h represented by utility function uh who
desires to trade his endowment at prices p ∈ℜN
+ faces an inequality constrained
optimisation problem:
max
x∈Xh uh (x) s.t. p⊤x ≤p⊤eh + c⊤
h Π (p) ≡Mh
(4.4.1)
where Π (p) is the vector of the F firms’ maximised profits when prices are p.
Constraining x to lie in the consumption set normally just means imposing non-
negativity constraints on the problem. From a mathematical point of view, the
source of income is irrelevant, and in particular the distinction between pure ex-
change and production economy is irrelevant. Thus, income can be represented
by M in either case.
Revised: December 2, 1998

70
4.4. OPTIMAL RESPONSE FUNCTIONS:
MARSHALLIAN AND HICKSIAN DEMAND
Since the constraint functions are linear in the choice variables x, the Kuhn-Tucker
theorem on second order conditions (Theorem 3.5.2) can be applied, provided that
the utility function uh is pseudo-concave. In this case, the first order conditions
identify a maximum.
The Lagrangian, using multipliers λ for the budget constraint and µ ∈ℜN for the
non-negativity constraints, is
uh (x) + λ

M −p⊤x

+ µ⊤x.
(4.4.2)
The first order conditions are given by the (N-dimensional) vector equation:
u′
h (x) + λ (−p) + µ = 0N
(4.4.3)
and the sign condition λ ≥0 with λ > 0 if the budget constraint is binding.
We also have µ = 0N unless one of the non-negativity constraints is binding:
Axiom 7 would rule out this possibility.
Now for each p ∈ℜN
++ (ruling out bads, or goods with negative prices, and even
(see below) free goods), eh ∈Xh, and ch ∈ℜF, or for each p, Mh combination,
there is a corresponding solution to the consumer’s utility maximisation problem,
denoted xh (p, eh, ch) or xh (p, Mh). The function (correspondence) xh is often
called a Marshallian demand function (correspondence).
If the utility function uh is also strictly quasiconcave (i.e. preferences are strictly
convex), then the conditions of the Kuhn-Tucker theorem on uniqueness (Theo-
rem 3.5.3) are satisfied. In this case, the consumer’s problem has a unique solu-
tion for given prices and income, so that the optimal response correspondence is a
single-valued demand function. On the other hand, the weak form of the convexity
axiom would permit a multi-valued demand correspondence.
4.4.2
The No Arbitrage Principle
Definition 4.4.1 An arbitrage opportunity means the opportunity to acquire a
consumption vector or its constituents, directly or indirectly, at one price, and
to sell the same consumption vector or its constituents, directly or indirectly, at a
higher price.
Theorem 4.4.1 (The No Arbitrage Principle) Arbitrage opportunities do not ex-
ist in equilibrium in an economy in which at least one agent has preferences which
exhibit local non-satiation.2
2The No Arbitrage Principle is also known as the No Free Lunch Principle, or the Law of One
Price
Revised: December 2, 1998

CHAPTER 4. CHOICE UNDER CERTAINTY
71
Proof If preferences exhibit local non-satiation, then Marshallian demand is not
well-defined if the price vector permits arbitrage opportunities.
If the no arbitrage principle doesn’t hold, then any individual can increase wealth
without bound by exploiting the available arbitrage opportunity on an infinite
scale. Thus there is no longer a budget constraint and, since local non-satiation
rules out bliss points, utility too can be increased without bound.
When we come to consider equilibrium, we will see that if even one individual has
preferences exhibiting local non-satiation, then equilibrium prices can not permit
arbitrage opportunities.
Q.E.D.
Examples are usually in the financial markets, in a multi-period context, e.g. cov-
ered interest parity, term structure of interest rates, &c. The most powerful appli-
cation is in the derivation of option-pricing formulae, since options can be shown
to be identical to various synthetic portfolios made up of the underlying security
and the riskfree security.
The simple rule for figuring out how to exploit arbitrage opportunities is ‘buy
low, sell high’. With interest rates and currencies, for example, this may be a
non-trivial calculation.
Exercise: If the interest rate for one-year deposits or loans is r1 per annum com-
pounded annually, the interest rate for two-year deposits or loans is r2 per annum
compounded annually and the forward interest rate for one year deposits or loans
beginning in one year’s time is f12 per annum compounded annually, calculate the
relationship that must hold between these three rates if there are to be no arbitrage
opportunities.
Solution: (1 + r1) (1 + f12) = (1 + r2)2.
4.4.3
Other Properties of Marshallian demand
Other noteworthy properties of Marshallian demand include the following:
1. If preferences exhibit local non-satiation, then the budget constraint is bind-
ing.
This is because no consumption vector in the interior of the budget set can
maximise utility as some nearby consumption vector will always be both
preferred and affordable. At the optimum, on the budget hyperplane, the
nearby consumption vector which is preferred will not be affordable.
2. If p includes a zero price (pn = 0 for some n), then xh (p, Mh) may not be
well defined.
Revised: December 2, 1998

72
4.4. OPTIMAL RESPONSE FUNCTIONS:
MARSHALLIAN AND HICKSIAN DEMAND
This is because, at least in the case of strongly monotonic preferences, the
consumer will seek to acquire and consume an infinite amount of the free
good, thereby increasing utility without bound. For this reason, it is neater
to define Marshallian demand only on the open non-negative orthant in ℜN,
namely ℜN
++.
3. The demand xh (p, Mh) is independent of the representation uh of the un-
derlying preference relation ⪰h which is used in the statement of the con-
sumer’s problem.
4. xh (p, Mh) is homogenous of degree 0 in p, Mh.
In other words, if all prices and income are multiplied by α > 0, then
demand does not change:
xh (αp, αMh) = xh (p, Mh) .
(4.4.4)
5. Demand functions are continuous.
This follows from the theorem of the maximum (Theorem 3.5.4). It fol-
lows that small changes in prices or income will lead to small changes in
quantities demanded.
4.4.4
The dual problem
Consider also the (dual) expenditure minimisation problem:
min
x p⊤x s.t. uh (x) ≥¯u.
(4.4.5)
In other words, what happens if expenditure is minimised subject to a certain level
of utility, ¯u, being attained?
The solution (optimal response function) is called the Hicksian or compensated
demand function (or correspondence) and is usually denoted hh (p, ¯u).
There should really be a more general discussion of duality, based on the mean-
variance problem as well as the utility maximisation/expenditure minimisation
problems.
If the local non-satiation axiom holds, then the constraints are binding in both
the utility-maximisation and expenditure-minimisation problems, and we have a
number of duality relations. In particular, there will be a one-to-one correspon-
dence between income M and utility ¯u for a given price vector p. The expenditure
function and the indirect utility function will then act as a pair of inverse envelope
functions mapping utility levels to income levels and vice versa respectively.
Revised: December 2, 1998

CHAPTER 4. CHOICE UNDER CERTAINTY
73
A full page table setting out exactly the parallels between the two problems is
called for here.
The following duality relations (or fundamental identities as ? calls them) will
prove extremely useful later on:
e (p, v (p, M))
=
M
(4.4.6)
v (p, e (p, ¯u))
=
¯u
(4.4.7)
x (p, M)
=
h (p, v (p, M))
(4.4.8)
h (p, ¯u)
=
x (p, e (p, ¯u))
(4.4.9)
These are just equations (3.6.5)–(3.6.8) adapted to the notation of the consumer’s
problem.
4.4.5
Properties of Hicksian demands
As in the Marshallian approach, if preferences are strictly convex, then any solu-
tion to the expenditure minimisation problem is unique and the Hicksian demands
are well-defined single valued functions.
It’s worth going back to the uniqueness proof with this added interpretation. If two
different consumption vectors minimise expenditure, then they both cost the same
amount, and any convex combination of the two also costs the same amount. But
by strict convexity, a convex combination yields higher utility, and nearby there
must, by continuity, be a cheaper consumption vector still yielding utility ¯u.
If preferences are not strictly convex, then Hicksian demands may be correspon-
dences rather than functions.
Hicksian demands are homogenous of degree 0 in prices:
hh (αp, ¯u) = hh (p, ¯u) .
(4.4.10)
4.5
Envelope Functions:
Indirect Utility and Expenditure
Now consider the envelope functions corresponding to the two approaches:
1. The indirect utility function:
vh (p, M) ≡uh (xh (p, M))
(4.5.1)
2. The expenditure function:
eh (p, ¯u) ≡p⊤hh (p, ¯u) .
(4.5.2)
Sometimes we meet two other related functions:
Revised: December 2, 1998

74
4.5. ENVELOPE FUNCTIONS:
INDIRECT UTILITY AND EXPENDITURE
3. The money metric utility function
mh (p, x) ≡eh (p, uh (x))
(4.5.3)
is the (least) cost at prices p of being as well off as with the consumption
vector x.
4. The money metric indirect utility function
µh (p; q, M) ≡eh (p, vh (q, M))
(4.5.4)
is the (least) cost at prices p of being as well off as if prices were q and
income was M.
The following are interesting properties of the indirect utility function:
1. By the Theorem of the Maximum, the indirect utility function is continuous
for positive prices and income.
2. The indirect utility function is non-increasing in p and non-decreasing in
M.
3. The indirect utility function is quasi-convex in prices.
To see this, let B (p) denote the budget set when prices are p and let pλ ≡
λp + (1 −λ) p′.
Then B (pλ) ⊆(B (p) ∪B (p′)).
Suppose this was not the case, i.e. for some x, pλ⊤x ≤M but p⊤x >
M and p′⊤x > M. Then taking a convex combination of the last two
inequalities yields
λp⊤x + (1 −λ) p′⊤x > M,
which contradicts the first inequality.
It follows that the maximum value of uh (x) on the subset B (pλ) is less
than or equal to its maximum value on the superset B (p) ∪B (p′).
In terms of the indirect utility function, this says that
vh (pλ, M) ≤max {vh (p, M) , vh (p′, M)} ,
or that vh is quasiconvex.
4. vh (p, M) is homogenous of degree zero in p, M, or
vh (λp, λM) = vh (p, M) .
Revised: December 2, 1998

CHAPTER 4. CHOICE UNDER CERTAINTY
75
The following are interesting properties of the expenditure function:
1. The expenditure function is continuous.
2. The expenditure function itself is non-decreasing in prices, since raising the
price of one good while holding the prices of all other goods constant can
not reduce the minimum cost of attaining a fixed utility level.
3. The expenditure function is concave in prices.
To see this, we just fix two price vectors p and p′ and consider the value of
the expenditure function at the convex combination pλ ≡λp + (1 −λ) p′.
e (pλ, ¯u)
=
(pλ)⊤h (pλ, ¯u)
(4.5.5)
=
λp⊤h (pλ, ¯u) + (1 −λ) (p′)⊤h (pλ, ¯u)
(4.5.6)
≥
λp⊤h (p, ¯u) + (1 −λ) (p′)⊤h (p′, ¯u)
(4.5.7)
=
λe (p, ¯u) + (1 −λ) e (p′, ¯u) ,
(4.5.8)
where the inequality follows because the cost of a suboptimal bundle for
the given prices must be greater than the cost of the optimal (expenditure-
minimising) consumption vector for those prices.
4. The expenditure function is homogenous of degree 1 in prices:
eh (αp, ¯u) = αeh (p, ¯u) .
(4.5.9)
4.6
Further Results in Demand Theory
In this section, we present four important theorems on demand functions and the
corresponding envelope functions. Shephard’s Lemma will allow us to recover
Hicksian demands from the expenditure function. Similarly, Roy’s Identity will
allow us to recover Marshallian demands from the indirect utility function. The
Slutsky symmetry condition and the Slutsky equation provide further insights into
the properties of consumer demand.
Theorem 4.6.1 (Shephard’s Lemma.)
∂eh
∂pn (p, ¯u)
=
∂
∂pn

p⊤x + λ (uh (x) −¯u)

(4.6.1)
=
xn
(4.6.2)
which, when evaluated at the optimum, is just hn
h (p, ¯u).
In other words, the partial derivatives of the expenditure function with respect to
prices are the corresponding Hicksian demand functions.
Revised: December 2, 1998

76
4.6. FURTHER RESULTS IN DEMAND THEORY
Proof By differentiating the expenditure function with respect to the price of
good n and applying the envelope theorem (Theorem 3.4.4), we obtain Shephard’s
Lemma:
(To apply the envelope theorem, we should be dealing with an equality constrained
optimisation problem; however, if we assume local non-satiation, we know that
the budget constraint or utility constraint will always be binding, and so the in-
equality constrained expenditure minimisation problem is essentially and equality
constrained problem.)
Q.E.D.
Theorem 4.6.2 (Roy’s Identity.) Marshallian demands may be recovered from
the indirect utility function using:
xn (p, M) = −
∂v
∂pn (p, M)
∂v
∂M (p, M).
(4.6.3)
Proof For Roy’s Identity, see ?.
It is obtained by differentiating equation (4.4.7) with respect to pn, using the Chain
Rule:
v (p, e (p, ¯u)) = ¯u
implies that
∂v
∂pn (p, e (p, ¯u)) + ∂v
∂M (p, e (p, ¯u)) ∂e
∂pn (p, ¯u) = 0
(4.6.4)
and using Shephard’s Lemma gives:
∂v
∂pn (p, e (p, ¯u)) + ∂v
∂M (p, e (p, ¯u)) hn (p, ¯u) = 0
(4.6.5)
Hence
hn (p, ¯u) = −
∂v
∂pn (p, e (p, ¯u))
∂v
∂M (p, e (p, ¯u))
(4.6.6)
and expressing this last equation in terms of the relevant level of income M rather
than the corresponding value of utility ¯u:
xn (p, M) = −
∂v
∂pn (p, M)
∂v
∂M (p, M).
(4.6.7)
Q.E.D.
Revised: December 2, 1998

CHAPTER 4. CHOICE UNDER CERTAINTY
77
Theorem 4.6.3 (Slutsky symmetry condition.) All cross-price substitution effects
are symmetric:
∂hn
h
∂pm = ∂hm
h
∂pn .
(4.6.8)
Proof From Shephard’s Lemma, we can easily derive the Slutsky symmetry condi-
tions, assuming that the expenditure function is twice continuously differentiable,
and hence that
∂2eh
∂pm∂pn =
∂2eh
∂pn∂pm.
(4.6.9)
Since hm
h = ∂eh
∂pm and hn
h = ∂eh
∂pn, and the result follows.
Q.E.D.
The next result doesn’t really have a special name of its own.
Theorem 4.6.4 Since the expenditure function is concave in prices (see p. 75), the
corresponding Hessian matrix is negative semi-definite. In particular, its diagonal
entries are non-positive, or
∂2eh
∂(pn)2 ≤0,
n = 1, . . . , N.
(4.6.10)
Using Shephard’s Lemma, it follows that
∂hn
h
∂pn ≤0,
n = 1, . . . , N.
(4.6.11)
In other words, Hicksian demand functions, unlike Marshallian demand functions,
are uniformly decreasing in own price. Another way of saying this is that own
price substitution effects are always negative.
Theorem 4.6.5 (Slutsky equation.) The total effect of a price change on (Mar-
shallian) demand can be decomposed as follows into a substitution effect and an
income effect:
∂xm
∂pn (p, M) = ∂hm
∂pn (p, ¯u) −∂xm
∂M (p, M) hn (p, ¯u) ,
(4.6.12)
where ¯u ≡V (p, M).
Before proving this, let’s consider the signs of the various terms in the Slutsky
equation and look at what it means in a two-good example.
By Theorem 4.6.4, we know that own price substitution effects are always non-
positive.
[This is still on a handwritten sheet.]
Revised: December 2, 1998


## General Equilibrium Theory

78
4.7. GENERAL EQUILIBRIUM THEORY
Proof Differentiating both sides of the lth component of (4.4.9) with respect to
pn, using the Chain Rule, will yield the so-called Slutsky equation which decom-
poses the total effect on demand of a price change into an income effect and a
substitution effect.
Differentiating the RHS of (4.4.9) with respect to pn yields:
∂xm
∂pn (p, e (p, ¯u)) + ∂xm
∂M (p, e (p, ¯u)) ∂e
∂pn (p, ¯u) .
(4.6.13)
To complete the proof:
1. set this equal to ∂hm
∂pn (p, ¯u)
2. substitute from Shephard’s Lemma
3. define M ≡e (p, ¯u) (which implies that ¯u ≡V (p, M))
Q.E.D.
4.7
General Equilibrium Theory
4.7.1
Walras’ law
Walras ... 3
4.7.2
Brouwer’s fixed point theorem
4.7.3
Existence of equilibrium
4.8
The Welfare Theorems
4.8.1
The Edgeworth box
4.8.2
Pareto efficiency
Definition 4.8.1 A feasible allocation X = (x1, . . . , xH) is Pareto efficient if
there does not exist any feasible way of reallocating the same initial aggregate
endowment,
PH
h=1 xh, which makes one individual better off without making any
other worse off.
Definition 4.8.2 X is Pareto dominated by X′ = (x′
1, . . . , x′
H) if
PH
h=1 xh =
PH
h=1 x′
h, x′
h ⪰h xh ∀h and x′
h ≻h xh for at least one h.
3This material still exists only in handwritten form in Alan White’s EC3080 notes from 1991-
2. One thing missing from the handwritten notes is Kakutani’s Fixed Point Theorem which should
be quoted from ?.
Revised: December 2, 1998

CHAPTER 4. CHOICE UNDER CERTAINTY
79
4.8.3
The First Welfare Theorem
(See ?.)
Theorem 4.8.1 (First Welfare Theorem) If the pair (p, X) is an equilibrium (for
given preferences, ⪰h, which exibit local non-satiation and given endowments, eh,
h = 1, . . . , H), then X is a Pareto efficient allocation.
Proof The proof is by contradiction. Suppose that X is an equilibrium allocation
which is Pareto dominated by a feasible allocation X′.
If individual h is strictly better off under X′ or x′
h ≻h xh, then it follows that
individual h cannot afford x′
h at the equilibrium prices p or
p⊤x′
h > p⊤xh = p⊤eh.
(4.8.1)
The latter equality is just the budget constraint, which is binding since we have
assumed local non-satiation.
Similarly, if individual h is indifferent between X and X′ or x′
h ∼h xh, then it
follows that
p⊤x′
h ≥p⊤xh = p⊤eh,
(4.8.2)
since if x′
h cost strictly less than xh, then by local non-satiation some consumption
vector near enough to x′
h to also cost less than xh would be strictly preferred to
xh and xh would not maximise utility given the budget constraint.
Summing (4.8.1) and (4.8.2) over households yields
p⊤
H
X
h=1
x′
h > p⊤
H
X
h=1
xh = p⊤
H
X
h=1
eh,
(4.8.3)
(where the equality is essentially Walras’ Law).
But since X′ is feasible we must have for each good n
H
X
h=1
x′n
h ≤
H
X
h=1
en
h
and, hence, multiplying by prices and summing over all goods,
p⊤
H
X
h=1
x′
h ≤p⊤
H
X
h=1
eh.
(4.8.4)
But (4.8.4) contradicts the inequality in (4.8.3), so no such Pareto dominant allo-
cation X′
h can exist.
Q.E.D.
Before proceeding to the second welfare theorem, we need to say a little bit about
separating hyperplanes.
Revised: December 2, 1998

80
4.8. THE WELFARE THEOREMS
4.8.4
The Separating Hyperplane Theorem
Definition 4.8.3 The set
n
z ∈ℜN : p⊤z = p⊤z∗o
is the hyperplane through z∗
with normal p.
Note that any hyperplane divides ℜN into two closed half-spaces,
n
z ∈ℜN : p⊤z ≤p⊤z∗o
and
n
z ∈ℜN : p⊤z ≥p⊤z∗o
.
The intersection of these two closed half-spaces is the hyperplane itself.
In two dimensions, a hyperplane is just a line; in three dimensions, it is just a
plane.
The idea behind the separating hyperplane theorem is quite intuitive: if we take
any point on the boundary of a convex set, we can find a hyperplane through
that point so that the entire convex set lies on one side of that hyperplane. We
will essentially be applying this notion to the upper contour sets of quasiconcave
utility functions, which are of course convex sets. We will interpret the separating
hyperplane as a budget hyperplane, and the normal vector as a price vector, so that
at those prices nothing giving higher utility than the cutoff value is affordable.
Theorem 4.8.2 (Separating Hyperplane Theorem) If Z is a convex subset of
ℜN and z∗∈Z, z∗̸∈int Z, then ∃p∗̸= 0 in ℜN such that p∗⊤z∗≤p∗⊤z ∀z ∈Z,
or Z is contained in one of the closed half-spaces associated with the hyperplane
through z∗with normal p∗.
Proof Not given. See ?
Q.E.D.
4.8.5
The Second Welfare Theorem
(See ?.)
We make slightly stronger assumptions than are essential for the proof of this
theorem. This allows us to give an easier proof.
Theorem 4.8.3 (Second Welfare Theorem) If all individual preferences are strictly
convex, continuous and strictly monotonic, and if X∗is a Pareto efficient al-
location such that all households are allocated positive amounts of all goods
(x∗g
h
> 0 ∀g = 1, . . . , N; h = 1, . . . , H), then a reallocation of the initial ag-
gregate endowment can yield an equilibrium where the allocation is X∗.
Revised: December 2, 1998

CHAPTER 4. CHOICE UNDER CERTAINTY
81
Proof There are four main steps in the proof.
1. First we construct a set of utility-enhancing endowment perturbations, and
use the separating hyperplane theorem to find prices at which no such en-
dowment perturbation is affordable.
We need to use the fact (Theorem 3.2.1) that a sum of convex sets, such as
X + Y ≡{x + y : x ∈X, y ∈Y } ,
is also a convex set.
Given an aggregate initial endowment x∗=
PH
h=1 x∗
h, we interpret any vec-
tor of the form z =
PH
h=1 xh −x∗as an endowment perturbation. Now
consider the set of all ways of changing the aggregate endowment without
making anyone worse off:
Z ≡(
z ∈ℜN : ∃xn
h ≥0 ∀g, h s.t. uh (xh) ≥uh (x∗
h) & z =
H
X
h=1
xh −x∗
)
.
(4.8.5)
Z is a sum of convex sets provided that preferences are assumed to be
convex:
Z =
H
X
h=1
Xh −{x∗}
where
Xh ≡{xh : uh (xh) ≥uh (x∗
h)} .
2. Next, we need to show that the zero vector is in the set Z, but not in the
interior of Z.
To show that 0 ∈Z, we just set xh = x∗
h and observe that 0 =
PH
h=1 x∗
h −
x∗.4
The zero vector is not, however, in the interior of Z, since then Z would
contain some vector, say z∗, in which all components were strictly negative.
In other words, we could take away some of the aggregate endowment of
every good without making anyone worse off than under the allocation X∗.
But by then giving −z∗back to one individual, he or she could be made
better off without making anyone else worse off, contradicting Pareto opti-
mality, again using the assumption that preferences are strictly monotonic.
4Note also (although I’m no longer sure why this is important) that budget constraints are
binding and that there are no free goods (by the monotonicity assumption).
Revised: December 2, 1998

82
4.8. THE WELFARE THEOREMS
So, applying the Separating Hyperplane Theorem with z∗= 0, we have a
price vector p∗such that 0 = p∗⊤0 ≤p∗⊤z ∀z ∈Z.
Since preferences are monotonic, the set Z must contain all the standard
unit basis vectors ((1, 0, . . . , 0), &c.). This fact can be used to show that
all components of p∗are non-negative, which is essential if it is to be inter-
preted as an equilibrium price vector.
3. Next, we specify one way of redistributing the initial endowment in order
that the desired prices and allocation emerge as a competitive equilibrium.
All we need to do is value endowments at the equilibrium prices, and redis-
tribute the aggregate endowment of each good to consumers in proportion
to their share in aggregate wealth computed in this way.
4. Finally, we confirm that utility is maximised by the given Pareto efficient
allocation, X∗, at these prices. As usual, the proof is by contradiction: the
details are left as an exercise.
Q.E.D.
4.8.6
Complete markets
The First Welfare Theorem tells us that competitive equilibrium allocations are
Pareto optimal if markets are complete. If there are missing markets, then com-
petitive trading may not lead to a Pareto optimal allocation. We can use the Edge-
worth Box diagram to illustrate the simplest possible version of this principle.
4.8.7
Other characterizations of Pareto efficient allocations
There are a total of five equivalent characterisations of Pareto efficient allocations.
Theorem 4.8.4 Each of the following is an equivalent description of the set of
allocations which are Pareto efficient:
1. by definition, feasible allocations such that no other allocation strictly in-
creases at least one individual’s utility without decreasing the utility of any
other individual;
2. by the Welfare Theorems, equilibrium allocations for all possible distribu-
tions of the fixed initial aggregate endowment;
3. in two dimensions, allocations lying on the contract curve in the Edgeworth
box;
Revised: December 2, 1998

CHAPTER 4. CHOICE UNDER CERTAINTY
83
4. allocations which solve: 5
max
{xh:h=1,...,H}
H
X
h=1
λh [uh(xh)]
(4.8.6)
subject to the feasibility constraints
H
X
h=1
xh
=
H
X
h=1
eh
(4.8.7)
for some non-negative weights {λh}H
h=1.
5. allocations which maximise the utility of a representative agent given by
H
X
h=1
λh [uh(xh)]
(4.8.8)
where {λh}H
h=1 are again any non-negative weights.
Proof If an allocation is not Pareto efficient, then the Pareto-dominating alloca-
tion gives a higher value of the objective function in the above problem for all
possible weights.
If an allocation is Pareto efficient, then the relative weights for which the above
objective function is maximized are the ratios of the Lagrange multipliers from
the problem of maximizing any individual’s utility subject to the constraint that
all other individuals’ utilities are unchanged:
max u1(x1)
(4.8.9)
s.t.
uh(xh) = uh(x∗
h) h = 2, . . . , H
(4.8.10)
since these two problems will have the same necessary and sufficient first order
conditions.
The absolute weights corresponding to a particular allocation are not unique, as
they can be multiplied by any positive constant without affecting the maximum.
Different absolute weights (or Lagrange multipliers) arise from fixing different
individuals’ utilities in the last problem, but the relative weights will be the same.
5The solution here would be unique if the underlying utility function were concave, since linear
combinations of concave functions with non-negative weights are concave, and the constraints
specify a convex set on which the objective function has a unique optimum. This argument can
not be used with merely quasiconcave utility functions.
Revised: December 2, 1998

84
4.9. MULTI-PERIOD GENERAL EQUILIBRIUM
Q.E.D.
Note that corresponding to each Pareto efficient allocation there is at least one:
1. set of non-negative weights defining
(a) the objective function in 4. and
(b) the representative agent in 5.
and
2. initial allocation leading to the competitive equilibrium in 2.
4.9
Multi-period General Equilibrium
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
Revised: December 2, 1998

CHAPTER 5. CHOICE UNDER UNCERTAINTY
85
Chapter 5
CHOICE UNDER UNCERTAINTY
5.1
Introduction
[To be written.]
5.2
Review of Basic Probability
Economic theory has, over the years, used many different, sometimes overlapping,
sometimes mutually exclusive, approaches to the analysis of choice under uncer-
tainty. This chapter deals with choice under uncertainty exclusively in a single
period context. Trade takes place at the beginning of the period and uncertainty
is resolved at the end of the period. This framework is sufficient to illustrate the
similarities and differences between the most popular approaches.
When we consider consumer choice under uncertainty, consumption plans will
have to specify a fixed consumption vector for each possible state of nature or
state of the world. This just means that each consumption plan is a random vector.
Let us review the associated concepts from basic probability theory: probability
space; random variables and vectors; and stochastic processes.
Let Ωdenote the set of all possible states of the world, called the sample space.
A collection of states of the world, A ⊆Ω, is called an event.
Let A be a collection of events in Ω. The function P : A →[0, 1] is a probability
function if
1.
(a) Ω∈A
(b) A ∈A ⇒Ω−A ∈A
(c) Ai ∈A for i = 1, . . . , ∞⇒
S∞
i=1 Ai ∈A
(i.e. A is a sigma-algebra of events)
Revised: December 2, 1998

86
5.2. REVIEW OF BASIC PROBABILITY
and
2.
(a) P (Ω) = 1
(b) P (Ω−A) = 1 −P (A) ∀A ∈A (redundant assumption)
(c) P (
S∞
i=1 Ai) =
P∞
i=1 P (Ai) when A1, A2, . . . are pairwise disjoint
events in A.
(Ω, A, P) is then called a probability space
Note that the certainty case we considered already is just the special case of un-
certainty in which the set Ωhas only one element.
We will consider these concepts in more detail when we come to intertemporal
models.
Suppose we are given such a probability space.
The function ˜x : Ω→ℜis a random variable (r.v.) if ∀x ∈ℜ{ω ∈Ω: ˜x (ω) ≤
x} ∈A, i.e. a function is a random variable if we know the probability that the
value of the function is less than or equals any given real number.
The function F˜x : ℜ→[0, 1] : x 7→Pr (˜x ≤x) ≡P ({ω ∈Ω: ˜x (ω) ≤x}) is
known as the cumulative distribution function (c.d.f.) of the random variable ˜x.
The convention of using a tilde over a letter to denote a random variable is com-
mon in financial economics; in other fields capital letters may be reserved for ran-
dom variables. In either case, small letters usually denote particular real numbers
(i.e. particular values of the random variable).
A random vector is just a vector of random variables. It can also be thought of as
a vector-valued function on the sample space Ω.
A stochastic process is a collection of random variables or random vectors indexed
by time, e.g. {˜xt : t ∈T} or just {˜xt} if the time interval is clear from the context.
For the purposes of this part of the course, we will assume that the index set
consists of just a finite number of times i.e. that we are dealing with discrete time
stochastic processes.
Then a stochastic process whose elements are N-dimensional random vectors is
equivalent to an N|T|-dimensional random vector.
The (joint) c.d.f. of a random vector or stochastic process is the natural extension
of the one-dimensional concept.
Random variables can be discrete, continuous or mixed. The expectation (mean,
average) of a discrete r.v., ˜x, with possible values x1, x2, x3, . . . is given by
E [˜x] ≡
∞
X
i=1
xiPr (˜x = xi) .
For a continuous random variable, the summation is replaced by an integral.
Revised: December 2, 1998

CHAPTER 5. CHOICE UNDER UNCERTAINTY
87
The covariance of two random variables ˜x and ˜y is given by
Cov [˜x, ˜y] ≡E [(˜x −e [˜x]) (˜y −E [˜y])] .
The covariance of a random variable with itself is called its variance.
The expectation of a random vector is just the vector of the expectations of the
component random variables.
The variance (variance-covariance matrix) of a random vector is the (symmetric,
positive semi-definite) matrix of the covariances between the component random
variables.
Given any two random variables ˜x and ˜y, we can define a third random variable˜ϵ
by
˜ϵ ≡˜y −α −β˜x.
(5.2.1)
To specify˜ϵ completely, we can either specify α and β explicitly or fix them
implicitly by imposing (two) conditions on˜ϵ. We do the latter by insisting
1. ˜ϵ and ˜x are uncorrelated (this is not the same as assuming statistical inde-
pendence, except in special cases such as bivariate normality)
2. E [˜ϵ] = 0
It follows that:
β
=
Cov [˜x, ˜y]
Var [˜x]
(5.2.2)
and
α
=
E [˜y] −βE [˜x] .
(5.2.3)
But what about the conditional expectation, E [˜y|˜x = x]? This is not equal to
α + βx, as one might expect, unless E [˜ϵ|˜x = x] = 0. This requires statistical
independence rather than the assumed lack of correlation. Again, a sufficient
condition is multivariate normality.
The notion of the β of ˜y with respect to ˜x as given in (5.2.2) will recur frequently.
The final concept required from basic probability theory is the notion of a mixture
of random variables. For lotteries which are discrete random variables, with pay-
offs x1, x2, x3, . . . occuring with probabilities π1, π2, π3, . . . respectively, we will
use the notation:
π1x1 ⊕π2x2 ⊕π3x3 ⊕. . .
Similar notation will be used for compound lotteries (mixtures of random vari-
ables) where the payoffs themselves are further lotteries.
This might be a good place to talk about the MVN distribution and Stein’s lemma.
Revised: December 2, 1998


## Finance and Asset Pricing

88
5.3. TAYLOR’S THEOREM: STOCHASTIC VERSION
5.3
Taylor’s Theorem: Stochastic Version
We will frequently use the univariate Taylor expansion as applied to a function
of a random variable expanded about the mean of the random variable.1 Taking
expectations on both sides of the Taylor expansion:
f(˜x)
=
f(E[˜x]) +
∞
X
n=1
1
n!f (n)(E[˜x])(˜x −E[˜x])n
(5.3.1)
yields:
E[f(˜x)]
=
f(E[˜x]) +
∞
X
n=2
1
n!f (n)(E[˜x])mn(˜x),
(5.3.2)
where
mn(˜x) ≡E [(˜x −E[˜x])n] .
(5.3.3)
In particular,
m1(˜x)
=
E
h
(˜x −E[˜x])1i
≡0
(5.3.4)
m2(˜x)
=
E
h
(˜x −E[˜x])2i
≡Var [˜x]
(5.3.5)
m3(˜x)
=
E
h
(˜x −E[˜x])3i
≡Skew [˜x]
(5.3.6)
and
m4(˜x)
=
E
h
(˜x −E[˜x])4i
≡Kurt [˜x] ,
(5.3.7)
which allows us to start the summation in (5.3.2) at n = 2 rather than n = 1.
Indeed, we can rewrite (5.3.2) as
E[f(˜x)]
=
f(E[˜x]) + 1
2f ′′(E[˜x])Var [˜x] + 1
6f ′′′(E[˜x])Skew [˜x]
+ 1
24f ′′′′(E[˜x])Kurt [˜x] +
∞
X
n=5
1
n!f (n)(E[˜x])mn(˜x).
(5.3.8)
5.4
Pricing State-Contingent Claims
This part of the course draws on ?, ? and ?.
The analysis of choice under uncertaintly will begin by reinterpreting the general
equilibrium model of Chapter 4 so that goods can be differentiated by the state
of nature in which they are consumed. Specifically, it will be assumed that the
1This section will eventually have to talk separately about kth order and infinite order Taylor
expansions.
Revised: December 2, 1998

CHAPTER 5. CHOICE UNDER UNCERTAINTY
89
underlying sample space comprises a finite number of states of nature. A more
thorough analysis of choice under uncertainty, allowing for infinite and continuous
sample spaces and based on additional axioms of choice, follows in Section 5.5.
Consider a world with M possible states of nature (distinguished by a first sub-
script), markets for N securities (distinguished by a second subscript) and H con-
sumers (distinguished by a superscript).2
Definition 5.4.1 A state contingent claim or Arrow-Debreu security is a random
variable or lottery which takes the value 1 in one particular state of nature and
the value 0 in all other states.
Definition 5.4.2 A complex security is a random variable or lottery which can
take on arbitrary values. The payoffs of a typical complex security will be repre-
sented by a column vector, yj ∈ℜM, where yij is the payoff in state i of security
j.
The set of all complex securities on a given finite sample space is an M-dimensional
vector space and the M possible Arrow-Debreu securities constitute the standard
basis for this vector space.
State contingent claims prices are determined by the market clearing equations in
a general equilibrium model:
Aggregate consumption in state i = Aggregate endowment in state i.
Each individual will have an optimal consumption choice depending on endow-
ments and preferences and conditional on the state of the world. Optimal future
consumption is denoted
x∗=





x∗
1
x∗
2
. . .
x∗
N




.
(5.4.1)
If there are N complex securities, then the investor must find a portfolio w =
(w1, . . . , wN) whose payoffs satisfy
x∗
i =
N
X
j=1
yijwj.
Let Y be the M × N matrix3 whose jth column contains the payoffs of the jth
complex security in each of the M states of nature, i.e.
Y ≡(y1, y2, . . . yN) .
(5.4.2)
2Check for consistency in subscripting etc in what follows.
3Or maybe I mean its transpose.
Revised: December 2, 1998

90
5.4. PRICING STATE-CONTINGENT CLAIMS
Theorem 5.4.1 If there are M complex securities (M = N) and the payoff matrix
Y is non-singular, then markets are complete.
Proof Suppose the optimal trade for consumer i state j is xij −eij. Then can
invert Y to work out optimal trades in terms of complex securities.
Q.E.D.
An (N + 1)st security would be redundant.
Either a singular square matrix or < N complex securities would lead to incom-
plete markets.
So far, we have made no assumptions about the form of the utility function, written
purely as
u (x0, x1, x2, . . . , xN) ,
where x0 represents the quantity consumed at date 0 and xi (i > 0) represents the
quantity consumed at date 1 if state i materialises.
5.4.1
Completion of markets using options
Assume that there exists a state index portfolio, Y , yielding different non-zero
payoffs in each state (i.e. a portfolio with a different payout in each state of nature,
possibly one mimicking aggregate consumption). WLOG we can rank the states
so that Yi < Yj if i < j.
We now present some results, following ?, showing conditions under which trad-
ing in a state index portfolio and in options on the state index portfolio can lead to
the Pareto optimal complete markets equilibrium allocation. Now consider com-
pletion of markets using options on aggregate consumption.
In real-world markets, the number of linearly independent corporate securities is
probably less than M.
However, options on corporate securities may be sufficient to form complete mar-
kets, and thereby ensure allocational (Pareto) efficiency for arbitrary preferences.
Further assume that ∃M −1 European call options on Y with exercise prices
Y1, Y2, . . . , YM−1.
A European call option with exercise price K is an option to buy a security for
K on a fixed date.
An American call option is an option to buy on or before the fixed date.
A put option is an option to sell.
Revised: December 2, 1998

CHAPTER 5. CHOICE UNDER UNCERTAINTY
91
Here, the original state index portfolio and the M −1 European call options yield
the payoff matrix:







y1
y2
y3
. . .
yM
0
y2 −y1
y3 −y1
. . .
yM −y1
0
0
y3 −y2
. . .
yM −y2
...
...
...
...
...
0
0
0
. . .
yM −yM−1







=







security Y
call option 1
call option 2
...
call option M −1







(5.4.3)
and as this matrix is non-singular, we have constructed a complete market.
Instead of assuming a state index portfolio exists, we can assume identical proba-
bility beliefs and state-independent utility and complete markets in a similar man-
ner (see below).
5.4.2
Restrictions on security values implied by allocational ef-
ficiency and covariance with aggregate consumption
Let
 Cω =
aggregate consumption in state ω
Ωk =
{ω ∈Ω: Cω = k}
Let φ(k) be the value of the claim with payoffs
ykω =
 1
if Cω = k
0
otherwise
(5.4.4)
and let the agreed probability of the event Ωk (i.e. of aggregate consumption
taking the value k) be:
π(k) =
X
ω∈Ωk
πω
(5.4.5)
By time-additivity and state-independence of the utility function:
φω = πωu′
i(ciω)
u′
i0(ci0)
∀ω ∈Ω
(5.4.6)
The no arbitrage condition implies
φ(k)
=
X
ω∈Ωk
φω
(5.4.7)
=
u′
i(fi(k))
u′
i0(ci0)
X
ω∈Ωk
πω
(5.4.8)
=
u′
i(fi(k))
u′
i0(ci0) π(k)
(5.4.9)
where fi(k) denotes the i-th individual’s equilibrium consumption in those states
where aggregate consumption equals k.
Revised: December 2, 1998

92
5.4. PRICING STATE-CONTINGENT CLAIMS
x(0)
x(1)
x(2)
˜C = 1
1
0
0
˜C = 2
2
1
0
˜C = 3
3
2
1
·
·
·
·
·
·
·
·
·
·
·
·
˜C = L
L
L −1
L −2
Table 5.1: Payoffs for Call Options on the Aggregate Consumption
State-independence of the utility function is required for fi(k) to be well-defined.
Therefore, an arbitrary security x has value:
Sx
=
X
ω∈Ω
φωxω
(5.4.10)
=
X
k
X
ω∈Ωk
φωxω
(5.4.11)
=
X
k
u′
i(fi(k))
u′
i0(ci0)
X
ω∈Ωk
πωxω
(5.4.12)
=
X
k
φ(k)
X
ω∈Ωk
πω
π(k)xω
(5.4.13)
=
X
k
φ(k)E[˜x| ˜C = k]
(5.4.14)
5.4.3
Completing markets with options on aggregate consump-
tion
Let x(k) be the vector of payoffs in the various possible states on a European call
option on aggregate consumption with one period to maturity and exercise price
k.
Let {1, 2, . . . , L} be the set of possible values of aggregate consumption C(ω).
Then payoffs are as given in Table 5.1.
This all assumes
1. identical probability beliefs
2. time-additivity of u
3. state-independent u
Revised: December 2, 1998

CHAPTER 5. CHOICE UNDER UNCERTAINTY
93
5.4.4
Replicating elementary claims with a butterfly spread
Elementary claims against aggregate consumption can be constructed as follows,
for example, for state 1, using a butterfly spread:
[x(0) −x(1)] −[x(1) −x(2)]
(5.4.15)
yields the payoff:










1
2
3...
L








−








0
1
2...
L −1










−










0
1
2...
L −1








−








0
0
1...
L −2










=








1
1
1...
1








−








0
1
1...
1








=








1
0
0...
0








(5.4.16)
i.e. this replicating portfolio pays 1 iff aggregate consumption is 1, and 0 other-
wise.
The prices of this, and the other elementary claims, must, by no arbitrage, equal
the prices of the corresponding replicating portfolios.
5.5
The Expected Utility Paradigm
5.5.1
Further axioms
The objects of choice with which we are concerned in a world with uncertainty
could still be called consumption plans, but we will acknowledge the additional
structure now described by terming them lotteries.
If there are k physical commodities, a consumption plan must specify a k-dimensional
vector, x ∈ℜk, for each time and state of the world.
We assume a finite number of times, denoted by the set T.
The possible states of the world are denoted by the set Ω.
So a consumption plan or lottery is just a collection of |T| k-dimensional random
vectors, i.e. a stochastic process.
Again to distinguish the certainty and uncertainty cases, we let L denote the col-
lection of lotteries under consideration; X will now denote the set of possible
values of the lotteries in L.
Revised: December 2, 1998

94
5.5. THE EXPECTED UTILITY PARADIGM
Preferences are now described by a relation on L. We will continue to assume that
preference relations are complete, reflexive, transitive, and continuous.
X can be identified with a subset of L, in that each sure thing in X can be identified
with the trivial lottery that pays off that sure thing with probability (w.p.) 1.
Although we have moved from a finite-dimensional to an infinite-dimensional
problem by explicitly allowing a continuum of states of nature, it can be shown
that the earlier theory of choice under certainty carries through to choice under
uncertainty, in particular a preference relation can always be represented by a
continuous utility function on L.
However, we would like utility functions to have a stronger property than conti-
nuity, namely the expected utility property.
Axiom 8 (Substitution or Independence Axiom) If a ∈(0, 1] and ˜p ≻˜q, then
a˜p ⊕(1 −a) ˜r ≻a˜q ⊕(1 −a) ˜r ∀˜r ∈L.
Axiom 9 (Archimedian Axiom) If ˜p ≻˜q ≻˜r then
∃a, b ∈(0, 1) s.t. a˜p ⊕(1 −a) ˜r ≻˜q ≻b˜p ⊕(1 −b) ˜r.
(The Archimedian axiom is just a generalisation of the continuity axiom.)
Axiom 10 (Sure Thing Principle) If probability is concentrated on a set of sure
things which are preferred to q, then the associated consumption plan is also
preferred to q.
(The Sure Thing Principle is just a generalisation of the Substitution Axiom.)
Now let us consider the Allais paradox.
Suppose
1£1m. ≻0.1£5m. ⊕0.89£1m. ⊕0.01£0.
Then, unless the substitution axiom is contradicted:
1£1m. ≻10
11£5m. ⊕1
11£0.
Finally, by the substitution axiom again,
0.11£1m. ⊕0.89£0 ≻0.1£5m. ⊕0.9£0.
If these appears counterintuitive, then so does the independence axiom above.
One justification for persisting with the independence axiom is provided by ?.
Revised: December 2, 1998

CHAPTER 5. CHOICE UNDER UNCERTAINTY
95
5.5.2
Existence of expected utility functions
A function u: ℜk×|T| →ℜcan be thought of as a utility function on sure things.
Definition 5.5.1 Let V : L →ℜbe a utility function representing the preference
relation ⪰.
Then ⪰is said to have an expected utility representation if there exists a utility
function on sure things, u, such that
V ({˜xt})
=
E [u ({˜xt})]
=
Z
. . .
Z
u ({xt}) dF{˜xt} ({xt})
Such a representation will often be called a Von Neumann-Morgenstern (or VNM)
utility function, after its originators (?), or just an expected utility function.
Any strictly increasing transformation of a VNM utility function represents the
same preferences.
However, only increasing affine transformations:
f (x) = a + bx (b > 0)
retain the expected utility property.
Proof of this is left as an exercise.
We will now consider necessary and sufficient conditions on preference relations
for an expected utility representation to exist.
Theorem 5.5.1 If X contains only a finite number of possible values, then the
substitution and Archimidean axioms are necessary and sufficient for a preference
relation to have an expected utility representation.
Proof We will just sketch the proof that the axioms imply the existence of an
expected utility representation; the proof of the converse is left as an exercise.
For full details, see ?.
Since X is finite, and unless the consumer is indifferent among all possible choices,
there must exist maximal and minimal sure things, say p+ and p−respectively.
By the substitution axiom, and a simple inductive argument, these are maximal
and minimal in L as well as in X. (If X is not finite, then an inductive argument
can no longer be used and the Sure Thing Principle is required.)
From the Archimedean axiom, it can be deduced that for every other lottery, ˜p,
there exists a unique V (˜p) such that
˜p ∼V (˜p) p+ ⊕(1 −V (˜p)) p−.
Revised: December 2, 1998

96
5.5. THE EXPECTED UTILITY PARADIGM
It is easily seen that V represents ⪰.
Linearity can be shown as follows:
We leave it as an exercise to deduce from the axioms that if ˜x ∼˜y and ˜z ∼˜t then
π˜x ⊕(1 −π) ˜z ∼π˜y ⊕(1 −π) ˜t.
Define ˜z ≡π˜x ⊕(1 −π) ˜y.
Then, using the definitions of V (˜x) and V (˜y),
˜z
∼
π˜x ⊕(1 −π) ˜y
∼
π

V (˜x) p+ ⊕(1 −V (˜x)) p−

⊕(1 −π)

V (˜y) p+ ⊕(1 −V (˜y)) p−

=
(πV (˜x) + (1 −π) V (˜y)) p+ ⊕(π (1 −V (˜x)) + (1 −π) (1 −V (˜y))) p−
It follows that
V (π˜x ⊕(1 −π) ˜y) = πV (˜x) + (1 −π) V (˜y) .
This shows linearity for compound lotteries with only two possible outcomes: by
an inductive argument, every lottery can be reduced recursively to a two-outcome
lottery when there are only a finite number of possible outcomes altogether.Q.E.D.
Theorem 5.5.2 For more general L, to these conditions must be added some tech-
nical conditions and the Sure Thing Principle.
Proof We will not consider the proof of this more general theorem. It can be
found in ?.
Q.E.D.
Note that expected utility depends only on the distribution function of the con-
sumption plan.
Two consumption plans having very different consumption patterns across states
of nature but the same probability distribution give the same utility. E.g. if wet
days and dry days are equally likely, then an expected utility maximiser is indiffer-
ent between any consumption plan and the plan formed by switching consumption
between wet and dry days.
The basic objects of choice under expected utility are not consumption plans but
classes of consumption plans with the same cumulative distribution function.
Chapter 6 will consider the problem of portfolio choice in considerable depth.
This chapter, however, must continue with some basic analysis of the choice be-
tween one riskfree and one risky asset, following ?.
Such an example is sufficient to show several things:
1. There is no guarantee that the portfolio choice problem has any finite or
unique solution unless the expected utility function is concave.
2. probably local risk neutrality and stuff like that too.
Revised: December 2, 1998

CHAPTER 5. CHOICE UNDER UNCERTAINTY
97
5.6
Jensen’s Inequality and Siegel’s Paradox
Theorem 5.6.1 (Jensen’s Inequality) The expected value of a (strictly) concave
function of a random variable is (strictly) less than the same concave function of
the expected value of the random variable.
E
h
u
 ˜W
i
≤u

E
h ˜W
i
when u is concave
Similarly, the expected value of a (strictly) convex function of a random variable
is (strictly) greater than the same convex function of the expected value of the
random variable.
Proof There are three ways of motivating this result, but only one provides a fully
general and rigorous proof. Without loss of generality, consider the concave case.
1. One can reinterpret the defining inequality (3.2.1) in terms of a discrete
random vector ˜x taking on the value x with probability π and x′ with prob-
ability 1 −π:
∀x ̸= x′ ∈X, π ∈(0, 1)
f (πx + (1 −π)x′) ≥πf(x) + (1 −π)f(x′),
(5.6.1)
which just says that
f (E [˜x]) ≥E [f (˜x)] .
(5.6.2)
An inductive argument can be used to extend the result to all discrete r.v.s
with a finite number of possible values, but runs into problems if the number
of possible values is either countably or uncountably infinite.
2. Using a similar approach to that used with the Taylor series expansion in
(5.3.2), take expectations on both sides of the first order condition for con-
cavity (3.2.3) given by Theorem 3.2.3, where the two vectors considered are
the mean E [˜x] and a generic value ˜x:
f(˜x) ≤f (E [˜x]) + f ′ (E [˜x]) (˜x −E [˜x]) .
(5.6.3)
Taking expectations on both sides, the first order term will again disappear,
once more yielding:
f (E [˜x]) ≥E [f (˜x)] .
(5.6.4)
3. One can also appeal to the second order condition for concavity, and the
second order Taylor series expansion of f around E [˜x]:
E[f(˜x)]
=
f(E[˜x]) + 1
2f ′′(x∗)Var [˜x] ,
(5.6.5)
Revised: December 2, 1998

98
5.6. JENSEN’S INEQUALITY AND SIEGEL’S PARADOX
for some x∗in the support of ˜x. However, this supposes that x∗is fixed,
whereas in fact it varies with the value taken on by ˜x, and is itself a random
variable, correlated with ˜x.
Accepting this (wrong) approximation, if f is concave, then by Theorem 3.2.4
the second derivative is non-positive and the variance is non-negative, so
E[f(˜x)]
≤
f(E[˜x]).
(5.6.6)
The arguments for convex functions, strictly concave functions and strictly con-
cave functions are almost identical.
Q.E.D.
This result is often useful with functions such as x 7→ln x and x 7→1
x.
To get a feel for the extent to which E[f(˜x)] differs from f(E[˜x]), we can again
use the following (wrong) second order Taylor approximation based on (5.3.8):
E[f(˜x)] ≈f(E[˜x]) + 1
2f ′′(E[˜x])Var [˜x] .
(5.6.7)
This shows that the difference is larger the larger is the curvature of f (as measured
by the second derivative at the mean of ˜x) and the larger is the variance of ˜x.
One area in which this idea can be applied is the computation of present values
based on replacing uncertain future discount factors with point estimates derived
from expected future interest rates.
Another nice application of Jensen’s Inequality in finance is:
Theorem 5.6.2 (Siegel’s Paradox) Current forward (relative) prices can not all
equal expected future spot prices.
Proof Let Ft be the current forward price and ˜St+1 the unknown future spot price.
If
Et
h ˜St+1
i
= Ft,
then Jensen’s Inequality tells us that
1
˜Ft
=
1
Et
h ˜St+1
i < Et
" 1
˜St+1
#
,
except in the degenerate case where ˜St+1 is known with certainty at time t.
But since the reciprocals of relatives prices are also relative prices, we have shown
that our initial hypothesis is untenable in terms of a different numeraire.
Revised: December 2, 1998

CHAPTER 5. CHOICE UNDER UNCERTAINTY
99
Q.E.D.
The original and most obvious application of Siegel’s paradox is in the case of
currency exchange rates. In that case,
n ˜Ft
o
and
n ˜St
o
are stochastic processes
representing forward and spot exhange rates respectively. It seems reasonable to
assume that forward exchange rates are good predictors of spot exchange rates in
the future, say:
˜Ft = Et
h ˜St+1
i
.
But this is an internally inconsistent hypothesis.
However, Siegel’s paradox applies equally well to any theory which uses current
prices as a predictor of future values. Another such theory which is enormously
popular is the Efficient Markets Hypothesis of ?. In its general form, this says
that current prices should fully reflect all available information about (expected)
future values. Attempts to make the words fully reflect in any way mathematically
rigorous quickly run into problems.
5.7
Risk Aversion
An individual is risk averse if he or she is unwilling to accept, or indifferent to,
any actuarially fair gamble.
(An individual is strictly risk averse if he or she is unwilling to accept any actu-
arially fair gamble.)
Figure 1.17.1 goes here.
i.e. ∀W0 and ∀p, h1, h2 such that ph1 + (1 −p) h2 = 0
W0 ⪰(≻)W0 + ph1 + (1 −p) h2
i.e.
u (W0) ≥(>)pu (W0 + h1) + (1 −p) u (W0 + h2)
The following interpretation of the above definition of risk aversion is based on
Jensen’s Inequality (see Section 5.6).
In other words, a (strictly) risk averse individual is one whose VNM utility func-
tion is (strictly) concave.
Similarly, a (strictly) risk loving individual is one whose VNM utility function is
(strictly) convex.
Finally, a risk neutral individual is one whose VNM utility function is affine.
Revised: December 2, 1998

100
5.7. RISK AVERSION
Most functions do not fall into any of these categories, and represent behaviour
which is locally risk averse at some wealth levels and locally risk loving at other
wealth levels.
However, in most of what follows we will find it convenient to assume that indi-
viduals are globally risk averse.
Individuals who are globally risk averse will never gamble, in the sense that they
will never have a bet unless they believe that the expected return on the bet is
positive. Thus assuming global risk aversion (and rational expectations) rules out
the existence of lotteries (except with large rollovers) and most other forms of
betting and gaming.
We can distinguish between local and global risk aversion. An individual is locally
risk averse at w if u′′(w) < 0 and globally risk averse if u′′(w) < 0 ∀w.
Individuals who gamble are not globally risk averse but may still be locally risk
averse around their current wealth level.
Cut and paste relevant quotes from Purfield-Waldron papers in here.
Some people are more risk averse than others; some functions are more concave
than others; how do we measure this?
The importance and usefulness of the Arrow-Pratt measures of risk aversion which
we now define will become clearer as we proceed, in particular from the analysis
of the portfolio choice problem:
Definition 5.7.1 (The Arrow-Pratt coefficient of) absolute risk aversion is:
RA(w) = −u′′(w)/u′(w)
which is the same for u and au + b.
Note that this varies with the level of wealth.
u′ (w) alone is meaningless, as u and u′ can be multiplied by any positive constant
and still represent the same preferences. However, the above ratio is independent
of the expected utility function chosen to represent the preferences.
Definition 5.7.2 (The Arrow-Pratt coefficient of) relative risk aversion is:
RR(w) = wRA(w)
The utility function u exhibits increasing (constant, decreasing) absolute risk
aversion (IARA, CARA, DARA) ⇐⇒
R′
A (w) > (=, <) 0 ∀w.
The utility function u exhibits increasing (constant, decreasing) relative risk aver-
sion (IRRA, CRRA, DRRA) ⇐⇒
Revised: December 2, 1998

CHAPTER 5. CHOICE UNDER UNCERTAINTY
101
R′
R (w) > (=, <) 0 ∀w.
Note:
• CARA or IARA ⇒IRRA
• CRRA or DRRA ⇒DARA
Here are some examples of utility functions and their risk measures:
• Quadratic utility (IARA, IRRA):
u(w)
=
w −b
2w2,
b > 0;
u′(w)
=
1 −bw;
u′′(w)
=
−b < 0
RA(w)
=
b
1 −bw
dRA(w)
dw
=
b2
(1 −bw)2 > 0
In this case, marginal utility is positive and utility increasing if and only if
w < 1/b. 1/b is called the bliss point of the quadratic utility function. For
realism, 1/b should be rather large and thus b rather small.
• Negative exponential utility (CARA, IRRA):
u(w)
=
−e−bw,
b > 0;
u′(w)
=
be−bw > 0;
u′′(w)
=
−b2e−bw < 0
RA(w)
=
b
dRA(w)
dw
=
0
• Narrow power utility (CRRA, DARA):
u(w)
=
B
B −1w1−1
B , w > 0, B > 0, B ̸= 1
Revised: December 2, 1998

102
5.8. THE MEAN-VARIANCE PARADIGM
The proofs in this case are left as an exercise. The solution is roughly as
follows:4
u(z)
=
B
B −1z1−1
B , z > 0, B > 0
u′(z)
=
z−1
B
u′′(z)
=
−1
Bz−1
B −1
RA(z)
=
1
Bz−1
RR(z)
=
1
B
dRA(z)
dz
=
−1
Bz−2 < 0
dRR(z)
dz
=
0
• Extended power utility ():5
u (w) =
1
(C + 1) B (A + Bw)C+1
Note that a risk neutral investor will seek to invest his or her entire wealth in the
asset with the highest expected return. If all investors are risk neutral, then prices
will adjust in equilibrium so that all securities have the same expected return. If
there are risk averse or risk loving investors, then there is no reason for this result
to hold, and in fact it almost certainly will not.
5.8
The Mean-Variance Paradigm
Three arguments are commonly used to motivate the mean-variance framework
for analysis of the portfolio choice problem:
1. Taylor-approximated utility functions (see Section 2.8):
u( ˜W)
=
u(E[ ˜W]) + u′(E[ ˜W])( ˜W −E[ ˜W])
+
1
2u′′(E[ ˜W])( ˜W −E[ ˜W])2 + R3
(5.8.1)
R3
=
∞
X
n=3
1
n!u(n)(E[ ˜W])( ˜W −E[ ˜W])n
(5.8.2)
4Add comments: u′(w) > 0, u′′(w) < 0 and u′(w) →1/w as B →1, so that u(w) →ln w.
5Check ? for details of this one.
Revised: December 2, 1998

