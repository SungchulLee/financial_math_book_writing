# Interest Rate Models

!!! info "Source"
    **Financial Mathematics: An Introduction to Derivatives Pricing** by Lane P. Hughston and Christopher J. Hunter, King's College London, 2000.
    These notes are used for educational purposes.

## Interest Rate Models

2. We want to calculate the dealer’s payofffor the hedged bet. The payoffis δU −ft(U)
dollars, where
δ = ft(U) −ft(D)
U −D
(C.14)
and hence the payoffis
ft(U) −ft(D)
U −D
U −ft(U) = Dft(U) −Uft(D)
U −D
(C.15)
dollars.
3. Suppose that a derivative has payofffunction ft(St), and that the dealer makes a
price of g0dollars, which is assumed to be less than the arbitrage price of f0 dollars.
Consider an arbitrageur that starts with empty pockets and borrows g0−δS0 dollars
interest-free from the Casino, where δ is the hedge ratio given by equation (3.7),
δ = ft(U) −ft(D)
U −D
.
The arbitrageur then buys the derivative from the dealer at price g0, and makes a
short bet with the casino, in the quantity δS0, i.e. the Casino pays the arbitrageur
δS0 at t = 0, and the arbitrageur must pay the Casino δS1 at time t.
Thus, at time t the arbitrageur gets the certain amount ft(St)−δSt dollars, in other
words, he gets ft(St) dollars from dealer, but has to pay δSt dollars to the Casino.
However, the loan of g0 −δS0 dollars must also be repaid. Thus the arbitrageur is
left with
ft(St) −δSt −(g0 −δS0)
dollars. But, recall that f0 = ft(St) −δSt + δS0. So the arbitrageur is left with
f0 −g0 dollars, which is, by assumption, positive. Thus a sure profit with no risk
has been made! Similarly if we took g0 > f0, then the arbitrageur could make a
profit by taking a short hedged position. You should work out the details of this
case as well.
Section 4
1. Let Ωbe a sample space. We want to show that the power set P(Ω), which is the
set of all subsets of Ω, is a valid event space. Since Ωis a subset of itself, Ω∈P(Ω).
If A, B ∈P(Ω), then they are subsets of Ω, that is A, B ⊂Ω. But then A ∪B ⊂Ω,
so A ∪B ∈P(Ω). Finally if A ∈P(Ω), then A ⊂Ω, and since the complement of
A in Ωis simply the set of elements of Ωthat are not in A, Ω−A ⊂Ω. Hence
Ω−A ∈P(Ω). Thus the power set is a valid event space.
We now want to write out the power set for a ‘possibility system’ that is based on
the outcome of two coin tosses. Denoting ‘heads’ by H and ‘tails’ by T, the sample
space can be written as {HH, HT, TT, TH}.
The power set will have 24 = 16
elements and is as follows:
Σ
=
n
∅,
{HH}, {HT}, {TT}, {TH},
{HH, HT}, {HH, TT}, {HH, TH}, {HT, TT}, {HT, TH}, {TT, TH},
{HH, HT, TT}, {HH, HT, TH}, {HH, TT, TH}, {HT, TT, TH},
{HH, HT, TT, TH}
o
.
150

2. We want to prove that given a sample space Ω, the set Σ = {∅, Ω} is a valid event
space. By definition, Σ satisfies Ω∈Σ. Since Ω∪∅= Ω, and these are the only two
elements in Σ, we see that Σ is closed under the union of its elements. Furthermore,
since Ω−∅= Ωand Ω−Ω= ∅, we see that Σ is closed under complementation of its
elements. Hence Σ = {∅, Ω} is a valid event space. However, it is not very useful,
as the only events that it can differentiate between are whether the experiment had
an outcome or not.
3. We want to show for a possibility system based on a finite sample space Ωand
an event space Σ equal to the power set of Ω, that any probability measure P is
uniquely defined by its values on the single element sets of the event space, that
is, on the ‘probabilities’ of the sample space. Let Ω= {ωi}N
i=1, and let A be any
element of Σ. But then A is simply a subset of Ω, and hence A = {ωik}M
k=1 for
some sequence ik. We can then use the property that the probability of the union
of disjoint sets is equal to the sum of the individual probabilities, that is,
P(A)
=
P
¡
{ωik}M
k=1
¢
=
M
X
k=1
P ({ωik})
=
M
X
k=1
pik.
(C.16)
Thus we see that the probability of any set is simply the sum of the ‘probabilities’
of its individual elements.
4. We want to calculate the probability, in the the possibility system (Ω, Σ) based on
three coin tosses, that there are exactly two heads. This event is A = {HHT, HTH, THH}.
We have two probability systems in which to calculate the probability of A. Sup-
pose that we are in the ‘equal probability’ system (Ω, Σ, P). The probability of A
is
P({HHT, HTH, THH})
=
P({HHT}) + P({HTH}) + P({THH})
=
3
8.
(C.17)
In the ‘weighted coin’ probability system (Ω, Σ, Q) we have
Q({HHT, HTH, THH})
=
Q({HHT}) + Q({HTH}) + Q({THH})
=
2
9.
(C.18)
5. We want to calculate the expectation of the random variable X that returns the
number of ‘heads’ in three coin tosses for both the ‘equal probability’ and ‘weighted
coin’ probability measures P and Q. The values of X were written out in equation
(4.4). For the probability measure P, the expectation is
EP [X]
=
1
8X({HHH}) + 1
8X({HHT}) + 1
8X({HTH}) + 1
8X({THH}) +
151

1
8X({HTT}) + 1
8X({TTH}) + 1
8X({THT}) + 1
8X({TTT}
=
1
8 [3 + 2 + 2 + 2 + 1 + 1 + 1 + 0]
=
1.5,
(C.19)
while for the measure Q, we have
EQ[X]
=
1
27X({HHH}) + 2
27X({HHT}) + 2
27X({HTH}) + 2
27X({THH}) +
4
27X({HTT}) + 4
27X({TTH}) + 4
27X({THT}) + 8
27X({TTT}
=
1
27 [3 + 2(2 + 2 + 2) + 4(1 + 1 + 1) + 0]
=
1.
(C.20)
Let Y be the random variable which is equal to twice the number of ‘heads’ minus
the number of ‘tails’. To simplify the calculation, let W be the random variable
equal to the number of ‘tails’. Then Y = 2(X −W). But, X + W = 3, so we see
that
Y
=
2[X −(3 −X)]
=
4X −6.
(C.21)
Using the result above for the expectation of X, we can calculate the expectation
of Y , first in the probability measure P
EP [Y ]
=
EP [4X −6]
=
4EP [X] −6
=
0,
(C.22)
and next in the measure Q,
EQ[Y ]
=
4EQ[X] −6
=
−2.
(C.23)
Let Z be the random variable defined by
Z({ABC}) =
n
1
ABC = HHH
0
otherwise
.
In the ‘equal probability’ measure P the expectation is
EP [Z]
=
P({HHH})Z({HHH})
=
1
8,
(C.24)
while in the ‘weighted coin’ measure Q
EQ[Z]
=
Q({HHH})Z({HHH})
=
1
27.
(C.25)
152

Section 5
1. P0t be a decreasing function of t because ...
2. We want to show that if the dealer misprices a derivative and sells it for g0 dollars,
which is less than the arbitrage value of f0 dollars, then an arbitrageur can make a
sure profit. Suppose that the arbitrageur starts with nothing. Since the derivative
is priced too low, he will buy it from the dealer for the price of g0 dollars and then
hedge this derivative position by making a short bet with the Casino in the amount
of δS0 dollars, where δ is the hedge ratio (5.8). In order to fund this position,
the arbitrageur must borrow g0 −δS0 dollars from the bank at an interest rate
r.
Note that if g0 −δS0 is negative then the arbitrageur is actually depositing
money in the bank.
At time t, the arbitrageur receives ft(St) dollars from the
dealer for the derivative and has to pay δSt dollars to the Casino in order to cover
his short bet. Furthermore, the loan, which is now worth (g0 −δS0)ert dollars,
must be repaid to the bank. Hence the net position of the arbitrageur after the
coin toss is ft(St) −δSt −(g0 −δS0)ert dollars. From equation (5.9) we see that
f0ert = ft(St) −δSt + δS0ert, and hence the arbitrageur’s position is worth the
guaranteed amount of
ft(St) −δSt −(g0 −δS0)ert = (f0 −g0)ert
(C.26)
dollars. Since f0 > g0 the arbitrageur has made a sure profit, starting from nothing.
If the derivative were over-priced, so g0 > f0, then the arbitrageur could construct
a gambling portfolio which is short a derivative and long δ units of the basic bet to
guarantee a profit.
3. Suppose that the basic bet in the Casino is $100 and that it pays off$105 and $95
for heads and tails respectively, while the continuously compounded interest rate is
rt = log 1.01.
(a) We want to calculate the risk-neutral probabilities. They are given by equa-
tion ??. Substituting in the values for S0, U, D and ert, we have
p∗
=
(100)(1.01) −95
105 −95
=
0.6,
(C.27)
and hence q∗= 1 −p∗= 0.4.
(b) We now want to price a call option with a strike of $100. The payofffunction
ft(St) for this derivative, is
ft(U) = $5
and
ft(D) = $0.
Using the risk-neutral probabilities calculated above, and the pricing formula
f0 = e−rtE∗[ft(St)], we see that the cost of the derivative is
f0
=
1
1.01 [(0.6)5 + (0.4)0]
=
2.97
(C.28)
dollars.
153

(c) The hedge ratio is given by equation (3.7). Substituting in the relevant values
yields
δ
=
5 −0
105 −95
=
0.5.
(C.29)
(d) We want to verify that the payoffof a bet that is long δ units of the basic bet
and short one derivative is independent of the outcome of the coin toss. At
time t the value of this hedged bet is δSt −ft(St). If the coin toss is heads,
then the payoffis
δU −ft(U)
=
(0.5)105 −5
=
47.50
(C.30)
dollars, while if the coin flip is tails, then the result is
δD −ft(D)
=
(0.5)95 −0
=
47.50
(C.31)
dollars. Thus the payofffrom the hedged bet is $47.50 and is independent of
the outcome of the coin toss.
(e) The cost of the derivative is independent of the ‘physical’ coin toss probabil-
ties, p and q, and depends only on the risk-neutral probabilities p∗and q∗.
Hence even if we change the physical probabilities the cost of the derivative
is still $2.97.
4. We want to show that the risk-neutral probabilities p∗and q∗are uniquely defined by
the requirement that S0 = e−rtE∗[St]. Suppose that we have different probabilities
˜p and ˜q that define a probability measure ˜P such that S0 = e−rt ˜E[St]. Then
S0
=
e−rt[˜pU + ˜qD]
=
e−rt[˜p(U −D) + D].
(C.32)
Solving for ˜p, we obtain
˜p = S0ert −D
U −D
.
(C.33)
But, this is simply p∗! Hence, the condition S0 = e−rt ˜E[St] uniquely determines
the risk-neutral probabilities.
Section 6
1. We want to calculate various probabilities for the numeric example illustrated in
(6.12).
The probability that S2 = 102 is simply the probability that we have
an initial ‘up’ movement times the probability that this is followed by a ‘down’
movement, that is p0ˆp01.
Substituting in the numbers yields 0.5 × 0.3 = 0.15.
We can calculate the probability that S2 > 95 by noting that it is one minus the
probability that S2 ≤95, which is equal to the probability that S = 92. This is the
probability of having two ‘down’ movements, which is given by 0.5 × 0.3 = 0.15.
Hence the probability of S2 being greater than 95 is 1 −0.15 = 0.85.
154

2. We want to calculate the annualised continuously compounded interest rate r for
the bond process $100 →$101 →$102.01, where each time step is one month. At
t = 1/12, that is, after one month, a continuously compounded investment of $100
will be worth $100er/12. Equating this to the value of the bond process after one
month B1 = $101, we see that
100er/12
=
101
r/12
=
log 1.01
r
=
0.1194,
(C.34)
thus the interest rate is 11.94% per year.
3. Using the numeric stock and bond processes given in (6.12) and (6.13), we want to
calculate the price of two call options which have maturity at time 1 and strikes of
$98 and $102 respectively. Before we can calculate any prices however, we need to
determine the risk-neutral probabilities. Fortunately we have already done this—in
exercise 5.3 we considered an identical system, albeit with only one-period, and
obtained the risk neutral probabilities p0
∗= 0.6 and p1
∗= 0.4. We can then price
any derivative by using the discounted expectation of the payoffin the risk-neutral
probability system,
f0
=
E∗[f1]B0/B1
=
p0
∗f 0 + p1
∗f 1
B1/B0
=
0.6f 0 + 0.4f 1
1.01
.
(C.35)
For the call with a strike of $102, the payoffin the event of an ‘up’ movement is
f 0 = $105 −$102 = $3, while for a ‘down’ movement f 1 = $0. Subsituting this
payofffunction into the pricing formula (C.35) we obtain f0 = $3×0.6/1.01 = $1.78.
If the strike is $98 then the payofffunction is f 0 = $7 and f 1 = $0. Calculating
the initial price of the derivative we find that it is $4.16.
We want to calculate the value of the call options again, but this time we are buying
them at time 1 with a maturity of time 2. Because there are two possible initial
prices at time 1, S0 and S1, we will need to calculate derivative prices for both cases.
Begin by assuming that the first stock movement was ‘up’, so that S1 = $105. But
then the time step from t = 1 to t = 2 is a simple binomial tree, with an ‘up’ price
of $108, and a ‘down’ price of $102. We can therefore calculate the risk-neutral
probabilities using equation (5.11), and find that
ˆp00
∗
=
S0B2/B1 −S01
S0 −S1
=
105 × 1.01 −102
108 −102
=
0.675,
(C.36)
and
ˆp00
∗
=
S00 −S0B2/B1
S0 −S1
155

=
108 −105 × 1.01
108 −102
=
0.325.
(C.37)
We can now calculate the initial price f 0 of a derivative by using the discounted
expectation of the payoffin the risk-neutral system,
f 0
=
ˆp00
∗f 00 + ˆp01
∗f 01
B2/B1
=
0.675f 0 + 0.325f 1
1.01
.
(C.38)
Recall that this formula assumes that the share price at time 1 is S0. If the share
price is S1 instead, then we will get a different formula. For the call option with
a strike of $102, the payofffunction is f 00 = $6 and f 01 = $0. We can substitute
this into equation (C.38) to obtain a derivative price of $4.01. For the call with a
strike of $98, the payofffunction is f 00 = $10 and f 01 = $4. This yields an initial
price of $7.97.
An identical calculation can be carried out for the case when S1 = 95. In this
case, the risk neutral probabilities are ˆp10
∗= 0.658 and ˆp11
∗= 0.342. However, the
payofffunctions for both call options are identically zero, and hence without further
calculation we see that their initial prices will be zero.
We now want to price the call options at time 0 when they have a maturity at time
2. This is equivalent to finding the value at time 0 of a derivative which pays offf i
at time 1. Why? Because we can think of the following two investment strategies:
(a) buy a call option at time 0 which pays offat time 2 and (b) buy a derivative at
time 0 which pays f1 at time 1, and then use the proceeds of this payoffto buy a
call option which pays offat time 2. Since both strategies have the same payoffthey
must have the same initial price, otherwise we could arbitrage by going long the
cheaper strategy and shorting the more expensive one. By substituting the values
calculated above for f 0 and f 1 into the pricing formula (C.35) we can obtain the
initial price of strategy (b), and hence of strategy (a) and the call option that we
are interested in pricing. The price of the call option with strike $102 is
f
=
0.6f 0 + 0.4f 1
1.01
=
0.6 × $4.01 + 0.4 × $0
1.01
=
$2.38.
(C.39)
For the call option with a strike of 98, we can substitute in the derivative values
f 0 = $7.97 and f 1 = $0 to find the initial price of $4.73.
4. We want to compare the Casino price equation (5.13),
f0 = e−rt
µS0ert −D
U −D
ft(U) + U −S0ert
U −D
ft(D)
¶
,
(C.40)
156

with the one-period derivative price of equation (6.21). If we make the substitutions
ert →B1/B, U →S0, D →S1, ft(U) →f 0 and ft(D) →f 1 in the Casino price
equation, then we obtain
f = B
B1
"
S B1
B −S1
S0 −S1 f 0 + S0 −S B1
B
S0 −S1 f 1
#
,
(C.41)
which is exactly the one-period result. Hence the Casino and the binomial tree
model price derivatives in the same way.
5. We want to verify that the ‘probabilities’ introduced in equation (6.22),
p0
∗=
˜S −S1
S0 −S1
and
p1
∗= S0 −˜S
S0 −S1 ,
(C.42)
where ˜S = SB1/B, generate a valid probability measure. We first note that
p0
∗+ p1
∗= 1.
(C.43)
We then need to show that the probabilities are both positive. We can do this by
applying an arbitrage argument to the values of ˜S, S0 and S1. By assumption we
take S1 < S0. Suppose that ˜S ≤S1. We can then form an arbitrage strategy by
starting with nothing, and then going long on stocks and shorting the bonds. The
initial holding of the portfolio is αS −B, where α = B/S so that the net value of
the investment is zero. At time 1 the position is worth αS1 −B1. The minimum
value of this random amount occurs when S1 = S1. We then see that
αS1 −B1
≥
αS1 −B1
≥
α(S1 −B1/α)
≥
α(S1 −˜S)
(C.44)
But, since S1 ≥˜S, we can never lose money by investing this way, and we will
make some whenever S1 = S0. Hence there is an arbitrage opportunity and to
avoid it we must have S1 < ˜S. This tells us that p0
∗> 0. A similar argument can
be used to demonstrate that S0 > ˜S, and hence that p1
∗> 0. Thus the risk-neutral
probabilities do, in fact, constitute a geunine probability measure.
6. We want to find the forward price at time 0 for the purchase of one share at time
1. We can do this by considering a forward contract, which is an agreement made
at time 0 to purchase a unit of stock for a fixed price K. This is a derivative which
pays offf1 = S1 −K (which may be negative) at time 1. The price of the forward
contract is
f0
=
B
B1
£
p0
∗(S0 −K) + p1
∗(S1 −K)
¤
=
B
B1
[p0
∗S0 + p1
∗S1] −[p0
∗+ p1
∗] B
B1
K
=
B
B1
E∗[S1] −B
B1
K
(C.45)
157

But, by definition of the risk-neutral probability, the first term is simply the price
of a derivative which pays offthe stock value at t = 1, which is therefore the initial
price of the stock. Hence
f0 = S0 −B
B1
K.
(C.46)
This is the price of a forward contract to buy a unit of stock at time 1 for the fixed
price K. The forward price of the stock F, is the value of K such that the cost of
the contract is zero. Thus,
F = S0
B1
B .
(C.47)
The correct forward price can also be obtained by an arbitrage argument. Suppose
that an investor agrees at time 0 to purchase a stock at time t from a dealer for the
price ˜St. The dealer immediately buys a share at the going rate S0, using money
borrowed at a continuously compounded rate r. At time t, the dealer receives ˜St
for the share, and uses it to repay the loan of S0ert. The dealer’s net position is
therefore ˜St −S0ert, and because he started with nothing this must be zero. Hence
˜St = S0ert.
Section 7
1. In a two-period market, we want to show that if S1 = S0
1, then the value of the
derivative at t = 1 must be f 0 as given in equation (7.2),
f 0
B1
= f 00p00
∗+ f 01p01
∗
B2
,
where
p00
∗=
˜S0
12 −S01
S00 −S01 ,
p01
∗= 1 −p00∗, and ˜S0
12 = S0 B2
B1 (the forward price, made at time 1, for delivery at
time 2, if at time 1 the stock is in the S0 state).
We do this by constructing a replicating portfolio, just as we did in the one-period
case. At t = 1, the dealer sells an investor a derivative which will pay out either f 00
or f 01 at time 2. The proceeds f 0 from this sale are used to construct a hedging
portfolio in the stock and bond markets. The dealer buys β1 bonds at a price of B1
each and δ1 shares at a price of S0 each. Since the dealer’s initial position is zero,
we have
f 0 = β1B1 + δ1S0
1.
(C.48)
At the next period we want the stock and bond investments to exactly replicate
the derivative payoff, so
f 0i = β1B2 + δ1S0i
2 .
(C.49)
Solving these two equations for β1 and δ1 we get
δ1 = f 00 −f 01
S00
2 −S01
2
and
β1 = f 01S00
2 −f 00S01
2
B2(S00
2 −S01
2 ) .
(C.50)
158

Plugging the values back into (C.48) we get
f 0
B1
= 1
B2
"
S0
1
B2
B1 −S01
2
S00
2 −S01
2
f 00 +
S00
2 −S0
1
B2
B1
S00
2 −S01
2
f 01
#
,
which is the required result.
Note, incidentally, that β1 and δ1 are the ‘new’ hedge ratios that the dealer puts
on at t = 1. Strictly speaking, we should write β0
1, δ0
1 to indicate that these are the
hedge ratios at t = 1 for the S0 state (in the S1 state, we would put on a different
hedge).
2. We want to show that the probability system generated by pi
∗and pij
∗satisfies the
relations (7.8),
B1
B0
= E∗[S1]
S0
and
B2
B0
= E∗[S2]
S0
.
(C.51)
The first equality is easy to verify,
E∗[S1]
=
p0
∗S0 + p1
∗S1
=
˜S −S1
S0 −S1 S0 −S0 −˜S
S0 −S1 S1
=
˜S
=
S0 B1
B0
.
(C.52)
In the two-period case, we have
E∗[S2] = p0
∗ˆp00
∗S00
2 + p0
∗ˆp01
∗S01
2 + p1
∗ˆp10
∗S10
2 + p1
∗ˆp11
∗S11
2 .
(C.53)
Now consider the first two terms,
ˆp00
∗S00
2 + ˆp01
∗S01
2
=
˜S0
12 −S01
2
S00
2 −S01
2
S00
2 + S00
2 −˜S0
12
S00
2 −S01
2
S01
2
=
˜S0
12,
(C.54)
where ˜S0
12 = S0 B2
B1 . A similar relation holds for the next two terms,
ˆp10
∗S10
2 + ˆp11
∗S11
2 = ˜S1
12,
(C.55)
where ˜S1
12 = S1B2/B1. Hence we see that
E∗[S2]
=
[p0
∗S0 + p1
∗S1]B2
B1
=
·
S0 B1
B0
¸ B2
B1
=
S0 B2
B0
,
(C.56)
159

where the second line follows from the previous argument.
Do these two conditions uniquely define a probability measure? Consider the fol-
lowing two stock price processes:
100 ©©©©
* 150
.5
HHHH
j 50
.5
©©©©
* 200
.5
HHHH
j 100
.5
©©©©
* 75
.5
HHHH
j 25
.5
(C.57)
and
100 ©©©©
* 150
.5
HHHH
j 50
.5
©©©©
* 600
.1
HHHH
j 100
.9
©©©©
* 75
.5
HHHH
j 25
.5
(C.58)
Set the interest rate to zero. Then both these processes satisfy the relations (7.8),
and hence they do not uniquely define a probability measure.
3. In order to calculate the risk-neutral probabilities, we need the discounted stock
prices,
˜S0
12
=
S0 B2
B1
= 106.05
˜S1
12
=
S1 B2
B1
= 95.95
˜S01
=
S B1
B0
= 101
We can then calculate the probabilities
p00
∗=
˜S0
12 −S01
S00 −S01 = .675,
160

100 ©©©©
* 105
.6
HHHH
j 95
.4
©©©©
* 108
.675
HHHH
j 102
.325
©©©©
* 98
.658
HHHH
j 92
.342
Figure C.3:
The two-period Stock Market with risk-neutral probabilities.
etc., which gives the risk-neutral tree shown in figure C.3. Using this system, it is
easy to calculate the price of any derivative from the formula
f = B
B2
E∗[f2]
We consider each of the derivatives in turn, expressing the payoffas a vector of the
form (f 00, f 01, f 10, f 11)
(a) If f ij = Sij, then the payoffvector is (108,102,98,92), and hence the derivative
price is
f =
100
102.01[.6(.675 × 108 + .325 × 102) + .4(.6583 × 98 + .3416 × 92)] = 100,
as expected.
(b) If we take a future contract with a strike of 100, then the payoffis (8,2,-2,-8),
and the price is 1.97.
(c) The European call option has payoff(8,2,0,0) and costs 3.29.
(d) The put option pays out (0,0,2,8) and has price 1.58.
(e) In order to calculate the value of the call option, f, we need to know the
value of the future at t = 1, ˜f1. We can calculate this using the martingale
property
˜f1 = B1
B2
E∗
1[ ˜f2]
which yields ˜f 0 = 5.99 and ˜f 1 = −4.01. Since the strike price is 3, the payoff
vector is (f 0, f 1) = (2.99, 0). Hence, calculating the value of the option, we
get 1.78.
(f) The derivative has payoff(0,0,2,7), and hence has price 1.45.
(g) The digital payoffis (10,10,0,0), and thus the value is 5.88.
161

(h) A European call option has payout (4,0,0,0), and hence a price of 1.59. For the
American option, we can price it by assuming that the investor always makes
the best move possible. Thus, the payoffvector is (4,1.01,0,0), corresponding
to exercising the option at t = 2, and t = 1 for the first two cases. Note
that if the option is exercised at t = 1, then the payoffcan be invested in the
money market account, and hence is worth 1.01, not 1 at t = 2. Using this
payofffunction, the American option is valued at 1.78.
4. We want to calculate the risk-neutral probabilities for a three-period model. First
of all let us define the forward prices that we are going to use:
˜S01 = B1
B0
S
˜Si
12 = B2
B1
Si
and
˜Sij
23 = B3
B2
Sij.
(C.59)
The probabilities at the first time step are
p0
∗=
˜S01 −S1
S0 −S1
and
p1
∗= S0 −˜S01
S0 −S1 .
(C.60)
At the second time setp,
ˆpi0
∗=
˜Si
12 −Si1
Si0 −Si1
and
pi1
∗= Si0 −˜Si
12
Si0 −Si1 .
(C.61)
At the third time step
ˆpij0
∗
=
˜Sij
23 −Sij1
Sij0 −Sij1
and
pij1
∗
= Sij0 −˜Sij
23
Sij0 −Sij1 .
(C.62)
5. Suppose that at time 2 we are at a node Sij. Then by the one period approach we
obtain the price of the derivative at the node as
f ij = B2
B3
(ˆpij0
∗f ij0 + ˆpij1
∗f ij1)
(C.63)
Multiply by pij
∗to remove the conditional probabilities from the right hand side,
pij
∗f ij = B2
B3
(pij0
∗f ij0 + pij1
∗f ij1)
(C.64)
Sum over all possible values of i and j. This is simply taking the expectation of
both sides,
E∗[f2] = B2
B3
E∗[f3].
(C.65)
We can then use our two-period result to write
f0 = B0
B3
E∗[f3].
(C.66)
162

6. Consider the stock process at time N −1.
We can write an arbitrary node as
Si1···iN−1, which will move to either Si1···iN−10 or Si1···iN−11. The bond process will
move from BN−1 to BN. The derivative will pay either f i1···iN−10 or f i1···iN−11.
Using the standard one-period argument, we find that the value of the derivative
at time N −1 is
f i1···iN−1 BN
BN−1
= ˆpi1···iN−10f 11···iN−10 + ˆpi1···iN−11f 11···iN−11
(C.67)
Multiply through by pi1···iN−1
∗
,
pi1···iN−1
∗
f i1···iN−1 BN
BN−1
= pi1···iN−1
∗
ˆpi1···iN−10f 11···iN−10+pi1···iN−1
∗
ˆpi1···iN−11f 11···iN−11.
(C.68)
But we can convert the conditional probabilities on the rigth hand side into uncon-
ditional probabilities
pi1···iN−1
∗
f i1···iN−1 BN
BN−1
= pi1···iN−10f 11···iN−10 + pi1···iN−11f 11···iN−11.
(C.69)
We then want to sum over all the possible values of i1 · · · iN−1. This is equivalent
to taking expectations of both sides,
E∗[fN−1] BN
BN−1
= E∗[fN].
(C.70)
By the induction hypothesis,
f0 = E∗[fN−1] B0
BN−1
(C.71)
and hence
f0 = E∗[fN] B0
BN
(C.72)
as desired.
Section 8
1. Working in a filtered probability system (Ω, Σ, P, F), we want to verify that the
stochastic process
Ym(ωi) = E[Sn|F (m)
k
],
(C.73)
where F (m)
k
is the unique element of the filtration at time m that contains ωi, is
adapted to the filtration F. Note that we are being slightly more general by using
Sn in the definition of Ym instead of S2. Recall that a process Y is adapted, if
at every time step m, Ym has the same value for all the elements that are in the
same set F (m)
k
of the partition of the sample space that is defined by the filtration
element Fm. So suppose ωi and ωj are both elements of F (m)
k
. Then by definiton,
Ym(ωi) = E[Sn|F (m)
k
]
and
Ym(ωj) = E[Sn|F (m)
k
],
(C.74)
and hence Y is adapted to the filtration F.
163

2. We want to verify that the martingale condition
Sm
Bm
= E∗
· Sn
Bn
¸
(C.75)
holds for the three period binomial model. Since the expectation is with respect to
the risk-neutral measure we need to calculate the relevant probabilities ˆpi
∗, ˆpij
∗and
ˆpijk
∗. Fortunately we have already done this in exercise 7.4. We begin by verifying
the result for adjacent time steps. At the first time step we have
E0
· S1
B1
¸
=
E
· S1
B1
|F0
¸
=
ˆp0S0 + ˆp1S1
B1
=
( ˜S −S1)S0 + (S0 −˜S)S1
B1(S0 −S1)
=
˜S
B1
=
S
B0
.
(C.76)
Between the first and second time steps,
E1
· S2
B2
¸
=
E
· S2
B2
|F i
¸
=
ˆpi0Si0 + ˆpi1Si1
B2
=
( ˜Si −Si1)Si0 + (Si0 −˜Si)Si1
B2(Si0 −Si1)
=
˜Si
B2
=
Si
B1
.
(C.77)
Finally, consider when we move from the second to third node,
E2
· S3
B3
¸
=
E
· S3
B3
|F ij
¸
=
ˆpij0Sij0 + ˆpij1Sij1
B3
=
( ˜Sij −Sij1)Sij0 + (Sij0 −˜Sij)Sij1
B3(Sij0 −Sij1)
=
˜Sij
B3
=
Sij
B2
.
(C.78)
164

We can verify the other cases by using a very important result:
Ei[Xn] = Ei[Ej[Xn]].
(C.79)
This is known as the tower law of conditional expectation. Rather than prove it,
we will verify it for a specific example. Consider the random variable E1[S3], which
is the expected value of the share price at time 3, given that we have information
about what happened at time 1. Evaluate it at a particular element of the sample
space, say UDU,
E1\[S3\](UDU)
=
E[S3|F 0]
=
P(UUU|F 0)S000 + P(UUD|F 0)S001
+P(UDU|F 0)S010P(UDD|F 0)S011.
(C.80)
Now consider the random variable E1[E2[S3]]. We want to evaluate it at the same
point and verify that we get the same result as above. Hence
E1\[E2\[S3\]\](UDU)
=
E[E2[S3]|F 0]
=
P(UUU|F 0)E[S3|F 00] + P(UUD|F 0)E[S3|F 00]
+
+P(UDU|F 0)E[S3|F 01] + P(UDD|F 0)E[S3|F 01]
=
{P(UUU|F 0) + P(UUD|F 0)}
×
{P(UUU|F 00)S000 + P(UUD|F 00)S001}
+
{P(UDU|F 0) + P(UDD|F 0)}
×
{P(UDU|F 01)S010 + P(UDD|F 01)S011}.
(C.81)
Collecting terms that have the same value of S3, we have
E1\[E2\[S3\]\](UDU)
=
{P(UUU|F 0) + P(UUD|F 0)}P(UUU|F 00)S000
+
{P(UUU|F 0) + P(UUD|F 0)}P(UUD|F 00)S001
+
{P(UDU|F 0) + P(UDD|F 0)}P(UDU|F 01)S010
+
{P(UDU|F 0) + P(UDD|F 0)}P(UDD|F 01)S011.(C.82)
We then note that P(UUU|F 0)+P(UUD|F 0) = P(F 00|F 0), and similarly P(UDU|F 0)+
P(UDD|F 0) = P(F 01|F 0), so
E1\[E2\[S3\]\](UDU)
=
P(F 00|F 0)P(UUU|F 00)S000
+
P(F 00|F 0)P(UUD|F 00)S001
+
P(F 01|F 0)P(UDU|F 01)S010
+
P(F 01|F 0)P(UDD|F 01)S011.
(C.83)
But then P(F 00|F 0)P(UUU|F 0) = P(UUU|F 0), and so on, which simplifies our
result to
E1\[E2\[S3\]\](UDU)
=
P(UUU|F 0)S000 + P(UUD|F 0)S001
+
P(UDU|F 0)S010 + P(UDD|F 0)S011
=
E1\[S3\](UDU),
(C.84)
165

which is what we wanted to prove.
We can then use the tower law to evaluate the other conditional expectations. For
example,
E0
· S2
B2
¸
= E0
·
E1
· S2
B2
¸¸
.
(C.85)
But, we have already evaluated the single time-step conditional expectations, and
hence
E0
· S2
B2
¸
= E0
· S1
B1
¸
.
(C.86)
Once again, we have already calculated this result, and so we see that
E0
· S2
B2
¸
= S0
B0
.
(C.87)
Similarly we see that
E0
· S3
B3
¸
=
E0
·
E2
· S3
B3
¸¸
=
E0
· S2
B2
¸
=
S0
B0
.
(C.88)
Finally, we also have
E1
· S3
B3
¸
=
E1
·
E2
· S3
B3
¸¸
=
E1
· S2
B2
¸
=
S1
B1
.
(C.89)
Section 9
1. We need to show that the number of ways of arriving at the node Sn
i is Cn
i . The
node Sn
i is a combination of i ‘down’ movements and n −i ‘up’ movements. Hence
we can view the problem as being the number of ways of placing i identical objects
(the down movements) in n ordered positions (the total number of time steps).
The number of ways of placing n distinct objects in n locations is n!. However,
this overcounts the number of ‘up’ movements by a factor of (n −i)!, since they are
indistinguishable, and overcounts the ‘down’ movements by a factor i!. Hence the
total number of distinct combinations is n!/[i!(n −i)!], which is simply Cn
i .
166

$100 ©©©©
* $105
HHHH
j $95
©©©©
* $110.25
HHHH
j $99.75
©©©©
*
HHHH
j $90.25
©©©©
* $115.76
HHHH
j
©©©©
* $104.74
HHHH
j $94.76
©©©©
*
HHHH
j $85.74
Figure C.4:
The share prices for the lattice model.
2. We want to verify that the risk-neutral probabilities for the binomial lattice are
consistent with the risk-neutral probabilities derived earlier for the non-recombining
tree,
p0
∗=
˜S −S1
S0 −S1
and
p1
∗= S0 −˜S
S0 −S1 .
(C.90)
Setting S0 = uS0, S1 = dS0 and ˜S = erS0 we see that
p0
∗
=
erS0 −dS0
uS0 −dS0
(C.91)
=
er −d
u −d ,
(C.92)
which is the probability p∗obtained for the lattice model.
By conservation of
probability we must also have p1
∗= q∗.
3. Consider a market with S0 = $100, p = 0.6, er = 1.01, u = 1.05 and d = 0.95. The
lattice of share prices is given in figure C.4. The risk neutral probability p∗can be
calculated as
p∗
=
er −d
u −d
=
1.01 −0.95
1.05 −0.95
=
0.6.
(C.93)
We now want to price a call option with a strike of $100. The initial price f0 of any
derivative is given by the binomial pricing formula
f0 = e−rn
n
X
i=0
Cn
i pn−i
∗
qi
∗f i
n,
(C.94)
167


## Short Rate Models

where in the case of our call option the payofffunction f i
n = Si
n−$100. Substituting
in the share prices, we have
f 0
3 = $15.76
f 1
3 = $4.74
f 2
3 = $0
and
f 3
3 = $0
(C.95)
The pricing formula then yields an initial cost for the call option of
f0
=
(1)(0.6)3(0.4)0($15.76) + (3)(0.6)2(0.4)1($4.74)
(1.01)3
=
$5.29
(C.96)
Section 11
1. For now, we will assume that Wa+b−Wb is normally distributed and merely calculate
its mean and variance. The calculation of the expectation is trivial,
E[Wa+b −Wa]
=
E[Wa+b] −E[Wa]
=
0,
(C.97)
where we have used the fact that the expectation of a Brownian motion Wt at any
time t is 0. The variance calculation is slightly more complicated, but not much.
We see that
E[(Wa+b −Wa)2]
=
E[W 2
a+b −2Wa+bWa + W 2
a ]
=
E[W 2
a+b] −2E[Wa+bWa] + E[W 2
a ]
=
a + b −2E[Wa+bWa] + a,
(C.98)
where we took advantage of the fact that the variance of Wt is t. But what about the
term E[Wa+bWa]? The two random variables Wa+b and Wa are not independent,
so we cannot factor the term into E[Wa+b]E[Wa].
So how do we evaluate it?
Well, we make use of a common trick for generating independent variables. Write
Wa+b = (Wa+b −Wa) + Wa. We then have
E[(Wa+b −Wa)2]
=
2a + b −2E[{(Wa+b −Wa) + Wa}Wa]
=
2a + b −2E[(Wa+b −Wa)Wa]
−2E[W 2
a ].
(C.99)
But now we can make use of the fact that (Wa+b −Wa) and Wa are independent
random variables, and hence
E[(Wa+b −Wa)2]
=
2a + b −2E[Wa+b −Wa]E[Wa] −2E[W 2
a ]
=
2a + b −0 −2a
=
b.
(C.100)
Thus we see that Wa+b −Wa has a mean of zero and a variance of b.
168

2. We want to calculate the variance of the asset price process St, which has a time
evolution governed by equation (11.1),
St = S0eµt−1
2 σ2t+σWt.
(C.101)
We already demonstrated in equation (11.10) that the expectation of the asset price
is
E[St] = S0eµt.
(C.102)
In order to obtain the variance, we first need to calculate the expectation of the
square of the asset price,
E[S2
t ]
=
E
h
S2
0e2µt−σ2t+2σWti
=
S2
0e2µt−σ2tE
£
e2σWt¤
.
(C.103)
Since Wt is an N(0, t) random variable, we can use the result of lemma (11.1) to
evaluate the expectation,
E[S2
t ]
=
S2
0e2µt−σ2te2σ2t
=
S2
0e2µt+σ2t.
(C.104)
Hence we can calculate the variance as
V [St]
=
E[S2
t ] −E[St]2
=
S2
0e2µt+σ2t −S2
0e2µt
=
S2
0e2µt(eσ2t −1).
(C.105)
3. We want to calculate the first four moments for an N(m, V ) random variable. To
begin with, we will calculate the first four moments of the ‘standard normal distri-
bution’, N(0, 1). Note that by symmetry any odd moments vanish. We can then
calculate the zeroth moment (which must be 1 by conservation of probability) by
using a well-known change of coordinates. We begin by considering the square of
the integral,
I2
=
·
1
√
2π
Z ∞
−∞
e−u2/2du
¸2
=
1
2π
Z ∞
−∞
e−x2/2dx
Z ∞
−∞
e−y2/2dy
=
1
2π
Z ∞
−∞
Z ∞
−∞
e−(x2+y2)/2dydx
(C.106)
We then want to change to polar coordinates r and θ
I2
=
1
2π
Z 2π
0
Z ∞
0
e−r2/2rdrdθ
=
Z ∞
0
e−r2/2rdr
(C.107)
169

Making the variable substitution v = r2/2 we obtain
I2
=
Z ∞
0
e−vdv
=
1,
(C.108)
so that I is indeed equal to 1. We can then obtain the other moments by using
integration by parts. For example,
1
√
2π
Z ∞
−∞
x2e−x2/2
=
−xe−x2/2
√
2π
¯¯¯¯¯
∞
−∞
+
1
√
2π
Z ∞
−∞
e−x2/2dx
=
1.
(C.109)
For the fourth moment, we have
1
√
2π
Z ∞
−∞
x4e−x2/2
=
−x3e−x2/2
√
2π
¯¯¯¯¯
∞
−∞
+
1
√
2π
Z ∞
−∞
3x2e−x2/2dx
=
3.
(C.110)
Using these results, we can then derive the moments for an N(m, V ) random vari-
able,
E[Xn] =
1
√
2πV
x=∞
Z
x=−∞
xne−(x−m)2
2V
dx.
Making the variable substitution u = (x −m)/
√
V , we have
E[Xn] =
1
√
2π
u=∞
Z
u=−∞
(
√
V u + m)ne−u2
2 du.
Expanding the binomial term,
E[Xn] =
n
X
k=0
¡ nk
¢ V k/2mn−k
√
2π
u=∞
Z
u=−∞
uke−u2
2 du.
The integral is now in terms of the moments of an N(0, 1) variable, and hence we
can find the values
E[X]
=
m
(C.111)
E[X2]
=
m2 + V
(C.112)
E[X3]
=
m3 + 3mV
(C.113)
E[X4]
=
m4 + 6m2V + 3V 2.
(C.114)
170

4. We want to calculate E[eαX] and V [eαX] for an N(m, V ) random variable X. We
already calculated the expectation of eαX in lemma 11.1,
E[eαX] = eαm+ 1
2 α2V .
(C.115)
In order to obtain the variance, we need to consider the expectation of (eαX)2 =
e2αX. This is easy to evaluate, again by using lemma 11.1,
E[e2αX] = e2αm+2α2V .
(C.116)
Hence the variance is
V [eαX]
=
E[e2αX] −E[eαX]2
=
e2αm+2α2V −e2αm+α2V
=
e2αm+2α2V (1 −e−α2V ).
(C.117)
5. We want to show that Mt(Wt) = eαWt−1
2 α2t is a martingale, that is, Es[Mt] = Ms.
The simplest way to do this is to rewrite Mt in terms of random variables that are
independent of the conditioning at time s. That is, write
Mt = eα(Wt−Ws)+αWs−1
2 α2t,
(C.118)
which is a function of the N(0, t −s) random variable (Wt −Ws) and the constant
Ws. Note that (Wt −Ws) is independent of any conditioning at time s because
of the independent increments property of Brownian motion, while Ws is fixed by
the fact that we know what actually happens at time s—this is what a conditional
expectation means. Thus we can calculate the conditional expectation of Mt by
integrating (C.118) over the probability distribution for (Wt −Ws) and treating Ws
as a constant,
Es[Mt]
=
Z ∞
−∞
exp
·
αx + αWs −1
2α2t
¸
1
p
2π(t −s)
exp
·
−x2
2(t −s)
¸
dx
=
1
√t −s exp
·
αWs −1
2α2t
¸
×
1
√
2π
Z ∞
−∞
exp
·
−
x2
2(t −s) + αx
¸
dx.
(C.119)
We then want to use the result, which is not difficult to prove, that
1
√
2π
Z ∞
−∞
exp
·
−1
2ax2 + bx + c
¸
dx =
1
√a exp
· b2
2a + c
¸
.
(C.120)
In our case we have
a =
1
t −s,
b = α,
and
c = 0,
(C.121)
171

and hence
Es[Mt]
=
1
√t −s exp
·
αWs −1
2α2t
¸ √
t −s exp
·
−1
2α2(t −s)
¸
=
exp
·
αWs −1
2α2s
¸
=
Ms,
(C.122)
so Mt is a martingale.
6. We want to show that Nt = cos(βWt)e
1
2 β2t is a martingale, that is, Es[Nt] = Ns.
Begin by rewriting Nt as the real part of a complex function,
Nt
=
cos(βWt)e
1
2 β2t
=
ℜexp
·
iβWt + 1
2β2t
¸
.
(C.123)
If we then set β = −iα, we obtain
Nt
=
ℜexp
·
αWt −1
2α2t
¸
=
ℜMt,
(C.124)
where we have substituted in the martingale process Mt considered in the previous
question. Taking expectations then yields
Es[Nt]
=
Es[ℜMt]
=
ℜEs[Mt]
=
ℜMs
=
ℜexp
·
αWs −1
2α2s
¸
=
ℜexp
·
iβWs + 1
2β2s
¸
=
cos(βWs) exp
·1
2β2s
¸
.
(C.125)
Thus we see that the process Nt is indeed a martingale.
Section 12
1. We want to show that the Wiener model for an asset price process, with dynamics
given by equation (11.1)
St = S0 exp
·µ
µ −1
2σ2
¶
t + σWt
¸
,
(C.126)
172

satisfies the stochastic differential equation (13.1),
dSt
St
= µdt + σdWt.
(C.127)
To do this we define the stochastic process
Xt =
µ
µ −1
2σ2
¶
t + σWt,
(C.128)
which clearly satisfies the differential equation
dXt =
µ
µ −1
2σ2
¶
dt + σdWt.
(C.129)
Moreover, if we square dXt then we obtain
dX2
t = σ2dt,
(C.130)
where we have applied the Ito calculus rules dt2 = 0, dtdWt = 0 and dW 2
t = dt.
We can then consider the asset price process St as a function of a process for which
we know the differential equation, namely Xt. Using Ito’s lemma on the function
St(Xt) = S0eXt we obtain
d(St)
=
S0d(eXt)
=
S0
·∂eXt
∂Xt
dXt + 1
2
∂2eXt
∂X2
t
dX2
t
¸
=
S0eXt
·
dXt + 1
2dX2
t
¸
=
St
·µ
µ −1
2σ2
¶
dt + σdWt + 1
2σ2dt
¸
=
St [µdt + σdWt] .
(C.131)
Thus the Wiener model asset price process St satisfies the desired differential equa-
tion.
2. In this exercise, we want to calculate the stochastic differential equations for a
number of stochastic processes Xt. We can do this by considering them as a function
of both a Wiener process and time, that is Xt = Xt(Wt, t). Ito’s lemma then tells
us that the stochastic differential equation is
dXt = ∂Xt
∂t dt + ∂Xt
∂Wt
dWt + 1
2
∂2Xt
∂W 2
t
dt,
(C.132)
where we have set dW 2
t = dt in the final term. Thus,
(a) for the process Xt = W 2
t −t,
dXt
=
−dt + 2WtdWt + dt
=
2WtdWt;
(C.133)
173

(b) for the process Xt = W 3
t −3tWt,
dWt
=
−3Wtdt + (3W 2
t −3t)dWt + 1
26Wtdt
=
3(W 2
t −t)dWt;
(C.134)
(c) and for the process Xt = W 4
t −6tW 2
t + 3t2,
dXt
=
(−6W 2
t + 6t)dt + (4W 3
t −12tWt)dWt
+1
2(12W 2
t −12t)dt
=
4(W 3
t −3tWt)dWt.
(C.135)
3. We want to calculate the product rule d(XtYt) for stochastic processes Xt and Yt.
Expanding the differential as a Taylor series in dXt and dYt, and remembering to
keep all terms up to the second order, we have
d(XtYt)
=
∂(XtYt)
∂Xt
dXt + ∂(XtYt)
∂Yt
dYt + 1
2
∂2(XtYt)
∂X2
t
dX2
t
+1
2
∂2(XtYt)
∂Y 2
t
dY 2
t + ∂2(XtYt)
∂Xt∂Yt
dXtdYt
=
YtdXt + XtdYt + dXtdYt.
(C.136)
4. We can calculate the division rule for stochastic differentials d(Xt/Yt) in a manner
identical to that used for the product rule in the previous question,
d(Xt/Yt)
=
∂(Xt/Yt)
∂Xt
dXt + ∂(Xt/Yt)
∂Yt
dYt + 1
2
∂2(Xt/Yt)
∂X2
t
dX2
t
+1
2
∂2(Xt/Yt)
∂Y 2
t
dY 2
t + ∂2(Xt/Yt)
∂Xt∂Yt
dXtdYt
=
1
Yt
dXt −Xt
Y 2
t
dYt + Xt
Y 3
t
dY 2
t −1
Y 2
t
dXtdYt
=
Xt
Yt
·dXt
Xt
−dYt
Yt
+ dY 2
t
Y 2
t
−dXtdYt
XtYt
¸
.
(C.137)
Section 13
1. Starting with nothing, if we take the position Vt = Ct −φtSt −ψtBt then since it
has no net value, we can solve for the bond position ψt
ψt = Ct
Bt
−φt
St
Bt
.
(C.138)
At time t + dt the value of the portfolio has changed to
dVt = dCt −φtdSt −ψtdBt,
(C.139)
174

where we have kept the stock and bond holdings fixed.
Substituting in for the
stochastic differentials from equations (13.1), (13.2) and (13.4) we obtain
dVt
=
∂Ct
∂t dt + ∂Ct
∂St
dSt + 1
2
∂2Ct
∂S2
t
dS2
t −φtdSt
−
µCt
Bt
−φt
St
Bt
¶
rtBtdt.
(C.140)
Since dS2
t = σ2
t S2
t dt, the only differential that contains a random component is
dSt. Hence we can obtain a guaranteed return on our portfolio if we set the stock
holding φt to be
φt = ∂Ct
∂St
.
(C.141)
The fixed return is then
dVt =
µ∂Ct
∂t + 1
2σ2
t s2
t
∂2Ct
∂S2
t
−rtCt + rtSt
∂Ct
∂St
¶
dt.
(C.142)
By the no arbitrage condition this must be zero, and hence we recover the Black-
Scholes equation
∂Ct
∂t + 1
2σ2
t s2
t
∂2Ct
∂S2
t
−rtCt + rtSt
∂Ct
∂St
= 0.
(C.143)
2. We want to value a call option for T −t = 0.5, K = 115, St = 100 σ = .2 and
r = 0.05. We find that
h+
=
−0.741
h−
=
−0.882
N(h+)
=
0.229
N(h−)
=
0.188
(C.144)
and hence the call option price is $1.76.
Section 14
1. We want to verify that the trading strategy (φt, ψt) is self-financing.
(a) We begin by calculating the stochastic differential of the ratio of the derivative
to the bond price,
d
µCt
Bt
¶
=
dCt
Bt
−CtdBt
B2
t
−dCtdBt
B2
t
=
Ct
Bt
µdCt
Ct
−dBt
Bt
¶
=
Ct
Bt
¡
µC
t dt + σC
t dWt −rtdt
¢
.
(C.145)
175

We then move on to the ratio of the asset to bond price,
φtd
µ St
Bt
¶
=
φt
µdSt
Bt
−StdBt
B2
t
−dCtdBt
B2
t
¶
=
σC
t Ct
σtSt
St
Bt
µdSt
St
−dBt
Bt
¶
=
σC
t Ct
σtBt
(µtdt + σtdWt −rtdt) .
(C.146)
Taking the difference between the two yields
d
µCt
Bt
¶
−φtd
µ St
Bt
¶
=
Ct
Bt
£
µC
t dt + σC
t dWt −rtdt
−σC
t
σt
(µtdt + σtdWt −rtdt)
¸
=
CtσC
t
Bt
·µC
t −rt
σC
t
dt + dWt −µt −rt
σt
dt −dWt
¸
=
CtσC
t
Bt
·µC
t −rt
σC
t
dt −µt −rt
σt
dt
¸
=
0.
(C.147)
(b) The equation Ct = φtSt + ψtBt can be taken as the definition of ψt. Hence
calculating the differential,
Btdψt
=
Btd
µCt
Bt
−φt
St
Bt
¶
=
Bt
·
d
µCt
Bt
¶
−φtd
µ St
Bt
¶
−dφt
St
Bt
−dφtd
µ St
Bt
¶¸
(C.148)
Using the differential rule for ratios of stochastic processes that we calculated
in exercise 12.4, we obtain
Btdψt = −dφtSt −dφtdSt + dφt
StdBt
Bt
+ dφt
dStdBt
Bt
(C.149)
We then notice that since dBt is deterministic, that is, it has only dt terms
and not dWt terms, the product of dBt with any other stochastic differential
is always zero. Hence we obtain
Btdψt = −dφtSt −dφtdSt.
(C.150)
176

(c) Finally, if we take the differential of Ct we obtain
dCt = φtdSt + dφtSt + dφtdSt + dψtBt + ψtdBt + dψtdBt.
(C.151)
We then want to set dψtdBt = 0 and substitute for Btdψt from above,
dCt
=
φtdSt + dφtSt + dφtdSt −dφtSt −dφtdSt + ψtdBt
=
φtdSt + ψtdBt.
(C.152)
Thus, we see that the trading strategy (φt, ψt) is, in fact, self-financing.
Section 15
1. We want to calculate the expectation of a stochastic integral
I =
Z t
0
g(Ws)dWs,
(C.153)
where g(Ws) is an arbitrary well-behaved function. Recall from equation (12.3)
that the definition of the stochastic integral is
I = lim
N→∞
N
X
i=0
g(Wti)(Wti+1 −Wti),
(C.154)
where the ti are some partition of the interval [0, 1]. Taking expectations of this we
have
E[I] = lim
N→∞
N
X
i=0
E[g(Wti)(Wti+1 −Wti)].
(C.155)
But by the independent increments property of Brownian motion, we know that
(Wti+1 −Wti) and Wti are independent random variables and hence we can factor
their product in an expectation, that is,
E[I] = lim
N→∞
N
X
i=0
E[g(Wti)]E[(Wti+1 −Wti)].
(C.156)
But the expected value of the difference of a Brownian motion at two different times
is zero E[(Wti+1 −Wti)] = 0 and hence every term in the sum vanishes. Thus
E[I] = 0,
(C.157)
which is what we set out to prove.
2. We want to verify that the function
A(x, τ)
=
E[f(x + σWτ)]
=
1
√
2πτ
Z ∞
−∞
f(x + σξ) exp
·
−ξ2
2τ
¸
dξ
(C.158)
177

is a solution of the heat equation
∂A
∂τ = 1
2σ2 ∂2A
∂x2 .
(C.159)
In order to simplify the calculation, we define a new integration variable η = x+σξ.
This has the effect of moving the x and τ dependence from f into the exponential,
A =
1
√
2πτ
Z ∞
−∞
f(η) exp
·
−(η −x)2
2σ2τ
¸
dη.
(C.160)
We now need to calculate the derivatives,
∂A
∂τ
=
−
1
2
√
2πτ 3/2
Z ∞
−∞
f(η) exp
·
−(η −x)2
2σ2τ
¸
dη
+
1
√
2πτ
Z ∞
−∞
f(η)(η −x)2
2σ2τ 2
exp
·
−(η −x)2
2σ2τ
¸
dη
(C.161)
and
∂A
∂x =
1
√
2πτ
Z ∞
−∞
f(η)η −x
σ2τ exp
·
−(η −x)2
2σ2τ
¸
dη
(C.162)
which yields
∂2A
∂x2
=
1
√
2πτ
Z ∞
−∞
f(η) −1
σ2τ exp
·
−(η −x)2
2σ2τ
¸
dη
+
1
√
2πτ
Z ∞
−∞
f(η)(η −x)2
σ4τ 2
exp
·
−(η −x)2
2σ2τ
¸
dη
(C.163)
from which the result follows.
3. We want to price a forward contract with strike K and maturity T. The payoff
function F(ST ) = ST −K is simply the difference between the share price ST at
maturity and the strike price. Writing the derivative price in terms of an expectation
we obtain
F0
=
e−rT E∗[F(ST )]
=
e−rT E∗[ST −K]
=
e−rT E∗[ST ] −e−rT E∗[K].
(C.164)
But in equation (15.43) we calculated the price of a derivative that simply pays off
the share value at maturity, and found that it was just the initial share price S0.
This result allows us to evaluate the first term in equation (C.164). To evaluate
the second term, we note that the expectation of a constant is simply its value. We
then have
F0 = S0 −e−rT K,
(C.165)
which is the no arbitrage price for the derivative. The value of the strike K which
zeros the initial cost of the derivative is S0erT . This is called the forward price for
the asset.
178

Section 16
1. In this question we want to calculate and plot the partial derivatives of the call
option price with respect to various parameters. These quantities are useful when
trying to create portfolios which are hedged against movements or estimation errors
in the parameters. Recall the that price of a call option is
C0 = S0N(h+) −Ke−rT N(h−).
(C.166)
If we differentiate this value with respect to an arbitrary parameter x we obtain
∂C0
∂x
=
∂
∂x[S0N(h+)] −∂
∂x[Ke−rT N(h−)]
=
∂S0
∂x N(h+) −∂(Ke−rT )
∂x
N(h−)
+S0
∂N(h+)
∂x
−Ke−rT ∂N(h−)
∂x
.
(C.167)
We can simplify the last two derivatives. Begin by using the chain rule for differ-
entiation,
∂N(h±)
∂x
=
1
√
2π
∂h±
∂x e−(h±)2/2.
(C.168)
If we substitute in the values of h±, we see that
e−(h±)2/2 = e−X
µS0erT
K
¶∓1/2
,
(C.169)
where
X = (log ˜S/K)2 + 1
4σ4T 2
2σ2T
.
(C.170)
Substituting this back into equation (C.167) we see that
∂C0
∂x
=
∂S0
∂x N(h+) −∂Ke−rT
∂x
N(h−)
+S0e−(h+)2/2 ∂h+
∂x −Ke−rT e−(h−)2/2 ∂h−
∂x
=
∂S0
∂x N(h+) −∂Ke−rT
∂x
N(h−)
+e−X
µS0K
erT
¶1/2 ∂h+
∂x −e−X
µS0K
erT
¶1/2 ∂h−
∂x
=
∂S0
∂x N(h+) −∂Ke−rT
∂x
N(h−)
+
1
√
2π e−X
µS0K
erT
¶1/2 ∂(h+ −h−)
∂x
(C.171)
179

But h+ −h−= σ
√
T and so we end up with the relatively simple formula
∂C0
∂x
=
∂S0
∂x N(h+) −∂Ke−rT
∂x
N(h−)
+
1
√
2π e−X
µS0K
erT
¶1/2 ∂(σ
√
T)
∂x
.
(C.172)
(a) The first quantity that we want to calculate is the change in the option price
with respect to a change in the value fo the underlying asset price. We see
that only the first term in equation (C.172) contributes and
∆
=
∂C0
∂S0
=
N(h+).
(C.173)
(b) If we now take a second derivative of this,
Γ
=
∂2C0
∂S2
0
=
∂N(h+)
∂S0
=
1
√
2π
1
σ
√
TS0
e−X
µS0erT
K
¶−1/2
(C.174)
(c) If we calculate the effect of varying the volatility, only the final term in (C.172)
contributes,
V
=
∂C0
∂σ
=
1
√
2π e−X
µS0K
erT
¶1/2 √
T.
(C.175)
(d) Calculating the change in the derivative value as we change the time to expiry,
we get contributions from the last two terms in (C.172),
θ
=
−∂C0
∂T
=
−
1
√
2π e−X
µS0K
erT
¶1/2
σ
2
√
T
−rKe−rT N(h−)
(C.176)
(e) Finally, if we vary the interest rate we obtain
ρ
=
∂C0
∂r
=
kTe−rT N(h−).
(C.177)
180

Section 17
1. We want to calculate the initial value of a binary put option with a payofffunction
BPT (ST ) = H(K −ST ) at time T. Using the derivative pricing equation (15.38),
we see that
BP0
=
e−rT E∗[BPT (ST )]
=
e−rT
√
2πT
Z ∞
−∞
H(K −ST )e−ξ2/2T dξ
=
e−rT
√
2πT
Z ∞
−∞
H (K −S0 exp[ (r −1
2σ2)T + σξ ]) e−ξ2/2T dξ
=
e−rT
√
2π
Z ∞
−∞
H (K −S0 exp[ (r −1
2σ2)T + σ
√
Tη ])
×e−η2/2dη,
(C.178)
where we have made the substitution η = ξ/
√
T in the final integral. The Heaviside
function is non-zero only when
S0 exp
·
(r −1
2σ2)T + σ
√
Tη
¸
< K.
(C.179)
Taking logarithms and isolating η yields
(r −1
2σ2)T + σ
√
Tη
<
−log(S/K)
η
<
−log(S/K) + (r −1
2σ2)Tσ
√
T
η
<
−h−.
(C.180)
Thus the integral simplifies to
BP0
=
e−rT
√
2π
Z −h−
−∞
e−η2/2dη
=
e−rT N(−h−).
(C.181)
We could have calculated this result by using the binary call option price, calculated
in equation (C.250)
BC0 = e−rT N(h−),
(C.182)
and the put-call result of equation (17.16)
BC0 + BP0 = e−rT .
(C.183)
These two equations immediately tell us that
BP0 = e−rT [1 −N(h−)].
(C.184)
If we then use the relation N(x) + N(−x) = 1, we recover the formula calculated
above,
BP0 = e−rT N(−h−).
(C.185)
181

2. Using positions in the underlying and call options, we want to construct a Gamma
neutral portfolio which is short one binary call. If we hold φ shares and ψ call
options, then the value of the portfolio is
V0 = −BC0 + φS0 + ψC0.
(C.186)
Differentiating with respect to the share price, we find that
∆= −∆bc + φ + ψ∆c
(C.187)
where ∆bc and ∆c are the Deltas of the binary call and call options respectively.
Differentiating again, we find the Gamma of the portfolio,
Γ = −Γbc + ψΓc.
(C.188)
Making the portfolio Gamma neutral, we can solve for the value of ψ,
ψ = Γbc
Γc
.
(C.189)
We can then make the portfolio Delta neutral, and hence obtain the value of φ,
φ = ∆bc −Γbc
Γc
∆c.
(C.190)
In a previous exercise we determined the values of Delta and Gamma for the call
option
∆c = N(h+)
and
Γc =
1
σ
√
TS0
e−X
√
2π
r
K
S0erT ,
(C.191)
where
X = (log ˜S/K)2 + 1
4σ4T 2
2σ2T
.
(C.192)
Substituting in the numbers K = 120, S0 = 100, r = 0.05, σ = .2 and T = 1.0 for
the call option, we find that
∆c = 0.287192
and
Γc = 0.0170369.
(C.193)
To calculate the Delta and Gamma for the binary call, we recall that the price is
BC0 = e−rT N(h−).
(C.194)
Differentiating twice with respect to S0 we find that
∆bc = e−rt
√
2π
1
σ
√
T
1
p
KS0erT
and
Γbc = −
∆b
σ
√
TS0
h+.
(C.195)
Substituting in K = 110, S0 = 100, r = 0.05, σ = .2 and T = 1.0 we find that
∆bc = 0.0179891
and
Γbc = 0.000113827,
(C.196)
which allows us to determine the share and call options holdings,
φ = 0.0160703
and
ψ = 0.00668119.
(C.197)
182

