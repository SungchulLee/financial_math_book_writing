# Arbitrage Pricing & Martingale Measures

!!! info "Source"
    **Mathematics of Financial Markets** by Robert J. Elliott and P. Ekkehard Kopp, Springer, 2nd ed., 2005.
    These notes are used for educational purposes.

## Pricing by Arbitrage

Chapter 1
Pricing by Arbitrage
1.1
Introduction: Pricing and Hedging
The ‘unreasonable effectiveness’ of mathematics is evidenced by the fre-
quency with which mathematical techniques that were developed without
thought for practical applications find unexpected new domains of appli-
cability in various spheres of life. This phenomenon has customarily been
observed in the physical sciences; in the social sciences its impact has per-
haps been less evident. One of the more remarkable examples of simulta-
neous revolutions in economic theory and market practice is provided by
the opening of the world’s first options exchange in Chicago in 1973, and
the ground-breaking theoretical papers on preference-free option pricing by
Black and Scholes [27] (quickly extended by Merton [222]) that appeared
in the same year, thus providing a workable model for the ‘rational’ market
pricing of traded options.
From these beginnings, financial derivatives markets worldwide have
become one of the most remarkable growth industries and now constitute
a major source of employment for graduates with high levels of mathemat-
ical expertise. The principal reason for this phenomenon has its origins in
the simultaneous stimuli just described, and the explosive growth of these
secondary markets (whose levels of activity now frequently exceed the un-
derlying markets on which their products are based) continues unabated,
with total trading volume now measured in trillions of dollars. The vari-
ety and complexity of new financial instruments is often bewildering, and
much effort goes into the analysis of the (ever more complex) mathematical
models on which their existence is predicated.
In this book,we present the necessary mathematics, within the con-
text of this field of application, as simply as possible in an attempt to
dispel some of the mystique that has come to surround these models and
at the same time to exhibit the essential structure and robustness of the
underlying theory. Since making choices and decisions under conditions
1

2
CHAPTER 1. PRICING BY ARBITRAGE
of uncertainty about their outcomes is inherent in all market trading, the
area of mathematics that finds the most natural applications in finance
theory is the modern theory of probability and stochastic processes, which
has itself undergone spectacular growth in the past five decades. Given
our current preoccupations, it seems entirely appropriate that the origins
of probability, as well as much of its current motivation, lie in one of the
earliest and most pervasive indicators of ‘civilised’ behaviour: gambling.
Contingent Claims
A contingent claim represents the potential liability inherent in a derivative
security; that is, in an asset whose value is determined by the values of one
or more underlying variables (usually securities themselves). The analysis
of such claims, and their pricing in particular, forms a large part of the
modern theory of finance. Decisions about the prices appropriate for such
claims are made contingent on the price behaviour of these underlying
securities (often simply referred to as the underlying), and the theory of
derivatives markets is primarily concerned with these relationships rather
than with the economic fundamentals that determine the prices of the
underlying.
While the construction of mathematical models for this analysis often
involves very sophisticated mathematical ideas, the economic insights that
underlie the modelling are often remarkably simple and transparent. In
order to highlight these insights we first develop rather simplistic mathe-
matical models based on discrete time (and, frequently, finitely generated
probability spaces) before showing how the analogous concepts can be used
in the more widely known continuous models based on diffusions and Itˆo
processes. For the same reason, we do not attempt to survey the range
of contingent claims now traded in the financial markets but concentrate
on the more basic stock options before attempting to discuss only a small
sample of the multitude of more recent, and often highly complex, finan-
cial instruments that finance houses place on the markets in ever greater
quantities.
Before commencing the mathematical analysis of market models and
the options based upon them, we outline the principal features of the main
types of financial instruments and the conditions under which they are
currently traded in order to have a benchmark for the mathematical ide-
alisations that characterise our modelling. We briefly consider the role of
forwards, futures, swaps, and options.
Forward Contracts
A forward contract is simply an agreement to buy
or sell a specified asset S at a certain future time T for a price K that is
specified now (which we take to be time 0). Such contracts are not normally
traded on exchanges but are agreements reached between two sophisticated
institutions, usually between a financial institution such as a bank and one
of its corporate clients. The purpose is to share risk: one party assumes

1.1. INTRODUCTION: PRICING AND HEDGING
3
a long position by agreeing to buy the asset, and the other takes a short
position by agreeing to sell the asset for the delivery price K at the delivery
date T. Initially neither party incurs any costs in entering into the contract,
and the forward price of the contract at time t ∈[0, T] is the delivery price
that would give the contract zero value. Thus, at time 0, the forward price
is K, but at later times movement in the market value of the underlying
commodity will suggest different values. The payoffto the holder of the
long position at time T is simply ST −K, and for the short position it is
K −ST . Thus, since both parties are obliged to honour the contract, in
general one will lose and the other gain the same amount.
Trading in forwards is not closely regulated, and the market participant
bears the risk that the other party may default-the instruments are not
traded on an exchange but ‘over-the-counter’ (OTC) worldwide, usually by
electronic means. There are no price limits (as could be set by exchanges),
and the object of the transaction is delivery; that is, the contracts are not
usually ‘sold on’ to third parties. Thus the problem of determining a ‘fair’
or rational price, as determined by the collective judgement of the market
makers or by theoretical modelling, appears complicated.
Intuitively, averaging over the possible future values of the asset may
seem to offer a plausible approach. That this fails can be seen in a simple
one-period example where the asset takes only two future values.
Example 1.1.1. Suppose that the current (time 0) value of the stock is
$100 and the value at time 1 is $120 with probability p = 3
4 and $80 with
probability 1 −p = 1
4. Suppose the riskless interest rate is r = 5% over the
time period. A contract price of 3
4 ×$120+ 1
4 ×$80 = $110 produces a 10%
return for the seller, which is greater than the riskless return, while p = 1
2
would suggest a price of $100, yielding a riskless benefit for the buyer.
This suggests that we should look for a pricing mechanism that is inde-
pendent of the probabilities that investors may attach to the different future
values of the asset and indeed is independent of those values themselves.
The simple assumption that investors will always prefer having more to
having less (this is what constitutes ‘rational behaviour’ in the markets)
already allows us to price a forward contract that provides no dividends
or other income. Let St be the spot price of the underlying asset S (i.e.,
its price at time t ∈[0, T]); then the forward price F(t, T) at that time is
simply the value at the time T of a riskless investment of St made at time
t whose value increases at a constant riskless interest rate r > 0. Under
continuous compounding at this rate, an amount of money Ms in the bank
will grow exponentially according to
dMs
Ms
= rds, s ∈[t, T].
To repay the loan St taken out at t, we thus need MT = Ster(T −t) by
time T.

4
CHAPTER 1. PRICING BY ARBITRAGE
We therefore claim that
F(t, T) = Ster(T −t) for t ∈[0, T] .
To see this, consider the alternatives. If the forward price is higher, we
can borrow St for the interval [t, T] at rate r, buy the asset, and take a
short position in the forward contract. At time T, we need Ster(T −t) to
repay our loan but will realise the higher forward price from the forward
contract and thus make a riskless profit.
For F(t, T) < Ster(T −t), we
can similarly make a sure gain by shorting the asset (i.e., ‘borrowing’ it
from someone else’s account, a service that brokers will provide subject
to various market regulations) and taking a long position in the contract.
Thus, simple ‘arbitrage’ considerations (in other words, that we cannot
expect riskless profits, or a ‘free lunch’) lead to a definite forward price at
each time t.
Forward contracts can be used for reducing risk (hedging). For example,
large corporations regularly face the risk of currency fluctuations and may
be willing to pay a price for greater certainty. A company facing the need to
make a large fixed payment in a foreign currency at a fixed future date may
choose to enter into a forward contract with a bank to fix the rate now in
order to lock in the exchange rate. The bank, on the other hand, is acting
as a speculator since it will benefit from an exchange rate fluctuation that
leaves the foreign currency below the value fixed today. Equally, a company
may speculate on the exchange rate going up more than the bank predicts
and take a long position in a forward contract to lock in that potential
advantage-while taking the risk of losses if this prediction fails. In essence,
it is betting on future movements in the asset. The advantage over actual
purchase of the currency now is that the forward contract involves no cost at
time 0 and only potential cost if the gamble does not pay off. In practice,
financial institutions will demand a small proportion of the funds as a
deposit to guard against default risk; nonetheless, the gearing involved in
this form of trading is considerable.
Both types of traders, hedgers and speculators, are thus required for
forward markets to operate. A third group, arbitrageurs, typically enter
two or more markets simultaneously, trying to exploit local or temporary
disequilibria (i.e., mispricing of certain assets) in order to lock in riskless
profits. The fundamental economic assumption that (ideal) markets op-
erate in equilibrium makes this a hazardous undertaking requiring rapid
judgements (and hence well-developed underlying mathematical models)
for sustained success-their existence means that assets do not remain mis-
priced for long or by large amounts. Thus it is reasonable to build models
and calculate derivative prices that are based on the assumption of the
absence of arbitrage, and this is our general approach.
Futures Contracts
Futures contracts involve the same agreement to
trade an asset at a future time at a certain price, but the trading takes

1.1. INTRODUCTION: PRICING AND HEDGING
5
place on an exchange and is subject to regulation. The parties need not
know each other, so the exchange needs to bear any default risk-hence the
contract requires standardised features, such as daily settlement arrange-
ments known as marking to market. The investor is required to pay an
initial deposit, and this initial margin is adjusted daily to reflect gains and
losses since the futures price is determined on the floor of the exchange by
demand and supply considerations. The price is thus paid over the life of
the contract in a series of instalments that enable the exchange to balance
long and short positions and minimise its exposure to default risk. Futures
contracts often involve commodities whose quality cannot be determined
with certainty in advance, such as cotton, sugar, or coffee, and the delivery
price thus has reference points that guarantee that the asset quality falls
between agreed limits, as well as specifying contract size.
The largest commodity futures exchange is the Chicago Board of Trade,
but there are many different exchanges trading in futures around the world;
increasingly, financial futures have become a major feature of many such
markets. Futures contracts are written on stock indices, on currencies, and
especially on movements in interest rates. Treasury bills and Eurodollar
futures are among the most common instruments.
Futures contracts are traded heavily, and only a small proportion are
actually delivered before being sold on to other parties. Prices are known
publicly and so the transactions conducted will be at the best price available
at that time. We consider futures contracts in Chapter 9, but only in the
context of interest rate models.
Swaps
A more recent development, dating from 1981, is the exchange of
future cash flows between two partners according to agreed prior criteria
that depend on the values of certain underlying assets. Swaps can thus
be thought of as portfolios of forward contracts, and the initial value as
well as the final value of the swap is zero. The cash flows to be exchanged
may depend on interest rates. In the simplest example (a plain vanilla
interest rate swap), one party agrees to pay the other cash flows equal to
interest at a fixed rate on a notional principal at each payment date. The
other party agrees to pay interest on the same notional principal and in
the same currency, but the cash flow is based on a floating interest rate.
Thus the swap transforms a floating rate loan into a fixed rate one and
vice versa. The floating rate used is often LIBOR (the London Interbank
Offer Rate), which determines the interest rate used by banks on deposits
from other banks in Eurocurrency markets; it is quoted on deposits of
varying duration-one month, three months, and so on. LIBOR operates as
a reference rate for international markets: three-month LIBOR is the rate
underlying Eurodollar futures contracts, for example.
There is now a vast range of swap contracts available, with currency
swaps (whereby the loan exchange uses fixed interest rate payments on
loans in different currencies) among the most heavily traded. We do not

6
CHAPTER 1. PRICING BY ARBITRAGE
study swaps in this book; see [232] or [305] for detailed discussions. The lat-
ter text focuses on options that have derivative securities, such as forwards,
futures, or swaps, as their underlying assets; in general, such instruments
are known as exotics.
Options
An option on a stock is a contract giving the owner the right,
but not the obligation, to trade a given number of shares of a common
stock for a fixed price at a future date (the expiry date T). A call option
gives the owner the right to buy stocks, and a put option confers the right
to sell, at the fixed strike price K. The option is European if it can only be
exercised at the fixed expiry date T. The option is American if the owner
can exercise his right to trade at any time up to the expiry date. Options
are the principal financial instruments discussed in this book.
In Figures 1.1 and 1.2, we draw the simple graphs that illustrate the
payofffunction of each of these options. In every transaction there are two
parties, the buyer and the seller, more usually termed the writer, of the
option. In the case of a European call option on a stock (St)t∈T with strike
price K at time T, the payoffequals ST −K if ST > K and 0 otherwise.
The payofffor the writer of the option must balance this quantity; that is,
it should equal K −ST if ST < K and 0 otherwise. The option writer must
honour the contract if the buyer decides to exercise his option at time T.
Fair Prices and Hedge Portfolios
The problem of option pricing is to determine what value to assign to the
option at a given time (e.g. at time 0). It is clear that a trader can make
a riskless profit (at least in the absence of inflation) unless she has paid an
‘entry fee’ that allows her the chance of exercising the option favourably at
the expiry date. On the other hand, if this ‘fee’ is too high, and the stock
price seems likely to remain close to the strike price, then no sensible trader
would buy the option for this fee. As we saw previously, operating on a set
T of possible trading dates (which may typically be a finite set of natural
numbers of the form {0, 1, . . . , T}, or, alternatively, a finite interval [0, T]
on the real line), the buyer of a European call option on a stock with price
process (St)t∈T will have the opportunity of receiving a payoffat time T
of C(t) = max {ST −K, 0}, since he will exercise the option if, and only if,
the final price of the stock ST is greater than the previously agreed strike
price K.
With the call option price set at C0, we can draw the graph of the gain
(or loss) in the transaction for both the buyer and writer of the option.
Initially we assume for simplicity that the riskless interest rate is 0 (the
‘value of money’ remains constant); in the next subsection we shall drop
this assumption, and then account must be taken of the rate at which
money held in a savings account would accumulate. For example, with
continuous compounding over the interval T = [0, T], the price C0 paid for
the option at time 0 would be worth C0erT by time T. With the rate r = 0,

1.1. INTRODUCTION: PRICING AND HEDGING
7
C0
C0
ST
ST
Payoff
Payoff
K
buyer
writer
K
Figure 1.1: Payoffand gain for European call option
the buyer’s gain from the call option will be ST −K −C0 if ST > K and
−C0 if ST ≤K. The writer’s gain is given by K −ST + C0 if ST > K
and C0 if ST ≤K. Similar arguments hold for the buyer and writer of a
European put option with strike K and option price P0. The payoffand
gain graphs are given in Figures 1.1 and 1.2.
Determining the option price entails an assessment of a price to which
both parties would logically agree. One way of describing the fair price for
the option is as the current value of a portfolio that will yield exactly the
same return as does the option by time T. Strictly, this price is fair only
for the writer of the option, who can calculate the fair price as the smallest
initial investment that would allow him to replicate the value of the option
throughout the time set T by means of a portfolio consisting of stock and
a riskless bond (or savings account) alone. The buyer, on the other hand,
will want to cover any potential losses by borrowing the amount required
to buy the option (the buyer’s option price) and to invest in the market in
order to reduce this liability, so that at time T the option payoffat least
covers the loan. In general, the buyer’s and seller’s option prices will not
coincide-it is a feature of complete market models, which form the main
topic of interest in this book, that they do coincide, so that it becomes
possible to refer to the fair price of the option. Our first problem is to
determine this price uniquely.
When option replication is possible, the replicating portfolio can be

8
CHAPTER 1. PRICING BY ARBITRAGE
C0
C0
ST
ST
Payoff
Payoff
buyer
writer
K
K
Figure 1.2: Payoffand gain for European put option
used to offset, or hedge, the risk inherent in writing the option; that is, the
risk that the writer of the option may have to sell the share ST for the fixed
price K even though, with small probability, ST may be much larger than
K. Our second problem is therefore to construct such a hedge portfolio.
Call-Put Parity
Our basic market assumption enables us to concentrate our attention on
call options alone. Once we have dealt with these, the solutions of the cor-
responding problems for the European put option can be read offat once
from those for the call option. The crucial assumption that ensures this is
that our market model rules out arbitrage; that is, no investor should be
able to make riskless profits, in a sense that we will shortly make more pre-
cise. This assumption is basic to option pricing theory since there can be
no market equilibrium otherwise. It can be argued that the very existence
of ‘arbitrageurs’ in real markets justifies this assumption: their presence
ensures that markets will quickly adjust prices so as to eliminate disequi-
librium and hence will move to eliminate arbitrage.
So let Ct (resp. Pt) be the value at time t of the European call (resp. put)
option on the stock (St)t∈T. Writing
x+ =

x
if x > 0
0
if x ≤0 ,

1.1. INTRODUCTION: PRICING AND HEDGING
9
we can write the payoffof the European call as (ST −K)+ and that of the
corresponding put option as (K −ST )+.
It is obvious from these definitions that, at the expiry date T, we have
CT −PT = (ST −K)+ −(K −ST )+ = ST −K.
(1.1)
Assume now that a constant interest rate r > 0 applies throughout T =
[0, T]. With continuous compounding, a sum X deposited in the bank (or
money-market account) at time t < T accumulates to Xer(T −t) by time T.
Hence a cash sum of K, needed at time T, can be obtained by depositing
Ke−r(T −t) at time t.
We claim that, in order to avoid arbitrage, the call and put prices on
our stock S must satisfy (1.1) at all times t < T, with the appropriate
discounting of the cash sum K; i.e.,
Ct −Pt = St −e−r(T −t)K for all t ∈T.
(1.2)
To see this, compare the following ‘portfolios’:
(i) Buy a call and sell a put, each with strike K and horizon T. The fair
price we should pay is Ct −Pt.
(ii) Buy one share at price St and borrow e−r(T −t)K from the bank. The
net cost is St −e−r(T −t)K.
The value of these portfolios at time T is the same since the first option
yields CT −PT = ST −K, while the net worth of the second portfolio at
that time is also ST −K. Hence, if these two portfolios did not have the
same value at time t, we could make a riskless profit over the time interval
[t, T] by simultaneously taking a long position in one and a short position
in the other. Equation (1.2) follows.
Exercise 1.1.2. Give an alternative proof of (1.2) by considering the pos-
sible outcomes at time T of the following trades made at time t < T: buy
a call and write a put on S, each with strike K, and sell one share of the
stock. Deposit the net proceeds in the bank account at constant riskless
interest rate r > 0. Show that if (1.2) fails, these transactions will always
provide a riskless profit for one of the trading partners.
More generally, the relation
Ct −Pt = St −βt,T K for all t ∈T
(1.3)
holds, where βt,T represents the discount at the riskless rate over the in-
terval [t, T]. In our examples, with r constant, we have βt,T = βT −t =
e−r(T −t) in the continuous case and βt,T = βT −t = (1 + r)−(T −t) in the
discrete case.

10
CHAPTER 1. PRICING BY ARBITRAGE
1.2
Single-Period Option Pricing Models
Risk-Neutral Probability Assignments
In our first examples, we restrict attention to markets with a single trading
period, so that the time set T contains only the two trading dates 0 and
T. The mathematical tools needed for contingent claim analysis are those
of probability theory: in the absence of complete information about the
time evolution of the risky asset (St)t∈T it is natural to model its value at
some future date T as a random variable defined on some probability space
(Ω, F, P). Similarly, any contingent claim H that can be expressed as a
function of ST or, more generally, a function of (St)t∈T, is a non-negative
random variable on (Ω, F, P).
The probabilistic formulation of option prices allows us to attack the
problem of finding the fair price H0 of the option in a different way: since
we do not know in advance what value ST will take, it seems logical to
estimate H by E (βH) using the discount factor β; that is, we estimate H
by its average discounted value. (Here E (·) = EP (·) denotes expectation
relative to the probability measure P.)
This averaging technique has been known for centuries and is termed the
‘principle of equivalence’ in actuarial theory; there it reflects the principle
that, on average, the (uncertain) discounted future benefits should be equal
in value to the present outlay. We are left, however, with a crucial decision:
how do we determine the probability measure? At first sight it is not clear
that there is a ‘natural’ choice at all; it seems that the probability measure
(i.e., the assignment of probabilities to every possible event) must depend
on investors’ risk preferences.
However, in particular situations, one can obtain a ‘preference-free’ ver-
sion of the option price: the theory that has grown out of the mathematical
modelling initiated by the work of Black and Scholes [27] provides a frame-
work in which there is a natural choice of measure, namely a measure
under which the (discounted) price process is a martingale. Economically,
this corresponds to a market in which the investors’ probability assign-
ments show them to be ‘risk-neutral’ in a sense made more precise later.
Although this framework depends on some rather restrictive conditions, it
provides a firm basis for mathematical modelling as well as being a test bed
for more ‘economically realistic’ market models. To motivate the choice of
the particular models currently employed in practice, we first consider a
simple numerical example.
Example 1.2.1. We illustrate the connection between the ‘fair price’ of a
claim and a replicating (or ‘hedge’) portfolio that mimics the value of the
claim. For simplicity, we again set the discount factor β ≡1; that is, the
riskless interest rate (or ‘inflator’) r is set at 0. The only trading dates are
0 and 1, so that any portfolio fixed at time 0 is held until time 1. Suppose
a stock S has price 10 (dollars, say) at time 0, and takes one of only two

1.2. SINGLE-PERIOD OPTION PRICING MODELS
11
possible values at time 1:
S1 =

20
with probability p
7.5
with probability 1 −p .
Consider a European call option H = (S1 −K)+ with strike price K = 15
written on the stock. At time 1, the option H yields a profit of $5 if S1 = 20
and $0 otherwise. The probability assignment is (p, 1−p), which, in general,
depends on the investor’s attitude toward risk: an inaccurate choice could
mean that the investor pays more for the option than is necessary. We look
for a ‘risk-neutral’ probability assignment (q, 1−q); that is, one under which
the stock price S is constant on average. Thus, if Q denotes the probability
measure given by (q, 1 −q), then the expected value of S under Q should
be constant (i.e., EQ (S1) = S0), which we can also write as EQ (∆S) = 0,
where ∆S = S1 −S0. (This makes S into a ‘one-step martingale’.) In our
example, we obtain
10 = 20q + 7.5(1 −q),
so that q = 0.2. With the probability assignment (0.2, 0.8), we then obtain
the option price π(H) = 5q = 1.
To see why this price is the unique ‘rational’ one, consider the hedge
portfolio approach to pricing: we attempt to replicate the final value of the
option by means of a portfolio (η, θ) of cash and stock alone and determine
what initial capital is needed for this portfolio to have the same time 1
value as H in all contingencies. The portfolio (η, θ) can then be used by
the option writer to insure, or hedge, perfectly against all the risk inherent
in the option.
Recall that the discount rate is 0, so that the bank account remains
constant. The value of our portfolio is
Vt = η + θSt for t = 0, 1.
Here we use $1 as our unit of cash, so that the value of cash held is simply
η, while θ represents the number of shares of stock held during the period.
Changes in the value of the portfolio are due solely to changes in the value
of the stock. Hence the gain from trade is simply given by G = θ∆S, and
V1 = V0 + G. By the choice of the measure Q, we also have
V0 = EQ (V0) = EQ (V1 −G) = EQ (V1)
(1.4)
since EQ (θ∆S) = θEQ (∆S) = 0. To find a hedge (η, θ) replicating the
option, we must solve the following equations at time 1:
5 = η + 20θ,
0 = η + 7.5θ.
These have the solution η = −3 and θ = 0.4. Substituting into V0 = η+θS0
gives V0 = −3 + 0.4(10) = 1.

12
CHAPTER 1. PRICING BY ARBITRAGE
The hedging strategy implied by the preceding situation is as follows.
At time 0, sell the option in order to obtain capital of $1, and borrow $3
in order to invest the sum of $4 in shares. This buys 0.4 shares of stock.
At time 1, there are two possible outcomes:
1. If S1 = 20, then the option is exercised at a cost of $5; we repay the
loan (cost $3) and sell the shares (gain 0.4 × $20 = $8).
Net balance of trade: 0.
2. If S1 = 7.5, then the option is not exercised (cost $0); we repay the
loan (cost $3) and sell the shares, gaining 0.4 × $7.5 = $3.
Net balance of trade: 0.
Thus, selling the option and holding the hedge portfolio exactly balance
out in each case, provided the initial price of the option is set at π(H) = 1.
It is clear that no other initial price has this property: if π(H) > 1 we can
make a riskless profit by selling the option in favour of the portfolio (η, θ)
and gain (π(H) −1), while if π(H) < 1 we simply exchange roles with the
buyer in the same transaction! Moreover, since π(H) = 5q = 1, the natural
(risk-neutral) probability is given by q = 0.2 as before.
Remark 1.2.2. This example shows that the risk-neutral valuation of the
option is the unique one that prevents arbitrage profits, so that the price
π(H) will be fixed by the market in order to maintain market equilibrium.
The preceding simple calculation depends crucially on the assumption that
S1 can take only two values at time 1: even with a three-splitting it is no
longer possible, in general, to find a hedge portfolio (see Exercise 1.4.6).
The underlying idea can, however, be adapted to deal with more general
situations and to identify the intrinsic risk inherent in the particular market
commodities. We illustrate this first by indicating briefly how one might
construct a more general single-period model, where the investor has access
to external funds and/or consumption.
1.3
A General Single-Period Model
We now generalise the hedge portfolio approach to option pricing by ex-
amining the cost function associated with various trading strategies and
minimising its mean-square variation. Suppose that our stock price takes
the (known) value S0 at time 0 and the random value S1 at time 1. (These
are again the only trading dates in the model.) In order to express all
values in terms of time-0 prices, we introduce a discount factor β < 1 and
use the notation X = βX for any random variable X. So write S1 = βS1
for the discounted value of the stock price.
The stock price S and a quite general contingent claim H are both taken
to be random variables on some probability space (Ω, F, P), and we wish
to hedge against the obligation to honour the claim; that is, to pay out

1.3. A GENERAL SINGLE-PERIOD MODEL
13
H(ω) at time 1. (Here we are assuming that an underlying probability P is
known in advance.) To this end, we build a portfolio at time 0 consisting of
θ shares of stock and η0 units of cash. The initial value of this portfolio is
V0 = η0 +θS0. We place the cash in the savings account, where it increases
by a factor β−1 by time 1. We wish this portfolio to have value V1 = H at
time 1; in discounted terms, V 1 = H.
Assuming that we have access to external funds, this can be achieved
very simply by adjusting the savings account from η0 to the value η1 = H −
θS1 since this gives the portfolio value V1 = θS1 +η1 = θS1 +H −θS1 = H.
As H is given, it simply remains to choose the constants θ and V0 to
determine our hedging strategy
(η, θ) completely. The cost of doing this
can be described by the process (C0, C1), where C0 = V0 is the initial
investment required, and ∆C = C1 −C0 = η1 −η0 since the only change
at time 1 was to adjust η0 to η1. Finally, write ∆X = βX1 −X0 for any
‘process’ X = (X0, X1), in order to keep all quantities in discounted terms.
From the preceding definitions, we obtain
∆C = βC1 −C0 = βη1 −η0
= β(V1 −θS1) −(V0 −θS0)
= H −(V0 + θ∆S).
(1.5)
Equation (1.5) exhibits the discounted cost increment ∆C simply as the
difference between the discounted claim H and its approximation by linear
estimates based on the discounted price increment ∆S. A rather natural
choice of the parameters θ and V0 is thus given by linear regression: the
parameter values θ and V0 that minimise the risk function
R = E

(∆C)2
= E

(H −(V0 + θ∆S))2
are given by the regression estimates
θ = cov

H, ∆S

var

∆S

,
V0 = E

H

−θE

∆S

.
In particular, E

∆C

= 0, so that the average discounted cost remains
constant at V0. The minimal risk obtained when using this choice of the
parameters is
Rmin = var

H

−θ2var

∆S

= var

H
 
1 −ρ2
,
where ρ = ρ

H, S1

is the correlation coefficient. Thus, the intrinsic risk
of the claim H cannot be completely eliminated unless |ρ| = 1.
In general pricing models, therefore, we cannot expect all contingent
claims to be attainable by some hedging strategy that eliminates all the
risk-where this is possible, we call the model complete. The essential feature
that distinguishes complete models is a martingale representation property:

14
CHAPTER 1. PRICING BY ARBITRAGE
it turns out that in these cases the (discounted) price process is a basis for
a certain vector space of martingales.
The preceding discussion is of course much simplified by the fact that
we have dealt with a single-period model. In the general case, this rather
sophisticated approach to option pricing (due to [136]; see [134] and [268] for
its further development, which we do not pursue here) can only be carried
through at the expense of using quite powerful mathematical machinery.
In this chapter we consider in more detail only the much simpler situation
where the probabilities arise from a binomial splitting.
1.4
A Single-Period Binomial Model
We look for pricing models in which we can take η1 = η0 = η, that is,
where there is no recourse to external funds. Recall that in the general
single-period model the initial holding is
V0 = η + θS0,
which becomes
V1 = η + θS1 = V0 + θ∆S
at time 1.
Pricing
The simplest complete model has the binomial splitting of ∆S that we
exploited in Example 1.2.1. We assume that the random variable S1 takes
just two values, denoted by Sb = (1+b)S0 and Sa = (1+a)S0, respectively,
where a, b are real numbers. For any contingent claim H, we find θ and
V0 such that, at time 1, the discounted value of βH coincides with the
discounted value βV1 of its replicating portfolio (η, θ), where η = V0 −θS0.
Writing Hb and Ha for the two possible time 1 values of H, we require V0
and θ to satisfy the equations
βHb = V0 + θ(βSb −S0),
βHa = V0 + θ(βSa −S0).
Their unique solution for (V0, θ) is given by
θ = Hb −Ha
Sb −Sa
(1.6)
and
V0 = βHa −Hb −Ha
Sb −Sa
(βSa −S0) = β

Hb
β−1S0 −Sa
Sb −Sa
+ Ha
Sb −β−1S0
Sb −Sa

.
Hence we also have
η = V0 −θS0 = β SbHa −SaHb
Sb −Sa
= β (1 + b)Ha −(1 + a)Hb
b −a
.
(1.7)

1.4. A SINGLE-PERIOD BINOMIAL MODEL
15
Since V1 = H for these choices of θ and V0,
θ = Vb −Va
Sb −Sa
= δV
δS
represents the rate of change in the value of the portfolio (or that of the
contingent claim it replicates) per unit change in the underlying stock price.
We shall meet this parameter again in more general pricing models (where
it is known as the delta of the contingent claim and is usually denoted by
∆).
Setting
q = β−1S0 −Sa
Sb −Sa
,
it follows that
V0 = β(qHb + (1 −q)Ha)
since 1 −q = Sb−β−1S0
Sb−Sa
. In the special case where the discount rate β is
(1+r)−1 for some fixed r > 0, we see that q ∈(0, 1) if and only if r ∈(a, b)
(i.e., the riskless interest rate must lie between the two rates of increase
in the stock price). This condition is therefore necessary and sufficient for
the one-step binomial model to have a risk-neutral probability assignment
Q = (q, 1 −q) under which the fair price of the claim H is given as the
expectation of its discounted final value, namely
π(H) = V0 = EQ(βVT ) = EQ(βH).
(1.8)
These choices of θ and V0 provide a linear estimator with perfect fit for
H. The fair price V0 for H therefore does not need to be adjusted by any risk
premium in this model, and it is uniquely determined, irrespective of any
initial probability assignment (i.e., it does not depend on the investor’s at-
titude toward risk). The binomial model constructed here therefore allows
preference-free or arbitrage pricing of the claim H. Since the cost function
C has constant value V0, we say that the replicating strategy (η, θ) is self-
financing in this special case. No new funds have to be introduced at time
1 (recall that η = V0 −θS0 by definition).
In the general single-period model, it is not possible to ensure that C is
constant. However, the pricing approach based on cost-minimisation leads
to an optimal strategy for which the cost function is constant on average.
Hence we call such a strategy mean-self-financing (see [141]).
The pricing formula (1.8) is valid for any contingent claim in the one-
period binomial model. The following example shows how this simplifies
for a European call option when the riskless interest rate is constant and
the strike price lies between the two future stock price values.
Example 1.4.1. Assume that H = (S1 −K)+, β = (1 + r)−1, and
(1 + a)S0 < K ≤(1 + b)S0.

16
CHAPTER 1. PRICING BY ARBITRAGE
Then we have
Hb = (1 + b)S0 −K,
Ha = 0,
so that
θ = Hb −Ha
Sb −Sa
= S0(1 + b) −K
S0(b −a)
.
The call option price is therefore
H0 = V0 =
1
1 + r
r −a
b −a (S0(1 + b) −K) .
Note that differentiation with respect to b and a, respectively, shows that,
under the above assumptions, the call option price is an increasing function
of b and a decreasing function of a, in accord with our intuition.
Risk and Return
We can measure the ‘variability’ of the stock S by means of the variance of
the random variable S1
S0 , which is the same as the variance of the return on
the stock, RS = S1−S0
S0
. This is a Bernoulli random variable taking values
b and a with probability p and 1 −p, respectively. Hence its mean µS and
variance σ2
S are given by
µS = pSb + (1 −p)Sa
S0
−1 = a + p(b −a)
(1.9)
and
σ2
S = p(1 −p)
Sb −Sa
S0
2
= p(1 −p)(b −a)2,
respectively.
We take the standard deviation σS =

p(1 −p)(b−a) as the measure of
risk inherent in the stock price S. We call it the volatility of the stock. Thus,
with a given initial probability assignment (p, 1−p), the risk is proportional
to (b −a) and hence increases with increasing ‘spread’ of the values a, b,
as expected.
However, contrary to a frequently repeated assertion, the
call option price H0 does not necessarily increase with increasing σS, as
is shown in the following simple example due to Marek Capinski (oral
communication).
Example 1.4.2. Take r = 0 and let the call option begin at the money
(i.e., let K = S0 = 1). Then (1 + b)S0 −K = b, so that the option price
computed via (1.8) reduces to V0 =
−ab
b−a. The choice of b = −a = 0.05
yields V0 = 0.025, while σS = 0.1

p(1 −p). On the other hand, b = 0.01,
a = −0.19 gives V0 = 0.0095, and σS = 0.2

p(1 −p).

1.4. A SINGLE-PERIOD BINOMIAL MODEL
17
Nonetheless, under any fixed initial probability assignment P = (p, 1 −
p), we can usefully compare the risk and return associated with holding
the stock S with those for the option (or any contingent claim H). The
treatment given here is a variant of that given in [69] and provides a fore-
taste of the sensitivity analysis undertaken for continuous-time models in
Chapter 7.
In the single-period binomial model, the calculations reduce to consid-
eration of the mean and standard deviation of Bernoulli random variables
since the mean and variance of the claim H under P are given analogously
by
µH = pHb + (1 −p)Ha
H0
−1,
σ2
H = p(1 −p)
Hb −Ha
H0
2
.
(1.10)
Define the elasticity (also known as the beta of the claim) as the covari-
ance of the returns RS and RH normalised by the variance of RS. Since
both are Bernoulli random variables, it is easy to see that
EH =
p(1 −p) Hb−Ha
H0
Sb−Sa
S0
p(1 −p)

Sb−Sa
S0
2
= Hb −Ha
H0
÷ Sb −Sa
S0
.
(1.11)
Noting that θ = Hb−Ha
Sb−Sa , we obtain EH = S0
H0 θ, and therefore σH = EHσS,
so that the volatility of the claim H is proportional to that of the underlying
stock S, with EH as the constant of proportionality.
What about their rates of return?
We shall consider the case of a
constant riskless rate r > 0 and compare the excess mean returns µH −r
and µS −r. Recall that the replicating portfolio (η, θ) computed for H in
(1.6) and (1.7) satisfies
η(1 + r) + θSb = Hb,
η(1 + r) + θSa = Ha,
while also determining the option price H0 = η + θS0. Thus, with this
portfolio we obtain
θSb −Hb = (1 + r)(θS0 −H0) = θSa −Ha.
Hence, for any p ∈(0, 1), we have
p(θSb −Hb) + (1 −p)(θSa −Ha) = (1 + r)(θS0 −H0);
i.e.,
θ(pSb + (1 −p)Sa) −(pHb + (1 −p)Ha) = (1 + r)(θS0 −H0),
so that
θS0
pSb + (1 −p)S0
S0
−1

−H0
pHb + (1 −p)Ha
H0
−1

= r(θS0 −H0).

18
CHAPTER 1. PRICING BY ARBITRAGE
Using the definitions of µS and µH given by (1.9) and (1.10), we have
θS0µS −H0µH = rθS0 −rH0.
Rearranging terms, and recalling that EH = S0
H0 θ, we have therefore shown
that
µH −r = EH(µS −r).
These relations are valid for any contingent claim H in the single-period
binomial model and any fixed probability assignment P = (p, 1 −p). Now
recall that the risk-neutral probabilities
(q, 1 −q) =
(1 + r)S0 −Sa
Sb −Sa
, Sb −(1 + r)S0
Sb −Sa

(1.12)
provide the price of the claim H as the discounted expectation of its final
values: H0 = (
1
1+r)(qHb + (1 −q)Ha). This leads to the identity
(1 + r) (S0(Hb −Ha) −H0(Sb −Sa)) + (SbHa −SaHb) = 0.
(1.13)
Exercise 1.4.3. Show that (1.13) indeed holds true.
In particular, if H = (S1 −K)+ is a European call, then
SbHa −SaHb ≤0,
(1.14)
irrespective of the relationship between the values of K, Hb, and Ha.
Exercise 1.4.4. Verify that (1.14) holds true in all three cases.
Hence, for a European call option, the elasticity satisfies EH ≥1. This
shows that holding the option is intrinsically riskier than holding the stock
but also leads to a greater mean excess rate of return over the riskless
interest rate.
Note further that for the risk-neutral probability Q = (q, 1 −q), the
mean excess return is zero, as EQ

1
1+rH1

= H0; i.e.,
EQ (RH) = qHb + (1 −q)Ha
H0
−1 = r.
It is easy to verify that, for any given P = (p, 1 −p), we have
EP (RH) −EQ (RH) = (p −q)Hb −Ha
H0
,
so that for any P with positive excess mean return (i.e., EP (RH) ≥r), we
can express the mean return as
EP (RH)−r = EP (RH)−EQ (RH) = |p −q| Hb −Ha
H0
= |p −q|
σH

p(1 −p)
.

1.4. A SINGLE-PERIOD BINOMIAL MODEL
19
This justifies the terminology used to describe Q: the excess mean
return under any probability assignment P is directly proportional to the
standard deviation σH of the return RH calculated under P. However, the
mean return under Q is just the riskless rate r, and this holds irrespective
of the ‘riskiness’ of H calculated under any other measure. The investor
using the probability q to calculate the likelihood that the stock will move
to (1 + b)S0 is therefore risk-neutral.
Thus, by choosing the risk-neutral measure Q, we can justify the long-
standing actuarial practice of averaging the value of the discounted claim,
at least for the case of our single-period binomial model. Moreover, we have
shown that in this model every contingent claim can be priced by arbitrage;
that is, there exists a (unique) self-financing strategy (η, θ) that replicates
the value of H, so that the pricing model is complete. In a complete model,
the optimal choice of strategy completely eliminates the risk in trading H,
and the fair price of H is uniquely determined as the initial value V0 of the
optimal strategy, which can be computed explicitly as the expectation of
H relative to the risk-neutral measure Q.
Before leaving single-period models, we review some of the preceding
concepts in a modification of Example 1.2.1.
Example 1.4.5. Suppose that the stock price S1 defined in Example 1.2.1
can take three values, namely 20, 15, and 7.5. In this case, there are an
infinite number of risk-neutral probability measures for this stock. Since
β = 1 in this example, the risk-neutral probability assignment requires
EQ (S1) = S0. This leads to the equations
20q1 + 15q2 + 7.5q3 = 10,
q1 + q2 + q3 = 1,
with solutions

λ, 1
3(1 −5λ), 1
3(2 + 2λ)

for arbitrary λ. For nondegenerate
probability assignments, we need qi ∈(0, 1) for i = 1, 2, 3; hence we require
λ ∈

0, 1
5

. For each such λ, we obtain a different risk-neutral probability
measure Qλ.
Let X = (X1, X2, X3) be a contingent claim based on the stock S. We
show that there exists a replicating portfolio for X if and only if
3X1 −5X2 + 2X3 = 0.
(1.15)
Indeed, recall that a hedge portfolio (η, θ) for X needs to satisfy V1 =
η + θS1 = X in all outcomes, so that
η + 20θ = X1,
η + 15θ = X2,
η + 7.5θ = X3.
This leads to
θ = X1 −X3
12.5
= X2 −X3
7.5
,
which, in turn, leads to (1.15). Thus, a contingent claim in this model is
attainable if and only if equation (1.15) holds.

20
CHAPTER 1. PRICING BY ARBITRAGE
Finally, we verify that the value of an attainable claim X is the same
under every risk-neutral measure: we have
EQλ (X) = λX1 + 1
3(1 −5λ)X2 + 1
3(2 + 2λ)X3
= 1
3 (λ(3X1 −5X2 + 2X3) + X2 + 2X3) .
This quantity is independent of λ precisely when the attainability crite-
rion (1.15) holds.
If the claim is not attainable, we cannot determine the price uniquely.
Its possible values lie in the interval (infλ EQλ (X) , supλ EQλ (X)), where
λ ∈

0, 1
5

. For example, if X = (S1−K)+ is a European call with strike 12,
then we obtain EQλ (X) = 1
3(λ(24 −15)+ 3) = 1 + 3λ. Hence, the possible
option values lie in the range (1, 1.6). The choice of the ‘optimal’ value
now depends on the optimality criterion employed. One such criterion was
described in Section 1.3, but there are many others. The study of optimal
pricing in incomplete models remains a major topic of current research and
is largely beyond the scope of this book.
Exercise 1.4.6. Extend the market defined in the previous example by
adding a second stock S′ with S′
0 = 5 and S′
1 = 6, 6, or 4, so that the
vector of stock prices (S, S′) reads
(S0, S′
0) = (10, 5),
(S1, S′
1) =
⎧
⎪
⎨
⎪
⎩
(20, 6)
with probability p1
(15, 6)
with probability p2
(7.5, 4)
with probability p3
.
Verify that in this case there is no risk-neutral probability measure for
the market-recall that we would need pi > 0 for i = 1, 2, 3. We say that
this market is not viable. Show that it is possible to construct arbitrage
opportunities in this situation.
Exercise 1.4.7. Suppose the one-period market has riskless rate r > 0 and
that the risky stock S has S0 = 4 while S1 can take the three values 2.5, 5,
and 3. Find all the risk-neutral probabilities Q = (q1, q2, q3) in this model
in terms of r. Show that there is no risk-neutral probability assignment for
this model when r = 0.25. With this riskless rate, find an explicit strategy
for making a profit with no net investment. When r < 0.25, find a sufficient
condition (in terms of r) for a claim X = (X1, X2, X3) to be attainable.
1.5
Multi-period Binomial Models
Consider a binomial pricing model with trading dates 0, 1, 2, . . . , T for some
fixed positive integer T. By this we mean that the price of the stock takes
values S0, S1, S2, . . . , ST , and, for each t ≤T,
St =

(1 + b)St−1
with probability p
(1 + a)St−1
with probability 1 −p .

1.5. MULTI-PERIOD BINOMIAL MODELS
21
S0
S0
S0
S0
S0
S0
S0
S0
S0
(1+b)2
S0
(1+a)(1+b)
(1+r)S0
(1+a)
(1+a)
(1+b)
(1+a)
(1+a)(1+b)
(1+b)(1+a)
2
2
2
(1+b)
(1+r) S
(1+r) S0
0
2
3
q
1-q
3
3
Figure 1.3: Event tree for the CRR model
As before, r > 0 is the riskless interest rate (so that β = (1 + r)−1) and
r ∈(a, b).
The event tree that describes the behaviour of stock prices in this model
is depicted in Figure 1.3. Each arrow points ‘up’ with probability q and
‘down’ with probability 1 −q.
A One-Step Risk-Neutral Measure
Assume that H is a contingent claim to be exercised at time T. Consider
the current value of H at time T −1, that is, one period before expiry. We
can consider this as the initial value of a claim in the single-period model
discussed previously, and so there is a hedging strategy (η, θ) that replicates
the value of H on the time set {T −1, T} and a risk-neutral measure Q;
we can therefore compute the current value of βH as its expectation under
Q.
To be specific, assume that H = (ST −K)+ is a European call option
with strike price K and expiry date T. Writing Hb for the value of H if
ST = (1 + b)ST −1 and Ha similarly, the current value of H is given by

22
CHAPTER 1. PRICING BY ARBITRAGE
EQ

H
1+r

, where the measure Q is given by (q, 1 −q) as defined in (1.12).
Hence
VT −1 =
1
1 + r(qHb + (1 −q)Ha)
(1.16)
with (writing S for ST −1)
q = (1 + r)S −(1 + a)S
(1 + b)S −(1 + a)S = r −a
b −a.
This again illustrates why we called Q the ‘risk-neutral’ measure since
a risk-neutral investor is one who is indifferent between an investment with
a certain rate of return and another whose uncertain rate of return has
the same expected value.
Under Q, the expectation of ST , given that
ST −1 = S, is given by
EQ (ST |ST −1 = S ) = q(1 + b)S + (1 −q)(1 + a)S = (1 + r)S.
Two-Period Trading
Now apply this analysis to the value VT −2 of the call H at time T −2:
the stock, whose value ST −2 is now written as S, can take one of the three
values (1 + b)2S, (1 + a)(1 + b)S, and (1 + a)2S at time T; hence the call
H must have one of three values at that time (see Figure 1.3). We write
these values as Hbb, Hab, and Haa, respectively. From (1.8), and using the
definition of q in (1.12), we can read offthe possible values of VT −1 as
Vb = β(qHbb + (1 −q)Hab),
Va = β(qHab + (1 −q)Haa),
respectively. For each of these cases, we have now found the value of the
option at time T −1 and can therefore select a hedging portfolio as before.
The value of the parameters θ and η is determined at each stage exactly
as in the single-period model. We obtain
VT −2 = β(qVb + (1 −q)Va)
= β {qβ(qHbb + (1 −q)Hab) + (1 −q)β(qHab + (1 −q)Haa)}
= β2 
q2 
(1 + b)2S −K
+ + 2q(1 −q) [(1 + a)(1 + b)S −K]+
+(1 −q)2 
(1 + a)2S −K
+
.
Hence the current value of the claim is completely determined by quantities
that are known to the investor at time T −2.
The CRR Formula
We can continue this backward recursion to calculate the value process
(Vt)t∈T. In particular, with β = (1 + r)−1, the initial investment needed to

1.5. MULTI-PERIOD BINOMIAL MODELS
23
replicate the European call option H is
V0 = βT
T

t=0
T
t

qt(1 −q)T −t 
(1 + b)t(1 + a)T −tS0 −K
+
= S0
T

t=A
T
t

qt(1 −q)T −t (1 + b)t(1 + a)T −t
(1 + r)T
−K(1 + r)−T
T

t=A
T
t

qt(1 −q)T −t,
(1.17)
where A is the smallest integer k for which S0(1 + b)k(1 + a)T −k > K.
Using
q = r −a
b −a,
q′ = q 1 + b
1 + r,
we obtain q′ ∈(0, 1) and 1 −q′ = (1 −q) 1+a
1+r . We can finally write the fair
price for the European call option in (1.17) in this multi-period binomial
pricing model as
V0 = S0Ψ (A; T, q′) −K(1 + r)−T Ψ (A; T, q) ,
(1.18)
where Ψ is the complementary binomial distribution function; that is,
Ψ (m; n, p) =
n

j=m
n
j

pj(1 −p)n−j.
Formula (1.18) is known as the Cox-Ross-Rubinstein (or CRR, see [59])
binomial option pricing formula for the European call. We shall shortly give
an alternative derivation of this formula by computing the expectation of H
under the risk-neutral measure Q directly, utilising the martingale property
of the discounted stock price under this measure.
Recall the event tree in Figure 1.3. At each node there are only two
branches, that is, one more than the number of stocks available. It is this
simple splitting property that ensures that the model is complete since it
allows us to ‘cover’ the two random outcomes at each stage by adjusting
the quantities θ and η.
The Hedge Portfolio
More generally, it is clear that the value Vt of the option at time t ≤T is
given by the formula
Vt = StΨ (At; T −t, q′) −K(1 + r)−T −tΨ (At; T −t, q) ,
(1.19)
where At is the smallest integer k for which St(1 + b)k(1 + a)T −t−k > K.
An analysis similar to that outlined in Section 1.4 provides the components

24
CHAPTER 1. PRICING BY ARBITRAGE
of the trading strategy (η, θ): the portfolio (ηt−1, θt−1) is held over the time
interval [t −1, t] and is required to replicate Vt; i.e.,
θt−1St + ηt−1(1 + r) = Vt.
Thus Vt is determined by St−1 and the price movement in the time interval
[t −1, t], so that it takes two possible values, depending on whether St =
(1 + b)St−1 or St = (1 + a)St−1. Writing V b
t and V a
t , respectively, for the
resulting values, we need to solve the equations
θt−1(1 + b)St−1 + ηt−1(1 + r) = V b
t ,
θt−1(1 + a)St−1 + ηt−1(1 + r) = V a
t .
Again we obtain
θt−1 =
V b
t −V a
t
(b −a)St−1
,
ηt−1 = (1 + b)V a
t −(1 + a)V b
t
(1 + r)(b −a)
.
(1.20)
This leads to the explicit formulas
θt =
T −t

s=At
T −t
s

(q′)s(1 −q′)T −t−s
ηt = −K(1 + r)−(T −t)
T −t

s=At
T −t
s

qs(1 −q)T −t−s
⎫
⎪
⎪
⎪
⎪
⎪
⎬
⎪
⎪
⎪
⎪
⎪
⎭
(1.21)
for θt and ηt.
Exercise 1.5.1. Verify the formulas in (1.21) by writing down binomial
expressions for V b
t and V a
t analogously with (1.16).
1.6
Bounds on Option Prices
We conclude this chapter with a few simple observations concerning bounds
on option prices. We restrict attention to call options, though similar arbi-
trage considerations provide bounds for put options. The bounds described
here are quite crude but are independent of the model used, relying solely
on the assumption of ‘no arbitrage’. In this section, we denote the call
price by C0 and the put price by P0.
It should be obvious that American options are, in general, more valu-
able than their European counterparts since the holder has greater flexi-
bility in exercising them. We can illustrate this by constructing a simple
arbitrage. For example, if the price C0(E) of a European call with strike
K and exercise date T were greater than the price C0(A) of an American
option with the same K and T, then we would make a riskless profit by
writing the European option and buying the American one, while pocket-
ing the difference C0(E) −C0(A). We keep this riskless profit by holding

1.6. BOUNDS ON OPTION PRICES
25
the American option until time T when both options have the same value.
Thus, in the absence of arbitrage, the relations
0 ≤C0(E) ≤C0(A)
(1.22)
will always hold.
Both option prices must lie below the current value S0 of the underlying
share (and will in practice be much less): if C0(A) were greater than S0,
we could buy a share at S0 and write the option. The profit made is secure
since the option liability is covered by the share. By (1.22), both option
values are therefore less than S0.
Call-put parity for European options (see (1.3)) demands that
C0(E) −P0(E) = S0 −βT K.
As P0(E) ≥0, it follows that C0(E) ≥S0 −βT K. We conclude that the
European call option price lies in the interval

min

0, S0 −βT K

, S0

.
While this remains a crude estimate, it holds in all option pricing models.
These bounds provide a simple, but initially surprising, relationship
between European and American call option prices for shares that (as here)
pay no dividends. Note first that
C0(A) ≥C0(E) ≥S0 −βT K ≥S0 −K
(1.23)
since the discount factor β is less than or equal to 1. This means that
the option price is, in either case, at least equal to the gain achieved by
immediate exercise of the option. Hence (as long as our investor prefers
more to less) the option will not be exercised immediately. But the same
argument applies at any starting time t < T, so that the European option’s
value Ct(E) at time t (which must be the same as that of an option written
at t with strike K and exercise date T) satisfies Ct(E) ≥St −βT −tK,
and, as previously, Ct(A) ≥St −K, which is independent of the time
to expiry T −t. Consequently, an American call option on a stock that
pays no dividends will not be exercised before expiry, so that in this case
C0(E) = C0(A).
Exercise 1.6.1. Derive the following bounds for the European put option
price P0(E) by arbitrage arguments:
max

0, βT K −S0

≤P0(E) ≤βT K.
Call-put parity allows a calculation of the riskless interest rate from
European put and call prices since we can write
e−r(T −t)K = St −Ct(E) + Pt(E) for t < T,
so that
r =
1
T −t [log K −log(St + Pt(E) −Ct(E))] .
(1.24)

26
CHAPTER 1. PRICING BY ARBITRAGE
However, as European options are much less frequently traded than
their American counterparts, it is more useful to have an estimate of r
in terms of the latter. This follows at once: as we have just seen for the
case t = 0, we must have Ct(A) = Ct(E) for all t < T, while Pt(A) ≥
Pt(E) by the same argument as was established in (1.22) for calls. Hence,
for American options during whose lifetime the underlying stock pays no
dividends, we have
r ≥
1
T −t [log K −log(St + Pt(A) −Ct(A))] .
(1.25)
In practice, this inequality is used to check put and call prices against the
prevailing riskless rate (e.g. , LIBOR rate); where it fails, market prices offer
(usually short-lived) arbitrage opportunities. It can also serve to provide
estimates of r for use in the simulation of the evolution of the stock price
from options on the stock (see, e.g. , [210].


## Martingale Measures

Chapter 2
Martingale Measures
2.1
A General Discrete-Time Market Model
Information Structure
Fix a time set T = {0, 1, . . . , T}, where the trading horizon T is treated as
the terminal date of the economic activity being modelled, and the points of
T are the admissible trading dates. We assume as given a fixed probability
space (Ω, F, P) to model all ‘possible states of the market’.
In most of the simple models discussed in Chapter 1, Ωis a finite prob-
ability space (i.e., has a finite number of points ω each with P({ω}) > 0).
In this situation, the σ-field F is the power set of Ω, so that every subset
of Ωis F-measurable.
Note, however, that the finite models can equally well be treated by
assuming that, on a general sample space Ω, the σ-field F in question is
finitely generated. In other words, there is a finite partition P of Ωinto
mutually disjoint sets A1, A2, . . . , An whose union is Ωand that generates
F so that F also contains only finitely many events and consists precisely
of those events that can be expressed in terms of P. In this case, we further
demand that the probability measure P on F satisfies P(Ai) > 0 for all i.
In both cases, the only role of P is to identify the events that investors
agree are possible; they may disagree in their assignment of probabilities
to these events. We refer to models in which either of the preceding addi-
tional assumptions applies as finite market models. Although most of our
examples are of this type, the following definitions apply to general market
models. Real-life markets are, of course, always finite; thus the additional
‘generality’ gained by considering arbitrary sample spaces and σ-fields is a
question of mathematical convenience rather than wider applicability!
The information structure available to the investors is given by an in-
creasing (finite) sequence of sub-σ-fields of F: we assume that F0 is trivial;
that is, it contains only sets of P-measure 0 or 1. We assume that (Ω, F0)
is complete (so that any subset of a null set is itself null and F0 contains all
27

28
CHAPTER 2. MARTINGALE MEASURES
P-null sets) and that F0 ⊂F1 ⊂F2 ⊂· · · ⊂FT = F. An increasing family
of σ-fields is called a filtration F = (Ft)t∈T on (Ω, F, P). We can think of Ft
as containing the information available to our investors at time t: investors
learn without forgetting, but we assume that they are not prescient-insider
trading is not possible.
Moreover, our investors think of themselves as
‘small investors’ in that their actions will not change the probabilities they
assign to events in the market. Again, note that in a finite market model
each σ-field Ft is generated by a minimal finite partition Pt of Ωand that
P0 = {Ω} ⊂P1 ⊂P2 ⊂· · · ⊂PT = P. At time t, all our investors know
which cell of Pt contains the ‘true state of the market’, but none of them
knows more.
Market Model and Num´eraire
The definitions developed in this chapter will apply to general discrete
market models, where the sample space need not be finite. Fix a prob-
ability space (Ω, F, P), a natural number d, the dimension of the mar-
ket model, and assume as given a (d + 1)-dimensional stochastic process
S =

Si
t : t ∈T, i = 0, 1, . . . , d

to represent the time evolution of the se-
curities price process. The security labelled 0 is taken as a riskless (non-
random) bond (or bank account) with price process S0, while the d risky
(random) stocks labelled 1, 2, . . . , d have price processes S1, S2, . . . , Sd. The
process S is assumed to be adapted to the filtration F, so that for each
i ≤d, Si
t is Ft-measurable; that is, the prices of the securities at all times
up to t are known at time t. Most frequently, we in fact take the filtra-
tion F as that generated by the price process S =

S1, S2, . . . , Sd
. Then
Ft = σ (Su : u ≤t) is the smallest σ-field such that all the Rd+1-valued
random variables

Su =

S0
u, S1
u, . . . , Sd
u

, u ≤t

are Ft-measurable.
In
other words, at time t, the investors know the values of the price vectors
(Su : u ≤t), but they have no information about later values of S.
The tuple (Ω, F, P, T, F, S) is the securities market model. We require
at least one of the price processes to be strictly positive throughout; that
is, to act as a benchmark, known as the num´eraire, in the model. As is
customary, we generally assign this role to the bond price S0, although in
principle any strictly positive Si could be used for this purpose.
Note on Terminology: The term ‘bond’ is the one traditionally used
to describe the riskless security that we use here as num´eraire, although
‘bank account’ and ‘money market account’ are popular alternatives. We
continue to use ‘bond’ in this sense until Chapter 9, where we discuss
models for the evolution of interest rates; in that context, the term ‘bond’
refers to a certain type of risky asset, as is made clear.

2.2. TRADING STRATEGIES
29
2.2
Trading Strategies
Value Processes
Throughout this section, we fix a securities market model (Ω, F, P, T, F, S).
We take S0 as a strictly positive bond or riskless security, and without loss
of generality we assume that S0(0) = 1, so that the initial value of the bond
S0 yields the units relative to which all other quantities are expressed. The
discount factor βt =
1
S0
t is then the sum of money we need to invest in
bonds at time 0 in order to have 1 unit at time t. Note that we allow the
discount rate - that is, the increments in βt - to vary with t; this includes
the case of a constant interest rate r > 0, where βt = (1 + r)−t.
The securities S0, S1, S2, . . . , Sd are traded at times t ∈T: an investor’s
portfolio at time t ≥1 is given by the Rd+1-valued random variable θt =
(θi
t)0≤i≤d with value process Vt(θ) given by
V0(θ) = θ1 · S0,
Vt(θ) = θt · St =
d

i=0
θi
tSi
t for t ∈T, t ≥1.
The value V0(θ) is the investor’s initial endowment. The investors select
their time t portfolio once the stock prices at time t −1 are known, and
they hold this portfolio during the time interval (t −1, t]. At time t the
investors can adjust their portfolios, taking into account their knowledge
of the prices Si
t for i = 0, 1, . . . , d. They then hold the new portfolio θt+1
throughout the time interval (t, t + 1].
Market Assumptions
We require that the trading strategy θ = {θt : t = 1, 2, . . . , T} consisting of
these portfolios be a predictable vector-valued stochastic process: for each
t < T, θt+1 should be Ft-measurable, so θ1 is F0-measurable and hence
constant, as F0 is assumed to be trivial. We also assume throughout that
we are dealing with a ‘frictionless’ market; that is, there are no transaction
costs, unlimited short sales and borrowing are allowed (the random vari-
ables θi
t can take any real values), and the securities are perfectly divisible
(the Si
t can take any positive real values).
Self-Financing Strategies
We call the trading strategy θ self-financing if any changes in the value
Vt(θ) result entirely from net gains (or losses) realised on the investments;
the value of the portfolio after trading has occurred at time t and before
stock prices at time t + 1 are known is given by θt+1 · St.
If the total
value of the portfolio has been used for these adjustments (i.e., there are
no withdrawals and no new funds are invested), then this means that
θt+1 · St = θt · St for all t = 1, 2, . . . , T −1.
(2.1)

30
CHAPTER 2. MARTINGALE MEASURES
Writing ∆Xt = Xt −Xt−1 for any function X on T, we can rewrite (2.1)
at once as
∆Vt(θ) = θt · St −θt−1 · St−1 = θt · St −θt · St−1 = θt · ∆St;
(2.2)
that is, the gain in value of the portfolio in the time interval (t −1, t] is
the scalar product in Rd of the new portfolio vector θt with the vector ∆St
of price increments. Thus, defining the gains process associated with θ by
setting
G0(θ) = 0,
Gt(θ) = θ1 · ∆S1 + θ2 · ∆S2 + · · · + θt · ∆St,
we see at once that θ is self-financing if and only if
Vt(θ) = V0(θ) + Gt(θ) for all t ∈T.
(2.3)
This means that θ is self-financing if and only if the value Vt(θ) arises
solely as the sum of the initial endowment V0(θ) and the gains process
Gt(θ) associated with the strategy θ.
We can write this relationship in yet another useful form: since Vt(θ) =
θt · St for any t ∈T and any strategy θ, it follows that we can write
∆Vt = Vt −Vt−1
= θt · St −θt−1 · St−1
= θt · (St −St−1) + (θt −θt−1) · St−1
= θt · ∆St + (∆θt) · St−1.
(2.4)
Thus, the strategy θ is self-financing if and only if
(∆θt) · St−1 = 0.
(2.5)
This means that, for a self-financing strategy, the vector of changes in
the portfolio θ is orthogonal in Rd+1 to the prior price vector St−1. This
property is sometimes easier to verify than (2.1). It also serves to justify the
terminology: the cumulative effect of the time t variations in the investor’s
holdings (which are made before the time t prices are known) should be to
balance each other. For example, if d = 1, we need to balance ∆θ0
t S0
t−1
against ∆θ1
t S1
t−1 since by (2.5) their sum must be zero.
Num´eraire Invariance
Trivially, (2.1) and (2.3) each have an equivalent ‘discounted’ form. In fact,
given any num´eraire (i.e., any process (Zt) with Zt > 0 for all t ∈T), it
follows that a trading strategy θ is self-financing relative to S if and only
if it is self-financing relative to ZS since
(∆θt) · St−1 = 0 if and only if (∆θt) · Zt−1St−1 = 0 for t ∈T \ {0} .

2.2. TRADING STRATEGIES
31
Thus, changing the choice of ‘benchmark’ security will not alter the
class of trading strategies under consideration and thus will not affect mar-
ket behaviour. This simple fact is sometimes called the ‘num´eraire invari-
ance theorem’; in continuous-time models it is not completely obvious (see
Chapter 9 and [102]). We will also examine the num´eraire invariance of
other market entities. While the use of different discounting conventions
has only limited mathematical significance, economically it amounts to un-
derstanding the way in which these entities are affected by a change of
currency.
Writing Xt = βtXt for the discounted form of the vector Xt in Rd+1,
it follows (using Z = β in the preceding equation) that θ is self-financing
if and only if (∆θt) · St−1 = 0, that is, if and only if
θt+1 · St = θt · St for all t = 1, 2, . . . , T −1,
(2.6)
or, equivalently, if and only if
V t(θ) = V0(θ) + Gt(θ) for all t ∈T.
(2.7)
To see the last equivalence, note first that (2.4) holds for any θ with S
instead of S, so that for self-financing θ we have ∆V t = θt·∆St; hence (2.7)
holds. Conversely, (2.7) implies that ∆V t = θt·∆St, so that (∆θt)·St−1 = 0
and so θ is self-financing.
We observe that the definition of G(θ) does not involve the amount θ0
t
held in bonds (i.e., in the security S0) at time t. Hence, if θ is self-financing,
the initial investment V0(θ) and the predictable real-valued processes θi
(i = 1, 2, . . . , d) completely determine θ0, just as we have seen in the one-
period model in Section 1.4.
Lemma 2.2.1. Given an F0-measurable function V0 and predictable real-
valued processes θ1, θ2, . . . , θd, the unique predictable process θ0 that turns
θ =

θ0, θ1, θ2, · · · , θd
into a self-financing strategy with initial value V0(θ) = V0 is given by
θ0
t = V0 +
t−1

u=1

θ1
u∆S
1
u + · · · + θd
u∆S
d
u

−

θ1
t S
1
t−1 + · · · + θd
t S
d
t−1

. (2.8)
Proof.
The process θ0 so defined is clearly predictable. To see that it pro-
duces a self-financing strategy, recall by (2.7) that we only need to observe
that this value of θ0 is the unique predictable solution of the equation
V t(θ) = θ0
t + θ1
t S
1
t + θ2
t S
2
t + · · · + θd
t S
d
t
= V0 +
t

u=1

θ1
u∆S
1
u + θ2
uS
2
u + · · · + θd
u∆S
d
u

.

32
CHAPTER 2. MARTINGALE MEASURES
Admissible Strategies
Let Θ be the class of all self-financing strategies.
So far, we have not
insisted that a self-financing strategy must at all times yield non-negative
total wealth; that is, that Vt(θ) ≥0 for all t ∈T. From now on, when
we impose this additional restriction, we call such self-financing strategies
admissible; they define the class Θa.
Economically, this requirement has the effect of restricting certain types
of short sales: although we can still borrow certain of our assets (i.e., have
θi
t < 0 for some values of i and t), the overall value process must remain
non-negative for each t. But the additional restriction has little impact on
the mathematical modelling, as we show shortly.
We use the class Θa to define our concept of ‘free lunch’.
Definition 2.2.2. An arbitrage opportunity is an admissible strategy θ
such that
V0(θ) = 0,
Vt(θ) ≥0 for all t ∈T,
E (VT (θ)) > 0.
In other words, we require θ ∈Θa with initial value 0 but final value
strictly positive with positive probability. Note, however, that the proba-
bility measure P enters into this definition only through its null sets: the
condition E (VT (θ)) > 0 is equivalent to P(VT (θ)) > 0) > 0, justifying the
following definition.
Definition 2.2.3. The market model is viable if it does not contain any
arbitrage opportunities; that is, if θ ∈Θa has V0(θ) = 0, then VT (θ) =
0 a.s..
‘Weak Arbitrage Implies Arbitrage’
To justify the assertion that restricting attention to admissible claims has
little effect on the modelling, we call a self-financing strategy θ ∈Θ a weak
arbitrage if
V0(θ) = 0,
VT (θ) ≥0,
E (VT (θ)) > 0.
The following calculation shows that if a weak arbitrage exists then it can
be adjusted to yield an admissible strategy - that is, an arbitrage as defined
in Definition 2.2.2.
Note. If the price process is a martingale under some equivalent measure-as
will be seen shortly-then any hedging strategy with zero initial value and
positive final expectation will automatically yield a positive expectation at
all intermediate times by the martingale property.
Suppose that θ is a weak arbitrage and that Vt(θ) is not non-negative a.s.
for all t. Then there exists t < T, and A ∈Ft with P(A) > 0 such that
(θt · St)(ω) < 0 for ω ∈A, θu · Su ≥0 a.s. for u > t.

2.2. TRADING STRATEGIES
33
We amend θ to a new strategy φ by setting φu(ω) = 0 for all u ∈T and
ω ∈Ω\ A, while on A we set φu(ω) = 0 if u ≤t, and for u > t we define
φ0
u(ω) = θ0
u(ω) −θt · St
S0
t (ω), φi
u(ω) = θi
u(ω) for i = 1, 2, . . . , d.
This strategy is obviously predictable. It is also self-financing: on Ω\A we
clearly have Vu(φ) ≡0 for all u ∈T, while on A we need only check that
(∆φt+1) · St = 0 by the preceding construction (in which ∆θu and ∆φu
differ only when u = t + 1) and (2.5). We observe that φi
t = 0 on Ac for
i ≥0 and that, on A,
∆φ0
t+1 = φ0
t+1 = θ0
t+1 −θt · St
S0
t
, ∆φi
t+1 = θi
t+1 for i = 1, 2, . . . , d.
Hence
(∆φt+1) · St = 1A(θt+1 · St −θt · St) = 1A(θt · St −θt · St) = 0
since θ is self-financing.
We show that Vu(φ) ≥0 for all u ∈T, and P(VT (φ) > 0) > 0. First
note that Vu(φ) = 0 on Ω\ A for all u ∈T. On A we also have Vu(φ) = 0
when u ≤t, but for u > t we obtain
Vu(φ) = φu · Su = θ0
uS0
u −(θt · St)S0
u
S0
t
+
d

i=1
θi
uSi
u = θu · Su −(θt · St)
S0
u
S0
t

.
Since, by our choice of t, θu · Su ≥0 for u > t, and (θt · St) < 0 while
S0 ≥0, it follows that Vu(φ) ≥0 for all u ∈T. Moreover, since S0
t > 0, we
also see that VT (φ) > 0 on A.
This construction shows that the existence of what we have called weak
arbitrage immediately implies the existence of an arbitrage opportunity.
This fact is useful in the fine structure analysis for finite market models we
give in the next chapter.
Remark 2.2.4. Strictly speaking, we should deal separately with the possi-
bility that the investor’s initial capital is negative. This is of course ruled
out if we demand that all trading strategies are admissible. We can relax
this condition and consider a one-period model, where a trading strategy
is just a portfolio θ, chosen at the outset with knowledge of time 0 prices
and held throughout the period. In that case, an arbitrage is a portfolio
that leads from a non-positive initial outlay to a non-negative value at time
1. Thus here we have two possible types of arbitrage since the portfolio θ
leads to one of two conclusions:
a) V0(θ) < 0 and V1(θ) ≥0 or
b) V0(θ) = 0 and V1(θ) ≥0 and P(V1(θ) > 0) > 0.

34
CHAPTER 2. MARTINGALE MEASURES
In this setting, the assumption that there are no arbitrage opportunities
leads to two conditions on the prices:
(i) V1(θ) = 0 implies V0(θ) = 0 or
(ii) V1(θ) ≥0 and P(V1(θ)) > 0 implies V0(θ) ≥0.
The reader will easily construct arbitrages if either of these conditions fails.
In our treatment of multi-period models, we consistently use admissible
strategies, so that Definition 2.2.3 is sufficient to define the viability of
pricing models.
Uniqueness of the Arbitrage Price
Fix H as a contingent claim with maturity T so H is a non-negative FT -
measurable random variable on (Ω, FT , P). The claim is said to be attain-
able if there is an admissible strategy θ that generates (or replicates) it,
that is, such that
VT (θ) = H.
We should expect the value process associated with a generating strategy
to be given uniquely: the existence of two admissible strategies θ and θ′
with Vt(θ) ̸= Vt(θ′) would violate the Law of One Price, and the market
would therefore allow riskless profits and not be viable. A full discussion
of these economic arguments is given in [241].
The next lemma shows, conversely, that in a viable market the arbitrage
price of a contingent claim is indeed unique.
Lemma 2.2.5. Suppose H is an attainable contingent claim in a viable
market model. Then the value processes of all generating strategies for H
are the same.
Proof. If θ and φ are admissible strategies with
VT (θ) = H = VT (φ)
but V (θ) ̸= V (φ), then there exists t < T such that
Vu(θ) = Vu(φ) for all u < t,
Vt(θ) ̸= Vt(φ).
The set A = {Vt(θ) > Vt(φ)} is in Ft and we can assume P(A) > 0 without
loss of generality. The random variable X = Vt(θ)−Vt(φ) is Ft-measurable
and defines a self-financing strategy ψ as by letting
ψu(ω) = θu(ω) −φu(ω) for u ≤t on A, for u ∈T, on Ac,
ψ0
u = βtX and ψi
u = 0 for i = 1, 2, . . . , d for u > t, on A.
It is clear that ψ is predictable. Since both θ and φ are self-financing,
it follows that (2.1) also holds with ψ for u < t, while if u > t, ψu+1 · Su =

2.3. MARTINGALES AND RISK-NEUTRAL PRICING
35
ψu · Su on Ac similarly. On A, we have ψu+1 = ψu. Thus we only need to
compare ψt · St = Vt(θ) −Vt(φ) and ψt+1 · St = 1Ac(θt+1 −φt+1) · St +
1AβtXS0
t . Now note that S0
t = β−1
t
and that X = Vt(θ) −Vt(φ), while
on Ac the first term becomes (θt −φt) · St = Vt(θ) −Vt(φ) and the latter
vanishes. Thus ψt+1 · St = Vt(θ) −Vt(φ) = ψt · St.
Since V0(θ) = V0(φ), ψ is self-financing with initial value 0.
But
VT (ψ) = 1A(βtXS0
t ) = 1Aβtβ−1
T X is non-negative a.s. and is strictly posi-
tive on A, which has positive probability. Hence ψ is a weak arbitrage, and
by the previous section the market cannot be viable.
We have shown that in a viable market it is possible to associate a
unique time t value (or arbitrage price) to any attainable contingent claim
H. However, it is not yet clear how the generating strategy, and hence
the price, are to be found in particular examples.
In the next section,
we characterise viable market models without having to construct explicit
strategies and derive a general formula for the arbitrage price instead.
2.3
Martingales and Risk-Neutral Pricing
Martingales and Their Transforms
We wish to characterise viable market models in terms of the behaviour
of the increments of the discounted price process S. To set the scene, we
first need to recall some simple properties of martingales. Only the most
basic results needed for our purposes are described here; for more details
consult, for example, [109], [199], [236], [299].
For these results, we take a general probability space (Ω, F, P)together
with any filtration F = (Ft)t∈T, where, as before, T = {0, 1, . . . , T}. Con-
sider stochastic processes defined on this filtered probability space (also
called stochastic basis) (Ω, F, P, F, T). Recall that a stochastic process X =
(Xt) is adapted to F if Xt is Ft-measurable for each t ∈T.
Definition 2.3.1. An F-adapted process M = (Mt)t∈T is an (F, P)-
martingale if E (|Mt|) < ∞for all t ∈T and
E (Mt+1 |Ft ) = Mt for all t ∈T \ {T} .
(2.9)
If the equality in (2.9) is replaced by ≤(≥), we say that M is a super-
martingale (submartingale).
Note that M is a martingale if and only if
E (∆Mt+1 |Ft ) = 0 for all t ∈T \ {T} .
Thus, in particular, E (∆Mt+1) = 0. Hence
E (Mt+1) = E (Mt) for all t ∈T \ {T} ,

36
CHAPTER 2. MARTINGALE MEASURES
so that a martingale is ‘constant on average’. Similarly, a submartingale
increases, and a supermartingale decreases, on average. Thinking of Mt
as representing the current capital of a gambler, a martingale therefore
models a ‘fair’ game, while sub- and supermartingales model ‘favourable’
and ‘unfavourable’ games, respectively (as seen from the perspective of the
gambler, of course!).
The linearity of the conditional expectation operator shows trivially
that any linear combination of martingales is a martingale, and the tower
property shows that M is a martingale if and only if
E (Ms+t |Fs ) = Ms for t = 1, 2, . . . , T −s.
Moreover, (Mt) is a martingale if and only if (Mt −M0) is a martingale,
so we can assume M0 = 0 without loss whenever convenient.
Many familiar stochastic processes are martingales. The simplest exam-
ple is given by the successive conditional expectations of a single integrable
random variable X. Set Mt = E (X |Ft ) for t ∈T. By the tower property,
E (Mt+1 |Ft ) = E (E (X |Ft+1 ) |Ft ) = E (X |Ft ) = Mt.
The values of the martingale Mt are successive best mean-square estimates
of X, as our ‘knowledge’ of X, represented by the σ-fields Ft, increases
with t.
More generally, if we model the price process of a stock by a martingale
M, the conditional expectation (i.e., our best mean-square estimate at time
s of the future value Mt of the stock) is given by its current value Ms. This
generalises a well-known fact about processes with independent increments:
if the zero-mean process W is adapted to the filtration F and (Wt+1−Wt) is
independent of Ft, then E (Wt+1 −Wt |Ft ) = E (Wt+1 −Wt) = 0. Hence
W is a martingale.
Exercise 2.3.2. Suppose that the centred (i.e., zero-mean) integrable ran-
dom variables (Yt)t∈T are independent, and let Xt = 
u≤t Yu for each
t ∈T. Show that X is a martingale for the filtration it generates. What
can we say when the Yt have positive means?
Exercise 2.3.3. Let (Zn)n≥1 be independent identically distributed random
variables, adapted to a given filtration (Fn)n≥0. Suppose further that each
Zn is non-negative and has mean 1. Show that X(0) = 1 and that Xn =
Z1Z2 · · · Zn (n ≥1) defines a martingale for (Fn), provided all the products
are integrable random variables, which holds, for example, if all Zn ∈
L∞(Ω, F, P).
Note also that any predictable martingale is almost surely constant: if
Mt+1 is Ft-measurable, we have E (Mt+1 |Ft ) = Mt+1 and hence Mt and
Mt+1 are a.s. equal for all t ∈T. This is no surprise: if at time t we know
the value of Mt+1, then our best estimate of that value will be perfect.
The construction of the gains process associated with a trading strategy
now suggests the following further definition.

2.3. MARTINGALES AND RISK-NEUTRAL PRICING
37
Definition 2.3.4. Let M = (Mt) be a martingale and φ = (φt)t∈T a
predictable process defined on (Ω, F, P, F, T). The process X = φ·M given
for t ≥1 by
Xt = φ1∆M1 + φ2∆M2 + · · · + φt∆Mt
(2.10)
and
X0 = 0
is the martingale transform of M by φ.
Martingale transforms are the discrete analogues of the stochastic in-
tegrals in which the martingale M is used as the ‘integrator’.
The Itˆo
calculus based upon this integration theory forms the mathematical back-
drop to martingale pricing in continuous time, which comprises the bulk
of this book. An understanding of the technically much simpler martin-
gale transforms provides valuable insight into the essentials of stochastic
calculus and its many applications in finance theory.
The Stability Property
If φ = (φt)t∈T is bounded and predictable, then φt+1 is Ft-measurable and
φt+1∆Mt+1 remains integrable. Hence, for each t ∈T \ {T}, we have
E (∆Xt+1 |Ft ) = E (φt+1∆Mt+1 |Ft ) = φt+1E (∆Mt+1 |Ft ) = 0.
Therefore X = φ·M is a martingale with X0 = 0. Similarly, if φ is also non-
negative and Y is a supermartingale, then φ·Y is again a supermartingale.
This stability under transforms provides a simple, yet extremely useful,
characterisation of martingales.
Theorem 2.3.5. An adapted real-valued process M is a martingale if and
only if
E ((φ · M)t) = E

t

u=1
φu∆Mu

= 0 for t ∈T \ {0}
(2.11)
for each bounded predictable process φ.
Proof. If M is a martingale, then so is the transform X = φ · M, and
X0 = 0. Hence E ((φ · M)t) = 0 for all t ≥1 in T.
Conversely, if (2.11) holds for M and every predictable φ, take s > 0, let
A ∈Fs be given, and define a predictable process φ by setting φs+1 = 1A,
and φt = 0 for all other t ∈T. Then, for t > s, we have
0 = E ((φ · M)t) = E(1A(Ms+1 −Ms)).
Since this holds for all A ∈Fs, it follows that E (∆Ms+1 |Fs ) = 0, so M is
a martingale.

38
CHAPTER 2. MARTINGALE MEASURES
2.4
Arbitrage Pricing: Martingale Measures
Equivalent Martingale Measures
We now return to our study of viable securities market models. Recall that
we assume as given an arbitrary complete measurable space (Ω, F) on which
we consider various probability measures.
We also consider a filtration
F = (Ft)t∈T such that (Ω, F0) is complete, and FT = F. Finally, we are
given a (d + 1)-dimensional stochastic process S = {Si
t : t ∈T, 0 ≤i ≤d}
with S0
0 = 1 and S0 interpreted as a riskless bond providing a discount
factor βt =
1
S0
t and with Si (i = 1, 2, . . . , d) interpreted as risky stocks.
Recall that we are working in a general securities market model: we do not
assume that the resulting market model is finite or that the filtration F is
generated by S.
Suppose that the discounted vector price process ¯S happens to be a
martingale under some probability measure Q; that is,
EQ

∆¯Si
t |Ft−1

= 0 for t ∈T \ {0} and i = 1, 2, . . . , d.
Note that, in particular, this assumes that the discounted prices are inte-
grable with respect to Q. Suppose that θ =

θi
t : i ≤d, t = 1, 2, . . . , T

∈
Θa is an admissible strategy whose discounted value process is also Q-
integrable for each t. Recall from (2.7) that the discounted value process
of θ has the form
¯Vt(θ) = V0(θ) + Gt(θ)
= θ1 · S0 +
t

u=1
θu · ∆¯Su
=
d

i=1

θi
1Si
0 +
t

u=1
θu∆S
i
u

.
Thus the discounted value process V (θ) is a constant plus a finite sum of
martingale transforms; and therefore it is a martingale with initial (con-
stant) value V0(θ). Hence we have E

V t(θ)

= E (V0(θ)) = V0(θ).
We want to show that this precludes the existence of arbitrage oppor-
tunities. If we know in advance that the value process of every admissible
strategy is integrable with respect to Q, this is easy: if V0(θ) = 0 and
VT (θ) ≥0 a.s. (Q), but EQ

V t(θ)

= 0, it follows that VT (θ) = 0 a.s. (Q).
This remains true a.s. (P), provided that the probability measure Q has
the same null sets as P (we say that Q and P are equivalent measures
and write Q ∼P). If such a measure can be found, then no self-financing
strategy θ can lead to arbitrage; that is, the market is viable. This leads
to an important definition.
Definition 2.4.1. A probability measure Q ∼P is an equivalent martin-
gale measure (EMM) for S if the discounted price process S is a (vector)

2.4. ARBITRAGE PRICING: MARTINGALE MEASURES
39
martingale under Q for the filtration F. That is, for each i ≤d the dis-
counted price process S
i is an (F, Q)-martingale (recall that S
0 ≡1).
To complete the argument, we need to justify the assumption that the
value processes we have considered are Q-integrable. This follows from the
following remarkable proposition (see also [132]).
Proposition 2.4.2. Given a viable model (Ω, F, P, T, F, S), suppose that
Q is an equivalent martingale measure for S. Let H be an attainable claim.
Then βT H is Q-integrable and the discounted value process for any gener-
ating strategy θ satisfies
V t(θ) = EQ (βT H |Ft ) a.s. (P) for all t ∈F.
(2.12)
Thus V (θ) is a non-negative Q-martingale.
Proof. Choose a generating strategy θ for H and let V = V (θ) be its
discounted value process.
We show by backward induction that V t ≥
0 a.s. (P)for each t. This is clearly true for t = T since V T = βT H ≥0 by
definition. Hence suppose that V t ≥0. If θt is unbounded, replace it by
the bounded random vectors θn
t = θt1An, where An = {|θt| ≤n} , so that
V t−1 (θn) = V t−1(θ)1An is Ft−1-measurable and Q-integrable. Then we
can write
V t−1 (θn) = V t (θn) −
d

i=1
θn,i
t ∆S
i
t ≥−
d

i=1
θn,i
t ∆S
i
t,
so that
V t−1(θ)1An = V t−1 (θn)
= EQ

V t−1 (θn) |Ft−1

≥−
d

i=1
θn,i
t EQ

∆S
i
t |Ft−1

= 0.
Letting n increase to ∞, we see that V t−1(θ) ≥0.
Thus we have a.s. (P) on each An that
EQ

V t(θ) |Ft−1

−V t−1(θ) = EQ
 d

i=1
θn,i
t ∆S
i
t |Ft−1

=
d

i=1
θn,i
t EQ

∆S
i
t |Ft−1

= 0.

40
CHAPTER 2. MARTINGALE MEASURES
Again letting n increase to ∞, we have the identity
EQ

V t(θ) |Ft−1

= V t−1(θ) a.s. (P) .
(2.13)
Finally, as V0 = θ1 · S0 is a non-negative constant, it follows that
EQ

V 1

= V0. But by the first part of the proof V 1 ≥0 a.s. (P) and
hence a.s. (Q), so V 1 ∈L1(Q). We can therefore begin an induction, using
(2.13) at the inductive step, to conclude that V t ∈L1(Q) and EQ

V t(θ)

=
V0 for all t ∈T. Thus V (θ) is a non-negative Q-martingale, and since its
final value is βT H, it follows that V t(θ) = EQ (βT H |Ft ) a.s. (P) for each
t ∈T.
Remark 2.4.3. The identity (2.12) not only provides an alternative proof of
Lemma 2.2.5 by showing that the price of any attainable European claim
is independent of the particular generating strategy, since the right-hand
side does not depend on θ, but also provides a means of calculating that
price without having to construct such a strategy. Moreover, the price does
not depend on the choice of any particular equivalent martingale measure:
the left-hand side does not depend on Q.
Exercise 2.4.4. Use Proposition 2.4.2 to show that if θ is a self-financing
strategy whose final discounted value is bounded below a.s. (P)by a con-
stant, then for any EMM Q the expected final value of θ is simply its initial
value. What conclusion do you draw for trading only with strategies that
have bounded risk?
We have proved that the existence of an equivalent martingale mea-
sure for S is sufficient for viability of the securities market model. In the
next chapter, we discuss the necessity of this condition. Mathematically,
the search for equivalent measures under which the given process S is a
martingale is often much more convenient than having to show that no
arbitrage opportunities exist for S.
Economically, we can interpret the role of the martingale measure as
follows. The probability assignments that investors make for various events
do not enter into the derivation of the arbitrage price; the only criterion is
that agents prefer more to less and would therefore become arbitrageurs if
the market allowed arbitrage. The price we derive for the contingent claim
H must thus be the same for all risk preferences (probability assignments)
of the agents as long as they preclude arbitrage. In particular, an econ-
omy of risk-neutral agents will also produce the arbitrage price we derived
previously. The equivalent measure Q, under which the discounted price
process is a martingale represents the probability assignment made in this
risk-neutral economy, and the price that this economy assigns to the claim
will simply be the average (i.e., expectation under Q) discounted value of
the payoffH.
Thus the existence of an equivalent martingale measure provides a gen-
eral method for pricing contingent claims, which we now also formulate in
terms of undiscounted value processes.

2.4. ARBITRAGE PRICING: MARTINGALE MEASURES
41
Martingale Pricing
We summarise the role played by martingale measures in pricing claims.
Assume that we are given a viable market model (Ω, F, P, F, S) and some
equivalent martingale measure Q. Recall that a contingent claim in this
model is a non-negative (F-measurable) random variable H representing a
contract that pays out H(ω) dollars at time T if ω ∈Ωoccurs. Its time
0 value or (current) price π(H) is then the value that the parties to the
contract would deem a ‘fair price’ for entering into this contract.
In a viable model, an investor could hope to evaluate π(H) by con-
structing an admissible trading strategy θ ∈Θa that exactly replicates the
returns (cash flow) yielded by H at time T. For such a strategy θ, the initial
investment V0(θ) would represent the price π(H) of H. Recall that H is an
attainable claim in the model if there exists a generating strategy θ ∈Θa
such that VT (θ) = H, or, equivalently, V t(θ) = βT H. But as Q is a mar-
tingale measure for S, V (θ) is, up to a constant, a martingale transform,
and hence a martingale, under Q, it follows that for all t ∈T,
V t(θ) = EQ (βT H |Ft ) ,
and thus
Vt(θ) = β−1
t
EQ (βT H |Ft )
(2.14)
for any θ ∈Θa. In particular,
π(H) = V 0(θ) = EQ (βT H |F0 ) = EQ (βT H) .
(2.15)
Market models in which all European contingent claims are attainable
are called complete. These models provide the simplest class in terms of op-
tion pricing since any contingent claim can be priced simply by calculating
its (discounted) expectation relative to an equivalent martingale measure
for the model.
Uniqueness of the EMM
We have shown in Proposition 2.4.2 that for an attainable European claim
H the identity ¯V0(θ) = EQ (βT H) holds for every EMM Q in the model
and for every replicating strategy θ.
This immediately implies that in a complete model the EMM must be
unique. For if Q and R are EMMs in a complete pricing model, then any
European claim is attainable. It follows that EQ (βT H) = ER (βT H) and
hence also
EQ (H) = ER (H) ,
(2.16)
upon multiplying both sides by βT , which is non-random. In particular,
equation (2.16) holds when the claim is the indicator function of an ar-
bitrary set F ∈FT = F. This means that Q = R; hence the EMM is

42
CHAPTER 2. MARTINGALE MEASURES
unique. Moreover, our argument again verifies that the Law of One Price
(see Lemma 2.2.5) must hold in a viable model; that is, we cannot have
two admissible trading strategies θ, θ′ that satisfy VT (θ) = VT (θ′) but
V0(θ) ̸= V0(θ′). Our modelling assumptions are thus sufficient to guarantee
consistent pricing mechanisms (in fact, this consistency criterion is strictly
weaker than viability; see [241] for simple examples).
The Law of One Price permits valuation of an attainable claim H
through the initial value of a self-financing strategy that generates H; the
valuation technique using risk-neutral expectations gives the price π(H)
without prior determination of such a generating strategy. In particular,
consider a single-period model and a claim H (an Arrow-Debreu security)
defined by
H(ω) =

1
if ω = ω′
0
otherwise,
where ω′ ∈Ωis some specified state. If H is attainable, then
π(H) = EQ (βT H) = 1
βT
Q({ω′}).
This holds even when β is random. The ratio Q({ω′})
βT (ω′) is known as the state
price of ω′. In a finite market model, we can similarly define the change
of measure density Λ = Λ({ω})ω∈Ω, where Λ({ω}) = Q({ω})
P ({ω})) as the state
price density. See [241] for details of the role of these concepts.
Superhedging
We adopt a slightly more general approach (which we shall develop further
in Chapter 5 and exploit more fully for continuous-time models in Chapters
7 to 10) to give an explicit justification of the ‘fairness’ of the option price
when viewed from the different perspectives of the buyer and the seller
(option writer), respectively.
Definition 2.4.5. Given a European claim H = f(ST ), an (x, H)−hedge is
an initial investment x in an admissible strategy θ such that VT (θ) ≥H a.s.
This approach to hedging is often referred to as defining a superhedging
strategy.
This clearly makes good sense from the seller’s point of view,
particularly for claims of American type, where the potential liability may
not always be covered exactly by replication. By investing x in the strategy
θ at time 0, an investor can cover his potential liabilities whatever the
stock price movements in [0, T]. When there is an admissible strategy θ
exactly replicating H, the initial investment x = π(H) is an example of an
(x, H)−hedge. Since the strategy θ exactly covers the final liabilities, (i.e.,
VT (θ) = H), we call this a minimal hedge.
All prices acceptable to the option seller must clearly ensure that the
initial receipts for the option enable him to invest in a hedge (i.e., must

2.5. STRATEGIES USING CONTINGENT CLAIMS
43
ensure that there is an admissible strategy whose final value is at least H).
The seller’s price can thus be defined as
πs = inf {z ≥0 : there exists θ ∈Θa with VT (θ) = z + GT (θ) ≥H a.s.} .
The buyer, on the other hand, wants to pay no more than is needed to
ensure that his final wealth suffices to cover the initial outlay, or borrowings.
So his price will be the maximum he is willing to borrow, y = −V0, at time
0 to invest in an admissible strategy θ, so that the sum of the option payoff
and the gains from following θ cover his borrowings. The buyer’s price is
therefore
πb = sup {y ≥0 : there exists θ ∈Θa with −y + GT (θ) ≥−H a.s.} .
In particular, θ must be self-financing, so that βT VT (θ) = V0+βT GT (θ),
and since βS is a Q-martingale, we have EQ (βT GT (θ)) = 0. So the seller’s
price requires that z ≥EQ (βT H) for each z in (2.21)and hence πs ≥
EQ (βT H) .
Similarly, for the buyer’s price, we require that −y+EQ (βT H) ≥0 and
hence also πb ≤EQ (βT H) . We have proved the following proposition.
Proposition 2.4.6. For any integrable European claim H in a viable pric-
ing model,
πb ≤EQ (βT H) ≤πs.
(2.17)
If the claim H is attained by an admissible strategy θ, the minimal
initial investment z in the strategy θ that will yield final wealth VT (θ) = H
is given by EQ (βT H) , and conversely this represents the maximal initial
borrowing y required to ensure that −y + GT (θ) + H ≥0. This proves the
following corollary.
Corollary 2.4.7. If the European claim H is attainable, then the buyer’s
price and seller’s price are both equal to EQ (βT H) . Thus, in a com-
plete model, every European claim H has a unique price, given by π =
EQ (βT H) , and the generating strategy θ for the claim is a minimal hedge.
2.5
Strategies Using Contingent Claims
Our definition of arbitrage involves trading strategies that include only
primary securities (i.e., a riskless bank account which acts as num´eraire
and a collection of risky assets, which we called ‘stocks’ for simplicity).
Our analysis assumes that these assets are traded independently of other
assets. In real markets, however, investors also have access to derivative
(or secondary) securities, whose prices depend on those of some underlying
assets. We have grouped these under the term ‘contingent claim’ and we
have considered how such assets should be priced. Now we need to consider
an extended concept of arbitrage since it is possible for an investor to build

44
CHAPTER 2. MARTINGALE MEASURES
a trading strategy including both primary securities and contingent claims,
and we use this combination to seek to secure a riskless profit. We must
therefore identify circumstances under which the market will preclude such
profits.
Thus our concept of a trading strategy should be extended to include
such combinations of primary and secondary securities, and we shall show
that the market remains viable precisely when the contingent claims are
priced according to the martingale pricing techniques for European contin-
gent claims that we have developed. To achieve this, we need to restrict
attention to trading strategies involving a bank account, stocks, and at-
tainable European contingent claims.
Assume that a securities market model (Ω, F, P, T, F, S) is given. We
allow trading strategies to include attainable European claims, so that the
value of the investor’s portfolio at time t ∈T will have the form
Vt = θt · St + γt · Zt =
d

i=0
θi
tSi
t +
m

j=1
γj
t Zj
t ,
(2.18)
where S0 is the bank account,

Si
t : i = 1, 2, . . . , d

are the prices of d
risky stocks, and Zt = (Zj
t )j≤m are the values of m attainable European
contingent claims with time T payofffunctions given by (Zj)j≤m.
We
write S = (Si)0≤i≤d.
Recall that an attainable claim Zj can be repli-
cated exactly by a self-financing strategy involving only the process S.
The holdings of each asset are assumed to be predictable processes, so that
for t = 1, 2, . . . , T, θi
t and γj
t are Ft−1-measurable for i = 0, 1, . . . , d and
j = 1, 2, . . . , m. We call our model an extended securities market model.
The trading strategy φ = (θ, γ) is self-financing if its initial value is
V0(φ) = θ1 · S0 + γ1 · Z0
and for t = 1, 2, . . . , T −1 we have
θt · St + γt · Zt = θt+1 · St + γt+1 · Zt.
(2.19)
Note that · denotes the inner product in Rd+1 and Rm, respectively. A new
feature of the extended concept of a trading strategy is that the final values
of some of its components are known in advance since the final portfolio
has value
VT (φ) = θT · ST + γT · Z,
as Z = (Zj
T )j≤m represents the m payofffunctions of the European claims.
Moreover, unlike stocks, we have to allow for the possibility that the values
Zj
t can be zero or negative (as can be the case with forward contracts).
However, with these minor adjustments we can regard the model simply

2.5. STRATEGIES USING CONTINGENT CLAIMS
45
as a securities market model with one riskless bank account and d + m
risky assets. With this in mind, we extend the concept of arbitrage to this
model.
Definition 2.5.1. An arbitrage opportunity in the extended securities
market model is a self-financing trading strategy φ such that V0(φ) = 0,
VT (φ) ≥0, and EP (VT (φ)) > 0. We call the model arbitrage-free if no such
strategy exists.
As in the case of weak arbitrage in Section 2.2, we do not demand
that the value process remain non-negative throughout T. That this has
no effect on the pricing of the contingent claims can be seen from the
following result.
Theorem 2.5.2. Suppose that (Ω, F, P, T, F, S) is an extended securities
market model admitting an equivalent martingale measure Q. The model
is arbitrage-free if and only if every attainable European contingent claim
with payoffZ has value process given by

S0
t EQ

Z
S0
T |Ft

: t ∈T

.
Proof. Let θ = (θi)i≤d be a generating strategy for Z. The value process of
θ is then given as in equation (2.14) by Vt(θ) = S0
t EQ

Z
S0
T |Ft

since the
discount process is βt =
1
S0
t when S0 is the numeraire.
We need to show that the model is arbitrage-free precisely when the
value process (Zt)t∈T of the claim Z is equal to (Vt(θ))t∈T. Suppose there-
fore that for some u ∈T these processes differ on a set D of positive
P-measure. We first assume that D = {Zu > Vu(θ)}, which belongs to Fu.
To construct an arbitrage, we argue as follows: do nothing for ω /∈D, and
for ω ∈D wait until time u. At time u, sell short one unit of the claim Z
for Zu(ω), invest Vu(ω) of this in the portfolio of stocks and bank account
according to the prescriptions given by strategy θ, and bank the remainder
(Zu(ω) −Vu(ω)) until time T. This produces a strategy φ, where
φt =

0
if t ≤u

θ0
t + Zu−Vu(θ)
S0
u
, θ1
t , . . . , θd
t , −1

1D
if t > u.
It is not hard to show that this strategy is self-financing; it is evidently
predictable. Its value process V (φ) has V0(φ) = 0 since in fact Vt(φ) = 0
for all t ≤u, while VT (φ)(ω) = 0 for ω /∈D. For ω ∈D, we have
(θT · ST )(ω) = VT (θ)(ω) = Z(ω)
since θ replicates Z. Hence
VT (φ)(ω) =

θT · ST + (Zu −Vu(θ))S0
T
S0u
−Z

(ω)
=

(Zu −Vu(θ))S0
T
S0u

(ω)

46
CHAPTER 2. MARTINGALE MEASURES
> 0.
This shows that φ is an arbitrage opportunity in the extended model since
VT (φ) ≥0 and P(VT (φ) > 0) = P(D) > 0.
To construct an arbitrage when Zu < Vu(θ) for some u ≤T on a set
E with P(E) > 0, we simply reverse the positions described above. On E
at time u, shortsell the amount Vu(θ) according to the strategy θ, buy one
unit of the claim Z for Zu, place the difference in the bank, and do nothing
else. Hence, if the claim Z does not have the value process V (θ) determined
by the replicating strategy θ, the extended model is not arbitrage-free.
Conversely, suppose that every attainable European claim Z has its
value function given via the EMM Q as Zt = S0
t EQ

Z
S0
T |Ft

for each
t ≤T, and let ψ = (φ, γ) be a self-financing strategy, involving S and
m attainable European claims (Zj)j≤m, with V0(ψ) = 0 and VT (ψ) ≥
0. We show that P(VT (ψ) = 0) = 1, so that ψ cannot be an arbitrage
opportunity in the extended model. Indeed, consider the discounted value
process V (ψ) = V (ψ)
S0
at time t > 0:
EQ

V t(ψ) |Ft−1

= EQ
⎛
⎝
d

i=0
φi
tS
i
t +
m

j=1
γj
t
Zj
t
S0
t
|Ft−1
⎞
⎠
=
d

i=0
φi
tEQ

S
i
t |Ft−1

+
m

j=1
γj
t EQ

V
j
t(θj) |Ft−1

.
Here we use the fact that S
i = Si
S0 is a martingale under Q and, defining
V
j
t(θj) as the discounted value process of the replicating strategy for the
claim Zj, we see that V
j
t(θj) = EQ

Zj
S0
T |Ft

=
Zj
t
S0
t . Since each process
V
j(θj), j ≤m, is a Q-martingale, it follows that
EQ

V t(ψ) |Ft−1

=
d

i=0
φi
tS
i
t−1 +
m

j=1
γj
t V
j
t−1(θj) = V t−1(ψ)
since the strategy ψ = (φ, γ) is self-financing, so that V (ψ) is also a
Q-martingale.
Consequently, EQ

V t(ψ)

= EQ (V0(ψ)) = 0. Therefore
Q(V T (ψ) = 0) = 1, and since Q ∼P it follows that P(VT (ψ) = 0) = 1.
Therefore the extended securities market model is arbitrage-free.
This result should not come as a surprise. It remains the case that
the only independent sources of randomness in the model are the stock
prices S1, S2, . . . , Sd, since the contingent claims used to construct trading
strategies are priced via an equivalent measure for which their discounted
versions are martingales. However, it does show that the methodology is
consistent. We return to extended market models when examining possible
arbitrage-free prices for claims in incomplete models in Chapter 4.

2.5. STRATEGIES USING CONTINGENT CLAIMS
47
Some Consequences of Call-Put parity
In the call-put parity relation (1.3), the discount rate is given by βt,T =
βT −t, where β = (1 + r). Write (1.3) in the form
St = Ct −Pt + βT −tK.
(2.20)
With the price of each contingent claim expressed at the expectation
under the risk-neutral measure Q of its discounted final value, we show
that the right-hand side of (2.20) is independent of K. Indeed,
St = βT −t[EQ

(ST −K)+
−EQ

(K −ST )+
+ K]
= βT −t

{ST ≥K}
(ST −K)dQ −

{ST <K}
(K −ST )dQ + K

= βT −t

Ω
(ST −K)dQ + K

= βT −tEQ (ST )
= β−1
t
EQ

βT ST

.
This shows that call-put parity is a consequence of the martingale property
of the discounted price under Q in any market model that allows pricing of
contingent claims by expectation under an equivalent martingale measure.
Remark 2.5.3. The identity also leads to the following interesting obser-
vation due to Marek Capinski, which first appeared in [35].
Recall the
Modigliani-Miller theorem (see [20]), which states that the value of a firm
is independent of the way in which it is financed. Since its value is repre-
sented by the sum of its equity (stock) and debt, the theorem states that
the level of debt has no impact on the value of the firm.
This can be
interpreted in terms of options, as follows.
If the firm’s borrowings at time 0 are represented by βT K, so that it
faces repayment of debt at K by time T, the stockholders have the option
to buy back this debt at that time, in order to avert bankruptcy of the
firm.
They will only do so if the value ST of the firm at time T is at
least K. The firm’s stock can therefore be represented as a European call
option on S with payoffK at time T, and thus the current (time 0) value of
the stock is the call option price C0. The total current value of the firm is
S0 = C0−P0+βT K, where P0 is a put option on S with the same strike and
horizon as the call. The calculation above shows that S0 is independent of
K, as the Modigliani-Miller theorem claims. Moreover, the current value
of the debt is given via the call-put parity relation as (βT K −P0). This is
lower than the present value βT K of K, so that P0 reflects the default risk
(i.e., risk that the debt may not be recovered in full at time T).

48
CHAPTER 2. MARTINGALE MEASURES
2.6
Example: The Binomial Model
We now take another look at the Cox-Ross-Rubinstein binomial model,
which provides a very simple, yet striking, example of the strength of the
martingale methods developed so far.
The CRR Market Model
The Cox-Ross-Rubinstein binomial market model was described in Chap-
ter 1. Recall that we assumed that d = 1. There is a single stock S1 and
a riskless bond S0, which accrues interest at a fixed rate r > 0. Taking
S0
0 = 1, we have S0
t = (1 + r)t for t ∈T, and hence βt = (1 + r)−t. The
ratios of successive stock values are Bernoulli random variables; that is, for
all t < T, either S1
t = S1
t−1(1+a) or S1
t = S1
t−1(1+b), where b > a > −1 are
fixed throughout, while S1
0 is constant. We can thus conveniently choose
the sample space
Ω= {1 + a, 1 + b}T
together with the natural filtration F generated by the stock price values;
that is, F0 = {∅, Ω}, and Ft = σ(S1
u : u ≤t) for t > 0. Note that FT =
F = 2Ωis the σ-field of all subsets of Ω.
The measure P on Ωis the measure induced by the ratios of the stock
values. More explicitly, we write S for S1 for the rest of this section to
simplify the notation, and set Rt =
St
St−1 for t > 0. For ω = (ω1, ω2, . . . , ωT )
in Ω, define
P({ω}) = P(Rt = ωt, t = 1, 2, . . . , T).
(2.21)
For any probability measure Q on (Ω, F), the relation EQ

St |Ft−1

=
St−1 is equivalent to
EQ (Rt |Ft−1 ) = 1 + r
since
βt
βt−1 = 1+r. Hence, if Q is an equivalent martingale measure for S, it
follows that EQ (Rt) = 1 + r. On the other hand, Rt only takes the values
1 + a and 1 + b; hence its average value can equal 1 + r only if a < r < b.
We have yet again verified the following result.
Lemma 2.6.1. For the binomial model to have an EMM, we must have
a < r < b.
When the binomial model is viable, there is a unique equivalent martin-
gale measure Q for S. We construct this measure in the following lemma.
Lemma 2.6.2. The discounted price process S is a Q-martingale if and
only if the random variables (Rt) are independent, identically distributed,
and Q(R1 = 1 + b) = q and Q(R1 = 1 + a) = 1 −q, where q = r−a
b−a.

2.6. EXAMPLE: THE BINOMIAL MODEL
49
Proof. Under independence, the (Rt) satisfy
EQ (Rt |Ft−1 ) = EQ (Rt) = q(1+b)+(1−q)(1+a) = q(b−a)+1+a = 1+r.
Hence, by our earlier discussion, S is a Q-martingale.
Conversely, if EQ (Rt |Ft−1 ) = 1+r, then, since Rt takes only the values
1 + a and 1 + b, we have
(1 + a)Q(Rt = 1 + a |Ft−1 ) + (1 + b)Q(Rt = 1 + b |Ft−1 ) = 1 + r,
while
Q(Rt = 1 + a |Ft−1 ) + Q(Rt = 1 + b |Ft−1 ) = 1.
Letting q = Q(Rt = 1 + b |Ft−1 ), we obtain
(1 + a)(1 −q) + (1 + b)q = 1 + r.
Hence q = r−a
b−a . The independence of the Rt follows by induction on t > 0.
For ω = (ω1, ω2, . . . , ωT ) ∈Ω, we see inductively that
Q (R1 = ω1, R2 = ω2, . . . , Rt = ωt) =
t
i=1
qi,
where qi = q when ωi = 1 + b and equals 1 −q when ωi = 1 + a. Thus the
(Rt) are independent and identically distributed as claimed.
Remark 2.6.3. Note that q ∈(0, 1) if and only if a < r < b. Thus a
viable binomial market model admits a unique EMM given by Q as in
Lemma 2.6.2.
The CRR Pricing Formula
The CRR pricing formula, obtained in Chapter 1 by an explicit hedging
argument, can now be deduced from our general martingale formulation
by calculating the Q-expectation of a European call option on the stock.
More generally, the value of the call CT = (ST −K)+ at time t ∈T is given
by (2.14); that is,
Vt(CT ) = 1
βt
EQ (βT CT |Ft ) .
Since ST = St
 T
u=t+1 Ru (by the definition of (Ru)), we can calculate
this expectation quite easily since St is Ft-measurable and each Ru (u > t)
is independent of Ft. Indeed,
Vt(CT ) = β−1
t
βT EQ
⎛
⎝
!
St
T

u=t+1
Ru −K
"+
|Ft
⎞
⎠

50
CHAPTER 2. MARTINGALE MEASURES
= (1 + r)t−T EQ
⎛
⎝
!
St
T

u=t+1
Ru −K
"+
|Ft
⎞
⎠
= v(t, St).
(2.22)
Here
v(t, x) = (1 + r)t−T EQ
⎛
⎝
!
x
T

u=t+1
Ru −K
"+⎞
⎠
= (1 + r)t−T
T −t

u=0
T −t
u

qu(1 −q)T −t−u 
x(1 + b)u(1 + a)T −t−u −K
+
and, in particular, the price at time 0 of the European call option C with
payoffCT = (ST −K)+ is given by
v(0, S0) = (1 + r)−T
T

u=A
T
u

qu(1 −q)T −u 
S0(1 + b)u(1 + a)T −u −K

,
(2.23)
where A is the first integer k for which S0(1 + b)k(1 + a)T −k > K. The
CRR option pricing formula (1.5.3) now follows exactly as in Chapter 1.
Exercise 2.6.4. Show that for the replicating strategy θ = (θ0, θ1) describ-
ing the value process of the European call C, the stock portfolio θ1 can be
expressed in terms of the differences of the value function as θ1
t = θ(t, St−1),
where
θ(t, x) = v(t, x(1 + b)) −v(t, x(1 + a))
x(b −a)
.
Exercise 2.6.5. Derive the call-put parity relation (2.20) by describing the
values of the contingent claims involved as expectations relative to Q.
2.7
From CRR to Black-Scholes
Construction of Approximating Binomial Models
The binomial model contains all the information necessary to deduce the
famous Black-Scholes formula for the price of a European call option in a
continuous-time market driven by Brownian motion. A detailed discussion
of the mathematical tools used in that model is deferred until Chapter 6,
but we now describe how the random walks performed by the steps in
the binomial tree lead to Brownian motion as a limiting process when we
reduce the step sizes continually while performing an ever larger number
of steps within a fixed time interval [0, T]. From this we will see how the
Black-Scholes price arises as a limit of CRR prices.

2.7. FROM CRR TO BLACK-SCHOLES
51
Consider a one-dimensional stock price process S = (St) on the finite
time interval [0, T] on the real line, together with a European put option
with payofffunction fT = (K −ST )+ on this stock. We use put options
here because the payofffunction f is bounded, thus allowing us to deduce
that the relevant expectations (using EMMs) converge once we have shown
via a central limit theorem that certain random variables converge weakly.
The corresponding result for call options can then be derived using call-put
parity.
We wish to construct a discrete-time binomial model beginning with
the same constant stock price S0 and with N steps in [0, T]. Thus we let
hN =
T
N and define the discrete timeline TN = {0, hN, 2hN, . . . , NhN} .
The European put P N with strike K and horizon T is then defined on TN.
By (2.14), (exactly as in the derivation of (2.22)), P N has CRR price P N
0
given by
P N
0 = (1 + ρN)−NEQN
⎛
⎝
!
K −S0
N

k=1
RN
k
"+⎞
⎠,
(2.24)
where, writing SN
k for the stock price at time khN, the ratios RN
k =
SN
k
SN
k−1
take values 1 + bN or 1 + aN at each discrete time point khN (k ≤N).
The values of aN, bN and the riskless interest rate ρN have yet to be
chosen.
Once they are fixed, with aN < ρN < bN, they will uniquely
determine the risk-neutral probability measure QN for the Nth binomial
model since by Lemma 2.6.2 the binomial random variables (RN
k )k≤N are
then an independent and identically distributed sequence. We obtain, as
before, that
QN(RN
1 = 1 + bN) = qN = ρN −aN
bN −aN
.
(2.25)
We treat the parameters from the Black-Scholes model as given and ad-
just their counterparts in our CRR models in order to obtain convergence.
To this end, we fix r ≥0 and set ρN = rhN, so that the discrete-time
riskless rate satisfies limN→∞(1 + ρN)N = erT , so that r acts as the ‘in-
stantaneous’ rate of return.
Fix σ > 0, which will act as the volatility per unit time of the Black-
Scholes stock price, and for each fixed N we now fix aN, bN by demanding
that the discounted logarithmic returns are given by
log
 1 + bN
1 + ρN

= σ

hN = σ
#
T
N ,
log
1 + aN
1 + ρN

= −σ

hN = −σ
#
T
N ,
so that
uN = 1 + bN =

1 + rT
N

eσ√
T
N ,
dN = 1 + aN =

1 + rT
N

e−σ√
T
N .

52
CHAPTER 2. MARTINGALE MEASURES
Note that the discount factor at each step is 1 + ρN = 1 + rT
N for each
k ≤N. The random variables
$
Y N
k
= log

RN
k
1 + ρN

: k ≤N
%
are independent and identically distributed. We shall consider their sum
ZN =
N

k=1
Y N
k
=
N

k=1
RN
k −N log(1 + ρN)
for each N. The discounted stock price is thus
S
N
N = (1 + ρN)−N
n

k=1
RN
k = exp
 N

k=1
Y N
k
&
= eZN ,
so that the N th put option price becomes
P N
0 = EQN
⎛
⎝
!
1 + rt
N
−N
K −S0eZN
"+⎞
⎠.
(2.26)
Convergence in Distribution
The values taken by Y N
1
are ±σ√hN, so its second moment is σ2hN = σ2 T
N ,
while its mean is given by
µN = (2qN −1)σ

hN = (2qN −1)σ
#
T
N .
Our choices will imply that qN converges to 1
2 as N →∞. We show
this by checking the rate of convergence. First recall some notation: aN =
a + o
 1
N

means that N(aN −a) →0 as N →∞.
Since 1 −qN = uN−ρN
uN−dN , we see that 2qN −1 is of order
1
√
N :
2qN −1 = 1 −2(1 −qN) = 1 −2

eσ√hN −1
eσ√hN −e−σ√hN

= 1 −eσ√hN −1
sinh(σ√hN).
Expanding into Taylor series the right-hand side has the form
1 −x + x2
2! + x3
3! + · · ·
x + x3
3! + · · ·
= −x2
2 −x4
4! + · · ·
x + x3
3! + · · ·
,
so that 2qN −1 = −1
2σ√hN + o
 1
N

. Thus µN = −1
2
σ2T
N + o
 1
N

, so that
NµN →−1
2σ2T as N →∞.

2.7. FROM CRR TO BLACK-SCHOLES
53
Since the second moment of Y N
1
is σ2 T
N , its variance σ2
N therefore sat-
isfies
σ2
N = σ2 T
N + o
 1
N

.
(2.27)
We apply the central limit theorem for triangular arrays (see, e.g. , [168,
VII.5.4] or [45, Corollary to Theorem 3.1.2]) in the following form to the
independent and identically distributed random variables (Y N
k ) for k ≤N
and N ∈N.
Theorem 2.7.1 (Central Limit Theorem). For N ≥1, let (Y N
k )k≤N
be an independent and identically distributed sequence of random variables,
each with mean µN and variance σ2
N. Suppose that there exist real µ and
Σ2 > 0 such that NµN →µ and σ2
N = Σ2 + o
 1
N

as N →∞. Then
the sums ZN = N
k=1 Y N
k
converge in distribution to a random variable
Z ∼N(µ, Σ2).
We prove this by verifying the Lindeberg-Feller condition for the Y N
k ,
namely that for all ε > 0
N

k=1
EQN

(Y N
k )21{|Y N
k |>ε}

→0 as N →∞.
(2.28)
We have seen that for fixed N and all k ≤N, (Y N
k )2 is constant on
Ωand takes the value σ2T
N . Therefore, using Chebychev’s inequality with
''Y N
k
'' = σ
(
T
N , we see that for each k ≤N
EQN

(Y N
k )21{|Y N
k |>ε}

= σ2T
N P(
''Y N
k
'' > ε) ≤σ2T
N
E
''Y N
k
''
ε
,
and since the right-hand side equals σ3
ε
 T
N
 3
2 , the Lindeberg condition is
satisfied. The Lindeberg-Feller Theorem completes the proof.
For the sequence (Y N
k ) defined above, the conditions of the theorem are
satisfied with µ = −1
2σ2T and Σ = 1
2σ2T with σ as fixed above. Thus (ZN)
converges in distribution to Z ∼N(−1
2σ2T, σ2T), while (1 + ρN)−N →
e−rT as N →∞. It follows that the limit of the CRR put option prices
(P N
0 ) is given by
E

(e−rT K −S0eZ)+
,
(2.29)
where the expectation is now taken with respect to the distribution of Z.
The Black-Scholes Formula
Standardising Z, we see that the random variable X =
1
σ
√
T (Z + 1
2σ2T)
has distribution N(0, 1); that is, Z = σ
√
TX −1
2σ2T. The limiting value
of P N
0
can be found by evaluating the integral
 ∞
−∞
)
e−rT K −S0e−1
2 σ2T +σ
√
T x*+ e−1
2 x2
√
2π dx.
(2.30)

54
CHAPTER 2. MARTINGALE MEASURES
Observe that the integrand is non-zero only when
σ
√
Tx +

r −1
2σ2

T < log
 K
S0

,
that is, on the interval (−∞, γ), where
γ =
log

K
S0

−(r −1
2σ2)T
σ
√
T
.
Thus the put option price for the limiting pricing model reduces to
P0 = Ke−rT (Φ(γ)) −S0
 γ
−∞
e−σ2T
2 eσ
√
T x−x2
2
dx
√
2π
= Ke−rT (Φ(γ)) −S0
 γ
−∞
e−1
2 (x−σ
√
T )2 dx
√
2π
= Ke−rT (Φ(γ)) −S0

Φ(γ −σ
√
T)

.
Here Φ denotes the cumulative normal distribution function.
Setting d−= −γ and d+ = d−+ σ
√
T, and using the symmetry of Φ,
we obtain 1−Φ(γ) = Φ(−γ) = Φ(d−) and 1−Φ(γ −σ
√
T) = Φ(d+), where
d± = log
 S0
K

+ (r ± 1
2σ2)T
σ
√
T
.
(2.31)
By call-put parity, this gives the familiar Black-Scholes formula for the call
option: the time 0 price of the call option fT = (ST −K)+ is given by
V0(C) = C0 = S0Φ(d+) −e−rT KΦ(d−).
(2.32)
Remark 2.7.2. An alternative derivation of this approximating procedure,
using binomial models where for each n the probabilities of the ‘up’ and
‘down’ steps are equal to 1
2, can be found in [35].
By replacing T by T −t and S0 by St, we can read offthe value process
Vt for the option similarly; in effect this treats the option as a contract
written at time t with time to expiry T −t,
Vt(C) = StΦ(dt+) −e−r(T −t)KΦ(dt−),
(2.33)
where
dt± = log
 St
K

+ (r ± 1
2σ2)(T −t)
σ
√
T −t
.
The preceding derivation has not required us to study the dynamics of
the ‘limit stock price’ S; it is shown in Chapter 7 that this takes the form
dSt = Stµdt + σStdWt,
(2.34)

2.7. FROM CRR TO BLACK-SCHOLES
55
where W is a Brownian motion. The stochastic calculus necessary for the
solution of such stochastic differential equations is developed in Chapter 6.
However, we can already note one remarkable property of the Black-Scholes
formula: it does not involve the mean return µ of the stock but depends on
the riskless interest rate r and the volatility σ. The mathematical reason
for this lies in the change to a risk-neutral measure (which underlies the
martingale pricing techniques described in this chapter), which eliminates
the drift term from the dynamics.
Dependence of the Option Price on the Parameters
Write Ct = Vt(C) for the Black-Scholes value process of the call option;
i.e.,
Ct = StΦ(dt+) −e−r(T −t)KΦ(dt−),
where dt± is given as in (2.33). As we have calculated for the case t = 0,
the European put option with the same parameters in the Black-Scholes
pricing model is given by
Pt = Ke−r(T −t)Φ(−dt−) −StΦ(−dt+).
We examine the behaviour of the prices Ct at extreme values of the param-
eters. (The reader may consider the put prices Pt similarly.)
When St increases, dt± grows indefinitely, so that Φ(dt±) tends to 1,
and so Ct has limiting value St −Ke−r(T −t). In effect, the option becomes
a forward contract with delivery price K since it is ‘certain’ to be exercised
at time T. Similar behaviour is observed when the volatility σ shrinks to 0
since again dt± become infinite, and the riskless stock behaves like a bond
(or money in the bank).
When t →T (i.e., the time to expiry decreases to 0) and St > K, then
dt± becomes ∞and e−r(T −t) →1, so that Ct tends to St −K. On the
other hand, if St < K, log
 St
K

< 0 so that dt± = −∞and Ct →0. Thus,
as expected, Ct →(ST −K)+ when t →T.
Remark 2.7.3. Note finally that there is a natural ‘replicating strategy’
given by (2.33) since this value process is expressed as a linear combination
of units of stocks St and bonds S0
t with S0
0 = 1 and S0
t = β−1
t
S0
0 = ert.
Writing the value process Vt = θt · St (where by abuse of notation S =
(S0, S)), we obtain
θ0
t = −Ke−rT Φ(dt−),
θ1
t = Φ(dt+).
(2.35)
In Chapter 7, we consider various derivatives of the Black-Scholes op-
tion price, known collectively as ‘the Greeks’, with respect to its different
parameters. This provides a sensitivity analysis with parameters that are
widely used in practice.

Chapter 3
The First Fundamental
Theorem
We saw in the previous chapter that the existence of a probability measure
Q ∼P under which the (discounted) stock price process is a martingale is
sufficient to ensure that the market model is viable (i.e. , that it contains
no arbitrage opportunities). We now address the converse: whether for
every viable model one can construct an equivalent martingale measure for
S, so that the price of a contingent claim can be found as an expectation
relative to Q.
To deal with this question fully while initially avoiding difficult technical
issues that can obscure the essential simplicity of the argument, we shall
assume throughout Sections 3.1 to 3.4 that we are working with a finite
market model, so each σ-field Ft is generated by a finite partition Pt of
Ω. In Section 3.5, we then consider in detail the construction of equivalent
martingale measures for general discrete models without any restrictions on
the probability space. This requires considerably more advanced concepts
and results from functional analysis.
3.1
The Separating Hyperplane Theorem in
Rn
In finite markets, the following standard separation theorem for compact
convex sets in Rn, which is a special case of the Hahn-Banach separation
theorem (see [97], [264]), will suffice for our purposes.
Theorem 3.1.1 (Separating Hyperplane Theorem). Let L be a linear
subspace of Rn and let K be a compact convex subset in Rn disjoint from L.
Then we can separate L and K strictly by a hyperplane containing L; (i.e.,
there exists a (bounded) linear functional φ : Rn →R such that φ(x) = 0
for all x ∈L but φ(x) > 0 for all x ∈K).
57


## The First Fundamental Theorem

58
CHAPTER 3. THE FIRST FUNDAMENTAL THEOREM
The following lemma will be used in the proof but also has independent
interest.
Lemma 3.1.2. Let C be any closed convex subset of Rn that does not
contain the zero vector. Then there is a linear functional φ on Rn that has
a strictly positive lower bound on C.
Proof. Denote by B = B(0, r) the closed ball of radius r centred at the
origin in Rn, and choose r > 0 so that B intersects C. Then B ∩C is non-
empty, closed and bounded, and hence compact. Therefore the continuous
map x →|x|n attains its infimum over B ∩C at some z ∈B ∩C. (Here
|x| = |x|n denotes the Euclidean norm of x in Rn.) Since |x| > r when
x /∈B, it is clear that |x| ≥|z| for all x ∈C. In particular, since C is
convex, y = λx + (1 −λ)z is in C whenever x ∈C and 0 ≤λ ≤1, so that
|y| ≥|z| , i.e.,
|λx + (1 −λ)z|2 ≥|z|2 .
(3.1)
Multiplying out both sides of (3.1), writing a · b for the scalar product in
Rn, we obtain
λ2x · x + 2λ(1 −λ)x · z + (1 −λ)2z · z ≥z · z,
which simplifies at once to
2(1 −λ)x · z −2z · z + λ(x · x + z · z) ≥0.
This holds for every λ ∈[0, 1] . Letting λ →0, we obtain
x · z ≥z · z = |z|2 > 0.
Defining φ(x) = x · z, we have found a linear functional such that φ(x)
is bounded below on C by the positive number |z|2 . (φ is also bounded
above, as any linear functional on Rn is bounded.)
Proof of Theorem 3.1.1. Let K be a compact convex set disjoint from the
subspace L. Define
C = K −L = {x ∈Rn : x = k −l for some k ∈K, l ∈L} .
Since K and L are convex, C is also convex.
In addition, C is closed; indeed, if xn = kn −ln converges to some
x ∈Rn, then, as K is compact, (kn) has a subsequence converging to some
k ∈K. Thus xnr = knr −lnr →x as r →∞and knr →k, so that
lnr = knr −xnr →k −x and hence l = k −x belongs to L since L is closed.
But then x = k −l ∈C, so that C is closed.
As C does not contain the origin, we can therefore apply Lemma 3.1.2
to C to obtain a bounded linear functional φ on Rn such that φ(x) ≥
|z|2 > 0 for z as above.
In other words, writing x = k −l, we have
φ(k) −φ(l) ≥|z|2 > 0. This must hold for all x ∈C. Fix k and replace l

3.2. CONSTRUCTION OF MARTINGALE MEASURES
59
by λl for arbitrary positive λ if φ(l) ≥0 or by λl for arbitrary negative λ
if φ(l) < 0. The vectors λl belong to L, as L is a linear space; since φ is
bounded, we must have φ(l) = 0 (i.e., L is a subspace of the hyperplane
kerφ = {x : φ(x) = 0}, while φ(K) is bounded below by |z|2 > 0). The
result follows.
3.2
Construction of Martingale Measures
The above separation theorem applies to sets in Rn. We can apply it to
RΩ, the space of all functions Ω→R, by identifying this space with Rn for
a finite n, in view of the assumption that the σ-field F is finitely generated
(i.e., any F-measurable real function on Ωtakes at most n distinct values,
where n is the number of cells in the partition P that generates F). In
other words, we assume that Ω= D1 ∪D2 ∪· · · ∪Dn, where
Di ∩Dj = ∅for i ̸= j,
P(Di) = pi > 0 for i = 1, 2, . . . , n.
Without loss, we now take the (Di) as atoms or ‘points’ ωi of Ω. Thus
any random variable X defined on (Ω, F) will be regarded as a point
(X(ω1), X(ω2), . . . , X(ωn))
in Rn. We apply this in particular to the random variables making up the
value process {Vt(θ)(ω) : ω ∈Ω} and the gains process {Gt(θ)(ω) : ω ∈Ω}
of a given admissible strategy θ ∈Θa.
Recall (Definition 2.2.3) that the market model is viable if it contains no
arbitrage opportunities (i.e., if whenever a strategy θ ∈Θa has initial value
V0(θ) = 0, and final value VT (θ) ≥0 a.s. (P), then VT (θ) = 0 a.s. (P)).
Denote by C the positive orthant in Rn with the origin removed; i.e.,
C = {Y ∈Rn : Yi ≥0 for i = 1, 2, . . . , n, Yi > 0 for at least one i} . (3.2)
The set C is a cone (i.e., closed under vector addition and multiplication
by non-negative scalars) and is clearly convex.
The no-arbitrage assumption means that for every admissible strategy
θ ∈Θa we have that
V t(θ) = Gt(θ) /∈C if V0(θ) = 0.
Thus the discounted gains process G(θ) for such a strategy θ with initial
value zero cannot have a final value contained in C since otherwise it would
be an arbitrage opportunity.
Recall from (2.8) that a self-financing strategy θ =

θ0, θ1, θ2, . . . , θd
is completely determined by the stock holdings ˆθ =

θ1, θ2, . . . , θd
. Thus,
given a predictable Rd-valued process ˆθ =

θ1, θ2, . . . , θd
, there is a unique
predictable real-valued process θ0 such that the augmented process θ =

60
CHAPTER 3. THE FIRST FUNDAMENTAL THEOREM

θ0, θ1, θ2, . . . , θd
has initial value V0(θ) = 0 and is self-financing. By a
minor abuse of notation, we define the discounted gains process associated
with ˆθ as
Gt(ˆθ) =
t

u=1
θu · ∆S(u) =
t

u=1
 d

i=1
θi
u∆S
i
u

for t = 1, 2, . . . , T.
Suppose that Gt(ˆθ) ∈C. Then, with β denoting the discount factor,
VT (θ) = β−1
T V t(θ) = β−1
T (V0(θ) + Gt(θ)) = β−1
T Gt(ˆθ)
is non-negative and is strictly positive with positive probability. So θ is
a weak arbitrage, which contradicts the viability of the model. We have
proved the following result.
Lemma 3.2.1. If the market model is viable, the discounted gains process
associated with any predictable Rd-valued process ˆθ cannot belong to the
cone C.
Since Gt(ˆθ) is a sum of scalar products θt · ∆St in Rn, and since any
linear functional on Rn takes the form x →x · y for some y ∈Rn, the rele-
vance of the separation theorem to these questions now becomes apparent
in the proof of the next theorem, which is the main result in this section.
Theorem 3.2.2 (First Fundamental Theorem of Asset Pricing for
Finite Market Models). A finite market model is viable if and only if
there exists an equivalent martingale measure (EMM) for S.
Proof. Since we have already shown more generally (in Chapter 2) that the
existence of an EMM ensures viability of the model, we need only prove
the converse.
Suppose therefore that the market model is viable. We need to construct
a measure Q ∼P under which the price processes are martingales relative
to the filtration F. Recall that C is the convex cone of all real random
variables φ on (Ω, F) such that φ(ω) ≥0 a.s. and φ(ωi) > 0 for at least
one ωi ∈Ω= {ω1, ω2, . . . , ωn} (and by assumption pi = P({ωi}) > 0).
We have shown that in a viable market we must have Gt(ˆθ) /∈C for all
predictable Rd-valued processes ˆθ. On the other hand, the set defined by
such gains processes,
L =

Gt(ˆθ) : ˆθ =

θ1, θ2, . . . , θd
, with θi predictable for i = 1, 2, . . . , d

,
is a linear subspace of the vector space of all F-measurable real-valued
functions on Ω.
Since L does not meet C, we can separate L and the compact convex
subset K = {X ∈C : EP (X) = 1} of C by a linear functional f on Rn

3.3. PATHWISE DESCRIPTION
61
that is strictly positive on K and 0 on L. The linear functional has a
representation of the form
f(x) = x · q =
n

i=1
xiqi
for a unique q = (qi) in Rn. Taking ξi = (0, . . . , 0, 1
pi ,0,. . . ,0) in turn for
each i ≤n, we see that EP (ξi) =
pi
pi = 1, so that ξi ∈K, and hence
f(ξi) = qi
pi > 0. Thus qi > 0 for all i ≤n.
Now define a new linear functional g = f
α, where α = n
i=1 qi > 0. This
is implemented by the vector p∗with p∗
i = qi
α > 0, so that n
i=1 p∗
i = 1.
Hence we may use the vector p∗to induce a probability measure P ∗on
Ω= {ω1, ω2, . . . , ωn} by setting P ∗({ωi}) = p∗
i > 0, so that P ∗∼P.
Let E∗(·) denote expectation relative to P ∗. Since g(x) = 1
αf(x) = 0
for all x ∈L, we have E∗
GT

ˆθ

= 0 for each vector ˆθ of stock holdings,
creating a self-financing strategy θ with V0(θ) = 0. As V t(θ) = V0(θ) +
GT (θ), this implies that E∗
V T (θ)

= 0 for such θ. But by (2.8) we can
generate such θ from any n-dimensional predictable process, in particular
from (0, . . . , 0, θi, 0, . . . , 0), where the predictable real-valued process θi is
given for i ≤n. Thus
E∗
 T

t=1
θi
t∆S
i
t

= 0
holds for every bounded predictable process

θi
i=1,2,...,T . Theorem 2.3.5
now implies that each Si is a martingale under P ∗. Hence P ∗is the desired
EMM for the price process S.
3.3
Pathwise Description
The geometric origin of the above result is clear from the essential use
that was made of the separation theorem.
A geometric formulation of
Theorem 3.2.2 can be based on the ‘local’ equivalent of the no-arbitrage
condition in terms of ‘one-step’ changes in the value of a portfolio. In fact,
although the definition of (weak) arbitrage involves only the initial and
final values of a strategy, this will demonstrate that the no-arbitrage con-
dition is an assumption about the pathwise behaviour of the value process.
Although this discussion is somewhat detailed, it is included here for its
value in providing an intuitive grasp of the ideas that underlie the more
abstract proof of Theorem 3.2.2 and in giving a step-by-step construction
of the equivalent martingale measure.
As before, our discussion (which
follows [290]) is confined to the case where F is finitely generated.

62
CHAPTER 3. THE FIRST FUNDAMENTAL THEOREM
One-Step Arbitrage
The idea behind the construction lies in the following simple observation.
Consider a market model with a single bond and stock (i.e., d = 1) and
assume that the bond price S0 ≡1 for all trading dates. In particular,
for any self-financing strategy θ = (θ0, θ1), the value process Vt(θ) has
increments ∆Vt = θ1
t ∆S1
t , as ∆S0(t) = 0. These increments will be ‘con-
centrated’ to one side of the origin precisely when the same is true for the
price increments ∆S1
t .
Now suppose we know at some time (t −1) ∈T that the stock price S1
will not decrease in the time interval [t −1, t]; that is, for some partition
set A ∈Pt−1 we have P(

∆S1
t ≥0

|A) = 1. Then we can buy stock S1 at
time t −1, sell it again at time t, and invest the profit ∆S1
t in the riskless
bond until the time horizon T. To prevent this arbitrage opportunity, we
need to have P(

∆S1
t = 0

|A) = 1; i.e., that S1 (and hence also the value
process V (θ) associated with any admisssible strategy θ) is a ‘one-step
martingale’ in the time interval [t −1, t].
This idea can be extended to models with d stocks and hyperplanes in
Rd+1. In this case, we have
∆Vt(θ) = θt · ∆St =
d

k=1
θk
t ∆Sk
t ,
so it is clear that condition (i) in Proposition 3.3.1 below expresses the
fact that, along each sample path of the price process S, the support of the
conditional distribution of the vector random variable ∆St, given A ∈Pt−1,
cannot be wholly concentrated only on one ‘side’ of any hyperplane in Rd+1.
Assume for the remainder of this section that S0(t) ≡1 for all t ∈T.
Proposition 3.3.1. If the finite market model S =

S0, S1, S2, . . . , Sd
is
viable, then, for all θ ∈Θ, t > 0 and A ∈Pt−1, and with Vt = Vt(θ), the
following hold:
P(∆Vt ≥0 |A) = 1 implies that P(∆Vt = 0 |A) = 1,
P(∆Vt ≤0 |A) = 1 implies that P(∆Vt = 0 |A) = 1.
Proof. Fix t > 0 and θ ∈Θ. Suppose that P(∆Vt ≥0 |A) = 1 for some
A ∈Pt−1. We define ψ with ψ0 = 0 as follows for s > 0: let
ψs(ω) = 0 for all s = 1, 2, . . . , T and ω /∈A,
while, for ω ∈A,
ψs(ω) =
⎧
⎪
⎨
⎪
⎩
0
if 0 < s < t,
(θ0
t (ω) −Vt−1(θ)(ω), θ1
t (ω), θ2
t (ω), . . . , θd
t (ω))′
if s = t,
(Vt(θ)(ω), 0, . . . , 0)′
if s > t.

3.3. PATHWISE DESCRIPTION
63
Under the strategy ψ, we start with no holdings at time 0 and trade
only from time t onwards, and then only if ω ∈A (which we know by time
t −1). In that case, we elect to follow the strategy θ in respect to stocks
and borrow an amount equal to (Vt−1(θ) −θ0) in order to deal in stocks at
(t −1)-prices using the strategy θ for our stock holdings. For ω in A, this
is guaranteed to increase total wealth. At times s > t, we then maintain
all wealth (i.e., our profits from these transactions) in the bond.
The strategy ψ is obviously predictable. To see that it is self-financing,
we need only consider ω ∈A. Then we have
(∆ψt) · St−1 = (θ0
t −Vt−1(θ))S0
t−1 +
d

i=1
θi
tSi
t−1
= θt · St−1 −Vt−1(θ)
= θt−1 · St−1 −Vt−1(θ)
= 0
since S0 ≡1 and θ is self-financing. Hence ψ is also self-financing.
With this strategy, we certainly obtain VT (ψ) ≥0. In fact, for u ≥t
we have
Vu(ψ) = ψt · St = ∆Vt(ψ) = ∆Vt(θ) ≥0
on A and Vu(ψ) = 0 offA. Hence ψ defines a self-financing strategy with
initial value 0 and VT (ψ) ≥0. If there is no arbitrage, we must therefore
conclude that VT (ψ) = 0. Since VT (ψ) = 0 offA and VT (ψ) = ∆Vt(θ) on
A, this is equivalent to
0 = P(VT (ψ) > 0) = P({VT (ψ) > 0} ∩A) = P({∆VT (θ) > 0} |A)P(A),
that is, P(∆Vt = 0 |A) = 1. This proves the first assertion. The proof of
the second part is similar.
The above formulation can be used to establish a further equivalent
form of market model viability. Below we write ˆS for the Rd-valued process
obtained by deleting the 0th component of S, that is; where S = (1, ˆS).
Note. For the statement and proof of the next proposition, we do not need
the assumption that the filtration F = (Ft)t∈T is finitely generated; it is
valid in an arbitrary probability space (Ω, F, P). It states, in essence, the
‘obvious’ fact that if there is an arbitrage opportunity for the model defined
on the time set T = {0, 1, . . . , T}, then there is an arbitrage opportunity
in at least one of the single-period markets [t −1, t).
Proposition 3.3.2. Let (Ω, F, P, T, F, S) be an arbitrary discrete market
model, where (Ω, F, P) is a probability space, T = {0, 1, . . . , T} is a discrete
time set, F = (Ft)t∈T is a complete filtration, and S = (Si)i=0,1,...,d is a
price process, as defined in Section 2.1. The following are equivalent:
(i) The model allows an arbitrage opportunity.

64
CHAPTER 3. THE FIRST FUNDAMENTAL THEOREM
(ii) For some t = 1, 2, . . . , T there is an Ft−1-measurable φ : Ω→Rd+1
such that φ · ∆St ≥0 and P(φ · ∆St > 0) > 0.
(iii) For some t = 1, 2, . . . , T there is an Ft−1-measurable ˆφ : Ω→Rd
such that ˆφ · ∆ˆSt ≥0 and P(ˆφ · ∆ˆSt > 0) > 0.
Proof. The equivalence of (ii) and (iii) is clear. Now assume that (ii) holds
with φ and A = {ω : (φ · ∆St)(ω) > 0}. We can construct an arbitrage
opportunity θ as follows: set
θu(ω) = 0 for all u ∈T and ω /∈A,
while, for ω ∈A,
θu(ω) =
⎧
⎪
⎪
⎨
⎪
⎪
⎩
0
if u < t,

−d
i=1 φi(ω)Si
t−1(ω), φ1(ω), φ2(ω), . . . , φd(ω)
′
if u = t,
(Vt(θ)(ω), 0, . . . , 0)′
if u > t.
By construction, θ is predictable. (The strategy θ is in fact a special case
of ψ constructed in Proposition 3.3.1.) To see that it is also self-financing,
note that the value process V (θ) only changes when ω ∈A, and then
∆Vu(θ) = 0 unless u = t. Moreover,
∆Vt(θ)(ω) = θt · St(ω) −θt−1 · St−1(ω)
= θt · St(ω)
= −
d

i=1
φi(ω)Si
t−1(ω) +
d

i=1
φi(ω)Si(t)(ω)
= θt · ∆St(ω).
Now V0(θ) = 0, while for u > t we have Vu(θ) = 0 on Ω\ A, and, since
S0 ≡1,
Vu(θ) = ∆Vt(θ) = θt · ∆St = φt · ∆St ≥0
on A. Hence VT (θ) ≥0 a.s. (P). By the definition of A,
{VT (θ) > 0} = {∆Vt(θ) > 0} ∩A.
Hence θ is an arbitrage opportunity since P(A) > 0. Thus (ii) implies (i).
Conversely, assume that (i) holds. Then there is a gains process GT (θ)
that is a.s. non-negative and strictly positive with positive probability for
some strategy θ ∈Θ. Assume without loss of generality that (θ · S)0 = 0.
There must be a first index u ≥1 in T such that (θ·S)u is a.s. non-negative
and strictly positive with positive probability. Consider (θ · S)u−1: either
(θ · S)u−1 = 0 a.s. or A = {(θ · S)u−1 < 0} has positive probability.
In the first case,
(θ · S)u = (θ · S)u −(θ · S)u−1 = θu · ∆Su ≥0

3.3. PATHWISE DESCRIPTION
65
since (θu−θu−1)·Su−1 = 0 because θ is self-financing. For the same reason,
P[θu · ∆Su > 0] > 0. Hence (ii) holds.
In the second case, we have
θu · ∆Su = (θ · S)u −(θ · S)u−1 ≥−(θ · S)u−1 > 0
on A, so that the predictable random variable φ = 1Aθu will satisfy (ii).
This completes the proof.
This result shows that the ‘global’ existence of arbitrage is equivalent
to the existence of ‘local’ arbitrage at some t ∈T. To exploit this fact
geometrically, we again concentrate on the special case of finite market
models. First we have the following immediate corollary.
Corollary 3.3.3. If a finite market model is viable, then for all t > 0 in T
and all (non-random) vectors x ∈Rd, we have that x · ∆ˆSt(ω) ≥0 a.s. (P)
implies that x · ∆ˆSt(ω) = 0 a.s. (P).
Geometric Interpretation of Arbitrage
We briefly review two well-known concepts and one basic result concerning
convex sets in Rd.
First, define the relative interior of a subset C in Rd as the interior of
C when viewed as a subset of its affine hull, where the affine hull and the
convex hull of C are defined by
aff(C) =

x ∈Rd : x =
n

i=1
aici, ci ∈C,
n

i=1
ai = 1
&
,
conv(C) =

x ∈Rd : x =
n

i=1
aici, ci ∈C, ai ≥0,
n

i=1
ai = 1
&
.
The relative interior of C is then simply the set
ri(C) = {x ∈aff(C) : Bϵ(x) ∩aff(C) ⊂C for some ϵ > 0} ,
where Bϵ(x) is the Euclidean ϵ-ball centred at x. (See [245] for details.)
It is an easy consequence of the definitions that the existence of a hyper-
plane separating two non-empty convex sets is equivalent to the statement
that their relative interiors are disjoint. For a proof, see [245], p.96.
In the absence of arbitrage, there is no hyperplane in Rd that properly
separates the origin from the convex hull of ˆA =

∆ˆSt(ω) : ω ∈A

for any
given A ∈Pt−1, t > 0. Writing Ct(A) for the convex hull, we have proved
the first part of the following result.
Proposition 3.3.4. In a finite market model, the no-arbitrage condition
is equivalent to the condition that, for all t ∈T and all A ∈Pt−1, the

66
CHAPTER 3. THE FIRST FUNDAMENTAL THEOREM
origin belongs to the relative interior of Ct(A). In other words, the finite
market model allows no arbitrage opportunities if and only if, for each t
and A ∈Pt−1, the value of St−1 is a strictly convex combination of the
values taken by St on A.
Proof. To prove the latter equivalence, suppose that 0 ∈Ct(A).
Since
A ∈Pt−1 and S is adapted, ˆSt−1(ω) = c ∈Rd is constant for ω ∈A.
Any vector in Ct(A) thus takes the form m
i=1 αi(zi −c), where αi > 0,
m
i=1 αi = 1, and each zi is equal to ˆSt(ω) for some ω ∈A. Thus 0 ∈Ct(A)
if and only if c = m
i=1 αizi, where the vectors zi are values of ˆSt on A,
m
i=1 αi = 1, and all αi > 0.
Constructing the EMM
The last result can in turn be interpreted in terms of conditional prob-
abilities.
For each fixed A ∈Pt−1, we can redistribute the conditional
probabilities to ensure that under this new mass distribution (probability
measure) the price increment vector ∆ˆSt has zero conditional expectation
on A. Piecing together these conditional probabilities, we then construct
an equivalent martingale measure for S.
More precisely, fix t, let A = +n
k=1 Ak be a minimal partition of A,
and let M = (aik) be the d × n matrix of the values taken by the price
increments ∆ˆSi
t on the cells Ak. By Proposition 3.3.4, the origin Rd lies
in the relative interior of Ct(A). Hence it can be expressed as a strictly
convex combination of elements of Ct(A).
This means that the equation Mx = 0 has a strictly positive solution
α = (αk) in Rn.
It is intuitively plausible that the coordinates of the vector α should
give rise to an EMM for the discounted prices. To see this, we first need
to derive a useful ‘matrix’ version of the separation theorem, for which we
will also have use in Chapter 4.
Lemma 3.3.5 (Farkas (1902)). If A is a d × n matrix and b ∈Rd, then
exactly one of the following alternatives holds:
(i) There is a non-negative solution x ≥0 of Ax = b.
(ii) The inequalities y′A ≤0 and y · b > 0 have a solution y ∈Rd.
Proof.
The columns aj = (aij) (j ≤n) of A define a convex polyhedral
cone K in Rd, each of whose elements is given in the form k = n
j=1 xjaj
for scalars xj ≥0. Thus Ax = b for some x ≥0 if and only if the vector
b ∈Rd belongs to K. If b /∈K, we can separate it from K by a linear
functional f on Rd such that f(b) > 0, f(k) ≤0 for k ∈K (this is an easy
adaptation of the first part of the proof of Theorem 3.1.1). Now implement
f by f(z) = y·z for some y ∈Rd. Then y·aj ≤0 for j ≤n. Hence y′A ≤0,
and y · b > 0, as required.

3.3. PATHWISE DESCRIPTION
67
The following reformulations of Farkas’ lemma follow without much
difficulty and will be used in the sequel.
Lemma 3.3.6. For a given d × n matrix M, exactly one of the following
holds:
(α) The equation Mx = 0 has a solution x ∈Rn with x > 0.
(β) There exists y ∈Rd such that y′M ≥0, and y′M is not identically 0.
For a given d × n matrix M and b ∈Rd, exactly one of the following holds:
(a) The equation Mx = b has a solution in Rn.
(b) There exists z ∈Rd with z′M = 0 and z · b > 0.
Exercise 3.3.7. Prove Lemma 3.3.6.
Applying the alternatives (α), (β) to the matrix M = (aik), we see
that the existence of a strictly positive solution α = (αk) of the equation
Mx = 0 is what precludes arbitrage: otherwise there would be a θ ∈Rd
with θ′M ≥0 and not identically zero; such a θ would yield an arbitrage
strategy.
We proceed to use the components (αk) of this positive solution to
build a one-step ‘conditional EMM’ for this model, restricting attention
to the fixed set A ∈Pt−1. First denote by AA the σ-field of subsets of
A generated by the cells A1, A2, . . . , An of Pt that partition A, and let
PA be the restriction to AA of the conditional probabilities P(· |A). Now
construct a probability measure QA on the measurable space (A, AA) by
setting
QA(Ak) = αk
|α| for k = 1, 2, . . . , n, where |α| =
n

i=1
αk.
Clearly QA ∼PA. As AA is generated by (Ak)k≤n, any AA-measurable
vector random variable Y : A →Rd takes constant values Y (ω) = yk ∈Rd
on each of the sets Ak. Hence its expectation under QA takes the form
EQA (Y ) =
n

k=1
ykQA(Ak) = 1
|α|
n

k=1
ykαk.
In particular, taking Y = ∆ˆSt yields yk = (aik)i≤d for each k ≤n, where
the aik are the entries of the matrix M defined above, so that 0 = Mα =
n
k=1 ykαk. Thus EQA

∆ˆSt1A

= 0. Since S0 is constant by hypothesis,
it follows that EQA (∆St1A) = 0 (in Rd+1) as well.
Conversely, suppose we are given a probability measure QA on AA with
EQA (∆St1A) = 0. Setting αk = QA(Ak) for k ≤n, the calculation above
shows that Mα = 0, so that the zero vector in Rd can be expressed as a
strictly convex combination of vectors in ct(A) and hence the condition of
Proposition 3.3.4 is satisfied. We have proved the following proposition.

68
CHAPTER 3. THE FIRST FUNDAMENTAL THEOREM
Proposition 3.3.8. For a finitely generated filtration F, the following are
equivalent:
(i) For all t > 0 and A ∈Pt−1, the zero vector in Rd can be ex-
pressed as a strictly convex combination of vectors in the set ct(A) =

∆ˆSt(ω) : ω ∈A

.
(ii) For all t > 0 in T and all Ft−1-measurable random vectors x ∈Rd,
we have that x · ∆ˆSt ≥0 a.s. (P) implies that x · ∆ˆSt = 0 a.s. (P).
(iii) There exists a probability measure QA ∼PA on (A, AA) satisfying
EQA (∆St1A) = 0.
Finally, we can put it all together to obtain three conditions, each de-
scribing the viability of the market model. Note, in particular, that con-
dition (ii) is not affected by an equivalent change of measure. However,
our proof of the steps described in Proposition 3.3.8 crucially used the fact
that the filtration F was taken to be finitely generated.
Theorem 3.3.9. The following statements are equivalent:
(i) The securities market model (Ω, F, P, T, F, S) is viable.
(ii) For all t > 0 in T and all Ft−1-measurable random vectors x ∈Rd,
we have that x · ∆ˆSt ≥0 a.s. (P) implies that x · ∆ˆSt = 0 a.s. (P).
(iii) There exists an equivalent martingale measure Q for S.
Proof. That (i) implies (ii) was shown in Corollary 3.3.3, and that (iii)
implies (i) was shown in Section 2.4. This leaves the proof that (ii) implies
(iii), in which we make repeated use of Proposition 3.3.8. The family
{PA : A ∈Pt, t < T}
determines P since all the σ-fields being considered are finitely generated.
Thus for each ω ∈Ωwe can find a unique sequence of sets (Bt)t∈T with
Bt ∈Pt for each t < T and such that
Ω= B0 ⊃B1 ⊃B2 ⊃· · · ⊃BT .
By the law of total probability, we can write
P({ω}) = PB0(B1)PB1(B2) · · · PBT −1({ω}).
Now, if (ii) holds, we can use Proposition 3.3.8 successively with t = 1 and
A ∈P0 to construct a probability measure QA and then repeat for t = 2
and sets in Pt, etc. In particular, this yields probability measures QBt for
each t < T, defined as in the discussion following Lemma 3.3.6. Setting
Q({ω}) = QB0(B1)QB1(B2) · · · QBT −1({ω}),

3.4. EXAMPLES
69
we obtain a probability measure Q ∼P on the whole of (Ω, F). For any
fixed t > 0 and A ∈Pt−1, the conditional probability is just
Q({ω} |A) = 1A({ω})QA(Bt)QBt(Bt+1) · · · QBT −1({ω}).
Therefore, for ω ∈A, EQ (∆St |Ft−1 ) (ω) = 0, and thus Q is an equivalent
martingale measure for S.
3.4
Examples
Example 3.4.1. The following binomial tree example, which is adapted
from [241], illustrates the stepwise construction of the EMM and also shows
how viability of the market can break down even in very simple cases.
Let Ω= {ω1, ω2, ω3, ω4} and T = 2. Suppose that the evolution of a
stock price S1 is given as
S1
0 = 5,
S1
1 = 8 on {ω1, ω2} ,
S1
2 = 9 on {ω1} ,
S1
1 = 4 on {ω3, ω4} ,
S1
2 = 6 on {ω2, ω3} ,
S1
2 = 3 on {ω4} .
Note that F0 = {∅, Ω} and that the partition Pt−1 = {ω1, ω2} ∪{ω3, ω4}
generates the algebra F1 = {∅, {ω1, ω2} , {ω3, ω4} , Ω} , while F2 = P(Ω).
Although the stock price S1
2 is the same in states ω2 and ω3, the histories
(i.e., paths) of the price process allow us to distinguish between them. Hence
the investor knows by time 2 exactly which state ωi has been realised. For
the present we shall take S0 ≡1 (i.e., the discount rate r = 0).
To find an EMM Q = {q1, q2, q3, q4} directly, we need to solve the
equations EQ

S1
u |Ft

= S1
t for all t and u > t. This leads to the following
equations:
t = 0, u = 1 :
5 = 8(q1 + q2) + 4(q3 + q4),
t = 0, u = 2 :
5 = 9q1 + 6(q2 + q3) + 3q4,
t = u = 1, S1
1 = 8 :
8 =
1
q1 + q2
(9q1 + 6q2),
t = u = 1, S1
1 = 4 :
4 =
1
q3 + q4
(6q3 + 3q4).
⎫
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎬
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎭
(3.3)
Solving any three of these (dependent) equations together with 4
i=1 qi = 1
yields the unique solution
q1 = 1
6,
q2 = 1
12,
q3 = 1
4,
q4 = 1
2.
(3.4)
On the other hand, it is simpler to construct qi step-by-step, as indicated
in the previous section. Here this means that we must calculate the one-
step conditional probabilities at each node of the tree for t = 0 and t = 1.
When S1
0 = 5, this requires 5 = 8p + 4(1 −p); i.e., p = 1
4.

70
CHAPTER 3. THE FIRST FUNDAMENTAL THEOREM
(1,11,9)
(1,11,10)
(1,8,11)
1/3
1/3
1/3
5/20
4/20
11/20
1/2
1/2
1/7
2/7
4/7
(1,10,13)
(1,10,8)
(1,12,11)
(1,10,9)
(1,12,5)
(1,10,14)
(1,14,8)
(1,6,11)
A
A
A
A
A
A
A
A
11
12
13
21
22
31
32
33
5/60
4/60
1/6
1/6
1/21
2/21
4/21
11/60
Q
(1,10,10)
Figure 3.1: Event tree for two-stock model
For S1
1 = 8 we solve 8 = 9p′ + 6(1 −p′), (i.e., p′ = 2
3,) while for S1
1 = 4
we need 4 = 6p′′ + 3(1 −p′′), (i.e., p′′ =
1
3.) According to the proof of
Theorem 3.3.9, this yields the qi as
q1 = 1
4 · 2
3,
q2 = 1
4 · 1
3,
q3 = 3
4 · 1
3,
q4 = 3
4 · 2
3.
This agrees with the values in (3.4).
It is instructive to examine the effect of discounting on this example.
Suppose instead that S0(t) = (1 + r)t for each t, with r ≥0. The left-hand
sides of the equations (3.3) then become 5(1 + r), 5(1 + r)2, 8(1 + r), and
4(1 + r), respectively.
This yields the solution for the qi (using the one-step method, greatly
simplifying the calculation) as
q1 = 1 + 5r
4
2 + 8r
3
,
q3 = 3 −5r
4
1 + 4r
3
,
q2 = 1 + 5r
4
1 −8r
3
,
q4 = 3 −5r
4
2 −4r
3
.
⎫
⎪
⎬
⎪
⎭
(3.5)

3.5 GENERAL DISCRETE MODELS
71
Exercise 3.4.2. Verify the solutions given in (3.5).
This time the requirement that Q be a probability measure is not au-
tomatically satisfied: when r ≥1
8, q2 becomes non-positive. Hence Q is
an EMM for S = (S0, S1) only if 0 ≤r < 1
8 (i.e., if the riskless interest
rate is less than 12.5%). If r ≥1
8, there is no EMM for this process, and
if we observe S1
1 = 8, an arbitrage opportunity can be constructed since
we know in advance that the discounted stock price S
1
2 will be lower than
S
1
1 =
8
1+r in each of the states ω1 and ω2.
Example 3.4.3. Consider a pricing model with two stocks S1, S2 and a
riskless bond S0 with tree structure as shown in Figure 3.1. This example
is taken from [301].
The partitions giving the filtration F begin with P0 as the trivial par-
tition and continue with
P1 = {A1, A2, A3} ,
P2 = {A11, A12, A13, A21, A22, A31, A32, A33} .
We take T = 2, and the various probabilities are as shown in Figure 3.1.
(Note that we again keep S0 ≡1 here.) Note that in each case the one-step
transition includes both ‘up’ and ‘down’ steps, so that by Theorem 3.3.9
the model is viable and an EMM Q can be constructed for S = (S0, S1, S2).
The calculation of Q proceeds as in the previous example (using the one-
step probabilities), so that for example Q(A13) = pq, where p is found by
solving the equations
10 = 11p + 11p′ + 8(1 −p −p′),
10 = 9p + 10p′ + 11(1 −p −p′),
which yields p = 1
3, while q must satisfy
11 = 10q + 10q′ + 14(1 −q −q′),
9 = 8q + 13q′ + 8(1 −q −q′).
This yields q = 11
20; hence Q(A13) = 11
60.
Exercise 3.4.4. Find the values of Q(A) for all A ∈P.
To use the measure Q to calculate the price of a European call option
C on stock S2 with strike price 10, we simply find the time 0 value of C as
EQ (C) = 0· 5
60 + 3· 4
60 + 0·11
60 + 1·1
6 + 0·1
6 + 0· 1
21 + 4· 2
21 + 1· 4
21 = 197
210.
3.5
General Discrete Models
We now turn to the construction of equivalent martingale measures for
discrete market models where the underlying probability space (Ω, F, P)
is not necessarily finitely generated. This question has been studied inten-
sively in recent years, both in the discrete- and continuous-time settings.

72
CHAPTER 3. THE FIRST FUNDAMENTAL THEOREM
The extension from finite market models to the general case proves to be
surprisingly delicate, and several different approaches have been developed
since the first proof of the result by Dalang, Morton, and Willinger [68]-
the interested reader should compare the expositions in [281] and [76]. We
mainly follow the development in [132], which is based in turn on recent
expositions in [262] and [181].
The importance of the first fundamental theorem should be clear: it
provides the vital link between the economically meaningful assumption of
the absence of arbitrage and the mathematical concept of the existence of
equivalent measures under which the discounted stock prices are martin-
gales. In generalising from the relatively simple context of finite market
models, one wishes to maintain the essential aspects of the equivalence
of these two conditions. In the continuous-time setting, however, the two
conditions are no longer equivalent and much work has gone into reformu-
lations that reflect the requirement that the market should be ‘essentially’
arbitrage-free while seeking to maintain a close link with the existence of
equivalent martingale measures.
The general discrete-time result can be stated in the following form,
which is close to that of the original paper [68].
Theorem 3.5.1 (First Fundamental Theorem of Asset Pricing).
Let
(Ω, F, P) be a probability space, and set T = {0, 1, . . . , T} for some
natural number T. Let F = (Ft)t∈T be filtration, with F0 consisting of all
P-null sets and their complements, and suppose the Rd+1 -valued process
S = (Si
t : 0 ≤i ≤d, t ∈T) is adapted to F, with S0
t > 0 a.s. (P) for each t
in T. The following are equivalent:
(i) There is a probability measure Q ∼P such that the discounted price
process S/S0 is a (Q, F)-martingale.
(ii) The market model (Ω, F, P, T, F, S) allows no arbitrage opportunities.
If either (i) or (ii) holds, then the measure Q can be chosen with bounded
density dQ
dP relative to P.
As we have seen for finite market models, in a model with an equivalent
martingale measure (i.e., when (i) holds), it is straightforward to prove the
absence of arbitrage, and this has already been proved in Chapter 2 without
any restrictions on (Ω, F, P). Moreover, for finite market models, the task of
showing that (ii) implies (i) was broken into a sequence of steps that allowed
us to consider a multi-period model as a finite sequence of single-period
models, where the EMM is constructed by piecing together a succession
of conditional probabilities (see the steps leading to Theorem 3.3.9). The
principal difficulty in extending this approach to general probability spaces,
where the corresponding function spaces can no longer be identified with
Rn for some finite n, lies in obtaining a formulation in the single-period
case that allows one to avoid subtle questions of measurable selection while
applying appropriate versions of the Hahn-Banach separation theorem to
find the required one-step densities.

3.5 GENERAL DISCRETE MODELS
73
No-arbitrage in a Randomised
Single-Period Model
For the inductive procedure, we shall need to move from single-period to
multi-period models, and it will not suffice to consider single-period models
where the initial prices are given positive constants. We therefore need to
find one-step martingale measures when the initial prices are themselves
random. For this, we make the following modelling assumptions.
First, we remove, until further notice, the restriction on F0 stated in the
theorem and instead assume as given an arbitrary σ-field F0 ⊂F. Let S0 =
(S0
0, S1
0, . . . , Sd
0) : Ω→Rd be an F0-measurable random vector representing
the bond and stock prices in a single-period market model at time 0. The
prices at time 1 are given by the F-measurable non-negative random vector
S1 = (S0
1, S1
1, . . . , Sd
1), so that the price process S = (S0
t , S1
t , . . . , Sd
t )t=0,1
is adapted to the filtration (F0, F1), where we take F1 = F. We take S0 as
numeraire; i.e., we assume that
P(S0
t > 0) = 1 for t = 0, 1.
The discounted price increment, omitting the 0th coordinate (which is
zero), is, as before, the Rd-random vector ∆,S = (∆,Si)1≤i≤d, where
∆,Si = Si
1
S0
1
−Si
0
S0
0
for 1 ≤i ≤d.
(3.6)
The condition that this market model does not admit an arbitrage op-
portunity can then be stated as follows: the one-step pricing model is viable
(also called arbitrage-free) if for every vector θ in Rd we have P-a.s. that
,θ · ∆,S ≥0 implies ,θ · ∆,S = 0.
(3.7)
Note that this requirement involves only the null sets of the given measure
and hence is invariant under an equivalent change of measure. Moreover,
since we assume that all prices are non-negative, ∆,Si is bounded below by
−Si
0
S0
0 , and thus EQ

∆,S |F0

is well-defined for any probability measure
Q ∼P.
The ‘martingale property’ in the single-period model reduces to the
requirement that
EQ
Si
1
S0
1
|F0

= Si
0
S0
0
a.s. (Q) for 1 ≤i ≤d,
so that we need to find an equivalent measure Q such that
EQ

∆,S |F0

= 0 a.s. (Q) .

74
CHAPTER 3. THE FIRST FUNDAMENTAL THEOREM
Notation 3.5.2. Write M1(Ω, F) for the space of all probability measures
on (Ω, F), and define
P =

Q : Q ∈M1(Ω, F), Q ∼P and EQ

∆,S |F0

= 0 a.s. (Q)

and
Pb =
$
Q ∈P, dQ
dP is bounded
%
.
We call elements of P equivalent martingale measures for the model.
We wish to analyse the geometric properties of the set of discounted
gains processes arising from admissible trading strategies.
By (2.8), we
know that such strategies are generated by predictable Rd-valued processes
,θ, so that in the single-period model we need to consider elements of the
space L0(Rd) = L0(Ω, F0, P; Rd) of all a.s. (P)-finite F0-measurable ran-
dom vectors
,θ =

θ1, θ2, . . . , θd
.
We then define the linear space of inner products,
K =

,θ · ∆,S : ,θ ∈L0(Ω, F0, P; Rd)

,
(3.8)
which is a subspace of L0 = L0(Ω, F0, P; R).
We can now rewrite the
no-arbitrage condition (3.7) as
K ∩L0
+ = {0} ,
(3.9)
where L0
+ is the convex cone of non-negative elements of L0. (The cones
Lp
+ are defined similarly for the Lebesgue spaces Lp = Lp(Ω, F, P; R) with
1 ≤p ≤∞.) We also introduce the convex cone
C = K−L0
+ =

Y = ,θ · ∆,S −U : ,θ ∈L0(Ω, F0, P; Rd), U ∈L0
+(Ω, F, P)

.
Lemma 3.5.3. C ∩L0
+ = {0} if and only if K ∩L0
+ = {0} .
Proof. The first statement is clearly necessary for the second. On the other
hand, if the second statement holds and Z is an element of C ∩L0
+, we can
find U ∈L0
+ and ,θ ∈L0 such that Z = ,θ · ∆,S −U ≥0 a.s. (P).
In
particular, ,θ · ∆,S ≥0 a.s. (P) and so is an element of K ∩L0
+ and hence
equals 0. This forces U = 0; thus Z = 0 a.s. (P), so that the two statements
are equivalent.
Having reformulated the no-arbitrage condition, we restate the principal
objective of this section as follows.
Theorem 3.5.4. With the above definitions for the single-period model,
the following are equivalent:

3.5 GENERAL DISCRETE MODELS
75
(i) K ∩L0
+ = {0},
(ii) C ∩L0
+ = {0},
(iii) Pb ̸= ∅,
(iv) P ̸= ∅.
The equivalence of (i) and (ii) was proved in Lemma 3.5.3. Trivially,
(iii) implies (iv), and the following lemma shows that (iv) implies (i).
Lemma 3.5.5. If P is non-empty, then K ∩L0
+ = {0} .
Proof. Let Q ∈P, and suppose that ,θ ∈L0(Rd) has ,θ · ∆,S ∈K ∩L0
+.
Since ,θ is a.s. finite, we can approximate it pointwise by truncation; i.e.,
,θn = ,θ1{|θ|<n} increases to ,θ. If ,θ · ∆,S > 0 on a set of positive P-measure,
the same must be true for ,θn · ∆,S if n is chosen sufficiently large. Now
EQ

,θn · ∆,S

is well-defined, but since Q ∈P we have
EQ

,θn · ∆,S

= EQ

,θn · EQ

∆,S |F0

= 0.
This contradicts the claim that ,θn ·∆,S is non-zero and in L0
+. So K∩L0
+ =
{0} .
Remark 3.5.6. In order to complete the proof of the fundamental theorem
for this single-period model, it remains to show that (ii) implies (iii) in
Theorem 3.5.4 (i.e., that the reformulated no-arbitrage condition C ∩L0
+ =
{0} implies the existence of an EMM with bounded density). To do this,
it will be advantageous to assume that
EP
 Si
t
S0
t

< ∞for i = 0, 1, . . . , d and t = 0, 1.
In fact, we can make this assumption without loss of generality since the
statement C ∩L0
+ = {0} is invariant under equivalent changes of measure.
We therefore assume that it holds for the measure P1 whose density relative
to P is given by
dP1
dP =
c
1 + d
i=0

Si
0
S0
0 + Si
1
S0
1
,
where c is a normalising constant chosen to make P1 a probability measure.
Clearly the P1-expectations of the discounted prices are finite. If we find
a probability measure Q with EQ

∆,S |F0

= 0 and
dQ
dP1 bounded, then
dQ
dP =
dQ
dP1
dP1
dP
is bounded, so that Q ∈Pb. Henceforth we shall assume
without further mention that the discounted prices are P-integrable.


## Complete Markets

76
CHAPTER 3. THE FIRST FUNDAMENTAL THEOREM
We show in several steps that (ii) implies (iii), initially by adding a
further assumption on the cone C, as described below.
The following proposition presents a basic fact about the behaviour of
conditional expectations under equivalent measure changes. We shall need
it several times in this chapter, as well as in Chapter 9.
Proposition 3.5.7 (Bayes’ Rule). Given probability measures P, Q with
Q ≪P on the measurable space (Ω, F), a sub-σ-field G of F and a random
variable Y ≥0 integrable with respect to both measures, we have the identity
EQ (Y |G ) =
EP

Y dQ
dP |G

EP

dQ
dP |G

a.s. (Q) .
(3.10)
Proof. Let Q ≪P have Radon-Nikodym derivative dQ
dP = Z. Then Q(Z >
0) = 1 since, for any A ∈F,
Q(A) =

A
ZdP =

A∩{Z>0}
ZdP = Q(A ∩{Z > 0}).
As G ⊂F, the density
dQ
dP
'''
G equals EP (Z |G ) since
Q(G) =

G
ZdP =

G
EP (Z |G ) dP for all G ∈G.
For the F-measurable random variable Y ≥0, let
W =
 EP (Y Z|G )
EP (Z|G )
if EP (Z |G ) > 0,
0
if EP (Z |G ) = 0.
By the above, the latter occurs only on a Q-null set.
To prove that W = EQ (Y |G ), we must verify that EQ (1GW) =
EQ (1GY ) for all G ∈G. But this follows from
EQ (1GW) = EP (1GWZ)
= EP (EP (1GWZ |G ))
= EP (1GWEP (Z |G ))
= EP (1GEP (Y Z |G ))
= EP (EP (1GY Z) |G )
= EP (1GY Z)
= EQ (1GY ) .
The role of the convex cone C is clarified in the following general theorem
about convex cones in L1. We use separation arguments in the Banach
space L1 to provide a normalised element of the dual space L∞, which will
act as the bounded density of the martingale measure we wish to construct.

3.5 GENERAL DISCRETE MODELS
77
Theorem 3.5.8 (Kreps-Yan). Let C be a closed convex cone in L1 con-
taining the negative essentially bounded functions (i.e., C ⊃−L∞
+ ) and such
that C ∩L1
+ = {0} . Then there exists Z ∈L∞such that Z > 0 a.s. (P) and
EP (Y Z) ≤0 for all Y ∈C.
Proof. The separation theorem we need is the analogue of the separating
hyperplane theorem (Theorem 3.1.1) and follows from the Hahn-Banach
theorem (see, e.g. , [264, Theorem I.9.2]): given a closed convex cone C
disjoint from a compact set K in a Banach space B, we can find a con-
tinuous linear functional f in the dual space B∗and reals α, β such that
f(c) ≤α < β < f(k) for all c ∈C, k ∈K.
Applying this to the convex cone C and the compact set {U}, where
0 ̸= U ∈L1
+, we find f ∈(L1)∗, with f(X) = EP (XZ) if X ∈L1, so that
Z ∈L∞implements f. Thus, for all Y ∈C,
EP (Y Z) ≤α < β < EP (UZ) for some α, β.
Since C contains 0, we must have α ≥0, and as C is a cone and EP (Y Z) ≤α
for all Y ∈C, it follows that α = 0 (Y ∈C implies λY ∈C for all λ ≥0,
so if EP (Y Z) > 0 for some Y in C, EP (λY Z) = λEP (Y Z) cannot be
bounded above as λ →∞). On the other hand, EP (−XZ) ≤0 holds for
all X ∈L∞
+ since C contains −L∞
+ . Apply this with X = 1{Z<0}, so that
EP (Z−) ≤0; hence Z ≥0 a.s. (P).
As EP (UZ) > β > 0, it follows that P(Z > 0) > 0. Note that we can
replace Z by
Z
|Z|∞so that we can assume without loss of generality from
now on that 0 ≤Z ≤1. Hence we have shown that for each non-zero
U ∈L1
+ there exists a ZU ∈L∞with 0 ≤ZU ≤1, P(ZU > 0) > 0, and
EP (Y ZU) ≤0 for all Y ∈C, but EP (UZU) > 0.
However, the claim is that we can find some Z > 0 a.s. (P) with these
properties. To construct it, we employ an exhaustion argument. First let
∞
k=1 αk = 1, αk ≥0, and define
Z =
∞

k=1
αkZUk,
where each Uk ∈L1
+ and ZUk is as constructed above. Then, for Y ∈C,
∞
k=1 |αkZUkY | ≤|Y | shows that EP (n
k=1 αkZUkY ) is bounded above
in L1. Therefore, by dominated convergence, we have
EP (Y Z) =
∞

k=1
αkEP (Y ZUk) ≤0.
Now let
c = sup
ZU∈D
P(ZU > 0),
where
D = {ZU ∈L∞: 0 ≤ZU ≤1, P(ZU > 0) > 0; EP (Y ZU) ≤0 if Y ∈C} .

78
CHAPTER 3. THE FIRST FUNDAMENTAL THEOREM
Choose a sequence (ZUk) in D such that P(ZUk > 0) →c as k →∞. The
countably convex combination Z = ∞
k=1
1
2k ZUk satisfies EP (Y Z) ≤0
for all Y in C by the above argument and hence is in D, and {Z > 0} =
∪∞
k=1 {ZUk > 0} . It follows that P(Z > 0) = c, and it remains to show that
c = 1.
If c < 1, the set A = {Z = 0} would have P(A) > 0. Then U =
1A ∈L1
+, U ̸= 0, and so EP (UZU) > 0. This would mean that P[A ∩
{ZU > 0}] > 0 and hence the function W = 1
2(Z + ZU) ∈D would have
P(W > 0) > P(Z > 0) = c, contradicting the definition of c.
As required, we have found Z ∈L∞with EP (Y Z) ≤0 for all Y in C
and Z > 0 a.s. (P).
Applying this to the cone C = K −L0
+, we can now prove the following
result.
Proposition 3.5.9. If C ∩L0
+ = {0} and C ∩L1 is closed in L1, then there
is a probability measure Q ∼P with bounded density relative to P such that
EQ

∆,S |F0

= 0 a.s. (Q).
Proof. The L1-closed cone C ∩L1contains −L∞
+ since 0 ∈K∩L1. Hence the
Kreps-Yan theorem provides a Z ∈L∞with Z > 0 a.s. (P) and EP (Y Z) ≤
0 for all Y in C. Since K ∩L1 is a linear space, α(,θ · ∆,S) lies in K ∩L1 and
hence in C ∩L1 (recall Remark 3.5.6) for any α ∈R and ,θ in L∞(F0, Rd).
It follows that EP

Z(,θ · ∆,S)

= 0 for all choices of ,θ. But then
EP

,θ · EP

Z∆,S |F0

= EP

Z(,θ · ∆,S)

= 0
for all ,θ ∈L∞(F0; Rd), so that EP

Z∆,S |F0

= 0 a.s. (P). Now apply
the conditional Bayes rule (3.10) so that, setting dQ
dP =
Z
EP (Z), we finally
obtain
EQ

∆,S |F0

=
EP

Z∆,S |F0

EP (Z |F0 )
= 0 a.s. (Q) .
(3.11)
Hence Q is an EMM for the single-period model.
We have now proved Theorem 3.5.4 under the additional assumption
that the cone C∩L1 is closed in the L1-norm. The removal of this additional
assumption requires a more subtle analysis, which is presented in the next
section.
The reader may prefer to omit this on a first reading and go
directly to the proof of the fundamental theorem in a multi-period setting,
which, with the above preparation, now only requires a careful backward
induction procedure.

3.5 GENERAL DISCRETE MODELS
79
Closed Subsets of L0
We saw that, to reformulate the no-arbitrage condition in geometric terms,
we need to deal with the larger space L0, which does not have the conve-
nience of a norm topology. Indeed, the appropriate topology in L0 is that
of convergence in probability.
Definition 3.5.10. The random variables (Xn) in L0(Ω, F, P; Rd) (d ≥1)
converge in probability to a random variable X if
lim
n→∞P(|Xn −X|d > ε) = 0 for all ε > 0.
Here |·|d denotes the Euclidean norm in Rd.
This convergence concept for Rd-valued random vectors can of course
also be defined in terms of their coordinate random variables. The topology
on L0(Ω, F, P; R) is induced by the metric
d(X, Y ) = EP

|X −Y |
1 + |X −Y |

,
so that with the resulting topology, L0(Ω, F, P; Rd) is metrisable and the
above definition suffices to describe convergence in this topology for each
coordinate. It is elementary that convergence in the Lp-norm for any p ≥1
implies convergence in probability. Moreover, a.s. (P)-convergence implies
convergence in probability, and if Xn →X in probability, then some sub-
sequence (Xnk)k≥1 converges to X a.s. (P).
Our principal source of relevant information on sets in L0(F0; Rd) are
the ,θ ∈L0(F0; Rd), which give rise to discounted gains processes whose
conditional expectation relative to F0 vanishes a.s. (P). It is thus natural
to fix vectors in Rd whose values are a.s. (P) orthogonal to the discounted
price increments.
Write
N =

φ ∈L0(F0; Rd) : φ · ∆,S = 0 a.s. (P)

,
N ⊥=

ψ ∈L0(F0; Rd) : φ · ψ = 0 a.s. (P) for all φ ∈N

.
It is of course by no means clear at this stage that the notation N ⊥signifies
any ‘orthogonality’ in the function space L0(F0; Rd): we show below how
this notation will be justified. First we note some simple properties of the
linear subspaces N and N ⊥.
Lemma 3.5.11. N and N ⊥are closed subspaces of L0(F0; Rd), and are
closed under multiplication by functions in L0(F0; R). Moreover, N∩N ⊥=
{0} .
Proof. If (φn) in N converges in probability to φ ∈L0(F0; Rd) then some
subsequence (φnk) converges to φ a.s. (P). Hence

φ · ∆,S

(ω) = lim
k

φnk · ∆,S

(ω) = 0 a.s. (P) ,

80
CHAPTER 3. THE FIRST FUNDAMENTAL THEOREM
so that φ ∈N. Hence N is closed in L0(F0; Rd). An identical proof shows
that N ⊥is also closed.
Next, let h : Ω→R be F0-measurable and finite a.s. (P). Then

(hφ) · ∆,S

(ω) = h(ω)

φ · ∆,S

(ω) = 0 a.s. (P) for all φ ∈N,
so that hφ ∈N. Similarly, for ψ in N ⊥, ((hψ) · φ) = h(ψ · φ) = 0 for all
φ ∈N.
Finally, if φ ∈N ∩N ⊥, we have (φ·φ)(ω) = |φ(ω)|2
d = 0 a.s. (P). Hence
N ∩N ⊥= {0} as subspaces of L0(F0; Rd).
The next result provides the ‘orthogonal decomposition’ of L0(F0; Rd)
indicated by the notation.
Proposition 3.5.12. Every φ ∈L0(F0; Rd) can be decomposed uniquely
as φ = P1φ + P2φ, where P1φ ∈N, P2φ ∈N ⊥.
Proof. We prove this first for the constant functions ω →ei, where the (ei)
form the standard ordered basis of Rd. Any element of L0(F0; Rd) can be
written in the form φ = d
i= φiei, where the coordinate functions (φi) are
F0-measurable real random variables.
Fix i ≤d, and by a minor abuse of notation write ei for the constant
function with this value. As a bounded function, ei is in the Hilbert space
H = L2(F0; Rd), and H1 = N ∩H and H2 = N ⊥∩H are linear subspaces
of H. Both are closed in H since L2-convergence implies convergence in
probability. Hence the projection maps Pi : H →Hi (i = 1, 2) are well-
defined. Consider the element ψ = ei −P1ei. To show that H2 = H⊥
1 , we
need only prove that ψ ∈N ⊥, which implies that ψ = P2ei. If ψ is not in
N ⊥, we can find φ ∈N such that the inner product (φ · ψ)(ω) > 0 on a set
A ∈F0 with P(A) > 0. Since it is possible that EP (φ · ψ) is infinite, we
consider the truncations
φn(ω) =

φ(ω)1{|φ|≤n}
if ω ∈A,
0
if ω /∈A.
Then each EP (φn · ψ) is finite, and we have (φn, ψ)H = EP (φn · ψ) > 0 for
large enough n, where (·, ·)H is the inner product in H. As φn ∈H1 = N∩H,
this would contradict the construction of ψ as a vector orthogonal to H1
in H, so ψ ∈N ⊥.
This completes the decomposition of ei. Since ei = P1ei + P2ei for
each i ≤d, with P1ei ∈N ∩H, P2ei ∈N ⊥∩H, is a unique decomposi-
tion, we can now write (P1φ)(ω) = d
i=1 φi(ω)(P1ei)(ω) and (P2φ)(ω) =
d
i=1 φi(ω)(P2ei)(ω) for each ω ∈Ω. The function P1φ is in N and P2φ
is in N ⊥by Lemma 3.5.11, which also confirms that the decomposition is
unique.

3.5 GENERAL DISCRETE MODELS
81
The final lemma we need provides a measurable way of selecting a con-
vergent subsequence from a given sequence in L0(F0; Rd). This is achieved
by a diagonal argument on the components of the random vectors.
Lemma 3.5.13. If (fn)n≥1 is a sequence in L0(F0; Rd) with lim infn |fn|
finite, then there is an element f in L0(F0; Rd) and a strictly increasing
sequence (τn) of F0-measurable random variables taking their values in N
such that fτn(ω)(ω) →f(ω) for P-almost all ω ∈Ω.
Proof. Write F(ω) = lim infn |fn(ω)|d , where |·|d is again the Euclidean
norm in Rd. On the P-null set B = {F = ∞}, we set τm = m for each m.
For ω in Bc we define τm inductively. First set
σ0
m(ω) =

1
if m = 1,
min

n > σ0
m−1(ω) : ||fn(ω)| −F(ω)|d ≤1
m

if m ≥2.
The first component f 1 of f is now taken as
f 1(ω) = lim inf
m→∞f 1
σ0
m(ω)(ω),
(3.12)
and at the same time we define a subsequence of random indices (σ1
m)m≥1
by using this ‘limit value’ in the construction: let σ1
1(ω) = 1, and for m ≥2
define
σ1
m(ω) = min
$
σ0
n : σ0
n(ω) > σ1
m−1(ω) and
'''f 1
σ0
n−1(ω)(ω) −f 1(ω)
''' ≤1
m
%
.
Continue this inductively for i = 2, 3, . . . , d, finding the second coordi-
nate of the limit function at the next step and simultaneously constructing
a subsequence (σ2
m) of

σ1
m

that leads to the next coordinate of f. Fi-
nally, let τm = σd
m for each m ≥1. It is clear from the construction that
'''f i
τm(ω)(ω) −f i(ω)
''' ≤1
m for each i ≤d and that (τm) is strictly increasing,
and each τm is F0-measurable by construction.
We are now ready for the final step in the proof of Theorem 3.5.4.
Proposition 3.5.14. If K ∩L0
+ = {0}, then C = K −L0
+ is closed in L0.
Proof. Let (Yn) be a sequence in C converging to Y ∈L0 as n →∞. There
is a subsequence converging to Y
a.s. (P), so we can assume without loss
of generality that Yn →Y a.s. (P). Write Yn = ψn · ∆,S −Un for some
Un ∈L0
+ and ψn ∈N ⊥since by Proposition 3.5.12 any θ ∈L0(F0; Rd) can
be decomposed uniquely as θ = φ + ψ with φ ∈N and ψ ∈N ⊥, and then
φ · ∆,S = 0 so θ · ∆,S = ψ · ∆,S.
Define αn = (1 + |ψn|d)−1 and set fn = αnψn. Extend this to a ‘port-
folio’ Fn = (αn, fn) in L0(F0, Rd+1) and note that |Fn| ≤2, so that we can
apply Lemma 3.5.13 to provide F0-measurable random variables with val-
ues τ1 < τ2 < · · · < τn < · · · in N and a function F ∈L∞(F0, Rd+1) such

82
CHAPTER 3. THE FIRST FUNDAMENTAL THEOREM
that Fτn →F P-almost surely. Since the convergence holds coordinate-
wise, we can write F = (α, f) and then ατn →α and fτn →f.
We show that fτn ∈N ⊥for each n. For this, let φ ∈N be given. Then
(φ · fτn)(ω) =
∞

k=1
αk (ω) 1{τn(ω)=k}(ω)(φ · ψk)(ω) = 0 a.s. (P)
since each ψk ∈N ⊥. Since N ⊥is closed in L0(F0; Rd), it follows that
f ∈N ⊥.
Now consider the set A = {α = 0} . We claim that P(A) = 0.
To
see this, note that since Yn →Y a.s. and ατn →α a.s. it follows that
ατnYτn = fτn ·∆,S −ατnUτn converges a.s. (P). On A the limit is obviously
0. But fτn · ∆,S →f · ∆,S a.s. (P), so we have proved that
1AατnUτn →1Af · ∆,S a.s. (P) .
Now each element on the left-hand side is non-negative and hence so is
their limit. By the no-arbitrage condition K ∩L0
+ = {0}, it follows that
(1Af) · ∆,S = 0. Since f ∈N ⊥, the same is true of 1Af, which therefore
belongs to N ∩N ⊥= {0} .
Thus f = 0 a.s. (P) on A. This forces P(A) = 0. To see this, note that
by definition, ατn(ω)(ω) →0 means that
(
''ψτn(ω)(ω)
''
d)n is unbounded
above. Hence
|ψτn|
1 + |ψτn| →1,
so that
1A |f| = 1A lim
n |ατnψτn| = 1A lim
n
|ψτn|
1 + |ψτn| = 1A.
(3.13)
In other words, |f| = 1 a.s. (P) on A, which is impossible unless P(A) = 0.
We therefore need only examine the convergence of (ψτn)n on Ac =
{α > 0} since this set has full P-measure. By construction, we have
ατn(ω)(ω) > 0 a.s. (P) .
Hence, as P(A) = 0,
1
αf = lim
n
1
ατn
fτn = lim
n ψτn a.s. (P) .
(3.14)
Thus, as Un ≥0 for all n, we have
Y = lim
n Yn = lim
n Yτn ≤lim
n (ψτn · ∆,S) = 1
αf · ∆,S a.s. (P) .
(3.15)
Thus Y has the form φ · ∆,S −U for some U ∈L0
+, so that Y ∈C as
required. This completes the proof.
Remark 3.5.15. Note that we have equality in (3.15) if Yn = ψn · ∆,S for
all n. Therefore, if all Yn are in K, then so is their L0-limit Y. Hence we
have also shown that if K ∩L0
+ = {0}, then K is closed in L0.

3.5 GENERAL DISCRETE MODELS
83
The Fundamental Theorem for a Multi-period Model
Having completed the construction of the EMM for a general single-period
model with random initial prices, we can finally return to a multi-period
setting to complete the proof of Theorem 3.5.1. We take as given a prob-
ability space (Ω, F, P) and a time set T = {0, 1, . . . , T} for some natural
number T. We also reinstate the condition on F0 as in the theorem: let
F = (Ft)t∈T be a filtration with F0 consisting of all P-null sets and their
complements. Suppose the Rd+1-valued process S = (Si
t : 0 ≤i ≤d, t ∈T)
is adapted to F, with S0
t > 0 a.s. (P) for each t in T.
As usual, we take the 0th asset as num´eraire and consider the discounted
price processes S
i
t =
Si
t
S0
t instead. This ensures that S
0 ≡1 and that all
prices are expressed in units of S0. Given any self-financing trading strategy
θ =

θi
t : 0 ≤i ≤d

1≤t≤T , the discounted value process V (θ) defined as
V 0(θ) = θ1 · S0,
V t(θ) = θt · St(θ) for t = 1, 2, . . . , T
satisfies
V t(θ) = V 0(θ) + Gt(θ) for all t = 1, 2, . . . , T,
where
Gt(θ) =
t

u=1
,θu · ∆,St,
with ∆,St =

Si
t
S0
t −
Si
t−1
S0
t−1

1≤i≤d and ,θt = (θi
t)1≤i≤d.
Proof of the Fundamental Theorem. As we have seen in Proposition 3.3.2,
the no-arbitrage condition in this multi-period model can be restated as,
for all t and θ ∈L0(Ω, Ft−1, P; Rd), the requirement ,θt · ∆,St ≥0 a.s. (P)
implies that ,θt · ∆,St = 0 a.s. (P).
We therefore consider the single-period model with times {t −1, t} in-
stead of {0, 1}. Defining the subspace
Kt =

,θt · ∆,St : ,θt ∈L0(Ω, Ft−1, P; Rd)

,
(3.16)
we have the reformulation of the no-arbitrage condition as
Kt ∩L0
+(Ω, Ft, P) = {0} .
(3.17)
This statement involves knowledge of the measure P only through its null
sets and thus remains valid for any probability equivalent to P. It also
allows us to apply Theorem 3.5.4 to the tth trading period for each t ≤T.
Beginning with t = T, we obtain a probability measure QT ∼P with
bounded density dQT
dP
such that EQT

∆,ST |FT −1

= 0. Thus we are able
to start the backward induction procedure.
Assume by induction that

84
CHAPTER 3. THE FIRST FUNDAMENTAL THEOREM
we have found a probability measure Qt+1 ∼P that turns the process
(,Su)t+1≤u≤T into a martingale; i.e., that
EQt+1

∆,Su |Fu−1

= 0 for u = t + 1, t + 2, . . . , T.
Then (3.17) is valid with Qt+1 in place of P, and we can again apply
Theorem 3.5.4 to find a probability measure Qt ∼Qt+1 with bounded
Ft-measurable density
dQt
dQt+1 such that EQt

∆,St |Ft−1

= 0. The density
dQt
dP =
dQt
dQt+1
dQt+1
dP
remains bounded and is strictly positive a.s. (P), since
Qt ∼Qt+1 ∼P. Now apply the Bayes rule (3.10) to these measures with
integrand ∆,Su for t + 1 ≤u ≤T:
EQt

∆,Su |Fu−1

=
EQt+1

∆,Su
dQt
dQt+1 |Fu−1

EQt+1

dQt
dQt+1 |Fu−1

= EQt+1

∆,Su |Fu−1

= 0
since the density
dQt
dQt+1 is Ft-measurable and hence Fu−1-measurable for
every u ≥t + 1. Under Qt ∼P, the process (,Su)t≤u≤T is therefore a
martingale, which completes the induction step. The measure Q1 ∼P we
obtain at the final step, when t = 1, turns (,Su)1≤u≤T into a martingale.
The result follows.
Equivalent Martingale Measures and
Change of Num´eraire
Having established the fundamental relationship between viability of the
model and the existence of EMMs, it is natural to consider the impact
of a change of num´eraire. On the one hand, the viability of the model
is not affected by a change of num´eraire, since the definition of arbitrage
(e.g. , as expressed in terms of the gains process at a single step, as in
Proposition 3.3.2) does not involve the amount of a positive gain but only
its existence. On the other hand, whether a given measure is an EMM
for the model will in general depend on the choice of num´eraire. At the
same time, it seems plausible that there should be a simple relationship
between the sets of EMMs for a given model under two different choices of
num´eraire: it is clear from model viability that both sets are either empty
or non-empty together.
So assume that we have a viable pricing model in which the assets S0
and S1 are strictly positive throughout. Denote by Pi the non-empty set
of EMMs for the model when Si is used as num´eraire (i = 0, 1). Recall that
we write the discounted price process as S =

1, S1
S0 , S2
S0 , . . . , Sd
S0

when S0

3.5 GENERAL DISCRETE MODELS
85
is used as num´eraire. Write -S for the discounted price process when the
num´eraire is S1, so that -S =

S0
S1 , 1, S2
S1 , . . . , Sd
S1

. Note that -Si = S0
S1 S
i
for i = 0, 1, . . . , d. Recall that M1(Ω, F) denotes the space of probability
measures on (Ω, F).
Proposition 3.5.16. We have
P1 =

-Q : -Q ∈M1(Ω, F); d -Q
dQ = S
1
t
S
1
0
for some Q ∈P0
&
.
Proof. Denote the set of probability measures on the right by -P. We first
show that P1 ⊂-P. To do this, fix Q ∈P0, let t ∈T be given, and write
Λt = S
1
t
S
1
0
= S1
t
S0
t
.S0
0
S1
0
.
Then Λ0 ≡1 and Λ is a Q-martingale since
EQ (Λt |Ft−1 ) = 1
S
1
0
EQ

S
1
t |Ft−1

= S
1
t−1
S
1
0
= Λt−1 a.s. (Q) .
(3.18)
Since S0
t > 0 and S1
t > 0 for all t by hypothesis, Λt > 0 a.s. (Q) for all t.
In particular, d 
Q
dQ = Λt defines a probability measure -Q ∼Q ∼P.
It remains to show that -S is a martingale under -Q. By Bayes’ rule and
the definition of Λ, we have a.s. (Q) for u < t in T and i = 0, 1, . . . , d,
E 
Q

-Si
t |Fu

=
EQ

-Si
tΛt |Fu

EQ (Λt |Fu )
= 1
Λu
EQ

-Si
tΛt |Fu

= 1
Λu
EQ
S0
t
S1
t
S
i
tΛt |Fu

= 1
Λu
S0
0
S1
0
EQ

S
i
t |Fu

= S0
u
S1u
S
i
u = -Si
u.
Therefore -Q ∈P1 and we have proved that -P contains P1. To prove
the opposite inclusion, we need only reverse the roles of -S and S, so the
proposition is proved.

Chapter 4
Complete Markets
Our objective in this chapter is to characterise completeness of the market
model. First we provide a simple reformulation of completeness in terms
of the representability of martingales. Although we restrict our attention
(and apply the results) to finite market models, the more general theorems
proved in the final two sections of this chapter can easily be applied to
reproduce this proof for general discrete-time models.
The key result proved for finite market models states that in a viable
complete model the equivalent martingale measure is unique. For finite
models such as the CRR model, which is examined in detail, the fine struc-
ture of the filtrations can be identified more fully. However, we shall see
later that the restriction to finite complete models is more apparent than
real and that, in the discrete setting, complete models form the exception
rather than the rule. To establish the desired characterisation of complete
models, we also characterise the attainability of contingent claims-in the
general setting, this requires the full power of the first fundamental theo-
rem.
Let S = (Si : i = 0, 1, . . . , d) be a non-negative Rd+1-valued stochastic
process representing the price vector of one riskless security with
S0
0 = 1,
S0
t = β−1
t
S0
0,
and d risky securities

Si
t : i = 1, 2, . . . , d

for each t ∈T = {0, 1, . . . , T} .
Let X be a contingent claim (i.e., a nonnegative F-measurable random
variable X : Ω→R). Recall that X is said to be attainable if there exists
an admissible trading strategy θ that generates X (i.e., whose value process
V (θ) ≥0 satisfies VT (θ) = X a.s. (P)).
87

88
CHAPTER 4. COMPLETE MARKETS
4.1
Completeness and Martingale Represen-
tation
Let (Ω, F, P, T, F) be a complete market model with unique EMM Q. This
is equivalent to the following martingale representation property: the dis-
counted price S serves as a basis (under martingale transforms) for the
space of (F, Q)-martingales on (Ω, F). To avoid integrability issues, we re-
strict ourselves to finite models in the proof of the following proposition.
Proposition 4.1.1. The viable finite market model (Ω, F, T, F, P) with
EMM Q is complete if and only if each real-valued (F, Q)-martingale M =
(Mt)t∈T can be represented in the form
Mt = M0 +
t

u=1
γu · ∆Su = M0 +
d

i=1

t

u=1
γi
u∆S
i
u

(4.1)
for some predictable process γ =

γi : i = 1, 2, . . . , d

.
Proof. Suppose the model is complete, and (since every martingale is the
difference of two positive martingales) assume without loss of generality
that M = (Mt) is a non-negative (F, Q)-martingale.
Let C = MT S0
T ,
and find a strategy θ ∈Θa that generates this contingent claim, so that
VT (θ) = C, and hence V T (θ) = MT . Now, since the discounted value
process V is a Q-martingale, we have
V t(θ) = EQ

V t(θ) |Ft

= EQ (MT |Ft ) = Mt.
Thus the martingale M has the form
Mt = V t(θ) = V0(θ) +
t

u=1
θu · ∆Su = M0 +
t

u=1
θu · ∆Su
for all t ∈T. Hence we have proved (4.1) with γu = θu for all u ∈T.
Conversely, fix a contingent claim C, and define the martingale M =
(Mt) by setting Mt = EQ (βT C |Ft ) . By hypothesis, the martingale M has
the representation (4.1). So we define a strategy θ by setting
θi
t = γi
t for i ≥1,
θ0
t = Mt −γt · St for t ∈T.
We show that θ is self-financing by verifying that (∆θt) · St−1 = 0. Indeed,
for fixed t ∈T, we have
(∆θt) · St−1 = S0
t−1

∆Mt −∆
! d

i=1
γi
tS
i
t
"
+
d

i=1
Si
t−1∆γi
t
=
d

i=1

S0
t−1
)
γi
t∆S
i
t −

γi
tS
i
t −γi
t−1S
i
t−1
*
+ Si
t−1∆γi
t


4.2. COMPLETENESS FOR FINITE MARKET MODELS
89
=
d

i=1
Si
t−1

∆γi
t −∆γi
t

= 0.
Moreover, Vt(θ) = θt · St = MtS0
t for all t ∈T. In particular, we obtain
C = VT (θ), as required. Thus the market model is complete.
4.2
Completeness for Finite Market Models
We saw in Chapter 2 that the Cox-Ross-Rubinstein binomial market model
is both viable and complete. In fact, we were able to construct the equiv-
alent martingale measure Q for S directly and showed that in this model
there is a unique equivalent martingale measure. We now show that this
property characterises completeness in the class of viable finite market mod-
els.
Theorem 4.2.1 (Second Fundamental Theorem for Finite Market
Models). A viable finite market model is complete if and only if it admits
a unique equivalent martingale measure.
Proof. Suppose the model is viable and complete and that Q and Q′ are
martingale measures for S with Q′ ∼P ∼Q. Let X be a contingent claim,
and let θ ∈Θa generate X. Then, by (2.7), we have
βT X = V T (θ) = V0(θ) +
T

t=1
θt · ∆St.
(4.2)
Since each discounted price process S
i is a martingale under both Q and
Q′, the above sum has zero expectation under both measures. Hence
EQ (βT X) = V0(θ) = EQ′ (βT X) ;
in particular,
EQ (X) = EQ′ (X) .
(4.3)
Equation (4.3) holds for every F-measurable random variable X, as the
model is complete. In particular, it holds for X = 1A, where A ∈F is
arbitrary, so that Q(A) = Q′(A). Hence Q = Q′, and so the equivalent
martingale measure for this model is unique.
Conversely, suppose that the market model is viable but not complete,
so that there exists a non-negative random variable X that cannot be
generated by an admissible trading strategy. This implies that X cannot
be generated by any self-financing strategy θ =

θ0, θ1, θ2, . . . , θd
, and
by (2.8) we can restrict attention to predictable processes

θ1, θ2, . . . , θd
in Rd, as these determine θ0 up to constants.
Therefore, define
L =

c +
T

t=1
θt · ∆St : θ predictable, c ∈R
&
.

90
CHAPTER 4. COMPLETE MARKETS
Then L is a linear subspace of the vector space L0(Ω, F, P). Note that this
is just Rn, where the minimal F-partition of Ωhas n members. Since this
space is finite-dimensional, L is closed.
Suppose that βT X ∈L (i.e., βT X = c+T
t=1 θt·∆St for some Rd-valued
predictable process θ). By (2.8), we can always extend θ to a self-financing
strategy with initial value c. However, X would be attained by this strategy.
Hence we cannot have βT X ∈L, and so L is a proper subspace of L0 and
thus has a non-empty orthogonal complement L⊥.
Thus, for any EMM Q, there exists a non-zero random variable Z ∈L0
such that
EQ (Y Z) = 0 for all Y ∈L.
(4.4)
As L0 is finite-dimensional, Z is bounded. Note that EQ (Z) = 0 since
Y ≡1 is in L (take θi ≡0 for i ≥1).
Define a measure Q′ ∼Q by
Q′(ω)
Q(ω) = R(ω),
where
R(ω) = 1 +
Z(ω)
2 ∥Z∥∞
,
∥Z∥∞= max {|Z(ω)| : ω ∈Ω} .
Then Q′ is a probability measure since Q′({ω}) > 0 for all ω and
Q′(Ω) = EQ (R) = 1,
as EQ (Z) = 0. Moreover, for each Y = c + T
t=1 θt · ∆St ∈L, we have
EQ′ (Y ) = EQ (RY ) = EQ (Y ) +
1
2 ∥Z∥∞
EQ (Y Z) = c.
In particular, EQ′ (Y ) = 0 when Y has c = 0. Thus, for any predictable
process θ =

θi
t : t = 1, 2, . . . , T, i = 1, 2, . . . , d

, we have
EQ′
 T

t=1
θt · ∆St

= 0.
(4.5)
Again using θ = (0, . . . , 0, θi, 0, . . . , 0) successively for i = 1, 2, . . . , d in (4.5),
it is clear that Theorem 2.3.5 implies that S is a Q′-martingale. We have
therefore constructed an equivalent martingale measure distinct from Q.
Thus, in a viable incomplete market, the EMM is not unique. This com-
pletes the proof of the theorem.

4.3. THE CRR MODEL
91
4.3
The CRR Model
Again the Cox-Ross-Rubinstein model provides a good testbed for the ideas
developed above. We saw in Section 2.6 that this model is complete, by
means of an explicit construction of the unique EMM as a product of one-
step probabilities. We explore the content of the martingale representation
result (Proposition 4.1.1) in this context and use it to provide a more precise
description of the generating strategy for a more general contingent claim.
Recall that the bond price in this model is S0
t = (1 + r)t for t ∈T =
{0, 1, . . . , T} , where r > 0 is fixed, and that the stock price S satisfies
St = RtSt−1, where
Rt =

1 + b
with probability q = r−a
b−a,
1 + a
with probability 1 −q = b−r
b−a.
Here we assume that −1 < a < r < b to have a viable market model,
and the sample space can be taken as Ω= {1 + a, 1 + b}T\{0} , so that the
independent, identically distributed random variables {Rt : t = 1, 2, . . . , T}
describe the randomness in the model. The unique EMM Q then takes the
form
Q(Rt = ωt : s = 1, 2, . . . , T) =

t≤T
qt,
where
qt =

q
if ωt = 1 + b,
1 −q
if ωt = 1 + a.
In such simple cases, a direct proof of the martingale representation
theorem is almost obvious and does not depend on the nature of the sample
space, since the (Rt) contain all the relevant information.
Proposition 4.3.1. Suppose that (Ω, F, Q) is a probability space and (Rt,
where 1, 2, . . . , T, is a finite sequence of independent and identically dis-
tributed random variables, taking the two values u, v with probabilities q and
1−q, respectively. Suppose further that E (R1) = w, where −1 < v < w < u
and
q = w −v
u −v
(4.6)
while mt = t
s=1(Rt −w), F0 = {∅, Ω}, andFt = σ(Rs : s ≤t) for all
t = 1, 2, . . . , T.
Then (mt, Ft, Q) is a centred martingale and every (Ft, Q)-martingale
(Mt, Ft, Q) with EQ (M0) = 0 can be expressed in the form
Mt =

s≤t
θs∆ms,
(4.7)
where the process θ = (θt) is (Ft)-predictable.

92
CHAPTER 4. COMPLETE MARKETS
Proof.
We follow the proof given in [299],15.1 (see also [63], [283]). It
is obvious that m = (mt) is a martingale relative to (Ft, Q). Since Mt is
Ft−measurable, it has the form
Mt(ω) = ft(R1(ω), R2(ω), . . . , Rt(ω)) for all ω ∈Ω.
Now suppose that (4.7) holds. It follows that the increments of M take the
form ∆Mt(ω) = θt(ω)∆mt(ω), so that, if we set
f u
t (ω) = ft(R1(ω), R2(ω), . . . , Rt−1(ω), u),
f v
t (ω) = ft(R1(ω), R2(ω), . . . , Rt−1(ω), v),
then (4.7) results from showing that
f u
t −ft−1 = θt(u −w),
f v
t −ft−1 = θt(v −w).
In other words, θt would need to take the form
θt = f u
t −ft−1
u −w
= f v
t −ft−1
v −w
.
(4.8)
To see that this is indeed the case, we simply use the martingale property
of M. Since EQ (∆Mt |Ft−1 ) = 0, we have
qf u
t + (1 −q)f v
t = ft−1 = qft−1 + (1 −q)ft−1.
This reduces to
f u
t −ft−1
1 −q
= f v
t −ft−1
q
,
which is equivalent to (4.8) because of (4.6).
Valuation of General European Claims
We showed in Section 2.6 that the value process
Vt(C) = (1 + r)−(T −t)EQ (C |Ft )
of a European call option C in the Cox-Ross-Rubinstein model can be
expressed more concretely in the form Vt(C) = v(t, St), where
v(t, x) = (1 + r)−(T −t)
T −t

u=o
.T −t
u

qu(1 −q)T −t−u
/
×(x(1 + b)u(1 + a)T −t−u −K)+
.
This Markovian nature of the European call (i.e., the fact that the value
process depends only on the current price and not on the path taken by the
process S), can be exploited more generally to provide explicit expressions
for the value process and generating strategies of a European contingent

4.3. THE CRR MODEL
93
claim (i.e., a claim X = g(ST )). In the CRR model, we know that the
evolution of S is determined by the ratios (Rt), which take only two values,
1 + b and 1 + a. For any path ω, the value ST (ω) is thus determined
by the initial stock price S0 and the number of ‘upward’ movements of
the price on T = {0, 1, . . . , T} . To express this more simply, note that
Rt = (1 + a) + (b −a)δt, where δt is a Bernoulli random variable taking the
value 1 with probability q. Hence we can consider, generally, claims of the
form X = h(uT ), where uT (ω) = 
t≤T δt(ω).
Recall from Proposition 4.3.1 that the martingale Mt = EQ (X |Ft ) can
be represented in the form Mt = M0 + 
u≤t θu∆mu. Using v = 1 + a,
w = 1 + r, and u = 1 + b in applying Proposition 4.3.1 in the CRR setting,
we have mu = Ru −(1 + r). Therefore
∆mu = (1+a)−(b−a)δu−(1+r) = (b−a)

δu −r −a
b −a

= (b−a)(δu−q).
Thus the representation of M can also be written in the form
Mt =

u≤t
αu(δu −q),
where αu = (b −a)θu.
Consider the identity ∆Mt = αt(δt −q). Exactly as in the proof of
Proposition 4.3.1, this leads to a description of α. Indeed,
αt = EQ (MT |{δu, u < t} , δt = 1) −EQ (MT |{δu, u < t})
1 −q
= EQ (h(uT ) |{δu, u < t} , δt = 1) −EQ (h(uT ) |{δu, u < t})
1 −q
.
We now restrict our attention to the set
A = {ω : ut−1(ω) = x, δt = 1} .
On A, we obtain, using the independence of the (Rt),
EQ (h(uT ) |Ft ) = EQ (h(x + 1 + (uT −ut))) ,
EQ (h(uT ) |Ft−1 ) = EQ (h(x + (uT −ut−1)))
= qEQ (h(x + 1 + (uT −ut)))
+ (1 −q)EQ (h(x + (uT −ut))) .
Thus, on the set A, we have
EQ (h(uT ) |Ft ) −EQ (h(uT ) |Ft−1 )
= (1 −q)EQ (h(x + 1 + (uT −ut)) −h(x + (uT −ut))) ,
and the final expectation is just
T −t

s=0
T −t
s

[h(x + 1 + s) −h(x + s)]qs(1 −q)T −t−s.

94
CHAPTER 4. COMPLETE MARKETS
We have therefore shown that
αt = HT −t(ut−1; q),
where
Hs(x; q) =
s

τ=0
s
τ

(h(x + 1 + τ) −h(x + τ)) qτ(1 −q)s−τ.
For a European claim X = f(ST ), this can be taken further using the
explicit form of the martingale representation given in Proposition 4.1.1.
We leave the details (which can be found in [283]) to the reader and simply
note here that the function h given above now takes the form
h(x) = (1 + r)−T f(S0(1 + b)x(1 + a)T −x),
which leads to the following ratio for the time t stock holdings:
αt = (1 + r)−(T −t) FT −t(St−1(1 + b); q) −FT −t(St−1(1 + a); q)
St−1(b −a)
,
(4.9)
where
Ft(x; p) =
t

s=0
t
s

f

x(1 + b)s(1 + a)t−s
ps(1 −p)t−s.
Note that for a non-decreasing f we obtain αt ≥0 for all t ∈T. Hence
the hedge portfolio can be obtained without ever having to take a short
position in the stock, although clearly we may have to borrow cash to
finance the position at various times.
Exercise 4.3.2.
Use formula (4.8) to obtain an explicit description of the
strategy that generates the European call option with strike K and expiry
T in the CRR model.
4.4
The Splitting Index and Completeness
Harrison and Kreps [148] introduced the notion of the splitting index for vi-
able finite market models as a means of identifying event trees that lead to
complete models. This idea is closely related to the concept of extremality
of a probability measure among certain convex sets of martingale mea-
sures, and in this setting, the ideas also extend to continuous-time models
(see [290], [150]).
Fix a finite market model (Ω, F, Q, T, F, S) with St = (Si
t)0≤i≤d. We
assume that the filtration F = (Ft) is generated by minimal partitions
(Pt). The splitting index K(t, A) of a set A ∈Pt−1 is then the number of
branches of the event tree that begin at node A; i.e.,
K(t, A) = card{A′ ∈Pt : A′ ⊂A} for t = 1, 2, . . . , T.
(4.10)

4.4. THE SPLITTING INDEX AND COMPLETENESS
95
It is intuitively clear that this number will serve to characterise com-
pleteness of the market since we can reduce our consideration to a single-
period market (as we have seen in Chapter 3) with A as the new sample
space. In order to construct a hedging strategy that we use to ‘span’ all the
possible states of the market at time t by means of a linear combination of
securities (i.e., a linear combination of the prices (Si
t(ω))0≤i≤d) clearly the
number of different possible states should not exceed (d+1). Moreover, it is
possible that some of the prices can be expressed as linear combinations of
the remaining ones and hence are ‘redundant’ in the single-period market,
so that, as before, what matters is the rank of the matrix of prices (which
correspond to the price increments in multi-period models). Recalling fi-
nally that the bond is held constant as num´eraire, the following result, for
which we shall only outline the proof, becomes plausible.
Proposition 4.4.1. A viable finite market model is complete if and only
if for every t = 1, 2, . . . , T and A ∈Pt−1 we have
dim(span{∆St(ω) : ω ∈A}) = K(t, A) −1.
(4.11)
In particular, if the market contains no redundant securities (i.e., there is
no α ̸= 0 in Rd+1, t > 0 in T and A ∈Pt−1 such that Q(α·St = 0 |A) = 1),
then K(t, A) = d + 1.
Outline of Proof. (see [290] for details) Refer to the notation introduced
in the discussion following Lemma 3.3.6. We can reduce this situation to
the one-step conditional probabilities as in Chapter 3 and finally ‘paste
together’ the various steps. We also assume without loss of generality that
S0 ≡1 throughout, so that St = St for all t ∈T.
Fix A ∈Pt−1 and consider the set M of all probability measures on the
space (A, AA), where AA is the σ-algebra generated by the sets {Ai, i ≤n}
in Pt that partition A. Consider an element QA of the convex set
M0 =

Q′
A ∈M : EQ′
A (∆St1A) = 0

.
If QA is in M0 and assigns positive mass to A1, A2, . . . , Am, while giving
zero mass to the other Ai, then we can write the price increment on the
set Aj, j ≤m, as ∆St(ω) = yi −y, where St−1(ω) = y is constant on A
since S is adapted. The condition that QA cannot be expressed as a convex
combination of measures in M0 now translates simply to the demand that
the vectors (yi−y) are linearly independent. In other words, that the matrix
of price increments has linearly independent columns. But we have already
seen that non-singularity of the matrix of price increments is equivalent to
completeness in the single-period model. The proof may now be completed
by pasting together the steps to construct the unique EMM.
Example 4.4.2. We already know that the binomial random walk model
is complete by virtue of the uniqueness of the EMM. Our present interest
is in the splitting index.
Recall that the price process S has the form

96
CHAPTER 4. COMPLETE MARKETS
St =  t
u=1 rt, where the return process rt takes only the values u = 1 + b
and d = 1+a and is independent of Ft−1, so that we can describe the price
dynamics by an event tree, as in Figure 1.3.
Clearly there are only two branches at each node, so that K(t, A) = 2,
while
dim(span{∆St(ω) : ω ∈A}) = 1
for each A ∈Pt, t ∈T : ∆S0 ≡0, and ∆S1
t (ω) = S1
t−1(ω)(Rt(ω) −1) takes
the values bS1
t−1(ω) and aS1
t−1(ω), both of which are multiples of S1
t−1(ω),
which remains constant throughout A.
Example 4.4.3. For d ≥2, however, the d-dimensional random walk com-
posed of independent copies of one-dimensional walks cannot be complete;
we have K(t, A) = 2d, and this equals d + 1 only when d = 1.
We can easily construct an infinite number of EMMs for the two-
dimensional (also known as two-factor) random walk model. In the ex-
ample above, we have a price process S = (1, S1, S2) with stock return
processes R1, R2, which we assume to take the values (1±a1) and (1±a2),
respectively (so that we make the ‘up’ and ‘down’ movements symmetrical
in each coordinate). Suppose that a1 = 1
2 and a2 = 1
4, and define, for each
λ ∈(0, 1
2), a probability measure Qλ by fixing, at each t = 1, 2, . . . , T, the
return probabilities as follows:
Qλ(R1
t = 1 + a1, R2
t = 1 + a2) = λ = Qλ(R1
t = 1 −a1, R2
t = 1 −a2),
Qλ(R1
t = 1 + a1, R2
t = 1 −a2) = 1
2 −λ = Qλ(R1
t = 1 −a1, R2
t = 1 + a2).
It is straightforward to check that each Qλ is an EMM; i.e., that
EQλ

Ri
t |Ft−1

= EQλ

Ri
t

= 1 for all t ≥1.
It can be shown (much as we did in Chapter 2) that the multifactor
Black-Scholes model is a limit of multifactor random walk models and is
complete. Consequently, it is possible to have a complete continuous-time
model that is a limit (in some sense) of incomplete discrete models.
If
one is interested in ‘maintaining completeness’ along the approximating
sequence, then one is forced to use correlated random walks. See [63], [151]
for details.
Filtrations in Complete Finite Models
The completeness requirement in finite models is very stringent. It fixes
the degree of linear dependence among the values of the price increments
∆St on any partition set A ∈Pt−1 in terms of the number of cells into
which Pt ‘splits’ the set A. It also ensures that the filtration F = (Ft) that
is determined by these partition sets is in fact the minimal filtration FS
(i.e., the σ-field Ft = FS
t = σ(Su : u ≤t) for each t).

4.5. INCOMPLETE MODELS: THE ARBITRAGE INTERVAL
97
To see this, let Q denote the unique EMM in the complete market
model and suppose that, on the contrary, the filtration F = (Ft) strictly
contains FS. Then there is a least u ∈T such that Fu strictly contains
FS
u . This means that some fixed A ∈PS
u (the minimal partition generating
FS
u ) can be split further into sets in the partition Pu generating Fu (i.e.,
A = ∪n
i=1Ai for some Ai ∈Pu(n ≥2)).
Note that Su is constant on A = ∪n
i=1Ai. There is a unique set B ∈
Pu−1 = PS
u−1 that contains A. The partition Pu then contains disjoint sets
{Ai : i = 1, 2, . . . , m} whose union is B, and since A ⊂B, we can assume
(re-ordering if needed) that m ≥n and the sets A1, A2, . . . , An defined
above comprise the first n of these.
Let Q∗be a probability measure on (Ω, F) such that Q∗(· |B ) defines
different conditional probabilities with Q∗(Ai |B ) > 0 for all i ≤n and
such that
n

i=1
Q∗(Ai |B ) = Q(A |B ),
Q∗(Aj |B ) = Q(A |B ) for j = n + 1, . . . , m,
and agreeing with Q otherwise. There are clearly many choices for such
Q∗.
Since ∆Su is constant on A = +n
i=1 Ai, it follows that
EQ∗(∆Su |Fu−1 ) (ω) = EQ (∆Su |Fu−1 ) (ω) = 0
holds for all ω ∈B and hence throughout Ω. Hence Q is not the only EMM
in the model, which contradicts completeness.
Thus, in a complete finite market model there is no room for ‘extraneous
information’ that does not result purely from the past behaviour of the
stock prices. This severely restricts its practical applicability, as Kreps [202,
p. 228] has observed: the presence of other factors (Kreps lists ‘differential
information, moral hazard, and individual uncertainty about future tastes’
as examples) that are not fully reflected in the security prices will destroy
completeness.
4.5
Incomplete Models:
The Arbitrage In-
terval
We return to the general setup of extended securities market models that
was introduced in Section 2.5.
We wish to examine the set of possible
prices of a European contingent claim H that preclude arbitrage. Since
H is itself a tradeable asset, we need to include it in the assets that can
be used to produce trading strategies.
It was shown in Theorem 2.5.2
that, for any given measure Q, the only price for H consistent with the
absence of arbitrage is given by the ‘martingale price’ π(H) = EQ (βT H)
derived in (2.15).
We now consider a viable model with P as the set

98
CHAPTER 4. COMPLETE MARKETS
of equivalent martingale measures for the discounted price process Sand
augment this model by regarding H as an additional primary asset. In
discounted terms, we therefore set S
d+1
t
= βtH and consider the range
of possible initial prices πH consistent with the no-arbitrage requirement
in the model. We call these prices arbitrage-free prices for the extended
model. Denote the extended (discounted) price process by -S = (S, S
d+1),
where the final coordinate must satisfy the constraints
S
d+1
0
= πH,
S
d+1
t
≥0 a.s. (P) for t = 1, 2, . . . , T −1,
S
d+1
T
= H.
Denote by Π(H) the set of all arbitrage-free prices for H. The first
fundamental theorem immediately enables us to identify Π(H) via the set
of expectations EQ (βT H) for Q in P. However, since H cannot necessarily
be generated by an admissible strategy, we do not know in advance that
the integral is finite. We need the following result.
Theorem 4.5.1. Let H be a European claim in a viable securities market
model (Ω, F, P, T, F, S) with P as the set of EMMs for S. The set Π(H) of
arbitrage-free prices for H is given by
Π(H) = {EQ (βT H) : Q ∈P, EQ (H) < ∞} .
(4.12)
The lower and upper bounds of Π(H) are given by
π−= inf
P EQ (βT H) ,
π+ = sup
P
EQ (βT H) .
Proof. The first fundamental theorem states that the extended model is
viable if and only if it admits an EMM Q for the price process -S = (S
i :
i = 0, 1, . . . , d + 1). This measure therefore satisfies
S
i
t = EQ

S
i
T |Ft

for i = 1, 2, . . . , d + 1 and t = 0, 1, . . . , T.
Thus, in particular, S = (S
i : i = 0, 1, . . . , d) is a Q-martingale, so that
Q ∈P, and EQ (βT H) = EQ

S
d+1
t

< ∞. The arbitrage-free price πH is
therefore a member of the set on the right-hand side in (4.12).
To establish the converse inclusion, let πH = EQ (βT H) for some Q ∈P.
We need to show that πH is an arbitrage-free price. For this, take the
martingale X = (Xt), where
Xt = EQ (βT H |Ft ) for t ∈T,
as the candidate for the ‘price process’ of the asset βH. This clearly satisfies
the requirements in (4.12) so that, with this S
d+1 = X, the price πH is
an arbitrage-free price and Q is an EMM for the extended model, which is
thus viable. Hence the two sets in (4.12) are equal.


## Stopping Times and American Options

4.5. INCOMPLETE MODELS: THE ARBITRAGE INTERVAL
99
The expectations are non-negative, so the expression for the lower
bound π−is clear. The same is true for the upper bound if the sets are
bounded above.
This leaves the proof that π+ = ∞if EQ (βT H) = ∞for some Q ∈P.
This is left to the reader as an exercise in using the fact that the EMM can
always be chosen to have bounded density relative to the given reference
measure.
This result allows us to characterise attainable claims as the only claims
admitting a unique arbitrage-free price and further identify the possible
prices of a general claim as the open interval (π−, π+). Our proof follows
that in [132].
Theorem 4.5.2. Let H be a European claim in a securities market model.
(i) If H is attainable, then Π(H) is a singleton and the unique arbitrage-
free price for H is π−= V0(θ) = π+, where θ is any generating
strategy for H.
(ii) If H is not attainable, then either Π(H) = ∅or π−< π+ and Π(H)
is the open interval (π−, π+).
Proof. The first statement follows from (2.15) and Theorem 4.5.1.
For the second, note that if Π(H) is non-empty, then it must be an
interval since P is convex.
We need to show that it is open and thus
neither bound is attained. For this, we need to construct for any π ∈Π(H)
two arbitrage-free prices π∗, π∗with π∗< π < π∗.
So fix π = EQ (βT H), where Q ∈P. We have to construct a measure
Q∗∈P such that
EQ∗(βT H) > EQ (βT H) .
The given price π is the initial value of the process V = (Vt)t∈T defined
by Vt = EQ (βT H |Ft ). Although the stochastic process V is not the value
process of a generating strategy, we are nonetheless guided in our search for
Q∗by what happens in that special situation. Since H is FT -measurable,
we obtain the telescoping sum
VT = EQ (βT H |FT ) = βT H = V0 +
T

t=1
(Vt −Vt−1) = V0 +
T

t=1
∆Vt. (4.13)
By the first conclusion of this theorem, H is an attainable claim if and
only if each term ∆Vt = EQ (βT H |Ft ) −EQ (βT H |Ft−1 ) has the form
∆Gt(θ) = ,θt∆,St for some predictable process ,θ = (θi)i=1,2,...,d, and by
Theorem 2.3.5 this occurs for the measure Q ∈P if and only if EQ (∆Vt) =
0 for each t = 1, 2, . . . , T. Since the given claim H is not attainable, this
must fail for some t = 1, 2, . . . , T (i.e., for some such t, ∆Vt is not of the
form ,θ · ∆,St for any Q-integrable Ft−1-measurable random vector ,θ).

100
CHAPTER 4. COMPLETE MARKETS
In other words, for this value of t, the random variable ∆Vt is disjoint
from the space Kt ∩L1(Ft, Q), where Kt is as defined by (3.16). Since this
is a closed subspace of L1(Ft, Q), we can separate it from the compact set
{∆Vt} by a linear functional Z in L∞(Ft, Q). We thus obtain real numbers
α < β such that for all X ∈Kt ∩L1(Ft, Q):
EQ (XZ) ≤α < β ≤EQ (∆VtZ) .
(4.14)
Now since Kt ∩L1(Ft, Q) is a subspace, EQ (XZ) ≤α for all X ∈Kt ∩
L1(Ft, Q) implies (as in the proof of Theorem 3.5.8) that α = 0. But then
if EQ (XZ) < 0 for some X, −X would violate the condition EQ (XZ) ≤0.
Hence EQ (XZ) = 0 for all X ∈Kt∩L1(Q). This means that EQ (∆VtZ) >
0. The same conclusion is reached if Z is replaced by
Z
3∥Z∥∞, so that we
may assume without loss of generality that |Z| ≤1
3 a.s. (P).
Therefore the L∞-function Z∗= 1+Z−EQ (Z |Ft−1 ) is a.s. (P) positive
and has EQ (Z∗) = 1, so that
dQ∗
dQ
= Z∗defines a probability measure
equivalent to Q and hence to P. We calculate the Q∗-expectation of βT H
using the fact that Z∗is Ft-measurable:
EQ∗(βT H) = EQ (βT HZ∗)
= EQ (βT H) + EQ (ZEQ (βT H |Ft ))
(4.15)
−EQ (EQ (Z |Ft−1 ) EQ (βT H |Ft−1 ))
= EQ (βT H) + EQ (ZVt) −EQ (Vt−1EQ (Z |Ft−1 ))
= EQ (βT H) + EQ (ZVt) −EQ (EQ (Vt−1Z |Ft−1 ))
= EQ (βT H) + EQ (∆VtZ)
> EQ (βT H)
(4.16)
by construction of Z. Therefore π∗= EQ∗(βT H) will be an element of
Π(H) greater than π, provided we can show that Q∗∈P, and thus we must
show that the discounted stock prices (,Si)i=1,2,...,d are Q∗-martingales.
Fix i ≤d and u > t. Then, by Bayes’ rule, we have
EQ∗

∆,Si
u |Fu−1

=
EQ

∆,Si
uZ∗|Fu−1

EQ (Z∗|Fu−1 )
= EQ

∆,Si
u |Fu−1

= 0
since Z∗is Fu−1-measurable for each u > t. On the other hand, since
EQ (Z∗|Ft−1 ) = EQ (1 + Z −EQ (Z |Ft−1 ) |Ft−1 ) = 1,
the restrictions of the measures Q and Q∗coincide on Fu for every u < t,
and so
EQ∗

∆,Si
u |Fu−1

= EQ

∆,Si
u |Fu−1

= 0.
Thus, to show that Q∗∈P, we need only consider EQ∗

∆,Si
t |Ft−1

.
For this, since by construction of Z, EQ

(,θ · ∆,St)Z

= 0 for all Ft−1-
measurable Rd-valued random vectors θ, we have EQ

Z∆,Si
t |Ft−1

=

4.6. CHARACTERISATION OF COMPLETE MODELS
101
0 a.s. (P) for each i ≤d. So we can write
EQ∗

∆,Si
t |Ft−1

= EQ

∆,Si
tZ∗|Ft−1

= EQ

∆,Si
t(1 + Z −EQ (Z |Ft−1 )) |Ft−1

= EQ

∆,Si
t(1 −EQ (Z |Ft−1 )) |Ft−1

+ EQ

Z∆,Si
t |Ft−1

.
The final term is a.s. (P) zero, as was shown above, while the first is,
a.s. (P),
EQ

∆,Si
t |Ft−1

[1 −EQ (Z |Ft−1 )] = 0
since EQ (Z |Ft−1 ) is Ft−1-measurable and Q ∈P. So we have verified that
Q∗∈P and hence π∗∈Π(H).
The construction of a suitable π∗< π in Π(H) is now straightforward.
For example, we can use the probability measure Q∗with density
dQ∗
dQ = 2 −Z∗,
a choice that ensures that EQ∗(2 −Z∗) = 1 and that 0 < 2 −Z∗≤5
3 since
|Z| ≤1
3. Since 2 −Z∗= 1 −Z + EQ (Z |Ft−1 ) , it follows as in (4.16) that
EQ∗(βT H) = EQ (βT H) −EQ (∆VtZ) < EQ (βT H) .
Also Q∗∈P :
EQ

∆,Si
t(2 −Z∗) |Ft−1

= 2EQ

∆,Si
t |Ft−1

−EQ

∆,Si
tZ∗|Ft−1

= 0,
as Q, Q∗∈P.
Remark 4.5.3. Note that Theorems 4.5.1 and 4.5.2 together imply that if
Π(H) is empty, then there is no EMM in the model for which the claim H
has finite expectation.
4.6
Characterisation of Complete Models
We saw in Theorem 4.5.2 that a viable finite market model is complete if
and only if the set P of its EMMs is a singleton. We could not establish this
result in greater generality until we had dealt with the first fundamental
theorem in the general setting (i.e., shown that the model is viable if and
only if P ̸= ∅) .
Having done this, and also having characterised the
attainability of claims, we can now go much further in identifying the class
of complete market models more fully. We shall demonstrate, after the fact,
that the argument provided to prove Theorem 4.5.2 will suffice in general
since every complete model in the discrete-time setting must actually be a
finite market model.

102
CHAPTER 4. COMPLETE MARKETS
Theorem 4.6.1. A viable securities market model (Ω, F, P, T, F, S) is com-
plete if and only if it allows a unique equivalent martingale measure. When
P is a singleton, the underlying probability space Ωis finitely generated and
its generating partition has at most (d + 1)T atoms.
Proof. With the more advanced tools now at our disposal, the proof of this
far-reaching result is elementary for general market models. Throughout,
we only need to work with bounded claims: in a finite-dimensional space
of random variables all elements are automatically bounded.
First consider the single-period case (i.e., let T = 1). Completeness of
the market means that every European contingent claim, that is, every non-
negative function in L0(F) is attainable by some generating strategy based
on the price processes (S)0≤i≤d. In particular, as already observed in Chap-
ter 2, the indicator 1A of any set in F is an attainable claim. Theorem 4.5.2
shows that the unique arbitrage-free price EQ (βT 1A) is independent of the
choice of EMM Q. Hence Q(A) is also uniquely determined for each A, so
that P is a singleton.
Conversely, if Q is the unique EMM in the model, any bounded claim H
is Q-integrable, and its price is given uniquely by EQ (βT H) . Again by The-
orem 4.5.2, it follows that H is attainable. Thus every element H ∈L∞(F)
is of the form θt ·St for some Rd+1-valued random vector θ. In other words,
the collection of possible portfolio values

θ · S : θ ∈θ ∈Rd+1
contains
L∞(F). This is only possible if L∞(F) has dimension at most d + 1 and
thus the σ-field F is generated by a finite partition with at most d + 1
atoms (see Lemma 4.6.2 below, whose proof is an easy exercise). Thus
every contingent claim is automatically bounded, hence attainable.
Turning now to the multi-period case, we argue by induction on T. Note
first that if every F-measurable bounded claim is attainable then F = FT
since for any A ∈F the generating value process is by construction FT -
measurable.
We know that, when T = 1, the probability space Ωof a
complete model has at most d + 1 atoms. Assume that, for every complete
model with T −1 trading periods, the underlying probability space has
at most (d + 1)T −1 atoms, and consider a complete model with T trading
periods. Thus every FT -measurable non-negative bounded random variable
can be written in the form VT −1 + θT · ∆ST for some FT −1-measurable
functions VT −1 and θT . These functions are constant on each of the (at
most (d + 1)T −1) atoms of (Ω, FT −1, P). For each such atom A, we can
consider the conditional probability P(· |A) since P(A) > 0. The vector
space L∞(Ω, FT , P(· |A)) has dimension at most (d+1), so by Lemma 4.6.2
it follows that (Ω, FT , P(· |A)) has at most (d + 1)T atoms.
Since the vector spaces Lp are therefore all finite-dimensional, all con-
tingent claims in the given model are bounded. Thus the value of each
claim H is given by the unique element of Π(H), and by Theorem 4.5.2 it
follows that H is attainable.
Lemma 4.6.2. For 0 ≤p ≤∞, the dimension of the space Lp(Ω, F, P)

4.6. CHARACTERISATION OF COMPLETE MODELS
103
equals
sup {n ≥1 : ∃partition {Fi ∈F : i ≤n} of Ωwith P(Ai) > 0 for i ≤n} .
The dimension n of Lp(F) is finite if and only if there is a partition of Ω
into n atoms.
Remark 4.6.3. There are various other characterisations of completeness,
notably in terms of the set of extreme points of P , which are better adapted
to their continuous-time analogues. We refer to [132] and [280] for details.
Note, however, that the characterisation given above illustrates that, in
mathematical terms, completeness will hold only for a very restricted subset
of the class of viable market models, since all complete models must in fact
be finite market models. Finance theorists, on the other hand, might argue
that realistic market models are necessarily finite.

Chapter 5
Discrete-time American
Options
American options differ fundamentally from their European counterparts
since the exercise date is now at the holder’s disposal and not fixed in
advance. The only constraint is that the option ceases to be valid at time T
and thus cannot be exercised after the expiry date T. The pricing problem
for American options is more complex than those considered up to now,
and we need to develop appropriate mathematical concepts to deal with
it. As in the preceding chapters, we shall model discrete-time options on a
given securities market model (Ω, F, P, T, F, S).
5.1
Hedging American Claims
Random Exercise Dates
First, we require a concept of ‘random exercise dates’ to reflect that the
option holder can choose different dates at which to exercise the option
depending on her perception of the random movement of the underlying
stock price.
The exercise date τ is therefore no longer the constant T
but becomes a function on Ωwith values in T, that is, a random variable
τ : Ω→T. It remains natural to assume that investors are not prescient,
so that the decision whether to exercise at time t when in state ω depends
only on information contained in the σ-field Ft. Hence our exercise dates
should satisfy the requirement that {τ = t} ∈Ft.
Exercise 5.1.1. Show that the following requirements on a random variable
τ : Ω→T are equivalent:
a) For all t ∈T, {τ = t} ∈Ft.
b) For all t ∈T, {τ ≤t} ∈Ft.
105

106
CHAPTER 5. DISCRETE-TIME AMERICAN OPTIONS
Hint: Recall that the (Ft) increase with t.
We briefly review relevant aspects of martingale theory and optimal
stopping.
These often require care about measurability problems.
The
greater technical complexity is offset by wider applicability of our results,
and they provide good practice for the unavoidable technicalities that we
encounter in the continuous-time setting. Throughout, however, it is in-
structive to focus on the underlying ideas, and it may be advantageous in
this and the following chapters to skip lightly over some technical matters
at a first reading.
Hedging Constraints
Hedge portfolios also require a little more care than in the European
case since the writer may face the liability inherent in the option at any
time in T.
More generally, an American contingent claim is a function
of the whole path t →St(ω) of the price process under consideration,
for each ω ∈Ω, not just a function of ST (ω).
We again assume that
S =

Si
t : i = 0, 1, . . . , d; t ∈T

, where S0
t = β−1
t
is a (non-random) risk-
less bond, and the stock price Si is a random process indexed by T for each
i = 1, 2, . . . , d.
Accordingly, let f = (ft(S))t∈T denote an American contingent claim,
so that f is a sequence of non-negative random variables, each depending,
in general, on

Si(ω) : 0 ≤i ≤d

for every ω ∈Ω. As considered in Sec-
tion 2.4, the hedge portfolio with initial investment x > 0 for this claim will
now be a self-financing strategy θ =

θi
t : i = 0, 1, . . . , d; t ∈T

, producing
a value process V (θ) that satisfies the hedging constraints
V0(θ) = θ1 · S0 = x,
Vt(θ)(ω) ≥ft(S0(ω), S1(ω), . . . , ST (ω)) for all ω ∈Ωand t > 0.
The hedge portfolio θ is now described as minimal if, for some random
variable τ with {ω : τ(ω) = t} ∈Ft for all t ∈T, we have
Vτ(ω)(θ)(ω) = fτ(ω)(S0(ω), . . . , ST (ω)).
(5.1)
Since the times at which the claim f takes its greatest value may vary
with ω, the hedge portfolio θ must enable the seller (writer) of the claim
to cover his losses in all eventualities since the buyer has the freedom to
exercise his claim at any time. The hedge portfolio will thus no longer
‘replicate’ the value of the claim in general, but it may never be less than
this value; that is, it must ‘superhedge’ or super-replicate the claim. This
raises several questions for the given claim f:
(i) Do such self-financing strategies exist for a given value of the initial
investment x > 0?
(ii) Do minimal self-financing strategies always exist for such x?

5.2. STOPPING TIMES AND STOPPED PROCESSES
107
(iii) What is the optimal choice of the random exercise time τ?
(iv) How should the ‘rational’ time-0 price of the option be defined?
These questions are examined in this chapter. To deal with them, however,
we first need to develop the necessary mathematical tools.
5.2
Stopping Times and Stopped Processes
The preceding considerations lead us to study ‘random times’, which we call
stopping times, more generally for (discrete) stochastic processes. While
our applications often have a finite time horizon, it is convenient to take
the study further, to include stopping times that take values in the set
¯N = {0, 1, . . . , ∞}. This extension requires us to establish results about
martingale convergence, continuous-time versions of which will also be
needed in later chapters.
The well-known martingale convergence theo-
rems are discussed briefly; we refer to other texts (e.g. ,[109], [199], [299])
for detailed development and proofs of these results.
The idea of stopping times for stochastic processes, while intuitively
obvious, provides perhaps the most distinguishing feature of the techniques
of probability theory that we use in this book.
At its simplest level, a
stopping time τ should provide a gambling strategy for a gambler seeking
to maximise his winnings; since martingales represent ‘fair’ games, such a
strategy should not involve prescience, and therefore the decision to ‘stop’
the adapted process X = (Xt) representing the gambler’s winnings at time
t should only involve knowledge of the progress of the winnings up to that
point; that is, if state ω occurs, the choice τ(ω) = t should depend only on
Ft. Generally, suppose we are given a filtration F = (Ft)t∈N on (Ω, F, P)
with F = F∞= σ (+∞
t=0 Ft) and such that F0 contains all P-null sets. We
have the following definition.
Definition 5.2.1. A stopping time is a random variable τ : (Ω, F) →¯N
such that for all t ∈N, {τ ≤t} ∈Ft.
Remark 5.2.2. Exercise 5.1.1 shows that we could equally well have used
the condition: for all t ∈N, {τ = t} ∈Ft. Note, however, that this depends
on the countability of N. For continuous-time models, the time set T is a
finite or infinite interval on the positive halfline, and we have to use the
condition {τ ≤t} ∈Ft for all t ∈T in the definition of stopping times. In
discrete-time models, the condition {τ = t} is often much simpler to verify.
Nevertheless, many of the basic results about stopping times, and their
proofs, are identical in both setups, and the exceptions become clear from
the following examples and exercises.
Example 5.2.3.
(i) Observe that if τ = t0 a.s., then {τ = t0} ∈F0 ⊂
Ft0, so that each ‘constant time’ is a stopping time. Similarly, it is
easy to see that τ + t0 is a stopping time for each stopping time τ
and constant t0.

108
CHAPTER 5. DISCRETE-TIME AMERICAN OPTIONS
(ii) Suppose that σ and τ are stopping times. Then σ ∨τ = max {σ, τ}
and σ ∧τ = min {σ, τ} are both stopping times. Indeed, consider
{σ ∨τ ≤t} = {σ ≤t} ∩{τ ≤t} ,
{σ ∧τ ≤t} = {σ ≤t} ∪{τ ≤t} .
In both cases, the sets on the right-hand side are in Ft since σ and τ
are stopping times.
(iii) Let (Xt)t∈N be an F-adapted process and let B be a Borel set. We
now show that τB : Ω→N defined by τB(ω) = inf {s ≥1 : Xs ∈B}
(where inf ∅= ∞) is an F-stopping time. (We call τB the hitting
time of B.)
To see this, note that each X−1
s (B) is in Fs since Xs is Fs-measurable.
Moreover, since F is increasing, Fs ⊂Ft when s ≤t. Hence, for any
t ≥0, {τB = t} ∈Ft since
{τB = t} =
t−1
0
s=0
{τB > s} ∩X−1
t
(B) =
t−1
0
s=0
(Ω\ X−1
s (B)) ∩X−1
t
(B).
The continuous-time counterpart of this result is rather more difficult
in general and involves delicate measurability questions; in special
cases, such as when B is an open set and t →Xt(ω) is continuous, it
becomes much simpler (see, e.g. ,[199]).
Exercise 5.2.4. Suppose that (τn) is a sequence of stopping times. Extend
the argument in the second example above to show that 1
n≥1 τn = sup(τn :
n ≥1) and 2
n≥1 τn = inf(τn : n ≥1) are stopping times. (Note that this
uses the requirement that the σ-fields Ft are closed under countable unions
and intersections.)
Fix a stochastic basis (Ω, F, ¯N, F, P) with F = F∞= σ (∪∞
t=0Ft). Recall
that we assume throughout that the σ-fields Ft are complete.
First we
consider random processes ‘stopped’ at a finite stopping time τ, as most of
our applications assume a finite trading horizon T.
Definition 5.2.5. If X = (Xt) is an adapted process and τ is any a.s.
finite
stopping time, then we define the map ω →Xτ(ω)(ω), giving the
values of X at the stopping time τ, by the random variable
Xτ =

t≥0
Xt1{τ=t}.
To see that Xτ is F-measurable, note that, for any Borel set B in R,
{Xτ ∈B} =
3
t≥0
({Xt ∈B} ∩{τ = t}) ∈F.
(5.2)
Moreover, if we define the σ-field of events prior to τ by
Fτ = {A ∈F : A ∩{τ = t} ∈Ft for all t ≥1} ,
(5.3)
then (5.2) shows that Xτ is Fτ-measurable since {Xt ∈B} is in Ft for each
t, so that {Xτ ∈B} ∈Fτ. Trivially, τ itself is Fτ-measurable.

5.2. STOPPING TIMES AND STOPPED PROCESSES
109
Exercise 5.2.6. Let σ and τ be stopping times.
(i) Suppose that A ∈Fσ. Show that A∩{σ ≤τ} and A∩{σ = τ} belong
to Fτ. Deduce that if σ ≤τ then Fσ ⊂Fτ. (Hint: The continuous-
time analogue of this result is proved in Theorem 6.1.8. Convince
yourself that a virtually identical statement and proof applies here.)
Deduce that, for any σ, τ, Fσ∧τ ⊂Fσ ⊂Fσ∨τ.
(ii) Show that the sets {σ < τ}, {σ = τ}, and {σ > τ} belong to both Fσ
and Fτ.
The next two results, which we will extend considerably later, use the
fact that stopping a martingale is essentially a special case of taking a
martingale transform. They are used extensively in the rest of this chapter.
Theorem 5.2.7 (Optional Sampling for Bounded Stopping Times).
Let X be a supermartingale and suppose that σ and τ are bounded stopping
times with σ ≤τ a.s. Then
E (Xτ |Fσ ) ≤Xσ a.s.
(5.4)
If X is a martingale, then E (Xτ |Fσ ) = Xσ a.s.
Proof. Consider the process φ = (φt), where φt = 1{σ<t≤τ}. The random
variable φt is Ft−1-measurable for t > 0 since
{σ < t ≤τ} = {σ < t} ∩(Ω\ {τ < t}) .
Thus φ is predictable and non-negative. We consider the transform φ · X.
Since τ is assumed to be bounded (by some k ∈N, say), we have
|(φ · X)t| ≤|X0| + · · · + |Xk| for all t,
so that each Zt = (φ · X)t is integrable. Thus Z is a supermartingale with
Z0 = 0 and Zk = Xτ −Xσ. Hence
0 = E (Z0) ≥E (Zk) = E (Xτ −Xσ) .
Now consider A ∈Fσ and apply the preceding equation to the bounded
stopping times σ′ and τ ′, where σ′ equals σ on A, and k otherwise, with a
similar definition for τ ′.
Exercise 5.2.8. Check carefully, using (5.3) and Exercise 5.2.6, that σ′ and
τ ′ are indeed stopping times.
This yields

A
XτdP ≤

A
XσdP.
Hence the result follows, again using Exercise 5.2.6.

110
CHAPTER 5. DISCRETE-TIME AMERICAN OPTIONS
Definition 5.2.9. Let X be a stochastic process on (Ω, F, P, T, F), and
let σ be any stopping time. Define the process Xσ stopped at time σ by
Xσ
t = Xσ∧t for all t ∈T.
Remark 5.2.10. Note carefully that (t, ω) →Xσ(ω)
t
(ω) = Xt∧σ(ω)(ω) is a
random process, while ω →Xσ(ω)(ω) is a random variable.
Then Xσ is again a transform φ · X, with φt = 1{σ≥t}. To complement
Theorem 5.2.7, we have the following result.
Theorem 5.2.11 (Optional Stopping Theorem). Suppose that X is
a (super-)martingale and let σ be a bounded stopping time. Then Xσ is
again a (super-)martingale for the filtration F.
Proof. We deal with the supermartingale case. For t ≥1,
Xt∧σ = X0 +

s≤t
φs∆Xs,
where we have set φs = 1{s≤σ}, which is predictable. Hence Xσ is adapted
to F and φs ≥0. Hence Xσ is a supermartingale. The martingale case is
then obvious.
5.3
Uniformly Integrable Martingales
In order to deal with unbounded stopping times, we need to develop a
little of the convergence theory for a particularly important class of mar-
tingales indexed by N, namely uniformly integrable (UI) martingales. The
counterparts of these results in the continuous-time setting are outlined in
Chapter 6.
Definition 5.3.1. A family C of random variables is uniformly integrable
(UI) if, given ϵ > 0, there exists K > 0 such that

{|X|>K}
|X| dP < ϵ for all X ∈C.
(5.5)
In other words, supX∈C
4
{|X|>K} |X| dP →0 as K →∞, which explains
the terminology. Such families are easy to find.
Examples of UI Families
First of all, if C is bounded in Lp(Ω, F, P) for some p > 1, then C is UI.
To see this, choose A such that E (|X|p) < A for all X ∈C and fix X ∈C,
K > 0. Write Y = |X| 1{|X|>K}. Then Y (ω) ≥K > 0 for all ω ∈Ω, and
since p > 1 it is clear that Y ≤K1−pY p. Thus
E (Y ) ≤K1−pE (Y p) ≤K1−pE (|X|p) ≤K1−pA.
But K1−p decreases to 0 when K →∞, so (5.5) holds.

5.3. UNIFORMLY INTEGRABLE MARTINGALES
111
Exercise 5.3.2. Prove that if C is UI, then it is bounded in L1, but the
converse is false.
A useful additional hypothesis is domination in L1: if there exists Y ≥0
in L1 such that |X| ≤Y for all X ∈C, then C is UI. (See, e.g. ,[299] for a
simple proof.)
To illustrate why uniform integrability is so important for martingales,
consider the following.
Proposition 5.3.3. Let X ∈Lp, p ≥1. The family
U = {E (X |G ) : G is a sub-σ-field of F}
is UI.
We prove this for the case p > 1 (which is all we need in the sequel) and
refer to [299, Theorem 13.4] for the case p = 1. First we need an important
inequality, which we will use frequently.
Proposition 5.3.4 (Jensen’s Inequality). Suppose that X ∈L1.
If
φ : R →R is convex and φ(X) ∈L1, then
E (φ(X) |G ) ≥φ (E (X |G )) .
(5.6)
Proof. Any convex function φ : R →R is the supremum of a family of affine
functions, so there exists a sequence (φn) of real functions with φn(x) =
anx + bn for each n, such that φ = supn φn. Therefore φ(X) ≥anX + bn
holds a.s. for each (and hence all) n. So by the positivity of E (· |G ), we
have
E (φ(X) |G ) ≥sup
n (anE (X |G ) + bn) = φ(E (X |G )) a.s.
Proof of Proposition 5.3.3. With φ(x) = |x|p, Jensen’s inequality implies
that |E (X |G )|p ≤E (|X|p |G ), and taking expectations and pth roots on
both sides, we obtain
∥E (X |G )∥p ≤∥X∥p for all G ⊂F.
Thus the family U is Lp-bounded and hence UI.
Remark 5.3.5. Jensen’s inequality shows that the conditional expectation
operator is a contraction on Lp. The same is true for L1. Taking φ(x) = |x|,
we obtain |E (X |G )| ≤E (|X| |G ), and hence ∥E (X |G )∥1 ≤∥X∥1.
Jensen’s inequality also shows that, given p > 1 and an Lp-bounded
martingale (Mt, Ft)t∈T, the sequence (|Mt|p , Ft) is a submartingale. This
follows upon taking φ(x) = |x|p, so that by (5.6), with t ≥s, we have
E (|Mt|p |Fs ) ≥|E (Mt |Fs )|p = |Ms|p .
Here the integrability of Nt, which is required for the application of (5.6),
follows from the Lp-boundedness of Mt. Similar results follow upon apply-
ing (5.6) with φ(x) = x+ or φ(x) = (x −K)+ with suitable integrability
assumptions.

112
CHAPTER 5. DISCRETE-TIME AMERICAN OPTIONS
Martingale Convergence
We now review briefly the principal limit theorems for martingales. The
role of uniform integrability is evident from the following proposition.
Proposition 5.3.6. Suppose (Xn) is a sequence of integrable random vari-
ables and X is integrable. The following are equivalent:
a) The sequence (Xn) converges to X in the L1-norm; i.e. , ∥Xn −X∥1 =
E (|Xn −X|) →0.
b) The sequence (Xn) is UI and converges to X in probability.
See [109] or [299] for the proof of this standard result. Since a.s. con-
vergence implies convergence in probability, we also have the following.
Corollary 5.3.7. If (Xn) is UI and Xn →X a.s., then X ∈L1 and
Xn →X in L1-norm.
Thus, to prove that a UI martingale converges in L1-norm, the princi-
pal task is showing a.s. convergence. Doob’s original proof of this result
remains instructive and has been greatly simplified by the use of martin-
gale transforms. We outline here the beautifully simple treatment given
in [299], to which we refer for details.
Let t →Mt(ω) denote the sample paths of a random process M defined
on N × Ωand interpret ∆Mt = Mt −Mt−1 as ‘winnings’ per unit stake
on game t. The total winnings (‘gains process’) can be represented by the
martingale transform Y = C ·M given by a playing strategy C in which we
stake one unit as soon as M has taken a value below a, continue placing
unit stakes until M reaches values above b, after which we do not play until
M is again below a, and repeat the process indefinitely. It is ‘obvious’ (and
can be shown inductively) that C is predictable.
Let UT [a, b](ω) denote the number of ‘upcrossings’ of [a, b] by the path
t →Mt, that is, the maximal k ∈N such that there are 0 ≤s1 < t1 < s2 <
· · · < tk < T for which Msi(ω) < a and Mti(ω) > b (i = 1, 2, . . . , k). Then
YT (ω) ≥(b −a)UT [a, b](ω) −(MT (ω) −a)−
(5.7)
since Y increases by at least (b −a) during each upcrossing, while the final
term overestimates the potential loss in the final play.
Now suppose that M is a supermartingale. Since C is bounded and
non-negative, the transform Y is again a supermartingale (the results of
Chapter 2 apply here as everything is restricted to the finite time set
{0, 1, . . . , T}. Thus E (YT ) ≤E (Y0) = 0. Then (5.7) yields
(b −a)E (UT [a, b]) ≤E (MT −a)−.
(5.8)
If, moreover, M = (Mt)t∈N is L1-bounded, K = supt ∥Mt∥1 is finite, so
that
(b −a)E (UT [a, b]) ≤|a| + K.

5.3. UNIFORMLY INTEGRABLE MARTINGALES
113
The bound is independent of T, so monotone convergence implies that
(b −a)E (U∞[a, b]) < ∞,
where U∞[a, b] = limT →∞UT [a, b].
Hence {U∞[a, b] = ∞} is a P-null set; that is, every interval is ‘up-
crossed’ only finitely often by almost all paths of M. Now the set D ⊂Ω
on which Mt(ω) does not converge to a finite or infinite limit can be written
as
D =
3
{a,b∈Q:a<b}
Da,b,
where
Da,b =
$
ω : lim inf
t
Mt(ω) < a < b < lim sup
t
Mt(ω)
%
.
Since Da,b ⊂{ω : U∞[a, b] = ∞}, it follows that D is also P-null.
Thus the a.s. limit M∞exists a.s. (P) in [−∞, ∞]. By Fatou’s lemma,
∥M∞∥1 = E (lim inf |Mt|) ≤lim inf ∥Mt∥1 ≤K,
so that M∞is in L1 and consequently a.s. finite.
Finally, if the family (Mt)t∈N is a martingale and is also UI (we simply
say that M is a UI martingale), then it follows at once from Corollary 5.3.7
that Mt →M∞in L1-norm. Moreover, the martingale property ‘extends
to the limit’; that is, for all t,
Mt = E (M∞|Ft ) .
(5.9)
To see this, note that for A ∈Ft and u ≥t, the martingale property yields
4
A MudP =
4
A MsdP, while
''''

A
MtdP −

A
M∞dP
'''' ≤

A
|Mt −M∞| dP ≤∥Mt −M∞∥1 →0
as t →∞. This proves (5.9). Whenever (5.9) holds, we say that the limit
random variable M∞closes the martingale M.
To summarise, we have the following.
Theorem 5.3.8 (Martingale Convergence).
(i) If the supermartin-
gale M is bounded in L1, then M∞(ω) = limt→∞Mt(ω) exists a.s. (P)
and the random variable M∞is integrable.
(ii) If M is a UI martingale, Mt →M∞a.s. and in L1, and M∞closes
the martingale M.
(iii) If X ∈L1 and Mt = E (X |Ft ) for all t ∈N, then M is a UI
martingale and Mt →E (X |F∞) a.s. and in L1.

114
CHAPTER 5. DISCRETE-TIME AMERICAN OPTIONS
Proof. Only the final statement still requires proof; this can be found
in [299, 14.2]. Note that if F = F∞(as we assume), then Mt →X.
One immediate consequence of the convergence theorems is that for
UI martingales we can extend Definition 5.2.5 to general stopping times.
Given a UI martingale M and any stopping time τ, the random variable
Mτ(ω) = Mτ(ω)(ω) is now also well-defined on the set {τ = ∞}, on which
we set Mτ = M∞.
We extend Theorems 5.2.7 (optional sampling) and 5.2.11 (optional
stopping) to general stopping times when M is a UI martingale. In the
first place, we have the following result.
Theorem 5.3.9. Let M be a UI martingale and τ a stopping time. Then
E (M∞|Fτ ) = Mτ a.s. (P) .
(5.10)
Proof. As M∞closes M, we have Mt = E (M∞|Ft ) for all t. In addi-
tion, as τ ∧t is a bounded stopping time, Theorem 5.2.7 yields Mτ∧t =
E (Mt |Fτ∧t ). Hence E (M∞|Fτ∧t ) = Mτ∧t.
Let A ∈Fτ. The set Bt = A ∩{τ ≤t} is in Ft by definition and in Fτ
since τ is Fτ-measurable. Hence Bt ∈Fτ∧t and so

Bt
M∞dP =

Bt
Mτ∧tdP =

Bt
MτdP.
(5.11)
Assume without loss of generality that M∞(and hence each Mt) is non-
negative, and let t ↑∞. Then (5.11) shows that

A∩{τ<∞}
M∞dP =

A∩{τ<∞}
MτdP.
Since Mτ = M∞trivially on {τ = ∞}, the result follows.
Corollary 5.3.10. Let M be a UI martingale.
(i) (Optional Sampling) If σ ≤τ are stopping times, then
E (Mτ |Fσ ) = Mσ a.s. (P) .
(5.12)
(ii) (Optional Stopping) If τ is a stopping time, then Mτ ∈L1 and M τ
is a UI martingale. In particular, E (Mτ) = E (M0).
Doob Decomposition and Quadratic Variation
Again let (Ω, F, P, N, F) be a stochastic basis, and let X = (Xt)t∈T be an
F-adapted process. Since martingales describe what we might call ‘purely
random’ behaviour, it is natural to ask to what extent the ‘martingale part’
of X can be isolated from the ‘long-term trends’ that X exhibits. In discrete
time, this is easily accomplished; remarkably there is also such a decompo-
sition in continuous time (the Doob-Meyer decomposition, see [109], [199]).
This fact underlies the success of general stochastic integration and the
success of martingale methods in continuous-time finance.

5.3. UNIFORMLY INTEGRABLE MARTINGALES
115
Definition 5.3.11. Given an adapted sequence X = (Xt) of random vari-
ables on (Ω, F, P), construct the stochastic processes M and A by setting
M0 = 0,
∆Mt = Mt −Mt−1 = Xt −E (Xt |Ft−1 ) for t > 0,
A0 = 0,
∆At = At −At−1 = E (Xt |Ft−1 ) −Xt−1 for t > 0.
Adding terms for s ≤t, it is clear that
Xt = X0 + Mt + At for all t ≥0.
(5.13)
We call this the Doob decomposition of the adapted process X.
It is clear that At is Ft−1-measurable, so that A is predictable. The
process M is a martingale null at 0 since E (∆Mt |Ft−1 ) = 0. Thus we
have
E (∆Xt |Ft−1 ) = ∆At for all t > 0.
(5.14)
By construction, ∆Mt + ∆At = ∆Xt for all t > 0.
The Doob decomposition is unique in the following sense. If we also
have X −X0 = M ′ + A′ for some martingale M ′ and predictable process
A′, then M + A = X −X0 = M ′ + A′, so that M −M ′ = A′ −A is a
predictable martingale. Such a process must be constant, as we saw in
Chapter 2. Hence (up to some fixed P-null set N, for all t ∈N) equation
(5.13) is the unique decomposition of an adapted process X into the sum
of its initial value, a martingale, and a predictable process A, both null at
0.
When X is a submartingale, equation (5.14) shows that ∆At ≥0, so
that t →At(ω) is increasing in t, for almost all ω ∈Ω. This increasing
predictable process A therefore has an a.s. limit A∞(which can take the
value +∞in general).
Now consider the special case where X = M 2 and M is an L2-bounded
martingale with M0 = 0; then M 2 is a submartingale by Jensen’s inequal-
ity (5.6) (see Remark 5.3.5). The Doob decomposition M 2 = N+A consists
of a UI martingale N and a predictable increasing process A, both null at
0. Define A∞= limt↑∞At a.s. We have
E

M 2
t

= E (Nt) + E (At) = E (At) for all t ∈N,
and these quantities are bounded precisely when A∞∈L1.
Observe, using (5.14), that, since M is a martingale,
∆At = E

M 2
t −M 2
t−1

|Ft−1

= E

(∆Mt)2 |Ft−1

.
(5.15)
For this reason, we call A the quadratic variation of M and write A = ⟨M⟩.
We have shown that an L2-bounded martingale has integrable quadratic
variation.

116
CHAPTER 5. DISCRETE-TIME AMERICAN OPTIONS
Remark 5.3.12. In Chapters 6 to 8, we make fuller use of the preceding
results in the continuous-time setting. The translation of the convergence
theorems so that they apply to continuous-time UI martingales is straight-
forward (though somewhat tedious) once one has established that such a
martingale M, with time set [0, T] or [0, ∞), always possesses a ‘version’
almost all of whose paths t →Mt(ω) are right-continuous and have left
limits. This enables one to use countable dense subsets to approximate
the path behaviour and use the results just presented; see [109], [199] for
details. With the interpretation of T as an interval in R+, the convergence
theorems and the optional sampling and optional stopping results proved in
the foregoing go over verbatim to the continuous-time setting. We assume
this in Chapter 6 and beyond.
Of particular importance in continuous time is the analogue of the Doob
decomposition, the Doob-Meyer decomposition of a sub- (or super-) mar-
tingale; we briefly outline its principal features without proof (see [109] for
a full treatment). We discuss the Doob-Meyer decomposition further when
introducing Itˆo processes in Chapter 6; we will make essential use of the
decomposition when analysing American put options in Chapter 8.
If T = [0, ∞) and X = (Xt) is a supermartingale with right-continuous
paths t →Xt(ω) for P-almost all ω ∈Ω, then we say that X is of class
D if the family {Xτ : τ is a stopping time} is UI. If X is a UI martingale,
this is automatic from Theorem 5.3.9, but this is not generally the case for
supermartingales. Every such supermartingale has decomposition
Xt = Mt −At,
where M is a UI martingale and the increasing process A has A0 = 0
and is predictable. In continuous time, this definition requires that A be
measurable with respect to the σ-field P on [0, ∞)×Ωthat is generated by
the continuous processes. The Doob-Meyer decomposition is unique up to
indistinguishability (see Definition 6.1.12), and the process A is integrable.
Given an L2-bounded (hence UI) martingale M, the decomposition
again defines a quadratic variation for the submartingale M 2 = N + A,
and we write A = ⟨M⟩. Note that since M is a martingale, (5.15) also
holds in this setting, which justifies the terminology.
Of particular in-
terest to us are martingales whose quadratic variation is non-random; we
shall find (Chapter 6) that Brownian motion W is a martingale such that
⟨W⟩t = t.
5.4
Optimal Stopping: The Snell Envelope
American Options
We return to our consideration of American options on a finite discrete
time set. Consider a price process S =

S0, S1
consisting of a riskless
bond S0
t = (1+r)t and a single risky stock (S1
t )t∈T, where T = {0, 1, . . . , T}

5.4. OPTIMAL STOPPING: THE SNELL ENVELOPE
117
for finite T > 0 and r > 0, defined on a probability space (Ω, F, P). We
have seen that the holder’s freedom to choose the exercise date (without
prescience) requires the option writer (seller) of an American call option
with strike K to hedge against a liability of (S1
τ −K)+ at a (random)
stopping time τ : Ω→T.
Thus, if the system is in state ω ∈Ω, and
if τ(ω) = t, the liability is

S1
t (ω) −K
+. In general, both the stopping
time and the liability vary with ω. We write T = TT for the class of all T-
valued stopping times. Since T is assumed finite, we can restrict attention
to bounded stopping times for the present, and hence Theorems 5.2.7 and
5.2.11 apply to this situation.
Suppose that the writer tries to construct a hedging strategy θ = (θ0, θ1)
to guard against the potential liability. This will generate a value process
V (θ) with
Vt(θ) = V0(θ) +

u≤t
θu · ∆Su = V0(θ) +

u≤t
(θ0
u∆S0
u + θ1
u∆S1
0).
The strategy should be self-financing, so we also demand that (∆θt)·St−1 =
0 for t ≥1.
We assume that the model is viable and that Q is an EMM for S. Then
the discounted value process M = V (θ) is a martingale under (F, Q) and
by Theorem 5.2.7 we conclude that
V0(θ) = M0 = EQ

V τ(θ)

= EQ

(1 + r)−τVτ(θ)

.
(5.16)
Note that, since τ is a random variable, we cannot now take the term
(1 + r)−τ outside the expectation as in the case of European options.
Hence, if the writer is to hedge successfully against the preceding lia-
bility, the initial capital required for this portfolio is EQ ((1 + r)−τVτ(θ)).
This holds for every τ ∈T. But since we need Vτ(θ) ≥(Sτ −K)+, the
initial outlay x with which to form the strategy θ must satisfy
x ≥sup
τ∈T
EQ

(1 + r)−τ(S1
τ −K)+
.
(5.17)
More generally, given an American option, we saw in Section 5.1 that its
payofffunction is a random sequence ft = ft(S1) of functions that (in
general) depend on the path taken by S1. The initial capital x needed for
a hedging strategy satisfies
x ≥sup
τ∈T
EQ

(1 + r)−τfτ

.
If we can find a self-financing strategy θ and a stopping time τ ∗∈T such
that Vτ ∗(θ) = fτ ∗almost surely, then the initial capital required is exactly
x = sup
τ∈T
EQ

(1 + r)−τfτ

= EQ

(1 + r)−τ ∗fτ ∗

.
(5.18)

118
CHAPTER 5. DISCRETE-TIME AMERICAN OPTIONS
Recall from Section 5.1 that a hedging strategy (or simply a hedge) is a
self-financing strategy θ that generates a value process Vt(θ) ≥ft a.s. (Q)
for all t ∈T, and we say that the hedge θ is minimal if there exists a
stopping time τ ∗with Vτ ∗(θ) = fτ ∗a.s. (Q). Thus (5.18) is necessary for
the existence of a minimal hedge θ, and we show that it is also sufficient.
This justifies calling x the rational price of the American option with payoff
function f.
To see how the value process V (θ) changes in each underlying single-
period model, we again consider the problem faced by the option writer
but work backwards in time from the expiry date T. Since fT is the value
of the option at time T, the hedge must yield at least VT = fT in order
to cover exercise at that time. At time T −1, the option holder has the
choice either to exercise immediately or to hold the option until time T.
The time T −1 value of the latter choice is
(1 + r)−1fT = S0
T −1EQ

f T |FT −1

;
recall that we write Y t = βtYt = (S0
t )−1Yt for the discounted value of any
quantity Yt. Thus the option writer needs income from the hedge to cover
the potential liability max

fT −1, S0
T −1EQ

f T |FT −1

, so this quantity is
a rational choice for VT −1(θ). Inductively, we obtain
Vt−1(θ) = max

ft−1, S0
t−1EQ (Vt |Ft−1 )

for t = 1, 2, . . . , T.
(5.19)
In particular, if βt = (1+r)t for some constant interest rate r > 0, equation
(5.19) simplifies to
Vt−1(θ) = max

ft−1, (1 + r)−1EQ (Vt |Ft−1 )

for t = 1, 2, . . . , T. (5.20)
The option writer’s problem is to construct such a hedge.
The Snell Envelope
Adapting the treatment given in [236], we now solve this problem in a more
abstract setting in order to focus on its essential features; given a finite
adapted sequence (Xt)t∈T of non-negative random variables on (Ω, F, Q),
we show that the optimisation problem of determining supτ∈T EQ (Xτ)
can be solved by the inductive procedure suggested previously and that
the optimal stopping time τ ∗∈T can be described in a very natural way.
Definition 5.4.1. Given (Xt)t∈T with Xt ≥0 a.s. for all t, define a new
adapted sequence (Zt)t∈T by backward induction by setting
ZT = XT ,
Zt−1 = max {Xt−1, EQ (Zt |Ft−1 )} for t = 1, 2, . . . , T. (5.21)
We call Z the Snell envelope of the finite sequence (Xt).

5.4. OPTIMAL STOPPING: THE SNELL ENVELOPE
119
The sequence (Zt)t∈T is clearly adapted to the filtration F = (Ft)t∈T. In
the following, we give a more general definition, applicable also to infinite
sequences.
Note that (Zt) is defined ‘backwards in time’. It is instructive to read
the definition with a ‘forward’ time variable using the time to maturity
s = T −t. Then the definitions (5.21) become
ZT = XT ,
ZT −s = max {XT −s, EQ (ZT −s+1 |FT −s )} for s = 1, 2, . . . , T.
We now examine the properties of the process Z.
Proposition 5.4.2. Let (Zt)t∈T be the Snell envelope of a process (Xt)t∈T
with Xt ≥0 a.s. for all t.
(i) The process Z is the smallest (F, Q)-supermartingale dominating X.
(ii) The random variable τ ∗= min {t ≥0 : Zt = Xt} is a stopping time,
and the stopped process Zτ ∗defined by Zτ ∗
t
= Zt∧τ ∗is an (F, Q)-
martingale.
Proof. From (5.21) we deduce that Zt ≥Xt for t ∈T; hence Z dominates
X. Since
Zt−1 ≥EQ (Zt |Ft−1 ) for all t = 1, 2, . . . , T,
the process Z is also a supermartingale.
To see that it is the smallest such supermartingale, we argue by back-
ward induction.
Suppose that Y
= (Yt) is any supermartingale with
Yt ≥Xt for all t ∈T. Clearly, YT ≥XT = ZT . Now if Yt ≥Zt for a
fixed t ∈T, then we have Yt−1 ≥EQ (Yt |Ft−1 ) since Y is a supermartin-
gale. It follows from the positivity of the conditional expectation operator
that Yt−1 ≥EQ (Zt |Ft−1 ). On the other hand, Y dominates X; hence
Yt−1 ≥Xt−1. Therefore
Yt−1 ≥max {Xt−1, EQ (Zt |Ft−1 )} = Zt−1,
which completes the induction step. The first assertion of the proof follows.
For the second claim, note that Z0 = max {X0, EQ (Z1 |F0 )}, and
{τ ∗= 0} = {Z0 = X0} ∈F0 since X0 and Z0 are F0-measurable.
By
the definition of τ ∗, we have
{τ ∗= t} =
t−1
0
s=0
{Zs > Xs} ∩{Zt = Xt} for t = 1, 2, . . . , T.
This set belongs to Ft since X and Z are adapted. Thus τ ∗is a stopping
time. Note that τ ∗(ω) ≤T a.s.
To see that the stopped process Zτ ∗
t
= Zt∧τ ∗defines a martingale, we
again use a martingale transform, as in the proof of Theorem 5.2.11. Define
φt = 1{τ ∗≥t} for t = 1, 2, . . . , T;

120
CHAPTER 5. DISCRETE-TIME AMERICAN OPTIONS
the process φ is predictable since {τ ∗≥t} = Ω\ {τ ∗< t}. Moreover,
Zτ ∗
t
= Z0 +
t

u=1
φu∆Zu for t = 1, 2, . . . , T.
Now, for t = 1, 2, . . . , T, we have
Zτ ∗
t
−Zτ ∗
t−1 = φt(Zt −Zt−1) = 1{τ ∗≥t}(Zt −Zt−1);
if τ ∗(ω) ≥t, then Zt−1(ω) > Xt−1(ω), so that Zt−1(ω) = EQ (Zt |Ft−1 ) (ω)
on this set. For all t = 1, 2, . . . , T, we therefore have
EQ

Zτ ∗
t
−Zτ ∗
t−1

|Ft−1

= 1{τ ∗≥t}EQ ((Zt −EQ (Zt |Ft−1 )) |Ft−1 ) = 0.
Thus the stopped process Zτ ∗is a martingale on (Ω, F, Q). Recall that we
assume that the σ-field F0 is trivial, so that it contains only Q-null sets
and their complements (in the case of a finite market model, this reduces
to F0 = {∅, Ω}). Therefore X0 and Z0 are a.s. constant since both are
F0-measurable.
Definition 5.4.3. We call a stopping time σ ∈T = TT optimal for (Xt)t∈T
if
EQ (Xσ) = sup
t∈T
EQ (Xτ) .
(5.22)
Proposition 5.4.4. Let (Zt)t∈T be the Snell envelope of a process (Xt)t∈T
with Xt ≥0 a.s. for all t. The stopping time τ ∗= min {t ≥0 : Zt = Xt}
is optimal for X, and
Z0 = EQ (Xτ ∗) = sup
τ∈T
EQ (Xτ) .
(5.23)
Proof. Since Zτ ∗is a martingale, we have
Z0 = Zτ ∗
0
= EQ

Zτ ∗
T

= EQ (Zτ ∗) = EQ (Xτ ∗) ,
where the final equality follows from the definition of τ ∗. On the other
hand, given any τ ∈T, we know from Proposition 5.4.2 that Zτ is a super-
martingale. Hence
Z0 = EQ (Zτ
0 ) ≥EQ (Zτ) ≥EQ (Xτ)
since Z dominates X.
Characterisation of Optimal Stopping Times
We are now able to describe how the martingale property characterises
optimality more generally. Let (Zt)t∈T be the Snell envelope of a process
(Xt)t∈T with Xt ≥0 a.s. for all t.

5.4. OPTIMAL STOPPING: THE SNELL ENVELOPE
121
Proposition 5.4.5. The stopping time σ ∈T is optimal for X if and only
if the following two conditions hold.
(i) Zσ = Xσ a.s. (Q) .
(ii) Zσ is an (F,Q)-martingale.
Proof. If Zσ is a martingale, then
Z0 = EQ (Zσ
0 ) = EQ (Zσ
T ) = EQ (Zσ) = EQ (Xσ) ,
where the final step uses condition 1. On the other hand, Zτ is a super-
martingale for τ ∈T. Hence
Z0 = EQ (Zτ
0 ) ≥EQ (Zτ
T ) = EQ (Zτ) ≥EQ (Xτ) ,
as Z dominates X. Since σ ∈T, it follows that σ is optimal.
Conversely, suppose that σ is optimal for X. By Proposition 5.4.4, we
have Z0 = supτ∈T EQ (Xτ); it follows that Z0 = EQ (Xσ) ≤EQ (Zσ) since
Z dominates X.
However, Zσ is a supermartingale, so EQ (Zσ) ≤Z0.
In other words, for any optimal σ, EQ (Xσ) = Z0 = EQ (Zσ).
But Z
dominates X, and thus Xσ = Zσ a.s. (Q). This proves condition 1 above.
Now observe that we have Z0 = EQ (Zσ) as well as
Z0 ≥EQ (Zσ∧t) ≥EQ (Zσ)
since Zσ is a supermartingale. Hence
EQ (Zσ∧t) = EQ (Zσ) = EQ(EQ (Zσ |Ft )).
Again because Z is a supermartingale, we also have, by Theorem 5.2.7,
that
Zσ∧t ≥EQ (Zσ |Ft ) ,
so that again Zσ∧t = EQ (Zσ |Ft ). This means that Zσ is in fact a mar-
tingale.
From Proposition 5.4.5, it is clear that τ ∗is the smallest optimal stop-
ping time for X since by definition it is the smallest stopping time such
that Zτ ∗= Xτ ∗a.s. (Q). To find the largest optimal stopping time for X,
we look for the first time that the increasing process A in the Doob decom-
position of Z ‘leaves zero’; that is, the time ν at which the stopped process
Zν ceases to be a martingale.
Since Z is a supermartingale, its Doob decomposition Z = Z0 + N + B
has N as a martingale and B as a predictable decreasing process, both null
at 0. Let M = Z0 + N, which is a martingale, since Z0 is a.s. constant,
and set A = −B, so that A = (At)t∈T is increasing, with A0 = 0, and
Z = M −A.

122
CHAPTER 5. DISCRETE-TIME AMERICAN OPTIONS
Define a random variable ν : Ω→T by
ν(ω) =

T
if AT (ω) = 0,
min {t ≥0 : At+1 > 0}
if AT (ω) > 0.
(5.24)
To see that ν ∈T, simply observe that
{ν = t} =
0
s≤t
{As = 0} ∩{At+1 > 0}
is in Ft because At+1 is Ft-measurable. Thus ν is a stopping time. It is
clearly T-valued and therefore bounded.
Proposition 5.4.6. The stopping time ν in (5.24) is the largest optimal
stopping time for X.
Proof. For s ≤ν(ω), Zs(ω) = Ms(ω) −As(ω). Hence Zν is a martingale,
so that the second condition in Proposition 5.4.5 holds for ν. To verify the
first condition (i.e. , Zν = Xν), let us write Zν in the form
Zν =
T

s=0
1{ν=s}Zs =
T −1

s=0
1{ν=s} max {Xs, E (Zs+1 |Fs )} + 1{ν=T }Xt.
Now
E (Zs+1 |Fs ) = E (Ms+1 −As+1 |Fs ) = Ms −As+1.
On the set {ν = s}, we have As = 0 and As+1 > 0; hence Zs = Ms. This
means that, on this set, E (Zs+1 |Fs ) < Zs a.s., and therefore that Zs =
max {Xs, E (Zs+1 |Fs )} = Xs. Thus Zν = Xν a.s.; hence ν is optimal.
It is now clear that ν is the largest optimal time for (Xt). Indeed, if
τ ∈T has τ ≥ν and Q(τ > ν) > 0, then
E (Zτ) = E (Mτ) −E (Aτ) = E (Z0) −E (Aτ) < E (Z0) = Z0.
By (5.23), the stopping time τ cannot be optimal.
Extension to Unbounded Stopping Times
We need to consider value processes at arbitrary times t ∈T since the
holder’s possible future actions from time t onwards will help to deter-
mine those processes. So let Tt denote the set of stopping times τ : Ω→
Tt = {t, t + 1, . . . , T}, and consider instead the optimal stopping problem
supτ∈Tt E (Xτ). Although the stopping times remain bounded, an immedi-
ate difficulty in attempting to transfer the results we have for t = 0 to more
general t ∈T is that we made use in our proofs of the fact that Z0 was a.s.
constant. This followed from our assumption that F0 contained only null
sets and their complements, and it led us to establish (5.23), which we used
throughout.

5.4. OPTIMAL STOPPING: THE SNELL ENVELOPE
123
In the general case, we are obliged to replace expectations EQ (Zτ) by
conditional expectations EQ (Zτ |Ft ), thus facing the problem of defining
the supremum of a family of random variables rather than real numbers.
We need to ensure that we obtain this supremum as an F-measurable func-
tion, even for an uncountable family. We use this opportunity to extend
the definition of the Snell envelope in preparation for a similar extension
to continuous-time situations needed in Chapter 8.
Proposition 5.4.7. Let (Ω, F, P) be a probability space. Let L be a fam-
ily of F-measurable functions Ω→[−∞, ∞]. There exists a unique F-
measurable function g : Ω→[−∞, ∞] with the following properties:
(i) g ≥f a.s. for all f ∈L.
(ii) If an F-measurable function h satisfies h ≥f a.s. for all f ∈L, then
h ≥g a.s.
We call g the essential supremum of L and write g = ess supf∈L f.
There exists a sequence (fn) such that g = supn fn. If L is upward filtering
(i.e., if for given f ′, f ′′ in L there exists f ∈L with f ≥max {f ′, f ′′}), then
the sequence (fn) can be chosen to be increasing, so that f = limn fn.
Proofs of this result can be found in [199], [236]. The idea is simple:
identify the closed intervals [0, 1] and [−∞, ∞], for example, via the in-
creasing bijection x →ex. Any countable family C in L has a well-defined
F-measurable ([0, 1]-valued) fC, which thus has finite expectation under P.
Define
α = sup {E (fC) : C ⊂L, C countable}
and choose a sequence (f ′
n, Cn) with E (f ′
n) →α.
Since K = +
n Cn is
countable and E (f ′
K) = α, we can set g = f ′
K. The sequence (f ′
n) serves
as an approximating sequence, and f0 = f ′
0, fn+1 ≥fn ∨f ′
n+1 will make it
increasing with n.
Definition 5.4.8. Let (Ω, F, T, F, P) be a stochastic base with T = N.
Given an adapted process (Xt)t∈T such that X∗= supt Xt ∈L1, define Tt
as the family of F-stopping times τ such that t ≤τ < ∞. We call τ ∈Tt a
t-stopping rule. The Snell envelope of (Xt) is the process Z defined by
Zt = ess sup
τ∈Tt
E (Xτ |Ft ) for t ∈T.
(5.25)
This definition allows unbounded (but a.s. finite) stopping times. When
X is UI, we can still use the optional stopping results proved earlier in this
context. The martingale characterisation of optimal stopping times can be
extended as well; see [199] or [236] for details.

