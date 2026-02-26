# Binomial Model & Discrete Arbitrage Theory

!!! info "Source"
    **Arbitrage Theory in Continuous Time** by Tomas Björk, Oxford University Press, 2nd ed., 2004.
    These notes are used for educational purposes.

## The Binomial Model

t 
INTRODUCTION 
1.1 Problem Formulation 
The main project in this book consists in studying theoretical pricing models for 
those financial assets which are known as financial derivatives. Before we give 
the formal definition of the concept of a financial derivative we will, however, by 
, 
means of a concrete example, introduce the single most important example: the 
1 European call option. 
i: 
Let us thus consider the Swedish company C&H, which today (denoted by 
I t = 0) has signed a contract with an American counterpart ACME. The contract 
stipulates that ACME will deliver 1000 computer games to C&H exactly six 
months from now (denoted by t = T). Furthermore it is stipulated that C&H 
will pay 1000 US dollars per game to ACME at the time of delivery (i.e. at 
t = T). For the sake of the argument we assume that the present spot currency 
rate between the Swedish krona (SEK) arid the US dollar is 8.00 SEK/$. 
One of the problems with this contract from the point of view d C&H is 
that it involves a considerable currency risk. Since C&H does not know the 
currency rate prevailing six months from now, this means that it does not know 
how many SEK it will have to pay at t = T. If the currency rate at t = T is 
still 8.00 SEK/$ it will have to pay 8,000,000 SEK, but if the rate rises to, say, 
I 8.50 it will face a cost of 8,500,000 SEK. Thus C&H faces the problem of how 
"0 
guard itself against this currency risk, and we now list a number of natural 
strategies. 
The most naive stratgey for C&H is perhaps that of buying $1,000,000 
today at the price of 8,000,000 SEK, and then keeping this money (in a 
Eurodollar account) for six months. The advantage of this procedure is 
f course that the currency risk is completely eliminated, but there are 
also some drawbacks. First of all the strategy above has the consequence 
of tying up a substantial amount of money for a long period of time, but 
an even more serious objection may be that C&H perhaps does not have 
access to 8,000,000 SEK today. 
2. A more sophisticated arrangement, which does not require any outlays at 
all today, is that C&H goes to the forward market and buys a forward 
contract for $1,000,000 with delivery six months from now. Such a con- 
tract may, for example, be negotiated with a commercial bank, and in the 
contract two things will be stipulated. 
The bank will, at t = T, deliver $1,000,000 to C&H. 
C@H will, at t = T, pay for this delivery at the rate of K SEK/$. 

2 
INTRODUCTION 
The exchange rate K, which is called the forward price, (or forward 
exchange rate) at t = 0, for delivery at t = T, is determined at t = 0. By 
the definition of a forward contract, the cost of entering the contract equals 
zero, and the forward rate K is thus determined by supply and demand on 
the forward market. Observe, however, that even if the price of entering the 
forward contract (at t = 0) is zero, the contract may very well fetch a nonzero 
price during the interval [0, TI. 
Let us now assume that the forward rate today for delivery in six months 
equals 8.10 SEK/$. If C&H enters the forward contract this simply means that 
there are no outlays today, and that in six months it will get $1,000,000 at the 
predetermined total price of 8,100,000 SEK. Since the forward rate is determined 
today, C&H has again completely eliminated the currency risk. 
However, the forward contract also has some drawbacks, which are related 
to the fact that a forward contract is a binding contract. To see this let us look 
at two scenarios. 
Suppose that the spot currency rate at t = T turns out to be 8.20. Then 
C&Hcan congratulate itself, because it can now buy dollars at the rate 8.10 
despite the fact that the market rate is 8.20. In terms of the million dollars 
at stake C&Hhas thereby made an indirect profit of 8,200,000-8,100,000 = 
100,000 SEK. 
Suppose on the other hand that the spot exchange rate at t = T turns out 
to be 7.90. Because of the forward contract this means that C&H is forced 
to buy dollars at the rate of 8.10 despite the fact that the market rate is 
7.90, which implies an indirect loss of 8,100,000-7,900,000 = 200,000 SEK. 
3. What C&H would like to have of course is a contract which guards it 
against a high spot rate at t = T, while still allowing it to take advantage 
of a low spot rate at t = T. Such contracts do in fact exist, and they 
are called European call options. We will now go on to give a formal 
definition of such an option. 
Definition 1.1 A European call option on the amount of X US dollars, with 
strike price (exercise price) K SEK/$ and exercise date T is a contract 
written at t = 0 with the following properties. 
The holder of the contract has, exactly at the time t = T ,  the right to buy 
X US dollars at the price K SEK/$. 
The holder of the option has no obligation to buy the dollars. 
Concerning the. nomenclature, the contract is called an option precisely 
because it gives the holder the option (as opposed to the obligation) of buy- 
ing some underlying asset (in this case US dollars). A call option gives the 
holder the right to buy, wheareas a put option gives the holder the right to sell 
the underlying object at a prespecified price. The prefix European means that 

the option can only be exercised at exactly the date of expiration. There also 
exist American options, which give the holder the right to exercise the option 
at any time before the date of expiration. 
Options of the type above (and with many variations) are traded on options 
markets all over the world, and the underlying objects can be anything from 
foreign currencies to stocks, oranges, timber or pig stomachs. For a given under- 
lying object there are typically a large number of options with different dates of 
expiration and different strike prices. 
We now see that CtYHcan insure itself against the currency risk very elegantly 
by buying a European call option, expiring six months from now, on a million 
dollars with a strike price of, for example, 8.00 SEK/$. If the spot exchange rate 
at T exceeds the strike price, say that it is 8.20, then CtYH exercises the option 
and buys at 8.00 SEK/$. Should the spot exchange rate at T fall below the strike 
price, it simply abstains from exercising the option. 
Note, however, that in contrast to a forward contract, which by definition 
has the price zero at the time at which it is entered, an option will always 
have a nonnegative price, which is determined on the existing options market. 
This means that our friends in CBH will have the rather delicate problem of 
determining exactly which option they wish to buy, since a higher strike price 
(for a call option) will reduce the price of the option. 
One of the main problems in this book is to see what can be said from a 
theoretical point of view about the market price of an option like the one above. 
In this context, it is worth noting that the European call has some properties 
which turn out to be fundamental. 
I 
r Since the value of the option (at T) depends on the future level of the 
spot exchange rate, the holding of an option is equivalent to a future 
I 
stochastic claim. 
r The option is a derivative asset in the sense that it is defined in terms 
., 
of some upderlying financial asset. 
Since the value of the option is contingent on the evolution of the exchange 
I 
rate, the option is often called a contingent claim. Later on we will give a 
precise mathematical definition of this concept, but for the moment the informal 
definition above will do. An option is just one example of a financial derivative, 
and a far from complete list of commonly traded derivatives is given below: 
European calls and puts 
American options 
r Forward rate agreements 
r Convertibles 
r Futures 
r Bonds and bond options 
r Caps and floors 
r Interest rate swaps 
R 

4 
INTRODUCTION 
Later on we will give precise definitions of (most of) these contracts, but at 
the moment the main point is the fact that financial derivatives exist in a great 
variety and are traded in huge volumes. We can now formulate the two main 
problems which concern us in the rest of the book. 
Main Problems: Take a fixed derivative as given. 
What is a "fair" price for the contract? 
Suppose that we have sold a derivative, such as a call option. Then we 
have exposed ourselves to a certain amount of financial risk at the date of 
expiration. How do we protect ("hedge") ourselves against this risk? 
Let us look more closely at the pricing question above. There exist two natural 
and mutually contradictory answers. 
Answer ,l: "Using standard principles of operations research, a reasonable price 
for the derivative is obtained by computing the expected value of the discounted 
future stochastic payoff." 
Answer 2: "Using standard economic reasoning, the price of a contingent claim, 
like the price of any other commodity, will be determined by market forces. In 
particular, it will be determined by the supply and demand curves for the market 
for derivatives. Supply and demand will in their turn be influenced by such factors 
as aggregate risk aversion, liquidity preferences, etc., so it is impossible to say 
anything concrete about the theoretical price of a derivative." 
The reason that there is such a thing as a theory for derivatives lies in the 
following fact. 
Main Result: Both answers above are incorrect! It is possible (given, of course, 
some assumptions) to talk about the "correct" price of a derivative, and this price 
is not computed by the method given in Answer 1. 
In the succeeding chapters we will analyze these problems in detail, but we 
can already state the basic philosophy here. The main ideas are as follows. 
Main Ideas 
A financial derivative is defined in terms of some underlying asset which 
already exists on the market. 
The derivative cannot therefore be priced arbitrarily in relation to 
the underlying prices if we want to avoid mispricing between the 
derivative and the underlying price. 
We thus want to price the derivative in a way that is consistent with the 
underlying prices given by the market. 
We are not trying to compute the price of the derivative in some "absolute" 
sense. The idea instead is to determine the price of the derivative in terms 
of the market prices of the underlying assets. 

2 
THE BINOMIAL MODEL 
In this chapter we will study, in some detail, the simplest possible nontrivial 
I 
model of a financial market-the binomial model. This is a discrete time model, 
a 
but despite the fact that the main purpose of the book concerns continuous time 
! $ 
models, the binomial model is well worth studying. The model is very easy to 
: 
understand, almost all important concepts which we will study later on already 
appear in the binomial case, the mathematics required to analyze it is at high 
\ 
school level, and last but not least the binomial model is often used in practice. 
I 
2.1 The One Period Model 
We start with the one period version of the model. In the next section we will 
(easily) extend the model to an arbitrary number of periods. 
2.1.1 Model Description 
Running time is denoted by the letter t, and by definition we have two points 
in time, t = 0 ("today") and t = 1 ("tomorrow"). In the model we have two 
assets: a bond and a stock. At time t the price of a bond is denoted by Bt, 
and the price of one share of the stock is denoted by St. Thus we have two price 
processes B and S. 
The bond price process is deterministic and given by 
C 
Bo = 1, 
B 1 = l + R .  
The constant R is the spot rate for the period, and we can also interpret the 
existence of the bond as the existence of a bank with R as its rate of interest. 
The stock price process is a stochastic process, and its dynarnical behavior is 
described as follows: 
s . u, with probability p,. 
S1 = s . d, with probability pd. 
I, It is often convenient to write this as 

THE BINOMIAL MODEL 
1 
FIG. 2.1. Price dynamics 
\ 
where Z is a stochastic variable defined as 
z = {  u, with probability p,. 
d, with probability pd. 
We assume that today's stock price s is known, as are the positive constants 
u ,  d, p, and pd. We assume that d < u ,  and we have of course p, + pd = 1. We 
can illustrate the price dynamics using the tree structure in Fig. 2.1. 
2.1.2 Portfolios and Arbitrage 
We will study the behavior of various portfolios on the (B, S) market, and to 
this end we define a portfolio as a vector h = (x, y). The interpretation is that 
x is the number of bonds we hold in our portfolio, whereas y is the number of 
units of the stock held by us. Note that it is quite acceptable for x and y to 
be positive as well as negative. If, for example, x = 3, this means that we have 
bought three bonds at time t = 0. If on the other hand y = -2, this means that 
we have sold two shares of the stock at time t = 0. In financial jargon we have 
a long position in the bond and a short position in the stock. It is an important 
F 
assumption of the model that short positions are allowed. 
Assumption 2.1.1 W e  assume the following institutional facts: 
Short positions, as well as fractional holdings, are allowed. In mathematical 
terms this means that every h E R2 is an allowed portfolio. 
There is no bid-ask spread, i.e. the selling price is equal to the buying price 
of all assets. 
There are no transactions costs of trading. 
The market is completely liquid, i.e. it is always possible to buy and/or sell 
unlimited quantities on the market. In particular it is possible to borrow 
unlimited amounts from the bank (by selling bonds short). 

THE ONE PERTOD MODEL 
7 
! 
i 
Consider now a fixed portfolio h = (x, y). This portfolio has a deterministic 
market value at t = 0 and a stochastic value at t = 1. 
Definition 2.1 The value process of the portfolio h is defined by 
or, in more detail, 
V: 
= x(1+ R) + ysZ. 
Everyone wants to make a profit by trading on the market, and in this context 
a so called arbitrage portfolio is a dream come true; this is one of the central 
concepts of the theory. 
Definition 2.2 A n  arbitrage portfolio is a portfolio h with the properties 
V: 
> 0, 
with probability 1. 
-. 
An arbitrage portfolio is thus basically a deterministic money making 
machine, and we interpret the existence of an arbitrage portfolio as equivalent to 
a serious case of mispricing on the market. It is now natural to investigate when a 
given market model is arbitrage free, i.e. when there are no arbitrage portfolios. 
Proposition 2.3 The model above is free of arbitrage if and only if the following 
conditions hold: 
d < ( l + R ) < u .  
(2.1) 
Proof The condition (2.1) has an easy economic interpretation. It simply says 
that the return on the stock is not allowed to dominate the return on the bond 
and vice versa. To show that absence of arbitrage implies (2.1), we assume that 
(2.1) does in fact not hold, and then we show that this implies an arbitrage oppor- 
tunity. Let us thus assume that one of the inequalities in (2.1) does not hold, so 
that we have, say, the inequality s(l+ R) > su. Then we also have s(l + R) > sd 
so it is always more profitable to invest in the bond than in the stock. An arbit- 
rage strategy is now formed by the portfolio h = (s, -I), i.e. we sell the stock 
short and invest all the money in the bond. For this portfolio we obviously have 
Vt = 0, and as for t = 1 we have 
which by assumption is positive. 

8 
THE BINOMIAL MODEL 
Now assume that (2.1) is satisfied. To show that this implies absence of 
arbitrage let us consider an arbitrary portfolio such that Voh = 0. We thus have 
x + ys = 0, i.e. x = -ys. Using this relation we can write the value of the 
portfolio at t = 1 as 
h - ys [u - (1 + R)] , if Z = u. 
- {ysid-(l+R)l, 
i f Z = d .  
1 
Assume now that y > 0. Then h is an arbitrage strategy if and only if we have 
i 
the inequalities 
but this is impossible because of the condition (2.1). The case y < 0 is treated 
similarly. 
At first glance this result is perhaps only moderately exciting, but we may 
write it in a more suggestive form. To say that (2.1) holds is equivalent to saying 
that 1 + R is a convex combination of u and d, i.e. 
where q,, qd > 0 and q, + qd = 1. In particular we see that the weights q, and 
qd can be interpreted as probabilities for a new probability measure Q with the 
property Q(Z = u) = q,, Q(Z = d) = qd. Denoting expectation w.r.t. this 
measure by EQ we now have the following easy calculation 
We thus have the relation 
which to an economist is a well-known relation. It is in fact a risk neutral 
valuation formula, in the sense that it gives today's stock price as the discounted 
expected value of tomorrow's stock price. Of course we do not assume that the 
i 
agents in our market are risk neutral-what we have shown is only that if we 
I 
use the Q-probabilities instead of the objective probabilities then we have in fact 
a risk neutral valuation of the stock (given absence of arbitrage). A probability 
measure with this property is called a risk neutral measure, or alternatively 
a risk adjusted measure or a martingale measure. Martingale measures 
will play a dominant role in the sequel so we give a formal definition. 

THE ONE PERIOD MODEL 
9 
Definition 2.4 A probability measure Q is called a martingale measure if 
the following condition holds: 
1 
B1 
so = - 
l + R  EQ [&I. 
I 
We may now state the condition of no arbitrage in the following way. 
Proposition 2.5 The market model is arbitrage free if and only if there exists 
a martingale measure Q. 
For the binomial model it is easy to calculate the martingale probabilities. 
The proof is left to the reader. 
Proposition 2.6 For the binomial model above, the martingale probabilities are 
given by 
( l + R ) - d  
u - ( l + R )  
u - d  
2.1.3 Contingent Claims 
I 
Let us now assume that the market in the preceding section is arbitrage free. 
We go on to study pricing problems for contingent claims. 
Definition 2.7 A contingent claim (financial derivative) is any stochastic 
variable X of the form X = @(Z), where Z is the stochastic variable driving the 
stock price process above. 
We interpret a given claim X as a contract which pays X SEK to the holder of 
1 
the contract at time t = 1. See Fig. 2.2, where the value of the claim at each node 
is given within the corresponding box. The function @ is called the contract 
function. A typical example would be a European call option on the stock with 
strike price K. For this option to be interesting we assume that sd < K < su. If 
' 
Sl > K then we use the option, pay K to get the stock and then sell the stock 
FIG. 2.2. Contingent claim 

THE BINOMIAL MODEL 
on the market for su, thus making a net profit of su - K. If S1 < K then the 
option is obviously worthless. In this example we thus have 
and the contract function is given by 
Our main problem is now to determine the "fair" price, if such an object 
exists at all, for a given contingent claim X. If we denote the price of X at time 
1 
t by n(t; X), then it can be seen that at time t = 1 the problem is easy to solve. 
In order to avoid arbitrage we must (why?) have 
and the hard part of the problem is to determine n(0; X). To attack this problem 
we make a slight detour. 
Since we have assumed absence of arbitrage we know that we cannot make 
. 
money out of nothing, but it is interesting to study what we can achieve on the 
market. 
Definition 2.8 A given contingent claim X is said to be reachable if there 
&ts 
a portfolio h such that 
v: = x, 
i 
with probability 1. In that case we say that the portfolio h is a hedging portfolio 
or a replicating portfolio. If all claims can be replicated we say that the market 
is complete. 
If a certain claim X is reachable with replicating portfolio h, then, from 
a financial point of view, there is no difference between holding the claim and 
- 
holding the portfolio. No matter what happens on the stock market, the value 
of the claim at time t = 1 will be exactly equal to the value of the portfolio at 
t = 1. Thus the price of the claim should equal the market value of the portfolio, 
and we have the following basic pricing principle. 
Pricing principle 1 If a claim X is reachable with replicating portfolio h, then 
1 
the only reasonable price process for X is given by 
The word "reasonable" above can be given a more precise meaning as in the 
following proposition. We leave the proof to the reader. 

THE ONE PERIOD MODEL 
11 
Proposition 2.9 Suppose that a claim X 
is reachable with replicating 
portfolio h. Then any price at t = 0 of the claim X ,  other than voh, will lead to 
an arbitrage possibility. 
We see that in a complete market we can in fact price all contingent claims, 
so it is of great interest to investigate when a given market is complete. For the 
binomial model we have the following result. 
Proposition 2.10 Assume that the general binomial model is free of arbitrage. 
Then it is also complete. 
Proof We fix an arbitrary claim X with contract function @, and we want to 
show that there exists a portfolio h = (x, y) such that 
If we write this out in detail we want to find a solution (x, y) to the following 
system of equations 
(1 + R)x + suy = @(u), 
(1 + R)x + sdy = @(d). 
Since by assumption u < d, this linear system has a unique solution, and a simple 
calculation shows that it is given by 
2.1.4 
Risk Neutral Valuation 
Since the binomial model is shown to be complete we can now price any contin- 
gent claim. According to the pricing principle of the preceding section the price 
at t = 0 is given by 
n(oi x) 
= v:, 
- 
and using the explicit formulas (2.2)-(2.3) we obtain, after some reshuffling 
of terms, 

12 
THE BINOMIAL MODEL 
Here we recognize the martingale probabilities qu and qd of Proposition 2.6. 
If we assume that the model is free of arbitrage, these are true probabilities (i.e. 
they are nonnegative), so we can write the pricing formula above as 
The right-hand side can now be interpreted as an expected value under the mar- 
tingale probability measure Q, so we have proved the following basic pricing 
result, where we also add our old results about hedging. 
Proposition 2.11 If the binomial model is free of arbitrage, then the arbitrage 
free price of a contingent claim X is given by 
Here the martingale measure Q is uniquely determined by the relation 
and the explicit expression for qu and qd are given in Proposition 2-6. Further- 
more the claim can be replicated using the portfolio 
1 
u@(d) - d@(u) 
x=-. 1+R 
u - d  
' 
(2.6) 
1 . @(u> - @(dl 
y = -  
s 
u - d  
' 
(2.7) 
We see that the formula (2.4) is a "risk neutral" valuation formula, and that 
the probabilities which are used are just those for which the stock itself admits 
a risk neutral valuation. The main economic moral can now be summarized. 
Moral 
The only role played by the objective probabilities is that they determine 
which events are possible and which are impossible. In more abstarct prob- 
abilistic terminology they thus determine the class of equivalent probability 
measures. See Chapter 10. 
When we compute the arbitrage free price of a financial derivative we carry 
out the computations as if we live in a risk neutral world. 
This does not mean that we de facto live (or believe that we live) in a risk 
neutral world. 
The valuation formula holds for all investors, regardless of their attitude 
towards risk, as long as they prefer more deterministic money to less. 

THE ONE PERIOD MODEL 
13 
' 8  
The formula above is therefore often referred to as a "preference free" 
valuation formula. 
We end by studying a concrete example. 
Example 2.12 We set s = 100, u = 1.2, d = 0.8, p, = 0.6, pd = 0.4 and, for 
computational simplicity, R = 0. By convention, the monetary unit is the US 
dollar. Thus we have the price dynamics 
so = 100, 
s1={ 
120, with probability 0.6. 
80, with probability 0.4. 
If we compute the discounted expected value (under the objective probability 
measure P) of tomorrow's price we get 
I
,
 1 
- E ~  [Sl] = 1 - [I20 -0.6 + 80 0.41 = 104. 
l + R  
This is higher than the value of today's stock price of 100, so the market is risk 
averse. Since condition (2.1) obviously is satisfied we know that the market is 
arbitrage free. We consider a European call with strike price K = 110, so the 
claim X is given by 
x = {  
10, if s1 = 120, 
0, if S = 80. 
Using the method of computing the price as the discounted expected values 
under the objective probabilities, i.e. "Answer 1" in Section 1.1, this would give 
II(0; X) = - 
[lo. 0.6 + 0 )0.4] = 6. 
1 + 0  
Using the theory above it is easily seen that the martingale probabilities are 
given by q, = qd = 0.5, thus giving us the theoretical price 
1 
II(0; X) = - 
[lo - 0.5 + 0 0.51 = 5. 
1+0 
We thus see that the theoretical price differs from the naive approach above. 
If our theory is correct we should also be able to replicate the option, and from 
the proposition above the replicating portfolio is given by 
1.2 - 0  - 0.8 10 
2 = 
= -20, 
1.2 - 0.8 
1 
10- 0 
1 
y=-. 
= - 
100 1.2 - 0.8 
4' 

THE BINOMIAL MODEL 
In everyday terms this means that the replicating portfolio is formed by 
I 
borrowing $20 from the bank, and investing this money in a quarter of a share 
in the stock. Thus the net value of the portfolio at t = 0 is five dollars, and at 
I 
I 
t = 1 the value is given by 
so we see that we have indeed replicated the option. We also see that if anyone 
is foolish enough to buy the option from us for the price $6, then we can make 
a riskless profit. We sell the option, thereby obtaining six dollars. Out of these 
six we invest five in the replicating portfolio and invest the remaining one in the 
bank. At time t = 1 the claims of the buyer of the option are completely balanced 
by the value of the replicating portfolio, and we still have one dollar invested in 
the bank. We have thus made an arbitrage profit. If someone is willing to sell 
the option to us at a price lower than five dollars, we can also make an arbitrage 
profit by selling the portfolio short. 
We end this section by making some remarks. 
First of all we have seen that in a complete market, like the binomial model 
above, there is indeed a unique price for any contingent claim. The price is given 
by the value of the replicating portfolio, and a negative way of expressing this 
is as follows. There exists a theoretical price for the claim precisely because of 
the fact that, strictly speaking, the claim is superfluous-it can equally well be 
replaced by its hedging portfolio. 
Second, we see that the structural reason for the completeness of the bino- 
mial model is the fact that we have two financial instruments at our disposal 
(the bond and the stock) in order to solve two equations (one for each possible 
outcome in the sample space). This fact can be generalized. A model is com- 
plete (in the generic case) if the number of underlying assets (including the bank 
account) equals the number of outcomes in the sample space. 
If we would like to make a more realistic multiperiod model of the stock 
market, then the last remark above seems discouraging. If we make a (non- 
recombining) tree with 20 time steps this means that we have 220- lo6 
elementary outcomes, and this number exceeds by a large margin the number of 
assets on any existing stock market. It would therefore seem that it is impossible 
to construct an interesting complete model with a reasonably large number of 
time steps. Fortunately the situation is not at all as bad as that; in a multiperiod 
model we will also have the possibility of considering intermediary trading, 
i.e. we can allow for portfolios which are rebalanced over time. This will give 
us much more degrees of freedom, and in the next section we will in fact study 
a complete multiperiod model. 

I 
THE MULTIPERZOD MODEL 
2.2 The Multiperiod Model 
2.2.1 Portfolios and Arbitrage 
The multiperiod binomial model is a discrete time model with the time index t 
running from t = 0 to t = T, where the horizon T is fixed. As before we have two 
underlying assets, a bond with price process Bt and a stock with price process St. 
We assume a constant deterministic short rate of interest R, which is inter- 
preted as the simple period rate. This means that the bond price dynamics are 
given by 
The dynamics of the stock price are given by 
here Zo, . . . , 
are assumed to be i.i.d. (independent and identically distrib 
uted) stochastic variables, taking only the two values u and d with probabilities 
P(zn = u) = PU, 
P(Zn 
= d) = pd. 
I 
We can illustrate the stock dynamics by means of a tree, as in Fig. 2.3. 
Note that the tree is recombining in the sense that an "upn-move followed by a 
"down"-move gives the same result as a "down"-move followed by an "up
7'-move. 
We now go on to define the concept of a dynamic portfolio strategy. 
Definition 2.13 A portfolio strategy is a stochastic process 
{ht=(xt,yt); 
t = l , . . . , T )  
such that ht is a function of So, S1,. . . , St-1. For a given portfolio strategy h we 
set ho = hl by convention. The value process corresponding to the portfolio h 
is defined by 
&h = xt(1 +R) +ytSt. 
The interpretation of the formal definition is that xt is the amount of money 
which we invest in the bank at time t - 1 and keep until time t. We interpret 
yt as the number of shares that we buy at time t - 1 and keep until time t. 
We allow the portfolio strategy to be a contingent strategy, i.e. the portfolio we 
buy at t is allowed to depend on all information we have collected by observing 
the evolution of the stock price up to time t. We are, however, not allowed to 

THE BINOMIAL MODEL 
FIG. 2.3. Price dynamics 
look into the future. The entity Kh above is of course the market value of the 
portfolio (xt, yt) (which has been held since t - 1) at time t. 
The portfolios which primarily interest us are the self-financing portfolios, 
i.e. portfolios without any exogenous infusion or withdrawal of money. In prac- 
tical terms this means that in a self-financing portfolio strategy the accession 
of a new asset has to be financed through the sale of some other asset. The 
mathematical definition is as follows. 
Definition 2.14 A portfolio strategy h is said to be self-financing if the 
following condition holds for all t = 0,. . . ,T - 1 
The condition above is simply a budget equation. It says that, at each time t, 
the market value of the "old" portfolio (xt, yt) (which was created at t - 1) equals 
the purchase value of the new portfolio (xt+l, ~ t + ~ ) ,  
which is formed at t (and 
held until t + 1). 
We can now define the multiperiod version of an arbitrage possibility. 
Definition 2.15 An arbitrage possibility is a self-financing portfolio h with 
the properties 

THE MULTIPERIOD MODEL 
17 
We immediately have the following necessary condition for absence of 
arbitrage. 
Lemma 2.16 If the model is free of arbitrage then the following conditions 
necessarily must hold. 
! 
d < ( l + R ) < u .  
(2.8) 
The condition above is in fact also sufficient for absence of arbitrage, but this 
I 
fact is a little harder to show, and we will prove it later. In any case we assume 
6 
that the condition holds. 
Assumption 2.2.1 Henceforth we assume that d < u, and that the condition 
(2.8) holds. 
As in the one period model we will have use for "martingale probabilities" 
which are defined and computed exactly as before. 
I 
Definition 2.17 The martingale probabilities q, and qd are defined as the 
probabilities for which the relation 
holds. 
Proposition 2.18 The martingale probabilities are given 
2.2.2 Contingent Claims 
We now give the formal definition of a contingent claim in the model. 
Definition 2.19 A contingent claim is a stochastic variable X of the form 
& where the contract function @ is some given real valued function. 
The interpretation is that the holder of the contract receives the stochastic 
+ amount X at time t = T. Notice that we are only considering claims that are 
"simple", in the sense that the value of the claim only depends on the value ST 
of the stock price at the final time T. It is also possible to consider stochastic 
I 
payoffs which depend on the entire path of the price process during the interval 
[O,T], but then the theory becomes a little more complicated, and in particular 
/ 
the event tree will become nonrecombining. 

THE BINOMIAL MODEL 
Our main problem is that of finding a "reasonable" price process 
for a given claim X, and as in the one period case we attack this problem by 
means of replicating portfolios. 
Definition 2.20 A given contingent claim X is said to be reachable if there 
exists a self-financing portfolio h such that 
with probability 1. In that case we say that the portfolio h is a hedging portfolio 
or a replicating portfolio. If all claims can be replicated we say that the market 
is (dynamically) complete. 
Again we have a natural pricing principle for reachable claims. 
Pricing principle 2 If a claim X is reachable with replicating (seIf-financing) 
portfolio h, then the only reasonable price process for X is given by 
Let us go through the argument in some detail. Suppose that X is reachable 
using the self-financing portfolio h. Fix t and suppose that at time t we have 
access to the amount Fh. 
Then we can invest this money in the portfolio h, 
and since the portfolio is self-financing we can rebalance it over time without 
any extra cost so as to have the stochastic value V$ at time T. By definition 
V -  = X with probability 1, so regardless of the stochastic movements of the 
stock price process the value of our portfolio will, at time T, be equal to the 
value of the claim X. Thus, from a financial point of view, the portfolio h and 
the claim X are equivalent so they should fetch the same price. 
The "reasonableness" of the pricing formula above can be expressed more 
formally as follows. The proof is left to the reader. 
Proposition 2.21 Suppose that X is reachable using the portfolio h. Suppose 1 
furthermore that, at some time t, it is possible to buy X at a price cheaper than 
(or to sell it at a price higher than) yh. Then it is possible to make an arbitrage 1 
profit. 
We now turn to the completeness of the model. 
Proposition 2.22 The multiperiod binomial model is complete, i.e. every clairiz 
can be replicated by a self-financing portfolio. 
I 
It is possible, and not very hard, to give a formal proof of the proposition, 
using mathematical induction. The formal proof will, however, look rather messy 1 
with lots of indices, so instead we prove the proposition for a concrete example, 1 

THE MULTIPERIOD MODEL 
19 
using a binomial tree. This should (hopefully) convey the idea of the proof, and 
the mathematically inclined reader is then invited to formalize the argument. 
Example 2.23 We set T = 3, So = 80, u = 1.5, d = 0.5, p, = 0.6, pd = 0.4 
and, for computational simplicity, R = 0. 
The dynamics of the stock price can now be illustrated using the binomial 
tree in Fig. 2.4, where in each node we have written the value of the stock price. 
We now consider a particular contingent claim, namely a European call on 
the underlying stock. The date of expiration of the option is T = 3, and the 
strike price is chosen to be K = 80. Formally this claim can be described as 
X = max [ST - K, 01. 
We will now show that this particular claim can be replicated, and it will be 
obvious from the argument that the result can be generalized to any binomial 
model and any claim. 
The idea is to use induction on the time variable and to work backwards in 
the tree from the leaves at t = T to the root at t = 0. We start by computing the 
price of the option at the date of expiration. This is easily done since obviously 
(why?) we must have, for any claim X, the relation 
This result is illustrated in Fig. 2.5, where the boxed numbers indicate the price 
of the claim. Just to check, we see that if S3 = 90, then we exercise the option, 
i 
FIG. 2.4. Price dynamics 

THE BINOMIAL MODEL 
pay 80 to obtain the stock, and then immediately sell the stock at market price 
90, thus making a profit of 10. 
Our problem is thus that of replicating the boxed payoff structure at t = 3. 
Imagine for a moment that we are at some node at t = 2, e.g. at the node 
Sz = 180. What we then see in front of us, from this particular node, is a simple 
one period binomial model, given in Fig. 2.6, and it now follows directly from 
the one period theory that the payoff structure in Fig. 2.6 can indeed be replic- 
ated from the node S2 = 180. We can in fact compute the cost of this replicating 
portfolio by risk neutral valuation, and since the martingale probabilities for this 
example are given by q, = qd = 0.5 the cost of the replicating portfolio is 
In the same way we can consider all the other nodes at t = 2, and compute the 
cost of the corresponding replicating portfolios. The result is the set of boxed 
numbers at t = 2 in Fig. 2.7. 

THE MULTIPERIOD MODEL 
21 
FIG. 2.7. 
<I 
FIG. 2.8. 
What we have done by this procedure is to show that if we can find a self- 
financing portfolio which replicates the boxed payoff structure at t = 2, then it is 
in fact possible to replicate the original claim at t = 3. We have thus reduced the 
problem in the time variable, and from now on we simply reproduce the construc- 
tion above, but this time at t = 1. Take, for example, the node S1 = 40. From 
the point of view of this node we have a one period model given by Fig. 2.8, and 
by risk neutral valuation we can replicate the payoff structure using a portfolio, 
which at the node & = 40 will cost 
1 
1 + 0  
- 
[5 -0.5 + 0 e0.51 = 2.5. 
In this manner we fill the nodes at t = 1 with boxed portfolio costs, and then 
we carry out the same construction again at t = 0. The result is given in Fig. 2.9. 
I 
We have thus proved that it is in fact possible to replicate the European call 
option at an initial cost of 27.5. To check this let us now follow a possible price 
path forward through the tree. 

THE BINOMIAL MODEL 
We start at t = 0, and since we want to reproduce the boxed claim (52.5, 2.5) 
at t = 1, we can use Proposition 2.4 to compute the hedging portfolio as 
X I  = - 22.5, yl = 518. The reader should check that the cost of this portfolio 
is exactly 27.5. 
Suppose that the price now moves to S1 = 120. Then our portfolio is worth 
Since we now are facing the claim (100, 5) at t = 2 we can again use Proposi- 
tion 2.4 to calculate the hedging portfolio as 2 2  = -42.5, y2 = 951120, and the 
reader should again check that the cost of this portfolio equals the value of our 
old portfolio, i.e. 52.5. Thus it is really possible to rebalance the portfolio in 
a self-financing manner. 
We now assume that the price falls to S 2  = 60. Then our portfolio is worth 
Facing the claim (10, 0) at t = 3 we use Proposition 2.4 to calculate the hedging 
portfolio as 2 3  = -5, y3 = 116, and again the cost of this portfolio equals the 
value of our old portfolio. 
Now the price rises to S3 = 90, and we see that the value of our portfolio is 
given by 
-5 (1 + 0) + .90 = 10, 
which is exactly equal to the value of the option at that node in the tree. In 
Fig. 2.10 we have computed the hedging portfolio at each node. 
If we think a bit about the computational effort we see that all the value 
computations, i.e. all the boxed values, have to be calculated off-line. Having 

THE MULTIPERIOD MODEL 
done this we have of course not only computed the arbitrage free price at t = 0 for 
the claim, but also computed the arbitrage free price, at every node in the tree. 
The dynamic replicating portfolio does not have to be computed off-line. As 
in the example above, it can be computed on-line as the price process evolves 
over time. In this way we only have to compute the portfolio for those nodes 
that we actually visit. 
We now go on to give the general binomial algorithm. In order to do this we 
need to introduce some more notation to help us keep track of the price evolu- 
tion. It is clear from the construction that the value of the price process at time 
t can be written as 
St = ~
u
~
d
~
-
~
 
, k=O ,..., t, 
where lc denotes the number of upmoves that have occurred. Thus each node in 
the binomial tree can be represented by a pair (t, k) with k = 0,. . . , t. 
Proposition 2.24 (Binomial algorithm) Consider a T-claim X = @(ST). 
Then this claim can be replicated using a self-financing portfolio. If &(k) denotes 
Me value of the portfolio at the node (t, k) then &(k) can be computed recursively 
by the scheme 

whem z%e martingale pmbabilitzes q, and qd am given by 
I 
With the notation as above, the hedging portfolio is given by 
Il 
In particular, the arbitrage free price of the claim at t = 0 is given by Vo(0). 
I 
From the algorithm above it is also clear that we can obtain a risk neutral 
valuation formula. 
Proposition 2.25 The arbitrage free price at t = 0 of a T-claim X is given by 
where Q denotes the martingale measure, or more explicitly 
Proof The first formula follows directly from the algorithm above. If we let Y 
denote the number of upmoves in the tree we can write 
and now the second formula follows from the fact that Y has a binomial 
distribution. 
We end this section by proving absence of arbitrage. 
Proposition 2.26 The condition 
is a necessary and suficient condition for absence of arbitrage. 
Proof The necessity follows from the corresponding one period result. Assume 
that the condition is satisfied. We want to prove absence of arbitrage, so let 

NOTES 
25 
us assume that h (a potential arbitrage portfolio) is a self-financing portfolio 
satisfying the conditions 
P(V$ 2 0) = 1, 
P(V$ > 0) > 0. 
&om these conditions, and from the risk neutral valuation formula, it follows 
1 
V ~ h  
= (1 + R)T . E~ [v-] 
> 0, 
which shows that h is not an arbitrage portfolio. 
0 
2.3 Exercises 
Exercise 2.1 
(a) Prove Proposition 2.6. 
m' 
(b) Show, in the one period binomial model, that if lI(1;X) # X with 
probability 1, then you can make a riskless profit. 
Exercise 2.2 Prove Proposition 2.21. 
Exercise 2.3 Consider the multiperiod example in the text. Suppose that at 
time t = 1 the stock price has gone up to 120, and that the market price of the 
option turns out to be 50.0. Show explictly how you can make an arbitrage profit. 
Exercise 2.4 Prove Proposition 2.24, by using induction on the time horizon T. 
For the origins of the binomial model, see Cox, Ross and Rubinstein (1979), and 
Rendleman and Bartter (1979). The book by Cox and Rubinstein (1985) has 
become a standard reference. 

I 
3 
A MORE GENERAL ONE PERIOD MODEL 
In this chapter, we will investigate absence of arbitrage and compf&eness in 
slightly more general terms than in the binomial model. To keep things simple we 
will be content with a one period model, but the financial market and the under- 
lying sample space will be more general than for the binomial model. The,point 
of this investigation of a simple case is that it highlights some very basic and 
important ideas, and our main results will in fact be valid for much more general 
models. 
3.1 The Model 
We consider a financial market with N different financial assets. These assets 
could in principle be almost anything, like bonds, stocks, options or whatever 
financial instrument that is traded on a liquid market. The market only exists 
at the two points in time t = 0 and t = 1, and the price per unit of asset No. i 
at time t will be denoted by St. We thus have a price vector process St, t = 0,l 
and we will view the price vector as a column vector, i.e. 
st = [ " 
] 
SF 
The randomness in the system is modeled by assuming that we hpve 
sample space R = {wl, . . . , W M )  and that the probabilities P(w4, *= 
1 
are all strictly positive. The price vector So is assumed to be deterministic and 
known to us, but the price vector at time t = 1 depends upon the outcome 
w E R, and S:(wj) denotes the price per unit of asset No. i at time t = 1 if wj 
has occurred. 
We may therefore define the matrix D by 
I 
S? ( ~ 1 )  s? ( ~ 2 )  ' ' s: ( W M )  
s?(wl) sf(-) ' ' ' 
S?(WM) 
D =  

ABSENCE OF ARBITRAGE 
27 
We can also write D as 
where dl,. . . , dM are the columns of D. 
3.2 Absence of Arbitrage 
We now define a portfolio as an N-dimensional row vector h = [hl,. . . , hN] 
with the interpretation that hi is the number of units of asset No. i that we buy 
at time t = 0 and keep until time t = 1. 
Since we are buying the assets with deterministic prices at time t = 0 and 
selling them at time t = 1 at stochastic prices, the value process of our portfolio 
will be a stochastic process v , ~  
defined by 
. , There are various (more or less equivalent) variations of the concept of an 
arbitrage portfolio, and in the present setting the following will do nicely. 
Definition 3.1 The portfolio h is an arbitrage portfolio if it satisfies the 
conditions 
v: 
< 0, 
V: 2 0, 
with probability 1. 
With obvious notation we can write this as 
We now go on to investigate when the market model above is free of arbitr- 
! age possibilities, and the main technical tool for this investigation is the 
I Farkas Lemma. 
i ' 
Lemma 3.2 (Farkas' Lemma) Suppose that do, dl,. . . , dM are column vec- 
: 
tors in RN. Then exactly one of the two following problems possesses a solution: 
Problem 1: Find nonnegative numbers zl, . . . , ZM such that 

28 
A MORE GENERA'L ONE PERIOD' MODEL 
1 
Problem 2: Find a row vector h E R~ such that 
hdo < 05 
hdj20, j=l, ..., M. 
. z h , L  
b' 
8 
A 
I 
Proof Let K be the set of all nonnegative linear combinations of dl,. . . , d
~
.
It is easy to see that K is a convex cone containing the origin. Exactlfr*'one of 
I 
i 
the following cases can hold: 
The vector 4 belongs to K. This means that Problem 1 above has 
a solution. 
The vector 4 does not belong to K. Then, by the separation theorem for 
contex sets, there exists a hyperplahe H such that do is strictly on one 
side of H whereas K is on the other side. Letting h be defined as a normal 
vector to H pointing in the direction where K lies, this means that Problem 
2 has a solution. 
-
.
 
We can now formulate our first result. 
Proposition 3.3 The market is arbitrage free if and only if there &t 
non- 
negative numbers 21,. . . , ZM such that the folloun'ng vector equality holds: 
M 
& = Czjfi(wj). 
j=1 
On component form this wads as 
A .  
N 
S, = X ~ S ~ ( W , ) : .  
i* 1, ..., N. 
Proof From the definition it follows that the market is arbitrage free if and 
only if the following system of ineq~ 
oes not possess a solution h E R ~ .  
where dl, . . . , dM are the columns of the a r k  
d &b~ve.~fio'm 
the Farkas Lemma 
(with 4 = So) we thus infer the e 
of nonnegative numbers zl , . . . , z~ 
such that 
l
s
,
 , 
M 

I 
ABSENCE OF ARBITRAGE 
We can now give an economic interpretation of this result by defining the 
real nonnegative numbers ql, . . . , q~ by 
/r 
In this way we may interpret 91,. . . , q~ as a probability distribution on S1 
by setting Q(w,) = qi, and we can reformulate our previous result. 
Proposition 3.4 The market is arbitrage free if and only if there exists a 
probability dzstribution Q on 0 and a real constant P such that 
Such a measure, or probability distribution Q is called a martingale measure, 
or a risk neutral distribution, or a risk adjusted distribution. 
' A natural question is now whether there exists a natural economic inteiprkt- 
ation of the factor p above. In order to obtain such an interpretation, we now 
make the additional assumption that there exists a risk free investment altern- 
ative among the basic assets S1,. . . , SN, and we assume that this is in fact asset 
1 No. 1. By a risk free investment we simply mean that the price at time t = 1 is 
deterministic, and by scaling we may thus assume that S: (wj) = 1, j = 1,. . . , M. 
In other words, S1 is a zero coupon bond with principal equal to one. 
The first component of the equality (3.3) then becomes 
s,'=p-1, 
i 
and we may thus write 
1 
p-'- 1 + R' 
I 
' 
1 F where r is the risk free interest rate. Plugging this into the general formula 
i 
! (3.3) we have the following result, which in its far reaching generalizations is 
I 
F 
known as "the first fundamental theorem of mathematical finance". 
Proposition 3.5 (First Fundamental Theorem) Assume that there exists a 
risk free asset, and denote the corresponding risk free interest rate bg R. Then 
1 the market is arbitrage free i f  and only if there exists a measure Q such that 
1 
So = i = - q j , ~ ~ [ s ~ ] .  
(3.4) 
The economic interpretation is thus that today's asset prices are obtained 
as the expected value (under Q) of tomorrow's asset prices, discounted with 

30 
A MORE GENERAL ONE PERIOD MODEL 
the risk free rateit The formula is also referred to as a 'lisk-neutral" pricing 
formula. The terminology "martingale measure" stems from the fact that, for 
every i = 1,. . . , N the process 
and 
Thus, in particular, Q is a martingale measure for the sunderlying assets. At 
time tb = 1 the value of the claim X is known, so in order to avoid arbitrage 
is a sc~called martingale under the measure Q. We will come back later to 
martingales in much more detail, but in the present setting it just means that 
3.3 Martingale Pricing 
In this section, we will study how to price financial derivatives or, in tech- 
nical terms contingent claims. We take the previously studied market model 
as given and we assume for simplicity that there exists a risk free asset. In 
order to highlight the, role of the risk free asset, we denote its price process 
by Bt and we may thus regard Bt as a bank account,$ where our money (or 
our debts) grow at the risk free rate. (In the previous section we thus had 
B = S1.) 
I 
Definition 3.6 A contingent claim is any random variable X ,  defined on 0. 
The interpretation is that a contingent claim X represents2 a stochastic 
amount of money which we will obtain at time t = 1. Our main problem is 
now to determine a "reasonable" price TI(@ X), at time t = 0 for a given claim 
X, and in order to do this we must give a more precise meaning to the word 
"reasonable" above. 
More precisely we would like to price the claim X consistently with the 
underlying a priori given assets S1,. . . , SN, or put in other words, we would like 
to price the claim X in such a way that there are no arbitrage opportunities 
on the extended market consisting of TI, S1,. . . , SN. This problem is, however, 
easily solved. The extended market is arbitrage free if and only if there exists 
some martingale measure Q such that 
1 
n(o; x) = -EQ 
[n(i; x)] 
, 
l + R  

