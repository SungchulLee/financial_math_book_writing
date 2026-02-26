# Copula Functions: Theory & Properties

!!! info "Source"
    **Copula Methods in Finance** by Umberto Cherubini, Elisa Luciano, and Walter Vecchiato, Wiley, 2004.
    These notes are used for educational purposes.

## Derivatives Pricing, Hedging and Risk Management

xii
Preface
in mathematical finance. In fact, the use of copula functions enables the task of specify-
ing the marginal distributions to be decoupled from the dependence structure of variables.
This allows us to exploit univariate techniques at the first step, and is directly linked to
non-parametric dependence measures at the second step. This avoids the flaws of linear
correlation that have, by now, become well known.
This book is an introduction to the use of copula functions from the viewpoint of mathe-
matical finance applications. Our method intends to explain copulas by means of applications
to major topics such as asset pricing, risk management and credit risk analysis. Our target
is to enable the readers to devise their own applications, following the strategies illustrated
throughout the book. In the text we concentrate all the information concerning mathematics,
statistics and finance that one needs to build an application to a financial problem. Examples
of applications include the pricing of multivariate derivatives and exotic contracts (basket,
rainbow, barrier options and so on), as well as risk-management applications. Beyond that,
references to financial topics and market data are pervasively present throughout the book,
to make the mathematical and statistical concepts, and particularly the estimation issues,
easier for the reader to grasp.
The audience target of our work consists of academics and practitioners who are eager
to master and construct copula applications to financial problems. For this applied focus,
this book is, to the best of our knowledge, the first initiative in the market. Of course, the
novelty of the topic and the growing number of research papers on the subject presented at
finance conferences all over the world allows us to predict that our book will not remain the
only one for too long, and that, on the contrary, this topic will be one of the major issues
to be studied in the mathematical finance field in the near future.
Outline of the book
Chapter 1 reviews the state of the art in asset pricing and risk management, going over the
major frontier issues and providing justifications for introducing copula functions.
Chapter 2 introduces the reader to the bivariate copula case. It presents the mathemat-
ical and probabilistic background on which the applications are built and gives some first
examples in finance.
Chapter 3 discusses the flaws of linear correlation and highlights how copula functions,
along with non-parametric association measures, may provide a much more flexible way to
represent market comovements.
Chapter 4 extends the technical tools to a multivariate setting. Readers who are not already
familiar with copulas are advised to skip this chapter at first reading (or to read it at their
own risk!).
Chapter 5 explains the statistical inference for copulas. It covers both methodological
aspects and applications from market data, such as calibration of actual risk factors comove-
ments and VaR measurement. Here the readers can find details on the classical estimation
methods as well as on most recent approaches, such as the conditional copula.
Chapter 6 is devoted to an exhaustive account of simulation algorithms for a large class
of multivariate copulas. It is enhanced by financial examples.
Chapter 7 presents credit risk applications, besides giving a brief introduction to credit
derivative markets and instruments. It applies copulas to the pricing of complex credit
structures such as basket default swaps and CDOs. It is shown how to calibrate the pricing

Preface
xiii
model to market data. Its sensitivity with respect to the copula choice is accounted for in
concrete examples.
Chapter 8 covers option pricing applications. Starting from the bivariate pricing kernel,
copulas are used to evaluate counterparty risk in derivative transactions and bivariate rain-
bow options, such as options to exchange. We also show how the barrier option pricing
problem can be cast in a bivariate setting and can be represented in terms of copulas.
Finally, the estimation and simulation techniques presented in Chapters 5 and 6 are put at
work to solve the evaluation problem of a multivariate basket option.


1
Derivatives Pricing, Hedging and Risk
Management:
The State of the Art
1.1
INTRODUCTION
The purpose of this chapter is to give a brief review of the basic concepts used in finance
for the purpose of pricing contingent claims. As our book is focusing on the use of copula
functions in financial applications, most of the content of this chapter should be considered
as a prerequisite to the book. Readers who are not familiar with the concepts exposed
here are referred for a detailed treatment to standard textbooks on the subject. Here our
purpose is mainly to describe the basic tools that represent the state of the art of finance,
as well as general problems, and to provide a brief, mainly non-technical, introduction to
copula functions and the reason why they may be so useful in financial applications. It
is particularly important that we address three hot issues in finance. The first is the non-
normality of returns, which makes the standard Black and Scholes option pricing approach
obsolete. The second is the incomplete market issue, which introduces a new dimension
to the asset pricing problem – that of the choice of the right pricing kernel both in asset
pricing and risk management. The third is credit risk, which has seen a huge development
of products and techniques in asset pricing.
This discussion would naturally lead to a first understanding of how copula functions can
be used to tackle some of these issues. Asset pricing and risk evaluation techniques rely
heavily on tools borrowed from probability theory. The prices of derivative products may be
written, at least in the standard complete market setting, as the discounted expected values
of their future pay-offs under a specific probability measure derived from non-arbitrage
arguments. The risk of a position is instead evaluated by studying the negative tail of the
probability distribution of profit and loss. Since copula functions provide a useful way to
represent multivariate probability distributions, it is no surprise that they may be of great
assistance in financial applications. More than this, one can even wonder why it is only
recently that they have been discovered and massively applied in finance. The answer has
to do with the main developments of market dynamics and financial products over the last
decade of the past century.
The main change that has been responsible for the discovery of copula methods in finance
has to do with the standard hypothesis assumed for the stochastic dynamics of the rates of
returns on financial products. Until the 1987 crash, a normal distribution for these returns
was held as a reasonable guess. This concept represented a basic pillar on which most of
modern finance theory has been built. In the field of pricing, this assumption corresponds
to the standard Black and Scholes approach to contingent claim evaluation. In risk manage-
ment, assuming normality leads to the standard parametric approach to risk measurement
that has been diffused by J.P. Morgan under the trading mark of RiskMetrics since 1994,
and is still in use in many financial institutions: due to the assumption of normality, the

2
Copula Methods in Finance
approach only relies on volatilities and correlations among the returns on the assets in the
portfolio. Unfortunately, the assumption of normally distributed returns has been severely
challenged by the data and the reality of the markets. On one hand, even evidence on the
returns of standard financial products such as stocks and bonds can be easily proved to
be at odds with this assumption. On the other hand, financial innovation has spurred the
development of products that are specifically targeted to provide non-normal returns. Plain
vanilla options are only the most trivial example of this trend, and the development of the
structured finance business has made the presence of non-linear products, both plain vanilla
and exotic, a pervasive phenomenon in bank balance sheets. This trend has even more been
fueled by the pervasive growth in the market for credit derivatives and credit-linked prod-
ucts, whose returns are inherently non-Gaussian. Moreover, the task to exploit the benefits
of diversification has caused both equity-linked and credit-linked products to be typically
referred to baskets of stocks or credit exposures. As we will see throughout this book, tack-
ling these issues of non-normality and non-linearity in products and portfolios composed
by many assets would be a hopeless task without the use of copula functions.
1.2
DERIVATIVE PRICING BASICS: THE BINOMIAL MODEL
Here we give a brief description of the basic pillar behind pricing techniques, that is the
use of risk-neutral probability measures to evaluate contingent claims, versus the objective
measure observed from the time series of market data. We will see that the existence of
such risk measures is directly linked to the basic pricing principle used in modern finance to
evaluate financial products. This requirement imposes that prices must ensure that arbitrage
gains, also called “free lunches”, cannot be obtained by trading the securities in the market.
An arbitrage deal is a trading strategy yielding positive returns at no risk. Intuitively, the
idea is that if we can set up two positions or trading strategies giving identical pay-offs at
some future date, they must also have the same value prior to that date, otherwise one could
exploit arbitrage profits by buying the cheaper and selling the more expensive before that
date, and unwinding the deal as soon as they are worth the same. Ruling out arbitrage gains
then imposes a relationship among the prices of the financial assets involved in the trading
strategies. These are called “fair” or “arbitrage-free” prices. It is also worth noting that these
prices are not based on any assumption concerning utility maximizing behavior of the agents
or equilibrium of the capital markets. The only requirement concerning utility is that traders
“prefer more to less”, so that they would be ready to exploit whatever arbitrage opportunity
was available in the market. In this section we show what the no-arbitrage principle implies
for the risk-neutral measure and the objective measure in a discrete setting, before extending
it to a continuous time model.
The main results of modern asset pricing theory, as well as some of its major problems,
can be presented in a very simple form in a binomial model. For the sake of simplicity,
assume that the market is open on two dates, t and T , and that the information structure
of the economy is such that, at the future time T , only two states of the world {H, L} are
possible. A risky asset is traded on the market at the current time t for a price equal to S (t),
while at time T the price is represented by a random variable taking values {S (H) , S (L)}
in the two states of the world. A risk-free asset gives instead a value equal to 1 unit of
currency at time T no matter which state of the world occurs: we assume that the price at
time t of the risk-free asset is equal to B. Our problem is to price another risky asset taking

Derivatives Pricing, Hedging and Risk Management
3
values {G (H) , G (L)} at time T . As we said before, the price g (t) must be consistent with
the prices S (t) and B observed on the market.
1.2.1
Replicating portfolios
In order to check for arbitrage opportunities, assume that we construct a position in g
units of the risky security S (t) and g units of the risk-free asset in such a way that at
time T
gS (H) + g = G (H)
gS (L) + g = G (L)
So, the portfolio has the same value of asset G at time T . We say that it is the “replicating
portfolio” of asset G. Obviously we have
g = G (H) −G (L)
S (H) −S (L)
g = G (L) S (H) −G (H) S (L)
S (H) −S (L)
1.2.2
No-arbitrage and the risk-neutral probability measure
If we substitute g and g in the no-arbitrage equation
g (t) = gS (t) + Bg
we may rewrite the price, after naive algebraic manipulation, as
g (t) = B [QG (H) + (1 −Q) G (L)]
with
Q ≡S (t) /B −S (L)
S (H) −S (L)
Notice that we have
0 < Q < 1 ⇔S (L) < S (t)
B
< S (H)
It is straightforward to check that if the inequality does not hold there are arbitrage
opportunities: in fact, if, for example, S (t) /B ⩽S (L) one could exploit a free-lunch by
borrowing and buying the asset. So, in the absence of arbitrage opportunities it follows that
0 < Q < 1, and Q is a probability measure. We may then write the no-arbitrage price as
g (t) = BEQ [G (T )]

4
Copula Methods in Finance
In order to rule out arbitrage, then, the above relationship must hold for all the contingent
claims and the financial products in the economy. In fact, even for the risky asset S we
must have
S (t) = BEQ [S (T )]
Notice that the probability measure Q was recovered from the no-arbitrage requirement
only. To understand the nature of this measure, it is sufficient to compute the expected rate
of return of the different assets under this probability. We have that
EQ
G (T )
g (t) −1

= EQ
S (T )
S (t) −1

= 1
B −1 ≡i
where i is the interest rate earned on the risk-free asset for an investment horizon from t
to T . So, under the measure Q all of the risky assets in the economy are expected to yield
the same return as the risk-free asset. For this reason such a measure is called risk-neutral
probability.
Alternatively, the measure can be characterized in a more technical sense in the following
way. Let us assume that we measure each risky asset in the economy using the risk-free
asset as numeraire. Recalling that the value of the riskless asset is B at time t and 1 at time
T , we have
g (t)
B (t) = EQ
G (T )
B (T )

= EQ [G (T )]
A process endowed with this property (i.e. z (t) = EQ (z (T ))) is called a martingale. For
this reason, the measure Q is also called an equivalent martingale measure (EMM).1
1.2.3
No-arbitrage and the objective probability measure
For comparison with the results above, it may be useful to address the question of which
constraints are imposed by the no-arbitrage requirements on expected returns under the
objective probability measure. The answer to this question may be found in the well-known
arbitrage pricing theory (APT). Define the rates of return of an investment on assets S and
g over the horizon from t to T as
ig ≡G (T )
g (t) −1
iS ≡S (T )
S (t) −1
and the rate of return on the risk-free asset as i ≡1/B −1.
The rate of returns on the risky assets are assumed to be driven by a linear data-generating
process
ig = ag + bgf
iS = aS + bSf
where the risk factor f is taken with zero mean and unit variance with no loss of generality.
1 The term equivalent is a technical requirement referring to the fact that the risk-neutral measure and the objective
measure must agree on the same subset of zero measure events.

Derivatives Pricing, Hedging and Risk Management
5
Of course this implies ag = E

ig

and aS = E (iS). Notice that the expectation is now
taken under the original probability measure associated with the data-generating process
of the returns. We define this measure P . Under the same measure, of course, bg and bS
represent the standard deviations of the returns. Following a standard no-arbitrage argument
we may build a zero volatility portfolio from the two risky assets and equate its return to
that of the risk-free asset. This yields
aS −i
bS
= ag −i
bg
= λ
where λ is a parameter, which may be constant, time-varying or even stochastic, but has
to be the same for all the assets. This relationship, that avoids arbitrage gains, could be
rewritten as
E (iS) = i + λbS
E

ig

= i + λbg
In words, the expected rate of return of each and every risky asset under the objective
measure must be equal to the risk-free rate of return plus a risk premium. The risk premium
is the product of the volatility of the risky asset times the market price of risk parameter λ.
Notice that in order to prevent arbitrage gains the key requirement is that the market price
of risk must be the same for all of the risky assets in the economy.
1.2.4
Discounting under different probability measures
The no-arbitrage requirement implies different restrictions under the objective probability
measures. The relationship between the two measures can get involved in more complex
pricing models, depending on the structure imposed on the dynamics of the market price
of risk. To understand what is going on, however, it may be instructive to recover this
relationship in a binomial setting. Assuming that P is the objective measure, one can easily
prove that
Q = P −λ

P (1 −P )
and the risk-neutral measure Q is obtained by shifting probability from state H to state L.
To get an intuitive assessment of the relationship between the two measures, one could
say that under risk-neutral valuation the probability is adjusted for risk in such a way as
to guarantee that all of the assets are expected to yield the risk-free rate; on the contrary,
under the objective risk-neutral measure the expected rate of return is adjusted to account
for risk. In both cases, the amount of adjustment is determined by the market price of risk
parameter λ.
To avoid mistakes in the evaluation of uncertain cash flows, it is essential to take into
consideration the kind of probability measure under which one is working. In fact, the
discount factor applied to expected cash flows must be adjusted for risk if the expectation
is computed under the objective measure, while it must be the risk-free discount factor if
the expectation is taken under the risk-neutral probability. Indeed, one can also check that
g (t) = E [G (T )]
1 + i + λbg
= EQ [G (T )]
1 + i

6
Copula Methods in Finance
and using the wrong interest rate to discount the expected cash flow would get the wrong
evaluation.
1.2.5
Multiple states of the world
Consider the case in which three scenarios are possible at time T , say {S (HH) , S (HL),
S (LL)}. The crucial, albeit obvious, thing to notice is that it is not possible to replicate an
asset by a portfolio of only two other assets. To continue with the example above, whatever
amount g of the asset S we choose, and whatever the position of g in the risk-free asset,
we are not able to perfectly replicate the pay-off of the contract g in all the three states
of the world: whatever replicating portfolio was used would lead to some hedging error.
Technically, we say that contract g is not attainable and we have an incomplete market
problem. The discussion of this problem has been at the center of the analysis of modern
finance theory for some years, and will be tackled in more detail below. Here we want to
stress in which way the model above can be extended to this multiple scenario setting. There
are basically two ways to do so. The first is to assume that there is a third asset, whose
pay-off is independent of the first two, so that a replicating portfolio can be constructed
using three assets instead of two. For an infinitely large number of scenarios, an infinitely
large set of independent assets is needed to ensure perfect hedging. The second way to go
is to assume that the market for the underlying opens at some intermediate time τ prior to
T and the underlying on that date may take values {S (H) , S (L)}. If this is the case, one
could use the following strategy:
• Evaluate g (τ) under both scenarios {S (H) , S (L)}, yielding {g (H) , g (L)}: this will result
in the computation of the risk-neutral probabilities {Q (H) , Q (L)} and the replicating
portfolios consisting of {g (H), g (L)} units of the underlying and {g (H) , g (L)}
units of the risk-free asset.
• Evaluate g (t) as a derivative product giving a pay-off {g (H) , g (L)} at time τ, depending
on the state of the world: this will result in a risk-neutral probability Q, and a replicating
portfolio with g units of the underlying and g units of the risk-free asset.
The result is that the value of the product will be again set equal to its replicating portfolio
g (t) = gS (t) + Bg
but at time τ it will be rebalanced, depending on the price observed for the underlying
asset. We will then have
g (H) = g (H) S (H) + Bg (H)
g (L) = g (L) S (L) + Bg (L)
and both the position on the underlying asset and the risk-free asset will be changed fol-
lowing the change of the underlying price. We see that even though we have three possible
scenarios, we can replicate the product g by a replicating portfolio of only two assets, thanks
to the possibility of changing it at an intermediate date. We say that we follow a dynamic
replication trading strategy, opposed to the static replication portfolio of the simple example

Derivatives Pricing, Hedging and Risk Management
7
above. The replication trading strategy has a peculiar feature: the value of the replicating
portfolio set up at t and re-evaluated using the prices of time τ is, in any circumstances,
equal to that of the new replicating portfolio which will be set up at time τ. We have in
fact that
gS (H) + g = g (H) = g (H) S (H) + Bg (H)
gS (L) + g = g (L) = g (L) S (L) + Bg (L)
This means that once the replicating portfolio is set up at time t, no further expense or
withdrawal will be required to rebalance it, and the sums to be paid to buy more of an
asset will be exactly those made available by the selling of the other. For this reason the
replicating portfolio is called self-financing.
1.3
THE BLACK–SCHOLES MODEL
Let us think of a multiperiod binomial model, with a time difference between one date and
the following equal to h. The gain or loss on an investment on asset S over every period
will be given by
S (t + h) −S (t) = iS (t) S (t)
Now assume that the rates of return are serially uncorrelated and normally distributed as
iS (t) = µ∗+ σ ∗ε (t)
with µ∗and σ ∗constant parameters and ε (t) ∼N (0, 1), i.e. a series of uncorrelated stan-
dard normal variables. Substituting in the dynamics of S we get
S (t + h) −S (t) = µ∗S (t) + σ ∗S (t) ε (t)
Taking the limit for h that tends to zero, we may write the stochastic dynamics of S in
continuous time as
dS (t) = µS (t) dt + σS (t) dz (t)
The stochastic process is called geometric brownian motion, and it is a specific case of a
diffusive process. z (t) is a Wiener process, defined by dz (t) ∼N (0, dt) and the terms µS (t)
and σS (t) are known as the drift and diffusion of the process. Intuitively, they represent
the expected value and the volatility (standard deviation) of instantaneous changes of S (t).
Technically, a stochastic process in continuous time S (t) , t ⩽T , is defined with respect
to a filtered probability space {, ℑt, P }, where ℑt = σ(S(u), u ⩽t) is the smallest σ-field
containing sets of the form {a ⩽S(u) ⩽b}, 0 ⩽u ⩽t: more intuitively, ℑt represents the
amount of information available at time t.
The increasing σ-fields {ℑt} form a so-called filtration F:
ℑ0 ⊂ℑ1 ⊂· · · ⊂ℑT
Not only is the filtration increasing, but ℑ0 also contains all the events with zero measure;
and these are typically referred to as “the usual assumptions”. The increasing property

8
Copula Methods in Finance
corresponds to the fact that, at least in financial applications, the amount of information is
continuously increasing as time elapses.
A variable observed at time t is said to be measurable with respect to ℑt if the set of
events, such that the random variable belongs to a Borel set on the line, is contained in
ℑt, for every Borel set: in other words, ℑt contains all the amount of information needed
to recover the value of the variable at time t. If a process S (t) is measurable with respect
to ℑt for all t ⩾0, it is said to be adapted with respect to ℑt. At time t, the values of a
variable at any time τ > t can instead be characterized only in terms of the last object, i.e.
the probability measure P , conditional on the information set ℑt.
In this setting, a diffusive process is defined, assuming that the limit of the first and
second moments of S (t + h) −S (t) exist and are finite, and that finite jumps have zero
probability in the limit. Technically,
lim
h→0
1
hE [S (t + h) −S (t) | S (t) = S] = µ (S, t)
lim
h→0
1
hE

[S (t + h) −S (t)]2 | S (t) = S

= σ 2 (S, t)
and
lim
h→0
1
h Pr (|S (t + h) −S (t)| > ε | S (t) = S) = 0
Of course the moments in the equations above are tacitly assumed to exist. For further and
detailed discussion of the matter, the reader is referred to standard textbooks on stochastic
processes (see, for example, Karlin & Taylor, 1981).
1.3.1
Ito’s lemma
A paramount result that is used again and again in financial applications is Ito’s lemma.
Say y (t) is a diffusive stochastic process
dy (t) = µy dt + σy dz (t)
and f (y, t) is a function differentiable twice in the first argument and once in the second.
Then f also follows a diffusive process
df (y, t) = µf dt + σf dz (t)
with drift and diffusion terms given by
µf = ∂f
∂t + ∂f
∂y µy + 1
2
∂2f
∂y2 σ 2
y
σf = ∂f
∂y σy

Derivatives Pricing, Hedging and Risk Management
9
Example 1.1
Notice that, given
dS (t) = µS (t) dt + σS (t) dz (t)
we can set f (S, t) = ln S (t) to obtain
d ln S (t) = (µ −1
2σ 2) dt + σdz (t)
If µ and σ are constant parameters, it is easy to obtain
ln S (τ) | ℑt ∼N(ln S (t) + (µ −1
2σ 2) (τ −t) , σ 2 (τ −t))
where N (m, s) is the normal distribution with mean m and variance s. Then, Pr (S (τ) | ℑt)
is described by the lognormal distribution.
It is worth stressing that the geometric brownian motion assumption used in the
Black–Scholes model implies that the log-returns on the asset S are normally distributed,
and this is the same as saying that their volatility is assumed to be constant.
1.3.2
Girsanov theorem
A second technique that is mandatory to know for the application of diffusive processes
to financial problems is the result known as the Girsanov theorem (or Cameron–Martin–
Girsanov theorem). The main idea is that given a Wiener process z (t) defined under the
filtration {, ℑt, P } we may construct another processz (t) which is a Wiener process under
another probability space {, ℑt, Q}. Of course, the latter process will have a drift under
the original measure P . Under such measure it will be in fact
dz (t) = dz (t) + γ dt
for γ deterministic or stochastic and satisfying regularity conditions. In plain words, chang-
ing the probability measure is the same as changing the drift of the process.
The application of this principle to our problem is straightforward. Assume there is an
opportunity to invest in a money market mutual fund yielding a constant instantaneous risk-
free yield equal to r. In other words, let us assume that the dynamics of the investment in
the risk-free asset is
dB (t) = rB (t)
where the constant r is also called the interest rate intensity (r ≡ln (1 + i)). We saw before
that under the objective measure P the no-arbitrage requirement implies
E
dS (t)
S (t)

= µ dt = (r + λσ) dt

10
Copula Methods in Finance
where λ is the market price of risk. Substituting in the process followed by S (t) we have
dS (t) = (r + λσ) S (t) dt + σS (t) dz (t)
= S (t) (r dt + σ (dz (t) + λ dt))
= S (t) (r dt + σ dz (t))
where dz (t) = dz (t) + λ dt is a Wiener process under some new measure Q. Under such
a measure, the dynamics of the underlying is then
dS (t) = rS (t) dt + σS (t) dz (t)
meaning that the instantaneous expected rate of the return on asset S (t) is equal to the
instantaneous yield on the risk-free asset
EQ
dS (t)
S (t)

= r dt
i.e. that Q is the so-called risk-neutral measure. It is easy to check that the same holds
for any derivative written on S (t). Define g (S, t) the price of a derivative contract giving
pay-off G (S (T ) , T ). Indeed, using Ito’s lemma we have
dg (t) = µgg (t) dt + σgg (t) dz (t)
with
µgg = ∂g
∂t + ∂g
∂S (r + λσ) S (t) + 1
2
∂2g
∂S2 σ 2 (t) S2
σgg = ∂g
∂S σ
Notice that under the original measure we then have
dg (t) =
∂g
∂t + ∂g
∂S µS (t) + 1
2
∂2g
∂S2 σ 2 (t) S2

dt + ∂g
∂S σ dz (t)
However, the no-arbitrage requirement implies
µgg = ∂g
∂t + ∂g
∂S (r + λσ) S (t) + 1
2
∂2g
∂S2 σ 2 (t) S2 = rg + λ ∂g
∂S σ
so it follows that
∂g
∂t + ∂g
∂S rS (t) + 1
2
∂2g
∂S2 σ 2 (t) S2 = rg
This is the fundamental partial differential equation (PDE) of the Black–Scholes model.
Notice that by substituting this result into the risk-neutral dynamics of g under measure Q
we get
dg (t) = rg (t) dt + ∂g
∂S σ dz (t)

Derivatives Pricing, Hedging and Risk Management
11
and the product g is expected to yield the instantaneous risk-free rate. We reach the con-
clusion that under the risk-neutral measure Q
EQ
dS (t)
S (t)

= EQ
dg (t)
g (t)

= r dt
that is, all the risky assets are assumed to yield the instantaneous risk-free rate.
1.3.3
The martingale property
The price of any contingent claim g can be recovered solving the fundamental PDE. An
alternative way is to exploit the martingale property embedded in the measure Q. Define Z as
the value of a product expressed using the riskless money market account as the numeraire,
i.e. Z (t) ≡g (t) /B (t). Given the dynamics of the risky asset under the risk-neutral measure
Q we have that
dS (t) = rS (t) dt + σS (t) dz (t)
dB (t) = rB (t) dt
and it is easy to check that
dZ (t) = σZ (t) dz (t)
The process Z (t) then follows a martingale, so that EQ (Z (T )) = Z (t). This directly
provides us with a pricing formula. In fact we have
Z (t) = g (S, t)
B (t)
= EQ (Z (T )) = EQ
	G (S, T )
B (T )

Considering that B (T ) is a deterministic function, we have
g (S, t) = B (t)
B (T )EQ (G (S, T )) = exp (−r (T −t)) EQ (G (S, T ))
The price of a contingent claim is obtained by taking the relevant expectation under the
risk-neutral measure and discounting it back to the current time t. Under the assumption of
log-normal distribution of the future price of the underlying asset S, we may recover for
instance the basic Black–Scholes formula for a plain vanilla call option
CALL(S, t; K, T ) = S (t) 
 (d1) −exp [−r (T −t)] K
 (d2)
d1 = ln (S (t) /K) +

r + σ 2/2

(T −t)
σ
√
T −t
d2 = d1 −σ
√
T −t
where 
 (x) is the standard normal distribution function evaluated at x

 (x) = 1
2π
 x
−∞
exp

−u2
2

du

12
Copula Methods in Finance
The formula for the put option is, instead,
PUT(S, t; K, T ) = −S (t) 
 (−d1) + exp [−r (T −t)] K
 (−d2)
Notice that a long position in a call option corresponds to a long position in the underlying
and a debt position, while a long position in a put option corresponds to a short position in
the underlying and an investment in the risk-free asset. As S (t) tends to infinity, the value
of a call tends to that of a long position in a forward and the value of the put tends to zero;
as S (t) tends to zero, the value of the put tends to the value of a short position in a forward
and the price of the call option tends to zero.
The sensitivity of the option price with respect to the underlying is called delta () and
is equal to 
 (d1) for the call option and 
 (d1) −1 for the put. The sensitivity of the
delta with respect to the underlying is called gamma (), and that of the option price with
respect to time is called theta (
). These derivatives, called the greek letters, can be used
to approximate, in general, the value of any derivative contract by a Taylor expansion as
g (S (t + h) , t + h) ≃g (S (t) , t) + g (S (t + h) −S (t))
+ 1
2g (S (t + h) −S (t))2 + 
gh
Notice that the greek letters are linked one to the others by the fundamental PDE ruling
out arbitrage. Indeed, this condition can be rewritten as

g + grS (t) + 1
2gσ 2 (t) S2 −rg = 0
1.3.4
Digital options
A way to understand the probabilistic meaning of the Black–Scholes formula is to compute
the price of digital options. Digital options pay a fixed sum or a unit of the underlying if
the underlying asset is above some strike level at the exercise date. Digital options, which
pay a fixed sum, are called cash-or-nothing (CoN) options, while those paying the asset are
called asset-or-nothing (AoN) options. Under the log-normal assumption of the conditional
distribution of the underlying held under the Black–Scholes model, we easily obtain
CoN(S, t; K, T ) = exp [−r (T −t)] 
 (d2)
The asset-or-nothing price can be recovered by arbitrage observing that at time T
CALL(S, T ; K, T ) + K CoN(S, T ; K, T ) = 1{S(T )>K}S (T ) = AoN(S, T ; K, T )
where 1{S(T )>K} is the indicator function assigning 1 to the case S (T ) > K. So, to avoid
arbitrage we must have
AoN(S, t; K, T ) = S (t) 
 (d1)
Beyond the formulas deriving from the Black–Scholes model, it is important to stress
that this result – that a call option is the sum of a long position in a digital asset-or-nothing
option and a short position in K cash-or-nothing options – remains true for all the option

Derivatives Pricing, Hedging and Risk Management
13
pricing models. In fact, this result directly stems from the no-arbitrage requirement imposed
in the asset pricing model. The same holds for the result (which may be easily verified) that
−exp [r (T −t)] ∂CALL(S, t; K, T )
∂K
= 
 (d2) = Pr (S (T ) > K)
where the probability is computed under measure Q. From the derivative of the call option
with respect to the strike price we can then recover the risk-neutral probability of the
underlying asset.
1.4
INTEREST RATE DERIVATIVES
The valuation of derivatives written on fixed income products or interest rates is more
involved than the standard Black–Scholes model described above, even though all models
are based on the same principles and techniques of arbitrage-free valuation presented above.
The reason for this greater complexity is that the underlying asset of these products is the
curve representing the discounting factors of future cash-flows as a function of maturity T .
The discount factor D(t, T ) of a unit cash-flow due at maturity T , evaluated at current time
t, can be represented as
D (t, T ) = exp [−r (t, T ) (T −t)]
where r (t, T ) is the continuously compounded spot rate or yield to maturity. Alternatively,
the discount factor can be characterized in terms of forward rates, as
D (t, T ) = exp

−
 T
t
f (t, u) du

Term structure pricing models are based on stochastic representations of the spot or forward
yield curve.
1.4.1
Affine factor models
The classical approach to interest rate modeling is based on the assumption that the stochastic
dynamics of the curve can be represented by the dynamics of some risk factors. The yield
curve is then recovered endogenously from their dynamics. The most famous models are
due to Vasicek (1977) and Cox, Ingersoll and Ross (1985). They use a single risk factor,
which is chosen to be the intercept of the yield curve – that is, the instantaneous interest
rate. While this rate was assumed to be constant under the Black–Scholes framework, now
it is assumed to vary stochastically over time, so that the value of a European contingent
claim g, paying G(T ) at time T , is generalized to
g (t) = EQ

exp

−
 T
t
r (u) du

G (T ) | ℑt

where the expectation is again taken under the risk-neutral measure Q. Notice that for the
discount factor D (t, T ) we have the pay-off D (T, T ) = 1, so that
D (t, T ) = EQ

exp

−
 T
t
r (u) du
 ℑt


14
Copula Methods in Finance
We observe that even if the pay-off is deterministic, the discount factor is stochastic, and
it is a function of the instantaneous interest rate r(t). Let us assume that the dynamics of
r(t) under the risk-neutral measure is described by the diffusion process
dr (t) = µr dt + σr dz (t)
and let us write the dynamics of the discount factor, under the same measure Q, as
dD (t, T ) = r (t) D (t, T ) dt + σT D (t, T ) dz (t)
where σT is the volatility of instantaneous percentage changes of the discount factor. Apply-
ing Ito’s lemma we have
r (t) D (t, T ) = ∂D (t, T )
∂t
+ µr
∂D (t, T )
∂r
+ 1
2σ 2
r
∂2D (t, T )
∂r2
which is a partial differential equation ruling out arbitrage opportunities.
It may be proved that in the particular case in which
µr = α + βr
σ 2
r = γ + ζr
that is, in the case in which both the drift and the instantaneous variance are linear in the
risk factor, the solution is
D (t, T ) = exp [A (T −t) −M (T −t) r (t)]
These models are called affine factor models, because interest rates are affine functions
of the risk factor.
The general shape of the instantaneous drift used in one-factor affine models is µr =
k (θ −r), so that the interest rate is recalled toward a long run equilibrium level θ: this
feature of the model is called mean reversion. Setting ζ = 0 and γ > 0 then leads to the
Vasicek model, in which the conditional distribution of the instantaneous interest rate is
normal. Alternatively, assuming ζ > 0 and γ = 0 then leads to the famous Cox, Ingersoll
and Ross model: the stochastic process followed by the instantaneous interest rate is a square
root process, and the conditional distribution is non-central chi-square. The case in which
ζ > 0 and γ > 0 is a more general process studied in Pearson and Sun (1994). Finally, the
affine factor model result was proved in full generality with an extension to an arbitrary
number of risk factors by Duffie and Kan (1996).
Looking at the solution for the discount factor D (t, T ), it is clear that the function
M (T −t) is particularly relevant, because it represents its sensitivity to the risk factor r(t).
In fact, using Ito’s lemma we may write the dynamics of D (t, T ) under the risk-neutral
measure as
dD (t, T ) = r (t) D (t, T ) dt + σT M (T −t) D (t, T ) dz (t)

Derivatives Pricing, Hedging and Risk Management
15
1.4.2
Forward martingale measure
Consider now the problem of pricing a contingent claim whose pay-off is a function of the
interest rate. Remember that, differently from the Black–Scholes framework, the discount
factor to be applied to the contingent claim is now stochastic and, if the underlying is an
interest rate sensitive product, it is not independent from the pay-off. The consequence is
that the discount factor and the expected pay-off under the risk-neutral measure cannot be
factorized. To make a simple example, consider a call option written on a zero coupon bond
maturing at time T , for strike K and exercise time τ. We have:
CALL (D (t, T ) , t; τ, K) = EQ

exp

−
 τ
t
r (u) du

max [D (τ, T ) −K, 0]| ℑt

̸= EQ

exp

−
 τ
t
r (u) du
 ℑt

EQ [max [D (τ, T ) −K, 0]| ℑt]
and the price cannot be expressed as the product of the discount factor D (t, τ) and the
expected pay-off. Factorization can, however, be achieved through a suitable change of
measure.
Consider the discount factors evaluated at time t for one unit of currency to be received at
time τ and T respectively, with τ < T . Their dynamics under the risk-neutral measure are
dD (t, T ) = r (t) D (t, T ) dt + σT D (t, T ) dz (t)
dD (t, τ) = r (t) D (t, τ) dt + στD (t, τ) dz (t)
We can define D (t, τ, T ) as the forward price set at time t for an investment starting
at time τ and yielding one unit of currency at time T . A standard no-arbitrage argument
yields
D (t, τ, T ) = D (t, T )
D (t, τ)
The dynamics of the forward price can be recovered by using Ito’s division rule.
Remark 1.1 [Ito’s division rule]
Assume two diffusive processes X (t) and Y (t) follow-
ing the dynamics
dX (t) = µXX (t) dt + σXX (t) dz (t)
dY (t) = µY Y (t) dt + σY Y (t) dz (t)
Then, the process F (t) ≡X (t) /Y (t) follows the dynamics
dF (t) = µF F (t) dt + σF F (t) dz (t)
with
σF = σX −σY
µF = µX −µY −σF σY

16
Copula Methods in Finance
Applying this result to our problem yields immediately
dD (t, τ, T ) = −σF στD (t, τ, T ) dt + σF D (t, τ, T ) dz (t)
σF = σT −στ
We may now use the Girsanov theorem to recover a new measure Qτ under which
d
z = dz −στdt is a Wiener process. We have then
dD (t, τ, T ) = σF D (t, τ, T ) d
z (t)
and the forward price is a martingale. Under such a measure, the forward price of any future
contract is equal to the expected spot value. We have
D (t, τ, T ) = EQτ [(D (τ, τ, T )) | ℑt] = EQτ [(D (τ, T )) | ℑt]
and the measure Qτ is called the forward martingale measure. This result, which was first
introduced by Geman (1989) and Jamshidian (1989), is very useful to price interest rate
derivatives. In fact, consider a derivative contract g, written on D (t, T ), promising the
pay-off G (D (τ, T ) , τ) at time τ. As g (t) /D (t, τ) is a martingale, we have immediately
g (D (t, τ, T ) , t) = P (t, τ) EQτ [G (D (τ, T ) , τ) | ℑt]
and the factorization of the discount factor and expected pay-off is now correct.
To conclude, the cookbook recipe emerging from the forward martingale approach is that
the forward price must be considered as the underlying asset of the derivative contract,
instead of the spot.
1.4.3
LIBOR market model
While the standard classical interest rate pricing models are based on the dynamics of
instantaneous spot and forward rates, the market practice is to refer to observed interest
rates for investment over discrete time periods. In particular, the reference rate mostly used
for short-term investments and indexed products is the 3-month LIBOR rate. Moreover,
under market conventions, interest rates for investments below the one-year horizon are
computed under simple compounding. So, the LIBOR interest rate for investment from t to
T is defined as
L (t, T ) =
1
T −t
	
1
D (t, T ) −1

The corresponding forward rate is defined as
L (t, τ, T ) =
1
T −τ
	
1
D (t, τ, T ) −1

=
1
T −τ
	 D (t, τ)
D (t, T ) −1

Notice that, under the forward martingale measure QT , we have immediately
L (t, τ, T ) = EQT [L (τ, τ, T ) | ℑt] = EQT [L (τ, T ) | ℑt]

Derivatives Pricing, Hedging and Risk Management
17
The price of a floater, i.e. a bond whose coupon stream is indexed to the LIBOR, is then
evaluated as
FLOATER(t, tN) =
N

j=1
δiEQ[D(t, tj)L(tj−1, tj) | ℑt] + P (t, tN)
=
N

j=1
δiD(t, tj)EQtj [L(tj−1, tj) | ℑt] + P (t, tN)
=
N

j=1
D(t, tj)δiL(t, tj−1, tj) + P (t, tN)
where the set {t, t1, t2, . . . , tN} contains the dates at which a coupon is reset and the previous
one is paid and δj = tj −tj−1. Consider now a stream of call options written on the index
rate for each coupon period. This product is called a cap, and the price is obtained, assuming
a strike rate LCAP, from
CAP(t, t1, tN) =
N

j=2
δiEQ[D(t, tj) max(L(tj−1, tj) −LCAP), 0 | ℑt]
=
N

j=2
δiD(t, tj)EQtj [max(L(tj−1, tj) −LCAP), 0 | ℑt]
and each call option is called caplet. By the same token, a stream of put options are called
floor, and are evaluated as
FLOOR(t, t1, tN) =
N

j=1
δ2D(t, tj)EQtj [max(LFLOOR −L(tj−1, tj)), 0 | ℑt]
where LFLOOR is the strike rate. The names cap and floor derive from the results, which
may be easily verified
L(tj, tj−1) −CAPLET(tj, tj−1) = min(L(tj−1, tj), LCAP)
L(tj, tj−1) + FLOORLET(tj, tj−1) = max(L(tj−1, tj), LFLOOR)
Setting a cap and a floor amounts to building a collar, that is a band in which the coupon
is allowed to float according to the interest rate. The price of each caplet and floorlet can
then be computed under the corresponding forward measure. Under the assumption that each
forward rate is log-normally distributed, we may again recover a pricing formula largely
used in the market, known as Black’s formula.
CAPLET(t; tj, tj−1) = D(t, tj)EQtj [max(L(tj−1, tj) −LCAP), 0 | ℑt]
= D(t, tj){EQtj [L(tj−1, tj) | ℑt]N(d1) −LCAPN(d2)}
= D(t, tj)L(t, tj−1, tj)N(d1) −D(t, tj)LCAPN(d2)

18
Copula Methods in Finance
d1 =
ln(L(t, tj−1, tj)/LCAP) + σ 2
j (tj −t)
σj√tj −t
d2 = d1 −σj

tj −t
where σj is the instantaneous volatility of the logarithm of the forward rate L

t, tj−1, tj

.
The floorlet price is obtained by using the corresponding put option formula
FLOORLET(t; tj, tj−1) = −D(t, tj)L(t, tj−1, tj)N(−d1) + D(t, tj)LCAPN(−d2)
d1 =
ln(L(t, tj−1, tj)/LFLOOR) + σ 2
j (tj −t)
σj√tj −t
d2 = d1 −σj

tj −t
1.5
SMILE AND TERM STRUCTURE EFFECTS OF VOLATILITY
The Black–Scholes model, which, as we saw, can be applied to the pricing of contingent
claims on several markets, has been severely challenged by the data. The contradiction
emerges from a look at the market quotes of options and a comparison with the implied
information, that is, with the dynamics of the underlying that would make these prices
consistent. In the Black–Scholes setting, this information is collected in the same parameter,
volatility, which is assumed to be constant both across time and different states of the world.
This parameter, called implied volatility, represents a sufficient statistic for the risk-neutral
probability in the Black–Scholes setting: the instantaneous rate of returns on the assets are
in fact assumed normal and with first moments equal to the risk-free rate. Contrary to this
assumption, implied volatility is typically different both across different strike prices and
different maturities. The first evidence is called the smile effect and the second is called the
volatility term structure.
Non-constant implied volatility can be traced back to market imperfections or it may
actually imply that the stochastic process assumed for the underlying asset is not borne out
by the data, namely that the rate of return on the assets is not normally distributed. The
latter interpretation is indeed supported by a long history of evidence on non-normality of
returns on almost every market. This raises the question of which model to adopt to get a
better fit of the risk-neutral distribution and market data.
1.5.1
Stochastic volatility models
A first approach is to model volatility as a second risk factor affecting the price of the
derivative contract. This implies two aspects, which may make the model involved. The
first is the dependence structure between volatility and the underlying. The second is that
the risk factor represented by volatility must be provided with a market price, something
that makes the model harder to calibrate.
A model that is particularly easy to handle, and reminds us of the Hull and White (1987)
model, could be based on the assumption that volatility risk is not priced in the market,
and volatility is orthogonal to the price of the underlying. The idea is that conditional on a
given volatility parameter taking value s, the stochastic process followed by the underlying
asset follows a geometric brownian motion. The conditional value of the call would then

Derivatives Pricing, Hedging and Risk Management
19
yield the standard Black–Scholes solution. As volatility is stochastic and is not known at
the time of evaluation, the option is priced by integrating the Black–Scholes formula times
the volatility density across its whole support. Analytically, the pricing formula for a call
option yields, for example,
CALL (S(t), t, σ(t); K, T ) =
 ∞
0
CALLBS (S, t; σ(t) = s, K, T ) qσ (s | ℑt) ds
where CALLBS denotes the Black–Scholes formula for call options and qσ (s | ℑt) repre-
sents the volatility conditional density.
Extensions of this model account for a dependence structure between volatility and the
underlying asset. A good example could be to model instantaneous variance as a square
root process, to exploit its property to be defined on the non-negative support only and
the possibility, for some parameter configurations, of making zero volatility an inaccessible
barrier. Indeed, this idea is used both in Heston (1993) and in Longstaff and Schwartz
(1992) for interest rate derivatives.
1.5.2
Local volatility models
A different idea is to make the representation of the diffusive process more general by
modeling volatility as a function of the underlying asset and time. We have then, under the
risk-neutral measure
dS (t) = rS (t) dt + σ (S, t) S (t) dz (t)
The function σ (S, t) is called the local volatility surface and should then be calibrated in
such a way as to produce the smile and volatility term structure effects actually observed
on the market. A long-dated proposal is represented by the so-called constant elasticity of
variance (CEV) models, in which
dS (t) = rS (t) dt + σS (t)α dz (t)
Alternative local volatility specifications were proposed to comply with techniques that are
commonly used by practitioners in the market to fit the smile. An idea is to resort to the so-
called mixture of log-normal or shifted log-normal distributions. Intuitively, this approach
leads to closed form valuations. For example, assuming that the risk-neutral probability
distribution Q is represented by a linear combination of n log-normal distributions Qj
Q (S (T ) | ℑt) =
n

j=1
λjQj

Xj (T ) | ℑt

where Xj are latent random variables drawn from log-normal distributions Qj, correspond-
ing to geometric brownian motions with volatility σj. It may be checked that the price of
a call option in this model can be recovered as
CALL (S(t), t; K, T ) =
n

j=1
λjCALLBS

Xj, t; K, T


20
Copula Methods in Finance
Brigo and Mercurio (2001) provide the corresponding local volatility specification corre-
sponding to this model, obtaining
dS(t) = rS(t) dt +




n
j=1 σ 2
j λjqj(Xj(T ) | ℑt)
n
j=1 λjqj(Xj(T ) | ℑt)
S(t) dz(t)
where qj

Xj (T ) | ℑt

are the densities corresponding to the distribution functions Qj.
Once the mixture weights λj are recovered from observed plain vanilla option prices,
the corresponding dynamics of the underlying asset under the risk-neutral measure can
be simulated in order to price exotic products.
1.5.3
Implied probability
A different idea is to use non-parametric techniques to extract general information con-
cerning the risk-neutral probability distribution and dynamics implied by observed options
market quotes. The concept was first suggested by Breeden and Litzenberger (1978) and
pushes forward the usual implied volatility idea commonly used in the Black–Scholes
framework. This is the approach that we will use in this book.
The basic concepts stem from the martingale representation of option prices. Take, for
example, a call option
CALL (S, t; K, T ) = exp [−r (T −t)] EQ [max (S (T ) −K, 0)]
By computing the derivative of the pricing function with respect to the strike K we easily
obtain
∂CALL (S, t; K, T )
∂K
= −exp [−r (T −t)] (1 −Q (K | ℑt))
where Q(K | ℑt) is the conditional distribution function under the risk-neutral measure.
Defining
Q (K | ℑt) ≡1 −Q (K | ℑt)
that is, the probability corresponding to the complementary event Pr (S (T ) > K), we may
rewrite
Q (K | ℑt) = −exp [r (T −t)] ∂CALL (S, t; K, T )
∂K
So, the risk-neutral probability of exercise of the call option is recovered from the forward
value of the derivative of the call option, apart from a change of sign. The result can be
immediately verified in the Black–Scholes model, where we easily compute Q (K | ℑt) =
N (d2 (K)).
Remark 1.2
Notice that by integrating the relationship above from K to infinity, the price
of the call option can also be written as
CALL (S, t; K, T ) = exp [−r (T −t)]
 ∞
K
Q (u | ℑt) du

Derivatives Pricing, Hedging and Risk Management
21
where we remark that the cumulative probability, rather than the density, appears in the
integrand. As we will see, this pricing representation will be used again and again throughout
this book.
Symmetric results hold for put prices which, in the martingale representation, are writ-
ten as
PUT (S, t; K, T ) = exp [−r (T −t)] EQ [max (K −S (T ) , 0)]
Computing the derivative with respect to the strike and reordering terms we have
Q (K | ℑt) = exp [r (T −t)] ∂PUT (S, t; K, T )
∂K
that is, the implied risk-neutral distribution. Again, we may check that, under the standard
Black–Scholes setting, we obtain
Q (K | ℑt) = N (−d2 (K)) = 1 −N (d2 (K))
Furthermore, integrating from zero to K we have
PUT (S, t; K, T ) = exp [−r (T −t)]
 K
0
Q (u | ℑt) du
Finally, notice that the density function can be obtained from the second derivatives of the
put and call prices. We have
q (K | ℑt) ≡∂Q (K | ℑt)
∂K
= exp [r (T −t)] ∂2PUT (S, t; K, T )
∂K2
q (K | ℑt) ≡−∂Q (K | ℑt)
∂K
= exp [r (T −t)] ∂2CALL (S, t; K, T )
∂K2
The strength of these results stems from the fact that they directly rely on the no-arbitrage
requirement imposed by the martingale relationship. In this sense, they are far more general
than the assumptions underlying the Black–Scholes setting. Indeed, if the assumptions
behind the Black–Scholes model were borne out by the data, the results above would be of
little use, as all the information sufficient to characterize the risk-neutral distribution would
be represented by the volatility implied by the prices. If the price distribution is not log-
normal, these results are instead extremely useful, enabling one to extract the risk-neutral
probability distribution, rather that its moments, directly from the option prices.
1.6
INCOMPLETE MARKETS
The most recent challenge to the standard derivative pricing model, and to its basic structure,
is represented by the incomplete market problem. A brief look over the strategy used to
recover the fair price of a derivative contract shows that a crucial role is played by the
assumption that the future value of each financial product can be exactly replicated by
some trading strategy. Technically, we say that each product is attainable and the market is

22
Copula Methods in Finance
complete. In other words, every contingent claim is endowed with a perfect hedge. Both in
the binomial and in the continuous time model we see that it is this assumption that leads
to two strong results. The first is a unique risk-neutral measure and, through that, a unique
price for each and every asset in the economy. The second is that this price is obtained with
no reference to any preference structure of the agents in the market, apart from the very
weak (and realistic) requirement that they “prefer more to less”.
Unfortunately, the completeness assumption has been fiercely challenged by the market.
Every trader has always been well aware that no perfect hedge exists, but the structure of
derivatives markets nowadays has made consideration of this piece of truth unavoidable.
Structured finance has brought about a huge proliferation of customized and exotic products.
Hedge funds manufacture and manage derivatives on exotic markets and illiquid products
to earn money from their misalignment: think particularly of long–short and relative value
hedge fund strategies. Credit derivatives markets have been created to trade protection on
loans, bonds, or mortgage portfolios. All of this has been shifting the core of the derivatives
market away from the traditional underlying assets traded on the organized markets, such as
stocks and government bonds, toward contingent claims written on illiquid assets. The effect
has been to make the problem of finding a perfect hedge an impossible task for most of the
derivative pricing applications, and the assumption of complete markets an unacceptable
approximation. The hot topic in derivative pricing is then which hedge to choose, facing
the reality that no hedging strategy can be considered completely safe.
1.6.1
Back to utility theory
The main effect of accounting for market incompleteness has been to bring utility theory
back in derivative pricing techniques. Intuitively, if no perfect hedge exists, every replication
strategy is a lottery, and selecting one amounts to defining a preference ranking among
them, which is the main subject of utility theory. In a sense, the ironic fate of finance is
that the market incompleteness problem is bringing it back from a preference-free paradigm
to a use of utility theory very similar to early portfolio theory applications: this trend is
clearly witnessed by terms such as “minimum variance hedging” (Follmer & Schweitzer,
1991). Of course, we know that the minimum variance principle is based on restrictive
assumptions concerning both the preference structure and the distributional properties of
the hedging error. One extension is to use more general expected utility representations,
such as exponential or power preferences, to select a specific hedging strategy and the
corresponding martingale measure (Frittelli, 2000).
A question that could also be useful to debate, even though it is well beyond the scope
of this book, is whether the axiomatic structure leading to the standard expected utility
framework is flexible enough and appropriate to be applied to the hedging error problem.
More precisely, it is well known that standard expected utility results rest on the so-called
independence axiom, which has been debated and criticized in decision theory for decades,
and which seems particularly relevant to the problem at hand. To explain the problem in
plain words, consider you prefer hedging strategy A to another denoted B (A ⪰B). The
independence axiom reads that you will also prefer αA + (1 −α) C to αB + (1 −α) C
for every α ∈[0, 1], and for whatever strategy C. This is the crucial point: the preference
structure between two hedging strategies is preserved under a mixture with any other third
strategy, and if this is not true the expected utility results do not carry over. It is not difficult
to argue that this assumption may be too restrictive, if, for example, one considers a hedging

Derivatives Pricing, Hedging and Risk Management
23
strategy C counter-monotone to B and orthogonal to A. Indeed, most of the developments
in decision theory were motivated by the need to account for the possibility of hedging
relationships among strategies, that are not allowed for under the standard expected utility
framework. The solutions proposed are typically the restriction of the independence axiom
to a subset of the available strategies. Among them, an interesting choice is to restrict C
to the set of so-called constant acts, which in our application means a strategy yielding
a risk-free return. This was proposed by Gilboa and Schmeidler (1989) and leads to a
decision strategy called Maximin Expected Utility (MMEU). In intuitive terms, this strategy
can be described as one taking into account the worst possible probability scenario for every
possible event. As we are going to see in the following paragraph, this worst probability
scenario corresponds to what in the mathematics of incomplete market pricing are called
super-replication or super-hedging strategies.
1.6.2
Super-hedging strategies
Here we follow Cherubini (1997) and Cherubini and Della Lunga (2001) in order to provide
a general formal representation of the incomplete market problem, i.e. the problem of pricing
a contingent claim on an asset that cannot be exactly replicated. In this setting, a general
contingent claim g(S, t) with pay-off G(S, T ), can be priced computing
g (S, t) = exp [−r (T −t)] EQ

G (S, T ) ; Q ∈℘| ℑt

where EQ represents the expectation with respect to a conditional risk-neutral measure Q.
Here and in the following we focus on the financial meaning of the issue and assume that
the technical conditions required to ensure that the problem is well-defined are met (the
readers are referred to Delbaen & Schachermayer, 1994, for details). The set ℘contains
the risk-neutral measures and describes the information available on the underlying asset.
If it is very precise, and the set ℘contains a single probability measure, we are in the
standard complete market pricing setting tackled above. In the case in which we do not
have precise information – for example, because of limited liquidity of the underlying – we
have the problem of choosing a single probability measure, or a pricing strategy. Therefore,
in order to price the contingent claim g in this incomplete market setting, we have to define:
(i) the set of probability measures ℘and (ii) a set of rules describing a strategy to select
the appropriate measure and price. As discussed above, one could resort to expected utility
to give a preference rank for the probabilities in the set, picking out the optimal one. As
an alternative, or prior to that, one could instead rely on some more conservative strategy,
selecting a range of prices: the bounds of this range would yield the highest and lowest price
consistent with the no-arbitrage assumption, and the replicating strategies corresponding to
these bounds are known as super-replicating portfolios. In this case we have
g−(S, t) = exp [−r (T −t)] inf EQ

G (S, T ) ; Q ∈℘| ℑt

g+ (S, t) = exp [−r (T −t)] sup EQ

G (S, T ) ; Q ∈℘| ℑt

More explicitly, the lower bound is called the buyer price of the derivative contract g, while
the upper bound is denoted the seller price. The idea is that if the price were lower than
the buyer price, one could buy the contingent claim and go short a replicating portfolio
ending up with an arbitrage gain. Conversely, if the price were higher than the maximum,

24
Copula Methods in Finance
one could short the asset and buy a replicating portfolio earning a safe return. Depending
on the definition of the set of probability measures, one is then allowed to recover different
values for long and short positions. Notice that this does not hold for models that address
the incomplete market pricing problem in a standard expected utility setting, in which the
selected measure yields the same value for long and short positions.
Uncertain probability model
The most radical way to address the problem of super-replication is to take the worst possible
probability scenario for every event. To take the simplest case, that of a call digital option
paying one unit of currency at time T if the underlying asset is greater than or equal to K,
we have
DC−(S, t) = exp [−r (T −t)] inf EQ

1S(T )⩾K; Q ∈℘| ℑt

= exp [−r (T −t)] inf

Q (K) ; Q ∈℘| ℑt

≡B (t, T ) Q
−
DC+ (S, t) = exp [−r (T −t)] sup EQ

1S(T )⩾K; Q ∈℘| ℑt

= exp [−r (T −t)] sup EQ

Q (K) ; Q ∈℘| ℑt

≡B (t, T ) Q
+
where we recall the definition Q (K) ≡1 −Q (K) and where the subscripts ‘+’ and ‘−’
stand for the upper and lower value of Q (K).
Having defined the pricing bounds for the digital option, which represents the pricing ker-
nel of any contingent claim written on asset S, we may proceed to obtain pricing bounds for
call and put options using the integral representations recovered in section 1.5.3. Remember
in fact that the price of a European call option C under the martingale measure Q may be
written in very general terms as
CALL (S, t; K, T ) = exp [−r (T −t)]
 ∞
K
Q (u | ℑt) du
We know that if the kernel were the log-normal distribution, the equation would yield the
Black–Scholes formula. Here we want instead to use the formula to recover the pricing
bounds for the option. The buyer price is then obtained by solving the problem
CALL−(S, t; K, T ) = exp [−r (T −t)]
 ∞
K
Q
−(u) du
By the same token, the seller price is obtained from
CALL+ (S, t; K, T ) = exp [−r (T −t)]
 ∞
K
Q
+ (u) du
and represents the corresponding upper bound for the value of the call option in the most
general setting.
The same could be done for the European put option with the same strike and maturity.
In this case we would have
PUT (S, t; K, T ) = exp [−r (T −t)]
 K
0
Q (u | ℑt) du

Derivatives Pricing, Hedging and Risk Management
25
for any conditional measure Q ∈℘and the pricing bounds would be
PUT−(S, t; K, T ) = exp [−r (T −t)]
 K
0
Q−(u | ℑt) du
PUT+ (S, t; K, T ) = exp [−r (T −t)]
 K
0
Q+ (u | ℑt) du
where Q−(u) and Q+ (u) have the obvious meanings of the lower and upper bound of the
probability distribution for every u. Notice that whatever pricing kernel, Q in the ℘set
has to be a probability measure, so it follows that Q (u) + Q (u) = 1. This implies that we
must have
Q−(u) + Q
+ (u) = 1
Q+ (u) + Q
−(u) = 1
In the case of incomplete markets, in which the set ℘is not a singleton, we have Q−(u) <
Q+ (u), which implies
Q−(u) + Q
−(u) = Q−(u) +

1 −Q+ (u)

< 1
and the measure Q−is sub-additive. In the same way, it is straightforward to check that
Q+ (u) + Q
+ (u) > 1
and the measure Q+ is super-additive.
So, if we describe the probability set as above, the result is that the buyer and seller prices
are integrals with respect to non-additive measures, technically known as capacities. The
integrals defined above are well defined even for non-additive measures, in which case they
are known in the literature as Choquet integrals. This integral is in fact widely used in the
modern decision theory trying to amend the standard expected utility framework: lotteries
are ranked using capacities instead of probability measures and expected values are defined
in terms of Choquet integrals rather than Lebesgue integrals, as is usual in the standard
expected utility framework.
Example 1.2 [Fuzzy measure model]
A particular parametric form of the approach above
was proposed by Cherubini (1997) and Cherubini and Della Lunga (2001). The idea is
drawn from fuzzy measure theory: the parametric form suggested is called Sugeno fuzzy
measure. Given a probability distribution Q and a parameter λ ∈ℜ+, define
Q
−(u) = 1 −Q (u)
1 + λQ (u)
Q
+ (u) =
1 −Q (u)
1 + λ∗Q (u)
with
λ∗= −
λ
1 + λ

26
Copula Methods in Finance
It may be easily checked that the measure Q−is sub-additive, and Q+ is the dual
super-additive measure in the sense described above.
The pricing bounds for call options are then recovered as discussed above based on any
choice of the reference probability distribution Q. If the pricing kernel is chosen to be
log-normal, we obtain
CALL−(S, t; K, T ) = exp [−r (T −t)]
 ∞
d2

 (u)
1 + λ
 (−u)du
CALL+ (S, t; K, T ) = exp [−r (T −t)]
 ∞
d2

 (u)
1 + λ∗
 (−u)du
Notice that in the case λ = λ∗= 0 the model yields the Black–Scholes formula. For any
value λ > 0, the model yields buyer and seller prices. The discount (premium) applied to
buyer (seller) prices is higher the more the option is out-of-the-money.
Uncertain volatility model
An alternative strategy to address the incomplete market problem would be to define a set
of risk-neutral dynamics of the underlying asset, rather than the set of risk-neutral measures.
A typical example is to assume that the volatility parameter is not known exactly, and is
considered to be included in a given interval. Assume further that the stochastic process
followed by the underlying asset is a geometric brownian motion. Under any risk-neutral
measure Q we have
dS (t) = rS (t) dt + σS (t) dz
and we assume that σ ∈

σ −, σ +
. This model is called the uncertain volatility model
(UVM) and is due to Avellaneda, Levy and Par`as (1995) and Avellaneda and Par`as (1996).
Working through the solution as in the standard Black–Scholes framework, assume to
build a dynamic hedged portfolio. Notice that if we knew the exact value of the σ parameter,
the delta hedging strategy could be designed precisely, enabling perfect replication of the
contingent claim. Unfortunately, we are only allowed to know the interval in which the true
volatility value is likely to be located, and we are not aware of any probability distribution
about it. Assume that we take a conservative strategy designing the hedging policy under
the worst possible volatility scenario. Avellaneda, Levy and Par`as (1995) show that this
leads to the pricing formula
∂g
∂t + 1
2σ 2S2 (t)
∂2g
∂S2
+
+ rS ∂g
∂S −rg = 0
with
∂2g
∂S2
+
=

σ −
(∂2g/∂S2) > 0
σ +
(∂2g/∂S2) < 0

Notice that the partial differential equation is a modified non-linear version of the Black–
Scholes no-arbitrage condition. The non-linearity is given by the fact that the multiplicative

Derivatives Pricing, Hedging and Risk Management
27
term of the second partial derivative is a function of the sign of the second partial derivative.
This equation was denoted the BSB (Black, Scholes & Barenblatt) fundamental equation.
The solution has to be carried out numerically except in trivial cases in which it may be
proved that the solution is globally convex or concave, when it obviously delivers the same
results as the standard Black–Scholes model. Notice also that in this approach, as in the
previous uncertain probability model, the result yields different values for long and short
positions.
1.7
CREDIT RISK
The recent developments of the market have brought about a large increase of credit risk
exposures and products. On the one hand, this has been due to the massive shift of the
investment practices from standard stocks and bonds products toward the so-called alterna-
tive investments. This shift has been motivated both by the quest for portfolio diversification
and the research of higher returns in a low interest rate period. Moreover, another face of
credit risk has become increasingly relevant along with the progressive shift from the clas-
sical standard intermediation business toward structured finance products, and the need to
resort to over-the-counter (OTC) transactions to hedge the corresponding exposure. Con-
trary to what happens in derivatives transactions operated in futures-style organized markets,
OTC deals involve some credit risk, as the counterparty in the contract may default by the
time it has to honor its obligations. The credit-risk feature involved in derivative con-
tracts is known as counterparty risk, and has been getting all the more relevant in the risk
management debate.
A very general way to represent the pay-off of a defaultable contingent claim – that is,
a contract in which the counterparty may go bankrupt – is
G (S, T ) [1 −1{DEF}(T )LGD]
where 1{DEF} is the indicator function denoting the default of the counterparty by time T
and LGD is the loss given default figure, also defined as LGD ≡1 −RR, that is one minus
the recovery rate. In very general terms, the value of the contract at time t is computed
under the risk-neutral measure as
EQ

exp

−
 T
t
r (u) du

G (S, T ) [1 −1{DEF}LGD]

Notice that there are three risk factors involved in this representation: (i) market risk due
to fluctuations of the underlying asset S; (ii) interest rate risk due to changes in the discount
factor; and (iii) credit risk due to the event of default of the counterparty. We will see that
evaluating defaultable contingent claims in this framework crucially involves the evaluation
of the dependence structure among the sources of risk involved. Fortunately, we know that
one of the sources may be made orthogonal by the change in measure corresponding to the
bond numeraire (forward martingale measure). In this case we have
D (t, T ) EQT [G (S, T ) [1 −1{DEF}LGD]]
and the credit risk problem is intrinsically bivariate, involving the dependence structure
between the underlying dynamics and default of the counterparty.

28
Copula Methods in Finance
The standard credit risk problem that we are used to think of is only the simplest case in
this general representation. Setting in fact G (S, T ) = 1 we have the standard defaultable
bond pricing problem. In the discussion below, we will first address this topic, before
extending it to the case in which the defaultable security is a derivative contract. Dealing
with the simplest case will enable us to stress that credit risk itself is similar to an exposure in
the derivative market. Curiously enough, it can be seen as a position in an option, following
the so-called structural approach, or as a position with the same features as an interest rate
derivative, according the so-called reduced form approach.
1.7.1
Structural models
Structural models draw the main idea from the pioneering paper by Merton (1974). Assume
that an entrepreneur is funding a project whose value is V (t) with debt issued in the form
of a zero coupon bond with a face value of DD. The debt is reimbursed at time T . If at
that date the value of the asset side of the firm is high enough to cover the value of debt,
the nominal value is repaid and equityholders get the remaining value. If instead the value
of the firm is not sufficient to repay the debt, it is assumed that the debtholders take over
the firm at no cost, and stockholders get zero (a feature called limited liability). The pay-off
value of debt at maturity is then min(DD, V (T )), while the value of equity is what is left
after bondholders have been repaid (we say stockholders are residual claimants).
C (T ) = max(V (T ) −DD, 0)
The value of equity capital is then the value of a call option written on the asset value
of the firm for a strike equal to the face value of the debt. Notice that the value of debt at
the same date can be decomposed alternatively as
DD (T ) = V (T ) −max(V (T ) −DD, 0)
or
DD (T ) = DD −max(DD −V (T ) , 0)
The latter representation is particularly instructive. The value of defaultable debt is the
same as that of default-free debt plus a short position in a put option written on the asset
value of the firm for a strike equal to the face value of debt. Notice that if put–call parity
holds we have
V (T ) = max(V (T ) −DD, 0) + DD −max(DD −V (T ) , 0)
and the value of the firm is equal to the value of equity, the call option, plus the value of
debt, in turn decomposed into default-free debt minus a put option. This result is known
in the corporate finance literature as the Modigliani–Miller theorem. Let us remark that it
is not a simple accounting identity, but rather a separation result: it means that the value
of the asset side of a firm is invariant under different funding policies; to put it another
way, following an increase in the amount of nominal debt its value increases exactly by the
same amount as the decrease in the value of equity. It is well known that this is only true
under very restrictive assumptions, such as the absence of taxes and bankruptcy costs, or

Derivatives Pricing, Hedging and Risk Management
29
agency costs. Accounting for all of these effects would imply a break-up of the relationship
above, and the choice of the amount of debt would have a feedback effect on the output of
the firm.
Apart from such possible complications, it is clear that option theory could be applied to
recover both the value of debt and equity, and to decompose debt into the default-free part
and the credit risk premium.
Assume that the asset side of the firm V (t) follows a geometric brownian motion, so
that under the risk-neutral measure we have
dV (t) = rV (t) dt + σV V (t) dz (t)
Then, the standard Black–Scholes formula can be applied to yield the value of equity C
C (t) = V (t) 
 (d1) −exp (−r (T −t)) DD
 (d2)
d1 = ln(V (t) /DD) + (r + σ 2
V /2) (T −t)
σV
√
T −t
d2 = d1 −σV
√
T −t
and the value of debt DD is recovered as
DD(t) = V (t) −[V (t)
(d1) −exp(−r(T −t))DD
(d2)]
= 
(−d1)V (t) + exp(−r(T −t))DD
(d2)
Notice that, by adding and subtracting exp (−r (T −t)) DD we can rewrite the value as
DD (t) = exp (−r (T −t)) DD −

−V (t) 
 (−d1) + exp (−r (T −t)) DD
 (−d2)

and we recognize the short position in the put option representing credit risk.
The result could be rewritten by defining the underlying asset of the option in percentage
terms, rather than in money amounts. For this reason, we introduce
d = exp (−r (T −t)) DD
V (t)
which is called by Merton quasi-debt-to-firm-value ratio or quasi-leverage. The quasi term
is motivated by the fact that the debt is discounted using the risk-free rate rather than the
defaultable discount factor. We have
DD (t) = exp (−r (T −t)) DD

1 −

−1
d 
 (−d1) + 
 (−d2)

d1 = ln (1/d) + σ 2
V /2 (T −t)
σV
√
T −t
d2 = d1 −σV
√
T −t

30
Copula Methods in Finance
Remembering that the probability of exercise of a put option is equal to 
 (−d2), a
modern way to rewrite the formula above would be
DD (t) = exp (−r (T −t)) DD

1 −
 (−d2)

1 −1
d

 (−d1)

 (−d2)

= exp (−r (T −t)) DD {1 −Dp ∗LGD}
where Dp stands for default probability and LGD is the loss given default figure in this
model.
Dp = 
 (−d2)
LGD = 1 −1
d

 (−d1)

 (−d2)
Notice that both the default probability and the loss given default are dependent on the
quasi leverage d.
Finally, in order to account for different maturities, credit risk can be represented in terms
of credit spreads as
r∗(t, T ) −r = −
ln

1 −
 (−d2)

1 −1
d

 (−d1)

 (−d2)

T −t
= −ln {1 −Dp ∗LGD}
T −t
where r∗(t, T ) is the yield to maturity of the defaultable bond.
While the original model is based on very restrictive assumptions, some extensions have
been proposed to make it more realistic. In particular, the extension to defaultable coupon
bond debt was handled in Geske (1977), while the possibility of default events prior to
maturity as well as the effects of debt seniority structures was tackled in Black and Cox
(1976). Finally, the effects of bankruptcy costs, strategic debt servicing behavior and absolute
priority violations were taken into account in Anderson and Sundaresan (1996) and Madan
and Unal (2000).
Structural models represent a particularly elegant approach to defaultable bond evaluation
and convey the main idea that credit risk basically amounts to a short position in an option.
Unfortunately, the hypothesis that both the recovery rate and default probability depend
on the same state variable, i.e. the value of the firm, may represent a serious drawback to
the flexibility of the model, overlooking other events that may trigger default. As a result,
the credit spreads that are generated by this model consistently with reasonable values of
asset volatility turn out to be much smaller than those actually observed on the market.
Furthermore, the fact that the value of the asset is modeled as a diffusive process observed
in continuous time gives a typical hump-shaped credit spread curve (in the usual case with
d < 1) with zero intercept: technically speaking this is due to the fact that default is a
predictable event with respect to the information set available at any time t. Three different
ways have been suggested to solve this problem: the first is to include a jump in the process
followed by the value of assets (Zhou, 1996); the second is to assume that the value of
the underlying is not observable in continuous time (Duffie & Lando, 2001); the third is
to assume that the default barrier is not observed at any time t (the CreditGrades approach
followed by Finger et al., 2002).

Derivatives Pricing, Hedging and Risk Management
31
1.7.2
Reduced form models
A more radical approach to yield a flexible parametric representation for the credit spreads
observed in the market is to model default probability and loss given default separately. By
contrast with structural models, this approach is called the reduced form.
Assuming the recovery rate to be exogenously given, the most straightforward idea is
to model the default event as a Poisson process. We know that the probability distribution
of this process is indexed by a parameter called intensity (or hazard rate): for this reason,
these models are also called intensity based. If γ is the intensity of the Poisson process
representing default, the probability that this event will not occur by time T is described by
the function
Pr (τ > T ) = exp

−γ (T −t)

where we assume τ > t, that is, the firm is not in default as of time t. Assume that under
the risk-neutral measure Q we have
EQ[1 −1DEF] ≡Pr (τ > T ) = exp

−γ (T −t)

and that the default event is independent of interest rate fluctuations. Furthermore, let us
assume that the recovery rate RR is equal to zero, so that the whole principal is lost in case
of default. Under these assumptions, the price of a defaultable zero-coupon bond maturing
at time T is simply
DD (t, T ; RR = 0) = D (t, T ) EQ [1 −1DEF]
= D (t, T ) exp

−γ (T −t)

and the credit spread is obtained as
r∗(t, T ; RR = 0) −r (t, T ) ≡
	
−ln DD (t, T ; RR = 0)
T −t

−
	
−ln D (t, T )
T −t

= γ
In this special case the credit spread curve is flat and equal to the intensity figure of the
default process.
In the more general case of a positive recovery rate RR ≡1 −LGD, assumed to be
non-stochastic, we have instead
DD (t, T ; RR) = D (t, T ) EQ [1 −1DEFLGD]
= D (t, T ) EQ [(1 −1DEF) + RR1DEF]
= D (t, T )

RR + (1 −RR) EQ [(1 −1DEF)]

= D (t, T ) RR + (1 −RR) D (t, T ) EQ [(1 −1DEF)]
= D (t, T ) RR + (1 −RR) DD (t, T ; RR = 0)
So, the value of the defaultable bond is recovered as a portfolio of an investment in
the default-free bond, and one in a defaultable bond with the same default probability and
recovery rate zero.

32
Copula Methods in Finance
In terms of credit spreads we have
r∗(t, T ; RR) −r(t, T ) = −ln{RR + (1 −RR) exp[−γ (T −t)]}
T −t
Notice that in this case the term structure of the credit spreads is not flat, even though
the intensity is still assumed constant.
A natural extension of the model is to assume the intensity to be stochastic. In this case,
the default event is said to follow what is called a Cox process. The survival probability of
the obligor beyond time T is determined as
EQ [1 −1DEF] ≡Pr (τ > T ) = EQ

exp

−
 T
t
γ (u) du

It is easy to see that, from a mathematical point of view, the framework is much the
same as that of interest rate models. These techniques can then be directly applied to the
evaluation of credit spreads.
Affine intensity
As an example, assume that the instantaneous intensity γ (t) follows a diffusive process
dynamics under the risk neutral measure Q
dγ (t) = k (γ −γ (t)) dt + σγ α dw
For α = 0,1 we know that the model is affine and we know that the solution to
EQ [1 −1DEF] = EQ

exp

−
 T
t
γ (u) du

is
EQ

exp

−
 T
t
γ (u) du

= exp

A (T −t) + M (T −t) γ (t)

The value of a defaultable discount bond is then
DD(t, T ; RR) = D(t, T )RR + (1 −RR)DD(t, T ; RR = 0)
= D(t, T ){RR + (1 −RR) exp[A(T −t) + M(T −t)γ (t)]}
Notice that using the framework of the forward martingale measure we can easily extend
the analysis to the case of correlation between interest rate and credit risk. In fact, we leave
the reader to check that the dynamics of the default intensity under such measure, which
we denoted QT , is
dγ (t) =

k (γ −γ (t)) −σT σγ α
dt + σγ αdw∗

Derivatives Pricing, Hedging and Risk Management
33
where we recall that σT is the instantaneous volatility of the default free zero-coupon bond
with maturity T . Using the dynamics above one can compute or simulate the price from
DD (t, T ; RR) = D (t, T ) RR + (1 −RR) D (t, T ) EQT

exp

−
 T
t
γ (u) du

A final comment is in order concerning the recovery rate. Extensions of the model refer
to a stochastic recovery rate. Of course, the extension is immediate as long as one is willing
to assume that the recovery rate is independent of the default intensity and interest rate. In
this case the expected value is simply substituted for the deterministic value assumed in the
analysis above. Obviously, as the support of the recovery rate is in the unit interval, one
has to choose a suitable probability distribution, which typically is the Beta. Accounting for
recovery risk, however, has not been investigated in depth.
Finally, consider that the choice of the amount with respect to which the recovery rate
is computed may be relevant for the analysis. There are three possible choices. The first is
to measure recovery rate with respect to the nominal value of the principal, as supposed in
Jarrow and Turnbull (1995) and Hull and White (1995). The second choice is to compute
it with respect to the market value of debt right before default, as in Duffie and Singleton
(1998). The last one, which is much more common in practice, is to compute it with respect
to principal plus accrued interest. Notice that with the last choice, we get the unfortunate
result that the value of a coupon bond cannot be decomposed into a stream of defaultable
zero-coupon bonds, and the analysis may turn out to be much more involved.
1.7.3
Implied default probabilities
A look at the models above shows that credit risk is evaluated drawing information from
different markets, in particular the equity market, for structural models, and the corporate
bond market, for reduced form models. Nowadays more information is implied in other
markets, such as the credit derivatives markets. A question is how to extract and combine
information from all of these markets to determine the implied risk-neutral default proba-
bility concerning a particular obligor. Here we give a brief account of the different choices
available.
Stock markets
A first choice, implicit in structural models, is to draw information from the equity market.
Taking the standard Merton model we have that
C (t) = V (t) 
 (d1) −exp (−r (T −t)) DD
 (d2)
where C (t) is the value of equity. As we know, this is a standard application of the
Black–Scholes formula, and we are interested in recovering the probability of exercise

 (d2). Let us remark that this probability is referred to the event that the option representing
equity ends up in the money, so that the company does not default. Default probability is then
1 −
 (d2) = 
 (−d2). The main difference with respect to the Black–Scholes framework

34
Copula Methods in Finance
is that in this case not only the volatility of the underlying asset σV , but also its current
value V (t), cannot be observed on the market. What we observe instead is the value of
equity C (t). Some other piece of information is needed to close the model. A possible
solution is to resort to some estimate of the volatility of equity, σC, which can be obtained
from the historical time series of prices or from the options traded on the stock. From Ito’s
lemma, we know that volatility of equity must satisfy
σC = σV 
 (d1) V (t)
C (t)
This equation, along with the Black–Scholes formula above, constitutes a non-linear system
of two equations in two unknowns that can be solved to yield the values of V (t) and σC
implied by market prices. The default probability is then recovered, under the risk-neutral
measure, as

(−d2) = 

−ln

V (T ) /DD

+

r −σ 2
V /2

(T −t)
σV
√T −t

The default probability under the objective measure can be recovered by simply substi-
tuting the actual drift µV of the asset value of the firm. The latter can be estimated either
from historical data or by resorting to the no-arbitrage relationship µV = r + λσV , where
λ is the market price of risk.
The solution described above is used in the very well known application of structural
models employed by KMV, a firm specialized in supplying default probability estimates
about many companies across the world, and recently purchased by Moody’s. We know
that a serious flaw of the Merton approach is that it underestimates the default probability.
The key KMV idea is to apply the argument of the default probability function, which they
denote distance to default
−ln

V (T ) /DD

+

µV −σ 2
V /2

(T −t)
σV
√
T −t
to fit the empirical distribution of actual historical defaults.
Example 1.3
Based on Standard and Poor’s statistics for the year 2001, the leverage
figures of AA and BBB industrial companies were equal to 26.4% and 41%. Using these
figures, an interest rate equal to 4% and a volatility of the asset side equal to 25% for
both firms, we compute a risk-neutral default probability over five years equal to 0.69%
and 4.71% respectively. Assuming a market price of risk equal to 6%, the corresponding
objective probabilities are 0.29% and 2.42% for the AA and the BBB firm.
Corporate bond markets
Reduced form models suggest that the information about default is in the observed prices
of corporate bonds. Given the zero-coupon-bond yield curve of debt issues from a single
obligor, and given a recovery rate figure RR we know that
DD (t, T ; RR) = D (t, T ) RR + (1 −RR) DD (t, T ; RR = 0)

Derivatives Pricing, Hedging and Risk Management
35
Furthermore, we know that the value of the zero-coupon with recovery rate zero implied in
this price is
DD (t, T ; RR = 0) = D (t, T ) Pr (τ > T )
where again we assume that interest rate risk and default risk are orthogonal. The implied
survival probability is then obtained from defaultable and non-defaultable bond prices as
Pr (τ > T ) = DD (t, T ; RR) /D (t, T ) −RR
1 −RR
Alternatively, a common practice in the market is to refer to asset swap spreads as
representative of the credit spread of a specific issue. To get the main idea behind this
practice, consider a defaultable coupon bond issued at par with coupon equal to r∗. We
know that if the bond issued were default-free, it could be swapped at the swap rate SR. We
remind the reader that the swap rate is defined as the coupon that equals the value of the
fixed leg to that of the floating one in a plain vanilla swap. So, the defaultable cash flow r∗
can be swapped against a stream of floating payments plus a spread equal to the difference
between the coupon and the swap rate. The advantage of using the asset swap spread is
that it conveys information on the riskiness of the individual bond, rather than a whole
set of bonds issued by the same entity, while the main flaw is that it may represent other
sources of risk, beyond that of default, linked to specific features of the issue, particularly its
liquidity. Furthermore, by its very nature it is not well suited to represent the term structure
of default risk and credit spreads. Typically, then, the asset swap spread is used to represent
a flat credit spread and default intensity curve.
Credit default swap markets
The process of financial innovation that has characterized the recent development credit
market has offered new tools to extract market information on the default risk of the main
obligors. Credit derivative products, which are used to transfer credit risk among financial
institutions, represent a natural source of information concerning the default risk. In particu-
lar, credit default swaps represent a very liquid market to extract such information. A credit
default swap is a contract in which one counterparty buys protection from the other against
default of a specific obligor, commonly denoted name. The buyer of protection promises
periodic payments of a fixed coupon until the end of the contract or default of the name.
The seller of protection agrees to refund the loss on the assets of a name if default occurs,
either by buying its obligations at par (physical settlement) or by cash refund of the loss on
them (cash settlement). As in a standard swap, its value at origin is zero.
Assuming, for the sake of simplicity, that no payment is made in case of default for the
coupon period in which the credit event occurs, the credit default swap coupon for maturity
tN is defined from
LGD
N−1

i=1
D (t, ti)

Q (ti) −Q (ti+1)

= cN
N−1

i=1
D (t, ti) Q (ti+1)
where cN are the credit default swap spreads observed on the market, Q (ti) is the survival
probability of the obligor beyond time ti and the loss given default figure is supposed to be

36
Copula Methods in Finance
non-stochastic. Notice that the term structure of survival probabilities can be recovered by
means of a bootstrap algorithm. The credit default swap rates are sorted from short to long
maturities. Then, for maturity t1 we have
Q (t1) =
LGD
c1 + LGD
and for any other maturity tN, N ⩾2, one can compute
Q (tN) =
cN−1 −cN
D (t, tN) (cN + LGD)
N−1

i=1
D (t, ti) Q (ti) + Q (tN−1)
LGD
cN + LGD
Alternatively, one can assume that the coupon of the period in which the underlying credit
defaults is paid at the end of the period. In this case, the credit default swap is defined as
LGD
N−1

i=1
D (t, ti)

Q (ti) −Q (ti+1)

= cN
N−1

i=1
D (t, ti) Q (ti)
The bootstrap procedure now yields
Q (t1) = 1 −
c1
LGD
and
Q (tN) =
cN−1 −cN
D (t, tN) LGD
N−1

i=1
D (t, ti) Q (ti−1) + Q (tN−1)

1 −cN
LGD

1.7.4
Counterparty risk
Credit risk is not only a feature of standard corporate or defaultable bonds. It is also an
element that should be taken into account in the evaluation of any contractual exposure to
a counterparty. Derivative contracts may generate such credit risk exposures, particularly
in transactions on the OTC market, that, as we have noticed above, represent the main
development of the derivative industry.
The pay-off of a defaultable, or as termed in the literature, vulnerable derivative, is
defined as
G (S, T ) [1 −1DEF (T ) LGD]
Of course the dependence structure between the pay-off and the default event may be
particularly relevant, and will be the object of some of the applications presented in this
book. However, even assuming independence of the two risk factors, some important effects
of counterparty risk on the evaluation of derivative contracts can be noticed.
The first, obvious, point is that accounting for counterparty risk leads to a discount in the
value of the derivative, with respect to its default-free value. Even under independence, the
value of the derivative contract is obtained under the risk-neutral valuation measure as
D (t, T ) EQ [G (S, T )] −D (t, T ) EQ [G (S, T )] EQ [1DEF (T ) LGD]

Derivatives Pricing, Hedging and Risk Management
37
that is, the value of the default-free derivative minus the product of such value times the
default probability and the loss given default figure.
Both the approaches described above to represent credit risk can be exploited to evaluate
the discount to be applied to a derivative contract in order to account for counterparty risk.
So, under a structural model one could have
D (t, T ) EQ [G (S, T )]

1 −
 (−d2)

1 −1
d

 (−d1)

 (−d2)

while an intensity based model would yield
D (t, T ) EQ [G (S, T )]

1 −(1 −exp (−γ (T −t))) LGD

The second point to realize is that even though market and credit risk are orthogonal,
they must be handled jointly in practice. If one overlooks counterparty risk in evaluating a
vulnerable derivative, one obtains the wrong price and the wrong hedging policy, ending
up with an undesired market risk.
The third point to notice is that counterparty risk generally turns linear derivatives into
non-linear ones. To make the point clear, consider the simplest example of a linear vulnerable
derivative, i.e. forward contract. Assume that counterparty A is long in the contract, and
counterparty B is short. The delivery price is the forward price F: we remind the reader that
the forward price is the delivery value that equals to zero the value of a forward contract at
the origin. Assume now that the two counterparties have default probabilities QA (T ) and
QB (T ) and zero recovery rates, and that the time of default is independent of the underlying
asset of the forward contract. Notice that the default risk of counterparty A is relevant only
if the contract ends up in the money for counterparty B, that is, if S (T ) < F, while default
of counterparty B is relevant only if the long counterparty ends up with a gain, that is, if
S (T ) > F. The value of the forward contract is then
EQ

(S (T ) −F) 1{S(T )>F}

QB (T ) + EQ

(S (T ) −F) 1{S(T )<F}

QA (T )
where we remind that QA (T ) and QB (T ) are the survival probabilities beyond time T .
Notice that linearity of the product is broken unless QA (T ) = QB (T ). Even in the latter
case, the delta of the contract would not be equal to 1, but would rather be equal to the
survival probability of the two counterparties.
1.8
COPULA METHODS IN FINANCE: A PRIMER
Up to this point, we have seen that the three main frontier problems in derivative pricing
are the departure from normality, emerging from the smile effect, market incompleteness,
corresponding to hedging error, and credit risk, linked to the bivariate relationship in OTC
transactions. Copula functions may be of great help to address these problems. As we will
see, the main advantage of copula functions is that they enable us to tackle the problem
of specification of marginal univariate distributions separately from the specification of
market comovement and dependence. Technically, we will see in Chapter 3 that the term
“dependence” is not rigorously correct, because, strictly speaking, dependence is a concept
limited to positive comovement of a set of variables. However, we will stick to the term

38
Copula Methods in Finance
“dependence” throughout most of this book because it is largely diffused both among prac-
titioners in the financial markets and academics in statistics and finance. We will instead
insist again and again on the distinction between the concept of dependence, defined in this
broad sense, and the concept of linear correlation, which is used by quantitative analysts
in most of the financial institutions in the world. In fact, we will show that the concept of
dependence embedded in copula functions is much more general than the standard linear
correlation concept, and it is able to capture non-linear relationships among the markets.
1.8.1
Joint probabilities, marginal probabilities and copula functions
To give an intuitive grasp of the use of copula functions in finance, consider a very simple
product, a bivariate digital option. This option pays one unit of currency if two stocks or
indexes are above or below a pair of strike price levels. Options like these are very often
used in structured finance, particularly index-linked products: examples are digital bivariate
notes and, more recently, Altiplano notes.
As an example, assume a product written on the Nikkei 225 and S&P 500 indexes which
pays, at some exercise date T , one unit if both are lower than some given levels KNKY and
KSP. According to the basic pricing principles reviewed in this chapter, the price of this
digital put option in a complete market setting is
DP = exp [−r (T −t)] Q (KNKY, KSP)
where Q (KNKY, KSP) is the joint risk-neutral probability that both the Japanese and US
market indexes are below the corresponding strike prices.
How can we recover a price consistent with market quotes? The first requirement that
may come to mind is to ensure that the price is consistent with the market prices for plain
vanilla options on each of the two indexes. Say, for example, we can recover, using some
of the models or techniques described in this chapter, the risk-neutral probability QNKY that
the Nikkei index at time T will be below the level KNKY. We can do the same with the
S&P 500 index, recovering probability QSP. In financial terms, we are asking what is the
forward price of univariate digital options with strikes KNKY and KSP; in statistical terms,
what we are estimating from market data are the marginal risk-neutral distributions of the
Nikkei and the S&P indexes.
In order to compare the price of our bivariate product with that of the univariate ones, it
would be great if we could write the price as
DP = exp [−r (T −t)] Q (KNKY, KSP) = exp [−r (T −t)] C (QNKY, QSP)
with C (x, y) a bivariate function.
Without getting involved in heavy mathematics, we can also discover the general require-
ments that the function C (x, y) must satisfy in order to be able to represent a joint
probability distribution. Beyond the basic requirement that the output of the function must be
in the unit interval, as it must represent a probability, three requirements immediately come
to mind. The first: if one of the two events has zero probability, the joint probability that both
events occur must also be zero. So, if one of the arguments of C (x, y) is equal to 0 the func-
tion must return 0. On the contrary, if one event will occur for sure, the joint probability that
both the events will take place corresponds to the probability that the second event will be

Derivatives Pricing, Hedging and Risk Management
39
observed. This leads to the second technical requirement that if one of the arguments C (x, y)
is equal to 1 the function must yield the other argument. Finally, it is intuitive to require that
if the probabilities of both the events increase, the joint probability should also increase,
and for sure it cannot be expected to decrease. Technically, this implies a third requirement
for the function C (x, y), that must be increasing in the two arguments (2-increasing is
approximately the correct term: you will learn more on this in Chapter 2). We have just
described the three requirements that enable us to define C (x, y) as a copula function.
If we go back to our pricing problem, that’s where copula functions come in: they enable
us to express a joint probability distribution as a function of the marginal ones. So, the
bivariate product is priced consistently with information stemming from the univariate ones.
Beyond the intuitive discussion provided here, this opportunity rests on a fundamental find-
ing, known as Sklar’s theorem. This result states that any joint probability distribution can
be written in terms of a copula function taking the marginal distributions as arguments and
that, conversely, any copula function taking univariate probability distributions as arguments
yields a joint distribution.
1.8.2
Copula functions duality
Consider now a bivariate digital call option. Differently from the digital put option, it pays
one unit of currency if both the Nikkei 225 and the S&P 500 indexes are above the strike
levels KNKY and KSP. The relevant probability in this case is
DC = exp [−r (T −t)] Q (KNKY, KSP)
Analogously to the approach above, the copula function method enables us to recover a
copula function C(v, z) such that
DC = exp [−r (T −t)] Q (KNKY, KSP)
= exp [−r (T −t)] C[Q (KNKY) , Q (KSP)]
The new copula function C(v, z) is known as survival copula. Readers will learn from
the mathematical treatment in Chapter 2 that the survival copula is related to the copula
function by the relationship
C[Q (KNKY) , Q (KSP)] = 1 −Q (KNKY) −Q (KSP) + C[Q (KNKY) , Q (KSP)]
Readers can also check, as will be discussed in detail in Chapter 8, that the relationship
above corresponds to a requirement to rule out arbitrage opportunities.
1.8.3
Examples of copula functions
Let us start with the simplest example of a copula function. This obviously corresponds
to the simplest hypothesis corresponding to the comovements of the Japanese and the US
markets. Assume, to keep things simple, that the two markets are independent. In this case
we know from basic statistics that the joint probability corresponds to the product of the
marginal probabilities, and we have
DP = exp [−r (T −t)] Q (KNKY, KSP) = exp [−r (T −t)] QNKYQSP

40
Copula Methods in Finance
So, C (x, y) = xy, also known as the product copula, is the first function we are able to
build and use to price our bivariate option.
The next question is what would happen if the two markets were perfectly positively or
negatively correlated. The answer to this question requires us to draw from more advanced
statistics, referring to the so-called Fr´echet bounds. The joint probability is constrained
within the bounds
max (QNKY + QSP −1, 0) ⩽Q (KNKY, KSP) ⩽min (QNKY, QSP)
Moreover, the upper bound corresponds to the case of perfect positive dependence between
the two markets and the lower bound represents perfect negative dependence. We can
therefore check the impact of perfect positive dependence on the value of the bivariate
product by computing
DP = exp [−r (T −t)] Q (KNKY, KSP) = exp [−r (T −t)] min (QNKY, QSP)
So, C (x, y) = min (x, y) is another copula function, known as the maximum copula. The
minimum copula will instead correspond to the case of perfect negative dependence and to
the Fr´echet lower bound C (x, y) = max (x + y −1, 0) yielding
DP = exp [−r (T −t)] Q (KNKY, KSP)
= exp [−r (T −t)] max (QNKY + QSP −1, 0)
We have then recovered copula functions corresponding to the extreme cases of indepen-
dence and perfect dependence. Moving one step forward, we could try to build a copula
function accounting for imperfect dependence between the two markets. The first idea would
be to try a linear combination of the three cases above, obtaining
C (QNKY, QSP) = β max (QNKY + QSP −1, 0) + (1 −α −β) QNKYQSP
+ α min (QNKY, QSP)
with 0 ⩽α, β ⩽1 and α + β = 1. Copula functions obtained in this way define the so-called
Fr´echet family of copula functions.
Other ways of obtaining copula functions are more involved and less intuitive. For
example, consider taking a function ϕ (.) satisfying some technical conditions that will
be discussed in more detail throughout the book. If we define
C (QNKY, QSP) = ϕ[−1] [ϕ (QNKY) + ϕ (QSP)]
we obtain copula functions. Copulas constructed in this way are called Archimedean copulas
and are largely used in actuarial science.
As a final idea, one could try to generalize and make more flexible the standard setting
under which most of the results in finance were obtained under the Black–Scholes theory.
This corresponds to normal distribution of the returns, which in this case is extended to mul-
tivariate normality. From this perspective, a particularly useful result is that the joint standard

Derivatives Pricing, Hedging and Risk Management
41
normal distribution computed in the inverse of the arguments satisfies the requirements of
a copula function. We may then price our bivariate claim using
DP = exp[−r(T −t)]
[
−1(QNKY), 
−1(QSP); ρ]
where 
 (x, y; ρ) is the standard bivariate normal distribution with correlation parameter
ρ. This example is particularly useful to highlight the main advantage from the use of
copula functions. Notice in fact that in this way we may preserve the dependence structure
typical of a multivariate normal distribution by modifying only the marginal distributions,
which may be allowed to display skewness and fat-tails behavior consistently with the data
observed from the market.
1.8.4
Copula functions and market comovements
As we have already seen from the examples, copula functions provide a way to represent the
dependence structure between markets and risk factors, while preserving the specification of
the marginal distribution of each and every one of them. Representing market comovements
in a world in which the marginal distribution of returns is not normal raises problems that
may be new for many scholars and practitioners in finance.
The main result is that linear correlation, which represents the standard tool used in the
dealing rooms and risk management units to measure the comovement of markets may turn
out to be a flawed instrument in the presence of a non-normal return. Linear correlation
between the rate of returns rNKY and rSP in our two markets may be written as
corr (rNKY, rSP) = cov (rNKY, rSP)
σNKYσSP
=
1
σNKYσSP
 ∞
−∞
 ∞
−∞
[Q (x, y) −QNKYQSP] dx dy
where σNKY and σSP represent volatilities. Notice that the correlation depends on the
marginal distributions of the returns. The maximum value it can achieve can be computed
by substituting the upper Fr´echet bound in the formula
corrmax (rNKY, rSP)
=
1
σNKYσSP
 ∞
−∞
 ∞
−∞
[min (QNKY, QSP) −QNKYQSP] dx dy
and the value corresponding to perfect negative correlation is obtained by substituting the
lower bound
corrmin (rNKY, rSP)
=
1
σNKYσSP
 ∞
−∞
 ∞
−∞
[max (QNKY + QSP −1, 0) −QNKYQSP] dx dy
Of course everyone would expect these formulas to yield corrmax = 1 and corrmin = −1.
The news is that this is not true in general. Of course, that is what we are used to expect in

42
Copula Methods in Finance
a world of normal returns. The result would also hold in the more general case of elliptic
distributions, but not for other arbitrary choices. Looking at the problem from a different
viewpoint, correlation is an effective way to represent comovements between variables if
they are linked by linear relationships, but it may be severely flawed in the presence of non-
linear links. Readers may check this in the simple case of a variable z normally distributed
and z2 which is obviously perfectly correlated with the first one, but has a chi-squared
distribution.
So, using linear correlation to measure the comovements of markets in the presence of
non-linear relationships may be misleading because it may not cover the whole range from
−1 to +1 even though two markets are moved by the same factor, and so are perfectly
dependent.
The alternative offered by statistics to this shortcoming is the use of non-parametric
dependence measures, such as Spearman’s ρS and Kendall’s τ. The non-parametric feature
of these measures means that they do not depend on the marginal probability distributions.
It does not come as a surprise, then, that these measures are directly linked to the copula
function. In particular, it may be proved that the following relationships hold
ρS = 12
 1
0
 1
0
C (u, v) dudv −3
τ = 4
 1
0
 1
0
C (u, v) dC (u, v) −1
Notice that the specific shape of the marginal probability distributions does not enter these
relationships. Furthermore, it may be proved that substituting the maximum and minimum
copulas in these equations gives values of 1 and −1 respectively. Differently from the linear
correlation measure, then, if the two variables (markets in our case) are perfectly dependent
we expect to observe figures equal to 1 for Spearman’s ρS and Kendall’s τ, while a score
−1 corresponds to perfect negative dependence.
The relationship between non-parametric dependence measures and copula functions can
also be applied to recover a first calibration technique of the copula function itself. In
some cases the relationship between these non-parametric statistics and the parameters of
the copula function may also be particularly easy. One of the easiest, that we report as
an example, is the relationship between the copula functions of the Fr´echet family and
Spearman’s ρS. We have in fact
ρS = α −β
where the parameters α, β are reported in the definition of the Fr´echet family given above.
1.8.5
Tail dependence
The departure from normality in a multivariate system and the need to represent the comove-
ment of markets as closely as possible raises a second dimension of the problem. We know
that non-normality at the univariate level is associated with skewness and leptokurtosis
phenomena, and what is known as the fat-tail problem. In a multivariate setting, the fat-
tail problem can be referred both to the marginal univariate distributions or to the joint

Derivatives Pricing, Hedging and Risk Management
43
probability of large market movements. This concept is called tail dependence. Intuitively,
we may conceive markets in which the marginal distributions are endowed with fat tails,
but extreme market movements are orthogonal, or cases in which the returns on each market
are normally distributed, but large market movements are likely to occur together. The use
of copula functions enables us to model these two features, fat tails and tail dependence,
separately.
To represent tail dependence we consider the likelihood that one event with probability
lower than v occurs in the first variable, given that an event with probability lower than
v occurs in the second one. Concretely, we ask which is the probability to observe, for
example, a crash with probability lower than v = 1% in the Nikkei 225 index, given that a
crash with probability lower than 1% has occurred in the S&P 500 index. We have
λ (v) ≡Pr(QNKY ⩽v | QSP ⩽v)
= Pr(QNKY ⩽v, QSP ⩽v)
Pr(QSP ⩽v)
= C (v, v)
v
If we compute this dependence measure far in the lower tail, that is, for very small values
of v, we obtain the so-called tail index, in particular the lower tail index
λL ≡lim
v→0+
C (v, v)
v
It may be easily verified that the tail index is zero for the product copula and 1 for the
maximum copula. Along the same lines, one can also recover the tail dependence for the
upper tail index. Analogously, using the duality among copulas described above, we have
λU = lim
v→1−λv ≡lim
v→1−
Pr(QNKY > v, QSP > v)
Pr(QSP > v)
= lim
v→1−
1 −2v + C (v, v)
1 −v
and this represents the probability that price booms may occur at the same time in the US
and Japanese markets.
1.8.6
Equity-linked products
Here we give a brief preview of applications to equity-linked products, beyond the simple
multivariate digital options seen above. Consider a simple case of a rainbow option, such
as, for example, a call option on the minimum between two assets. These derivatives are
largely used in structured finance. An example is a class of products, known as Everest
notes, whose coupon at the given time T is determined by computing, for example,
coupon (T ) = max

min
	SNKY (T )
SNKY (0) , SSP (T )
SSP (0)

−1, 0


44
Copula Methods in Finance
where SNKY and SSP are the values of the Nikkei 225 and the S&P 500 indexes and time
0 is the initial date of the contract. At any time 0 < t < T , the value of the coupon will
be computed as a call option with strike on the minimum between two assets whose initial
value was 1. The strike price is set equal to 1. We will see in Chapter 8 that the price
of options like these can be computed using copula functions. Here we just convey the
intuition by working the argument backward. Assume that you have a price function for the
rainbow option above
CALL [sNKY (t) , sSP (t) ; K, T ]
= exp [−r (T −t)] EQ [max (min (sNKY (T ) , sSP (T )) −K, 0) | ℑt]
where we have simplified the notation defining sNKY (t) and sSP (t), the values of the indexes
rescaled with respect to their levels at time 0. Of course in our case we also have K = 1.
Applying what we know about implied risk-neutral probability we have
Pr (min (sNKY (T ) , sSP (T )) > 1 | ℑt) = Pr (sNKY (T ) > 1, sSP (T ) > 1 | ℑt)
= Q (1, 1 | ℑt)
= −exp [r (T −t)] ∂CALL
∂K
Using copula functions we obtain
Q (1, 1 | ℑt) = C

QNKY (1) , QSP (1) | ℑt

= −exp [r (T −t)] ∂CALL
∂K
By integrating from the strike K = 1 to infinity we have
CALL (sNKY (t) , sSP (t) ; K, T ) =
 ∞
1
C

QNKY (η) , QSP (η) | ℑt

dη
and the call option is written in terms of copula functions. Much more about applications
and cases like these and techniques by which closed form solutions may also be recovered
is reported in Chapter 8.
1.8.7
Credit-linked products
The vast majority of copula function applications have been devoted to credit risk and
products whose pay-off depends on the performance of a basket of obligations from several
obligors (names). In order to illustrate the main choices involved, we describe the application
to a standard problem, that is the pricing of a first-to-default swap. This product is a credit
derivative, just like the credit default swap described above, with the difference that the
counterparty offering protection pays a sum, for example a fixed amount, at the first event
of default out of a basket of credit exposures.
To see how the pricing problem of a first-to-default derivative leads to the use of copula
functions consider a product that pays one unit of currency if at least one out of two
credit exposures defaults by time T . It is clear that the risk-neutral probability of paying

Derivatives Pricing, Hedging and Risk Management
45
the protection is equal to that of the complement to the event that a credit exposure goes
bankrupt – that is, the case that both names will survive beyond time T . Formally,
FTD = exp [−r (T −t)] [1 −Pr (τ1 > T, τ2 > T | ℑt)]
where FTD denotes first-to-default, τi, i = 1, 2 denote the default times of the two names.
It is then immediate to write the price in terms of copula functions
FTD = exp [−r (T −t)]

1 −C

Q1 (T ) , Q2 (T ) | ℑt

Using the duality relationship between a copula function and its survival copula we obtain
FTD = exp [−r (T −t)] [Q1 (T ) + Q2 (T ) −C (Q1 (T ) , Q2 (T ) | ℑt)]
and the value of the product is negatively affected by the dependence between the defaults
of the two names. This diversification effect may be appraised computing the case of perfect
positive dependence
FTDmax = exp [−r (T −t)] [Q1 (T ) + Q2 (T ) −min (Q1 (T ) , Q2 (T ) | ℑt)]
= exp [−r (T −t)] [max (Q1 (T ) , Q2 (T ) | ℑt)]
and that corresponding to independence
FTD⊥= exp [−r (T −t)] [Q1 (T ) + Q2 (T ) −Q1 (T ) Q2 (T ) | ℑt]
= exp [−r (T −t)]

Q1 (T ) + Q1 (T ) Q2 (T ) , | ℑt

So, as the value of the copula function increases with dependence, the value of the
first-to-default product decreases.
Of course one could consider reconducting the analysis to the multivariate normal dis-
tribution, by using structural models to specify the marginal distributions and the Gaussian
copula to represent dependence
C (Q1 (T ) , Q2 (T ) | ℑt) = 
[
−1 (Q1 (T )) , 
−1 (Q2 (T )) ; ρ]
where 
−1 (Qi (T )), i = 1, 2 denote the inverse of marginal default probabilities consistent
with both the leverage figures of the names and volatilities of their assets, while ρ is the
correlation between the assets. In this approach, which is used for example in CreditMetrics,
the correlation figure is recovered either from equity correlation or by resorting to the
analysis of industrial sector comovements.
Example 1.4
Consider a first-to-default option written on a basket of two names, rated AA
and BBB. Under the contract, the counterparty selling protection will pay 1 million euros
if one of the names defaults over a 5-year period. We saw in a previous example that the
leverage figures of AA and BBB industrial companies were equal to 26.4% and 41%. Under
the risk-neutral probability measure, assuming the risk-free rate flat at 4% and a volatility
of the asset side equal to 25% for both the firms, we obtained 0.69% and 4.71% default


## Bivariate Copula Functions

46
Copula Methods in Finance
probabilities respectively. The maximum value of the first-to-default can be immediately
computed as
FTDmax = 1 000 000 exp [−0.04(5)] [0.0471] = 38 562
If one assumes independence between the two credit risks, we obtain instead
FTD⊥= 1 000 000 exp [−0.04(5)] [0.0069 + 0.9931(0.0471)] = 43 945
Finally, assuming a Gaussian copula with an asset correlation equal to 20%, the value
“in fashion” in the market at the time we are writing, we obtain a joint default probability
of 0.088636%. The price of the first-to-default swap is then
FTD = 1 000 000 exp [−0.04(5)] [0.0471 + 0.0069 −0.00088636] = 43 486
Besides this case, it is easy to see why copula functions may be particularly useful in
this case. If, for example, we choose to model the distribution of the time to default as
in reduced form models, rather than the structure of the firm as in structural models, it is
clear that the assumption of normality can no longer be preserved. In this case the marginal
distributions are obviously non-Gaussian since they are referred to default times and are
naturally defined on a non-negative support. Nevertheless, we may conceive applications
that may involve features from both structural and reduced form models. For example, the
joint default probability may be specified by using a reduced form model for the marginals
and the structural model for the dependence structure. We may write
C(Q1(T ), Q2(T ) | ℑt) = 
[
−1(1 −exp(−γ1(T −t))), 
−1(1 −exp(−γ2(T −t))); ρ]
where γi, i = 1, 2 denote the default intensities of the two names and now, differently
from the fully structural model quoted above, ρ is correlation between the default times.
Notice that in this way we may mix information stemming from different sources, such as
equity market for the specification of the dependence structure, and corporate bond or credit
default bond markets for the marginal distributions. We now give a simple example of this
flexibility, but, again, this has to be taken only as an appetizer to invite readers to get into
the details of the matter, which will be covered in the rest of the book.
Example 1.5
Consider a 5-year first-to-default option written on a basket of two names,
namely Deutsche Telecom and Dresdner Bank. The nominal value is 1 million euros. The
information we have is that the default probability of DT, bootstrapped from a credit default
swap, is 12.32%. As for Dresdner, we know that the asset swap spread for a 5-year bond
is 75 bp. This allows us to compute a default probability of [1 −exp(−0.0075(5))] =
3.6806%. We assume that the correlation between the default times is 50% and that the
copula is Gaussian. So, we first compute 
−1 (12.32%) = −1.15926. Analogously, we have
for Dresdner 
−1 (3.6806%) = −1.788967169. The joint default probability is computed
from
C (Q1 (T ) , Q2 (T ) | ℑt) = 
(
−1 (3.6806%) , 
−1 (12.32%) ; 50%)
= 
 (−1.788967169, −1.15926; 50%) = 1.729%

Derivatives Pricing, Hedging and Risk Management
47
The price of the first-to-default is then
FTD = 1 000 000 exp [−0.04(5)] [0.03606 + 0.1232 −0.01729] = 116 240
Notice that the value obtained is very close to the case of perfect default dependence,
which would obviously cost 123 200, and the basket of names of the first-to-default in this
example is definitely undiversified.


2
Bivariate Copula Functions
This chapter introduces the notion of a copula function and its probabilistic interpretation,
which allows us to consider it a “dependence function” (Deheuvels, 1978). It also examines
the survival copula and density notions, together with the canonical representation and,
lastly, the use of copulas in setting probability bounds for sums of random variables. It
collects a number of financial applications, which will be further developed in the following
chapters. The examples are mainly intended to make the reader aware of the usefulness of
copulas in extending financial modeling beyond the Black–Scholes world. All the proofs
are in the Appendix (see page 87).
We take for granted that the reader is familiar with the notions of the (right continuous)
joint distribution function (or joint cumulative distribution function or joint c.d.f.)
F(x, y) of a couple of random variables (r.v.s) X and Y, as well as with their marginal
distribution functions (or d.f.s or margins) Fi(t), i = 1, 2. We define the generalized
inverse of a distribution function as1
F −1
i
(t) = inf {u : Fi(u) ⩾t, 0 < t < 1}
2.1
DEFINITION AND PROPERTIES
The section is organized as follows: first we present subcopulas, provide an example and list
a number of subcopula properties. Then we define copulas, as introduced by Sklar2 (1959)
and link them to distributions of uniform random variates.
To start with, we need the notions of groundedness and the 2-increasing property, which
allow copulas to respect the distribution function properties.
Definition 2.1
Let us consider two non-empty subsets A1 and A2 of ℜ∗and a function
G : A1 × A2 →ℜ. Denote with ai the least element of Ai, i = 1, 2. The function G is
named grounded if, for every (v, z) of A1 × A2,
G(a1, z) = 0 = G(v, a2)
1 Evidently, this notion reduces to the usual inverse function one if Fi is increasing.
2 Copulas were introduced by Sklar (1959): important developments in the theory are due to Schweizer and Sklar
(1974, 1983), who studied them in the context of probabilistic metric spaces, and to Schweizer and Wolff (1981).
Independent, early work is due also to Hoeffding (1940), Kimeldorf and Sampson (1975), Deheuvels (1978, 1979).
Related problems, such as the characterization of the Fr´echet class or the definition of measures of dependence,
date back to the 1950s (see, respectively, Fr´echet (1951) and R´enyi (1959)): they were later related with and
merged in the theory of copulas, as we will illustrate in the text. For “a historical overview and rather personal
account” see Schweizer (1991).

50
Copula Methods in Finance
Definition 2.2
G : A1 × A2 →ℜis called 2-increasing if for every rectangle [v1, v2] ×
[z1, z2] whose vertices lie in A1 × A2, such that v1 ⩽v2, z1 ⩽z2
G(v2, z2) −G(v2, z1) −G(v1, z2) + G(v1, z1) ⩾0
(2.1)
The l.h.s. of (2.1) measures the mass or area, according to the function G, of the rectangle
[v1, v2] × [z1, z2]. Then, 2-increasing functions assign non-negative mass to every rectangle
in their domain.
The above definitions allow us to define subcopulas.
Definition 2.3
A two-dimensional subcopula C is a real function defined on A × B, where
A and B are non-empty subsets of I = [0, 1], containing both 0 and 1:
C : A × B →ℜ
(i) grounded (C(v, 0) = C(0, z) = 0)
(ii) such that
C(v, 1) = v,
C(1, z) = z
for every (v, z) of A × B
(iii) 2-increasing
Example 2.1
Set A = B = I and consider the function C(v, z) = max(v + z −1, 0).
Since max(z −1, 0) = max(v −1, 0) = 0, C is grounded. Property (ii) is satisfied, since
max(z, 0) = z, max(v, 0) = v. C is also 2-increasing, since z1 ⩽z2 implies
max(v2 + z1 −1, 0) −max(v1 + z1 −1, 0)
⩽max(v2 + z2 −1, 0) −max(v1 + z2 −1, 0)
(2.2)
Rearranging we get (2.1). The function max(v + z −1, 0) on I 2 is therefore a subcopula.
Remark 2.1
The above function is still a subcopula if, instead of setting A = B = I, one
sets A = B = {0} ∪

1
2, 1

.
As a general rule, the 2-increasing property neither implies nor is implied by the non-
decreasing property in each argument3: however, 2-increasing functions which are also
grounded, such as subcopulas, are non-decreasing in each place.
Theorem 2.1
A function G(v, z) : A1 × A2 →ℜgrounded and 2-increasing is non-de-
creasing in both v and z.
It follows from properties (i), (ii) of the subcopula definition, together with Theorem 2.1,
that:
3 Examples of 2-increasing functions which are not non-decreasing in each argument (and vice versa) are given
for instance by Schweizer and Sklar (1983, section 6.1).

Bivariate Copula Functions
51
Corollary 2.1
For every (v, z) of A × B
0 ⩽C(v, z) ⩽1
Another property of subcopulas is (uniform) continuity, which in turn will prove to be
useful for the so-called section (and differentiability) properties.
Theorem 2.2
C is uniformly continuous on A × B.
Indeed, as a consequence of Theorems 2.1 and 2.2 we get
Corollary 2.2
For a given subcopula, the functions W and V defined – for k ∈B, K ∈
A – as follows:
Wk(x) = C(x, k)
VK(x) = C(K, x)
are non-decreasing and uniformly continuous.
These functions are called, respectively, the horizontal and vertical sections of the subcop-
ula C. The section properties entail the following.
Theorem 2.3
In the interior of A × B, both partial derivatives of the C function, ∂C/∂v,
∂C/∂z, exist almost everywhere and take values in I.
Example 2.2
The partial derivatives of the subcopula in Example 2.1 exist whenever
v + z −1 ̸= 0, i.e. z ̸= 1 −v. Since max(v + z −1, 0) = v + z −1 whenever z > 1 −v,
they are
∂C
∂v = ∂C
∂z =

0
z < 1 −v
1
z > 1 −v
Having given the definition of the two-dimensional subcopula and its main properties, we
are now in a position to define two-dimensional copulas.4
Definition 2.4 (Sklar, 1959)
A two-dimensional copula C is a two-dimensional subcopula
with A = B = I.
The subcopula of Example 2.1 is actually a copula.
First of all, let us notice that, from the definition, copulas are joint distribution functions
of standard uniform random variates:
C(v, z) = Pr(U1 ⩽v, U2 ⩽z)
4 In the rest of the chapter we will omit the term “two-dimensional” while referring to subcopulas and copulas,
since the definition of n-dimensional subcopulas and copulas is deferred until Chapter 4.

52
Copula Methods in Finance
The following probabilities of uniform variates can then be written via copulas:
Pr(U1 ⩽v, U2 > z) = v −C(v, z)
Pr(U1 > v, U2 ⩽z) = z −C(v, z)
Pr(U1 ⩽v | U2 ⩽z) = C(v, z)/z
Pr(U1 ⩽v | U2 > z) = v −C(v, z)
1 −z
C1|2(v, z) ≡Pr(U1 ⩽v | U2 = z) =
lim
z→0+
C(v, z + z) −C(v, z)
z
= ∂C(v, z)
∂z
C2|1(v, z) ≡Pr(U2 ⩽z | U1 = v) = ∂C(v, z)
∂v
Second, we know from elementary probability theory that the probability-integral trans-
forms of the r.v.s X and Y, X →F1 (X), Y →F2 (Y), are distributed as standard uniform
Ui, i = 1, 2:
F1(X) ∼U1,
F2(Y) ∼U2
Analogously, the transforms according to F −1
i
of standard uniforms are distributed according
to Fi:
F −1
i
(Ui) ∼Fi
Since copulas are joint distribution functions of standard uniforms, a copula computed at
F1(x), F2(y) gives a joint distribution function at (x, y):
C(F1(x), F2(y)) = Pr (U1 ⩽F1(x), U2 ⩽F2(y))
= Pr

F −1
1
(U1) ⩽x, F −1
2
(U2) ⩽y

= Pr (X ⩽x, Y ⩽y)
= F(x, y)
(2.3)
This anticipates part of the link between distribution functions and copulas, which will be
the content of Sklar’s theorem. Before studying the latter, let us introduce the bounds for
copulas, analogous to the Fr´echet bounds for distribution functions.
2.2
FR ´ECHET BOUNDS AND CONCORDANCE ORDER
It is straightforward to demonstrate that subcopulas are bounded:
Theorem 2.4
Subcopulas satisfy the following inequality:
max(v + z −1, 0) ⩽C(v, z) ⩽min(v, z)
(2.4)
for every point (v, z) ∈A × B.

Bivariate Copula Functions
53
1
0.75
0.5
0.25
0.0
0
0.33
0.33
0.67
0.67
1
1
1
0.75
0.5
0.25
0.0
00.330.67 1
Figure 2.1
Minimum (left) and maximum (right) copulas
When (v, z) ∈I 2, so that C becomes a copula, the bounds in (2.4) are copulas too: in the
remainder of the section we will consider this case. The lower bound is denoted by C−, and
called the minimum copula; the upper bound is denoted by C+, and called the maximum
copula. They are represented in Figure 2.1.
From Theorem 2.4 and continuity it follows that the graph of each copula is “a continuous
surface over the unit square that contains the skew quadrilateral whose vertices are (0, 0, 0),
(1, 0, 0), (1, 1, 1) and (0, 1, 0). This surface is bounded below by the two triangles that
together make up the surface of C−and above by the two triangles that make up the surface
of C+” (Schweizer, 1991), as in Figure 2.2.
Theorem 2.4 has consequences on the so-called level curves of the copula C(v, z), i.e.
the set of points of I 2 such that C(v, z) = K, with K constant:

(v, z) ∈I 2 : C(v, z) = K

The level curves of the minimum and maximum copulas are
{(v, z) : max(v + z −1, 0) = K},
K ∈I
{(v, z) : min(v, z) = K},
K ∈I
(2.5)
They are represented in the plane (v, z) respectively by segments parallel to the line z = −v,
and kinked lines (see Figure 2.3).
It follows from the previous theorem that, for fixed K, the level curve of each C
stays in the triangle formed by the level sets (2.5). As K increases, the triangle is shifted
upwards.
We will see below that level curves play an important role in financial applications of
copulas, both for the simple evaluation of relationships between financial asset returns and
for value-at-risk trade-off assessment.
The existence of the lower and upper bounds also suggests the following definition of
concordance order:

54
Copula Methods in Finance
0.8
0.6
0.4
0.2
0
0
0.2
0.4
0.6
0.8
0
0.2
0.4
0.6
0.8
Figure 2.2
The pyramid is the region in which the copula graph is always included
Figure 2.3
Level curves of the minimum (left) and maximum (right) copulas
Definition 2.5
The copula C1 is smaller than the copula C2 −written as C1 ≺C2 −iff
C1(v, z) ⩽C2(v, z)
for every (v, z) ∈I 2.

Bivariate Copula Functions
55
1
0.75
0.25
0.5
0.00
1
0.33
0.33
0.67
0.67
Figure 2.4
The product copula and its level curves
The order so defined is only partial, since not all copulas can be compared. In order to present
some examples of concordance order, let us also define the product copula, represented in
Figure 2.4, as
C⊥(v, z) = vz
Example 2.3
One can easily verify that any convex linear combination of C−and C+ is
a copula. Consider, for instance, the case
C = 1
3C−+ 2
3C+
It is possible to find points in I 2 where C ⩾C⊥, as well as points where C < C⊥, so that
the two are not comparable. In particular
1
3 max(v + z −1, 0) + 2
3 min(vz) > vz
when v = z = 1
2, while the opposite inequality holds for v = 1
4, z = 3
4.
We will encounter one-parameter families of copulas – to be defined exactly below – which
are totally ordered. The order will depend on the value of the parameter: in particular, a
family will be positively (negatively) ordered iff, denoting with Cα and Cβ the copulas with
parameter values α and β respectively, Cα(v, z) ≺Cβ(v, z) whenever α ⩽β (α ⩾β). For
positively (negatively) ordered families, the level curves of Cα stay above those of Cβ.
Example 2.4
One can easily demonstrate – using the definition – that, for every p ∈I
C(v, z) = pC−+ (1 −p)C⊥
is a copula. Since C−≺C⊥, for p1 ⩾p2 we have
(p1 −p2) C−−(p1 −p2)C⊥⩽0

56
Copula Methods in Finance
Rearranging:
p1C−+ (1 −p1)C⊥⩽p2C−+ (1 −p2)C⊥
which shows that the copula family under examination is negatively ordered with respect
to the constant p.
2.3
SKLAR’S THEOREM AND THE PROBABILISTIC
INTERPRETATION OF COPULAS
The point of departure for financial applications of copulas is their probabilistic interpreta-
tion, i.e. the relationship between copulas and distribution functions of r.v.s. This relationship
is essentially contained in Sklar’s theorem, which says that not only are copulas joint dis-
tribution functions, as argued in (2.3), but the converse also holds true: joint distribution
functions can be rewritten in terms of the marginals and a (unique) subcopula, which in
turn can be extended (not uniquely, in general) to a copula. Therefore, “much of the study
of joint distribution functions can be reduced to the study of copulas” (Schweizer, 1991).
The presentation is organized as follows: in section 2.3.1 we state Sklar’s theorem. In
section 2.3.2 we present a corollary of Sklar’s theorem, which permits us to reconstruct
the subcopula mentioned in the theorem. In section 2.3.3 we comment on the modeling
flexibility given by the theorem. Section 2.3.4 provides some financial applications.
2.3.1
Sklar’s theorem
Consider a probability space (, ℑ, P ), with  a non-empty set, ℑa sigma algebra on
 and P a probability measure on ℑ. Let X and Y be two (Borel-measurable) r.v.s on
(, ℑ, P ) with values in ℜ∗, the extended real line. Let also F, F1 and F2 be their joint
and marginal distribution functions. As usual, the r.v.s are said to be continuous when their
d.f.s are.
Theorem 2.5 (Sklar, 1959)
Let F1(x), F2(y) be (given) marginal distribution functions.
Then, for every (x, y) ∈ℜ∗2:
(i) if C is any subcopula whose domain contains Ran F1 × Ran F2,
C(F1(x), F2(y))
is a joint distribution function with margins F1(x), F2(y);
(ii) conversely, if F(x, y) is a joint distribution function with margins F1(x), F2(y), there
exists a unique subcopula C, with domain Ran F1 × Ran F2, such that
F(x, y) = C(F1(x), F2(y))
(2.6)
If F1(x), F2(y) are continuous, the subcopula is a copula; if not, there exists a copula
C such that
C(v, z) = C(v, z)
for every (v, z) ∈Ran F1 × Ran F2.

Bivariate Copula Functions
57
Example 2.5
Consider the copula in Example 2.1, defined on Ran F1 × Ran F2. The
function
C(F1(x), F2(y)) = max(F1(x) + F2(y) −1, 0)
is a joint distribution function if F1 and F2 are marginal, since:
(i) it is defined for every (x, y) ∈ℜ∗2
(ii) it is 2-increasing:
max(F1(x2) + F2(y2) −1, 0) −max(F1(x2) + F2(y1) −1, 0)
−max(F1(x1) + F2(y2) −1, 0) + max(F1(x1) + F2(y1) −1, 0) ⩾0
(iii) it is grounded:
max(F1(−∞) + F2(y) −1, 0) = 0
max(F1(x) + F2(−∞) −1, 0) = 0
(iv) it gives:
C(F1(+∞), F2(+∞)) = max(1, 1) = 1
(v) it is right continuous, since F1 and F2 are. Its margins are
C(F1(x), F2(+∞)) = max(F1(x), 0) = F1(x)
C(F1(+∞), F2(y)) = max(F2(y), 0) = F2(y)
This verifies part (i) of the theorem. As for part (ii), consider for instance two standard
uniform r.v.s:
F1(x) =



0
x < 0
x
0 ⩽x ⩽1
1
x > 1
and analogously for y. Suppose that their joint distribution function for inf(x, y) > 0 is
F(x, y) = max(inf(x, 1) + inf(y, 1) −1, 0)
(2.7)
and 0 otherwise. Since F1 and F2 are continuous, there exists a unique copula C such
that
F(x, y) = C(F1(x), F2(y))
This is exactly the copula of Example 2.1.
If F1(x), F2(y) are not continuous, uniqueness of the copula C, which extends the sub-
copula C, is not guaranteed. If, for instance, Ran F1 × Ran F2 is a singleton, every copula
that has the same value as C at that point satisfies the theorem. We can also provide the
following example.

58
Copula Methods in Finance
Example 2.6
Let us consider the following distributions:
F(x, y) =
 0
x or y < 0
1
2(inf(x, 1) + inf(y, 1))
0 ⩽x, y ⩽1
F1(x) =



0
x < 0
1
2(x + 1)
0 ⩽x ⩽1
1
x > 1
F2(y) =



0
y < 0
1
2(y + 1)
0 ⩽y ⩽1
1
y > 1
For them, the subcopula of Remark 2.1 satisfies the second part of Sklar’s theorem on
A = B = {0} ∪

1
2, 1

, as one can easily verify from the fact that for 1
2 ⩽x, y ⩽1,
F(x, y) = 1
2(x + y) = max( 1
2(x + 1) + 1
2(y + 1) −1, 0) = C(F1(x), F2(y))
This subcopula can be extended to I 2 either using the copula of Example 2.1, or the fol-
lowing one, suggested by Deheuvels (1978):
C(v, z) =



2v(z −1
2)
0 ⩽v ⩽1
2, 1
2 ⩽z ⩽1
2z(v −1
2)
1
2 ⩽v ⩽1, 0 ⩽z ⩽1
2
0
v ⩽1
2, z ⩽1
2
Non-uniqueness arises from the fact that Y and X are not continuous and Ran F1(x) =
Ran F2(y) = {0} ∪

1
2; 1

.
According to Sklar’s theorem, while writing
F(x, y) = C(F1(x), F2(y))
one splits the joint probability into the marginals and a copula, so that the latter only
represents the “association” between X and Y. Copulas separate marginal behavior, as
represented by the Fi, from the association: at the opposite, the two cannot be disentangled
in the usual representation of joint probabilities via distribution functions. For this reason,
copulas are called also dependence functions (Deheuvels, 1978). We refer to the possibility
of writing the joint cumulative probability in terms of the marginal ones as the probabilistic
interpretation of copulas.
Remark 2.2
Evidently, Sklar’s theorem entails:
Pr(X ⩽x, Y > y) = F1 (x) −C(F1 (x) , F2 (y))
Pr(X > x, Y ⩽y) = F2 (y) −C(F1 (x) , F2 (y))

Bivariate Copula Functions
59
Pr(X ⩽x | Y ⩽y) = C(F1 (x) , F2 (y))/F2 (y)
Pr(X ⩽x | Y > y) = F1 (x) −C(F1 (x) , F2 (y))/(1 −F2 (y))
Pr(X ⩽x | Y = y) = C1|2(F1 (x) , F2 (y)) = ∂C(v, z)
∂z
v = F1(x), z = F2(y)
As a consequence of Sklar’s theorem, the minimum and maximum copulas C−, C+
are named respectively the Fr´echet lower and upper bounds: using Sklar’s result, the
inequality C−⩽C ⩽C+ can be rewritten as
max(F1(x) + F2(y) −1, 0) ⩽F(x, y) ⩽min(F1(x), F2(y))
(2.8)
which is the well-known Fr´echet–Hoeffding inequality for distribution functions.
2.3.2
The subcopula in Sklar’s theorem
It follows as a corollary of Sklar’s theorem that the subcopula that allows the representation
(2.6) can be reconstructed from the margins and the joint distribution by inversion. Using
the generalized inverse concept, we can state that
Corollary 2.3
Under the hypotheses of part (ii) of Sklar’s theorem the (unique) subcopula
C: Ran F1 × Ran F2 →I such that
F(x, y) = C(F1(x), F2(y))
for every (x, y) in ℜ∗2 is
C(v, z) = F

F −1
1 (v), F −1
2 (z)

Evidently, if Ran F1 = Ran F2 = I, the previous subcopula is a copula.
Example 2.7
Suppose, in part (ii) of Sklar’s theorem, that X and Y are exponential random
variables
F1(x) = 1 −exp(−λ1x)
F2(y) = 1 −exp(−λ2y)
for x > 0, y > 0, λ1, λ2 > 0. Suppose also that their joint distribution is
F(x, y) = max(1 −exp(−λ1x) −exp(−λ2y), 0)
(2.9)
Then, since
F −1
1 (v) = −ln(1 −v)/λ1
(2.10)
and an analogous expression holds for z, the copula C such that
C (F1(x), F2(y)) = C (1 −exp(−λ1x), 1 −exp(−λ2y))
= max(1 −exp(−λ1x) −exp(−λ2y), 0)

60
Copula Methods in Finance
is
F

F −1
1 (v), F −1
2 (z)

= F (−ln(1 −v)/λ1, −ln(1 −z)/λ2)
= max (1 −exp(ln(1 −v)) −exp (ln (1 −z)) , 0)
= max(v + z −1, 0)
i.e. the copula of Example 2.1.
Corollary 2.3 states that the construction via Sklar’s theorem exhausts the so-called
Fr´echet class, i.e. the class of joint distribution functions which have F1 and F2 as margins
(Fr´echet, 1935, 1951; Hoeffding, 1940).
2.3.3
Modeling consequences
The separation between marginal distributions and dependence explains the modeling flexi-
bility given by copulas, which has a number of theoretical and practical applications. Before
explaining them, let us introduce the following remark.
Remark 2.3
In Examples 2.5 and 2.7 above, the association between the r.v.s X and Y
was encapsulated in the copula C(v, z) = max(v + z −1, 0). As argued in Chapter 1 and
in section 2.4.2 below, this copula represents perfect negative dependence. The marginal
behavior was uniform in Example 2.5, exponential in Example 2.7: as a consequence, in the
two examples the same copula gave different joint distributions, (2.7) and (2.9) respectively.
The first part of Sklar’s theorem allows us to construct bivariate distributions in a straight-
forward, flexible way: simply “plug” a couple of univariate margins into a function which
satisfies the subcopula definition. This contrasts with the “traditional” way to construct mul-
tivariate distributions, which suffers from the restriction that the margins are usually of the
same type, i.e. the corresponding random variables are a linear affine transform of each
other. With the copula construction we are allowed to start from marginals of different
types.
Example 2.8
Using the product copula and the marginal of X of Example 2.5, i.e. expo-
nential, assume Y to be a (central) Student r.v., with υ degrees of freedom (d.o.f.). Formally,
this means that:
F2(y) = tυ(y) =

 y
−∞
((υ + 1)/2)
√πυ (υ/2)

1 + s2
υ
−υ+1
2
ds
where  is the usual Euler function. Then the joint distribution function, according to Sklar’s
theorem, is:
F(x, y) = [1 −exp(λ1x)]

 y
−∞
((υ + 1)/2)
√πυ (υ/2)

1 + s2
υ
−υ+1
2
ds

Bivariate Copula Functions
61
Consider now, with the same marginals, the following function, which, as the readers can
check, satisfies the copula definition5:
˚C(v, z) =
 vz1−r,
v ⩽z
v1−rz,
v > z
Then Sklar’s theorem allows us to state that also ˚C(F1(x), F2(y)) is a distribution function:
˚F(x, y) =




1 −exp(λ1x)
  y
−∞
((υ+1)/2)
√πυ(υ/2)

1 + s2
υ
−υ+1
2 ds
1−r
,
(x, y) ∈A

1 −exp(λ1x)
1−r  y
−∞
((υ+1)/2)
√πυ(υ/2)

1 + s2
υ
−υ+1
2 ds,
(x, y) /∈A
where the region A is defined by
x ⩽−1
λ1
ln

1 −

 y
−∞
((υ + 1)/2)
√πυ (υ/2)

1 + s2
υ
−υ+1
2
ds


We have been able, through copulas, to construct joint distributions for X and Y, even
if they had marginals of different types. These distribution functions encapsulate different
assumptions on the dependence between X and Y: in particular, the former, F, represents
independence, since it is the product of the marginals, while the latter, ˚F, does not, unless
r = 0.
In the previous example, we could continue to generate joint distribution functions from
the given marginals as long as we could produce copula functions, even though we started
from marginals of different types. A fortiori, the result would have obtained with marginals
of the same type.
When modeling from the theoretical point of view then, copulas allow a double “infinity”
of degrees of freedom, or flexibility:
(i) define the appropriate marginals and
(ii) choose the appropriate copula.
This flexibility holds also when modeling from the practical (or estimation) point of view,
since the separation between marginal distributions and dependence suggests that we should
decompose any estimation problem into two steps: the first for the marginals and the second
for the copula. We will return to this issue in Chapter 5.
2.3.4
Sklar’s theorem in financial applications: toward a non-Black–Scholes world
This section presents some applications of Sklar’s theorem, as well as of the other copula
properties listed above, to option pricing and credit risk evaluation: by so doing, it devel-
ops the examples in the primer of Chapter 1. It also provides an example in market risk
evaluation.
5 It is the so-called Cuadras–Aug´e one.

62
Copula Methods in Finance
Bivariate digital option pricing
Let us consider two (univariate) put digital options, which pay 1 unit of account iff the
underlying asset is at or below the strike at maturity T . Suppose that the riskless interest
rate is zero. If we denote by X and Y the prices of the underlyings at maturity, and by K and
k their strikes, it is known from martingale pricing theory that (in a complete, arbitrage-free
market) the option prices are:
Pr (X ⩽K) = F1(K)
Pr (Y ⩽k) = F2(k)
The so-called bivariate put digital option, which pays one unit of account iff both X and Y
are at or below the strike, has price
Pr (X ⩽K, Y ⩽k) = F(K, k)
According to Sklar’s theorem, it is always possible to represent this price in terms of the
single digital prices:
F(K, k) = C(F1(K), F2(k))
and the representation is unique on Ran F1 × Ran F2. It is unique tout court if X and Y
are continuous.
If the riskless interest rate is different from zero, then the price at 0 is B(0, T )C(F1(K),
F2(k)) where B(0, T ) is the discount factor from T to 0, so that C(F1(K), F2(k)) is the
forward price.
Assume now that X and Y are log-normally distributed, with log returns, ln(X/X0) and
ln(Y/Y0), normal with mean

r −1
2σ 2
X

T ,

r −1
2σ 2
Y

T and variance σ 2
XT , σ 2
Y T respec-
tively, as in the (risk-neutralized) Black–Scholes model. We have
Pr (X ⩽K) = F1(K) = 

−
ln (X0/K) +

r −1
2σ 2
X

T
σX
√
T

≡(−d2X(K))
Pr (Y ⩽k) = F2(k) = 

−
ln (Y0/k) +

r −1
2σ 2
Y

T
σY
√
T

≡(−d2Y(k))
and therefore
Pr (X ⩽K, Y ⩽k) = F(K, k) = C (F1(K), F2(k)) = C ((−d2X(K)),  (−d2Y (k)))
Suppose, for instance, that K = 2, k = 1
2, X0 = Y0 = 1, r −1
2σ 2
X = r −1
2σ 2
Y = 0, σX =
σY = 0.2, T = 5, so that
−d2X(K) = 1.55,
−d2Y (k) = −1.55
Then the forward bivariate digital price is
F(2, 1
2) = C ((1.55),  (−1.55)) = C(0.9394, 0.0606)

Bivariate Copula Functions
63
If in addition we assume C = C−, then the forward price becomes
max ((1.55) +  (−1.55) −1, 0) = max(0.9394 + 0.0606 −1, 0) = 0
If instead we assume C = C+, we obtain
min((1.55), (−1.55)) = min(0.9394, 0.0606) = 0.0606
and it follows from the Fr´echet inequality that
0 ⩽C(0.9394, 0.0606) ⩽0.0606
In particular, if we assume independence between the two returns, we have argued in
Chapter 1 and will see below that C = C⊥. The forward digital price is
(1.55) (−1.55) = 0.0569
However, the natural extension of the Black–Scholes model to a bivariate setting consists
in assuming jointly normal returns. In we assume that ln

X/X 0

and ln

Y /Y 0

are not only
marginally, but also jointly normally distributed, with correlation coefficient ρ, Corollary 2.3
permits us to state that their copula is the so-called Gaussian one, defined as:
CGa(v, z) =

 −1(v)
−∞

 −1(z)
−∞
1
2π
 
1 −ρ2 exp
!
2ρsω −s2 −ω2
2

1 −ρ2
"
dsdω
Using the copula framework, the no-arbitrage forward price of the bivariate digital option is
Pr (X ⩽K, Y ⩽k) = F(K, k) = CGa((−d2X(K)), (−d2Y(k)))
=

 −d2X(K)
−∞

 −d2Y (k)
−∞
1
2π
 
1 −ρ2 exp
!
2ρsw −s2 −w2
2

1 −ρ2
"
dsdw
If K = 2, k = 1
2, as previously assumed, and ρ = 20%, the price turns out to be
F

2, 1
2

=

 1.55
−∞

 −1.55
−∞
1
2π
√
1 −0.22 exp
!
0.4sw −s2 −w2
2

1 −0.22
"
dsdw = 0.886
If, in the previous case, we use a copula other than the Gaussian one, this means that, via
copulas, we are extending bivariate financial modeling beyond Black–Scholes. Consider, for
instance, two stock indices, DAX 30 and FTSE 100. Assume that they are marginally normal.
Using a daily time series from January 2, 1999, to March 27, 2000, one can argue that
their (daily) variances are respectively σ 2
X = 0.0147 and σ 2
Y = 0.01197, while, considering
the riskless rate on the euro zone, µX = r −1
2σ 2
X = 0.0013 and µY = r −1
2σ 2
Y = 0.0004.

64
Copula Methods in Finance
Cherubini and Luciano (2002a) argue that for these indices the “best fit” copula, starting
from a selection of three, is the so-called Frank copula6:
CA(v, z) = −1
α ln

1 + (exp (−αv) −1) (exp (−αz) −1)
exp (−α) −1

(2.11)
Under this copula, the no-arbitrage forward price of the bivariate digital option is
Pr (X⩽K, Y ⩽k)=F(K, k)=CA((−d2X(K)), (−d2Y(k)))
=−1
α ln

1 +

exp (−α(−d2X(K)) −1)
 
exp (−α(−d2Y(k)) −1)

exp (−α) −1
#
If K = 2, k = 1
2, X0 = Y0 = 1, T = 5 and, as turns out from the estimates in Cherubini
and Luciano (2002a), α = 4.469, the price becomes
F(2, 1
2) = −
1
4.469 ln



1 +

exp (−4.469(−d2X(2)) −1)

×

exp (−4.469(−d2Y(1/2)) −1)

exp (−4.469) −1



= 0.0231
The copula approach then has allowed us, starting from marginally normal returns (with no
joint behavior hypothesis) to obtain bounds for the bivariate digital price, then (under joint
normality) to reconstruct the Black–Scholes price, and finally to price the derivative under
the “best fit” dependence function choice.
Credit risk evaluation
We have seen in Chapter 1 that, in Merton’s (1974) structural approach to credit risk, a firm
defaults if its asset value falls below the debt at maturity of the latter, T . Denote with V
and W the asset values at debt maturity of two firms and assume them to be log-normal:
ln (V/V0) and ln (W/W0) are normal, with risk neutral means

r −σ 2
V /2

T ,

r −σ 2
W/2

T
and variances σ 2
V T , σ 2
WT respectively. Then, the probability that each firm defaults at time
T , if DV (DW) ∈ℜis its debt, is
Pr (V ⩽DV ) = 
!
−ln (V0/DV ) +

r −σ 2
V /2

T
σV
√
T
"
≡ (−d2V (V0))
Pr (W ⩽DW) = 
!
−ln (W0/DW) +

r −σ 2
W/2

T
σW
√
T
"
≡ (−d2W(W0))
6 Please note that in the original paper the current assumption on the marginals is abandoned.

Bivariate Copula Functions
65
and the risk-neutral joint default probability Pr (V ⩽DV , W ⩽DW) can always be written,
according to Sklar’s theorem, as
C ( (−d2V (V0)) ,  (−d2W(W0)))
Suppose, for instance, that the two firms have debts equal to DV = 0.5, DW = 0.7, and V0 =
W0 = 1, µV = µW = 0, σV = σW = 0.2, T = 5, so that −d2V (V0) = −1.55, −d2W(W0) =
−0.797. Then
(−d2V (V0)) = 0.0606,
(−d2V (W0)) = 0.2126
and the joint default probability is
Pr (V ⩽0.5, W ⩽0.7) = C(0.0606, 0.2126)
If C = C−, then the probability becomes 0; if C = C+, then it is 0.0606. As an immediate
application of Fr´echet inequality, no matter which is the dependence function chosen, the
joint default probability always stays between the C−and C+ values:
0 ⩽C(0.0606, 0.2126) ⩽0.0606
In particular, if C = C⊥, then it is 0.0129.
If the returns on the two firms are jointly normal at T , in addition to being marginally
normal, we are again in the Black–Scholes framework. The joint default probability at time
T , since the copula for the firms’ values and returns is the same,7 is the Gaussian one:
H(DV , DW) = Pr (V ⩽DV , W ⩽DW) = CGa ( (−d2V (V0)) ,  (−d2W(W0)))
Suppose, for instance, that the asset returns have a correlation coefficient 1
2, while the
outstanding debts are 0.5 and 0.7, as above: the joint default probability is
H(0.5, 0.7) =

 −1.55
−∞

 −0.0797
−∞
1
2π
√
1 −0.52 exp
!
sw −s2 −w2
2

1 −0.52
"
dsdw = 0.0069
The extension of the Black–Scholes framework in the default context could proceed
along the same lines of the bivariate option example: assume a copula different from the
Gaussian one, even if the marginals are Gaussians.
In order to make the reader aware of the full flexibility of copulas however, let us explore
a totally different way to obtain joint default probabilities via copulas. In contrast with the
Merton’s case, let us consider historical default probabilities, following Luciano and Marena
(2003).
As is well known, rating agencies provide tables (see Table 2.1), such as those of S&P,
reported below, which give the marginal default probabilities Fi(t) for different maturities
and depending on the rating of the issuer:
7 The result is straightforward in the example, when one switches from returns to values, and will be proved in
general for increasing transforms in section 2.4.3 below.

66
Copula Methods in Finance
Table 2.1
Historically observed default probabilities, source:
S&P, 2000
Rating
Maturity
AAA
AA
A
BBB
1
0.00%
0.01%
0.04%
0.22%
2
0.00%
0.04%
0.11%
0.50%
3
0.03%
0.09%
0.19%
0.79%
4
0.06%
0.16%
0.32%
1.30%
5
0.10%
0.25%
0.49%
1.80%
7
0.26%
0.53%
0.83%
2.73%
8
0.40%
0.63%
1.01%
3.10%
9
0.45%
0.70%
1.21%
3.39%
10
0.51%
0.79%
1.41%
3.68%
15
0.51%
1.07%
1.83%
4.48%
We can immediately use these marginal default probabilities in a copula representation
of the joint default probability
Pr(T1 ⩽t, T2 ⩽t) = C(F1(t), F2(t))
Consider, for instance, an AAA and a simple A obligor, and focus attention on the
maturities t = 1, 5, 10, 15:
F(1, 1) = C(0%, 0.04%)
F(5, 5) = C(0.1%, 0.49%)
F(10, 10) = C(0.51%, 1.41%)
F(15, 15) = C(0.51%, 1.83%)
For each specific copula choice, we can easily evaluate the joint default probability, by
simple substitution.
Also, by choosing a single-parameter copula, such as the Gaussian or Frank defined above,
we can study the behavior of the joint probability with respect to the parameter choice: since
the copula represents dependence, its parameter, in analogy with the Gaussian case, must
give a measure of how much the random variables in the copula (the times to default,
here) “move together”.8 Let us denote as d(F1(t), F2(t), α) the joint default probability as
a function of the parameter value:
d(F1(t), F2(t), α) = C(F1(t), F2(t); α)
and consider a Frank copula.
When α, the association parameter, varies from 1 to 25, we get the increasing behavior
of the joint default probabilities illustrated in Figure 2.5.
8 This concept will be clarified and made exact in Chapter 3.

Bivariate Copula Functions
67
d(.00,.0004, a)
3.10−4
2.10−4
1.10−4
00
10
20
a
30
d(.001,.0049, a)
d(.0051,.00141, a)
d(.0051.,.00183, a)
Figure 2.5
Joint default probabilities between an AAA and an A obligor, as a function of dependence
(a = α in the text), over 1, 5, 10, 15 years (lines from bottom to top), Frank copula
d(.00,.0022, a)
0.004
0.002
00
10
20
a
d(.001,.018, a)
d(.0051,.00368, a)
d(.0051.,.0448, a)
Figure 2.6
Joint default probabilities between an AAA and a BBB obligor, as a function of depen-
dence (a = α in the text), over 1, 5, 10, 15 years (lines from bottom to top), Frank copula
Figure 2.6 presents analogous results, for an AAA and a BBB obligor.
A comparison between the two figures permits us to verify that the increase of the
probabilities is much less pronounced in the second case than in the first: the greater the
rating class distance between the counterparties, the less increase we notice in the joint
default probability. This happens homogeneously across maturities.
In the bivariate option example the use of copulas permitted us to abandon the Black–
Scholes assumption and to adopt the “best fit” model for joint behavior. Here, even without
aiming at best fitting the joint model (due to the generality of the marginals), we obtained
a sensitivity analysis with respect to the copula parameter, which, as claimed above, must
represent the “dependence” between the underlying random variables. This will be the object
of Chapter 3.

68
Copula Methods in Finance
VaR computation
Copulas have been applied to the measurement of market risk, in particular to the assessment
of the Value at Risk (VaR) of a portfolio. Let us recall that, for a given confidence level θ,
VaR is the level under which returns will fall only with probability θ. If we denote as Z
the portfolio return over a given horizon T , VaR is the threshold such that:
Pr(Z ⩽VaRZ) = θ
Equivalently, using the distribution function of Z, H(z), VaR can be defined as the solution
z∗of the equation H(z∗) = θ. In turn, the distribution function H can be written via copulas,
as follows. Consider a portfolio of two assets. Let X and Y be their continuous returns,
over a common horizon T , and let β ∈(0, 1) be the weight of X. The portfolio return is
Z = βX + (1 −β) Y, with distribution function
H(z) = Pr(Z ⩽z) = Pr(βX + (1 −β) Y ⩽z)
=
+∞

−∞
Pr

X ⩽1
β z −1 −β
β
y, Y = y

f2(y)dy
=
+∞

−∞
C1|2

F1
 1
β z −1 −β
β
y

, F2(y)

f2(y)dy
(2.12)
where the conditional probability assessment via C1|2, introduced in Remark 2.2, has been
used.
Suppose, as in Luciano and Marena (2003), that the returns on two assets X and Y have
been estimated to be distributed according to a Student’s t, with 5 and 6 d.o.f. respectively.
Formally, we have
F1(x) =

 x
−∞
(3)
(5/2)
√
5π

1 + u2
5
−3
du
F2(y) =

 y
−∞
(7/2)
(3)
√
6π

1 + u2
6
−7/2
du
where  is the usual Euler function.
Assume that the Frank copula represents their association, and let α = −3, so as to
consider a case of negative “dependence” between the two assets, which hedge each other.
By letting the allocation weight vary from 10% to 90%, and considering both the level
of confidence (loc) 95% and the 99% one, formula (2.12) gives the values at risk shown in
Table 2.2.
Three facts are evident from Table 2.2: first, as usual, diversification pays, since when
the allocation weight gets closer to 50% the VaR decreases, for given level of confidence;
second, due to the fat-tailed nature of the returns, the VaR increases substantially with
the loc, for given allocation weight; third, for symmetric weights (for instance β = 10%,
1 −β = 90% and β = 90%, 1 −β = 10%), the VaR is greater when β increases, since X is
riskier than Y (the variance of a Student’s t is υ/(υ −2), where υ is the number of d.o.f.).

Bivariate Copula Functions
69
Table 2.2
VaR for the bivariate portfolio of page 68, as a function of β and
the loc, Students’s t marginals, Frank copula
β
10%
25%
50%
75%
90%
loc 95%
−1.670
−1.332
−1.093
−1.379
−1.735
loc 99%
−2.726
−2.197
−1.792
−2.344
−2.917
Table 2.3
VaR for the bivariate portfolio of page 68, as a function of β and the
loc, normal marginals, Frank copula
β
10%
25%
50%
75%
90%
loc 95%
−1.735
−1.373
−1.105
−1.453
−1.835
loc 99%
−2.459
−1.983
−1.622
−2.093
−2.599
Table 2.4
VaR for the bivariate portfolio of page 68, as a function of β and the
loc, Students’s t marginals, product copula
β
10%
25%
50%
75%
90%
loc 95%
−1.757
−1.549
−1.422
−1.590
−1.818
loc 99%
−2.823
−2.451
−2.217
−2.587
−3.011
The copula approach then allows us to compute the VaRs for a portfolio with a non-
normal joint distribution, and to study its sensitivity with respect to the portfolio mix. We
could also study the sensitivity with respect to the copula parameter, as we did in the credit
risk case.
Moreover, the copula approach has still its double “infinity” of d.o.f. to be exploited: it
permits us either (i) to change the marginals while keeping the copula fixed or (ii) to change
the copula while keeping the marginals fixed.
In the first case, suppose you want to eliminate the fat-tails effect of the Student’s t, and
consider the returns as being normal, with zero mean and the same standard deviations as
above (1.291 for X and 1.225 for Y). The VaRs are shown in Table 2.3.
At the loc 99%, the VaR values for each allocation weight are smaller in absolute value
than in Table 2.2, since we no longer have fat tails. However, for the very nature of the
tails, this effect shows up only at the higher quantile.
In the second case, keep the marginals fixed (Student’s t) and assume independence
between the returns, i.e. a product copula.9 We get Table 2.4.
As expected, the VaR values for each couple loc–allocation weight are greater (in absolute
value) than in Table 2.2, since the two assets no longer hedge.
To conclude, the copula approach to VaR permits us to avoid the usual assumption of
marginal and joint normality. For the marginals, one can indeed use in (2.12) any choice
of F1, F2, so as to take into account, as above, fat tails. For the copula, functions with
9 As we will argue in Chapter 3, the Frank copula also degenerates into the product one when the parameter goes
to zero.

70
Copula Methods in Finance
so-called upper (or lower) tail dependency (see the next chapter) have been suggested. The
very powerfulness of the copula approach, however, consists in separating the marginal
and dependence effects, as the example, as well as the previous pricing and credit risk
ones, shows.
2.4
COPULAS AS DEPENDENCE FUNCTIONS: BASIC FACTS
Since copulas are dependence functions, they permit us to characterize independence and
perfect dependence in a straightforward way. Since they separate the marginal behavior
from dependence itself, they turn out to be invariant w.r.t. increasing the transform of the
(continuous) r.v.s X and Y. Let us analyze these features separately.
In order not to be obliged to distinguish the (unique) copula of X and Y on Ran F1 ×
Ran F2 from its (non-unique) extension to the whole of I 2, in this section we assume that
X and Y are continuous random variates.
2.4.1
Independence
Recall that X and Y are independent r.v.s iff F(x, y) = F1(x)F2(y). It is evident that Sklar’s
theorem entails
Corollary 2.4
The r.v.s X and Y are independent iff they have the product copula C⊥.
2.4.2
Comonotonicity
Two r.v.s are comonotone or countermonotone – and therefore perfectly dependent – iff
their copula is respectively the upper and lower Fr´echet bound. To make this statement
precise, let us recall the following.
Definition 2.6
The set A ⊂ℜ∗2 is said to be comonotic iff, for any (x1, y1), (x2, y2) in
A, either
 x1 ⩽y1
x2 ⩽y2
or
 x1 ⩾y1
x2 ⩾y2
Definition 2.7
A random vector (X, Y) is comonotonic or perfectly positively dependent
iff there exists a comonotonic set A ⊂ℜ∗2 such that
Pr((X, Y) ∈A) = 1
Loosely said, a couple of comonotonic random variates has outcomes that are ordered
componentwise: realizations for which X is higher, have Y higher too. The comonotonic
property can be characterized in a number of equivalent ways, as the following theorem,
which appears up to point 5 also in Dhaene et al. (2002), shows:
Theorem 2.6
A random vector (X, Y), with marginal distribution functions F1, F2 and
joint distribution F(x, y) is comonotonic iff one of the following (equivalent) statements
holds:

Bivariate Copula Functions
71
(1) (X, Y) has comonotonic support
(2) (Hoeffding, 1940; Fr´echet, 1951) for every (x, y) ∈ℜ∗2
F(x, y) = min(F1(x), F2(y))
(3) C(v, z) = C+(v, z)
(4) (Hoeffding, 1940; Fr´echet, 1951) (X, Y) is distributed as (F −1
1 (U), F −1
2 (U)), where U
is a standard uniform random variate
(5) (X, Y) is distributed as (F −1
1 (F2(Y)), F −1
2 (F1(X)))
It follows that
Corollary 2.5
If F1 = F2, then X and Y are comonotonic iff they are equal a.s.
A symmetric definition for countermonotonic or perfectly negatively dependent random
variates can be given as:
Definition 2.8
The set A ⊂ℜ∗2 is said to be countermonotonic iff, for any (x1, y1), (x2, y2)
in A, either
 x1 ⩽y1
x2 ⩾y2
or
 x1 ⩾y1
x2 ⩽y2
Definition 2.9
A random vector (X, Y) is countermonotonic or perfectly negatively
dependent iff there exists a countermonotonic set A ⊂ℜ∗2 such that
Pr((X, Y) ∈A) = 1
The following theorem can be easily demonstrated.
Theorem 2.7
A random vector (X, Y), with marginal distribution functions F1, F2 and
joint distribution F(x, y) is countermonotonic iff one of the following (equivalent) state-
ments holds:
(1) (X, Y) has countermonotonic support
(2) (Hoeffding, 1940; Fr´echet, 1951) for every (x, y) ∈ℜ∗2
F(x, y) = max(F1(x) + F2(y) −1, 0)
(3) C(v, z) = C−(v, z)
(4) (Hoeffding, 1940; Fr´echet, 1951) (X, Y) is distributed as (F −1
1 (U), 1 −F −1
2 (U)), where
U is a standard uniform random variate
(5) (X, Y) is distributed as (F −1
1 (1 −F2(Y)), F −1
2 (1 −F1(X)))
Example 2.9
The r.v.s in Example 2.7 have the C−copula: the previous theorem entails
that Y = F −1
2 (1 −F1) a.s.
Recalling that X and Y are exponential, with the inverse (2.10), we have
Y = −ln(1 −exp (−λ1X))/λ2

72
Copula Methods in Finance
2.4.3
Monotone transforms and copula invariance
Copulas of increasing or decreasing transforms of (continuous) r.v.s are easily written
in terms of the copula of X and Y: in particular, copulas are invariant w.r.t. increasing
transforms.
Let αi : ℜ∗→ℜ, i = 1, 2, be two functions, increasing a.s. It is known from elementary
probability theory that the margins of the r.v.s α1(X), α2(Y) are transformations of the
corresponding Fi, i.e.
α1(X) ∼F1

α−1
1

,
α2(Y) ∼F2

α−1
2

Let us denote the margins Fi

α−1
i

as Hi. The following theorem holds:
Theorem 2.8 (Schweizer & Wolff, 1976, 1981)
Let X, Y be continuous random variables
with marginal distribution functions F1, F2 and copula C. If α1, α2 are two transformations,
increasing (a.s.), the r.v.s α1(X), α2(Y), which have marginal distribution functions H1 =
F1

α−1
1

, H2 = F2

α−1
2

and joint one H
H(u, t) = Pr(α1(X) ⩽u, α2(Y) ⩽t)
have copula C too:
H(u, t) = C(H1(u), H2(t))
Loosely speaking, copulas are invariant w.r.t. increasing transformations, even though the
latter act differently on X and Y (α1 ̸= α2).
Example 2.10
Consider two standard normals X and Y and let their dependence be repre-
sented by the Gaussian copula. If we consider now the increasing transforms U = exp(X),
T = exp(Y), which we know to be log-normally distributed, we can state, according to
Theorem 2.8, that they still have the Gaussian copula. Therefore, their joint distribution
function is
H(u, t) = CGa(H1(u), H2(t)) = CGa((ln u), (ln t))
Conversely, if one starts with X and Y log-normally distributed, so that U = ln X and
T = ln Y are standard normal, and assumes the Gaussian copula for X and Y, then the joint
distribution of U and T , according to Theorem 2.8, is
H(u, t) = CGa( ˙H1(u), ˙H2(t)) = CGa( ⃗(eu), ⃗(et))
where ⃗ is the log-normal distribution function with parameters (0, 1), and ˙H1 and ˙H2 are
the margins of U and T .
Analogously, one could demonstrate that for α1 increasing a.s. and α2 decreasing a.s.,
ceteris paribus,
H(u, t) = H1(u) −C(H1(u), 1 −H2(t))

Bivariate Copula Functions
73
For α1 decreasing and α2 increasing (both a.s.)
H(u, t) = H2(t) −C(1 −H1(u), H2(t))
while for both α1 and α2 decreasing (both a.s.)
H(u, t) = H1(u) + H2(t) −1 + C(1 −H1(u), 1 −H2(t))
(2.13)
From the behavior of the copula w.r.t. increasing or decreasing transforms, and in particular
from the fact that “the copula is invariant while the margins can be changed at will”, a
number of theoretical and applicative consequences follow.
From the theoretical point of view, it follows that “any functional or ‘property’ of the joint
distribution function of (two) r.v.s that is invariant under strictly increasing transformations
of the r.v.s is a functional or ‘property’ of their copula (and independent of the individual
distributions . . .). Thus . . . it is natural to use any measure of distance between surfaces
as a measure of dependence for pairs of r.v.s” (Schweizer & Sklar, 1983): this is the
core of the definition of concordance between r.v.s, which we will discuss in the next
chapter.
From the point of view of applications, the comonotonicity property, together with invari-
ance, allows us to fully exploit the copula tool to enlarge financial modeling. An example
is presented in the next section.
2.4.4
An application: VaR trade-off
Let us introduce an example in which the copula technique itself suggests an economic
evaluation, the trade-off between values at risk.
Let us consider, as in Cherubini and Luciano (2001), the returns on two stock indices,
namely the FTSE 100 and the S&P 100. Starting from their daily closing prices from
January 3, 1995 to April 20, 2000, compute the empirical marginal distributions of their
log returns X and Y, i.e. their cumulated frequencies. Let us denote them as F1(xi), F2(yi),
i = 1, 2, . . . , n respectively.
As a first step, determine the level curves of the two indices, returns, using the minimum,
product and maximum copula. Recalling the definition, they are respectively the loci of
points
{(v, z) : max(v + z −1, 0) = K} ,
K ∈I
{(v, z) : vz = K} ,
K ∈I
{(v, z) : min(v, z) = K} ,
K ∈I
As the readers learned from Theorems 2.6 and 2.7, the first copula – and then the first
level curves – apply if (and only if) the returns on the FTSE and S&P are countermono-
tonic, the second if (and only) they are independent, the third if (and only if) they are
comonotonic.
Cherubini and Luciano (2001) also computed some level curve values using the Clayton
copula, defined as
CC(v, z) = max

v−α + z−α −1
−1/α , 0

(2.14)

74
Copula Methods in Finance
They adopted the parameter value α = 1
2, since this was demonstrated to be the “best fit”
one. Under the Clayton choice, with parameter value 1
2, the level curves have equation:
{(v, z) : (v−1/2 + z−1/2 −1)−2 = K},
K ∈I
As a second step, use the empirical marginals in order to reconstruct the return values
corresponding to the (v, z) couples of each curve, by (generalized) inversion: F −1
1 (v) =
infi {xi : F1(xi) ⩾v}, and analogously for Y. By so doing, one obtains the probability level
curves
{(x, y) : F(x, y) = C(F1(x), F2(y)) = K%}
For a given value of the FTSE return (on the abscissa axis), the latter represent the return
on the S&P which gives a joint distribution value of K%, i.e. such that the joint probability
of occurrence of smaller or equal returns is K%.
Figure 2.7 presents the level curves of the minimum, product, maximum and fitted Clayton
copulas for K = 1%, i.e. it represents the couples
{(x, y) : max(F1(x) + F2(y) −1, 0) = 1%}
{(x, y) : F1(x)F2(y) = 1%}
{(x, y) : min(F1(x), F2(y)) = 1%}
{(x, y) : (F1(x)−1/2 + F2(y)−1/2 −1)−2 = 1%}
−0.04
−0.03
−0.02
−0.01
0
0.01
0.02
0.03
0.04
0.05
0.06
0.07
−0.04
−0.03
−0.02
−0.01
0
0.01
0.02
0.03
0.04
0.05
Fitted
Perf.Corr+
Perf.Corr−
Independence
Figure 2.7
Level curves for returns on FTSE and S&P 100, corresponding to the (fitted) Clayton
copula, the maximum one (perfect positive correlation), the minimum one (perfect negative correlation)
and the product (independence) one

Bivariate Copula Functions
75
The top right line in the figure corresponds to the countermonotonic case, while the bottom
left line corresponds to the comonotonic one: evidently, it is higher in the countermonotonic
than in the comonotonic case, since in the former the two indices are perfect hedges, but
in the second not at all. The independence case is between the two, and to the right of the
fitted one, since, as we remarked above, positively ordered families (such as the Clayton)
have level curves that shift upwards as the parameter decreases.
Using these curves, we can answer the following question: which are the levels x and y
(respectively) of the DAX and FTSE returns, to be interpreted as (percentage) VaRs, that
will be trespassed only with (joint) probability 1%? The level curves of the previous figure
give these thresholds for the two assets, and therefore represent the VaR trade-off between
the British and USA markets. As Cherubini and Luciano (2001) remark, “the closer the
trade-off line to the lower region of the triangle, the higher the ‘correlation’ between losses:
in this case, the joint probability cannot be affected by moving capital from one desk to
another. On the contrary, if the trade-off line is close to the upper region of the triangle,
we have negative dependence, and the losses of the two business units tend to offset each
other. Finally, if the trade-off schedule is close to the independence line, trading-off capital
from one desk to another is made possible by diversification. The case of our application
is (. . .) close to the independence schedule.”
2.5
SURVIVAL COPULA AND JOINT SURVIVAL FUNCTION
This section introduces the notions of survival copula and joint survival function, it discusses
the relationships between them and applies them to the evaluation of the distribution func-
tions of maxima and minima of two r.v.s. A financial application follows. Let us introduce
the following definition.
Definition 2.10
The survival copula associated with the copula C, is
C(v, z) = v + z −1 + C(1 −v, 1 −z)
It is easy to verify that C has the copula properties. Once computed in (1 −v, 1 −z), it
represents the probability that two standard uniform variates with copula C be greater than
v, z respectively, since
C(1 −v, 1 −z) = 1 −v + 1 −z −1 + C(v, z)
= 1 −Pr(U1 ⩽v) + 1 −Pr(U2 ⩽z) −1 + Pr(U1 ⩽v, U2 ⩽z)
= Pr(U1 > v) + Pr(U2 > z) −1 + Pr(U1 ⩽v, U2 ⩽z)
= Pr(U1 > v, U2 > z)
Since C is a copula, it stays within the Fr´echet bounds:
C−≺C ≺C+
In addition, it can be easily verified that in the minimum, product and maximum case,
copulas and survival copulas coincide:
C−= C−,
C⊥= C⊥,
C+ = C+

76
Copula Methods in Finance
Sklar’s theorem can be restated in terms of survival copula: to this end, given the random
variables X and Y, let us consider
F(x, y) = Pr(X > x, Y > y)
(2.15)
and denote as F i the complement to one of Fi. Notice that, as is known from elementary
probability, F can be written in terms of F as 1 −F1 (x) −F2 (y) + F(x, y). It follows that:
F(x, y) = F 1 (x) + F 2 (y) −1 + C(1 −F 1 (x) , 1 −F 2 (y))
(2.16)
Sklar’s theorem guarantees the existence of a subcopula, the survival one, unique on
Ran F 1 × Ran F 2, such that the probability (2.15) can be represented in terms of F 1 (x),
F 2 (y) , i.e. F(x, y) = C(F 1(x), F 2(y)). Before introducing it, let us notice that in the Actu-
arial (reliability theory) field F 1 (x) is named the marginal survival probability or survival
function of X: it represents the probability of survivalship of the agent (respectively, com-
ponent) of age X beyond x. Since the probability (2.15) represents the joint survival
probability or survival function of X and Y respectively beyond time x and y, the copula
which represents it in terms of the marginal survival probabilities or survival distribution
functions of the two agents or components separately, F 1 (x) and F 2 (y), is named survival
copula. With this terminology, we have:
Theorem 2.9
Let F 1(x), F 2(y) be (given) marginal survival functions. Then, for every
(x, y) ∈ℜ∗2:
(i) if C is any subcopula whose domain contains Ran F 1 × Ran F 2,
C(F 1(x), F 2(y))
is a joint survival function with margins F 1(x), F 2(y);
(ii) conversely, if F(x, y) is a joint survival function with margins F 1(x), F 2(y), there
exists a unique subcopula C, with domain Ran F 1 × Ran F 2, such that
F(x, y) = C(F 1(x), F 2(y))
(2.17)
If F1(x), F2(y) are continuous, the subcopula is a copula; if not, there exists a copula
C such that
C(v, z) = C(v, z)
for every (v, z) ∈Ran F 1 × Ran F 2.
Remark 2.4
By comparing Definition 2.10 and formula (2.13) one can notice that the
joint distribution function of two decreasing transforms of given r.v.s is represented through
their survival copula.

Bivariate Copula Functions
77
It is also possible to express, via survival copula, the conditional probability
Pr(U1 > v | U2 > z) = 1 −v −z + C(v, z)
1 −z
= C(1 −v, 1 −z)
1 −z
and therefore
Pr(X > x | Y > y) = C(F 1 (x) , F 2 (y))
F 2 (y)
It is customary to distinguish the survival copula from the joint survival function for uniform
variates:
Definition 2.11
The joint survival or survival function for (standard) uniform variates
U1, U2 with copula C, denoted as C/, represents, if evaluated at (v, z), the joint probability
that (U1, U2) be greater than v and z respectively:
C/(v, z) = Pr(U1 > v, U2 > z)
(2.18)
It follows from the definition that
C/(v, z) = 1 −v −z + C(v, z) = C(1 −v, 1 −z)
Comparing (2.18) and (2.16), it can easily be argued that, in terms of joint survival function
for uniform variates, the survival probability F(x, y) can be written as
F(x, y) = C/(F1 (x) , F2 (y))
Definition 2.12
Together with the survival copula, we define also the co-copula
C∗(v, z) = 1 −C(1 −v, 1 −z)
and the dual of the copula
˜C(v, z) = v + z −C(v, z)
Remark 2.5
Both the co-copula and the dual are not copulas10, since the former fails
to have property (i) in the subcopula definition, while the latter fails to be 2-increasing
10 As concerns the co-copula, one can notice that C∗∗= C and that the co-copulas of the Fr´echet bounds and the
product copula are respectively
C−∗= min(v + z, 1)
C⊥∗= v + z −vz
C+∗= max(v, z)
As concerns the dual, it coincides with the co-copula in the bounds and product case. In addition, every dual
copula satisfies the following inequality:
˜C+ ≺˜C⊥≺˜C−
since C1 ≺C2 implies ˜C1 ≻˜C2 and vice versa.

78
Copula Methods in Finance
(see Schweizer and Sklar, 1983, lemma 6.4.2). However, they represent respectively the
probability that either X > x or Y > y, and the probability that either X ⩽x or Y ⩽y:
Pr(X > x or Y > y) = C∗(1 −F1(x), 1 −F2(y))
(2.19)
Pr(X ⩽x or Y ⩽y) = ˜C(F1(x), F2(y))
(2.20)
In addition, they have the following property, which will be used in Chapter 8: the dual of
the survival copula is the co-copula. Substituting for the definition in fact it is easy to show
that
≂
C(v, z) = 1 −C(1 −v, 1 −z) = C∗(v, z)
Example 2.11
Consider two independent r.v.s, with copula C(v, z) = vz. It follows that
C/ = (1 −v) (1 −z)
C∗= z + v −vz = 1 −C/
˜C = z + v −vz
from which it is evident, as mentioned above, that C∗= ˜C.
There are several concepts that may be expressed in terms of copulas, survival copulas and
survival functions for uniform variates. For example, the c.d.f. for minima or maxima of
two random variables is easily expressed in terms of copula.
In fact, denote m = min(X, Y) and M = max(X, Y). Let Fm and FM be the d.f.s of the
minimum and maximum respectively.
We have, for maxima:
FM(a) = Pr(M ⩽a) = Pr(X ⩽a, Y ⩽a) = F(a, a) =
= C(F1(a), F2(a))
and, for minima:
Fm(a) = Pr(m ⩽a) = 1 −Pr(m > a)
= 1 −Pr(X > a, Y > a)
= 1 −C/(F1(a), F2(a)) =
= 1 −C(F 1(a), F 2(a))
where, clearly, the point a has to be well chosen in the Ran F1, Ran F2.
2.5.1
An application: default probability with exogenous shocks
Consider the survivalship of two firms, whose default or survival time is denoted as X and
Y, and let them be subject to three shocks, two idiosyncratic ones and the latter common
to both firms. Let us assume that the shocks follow three independent Poisson processes

Bivariate Copula Functions
79
with parameters λ1, λ2 and λ12, where the index denotes the firm/s on which the shock
has effect: this means that the times of occurrence of the shocks, denoted respectively as
Z1, Z2, Z12, are independent and exponential, with parameters λ1, λ2 and λ12 respectively.
Their distribution functions, denoted as G1, G2, G12, are:
G1(z1) = 1 −exp (−λ1z1)
G2(z2) = 1 −exp (−λ2z2)
G12(z12) = 1 −exp (−λ12z12)
If the shocks ever occur, the corresponding firm defaults, so that
X = min(Z1, Z12),
Y = min(Z2, Z12)
The probability that X survives beyond x, F 1(x), is
F 1(x) = Pr(X > x) = Pr(Z1 > x, Z12 > x)
= G1(x)G12(x) = exp(−(λ1 + λ12)x)
(2.21)
Analogously for Y:
F 2(y) = exp(−(λ2 + λ12)y)
(2.22)
The probability that both survive beyond x and y respectively, F(x, y), is
F(x, y) = Pr(X > x, Y > y) = Pr(min(Z1, Z12) > x, min(Z2, Z12) > y)
= Pr(Z1 > x) Pr(Z2 > y) Pr(Z12 > max(x, y))
= exp (−λ1x) exp (−λ2y) exp (−λ12 max(x, y))
= exp(−(λ1 + λ12)x −(λ2 + λ12)y + λ12 min(x, y))
(2.23)
Substituting for (2.21) and (2.22) we get
F(x, y) = F 1(x)F 2(y) min(exp(λ12x), exp(λ12y))
In turn, having defined
m =
λ12
λ1 + λ12
,
n =
λ12
λ2 + λ12
we recognize that
exp(λ12x) = F 1(x)−m,
exp(λ12y) = F 2(y)−n

80
Copula Methods in Finance
so that the survival probability is
F(x, y) = F 1(x)F 2(y) min

F 1(x)
−m ,

F 2(y)
−n
= min

F 2(y)
 
F 1(x)
1−m ,

F 1(x)
 
F 2(y)
1−n
(2.24)
It is easy to verify that this joint survival probability can be written in terms of the one of
X and Y, F(x, y) = C(F 1 (x) , F 2 (y)), using the following survival copula, named after
Marshall and Olkin (1967a, b):
CMO(v, z) = min(v1−mz, vz1−n) =
 v1−mz,
vm ⩾zn
vz1−n,
vm < zn
The joint survival probability beyond time t for instance is:
F(t, t) = C
MO(F 1(t), F 2(t))
= min

F 2(t)
 
F 1(t)
1−m ,

F 1(t)
 
F 2(t)
1−n
(2.25)
and the corresponding default probability is:
Pr(X ⩽t, Y ⩽t) = C
MO(F 1(t), F 2(t)) −1 + F1(t) + F2(t)
Suppose for instance that the two firms belong to the chemical and food sector respectively,
and that the three shocks are, respectively, of the chemical sector, the food one, and of the
economy as a whole. Let the expected time of occurrence of the three shocks be respectively
2, 1 and 4 years, which implies11 λ1 = 0.5, λ2 = 1, λ12 = 0.25. It follows that the survival
probability of the two firms beyond x and y respectively is
F 1(x) = exp(−(λ1 + λ12)x) = exp(−0.75x)
F 2(y) = exp(−1.25y)
(2.26)
while their joint survival probability, according to the Marshall–Olkin model, is
CMO(F 1(x), F 2(y)) = min
'
exp(−1.25y)
 
exp(−0.5x)

,

exp(−0.75x)
 
exp(−y)
(
=
 exp(−1.25y −0.5x),
x ⩽y
exp(−0.75x −y),
x > y
since m = 1/3, n = 1/5. The joint survival probability beyond x = y = t = 3 years for
instance is
C
MO(F 1(3), F 2(3)) = exp(3 (−1.25 −0.5)) = 0.5248%
11 For an exponential r.v. the expected value is the reciprocal of the intensity.

Bivariate Copula Functions
81
2.6
DENSITY AND CANONICAL REPRESENTATION
This section introduces the notion of density and canonical representation of a copula,
together with those of its absolutely continuous and singular components.
Copulas, similarly to distribution functions, admit the notion of density:
Definition 2.13
The density c(v, z) associated to a copula C(v, z) is
c(v, z) = ∂2C(v, z)
∂v∂z
Theorem 2.10
The density exists a.e. in the interior of I 2 and is non-negative.
Example 2.12
The density of the Gaussian copula is
1
 
1 −ρ2 exp
!
ζ 2
1 + ζ 2
2
2
+ 2ρζ1ζ2 −ζ 2
1 −ζ 2
2
2

1 −ρ2
"
(2.27)
where ζ1 := −1 (v), ζ2 := −1 (z). This is represented, for ρ = 0.5, in Figure 2.8.
The density can be used in order to define the absolutely continuous component and the
singular component of C, denoted as AC and SC, as follows (Nelsen, 1999):
AC(v, z) =

 v
0

 z
0
∂2C(u, t)
∂u∂t
dudt
SC(v, z) = C(v, z) −AC(v, z)
In turn, a copula for which C = AC on I 2 is called absolutely continuous, while it is called
singular if C = SC on I 2. In the latter case c = 0 a.e. A copula that is neither absolutely
0
Figure 2.8
The Gaussian copula density, ρ = 0.5

82
Copula Methods in Finance
continuous nor singular, C = AC + SC, is said to have an absolutely continuous and a
singular component.
Non-negativity of the density permits us to ascertain the 2-increasing property in a
straightforward way, if C is absolutely continuous:
Example 2.13
Suppose that we want to verify that the function
h(v, z) :=

 −1(v)
−∞

 −1(z)
−∞
1
2π
 
1 −ρ2 exp
!
2ρsw −s2 −w2
2

1 −ρ2
"
dsdw
is actually a copula. It is easy to check that
(i) h(0, z) = h(v, 0) = 0
(ii) h(1, z) = z, h(v, 1) = v
(iii) C = AC, ∂2h(v,z)
∂v∂z
⩾0 : h is absolutely continuous, with non-negative mixed second
partial derivative, which means that it is 2-increasing
(iv) Dom h = I 2
It follows that h is a copula.
Each copula induces a probability measure on I 2, which is nothing other than the C-mass
of section 2.1, definition 2.2. The C-measure of the absolute component is AC(1, 1), while
the one of the singular component is SC(1, 1).
Example 2.14
The product copula C⊥= vz is absolutely continuous, since for every
(v, z) ∈I 2
AC =

 v
0

 z
0
∂2ut
∂u∂t dudt =

 v
0

 z
0
dudt = vz = C⊥
The Fr´echet upper bound C+ is singular, since for every (u, t)
∂2C+(u, t)
∂u∂t
= 0
Consequently
AC =

 v
0

 z
0
∂2C+
∂u∂t dudt = 0 ̸= C+
Analogously for the Fr´echet lower bound.
To end up with, consider the Marshall–Olkin copula of section 2.5.1. It is shown in
Nelsen (1999) that, since
∂2CMO(u, t)
∂u∂t
 u−m,
um ⩾tn
t−n,
um < tn

Bivariate Copula Functions
83
then
AC = CMO −µ min(vm, zn)1/µ
where
µ ≡
mn
m + n −mn
It follows that
SC = C −AC = µ min(vm, zn)1/µ
The Marshall–Olkin copula has then both an absolutely continuous and a singular compo-
nent. The C-measure of the former is
AC (1, 1) = CMO (1, 1) −µ min(1, 1)1/µ = 1 −µ
while that of the latter is µ.
Notice that for continuous random vectors, the copula density is related to the density of
the distribution F, denoted as f . More precisely, it is equal to the ratio of the joint density
f to the product of the marginal densities fi, i = 1, 2:
c(F1(x), F2(y)) =
f (x, y)
f1(x)f2(y)
(2.28)
since by Sklar’s theorem the following canonical representation holds12:
f (x, y) = c(F1(x), F2(y))f1(x)f2(y)
(2.29)
In the continuous random vector case, the density of the survival distribution, F(x, y),
coincides with the distribution function one, f (x, y). Indeed, the survival copula density,
defined as
c(v, z) = ∂2C(v, z)
∂v∂z
12 In fact, remembering that the probability integral transforms are uniform (U1 = F1(X) and U2 = F2(Y)), we
have X = F −1
1
(U1) and Y = F −1
2
(U2). Since for continuous random variates these transformations are strictly
increasing and continuous
c (u1, u2) = f (F −1
1
(u1), F −1
2
(u2)) · det

∂X/∂U1
∂X/∂U2
∂Y/∂U1
∂Y/∂U2

=
f (F −1
1
(u1), F −1
2
(u2))
f1(F −1
1
(u1)) · f2(F −1
2
(u2))
From the above expression it is clear also that the copula density takes value equal to 1 everywhere when the
original r.v.s are independent.

84
Copula Methods in Finance
exists a.e. and is such that c(v, z) = c(1 −v, 1 −z). It is related to the density of the
survival distribution F, f , by the relationship
f (x, y) = c(1 −F1(x), 1 −F2(y))f1(x)f2(y)
so that
c(F1(x), F2(y)) = c(1 −F1(x), 1 −F2(y))
The canonical representation is very useful when, for a given multivariate distribution and
given marginals, one wants to know the copula that “couples” those marginals. Consider,
for instance, the following example.
Example 2.15
Let X and Y be standard Gaussian, with standard normal joint distribu-
tion. Let their correlation coefficient be ρ. We want to know which copula “couples” their
marginal distributions.
We know that the density of the joint distribution is
1
2π
 
1 −ρ2 exp
!
2ρst −s2 −t2
2

1 −ρ2
"
Using (2.28) one gets the copula density (2.27) and, consequently, the Gaussian copula.
The canonical representation will play also a fundamental role in the estimation procedures
for copulas, treated in Chapter 5.
2.7
BOUNDS FOR THE DISTRIBUTION FUNCTIONS
OF SUM OF R.V.S
A question that is connected to the copula definition and appears frequently in financial
applications is the evaluation of bounds for the distribution function of the sum of two r.v.s.
More precisely, let X and Y be r.v.s with distribution functions F1 and F2, and denote
with FS the distribution function of their sum. We want to find distribution functions FL
and FM such that, for every s ∈ℜ∗
FL(s) = inf
F∈F FS(s)
(2.30)
FM(s) = sup
F∈F
FS(s)
(2.31)
where F is the Fr´echet class which has F1 and F2 as marginals.
The question, posed by Kolmogorov, has been addressed in Moynihan, Schweizer and
Sklar (1978), Frank, Nelsen and Schweizer (1987) and Makarov (1981). It is solved by the
distribution functions
FL(s) = sup
x∈ℜ∗max {F1(x) + F2(s −x) −1, 0} = sup
x∈ℜ∗C−(F1(x), F2(s −x))
(2.32)
FM(s) = inf
x∈ℜ∗min {F1(x) + F2(s −x), 1}
(2.33)

Bivariate Copula Functions
85
The bounds are the best possible in the sense of stochastic dominance, as argued by Frank,
Nelsen and Schweizer (1987). For a.s. positive random variables, they can be improved
only if there exists a copula C−, smaller than the copula of X and Y, different from the
minimum copula:
C−≺C ≺C
Explicit, analytical representations for the bounds exist when X and Y belong to the same
“family”, such as the normal, uniform, Cauchy, (even shifted) exponential or – under some
restrictions on the parameters – (even shifted) Pareto.
Example 2.16
For the exponential family
F1(x) = 1 −exp(−λ1x),
λ1 > 0
(2.34)
F2(y) = 1 −exp(−λ2y),
λ2 > 0
(2.35)
Frank, Nelsen and Schweizer (1987) compute the bounds as follows:
FL(s) = 1 −exp

−λ1λ2
λ1 + λ2

s −
λ1 + λ2
λ1λ2

log
λ1 + λ2
λ1λ2

−1
λ1
log (λ1) −1
λ2
log (λ2)

FM(s) = 1 −exp (−s min(λ1, λ2))
Apart from these analytical cases, Williamson and Downs (1990) give numerical algo-
rithms for the computation of (2.32) and (2.33). The algorithms provide the value at the
point u of the generalized inverse of FL and FM, F −1
L (u) and F −1
M (u), as follows:
F −1
L (u) =
inf
t∈[u,1]

F −1
1 (t) + F −1
2 (u −t + 1)

F −1
M (u) = sup
t∈[0,u]

F −1
1 (t) + F −1
2 (u −t)

2.7.1
An application: VaR bounds
As we showed above, copulas have been applied to the measurement of market risk, in
particular to the assessment of the Value at Risk (VaR) of a portfolio. Suppose that we have
estimated the marginal distribution of two assets in a portfolio and want to “know” the
portfolio VaR without introducing any assumption on their copula. It follows from (2.30),
(2.31), i.e. from the fact that FL(s) ⩽FS(s) ⩽FM(s) for every s, that for any confidence
level θ
VaRM(θ) ⩽VaRS(θ) ⩽VaRL(θ)
(2.36)
where VaRM and VaRL are the VaRs corresponding to the distributions FM and FL. The
latter distributions then provide respectively a lower and an upper bound for the VaR: the
lower bound in particular is interesting, from the point of view of risk management, since it
is the “worst possible outcome”, with the given level of confidence. Opposite to intuition,


## Market Comovements and Copula Families

86
Copula Methods in Finance
SPX
NKY
NKY
CAC
CAC
DAX
UKX
MIB
MIB
SPX
CAC
MIB
MIB
NKY
UKX
DAX
MIB
SPX
CAC
DAX
DAX
NKY
UKX
UKX
SPX
DAX
UKX
SPX
NKY
CAC
–4
–3.5
–3
–2.5
–2
–1.5
–1
–0.5
0
0.5
1
Figure 2.9
VaR bounds at the 95% level of confidence for equally weighted portfolios of couples of
selected stock indices. The first line represents the bounds obtained from the empirical quantiles while
the second and third lines represent the bounds from EVT estimated quantiles and from Student’s t
estimated quantiles respectively
Table 2.5
Comparison between the expected number of exceedances (1st row) and the actual
ones (2nd to 5th column) for couples of selected stock indices, together with their p-values
Var at 95% level
Var at 99% level
E
E
E
E
Lower Bound
Normal VaR
Lower Bound
Normal VaR
Expected
35
7
MIB-DAX
28
65
4
30
(0.11)
(0.00)
(0.12)
(0.00)
MIB-UKX
31
56
9
29
(0.24)
(0.00)
(0.23)
(0.00)
MIB-SPX
18
58
5
23
(0.00)
(0.00)
(0.22)
(0.00)
MIB-CAC
26
61
7
25
(0.06)
(0.00)
(0.49)
(0.00)
DAX-UKX
32
62
8
33
(0.29)
(0.00)
(0.36)
(0.00)
DAX-SPX
21
62
6
28
(0.01)
(0.00)
(0.35)
(0.00)
DAX-CAC
31
64
6
35
(0.24)
(0.00)
(0.35)
(0.00)
UKX-SPX
27
57
6
30
(0.08)
(0.00)
(0.35)
(0.00)
UKX-CAC
31
60
10
30
(0.24)
(0.00)
(0.13)
(0.00)
SPX-CAC
23
56
6
28
(0.02)
(0.00)
(0.35)
(0.00)

Bivariate Copula Functions
87
the lower bound VaRM does not correspond to the maximum copula, i.e. to the case in
which portfolio returns are comonotone, even if no hedging is possible in this case.
The following numerical example is provided in Luciano and Marena (2002a,b): they con-
sider the time series of daily closing prices of MIB 30, DAX, UKX, SPX, CAC, NKY, from
December 30, 1994, to April 20, 2000. They compute the marginal empirical distributions
and fit to the data both an Extreme Value Theory distribution13 and a Student’s t distribution.
For each couple of indices, and assuming an equally weighted portfolio, S = 0.5X + 0.5Y,
they evaluate the 95% daily VaR bounds corresponding to the three different choices for
the marginals, using the numerical procedure in Williamson and Downs (1990). The results
are collected in Figure 2.9.
They also compare the appropriateness of the lower bound with respect to that of the
VaR obtained under the so-called normal approach, i.e. assuming both the marginal and
joint return distribution to be normal (by estimating the mean, variances and covariances
of the indices). In order to assess the appropriateness, they perform backtesting of the
VaR, both at the 95% and 99% loc. In turn, backtesting consists in computing the number
of loss exceedances with respect to the VaR and in comparing it with its expectation: a
number of actual exceedances smaller than the expected one signals an overconservative
VaR, while a number greater than the expected one signals an overoptimistic VaR. The
results of the comparison are presented in Table 2.5 and show that the lower bound is not
as overconservative as one could fear, while the normal VaR is excessively overoptimistic.
2.8
APPENDIX
This appendix collects the proofs of the theorems in this chapter (as for corollaries, only
the corollary to Sklar’s theorem is demonstrated).
Proof of Theorem 2.1
We demonstrate the property with reference to the first argument,
v. More precisely, we show that v1 ⩽v2 implies G(v1, x) ⩽G(v2, x) for every x in A2.
From (2.1), the 2-increasing property of G, rearranging, gives
G (v2, z1) −G (v1, z1) ⩽G (v2, z2) −G (v1, z2)
for every z2 ⩾z1, i.e. the difference G(v2, x) −G(v1, x) is a non-decreasing function of x.
In particular,
G(v2, a2) −G(v1, a2) ⩽G(v2, x) −G(v1, x)
(2.37)
for every x ⩾a2. Since G(v1, a2) = G(v2, a2) = 0, one gets G(v1, x) ⩽G(v2, x) for every
x in A2, as needed.
□
Proof of Theorem 2.2
We demonstrate that for every couple of points (v1, z1), (v2, z2)
in A × B, with v1 ⋚v2, z1 ⋚z2
|C (v2, z2) −C (v1, z1)| ⩽|v2 −v1| + |z2 −z1|
(2.38)
13 See, for instance, Embrechts, Kl¨uppenberg and Mikosch (1997).

88
Copula Methods in Finance
Starting from the difference on the l.h.s., subtracting and adding C (v1, z2), and applying
a basic property of absolute values, we have:
|C (v2, z2) −C (v1, z1)| ⩽|C (v2, z2) −C (v1, z2)| + |C (v1, z2) −C (v1, z1)|
(2.39)
If v1 ⩽v2, it follows from Theorem 2.1 that C (v2, z2) −C (v1, z2) ⩾0, and from the 2-
increasing property, applied to the rectangle [v1, v2] × [z2, 1], that
C (v2, 1) −C (v2, z2) −C (v1, 1) + C (v1, z2) ⩾0
i.e.14
C (v2, z2) −C (v1, z2) ⩽C (v2, 1) −C (v1, 1) = v2 −v1
For the same reasons, when v1 > v2, we have
C (v2, z2) −C (v1, z2) ⩽0
C (v2, z2) −C (v1, z2) ⩾C (v2, 1) −C (v1, 1) = v2 −v1
Putting together the two cases:
|C (v2, z2) −C (v1, z2)| ⩽|v2 −v1|
An analogous reasoning yields
|C (v1, z2) −C (v1, z1)| ⩽|z2 −z1|
Substituting in (2.39) one gets (2.38).
□
Proof of Theorem 2.3
Existence follows from the fact that
∂C(x, k)
∂v
= W ′
k(x),
∂C(K,x)
∂z
= V ′
K(x)
In turn, the sections are differentiables almost everywhere because they are monotone
(non-decreasing). As for the values taken by the partial derivatives, consider ∂C/∂v. The
incremental ratio of W at x is
Wk(x + h) −Wk(x)
h
= C(x + h, k) −C(x, k)
h
which, by uniform continuity, is not greater than one in absolute value. It follows that
W ′
k(x)
 ⩽1. In addition, W ′
k(x) ⩾0 by monotonicity: as a consequence, W ′
k(x) ∈I.
□
14 As in the proof of Theorem 2.1, we are using the fact that, when v1 ⩽v2, C (v2, z2) −C (v1, z2) is a non-
decreasing function of z2.

Bivariate Copula Functions
89
Proof of Theorem 2.4
L.h.s.: from the 2-increasing property, C(v2, z2) −C(v2, z1) −
C(v1, z2) + C(v1, z1) ⩾0,
choosing
v2 = z2 = 1,
we
get
1 −C(1, z1) −C(v1, 1) +
C(v1, z1) ⩾0, or 1 −z1 −v1 ⩾−C(v1, z1), which, being valid for every (v1, z1) in A × B,
can be rewritten as C(v, z) ⩾v + z −1. Since at the same time Corollary 2.1 holds, we have
the l.h.s. of the inequality. R.h.s.: it follows from property (ii) of the subcopula definition
and Theorem 2.1, as applied to both arguments of C.
□
Proof of Theorem 2.5 (Sklar’s Theorem)
We
present
a
(partial)
proof,
following
Schweizer and Sklar (1983). The proof is partial since we do not demonstrate an extension
lemma, which is used in it.
An inequality for distribution functions involving their margins is used in the proof
of Sklar’s theorem. It is the second of the following lemmas, that concern grounded, 2-
increasing functions with margins. The margins in turn are defined as follows:
Definition 2.14
The margins of a function G: A1 × A2 →ℜare the functions G1(x):
A1 →ℜ, defined as
G1(x) = G(x, a2)
and G2(y): A2 →ℜ, defined as
G2(y) = G(a1, y)
where ai is the maximal element of Ai.
Evidently, marginal distribution functions of r.v.s are margins according to the previous
definition.
Lemmas 2.1 and 2.2 apply.
Lemma 2.1
A function G: A1 × A2 →ℜgrounded, 2-increasing, with margins G1 and
G2, is such that
|G (v2, z) −G (v1, z)| ⩽|G1(v2) −G1(v1)|
for every couple of points (v2, z), (v1, z) belonging to Dom G,
|G (v, z2) −G (v, z1)| ⩽|G2(z2) −G2(z1)|
for every couple of points (v, z2), (v, z1) belonging to Dom G.
Proof of Lemma 2.1
Consider first the case v2 > v1. Apply the 2-increasing property to
the rectangle [v1, v2] × [z, a2]
G (v2, a2) −G (v1, a2) −G(v2, z) + G(v1, z) ⩾0
By the definition of marginals, G (v2, a2) = G1(v2) and G (v1, a2) = G1(v1) and the pre-
vious inequality can be transformed into
G (v2, z) −G (v1, z) ⩽G1(v2) −G1(v1)

90
Copula Methods in Finance
In turn, by the non-decreasing property of G and G1, this is equivalent to
|G (v2, z) −G (v1, z)| ⩽|G1(v2) −G1(v1)|
If v2 < v1, the 2-increasing property entails
G (v1, z) −G (v2, z) ⩽G1(v2) −G1(v1)
or
|G (v2, z) −G (v1, z)| ⩽|G1(v2) −G1(v1)|
The two cases together give the first statement in the lemma. Analogously for the second
assertion.
□
Lemma 2.2
For the function G of the previous lemma,
|G(v1, z1) −G(v2, z2)| ⩽|G1(v1) −G1(v2)| + |G2(z1) −G2(z2)|
for every (v1, z1), (v2, z2) ∈Dom G.
Proof of Lemma 2.2
It is sufficient to apply the previous lemma twice:
|G(v2, z2) −G(v1, z1)| ⩽|G(v2, z2) −G(v2, z1)| + |G(v2, z1) −G(v1, z1)|
⩽|G1(v1) −G1(v2)| + |G2(z1) −G2(z2)|
□
Using the previous lemmas, we can proceed to the proof of Sklar’s theorem.
Proof of part (i)
Let us demonstrate that, if Ran F1 ⊂A, Ran F2 ⊂B, the function F(x, y)
defined by
F(x, y) = C(F1(x), F2(y))
• is a joint distribution function
• has margins F1, F2
As for the first assertion, let us check that
(1) Dom F = ℜ∗2
(2) F is 2-increasing
(3) F is grounded
(4) F(+∞, +∞) = 1

Bivariate Copula Functions
91
Point (1) follows from the fact that Dom Fi = ℜ∗, i = 1, 2; Ran F1 ⊂A; Ran F2 ⊂B.
Point (2) follows from the fact that C is 2-increasing, F1 and F2 are non-decreasing.
Point (3) is a consequence of the fact that
F(−∞, y) = C(0, F2(y)) = 0
F(x, −∞) = C(F1(x), 0) = 0
which in turn depends on F1 and F2 being marginal distribution functions and C being
grounded.
Point (4) depends on property (ii) in the subcopula definition, which entails F(+∞, +∞) =
C(1, 1) = 1.
As for the second assertion, let us check that the first margin of F, F(x, +∞), is actually
the marginal distribution function F1(x): since F(x, +∞) = C(F1(x), 1) and property (ii)
in the subcopula definition holds, F(x, +∞) = F1(x). Analogously for the second margin.
Proof of part (ii)
This requires the following lemma, which guarantees that every subcop-
ula can be extended to a copula. The proof is in Schweizer and Sklar (1974).
Lemma 2.3 (Sklar, 1973)
Given any subcopula, there exists a copula C such that
C(v, z) = C(v, z)
for every (v, z) ∈Dom C.
Given the lemma, we can now proceed to:
Proof of part (ii)
Consider a joint distribution function F(x, y) with margins F1 and F2
and two points (x1, y1), (x2, y2) ∈ℜ∗2. Suppose that
F1(x1) = F1(x2),
F2(y1) = F2(y2)
Then F(x, y) has the same value at the points (x1, y1), (x2, y2), since, by Lemma 2.2,
|F(x1, y1) −F(x2, y2)| ⩽|F1(x1) −F1(x2)| + |F2(y1) −F2(y2)| = 0
Then, for every point (x, y), the value of F depends on F1(x), F2(y) only: otherwise stated,
there is a unique function C, with Dom C = Ran F1 × Ran F2, such that
F(x, y) = C(F1(x), F2(y))
The function under examination is a subcopula, since, on Ran F1 × Ran F2,
(i) it is grounded:
C(0, F2(y)) = C(F1(−∞), F2(y)) = F(−∞, y) = 0
C(F1(x), 0) = C(F1(x), F2(−∞)) = F(x, −∞) = 0

92
Copula Methods in Finance
(ii) it has margins that are the identity function:
C(1, F2(y)) = C(F1(+∞), F2(y)) = F(+∞, y) = F2(y)
C(F1(x), 1) = C(F1(x), F2(+∞)) = F(x, +∞) = F1(x)
(iii) it is 2-increasing, as a consequence of the analogous property of distribution functions.
If F1(x), F2(y) are continuous, Dom C = I 2 and the subcopula is a copula. Otherwise,
Sklar’s lemma applies.
□
Proof of Corollary 2.3
Consider the subcopula in part (ii) of Sklar’s theorem and denote
the value of F1(x) as v, and the value of F2(y) as z. Since F1 and F2 are margins of a
distribution function, they are marginal distribution functions and therefore admit generalized
inverses: x = F −1
1 (v), y = F −1
2 (z). Then
F(x, y) = F

F −1
1 (v), F −1
2 (z)

C(F1(x), F2(y)) = C(v, z)
Substituting into (2.6) we obtain the statement of the corollary.
□
Proof of Theorem 2.6
(1) →(2) Notice that
Pr(X ⩽x, Y ⩽y) = Pr((X, Y) ∈A1 ∩A2)
(2.40)
where
A1 : = {(s, t) ∈A : s ⩽x}
A2 : = {(s, t) ∈A : t ⩽y}
The comonotonicity property of the support entails that either A1 ⊂A2, so that A1 ∩A2 =
A1 and the probability in (2.40) is F1(x), or A1 ⊃A2, so that A1 ∩A2 = A2 and the
probability in (2.40) is F2(y). In the first case F1(x) ⩽F2(y), in the second the opposite
inequality holds. Property (2) follows.
(2) →(3) From Sklar’s theorem.
(3) →(4) We want to show that
F(x, y) = C(F1(x), F2(y)) = min(F1(x), F2(y))
implies
F(x, y) = Pr(F −1
1 (U) ⩽x, F −1
2 (U) ⩽y)
The latter in fact is
Pr(U ⩽F1(x), U ⩽F2(y)) = Pr(U ⩽min(F1(x), F2(y)))
= min(F1(x), F2(y))

Bivariate Copula Functions
93
(4) →(5) Since X = F −1
1 (U), U = F1(X). Substituting into Y = F −1
2 (U), we have
Y = F −1
2 (F1(X)). Conversely, since Y = F −1
2 (U), U = F2(Y) and X = F −1
1 (F2(X)).
(5) →(1) The set of possible outcomes, under (6), is

(x, F −1
2 (F1(x))) : x ∈ℜ∗
Since both F1 and F2 are marginal distributions, they are non-decreasing: as a consequence,
both the above set and the couple (X, Y) are comonotonic.
□
An analogous technique applies to the proof of Theorem 2.7.
Proof of Theorem 2.8
Denote with ˘C the copula of α1(X), α2(Y). We are going to show
that
˘C(v, z) = C(v, z)
for every (v, z) in ℜ∗2. For fixed (v, z), take (x, y) such that v = F1(x), z = F2(y). Then
C(v, z) = C(F1(x), F2(y))
= F(x, y) = Pr (X ⩽x, Y ⩽y)
= Pr (α1 (X) ⩽α1 (x) , α2 (Y) ⩽α2 (y)) = H(α1 (x) , α2 (y))
= ˘C (H1 (α1 (x)) , H2 (α2 (y))) = ˘C (F1(x), F2(y)) = ˘C(v, z)
This, together with surjectivity of F1, F2, which in turn follows from their continuity, proves
the theorem.
□
The proof of Theorem 2.9 is analogous to the proof of Sklar’s theorem.
The proof of Theorem 2.10 requires the following lemma:
Lemma 2.4
The functions
∂C(v, z)
∂v
: I →I,
∂C(v, z)
∂z
: I →I
are non-decreasing a.e. in the interior of I.
Proof of Lemma 2.4
The derivatives exist by Theorem 2.3; their non-decreasing behavior
follows from the fact, exploited above, that, if v1 ⩽v2, C (v2, z) −C (v1, z) is a non-
decreasing function of z. This means that
∂(C (v2, z) −C (v1, z))
∂z
is non-negative a.e., i.e. ∂C (v2, z) /∂z ⩾C (v1, z) /∂z when v1 ⩽v2, or ∂C/∂z is non-
decreasing a.e. in v (symmetrically for z).
□
Proof of Theorem 2.10
Since non-decreasing functions such as ∂C/∂v and ∂C/∂z are
differentiable a.e., the density exists. Since the partial derivatives are non-decreasing,
c ⩾0.
□


3
Market Comovements and Copula Families
This chapter discusses first the relationships between copula functions and association
measures for couples of random variates, i.e. for financial applications, market indicators
such as prices or returns. It then presents some well-known parametric families (or classes)
of copula functions, for which the parameter value is directly related to one or more asso-
ciation measures. Due to their utility for financial applications – to be fully discussed after
the estimation problem has been addressed (Chapter 5) – we present the following copula
families: the Gaussian, the Student’s t, the Fr´echet, the Archimedean, the Marshall–Olkin.
3.1
MEASURES OF ASSOCIATION
Generally speaking, the random variates X and Y are said to be associated when they are
not independent according to the characterization in section 2.4 of Chapter 2. However,
there are a number of concepts of association. In the sequel, we will present some of these
concepts, namely:
• concordance (as distinct from dependence), linear correlation, tail dependence, positive
quadrant dependency
and some measures associated with them:
• Kendall’s tau, Spearman’s rho, the linear correlation coefficient, the indices of tail depen-
dency.
All these measures are related to copulas since, in coupling a joint distribution function
with its marginals, the copula “captures certain . . . aspects of the relationship between the
variates, from which it follows that (. . .) dependence concepts are properties of the copula”
(Nelsen, 1991). As mentioned above, the same applies because of copula invariance with
respect to increasing transformations.
From now on we will assume that X and Y are continuous.
3.1.1
Concordance
Concordance concepts, loosely speaking, aim at capturing the fact that the probability of
having “large” (or “small”) values of both X and Y is high, while the probability of having
“large” values of X together with “small” values of Y – or vice versa – is low.
Geometrically, it looks at the probability mass associated with the upper and lower quad-
rants, as opposite to the one associated with the rest of the plane (x, y).
Formally, a measure of concordance between the r.v.s X and Y, with copula C, may be
denoted by MX,Y or MC. It is characterized by the following set of axiomatic properties
(Scarsini, 1984):

96
Copula Methods in Finance
Definition 3.1
MX,Y = MC is a measure of concordance between the r.v.s X and Y – with
copula C – iff
(i) it is defined for every pair of r.v.s (completeness)
(ii) it is a relative (or normalized) measure: MX,Y ∈[−1, 1]
(iii) it is symmetric: MX,Y = MY,X
(iv) if X and Y are independent, then MX,Y = 0
(v) M−X,Y = MX,−Y = −MY,X
(vi) it converges when the copula (pointwise)1 does: if {(Xn, Yn)} is a sequence of contin-
uous r.v.s with copula Cn, and
lim
n→+∞Cn(v, z) = C(v, z)
for every (v, z) ∈I 2
then
lim
n→+∞MXn,Yn = MX,Y
(vii) it respects concordance order: if C1 ≺C2, then MC1 ⩽MC2
This definition implies invariance with respect to increasing transformations and the exis-
tence of bounds for M in correspondence to comonotonicity and countermonotonicity.
Theorem 3.1
If αi, i = 1, 2, are a.s. increasing functions on Ran Fi, then MX,Y =
Mα1(X),α2(Y).
Theorem 3.2
If X and Y are comonotone, MX,Y = 1; if they are countermonotone,
MX,Y = −1.
Scarsini (1984) also proved that the following representation holds:
Theorem 3.3
Given a bounded, weakly monotone, odd function f , with Dom f =

−1
2, 1
2

,
then
k

I2 f (v −1
2)f (z −1
2) dC(v, z)
(3.1)
where k−1 =

I f 2(u −1
2) du, is a concordance measure.
By specifying the function f , some very well-known measures of concordance can be
obtained. For f (u) = u one obtains Spearman’s ρS, defined in the sequel; for f (u) = sgn (u)
Blomqvist’s β, which is defined as
q = 4C( 1
2, 1
2) −1
(3.2)
Other popular concordance measures cannot be obtained from the above representation: this
is the case of Kendall’s τ, which will be discussed in the next section, or Gini’s coefficient
1 Please note that for bivariate copula functions, pointwise and uniform convergence coincide, due to uniform
continuity.

Market Comovements and Copula Families
97
γ , defined as
γ = 2

I2(|v + z −1| −|v −z|) dC(v, z)
(3.3)
It is interesting to notice that concordance measures have two features:
• Independency is a sufficient, but not a necessary condition for them to be equal to zero.
• They are distinct from dependence measures, as defined by R´enyi (1959). Opposite to
the former, the latter assume their minimum value when X and Y are independent, not
when they are countermonotonic.
3.1.2
Kendall’s τ
In this section we define Kendall’s coefficient, first introduced – according to Nelsen (1991) –
by Fechner around 1900, and rediscovered by Kendall (1938). We then interpret it, remark that
it is a normalized expected value and give an alternative method to compute it for absolutely
continuous copulas. Examples of computation, together with a discussion and some examples
of estimation, conclude the section.
Definition 3.2
Kendall’s tau for the r.v.s X and Y with copula C, denoted as τ or τC, is:
τ = 4

I2 C(v, z) dC(v, z) −1
(3.4)
One can demonstrate that it measures the difference between the probability of con-
cordance and the one of discordance for two independent random vectors, (X1, Y1) and
(X2, Y2), each with the same joint distribution function F and copula C. The vectors are
said to be concordant if X1 > X2 whenever Y1 > Y2, and X1 < X2 whenever Y1 < Y2; and
discordant in the opposite case.2 We have
Theorem 3.4
Given (X1, Y1) and (X2, Y2) i.i.d. with copula C,
τ = Pr((X1 −X2)(Y1 −Y2) > 0) −Pr((X1 −X2)(Y1 −Y2) < 0)
(3.5)
We refer the reader to Scarsini (1984) for a proof of the fact that Kendall’s τ satisfies
axioms (i) to (vii) for a concordance measure. We stress only the fact that −1 ⩽τ ⩽1, and
if we consider continuous random variables, the lower bound applies to countermonotonic
r.v.s only, while the upper one applies to comonotonic ones only:
τ = −1
iff C = C−
τ = 1
iff C = C+
2 In turn, the idea of using the concordance and discordance probabilities comes from the fact that probabilities of
events involving only inequality relationships between two random variables are invariant with respect to increasing
transformations. Measures based on these probabilities are then expected to satisfy axiom (vii) in the definition of
measures of concordance.

98
Copula Methods in Finance
Remark 3.1
One can also couple Theorem 3.2 with the fact that the double integral in
the definition of τ is the expected value of the function C(U1, U2), where both U1 and U2
are standard uniform and have joint distribution C:
τ = 4E [C(U1, U2)] −1
It follows that
−1 ⩽4E [C(U1, U2)] −1 ⩽1
i.e. that Kendall’s coefficient is a normalized expected value.
When the copula is absolutely continuous, the differential
dC = ∂2C
∂v∂z dv dz
can be substituted into the definition of τ (equation 3.4), in order to compute it. However,
when C has both an absolutely continuous and a singular component, or is singular, the
following theorem holds.
Theorem 3.5
Kendall’s τ can be computed as:
τ = 1 −4

I2
∂C(v, z)
∂v
∂C(v, z)
∂z
dv dz
(3.6)
The equivalence of (3.4) and (3.6) follows from the following lemma (Nelsen, 1991):
Lemma 3.1
If C is a copula

I2 C(v, z) dC(v, z) +

I2
∂C(v, z)
∂v
∂C(v, z)
∂z
dv dz = 1
2
Example 3.1
Consider the product copula, for which we know from Example 2.14 that
∂2C⊥
∂v ∂z = 1
It follows, according to the definition, that
τC⊥= 4

I2 vz dv dz −1 = 0
Example 3.2
Consider the Marshall–Olkin copula defined in section 2.5.1, which is not
absolutely continuous. Its partial derivatives exist whenever vm ̸= zn and
∂CMO(v, z)
∂v
∂CMO(v, z)
∂z
=
 (1 −m)v1−2mz,
vm ⩾zn
(1 −n)vz1−2n,
vm < zn

Market Comovements and Copula Families
99
Therefore, one can compute

I2
∂C(v, z)
∂v
∂C(v, z)
∂z
dv dz = 1
4 (1 −µ)
and
τCMO = µ
which is the measure of the copula singular component.
It is easy to demonstrate, using (3.6), that
Theorem 3.6
The Kendall’s τ of a copula and of its associated survival copula coincide:
τC = τC
In order to estimate τ from a random sample of n pairs
(Xi, Yi)
i = 1, . . . , n, having defined the indicator variables
Aij ≡sgn (Xi −Xj)(Yi −Yj)
as in Gibbons (1992), one can notice that
E(Aij) = (+1) Pr((Xi −Xj)(Yi −Yj) > 0) + (−1) Pr((Xi −Xj)(Yi −Yj) < 0) = τ
It follows that an unbiased estimator of Kendall’s coefficient is the so-called Kendall’s
sample τ:
2
n(n −1)
n

i=1

j>i
Aij
(3.7)
The estimator can be demonstrated to be consistent too.
An application: Kendall’s tau estimation for some financial indices and an FX rate
Let us consider3 the time series of five assets, namely two stock indices (DAX 30 and S&P
500), two bond indices (the 10-year total return index for the German bond market and
the corresponding index for the US market, GER10y and USA10y respectively) and one
exchange rate, the DEM/USD. Namely, let us consider the weekly average data on their
returns from January 1992 to June 2001, for a total of n = 248 observations. These data,
which will be discussed and further used in Chapter 5 in order to illustrate the estimation
methods for copulas, permit us to estimate Kendall’s coefficient between the corresponding
indices, using (3.7). The values obtained are given in Table 3.1.
3 See Cazzulani, Meneguzzo and Vecchiato (2001).

100
Copula Methods in Finance
Table 3.1
Sample Kendall’s tau for selected assets, 01/92 to 06/01, weekly (average) data
DAX 30
S&P 500
GER10y
USA10y
DEM/USD
DAX 30
S&P 500
0.44
GER10y
0.13
0.12
USA10y
0.03
0.14
0.35
DEM/USD
0.22
0.13
0.05
−0.11
3.1.3
Spearman’s ρS
In this section we define the Spearman coefficient, first proposed – according to Nelsen
(1991) – in 1904. In analogy with what we did with Kendall’s τ, we interpret the coefficient,
remark that it is a normalized expected value and that it represents rank correlation. Examples
of computation, together with a discussion and some examples of estimation, follow. A
comment on the relationship between Kendall’s τ and Spearman’s ρS concludes the section.
Definition 3.3
Spearman’s rho for r.v.s X and Y with copula C – denoted as ρS or
ρSC – is:
ρS = 12

I2 C(v, z) dv dz −3 = 12

I2 vz dC(v, z) −3
(3.8)
This measure also exploits probabilities of concordance and discordance. It starts from
three couples of i.i.d. random vectors, namely (X1, Y1), (X2, Y2) and (X3, Y3), with copula
C. It is a multiple (because of normalization) of the difference between the probability of
concordance and discordance for the vectors (X1, Y1), (X2, Y3), the latter being made up of
independent r.v.s. Therefore, in the ρS case the probabilities of concordance and discordance
are measured w.r.t. the independence case. We have:
Theorem 3.7
Given (X1, Y1), (X2, Y2), (X3, Y3), i.i.d. with copula C, then
ρS = 3 [Pr ((X1 −X2) (Y1 −Y3) > 0) −Pr ((X1 −X2) (Y1 −Y3) < 0)]
(3.9)
Substituting in the first definition, one can also write
ρSC = 12

I2 [C(v, z) −vz] dv dz
Remark 3.2
Since the integral transforms U1 = F1(X), U2 = F2(Y) are standard uniform,
with joint distribution function C, the integral in the second form of Spearman’s ρS Defi-
nition 3.3 is E [U1U2]. As a consequence
ρS = 12E [U1U2] −3 = E [U1U2] −1
4
1/12
Since 1
2 and
1
12 are the mean and variance of standard uniforms, it follows that
ρS =
cov (F1(X), F2(Y))
√var(F1(X))var(F2(Y))
(3.10)

Market Comovements and Copula Families
101
We will define below such a ratio as the linear correlation coefficient between F1(X) and
F2(Y): Spearman’s ρS is therefore the rank correlation, in the sense of correlation of the
integral transforms, of X and Y.
Also for Spearman’s ρS one could demonstrate that it satisfies the definition of concor-
dance measure and that it reaches its bounds iff X and Y are respectively countermonotonic
and comonotonic continuous random variates:
ρS = −1
iff C = C−
ρS = 1
iff C = C+
As for computation, both the first and second formulas in Definition 3.3 can be fruitfully
applied.
Example 3.3
Using the first or the second part of the definition, it is straightforward to
show that Spearman’s rho for the product copula is equal to zero:
ρSC⊥= 12

I2 vz dv dz −3 = 0
Example 3.4
In the Marshall–Olkin case, since

I2 CMO(v, z) dv dz = 1
2
m + n
2m + 2n −mn
we have
ρSCMO = 3
mn
2m + 2n −mn
It is easy to demonstrate, using the definition, that
Theorem 3.8
Spearman’s ρS of a copula and its associated copula coincide:
ρSC = ρSC
As far as estimation is concerned (see Gibbons, 1992), starting from a random sample of
n pairs
(Xi, Yi)
i = 1, . . . , n, and recalling that ρS is the rank correlation, according to (3.10), one can
switch to the ranks of the sample variates:
Ri ≡rank(Xi),
Si ≡rank(Yi)
where the ranking has to be done in ascending order. By so doing, the following Spearman’s
sample ρS can be obtained:
n
i=1(Ri −R)(Si −S)
n
i=1(Ri −R)2 n
i=1(Si −S)2

102
Copula Methods in Finance
Taking into consideration the fact that the ranks of n data are the first n integer numbers,
the above expression simplifies into either
12
n
i=1(Ri −R)(Si −S)
n(n2 −1)
or
1 −6
n
i=1(Ri −Si)2
n(n2 −1)
(3.11)
which has to be slightly modified, in applications, in order to take into account tied obser-
vations. The sample version of ρS so obtained is an unbiased estimator of the population
one.
An application: Spearman’s rho estimation for some financial indices and an FX rate
Using the same data as in the application of section 3.1.2, together with expression (3.11),
the values for the rank correlation coefficient between the financial assets under examination,
over the years 1992–2001, were obtained (see Table 3.2).
Table 3.2
Sample Spearman’s rho for selected assets, 01/92 to 06/01, weekly (average) data
DAX 30
S&P 500
GER10y
USA10y
DEM/USD
DAX 30
−
S&P 500
0.67
−
GER10y
0.20
0.18
−
USA10y
0.04
0.13
0.49
−
DEM/USD
0.31
0.19
0.06
−0.22
−
−1
1
0
−1
0
1
t
Figure 3.1
Spearman’s ρS, as a function of Kendall’s τ, for a given copula

Market Comovements and Copula Families
103
Finally, one could wonder whether there exists a functional relationship between Kendall’s
τ and Spearman’s ρS. Durbin and Stuart (1951) showed that (see Figure 3.1) for a given
association between X and Y, i.e. for a given copula:
	
3
2τ −1
2 ⩽ρS ⩽1
2 + τ −1
2τ 2
τ ⩾0
−1
2 + τ + 1
2τ 2 ⩽ρS ⩽3
2τ + 1
2
τ < 0
3.1.4
Linear correlation
For r.v.s belonging to L2, concordance – in its loose significance – should be captured also
by covariance. Since covariance is not a normalized or relative measure, however, the so-
called Pearson product-moment or linear correlation coefficient has been introduced. We
define it, show that it satisfies some of the axioms for a measure of concordance, and list
five of its properties, which entail that it does not satisfy the remaining axioms. Last, we
mention the estimation procedure and give an example.
In order to define linear correlation, let us denote by var(X) the variance of the r.v. X,
and recall that a non-degenerate random variable has non-null variance.
Definition 3.4
For non-degenerate r.v.s X and Y belonging to L2, the linear correlation
coefficient ρXY is
ρXY =
cov(X, Y)
√var(X)var(Y)
Theorem 3.9
The linear correlation coefficient satisfies axioms (i) to (v) and (vii) of the
concordance measure definition.
Proof :
It is evident that, if we exclude degenerate r.v.s, the linear correlation coefficient
satisfies (i).
Axiom (ii) follows from the fact that |cov(X, Y)| ⩽√var(X)var(Y), while axiom (iii)
depends on the symmetry of covariance, cov(X, Y) = cov(Y, X).
Property (iv) follows from the fact that independence between X and Y implies cov(X, Y)
= 0.
Property (v) is a consequence of the fact that if Y = aX + b a.s., with a ∈ℜ\ {0}, b ∈ℜ,
then |ρXY | = 1 and vice versa.4
As concerns property (vii), one needs Hoeffding’s (1940) expression for covariance:
cov(X, Y) =

D
(F(x, y) −F1(x)F2(y)) dx dy
(3.12)
where D = Dom F1 × Dom F2.
4 Since r2 = {var(Y) −mina,b E[(Y −(aX + b))2]}/var(Y).

104
Copula Methods in Finance
It follows from this and the Fr´echet inequality that, if C1 ≺C2, and we denote as ρ1 and
ρ2 the corresponding linear correlations, then from

D
(C1(F1(x), F2(y)) −F1(x)F2(y)) dx dy
⩽

D
(C2 (F1(x), F2(y)) −F1(x)F2(y)) dx dy
it follows that ρ1 ⩽ρ2.
□
Nonetheless, the correlation coefficient does not satisfy axiom (vi) and therefore is not
a measure of concordance. It satisfies instead the following properties, which entail that it
violates Theorems 3.1 and 3.2.
Property 1
ρXY is invariant under linear increasing transformations, not under (non-linear)
increasing transformations.
Proof :
In order to prove the first fact, consider that
ρaX+b,cY+d = sgn(ac)ρXY
for a, c ∈ℜ\ {0} , b, d ∈ℜ
Linear increasing transforms produce sgn(ac) = 1 and ρaX+b,cY+d = ρXY .
□
In order to show that ρXY is not invariant under increasing, non-linear transforms, consider
the following example:
Example 3.5
Start from two r.v.s X and Y jointly distributed as a bivariate standard
normal, with correlation coefficient ρXY , and take their transforms according to the distri-
bution function of the standard normal , (X) and (Y). Computing the linear correlation
coefficient between (X) and (Y) one gets
ρ(X),(Y) = 6
π arcsin

ρXY
2

(3.13)
In spite of reaching its bounds when X and Y are linear transformations of each other, ρXY
does not necessarily reach its bounds when X and Y are comonotonic or countermonotonic,
without being linearly related. Formally, it has the following property:
Property 2
ρXY is bounded
ρl ⩽ρXY ⩽ρu
where the bounds ρl and ρu are defined as
ρl =

D

C−(F1(x), F2(y)) −F1(x)F2(y)

dx dy

DomF1 (x −EX)2 dF1(x)

DomF2 (y −EY)2 dF2(y)
(3.14)
ρu =

D

C+ (F1(x), F2(y)) −F1(x)F2(y)


DomF1 (x −EX)2 dF1(x)

DomF2 (y −EY)2 dF2(y)
(3.15)
and are attained respectively when X and Y are countermonotonic and comonotonic.

Market Comovements and Copula Families
105
Proof :
The bounds for ρXY can be obtained from Hoeffding’s (1940) expression for
covariance, (3.12) above, together with the Fr´echet inequality:

D

C−(F1(x), F2(y)) −F1(x)F2(y)

dx dy ⩽cov(X, Y)
cov(X, Y) ⩽

D

C+ (F1(x), F2(y)) −F1(x)F2(y)

dx dy
Dividing by the square root of the variances, the bounds are obtained. It is evident that they
are attained when C = C−and C = C+ respectively.
□
Property 3
ρXY for comonotone (countermonotone) random variables can be different
from 1 (−1).
Proof :
In order to show this, let us consider an example of comonotonicity, for which
the linear correlation coefficient is bounded away from 1. Before doing that, remark however
that the bounds in Property 2 depend on margins. The dependence of the bounds for ρXY
on margins can a priori prevent the coefficient from being equal to 1 in absolute value for
any pair of comonotone or countermonotone r.v.s.
□
As for the example, consider the following, due to Wang (1998):
Example 3.6
Let X and Y be two log-normal r.v.s, with parameters
(µX, σX) ,
(µY , σY)
respectively. Computing αl and αu gives respectively:
ρl =
exp (−σXσY ) −1

exp

σ 2
X

−1

 
exp

σ 2
Y

−1

 ⩽0
ρu =
exp (σXσY ) −1

exp

σ 2
X

−1

 
exp

σ 2
Y

−1

 ⩾0
As argued by Georges et al. (2001), the lower bound tends to −1 when max(σX, σY ) →0,
while the upper bound is equal to 1 iff σX = σY . When the two variances are different,
the interval [ρl, ρu] is different from [−1, +1]. Even worse, it may happen that the interval
[ρl, ρu] is very “small”, since
lim
max(σX,σY )→∞
ρl = 0
lim
|σX−σY |→∞
ρu = 0
(3.16)
Example 3.7
To get a feeling of the phenomenon, consider for instance σX = 0.4, σY =
0.6. In this case we get ρl = −0.45, ρu = 0.57. In addition, Figure 3.2 shows the whole
behavior of the bounds, keeping σX fixed at the chosen value, 0.4, and letting σY change.
An application: Stock indices correlation bounds
As an application of the linear correlation bounds concept, consider the following one,
presented in Cherubini and Luciano (2002a). We want to determine the correlation bounds

106
Copula Methods in Finance
−0.6
−0.4
−0.2
0
0.2
0.4
0.6
0.8
0.6
0.5
0.4
0.3
0.2
0.1
lower bound
upper bound
Figure 3.2
Bounds for linear correlation as a function of Y’s volatility, volatility of X = 0.4,
log-normal case
for the risk-neutral 3-month distributions of four stock indices, namely MIB 30, S&P 500,
FTSE, DAX, using the time series of daily closing prices, from January 2, 1999 to March
27, 2000.
We first estimate the risk-neutral marginal distribution of each index using the European
calls closing prices, as given by Bloomberg on March 27, 2000, for contracts with June
expiration and different strikes. In doing this, we follow the approach in Shimko (1993),
which exploits the seminal idea in Breeden and Litzenberger (1978), of reconstructing the
distribution function of an underlying from the derivative of its European call price with
respect to the strike.5 If S is the underlying, with risk-neutral distribution F ∗
S , B(0, t) is
the zero-coupon bond value for maturity t, C(K, t) is the value of the call option on S
with strike K and maturity t, it has been known since Breeden and Litzenberger (1978)
that
F ∗
S (K) = 1 +
1
B(0, t)
∂C(K, t)
∂K
Shimko superimposed on this idea the assumption of (conditionally) log-normal underly-
ings, where the conditioning is done with respect to the volatility, and of quadratic (implied)
volatility function, σ(K) = A0 + A1K + A2K2. By so doing he obtained the following
risk-neutral distribution function FS of the underlying S:
FS(s) = 1 + sφ(D2(s))
√
t(A1 + 2A2s) −(D2(s))
(3.17)
D2(s) = ln(S (0) /B(0, t)s)
σ(s)√t
−1
2σ(s)√t
5 The estimation technique for the marginals can be changed without modifying the bounds’ existence and inter-
pretation.

Market Comovements and Copula Families
107
where φ(·) and (·) are respectively the density and the distribution of the standard normal,
S (0) is the current value of the underlying, less the discounted dividends. We exploit his
idea by first estimating the coefficients A0, A1, A2 so as to minimize the squared differences
between actual and theoretical implied volatility, σ(K), on March 28. In order to obtain the
whole indices’ distributions (3.17) we then use, together with the coefficients so obtained,
data on dividends and 3-month zero-coupon bond values from the same data source, in the
same day. Finally, using the four marginals so obtained, we numerically compute the lower
and upper Fr´echet bounds for the joint distributions, C−and C+ evaluated at the marginal
distribution values. Substituting them in (3.14) and (3.15) we recover the correlation bounds
ρl and ρu in Figure 3.2.
As the readers can notice, these bounds are always of opposite sign but, at least for
the first three pairs of indices, they are far from −1 and 1 respectively. The economic
lesson we learn from the example is that for the Italian stock market, in the period under
consideration, estimated correlation figures greater than (approximately) 0.7 in absolute
value were inconsistent with the volatility smile. At the same time, estimated values close
to (but smaller than) 0.7 were already very close to the maximum theoretical value: they
had to be considered very high indeed, while usually a correlation close to 0.7 is not read
as being very strong.
Recalling Theorems 2.6 and 2.7, we can state that, when ρ = ρl, one index is a decreasing
function of the other, while when ρ = ρu it is an increasing one, and the transformation
functions are given in the aforementioned theorems. Applying and plotting them, for the
case X = DAX, Y = FTSE, we obtain the relationships between the two indices shown in
Figure 3.4, assuming extreme correlation between them.
Property 4
ρXY = 0 does not imply independence between X and Y, unless the latter are
Gaussian.
Proof :
If X and Y are Gaussian, ρXY = 0 implies F(x, y) = F1(x)F2(y). This can be
checked by substituting ρXY = 0 in the Gaussian expression for the joint distribution: as
Figure 3.3
Linear correlation bounds for selected stock indices
1.104
1.104
1.104
5000
5000
5000
1.104
5000
DAX
DAX
lowerF(DAX)
upperF(DAX)
0
0
Figure 3.4
FTSE as a function of DAX, in the extreme correlation cases, lower F(DAX) & upper
F(DAX)

108
Copula Methods in Finance
usual, it is sufficient to prove the result for standardized normal variates. With ρXY = 0,
the distribution of two standard jointly normal variables becomes
F(x, y) =
 x
−∞
 y
−∞
1
2π exp
−s2 −t2
2

ds dt
Since the marginal ones are Fi = , it is easy to see that F(x, y) = F1(x)F2(y).
The same fact, that ρXY = 0 implies F(x, y) = F1(x)F2(y), cannot be demonstrated in
general: at the opposite, there are counterexamples, such as the one in the next property, in
which, in spite of having ρXY = 0, one variable is a.s. a function of the other.
□
Property 5
ρXY = 0 does not mean that one r.v. cannot be almost surely a function of
the other.
Proof :
Nelsen (1999) defines the following copula
C(v, z) =



v
0 ⩽v ⩽z/2 ⩽1
2
z/2
0 ⩽z/2 ⩽v ⩽1 −z/2
v + z −1
1
2 ⩽1 −z/2 ⩽v ⩽1
Given this copula, cov(U1, U2) = 0, but
Pr (U2 = 1 −|2U1 −1|) = 1
The r.v.s U1 and U2 are uncorrelated, but one is a.s. a function of the other.
□
An application: Linear correlation estimation for some financial indices and an FX rate
Using the same data as in the application of section 3.1.2, the values in Table 3.3 were
obtained for the correlation coefficient between the financial assets under examination over
the years 1992–2001.
Table 3.3
Sample Pearson’s linear correlation coefficient for selected assets, 01/92 to 06/01,
weekly (average) data
DAX 30
S&P 500
GER10y
USA10y
DEM/USD
DAX 30
−
S&P 500
0.67
−
GER10y
0.18
0.13
−
USA10y
−0.02
0.13
0.50
−
DEM/USD
0.30
0.14
0.06
−0.21
−
3.1.5
Tail dependence
Loosely said, bivariate tail dependence looks at concordance in the tail, or extreme, values
of X and Y. Geometrically, it concentrates on the upper and lower quadrant tails of the
joint distribution function.
Formally, having defined the joint survival function for uniform variates, C/, we have the
following:

Market Comovements and Copula Families
109
Definition 3.5
Let
lim
v→1−
C/(v, v)
1 −v = λU
exist finite. C is said to have upper tail dependence iff λU ∈(0, 1], no upper tail dependence
iff λU = 0. Analogously, let
lim
v→0+
C(v, v)
v
= λL
exist finite. C is said to have lower tail dependence iff λL ∈(0, 1], no lower tail dependence
iff λL = 0.
In order to capture the correspondence between these definitions and the intuition above,
recall that
C/(v, v) = Pr (U1 > v, U2 > v)
so that the ratio C/(v, v)/(1 −v) is the following conditional probability:
C/(v, v)
1 −v = Pr (U1 > v | U2 > v) = Pr (U2 > v | U1 > v)
Therefore
λU = lim
v→1−Pr (U1 > v | U2 > v) = lim
v→1−Pr (U2 > v | U1 > v)
and similarly for λL.
The value λU represents the limit of the conditional probability that the distribution func-
tion of X exceeds the threshold v, given that the corresponding function for Y does, when
v tends to one (and therefore the r.v.s assume extreme or upper tail values). Analogously
for λL.
Example 3.8
The copula pC+ + (1 −p)C⊥has both upper and lower tail dependency,
since in the upper tail
C/(v, v)
1 −v = 1 −2v + p min(v, v) + (1 −p)v2
1 −v
= 1 −(2 −p) v + (1 −p)v2
1 −v
and therefore
λU = lim
v→1−
C/(v, v)
1 −v = p
In the lower tail
C(v, v)
v
= p min(v, v) + (1 −p)v2
v

110
Copula Methods in Finance
and therefore
λL = lim
v→0+
C(v, v)
v
= p
The tail dependence and its coefficients in turn come from the fact that C+ presents tail
dependency, with both upper and lower index 1, while C⊥(as well as C−) has neither
lower nor upper tail dependency.
We can also introduce the coefficients of tail dependency for the survival copula C:
lim
v→1−
1 −2v + C(v, v)
1 −v
= λU
lim
v→0+
C(v, v)
v
= λL
if these limits are finite. The following property holds trivially:
Theorem 3.10
If C is the survival copula associated with C, then
λU = λL
λL = λU
Proof :
lim
v→1−
1 −2v + C(v, v)
1 −v
= lim
v→1−
C(1 −v, 1 −v)
1 −v
implies λU = λL. Symmetrically
lim
v→0+
C(v, v)
v
= lim
v→0+
2v −1 + C(1 −v, 1 −v)
v
= lim
w→1−
1 −2w + C(w, w)
1 −w
gives λL = λU.
□
3.1.6
Positive quadrant dependency
The concept of positive quadrant dependency (PQD), due to Lehmann (1966), can be
expressed in terms of copulas as follows.
Definition 3.6
The r.v.s X and Y are positive quadrant dependent iff
C(v, z) ⩾vz
for every (v, z) ∈I 2.

Market Comovements and Copula Families
111
Alternatively, using the concordance order between copulas, X and Y are PQD iff their
copula is greater than that of the product:
C ≻C⊥
Example 3.9
R.v.s with the copula pC+ + (1 −p)C⊥, p ∈I, are PQD, since
C+ ≻C⊥
implies
pC+ + (1 −p)C⊥≻C⊥
On the other hand, r.v.s with the copula pC−+ (1 −p)C⊥, p ∈I, are not PQD, since
C−≺C⊥
implies
pC−+ (1 −p)C⊥≺C⊥
In terms of distribution functions, PQD can be formalized as
F(x, y) ⩾F1(x)F2(y)
for every (x, y) ∈ℜ∗2
the joint probability at each point must be not smaller than the independence one.
PQD implies the non-negativity of Kendall’s τ, Spearman’s ρS and of the linear cor-
relation coefficient, since independent random variates, for which C = C⊥, make these
coefficients equal to zero, and the coefficients themselves respect concordance order.
By applying Bayes’ rule the PQD inequality may be rewritten as:
Pr(X ⩽x|Y ⩽y) ⩾Pr(X ⩽x)
(3.18)
Hence, Lehmann’s PQD condition may be strengthened by requiring the conditional
probability to be a non-increasing function of y. This implies that the probability that the
return Xt takes a small value does not increase as the value taken by the other return Yt
increases. This corresponds to a particular monotonicity in the tails.
Analogously, we say that a random variable X is left tail decreasing in Y, denoted by
LTD(X|Y), if
Pr(X ⩽x|Y ⩽y) is a non-decreasing function of y for all x
This, in turn, is equivalent to the condition that, for all v in [0, 1], C(v, z)/z is a non-
decreasing function in z, or:
∂C(v, z)
∂z
⩽C(v, z)
z
for almost all z
(3.19)

112
Copula Methods in Finance
3.2
PARAMETRIC FAMILIES OF BIVARIATE COPULAS
In this section we are going to present several families or classes of copulas. We will call
comprehensive (Devroye, 1986) a copula family which encompasses the minimum, product
and maximum one.
For each family, we give the copula definition and write down the density and condi-
tional distribution via copula. We then discuss the concordance order and comprehensiveness
properties of the family. Each family is characterized by a parameter or a vector of param-
eters. Whenever possible, the relationship between this parameter(s) and the measures of
concordance or tail dependence defined above is clarified.
3.2.1
The bivariate Gaussian copula
Definition 3.7
The Gaussian copula is defined as follows:
CGa(v, z) = ρXY

−1(v), −1(z)

where ρXY is the joint distribution function of a bi-dimensional standard normal vec-
tor, with linear correlation coefficient ρXY ,  is the standard normal distribution function.
Therefore
ρXY

−1(v), −1(z)

=
 −1(v)
−∞
 −1(z)
−∞
1
2π

1 −ρ2
XY
exp

2rXYst −s2 −t2
2

1 −ρ2
XY


ds dt
(3.20)
Since it is parametrized by the linear correlation coefficient, we can also write CGa
ρ . We
have proved that it is actually a copula in Chapter 2 and we represent it and its level curves
in Figure 3.5.
The following representation has been demonstrated by Roncalli (2002) to be equivalent
to (3.20):
CGa(v, z) =
 v
0



−1(z) −ρXY −1(t)

1 −ρ2
XY

dt
(3.21)
In order to appreciate the effect of different correlation coefficients on the copula values,
let us consider random samples from the Gaussian copula (Figure 3.6): the closer the samples
are to a straight line (the main diagonal or the secondary one) the higher is (in absolute
value) the correlation coefficient. The sign of the coefficient determines the diagonal on
which the samples concentrate.
The density of CGa has been calculated in Chapter 2. By integrating the density, since
the copula is absolutely continuous, the following, equivalent expression for the copula can

Market Comovements and Copula Families
113
1
0.5
0
Figure 3.5
The Gaussian copula, ρ = 0.5
1
0.5
00
0.5
1
1
0.5
00
0.5
1
Figure 3.6
Random samples of (v, z) couples from a Gaussian copula, ρ = 0.5 (right) and ρ = −0.5
(left)
be obtained:
CGa(v, z) =
 v
0
 z
0
1

1 −ρ2
XY
exp

2rXY xy −x2 −y2
2

1 −ρ2
XY

+ x2 + y2
2

ds dt
where x = −1(s), y = −1(t).
As for the conditional distribution via copula, from expression (3.21) one obtains:
CGa
2|1(v, z) = 

−1(z) −ρXY −1(v)

1 −ρ2
XY


The reason why we start by analyzing this copula is that it may generate the Gaussian
bivariate joint distribution function. Specifically, we have the following:
Proposition 3.1
The Gaussian copula generates the joint normal standard distribution func-
tion – via Sklar’s theorem – iff the margins are standard normal.

114
Copula Methods in Finance
Proof :
Consider that
CGa(F1(x), F2(y)) =
 x
−∞
 y
−∞
1
2π

1 −ρ2
XY
exp

2rXYst −s2 −t2
2

1 −ρ2
XY


ds dt
iff −1(F1(x)) = x and −1(F2(y)) = y, that is to say, iff F1 = F2 = .
□
For any other marginal choice, the Gaussian copula does not give a standard jointly normal
vector. In order to have a visual representation of the phenomenon, and more generally of
the effect of “coupling” the same copula with different marginals, let us consider the joint
density functions in the following figures, obtained coupling the Gaussian copula with
standard Gaussian margins (above) and with three Student’s t d.o.f. (below); let us consider
both the case ρ = 0.2 (in Figure 3.7) and ρ = 0.9 (in Figure 3.8).
0.15
0.1
0.05
0.1
0.05
Figure 3.7
Density and level curves of the distribution obtained coupling the Gaussian copula with
standard normal marginals (top) and 3-d.o.f. Student ones (bottom), ρ = 0.2

Market Comovements and Copula Families
115
0.2
0.15
0.1
0.05
0.1
Figure 3.8
Density and level curves of the distribution obtained coupling the Gaussian copula with
standard normal marginals (top) and 3-d.o.f. Student ones (bottom), ρ = 0.9
As expected, both in the positive and in the negative correlation cases, the same copula,
together with different marginals, presents a different joint behavior, here synthesized by
the density. In the specific case, the effect of marginal Student distributions is that of
increasing the tail probabilities. In general, Figures 3.7 and 3.8 provide examples of the
modeling flexibility obtained using copula functions instead of joint distribution functions:
analogous effects could also be obtained by substituting different types of marginals in the
other copulas. We will omit the corresponding diagrams in the next sections, but we strongly
invite the readers to perform the substitutions and obtain the corresponding graphs.
As a consequence of the fact that it is parametrized by the linear correlation coefficient,
which respects concordance order, the Gaussian copula is positively ordered with respect
to the parameter:
CGa
ρ=−1 ≺CGa
ρ<0 ≺CGa
ρ=0 ≺CGa
ρ>0 ≺CGa
ρ=1
Also, it is comprehensive: one in fact can verify that
CGa
ρ=−1 = C−
and
CGa
ρ=1 = C+

116
Copula Methods in Finance
In addition, CGa
ρ=0 = C⊥. As for the measures of dependence, one can show, using the
definition of Kendall’s τ and Spearman’s ρS, that
τ = 2
π arcsin ρ
and
ρS = 6
π arcsin ρ
2
As for other types of dependence, it can be shown that Gaussian copulas have neither
upper nor lower tail dependence, unless ρ = 1:
λU = λL =
 0
iff ρ < 1
1
iff ρ = 1
They present PQD if ρ ⩾0.
3.2.2
The bivariate Student’s t copula
Let tυ : ℜ→ℜbe the (central) univariate Student’s t distribution function, with υ degrees
of freedom (d.o.f.)6:
tυ(x) =
 x
−∞

 ((υ + 1)/2))
√πυ
 (υ/2)

1 + s2
υ
−υ+1
2
ds
where 
 is the usual Euler function. Let ρ ∈I and tρ,υ the bivariate distribution corre-
sponding to tυ:
tρ,υ(x, y) =
 x
−∞
 y
−∞
1
2π

1 −ρ2

1 + s2 + t2 −2ρst
υ

1 −ρ2
−υ+2
2
ds dt
Definition 3.8
The bivariate Student’s copula, Tρ,υ, is defined as
Tρ,υ(v, z) = tρ,υ

t−1
υ (v), t−1
υ (z)

=
 t−1
υ (v)
−∞
 t−1
υ (z)
−∞
1
2π

1 −ρ2

1 + s2 + t2 −2ρst
υ

1 −ρ2
−υ+2
2
ds dt
When the number of degrees of freedom diverges, the copula converges to the Gaussian one.
For a limited number of degrees of freedom, however, the behavior of the two copulas is
quite different, as the readers can appreciate comparing Figure 3.9, which presents random
extractions from a 3-d.o.f. Student’s copula, with the corresponding picture for the Gaussian
copula (Figure 3.6). It is easy to remark that the Student copula presents more observations
in the tails than the Gaussian one. Please notice also that this effect precedes the one
exemplified by Figures 3.7 and 3.8, in which the different joint behavior was obtained – with
the same copula – by changing the marginals. In concrete applications, both the copula and
the marginal choice will be allowed, in sequential order.
6 All odd moments of the distribution are zero due to symmetry; while the second moment exists if υ > 2 and it
is equal to υ/(υ −2); the fourth moment exists if υ > 4 and its kurtosis is given by 3 (υ −2) / (υ −4).

Market Comovements and Copula Families
117
0.5
00
0.5
1
1
0.5
00
0.5
1
1
Figure 3.9
Random samples of (v, z) couples from a Student copula, ρ = 0.5 (right) and ρ = −0.5
(left), υ = 3
1
0.75
0.5
0.25
0
1
1
1
1
200
100
0
Figure 3.10
The Student copula (left) and its density (right), ρ = 0.5, υ = 3
The Student’s copula density is:
cS
υ,ρ(v, z) = ρ−1
2


υ+2
2


 υ
2



υ+1
2
2

1 + ς2
1 +ς2
2 −2ρς1ς2
υ(1−ρ2)
−(υ+2)/2
2
j=1

1 +
ς2
j
υ
−(υ+2)/2
where ς1 = t−1
υ (v), ς2 = t−1
υ (z), and the copula itself is absolutely continuous.
Since, as recalled by Roncalli (2002), given a couple of r.v.s (X, Y), jointly distributed
as a Student’s t, the conditional distribution of

υ + 1
υ + x2
Y −ρx

1 −ρ2
given X = x, is a Student’s t with υ + 1 degrees of freedom, the conditional distribution
via copula CS
2|1υ,ρ(v, z) is
CS
2|1υ,ρ(v, z) = tυ+1

υ + 1
υ + t−1
υ (v)2
t−1
υ (z) −ρt−1
υ (v)

1 −ρ2


118
Copula Methods in Finance
It follows that an equivalent expression for the bivariate Student’s copula is
Tρ,υ(v, z) =
 v
0
tυ+1

υ + 1
υ + t−1
υ (s)2
t−1
υ (z) −ρt−1
υ (s)

1 −ρ2

ds
If υ > 2, each margin admits a (finite) variance, υ/(υ −2), and ρXY can be interpreted as a
linear correlation coefficient. The Student’s copula is positively ordered w.r.t. ρ, for given
degrees of freedom. It also reaches the lower and upper bound, since
CS
υ,−1 = C−
and
CS
υ,1 = C+
Nonetheless, CS
υ,0 ̸= C⊥for finite υ.
As for tail dependency, for finite υ
λU = λL =
 > 0
iff ρ > −1
0
iff ρ = 1
3.2.3
The Fr´echet family
Definition 3.9
Fr´echet (1958) introduced the following two-parameter copula family
(Figure 3.11):
CF(v, z) = p max(v + z −1, 0) + (1 −p −q)vz + q min(v, z)
= pC−+ (1 −p −q)C⊥+ qC+
where p, q ∈I, p + q ⩽1.
The Fr´echet copula density is
CF(v, z) = 1 −p −q
It follows that this copula has an absolutely continuous and a singular component, if at least
one between p and q is positive.
0.8
0.6
0.4
0.2
0.0
0.00.4 0.60.8
0.8
1
1
1
Figure 3.11
The Fr´echet copula and its level curves, p = 0.2, q = 0.5

Market Comovements and Copula Families
119
As for the conditional probability via copula, one can easily verify that
CF
2|1(v, z) =



p + (1 −p −q)z + q
v + z −1 > 0,
v < z
p + (1 −p −q)z
v + z −1 > 0,
v > z
(1 −p −q)z
v + z −1 < 0,
v > z
(1 −p −q)z + q
v + z −1 < 0,
v < z
The Fr´echet class is positively ordered with respect to q and negatively ordered with respect
to p.
The class is comprehensive, since for p = 1, q = 0 it gives the Fr´echet lower bound
C−, for p = 0, q = 1 it gives the upper, C+, for p = q = 0 it collapses into the product
copula C⊥.
The relationship between the parameters of the Fr´echet class and the concordance mea-
sures introduced above is (Nelsen, 1991):
τ = (q −p) (2 + p + q)
3
ρS = q −p
which implies
τ ⩽ρS ⩽−1 +
√
1 + 3τ
when τ ⩾0
1 −
√
1 −3τ ⩽ρS ⩽τ
when τ < 0
These bounds are stricter than those holding in general between τ and ρS.
In Figure 3.12 we depict the relationship between τ and ρS for the Fr´echet family, together
with the general one, already presented in Figure 3.1.
The Fr´echet family reduces to the so-called mixture copula (Li, 2000), when either p or
q are set to zero. In the former case, introduced by Konijn (1959), and presented as family
B11 in Joe (1997)
CM
q (v, z) = (1 −q)vz + q min(v, z) = (1 −q)C⊥+ qC+
−1
0
1
−1
0
1
t
Figure 3.12
Spearman’s ρS, as a function of Kendall’s τ, for a given copula (external lines) and a
given Spearman’s copula (internal lines)

120
Copula Methods in Finance
while in the second
CM
p (v, z) = (1 −p)vz + p max(v + z −1, 0) = (1 −p)C⊥+ pC−
Opposite to CF, CM
q and CM
p are not comprehensive. Nonetheless, the former includes the
product and upper bound copula, respectively when q = 0 and q = 1. The latter includes
the product and lower bound copula, respectively when p = 0 and p = 1.
As for the relationship between the parameters of the mixture copulas and the concordance
measures, it is sufficient to substitute for p = 0 or q = 0 in the previous relationship: for
positive dependence (p = 0) we have
τ = q (2 + q)
3
and
ρS = q
and therefore
τ = ρS
2 + ρS
3
and
ρS = −1 +
√
1 + 3τ
For negative dependence instead (q = 0)
τ = −p (2 + p)
3
and
ρS = −p
so that
τ = ρS
2 −ρS
3
and
ρS = 1 −
√
1 −3τ
The relationship between τ and ρS, which is “narrowed” in the Fr´echet family, reduces to
a single value in the mixture family. In addition, the mixture copula reaches both the upper
bound for ρS in the Fr´echet copula in the positive case, and the lower bound in the negative
case.
As for tail dependency, it is easy to show that for positive dependence7
λU = λL = q
so that the mixture copula presents tail dependence when q > 0. Symmetrically, it can be
shown that for negative dependence
λU = λL = 0
so that the mixture copula presents no tail dependence in the presence of negative depen-
dence.
3.2.4
Archimedean copulas
The class of Archimedean copulas has been named by Ling (1965), but it was recognized
by Schweizer and Sklar (1961) in the study of t-norms. Before being introduced in Finance,
7 See Example 3.8, where the notation was slightly different.

Market Comovements and Copula Families
121
Archimedean copulas have been applied in the Actuarial field: the idea arose indirectly in
Clayton (1978) and was developed in Oakes (1982), Cook and Johnson (1981). A survey
of Actuarial applications is in Frees and Valdez (1998).
We divide the discussion of Archimedean copulas in three subsections: the first introduces
them and their main properties, the second discusses dependence, the third presents different
one-parameter families of Archimedean copulas. In the case of Archimedean copulas in fact,
it is customary to use the term “class” for all of them, and to reserve “families” for some
particular subclasses.
Definition and basic properties
Archimedean copulas may be constructed using a function φ : I →ℜ∗+, continuous, de-
creasing, convex and such that φ(1) = 0. Such a function φ is called a generator. It is called
a strict generator whenever φ(0) = +∞. The behavior of the φ function is exemplified in
Figure 3.13.
The pseudo-inverse of φ must also be defined, as follows:
φ\[−1\](v) =

φ−1(v)
0 ⩽v ⩽φ(0)
0
φ(0) ⩽v ⩽+∞
This pseudo-inverse is such that, by composition with the generator, it gives the identity,
as ordinary inverses do for functions with domain and range ℜ:
φ\[−1\](φ (v)) = v
for every v ∈I
In addition, it coincides with the usual inverse if φ is a strict generator.
Definition 3.10
Given a generator and its pseudo-inverse, an Archimedean copula CA is
generated as follows:
CA(v, z) = φ[−1] (φ(v) + φ(z))
(3.22)
If the generator is strict, the copula is said to be a strict Archimedean copula.
Let us recall the definition of Laplace transform:
15
10
5
0
0.5
1
1.5
2
Figure 3.13
Generator of the Gumbel copula, α = 1.5

122
Copula Methods in Finance
Definition 3.11
The Laplace transform of a positive random variable γ, with distribution
function Fγ , is defined as:
τ(s) = Eγ

e−sγ 
=
 +∞
0
e−st dFγ (t)
(3.23)
It is easy to show that the inverse of Laplace transforms gives strict generators: in order to
generate Archimedean copulas then it is sufficient to start from the class of such transforms.
Archimedean copulas are easily verified to be symmetric, in the sense that
CA(v, z) = CA(z, v)
for every (v, z) ∈I 2
They are also associative8, i.e.
CA(CA(v, z), u) = CA(v, CA(z, u))
for every (v, z, u) ∈I 3
since both sides of the previous equality reduce to φ[−1] (φ(v) + φ(z) + φ(u)) .
In addition, their level curves can be easily identified, since the condition
{(v, z) ∈I 2 : C(v, z) = K}
in the Archimedean case becomes
{(v, z) ∈I 2 : φ(v) + φ(z) = φ(K)}
Therefore, for K > 0 the level curves consist of the couples
{(v, z) ∈I 2 : z = φ[−1] (φ(K) −φ(v)) = φ−1 (φ(K) −φ(v))}
where we substituted the ordinary inverse for the pseudo one since φ(K) −φ(v) ∈[0, φ(0)).
For K = 0, the level curve can actually be a whole region in I 2, consisting of the so-called
zero curve itself
{(v, z) ∈I 2 : z = φ[−1] (φ(0) −φ(v)) = φ−1 (φ(0) −φ(v))}
and the so-called zero set of C, which is the region of I 2 between the axes of the Cartesian
plane and the zero curve.
The following theorem is proved in Nelsen (1999):
Theorem 3.11
The level curves of an Archimedean copula (the zero curve included) are
convex.
The density of Archimedean copulas is
CA(v, z) = −φ′′(C(v, z))φ′(v)φ′(z)
(φ′(C(v, z)))3
(3.24)
8 This justifies the relationship with t-norms: bi-dimensional copulas in fact are t-norms iff they are associative
(see Schweizer, 1991). A further discussion of associative functions, copulas and t-norms is in Schweizer and
Sklar (1983).

Market Comovements and Copula Families
123
Dependency
Archimedean copulas are easily related to measures of association.
Genest and MacKay (1986) demonstrated that Kendall’s τ is given by
τ = 4

I
φ(v)
φ′(v) dv + 1
(3.25)
where φ′(v) exists a.e., since the generator is convex. This makes Archimedean copulas
easily amenable to estimation, as we will see in Chapter 5. Furthermore, conditions on the
generators of two Archimedean copulas φ1 and φ2 can be given, which guarantee that the
corresponding copulas are ordered in the same way as their association parameters (Genest
& MacKay, 1986). If one denotes by Ci the copula corresponding to φi, i = 1, 2, then
C1 ≺C2 ↔τC1 ⩽τC2
(3.26)
or, equivalently,
C1 ≺C2 ↔ρSC1 ⩽ρSC2
(3.27)
Otherwise stated, the order between copulas is “measured” by either the Kendall or the
Spearman association parameter. This is another “nice” feature of Archimedean copulas. As
for tail dependency, the following result is demonstrated in Joe (1997):
Theorem 3.12
Let ϕ be a strict generator such that ϕ−1 belongs to the class of Laplace
transforms of a.s. strictly positive r.v.s. If ϕ′(0) is finite and different from zero, then
C(v, z) = ϕ−1(φ(v) + φ(z))
does not have upper tail dependency. If instead C has upper tail dependency, then 1/ϕ′(0) =
−∞and the coefficient of upper tail dependency is
λU = 2 −2 lim
s→0+
ϕ′(s)
ϕ′(2s)
The coefficient of lower tail dependency is
λL = 2 lim
s→+∞
ϕ′(s)
ϕ′(2s)
As for PQD, the relationship between this notion of dependency and Archimedean copulas
relies on the following notion:
Definition 3.12
A function h(t) : ℜ→ℜis said to be completely monotone on the interval
J if it belongs to C∞and if in the interior of J derivatives alternate in sign:
(−1)n dnh(t)
dtn
⩾0,
n = 0, 1, 2, ...
Notice that in particular such a function is non-negative (h ⩾0) and non-increasing
(h′ ⩽0). Given the notion of complete monotonocity, we have the following:

124
Copula Methods in Finance
Theorem 3.13
If the inverse of a strict generator is completely monotone, then the corre-
sponding copula entails PQD:
ϕ−1(φ(v) + φ(z)) ⩾vz
One-parameter Archimedean copulas
Among Archimedean copulas, we are going to consider in particular the one-parameter
ones, which are constructed using a generator ϕα(t), indexed by the (real) parameter α. By
choosing the generator, one obtains a subclass or family of Archimedean copulas. Table 3.4
describes some well-known families and their generators (for a more exhaustive list see
Nelsen, 1999).
The Gumbel family has been introduced by Gumbel (1960). Since it has been discussed
in Hougaard (1986), it is also known as the Gumbel–Hougaard family. Another important
reference is Hutchinson and Lai (1990). It gives the product copula if α = 1 and the upper
Fr´echet bound min(v, z) for α →+∞. Figure 3.14 presents its behavior and some of its
level curves in correspondence to α = 1.5.
The Clayton family was first proposed by Clayton (1978), and studied by Oakes (1982,
1986), Cox and Oakes (1984), Cook and Johnson (1981, 1986). It is comprehensive and
gives the product copula if α = 0, the lower Fr´echet bound max(v + z −1, 0) when α = −1,
and the upper one for α →+∞. Figure 3.15 presents its behavior and some of its level
curves in correspondence to α = 6.
To end up with, the Frank family, which appeared in Frank (1979), is discussed at length
in Genest (1987). It reduces to the product copula if α = 0, and reaches the lower and upper
Fr´echet bounds for α →−∞and α →+∞, respectively. It is the only family for which
both C and C/ are associative. Figure 3.16 presents its behavior and some of its level curves
in correspondence to α = 0.5.
The densities of the previous copulas, obtained via (3.24), are represented in Figure 3.17.
As for the relationship between the parameters of Archimedean copulas and measures of
concordance, using formula (3.25) we get the results collected in Table 3.5 (see, e.g. Frees
& Valdez, 1998).
Table 3.4
Some Archimedean copulas
Gumbel (1960)
φα(t)
(−ln t)α
range for α
[1, +∞)
C(v, z)
exp{−[(−ln v)α + (−ln z)α]1/α}
Clayton (1978)
φα(t)
1
α (t−α −1)
range for α
[−1, 0) ∪(0, +∞)
C(v, z)
max[(v−α + z−α −1)−1/α, 0]
Frank (1979)
φα(t)
−ln exp(−αt)−1
exp(−α)−1
range for α
(−∞, 0) ∪(0, +∞)
C(v, z)
−1
α ln

1 + (exp(−αv)−1)(exp(−αz)−1)
exp(−α)−1


Market Comovements and Copula Families
125
1
0.75
0.5
0.25
0.00
0.5
1
Figure 3.14
The Gumbel copula and its level curves, α = 1.5
1
0.8
0.6
0.4
0.2
0.0
0.00.20.40.60.8 1
Figure 3.15
The Clayton copula and its level curves, α = 6
1
0.75
0.5
0.0
0.00.330.67
1
0.25
Figure 3.16
The Frank copula and its level curves, α = 1
2


## Multivariate Copulas

126
Copula Methods in Finance
100
50
40
30
20
10
10
5
1
1
1
1
1
1
0.5
0
0
0
0.5
0.5
0.5
0.5
0.5
Figure 3.17
Densities of the Gumbel (α = 2, left), the Clayton (α = 6, center) and the Frank
(α = 14.14, right) copulas. All the parameters correspond to a Kendall’s τ = 0.75
Table 3.5
Association measures for some Archimedean copulas
Family
Kendall’s τ
Spearman’s ρS
Gumbel (1960)
1 −α−1
no closed form
Clayton (1978)
α/(α + 2)
complicated expression
Frank (1979)
1 + 4
 
D1 (α) −1
!
/α
1 −12
 
D2 (−α) −D1 (−α)
!
/α
In Table 3.5 the concordance measures of the Frank copula require the computation of
the so-called “Debye” functions, defined as
Dk (α) = k
αk
 α
0
tk
exp(t) −1 dt,
k = 1, 2
For these functions, it follows from basic calculus that
Dk (−α) = Dk (α) +
kα
k + 1
Table 3.5 allows us to remark that, with the exception of Spearman’s ρS for the Gumbel
case, the computation of the copula parameter from the association one is elementary and
the relationship between the two is one-to-one.
An application: An Archimedean copula for international stock indices
Using the time series presented on page 105, whose size is reported in Figure 3.18, we
estimated both Kendall’s τ and Spearman’s ρS, according to the methodology explained
in the corresponding sections. The relationships between the copula parameter and the
association measures in Table 3.5 then permitted us to compute the α value assuming a
Gumbel, Clayton and Frank copula.
Once endowed with the parameter value, we are able to compute any joint probability
between the stock indices: if for instance we consider the DAX–FTSE case and the Frank
copula, we obtain the joint distribution and level curves shown in Figure 3.19.

Market Comovements and Copula Families
127
Figure 3.18
Estimated Kendall’s τ, Spearman’s ρS and α for MIB 30, S&P 500, FTSE, DAX,
1/2/99–3/27/00
0.8
0.1
0.1
0.1
0.1
0.2
0.2
0.2
0.2
0.3
0.3
0.3
0.3
0.4
0.4
0.4
0.5
0.5
0.5
0.6
0.6
0.7
0.7
0.8
0.8
0.9
0.6
0.4
0.2
Figure 3.19
Joint distribution and level curves, DAX–FTSE
When, in particular, the relationship is monotonic, the family can be ordered not only
according to the dependence parameter, as in (3.26) or (3.27) above, but also according
to the α parameter: if the relationship is increasing, as in the Gumbel, Clayton and Frank
cases, the following rule applies:
C1 ≺C2 ↔α1 ⩽α2
where αi is the parameter corresponding to the copula Ci.
It follows that the Gumbel family can represent independence and “positive” dependence
only, since the lower and upper bound for its parameter correspond to the product copula
and the upper Fr´echet bound. On the other hand, the Frank and Clayton family both cover
the whole range of dependence.
As for tail dependency, applying Theorem 3.12 one can show that the Gumbel family
has upper tail dependency, with
λU = 2 −21/α
The Clayton family has lower tail dependency for α > 0, since
λL = 2−1/α
The Frank family has neither lower nor upper tail dependency.
The remarks on Table 3.5, together with the fact that the Frank and Clayton are com-
prehensive, so that they allow the maximum range of dependence, explain the relative
popularity of the one-parameter families in the applied literature on copulas.

128
Copula Methods in Finance
1
0.8
0.6
0.4
0.2
0.0
0.00.20.40.60.8 1
1
1
0
2
1
1.5
Figure 3.20
The Marshall–Olkin copula (left) and its density (right), m = 0.2, n = 0.3
3.2.5
The Marshall–Olkin copula
Definition 3.13
The Marshall–Olkin family (Marshall & Olkin, 1967a, b) is characterized
by two parameters, m and n, belonging to I. It is defined as follows:
CMO(v, z) = min(v1−mz, vz1−n) =
 v1−mz,
vm ⩾zn
vz1−n,
vm < zn
(3.28)
The copula density is
CMO(v, z) =
 (1 −m) v−m,
vm > zn
(1 −n)z−n,
vm < zn
and the copula itself has both an absolutely continuous and a singular component, whose
mass is along the line vm = zn, in I 2. Both the copula and its density are represented in
Figure 3.20.
As for the conditional probability via copula, one can easily verify that
CMO
2|1 (v, z) =
 (1 −m) v−mz,
vm > zn
z1−n,
vm < zn
The family is positively ordered w.r.t. each parameter. It can be noticed that when either
m or n is set to zero, the product copula is obtained; when both parameters are equal to
1, the Marshall–Olkin copula gives the upper Fr´echet bound. Therefore, this copula is not
comprehensive.
As for its relationship with measures of concordance, we have (Nelsen, 1999):
τ =
mn
m −mn + n
and
ρS =
3mn
2m + 2n −mn
This class of copulas presents upper tail dependency, with coefficient
λU = min(m, n)

4
Multivariate Copulas
This chapter extends the results of Chapter 2 to the multidimensional case. For the sake of
simplicity, we will omit the proofs, when the corresponding ones have been given in the
previous chapter.
4.1
DEFINITION AND BASIC PROPERTIES
In the n-dimensional case, n > 2, the notions of groundedness and the n-increasing property
are straightforward extensions of the definitions for the 2-dimensional case.
Let us recall that we denote vectors with bold letters: u = (u1, u2, . . . , un).
Definition 4.1
Let the function G : ℜ∗n →ℜhave a domain Dom G = A1 × A2 × · · · ×
An, where the non-empty sets Ai have a least element ai. The function G is said to be
grounded iff it is null for every v ∈Dom G, with at least one index k such that vk = ak:
G (v) = G(v1, v2, . . . , vk−1, ak, vk+1, . . . , vn) = 0
Let also the n-box A be defined as
A = [u11, u12] × [u21, u22] × · · · × [un1, un2]
with ui1 ⩽ui2, i = 1, 2, . . . , n. An n-box is then the Cartesian product of n closed intervals.
Let us denote with w any vertex of A and with ver(A) the set of all vertices of A:
w ∈ver(A) iff its ith component wi, i = 1, 2, . . . , n, is either equal to ui1 or to ui2. Consider
the product
n

i=1
sgn(2wi −ui1 −ui2)
Since each factor in the product is −1 if wi = ui1 < ui2, is equal to zero if wi = ui1 = ui2,
and is +1 if wi = ui2 > ui1,
n

i=1
sgn(2wi −ui1 −ui2) =



−1
if ui1 ̸= ui2, ∀i, ♯{i : wi = ui2} = 2m + 1
0
if ∃i : ui1 = ui2
m ∈N
+1
if ui1 ̸= ui2, ∀i, ♯{i : wi = ui1} = 2m
If ver(A) ⊂Dom G, define the G-volume of A as the sum

w∈ver(A)
G(w)
n

i=1
sgn(2wi −ui1 −ui2)
(4.1)

130
Copula Methods in Finance
As in the bi-dimensional case, the sum (4.1) measures the mass or volume, according to the
function G, of the n-box A.
We are now ready to define an n-increasing function:
Definition 4.2
The function G : A1 × A2 × · · · × An →ℜis said to be n-increasing if
the G-volume of A is non-negative for every n-box A for which ver(A) ⊂Dom G:

w∈ver(A)
G(w)
n

i=1
sgn(2wi −ui1 −ui2) ⩾0
Grounded, n-increasing functions are non-decreasing with respect to all entries:
Theorem 4.1
A function G : A1 × A2 × · · · × An →ℜgrounded and n-increasing is non-
decreasing in each argument.
Proof :
We are going to demonstrate that, if (u1, u2, . . . , ui−1, x, ui+1, . . . , un) ∈
Dom G, (u1, u2, . . . , ui−1, y, ui+1, . . . , un) ∈Dom G and x ⩽y, then
G(u1, u2, . . . , ui−1, x, ui+1, . . . , un) ⩽G(u1, u2, . . . , ui−1, y, ui+1, . . . , un)
(4.2)
Consider the n-box
A = [a1, u1] × [a2, u2] × · · · ×

ai−1, ui−1

×

x, y

×

ai+1, ui+1

× · · · × [an, un]
Since G is grounded, the G-volume of A is
G(u1, u2, . . . , ui−1, y, ui+1, . . . , un) −G(u1, u2, . . . , ui−1, x, ui+1, . . . , un)
Since it is n-increasing, the volume is non-negative, i.e. (4.2) holds.
□
In order to characterize the copula, we use the notion of margins:
Definition 4.3
The k-dimensional margins of the function G : A1 × A2 × · · · × An →ℜ,
for 1 ⩽k ⩽n, k ∈N, if each Ai is non-empty, are the functions Ci1i2...ik(ui1, ui2, . . . , uik) :
Ai1 × Ai2 × · · · × Aik →ℜdefined by
Gi1i2...ik(ui1, ui2, . . . , uik) = G(a1, a2, . . . , ui1, . . . , ui2, . . . , uik . . . , an)
(4.3)
where i1i2 . . . ik is any selection of k indices (also non-consecutive) among the original n
indices. In particular, we have:
Definition 4.4
The ith one-dimensional margin of the function G : A1 × A2 × · · · × An →
ℜ, if each Ai is non-empty and we denote with ai its maximal element, is the function
Gi(u) : Ai →ℜdefined by
Gi(u) = G(a1, a2, . . . , ai−1, u, ai+1, . . . , an)

Multivariate Copulas
131
A grounded, n-increasing function with one-dimensional margins satisfies the following
lemmas, which are used in the proof of the multidimensional version of Sklar’s theorem:
Lemma 4.1
A function G : A1 × A2 × · · · × An →ℜgrounded, n-increasing, with one-
dimensional margins, is such that
G

uy	
−G

ux	
⩽Gi(y) −Gi(x)
for every 1 ⩽i ⩽n,
x < y
and
uy = (u1, u2, . . . , ui−1, y, ui+1, . . . , un) ∈Dom G
ux = (u1, u2, . . . , ui−1, x, ui+1, . . . , un) ∈Dom G
Lemma 4.2
For the function G of the previous lemma,
|G(u) −G(˙u)| ⩽
n

i=1
|Gi(ui) −Gi(˙ui)|
for every u = (u1, u2, . . . , un) , ˙u = (˙u1, ˙u2, . . . , ˙un) ∈Dom G.
Given this terminology, the definition of n-dimensional subcopula and n-dimensional
copula (from now on subcopula and copula respectively) is:
Definition 4.5
An n-dimensional subcopula is a function C : A1 × A2 × · · · × An →ℜ,
where, for each i, Ai ⊂I and contains at least 0 and 1, such that
(i) C is grounded
(ii) its one-dimensional margins are the identity function on I: Ci(u) = u, i = 1, 2, . . . , n
(iii) C is n-increasing
An n-dimensional subcopula for which Ai = I for every i is a copula C.
It follows from this definition that
Theorem 4.2
For n > 2, 1 < k < n, the k-dimensional margins of C are k-dimensional
copulas.
Proof :
We demonstrate that, when Ai = I for every i, the function
Ci1i2 ... ik (ui1, ui2, . . . , uik) : I k →ℜ
defined according to (4.3) is
(i) grounded
(ii) such that Ci(u) = u, i = i1, i2, . . . , ik
(iii) k-increasing

132
Copula Methods in Finance
As for (i), groundedness, with at least one index ij such that uij = aij , we have
Ci1i2...ik (ui1, ui2, . . . , uik) = C(a1, a2, . . . , ui1, . . . , uij−1, aij , uij+1, . . . , uik, an) = 0
since the vector

a1, a2, . . . , ui1, . . . , uij−1, aij , uij+1, . . . , uik, an
	
has the feature of v in
Definition 4.1.
As for (ii), it comes from the fact that one-dimensional margins for C are also one-
dimensional margins for its k-dimensional margins.
Property (iii), k-increasingness is a consequence of the fact that the Ci1i2 ... ik -volume of
each k-box

ui11, ui12

×

ui21, ui22

× · · · ×

uik1, uik2

is the C-column of the n-box
[a1, a1] × · · · ×

ui11, ui12

×

ui21, ui22

× · · · ×

uik1, uik2

× · · · × [an, an]
which is non-negative because of n-increasingness.
□
Example 4.1
It is easy to verify that the function
C(u) = min(u1, u2, . . . , un)
is an n-dimensional copula:
(i) min (u1, u2, . . . , ui−1, 0, ui+1, . . . , un) = 0, i = 1, 2, . . . , n
(ii) min (1, 1, . . . , ui, . . . , 1) = ui, i = 1, 2, . . . , n
(iii)

w∈ver(A)
min(w1, w2, . . . , wn)
n

i=1
sgn(2wi −ui1 −ui2) ⩾0
With the same technique we can verify that its margins are copulas, since for every k
Ci1i2 ... ik (ui1, ui2, . . . , uik) = min(ui1, ui2, . . . , uik)
As in the bi-dimensional case, from the characterization of C it follows that
• it is non-decreasing in each argument (Theorem 4.1)
• Ran C = I (by (i)), C(v) = 0 if there exists an index i such that ui = 0; by (ii), if we
denote by ei the vector that has all entries equal to zero, apart from the ith, which is equal
to 1, C(v + ei) = 1. The two features, together with the fact that C is non-decreasing in
each component, give the assertion about Ran C
• it is uniformly continuous (as a straightforward consequence of Lemma 4.2 above):
|C(u) −C(˙u)| ⩽
n

i=1
|ui −˙ui|
for every u, ˙u ∈I n
• it has mixed kth-order partial derivatives a.s., 1⩽k ⩽n, and
0 ⩽
∂kC(u)
∂u1 ∂u2 . . . ∂uk
⩽1

Multivariate Copulas
133
Example 4.2
For the copula in the previous example
• x ⩽y
implies min(u1, u2, . . . , ui−1, x, ui+1, . . . , un) ⩽min(u1, u2, . . . , ui−1, y, ui+1,
. . . , un)
• 0 ⩽min(u1, u2, . . . , un) ⩽1:
|min(u1, u2, . . . , un) −min(˙u1, ˙u2, . . . , ˙un)| ⩽
n

i=1
|ui −˙ui|
• the partial derivatives are
∂C(u)
∂ui
=

 1
if ui = min(u1, u2, . . . , un)
0
otherwise
and
∂kC(u)
∂u1∂u2 . . . ∂uk
= 0
for k ⩾2
4.2
FR ´ECHET BOUNDS AND CONCORDANCE ORDER:
THE MULTIDIMENSIONAL CASE
It is straightforward to demonstrate that
Theorem 4.3
Every copula satisfies the following inequality:
max(u1 + u2 + · · · + un −1, 0) ⩽C(u) ⩽min(u1, u2, . . . , un)
for every u ∈I n.
The upper bound still satisfies the definition of copula, and is denoted with C+ (the
maximum copula). However, as first noted by F´eron (1956), the lower bound never satisfies
the definition of copula for n > 2. This can be seen from the following:
Example 4.3 (Schweizer & Sklar, 1983)
Consider the n-cube

1
2, 1
n
and compute its
volume according to the lower copula bound:
max (1 + 1 + · · · + 1 −n + 1, 0 −n) −n max( 1
2 + 1 + · · · + 1 −n + 1, 0)
+
n
2
	
max( 1
2 + 1
2 + 1 + · · · + 1 −n + 1, 0) + . . .
+ max( 1
2 + 1
2 + · · · + 1
2 −n + 1, 0)
= 1 −n/2 + 0 + · · · + 0
Since for n > 2 the volume is negative (n > 2 ⇔1 −n/2 < 0), the lower bound cannot be
a copula.
Nonetheless, the bound is the best possible: pointwise there always exists a copula that takes
its value. Therefore, the latter copula is parametrized using the point for which it coincides
with the Fr´echet lower bound:

134
Copula Methods in Finance
Theorem 4.4 (Sklar, 1998)
When n > 2, for every u ∈I n there exists a copula Cu such
that
Cu(u) = max(u1 + u2 + · · · + un −1, 0)
Proof :
See Nelsen (1999).
□
The notion of order for n-dimensional copulas requires the introduction of the survival
function for n-dimensional vectors of uniform variates, which will be discussed further
in section 4.4:
Definition 4.6
The joint survival function for the vector (U1, U2, . . . , Un) of (standard)
uniform r.v.s with copula C, denoted as C/, represents, when evaluated at (u1, u2, . . . , un),
the joint probability that (U1, U2, . . . , Un) be greater than u1, u2, . . . , un:
C/(u1, u2, . . . , un) = Pr[U1 > u1, U2 > u2, . . . , Un > un]
The following definition of concordance order between copulas can then be introduced:
Definition 4.7
The copula C1 is smaller than the copula C2 (written as C1 ≺C2) iff
C1(u) ⩽C2(u)
C/1(u) ⩽C/2(u)
for every u ∈I n.
The order so defined is only partial, as in the bi-dimensional case.1
Example 4.4
We want to determine whether every three-dimensional copula is smaller
than the maximum one, i.e. whether
C ≺C+
for n = 3. Since Theorem 4.3 guarantees that, at any point in I 3, C(u) ⩽C+(u), we are
left with testing whether C/(u) ⩽C/
+(u). We will show in Example 4.5 below that when
n = 3 the survival function is
C/(u1, u2, u3) = 1 −u1 −u2 −u3 + C12(u1, u2) + C13(u1, u3)
+ C23(u2, u3) −C(u1, u2, u3)
It follows that C/(u) ⩽C/
+(u) iff
1 −u1 −u2 −u3 + C12(u1, u2) + C13(u1, u3) + C23(u2, u3) −C(u1, u2, u3)
⩽1 −u1 −u2 −u3 + min(u1, u2) + min(u1, u3) + min(u2, u3) −min(u1, u2, u3)
1 In the bi-dimensional case, the definition was reduced to the first inequality, since C1(v, z) ⩽C2(v, z) iff
C/1(v, z) ⩽C/2(v, z) (due to the fact that C/1(v, z) = 1 −v −z + C(v, z)).

Multivariate Copulas
135
Since the two-dimensional margins are copulas, Cij(ui, uj) ⩽min(ui, uj) for any choice
of indices; however, also
C(u1, u2, u3) ⩽min(u1, u2, u3)
and we cannot state that C/ (u) ⩽C/
+(u).
4.3
SKLAR’S THEOREM AND THE BASIC PROBABILISTIC
INTERPRETATION: THE MULTIDIMENSIONAL CASE
In order to introduce Sklar’s theorem, we take it for granted that the readers are familiar
with the notion of n-dimensional joint distribution functions (or n-dimensional distribu-
tion functions or joint distribution functions) for r.v.s, whose one-dimensional margins are
marginal distribution functions.
The following generalization to the n-dimensional case of Sklar’s theorem guarantees
that not only every subcopula is a joint distribution function, if its arguments are marginal
distribution functions, but that the converse holds too. Every joint distribution function can
be represented as a (unique) subcopula, which in turn can be extended (not uniquely, in
general) to a copula. If the marginals are continuous, the extension is unique.
Theorem 4.5
Let F1(x1), F2(x2), . . . , Fn(xn) be (given) marginal distribution functions.
Then, for every x = (x1, x2, . . . , xn) ∈ℜ∗n:
(i) If C is any subcopula whose domain contains Ran F1 × Ran F2 × · · · × Ran Fn,
C(F1(x1), F2(x2), . . . , Fn(xn))
is a joint distribution function with margins F1(x1), F2(x2), . . . , Fn(xn).
(ii) Conversely, if F is a joint distribution function with margins
F1(x1), F2(x2), . . . , Fn(xn)
there exists a unique subcopula C, with domain Ran F1 × Ran F2 × · · · × Ran Fn,
such that
F(x) = C(F1(x1), F2(x2), . . . , Fn(xn))
(4.4)
If F1(x1), F2(x2), . . . , Fn(xn) are continuous, the subcopula is a copula; if not, there exists
a copula C such that
C(u1, u2, . . . , un) = C(u1, u2, . . . , un)
for every (u1, u2, . . . , un) ∈Ran F1 × Ran F2 × · · · × Ran Fn.
The proof of the theorem in the n-dimensional case without the extension lemma is in
Schweizer and Sklar (1983). The complete proof, i.e. with the extension lemma, was given
independently by Moore and Spruill (1975), Deheuvels (1978) and Sklar (1996).

136
Copula Methods in Finance
The following corollary holds:
Corollary 4.1
Under the hypotheses of part (ii) of Sklar’s theorem, the (unique) subcopula
C: Ran F1 × Ran F2 × · · · × Ran Fn →I such that
F(x) = C(F1(x1), F2(x2), . . . , Fn(xn))
for every x in ℜ∗n is
C(u) = F(F −1
1 (u1), F −1
2 (u2), . . . , F −1
n
(un))
Otherwise stated, Corollary 4.1 states that the construction via Sklar’s theorem exhausts the
so-called Fr´echet class, i.e. the class of joint distribution functions that have F1, F2, . . . , Fn
as margins.
As in the bi-dimensional case, Sklar’s theorem guarantees that the cumulative joint prob-
ability can be written (via an eventually non-unique copula) as a function of the cumulative
marginal ones and vice versa
F(x) = C(F1(x1), F2(x2), . . . , Fn(xn))
We say that the r.v.s in X have the copula C or that the latter is the copula of X. When
needed, we denote the copula of X = [X1X2 . . . Xn] also as CX or CX1X2...Xn. Also in the
multidimensional case the possibility of writing the joint cumulative probability in terms
of the marginal ones, i.e. the basic probabilistic interpretation of copulas, and the fact
that multidimensional copulas are dependence functions, opens the way to a number of
financial applications.
An application: Digital options with n underlyings
The copula application to bivariate option pricing in Chapter 2 can be extended to the
n-dimensional case, as follows. Consider an n-variate bearish digital option, written on
n underlyings, X1, . . . , Xn, with strikes k1, . . . , kn and expiration T . Under complete,
arbitrage-free markets its forward price is the risk-neutral probability
Pr(X1 ⩽k1, . . . , Xn ⩽kn) = F(k1, . . . , kn)
According to the multivariate version of Sklar’s theorem, it is always possible to represent
this price in terms of the single digital prices, through a copula, unique on n
i=1Ran Fi:
F(k1, . . . , kn) = C(F1(k1), . . . , Fn(kn))
where the distribution functions Fi are those of the single underlyings Xi. If the latter have
normal log returns, no matter how we want to model their dependency, we have in particular
F(k1, . . . , kn) = C((−d21 (k1)), . . . , (−d2n (kn)))
(4.5)
where
−d2i (ki) = −ln

Xi,0/ki
	
+ µXiT
σXi
√
T
,
µXi = r −
σ 2
Xi
2
and r is the (instantaneous) riskless rate, assumed constant.

Multivariate Copulas
137
The basic probabilistic interpretation has at least two important consequences, which we are
going to discuss in the rest of the section:
(1) r.v.s are independent iff on n
i=1Ran Fi their copula is the product one;
(2) the copulas of a.s. increasing or decreasing transforms of continuous r.v.s are easily
written in terms of the copula of X and Y: in particular, copulas are invariant w.r.t.
increasing transforms.
As for the characterization of independence via copulas, recall that the r.v.s in the vector X
are independent iff F(x) = F1(x1)F2(x2) . . . Fn(xn), and define the product copula as
C⊥(u) = u1u2 . . . un
It is evident that Sklar’s theorem entails
Corollary 4.2
The r.v.s in X are independent iff they have the product copula on
n
i=1Ran Fi.
As for the copulas of increasing or decreasing transforms of continuous r.v.s, the following
theorem holds:
Theorem 4.6 (Schweizer & Wolff, 1976, 1981)
Let the r.v.s in X be continuous with cop-
ula C. If α1, α2, . . . , αn are a.s. increasing transformations on αi : Ran Fi →ℜ∗, the r.v.s
α1(X1), α2(X2), . . . , αn(Xn) – with marginals
H1 = F1(α−1
1 ), H2 = F2(α−1
2 ), . . . , Hn = Fn(α−1
n )
and joint distribution H – have copula C too:
Cα1(X1),α2(X2), ... ,αn(Xn)(u) = CX1X2...Xn(u)
for every u ∈I n or, equivalently:
H(u) = C(H1(u1), H2(u2), . . . , Hn(un))
Copulas are then invariant w.r.t. increasing transformations, even though the latter act
differently on the components of X.
Analogously, one could demonstrate that
Corollary 4.3
Under the hypotheses of Theorem 4.6, if α1 is a.s. decreasing and α2, . . . , αn
are a.s. increasing
Cα1(X1),α2(X2),...,αn(Xn)(u) = Cα2(X2),...,αn(Xn)(u2, u3, . . . , un)
−CX1,α2(X2),...,αn(Xn)(1 −u1, u2, u3, . . . , un)
or, in terms of distribution functions:
H(u) = Cα2(X2),...,αn(Xn)(H2(u2), . . . , Hn(un))
−CX1,α2(X2),...,αn(Xn)(1 −H1(u1), H2(u2), . . . , Hn(un))

138
Copula Methods in Finance
where
Cα2(X2),...,αn(Xn) : I n−1 →I
is the copula of α2(X2), . . . , αn(Xn) (and consequently of X2 . . . Xn), while
CX1,α2(X2),...,αn(Xn)
is the copula of X1, α2(X2), . . . , αn(Xn) (and consequently of X1X2 . . . Xn):
Cα2(X2),...,αn(Xn)(u2, u3, . . . , un) = CX2,...,Xn(u2, u3, . . . , un)
CX1,α2(X2),...,αn(Xn)(u) = CX1X2...Xn(u)
For the three-dimensional case, for instance, we have, for α1 decreasing and α2, α3
increasing
Cα1(X1),α2(X2),α3(X3)(u) = Cα2(X2),α3(X3)(u2, u3) −CX1,α2(X2),α3(X3)(1 −u1, u2, u3)
= CX2,X3(u2, u3) −CX1X2,X3(1 −u1, u2, u3)
Using recursively the corollary above, one can obtain the copula for the case in which two
of the n functions αi are decreasing, three are, and so on.
To conclude this section on the relationship between copula functions and r.v.s, let us
notice that, as in the bi-dimensional case, multivariate copulas can be easily seen to be
distribution functions of vectors of standard uniform random variables: for every u ∈I n
C(u) = Pr(U1 ⩽u1, . . . , Un ⩽un)
The following remark extends to the multidimensional case:
Remark 4.1
The copula of the vector X is the joint distribution function of the probability-
integral transforms of the functions Fi:
Pr (F1(X1) ⩽u1, F2(X2) ⩽u2, . . . , Fn(Xn) ⩽un)
= Pr

X1 ⩽F −1
1
(u1) , X2 ⩽F −1
2 (u2), . . . , Xn ⩽F −1
n (un)

= C

F1

F −1
1
(u1)

, F2

F −1
2
(u2)

, . . . , Fn

F −1
n
(un)

= C(u1, u2, . . . , un)
4.3.1
Modeling consequences
In this section we revisit some examples of Chapter 2, in order to highlight that also in the
multidimensional case the modeling consequence of the copula adoption is that of enlarging
the pricing and risk evaluation possibilities beyond the Black–Scholes world.
An application: Digital options with log-normal underlyings
Let us consider the pricing of digital options with n underlyings on page 136, when the
corresponding returns are assumed to be not only marginally normal, but also jointly normal,

Multivariate Copulas
139
i.e. in the Black–Scholes world. In this case the joint risk-neutral distribution of the returns
can be written via the Gaussian copula with Gaussian marginals, as in the bivariate case
(see also section 8.1 below). The Gaussian copula in turn is defined as
CGa
R (u) = R

−1(u1), −1(u2), . . . , −1(un)

=
 −1(u1)
−∞
. . .
 −1(un)
−∞
1
(2π)
n
2 |R|
1
2
exp

−1
2xT R−1x

dx1 . . . dxn
where R is the multivariate Gaussian distribution function with correlation matrix R. It
follows from Theorem 4.6 that the price can be written in copula terms using the Gaussian
copula too. More precisely, let the log returns of the underlyings, ln

Xi/Xi,0
	
, be normal
with risk-neutral mean µXi = r −1
2σ 2
Xi and variance σ 2
Xi per unit of time, so that the
so-called standardized returns from 0 to T ,
X′i = ln

Xi/Xi,0
	
−µXiT
σXi
√
T
are standard normal. Assume them to be also jointly normal. Then the joint risk-neutral
distribution of the underlyings, F, can be written as:
F(x1, . . . , xn) = CGa
R ((x′
1), . . . , (x′
n))
According to (4.5), the forward price of the n-variate bearish digital option is then:
F(k1, . . . kn) =
 −d21
−∞
. . .
 −d2n
−∞
1
(2π)
n
2 |R|
1
2
exp

−1
2x
T R−1x

dx1 . . . dxn
(4.6)
where
−d2i = −d2i(ki) = ln

ki/Xi,0
	
−µXiT
σXi
√
T
Suppose instead that the copula of the underlyings (or the returns) is a Student’s T copula,
an assumption that, as we will discuss in Chapter 5, seems much more appropriate in the
financial domain. The Student’s copula will be defined below to be
TR,υ(u1, u2, . . . , un)
=
 t−1
υ (u1)
−∞
 t−1
υ (u2)
−∞
. . .
 t−1
υ (un)
−∞
	
υ + n
2

|R|−1
2
	

υ
2

(υπ)
n
2

1 + 1
υ x
T R−1x
−υ+n
2
dx1dx2 . . . dxn
where υ is, as usual, the number of degrees of freedom. Maintaining the marginal normality
assumption on standardized returns, it follows from (4.5) that the digital option forward

140
Copula Methods in Finance
price is
F(k1, . . . , kn) =
 t−1
υ ((−d21))
−∞
 t−1
υ ((−d22))
−∞
. . .
 t−1
υ ((−d2n))
−υ
	
υ + n
2

|R|−1
2
	

υ
2

(υπ)
n
2

1 + 1
υ x
T R−1x
−υ+n
2
dx1dx2 . . . dxn
Let us consider the following three assets: the DAX 30 index, the DEM/USD exchange
rate and the 10-year total return index for the German bond market (GER10y). In the next
chapter we will use weekly (average) data from January 1992 to June 2001, for a total of
248 observations, in order to fit a Gaussian copula to them. By so doing, we will obtain the
following correlation matrix:
R =
DAX 30
DEM/USD
GER10y
DAX 30
1
DEM/USD
0.3035
1
GER10y
0.1998
0.0551
1
Suppose that you want to price an at-the-money digital option on them, with one week to
expiration. Using the same dataset, the initial levels of the three indices, and therefore
the option strikes, were respectively X1,0 = k1 = 1603.620, X2,0 = k2 = 1.547, X3,0 =
k3 = 7.37%. Consider also that the estimated standard deviations, over the same period,
are σX1 = 3.56%, σX2 = 2.04%, σX3 = 0.90%, while the riskless rate is r = 3%, so that
µX1 = 2.94%, µX2 = 2.98%, µX3 = 2.996% and
−d21 = −µX1
σX1
= −0.8249,
−d22 = −1.4604,
−d23 = −3.3289
Using formula (4.6) we obtain the following price:
 −0.8249
−∞
 −1.46049
−∞
 −3.3289
−∞
1
(2π)
3
2 |R|
1
2
exp(−1
2x
T R−1x) dx1 dx2 dx3
(4.7)
4.4
SURVIVAL COPULA AND JOINT SURVIVAL FUNCTION
This section introduces the notion of survival copula and recalls the joint survival function
(for standard uniform r.v.s) copula given above. It discusses the relationships between them
and applies them to the evaluation of the distribution functions of maxima and minima of
n > 2 r.v.s.
Let us consider the probability:
F(x) = Pr(X1 > x1, X2 > x2, . . . , Xn > xn)
(4.8)
As in the bi-dimensional case, this probability is called the joint survival probability
or survival function of the n agents or components Xi, while the marginal survival

Multivariate Copulas
141
probabilities or survival functions are:
F i(xi) = Pr(Xi > xi)
The copula that represents the joint survival probability in terms of the survival probabili-
ties of the n agents or components Xi separately is named the survival copula. The existence
of the latter is guaranteed by the survival version of Sklar’s theorem, which guarantees that
there is a copula C, unique on Ran F 1 × Ran F 2 × · · · × Ran F n, such that
F(x) = C(F 1 (x1) , F 2 (x2) , . . . , F n (xn))
(4.9)
Uniqueness tout court holds if the marginal survival probabilities are continuous. We are
then allowed to introduce the following:
Definition 4.8
The survival copula of the r.v.s X1, X2, . . . , Xn is the copula C, unique on
Ran F1 × Ran F2 × · · · × Ran Fn, such that
F(x) = C(F 1 (x1) , F 2 (x2) , . . . , F n (xn))
(4.10)
Also in the multidimensional case it is customary to distinguish the survival copula from
the joint survival or survival function of n uniform variates, defined above. In terms of
the latter, the probability F(x) is simply
F(x) = C/(F1 (x) , F2 (x2) , . . . , Fn(xn))
Recalling that the probability integral transforms are uniformly distributed, and denoting
with Ui the nth transform:
Ui = Fi(Xi)
one can also write Fi(xi) = ui and 1 −F i(xi) = ui; with this notation, it is very easy to
find the relationship between the survival copula and the survival function for uniform
variates. Since both can express the joint survival probability, F(x), respectively as
C(F 1 (x1) , F 2 (x2) , . . . , F n (xn))
and
C/(F1 (x) , F2 (x2) , . . . , Fn(xn))
we have
−
C(F 1(x1), F 2(x2), . . . , F n(xn)) = C/(F1 (x) , F2 (x2) , . . . , Fn(xn))
= C/ (1 −F 1(x1), 1 −F 2(x2), . . . , 1 −F n(xn))
It follows that the relationship between
−
C and C/ is
−
C(u1, u2, . . . , un) = C/(1 −u1, 1 −u2, . . . , 1 −un)

142
Copula Methods in Finance
We are also interested in the relationship between the survival copula and the copula,
since, differently from the bi-dimensional case, in the multidimensional one we do not define
the former using the latter. Georges et al. (2001), adapting a result proved by Feller (1968),
demonstrate the following theorems, which give the survival copula in terms of the copula
and vice versa:
Theorem 4.7
The survival copula
−
C can be written in terms of the corresponding copula
C as follows:
−
C(u1, u2, . . . , un) = C/(1 −u1, 1 −u2, . . . , 1 −un)
=
n

i=0

(−1)i

w(u)∈Z(n−i,n,1)
C(1 −w)

where Z(n −i, n, 1) is the set of the
n
i
	
possible vectors with n −i components equal to
1, i equal to ui, and
1 −w ≡(1 −w1, . . . , 1 −wn)
Symmetrically, the copula C can be written in terms of the corresponding survival copula
−
C as follows:
C(u1, u2, . . . , un) =
n

i=0

(−1)i

w(u)∈Z(n−i,n,1)
C(1 −w)

Example 4.5
In the three-dimensional case, for instance, the previous theorem allows us,
for a given copula, to obtain first the survival function and then the survival copula, as
follows: we have the following representation for the survival function
C/(u1, u2, u3) =
3

i=0

(−1)i

w(u)∈Z(3−i,3,1)
C(w)

= C(1, 1, 1) −C(u1, 1, 1) −C(1, u2, 1) −C(1, 1, u3)
+ C(u1, u2, 1) + C(u1, 1, u3) + C(1, u2, u3) −C(u1, u2, u3)
Exploiting the uniform margins property this becomes
C/(u1, u2, u3) = 1 −u1 −u2 −u3 + C12(u1, u2)
+ C13(u1, u3) + C23(u2, u3) −C(u1, u2, u3)
where Cij, i = 1, 2, j = 2, 3, are the two-dimensional margins of the copula. It follows that
the survival copula is
−
C(u1, u2, u3) = C/(1 −u1, 1 −u2, 1 −u3)
= −2 + u1 + u2 + u3 + C12(1 −u1, 1 −u2)

Multivariate Copulas
143
+ C13(1 −u1, 1 −u3) + C23(1 −u2, 1 −u3)
−C(1 −u1, 1 −u2, 1 −u3)
To conclude our discussion of the survival copula, we mention the following theorem,
which gives – in terms of the copula of a random vector – the survival copula of certain
transforms of its components. The theorem can be very useful for simulation issues.
Theorem 4.8
Let X1, X2, . . . , Xn be n r.v.s with continuous c.d.f.s F1, F2, . . . , Fn and
copula C. We consider n continuous c.d.f.s G1, G2, . . . , Gn and we denote by Tj the r.v.
Tj = G−1
j (1 −Fj(Xj)). Then, the margins and the copula of the random vector (T1, T2, . . .,
Tn) are respectively G1, G2, . . . , Gn and the survival copula C of C.
Proof :
To prove that the margins are G1, G2, . . . , Gn is very simple since:
Pr(Tj ⩽tj) = Pr(G(−1)
j
(1 −Fj(Xj)) ⩽tj)
= 1 −Pr(1 −Fj(Xj) ⩾Gj(tj)) = 1 −Pr(Fj(Xj) ⩽1 −Gj(tj))
= 1 −Fj

F (−1)
j

1 −Gj(tj)
	
= Gj(tj)
As for the copula, the fact that the copula of the random vector (T1, T2, . . . , Tn) is C
depends on the theorem of Schweizer and Wolff (1976, 1981), because G−1
j
and 1 −Fj are
respectively increasing and decreasing functions.
□
As in the bi-dimensional case, distribution functions (d.f.s) for minima or maxima of n
random variables are easily expressed in terms of their copula, survival copula or survival
function. In fact, let us denote with m the minimum between the given r.v.s:
m = min(X1, X2, . . . , Xn)
and with M their maximum:
M = max(X1, X2, . . . , Xn)
Let Fm and FM be the d.f.s of the minimum and maximum respectively. We have
for maxima:
FM(a) = Pr(M ⩽a) = Pr(X1 ⩽a, X2 ⩽a, . . . , Xn ⩽a) = F(a, a, . . . , a) =
= C(F1(a), F2(a), . . . , Fn(a))
for minima:
Fm(a) = Pr(m ⩽a) = 1 −Pr(m > a)
= 1 −Pr(X1 > a, X2 > a, . . . , Xn > a)
= 1 −C/(F1(a), F2(a), . . . , Fn(a)) =
= 1 −C(F 1(a), F 2(a), . . . , F n(a))

144
Copula Methods in Finance
This method may be extended to any order statistics involving the r.v.s X1, X2, . . . , Xn
(Theorem 23 of Georges et al., 2001).
4.5
DENSITY AND CANONICAL REPRESENTATION
OF A MULTIDIMENSIONAL COPULA
This section introduces the notions of density and canonical representation of a copula,
together with those of the absolutely continuous and singular components.
Definition 4.9
The density c(u1, u2, . . . , un) associated to a copula C(u1, u2, . . . , un) is
c(u1, u2, . . . , un) = ∂nC(u1, u2, . . . , un)
∂u1 . . . ∂un
It exists a.e. in I n, as noticed at the end of section 4.1.
The density can be used to define the absolutely continuous and singular components of
C, denoted as AC and SC, as follows:
AC(u1, u2, . . . , un) =
 u1
0
 u2
0
. . .
 un
0
∂nC(s1, s2, . . . , sn)
∂s1 . . . ∂sn
ds1 . . . dsn
SC(u1, u2, . . . , un) = C(u1, u2, . . . , un) −AC(u1, u2, . . . , un)
In turn, a copula for which C = AC on I n is called absolutely continuous, while it is
called singular if C = SC on I n. It has both an absolutely continuous and a singular
component if it belongs to neither the first nor the second class.
Each copula induces a probability measure on I n, which is no other than the C-volume of
section 4.1. The C-measure of the absolute component is AC(1), while that of the singular
component is SC(1).
Example 4.6
The product copula C⊥= u1u2u3 is absolutely continuous, since
∂3s1s2s3
∂s1∂s2∂s3
= 1
and for every (u1, u2, u3) ∈I 3
AC =
 u1
0
 u2
0
 u3
0
∂3s1s2s3
∂s1∂s2∂s3
ds1ds2ds3 = u1u2u3 = C⊥
The Fr´echet upper bound C+ is singular, since a.e.
∂3C+(u1, u2, u3)
∂u1 ∂u2 ∂u3
= ∂3 min(u1, u2, u3)
∂u1 ∂u2 ∂u3
= 0
Consequently
AC =
 u1
0
 u2
0
 u3
0
∂3C+
∂s1∂s2∂s3
ds1ds2ds3 = 0 ̸= C+

Multivariate Copulas
145
Finally, notice that for continuous random variables, the copula density is related to the
density of the distribution F, denoted as f , by the canonical representation:
f (x1, x2, . . . , xn) = c(F1(x1), F2(x2), . . . , Fn(xn)) ·
n

j=1
fj(xj)
where
c(F1(x1), F2(x2), . . . , Fn(xn)) = ∂n(C(F1(x1), F2(x2), . . . , Fn(xn)))
∂F1(x1)∂F2(x2) . . . ∂Fn(xn)
and fj are the densities of the marginals
fj(xj) = dFj(xj)
dxj
Also in the n-dimensional case the copula density is therefore equal to the ratio of the
joint density f and the product of all marginal densities fj. From this expression it is clear
also that the copula density takes a value equal to 1 everywhere when the original r.v.s are
independent.
The canonical representation is very useful in statistical estimation, in order to have a
flexible representation for joint densities (mostly other than Gaussian, in financial applica-
tions), and in order to determine the copula, if one knows the joint and marginal distribution:
see Chapter 5.
4.6
BOUNDS FOR DISTRIBUTION FUNCTIONS OF SUMS OF n
RANDOM VARIABLES
The matter of the distribution function of the sum of r.v.s can be addressed in the multivariate
case as well.
In the present setting, it has the following formulation: given n r.v.s with distribution
functions Fi, i = 1, 2, . . . , n, and having denoted with FS the distribution function of their
sum, find distribution functions FL and FU such that, for every s ∈ℜ∗
FL(s) = inf
F∈F FS(s)
(4.11)
FU(s) = sup
F∈F
FS(s)
(4.12)
where F is the Fr´echet class which has Fi, i = 1, 2, . . . , n as marginals, defined as in the
bi-dimensional case.
Theorem 4.9
If one denotes with 1 the n-dimensional vector whose components are all
equal to 1, and defines as T (s) the set of vectors such that the sum of their components is
equal to 1:
T (s) =

t ∈ℜn : t1 = s


146
Copula Methods in Finance
1.5
MIB
DAX
UKX
MIB
DAX
SPX
MIB
DAX
CAC
MIB
DAX
NKY
MIB
UKX
NKY
MIB
SPX
NKY
MIB
CAC
NKY
MIB
UKX
SPX
MIB
UKX
CAC
MIB
SPX
CAC
1
0.5
0
−0.5
−1
−1.5
−2
−2.5
−3
−3.5
Figure 4.1
VaR bounds at the 95% level of confidence for equally weighted portfolios of three stock
indices, the empirical quantiles
then the stochastic bounds on FS are
FL(s) = sup
t∈T (s)
max
 n

1
Fi(ti) −(n −1), 0

(4.13)
FU(s) =
inf
t∈T (s) min
 n

1
Fi(ti), 1

(4.14)
As in the bi-dimensional case, apart from very special cases, the bounds do not have a
closed form expression: however, Frank, Nelsen and Schweizer (1987) notice that they can
be computed iteratively. The same iterative procedure can be adopted with the numerical
algorithms of Williamson and Downs (1990).
An application: VaR bounds, Luciano & Marena, 2002a
The computation of the VaR bounds in Chapter 2 can be extended to larger portfolios.
Luciano and Marena start by considering equally weighted portfolios of three assets, using
the same data as in the three-dimensional case and adopting the numerical computation
device in Williamson and Downs (1990). Figure 4.1 presents the portfolio VaR bounds,
corresponding to Figure 2.9 in Chapter 2.
4.7
MULTIVARIATE DEPENDENCE
Some of the copula properties related to dependence measures may be extended to the
multivariate case. For example, in three or more dimensions we have orthants as the gen-
eralization of quadrants: the extension of quadrant dependence is therefore the following
orthant dependence concept.
Definition 4.10 [Positively orthant dependence]
Let X = (X1, X2, . . . , Xn) be an n-di-
mensional random vector.

Multivariate Copulas
147
(1) X is said to be positively lower orthant dependent (PLOD) if for all (x1, x2, . . . , xn)
in ℜn,
Pr (X1 ⩽x1, X2 ⩽x2, . . . , Xn ⩽xn) ⩾
n

i=1
Pr (Xi ⩽xi)
i.e. C ≻C⊥.
(2) X is said to be positively upper orthant dependent (PUOD) if for all (x1, x2, . . . , xn) in
ℜn,
Pr (X1 > x1, X2 > x2, . . . , Xn > xn) ⩾
n

i=1
Pr (Xi > xi)
i.e. C/ ≻C⊥.
(3) X is said to be positively orthant dependent (POD) if for all (x1, x2, . . . , xn) in ℜn it is
both PLOD and PUOD.2
Negative lower orthant dependence (NLOD), negative upper orthant dependence (NUOD),
and negative orthant dependence (NOD) are defined analogously by reversing the sense of
the previous inequalities.
Many of the measures of concordance have a multivariate version. In general, however,
each bivariate concordance and association measure has several multidimensional versions
(see Joe, 1990, 1997; Wolff, 1981; Brindley & Thompson, 1972 and Block & Ting, 1981,
for a further discussion of multivariate dependence concepts).
4.8
PARAMETRIC FAMILIES OF n-DIMENSIONAL COPULAS
4.8.1
The multivariate Gaussian copula
Definition 4.11 [Multivariate Gaussian copula (MGC)]
Let R be a symmetric, positive
definite matrix with diag(R) = (1, 1, . . . , 1)
T and R the standardized multivariate normal
distribution with correlation matrix R. The MGC is defined as follows:
CGa
R (u) = R

−1(u1), −1(u2), . . . , −1(un)

where −1, as usual, is the inverse of the standard univariate normal distribution function .
As in the bivariate case, the Gaussian copula generates the standard Gaussian joint distri-
bution function, whenever the margins are standard normal.
Proposition 4.1
The Gaussian copula generates the standard joint normal distribution func-
tion – via Sklar’s theorem – iff the margins are standard normal.
From the definition of the Gaussian copula we can easily determine the corresponding
density. Using the canonical representation, we have:
1
(2π)
n
2 |R|
1
2
exp

−1
2x
T R−1x

= cGa
R ((x1), (x2), . . . , (xn))
×
n

j=1

1
√
2π
exp

−1
2x2
j

2 Since in the bi-dimensional case PLOD and PUOD coincide, we introduced PQD only.

148
Copula Methods in Finance
where |R| is the determinant of R. We deduce that:
cGa
R ((x1), (x2), . . . , (xn)) =
1
(2π)
n
2 |R|
1
2
exp

−1
2x
T R−1x

n

j=1

1
√
2π
exp

−1
2x2
j

Let uj = (xj), so that xj = −1(uj). The density can be rewritten as follows:
cGa
R (u1, u2, . . . , un) =
1
|R|
1
2
exp

−1
2ς
T (R−1 −I)ς

where ς =

−1(u1), −1(u2), . . . , −1(un)
	T
.
4.8.2
The multivariate Student’s t copula
Definition 4.12 [Multivariate Student’s t copula (MTC)]
Let R be a symmetric, positive
definite matrix with diag(R) = (1, 1, . . . , 1)
T and tR,υ the standardized multivariate Stu-
dent’s t distribution with correlation matrix R and υ degrees of freedom, i.e.
tR,υ(x1, x2, . . . , xn) =
 x1
−∞
 x2
−∞
. . .
 xn
−∞
×
	
υ + n
2

|R|−1
2
	

υ
2

(υπ)
n
2

1 + 1
υ x
T R−1x
−υ+n
2
dx1dx2 . . . dxn
The MTC is then defined as follows:
TR,υ(u1, u2, . . . , un) = tR,υ(t−1
υ (u1), t−1
υ (u2), . . . , t−1
υ (un))
=
 t−1
υ (u1)
−∞
 t−1
υ (u2)
−∞
. . .
 t−1
υ (un)
−∞
	
υ + n
2

|R|−1
2
	

υ
2

(υπ)
n
2

1 + 1
υ x
T R−1x
−υ+n
2
dx1dx2 . . . dxn
where t−1
υ
is the inverse of the univariate c.d.f. of Student’s t with υ degrees of freedom.
Using the canonical representation, it turns out that the copula density for the MTC is:
cR,υ(u1, u2, . . . , un) = |R|−1
2
	
υ + n
2

	

υ
2



	

υ
2

	
υ + 1
2



n 
1 + 1
υ ς
T R−1ς
−υ+n
2
n

j=1

1 +
ς2
j
υ
−υ+1
2
where ςj = t−1
υ (uj).

Multivariate Copulas
149
4.8.3
The multivariate dispersion copula
Definition 4.13 [Multivariate dispersion copula (MDC)]
Let µ = (µ1, µ2, . . . , µn)
T be a
position parameter, σ 2 =

σ 2
1 , σ 2
2 , . . . , σ 2
n
	T
a dispersion parameter and R a correlation
matrix. We say that X ∼MDC(µ, σ 2, R) if
f (y; µ, σ 2, R) =
1
|R|
1
2
exp

−1
2ς
T (R−1 −I)ς

n

j=1
fj

yj; µj, σ 2
j

where
ςj = −1 
Fj

yj; µj, σ 2
j

for j = 1, 2, . . . , n
and
fj

yj; µj, σ 2
j

=
∂Fj

yj; µj, σ 2
j

∂yj
for every set of c.d.f. Fj

yj; µj, σ 2
j

Example 4.7
Just for a simple application of this definition, we can construct the MDC
assuming Weibull margins. In such a case we have:
f (x) = αxα−1
β
exp

−xα
β

so we obtain the MDC density:
f (x1, x2, . . . , xn) =
1
|R|
1
2
exp

−1
2ς
T (R−1 −I)ς

n

j=1
αjx
αj −1
j
βj
exp

−
x
αj
j
βj

where
ςj = −1

1 −exp

−
x
αj
j
βj

4.8.4
Archimedean copulas
As in the bi-dimensional case, let us consider a generator function. Assume directly a strict
generator:
ϕ(u) : [0, 1] →[0, ∞]
continuous and strictly decreasing. Define its inverse as in Chapter 2.
The following theorem can be proved:
Theorem 4.10 (Kimberling, 1974)
Let ϕ be a generator. The function C : [0, 1]n →[0, 1]
defined by
C(u1, u2, . . . , un) = ϕ−1(ϕ(u1) + ϕ(u2) + · · · + ϕ(un))
is a copula iff ϕ−1 is completely monotonic on [0, ∞].

