# Arbitrage Pricing Theory

!!! info "Source"
    **The Mathematics of Financial Modeling and Investment Management** by Sergio M. Focardi and Frank J. Fabozzi, Wiley, 2004.
    These notes are used for educational purposes.

## Arbitrage Pricing: Finite-State Models

CHAPTER 14 
Arbitrage Pricing: 
Finite-State Models 
T
he Principle of Absence of Arbitrage is perhaps the most fundamental 
principle of finance theory. In the presence of arbitrage opportunities, 
there is no trade-off between risk and returns because it is possible to 
make unbounded risk-free gains. The principle of absence of arbitrage is 
fundamental for understanding asset valuation in a competitive market. 
This chapter discusses arbitrage pricing in a finite-state, discrete-time 
setting. In the following chapter we extend the discussion to a continu-
ous-time, continuous-state setting. 
THE ARBITRAGE PRINCIPLE 
Let’s begin by defining what is meant by arbitrage. In its simple form, 
arbitrage is the simultaneous buying and selling of an asset at two differ-
ent prices in two different markets. The arbitrageur profits without risk 
by buying cheap in one market and simultaneously selling at the higher 
price in the other market. Such opportunities for arbitrage are rare. In 
fact, a single arbitrageur with unlimited ability to sell short could correct 
a mispricing condition by financing purchases in the underpriced market 
with proceeds of short sales in the overpriced market. (Short-selling 
means selling an asset that is not owned in anticipation of a price 
decline. The mechanism for doing this is described in Chapter 2.) This 
means that riskless arbitrage opportunities are short-lived. 
Less obvious arbitrage opportunities exist in situations where a 
package of assets can produce a payoff (expected return) identical to an 
asset that is priced differently. This arbitrage relies on a fundamental 
393 

394 
The Mathematics of Financial Modeling and Investment Management 
principle of finance called the law of one price, which states that a given 
asset must have the same price regardless of the location where the asset 
is traded and the means by which one goes about creating that asset. 
The law of one price implies that if the payoff of an asset can be syn-
thetically created by a package of assets, the price of the package and 
the price of the asset whose payoff it replicates must be equal. 
When a situation is discovered whereby the price of the package of 
assets differs from that of an asset with the same payoff, rational inves-
tors will trade these assets in such a way so as to restore price equilib-
rium. This market mechanism is founded on the fact that an arbitrage 
transaction does not expose the investor to any adverse movement in 
the market price of the assets in the transaction. 
For example, consider how we can produce an arbitrage opportu-
nity involving three assets A, B, and C. These assets can be purchased 
today at the prices shown below, and can each produce only one of two 
payoffs (referred to as State 1 and State 2) a year from now: 
Asset 
Price 
Payoff in State 1 
Payoff in State 2 
A 
$70 
$50 
$100 
B 
60
 30 
120 
C 
80 
38 
112 
While it is not obvious from the data presented above, an investor 
can construct a portfolio of assets A and B that will have the identical 
return as asset C in both State 1 and State 2. Let wA and wB be the pro-
portion of assets A and B, respectively, in the portfolio. Then the payoff 
(i.e., the terminal value of the portfolio) under the two states can be 
expressed mathematically as follows: 
■ If State 1 occurs: $50 wA + $30 wB
 ■ If State 2 occurs: $100 wA + $120 wB 
We create a portfolio consisting of A and B that will reproduce the 
payoff of C regardless of the state that occurs one year from now. Here 
is how: for either condition (State 1 and State 2) we set the payoff of the 
portfolio equal to the payoff for C as follows: 
■ State 1: $50 wA + $30 wB = $38
 ■ State 2: $100 wA + $120 wB = $112 

395 
Arbitrage Pricing: Finite-State Models 
We also know that wA + wB = 1. If we solved for the weights for wA 
and wB that would simultaneously satisfy the above equations, we 
would find that the portfolio should have 40% in asset A (i.e., wA = 0.4) 
and 60% in asset B (i.e., wB = 0.6). The cost of that portfolio will be 
equal to 
(0.4)($70) + (0.6)($60) = $64 
Our portfolio (i.e., package of assets) comprised of assets A and B 
has the same payoff in State 1 and State 2 as the payoff of asset C. The 
cost of asset C is $80 while the cost of the portfolio is only $64. This is 
an arbitrage opportunity that can be exploited by buying assets A and B 
in the proportions given above and shorting (selling) asset C. 
For example, suppose that $1 million is invested to create the port-
folio with assets A and B. The $1 million is obtained by selling short 
asset C. The proceeds from the short sale of asset C provide the funds to 
purchase assets A and B. Thus, there would be no cash outlay by the 
investor. The payoffs for States 1 and 2 are shown below: 
Asset 
Investment 
State 1 
State 2 
A 
$400,000
 $285,715
 $571,429 
B
 600,000
 300,000
 1,200,000 
C 
–1,000,000
 –475,000 
–1,400,000 
Total
 0
 110,715
 371,429 
ARBITRAGE PRICING IN A ONE-PERIOD SETTING 
We can describe the concepts of arbitrage pricing in a more formal 
mathematical context. It is useful to start in a simple one-period, finite-
state setting as in the example of the previous section. This means that 
we consider only one period and that there is only a finite number M of 
states of the world. In this setting, asset prices can assume only a finite 
number of values. 
The assumption of finite states is not as restrictive as it might 
appear. In practice, security prices can only assume a finite number of 
values. Stock prices, for example, are not real numbers but integer frac-
tions of a dollar. In addition, stock prices are nonnegative numbers and 
it is conceivable that there is some very high upper level that they can-
not exceed. In addition, whatever simulation we might perform is a 
finite-state simulation given that the precision of computers is finite. 

396 
The Mathematics of Financial Modeling and Investment Management 
The finite number of states represents uncertainty. There is uncer-
tainty because the world can be in any of the M states. At time 0 it is not 
known in what state the world will be at time 1. Uncertainty is quanti-
fied by probabilities but a lot of arbitrage pricing theory can be devel-
oped without any reference to probabilities. Suppose there are N 
securities. Each security i pays dij number of dollars (or of any other 
unit of account) in each state of the world j. The payoff of each security 
need not be a positive number. For instance, a derivative instrument 
might have negative payoffs in some states of the world. Therefore, in a 
one-period setting, the securities are formally represented by an N×M 
matrix D = {dij} where the dij entry is the payoff of security i in state j. 
Recall from Chapter 5 that the matrix D can also be written as a set of 
N row vectors: 
d1 
D = 
·
, di = 
dN 
di1 · diM 
where the M-vector di represents the payoffs of security i in each of the 
M states. 
Each security is characterized by a price S. Therefore, the set of N 
securities is characterized by an N-vector S and an N×M matrix D. Sup-
pose, for instance, there are two states and three securities. Then the 
three securities are represented by 
S1 
S = S2 , D = 
S3 
d11 d12 
d21 d22 
d31 d32 
Every row of the D matrix represents one security, every column one 
state. Note that in a one-period setting, prices are defined at time 0 
while payoffs are defined at time 1. There is no payoff at time 0 and 
there is no price at time 1. A portfolio is represented by a N-vector of 
weights θ. In our example of a market with two states and three securi-
ties, a portfolio is a 3-vector: 
θ = 
θ1 
θ2 
θ3 

397 
Arbitrage Pricing: Finite-State Models 
The market value Sθ of a portfolio θ at time 0 is a scalar given by 
the scalar product: 
N 
Sθ = Sθ = ∑ Siθi 
i = 1 
Its payoff dθ at time 1 is the M-vector: 
dθ = D′θ
The price of a security and the market value of a portfolio can be negative 
numbers. In the previous example of a two-state, three-security market 
we obtain 
Sθ = Sθ = S1θ1 + S2θ2 + S3θ3 
dθ
D′θ
d11 d21 d31 
d12 d22 d32 
θ1 
θ2 
θ3 
d11θ1 
d21θ2 
d31θ3
+ 
+ 
d12θ1 
d22θ2 
d32θ3
+ 
+ 
= 
= 
= 
Let’s introduce the concept of arbitrage in this simple setting. As we 
have seen, arbitrage is essentially the possibility of making money by trad-
ing without any risk. Therefore, we define an arbitrage as any portfolio θ 
which has a negative market value Sθ = Sθ < 0 and a nonnegative payoff 
Dθ = D′θ ≥ 0 or, alternatively, a nonpositive market value Sθ = Sθ ≤ 0 and 
a positive payoff Dθ = D′θ > 0 . 
State Prices 
Next we define state prices. A state-price vector is a strictly positive M-
vector ψ such that security prices can be written as S = Dψ. In other 
words, given a state-price vector, if it exists, security prices can be 
recovered as a weighted average of the securities’ payoffs, where the 
state-price vector gives the weights. In the previous two-state, three-security 
example we can write: 
ψ1
ψ = ψ2 
S = Dψ 

398 
The Mathematics of Financial Modeling and Investment Management 
S1 
d11 d12 ψ1 
d11ψ1 + d12ψ2 
S2 = d21 d22 ψ2 
= d21ψ1 + d22ψ2 
S3 
d31 d32 
d31ψ1 + d32ψ2 
Given security prices and payoffs, state prices can be determined 
solving the system: 
+ d12ψ2 = S1
d11ψ1 
+ d22ψ2 = S2
d21ψ1 
+ d32ψ2 = S3
d31ψ1 
This system admits solutions if and only if there are two linearly inde-
pendent equations and the third equation is a linear combination of the 
other two. Note that this condition is necessary but not sufficient to ensure 
that there are state prices as state prices must be strictly positive numbers. 
A portfolio θ is characterized by payoffs dθ = D′θ . Its price is given, 
in terms of state prices, by: Sθ = Sθ = Dψθ = dθψ. 
It can be demonstrated that there is no arbitrage if and only if there is 
a state-price vector. The formal demonstration is quite complicated given 
the inequalities that define an arbitrage portfolio. It hinges on the Separat-
ing Hyperplane Theorem, which says that, given any two convex disjoint 
sets in RM, it is possible to find a hyperplane separating them. A hyper-
plane is the locus of points xi that satisfy a linear equation of the type: 
M 
a0 + ∑ aixi = 0 
i = 1 
Intuitively, however, it is clear that the existence of state prices ensures 
that the law of one price introduced in the previous section is automatically 
satisfied. In fact, if there are state prices, two identical payoffs have the 
same price, regardless of how they are constructed. This is because the price 
of a security or of any portfolio is univocally determined as a weighted 
average of the payoffs, with the state prices as weights. 
Risk-Neutral Probabilities 
Let’s now introduce the concept of risk-neutral probabilities. Given a 
state-price vector, consider the sum of its components ψ0 = ψ1 + ψ2 + … 
+ ψM. Normalize the state-price vector by dividing each component by 
the sum ψ0. The normalized state-price vector 

399 
Arbitrage Pricing: Finite-State Models 
ψj 
ψ = {
}
 
= ------ 
ψ0  
ψ
ˆ
ˆ j
is a set of positive numbers whose sum is one. These numbers can be 
interpreted as probabilities. They are not, in general, the real probabili-
ties associated with states. They are called risk-neutral probabilities. We 
can then write 
1
S------ = Dψˆ 
ψ0 
We can interpret the above relationship as follows: The normalized 
security prices are their expected payoffs under these special probabili-
ties. In fact, we can rewrite the above equation as 
Si 
[
]
Si = ------ = E di
ψ0 
where expectation is taken with respect to risk-neutral probabilities. In 
this case, security prices are the discounted expected payoffs under these 
special risk-neutral probabilities. 
Suppose that there is a portfolio θ  such that dθ = D′θ  = {1,1,...,1}. 
This portfolio can be one individual risk-free security. As we have seen 
above Sθ = dθψ, which implies that ψ0 = θS is the discount on riskless 
borrowing. 
Complete Markets 
Let’s now define the concept of complete markets, a concept that plays a 
fundamental role in finance theory. In the simple setting of the one-
period finite-state market, a complete market is one in which the set of 
possible portfolios is able to replicate an arbitrary payoff. Call span(D) 
the set of possible portfolio payoffs which is given by the following 
expression: 
span D
(
) ≡{D′θ: θ ∈ RM} 
A market is complete if span(D) = RM . 
A one-period finite-state complete market is one where the equation 

400 
The Mathematics of Financial Modeling and Investment Management 
D′θ = ξ: ξ ∈ RM 
always admits a solution. Recall from Chapter 5 on matrix algebra that 
this is the case if and only if the rank of D is M. This means that there 
are at least M linearly independent payoffs—that is, there are as many 
linearly independent payoffs as there are states. Let’s write down explic-
itly the system in the two-state three-security market. 
D′θ = ξ 
θ1
d11 d21 d31 θ2 = ξ1 
d12 d22 d32 θ3 
ξ2 
= ξ1
d11θ1 + d21θ2 + d31θ3 
= ξ2
d12θ1 + d22θ2 + d32θ3 
Recall from Chapter 5 that this system of linear equations admits 
solutions if and only if the rank of the coefficient matrix is 2. This con-
dition is not verified, for example, if the securities have the same payoff 
in each state. In this case, the relationship ξ1 = ξ2 must always be veri-
fied. In other words, the three securities can only replicate portfolios 
that have the same payoff in each state. 
In this simple setting it is easy to associate risk-neutral probabilities 
with real probabilities. In fact, suppose that the vector of real probabili-
ties p is associated to states so that pi is the probability of the i-th state. 
For any given M-dimensional vector x, we write its expected value 
under the real probabilities as 
M 
E x
[ ]  = px = ∑ pixi 
i = 1 
It can be demonstrated that there is no arbitrage if and only if there 
is a strictly positive M-vector π such that: S = E[Dπ]. Any such vector π
is called a state-price deflator. To see this point, define 
ψi
πi = -----
pi 

401 
Arbitrage Pricing: Finite-State Models 
Prices can then be expressed as 
M
M 
M
ψj
Si = ∑ dijψj = ∑ pjdij----- = ∑ pjdijπj 
j = 1 
j = 1 
pj 
j = 1 
which demonstrates that S = E[Dπ]. 
We can now specialize the above calculations in the numerical case 
of the previous section. Recall that in the previous section we gave the 
example of three securities with the following prices and payoffs 
expressed in dollars: 
S = 
70 
60 
80 
D = 
50 100 
30 120 
38 112 
We first compute the relative state prices: 
50ψ1 + 100ψ2 = 70 
30ψ1 + 120ψ2 = 60 
38ψ1 + 112ψ2 = 80 
Solving the first two equations, we obtain 
ψ1 
ψ2 
⁴₅ 
³₁₀ 
= 
However, the third equation is not satisfied by these values for the state 
prices. As a consequence, there does not exist a state-price vector which 
confirms that there are arbitrage opportunities as observed in the first 
section. 
Now suppose that the price of security C is $64 and not $80. In this 
case, the third equation is satisfied and the state-price vector is the one 
shown above. Risk-neutral probabilities can now be easily computed. 
Here is how. First sum the two state prices: ⁴₅ + ³⁄₁₀ = ¹¹⁄₁₀ to obtain 

402 
The Mathematics of Financial Modeling and Investment Management 
ψ0 = ψ1 + ψ2 = ¹¹₁₀ 
and consequently the risk-neutral probabilities: 
ψˆ 
ψˆ 1 
ψˆ 2 
ψ1 ψ0
⁄ 
ψ2 ψ0
⁄ 
⁸₁₁ 
³₁₁ 
= 
= 
= 
Risk-neutral probabilities sum to one while state prices do not. We can 
now check if our market is complete. Write the following equations: 
50θ1 + 30θ2 + 38θ3 = ξ1 
100θ1 + 120θ2 + 112θ3 = ξ2 
The rank of the coefficient matrix is clearly 2 as the determinant of the 
first minor is different from zero: 
50 30 
= 50 × 120 – 100 × 30 = 300 ≠ 0 
100 120 
Our sample market is therefore complete and arbitrage-free. A portfolio 
made with the first two securities can replicate any payoff and the third 
security can be replicated as a portfolio of the first two. 
ARBITRAGE PRICING IN A MULTIPERIOD FINITE-STATE 
SETTING 
The above basic results can be extended to a multiperiod finite-state set-
ting using the probabilistic concepts developed in Chapter 6. The econ-
omy is represented by a probability space (Ω,ℑ,P) where Ω is the set of 
possible states, ℑ is the algebra of events (recall that we are in a finite-
state setting and therefore there are only a finite number of events), and 
P is a probability function. As the number of states is finite, finite prob-
abilities P({ω}) ≡ P(ω) ≡ pω are defined for each state. There is only a 
finite number of dates from 0 to T. 
Propagation of Information 
Recall from Chapter 6 that the propagation of information is repre-
sented by a filtration ℑt that, in the finite case, is equivalent to an infor-

403 
Arbitrage Pricing: Finite-State Models 
mation structure It. The latter is a discrete, hierarchical organization of 
partitions It with the following properties:
…
…
·
·
Ik ≡( 
}); k = 0,
 ,
 
T; i = 1,
 ,
 
Mk; 1 = M1 ≤≤Mk ≤≤MT = M
{Aik 
Mk
Aik ∩Ajk = ∅if i ≠j and ∪Aik = Ω 
i = 1 
and, in addition, given any two sets Aik, Ajh, with h > k, either their 
intersection is empty Aik ∩Ajh = ∅or Aik ⊇Ajh. In other words, the par-
titions become more refined with time. 
Each security i is characterized by a payoff process dt
i and by a
i
i
price process St
i . In this finite-state setting, dt and St are discrete vari-
ables that, given that there are M states, can be represented by M-vec-
i ω
i 
ω
ω
ω
tors dt
i = [dt(
)] and St = [St
i (
)] where dt
i (
)
 and St
i (
)
 are, 
respectively, the payoff and the price of the i-th asset at time t, 0 ≤t ≤T 
and in state ω ∈ Ω. Following Chapter 6, all payoffs and prices are sto-
chastic processes adapted to the filtration ℑt. Recall from Chapter 6
i
that, given that dt
i and St are adapted processes in a finite probability 
space, they have to assume a constant value on each partition of the 
information structure It. It is convenient to introduce the following 
notation: 
= dt
i (
) , ω ∈Ajt
ω
dA
i 
jt 
i 
= St
i (
) , ω ∈Ajt
ω
SAjt 
i
where 
i dA
i 
jt and 
represent the constant values that the processes dt
i
SAjt
and St assume on the states that belong to the sets Ajt of each partition 
It. There is M0 = 1 value for dA
i 
j0 
i and SA
i 
j0 , Mt values for 
and SA
i 
jt 
dA
i 
jt
and MT = M values for dA
i 
jT and 
. The same notation and the same
SAjT
consideration can be applied to any process adapted to the filtration ℑt. 
Trading Strategies 
We have to define the meaning of trading strategies in this multiperiod 
setting. A trading strategy is a sequence of portfolios θ such that θt is the 
portfolio held at time t after trading. To ensure that there is no anticipa-
tion of information, each trading strategy θ must be an adapted process.
θ
The payoff dθ generated by a trading strategy is an adapted process dt 
with the following time dynamics: 

404 
The Mathematics of Financial Modeling and Investment Management 
θ
dt = 
(St + dt) – θtSt
θt – 1 
An arbitrage is a trading strategy whose payoff process is nonnega-
tive and not always zero. In other words, an arbitrage is a trading strat-
egy which is never negative and which is strictly positive for some 
instants and some states. Note that imposing the condition that payoffs 
are always nonnegative forbids any initial positive investment that is a 
negative payoff. 
A consumption process is any nonnegative adapted process. Mar-
kets are said to be complete if any consumption process can be obtained 
as the payoff process of a trading strategy with some initial investment. 
Market completeness means that any nonnegative payoff process can be 
replicated with a trading strategy. 
State-Price Deflator 
We will now extend the concept of state-price deflator to a multiperiod 
setting. A state-price deflator is a strictly positive adapted process πt 
such that the following set of M equations hold: 
T 
1
St
i = ----Et ∑
πjdj
i 
πt
j = t + 1 
In other words, a state-price deflator is a strictly positive process such 
that prices St
i are random variables equal to the conditional expectation 
of discounted payoffs with respect to the filtration ℑ. As noted above, in 
this finite-state setting a filtration is equivalent to an information struc-
ture It. Note that in the above stochastic equation—which is a set of M 
equations, one for each state, the term on the left, the prices St
i , is an 
adapted process that, as mentioned, assumes constant values on each set 
of the partition It. The term on the right is a conditional expectation 
multiplied by a factor 1/πt. The process πt is adapted by definition and, 
therefore, assumes constant values πAit on each set of the partition It. 
In this finite setting, conditional expectations are expectations com-
puted with conditional probabilities. Recall from Chapter 6 that condi-
tional expectations are adapted processes. Therefore they assume one 
value at t = 0, Mj values for t = j, and M values at the last date. 
To illustrate the above, let’s write down explicitly the above equa-
i
tion in terms of the notation dA
i 
jt and 
. Note first that
SAjt 

405 
Arbitrage Pricing: Finite-State Models 
P({
} ∩Akt) 
P({
})
ω
ω
P({
}
ω
Akt) = ----------------------------------- = ------------------- , if ω ∈Akt , 0 if ω ∉Akt
(
(
P Akt) 
P Akt) 
Given that the probability space is finite, 
(
P Ajt) = ∑pω 
ω ∈Ajt 
As we defined P({ω}) ≡pω the previous equation becomes 
P({
} ∩Akt) 
P({
}) 
pω
ω
ω
) = ----------------------------------- = ------------------- = ---------------------------
P({
}
ω
Akt 
(
(
P Akt) 
P Akt)
 
∑
pω
 
ω ∈Akt 
if ω ∈Akt , 0 if 
.
ω ∉Akt 
Pricing Relationships 
We can now write the pricing relationship as follows: 

 
T
i ω

i 
1 
= ---------
∑
P({
}
ω
ω
Akt)∑
πj(
)dj(
)
SAkt 
π
 
 

j = t + 1
Akt ω ∈Akt 

 

 
 
T
 
pω
1 
= ---------
∑
---------------------------∑
πj(
)di ω
 
π
ω ∈Akt 

∑ 
ω
j(
) 

j = t + 1 

pω 
Akt 
ω ∈Akt 
 
∈It , 1 ≤k ≤Mt
Akt 
The above formulas generalize to any trading strategy. In particular, 
if there is a state-price deflator, the market value of any trading strategy 
is given by 
1 
= ----E
θt × St 
πt 
πjdj 
θ 
j 
t 1
+
= 
T 
∑ 

406 
The Mathematics of Financial Modeling and Investment Management 
 
T

1
(θtSt)Akt = ---------
∑
P({
}
ω
Akt)∑
πj(
)dθ ω
 
π
ω
j (
) 
 
 

j = t + 1
Akt ω ∈Akt 

 

 
 
T
 
pω
1 
= ---------
∑
---------------------------∑
πj(
)dθ ω
 
π

j = t + 1
Akt ω ∈Akt 

 ∑
pω
ω
j (
)


ω ∈Akt 
 
i
It is possible to demonstrate that the payoff-price pair (dt, St
i ) admits 
no arbitrage if and only if there is a state-price deflator. These concepts 
and formulas generalize those of a one-period setting to a multiperiod 
setting. 
i
Given a payoff-price pair (dt
i , St) it is possible to compute the state-
price deflator, if it exists, from the previous equations. In fact, it is possi-
ble to write a set of linear equations in the πt, πt – 1 for each period. One 
can proceed backward from the period T to period 1 writing a homoge-
neous system of linear equations. As the system is homogeneous, one of 
the variables can be arbitrarily fixed; for example, the initial value π0 can 
be assumed equal to 1. If the system admits nontrivial solutions and if all 
solutions are strictly positive, then there are state-price deflators. 
Examples 
To illustrate the above, let’s write down explicitly the previous formulas 
for prices, extending the example of the previous section to a two-
period setting. We assume there are three securities and two periods, 
that is, three dates (0,1,2) and four states, indicated with the integers 
1,2,3,4, so that Ω= {1,2,3,4}. Assume that the information structure is 
given by the following partitions of events: 
Ii ≡(I0 ≡{ 
, 
A1 1 A2 1}, I2 ≡{
, , 
, , 
, , 
})
A1 0}, I1 ≡{
, , 
, 
A1 2 A2 2 A3 2 A4 2
, 
, 
1
2
3
4}, A1 1 = { + 
A2 1
3
4}
A1 0 = { +
+
+
 
, 
1
2}, 
, = { + 
A1 2 = { }, 
, = { }, A3 2 = { }, A4 2 = { }
, 
1
A2 2
2
, 
3
, 
4
where we use + to indicate logical union, so that, for example, {1 + 2} is 
the event formed by states 1 and 2. The interpretation of the above 
notation is the following. At time zero the world can be in any possible 
state, that is, the securities can take any possible path. Therefore the 

407 
Arbitrage Pricing: Finite-State Models 
partition at time zero is formed by the event {1 + 2 + 3 + 4}. At time 1, 
the set of states is partitioned into two mutually exclusive events, {1 + 2} 
or {3 + 4}. At time 2 the partition is formed by all individual states. 
Note that this is a particular example; different partitions would be log-
ically admissible. 
Exhibit 14.1 represents the above structure. Each security is character-
ized by a price process and a payoff process adapted to the information 
structure. Each process is a collection of three discrete random variables 
indexed with the time indexes 0,1,2. Each discrete random variable is a 4-
vector as it assumes as many values as states. However, as processes are 
adapted, they must assume the same value on each partition of the infor-
mation structure. Note also that payoffs are zero at date zero and prices 
are zero at date 2. Therefore, in this example, we can put together these 
vectors in two 3×4 matrices for each security as follows 
iS0( ) S1 
i ( ) 0
0 d1 
i ( ) d2( )
1
1
1
i 1
i 
2
i 
St
i ω
2
2
dt
i ω
0 d1 
i ( ) d2( )
2
(
)
 
{
 } ≡S0( ) S1 
i ( ) 0 ; 
(
)
 
{
 } ≡ 
iS0( ) S1 
i ( ) 0
0 d1 
i ( ) d2( )
3
3
3
i 3
iS0( ) S1 
i ( ) 0
0 d1 
i ( ) d2( )
4
4
4
i 4
The following relationships hold: 
i 
i
i
i
S0( ) = S0 
i ( ) = S0( ) = S0( ) = 
; S1( ) = S1 
i ( ) = 
;
1
2
i 3
i 4
SA1 0
1
,
, 
2
SA1 1
EXHIBIT 14.1 
An Information Structure with Four States and Three Dates 

408 
The Mathematics of Financial Modeling and Investment Management 
i
3
i 4
SA2 1
S1 
i ( ) = S1( ) = 
, 
i 
i
i
d1 
i ( ) = d1( ) = 
; d1 
i ( ) = d1( ) =
1
i 2
dA1 1
3
,
, 
4
dA2 1
where, as above, St
i (
) is the price of security i in state ω at moment t
ω
and dt
i (
) is the payoff of security i in state ω at time t with the restric-
ω
tion that processes must assume the same value on partitions. This is 
because processes are adapted to the information structure so that there 
is no anticipation of information. One must not be able to discriminate 
at time 0 events that will be revealed at time 1 and so on. 
Observe that there is no payoff at time 0 and no price at time 2 and 
that the payoffs at time 2 have to be intended as the final liquidation of 
the security as in the one-period case. Payoffs at time 1, on the other 
hand, are intermediate payments. Note that the number of states is cho-
sen arbitrarily for illustration purposes. Each state of the world repre-
sents a path of prices and payoffs for the set of three securities. To keep 
the example simple, we assume that of all the possible paths of prices 
and payoffs only four are possible. 
The state-price deflator can be represented as follows: 
( ) π1 1
( )
π0 1
( ) π2 1
( ) π2 2
( ) π1 2
( )
ω
(
)
 
{
 } ≡π0 2
( ) π1 3
( )
πt 
π0 3
( ) π2 3
( ) π1 4
( )
π0 4
( ) π2 4
π0 1
( ) = π0 3
( )
( ) = π0 2
( ) = π0 4
( ) = π1 2
( ) = π1 4
π1 1
( )  π1 3
( )  
A probability pω is assigned to each of the four states of the world. 
The probability of each event is simply the sum of the probabilities of its 
states. We can write down the formula for security prices in this way: 
i
i
i
1
SA2 2
3
SA
i 
4 2
4
= S2 
i ( ) =
= S2 
i ( ) =
= S2 
i ( ) =
= S2 
i ( ) = 0
SA1 2
, 
2
SA3 2
,
,
, 

409 
i 
2
Arbitrage Pricing: Finite-State Models 
1
i 2
= S1 
i ( ) = S1( )
SA1 1
, 
1 
= ------------[P A1 2 A1 1
( )d2 
i ( ) + P A2 2
)π2 1
1
(
, 
)π2 2
A1 1
( )d2 
i ( )]
(
, 
, 
,
πA1 1
, 
1 
= ------------ ----------------- π2 1
1
p2 
( )d2 
i ( )
p1 
( )d2 
i ( ) + ----------------- π2 2
2
π
p1 + p2 
p1 + p2
A1 1
, 
i 
3
i 4
= S1 
i ( ) = S1( )
SA2 1
, 
1 
= ------------[P A3 2 A2 1
( )d2 
i ( ) + P A4 2
)π2 3
3
(
, 
)π2 4
4
A2 1
( )d2 
i ( )]
(
, 
, 
,
πA2 1
, 
1 
= ------------ ----------------- π2 3
3
p4 
( )d2 
i ( )
p3 
( )d2 
i ( ) + ----------------- π2 4
4
π
p3 + p4 
p3 + p4
A2 1
, 
i
i 
+ π2 1
1
i 
+ π2 2
2
SA1 0 = 


 p1[πA1 1dA1 1
( )d2 
i ( )] + p2[πA1 1dA1 1
( )d2 
i ( )] 
, 
,
, 
,
, 

i
i
+ π2 3
3
A1 2dA1 2
( )d2 
i ( )] 
+ p3[πA1 2dA1 2
( )d2 
i ( )] + p4[π
, 
+ π2 4
4
,
, 
,
 
These equations illustrate how to compute the state-price deflator 
knowing prices, payoffs, and probabilities. They form a homogeneous sys-
tem of linear equations in π2(1), π2(2), π2(3), π2(4), πA1 1 , π
, , π
. 
, 
A2 1
A1 0
, 
p1di 
2( )π2 1
2
( )  SA
i 
1 1(p1 + p2 )π
, 
= 0
1
( ) + p2d2 
i ( )π2 2 – 
, 
A1 1
p3di 
2( )π2 3
4
( )  SA
i 
2 1(p3 + p4 )π
, 
= 0
3
( ) + p4d4 
i ( )π2 4 – 
, 
A2 1
1
( ) + p2di 
2( )π2 2
3
( ) + p4d4 
i ( )π2 4
p1di 
2( )π2 1
2
( ) + p3d2 
i ( )π2 3
4
( )  
i
+ (p1 + p2 )
i 
, πA1 1 + (p3 + p4 )
π
= 0
dA1 1
, 
dA2 3πA2 3 – SA
i 
1 0
A1 0
,
, 
,
, 
Substituting, we obtain 
p1di 
2( )π2 1
2
( )  SA
i 
1 1(p1 + p2 )π
, 
= 0
1
( ) + p2d2 
i ( )π2 2 – 
, 
A1 1

410 
The Mathematics of Financial Modeling and Investment Management
p3di 
2( )π2 3
4
( )  SA
i 
2 1(p3 + p4)π
, 
= 0
3
( ) + p4d4 
i ( )π2 4 – 
, 
A2 1
[(p1 + p2) i 
+ (p1 + p2)
i 
, ]πA1 1
, 
SA1 1
dA1 1
, 
+ [(p3 + p4) i 
+ (p3 + p4)
i 
]πA2 1 – i 
, π
= 0 
,
, 
, 
SA2 1
dA2 1
, 
SA1 0
A1 0
 This homogeneous system must admit a strictly positive solution to 
yield a state-price deflator. There are seven unknowns. However, as the 
system is homogeneous, if nontrivial solutions exist, one of the 
unknowns can be arbitrarily fixed, for example πA1 0 . Therefore, six 
,
independent equations are needed. Each asset provides two conditions, 
so a minimum of three assets are needed. 
To illustrate the point, we assume that all states (which are also 
events in this discrete example) have the same probability 0.25. Thus 
the events of the information structure have the following probabilities: 
the single event at time zero has probability 1, the two events at time 1 
have probability 0.5, and the four events at time 2 coincide with indi-
vidual states and have probability 0.25. Conditional probabilities are 
shown in Exhibit 14.2. 
For illustration purposes, let’s write the following matrices for pay-
offs for each security at each date in each state: 
0 15 50  
0 8  30  
0 5 38  
0 5 112 
d1 
i ω
d2 
i ω
(
)
 
{
 } ≡0 15 100  ; 
(
)
 
{
 } ≡0 8 120 ; 
(
)
 
{
 } ≡
d3 
i ω
0 20 70  
0 15 40  
0 8 42  
0 20 110  
0 15 140  
0 8 130 
We will assume that the state-price deflator is the following given pro-
cess: 
1 0.8 0.7 
(
)
 
{
 } ≡1 0.8 0.75 
ω
πt 
1 0.9 0.75 
1 0.9 0.8 
Each price is computed according to the previous equations. For exam-
ple, calculations related to asset 1 are as follows: 
1 1
1 2
1 3
1 4
S2( ) = S2( ) = S2( ) = S2( ) = 0 

EXHIBIT 14.2 
Conditional Probabilities 
411 
P A1 1 ∩A ,
{ +
(
, 
1 0) 
P 1
2} 
( 
,
∩A 1 0) 
P 3
4} 
P A2 1
,
{ +
P A1 1 A 1 0) = ---------------------------------------- = ------------------------------------------ = 0.5
) = ---------------------------------------- = ------------------------------------------ = 0.5
(
, 
, 
P A2 1
(
, 
A 1 0
, 
{ +
+
+
P A1 0) 
P 1
2
3
4} 
P A1 0
{ +
+
+
( 
, ) 
P 1
2
3
4}
(
, 
(
, 
1 0) 
P 1 
P A1 2 ∩A , 
{ }  
∩A 1 0) 
P 2
P A2 2
, 
{ }
(
, 
P A1 2 A 1 0) = ---------------------------------------- = ------------------------------------------ = 0.25
A 1 0) = ---------------------------------------- = ------------------------------------------ = 0.25
(
, 
, 
P A2 2
(
, 
, 
{ +
+
+
P A1 0) 
P 1
2
3
4} 
(
, 
{ +
+
+
P A1 0) 
P 1
2
3
4}
(
, 
(
, 
1 0) 
P 3 
P A3 2 ∩A , 
{ }  
∩A 1 0) 
P 4
P A4 2
, 
{ }
(
, 
P A3 2 A 1 0) = ---------------------------------------- = ------------------------------------------ = 0.25
) = ---------------------------------------- = ------------------------------------------ = 0.25
(
, 
, 
P A4 2
(
, 
A 1 0
, 
{ +
+
+
P A1 0) 
P 1
2
3
4} 
(
, 
{ +
+
+
P A1 0) 
P 1
2
3
4}
(
, 
(
, 
1 1) 
P 1 
∩A 2 1) 
P ∅
P A1 2 ∩A , 
{ }  
0.25
P A1 2
, 
{
}
(
, 
P A1 2 A 1 1) = ---------------------------------------- = ----------------------- = ----------- = 0.5
) = ---------------------------------------- = ----------------------- = 0
(
, 
, 
P A1 2
(
, 
A 2 1
, 
(
, 
{ +
P A1 1) 
P 1
2} 
0.5 
{ +
( 
, ) 
P 1
2}
P A2 1
 
P A2 2 ∩A , ) 
P 2 
∩A 2 1) 
P ∅
(
, 
1 1
{ }  
0.25
P A2 2
, 
{
}
(
, 
P A2 2 A 1 1) = ---------------------------------------- = ----------------------- = ----------- = 0.5
) = ---------------------------------------- = ----------------------- = 0
(
, 
, 
P A2 2
(
, 
A 2 1
, 
(
, 
{ +
P A1 1) 
P 1
2} 
0.5 
{ +
( 
, ) 
P 1
2}
P A2 1
(
, 
1 1) 
P ∅
P A3 2 ∩A , 
{
}
 
∩A 2 1) 
P 3
P A3 2
, 
{ }
(
, 
P A3 2 A 1 1) = ---------------------------------------- = ----------------------- = 0
) = ---------------------------------------- = ----------------------- = 0.5
(
, 
, 
P A3 2
(
, 
A 2 1
, 
{ +
P A1 1) 
P 1
2} 
(
, 
{ +
P A2 1) 
P 3
4}
(
, 
(
, 
1 1) 
P ∅
 
P A4 2 ∩A , 
{
}
 
∩A 2 1) 
P 4
P A4 2
, 
{ }
(
, 
P A4 2 A 1 1) = ---------------------------------------- = ----------------------- = 0
) = ---------------------------------------- = ----------------------- = 0.5
(
, 
, 
P A4 2
(
, 
A 2 1
, 
{ +
P A1 1) 
P 1
2} 
(
, 
{ +
P A2 1) 
P 3
4}
(
, 

412 
The Mathematics of Financial Modeling and Investment Management 
1
1 
= -------(0.5 × 0.7 × 50 + 0.5 × 075 × 100) = 68.75 
, 
SA1 1
0.8 
1
1 
= -------(0.5 × 0.75 × 70 + 0.5 × 0.8 × 110) = 78.05 
, 
SA2 1
0.9 
1
1 
(
(
= --[0.25 0.8 × 15 + 0.7 × 50) + 0.25 0.8 × 15 + 0.75 × 100)
SA1 0
1
, 
(
(
+ 0.25 0.9 × 20 + 0.75 × 70) + 0.25 0.9 × 20 + 0.8 × 110)] 
= 68.75 
2 1
2 2
2 3
2 4
S2( ) = S2( ) = S2( ) = S2( ) = 0 
2
1 
= -------(0.5 × 0.7 × 30 + 0.5 × 0.75 × 120) = 69.37 
, 
SA1 1
0.8 
2
1 
= -------(0.5 × 0.75 × 40 + 0.5 × 0.8 × 140) = 78.88 
, 
SA2 1
0.9 
2
1 
(
(
= --[0.25 0.8 × 8 + 0.7 × 30) + 0.25 0.8 × 8 + 0.75 × 120)
SA1 0
1
, 
(
(
+ 0.25 0.9 × 15 + 0.75 × 40) + 0.25 0.9 × 15 + 0.8 × 140)] 
= 73.2 
3 1
3 2
3 3
3 4
S2( ) = S2( ) = S2( ) = S2( ) = 0 
3
1 
= -------(0.5 × 0.7 × 38 + 0.5 × 0.75 × 112) = 69.12 
, 
SA1 1
0.8 
3
1 
= -------(0.5 × 0.75 × 42 + 0.5 × 0.8 × 130) = 75.27 
, 
SA2 1
0.9 
3
1 
(
(
= --[0.25 0.8 × 5 + 0.7 × 38) + 0.25 0.8 × 5 + 0.75 × 112)
SA1 0
1
, 
(
(
+ 0.25 0.9 × 8 + 0.75 × 42) + 0.25 0.9 × 8 + 0.8 × 130)] 
= 67.125 

413 
Arbitrage Pricing: Finite-State Models 
With the above equations we computed prices from payoffs and state-
price deflators. If prices and payoffs were given, we could compute state-
price deflators from the homogeneous system for state prices established 
above. Suppose that the following price processes were given: 
1 ω
(
)
 
{
 } =
St 
2 ω
(
)
 
{
 } =
St 
3 ω
(
)
 
{
 } =
St 
68.75 68.75 0 
68.75 68.75 0 
68.75 78.05 0 
68.75 78.05 0 
73.2 69.37 0 
73.2 69.37 0 
73.2 78.88 0 
73.2 78.88 0 
67.125 69.12 0 
67.125 69.12 0 
67.125 75.27 0 
67.125 75.27 0 
We could then write the following system of equations to compute state-
price deflators: 
( ) + 0.25 × 100 × π2 2
0.25 × 50 × π2 1
( ) – 68.75 × 0.5 × πA1 1 = 0 
, 
( ) + 0.25 × 110 × π2 2
0.25 × 70 × π2 1
( ) – 78.05 × 0.5 × πA1 1 = 0 
, 
(55 × 0.5 + 0.5 × 15) × πA1 1 + (70.25 × 0.5 + 0.5 × 20) × π
,
, 
A2 1
– 68.75 × πA1 0 = 0 
, 
( ) + 0.25 × 120 × π2 2
0.25 × 30 × π2 1
( ) – 69.37 × 0.5 × πA1 1 = 0 
, 
( ) + 0.25 × 140 × π2 2
0.25 × 40 × π2 1
( ) – 78.88 × 0.5 × πA1 1 = 0 
, 
(55.5 × 0.5 + 0.5 × 8) × πA1 1 + (71 × 0.5 + 0.5 × 15) × π
,
, 
A2 1
–73.2 × πA1 0 = 0 
, 

414 
The Mathematics of Financial Modeling and Investment Management 
( ) + 0.25 × 115 × π2 2
0.25 × 38 × π2 1
( ) – 69.12 × 0.5 × πA1 1 = 0 
, 
( ) + 0.25 × 130 × π2 2
0.25 × 42 × π2 1
( ) – 75.27 × 0.5 × πA1 1 = 0 
, 
(55 × 0.5 + 0.5 × 15) × πA1 1 + (70.25 × 0.5 + 0.5 × 20) × π
,
, 
A2 1
– 67.125 × πA1 0 = 0 
, 
It can be verified that this system, obviously, is solvable and returns the 
same state-price deflators as in the previous example. 
Equivalent Martingale Measures 
We now introduce the concept and properties of equivalent martingale 
measures. This concept has become fundamental for the technology of 
derivative pricing. The idea of equivalent martingale measures is the fol-
lowing. Recall from Chapter 6 that a martingale is a process Xt such 
that at any time t its conditional expectation at time s, s > t coincides 
with its present value: Xt = Et[Xs]. In discrete time, a martingale is a 
process such that its value at any time is equal to its conditional expec-
tation one step ahead. In our case, this principle can be expressed in a 
different but equivalent way by stating that prices are the discounted 
expected values of future payoffs. The law of iterated expectation then 
implies that price plus payoff processes are martingales. 
In fact, assume that we can write 
T 
St = Et ∑
dj 
j = t + 1 
then the following relationship holds: 
T
T 
St = Et ∑
dj = Et dt + 1 + Et + 1 
∑ 
dj 
= Et[dt + 1 + St + 1] 
j = t + 1 
j = t +
+
1
1
Given a probability space, price processes are not, in general, martin-
gales. However it can be demonstrated that, in the absence of arbitrage, 
there is an artificial probability measure in which all price processes, 
appropriately discounted, become martingales. More precisely, we will see 
that in the absence of arbitrage there is an artificial probability measure Q 
in which the following discounted present value relationship holds: 

--------
--------
----------------
----------------
----------------
----------------
--------
--------
----------------
------------------------------
415 
Arbitrage Pricing: Finite-State Models 
di 
St
i 
Q
Et 
j
= 
T 
∑
Rt j,
j = t + 1 
We can rewrite this equation explicitly as follows: 
Q
St
i = Et 
Q
= Et 
dj 
i 
Rt j, 
-
j 
t 1
+
= 
T 
∑
Et 
Q dt 1
+ 
i 
Rt t  1
+
, 
-
1 
Rt t  1
+
, 
-
dj 
i 
Rt 1
+ 
j,
j 
t 2
+
= 
T 
∑
+
= 
dt 1
+ 
i 
Rt t  1
+
, 
-
Et 1
+ 
Q 
Rt t  1
+
, 
-
dj 
i 
Rt j, 
-
j 
t 2
+
= 
T 
∑
+ 
Et 
Q dt 1
+ 
i 
St 1
+ 
i
+ 
Rt t  1
+
, 
= 
which shows that the discounted price plus payoff process is a martin-
gale. The terms on the left are the price processes, the terms on the right 
are the conditional expectations under the probability measure Q of the 
payoffs discounted with the risk-free payoff. 
The measure Q is a mathematical construct. The important point is 
that this new probability measure can be computed either from the real 
probabilities if the state-price deflators are known or directly from the 
price and payoff processes. This last observation illustrates that the con-
cept of arbitrage depends only on the structure of the price and payoff 
processes and not on the actual probabilities. As we will see later in this 
chapter, equivalent martingale measures greatly simplify the computa-
tion of the pricing of derivatives. 
Let’s assume that there is short-term risk-free borrowing in the sense 
that there is a trading strategy able to pay for any given interval (t,s) one 
sure dollar at time s given that (dtdt + 1...ds – 1)–1 has been invested at 
time t. Equivalently, we can define for any time interval (t,s) the payoff 
of a dollar invested risk-free at time t as Rt,s = (dtdt + 1...ds – 1). 
We now define the concept of equivalent probability measures. 
Given a probability measure P the probability measure Q is said to be 
equivalent to P if both assign probability zero to the same events. An 
equivalent probability measure Q is an equivalent martingale measure if 
all price processes discounted with Ri,j become martingales. More pre-
cisely, Q is an equivalent martingale measure if and only if the market 
value of any trading strategy is a martingale: 
j 
θ 
Rt j, 
-
T 
∑
d
θt × St = 
Q
Et 
j = t + 1 

416 
i 
The Mathematics of Financial Modeling and Investment Management 
Risk-Neutral Probabilities 
Probabilities computed according to the equivalent martingale measure 
Q are the risk-neutral probabilities. Risk-neutral probabilities can be 
explicitly computed. Here is how. Call qω the risk-neutral probability of 
state ω. Let’s write explicitly the relationship 
i 
Q dj
St
i = Et --------
Rt j, 
as follows: 
i ω 
i ω
qω 
T 
dj(
)
 
qω 
T 
dj(
)
 
= ∑
------------------
∑
-------------
= ∑
---------------------------
∑
-------------
SAkt 
( 
, 
ω ∈AktQ Akt) j = t + 1 Rt j
ω ∈Akt 
∑
qω
j = t + 1 Rt j

, 
ω ∈Akt 
The above system of equations determines the risk-neutral probabil-
ities. In fact, we can write, for each risky asset, Mt linear equations, 
where Mt is the number of sets in the partition It plus the normalization 
equation for probabilities. From the above equation, one can see that 
the system can be written as 
i ω
T 
dj(
)
 
∑
qω ∑
------------- – SA
i 
kt = 0 
∈ 
,
,
ω 
Ak t  
j = t + 1 Rt j
S 
∑qω = 1 
ω = 1 
This system might be determined, indetermined, or impossible. The 
system will be impossible if there are arbitrage opportunities. This sys-
tem will be indetermined if there is an insufficient number of securities. 
In this case, there will be an infinite number of equivalent martingale 
measures and the market will not be complete. 
Now consider the relationship between risk-neutral probabilities and 
state-price deflators. Consider a probability measure P and a nonnegative 
random variable Y with expected value on the entire space equal to 1. 
Define a new probability measure as Q(B) = E[1BY] for any event B and 
where 1B is the indicator function of the event B. The random variable Y 
is called the Radon-Nikodym derivative of Q and it is written 

417 
Arbitrage Pricing: Finite-State Models 
dQ
Y = --------
dP 
It is clear from the definition that P and Q are equivalent probabil-
ity measures as they assign probability zero to the same events. Note 
that in the case of a finite-state probability space the new probability 
measure is defined on each state and is equal to 
qω = Y ω
(
)pω 
Suppose πt is a state-price deflator. Let Q be the probability measure 
defined by the Radon-Nikodym derivative: 
πTR0, T 
= ------------------
ξT 
π0 
The new state probabilities under Q are the following:  
πT ω 
(
)R0, T 
qω = --------------------------- pω
π0 ω
(
)
 
Define the density process ξt for Q as ξ = Et[ξT]. As ξ = Et[ξT] is an
t
t 
adapted process, we can write: 
pω 
(
)R0, T
ξT
Akt 
ω ∈AktP Akt) 
(
) = ∑
--------------------------------------------
(Et[
])
= ξAkt = ∑
-----------------ξT ω
pω
πT ω 
( 
(
)
 
( 
ω ∈AktP Akt)
π0 ω
πAktR0, t 1 
pω 
(
)]
, 
= ---------------------
= ------------------------------ ∑
-----------------πT[π0 ω
Rt T
πAktR0, t 
π0 ω
(
(
) πAkt ω ∈AktP Akt) 
π0 
As Rt,s = (dtdt + 1...ds – 1) is the payoff at time s of one dollar invested in 
a risk-free asset at time t, s > t, we can then write the following equations: 
1
1 = ----Et[π
, ]
sRt s
πt 
Therefore, 

418 
1 
The Mathematics of Financial Modeling and Investment Management 
pω
1
1 = ---------
∑
P({
}
ω
ω Rt s
= ---------
∑
-----------------π (
)Rt s
ω
Akt)πs(
)
,
π
π
ω ∈AktP Akt)
s
(
, 
Akt 
Akt
ω ∈Akt 
1 ≤k ≤Mt 
Substituting in the previous equation, we obtain, for each interval (t,T), 
πAktR0, t
ξAkt = (Et[
])
= ---------------------
ξT
Akt 
πA10 
which we can rewrite in the usual notation as 
πtR0, t
ξT
ξt = Et[
] = ---------------
π10 
We can now state the following result. Consider any ℑj-measurable 
variable xj. This condition can be expressed equivalently stating that xj 
assumes constant values on each set of the partition Ij. Then the follow-
ing relationship holds: 
P 1
Et xj
Q[
] = Et ----[ξjxj]
ξt 
To see this, consider the following demonstration, which hinges on the 
fact that xj assumes a constant value on each Ahj and, therefore, can be 
taken out of sums. In addition, as demonstrated above, from 
1
1 = ----Et[π
, ]
sRt s
πt 
the following relationship holds: 
( 
ω
, 
P Akt)πAkt = ∑
pωπ (
)Rt s
s 
ω ∈Akt 
1 ≤k ≤Mt 

-----------------------------------------------------------
419 
Arbitrage Pricing: Finite-State Models 
Q 
(
)R0, T
(Et [
])Akt = ∑ 
qω
ω
pω
πT ω
ω
xj
------------------ xj(
) = ∑
------------------ --------------------------- xj(
)
 
ω ∈AktQ Akt) 
ω ∈AktQ Akt)
π0 ω
( 
(
(
)
 
1 
, pωπT ω
ω
= ------------------ ∑
∑
R0, jRj T
(
)xj(
)
 
(
π0 ω
(
)
Q Akt)Ahj ⊂Akt ω ∈Ahj 
1 
xAhjR0, j 
, pωπT ω
= ------------------ ∑ 
-------------------- ∑Rj T
(
)
(
π0 ω
(
)
 ω ∈Ahj 
Q Akt)Ahj ⊂Akt 
(
1 
xAhjR0, jπAhjP Ahj) 
= ------------------ ∑ 
-------------------------------------------------
( 
π0 ω
(
)
Q Akt)Ahj ⊂Akt 
1 
= ------------------ ∑
[xAhj ξAhjP Ahj)]
(
(
Q Akt)Ahj ⊂Akt 
(
1 
xAhj ξAhjP Ahj) 
1 
P(ξjx )
= ---------
∑
------------------------------------- = ---------[Et 
j Akt]
P Akt)
ξAkt
(
ξAkt Ahj ⊂Akt 
Let’s now apply the above result to the relationship: 
T 
,
1 
π0 
T 
πjRt j dj
i 
St
i = ----Et ∑
πjdj
i = -----Et ∑
----------------------
πt
j = t + 1 
πt
j = t + 1 π0 Rt j, 
π0 
T 
πjR0, j dj
i 
Qdj
i  
= ---------------Et ∑
-----------------------
= Et -------- 
Rt j
πtR0, j
j = t + 1 π0 Rt j
,
, 
We have thus demonstrated the following results: There is no arbitrage 
if and only if there is an equivalent martingale measure. In addition, πt 
is a state-price deflator if and only if an equivalent martingale measure 
Q has the density process defined by 
πtR0, t 
= ---------------
ξt 
π0 
In addition, it can be demonstrated that, if there is no arbitrage, 
markets are complete if and only if there is a unique equivalent martin-
gale measure. 

420 
The Mathematics of Financial Modeling and Investment Management 
Examples 
To illustrate the above we now proceed to detail the calculations for the 
previous example of three assets, three dates, and four states. Let’s first 
write the equations for the risk-free asset: 
1 
pω
1 = ---------
∑
-----------------π (
)Rt s
ω
πAkt ω ∈AktP Akt)
s
(
, 
1  
p1
1 = --------------------------- π2 1 R1 2
p2 
( )R1 2
 
( )
, + ----------------- π2 2
,
πA11 p1 + p2 
p1 + p2 
 
1  
p3
1 = --------------------------- π2 3 R1 2
p4 
( )R1 2
 
( )
, + ----------------- π2 4
,
πA21 p3 + p4 
p3 + p4 
 
1 
( )
, + p2π2 2 R0 2 + p3π2 3 R0 2 + p4π2 4 R0 2]
1 = ----------[p1π2 1 R0 2
( )
, 
( )
, 
( )
,
πA10 
πA11 = π1 1
( )
( ) = π1 2
πA21 = π1 3
( )
( ) = π1 4
πA10 = π0 1
( ) = π0 3
( )
( ) = π0 2
( ) = π0 4
We can now rewrite the pricing relationships for the other risky 
assets as follows: 
At date 2, prices are zero: S2 
i = 0 . 
At date 1, the relationship 
d2 
i 
S1 
i = E1 -----------
R1 2
, 
holds. In fact, we can write the following: 

421 
Arbitrage Pricing: Finite-State Models 
Si 
1( ) = Si 2
= Si 1
1( )
A1 1
, 
1 
= ------------- [P A ,
( 
, 
( )di 1
( 2 2
A1 1)π2 1
2( ) + P A , 
A1 1
( )di 2
)π2 2
2( )]
1 2
,
π1 2
( )  
1  
p1 
di 1
2 
di 2
2( )  
p
2( ) 
= ------- ----------------- π2 1
1 2-------------- + ----------------- π2 2
( )R , 
( )R , --------------
1 2
, 
p1 + p

π11p1 + p2 
R1 2
2 
R1 2
, 
di 1
2( )
2( )  
di 2
= Q A1 2 A1 1)-------------- + Q A ,
( 
)--------------
(
, 
, 
2 2 A1 1
, 
, 
R1 2
R1 2
, 
q
d2 
i ( )  
q
d2 
i ( )
2
1
1
2 
= ----------------- -------------- + ----------------- -------------- 
q1 + q
, 
q1 + q 
2 R1 2
2 R1 2
, 
Si 
i 3
4
= S1( ) = S1 
i ( )
A2 1
, 
di 3
2( )
2( )  
di 4
= Q A3 2 A1 1)-------------- + Q A ,
( 
)--------------
(
, 
, 
4 2 A1 1
, 
, 
R1 2
R1 2
, 
q
d2 
i ( )  
q
d2 
i ( )
4
3
3
4 
= ----------------- -------------- + ----------------- --------------
q3 + q
, 
q3 + q
4 R1 2
4 R1 2
, 
At date 0, the relationship 
d1 
i
d2 
i 
S0 
i = E0 ----------- + -----------
,
, 
R0 1
R0 2
holds. In fact we can write the following: 
Si 
i 1
2
i 3
i 
= S0( ) = S0 
i ( ) = S0( ) = S0( )
4
A1 0
, 
 
p1[π1 1
1 + 
( )d2 
i ( )] 


( )di 
1( )  π2 1
1
 
( )di 2 + 
( )di 2
 
1  + p2[π1 2
1( )  π2 2
2( )] 
= ----------
 
π
 + p3[π1 3
1( )  π2 3
( )]
( )di 3 + 
( )di 3 
A10  
2 
 
( )di 4 + 
( )di 4
 + p4[π1 4
1( )  π2 4
2( )]
 
 

422 
The Mathematics of Financial Modeling and Investment Management 
π1 1
, 
1
( )R0 2d2 
i ( )
( )R0 1d1 
i ( )  π2 1
, 
1
= p1 ---------------------------------------- + ----------------------------------------
πA1 0
R0 1
πA1 0
R0 2
,
,
,
, 
π1 2
, 
2
( )R0 2d2 
i ( )
( )R0 1d1 
i ( )  π2 2
, 
2
+ p2 ---------------------------------------- + ---------------------------------------- 
πA1 0
R0 1
πA1 0
R0 2  
,
,
,
, 
π1 3
, 
3
( )R0 2d2 
i ( )
( )R0 1d1 
i ( )  π2 3
, 
3
+ p3 ---------------------------------------- + ---------------------------------------- 
πA1 0
R0 1
πA1 0
R0 2  
,
,
,
, 
π1 4
, 
4
( )R0 2d2 
i ( )
( )R0 1d1 
i ( )  π2 4
, 
4
+ p4 ---------------------------------------- + ---------------------------------------- 
πA1 0
R0 1
πA1 0
R0 2  
,
,
,
, 

 
( )R0 1d1 
i ( ) 1 
p1 
( )
, 
π1 1
, 
1
p2 
( )
,
 
= p1----------------------------------------------- ----------------- π2 1 R1 2 + ----------------- π2 2 R1 2  
 
 
,
, 
p1 + p2 
 

πA1 0
R0 1 π11 
p1 + p2 

 

( )R0 1d1 
i ( ) 1 
p1 
( )
, 
π1 2
, 
2
p2 
( )
, 
+ p2----------------------------------------------- ----------------- π2 1 R1 2 + ----------------- π2 2 R1 2  
 
 
,
, 
p1 + p2 
 

πA1 0
R0 1 π21 
p1 + p2 

 
( )R0 1d1 
i ( ) 1 
p3 
( )
, 
π1 3
, 
3
p4 
( )
,
 
+ p3----------------------------------------------- ----------------- π2 3 R1 2 + ----------------- π2 4 R1 2  
 
 
,
, 
p3 + p4 
 

πA1 0
R0 1 π31 
p3 + p4 

 
( )R0 1d1 
i ( ) 1 
p3 
( )
, 
π1 4
, 
4
p3 
( )
,
 
+ p4----------------------------------------------- ----------------- π2 3 R1 2 + ----------------- π2 4 R1 2  
 
 
,
, 
p3 + p4 
 

πA1 0
R0 1 π41 
p3 + p4 
1
2
3
4
d2 
i ( )  
d2 
i ( )  
d2 
i ( )  
d2 
i ( )
+ q1-------------- + q2-------------- + q3-------------- + q4-------------- 
R0 2
R0 2
R0 2
R0 2  
,
,
,
, 

------------- --------------------
--------------------
------------- --------------------
--------------------
423 
Arbitrage Pricing: Finite-State Models 
d1 
i 1
( )  
R0 1
, 
-
p1π2 1
( )  
πA1 0
, 
-R0 2
, 
p2π2 2
( )  
πA1 0
, 
-R0 2
, 
+ 
d2 
i 3
( )  
R0 1
, 
-
p3π2 3
( )  
πA1 0
, 
-R0 2
, 
p4π2 4
( )  
πA1 0
, 
-R0 2
, 
+
+
= 
1
2
3
4
d2 
i ( )  
d2 
i ( )  
d2 
i ( )  
d2 
i ( )
+ q1-------------- + q2-------------- + q3-------------- + q4--------------
R0 2
R0 2
R0 2
R0 2
,
,
,
, 
1
2
3
4
d1 
i ( )  
d1 
i ( )  
d1 
i ( )  
d1 
i ( )
= q1-------------- + q2-------------- + q3-------------- + q4--------------
R0 1
R0 1
R0 1
R0 1
,
,
,
, 
1
2
3
4
d2 
i ( )  
d2 
i ( )  
d2 
i ( )  
d2 
i ( )
+ q1-------------- + q2-------------- + q3-------------- + q4--------------
R0 2
R0 2
R0 2
R0 2
,
,
,
, 
PATH DEPENDENCE AND MARKOV MODELS 
The value of a derivative instrument might depend on the path of its past 
values. Consider a lookback option on a stock—that is, a derivative 
instrument on a stock whose payoff at time t is the maximum difference 
between the price of the stock and a given value K at any moment prior to 
t. Call Vt the payoff of the lookback option at time t. We can then write: 
Vt = max (Sk – K)+ 
0 
< 
≤ k
t
The notation (Sk – K)+ means Sk – K if the difference is positive, 0 oth-
erwise, that is, (Sk – K)+ = max(Sk – K, 0) . Because its value depends 
on the entire path taken by the underlying stock, a lookback option is a 
path-dependent security. 
An adapted process Xt is said to be a Markov process if its condi-
tional distribution at time t depends only on the value of the process at 
time t – 1 and not on the value of the process at dates t – 2, t – 3, .... The 
Markov property can be formally stated as follows: 
P Xt
( 
) = P Xt
( 
, 
, …, X0)
Xt – 1 
Xt – 1 Xt – 2 
THE BINOMIAL MODEL 
Let’s now introduce the simple but important multiperiod finite-state 
model known as the binomial model. The binomial model is important 

424 
The Mathematics of Financial Modeling and Investment Management 
because it gives a simple and mathematically tractable model of stock 
price behavior that tends, in the limit of a zero time step, to a Brownian 
motion. We introduce a market populated by one risk-free asset and by 
one or more risky assets whose price(s) follow(s) a binomial or trino-
mial model. In the next section we will see how to compute the price of 
derivative instruments in this market. 
In the binomial model of stock prices, we assume that at each time 
step the stock price will assume one of two possible values. This is a 
restriction of the general multiperiod finite-state model described in the 
previous sections and in Chapter 6 on probability. The latter is, as we 
have seen in the previous section, a hierarchical structure of partitions 
of the set of states. The number of sets in any partition is arbitrary, pro-
vided that partitions grow more refined with time. 
The binomial model assumes that there are two positive numbers, d 
and u, such that 0 < d < u and such that at each time step the price St of 
the risky asset changes to dSt or to uSt. In general one assumes that 0 < d 
< 1 < u so that d represents a price decrease (a movement down) while u 
represents a price increase (a movement up). It is often required that 
1
d = --
u 
In this case an equal number of movements up and down leave prices 
unchanged. The binomial model is a Markov model as the distribution 
of St clearly depends only on the value of St – 1. 
A binomial model can be graphically represented by a tree. For 
example, Exhibit 14.3 shows a binomial model for three periods. A 
binomial model over T time steps, from 0 to T, produces a total of 2T 
paths. Therefore, the corresponding space of states has 2T states. How-
ever, the number of different final prices ST = ukdT – kS0, k = 0,1,...,T is 
determined solely by the number of u and d in each path and increases 
by 1 at each time step; there are as many final prices as dates. For exam-
ple, the model in Exhibit 14.3 shows three final prices and four states. 
Note that there is a simple relationship between the numbers d and 
u and returns. In fact, we can write, 
– St 
uSt – St
St + 1
Rt(up) = ---------------------- = ------------------ = u – 1 
St 
St 
Rt(down) = d – 1 

425 
Arbitrage Pricing: Finite-State Models 
EXHIBIT 14.3 
Binomial Model: The Figure Illustrates a Binomial Tree with Three 
Dates, Three Final Prices, and Four States: uu,ud,du,dd 
Real probabilities of states are typically constructed from the proba-
bilities of a movement up or down. Call p the probability of a move-
ment up; 1 – p is thus the probability of a movement down. Suppose 
that the state s, which is identified by a price path, has k movements up 
and T – k movements down. The probability of the state s is 
T
k
– 
ps = pk(1 – p)
Consider the final date T. Each of the possible final prices ST = ukdT – kS0, 
k = 0,1,...,T can be obtained through 
T
T!
= -------------------------
k
– 
 k!(T
k)! 
paths with k movements up and T – k movements down. The probabil-
ity distribution of final prices is therefore a binomial distribution: 
( 
– 
T 
T
k
– 
P ST = ukdT
kS0) = pk(1 – p)

k
Following the same reasoning, one can demonstrate that at any interme-
diate date the probability distribution of prices is a binomial distribu-
tion as follows: 

426 
The Mathematics of Financial Modeling and Investment Management 
( 
– 
y 
t
k
– 
P St = ukdt
kS0) = pk(1 – p)

k
Next introduce a risk-free security. In the setting of a binomial 
model, a risk-free security is simply a security such that d = u =1 + r 
where r > 0 is the positive risk-free rate. To avoid arbitrage it is clearly 
necessary that d < 1 + r < u. In fact, if the interest rate is inferior to both 
the up and down returns, one can make a sure profit by buying the risky 
asset and shorting the risk-free asset. If the interest rate is superior to 
both the up and down returns, one can make a sure profit by shorting 
the risky asset and buying the risk-free asset. Denote by bt the price of 
the risk-free asset at time t. From the definition of price movement in 
the binomial model we can write: bt = (1 + r)tb0. 
Risk-Neutral Probabilities for the Binomial Model 
Let’s now compute the risk-neutral probabilities. In the setting of bino-
mial models, the computation of risk-neutral probabilities is simple. In 
fact we have to impose the condition: 
Q
qt = Et [qt + 1] 
which we can explicitly write as follows: 
quSt + (1 – q)dSt
St = --------------------------------------------
1 + r 
1 + r = qu + d – qd 
1 + r
d
– 
q = --------------------
u
d
– 
u – 1 – r
1 – q = --------------------
u
d
– 
q
As we have assumed 0 < d < 1 + r < u, the condition 0 <
< 1 holds. 
Therefore we can state that the unique risk-neutral probabilities are 
1 + r
d
– 
q = --------------------
u
d
– 

427 
Arbitrage Pricing: Finite-State Models 
u – 1 – r
1 – q = --------------------
u
d
– 
The binomial model is complete and arbitrage free. 
Suppose that there is more than one risky asset, for example two 
risky assets, in addition to the risk-free asset. At each time step each 
risky asset can go either up or down. Therefore there are four possible 
joint movements at each time step: uu,ud,du,dd that we identify with 
the states 1,2,3,4. Four probabilities must be determined at each time 
step; four equations are therefore needed. Two equations are provided 
by the martingale conditions: 
1
1
1
1 
1 
q1uSt + q2uSt + q3uSt + q4uSt
St = ----------------------------------------------------------------------------------
1 + r 
2
2
2
2 
2 
q1uSt + q3uSt + q2uSt + q4uSt
St = ----------------------------------------------------------------------------------
1 + r 
A third equation is provided by the fact that probabilities must sum to 
1. The fourth condition, however, is missing. The model is incomplete. 
The problem of approximating price processes when there are two 
stocks and one bond and where the stock prices follow two correlated 
lognormal processes has long been of interest to financial economists. 
As seen above, with two stocks and one bond available for trading, mar-
kets cannot be completed by dynamic trading. This is not the case in the 
continuous-time model, in which markets can be completed by continu-
ous trading in the two stocks and the bond. Different solutions to this 
problem have been proposed in the literature.1 
VALUATION OF EUROPEAN SIMPLE DERIVATIVES 
Consider a market formed by a risky asset (a stock) that follows the 
binomial model plus a risk-free asset. As we have seen in the previous 
section, this market is complete and its risk-neutral probabilities are 
1 Hua He, “Convergence from Discrete- to Continuous-Time Contingent Claims 
Prices,” Review of Financial Studies 3, no. 4 (1990), pp. 523–546. 

428 
The Mathematics of Financial Modeling and Investment Management 
1 + r
d
– 
q = --------------------
u
d
– 
u – 1 – r
1 – q = --------------------
u
d
– 
Let’s introduce in this market a derivative instrument. The condition 
of absence of arbitrage univocally determines the price of this third secu-
rity. Consider first a European call option on the stock with expiration 
date τ < T and with exercise price K > 0. Recall from Chapter 2 that a 
European call option is a security that gives its holder the right but not 
the obligation to purchase the stock at time τ at price K. Therefore, the 
payoff process of the option is zero before time τ and, at time τ, is 
Cτ
τ = max(Sτ – K, 0) 
Let’s compute the value of the option Ct 
τ at any time 0 < t < τ. Given 
that the binomial model is complete, the value Ct 
τ can be computed as 
the discounted payoff at time t using the risk-neutral probabilities. 
Using the formulas of the previous sections, we can therefore write 
Cτ
τ
Q
Ct 
τ = Et ------------------------
(1 + r)τ – t 
This formula can be explicitly computed as follows. The distribution 
of the payoff of the option at time τ under the risk-neutral probabilities is 
the following: 
P Cτ
τ = (ukdτ – t – k 
+
[ 
S0 – K) ] = 
τ 
k 
– t 

 qk(1 – q)τ – t – k 
Therefore the conditional expectation under the risk-neutral probabili-
ties becomes 
τ – t 
τ 
1 
τ – t – k
Ct = ------------------------ ∑(ukdτ – t – kS0 – K)
+ 

τ 
k 
– t 

 qk(1 – q)
(1 + r)τ – tk = 0 

429 
Arbitrage Pricing: Finite-State Models 
More generally, we give the following definition: A simple European 
derivative instrument with expiration time τ is a financial instrument 
whose payoff is zero for 0 ≤ t < τ and is an ℑτ-measurable random vari-
able Vτ at time τ. Recall from Chapter 6 that in this finite-state context, a 
variable is ℑt-measurable if it assumes a constant value on each of the sets 
of the partition It. 
Given the risk-neutral probability measure Q, the value at time t of 
the simple European derivative instrument can be computed as follows: 
Q
Vτ
Vt = Et ------------------------
( 1 + r)τ – t 
If the underlying stock is represented by a binomial model, the value of 
the European derivative instrument can be explicitly computed as: 
τ – t 
1 
τ – t – k
Vt = ------------------------ ∑ Vτ

τ – t qk( 1 – q)
( 1 + r)τ – tk = 0 
k  
VALUATION OF AMERICAN OPTIONS 
In order to define American options we have first to define the concept 
of a stopping time. In fact, American options can be exercised at any 
moment prior to expiration date in function of some exercising policy. 
These policies define a stopping time. A stopping time is a random time 
s, i.e., a random variable s such that 
{ω ∈ Ω; s ω
(
)
 = k} ∈ℑk 
Consider now an adapted process Xt and a stopping time s. Define a 
s
payoff process ds as dt
s = 0 if t ≠ s and dτ = X . Under the risk-neutral
s 
probabilities we can write a valuation formula: 
Q 
Xs
Vt
s = Et ------------------------
– 
(1 + r)s
t
These formulas allow the valuation of American securities in complete 
markets. 

-------------
430 
The Mathematics of Financial Modeling and Investment Management 
ARBITRAGE PRICING IN A DISCRETE-TIME, 
CONTINUOUS-STATE SETTING 
Let’s now discuss the discrete-time, continuous-state setting. This is an 
important setting as it is, for example, the setting of the Arbitrage Pric-
ing Theory (APT) Model that we will discuss later in this chapter. 
As in the previous discrete-time, discrete-state setting, we use the 
probabilistic concepts developed in Chapter 6. The economy is repre-
sented by a probability space (Ω,ℑ,P) where Ω is the set of possible 
states, ℑ is the σ-algebra of events (formed, in this continuous-state set-
ting, by a nondenumerable number of events), and P is a probability 
function. As the number of states is infinite, the probability of each state 
is zero and only events, in general, formed by nondenumerable states, 
have a finite probability. There are only a finite number of dates from 0 
to T. Recall from Chapter 6 that the propagation of information is rep-
resented by a finite filtration ℑt, t = 0,1,...,T. In this case, the filtration ℑt 
is not equivalent to an information structure It. 
Each security i is characterized by a payoff process dt
i and by a
i
i
price process St
i . In this continuous-state setting, dt and St are formed 
ω
i ω
by a finite number of continuous variables. As before, dt
i (
)
 and St(
)
 
are, respectively, the payoff and the price of the i-th asset at time t, 0 ≤ t 
≤ T and in state ω ∈ Ω. Following Chapter 6, all payoffs and prices are 
stochastic processes adapted to the filtration ℑ. 
To develop an intuition for continuous-state arbitrage pricing, con-
sider the previous multiperiod, finite-state case with a very large number 
M of states, M>>N where N is the number of securities. Recall from our 
earlier discussion in this chapter that risk-neutral probabilities can be 
computed solving the following system of linear equations: 
qω 
ω 
Ak t
, 
∈ ∑ 
j 
dj 
i ω
(
)
 
Rt j, 
-
SAkt 
i 
– 
t + 1
= 
T 
∑ 
= 0 
M 
∑ qω = 1 
ω = 1 
Recall also that at each date t the information structure It partitions the 
set of states into Mt subsets. Each partition therefore yields N × Mt 
equations and the system is formed by a total of 

431 
Arbitrage Pricing: Finite-State Models 
T – 1 
N × ∑ Mt 
t = 0 
equation plus the probability normalizing equation. Consider that the 
previous system can be broken down, at each date t, into separate 
blocks formed by N equations (one for each asset) of the following type: 
T 
dj
i 
*
∑ qω ∑ -------- = SAkt 
ω ∈ Akt 
j = t + 1 Rt j, 
* 
qω 
qω = ----------------------
∑ qω 
ω ∈ Akt 
Each of these systems can be solved individually for the conditional 
*
probabilities qω . Recall that a system of this type admits a solution if 
and only if the coefficient matrix and the augmented coefficient matrix 
have the same rank. If the system is solvable, its solution will be unique 
if and only if the number of unknowns is equal to the rank of the coeffi-
cient matrix. 
If the above system is not solvable then there are arbitrage opportuni-
ties. This occurs if the payoffs of an asset are a linear combination of those 
of other assets, but its price is not the same linear combination of the prices 
of the other assets. This happens, in particular, if two assets have the same 
payoff in each state but different prices. In these cases, in fact, the rank of 
the coefficient matrix is inferior to the rank of the augmented matrix. 
Under the assumption 
T – 1 
M
N
 
× ∑ Mt
» 
t = 0 
this system, if it is solvable, will be undetermined. Therefore, there will 
be infinite equivalent risk-neutral probabilities and the market will not 
be complete. Going to the limit of an infinite number of states, the 
above reasoning proves, heuristically, that a discrete-time continuous-
state market with a finite number of securities is inherently incomplete. 
In addition, there will be arbitrage opportunities only if the random 
variable that represents the payoff of an asset is a linear combination of 
the random variables that represent the payoffs of other assets, but the 
random variables that represent prices are not in the same relationship. 

432 
The Mathematics of Financial Modeling and Investment Management 
The above discussion can be illustrated in the case of multiple 
assets, each following a binomial model. If there are N linearly indepen-
dent assets, the price paths in the interval (0,T) will form a total of 2NT 
states. In a binomial model, we can limit our considerations to one time 
step as the other steps are identical. In one step, each price St
i at time t 
i 
idi
can go up to Stui or down to St 
at time t + 1. Given the prices 
St
i
1
2 
N
{
} ≡{St , St , …, St } at time t, there will be, at the next time step, 2N 
1 
2
2 
N
N 
i
i
possible combinations {St w 1 , St w , …, St w } , w  = u  or di . 
Suppose that there are 2NT states and that each combination of 
prices identifies a state. This means that at each date t the information 
structure It partitions the set of states into 2Nt subsets. Each set of the 
partition is partitioned into 2N subsets at the next time step. This yields 
2N(t+1) subsets at time t + 1. 
Note that this partitioning is compatible with any correlation struc-
ture between the random variables that represent prices. In fact, correla-
tions depend on the value of the probability assigned to each state while 
the partitioning we assume depends on how different prices are assigned 
to different states. 
Risk-neutral probabilities qi, i = 1,2,...,2N can be determined solving 
the following system of martingale conditions: 
2N 
i
j
i
∑qjStwi( ) = St 
j = 1 
2N 
∑qj = 1 
j = 1 
j = 1,2,...,2N , i = 1,2,...,N 
which becomes, after dividing each equation by St
i , the following: 
2N 
∑qjwi( ) = 1
j
j = 1 
2N 
∑qj = 1 
j = 1 
i
where wi(j) = u  or di for asset i in state j. 

433 
Arbitrage Pricing: Finite-State Models 
It can be verified that, under the previous assumptions and provided 
prices are positive, the above system admits infinite solutions. In fact, as 
N + 1 < 2N, the number of equations is larger than the number of 
unknowns. Therefore, if the system is solvable it admits infinite solu-
tions. To verify that the system is indeed solvable, let’s choose the first 
asset and partition the set of states into two events corresponding to the 
movement up or down of the same asset. Assign to these events proba-
bilities as in the binomial model
1 
1
1 – r + dt 
1 
qt = ----------------------- and 1 – qt
1
1 
ut – dt 
Choose a second asset and partition each of the previous events into 
two events corresponding to the movements up or down of the second 
asset. We can now assign the following probabilities to each of the fol-
lowing four events: 
1
2 
2 
1
2
2
1 
qt qt , qt 
1(1 – qt ), (1 – qt )qt , (1 – qt )(1 – qt ) 
It can be verified that these numbers sum to one. The same process 
can be repeated for each additional asset. We obtain a set of positive 
numbers that sum to one and that satisfy the system by construction. 
There are infinite other possible constructions. In fact, at each step, we 
could multiply probabilities by “correlation factors” (i.e., numbers that 
form a 2 × 2 correlation matrix) and still obtain solutions to the system. 
We can therefore conclude that a system of positive binomial prices 
such as the one above plus a risk-free asset is arbitrage-free and forms 
an incomplete market. Recall from Chapter 8 that if we let the number 
of states tend to infinity, the binomial distribution converges to a nor-
mal distribution. We have therefore demonstrated heuristically that a 
multivariate normal distribution plus a risk-free asset forms an incom-
plete and arbitrage-free market. Note that the presence of correlations 
does not change this conclusion. 
Let’s now see under what conditions this conclusion can be changed. 
Go back to the multiple binomial model, assuming, as before, that there 
are N assets and T time steps. There is no logical reason to impose that 
the number of states be 2NT. As we can consider each time step sepa-
rately, suppose that there is only one time step and that there are a num-
ber of states less than or equal to the number of assets plus 1: M ≤ N + 1. 
In this case, the martingale condition that determines risk-neutral proba-
bilities becomes: 

434 
The Mathematics of Financial Modeling and Investment Management 
M 
j
∑qjwi( ) = 1 
j = 1 
N 
∑qj = 1 
j = 1 
There are M equations and N + 1 unknowns with M ≤N + 1. This 
system will either determine unique risk-neutral probabilities or will be 
unsolvable. Therefore, the market will be either complete and arbitrage-
free or will exhibit arbitrage opportunities. Note that in this case we 
cannot use the constructive procedure used in the previous case. 
What is the economic meaning of the condition that the number of 
states be less than or equal to the number of assets? To illustrate this 
point, assume that the number of states is M = 2K ≤N + 1. This means 
that we can choose K assets whose independent price processes identify 
all the states as in the previous case. Now add one more asset. This asset 
will go up or down not in specific states but in events formed by a num-
ber of states. Suppose it goes up in the event A and goes down in the 
event B. These events are determined by the value of the first K assets. In 
other words, the new asset will be a function of the first K assets. An 
interesting case is when the new asset can be expressed as a linear func-
tion of the first K assets. We can then say that the first K assets are fac-
tors and that any other asset is expressed as a linear combination of the 
factors. 
Consider that, given the first K assets, it is possible to determine 
state-price deflators. These state-price deflators will not be uniquely 
determined. Any other price process must be expressed as a linear com-
bination of state-price deflators to avoid arbitrage. If all price processes 
are arbitrage-free, the market will be complete if it is possible to deter-
mine uniquely the risk-neutral probabilities. 
If we let the number of states become very large, the number of 
assets must become large as well. Therefore it is not easy to develop 
simple heuristic arguments in the limit of a large economy. What we can 
say is that in a large discrete economy where the number of states is less 
than or equal to the number of assets, if there are no arbitrage opportu-
nities the market might be complete. If the market is complete and arbi-
trage-free, there will be a number of factors while all other processes 
will be linear combinations of these factors. These considerations will 
be further developed in Chapter 18. 

435 
Arbitrage Pricing: Finite-State Models 
APT MODELS 
In the previous sections we presented the general theory of arbitrage 
pricing. The most fundamental principle of finance theory, absence of 
arbitrage, applies to all price processes. In this section we present a spe-
cial case of the theory which applies to equity prices. In 1976 Stephen 
Ross published a seminal paper2 where he argued that equity returns 
can be represented as a linear regression over a small set of factors and 
that expected returns are determined by principle of absence of arbi-
trage. This pricing theory is called the Arbitrage Pricing Theory (APT). 
APT is formulated in a one period setting. Suppose that equity 
returns can be written as follows: 
r = a + Bf + ε
where r is the n-vector of returns to be modeled, f is a k-vector of com-
mon factors with k << n, a is an n-vector of constants, B is a n×k matrix 
and ε is an n-vector of random disturbances such that: 
E[ε f] = 0 
E[εε′ f] = Σ
In the above relationships, the factors are stochastic variables. APT 
states that, if there is no arbitrage, the constants a in the above relation-
ship must all be equal to the risk-free rate. 
In a one period setting, if there are only a finite number of securities 
traded at discrete dates and if the price of each security can take any 
value regardless of the prices of other securities, clearly no arbitrage 
opportunity is possible. In fact, given any portfolio, infinite price paths 
can assume negative values. In a probabilistic context it might happen 
that the probability of making a loss starting from zero investment 
might be small but not zero. 
APT holds in the limit of a large economy. Ross assumed that well-
diversified portfolios exist; this implies that stochastic fluctuations go to 
zero in the limit of very large portfolios. This is not to say that portfolio 
behavior becomes deterministic in the limit of large portfolios as factors are 
assumed to be stochastic; it does however mean that uncertainty is com-
pletely captured by the dynamics of factors. Under this assumption, Ross 
demonstrated that the following relationship holds for large economies: 
2 Stephen Ross, “The Arbitrage Theory of Capital Asset Pricing,” Journal of Eco-
nomic Theory 13, no. 3 (December 1976), pp. 341–360. 

436 
The Mathematics of Financial Modeling and Investment Management 
E r[ ]  = λ 0ι + Bλ
where λ are risk premia. This relationship says that each asset’s return is 
equal to the risk-free rate λ 0 plus a linear combination of factors. 
In the original formulation, the above linear relationship holds only 
approximately in the limit of an infinite economy. Any finite number of 
assets can be mispriced, that is, violate the above relationship. The APT 
relationship can be made rigorous with additional restrictions on agent 
behavior. 
T esting APT 
The original formulation of APT does not identify factors. Subsequently 
a number of researchers tried to tackle the problem. As we will see in 
Chapter 18, factors can be either exogenously given factors or abstract 
factors formed by particular portfolios. A number of studies have tried 
to identify macroeconomic factors responsible for stock returns.3 Statis-
tical techniques such as factor analysis or principal components analysis 
have also been used. 
The approximate nature of APT makes it difficult to test it. In fact, 
the APT holds only in the limit of an infinite economy while any finite 
number of securities can be arbitrarily priced without affecting the arbi-
trage principle. For this reason it has been suggested that APT cannot be 
tested at all.4 Based on a given selection of factors APT has been tested 
with the techniques that we will explain in the following sections. 
Testing APT when Factors are Portfolios 
Suppose that factors are given portfolios and that there is a risk-free 
asset. This means that it is known (or at least assumed) that the model 
in excess returns takes the form 
zt = a
Bft + εt
+ 
3 See, for example, Chen, Nai-Fu, Richard R. Roll, and Stephen A. Ross, “Economic 
Forces and the Stock Market,” Journal of Business 59, no. 3 (1986), pp. 383–404 
and Michael A. Berry, Edwin Burmeister, and Marjorie B. McElroy, “Sorting out 
Risk Using Known APT Factors,” Financial Analysts Journal 44, no. 2 (1988), pp. 
29–42. 
4 Phoebus J. Dhrymes, Irwin Friend, and N. Bulent Gultekin, “A Critical Re-Exami-
nation of the Empirical Evidence on the Arbitrage Pricing Theory,” Journal of Fi-
nance 39, no. 2 (1988), pp. 323–346. 

437 
Arbitrage Pricing: Finite-State Models 
f = ( f1
,
…
,
fk) , K << N 
fi = 
α
si 
∑
sris 
s = 1 
where ri = zi – ai and αs are the weights of those portfolios that iden-
s 
s
s
tify factors. 
APT requires that the constants a, when the model is formulated in 
excess returns, are zero. To test APT the model parameters have first to 
be estimated. Suppose that returns are normal IID variables and that the 
multifactor model is unconstrained. Model estimation can be done by 
Maximum Likelihood methods which are, in this case, identical to Ordi-
nary Least Square (OLS) estimates. The model parameters are then 
obtained as the empirical moments, as follows: 
ˆa
ˆB ˆµ
ˆµ
= 
– 
K 
T 
∑
ˆµ 
– ˆµ K)
(zt
() zKt 
– 
t = 1
Bˆ = -------------------------------------------------------------
T 
∑
ˆµ K 
– ˆµ K)
(
() zKt
zKt – 
t = 1 
T 
∑
1 
ˆµ 
zt 
= ---
Tt = 1 
T 
∑
1 
ˆµ 
zKt 
= ---
K 
Tt = 1 
Now suppose that there is a risk-free asset and that the model is 
constrained by the APT constraints. In this case, we can still use MLE 
estimation which yields a zero intercept and the following sensitivities: 

438 
The Mathematics of Financial Modeling and Investment Management 
T 
∑ztz' Kt 
t = 1
ˆB = --------------------------
T 
∑zKtz' Kt 
t = 1 
The APT restriction can be tested with Likelihood Ratio methods which 
compare the likelihood of the constrained and unconstrained model. 
Testing and Estimating APT When Factors are not Portfolios 
If factors are not portfolios and if they are given exogenous processes, 
multifactor models are multivariate regressions on the factors. If the 
regression innovations are assumed to be jointly normally distributed and 
no restriction is imposed, models can be estimated with MLE methods 
that are, in this case, equivalent to OLS estimates. Writing the multifactor 
model in real returns, OLS estimation yields the following results: 
ˆµ µ
ˆB ˆµ 
aˆ = 
– 
K 
T 
∑
ˆµ 
– ˆµ K)
(
() fKt
rt – 
t = 1
ˆB = ------------------------------------------------------------
T 
∑
ˆµ K 
– ˆµ K)
(
() fKt
fKt – 
t = 1 
T 
∑
1 
ˆµ = ---
T 
rt 
t = 1 
T 
∑
1 
ˆµ 
fKt 
= ---
K 
Tt = 1 
Testing the zero intercept restriction from the above estimates can be 
performed using MLE methods. Note that in this case only one model is 
estimated because factors are given. Should factors be portfolios, the 
constrained and unconstrained models yield different factors. 

439 
Arbitrage Pricing: Finite-State Models 
SUMMARY 
 ■ The law of one price states that a given asset must have the same price 
regardless of the means by which one goes about creating that asset.
 ■ Arbitrage is the simultaneous buying and selling of an asset at two dif-
ferent prices in two different markets.
 ■ A finite-state one-period market is represented by a vector of prices and 
a matrix of payoffs.
 ■ A state-price vector is a strictly positive vector such that prices are the 
product of the state-price vector and the payoff matrix.
 ■ There is no arbitrage if and only if there is a state-price vector.
 ■ A market is complete if an arbitrary payoff can be replicated by a port-
folio.
 ■ A finite-state one-period market is complete if there are as many lin-
early independent assets as states.
 ■ A multiperiod finite-state economy is represented by a probability 
space plus an information structure.
 ■ In a multiperiod finite-state market each security is represented by a 
payoff process and a price process.
 ■ An arbitrage is a trading strategy whose payoff process is nonnegative 
and not always zero.
 ■ A market is complete if any nonnegative payoff process can be repli-
cated with a trading strategy.
 ■ A state-price deflator is a strictly positive process such that prices are 
random variables equal to the conditional expectation of discounted 
payoffs.
 ■ A martingale is a process such that at any time t its conditional expec-
tation at time s, s > t coincides with its present value.
 ■ In absence of arbitrage there is an artificial probability measure in 
which all price processes, appropriately discounted, become martin-
gales.
 ■ Given a probability measure P, the probability measure Q is said to be 
equivalent to P if both assign probability zero to the same events.
 ■ The binomial model assumes that there are two positive numbers, d, 
and u, such that 0 < d < u and such that at each time step the price S of 
the risky asset changes to dS or to uS.
 ■ The distribution of prices of a binomial model is a binomial distribu-
tion.
 ■ The binomial model is complete.
 ■ The Arbitrage Pricing Theory (APT) asserts that each asset’s return is 
equal to the risk-free rate plus a linear combination of factors.
 ■ The APT can be tested with maximum likelihood methods. 



## Arbitrage Pricing: Continuous-State

I 
CHAPTER 15 
Arbitrage Pricing: 
Continuous-State, 
Continuous-Time Models 
n the previous chapter we described arbitrage pricing using finite-state 
models. In this chapter we describe arbitrage pricing in the continuous-
state, continuous-time setting. There are a number of important conceptual 
changes in going from a discrete-state, discrete-time setting to a continuous-
state, continuous-time setting. First, each state of the world has probability 
zero. As described in Chapter 6, this precludes the use of standard con-
ditional probabilities for the definition of conditional expectation and 
requires the use of filtrations (rather than of information structures) to 
describe the propagation of information. Second, the tools of matrix 
algebra are inadequate; the more complex tools of calculus and stochas-
tic calculus described in Chapters 4, 8, 9, and 10, respectively, are 
required. Third, simple generalizations are rarely possible as many patho-
logical cases appear in connection with infinite sets. 
THE ARBITRAGE PRINCIPLE IN CONTINUOUS TIME 
Let’s start with the definition of basic concepts. The economy is repre-
sented by a probability space (Ω, ℑ, P) where Ω is the set of possible 
states, ℑis the σ-algebra of events, and P is a probability measure. Time 
is a continuous variable in the interval [0,T]. Recall from Chapter 6 that 
the propagation of information is represented by a filtration ℑt. The lat-
ter is a family of σ-algebras such that ℑt ⊆ℑs, t < s. 
441 

442 
The Mathematics of Financial Modeling and Investment Management 
Each security i is characterized by a payoff-rate process δt
i and by a
i
price process Si
t . In this continuous-state setting, δt
i and St are real vari-
ω
i ω
ables with a continuous range such that δt
i (
)
 and St(
)
 
 are, respectively, 
the payoff-rate and the price of the i-th asset at time t, 0 ≤t ≤T and in state 
ω ∈Ω. Note that δt
i represents a rate of payoff and not a payoff as was the 
case in the discrete-time setting. The payoff-rate process must be inter-
preted in the sense that the cumulative payoff of each individual asset is 
t 
Dt
i = ∫δi s
d 
s 
0 
We assume that the number of assets is finite. We can therefore use 
the vector notation to indicate a set of processes. For example, we write 
δt and St to indicate the vector process of payoff rates and prices respec-
tively. Following Chapter 6, all payoff-rates and prices are stochastic 
processes adapted to the filtration ℑ. One can make assumptions about 
the price and the payoff-rate processes. For example, it can be assumed 
that price and payoff-rate processes satisfy a set of stochastic differen-
tial equations or that they exhibit finite jumps. Later in this chapter we 
will explore a number of these processes. 
As explained in Chapter 6, conditional expectations are defined as 
partial averaging. In fact, given a variable Xs, s > t, its conditional 
expectation Et[Xs] is defined as a variable that is ℑt-measurable and 
whose average on each set A ∈ ℑt is the same as that of X: 
[
ω
[
ω
Yt = Et[X ] ⇔E Yt(
)] = E X (
)]
s
s 
for ω ∈ A, ∀A ∈ℑt and Y is ℑt-measurable. 
The law of iterated expectations applies as in the finite-state case: 
Et[Eu(Xs)] = Et[Xs] 
In a continuous-state setting, conditional expectations are variables 
that assume constant values on the sets of infinite partitions. Imagine 
the evolution of a variable X. At the initial date, X0 identifies the entire 
space Ω. At each subsequent date t, the space Ω is partitioned into an 
infinite number of sets, each determined by one of the infinite values of 
Xt.1 However, these sets have measure zero. In fact, they are sets of the 
1 One can visualize this process as a tree structure with an infinite number of branch-
es and an infinite number of branching points. However, as the number of branches 
and of branching points is a continuum, intuition might be misleading. 

443 
Arbitrage Pricing: Continuous-State, Continuous-Time Models 
type: {A: ω ∈ A ⇔ Xt(ω) = x} determined by specific values of the vari-
able Xt. These sets have probability zero as there is an infinite number 
of values Xt. As a consequence, we cannot define conditional expecta-
tion as expectation under the usual definition of conditional probabili-
ties the same way we did in the case of finite-state setting. 
Trading Strategies and Trading Gains 
We have to define the meaning of trading strategies in the continuous-
state, continuous-time setting; this requires the notion of continuous 
trading. Mathematically, continuous trading means that the composi-
tion of portfolios changes continuously at every instant and that these 
changes are associated with trading gains or losses. A trading strategy is 
θt
i
a (vector-valued) process θ = {θi} such that θt = {
}
 
is the portfolio 
held at time t. To ensure that there is no anticipation of information, 
each trading strategy θ must be an adapted process. 
Given a trading strategy, we have to define the gains or losses asso-
ciated with it. In discrete time, the trading gains equal the sum of pay-
offs plus the change of a portfolio’s value 
T 
 
i
i
∑ ∑dt
i θi
t 
 + ∑Si
TθT – ∑S0 
i θ0 
t = 0 
i 
i
i 
over a finite interval [0,T]. 
We must define trading gains when time is a continuous variable. 
Recall from Chapter 8 that it is not possible to replace finite sums of 
stochastic increments with pathwise Riemann-Stieltjes integrals after 
letting the time interval go to zero. The reason is that, though we can 
assume that paths are continuous, we cannot assume that they have 
bounded variation. As a consequence, pathwise Riemann-Stieltjes inte-
grals generally do not exist. However, we can assume that paths are of 
bounded quadratic variation. Under this latter assumption, using Itô 
isometry, we can define pathwise Itô integrals and stochastic integrals. 
Let’s first assume that the payoff-rate process is zero, so that there 
are only price processes. Under this assumption, the trading gain Tt of a 
trading strategy can be represented by a stochastic integral: 
t
t 
i
Tt = ∫θsdS
= ∑∫θidS
s 
s
s 
0 
i 0 
In the rest of this section, we will not strictly adhere to the vector 
notation when there is no risk of confusion. For example, we will write 

444 
The Mathematics of Financial Modeling and Investment Management 
θ ⋅ S to represent the scalar product θ ⋅ S. If a payoff-rate process is asso-
ciated with each asset, we have to add the gains consequent to the pay-
off-rate process. We therefore define the gain process 
i
i
Gt
i = St + Dt 
as the sum of the price processes plus the cumulative payoff-rate pro-
cesses and we define the trading gains as the stochastic integral 
t
t 
i
Tt = ∫θsdG
= ∑∫θsdGi 
s
s 
0 
i 0 
How can we match the abstract notion of a stochastic integral with 
the buying and selling of assets? In discrete time, trading gains have a 
meaning that is in agreement with the practical notion of buying a port-
folio of assets, holding it for a period, and then selling it at market 
prices, thus realizing either a gain or a loss. One might object that in 
continuous time this meaning is lost. How can a process where prices 
change so that their total variation is unbounded be a reasonable repre-
sentation of financial reality? This is a question of methodology that is 
relevant to every field of science. In classical physics, the use of continu-
ous models was assumed to reflect reality; time and space, for example, 
were considered continuous. Quantum physics upset the conceptual cart 
of classical physics and the reality of continuous processes has since been 
questioned at every level. In quantum physics, a theory is considered to 
be nothing but a model useful as a mathematical device to predict mea-
surements. This is, in essence, the theory set forth in the 1930s by Niels 
Bohr and the School of Copenhaghen; it has now become mainstream 
methodology in physics. It is also, ultimately, the point of view of posi-
tive economics. In a famous and widely quoted essay, Milton Friedman, 
recipient of the 1976 Nobel Prize in Economic Science, wrote: 
The relevant question to ask about the “assumptions” of a theory 
is not whether they are descriptively “realistic,” for they never are, 
but whether they are sufficiently good approximations for the pur-
pose in hand. And this question can be answered only by seeing 
whether the theory works, which means if it yields sufficiently 
accurate predictions.2 
2 Milton Friedman, Essays in the Theory of Positive Economics (Chicago: University 
of Chicago Press, 1953). 

445 
Arbitrage Pricing: Continuous-State, Continuous-Time Models 
In the spirit of positive economics, continuous-time financial models 
are mathematical devices used to predict, albeit in a probabilistic sense, 
financial observations made at discrete intervals of time. Stochastic 
gains predict trading gains only at discrete intervals of time—the only 
intervals that can be observed. Continuous-time finance should be seen 
as a logical construction that meets observations only at a finite number 
of dates, not as a realistic description of financial trading. 
Let’s consider processes without any intermediate payoff. A self-
financing trading strategy is a trading strategy such that the following 
relationships hold: 

i
i 
i
i
i
θtSt = ∑θtSt = ∑

θi 
0S0 + ∫ 
t 
θtdSt , t ∈[0, T] 
i
i  
0 
 
We first define arbitrage in the absence of a payoff-rate process. An 
arbitrage is a self-financing trading strategy such that: θ0S0 < 0 and θTST 
≥ 0, or θ0S0 ≤ 0 and θTST > 0. If there is a payoff-rate process, a self-
financing trading strategy is a trading strategy such that the following 
relationships hold: 

i
i 
i
i
i
θtSt = ∑θtSt = ∑

θi 
0S0 + ∫ 
t 
θtdGt , t ∈[0, T] 
i
i  
0 
 
i
i
where Gt
i = St + Dt is the gain process as previously defined. An arbi-
trage is a self-financing trading strategy such that: θ0S0 < 0 and θTST ≥ 
0, or θ0S0 ≤ 0 and θTST > 0. 
ARBITRAGE PRICING IN CONTINUOUS-STATE, 
CONTINUOUS-TIME 
The abstract principles of arbitrage pricing are the same in a discrete-
state, discrete-time setting as in a continuous-state, continuous-time set-
ting. Arbitrage pricing is relative pricing. In the absence of arbitrage, the 
price and payoff-rate processes of a set of basic assets fix the prices of 
other assets given the payoff-rate process of the latter. If markets are com-
plete, every price process can be computed in this way. In a discrete-state, 
discrete-time setting, the computation of arbitrage pricing is done with 
matrix algebra. In fact, in the absence of arbitrage, every price process 
can be expressed in two alternative ways: 

--------
446 
The Mathematics of Financial Modeling and Investment Management 
1. Prices St
i are equal to the normalized conditional expectation of pay-
offs deflated with state prices under the real probabilities: 
T 
1
St
i = ----Et ∑
πjdj
i 
πt
j = t + 1 
2. Prices St
i are equal to the conditional expectation of discounted payoffs 
under the risk-neutral probabilities 
T 
Q 
dj
i 
St
i = Et 
∑ Rt j
j = t + 1 
, 
State-price deflators and risk-neutral probabilities can be computed solv-
ing systems of linear equations for a kernel of basic assets. The above 
relationships are algebraic linear equations that fix all price processes. 
In a continuous-state, continuous-time setting, the principle of arbi-
trage pricing is the same. In the absence of arbitrage, given a number of 
basic price and payoff stochastic processes, other processes are fixed. 
The latter are called redundant securities as they are not necessary to fix 
prices. If markets are complete, every price process can be fixed in this 
way. In order to make computations feasible, some additional assump-
tions are made, in particular all payoff-rate and price processes are 
assumed to be Itô processes. 
The theory of arbitrage pricing in a continuous-state, continuous-
time setting uses the same tools as in a discrete-state, discrete-time set-
ting. Under an equivalent martingale measure, all price processes 
become martingales. Therefore prices can be determined as discounted 
present value relationships. Equivalent martingale measures are the 
same concept as state-price deflators: After appropriate deflation, all 
processes become martingales. The key point of arbitrage pricing theory 
is that both equivalent martingale measures and state-price deflators can 
be determined from a subset of the market. All other processes are 
redundant. 
In the following sections we will develop the theory of arbitrage 
pricing in steps. First, we will illustrate the principles of arbitrage pric-
ing in the case of options, arriving at the Black-Scholes option pricing 
formula. We will then extend this theory to more general derivative 
securities. Subsequently, we will state arbitrage pricing theory in the 
context of equivalent martingale measures and of state-price deflators. 

447 
Arbitrage Pricing: Continuous-State, Continuous-Time Models 
OPTION PRICING 
We will now apply the concepts of arbitrage pricing to option pricing in a 
continuous-state, continuous-time setting. Suppose that a market consists 
of three assets: a risk-free asset (which allows risk-free borrowing and lend-
ing at the risk-free rate of interest), a stock, and a European option. We will 
show that the price processes of a stock and of a risk-free asset fix the price 
process of an option on that stock. 
Suppose the risk-free rate is a constant r. Recall from Chapter 4 that 
the value Vt of a risk-free asset with constant rate r evolves according to 
the deterministic differential equation of continually compounding 
interest rates: 
dVt = rVtdt 
The above is a differential equation with separable variables. After sep-
arating the variables, the equation can be written as 
dVt 
--------- = rdt 
Vt 
which admits the solution Vt = V0ert where V0 is the initial value of 
the bank account. This formula can also be interpreted as the price pro-
cess of a risk-free bond with deterministic rate r. 
Stock Price Processes 
Let’s now examine the price process of the stock. Consider the process y 
= αt + σBt where Bt is a standard Brownian motion. From the definition 
of Itô integrals, it can be seen that this process, which is called an arith-
metic Brownian motion, is the solution of the following diffusion equa-
tion: 
dyt = αdt + σdBt 
where α is a constant called the drift of the diffusion and σ is a constant 
called the volatility of the diffusion. 
(αt + σBt)
Consider now the process St = S0e 
, t ≥ 0. Applying Itô’s 
lemma it is easy to see that this process, which is called a geometric 
Brownian motion, is an Itô process that satisfies the following stochastic 
differential equation: 
dSt = µStdt + σStdBt ; S0 = x 

448 
The Mathematics of Financial Modeling and Investment Management 
where x is an initial value, µ = α + ¹₂σ2 and Bt is a standard Brownian 
motion. We assume that the stock price process follows a geometric 
Brownian motion and that there is no payoff-rate process. 
Now consider a European call option which gives the owner the right 
but not the obligation to buy the underlying stock at the exercise price K 
at the expiry date T. Call Yt the price of the option at time t. The price of 
the option as a function of the stock price is known at the final expiry 
date. If the option is rationally exercised, the final value of the option is 
YT = max(ST – K, 0) 
In fact, the option can be rationally exercised only if the price of the 
stock exceeds K. In that case, the owner of the option can buy the 
underlying stock at the price K, sell it immediately at the current price St 
and make a profit equal to (ST – K). If the stock price is below K, the 
option is clearly worthless. After T, the option ceases to exist. 
How can we compute the option price at every other date? We can 
arrive at the solution in two different but equivalent ways: (1) through 
hedging arguments and (2) the equivalent martingale measures. In the 
following sections we will introduce hedging arguments and equivalent 
martingale measures. 
Hedging 
To hedge means to protect against an adverse movement. The seller of an 
option is subject to a liability as, from his point of view, the option has a 
negative payoff in some states. In our context, hedging this option means 
to form a self-financing trading strategy formed with the stock plus the 
risk-free asset in appropriate proportions such that the option plus this 
hedging portfolio is risk free. Hedging the option implies that the hedging 
portfolio perfectly replicates the option payoff in every possible state. 
A European call option has only one payoff at the expiry date. It 
therefore suffices that the hedging portfolio replicates the option payoff 
at that date. Suppose that there is a self-financing trading strategy
(θt 
2
1 , θt ) in the bond and the stock such that 
1
2
θt VT + θt ST = YT 
To avoid arbitrage, the price of the option at any moment must be equal 
to the value of the hedging self-financing trading strategy. In fact, sup-
pose that at any time t < T the self-financing strategy (θt 
2
1 , θt ) has a 
value lower than the option: 

449 
Arbitrage Pricing: Continuous-State, Continuous-Time Models 
1
2
θt Vt + θt St < Yt 
An investor could then sell the option for Yt, make an investment
1
2
θt Vt + θt St in the trading strategy, and at time T liquidate both the
1
2
option and the trading strategy. As θTVT + θt ST = YT the final liquida-
tion has value zero in every state of the world, so that the initial profit
1
2
Yt – θt VT + θt ST is a risk-free profit. A similar reasoning could be 
applied if, at any time t < T, the strategy (θt 
2
1 , θt ) had a value higher 
than the option. Therefore, we can conclude that if there is a self-financ-
ing trading strategy that replicates the option’s payoff, the value of the 
strategy must coincide with the option’s price at every instant prior to 
the expiry date. 
Observe that the above reasoning is an instance of the law of one 
price that we discussed in the previous chapter. If two portfolios have 
the same payoffs at every moment and in every state of the world, their 
price must be the same. In particular, if a trading strategy has the same 
payoffs of an asset, its value must coincide with the price of that asset. 
The Black-Scholes Option Pricing Formula 
Let’s now see how the price of the option can be computed. Assume that 
the price of the option is a function of time and of the price of the 
underlying stock: Yt = C(St,t). This assumption is reasonable but needs 
to be justified; for the moment it is only a hint as to how to proceed 
with the calculations. It will be justified later by verifying that the pric-
ing formula produces the correct final payoff. 
As St is assumed to be an Itô process, in particular a geometric 
Brownian motion, Yt = C(St,t)—which is a function of St—is an Itô pro-
cess as well. Therefore, using Itô’s formula, we can write down the sto-
chastic equation that Yt must satisfy. Recall from Chapter 8 that Itô’s 
formula prescribes that: 
(
( 
(
∂C St, t)
(
∂C St, t)
∂C St, t) 
1∂2C St, t) 2σ2 dt + ----------------------σStdB
dYt = ---------------------- + ----------------------Stµ + -- ------------------------St 
∂t 
∂St 
2 
∂St 
∂St 
2 
1
Suppose now that there is a self-financing trading strategy Yt = θt Vt
2
+ θt St . We can write this equation as 
t 
t
t 
dYt = 
1 dVt + θt dSt
∫
θt ∫ 
2∫ 
0 
0
0 

---------------------
-----
---------------------
450 
The Mathematics of Financial Modeling and Investment Management 
or, in differential form, as 
1
2 
1
2
dYt = θt dVt + θt dSt = (θt rVt + θt µSt)dt + θt 
2σStdBt 
If the trading strategy replicates the option price process, the two 
expressions for dYt—the one obtained through Itô’s lemma and the 
other obtained through the assumption that there is a replicating self-
financing trading strategy—must be equal: 
1
2
(θt rVt + θt µSt)dt + θt 
2σStdBt 
(
( 
(
∂C St, t)
(
∂C St, t)
∂C St, t) 
1∂2C St, t) 2σ2 dt + ----------------------σStdBt 
= ---------------------- + ----------------------Stµ + -- ------------------------St 
∂t 
∂St 
2 
∂St 
∂St 
2 
The equality of these two expressions implies the equality of the 
coefficients in dt and dB respectively. Equating the coefficients in dB 
yields, 
θt 
2 = ∂C St, t
( 
) 
∂St 
-
As Yt = C St, t
( 
) = θt 
1Vt 
, substituting, we obtain
θt 
2St
+ 
θt 
1 = 1 
Vt 
- C St, t
( 
) – ∂C St, t
( 
) 
∂St 
-St 
We have now obtained the self-financing trading strategy in function of 
the stock and option prices. Substituting and equating the coefficients of 
dt yields, 
(
(
1 
(
∂C St, t)
∂C St, t) 
----- C St, t) – ----------------------St rVt + ----------------------µSt
Vt 
∂St 
∂St 
∂C St, t)
∂C St, t) 
1∂2C St, t) 2σ2
(
( 
( 
= ---------------------- + ----------------------Stµ + -- ------------------------St
∂t 
∂St 
2 
∂St 
2 
Simplifying and eliminating common terms, we obtain 

451 
Arbitrage Pricing: Continuous-State, Continuous-Time Models 
(
( 
(
∂C St, t)
∂C St, t) 
1∂2C St, t)
2σ2
(
– rC St, t) + r----------------------St + ---------------------- + -- ------------------------St 
= 0 
∂St 
∂t 
2 
∂St 
2 
If the function C(St,t) satisfies this relationship, then the coefficients 
in dt match. The above relationship is a partial differential equation 
(PDE). In Chapter 9 we discussed how to solve this equation with suit-
able boundary conditions. Boundary conditions are provided by the 
payoff of the option at the expiry date: 
(
YT = C ST, T) = max(ST – K, 0) 
The closed-form solution of the above PDE with the above boundary 
conditions was derived by Fischer Black and Myron Scholes3 and 
referred to as the Black-Scholes option pricing formula: 
( 
( ) – e –r T  – t)
C St, t) = xΦ z
( 
KΦ(z – σ T
t)
– 
with 
 
1
2 
–
log (St ⁄ K) + r + --σ (T
t)
2 
 
z = -------------------------------------------------------------------------
σ T
t
– 
and where Φ is the cumulative normal distribution. 
Let’s stop for a moment and review the logical steps we have fol-
lowed thus far. First, we defined a market made by a stock whose price 
process follows a geometric Brownian motion and a bond whose price 
process is a deterministic exponential. We introduced into this market a 
European call option. We then made two assumptions: (1) The option’s 
price process is a deterministic function of the stock price process; and 
(2) the option’s price process can be replicated by a self-financing trad-
ing strategy. 
If the above assumptions are true, we can write a stochastic differ-
ential equation for the option’s price process in two different ways: (1) 
Using Itô’s lemma, we can write the option price stochastic process as a 
function of the stock stochastic process; and (2) using the assumption 
that there is a replicating trading strategy, we can write the option price 
3 Fischer Black and Myron Scholes, “The Pricing of Options and Corporate Liabili-
ties,” Journal of Political Economy 81 (1973), pp. 637–654. 

452 
The Mathematics of Financial Modeling and Investment Management 
stochastic process as the stochastic process of the trading strategy. As 
the two equations describe the same process, they must coincide. Equat-
ing the coefficients in the deterministic and stochastic terms, we can 
determine the trading strategy and write a deterministic partial differen-
tial equation (PDE) that the pricing function of the option must satisfy. 
The latter PDE together with the boundary conditions provided by the 
known value of the option at the expiry date uniquely determine the 
option pricing function. 
Note that the above is neither a demonstration that there is an 
option pricing function, nor a demonstration that there is a replicating 
trading strategy. However, if both a pricing function and a replicating 
trading strategy exist, the above process allows one to determine both 
by solving a partial differential equation. After determining a solution 
to the PDE, one can verify if it provides a pricing function and if it 
allows the creation of a self-financing trading strategy. Ultimately, the 
justification of the existence of an option’s pricing function and of a rep-
licating self-financing trading strategy resides in the possibility of actu-
ally determining both. Absence of arbitrage assures that this solution is 
unique. 
Generalizing the Pricing of European Options 
We can now generalize the above pricing methodology to a generic 
European option and to more general price processes for the bond and 
for the underlying stock. In the most general case, the process underly-
ing a derivative need not be a stock price process. However, we suppose 
that the underlying is a stock price process so that replicating portfolios 
can be formed. We generalize in three ways:
 ■ The option’s payoff is an arbitrary finite-variance random variable.
 ■ The stock price process is an Itô process.
 ■ The short-rate process is stochastic. 
Following the definition given in the finite-state setting, we define a 
European option on some underlying process St as an asset whose pay-
off at time T is given by the random variable YT = g(ST) where g(x), x ∈ 
R is a continuous real-valued function. In other words, a European 
option is defined as a security whose payoff is determined at a given 
expiry date T as a function of some underlying random variable. The 
option has a zero payoff at every other date t ∈ [0,T]. This definition 
clearly distinguishes European options from American options which 
yield payoffs at random stopping times. 

453 
Arbitrage Pricing: Continuous-State, Continuous-Time Models 
Let’s now generalize the price process of the underlying stock. We 
represent the underlying stock price process as a generic Itô process. 
Recall from Chapter 8 that a generic univariate Itô process can be repre-
sented through the differential stochastic equation: 
dSt = µ(St, t)dt + σ(St, t)dBt ; S0 = x 
where x is the initial condition, B is a standard Brownian motion, and 
µ(St,t) and (St,t) are given functions R × [0,∞) → R. The geometric 
Brownian motion is a particular example of an Itô process. 
Let’s now define the bond price process. We retain the risk-free 
nature of the bond but let the interest rate be stochastic. Recall that in a 
discrete-state, discrete-time setting, a bond was defined as a process 
that, at each time step, exhibits the same return for each state though 
the return can be different in different time steps. Consequently, in con-
tinuous-time we define a bond price process as the following integral: 
t 
(r S , u) u
d 
u
∫0
Vt = V0e 
where r is a given function that represents the stochastic rate. In fact, 
the rate r depends on the time t and on the stock price process St. Appli-
cation of Itô’s lemma shows that the bond price process satisfies the fol-
lowing equation: 
(
dVt = Vtr St, t)dt 
We can now use the same reasoning that led to the Black-Scholes 
formula. Suppose that there are both an option pricing function Yt  = 
C(St,t) and a replicating self-financing trading strategy 
1
2
Yt = θt Vt + θt St 
We can now write a stochastic differential equation for the process Yt in 
two ways: 
1. Applying Itô’s lemma to Yt = C(St,t)
1
2
2. Directly to Yt = θt Vt + θt St 
The first approach yields 

454 
The Mathematics of Financial Modeling and Investment Management 
(
( 
(
∂C St, t)
∂C St, t) 
1∂2C St, t)
dYt = ---------------------- + ----------------------µ(St, t) + -- ------------------------σ2(St, t) dt 
∂t 
∂St 
2 
∂St 
2 
∂C St, t)
(
+ ----------------------σ(St, t)dBt 
∂St 
The second approach yields 
1 ( 
2
dYt = [θt r St, t)Vt + θt µ(St, t)]dt + θt 
2σ(St, t)dBt 
Equating coefficients in dt, Db we obtain the trading strategy 
1
1 
(
∂C St, t)
(
θt = ----- C St, t) – ----------------------St
Vt 
∂St 
2 
∂C St, t)
(
θt = ----------------------
∂St 
and the PDE 
( ,
( , 
( ,
( , 
( , 
( ,
∂C x  t)
∂C x  t) 
1∂2C x  t) 
,
–r x  t)C x  t) + r x  t)--------------------x + -------------------- + -- -----------------------σ2(x t) = 0 
∂x 
∂t 
2 
∂x 2 
with the boundary conditions C(ST,T) = g(ST). Solving this equation we 
obtain a candidate option pricing function. In each specific case, one 
can then verify that the option pricing function effectively solves the 
option pricing problem. 
STATE-PRICE DEFLATORS 
We now extend the concepts of state prices and equivalent martingale 
measures to a continuous-state, continuous-time setting. As in the previ-
ous sections, the economy is represented by a probability space (Ω, ℑ, P) 
where Ω is the set of possible states, ℑ is the σ-algebra of events, and P 
is a probability measure. Time is a continuous variable in the interval 
[0,T]. The propagation of information is represented by a filtration ℑt. 

455 
Arbitrage Pricing: Continuous-State, Continuous-Time Models 
A multivariate standard Brownian motion B = (B1,...,BD) in RD adapted 
to the filtration ℑt is defined over this probability space. From Chapter 
10 we know that there are mathematical subtleties that we will not take 
into consideration, as regards whether (1) the filtration is given and the 
Brownian motion is adapted to the filtration or (2) the filtration is gen-
erated by the Brownian motion. 
Suppose that there are N price processes X = (X1,...,XN) that form a 
multivariate Itô process in RN. Trading strategies are adapted processes θ 
= (θ1,...,θΝ) that represent the quantity of each asset held at each instant. 
In order to ensure the existence of stochastic integrals, we require the 
processes (X1,...,XN) and any trading strategy to be of bounded varia-
tion. Let’s first suppose that there is no payoff-rate process. This assump-
tion will be relaxed in a later section. Suppose also that one of these
1 
processes, say Xt , is defined by a short-rate process r, so that 
t 
r
u
d 
u
∫0
1
Xt = e 
or 
1
1
dXt = rtXt dt 
where rt is a deterministic function of t called the short-rate process. 
1
Note that Xt  could be replaced by a trading strategy. We can think of rt 
as the risk-free short-term continuously compounding interest rate and
1
of Xt as a risk-free continuously compounding bank account. 
The concept of arbitrage and of trading strategy was defined in the 
previous section. We now introduce the concept of deflators in a contin-
uous-time continuous-state setting. Any strictly positive Itô process is 
called a deflator. Given a deflator Y we can deflate any process X, 
obtaining a new deflated process 
Y
Xt = XtYt 
For example, any stock price process of a nondefaulting firm or the risk-
free bank account is a deflator. For technical reasons it is necessary to intro-
duce the concept of regular deflators. A regular deflator is a deflator that, 
after deflation, leaves unchanged the set of admissible bounded-variation 
trading strategies. 
We can make the first step towards defining a theory of pricing 
based on equivalent martingale measures. It can be demonstrated that if 

456 
The Mathematics of Financial Modeling and Investment Management 
Y is a regular deflator, a trading strategy θ is self-financing with respect 
to the price process X = (X1,...,XN) if and only if it is self-financing with 
respect to the deflated price process 
1 
N
XY = (YtXt , …, YtXt ) 
In addition, it can be demonstrated that the price process X  = 
(X1,...,XN) admits no arbitrage if and only if the deflated price process 
1 
N
XY = (YtXt , …, YtXt ) 
admits no arbitrage. 
A state-price deflator is a deflator π with the property that the 
deflated price process Xπ is a martingale. As explained in Chapter 6, a 
martingale is a stochastic process Mt such that its current value equals 
the conditional expectation of the process at any future time: Mt  = 
Et[Ms], s > t. For each price process Xt
i , the following relationship 
therefore holds: 
i
πtXt = Et[π Xi ] , s > t
s
s 
This definition is the equivalent in continuous time of the definition of a 
state-price deflator that was given in discrete time in the previous chap-
ter. In fact, recall that we defined a state-price deflator as a process π 
such that 
T 
1
St
i = ----Et ∑
πjdj
i 
πt
j = t + 1 
If there is no intermediate payoff, as in our present case, the previous 
relationship can be written as 
i 
i
i
πtSt = Et[πTST
i ] = Et[Et + 1[πTST]] = Et[πt + 1St + 1] 
The next proposition states that if there is a regular state-price 
deflator then there is no arbitrage. The demonstration of this proposi-
tion hinges on the fact that, as the deflated price process is a martingale, 
the following relationship holds: 

457 
Arbitrage Pricing: Continuous-State, Continuous-Time Models 
T 
E ∫θudSπ = 0
u 
0 
and therefore any self-financing trading strategy is a martingale. We can 
thus write 
π
π
θ0S0 = E[θTST ] 
If
π
π 
π
π
θTST ≥ 0 then θ0S0 ≥ 0 and if θTST > 0 then θ0S0 > 0 
which shows that there cannot be any arbitrage. 
We have now stated that the existence of state-price deflators ensures 
the absence of arbitrage. The converse of this statement in a continuous-
state, continuous-time setting is more delicate and will be dealt with later. 
We will now move on to equivalent martingale measures. 
EQUIVALENT MARTINGALE MEASURES 
In the previous section we saw that if there is a regular state-price deflator 
then there is no arbitrage. A state-price deflator transforms every price pro-
cess and every self-financing trading strategy into a martingale. We will 
now see that, after discounting by an appropriate process, price pro-
cesses become martingales through a transformation of the real probability 
measure into an equivalent martingale measure.4 This theory parallels the 
theory of equivalent martingale measures developed in the discrete-state, 
discrete-time setting. First some definitions must be discussed. 
Given a probability measure P, the probability measure Q is said to 
be equivalent to P if both assign probability zero to the same events, 
that is, if P(A) = 0 if and only if Q(A) = 0 for every event A. The equiva-
lent probability measure Q is said to be an equivalent martingale mea-
4 The theory of equivalent martingale measures was developed in the following arti-
cles: J.M. Harrison and S.R. Pliska, “A Stochastic Calculus Model of Continuous 
Trading: Complete Markets,” Stochastic Process Application 15 (1985), pp. 313– 
316; J.M. Harrison and S.R. Pliska, “Martingales and Stochastic Integrals in the 
Theory of Continuous Trading,” Stochastic Process Application 11 (1981), pp. 215– 
260 and, J.M. Harrison and D.M. Kreps, “Martingales and Arbitrage in Multiperiod 
Securities Markets,” Journal of Economic Theory 20 (June 1979), pp. 381–408. 

458 
The Mathematics of Financial Modeling and Investment Management 
sure for the process X if X is a martingale with respect to Q and if the 
Radon-Nikodym derivative 
dQ
ξ = --------
dP 
has finite variance. The definition of the Radon-Nikodym derivative is 
the same here as it is in the finite-state context. The Radon-Nikodym 
derivative is a random variable ξ such that Q(A) = EP[ξIA] for every 
event A where IA is the indicator function of the event A. 
To develop an intuition for this definition, consider that any sto-
chastic process X is a time-dependent random variable Xt. The latter is 
a family of functions Ω → R from the set of states to the real numbers 
indexed with time such that the sets {Xt(ω) ≤ x} are events for any real 
x. Given the probability measure P, the finite-dimension distributions of 
the process X are determined. The equivalent measure Q determines 
another set of finite-dimension distributions. However, the correspon-
dence between the process paths and the states remains unchanged. 
The requirement that P and Q are equivalent is necessary to ensure 
that the process is effectively the same under the two measures. There is 
no assurance that given an arbitrary process an equivalent martingale 
measure exists. Let’s assume that an equivalent martingale measure does 
exist for the N-dimensional price process X = (X1,...,XN). It can be dem-
onstrated that if the price process X = (X1,...,XN) admits an equivalent 
martingale measure then there is no arbitrage. 
The proof is similar to that for state-price deflators as discussed 
above. Under the equivalent martingale measure Q, which we assume 
exists, every price process and every self-financing trading strategy 
becomes a martingale. Using the same reasoning as above it is easy to 
see that there is no arbitrage. 
This result can be generalized; here is how. If there is a regular defla-
1 
N
tor Y such that the deflated price process XY = (YtXt , …, YtXt ) admits 
an equivalent martingale measure, then there is no arbitrage. The proof 
hinges on the result established in the previous section that, if there is a 
regular deflator Y, the price process X admits no arbitrage if and only if 
the deflated price process XY admits no arbitrage. 
Note that none of these results is constructive. They only state that 
the existence of an equivalent martingale measure with respect to a price 
process ensures the absence of arbitrage. Conditions to ensure the exist-
ence of an equivalent martingale measure with respect to a price process 
are given in the next section. 

459 
Arbitrage Pricing: Continuous-State, Continuous-Time Models 
EQUIVALENT MARTINGALE MEASURES AND 
GIRSANOV’S THEOREM 
We first need to establish an important mathematical result known as 
Girsanov’s Theorem. This theorem applies to Itô processes. Let’s first 
state Girsanov’s theorem in simple cases. Let X be a single-valued Itô 
process where B is a single-valued standard Brownian motion: 
t
t 
Xt = x + ∫µs s
d + ∫σsdBs 
0
0 
Suppose that a process ν and a process θ such that σtθt = µt – νt are 
given. Suppose, in addition, that the process θ satisfies the Novikov con-
dition which requires 
1 t
2 
--
θ
s
d 

2∫0 s 
E e 
∞
< 
Then, there is a probability measure Q equivalent to P such that the fol-
lowing integral 
t 
ˆBt = Bt + ∫θ
s
d
s 
0 
ˆ
defines a standard Brownian motion Bt in R on (Ω,ℑ,Q) with the same 
standard filtration of the original Brownian motion Bt. In addition, 
under Q the process X becomes 
t
t 
ˆ
Xt = x + ∫νs s
d + ∫σ dBs
s 
0
0 
Girsanov’s Theorem states that we can add drift to a standard 
Brownian motion and still obtain a standard Brownian motion under 
another probability measure. In addition, by changing the probability 
measure we can arbitrarily change the drift of an Itô process. 
The same theorem can be stated in multiple dimensions. Let X be an 
N-valued Itô process: 

460 
The Mathematics of Financial Modeling and Investment Management 
t
t 
Xt = x + ∫µs s
d + ∫σsdBs 
0
0 
In this process, µs is an N-vector process and σs is an N × D matrix. 
Suppose that there are both a vector process ν = (ν1,...,νN) and a vector 
process θ = (θ1,...,θN) such that σtθt = µt – νt where the product σtθt is 
not a scalar product but is performed component by component. Sup-
pose, in addition, that the process θ satisfies the Novikov condition: 
1∫0 
t
⋅ 
--
θ θ s
d 

2
E e 
∞
< 
Then there is a probability measure Q equivalent to P such that the fol-
lowing integral 
t 
ˆBt = Bt + ∫θ
s
d
s 
0 
ˆ
defines a standard Brownian motion Bt in RD on (Ω,ℑ,Q) with the same 
standard filtration of the original Brownian motion Bt. In addition, 
under Q the process X becomes 
t
t 
ˆ
Xt = x + ∫νs s
d + ∫σ dBs
s 
0
0 
Girsanov’s Theorem essentially states that under technical condi-
tions (the Novikov condition) by changing the probability measure, it is 
possible to transform an Itô process into another Itô process with arbi-
trary drift. Prima facie, this result might seem unreasonable. In the end 
the drift of a process seems to be a fundamental feature of the process as 
it defines, for example, the average of the process. Consider, however, 
that a stochastic process can be thought as the set of all its possible 
paths. In the case of an Itô process, we can identify the process with the 
set of all continuous and square integrable functions. As observed 
above, the drift is an average and it is determined by the probability 
measure on which the process is defined. Therefore, it should not be sur-
prising that by changing the probability measure it is possible to change 
the drift. 

461 
Arbitrage Pricing: Continuous-State, Continuous-Time Models 
The Diffusion Invariance Principle 
Note that Girsanov’s Theorem requires neither that the process X be a 
martingale nor that Q be an equivalent martingale measure. If X is 
indeed a martingale under Q, an implication of Girsanov’s Theorem is 
the diffusion invariance principle which can be stated as follows. Let X 
be an Itô process: 
dXt = µtdt + σtdBt 
If X is a martingale with respect to an equivalent probability measure Q, 
ˆ
then there is a standard Brownian motion BT in RD under Q such that 
ˆ
dXt = σtdBt 
Let’s now apply the previous results to a price process X = (V,S1,...,SN–1) 
where 
dSt = µtdt + σtdBt 
and 
dVt = rtVtdt 
–1
If the short-term rate r is bounded, Vt  is a regular deflator. Con-
sider the deflated processes: 
Zt = StVt 
–1 
By Itô’s lemma, this process satisfies the following stochastic equation: 

µt 
σt
dZt = –rtZt + ----- dt + -----dBt
 
Vt 
Vt 
Suppose there is an equivalent martingale measure Q. Under the 
equivalent martingale measure Q, the discounted price process 
Zt = StVt 
–1 
is a martingale. In addition, by the diffusion invariance principle there is 
ˆ
a standard Brownian motion Bt in RD under Q such that: 

462 
The Mathematics of Financial Modeling and Investment Management 
σt
dZt = -----dBˆ t
Vt 
Applying Itô’s lemma, given that ZtVt = St, we obtain the fundamen-
tal result: 
ˆ
dSt = rtdt + σtdBt 
This result states that, under the equivalent martingale measure, all 
price processes become Itô processes with the same drift. 
Application of Girsanov’s Theorem to Black-Scholes 
Option Pricing Formula 
To illustrate Girsanov’s Theorem, let’s see how the Black-Scholes option 
pricing formula can be obtained from an equivalent martingale mea-
sure. In the previous setting, let’s assume that N = 3, d = 1, rt is a con-
stant and 
σt = σSt 
with σ constant. Let S be the stock price process and C be the option 
price process. The option’s price at time T is 
1
C = max(ST – K) 
In this setting, therefore, the following three equations hold: 
S
dSt = µt
Sdt + σSt dBt 
2 
c
dCt = µt
cdt + σtdBt 
dVt = rVtdt 
Given that CtVt 
–1 is a martingale, we can write 
2 
Ct = VtEt ------
= Et 
(
Q CT 
Q[e –r T  – t)max(ST – K)]
Vt 

463 
Arbitrage Pricing: Continuous-State, Continuous-Time Models 
It can be demonstrated by direct computation that the above for-
mula is equal to the Black-Scholes option pricing formula presented ear-
lier in this chapter. 
EQUIVALENT MARTINGALE MEASURES AND 
COMPLETE MARKETS 
In the continuous-state, continuous-time setting, a market is said to be 
complete if any finite-variance random variable Y can be obtained as the 
terminal value at time T of a self-financing trading strategy θ: Y = θTXT. 
A fundamental theorem of arbitrage pricing states that, in the absence 
of arbitrage, a market is complete if and only if there is a unique equiv-
alent martingale measure. This is condition can be made more specific 
given that the market is populated with assets that follow Itô processes. 
Suppose that the price process is X = (V,S1,...,SN–1) where, as in the pre-
vious section: 
dSt = µtdt + σtdBt 
dVt = rVtdt 
and B is a standard Brownian motion B = (B1,...,BD) in RD . 
It can be demonstrated that markets are complete if and only if 
rank(σ) = d almost everywhere. This condition should be compared with 
the conditions for completeness we established in the discrete-state set-
ting in the previous chapter. In that setting, we demonstrated that mar-
kets are complete if and only if the number of linearly independent price 
processes is equal to the maximum number of branches leaving a node. 
In fact, market completeness is equivalent to the possibility of solving a 
linear system with as many equations as branches leaving each node. 
In the present continuous-state setting, there are infinite states and 
so we need different types of considerations. Roughly speaking, each 
price process (which is an Itô process) depends on D independent 
sources of uncertainty as we assume that the standard Brownian motion 
is D-dimensional. In a finite-state setting this means that, if processes 
are Markovian, at each time step any process can jump to D different 
values. The market is complete if there are D independent price pro-
cesses. Note that the number D is arbitrary. 

--------
464 
The Mathematics of Financial Modeling and Investment Management 
EQUIVALENT MARTINGALE MEASURES AND STATE PRICES 
We will now show that equivalent martingale measures and state prices 
are the same concept. We use the same setting as in the previous sec-
tions. Suppose that Q is an equivalent martingale measure after defla-
tion by the process 
t 
–r
u
d 
1 
∫0 
u 
------ = e 
1
Vt 
where r is a bounded short-rate process. The density process ξt for Q is 
defined as 
= E
-------- , t ∈[0,T]
ξt 
r
dQ 
dP 
where 
dQ 
dP 
is the Radon-Nikodym derivative of Q with respect to P. As in the dis-
crete-state setting, the Radon-Nikodym derivative of Q with respect to 
P is a random variable 
dQ
ξ = --------
dP 
with average value on the entire space equal to 1 and such that, for 
every event A, the probability of A under Q is the average of ξ: 
(
) = EA ξ
PQ A
[ ]  
It can be demonstrated that, given any ℑt-measurable random vari-
able W, the density process ξt for Q has the following property: 
Q W
Et[Wξt]
Et [
] = ---------------------
ξt 

465 
Arbitrage Pricing: Continuous-State, Continuous-Time Models 
To gain an intuition for the Radon-Nikodym derivative in a contin-
uous-state setting, let’s assume that the probability space is the real line 
equipped with the Borel σ-algebra and with a probability measure P. In 
this case, ξ = ξ(x), R →R and we can write 
Q A
(
) = 
ξ P
d 
∫ 
A 
or, dQ = ξdP. Given any random variable X with density f under P and 
density q under Q, we can then write 
[
] = 
xq x
( )f x
( ) x
d = 
xξ x
( ) x
d 
EQ X
∫
∫ 
R
R 
In other words, the random variable ξ is a function that multiplies the 
density f to yield the density q. 
We can now show the following key result. Given an equivalent 
martingale measure with density process ξt a state-price deflator is given 
by the process 
t 
–r
u
d 
u
∫0 
= ξte
πt 
Conversely, given a state-price deflator πt, the density process 
t 
r
u
d 
u
∫0 
πt
= e 
-----
ξt 
π0 
defines an equivalent martingale measure. In fact, suppose that Q is an 
equivalent martingale measure for XY with πt = ξtYt where 
t 
–r
u
d 
u
∫0
Yt = e 
Then, using the above relationship we can write: 
Y 
Y
Y
Et[πtXt] = Et[ξtXt ] = ξtEQ[ξtXt ] = ξtXt = πtXt
t 

466 
The Mathematics of Financial Modeling and Investment Management 
which shows that πt is a state-price deflator. The same reasoning in 
reverse order demonstrates that if πt is a state-price deflator then: 
t 
r
u
d
u
∫0 
πt
ξt = e 
-----
π0 
is a density process for Q. 
ARBITRAGE PRICING WITH A PAYOFF RATE 
In the analysis thus far, we assumed that there is no intermediate payoff. 
The owner of an asset makes a profit or a loss due only to the changes in 
value of the asset. Let’s now introduce a payoff-rate process δt
i for each 
asset i. The payoff-rate process must be interpreted in the sense that the 
cumulative payoff of each individual asset is 
t 
Dt
i = ∫δs
i s
d 
0 
We define a gain process 
i
i
Gt
i = St + Dt 
By the linearity of the Itô integrals, we can write any trading strategy as 
t 
t
t 
θtdGt = θtdXt + ∫θtdDt
∫
∫ 
0 
0
0 
If there is a payoff-rate process, a self-financing trading strategy is a 
trading strategy such that the following relationships hold: 

i
i 
i
θtSt = ∑θtSt = ∑

θt
iSt
i + ∫ 
t 
θi
tdGt , t ∈ [0,T] 
i
i  
0 
 
An arbitrage is, as before, a self-financing trading strategy such that 

467 
Arbitrage Pricing: Continuous-State, Continuous-Time Models 
θ0S0 < 0 and θTST ≥ 0, or θ0S0 ≤ 0 and θTST > 0 
The previous arguments extend to this case. An equivalent martingale 
measure for the pair (D,S) is defined as an equivalent probability mea-
sure Q such that the Radon-Nikodym derivative 
dQ
ξ = --------
dP 
has finite variance and the process G = S + D is a martingale. Under these 
conditions, the following relationship holds: 
T
s 
–r
u
d 
T ∫ –r
u
d 
u
u
Q ∫ 
+ ∫ 
t
s
St = Et
e
t 
e 
dD
t 
IMPLICATIONS OF THE ABSENCE OF ARBITRAGE 
We saw that the existence of an equivalent martingale measure or of 
state-price deflators implies absence of arbitrage. We have also seen 
that, in the absence of arbitrage, markets are complete if and only if 
there is a unique equivalent martingale measure. 
In a discrete-state, discrete-time context we could establish the com-
plete equivalence between the existence of state-price deflators, equiva-
lent martingale measures and absence of arbitrage, in the sense that any 
of these conditions implies the other two. In addition, the existence of a 
unique equivalent martingale measure implies absence of arbitrage and 
market completeness. 
In the present continuous-state context, however, absence of arbi-
trage implies the existence of an equivalent martingale measure and of 
state price deflators only under rather restrictive and complex technical 
conditions. If we want to relax these conditions, the condition of 
absence of arbitrage has to be slightly modified. These discussions are 
quite technical and will not be presented in this chapter.5 
5 See F. Delbaen and W. Schachermayer, “The Fundamental Theorem of Asset Pric-
ing for Unbounded Stochastic Processes,” Mathematische Annalen 312, no. 2 (Oc-
tober 1999), pp. 215–250 and F. Delbaen and W. Schachermayer, “A General 
Version of the Fundamental Theorem of Asset Pricing,” Mathematische Annalen 
300, no. 3 (November 1994), pp. 463–520. 

468 
The Mathematics of Financial Modeling and Investment Management 
WORKING WITH EQUIVALENT MARTINGALE MEASURES 
The concepts established in the preceding sections of this chapter might 
seem very complex, abstract, and scarcely useful. On the contrary, they 
entail important simplifications in the computation of derivative prices. 
We will see examples of these computations when we cover bond pric-
ing and credit derivatives in later chapters. Here we want to make a few 
general comments on how these tools are used. 
The key result of the arbitrage pricing theory is that, under the 
equivalent martingale measure, all discounted price processes become 
martingales and all price processes have the same drift. Therefore, all 
calculations can be performed under the assumption that the change to 
an equivalent martingale measure has been made. This environment 
allows important simplifications. For example, as we have seen, the 
option pricing problem becomes a problem of computing the present 
value of simpler processes. 
Obviously one has to go back to a real environment at the end of 
the pricing exercise. This is essentially a calibration problem, as risk-
neutral probabilities have to be estimated from real probabilities. 
Despite this complication, the equivalent martingale methodology has 
proved to be an important tool in derivative pricing. 
SUMMARY
 ■ A trading strategy is a vector-valued process that represents portfolio 
weights at each moment.
 ■ Trading gains are defined as stochastic integrals.
 ■ A self-financing trading strategy is one whose value at every moment is 
the initial value plus the trading gains at that moment.
 ■ An arbitrage is a self-financing trading strategy whose initial value is 
either negative and the final value nonnegative or the initial value non-
negative and the final value positive.
 ■ The Black-Scholes option pricing formula can be established by repli-
cating self-financing trading strategies.
 ■ The Black-Scholes pricing argument is based on constructing a self-
financing trading strategy that replicates the option price in each state 
and for each time.
 ■ Absence of arbitrage implies that a replicating self-financing trading 
strategy must have the same price as the option. 

469
Arbitrage Pricing: Continuous-State, Continuous-Time Models 
■ The Black-Scholes option pricing formula is obtained solving the par-
tial differential equation implied by the equality of the replicating self-
financing trading strategy and the option price process. 
■ A deflator is any strictly positive Itô process; a state-price deflator is a 
deflator with the property that the deflated price process is a martin-
gale.
 ■ If there is a (regular) state-price deflator then there is no arbitrage; the 
converse is true only under a number of technical conditions.
 ■ Two probability measures are said to be equivalent if they assign prob-
ability zero to the same event.
 ■ Given a process X on a probability space with probability measure P, 
the probability measure Q is said to be an equivalent martingale mea-
sure if it is equivalent to P and X is a martingale with respect to Q 
(plus other conditions).
 ■ If there is a regular deflator such that the deflated price process admits 
an equivalent martingale measure, then there is no arbitrage.
 ■ Under the equivalent martingale measure, all Itô price processes have 
the same drift.
 ■ In the absence of arbitrage, a market is complete if and only if there is a 
unique equivalent martingale measure. 


