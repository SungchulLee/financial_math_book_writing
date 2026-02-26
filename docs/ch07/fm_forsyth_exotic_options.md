# Exotic Options

!!! info "Source"
    **An Introduction to Computational Finance Without Agonizing Pain** by Peter Forsyth, 2007.
    These notes are used for educational purposes.

## Exotic Options

−0.08
−0.06
−0.04
−0.02
0.02
0.04
−0.1
−0.05
0.05
0.1
0.15
Return on market
Return on stock
Rogers Wireless Communications
Figure 11.4: Return on Rogers Wireless Communications versus return on TSE 300. Each point represents
pairs of daily returns. The vertical axis measures the daily return on the stock and the horizontal axis that
of the TSE300.
Equation (11.46) has the interpretation that the return on asset i can be decomposed into a drift component,
a part which is correlated to the market portfolio (the broad index), and a random part uncorrelated with
the index. Make the following assumptions
E[ϵiϵj]
=
0 ;
i ̸= j
=
e2
i
;
i = j
(11.47)
e.g. that returns on each each asset are correlated only through their correlation with the index. Consider
once again a portfolio where the wealth is divided amongst N assets, each asset receiving a fraction wi of
the initial wealth. In this case, the return on the portfolio is
Rp
=
i=N
X
i=1
wiRi
Rp
=
i=N
X
i=1
wiαi + RM
i=N
X
i=1
wiβi
(11.48)
and
s.d.(Rp)
=
v
u
u
t(σ′
M)2
i=N
X
i=1
j=N
X
j=1
wiwjβiβj +
i=N
X
i=1
w2
i e2
i
=
v
u
u
t(σ′
M)2
 i=N
X
i=1
wiβi
!2
+
i=N
X
i=1
w2
i e2
i
.
(11.49)
Now, if wi = O(1/N), then
i=N
X
i=1
w2
i e2
i
(11.50)
is O(1/N) as N becomes large, hence equation (11.49) becomes
s.d.(Rp)
≃
σ′
M

i=N
X
i=1
wiβi

.
(11.51)
Note that if we write
Ri
=
r′ + λiσ′
i
(11.52)
then we also have that
Ri
=
r′ + βi(RM −r′)
(11.53)
so that the market price of risk of security i is
λi
=
βi(RM −r′)
σ′
i
(11.54)
which is useful in real options analysis.
Stocks for the Long Run?
Conventional wisdom states that investment in a diversified portfolio of equities has a low risk for a long
term investor. However, in a recent article (”Irrational Optimism,” Fin. Anal. J. E. Simson, P.Marsh, M.
Staunton, vol 60 (January, 2004) 25-35) an extensive analysis of historical data of equity returns was carried
out. Projecting this information forward, the authors conclude that the probability of a negative real return
over a twenty year period, for a investor holding a diversified portfolio, is about 14 per cent. In fact, most
individuals in defined contribution pension plans have poorly diversified portfolios. Making more realistic
assumptions for defined contribution pension plans, the authors find that the probability of a negative real
return over twenty years is about 25 per cent.
Let’s see if we can explain why there is this common misconception about the riskiness of long term
equity investing. Table 12.1 shows a typical table in a Mutual Fund advertisement. From this table, we are
supposed to conclude that
• Long term equity investment is not very risky, with an annualized compound return about 3% higher
than the current yield on government bonds.
• If S is the value of the mutual fund, and B is the value of the government bond, then
B(T)
=
B(0)erT
r = .03
S(T)
≃
S(0)eαT
α = .06,
(12.1)
for T large, which gives
S(T =30)
S(0)
B(T =30)
B(0)
=
e1.8−.9 = e.9 ≃2.46,
(12.2)
indicating that you more than double your return by investing in equities compared to bonds (over the
long term).
A convenient way to measure the relative returns on these two investments (bonds and stocks) is to
compare the total compound return
Compound return: stocks
=
log
S(T)
S(0)

= αT
Compound return: bonds
=
log
B(T)
B(0)

= rT ,
(12.3)
1 year
2 years
5 years
10 years
20 years
30 years
30 year bond
yield
-2%
-5%
10%
8%
7%
6%
3%
Table 12.1: Historical annualized compound return, XYZ Mutual Equity Funds. Also shown is the current
yield on a long term government bond.
or the annualized compound returns
Annualized compound return: stocks
=
T log
S(T)
S(0)

= α
Annualized compound return: bonds
=
T log
B(T)
B(0)

= r .
(12.4)
If we assume that the value of the equity portfolio S follows a Geometric Brownian Motion
dS
=
µS dt + σS dZ
(12.5)
then from equation (2.56) we have that
log
S(T)
S(0)

∼N((µ −σ2
2 )T, σ2T) ,
(12.6)
i.e. the compound return in is normally distributed with mean (µ −σ2
2 )T and variance σ2T, so that the
variance of the total compound return increases as T becomes large.
Since var(aX) = a2var(X), it follows that
T log
S(T)
S(0)

∼N((µ −σ2
2 ), σ2/T) ,
(12.7)
so that the the variance of the annualized return tends to zero at T becomes large.
Of course, what we really care about is the total compound return (that’s how much we actually have at
t = T, relative to what we invested at t = 0) at the end of the investment horizon. This is why Table 12.1
is misleading. There is significent risk in equities, even over the long term (30 years would be long-term for
most investors).
Figure 12.1 shows the results of 100, 000 simulations of asset prices assuming that the asset follows
equation (12.5), with µ = .08, σ = .2. The investment horizon is 5 years. The results are given in terms of
histograms of the annualized compound return (equation (12.4)) and the total compound return ((equation
(12.3)).
Figure 12.2 shows similar results for an investment horizon of 30 years. Note how the variance of the
annualized return has decreased, while the variance of the total return has increased (verifying equations
(12.6-12.7)).
Assuming long term bonds yield 3%, this gives a total compound return over 30 years of .90, for bonds.
Looking at the right hand panel of Figure 12.2 shows that there are many possible scenarios where the return
on equities will be less than risk free bonds after 30 years. The number of scenarios with return less than
risk free bonds is given by the area to the left of .9 in the histogram.
Further Reading
13.1
General Interest
• Peter Bernstein, Capital Ideas: the improbable origins of modern Wall street, The Free Press, New
York, 1992.
−0.8
−0.6
−0.4
−0.2
0.2
0.4
0.6
0.8
0.5
1.5
2.5
x 10
Annualized Returns − 5 years
Ann. Returns ($)
−3
−2
−1
1
3
5
0.2
0.4
0.6
0.8
1.2
1.4
1.6
1.8
x 10
Log Returns − 5 years
Log Returns ($)
Figure 12.1: Histogram of distribution of returns T = 5 years. µ = .08, σ = .2, 100, 000 simulations. Left:
annualized return 1/T log[S(T)/S(0)]. Right: return log[S(T)/S(0)].
−0.8
−0.6
−0.4
−0.2
0.2
0.4
0.6
0.8
0.5
1.5
2.5
x 10
Annualized Returns − 30 years
Ann. Returns ($)
−3
−2
−1
1
3
5
0.2
0.4
0.6
0.8
1.2
1.4
1.6
1.8
x 10
Log Returns − 30 years
Log Returns ($)
Figure 12.2: Histogram of distribution of returns T = 30 years. µ = .08, σ = .2, 100, 000 simulations. Left:
annualized return 1/T log[S(T)/S(0)]. Right: return log[S(T)/S(0)],
• Peter Bernstein, Against the Gods: the remarkable story of risk, John Wiley, New York, 1998, ISBN
0-471-29563-9.
• Burton Malkeil, A random walk down Wall Street, W.W. Norton, New York, 1999, ISBN 0-393-32040-5.
• N. Taleb, Fooled by Randomness, Texere, 2001, ISBN 1-58799-071-7.
13.2
More Background
• A. Dixit and R. Pindyck, Investment under uncertainty, Princeton University Press, 1994.
• John Hull, Options, futures and other derivatives, Prentice-Hall, 1997, ISBN 0-13-186479-3.
• S. Ross, R. Westerfield, J. Jaffe, Corporate Finance, McGraw-Hill Irwin, 2002, ISBN 0-07-283137-5.
• W. Sharpe, Portfolio Theory and Capital Markets, Wiley, 1970, reprinted in 2000, ISBN 0-07-135320-8.
(Still a classic).
• Lenos Triegeorgis, Real Options: Managerial Flexibility and Strategy for Resource Allocation, MIT
Press, 1996, ISBN 0-262-20102-X.
13.3
More Technical
• P. Brandimarte, Numerical Methods in Finance: A Matlab Introduction, Wiley, 2002, ISBN 0-471-
39686-9.
• Boyle, Broadie, Glassermman, Monte Carlo methods for security pricing, J. Econ. Dyn. Con., 21:1267-
1321 (1997)
• P. Glasserman, Monte Carlo Methods in Financial Engineering, Springer (2004) ISBN 0-387-00451-3.
• D. Higham, An Introduction to Financial Option Valuation, Cambridge (2004) ISBN 0-521-83884-3.
• P. Jackel, Monte Carlo Methods in Finance, Wiley, 2002, ISBN 0-471-49741-X.
• Y.K. Kwok, Mathematical Models of Finance, Springer Singapore, 1998, ISBN 981-3083-565.
• S. Neftci, An Introduction to the Mathematics of Financial Derivatives, Academic Press (2000) ISBN
0-12-515392-9.
• R. Seydel, Tools for Computational Finance, Springer, 2002, ISBN 3-540-43609-X.
• D. Tavella and C. Randall, Pricing Financial Instruments: the Finite Difference Method, Wiley, 2000,
ISBN 0-471-19760-2.
• D. Tavella, Quantitative Methods in Derivatives Pricing: An Introduction to Computational Finance,
Wiley (2002) ISBN 0-471-39447-5.
• N. Taleb, Dynamic Hedging, Wiley, 1997, ISBN 0-471-15280-3.
• P. Wilmott, S. Howison, J. Dewynne, The mathematics of financial derivatives: A student introduction,
Cambridge, 1997, ISBN 0-521-49789-2.
• Paul Wilmott, Paul Wilmott on Quantitative Finance, Wiley, 2000, ISBN 0-471-87438-8.
pdflatex version

