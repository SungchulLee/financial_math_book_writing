# Financial Markets & Stochastic Processes

!!! info "Source"
    **Quantitative Finance for Physicists: An Introduction** by Belal E. Baaquie, Academic Press, 2004.
    These notes are used for educational purposes.

## Introduction

Chapter 1
Introduction
This book is written for those physicists who want to work on Wall
Street but have not bothered to read anything about Finance. This is
a crash course that the author, a physicist himself, needed when he
landed a financial data analyst job and became fascinated with the
huge data sets at his disposal. More broadly, this book addresses the
reader with some background in science or engineering (college-level
math helps) who is willing to learn the basic concepts and quantitative
methods used in modern finance.
The book loosely consists of two parts: the ‘‘applied’’ part and the
‘‘academic’’ one. Two major fields, Econometrics and Mathematical
Finance, constitute the applied part of the book. Econometrics can be
broadly defined as the methods of model-based statistical inference in
financial economics [1]. This book follows the traditional definition
of Econometrics that focuses primarily on the statistical analysis of
economic and financial time series [2]. The other field is Mathematical
Finance [3, 4]. This term implies that finance has given a rise to
several
new
mathematical
theories.
The
leading
directions
in
Mathematical
Finance
include
portfolio
theory,
option-pricing
theory, and risk measurement.
The ‘‘academic’’ part of this book demonstrates that financial data
can be an area of exciting theoretical research, which might be of
interest to physicists regardless of their career motivation. This part
includes the Econophysics topics and the agent-based modeling of
1

financial markets.1 Physicists use the term Econophysics to emphasize
the concepts of theoretical physics (e.g., scaling, fractals, and chaos)
that are applied to the analysis of economic and financial data. This
field was formed in the early 1990s, and it has been growing rapidly
ever since. Several books on Econophysics have been published to date
[5–11] as well as numerous articles in the scientific periodical journals
such as Physica A and Quantitative Finance.2 The agent-based model-
ing of financial markets was introduced by mathematically inclined
economists (see [12] for a review). Not surprisingly, physicists, being
accustomed to the modeling of ‘‘anything,’’ have contributed into this
field, too [7, 10].
Although physicists are the primary audience for this book, two
other reader groups may also benefit from it. The first group includes
computer science and mathematics majors who are willing to work (or
have recently started a career) in the finance industry. In addition, this
book may be of interest to majors in economics and finance who are
curious about Econophysics and agent-based modeling of financial
markets. This book can be used for self-education or in an elective
course on Quantitative Finance for science and engineering majors.
The book is organized as follows. Chapter 2 describes the basics of
financial markets. Its topics include market price formation, returns
and dividends, and market efficiency. The next five chapters outline
the theoretical framework of Quantitative Finance: elements of math-
ematical statistics (Chapter 3), stochastic processes (Chapter 4), time
series analysis (Chapter 5), fractals (Chapter 6), and nonlinear dy-
namical systems (Chapter 7). Although all of these subjects have been
exhaustively covered in many excellent sources, we offer this material
for self-contained presentation.
In Chapter 3, the basic notions of mathematical statistics are
introduced and several popular probability distributions are listed.
In particular, the stable distributions that are used in analysis of
financial time series are discussed.
Chapter 4 begins with an introduction to the Wiener process, which
is the basis for description of the stochastic financial processes. Three
methodological approaches are outlined: one is rooted in the generic
Markov process, the second one is based on the Langevin equation,
and the last one stems from the discrete random walk. Then the basics
of stochastic calculus are described. They include the Ito’s lemma and
2
Introduction

the stochastic integral in both the Ito and the Stratonovich forms.
Finally, the notion of martingale is introduced.
Chapter 5 begins with the univariate autoregressive and moving
average models, the classical tools of the time series analysis. Then the
approaches to accounting for trends and seasonality effects are dis-
cussed. Furthermore, processes with non-stationary variance (condi-
tional heteroskedasticity) are described. Finally, the specifics of the
multivariate time series are outlined.
In Chapter 6, the basic definitions of the fractal theory are dis-
cussed. The concept of multifractals, which has been receiving a lot of
attention in recent financial time series research, is also introduced.
Chapter 7 describes the elements of nonlinear dynamics that are
important for agent-based modeling of financial markets. To illustrate
the major concepts in this field, two classical models are discussed: the
discrete logistic map and the continuous Lorenz model. The main
pathways to chaos and the chaos measures are also outlined.
Those readers who do not need to refresh their knowledge of the
mathematical concepts may skip Chapters 3 through 7.3
The other five chapters are devoted to financial applications. In
Chapter 8, the scaling properties of the financial time series are
discussed. The main subject here is the power laws manifesting in
the distributions of returns. Alternative approaches in describing the
scaling properties of the financial time series including the multifrac-
tal models are also outlined.
The next three chapters, Chapters 9 through 11, relate specifically
to Mathematical Finance. Chapter 9 is devoted to the option pricing.
It starts with the general properties of stock options, and then the
option pricing theory is discussed using two approaches: the method
of the binomial trees and the classical Black-Scholes theory.
Chapter 10 is devoted to the portfolio theory. Its basics include the
capital asset pricing model and the arbitrage pricing theory. Finally,
several arbitrage trading strategies are listed. Risk measurement is the
subject of Chapter 11. It starts with the concept of value at risk, which
is widely used in risk management. Then the notion of coherent risk
measure is introduced and one such popular measure, the expected
tail losses, is described.
Finally, Chapter 12 is devoted to agent-based modeling of financial
markets.
Two
elaborate
models
that
illustrate
two
different
Introduction
3

approaches to defining the price dynamics are described. The first one
is based on the supply-demand equilibrium, and the other approach
employs an empirical relation between price change and excess
demand. Discussion of the model derived in terms of observable
variables concludes this chapter.
The bibliography provides the reader with references for further
reading rather than with a comprehensive chronological review. The
reference list is generally confined with recent monographs and
reviews. However, some original work that either has particularly
influenced the author or seems to expand the field in promising
ways is also included.
In every chapter, exercises with varying complexity are provided.
Some of these exercises simply help the readers to get their hands on
the financial market data available on the Internet and to manipulate
the data using Microsoft Excel software.4 Other exercises provide a
means of testing the understanding of the book’s theoretical material.
More challenging exercises, which may require consulting with ad-
vanced textbooks or implementation of complicated algorithms, are
denoted with an asterisk. The exercises denoted with two asterisks
offer discussions of recent research reports. The latter exercises may
be used for seminar presentations or for course work.
A few words about notations. Scalar values are denoted with the
regular font (e.g., X) while vectors and matrices are denoted with
boldface letters (e.g., X). The matrix transposes are denoted with
primes (e.g., X0) and the matrix determinants are denoted with vertical
bars (e.g., jXj). The following notations are used interchangeably:
X(tk)  X(t) and X(tk1)  X(t  1). E[X] is used to denote the ex-
pectation of the variable X.
The views expressed in this book may not reflect the views of my
former and current employers. While conducting the Econophysics
research and writing this book, I enjoyed support from Blake LeBaron,
Thomas Lux, Sorin Solomon, and Eugene Stanley. I am also indebted
to anonymous reviewers for attentive analysis of the book’s drafts.
Needless to say, I am solely responsible for all possible errors present in
this edition. I will greatly appreciate all comments about this book;
please send them to a_b_schmidt@hotmail.com.
Alec Schmidt
Cedar Knolls, NJ, June 2004
4
Introduction


## Financial Markets

Chapter 2
Financial Markets
This chapter begins with a description of market price formation. The
notion of return that is widely used for analysis of the investment
efficiency is introduced in Section 2.2. Then the dividend effects on
return and the present-value pricing model are described. The next big
topic is market efficiency (Section 2.3). First, the notion of arbitrage is
defined. Then the Efficient Market Hypothesis, both the theory and
its critique, are discussed. The pathways for further reading in Section
2.4 conclude the chapter.
2.1 MARKET PRICE FORMATION
Millions of different financial assets (stocks, bonds, currencies,
options, and others) are traded around the world. Some financial
markets are organized in exchanges or bourses (e.g., New York
Stock Exchange (NYSE)). In other, so-called over-the-counter
(OTC) markets, participants operate directly via telecommunication
systems. Market data are collected and distributed by markets them-
selves and by financial data services such as Bloomberg and Reuters.
Modern electronic networks facilitate access to huge volumes of
market data in real time.
Market prices are formed with the trader orders (quotes) submitted
on the bid (buy) and ask (sell) sides of the market. Usually, there is a
5

spread between the best (highest) bid and the best (lowest) ask prices,
which provides profits for the market makers. The prices seen on the
tickers of TV networks and on the Internet are usually the transaction
prices that correspond to the best prices. The very presence of trans-
actions implies that some traders submit market orders; they buy at
current best ask prices and sell at current best bid prices. The trans-
action prices represent the mere tip of an iceberg beneath which prices
of the limit orders reside. Indeed, traders may submit the sell orders at
prices higher than the best bid and the buy orders at prices lower than
the best ask. The limit orders reflect the trader expectations of future
price movement. There are also stop orders designated to limit pos-
sible losses. For an asset holder, the stop order implies selling assets if
the price falls to a predetermined value.
Holding assets, particularly holding derivatives (see Section 9.1), is
called long position. The opposite of long buying is short selling, which
means selling assets that the trader does not own after borrowing
them from the broker. Short selling makes sense if the price is
expected to fall. When the price does drop, the short seller buys the
same number of assets that were borrowed and returns them to the
broker. Short sellers may also use stop orders to limit their losses in
case the price grows rather than falls. Namely, they may submit the
stop order for triggering a buy when the price reaches a predeter-
mined value.
Limit orders and stop orders form the market microstructure: the
volume-price distributions on the bid and ask sides of the market. The
concept market liquidity is used to describe price sensitivity to market
orders. For instance, low liquidity means that the number of securities
available at the best price is smaller than a typical market order. In this
case, a new market order is executed within a range of available prices
rather than at a single best price. As a result, the best price changes its
value. Securities with very low liquidity may have no transactions and
few (if any) quotes for some time (in particular, the small-cap stocks off
regular trading hours). Market microstructure information usually is
not publicly available. However, the market microstructure may be
partly revealed in the price reaction to big block trades.
Any event that affects the market microstructure (such as submis-
sion, execution, or withdrawal of an order) is called a tick. Ticks are
recorded along with the time they are submitted (so-called tick-by-tick
6
Financial Markets

data). Generally, tick-by-tick data are not regularly spaced in time,
which leads to additional challenges for high-frequency data analysis
[1, 2]. Current research of financial data is overwhelmingly conducted
on the homogeneous grids that are defined with filtering and aver-
aging tick-by-tick data.
Another problem that complicates analysis of long financial time
series is seasonal patterns. Business hours, holidays, and even daylight
saving time shifts affect market activity. Introducing the dummy
variables into time series models is a general method to account for
seasonal effects (see Section 5.2). In another approach, ‘‘operational
time’’ is employed to describe the non-homogeneity of business activ-
ity [2]. Non-trading hours, including weekends and holidays, may be
cut off from operational time grids.
2.2 RETURNS AND DIVIDENDS
2.2.1 SIMPLE AND COMPOUNDED RETURNS
While price P is the major financial variable, its logarithm,
p ¼ log (P) is often used in quantitative analysis. The primary reason
for using log prices is that simulation of a random price innovation
can move price into the negative region, which does not make sense.
In the mean time, negative logarithm of price is perfectly acceptable.
Another important financial variable is the single-period return (or
simple return) R(t) that defines the return between two subsequent
moments t and t1. If no dividends are paid,
R(t) ¼ P(t)=P(t  1)  1
(2:2:1)
Return is used as a measure of investment efficiency.1 Its advantage is
that some statistical properties, such as stationarity, may be more
applicable to returns rather than to prices [3]. The simple return of a
portfolio, Rp(t), equals the weighed sum of returns of the portfolio
assets
Rp(t) ¼
X
N
i¼1
wipRip(t),
X
N
i¼1
wip ¼ 1,
(2:2:2)
where Rip and wip are return and weight of the i-th portfolio asset,
respectively; i ¼ 1, . . . , N.
Financial Markets
7

The multi-period returns, or the compounded returns, define the
returns between the moments t and t  k þ 1. The compounded
return equals
R(t, k) ¼ [R(t) þ 1] [R(t  1) þ 1] . . . [R(t  k þ 1) þ 1] þ 1
¼ P(t)=P(t  k) þ 1
(2:2:3)
The return averaged over k periods equals
ˇR(t, k) ¼
Y
k1
i¼0
(R(t  i) þ 1)
"
#1=k
1
(2:2:4)
If the simple returns are small, the right-hand side of (2.2.4) can be
reduced to the first term of its Taylor expansion:
ˇR(t, k)  1
k
X
k1
i¼1
R(t, i)
(2:2:5)
The continuously compounded return (or log return) is defined as:
r(t) ¼ log [R(t) þ 1] ¼ p(t)  p(t  1)
(2:2:6)
Calculation of the compounded log returns is reduced to simple
summation:
r(t, k) ¼ r(t) þ r(t  1) þ . . . þ r(t  k þ 1)
(2:2:7)
However, the weighing rule (2.2.2) is not applicable to the log returns
since log of sum is not equal to sum of logs.
2.2.2 DIVIDEND EFFECTS
If dividends D(t þ 1) are paid within the period [t, t þ 1], the simple
return (see 2.2.1) is modified to
R(t þ 1) ¼ [P(t þ 1) þ D(t þ 1) ]=P(t)  1
(2:2:8)
The compounded returns and the log returns are calculated in the
same way as in the case with no dividends.
Dividends play a critical role in the discounted-cash-flow (or pre-
sent-value) pricing model. Before describing this model, let us intro-
duce the notion of present value. Consider the amount of cash K
invested in a risk-free asset with the interest rate r. If interest is paid
8
Financial Markets

every time interval (say every month), the future value of this cash
after n periods is equal to
FV ¼ K(1 þ r)n
(2:2:9)
Suppose we are interested in finding out what amount of money will
yield given future value after n intervals. This amount (present value)
equals
PV ¼ FV=(1 þ r)n
(2:2:10)
Calculating the present value via the future value is called discounting.
The notions of the present value and the future value determine the
payoff of so-called zero-coupon bonds. These bonds sold at their
present value promise a single payment of their future value at ma-
turity date.
The discounted-cash-flow model determines the stock price via its
future cash flow. For the simple model with the constant return
E[R(t) ] ¼ R, one can rewrite (2.2.8) as
P(t) ¼ E[{P(t þ 1) þ D(t þ 1)}=(1 þ R)]
(2:2:11)
If this recursion is repeated K times, one obtains
P(t) ¼ E
X
K
i¼1
D(t þ i)=(1 þ R)i
"
#
þ E[P(t þ K)=(1 þ R)K]
(2:2:12)
In the limit K ! 1, the second term in the right-hand side of (2.2.12)
can be neglected if
lim
K!1 E[P(t þ K)=(1 þ R)K] ¼ 0
(2:2:13)
Then the discounted-cash-flow model yields
PD(t) ¼ E
X
1
i¼1
D(t þ i)=(1 þ R)i
"
#
(2:2:14)
Further simplification of the discounted-cash-flow model is based on
the assumption that the dividends grow linearly with rate G
E[D(t þ i) ] ¼ (1 þ G)iD(t)
(2:2:15)
Then (2.2.14) reduces to
Financial Markets
9

PD(t) ¼ 1 þ G
R  G D(t)
(2:2:16)
Obviously, equation (2.2.16) makes sense only for R > G. The value
of R that may attract investors is called the required rate of return.
This value can be treated as the sum of the risk-free rate and the asset
risk premium. While the assumption of linear dividend growth is
unrealistic, equation (2.2.16) shows the high sensitivity of price to
change in the discount rate R when R is close to G (see Exercise 2). A
detailed analysis of the discounted-cash-flow model is given in [3].
If the condition (2.2.13) does not hold, the solution to (2.2.12) can
be presented in the form
P(t) ¼ PD(t) þ B(t), B(t) ¼ E[B(t þ 1)=(1 þ R) ]
(2:2:17)
The term PD(t) has the sense of the fundamental value while the
function B(t) is often called the rational bubble. This term implies
that B(t) may lead to unbounded growth—the ‘‘bubble.’’ Yet, this
bubble is ‘‘rational’’ since it is based on rational expectations of future
returns. In the popular Blanchard-Watson model
B(t þ 1) ¼
1 þ R
p
B(t) þ e(t þ 1) with probability p,0 < p < 1
e(t þ 1) with probability 1  p
(2:2:18)
(
where e(t) is an independent and identically distributed process (IID)2
with E[e(t) ] ¼ 0. The specific of this model is that it describes period-
ically collapsing bubbles (see [4] for the recent research).
So far, the discrete presentation of financial data was discussed.
Clearly, market events have a discrete nature and price variations
cannot be smaller than certain values. Yet, the continuum presenta-
tion of financial processes is often employed [5]. This means that the
time interval between two consecutive market events compared to the
time range of interest is so small that it can be considered an infini-
tesimal difference. Often, the price discreteness can also be neglected
since the markets allow for quoting prices with very small differen-
tials. The future value and the present value within the continuous
presentation equal, respectively
FV ¼ K exp (rt), PV ¼ FV exp (rt)
(2:2:19)
In the following chapters, both the discrete and the continuous pre-
sentations will be used.
10
Financial Markets

2.3 MARKET EFFICIENCY
2.3.1 ARBITRAGE
Asset prices generally obey the Law of One Price, which says that
prices of equivalent assets in competitive markets must be the same
[6]. This implies that if a security replicates a package of other
securities, the price of this security and the price of the package it
replicates must be equal. It is expected also that the asset price must
be the same worldwide, provided that it is expressed in the same
currency and that the transportation and transaction costs can be
neglected. Violation of the Law of One Price leads to arbitrage, which
means buying an asset and immediate selling it (usually in another
market) with profit and without risk. One widely publicized example
of arbitrage is the notable differences in prices of prescription drugs in
the USA, Europe, and Canada. Another typical example is the so-
called triangle foreign exchange arbitrage. Consider a situation in
which a trader can exchange one American dollar (USD) for one
Euro (EUR) or for 120 Yen (JPY). In addition, a trader can exchange
one EUR for 119 JPY. Hence, in terms of the exchange rates, 1 USD/
JPY > 1 EUR/JPY * 1 USD/EUR.3 Obviously, the trader who
operates, say 100000 USD, can make a profit by buying 12000000
JPY, then selling them for 12000000/119  100840 EUR, and then
buying back 100840 USD. If the transaction costs are neglected, this
operation will bring profit of about 840 USD.
The arbitrage with prescription drugs persists due to unresolved
legal problems. However, generally the arbitrage opportunities do not
exist for long. The triangle arbitrage may appear from time to time.
Foreign exchange traders make a living, in part, by finding such
opportunities. They rush to exchange USD for JPY. It is important
to remember that, as it was noted in Section 2.1, there is only a finite
number of assets at the ‘‘best’’ price. In our example, it is a finite
number of Yens available at the exchange rate USD/JPY ¼ 120. As
soon as they all are taken, the exchange rate USD/JPY falls to the
equilibrium value 1 USD/JPY ¼ 1 EUR/JPY * 1 USD/EUR, and the
arbitrage vanishes. In general, when arbitrageurs take profits, they act
in a way that eliminates arbitrage opportunities.
Financial Markets
11

2.3.2 EFFICIENT MARKET HYPOTHESIS (EMH)
Efficient market is closely related to (the absence of) arbitrage. It
might be defined as simply an ideal market without arbitrage, but there
is much more to it than that. Let us first ask what actually causes price
to change. The share price of a company may change due to its new
earnings report, due to new prognosis of the company performance, or
due to a new outlook for the industry trend. Macroeconomic and
political events, or simply gossip about a company’s management,
can also affect the stock price. All these events imply that new infor-
mation becomes available to markets. The Efficient Market Theory
states that financial markets are efficient because they instantly reflect
all new relevant information in asset prices. Efficient Market Hypoth-
esis (EMH) proposes the way to evaluate market efficiency. For
example, an investor in an efficient market should not expect earnings
above the market return while using technical analysis or fundamental
analysis.4
Three forms of EMH are discerned in modern economic literature.
In the ‘‘weak’’ form of EMH, current prices reflect all information on
past prices. Then the technical analysis seems to be helpless. In the
‘‘strong’’ form, prices instantly reflect not only public but also private
(insider) information. This implies that the fundamental analysis
(which is what the investment analysts do) is not useful either. The
compromise between the strong and weak forms yields the ‘‘semi-
strong’’ form of EMH according to which prices reflect all publicly
available information and the investment analysts play important role
in defining fair prices.
Two notions are important for EMH. The first notion is the
random walk, which will be formally defined in Section 5.1. In short,
market prices follow the random walk if their variations are random
and independent. Another notion is rational investors who immedi-
ately incorporate new information into fair prices. The evolution of
the EMH paradigm, starting with Bachelier’s pioneering work on
random price behavior back in 1900 to the formal definition of
EMH by Fama in 1965 to the rigorous statistical analysis by Lo
and MacKinlay in the late 1980s, is well publicized [9–13]. If prices
follow the random walk, this is the sufficient condition for EMH.
However, as we shall discuss further, the pragmatic notion of market
12
Financial Markets

efficiency does not necessarily require prices to follow the random
walk.
Criticism of EMH has been conducted along two avenues. First, the
thorough theoretical analysis has resulted in rejection of the random
walk hypothesis for the weekly U.S. market returns during 1962–1986
[12]. Interestingly, similar analysis for the period of 1986–1996 shows
that the returns conform more closely to the random walk. As the
authors of this research, Lo and MacKinlay, suggest, one possible
reason for this trend is that several investment firms had implemented
statistical arbitrage trading strategies5 based on the market inefficien-
cies that were revealed in early research. Execution of these strategies
could possibly eliminate some of the arbitrage opportunities.
Another reason for questioning EMH is that the notions of ‘‘fair
price’’ and ‘‘rational investors’’ do not stand criticism in the light of
the financial market booms and crashes. The ‘‘irrational exuberance’’
in 1999–2000 can hardly be attributed to rational behavior [10]. In
fact, empirical research in the new field ‘‘behavioral finance’’ demon-
strates that investor behavior often differs from rationality [14, 15].
Overconfidence, indecisiveness, overreaction, and a willingness to
gamble are among the psychological traits that do not fit rational
behavior. A widely popularized example of irrational human behav-
ior was described by Kahneman and Tversky [16]. While conducting
experiments with volunteers, they asked participants to make choices
in two different situations. First, participants with $1000 were given a
choice between: (a) gambling with a 50% chance of gaining $1000 and
a 50% chance of gaining nothing, or (b) a sure gain of $500. In the
second situation, participants with $2000 were given a choice be-
tween: (a) a 50% chance of losing $1000 and a 50% of losing nothing,
and (b) a sure loss of $500. Thus, the option (b) in both situations
guaranteed a gain of $1500. Yet, the majority of participants chose
option (b) in the first situation and option (a) in the second one.
Hence, participants preferred sure yet smaller gains but were willing
to gamble in order to avoid sure loss.
Perhaps Keynes’ explanation that ‘‘animal spirits’’ govern investor
behavior is an exaggeration. Yet investors cannot be reduced to
completely rational machines either. Moreover, actions of different
investors, while seemingly rational, may significantly vary. In part,
this may be caused by different perceptions of market events and
Financial Markets
13

trends (heterogeneous beliefs). In addition, investors may have differ-
ent resources for acquiring and processing new information. As a
result, the notion of so-called bounded rationality has become popular
in modern economic literature (see also Section 12.2).
Still the advocates of EMH do not give up. Malkiel offers the
followingargumentinthesection‘‘Whatdowemeanbysayingmarkets
are efficient’’ of his book ‘‘A Random Walk down Wall Street’’ [9]:
‘‘No one person or institution has yet to provide a long-term,
consistent record of finding risk-adjusted individual stock
trading opportunities, particularly if they pay taxes and
incur transactions costs.’’
Thus, polemics on EMH changes the discussion from whether
prices follow the random walk to the practical ability to consistently
‘‘beat the market.’’
Whatever experts say, the search of ideas yielding excess returns
never ends. In terms of the quantification level, three main directions
in the investment strategies may be discerned. First, there are qualita-
tive receipts such as ‘‘Dogs of the Dow’’ (buying 10 stocks of the Dow
Jones Industrial Average with highest dividend yield), ‘‘January
Effect’’ (stock returns are particularly high during the first two Janu-
ary weeks), and others. These ideas are arguably not a reliable profit
source [9].
Thentherearerelativelysimplepatternsof technicalanalysis,suchas
‘‘channel,’’ ‘‘head and shoulders,’’ and so on (see, e.g., [7]). There has
been ongoing academic discussion on whether technical analysis is able
to yield persistent excess returns (see, e.g., [17–19] and references
therein). Finally, there are trading strategies based on sophisticated
statisticalarbitrage.Whileseveraltradingfirmsthatemploythesestrat-
egies have proven to be profitable in some periods, little is known about
persistent efficiency of their proprietary strategies. Recent trends indi-
cate that some statistical arbitrage opportunities may be fading [20].
Nevertheless, one may expect that modern, extremely volatile markets
will always provide new occasions for aggressive arbitrageurs.
2.4 PATHWAYS FOR FURTHER READING
In this chapter, a few abstract statistical notions such as IID and
random walk were mentioned. In the next five chapters, we take a short
14
Financial Markets

tour of the mathematical concepts that are needed for acquaintance
with quantitative finance. Those readers who feel confident in their
mathematical background may jump ahead to Chapter 8.
Regarding further reading for this chapter, general introduction to
finance can be found in [6]. The history of development and valid-
ation of EMH is described in several popular books [9–11].6 On the
MBA level, much of the material pertinent to this chapter is given
in [3].
EXERCISES
1. Familiarize yourself with the financial market data available on
the Internet (e.g., http://www.finance.yahoo.com). Download the
weekly closing prices of the exchange-traded fund SPDR that
replicates the S&P 500 index (ticker SPY) for 1996–2003. Cal-
culate simple weekly returns for this data sample (we shall use
these data for other exercises).
2. Calculate the present value of SPY for 2004 if the asset risk
premium is equal to (a) 3% and (b) 4%. The SPY dividends in
2003 were $1.63. Assume the dividend growth rate of 5% (see
Exercise 5.3 for a more accurate estimate). Assume the risk-free
rate of 3%. What risk premium was priced in SPY in the end of
2004 according to the discounted-cash-flow theory?
3. Simulate the rational bubble using the Blanchard-Watson
model (2.2.18). Define e(t) ¼ PU(t)  0:5 where PU is standard
uniform distribution (explain why the relation e(t) ¼ PU(t)
cannot be used). Use p ¼ 0:75 and R ¼ 0:1 as the initial values
for studying the model sensitivity to the input parameters.
4. Is there an arbitrage opportunity for the following set of the
exchange rates: GBP/USD ¼ 1.7705, EUR/USD ¼ 1.1914,
EUR/GBP ¼ 0.6694?
Financial Markets
15

This page intentionally left blank 


## Stochastic Processes

Chapter 4
Stochastic Processes
Financial variables, such as prices and returns, are random time-
dependent variables. The notion of stochastic process is used to de-
scribe their behavior. Specifically, the Wiener process (or the Brownian
motion) plays the central role in mathematical finance. Section 4.1
begins with the generic path: Markov process ! Chapmen-Kolmo-
gorov equation ! Fokker-Planck equation ! Wiener process. This
methodology is supplemented with two other approaches in Section
4.2. Namely, the Brownian motion is derived using the Langevin’s
equation and the discrete random walk. Then the basics of stochastic
calculus are described. In particular, the stochastic differential equa-
tion is defined using the Ito’s lemma (Section 4.3), and the stochastic
integral is given in both the Ito and the Stratonovich forms
(Section 4.4). Finally, the notion of martingale, which is widely popu-
lar in mathematical finance, is introduced in Section 4.5.
4.1 MARKOV PROCESSES
Consider a process X(t) for which the values x1, x2, . . . are meas-
ured at times t1, t2, . . . Here, one-dimensional variable x is used
for notational simplicity, though extension to multidimensional
systems is trivial. It is assumed that the joint probability density
f(x1, t1; x2, t2; . . . ) exists and defines the system completely. The con-
ditional probability density function is defined as
29

f(x1, t1; x2, t2; . . . xk, tkjxkþ1, tkþ1; xkþ2, tkþ2; . . . ) ¼
f(x1, t1; x2, t2; . . . xkþ1, tkþ1; . . . )=f(xkþ1, tkþ1; xkþ2, tkþ2; . . . )
(4:1:1)
In (4.1.1) and further in this section, t1 > t2 > . . . tk > tkþ1 > . . .
unless stated otherwise. In the simplest stochastic process, the present
has no dependence on the past. The probability density function for
such a process equals
f(x1, t1; x2, t2; . . . ) ¼ f(x1, t1)f(x2, t2) . . . 
Y
i
f(xi, ti)
(4:1:2)
The Markov process represents the next level of complexity, which
embraces an extremely wide class of phenomena. In this process, the
future depends on the present but not on the past. Hence, its condi-
tional probability density function equals
f(x1, t1; x2, t2; . . . xk, tkjxkþ1, tkþ1; xkþ2, tkþ2; . . . ) ¼
f(x1, t1; x2, t2; . . . xk, tkjxkþ1, tkþ1)
(4:1:3)
This means that evolution of the system is determined with the initial
condition (i.e., with the value xkþ1 at time tkþ1). It follows for the
Markov process that
f(x1, t1; x2, t2; x3, t3) ¼ f(x1, t1jx2, t2)f(x2, t2jx3, t3)
(4:1:4)
Using the definition of the conditional probability density, one can
introduce the general equation
f(x1, t1jx3, t3) ¼
ð
f(x1, t1; x2, t2jx3, t3)dx2
¼
ð
f(x1, t1jx2, t2; x3, t3)f(x2, t2jx3, t3)dx2
(4:1:5)
For the Markov process,
f(x1, t1jx2, t2; x3, t3) ¼ f(x1, t1jx2, t2),
(4:1:6)
Then the substitution of equation (4.1.6) into equation (4.1.5) leads to
the Chapmen-Kolmogorov equation
f(x1, t1jx3, t3) ¼
ð
f(x1, t1jx2, t2)f(x2, t2jx3, t3)dx2
(4:1:7)
This equation can be used as the starting point for deriving the
Fokker-Planck equation (see, e.g., [1] for details). First, equation
(4.1.7) is transformed into the differential equation
30
Stochastic Processes

@
@t f(x, tjx0, t0) ¼ @
@x [A(x, t)f(x, tjx0, t0)] þ 1
2
@2
@x2 [D(x, t)f(x, tjx0, t0)]þ
ð
[R(xjz, t)f(z, tjx0, t0) R(zjx, t)f(x, tjx0, t0)]dz (4:1:8)
In (4.1.8), the drift coefficient A(x, t) and the diffusion coefficient
D(x, t) are equal
A(x, t) ¼ lim
Dt!0
1
Dt
ð
(z  x)f(z, t þ Dtjx, t)dz
(4:1:9)
D(x, t) ¼ lim
Dt!0
1
Dt
ð
(z  x)2f(z, t þ Dtjx, t)dz
(4:1:10)
The integral in the right-hand side of the Chapmen-Kolmogorov
equation (4.1.8) is determined with the function
R(xjz, t) ¼ lim
Dt!0
1
Dt f(x, t þ Dtjz, t)
(4:1:11)
It describes possible discontinuous jumps of the random variable. Neg-
lecting this term in equation (4.1.8) yields the Fokker-Planck equation
@
@t f(x, tjx0, t0) ¼  @
@x [A(x, t)f(x, tjx0, t0)]
þ 1
2
@2
@x2 [D(x, t)f(x, tjx0, t0)]
(4:1:12)
This equation with A(x, t) ¼ 0 and D ¼ const is reduced to the
diffusion equation that describes the Brownian motion
@
@t f(x, tjx0, t0) ¼ D
2
@2
@x2 f(x, tjx0, t0)
(4:1:13)
Equation (4.1.13) has the analytic solution in the Gaussian form
f(x, tjx0, t0) ¼ [2pD(t  t0)]1=2 exp [(x  x0)2=2D(t  t0)] (4:1:14)
Mean and variance for the distribution (4.1.14) equal
E[x(t)] ¼ x0, Var[x(t)] ¼ E[(x(t)  x0)2] ¼ s2 ¼ D(t  t0)
(4:1:15)
The diffusion equation (4.1.13) with D ¼ 1 describes the standard
Wiener process for which
E[(x(t)  x0)2] ¼ t  t0
(4:1:16)
Stochastic Processes
31

The notions of the generic Wiener process and the Brownian motion
are sometimes used interchangeably, though there are some fine
differences in their definitions [2, 3]. I shall denote the Wiener process
with W(t) and reserve this term for the standard version (4.1.16), as it
is often done in the literature.
The Brownian motion is the classical topic of statistical physics.
Different approaches for introducing this process are described in the
next section.
4.2 BROWNIAN MOTION
In mathematical statistics, the notion of the Brownian motion is
used for describing the generic stochastic process. Yet, this term
referred originally to Brown’s observation of random motion of
pollen in water. Random particle motion in fluid can be described
using different theoretical approaches. Einstein’s original theory of
the Brownian motion implicitly employs both the Chapman-Kolmo-
gorov equation and the Fokker-Planck equation [1]. However, choos-
ing either one of these theories as the starting point can lead to the
diffusion equation. Langevin offered another simple method for de-
riving the Fokker-Planck equation. He considered one-dimensional
motion of a spherical particle of mass m and radius R that is subjected
to two forces. The first force is the viscous drag force described by the
Stokes formula, F ¼ 6pZRv, where Z is viscosity and v ¼ dr
dt is the
particle velocity. Another force, Z, describes collisions of the water
molecules with the particle and therefore has a random nature. The
Langevin equation of the particle motion is
m dv
dt ¼ 6pZRv þ Z
(4:2:1)
Let
us
multiply
both
sides
of
equation
(4.2.1)
by
r.
Since
rdv
dt ¼ d
dt (rv)  v2 and rv ¼ 1
2
d
dt (r2), then
1
2 m d2
dt2 (r2)  m dr
dt

2
¼ 3pZR d
dt (r2) þ Zr
(4:2:2)
Note that the mean kinetic energy of a spherical particle, E[ 1
2 mv2],
equals 3
2 kT. Since E[Zr] ¼ 0 due to the random nature of Z, averaging
of equation (4.2.2) yields
32
Stochastic Processes

m d2
dt2 E[r2] þ 6pZR d
dt E[r2] ¼ 6kT
(4:2:3)
The solution to equation (4.2.3) is
d
dt E[r2] ¼ kT=(pZR) þ C exp (6pZRt=m)
(4:2:4)
where C is an integration constant. The second term in equation
(4.2.4) decays exponentially and can be neglected in the asymptotic
solution. Then
E[r2]  r2
0 ¼ [kT=(pZR)]t
(4:2:5)
where r0 is the particle position at t ¼ 0. It follows from the compari-
son of equations (4.2.5) and (4.1.15) that D ¼ kT=(pZR).1
The Brownian motion can be also derived as the continuous limit
for the discrete random walk (see, e.g., [3]). First, let us introduce the
process e(t) that is named the white noise and satisfies the following
conditions
E[e(t)] ¼ 0; E[e2(t)] ¼ s2; E[e(t) e(s)] ¼ 0, if t 6¼ s:
(4:2:6)
Hence, the white noise has zero mean and constant variance s2. The
last condition in (4.2.6) implies that there is no linear correlation
between different observations of the white noise. Such a model repre-
sents an independently and identically distributed process (IID) and is
sometimes denoted IID(0, s2). The IID process can still have non-
linear correlations (see Section 5.3). The normal distribution N(0, s2)
is the special case of the white noise. First, consider a simple discrete
process
y(k) ¼ y(k  1) þ e(k)
(4:2:7)
where the white noise innovations can take only two values2
e(k) ¼
D,
with probability p, p ¼ const < 1
D,
with probability (1  p)

(4:2:8)
Now, let us introduce the continuous process yn(t) within the time
interval t 2 [0, T], such that
yn(t) ¼ y([t=h]) ¼ y([nt=T]), t 2 [0, T]
(4:2:9)
Stochastic Processes
33

In (4.2.9), [x] denotes the greatest integer that does not exceed x. The
process yn(t) has the stepwise form: it is constant except the moments
t ¼ kh, k ¼ 1, . . . , n. Mean and variance of the process yn(T) equal
E[yn(T)] ¼ n(2p  1)D ¼ T(2p  1)D=h
(4:2:10)
Var[yn(T)] ¼ nD2 ¼ TD2=h
(4:2:11)
Both mean (4.2.10) and variance (4.2.11) become infinite in the
limiting case h ! 0 with arbitrary D. Hence, we must impose a rela-
tion between D and h that ensures the finite values of the moments
E[yn(T)] and Var[yn(T)]. Namely, let us set
p ¼ (1 þ m
ffiffiffi
h
p
=s)=2, D ¼ s
ffiffiffi
h
p
(4:2:12)
where m and s are some parameters. Then
E[yn(T)] ¼ mT, Var[yn(T)] ¼ s2T
(4:2:13)
It can be shown that yn(T) converges to the normal distribution
N(mT, s2T) in the continuous limit. Hence, m and s are the drift
and diffusion parameters, respectively. Obviously, the drift parameter
differs from zero only when p 6¼ 0:5, that is when there is preference
for one direction of innovations over another. The continuous process
defined with the relations (4.2.13) is named the arithmetic Brownian
motion. It is reduced to the Wiener process when m ¼ 0 and s ¼ 1.
Note that in a more generic approach, the time intervals between
observations of y(t) themselves represent a random variable [4, 5].
While this process (so-called continuous-time random walk) better
resembles the market price variations, its description is beyond the
scope of this book.
In the general case, the arithmetic Brownian motion can be ex-
pressed in the following form
y(t) ¼ m(t)t þ s(y(t), t)W(t)
(4:2:14)
The random variable in this process may have negative values. This
creates a problem for describing prices that are essentially positive.
Therefore, the geometric Brownian motion Y(t) ¼ exp [y(t)] is often
used in financial applications.
One can simulate the Wiener process with the following equation
[W(t þ Dt)  W(t)]  DW ¼ N(0, 1)
ffiffiffiffiffi
Dt
p
(4:2:15)
34
Stochastic Processes

While the Wiener process is a continuous process, its innovations are
random. Therefore, the limit of the expression DW=Dt does not
converge when Dt ! 0. Indeed, it follows for the Wiener process that
lim
Dt!0 [DW(t)=Dt)] ¼ lim
Dt!0 [Dt1=2]
(4:2:16)
As a result, the derivative dW(t)/dt does not exist in the ordinary
sense. Thus, one needs a special calculus to describe the stochastic
processes.
4.3 STOCHASTIC DIFFERENTIAL EQUATION
The Brownian motion (4.2.14) can be presented in the differential
form3
dy(t) ¼ mdt þ sdW(t)
(4:3:1)
The equation (4.3.1) is named the stochastic differential equation.
Note that the term dW(t) ¼ [W(t þ dt)  W(t)] has the following
properties
E[dW] ¼ 0, E[dW dW] ¼ dt, E[dW dt] ¼ 0
(4:3:2)
Let us calculate (dy)2 having in mind (4.3.2) and retaining the terms
O(dt):4
(dy)2 ¼ [mdt þ sdW]2 ¼ m2dt2 þ 2mdt sdW þ s2dW2  s2dt (4:3:3)
It follows from (4.3.3) that while dy is a random variable, (dy)2 is a
deterministic one. This result allows one to derive the Ito’s lemma.
Consider a function F(y, t) that depends on both deterministic, t, and
stochastic, y(t), variables. Let us expand the differential for F(y, t)
into the Taylor series retaining linear terms and bearing in mind
equation (4.3.3)
dF(y, t) ¼ @F
@y dy þ @F
@t dt þ 1
2
@2F
@y2 (dy)2
¼ @F
@y dy þ @F
@t þ s2
2
@2F
@y2


dt
(4:3:4)
The Ito’s expression (4.3.4) has an additional term in comparison with
the differential for a function with deterministic independent vari-
Stochastic Processes
35

ables. Namely, the term s2
2
@2F
@y2 dt has stochastic nature. If y(t) is the
Brownian motion (4.3.1), then
dF(y, t) ¼ @F
@y [mdt þ sdW(t)] þ @F
@t þ s2
2
@2F
@y2


dt
¼ m @F
@y þ @F
@t þ s2
2
@2F
@y2


dt þ s @F
@y dW(t)
(4:3:5)
Let us consider the function F ¼ W2 as a simple example for
employing the Ito’s lemma. In this case, m ¼ 0, s ¼ 1, and equation
(4.3.5) is reduced to
dF ¼ dt þ 2WdW
(4:3:6)
Finally, we specify the Ito’s expression for the geometric Brownian
motion F ¼ exp [y(t)]. Since in this case, @F
@y ¼ @2F
@y2 ¼ F and @F
@t ¼ 0,
then
dF ¼ m þ s2
2


Fdt þ sFdW(t)
(4:3:7)
Hence, if F is the geometric Brownian motion, its relative change, dF/F,
behaves as the arithmetic Brownian motion.
The Ito’s lemma is a pillar of the option pricing theory. It will be
used for deriving the classical Black-Scholes equation in Section 9.4.
4.4 STOCHASTIC INTEGRAL
Now that the stochastic differential has been introduced, let us
discuss how to perform its integration. First, the Riemann-Stieltjes
integral should be defined. Consider a deterministic function f(t)
on the interval t 2 [0, T]. In order to calculate the Riemann integral
of f(t) over the interval [0, T], this interval is divided into n sub-intervals
t0 ¼ 0 < t1 < . . . < tn ¼ T and the following sum should be computed
Sn ¼
X
n
i¼1
f(ti)(ti  ti1)
(4:4:1)
where ti 2 [ti1, ti]. The Riemann integral is the limit of Sn
36
Stochastic Processes

ðT
0
f(t)dt ¼ lim Sn, max (ti  ti1) ! 0 for all i:
(4:4:2)
Note that the limit (4.4.2) exists only if the function f(t) is sufficiently
smooth. Another type of integral is the Stieltjes integral. Let us define
the differential of a function g(x)
dg ¼ g(x þ dx)  g(x)
(4:4:3)
Then the Stieltjes integral for the function g(t) on the interval
t 2 [0, T] is defined as
Sn ¼
X
n
i¼1
f(ti)[g(ti)  g(ti1)]
(4:4:4)
where ti 2 [ti1, ti]
ðT
0
f(t)dg(t) ¼ lim Sn, where max (ti  ti1) ! 0 for all i:
(4:4:5)
If g(t) has a derivative, then dg  dg
dt dt ¼ g0(t)dt, and the sum (4.4.4)
can be written as
Sn ¼
X
n
i¼1
f(ti)g0(ti)(ti  ti1)
(4:4:6)
Similarity between the Riemann sum (4.4.1) and the Stieltjes sum
(4.4.6) leads to the definition of the Riemann-Stieltjes integral. The
Riemann-Stieltjes integral over the deterministic functions does not
depend on the particular choice of the point ti within the intervals
[ti1, ti]. However, if the function f(t) is random, the sum Sn does
depend on the choice of ti. Consider, for example, the sum (4.4.4) for
the case f(t) ¼ g(t) ¼ W(t) (where W(t) is the Wiener process). It
follows from (4.1.16) that
E[Sn] ¼ E
X
n
i¼1
W(ti){W(ti)  W(ti1)}
"
#
¼
X
n
i¼1
[ min (ti, ti)  min (ti, ti1)] ¼
X
n
i¼1
(ti  ti1)
(4:4:7)
Stochastic Processes
37

Let us set for all i
ti ¼ ati þ (1  a)ti1 0  a  1
(4:4:8)
Substitution of (4.4.8) into (4.4.7) leads to E[Sn] ¼ aT. Hence, the
sum (4.4.7) depends on the arbitrary parameter a and therefore can
have any value. Within the Ito’s formalism, the value a ¼ 0 is chosen,
so that ti ¼ ti1. The stochastic Ito’s integral is defined as
ðT
0
f(t)dW(t) ¼ mslim
n!1
X
n
i¼1
f(ti1)[W(ti)  W(ti1)]
(4:4:9)
The notation ms-lim stands for the mean-square limit. It means that
the difference between the Ito integral in the left-hand side of (4.4.9)
and the sum in the right-hand side of (4.4.9) has variance that ap-
proaches zero as n increases to infinity. Thus, (4.4.9) is equivalent to
lim
n!1 E
ðT
0
f(t)dW(t) 
X
n
i1
f(ti1){W(ti)  W(ti1)}
2
4
3
5
2
¼ 0
(4:4:10)
Let us consider the integral
I(t2, t1) ¼
ðt2
t1
W(t)dW(t)
(4:4:11)
as an example of calculating the Ito’s integral. If the function W(t) is
deterministic, then the Riemann-Stieltjes integral IRS(t2, t1) equals
IRS(t2, t1) ¼ 0:5[W(t2)2  W(t1)2]
(4:4:12)
However, when W(t) is the Wiener process, the Ito’s integral II(t2, t1)
leads to a somewhat unexpected result
II(t2, t1) ¼ 0:5[W(t2)2  W(t1)2  (t2  t1)]
(4:4:13)
This follows directly from equation (4.3.6). Obviously, the result
(4.4.13) can be derived directly from the definition of the Ito’s integral
(see Exercise 1). Note that the mean of the Ito’s integral (4.4.11)
equals zero
E[II(t2, t1)] ¼ 0
(4:4:14)
38
Stochastic Processes

The difference between the right-hand sides of (4.4.12) and (4.4.13) is
determined by the particular choice of a ¼ 0 in (4.4.8). Stratonovich
has offered another definition of the stochastic integral by choosing
a ¼ 0:5. In contrast to equation (4.4.9), the Stratonovich’s integral is
defined as
ðT
0
f(t)dW(t) ¼ mslim
n!1
X
n
i¼1
f
ti1 þ ti
2


[W(ti)  W(ti1)]
(4:4:15)
For the integrand in (4.4.11), the Stratonovich’s integral IS(t2, t1)
coincides with the Riemann-Stieltjes integral
IS(t2, t1) ¼ 0:5[W(t2)2  W(t1)2]
(4:4:16)
Both Ito’s and Stratonovich’s formulations can be transformed into
eachother.Inparticular,theIto’sstochasticdifferentialequation(4.3.1)
dyI(t) ¼ mdt þ sdW(t)
(4:4:17)
is equivalent to the Stratonovich’s equation
dyS(t) ¼ m  0:5s @s
@y


dt þ sdW(t)
(4:4:18)
The applications of stochastic calculus in finance are based almost
exclusively on the Ito’s theory. Consider, for example, the integral
ðt2
t1
s(t)dW(t)
(4:4:19)
If no correlation between the function s(t) and the innovation dW(t)
is assumed, then the Ito’s approximation is a natural choice. In this
case, the function s(t) is said to be a nonanticipating function [1, 2].
However, if the innovations dW(t) are correlated (so-called non-white
noise), then the Stratonovich’s approximation appears to be an ad-
equate theory [1, 6].
4.5 MARTINGALES
The martingale methodology plays an important role in the
modern theory of finance [2, 7, 8]. Martingale is a stochastic process
X(t) that satisfies the following condition
Stochastic Processes
39

E[X(t þ 1)jX(t), X(t  1), . . . ] ¼ X(t)
(4:5:1)
The equivalent definition is given by
E[X(t þ 1)  X(t)jX(t), X(t  1), . . . ] ¼ 0
(4:5:2)
Both these definitions are easily generalized for the continuum pre-
sentation where the time interval, dt, between two sequent moments
t þ 1 and t approaches zero (dt ! 0). The notion of martingale is
rooted in the gambling theory. It is closely associated with the notion
of fair game, in which none of the players has an advantage. The
condition (4.5.1) implies that the expectation of the gamer wealth at
time t þ 1 conditioned on the entire history of the game is equal to the
gamer wealth at time t. Similarly, equation (4.5.2) means that the
expectation to win at every round of the game being conditioned on
the history of the game equals zero. In other words, martingale has no
trend. A process that has positive trend is named submartingale.
A process with negative trend is called supermartingale.
The martingale hypothesis applied to the asset prices states that the
expectation of future price is simply the current price. This assumption
is closely related to the Efficient Market Hypothesis discussed in
Section 2.3. Generally, the asset prices are not martingales for they
incorporate risk premium. Indeed, there must be some reward offered
to investors for bearing the risks associated with keeping the assets. It
can be shown, however, that the prices with discounted risk premium
are martingales [3].
The important property of the Ito’s integral is that it is martingale.
Consider, for example, the integral (4.4.19) approximated with the
sum (4.4.9). Because the innovations dW(t) are unpredictable, it
follows from (4.4.14) that
E
ð
tþDt
t
s(z)dW(z)
2
4
3
5 ¼ 0
(4:5:3)
Therefore,
E
ð
tþDt
0
s(z)dW(z)
2
4
3
5 ¼
ðt
0
s(z)dW(z)
(4:5:4)
40
Stochastic Processes

and the integral (4.4.19) satisfies the martingale definition. Note that
for the Brownian motion with drift (4.2.14)
E[y(t þ dt)] ¼ E y(t) þ
ð
tþdt
t
dy
2
4
3
5 ¼ y(t) þ mdt
(4:5:5)
Hence, the Brownian motion with drift is not a martingale. However,
the process
z(t) ¼ y(t)  mt
(4:5:6)
is a martingale since
E[z(t þ dt)] ¼ z(t)
(4:5:7)
This result follows also from the Doob-Meyer decomposition theorem,
which states that a continuous submartingale X(t) at 0  t  1 with
finite expectation E[X(t)] < 1 can be decomposed into a continuous
martingale and an increasing deterministic process.
4.6 REFERENCES FOR FURTHER READING
Theory and applications of the stochastic processes in natural
sciences are described in [1, 6]. A good introduction to the stochastic
calculus in finance is given in [2]. For a mathematically inclined
reader, the presentation of the stochastic theory with increasing
level of technical details can be found in [7, 8].
4.7 EXERCISES
1. Simulate daily price returns using the geometric Brownian
motion (4.3.7) for four years. Use equation (4.2.15) for approxi-
mating DW. Assume that S(0) ¼ 10, m ¼ 10%, s ¼ 20% (m and
s are given per annum). Assume 250 working days per annum.
2. Prove that
ðt2
t1
W(s)ndW(s) ¼
1
n þ 1 [W(t2)nþ1  W(t1)nþ1]  n
2
ðt2
t1
W(s)n1ds
Hint: Calculate d(Wnþ1) using the Ito’s lemma.
Stochastic Processes
41

3. Solve the Ornstein-Uhlenbeck equation that describes the mean-
reverting process in which the solution fluctuates around its
mean
dX ¼ mXdt þ sdW, m > 0
Hint: introduce the variable Y ¼ X exp (mt).
*4. Derive the integral (4.4.13) directly from the definition of the
Ito’s integral (4.4.9).
42
Stochastic Processes

