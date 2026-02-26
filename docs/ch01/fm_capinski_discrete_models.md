# Discrete Market Models & Binomial Pricing

!!! info "Source"
    **Mathematics for Finance: An Introduction to Financial Engineering** by Marek Capinski and Tomasz Zastawniak, Springer, 2003.
    These notes are used for educational purposes.

## Simple Market Model

2
Mathematics for Finance
current bond price A(0) is known to all investors, just like the current stock
price. However, in contrast to stock, the price A(1) the bond will fetch at time 1
is also known with certainty. For example, A(1) may be a payment guaranteed
by the institution issuing bonds, in which case the bond is said to mature at
time 1 with face value A(1). The return on bonds is defined in a similar way
as that on stock,
KA = A(1) −A(0)
A(0)
.
Chapters 2, 10 and 11 give a detailed exposition of risk-free assets.
Our task is to build a mathematical model of a market of financial securi-
ties. A crucial first stage is concerned with the properties of the mathematical
objects involved. This is done below by specifying a number of assumptions,
the purpose of which is to find a compromise between the complexity of the
real world and the limitations and simplifications of a mathematical model,
imposed in order to make it tractable. The assumptions reflect our current
position on this compromise and will be modified in the future.
Assumption 1.1 (Randomness)
The future stock price S(1) is a random variable with at least two different
values. The future price A(1) of the risk-free security is a known number.
Assumption 1.2 (Positivity of Prices)
All stock and bond prices are strictly positive,
A(t) > 0
and
S(t) > 0
for t = 0, 1.
The total wealth of an investor holding x stock shares and y bonds at a
time instant t = 0, 1 is
V (t) = xS(t) + yA(t).
The pair (x, y) is called a portfolio, V (t) being the value of this portfolio or, in
other words, the wealth of the investor at time t.
The jumps of asset prices between times 0 and 1 give rise to a change of
the portfolio value:
V (1) −V (0) = x(S(1) −S(0)) + y(A(1) −A(0)).
This difference (which may be positive, zero, or negative) as a fraction of the
initial value represents the return on the portfolio,
KV = V (1) −V (0)
V (0)
.

1. Introduction: A Simple Market Model
3
The returns on bonds or stock are particular cases of the return on a portfolio
(with x = 0 or y = 0, respectively). Note that because S(1) is a random
variable, so is V (1) as well as the corresponding returns KS and KV . The
return KA on a risk-free investment is deterministic.
Example 1.1
Let A(0) = 100 and A(1) = 110 dollars. Then the return on an investment in
bonds will be
KA = 0.10,
that is, 10%. Also, let S(0) = 50 dollars and suppose that the random variable
S(1) can take two values,
S(1) =
 52
with probability p,
48
with probability 1 −p,
for a certain 0 < p < 1. The return on stock will then be
KS =

0.04
if stock goes up,
−0.04
if stock goes down,
that is, 4% or −4%.
Example 1.2
Given the bond and stock prices in Example 1.1, the value at time 0 of a
portfolio with x = 20 stock shares and y = 10 bonds is
V (0) = 2, 000
dollars. The time 1 value of this portfolio will be
V (1) =
 2, 140
if stock goes up,
2, 060
if stock goes down,
so the return on the portfolio will be
KV =
 0.07
if stock goes up,
0.03
if stock goes down,
that is, 7% or 3%.

4
Mathematics for Finance
Exercise 1.1
Let A(0) = 90, A(1) = 100, S(0) = 25 dollars and let
S(1) =
 30
with probability p,
20
with probability 1 −p,
where 0 < p < 1. For a portfolio with x = 10 shares and y = 15 bonds
calculate V (0), V (1) and KV .
Exercise 1.2
Given the same bond and stock prices as in Exercise 1.1, find a portfolio
whose value at time 1 is
V (1) =
 1, 160
if stock goes up,
1, 040
if stock goes down.
What is the value of this portfolio at time 0?
It is mathematically convenient and not too far from reality to allow arbi-
trary real numbers, including negative ones and fractions, to represent the risky
and risk-free positions x and y in a portfolio. This is reflected in the following
assumption, which imposes no restrictions as far as the trading positions are
concerned.
Assumption 1.3 (Divisibility, Liquidity and Short Selling)
An investor may hold any number x and y of stock shares and bonds, whether
integer or fractional, negative, positive or zero. In general,
x, y ∈R.
The fact that one can hold a fraction of a share or bond is referred to
as divisibility. Almost perfect divisibility is achieved in real world dealings
whenever the volume of transactions is large as compared to the unit prices.
The fact that no bounds are imposed on x or y is related to another market
attribute known as liquidity. It means that any asset can be bought or sold on
demand at the market price in arbitrary quantities. This is clearly a mathe-
matical idealisation because in practice there exist restrictions on the volume
of trading.
If the number of securities of a particular kind held in a portfolio is pos-
itive, we say that the investor has a long position. Otherwise, we say that a
short position is taken or that the asset is shorted. A short position in risk-free

1. Introduction: A Simple Market Model
5
securities may involve issuing and selling bonds, but in practice the same fi-
nancial effect is more easily achieved by borrowing cash, the interest rate being
determined by the bond prices. Repaying the loan with interest is referred to
as closing the short position. A short position in stock can be realised by short
selling. This means that the investor borrows the stock, sells it, and uses the
proceeds to make some other investment. The owner of the stock keeps all the
rights to it. In particular, she is entitled to receive any dividends due and may
wish to sell the stock at any time. Because of this, the investor must always
have sufficient resources to fulfil the resulting obligations and, in particular, to
close the short position in risky assets, that is, to repurchase the stock and
return it to the owner. Similarly, the investor must always be able to close a
short position in risk-free securities, by repaying the cash loan with interest. In
view of this, we impose the following restriction.
Assumption 1.4 (Solvency)
The wealth of an investor must be non-negative at all times,
V (t) ≥0
for t = 0, 1.
A portfolio satisfying this condition is called admissible.
In the real world the number of possible different prices is finite because
they are quoted to within a specified number of decimal places and because
there is only a certain final amount of money in the whole world, supplying an
upper bound for all prices.
Assumption 1.5 (Discrete Unit Prices)
The future price S(1) of a share of stock is a random variable taking only
finitely many values.
1.2 No-Arbitrage Principle
In this section we are going to state the most fundamental assumption about
the market. In brief, we shall assume that the market does not allow for risk-free
profits with no initial investment.
For example, a possibility of risk-free profits with no initial investment can
emerge when market participants make a mistake. Suppose that dealer A in
New York offers to buy British pounds at a rate dA = 1.62 dollars to a pound,

6
Mathematics for Finance
while dealer B in London sells them at a rate dB = 1.60 dollars to a pound.
If this were the case, the dealers would, in effect, be handing out free money.
An investor with no initial capital could realise a profit of dA −dB = 0.02
dollars per each pound traded by taking simultaneously a short position with
dealer B and a long position with dealer A. The demand for their generous
services would quickly compel the dealers to adjust the exchange rates so that
this profitable opportunity would disappear.
Exercise 1.3
On 19 July 2002 dealer A in New York and dealer B in London used the
following rates to change currency, namely euros (EUR), British pounds
(GBP) and US dollars (USD):
dealer A
buy
sell
1.0000 EUR
1.0202 USD
1.0284 USD
1.0000 GBP
1.5718 USD
1.5844 USD
dealer B
buy
sell
1.0000 EUR
0.6324 GBP
0.6401 GBP
1.0000 USD
0.6299 GBP
0.6375 GBP
Spot a chance of a risk-free profit without initial investment.
The next example illustrates a situation when a risk-free profit could be
realised without initial investment in our simplified framework of a single time
step.
Example 1.3
Suppose that dealer A in New York offers to buy British pounds a year from
now at a rate dA = 1.58 dollars to a pound, while dealer B in London would sell
British pounds immediately at a rate dB = 1.60 dollars to a pound. Suppose
further that dollars can be borrowed at an annual rate of 4%, and British
pounds can be invested in a bank account at 6%. This would also create an
opportunity for a risk-free profit without initial investment, though perhaps
not as obvious as before.
For instance, an investor could borrow 10, 000 dollars and convert them into
6, 250 pounds, which could then be deposited in a bank account. After one year
interest of 375 pounds would be added to the deposit, and the whole amount
could be converted back into 10, 467.50 dollars. (A suitable agreement would
have to be signed with dealer A at the beginning of the year.) After paying

1. Introduction: A Simple Market Model
7
back the dollar loan with interest of 400 dollars, the investor would be left with
a profit of 67.50 dollars.
Apparently, one or both dealers have made a mistake in quoting their ex-
change rates, which can be exploited by investors. Once again, increased de-
mand for their services will prompt the dealers to adjust the rates, reducing dA
and/or increasing dB to a point when the profit opportunity disappears.
We shall make an assumption forbidding situations similar to the above
example.
Assumption 1.6 (No-Arbitrage Principle)
There is no admissible portfolio with initial value V (0) = 0 such that V (1) > 0
with non-zero probability.
In other words, if the initial value of an admissible portfolio is zero, V (0) =
0, then V (1) = 0 with probability 1. This means that no investor can lock in a
profit without risk and with no initial endowment. If a portfolio violating this
principle did exist, we would say that an arbitrage opportunity was available.
Arbitrage opportunities rarely exist in practice. If and when they do, the
gains are typically extremely small as compared to the volume of transactions,
making them beyond the reach of small investors. In addition, they can be more
subtle than the examples above. Situations when the No-Arbitrage Principle is
violated are typically short-lived and difficult to spot. The activities of investors
(called arbitrageurs) pursuing arbitrage profits effectively make the market free
of arbitrage opportunities.
The exclusion of arbitrage in the mathematical model is close enough to
reality and turns out to be the most important and fruitful assumption. Ar-
guments based on the No-arbitrage Principle are the main tools of financial
mathematics.
1.3 One-Step Binomial Model
In this section we restrict ourselves to a very simple example, in which the
stock price S(1) takes only two values. Despite its simplicity, this situation is
sufficiently interesting to convey the flavour of the theory to be developed later
on.

8
Mathematics for Finance
Example 1.4
Suppose that S(0) = 100 dollars and S(1) can take two values,
S(1) =
 125
with probability p,
105
with probability 1 −p,
where 0 < p < 1, while the bond prices are A(0) = 100 and A(1) = 110 dollars.
Thus, the return KS on stock will be 25% if stock goes up, or 5% if stock goes
down. (Observe that both stock prices at time 1 happen to be higher than that
at time 0; ‘going up’ or ‘down’ is relative to the other price at time 1.) The
Figure 1.1
One-step binomial tree of stock prices
risk-free return will be KA = 10%. The stock prices are represented as a tree
in Figure 1.1.
In general, the choice of stock and bond prices in a binomial model is con-
strained by the No-Arbitrage Principle. Suppose that the possible up and down
stock prices at time 1 are
S(1) =
 Su
with probability p,
Sd
with probability 1 −p,
where Sd < Su and 0 < p < 1.
Proposition 1.1
If S(0) = A(0), then
Sd < A(1) < Su,
or else an arbitrage opportunity would arise.
Proof
We shall assume for simplicity that S(0) = A(0) = 100 dollars. Suppose that
A(1) ≤Sd. In this case, at time 0:
• Borrow $100 risk-free.
• Buy one share of stock for $100.

1. Introduction: A Simple Market Model
9
This way, you will be holding a portfolio (x, y) with x = 1 shares of stock
and y = −1 bonds. The time 0 value of this portfolio is
V (0) = 0.
At time 1 the value will become
V (1) =
 Su −A(1)
if stock goes up,
Sd −A(1)
if stock goes down.
If A(1) ≤Sd, then the first of these two possible values is strictly positive,
while the other one is non-negative, that is, V (1) is a non-negative random
variable such that V (1) > 0 with probability p > 0. The portfolio provides an
arbitrage opportunity, violating the No-Arbitrage Principle.
Now suppose that A(1) ≥Su. If this is the case, then at time 0:
• Sell short one share for $100.
• Invest $100 risk-free.
As a result, you will be holding a portfolio (x, y) with x = −1 and y = 1, again
of zero initial value,
V (0) = 0.
The final value of this portfolio will be
V (1) =
 −Su + A(1)
if stock goes up,
−Sd + A(1)
if stock goes down,
which is non-negative, with the second value being strictly positive, since
A(1) ≥Su. Thus, V (1) is a non-negative random variable such that V (1) > 0
with probability 1−p > 0. Once again, this indicates an arbitrage opportunity,
violating the No-Arbitrage Principle.
The common sense reasoning behind the above argument is straightforward:
Buy cheap assets and sell (or sell short) expensive ones, pocketing the difference.
1.4 Risk and Return
Let A(0) = 100 and A(1) = 110 dollars, as before, but S(0) = 80 dollars and
S(1) =
 100
with probability 0.8,
60
with probability 0.2.

10
Mathematics for Finance
Suppose that you have $10, 000 to invest in a portfolio. You decide to buy
x = 50 shares, which fixes the risk-free investment at y = 60. Then
V (1) =
 11, 600
if stock goes up,
9, 600
if stock goes down,
KV =

0.16
if stock goes up,
−0.04
if stock goes down.
The expected return, that is, the mathematical expectation of the return on the
portfolio is
E(KV ) = 0.16 × 0.8 −0.04 × 0.2 = 0.12,
that is, 12%. The risk of this investment is defined to be the standard deviation
of the random variable KV :
σV =

(0.16 −0.12)2 × 0.8 + (−0.04 −0.12)2 × 0.2 = 0.08,
that is 8%. Let us compare this with investments in just one type of security.
If x = 0, then y = 100, that is, the whole amount is invested risk-free. In
this case the return is known with certainty to be KA = 0.1, that is, 10% and
the risk as measured by the standard deviation is zero, σA = 0.
On the other hand, if x = 125 and y = 0, the entire amount being invested
in stock, then
V (1) =
 12, 500
if stock goes up,
7, 500
if stock goes down,
and E(KS) = 0.15 with σS = 0.20, that is, 15% and 20%, respectively.
Given the choice between two portfolios with the same expected return, any
investor would obviously prefer that involving lower risk. Similarly, if the risk
levels were the same, any investor would opt for higher return. However, in the
case in hand higher return is associated with higher risk. In such circumstances
the choice depends on individual preferences. These issues will be discussed in
Chapter 5, where we shall also consider portfolios consisting of several risky
securities. The emerging picture will show the power of portfolio selection and
portfolio diversification as tools for reducing risk while maintaining the ex-
pected return.
Exercise 1.4
For the above stock and bond prices, design a portfolio with initial wealth
of $10, 000 split fifty-fifty between stock and bonds. Compute the ex-
pected return and risk as measured by standard deviation.

1. Introduction: A Simple Market Model
11
1.5 Forward Contracts
A forward contract is an agreement to buy or sell a risky asset at a specified
future time, known as the delivery date, for a price F fixed at the present
moment, called the forward price. An investor who agrees to buy the asset is
said to enter into a long forward contract or to take a long forward position. If
an investor agrees to sell the asset, we speak of a short forward contract or a
short forward position. No money is paid at the time when a forward contract
is exchanged.
Example 1.5
Suppose that the forward price is $80. If the market price of the asset turns out
to be $84 on the delivery date, then the holder of a long forward contract will
buy the asset for $80 and can sell it immediately for $84, cashing the difference
of $4. On the other hand, the party holding a short forward position will have
to sell the asset for $80, suffering a loss of $4. However, if the market price of
the asset turns out to be $75 on the delivery date, then the party holding a
long forward position will have to buy the asset for $80, suffering a loss of $5.
Meanwhile, the party holding a short position will gain $5 by selling the asset
above its market price. In either case the loss of one party is the gain of the
other.
In general, the party holding a long forward contract with delivery date 1
will benefit if the future asset price S(1) rises above the forward price F. If
the asset price S(1) falls below the forward price F, then the holder of a long
forward contract will suffer a loss. In general, the payofffor a long forward
position is S(1) −F (which can be positive, negative or zero). For a short
forward position the payoffis F −S(1).
Apart from stock and bonds, a portfolio held by an investor may contain
forward contracts, in which case it will be described by a triple (x, y, z). Here
x and y are the numbers of stock shares and bonds, as before, and z is the
number of forward contracts (positive for a long forward position and negative
for a short position). Because no payment is due when a forward contract is
exchanged, the initial value of such a portfolio is simply
V (0) = xS(0) + yA(0).
At the delivery date the value of the portfolio will become
V (1) = xS(1) + yA(1) + z(S(1) −F).

12
Mathematics for Finance
Assumptions 1.1 to 1.5 as well as the No-Arbitrage Principle extend readily to
this case.
The forward price F is determined by the No-Arbitrage Principle. In par-
ticular, it can easily be found for an asset with no carrying costs. A typical
example of such an asset is a stock paying no dividend. (By contrast, a com-
modity will usually involve storage costs, while a foreign currency will earn
interest, which can be regarded as a negative carrying cost.)
A forward position guarantees that the asset will be bought for the forward
price F at delivery. Alternatively, the asset can be bought now and held until
delivery. However, if the initial cash outlay is to be zero, the purchase must be
financed by a loan. The loan with interest, which will need to be repaid at the
delivery date, is a candidate for the forward price. The following proposition
shows that this is indeed the case.
Proposition 1.2
Suppose that A(0) = 100, A(1) = 110, and S(0) = 50 dollars, where the risky
security involves no carrying costs. Then the forward price must be F = 55
dollars, or an arbitrage opportunity would exist otherwise.
Proof
Suppose that F > 55. Then, at time 0:
• Borrow $50.
• Buy the asset for S(0) = 50 dollars.
• Enter into a short forward contract with forward price F dollars and delivery
date 1.
The resulting portfolio (1, −1
2, −1) consisting of stock, a risk-free position, and
a short forward contract has initial value V (0) = 0. Then, at time 1:
• Close the short forward position by selling the asset for F dollars.
• Close the risk-free position by paying 1
2 × 110 = 55 dollars.
The final value of the portfolio, V (1) = F −55 > 0, will be your arbitrage
profit, violating the No-Arbitrage Principle.
On the other hand, if F < 55, then at time 0:
• Sell short the asset for $50.
• Invest this amount risk-free.
• Take a long forward position in stock with forward price F dollars and
delivery date 1.
The initial value of this portfolio (−1, 1
2, 1) is also V (0) = 0. Subsequently, at
time 1:

1. Introduction: A Simple Market Model
13
• Cash $55 from the risk-free investment.
• Buy the asset for F dollars, closing the long forward position, and return
the asset to the owner.
Your arbitrage profit will be V (1) = 55 −F > 0, which once again violates
the No-Arbitrage Principle. It follows that the forward price must be F = 55
dollars.
Exercise 1.5
Let A(0) = 100, A(1) = 112 and S(0) = 34 dollars. Is it possible to
find an arbitrage opportunity if the forward price of stock is F = 38.60
dollars with delivery date 1?
Exercise 1.6
Suppose that A(0) = 100 and A(1) = 105 dollars, the present price of
pound sterling is S(0) = 1.6 dollars, and the forward price is F = 1.50
dollars to a pound with delivery date 1. How much should a sterling
bond cost today if it promises to pay £100 at time 1? Hint: The for-
ward contract is based on an asset involving negative carrying costs (the
interest earned by investing in sterling bonds).
1.6 Call and Put Options
Let A(0) = 100, A(1) = 110, S(0) = 100 dollars and
S(1) =
 120
with probability p,
80
with probability 1 −p,
where 0 < p < 1.
A call option with strike price or exercise price $100 and exercise time 1 is
a contract giving the holder the right (but no obligation) to purchase a share
of stock for $100 at time 1.
If the stock price falls below the strike price, the option will be worthless.
There would be little point in buying a share for $100 if its market price is
$80, and no-one would want to exercise the right. Otherwise, if the share price
rises to $120, which is above the strike price, the option will bring a profit of
$20 to the holder, who is entitled to buy a share for $100 at time 1 and may
sell it immediately at the market price of $120. This is known as exercising
the option. The option may just as well be exercised simply by collecting the

14
Mathematics for Finance
difference of $20 between the market price of stock and the strike price. In
practice, the latter is often the preferred method because no stock needs to
change hands.
As a result, the payoffof the call option, that is, its value at time 1 is a
random variable
C(1) =
 20
if stock goes up,
0
if stock goes down.
Meanwhile, C(0) will denote the value of the option at time 0, that is, the price
for which the option can be bought or sold today.
Remark 1.1
At first sight a call option may resemble a long forward position. Both involve
buying an asset at a future date for a price fixed in advance. An essential
difference is that the holder of a long forward contract is committed to buying
the asset for the fixed price, whereas the owner of a call option has the right
but no obligation to do so. Another difference is that an investor will need to
pay to purchase a call option, whereas no payment is due when exchanging a
forward contract.
In a market in which options are available, it is possible to invest in a
portfolio (x, y, z) consisting of x shares of stock, y bonds and z options. The
time 0 value of such a portfolio is
V (0) = xS(0) + yA(0) + zC(0).
At time 1 it will be worth
V (1) = xS(1) + yA(1) + zC(1).
Just like in the case of portfolios containing forward contracts, Assumptions 1.1
to 1.5 and the No-Arbitrage Principle can be extended to portfolios consisting
of stock, bonds and options.
Our task will be to find the time 0 price C(0) of the call option consistent
with the assumptions about the market and, in particular, with the absence of
arbitrage opportunities. Because the holder of a call option has a certain right,
but never an obligation, it is reasonable to expect that C(0) will be positive:
one needs to pay a premium to acquire this right. We shall see that the option
price C(0) can be found in two steps:
Step 1
Construct an investment in x stocks and y bonds such that the value of the
investment at time 1 is the same as that of the option,
xS(1) + yA(1) = C(1),

1. Introduction: A Simple Market Model
15
no matter whether the stock price S(1) goes up to $120 or down to $80. This
is known as replicating the option.
Step 2
Compute the time 0 value of the investment in stock and bonds. It will be
shown that it must be equal to the option price,
xS(0) + yA(0) = C(0),
because an arbitrage opportunity would exist otherwise. This step will be re-
ferred to as pricing or valuing the option.
Step 1 (Replicating the Option)
The time 1 value of the investment in stock and bonds will be
xS(1) + yA(1) =
 x120 + y110
if stock goes up,
x80 + y110
if stock goes down.
Thus, the equality xS(1) + yA(1) = C(1) between two random variables can
be written as
 x120 + y110 = 20,
x80 + y110 = 0.
The first of these equations covers the case when the stock price goes up to
$120, whereas the second equation corresponds to the case when it drops to $80.
Because we want the value of the investment in stock and bonds at time 1 to
match exactly that of the option no matter whether the stock price goes up
or down, these two equations are to be satisfied simultaneously. Solving for x
and y, we find that
x = 1
2,
y = −4
11.
To replicate the option we need to buy 1
2 a share of stock and take a short
position of −4
11 in bonds (or borrow
4
11 × 100 = 400
11 dollars in cash).
Step 2 (Pricing the Option)
We can compute the value of the investment in stock and bonds at time 0:
xS(0) + yA(0) = 1
2 × 100 −4
11 × 100 ∼= 13.6364
dollars. The following proposition shows that this must be equal to the price
of the option.
Proposition 1.3
If the option can be replicated by investing in the above portfolio of stock and
bonds, then C(0) = 1
2S(0) −
4
11A(0), or else an arbitrage opportunity would
exist.

16
Mathematics for Finance
Proof
Suppose that C(0) + 4
11A(0) > 1
2S(0). If this is the case, then at time 0:
• Issue and sell 1 option for C(0) dollars.
• Borrow
4
11 × 100 = 400
11 dollars in cash (or take a short position y = −4
11 in
bonds by selling them).
• Purchase x = 1
2 shares of stock for xS(0) = 1
2 × 100 = 50 dollars.
The cash balance of these transactions is positive, C(0) + 4
11A(0) −1
2S(0) > 0.
Invest this amount risk-free. The resulting portfolio consisting of shares, risk-
free investments and a call option has initial value V (0) = 0. Subsequently, at
time 1:
• If stock goes up, then settle the option by paying the difference of $20
between the market price of one share and the strike price. You will pay
nothing if stock goes down. The cost to you will be C(1), which covers both
possibilities.
• Repay the loan with interest (or close your short position y = −4
11 in bonds).
This will cost you
4
11 × 110 = 40 dollars.
• Sell the stock for 1
2S(1) obtaining either 1
2 × 120 = 60 dollars if the price
goes up, or 1
2 × 80 = 40 dollars if it goes down.
The cash balance of these transactions will be zero, −C(1)+ 1
2S(1)−4
11A(1) = 0,
regardless of whether stock goes up or down. But you will be left with the initial
risk-free investment of C(0) +
4
11A(0) −1
2S(0) plus interest, thus realising an
arbitrage opportunity.
On the other hand, if C(0) + 4
11A(0) < 1
2S(0), then, at time 0:
• Buy 1 option for C(0) dollars.
• Buy
4
11 bonds for
4
11 × 100 = 400
11 dollars.
• Sell short x = 1
2 shares of stock for 1
2 × 100 = 50 dollars.
The cash balance of these transactions is positive, −C(0)−4
11A(0)+ 1
2S(0) > 0,
and can be invested risk-free. In this way you will have constructed a portfolio
with initial value V (0) = 0. Subsequently, at time 1:
• If stock goes up, then exercise the option, receiving the difference of $20
between the market price of one share and the strike price. You will receive
nothing if stock goes down. Your income will be C(1), which covers both
possibilities.
• Sell the bonds for
4
11A(1) =
4
11 × 110 = 40 dollars.
• Close the short position in stock, paying 1
2S(1), that is, 1
2 ×120 = 60 dollars
if the price goes up, or 1
2 × 80 = 40 dollars if it goes down.
The cash balance of these transactions will be zero, C(1)+ 4
11A(1)−1
2S(1) = 0,
regardless of whether stock goes up or down. But you will be left with an

1. Introduction: A Simple Market Model
17
arbitrage profit resulting from the risk-free investment of −C(0) −
4
11A(0) +
1
2S(0) plus interest, again a contradiction with the No-Arbitrage Principle.
Here we see once more that the arbitrage strategy follows a common sense
pattern: Sell (or sell short if necessary) expensive securities and buy cheap ones,
as long as all your financial obligations arising in the process can be discharged,
regardless of what happens in the future.
Proposition 1.3 implies that today’s price of the option must be
C(0) = 1
2S(0) −4
11A(0) ∼= 13.6364
dollars. Anyone who would sell the option for less or buy it for more than this
price would be creating an arbitrage opportunity, which amounts to handing
out free money. This completes the second step of our solution.
Remark 1.2
Note that the probabilities p and 1−p of stock going up or down are irrelevant
in pricing and replicating the option. This is a remarkable feature of the theory
and by no means a coincidence.
Remark 1.3
Options may appear to be superfluous in a market in which they can be repli-
cated by stock and bonds. In the simplified one-step model this is in fact a valid
objection. However, in a situation involving multiple time steps (or continuous
time) replication becomes a much more onerous task. It requires adjustments
to the positions in stock and bonds at every time instant at which there is a
change in prices, resulting in considerable management and transaction costs.
In some cases it may not even be possible to replicate an option precisely. This
is why the majority of investors prefer to buy or sell options, replication being
normally undertaken only by specialised dealers and institutions.
Exercise 1.7
Let the bond and stock prices A(0), A(1), S(0), S(1) be as above. Com-
pute the price C(0) of a call option with exercise time 1 and a) strike
price $90, b) strike price $110.
Exercise 1.8
Let the prices A(0), S(0), S(1) be as above. Compute the price C(0) of

18
Mathematics for Finance
a call option with strike price $100 and exercise time 1 if a) A(1) = 105
dollars, b) A(1) = 115 dollars.
A put option with strike price $100 and exercise time 1 gives the right to
sell one share of stock for $100 at time 1. This kind of option is worthless if
the stock goes up, but it brings a profit otherwise, the payoffbeing
P(1) =

0
if stock goes up,
20
if stock goes down,
given that the prices A(0), A(1), S(0), S(1) are the same as above. The notion
of a portfolio may be extended to allow positions in put options, denoted by z,
as before.
The replicating and pricing procedure for puts follows the same pattern as
for call options. In particular, the price P(0) of the put option is equal to the
time 0 value of a replicating investment in stock and bonds.
Remark 1.4
There is some similarity between a put option and a short forward position:
both involve selling an asset for a fixed price at a certain time in the future.
However, an essential difference is that the holder of a short forward contract
is committed to selling the asset for the fixed price, whereas the owner of a put
option has the right but no obligation to sell. Moreover, an investor who wants
to buy a put option will have to pay for it, whereas no payment is involved
when a forward contract is exchanged.
Exercise 1.9
Once again, let the bond and stock prices A(0), A(1), S(0), S(1) be as
above. Compute the price P(0) of a put option with strike price $100.
An investor may wish to trade simultaneously in both kinds of options and,
in addition, to take a forward position. In such cases new symbols z1, z2, z3, . . .
will need to be reserved for all additional securities to describe the positions
in a portfolio. A common feature of these new securities is that their payoffs
depend on the stock prices. Because of this they are called derivative securities
or contingent claims. The general properties of derivative securities will be
discussed in Chapter 7. In Chapter 8 the pricing and replicating schemes will
be extended to more complicated (and more realistic) market models, as well
as to other financial instruments.

1. Introduction: A Simple Market Model
19
1.7 Managing Risk with Options
The availability of options and other derivative securities extends the possible
investment scenarios. Suppose that your initial wealth is $1, 000 and compare
the following two investments in the setup of the previous section:
• buy 10 shares; at time 1 they will be worth
10 × S(1) =
 1, 200
if stock goes up,
800
if stock goes down;
or
• buy 1, 000/13.6364 ∼= 73.3333 options; in this case your final wealth will be
73.3333 × C(1) ∼=
 1, 466.67
if stock goes up,
0.00
if stock goes down.
If stock goes up, the investment in options will produce a much higher return
than shares, namely about 46.67%. However, it will be disastrous otherwise:
you will lose all your money. Meanwhile, when investing in shares, you would
gain just 20% or lose 20%. Without specifying the probabilities we cannot
compute the expected returns or standard deviations. Nevertheless, one would
readily agree that investing in options is more risky than in stock. This can be
exploited by adventurous investors.
Exercise 1.10
In the above setting, find the final wealth of an investor whose initial
capital of $1, 000 is split fifty-fifty between stock and options.
Options can also be employed to reduce risk. Consider an investor planning
to purchase stock in the future. The share price today is S(0) = 100 dollars,
but the investor will only have funds available at a future time t = 1, when the
share price will become
S(1) =
 160
with probability p,
40
with probability 1 −p,
for some 0 < p < 1. Assume, as before, that A(0) = 100 and A(1) = 110
dollars, and compare the following two strategies:
• wait until time 1, when the funds become available, and purchase the stock
for S(1);
or

20
Mathematics for Finance
• at time 0 borrow money to buy a call option with strike price $100; then, at
time 1 repay the loan with interest and purchase the stock, exercising the
option if the stock price goes up.
The investor will be open to considerable risk if she chooses to follow the first
strategy. On the other hand, following the second strategy, she will need to
borrow C(0) ∼= 31.8182 dollars to pay for the option. At time 1 she will have
to repay $35 to clear the loan and may use the option to purchase the stock,
hence the cost of purchasing one share will be
S(1) −C(1) + 35 =
 135
if stock goes up,
75
if stock goes down.
Clearly, the risk is reduced, the spread between these two figures being narrower
than before.
Exercise 1.11
Compute the risk (as measured by the standard deviation of the return)
involved in purchasing one share with and without the option if a) p =
0.25, b) p = 0.5, c) p = 0.75.
Exercise 1.12
Show that the risk (as measured by the standard deviation) of the above
strategy involving an option is a half of that when no option is purchased,
no matter what the probability 0 < p < 1 is.
If two options are bought, then the risk will be reduced to nil:
S(1) −2 × C(1) + 70 = 110 with probability 1.
This strategy turns out to be equivalent to a long forward contract, since the
forward price of the stock is exactly $110 (see Section 1.5). It is also equivalent
to borrowing money to purchase a share for $100 today and repaying $110 to
clear the loan at time 1.
Chapter 9 on financial engineering will discuss various ways of managing
risk with options: magnifying or reducing risk, dealing with complicated risk
exposure, and constructing payoffprofiles tailor made to meet the specific needs
of an investor.

2
Risk-Free Assets
2.1 Time Value of Money
It is a fact of life that $100 to be received after one year is worth less than
the same amount today. The main reason is that money due in the future or
locked in a fixed term account cannot be spent right away. One would therefore
expect to be compensated for postponed consumption. In addition, prices may
rise in the meantime and the amount will not have the same purchasing power
as it would have at present. Finally, there is always a risk, even if a negligible
one, that the money will never be received. Whenever a future payment is
uncertain to some degree, its value today will be reduced to compensate for
the risk. (However, in the present chapter we shall consider situations free from
such risk.) As generic examples of risk-free assets we shall consider a bank
deposit or a bond.
The way in which money changes its value in time is a complex issue of
fundamental importance in finance. We shall be concerned mainly with two
questions:
What is the future value of an amount invested or borrowed today?
What is the present value of an amount to be paid or received at
a certain time in the future?
The answers depend on various factors, which will be discussed in the present
chapter. This topic is often referred to as the time value of money.
21


## Risky Assets

42
Mathematics for Finance
dollars. Observe that the total wealth at time 1 is
V (1) + C = V (0)er.
Six months later the bond will be worth
V (1.5) = 10e−0.5r + 10e−1.5r + 10e−2.5r + 110e−3.5r ∼= 97.45
dollars. After four years the bond will become a zero-coupon bond with face
value $110 and price
V (4) = 110e−r ∼= 97.56
dollars.
An investor may choose to sell the bond at any time prior to maturity. The
price at that time can once again be found by discounting all the payments due
at later times.
Exercise 2.32
Sketch the graph of the price of the coupon bond in Examples 2.9
and 2.10 as a function of time.
Exercise 2.33
How long will it take for the price of the coupon bond in Examples 2.9
and 2.10 to reach $95 for the first time?
The coupon can be expressed as a fraction of the face value. Assuming that
coupons are paid annually, we shall write C = iF, where i is called the coupon
rate.
Proposition 2.5
Whenever coupons are paid annually, the coupon rate is equal to the interest
rate for annual compounding if and only if the price of the bond is equal to its
face value. In this case we say that the bond sells at par.
Proof
To avoid cumbersome notation we restrict ourselves to an example. Suppose
that annual compounding with r = i applies, and consider a bond with face
value F = 100 maturing in three years, T = 3. Then the price of the bond is
C
1 + r +
C
(1 + r)2 + F + C
(1 + r)3 =
rF
1 + r +
rF
(1 + r)2 + F(1 + r)
(1 + r)3

2. Risk-Free Assets
43
=
rF
1 + r +
rF
(1 + r)2 +
F
(1 + r)2 =
rF
1 + r + F(1 + r)
(1 + r)2 = F.
Conversely, note that
C
1 + r +
C
(1 + r)2 + F + C
(1 + r)3
is one-to-one as a function of r (in fact, a strictly decreasing function), so it
assumes the value F exactly once, and we know this happens for r = i.
Remark 2.9
If a bond sells below the face value, it means that the implied interest rate
is higher than the coupon rate (since the price of a bond decreases when the
interest rate goes up). If the bond price is higher than the face value, it means
that the interest rate is lower than the coupon rate. This may be important
information in real circumstances, where the bond price is determined by the
market and gives an indication of the level of interest rates.
Exercise 2.34
A bond with face value F = 100 and annual coupons C = 8 maturing
after three years, at T = 3, is trading at par. Find the implied continuous
compounding rate.
2.2.3 Money Market Account
An investment in the money market can be realised by means of a financial
intermediary, typically an investment bank, who buys and sells bonds on behalf
of its customers (thus reducing transaction costs). The risk-free position of
an investor is given by the level of his or her account with the bank. It is
convenient to think of this account as a tradable asset, which is indeed the
case, since the bonds themselves are tradable. A long position in the money
market involves buying the asset, that is, investing money. A short position
amounts to borrowing money.
First, consider an investment in a zero-coupon bond closed prior to maturity.
An initial amount A(0) invested in the money market makes it possible to
purchase A(0)/B(0, T) bonds. The value of each bond will fetch
B(t, T) = e−(T −t)r = erte−rT = ertB(0, T)

44
Mathematics for Finance
at time t. As a result, the investment will reach
A(t) =
A(0)
B(0, T)B(t, T) = A(0)ert
at time t ≤T.
Exercise 2.35
Find the return on a 75-day investment in zero-coupon bonds if B(0, 1) =
0.89.
Exercise 2.36
The return on a bond over six months is 7%. Find the implied continuous
compounding rate.
Exercise 2.37
After how many days will a bond purchased for B(0, 1) = 0.92 produce
a 5% return?
The investment in a bond has a finite time horizon. It will be terminated
with A(T) = A(0)erT at the time T of maturity of the bond. To extend the
position in the money market beyond T one can reinvest the amount A(T) into
a bond newly issued at time T, maturing at T ′ > T. Taking A(T) as the initial
investment with T playing the role of the starting time, we have
A(t′) = A(T)er(t′−T ) = A(0)ert′
for T ≤t′ ≤T ′. By repeating this argument, we readily arrive at the conclu-
sion that an investment in the money market can be prolonged for as long as
required, the formula
A(t) = A(0)ert
(2.14)
being valid for all t ≥0.
Exercise 2.38
Suppose that one dollar is invested in zero-coupon bonds maturing after
one year. At the end of each year the proceeds are reinvested in new
bonds of the same kind. How many bonds will be purchased at the
end of year 9? Express the answer in terms of the implied continuous
compounding rate.

2. Risk-Free Assets
45
An alternative way to prolong an investment in the money market for as
long as required is to reinvest the face value of any bonds maturing at time T
in other bonds issued at time 0, but maturing at a later time t > T. Having
invested A(0) initially to buy unit bonds maturing at time T, we will have the
sum of A(0)/B(0, T) at our disposal at time T. At this time we chose a bond
maturing at time t, its price at T being B(T, t). At time t this investment will
be worth
A(0)
B(0, T)B(T, t) =
A(0)
B(0, t) = A(0)ert,
the same as in (2.14).
Finally, consider coupon bonds as a tool to manufacture an investment in
the money market. Suppose for simplicity that the first coupon C is due after
one year. At time 0 we buy A(0)/V (0) coupon bonds. After one year we cash the
coupon and sell the bond for V (1), receiving the total sum C + V (1) = V (0)er
(see Example 2.10). Because the interest rate is constant, this sum of money is
certain. In this way we have effectively created a zero-coupon bond with face
value V (0)er maturing at time 1. It means that the scheme worked out above
for zero-coupon bonds applies to coupon bonds as well, resulting in the same
formula (2.14) for A(t).
Exercise 2.39
The sum of $1, 000 is invested in five-year bonds with face value $100
and $8 coupons paid annually. All coupons are reinvested in bonds of the
same kind. Assuming that the bonds are trading at par and the interest
rate remains constant throughout the period to maturity, compute the
number of bonds held during each consecutive year of the investment.
As we have seen, under the assumption that the interest rate is constant,
the function A(t) does not depend on the way the money market account is
run, that is, it neither depends on the types of bonds selected for investment
nor on the method of extending the investment beyond the maturity of the
bonds.
Throughout most of this book we shall assume A(t) to be deterministic and
known. Indeed, we assume that A(t) = ert, where r is a constant interest rate.
Variable interest rates will be considered in Chapter 10 and a random money
market account will be studied in Chapter 11.

This page intentionally left blank 

3
Risky Assets
The future prices of any asset are unpredictable to a certain extent. In this
chapter we shall typically be concerned with common stock, though any security
such as foreign currency, a commodity, or even a partially unpredictable future
cash flow can be considered. Market prices depend on the choices and decisions
made by a great number of agents acting under conditions of uncertainty. It
is therefore reasonable to treat the prices of assets as random. However, little
more can be said in a fully general situation. We shall therefore impose specific
conditions on asset prices, motivated by a need for the mathematical model to
be realistic and relevant on the one hand, and tractable on the other hand.
3.1 Dynamics of Stock Prices
The price of stock at time t will be denoted by S(t). It is assumed to be strictly
positive for all t. We take t = 0 to be the present time, S(0) being the current
stock price, known to all investors. The future prices S(t) for t > 0 remain
unknown, in general. Mathematically, S(t) can be represented as a positive
random variable on a probability space Ω, that is,
S(t) : Ω→(0, ∞).
The probability space Ωconsists of all feasible price movement ‘scenarios’ ω ∈
Ω. We shall write S(t, ω) to denote the price at time t if the market follows
scenario ω ∈Ω.
47

48
Mathematics for Finance
The current stock price S(0) known to all investors is simply a positive
number, but it can be thought of as a constant random variable. The unknown
future prices S(t) for t > 0 are non-constant random variables. This means that
for each t > 0 there are at least two scenarios ω, ω ∈Ωsuch that S(t, ω) ̸=
S(t, ω).
We assume that time runs in a discrete manner, t = nτ, where n =
0, 1, 2, 3, . . . and τ is a fixed time step, typically a year, a month, a week, a
day, or even a minute or a second to describe some hectic trading. Because we
take one year as the unit measure of time, a month corresponds to τ = 1/12, a
week corresponds to τ = 1/52, a day to τ = 1/365, and so on.
To simplify our notation we shall write S(0), S(1), S(2), . . . , S(n), . . . instead
of S(0), S(τ), S(2τ), . . . , S(nτ), . . . , identifying n with nτ. This convention will
in fact be adopted for many other time-dependent quantities.
Example 3.1
Consider a market that can follow just two scenarios, boom or recession, de-
noted by ω1 and ω2, respectively. The current share price of a certain stock is
$10, which may rise to $12 after one year if there is a boom or come down to
$7 in the case of recession. In these circumstances Ω= {ω1, ω2} and, putting
τ = 1, we have
Scenario
S(0)
S(1)
ω1 (boom)
10
12
ω2 (recession)
10
7
Example 3.2
Suppose that there are three possible market scenarios, Ω= {ω1, ω2, ω3}, the
stock prices taking the following values over two time steps:
Scenario
S(0)
S(1)
S(2)
ω1
55
58
60
ω2
55
58
52
ω3
55
52
53
These price movements can be represented as a tree, see Figure 3.1. It is con-
venient to identify the scenarios with paths through the tree leading from the
single node on the left (the ‘root’ of the tree) to the rightmost branch tips.
Such a tree structure of price movements, if found realistic and desirable,
can readily be implemented in a mathematical model.

3. Risky Assets
49
Figure 3.1
Tree of price movements in Example 3.2
Exercise 3.1
Sketch a tree representing the scenarios and price movements in Exam-
ple 3.1.
Exercise 3.2
Suppose that the stock price on any given day can either be 5% higher or
4% lower than on the previous day. Sketch a tree representing possible
stock price movements over the next three days, given that the price
today is $20. How many different scenarios can be distinguished?
3.1.1 Return
It proves convenient to describe the dynamics of stock prices S(n) in terms of
returns. We assume that the stock pays no dividends.
Definition 3.1
The rate of return, or briefly the return K(n, m) over a time interval [n, m] (in
fact [mτ, nτ]), is defined to be the random variable
K(n, m) = S(m) −S(n)
S(n)
.
The return over a single time step [n −1, n] will be denoted by K(n), that is
K(n) = K(n −1, n) = S(n) −S(n −1)
S(n −1)
,
which implies that
S(n) = S(n −1)(1 + K(n)).
(3.1)

50
Mathematics for Finance
Example 3.3
In the situation considered in Example 3.2 the returns are random variables
taking the following values:
Scenario
K(1)
K(2)
ω1
5.45%
3.45%
ω2
5.45%
−10.34%
ω3
−5.45%
1.92%
Exercise 3.3
Given the following returns and assuming that S(0) = 45 dollars, find
the possible stock prices in a three-step economy and sketch a tree of
price movements:
Scenario
K(1)
K(2)
K(3)
ω1
10%
5%
−10%
ω2
5%
10%
10%
ω3
5%
−10%
10%
Remark 3.1
If the stock pays a dividend of div(n) at time n, then the definition of return
has to be modified. Typically, when a dividend is paid, the stock price drops
by that amount. Since the right to a dividend is decided prior to the payment
day, the drop of stock price is already reflected in S(n). As a result, an investor
who buys stock at time n −1 paying S(n −1) and wishes to sell the stock at
time n will receive S(n) + div(n) and the return must reflect this:
K(n) = S(n) −S(n −1) + div(n)
S(n −1)
.
Exercise 3.4
Introduce the necessary modifications in Exercise 3.3 if a dividend of $1
is paid at the end of each time step.
It is important to understand the relationship between one-step returns and
the return over a longer time interval.

3. Risky Assets
51
Example 3.4
Suppose that S(0) = 100 dollars.
1. Consider a scenario in which S(1) = 110 and S(2) = 100 dollars. In this
case K(0, 2) = 0%, while K(1) = 10% and K(2) ∼= −9.09%, the sum of the
one-step returns K(1) and K(2) being positive and greater than K(0, 2).
2. Consider another scenario with lower price S(1) = 90 dollars and with
S(2) = 100 dollars as before. Then K(1) = −10% and K(2) ∼= 11.11%,
their sum being once again greater than K(0, 2) = 0%.
3. In a scenario such that S(1) = 110 and S(2) = 121 dollars we have K(0, 2) =
21%, which is greater than K(1) + K(2) = 10% + 10% = 20%.
Exercise 3.5
Find K(0, 2) and K(0, 3) for the data in Exercise 3.3 and compare the
results with the sums of one-step returns K(1)+K(2) and K(1)+K(2)+
K(3), respectively.
Remark 3.2
The non-additivity of returns, already observed in Chapter 2 for deterministic
returns, is worth pointing out, since it is common practice to compute the av-
erage of recorded past returns as a prediction for the future. This may result in
misrepresenting the information, for example, overestimating the future return
if the historical prices tend to fluctuate, or underestimating if they do not.
Proposition 3.1
The precise relationship between consecutive one-step returns and the return
over the aggregate period is
1 + K(n, m) = (1 + K(n + 1))(1 + K(n + 2)) · · · (1 + K(m)).
Proof
Compare the following two formulae for S(m):
S(m) = S(n)(1 + K(n, m))
and
S(m) = S(n)(1 + K(n + 1))(1 + K(n + 2)) · · · (1 + K(m)).
Both of them follow from Definition 3.1.

52
Mathematics for Finance
Exercise 3.6
In each of the following three scenarios find the one-step returns, assum-
ing that K(1) = K(2):
Scenario
S(0)
S(2)
ω1
35
41
ω2
35
32
ω3
35
28
Exercise 3.7
Given that K(1) = 10% or −10%, and K(0, 2) = 21%, 10% or −1%,
find a possible structure of scenarios such that K(2) takes at most two
different values.
The lack of additivity is often an inconvenience. This can be rectified by
introducing the logarithmic return on a risky security, motivated by similar
considerations for risk-free assets in Chapter 2.
Definition 3.2
The logarithmic return over a time interval [n, m] (more precisely, [τn, τm]) is
a random variable k(n, m) defined by
k(n, m) = ln S(m)
S(n) .
The one-step logarithmic return will be denoted simply by k(n), that is,
k(n) = k(n −1, n) = ln
S(n)
S(n −1),
so that
S(n) = S(n −1)ek(n).
(3.2)
The relationship between the return K(m, n) and the logarithmic return
k(m, n) is obvious by comparing their definitions, namely
1 + K(m, n) = ek(m,n).
Because of this we can readily switch from one return to the other.

3. Risky Assets
53
Remark 3.3
If the stock pays a dividend of div(n) at time n and this is reflected in the price
S(n), then the following version of the logarithmic return should be used:
k(n) = ln S(n) + div(n)
S(n −1)
.
Consecutive one-step logarithmic returns can be combined in an additive
manner to find the return during the overall time period.
Exercise 3.8
For the data in Example 3.2 find the random variables k(1), k(2) and
k(0, 2). Compare k(0, 2) with k(1) + k(2).
Proposition 3.2
If no dividends are paid, then
k(n, m) = k(n + 1) + k(n + 2) + · · · + k(m).
Proof
On the one hand,
S(m) = S(n)ek(n,m)
by the definition of the logarithmic return. On the other hand, using one-step
logarithmic returns repeatedly, we obtain,
S(m) = S(n)ek(n+1)ek(n+2) · · · ek(m) = S(n)ek(n+1)+k(n+2)+···+k(m).
The result follows by comparing these two expressions.
3.1.2 Expected Return
Suppose that the probability distribution of the return K over a certain time
period is known. Then we can compute the mathematical expectation E(K),
called the expected return.
Example 3.5
We estimate the probabilities of recession, stagnation and boom to be 1/4,
1/2, 1/4, respectively. If the predicted annual returns on some stock in these

54
Mathematics for Finance
scenarios are −6%, 4%, 30%, respectively, then the expected annual return is
−6% × 1
4 + 4% × 1
2 + 30% × 1
4 = 8%.
Exercise 3.9
With the probabilities of recession, stagnation and boom equal to 1/2,
1/4, 1/4 and the predicted annual returns in the first two of these scenar-
ios at −5% and 6%, respectively, find the annual return in the remaining
scenario if the expected annual return is known to be 6%.
Exercise 3.10
Suppose that the stock prices in the following three scenarios are
Scenario
S(0)
S(1)
S(2)
ω1
100
110
120
ω2
100
105
100
ω3
100
90
100
with probabilities 1/4, 1/4, 1/2, respectively. Find the expected returns
E(K(1)), E(K(2)) and E(K(0, 2)). Compare 1 + E(K(0, 2)) with (1 +
E(K(1)))(1 + E(K(2))).
The last exercise shows that the relation established in Proposition 3.1 does
not extend to expected returns. For that we need an additional assumption.
Proposition 3.3
If the one-step returns K(n + 1), . . . , K(m) are independent, then
1 + E(K(n, m)) = (1 + E(K(n + 1)))(1 + E(K(n + 2))) · · · (1 + E(K(m))).
Proof
This is an immediate consequence of Proposition 3.1 and the fact that the
expectation of a product of independent random variables is the product of
expectations. (Note that if the K(i) are independent, then so are the random
variables 1 + K(i) for i = n + 1, . . . , m.)

3. Risky Assets
55
Exercise 3.11
Suppose that the time step is taken to be three months, τ = 1/4, and
the quarterly returns K(1), K(2), K(3), K(4) are independent and iden-
tically distributed. Find the expected quarterly return E(K(1)) and the
expected annual return E(K(0, 4)) if the expected return E(K(0, 3))
over three quarters is 12%.
Remark 3.4
In the case of logarithmic returns additivity extends to expected returns, even
if the one-step returns are not independent. Namely
E(k(n, m)) = E(k(n + 1)) + E(k(n + 2)) + · · · + E(k(m)).
This is because the expectation of a sum of random variables is the sum of
expectations.
Remark 3.5
In practice it is difficult to estimate the probabilities and returns in each sce-
nario, needed to compute the expected return. What can readily be computed
is the average return over a past period. The result can be used as an estimate
for the expected future return. For example, if the stock prices on the last
10 consecutive days were $98, $100, $99, $95, $88, $82, $89, $98, $101, $105, then
the average of the resulting nine daily returns would be about 0.77%. However,
the average of the last four daily returns would be about 6.18%. (We use log-
arithmic returns because of their additivity.) This shows that the result may
depend heavily on the choice of data. Using historical prices for prediction is a
complex statistical issue belonging to Econometrics, which is beyond the scope
of this book.
3.2 Binomial Tree Model
We shall discuss an extremely important model of stock prices. On the one
hand, the model is easily tractable mathematically because it involves a small
number of parameters and assumes an identical simple structure at each node
of the tree of stock prices. On the other hand, it captures surprisingly many
features of real-world markets.
The model is defined by the following conditions.

56
Mathematics for Finance
Condition 3.1
The one-step returns K(n) on stock are identically distributed independent
random variables such that
K(n) =
 u
with probability p,
d
with probability 1 −p,
at each time step n, where −1 < d < u and 0 < p < 1.
This condition implies that the stock price S(n) can move up or down by a
factor 1 + u or 1 + d at each time step. The inequalities −1 < d < u guarantee
that all prices S(n) will be positive if S(0) is.
Let r be the return on a risk-free investment over a single time step of
length τ.
Condition 3.2
The one-step return r on a risk-free investment is the same at each time step
and
d < r < u.
The last condition describes the movements of stock prices in relation to
risk-free assets such as bonds or cash held in a bank account. The inequalities
d < r < u are justified because of Proposition 1.1 in Chapter 1 (which will be
generalised in Proposition 4.2).
Since S(1)/S(0) = 1+K(1), Condition 3.1 implies that the random variable
S(1) can take two different values,
S(1) =
 S(0)(1 + u)
with probability p,
S(0)(1 + d)
with probability 1 −p.
Exercise 3.12
How many different values do the random variables S(2) and S(3) take?
What are these values and the corresponding probabilities?
The values of S(n) along with the corresponding probabilities can be found
for any n by extending the solution to Exercise 3.12. In an n-step tree of stock
prices each scenario (or path through the tree) with exactly i upward and n−i
downward price movements produces the same stock price S(0)(1 + u)i(1 +

3. Risky Assets
57
d)n−i at time n. There are
n
i

such scenarios, the probability of each equal to
pi(1 −p)n−i. As a result,
S(n) = S(0)(1 + u)i(1 + d)n−i with probability
	n
i

pi(1 −p)n−i
(3.3)
for i = 0, 1, . . . , n. The stock price S(n) at time n is a discrete random variable
with n + 1 different values. The distribution of S(n) as given by (3.3) is shown
in Figure 3.2 for n = 10, p = 0.5, S(0) = 1, u = 0.1 and d = −0.1.
Figure 3.2
Distribution of S(10)
The number i of upward price movements is a random variable with a
binomial distribution. The same is true for the number n −i of downward
movements. We therefore say that the price process follows a binomial tree. In
an n-step binomial three the set Ωof all scenarios, that is, n-step paths moving
up or down at each step has 2n elements. An example of a two-step binomial
tree of stock prices is shown in Figure 3.3 and a three-step tree in Figure 3.4.
Figure 3.3
Two-step binomial tree of stock prices
In both figures S(0) = 1 for simplicity.

58
Mathematics for Finance
Figure 3.4
Three-step binomial tree of stock prices
Exercise 3.13
Find d and u if S(1) can take two values, $87 or $76, and the top possible
value of S(2) is $92.
Exercise 3.14
Suppose that the risk-free rate under continuous compounding is 14%,
the time step τ is one month, S(0) = 22 dollars and d = −0.01. Find the
bounds on the middle value of S(2) consistent with Condition 3.2.
Exercise 3.15
Suppose that $32, $28 and x are the possible values of S(2). Find x,
assuming that stock prices follow a binomial tree. Can you complete the
tree? Can this be done uniquely?
Exercise 3.16
Suppose that stock prices follow a binomial tree, the possible values of
S(2) being $121, $110 and $100. Find u and d when S(0) = 100 dollars.
Do the same when S(0) = 104 dollars.
3.2.1 Risk-Neutral Probability
While the future value of stock can never be known with certainty, it is possible
to work out expected stock prices within the binomial tree model. It is then
natural to compare these expected prices and risk-free investments. This simple
idea will lead us towards powerful and surprising applications in the theory of
derivative securities (for example, options, forwards, futures), to be studied in

3. Risky Assets
59
later chapters.
To begin with, we shall work out the dynamics of expected stock prices
E(S(n)). For n = 1
E(S(1)) = pS(0)(1 + u) + (1 −p)S(0)(1 + d) = S(0)(1 + E(K(1))),
where
E(K(1)) = pu + (1 −p)d
is the expected one-step return. This extends to any n as follows.
Proposition 3.4
The expected stock prices for n = 0, 1, 2, . . . are given by
E(S(n)) = S(0)(1 + E(K(1)))n.
Proof
Since the one-step returns K(1), K(2), . . . are independent, so are the random
variables 1 + K(1), 1 + K(2), . . . . It follows that
E(S(n)) = E(S(0)(1 + K(1))(1 + K(2)) · · · (1 + K(n)))
= S(0)E(1 + K(1))E(1 + K(2)) · · · E(1 + K(n))
= S(0)(1 + E(K(1)))(1 + E(K(2))) · · · (1 + E(K(n))).
Because the K(n) are identically distributed, they all have the same expecta-
tion,
E(K(1)) = E(K(2)) = · · · = E(K(n)),
which proves the formula for E(S(n)).
If the amount S(0) were to be invested risk-free at time 0, it would grow to
S(0)(1 + r)n after n steps. Clearly, to compare E(S(n)) and S(0)(1 + r)n we
only need to compare E(K(1)) and r.
An investment in stock always involves an element of risk, simply because
the price S(n) is unknown in advance. A typical risk-averse investor will re-
quire that E(K(1)) > r, arguing that he or she should be rewarded with a
higher expected return as a compensation for risk. The reverse situation when
E(K(1)) < r may nevertheless be attractive to some investors if the risky re-
turn is high with small non-zero probability and low with large probability.
(A typical example is a lottery, where the expected return is negative.) An
investor of this kind can be called a risk-seeker. We shall return to this topic

60
Mathematics for Finance
in Chapter 5, where a precise definition of risk will be developed. The border
case of a market in which E(K(1)) = r is referred to as risk-neutral.
It proves convenient to introduce a special symbol p∗for the probability as
well as E∗for the corresponding expectation satisfying the condition
E∗(K(1)) = p∗u + (1 −p∗)d = r
(3.4)
for risk-neutrality, which implies that
p∗= r −d
u −d.
We shall call p∗the risk-neutral probability and E∗the risk-neutral expecta-
tion. It is important to understand that p∗is an abstract mathematical object,
which may or may not be equal to the actual market probability p. Only in a
risk-neutral market do we have p = p∗. Even though the risk-neutral probabil-
ity p∗may have no relation to the actual probability p, it turns out that for
the purpose of valuation of derivative securities the relevant probability is p∗,
rather than p. This application of the risk-neutral probability, which is of great
practical importance, will be discussed in detail in Chapter 8.
Exercise 3.17
Let u = 2/10 and r = 1/10. Investigate the properties of p∗as a function
of d.
Exercise 3.18
Show that d < r < u if and only if 0 < p∗< 1.
Condition (3.4) implies that
p∗(u −r) + (1 −p∗)(d −r) = 0.
Geometrically, this means that the pair (p∗, 1 −p∗) regarded as a vector on
the plane R2 is orthogonal to the vector with coordinates (u −r, d −r), which
represents the possible one-step gains (or losses) of an investor holding a single
share of stock, the purchase of which was financed by a cash loan attracting
interest at a rate r, see Figure 3.5. The line joining the points (1, 0) and (0, 1)
consists of all points with coordinates (p, 1 −p), where 0 < p < 1. One of these
points corresponds to the actual market probability and one to the risk-neutral
probability.
Another interpretation of condition (3.4) for the risk-neutral probability is
illustrated in Figure 3.6. If masses p∗and 1 −p∗are attached at the points
with coordinates u and d on the real axis, then the centre of mass will be at r.

3. Risky Assets
61
Figure 3.5
Geometric interpretation of risk-neutral probability p∗
Figure 3.6
Barycentric interpretation of risk-neutral probability p∗
3.2.2 Martingale Property
By Proposition 3.4 the expectation of S(n) with respect to the risk-neutral
probability p∗is
E∗(S(n)) = S(0)(1 + r)n,
(3.5)
since r = E∗(K(1)).
Example 3.6
Consider a two-step binomial tree model such that S(0) = 100 dollars, u = 0.2,
d = −0.1 and r = 0.1. Then p∗= 2/3 is the risk-neutral probability, and the
expected stock price after two steps is
E∗(S(2)) = S(0)(1 + r)2 = 121
dollars. After one time step, once it becomes known whether the stock price has
gone up or down, we shall need to recompute the expectation of S(2). Suppose
that the stock price has gone up to $120 after the first step. In these circum-
stances the set of possible scenarios reduces to those for which S(1) = 120
dollars, and the tree of stock prices reduces to the subtree in Figure 3.7. Given
that S(1) = 120 dollars, the risk-neutral expectation of S(2) will therefore be

62
Mathematics for Finance
Figure 3.7
Subtree such that S(1) = 120 dollars
2
3 ×144+ 1
3 ×108 = 132 dollars, which is equal to 120(1+r). Formally, this can
be written using the conditional expectation1 of S(2) given that S(1) = 120,
E∗(S(2)|S(1) = 120) = 120(1 + r).
Similarly, if the stock price drops to $90 after one time step, the set of possible
scenarios will reduce to those for which S(1) = 90 dollars, and the tree of stock
prices will reduce to the subtree in Figure 3.8. Given that S(1) = 90 dollars,
Figure 3.8
Subtree such that S(1) = 90 dollars
the risk-neutral expectation of S(2) will be 2
3 ×108+ 1
3 ×81 = 99 dollars, which
is equal to 90(1 + r). This can be written as
E∗(S(2)|S(1) = 90) = 90(1 + r).
The last two formulae involving conditional expectation can be written as a
single equality, properly understood:
E∗(S(2)|S(1)) = S(1)(1 + r).
This analysis can be extended to any time step in the binomial tree model.
Suppose that n time steps have passed and the stock price has become S(n).
What is the risk-neutral expectation of the price S(n + 1) after one more step?
1 The conditional expectation of a random variable ξ given an event A such that
P(A) ̸= 0 is defined by E(ξ|A) = E(ξ1A)/P(A), where 1A is the indicator random
variable, equal to 1 on A and 0 on the complement of A.

3. Risky Assets
63
Proposition 3.5
Given that the stock price S(n) has become known at time n, the risk-neutral
conditional expectation of S(n + 1) will be
E∗(S(n + 1)|S(n)) = S(n)(1 + r).
Proof
Suppose that S(n) = x after n time steps. Then
E∗(S(n + 1)|S(n) = x) = p∗x(1 + u) + (1 −p∗)x(1 + d)
because S(n + 1) takes the value x(1 + u) with probability p∗and x(1 + d)
with probability 1 −p∗. But p∗(1 + u) + (1 −p∗)(1 + d) = 1 + r by (3.4), which
implies that
E∗(S(n + 1)|S(n) = x) = x(1 + r)
for any possible value x of S(n), completing the proof.
Dividing both sides of the equality in Proposition 3.5 by (1 + r)n+1, we
obtain the following important result for the discounted stock prices S(n) =
S(n) (1 + r)−n.
Corollary 3.6 (Martingale Property)
For any n = 0, 1, 2, . . .
E∗(S(n + 1)|S(n)) = S(n).
We say that the discounted stock prices S(n) form a martingale under the
risk-neutral probability p∗. The probability p∗itself is also referred to as the
martingale probability.
Exercise 3.19
Let r = 0.2. Find the risk-neutral conditional expectation of S(3) given
that S(2) = 110 dollars.
3.3 Other Models
This section may be skipped at first reading because the main ideas to follow
later do not depend on the models presented here.

64
Mathematics for Finance
3.3.1 Trinomial Tree Model
A natural generalisation of the binomial tree model extends the range of possi-
ble values of the one-step returns K(n) to three. The idea is to allow the price
not only to move up or down, but also to take an intermediate value at any
given step.
Condition 3.3
The one-step returns K(n) are independent random variables of the form
K(n) =



u
with probability p,
n
with probability q,
d
with probability 1 −p −q,
where d < n < u and 0 < p, q, p + q < 1.
This means that u and d represent upward and downward price movements,
as before, whereas n stands for the middle price movement, typically a neutral
one, n = 0.
Condition 3.4
The one-step return r on a risk-free investment is the same at each time step
and
d < r < u.
Since S(1)/S(0) = 1 + K(1), Condition 3.3 implies that S(1) takes three
different values,
S(1) =



S(0)(1 + u)
S(0)(1 + n)
S(0)(1 + d)
with probability p,
with probability q,
with probability 1 −p −q.
Exercise 3.20
How many different values does the random variable S(2) take? What
are these values and the corresponding probabilities?
The condition E∗(K(n)) = r for risk-neutral probabilities p∗, q∗can be
written as
p∗(u −r) + q∗(n −r) + (1 −p∗−q∗)(d −r) = 0.
(3.6)

3. Risky Assets
65
The triple (p∗, q∗, 1 −p∗−q∗) regarded as a vector in R3 is orthogonal to the
vector with coordinates (u −r, n −r, d −r) representing the possible one-step
gains (or losses) of an investor holding a singe share of stock, the purchase of
which was financed by a cash loan. This means that (p∗, q∗, 1 −p∗−q∗) lies on
the intersection of the triangle {(a, b, c) : a, b, c ≥0, a+b+c = 1} and the plane
orthogonal to the gains vector (u−r, n−r, d−r), as in Figure 3.9. Condition 3.4
Figure 3.9
Geometric interpretation of risk-neutral probabilities p∗, q∗
guarantees that the intersection is non-empty, since the line containing the
vector (u −r, n −r, d −r) does not pass through the positive octant. In this
case there are infinitely many risk-neutral probabilities, the intersection being
a line segment.
Another interpretation of condition (3.6) for the risk-neutral probability is
illustrated in Figure 3.10. If masses p∗, q∗and 1 −p∗−q∗are attached at the
points with coordinates u, n and d on the real axis, then the centre of mass
will be at r.
Figure 3.10
Barycentric interpretation of risk-neutral probabilities p∗, q∗
Exercise 3.21
Let u = 0.2, n = 0, d = −0.1, and r = 0. Find all risk-neutral probabili-
ties.

66
Mathematics for Finance
3.3.2 Continuous-Time Limit
Discrete-time and discrete-price models have apparent disadvantages. They
clearly restrict the range of asset price movements as well as the set of time
instants at which these movements may occur. In this section we shall outline
an approach free from such restrictions. It will be obtained by passing to the
continuous-time limit from the binomial tree model.
We shall consider a sequence of binomial tree models with time step τ = 1
N ,
letting N →∞. For all binomial tree models in the approximating sequence it
will be assumed that the probability of upward and downward price movements
is 1
2 in each step.
In this context it proves convenient to use the logarithmic return
k(n) = ln(1 + K(n)) =
 ln(1 + u)
with probability 1/2,
ln(1 + d)
with probability 1/2.
In place of the risk-free rate of return over one time step, we shall use the
equivalent continuous compounding rate r, so that the return over a time step
of length τ will be eτr.
We denote by m the expectation and by σ the standard deviation of the
logarithmic return k(1)+k(2)+· · ·+k(N) over the unit time interval from 0 to 1,
consisting of N steps of
τ. The logarithmic returns k(1), k(2), . . . , k(N)
are identically distributed and independent, just as K(1), K(2), . . . , K(N) are.
It follows that
m = E (k(1) + k(2) + · · · + k(N))
= E(k(1)) + E(k(2)) + · · · + E(k(N)) = NE(k(n)),
σ2 = Var (k(1) + k(2) + · · · + k(N))
= Var (k(1)) + Var (k(2)) + · · · + Var (k(N)) = NVar (k(n))
for each n = 1, 2, . . . , N. This means that each k(n) has expectation m
N = mτ
and standard deviation

σ2
N = σ√τ, so the two possible values of each k(n)
must be
ln(1 + u) = mτ + σ√τ,
ln(1 + d) = mτ −σ√τ.
(3.7)
Exercise 3.22
Find m and σ for u = 0.02, d = −0.01 and τ = 1/12.
length

3. Risky Assets
67
Introducing a sequence of independent random variables ξ(n), each with
two values
ξ(n) =
 +√τ
with probability 1/2,
−√τ
with probability 1/2,
we can write the logarithmic return as
k(n) = mτ + σξ(n).
Exercise 3.23
Find the expectation and variance of ξ(n) and k(n).
Exercise 3.24
Write S(1) and S(2) in terms of m, σ, τ, ξ(1) and ξ(2).
Next, we introduce an important sequence of random variables w(n), called
a symmetric random walk, such that
w(n) = ξ(1) + ξ(2) + · · · + ξ(n),
and w(0) = 0. Clearly, ξ(n) = w(n) −w(n −1). Because of the last equality,
the ξ(n) are referred to as the increments of w(n).
From now on we shall often write S(t) and w(t) instead of S(n) and w(n)
for t = τn, where n = 1, 2, . . . .
Proposition 3.7
The stock price at time t = τn is given by
S(t) = S(0) exp(mt + σw(t)).
Proof
By (3.2)
S(t) = S(nτ) = S(nτ −τ)ek(n)
= S(nτ −2τ)ek(n−1)+k(n)
= · · · = S(0)ek(1)+···+k(n)
= S(0)emnτ+σ(ξ(1)+···+ξ(n))
= S(0)emt+σw(t),
as required.

68
Mathematics for Finance
In order to pass to the continuous-time limit we use the approximation
ex ≈1 + x + 1
2x2,
accurate for small values of x, to obtain
S(nτ + τ)
S(nτ)
= ek(n+1) ≈1 + k(n + 1) + 1
2k(n + 1)2.
Then, we compute
k(n + 1)2 = (mτ + σξ(n + 1))2 = σ2τ + · · · ,
where the dots represent all terms with powers of τ higher than 1, which will
be omitted because they are much smaller than the leading term whenever τ
is small. Next,
S(nτ + τ)
S(nτ)
≈1 + mτ + σξ(n + 1) + 1
2σ2τ
= 1 +
	
m + 1
2σ2

τ + σξ(n + 1),
and so
S(nτ + τ) −S(nτ) ≈
	
m + 1
2σ2

S(nτ)τ + σS(nτ)ξ(n + 1).
Since ξ(n + 1) = w(nτ + τ) −w(nτ), we obtain an approximate equation
describing the dynamics of stock prices:
S(t + τ) −S(t) ≈
	
m + 1
2σ2

S(t)τ + σS(t)(w(t + τ) −w(t)),
(3.8)
where t = nτ. The solution S(t) of this approximate equation is given by the
same formula as in Proposition 3.7.
For any N = 1, 2, . . . we consider a binomial tree model with time step of
length τ =
1
N . Let SN(t) be the corresponding stock prices and let wN(t) be
the corresponding symmetric random walk with increments ξN(t) = wN(t) −
wN(t −1
N ), where t = n
N is the time after n steps.
Exercise 3.25
Compute the expectation and variance of wN(t), where t = n
N .

3. Risky Assets
69
We shall use the Central Limit Theorem2 to obtain the limit as N →∞of
the random walk wN(t). To this end we put
x(n) = k(n) −mτ
σ√τ
for each n = 1, 2, . . . , which is a sequence of independent identically distributed
random variables, each with expectation 0 and variance 1. The Central Limit
Theorem implies that
x(1) + x(2) + · · · + x(n)
√n
→X
in distribution as n →∞, where X is a random variable with standard normal
distribution (mean 0 and variance 1).
Let us fix any t > 0. Because the random walk wN is only defined at discrete
times being whole multiples of the step τ = 1
N , we consider wN(tN), where tN
is the whole multiple of
1
N nearest to t. Then, clearly, NtN is a whole number
for each N, and we can write
wN(tN) = √tN
x(1) + x(2) + · · · + x(NtN)
√NtN
.
As N →∞, we have tN →t and NtN →∞, so that
wN(tN) →W(t)
in distribution, where W(t) =
√
tX. The last equality means that W(t) is
normally distributed with mean 0 and variance t.
This argument, based on the Central Limit Theorem, works for any single
fixed time t > 0. It is possible to extend the result to obtain a limit for all
times t ≥0 simultaneously, but this is beyond the scope of this book. The limit
W(t) is called the Wiener process (or Brownian motion). It inherits many of
the properties of the random walk, for example:
1. W(0) = 0, which corresponds to wN(0) = 0.
2. E(W(t)) = 0, corresponding to E(wN(t)) = 0 (see the solution of Exer-
cise 3.25).
3. Var(W(t)) = t, with the discrete counterpart Var(wN(t)) = t (see the solu-
tion of Exercise 3.25).
4. The increments W(t3)−W(t2) and W(t2)−W(t1) are independent for 0 ≤
t1 ≤t2 ≤t3; so are the increments wN(t3) −wN(t2) and wN(t2) −wN(t1).
2 See, for example, Capi´nski and Zastawniak (2001).

70
Mathematics for Finance
5. W(t) has a normal distribution with mean 0 and variance t, that is, with
density
1
√
2πte−x2
2t . This is related to the distribution of wN(t). The latter is
not normal, but approaches the normal distribution in the limit according
to the Central Limit Theorem.
An important difference between W(t) and wN(t) is that W(t) is defined for
all t ≥0, whereas the time in wN(t) is discrete, t = n/N for n = 0, 1, 2, . . . .
The price process obtained in the limit from SN(t) as N →∞will be
denoted by S(t). While SN(t) satisfies the approximate equation (3.8) with the
appropriate substitutions, namely
SN(t + 1
N ) −SN(t) ≈
	
m + 1
2σ2

SN(t) 1
N + σSN(t)(wN(t + 1
N ) −wN(t)),
the continuous-time stock prices S(t) satisfy an equation of the form
dS(t) =
	
m + 1
2σ2

S(t)dt + σS(t)dW(t).
(3.9)
Here dS(t) = S(t+dt)−S(t) and dW(t) = W(t+dt)−W(t) are the increments
of S(t) and W(t) over an infinitesimal time interval dt. The explicit formulae
for the solutions are also similar,
SN(t) = SN(0) exp(mt + σwN(t))
in the discrete case, whereas
S(t) = S(0) exp(mt + σW(t))
in the continuous case.
Figure 3.11
Density of the distribution of S(10)
Since W(t) has a normal distribution with mean 0 and variance t, it follows
that ln S(t) has a normal distribution with mean ln S(0)+mt and variance σ2t.
Because of this it is said that the continuous-time price process S(t) has the log

3. Risky Assets
71
normal distribution. The number σ is called the volatility of the price S(t). The
density of the distribution of S(t) is shown in Figure 3.11 for t = 10, S(0) = 1,
m = 0 and σ = 0.1. This can be compared with the discrete distribution in
Figure 3.2.
Remark 3.6
Equation (3.9) and the increments dS(t), dW(t) and dt are introduced above
only informally by analogy with the discrete case. They can be given a pre-
cise status in Stochastic Calculus, a theory with fundamental applications in
advanced mathematical finance. In particular, (3.9) is an example of what is
known as a stochastic differential equation.

This page intentionally left blank 

4
Discrete Time Market Models
Having discussed a number of different models of stock price dynamics, we
shall now generalise and pursue a little further some of the ideas introduced in
Chapter 1. In particular, we shall reformulate and extend the general notions
and assumptions underlying mathematical finance already mentioned in that
chapter.
As in Chapter 3, we assume that time runs in steps of fixed length τ. For
many time-dependent quantities we shall simplify the notation by writing n in
place of the time t = nτ of the nth step.
4.1 Stock and Money Market Models
Suppose that m risky assets are traded. These will be referred to as stocks. Their
prices at time n = 0, 1, 2, . . . are denoted by S1(n), . . . , Sm(n). In addition,
investors have at their disposal a risk-free asset, that is, an investment in the
money market. Unless stated otherwise, we take the initial level of the risk-
free investment to be one unit of the home currency, A(0) = 1. However, in
some numerical examples and exercises we shall often take A(0) = 100 for
convenience. Because the money market account can be manufactured using
bonds (see Chapter 2), we shall frequently refer to a risk-free investment as a
position in bonds, finding it convenient to think of A(n) as the bond price at
time n.
The risky positions in assets number 1, . . . , m will be denoted by x1, . . . , xm,
73


## Discrete-Time Market Models

74
Mathematics for Finance
respectively, and the risk-free position by y. The wealth of an investor holding
such positions at time n will be
V (n) =
m

j=1
xjSj(n) + yA(n).
(4.1)
Assumptions 1.1 to 1.5 of Chapter 1 can readily be adapted to this general
setting. The motivation and interpretation of these assumptions are the same
as in Chapter 1, with the natural changes from one to several time steps and
from one to several risky assets.
Assumption 4.1 (Randomness)
The future stock prices S1(n), . . . , Sm(n) are random variables for any n =
1, 2, . . . . The future prices A(n) of the risk-free security for any n = 1, 2, . . . are
known numbers.
Assumption 4.2 (Positivity of Prices)
All stock and bond prices are strictly positive,
S(n) > 0
and
A(n) > 0
for n = 0, 1, 2, . . . .
Assumption 4.3 (Divisibility, Liquidity and Short Selling)
An investor may buy, sell and hold any number xk of stock shares of each kind
k = 1, . . . , m and take any risk-free position y, whether integer or fractional,
negative, positive or zero. In general,
x1, . . . , xm, y ∈R.
Assumption 4.4 (Solvency)
The wealth of an investor must be non-negative at all times,
V (n) ≥0
for n = 0, 1, 2, . . . .
Assumption 4.5 (Discrete Unit Prices)
For each n = 0, 1, 2, . . . the share prices S1(n), . . . , Sm(n) are random variables
taking only finitely many values.

4. Discrete Time Market Models
75
4.1.1 Investment Strategies
The positions held by an investor in the risky and risk-free assets can be altered
at any time step by selling some assets and investing the proceeds in other
assets. In real life cash can be taken out of the portfolio for consumption or
injected from other sources. Nevertheless, we shall assume that no consumption
or injection of funds takes place in our models to keep things as simple as
possible.
Decisions made by any investor of when to alter his or her portfolio and
how many assets to buy or sell are based on the information currently available.
We are going to exclude the unlikely possibility that investors could foresee the
future, as well as the somewhat more likely (but illegal) one that they will
act on insider information. However, all the historical information about the
market up to and including the time instant when a particular trading decision
is executed will be freely available.
Example 4.1
Let m = 2 and suppose that
S1(0) = 60,
S1(1) = 65,
S1(2) = 75,
S2(0) = 20,
S2(1) = 15,
S2(2) = 25,
A(0) = 100,
A(1) = 110,
A(2) = 121,
in a certain market scenario. At time 0 initial wealth V (0) = 3, 000 dollars is
invested in a portfolio consisting of x1(1) = 20 shares of stock number one,
x2(1) = 65 shares of stock number two, and y(1) = 5 bonds. Our notational
convention is to use 1 rather than 0 as the argument in x1(1), x2(1) and y(1) to
reflect the fact that this portfolio will be held over the first time step. At time 1
this portfolio will be worth V (1) = 20 × 65 + 65 × 15 + 5 × 110 = 2, 825 dollars.
At that time the number of assets can be altered by buying or selling some of
them, as long as the total value remains $2, 825. For example, we could form a
new portfolio consisting of x1(2) = 15 shares of stock one, x2(2) = 94 shares of
stock two, and y(2) = 4 bonds, which will be held during the second time step.
The value of this portfolio will be V (2) = 15 × 75 + 94 × 25 + 4 × 121 = 3, 959
dollars at time 2, when the positions in stocks and bonds can be adjusted once
again, as long as the total value remains $3, 959, and so on. However, if no
adjustments are made to the original portfolio, then it will be worth $2, 825 at
time 1 and $3, 730 at time 2.

76
Mathematics for Finance
Definition 4.1
A portfolio is a vector (x1(n), . . . , xm(n), y(n)) indicating the number of shares
and bonds held by an investor between times n −1 and n. A sequence of
portfolios indexed by n = 1, 2, . . . is called an investment strategy. The wealth
of an investor or the value of the strategy at time n ≥1 is
V (n) =
m

j=1
xj(n)Sj(n) + y(n)A(n).
At time n = 0 the initial wealth is given by
V (0) =
m

j=1
xj(1)Sj(0) + y(1)A(0).
We have seen in Example 4.1 that the contents of a portfolio can be adjusted
by buying or selling some assets at any time step, as long as the current value
of the portfolio remains unaltered.
Definition 4.2
An investment strategy is called self-financing if the portfolio constructed at
time n ≥1 to be held over the next time step n + 1 is financed entirely by the
current wealth V (n), that is,
m

j=1
xj(n + 1)Sj(n) + y(n + 1)A(n) = V (n).
(4.2)
Example 4.2
Let the stock and bond prices be as in Example 4.1. Suppose that an initial
wealth of V (0) = 3, 000 dollars is invested by purchasing x1(1) = 18.22 shares
of the first stock, short selling x2(1) = −16.81 shares of the second stock,
and buying y(1) = 22.43 bonds. The time 1 value of this portfolio will be
V (1) = 18.22 × 65 −16.81 × 15 + 22.43 × 110 = 3, 399.45 dollars. The investor
will benefit from the drop of the price of the shorted stock. This example
illustrates the fact that portfolios containing fractional or negative numbers of
assets are allowed.
We do not impose any restrictions on the numbers x1(n), . . . , xm(n), y(n).
The fact that they can take non-integer values is referred to as divisibility.
Negative xj(n) means that stock number j is sold short (in other words, a

4. Discrete Time Market Models
77
short position is taken in stock j), negative y(n) corresponds to borrowing
cash (taking a short position in the money market, for example, by issuing and
selling a bond). The absence of any bounds on the size of these numbers means
that the market is liquid, that is, any number of assets of each type can be
purchased or sold at any time.
In practice some security measures to control short selling may be imple-
mented by stock exchanges. Typically, investors are required to pay a certain
percentage of the short sale as a security deposit to cover possible losses. If their
losses exceed the deposit, the position must be closed. The deposit creates a
burden on the portfolio, particularly if it earns no interest for the investor.
However, restrictions of this kind may not concern dealers who work for ma-
jor financial institutions holding large numbers of shares deposited by smaller
investors. These shares may be borrowed internally in lieu of short selling.
Example 4.3
We continue assuming that stock prices follow the scenario in Example 4.1.
Suppose that 20 shares of the first stock are sold short, x1(1) = −20. The
investor will receive 20 × 60 = 1, 200 dollars in cash, but has to pay a security
deposit of, say 50%, that is, $600. One time step later she will suffer a loss
of 20 × 65 −1, 200 = 100 dollars. This is subtracted from the deposit and
the position can be closed by withdrawing the balance of 600 −100 = 400
dollars. On the other hand, if 60 shares of the second stock are shorted, that is,
x2(1) = −60, then the investor will make a profit of 1, 200−60×15 = 300 dollars
after one time step. The position can be closed with final wealth 600+300 = 900
dollars. In both cases the final balance should be reduced by 600 × 0.1 = 60
dollars, the interest that would have been earned on the amount deposited, had
it been invested in the money market.
An investor constructing a portfolio at time n has no knowledge of future
stock prices. In particular, no insider dealing is allowed. Investment decisions
can be based only on the performance of the market to date. This is reflected
in the following definition.
Definition 4.3
An investment strategy is called predictable if for each n = 0, 1, 2, . . . the port-
folio (x1(n + 1), . . . , xm(n + 1), y(n + 1)) constructed at time n depends only
on the nodes of the tree of market scenarios reached up to and including time n.
The next proposition shows that the position taken in the risk-free asset is

78
Mathematics for Finance
always determined by the current wealth and the positions in risky assets.
Proposition 4.1
Given the initial wealth V (0) and a predictable sequence (x1(n), . . . , xm(n)),
n = 1, 2, . . . of positions in risky assets, it is always possible to find a sequence
y(n) of risk-free positions such that (x1(n), . . . , xm(n), y(n)) is a predictable
self-financing investment strategy.
Proof
Put
y(1) = V (0) −x1(1)S1(0) −· · · −xm(1)Sm(0)
A(0)
and then compute
V (1) = x1(1)S1(1) + · · · + xm(1)Sm(1) + y(1)A(1).
Next,
y(2) = V (1) −x1(2)S1(1) −· · · −xm(2)Sm(1)
A(1)
,
V (2) = x1(2)S1(2) + · · · + xm(2)Sm(2) + y(2)A(2),
and so on. This clearly defines a self-financing strategy. The strategy is pre-
dictable because y(n + 1) can be expressed in terms of stock and bond prices
up to time n.
Exercise 4.1
Find the number of bonds y(1) and y(2) held by an investor during the
first and second steps of a predictable self-financing investment strategy
with initial value V (0) = 200 dollars and risky asset positions
x1(1) = 35.24,
x1(2) = −40.50,
x2(1) = 24.18,
x2(2) =
10.13,
if the prices of assets follow the scenario in Example 4.1. Also find the
time 1 value V (1) and time 2 value V (2) of this strategy.
Example 4.4
Once again, suppose that the stock and bond prices follow the scenario in
Example 4.1. If an amount V (0) = 100 dollars were invested in a portfolio with

4. Discrete Time Market Models
79
x1(1) = −12, x2(1) = 31 and y(1) = 2, then it would lead to insolvency, since
the time 1 value of this portfolio is negative, V (1) = −12×65+31×15+2×110 =
−95 dollars .
Such a portfolio, which is excluded by Assumption 4.4, would be impossible
to construct in practice. No short position will be allowed unless it can be
closed at any time and in any scenario (if necessary, by selling other assets in
the portfolio to raise cash). This means that the wealth of an investor must be
non-negative at all times.
Definition 4.4
A strategy is called admissible if it is self-financing, predictable, and for each
n = 0, 1, 2, . . .
V (n) ≥0
with probability 1.
Exercise 4.2
Consider a market consisting of one risk-free asset with A(0) = 10 and
A(1) = 11 dollars, and one risky asset such that S(0) = 10 and S(1) =
13 or 9 dollars. On the x, y plane draw the set of all portfolios (x, y)
such that the one-step strategy involving risky position x and risk-free
position y is admissible.
4.1.2 The Principle of No Arbitrage
We are ready to formulate the fundamental principle underlying all mathe-
matical models in finance. It generalises the simplified one-step version of the
No-Arbitrage Principle in Chapter 1 to models with several time steps and
several risky assets. Whereas the notion of a portfolio is sufficient to state the
one-step version, in the general setting we need to use a sequence of portfolios
forming an admissible investment strategy. This is because investors can adjust
their positions at each time step.
Assumption 4.6 (No-Arbitrage Principle)
There is no admissible strategy such that V (0) = 0 and V (n) > 0 with positive
probability for some n = 1, 2, . . . .

80
Mathematics for Finance
Exercise 4.3
Show that the No-Arbitrage Principle would be violated if there was a
self-financing predictable strategy with initial value V (0) = 0 and final
value 0 ̸= V (2) ≥0, such that V (1) < 0 with positive probability.
The strategy in Exercise 4.3 clearly violates the solvency assumption (As-
sumption 4.4), since V (1) may be negative. In fact, this assumption is not essen-
tial for the formulation of the No-Arbitrage Principle. An admissible strategy
realising an arbitrage opportunity can be found whenever there is a predictable
self-financing strategy (possibly violating Assumption 4.4) such that V (0) = 0
and 0 ̸= V (n) ≥0 for some n > 0.
Exercise 4.4
Consider a market with one risk-free asset and one risky asset that follows
the binomial tree model. Suppose that whenever stock goes up, you
can predict that it will go down at the next step. Find a self-financing
(but not necessarily predictable) strategy with V (0) = 0, V (1) ≥0 and
0 ̸= V (2) ≥0.
This exercise indicates that predictability is an essential assumption in the
No-Arbitrage Principle. An investor who could foresee the future behaviour of
stock prices (here, if stock goes down at one step, you can predict what it will
do at the next step) would always be able to find a suitable investment strategy
to ensure a risk-free profit.
Exercise 4.5
Consider a market with a risk-free asset such that A(0) = 100, A(1) =
110, A(2) = 121 dollars and a risky asset, the price of which can follow
three possible scenarios,
Scenario
S(0)
S(1)
S(2)
ω1
100
120
144
ω2
100
120
96
ω3
100
90
96
Is there an arbitrage opportunity if a) there are no restrictions on short
selling, and b) no short selling of the risky asset is allowed?

4. Discrete Time Market Models
81
Exercise 4.6
Given the bond and stock prices in Exercise 4.5, is there an arbitrage
strategy if short selling of stock is allowed, but the number of units of
each asset in a portfolio must be an integer?
Exercise 4.7
Given the bond and stock prices in Exercise 4.5, is there an arbitrage
strategy if short selling of stock is allowed, but transaction costs of 5%
of the transaction volume apply whenever stock is traded.
4.1.3 Application to the Binomial Tree Model
We shall see that in the binomial tree model with several time steps Condi-
tion 3.2 is equivalent to the lack of arbitrage.
Proposition 4.2
The binomial tree model admits no arbitrage if and only if d < r < u.
Proof
We shall begin with a one-step binomial tree. This will then be used as a
building block in the case of several time steps.
One step. Suppose that r ≤d. If so, then:
• Borrow 1 dollar at the risk-free rate.
• Buy 1/S(0) shares.
That is to say, construct a portfolio with x = 1/S(0) and y = −1, the value
of which is V (0) = 0. After one step, either S(1) = S(0)(1 + d) and V (1) =
−r +d ≥0, or S(1) = S(0)(1+u) and V (1) = −r +u > 0, leading to arbitrage.
Suppose that u ≤r. In this case:
• Buy one bond.
• Sell short 1/S(0) shares.
The resulting portfolio with x = −1/S(0) and y = 1 will once again have initial
value V (0) = 0. After one step this portfolio will be worth V (1) = r −u ≥0 if
the stock price goes up, or V (1) = r −d > 0 if it goes down, also realising an
arbitrage opportunity.
Finally, suppose that d < r < u. Every portfolio with V (0) = 0 must be
of the form x = a/S(0) and y = −a for some real number a. Consider the

82
Mathematics for Finance
following three cases:
1) a = 0 (a trivial portfolio consisting of no cash and no stock). Then V (1) = 0
identically.
2) a > 0 (a cash loan invested in stock). Then V (1) = a(d −r) < 0 if the price
of stock goes down.
3) a < 0 (a long position in bonds financed by shorting stock). In this case
V (1) = a(u −r) < 0 if stock goes up.
Arbitrage is clearly impossible when d < r < u.
The above argument shows that d < r < u if and only if there is no arbitrage
in the one-step case.
Several steps. Let d < r < u and suppose there is an arbitrage strategy.
The tree of stock prices can be considered as a collection of one-step subtrees,
as in Figure 4.1. By taking the smallest n for which V (n) ̸= 0, we can find a
one-step subtree with V (n −1) = 0 at its root and V (n) ≥0 at each node
growing out of this root, with V (n) > 0 at one or more of these nodes. By the
one-step case this is impossible if d < r < u, leading to a contradiction.
Figure 4.1
One-step subtrees in a two-step binomial model
Conversely, suppose that there is no arbitrage in the binomial tree model
with several steps. Then for any strategy such that V (0) = 0 it follows that
V (n) = 0 for any n and, in particular, V (1) = 0. This implies that d < r < u
by the above argument in the one-step case.
We shall conclude this chapter with a brief discussion of a fundamental re-
lationship between the risk-neutral probability and the No-Arbitrage Principle.
First, we observe that the lack of arbitrage is equivalent to the existence of a
risk-neutral probability in the binomial tree model.
Proposition 4.3
The binomial tree model admits no arbitrage if and only if there exists a risk-
neutral probability p∗such that 0 < p∗< 1.

4. Discrete Time Market Models
83
Proof
This is an immediate consequence of Exercise 3.18 and Proposition 4.2.
4.1.4 Fundamental Theorem of Asset Pricing
In this section, which can be omitted on first reading, we return to the general
setting under Assumptions 4.1 to 4.5.
We already know that the discounted stock prices in the binomial tree model
form a martingale under the risk-neutral probability, see Proposition 3.5 and
Corollary 3.6. The following result extends these observations to any discrete
model.
Theorem 4.4 (Fundamental Theorem of Asset Pricing)
The No-Arbitrage Principle is equivalent to the existence of a probability P∗
on the set of scenarios Ωsuch that P∗(ω) > 0 for each scenario ω ∈Ωand the
discounted stock prices Sj(n) = Sj(n)/A(n) satisfy
E∗(Sj(n + 1)|S(n)) = Sj(n)
(4.3)
for any j = 1, . . . , m and n = 0, 1, 2, . . . , where E∗( · |S(n)) denotes the
conditional expectation with respect to probability P∗computed once the stock
price S(n) becomes known at time n.
The proof of the Fundamental Theorem of Asset Pricing is quite technical
and will be omitted.
Definition 4.5
A sequence of random variables X(0), X(1), X(2), . . . such that
E∗(X(n + 1)|S(n)) = X(n)
for each n = 0, 1, 2, . . . is said to be a martingale with respect to P∗.
Condition (4.3) can be expressed by saying that the discounted stock prices
Sj(0), Sj(1), Sj(2), . . . form a martingale with respect to P∗. The latter is called
a risk-neutral or martingale probability on the set of scenarios Ω. Moreover, E∗
is called a risk-neutral or martingale expectation.

84
Mathematics for Finance
Example 4.5
Let A(0) = 100, A(1) = 110, A(2) = 121 and suppose that stock prices can
follow four possible scenarios:
Scenario
S(0)
S(1)
S(2)
ω1
90
100
112
ω2
90
100
106
ω3
90
80
90
ω4
90
80
80
The tree of stock prices is shown in Figure 4.2. The risk-neutral probability P∗
is represented by the branching probabilities p∗, q∗, r∗at each node. Condition
Figure 4.2
Tree of stock prices in Example 4.5
(4.3) for S(n) = S(n)/A(n) can be written in the form of three equations, one
for each node of the tree,
100
110p∗+ 80
110(1 −p∗) = 90
100,
112
121q∗+ 106
121(1 −q∗) = 100
110,
90
121r∗+ 80
121(1 −r∗) = 80
110.
These can be solved to find
p∗= 19
20,
q∗= 2
3,
r∗= 4
5.
For each scenario (each path through the tree) the corresponding risk-neutral
probability can be computed as follows:
P∗(ω1) = p∗q∗= 19
20 × 2
3 = 19
30,
P∗(ω2) = p∗(1 −q∗) = 19
20 ×
	
1 −2
3

= 19
60,
P∗(ω3) = (1 −p∗)r∗=
	
1 −19
20

× 4
5 = 1
25,
P∗(ω4) = (1 −p∗)(1 −r∗) =
	
1 −19
20

×
	
1 −4
5

=
1
100.

4. Discrete Time Market Models
85
By Theorem 4.4 the existence of a risk-neutral probability implies that there
is no arbitrage.
4.2 Extended Models
Securities such as stock, which are traded independently of other assets, are
called primary securities. By contrast, derivative securities such as, for exam-
ple, options or forwards (in Chapter 1 we have seen some simple examples of
these) are legal contracts conferring certain financial rights or obligations upon
the holder, contingent on the prices of other securities, referred to as the un-
derlying securities. An underlying security may be a primary security, as for a
forward contract on stock, but it may also be a derivative security, as in the
case of an option on futures. A derivative security cannot exist in its own right,
unless the underlying security or securities are traded. Derivative securities are
also referred to as contingent claims because their value is contingent on the
underlying securities.
For example, the holder of a long forward contract on a stock is committed
to buying the stock for the forward price at a specified time of delivery, no
matter how much the actual stock price turns out to be at that time. The
value of the forward position is contingent on the stock. It will become positive
if the market price of stock turns out to be higher than the forward price on
delivery. If the stock price turns out to be lower than the forward price, then
the value of the forward position will be negative.
Remark 4.1
The assumptions in Section 4.1, including the No-Arbitrage Principle, are
stated for strategies consisting of primary securities only, such as stocks and
bonds (or the money market account). Nevertheless, in many texts they are
invoked in arbitrage proofs involving strategies constructed out of derivative
securities in addition to stocks and bonds. To avoid this inaccuracy the as-
sumptions need to be extended to strategies consisting of both primary and
derivative securities.
The setting of Section 4.1, involving portfolios of risky stocks and the money
market account, will be extended to include risky securities of various other
kinds in addition to (and sometimes in place of) stock. In particular, to cover
real-life situations we need to include derivative securities such as forwards or
options, but also primary securities such as bonds of various maturities, the

86
Mathematics for Finance
future prices of which may be random (except, of course, at maturity). We
shall also relax the assumption that an investment in a money market account
should be risk-free, with a view towards modelling random interest rates. In
this way we prepare the stage for a detailed study of derivative securities in
Chapters 6, 7 and 8, and random bond prices and the term structure of interest
rates in Chapters 10 and 11.
Securities of various kinds will be treated on a similar footing as stock in
Section 4.1. We shall denote by S1(n), . . . , Sm(n) the time n prices of m dif-
ferent primary securities, typically m different stocks, though they may also
include other assets such as foreign currency, commodities or bonds of vari-
ous maturities. Moreover, the price of one distinguished primary security, the
money market account, will be denoted by A(n). In addition, we introduce k
different derivative securities such as forwards, call and put options, or indeed
any other contingent claims, whose time n market prices will be denoted by
D1(n), . . . , Dk(n).
As opposed to stocks and bonds, we can no longer insist that the prices of all
derivative securities should be positive. For example, at the time of exchanging
a forward contract its value is zero, which may and often does become negative
later on because the holder of a long forward position may have to buy the
stock above its market price at delivery. The future prices S1(n), . . . , Sm(n) and
A(n) of primary securities and the future prices D1(n), . . . , Dk(n) of derivative
securities may be random for n = 1, 2, . . . , but we do not rule out the possibility
that some of them, such as the prices of bonds at maturity, may in fact be
known in advance, being represented by constant random variables or simply
real numbers. All the current prices S1(0), . . . , Sm(0), A(0), D1(0), . . . , Dk(0)
are of course known at time 0, that is, are also just real numbers.
The positions in primary securities, including the money market account,
will be denoted by x1, . . . , xm and y, and those in derivative securities by
z1, . . . , zk, respectively. The wealth of an investor holding such positions at
time n will be
V (n) =
m

j=1
xjSj(n) + yA(n) +
k

i=1
ziDi(n),
which extends formula (4.1).
The assumptions in Section 4.1 need to be replaced by the following.
Assumption 4.1a (Randomness)
The asset prices S1(n), . . . , Sm(n), A(n), D1(n), . . . , Dk(n) are random vari-
ables for any n = 1, 2, . . . .

4. Discrete Time Market Models
87
Assumption 4.2a (Positivity of Prices)
The prices of primary securities, including the money market account, are pos-
itive,
S1(n), . . . , Sm(n), A(n) > 0
for n = 0, 1, 2, . . . .
Assumption 4.3a (Divisibility, Liquidity and Short Selling)
An investor may buy, sell and hold any number of assets, whether integer or
fractional, negative, positive or zero. In general,
x1, . . . , xm, y, z1, . . . , zk ∈R.
Assumption 4.4a (Solvency)
The wealth of an investor must be non-negative at all times,
V (n) ≥0
for n = 0, 1, 2, . . . .
Assumption 4.5a (Discrete Unit Prices)
For each n = 0, 1, 2, . . . the prices S1(n), . . . , Sm(n), A(n), D1(n), . . . , Dk(n) are
random variables taking only finitely many values.
Definitions 4.1 to 4.4 also extend immediately to the case in hand.
Definition 4.1a
A portfolio is a vector
(x1(n), . . . , xm(n), y(n), z1(n), . . . , zk(n))
indicating the number of primary and derivative securities held by an investor
between times n −1 and n. A sequence of portfolios indexed by n = 1, 2, . . .
is called an investment strategy. The wealth of an investor or the value of the
strategy at time n ≥1 is
V (n) =
m

j=1
xj(n)Sj(n) + y(n)A(n) +
k

i=1
zi(n)Di(n).
At time n = 0 the initial wealth is given by
V (0) =
m

j=1
xj(1)Sj(0) + y(1)A(0) +
k

i=1
zi(1)Di(0).

88
Mathematics for Finance
Definition 4.2a
An investment strategy is called self-financing if the portfolio constructed at
time n ≥1 to be held over the next time step n + 1 is financed entirely by the
current wealth V (n), that is,
m

j=1
xj(n + 1)Sj(n) + y(n + 1)A(n) +
k

i=1
zi(n + 1)Di(n) = V (n).
Definition 4.3a
An investment strategy is called predictable if for each n = 0, 1, 2, . . . the port-
folio
(x1(n + 1), . . . , xm(n + 1), y(n + 1), z1(n + 1), . . . , zk(n + 1))
constructed at time n depends only on the nodes of the tree of market scenarios
reached up to and including time n.
Definition 4.4a
A strategy is called admissible if it is self-financing, predictable, and for each
n = 0, 1, 2, . . .
V (n) ≥0
with probability 1.
The No-Arbitrage Principle extends without any modifications.
Assumption 4.6a (No-Arbitrage Principle)
There is no admissible strategy such that V (0) = 0 and V (n) > 0 with positive
probability for some n = 1, 2, . . . .
Finally, the Fundamental Theorem of Asset Pricing takes the following form.
Theorem 4.4a (Fundamental Theorem of Asset Pricing)
The No-Arbitrage Principle is equivalent to the existence of a probability P∗
on the set of scenarios Ωsuch that P∗(ω) > 0 for each scenario ω ∈Ωand the
discounted prices of primary and derivative securities Sj(n) = Sj(n)/A(n) and
Di(n) = Di(n)/A(n) form martingales with respect to P∗, that is, satisfy
E∗(Sj(n + 1)|S(n)) = Sj(n),
E∗( Di(n + 1)|S(n)) = Di(n)

4. Discrete Time Market Models
89
for any j = 1, . . . , m, any i = 1, . . . , k and any n = 0, 1, 2, . . . , where E∗( · |S(n))
denotes the conditional expectation with respect to probability P∗computed
once the stock price S(n) becomes known at time n.
Example 4.6
We shall use the same scenarios ω1, ω2, ω3, ω4, stock prices S(0), S(1), S(2)
and money market prices A(0), A(1), A(2) as in Example 4.5. In addition, we
consider a European call option giving the holder the right (but no obligation)
to buy the stock for the strike price of X = 85 dollars at time 2.
In this situation we need to consider an extended model with three assets,
the stock, the money market, and the option, with unit prices S(n), A(n), CE(n),
respectively, where CE(n) is the market price of the option at time n = 0, 1, 2.
The time 2 option price is determined by the strike price and the stock
price,
CE(2) = max{S(2) −X, 0}.
The prices CE(0) and CE(1) can be found using the Fundamental Theorem
of Asset Pricing. (Which explains the name of the theorem!) According to the
theorem, there is a probability P∗such that the discounted stock and option
prices S(n) = S(n)/A(n) and CE(n) = CE(n)/A(n) are martingales, or else
an arbitrage opportunity would exist. However, there is only one probability
P∗turning S(n) into a martingale, namely that found in Example 4.5. As a
result, CE(n) must be a martingale with respect to the same probability P∗.
This gives
CE(1) = A(1)
A(2)E∗(CE(2)|S(1))
and
CE(0) = A(0)
A(1)E∗(CE(1)).
The values of P∗for each scenario found in Example 4.5 can now be used to
compute CE(1) and then CE(0). For example,
CE(1, ω1) = CE(1, ω2) = A(1)
A(2)
P∗(ω1)CE(2, ω1) + P∗(ω2)CE(2, ω2)
P∗(ω1) + P∗(ω2)
= 110
121
19
30 × 27 + 19
60 × 21
19
30 + 19
60
∼= 22.73
dollars. Proceeding in a similar way, we obtain
Scenario
CE(0)
CE(1)
CE(2)
ω1
19.79
22.73
27.00
ω2
19.79
22.73
21.00
ω3
19.79
3.64
5.00
ω4
19.79
3.64
0.00

90
Mathematics for Finance
Exercise 4.8
Apply the Fundamental Theorem of Asset Pricing to find the time 0
and 1 prices of a put option with strike price $110 maturing after two
steps, given the same scenarios ω1, ω2, ω3, ω4, stock prices S(0), S(1), S(2)
and money market prices A(0), A(1), A(2) as in Example 4.5.

5
Portfolio Management
An investment in a risky security always carries the burden of possible losses
or poor performance. In this chapter we analyse the advantages of spreading
the investment among several securities. Even though the mathematical tools
involved are quite simple, they lead to formidable results.
5.1 Risk
First of all, we need to identify a suitable quantity to measure risk. An invest-
ment in bonds returning, for example, 8% at maturity is free of risk, in which
case the measure of risk should be equal to zero. If the return on an investment
is, say 11% or 13%, depending on the market scenario, then the risk is clearly
smaller as compared with an investment returning 2% or 22%, respectively.
However, the spread of return values can hardly be used to measure risk be-
cause it ignores the probabilities. If the return rate is 22% with probability 0.99
and 2% with probability 0.01, the risk can be considered quite small, whereas
the same rates of return occurring with probability 0.5 each would indicate a
rather more risky investment. The desired quantity needs to capture the follow-
ing two aspects of risk: 1) the distances between a certain reference value and
the rates of return in each market scenario and 2) the probabilities of different
scenarios.
The return K on a risky investment is a random variable. It is natural to
take the expectation E(K) as the reference value. The variance Var(K) turns
91

