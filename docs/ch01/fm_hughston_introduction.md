# Introduction to Financial Markets & Discrete Pricing

!!! info "Source"
    **Financial Mathematics: An Introduction to Derivatives Pricing** by Lane P. Hughston and Christopher J. Hunter, King's College London, 2000.
    These notes are used for educational purposes.

## Introduction to Financial Mathematics

1
Introduction
The study of most sciences can be usefully divided into two distinct but inter-
related branches, theory and experiment. For example, the body of knowledge
that we conventionally label ‘physics’ consists of theoretical physics, where we
develop mathematical models and theories to describe how nature behaves,
and experimental physics, where we actually test and probe nature to see how
it behaves. There is an important interplay between the two branches—for
example, theory might develop a model which is then tested by experiment,
or experiment might measure or discover a fact or feature of nature which
must then be explained by theory.
Finance is the science of the financial markets. Correspondingly, it has
an important ‘theoretical’ side, called finance theory or mathematical finance,
which entails both the development of the conceptual apparatus needed for an
intellectually sound understanding of the behaviour of the financial markets,
as well as the development of mathematical techniques and models useful in
finance; and an ‘experimental’ side, which we might call practical or applied
finance, that consists of the extensive range of trading techniques and risk
management practices as they are actually carried out in the various finan-
cial markets, and applied by governments, corporations and individuals in
their quest to improve their fortune and control their exposure to potentially
adverse circumstances.
In this book we offer an introductory guide to mathematical finance, with
particular emphasis on a topic of great interest and the source of numerous
applications: namely, the pricing of derivatives. The mathematics needed for
a proper understanding of this significant branch of theoretical and applied
finance is both fascinating and important in its own right. Before we can
begin building up the necessary mathematical tools for analysing derivatives,
however, we need to know what derivatives are and what they are used for.
But this requires some knowledge of the so-called ‘underlying assets’ on which
these derivatives are based. So we begin this book by discussing the financial
markets and the various instruments that are traded on them. Our intention
here is not, of course, to make a comprehensive survey of these markets, but
to sketch lightly the relevant notions and introduce some useful terminology.
Unless otherwise stated, all dates in this section are from the year 1999, and
all prices are the relevant markets’ closing values. If no date is given for a
price, then it can be assumed to be January 11, 1999.
1

1.1
Financial Markets
The global financial markets collectively comprise a massive industry spread
over the entire world, with substantial volumes of buying and selling occur-
ring in one market or another at one place or another at virtually any time.
The dealing is mediated by traders who carry out trades on behalf of both
their clients (institutional and individual investors) and their employers (in-
vestment banks and other financial institutions). This world-wide menagerie
of traders, in the end, determines the prices of the available financial prod-
ucts, and is sometimes collectively referred to as the ‘market’. The most
‘elementary’ financial instruments bought and sold in financial markets can
be described as basic assets. There are several common types.
1.1.1
Basic Assets
A stock or share represents a part ownership of a company, typically on a
limited liability basis (that is, if the company fails, then the shareholder’s
loss is usually limited to his original investment).
When the company is
profitable, the owner of the stock benefits from time to time by receiving a
dividend, which is typically a cash payment. The shareholder may also realize
a profit or capital gain if the value of the stock increases. Ultimately, the
share price is determined by the market according to the level of confidence of
investors that the firm will be profitable, and hence pay further and perhaps
higher dividends in the future. For example, the value of a Rolls-Royce share
at the close of the London Stock Exchange on January 11 was 248.5p (pence),
which was down 0.5p from the prior day’s closing value. In the previous 52
weeks the highest closing value was 309p, while the lowest was 176.5p. The
company has declared a dividend of 6.15p per share for 1998 compared with
5.9p and 5.3p per share paid in the two years previous to that.
A bond is, in effect, a loan made to a company or government by the bond-
holder, usually for a fixed period of time, for which the bond-holder receives
a fee, known as interest. The interest rate charged is typically fixed at the
time that the loan is made, but might be allowed to vary in time according
to market levels and certain prescribed rules. The interest payments, which
are typically made on an annual, semi-annual or quarterly basis, are called
‘coupon’ payments. If a 10-year bond with a ‘face-value’ of $1000 has a 6%
annual coupon, that means that an interest rate payment of $60 is made
every year for ten years, and then at the end of the ten year period the $1000
2

‘principal’ is paid back to the bond-holder. Bonds are, in some respects, a
more conservative investment than stocks, since they provide a more or less
guaranteed or ‘fixed’ income. Hence the bond market is sometimes called
the ‘fixed-income’ market. However, if the company or government issuing
the bonds defaults, and cannot or will not pay back the loan, or part of the
loan, then the bond-holder may lose his shirt. The likelihood that a borrower
will default on any part of the loan is described by the credit quality of the
borrower. There are several credit rating agencies, for example Standard &
Poor’s (S&P) and Moody’s, which assign a rating to many companies and
governments. The rating systems vary between the agencies, but given two
ratings it is generally possible to decipher which one is better by following
some simple rules—A’s are better than B’s, which are better than C’s, and
so on; and more letters are better than less so, AAA is better than A. For
example, on our fiducial date, January 11, a bond previously issued by Wal
Mart, an American retail company that has an S&P credit rating of AA, with
a maturity date of May 2002, a face-value of $100 and a coupon of $6.75 cost
$105.02. By contrast, a Croatian government bond with a credit rating of
BBB-, a maturity date of February 2002, a face-value of $100, and a coupon
of $7.00 cost $93.21. Given the similar values of maturity and coupon, the
difference in price between the bonds is due to the superior credit rating of
Wal Mart (AA) over the Croatian government (BBB-). If the credit quality
of the borrower declines, then the price of a bond issued by the borrower will
also decline. Similarly, if interest rates generally rise, then bond prices will
fall. In either case, the purchaser of a bond may find that it is worth less
that what it was previously, despite the fixed income that it provides.
Exercise 1.1 Why does the value of a bond drop if interest rates go up?
Why does the value of a bond rise if credit quality improves?
When money is put on deposit with a bank or other financial institution
on an ‘overnight’ basis, i.e., where withdrawal on short notice is available,
then the depositor is essentially making a very short term loan to the financial
institution. The instantaneous (i.e., ‘overnight’) rate of interest paid on this
loan is called a money market rate, or ‘short term interest rate’.
Money
market accounts can be very nearly ‘risk-free’, in the sense that depositors
can get their money back on short notice, if required, and the balance in the
account always goes up. As an example, a private client with an account
balance of more than £1,000,000 in a money market account with the Royal
Bank of Scotland would receive an interest rate of 6.1% per year.
3

Exercise 1.2 Consider the money market account mentioned above. Sup-
pose that the interest earned every month is added to the account at the end
of the month. What is the actual annual interest rate that is earned?
Exercise 1.3 Let Bt be the amount in a money market account at time t.
Suppose that there is interest paid on the money in the account at a constant
rate r, that is, in a short time period dt, the interest that is paid is rBtdt.
Derive and solve the differential equation for Bt.
Commodities are physical objects, typically natural resources or foods
such as oil, gold, copper, cattle or wheat. There are often additional compli-
cations associated with commodities, for example, holding costs for the stor-
age and insurance of goods and delivery costs to move them about. These
costs are representative of the intricate details that can arise in practical
finance.
The concept of a domestic or foreign currency is, in reality, a fairly ab-
stract idea, but certainly includes the conventional ‘money’ issued by the
various countries of the world. The value of a currency, in units of other
currencies, depends on a number of factors, such as interest rates in that
country, the nation’s foreign trade surplus, the stability of the government,
employment levels, inflation, and so on. The exchange rate for immediate
delivery of a currency is called the spot exchange rate. This is the one kind of
financial asset that almost everyone has had some experience with, and you
will be familiar with the fact that the value (say in units of your own ‘domes-
tic’ currency) of a unit of ‘foreign’ currency can go up or down. Sometimes
these swings can be substantial, even over limited time horizons. Currencies
are very actively traded on a large scale in international over-the-counter
markets (that is, by telephone and electronic means). Some currency prices
are quoted to several decimal points in the professional markets. For exam-
ple, a typical ‘bid/offer’ spread for the price of sterling in U.S. dollars might
be 1.6558/1.6568. This means that the trader is willing to buy one pound
for 1.6558 dollars, and is willing to sell one pound for 1.6568 dollars. Traders
use fanciful nicknames for various rates, for example, the U.S. dollar/French
franc rate is called ‘dollar/Paris’, while the Canadian dollar/Swiss franc rate
is called ‘Candollar/Swiss’. The dollar/sterling rate is so important histori-
cally that it has a special name: ‘Cable’.
4

1.1.2
Derivatives
In addition to the basic assets that we have just described, another important
component of the financial markets are derivatives, which are in essence ‘side-
bets’ based on the behaviour of the ‘underlying’ basic assets. A derivative
can also be regarded as a kind of asset, the ownership of which entitles the
holder to receive from the seller a cash payment or possibly a series of cash
payments at some point in the future, depending in some pre-specified way
on the behaviour of the underlying assets over the relevant time interval. In
some instances, instead of a ‘cash’ payment another asset might be delivered
instead. For example, a basic stock option allows the holder to purchase
shares at some point in the future for a pre-specified price.
Derivatives, unlike the underlying assets, are in many cases directly syn-
thesized by investment banks and other financial institutions.
They can
either be ‘tailor-made’ and sold directly to a specific client, or, if they are
general enough, they can be traded in a financial market, just like the un-
derlying assets. The range of possible derivatives is essentially unlimited.
However there are a number of standard examples and types of derivatives
that one should be familiar with and which we shall mention briefly below.
The most common types of derivatives are the so-called options. An op-
tion is a derivative with a specified payofffunction that can depend on the
prices of one or more underlying assets. It will have specific dates when it
can be exercised, that is, when the owner of the option can demand pay-
ment, based on the value of the payofffunction. However, you are never
forced to ‘exercise the option’. Most options can only be exercised once, and
have a fixed expiration date, after which the option is no longer valid. There
are many different schemes for prescribing when an option can be exercised.
The most common examples are the so-called European options, which can
only be exercised on the expiration date, and American options, which can
be exercised at any time up to the expiration date. In this book, we shall
be concerned primarily with European derivatives, since they are mathemat-
ically much simpler, although the formalism that we build up is certainly
capable of handling the American case as well.
Exercise 1.4 What is the most money that you can lose by buying an op-
tion? Why?
The two most common options are the call option, which gives the owner
the right to buy a designated underlying asset at a set price (called the strike
5

price), and the put option which allows the owner to sell the underlying
asset at a given strike price. In London, organised derivatives trading takes
place at the London International Financial Futures and Options Exchange
(LIFFE). Among others, American call and put options on about 75 stocks
U.K. stocks are traded at LIFFE. For example, a call option on Rolls-Royce
with a strike of 240p and an expiry date of February 17, costs 19p per share,
whereas a put with the same strike and maturity costs 9.5p per share (recall
that the share price was 248.5p). In appendix E, an article from the May
2, 1885 Economist is reproduced. It contains a description of call and put
options that has not really changed much in the intervening century. We
shall give a fairly thorough treatment of the pricing of options in the sections
that follow. Note that there are options not only on underlying assets, but
also on other derivatives. For example, an option to enter into a swap is
called a ‘swaption’ (swaps are defined below).
An index is a number derived from a set of underlying assets (it generally
is a weighted sum or average of the underlying asset prices). The most com-
mon underlying assets to use are stocks, but there are also indices based on
bonds and commodities. As examples, The Financial Times-Stock Exchange
100 (FT-SE 100) index and the Dow Jones Industrial Average (DJIA) are
indices that take their values from share prices on the London and New York
exchanges respectively.
How is the FT-SE 100 index calculated? Well, the calculation uses the
100 largest companies by market capitalisation (share price times the number
of shares) on the London Stock Exchange. The index is simply the sum of
the market capitalisations of the 100 firms divided by an overall normalising
factor. This normalising factor was fixed at the inception of the index and is
only altered to ensure continuity of the index when the market capitalisation
of a firm used in the index calculation changes in a discontinuous way. This
can happen when new shares are issued by the firm or when it is removed
from the index calculation altogether and replaced by a new, larger firm.
The value of the FT-SE 100 index on January 11 was 6085.00.
In contrast, the DJIA was originally based on the unweighted average
of 30 ‘industrial’ companies on the New York Stock Exchange that were
chosen to span the manufacturing sector. Over the years two things have
happened—the definition of industrial has been widened and the index now
includes, for example, companies from the entertainment, financial and food
industries, and weightings have been attached to the companies in order to
keep the index continuous, just as in the case of the FT-SE 100. The value
6

of the DJIA on January 11 was 9619.89.
The advantage of an index is that it depends on a group of assets and
hence describes a particular sector or cross-section of the market. This means
that possible spurious fluctuations in individual asset prices that are specific
to that asset, rather than to the set of all underlying assets, will have a
decreased effect on the index. Two of the most common derivatives based on
an index are call and put options. For example, four days before expiration,
an American call option on the FTSE 100 index, with a strike of 6000, a
payoffof £10 per point, and a expiry date of January 15 cost £1,265 while
the corresponding put cost £295 (recall that the index value on January 11
was 6085.00). A European call option with a strike of 6025 and the same
expiry date cost £1,085, while the put cost £340.
Clearly however, the
underlying asset, the index, cannot be delivered, so instead a cash transfer
is made for the difference between the index value and the strike price when
the payoffis positive.
Exercise 1.5 How many pounds would you receive if you exercised the Amer-
ican call and put options on the FTSE? Why is this different from the market
price of the option?
A forward contract allows the investor to fix the price now for either
sale or purchase of the underlying asset at a fixed time in the future. For
example, one might contract to buy 100 shares of Rolls-Royce in 1 year’s
time for a price of 250p per share. Forward contracts of various maturities
are in principle possible for any underlying asset and can also be negotiated
on indices.
A swap is an agreement to exchange two underlying assets at some speci-
fied time in the future. For example, a currency swap might involve exchang-
ing n pounds for m dollars in one year.
As with any field of knowledge, there are many specialized terms that
require explanation or definition. A position refers to the state of an investor
or trader after either buying or selling an asset or derivative. If you have
bought a financial instrument, then we say that you are long that instrument,
or have taken a long position in it; whereas if you sell it, then you are short the
instrument. Note that taking a short position means that you have actually
sold something that you do not own, however, modulo certain rules and
regulations, this is allowed by many exchanges. A portfolio is a combination
of positions in many different instruments, variously long and short. A very
7

simple derivative, such as a call or put option, is described as vanilla, while
a more complicated one is refered to as an exotic derivative.
1.2
Uses of Derivatives
Derivatives are used for a variety of purposes. They can be used to reduce
risk by allowing the investor to hedge an investment or exposure, and hence
function as a sort of insurance policy against adverse market movements.
For example, if a firm needs a particular commodity, such as petroleum, on
a regular basis, then they can guard against a rise in the price of oil by
purchasing a call option. If the price of oil remains low, then the option is
not exercised and the oil is bought at the current price in the market, while
if the price rises above the strike, then the option is exercised to buy oil at a
below-market value. Derivatives can also be used to gain extra leverage for
specialized market speculation. In other words, if an investor has reason to
believe that the market is going to move in a particular way, then a larger
profit per dollar invested can be made by buying suitable derivatives, rather
than the underlying asset. But similarly, if the investment decision is wrong,
the investor runs the risk of making a correspondingly larger loss.
Exercise 1.6 Can you think of an example where a company might have
interest-rate risk? How about foreign exchange risk?
So far we have talked about investors that buy derivatives, but there must
likewise be financial institutions selling them.
These sellers are generally
investment banks, stock exchanges, and other large institutions. When selling
a derivative, the issuer makes an initial gain up-front from the fee that they
charge. They must then use the up-front money, possibly in conjunction
with borrowing, to hedge the derivative that they have sold by buying other
instruments in the market to form a hedging portfolio, in such a manner that,
regardless of the way that the prices of the underlying assets change, they
neither gain nor lose money. When the derivative expires, any payoffdue to
its owner will be equal to the current value of the hedging portfolio, less any
borrowings that have to be repaid.
But how is the value of the initial payment to be calculated? What is
the composition of the hedging portfolio? It is the principle of no arbitrage,
which asserts that in well-developed financial markets it is impossible to
make a risk-free profit from an initially empty portfolio, that is the key to
derivative pricing. If arbitrage were possible, arbitrageurs would rush in to
8

take advantage of it, and thereby alter the price so that inevitably no further
arbitrage would be possible. A kind of market equilibrium is therefore es-
tablished. By requiring that no arbitrage opportunities should arise between
a derivative price and the prices of the corresponding underlying assets it is
possible to arrive at a formula for the value of the derivative. This will yield
a so-called ‘fair price’ for a derivative. In practice, a suitable commission has
to be added to the fair price, otherwise the trader would not make a profit or
even cover the execution costs associated with the creation of the derivative.
1.3
Derivative PayoffFunctions
Before it is possible to price a derivative, however, we must understand its
payofffunction—the amount of money that the owner of the derivative is
entitled to receive (or must pay) at a given date or set of dates in the future,
as a function of the values of one or more underlying assets at certain dates.
If we consider European options, then the payofffunction depends only on
the value of the underlying assets at the expiry date, t = T.
For a call option with strike K, the owner of the derivative only receives
a payoffif the final asset price ST is greater than the strike price K, and then
the payoffis equal to the difference in the two prices. This can be expressed
mathematically as
CT = max[ST −K, 0].
(1.1)
Sometimes the more compact notation [x]+ = max[x, 0] is used. The payoff
of a call option is plotted as a function of the underlying asset price in figure
1.1.
In the case of a put option, the payoffis only non-zero if the asset price
at expiration is less than the strike price. This is given by
PT = max[K −ST, 0].
(1.2)
The payofffunction of the put option is plotted in figure 1.2
The third example of a derivative that we want to consider here is the
forward contract. A position in a forward contract differs from call and put
options in that it can have a negative payoff, that is, the investor can lose
money by owning the derivative. This is because the forward contract is not
an option; the investor is obliged to buy (or sell) the underlying asset at the
strike price previously agreed, even if it is not advantageous for him to do
9

Asset Price
$0
$50
$100
$150
$200
Payoff
$0
$50
$100
Figure 1.1:
The payofffunction of a call option with a strike of $100 as a function of
the price of the underlying asset.
Asset Price
$0
$50
$100
$150
$200
Payoff
$0
$50
$100
Figure 1.2:
The payofffunction of a put option with a strike of $100 as a function of
the price of the underlying asset.
so. The payofffunction is therefore the difference between the stock price ST
10

and the strike price K, that is,
FT = ST −K.
(1.3)
This function is plotted in figure 1.3.
Asset Price
$0
$50
$100
$150
$200
-$100
-$50
$0
$50
$100
Payoff
Figure 1.3:
The payofffunction of a long position in a forward contract with a strike
of $100 as a function of the price of the underlying asset.
Exercise 1.7 Suppose that a dealer sells a put option, instead of buying
one.
What is the payofffunction of the dealer’s position?
Why might a
dealer consider selling a put option? Can you find a combination of buying
and selling calls and/or puts such that the resulting portfolio payofffunction
is equal to the payofffunction for a long position in a forward contract with
strike K?
Exercise 1.8 Can you find a combination of long or short positions in calls
and puts that will reproduce the following payofffunctions:
11

Asset Price
$0
$50
$100
$150
$200
Payoff
$0
$50
$100
Figure 1.4:
The payofffunction of an option for exercise 1.8. Can you decompose it
into a combination of long and short calls and puts?
Asset Price
$0
$50
$100
$150
$200
Payoff
$0
$50
$100
Figure 1.5:
The payofffunction of an option for exercise 1.8.
12


## Arbitrage Pricing

2
Arbitrage Pricing
As mentioned in the previous section, arbitrage—the ability to start with
nothing and yet make a risk-free profit—is the key to understanding the
mathematics of derivative pricing. In this section we will show how it can be
used to determine a unique price for a derivative by using an example taken
from the foreign exchange markets.
Consider the exchange rate between U.S. dollars and U.K. pounds ster-
ling. Let St be the price of one unit of sterling (i.e., one pound) in dollars at
time t. For example, we might have S0 = $1.60, which means that at time 0,
it costs $1.60 to buy one pound. We say that St is the spot price for sterling
at time t. We can contrast this with ˜St, the forward price, which is the price
in dollars contracted today, that is at time t = 0, for the purchase of one
unit of asset (in our case one pound sterling) at time t in the future.3 This
means that we agree today to buy one pound sterling at time t for the price
˜St, paying the amount ˜St at time t on delivery of the sterling. The ‘tilde’ no-
tation is used throughout the book as a reminder that ˜St is a forward rather
than spot price. We want to calculate the value of ˜St which ensures that no
arbitrage is possible.
2.1
Expectation Pricing
One possible method for determining the forward price is expectation pricing.
In this framework, we assume that St is a random variable, and set the
forward price equal to the expected spot price at time t,
˜St = E[St].
(2.1)
While at first glance this may seem reasonable, it is, unfortunately, not cor-
rect. This is because if the forward price is set by equation (2.1), then a
clever arbitrageur can, by use of a crafty series of investments in the dol-
lar and sterling money market accounts, make a risk-free profit. This is a
situtation that, so the argument goes, would not be tolerated for long. You
will have heard the old saying, “There ain’t no such thing as a free lunch”.
3Note that the forward price should actually have two time indices, ˜S0,t, that denote
the contract time t = 0 and the purchase time t, rather than the single time index for the
spot price. However, we shall always assume that the forward price is agreed upon today,
at time 0, and hence only the exercise time t is important
13

We shall now demonstrate just how the arbitrageur is denied from dining at
others’ expense.
2.2
Arbitrage Pricing
Let r and ρ be the continuously compounded interest rates for dollars and
pounds respectively. We assume here, for simplicity, that r and ρ are con-
stant. We can then let Dt and Pt denote the values respectively of the dollar
and sterling bank accounts (money market accounts) at time t. As shown in
exercise 1.3, the value of the dollar bank account at time t is
Dt = D0ert,
(2.2)
while a similar relation holds for the sterling bank account, Pt = P0eρt. Here
D0 and P0 denote the initial number of dollars and pounds put on deposit.
We now want to consider two different trading strategies for an initial
investment of n pounds that must be converted into dollars by time t. We
would like the strategies to be deterministic, that is, they should not depend
on any random variables, but instead must yield a definite result at time t.
Since there are only two exchange rates that we know for sure, today’s rate S0
and the forward rate ˜St, then there are only two times that we can exchange
currencies without introducing some element of randomness—today, and at
time t. Consider the two investment strategies described in figure 2.1. The
‘dollar investment strategy’ converts the initial n pound investment to dollars
immediately, and has a final value of nS0ert dollars. The ‘forward buying
strategy’ takes the opposite tack and doesn’t convert the pounds to dollars
until time t. This alternative route yields n ˜Steρt dollars. We then equate the
results of the two investment strategies, that is, we have the relation
n ˜Steρt = nS0ert,
(2.3)
which implies that
˜St = S0e(r−ρ)t.
(2.4)
Thus, the forward price ˜St is entirely determined by the interest rate dif-
ferential r −ρ, and not, perhaps surprisingly, by the expected value of the
spot rate E[St]. But why did we equate the results of the two investment
strategies? The answer lies in the no arbitrage condition.
Suppose that one could contract to sell sterling at a rate Ft, higher than
˜St. Then, using the arbitrage strategy outlined in figure 2.2, an enterprising
14

Dollar Investment Strategy:
1. Start with n pounds.
2.
Exchange the n pounds for
dollars at time 0, using the spot
price S0. We now have nS0 dollars,
which we invest in a dollar bank
account.
3. Sit back and relax.
4.
At time t the investment is
worth nS0ert dollars.
Forward Buying Strategy:
1.
Start with n pounds and de-
posit them in the sterling bank ac-
count.
2.
Contract to sell neρt pounds
for dollars at the forward exchange
rate ˜St at time t. This is called a
forward sale, since the contract is
made at time 0 for a sale at time
t.
3.
At time t, the value of the
sterling bank account will be neρt
pounds.
4. Convert the sterling to dollars
at the contracted exchange rate ˜St
(that is, execute the forward sale).
The value of the dollar account is
then n ˜Steρt dollars.
Figure 2.1:
Two trading strategies which both begin with n pounds and 0 dollars, and
end with 0 pounds and a fixed number of dollars. Arbitrage arguments tell us that the
final number of dollars must be the same for both strategies.
but penniless arbitrageur could start with no money but end up with n(Ft −
˜St)eρt dollars. Since Ft > ˜St, by use of this fiendishly clever strategy a sure
profit is generated without any initial investment and with absolutely no
risk, that is, arbitrage occurs. In such a case, arbitrageurs will swoop in and
take advantage of the situation, generating guaranteed profits for themselves,
and essentially forcing traders to adjust their forward prices until at last the
arbitrage opportunities disappear. In this way, the no arbitrage condition
allows us to obtain a price for the forward contract.
Exercise 2.1 Show how an arbitrageur can make a sure profit with no risk
if Ft < ˜St.
15

Arbitrage Strategy:
1. Start with nothing and borrow nS0 dollars at the in-
terest rate r. Immediately exchange these dollars at the
spot rate S0 for n pounds, which we deposit in the sterling
bank account.
2. Still at time 0, contract to sell neρt pounds forward at
time t at the given ‘high’ forward exchange rate Ft (> ˜St).
3. At time t, the initial loan of nS0 dollars now requires
nS0ert dollars be repaid, while the sterling bank account
has neρt pounds in it.
4. Sell the pounds in the sterling bank account (taking
advantage of the previous contracted agreement) at the
price Ft dollars per pound. This generates nFteρt dollars,
so that after repaying the loan, the remaining number of
dollars is
nFteρt −nS0ert
=
neρt(Ft −S0e(r−ρ)t)
=
neρt(Ft −˜St).
(2.5)
Figure 2.2:
A trading strategy which generates a guaranteed profit if the offered forward
price Ft is greater than the no arbitrage value ˜St.
16

Exercise 2.2 Suppose that the initial exchange rate is $1.60, and that the in-
terest rates are 10% and 8% (per annum) for dollars and pounds respectively.
What is the exchange rate for a two-year forward purchase?
Exercise 2.3 If the sterling interest rate is no longer time independent, but
is instead given by a steadily changing rate according to the scheme ρ(t) = a+
bt, then what is the forward exchange rate? Suppose that the initial exchange
rate is $1.60, the dollar interest rate is 10%, and the constant terms in sterling
rate are 8% and 1% for a and b respectively. What is the exchange rate for
(a) a two-year forward purchase, and (b) a four-year forward purchase?
2.3
Trading Strategies
However, it still may not be clear why we had to equate the final values of the
two trading strategies given in figure 2.1, since we ended up using a different
trading strategy (that of figure 2.2) in order to prove that a forward price
other than ˜St would imply arbitrage. In order to understand the connection
between the three trading strategies better, we should consider exactly what
it is that we mean by a trading strategy—up to this point we have been
slightly cavalier in our definitions and assumptions. For example, Dt does
not tell you how much money that you have in the dollar bank account at
time t, but rather it tells you how much a unit of the money market account
is worth. It is easy to forget that the money market account is an underlying
asset, just like a share in a company, and it can be bought and sold on the
market. This is best illustrated with a simple example. Suppose that at time
0, the money market account is worth one dollar (D0 = 1). If I buy 100
units of it, then it will cost me 100 dollars. At time t, one unit of the money
market account is worth ert dollars, and since I have 100 units, my original
investment is now worth 100ert dollars. If I sell my units, then I receive this
money and the value of my holdings in the money market becomes zero, but
the money market account is still worth Dt = ert dollars per unit.
From this example, it should be obvious that in addition to the value of
a unit of the money market account Dt, we also need to introduce a second
quantity φt which tells you how much of the money market account that you
own. The total value of your holding is then φtDt, that is, it is the number
of units of the money market account that you own, multiplied by the value
of each unit. We will also need to introduce a quantity ψt which is equal
to the number of units of the sterling money market account that you own.
17

A trading strategy is then the pair or ‘portfolio’ (φt, ψt) which tells you how
much of each asset that you own. ‘Buying’ an asset then corresponds to
increasing the value of φt or ψt, whereas ‘selling’ means decreasing the value.
A negative value means that we are borrowing money, or have ‘sold short’
the asset.
Look at figure 2.3.
This is a graphical representation of the trading
Dollar Investment Strategy
Forward Buying Strategy
-
r
6
6
6
0−
0+
t−
t+
nS0
nS0ert nS0ert
φtDt
time
-
r
r
r
6
0−
0+
t−
t+
n ˜Steρt
φ′
tD′
t
time
-
6
r
r
r
0−
0−
t−
t+
n
ψtPt
time
-
6
6
6
r
0−
0+
t−
t+
n
n
neρt
ψ′
tP ′
t
time
Figure 2.3:
The portfolio values for the dollar investment strategy (left) and the forward
buying strategy (right).
strategies outlined in figure 2.1. The portfolios are discontinuous in time
because money can be exchanged instantaneously. The times 0−, 0+ and
t−, t+ represent left and right handed limits as time approaches 0 and t
respectively. The steps 1,2,3 and 4 in figure 2.1 correspond to the time steps
0−, 0+, t−and t+. Similarly figure 2.4 is a realization of the arbitrage strategy
described in figure 2.2.
What mathematical operations can we perform on trading strategies?
Well, suppose that (φt, ψt) is a trading strategy. Then what about its negative
(−φt, −ψt), is this also a trading strategy? Of course it is! It is the strategy
which simply buys whenever the original strategy sells and sells whenever the
original strategy buys. How about if we had two trading strategies (φt, ψt)
and (φ′
t, ψ′
t). Could we add them together to get a new strategy, (φt+φ′
t, ψt+
18

Arbitrage Strategy
-
6
?
?
?
?
6
0−
0+
t−
t+
nS0
−nS0 −nS0
−nS0ert −nS0ert
nFteρt
φtDt
time
-
r
6
6
r
0−
0+
t−
t+
n
neρt
ψtPt
time
Figure 2.4:
The portfolio values for the Arbitrage strategy.
ψ′
t)? Again, the answer is yes! The new strategy simply performs all the buy
and sell operations of the two original strategies. In terms of portfolio value
plots, like those in figures 2.3 and 2.4, a negative trading strategy simply
reverses the direction of all the arrows, while a sum of two strategies means
that you combine all the arrows from both plots into a new one.
We are now in a position to see exactly why we must equate the final
values of the ‘dollar investment strategy’ and the ‘forward buying strategy’.
Consider the trading strategy formed by adding the negative of the dollar
investment strategy to the forward buying strategy. What does this look like?
Well, at 0−the sterling holdings cancel and there are no dollar holdings, so
we begin with nothing. Then at time 0+ we have n pounds and −nS0 dollars.
At t−, the sterling holdings are worth neρt, while our dollar debt has mounted
to −nS0ert. Finally, at t+, we liquidate our sterling position and have a final
dollar holding of n ˜Steρt −nS0ert. But since we began with nothing, in order
to avoid arbitrage we must also end with nothing, and hence we must set
19

n ˜Steρt −nS0ert = 0, which is the equivalent of equating the final values of
the dollar investment strategy and the forward buying strategy.
This new trading strategy outlined above is easiest to follow by simply
subtracting the left hand side of figure 2.3 from the right hand side. You
should then notice a remarkable similarity to the arbitrage strategy of figure
2.4, except that Ft is replaced by ˜St. Thus, the arbitrage strategy is simply
the forward buying strategy minus the dollar investment strategy.
2.4
Replication Strategy
Any no arbitrage argument for pricing a derivative is ultimately based on a
replication strategy, which is a trading strategy that uses market instruments
to ‘replicate’ the initial and final positions required by the derivative. How
does this work? Well, given two strategies with the same initial position,
and guaranteed final positions, then these final positions must be equal.
Otherwise, by going long the strategy with the higher final value and short
the other we would generate an arbitrage.
For example, suppose that we have a forward contract to buy one unit of
sterling for a price ˜St. Then the cash flow is very simple: at time t we receive
one unit of sterling and pay ˜St dollars. This cash flow is shown in the left side
of figure 2.5. Can we replicate this cash flow by using market instruments?
Most certainly.
Start with nothing, then borrow S0e−ρt dollars from the
bank and convert it into e−ρt pounds. At time t we shall have the required
one pound sterling, while the dollar position is short S0e(r−ρ)t dollars. This
is shown on the right side of figure 2.5. Since the intial and final position
of the derivative cash flow and replicating strategy are the same, and their
final positions are both deterministic, then by our earlier arguments these
final positions must be equal, so ˜St = S0e(r−ρ)t, as we have calculated several
times before. Now let us consider a slightly more complicated example.
2.5
Currency Swap
What we have done up to now is, given the current exchange rate and the
interest rates in two currencies, to determine the no arbitrage value for the
forward exchange rate at some time t in the future. However, suppose that we
know what exchange rate we would like to pay in the future, and would like
to agree on it now. This is a currency swap. Unlike the previous example it
20


## Discrete Probability

Derivative Cash Flow
Replication Strategy
-
?
0
t
−˜St
Dollars
time
-
6
?
?
?
0−
0+
t
S0e−ρt
-S0e−ρt -S0e−ρt
-nS0e(r−ρ)t
φtDt
time
-
r
6
0−
t
1
Pounds
time
-
r
6
6
0−
0+
t
e−ρt
1
ψtPt
time
Figure 2.5:
The cash flow for a forward contract is shown on the left side. We can
construct the replication strategy shown on the right such that it has the same initial and
final positions as the derivative. This allows us to determine the forward price.
may involve an initial purchase price. But identical to the previous example,
we can calculate the price of the derivative by replicating its cash flow.
Suppose that we agree to swap nK dollars for n pounds at time t. What
is the cash flow? Well, at time 0, we receive an initial cash payment of C
dollars, which may be negative. This is the price paid by the dollar-purchaser
for the swap. At time t, the currency swap occurs and we receive n pounds
but must pay nK dollars to our counterparty. This cash flow is shown in
figure 2.6. Can we artificially construct a trading strategy that has the same
initial and final positions as the derivative?
The first step in creating the replicating strategy is to start with C dollars
and no sterling so that the initial positions are the same. Recall that C is
the cost of the derivative (in dollars) that we are trying to calculate. If we
convert nS0e−ρt dollars into ne−ρt pounds at time 0, then at time t this will
produce the required sterling position of n pounds. The value at time 0+
21

Derivative Cash Flow
Replication Strategy
-
6
?
0
t
C
−nK
Dollars
time
-
6
?
?
0−
0+
t
C
C −nS0e−ρt
(C −nS0e−ρt)ert
φtDt
time
-
r
6
0−
t
n
Pounds
time
-
r
6
6
0−
0+
t
ne−ρt
n
ψtPt
time
Figure 2.6:
The cash-flow for a dollar-pound currency swap is shown on the left. The
sterling-purchaser receives an initial amount C in dollars. This is the ‘cost’ of the swap.
Then at time t, he receives n pounds and pays nK dollars to his counterparty. On the right
is a replicating strategy which reproduces the swap cash-flow. Starting with C dollars,
nS0e−ρt dollars are converted into pounds. At time t this will produce the required sterling
position. We can then adjust the value of C such that the dollar position is also equal to
the required swap value, which therefore uniquely determines the cost of the swap.
of the dollar account is C −nS0e−ρt dollars, and hence at time t it will be
worth (C −nS0e−ρt)ert dollars. What do we do next? Well, just as in the
previous example, we set the value of the replicating position equal to that
of the derivative. Anything would else allow arbitrage. Thus
³
C −nS0e−ρt´
ert = −nK
(2.6)
This allows us to solve for the purchase price C,
C
=
ne−rt ³
S0e(r−ρ)t −K
´
=
ne−rt ³ ˜St −K
´
(2.7)
Hence the price that the dollar-purchaser must pay for a currency swap where
22

n pounds are exchanged for nK dollars is n( ˜St −K)e−rt dollars. The repli-
cation strategy is shown in the right side of figure 2.6. Note that the value of
K that yields a zero price for the currency swap is the forward rate ˜St. That
is why there is no cost for either party to enter into a forward contract.
2.6
Summary
The principle of no arbitrage may be the key to understanding derivative
pricing, but what kind of law is it? It is clearly not a fundamental law of
nature, and is not even always obeyed by the markets. In some ways it is
similar to Darwin’s theory of natural selection. An institution that does not
price by arbitrage arguments the derivatives that it sells will suffer relative
to institutions that do. If the price is set too high, then competitors will
undercut it; if the price is too low, then the institution will be liable to
market uncertainty as a hedging portfolio cannot be properly constructed.
In the competitive world of finance, such an institution would not last long.
There is a crucial point to take away from this section, and to which we
shall come back again and again in the course of this book. It is that the
actual probabilities of what might happen to the exchange rate (or any other
underlying asset) are not important. This is because the expectation of a
random variable, such as the exchange rate, may give a good idea of what
the exchange rate may be in the future, but it leaves too much to chance.
What matters instead, is that we can create a trading strategy such that
there is no uncertainty in the outcome. By creating a risk-free strategy that
also replicates the derivative payofffunction, we can uniquely determine the
no arbitrage price for the derivative.
23

3
A Simple Casino
When it comes right down to it, putting money into the financial world can
be a bit of a gamble. So there is really no better way to begin thinking about
financial mathematics than by looking at betting in a Casino, which is every
bit a gamble. To meet our sophisticated tastes, we will be betting in a deluxe
Casino that allows not only standard wagers, but also ‘side-bets’ which we
shall call derivative bets. Our Casino analogy will turn out to be a very
simple, but highly effective, model for a stock market. After laying down
the rules for gambling and investigating the nature of ‘ordinary’ bets, the
goal will be to find a price for the derivative bets by use of the no arbitrage
condition.
3.1
Rules of the Casino
Suppose that we make our way into a Casino that allows gamblers to make
bets on the outcome of a coin flip. While this is probably one of the simplest
Casinos imaginable, we can make it a more interesting place by increasing
the complexity of the bets that can be made on the result of the coin toss.
At time 0, just before the coin toss, the initial stake for a bet is S0 dollars,
which you pay to the Casino. The amount that you receive back from the
Casino at time t, just after the coin toss, is St dollars, which for the ‘standard’
bet we define to be U dollars (‘up’) for heads and D dollars (‘down’) for tails.
For example, we could take
S0 = $2.00,
U = $3.00,
and
D = $1.50.
(3.1)
In this case, we place $2.00 on the the table, and if the outcome is heads we
get $3.00 back, while if the outcome is tails, then we only get $1.50 back. In
addition to this ‘standard’ bet, we can also make a short bet. This means
that at time 0 the Casino pays you S0 dollars to enter the game, but then
you have to pay the Casino St dollars at time t, so the actual amount that
you have to pay depends on the outcome of the coin flip. Under this naming
scheme, the standard bet is actually a long bet. Since we can place both long
and short bets with the same initial stake, the roles of the Casino and player
are symmetric in our simple model. In a real Casino this is not, of course,
the case, and the rules of the various games are designed so that the Casino
will on average make money.
24

Since the Casino is trying to encourage gambling, it is willing to lend
money at no charge. It will also hold your money for you, however no interest
is earned.
Thus, we can think of the Casino as having a money market
account where the risk-free interest rate is zero.
Exercise 3.1 Using a simple arbitrage argument, show why we must have
U > S0 > D.
The Casino is a chaotic place, but the organisers and participants are
known to be honest. That is, the rules of the Casino are always obeyed. We
are not told whether the coin is ‘fair’ (50-50), nor is there any implication
that it is. We suspect that it isn’t fair, and after watching play for a few
hours and making use of the law of averages, we conclude that the relevant
probabilities are
Prob[H] = p
and
Prob[T] = q,
(3.2)
where H, T stand for heads and tails respectively, and p + q = 1. We are
also worried that these probablities may change over time.
Clearly the expected payofffrom a standard bet is E[St] = pU + qD
dollars. But there is no reason (a priori) to suppose that the initial stake
satisfies S0 = E[St]. This is the expectation hypothesis, which we saw in the
previous section is generally wrong. If S0 < E[St], then anyone willing to
play this game is risk-averse, that is, they expect some profit, on average, for
taking risk. If S0 > E[St], then players, on average, pay to take risk (which is
typical for a Casino), and are risk-preferring. If S0 = E[St], then the players
are risk-neutral, since they expect to neither gain nor lose money if they play
for a long time.
3.2
Derivatives
A derivative is a kind of side-bet, with a prescribed payoffthat depends on
the outcome of the coin flip. The Casino is happy to allow derivative bets
by special arrangement. In a typical contract, a player pays an initial bet f0
at time 0, and then receives a payoffof ft(St) dollars at time t, where ft(St)
is a prescribed function of the random variable St. A derivative contract is
defined by its payofffunction ft(St) and its purchase price f0. It is possible, in
principle, for f0 to be negative, which by convention means that the Casino
pays the player to enter into the contract.
Note that ft(St) can also, in
25

principle, be negative, in which case the player has to pay the Casino at time
t.
For example, we can consider the important case of a call option, which
has a payofffunction
ft(St) = max[St −K, 0],
(3.3)
where K is a fixed number of dollars, known as the strike price, such that
U > K > D. By construction, the call option pays offonly when St = U.
Note that many options, even if they are based on an underlying asset, do
not necessarily involve the buying or selling of the underlying, but rather the
cash difference between the asset value and the strike price is transferred if
the terminal value of the asset exceeds the strike (assuming that the option is
a call). In cases where the underlying is not transferrable, such as an option
on a stock index, or the outcome of a coin flip, then a cash transfer is the
only possibility. We could also consider a more complicated derivative, with
a payofffunction such as
ft(St) = αS3
t + βS2
t + γSt + δ,
(3.4)
where α, β, γ, δ are constants. The pricing of an exotic derivative, like this
one, is computationally more difficult than for a vanilla one, such as the call
option above, however, mathematically they are given by the same general
formula.
Now we need to determine the price f0 that someone should pay at time
0 to buy a derivative that pays offft(St) dollars at time t. A plausible guess
is
f0
=
E[ft(St)]
=
pft(U) + qft(D),
(3.5)
which represents the expected payoffof the derivative, that is, the probability
weighted average of the possible payoffs. This guess is another typical ex-
ample of the ‘expectation hypothesis’. As before, it is wrong. So how do we
determine f0? Just like in the simple currency model of section 2, we want
to use a no arbitrage condition to determine the correct price.
3.3
No Arbitrage Argument
Suppose that instead of dealing directly with the Casino, the player instead
goes through an intermediary known as the dealer or trader. Then, if the
26


## One-Period Asset Pricing

gambler purchases a derivative from the dealer, the dealer gets f0 dollars
at time 0, and must pay ft(St) dollars back to the player at time t. The
dealer does not want to take any risk, and hence must hedge his derivative
position by making a standard bet with the Casino, in a manner that we shall
describe. Rather than making a full-sized bet, the stake for this standard
bet is only δS0. The idea is that the dealer will choose δ such that the total
payoffat time t is independent of the result of the coin flip, and hence a
guaranteed amount.
To calculate the required value of δ, we note that at time t the dealer
gets δSt dollars from the Casino, but has to pay ft(St) dollars to the player.
So the dealer’s net payoffat time t is δSt −ft(St) dollars. Since the dealer
wants this potentially random amount to be independent of the outcome of
the coin flip, we need to force the two possible payoffs to be the same, that
is, we require that
δU −ft(U) = δD −ft(D).
(3.6)
But, we can solve this for δ to get
δ = ft(U) −ft(D)
U −D
.
(3.7)
This value of δ is called the hedge ratio. If the dealer makes a standard bet
with the Casino in this quantity, that is, with initial stake δS0 dollars, then
his obligation to the player (through the derivative) is ‘hedged’.
Exercise 3.2 Calculate the value of dealer’s payofffor the hedged bet.
We can now apply the no arbitrage argument. Suppose that the dealer
starts with nothing. At time 0 he sells the derivative to the player and receives
f0 dollars, while at the same time he makes a basic bet with the Casino for
δS0 dollars. After completing these two transactions the dealer will have
f0 −δS0 dollars left over, which is put into the bank account. At time t,
after the coin toss, the dealer obtains the guaranteed amount δSt −f(St).
In addition, he has money in the bank account, although since it has not
earned any interest it is still worth f0 −δS0 dollars. Thus, the net value of
the dealer’s position at time t is f0 −δS0 + δSt −ft(St) dollars. But this is
a risk-free amount, and since the dealer started with nothing, he must end
with nothing, so
f0 −δS0 + δU −ft(U) = 0,
(3.8)
27

or equivalently,
f0 −δS0 + δD −ft(D) = 0.
(3.9)
This relation can be used to solve for the correct price f0 of the derivative.
We get
f0
=
ft(U) + δ(S0 −U)
=
ft(U) + ft(U) −ft(D)
U −D
(S0 −U)
=
ft(U)(U −D) + \[ft(U) −ft(D)\](S0 −U)
U −D
=
ft(U)[S0 −D] −ft(D)[S0 −U]
U −D
=
ft(U)S0 −D
U −D + ft(D)U −S0
U −D .
(3.10)
Note that it was only possible to apply this argument because the dealer al-
ways gets the same payofffrom his hedged position, that is, it is independent
of the actual outcome of the coin flip.
The derivative price calculated in equation (3.10) can be summarised
succintly by writing
f0 = p∗ft(U) + q∗ft(D),
(3.11)
where
p∗= S0 −D
U −D ,
and
q∗= U −S0
U −D .
(3.12)
A quick calculation will confirm that p∗, q∗> 0 and p∗+q∗= 1, which means
that f0 can be interpreted as a kind of weighted average of the outcomes
ft(U) and ft(D), where the weights are given by the numbers p∗and q∗.
Exercise 3.3 Show that an arbitrageur can make a sure profit if the deriva-
tive is priced other than at f0.
The price f0 does not depend in any way on the actual weighting of the
coin as given by the probabilities p, q. In fact, the price f0 is completely
determined once we know the Casino rules, that is, the basic stake S0, the
payoffs U and D, and the derivative payoffcontract specification ft(St). This
independence from ‘real’ or ‘physical’ probabilities is one of the ‘mysterious’
features of derivative pricing in general, as we shall see, that already applies
very clearly in this somewhat simplistic, but nevertheless very important
example.
28

4
Probability Systems
Here we shall digress briefly to review some basic ideas in probability. We
need to acquire an understanding of the different parts of a probability system
and how they fit together. In order to make some sense of it all, we shall
find it useful to think of a probability system as a physical experiment with
a random outcome. To be more concrete, we shall use a specific example to
guide us through the various definitions and what they signify.
Suppose that we toss a coin three times and record the results in order.
This is a very simple experiment, but note that we should not necessarily
assume that the coin toss is fair, with an equally likely outcome for heads or
tails. After all, life is rarely as fair as we would like it to be, and we need to
be prepared for this. Joking aside, the reason for this chapter is to make it
clear that there can, in principle, be many different probabilities associated
with the same ‘physical experiment’. This will have an impact on how we
price derivatives.
4.1
Sample Space
The basic entity in a probability system is the sample space, usually denoted
Ω, which is a set containing all the possible outcomes of the experiment. If
we denote heads by H and tails by T, then there are 8 different possible
outcomes of the coin-tossing experiment, and they define the sample space
Ωas follows:
Ω= {HHH, HHT, HTH, HTT, THH, THT, TTH, TTT}.
(4.1)
We formalize the concept of a sample space in the following definition,
Definition 4.1 The sample space Ω= {ωi}N
i=1 is the set of all possible
outcomes of the experiment.
Note that we are assuming that the sample space is finite. This is applicable
to the discrete time formalism that we are developing in our discussion of
the Casino and the binomial model that follows on from this, but will have
to be modified for the continuous time formalism that is to come later.
4.2
Event Space
We are eventually going to want to talk about the probability of a specific
‘event’ occurring. Is the sample space, simply as given, adequate to allow
29

us to discuss such a concept?
Unfortunately, the answer is “not quite”.
This is because we want to ask more than just, “What is the probability
that the outcome of the coin toss is a specific element of the sample space,
say HTH?” We also want to ask, “What is the probability that the out-
come of the coin toss belongs to a certain subset of the sample space, for
example {HTT, HTH}?”. We refer to subsets of Ωas events. For exam-
ple, {HTT, HTH} is the event that the coin tosses result in either HTT or
HTH. Thus, the question to ask is, “What is the probability that such-and-
such a specific event occurs?”. In order to be able to answer this, we need
the concept of the set of all the events that we are interested in. This is
called the event space, usually denoted Σ.
What conditions should an event space satisfy? The most ‘basic’ event
is Ωitself, that is, the event that one of the possible outcomes occurs. This
event has probability one, that is, it always happens. It would thus make
sense to require the event space to contain Ω. Likewise, we shall assume
that the ‘null’ event ∅, which occurs with probability zero, is also in the
event space. Next, suppose that the events A = {HTT, THH} and B =
{HTH, HHH, HTT} are elements of Σ. It is natural to be interested in the
event that either A or B occurs. This is the union of the events, A ∪B =
{HTT, THH, HTH, HHH}. We would like Σ to be closed under the union
of two of its elements. Finally, if the event C = {HHH, HTH, HTT} is an
element of Σ, then the probability of it occurring is one minus the probability
that the complementary event Ω−C = {HHT, TTT, TTH, THT, THH}
occurs. Hence if an event is in Σ, we would also like its complement to be in
Σ. We can summarise the definition of the event space as follows.
Definition 4.2 The event space Σ is a set of subsets of the sample space
Ω, satisfying the following conditions:
1. Ω∈Σ.
2. if A, B ∈Σ, then A ∪B ∈Σ.
3. if A ∈Σ, then Ω−A ∈Σ.
Note that for our purposes, we can take Σ to be the power set (the set of all
subsets) of Ω. The power set of our example system is perhaps just slightly
too large to comfortably write out. It contains 28 = 256 elements.
Exercise 4.1 Show that the power set of Ωis a valid event space. Write
down the power set generated by two coin tosses.
30


## Single-Period Two-State Model

Exercise 4.2 How about the set {∅, Ω}? Does it satisfy the definition of an
event space?
The system consisting of the sample space and the event space (Ω, Σ)
might appropriately be called a ‘possibility system’, as opposed to a ‘prob-
ability system’ because all that it tells us are the possible outcomes of our
experiment. It contains no information about how probable each event is.
The so-called ‘probability’ measure is an additional ingredient, that must be
specified in addition to the pair (Ω, Σ).
4.3
Probability Measure
Now suppose that we want to assign a probability to each event in Σ. We
can do this by means of a probability measure P : Σ →[0, 1]. For any event
A ∈Σ, P[A] is the probability that the event A occurs. For example, if the
coin is fair, then the probability of any event XY Z occurring (where X, Y ,
Z can be either H or T) is clearly 1/8. Sometimes, instead of writing P[A]
for the probability of event A, we write Prob[A] to make the notation more
explicit.
Now, what conditions should we place on a probability measure? We have
already constrained its values to lie between zero and one. Since the event
Ωalways occurs, its probability is one. Finally, if we have two disjoint sets,
then the probability of their union occurring should be equal to the sum of
the probabilities of the disjoint sets. For example,
Prob[{HHH, TTT}]
=
Prob[{HHH}] + Prob[{TTT}]
=
1
4.
(4.2)
Combining these constraints leads to the definition
Definition 4.3 A probability measure P is a function P : Σ →[0, 1]
satisfying
1. P[Ω] = 1.
2. if σ, ρ ∈Σ and σ ∩ρ = ∅, then P[σ ∪ρ] = P[σ] + P[ρ].
Taken together, the sample space, event space and probability measure form
a so-called probability system, denoted P = (Ω, Σ, P).
31

Exercise 4.3 Assume that Σ is the power set of Ω, and that Ωhas a finite
number of elements. Show that a probability measure is uniquely defined by
its action on the single element sets of Σ.
Exercise (4.3) demonstrates why we can sometimes get away with only talking
about the sample space Ωand ignoring the more complicated event space Σ.
For example, if Ω= {ωi}N
i=1 is the sample space, then we call the set of
numbers {pi = P[ωi]}N
i=1 the probabilities of Ω. Knowing the ‘probabilities’
of Ωis then equivalent to knowing the full probability measure P, and so,
as long as the sample space is finite, we can use either formulation when
discussing a probability system P.
The key point to stress here is that we can in principle consider various
probability measures on the same sample and event spaces (Ω, Σ). This turns
out to be very useful in financial analysis. In our coin tossing example, we
have already considered the probability measure P that we obtain if the
coin that we are tossing is fair. However, we could also define a probability
measure Q : Σ →[0, 1] that is based on an ‘unfair’ coin. Suppose that for
the unfair coin we get heads with probability 1/3, and tails with probability
2/3. Then the probability measure is defined by the probabilities
Q({HHH})
=
1
27
Q({HHT})
=
q({HTH}) = q({THH}) =
2
27
Q({HTT})
=
q({TTH}) = q({THT}) =
4
27
Q({TTT})
=
8
27.
(4.3)
Both measures are, in principle, valid to consider, so that when we are talking
about probabilities related to the coin tossing, we must specify whether we
are ‘in’ the probability system P = (Ω, Σ, P), ‘in’ the probability system
Q = (Ω, Σ, Q), or possibly ‘in’ some other system based on another weighting
of the coins.
Exercise 4.4 What is the probability in the system P that there are exactly
two heads? What about in the system Q?
4.4
Random Variables
The final concept that we want to think about is that of a ‘real-valued func-
tion’ X defined on the sample space Ω. Thus X : Ω→ℜassigns to each
32

element ωi of Ωan element of ℜ, that is, a real number. We call such a func-
tion a random variable. Even though the function is itself deterministic, that
is, if we give X a definite input then we get a definite output, its argument
ωi is the random outcome of our physical experiment and hence X(ωi) is also
random. For example, X could be the function that counts the numbers of
heads,
X({HHH})
=
3
X({HHT})
=
X({HTH}) = X({THH}) = 2
X({HTT})
=
X({TTH}) = X({THT}) = 1
X({TTT})
=
0.
(4.4)
As a second example, X could be twice the difference between the number
of heads and the number of tails; or as a third example X could be 1 for
the element HHH and 0 for all the other elements of Ω. While these are
all different functions, they do have one important thing in common: they
are defined independently of any probability measure. That is, they depend
on the ‘possibility system’ (Ω, Σ), but not on a particular probability system
(Ω, Σ, P). Thus we could change probability measures from P to Q, and the
values of X would be unaffected.
However, what would be affected by a change of probability measure is
the probability that X would take on some given value. In particular the
expectation of X, which is the probability weighted sum over the sample
space of the possible values of the random variable, will depend on the prob-
ability measure that we are using. This is obvious from the formula for the
expectation,
EP[X]
=
n
X
i=1
P ({ωi}) X(ωi)
=
n
X
i=1
piX(ωi),
(4.5)
which clearly depends in a crucial way on the probability measure.
The
notation EP[X] is used to denote the expectation of the random variable X
with respect to the probability system P.
Going back to our example, suppose that we are in the ‘fair-coin’ proba-
bility system P. Then the expectation of the random variable X that returns
the number of heads is
EP[X] = 1.5,
(4.6)
33

while in the unfair ‘weighted-coin’ system Q, the expectation is
EQ[X] = 1.
(4.7)
So we have explicitly verified that the expectation of a random variable de-
pends on the probability system that we are using. If it is obvious which
possibility system that we are ‘in’, then we will talk about expectation with
respect to the relevant probability measure P, rather than with respect to
the probability system P = (Ω, Σ, P).
Exercise 4.5 Verify the expectation values calculated above in equations 4.6
and 4.7 . Calculate the expected values for the other two random variables
described in the text for both P and Q.
34

5
Back to the Casino
In this chapter we want to look at two things relating to the Casino. First,
we want to use the results of the previous chapter on probability systems to
interpret the derivative pricing result of chapter 3, and second, we want to
add in a non-zero interest rate. A non-zero interest rate affects the hedging
of the bet because it means that we have to pay in order to borrow money
to construct a hedged bet. This added cost must be added to the derivative
price in order to ensure that no arbitrage is possible.
5.1
The Casino as a Probability System
We begin by using the results of chapter 4 to describe the Casino as a proba-
bility system. The sample space Ωis simply the set of the two possible events,
{H, T}. The event space is the power set of this, Σ = {∅, {H}, {T}, Ω}.
These two sets define the ‘possibility’ system, (Ω, Σ). The payofffunction St
for a basic bet is a random variable defined on the possibility system, as is
any arbitrary derivative payofffunction ft(St).
As shown in exercise 4.3, we can uniquely define a probability measure
by its action on the sample space. We therefore can define the ‘physical’
probability measure P by
P[{H}] = p
and
P[{T}] = q.
(5.1)
What is it that this measure describes? Very simply it tells us the actual or
physical probability of the coin toss being heads or tails. However, a key point
of the derivative calculation was that the initial price of a derivative bet does
not involve these physical probability values. That is why the expectation
hypothesis fails. However, we can define a probability measure related to the
derivative pricing formula.
5.2
The Risk-Neutral Measure
Recall that in chapter 3 we found that the price of a derivative bet based on
the ‘no arbitrage’ valuation is given by the formula
f0 = p∗ft(U) + q∗ft(D),
(5.2)
where
p∗= S0 −D
U −D
and
q∗= U −S0
U −D .
(5.3)
35

The first thing to note is that p∗and q∗satisfy p∗, q∗≥0 and p∗+ q∗= 1.
This means that we can define a probability measure P ∗by
P ∗[{H}] = p∗
and
P ∗[{T}] = q∗,
(5.4)
and hence a probability system P∗= (Ω, Σ, P ∗). When calculating expecta-
tions in the P∗system we will abbreviate the notation by writing E∗instead
of EP∗. Note that the probability measure P ∗has nothing to do with the
‘physical’ probability measure P.
Suppose that we take the expected value of the derivative payofffunction
with respect to the P∗probability system. This yields
E∗[ft(St)]
=
p∗ft(U) + q∗ft(D)
=
f0.
(5.5)
In other words, the value of the derivative is given by the expectation of its
payofffunction with respect to the new probability system P ∗.
Moreover, in the special case when the derivative payofffunction is simply
the standard bet ft(St) = St, we see that
E∗[ft(St)]
=
E∗[St]
=
p∗U + q∗D
=
S0 −D
U −D U + U −S0
U −D D
=
S0.
(5.6)
We already know, of course, that the value of a derivative that pays offSt
dollars at time t is by definition S0 dollars. This is simply a statement of the
Casino rule that the basic stake of S0 dollars pays offSt dollars. But now we
see that
S0 = E∗[St].
(5.7)
In other words, the new probabilities p∗and q∗are precisely the ‘physical
weightings’ that the coin must have if the stake S0 were equal to its expected
value at time t. If this is the case then the expectation hypothesis actually
gives the correct price for derivatives!
We can interpret the P∗probability system in terms of the amount of risk
that a player is willing to take. If a player has no preference whether he (a)
holds onto his initial stake of S0 dollars, or (b) bets it with an expected return
36

of E[St] dollars, then the two strategies must have the same value to him,
that is, S0 = E[St]. Such players are called risk-neutral, or risk-indifferent
and expect that if they play many times, they will neither gain nor lose
money. For risk-neutral players to bet, the actual coin probabilities must be
p = p∗and q = q∗. Thus, we call the probability measure P ∗the risk-neutral
measure and the probability system P∗= (Ω, Σ, P ∗) the risk-neutral system.
In reality, we expect that players are either investors, who are by nature
risk-averse, only playing if S0 < E[St], or gamblers, who are risk-preferring,
and are willing to play if S0 > E[St] (which corresponds to a risk-averse
Casino).
5.3
A Non-Zero Interest Rate
Suppose that the Casino bank begins to charge interest on borrowed money
at a continuously compounded rate r. Similarly, it pays interest on deposits
at the same rate. As in the foreign exchange example of chapter 2, the value
of the interest rate will affect the derivative price. We therefore need to find
the new value for the purchase price f0 of a derivative, again by using a no
arbitrage argument.
Consider the following scenario for a dealer who starts with nothing. At
time 0 he sells a derivative with payofffunction ft(St) to a gambler. He
receives f0 dollars for selling the derivative and then hedges it by making a
basic bet of δS0 dollars with the Casino. As in the zero interest rate case, the
dealer wants his payout to be independent of the outcome of the coin toss,
so he picks δ such that δU −ft(U) = δD −ft(D). Solving this equation for
the hedge ratio we find that is still given by equation (3.7)
δ = ft(U) −ft(D)
U −D
,
(5.8)
and therefore is not affected by the presence of a non-zero interest rate.
However, the dealer’s basic bet is financed by borrowing δS0 −f0 dollars
from the bank at the interest rate r. Note that if δS0 −f0 is negative, then
the dealer deposits some money in the bank and gets it back with interest at
time t.
Now that we have described what happens before the coin toss, we need
to turn our attention to what happens after it. The dealer gets δSt dollars
from the Casino for his basic bet, but has to pay ft(St) dollars to the player
as part of the derivative contract. By the construction of the hedged bet,
37

this amount, δSt −ft(St) dollars, is a guaranteed quantity. Furthermore, the
amount that the dealer owes the Casino bank, (δS0 −f0)ert dollars, is also
a guaranteed quantity. Hence the dealer’s final position is risk-free. Since
he starts with no money, a guaranteed profit would be an arbitrage. This
implies that in an arbitrage-free Casino the dealer’s final position must be
zero,
δSt −ft(St) −(δS0 −f0)ert = 0.
(5.9)
If we substitute in for the hedge ratio δ from equation (5.8), then we can
solve this equation for f0 to obtain
f0 = e−rt[p∗ft(U) + q∗ft(D)],
(5.10)
where
p∗= S0ert −D
U −D
and
q∗= U −S0ert
U −D .
(5.11)
We can define the risk-neutral probability measure P ∗for the Casino with
non-zero interest rates by setting the probabilities to be
P ∗[{H}] = p∗
and
P ∗[{T}] = q∗.
(5.12)
The derivative price can therefore be written as
f0 = e−rtE∗[ft(St)],
(5.13)
where E∗[X] is the expectation of a random variable X using the risk-neutral
measure P ∗. This arbitrage argument differs from the zero interest rate case
only in the fact that the dealer has to pay interest on the money borrowed
to finance the initial hedged bet. The original argument and its values for
f0, p∗and q∗are recovered if we set r = 0 in the above result.
What is the significance of the factor e−rt in the derivative price? We can
think of it as follows. If a sure sum of money Xt is to be delivered at time t,
then its present value X0 is given by X0 = P0tXt, where P0t is the discount
factor. In general, we require that 0 ≤P0t ≤1, and that P0t is a decreasing
function of t. For example, if r is a constant and P0t = e−rt, then we say that
we have constant interest rates. The discount factor arises because of the
time-value of money, which takes into account the fact that a fixed amount
of money is worth more now than the same amount of money will be in the
future. This is because the risk-free interest rate allows the value of an initial
amount of money to grow in time. So the factor e−rt in the derivative price
can be thought of as a discount factor that is applied because the derivative
pays out at a time t in the future, rather than at t = 0 when it is purchased.
38

Exercise 5.1 Why must P0t be a decreasing function of t?
As we shall see in the following sections, the formula f0 = e−rtE∗[ft(St)] is
a good prototype for derivative pricing in general. In words, it says that the
present value of a derivative is equal to the discounted value of the risk-neutral
expectation of its payoff. Note, once again, that to value the derivative we do
not need to know the actual probabilities p and q for the results of the coin
flip.
We can verify the price for the special case of a derivative that pays off
ft(St) = St. We have
f0
=
e−rtE∗[St]
=
e−rt(p∗U + q∗D)
=
e−rt
ÃS0ert −D
U −D U + U −S0ert
U −D D
!
=
S0.
(5.14)
This shows that a derivative that has the same payoffs as the basic bet also
has the same initial price.
Exercise 5.2 In the case where there is an interest rate r, show how an
arbitrageur can still make a profit without risk if the dealer mispriced the
derivative.
Exercise 5.3 Suppose that the basic stake is $100, while the basic payoffs
are $105 and $95, for heads and tails respectively, and ert = 1.01. The actual
probabilities of heads and tails are p = .8 and q = .2.
(a) Calculate the risk-neutral probabilities p∗and q∗.
(b) Calculate the price of a derivative that pays offthe value 5 for heads
and nothing for tails. This is really a call option with a strike of $100.
(c) What is the value of the hedge ratio δ?
(d) Verify that the payoffof a bet consisting of being long δ units of the
basic bet, and short one derivative is independent of the coin toss.
(e) What is the price of the derivative if the actual probabilities of heads
and tails are p = 0.3 and q = 0.7?
39

Why do people gamble? Surely the answer must be that, despite losses
on average in cash terms, there is an implicit benefit—that is, an intangible
yield in the form of (say) pleasure, a fun evening out, interesting company,
the thrill of living dangerously, satisfaction of an uncontrollable urge, or
something along these lines. For fear of lapsing into a state of arm-chair
psychology, let us not say more on this. The implicit benefit obtained in this
way is formalised in the concept of a convenience yield. It is possible to price
derivatives using a particular convenience yield but this method suffers from
the fact that every player will have a different yield, and so no scheme that
will satisfy every gambler is possible. The advantage of arbitrage pricing is
that it is independent of the wishes or views of the players, and therefore can
be uniquely defined.
Summing up, we have seen here that the value of a derivative in the Casino
is given by the discounted risk-neutral expectation of its payofffunction,
f0 = e−rtE∗[ft(St)], where P ∗is the unique system of probabilities such that
S0 = e−rtE∗[St]. These relations were derived by applying the no arbitrage
condition to a hedged and hence risk-free bet.
Exercise 5.4 Verify that the risk-neutral measure P ∗, defined by equation
(5.11), is the unique probability measure that satisfies S0 = e−rtE∗[St], that
is, the basic bet is equal to its discounted expectation.
40

6
The Binomial Model
We return once more to the Casino, but this time we give it a different
interpretation: as a simple idealisation of a stock market. The ‘stake’ S0
at time 0 is now interpreted as the price of an asset.
One can think of
this as a ‘chip’ or ‘one share’. As a consequence of the ‘coin flip’, which
represents a random movement in the stock price, the asset is worth either
more (S1 = U), or less (S1 = D) at t = 1. Thus, we have a very elementary
model for a ‘stock market’, in this case a ‘one-period’ market, since there is
only one time step. In this chapter we shall expand this model and give the
definition and construction of n-period markets before pricing derivatives in
a one-period market. In the next chapter we turn our attention to the value
of derivatives in an n-period market. The techniques that we introduce here,
although very elementary in nature, have wide applications.
6.1
Tree Models
In order to deal with a more complex system than the simple one-period
market, we need to refine our current notation. Our convention will be to
use a subscript for the time variable, and a superscript to indicate the state
of the share price. Thus, initially the share price is S0 (there is only one
state, so we don’t need a superscript). At time 1 we have two states, so we
write Si
1, where i = 0, 1, as shown below:
S0©©©©
*
HHHH
j
S0
1
(0-state ‘up’)
S1
1
(1-state ‘down’)
(6.1)
Now we suppose that at time 2 each of the states Si
1 can evolve to a pair
of new states which we write as Sij
2 . The first index tells you which state you
were in at time 1, while the second index tells you whether you have an up
or down move following that, as illustrated in the following diagram:
41


## Forward Contracts and Futures

S0©©©©
* S0
1
HHHH
j S1
1
©©©©
* S00
2
HHHH
j S01
2
©©©©
* S10
2
HHHH
j S11
2
(6.2)
The resulting system of prices is called a tree model. For simplicity, we
shall consider trees which have two branches at each node, but in principle the
idea can be extended to the situation where we have any number of branches
at each node. We can display the system more compactly by suppressing the
branches and writing, for example,
S0 −→Si
1 −→Sij
2 −→Sijk
3 ,
(6.3)
for a three-period model. Note that by simply changing the allowed range for
the superscripts, this notation is general enough for any number of branches.
We also need to introduce notation for the probabilities with which the
various transitions occur. In compact form this is
S0
pi
0
−→Si
1
ˆpij
1
−→Sij
2
ˆpijk
2
−→Sijk
3 .
(6.4)
Thus, p1
0 is the probability that S0 will drop to S1
1. The corresponding tree
representation is given explicitly as follows:
S0©©©©
* S0
1
p0
0
HHHH
j S1
1
p1
0
©©©©
* S00
2
ˆp00
1
HHHH
j S01
2
ˆp01
1
©©©©
* S10
2
ˆp10
1
HHHH
j S11
2
ˆp11
1
(6.5)
Note that pi
0 gives the probability that S1 = Si
1, while ˆpij
1 is the conditional
probability that S2 = Sij
2 , given that S1 = Si
1. We will use a ‘hat’ throughout
42

the book to denote conditional probabilities. The actual probability that
S2 = Sij
2 is pij
01 = pi
0ˆpij
1 . Since the total probability at any node must be one,
we have P
i pi
0 = 1, P
j ˆpij
1 = 1, P
k ˆpijk
3
= 1, and so on. This notation means
that if we sum ˆpij over j for any fixed value of i, then the result is one, with
the analogous generalisation to the sum of conditional probabilities at later
times.
When convenient, we can drop the ‘time’ subscript from the share prices
because the time is simply equal to the number of ‘state’ indices. This yields
the less cluttered tree representation shown below:
S ©©©©
* S0
p0
HHHH
j S1
p1
©©©©
* S00
ˆp00
HHHH
j S01
ˆp01
©©©©
* S10
ˆp10
HHHH
j S11
ˆp11
(6.6)
The corresponding compact notation is
S
pi
−→Si
ˆpij
−→Sij
ˆpijk
−→Sijk.
(6.7)
6.2
Money Market Account
We have already considered the notion of borrowing in the Casino at a non-
zero interest rate. Now we need to formalise this idea further by introducing
the concept of a money market process that accumulates interest on a risk-
free basis. Let Bt denote the value of the money market account at time t.
For brevity, we shall sometimes refer to a unit in the money market account
as a ‘bond’, hence the notation Bt, which might also be taken to stand for
‘bank account’. Assuming that the interest rate is deterministic, then the
process is simply the linear tree:
B0 −→B1 −→B2 −→B3.
(6.8)
If interest rates are constant, then, as we proved in exercise 1.3, the value of
the money market account is
Bt = B0ert,
(6.9)
43

where r is the interest rate ‘per period’, expressed on a continuously com-
pounded basis. For example, if R is the annualised continuously compounded
interest rate, and if time is counted in days, then r = R/365. We will not
necessarily assume that interest rates are constant, but merely that they are
positive, so Bt+1 > Bt, that is, the bank account increases in value.
Buying a unit of the money market account at time t for the price Bt is
like ‘putting the amount Bt in the bank’. At time t + 1 it is worth a larger
amount Bt+1. Selling a unit of the money market account for the price Bt at
time t is like ‘borrowing the amount Bt’ from the bank. If you want to buy
it back again at time t + 1, that is, repay the loan, then you must pay Bt+1
for it—principal plus interest.
6.3
Derivatives
For a derivative we need to specify (a) the maturity date t, that is, the time
when it pays off, and (b) the payofffunction f. It is convenient to think of
the payoffas being determined by the state of the market at the payofftime,
so f = ft(St). For example, a derivative that pays offat t = 2 will have
a payofffunction f ij = f(Sij). Specification of the payofffunction is part
of the derivative contract, so the real problem is to determine the present
value, or initial cost f of the derivative. Indeed, since a derivative itself can
be viewed as an asset, we can express its time evolution in either the compact
form,
f −→f i −→f ij −→f ijk,
(6.10)
or as the following tree:
f
©©©©
* f 0
HHHH
j f 1
©©©©
* f 00
HHHH
j f 01
©©©©
* f 10
HHHH
j f 11
(6.11)
In order to make the derivative calculations somewhat more tangible, it
is worth considering some sample numerical exercises. A hypothetical share
price process is given as follows:
44

100 ©©©©
* 105
.5
HHHH
j 95
.5
©©©©
* 108
.7
HHHH
j 102
.3
©©©©
* 98
.7
HHHH
j 92
.3
(6.12)
For the money market account, we will assume a flat rate of 1% per month,
so the process can be represented by the diagram
100 −→101 −→102.01,
(6.13)
where each time step is one month.
Exercise 6.1 In the given hypothetical two-period stock market what are the
probabilities that (a) S2 = 102 and (b) S2 > 95?
Exercise 6.2 What is the value of r for the money market process given by
equation (6.13), assuming that the interest is continuously compounded at an
annualized rate r?
Exercise 6.3 Using what you have learned in chapter 3, calculate the values
of call options with a maturity of t = 1 and strike prices of $98 and $102.
How much would similar derivative costs if you bought them at time 1 for
exercise at time 2? Note that in this case you need to calculate two prices for
each call option, one in the event that S1 = 105 and one for the case when
S1 = 95. Finally, how much would you be willing to pay at time 0 for the
call options with a maturity of t = 2?
6.4
One-Period Replication Model
We now want to price the derivative by using a no arbitrage argument. As
in the case of the Casino analogy, the investor will buy a derivative from a
trader, who will then take the proceeds of this sale and invest in the stock and
money market so that the randomness in his stock and derivative positions
cancel. By hedging in this way, the trader can obtain a guaranteed payoff
when the derivative expires, at which point he collects the proceeds from his
45

stock and money market positions and pays the investor any money due on
the derivative. By the no arbitrage condition, this guaranteed payout must
be zero, since the trader started with nothing. If it were less than zero, the
trader wouldn’t trade; whereas if it were more than zero, then the investor
wouldn’t invest.
To actually calculate the initial price of a derivative, we now need to turn
these words into equations. Hence, suppose that we have a trader with no
initial position and an investor that is flush with cash. At time 0 the investor
buys a derivative with payofff i at t = 1 from the trader. The investor pays
f dollars, the value of the derivative at t = 0, to the trader, who then uses
the money to take a position in the stock S and the money market account
B. Let β be the number (possibly fractional, possibly negative) of units in
the money market account that the trader buys, and δ the number of units
in the stock S. Since this purchase is entirely funded by the money received
from the sale of the derivative, we have
f = βB + δS.
(6.14)
How does the trader choose the values of β and δ? Well, his position at
time 1 is equal to the value of his stock and bond portfolio βBi + δSi, minus
the derivative payment f i that he must make to the investor, and most
importantly, the trader would like this amount to be risk-free. By the no
arbitrage condition, the value of this position must be zero, that is,
βBi + δSi −f i = 0,
(6.15)
or
f i = βBi + δSi.
(6.16)
Because the bond and stock portfolio exactly duplicates the payofffunction of
the derivative, we call it a replicating strategy. The existence of a replicating
strategy means that the derivative can be constructed from the underlying
assets and hence an investor need never buy the derivative—he can do just
as well by taking positions in stocks and bonds. In the real world, however,
a derivative has lower transaction and maintenance costs and that is why
investors will purchase them.
Since equation (6.16) must hold independent of the ‘up’ or ‘down’ move-
ment of the share price, we must have
f 0 = βB1 + δS0
and
f 1 = βB1 + δS1.
(6.17)
46

We can then solve these two equations for β and δ,
β = f 1S0 −f 0S1
B1(S0 −S1)
and
δ = f 0 −f 1
S0 −S1,
(6.18)
where we have assumed that S0 > S1. Substituting these expressions back
into equation (6.14) we obtain
f = f 1S0 −f 0S1
B1(S0 −S1)B + f 0 −f 1
S0 −S1S,
(6.19)
which completely determines the value of the derivative. Rearranging this
expression, we get
f =
S −S1 B
B1
S0 −S1 f 0 +
S0 B
B1 −S
S0 −S1 f 1,
(6.20)
or alternatively
f = B
B1
"S B1
B −S1
S0 −S1 f 0 + S0 −S B1
B
S0 −S1 f 1
#
.
(6.21)
Exercise 6.4 Compare the derivative price equation (6.21) with the Casino
price equation (5.13). Show that they are equivalent.
6.5
Risk-Neutral Probabilities
As in the Casino example, we see that the derivative price, given by equation
(6.21), is independent of the ‘physical’ probabilities pi. Instead of the physi-
cal probabilities, we want to define the risk-neutral probability measure P ∗,
generated by the probabilities
p0
∗=
˜S −S1
S0 −S1
and
p1
∗= S0 −˜S
S0 −S1,
(6.22)
where ˜S = B1
B S.
Exercise 6.5 Verify that the probabilities p0
∗and p1
∗do generate a valid prob-
ability measure.
47

The initial price of the derivative can therefore be written as
f
=
B
B1
[p0
∗f 0 + p1
∗f 1]
=
B
B1
E∗[f1],
(6.23)
where f1 is the random payoffof either f 0 or f 1 at time 1 and E∗[−] is the
expectation with respect to the risk-neutral measure P ∗. Since B and B1 are
deterministic, the derivative pricing formula (6.23) can be expressed in the
form
f
B = E∗[ f1
B1
].
(6.24)
In other words, the ratio f/B of the present value of the derivative to the ini-
tial cost of the money market account is given by the risk neutral expectation
of this ratio at t = 1.
But in what sense is this new probability system ‘risk-neutral’? We need
to verify that the probabilities pi
∗are indeed the probabilties that would apply
in reality if investors were really ‘indifferent’, that is, neutral to risk. In this
situation (risk indifference) investors would expect the same rate of return
(average profitability per unit investment) on both (a) an investment in the
stock market, and (b) an investment in a money market account. In equation
form, this means that
E∗[S1]
S0
= E∗[B1]
B
.
(6.25)
Note that Bt is actually deterministic, so E∗[B1] = B1. After expanding
E∗[S1] in terms of the risk-neutral probabilities, we have
S0p0
∗+ S1p1
∗
S0
= B1
B ,
(6.26)
where p0
∗+ p1
∗= 1. These relation imply, after a short calculation, that
p0
∗=
˜S −S1
S0 −S1
and
p1
∗= S0 −˜S
S0 −S1,
(6.27)
where
˜S = S B1
B ,
(6.28)
which is the same result as equation (6.22). This verifies the interpretation
of the probabilities pi
∗as risk-neutral.
48

Exercise 6.6 Calculate the forward price at time 0 for the purchase at time
1 of one share.
49


## Pricing in N-Period Tree Models

7
Pricing in N-Period Tree Models
Equation (6.21) completely determines the price of a derivative in a one-
period market. So it is clearly time to expand our model and think about
something a little more complicated! Consider a two-period market with a
stock, a money market account, and a derivative. We know the values in
the stock process, as illustrated in (6.6), and in the bond process, shown in
(6.8). We also know the terminal values or payoffof the derivative process
f ij, that is, the final values of the tree (6.11).
Our goal is to use a no
arbitrage argument to compute the rest of the derivative process, including,
in particular, its present value f0, that is, today’s price.
From the work that we have done on the one-period model, it should be
clear that if we determine the possible values f 0 and f 1 of the derivative at
time 1, then we can determine its value at time 0 by use of equation (6.24).
Now consider the situation at time 1, and suppose that the outcome of the
first period was an upward movement (‘heads’), so S →S0. Then the stock
has value S0, the bond has value B1, and we must find the value f 0 of a
derivative that pays offeither f 00 or f 01 depending on whether S0 →S00 or
S0 →S01. But clearly the problem now posed is formally identical to the
original problem for a one-period derivative, as we can see from the relevant
tree diagrams:
S0©©©©
* S00
ˆp00
∗
HHHH
j S01
ˆp01
∗
B1
- B2
(7.1)
f 0 ©©©©
* f 00
HHHH
j f 01
We might call this realization an ‘inductive insight’.
Since we can price
derivatives in a one-period model using equation (6.21), we can determine
the value of f 0 by simply using the same formula.
50

So, using equations (6.22) and (6.24) we can immediately write down the
solution in the form
f 0
B1
= f 00ˆp00
∗+ f 01ˆp01
∗
B2
,
(7.2)
where
ˆp00
∗=
˜S0
12 −S01
S00 −S01,
ˆp01
∗= S00 −˜S0
12
S00 −S01,
(7.3)
and ˜S0
12 = S0B2/B1 is the conditioned forward price made at time 1, when
the stock has value S0 (‘up’ state) for delivery of a share at time 2. More
generally, the random variable ˜S12 is is the forward price that will be made
at time 1 for purchase of a share at time 2. It can take on two values, ˜Si
12,
(i = 0, 1) depending on the actual value Si of the stock at time 1.
Exercise 7.1 Use an arbitrage argument to show that if S1 = S0
1 at time
t = 1, then the value of the derivative must be f 0, as given in equation (7.2).
Similarly for f 1, equations (6.22) and (6.24) tell us that
f 1
B1
= f 10ˆp10
∗+ f 11ˆp11
∗
B2
,
(7.4)
where
p10
∗=
˜S1
12 −S11
S10 −S11,
p11
∗= S10 −˜S1
12
S10 −S11,
(7.5)
and ˜S1
12 = S1B2/B1 is the forward price made at time 1, when the stock has
value S1, for delivery and payment at time 2.
But now we know f 0 and f 1. Thus, we can substitute these values back
into equation (6.24) to obtain the initial price of the derivative, given by
f
B
=
f 0p0
∗+ f 1p1
∗
B1
=
f 00p0
∗ˆp00
∗+ f 01p0
∗ˆp01
∗+ f 10p1
∗ˆp10
∗+ f 11p1
∗ˆp11
∗
B2
=
f 00p00
∗+ f 01p01
∗+ f 10p10
∗+ f 11p11
∗
B2
,
(7.6)
51

where we have used the fact that pi
∗ˆpij
∗= pij
∗is the risk-neutral probability
that S goes to Sij. Thus, we see that the final equation is an expectation in
the risk-neutral measure,
f
B = E∗
" f2
B2
#
,
(7.7)
where f2 is the random payoffof the derivative at time 2.
The financial interpretation of this result is that the probabilities pi
∗and
ˆpij
∗yield the unique probability system such that the expected return from
an investment in the money market account equals the expected return if the
money were put in the stock market instead. Thus,
B1
B0
= E∗[S1]
S0
and
B2
B0
= E∗[S2]
S0
(7.8)
Exercise 7.2 Verify that the relations given in equation (7.8) hold. Do these
conditions uniquely define a probability measure?
Exercise 7.3 Calculate the risk-neutral probabilities for the numerical ex-
ample illustrated in 6.12. Price the following derivatives:
(a) f ij = Sij, i.e., the derivative simply pays offthe value of the stock.
(b) A forward contract with a strike price of $100.
(c) A European call option with a strike of $100.
(d) A European put option with a strike of $100.
(e) A call option that expires at t = 1 with a strike of $3 on a forward
contract with a strike price of $100.
(f) A derivative that pays out the difference if the share price falls below
$97, summed over both time periods. That is, the payofffunction is
max[97 −S2, 0] + max[97 −S1, 0] dollars. This is a ‘path-dependent’
derivative because the final payout depends on the entire path that the
share price takes, rather than just its final value.
(g) A digital contract that pays out $10 if the share price is above $100.
(h) Both a European and an American call option with strikes of $104.
52

Exercise 7.4 Compute the entire system of risk-neutral probabilties pi
∗, ˆpij
∗
and ˆpijk
∗
for a three-period binomial model.
So what have we learned about pricing in the tree model so far? We have
shown that in a one-period market, a derivative is priced according to the
rule
f0
B0
= E∗[f1]
B1
,
(7.9)
while in a two-period market we used this result inductively to deduce that
f0
B0
= E∗[f2]
B2
.
(7.10)
Moreover, in an N-period binomial market model, a ‘backward induction’
argument can be made that the price of a derivative f0 at t = 0 with random
payout fN at t = N is given by
f0
B0
= E∗[fN]
BN
(7.11)
where BN is the value of the money market account at t = N, fN is the
random value of the derivative at time N, and E∗[−] is the expectation in
the risk-neutral measure determined by use of the one-period relation (6.22)
at each node of the tree.
Exercise 7.5 Verify equation (7.11) explicitly in the case of a three-period
market.
Exercise 7.6 Complete the backwards induction argument to prove equation
(7.11).
53


## Martingales and Conditional Expectation

8
Martingales and Conditional Expectation
We are now at a point where we have an algorithm that can be used to
evaluate the initial price of any derivative with a known payofffunction.
Before proceeding further, we want to formalise some of the probabilistic
concepts that we have been dealing with and which will reappear in the
continuous time setting. Instead of the coin tosses considered in section 4 we
will use the two-period tree model as the underlying ‘random’ experiment.
The sample space is
Ω= {UU, UD, DD, DU},
(8.1)
where U indicates an ‘up’ movement in the stock market and D a ‘down’ one.
We assume that the event space Σ is the power set of Ω. The share price S2
at time 2 is a random variable that takes the values Sij depending on the
up and down movements in the markets. How about the share price S1 at
an earlier time 1? It is also a random variable defined on the same sample
space, but unlike S2, it should not depend on the movements of the market
after time 1. This means that S1(UU) = S1(UD) and S1(DD) = S1(DU).
This discussion has illustrated the two concepts that we want to discuss next:
stochastic processes and filtrations.
8.1
Stochastic Processes
The share price process Si that we have been dealing with so far is really a
family of random variables indexed by a time parameter i. That is, there are
three random variables S0, S1 and S2 defined on the sample space Ω. This
is an example of a stochastic process.
Definition 8.1 A stochastic process X is a sequence of random variables
{Xn}K
n=1 defined on the sample space Ω.
8.2
Filtration
Suppose that instead of being concerned with only the final outcome of the
share price movements, we want to be able to describe the share price at
any time before the final time. For example, we could evaluate the share
price stochastic process Si for each time i at the sample space element UU:
S0(UU) = S at time 0, S1(UU) = S0 at time 1 and S0(UU) = S00 at time
2. Note that at times before the final time, while the sample space is always
54

the same, the elements of it that can be differentiated from one another may
not always be the same. For example, at time 0 it is impossible to tell any
of the elements of the sample space apart, so the members of the set
F0 = {UU, UD, DU, DD}
(8.2)
all ‘appear’ the same. Similarly at time 1 it is possible to divide the sample
space up into two distinguishable ‘partitions’
F 0
1 = {UU, UD}
and
F 1
1 = {DU, DD},
(8.3)
depending on whether the initial movement in the market was ‘up’ or ‘down’.
Finally at time 2, there are four different market states, that we can differ-
entiate between
F 00
2
= {UU},
F 01
2
= {UD},
F 10
2
= {DU},
and
F 11
2
= {DD}.
(8.4)
Each of these collection of sets F0, F i
1 and F ij
2
divides up or ‘partitions’
the sample space at the relevant time. We can formalise the definition of a
partition.
Definition 8.2 A partition {Fi}K
i=1 of a set A is a family of mutually disjoint
subsets of A whose union is A. That is, for i ̸= j, Fi ∩Fj = ∅, and ∪K
i=1Fi =
A.
From our example we see that associated with the random movements of the
market there is a natural sequence of partitions of the sample space in terms
of F0, F i
1 and F ij
2 . We call such a sequence a filtration, which we formally
define below.
Definition 8.3 A filtration F is a family {Fi}K
i=1 of partitions of Ω. The
notation that we use for an element of the filtration is Fi = {F (i)
j }Ki
j=1, where
the sets F (i)
j
are a partition of the sample space. An additional constraint that
we require is that the partitions at later times respect the earlier partitions.
That is, if i < k, then every partition F (l)
i
at the earlier time is equal to the
union of some set of partitions {F (jn)
k
}
Ni,k
n=1 at the later time.
Thus the sets Fi that we have defined above are a valid filtration for the
market sample space because at each time they partition the sample space,
and because the partitions at later times respect the partitions at earlier
55

times, for example, F0 = F 0
1 ∪F 1
1 . Using the concept of a filtration F allows
us to define a ‘filtered possibility system’ (Ω, Σ, F) and a ‘filtered probability
system’ (Ω, Σ, F, P). It gives some sort of ‘time ordering’ to the possibility
or probability system.
8.3
Adapted Process
Suppose that we had a stochastic process X defined on the market possibility
system such that X1(UU) ̸= X1(UD). This means that the process needs to
know at time 1 what happens at time 2. We do not want this. Another way
to look at it is that X1 is not constant on the partition F 0 defined by the
filtration F. This leads to the following definition.
Definition 8.4 A stochastic process X is adapted to a filtration F if at every
‘time step’ n, whenever ω and σ belong to the same partition F (n)
j
defined by
the filtration then Xn(ω) = Xn(σ). That is, Xn is constant on each partition
at time n.
The share price process is clearly adapted to the filtration that we have de-
fined for the market. The only stochastic processes that we will be interested
in are adapted ones.
8.4
Conditional Expectation
The conditional probability for an event A given an event B is the probability
that A occurs when we alreay know that B occurs. It is equal to
P(A|B) = P(A
and
B)
P(B)
.
(8.5)
In particular, we will be interested in the case when A is a single element
set, and B is an element of a filtration, for example P({ωi}|{F (j)
k }). More
concretely, taking an example from the market system,
P({UU}|{UU, UD}) = ˆp00,
(8.6)
is the probability that we have two up movements, given that we know that
the first market move was up.
56

We can use the conditional probability to define the conditional expecta-
tion of a random variable
E[X|σ] =
N
X
i=1
X({ωi})P({ωi}|σ).
(8.7)
Again, drawing on the market system, we could consider
E[S2|F 0] = S00ˆp00
∗+ S01ˆp01
∗,
(8.8)
which is the expected value of the share price at time 2, given that the initial
market move was up.
Define the stochastic process
Ym(ωi) = E[S2|F (m)
k
],
(8.9)
where ωi ∈F (m)
k
. That is, at time m we evaluate the conditional expectation
of the share price at time 2 given the filtration at time m. For example,
Y1({UU}) = E[S2|F 0],
(8.10)
which was evaluated above. We will use the notation Ym = Em[S2] to denote
the conditional expectation of S2 given information up to time m. Note that
since the filtration at time 0 is unable to distinguish between any elements,
we have E[Sn] = E0[Sn].
Exercise 8.1 Verify that the stochastic process Ym is adapted to the filtration
F.
Recall that from the derivative pricing formulae we have
S0
B0
= E∗
0
· S2
B2
¸
and
S0
B0
= E∗
0
· S1
B1
¸
,
(8.11)
where we have inserted some suggestive zeros. By a simple calculation we
could verify that
S1
B1
= E∗
1
· S2
B2
¸
.
(8.12)
This is an important example of the next concept that we want to consdier—a
martingale.
57

8.5
Martingales
A stochastic process X is called a martingale (with respect to a filtered
probability system (Ω, Σ, P, F), if it satisfies
Xm = Em[Xn]
∀m ≤n ≤N.
(8.13)
The standard definition of a martingale also requires that
Em[|Xn|] < ∞
∀m ≤n ≤N,
(8.14)
i.e., it exists for all valid m, n.
However, this condition is automatically
satisfied in our model. If a process is a martingale, then it means that its
expected value at any later time is equal to its current value.
8.6
Financial Interpretation
Let us go back and actually verify that the ratio of the stock to bond process
is a martingale. In the case of a two-period market we have
S0
B1
=
ˆp00
∗S00 + ˆp01
∗S01
B2
=
E∗
· S2
B2
|F 0
¸
(8.15)
and
S1
B1
=
ˆp10
∗S10 + ˆp11
∗S11
B2
=
E∗
· S2
B2
|F 1
¸
,
(8.16)
which says that given that the system is in the state S0 at time 1, the ratio of
the stock to bond price can be expressed in terms of conditional probabilities
ˆp00
∗
and ˆp01
∗, and similarly for S1, ˆp10
∗
and ˆp11
∗.
Writing this in terms of
conditional expectation, we then obtain
S1
B1
= E∗
1
· S2
B2
¸
.
(8.17)
In fact, using the one-period argument to derive the risk-netural probabilities
we have for n ≤N,
Sn−1
Bn−1
= E∗
n−1
· Sn
Bn
¸
,
(8.18)
58

or, more generally, by induction we have
Sm
Bm
= E∗
m
· Sn
Bn
¸
(8.19)
for m ≤n.
Exercise 8.2 Verify equation (8.19) for the three-period binomial model.
Thus, in the risk-neutral measure the ratio of the share price Sn to the
money market account Bn is a martingale.
This can be regarded as the
definition of the risk-neutral measure. Alternatively, we say that the risk-
neutral probability measure P ∗is a martingale measure for the ratio Sn/Bn.
The no arbitrage argument for derivative pricing, combined with a back-
wards induction, allows us to deduce, in the case of an N-period binomial
model, that
fm
Bm
= E∗
m
" fn
Bn
#
,
(8.20)
for 0 ≤m ≤n ≤N. In other words: the ratio of the derivative price to the
money market account is a martingale. In particular, if N is the payoffdate
of the derivative, then
f0
B0
= E∗
" fN
BN
#
.
(8.21)
So, once we show that the ratio of the derivative price to the money market
account is a martingale in the risk-neutral measure, that is, equation (8.20)
holds, then we can ‘price’ the derivative by use of (8.21). It will be a crucial
relation when we come to pricing derivatives in the continuous time case.
59


## Binomial Lattice Model

9
Binomial Lattice Model
The general kind of tree model that we have been discussing so far is some-
times called a ‘bushy tree’, since the number of branches gets large very
quickly. At time n there are 2n states, which as n grows larger clearly makes
the tree computationally unfeasible. A very useful special model is obtained,
however, by letting the branches recombine to form a lattice of prices, and
hence is called a ‘lattice model’ or ‘recombining tree’. At time t = n the
number of different states is only n + 1 which grows much more slowly than
the 2n nodes of the ‘basic’ tree.
At each node, the asset price can move either up in value, with probability
p, by a multiplicative factor u, or down, with probability q, by a factor d.
Index the nodes at each time by the number of ‘down’ moves that you need
to reach it, for example, S1
3 is the node at time 3 with one ‘down’ and two
‘up’ movements. We can write the value of the ith node at time n as
Si
n = S0un−idi
(9.1)
where i = 0, . . . , n and the time index is now necessary. Thus, for example,
S0
2 = S0u2, S1
2 = S0ud, and so on. A three-period recombining tree is shown
below:
S0©©©©
* S0u
p
HHHH
j S0d
q
©©©©
* S0u2
p
HHHH
j S0ud
q
©©©©
*
p
HHHH
j S0d2
q
©©©©
* S0u3
p
HHHH
j
q
©©©©
* S0u2d
p
HHHH
j S0ud2
q
©©©©
*
p
HHHH
j S0d3
q
(9.2)
Suppose that at each node the actual probability of an up move is p, and
a down move is q. Then, the probability of Sn taking on a specific value Si
n
is
Prob[Sn = Si
n] = Cn
i pn−iqi,
(9.3)
where Cn
i is the standard binomial coefficient, given by
Cn
i =
n!
i!(n −i)!,
(9.4)
60

e.g., C3
2 = 3!/(2!1!) = 3. The factor Cn
i is the number of different ways of
arriving at the node Si
n.
Exercise 9.1 Show that the number of different ways of arriving at the node
Si
n is Cn
i .
Recall that Cn
i is called the binomial coefficient because
(x + y)n =
n
X
i=0
Cn
i xn−iyi.
(9.5)
Hence if we set x = p and y = q then using the fact that p + q = 1, we see
that
n
X
i=0
Cn
i pn−iqi = 1.
(9.6)
This means that if we sum the probabilities (9.3) of each node at the nth
time step, then we get one, as we should.
However, in order to price derivatives, we know that we do not need to
make any assumptions about the ‘physical’ probabilities, that is, the num-
bers p and q, but instead, we must calculate the appropriate risk-neutral
probabilities. For the bank account process, we assume for simplicity a con-
stant interest rate of r per period, continuously compounded, so Bn = B0ern.
Then, for risk-neutrality, we want
S0
B1
B0
= E∗[S1] = p∗S0u + q∗S0d
(9.7)
at the first node. In fact, the probabilities are governed by essentially the
same equation at each node. For example, at the node S1
2 = S0ud we want
S0udB3
B2
=
E∗[S3]
=
p∗S0u2d + q∗S0ud2,
(9.8)
but this reduces to the previous equation. The solution for p∗, q∗is easily
seen to be
p∗= er −d
u −d
and
q∗= u −er
u −d .
(9.9)
Exercise 9.2 Verify that equation (9.9) is consistent with the risk-neutral
probabilities calculated in the general theory of tree models developed earlier.
61

In the risk-neutral measure, the lattice is highly structured, which makes
calculations easy. In particular, we can price derivatives. The risk-neutral
probability of any state Si
n is
Prob∗[Sn = Si
n] = Cn
i pn−1
∗
qi
∗,
(9.10)
where Prob∗denotes probability in the risk-neutral measure P ∗. Thus, sup-
pose f0 is the price of a derivative (at time 0) with specified payofff i
n at time
n in the ith state. Then, from our general theory of tree models, we know
that
f0
B0
= E∗[fn]
Bn
,
(9.11)
from which it follows that
f0 = e−rn
n
X
i=0
Cn
i pn−i
∗
qi
∗f i
n.
(9.12)
This is the binomial derivative pricing formula which, together with its vari-
ous generalizations, has many useful applications. In the case of a call option
with strike K, for example, we would insert
f i
n
=
max[Si
n −K, 0]
=
max[S0diun−i −K, 0]
(9.13)
for the payofffunction f i
n.
Exercise 9.3 For a three-period model with S0 = $100, p = 0.6, r = 1.01,
u = 1.01 and d = 0.99, construct the lattice of stock prices and probabilities,
calculate the risk-neutral probabilities for the lattice, and then price a call
option with strike $100.
62


## Relation to Binomial Model

10
Relation to Binomial Model
We shall now show how in a suitable limit the binomial lattice model of
chapter 3 can give rise to the Wiener model for asset price movements.
10.1
Limit of a Random Walk
Consider an n-period lattice. Recall that at any node of the lattice we have
an ‘up’ and a ‘down’ branch, with probabilities p and q respectively, as shown
below From an initial value of S0, the asset price will increase to S0u with
probability p, or decrease to S0d with probability q.
S0©©©©
* S0u
p
HHHH
j S0d
q
(10.1)
.
Let δt be the time-step to the next node, and since there are n steps, the
final time will be t = nδt. Suppose moreover that the up and down factors
are given explicitly by
u = e˜µδt+σ
√
δt
and
d = e˜µδt−σ
√
δt,
(10.2)
where ˜µ and σ are constants. We shall assume that the actual probabilities
p and q (i.e., not the risk-neutral probabilities) are each 1
2. If we let Xn be
the random variable equal to the number of ‘up’ movements after n steps,
then the asset price St is
St = S0uXndn−Xn,
(10.3)
where n −Xnis the number of ‘down’ movements. Substituting in the values
of u and d given above then yields
St = S0 exp
"
˜µt + σ
√
t 2Xn −n
√n
)
#
.
(10.4)
The random variable Xn has a binomial distribution, with mean
1
2n and
variance 1
4n. We can improve the notation here slightly by defining the new
random variable
Zn ≡2Xn −n
√n
,
(10.5)
63

which has a binomial distribution with mean zero and variance one. Hence
the asset price process is given by
St = S0 exp
h
˜µt + σ
√
tZn
i
.
(10.6)
Next we use the central limit theorem, which says that if A1, A2, . . . are inde-
pendent, identically distributed random variables with mean m and variance
V , and Xn is the sum Xn = A1 + A2 + · · · An, then the random variable Zn
defined by Zn = (Xn −nm)/
√
nV →N(0, 1) for large n. This tells us that in
the limit of large n, Zn converges to a normally distributed random variable
with mean zero, and variance 1. Thus, it follows that
lim
n→∞St = S0 exp[˜µt + σWt]
(10.7)
where Wt is a normally distributed random variable with mean zero and
variance t. Then if we set ˜µ = µ −1
2σ2, the asset price process becomes
lim
n→∞St = S0 exp[µt + σWt −1
2σ2t],
(10.8)
and we are back to the Wiener model. Or so it appears. To show that we
have recovered the model entirely, we still need to show that Wt is indeed the
Wiener process—we know that it is normally distributed, but now we need
to check that it has independent increments. This follows intuitively from
the fact that the binomial process is defined as n independent measurements,
and hence, by construction, has independent increments. When we take the
large n limit, we are tempted to believe that this property is preserved, so
(10.8) actually is the Wiener process.
10.2
Martingales associated with Random Walks
This is, of course, a rather simplistic ‘derivation’ of the Wiener process, and
does not yet fully exploit the technology that we developed for the binomial
model. To proceed further, we begin by refining the binomial lattice model
by consideration of a certain family of martingales that arise naturally in this
context.
Lemma 10.1 Suppose Y1, Y2, . . . are independent, identically distributed ran-
dom variables with the property that the moment generating function,
M(θ) = E[eθY1],
(10.9)
64

exists (i.e., is finite) for some value of θ.
Define a sequence of random
variables by Z0 = 1, and
Zn = eθ(Y1+Y2+···+Yn)
[M(θ)]n
.
(10.10)
Then
En[Zm] = Zn,
m ≥n
(10.11)
where En is the conditional expectation given information up to time n (in
this case, given Y1, Y2, . . . , Yn) .
Proof By definition, we have
En[Zm] = En
"eθ(Y1+Y2+···+Ym)
[M(θ)]m
#
.
(10.12)
Since the expectation is conditional, we know the values of Y1, Y2, . . . , Yn,
and hence can take them outside the expectation, so
En[Zm] = eθ(Y1+Y2+···+Yn)
[M(θ)]n
E
"eθ(Yn+1+Yn+2+···+Ym)
[M(θ)]m−n
#
(10.13)
But then since the Yi’s are independent and identically distributed, we can
factor their expectation, which will then cancel with the factors of the mo-
ment generating function in the denominator,
E
"eθ(Yn+1+Yn+2+···+Ym)
[M(θ)]m−n
#
=
E
h
eθYn+1
i
E
h
eθYn+2
i
× · · · × E
h
eθYm
i
[M(θ)]m−n
= 1.
(10.14)
Hence,
En[Zm] = eθ(Y1+Y2+···+Yn)
[M(θ)]n
= Zn
(10.15)
as desired.
For example, if Y1 is normally distributed with mean m and variance V ,
it follows that
M(θ) = E[eθY1] = eθm+ 1
2θ2V ,
(10.16)
65

so
Zn = eθ( ˜Y1+ ˜Y2+··· ˜Yn)−1
2 nθ2V
(10.17)
where ˜Yi = Yi −m (i.e., remove the mean). But, this is clearly the product
Zn = eθ ˜Y1−1
2 θ2V eθ ˜Y2−1
2 θ2V · · · eθ ˜Yn−1
2 θ2V
(10.18)
which is given multiplicatively by a series of exponential martingales.
Another example, which is the one we are particularly interested in here,
is generated when Yi = ±1, so Y1 + Y2 + · · · + Yn is the random variable
corresponding to the nth step of a random walk. Then
M(θ) = peθ + qe−θ
(10.19)
where p, q are the probabilities respectively for Yi = ±1, and thus we have
Zn = eθ(Y1+Y2+···+Yn)
(peθ + qe−θ)n
(10.20)
Equivalently, we have
Zn =
eθXn
(peθ + qe−θ)n
(10.21)
where Xn = Y1+Y2+· · ·+Yn is the random walk. We note that E[Yi] = p−q.
Thus, E[Xn] = n(p−q), and we have ˜Xn = Xn −n(p−q), where E[ ˜Xn] = 0.
Now suppose that we consider the case where p = q = 1
2. Then we have
Zn =
eθXn
[ 1
2(eθ + e−θ)]n
(10.22)
and E[Xn] = 0. Now, suppose that we set
St = S0eµt
eσ
√
δtXn
[ 1
2(eσ
√
δt + e−σ
√
δt)]n,
(10.23)
where t = nδt. Then we can write
St = S0eµt
eσ
√
t(Xn/√n
[ 1
2(eσ
√
t/√n + e−σ
√
t/√n)]n.
(10.24)
66

In the limit n →∞, the numerator Xn/√n converges to an N(0, 1) random
variable, whereas for the denominator we have
1
2(eσ
√
t/√n + e−σ
√
t/√n) = 1 + σ2t
2n + O(n−2).
(10.25)
So as n →∞,
·1
2(eσ
√
t/√n + e−σ
√
t/√n)
¸n
→e
1
2σ2t
(10.26)
Thus, in the limit n →∞, we find that St converges to
St = S0eµteσ
√
tX−1
2 σ2t,
(10.27)
where X has an N(0, 1) distribution, and hence
√
tX has an N(0, t) dis-
tribution. This confirms in rather more detail the result that we deduced
earlier.
67

