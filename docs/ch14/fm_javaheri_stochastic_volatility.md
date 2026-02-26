# Stochastic Volatility Models & Pricing

!!! info "Source"
    **Inside Volatility Arbitrage: The Secrets of Skewness** by Alireza Javaheri, Wiley, 2005.
    These notes are used for educational purposes.

## Stochastic Volatility and Derivatives Pricing

Illustrations
xi
2.26
Comparison of EKF Filtering Errors for Heston, GARCH,
and 3/2 Models.
123
2.27
Comparison of UKF Filtering Errors for Heston, GARCH,
and 3/2 Models.
123
2.28
Comparison of EPF Filtering Errors for Heston, GARCH,
and 3/2 Models.
124
2.29
Comparison of UPF Filtering Errors for Heston, GARCH,
and 3/2 Models.
124
2.30
Comparison of Filtering Errors for the Heston Model.
125
2.31
Comparison of Filtering Errors for the GARCH Model.
125
2.32
Comparison of Filtering Errors for the 3/2 Model.
126
2.33
Simulated Stock Price Path via Heston Using ∗.
128
2.34
f (ω) = L(ω ˆθ ˆξ ˆρ) Has a Good Slope Around ˆω = 0.10.
129
2.35
f (θ) = L( ˆωθ ˆξ ˆρ) Has a Good Slope Around ˆθ = 10.0.
130
2.36
f (ξ) = L( ˆω ˆθξ ˆρ) Is Flat Around ˆξ = 0.03.
130
2.37
f (ρ) = L( ˆω ˆθ ˆξρ) Is Flat and Irregular Around ˆρ = −0.50. 131
2.38
f (ξ) = L( ˆω ˆθξ ˆρ) via EKF for N = 5000 Points.
132
2.39
f (ξ) = L( ˆω ˆθξ ˆρ) via EKF for N = 50 000 Points.
134
2.40
f (ξ) = L( ˆω ˆθξ ˆρ) via EKF for N = 100 000 Points.
134
2.41
f (ξ) = L( ˆω ˆθξ ˆρ) via EKF for N = 500 000 Points.
135
2.42
Density for ˆω Estimated from 500 Paths of Length 5000 via
EKF.
142
2.43
Density for ˆθ Estimated from 500 Paths of Length 5000 via
EKF.
142
2.44
Density for ˆξ Estimated from 500 Paths of Length 5000 via
EKF.
143
2.45
Density for ˆρ Estimated from 500 Paths of Length 5000 via
EKF.
143
2.46
Gibbs Sampler for µ in N(µ σ).
147
2.47
Gibbs Sampler for σ in N(µ σ).
148
2.48
Metropolis-Hastings Algorithm for µ in N(µ σ).
151
2.49
Metropolis-Hastings Algorithm for σ in N(µ σ).
152
2.50
Plots of the Incomplete Beta Function.
152
2.51
Comparison of EPF Results for Heston and Heston+Jumps
Models. The presence of jumps can be seen in the residuals.
166
2.52
Comparison of EPF Results for Simulated and Estimated
Jump-Diffusion Time Series.
167
2.53
The
Simulated
Arrival
Rates
via
 = (κ = 0 η = 0
λ = 0 σ = 0.2 θ = 0.02 ν = 0.005) and  = (κ = 0.13
η = 0 λ = 0.40 σ = 0.2 θ = 0.02 ν = 0.005)
Are Quite
Different; compare with Figure 2.54.
177
2.54
However, the Simulated Log Stock Prices are Close.
177

xii
ILLUSTRATIONS
2.55
The Observation Errors for the VGSA Model with a
Generic Particle Filter.
179
2.56
The Observation Errors for the VGSA model and an
Extended Particle filter.
180
2.57
The VGSA Residuals Histogram.
180
2.58
The VGSA Residuals Variogram.
181
2.59
Simulation of VGG-based Log Stock Prices with Two
Different
Parameter
Sets
 = (µa = 10.0,
νa = 0.01,
ν = 0.05, σ = 0.2 θ = 0.002) and  = (9.17 0.19 0.012,
0.21 0.0019).
183
3.1
Implied Volatilities of Close to ATM Puts and Calls as of
01/02/2002.
191
3.2
The Observations Have Little Sensitivity to the Volatility
Parameters.
194
3.3
The state Has a Great Deal of Sensitivity to the Volatility
Parameters.
195
3.4
The Observations Have a Great Deal of Sensitivity to the
Drift Parameters.
195
3.5
The State Has a Great Deal of Sensitivity to the Drift Par-
ameters.
196
3.6
Comparing SPX Cross-Sectional and Time-Series Volatility
Smiles (with Historic ξ and ρ) as of January 2, 2002.
197
3.7
A Generic Example of a Skewness Strategy to Take Advan-
tage of the Undervaluation of the Skew by Options.
201
3.8
A Generic Example of a Kurtosis Strategy to Take Advan-
tage of the Overvaluation of the Kurtosis by Options.
202
3.9
Historic Spot Level Movements During the Trade Period.
205
3.10
Hedging PnL Generated During the Trade Period.
205
3.11
Cumulative Hedging PnL Generated During the Trade
Period.
206
3.12
A Strong Option-Implied Skew: Comparing MMM (3M
Co) Cross-Sectional and Time-Series Volatility Smiles as of
March 28, 2003.
207
3.13
A Weak Option-Implied Skew: Comparing CMI (Cummins
Inc) Cross-Sectional and Time-Series Volatility Smiles as of
March 28, 2003.
207
3.14
GW
(Grey
Wolf
Inc.)
Historic
Prices
(03/31/2002–
03/31/2003) Show a High Volatility-of-Volatility But a
Weak Stock-Volatility Correlation.
210
3.15
The Historic GW (Grey Wolf Inc.) Skew Is Low and Not in
Agreement with the Options Prices.
210

Illustrations
xiii
3.16
MSFT
(Microsoft)
Historic
Prices
(03/31/2002–
03/31/2003) Show a High Volatility-of-Volatility and
a Strong Negative Stock-Volatility Correlation.
211
3.17
The Historic MSFT (Microsoft) Skew Is High and in Agree-
ment with the Options Prices.
211
3.18
NDX (Nasdaq) Historic Prices (03/31/2002–03/31/2003)
Show a High Volatility-of-Volatility and a Strong Negative
Stock-Volatility Correlation.
212
3.19
The Historic NDX (Nasdaq) Skew Is High and in Agree-
ment with the Options Prices.
213
3.20
Arrival Rates for Simulated SPX Prices Using  = (κ =
0.0000
η = 0.0000
λ = 0.000000
σ = 0.117200
θ =
0.0056 ν = 0.002) and  = (κ = 79.499687 η = 3.557702
λ = 0.000000 σ = 0.049656 θ = 0.006801 ν = 0.008660
µ = 0.030699).
216
3.21
Gamma Times for Simulated SPX Prices Using  = (κ =
0.0000
η = 0.0000
λ = 0.000000
σ = 0.117200
θ =
0.0056
ν = 0.002)
and
 = (κ = 79.499687
η =
3.557702
λ = 0.000000
σ = 0.049656
θ = 0.006801
ν = 0.008660 µ = 0.030699).
217
3.22
Log Stock Prices for Simulated SPX Prices Using  = (κ =
0.0000
η = 0.0000
λ = 0.000000
σ = 0.117200
θ =
0.0056
ν = 0.002)
and
 = (κ = 79.499687
η =
3.557702
λ = 0.000000
σ = 0.049656
θ = 0.006801
ν = 0.008660 µ = 0.030699).
218
3.23
A Time Series of the Euro Index from January 2000 to
January 2005.
222
Tables
1.1
SPX Implied Surface as of 03/09/2004. T is the maturity
and M = K/S the inverse of the moneyness.
30
1.2
Heston Prices Fitted to the 2004/03/09 Surface.
30
2.1
The Estimation is Performed for SPX on t = 05/21/2002
with Index = $1079.88 for Different Maturities T.
53
2.2
The True Parameter Set ∗Used for Data Simulation.
127
2.3
The Initial Parameter Set 0 Used for the Optimization
Process.
127
2.4
The Optimal Parameter Set ˆ.
128
2.5
The Optimal EKF Parameters ˆξ and ˆρ Given a Sample
Size N.
132
2.6
The True Parameter Set ∗Used for Data Generation.
133

xiv
ILLUSTRATIONS
2.7
The Initial Parameter Set 0 Used for the Optimization
Process.
133
2.8
The Optimal EKF Parameter Set ˆ Given a Sample Size N. 133
2.9
The Optimal EKF Parameter Set ˆ via the HRS Approxi-
mation Given a Sample Size N.
136
2.10
The Optimal PF Parameter Set ˆ Given a Sample Size N.
137
2.11
Real and Optimal Parameter Sets Obtained via NGARCH
MLE.
138
2.12
Real and Optimal Parameter Sets Obtained via NGARCH
MLE as well as EKF.
139
2.13
The Optimal Parameter Set ˆ for 5 000 000 Data Points.
139
2.14
Mean and (Standard Deviation) for the Estimation of
Each Parameter via EKF Over P = 500 Paths of Lengths
N = 5000 and N = 50 000.
141
2.15
MPE and RMSE for the VGSA Model Under a Generic PF
as well as the EPF.
179
3.1
Average Optimal Heston Parameter Set (Under the Risk-
Neutral Distribution) Obtained via LSE Applied to One-
Year SPX Options in January 2002.
191
3.2
Average Optimal Heston Parameter Set (Under the Statis-
tical Distribution) Obtained via Filtered MLE Applied to
SPX Between January 1992 and January 2004.
193
3.3
VGSA Statistical Parameters Estimated via PF.
218
3.4
VGSA Risk-Neutral Arrival-Rate Parameters Estimated
from Carr et al. [48].
219
3.5
The Volatility and Correlation Parameters for the Cross-
Sectional and Time-Series Approaches.
220

Acknowledgments
T
his book is based upon my Ph.D. dissertation at École des Mines de Paris.
I would like to thank my advisor, Alain Galli, for his guidance and help.
Many thanks go to Margaret Armstrong and Delphine Lautier and the entire
CERNA team for their support.
A special thank-you goes to Yves Rouchaleau for helping make all this
possible in the first place.
I would like to sincerely thank other committee members, Marco
Avellaneda, Lane Hughston, Piotr Karasinski, and Bernard Lapeyre, for their
comments and time.
I am grateful to Farshid Asl, Peter Carr, Raphael Douady, Robert Engle,
Stephen Figlewski, Espen Haug, Ali Hirsa, Michael Johannes, Simon Julier,
Alan Lewis, Dilip Madan, Vlad Piterbarg, Youssef Randjiou, David Wong,
and the participants at ICBI 2003 and 2004 for all the interesting discussions
and idea exchanges.
I am particularly indebted to Paul Wilmott for encouraging me to speak
with Wiley about converting my dissertation into this book.
Finally, I would like to thank my wife, Firoozeh, and my daughters,
Neda and Ariana, for their patience and support.
xv


Introduction
SUMMARY
This book focuses on developing methodologies for estimating stochastic
volatility (SV) parameters from the stock-price time series under a classical
framework. The text contains three chapters structured as follows.
In Chapter 1, we shall introduce and discuss the concept of various
parametric SV models. This chapter represents a brief survey of the existing
literature on the subject of nondeterministic volatility.
We start with the concept of log-normal distribution and historic volatil-
ity. We then introduce the Black-Scholes [38] framework. We also mention
alternative interpretations as suggested by Cox and Rubinstein [66]. We
state how these models are unable to explain the negative skewness and the
leptokurticity commonly observed in the stock markets. Also, the famous
implied-volatility smile would not exist under these assumptions.
At this point we consider the notion of level-dependent volatility as
advanced by researchers, such as Cox and Ross [64] and [65], as well as
Bensoussan, Crouhy, and Galai [33]. Either an artificial expression of the
instantaneous variance will be used, as is the case for constant elasticity
variance (CEV) models, or an implicit expression will be deduced from a
firm model, similar to Merton’s [189], for instance.
We also bring up the subject of Poisson jumps [190] in the distributions
providing a negative skewness and larger kurtosis. These jump-diffusion
models offer a link between the volatility smile and credit phenomena.
We then discuss the idea of local volatility [36] and its link to the instant-
aneous unobservable volatility. Work by researchers such as Dupire [89] and
by Derman and Kani [74] will be cited. We also describe the limitations of this
idea owing to an ill-poised inversion phenomenon, as revealed by Avellaneda
[16] and others.
Unlike nonparametric local volatility models, parametric stochastic
volatility (SV) models [140] define a specific stochastic differential equa-
tion for the unobservable instantaneous variance. We therefore introduce the
notion of two-factor stochastic volatility and its link to one-factor general-
ized autoregressive conditionally heteroskedastic (GARCH) processes [40].
The SV model class is the one we focus upon. Studies by scholars, such as
xvii

xviii
INTRODUCTION
Engle [94], Nelson [194], and Heston [134], are discussed at this juncture.
We briefly mention related works on stochastic implied volatility by Schon-
bucher [213], as well as uncertain volatility by Avellaneda [17].
Having introduced SV, we then discuss the two-factor partial differential
equations (PDE) and the incompleteness of the markets when only cash and
the underlying asset are used for hedging.
We then examine option pricing techniques, such as inversion of the
Fourier transform and mixing Monte Carlo, as well as a few asymptotic
pricing techniques, as explained, for instance, by Lewis [177].
At this point we tackle the subject of pure-jump models, such as Madan’s
variance gamma [182] or its variants VG with stochastic arrivals (VGSA)
[48]. The latter adds to the traditional VG a way to introduce the volatil-
ity clustering (persistence) phenomenon. We mention the distribution of
the stock market as well as various option-pricing techniques under these
models. The inversion of the characteristic function is clearly the method of
choice for option pricing in this context.
In Chapter 2, we tackle the notion of inference (or parameter estimation)
for parametric SV models. We first briefly analyze cross-sectional inference
and then focus upon time-series inference.
We start with a concise description of cross-sectional estimation of SV
parameters in a risk-neutral framework. A least-square estimation (LSE)
algorithm is discussed. The direction-set optimization algorithm [204] is
introduced at this point. The fact that this optimization algorithm does not
use the gradient of the input function is important because we shall later
deal with functions that contain jumps and are not necessarily differentiable
everywhere.
We then discuss the parameter inference from a time series of the under-
lying asset in the real world. We do this in a classical (non-Bayesian) [240]
framework, and in particular we will estimate the parameters via a maxi-
mization of likelihood estimation (MLE) [127] methodology. We explain the
idea of MLE, its link to the Kullback-Leibler [100] distance, as well as
the calculation of the likelihood function for a two-factor SV model.
We see that unlike GARCH models, SV models do not admit an analytic
(integrated) likelihood function. This is why we need to introduce the concept
of filtering [129].
The idea behind filtering is to obtain the best possible estimation of
a hidden state given all the available information up to that point. This
estimation is done in an iterative manner in two stages: The first step is a time
update in which the prior distribution of the hidden state at a given point in
time is determined from all the past information via a Chapman-Kolmogorov
equation. The second step would then involve a measurement update where
this prior distribution is used together with the conditional likelihood of

Introduction
xix
the newest observation in order to compute the posterior distribution of the
hidden state. The Bayes rule is used for this purpose. Once the posterior
distribution is determined, it can be exploited for the optimal estimation of
the hidden state.
We start with the Gaussian case where the first two moments characterize
the entire distribution. For the Gaussian-linear case, the optimal Kalman fil-
ter (KF) [129] is introduced. Its nonlinear extension, the extended KF (EKF),
is described next. A more suitable version of KF for strongly nonlinear cases,
the unscented KF (UKF) [166], is also analyzed. In particular, we see how
this filter is related to Kushner’s nonlinear filter (NLF) [173] and [174].
The unscented KF uses a first-order Taylor approximation on the non-
linear transition and observation functions, in order to bring us back into
a simple KF framework. On the other hand, UKF uses the true nonlinear
functions without any approximation. It, however, supposes that the Gaus-
sianity of the distribution is preserved through these functions. The UKF
determines the first two moments via integrals that are computed upon a few
appropriately chosen “sigma points.” The NLF does the same exact thing
via a Gauss-Hermite quadrature. However, NLF often introduces an extra
centering step, which will avoid poor performance owing to an insufficient
intersection between the prior distribution and the conditional likelihood.
As we observe, in addition to their use in the MLE approach, the filters
can be applied to a direct estimation of the parameters via a joint filter (JF)
[133]. The JF would simply involve the estimation of the parameters together
with the hidden state via a dimension augmentation. In other words, one
would treat the parameters as hidden states. After choosing initial conditions
and applying the filter to an observation data set, one would then disregard a
number of initial points and take the average upon the remaining estimations.
This initial rejected period is known as the “burn-in” period.
We test various representations or state space models of the stochastic
volatility models, such as Heston’s [134]. The concept of observability [205]
is introduced in this context. We see that the parameter estimation is not
always accurate given a limited amount of daily data.
Before a closer analysis of the performance of these estimation methods,
we introduce simulation-based particle filters (PF) [79] and [122], which can
be applied to non-Gaussian distributions. In a PF algorithm, the importance
sampling technique is applied to the distribution. Points are simulated via a
chosen proposal distribution, and the resulting weights proportional to the
conditional likelihood are computed. Because the variance of these weights
tends to increase over time and cause the algorithm to diverge, the simulated
points go through a variance reduction technique commonly referred to as
resampling [14]. During this stage, points with too small a weight are dis-
regarded and points with large weights are reiterated. This technique could

xx
INTRODUCTION
cause a sample impoverishment, which can be corrected via a Metropolis-
Hastings accept/reject test. Work by researchers such as Doucet [79] and
Smith and Gordon [122] are cited and used in this context.
Needless to say, the choice of the proposal distribution could be funda-
mental in the success of the PF algorithm. The most natural choice would be
to take a proposal distribution equal to the prior distribution of the hidden
state. Even if this makes the computations simpler, the danger would be a
nonalignment between the prior and the conditional likelihood as we pre-
viously mentioned. To avoid this, other proposal distributions taking into
account the observation should be considered. The extended PF (EPF) and
the unscented PF (UPF) [229] precisely do this by adding an extra Gaussian
filtering step to the process. Other techniques, such as auxiliary PF (APF),
have been developed by Pitt and Shephard [203].
Interestingly, we will see that PF brings only marginal improvement to
the traditional KF’s when applied to daily data. However, for a larger time
step where the nonlinearity is stronger, the PF does help more.
At this point, we also compare the Heston model with other SV models,
such as the “3/2” model [177] using real market data, and we see that the
latter performs better than the former. This is in line with the findings of
Engle and Ishida [95]. We can therefore apply our inference tools to perform
model identification.
Various diagnostics [129] are used to judge the performance of the esti-
mation tools. Mean price errors (MPE) and root mean square errors (RMSE)
are calculated from the residual errors. The same residuals could be submit-
ted to a Box-Ljung test, which will allow us to see whether they still contain
auto correlation. Other tests, such as the chi-square normality test as well as
plots of histograms and variograms [110], are performed.
Most importantly, for the inference process, we back-test the tools upon
artificially simulated data, and we observe that although they give the correct
answer asymptotically, the results remain inaccurate for a smaller amount of
data points. It is reassuring to know that these observations are in agreement
with work by other researchers, such as Bagchi [19].
Here, we attempt to find an explanation for this mediocre performance.
One possible interpretation comes from the fact that in the SV problem,
the parameters affect the noise of the observation and not its drift. This is
doubly true of volatility-of-volatility and stock-volatility correlation, which
affect the noise of the noise. We should, however, note that the product of
these two parameters enters in the equations at the same level as the drift
of the instantaneous variance, and it is precisely this product that appears in
the skewness of the distribution.
Indeed, the instantaneous volatility is observable only at the second order
of a Taylor (or Ito) expansion of the logarithm of the asset price. This also

Introduction
xxi
explains why one-factor GARCH models do not have this problem. In their
context, the instantaneous volatility is perfectly known as a function of pre-
vious data points. The problem therefore seems to be a low signal-to-noise
ratio (SNR). We could improve our estimation by considering additional
data points. Using a high frequency (several quotes a day) for the data does
help in this context. However, one needs to obtain clean and reliable data
first.
Furthermore, we can see why a large time step (e.g., yearly) makes the
inference process more robust by improving the observation quality. Still,
using a large time step brings up other issues, such as stronger nonlinearity
as well as fewer available data points, not to mention the inapplicability of
the Girsanov theorem.
We analyze the sampling distributions of these parameters over many
simulations and see how unbiased and efficient the estimators are. Not sur-
prisingly, the inefficiency remains significant for a limited amount of data.
One needs to question the performance of the actual optimization algo-
rithm as well. It is known that the greater the number of the parameters we
are dealing with, the flatter the likelihood function and therefore the more
difficult to find a global optimum. Nevertheless, it is important to remember
that the SNR and therefore the performance of the inference tool depend on
the actual value of the parameters. Indeed, it is quite possible that the real
parameters are such that the inference results are accurate.
We then apply our PF to a jump-diffusion model (such as the Bates
[28] model), and we see that the estimation of the jump parameters is more
robust than the estimation of the diffusion parameters. This reconfirms that
the estimation of parameters affecting the drift of the observation is more
reliable.
We finally apply the PF to non-Gaussian models such as VGSA [48],
and we observe results similar to those for the diffusion-based models. Once
again the VG parameters directly affecting the observation are easier to
estimate, whereas the arrival rate parameters affecting the noise are more
difficult to recover.
Although as mentioned we use a classical approach, we briefly dis-
cuss Bayesian methods [34], such as Markov Chain Monte Carlo (MCMC)
[163]—including the Gibbs Sampler [55] and the Metropolis-Hastings (MH)
[58] algorithm. Bayesian methods consider the parameters not as fixed num-
bers, but as random variables having a prior distribution. One then updates
these distributions from the observations similarly to what is done in the
measurement update step of a filter. Sometimes the prior and posterior dis-
tributions of the parameters belong to the same family and are referred to as
conjugates. The parameters are finally estimated via an averaging procedure
similar to the one employed in the JF. Whether the Bayesian methods are

xxii
INTRODUCTION
actually better or worse than the classical ones has been a subject of long
philosophical debate [240] and remains for the reader to decide.
Other methodologies that differ from ours are the nonparametric (NP)
and the semi-nonparametric (SNP). These methods are based on kernel inter-
polation procedures and have the obvious advantage of being less restrictive.
However, parametric models, such as the ones used by us, offer the possi-
bility of comparing and interpreting parameters such as drift and volatility
of the instantaneous variance explicitly. Researchers, such as Gallant and
Tauchen [109] and Aït-Sahalia [6], use NP/SNP approaches.
Finally, in Chapter 3, we apply the aforementioned parametric inference
methodologies to a few assets and will question the consistency of informa-
tion contained in the options markets on the one hand, and in the stock
market on the other hand.
We see that there seems to be an excess negative skewness and kurtosis in
the former. This is in contradiction with the Girsanov theorem for a Heston
model and could mean either that the model is misspecified or that there is
a profitable transaction to be made. Another explanation could come from
the peso theory [12] (or crash-o-phobia [155]), where an expectation of a
so-far absent crash exists in the options markets.
Adding a jump component to the distributions helps to reconcile
the volatility-of-volatility and correlation parameters; however, it remains
insufficient. This is in agreement with statements made by Bakshi, Cao, and
Chen [20].
It is important to realize that, ideally, one should compare the infor-
mation embedded in the options and the evolution of the underlying asset
during the life of these options. Indeed, ordinary put or call options are for-
ward (and not backward) looking. However, given the limited amount of
available daily data through this period, we make the assumption that the
dynamics of the underlying asset do not change before and during the exist-
ence of the options. We therefore use time series that start long before the
commencement of these contracts.
This assumption allows us to consider a skewness trade [6], in which
we would exploit such discrepancies by buying out-of-the-money (OTM)
call options and selling OTM put options. We see that the results are not
necessarily conclusive. Indeed, even if the trade often generates profits, occa-
sional sudden jumps cause large losses. This transaction is therefore similar
to “selling insurance.”
We also apply the same idea to the VGSA model in which despite the
non-Gaussian features, the volatility of the arrival rate is supposed to be the
same under the real and risk-neutral worlds.
Let us be clear on the fact that this chapter does not constitute a thorough
empirical study of stock versus options markets. It rather presents a set of

Introduction
xxiii
examples of application for our previously constructed inference tools. There
clearly could be many other applications, such as model identification as
discussed in the second chapter.
Yet another application of the separate estimations of the statistical and
risk-neutral distributions is the determination of optimal positions in deriva-
tives securities, as discussed by Carr and Madan [52]. Indeed, the expected
utility function to be maximized needs the real-world distribution, whereas
the initial wealth constraint exploits the risk-neutral distribution. This can
be seen via a self-financing portfolio argument similar to the one used by
Black and Scholes [38].
Finally, we should remember that in all of the foregoing, we are assuming
that the asset and options dynamics follow a known and fixed model, such as
Heston or VGSA. This is clearly a simplification of reality. The true markets
follow an unknown and, perhaps more importantly, constantly changing
model. The best we can do is to use the information hitherto available and
hope that the future behavior of the assets is not too different from that of
the past. Needless to say, as time passes by and new information becomes
available, we need to update our models and parameter values. This could
be done within either a Bayesian or classical framework.
Also, we apply the same procedures to other asset classes, such as foreign
exchange and fixed income. It is noteworthy that although most of the text
is centered on equities, almost no change whatsoever is necessary in order
to apply the methodologies to these asset classes, which shows again how
flexible the tools are.
In the Bibliography, many but not all relevant articles and books are
cited. Only some of them are directly referred to in the text.
CONTRIBUTIONS AND FURTHER RESEARCH
The contribution of the book is in presenting a general and systematic way
to calibrate any parametric SV model (diffusion based or not) to a time
series under a classical (non-Bayesian) framework. Although the concept
of filtering has been used for estimating volatility processes before [130],
to my knowledge, this has always been for specific cases and was never
generalized. The use of particle filtering allows us to do this in a flexible and
simple manner. We also study the convergence properties of our tools and
show their limitations.
Whether the results of these calibrations are consistent with the infor-
mation contained in the options markets is a fundamental question. The
applications of this test are numerous, among which the skewness trade is
only one example.

xxiv
INTRODUCTION
What else can be done?—a comparative study between our approach
and Bayesian approaches on the one hand, and nonparametric approaches
on the other hand. Work by researchers such as Johannes, Polson, and Aït-
Sahalia would be extremely valuable in this context.
DATA AND PROGRAMS
This book centers on time-series methodologies and exploits either artificially
generated inputs or real market data. When real market data is utilized, the
source is generally Bloomberg. However, most of the data could be obtained
from other public sources available on the Internet.
All numeric computations are performed via routines implemented in
the C++ programming language. Some algorithms, such as the direction-set
optimization algorithm are taken from Numerical Recipes in C [204]. No
statistical packages, such as S-Plus or R, have been used.
The actual C++ code for some of the crucial routines (such as EKF or
UPF) is provided in this text.

CHAPTER 1
The Volatility Problem
Suppose we use the standard deviation of possible future returns
on a stock as a measure of its volatility. Is it reasonable to take
that volatility as a constant over time? I think not.
— Fischer Black
INTRODUCTION
It is widely accepted today that an assumption of a constant volatility fails
to explain the existence of the volatility smile as well as the leptokurtic
character (fat tails) of the stock distribution. The above Fischer Black quote,
made shortly after the famous constant-volatility Black-Scholes model was
developed, proves the point.
In this chapter, we will start by describing the concept of Brownian
motion for the stock price return as well as the concept of historic volatility.
We will then discuss the derivatives market and the ideas of hedging and
risk neutrality. We will briefly describe the Black-Scholes partial derivatives
equation (PDE) in this section. Next, we will talk about jumps and level
dependent volatility models. We will first mention the jump diffusion process
and introduce the concept of leverage. We will then refer to two popular level
dependent approaches: the constant elasticity variance (CEV) model and the
Bensoussan-Crouhy-Galai (BCG) model. At this point, we will mention local
volatility models developed in the recent past by Dupire and Derman-Kani,
and we will discuss their stability.
Following this, we will tackle the subject of stochastic volatility, where
we will mention a few popular models, such as the square-root model and
the general autoregressive conditional heteroskedasticity (GARCH) model.
We will then talk about the pricing PDE under stochastic volatility and the
1

2
INSIDE VOLATILITY ARBITRAGE
risk-neutral version of it. For this we will need to introduce the concept of
market price of risk.
The generalized Fourier transform is the subject of the following section.
This technique was used by Alan Lewis extensively for solving stochastic
volatility problems. Next, we will discuss the mixing solution, both in cor-
related and uncorrelated cases. We will mention its link to the fundamental
transform and its usefulness for Monte Carlo–based methods. We will then
describe the long-term asymptotic case, where we get closed-form approxi-
mations for many popular methods, such as the square-root model. Lastly,
we will talk about pure-jump models, such as variance gamma and variance
gamma with stochastic arrival.
THE STOCK MARKET
The Stock Price Process
The relationship between the stock market and the mathematical concept
of Brownian motion goes back to Bachelier [18]. A Brownian motion cor-
responds to a process, the increments of which are independent stationary
normal random variables. Given that a Brownian motion can take negative
values, it cannot be used for the stock price. Instead, Samuelson [211] sug-
gested using this process to represent the return of the stock price, which
will make the stock price a geometric (or exponential) Brownian motion.
In other words, the stock price S follows a log-normal process1
dSt = µStdt + σStdBt
(1.1)
where dBt is a Brownian motion process, µ the instantaneous expected total
return of the stock (possibly adjusted by a dividend yield), and σ the instant-
aneous standard deviation of stock price returns, called the volatility in finan-
cial markets.
Using Ito’s lemma,2 we also have
d ln(St) =

µ −1
2σ2

dt + σdBt
(1.2)
The stock return µ could easily become time dependent without changing
any of our arguments. For simplicity, we will often refer to it as µ even if we
mean µt. This remark holds for other quantities, such as rt, the interest-rate,
or qt, the dividend yield.
Equation (1.1) represents a continuous process. We can either take this
as an approximation of the real discrete tick-by-tick stock movements or
1For an introduction to stochastic processes, see Karatzas [167] or Oksendal [197].
2See, for example, Hull [146].

The Volatility Problem
3
consider it the real unobservable dynamics of the stock price, in which case
the discrete prices constitute a sample from this continuous ideal process.
Either way, the use of a continuous equation makes the pricing of financial
instruments more analytically tractable.
The discrete equivalent of (1.2) is
ln St+t = ln St +

µ −1
2σ2

t + σ
√
tBt
(1.3)
where (Bt) is a sequence of independent normal random variables with zero
mean and variance of 1.
Historic Volatility
This suggests a first simple way to estimate the volatility, σ, namely the his-
toric volatility. Considering S1 ... SN as a sequence of known historic daily
stock close prices, calling Rn = ln(Sn+1/Sn) the stock price return between
two days and ¯R = 1
N
N−1
n=0 Rn the mean return, the historic volatility would
be the annualized standard deviation of the returns, namely
σhist =



 252
N −1
N−1

n=0
(Rn −¯R)2
(1.4)
Because we work with annualized quantities, and we are using daily
stock closing prices, we needed the factor 252, supposing that there are
approximately 252 business days in a year.3
Note that N, the number of observations, can be more or less than one
year; therefore when talking about a historic volatility, it is important to
know what time horizon we are considering. We can indeed have three-
month historic volatility or three-year historic volatility. Needless to say,
taking too few prices would give an inaccurate estimation. Similarly, the
begin and end date of the observations matter. It is preferable to take the
end date as close as possible to today so that we include recent observations.
An alternative was suggested by Parkinson [200] in which instead of
daily closing prices we use the high and the low prices of the stock on that
day, and Rn = ln(Shigh
n
/Slow
n
). The volatility would then be
σparkinson =



 252
N −1
1
4 ln(2)
N−1

n=0
(Rn −¯R)2
This second moment estimation derived by Parkinson is based upon the
fact that the range Rn of the asset follows a Feller distribution.
3Clearly the observation frequency does not have to be daily.

4
INSIDE VOLATILITY ARBITRAGE
0.18
0.19
0.2
0.21
0.22
0.23
0.24
0
50
100
150
200
250
300
350
400
450
500
Historic Volatility
Days
Historic Volatility
Historic Volatility
FIGURE 1.1
The SPX Historic Rolling Volatility from 01/03/2000 to 12/31/2001.
As we can see, the volatility is clearly nonconstant.
Plotting, for instance, the one-year rolling4 historic volatility (1.4) of the
S&P 500 Stock Index, it is easily seen that this quantity is not constant over
time (Figure 1.1). This observation was made as early as the 1960s by many
financial mathematicians and followers of the chaos theory. We therefore
need time-varying volatility models.
One natural extension of the constant volatility approach is to make σt
a deterministic function of time. This is equivalent to giving the volatility a
term structure, by analogy with interest rates.
THE DERIVATIVES MARKET
Until now, we have mentioned the stock price movements independently
from the derivatives market, but we now are going to include the financial
derivatives (especially options) prices as well. These instruments became very
popular and as liquid as the stocks themselves after Black and Scholes intro-
duced their risk-neutral pricing formula in [38].
4By rolling we mean that the one-year interval slides within the total observation
period.

The Volatility Problem
5
The Black-Scholes Approach
The Black-Scholes approach makes a number of reasonable assumptions
about markets being frictionless and uses the log-normal model for the
stock price movements. It also supposes a constant or deterministically time-
dependent stock drift and volatility. Under these conditions, they prove that
it is possible to hedge a position in a contingent claim dynamically by taking
an offsetting position in the underlying stock and hence become immune to
the stock movements. This risk neutrality is possible because, as they show,
we can replicate the financial derivative (for instance, an option) by taking
positions in cash and the underlying security. This condition of the possibility
of replication is called market completeness.
In this situation, everything happens as if we were replacing the stock
drift µt with the risk-free rate of interest rt in (1.1) or rt −qt if there is a
dividend-yield qt. The contingent claim f (S t) having a payoff G(ST) will
satisfy the famous Black-Scholes equation
rf = ∂f
∂t + (r −q)S ∂f
∂S + 1
2σ2S2 ∂2f
∂S2
(1.5)
Indeed the hedged portfolio  = f −∂f
∂S S is immune to the stock random
movements and, according to Ito’s lemma, verifies
d =
∂f
∂t + 1
2σ2S2 ∂2f
∂S2

dt
which must also be equal to rdt or else there would be possibility of Risk-
less arbitrage.5
Note that this equation is closely related to the Feynman-Kac equation
satisfied by F(S t) = Et(h(ST)) for any function h under the risk-neutral
measure; F(S t) must be a Martingale6 under this measure and therefore
must be driftless, which implies dF = σS ∂F
∂S dBt and
0 = ∂F
∂t + (r −q)S ∂F
∂S + 1
2σ2S2 ∂2F
∂S2
This would indeed be a different way to reach the same Black-Scholes equa-
tion, by using f (S t) = exp(−rt)F(S t), as was done, for instance, in Shreve
[218].
Let us insist again on the fact that the real drift of the stock price does
not appear in the preceding equation, which makes the volatility σt the only
5For a detailed discussion, see Hull [146].
6For an explanation, see Shreve [218] or Karatzas [167].

6
INSIDE VOLATILITY ARBITRAGE
unobservable quantity. As we said, the volatility could be a deterministic
function of time without changing the foregoing argument, in which case all
we need to do is to replace σ2 with 1
t
 t
0 σ2
sds, and keep everything else the
same.
For calls and puts, where the payoffs G(ST) are respectively MAX(0 ST−
K) and MAX(0 K −ST) and where K is the strike price and T the maturity
of the option, the Black-Scholes partial derivatives equation is solvable and
gives the celebrated Black-Scholes formulae
callt = Ste−q(T −t)(d1) −Ke−r(T −t)(d2)
(1.6)
and
putt = −Ste−q(T −t)(−d1) + Ke−r(T −t)(−d2)
(1.7)
where
(x) =
1
√
2π
	 x
−∞
e−u2
2 du
is the cumulative standard normal function and
d1 = d2 + σ
√
T −t
and
d2 = ln

 St
K

+

r −q −1
2σ2
(T −t)
σ√T −t
Note that using the well-known symmetry property for normal distributions
(−x) = 1 −(x) in the above formulae, we could reach the put-call parity
relationship
callt −putt = Ste−q(T −t)−Ke−r(T −t)
(1.8)
which we can also rearrange as
Ste−q(T −t)−callt = Ke−r(T −t)−putt
The left-hand side of this last equation is called a covered call and is
equivalent to a short position in a put combined with a bond.
The Cox-Ross-Rubinstein Approach
Later, Cox, Ross, and Rubinstein [66] developed a simplified approach using
the binomial law to reach the same pricing formulae. The approach com-
monly referred to as the binomial tree uses a tree of recombining spot prices,
in which at a given time step n we have n + 1 possible S[n][j] spot prices,
with 0 ≤j ≤n. Calling p the upward transition probability and 1 −p
the downward transition probability, S the stock price today, and Su = uS

The Volatility Problem
7
and Sd = dS upper and lower possible future spot prices, we can write the
expectation equation7
E[S] = puS + (1 −p)dS = ertS
which immediately gives us
p = a −d
u −d
with a = exp(rt).
We can also write the variance equation
V ar[S] = pu2S2 + (1 −p)d2S2 −e2rtS2 ≈σ2S2t
which after choosing a centering condition, such as ud = 1, will provide us
with u = exp

σ
√
t

and d = exp

−σ
√
t

. Using the values for u, d, and p
we can build the tree, and using the final payoff we can calculate the option
price by backward induction.8 We can also build this tree by applying an
explicit finite difference scheme to the PDE (1.5), as was done in Wilmott
[238]. An important advantage of the tree method is that it can be applied
to American options (with early exercise) as well.
It is possible to deduce the implied volatility of call and put options by
solving a reverse Black-Scholes equation, that is, find the volatility that would
equate the Black-Scholes price to the market price of the option. This is a
good way to see how derivatives markets perceive the underlying volatility.
It is easy to see that if we change the maturity and strike prices of options
(and keep everything else fixed) the implied volatility will not be constant. It
will have a linear skew and a convex form as the strike price changes. This
famous “smile” cannot be explained by simple time dependence, hence the
necessity of introducing new models (Figure 1.2).9
JUMP DIFFUSION AND LEVEL-DEPENDENT VOLATILITY
In addition to the volatility smile observable from the implied volatilities of
the options, there is evidence that the assumption of a pure normal distribu-
tion (also called pure diffusion) for the stock return is not accurate. Indeed
“fat tails” have been observed away from the mean of the stock return. This
7The expectation equation is written under the risk-neutral probability.
8For an in-depth discussion on binomial trees, see Cox [67].
9It is interesting to note that this smile phenomenon was practically nonexistent
prior to the 1987 stock-market crash. Many researchers therefore believe that the
markets have learnt to factor-in a crash possibility, which creates the volatility smile.

8
INSIDE VOLATILITY ARBITRAGE
0.16
0.18
0.2
0.22
0.24
0.26
0.28
0.3
0.32
950
1000
1050
1100
1150
Implied Volatility
Strike Price
Volatility Smile
Implied Volatility 1 month to Maturity
Implied Volatility 7 months to Maturity
FIGURE 1.2
The SPX Volatility Smile on February 12, 2002 with Index = $1107.50,
1 Month and 7 Months to Maturity. The negative skewness is clearly visible. Note
how the smile becomes flatter as time to maturity increases.
phenomenon is called leptokurticity and could be explained in many differ-
ent ways.
Jump Diffusion
Some try to explain the smile and the leptokurticity by changing the under-
lying stock distribution from a diffusion process to a jump-diffusion process.
A jump diffusion is not a level-dependent volatility process; however, we
are mentioning it in this section to demonstrate the importance of the lever-
age effect. Merton [190] was first to actually introduce jumps in the stock
distribution. Kou [172] recently used the same idea to explain both the exist-
ence of fat tails and the volatility smile.
The stock price will follow a modified stochastic process under this
assumption. If we add to the Brownian motion, dBt; a Poisson (jump) pro-
cess10 dq with an intensity11 λ, and then calling k = E(Y −1) with Y −1
10See, for instance, Karatzas [167].
11The intensity could be interpreted as the mean number of jumps per time unit.

The Volatility Problem
9
the random variable percentage change in the stock price, we will have
dSt = (µ −λk)Stdt + σStdBt + Stdq
(1.9)
or equivalently,
St = S0 exp

µ −σ2
2 −λk

t + σBt

Yn
where Y0 = 1 and Yn = n
j=1 Yj, with Yj’s independently identically distri-
buted random variables and n a Poisson random variable with a parameter λt.
It is worth noting that for the special case where the jump corresponds
to total ruin or default, we have k = −1, which will give us
dSt = (µ + λ)Stdt + σStdBt + Stdq
(1.10)
and
St = S0 exp

µ + λ −σ2
2

t + σBt

Yn
Given that in this case E(Yn) = E(Y 2
n ) = e−λt, it is fairly easy to see that in
the risk-neutral world
E(St) = S0ert
exactly as in the pure diffusion case, but
V ar(St) = S2
0e2rt
e(σ2+λ)t −1

≈S2
0

σ2 + λ

t
(1.11)
unlike the pure diffusion case, where V ar(St) ≈S2
0σ2t.
Proof:
Indeed
E(St) = S0 exp((r + λ)t) exp

−σ2
2 t

E[exp(σBt)]E(Yn)
= S0 exp((r + λ)t) exp

−σ2
2 t

exp
σ2
2 t

exp(−λt) = S0 exp(rt)
and
E(S2
t ) = S2
0 exp(2(r + λ)t) exp

−σ2t

E[exp(2σBt)]E(Y 2
n )
= S2
0 exp(2(r + λ)t) exp

−σ2t

exp
(2σ)2
2

exp(−λt)
= S2
0 exp((2r + λ)t) exp

σ2t

and as usual
V ar(St) = E

S2
t

−E2(St)
(QED)

10
INSIDE VOLATILITY ARBITRAGE
Link to Credit Spread
Note that for a zero-coupon risky bond Z with no recov-
ery, a credit spread C and a face value X paid at time t we have
Z = e−(r+C)tX = e−λt(e−rtX) + (1 −e−λt)(0)
consequently λ = C and using (1.11) we can write
˜σ2(C) = σ2 + C
where σ is the fixed (pure diffusion) volatility and ˜σ is the modified jump dif-
fusion volatility. The preceding equation relates the volatility and leverage,
a concept we will see later in level-dependent models as well.
Also, we could see that everything happens as if we were using the Black-
Scholes pricing equation but with a modified “interest rate,” which is r + C.
Indeed the hedged portfolio  = f −∂f
∂S S now satisfies
d =
∂f
∂t + 1
2σ2S2 ∂2f
∂S2

dt
under the no-default case, which occurs with a probability of e−λdt ≈1 −λdt
and
d = −
under the default case, which occurs with a probability of 1 −e−λdt ≈λdt.
We therefore have
E(d) =
∂f
∂t + 1
2σ2S2 ∂2f
∂S2 −λ

dt
and using a diversification argument we can always say that E(d) = rdt
which provides us with
(r + λ)f = ∂f
∂t + (r + λ)S ∂f
∂S + 1
2σ2S2 ∂2f
∂S2
(1.12)
which again is the Black-Scholes PDE with a “risky rate.”
A generalization of the jump diffusion process would be the use of the
Levy process. A Levy process is a stochastic process with independent and
stationary increments. Both the Brownian motion and the Poisson process
are included in this category. For a description, see Matacz [186].
Level-Dependent Volatility
Many assume that the smile and the fat tails are due to the level dependence
of the volatility. The idea would be to make σt level dependent or a function
of the spot itself; we would therefore have
dSt = µtStdt + σ(S t)StdBt
(1.13)

The Volatility Problem
11
Note that to be exact, a level-dependent volatility is a function of the spot
price alone. When the volatility is a function of the spot price and time, it is
referred to as local volatility, which we shall discuss further.
The Constant Elasticity Variance Approach
One of the very first attempts to use
this approach was the constant elasticity variance (CEV) method realized
by Cox [64] and [65] (Figure 1.3). In this method we would suppose an
equation of the type
σ(S t) = CSγ
t
(1.14)
where C and γ are parameters to be calibrated either from the stock price
returns themselves or from the option prices and their implied volatilities.
The CEV method was recently analyzed by Jones [165] in a paper in which
he uses two γ exponents.
This level-depending volatility represents an important feature that is
observed in options markets as well as in the underlying prices: the negative
correlation between the stock price and the volatility, also called the leverage
effect.
The Bensoussan-Crouhy-Galai Approach
Bensoussan, Crouhy, and Galai (BCG)
[33] try to find the level dependence of the volatility in a manner that differs
from that of Cox and Ross (Figure 1.4). Indeed in the CEV model, Cox and
0
20
40
60
80
100
120
140
160
950
1000
1050
1100
1150
Call Price
Strike Price
CEV Model
Market
Model
FIGURE 1.3
The CEV Model for SPX on February 12, 2002 with Index = $1107.50,
1 Month to Maturity. The smile is fitted well, but the model assumes a perfect
(negative) correlation between the stock and the volatility.

12
INSIDE VOLATILITY ARBITRAGE
Ross first suppose that σ(S t) has a certain exponential form and only then
try to calibrate the model parameters to the market. Alternatively, BCG try
to deduce the functional form of σ(S t) by using a firm structure model.
The idea of firm structure is not new and goes back to Merton [189],
when he considers that the firm assets follow a log-normal process
dV = µVV dt + σVV dBt
(1.15)
where µV and σV are the asset’s return and volatility. One important point
is that σV is considered constant. Merton then argues that the equity S of
the firm could be considered a call option on the assets of the firm with a
strike price K equal to the face value of the firm liabilities and an expiration
T equal to the average liability maturity.
Using Ito’s lemma, it is fairly easy to see that
dS = µSdt + σ(S t)SdBt
(1.16)
=
∂S
∂t + µVV ∂S
∂V + 1
2σ2
VV 2 ∂2S
∂V 2

dt + σVV ∂S
∂V dBt
which immediately provides us with
σ(S t) = σV
V
S
∂S
∂V
(1.17)
which is an implicit functional form for σ(S t).
0
20
40
60
80
100
120
140
160
950
1000
1050
1100
1150
Call Price
Strike Price
BCG Model
Market
Model
FIGURE 1.4
The BCG Model for SPX on February 12, 2002 with Index = $1107.50,
1 Month to Maturity. The smile is fitted well.

The Volatility Problem
13
Next, BCG eliminate the asset term in the preceding functional form and
end up with a nonlinear PDE
∂σ
∂t + 1
2σ2S2 ∂2σ
∂S2 +

r + σ2
S ∂σ
∂S = 0
(1.18)
This PDE gives the dependence of σ on S and t.
Proof:
A quick sketch of the proof is as follows: With S being a contingent
claim on V , we have the risk-neutral Black-Scholes PDE
∂S
∂t + rV ∂S
∂V + 1
2σ2
VV 2 ∂2S
∂V 2 = rS
and using ∂S
∂V = 1/ ∂V
∂S as well as ∂S
∂t = −∂S
∂V
∂V
∂t and ∂2S
∂V 2 = −∂2V
∂S2 /

 ∂V
∂S
3 we have
the reciprocal Black-Scholes equation
∂V
∂t + rS ∂V
∂S + 1
2σ2S2 ∂2V
∂S2 = rV
Now posing (S t) = ln V (S t), we have ∂V
∂t = V ∂
∂t as well as ∂V
∂S = V ∂
∂S
and ∂2V
∂S2 = V

∂2
∂S2 + ( ∂
∂S )2
, and we will have the new PDE
r = ∂
∂t + rS ∂
∂S + 1
2σ2S2

∂2
∂S2 +
∂
∂S
2
and the equation
σ = σV/

S ∂
∂S

This last identity implies that ∂
∂S = σV
Sσ as well as ∂2
∂S2 =
−σV(σ+S ∂σ
∂S )
S2σ2
, and
therefore the PDE becomes
r = ∂
∂t + rσV/σ + 1
2

σ2
V −σV

σ + S ∂σ
∂S

taking the derivative with respect to S and using ∂2
∂S∂t = −σV
Sσ2
∂σ
∂t we get the
final PDE
∂σ
∂t + 1
2σ2S2 ∂2σ
∂S2 +

r + σ2
S ∂σ
∂S = 0
as previously stated. (QED)
We therefore have an implicit functional form for σ(S t), and, just as
for the CEV case, we need to calibrate the parameters to the market data.

14
INSIDE VOLATILITY ARBITRAGE
LOCAL VOLATILITY
In the early 1990s, Dupire [89], as well as Derman and Kani [74], developed
a concept called local volatility, in which the volatility smile was retrieved
from the option prices.
The Dupire Approach
The Breeden & Litzenberger Identity
This approach uses the options prices to get
the implied distribution for the underlying stock. To do this we can write
V (S0 K T ) = call(S0 K T ) = e−rT
	 +∞
0
(S −K)+p(S0 S T )dS
(1.19)
where S0 is the stock price at time t = 0 and K the strike price of the call, and
p(S0 S T ) is the unknown transition density for the stock price. As usual,
x+ = MAX(x 0)
Using Equation (1.19) and differentiating with respect to K twice, we
get the Breeden and Litzenberger [44] implied distribution
p(S0 K T ) = erT ∂2V
∂K2
(1.20)
Proof:
The proof is straightforward if we write
erTV (S0 K T ) =
	 +∞
K
Sp(S0 S T )dS −K
	 +∞
K
p(S0 S T )dS
and take the first derivative
erT ∂V
∂K = −Kp(S0 K T ) + Kp(S0 K T ) −
	 +∞
K
p(S0 S T )dS
and the second derivative in the same manner. (QED)
The Dupire Identity
Now, according to the Fokker-Planck (or forward
Kolmogorov) equation12 for this density, we have
∂p
∂T = 1
2
∂2(σ2(S t)S2p)
∂S2
−r ∂(Sp)
∂S
12See, for example, Wilmott [237] for an explanation on Fokker-Planck equation.

The Volatility Problem
15
and therefore after a little rearrangement have
∂V
∂T = 1
2σ2K2 ∂2V
∂K2 −rK ∂V
∂K
which provides us with the local volatility formula
σ2(K T ) =
∂V
∂T + rK ∂V
∂K
1
2K2 ∂2V
∂K2
(1.21)
Proof:
For a quick proof of the above let us use the zero interest rates case
(the general case could be done similarly). We would then have
p(S0 K T ) = ∂2V
∂K2
as well as Fokker-Planck
∂p
∂T = 1
2
∂2(σ2(S t)S2p)
∂S2
Now
∂V
∂T =
	 +∞
0
(ST −K)+ ∂p
∂T dST
=
	 +∞
0
(ST −K)+ 1
2
∂2 
σ2(S T )S2p

∂S2
dST
and integrating by parts twice and using the fact that
∂2(ST −K)+
∂K2
= δ(ST −K)
with δ(.), the Dirac function, we will have
∂V
∂T = 1
2σ2(K T )K2p(S0 K T ) = 1
2K2σ2(K T ) ∂2V
∂K2
as stated. (QED)
It is also possible to use the implied volatility, σBS, from the Black-
Scholes formula (1.6) and express the foregoing local volatility in terms of
σBS instead of V. For a detailed discussion, we could refer to Wilmott [237].

16
INSIDE VOLATILITY ARBITRAGE
Local Volatility vs. Instantaneous Volatility
Clearly, the local volatility is related
to the instantaneous variance vt, as Gatheral [113] shows; the relationship
could be written as
σ2(K T ) = E[vT|ST = K]
(1.22)
that is, local variance is the risk-neutral expectation of the instantaneous
variance conditional on the final stock price being equal to the strike price.13
Proof:
Let us show the above identity for the case of zero interest rates.14
As mentioned, we have
σ2(K T ) =
∂V
∂T
1
2K2 ∂2V
∂K2
On the other hand, using the call payoff V (S0 K t = T ) = E[(ST −K)+]
we have
∂V
∂K = E[H(ST −K)]
with H(.), the heaviside function and
∂2V
∂K2 = E[δ(ST −K)]
with δ(.), the Dirac function.
Therefore the Ito lemma at t = T would provide
d(ST −K)+ = H(ST −K)dST + 1
2vTS2
Tδ(ST −K)dT
Using the fact that the forward price (here with zero interest rates, the stock
price) is a Martingale under the risk-neutral measure
dV = dE[(ST −K)+] = 1
2E

vTS2
Tδ(ST −K)

dT
Now we have
E[vTS2
Tδ(ST −K)] = E[vT|ST = K]K2E[δ(ST −K)]
= E[vT|ST = K]K2 ∂2V
∂K2
13Note that this is independent from the process for vt, meaning that any stochastic
volatility model satisfies this property, which is an attractive feature of local volatility
models.
14For the case of nonzero rates, we need to work with the forward price instead of
the stock price.

The Volatility Problem
17
Putting all this together
∂V
∂T = 1
2K2 ∂2V
∂K2 E[vT|ST = K]
and by the preceding expression of σ2(K T ), we will have
σ2(K T ) = E[vT|ST = K]
as claimed. (QED)
The Derman-Kani Approach
The Derman-Kani technique is very similar to the above approach, except
that it uses the binomial (or trinomial) tree framework instead of the continu-
ous one. Using the binomial tree notations, their upward transition prob-
ability pi from the spot si at time tn to the upper node Si+1 at the following
time-step tn+1, is obtained from the usual
pi = Fi −Si
Si+1 −Si
(1.23)
where Fi is the stock forward price known from the market and Si the lower
spot at the step tn+1.
In addition, we have for a call expiring at time step tn+1
C(K tn+1) = e−rt
n

j=1

λj pj + λj+1

1 −pj+1

MAX(Sj+1 −K 0)
where λj ’s are the known Arrow-Debreu prices corresponding to the dis-
counted probability of getting to the point sj at time tn from S0, the initial
stock price. These probabilities could easily be derived iteratively.
This allows us after some calculation to obtain Si+1 as a function of si
and Si, namely
Si+1 = Si[ertC(si K tn+1) −] −λisi(Fi −Si)
[ertC(si K tn+1) −] −λi(Fi −Si)
where the term  represents the sum n
j = i+1 λj (Fj −si). This means that
after choosing the usual centering condition for the binomial tree
s2
i = SiSi+1
we have all the elements to build the tree and deduce the implied distribution
from the Arrow-Debreu prices.

18
INSIDE VOLATILITY ARBITRAGE
Stability Issues
The local volatility models are very elegant and theoretically sound; how-
ever, they present in practice many stability issues. They are ill-posed inver-
sion problems and are extremely sensitive to the input data.15 This might
introduce arbitrage opportunities and in some cases negative probabilities
or variances. Derman and Kani suggest overwriting techniques to avoid such
problems.
Andersen [13] tries to improve this issue by using an implicit finite dif-
ference method; however, he recognizes that the negative variance problem
could still happen.
One way to make the results smoother is to use a constrained optimiza-
tion. In other words, when trying to fit theoretical results Ctheo to the market
prices Cmrkt, instead of minimizing
N

j=1

Ctheo

Kj

−Cmrkt

Kj
2
we could minimize
λ∂σ
∂t +
N

j=1

Ctheo

Kj

−Cmrkt

Kj
2
where λ is a constraint parameter, which could also be interpreted as a
Lagrange multiplier. However, this is an artificial way to smoothen the results
and the real issue remains that, once again, we have an inversion problem that
is inherently unstable. Furthermore, local volatility models imply that future
implied volatility smiles will be flat relative to today’s, which is another lim-
itation.16 As we will see in the following section, stochastic volatility models
offer more time-homogeneous volatility smiles.
An alternative approach suggested in [16] would be to choose a prior
risk-neutral distribution for the asset (based on a subjective view) and then
minimize the relative entropy distance between the desired surface and this
prior distribution. This approach uses the Kullback-Leibler distance (which
we will discuss in the context of maximum likelihood estimation [MLE])
and performs the minimization via dynamic programming [35] on a tree.
15See Tavella [226] or Avellaneda [16].
16See Gatheral [114].

The Volatility Problem
19
Calibration Frequency
One of the most attractive features of local-vol models is their ability to
match plain-vanilla puts and calls exactly. This will avoid arbitrage situ-
ations, or worse, market manipulations by traders to create “phantom”
profits. As explained in Hull [147], these arbitrage-free models were devel-
oped by researchers with a single calibration (SC) methodology assumption.
However, in practice, traders use them with a continual recalibration (CR)
strategy. Indeed if they used the SC version of the model, significant errors
would be introduced from one week to the following as shown by Dumas
et al. [88]. However, once this CR version is used, there is no guarantee
that the no-arbitrage property of the original SC model is preserved. Indeed
the Dupire equation determines the marginal stock distribution at different
points in time, but not the joint distribution of these stock prices. There-
fore a path-dependent option could very well be mispriced, and the more
path-dependent this option, the greater the mispricing.
Hull [147] takes the example of a bet option, a compound option, and a
barrier option. The bet option depends on the distribution of the stock at one
point in time and therefore is correctly priced with a continually recalibrated
local vol model. The compound option has some path dependency, and hence
a certain amount of mispricing compared with a stochastic volatility (SV)
model. Finally, the barrier option has a strong degree of path dependency
and will introduce large errors. Note that this is due to the discrete nature
of the data. Indeed, the maturities we have are limited. If we had all possible
maturities in a continuous way, the joint distribution would be determined
completely. Also, when interpolating in time, it is customary to interpolate
upon the true variance tσ2
t rather than the volatility σt given the equation
T2σ2(T2) = T1σ2(T1) + (T2 −T1)σ2(T1 T2)
Interpolating upon the true variance will provide smoother results as shown
by Jackel [152].
Proof:
Indeed, calling for 0 ≤T1 ≤T2, the spot return variances
V ar(0 T2) = T2σ2(T2)
V ar(0 T1) = T1σ2(T1)
for a Brownian motion, we have independent increments and therefore a
forward variance V ar(T1 T2) such that
V ar(0 T1) + V ar(T1 T2) = V ar(0 T2)
which demonstrates the point. (QED)

20
INSIDE VOLATILITY ARBITRAGE
STOCHASTIC VOLATILITY
Unlike nonparametric local volatility models, parametric stochastic volatility
(SV) models define a specific stochastic differential equation for the unobserv-
able instantaneous variance. As we shall see, the previously defined CEV
model could be considered a special case of these models.
Stochastic Volatility Processes
The idea would be to use a different stochastic process for σ altogether. Mak-
ing the volatility a deterministic function of the spot is a special “degenerate”
two-factor, a natural generalization of which would precisely be to have two
stochastic processes with an imperfect correlation.17
Several different stochastic processes have been suggested for the volatil-
ity. A popular one is the Ornstein-Uhlenbeck (OU) process:
dσt = −ασtdt + βdZt
(1.24)
where α and β are two parameters, remembering the stock equation
dSt = µtStdt + σtStdBt
there is a (usually negative) correlation ρ between dZt and dBt, which can
in turn be time or level dependent.
Heston [134] and Stein [223] were
among those who suggested the use of this process. Using Ito’s lemma, we
can see that the stock-return variance vt = σ2
t satisfies a square-root or Cox-
Ingersoll-Ross (CIR) process
dvt = (ω −θvt)dt + ξ√vtdZt
(1.25)
with ω = β2, θ = 2α, and ξ = 2β.
Note that the OU process has a closed-form solution
σt = σ0e−αt + β
	 t
0
e−α(t−s)dZs
17Note that here the instantaneous volatility is stochastic. Recent work by research-
ers such as Schonbucher supposes a stochastic implied-volatility process, which
is a completely different approach. See, for instance, [213]. On the other hand,
Avellaneda et al. [17] use the concept of uncertain volatility for pricing and hedging
derivative securities. They make the volatility switch between two extreme values
based on the convexity of the derivative contract and obtain a nonlinear Black-
Scholes-Barenblatt equation, which they solve on a grid.

The Volatility Problem
21
which means that σt follows in law 

σ0e−αt β2
2α

1−e−2αt
, with  again the
normal distribution. This was discussed in Fouque [104] and Shreve [218].
Heston and Nandi [137] show that this process corresponds to a special
case of the general auto regressive conditional heteroskedasticity (GARCH)
model, which we will discuss next. Another popular process is the GARCH
(1,1) process, where we would have
dvt = (ω −θvt)dt + ξvtdZt
(1.26)
GARCH and Diffusion Limits
The most elementary GARCH process, called GARCH(1,1), was developed
originally in the field of econometrics by Engle [94] and Bollerslev [40] in a
discrete framework. The stock discrete equation (1.3) could be rewritten by
taking t = 1 and vn = σ2
n as
ln Sn+1 = ln Sn +

µ −1
2vn+1

+ √vn+1Bn+1
(1.27)
calling the mean adjusted return
un = ln
 Sn
Sn−1

−

µ −1
2vn

= √vnBn
(1.28)
the variance process in GARCH(1,1) is supposed to be
vn+1 = ω0 + βvn + αu2
n = ω0 + βvn + αvnB2
n
(1.29)
where α and β are weight parameters and ω0 is a parameter related to the
long-term variance.18
Nelson [194] shows that as the time interval length decreases and
becomes infinitesimal, Equation (1.29) becomes precisely the previously cited
Equation (1.26). To be more accurate, there is a weak convergence of the dis-
crete GARCH process to the continuous diffusion limit.19 For a GARCH(1,1)
continuous diffusion, the correlation between dZt and dBt is zero.
18It is worth mentioning that as explained in [100], a GARCH(1,1) model could be
rewritten as an autoregressive moving average model of first order, ARMA(1,1), and
therefore an auto regressive model of infinite order, AR(+∞). GARCH is therefore
a parsimonious model that can fit the data with only a few parameters. Fitting the
same data with an ARCH or AR model would require a much larger number of
parameters. This feature makes the GARCH model very attractive.
19For an explanation on weak convergence, see, for example, Varadhan [230].

22
INSIDE VOLATILITY ARBITRAGE
It might appear surprising that even if the GARCH(1,1) process has
only one source of randomness, namely Bn, the continuous version has two
independent Brownian motions. This is understandable if we consider Bn a
standard normal random variable and An = B2
n−1 another random variable.
It is fairly easy to see that An and Bn are uncorrelated even if An is a function
of Bn. As we go toward the continuous version, we can use Donsker’s the-
orem,20 by letting the time interval t →0, to prove that we end up with two
uncorrelated and therefore independent Brownian motions. This is a limi-
tation of the GARCH(1,1) model–hence the introduction of the nonlinear
asymmetric GARCH (NGARCH) model.
Duan [83] attempts to explain the volatility smile by using the NGARCH
process expressed by
vn+1 = ω0 + βvn + α

un −c√vn
2
(1.30)
where c is a parameter to be determined.
The NGARCH process was first introduced by Engle [97]. The continu-
ous counterpart of NGARCH is the same equation (1.26), except unlike the
equation resulting from GARCH(1,1) there is a nonzero correlation between
the stock process and the volatility process. This correlation is created pre-
cisely because of the parameter c that was introduced, and is once again
called the leverage effect. The parameter c is sometimes referred to as the
leverage parameter.
We can find the following relationships between the discrete process and
the continuous diffusion limit parameters by letting the time interval become
infinitesimal
ω = ω0
dt2
θ = 1 −α

1 + c2
−β
dt
ξ = α

κ −1 + 4c2
dt
and the correlation between dBt and dZt
ρ =
−2c
√
κ −1 + 4c2
where κ represents the Pearson kurtosis21 of the mean adjusted returns (un).
As we can see, the sign of the correlation ρ is determined by the parameter c.
20For a discussion on Donsker’s theorem, similar to the central limit theorem, see,
for instance, Whitt [235].
21The kurtosis corresponds to the fourth moment. The Pearson kurtosis for a normal
distribution is equal to 3.

The Volatility Problem
23
Proof:
A quick proof of the convergence to diffusion limit could be outlined
as follows. Let us assume that c = 0 for simplicity; we therefore are dealing
with the GARCH(1,1) case. As we saw
vn+1 = ω0 + βvn + αvnB2
n
therefore
vn+1 −vn = ω0 + βvn −vn + αvn −αvn + αvnB2
n
or
vn+1 −vn = ω0 −(1 −α −β)vn + αvn(B2
n −1)
Now, allowing the time-step t to become variable and posing Zn =
(B2
n −1)/
√
κ −1
vn+t −vn = ωt2 −θtvn + ξvn
√
tZn
and annualizing vn by posing vt = vn/t, we shall have
vt+t −vt = ωt −θtvt + ξvt
√
tZn
and as t →0, we get
dvt = (ω −θvt)dt + ξvtdZt
as claimed. (QED)
Note that the discrete GARCH version of the square-root process (1.25 )
is
vn+1 = ω0 + βvn + α(Bn −c√vn)2
(1.31)
as Heston and Nandi show22 in [137] (Figure 1.5).
Also, note that having a diffusion process dvt = b(vt)dt + a(vt)dZt we
can apply an Euler approximation23 to discretize and obtain a Monte Carlo
process, such as vn+1 −vn = b(vn)t + a(vn)
√
tZn. It is important to note
that if we use a GARCH process and go to the continuous diffusion limit, and
then apply an Euler approximation, we will not necessarily find the original
GARCH process again. Indeed, there are many different ways to discretize
the continuous diffusion limit and the GARCH process corresponds to one
special way. In particular, if we use (1.31) and allow t →0 to get to the
continuous diffusion limit, we shall obtain (1.25). As we will see later in
22For a detailed discussion on the convergence of different GARCH models toward
their diffusion limits, also see Duan [85].
23See, for instance, Jones [165].

24
INSIDE VOLATILITY ARBITRAGE
0
20
40
60
80
100
120
140
160
950
1000
1050
1100
1150
Call Price
Strike Price
Square-Root Model via GARCH
Market
Model
FIGURE 1.5
The GARCH Monte Carlo Simulation with the Square-Root Model for
SPX on February 12, 2002 with Index = $1107.50, 1 Month to Maturity. The Powell
optimization method was used for least-square calibration.
the section on mixing solutions, we can then apply a discretization to this
process and obtain a Monte Carlo simulation
vn+1 = vn + (ω −θvn)t + ξ√vn
√
tZn
which is again different from (1.31) but obviously has to be consistent in
terms of pricing. However, we should know which method we are working
with from the very beginning to perform our calibration on the correspond-
ing specific process.
Corradi [61] explains this in the following manner: The discrete GARCH
model could converge either toward a two-factor continuous limit if one
chooses the Nelson parameterization, or could very well converge to a one-
factor diffusion limit if one chooses another parameterization. Furthermore,
an appropriate Euler discretization of the one-factor continuous model will
provide a GARCH discrete process, while as previously mentioned the dis-
cretization of the two-factor diffusion model provides a two-factor discrete
process. This distinction is fundamental and could explain why GARCH and
SV behave differently in terms of parameter estimation.
THE PRICING PDE UNDER STOCHASTIC VOLATILITY
A very important issue to underline here is that, because of the unhedgeable
second source of randomness, the concept of market completeness is lost.

The Volatility Problem
25
We can no longer have a straightforward risk-neutral pricing. This is where
the market price of risk will come into consideration.
The Market Price of Volatility Risk
Indeed, taking a more general form for the variance process
dvt = b(vt)dt + a(vt)dZt
(1.32)
as we previously said, using the Black-Scholes risk-neutrality argument,
Equation (1.1) could be replaced with
dSt = (rt −qt)Stdt + σtStdBt
(1.33)
This is equivalent to changing the probability measure from the real one
to the risk-neutral one.24 We therefore need to use (1.33) together with the
risk-adjusted volatility process
dvt = ˜b(vt)dt + a(vt)dZt
(1.34)
where
˜b(vt) = b(vt) −λa(vt)
with λ the market price of volatility risk. This quantity is closely related to
the market price of risk for the stock λe = (µ −r)/σ. Indeed, as Hobson
[140] and Lewis [177] both show, we have
λ = ρλe +

1 −ρ2λ∗
(1.35)
where λ∗is the market price of risk associated with dBt −ρdZt, which can
also be regarded as the market price of risk for the hedged portfolio.
The passage from Equation (1.32) to Equation (1.34) and the introduc-
tion of the market price of volatility risk could also be explained by the
Girsanov theorem, as was done for instance in Fouque [104].
It is important to underline the difference between the real and the risk-
neutral measures here. If we use historic stock prices together with the real
stock-return drift µ to estimate the process parameters, we will obtain the
real volatility drift b(v). An alternative method would be to estimate ˜b(v) by
using current option prices and performing a least-square estimation. These
calibration methods will be discussed in detail in the following chapters.
24See Hull [146] or Shreve [218] for more detail.

26
INSIDE VOLATILITY ARBITRAGE
The risk-neutral version for a discrete NGARCH model would also
involve the market price of risk and instead of the usual
ln Sn+1 = ln Sn +

µ −1
2vn+1

+ √vn+1Bn+1
vn+1 = ω0 + βvn + αvn(Bn −c)2
we would have
ln Sn+1 = ln Sn +

r −1
2vn+1

+ √vn+1 ˜Bn+1
(1.36)
vn+1 = ω0 + βvn + αvn

 ˜Bn −c −λe
2
where ˜Bn = Bn + λe, which could be regarded as the discrete version of
the Girsanov theorem. Note that the market price of risk for the stock λe is
not separable from the leverage parameter c in the above formulation. Duan
shows in [84] and [86] that risk-neutral GARCH system (1.36) will indeed
converge toward the continuous risk-neutral GARCH
dSt = Strdt + St
√vtdBt
dvt = (ω −˜θvt)dt + ξvtdZt
as we expected.
The Two-Factor PDE
From here, writing a two-factor PDE for a derivative security f becomes a
simple application of the two-dimensional Ito’s lemma. The PDE will be25
rf = ∂f
∂t + (r −q)S ∂f
∂S + 1
2vS2 ∂2f
∂S2 + ˜b(v)∂f
∂v
+1
2a2(v)∂2f
∂v2 + ρa(v)√vS ∂2f
∂S∂v
(1.37)
Therefore, it is possible, after calibration, to apply a finite difference
method26 to the above PDE to price the derivative f (S t v). An alterna-
tive would be to use directly the stochastic processes for dSt and dvt and
apply a two-factor Monte Carlo simulation. Later in the chapter we will
also mention other possible methods, such as the mixing solution or asymp-
totic approximations.
25For a proof of the derivation see Wilmott [237] or Lewis [177].
26See, for instance, Tavella [227] or Wilmott [237] for a discussion on finite
difference methods.

The Volatility Problem
27
Other possible approaches for incomplete markets and stochastic volatil-
ity assumption include super-replication and local risk minimization.27 The
super-replication strategy is the cheapest self-financing strategy with a termi-
nal value no less than the payoff of the derivative contract. This technique
was primarily developed by El-Karoui and Quenez in [91]. Local risk mini-
mization involves a partial hedging of the risk. The risk is reduced to an
“intrinsic component” by taking an offsetting position in the underlying
security as usual. This method was developed by Follmer and Sondermann
in [102].
THE GENERALIZED FOURIER TRANSFORM
The Transform Technique
One useful technique to apply to the PDE (1.37) is the generalized Fourier
transform.28 First, we can use the variable x = ln S in which case, using Ito’s
lemma, Equation (1.37) could be rewritten as
rf = ∂f
∂t +

r−q−1
2v
∂f
∂x + 1
2v ∂2f
∂x2 + ˜b(v)∂f
∂v + 1
2a2(v)∂2f
∂v2 +ρa(v)√v ∂2f
∂x∂v
(1.38)
Calling
ˆf (k v t) =
	 +∞
−∞
eikxf (x v t)dx
(1.39)
where k is a complex number,29 ˆf will be defined in a complex strip where
the imaginary part of k is between two real numbers α and β. Once ˆf is
suitably defined, meaning that ki = I(k)(the imaginary part of k) is within
the appropriate strip, we can write the inverse Fourier transform
f (x v t) = 1
2π
	 iki+∞
iki−∞
e−ikx ˆf (k v t)dk
(1.40)
where we are integrating for a fixed ki parallel to the real axis.
Each derivative satisfying (1.37) or equivalently (1.38) has a known
payoff G(ST) at maturity. For instance, as we said before, a call option has
a payoff MAX(0 ST −K) where K is the call strike price. It is easy to see
27For a discussion on both these techniques, see Frey [107].
28See Lewis [177] for a detailed discussion on this technique.
29As usual we note i =
√
−1.

28
INSIDE VOLATILITY ARBITRAGE
that for ki > 1 the Fourier transform of a call option exists and the payoff
transform is
−Kik+1
k2 −ik
(1.41)
Proof:
Indeed, we can write
	 +∞
−∞
eikx(ex −K)+dx =
	 +∞
ln K
eikx(ex −K)dx
= 0 −
 Kik+1
ik + 1 −K Kik
ik

= −Kik+1

1
ik + 1 −1
ik

= −Kik+1
1
k2 −ik
as stated. (QED)
The same could be applied to a put option or other derivative securities.
In particular, a covered call (stock minus call) having a payoff MIN(ST K)
will have a transform for 0 < ki < 1 equal to
Kik+1
k2 −ik
(1.42)
Applying the transform to the PDE (1.38) and introducing τ = T −t and
ˆh(k v τ) = e(r+ik(r−q))τ ˆf (k v τ)
(1.43)
and posing30 c(k) = 1
2(k2 −ik), we get the new PDE equation
∂ˆh
∂τ = 1
2a2(v)∂2 ˆh
∂v2 + (˜b(v) −ikρ(v)a(v)√v)∂ˆh
∂v −c(k)v ˆh
(1.44)
Lewis calls the fundamental transform a function ˆH(k v τ) satisfying
the PDE (1.44) and satisfying the initial condition ˆH(k v τ = 0) = 1. If we
know this fundamental transform, we can then multiply it by the derivative
security’s payoff transform and then divide it by e(r+ik(r−q))τ and apply the
inverse Fourier technique by keeping ki in an appropriate strip and finally
get the derivative as a function of x = ln S.
Special Cases
There are cases where the fundamental transform is known. The case of a
constant (or deterministic) volatility is the most elementary one. Indeed,
30We are following Lewis [177] notations.

The Volatility Problem
29
using (1.44) together with dvt = 0, we can easily find
ˆH(k v τ) = e−c(k)vτ
which is analytic in k over the entire complex plane. Using the call payoff
transform (1.41), we can rederive the Black-Scholes equation. The same
can be done if we have a deterministic volatility dvt = b(vt)dt by using the
function Y(v t)where dY = b(Y)dt.
The square-root model (1.25) is another important case where ˆH(k v τ)
is known and analytic. We have for this process
dvt = (ω −θvt)dt + ξ√vtdZt
or under the risk-neutral measure
dvt = (ω −˜θvt)dt + ξ√vtdZt
with ˜θ = (1 −γ)ρξ +

θ2 −γ(1 −γ)ξ2, where γ ≤1 represents the risk-
aversion factor.
For the fundamental transform, we get
ˆH(k v τ) = exp [f1(t) + f2(t)v]
(1.45)
with
t = 1
2ξ2τ
˜ω = 2
ξ2 ω
˜c = 2
ξ2 c(k)
and
f1(t) =

tg −ln
1 −hetd
1 −h

˜ω
f2(t) =
 1 −etd
1 −hetd

g
where
d =

¯θ2 + 4˜c
g = 1
2( ¯θ + d)
h =
¯θ + d
¯θ −d
and
¯θ = 2
ξ2

(1 −γ + ik)ρξ +

θ2 −γ(1 −γ)ξ2

The above transform has a cumbersome expression, but it can be seen
that it is analytic in k and therefore always exists. For a proof of the foregoing
refer to Lewis [177].

30
INSIDE VOLATILITY ARBITRAGE
TABLE 1.1
SPX Implied Surface as of 03/09/2004. T is the maturity and M = K/S
the inverse of the moneyness
T / M
0.70
0.80
0.85
0.90
0.95
1.00
1.05
1.10
1.15
1.20
1.30
1.000
24.61
21.29
19.73
18.21
16.81
15.51
14.43
13.61
13.12
12.94
13.23
2.000
21.94
18.73
18.68
17.65
16.69
15.79
14.98
14.26
13.67
13.22
12.75
3.000
20.16
18.69
17.96
17.28
16.61
15.97
15.39
14.86
14.38
13.96
13.30
4.000
19.64
18.48
17.87
17.33
16.78
16.26
15.78
15.33
14.92
14.53
13.93
5.000
18.89
18.12
17.70
17.29
16.88
16.50
16.13
15.77
15.42
15.11
14.54
6.000
18.46
17.90
17.56
17.23
16.90
16.57
16.25
15.94
15.64
15.35
14.83
7.000
18.32
17.86
17.59
17.30
17.00
16.71
16.43
16.15
15.88
15.62
15.15
8.000
17.73
17.54
17.37
17.17
16.95
16.72
16.50
16.27
16.04
15.82
15.40
The inversion of the Fourier transform for the square-root (Heston)
model is a very popular and powerful approach. It is appealing because of
its robustness and speed. The following example is based on SPX options as
of 03/09/2004 expiring in 1 to 8 years from the calibration date (Tables 1.1
and 1.2).
As we shall see further, the optimal Heston parameter set to fit this
surface could be found via a least-square estimation approach and for the
index at S = $1156.86 we find the optimal parameters ˆv0 = 0.1940 and
ˆ = ( ˆω ˆθ ˆξ ˆρ) = (0.052042332 1.8408 0.4710 −0.4677)
THE MIXING SOLUTION
The Romano-Touzi Approach
The idea of mixing solutions was probably presented for the first time by
Hull and White [149] for a zero correlation case. Later, Romano and Touzi
TABLE 1.2
Heston Prices Fitted to the 03/09/2004 Surface
T / M
0.70
0.80
0.85
0.90
0.95
1.00
1.05
1.10
1.15
1.20
1.30
1.000
30.67
21.44
17.09
13.01
9.33
6.18
3.72
2.03
1.03
0.50
0.13
2.000
31.60
22.98
18.98
15.25
11.87
8.89
6.37
4.35
2.83
1.78
0.66
3.000
32.31
24.18
20.44
16.98
13.82
11.00
8.55
6.47
4.77
3.43
1.66
4.000
33.21
25.48
21.93
18.66
15.63
12.91
10.50
8.39
6.61
5.10
2.93
5.000
33.87
26.54
23.20
20.09
17.22
14.63
12.30
10.21
8.39
6.82
4.36
6.000
34.56
27.55
24.34
21.36
18.60
16.08
13.79
11.73
9.89
8.26
5.64
7.000
35.35
28.61
25.52
22.64
19.96
17.49
15.24
13.19
11.35
9.70
6.97
8.000
35.77
29.34
26.39
23.64
21.07
18.69
16.51
14.51
12.68
11.04
8.24

The Volatility Problem
31
70%
85%
95%
105%
115%
130%
0.00
5.00
10.00
15.00
20.00
25.00
j
K/S
FIGURE 1.6
The SPX implied surface as of 03/09/2004. We can observe the negative
skewness as well as the flattening of the slope with maturity.
[209] generalized this approach for a correlated case. The basic idea is to
separate the random processes of the stock and the volatility, integrate the
stock process conditionally upon a given volatility, and finally end up with
a one-factor problem. Let us be reminded of the two processes we had:
dSt = (rt −qt)Stdt + σtStdBt
and
dvt = ˜b(vt)dt + a(vt)dZt
under a risk-neutral measure.
Given a correlation ρt between dBt and dZt, we can introduce the
Brownian motion dWt independent of dZt and write the usual Cholesky31
factorization:
dBt = ρtdZt +

1 −ρ2
t dWt
We can then introduce the same Xt = ln St and write the new system of
equations:
dXt = (r −q)dt + dYt −1
2

1 −ρ2
t

σ2
t dt +

1 −ρ2
t σtdWt
(1.46)
dYt = −1
2ρ2
t σ2
t dt + ρtσtdZt
dvt = ˜btdt + atdZt
where, once again, the two Brownian motions are independent.
31See, for example, Press [204].

