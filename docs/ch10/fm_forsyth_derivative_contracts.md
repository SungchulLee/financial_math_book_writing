# Derivative Contracts on Non-Traded Assets

!!! info "Source"
    **An Introduction to Computational Finance Without Agonizing Pain** by Peter Forsyth, 2007.
    These notes are used for educational purposes.

## Derivative Contracts on Non-Traded Assets and Real Options

or
lim
∆t→0 E
"X
cj∆Z2
j −
Z t
c(s, X(s))ds
2#
=
(6.24)
so that in this sense we can write
dZ2
→
dt ;
dt →0 .
(6.25)
Derivative Contracts on non-traded Assets and Real Options
The hedging arguments used in previous sections use the underlying asset to construct a hedging portfolio.
What if the underlying asset cannot be bought and sold, or is non-storable? If the underlying variable is
an interest rate, we can’t store this. Or if the underlying asset is bandwidth, we can’t store this either.
However, we can get around this using the following approach.
7.1
Derivative Contracts
Let the underlying variable follow
dS
=
a(S, t)dt + b(S, t)dZ,
(7.1)
and let F = F(S, t), so that from Ito’s Lemma
dF
=

aFS + b2
2 FSS + Ft

dt + bFSdZ,
(7.2)
or in shorter form
dF
=
µdt + σ∗dZ
µ = aFS + b2
2 FSS + Ft
σ∗= bFS .
(7.3)
Now, instead of hedging with the underlying asset, we will hedge one contract with another. Suppose we
have two contracts F1, F2 (they could have different maturities for example). Then
dF1
=
µ1dt + σ∗
1dZ
dF2
=
µ2dt + σ∗
2dZ
µi = a(Fi)S + b2
2 (Fi)SS + (Fi)t
σ∗
i = b(Fi)S ;
i = 1, 2 .
(7.4)
Consider the portfolio Π
Π = n1F1 + n2F2
(7.5)
so that
dΠ
=
n1 dF1 + n2 dF2
=
n1(µ1 dt + σ∗
1 dZ) + n2(µ2 dt + σ∗
2 dZ)
=
(n1µ1 + n2µ2) dt + (n1σ∗
1 + n2σ∗
2) dZ .
(7.6)
Now, to eliminate risk, choose
(n1σ∗
1 + n2σ∗
2) = 0
(7.7)
which means that Π is riskless, hence
dΠ
=
rΠ dt ,
(7.8)
so that, using equations (7.6-7.8), we obtain
(n1µ1 + n2µ2)
=
r(n1F1 + n2F2).
(7.9)
Putting together equations (7.7) and (7.9) gives

σ∗
σ∗
µ1 −rF1
µ2 −rF2
 
n1
n2

=

0

.
(7.10)
Now, equation (7.10) only has a nonzero solution if the two rows of equation (7.10) are linearly dependent.
In other words, there must be a λS = λS(S, t) (independent of the type of contract) such that
µ1 −rF1
=
λSσ∗
µ2 −rF2
=
λSσ∗
2 .
(7.11)
Dropping the subscripts, we obtain
µ −rF
σ∗
=
λS
(7.12)
Substituting µ, σ∗from equations (7.3) into equation (7.12) gives
Ft + b2
2 FSS + (a −λSb)FS −rF = 0 .
(7.13)
Equation (7.13) is the PDE satisfied by a derivative contract on any asset S. Note that it does not matter
if we cannot trade S.
Suppose that F2 = S is a traded asset. Then we can hedge with S, and from equation (7.11) we have
µ2 −rS
=
λSσ∗
(7.14)
and from equations (7.1) and (7.3) we have
σ∗
=
b
µ2
=
a
(7.15)
and so, using equations (7.11) and (7.15) , we have that
λS
=
a −rS
b
(7.16)
and equation (7.13) reduces to
Ft + b2
2 FSS + rSFS −rF = 0 .
(7.17)
Suppose
µ
=
Fµ′
σ∗
=
Fσ′
(7.18)
so that we can write
dF
=
Fµ′dt + Fσ′dZ
(7.19)
then using equation (7.18) in equation (7.12) gives
µ′
=
r + λSσ′
(7.20)
which has the convenient interpretation that the expected return on holding (not hedging) the derivative
contract F is the risk-free rate plus extra compensation due to the riskiness of holding F. The extra return
is λSσ′, where λS is the market price of risk of S (which should be the same for all contracts depending on
S) and σ′ is the volatility of F. Note that the volatility and drift of F are not the volatility and drift of the
underlying asset S.
If we believe that the Capital Asset Pricing Model holds, then a simple minded idea is to estimate
λS = ρSMλM
(7.21)
where λM is the price of risk of the market portfolio, and ρSM is the correlation of returns between S and
the returns of the market portfolio.
Another idea is the following. Suppose we can find some companies whose main source of business is
based on S. Let qi be the price of this companies stock at t = ti. The return of the stock over ti −ti−1 is
Ri
=
qi −qi−1
qi−1
.
Let RM
i
be the return of the market portfolio (i.e. a broad index) over the same period. We compute β as
the best fit linear regression to
Ri
=
α + βRM
i
which means that
β
=
Cov(R, RM)
V ar(RM) .
(7.22)
Now, from CAPM we have that
E(R)
=
r + β

E(RM) −r

(7.23)
where E(...) is the expectation operator. We would like to determine the unlevered β, denoted by βu, which
is the β for an investment made using equity only. In other words, if the firm we used to compute the β
above has significant debt, its riskiness with respect to S is amplified. The unlevered β can be computed by
βu
=
E
E + (1 −Tc)Dβ
(7.24)
where
D
=
long term debt
E
=
Total market capitalization
Tc
=
Corporate Tax rate .
(7.25)
So, now the expected return from a pure equity investment based on S is
E(Ru)
= r+
βu 
E(RM) −r

.
(7.26)
If we assume that F in equation (7.19) is the company stock, then
µ′
=
E(Ru)
=
r + βu 
E(RM) −r

(7.27)
But equation (7.20) says that
µ′
=
r + λSσ′ .
(7.28)
Combining equations (7.27-7.27) gives
λSσ′
=
βu 
E(RM) −r

.
(7.29)
Recall from equations (7.3) and (7.18) that
σ∗
=
Fσ′
σ∗
=
bFS ,
or
σ′
=
bFS
F
.
(7.30)
Combining equations (7.29-7.30) gives
λS
=
βu 
E(RM) −r

bFS
F
.
(7.31)
In principle, we can now compute λS, since
• The unleveraged βu is computed as described above. This can be done using market data for a specific
firm, whose main business is based on S, and the firms balance sheet.
• b(S, t)/S is the volatility rate of S (equation (7.1)).
• [E(RM) −r] can be determined from historical data. For example, the expected return of the market
index above the risk free rate is about 6% for the past 50 years of Canadian data.
• The risk free rate r is simply the current T-bill rate.
• FS can be estimated by computing a linear regression of the stock price of a firm which invests in
S, and S. Now, this may have to be unlevered, to reduce the effect of debt. If we are going to now
value the real option for a specific firm, we will have to make some assumption about how the firm will
finance a new investment. If it is going to use pure equity, then we are done. If it is a mixture of debt
and equity, we should relever the value of FS. At this point, we need to talk to a Finance Professor to
get this right.
7.2
A Forward Contract
A forward contract is a special type of derivative contract. The holder of a forward contract agrees to buy or
sell the underlying asset at some delivery price K in the future. K is determined so that the cost of entering
into the forward contract is zero at its inception.
The payoffof a (long) forward contract expiring at t = T is then
V (S, τ = 0)
=
S(T) −K .
(7.32)
Note that there is no optionality in a forward contract.
The value of a forward contract is a contingent claim. and its value is given by equation (7.13)
Vt + b2
2 VSS + (a −λSb)VS −rV = 0 .
(7.33)
Now we can also use a simple no-arbitrage argument to express the value of a forward contract in terms
of the original delivery price K, (which is set at the inception of the contract) and the current forward price
f(S, τ). Suppose we are long a forward contract with delivery price K. At some time t > 0, (τ < T), the
forward price is no longer K. Suppose the forward price is f(S, τ), then the payoffof a long forward contract,
entered into at (τ) is
Payoff
=
S(T) −f(S(τ), τ) .
Suppose we are long the forward contract struck at t = 0 with delivery price K. At some time t > 0, we
hedge this contract by going short a forward with the current delivery price f(S, τ) (which costs us nothing
to enter into). The payoffof this portfolio is
S −K −(S −f) = f −K
(7.34)
Since f, K are known with certainty at (S, τ), then the value of this portfolio today is
(f −K)e−rτ .
(7.35)
But if we hold a forward contract today, we can always construct the above hedge at no cost. Therefore,
V (S, τ)
=
(f −K)e−rτ .
(7.36)
Substituting equation (7.36) into equation (7.33), and noting that K is a constant, gives us the following
PDE for the forward price (the delivery price which makes the forward contract worth zero at inception)
fτ = b2
2 fSS + (a −λSb)fS
(7.37)
with terminal condition
f(S, τ = 0) = S
(7.38)
which can be interpreted as the fact that the forward price must equal the spot price at t = T.
Suppose we can estimate a, b in equation (7.37), and there are a set of forward prices available. We can
then estimate λS by solving equation (7.37) and adjusting λS until we obtain a good fit for the observed
forward prices.
7.2.1
Convenience Yield
We can also write equation (7.37) as
ft + b2
2 fSS + (r −δ)SfS = 0
(7.39)
where δ is defined as
δ = r −a −λSb
S
.
(7.40)
In this case, we can interpret δ as the convenience yield for holding the asset.
For example, there is a
convenience to holding supplies of natural gas in reserve.
7.2.2
Volatility of Foward Prices
From equation (7.37) we have that the forward price for a contract expiring at time T, at current time t,
spot price S(t) is given by
f(S, t)
=
EQ[S(T)]
(7.41)
where S follows the risk neutral process
dS
=
(a −λSb) dt + b dZ .
(7.42)
In other words. the forward price is the risk neutral expected spot price at expiry.
Now, using Ito’s Lemma and assuming the risk neutral spot process (7.42) gives
df
=
 ft + b2
2 fSS + (a −λSb)fS

dt + fSb dZ .
(7.43)
But since f satisfies equation (7.37), equation (7.43) becomes
df
=
fSb dZ
=
ˆσf dZ ,
(7.44)
where the effective volatility of the foward price is
ˆσ = fSb
f
.
(7.45)
Note that from equation (7.44), the forward price has zero drift.
Discrete Hedging
In practice, we cannot hedge at infinitesimal time intervals. In fact, we would like to hedge as infrequently as
possible, since in real life, there are transaction costs (something which is ignored in the basic Black-Scholes
equation, but which can be taken into account and results in a nonlinear PDE).
8.1
Delta Hedging
Recall that the basic derivation of the Black-Scholes equation used a hedging portfolio where we hold VS
shares. In finance, VS is called the option delta, hence this strategy is called delta hedging.
As an example, consider the hedging portfolio P(t) which is composed of
• A short position in an option −V (t).
• Long α(t)hS(t) shares
• An amount in a risk-free bank account B(t).
Initially, we have
P(0) = 0
=
−V (0) + α(0)hS(0) + B(0)
α = VS
B(0) = V (0) −α(0)hS(0)
The hedge is rebalanced at discrete times ti. Defining
αh
i
=
VS(Si, ti)
Vi
=
V (Si, ti)
then, we have to update the hedge by purchasing αi −αi−1 shares at t = ti, so that updating our share
position requires
S(ti)(αh
i −αh
i−1)
in cash, which we borrow from the bank if (αh
i −αh
i−1) > 0. If (αh
i −αh
i−1) < 0, then we sell some shares and
deposit the proceeds in the bank account. If ∆t = ti −ti−1, then the bank account balance is updated by
Bi = er∆tBi−1 −Si(αh
i −αh
i−1)
At the instant after the rebalancing time ti, the value of the portfolio is
P(ti) = −V (ti) + α(ti)hS(ti) + B(ti)
Since we are hedging at discrete time intervals, the hedge is no longer risk free (it is risk free only in the
limit as the hedging interval goes to zero). We can determine the distribution of profit and loss ( P& L) by
carrying out a Monte Carlo simulation. Suppose we have precomputed the values of VS for all the likely (S, t)
values. Then, we simulate a series of random paths. For each random path, we determine the discounted
relative hedging error
error
=
e−rT ∗P(T ∗)
V (S0, t = 0)
(8.1)
After computing many sample paths, we can plot a histogram of relative hedging error, i.e. fraction of Monte
Carlo trials giving a hedging error between E and E+∆E. We can compute the variance of this distribution,
and also the value at risk (VAR). VAR is the worst case loss with a given probability. For example, a typical
VAR number reported is the maximum loss that would occur 95% of the time. In other words, find the value
of E along the x-axis such that the area under the histogram plot to the right of this point is .95× the total
area.
As an example, consider the case of an American put option, T = .25, σ = .3, r = .06, K = S0 = 100. At
t = 0, S0 = 100. Since there are discrete hedging errors, the results in this case will depend on the stock drift
rate, which we set at µ = .08. The initial value of the American put, obtained by solving the Black-Scholes
linear complementarity problem, is $5.34. Figure 8.1 shows the results for no hedging, and hedging once
a month. The x-axis in these plots shows the relative P & L of this portfolio (i.e. P & L divided by the
Black-Scholes price), and the y-axis shows the relative frequency.
Relative P& L
=
Actual P& L
Black-Scholes price
(8.2)
Note that the no-hedging strategy actually has a high probability of ending up with a profit (from the
option writer’s point of view) since the drift rate of the stock is positive. In this case, the hedger does
nothing, but simply pockets the option premium. Note the sudden jump in the relative frequency at relative
P&L = 1. This is because the maximum the option writer stands to gain is the option premium, which
we assume is the Black-Scholes value. The writer makes this premium for any path which ends up S > K,
which is many paths, hence the sudden jump in probability. However, there is significant probability of a
loss as well. Figure 8.1 also shows the relative frequency of the P&L of hedging once a month (only three
times during the life of the option).
In fact, there is a history of Ponzi-like hedge funds which simply write put options with essentially no
hedging. In this case, these funds will perform very well for several years, since markets tend to drift up on
average. However, then a sudden market drop occurs, and they will blow up. Blowing up is a technical term
for losing all your capital and being forced to get a real job. However, usually the owners of these hedge
funds walk away with large bonuses, and the shareholders take all the losses.
Figure 8.2 shows the results for rebalancing the hedge once a week, and daily. We can see clearly here
that the mean is zero, and variance is getting smaller as the hedging interval is reduced. In fact, one can
show that the standard deviation of the hedge error should be proportional to
√
∆t where ∆t is the hedge
rebalance frequency.
0
0.5
1.5
2.5
3.5
-3
-2.5
-2
-1.5
-1
-0.5
0.5
Relative frequency
Relative hedge error
0.5
1.5
2.5
3.5
-3
-2.5
-2
-1.5
-1
-0.5
0.5
Relative frequency
Relative hedge error
Figure 8.1: Relative frequency (y-axis) versus relative P&L of delta hedging strategies. Left: no hedging,
right: rebalance hedge once a month. American put, T = .25, σ = .3, r = .06, µ = .08, K = S0 = 100. The
relative P&L is computed by dividing the actual P&L by the Black-Scholes price.
0.5
1.5
2.5
3.5
-3
-2.5
-2
-1.5
-1
-0.5
0.5
Relative frequency
Relative hedge error
0.5
1.5
2.5
3.5
-3
-2.5
-2
-1.5
-1
-0.5
0.5
Relative frequency
Relative hedge error
Figure 8.2: Relative frequency (y-axis) versus relative P&L of delta hedging strategies. Left: rebalance hedge
once a week, right: rebalance hedge daily. American put, T = .25, σ = .3, r = .06, µ = .08, K = S0 = 100.
The relative P&L is computed by dividing the actual P&L by the Black-Scholes price.
8.2
Gamma Hedging
In an attempt to account for some the errors in delta hedging at finite hedging intervals, we can try to use
second derivative information. The second derivative of an option value VSS is called the option gamma,
hence this strategy is termed delta-gamma hedging.
A gamma hedge consists of
• A short option position −V (t).
• Long αhS(t) shares
• Long β another derivative security I.
• An amount in a risk-free bank account B(t).
Now, recall that we consider αh, β to be constant over the hedging interval (no peeking into the future),
so we can regard these as constants (for the duration of the hedging interval).
The hedge portfolio P(t) is then
P(t) = −V + αhS + βI + B(t)
Assuming that we buy and hold αh shares and β of the secondary instrument at the beginning of each
hedging interval, then we require that
∂P
∂S
=
−∂V
∂S + αh + β ∂I
∂S = 0
∂2P
∂S2
=
−∂2V
∂S2 + β ∂2I
∂S2 = 0
(8.3)
Note that
• If β = 0, then we get back the usual delta hedge.
• In order for the gamma hedge to work, we need an instrument which has some gamma (the asset S has
second derivative zero). Hence, traders often speak of being long (positive) or short (negative) gamma,
and try to buy/sell things to get gamma neutral.
So, at t = 0 we have
P(0)
=
0 ⇒B(0) = V (0) −αh
0S0 −β0I0
The amounts αh
i , βi are determined by requiring that equation (8.3) hold
−(VS)i + αh
i + βi(IS)i
=
−(VSS)i + βi(ISS)i
=
(8.4)
The bank account balance is then updated at each hedging time ti by
Bi
=
er∆tBi−1 −Si(αh
i −αh
i−1) −Ii(βi −βi−1)
We will consider the same example as we used in the delta hedge example. For an additional instrument,
we will use a European put option written on the same underlying with the same strike price and a maturity
of T=.5 years.
Figure 8.3 shows the results of gamma hedging, along with a comparison on delta hedging. In principle,
gamma hedging produces a smaller variance with less frequent hedging. However, we are exposed to more
model error in this case, since we need to be able to compute the second derivative of the theoretical price.
0
10
20
30
40
-3
-2.5
-2
-1.5
-1
-0.5
0.5
Relative frequency
Relative hedge error
5
15
25
35
-3
-2.5
-2
-1.5
-1
-0.5
0.5
Relative frequency
Relative hedge error
Figure 8.3: Relative frequency (y-axis) versus relative P&L of gamma hedging strategies. Left: rebalance
hedge once a week, right: rebalance hedge daily. Dotted lines show the delta hedge for comparison. American
put, T = .25, σ = .3, r = .06, µ = .08, K = 100, S0 = 100. Secondary instrument: European put option,
same strike, T = .5 years. The relative P&L is computed by dividing the actual P&L by the Black-Scholes
price.
8.3
Vega Hedging
The most important parameter in the option pricing is the volatility. What if we are not sure about the
value of the volatility? It is possible to assume that the volatility itself is stochastic, i.e.
dS
=
µSdt + √vSdZ1
dv
=
κ(θ −v)dt + σv
√vdZ2
(8.5)
where µ is the expected growth rate of the stock price, √v is its instantaneous volatility, κ is a parameter
controlling how fast v reverts to its mean level of θ, σv is the “volatility of volatility” parameter, and Z1, Z2
are Wiener processes with correlation parameter ρ.
If we use the model in equation (8.5), the this will result in a two factor PDE to solve for the option price
and the hedging parameters. Since there are two sources of risk (dZ1, dZ2), we will need to hedge with the
underlying asset and another option (Heston, A closed form solution for options with stochastic volatility
with applications to bond and currency options, Rev. Fin. Studies 6 (1993) 327-343).
Another possibility is to assume that the volatility is uncertain, and to assume that
σmin ≤σ ≤σmax,
and to hedge based on a worst case (from the hedger’s point of view). This results in an uncertain volatil-
ity model (Avellaneda, Levy, Paris, Pricing and Hedging Derivative Securities in Markets with Uncertain
Volatilities, Appl. Math. Fin. 2 (1995) 77-88). This is great if you can get someone to buy this option at
this price, because the hedger is always guaranteed to end up with a non-negative balance in the hedging
portfolio. But you may not be able to sell at this price, since the option price is expensive (after all, the
price you get has to cover the worst case scenario).
An alternative, much simpler, approach (and therefore popular in industry), is to construct a vega hedge.
We assume that we know the volatility, and price the option in the usual way. Then, as with a gamma
hedge, we construct a portfolio
• A short option position −V (t).
• Long αhS(t) shares
• Long β another derivative security I.

