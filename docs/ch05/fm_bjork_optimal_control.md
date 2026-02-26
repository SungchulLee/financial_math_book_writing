# Stochastic Optimal Control

!!! info "Source"
    **Arbitrage Theory in Continuous Time** by Tomas Björk, Oxford University Press, 2nd ed., 2004.
    These notes are used for educational purposes.

## Stochastic Optimal Control

250 
CURRENCY DERIVATIVES 
Following the arguments from the domestic analysis, we now transform the pro- 
cesses Y, Sd, Sf, Bd, Bf into a set of asset prices on the foreign market, namely 
Sf, Sd, Bd, where 
If we want to obtain the P-dynamics of Sf, Sd, Bd we now only have to use 
(17.21)-(17.24), substituting Y for X and d for f. Since we are not interested in 
these dynamics per se, we will, however, not carry out these computations. The 
object that we are primarily looking for is the foreign market price of risk Xf, 
and we can easily obtain that by writing down the foreign version of the system 
and substituting d for f and Y for X directly in (17.32)-(17.34). We get 
and, inserting (17.36)-(17.37), we finally obtain 
After some simple algebraic manipulations, the two systems (17.32)-(17.34) 
and (17.38)-(17.40) can be written as 
These equations can be written as 

DOMESTIC AND FOREIGN MARKET PRICES OF RISK 
25 1 
where 
so, since u is invertible, 
Thus we have 
Ad - X f  = ~-'(6 - v), 
and since 
we obtain 
Ad - X j  = 0-'(6 - cp) = o-'ou;i = o;. 
We have thus proved the following central result. 
Proposition 17.10 The foreign market price of risk is uniquely determined by 
the domestic market price of risk, and by the exchange rate volatility vector ox, 
through the formula 
X j  = A d  -0;. 
(17.41) 
Remark 17.3.1 For the benefit of the probabilist we note that this res- 
ult implies that the transition from Qd to Q f  is effected via a Girsanov 
transformation, for which the likelihood process L has the dynamics 
dL = Lox dW, 
L(0) = 1. 
Proposition 17.10 has immediate consequences for the existence of risk neut- 
ral markets. If we focus on the domestic market we can say that the market is 
(on the aggregate) risk neutral if the following valuation formula holds, where 
IId is the price process for any domestically traded asset. 
J'Jd ( t )  = e-'d(T-t)~P P"MT)1 file 
(17.42) 
In other words, the domestic market is risk neutral if and only if P = Qd. In 
many scientific papers an assumption is made that the domestic market is in 
fact risk neutral, and this is of course a behavioral assumption, typically made 

252 
CURRENCY DERIVATIVES 
in order to facilitate computations. In an international setting it then seems nat- 
ural to assume that both the domestic market and the foreign market are risk 
neutral, i.e. that, in addition to (17.42), the following formula also holds, where 
I I f  is the foreign price of any asset traded on the foreign market 
This seems innocent enough, but taken together these assumptions imply that 
P = Q d = Q f .  
Proposition 17.10 now tells us that (17.44) can never hold, unless ax = 0, 
i.e. if and only if the exchange rate is deterministic. 
At first glance this seems highly counter-intuitive, since the assumption about 
risk neutrality often is interpreted as an assumption about the (aggregate) atti- 
tude towards risk as such. However, from (17.42), which is an equation for 
objects measured in the domestic currency, it should be clear that risk neutral- 
ity is a property which holds only relative to a specified numeraire. To put 
it as a slogan, you may very well be risk neutral w.r.t. pounds sterling, and still 
be risk averse w.r.t. US dollars. 
There is nothing very deep going on here: it is basically just the Jensen 
inequality. To see this more clearly let us consider the following simplified situ- 
ation. We assume that rd = r f  = 0, and we assume that the domestic market 
is risk neutral. This means in particular that the exchange rate itself has the 
following risk neutral valuation formula 
X (0) = E [X (T)] . 
Looking at the exchange rate from the foreign perspective we see that if the 
foreign market also is risk neutral, then it must hold that 
Y(O) = EIY(T)I, 
with Y = 1/X. The Jensen inequality together with (17.45) gives us, however, 
Thus (17.45) and (17.46) can never hold simultaneously with a stochastic 
exchange rate. 
17.4 Exercises 
Exercise 17.1 Consider the European call on the exchange rate described at the 
end of Section 17.1. Denote the price of the call by c(t, x), and denote the price of 
the corresponding put option (with the same exercise price K and exercise date 

NOTES 
253 
T) by p(t, 2). Show that the put-call parity relation between p and c is given by 
p = c - xe-'f(T-t) 
+ Ke-'d (T-t). 
Exercise 17.2 Compute the pricing function (in the domestic currency) for a 
binary option on the exchange rate. This option is a T-claim, 2, of the form 
2 = l[a,b](X(T)), 
i.e. if a I X(T) 5 b then you will obtain one unit of the domestic currency, 
otherwise you get nothing. 
Exercise 17.3 Derive the dynamics of the domestic stock price Sd under the 
foreign martingale measure Q f .  
Exercise 17.4 Compute a pricing formula for the exchange option in (17.19). 
Use the ideas from Section 13.4 in order to reduce the complexity of the formula. 
For simplicity you may assume that the processes Sd, Sf, and X are uncorrelated. 
Exercise 17.5 Consider a model with the domestic short rate r d  and two for- 
eign currencies, the exchange rates of which (from the domestic perspective) 
are denoted by XI, and X2, respectively. The foreign short rates are denoted by 
rl and r2, respectively. We assume that the exchange rates have P-dynamics 
dXi=X,aidt+X,a,dW,, 
i=1,2, 
where %, W
2
 are P-Wiener processes with correlation p. 
(a) Derive the pricing PDE for contracts, quoted in the domestic currency, 
of the form 2 = @(XI (T) , Xz (T) ) . 
(b) Derive the corresponding risk neutral valuation formula, and the 
Qd-dynamics of XI 
and X2. 
(c) Compute the price, in domestic terms, of the "binary quanto con- 
tract" 2, which gives, at time T, K units of foreign currency No. 1, if 
a 5 X2(T) 5 b, (where a and b are given numbers), and zero otherwise. 
If you want to facilitate computations you may assume that p = 0. 
Exercise 17.6 Consider the model of the previous exercise. Compute the price, 
in domestic terms, of a quanto exchange option, which at time T gives you the 
option, but not the obligation, to exchange K units of currency No. 1 for 1 unit 
of currency No. 2. 
Hint: It is possible to reduce the state space as in Section 13.4. 
17.5 Notes 
The classic in this field is Garman and Kohlhagen (1983). See also Reiner (1992). 
A more technical treatment is given in Amin and Jarrow (1991). 

a 
18 
BARRIER OPTIONS 
The purpose of this chapter is to give a reasonably systematic overview of the 
pricing theory for those financial derivatives which are, in some sense, connected 
to the extremal values of the underlying price process. We focus on barrier 
options, ladders and lookbacks, and we confine ourselves to the case of one 
underlying asset. 
18.1 Mathematical Background 
In this chapter, we will give some probability distributions connected with barrier 
problems. All the results are standard, see e.g. Borodin-Salminen (1997). 
To start with some notational conventions, let { X ( t ) ;  0 I t < oo) be any 
process with continuous trajectories taking values on the real line. 
Definition 18.1 For any y E R, the hitting time of y, r ( X ,  y), sometimes 
denoted by ~ ( y )  
or rY, is defined by 
~ ( y )  
= inf {t 2 0 IX(t) = y). 
The X-process absorbed at y is defined by 
Xy(t) = X ( t  A T ) ,  
where we have used the notation a A p = min [a, PI. 
The running maximum and minimum processes, Mx(t) and mx(t), are 
defined by 
M x ( t )  = sup X ( s ) ,  
o<s<t 
mx (t) = inf X ( s ) ,  
ossst 
where we sometimes suppress the subscript X .  
We will be mainly concerned with barrier problems for Wiener processes, so 
naturally the normal distribution will play a prominent role. 
Definition 18.2 Let p(x; p, a )  denote the density of a normal distribution with 
mean p and variance u2, i.e. 
1 
v ( x ;  P, a) = - 
a& 

MATHEMATICAL BACKGROUND 
255 
The standardized density cp(x;O, 1) is denoted by cp(x), and the cumulative 
distribution function of cp(x) is as usual denoted by N(x), i.e. 
Let us now consider a Wiener process with (constant) drift p and (constant) 
diffusion a, starting at a point a, i.e. 
I 
I ,  
dX(t) = pdt + adWt, 
(18.1) 
X(0) = a. 
(18.2) 
We are primarily interested in the onedimensional marginal distribution for 
Xp(t), i.e. the distribution at time t of the X-process, absorbed at the point P. 
The distribution of Xp(t) is of course a mixed distribution in the sense that it 
has a point mass at x = ,8 (the probability that the process is absorbed prior 
to time t) and a density. This density has its support on the interval (P, oo) if 
a > p, whereas the support is the interval (-oo, P) if a < P. We now cite our 
main result concerning absorption densities. 
Proposition 18.3 The density fp(x; t, a )  of the absorbed process Xp(t), where 
X is defined by (18.1)-(18.2), is given by 
fp(x; t, a )  = cp(x; pt + a, a h )  - exp {- "(I; 
')} 
~ ( x ;  
pt - n + 2 ~ ,  
o ~ i ) .  
The support of this density is the interval (P, oo) if a > >, and the interval 
(-00, P) if ff < P. 
We end this section by giving the distribution for the running maximum 
(minimum) processes. 
Proposition 18.4 Consider the process X defined by (18.1)-(18.2), 
and let M 
(m) denote the running maximum (minimum) processes as in Definition 18.1. 
Then the distribution functions for M(t) (m(t)) are given by the following 
expressions, which hold for x 2 a and x < a respectively. 
x - a -  
x - a + p t  

BARRIER OPTIONS 
18.2 Out Contracts 
In this section, we will undertake a systematic study of the relations between 
a "standard" contingent claim and its different "barrier" versions. This will 
provide us with some basic insights and will also give us a number of easy for- 
mulas to use when pricing various barrier contracts. As usual we consider the 
standard BlackScholes model 
dS = aSdt + a S d ~ ,  
dB = r B  dt, 
with fixed parameters a, a, and r. 
We fix an exercise time T and we consider as usual a contingent claim 2 of 
the form 
2 = iP (S(T)). 
(18.3) 
We denote the pricing function of 2 by F(t, s; T, a), often suppressing the par* 
meter T. For mnem&echnical purposes we will also sometimes use the notation 
8(t, s), i.e. the pricing function (as opposed to the function defining the claim) 
is given in bold. 
18.2.1 Down-and-Out Contracts 
Fix a real number L < S(O), which will act as the barrier, and consider the 
following contract, which we denote by ZLO: 
If the stock price stays above the barrier L during the entire contract 
period, then the amount 2 is paid to the holder of the contract. 
If the stock price, at some time before the delivery time T, hits the barrier 
L, then the contract ceases to exist, and nothing is paid to the holder of 
the contract. 
The contract ZLO is called the "down-and-out" version of the contract 2 
above, and our main problem is to price ZLo. 
More formally we can describe 
ZLO 
as follows. 
Definition 18.5 Take as given a T-contract 2 = @(S(T)). Then the T-contract 
ZLO is defined by 
if ~ ( t )  
> L for all t E [O,T], 
zf S(t) t) L for some t E [0, TI. 
(18.4) 
Concerning the notation, L as a subscript indicates a "down
7'-type contract, 
whereas the letter 0 indicates that we are considering an "out" claim. You may 
also consider other types of barrier specifications and thus construct a "down- 
and-in" version of the basic contract 2. A "down-and-in" contract starts to 
exist the first time the stock price hits a lower barrier. Going on we may then 

OUT CONTRACTS 
257 
consider upand-out as well as upand-in contracts. All these types will be given 
precise definitions and studied in the following sections. 
In order to price ZLO we will have use for the function QL, which is the 
original contract function @ in (18.3) "chopped off" below L. 
Definition 18.6 For a &ed function @ the function @L is defined by 
@(x), for x > L, 
@ L ( ~ )  
= { 0, 
for x 5 L. 
In other words, QL (x) = @(x). I {x > L), where I denotes the indicator function. 
For further use we note that the pricing functional F(t, S; @) is linear in the 
@-argument, and that the "chopping" operation above is also linear. 
Lemma 18.7 For all reals a and P, and all functions @ and Q, we have 
F (t, s; a@ + PQ) = aF(t, s; @) + PF(t, s; Q), 
(a@ + P!qL = a * ~  
+ ~ Q L .  
Proof For F the linearity follows immediately from the risk neutral valuation 
formula together with the linearity of the expectation operator. The linearity of 
the chopping operation is obvious. 
Our main result is the following theorem, which tells us that the pricing 
problem for the down-and-out version of the contract @ is essentially reduced 
to that of pricing the nonbarrier claim aL. Thus, if we can price a standard 
(nonbarrier) claim with contract function cPL then we can also price the down- 
and-out version of the contract @. 
Theorem 18.8 (Pricing down-and-out contracts) Consider a &ed T-claim 
2 = @(S(T)). 
Then the pricing function, denoted by FLO, 
of the corresponding 
down-and-out contract ZLO is given, for s > L, by 
FLO(t, S; @) = F (t, S; @L) - ( ~ ) 2 i ' u '  F ( t,-;@L ) . 
(18.6) 
Here we have used the notation 
Proof Without loss of generality we may set t = 0 in (18.6). Assume then 
that S(0) = s > L, and recall that SL denotes the process S with (possible) 

258 
BARRIER OPTIONS 
absorption at L. Using risk neutral valuation we have 
It remains to compute the last expectation, and we have 
where h is the density function for the stochastic variable SL(T). 
From standard theory we have 
S(T) = exp {Ins + r'T + aW(T)) = 
where the process X is defined by 
dX(t) = r'dt + udW(t), 
X(0) = Ins. 
Thus we have 
so we may write 
where f is the density of the stochastic variable XlnL(T). This 
however, given by Proposition 18.3 as 
f (x) = q (x; r'T + ln s, u&) 

Thus we have 
OUT CONTRACTS 
=G 
O ~ ( e ~ ) v  
(x; iT + ln s, o&) 
dx 
00 
= Lm 
mL(ex)q (x; i~ + ~n s, o f i )  dx 
2 
00 
OL(ez), (,; iT + ln (c) 
, o f i )  dx. 
Inspecting the last two lines we see that the density in the first integral is the 
density of X(T) under the usual martingale measure Q, given the starting value 
S(0) = s. The density in the second integral is, in the same way, the density 
(under Q) of X(T), given the starting point S(0) = L2/s. 
Thus we have 
which gives us the result. 
We again emphasize the point of this result. 
The problem of computing the price for a down-and-out claim reduces to 
the standard problem of computing the price of an ordinary (related) claim 
without a barrier. 
For future use we also note the fact that down-and-out pricing is a linear 
operation. 
Corollary 18.9 For any contract functions CP and Q, and for any real numbers 
cr and p, the following relation holds. 
Proof The result follows immediately from Theorem 18.8 together with the 
linearity of the ordinary pricing functional F and the linearity of the chopping 
operation. 

260 
BARRIER OPTIONS 
18.2.2 Up-and-Out Contracts 
We again consider a fixed T-contract of the form 2 = @ (S(T)), and we now 
describe the upand-out version of 2 .  This is the contract which at the time of 
delivery, T, will pay 2 if the underlying price process during the entire contract 
period has stayed below the barrier L. If, at some time during the contract 
period, the price process exceeds L, then the contract is worthless. In formal 
terms this reads as follows. 
Definition 18.10 Take as given the T-wntmct 2 = @ (S(T)). Then the 
T-contract ZLO zs defined b y  
2 L O  = {@ (Sj')), y s ( t )  < L for all t E [O,Tl, 
if S(t) 2 L for some t E [0, TI. 
The pricing functional for zLO 
is denoted by FLO(t, s; a), or according to our 
earlier notational convention, by 
(t, s) . 
L as a superscript indicates an "upv-type contract, whereas the superscript 0 
indicates that the contract is an "out" contract. As in the previous sections we 
will relate the upand-out contract to an associated standard contract. To this 
end we need to define, for a fixed contract function @, the function aL, 
which is 
the function 
"chopped off" above L. 
Definition 18.11 For a fied function @ the function aL is defined by 
aL(x) = { a t ) ,  for x < L 
forx 2 L. 
In other words, @=(x) = @(x) I {x < L). 
The main result of this section is the following theorem, which is parallel to 
Theorem 18.8. The proof is almost identical. 
Theorem 18.12 (Pricing upand-out contracts) Consider a fied T-claim 
2 = @(S(T)). Then the pricing function, FLO, of the wwesponding up-and-out 
contract zLO 
is given, for S < L, by 
F ~ O ( ~ ,  
S, a )  = F (t, S, aL) - (5)"'"' F ( t, -,aL 
y ) 
where we have wed the notation 
- 
1
2
 
r = r - - 2 0 .  

OUT CONTRACTS 
261 
18.2.3 Examples 
In this section we will use Theorems 18.8 and 18.12, together with the linearity 
lemma 18.7, to give a systematic account of the pricing of a fairly wide class 
of barrier derivatives, including barrier call and put options. Let us define the 
following standard contracts, which will be the basic building blocks in the sequel. 
Definition 18.13 Fix a delivery time T. For jixed parameters K and L define 
the claims S T ,  BO, H ,  and C by 
C(x; K )  = max [x - K, O] . 
(18.13) 
The contract S T  ( S T  for "stock") thus gives the owner (the price of) one unit of 
the underlying stock at delivery time T, whereas BO is an ordinary zero coupon 
bond paying one at maturity T. The H-contract ( H  stands for the Heaviside 
function) gives the owner one if the value of the underlying stock exceeds L at 
delivery time T, otherwise nothing is paid out. The C-claim is of course the 
ordinary European call with strike price K. We note in passing that H(x; L) = 
HL 
(2). 
We now list the pricing functions for the standard contracts above. The value 
of ST at time t is of course equal to the value of the underlying stock at the 
same time, whereas the value of BO at t is e-T(T-t). The value of C is given by 
the Black-Scholes formula, and the value of H is easily calculated by using risk 
neutral valuation. Thus we have the following result. 
Lemma 18.14 The contracts (18.10)-(18.13) with delivery time T are priced 
at time t as follows (with the pricing function in bold). 
C(t, s; K )  = c(t, s; K), 
where c(t, s; K )  is the usual Black-Scholes formula. 
We may now put this machinery to some use and start with the simple case 
of valuing a down-and-out contract on a bond. This contract will thus pay out 
1 dollar at time T if the stock price is above the level L during the entire contract 

262 
BARRIER OPTIONS 
period, and nothing if the stock price at some time during the period is below 
or equal to L. 
A direct application of Theorem 18.8 gives us the formula 
FLO 
(t, S; BO) = F (t, S; BOL) - 
Obviously we have BOL(x) = H(x; L) for all x so we have the following result. 
Lemma 18.15 The down-and-out bond with barrier L is priced, for s > L, by 
the formula 
where H(t, s; L) is given by Lemma 18.14. 
We continue by pricing a down-and-out contract on the stock itself (no option 
is involved). Thus we want to compute FLO(t, S; ST) and Theorem 18.8 gives us 
, ., pr< I , '  . 
(
)
 
( 
) 
(18.15) 
FLO(t, S; ST) = F(t, S; STL) - 
F t,-;STL 
. 
A quick look at a figure gives us the relation 
STL(x) = L . H(x; L) + C(X; L). 
Substituting this into (18.15) and using linearity (Lemma 18.7) we get 
= F (t, s; LH(*, L) + C(+, L)) - - 
+C(*;L) 
+ 'F (t, s; C(*; 
L)) - (:)"I2 F ( t,-;C(*;L) 
L' s 
) . 
Summarizing we have the following. 


264 
BARRIER OPTIONS 
Putting this relation into (18.16), and using the linear property of pricing, we 
get (18.18). 
As we have seen, almost all results are fairly easy consequences of the linearity 
of the pricing functional. In Section 9.1 we used this linearity to prove the stand- 
ard put-call parity relation for standard European options, and we can now 
derive the put-call parity result for down-and-out options. 
Drawing a figure we see that P(x; K )  = K - x + C(x; K), so, in terms of the 
standard contracts, we have 
P(x; K )  = K BO(X) - ST(x) + C(x; K). 
Using Corollary 18.9 we immediately have the following result. Note that when 
L = 0 we have the usual put-call parity. 
Proposition 18.18 (Put-call parity) The down-and-out put price PLO, and 
call price CLOY are related by the formula 
Here BLO and STLo are given by Lemmas 18.15 and 18.16, whereas CLO is 
given by Proposition 18.17. 
We end this section by computing the price of a European upand-out put 
option with barrier L and strike price K. 
Proposition 18.19 (Upand-out put) The price of an up-and-out European 
put option is given by the following formulas. 
If L > K ,  then for s < L: 
If L > K ,  then for s < L: 
pLO(t, 
S; K )  = P(t, S; L) - (K - L)H(t, s; L) 
Proof If L > K then pL(s; K )  = P(s; K), and then (18.20) follows 
immediately from Proposition 18.12. 
If L < K then it is easily seen that 
I 
Linearity and Proposition 18.12 give us (18.21). 
I7 

IN CONTRACTS 
265 
18.3 I n  Contracts 
In this section we study contracts which will start to exist if and only if the price 
of the underlying stock hits a prespecified barrier level at some time during the 
contract period. We thus fix a standard T-claim of the form 2 = 9 (S(T)), and 
we also fix a barrier L. We start by studying the "down-and-in" version of 2 ,  
which is defined as follows: 
a If the stock price stays above the barrier L during the entire contract 
period, then nothing is paid to the holder of the contract. 
If the stock price, at some time before the delivery time T, hits the barrier 
L, then the amount 2 is paid to the holder of the contract. 
We will write the down-and-in version of 2 as ZLI, and the formal definition 
Definition 18.20 Take as given the T-contract 2 = 9 (S(T)). Then the 
T-contract ZLI is defined by 
if S(t) > L for all t E [0, TI, 
2Lz = {a ($T)), 
if ~ ( t )  
< L for some t E [o, 4. 
(18.22) 
The pricing function for ZLI is denoted by FLI(t, s; a ) ,  or sometimes by 
Concerning the notation, L as a subscript indicates a "down" contract, 
whereas the subscript I denotes an "in" contract. Pricing a down-and-in con- 
tract turns out to be fairly easy, since we can in fact price it in terms of the 
corresponding down-and-out contract. 
Lemma 18.21 (In-out parity) 
FLI(t, S; 9 )  = F(t, S; a )  - F L ~ ( ~ ,  
S; a), VS. 
Proof If, at time t, you have a portfolio consisting of a down-and-out version of 
2 as well as a down-and-in version of 2 (with the same barrier L) then obviously 
you will receive exactly Z at time T. We thus have 
F(t, S; 9 )  = F ~ z ( t ,  
S; 9 )  + F ~ o ( t ,  
S; a). 
We can now formulate the basic result. 
Proposition 18.22 (Pricing down-and-in contracts) Consider 
a 
fied 
T-contract 2 = 9 (S(T)). Then the price of the corresponding down-and-in 
contract ZLI is given by 
(t)"'"' ( y ) 
FLl(t, S; 9 )  = ~ ( t ,  
S; aL) + - 
F t, -;aL 
. 

266 
BARRIER OPTIONS 
Proof Fkom the equality QI = @L + aL we have 
Now use this formula, the lemma above, and Theorem 18.8. 
17 
The treatment of "upand-in" contracts is of course parallel to down-and-in 
contracts, so we only give the basic definitions and results. We denote the 
upand-in version of 2 by ZL', and the definition of zL' is as follows: 
If the stock price stays below the barrier L during the entire contract 
period, then nothing is paid to the holder of the contract. 
If the stock price, at some time before the delivery time T, hits the barrier 
L, then the amount 2 is paid to the holder of the contract. 
Corresponding to Lemma 18.21, we have 
F='(~,s; a) = F(t, S; a) - F ~ O ( ~ ,  
s; QI), 
Vs, 
(18.23) 
and from this relation, together with the pricing formula for upand-out 
contracts, we have an easy valuation formula. 
Proposition 18.23 (Pricing up-and-in contracts) Consider a @ed T- 
contract 2 = QI (S(T)). Then the price of the corresponding up-and-in contract 
zL' is given by 
We end this section by giving, as an example, the pricing formula for 
a down-and-in European call with strike price K. 
Proposition 18.24 (Down-and-in European call) For s > L the down- 
and-in European call option is priced as follows: 
For L < K :  
2i;/02 
CLI(t, S; K) = (:) 
C (t, :; 
K) 
ForL > K: 
2i;/u2 
C ~ l ( t ,  
S; K) = (:) 
{ C  (t, ?; 
K) + (L - K)H 
- (L - K)H(t, S; L). 

LADDERS 
, 18.4 Ladders 
i Let us take as given 
A finite increasing sequence of real numbers 
I 
0 =ao < a1 < 
< a ~ .  
This sequence will be denoted by a .  
i 
Another finite increasing sequence of real numbers 
I 
This sequence will be denoted by a. 
I Note that the number N is the same in both sequences. The interval [a,, a,+l) 
1 will play an important role in the sequel, and we denote it by Dn, with DN 
defined as DN = [aN, 
m). For a fixed delivery time T we will now consider 
a new type of contract, called the "(a, P)-ladder", which is defined as follows. 
Definition 18.25 The (a,P)-ladder with delivery time T is a T-claim 2 ,  
described by 
N 
I 
\ 
In other. words, if the realized maximum of the underlying stock during the 
contract period falls within the interval D,, then the payout at T is P,. A typical 
ladder used in practice is the forward ladder call with strike price K. For this 
contract a is exogenously specified, and P is then defined as 
The a-sequence in this case acts as a sequence of barriers, and the ladder call 
allows you to buy (at time T )  the underlying asset at the strike price K, while 
selling it (at T )  at the highest barrier achieved by the stock price during the con- 
tract period. The ladder call is intimately connected to the lookback forward call 
(see the next section), to which it will converge as the a-partition is made finer. 
The general (a, P)-ladder is fairly easy to value analytically, although the 
actual expressions may look formidable. To see this let us define the following 
series of upand-in contracts. 
Definition 18.26 For a given pair (a, P), the series of contracts 20, . . . , ZN is 
defined by 

BARRIER OPTIONS 
obvic 
The point of introducing the 2,-contracts is that we have the following 
,us relation 
N 
I 
Thus a ladder is simply a sum of a series of up-and-in contracts. We see that 
in fact 2, is an upand-in contract on /3, 
-/3n-l 
bonds, with barrier a,. Thus we 
may use the results of the preceding sections to value 2,. The result is as follows. 
Proposition 18.27 (Ladder pricing formula) Consider an ( a ,  /3) -ladder 
with delivery time T .  Assume that S(t) = s and that Ms(t) E Dm. 
Then the 
price, Il (t), of the ladder is given by 
1 
n ( t )  = /%TI + 
%Fan' (t, s; BO), 
n=m+l 
1 
where "I, = pn - /3n-1, and 
d 
Proof Exercise for the reader. 
I 
18.5 Lookbacks 
3 
Lookback options are contracts which at the delivery time T allow you to take 
advantage of the realized maximum or minimum of the underlying price process 
over the entire contract period. Typical examples are 
I 
I 
S(T) - min S(t) 
lookback call, 
t<T 
% m  S(t) - S(T) 
lookback put, 
S(t) - K, 0 
forward lookback 
I 
S(t), 0 
forward lookback 
I 
call, 
put. 
We will confine ourselves to give a sketch of the pricing of a lookback put; 
for further results see the Notes below. 

LOOKBACKS 
269 
From general theory, the price of the lookback put at t = 0 is given by 
= e-rT E~ max S(t) - e-'T~Q [S(T)]. 
[ d T  
1 
With S(0) = s, the last term is easily obtained as 
and it remains to compute the term EQ [maxtsT S(t)]. To this end we recall that 
S(t) is given by 
S(t) = exp {Ins + ft + u W ( t ) )  = ex(t), 
where 
Thus we see that 
Ms(T) = e M x  (TI, 
and the point is of course that the distribution for Mx(T) is known to us from 
Proposition 18.4. Using this proposition we obtain the distribution function, F, 
for Mx (T) as 
i 
F ( ~ )  
= N (x - Ins - 
- exp { 
2f(x - Ins) } N -
 
( x -f;+fT) 
a
0
 
02 
9 
for all x 2 Ins. From this expression we may compute the density function 
f = F', and then the expected value is given by 
After a series of elementary, but extremely tedious, partial integrations we end 
up with the following result. 
Proposition 18.28 (Pricing formula for lookback put) The price, at t = 0, 
of the lookback put is given by 
where 

BARRIER OPTIONS 
18.6 Exercises 
In all exercises below we assume a standard Black-Scholes model. 
Exercise 18.1 An "all-or-nothing" contract, with delivery date T, and strike 
price K, will pay you the amount K, if the price of the underlying stock exceeds 
the level L at some time during the interval [0, t]. Otherwise it will pay nothing. 
Compute the price, at t < T, of the all-or-nothing contract. In order to avoid 
trivialities, we assume that S(s) < L for all s 5 t. 
Exercise 18.2 Consider a binary contract, i.e. a T-claim of the form 
x = I[a,b] (ST), 
where as usual I is the indicator function. Compute the price of the down-and-out 
version of the binary contract above, for all possible values of the barrier L. 
Exercise 18.3 Consider a general down-and-out contract, with contract func- 
tion a, as descibed in Section 18.2.1. We now modifiy the contract by adding a 
fixed "rebate" A, and the entire contract is specified as follows: 
If S(t) > L for all t 5 T then @(S(T)) is paid to the holder. 
If S(t) 5 L for some t 5 T then the holder receives the fixed amount A. 
Derive a pricing formula for this contract. 
Hint: Use Proposition 18.4. 
Exercise 18.4 Use the exercise above to price a down-and-out European call 
with rebate A. 
Exercise 18.5 Derive a pricing formula for a down-and-out version of the T 
contract X = iP(S(T)), when S has a continuous dividend yield 6. Specialize to 
the case of a European call. 
18.7 Notes 
Most of the concrete results above are standard. The general Theorem 18.8 and 
its extensions seem, however, to be new. For barrier options we refer to Rubin- 
stein and Reiner (1991), and the survey in Carr (1995). Two standard papers on 
lookbacks are Come and Viswanathan (1991), and Goldman et al. (1979). See 
also Musiela and Rutkowski (1997). 

I 
STOCHASTIC OPTIMAL CONTROL 
19.1 An Example 
1 Let us consider an economic agent over a fixed time interval [0, TI. At time 
I t = 0 the agent is endowed with initial wealth xo and his/her problem is how to 
1 allocate investments and consumption over the given time horizon. We assume 
' that the agent's investment opportunities are the following: 
The agent can invest money in the bank at the deterministic short rate of 
, 
interest r, i.e. he/she has access to the risk free asset B with 
dB = rB dt. 
(19.1) 
The agent can invest in a risky asset with price process St, where we assume 
that the S-dynamics are given by a standard Black-Scholes model 
d S  = oSdt + aSdW. 
(19.2) 
We denote the agent's relative portfolio weights at time t by u,O (for the riskless 
asset), and u! (for the risky asset) respectively. His/her consumption rate at 
time t is denoted by q. 
We restrict the consumer's investment-consumption strategies to be self- 
financing, and as usual we assume that we live in a world where continuous 
trading and unlimited short selling is possible. If we denote the wealth of the 
consumer at time t by Xt, it now follows from Lemma 6.4 that (after a slight 
rearrangement of terms) the X-dynamics are given by 
1 
dXt = Xt [uir + uia] dt - q dt + uiaxt dWt. 
(19.3) 
The object of the agent is to choose a portfolio-consumption strategy in such 
a way as to maximize &/her total utility over [0, T ] ,  and we assume that this 
utility is given by 
I3 [I' F(t,G)dt+ @(xT)] 
, 
(19.4) 
where F is the instantaneous utility function for consumption, whereas @ is a 
4egacy" function which measures thp utility of having some money left at the 
end of the period. 
A natural constraint on consumption is the condition 
QLO, Vt20, 
(19.5) 

272 
STOCHASTIC OPTIMAL CONTROL 
and we also have of course the constraint 
Depending upon the actual situation we may be forced to impose other con- 
straints (it may, say, be natural to demand that the consumer's wealth never 
becomes negative), but we will not do this at the moment. 
We may now formally state the consumer's utility maximization problem as 
follows: 
A problem of this kind is known as a stochastic optimal control problem. 
In this context the process X is called the state process (or state variable), 
the processes uO, ul, c are called control processes, and we have a number of 
control constraints. In the next sections we will study a fairly general class 
of stochastic optimal control problems. The method used is that of dynamic 
programming, and at the end of the chapter we will solve a version of the 
problem above. 
19.2 The Formal Problem 
We now go on to study a fairly general class of optimal control problems. To this 
end, let p(t, x, u) and u(t, x, u) be given functions of the form 
For a given point xo. E Rn we will consider the following controlled 
stochastic differential equation: 
dXt = C1 (t, Xt , ut) dt + u (t, Xt , ut) dWt , 
(19.12) 
XO = 50. 
(19.13) 
We view the n-dimensional process X as a state process, which we are trying 
to "control" (or "steer"). We can (partly) control the state process X by choosing 
the k-dimensional control process u in a suitable way. W is a d-dimensional 

THE FORMAL PROBLEM 
273 
Wiener process, and we must now try to give a precise mathematical meaning 
to the formal expressions (19.12)-(19.13). 
Remark 19.2.1 In this chapter, where we will work under a fixed measure, all 
Wiener processes are denoted by the letter W. 
Our first modeling problem concerns the class of admissible control processes. 
In most concrete cases it is natural to require that the control process u is adapted 
to the X process. In other words, at time t the value ut of the control process is 
only allowed to "depend" on past observed values of the state process X. One 
natural way to obtain an adapted control process is by choosing a deterministic 
g
:
~
+
~
~
n
+
~
k
,
 
and then defining the control process u by 
ut = g (t, Xt). 
Such a function g is called a feedback control law, and in the sequel we will 
restrict ourselves to consider only feedback control laws. For mnemo-technical 
purposes we will often denote control laws by u(t, x), rather than g(t,x), and 
write ut = u(t, Xt). We use boldface in order to indicate that u is a function. In 
contrast to this we use the notation u (italics) to denote the value of a control 
at a certain time. Thus u denotes a mapping, whereas u denotes a point in R ~
Suppose now that we have chosen a fixed control law u(t, x). Then we can 
insert u into (19.12) to obtain the standard SDE 
dXt = P (4 Xt, u(t, Xt)) dt + 0 (t, xt, ~ ( t ,  
xt)) dwt. 
(19.14) 
In most concrete cases we also have to satisfy some control constraints, 
and we model this by taking as given a fixed subset U C Rk and requiring that 
ut E U for each t. We can now define the class of admissible control laws. 
Definition 19.1 A control law u is called admissible if 
u(t,x) E U for all t E R+ and all x E Rn. 
For any given initial point (t, x) the SDE 
dXs = P (8, Xs, U(S, Xs)) + 0 (s, Xs, U(S, Xs)) dWs, 
xt = x 
has a unique solution. 
I ;The class of admissible control laws is denoted by U. 
For a given control law u, the solution process X will of course depend on the 
initial value x, as well as on the chosen control law u. To be precise we should 

274 
STOCHASTIC OPTIMAL CONTROL 
I 
therefore denote the process X by XZ*", but sometimes we will suppress x or u. 
We note that eqn (19.14) looks rather messy, and since we will also have to deal 
with the It8 formula in connection with (19.14) we need some more streamlined 
notation. 
i 
Definition 19.2 Consider eqn (19.14), and let ' denote matrix transpose. 
For any fied vector u E R k,  the functions p", uu, and Cu are defined by 
For any control law u, the functions pU, a U, C U(t,x), and F U(t,x) are 
defined by 
pU(t, 2) = At, 2, u(t, x ) ) ,  
ffU(tl 
5) = ~ ( t ,  
2, ~ ( t ,  
XI), 
CU(t, 2) = ~ ( t ,  
2, ~ ( t ,  
x))u(t,x, u(t,x))', 
F U(t, x )  = F(t, x, u(t, x)). 
For any fied vector u E R k, the partial diffeerenticll operator A" is 
defined by 
1 
For any control law u, the partial differential operator d" is defined by 
I 
Given a control law u we will sometimes write eqn (19.14) in a convenient 
shorthand notation as 
dXy = bU dt + uU dWt. 
(19.15) 
For a given control law u with a corresponding controlled process X U  we 1 
will also often use the shorthand notation ut instead of the clumsier e: 
. 
- .  
The reader should be aware of the fact that the existence assumption in 
the definition above is not at all an innocent one. In many cases it is natural 
to consider control laws which are "rapidly varying", i.e. feedback laws u(t, x) 
which are very irregular as functions of the state variable x. Inserting such an 

THE HAMILTON-JACOBI-BELLMAN EQUATION 
275 
irregular control law into the state dynamics will easily give us a very irregular 
drift function p (t, x, u(t, x)) (as a function of x), and we may find ourselves 
outside the nice Lipschitz situation in Proposition 5.1, thus leaving us with a 
I highly nontrivial existence problem. The reader is referred to the literature for 
details. 
We now go on to the objective function of the control problem, and therefore 
we consider as given a pair of functions 
b 
if? : Rn + R. 
b 
Now we define the value function of our problem as the function 
defined by 
I 
where Xu is the solution to (19.14) with the given initial condition Xo = xo. 
Our formal problem can thus be written as that of maximizing Jo(u) over 
all u E U, 
and we define the optimal value 
by 
30 = sup 31 (u). 
UEU 
If there exists an admissible control law u with the property that 
then we say that u is an optimal control law for the given problem. Note that, 
as for any optimization problem, the optimal law may not exist. For a given 
concrete control problem our main objective is of course to find the optimal 
control law (if it exists), or at least to learn something about the qualitative 
behavior of the optimal law. 
19.3 T h e  Hamilton-Jacobi-Bellman Equation 
Given an optimal control problem we have two natural questions to answer: 
(a) Does there exist an optimal control law? 
(b) Given that an optimal control exists, how do we find it? 
In this text we will mainly be concerned with problem (b) above, and the meth- 
odology used will be that of dynamic programming. The main idea is to 
embed our original problem into a much larger class of problems, and then to tie 

276 
STOCHASTIC OPTIMAL CONTROL 
all these problems together with a PDE known as the Hamilton-Jacobi-Bellman 
equation. The control problem is then shown to be equivalent to the problem of 
finding a solution to the HJB equation. 
We will now describe the embedding procedure, and for that purpose we 
choose a fixed point t in time, with 0 5 t 5 T. We also choose a fixed point x in 
the state space, i.e. x E Rn. For this fixed pair (t, x) we now define the following 
control problem. 
Definition 19.3 The control problem P(t,x) is defined as the problem to 
maximize 
E,,, [jT 
F(s, x:, 
us) 
given the dynamics 
dX," = p (8, X,U, U(S, X,")) ds + u (8, X:, 
U(S, X:)) 
dWB, 
(19.17) 
xt = x, 
and the constmints 
4% 
9) E U, V(s, Y) E [t, TI x R". 
Observe that we use the notation s and y above because the letters t and x 
are already used to denote the fixed chosen point (t, x). 
We note that in terms of the definition above, our original problem is the 
problem P(0, xo) . A somewhat drastic interpretation of the problem P(t, x) is 
that you have fallen asleep at time zero. Suddenly you wake up, noticing that 
the time now is t and that your state process while you were asleep has moved 
to the point x. You now try to do as well as possible under the circumstances, so 
you want to maximize your utility over the remaining time, given the fact that 
you start at time t in the state x. 
We now define the value function and the optimal value function. 
Definition 19.4 
The value function 
J : R +  x R n  x U + R  
is defined by 
T 
J(t,., u) = E [i 
F(s, 
given the dynamzcs (19.17)-(19.18). 
The optimal value function 
V : R + x R n + R  

I 
THE HAMILTON-JACOBI-BELLMAN EQUATION 
is defined by 
V(t, x) = sup J(t, x, u). 
u€U 
to , Thus J(t, x, u) is the expected utility of using the control law u over the time 
interval [t, TI, given the fact that you start in state x at time t. The optimal value 
function gives you the optimal expected utility over [t, TI under the same initial 
conditions. 
The main object of interest for us is the optimal value function, and we 
now go on to derive a PDE for V. It should be noted that this derivation is 
largely heuristic. We make some rather strong regularity assumptions, and we 
disregard a number of technical problems. We will comment on these problems 
later, but to see exactly which problems we are ignoring we now make some basic 
assumptions. 
Assumption 19.3.1 We assume the following: 
1. There exists an optimal control law u. 
2. The optimal value function V is regular in the sense that V E C1t2. 
3. A number of limiting procedures in the following arguments can be justified. 
We now go on to derive the PDE, and to this end we fix (t, x) E (0, T) x Rn. 
Furthermore we choose a real number h (interpreted as a "small" time increment) 
such that t + h < T. We choose a fixed but arbitrary control law u, and define 
the control law u* by 
u*(s,Y) = { 
4 3 ,  Y), (s, 9) E It, t + hl x En, 
~ ( s ,  
Y), (s, 9) E (t + h, TI x Rn. 
In other words, if we use u* then we use the arbitrary control u during the time 
interval [t, t + h], and then we switch to the optimal control law during the rest 
of the time period. 
The whole idea of dynamic programming actually boils down to the following 
procedure: 
First, given the point (t,x) as above, we consider the following two 
strategies over the time interval [t , TI: 
Strategy I. Use the optimal law Ez. 
Strategy 11. Use the control law u* defined above. 
We then compute the expected utilities obtained by the respective 
strategies. 
Finally, using the obvious fact that Strategy I by definition has to be at 
least as good as Strategy 11, and letting h tend to zero, we obtain our 
fundamental PDE. 
We now carry out this program. 

278 
STOCHASTIC OPTIMAL CONTROL 
Expected utility for strategy I: This is trivial, since by definition the utility 
is the optimal one given by J(t, x, u) = V(t, x). 
Expected utility for strategy 11: We divide the time interval [t,T] into two 
parts, the intervals [t, t + h] and (t + h, TI, respectively. 
The expected utility, using Strategy 11, for the interval [t, t + h) is given by 
E~,x 
[ f h  
F(s,X,U,u,) ds . I 
In the interval [t + h,T] we observe that at time t + h we will be in 
the (stochastic) state X,U+h.. Since, by definition, we will use the optimal 
strategy during the entire interval [t + h,T] we see that the remaining 
expected utility at time t + h is given by V(t + h, X,U+h). Thus the expected 
utility over the interval [t + h, TI, conditional on the fact that at time t we 
are in state x, is given by 
Et, [V(t + h, X,U,h)l. 
Thus the total expected utility for Strategy I1 is 
Et,- [rh 
F(s,X,U,u,) ds +V(t + h,X,U,,) . I 
Comparing the strategies: We now go on to compare the two strategies, and 
since by definition Strategy I is the optimal one, we must have the inequality 
t+h 
V(t.1) L Et,, [i F(s,X,U,us) ds + V(t + h,X:+h) I 
We also note that the inequality sign is due to the fact that the arbitrarily chosen 
control law u which we use on the interval [t, t + h] need not be the optimal one. 
In particular we have the following obvious fact. 
Remark 19.3.1 We have equality in (19.20) if and only if the control law u is 
an optimal law u. (Note that the optimal law does not have to be unique.) 
Since, by assumption, V is smooth we now use the It6 formula to obtain (with 
obvious notation) 
t+h av 
V(t + h, Xr+h) = V(t, x) + 1 {%(s, x;) + duV(s, X:) 
t+h 
+ 1 V,V(S, X,U)gu dWs. 

THE HAMILTON-JACOBI-BELLMAN EQUATION 
279 
If we apply the expectation operator Et,, to this equation, and assume enough 
integrability, then the stochastic integral will vanish. We can then insert the res- 
ulting equation into the inequality (19.20). The term V(t, x) will cancel, leaving 
us with the inequality 
av 
4,. [Iih [i x:, 
us) + =(a, C) 
+ dUV(s, X:) ds 5 0. 
(19.22) 
1 I 
Going to t h e  limit: Now we divide by h, move h within the expectation and 
let h tend to zero. Assuming enough regularity to allow us to take the limit 
within the expectation, using the fundamental theorem of integral calculus, and 
recalling that Xt = x, we get 
av 
F(t,x,u) + x(t,x) + dUV(t,x) < 0, 
(19.23) 
where u denotes the value of the law u evaluated at (t, x), i.e. u = u(t, x). Since 
the control law u was arbitrary, this inequality will hold for all choices of u E U, 
and we will have equality if and only if u = G(t, x). We thus have the following 
av 
-(t, 
x) + sup {F(t, x,u) + duV(t,x)) = 0. 
at 
uEU 
During the discussion the point (t, x) was fixed, but since it was chosen as an 
arbitrary point we see that the equation holds in fact for all (t, x) E (0, T) x Rn. 
Thus we have a (nonstandard type of) PDE, and we obviously need some 
boundary conditions. One such condition is easily obtained, since we obviously 
(why?) have V(T, x) = @(x) for all x E Rn. We have now arrived at our goal, 
amilton-Jacobi-Bellman equation, (often referred to as the HJB 
Theorem 19.5 (Hamilton-Jacobi-Bellman equation) Under Assumption 
19.3.1, the following hold: 
1. V satisfies the Hamilton-Jacobi-Bellman equation 
~(t,x)+sup{F(t,x,~)+d~V(t,x)}=O, 
V(t,x) E (0,T) x Rn 
UEU 
V(T,x) =@(x), V X E  Rn. 
2. For each (t, x) E [0, TI x Rn the supremum in the HJB equation above is 
attained by u = G(t, x). 

