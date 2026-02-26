# Stochastic Volatility & Financial Risk

!!! info "Source"
    **Financial Econometrics: From Basics to Advanced Modeling Techniques** edited by Greg N. Gregoriou and Razvan Pascalau, Wiley, 2009.
    These notes are used for educational purposes.

## Stochastic Volatility and Risk Models

136
M. Modena
amplitude (A) and the phase shift (θ). The cyclical component is thus
expressed as follows:
ψt = Acos(λt −θ)
(7.10)
A complete formulation representing the cycle combines both the sine
and the cosine waves:
ψt = acos(λt) + bsin(λt)
(7.11)
The time series of the IP cycle thus can be seen as the summation of the
above cyclical component plus a white noise error term with zero mean. A
stochastic pattern for the cycle requires parameters a and b to evolve over
time; to preserve time series continuity we adopt the following recursion:

ψt
ψ∗
t

=
 cosλ
sinλ
−sinλ
cosλ

ψt−1
ψ∗
t−1

+

κt
κ∗
t

(7.12)
with initial states ψ0 = a and ψ∗
0 = b; and, where κt and κ∗
t are white
noise disturbances. The model is identified if either we assume that two
disturbances have the same variance or if they are uncorrelated. Finally,
we introduce a dumping factor (ρ) affecting the amplitude of the cycle in
order to allow for more flexibility. System (7.13) summarizes the entire
structural model for IP:


µt
βt
ψt
ψ∗
t

=


1
0
0
0
1
1
0
0
0
0
ρ cosλ
−ρ sinλ
0
0
ρ sinλ
ρ cosλ




µt−1
βt−1
ψt−1
ψ∗
t−1

+


ηt
ςt
κt
κ∗
t


(7.13)
Equation (7.13) is the state, or transition, equation of the state-space
representation. The transition matrix on RHS describes the evolution of
the unobservable components so that it captures the stochastic behavior
of both the trend and the cycle.
The seasonal component is excluded from the model since we use the
seasonally adjusted IP series. IP is thus decomposed into a trend and
a cycle (plus a residual component). The model is estimated using the
Kalman filter for both the level of the seasonally adjusted IP series and
for its log transformation. The estimation of the amplitude is 0.9357
(p-value: 0); it is a stable solution (|ρ| < 1) that denotes a cycle with
decreasing amplitude (i.e., convergence).10
Diagrams in Figure 7.4 plot the cyclical component together with dif-
ferent indicators of the business cycle. There is a positive and significant

Latent Factors of the Yield Curve
137
–6
–4
–2
0
2
4
6
88 90 92 94 96 98 00 02 04 06
cycle prediction
gap HP
–6
–4
–2
0
2
4
6
88 90 92 94 96 98 00 02 04 06
cycle prediction
gap BK
–6
–4
–2
0
2
4
6
88 90 92 94 96 98 00 02 04 06
cycle prediction
unempl. growth
Figure 7.4
Cycle prediction and cyclical variables
Notes: Cycle prediction: cyclical component of the structural model; gap HP: IP
gap obtained with the Hodrick–Prescott filter; gap BK: IP gap obtained with the
Baxter King filter; unempl. growth: rate of growth of the unemployment rate.
relationship with the output gap computed applying both the Hodrick-
Prescott and the Baxter-King frequency filters; while, there is an evident
inverse relation with the annual5, instead, shows that the IP cyclical
component is highly correlated with the curvature factor one-year ahead.
The correlation coefficient is about 0.71. Moreover, curvature lies within
the forecast standard error bands only except for periods of economic
downturn, when it slightly crosses the bands downward. The central and
the right panels of Figure 7.5 plot respectively the deviations between
curvature and the cycle prediction and the associated correlogram. The
forecast errors series is stationary, as suggested by both the autocorrela-
tion function. Stationarity of the forecast errors series is also supported by
unit root tests; both the ADF and the Phillips–Perron tests reject the null
hypothesis of unit root. In addition, the KPSS test confirms stationarity.

138
M. Modena
–0.15
–0.10
–0.05
0.00
0.05
0.10
0.15
88 90 92 94 96 98 00 02 04 06
cycle prediction
std errors
curvature
–1.0
–0.5
0.0
0.5
1.0
88 90 92 94 96 98 00 02 04 06
deviations
–1.0
–0.5
0.0
0.5
1.0
5
10
15
20
25
30
35
ACF (deviations)
Figure 7.5
Cycle prediction and curvature (nominal TS); autocorrelogram of the
deviations
Notes: Cycle prediction: cyclical component of the structural model; std errors:
curvature: standard errors of the prediction; curvature: curvature factor; devia-
tions: difference between curvature and its prediction; ACF(deviations): autocor-
relogram of the deviation series.
We also compare the cyclical component with curvature from the real
TS. The correlation coefficient between the series is almost 0.70. The
left panel of the diagram below highlights how similar the path of both
series are. The central diagram shows the discrepancies between the cur-
vature and the predicted cycle and the right diagram plots the associated
autocorrelogram (Figure 7.6).
7.7
A joint macroeconometric model for curvature and
industrial production
To provide more evidence about the economic relationship between cur-
vature and the business cycle, in this section we develop and estimate

Latent Factors of the Yield Curve
139
–0.15
–0.10
–0.05
0.00
0.05
0.10
0.15
88 90 92 94 96 98 00 02 04 06
cycle prediction
for s.e.
real TS curvature
–2
–1
0
1
2
88 90 92 94 96 98 00 02 04 06
deviations (real TS)
–1.0
–0.5
0.0
0.5
1.0
5
10
15
20
25
30
35
ACF (deviations)
Figure 7.6
Cycle prediction and curvature (real TS); autocorrelogram of the
deviations
Notes: Cycle prediction: cyclical component of the structural model; std errors:
curvature: standard errors of the prediction; curvature: curvature factor; devia-
tions: difference between curvature and its prediction; ACF(deviations): autocor-
relogram of the deviation series.
a joint structural macroeconometric model for both curvature and IP.11
The measurement equations are summarized by the following system:

log (ipt)

curt

−

1
0
1
0
1
0
1
0



µt
βt
ψt
ψ∗
t

+

εt
εc,t

(7.14)
where 
curt is the simulated trended curvature series. In the model above
we assume that both trends follow first-order integrated stochastic pro-
cesses, while the cyclical components are a combination of sine and

140
M. Modena
cosine waves. The model structure is:


µt
βt
ψt
ψ∗
t
µc,t
βc,t
ψc,t
ψ∗
c,t


=


1
1
0
0
0
0
0
0
0
1
0
0
0
0
0
0
0
0
ρ cosλ
ρ sinλ
0
0
0
0
0
0
−ρ sinλ
ρ cosλ
0
0
0
0
0
0
0
0
1
1
0
0
0
0
0
0
0
1
0
0
0
0
0
0
0
0
ρc cosλ
ρc sinλ
0
0
0
0
0
0
−ρc sinλ
ρc cosλ




µt−1
βt−1
ψt−1
ψ∗
t−1
µc,t−1
βc,t−1
ψc,t−1
ψ∗
c,t−1


+


ηt
ςt
κt
κ∗
t
ηc,t
ςc,t
κc,t
κ∗
c,t


(7.15)
The model has been estimated with data from 1987 to 2007. The esti-
mated amplitude of the cycle is 0.9311 for IP (ρ) and 0.7741 for the
simulated curvature factor (ρc). These results are coherent with a decreas-
ing amplitude of the cycle, that is, stability. The covariance between
the cycles has been imposed to be approximately zero. The left dia-
gram in Figure 7.7 shows the evolution over time of both the predicted
–0.05
0.00
0.05
0.10
0.15
–0.04
–0.02
0.00
0.02
1992 1994 1996 1998 2000 2002 2004 2006
IP grw
IP gap HP
cycle CUR KF prediction
cycle KF prediction
–0.08
–0.04
0.00
0.04
0.08
0.12
–0.03
–0.02
–0.01
0.00
0.01
0.02
88
90
92
94
96
98
00
02
04
06
IP grw
IP gap HP
cycle r-cur KF est
cycle r-cur KF pred
cycle IP KF est
cycle IP KF pred 
Figure 7.7
Cyclical indicators and curvature
Notes: IP grw: rate of growth of the industrial production index; IP gap HP:
industrial production gap obtained with the Hodrick–Prescott filter; cycle CUR
KF prediction: curvature prediction obtained by Kalman filtering the structural
model; cycle KF prediction: cyclical component obtained by Kalman filtering the
structural model.

Latent Factors of the Yield Curve
141
states of the cycle (right scale) and the cyclical indicators (left scale).
Co-movements with the IP growth and the IP gap (HP filtered) are
important.
As far as the trend component is concerned, Figure 7.8 plots the esti-
mated deterministic trend of log IP and the trend series obtained after
Kalman filtering the joint model. The predicted series displays a slightly
larger variance than the estimated one; both series fluctuate regularly
around the deterministic time trend though. We now show how the
decomposition of the SA series of log IP into a cyclical component and
4.0
4.2
4.4
4.6
4.8
5.0
88 90 92 94 96 98 00 02 04 06
KF predicted trend
KF estimated trend
log(IP) trend 
–0.04
–0.02
0.00
0.02
0.04
88 90 92 94 96 98 00 02 04 06
log(IP) Observation Eq. errors
–1.0
–0.5
0.0
0.5
1.0
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
correlogram
Figure 7.8
Industrial production trend
Notes: KF predicted trend: Kalman filtered trend prediction; KF estimated trend:
Kalman filtered estimation of the trend; log (IP) trend: log series of the IP trend;
log (IP) Observation Eq. errors: residual of the observation equation of model
(7.14) and its correlogram.

142
M. Modena
a trend reliable is. We thus consider the error term of the measurement
equation for log IP, that is εz in equation (7.15).
Residuals are covariance stationary (ADF, Phillips–Perron, KPSS). The
correlogram confirms the noise series is stationary. The Jarque and Bera
test suggests the normal distribution of residuals.12 Before conclud-
ing, we repeat the same experiment using the curvature series obtained
from the real TS. The simulated trended curvature series is obtained as
described above. The estimated dumping factor that affects the ampli-
tude of the cycle is 0.9365 for IP (ρ) and 0.6926 for simulated curvature
(ρc). The right panel of Figure 7.8 shows both the predicted and estimated
states of the cycle together with the annual IP growth rate and the out-
put gap (constructed by removing the HP filtered log IP from the actual
series). There is an evident relationship between the series extracted by
Kalman filtering and the real economic indicators.
7.8
Conclusion
Both macroeconomists and financial economists have always paid
scrupulous attention to the bidirectional relation linking macroeco-
nomics and finance. The yield curve certainly represents an appealing
bridge to explore the aforementioned relation. In this vein, TS mod-
els provide an effective framework to summarize in few factors all the
information contained in the yield curve, which is regarded to be a lead-
ing economic indicator. So far, the empirical literature has expressed a
certain consensus about the macroeconomic interpretation of only two
components underlying TS, namely the level and the slope. The former
is associated to the rate of inflation targeted by the monetary authority,
while the latter is considered a sign of the monetary policy stance. This
study offers a refinement of traditional TS factor-models since we mainly
focus on the third latent factor.
Working with US data we provide significant evidence that curva-
ture reflects the cyclical behavior of the economy, as represented by the
dynamics of unemployment and IP. We find evidence, in fact, that a
negative shock to curvature seems either to anticipate or to accompany
a slowdown in economic activity. The curvature effect thus appears to
complement the transition from an upward-sloping to a flat yield curve.
Interestingly, our main result holds despite the fact that the curvature
factor is extracted from the real or the nominal TS of interest rates. In
particular, US data also suggest that curvature from the real TS is related
to consumption growth.

Latent Factors of the Yield Curve
143
Notes
1. Dewachter et al. (2006) find evidence that a shock to the central tendency
of real interest rates exerts a significant effect on intermediate maturities of
the yield curve. Dewachter and Lyrio (2002) suggest that curvature repre-
sents a clear independent monetary policy factor; in particular, curvature
reflects movements of the real interest rates that are orthogonal to any other
macroeconomic variables. They also argue that the slope reflects business
cycle conditions.
2. To match the monthly frequency of data 12 is the selected number of lags in
the auxiliary regression. Automatic lag selection (Akaike, Schwarz, Hannan-
Quinn criteria) leads to similar results. KPSS critical values (including intercept
and trend) are 0.216, 0.146, and 0.119 at 1%, 5%, and 10% significance levels
respectively. We cannot reject the null of stationarity when the empirical KPSS
statistics (reported in the Table) is below the critical values.
3. Nelson and Siegel suggest fixing it equal to 0.06, the value that maximizes
the third loading. Following Diebold, Rudebusch and Aruoba (2006) we fix it
equal to 0.077.
4. The theoretical measure of curvature proposed by Ang and Piazzesi (2003)
is computed as y(1m)+y(60m)-2*y(12m), where m indicate the maturity in
months. Bekaert, Cho and Moreno (2005) propose y(3m)+y(60m)-2*y(12m).
Finally, Nelson and Siegel (1987), as well as Diebold and Li (2006), and
Diebold, Rudebusch and Aruoba (2006), compute the curvature as 2*(y24m)-
y(120m)-y(3m).
5. The first lag of explanatory variables has been used as instruments.
6. Since we cannot assume that residuals are serially uncorrelated and iid normal,
the asymptotic chi-square test rather than the small sample F-test is used to
assess the joint significance of estimated coefficients. The White correction is
used in presence of heteroscedasticity of unknown form. The Hansen-Hodrick
correction is a standard way to deal with overlapping data and serially cor-
related residuals in forecasting models. The Hansen-Hodrick procedure does
not guarantee a positive definite covariance matrix. The Newey-West correc-
tion returns a positive definite matrix. The chi-square statistics to test for joint
significant is suspiciously large, so that we carry out estimates with the simpli-
fied HH. Standard errors are built ignoring conditional heteroscedasticity and
assuming that serial correlation is simply due to overlapping observations of
homoscedastic forecast errors.
7. We have estimated the monetary equation (7.5) for the slope factor; all
coefficients are statistically significant and robust (White, Hansen-Hodrick,
Newey-West, simplified HH). The goodness of fit is about 60%. Mone-
tary variables predict the slope more accurately than curvature. We have
jointly estimated two simple Taylor-type reaction functions by maximum
likelihood. One equation based on the federal funds rate, the other on
the slope factor, which (as in Rudebusch and Wu, 2004) is considered as
a proxy of the policy rate. The first lag of the dependent variable has
been included among regressors to capture monetary policy inertia. The
Wald test confirms that respective coefficients are the same in the two
Taylor-type equations. GMM results are similar if we include future (expected)
inflation.

144
M. Modena
8. Our analysis is theory-consistent since the level obtained from the nominal
TS dominates in magnitude the level factor extracted from the real TS, which
is flat.
9. GMM estimation does not require distributional assumptions. GMM is a large
sample estimator; each equation is estimated using more than 250 observa-
tions. Instruments: the annual rate of growth of industrial production and
its first lag, both of which are highly correlated with both the industrial
production gap and the curvature factor; the realized real interest rate, com-
puted as the difference between the fist lag of the federal funds rate and actual
inflation.
10. The estimation of the of the variance of the disturbances are the fol-
lowing. Measurement equation: (0.1588)2 (p-value: 0); trend component:
(0.0564)2 (p-value: 0.0040); and cyclical component: (0.3358)2 (p-value:
0). The estimate of the amplitude of the cycle extracted from the log
series of the IP is 0.9461; the variance of disturbances are the following.
Measurement equation: (0.0016)2 (p-value: 0); trend component: (0.006)2
(p-value: 0.0030); and cyclical component (0.004)2 (p-value: 0). In both cases
convergence is achieved after quite a few iterations.
11. Since curvature is stationary we need to add a stochastic trend in order to make
it comparable with the log IP series. We estimate the trend and the intercept of
the IP series; then we run a stochastic simulation (with 1000, 5000, and 10000,
repetitions achieving similar results) in order to get the trended series for
curvature. The OLS regression of log IP onto the constant and the trend returns
an estimate of 3.41 and 0.0026 respectively; both coefficients are statistically
significant with null p-values. Statistical significance is confirmed by both the
White and the Newey-West corrections.
12. We have also run an auxiliary OLS estimation of log IP onto the trend and the
cycle. Residuals obtained from this regression turns out to be homoscedastic
and serially uncorrelated. The statistical properties of both the error series
from the measurement equation and the residuals from this auxiliary regres-
sion are almost identical. Moreover, since regressors of the aforementioned
auxiliary regression are generated series (KF estimated trend and cycle), we
have also employed the IV method, using as instruments the lagged values of
IP. The IV estimated coefficients are actually the same; the estimation returns
a suitable pattern for residuals. Trivially, as largely expected, the goodness of
fit of the auxiliary regression is almost 1.
References
Ang, A., Bekaert, G., and Wei, M. (2008) “The Term Structure of Real Rates and
Expected Inflation,” Journal of Finance, 63 (2): 797–849.
Ang, A. and Piazzesi, M. (2003) “A No-Arbitrage Vector Autoregression of Term
Structure Dynamics with Macroeconomic and Latent Variables,” Journal of
Monetary Economics, 50 (4): 745–787.
Ang, A., Piazzesi, M., and M. Wei. (2006) “What Does the Yield Curve Tell Us
about GDP Growth?” Journal of Econometrics, 131 (1): 359–403.
Bekaert, G., Cho S., and Moreno, A. (2005) “New-Keynesian Macroeconomics and
the Term Structure,” NBER Working Paper 11340, Cambridge, Massachusetts.

Latent Factors of the Yield Curve
145
Bernanke, B. S. and Blinder, A. S. (1992) “The Federal Funds Rate and the Channel
of Monetary Transmission,” American Economic Review, 82 (4): 901–921.
Bernanke, B. S. and Mihov, I. (1998) “Measuring Monetary Policy,” The Quarterly
Journal of Economics, 113 (3): 869–902.
Campbell, J. Y. and Cochrane, J. H. (1999) “By Force of Habit: A Consumption-
Based Explanation of Aggregate Stock Market Behaviour,” Journal of Political
Economy, 107 (2): 205–251.
Chapman, D. A. (1997) “The Cyclical Properties of Consumption Growth and the
Real Term Structure,” Journal of Monetary Economics, 39 (2): 145–172.
Cochrane, J. H. (2005) Asset Pricing, Princeton, NJ: Princeton University Press.
Cochrane, J. H. and Piazzesi, M. (2005) “Bond Risk Premia,” American Economic
Review, 95 (1): 138–160.
Cox, J. C., Ingersoll, J. E., and Ross, S. A. (1985) “A Theory of the Term Structure
of Interest Rates,” Econometrica, 53 (2): 385–408.
Dai, Q. and Singleton, K. J. (2000) “Specification Analysis of Affine Term Structure
Models,” Journal of Finance, 55 (5): 1943–1978.
Dai, Q. and Singleton, K. J. (2001) “Expectations Puzzles, Time-Varying Risk Pre-
mia and Dynamic Models of the Term Structure,” Journal of Financial Economics,
63 (3): 415–441.
Dewachter, H. and Lyrio, M. (2002) “Macro Factors and the Term Structure of
Interest Rates,” Working Paper, Catholic University of Leuven, Leuven.
Dewachter, H., Lyrio, M., and Maes, K. (2006) “A Joint Model for the Term Struc-
ture of Interest Rates and the Macroeconomy,” Journal of Applied Econometrics,
21 (4): 439–463.
Diebold, F. X. and Li, C. (2006) “Forecasting the Term Structure of Government
Bond Yields,” Journal of Econometrics, 130 (2): 337–364.
Diebold, F. X., Piazzesi, M., and Rudebusch, G. D. (2005) “Modeling Bond
Yields in Finance and Macroeconomics,” American Economic Review, 95 (2):
415–420.
Diebold, F. X., Rudebusch, G. D., and Aruoba, S. B. (2006) “The Macro-
economy and the Yield Curve: A Dynamic Latent Factor Approach,” Journal
of Econometrics, 131 (1): 309–338.
Duffee, G. R. (2002) “Term Premia and Interest Rate Forecasts in Affine Models,”
Journal of Finance, 57 (1): 405–433.
Duffie, D. and Kan, R. (1996) “A Yield-Factor Model of Interest Rates,” Mathemat-
ical Finance, 6 (4): 379–406.
Durbin, J. and Koopman, S. J. (2001) Time Series Analysis by State Space Methods,
Oxford: Oxford University Press.
Estrella, A. and Hardouvelis, G. A. (1991) “The Term Structure as a Predictor of
Real Economic Activity,” Journal of Finance, 46 (2): 555–576.
Estrella, A. and Mishkin, F. S. (1997) “The Predictive Power of the Term Structure
of Interest Rates in Europe and the United States: Implications for the European
Central Bank,” European Economic Review, 41 (7): 1375–1401.
Evans, C. L. and Marshall, D. A. (2007) “Economic Determinants of the Nominal
Treasury Yield Curve,” Journal of Monetary Economics, 54 (7): 1986–2003.
Fama, E. F. and Bliss, R. R. (1987) “The Information in Long Maturity Forward
Rates,” American Economic Review, 77 (4): 680–692.
Favero, C. A. (2006) “Taylor Rules and the Term Structure,” Journal of Monetary
Economics, 53 (7): 1377–1393.

146
M. Modena
Gallmeyer, M. F., Hollifield B., and Zin, S. E. (2005) “Taylor Rules, McCallum Rules
and the Term Structure of Interest Rates,” Journal of Monetary Economics, 52 (5):
921–950.
Garcia, R. and Luger, R. (2007) “The Canadian Macroeconomy and the Yield
Curve: An Equilibrium-Based Approach,” Canadian Journal of Economics, 40 (2):
561–583.
Hamilton, J. D. and Kim, D. H. (2002) “A Reexamination of the Predictability of
Economic Activity Using the Yield Spread,” Journal of Money, Credit, and Banking,
34 (2): 340–360.
Harvey, C. R. (1988) “The Real Term Structure and Consumption Growth,” Journal
of Financial Economics, 22 (2): 305–333.
Hordahl, P., Tristani, O., and D. Vestin. (2006) “A Joint Econometric Model of
Macroeconomic and Term Structure Dynamics,” Journal of Econometrics, 131
(1): 405–444.
Kim, C. J. and Nelson, C. R. (1999) State Space Models with Regime Switching,
Cambridge, Mass.: MIT Press.
Litterman, R. and Scheinkman, J. (1991) “Common Factors Affecting Bond
Returns,” Journal of Fixed Income, 1 (1): 54–61.
Nelson, C. R. and Siegel, A. F. (1987) “Parsimonious Modelling of Yield Curves,”
Journal of Business, 60 (4): 473–489.
Nelson, C. R. and Siegel, A. F. (1988) “Long-Term Behaviour of Yield Curves,”
Journal of Financial and Quantitative Analysis, 23 (1): 105–110.
Piazzesi,
M. (2003) “Affine Term Structure Models,”
in Y. Ait-Sahalia and
L. P. Hansen (eds.), Handbook of Financial Econometrics, Princeton, NJ.
Rudebusch, G. D. (1995) “Federal Reserve Interest Rate Targeting, Rational
Expectations, and the Term Structure,” Journal of Monetary Economics, 35 (2):
245–274.
Rudebusch, G. D. and Wu, T. (2007) “Accounting for a Shift in Term Struc-
ture Behavior with No-Arbitrage and Macro-Finance Models,” Journal of Money,
Credit and Banking, 39 (2–3): 395–422.
Rudebusch, G. D. and Wu, T. (2008) “A Macro-Finance Model of the Term
Structure, Monetary Policy, and the Economy,” Economic Journal, 118 (530):
906–926.
Singleton, K. J. (2006). Empirical Dynamic Asset Pricing. Model Specification and
Econometric Assessment, Princeton, NJ: Princeton University Press.
Stock, J. H. and Watson, M. W. (1989) “New Indexes of Coincident and Leading
Indicators,” in O. Blanchard and S. Fischer (eds.), NBER Macroeconomics Annual,
vol. IV, Cambridge, Mass.: MIT Press.
Wachter, J. (2006) “A Consumption Based Model of the Term Structure of Interest
Rates,” Journal of Financial Economics, 79 (2): 365–399.

8
On the Efficiency of Capital
Markets: An Analysis of the Short
End of the UK Term Structure
Andrew Hughes Hallett and Christian Richter
8.1
Introduction
In this chapter, we analyze the term structure of interest rates in a novel
way. We test to what extent the UK short-term interest rate is determined
by the short-term US interest rate, and how much by the UK monetary
instrument. In other words, we test jointly whether and to what extent
the uncovered interest parity (UIP) and/or the expectations hypothesis
(EH) of the term structure of interest rates holds.
The EH of the term structure was prominently formulated by Fisher
(1930), Keynes (1930), and Hicks (1953) and states that long-term inter-
est rates are determined by expectations of future short-term interest
rates. UIP, in turn, postulates that the interest differential between two
countries should equal the expected rate of depreciation or apprecia-
tion of the corresponding exchange rate. UIP received prominence from
expositions by Keynes (1923), whose attention had been captured by the
rapid expansion of organized trading in the forward exchange markets
following World War I.
Both hypotheses have in common that they use expectations. The
UIP uses expectations concerning the (spot) exchange rate; and the EH
uses expectations of the monetary instrument in our case, but of shorter
term interest rates in the general case. Both hypotheses have also in
common that the expectations are usually modeled assuming rational
expectations, although both hypotheses were actually formulated well
before the concept of rational expectations had been developed. Hence,
147

148
A. Hughes Hallett and C. Richter
expectations in UIP and EH do not have to be “rational.” In fact, in
the original literature, expectations were given exogenously. As a result,
when combining UIP and EH with rational expectations, one has to be
aware that an empirical rejection is not necessarily a rejection of UIP
and EH per se but may simply be a rejection of rational expectations.
This outcome should be of particular interest in the light of the finan-
cial crisis that started in 2007. Rational expectations imply that agents
have a complete knowledge of the economy and the economics involved.
Therefore, it is not surprising that UIP and EH are usually rejected when
rational expectations are included.1 At the same time, experimental
and survey evidence on exchange-rate expectations often rejects rational
expectations and also static expectations for that matter but tends to sup-
port extrapolative, adaptive, or regressive expectations instead (Marey
2004).2
In this chapter, we test UIP and EH jointly using extrapolative expec-
tations for the short end of the UK term structure. We can show that
both hypotheses affect the short-term interest rate albeit with unequal
weights. In our sample, the short-term interest rate is more affected by
the US interest rate than by the UK monetary instrument. However, that
does not mean that UK monetary policy has no impact. Indeed, we find
that extrapolative expectations serve well as a proxy for the formation of
expectations. Finally, we are also able to show how the current financial
crisis has affected the link between UK and US interest rates.
This chapter is organized as follows: Section 8.2 introduces our model
to be tested and how it is estimated. Section 8.3 presents the results, and
Section 8.4 concludes.
8.2
Empirical techniques
8.2.1
The hypotheses tested in this chapter
For UIP we use the common notation:
it,1 = if
t,1 + se
t + λt
(8.1)
where “λt” is the time-varying risk premium, “st” is the spot exchange
rate, “it” is the interest rate (maturity of three months), superscript “f”
is foreign, and “e” means expectation.
The EH of the term structure in turn implies:
it,1 = αCBe
t
(8.2)

On the Efficiency of Capital Markets
149
where “CBt” is the central-bank interest rate. We use extrapolative
expectations of the form:
xe
t = (1 −β)xt −βxt−1
(8.3)
The reason for using extrapolative expectations is that they represent,
together with the Kalman filter, an optimal learning and updating algo-
rithm (Garratt and Hall 1997a). It therefore has a sound theoretical
foundation in markets where agents may not be perfectly informed all
the time. Moreover, using extrapolative expectations results in a lag
structure, which is important for calculating phase shifts between mon-
etary policy changes and avoids the poor fits often found with rational
expectations.
If we substitute Equation (8.3) into (8.4), we get:
it,1 = if
t,1 + (1 −γ )st −γ st−1 −st−1 + λt
= if
t,1 + (1 −γ )st −(1 + γ )st−1 + λt
(8.4)
Using extrapolative expectations in EH results in:
it,1 = α (1 −δ)CBt −αδCBt−1
(8.5)
Take a time-varying weighted average of both equations (i.e., sometimes
domestic influences are more important but sometimes foreign pressures
are more important):
wtit,1 + (1 −wt)it,1 = wt[α (1 −δ)CBt −αδCBt−1]
+ (1 −wt)[if
t,1 + (1 −γ )st −(1 + γ )st−1 + λt]
⇔it,1 = wtα(1 −δ)CBt −wtαδCBt−1 + (1 −wt)
[if
t,1 + (1 −γ )st −(1 + γ )st−1 + λt]
(8.6)
Equation (8.6) is the equation we estimate in this chapter, although we
added one extra lag for the foreign interest rate. If UIP and EH had the
same impact on the UK interest rate, then wt would be equal to 0.5.
Notice that in equation (8.6), not only do the variables vary over time
but so also do the parameters. Our approach therefore allows for time-
varying risk premiums as well as for a changing relationship between
foreign and domestic interest rates (market conditions at home and
abroad).

150
A. Hughes Hallett and C. Richter
In order to estimate the parameters in Equation (8.6) we use the
Kalman filter. That is, we estimate the following state space model:
it = DtXt + ε1,t
(8.7)
where equation (2.7) is the measurement equation, and with
Dt = Dt−1 + ε2,t
(8.8)
where εa,t ∼i.i.d. (0, σ 2εa) for a = 1, 2, in the state equation.
In this formulation, it is the British three-month T-Bill rate; Xt is a
set of determining variables such as the British base rate (the monetary
instrument in the British case) and the US three-month T-Bill rate; and
Dt is a matrix of estimated parameters, including any time-varying risk
premium. In either case, the rationale of equation (2.8) is that agents
only update the parameters of the model once an unforeseen shock
has occurred (Lucas 1976). Moreover, an attractive advantage of the
Kalman filter algorithm is that it assumes that agents form one-period
ahead forecasts. These forecasts are then compared with the correspond-
ing (new) observation for the same variable. According to the Kalman
gain, the coefficients are systematically updated in order to minimize
the one-period ahead forecast error. That property makes the Kalman
filter convenient for modeling the process of learning3 and the acqui-
sition of new information It incorporates rational learning behavior by
market participants, defined as the ability to minimize their short-run
forecasting errors.
The question now is how the parameters are updated to reflect learn-
ing. Wells (1996) shows that, in the case of an exogenous shock, the
parameters are optimally updated as follows:
d t|t = d t|t−1 + Kt

it −Xtd t|t−1

(8.9)
where d t|s denotes the estimate of the state “d” at time t conditional
on the information available at time s. The interesting part of equation
(8.9) is the term in brackets. It shows the forecast error. Hence, the cur-
rent parameters are updated according to the forecast error resulting from
an estimated parameter, which did not contain the additional informa-
tion revealed in the current period. This forecast error in turn affects the
Kalman gain. Thus, the Kalman gain may be calculated as:
Kt = P t|t−1X′
t

XtP t|t−1X′
t + 
−1
(8.10)

On the Efficiency of Capital Markets
151
where P t|s is the variance of the forecast error at time t conditioned on
the system at time s and  is the covariance matrix of ε2,t. In other
words, the updating process depends on the one period forecast error
and its distribution in the past.
8.2.2
Significance tests and diagnostic test
Using the procedure described so far implies that we get a set of param-
eter values for each point in time. Hence, a particular parameter could
be significant for all points in time, or at some periods but not oth-
ers; or it might never be significant. These parameter changes are at the
heart of this chapter since they imply changes in the lag structure and
hence in our frequency and dependency analysis. We therefore employed
the following testing strategy. We start with a general lag structure of
order q. The value of q is determined by the Akaike information criterion
(AIC) test. If a particular lag was never significant (across successive time
periods) then this lag was dropped from the equation and the model
estimated again. If the AIC criterion was less than before, then that lag
was excluded altogether. If a parameter was significant for some periods
but not others, it was kept in the equation with a parameter value of zero
for those periods in which it was insignificant. This strategy minimizes
the AIC criterion and leads to a parsimonious specification. Finally, we
tested the residuals in each regression for the absence of serial correlation
and heteroscedasticity.
The final specification, equations (8.8)–(8.9), was then validated using
two different stability tests. Both tests check the same null hypothesis
against differing temporal instabilities. The first is the fluctuations test of
Ploberger et al. (1989), which detects discrete breaks at any point in time
in the coefficients of a (possibly dynamic) regression. The second test
is due to LaMotte and McWorther (1978) and is designed specifically to
detect random parameter variation of a specific unit root form (our speci-
fication). We found that the random walk hypothesis for the parameters
was justified for each country (results available on request). Finally, we
chose the fluctuations test for detecting structural breaks because the
Kalman filter allows structural breaks at any point and the fluctuations
test is able to accommodate this.4 Thus, and in contrast to other tests, the
fluctuations test is not restricted to any prespecified (and hence untested)
number of breaks.5
Once this regression is done, it gives us a time-varying model. From
this model, we can then calculate the short-time Fourier transform as
outlined below in order to calculate the associated time-varying spectra
and cross-spectra.

152
A. Hughes Hallett and C. Richter
8.2.3
Spectral analysis
The spectral density function shows the strength of the variations of a
time series at each frequency of oscillation. It decomposes the variance
of a time series into the component that occurs at each frequency or
cycle length. Put in a diagram, it shows at which frequencies the vari-
ance or fluctuations are strong or powerful and at which frequencies the
variations are weak.
In order to calculate the spectrum from the estimated version of
equation (8.6), it is convenient to use the fast Fourier transform. The fast
Fourier transform creates a frequency domain representation of the original
time domain representation of the data. Thus, the spectra, cross-spectra,
and phase shifts are based on regressions done in the time domain but
then transformed into a frequency domain representation by the Fourier
transform. However, we have allowed the coefficients in our regressions
to vary over time. We therefore have to derive one Fourier transform for
each point in time. These calculations define a sequence of short-time
Fourier transformations (STFTs). In discrete time, this means the data to
be transformed has been broken up into frames (which usually overlap
each other). Each frame is then transformed as described, and the result
added to a matrix, which records its magnitude, phase, and frequency at
each time point. These steps may be expressed as:
STFT {x[n]} ≡X(m,ω) =
∞

n=−∞
x[n]w[n −m]e−jωn
(8.11)
In this case, m and n are different points in time; ω is the frequency
and is continuous; j = √−1; and “n−m” is the estimation period of the
regression currently in play. In our application, the estimation period is
not constant but is increasing with each new observation. The squared
magnitude of the STFT then yields the spectrogram of the function:
spectogram

xt

≡|X(τ,ω)|2
(8.12)
In this chapter, the specific algorithm used to calculate the various
Fourier transforms is the Bluestein algorithm (Bluestein 1968). This is a
well established algorithm, widely used in engineering (Boashash 2003;
Boashash and Reilly 1992) but not commonly used in economics.
Finally, Boashash and Reilly (1992) have shown that, once equation
(8.2) has been estimated, its coefficients αi,t can be used to calculate the
STFT and the power spectra directly. That has the convenient property
that the traditional formulae are still valid and may still be used, but they
have to be recalculated at each point in time. The time-varying spectrum

On the Efficiency of Capital Markets
153
of the growth rate series can therefore be calculated as follows (see also
Lin 1997):
Pt (ω) =
σ 2
1 +
9
i=1
αi,t exp

−jωi


2
t
(8.13)
Hence, at any point in time, the power spectrum can be calculated instan-
taneously from the updated parameters of the model. In addition, we are
able to generate a power spectrum even if we have a short time series,
and even if that time series contains structural breaks.
8.2.4
Cross-spectral analysis
Let us assume that we estimated the following model:
it = A(L)t xt + ut, ut ∼i.i.d.

0,σ 2	
(8.14)
where A(L)t is a filter, and L is the lag operator such that Lzt = zt−1.
Notice that the lag structure, A(L)t, is time-varying. That means we need
to use a time-varying model (we use the Kalman filter again) to estimate
the implied lag structure. That is:
aj,t = aj,t−1 + ηj,t, for j = 0, …, q and ηt ∼

0,σ 2
η
	
(8.15)
What we are interested in is to find a lead-lag relationship between the
different variables. For example, for UIP we would like to know how
fast the adjustment of the UK interest rate is, once the US rate changes.
That is, by how much is the US rate leading? With respect to the central-
bank rate, we would also like to know how much the central-bank rate is
reflected in movements in the three-month market interest rate. In other
words, by how much does the three-month interest rate lead the central
bank’s rate? A convenient tool to measure these lead-lag relationships
is the phase shift. The phase shift is widely used in frequency or time-
frequency analysis6. Given that we have already estimated the model
(8.13), all we have to do is to use the coefficient to calculate the phase
shift from it.
In what follows, we briefly explain the concept of the phase shift.
In order to calculate the phase shift, we need the phase angle. The phase
angle measures the lead or lag relationship between two variables at each
cyclical frequency. Formally:
ϕ(ω) = tan−1 −QYX (ω)
CYX (ω)
(8.16)

154
A. Hughes Hallett and C. Richter
where
CYX (ω) = fXX (ω)
∞

j=0
aj cosωj, and QYX(ω) = fXX (ω)
∞

j=0
aj sinωj
(8.17)
The phase angle can therefore be written as
ϕ(ω) = tan−1


∞

j=0
aj sinωj
∞

j=0
aj cosωj


(8.18)
Hence, to calculate the phase angle, all we need to know are the coeffi-
cients aj from equation (8.14). However, in this chapter we will actually
analyze a “standardized” phase angle, or phase shift:
τ(ω) = ϕ(ω)
ω
(8.19)
To see how to interpret the phase shift statistic, consider Figure 8.1,
which shows one variable is following the other at long cycles, with
a delay of one month – peak to peak, say. However, for smaller cycles,
the delay is shorter. If the markets are efficient in the conventional sense,
the two processes should follow each other very closely since agents are
able to process new information relatively quickly. Nevertheless, in other
cases, there will be natural leads or lags depending on the structure of
the markets, the institutional arrangements, and the degree of financial
integration.
The formulae given above are for the time-invariant case. Since we get
new values for aj for each point of observation t, we can apply the above
τ(ω)
1
ω
Figure 8.1
Assumed shape of a phase shift

On the Efficiency of Capital Markets
155
formulae for every point in time t. That means the time-varying phase
shift changes to:
τ(ω)t = ϕ(ω)t
ω
(8.20)
8.3
Empirical results for the UK and US money markets
8.3.1
Data set
The UK and US three-month T-Bill rates and the dollar–pound exchange
rate are taken from the IFS database. We used monthly data from 1972M1
to 2008M12. The UK central-bank rate is from the Bank of England and is
available from its webpage. The sample for the bank rate is also 1972M1–
2008M12.
8.3.2
Kalman filter results
To economize on space, we show only the final regressions here. All
other results, for the earlier periods, are available from the authors
upon request. The time series estimates of equation (8.6) are shown in
Table 8.1.
Table 8.1
Regression results
VAR/System (estimation by Kalman filter)
Dependent
variable
UKTBILL
Monthly data from
January 1976 to
December 2008
Usable
observations
396
Std error of
dependent
variable
3.4868193831
R2
0.996184
Standard error of
estimate
0.5527347969
Mean of
dependent
variable
8.1563131313
Sum of squared
residuals
118.84562898
Akaike (AIC)
criterion
0.54873
Ljung-box test: Q*
(40)
44.3872
Variable
Coefficient
Std error
T-Stat
Constant
0.178406348
0.035619453216
5.008677325101
UKDISC
1.121130944
0.100796310081
11.12273795870
UKDISC{1}
−0.302678222
0.084186905184
−3.59531237803
USTBILL
0.244651619
0.041170474386
5.94240467455
GBPDOL
−1.261248657
0.169144089998
−7.4566522360
GBPDOL{1}
0.764879193
0.103076219570
7.42052043125
USTBILL{4}
−0.001187483
0.005018534745
−0.2366194133

156
A. Hughes Hallett and C. Richter
In Table 8.1, UKTBILL is the UK three-months T-bill rate, UKDISC is
the central-bank rate; USTBILL is the US three-months T-bill rate, and
GBPDOL is the pound–dollar rate. We included the fourth lag of the
US T-bill rate in order to generate non-autocorrelated errors. If we add
the two coefficients of USTBILL and use that value to calculate wt from
equation (8.6), then we get the long-run impact of the US T-bill rate
on UK rate, that is it is the impact if the system reaches a steady state.
As figure 8.2 shows, the impact of the US rate varies over time but is
always the most important determinant, although its influence is shrink-
ing sharply towards the end of the sample. That may be an indication
that the UK rate is decoupling itself from the US rate. However, that is a
relatively recent phenomenon and follows a period when the US influ-
ence was unusually high (2003–2008). The history before that shows that
US rates had a steadily declining influence, although it was always high,
through the EMS period (1979–1990); but then a slowly increasing influ-
ence from the breakdown of the EMS (1993) until the period of recent
growth (2006).
The obvious next question that we need to answer is by how much
does the US Treasury bill rate lead the UK rate? For that, we look at the
phase shift.
0
0.2
0.4
0.6
0.8
1
1.2
77M2
79M6
80M1
82M12
86M6
87M1
89M12
93M6
94M1
96M12
00M6
01M1
03M12
07M6
08M1
Figure 8.2
Impact of the US rate on the UK rate (wt)

On the Efficiency of Capital Markets
157
0.1
1.1
2.1
–0.04
–0.02
0
0.02
0.04
0.06
0.08
0.1
0.12
77M2
81M6
87M12
89M1
94M6
00M12
02M1
07M6
Time
Months
Frequency
Figure 8.3
Phase shift between the UK and the US rate
From Figure 8.3, we can see that the lead of the US rate at long cycles is
small and has decreased over time, essentially since 2002. At the begin-
ning of the sample it was about 0.08 months and that was reduced to
0.06 months by the start of the financial crisis in mid-2007. The finan-
cial crisis itself has led to immediate reactions of the UK rate and a small
increase in the lead of US interest rates. However, the interesting result
is that, according to UIP, the UK rate does not necessarily have to follow
the US rate. Instead, the exchange rate (expectation) could change and
that could lead to a change of the UK rate. The above figure shows that
this is not the case. US rate changes have had a direct impact on the
UK rate, implying fairly fixed exchange rates and exchange rate expec-
tations. This appears to have held, even into the current financial crisis.
Whilst previous changes in the lead-lag relationship could be attributed
to changes in technology (early 70s), the recent immediate incorporation
of US rate into UK rates reflects much more markets sentiments towards
the US.
The fact that UK agents now incorporate changes in US rates into UK
rates more rapidly than they used to, does not contradict the fact that
the importance of the US rate decreased. What the above diagram shows
is the speed of adjustments and not the extent.

158
A. Hughes Hallett and C. Richter
–0.18
–0.16
–0.14
–0.12
–0.1
–0.08
–0.06
–0.04
–0.02
0
77M2
77M12
80M6
82M12
85M6
87M12
90M6
92M12
95M6
97M12
00M6
02M12
05M6
07M12
Time
Frequency
0.1
1.6
Months
Figure 8.4
Phase shift between the central-bank rate and the T-Bill rate
We now turn our attention to the central bank’s rate. Here we asked
how well extrapolative expectations work in this model. If extrapolative
expectations work well, then they should enable agents to incorporate
their expectations into the interest rate and hence the T-bill rate should
lead the central bank rate.
Figure 8.4 shows the phase shift between the T-bill rate and the central
bank rate in the UK.
From the above figure we can see, that extrapolative expectations work
well on average, because the T-bill rate is leading the monetary instru-
ment except in the period 2002 – 2007. Hence, expectations up to 2007
were formed in terms of what they could anticipate of monetary pol-
icy and incorporate into the current T-bill rate, otherwise the T-bill rate
could not lead the monetary instrument. This example shows that form-
ing extrapolative expectations does not imply that agents are irrational.
Instead, they may just be learning how to anticipate the behavior of the
monetary authorities in the sense we defined earlier. Thus, if we allow
for learning, extrapolative expectations can serve as a tool to anticipate
the behavior of other variables.
Finally, we look at the lead-lag relationship between the T-bill rate
and the spot exchange rate. From the UIP relationship (8.1), the interest
rate will depend on the expected spot rate. As in the previous example,
we have assumed extrapolative expectations are at work here. If extrap-
olative expectations are at work, then they should help to incorporate
future developments of the exchange rate into the interest rate and imply

On the Efficiency of Capital Markets
159
0.1
1.1
2.1
–1.5
–1
–0.5
0
0.5
1
1.5
2
2.5
77M2
78M1
78M12
84M6
89M1
89M12
95M6
00M1
00M12
06M6
Time
Frequency
Months
Figure 8.5
The phase shift between the T-bill rate and the exchange rate
that the T-bill rate leads the exchange rate. Figure 8.5 now shows the
relationship between the two variables in practice.
Figure 8.5 shows that, in qualitative terms, the lead-lag relationship is
relatively stable. Up to a frequency of 1.2, or 5.2 months, the exchange
rate is leading the T-bill rate. Nevertheless, for shorter cycles the T-bill
rate leads. The interesting thing about these results is that the current
crisis has increased the lead of the exchange rate in the long term, and the
lead of the T-bill rate in the short term. This says that agents have been
able to anticipate short-term fluctuations in the exchange rate relatively
well, but have difficulties concerning long run behavior.
Moreover, this diagram also highlights why it is sometimes difficult to
reach results concerning the validity of an expectation formation. The
advantage of the Fourier transform is that it shows for all frequencies how
one variable affects another one. It does not average an effect across some
or all frequencies. If we had focused solely on a time-series approach, the
property that extrapolative expectations work for some cycles but not for
all would have been hidden. The reason is that a time-series approach,
if not filtered, calculates averages over all the different frequencies.
8.4
Conclusion
In this chapter, we test the EH for the term structure of interest rates
jointly with the UIP condition for the short end of the UK term structure.

160
A. Hughes Hallett and C. Richter
We find that the US interest rate, the UK monetary instrument, and the
(spot) exchange rate all affect the short-term interest rate. However, the
impact of the US rate is the biggest effect, although that has decreased a
little during the recent financial crisis.
We also tested a bounded rationality approach. We deviated from
the contemporary literature by refusing to impose rational expectations.
Instead, we have assumed extrapolative expectations as an obvious
behavioral alternative. We have shown that incorporating extrapolative
expectations in both hypotheses turned out to be a significant improve-
ment. Hence, and in contrast to previous work which has assumed
rational expectations, we find the UIP and the EHs are not rejected. Thus,
the problem seems to have been violations of the rational expectations
paradigm, not violations of UIP or the EH of behavior in the financial
markets. Second, we also show that extrapolative expectations formation
can help us anticipate the central bank’s impact on short-term interest
rates. Finally, concerning the exchange rate, we were able to show that
extrapolative expectations can help to anticipate short-term movements
of the exchange rate but not long-term movements of the exchange rate.
Hence, in the short-run, interest rates lead movements in the exchange
rate. However, in the longer term they do not.
Notes
1. Many comprehensive surveys exist: see, for example, Froot and Thaler (1990),
Lewis (1995) and Engel (1996) for UIP, and Cook and Hahn (1990) and
Campbell and Shiller (1991) for EH.
2. See also Hughes Hallett and Richter (2002; 2003a; 2003b; 2004).
3. The Kalman filter is widely used in finance and macroeconomics as a learning
algorithm: see for example, Lucas (1976), Garatt and Hall (1997a; 1997b),
Whitley (1994). Salmon (1995) shows that the Kalman filter is a special case
of a neural network. Hence the Kalman filter can be regarded as an optimal
procedural learning algorithm.
4. Note that all our tests of significance, and significant differences in parameters,
are being conducted in the time domain, before transferring to the frequency
domain. This is because no statistical tests exist for calculated spectra (the
data transformations are nonlinear and involve complex arithmetic). Stability
tests are important here because our spectra are sensitive to changes in the
underlying parameters. But, given the extensive stability and specification tests
conducted, we know there is no reason to switch to another model that fails
to pass those tests.
5. The fluctuations test works as follows: one parameter value is taken as the ref-
erence value, for example, the last value of the sample. All other observations
are now tested whether they significantly differ from that value. In order to do
so, Ploberger et al. (1989) have provided critical values which we have used in

On the Efficiency of Capital Markets
161
the figures. If the test value is above the critical value then we have a structural
break, i.e. the parameters differ significantly from their reference values and
vice versa. For reasons of limited space we have excluded the test diagrams
from this chapter but report on the results. The diagrams are available from
the authors upon request.
6. See, for example, Boashash (2003), Boashash and Reilly (1992) and Hughes
Hallett and Richter (2009).
References
Bluestein, L. I. (1968) “A Linear Filtering Approach to the Computation of the Dis-
crete Fourier Transform,” Northeast Electronics Research and Engineering Meeting
Record, 10 (3): 218–219.
Boashash, B. (2003) Time Frequency Signal Analysis and Processing, Oxford: Elsevier.
Boashash,
B. and Reilly,
A. (1992) “Algorithms for Time-Frequency Signal
Analysis,” in B. Boashash (ed.), Time-Frequency Signal Analysis: Methods and
Applications, Melbourne: Longman-Cheshire, pp. 163–181.
Campbell, J. Y. and Shiller, R. (1991) “Yield Spreads and Interest Rate Movements:
A Bird’s Eye View,” The Review of Economic Studies, 58 (5): 496–514.
Cook, T., and Hahn, T. (1990) “Interest Rate Expectations and the Slope of the
Money Market Yield Curve,” Federal Reserve Bank of Richmond Economic Review,
76 (1): 3–26.
Engel, C. (1996) “The Forward Discount Anomaly and the Risk Premium: A Survey
of Recent Evidence,” Journal of Empirical Finance, 3 (2): 123–192.
Fisher, I. (1930) The Theory of Interest, New York: Macmillan Press.
Froot, K. A. and Thaler, R. H. (1990) “Anomalies: Foreign Exchange,” Journal of
Economic Perspectives, 4 (3): 179–192.
Garratt, A. and Hall, S. (1997a) “E-equilibria and Adaptive Expectations: Output
and Inflation in the LBS Model,” Journal of Economic Dynamics and Control, 21
(7): 1149–1171.
Garratt, A. and Hall, S. G. (1997b) “The Stability of Expectational Equilibria in
the LBS Model,” in C. Allen and S. G. Hall (eds), Macroeconomic Modelling in a
Changing World, New York: Wiley, pp. 217–246.
Hicks, J. (1953) Value and Capital, London: Oxford University Press.
Hughes Hallett, A. and Richter, C. (2002) “Are Capital Markets Efficient? Evidence
from the Term Structure of Interest Rates in Europe,” Economic and Social Review,
33 (3): 333–356.
Hughes Hallett,
A. and Richter,
C. (2003a) “Learning and Monetary Pol-
icy in a Spectral Analysis Representation,”
in P. Wang and S.-H. Chen
(eds.), Computational Intelligence in Economics and Finance, Berlin: Springer,
pp. 91–103.
Hughes Hallett, A. and Richter, C. (2003b) “A Spectral Analysis of the Short-End of
the British Term Structure,” in R. Neck (ed.), Modelling and Control of Economic
Systems, Amsterdam: Elsevier, pp. 123–128.
Hughes Hallett, A. and Richter, C. (2004) “Spectral Analysis as a Tool for Finan-
cial Policy: An Analysis of the Short End of the British Term Structure,”
Computational Economics, 23 (3): 271–288.

162
A. Hughes Hallett and C. Richter
Hughes Hallett, A. and Richter, C. (2009): “Is the US No Longer the Economy
of First Resort? Changing Economic Relationships in the Asia-Pacific Region,”
International Economics and Economic Policy, 6 (2): 207–234.
Keynes, J. M. (1923) A Tract on Monetary Reform, London: Macmillan Press.
Keynes, J. M. (1930) A Treatise on Money, New York: Macmillan Press.
LaMotte, L. R. and McWorther, A. J. (1978) “An Exact Test for the Presence of
Random Walk Coefficients in a Linear Regression,” Journal of the American
Statistical Association, 73 (364): 816–820.
Lewis, K. K. (1995) “Puzzles in International Financial Markets,” in G. M. Gross-
man and K. Rogoff (eds.), Handbook of International Economics, New York:
Elsevier.
Lin, Z. (1997) “An Introduction to Time-Frequency Signal Analysis,” Sensor Review,
17 (1): 46–53.
Lucas, R. E. (1976) “Econometric Policy Evaluation: A Critique,” in K. Brunner,
and A. Meltzer (eds.), The Phillips Curve and Labor Markets, Amsterdam: North-
Holland.
Marey, P. S. (2004) “Uncovered Interest Parity Tests and Exchange Eate Expecta-
tions,” Working Paper, Maastricht University, Maastricht.
Ploberger, W., Krämer, W., and Kontrus, K. (1989) “A New Test For Structural
Stability in the Linear Regression Model,” Journal of Econometrics, 40 (2): 307–
318.
Salmon, M. (1995) “Bounded Rationality and Learning: Procedural Learning,” in
A. Kirman and M. Salmon (eds.), Learning and Rationality in Economics, Oxford:
Basil Blackwell.
Wells, C. (1996) The Kalman Filter in Finance, Dordrecht: Kluwer Academic
Publishers.
Whitley, J. D. (1994) A Course in Macroeconomic Modelling and Forecasting, London:
Harvester Wheatsheaf.

9
Continuous and Discrete Time
Modeling of Short-Term
Interest Rates
Chih-Ying Hsiao and Willi Semmler
9.1
Introduction
In modern finance theory, the short-term interest rate is important
in characterizing the term structure of interest rates and in pricing
interest-rate-contingent-claims. There is some pioneering work in the
continuous-time framework, for example by Vasicek (1997) and Cox et al.
(1985). A survey of is provided by Chan et al. (1992). Chan et al. (1992)
show that a wide variety of well-known one-factor models for short rates
can be nested within the following stochastic different equation (SDE):
dXt = (c −βXt)dt + σXγ
t dWt.
(9.1)
The unpredictable residual of the Chan, Karolyi, Longstaff and Sanders
(CKLS) model is modeled as a Brownian motion Wt. The features of this
model include a mean-reverting drift coefficient1 and a level-dependent
diffusion coefficient. This continuous-time framework can provide ele-
gant expressions in theory, but it entails some difficulty in the empirical
research (see Lo 1988). Many methods have been developed to imple-
ment the empirical estimations. For example, among others, one can
mention the indirect inference method of Gouriéroux et al. (1993),
the approximate likelihood method of Perdersen (1995), the general
method of moments with respect to diffusion generators by Hansen and
Scheinkman (1995) and Duffie and Glynn (2001), the efficient method
of moments of Gallant and Tauchen (1996), the nonparametric method
of Ait-Sahalia (1996) and Ait-Sahalia (1997), the density-approximation
method by Dacunha-Castelle and Florens-Zmirou (1986) and Ait-Sahalia
(1999), and the Milstein method by Elerian (1998). Finally, this chapter2
163

164
Chih-ying Hsiao and W. Semmler
considers the new local linearization (NLL) method developed by Shoji
and Ozaki (1997, 1998).
In order to take continuous-time models to the data, one first has
to discretize those models. We employ here three discretization meth-
ods: the Euler method, the NLL method, and the Milstein method. The
three methods deliver discrete-time approximate models for discrete-
time-observed data of a continuous-time diffusion process. In this way
we can implement the maximum likelihood estimation (ML estimation)
and provide predictions. In the literature, Lo (1988) pointed out that the
Euler estimator3 is not consistent. The Milstein and NLL approximations
are shown to improve the Euler approximation (see Elerian 1998: 11,
Table 1; and Shoji and Ozaki 1997: 494–501). The improvement in their
papers is represented by smaller errors of the parameter estimations in the
numerical experiments. Our chapter takes another view to assess those
models. Besides the accuracy of parameter estimation, we also consider
the accuracy of prediction. For the SDE (1) where the drift coefficient is
linear, we show that the Euler and the NLL methods provide the same
prediction. Thus, these two methods are actually statistically equivalent.
For comparing the Euler and the Milstein methods we do not verify the
superiority of the Milstein method, in contrast to Elerian (1998). The
parameter estimations and the one-step-ahead predictions of the two
models are very similar. We argue it is because of the small scales of the
parameters, which lead to a relatively small effect on the discretization
bias. The scales of the parameters are chosen from the results of our
empirical study. In other words, the advantage of the Milstein method
is not very significant in the current short-term interest-rate case.
The Euler and Milstein approximate models are applied to the short-
term interest-rate data of Germany, the UK, and the USA. The two
approximate models perform quite similarly in both estimation and
prediction. We find none of the country short-rate data can pass our
specification tests in a satisfactory way where the estimated residuals of
all the three countries have too high autocorrelation and too thick tails.
So we look for new models which can explain these stylized facts. In the
continuous-time framework there is some work pointing out the short-
comings of the CKLS model (9.1) (see, for example, Ait-Sahalia 1996 and
Andersen and Lund 1997). However, the data simulated by these two
continuous-time models still cannot generate the high autocorrelation
of the residuals either.
Since we cannot find a suitable model in the continuous-time frame-
work we turn to the discrete-time framework. The autoregressive moving-
average (ARMA) structure is a candidate for fitting high autocorrelations

Time Modeling of Short-Term Interest Rates
165
of the estimated white noise. We will see, in Section 9.4, that we can
model the autocorrelation of the estimated noise by taking more lags in
the models. To model the thick tails in the estimated white noise we fol-
low the work of Brenner et al. (1996) and Koediji et al. (1997). They
employ the autoregressive conditional heteroscedastic (ARCH) model
suggested by Engle (1982) and Bollerslev (1986) to model the thick tails.
In addition, their conditional variance depends on the level of the short-
time interest rates. Combining the modeling strategies above, we obtain
an ARMA-ARCH structure with level-dependent volatility. Our model
generalizes the model of Brenner et al. (1996) by the ARMA structure.
The remainder of this chapter is organized as follows. Section 9.2
introduces the three discretization methods. We show that the Euler
and NLL approximate models for the SDE (9.1) are equivalent under
reparametrization. In Section 9.3, the Euler and the Milstein approxima-
tions will be applied to the empirical short-rate data. We find evidence
which cannot be represented by the model (9.1). We thus look for new
models in Section 9.4, where we find the discrete-time ARMA-ARCH
model with level-dependent volatility is a better candidate for the short
rates. Section 9.5 concludes this chapter.
9.2
Discrete-time approximation
Here we introduce briefly the three methods of discrete-time approxima-
tion: the Euler, the Milstein, and the NLL method.
9.2.1
Euler method
The idea of the Euler method is to replace dt in the equation (1) by a time
interval t and we have a discrete-time approximation for the diffusion
process X:
Xti+1 −Xti = b(Xti,θ)ti + a(Xti,θ)Wti.
(9.2)
9.2.2
Milstein method
The Milstein method approximates the SDE by the following scheme:
Xti+1 −Xti = b(Xti,θ)ti + a(Xti,θ)Wti + 1
2a(Xti)a′(Xti)((Wti)2 −ti)
(9.3)
where ti = (ti+1 −ti) and Wti = Wti+1 −Wti.4 It has one more term
then the Euler method of the equation (9.2) and better convergence.5

166
Chih-ying Hsiao and W. Semmler
The likelihood based on the Milstein method is calculated as follows.
Following (9.3), the dynamic of the SDE (9.1) is approximated by
Xti+1 −Xti = (c −βXti)ti + σXγ
ti Wti + 1
2σ 2γ X2γ −1
ti
(W2
ti −ti),
where ti = ti+1 −ti, Wti = Wti+1 −Wti.
Let
Yti+1 = Xti+1 −Xti −(c −βXti)ti + 1
2σ 2γ X2γ −1
ti
ti.
The above equation becomes
1
2σ 2γ X2γ −1
ti
(Wti)2 + σXγ
ti Wti = Yti+1.
Let xi ∈R still be the realizations of Xti and yi be the realizations of Yti
for i = 0,...,N correspondingly. We solve the equation (16) to obtain the
realizations of Wti = u+
i+1,u−
i+1, where
u+
i+1 =
−1 +

1 + 2γ yi+1
xi
σγ xγ −1
i
u−
i+1 =
−1 −

1 + 2γ yi+1
xi
σγ xγ −1
i
.
Then the conditional density is given by
p(Xti+1 = xi+1|Xti = xi) =
dP({Wti = du+
i+1} ∪{Wti = du−
i+1})
dyi+1
=
dP(Wti = du+
i+1)
du+
i+1

du+
i+1
dyi+1
 +
dP(Wti = du−
i+1)
du−
i+1

du−
i+1
dyi+1

=
1

2πti

exp

−
(u+
i+1)2
2ti

+ exp

−
	
u−
i+1

2
2ti





1
σxγ
i

1 + 2γ yi+1
xi

,
as 1 + 2γ yi+1
xi
> 0. If 1 + 2γ yi+1
xi
< 0, then the density above is infinity. If
1+ 2γ yi+1
xi
< 0, which means there is no real solution of Wti in (16) for
such yi+1, therefore the density is equal to zero
p(Xti+1 = dxi+1|Xti = xi) = 0.

Time Modeling of Short-Term Interest Rates
167
Comparing this density function and the density function in Equation
(2.5) in Elerian (1998: 7), it is not difficult to show the identity of these
two functions by some calculation.
By numerical operations of the ML estimations we must modify the
density function, because when 1 + 2γ yi+1
xi
= 0, the value of the density
function is infinity. Therefore, we apply the following density function
for the ML estimations:
gmil(xi,xi+1,θ,ti) =
dP(Xti+1 = dxi+1|Xti = xi)
dxi+1
=
1

2πti

exp

−
	
u+
i+1

2
2ti

+ exp

−
	
u−
i+1

2
2ti





1
σxγ
i

1 + 2γ yi+1
xi

,
for 1 + 2γ yi+1
xi
> 10−10,
= 10−10, otherwise.
9.2.3
New local linearization method
The NLL method is suggested by Shoji and Ozaki (1997: 490–491). It
approximates the drift coefficient b(Xs) up to the second-order terms by
using the Itô formula
dXs = (b(Xti) + b′(Xti)(Xs −Xti) + 1
2b′′(Xti)a2(Xti)(s −ti))ds + a(Xti)dWs.
(9.4)
while the diffusion coefficient is still kept as a constant. The equation
(9.4) can be solved analytically, and the solution at ti+1 is given by
Xti+1 −Xti =
b(Xti)
b′(Xti)(eb′(Xti)(ti+1−ti) −1)
+
b′′(Xti)
(b′(Xti))2
a(Xti)2
2
(eb′(Xti)(ti+1−ti) −1 −b′(Xti)(ti+1 −ti))
+ a(Xti)
 ti+1
ti
eb′(Xti)(ti+1−z)dWz.
(9.5)
The distribution of the last term can is given by
a(Xti)
 ti+1
ti
eb′(Xti)(ti+1−z)dWz
dis.
∼N

0,a(Xti)2
 ti+1
ti
e2b′(Xti)(ti+1−z)dz

.
(9.6)

168
Chih-ying Hsiao and W. Semmler
9.2.4
Equivalence of the Euler and NLL predictors
Here we show the Euler and NLL predictors of the SDE (1) are actu-
ally statistically equivalent due to the linearity of the drift coefficient
in Equation (9.1). The Euler approximation is obtained according to
Equation (9.3) and given by
X(i+1)t −Xit = (c −βXit)t + σXγ
itWit
(9.7)
while the NLL approximation is obtained according to Equation (5)
X(i+1)t −Xit = h1(β)
β
(c −βXit) + σh2(β)Xγ
itUi+1
(9.8)
Then we can observe an equivalent mapping under the reparametrization
βeut = h1(βnll) := 1 −e−βnllt,
ceut = cnll
βnll
h1(βnll)
γeu = γnll,
σeu = σnllh2(βnll) := σnll

1 −e−2βnllt
2βnllt
,
where Ui,i = 1,... are i.i.d N(0,t)-distributed.
9.3
Empirical results on modeling short-term interest rates
9.3.1
Data
We apply only the Euler and the Milstein approximations for the empir-
ical short-rate data. The short-rate data are interest rates with a one-day
maturity, which are the call money rate of Germany, the overnight inter-
bank rate of the UK, and the federal funds rate of the USA. All data are
monthly data from “The International Statistical Yearbook”6 for the time
period January 1983 to December 1997 (180 observations) for estima-
tion. The further period January 1998 to June 2000 (30 observations) is
reserved for prediction. We take data after the oil crisis, for January 1983–
June 2000, because many researchers have found evidence of regime
changes for the crisis period 1979–1982. The time series of the rates are
plotted in Figures 9.1, 9.4, and 9.7.
9.3.2
Specification test
The main idea of the specification tests is to check whether there
is still deterministic structure in the residuals. Two specification tests
are adopted.
The first test is to check whether the residuals are
auto-correlated. The second one is to test whether the residuals have
thick tails.

Time Modeling of Short-Term Interest Rates
169
Checking autocorrelation
Let U1,...,UN be identically distributed random variables with that
E[Ui] = 0, Var[Ui] = 1 and E|Ui|s < ∞, for all s ≥2. Let ˆRk be the sample
autovariance function
ˆRk =
1
N −k
N

i=k+1
UiUi−k.
Under the null we have E[ˆRk] = 0 and
Var[ˆRk] =
1
N −k ,
for k ≥1. We normalized ˆRk into
ˆrk =
ˆRk −E[ˆRk]

Var[ˆRk]
=

N −k ˆRk =
1
√
N −k
N

i=k+1
UiUi−k.
(9.9)
Consider the sequence (UiUi−k)i=k+1,...,N for a fixed k. It is near epoch
dependent on (Ui)i=1,...,N.7 Using the central limit theorem for near
epoch processes,8 ˆrk converges to N(0,1) in distribution as N →∞.
Applying the test for our discrete-time approximations, we let Ui =
Wi −Wi−1.
We remark here that ˆrk ∼N(0,1) means ˆRk ∼N(0,
1
N−k ). It is similar
with the result Var[ˆRk] ∼1/N in Box et al. (1994: 32) when N is large
enough.
Testing normality
We employ here χ2-test for histogram to test whether the distribution
of samples is N(0,1) distribution.9 The idea is to compare the relative
frequency of samples on intervals Im
ˆpm = number of {i;Ui ∈Im}
N
and pm the probability of N(0,1)-distribution on the intervals Im where
{Im,m = 1,...,M} are disjoint intervals of the real line.
The weighted distance
d =
M

m=1
N
pm(1 −pm)(ˆpm −pm)2
(9.10)

170
Chih-ying Hsiao and W. Semmler
measures the distance between the sample and the normal distributions.
It converges to χ2(M −1) in distribution as N →∞.
9.3.3
Results of estimating the CKLS model
In Tables 9.1, 9.2, and 9.3, the empirical results are reported. The first two
columns show the results of the Euler and Milstein approximations for
the CKLS model (9.1). The notations of the parameters are adjusted for
Section 9.4 later. All estimates in the drift coefficients are not significantly
different from zero. The forecast errors are given in the lower part of the
tables. We found that the CKLS model does not provide better data pre-
diction than a “naïve” forecast without any model. In the row “relative,”
the relative forecast errors comparing a “naïve” forecast are quoted. The
naïve forecast just uses today’s data to forecast the next period. The rela-
tive errors both for the in-sample and out-of-sample forecast are all about
100 percent or even above.
The estimated white noises based on the two methods are very sim-
ilar as plotted in Figures 9.2, 9.5, and 9.8. Figures 9.3, 9.6, and 9.9.
plot the normalized autocorrelations given in Equation (9.9) for the
Euler approximation. The normalized autocorrelations should be within
[−2,+2] band. However, in the figures they are about 3.5 for Germany
and the UK and about 5 for the USA. This finding indicates strong
autocorrelation in the estimated residuals. Durbin (1970) and Box and
Pierce (1970) have pointed out that the sample autocorrelations will be
underestimated for close time differences.10 In this case, the underesti-
mation indicates an even stronger autocorrelation than the values given
above. As a reference, we run a Monte Carlo simulation for 1,000 repeti-
tions using the result of the US estimations. Most of them (96 percent)
have the maximal normalized autocorrelations smaller than 2.8 (we take
the first ten normalized autocorrelations), and the maximal of them
is only 4.2.
We also observe that the estimated residuals are more concentrated
around zero than the standard normal distribution, which implies they
have thick tails.11 This fact can be inferred from Figures 9.2, 9.5, and 9.8,
and the large d-statistics of the normality test in Tables 9.1–9.3 indicate
that the distributions of the residuals are far from a normal distribution.
9.4
Searching for new models
Because of the results that show high correlations and thick tails for the
model (9.1) shown in the last section we search for new models.

Time Modeling of Short-Term Interest Rates
171
10
9
8
7
6
5
Short rate (%)
4
3
2
1980
1984
1988
1992
1996
2000
2004
Call money rate in Germany
Figure 9.1
Call money rate, Germany
0.32
0.28
0.24
0.20
0.16
0.12
Relative frequence
0.08
0.04
0.00
–6
–4
–2
0
2
Euler
Milstein
Normal
Estimated white noise
4
6
Figure 9.2
Distribution of estimated white noise (I), Germany

172
Chih-ying Hsiao and W. Semmler
4
3
2
1
0
–1
Normalized autocorrelation
–2
0
4
8
12
16
20
CKLS
LARMA
LARMA–ARCH
24
Lags
Figure 9.3
Normalized autocorrelation of the estimated noise, Germany
16
14
12
10
Short rate (%)
8
6
1980
1984
1988
1992
1996
Interbank rate in UK
2000
2004
4
Figure 9.4
Interbank rate, UK

Time Modeling of Short-Term Interest Rates
173
Euler
0.36
0.32
0.28
0.24
0.20
0.16
0.12
Relative frequence
0.08
0.04
0.00
–6
–4
–2
0
2
4
6
Estimated white noise
Milstein
Normal
Figure 9.5
Distribution of estimated white noise (I), UK
CKLS
4
3
2
1
0
–1
–2
0
4
8
12
Lags
16
20
24 
Normalized autocorrelation
LARMA
LARMA–ARCH
Figure 9.6
Normalized autocorrelation of the estimated noise, UK

174
Chih-ying Hsiao and W. Semmler
12
10
8
6
Short rate (%)
4
2
1980
1984
1988
1992
1996
2000
2004
Federal funds rate in USA
Figure 9.7
Federal funds rate of the USA
Euler
0.32
0.28
0.24
0.20
0.16
0.12
0.08
Relative frequence
0.04
0.00
–6
–4
–2
0
2
4
6
Estimate white noise
Milstein
Normal
Figure 9.8
Distribution of estimated white noise (I), USA

Time Modeling of Short-Term Interest Rates
175
CKLS
5
4
3
2
1
0
Normalized autocorrelation
–1
–2
–3
0
4
8
12
16
20
24
Lags
LARMA
LARMA–ARCH
Figure 9.9
Normalized autocorrelation of the estimated noise, USA
9.4.1
Improvement in the continuous-time framework
In the literature, there are further works to improve the model (9.1)
for modeling the short-term rate in the framework of continuous-
time models. For example, Ait-Sahalia (1996) suggests a nonlinear drift
coefficient:
drt = (α0 + α1rt + α2r2 + α3
rt
)dt +

β0 + β1rt + β2rβ
3 dWt
and Andersen and Lund (1997) suggest a stochastic volatility model:
drt = κ1(µ −rt)dt + σtrγ
t dW1t,
d logσ 2
t = κ2(α −logσ 2
t )dt + ξdW2t.
We simulate data using the models specified in Ait-Sahalia (1996) and
Andersen and Lund (1997).12 We plot them in Figures 9.10 and 9.11.
The model of Ait-Sahalia cannot reproduce a similar time series of the
real data. It stays always in a narrow band around the steady state. The
normalized autocorrelation functions from these two models are plotted
in Figure 9.12. We observe that there is no extreme autocorrelation in
the estimated noise.

176
Chih-ying Hsiao and W. Semmler
Table 9.1
Results of estimation and forecast for Germany
Milstein
Euler
Euler
Euler
Germany
CKLS
CKLS
LALARMA
LARMA-ARCH
Model Identification
p
1
{1,6}
{1,6}
q
0
0
0
k
0
0
{1,7}
α0(c)
0.020
0.017
0.068
0.065
(t-stat.)
(0.37)
(0.34)
(1.38)
(1.74)
α1(−β)
−0.007
−0.007
0.095
0.079
(−0.73)
(−0.71)
(3.89)
(3.54)
α6
−0.107
−0.091
(−4.28)
(−4.01)
γ
0.417
0.378
0.186
0.485
(2.21)
(2.01)
(1.00)
(2.14)
c0(σ)
0.113
0.122
0.153
0.062
(3.11)
(3.11)
(3.16)
(2.48)
c1
0.297
(2.43)
c7
0.272
(2.47)
Log-Likelihood
0.0054
0.0054
0.0061
0.0067
d-Statistics (χ2)
161
160
95
31
(p-value)
(1.78e−25)
(2.91e−25)
(6.39e−13)
(0.02)
Avg. Forecast Errors
- Level Forecast
In Sample
0.0540%
0.0541%
0.0439%
0.0441%
(Relative)
(99%)
(99%)
(90%)
(90%)
Out of Sample
0.0192%
0.0193%
0.0153%
0.0156%
(Relative)
(100%)
(100%)
(79%)
(81%)
- Volatility Forecast
In Sample
0.0144%
0.0144%
0.0090%
0.0082%
Out of Sample
0.0017%
0.0017%
0.0015%
0.0013%
9.4.2
Modeling autocorrelations in the estimated noise
We employ the ARMA process13 to model the autocorrelation of the
estimated noise
Wt =
p

i=1
φiWt−i +
q

j=0
ψiεt−j.
(9.11)

Time Modeling of Short-Term Interest Rates
177
Table 9.2
Results of estimation and forecast for UK
Milstein
Euler
Euler
Euler
United Kingdom
CKLS
CKLS
LALARMA
LARMA-ARCH
Model Identification
p
{1}
{1}
{1}
q
0
{1}
{1}
k
0
0
{1}
α0(c)
0.153
0.155
0.289
0.210
(t-stat.)
(1.30)
(1.23)
(1.63)
(1.71)
α1(−β)
−0.018
−0.019
−0.034
−0.025
(−1.25)
(−1.26)
(−1.67)
(−1.71)
β1
0.431
0.313
(5.38)
(2.18)
γ
0.974
0.742
0.574
0.527
( 4.97)
( 3.45)
(2.91)
(2.21)
c0(σ)
0.067
0.115
0.157
0.136
( 2.31)
( 2.11)
(2.29)
(1.86)
c1
0.498
(2.31)
Log-Likelihood
0.00038
0.00019
0.00052
0.00091
d−Statistics (χ2)
1639
1675
349
235
(p-value)
(0.00)
(0.00)
(9.59e−64)
(2.22e−40)
Avg. Forecast Errors
- Level Forecast
In Sample
0.3668%
0.3886%
0.3155%
0.3212%
(Relative)
(99%)
(99%)
(85%)
(87%)
Out of Sample
0.0701%
0.0701%
0.0777%
0.0714%
(Relative)
(105%)
(105%)
(116%)
(107%)
- Volatility Forecast
In Sample
1.1705%
1.1503%
0.6469%
0.8050%
Out of Sample
0.0218%
0.0306%
0.0298%
0.0277%
If the noise Wt has an autoregressive coefficient of order one then
Wt = φWt−1 + εt.
By replacing Wt using (9.7), we obtain
Xt −(c −βXt−1)
σXγ
t−1
= φ Xt−1 −(c −βXt−2)
σXγ
t−2
+ εt.

178
Chih-ying Hsiao and W. Semmler
Table 9.3
Results of estimation and forecast for USA
Milstein
Euler
Euler
Euler
US
CKLS
CKLS
LALARMA
LARMA-ARCH
Model Identification
p
1
{1,2}
{1,2}
q
0
0
0
k
0
0
{1,6}
α0(c)
0.048
0.047
0.055
0.028
(t-stat.)
(1.03)
(1.01)
(1.23)
(0.64)
α1(−β)
−0.010
−0.010
0.361
0.456
(−1.22)
(−1.20)
(5.219)
(6.11)
α2
−0.371
−0.461
(−5.39)
(−6.29)
γ
0.827
0.839
0.767
0.808
(5.70)
(5.74)
(5.25)
(3.57)
c0(σ)
0.055
0.054
0.057
0.037
(3.70)
(3.68)
(3.68)
(2.23)
c1
0.225
(1.26)
c6
0.330
(2.07)
Log-Likelihood
0.0050
0.0050
0.0054
0.0057
d-Statistics (χ2)
65
63
76
36
(p-value)
(1.32e−7)
(3.43e−7)
(2.33e−9)
(0.0053)
Avg. forecast errors
- Level forecast
In sample
0.0732%
0.0732%
0.0614%
0.0618%
(Relative)
(99%)
(99%)
(82%)
(83%)
Out of sample
0.0252%
0.0252%
0.0190%
0.0187%
(Relative)
(102%)
(102%)
(77%)
(76%)
- Volatility forecast
In sample
0.0256%
0.0256%
0.0183%
0.0178%
Out of sample
0.0020%
0.0020%
0.0017%
0.0014%
Rearranging it we obtain:
Xt = (c −βXt−1) + φ
Xt−1
Xt−2
γ
(Xt−1 −(c −βXt−2)) + σXγ
t−1εt.
(9.12)

Time Modeling of Short-Term Interest Rates
179
3.78
3.76
3.74
3.72
3.70
3.68
Interest rate %
3.66
3.64
3.62
0
20
40
60
80
100
120
140
160
180 200
Month
Figure 9.10
Simulated data from Ait-Sahalia’s model
7
6
5
4
3
2
Short rate (%)
1
0
0
2
4
6
8
10
12
14
16
18
20
Year
Figure 9.11
Simulated data from Andersen-Lund’s model

180
Chih-ying Hsiao and W. Semmler
Ait–Sahalia
1.5
1.0
0.5
0.0
–0.5
–1.0
–1.5
Normalized autocorrelation
–2.0
–2.5
0
4
8
12
16
20
24
Lags
Andersen–Lund
Figure
9.12
Normalized
autocorrelation
of
the
estimated
noise
for
the
continuous-time models
Rewriting (9.12) using the approximation ( Xt−1
Xt−2 )γ ≈1, we obtain a model
with two lags in the drift term
Xt = α0 + α1Xt−1 + α2Xt−2 + σXγ
t−1εt.
So, the noise Wt, with an autocorrelation of order one, gives us an
model with two lags. Using this idea, we give the general structure as:
Xt = α0 +
p

i=1
αiXt−i + Xγ
t−1


q

i=0
βiεt−i

.
(9.13)
9.4.3
Modeling thick tails in the estimated noise
For modeling thick tails of the noise we employ the idea of Brenner et al.
(1996) and Koedijk et al. (1997). The common feature of their construc-
tions is that they apply the ARCH14 to model the thick tail. Moreover,
the conditional variance (the volatility) of Xt is level-dependent. Bren-
ner et al. (1996) argue that both level and ARCH effects are significant
for short-term rates. We follow their idea and build the ARCH-structure
into the model (9.13) where εt is N(0,ht) distributed with
ht = c2
0 +
k

i=1
ciε2
t−i.
(9.14)

Time Modeling of Short-Term Interest Rates
181
We employ (9.13) and (9.14) as our model class to model short rates.
For the unique specification of the parameter we normalize β0 = 1. We
have a more general model than Brenner et al. (1996) by considering
the ARMA structure (9.13). This can correct the autocorrelations of the
residuals.15 We note that we employ the ARCH structure instead of the
GARCH structure in Brenner et al. (1996). The GARCH model is a techni-
cal improvement over the ARCH model16 when the lags of ε2
t are long.
The results during the model-identification stage suggest we do not need
to employ the GARCH structure.
9.4.4
Results
In Tables 9.1, 9.2, and 9.3, we report the empirical results for the short
rate of Germany, the UK, and the USA. The first and second columns are
results of the CKLS model (1) using the Euler and the Milstein approxi-
mation as mentioned. The third and fourth columns report the results of
the ARMA and the ARMA-ARCH models, respectively. The abbreviation
“LARMA” denotes “level + ARMA” meaning the ARMA structure with a
level effect.
The “Model Identification” in the tables means the determination
of the orders p, q, and k in (9.13) and (9.14). We follow the stan-
dard procedure of Box et al. (1994). p and q are determined based on
the autocorrelation function of εt. Next, k is chosen according to the
autocorrelation function of ε2
t . The procedure chooses the most par-
simonious model where the estimated noise does not have significant
autocorrelations.
The parameters of the drift coefficients α are not significant in the CKLS
model (the t-statistics are quoted in parenthesis). However, they become
significant after the ARMA and ARMA-ARCH structures are introduced in
the third and fourth column (with the UK as an exception). All likelihood
values increase when the ARMA structure is considered and are improved
further when the ARCH components are introduced.
The forecast errors are reported in the tables for both the in-sample and
the out-of-sample forecasts. According to (9.13), the predictor of Xt+1 in
the LARMA and the LARMA-ARCH model is given by:
ˆXt+1 = Et[Xt+1]( ˆθ) = Xt + ˆα0 +
p

i=1
ˆαiXt−i+1 + X ˆγ
t ( ˆβ1εt + ... + ˆβqεt−q+1).
Thus, the forecast error of the level is the difference:
Xt+1 −ˆXt+1 = X ˆγ
t εt+1

182
Chih-ying Hsiao and W. Semmler
and the forecast error of volatility is given by:
(Xt+1 −ˆXt+1)2 −Et[(Xt+1 −ˆXt+1)2] = (X ˆγ
t εt+1)2 −X2 ˆγ
t
ˆht.
We observe in Tables 9.1, 9.2, and 9.3 that the in-sample and out-of-
sample forecasts have improved, with the exception of the out-of-sample
level forecast for the UK. We relate this improvement with the results that
all estimates become significant after the introduction of the ARMA and
ARMA-ARCH structure (again with the exception of the drift coefficients
for the UK).
We can see that the major improvement of the level forecast is due to
the introduction of the ARMA structure and the ARMA-ARCH structure
contributes to the forecast improvement of volatility. The parameter γ is
significantly different from zero for all three countries. This corresponds
to the existence of the level effect in Brenner et al. (1996). For the data of
Germany and the UK, the estimates of the parameter γ are not far from
0.5 as in the model of Cox et al. (1985).
The normalized autocorrelations with respect to the lags are plotted in
Figures 9.3, 9.6, and 9.9. The normalized autocorrelations for the chosen
LARMA and LARMA-ARCH models are controlled within [−2,+2]. The
distribution of the noise can be found in Figures 9.13, 9.14, and 9.15,
and the χ2-statistics for the normality test are reported in Tables 9.1–9.3.
CKLS
0.32
0.28
0.24
0.20
0.16
0.12
Relative frequence
0.08
0.04
0.00
–6
–4
–2
0
2
4
6
Estimated white noise
LARMA
LARMA–ARCH
Normal
Figure 9.13
Distribution of estimated white noise (II), Germany

Time Modeling of Short-Term Interest Rates
183
0.36
0.32
0.28
0.24
0.20
0.16
0.12
Relative frequence
0.08
0.04
0.00
–6
–4
–2
0
2
4
6
Estimated white noise
CKLS
LARMA
LARMA–ARCH
Normal
Figure 9.14
Distribution of estimated white noise (II), UK
0.32
0.28
0.24
0.20
0.16
0.12
Relative frequence
0.08
0.04
0.00
–6
–4
–2
0
2
4
6
Estimated white noise
CKLS
LARMA
LARMA–ARCH
Normal
Figure 9.15
Distribution of estimated white noise (II), USA
Although we already have reduced the concentration of the distributions
by introducing the ARCH structure, we still note that they are signifi-
cantly different from the normal distribution at the 5 percent level. The
distance is greatest for the short rate in the ÚK.

184
Chih-ying Hsiao and W. Semmler
Comparing all three countries, we can observe that the modeling of
the short rate for the UK is less successful. The t-statistics of the esti-
mated parameters are not significantly different from zero, and the
distance between the distribution of the estimated noise and the nor-
mal distribution is still sizeable, even after the introduction of the ARCH
structure.
The parameters p,q, and k are the model identification parameters as
given in Equation (9.13) and (9.14). In the parenthesis are t-statistics.
d-Statistics is χ2-distributed given by Equation (9.10). The relative in-
sample forecast error in level is 99 percent of the error of the naive
forecast. The naive forecast assumes the value in the next period is just
that of today.
9.5
Conclusions
The objective of this chapter is to empirically model the short-term inter-
est rates. We begin with the continuous-time CKLS model (9.1), and we
apply the Euler, Milstein, and NLL approximations. For evaluating the
quality of the discrete-time approximations, we compare the errors of the
parameter estimations and the one-step-ahead predictions. Our results
do not show an improvement of the NLL and Milstein approximations
over the Euler approximation frequently found in the literature. The NLL
approximation is equivalent to the Euler approximation due to the lin-
earity of the drift coefficient. The Milstein and the Euler approximations
behave similarly.
We apply the Euler and the Milstein approximations to the short-term
interest rates of Germany, the UK, and the USA. It indicates evidence
of model misspecification where the estimated residuals have high auto-
correlation and thick tails. We show that two further continuous-time
models of Ait-Sahalia (1996) and Andersen and Lund (1997) cannot suf-
ficiently model the autocorrelation of the estimated white noise either.
Therefore, we decide to model the short rates in a discrete-time frame-
work. The model of the ARMA-ARCH structure with level-dependent
volatility copes with the autocorrelation problem successfully. This
model can also provide higher likelihood values and improve the level
and volatility forecasts by a significant amount. However, the results
regarding the distribution normality of the residuals display only a mod-
erate success. In addition, the out-of-sample level forecasts of the UK data
do not show marked improvements. This suggests one needs to broaden
the framework and consider other models such as the multifactor and
regime-switching models.

Time Modeling of Short-Term Interest Rates
185
Notes
1. If the process deviates from c
β (the mean), for example, Xt > c
β , then the
process is drifting down and it is pulled up when Xt < c
β .
2. The application of the Milstein method for approximating diffusion processes
is independently developed by the authors. In the appendix of this chapter
we present our application and show that it is equivalent to that of Elerian
(1998).
3. It means the ML estimator by using the Euler method.
4. See Kloeden and Platen (1992: 345).
5. See Kloeden and Platen (1992: Chap.10).
6. See http://www.ub.uni-bielefeld.de/english/library/databases/, then choose
International Statistical YearBook 2000, for “Datenbank” choosing “OECD”
and “main economic indicators”, for “Period” choose “monthly data”, for
“Search” choose “indicator-search”, then “interest rates”, then “immediate
rates”.
7. See Gallant and White (1988) Def. 3.13, p. 27 with Zni = UiUi−k. One can see
vm = 0 when m ≥k.
8. See Gallant and White (1988), Theorem 5.3, p. 76. The conditions of the
theorem are satisfied because under null (Ui) is independent and vn = n −k.
9. See Breiman (1973: 189).
10. The is why the “Q-statistic” is developed, see Box and Pierce(1970) and Ljung
and Box(1978).
11. Because the variance is normalized to 1. The concentration of the distribution
around 0 leads to a smaller variance. In order to keep the variance as 1, there
must be more weight in the tail.
12. We undertake simulation with an interval 0.01 and then pick up the simulated
series with an interval, 1.
13. See Box, Jenkins and Reinsel (1994).
14. See Engle (1982).
15. See Brenner et al. (1996) p. 95 “The Ljung-Box Q(εt/σt) statistics indicate that
both models have significant serial correlation in the residuals.”
16. See Bollerslev (1986).
References
Ait-Sahalia, Y. (1996) “Testing Continuous-Time Models of the Spot Interest Rate,”
Review of Financial Studies, 9 (2): 385–426.
Ait-Sahalia, Y. (1997) “Maximum Likelihood Estimation of Discretely Sampled
Diffusions: A Closed-Form Approximation Approach,” Econometrica, 70 (1):
223–262.
Ait-Sahalia, Y. (1999) “Transition Densities for Interest Rate and Other Nonlinear
Diffusions,” Journal of Finance, 54 (4): 1361–1395.
Andersen, T. G. and Lund, J. (1997) “Estimating Continuous-Time Stochastic
Volatility Models of the Short-Term Interest Rate,” Journal of Econometrics, 77
(1): 343–377.

186
Chih-ying Hsiao and W. Semmler
Bollerslev, T. (1986) “Generalized Autoregressive Conditional Heteroscedasticity,”
Journal of Econometrics, 31 (3): 307–327.
Box, G. E. P., Jenkins, G. M., and Reinsel, G. C. (1994) Time Series Analysis, 3rd
edn, Englewood Cliffs, NJ: Prentice Hall.
Box, G. E. P. and Pierce, D. A. (1970) “Distribution of Residual Autocorrelations in
Autoregressive-Integrated Moving Average Time Series Models,” Journal of the
American Statistical Association, 65 (332): 1509–1526.
Breiman, L. (1973) Statistics, Boston, Mass.: Houghton Mifflin.
Brenner, R. J., Harjes, R. H., and Kroner, K. F. (1996) “Another Look at Models of
the Short-Term Interest Rate,” Journal of Financial and Quantitative Analysis, 31
(1): 85–107.
Chan, K. C., Karolyi, G. A., Longstaff, F. A., and Sanders, A. B. (1992) “An Empirical
Comparison of Alternative Models of the Short-Term Interest Rate,” Journal of
Finance, 47 (3): 1209–1227.
Cox, J. C., Ingersoll, J. E., and Ross, S. A. (1985) “An Intertemporal General
Equilibrium Model of Asset Prices,” Econometrica, 53 (2): 363–384.
Cox, J. C., Ingersoll, J. E. and Ross, S. A. (1985) “A Theory of the Term Structure
of Interest Rates,” Econometrica, 53 (2): 385–407.
Dacunha-Castelle, D. and Florens-Zmirou, D. (1986) “Estimation of the Coeffi-
cients of a Diffusion from Discrete Observations,” Stochastics, 19 (4): 263–284.
Duffie, D. and Glynn, P. (2004) “Estimation of Continuous-Time Markov Processes
Sampled at Random Time Intervals,” Econometrica, 72 (6): 1773–1808.
Durbin, J. (1970) “Testing for Serial Correlation in Least-Squares Regression When
Some of the Regressors Are Lagged Dependent Variables,” Biometrika, 38 (3):
410–421.
Elerian, O. (1998) “A Note on the Existence of a Closed Form Conditional Tran-
sition Density for the Milstein Scheme,” Nuffield College Economics Working
Papers 1998-W18.
Engle, R. F. (1982) “Autoregressive Conditional Heteroscedasticity with Estimates
of the Variance of United Kingdom Inflation,” Econometrica, 50 (4): 987–1007.
Frohn, J. (1995) Grundausbildung in Oekonometrie, 2nd edn, Berlin: Walter de
Gruyter.
Fuller, W. A. (1996). Introduction to Statistical Time Series, 2nd edn, New York: Wiley.
Gallant, A. R. and Tauchen, G. (1996) “Which Moments to Match?” Econometric
Theory, 12 (4): 657–681.
Gallant, A. R. and White, H. (1988) A Unified Theory of Estimation and Inference for
Nonlinear Dynamic System, Oxford: Blackwell.
Gourieroux, C., Monfort, A., and Renault, E. (1993) “Indirect Inference,” Journal
of Applied Econometrics, 8 (S): S85–S118.
Hansen, L. A. and Scheinkman, J. A. (1995) “Back to the Future: Generating
Moment Implications for Continuous-Time Markov Processes,” Econometrica,
63 (4): 767–804.
Karatzas, I. and Shreve, S. E. (1991) Brownian Motion and Stochastic Calculus, New
York: Springer.
Koedijk, K. G., Nissen, F. G. J. A., Schotman, P. C. and Wolff, C. C. P. (1997)
“The Dynamics of Short-Term Interest Rate Volatility Reconsidered,” European
Finance Review, 1 (1): 105–130.
Ljung, G. M. and Box, G. E. P. (1978) “On Measure of Lack of Fit in Time Series
Models,” Biometrika, 65 (2): 297–303.

Time Modeling of Short-Term Interest Rates
187
Lo, A. W. (1988) “Maximum Likelihood Estimation of Generalized Ito Processes
with Discretely Sampled Data,” Econometric Theory, 4 (August): 231–247.
Pedersen, A. R. (1995). “A New Approach to Maximum Likelihood Estimation for
Stochastic Differential Equations Based on Discrete Observations,” Scandinavian
Journal of Statistics, 22 (1): 55–71.
Shoji, I. and Ozaki, T. (1997) “Comparative Study of Estimation Methods for
Continuous Time Stochastic Processes,” Journal of Time Series Analysis, 18 (5):
485–506.
Shoji, I. and Ozaki, T. (1998) “Estimation for Nonlinear Stochastic Differential
Equations by Local Linearization Method,” Stochastic Analysis and Applications,
16 (4): 733–752.
Thompson, S. B. (2002) “Evaluating the Goodness of Fit of Conditional Distribu-
tions, with an Application to Affine Term Structure Models,” Working Paper,
Department of Economics, Harvard University.
Vasicek, O. (1977) “An Equilibrium Characterization of the Term Structure,”
Journal of Financial Economics, 5 (1): 177–188.

10
Testing the Expectations
Hypothesis in the Emerging
Markets of the Middle East: An
Application to Egyptian and
Lebanese Treasury Securities
Sam Hakim and Simon Neaime
10.1
Introduction
For many years, and despite many rejections,1 the expectations hypoth-
esis remains the widely accepted premise believed to explain the shape
of the yield curve. In its simplest form, the expectations theory sug-
gests that the current long-term interest rate is a weighted average of
current and expected future short-term rates. In this setting, the spread
between long- and short-term rates predicts future changes in short rates.
Changes in the slope of the yield curve depend on interest expectations,
with steeper yield curves foreboding greater expectations of rate changes.
This chapter focuses on testing the expectations hypothesis in two
emerging capital markets. The theory assumes that securities of differ-
ent maturities are substitutes and investors’ arbitrage away yield spreads,
which are caused by the relative excess supply or demand of a particu-
lar security over the term structure. Specifically, investors shift from one
maturity sector to another in order to take advantage of yield differentials
due to differences between expectations and forward rates. In this frame-
work, the term structure is shaped by market expectations regarding the
future direction of rates.
To evaluate the validity of the expectations hypothesis in the Mid-
dle East, we analyze the stochastic nature of interest rates representing
the yields on securities for the entire maturity spectrum of the Egyp-
tian and Lebanese term structures. To our knowledge, this is the first
time that a study of the term structure in Middle Eastern countries has
188

Expectations Hypothesis in the Emerging Markets
189
been undertaken despite the popularity of the region’s fixed income
instruments amongst mutual and hedge funds investing in emerging
markets.2 Our findings show that Egyptian and Lebanese interest rates
are non-stationary and can be modeled as unit-root processes. Further
investigation of their common relations showed that the interest rates
in each country are bound by a cointegrating relation and that a unique
common trend between them exists. This property suggests that Egyp-
tian and Lebanese interest rates do not diverge consistently apart from
one another and that a change in one interest rate is rapidly transmitted
to the entire term structure. Overall, our results lend theoretical support
to the expectations hypothesis and confirm the analysis of bond markets
in more mature economies.
The remainder of this chapter is organized as follows. Section 10.2
briefly examines the empirical and theoretical literature on the term
structure. Section 10.3 describes the data and provides descriptive statis-
tics. The tests for unit roots are done in Section 10.4. We investigate the
cointegrating relations between interest rates in each of the two coun-
tries and discuss the results in Section 10.5. Section 10.6 concludes this
chapter.
10.2
The existing literature
The recent theoretical underpinnings of the term structure assume that
the yield curve is represented by a stochastic process. Several models
have evolved. In single state models, all yields, and correspondingly all
discount bonds, are affected by movements in the short rate. Given the
spot-rate dynamics and the structure of the market price of interest rates,
default-free bonds of all maturities can be priced (Cox et al. 1985). Two
factor models of the term structure were also developed by Brennan and
Schwartz (1979). By and large, the interest rate is assumed to follow an
Ornstein–Uhlenbeck – or mean-reverting – process, where the underlying
distribution is normal. Unfortunately, this last property has the perverse
implication that interest rates could also become negative, a likelihood
largely mitigated by an appropriate choice of parameters of the stochastic
process or by imposing certain boundary restrictions.
In general, the single-factor models are based solely on the initial short-
term rate and overlook any other information on rates which can be
imputed from the yield curve. Models that incorporate more information
include Heath et al. (1992), Ritchken and Sankarasubramanian (1995),
and Hull and White (1996).

190
S. Hakim and S. Neaime
The empirical literature on the term structure includes Engel et al.
(1987) who pioneered the use of autoregressive conditional heteroscedas-
tic models in the analysis of interest-rate series. This versatility allows
for the conditional variance to affect the excess holding yield on a long-
term bond. Their approach leads to a time-varying premia on securities
of different maturities and a relaxation of the assumption of constant
heteroscedasticity in the disturbances, based on earlier results obtained
by Shiller (1979) and Campbell and Shiller (1987).
Historical support for the expectations hypothesis in the USA is docu-
mented in Bradley and Lumpkin (1992) and Hall et al. (1992), who find
the rates for treasury securities cointegrated with unit roots.3 Similar con-
clusions drawn from the analysis of British and Danish data is found in
McDonald and Speight (1988), Mills (1991), Lee and Tse (1991), Taylor
(1992), and Engsted and Tangaard (1994). More recently, Beechey et al.
(2009) also found evidence of the expectations hypothesis in eight devel-
oped and six emerging economies. Nevertheless, there is also mixed
evidence documented in Boothe (1991), Hall et al. (1992), Zhang (1993),
and Lardic and Mignon (2004). The academic attention to interest rates
in the Middle East is small but growing. Instead of interest rates, studies
have focused on the region’s thriving equity markets and the more tradi-
tional currency exchange rates. For example, Hammoudeh et al. (2009)
examine the co-movements among the prices of four strategic commodi-
ties and their causal relationships with interest and exchange rates. The
goal is to shed some light on the predictive behavior of those individ-
ual commodity prices relative to the selected financial variables and to
establish a transmission link between commodity prices and the dollar
exchange rate. Another set of studies examined the spread on sovereign
bonds and how these measures are influenced either by the geopoliti-
cal landscape of the region (Haddad and Hakim 2007, 2009) or by US
macroeconomic news (Ozatay et al. 2009).
10.3
Data and diagnostic statistics
Our data consists of the weekly yields on Egyptian treasury securities auc-
tioned between July 21, 2006, and April 3, 2009, in five maturity sectors:
one year, two years, three years, five years, and seven years. Treasury secu-
rities have only recently been auctioned in Egypt, and, therefore, there is
a lot of interest to determine the efficiency of the term structure for that
country. For Lebanon, our data is based on monthly observations since
these securities were first introduced in 1991 as a tool of monetary policy.
The data period for Lebanon covers October 1991 through to February

Expectations Hypothesis in the Emerging Markets
191
3
4
5
6
7
8
9
10
11
12
13
Jul-06
Aug-06
Sep-06
Oct-06
Nov-06
Dec-06
Jan-07
Feb-07
Mar-07
Apr-07
May-07
Jun-07
Jul-07
Aug-07
Sep-07
Oct-07
Nov-07
Dec-07
Jan-08
Feb-08
Mar-08
Apr-08
May-08
Jun-08
Jul-08
Aug-08
Sep-08
Oct-08
Nov-08
Dec-08
Jan-09
Feb-09
Mar-09
1Y
2Y
3Y
5Y
7Y
Figure 10.1
Egyptian treasury securities
0
5
10
15
20
25
30
35
40
Oct-91
Apr-92
Oct-92
Apr-93
Oct-93
Apr-94
Oct-94
Apr-95
Oct-95
Apr-96
Oct-96
Apr-97
Oct-97
Apr-98
Oct-98
Apr-99
Oct-99
Apr-00
Oct-00
Apr-01
Oct-01
Apr-02
Oct-02
Apr-03
Oct-03
Apr-04
Oct-04
Apr-05
Oct-05
Apr-06
Oct-06
Apr-07
Oct-07
Apr-08
Oct-08
3M
6M
12M
24M
Figure 10.2
Lebanese treasury securities
2009. The Lebanese treasury securities are auctioned by Banque du Liban,
the Lebanese central bank, and their yield is determined in a competi-
tive environment. The figures were obtained from the quarterly reports
published by the central bank. In both countries, the subscribers to the
treasury auctions include commercial banks, financial institutions, pub-
lic agencies, and private (domestic and foreign) buyers, most notably
mutual funds that invest in emerging markets. Figures 10.1 and 10.2

192
S. Hakim and S. Neaime
Table 10.1
Descriptive statistics yields on Egyptian and Lebanese treasury
securities
Lebanon
Egypt
3M
6M
1Y
2Y
1Y
2Y
3Y
5Y
7Y
Mean
11.38
12.87
14.17
15.65
8.94
9.08
9.13
10.00
10.24
Median
11.18
12.12
13.43
14.64
9
9.35
9.4
9.88
9.97
Mode
5.22
7.24
7.75
8.68
9
7.25
7.25
10.72
10.76
Standard
deviation
5.61
5.60
6.42
6.73
1.44
1.30
1.39
0.89
1.03
Kurtosis
1.53
1.50
1.48
−0.51
−0.65
−1.38
0.20
−1.17
−0.88
Skewness
0.95
1.03
1.09
0.64
0.18
−0.23
−0.71
0.11
0.39
Range
29.08
28.97
31.17
25.7
5.98
3.57
7.03
3.4
3.8
Minimum
5.1
6.31
6.68
7.89
5.75
7.25
3.79
8.15
8.45
Maximum
34.18
35.28
37.85
33.59
11.73
10.82
10.82
11.55
12.25
No. of
observations
209
209
209
209
120
120
120
120
120
Egypt: February 2006–April 2009 (weekly)
Lebanon: October 1991–April 2009 (monthly)
show the behavior of interest rates from the two countries over the study
periods.
The descriptive statistics of the term structure in each country are
provided in Table 10.1. The mean interest rate during the study period
ranged between 11.38 percent and 15.65 percent for Lebanon and 8.94
percent and 10.24 percent for Egypt. It appears that the term structure
in each country was upward-sloping as the interest rates increased with
longer maturity, an observation that is consistent with the normal shape
of the yield curve. The distribution of each maturity class over time is
not normal as is clear from the skewness statistic reported in Table 10.1
(a normal distribution has 0 skewness). The Lebanese interest rates are
skewed to the right while the Egyptian interest rates are mixed. Looking
at the standard deviation of the interest rates over time in relation to their
mean, we find that the two-year security in Lebanon has offered its hold-
ers the lowest risk per unit of return at 0.43 ( = 15.65/6.73). The best com-
parable rate in Egypt is the five-year treasury security at 0.09 ( = 0.89/10).
10.4
Tests of unit roots in Lebanese and Egyptian
interest rates
We begin by examining the stochastic nature of the yields offered on
the treasury securities across the Egyptian and Lebanese term structures.
We show that each set of series represents a unit-root process which we

Expectations Hypothesis in the Emerging Markets
193
assume can be written as:
yt = β + αyt−1 + ut
(10.1)
where β is a drift parameter. The process can be rewritten in first
difference form as:
yt = β + (α −1)yt−1 + ut
(10.2)
The test for unit root is essentially one which tests for α = 1. If the errors
are assumed to follow an AR (1) process
ut = ρut−1 + εt
(10.3)
the model can be rewritten as:
yt = Ztβ+(α −1)(ρ −1)yt−1 + αρyt−1 + εt
(10.4)
where Zt is the drift term. The new test is an Augmented Dickey Fuller
(ˆτ) test of (α −1)(ρ −1) = 0. Elliott et al. (1996) perform asymptotic
power calculations and show that the modified DF-GLS test can achieve
substantial power gain over the testing procedure outlined in (10.4). In
the DF-GLS test, we consider the same null hypothesis on the t-ratio
tests but critical values change as reported in Elliott et al. (1996). To see
whether our results are sensitive to serial correlation in the disturbances,
we ran the tests with AR (2), AR (3), and AR (4) errors4 without a change
in our results. In the end, we base the model selection on Schwartz’s
criterion.5
We also employ the KPSS test as developed in Kwiatkowski (1992) with
bandwidth set at 4 and Bartlett kernel. For the KPSS test, we perform
estimation with the modified Akaike information criterion (AIC).
The test statistics for all variables reported in Table 10.2 clearly reject
the null hypothesis of unit root in the differences but not in the lev-
els. This leads us to believe that each variable is an I(1) process, which
becomes stationary after differencing it once.
Overall, our results confirm the analysis of the bonds market in other
countries, notably Lee and Tse (1991), Mills (1991), Taylor (1992),
Engsted and Tangaard (1994), Chong et al. (2006), Kleimeier and Sander
(2006), De Graeve et al. (2007), and Liu et al. (2008).
The preceding findings suggest that the Lebanese and Egyptian inter-
est rates can be modeled as unit-root processes. As such, the variance
for each interest-rate series goes to infinity as the sample size increases.
Furthermore, from equation (10.1), any innovation ut has a permanent
effect on the value yt which can be written as a sum of all previous
innovations.

194
S. Hakim and S. Neaime
Table 10.2
Unit-root tests for interest-rate spreads of
Egyptian and Lebanese treasury securities
ADF-GLS (2 lags)
KPSS (4 lags)
Egypt
Spreads with 1Y Treasury
2Y–1Y
−2.48
0.28
**
3Y–1Y
−2.75
*
0.28
**
5Y–1Y
−2.62
*
0.4
**
7Y–1Y
−2.52
0.34
**
Lebanon
Spreads with 3m Treasury
6m–3m
−1.33
0.72
**
12m–3m
−3.5
**
1.27
**
24m–3m
−0.72
2.08
**
Significant at 10% (*) or 1 percent (**)
10.5
Testing the expectations hypothesis and
cointegration analysis
In this section, we turn our attention to the expectations hypothesis in
the term structure of each country. To that end, we begin with a simple
model of the expectations hypothesis of the term structure which can be
written as:
ym,t = 1
m ·
m−1

k=0
Et(y1,t+k) + m
(10.5)
where ym,t represents the yield on a pure discount treasury bond with
maturity m, E(.) is the expectations operator, and m is the term pre-
mium. Equation (10.5) suggests that the yield at time t of a pure discount
bond with m maturity can be written as the average expected yield on m
future bonds. In our case, we consider four specific yields with time to
maturity equal to three, six, twelve, and twenty-four months in Lebanon
and five specific yields for Egypt with maturities of one year, two years,
three years, five years, and seven years. These interest rates enable us
to construct three possible pairs for Lebanon and four pairs for Egypt
that obey equation (10.5) and define stationary interest-rate spreads.
These are:
Lebanon : {y6m,y3m},{y12m,y3m},{y24m,y3m}
Egypt : {y1,y2},{y1,y3},{y1,y5},{y1,y7}

Expectations Hypothesis in the Emerging Markets
195
Based on the results of the preceding section suggesting the unit-root
nature of the series, we now examine their cointegrating relationship.
Let Yt represents a k × 1 vector of non-stationary I(1) time series. A
k × r matrix of cointegrating vectors γ is said to exist if the linear com-
bination γ ′ Yt is stationary or I(0). Each cointegrating vector suggests
the existence of a long-term relationship between the series, namely an
equilibrium.
We define YLebanon ≡[y3m,y6m,y12m,y24m]′ as the vector of four inter-
est rates composing the Lebanese term structure. The expectations
hypothesis asserts that if each component of Yt is I(1), then the spreads
defined as Si(Lebanon) ≡yi −y3m for i = 6m, 12m, 24m may be I(0),
and, hence, any two yields must be cointegrated with cointegrating
vectors determined by the spread vectors. A similar vector YEgypt is
defined for the Egyptian term structure with the corresponding spreads
Sj(Egypt) ≡yj −y1y for j = 2y, 3y, 5y, and 7y. Table 10.3 reports the ADF-
GLS and KPSS tests for unit roots applied to the interest-rate spreads
in each country. The results of ADF-GLS are somewhat mixed but hold
more for the intermediate term spreads. For example, the Egyptian 7y–1y
interest-rate spread is non-stationary. The same applies to the 2y–1y
spread for Egypt and the 24m–3m and the 12m–3m for Lebanon. The
Table 10.3
Unit-root tests for yields on Egyptian and Lebanese treasury
securities∗
ADF–GLS (2 lags)
KPSS (4 lags)
Series
Levels
1st differences
Levels
1st differences
Egypt
1M
−1.12
−5.74
**
0.47
**
0.08
1Y
−1.47
−5.47
**
0.51
**
0.08
2Y
−1.41
−6.18
**
0.37
**
0.09
3Y
−1.45
−7.48
**
0.36
**
0.08
5Y
−1.30
−6.53
**
0.47
**
0.14
7Y
−1.29
−6.60
**
0.47
**
0.15
Lebanon
3M
−1.30
−8.93
**
3.72
**
0.02
6M
−1.08
−5.06
**
3.70
**
0.02
1Y
−1.29
−7.30
**
3.56
**
0.02
2Y
−0.22
−3.35
**
3.76
**
0.05
Significant at 10 percent (*) or 1 percent (**)
Egypt: 1-month, 1-year, 2-year, 3-year, 5-year, and 7-year maturity
Lebanon: 3-month, 6-month, 1-year, and 2-year maturity

196
S. Hakim and S. Neaime
KPSS tests are more consistent and show that all interest-rate spreads are
stationary in both countries.
When the expectations hypothesis holds, the spreads between the
long-term rate and the short-term rate provide information about
the future level of the short-term rate. However, if the fluctuations in
the short-term rate are unpredictable, the spread between long-term and
short-term rates cannot provide useful information about the market’s
expectation for the short-term rate unless the two rates share a cointe-
grating relation. Specifically, having established that the interest rates
are unit roots, they can be stationary in levels in the direction of the
cointegrating vector.
We now turn our attention to the cointegration analysis. This is impor-
tant because the lack of cointegration represents strong evidence against
the expectations hypothesis as there is no stable long-run relationship
between interest rates of different maturities.
To test for cointegration, we consider a multivariate model of the form:
Yt = µ + A1Yt−1 + A2Yt−2 + ··· + AqYt−q + εt
t = 1,2,···,T
(10.6)
where each Yt is an N-dimensional vector of yields defined above and εt’s
are independent k-dimensional Gaussian errors with covariance matrix
	. N represents the number of yields in each country (four for Lebanon,
and five for Egypt). The model can be written in difference form as:
Yt = µ + 
1Yt−1 + 
2Yt−2 + ··· + 
qYt−q + Yt−q + εt
(10.7)
where µ is a linear deterministic trend,

i ≡−I + A1 + A2 + ··· + Ai
(10.8)
 ≡−I + A1 + A2 + ··· + Aq
(10.9)
and I is the identity matrix. Note that equation (10.7) is equivalent to a
q dimensional VAR except for the term Yt−q. Note also that the inclu-
sion of the term Yt−q makes equation (10.7) an error-correction model,
where the matrix  contains the information about the cointegrating
relations. If there are r cointegrating vectors then  can be expressed as:
 = ϕγ ‘
(10.10)

Expectations Hypothesis in the Emerging Markets
197
where ϕ and γ are kxr matrices of rank r, 0 < r < k, and γ is a matrix of
cointegrating vectors. Therefore, the rank6 of  is also r. Johansen (1988)
and Johansen and Juselius (1990) maximize the likelihood function for
Yt conditional on the restrictions  = ϕγ‘. The likelihood ratio (LR) is
derived by applying least squares on the following equations:
Yt−q = µ + V1Yt−1 + V2Yt−2 + ··· + Vq−1Yt−q+1 + u0t
(10.11)
Yt = µ + W1Yt−1 + W2Yt−2 + ··· + Wq−1Yt−q+1 + u1t (10.12)
and computing the residual sample second-moment matrices:
ˆ00 = T−1
T

t=1
ˆu0t ˆu′
0t
ˆ11 = T−1
T

t=1
ˆu1t ˆu′
1t
ˆ10 = T−1
T

t=1
ˆu1t ˆu0t
(10.13)
where u0 and u1 are i.i.d. Under the null hypothesis H(r) that there are r
cointegrating vectors against the alternative of no cointegrating vectors,
the LR statistic, can be written as:7
−2 ln Q(H(r)|H0) = −T
n

i=r+1
ln(1 −ˆλi)
(10.14)
This is referred to as the λ-trace test, where ˆλr+1,..., ˆλn are the n −r
smallest eigenvalues that solve the detrimental equation:
|λ ˆ11 −ˆ10 ˆ−1
00 ˆ01| = 0
(10.15)
The λ-trace test statistics are provided in Table 10.4. The results reveal
the existence of a single cointegrating vector for Lebanon and three
cointegrating vectors for Egypt. Among the Lebanese treasury securi-
ties, there is a single common stochastic trend, and there are two among
the Egyptian securities. The number of trends is simply the difference
between the number of interest variables and the number of cointegrat-
ing vectors. Generally, with n yields to maturity, it is possible to form
n−1 linearly independent yield spreads. The yields are I(1) cointegrated
processes and the spreads between them represent cointegrating rela-
tions. If the expectations hypothesis is valid, this leaves three common

198
S. Hakim and S. Neaime
Table 10.4
Tests of cointegration of interest rates
Lebanon
Rank
Eigenvalue
Trace test
p-value
Lmax test
p-value
0
0.413
166.28
0.0000
110.29
0.0000
1
0.192
55.993
0.0000
44.341
0.0000
2
0.0491
11.653
0.1765
10.44
0.1878
3
0.0058
1.2131
0.2707
1.2131
0.2707
Cointegration vector: (12m) + 0.40(3m) −1.31(6m) −0.19(24m) = −1.04
Egypt
Rank
Eigenvalue
Trace test
p-value
Lmax test
p-value
0
0.366
129.80
0.000
53.732
0.000
1
0.245
76.068
0.000
33.125
0.0065
2
0.191
42.944
0.0007
25.021
0.0114
3
0.100
17.923
0.0195
12.447
0.0945
Cointegration vector: (1y) −0.42(2y) + 0.04(3y) −0.66(5y) −0.39(7y) = −5.10
Egypt: 1-month, 1-year, 2-year, 3-year, 5-year, and 7-year maturity
Lebanon: 3-month, 6-month, 1-year, and 2-year maturity
Egypt: February 2006–April 2009 (weekly)
Lebanon: October 1991–April 2009 (monthly)
non-stationary I(1) factors for Lebanon and two for Egypt that represent
exogenous elements to the system of yields, as, for example, the growth
in monetary aggregates which derives from the central bank’s monetary
policy. The evidence in support of a unique common factor is found in
several studies (Engle and Granger 1987; Stock and Watson 1988).
The cointegrating vectors for Egypt and Lebanon are:
Lebanese yields cointegrating vector:
(12m) + 0.40 (3m) −1.31 (6m) −0.19 (24m) = −1.04
Egyptian yields cointegrating vector:
(1y) −0.42(2y) + 0.04(3y) −0.66(5y) −0.39(7y) = −5.10
The preceding results suggest that Lebanese and Egyptian bond yields
do not drift apart from one another indefinitely. Even though each inter-
est rate is stochastic and non-predictable, the rates are linked together by
a stable and long-term relation. They move together over time, a basic
feature of the expectations theory.

Expectations Hypothesis in the Emerging Markets
199
10.6
Conclusion
This chapter tested the expectations hypothesis and found it to hold in
two emerging bond markets. We investigated in detail the time-series
properties of interest rates offered on distinct securities forming the
entire Egyptian and Lebanese term structures. The results showed that
long- and short-term interest rates are characterized as unit-root pro-
cesses with stationary spreads. This suggests that interest rates in each
country are well behaved in the sense that they do not diverge consis-
tently and permanently from one another. Further analysis showed that
it is appropriate to model the Egyptian and Lebanese term structures as
a cointegrated system. The results pointed to the existence of three coin-
tegrating vectors for Egypt and a single vector for Lebanon, a property
that suggests that the liquidity premia are stationary across the maturity
spectrum. Overall, our results offer hope for the development of capital
markets in other infant emerging economies, particularly in the Middle
East.
Notes
1. See Froot (1989) for a historical recap of the expectations hypothesis.
2. See Russian, Kazakh, Middle East bonds fill bulging pipeline.” Euroweek
(September 15, 2006): 25–25.
3. Campbell (1995) reviews the latest literature on the term structure, and Crock-
ett (1998) examines the assumptions underlying the expectations hypothesis.
4. MacKinnon (1990) provides a more complete set of critical values for ˆτ. A
non-parametric analog to ˆτ which allows for a wide range of serial correlation
and heterogeneity patterns was suggested by Phillips (1987a and 1987b) and
Phillips and Perron (1988). The critical values for the statistic are presented
in Phillips and Ouliaris (1990). However the finite sample properties of the
statistic are not fully investigated.
5. Schwartz’s (1978) criterion is defined as: BIC = log| ˆ	| + (p2q)T−1 logT where
p is the dimension of the VAR; q the order of the VAR model being tested
for q = m against q = m −1; m is the maximum order considered; and ˆ	 is the
estimated covariance of the errors. In effect, BIC includes a penalty adjustment
for the number of estimated parameters. Note that Schwartz’s (BIC) is similar
to Akaike’s Information Criterion (AIC) with the distinction that the former
can be shown to be strongly consistent.
6. Without arbitrary constraints it is impossible to uniquely identify the elements
of φγ ‘because for any rxr matrix , we have (ϕ−1)(γ ′) = ϕγ ′.
7. The test statistic has an asymptotic χ2 distribution with r(v-w) degrees of free-
dom where r is the number of cointegrating vectors, v the number of variables
in the VAR system, and w is the number of variables left in the VAR system
after testing the restrictions of the cointegrating relations. Note that if r = w,

200
S. Hakim and S. Neaime
then the null hypothesis places no restrictions on the cointegrating relations,
whereas if w = r, all the VAR system variables need to be I(0) under the null. In
general we have r ≤w ≤v.
References
Boothe, P. (1991) “Interest Parity, Cointegration, and the Term Structure in Canada
and the United States,” Canadian Journal of Economics, 24 (3): 499–516.
Beechey, M., Hjalmarsson, E., and Osterholm, P. (2009) “Testing the Expectations
Hypothesis When Interest Rates Are Near Integrated,” Journal of Banking and
Finance, 33 (5): 934–943.
Bradley, M. G. and Lumpkin, S. A. (1992) “The Treasury Yield Curve as a
Cointegrated System,” Journal of Financial and Quantitative Analysis, 27 (3):
449–463.
Brennan, M. and Schwartz, E. (1979) “A Continuous Time Approach to the Pricing
of Bonds,” Journal of Banking and Finance, 3 (2): 133–155.
Campbell, J. Y. (1995) “Some Lessons from the Yield Curve,” Journal of Economic
Perspectives, 9 (3): 1986–1998.
Campbell, J. Y. and Shiller, R. J. (1987) “Cointegration and Tests of Present Value
Models,” Journal of Political Economy, 95: 1062–1088.
Chong, B. S., Liu, M.-H., and Shrestha, K. (2006) “Monetary Transmission Via the
Administered Interest Rate Channels,” Journal of Banking and Finance, 30 (5):
1467–1484.
Cox J., Ingersoll, J., and Ross, S. (1985) “A Theory of the Term Structure of Interest
Rates,” Econometrica, 53 (2): 385–407.
Crockett, J. A. (1998) “Rational Expectations, Inflation and the Nominal Interest
Rate,” Journal of Econometrics, 83 (1–2): 349–363.
De Graeve, F., De Jonghe, O., and Vander Vennet, R. ( 2007) “Competition, Trans-
mission and Bank Pricing Policies: Evidence from Belgian Loan and Deposit
Markets,” Journal of Banking and Finance, 31: 259–278.
Engel, R. F. and Granger, W. J. (1987) “Co-Integration and Error Correction:
Representation Estimation and Testing,” Econometrica, 55: 251–276.
Engel, R. F., Lilien, D. M., and Robins, R. P. (1987) “Estimating Time Varying
Risk Premia in the Term Structure: The ARCH-M Model,” Econometrica, 55 (2):
391–407.
Engsted, T. and Tanggaard, C. (1994) “Cointegration and the US Term Structure,”
Journal of Banking and Finance, 18 (3): 167–181.
Froot, K. A. (1989) “New Hope for the Expectations Hypothesis of the Term
Structure of Interest Rates,” Journal of Finance, 44 (2): 283–305.
Haddad, M. and Hakim, S. (2008) “The Impact of War and Terrorism on Sovereign
Risk in the Middle East,” Journal of Derivatives and Hedge Funds, 14: 237–250.
Haddad, M. and Hakim, S. (2007) “The Cost of Sovereign Lending in the Middle
East after September 11,” Journal for Global Business Advancement, 1 (1): 127–139.
Hall, A. D., Anderson, H. M., and Granger, C. W. (1992) “A Cointegration Analysis
of Treasury Bill Yields,” The Review of Economics and Statistics, 74 (2): 117–126.
Hammoudeh, S., Sari, R., and Ewing, B. (2009) “Relationships among Strate-
gic Commodities and with Financial Variables: A New Look,” Contemporary
Economic Policy, 27 (2): 251–264.

