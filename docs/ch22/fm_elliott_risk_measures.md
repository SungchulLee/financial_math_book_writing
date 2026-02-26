# Consumption-Investment & Risk Measures

!!! info "Source"
    **Mathematics of Financial Markets** by Robert J. Elliott and P. Ekkehard Kopp, Springer, 2nd ed., 2005.
    These notes are used for educational purposes.

## Consumption-Investment Strategies

292
CHAPTER 10. CONSUMPTION-INVESTMENT STRATEGIES
Write SFB(x) for the set of such strategies. Following Definition 10.2.3,
we have seen that (H1, c1) ∈SF(0, x) implies c1 ∈C(x). Therefore,
Eθ
 T
0
βsc1(s)ds

≤x.
In this situation, utility is coming only from consumption, so it is easily
seen that one should increase consumption up to the limit imposed by the
bound. Consequently, we should consider only consumption rate processes
for which
Eθ
 T
0
βsc1(s)ds

= E
 T
0
Λsβsc1(s)ds

= x.
That is, we consider c1 ∈D(x). In other words, if we define the value
function
V1(x) =
sup
(H1,c1)∈SFB(x)
J1(x, H1, c1),
then
V1(x) =
sup
(H1,c1)∈SFB(x)
c1∈D(x)
J1(x, H1, c1).
(10.9)
For this constrained maximisation problem, we consider the Lagrangian
Γ(c1, y) = E
 T
0
U1(c1(s))ds

−y

E
 T
0
Λsβsc1(s)ds

−x

.
The first-order conditions imply that the optimal consumption rate c∗
1(s)
should satisfy
U ′
1 (c∗
1(s)) = yΛsβs,
E
 T
0
Λsβsc∗
1(s)ds

= x.
(10.10)
Therefore, with I1 the inverse function of the strictly decreasing map U ′
1,
c∗
1(s) = I1(s, yΛsβs),
and y is determined by the condition (10.10). In fact, write
L1(y) = E
 T
0
ΛsβsI1(s, yΛsβs)ds

for 0 < y < ∞.
Assume that L1(y) < ∞for 0 < y < ∞. Then, from the corresponding
properties of I1, L1 is continuous and strictly decreasing, with
L1(0+) = ∞,
L1(∞) = 0.

10.3. MAXIMISING UTILITY OF CONSUMPTION
293
Consequently, there is an inverse map for L1, which we denote by G1, so
that
L1(G1(y)) = y.
That is, for any x > 0, there is a unique y such that
y = G1(x).
Differentiating, we also see that L′
1(G1(y))G′
1(y) = 1. The corresponding
optimal consumption process is therefore
c∗
1(s) = I (s, G1(x)Λsβs) for 0 ≤t ≤T.
(10.11)
By construction, c∗
1 ∈D(x). From Theorem 10.2.4, there is a unique port-
folio process H∗
1 (up to equivalence) such that (H∗
1, c∗
1) ∈SF(0, x). The
corresponding wealth process is then X1, where
βtX1(t) = Eθ
 T
t
βsc∗(s)ds |Ft

= x −
 t
0
βsc∗(s)ds +
 t
0
βsH∗(s)′σ(s)dW θ(s).
Note that X1(t) > 0 on [0, T) and X1(T) = 0 a.s.
Theorem 10.3.1. Assume L1(y) < ∞for 0 < y < ∞. Then, for any
x > 0, with c∗
1 given by (10.11), the pair (H∗
1, c∗
1) belongs to SFB(x) and is
optimal for the problem (10.9). That is,
V1(x) = J1(x, H∗
1, c∗
1).
Proof. Consider any other c ∈C(x). From the concavity of U1, inequal-
ity (10.4) implies that
U1 (t, c∗
1(t)) ≥U1(t, ct) + G1(x)Λtβt (I(t, G1(x)Λtβt) −ct) .
(10.12)
Write ,ct = x

E
4 T
0 Λuβudu
−1
. Then ,c is a constant rate of con-
sumption and
Eθ
 T
0
βu,cudu

= E

ΛT
 T
0
βu,cudu

= x,
so that ,c ∈D(x). Also, substituting ,c in the right-hand side of (10.12) and
integrating, we obtain
E
 T
0
U1 (t, ,ct) dt

+ G1(x) (L1(G1(x)) −x) = E
 T
0
U1 (t, ,ct) dt

.

294
CHAPTER 10. CONSUMPTION-INVESTMENT STRATEGIES
Thus, integrating both sides of (10.12) yields E
4 T
0 U −
1 (c∗(s)) ds

< ∞.
Finally, consider c ∈C(x). Integrating both sides of (10.12), we have
E
 T
0
U1 (t, c∗
1(t)) dt

≥
E
 T
0
U1(t, ct)dt

+ G1(x)

x −E
 T
0
Λtβtctdt

.
The final bracket equals
E

ΛT
 T
0
βtctdt

= Eθ
 T
0
βtctdt

and so is non-negative. Therefore, c∗
1 is optimal.
Remark 10.3.2. From the optimality conditions we have seen that the op-
timal consumption rate c∗
1(t) is of the form
c∗
1(t) = I1 (t, yξt) for some y > 0.
Here ξt = βtΛt is the market deflator of Definition 10.2.1. Let us consider
the expected utility function associated with a consumption rate process
of this form:
K1(y) = E
 T
0
U1 (t, I1(t, yξt)) dt

for 0 < y < ∞.
(10.13)
We require
E
 T
0
|U1 (t, I(t, yξt))| dt

< ∞for all y ∈(0, ∞).
(10.14)
Then K1 is continuous and strictly decreasing in y. We have proved in
Theorem 10.3.1 that
V1(x) = K1 (G1(x)) .
Under the assumption, for example, that U1(t, y) is C2 in y > 0 and
∂2U1(t,y)
∂y2
is non-decreasing in y for all t ∈[0, T], we can perform the differ-
entiations of L1(y) and K1(y) to obtain
L′
1(y) = E
 T
0
ξ2
t
∂
∂z I1 (t, yξt) dt

.
Recalling that
∂U1
∂z (t, I1(t, z)) = z ∂
∂z I1(t, z),

10.3. MAXIMISING UTILITY OF CONSUMPTION
295
we have, with z = yξt, that
K′
1(y) = E
 T
0
ξt
∂U1
∂z (t, I1(t, yξt)) dt

= E
 T
0
yξ2
t
∂
∂z I1 (t, yξt) dt

= yL′
1(y).
We can therefore state the following result.
Theorem 10.3.3. Under the integrability conditions that L1(y) < ∞
and (10.4) holds, the value function is given by
V1(x) = K1 (G1(x)) .
(10.15)
Also, if the utility function U1(t, y) is C2 in y and
∂2U
∂y2 (t, y) is non-
decreasing in y, then the strictly decreasing functions L1 and K1 are con-
tinuously differentiable and
K′
1(y) = yL′
1(y).
Furthermore, from (10.15),
V ′
1(x) = K′
1 (G1(x)) G′
1(x) = G1(x)L′
1 (G1(x)) G′
1(x) = G1(x).
In addition, note that V1 is strictly increasing and concave.
Example 10.3.4. Suppose U1(t, c) = exp

−
4 t
0 ρ(u)du

log c, where ρ :
[0, T] →R is measurable and bounded. Then
U ′
1(t, c) = exp
$
−
 t
0
ρ(u)du
%
c−1,
I1(t, c) = exp
$
−
 t
0
ρ(u)du
%
c−1,
L1(y) = a1
y ,
K1(y) = −a1 log y + b1,
so
V1(x) = a1 log
 x
a1

+ b1,
where
a1 =
 T
0
exp
$
−
 t
0
ρ(u)du
%
dt
and
b1 = E
 T
0
exp
$
−
 t
0
ρ(u)du
%  t
0

ru + 1
2 |θu|2 −ρ(u)

du

dt

.

296
CHAPTER 10. CONSUMPTION-INVESTMENT STRATEGIES
Example 10.3.5. Suppose U1(t, c) = −exp

−
4 t
0 ρ(u)du

c−1. Then
L1(y) = d1y−1
2 ,
G1(y) = −d1y
1
2 ,
so
V1(x) = −d2
1
x ,
where
d1 = E
 T
0
exp
$
−1
2
 t
0
(ρ(u) + ru)du
%
Λ
1
2
t dt

.
Note that conditions L1(y) < ∞and (10.14) are both satisfied in these
examples.
10.4
Maximisation of Terminal Utility
The previous section discussed maximisation of consumption. This section
considers the dual problem of maximization of terminal wealth. That is,
for any (H2, c2) ∈SF(0, x), we consider
J2(x, H2, c2) = E (U2 (XT ))
for a utility function U2.
We restrict ourselves to the subset SFC(0, x) consisting of those (H, c)
such that
E

U −
2 (XT )

< ∞.
Define the value function
V2(x) =
sup
(H2,c2)∈SFC(0,x)
J2(x, H2, c2).
(10.16)
The expected terminal wealth discounted to time 0 should not exceed the
initial investment x; that is,
Eθ (βT XT ) = E (ξtXT ) ≤x.
The methods are similar to those of Theorem 10.3.1, so we sketch the
ideas and proofs. Define
L2(y) = E (ξT I2 (T, yξT )) for y > 0.
We assume L2(y) < ∞for y ∈(0, ∞). Again L2 is continuous and strictly
decreasing with L2(0+) = ∞and L2(∞) = 0.
Write G2 for the inverse function of L2. For an initial capital x2, consider
X2(T) = I2 (T, G2(x2)ξT ) .
(10.17)

10.4. MAXIMISATION OF TERMINAL UTILITY
297
This belongs to the class M(x2) of Theorem 10.2.5 because
Eθ (X2(T)βT ) = E (ξT X2(T)) = E (ξT I2 (T, G2(x2)ξT )) = x2.
Hence, by Theorem 10.3.1, there is a trading strategy (H2, c2) ∈SF(0, x2)
that attains the terminal wealth X2(T). This strategy is unique up to equiv-
alence, and for this pair c2 ≡0. Consequently, the corresponding wealth
process is given by
βtX2(t) = Eθ (βT X2(T) |Ft )
= x2 +
 t
0
βsH′
2(s)σ(s)dW θ(s) for 0 ≤t ≤T.
(10.18)
Using again the inequality (10.4) for utility functions, we can parallel
the proof of Theorem 10.3.1 to show that X2(T), defined by (10.17), satisfies
E

U −
2 (X2(T))

< ∞,
E (U2 (X2(T))) ≥E (U2 (XT )) ,
(10.19)
where XT is any other random variable satisfying (10.19).
Consequently, we have proved the following result.
Theorem 10.4.1. If L2(y) < ∞for all y ∈(0, ∞), consider any x2 > 0
and the random variable
X2(T) = I2 (T, G2(x2)ξT ) .
Then the trading strategy (H2, 0) belongs to SFC(0, x2) and
V2(x2) = E (U2 (T, X2(T))) .
That is, (H2, 0) achieves the maximum in (10.16).
Similarly to Theorem 10.3.3, we can also establish the following.
Theorem 10.4.2. If L2(y) < ∞and if
E (|U2 (I2(T, yξT ))|) < ∞
for all y ∈(0, ∞), then the value function V2 is given by
V2(x) = K2 (G2(x)) ,
where
K2(y) = E (U2 (T, I2(T, yξT ))) .
(10.20)
Note that K2 is continuous and strictly decreasing for 0 < y < ∞.
Also, if U2(t, y) belongs to C2(0, ∞) and ∂2U(t,y)
∂y2
is non-decreasing in
y, then the functions L2, K2 are also in C2(0, ∞) and K′
2(y) = yL′
2(y) for
0 < y < ∞.
Furthermore,
V ′
2 = G2,
implying that V2 is strictly increasing and strictly concave.

298
CHAPTER 10. CONSUMPTION-INVESTMENT STRATEGIES
Example 10.4.3. Again consider the utility function
U(T, c) = exp

−
 T
0
ρ(u)du

log c,
where ρ is bounded, real, and measurable. In this case,
L2(y) = a2
y ,
G2(y) = −a2 log y + d2,
V2(x) = a2 log
 x
a2

+ d2,
with
a2 = exp
 T
0
ρ(u)du
&
and
d2 = E

exp

−
 T
0
ρ(u)du
&  T
0

ru + 1
2 |θu|2 −ρ(u)

du

.
With ρ(u) ≡0, we have
I2(T, y) = L2(y) = y−1.
Consequently, from (10.17),
X2(T) = (G2(x2)ξT )−1 .
In this example, G2(x2) = x−1
2
and
ξT = ΛT βT ,
ΛT = exp

−
 T
0
θudW(u) −1
2
 T
0
|θu|2 du
&
.
Then
βT X2(T) = x2 exp
 T
0
θudW(u) + 1
2
 T
0
|θu|2 du
&
.
Recalling dW(t) = dW θ
t −θtdt, we have
βT X2(T) = x2 exp
 T
0
θudW θ
u −1
2
 T
0
|θu|2 du
&
and, since the right-hand side is the final value of a P θ-martingale, (10.18)
yields
βtX2(t) = Eθ (βT X2(T) |Ft )
= x2 exp
$ t
0
θudW θ
u −1
2
 t
0
|θu|2 du
%

10.5. CONSUMPTION AND TERMINAL WEALTH
299
= x2 +
 t
0
βuX2(u)dW θ
u.
Comparing this with (10.18), we see
H2(t) = X2(t)σ′(t)−1θt.
Example 10.4.4. For the utility function
U2(T, c) = −exp

−
 T
0
ρ(u)du
&
c−1,
we can show that
L2(y) = a2y−1
2 ,
G2(y) = −a2y
1
2 ,
V2(x) = −a2
2
x ,
with
a2 = E

exp

−1
2
 T
0
(ρ(u) + ru) du
&
Λ
1
2
T

.
10.5
Consumption and Terminal Wealth
We consider now an investor who wishes to both live well (consume) and
also acquire terminal wealth at time T > 0. These two objectives conflict,
so we determine the investor’s best policy.
Consider two utility functions U1 and U2. As in Section 10.3, the in-
vestor’s utility from consumption is given by
J1(x, H, c) = E
 T
0
U1 (cu) du

.
The investor’s terminal utility, as in Section 10.4, is
J2(x, H, c) = E (U2(T, Xt)) .
Write SFD(0, x) = SFB(0, x)∩SFC(0, x) for the set of admissible trad-
ing and consumption strategies. Then, with
J(x, H, c) = J1(x, H, c) + J2(x, H, c),
the investor aims to maximise J(x, H, c) over all strategies
(H, c) ∈SFD(0, x).
It turns out that the optimal policy for the investor is to split his initial
endowment x into two parts, x1 and x2, with x1 + x2 = x, and then to
use the optimal consumption strategy (H1, c1) of Section 10.3 with initial

300
CHAPTER 10. CONSUMPTION-INVESTMENT STRATEGIES
investment x1 and the optimal investment strategy (H2, 0) of Section 10.4
with initial investment x2.
Thus, consider an initial endowment x and a pair (H, c) ∈SFD(0, x).
Write
x1 = Eθ
 T
0
βucudu

,
x2 = x −x1.
If Xt is the wealth process for (H, c), then
Xt = β−1
t

x −
 t
0
βucudu +
 t
0
βuH′(u)σ(u)dW θ
u

,
J(x, H, c) = E
 T
0
U1 (s, cs) dt + U2 (T, XT )

.
By definition, c ∈D(x1) and XT ∈L(x2).
Now, from Theorem 10.3.1 there is an optimal strategy (H1, c1) ∈
SFB(0, x1) that attains the value
V1(x1) =
sup
(H,c)∈SFB(0,x1)
J1(x1, H, c).
Also, from Theorem 10.4.1 there is an optimal strategy (H2, 0) ∈SFC(0, x2)
that attains the value
V2(x2) =
sup
(H,c)∈SFC(0,x2)
J2(x2, H, c).
Now suppose X1(t) is the wealth process corresponding to (H1, c1) and
X2(t) is the wealth process corresponding to (H2, 0). Then
X1(t) = β−1
t

x1 −
 t
0
βuc1(u)du +
 t
0
βuH′
1(u)σ(u)dW θ
u

,
with X1(T) = 0 and
X2(t) = β−1
t

x2 +
 t
0
βuH′
2(u)σ(u)dW θ
u

.
Consider, therefore, the wealth process X, which is the sum of X1
and X2 and corresponds to an investment strategy H = H1 + H2 and
consumption process c = c1. Then, with x = x1 + x2,
Xt = X1(t) + X2(t) = β−1
t

x −
 t
0
βucudu +
 t
0
βuHuσ(u)dW θ
u

.
However, for any initial endowment x, any decomposition of x into
x = x1 + x2, and any strategy (H, c) ∈SFD(0, x), we must have, because
of the optimality of V1(x1) and V2(x2), that
J(x, H, c) ≤V1(x1) + V2(x2).

10.5. CONSUMPTION AND TERMINAL WEALTH
301
Consequently,
V (x) =
sup
(H,c)∈SFD(0,x)
J(x, H, c) ≤V ∗(x) =
max
x1+x2=x
x1≥0,x2≥0
[V1(x1) + V2(x2)].
We shall show that the maximum on the right-hand side can be achieved
by an appropriate choice of x1 and x2. For such x1 and x2, there are optimal
strategies (H1, c1) and (H2, 0), so the strategy (H, c) is then optimal for
the combined consumption and investment problem. In fact, the maximum
on the right-hand side is found by considering
γ(x1) = V1(x1) + V2(x −x1).
The critical point of γ arises when γ′(x1) = 0; i.e., when V ′
1(x1) = V ′
2(x −
x1). This means we are looking for the values x1, x2, x1 + x2 = x such that
the marginal expected utilities from the consumption problem and terminal
wealth problem are equal. From Theorems 10.3.3 and 10.4.2, V ′
i = Gi, so
this is when
G1(x1) = G2(x2).
Write z for this common value. The inverse function of Gi is Li, i = 1, 2,
so
x1 = L1(z),
x2 = L2(z).
For any y ∈(0, ∞), consider the function
L(y) = L1(y) + L2(y) = E
 T
0
ξtI1(t, yξt)dt + ξT I2(T, yξT )

.
Here ξ is the ‘deflator’ of Definition 10.2.1.
Then L is continuous, strictly decreasing, and L(0+) = ∞, L(∞) = 0.
Write G for the inverse function of L. Then, for the optimal decomposition,
x = x1 + x2 = L1(z) + L2(z) = L(z),
z = G(x).
Consequently, the optimal decomposition of the initial endowment x is
given by
x1 = L1 (G(x)) , x2 = L2 (G(x)) .
Consider the function
K(y) = K1(y)+K2(y) = E
 T
0
U1 (t, I1(t, yξt)) dt + U2 (T, I2(T, yξT ))

.
K is continuous and decreasing on (0, ∞). From (10.15) and (10.20)
V (x) = V ∗(x) = K (G(x)) .
Summarizing the above discussion we state the following theorem.

302
CHAPTER 10. CONSUMPTION-INVESTMENT STRATEGIES
Theorem 10.5.1. For an initial endowment x > 0, the optimal consump-
tion rate is
c = I1 (t, G(x)ξt) for 0 ≤t ≤T,
and the optimal terminal wealth level is
XT = I2 (T, G(x)ξT ) .
There is an optimal portfolio process H such that (H, c) ∈SFD(0, x),
and the corresponding wealth process X is
Xt = β−1
t
Eθ
 T
t
βuI1 (u, G(x)ξ(u)) du + βT I2 (T, G(x)ξT ) |Ft

for 0 ≤t ≤T. Furthermore, the value function of the problem is given by
V (x) = K (G(x)) .
Example 10.5.2. Suppose U1(t, c) = U2(t, c) = exp

−
4 t
0 ρ(u)du

log c.
Then
L(y) = a
y ,
K(y) = −a log y + b,
V (x) = a log
x
a

+ b for 0 < x < ∞.
Here a = a1 + a2, b = b1 + b2, where a1, b1 (resp., a2, b2) are given in
Example 10.3.4 (resp. Example 10.4.3).
Example 10.5.3. Suppose U1(t, c) = U2(t, c) = −1
c exp

−
4 t
0 ρ(u)du

.
Then
L(y) = ay−1
2 ,
K(y) = −ay−1
2 ,
V (x) = −a2
x ,
where a = a1+a2 with a1 as in Example 10.3.5 and a2 as in Example 10.4.4.
Remark 10.5.4. In the case when the coefficients r, µi, and σ = (σij) in the
dynamics (10.1), (10.2) are constant, more explicit closed form solutions
for the optimal strategies, in terms of feedback strategies as functions of
the current level of wealth, can be obtained.
The solution of the dynamic programming equation can be obtained in
terms of a function that is the value function of a European put option.
Details can be found in [186] through [189].

Chapter 11
Measures of Risk
Trading in assets whose future outcomes are uncertain necessarily involves
risk for the investor. The management of such risk is of fundamental con-
cern for the operation of financial markets. For example:
• Financial regulators seek to minimise the occurrence and impact of
the collapse of financial institutions by placing restrictions on the
types and sizes of permitted trades, such as limits on short sales;
• Risk managers in investment firms place restrictions on the activities
of individual traders, seeking to avoid levels of exposure that the firm
may not be able to meet in extreme circumstances;
• Individual investors seek to diversity their holdings, so as to avoid
undue exposure to sudden moves in particular stocks or sectors of
the market.
The mathematical analysis of measures of risk has also been a principal
concern of the actuarial and insurance professions since their inception.
Equally, it plays a fundamental role in the theory of portfolio selection
(which is not covered in this book - see, for example, [217],[36]).
At its simplest, the standard deviation σK of the return K on a risky
investment provides a measure of the deviation of the values of K from their
mean E (K). We saw in Chapters 1 and 7 that in the binomial and Black-
Scholes pricing models, a European call option C on a stock S satisfies
σC ≥σS for the standard deviations of the return on the option and stock,
respectively, and the same inequality holds for their excess mean returns.
We interpreted this as indicating that the option is inherently riskier than
the stock, although potentially more profitable.
In portfolio selection, the objective is to find a portfolio that maximises
expected return while minimising risk; i.e., given portfolios V1 and V2 with
mean returns µ1, µ2 and standard deviations σ1, σ2, respectively, it is
assumed that investors will prefer V1 to V2 provided that µ1 ≥µ2 and
303

304
CHAPTER 11. MEASURES OF RISK
σ1 ≤σ2. V1 is said to dominate V2 in this event. An efficient portfolio is
one that is not dominated by any other, and the set of these (among all
attainable portfolios) is the efficient frontier. Elementary properties of the
variance show that, in the absence of short sales, when (positive) fractions
of the investor’s wealth are placed in a portfolio comprising two stocks,
the variance of the return on this portfolio will be no greater than the
larger of the variances of the return on the individual stocks. This simple
result is easily generalised to general portfolios and underlies the claim that
‘diversification reduces risk’, which lies at the heart of the Capital Asset
Pricing Model (CAPM) - see [36] for an elementary account. It is reasonable
to expect more sophisticated measures of risk to retain this property, and
this informs many of the more recent developments that seek to provide an
axiomatic basis for measures of risk.
Variance is symmetric, while in risk management one is primarily con-
cerned with containing the downside risk (i.e., to place bounds on the
amount of potential loss, or the amount by which the final position may
fall short of an expected return). This leads to the definition of measures of
risk that focus on the lower tail of the distribution of the random variable
representing the final position. Currently the most widely used measure
of exposure in risk management is Value at Risk, usually abbreviated to
V aR. Value at Risk was developed and adopted in response to the financial
disasters, such as those at Baring’s Bank, Orange County, and Metallge-
sellschaft, of the early 1990s.
We shall give a precise definition of V aR and show that there are pos-
sible problems with this measure of risk. Continuing to work in a single-
period framework, we then introduce the definition of coherent risk measure
proposed by Artzner et al. [9], which leads to possible refinements of V aR.
11.1
Value at Risk
A standard treatment of V aR can be found in the book by Jorion [180].
It is noted that risk management has undergone a revolution since the
mid-1990s, generated largely by the use of V aR. In fact, V aR has become
the standard benchmark for measuring financial risks.
JP Morgan has
developed Risk MetricsTM based on V aR.
In practice, given sufficient data, V aR is easy to apply. The idea is
to determine the level of exposure in a position (portfolio) that we can be
‘reasonably sure’ will not be exceeded. For example, suppose one knows the
monthly returns on US Treasury notes over a certain time period - some
returns will be positive, others negative. A confidence level of (say) 95% is
chosen. One then wishes to determine the loss that will not be exceeded in
95% of the cases, or, put another way, so that only 5% of the returns are
lower than this level.
That level of return can be determined from the data. Suppose, for
example, it is a return of −2.25%. If an investor holds $100 million of such

11.1. VALUE AT RISK
305
Treasury notes, based on previous data he or she can be 95% sure that the
portfolio will not fall by more than 2.25% of its holdings (i.e., by more than
$2.25 million) over the next month.
Clearly, the confidence level of 95% could be changed, as could the time
period of one month.
The idea behind V aR is therefore that some threshold probability level
α (say 5%) is given. If the random variable representing some position,
which may suffer a possible loss, is denoted by X, then there is a smallest
x such that P(X > x) < α. Here x represents an ‘acceptable’ level of loss.
To make this more precise, we first have the following definition.
Definition 11.1.1. Suppose X is a real random variable defined on a
probability space (Ω, F, P) and α ∈[0, 1]. The number q is an α-quantile if
P(X < q) ≤α ≤P(X ≤q).
The largest α-quantile is
qα(X) = inf{x : P(X ≤x) > α}.
(11.1)
The smallest α-quantile is
qα(X) = inf{x : P(X ≤x) ≥α}.
(11.2)
Note that qα ≤qα. Moreover, q is an α-quantile if and only if qα ≤q ≤
qα.
It is helpful to describe qα(X) in terms of the distribution FX(x) =
P(X ≤x) of X. As a function of α, qα(X) is the right-continuous inverse
of FX; i.e.,
qα(X) = inf{x ∈R : FX(x) > α}.
(11.3)
The function q(α) = qα(X) is then increasing and right-continuous in the
variable α on (0, 1) and satisfies the inequalities
FX(q(α)−) ≤α ≤FX(q(α)),
q(FX(x)−) ≤x ≤q(FX(x)),
(11.4)
where g(s+) = limt↓s g(t) and g(s−) = limt↑s g(t) for any real function g.
We also have
FX(x) = inf{α ∈(0, 1) : q(α) > x}.
(11.5)
These results are elementary, and the proofs are left to the reader. (See,
e.g. , [132, Lemma 2.72].)
Note that Figure 11.1 illustrates clearly that qα = qα unless the distribu-
tion function FX has a ‘flat’ piece, and then the set Jα = {x : FX(x) = α}
is a non-trivial left-closed interval with endpoints qα and qα. In that case,
Jα = [qα, qα] if P(X = qα) = 0,
Jα = [qα, qα) if P(X = qα) > 0.

306
CHAPTER 11. MEASURES OF RISK
Figure 11.1
It is easily seen from Figure 11.1 that qα(X) = sup {x : P(X < x) ≤α} .
It follows that for any X
q1−α(−X) = inf {x : P(−X ≤x) ≥1 −α}
= inf {x : 1 −P(X < −x) ≥1 −α}
= inf {x : P(X < −x) ≤α}
= −sup {y : P(X < y) ≤α}
= −qα(X).
(11.6)
We are now ready to define V aR as follows.
Definition 11.1.2. Given a position described by the random variable X
and a number α ∈[0, 1], define
V aRα(X) = −qα(X) = q1−α(−X).
X is then said to be V aRα-acceptable if
qα(X) ≥0 or, equivalently, V aRα(X) ≤0.
The choice of qα instead of qα is somewhat arbitrary, and the discussion
above shows that it only yields different results when the distribution FX
is ‘flat’ at α, so that Jα is a non-trivial interval.
However, this occurs
frequently in practical situations: for example, with discrete probability
distributions. The significance of our choice will become clearer when we
discuss ‘expected shortfall’, which is also known as ‘conditional value at

11.1. VALUE AT RISK
307
risk’ and is prominent among the candidate risk measures proposed in
recent years as potential replacements for V aR.
V aR can be considered as the amount of extra capital a firm needs
to reduce to α the probability of bankruptcy, or the extra capital needing
to be added (as a risk-free investment) to a given position to make an
investing agency’s financial exposure acceptable to an external regulator.
A negative V aR implies that the firm could return some of its capital to
shareholders or that it (or the investing agency) could accept more risk.
Writing m instead of x in the third line of equations (11.6), we can express
this by
V aRα(X) = inf {m ∈R : P(X + m < 0) ≤α} .
(11.7)
This formulation provides an immediate proof of the following result.
Lemma 11.1.3. V aR has the following properties:
(i) if X ≥0, then V aRα(X) ≤0;
(ii) if X ≥Y , then V aRα(X) ≤V aRα(Y );
(iii) if λ ≥0, V aRα(λX) = λV aRα(X);
(iv) V aRα(X + k) = V aRα(X) −k for any real number k.
Note that (iv) implies that
V aRα(X + V aRα(X)) = 0.
(11.8)
Thus we can interpret V aR as the minimum amount that will ensure
that the probability that the absolute loss that could be suffered will be no
more than this amount is at least 1 −α.
Remark 11.1.4. We observe that the properties (ii) and (iv), which are
similar to those considered in an axiomatic context below, already suffice
to make V aR Lipschitz-continuous with respect to the L∞-norm. To see
this, let X and Y be bounded random variables, and note that X = Y +
(X −Y ) ≤Y + ∥X −Y ∥∞a.s. By properties (ii) and (iv), this yields, for
any α, that
V aRα(X) ≥V aRα(Y + ∥X −Y ∥∞) = V aRα(Y ) −∥X −Y ∥∞,
so that
V aRα(Y ) −V aRα(X) ≤∥X −Y ∥∞.
Reversing the roles of X and Y , we also obtain
V aRα(X) −V aRα(Y ) ≤∥Y −X∥∞= ∥X −Y ∥∞.
Therefore
|V aRα(Y ) −V aRα(X)| ≤∥X −Y ∥∞.
(11.9)

308
CHAPTER 11. MEASURES OF RISK
However, a serious problem with V aR is that it is not subadditive, as
the following simple example shows.
Example 11.1.5. Suppose a bank loans $100, 000 to a company that will
default on the loan with probability 0.008 (i.e., 0.8%). We are supposing the
company either defaults on the whole amount or not at all. Writing X for
the default amount, we have that X = −$100, 000 with probability 0.8%,
and otherwise X = $0. Therefore, with α = 0.01 we see that V aRα(X) ≤0.
Suppose now that the bank makes two loans each of $50, 000 to two different
companies, each of which may default with probability 0.8%. Suppose the
probabilities of default are independent. Then, with α = 0.01, the V aRα
for the bank’s diversified position is $50, 000. While the probability of both
companies defaulting remains below α = 0.01, the probability of at least
one default of $50000 is 0.016 > α.
Diversification is usually thought to reduce risk. However in this ex-
ample it increases V aR. Moreover, as the next example, taken from [9],
shows, V aR is also ineffective in recognising the dangers of concentrating
credit risk.
Example 11.1.6. Consider the issue of corporate bonds in a market with
zero base rate, all corporate bond spreads equal to 2%, and default by
any company set at 1%. At a 5% quantile, V aR for a loan of $1, 000, 000
invested in bonds with a single company is −$20, 000; thus this measure
indicates that there is no risk. On the other hand, suppose instead that the
loan is placed in bonds issued independently by 100 companies at $10, 000
each. The probability that two companies will default is
100
2

(.01)2(.99)98,
which is approximately 0.184865, so the probability of at least 2 defaults is
certainly greater than 0.18. Hence a positive V aR results at the 5% level;
i.e., again diversification has increased risk as measured by V aR.
Finally, V aR does not give us any indication of the severity of the
economic consequences of exposure to the rare events that it excludes from
consideration. Consequently, in spite of its widespread use and its adoption
by the Basel committee (see [9]), there are good reasons for rejecting V aR
as an adequate measure of risk.
11.2
Coherent Risk Measures
The examples above show that, although it is widely used in practice as a
management tool, there are problems with V aR: the V aR of a diversified
position can be greater than the V aR of the original position; if a large
loss occurs, V aR does not measure the actual size of the loss; and, because
V aR is a single number, V aR does not indicate which item in a portfolio
is responsible for the largest risk exposure.
In this section, we shall define and discuss coherent measures of risk.
These have been introduced by Artzner et al. [9]. This paper discusses why

11.2. COHERENT RISK MEASURES
309
such measures should have the properties stated in the definition given be-
low. Here we concentrate on their mathematical properties. Our discussion
is largely based on the notes by Delbaen [74] and the paper of Nakano [235].
We work on a probability space (Ω, F, P). Our time parameter t takes
values 0 (now) and 1, which may represent tomorrow or some date next
month or next year. We thus restrict attention to a single-period model,
where Ωrepresents the possible states at time t = 1 of our economic model.
As before, write L∞= L∞(Ω) for the space of essentially bounded real-
valued functions on Ω, and L1 = L1(Ω). We again denote by L1
+ the cone
of non-negative functions in L1. Although risk measures can be defined
more generally on the space L0 of all real-valued random variables on Ω,
we choose to restrict attention to L1, which is large enough for interesting
applications and remains more tractable mathematically.
Definition 11.2.1. A coherent risk measure is a function ρ : L1 →R such
that
(i) if X ≥0, then ρ(X) ≤0;
(ii) if k ∈R, then ρ(X + k) = ρ(X) −k;
(iii) if λ ≥0 in R, then ρ(λX) = λρ(X);
(iv) ρ(X + Y ) ≤ρ(X) + (Y ).
Remark 11.2.2. In [9], the above definition is stated in terms of the actual
final value of the position X at time 1, whereas our definition follows the
more recent literature in assuming that X represents the discounted value of
the position, or, alternatively, sets the discount rate to 0. This simplifies the
formulation without loss of generality: working with a discount rate β and
final position X′, so that X = βX′ is the discounted value, one can express
a risk measure ρ′ in terms of X′ by modifying (ii) to ρ′(X′ + β−1m) =
ρ′(X′) −m. The remaining axioms remain unchanged. Conversely, given
such a risk measure ρ′ defined on the set of undiscounted positions X′,
a coherent risk measure defined on discounted values is given by ρ(X) =
ρ′(β−1X) = ρ′(X′). Thus we shall assume throughout that X represents
the discounted values.
Note that, while V aR satisfies properties (i)-(iii) (see Lemma 11.1.3),
it fails to have the subadditivity property (iv), as the earlier examples
illustrate.
It is easy to see that, in the presence of (iii), the subadditivity property
(iv) is equivalent to convexity: let X, Y and 0 ≤λ ≤1 be given and note
that, if a risk measure ρ satisfies (iii) and (iv), then
ρ(λX + (1 −λ)Y ) ≤ρ(λX) + ρ((1 −λ)Y ) = λρ(X) + (1 −λ)ρ(Y )
so that ρ is convex. Conversely, still assuming that (iii) holds, if ρ is convex,
then for any X, Y
ρ(X + Y ) = 2ρ
1
2(X + Y )

≤2
1
2ρ(X) + 1
2ρ(Y )

= ρ(X) + ρ(Y ),


## Measures of Risk

310
CHAPTER 11. MEASURES OF RISK
so that ρ has the subadditivity property (iv).
Convexity provides a more general statement that diversification of the
investor’s portfolio does not increase risk, while the subadditivity property
is important for risk managers in banks, as it ensures that setting risk limits
independently for different trading desks (i.e., risk allocation) will not lead
to a greater overall risk for the bank.
Convex risk measures (for which the property (iii) is typically not as-
sumed, thus allowing risk to grow non-linearly as the position increases)
were introduced by Foellmer and Schied and are studied extensively in
[132]. However, we shall not pursue this and restrict our analysis to coher-
ent risk measures.
Following Nakano, [235] we consider coherent risk measures that are
lower semi-continuous in the L1-norm; i.e., given X ∈L1 and ε > 0, we
have
ρ(Y ) > ρ(X) −ε when ∥X −Y ∥1 < ε.
Equivalently,
lim inf
Y →X ρ(Y ) ≥ρ(X).
(11.10)
In particular, (11.10) holds if the sequence (Xn) converges to X in L1-norm.
Remark 11.2.3. In [74], coherent risk measures are initially defined on L∞.
Lower semi-continuity with respect to the topology of convergence in prob-
ability is assumed in this context and is then referred to as the Fatou
property.
Lemma 11.2.4. Let ρ be a coherent risk measure. Then
(i) if a ≤X ≤b, then −b ≤ρ(X) ≤−a;
(i) ρ(X + ρ(X)) = 0.
Proof. As the random variable X−a ≥0, ρ(X−a) ≤0 by (i) and ρ(X−a) =
ρ(X) + a by (ii). Hence ρ(X) ≤−a. Taking X = 0 and λ = 0 in (iii)
yields ρ(0) = 0. Taking X = 0 in (ii), we obtain ρ(k) = −k. As X ≤b,
b −X ≥0, so ρ(−X + b) = ρ(−X) −b ≤0 using (ii) and (i). Therefore,
ρ(−X) ≤b. Now ρ(X −X) = ρ(0) = 0 ≤ρ(X) + ρ(−X) by (iv), so that
−ρ(X) ≤ρ(−X) ≤b, giving ρ(X) ≥−b.
Taking k = ρ(X), the second assertion follows immediately from (ii).
Example 11.2.5. Suppose that the probability space (Ω, F, P) is equipped
with a family P of probability measures, each of which is absolutely con-
tinuous with respect to P. Write
ρP(X) = sup {EQ (−X) : Q ∈P} .
(11.11)
Then ρP is a coherent risk measure.
Exercise 11.2.6. Prove this assertion.

11.2. COHERENT RISK MEASURES
311
This example is fundamental. We shall show in Theorem 11.2.19, that
under quite mild assumptions every coherent risk measure has this form.
We give two examples of such risk measures for extreme choices of the
family P that show that the choice of P needs to be made with some care
in order to obtain ‘sensible’ risk measures: the family P should be neither
too big nor too small.
Example 11.2.7. Suppose that P = {P} . Then ρP(X) = EP (−X) . Thus
a portfolio or position X is acceptable under this risk measure if and only
if EP (X) ≥0.
This risk measure is too tolerant. It makes insufficient demand on the
probability that the position X is positive.
Example 11.2.8. Suppose now that P is the set of all probability measures
on (Ω, F) that are absolutely continuous with respect to P. In this case, we
simply have sup {EQ (X) : Q ∈P} = ess sup X, so that ρP(X) ≤0 if and
only if X ≥0 a.s. (P).
For this choice of P, a position is acceptable if and only if it is almost
surely non-negative. This risk measure is too strict. We thus seek families
P that avoid these two extremes.
Restrictions on the Radon-Nikodym
derivatives dQ
dP will ensure this.
Notation 11.2.9. Given the probability space (Ω, F, P) and k ∈N, write
Pk =
$
Q : Q is a probability measure, Q ≪P and dQ
dP ≤k
%
.
(11.12)
Note that as Q is a probability measure, we must have dQ
dP ≥0 a.s. (P).
Moreover, we have the following.
Exercise 11.2.10. Show that if Q is a probability measure and dQ
dP ≤1 a.s.,
then Q = P.
Consequently, we shall assume that k > 1. The following important
result shows that when the distribution of the integrable random variable
X does not have a jump at qα(X), the family Pk provides us with a coherent
risk measure that dominates V aR.
Theorem 11.2.11. Suppose X ∈L1 and X has a continuous distribution
function FX. For k > 1, write α = 1
k. Then
ρPk(X) = EP (−X |X ≤qα(X)) ≥−qα(X) = V aRα(X).
Proof. As FX is continuous, (11.4) shows that
P[X ≤qα(X)] = FX(qα(X)) = α = 1
k .
Write A = {X ≤qα(X)} and consider the measure Qα defined by dQα
dP
=
k1A. Then Qα ∈Pk and
EQα (−X) = EP

−X
 1
α1A


312
CHAPTER 11. MEASURES OF RISK
=
1
P(A)EP (−X1A)
= EP (−X |A) ≥−qα(X) = V aRα(X).
Consider an arbitrary Q ∈Pk. Since dQ
dP ≤k, A = {X ≤qα(X)} and
k =
1
P (A), we obtain
EQ (−X) =

A
(−X)dQ
dP dP +

Ac(−X)dQ
dP dP
= k

A
(−X)dP +

A
(−X)
dQ
dP −k

dP +

Ac(−X)dQ
dP dP
≤k

A
(−X)dP −qα(X)

A
dQ
dP −k

dP + (−qα(X))

Ac
dQ
dP dP
= k

A
(−X)dP −qα(X)[Q(A) −kP(A) + Q(Ac)]
= k

A
(−X)dP = EQα (−X) .
Remark 11.2.12. However, it was shown in [4] that for general distribu-
tions the quantity EP (−X |A) does not define a subadditive function of
X. Hence the risk measure so defined, which is known as the tail condi-
tional expectation at level α and is sometimes written as TCE α(X), can in
particular circumstances suffer the same shortcomings as V aR.
Nonetheless, TCE α(X) has been proposed in the literature as a possible
improvement upon V aR. To illustrate some of its advantages, we have the
following example, which is taken from [74].
Example 11.2.13. A bank has 150 clients, labelled C1, C2, . . . , C150. Write
Di for the random variable, which equals 1 if client i defaults on a loan
and equals 0 if client i does not default. Suppose the bank lends $1000
to each client C1, C2, . . . , C150. Initially we suppose that all the defaults
are independent and that P(Di = 1) = 1.2%. The number Σ150
i=1Di thus
represents the total number of defaults, and the bank’s total loss is therefore
1000(Σ150
i=1Di) dollars.
Now D = Σ150
i=1Di has a binomial distribution and
P(D = k) =
150!
k!(150 −k)!(0.012)k(0.988)150−k.
If we take α = 1%, it can be shown that V aRα(D) = 5 and E (D |D ≥5) =
6.287.
Suppose, however, that the defaults are dependent. This can be mod-
elled by introducing a probability Q, where dQ
dP ceεD2. Here D and P are
as above, ε > 0, and c is a normalising constant chosen so that Q is a

11.2. COHERENT RISK MEASURES
313
probability measure. Then Q[Di = 1] increases as ε increases. Choosing
ε = 0.03029314, α = 1%, and p = 0.01 (recalling that D is binomial), we
obtain Q[Di = 1] = 1.2% and V aRα(D) = 6, but E (D |D ≥6) = 14.5.
Consequently, V aR does not distinguish between the two cases, while
the tail conditional expectation E (D |D ≥V aRα(D)) distinguishes clearly
between them.
The probability Q can model the situation where, if a number of clients
default, there is a higher conditional probability that other clients will
also default.
We note that V aR is only a quantile and thus does not
provide information about the size of the potential losses, whereas the tail
conditional expectation is an average of all the worse cases and so provides
better information about the tail distribution of the losses. It is, however,
more difficult to calculate in many practical examples. The amendment
required to rescue the proof of Theorem 11.2.11 is as follows (compare the
definition of CV aR Section 11.3).
Corollary 11.2.14. If the distribution of X has a discontinuity at qα, the
proof of Theorem 11.2.11 applies with the modification
dQα
dP
= k1{X<qα} + β1{X=qα},
where k =
1
P (X<qα) and β =
1
P (X=qα).
Remark 11.2.15. The complications introduced by the presence of jumps in
the distribution function FX have led to a proliferation of proposals for risk
measures that dominate V aR. We shall not examine them further but refer
the reader to [4] for a clear account of their main features. For our purposes,
it suffices to note that if FX is continuous, then Theorem 11.2.11 shows
that the tail conditional expectation TCE α(X) coincides with the so-called
worst conditional expectation WCE α(X), which can equivalently be defined
as −inf {EQ (−X) : P(A) > α}. Moreover, in this case these measures are
the same as the so-called conditional value at risk, CV aRα(X), although
this description is really a misnomer since in the general case this quantity,
which has also become known as expected shortfall, cannot be expressed as
a conditional expectation of a quantity defined solely in terms of X. We
shall return briefly to a consideration of the properties of expected shortfall
in the next section.
Polar Sets and the Bipolar Theorem
In this brief subsection, we introduce definitions and results from functional
analysis, which we state without proof.
More details and proofs of the
quoted results can be found in standard texts such as [264], [97].
Recall that the dual E∗of a real Banach space E is the vector space of
all continuous linear functionals f : E →R on E, and that E∗is a Banach
space under the norm |f| = sup {|f(x)| : |x| ≤1} . We shall need to consider

314
CHAPTER 11. MEASURES OF RISK
various topologies on E and E∗. The weak∗topology on E∗is the locally
convex topology induced by the family of seminorms S = {px : x ∈E} ,
where px(f) = |f(x)| for f ∈E∗. Thus the sets
{{f : px(f −f0) < ε} : px ∈S, f0 ∈E∗, ε > 0}
form a subbase for the weak∗topology σ(E∗, E) on E∗. It is traditional to
write x∗for elements of E∗, and we do so below.
Our first result is commonly known as the Krein-Smulian theorem.
Theorem 11.2.16. Suppose E is a Banach space with dual space E∗.
A convex set S ⊂E∗is weak∗-closed if and only if for each n ∈N its
intersection with the closed ball Bn = {e∗: ∥e∗∥≤n} is weak∗-closed; i.e.,
each set Sn = S ∩Bn is weak∗-closed.
We shall also need the Bipolar theorem, which describes the closed
convex balanced hull (see below) of a set A ⊂E in terms of the dual E∗of
E. First, define the polar of A ⊂E by A◦= {x∗∈E∗: |x∗(a)| ≤1∀a ∈A} .
This set is convex (i.e., closed under convex combinations) and balanced
(i.e., if x∗∈A◦, |λ| ≤1 then λx ∈A◦).
Note in particular that when A is itself closed under multiplication
by positive scalars (e.g., when A is a cone), then the polar cone A◦may
equivalently be defined as {x∗∈E∗: x∗(a) ≥0∀a ∈A}.
The operation
may equally be applied to A◦to define the bipolar A◦◦= (A◦)◦.
The
Bipolar theorem then states the following.
Theorem 11.2.17. In any locally convex space E, the bipolar of a set
A ⊂E is its closed convex balanced hull (i.e., the smallest set with these
properties containing A).
This is a consequence of the Hahn-Banach theorem. For the dual pair
(L1, L∞), we note in particular that if A ⊂L1 is a closed convex cone
and Z ∈L1 \ A, then we can find Y
∈L∞such that E (ZY ) < 0
and E (XY ) ≥0 for all X in A. But then the polar A◦of A is the set
{Y ∈L∞: E (XY ) ≥0 for X ∈A} so that Z cannot be in the polar of
A◦. Since trivially A ⊂A◦◦, it follows that A = A◦◦.
Definition 11.2.18. Let (Ω, F, P) be a probability space and ρ : L1(Ω) →
R a coherent risk measure. Write A =

X ∈L1(Ω) : ρ(X) ≤0

. We call
A the set of acceptable positions, or the acceptance set for ρ.
Note that because ρ is subadditive and positive homogeneous, A is a
convex cone.
Representation of Coherent Risk Measures
We now have the following result, specifying conditions under which we can
represent every coherent risk measure in the form given in Example 11.2.5.
Write Q for the set of all probability measures on (Ω, F) that are absolutely
continuous with respect to P. Write ZQ = dQ
dP for Q ∈Q.

11.2. COHERENT RISK MEASURES
315
Theorem 11.2.19. Suppose ρ : L1 →R. The following are equivalent.
(i) The function ρ is a lower semi-continuous coherent risk measure.
(ii) There is a subset -Q of Q such that

ZQ : Q ∈-Q

is a weak∗-closed
convex subset of L∞and for X ∈L1
ρ(X) = sup
Q∈
Q
EQ (−X) .
(11.13)
Proof. That the second statement implies the first is immediate. For the
converse, write φ(X) = −ρ(X) and recall that A =

X ∈L1 : ρ(X) ≤0

=

X ∈L1 : φ(X) ≥0

is the set of acceptable positions. Then A is clearly a
convex cone. As φ is upper semi-continuous, the set A is also closed in the
L1-norm. To see this, let (Xn) be a sequence in L1 with ∥Xn −X∥1 →0.
By lower semi-continuity, ρ(X) = ρ(limn Xn) ≤lim infn ρ(Xn) ≤0, so that
X ∈A. Applying the comments following the Krein-Smulian theorem to
the cone A, we see that
A◦= {Y ∈L∞: E (XY ) ≥0 for all X ∈A} .
Thus A◦is a weak∗-closed convex cone in L∞, and, writing
C = {Y ∈A◦: E (Y ) = 1} ,
it follows that A◦= ∪λ≥0λC. In fact, if A ∈A◦and E (Y ) > 0, then
Y = λ-Y for -Y =
Y
E(Y ) ∈C, and λ = E (Y ) . Further, we have L1
+ ⊂A since
all indicator functions 1A (A ∈F) belong to L1
+, so that if E (Y 1A) ≥0
for all A ∈F, then Y ≥0 a.s. Hence, if Y ∈A◦and E (Y ) = 0, then
Y = 0 a.s.
The bipolar theorem now implies that
A =

X ∈L1 : E (XY ) ≥0 for all Y ∈C

.
Consequently, φ(X) ≥0 if and only if E (XY ) ≥0 for all Y ∈C.
Now φ(X −φ(X)) = 0, so E (X −φ(X)Y ) ≥0 for all Y ∈C. This
implies that infY ∈CE (XY ) ≥φ(X).
For any ε > 0, we have φ(X −φ(X)) −ε < 0, so there is a Y in C such
that E (X −φ(X) −ε) < 0, or E (XY ) ≤φ(X) + ε. But ε is arbitrary, so
infY ∈C E (XY ) ≤φ(X). Hence they are equal.
If we write
-Q = {Q ∈Q : ZQ = Y for some Y ∈C} ,
then the identity
φ(X) = inf
Y ∈C E (XY )
implies that -Q is a weak∗-closed subset of L∞. But C =

ZQ : Q ∈-Q

, so
this is the required representation for ρ.

316
CHAPTER 11. MEASURES OF RISK
11.3
Deviation Measures
An alternative approach to risk measures has been proposed in [246], [293].
This is based on the concept of a deviation measure and is related to gener-
alisations of standard deviation or variance. We give an axiomatic descrip-
tion and derive the most basic properties, while briefly relating deviation
measures to coherent risk measures.
As we have seen, the minimisation of standard deviation or variance is
a familiar objective in portfolio optimisation. Problems with this approach
are that it penalises up and down deviations equally and that it does not
take account of ‘fat tails’ in loss distributions.
A related criticism of coherent risk measures and V aR is that they
measure a negative outcome of the position X. For practitioners, ‘loss’ often
refers to the shortfall relative to expectation. That is, for practitioners, risk
measures usually refer to X −E (X) .
Working on the probability space (Ω, F, P) we shall define a deviation
measure on the space L2(Ω).
Definition 11.3.1. A deviation measure is a functional D : L2(Ω) →
[0, ∞] satisfying:
D1. D(X + C) = D(X) for X ∈L2(Ω) and C ∈R;
D2. D(λX) = λD(X) for λ > 0;
D3. D(X + Y ) ≤D(X) + D(Y ) for X, Y ∈L2(Ω);
D4. D(C) = 0 for C ∈R, and D(X) > 0 if X is non-constant.
Note that D(X −E (X)) = D(X) from D1. It follows from D4 that
D(X) = 0 if and only if X −E (X) = 0 since D(Y ) = 0 if and only if Y = c
is constant. But X −E (X) = c implies c = 0 since E (X −E (X)) = 0.
However, in general, D may not be symmetric; that is, it is possible that
D(−X) ̸= D(X).
Note that if D is a deviation measure, then its reflection C, given by
C(X) = D(−X), is also a deviation measure, and its symmetrisation, -D,
given by -D(X) = 1
2[D(X) + C(X)], is a deviation measure.
Example 11.3.2. Standard deviation σ(X) = (E ((X −E (X)))2)
1
2 is a de-
viation measure, as are
σ+(X) =

E

(max {X −E (X) , 0})2 1
2
and
σ−(X) =

E

(max {E (X) −X, 0})2 1
2 .
To relate deviation measures and coherent risk, expectation-bounded
risk measures are introduced in [246].
Definition 11.3.3. An expectation-bounded risk measure on L2(Ω) is a
functional R : L2(Ω) →(−∞, ∞] satisfying:

11.3. DEVIATION MEASURES
317
R1. R(X + C) = R(X) −C for X ∈L2(Ω) and C ∈R;
R2. R(0) = 0 and R(λX) = λR(X) for X ∈L2(Ω) and λ > 0;
R3. R(X + Y ) ≤R(X) + R(Y ) for X, Y ∈L2(Ω);
R4. R(X) > E (−X) for non-constant X and R(X) = −X for constant
X.
An expectation-bounded risk measure is coherent if, further,
R5. R(X) ≤R(Y ) when X ≥Y.
From R1 and R2 it is clear that R(C) = −C.
Property R4 is described as expectation-boundedness.
Property R5 is again monotonicity. Although R5 is apparently stronger
than condition (i) of Definition 11.2.1, we see that if X ≤Y a.s., then
Y = X + (Y −X) where (Y −X) ≥0. Consequently, if ρ satisfies (i) and
(iv) of Definition 11.2.1, then ρ(Y ) ≤ρ(X) + ρ(Y −X) ≤ρ(X). That is,
a coherent risk measure satisfies condition R5.
Note that if R is a functional satisfying R1-R4, then, on L2(Ω), it
satisfies the conditions of Definition 11.2.1 and so is a coherent risk measure.
The next result relates deviation measures to expectation-bounded risk
measures.
Theorem 11.3.4. Suppose D : L2(Ω) →[0, ∞] is a deviation measure.
Then R(X) = D(X) −E (X) is an expectation-bounded risk measure.
Conversely, if R is this expectation-bounded risk measure, then D(X) =
R(X −E (X)).
Proof. Suppose D is a deviation measure. The properties R2 and R3 follow
from D2 and D3. Also,
R(X + C) = D(X + C) −E (X) −C
= D(X) −E (X) −C
= R(X) −C,
so R satisfies R1.
From D4, if X is non-constant,
D(X) = R(X) + E (X) > 0,
and R4 follows.
Conversely, if D(X) = R(X −E (X)), then
D(X + C) = R((X + C) −E (X) −C)
= R(X) + E (X)
= D(X),
so D1 is satisfied. Again, D2 and D3 follow from R2 and R3. Also, for
non-constant X, R1 and R4 imply
R(X −E (X)) = R(X) + E (X) > 0.
Therefore D4 is satisfied. This completes the proof.

318
CHAPTER 11. MEASURES OF RISK
Example 11.3.5. For X ∈L2(Ω), write
D(X) = E (X) −ess inf X = ess sup {E (X) −X} .
This is a deviation measure describing the lower range of X. R(X) =
ess sup(−X) is the corresponding risk measure. Both D and R are co-
herent, and R is expectation-bounded.
Conditional Value at Risk, or Expected Shortfall
A popular risk measure is conditional value at risk, CV aR. If we assume
that there is a zero probability that X = V aRα(X), we can define this as
a true conditional expectation: for α ∈(0, 1) and X ∈L2(Ω),
CV aRα(X) = −E (X |X ≤V aRα(X)) .
When X has a general distribution (i.e., possibly with jumps), this breaks
down. Thus we define CV aR as follows: let U = {X ≤qα(X)} and write
CV aRα(X) = −α−1E(X1U) + qα(X)(α −P(U)).
This quantity is also called the expected shortfall by some authors and has
other attractive features, such as continuity in the quantile level α, which
can be seen immediately from its representation in integral form; see [4] for
a derivation:
CV aRα(X) = −1
α
 α
0
qβ(X)dβ.
(11.14)
We introduce the following notation.
Notation 11.3.6. For α ∈(0, 1), write
1α
{X≤x} =

1{X≤x} + α−P (X≤x)
P (X=x) 1{X=x}
if P(X = x) > 0,
1{X≤x}
if P(X = x) = 0.
Then
1α
{X≤qα(X)} ∈[0, 1],
(11.15)
E

1α
{X≤qα(X)}

= α −α−1E

X1α
X≤qα(X)

= CV aRα(X).
(11.16)
We now show that CV aR is a coherent risk measure.
Theorem 11.3.7. Suppose α ∈(0, 1). Write ρ : L2(Ω) →R for ρ(X) =
CV aRα(X). Then:
(i) if X ≥0, ρ(X) ≤0;
(ii) if λ ≥0, then ρ(λX) = λρ(X);

11.3. DEVIATION MEASURES
319
(iii) if k ∈R, then ρ(X + k) = ρ(X) −k;
(iv) if X, Y ∈L2(Ω), then ρ(X + Y ) ≤ρ(X) + ρ(Y ).
Proof. (i) From the definition, if X ≥0, then ρ(X) = CV aRα(X) ≤0.
(ii) For λ ≥0, P(λX ≤λx) = P(X ≤x), so
qα(λX) = inf{λx : P(λX ≤λx) ≥α}
= λ inf{x : P(X ≤x) ≥α}
= λqα(X).
Therefore, setting D(U) = {U ≤qα(U)} for any random variable U, we
have
ρ(λX) = CV aRα(X)
= −α−1 
E

λX1D(λX)

+ qα(X)(α −P(D(λX)))

= −α−1λ

E

X1D(λX) + qα(X)(α −P(D(λX)))

= λCV aRα(X) = λρ(X).
(iii) For k ∈R, P(X + k ≤x + k) = P(X ≤x), so that
qα(X + k) = inf
x {x + k : P(X + k ≤x + k) ≥α}
= k + inf
x {x : P(X ≤x) ≥α}
= k + qα(X).
Therefore
ρ(X + k) = CV arα(X + k)
= −α−1 
E

(X + k)1{D(X+k)}

+ qα(X + k)(α −P(D(X + k)))

= −α−1 
E

X1{D(X)}

+ qα(X)(α −P(D(X)))

−α−1k

E

1{D(X+k)}

+ α −P(D(X + k))

= ρ(X) −k.
(iv) Using the notation introduced above, we prove that ρ is subadditive.
Suppose that X, Y ∈L2(Ω) and write Z = X + Y. Then, from (11.7),
α(ρ(X) + ρ(Y ) −ρ(Z))
= E

Z1α
{D(Z)} −X1α
{D(X)} −Y 1α
{D(Y )}

= E

X(1α
{D(Z)} −1α
{D(X)})

+ E

Y

1α
{D(Z)} −1α
{D(Y )}

≥qα(X)E

1α
{D(Z)} −1α
{D(X)}

+ qα(Y )E

1α
{D(Z)} −1α
{D(Y )}

= qα(X)(α −α) + qα(Y )(α −α) = 0.

320
CHAPTER 11. MEASURES OF RISK
We have used the facts that
1α
{Z≤qα(Z)} −1α
{X≤qα(X)} ≥0 if X > qα(X)
and
1α
{Z≤qα(Z)} −1α
{{X≤qα(X)} ≤0 if X < qα(X).
This follows from the definition of 1α.
Remark 11.3.8. This brief review of various approaches to measuring risk,
including V aR and deviation measures, has only skimmed the surface of re-
cent work in this very active field of research. Importantly, this research has
revealed deficiencies of V aR, which is still the dominant risk-management
tool used in practice. The concept of coherent risk measure was created
to address this situation, and to aid computation and the construction
of concrete examples for particular needs, a representation result for such
measures was established. In particular, conditional value at risk, CV aR,
has been shown to be a coherent measure of risk. Deviation measures and
the related bounded expectation measures were introduced with similar
objectives in view, and we have shown how relationships with coherent risk
measures can be established. Though this field is one of intense current
research, it may take time for the newer concepts touched upon here to
settle down and become common in financial practice.
An area of much current work is the extension of these ideas to a multi-
period setting, where martingales and generalised Snell envelopes come to
the fore. The interested reader is referred to the recent papers [10], [11] for
this material, which is beyond the scope of this book.
11.4
Hedging Strategies with Shortfall Risk
This final section outlines how risk measures can be applied to the construc-
tion of hedging strategies for financial assets, which is one of the principal
topics covered in this book. We have seen how, in a viable financial market
model, derivative securities can be priced by arbitrage considerations alone,
and that this price, as well as the replicating strategy, are uniquely deter-
mined when the market is complete. For incomplete markets, we were able
to reproduce these results for attainable claims, but in the general case the
buyer’s and seller’s prices represent the limits of an arbitrage interval of
possible prices for the claim, and additional optimality criteria are needed
to identify both the optimal price and optimal hedging strategy.
An investor can always play safe by employing a ‘superhedging strategy’
- an approach outlined in Chapters 2 and 7 for discrete and continuous-time
pricing models, respectively (also see [184] for a fuller account). However,
the initial capital required to eliminate all risk may be considered too high
by the investor, who may be willing instead to accept the risk of loss at

11.4. HEDGING STRATEGIES WITH SHORTFALL RISK
321
a specified level.
The question then becomes: how much initial capital
can be saved by accepting the risk of having to find additional capital at
maturity in (say) 1% of all possible outcomes? A second question is then:
by what criteria should the shortfall risk be measured, or what measure of
risk should be employed?
In [128],[129] F¨ollmer and Leukert introduced these ideas and showed
how the problem of such ‘quantile hedging’ against a given contingent claim
H can be reduced to consideration of an optimisation problem for the
modified claim φH, where φ ranges over the class of ‘randomised tests’
(i.e., FT -measurable random variables with values in the interval [0, 1]).
This allows an application of the Neyman-Pearson lemma from the theory
of hypothesis testing to provide an optimal solution (see, e.g., [303] for a
detailed treatment). Here we confine attention to integrable claims, and,
in particular, adapt the treatment given in [235] using coherent measures
of risk.
Quantile Hedging in a Complete Market
Assume that the price process (St)t∈[0,T ] is given as a semimartingale de-
fined on a probability space (Ω, F, P) adapted to a filtration F = (Ft)t∈[0,T ],
where F0 is assumed to be trivial and FT = F. We assume that this mar-
ket model is viable, so that the set P of equivalent martingale measures is
non-empty. In this market, a self-financing strategy (V0, θ) is determined
by the initial capital V0 and a predictable process θ such that the resulting
value process V = (Vt) satisfies, P-a.s. for all t,
Vt = Vt(θ) = V0 +
 t
0
θudSu,
(11.17)
where we shall assume the usual integrability conditions without further
mention (see Chapter 7). The strategy is admissible if also Vt ≥0 P-a.s.
for all t.
In a complete market, there is a unique measure Q ∼P under which the
(discounted) price process is a martingale. For simplicity, we shall assume
that the discount rate is 0, so that St already represents the discounted
asset price. Now let H ∈L1
+(Q) be a contingent claim. There is a perfect
hedging strategy θH such that for all t, P-a.s.,
EQ(H|Ft) = H0 +
 t
0
θH
u dSu.
(11.18)
Thus the claim H is replicated by the strategy (H0, θH), provided the
investor allocates initial capital H0 = EQ(H) to the hedge.
However,
suppose the investor is willing to allocate initial capital at most V ∗
0 to
hedge against the claim H. We may then seek the strategy that provides
maximum probability that the hedge will be successful (i.e., will suffice to

322
CHAPTER 11. MEASURES OF RISK
cover the liability of the claim at time T). In other words, we seek the
strategy (V0, θ) that maximises the probability of the set
A(H, θ) = {VT ≥H} =

ω : V0 +
 T
0
θu(ω)dSu(ω) ≥H(ω)

(11.19)
subject to the constraint
V0 ≤V ∗
0 .
(11.20)
In [128], A(H, θ) is called the success set for the claim and the resulting
strategy. For any measurable set B, we can consider the knockout option
HB = H1B, which, at time T, pays out H(ω) if ω ∈B and 0 otherwise.
Note that with our assumptions HB ∈L1
+(Q). As the market model is com-
plete, this contingent claim can be hedged perfectly by a unique admissible
strategy. Now let A∗be a success set for H with maximal probability; i.e.,
such that
P(A∗) = max P(A(H, θ))
(11.21)
subject to the constraint
EQ(H1A(H,θ)) ≤V ∗
0 .
(11.22)
Denote the perfect hedging strategy for the knockout option HA∗= H1A∗
by θ∗. Thus we have P-a.s for all t ≤T,
EQ(H1A∗|Ft) = EQ(H1A∗) +
 t
0
θ∗
udSu.
(11.23)
This allows us to reduce the original optimisation problem to the ques-
tion of constructing a success set of maximal probability.
Proposition 11.4.1. Suppose that, as defined above, A∗is a success set
with maximal probability under the constraint (11.22). Then the perfect
hedging strategy (V ∗
0 , θ∗) for the knockout option HA∗solves the optimisa-
tion problem defined by (11.19),(11.20), and its success set is P-a.s. equal
to A∗.
Proof. First consider any admissible strategy (V0, θ) with V0 ≤V ∗
0 . The
process Vt = V0 +
4 t
0 θudSu is a non-negative local martingale and hence
a supermartingale (see Lemma 7.5.3) under Q. Since VT ≥0 P-a.s., the
success set A = A(H, θ) for this strategy satisfies VT ≥H1A P-a.s., so that
V ∗
0 ≥V0 ≥EQ(VT ) ≥EQ(H1A).
This shows that A satisfies the constraint (11.22), and therefore, by the
definition of A∗, we conclude that P(A) ≤P(A∗).
We will show that any strategy (V0, θ∗) satisfying EQ(H1A∗) ≤V0 ≤V ∗
0 is

11.4. HEDGING STRATEGIES WITH SHORTFALL RISK
323
optimal. Such a strategy is admissible since, P-a.s., H1∗
A ≥0, so that by
(11.23),
V0 +
 t
0
θ∗
udSu ≥EQ(H1A∗) +
 t
0
θ∗
udSu = EQ(H1A∗|Ft) ≥0.
(11.24)
Consider the success set A(H, θ∗) for the strategy (V0, θ∗). We have
A∗⊂{H1A∗= H} ⊂A(H, θ∗)
since V0 ≥EQ(H1A∗) and (11.23) imply that VT (θ∗) ≥H a.s. on A∗.
On the other hand, A∗has maximal P-measure among success sets, so it
follows that A∗= A(H, θ∗) P-a.s. Hence the strategy (V0, θ∗) is an optimal
solution of the original problem (11.19), (11.20), as required.
Remark 11.4.2. Having reduced the problem to that of finding a maximal
success set, we briefly recall the basic elements of the Neyman-Pearson
theory of hypothesis testing: to discriminate between two given probability
measures P and P ∗, one may try to devise a pure test (i.e., a random
variable φ : Ω→{0, 1}), under which we reject P ∗if the event {φ = 1}
occurs. This allows for two kinds of erroneous conclusions: P ∗(φ = 1) is
the probability that we reject P ∗in error, and P(φ = 0) = 1 −P(φ = 1) is
the probability that P ∗is accepted in error. In general, it is not possible
to minimise both probabilities simultaneously. However, one can accept a
tolerance level α (e.g., α = .01) for the first kind of error - much as is done
for V aR - and seek instead to solve a constrained optimisation problem
for the second kind, i.e., we seek to maximise P(φ = 1) subject to the
constraint
P ∗(φ = 1) ≤α.
(11.25)
A solution for this optimisation problem can be found by choosing a
third probability measure Q such that P and P ∗are both absolutely con-
tinuous with respect to Q, with densities ZP and ZP ∗, respectively. The
key quantity is then the likelihood ratio ZP /ZP ∗: the optimal test is the
function
φ∗= 1{a∗ZP ∗<ZP },
(11.26)
where a∗∈(0, ∞) is chosen so that P ∗(a∗ZP ∗< ZP ) = α. Thus the test
φ∗rejects P ∗if and only if the likelihood ratio exceeds the level a∗.
To construct a maximal success set in the family A(H, θ), we therefore
introduce the measure P ∗≪Q with Radon-Nikodym derivative
dP ∗
dQ =
H
EQ(H) = H
H0
.
(11.27)
The constraint EQ(H1A) ≤V ∗
0 becomes
P ∗(A) = EP ∗(1A∗) = 1
H0
EQ(H1A) ≤V ∗
0
H0
.
(11.28)

324
CHAPTER 11. MEASURES OF RISK
Write α = V ∗
0
H0 and define the set
-A =
dP
dQ > aH

.
(11.29)
Define the level a∗by
a∗= inf{a : P ∗[ -A] ≤α}.
(11.30)
The Neyman-Pearson lemma now allows us to deduce that -A is a success
set of maximal measure as follows.
Theorem 11.4.3. Suppose that P ∗( -A) = α. Then the optimal strategy
solving (11.19), (11.20) is the unique replicating strategy (V ∗
0 , θ∗) for the
knockout option H1 
A.
Proof. Both P and P ∗are absolutely continuous with respect to the unique
EMM Q, and the set -A consists precisely of the points ω ∈Ωat which
dP
dQ(ω) > -aH0 dP ∗
dQ (ω), so that the likelihood ratio is bounded below by the
constant -aH0. Then the Neyman-Pearson lemma states that for any mea-
surable set A, P ∗(A) ≤P ∗( -A) implies P(A) ≤P( -A). Hence the constraint
(11.22) is satisfied and -A is a success set of maximal measure, so that, by
Proposition 11.4.1, the strategy (V ∗
0 , θ∗) solves the original optimisation
problem.
Remark 11.4.4. These ideas are taken much further in [128], where explicit
results are given for the Black-Scholes model and the theory is developed
further for incomplete markets. We do not pursue this here but will instead
sketch briefly how the same ideas may be used in the context of coherent
risk measures.
However, in the more general situation, we need to extend the class
of ‘tests’ that allows us to discriminate between alternative hypotheses
since the ‘level’ a∗defined in (11.30) need not exist in general. To deal
with this, we replace the {0, 1}-valued test function φ∗by a more general
‘randomised’ test φ with possible values ranging through the interval [0, 1].
The interpretation of these tests is that, in the event that the outcome
ω ∈Ωis observed, then P ∗is rejected with probability φ(ω) and rejected
with probability 1 −φ(ω). This means that EP (φ) provides for us the
probability of rejecting the hypothesis P ∗when it is false (and thus defines
the power of the test φ), while EP ∗(φ) gives the probability of error of
the first kind (rejecting P ∗when it is true). The optimisation problem to
be solved is therefore to maximise EP (φ) over all tests φ that satisfy the
constraint E∗
P (φ) ≤α. This problem again has an explicit solution, as will
be seen in the general situation outlined in the next subsection.
Efficient Hedging with Coherent Risk Measures
We outline the results obtained in [235]. As in the previous subsection,
assume as given a viable market model (Ω, F, P, (Ft)t∈[0,T ], (St)t∈[0,T ]) and

11.4. HEDGING STRATEGIES WITH SHORTFALL RISK
325
denote the non-empty set of equivalent martingale measures by P. Assume
further that the integrable contingent claim H satisfies supQ∈P EQ(H) <
∞.
Now let ρ : L1 →R denote a coherent risk measure that is lower semi-
continuous in the L1-norm. We wish to minimise the shortfall risk when
using admissible hedging strategies with given initial capital V ∗
0 , so that
we seek the admissible strategy (V0, θ) that minimises
ρ(min[(VT −H), 0]) = ρ

min

V0 +
 T
0
θudSu −H

, 0

(11.31)
subject to the constraint
V0 ≤V ∗
0 .
(11.32)
Defining the set of ‘randomised tests’ (see [67] for an explanation of the
terminology, which comes from the theory of hypothesis testing) by
R = {φ : Ω→[0, 1] : φ is F-measurable}
and the constrained set of tests
R0 = {φ ∈R : sup
Q∈P
EQ(φH) ≤V ∗
0 },
(11.33)
we can use the representation theorem for coherent risk measures to prove
the following proposition.
Proposition 11.4.5. There exists a randomised test φ∗in R0 such that
inf
φ∈R0 ρ(−(1 −φ)H) = ρ(−(1 −φ∗)H).
(11.34)
Proof. The set R is σ(L∞, L1)-compact in L∞, and the map
φ →sup
Q∈P
EQ(φH)
is lower semi-continuous in the weak∗topology on L∞. Hence the set R0
is weak∗-closed and hence also weak∗-compact.
We recall the essential features of the proof of Theorem 11.2.19: if
Q denotes the set of all probability measures absolutely continuous with
respect to P, and C = {Y ∈A◦: E[Y ] = 1}, where A denotes the set of
acceptable positions for ρ, then the subset of Q given by
-Q = {Q ∈Q : ZQ = Y for some Y ∈C}
satisfies, for any X ∈L1,
ρ(X) = sup
Q∈
Q
EQ(−X)
(11.35)

326
CHAPTER 11. MEASURES OF RISK
and the set { dQ
dP : Q ∈-Q} is convex and weak∗-closed in L1.
But the L∞-functional
φ →sup
Q∈
Q
EQ[(1 −φ)H]
is also lower semi-continuous in the weak∗topology, so its infimum over R0
is attained.
This again reduces the original optimisation problem of finding an ad-
missible strategy that solves (11.31), (11.32) to the question of finding an
optimal randomised test φ∗. However, we first need to generalise the con-
cept of ‘success set’, which applies when φ is an indicator function, to this
more general context.
Definition 11.4.6. For any admissible strategy (V0, θ), the success ratio is
the function
φ(V0, θ) = 1{VT ≥H} + VT
H 1{VT <H}.
(11.36)
The role of the simple knockout option is now taken by φ∗H. We denote
by V ∗the right-continuous version of the process
V ∗
t = ess sup
Q∈P
EQ(φ∗H|Ft).
This is a supermartingale for every Q in P, and thus the optional decom-
position theorem (see [201], [129]) applies to provide an admissible strategy
(V ∗
0 , θ∗) and an increasing optional process C∗with C∗
0 = 0 such that
V ∗
t = V ∗
0 +
 t
0
θ∗
udSu −C∗
t .
Remark 11.4.7. The force of the optional decomposition theorem is to pro-
vide a characterisation of the wealth processes defined in Chapters 7 and
10. The collection of processes V defined by Vt = V0+
4 t
0 θudSu−Cu, where
C = (Cu)u∈[0,T ] is adapted and increasing, with C0 = 0, is identical with
the collection of P- supermartingales (i.e., processes that are supermartin-
gales for every EMM Q).
The decomposition is non-unique, unlike the
Doob-Meyer decomposition of the P-supermartingale Vt = V0 + Mt −At,
where A is increasing and predictable, with A0 = 0. However, under the
stronger condition that V is a supermartingale for each EMM Q the mar-
tingale M can be taken to be the stochastic integral (i.e., a gains process)
generated by some admissible strategy θ at the cost of relaxing the require-
ments on the ‘compensator’ C.
The strategy (V ∗
0 , θ∗) provides the solution to our original optimisa-
tion problem whenever the randomised test has the minimisation property
described in Proposition 11.4.5.

11.4. HEDGING STRATEGIES WITH SHORTFALL RISK
327
Theorem 11.4.8. Suppose that φ∗solves the minimisation problem posed
in Proposition 11.4.5 and (V ∗
0 , θ∗) is the admissible strategy for the claim
φ∗H determined by its optional decomposition, then this strategy solves the
optimisation problem (11.31), (11.32), and its success ratio is φ∗P-a.s.
Proof. The proof follows the same pattern as for the quantile hedging case.
Take an admissible strategy (V0, θ) satisfying the constraint V0 ≤V ∗
0 and
with success ratio φ. Since φH = VT ∧H, we have
(VT −H) ∧0 = −(VT −H)+ = −(H −VT ∧H) = −(1 −φ)H.
Also, the supermartingale property of V implies that
EQ(φH) ≤EQ(VT ) ≤V0 ≤V ∗
0 .
Hence the success ratio φ is in R0 and so
ρ((VT −H) ∧0) = sup
Q∈
Q
EQ((1 −φ)H) ≥sup
Q∈
Q
E((1 −φ∗)H).
(11.37)
In particular, the success ratio φ(V ∗
0 , θ∗) satisfies this inequality, while
on the other hand
φ(V ∗
0 , θ∗)H = V ∗
T ∧H ≥φ∗H,
so that, for all Q ∈-Q ,
EQ[(1 −φ(V ∗
0 , θ∗)H)] ≤EQ[(1 −φ∗)H].
This shows that the two quantities are equal, and so
ρ((V ∗
T −H) ∧0) = sup
Q∈
Q
EQ((1 −φ(V ∗
0 , θ∗)H)) = sup
Q∈
Q
E((1 −φ∗)H).
Remark 11.4.9. In [235] and [129], these general results are applied to
particular examples of coherent risk measures. In the context of the Black-
Scholes model, for example, that with ρ as the worst conditional expecta-
tion, the amount of capital ‘saved’ by accepting a given level of loss can be
computed explicitly. For a European call option H, where in the present
setting, with Φ denoting the cumulative normal distribution function, the
cost of replication is
EQ(H) = S0Φ(d+) −KΦ(d−),
let V ∗
0 ≤EQ(H) be a given level of initial capital, and assume further that
the drift µ ≥0 and that
P(H > 0) = Φ(µ

T + d−) ≤α.

328
CHAPTER 11. MEASURES OF RISK
Then it is shown in [235] that the minimisation problem for φ is solved by
the most powerful randomised test φ∗= 1{ST >c}, so that
V ∗
0 = EQ(H1{ST >c}
and the constant c can be determined from the identity
EQ(H1{ST >c}
= S0Φ

1
σ
√
T
log
S0
c

+ 1
2σ
√
T

−KΦ

1
σ
√
T
log
S0
c

−1
2σ
√
T

.

Bibliography
[1] K.K. Aase and B. Oksendal.
Admissible investment strategies in
continuous trading. Stochastic Process. Appl., 30:291–301, 1988.
[2] C. Acerbi, C. Nordio, and C. Sirtori. Expected shortfall as a tool for
financial risk management. Working paper, Abaxbank, 2001.
[3] C. Acerbi and D. Tasche. Expected shortfall: A natural coherent
alternative to value at risk. Working paper, Abaxbank, 2001.
[4] C. Acerbi and D. Tasche. On the coherence of expected shortfall.
Working paper, Abaxbank, 2002.
[5] W. Allegretto, G. Barone-Adesi, and R.J. Elliott. Numerical evalua-
tion of the critical price and American options. Eur. J. of Finance,
1:69–78, 1995.
[6] J.-P. Ansel and C. Stricker.
Lois de martingale, densit´es et
d´ecomposition de F¨ollmer-Schweizer. Ann. Inst. H. Poincar´e Probab.
Statist., 28:375–392, 1992.
[7] P. Artzner and F. Delbaen. Term structure of interest rates: The
martingale approach. Adv. Appl. Math., 10:95–129, 1989.
[8] P. Artzner, F. Delbaen, J. Eber, and D. Heath. Thinking coherently.
Risk, 10:68–71, 1997.
[9] P. Artzner, F. Delbaen, J. Eber, and D. Heath. Coherent measures
of risk. Math. Finance, 9:203–228, 1999.
[10] P. Artzner, F. Delbaen, J. Eber, D. Heath, and H. Ku. Coherent
multiperiod risk measurement. Preprint, ETH, 2002.
[11] P. Artzner, F. Delbaen, J. Eber, D. Heath, and H. Ku. Multiperiod
risk and multiperiod risk measurement. Preprint, ETH, 2002.
[12] P. Artzner, F. Delbaen, J. Eber, D. Heath, and H. Ku. Coherent
multiperiod risk-adjusted values and Bellman’s principle. Preprint,
ETH, 2003.
329

330
BIBLIOGRAPHY
[13] P. Artzner and D. Heath. Approximate completeness with multiple
martingale measures. Math. Finance, 5:1–11, 1995.
[14] L. Bachelier. Theory of speculation. In P.H. Cootner, editor, The
Random Character of Stock Market Prices, volume 1018 (1900) of
Ann. Sci. ´Ecole Norm. Sup., pages 17–78. MIT Press, Cambridge,
Mass., 1964.
[15] G. Barone-Adesi and R.J. Elliott. Approximations for the values of
American options. Stochastic Anal. Appl., 9:115–131, 1991.
[16] G. Barone-Adesi and R.J. Elliott. Pricing the treasury bond futures
contract as the minimum value of deliverable bond prices. Rev. Fu-
tures Markets, 8:438–444, 1991.
[17] G. Barone-Adesi and R. Whaley.
The valuation of American call
options and the expected ex-dividend stock price decline. J. Finan.
Econ., 17:91–111, 1986.
[18] G. Barone-Adesi and R. Whaley. Efficient analytic approximation of
American option values. J. Finance, 42:301–320, 1987.
[19] E.M. Barron and R. Jensen. A stochastic control approach to the
pricing of options. Math. Oper. Res., 15:49–79, 1990.
[20] E. Barucci. Financial Markets Theory: Equilibrium, Efficiency and
Information. Springer, Heidelberg, 2003.
[21] B. Bensaid, J.-P. Lesne, H. Pag`es, and J. Scheinkman. Derivative
asset pricing with transaction costs. Math. Finance, 2:63–68, 1992.
[22] A. Bensoussan. On the theory of option pricing. Acta Appl. Math.,
2:139–158, 1984.
[23] A. Bensoussan and R.J. Elliott. Attainable claims in a Markov model.
Math. Finance, 5:121–132, 1995.
[24] A. Bensoussan and J.L. Lions. Applications of Variational Inequal-
ities in Stochastic Control. North Holland, Amsterdam, New York,
Oxford, 1982.
[25] J.M. Bismut. Martingales, the Malliavin calculus and hypoellipticity
under general H¨ormander’s conditions. Z. Wahrsch. Verw. Gebiete.,
56:469–505, 1981.
[26] F. Black and M. Scholes. The valuation of option contracts and a
test of market efficiency. J. Finance, 27:399–417, 1972.
[27] F. Black and M. Scholes. The pricing of options and corporate lia-
bilities. J. Polit. Econ., 81:637–659, 1973.

BIBLIOGRAPHY
331
[28] N. Bouleau and D. Lamberton. Residual risks and hedging strategies
in Markovian markets. Stochastic Process. Appl., 33:131–150, 1989.
[29] P. Boyle and T. Vorst. Option replication in discrete time with trans-
action costs. J. Finance, 47:271–293, 1992.
[30] P.P. Boyle.
Options: A Monte-Carlo approach.
J. Finan. Econ.,
4:323–338, 1977.
[31] A. Brace and M. Musiela. A multifactor Gauss Markov implemen-
tation of Heath, Jarrow, and Morton.
Math. Finance, 4:259–283,
1994.
[32] M. Brennan, G. Courtadon, and M. Subrahmanyan. Options on the
spot and options on futures. J. Finance, 40:1303–1317, 1985.
[33] M. Brennan and E. Schwartz. The valuation of American put options.
J. Finance, 32:449–462, 1976.
[34] M. Brennan and E. Schwartz. A continuous-time approach to the
pricing of bonds. J. Bank Finance, 3:135–155, 1979.
[35] M. Capinski and E. Kopp.
Measure, Integral and Probability.
Springer, London, 2004.
[36] M. Capinski and T. Zastawniak. Mathematics for Finance. Springer,
London, 2003.
[37] P. Carr, R. Jarrow, and R. Myneni. Alternative characterizations of
American put options. Math. Finance, 2:87–106, 1992.
[38] A.P. Carverhill. When is the short rate Markovian? Math. Finance,
4:305–312, 1994.
[39] P. Cheridito, F. Delbaen, and M. Kupper. Coherent and convex risk
measures for cadlag processes. Preprint, ETH, 2003.
[40] M. Chesney, R. Elliott, and R. Gibson. Analytical solutions for the
pricing of American bond and yield options. Math. Finance, 3:277–
294, 1993.
[41] M. Chesney and R.J. Elliott. Estimating the instantaneous volatility
and covariance of risky assests. Appl. Stochastic Models Data Anal.,
11:51–58, 1995.
[42] M. Chesney, R.J. Elliott, D. Madan, and H. Yang. Diffusion coeffi-
cient estimation and asset pricing when risk premia and sensitivities
are time varying. Math. Finance, 3:85–100, 1993.
[43] M. Chesney and L. Scott. Pricing European currency options: A
comparison of the modified Black-Scholes model and a random vari-
ance model. J. Finan. Quant. Anal., 24:267–284, 1989.

332
BIBLIOGRAPHY
[44] N. Christopeit and M. Musiela. On the existence and characterization
of arbitrage-free measures in contingent claim valuation. Stochastic
Anal. Appl., 12:41–63, 1994.
[45] K-L. Chung.
A Course in Probability Theory.
Academic Press,
Princeton, 2000.
[46] D.B. Colwell and R.J. Elliott. Discontinuous asset prices and nonat-
tainable contingent claims. Math. Finance, 3:295–308, 1993.
[47] D.B. Colwell, R.J. Elliott, and P.E. Kopp. Martingale representation
and hedging policies. Stochastic Process. Appl., 38:335–345, 1991.
[48] Basle Committee. Credit risk modelling: Current practices and appli-
cations. Technical report, Basle Committee on Banking Supervision,
1999.
[49] A. Conze and R. Viswanathan. Path dependent options: The case of
lookback options. J. Finance, 46:1893–1907, 1991.
[50] G. Courtadon. A more accurate finite difference approximation for
the valuation of options. J. Finan. Quant. Anal., 18:697–700, 1982.
[51] J.C. Cox and C.-F. Huang. Optimal consumption and portfolio poli-
cies when asset prices follow a diffusion process. J. Econ. Theory,
49:33–83, 1989.
[52] J.C. Cox, J.E. Ingersoll, and S.A. Ross. Duration and the measure-
ment of basic risk. J. Business, 52:51–61, 1979.
[53] J.C. Cox, J.E. Ingersoll, and S.A. Ross. The relation between forward
prices and futures prices. J. Finan. Econ., 9:321–346, 1981.
[54] J.C. Cox, J.E. Ingersoll, and S.A. Ross. An intertemporal general
equilibrium model of asset prices. Econometrica, 53:363–384, 1985.
[55] J.C. Cox, J.E. Ingersoll, and S.A. Ross. A theory of the term structure
of interest rates. Econometrica, 53:385–407, 1985.
[56] J.C. Cox and S.A. Ross. The pricing of options for jump processes.
Rodney L. White Center Working Paper 2-75, University of Pennsyl-
vania, 1975.
[57] J.C. Cox and S.A. Ross. A survey of some new results in financial
options pricing theory. J. Finance, 31:382–402, 1976.
[58] J.C. Cox and S.A. Ross.
The valuation of options for alternative
stochastic processes. J. Finan. Econ., 3:145–166, 1976.
[59] J.C. Cox, S.A. Ross, and M. Rubinstein. Option pricing: A simplified
approach. J. Finan. Econ., 7:229–263, 1979.

BIBLIOGRAPHY
333
[60] J.C. Cox and M. Rubinstein. A survey of alternative option-pricing
models. In M. Brenner, editor, Option Pricing, Theory and Applica-
tions, pages 3–33. 1983.
[61] J.C. Cox and M. Rubinstein. Options Markets. Prentice-Hall, Engle-
wood Cliffs, N.J., 1985.
[62] N. Cutland, E. Kopp, and W. Willinger. A nonstandard approach to
option pricing. Math. Finance, 1(4):1–38, 1991.
[63] N. Cutland, E. Kopp, and W. Willinger. From discrete to continuous
financial models: New convergence results for option pricing. Math.
Finance, 3:101–124, 1993.
[64] J. Cvitani´c and I. Karatzas. Convex duality in constrained portfolio
optimization. Ann. Appl. Probab., 2:767–818, 1992.
[65] J. Cvitani´c and I. Karatzas. Hedging contingent claims with con-
strained portfolios. Ann. Appl. Probab., 3:652–681, 1993.
[66] J. Cvitani´c and I. Karatzas. Hedging and portfolio optimization un-
der transaction costs: A martingale approach.
Math. Finance, 6,
1996.
[67] J. Cvitani´c and I. Karatzas. Generalized Neyman-Pearson lemma via
convex duality. Bernoulli, 7:79–97, 2001.
[68] R.C. Dalang, A. Morton, and W. Willinger.
Equivalent martin-
gale measures and no-arbitrage in stochastic securities market model.
Stochastics Stochastics Rep., 29:185–201, 1990.
[69] R-A. Dana and M. Jeanblanc.
Financial Markets in Continuous
Time. Springer, Heidelberg, 2003.
[70] M.H.A. Davis and A.R. Norman. Portfolio selection with transaction
costs. Math. Oper. Res., 15:676–713, 1990.
[71] M.H.A. Davis, V.P. Panas, and T. Zariphopoulou. European option
pricing with transaction costs. SIAM J. Control Optim., 31:470–493,
1993.
[72] F. Delbaen. Representing martingale measures when asset prices are
continuous and bounded. Math. Finance, 2:107–130, 1992.
[73] F. Delbaen. Consols in CIR model. Math. Finance, 3:125–134, 1993.
[74] F. Delbaen. Coherent risk measures. Lecture notes, Scuola Normale
Superiore di Pisa, 2000.
[75] F. Delbaen. Coherent risk measures on general probability spaces.
Preprint, ETH, 2000.

334
BIBLIOGRAPHY
[76] F. Delbaen and W. Schachermayer. A general version of the funda-
mental theorem of asset pricing. Math. Ann., 300:463–520, 1994.
[77] F. Delbaen and W. Schachermayer. The no-arbitrage property un-
der a change of numeraire. Stochastics Stochastics Rep., 53:213–226,
1995.
[78] F. Delbaen and W. Schachermayer. The Banach space of workable
contingent claims in arbitrage theory. Ann. Inst. H. Poincar´e Probab.
Statist., 33:113–144, 1997.
[79] F. Delbaen and W. Schachermayer.
A compactness principle for
bounded sequences of martingales with applications. Prog. Probab.,
45:137–173, 1999.
[80] C. Dellacherie and P.-A. Meyer. Probabilities and Potential A. North-
Holland, Amsterdam, 1975.
[81] C. Dellacherie and P.-A. Meyer. Probabilities and Potential B. North-
Holland, Amsterdam, 1982.
[82] L.U. Dothan.
On the term structure of interest rates.
J. Finan.
Econ., 6:59–69, 1978.
[83] L.U. Dothan. Prices in Financial Markets. Oxford University Press,
New York, 1990.
[84] L.U. Dothan and D. Feldman. Equilibrium interest rates and multi-
period bonds in a partially observable economy. J. Finance, 41:369–
382, 1986.
[85] R. Douady. Options ´a limite et options ´a limite double. Working
paper, 1994.
[86] J.-C. Duan.
The GARCH option pricing model.
Math. Finance,
5:13–32, 1995.
[87] D. Duffie. An extension of the Black-Scholes model of security valu-
ation. J. Econ. Theory, 46:194–204, 1988.
[88] D. Duffie.
Security Markets: Stochastic Models.
Academic Press,
Boston, 1988.
[89] D. Duffie. Futures Markets. Prentice-Hall, Englewood Cliffs, N.J.,
1989.
[90] D. Duffie.
Dynamic Asset Pricing Theory.
Princeton University
Press, Princeton, N.J., 1992.
[91] D. Duffie and C. Huang. Multiperiod security markets with differen-
tial information. J. Math. Econ., 15:283–303, 1986.

BIBLIOGRAPHY
335
[92] D. Duffie and C.-F. Huang.
Implementing Arrow-Debreu equilib-
ria by continuous trading of few long-lived securities. Econometrica,
53:1337–1356, 1985.
[93] D. Duffie and R. Kan. Multi-factor term structure models. Philos.
Trans. R. Soc. London, 347:577–586, 1994.
[94] D. Duffie and P. Protter. From discrete- to continuous-time finance:
Weak convergence of the financial gain process. Math. Finance, 2:1–
15, 1992.
[95] D. Duffie and H.P. Richardson. Mean-variance hedging in continuous
time. Ann. Appl. Probab., 1:1–15, 1991.
[96] D. Duffie, M. Schroder, and C. Skiadas.
Recursive valuation of
defaultable securities and the timing of resolution of uncertainty.
Ann.Appl. Prob., 6:1075–1090, 1996.
[97] N. Dunford and J.T. Schwartz.
Linear Operators, Part I.
Inter-
science, New York, 1956.
[98] E. Eberlein.
On modeling questions in security valuation.
Math.
Finance, 2:17–32, 1992.
[99] N. El Karoui. Les aspects probabilistes du contrˆole stochastique. In
Lecture Notes in Mathematics, volume 876, pages 73–238. Springer,
Berlin, 1981.
[100] N. El Karoui and H. Geman. A probabilistic approach to the valua-
tion of floating rate notes with an application to interest rate swaps.
Adv. Options Futures Res., 7:47–63, 1994.
[101] N. El Karoui, H. Geman, and V. Lacoste. On the role of state vari-
ables in interest rate models. Working paper, 1995.
[102] N. El-Karoui, H. Geman, and J.C. Rochet. Changes of numeraire,
arbitrage and option prices. J. Appl. Probab., 32:443–458, 1995.
[103] N. El Karoui, M. Jeanblanc-Picqu´e, and S. Shreve. Robustness of
the Black and Scholes formula. Math. Finance, 8, 1998.
[104] N. El Karoui and I. Karatzas.
A new approach to the Skorohod
problem and its applications. Stochastics Stochastics Rep., 34:57–82,
1991.
[105] N. El Karoui, S. Peng, and M.C. Quenez. Backward stochastic differ-
ential equations in finance. Preprint 260, Universit´e Paris VI, 1994.
[106] N. El Karoui and M.C. Quenez. Dynamic programming and pricing of
contingent claims in an incomplete market. SIAM J. Control Optim.,
33:29–66, 1995.

336
BIBLIOGRAPHY
[107] N. El Karoui and J.C. Rochet.
A pricing formula for options on
coupon bonds.
In Modeles Mathematiques de la finance. INRIA,
Paris, 1990.
[108] N. El Karoui and D. Saada.
A review of the Ho and Lee model.
International Conference in Finance, June 1992.
[109] R.J. Elliott. Stochastic Calculus and Applications. Springer-Verlag,
Berlin, 1982.
[110] R.J. Elliott, L. Aggoun, and J.B. Moore. Hidden Markov Models:
Estimation and Control. Applications of Mathematics 29. Springer-
Verlag, New York, 1994.
[111] R.J. Elliott and M. Chesney. Estimating the volatility of an exchange
rate. In J. Janssen and C. Skiadis, editors, 6th International Sympo-
sium on Applied Stochastic Models and Data Analysis, pages 131–135.
World Scientific, Singapore, 1993.
[112] R.J. Elliott and D.B. Colwell. Martingale representation and non-
attainable contingent claims. In P. Kall, editor, 15th IFIP Confer-
ence, Lecture Notes in Control & Information Sciences 180, pages
833–842. Springer, Berlin, 1992.
[113] R.J. Elliott and H. F¨ollmer. Orthogonal martingale representation.
In Liber Amicorum for M. Zakai. Academic Press, New York.
[114] R.J. Elliott, H. Geman, and R. Korkie. Portfolio optimization and
contingent claim pricing with differential information.
Stochastics
Stochastic Rep., 60:185–203, 1997.
[115] R.J. Elliott, H. Geman, and D. Madan. Closed form formulae for
valuing portolios of American options. Working paper.
[116] R.J. Elliott and W.C. Hunter. Filtering a discrete time price pro-
cess.
In 29th IEEE Asilomar Conference on Signals Systems and
Computers, Asilomar, CA. November 1995, pages 1305–1309. IEEE
Computer Society Press, Los Alamos, 1996.
[117] R.J. Elliott, W.C. Hunter, and B.M. Jamieson. Drift and volatility
estimation in discrete time.
J. Econ. Dynamics and Control, 22,
1998), PAGES= 209-218.
[118] R.J. Elliott, W.C. Hunter, and B.M. Jamieson. Financial signal pro-
cessing. Int. J. Theor. Appl. Finance, 4:561–584, 2001.
[119] R.J. Elliott, W.C. Hunter, P.E. Kopp, and D.B. Madan. Pricing via
multiplicative price decomposition. J. Finan. Eng., 4:247–262, 1995.
[120] R.J. Elliott and P.E. Kopp. Option pricing and hedge portfolios for
Poisson processes. J. Stochastic Anal. Appl., 8:157–167, 1990.

