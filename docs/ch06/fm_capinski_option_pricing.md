# Option Pricing & Financial Engineering

!!! info "Source"
    **Mathematics for Finance: An Introduction to Financial Engineering** by Marek Capinski and Tomasz Zastawniak, Springer, 2003.
    These notes are used for educational purposes.

## General Theory of Options

152
Mathematics for Finance
lying stock is $20.37 and the interest rate is 7.48%. Find an arbitrage
opportunity.
Remark 7.1
We can make a simple but powerful observation based on Theorem 7.1: The
prices of European calls and puts depend in the same way on any variables
absent in the put-call parity relation (7.1). In other words, the difference of
these prices does not depend on such variables. As an example, consider the
expected return on stock
If the price of a call should grow along with the
expected return, which on first sight seems consistent with intuition because
higher stock prices mean higher payoffs on calls, then the price of a put would
also grow. The latter, however, contradicts common sense because higher stock
prices mean lower payoffs on puts. Because of this, one could argue that put
and call prices should be independent of the expected return on stock. We shall
see that this is indeed the case once the Black–Scholes formula is derived for
call and put options in Chapter 8.
Following the argument presented at the beginning of this section, we can
reformulate put-call parity as follows:
CE −P E = VX(0),
(7.4)
where VX(0) is the value of a long forward contract, see (6.10). Note that if X
is equal to the theoretical forward price S(0)erT of the asset, then the value of
the forward contract is zero, VX(0) = 0, and so CE = P E. Formula (7.4) allows
us to generalise put-call parity by drawing on the relationships established in
Remark 6.3. Namely, if the stock pays a dividend between times 0 and T, then
VX(0) = S(0) −div0 −Xe−rT , where div0 is the present value of the dividend.
It follows that
CE −P E = S(0) −div0 −Xe−rT .
(7.5)
If dividends are paid continuously at a rate rdiv, then VX(0) = S(0)e−rdivT −
Xe−rT , so
CE −P E = S(0)e−rdivT −Xe−rT .
(7.6)
Exercise 7.5
Outline an arbitrage proof of (7.5).
Exercise 7.6
Outline an arbitrage proof of (7.6).

7. Options: General Properties
153
Exercise 7.7
For the data in Exercise 6.5, find the strike price for European calls and
puts to be exercised in six months such that CE = P E.
For American options put-call parity gives only an estimate, rather than a
strict equality involving put and call prices.
Theorem 7.2 (Put-Call Parity Estimates)
The prices of American put and call options with the same strike price X and
expiry time T on a stock that pays no dividends satisfy
S(0) −Xe−rT ≥CA −P A ≥S(0) −X.
Proof
Suppose that the first inequality fails to hold, that is,
CA −P A −S(0) + Xe−rT > 0.
Then we can write and sell a call, and buy a put and a share, financing the
transactions on the money market. If the holder of the American call chooses
to exercise it at time t ≤T, then we shall receive X for the share and settle
the money market position, ending up with the put and a positive amount
X + (CA −P A −S(0))ert = (Xe−rt + CA −P A −S(0))ert
≥(Xe−rT + CA −P A −S(0))ert > 0.
If the call option is not exercised at all, we can sell the share for X by exercising
the put at time T and close the money market position, also ending up with a
positive amount
X + (CA −P A −S(0))erT > 0.
Now suppose that
CA −P A −S(0) + X < 0.
In this case we can write and sell a put, buy a call and sell short one share,
investing the balance on the money market. If the American put is exercised
at time t ≤T, then we can withdraw X from the money market to buy a share
and close the short sale. We shall be left with the call option and a positive
amount
(−CA + P A + S(0))ert −X > Xert −X ≥0.

154
Mathematics for Finance
If the put is not exercised at all, then we can buy a share for X by exercising
the call at time T and close the short position in stock. On closing the money
market position, we shall also end up with a positive amount
(−CA + P A + S(0))erT −X > XerT −X > 0.
The theorem, therefore, holds by the No-Arbitrage Principle.
Exercise 7.8
Modify the proof of Theorem 7.2 to show that
S(0) −Xe−rT ≥CA −P A ≥S(0) −div0 −X
for a stock paying a dividend between time 0 and the expiry time T,
where div0 is the value of the dividend discounted to time 0.
Exercise 7.9
Modify the proof of Theorem 7.2 to show that
S(0) −Xe−rT ≥CA −P A ≥S(0)e−rdivT −X
for a stock paying dividends continuously at a rate rdiv.
7.3 Bounds on Option Prices
First of all, we note the obvious inequalities
CE ≤CA,
P E ≤P A,
(7.7)
for European and American options with the same strike price X and expiry
time T. They hold because an American option gives at least the same rights
as the corresponding European option.
Figure 7.3 shows a scenario of stock prices in which the payoffof a European
call is zero at the exercise time T, whereas that of an American call will be
positive if the option is exercised at an earlier time t < T when the stock price
S(t) is higher than X. Nevertheless, it does not necessarily follow that the
inequalities in (7.7) can be replaced by strict ones; see Section 7.3.2, where it
is shown that CE = CA for call options on an asset that pays no dividends.
Exercise 7.10
Prove (7.7) by an arbitrage argument.

7. Options: General Properties
155
Figure 7.3
Scenario in which an American call can bring a positive payoff,
but a European call cannot
It is also obvious that the price of a call or put option has to be non-negative
because an option of this kind offers the possibility of a future gain with no
liability. Therefore,
CE ≥0,
P E ≥0.
Similar inequalities are of course valid for the more valuable American options.
In fact the prices of options are nearly always strictly positive, except for some
very special circumstances, for example, CE = 0 for a call option with strike
price X = 120 dollars one day prior to exercise when the underlying stock
is trading at $100 and daily price movements are limited by stock exchange
regulations to ±10%.
In what follows we are going to discuss some further simple bounds for the
prices of European and American options. The advantage of such bounds is
that they are universal. They are independent of any particular model of stock
prices and follow from the No-Arbitrage Principle alone.
7.3.1 European Options
We shall establish some upper and lower bounds on the prices of European call
and put options.
On the one hand, observe that
CE < S(0).
If the reverse inequality were satisfied, that is, if CE ≥S(0), then we
could write and sell the option and buy the stock, investing the balance
on the money market. On the exercise date T we could then sell the stock
for min(S(T), X), settling the call option. Our arbitrage profit would be
(CE −S(0))erT + min(S(T), X) > 0. This proves that CE < S(0). On the

156
Mathematics for Finance
other hand, we have the lower bound
S(0) −Xe−rT ≤CE,
which follows immediately by put-call parity, since P E ≥0. Moreover, put-call
parity implies that
P E < Xe−rT ,
since CE < S(0), and
−S(0) + Xe−rT ≤P E,
since CE ≥0.
These results are summarised in the following proposition and illustrated
in Figure 7.4. The shaded areas correspond to option prices that satisfy the
bounds.
Figure 7.4
Bounds on European call and put prices
Proposition 7.3
The prices of European call and put options on a stock paying no dividends
satisfy the inequalities
max{0, S(0) −Xe−rT } ≤CE < S(0),
max{0, −S(0) + Xe−rT } ≤P E < Xe−rT .
For dividend-paying stock the bounds are
max{0, S(0) −div0 −Xe−rT } ≤CE < S(0) −div0,
max{0, −S(0) + div0 + Xe−rT } ≤P E < Xe−rT .
Exercise 7.11
Prove the above bounds on option prices for dividend-paying stock.

7. Options: General Properties
157
Exercise 7.12
For dividend-paying stock sketch the regions of call and put prices de-
termined by the bounds.
7.3.2 European and American Calls on Non-Dividend
Paying Stock
Consider European and American call options with the same strike price X and
expiry time T. We know that CA ≥CE, since the American option gives more
rights than its European counterpart. If the underlying stock pays no dividends,
then CE ≥S(0) −Xe−rT by Proposition 7.3. It follows that CA > S(0) −X if
r > 0. Because the price of the American option is greater than the payoff, the
option will sooner be sold than exercised at time 0.
The choice of 0 as the starting time is of course arbitrary. Replacing 0 by
any given t < T, we can show by the same argument that the American option
will not be exercised at time t. This means that the American option will in
fact never be exercised prior to expiry. This being so, it should be equivalent
to the European option. In particular, their prices should be equal, leading to
the following theorem.
Theorem 7.4
The prices of European and American call options on a stock that pays no
dividends are equal, CA = CE, whenever the strike price X and expiry time T
are the same for both options.
Proof
We already know that CA ≥CE, see (7.7) and Exercise 7.10. If CA > CE, then
write and sell an American call and buy a European call, investing the balance
CA −CE at the interest rate r. If the American call is exercised at time t ≤T,
then borrow a share and sell it for X to settle your obligation as writer of the
call option, investing X at rate r. Then, at time T you can use the European
call to buy a share for X and close your short position in stock. Your arbitrage
profit will be (CA −CE)erT + Xer(T −t) −X > 0. If the American option is not
exercised at all, you will end up with the European option and an arbitrage
profit of (CA −CE)erT > 0. This proves that CA = CE.
Theorem 7.4 may seem counter-intuitive at first sight. While it is possible

158
Mathematics for Finance
to gain S(t) −X by exercising an American call option if S(t) > X at time
t < T, this is not so with a European option, which cannot be exercised at time
t < T. It might, therefore, appear that the American call option should be more
valuable than the European one. Nevertheless, there is no contradiction. Even
though a European call option cannot be exercised at time t < T, it can be
sold for at least S(t) −X.
The situation is different for dividend-paying stock. Example 8.2 in the next
chapter shows a case in which an American call option is worth more than its
European counterpart and should be exercised prior to expiry, at least in some
scenarios.
On the other hand, it often happens that an American put should be ex-
ercised prematurely even if the underlying stock pays no dividends, as in the
following example.
Example 7.2
Suppose that the stock price is $10, the strike price of an American put expiring
in one year is $80, and the interest rate is 16%. Exercising the option now, we
can gain $70, which can be invested at 16% to become $81.20 after one year.
The value of a put option cannot possibly exceed the strike price, see (7.8), so
we are definitely better offby exercising the option early.
7.3.3 American Options
First we consider options on non-dividend paying stock. In this case the price of
an American call is equal to that of a European call, CA = CE, see Theorem 7.4,
so it must satisfy the same bounds as in Proposition 7.3. For an American put
we have
−S(0) + X ≤P A
because P A cannot be less than the payoffof the option at time 0. This gives a
sharper lower bound than that for a European put. However, the upper bound
has to be relaxed as compared to a European put. Namely,
P A < X.
(7.8)
Indeed, if P A ≥X, then the following arbitrage strategy could be constructed:
Write and sell an American put for P A and invest this amount at the interest
rate r. If the put is exercised at time t ≤T, then a share of the underlying
stock will have to be bought for X and can then be sold for S(t). The final cash
balance will be positive, P Aert −X + S(t) > 0. If the option is not exercised at

7. Options: General Properties
159
all, the final balance will also be positive, P AerT > 0, at expiry. These results
can be summarised as follows.
Proposition 7.5
The prices of American call and put options on a stock paying no dividends
satisfy the inequalities
max{0, S(0) −Xe−rT } ≤CA < S(0),
max{0, −S(0) + X} ≤P A < X.
Next we consider options on dividend-paying stock. The lower bounds for
European options imply that S(0) −div0 −Xe−rT ≤CE ≤CA and −S(0) +
div0 + Xe−rT ≤P E ≤P A. But because the price of an American option
cannot be less than its payoffat any time, we also have S(0) −X ≤CA and
X −S(0) ≤P A. Moreover, the upper bounds CA < S(0) and P A < X can
be established in a similar manner as for non-dividend paying stock. All these
inequalities can be summarised as follows: For dividend-paying stock
max{0, S(0) −div0 −Xe−rT , S(0) −X} ≤CA < S(0),
max{0, −S(0) + div0 + Xe−rT , −S(0) + X} ≤P A < X.
Exercise 7.13
Prove by an arbitrage argument that CA < S(0) for an American call
on dividend-paying stock.
7.4 Variables Determining Option Prices
The option price depends on a number of variables. These can be variables
characterising the option, such as the strike price X or expiry time T, variables
describing the underlying asset, for example, the current price S(0) or dividend
rate rdiv, variables connected with the market as a whole such as the risk-free
rate r, and of course the running time t.
We shall analyse option prices as functions of one of the variables, keeping
the remaining variables constant. This is a significant simplification because
usually a change in one variable is accompanied by changes in some or all
of the other variables. Nevertheless, even the simplified situation will provide
interesting insights.

160
Mathematics for Finance
7.4.1 European Options
Dependence on the Strike Price. We shall consider options on the same
underlying asset and with the same exercise time T, but with different val-
ues of the strike price X. The call and put prices will be denoted by CE(X)
and, respectively, P E(X) to emphasise their dependence on X. All remaining
variables such as the exercise time T, running time t and the underlying asset
price S(0) will be kept fixed for the time being.
Proposition 7.6
If X′ < X′′, then
CE(X′) > CE(X′′),
P E(X′) < P E(X′′).
This means that CE(X) is a strictly decreasing and P E(X) a strictly increasing
function of X.
These inequalities are obvious. The right to buy at a lower price is more
valuable than the right to buy at a higher price. Similarly, it is better to sell
an asset at a higher price than at a lower one.
Exercise 7.14
Give a rigorous arbitrage argument to prove the inequalities in Proposi-
tion 7.6.
Proposition 7.7
If X′ < X′′, then
CE(X′) −CE(X′′) < e−rT (X′′ −X′) ,
P E(X′′) −P E(X′) < e−rT (X′′ −X′) .
Proof
By put-call parity (7.1)
CE(X′) −P E(X′) = S(0) −X′e−rT ,
CE(X′′) −P E(X′′) = S(0) −X′′e−rT .

7. Options: General Properties
161
Subtracting, we get

CE(X′) −CE(X′′)

+

P E(X′′) −P E(X′)

= (X′′ −X′)e−rT .
Since, by Proposition 7.6, both terms on the left-hand side are positive, each
is strictly smaller than the right-hand side.
Remark 7.2
In the language of mathematics the inequalities mean that the call and put
prices as functions of the strike price satisfy the Lipschitz condition with con-
stant e−rT < 1,
|CE(X′′) −CE(X′)| ≤e−rT |X′′ −X′|,
|P E(X′′) −P E(X′)| ≤e−rT |X′′ −X′|.
In particular, the slope of the graph of the option price as a function of the
strike price is less than 45◦. This is illustrated in Figure 7.5 for a call option.
Figure 7.5
Lipschitz property of call prices CE(X)
Proposition 7.8
Let X′ < X′′ and let α ∈(0, 1). Then
CE(αX′ + (1 −α)X′′) ≤αCE(X′) + (1 −α)CE(X′′),
P E(αX′ + (1 −α)X′′) ≤αP E(X′) + (1 −α)P E(X′′).
In other words, CE(X) and P E(X) are convex functions of X.
Proof
For brevity, we put X = αX′ + (1 −α)X′′. Suppose that
CE(X) > αCE(X′) + (1 −α)CE(X′′).

162
Mathematics for Finance
We can write and sell an option with strike price X, and purchase α options with
strike price X′ and 1 −α options with strike price X′′, investing the balance
CE(X) −

αCE(X′) + (1 −α)CE(X′′)

> 0 without risk. If the option with
strike price X is exercised at expiry, then we shall have to pay (S(T) −X)+.
We can raise the amount α (S(T) −X′)++(1 −α) (S(T) −X′′)+ by exercising
α calls with strike X′ and 1−α calls with strike X′′. In this way we will realise
an arbitrage profit because of the following inequality, which is easy to verify
(the details are left to the reader, see Exercise 7.15):
(S(T) −X)+ ≤α (S(T) −X′)+ + (1 −α) (S(T) −X′′)+ .
(7.9)
Convexity for put options follows from that for calls by put-call parity (7.1).
Alternatively, an arbitrage argument can be given along similar lines as for call
options.
Exercise 7.15
Verify inequality (7.9).
Remark 7.3
According to Proposition 7.8, CE(X) and P E(X) are convex functions of X.
Geometrically, this means that if two points on the graph of the function are
joined with a straight line, then the graph of the function between the two
points will lie below the line. This is illustrated in Figure 7.6 for call prices.
Figure 7.6
Convexity of call prices CE(X)
Dependence on the Underlying Asset Price. The current price S(0) of the
underlying asset is given by the market and cannot be altered. However, we can
consider an option on a portfolio consisting of x shares, worth S = xS(0). The
payoffof a European call with strike price X on such a portfolio to be exercised
at time T will be (xS(T) −X)+. For a put the payoffwill be (X −xS(T))+. We
shall study the dependence of option prices on S. Assuming that all remaining
variables are fixed, we shall denote the call and put prices by CE(S) and P E(S).

7. Options: General Properties
163
Remark 7.4
Even though options on a portfolio of stocks are of little practical significance,
the functions CE(S) and P E(S) are important because they also reflect the de-
pendence of option prices on very sudden changes of the price of the underlying
such that the remaining variables remain almost unaltered.
Proposition 7.9
If S′ < S′′, then
CE(S′) < CE(S′′),
P E(S′) > P E(S′′),
that is, CE(S) is a strictly increasing function and P E(S) a strictly decreasing
function of S.
Proof
Suppose that CE(S′) ≥CE(S′′) for some S′ < S′′, where S′ = x′S(0) and S′′ =
x′′S(0). We can write and sell a call on a portfolio with x′ shares and buy a call
on a portfolio with x′′ shares, the two options sharing the same strike price X
and exercise time T, and we can invest the balance CE(S′) −CE(S′′) without
risk. Since x′ < x′′, the payoffs satisfy (x′S(T) −X)+ ≤(x′′S(T) −X)+ with
strict inequality whenever X < x′′S(T). If the option sold is exercised at time T,
we can, therefore, exercise the other option to cover our liability and will be
left with an arbitrage profit.
The inequality for puts follows by a similar arbitrage argument.
Exercise 7.16
Prove the inequality in Proposition 7.9 for put options.
Proposition 7.10
Suppose that S′ < S′′. Then
CE(S′′) −CE(S′) < S′′ −S′,
P E(S′) −P E(S′′) < S′′ −S′.

164
Mathematics for Finance
Proof
We employ put-call parity (7.1):
CE(S′′) −P E(S′′) = S′′ −Xe−rT ,
CE(S′) −P E(S′) = S′ −Xe−rT .
Subtracting, we get
(CE(S′′) −CE(S′)) + (P E(S′) −P E(S′′)) = S′′ −S′.
Both terms on the left-hand side are non-negative by the previous theorem, so
each is strictly less than the right-hand side.
Remark 7.5
A consequence of Proposition 7.10 is that the slope of the straight line joining
two points on the graph of the call or put price as a function of S is less than 45◦.
This is illustrated in Figure 7.7 for call options. In other words, the call and
Figure 7.7
Lipschitz property of call prices CE(S)
put prices CE(S) and P E(S) satisfy the Lipschitz condition with constant 1,
!!CE(S′′) −CE(S′)
!! ≤|S′′ −S′| ,
!!P E(S′′) −P E(S′)
!! ≤|S′′ −S′| .
Proposition 7.11
Let S′ < S′′ and let α ∈(0, 1). Then
CE(αS′ + (1 −α)S′′) ≤αCE(S′) + (1 −α)CE(S′′),
P E(αS′ + (1 −α)S′′) ≤αP E(S′) + (1 −α)P E(S′′).
This means that the call and put prices are convex functions of S.

7. Options: General Properties
165
Proof
We put S = αS′ + (1 −α)S′′ for brevity. Let S′ = x′S(0), S′′ = x′′S(0) and
S = xS(0), so x = αx′ + (1 −α) x′′. Suppose that
CE(S) > αCE(S′) + (1 −α)CE(S′′).
We write and sell a call on a portfolio with x shares, and purchase α calls on a
portfolio with x′ shares and 1 −α calls on a portfolio with x′′ shares, investing
the balance CE(S) −αCE(S′) −(1 −α)CE(S′′) without risk. If the option sold
is exercised at time T, then we shall have to pay (xS(T) −X)+. To cover this
liability we can exercise the other options. Since
(xS(T) −X)+ ≤α (x′S(T) −X)+ + (1 −α) (x′′S(T) −X)+ ,
this is an arbitrage strategy.
The inequality for put options can be proved by a similar arbitrage argument
or using put-call parity.
7.4.2 American Options
In general, American options have similar properties to their European counter-
parts. One difficulty is the absence of put-call parity; we only have the weaker
estimates in Theorem 7.2. In addition, we have to take into account the possi-
bility of early exercise.
Dependence on the Strike Price. We shall denote the call and put prices
by CA(X) and P A(X) to emphasise the dependence on X, keeping any other
variables fixed.
The following proposition is obvious for the same reasons as for European
options: Higher strike price makes the right to buy less valuable and the right
to sell more valuable.
Proposition 7.12
If X′ < X′′, then
CA(X′) > CA(X′′),
P A(X′) < P A(X′′).
Exercise 7.17
Give a rigorous arbitrage proof of Proposition 7.12.

166
Mathematics for Finance
Proposition 7.13
Suppose that X′ < X′′. Then
CA(X′) −CA(X′′) < X′′ −X′,
P A(X′′) −P A(X′) < X′′ −X′.
Proof
Suppose that X′ < X′′, but CA(X′) −CA(X′′) ≥X′′ −X′. We write and
sell a call with strike price X′, buy a call with strike price X′′ and invest the
balance CA(X′) −CA(X′′) without risk. If the written option is exercised at
time t ≤T, then we shall have to pay (S(t) −X′)+. Exercising the other option
immediately, we shall receive (S(t) −X′′)+. Observe that
(S(t) −X′′)+ −(S(t) −X′)+ ≥−(X′′ −X′)
with strict inequality whenever S(t) < X′′. Together with the risk-free invest-
ment, amounting to at least X′′ −X′, we shall therefore end up with a non-
negative sum of money, and in fact realise an arbitrage profit if S(t) < X′′.
The proof is similar for put options.
Theorem 7.14
Suppose that X′ < X′′ and let α ∈(0, 1). Then
CA(αX′ + (1 −α)X′′) ≤αCA(X′) + (1 −α)CA(X′′),
P A(αX′ + (1 −α)X′′) ≤αP E(X′) + (1 −α)P A(X′′).
Proof
For brevity, we put X = αX′ + (1 −α)X′′. Suppose that
CA(X) > αCA(X′) + (1 −α)CA(X′′).
We write an option with strike price X and buy α options with strike price X′
and (1 −α) options with strike price X′′, investing without risk the positive
balance of these transactions. If the written option is exercised at time t ≤T,
then we exercise both options held. In this way we shall achieve arbitrage
because
(S(t) −X)+ ≤α (S(t) −X′)+ + (1 −α) (S(t) −X′′)+ .
The proof for put options is similar.

7. Options: General Properties
167
Dependence on the Underlying Asset Price. Once again, we shall con-
sider options on a portfolio of x shares. The prices of American calls and puts
on such a portfolio will be denoted by CA(S) and P A(S), where S = xS(0) is
the value of the portfolio, all remaining variables being fixed. The payoffs at
time t are (xS(t) −X)+ for calls and (X −xS(t))+ for puts.
Proposition 7.15
If S′ < S′′, then
CA(S′) < CA(S′′),
P A(S′) > P A(S′′).
Proof
Suppose that CA(S′) ≥CA(S′′) for some S′ < S′′, where S′ = x′S(0) and
S′′ = x′′S(0). We can write and sell a call on a portfolio with x′ shares and buy
a call on a portfolio with price x′′ shares, both options having the same strike
price X and expiry time T. The balance CA(S′)−CA(S′′) of these transactions
can be invested without risk. If the written option is exercised at time t ≤T,
then we can meet the liability by exercising the other option immediately.
Because x′ < x′′, the payoffs satisfy (x′S(t) −X)+ ≤(x′′S(t) −X)+ with
strict inequality whenever X < x′′S(t). As a result, this strategy will provide
an arbitrage opportunity.
The proof is similar for put options.
Proposition 7.16
Suppose that S′ < S′′. Then
CA(S′′) −CA(S′) < S′′ −S′,
P A(S′) −P A(S′′) < S′′ −S′.
Proof
By the inequalities in Theorem 7.2
CA(S′) −P A(S′) ≥S′ −X,
CA(S′′) −P A(S′′) ≤S′′ −Xe−rT .

168
Mathematics for Finance
On subtracting, we obtain

CA(S′′) −CA(S′)

+

P A(S′) −P A(S′′)

≤S′′ −S′ + X(1 −e−rT )
≤S′′ −S′.
Each of the two terms on the left-hand side is positive, so it must be strictly
less than S′′ −S′, which completes the proof.
Proposition 7.17
Let S′ < S′′ and let α ∈(0, 1). Then
CA(αS′ + (1 −α)S′′) ≤αCA(S′) + (1 −α)CA(S′′),
P A(αS′ + (1 −α)S′′) ≤αP A(S′) + (1 −α)P A(S′′).
Proof
Let S = αS′ + (1 −α)S′′ and let S′ = x′S(0), S′′ = x′′S(0) and S = xS(0).
Suppose that
CA(S) > αCA(S′) + (1 −α)CA(S′′).
We can write and sell a call on a portfolio with x shares, and purchase α calls
on a portfolio with x′ shares and 1 −α calls on a portfolio with x′′ shares, all
three options sharing the same strike price X and expiry time T. The positive
balance CA(S)−αCA(S′)−(1−α)CA(S′′) of these transactions can be invested
without risk. If the written option is exercised at time t ≤T, then we shall
have to pay (xS(t) −X)+, where x = αx′ + (1 −α) x′′. We can exercise the
other two options to cover the liability. This is an arbitrage strategy because
(xS(t) −X)+ ≤α (x′S(t) −X)+ + (1 −α) (x′′S(t) −X)+ .
The proof for put options is similar.
Dependence on the Expiry Time. For American options we can also for-
mulate a general result on the dependence of their prices on the expiry time T.
To emphasise this dependence, we shall now write CA(T) and P A(T) for the
prices of American calls and puts, assuming that all other variables are fixed.
Proposition 7.18
If T ′ < T ′′, then
CA(T ′) ≤CA(T ′′),
P A(T ′) ≤P A(T ′′).

7. Options: General Properties
169
Proof
Suppose that CA(T ′) > CA(T ′′). We write and sell one option expiring at
time T ′ and buy one with the same strike price but expiring at time T ′′, invest-
ing the balance without risk. If the written option is exercised at time t ≤T ′,
we can exercise the other option immediately to cover our liability. The posi-
tive balance CA(T ′) −CA(T ′′) > 0 invested without risk will be our arbitrage
profit.
The argument is the same for puts.
7.5 Time Value of Options
The following convenient terminology is often used. We say that at time t a
call option with strike price X is
• in the money if S(t) > X,
• at the money if S(t) = X,
• out of the money if S(t) < X.
Similarly, for a put option we say that it is
• in the money if S(t) < X,
• at the money if S(t) = X,
• out of the money if S(t) > X.
Also convenient, though less precise, are the terms deep in the money and deep
out of the money, which mean that the difference between the two sides in the
respective inequalities is considerable.
An American option in the money will bring a positive payoffif exercised
immediately, whereas an option out of the money will not. We use the same
terms for European options, though their meaning is different: Even if the
option is currently in the money, it may no longer be so on the exercise date,
when the payoffmay well turn out to be zero. A European option in the money
is no more than a promising asset.
Definition 7.1
At time t ≤T the intrinsic value of a call option with strike price X is equal
to (S(t) −X)+. The intrinsic value of a put option with the same strike price
is (X −S(t))+.
We can see that the intrinsic value is zero for options out of the money or at
the money. Options in the money have positive intrinsic value. The price of an

170
Mathematics for Finance
option at expiry T coincides with the intrinsic value. The price of an American
option prior to expiry may be greater than the intrinsic value because of the
possibility of future gains. The price of a European option prior to the exercise
time may be greater or smaller than the intrinsic value.
Definition 7.2
The time value of an option is the difference between the price of the option
and its intrinsic value, that is,
CE(t) −(S(t) −X)+
for a European call,
P E(t) −(X −S(t))+
for a European put,
CA(t) −(S(t) −X)+
for an American call,
P A(t) −(X −S(t))+
for an American put.
Example 7.3
Let us examine some typical data. Suppose that the current price of stock is
$125.23 per share. Consider the following:
Intrinsic Value
Time Value
Option Price
Srike Price
Call
Put
Call
Put
Call
Put
110
15.23
0.00
3.17
2.84
18.40
2.84
120
5.23
0.00
7.04
6.46
12.27
6.46
130
0.00
5.23
6.78
4.41
6.78
9.64
An American call option with strike price $110 is in the money and has $15.23
intrinsic value. The option price must be at least equal to the intrinsic value,
since the option may be exercised immediately. Typically, the price will be
higher than the intrinsic value because of the possibility of future gains. On
the other hand, a put option with strike price $110 will be out of the money
and its intrinsic value will be zero. The positive price of the put is entirely due
to the possibility of future gains. Similar relationships for other strike prices
can be seen in the table.
The time value of a European call as a function of S is shown in Figure 7.8.
It can never be negative, and for large values of S it exceeds the difference
X −Xe−rT . This is because of the inequality CE(S) ≥S −Xe−rT , see Propo-
sition 7.3.
The market value of a European put may be lower than its intrinsic value,
that is, the time value may be negative, see Figure 7.9. This may be so only if
the put option is in the money, S < X, and it should be deep in the money.

7. Options: General Properties
171
Figure 7.8
Time value CE(S) −(S −X)+ of a European call option
For a European option we have to wait until the exercise time T to realise the
payoff. The risk that the stock price will rise above X in the meantime may be
considerable, which reduces the value of the option.
Figure 7.9
Time value P E(S) −(X −S)+ of a European put option
The time value of an American call option is the same as that of a European
call (if there are no dividends) and Figure 7.8 applies. For an American put a
typical graph of the time value is shown in Figure 7.10.
Figure 7.10
Time value CA(S) −(S −X)+ of an American put option
Figures 7.8, 7.9 and 7.10 also illustrate the following assertion.
Proposition 7.19
For any European or American call or put option with strike price X, the time
value attains its maximum at S = X.
Proof
We shall present an argument for European calls. For S ≤X the intrinsic

172
Mathematics for Finance
value of the option is zero. Since CE(S) is an increasing function of S by
Proposition 7.9, this means that the time value is an increasing function of S
for S ≤X. On the other hand, CE(S′′) −CE(S′) ≤S′′ −S′ for any S′ < S′′ by
Proposition 7.10. It follows that CE(S′′) −(S′′ −X)+ ≤CE(S′) −(S′ −X)+
if X ≤S′ < S′′, which means that the time value is a decreasing function of S
for S ≥X. As a result, the time value has a maximum at S = X.
The proof for other options is similar.
Exercise 7.18
Prove Proposition 7.19 for put options.

8
Option Pricing
By a European derivative security or contingent claim with stock S as the
underlying asset we mean a random variable of the form D(T) = f(S(T)),
where f is a given function, called the payoff. This is a direct generalisation of
a call option with f(S) = (S −X)+, a put option with f(S) = (X −S)+, or a
forward contract with f(S) = S −X (for the long position).
We have already learnt the basic method of pricing options in the one-step
model (see Section 1.6) based on replicating the option payoff. Not surprisingly,
this idea extends to a general binomial tree model constructed out of such one-
step two-state building blocks. Developing this extension will be our primary
task in this chapter.
Theorem 8.1
Suppose that for any contingent claim D(T) there exists a replication strategy,
that is, an admissible strategy x(t), y(t) with final value V (T) = D(T). Then
the price D(0) of the contingent claim at time 0 must be equal to that of the
replicating strategy, V (0) = D(0).
Proof
The proof is just a modification of that of Proposition 1.3. If D(0) > V (0),
then we write the derivative security and take a long position in the strategy.
Our obligation will be covered by the strategy, the difference D(0)−V (0) being
173


## Option Pricing

174
Mathematics for Finance
our arbitrage profit. If D(0) < V (0), then we take the opposite positions, with
V (0) −D(0) the resulting arbitrage profit.
Replication also solves the problem of hedging the position of the option
writer. If the cash received for the option is invested in the replicating strategy,
then all the risk involved in writing the option will be eliminated.
In this chapter we shall gradually develop such pricing methods for options,
starting with a comprehensive analysis of the one-step binomial model, which
will then be extended to a multi-step model. Finally, the Black–Scholes formula
in continuous time will be introduced.
8.1 European Options in the Binomial Tree
Model
8.1.1 One Step
This simple case was discussed in Chapter 1. Here we shall reiterate the ideas
in a more general setting: We shall be pricing general derivative securities and
not just call or put options. This will enable us to extend the approach to the
multi-step model.
We assume that the random stock price S(1) at time 1 may take two values
denoted by
 Su = S(0)(1 + u),
Sd = S(0)(1 + d),
with probabilities p and 1 −p, respectively. To replicate a general derivative
security with payofff we need to solve the system of equations
 x(1)Su + y(1)(1 + r) = f(Su),
x(1)Sd + y(1)(1 + r) = f(Sd),
for x(1) and y(1). This gives
x(1) = f(Su) −f(Sd)
Su −Sd
,
which is the replicating position in stock, called the delta of the option. We
also find the money market position
y(1) = −(1 + d)f(Su) −(1 + u)f(Sd)
(u −d)(1 + r)
.

8. Option Pricing
175
The initial value of the replicating portfolio is x(1)S(0)+y(1). By Theorem 8.1
D(0) = x(1)S(0) + y(1)
= f(Su) −f(Sd)
u −d
−(1 + d)f(Su) −(1 + u)f(Sd)
(u −d)(1 + r)
.
(8.1)
Exercise 8.1
Show that the price of a call option grows with u, the other variables
being kept constant. Analyse the impact of a change of d on the option
price.
Exercise 8.2
Find a formula for the price CE(0) of a call option if r = 0 and S(0) =
X = 1 dollar. Compute the price for u = 0.05 and d = −0.05, and also
for u = 0.01 and d = −0.19. Draw a conclusion about the relationship
between the variance of the return on stock and that on the option.
Recall the notion of the risk-neutral probability, given by
p∗= r −d
u −d,
(8.2)
which turns the discounted stock price process (1+r)−nS(n) into a martingale,
see Chapter 3.
Theorem 8.2
The expectation of the discounted payoffcomputed with respect to the risk-
neutral probability is equal to the present value of the contingent claim,
D(0) = E∗

(1 + r)−1f(S(1))

.
(8.3)

176
Mathematics for Finance
Proof
This is an immediate consequence of (8.1):
D(0) = f(Su) −f(Sd)
u −d
+ (1 + u)f(Sd) −(1 + d)f(Su)
(u −d) (1 + r)
=
1
1 + r
	(r −d)f(Su)
(u −d)
+ (u −r)f(Sd)
u −d

=
1
1 + r

p∗f(Su) + (1 −p∗)f(Sd)

= E∗

(1 + r)−1f(S(1))

,
as claimed.
Exercise 8.3
Find the initial value of the portfolio replicating a call option if propor-
tional transaction costs are incurred whenever the underlying stock is
sold. (No transaction costs apply when the stock is bought.) Compare
this value with the case free of such costs. Assume that S(0) = X = 100
dollars, u = 0.1, d = −0.1 and r = 0.05, admitting transaction costs at
c = 2% (the seller receiving 98% of the stock value).
Exercise 8.4
Let S(0) = 75 dollars and let u = 0.2 and d = −0.1. Suppose that you
can borrow money at 12%, but the rate for deposits is lower at 8%. Find
the values of the replicating portfolios for a put and a call. Is the answer
consistent with the put and call prices following from Theorem 8.2?
8.1.2 Two Steps
We begin with two time steps. The stock price S(2) has three possible values
Suu = S(0)(1 + u)2,
Sud = S(0)(1 + u)(1 + d),
Sdd = S(0)(1 + d)2,
and S(1) has two values
Su = S(0)(1 + u),
Sd = S(0)(1 + d),
at the nodes of the tree in Figure 8.1 marked by the corresponding sequences
of letters u and d.

8. Option Pricing
177
Figure 8.1
Branchings in the two-step binomial tree
For each of the three subtrees in Figure 8.1 we can use the one-step repli-
cation procedure as described above. At time 2 the derivative security is rep-
resented by its payoff,
D(2) = f(S(2)),
which has three possible values. The derivative security price D(1) has two
values
1
1 + r

p∗f(Suu) + (1 −p∗) f(Sud)

,
1
1 + r

p∗f(Sdu) + (1 −p∗) f(Sdd)

,
found by the one-step procedure applied to the two subtrees at nodes u and d.
This gives
D(1) =
1
1 + r

p∗f(S(1)(1 + u)) + (1 −p∗) f(S(1)(1 + d))

= g(S(1)),
where
g(x) =
1
1 + r

p∗f(x(1 + u)) + (1 −p∗)f(x(1 + d))

.
As a result, D(1) can be regarded as a derivative security expiring at time 1
with payoffg. (Though it cannot be exercised at time 1, the derivative security
can be sold for D(1) = g(S(1)).) This means that the one-step procedure can
be applied once again to the single subtree at the root of the tree. We have,
therefore,
D(0) =
1
1 + r

p∗g(S(0)(1 + u)) + (1 −p∗) g(S(0)(1 + d))

.
It follows that
D(0) =
1
1 + r

p∗g(Su) + (1 −p∗) g(Sd)

=
1
(1 + r)2

p2
∗f(Suu) + 2p∗(1 −p∗) f(Sud) + (1 −p∗)2 f(Sdd)

.
The last expression in square brackets is the risk-neutral expectation of f(S(2)).
This proves the following result.

178
Mathematics for Finance
Theorem 8.3
The expectation of the discounted payoffcomputed with respect to the risk-
neutral probability is equal to the present value of the derivative security,
D(0) = E∗

(1 + r)−2f(S(2))

.
Exercise 8.5
Let S(0) = 120 dollars, u = 0.2, d = −0.1 and r = 0.1. Consider a call
option with strike price X = 120 dollars and exercise time T = 2. Find
the option price and the replicating strategy.
Exercise 8.6
Using the data in the previous exercise, find the price of a call and the
replicating strategy if a 15 dollar dividend is paid at time 1.
8.1.3 General N-Step Model
The extension of the results above to a multi-step model is straightforward.
Beginning with the payoffat the final step, we proceed backwards, solving the
one-step problem repeatedly. Here is the procedure for the three-step model:
D(3) = f(S(3)),
D(2) =
1
1 + r [p∗f(S(2)(1 + u)) + (1 −p∗)f(S(2)(1 + d))]
= g(S(2)),
D(1) =
1
1 + r [p∗g(S(1)(1 + u)) + (1 −p∗)g(S(1)(1 + d))]
= h(S(1)),
D(0) =
1
1 + r [p∗h(S(0)(1 + u)) + (1 −p∗)h(S(0)(1 + d))] ,
where
g(x) =
1
1 + r [p∗f(x(1 + u)) + (1 −p∗)f(x(1 + d))] ,
h(x) =
1
1 + r [p∗g(x(1 + u)) + (1 −p∗)g(x(1 + d))] .

8. Option Pricing
179
It follows that
D(0) =
1
1 + r

p∗h(Su) + (1 −p∗)h(Sd))

=
1
(1 + r)2

p2
∗g(Suu) + 2p∗(1 −p∗)g(Sud) + (1 −p∗)2g(Sdd))

=
1
(1 + r)3

p3
∗f(Suuu) + 3p2
∗(1 −p∗)f(Suud)
+3p∗(1 −p∗)2f(Sudd) + (1 −p∗)3f(Sddd))

.
The emerging pattern is this: Each term in the square bracket is characterised
by the number k of upward stock price movements. This number determines
the power of p∗and the choice of the payoffvalue. The power of 1 −p∗is the
number of downward price movements, equal to 3 −k in the last expression,
and N −k in general, where N is the number of steps. The coefficients in front
of each term give the number of scenarios (paths through the tree) that lead
to the corresponding payoff, equal to
N
k

=
N!
k!(N−k)!, the number of k-element
combinations out of N elements. For example, there are three paths through
the 3-step tree leading to the node udd.
As a result, in the N-step model
D(0) =
1
(1 + r)N
N

k=0
	N
k

pk
∗(1 −p∗)N−kf

S(0)(1 + u)k(1 + d)N−k
.
(8.4)
The expectation of f(S(N)) under the risk-neutral probability can readily be
recognised in this formula. The result can be summarised as follows.
Theorem 8.4
The value of a European derivative security with payofff(S(N)) in the N-
step binomial model is the expectation of the discounted payoffunder the
risk-neutral probability:
D(0) = E∗

(1 + r)−Nf(S(N))

.
Remark 8.1
There is no need to know the actual probability p to compute D(0). This re-
markable property of the option price is important in practice, as the value
of p may be difficult to estimate from market data. Instead, the formula for
D(0) features p∗, the risk-neutral probability, which may have nothing in com-
mon with p, but is easy to compute from (8.2).

180
Mathematics for Finance
8.1.4 Cox–Ross–Rubinstein Formula
The payofffor a call option with strike price X satisfies f(x) = 0 for x ≤X,
which reduces the number of terms in (8.4). The summation starts with the
least m such that
S(0)(1 + u)m(1 + d)N−m > X.
Hence
CE(0) = (1 + r)−N
N

k=m
	N
k

pk
∗(1 −p∗)N−k
S(0)(1 + u)k(1 + d)N−k −X

.
This can be written as
CE(0) = x(1)S(0) + y(1),
relating the option price to the initial replicating portfolio x(1), y(1), where
x(1) = (1 + r)−N
N

k=m
	N
k

pk
∗(1 −p∗)N−k(1 + u)k(1 + d)N−k,
y(1) = −X(1 + r)−N
N

k=m
	N
k

pk
∗(1 −p∗)N−k.
The expression for x(1) can be rewritten as
x(1) =
N

k=m
	N
k

 	
p∗
1 + u
1 + r

k 	
(1 −p∗)1 + d
1 + r

N−k
=
N

k=m
	N
k

q
k
(1 −q)N−k,
where
q = p∗
1 + u
1 + r .
(Note that p∗1+u
1+r and (1 −p∗) 1+d
1+r add up to one.) Similar formulae can be
derived for put options, either directly or using put-call parity.
These important results are summarised in the following theorem, in which
Φ(m, N, p) denotes the cumulative binomial distribution with N trials and
probability p of success in each trial,
Φ(m, N, p) =
m

k=0
	N
k

pk (1 −p)N−k .

8. Option Pricing
181
Theorem 8.5 (Cox–Ross–Rubinstein Formula)
In the binomial model the price of a European call and put option with strike
price X to be exercised after N time steps is given by
CE(0) = S(0) [1 −Φ(m −1, N, q)] −(1 + r)−NX [1 −Φ(m −1, N, p∗)] ,
P E(0) = −S(0)Φ(m −1, N, q) + (1 + r)−NXΦ(m −1, N, p∗).
The initial replicating portfolio x(1), y(1) is given by
x(1)
y(1)
for a call
1 −Φ(m −1, N, q)
−(1 + r)−NX [1 −Φ(m −1, N, p∗)]
for a put
−Φ(m −1, N, q)
(1 + r)−NXΦ(m −1, N, p∗)
Exercise 8.7
Let S(0) = 50 dollars, r = 5%, u = 0.3 and d = −0.1. Find the price of
a European call and put with strike price X = 60 dollars to be exercised
after N = 3 time steps.
Exercise 8.8
Let S(0) = 50 dollars, r = 0.5%, u = 0.01 and d = −0.01. Find m, x(1),
and the price CE(0) of a European call option with strike X = 60 dollars
to be exercised after N = 50 time steps.
Exercise 8.9
Consider the scenario in which stock goes up at each step. At which step
will the delta of a European call become 1?
8.2 American Options in the Binomial Tree
Model
Even the formulation of a precise mathematical definition of an American type
contingent claim presents some difficulties. Nevertheless, the informal descrip-
tion is simple: The option can be exercised at any time step n such that
0 ≤n ≤N, with payofff(S(n)). Of course, it can be exercised only once.
The price of an American option at time n will be denoted by DA(n).

182
Mathematics for Finance
To begin with, we shall analyse an American option expiring after 2 time
steps. Unless the option has already been exercised, at expiry it will be worth
DA(2) = f(S(2)),
where we have three values depending on the values of S(2). At time 1 the op-
tion holder will have the choice to exercise immediately, with payofff(S(1)), or
to wait until time 2, when the value of the American option will become f(S(2)).
The value of waiting can be computed by treating f(S(2)) as a one-step Euro-
pean contingent claim to be priced at time 1, which gives the value
1
1 + r [p∗f(S(1)(1 + u)) + (1 −p∗)f(S(1)(1 + d))]
at time 1. In effect, the option holder has the choice between the latter value or
the immediate payofff(S(1)). The American option at time 1 will, therefore,
be worth the higher of the two,
DA(1) = max
"
f(S(1)),
1
1 + r [p∗f(S(1)(1 + u)) + (1 −p∗)f(S(1)(1 + d))]
#
= f1(S(1))
(a random variable with two values), where
f1(x) = max
"
f(x),
1
1 + r [p∗f(x(1 + u)) + (1 −p∗)f(x(1 + d))]
#
.
A similar argument gives the American option value at time 0,
DA(0) = max
"
f(S(0)),
1
1 + r [p∗f1(S(0)(1 + u)) + (1 −p∗)f1(S(0)(1 + d))]
#
.
Example 8.1
To illustrate the above procedure we consider an American put option with
strike price X = 80 dollars expiring at time 2 on a stock with initial price
S(0) = 80 dollars in a binomial model with u = 0.1, d = −0.05 and r = 0.05.
(We consider a put, as we know that there is no difference between American
and European call options, see Theorem 7.4.) The stock values are
n
0
1
2
96.80
88.00
<
S(n)
80.00
<
83.60
76.00
<
72.20

8. Option Pricing
183
The price of the American put will be denoted by P A(n) for n = 0, 1, 2. At
expiry the payoffwill be positive only in the scenario with two downward stock
price movements,
n
0
1
2
0.00
?
<
P A(n)
?
<
0.00
?
<
7.80
At time 1 the option writer can choose between exercising the option immedi-
ately or waiting until time 2. In the up state at time 1 the immediate payoff
and the value of waiting are both zero. In the down state the immediate payoff
is 4 dollars, while the value of waiting is 1.05−1 × 1
3 × 7.8 ∼= 2.48 dollars. The
option holder will choose the higher value (exercising the option in the down
state at time 1). This gives the time 1 values of the American put,
n
0
1
2
0.00
0.00
<
P A(n)
?
<
0.00
4.00
<
7.80
At time 0 the choice is, once again, between the payoff, which is zero, or the
value of waiting, which is 1.05−1 × 1
3 × 4 ∼= 1.27 dollars. Taking the higher of
the two completes the tree of option prices,
n
0
1
2
0.00
0.00
<
P A(n)
1.27
<
0.00
4.00
<
7.80
For comparison, the price of a European put is P E(0) = 1.05−1× 1
3 ×2.48 ∼= 0.79
dollars, clearly less than the American put price P A(0) ∼= 1.27 dollars.
This can be generalised, leading to the following definition.
Definition 8.1
An American derivative security or contingent claim with payofffunction f
expiring at time N is a sequence of random variables defined by backward

184
Mathematics for Finance
induction:
DA(N) = f(S(N)),
DA(N −1) = max
"
f(S(N −1)),
1
1 + r[p∗f(S(N −1)(1 + u))
+ (1 −p∗)f(S(N −1)(1 + d))]
#
=: fN−1(S(N −1)),
DA(N −2) = max
"
f(S(N −2)),
1
1 + r[p∗fN−1(S(N −2)(1 + u))
+ (1 −p∗)fN−1(S(N −2)(1 + d))]
#
=: fN−2(S(N −2)),
...
DA(1) = max
"
f(S(2)),
1
1 + r[p∗f2(S(1)(1 + u))
+ (1 −p∗)f2(S(1)(1 + d))]
#
=: f1(S(1)),
DA(0) = max
"
f(S(0)),
1
1 + r[p∗f1(S(0)(1 + u))
+ (1 −p∗)f1(S(0)(1 + d))]
#
.
Exercise 8.10
Compute the value of an American put expiring at time 3 with strike
price X = 62 dollars on a stock with initial price S(0) = 60 dollars in a
binomial model with u = 0.1, d = −0.05 and r = 0.03.
Exercise 8.11
Compare the prices of an American call and a European call with strike
price X = 120 dollars expiring at time 2 on a stock with initial price
S(0) = 120 dollars in a binomial model with u = 0.2, d = −0.1 and
r = 0.1.
Example 8.2
The last exercise can be modified to show that the equality of European and
American call prices may not hold if a dividend is paid. Suppose that a dividend
of 14 dollars is paid at time 2. Otherwise, we shall use the same data as in

8. Option Pricing
185
Exercise 8.11. The ex-dividend stock prices are
n
0
1
2
158.80
144.00
<
S(n)
120.00
<
115.60
ex-div
108.00
<
83.20
The corresponding European and American call values will be
n
0
1
2
38.80
38.80
23.52
24.00
<
CE(n)
CA(n)
14.25
14.55
<
0.00
0.00
0.00
0.00
<
0.00
0.00
The American call should be exercised early in the up state at time 1 with
payoff24 dollars (bold figures), which is more than the value of holding the
option to expiry. As a result, the price of the American call is higher than that
of the European call.
Exercise 8.12
Compute the prices of European and American puts with exercise and
strike price X = 14 dollars expiring at time 2 on a stock with S(0) = 12
dollars in a binomial model with u = 0.1, d = −0.05 and r = 0.02,
assuming that a dividend of 2 dollars is paid at time 1.
8.3 Black–Scholes Formula
We shall present an outline of the main results for European call and put
options in continuous time, culminating in the famous Black–Scholes formula.
Our treatment of continuous time is a compromise lacking full mathematical
rigour, which would require a systematic study of Stochastic Calculus, a topic

186
Mathematics for Finance
treated in detail in more advanced texts. In place of this, we shall exploit an
analogy with the discrete time case.
As a starting point we take the continuous time model of stock prices de-
veloped in Chapter 3 as a limit of suitably scaled binomial models with time
steps going to zero. In the resulting continuous time model the stock price is
given by
S(t) = S(0)emt+σW (t),
(8.5)
where W(t) is the standard Wiener process (Brownian motion), see Sec-
tion 3.3.2. This means, in particular, that S(t) has the log normal distribution.
Consider a European option on the stock expiring at time T with payoff
f(S(T)). As in the discrete-time case, see Theorem 8.4, the time 0 price D(0)
of the option ought to be equal to the expectation of the discounted payoff
e−rT f(S(T)),
D(0) = E∗

e−rT f(S(T))

,
(8.6)
under a risk-neutral probability P∗that turns the discounted stock price process
e−rtS(t) into a martingale. Here we shall accept this formula without proof,
by analogy with the discrete time result. (The proof is based on an arbitrage
argument combined with a bit of Stochastic Calculus, the latter beyond the
scope of this book.)
What is the risk-neutral probability P∗, then? A necessary condition is that
the expectation of the discounted stock prices e−rtS(t) should be constant
(independent of t), just like in the discrete time case, see (3.5).
Let us compute this expectation using the real market probability P. Since
W(t) is normally distributed with mean 0 and variance t, it has density
1
√
2πte−x2
2t under probability P. As a result,
E

e−rtS(t)

= S(0)E

eσW (t)+(m−r)t
= S(0)
$ ∞
−∞
eσx+(m−r)t
1
√
2πte−x2
2t dx
= S(0)e(m−r+ 1
2 σ2)t
$ ∞
−∞
1
√
2πte−(x−σt)2
2t
dx
= S(0)e(m−r+ 1
2 σ2)t
$ ∞
−∞
1
√
2πte−y2
2t dy
= S(0)e(m−r+ 1
2 σ2)t.
If m + 1
2σ2 ̸= r, then the expectation E(e−rtS(t)) = S(0)e(m−r+ 1
2 σ2)t clearly
depends on t, so S(t) cannot be a martingale under P.
However, the calculations above suggest a modification P∗of P that would
make the corresponding expectation E∗(e−rtS(t)) independent of t by elimi-
nating the exponential factor e(m−r+ 1
2 σ2)t. Namely, if P can be replaced by

8. Option Pricing
187
a probability P∗such that V (t) = W(t) +

m −r + 1
2σ2
t/σ (rather than
W(t) itself) becomes a Wiener process under P∗, then the exponential factor
e(m−r+ 1
2 σ2)t will be eliminated from the final expression. (The existence of such
a probability P∗follows from an advanced result in Stochastic Calculus, the so-
called Girsanov theorem.) Indeed, since V (t) has density
1
√
2πte−x2
2t under P∗,
that is, it is normally distributed with mean 0 and variance t, it follows that
E∗

e−rtS(t)

= S(0)E∗

eσW (t)+(m−r)t
= S(0)E∗

eσV (t)−1
2 σ2t
= S(0)
$ ∞
−∞
eσx−1
2 σ2t
1
√
2πte−x2
2t dx
= S(0)
$ ∞
−∞
1
√
2πte−(x−σt)2
2t
dx
= S(0)
$ ∞
−∞
1
√
2πte−y2
2t dy = S(0).
The fact that E∗(e−rtS(t)) = S(0) does not depend on time t is a necessary
condition for the discounted price process e−rtS(t) to be a martingale under P∗.
To show that e−rtS(t) is indeed a martingale under P∗we need in fact to verify
the stronger condition
E∗

e−rtS(t)|S(u)

= e−ruS(u)
(8.7)
for any t ≥u ≥0, involving the conditional expectation of e−rtS(t) given S(u).
So far we have dealt with conditional expectation where the condition was
given in terms of a discrete random variable, see Section 3.2.2. Here, however,
the condition is expressed in terms of S(u), a random variable with continuous
distribution. In this case the precise mathematical meaning of (8.7) is that for
every a > 0
E∗

e−rtS(t)1S(u)<a

= E∗

e−ruS(u)1S(u)<a

,
(8.8)
where 1S(u)<a is the indicator random variable, equal to 1 if S(u) < a and to 0
if S(u) ≥a.
Exercise 8.13
Verify equality (8.8).
Exercise 8.14
Find the density of W(t) under the risk-neutral probability P∗.

188
Mathematics for Finance
Above we have identified the risk-neutral probability P∗. Now we shall con-
sider a European call option on the stock with strike price X to be exercised
at time T. The general formula (8.6) for the price of an option becomes
CE(0) = E∗

e−rT (S(T) −X)+
.
Let us compute this expectation. Because V (T) = W(t) +

m −r + 1
2σ2 t
σ for
t ≥0 is a Wiener process under P∗, the random variable V (T) = W(T) +

m −r + 1
2σ2 T
σ is normally distributed with mean 0 and variance T, that is,
it has density
1
√
2πT e−x2
2T . As a result,
CE(0) = E∗

e−rT (S(T) −X)+
= E∗
	
S(0)eσV (t)−1
2 σ2T −Xe−rT +
=
$ ∞
−d2
√
T

S(0)eσx−1
2 σ2T −Xe−rT 
1
√
2πT
e−x2
2T dx
= S(0)
$ ∞
−d1
1
√
2π e−y2
2 dy −Xe−rT
$ ∞
−d2
1
√
2π e−y2
2 dy
= S(0)N(d1) −Xe−rT N(d2),
where
d1 = ln S(0)
X
+

r + 1
2σ2
T
σ
√
T
,
d2 = ln S(0)
X
+

r −1
2σ2
T
σ
√
T
,
(8.9)
and where
N(x) =
$ x
−∞
1
√
2π e−y2
2 dy =
$ ∞
−x
1
√
2π e−y2
2 dy
(8.10)
is the normal distribution function.
What we have just derived is the celebrated Black–Scholes formula for Eu-
ropean call options. The choice of time 0 to compute the price of the option
is arbitrary. In general, the option price can be computed at any time t < T,
in which case the time remaining before the option is exercised will be T −t.
Substituting t for 0 and T −t for T in the above formulae, we thus obtain the
following result.
Theorem 8.6 (Black–Scholes Formula)
The time t price of a European call with strike price X and exercise time T,
where t < T, is given by
CE(t) = S(t)N(d1) −Xe−r(T −t)N(d2)

8. Option Pricing
189
with
d1 = ln S(0)
X
+

r + 1
2σ2
(T −t)
σ
√
T −t
,
d2 = ln S(0)
X
+

r −1
2σ2
(T −t)
σ
√
T −t
.
(8.11)
Exercise 8.15
Derive the Black–Scholes formula
P E(t) = Xe−r(T −t)N(−d2) −S(t)N(−d1),
with d1 and d2 given by (8.11), for the price of a European put with
strike X and exercise time T.
Remark 8.2
Observe that the Black–Scholes formula contains no m. It is a property anal-
ogous to that in Remark 8.1, and of similar practical significance: There is no
need to know m to work out the price of a European call or put option in
continuous time.
It is interesting to compare the Black–Scholes formula for the price of a
European call with the Cox–Ross–Rubinstein formula. There is close analogy
between the terms. Apart from the obvious correspondence between the con-
tinuous and discrete time discount factors e−rT and (1 + r)−N, the binomial
and normal distribution terms appearing in these formulae are also related
to one another. The precise relationship comes from a version of the Central
Limit Theorem: It can be shown that the option price given by the Cox–Ross–
Rubinstein formula tends to that in the Black–Scholes formula in the continuous
time limit described in Chapter 3.
Figure 8.2
Option price CE in continuous and discrete time models as a
function of time T remaining before the option is exercised

190
Mathematics for Finance
Rather than looking at the details of this limit, we just refer to Figure 8.2
for illustration. It shows the price CE of a European call with strike X = 100
on a stock with S(0) = 100, σ = 0.3 and m = 0.2. (Though m is irrelevant for
the Black–Scholes formula, it still features in the discrete time approximation.)
The continuous compounding interest rate is taken to be r = 0.2. The option
price is computed in two ways, as a function of the time T remaining before
the option is exercised:
a) (solid line) from the Black–Scholes formula for T between 0 and 1;
b) (dots) using the Cox–Ross–Rubinstein formula with T increasing from 0
to 1 in N = 10 steps of duration τ = 0.1 each; the discrete growth rates for
each step are computed using formulae (3.7).
Even with as few as 10 steps there is remarkably good agreement between the
discrete and continuous time formulae.

9
Financial Engineering
This chapter shows some applications of derivative securities to managing the
risk exposure in various situations. The presentation will be by means of exam-
ples and mini case studies. Even though these are concerned with very particu-
lar circumstances, the methods are applicable to a wide range of tasks handled
by financial managers.
First, we shall present methods for eliminating or reducing the risk involved
in writing options. This is a problem faced by financial institutions who issue
and sell derivative securities, but may not wish to bear the accompanying risk.
Such institutions are typically satisfied by the commission charged for their
services, without taking an active position in the market.
Next, we shall analyse methods of reducing undesirable risk stemming from
certain business activities. Our case studies will be concerned with foreign ex-
change risk. It is possible to deal in a similar way with the risk resulting from un-
expected future changes of various market variables such as commodity prices,
interest rates or stock prices. We shall introduce a measure of risk called Value
at Risk (VaR), which has recently become very popular. Derivative securities
will be used to design portfolios with a view to reducing this kind of risk.
Finally, we shall consider an application of options to manufacturing a lev-
ered investment, for which increased risk will be accompanied by high expected
return.
191

192
Mathematics for Finance
9.1 Hedging Option Positions
The writer of a European call option is exposed to risk, as the option may end
up in the money. The risk profile for a call writer is CEerT −(S(T)−X)+, where
CEerT is the value at the exercise time T of the premium CE received for the
option and invested without risk. Theoretically, the loss to the writer may be
unlimited. For a put option the risk profile has the form P EerT −(X −S(T))+,
with limited loss, though still possibly very large compared to the premium P E
received. We shall see how to eliminate or at least reduce this risk over a
short time horizon by taking a suitable position in the underlying asset and, if
necessary, also in other derivative securities written on the same asset.
In practice it is impossible to hedge in a perfect way by designing a single
portfolio to be held for the whole period up to the exercise time T. The hedging
portfolio will need to be modified whenever the variables affecting the option
change with time. In a realistic case of non-zero transaction costs these mod-
ifications cannot be performed too frequently and some compromise strategy
may be required. Nevertheless, here we shall only discuss hedging over a single
short time interval, neglecting transaction costs.
9.1.1 Delta Hedging
The value of a European call or put option as given by the Black–Scholes
formula clearly depends on the price of the underlying asset. This can be seen
in a slightly broader context.
Consider a portfolio whose value depends on the current stock price S =
S(0) and is hence denoted by V (S). Its dependence on S can be measured
by the derivative
d
dS V (S), called the delta of the portfolio. For small price
variations from S to S + ∆S the value of the portfolio will change by
∆V (S) ∼= d
dS V (S) × ∆S.
The principle of delta hedging is based on embedding derivative securities in a
portfolio, the value of which does not alter too much when S varies. This can
be achieved by ensuring that the delta of the portfolio is equal to zero. Such a
portfolio is called delta neutral.
We take a portfolio composed of stock, bonds and the hedged derivative
security, its value given by
V (S) = xS + y + zD(S),
where the derivative security price is denoted by D(S) and a bond with current
value 1 is used. Specifically, suppose that a single derivative security has been

9. Financial Engineering
193
written, that is, z = −1. Then
d
dS V (S) = x −d
dS D(S).
The last term
d
dS D(S), which is the delta of the derivative security, can readily
be computed if the model of stock prices is specified, so that an explicit formula
for D(S) is available.
Proposition 9.1
Denote the European call option price in the Black–Scholes model by CE(S).
The delta of the option is given by
d
dS CE(S) = N(d1),
where N(x) is the normal distribution function given by (8.10) and d1 is defined
by (8.9).
Proof
The price S = S(0) appears in three places in the Black–Scholes formula, see
Theorem 8.6, so the differentiation requires a bit of work, with plenty of nice
cancellations in due course, and is left to the reader. Bear in mind that the
derivative
d
dS CE(S) is computed at time t = 0.
Exercise 9.1
Find a similar expression for the delta
d
dS P E(S) of a European put option
in the Black–Scholes model.
For the remainder of this section we shall consider a European call option
within the Black–Scholes model. By Proposition 9.1 the portfolio (x, y, z) =
(N(d1), y, −1), where the position in stock N(d1) is computed for the initial
stock price S = S(0), has delta equal to zero for any money market position y.
Consequently, its value
V (S) = N(d1)S + y −CE(S)
does not vary much under small changes of the stock price about the initial
value. It is convenient to choose y so that the initial value of the portfolio is
equal to zero. By the Black–Scholes formula for CE(S) this gives
y = −Xe−T rN(d2),

194
Mathematics for Finance
with d2 is given by (8.9).
Let us analyse the following example, which will subsequently be expanded
and modified. Suppose that the risk-free rate is 8% and consider a 90-day call
option with strike price X = 60 dollars written on a stock with current price
S = 60 dollars. Assume that the stock volatility is σ = 30%. The Black–Scholes
formula gives the option price CE = 4.14452 dollars, the delta of the option
being equal to 0.581957.
Suppose that we write and sell 1, 000 call options, cashing a premium of
$4, 144.52. To construct the hedge we buy 581.96 shares for $34, 917.39, borrow-
ing $30, 772.88. Our portfolio will be (x, y, z) with x = 581.96, y = −30, 772.88,
z = −1, 000 and with total value zero. (While it might be more natural math-
ematically to consider a single option with z = −1, in practice options are
traded in batches.)
We shall analyse the value of the portfolio after one day by considering some
possible scenarios. The time to expiry will then be 89 days. Suppose that the
stock volatility and the risk-free rate do not vary, and consider the following
three scenarios of stock price movements:
1. The stock price remains unaltered, S( 1
365) = 60 dollars. A single option is
now worth $4.11833, so our liability due to the short position in options is
reduced. Our debt on the money market is increased by the interest due.
The position in stock is worth the same as initially. The balance on day one
is
stock
34, 917.39
money
−30, 779.62
options
−4, 118.33
TOTAL
19.45
Without hedging (x = 0, y = 4, 118.33, z = −1, 000) our wealth would have
been $27.10, that is, we would have benefited from the reduced value of the
option and the interest due on the premium invested without risk.
2. The stock price goes up to S( 1
365) = 61 dollars. A single option is now worth
$4.72150, which is more than initially. The unhedged (naked) position would
have suffered a loss of $576.07. On the other hand, for a holder of a delta
neutral portfolio the loss on the options is almost completely balanced out
by the increase in the stock value:
stock
35, 499.35
money
−30, 779.62
options
−4, 721.50
TOTAL
−1.77

9. Financial Engineering
195
3. The stock price goes down to S( 1
365) = 59 dollars. The value of the written
options decreases, a single option now being worth $3.55908. The value of
the stock held decreases too. The portfolio brings a small loss:
stock
34, 335.44
money
−30, 779.62
options
−3, 559.08
TOTAL
−3.26
In this scenario it would have been much better not to have hedged at all,
since then we would have gained $586.35.
It may come as a surprise that the hedging portfolio brings a profit when the
stock price remains unchanged. As we shall see later in Exercise 9.5, a general
rule is at work here.
Exercise 9.2
Find the stock price on day one for which the hedging portfolio attains
its maximum value.
Exercise 9.3
Suppose that 50, 000 puts with exercise date in 90 days and strike price
X = 1.80 dollars are written on a stock with current price S(0) = 1.82
dollars and volatility σ = 14%. The risk-free rate is r = 5%. Construct a
delta neutral portfolio and compute its value after one day if the stock
price drops to S( 1
365) = 1.81 dollars.
Going back to our example, let us collect the values V of the delta neutral
portfolio for various stock prices after one day as compared to the values U of
the unhedged position:
S
V
U
58.00
−71.35
1, 100.22
58.50
−31.56
849.03
59.00
−3.26
586.35
59.50
13.69
312.32
60.00
19.45
27.10
60.50
14.22
−269.11
61.00
−1.77
−576.07
61.50
−28.24
−893.53
62.00
−64.93
−1, 221.19

196
Mathematics for Finance
Now, let us see what happens if the stock price changes are considerable:
S
V
U
50
−2, 233.19
3, 594.03
55
−554.65
2, 362.79
60
19.45
27.10
65
−481.60
−3, 383.73
70
−1, 765.15
−7, 577.06
If we fear that such large changes might happen, the above hedge is not a
satisfactory solution. If we do not hedge, at least we have a gamble with a
positive outcome whenever the stock price goes down. Meanwhile, no matter
whether the stock price goes up or down, the delta neutral portfolio may bring
losses, though considerably smaller than the naked position.
Let us see what can happen if some other variables, in addition to the stock
price, change after one day:
1. Suppose that the interest rate increases to 9% with volatility as before.
Some loss will result from an increase in the option value. The interest on
the cash loan due on day one is not affected because the new rate will only
have an effect on the interest payable on the second day or later. The values
of the hedging portfolio are given in the second column in the table below.
2. Now suppose that σ grows to 32%, with the interest rate staying at the
original level of 8%. The option price will increase considerably, which is
not compensated by the stock position even if the stock price goes up. The
results are given in the third column in the following table:
V
S
r = 9%, σ = 30%
r = 8%, σ = 32%
58.00
−133.72
−299.83
58.50
−97.22
−261.87
59.00
−72.19
−234.69
59.50
−58.50
−218.14
60.00
−55.96
−212.08
60.50
−64.38
−216.33
61.00
−83.51
−230.68
61.50
−113.07
−254.90
62.00
−152.78
−288.74

9. Financial Engineering
197
As we can see, in some circumstances delta hedging may be far from satis-
factory. We need to improve the stability of hedging when the underlying asset
price changes considerably and/or some other variables change simultaneously.
In what follows, after introducing some theoretical tools we shall return again
to the current example.
Exercise 9.4
Find the value of the delta neutral portfolio in Exercise 9.3 if the risk-free
rate of interest decreases to 3% on day one.
9.1.2 Greek Parameters
We shall define so-called Greek parameters describing the sensitivity of a port-
folio with respect to the various variables determining the option price. The
strike price X and expiry date T are fixed once the option is written, so we
have to analyse the four remaining variables S, t, r, σ.
Let us write the value of a general portfolio containing stock and some
contingent claims based on this stock as a function V (S, t, σ, r) of these variables
and denote
deltaV = ∂V
∂S ,
gammaV = ∂2V
∂S2 ,
thetaV = ∂V
∂t ,
vegaV = ∂V
∂σ ,
rhoV = ∂V
∂r .
For small changes ∆S, ∆t, ∆σ, ∆r of the variables we have the following
approximate equality (by the Taylor formula):
∆V ∼= deltaV × ∆S + thetaV × ∆t + vegaV × ∆σ + rhoV × ∆r
+ 1
2gammaV × (∆S)2.
Hence, a way to immunise a portfolio against small changes of a particular vari-
able is to ensure that the corresponding Greek parameter is equal to zero. For
instance, to hedge against volatility movements we should construct a vega neu-
tral portfolio, with vega equal to zero. To retain the benefits of delta hedging,

198
Mathematics for Finance
we should design a portfolio with both delta and vega equal to zero (delta-
vega neutral). A delta-gamma neutral portfolio will be immune against larger
changes of the stock price. Examples of such hedging portfolios will be exam-
ined below.
The Black–Scholes formula allows us to compute the derivatives explicitly
for a single option. For a European call we have
deltaCE = N(d1),
gammaCE =
1
Sσ
√
2πT
e−
d2
1
2 ,
thetaCE = −
Sσ
2
√
2πT
e−
d2
1
2 −rXe−rT N(d2),
vegaCE = S
√
T
√
2π e−
d2
1
2 ,
rhoCE = TXe−rT N(d2).
(The Greek parameters are computed at time t = 0.)
Remark 9.1
It is easy to see from the above that
thetaCE + rS deltaCE + 1
2σ2S2gammaCE = rCE.
In general, the price D of any European derivative security can be shown to
satisfy the Black–Scholes equation
∂D
∂t + rS ∂D
∂S + 1
2σ2S2 ∂2D
∂S2 = rD.
Exercise 9.5
Show that a delta neutral portfolio with initial value zero hedging a
single call option will gain in value with time if the stock price, volatility
and risk-free rate remain unchanged.
Exercise 9.6
Derive formulae for the Greek parameters of a put option.

9. Financial Engineering
199
9.1.3 Applications
To show some possibilities offered by Greek parameters we consider hedging
the position of a writer of European call options.
Delta-Gamma Hedging. The construction is based on making both delta
and gamma zero. A portfolio of the form (x, y, z) is insufficient for this. Given
the position in options, say z = −1, 000, there remains only one parameter
that can be adjusted, namely the position x in the underlying. This allows us
to make the delta of the portfolio zero. To make the gamma also equal to zero
an additional degree of freedom is needed. To this end we consider another
option on the same underlying stock, for example, a call expiring after 60 days,
%T = 60/365, with strike price %
X = 65, and construct a portfolio (x, y, z, %z),
where %z is a position in the additional option. The other variables are as in the
previous examples: r = 8%, σ = 30%, S(0) = 60.
Let us sum up all the information about the prices and selected Greek
parameters (we also include vega, which will be used later):
option
time to
strike
option
delta
gamma
vega
expiry
price
price
original
90/365
60
4.14452
0.581957
0.043688
11.634305
additional
60/365
65
1.37826
0.312373
0.048502
8.610681
We choose x and %z so that the delta and gamma of the portfolio are zero,
deltaV = x −1, 000 deltaCE + %z delta %CE = 0,
gammaV = −1, 000 gammaCE + %z gamma %CE = 0,
and the money position y so that the value of the portfolio is zero,
V (S) = xS + y −1, 000CE(S) + %z %CE(S) = 0.
This gives the following system of equations:
x −581.957 + 0.312373 %z = 0,
−43.688 + 0.048502 %z = 0,
with solution x ∼= 300.58, %z ∼= 900.76. It follows that y ∼= −15, 131.77. That
is, we take long positions in stock and the additional option, and a short cash
position. (We already have a short position z = −1, 000 in the original option.)
After one day, if stock goes up, the original option will become more expen-
sive, increasing our liability, which will be set offby increases in the value of
stock and the additional options held. The reverse happens if the stock price
declines. Our money debt increases in either case by the interest due after one

200
Mathematics for Finance
day. The values of the portfolio are given below (for comparison we also recall
the values of the delta neutral portfolio):
S( 1
365)
delta-gamma
delta
58.00
−2.04
−71.35
58.50
0.30
−31.56
59.00
1.07
−3.26
59.50
0.81
13.69
60.00
0.02
19.45
60.50
−0.79
14.22
61.00
−1.11
−1.77
61.50
−0.49
−28.24
62.00
1.52
−64.93
We can see that we are practically safe within the given range of stock prices.
For larger changes we are also in a better position as compared with delta
hedging:
S( 1
365)
delta-gamma
delta
50
−614.08
−2, 233.19
55
−78.22
−554.65
60
0.02
19.45
65
63, 13
−481.60
70
440.81
−1, 765.15
As predicted, a delta-gamma neutral portfolio offers better protection against
stock price changes than a delta neutral one.
Delta-Vega Hedging. Next we shall hedge against an increase in volatility,
while retaining cover against small changes in the stock price. This will be
achieved by constructing a delta-vega neutral portfolio containing, as before,
an additional option. The conditions imposed are
deltaV = x −1, 000 deltaCE + %z delta %CE = 0,
vegaV = −1, 000 vegaCE + %z vega %CE = 0.
They lead to the system of equations
x −581.957 + 0.312373 %z = 0,
−1, 1634.305 + 8.610681 %z = 0,
with an approximate solution x ∼= 159. 89, %z ∼= 1, 351.15. The corresponding
money position is y ∼= −7, 311.12.

9. Financial Engineering
201
Suppose that the volatility increases to σ = 32% on day one. Let us compare
the results for delta-vega and delta hedging:
S(1/365)
delta-vega
delta
58.00
−5.90
−299.83
58.50
−12.81
−261.87
59.00
−16.05
−234.69
59.50
−14.99
−218.14
60.00
−9.06
−212.08
60.50
2.27
−216.33
61.00
19.52
−230.68
61.50
43.17
−254.90
62.00
73.62
−288.74
Exercise 9.7
Using the data in our ongoing example (stock price $60, volatility 30%,
interest rate 8%), construct a delta-rho neutral portfolio to hedge a short
position of 1, 000 call options expiring after 90 days with strike price $60,
taking as an additional component a call option expiring after 120 days
with strike price $65. Analyse the sensitivity of the portfolio value to
stock price variations if the interest rate goes up to 9% after one day,
comparing with the previous results. What will happen if the interest
rate jumps to 15%?
The examples above illustrate the variety of possible hedging strategies. The
choice between them depends on individual aims and preferences. We have not
touched upon questions related to transaction costs or long term hedging. Nor
have we discussed the optimality of the choice of an additional derivative instru-
ment. Portfolios based on three Greek parameters would require yet another
derivative security as a component. They could provide comprehensive cover,
though their performance might deteriorate if the variables remain unchanged.
In addition, they might prove expensive if transaction costs were included.
9.2 Hedging Business Risk
We begin by introducing an alternative measure of risk, related to an intuitive
understanding of risk as the size and likelihood of a possible loss.


## Financial Engineering

202
Mathematics for Finance
9.2.1 Value at Risk
Let us present the basic idea using a simple example. We buy a share of stock for
S(0) = 100 dollars to sell it after one year. The selling price S(1) is random. We
shall suffer a loss if S(1) < 100er, where r is the risk-free rate under continuous
compounding. (The purchase can either be financed by a loan, or, if the initial
sum is already at our disposal, we take into account the foregone opportunity
of a risk-free investment.) What is the probability of a loss being less than a
given amount, for example,
P(100er −S(1) < 20) = ?
Let us reverse the question and fix the probability, 95% say. Now we seek an
amount such that the probability of a loss not exceeding this amount is 95%.
This is referred to as Value at Risk at 95% confidence level and denoted by
VaR. (Other confidence levels can also be used.) So, VaR is an amount such
that
P(100er −S(1) < VaR) = 95%.
It should be noted that the majority of textbooks neglect the time value of
money in this context, stating the definition of VaR only for r = 0.
Example 9.1
Suppose that the distribution of the stock price is log normal, the logarithmic
return k = ln(S(1)/S(0)) having normal distribution with mean m = 12%
and standard deviation σ = 30%. With probability 95% the return will satisfy
k > m + xσ ∼= −37.50%, where N(x) ∼= 5%, so x ∼= −1.645. (Here N(x) is the
normal distribution function (8.10) with mean 0 and variance 1.) Hence with
probability 95% the future price S(1) will satisfy
S(1) > S(0)em+xσ ∼= 68.83 dollars,
and so, given that r = 8%,
VaR = S(0)er −S(0)em+xσ ∼= 39.50 dollars.
Exercise 9.8
Evaluate VaR at 95% confidence level for a one-year investment of $1, 000
into euros if the interest rate for risk-free investments in euros is rEUR =
4% and the exchange rate from euros into US dollars follows the log
normal distribution with m = 1% and σ = 15%. Take into account the
foregone opportunity of investing dollars without risk, given that the
risk-free interest rate for dollars is rUSD = 5%.

9. Financial Engineering
203
Exercise 9.9
Suppose that $1, 000 is invested in European call options on a stock
with current price S(0) = 60 dollars. The options expire after 6 months
with strike price X = 40 dollars. Assume that σ = 30%, r = 8%, and
the expected logarithmic return on stock is 12%. Compute VaR after
6 months at 95% confidence level. Find the final wealth if the stock
price grows at the expected rate. Find the stock price level that will
be exceeded with 5% probability and compute the corresponding final
payoff.
9.2.2 Case Study
We shall discuss a number of ways in which VaR can be managed with the aid
of derivative securities. The methods will be illustrated by a simple example of
business activity.
Case 9.1
A company manufactures goods in the UK for sale in the USA. The investment
to start production is 5 million pounds. Additional funds can be raised by
borrowing British pounds at 16% to finance a hedging strategy. The rate of
return demanded by investors, bearing in mind the risk involved, is 25%. The
sales are predicted to generate 8 million dollars at the end of the year. The
manufacturing costs are 3 million pounds per year. The interest rate is 8%
for dollars and 11% for pounds. The current rate of exchange is 1.6 dollars to
a pound. The volatility of the logarithmic return on the rate of exchange is
estimated at 15%. The company pays 20% tax on earnings.
First note that to satisfy the expectations of investors the company should
be able to achieve a profit of 1.25 million pounds a year to pay the dividend. A
lower profit would mean a loss. The profit depends on the rate of exchange d
at the end of the year, hence some risk emerges. (We assume that the other
values will be as predicted.)
To begin with, suppose that no action is taken to manage the risk.
1. Unhedged Position. If the exchange rate d turns out to be 1.6 dollars to
a pound at the end of the year, then the net earnings will be 1.6 million
pounds, as shown in the following profit and loss statement (all amounts in

204
Mathematics for Finance
pounds):
sales
5, 000, 000
cost of sales
−3, 000, 000
earnings before tax
2, 000, 000
tax
−400, 000
earnings after tax
1, 600, 000
dividend
−1, 250, 000
result
350, 000
The surplus income will be 0.35 million pounds.
However, if the exchange rate d becomes 2 dollars to a pound, the com-
pany will end up with a loss of 0.45 million pounds (and the dividend will
in fact have to be reduced):
sales
4, 000, 000
cost of sales
−3, 000, 000
earnings before tax
1, 000, 000
tax
−200, 000
earnings after tax
800, 000
dividend
−1, 250, 000
result
−450, 000
Let us compute VaR. We assume that the rate of exchange has log-
normal distribution with mean return equal to the difference between the
interest rates, 8% −11% = −3%.1 With the volatility of the return on
the exchange rate at 15%, the return on the investment will exceed −3% +
1.65×15% = 21.75% with probability 95%. This corresponds to an exchange
rate d = 1.6 × e21.75% ∼= 1.9887 dollars to a pound, for which the income
statement will be as follows (all amounts rounded to the nearest pound):
sales
4, 022, 728
cost of sales
−3, 000, 000
earnings before tax
1, 022, 728
tax
−204, 546
earnings after tax
818, 182
dividend
−1, 250, 000
result
−431, 818
1 This assumption can be justified as follows: If a pound is invested without risk
for one year and then converted to dollars at a rate d known in advance, to avoid
arbitrage we should have d × e11% = 1.6 × e8%, so d = 1.6 × e−3%. This gives −3%
logarithmic return on the exchange rate. For a random exchange rate it is therefore
natural to assume the mean logarithmic return to be −3%.

9. Financial Engineering
205
As a result, VaR ∼= 431, 818 dollars. The final balance as a function of the
exchange rate d is
b(d) = 80% × (8, 000, 000
d
−3, 000, 000) −1, 250, 000
= 6, 400, 000
d
−3, 650, 000.
The break even exchange rate, which solves b(d) = 0, is approximately equal
to 1.7534 dollars to a pound. In an optimistic scenario in which the pound
weakens, for example, down to 1.5 dollars, the final balance will be about
£616, 666.
The question is how to manage this risk exposure.
2. Forward Contract. The easiest solution would be to fix the exchange
rate in advance by entering into a long forward contract. The forward rate
is 1.6 × e−3% ∼= 1.5527 dollars to a pound. As a result, the company can
obtain the following statement with guaranteed surplus, but no possibility
of further gains should the exchange rate become more favourable:
sales
5, 152, 315
cost of sales
−3, 000, 000
earnings before tax
2, 152, 315
tax
−430, 463
net income
1, 721, 852
dividend
−1, 250, 000
result
471, 852
3. Full Hedge with Options. Options can be used to ensure that the rate
of exchange is capped at a certain level, whilst the benefits associated with
favourable exchange rate movements are retained. However, this may be
costly because of the premium paid for options.
The company can buy call options on the exchange rate. A European
call to buy one pound with strike price 1.6 dollars to a pound will cost
£0.0669.2 Suppose that the company buys 5 million of such options, paying
a £334, 510 premium, which they have to borrow at 16%. The interest is
tax deductible, making the loan less costly. Nevertheless, the final result is
2 For options on currencies the Black–Scholes formula has to be modified by replacing
the risk-free interest rate r by the difference between the risk-free rates for the
currencies, in our case: −3%.

206
Mathematics for Finance
disappointing:
sales
5, 000, 000
cost of sales
−3, 000, 000
earnings before interest and tax
2, 000, 000
interest
−53, 522
earnings before tax
1, 946, 478
tax
−389, 296
net income
1, 557, 182
loan repaid
−334, 510
dividend
−1, 250, 000
result
−27, 328
The optimal (in the sense of minimising the loss) strike price is 1.5734
dollars to a pound, resulting in a loss of £24, 283. If the exchange rate
drops to 1.5 dollars to a pound, the options will not be exercised and the
sum obtained from sales will reach £5, 333, 333, with a positive final result
of £239, 339. This strategy leads to a better result than the hedge involving
a forward contract only if the rate of exchange drops below 1.42 dollars to
a pound.
4. Partial Hedge with Options. To reduce the cost of options the company
can hedge partially by buying call options to cover only a fraction of the
dollar amount from sales. Suppose that the company buys 2, 500, 000 units
of the same call option as above, paying a half of the previous premium. A
half of the revenue is then exposed to risk. To find VaR at 95% confidence
level we assume that this sum is exchanged at 1.9887 dollars to a pound, as
in the case of an unhedged position, the other half being exchanged at the
exercise price:
sales
4, 511, 364
cost of sales
−3, 000, 000
earnings before interest and tax
1, 511, 364
interest
−26, 761
earnings before tax
1, 484, 603
tax
−296, 921
net income
1, 187, 682
loan repaid
−167, 255
dividend
−1, 250, 000
result
−229, 573
If the exchange rate drops to 1.5 dollars to a pound, the company will have
a surplus of £428, 003.

9. Financial Engineering
207
5. Combination of Options and Forward Contracts. Finally, let us inves-
tigate what happens if the company hedges with both kinds of derivatives.
Half of their position will be hedged with options. In the worst case sce-
nario they will buy pounds for half of their dollar revenue at the rate of
1.6 dollars to a pound, the remaining half being exchanged at the forward
rate of 1.5527 dollars to a pound. The outcome is shown below, where we
summarise the resulting VaR for all strategies considered (the result below
is equal to minus VaR):
strategy
1
2
3
4
5
result
−431, 818
471, 852
−27, 328
−229, 573
222, 263
These values are computed at 95% confidence level, corresponding to the
exchange rate of 1.9887 dollars to a pound.
Clearly, VaR provides only partial information about possible outcomes of
various strategies. Figure 9.1 shows the graphs of the final result as a function
of the exchange rate d for each of the above strategies. The graphs are labelled
by the strategy number as above. The strategy using a forward contract (strat-
Figure 9.1
Comparison of various strategies
egy 2) appears to be the safest one. An adventurous investor who strongly
believes that the pound will weaken considerably may prefer to remain uncov-
ered (strategy 1). A variety of middle-of-the-road strategies are also available.
The probability distribution of the exchange rate d should also be taken into
account when examining the graphs.

208
Mathematics for Finance
9.3 Speculating with Derivatives
9.3.1 Tools
Options can be used as building blocks to design sophisticated investment in-
struments. We shall consider an investor with specific views on the future be-
haviour of stock prices and willing to take risks. Our task will be to design a
portfolio of securities with a prescribed payoffprofile that would satisfy this
kind of investor.
Suppose that the investor expects the stock price to rise and wants to gamble
on that. One simple way is to buy a call option. An option with strike price X′
close to the current stock price is considerably cheaper than the stock itself,
creating a risky leverage position, as will be seen in the case study to follow. The
premium may be reduced by selling a call option with strike price X′′ > X′. In
this way we can build a so-called bull spread with payoffshown in Figure 9.2.
This strategy will bring a good return if stock price increases are moderate.
Figure 9.2
Bull spread
Using put options with strike prices X′ < X′′, selling the former and pur-
chasing the latter, we can construct a bear spread with positive payofffor low
future stock prices, see Figure 9.3. This may be employed by an investor who
expects a moderate decline in the stock price.
Figure 9.3
Bear spread
An investor who believes that the stock price will stay unaltered or change
insignificantly may choose a butterfly. It is constructed from three call options
with strike prices X′ < X′′ < X′′′. Two calls are bought, one with strike X′
and one with strike X′′′, and two calls with strike price X′′ are sold. Figure 9.4

9. Financial Engineering
209
shows the case when X′′ is the average of the other two strike prices. Reversed
butterfly is the opposite strategy, bringing profits when the stock price changes.
(We have already come across the butterfly in the proof of Proposition 7.8.)
Figure 9.4
Butterfly
Finally, we observe that any continuous payofffunction consisting of straight
line segments can be manufactured from put and call options. Figure 9.5 out-
lines the step-by-step decomposition of a target profile into a portfolio of op-
tions with various strike price values. The number of options for each strike
price is chosen to match the slopes of the target profile. Such a construction is
sufficient for practical purposes because any continuous payofffunction can be
approximated by straight line segments.
9.3.2 Case Study
We shall combine the portfolio theory techniques with the tools described
above. We have in mind an investor with specific views on the future prices
of assets, who is prepared to accept some risk in order to increase expected
return.
Case 9.2
An investor with $15, 000 believes that a certain stock price should rise during
the next month, with expected annualised return µS = 31%. The current stock
price is S(0) = 60 dollars. Call options expiring in 20 days with strike price $60
are available at $2.112. The effective risk-free rate is 12%.
To analyse this case we shall use the binomial model, assuming that trading
takes place once a day and that the market probabilities are the same for up

210
Mathematics for Finance
Figure 9.5
Decomposition of a target payoffinto options
and down price jumps. We also assume for simplicity that there are 360 days in
a year. The risk-free return over 20 days is rF ∼= 0.6316%. (Implied by the effec-
tive rate of 12%.) The $15, 000 invested without risk would become $15, 094.74
at the end of the 20-day period. Consider the following risky investments:
1. Stock. An investment in stock should bring an expected return of µS ∼=
1.5115%. (Equivalent to 31% annually.) Buying 250 shares, the investor
would expect to end up with $15, 226.72 after 20 days. The risk can be
estimated from the option price, see below.
2. Call Options. A more risky alternative is to buy call options. The return

9. Financial Engineering
211
is random and depends on the stock price after 20 days,
KC = (S(20/365) −60)+ −C
C
.
To compute the expected return on an option we can find the parameters
of the binomial model consistent with the option price and the expected
return on stock, assuming that the market probability of up and down
price movements is 1/2. First we find the risk-free return over a single day,
r = (1 + 12%)
1
360 −1 ∼= 0.0315%.
Then we write down a condition on the up and down daily stock returns
such that the expected annual return is 31%,
u + d
2
= (1 + 31%)
1
360 −1 ∼= 0.075%.
The call price gives another condition for u and d, and we finally arrive at
the following values:3
u ∼= 1.85%,
d ∼= −1.70%.
Now we can compute the standard deviation for the period in question
(using the actual market probabilities pk =
20
k

0.520, k = 0, 1, . . . , 20),
σS ∼= 8.0962%.
Finally, we compute the expected return and risk of the investment in op-
tions,
µC ∼= 14.1268%,
σC ∼= 153.006%.
The return is impressive, but so is the risk. Observe that with probability
0.4119 the investor can lose all his or her money.
3. Forward Contracts. The forward price is approximately $60.38. Suppose
that entering into a forward contract requires a 20% deposit of the initial
stock price, that is $12 per share. The investor can afford to enter into 1, 250
forward contracts. The expected return and risk in the binomial model are
µF ∼= 4.3993%,
σF ∼= 40.4811%.
Note that if the stock price falls below $48.38, the investor will lose the
deposit and suffer an additional loss, resulting in a return below −100%.
3 Take any value of u, compute the corresponding 21 stock price values after 20 days,
the option payoffs, risk-neutral probability, and finally the option price. Using the
Goal Seek facility in a spreadsheet application (or trial and error), find the value
of u such that the option price is as given.

212
Mathematics for Finance
4. Options Combined with Risk-Free Investment. The risk can be ad-
justed to an arbitrary level if options are combined with a risk-free asset.
Suppose that the investor is willing to accept similar risk to the stock in-
vestment. Investing 94.77% of the capital without risk and the remainder in
options, the investor can construct a portfolio with the same standard devi-
ation as that for the stock. The expected return on the portfolio is slightly
lower than that on stock,
µP ∼= 1.3457%,
σP ∼= 8.0962%.
Remark 9.2
The slope of the line connecting the risk-free asset F with any other portfolio A
on the (σ, µ) plane is given by µA−rF
σA
, called the market price of risk. It can
be used to compare different portfolios: Those with steep slope are preferable.
We can see that the above risky investments have similar values of the market
price of risk, about 0.1 in each case. (These values would in fact be identical if
the Black–Scholes model were used for stock prices.)
The advantage of the investment in a portfolio of options and risk-free
assets can be seen if we consider VaR, given in the table below for two different
confidence levels (chosen to be compatible with the probabilities in the binomial
model). On the other hand, VaR would be disastrously high if the whole amount
were invested only in options: The investor could lose everything at the given
confidence levels.
Investment
Stock
Call options
Forwards
Calls with
risk-free asset
Market price
of risk
0.1087
0.0882
0.0931
0.0882
VaR at 94.23%
$1, 931.78
$15, 000.00
$9, 753.63
$798.73
VaR at 99.41%
$2, 836.84
$15, 000.00
$14, 278.95
$798.73
Case 9.3
An analyst researching the company has come to the conclusion that the stock
price after 20 days will not fall below $58 or raise above $66. All market pa-
rameters remain as in Case 9.2. From the point of view of the analyst, compare
the expected return and risk for stock, options and a bull spread with strike
prices $58 and $62.

9. Financial Engineering
213
We shall build a simple model reflecting the analysts’s point of view. Addi-
tional information obtained by the analyst will result in modified probabilities
as compared to the market probability P. (We assume, as before, that the
market probability of up and down movements is 1/2 in each step.) Namely,
the probability Q assigned by the analyst will be the market probability P
conditioned by the event 58 ≤S(20) ≤62. In particular,
Q(S(20) = x) = P(S(20) = x|58 ≤S(20) ≤62)
=
&
P (S(20)=x)
P (58≤S(20)≤62)
if 58 ≤x ≤62,
0
if x < 50 or x > 62.
As a result, the analyst will arrive at the following values:
1. Stock. Under the modified probability Q
µS ∼= 2.6788%,
σS ∼= 3.9257%.
2. Call Options. Take a call with strike price X = 58 dollars. Hence
CE ∼= 3.2923 dollars (this price is found in the binomial model without any
restriction on the range of stock prices after 20 days). For an investment in
options we find that
µC ∼= 8.8816%,
σC ∼= 71.095%.
3. Bull Spread. Construct the spread by purchasing a call with strike $58
and selling a call with strike $60. The premium received for the latter is
$2.10, hence a single spread costs $1.18. The expected return and risk are
µbull ∼= 38.4094%,
σbull ∼= 52.3997%.
4. Bull Spread Combined with Risk-Free Asset. Investing 94.58% of
the capital in the risk-free asset and the remainder in a bull spread, we can
construct a portfolio P with the same expected return as stock, but lower
risk,
µP ∼= 2.6788%,
σP ∼= 2.8396%.
From the point of view of VaR, we consider the worst case scenario (among
those admitted by the investor) when S(20) ∼= 58.59 dollars, which may happen
with conditional probability 0.2597. In this scenario each of the above invest-
ments will bring a loss, which can be regarded as VaR at 74.03% confidence
level. The values of VaR and the market price of risk are collected below:
Investment
Stock
Call options
Bull spread
Bull spread with
risk-free asset
Market price
of risk
0.5
0.1
0.7
0.7
VaR
at 74.03%
$447
$12, 426
$7, 602
$412

214
Mathematics for Finance
The bull spread combined with risk-free will clearly be preferable to the other
investments as it has the highest market price of risk and lowest VaR.
Exercise 9.10
Check the above computations and consider a modification such that
the bull spread is constructed by buying a call with strike price $60 and
selling a call with strike price $62. Compute the expected return, risk
and VaR.
Exercise 9.11
Within the framework of the binomial model used above consider an
analyst who has reasons to believe that the stock price will fall, but no
more than 20% after 20 days. For a bear spread with strikes $56 and $58
constructed from put options compute the expected return, risk, and
VaR for the worst possible outcome.

10
Variable Interest Rates
This chapter begins with a model in which the interest rates implied by bonds
do not depend on maturity. If the rates are deterministic, then they must
be constant and the model turns out to be too simple to describe any real-life
situation. In an extension allowing random changes of interest rates the problem
of risk management will be dealt with by introducing a mathematical tool
called the duration of bond investments. Finally, we shall show that maturity-
dependent rates cannot be deterministic either, preparing the motivation and
notation for the next chapter, in which a model of stochastic rates will be
explored.
As in Chapter 2, B(t, T) will denote the price at time t (the running time)
of a zero-coupon unit bond maturing at time T (the maturity time). The de-
pendence on two time variables gives rise to some difficulties in mathematical
models of bond prices. These prices are exactly what is needed to describe the
time value of money. In Chapter 2 we saw how bond prices imply the interest
rate, under the assumption that the rate is constant. Here, we want to relax
this restriction, allowing variable interest rates.
In this chapter and the next one time will be discrete, though some parts of
the theory can easily be extended to continuous time. We shall fix a time step
τ, writing t = τn for the running time and T = τN for the maturity time. In
the majority of examples we shall take either τ =
1
12 or τ = 1. The notation
B(n, N) will be employed instead of B(t, T) for the price of a zero-coupon unit
bond. We shall use continuous compounding, bearing in mind that it simplifies
notation and makes it possible to handle time steps of any length consistently.
215

216
Mathematics for Finance
10.1 Maturity-Independent Yields
The present value of a zero-coupon unit bond determines an interest rate called
the yield and denoted by y(0) to emphasise the fact that it is computed at
time 0:
B(0, N) = e−Nτy(0).
For a different running time instant n such that 0 < n < N the implied yield
may in general be different from y(0). For each such n we thus have a number
y(n) satisfying
B(n, N) = e−(N−n)τy(n).
Generally (and in most real cases), a bond with different maturity N will
imply a different yield. Nevertheless, in this section we consider the simplified
situation when y(n) is independent of N, that is, bonds with different maturities
generate the same yield. Independence of maturity will be relaxed later in
Section 10.2.
Proposition 10.1
If the yield y(n) for some n > 0 were known at time 0, then y(0) = y(n) or else
an arbitrage strategy could be found.
Proof
Suppose that y(0) < y(n). (We need to know not only y(0) but also y(n) at
time 0 to decide whether or not this inequality holds.)
• Borrow a dollar for the period between 0 and n + 1 and deposit it for the
period between 0 and n, both at the rate y(0). (The yield can be regarded
as the interest rate for deposits and loans.)
• At time n withdraw the deposit with interest, enτy(0) in total, and invest
this sum for a single time step at the rate y(n). At time n + 1 this brings
enτy(0)+τy(n). The initial loan requires repayment of e(n+1)τy(0), leaving a
positive balance enτy(0)(eτy(n) −eτy(0)), which is the arbitrage profit.
The reverse inequality y(0) > y(n) can be dealt with in a similar manner.
Exercise 10.1
Let τ =
1
12. Find arbitrage if the yields are independent of maturity,
and unit bonds maturing at time 6 (half a year) are traded at B(0, 6) =
0.9320 dollars and B(3, 6) = 0.9665 dollars, both prices being known at
time 0.

10. Variable Interest Rates
217
As a consequence of Proposition 10.1, if the yield is independent of maturity
and deterministic (that is, y(n) is known in advance for any n ≥0), then it must
be constant, y(n) = y for all n. This is the situation in Chapter 2, where all
the bond prices were determined by a single interest rate. The yield y(n) = y,
independent of n, is then equal to the constant risk-free interest rate denoted
previously by r.
Historical bond prices show a different picture: The yields implied by the
bond prices recorded in the past clearly vary with time. In an arbitrage-free
model, to admit yields varying with time but independent of maturity we should
allow them to be random, so it is impossible to predict in advance whether y(n)
will be higher or lower than y(0).
We assume, therefore, that at each time instant the yield y(n) is a positive
random number independent of the maturity of the underlying bond.
Our goal is to analyse the return on a bond investment and the imminent
risk arising from random changes of interest rates. Suppose that we intend to
invest a certain sum of money P for a fixed period of N time steps. If the
yield y remains constant, then, as observed in Chapter 2, our terminal wealth
will be PeNτy. This will be our benchmark for designing strategies hedged
against unpredictable interest rate movements.
10.1.1 Investment in Single Bonds
If we invest in zero-coupon bonds and keep them to maturity, the rate of return
is guaranteed, since the final payment is fixed in advance and is not affected
by any future changes of interest rates. However, if we choose to close out our
investment prior to maturity by selling the bonds, we face the risk that the
interest rates may change in the meantime with an adverse effect on the final
value of the investment.
Example 10.1
Suppose we invest in bonds for a period of six months. Let τ =
1
12. We buy a
number of unit bonds that will mature after one year, paying B(0, 12) = 0.9300
for each. This price implies a rate y(0) ∼= 7.26%. Since we are going to sell the
bonds at time n = 6, we are concerned with the price B(6, 12) or, equivalently,
with the corresponding rate y(6). Let us discuss some possible scenarios:
1. The rate is stable, y(6) = 7.26%. The bond price is B(6, 12) ∼= 0.9644 and
the logarithmic return on the investment is 3.63%, a half of the interest
rate, in line with the additivity of logarithmic returns.
2. The rate decreases to y(6) = 6.26%, say. (The convention is that 0.01% is

218
Mathematics for Finance
one basis point, so here the rate drops by 100 basis points.) Then B(6, 12) ∼=
0.9692, which is more than in scenario 1. As a result, we are going to earn
more, achieving a logarithmic return of 4.13%.
3. The rate increases to y(6) = 8.26%. In this case the logarithmic return on
our investment will be 3.13%, which is lower than in scenario 1, the bond
price being B(6, 12) ∼= 0.9596.
We can see a pattern here: One is better offif the rate drops and worse offif
the rate increases. A general formula for the return on this kind of investment
is easy to find.
Suppose that the initial yield y(0) changes randomly to become y(n) ̸= y(0)
at time n. Hence
B(0, N) = e−y(0)τN,
B(n, N) = e−y(n)τ(N−n),
and the return on an investment closed at time n will be
k(0, n) = ln B(n,N)
B(0,N) = ln ey(0)τN−y(n)τ(N−n) = y(0)τN −y(n)τ(N −n).
We can see that the return decreases as the rate y(n) increases. The impact
of a rate change on the return depends on the timing. For example, if τ =
1
12,
N = 12 and n = 6, then a rate increase of 120 basis points will reduce the
return by 0.6% as compared to the case when the rate remains unchanged.
Exercise 10.2
Let τ =
1
12. Invest $100 in six-month zero-coupon bonds trading at
B(0, 6) = 0.9400 dollars. After six months reinvest the proceeds in bonds
of the same kind, now trading at B(6, 12) = 0.9368 dollars. Find the
implied interest rates and compute the number of bonds held at each
time. Compute the logarithmic return on the investment over one year.
Exercise 10.3
Suppose that B(0, 12) = 0.8700 dollars. What is the interest rate after
6 months if an investment for 6 months in zero-coupon bonds gives a
logarithmic return of 14% ?
Exercise 10.4
In this exercise we take a finer time scale with τ =
1
360. (A year is
assumed to have 360 days here.) Suppose that B(0, 360) = 0.9200 dollars,
the rate remains unchanged for the first six months, goes up by 200 basis

10. Variable Interest Rates
219
points on day 180, and remains at this level until the end of the year. If
a bond is bought at the beginning of the year, on which day should it
be sold to produce a logarithmic return of 4.88% or more?
An investment in coupon bonds is more complicated. Even if the bond is
kept to maturity, the coupons are paid in the meantime and can be reinvested.
The return on such an investment depends on the interest rates prevailing at
the times when the coupons are due. First consider the relatively simple case
of an investment terminated as soon as the first coupon is paid.
Example 10.2
Let us invest the sum of $1, 000 in 4-year bonds with face value $100 and $10
annual coupons. A coupon bond of this kind can be regarded as a collection
of four zero-coupon bonds maturing after 1, 2, 3 and 4 years with face value
$10, $10, $10 and $110, respectively. Suppose that such coupon bonds trade at
$91.78, which can be expressed as the sum of the prices of the four zero-coupon
bonds,
91.78 = 10e−y(0) + 10e−2y(0) + 10e−3y(0) + 110e−4y(0).
(The length of a time step is τ = 1.) This equation can be solved to find the
yield, y(0) ∼= 12%. We can afford to buy 10.896 coupon bonds. After one year
we cash the coupons, collecting $108.96, and sell the bonds, which are now
3-year coupon bonds. Consider three scenarios:
1. After one year the interest rate remains unchanged, y(1) = 12%, the coupon
bonds being valued at
10e−0.12 + 10e−2×0.12 + 110e−3×0.12 ∼= 93.48
dollars, and we shall receive 108.96 + 1, 018.52 ∼= 1, 127.48 dollars in total.
2. The rate drops to 10%. As a result, the coupon bonds will be worth
10e−0.1 + 10e−2×0.1 + 110e−3×0.1 ∼= 98.73
dollars each. We shall end up with $1, 184.63.
3. The rate goes up to 14%, the coupon bonds trading at $88.53. The final
value of our investment will be $1, 073.51.
Exercise 10.5
Find the rate y(1) such that the logarithmic return on the investment in
Example 10.2 will be a) 12%, b) 10%, c) 14%.

220
Mathematics for Finance
If the lifetime of our investment exceeds one year, we will be facing the
problem of reinvesting coupons. In the following example we assume that the
coupons are used to purchase the same bond.
Example 10.3
We begin as in Example 10.2, but our intention is to terminate the investment
after 3 years. After one year we reinvest the coupons obtained in the same, now
a 3-year, coupon bond. Consider the following scenarios after one year:
1. The rate remains the same for the period of our investment, y(0) = y(1) =
y(2) = y(3) = 12%. The bond price is $93.48, so for the $108.96 received
from coupons we can buy 1.17 additional bonds, increasing the number of
bonds held to 12.06. We can monitor the value of our investment by simply
multiplying the number of bonds held by the current bond price. We repeat
this in the following year. After three years we cash the coupons and sell
the bonds, the final value of the investment being $1, 433.33. This number
will be used as a benchmark for other scenarios. Observe that
1, 433.33 ∼= 1, 000e3×12%,
the same as the value after 3 years of $1, 000 invested on zero-coupon bonds.
The building blocks of our investment are summarised in the table below.
Year
0
1
2
3
Rate
12%
12%
12%
12%
PV of coupon 1
$8.87
$10.00
PV of coupon 2
$7.87
$8.87
$10.00
PV of coupon 3
$6.98
$7.87
$8.87
$10.00
PV of coupon 4
$6.19
$6.98
$7.87
$8.87
PV of face value
$61.88
$69.77
$78.66
$88.69
Bond price
$91.78
$93.48
$95.40
$97.56
Cashed coupons
$108.96
$120.60
$133.26
Additional bonds
1.17
1.26
Number of bonds
10.90
12.06
13.33
Value of investment
$1, 000.00
$1, 127.50
$1, 271.25
$1, 433.33
2. Suppose that the rate goes down by 2% after one year and then remains
at the new level. The drop of the rate results in an increase of all bond
prices. The number of additional bonds that can be bought for the coupons
is lower than in scenario 1. Nevertheless, the final value of the investment is

10. Variable Interest Rates
221
higher because so is the price at which we sell the bonds after three years.
Year
0
1
2
3
Rate
12%
10%
10%
10%
PV of coupon 1
$8.87
$10.00
PV of coupon 2
$7.87
$9.05
$10.00
PV of coupon 3
$6.98
$8.19
$9.05
$10.00
PV of coupon 4
$6.19
$7.41
$8.19
$9.05
PV of face value
$61.88
$74.08
$81.87
$90.48
Bond price
$91.78
$98.73
$99.11
$99.53
Cashed coupons
$108.96
$119.99
$132.10
Additional bonds
1.10
1.21
Number of bonds
10.90
12.00
13.21
Value of investment
$1, 000.00
$1, 184.65
$1, 309.25
$1, 446.94
3. If the rate increases to 14% and stays there, the bonds will be cheaper than
in Scenario 1. The final value of the investment will be disappointing.
Year
0
1
2
3
Rate
12%
14%
14%
14%
PV of coupon 1
$8.87
$10.00
PV of coupon 2
$7.87
$8.69
$10.00
PV of coupon 3
$6.98
$7.56
$8.69
$10.00
PV of coupon 4
$6.19
$6.57
$7.56
$8.69
PV of face value
$61.88
$65.70
$75.58
$86.94
Bond price
$91.78
$88.53
$91.83
$95.63
Cashed coupons
$108.96
$121.26
$134.46
Additional bonds
1.23
1.32
Number of bonds
10.90
12.13
13.45
Value of investment
$1, 000.00
$1, 073.53
$1, 234.85
$1, 420.41
As a motivation for certain theoretical notions, consider the above invest-
ment, with the same possible scenarios, but involving a specially designed se-
curity, a coupon bond with annual coupons paying $32, all other parameters
remaining unchanged. The results are as follows:
Scenario
Value after 3 years
12%, 12%, 12%, 12%
$1,433.33
12%, 10%, 10%, 10%
$1,433.68
12%, 14%, 14%, 14%
$1,433.78
It is remarkable that any change in interest rates improves the result of our
investment. We do not lose if the rates change unfavourably. On the other

222
Mathematics for Finance
hand, we do not gain in other circumstances. This is explained by the fact,
that a certain parameter of the bond, called duration and defined below, is
exactly equal to the lifetime of our investment. In some sense, the bond behaves
approximately like a zero-coupon bond with prescribed maturity.
Exercise 10.6
Check the numbers given in the above tables.
Exercise 10.7
Compute the value after three years of $1, 000 invested in a 4-year bond
with $32 annual coupons and $100 face value if the rates in consecutive
years are as follows:
Scenario 1: 12%, 11%, 12%, 12%;
Scenario 2: 12%, 13%, 12%, 12%.
Design a spreadsheet and experiment with various interest rates.
10.1.2 Duration
We have seen that variable interest leads to uncertainty as to the future value
of an investment in bonds. This may be undesirable, or even unacceptable, for
example for a pension fund manager. We shall introduce a tool which makes
it possible to immunise such an investment, at least in the special situation of
maturity-independent rates considered in this section.
For notational simplicity we denote the current yield y(0) by y. Consider a
coupon bond with coupons C1, C2, . . . , CN payable at times 0 < τn1 < τn2 <
. . . < τnN and face value F, maturing at time τnN. Its current price is given
by
P(y) = C1e−τn1y + C2e−τn2y + · · · + (CN + F)e−τnNy.
(10.1)
The duration of the coupon bond is defined to be
D(y) = τn1C1e−τn1y + τn2C2e−τn2y + · · · + τnN(CN + F)e−τnNy
P(y)
.
(10.2)
The numbers C1e−τn1y/P(y), C2e−τn2y/P(y), . . . , (CN + F)e−τnNy/P(y) are
non-negative and add up to one, so they may be regarded as weights or proba-
bilities. It can be said that the duration is a weighted average of future payment
times. The duration of any future cash flow can be defined in a similar manner.

10. Variable Interest Rates
223
Duration measures the sensitivity of the bond price to changes in the interest
rate. To see this we compute the derivative of the bond price with respect to y,
d
dy P(y) = −τn1C1e−τn1y −τn2C2e−τn2y −· · · −τnN(CN + F)e−τnNy,
which gives
d
dy P(y) = −D(y)P(y).
The last formula is sometimes taken as the definition of duration.
Example 10.4
A 6-year bond with $10 annual coupons, $100 face value and yield of 6% has a
duration of 4.898 years. A 6-year bond with the same coupons and yield, but
with $500 face value, will have a duration of 5.671 years. The duration of any
zero-coupon bond is equal to its lifetime.
Exercise 10.8
A 2-year bond with $100 face value pays a $6 coupon each quarter and
has 11% yield. Compute the duration.
Exercise 10.9
What should be the face value of a 5-year bond with 10% yield, paying
$10 annual coupons to have duration 4? Find the range of durations that
can be obtained by altering the face value, as long as a coupon cannot
exceed the face value. If the face value is fixed, say $100, find the level of
coupons for the duration to be 4. What durations can be manufactured
in this way?
Exercise 10.10
Show that P is a convex function of y.
If we invest in a bond with the intention to close the investment at time t,
then the future value of the money invested in a single bond will be P(y)ety,
provided that the interest rate remains unchanged (being equal to the initial
yield y(0)). To see how sensitive this amount is to interest rate changes compute
the derivative with respect to y,
d
dy (P(y)ety) =
	 d
dy P(y)

ety + tP(y)ety = (t −D(y))P(y)ety.

224
Mathematics for Finance
If the duration of the bond is exactly t, then
d
dy (P(y)ety) = 0.
If the derivative is zero at some point, then the graph of the function is ‘flat’
near this point. This means that small changes of the rate will have little effect
on the future value of the investment.
10.1.3 Portfolios of Bonds
If a bond of desirable duration is not available, it may be possible to create a
synthetic one by investing in a suitable portfolio of bonds of different durations.
Example 10.5
If the initial interest rate is 14%, then a 4-year bond with annual coupons
C = 10 and face value F = 100 has duration 3.44 years. A zero-coupon bond
with F = 100 and N = 1 has duration 1. A portfolio consisting of two bonds,
one of each kind, can be regarded as a single bond with coupons C1 = 110,
C2 = C3 = C4 = 10, F = 100. Its duration can be computed using the general
formula (10.2), which gives 2.21 years.
We shall derive a formula for the duration of a portfolio in terms of the
durations of its components. Denote by PA(y) and PB(y) the values of two
bonds A and B with durations DA(y) and DB(y). Take a portfolio consisting
of a bonds A and b bonds B, its value being aPA(y) + bPB(y). The task of
finding the duration of the portfolio will be divided into two steps:
1. Find the duration of a portfolio consisting of a bonds of type A. We shall
write aA to denote such a portfolio. Its price is obviously aPA(y). Since
d
dy (aPA(y)) = −DA(y)(aPA(y)),
it follows that
DaA(y) = DA(y).
This is clear if we examine the cash flow of aA. Each coupon and the face value
are multiplied by a, which cancels out in the computation of duration directly
from (10.2).
2. Find the duration of a portfolio consisting of one bond A and one bond B,
which will be denoted by A + B. The price of this portfolio is PA(y) + PB(y).

10. Variable Interest Rates
225
Differentiating the last expression, we obtain
d
dy (PA(y) + PB(y)) = d
dy PA(y) + d
dy PB(y)
= −DA(y)PA(y) −DB(y)PB(y).
The last term can be written as −DA+B(y)(PA(y) + PB(y)) if we put
DA+B(y) = DA(y)
PA(y)
PA(y) + PB(y) + DB(y)
PB(y)
PA(y) + PB(y).
This means that DA+B(y) is a linear combination of DA(y) and DB(y), the
coefficients being the percentage weights of each bond in the portfolio.
From the above considerations we obtain the general formula
DaA+bB(y) = DA(y)wA + DB(y)wB,
where
wA =
aPA(y)
aPA(y) + bPB(y),
wB =
bPA(y)
aPA(y) + bPB(y),
are the percentage weights of individual bonds.
If we allow negative values of a or b (which corresponds to writing a bond
instead of purchasing it, in other words, to borrowing money instead of invest-
ing), then, given two durations DA ̸= DB, the duration D of the portfolio can
take any value because wB = 1 −wA and
D = DAwA + DB(1 −wA) = DB + wA(DA −DB).
The value of D can even be negative, which corresponds to a negative cash
flow, that is, sums of money to be paid rather than received.
Example 10.6
Let DA = 1 and DB = 3. We wish to invest $1, 000 for 6 months. For the
duration to match the lifetime of the investment we need 0.5 = wA+3wB. Since
wA + wB = 1, it follows that wB = −0.25 and wA = 1.25. With PA = 0.92
dollars and PB = 1.01 dollars, we invest $1, 250 in 1250
0.92 ∼= 1, 358.70 bonds A
and we issue
250
1.01 ∼= 247.52 bonds B.
Exercise 10.11
Find the number of bonds of type A and B to be bought if DA = 2,
DB = 3.4, PA = 0.98, PB = 1.02 and you need a portfolio worth $5, 000
with duration 6.

226
Mathematics for Finance
Exercise 10.12
Invest $1, 000 in a portfolio of bonds with duration 2 using 1-year zero-
coupon bonds with $100 face value and 4-year bonds with $15 annual
coupons and $100 face value that trade at $102.
A portfolio with duration matching the investment lifetime is insensitive to
small changes of interest rates. However in practice we shall have to modify the
portfolio if, for example, the investment is for 3 years and one of the bonds is
a zero-coupon bond expiring after one year. In addition, the duration may, as
we shall see below, go offthe target. As a result, it will become necessary to
update the portfolio during the lifetime of the investment. This is the subject
of the next subsection.
10.1.4 Dynamic Hedging
Even if a portfolio is selected with duration matching the desired investment
lifetime, this will only be valid at the initial instant, since duration changes
with time as well as with the interest rate.
Example 10.7
Take a 5-year bond with $10 annual coupons and $100 face value. If y = 10%,
then the duration will be about 4.16 years. Before the first coupon is paid the
duration decreases in line with time: After 6 months it will be 3.66, and after
9 months 4.16 −0.75 = 3.31. If the duration matches our investment’s lifetime
and the interest rates do not change, no action will be necessary until a coupon
becomes payable. As soon as the first coupon is paid after one year, the bond
will become a 4-year one with duration 3.48, no longer consistent with the
investment lifetime.
Exercise 10.13
Assuming that the interest rate does not change, show that before the
first coupon is paid the duration after time t will D −t, where D is the
duration computed at time 0.
The next example shows the impact of the interest rate on duration.

10. Variable Interest Rates
227
Example 10.8
The bond in Example 10.7 will have duration 4.23 if y = 6%, and 4.08 if
y = 14%.
Exercise 10.14
Show that the duration of a 2-year bond with annual coupons decreases
as the yield increases.
Duration will now be applied to design an investment strategy immune to
interest rate changes. This will be done by monitoring the position at the end
of each year, or more frequently if needed. For clarity of exposition we restrict
ourselves to an example.
Set the lifetime of the investment to be 3 years and the target value to be
$100, 000. Suppose that the interest rate is 12% initially. We invest $69, 767.63,
which would be the present value of $100, 000 if the interest rate remained
constant.
We restrict our attention to two instruments, a 5-year bond A with $10
annual coupons and $100 face value, and a 1-year zero-coupon bond B with
the same face value. We assume that a new bond of type B is always available.
In subsequent years we shall combine it with bond A.
At time 0 the bond prices are $90.27 and $88.69, respectively. We find
DA ∼= 4.12 and the weights wA ∼= 0.6405, wB ∼= 0.3595 which give a portfolio
with duration 3. We split the initial sum according to the weights, spending
$44, 687.93 to buy a ∼= 495.05 bonds A and $25, 079.70 to buy b ∼= 282.77
bonds B. Consider some possible scenarios of future interest rate changes.
1. After one year the rate increases to 14%. The value of our portfolio is the
sum of:
• the first coupons of bonds A: $4, 950.51,
• the face value of cashed bonds B: $28, 277.29,
• the market value of bonds A held, which are now 4-year bonds selling
at $85.65: $42, 403.53.
This gives $75, 631.32 altogether. The duration of bonds A is now 3.44. The
desired duration is 2, so we find wA ∼= 0.4094 and wB ∼= 0.5906 and arrive
at the number of bonds to be held in the portfolio: 361.53 bonds A and
513.76 bonds B. (This means that we have to sell 133.52 bonds A and buy
513.76 new bonds B.)
a) After two years the rate drops to 9%. To compute our wealth we add:
• the coupons of A: $3, 615.30,

228
Mathematics for Finance
• the face values of B: $51, 376.39,
• the market value of A, selling at $101.46: $36, 682.22.
The result is $91, 673.92. We invest all the money in bonds B, since the
required duration is now 1. (The payoffof these bonds is guaranteed
next year.) We can afford to buy 1, 003.07 bonds B selling at $91.39.
The terminal value of the investment will be about $100,307.
b) After two years the rate goes up to 16%. We cash the same amount as
above for coupons and zero-coupon bonds, but bonds A are now cheaper,
selling at $83.85, so we have less money in total: $85, 305.68. However,
the zero-coupon bonds are now cheap as well, selling at $85.21, and we
can afford to buy 1, 001.07 of them, ending up with $100,107.
2. After one year the rate drops to 9%. In a similar way as before, we arrive
at the current value of the investment by adding the coupons of A, the face
value of B and the market value of bonds A held, obtaining $83, 658.73.
Then we find the weights wA ∼= 0.4013, wB ∼= 0.5987, determining our new
portfolio of 329.56 bonds A and 548.04 bonds B. (We have to sell 165.50
bonds A and buy 548.04 new bonds B.)
a) After two years the rate goes up to 14%. We cash $3, 295.55 from the
coupons of A, which together with the $54, 803.77 obtained from B and
the market value of $29, 174.39 of bonds A gives $87, 273.72 in total. We
buy 1003.89 new zero-coupon bonds B, ending up with $100,389 after
3 years.
b) After two years the rate drops to 6%. Our wealth will then be $94, 405.29,
we can afford to buy 1, 002.43 bonds B, and the final value of our in-
vestment will be $100,243.
As we can see, we end up with more than $100, 000 in each scenario.1
Exercise 10.15
Design an investment of $20, 000 in a portfolio of duration 2 years con-
sisting of two kinds of coupon bonds maturing after 2 years, with annual
coupons, bond A with $20 coupons and $100 face value, and bond B
with $5 coupons and $500 face value, given that the initial rate is 8%.
How much will this investment be worth after 2 years?
1 It can be shown that the future value at time t of a bond investment with duration
equal to t has a minimum if the rate y remains unchanged. This means that rate
jumps in a model with yields independent of maturity lead to arbitrage. In an
arbitrage-free model with rate jumps, the yields must therefore depend on maturity.

10. Variable Interest Rates
229
10.2 General Term Structure
Here we shall discuss a model of bond prices without the condition that the
yield should be independent of maturity.
The prices B(n, N) of zero-coupon unit bonds with various maturities de-
termine a family of yields y(n, N) by
B(n, N) = e−(N−n)τy(n,N).
Note that the yields have to be positive, since B(n, N) has to be less than 1
for n < N. The function y(n, N) of two variables n < N is called the term
structure of interest rates. The yields y(0, N) dictated by the current prices
are called the spot rates.
The initial term structure y(0, N) formed by the spot rates is a function
of one variable N. Typically, it is an increasing function, but other graphs
have also been observed in financial markets. In particular, the initial term
structure may be flat, that is, the yields may be independent of N, which is
the case considered in the previous section.
Exercise 10.16
If B(0, 6) = 0.96 dollars, find B(0, 3) and B(0, 9) such that the initial
term structure is flat.
The price of a coupon bond as the present value of future payments can be
written using the spot rates in the following way:
P = C1e−τn1y(0,n1) + C2e−τn2y(0,n2) + · · · + (CN + F)e−τnNy(0,nN)
(10.3)
for a bond with coupons C1, C2, . . . , CN due at times 0 < τn1 < τn2 < · · · <
τnN and with face value F, maturing at time τnN.
Despite the fact that for a coupon bond we cannot use a single rate for
discounting future payments, such a rate can be introduced just as an artificial
quantity. It is called the yield to maturity, and is defined to be the number y
solving the equation
P = C1e−τn1y + C2e−τn2y + · · · + (F + CN)e−τnN y.
Yield to maturity provides a convenient simple description of coupon bonds and
is quoted in the financial press. Of course, if the interest rates are independent
of maturity, then this formula is the same as (10.1).

230
Mathematics for Finance
Remark 10.1
To determine the initial term structure we need the prices of zero-coupon bonds.
However, for longer maturities (typically over one year) only coupon bonds may
be traded, making it necessary to decompose coupon bonds into zero-coupon
bonds with various maturities. This can be done by applying formula (10.3)
repeatedly to find the yield with the longest maturity, given the bond price and
all the yields with shorter maturities. This procedure was recognised by the
U.S. Treasury, who in 1985 introduced a programme called STRIPS (Separate
Trading of Registered Interest and Principal Securities), allowing an investor
to keep the required cash payments (for certain bonds) by selling the rest (the
‘stripped’ bond) back to the Treasury.
Example 10.9
Suppose that a one-year zero-coupon bond with face value $100 is trading at
$91.80 and a two-year bond with $10 annual coupons and face value $100 is
trading at $103.95. This gives the following equations for the yields
91.80 = 100e−y(0,1),
103.95 = 10e−y(0,1) + 110e−2y(0,2).
From the first equation we obtain y(0, 1) ∼= 8.56%. On substituting this into
the second equation, we find y(0, 2) ∼= 7.45%. As a result, the price of the
‘stripped’ two-year bond, a zero-coupon bond maturing in two years with face
value $100, will be 100e−2y(0,2) ∼= 86.16 dollars. Given the price of a three-year
coupon bond, we could then evaluate y(0, 3), and so on.
Going back to our general study of bonds, let us consider a deterministic
term structure (thus known in advance with certainty). The next proposition
indicates that this, in fact, is not realistic.
Proposition 10.2
If the term structure is deterministic, then the No-Arbitrage Principle implies
that
B(0, N) = B(0, n)B(n, N).
(10.4)
Proof
If B(0, N) < B(0, n)B(n, N), then:

10. Variable Interest Rates
231
• Buy a bond maturing at time N and write a fraction B(n, N) of a bond
maturing at n. (Here we use the assumption that the future bond prices are
known today.) This gives B(0, n)B(n, N) −B(0, N) dollars now.
• At time n settle the written bonds, raising the required sum of B(n, N) by
issuing a single unit bond maturing at N.
• At time N close the position, retaining the initial profit.
The reverse inequality B(0, N) > B(0, n)B(n, N) can be dealt with in a similar
manner, by adopting the opposite strategy.
Employing the representation of bond prices in terms of yields, we have
B(n, N) = B(0, N)
B(0, n) = eτny(0,n)−τNy(0,N).
This would mean that all bonds prices (and so the whole term structure) are
determined by the initial term structure. However, it is clear that one cannot
expect this to hold in real bond markets. In particular, this relation is not
supported by historical data.
This shows that assuming deterministic bond prices would go too far in
reducing the complexity of the model. We have no choice but to allow the future
term structure to be random, only the initial term structure being known with
certainty. In what follows, future bond prices will be random, as will be the
quantities determined by them.
10.2.1 Forward Rates
We begin with an example showing how to secure in advance the interest rate
for a deposit to be made or a loan to be taken at some future time.
Example 10.10
Suppose that the business plan of your company will require taking a loan of
$100, 000 one year from now in order to purchase new equipment. You expect to
have the means to repay the loan after another year. You would like to arrange
the loan today at a fixed interest rate, rather than to gamble on future rates.
Suppose that the spot rates are y(0, 1) = 8% and y(0, 2) = 9% (with τ = 1).
You buy 1, 000 one-year bonds with $100 face value, paying 100, 000e−8% ∼=
92, 311.63 dollars. This sum is borrowed for 2 years at 9%. After one year
you will receive the $100, 000 from the bonds, and after two years you can
settle the loan with interest, the total amount to pay being 92, 311.63e2×9% ∼=
110, 517.09 dollars. Thus, the interest rate on the constructed future loan will

