# Volatility Consistency & Trading

!!! info "Source"
    **Inside Volatility Arbitrage: The Secrets of Skewness** by Alireza Javaheri, Wiley, 2005.
    These notes are used for educational purposes.

## The Consistency Problem

The Inference Problem
171
For VGSA, for a given arrival rate dt∗= ytdt, we have a VG distribution
and
d ln St = (µS + ω)dt + B(γ(dt∗ 1 ν); θ σ)
and the corresponding integrated density becomes
p(z|h h∗) =
2 exp

θxh/σ2
ν
h∗
ν √
2πσ
 h∗
ν


x2
h
2σ2/ν + θ2
	 h∗
2ν −1
4
K h∗
ν −1
2
 1
σ2

x2
h

2σ2/ν + θ2	
(2.31)
Indeed, as described in [182] for VG, we have
p(z|h) =
 +∞
0
p(z|g h)p(g|h)dg
with p(z|g h) a normal density and p(g|h) a gamma density. More accurately
p(z|g h) =
1
σ√2πg exp

−
1
2σ2g

z −µSh −h
ν ln

1 −θν −σ2ν/2

−θg
	2
and
p(g|h) = g
hν −1 exp(−g
ν)
ν
hν ( h
ν)
Now, for VGSA we simply have a different arrival rate h∗for the gamma
process and therefore
p(z|h h∗) =
 +∞
0
p(z|g h)p(g|h∗)dg
which demonstrates the point. This gives us the idea of using the arrival rate
as the state, and we use the following algorithm.
1. Initialize the state x(i)
0
and the weight w(i)
0
for i between 1 and Nsims
While 1 ≤k ≤N
2. Simulate the state xk for i between 1 and Nsims
˜x(i)
k = x(i)
k−1 + κ

η −x(i)
k−1

t + λ

x(i)
k−1
√
tN −1 
U(i)[0 1]

3. Calculate the associated weights for each i
w(i)
k = w(i)
k−1p

zk|˜x(i)
k


172
INSIDE VOLATILITY ARBITRAGE
with p(zk|˜x(i)
k ) as defined in (2.31), where h will be set to t and h∗to
the simulated state ˜x(i)
k times t
4. Normalize the weights
˜w(i)
k =
w(i)
k
 Nsims
i=1
w(i)
k
5. Resample the points ˜x(i)
k and get x(i)
k and reset w(i)
k = ˜w(i)
k = 1/Nsims.
6. Increment k, go back to Step 2 and Stop at the end of the While loop.
The advantage of this method is that there is one simulation process
instead of two, and we “skip” the gamma distribution altogether. However,
the dependence of the observation zk on xk is highly nonlinear, which makes
the convergence more difficult.
An Extended/Unscented Particle Filter
Finally, a natural idea would be to use a
proposal distribution q(x) for the state, taking into account the observation
information. In order to be able to use a Kalman-based proposal distribution
(EPF or UPF), we need a Gaussian approximation. Note that given the strong
non-Gaussianity of the equations, we absolutely need the particle filtering
aspect. The Gaussian approximation for the observation equation would
be39
zk = zk−1 +

µS + ω + θxk

t +

θ2ν + σ2
xktBk
which is of the form zk = h(xk Bk) and allows us to use the Kalman filtering
algorithm. We therefore replace Steps 2 and 3 of the previous algorithm with
the following.
2-a. Apply an extended/unscented Kalman filter for i between 1 and Nsims
to the state x(i)
k−1 and obtain
ˆx(i)
k = KF

x(i)
k−1

as well as the associated covariance P (i)
k .
2-b. Simulate the state for i between 1 and Nsims
˜x(i)
k = ˆx(i)
k +

P (i)
k N −1 
U(i)[0 1]

3. Calculate the associated weights for each i
w(i)
k = w(i)
k−1
p

zk|˜x(i)
k

p

˜x(i)
k |x(i)
k−1

q

˜x(i)
k |x(i)
k−1 z1:k

39We are using the fact that for X(t) = B
γ(t 1 ν);θσ

we have a mean θt and a
variance (θ2ν + σ2)t as stated in [182].

The Inference Problem
173
with p

zk|˜x(i)
k

as defined in (2.31), where h will be set to t and h∗to
the simulated state ˜x(i)
k times t, where p

˜x(i)
k |x(i)
k−1

is the normal density
with mean x(i)
k−1 + κ

η −x(i)
k−1

t and standard deviation λ

x(i)
k−1
√
t,
and where q

˜x(i)
k |x(i)
k−1 z1:k

is the normal density with mean ˆx(i)
k
and
standard deviation

P (i)
k .
The rest of the algorithm is exactly the same as the previous one.
What follows is a C++ routine for the EPF applied to VGSA.
// log_stock_prices
are the log of stock prices
// muS is the real-world stock drift
// n_stock_prices is the number of the above stock prices
// (kappa,eta,lambda,sigma,theta,nu) are the VGSA parameters
// ll is the value of (negative log) Likelihood function
// estimates[] are the estimated observations from the filter
// errors are the observation errors
// The function ran2() is from Numerical Recipes in C
// and generates uniform random variables
// The function Normal_inverse() can be found from
many sources
// and is the inverse of the Normal CDF
// Normal_inverse(ran2(.)) generates a set of Normal
random variables
// The Bessel and Gamma functions bessik() and gammln()
// are also available in Numerical Recipes in C
void estimate_particle_extended_VGSA_parameters_bessel(
double *log_stock_prices,
double mu,
int n_stock_prices,
double kappa,
double eta,
double lambda,
double sigma,
double theta,
double nu,
double *ll,
double *estimates,

174
INSIDE VOLATILITY ARBITRAGE
double *errors)
{
int
i1, i2, i3;
double
y0, z, omega;
int
M=1000;
double
x[1000], xx[1000], X;
double
w[1000],
u[1000], c[1000];
double
pz, px, q, s, m, l, x1_sum;
long
idum=-1;
double
delt=1.0/252.0;
double
eps=1.0e-30;
double
Ka,Ia,Kp,Ip, Kx,Knu;
double
H, A, x0, P0;
double
P[1000], P1[1000], U[1000], K[1000], W[1000];
double
x1[1000], x2[1000];
/* initialize */
omega=log(1.0-theta*nu- sigma*sigma*nu/2.0)/nu;
x0 = 1.0;
P0 = 0.000001;
for (i2=0; i2<M; i2++)
{
x[i2] = x0 + sqrt(P0)* Normal_Inverse(ran2(&idum));
P[i2] = P0;
}
A = 1.0-kappa*delt;
H = theta*delt;
/* time loop */
*ll=0.0;
for (i1=1;i1<n_stock_prices-1;i1++)
{
z = log_stock_prices[i1+1]-log_stock_prices[i1];
X= z - mu*delt - delt/nu*log(1.0-theta*nu-
sigma*sigma*nu/2.0);
l = 0.0;
x1_sum=0.0;
for (i2=0; i2<M; i2++)
{
/* EKF for the proposal distribution */
x1[i2] = x[i2] + kappa*(eta - x[i2])*delt;
W[i2]
= lambda*sqrt(x[i2] * delt);
P1[i2] = W[i2]*W[i2] + A*P[i2]*A;
x1[i2]=MAX(x1[i2],eps);

The Inference Problem
175
U[i2] = sqrt(theta*theta*nu+sigma*sigma)*
sqrt(x1[i2]*delt);
K[i2] = P1[i2]*H/( H*P1[i2]*H + U[i2]*U[i2]);
x2[i2] = x1[i2] + K[i2] *
(z - (mu+omega+theta*x1[i2])*delt);
x1_sum+= x1[i2];
P[i2]=(1.0-K[i2]*H)*P1[i2];
/* sample */
xx[i2] = x2[i2] + sqrt(P[i2])*
Normal_Inverse(ran2(&idum));
xx[i2]=MAX(xx[i2],eps);
/* calculate weights */
m = x2[i2];
s = sqrt(P[i2]);
q = 0.39894228/s * exp( - 0.5* (xx[i2] - m)*
(xx[i2] - m)/(s*s) );
m = x[i2] + kappa*(eta - x[i2])*delt;
s = lambda*sqrt(x[i2] * delt);
px = 0.39894228/s * exp( - 0.5* (xx[i2] - m)*
(xx[i2] - m)/(s*s) );
Kx
= MAX(eps, 1.0/(sigma*sigma)*
sqrt(X*X*(2*sigma*sigma/nu+theta*theta)));
Knu = MAX(eps, (xx[i2]*delt/nu-0.5));
bessik(Kx , Knu , &Ia, &Ka, &Kp, &Ip);
pz=2.0*exp(theta*X/(sigma*sigma)) /
(pow(nu,xx[i2]*delt/nu)*sigma*
exp(gammln(xx[i2]*delt/nu))) *0.39894228*
pow(X*X/(2*sigma*sigma/nu+theta*theta),
0.5*xx[i2]*delt/nu-0.25) * Ka;
w[i2]= pz * px / MAX(q, eps);
l += w[i2];
}
*ll += log(l);
/* estimates[i1+1] for z[i1] => error term */
estimates[i1+1]= log_stock_prices[i1+1]-
(log_stock_prices[i1] + (mu+omega+theta*x1_sum/M)*
delt);
errors[i1]
= (theta*theta*nu + sigma*sigma)*
x1_sum/M*delt;
/* normalize weights */
for (i2=0; i2<M; i2++)
w[i2] /= l;
/* resample and reset weights */
c[0]=0;

176
INSIDE VOLATILITY ARBITRAGE
for (i2=1; i2<M; i2++)
c[i2] = c[i2-1] + w[i2];
i2=0;
u[0] = 1.0/M * ran2(&idum);
for (i3=0; i3<M; i3++)
{
u[i3] = u[0] + 1.0/M *i3;
while (u[i3] > c[i2])
i2++;
x[i3]= xx[i2];
w[i3]=1.0/M;
}
}
*ll *= -1.0;
}
// *ll represents the (negative log) Likelihood
Numeric Results
We performed the same kind of back-testing procedure as
for the VG model, using either of the foregoing particle filters applied to an
artificially generated stock-price time series. We chose t = 1/252 , µ∗
S = 0,
y0 = 1 and
∗= (κ∗= 0 η∗= 0 λ∗= 0 ν∗= 0.005 θ∗= 0.02 σ∗= 0.2)
after applying the importance sampling/resampling PF via the modified Bessel
function, we found
ˆ = (0.13 0.001 0.37 0.0048 0.018 0.21)
which seems to indicate that the estimation process for (ν θ σ) works well,
whereas the one for (κ η λ) does not. However, if we simulate two sets
of spot-price times series with these different parameter sets, we will see
that the generated paths are very similar. See Figures 2.53 and 2.54. This
also confirms our previous remarks about the estimation of the parameters
affecting the noise.
We performed a second test with a more realistic choice of parameters,
with once again t = 1/252 , Nsims = 100 , and 500 data points correspond-
ing to two years. The real values were
∗= (κ∗= 2.10 η∗= 5.70 λ∗= 2.00 ν∗= 0.05 θ∗= −0.40 σ∗= 0.20)

The Inference Problem
177
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
1.1
1.2
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
Simulated Arrival Rates
y
y-bis
FIGURE 2.53
The Simulated Arrival Rates via  = (κ = 0 η = 0λ = 0
σ = 0.2θ = 0.02ν = 0.005) and  = (κ = 0.13η = 0λ = 0.40σ = 0.2,
θ = 0.02ν = 0.005) Are Quite Different; compare with Figure 2.54.
4.45
4.5
4.55
4.6
4.65
4.7
4.75
4.8
4.85
4.9
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
Simulated Log Stock Prices
lnS
lnS-bis
FIGURE 2.54
However, the Simulated Log Stock Prices are Close. (Compare with
Figure 2.53.)

178
INSIDE VOLATILITY ARBITRAGE
Note that θ has a negative value that corresponds to the negative skewness
of the distribution. We choose a fairly reasonable initial set
0 = (κ0 = 2.00 η0 = 6.00 λ0 = 1.50 ν0 = 0.03 θ0 = −0.30 σ0 = 0.30)
and
µ0 = µ∗= 0.05
We find the optimal parameter set
ˆ = (ˆκ = 4.25 ˆη = 7.89 ˆλ = 3.25 ˆν = 0.047 ˆθ = −0.40 ˆσ = 0.19)
and
ˆµ = µ∗= 0.05
Again we see that the estimations for the three VG parameters (ν θ σ)
are much more accurate than those corresponding to the arrival process
(κ η λ)—and this despite our choosing the initial arrival parameters close
to the real ones. As previously stated, the time series of spot prices has little
sensitivity to the arrival-rate parameters and a higher degree of sensitivity to
the gamma process parameters. Again, this shows that estimation method-
ologies such as MLE work much better when applied to parameters that
affect the drift of an observation, and not its noise.
Diagnostics
As for diagnostics, we need to estimate the observation error
associated with the algorithm. We define once again
ˆz(i)
k = zk−1 +

µS + ω + θ˜x(i)
k

t
ˆz−
k =
1
Nsims
Nsims

i=1
ˆz(i)
k
or
ˆz−
k = zk−1 + (µS + ω)t + θt
1
Nsims
Nsims

i=1
˜x(i)
k
and the error term
ek = zk −ˆz−
k
The variance associated with this error is
sk =

θ2ν + σ2
1
Nsims
Nsims

i=1
˜x(i)
k t
and
˜ek = ek/sk
would represent the normalized error.

The Inference Problem
179
–0.025
–0.02
–0.015
–0.01
–0.005
0
0.005
0.01
0.015
0.02
0.025
0
100
200
300
400
500
600
700
VGSA Observation Errors with GPF
MPE
FIGURE 2.55
The Observation Errors for the VGSA Model with a Generic Particle
Filter.
TABLE 2.15
MPE and RMSE for the VGSA Model Under a Generic PF as well as
the EPF.
MPE
RMSE
PF
-0.000350241
0.005867065
EPF
-4.74747e-07
0.005869782
MPE/RMSE
In order to measure the performance, once again we use the mean
price error (MPE) and the root mean-squared error (RMSE). As an example,
we use the S&P 500 data between 1992 and 1994 (as used in [182]). For the
generic particle filter (GPF) and the extended particle filter (EPF), we find
the results in Table 2.15.
As we can see, the use of the extended Kalman filter as the proposal
distribution brings some improvement. Also see Figures 2.55 and 2.56.
Chi-Square Test
The residuals are normal; a χ2
20 test provides us with a value
of 10.397699, which is below the threshold value of 31.5 for a confidence
of 0.95. This means that the non-Gaussianity was “filtered out” of the time
series successfully. This could also be observed in the corresponding his-
togram in Figure 2.57.

180
INSIDE VOLATILITY ARBITRAGE
–0.025
–0.02
–0.015
–0.01
–0.005
0
0.005
0.01
0.015
0.02
0.025
0
100
200
300
400
500
600
700
VGSA Observation Errors with EPF
MPE
FIGURE 2.56
The Observation Errors for the VGSA Model and an Extended Particle
Filter.
0
0.01
0.02
0.03
0.04
0.05
0.06
0.07
–10
–8
–6
–4
–2
0
2
4
6
8
10
Histogram for the VGSA Residuals
VGSA
normal(x)
FIGURE 2.57
The VGSA Residuals Histogram. The residuals are fairly normal.

The Inference Problem
181
0.85
0.9
0.95
1
1.05
1.1
1.15
0
5
10
15
20
25
30
35
40
45
50
Variogram for the VGSA Residuals
Variogram
1.0
FIGURE 2.58
The VGSA Residuals Variogram. The variogram is close to 1 as
expected.
Auto-Correlation
Having p = 7 parameters and taking K = 27, we shall have
K −p = 20, so we will compare the output of the Box-Ljung test to the χ2
20
threshold, which, as previously mentioned, for a confidence of 0.95 is around
31.5. We find a value of 0.001138, which definitely passes the test. This shows
that the residuals are indeed uncorrelated.
Variogram
The variogram still indicates that we have independent and iden-
tically distributed random variables. Calling
γh = 1
2E

(˜ek+h −˜ek)2
= 1
2E

˜e2
k+h

+ 1
2E

˜e2
k

−E[˜ek+h˜ek]
we should obtain 1
2+ 1
2−0 = 1, which is indeed the case as seen in Figure 2.58.
VGG
The observation is zk = ln Sk+1
zk = zk−1 + (µS + ω)t + θxk + σ√xkBk
with ω = 1ν ln(1 −θν −σ2ν/2), and the hidden state is
xk = Yk(t)

182
INSIDE VOLATILITY ARBITRAGE
We could take advantage of the fact that VG provides an integrated density
of stock return [182]. Calling z = ln(Sk/Sk−1) and h = tk −tk−1 and posing
ξh = z −µSh −h
ν ln(1 −θν −σ2ν/2)
we have
p(z|h) = 2 exp

θξh/σ2
ν
hν √
2πσ
 h
ν


ξ2
h
2σ2/ν + θ2
 h
2ν −1
4
K hν −1
2
 1
σ2

ξ2
h

2σ2/ν + θ2	
where Kα(x) corresponds to the modified Bessel function of second kind. As
we can see, the dependence on the gamma distribution is “integrated out.”
For the VGG for a given arrival rate dt∗= dYt we have a VG distribution
and
d ln St = (µ + ω)dt + B(γ(dt∗ 1 ν); θ σ)
and the corresponding integrated density becomes
p(z|h h∗) = 2 exp(θξh/σ2)
ν
h∗
ν √
2πσ( h∗
ν )

ξ2
h
2σ2/ν + θ2
 h∗
2ν −1
4
K h∗
ν −1
2
 1
σ2

ξ2
h

2σ2/ν + θ2	
(2.32)
hence the idea of using the arrival rate as the state and using the following
algorithm.
1. Initialize the state x(i)
0
and the weight w(i)
0
for i between 1 and Nsims
While 1 ≤k ≤N
2. Simulate the state xk for i between 1 and Nsims
˜x(i)
k = F −1
µa νa; t U(i)[0 1]

where as before F represents the gamma CDF.
3. Calculate the associated weights for each i
w(i)
k = w(i)
k−1p(zk|˜x(i)
k )
with p(zk|˜x(i)
k ) as defined in (2.32) where h will be set to t and h∗to
˜x(i)
k
4. Normalize the weights
˜w(i)
k =
w(i)
k
 Nsims
i=1
w(i)
k

The Inference Problem
183
5. Resample the points ˜x(i)
k and get x(i)
k and reset w(i)
k = ˜w(i)
k = 1/Nsims.
6. Increment k, go back to Step 2 and Stop at the end of the While loop.
As for VGSA, numeric tests were carried out in the following way. After
choosing a time step t = 1/252, µS = 0 and a parameter set
 = (µa = 10.0 νa = 0.01 ν = 0.05 σ = 0.2 θ = 0.002)
an artificial time series of N = 500 spot prices was generated. The preceding
filtering algorithm was then applied to this time series and the resulting
likelihood was maximized. The optimal parameter set was
ˆ = (9.17 0.19 0.012 0.21 0.0019)
It therefore seems that the parameters ν and νa are not recovered prop-
erly. Hence we ask, how sensitive are the observable spot prices to these
variables? Simulating two time series with the two different parameter sets,
we can see in Figure 2.59 that the results could be very close. This once again
brings up the issue of inference reliability. Not having enough data points,
we can get parameter sets that are quite different from the real ones and that
could generate similar time series. This is consistent with what we have seen
for diffusion-based processes.
4
4.5
5
5.5
6
6.5
7
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
Simulated Log Stock Prices
lnS
lnS-bis
FIGURE 2.59
Simulation of VGG-based Log Stock Prices with Two Different
Parameter Sets  = (µa = 10.0νa = 0.01ν = 0.05σ = 0.2θ = 0.002)
and  =
(9.17 0.19 0.012 0.21 0.0019). The observed time series remain close.

184
INSIDE VOLATILITY ARBITRAGE
A Bayesian Approach for VGSA
An approach similar to the one in the paragraph
on the Bayesian approach for Heston could be used here, because the latent
state follows the same square-root SDE. The only thing that changes is the
likelihood function. Instead of having a conditionally log normal observa-
tion, we have a conditionally VG observation. Furthermore, we do know the
density of the VG distribution under a closed form as previously mentioned.
Indeed as previously mentioned, we have the state (the arrival rate)
dyt = κ(θ −yt)dt + σy
√ytdWt
and the observation
d ln St = (µS + ω)dt + B(γ(dt∗ 1 ν); θ σ)
and the corresponding conditional likelihood becomes
p(ln Sk|yk ) = 2 exp

θxh/σ2
ν
h∗
ν √
2πσ( h∗
ν )

x2
h
2σ2/ν + θ2
	 h∗
2ν −1
4
× K h∗
ν −1
2
 1
σ2

x2
h(2σ2/ν + θ2)
	
with Kα(x) the modified Bessel function and
xh = ln(Sk/Sk−1) −µSh −h
ν ln

1 −θν −σ2ν/2

h = t
and
h∗= ykt
Finally, integrating over time, we have
p(ln S|y ) =
N

k=1
p(ln Sk|yk )
Note that in the classical VGSA model there is no correlation between the sys-
tem noise and the observation noise. This means that the likelihood function
will not depend on the parameters κ, θ, σy, and therefore the MH update step
becomes almost a Gibbs sampler (except for the adjustment factor  N
k=1 x2
k).
RECAPITULATION
We tested three categories of models: the Heston/GARCH category where
a pure diffusion assumption was used, the Bates category where Poisson
jumps were added to the stock SDE, and the VG category where a gamma
distribution was applied to the time dimension.

The Inference Problem
185
Model Identification
We saw from the table in Section 2.3.10 that in the pure diffusion category,
a power of 3/2 outperformed the Heston model (power of 1/2). As stated,
this is in line with the findings of Engle & Ishida [95].
Needless to say, adding Poisson jumps (Bates model) will reduce the
MPE/RMSE of the filters; however, it will also cause the number of param-
eters to increase. A simple comparison between the residual errors is there-
fore not fair. In other words, given the fundamental differences between the
categories, we need to judge their appropriateness not by comparing the
residuals, but by using financial arguments such as, should the stock process
contain jumps or not? Once a category is chosen, then we can compare the
performance of models belonging to a given category.
Note that a number of likelihood-based tools exist, such as the Akaike
information criterion [100], which will take into the account the number of
parameters when assessing the goodness of fit for a model. These tools would
therefore allow us to compare models belonging to different categories (e.g,
Heston vs. VGSA). However, these criteria remain valid only asymptotically.
As we saw, this often requires a large number of data points, which may or
may not be readily available.
Convergence Issues and Solutions
No matter which category we choose, it seems that the same convergence
issues exist. For all the foregoing models, we can see that a parameter affect-
ing the drift of the observation is much easier to estimate than one affecting
the noise of the observation. For the pure diffusion category, we saw that
all four parameters ω, θ, ξ, and ρ were difficult to estimate (in some cases)
and that the two latter parameters, which affect the noise of the noise, were
even harder to estimate properly. For the Bates model, we saw that the jump
parameters λ, j were much more straightforward to estimate than the afore-
mentioned four diffusion parameters. For the VGSA models, we saw that the
VG parameters θ, ν, and σ (which once again, affect the observation drift)
are much easier to infer than the arrival-rate parameters κ, η, and λ.
All this was explained via the poor observability at a daily frequency level
owing to the fact that t = o
√
t

. We tested the validity of this statement
by artificially reducing the observation noise and saw the convergence rate
increase dramatically.
As stated, a possible solution would be to employ more observation
points via the use of high-frequency data. We saw that the increase in the
number of observations and the decrease in t (after a certain level) do not
cancel, and a higher frequency would indeed cause the likelihood function

186
INSIDE VOLATILITY ARBITRAGE
to have a higher value and provide a better estimation of the parameters. In
any case, because we do not know in advance how good the inference results
will be and whether we are in the asymptotic area or not, it is always a good
idea to perform a simulation test and determine the sampling distribution of
each parameter.
In the next chapter, we shall apply these inference tools to a specific
question: are the implied distributions from the stock and options markets
consistent?

CHAPTER 3
The Consistency Problem
Whether cross-sectional option prices are consistent with the
time-series properties of the underlying asset returns is probably
the most fundamental of tests.
— David S. Bates
INTRODUCTION
In the previous chapter, we discussed two approaches for stochastic volatility
parameter estimation: the cross-sectional one, in which we use a number
of options prices for given strike prices (and possibly maturities), and the
time-series approach, in which we use the stock prices over a certain period
of time. One natural question1 would therefore be the following: Will the
theoretically invariant portion of the parameter sets obtained by the two
methods be the same?
More accurately, supposing we are at time t = 0 and we use J options
with strikes K1 ... KJ and with maturity T , we have
ˆoptions = argmin



J
j=1

Cmodel(t = 0 S0 Kj T  )
−Cmkt(t = 0 S0 Kj T )
2



(3.1)
These options could include calls or puts. Alternatively, during the period
[0 T ] we can observe (Sk)0≤k≤N corresponding to the time points t0 ... tN
1Aït-Sahalia [6], Bakshi et al. [20], and Dumas et al. [88] have already asked a
similar question; however, they use a different approach for the time-series treatment.
187

188
INSIDE VOLATILITY ARBITRAGE
with t0 = 0 and tN = T, and then apply one of the previously discussed filters
and estimate the parameter set via the maximum likelihood method.
ˆstocks = argmax{L(S0 ... SN )}
(3.2)
Now the question is how different these estimations for (ξ ρ) are and why.
As we saw in the previous chapter, the size of the time interval t and the
time-series length are to be questioned: Indeed t has to be small enough for
us to be able to apply the Girsanov theorem. However, we saw that for a very
small t, the filtering errors are so little that the MLE will not necessarily
converge to the right parameter set. On the other hand, we would need
the time series to be as long as possible, which requires a high observation
frequency.
This brings up a more fundamental question. The current financial eco-
nometrics literature seems to make inference-based conclusions using a lim-
ited amount of daily data. As we saw in Chapter 2, the time-series infer-
ence results are not necessarily reliable unless the number of observations
is sufficiently large. This is the central question of this chapter: Are the im-
plied parameters from the options markets and the assets time series indeed
inconsistent?
Many practical issues need to be questioned: How many strikes should
we be using in the cross-sectional analysis and which ones? Should we use
only OTM puts and calls for liquidity reasons? Many use a penalty function
p() in the cross-sectional optimization in order to get reasonable results. Do
we need such a function here? In the cross-sectional method, what value for
v0 are we using? Should we estimate this value together with the other four
parameters? If so, should this estimated ˆv0 be used in the time series?
If the results are substantially different for the parameters ξ and ρ (as-
suming the validity of the Girsanov theorem), can this test be used as an
argument against the validity of the Heston stochastic volatility model? Or
would it mean that the options markets do not predict the stock movements
as they should? And if so, does this mean that there is a profitable trading
strategy to take? That is, are options systematically mispriced?
If the Heston model is judged to be incorrect, what is the correct
model—GARCH or 3/2? Is the diffusion assumption itself to be questioned?
Do we need to introduce jumps?2
2Note that an alternative method not involving any optimization would be a method
of matching of moments. Indeed the Heston parameters ω θ ξ ρ are analytically
related to the first four moments of the time series (mean, variance, skew, kurtosis).
The calculation of the moments from the time series is fairly easy. The calcula-
tion of the moments from the options would require the use of the Carr-Madan
[50] replication strategy using all available strike prices. However, because the

The Consistency Problem
189
Another way to approach the question is to reason in the following man-
ner. If the information contained in the options markets is indeed
inconsistent with the one embedded in the assets time series, there should be
a regularly and conclusively profitable trade strategy. For instance, a higher
volatility-of-volatility and more negative correlation in the options market
should indicate the possibility of a profitable skewness trade (to be explained
later) in absence of crashes. We could therefore use the profit/loss of this trade
as an empirical measure of the inconsistency of the information.
If (and only if!) there exists a regular and definite profit generated from
this strategy, we can conclude that there is inconsistency. It is important to
note that this empirical measure is model free.
In our empirical analysis, unless stated otherwise, we shall use S&P 500
calls and puts. There are two main reasons for this. First, these are the most
liquid european options available on the CBOE. They expire on the third
Friday of each contract month at the open. Second, abundant research has
already been carried out on these options. Aït-Sahalia [6]; Bakshi, Cao, and
Chen [20]; Bates [30]; Dumas, Fleming, and Whaley [88] and many others
have all carried out their empirical analysis on S&P 500 options.
The data quality is obviously dependent on the degree of liquidity.
Another issue we need to take into account is that of synchronization
between the spot close price and the option close price. Even if the tim-
ing of these two closings is off by a few minutes, the accuracy of the implied
volatility can be affected. Bates [32] specifically mentions this issue.
Let us be clear on the fact that this chapter does not constitute a thorough
empirical study of the stock versus the options markets. It rather presents
a set of examples of application of our inference tools constructed in the
previous chapter. There clearly could be many other applications for these
tools. As discussed in Chapter 2, model identification is another instance.
THE CONSISTENCY TEST
In this section we shall compare the values of (ξ ρ) in the results ˆoptions
to ˆstocks obtained via MLE. The time period [0 T ] is fixed, and the time
interval t for the stock is daily, as in Chapter 2.
information contained in the first four moments is less complete than the informa-
tion contained in the density, the optimization method is more accurate. It might
seem that by avoiding the numeric optimization involved in our method we would
gain precision; however, given that the equations linking the first four moments and
the four parameters are nonlinear, we would need to solve them numerically, which
would be similar to an optimization.

190
INSIDE VOLATILITY ARBITRAGE
The Setting
The test is based on SPX options as of 01/02/2002 expiring in approximately
1 year from the calibration date. The daily time series is taken during a period
of 12 years corresponding to approximately 3000 points. The start of the
period is 10 years before the calibration date and the end of the period is
1 year after the expiration of the options. Ideally we should only use the
asset prices between the calibration date and the expiration to see whether
the options predict the asset movements consistently. However, this would
provide us with too few observation points.
In what follows we will be considering one example of comparison
between cross-sectional and time-series implied parameters. Many other sim-
ilar examples were examined. They are not reported here because they do
not change the conclusions. The original contribution of our approach is
presenting a systematic way to evaluate time-series embedded parameters.
We shall do this via the methodologies detailed in Chapter 2.
The Cross-Sectional Results
We consider one-year options as of January 2, 2002, for close-to-the-money
options. The calibration is done via LSE Monte Carlo mixing as well as
the Fourier inversion applied to the Heston model. We fix the instanta-
neous variance v0 at 0.04, and we take the index level at S0 = $1154.67. As
usual we take the appropriate interest-rate rT and dividend-yield3 qT, where
T represents the options’ maturity. The dividend yield could, for instance,
be the one implied from the forward contracts FT calculated as
qT = rT −1/T ln(FT/S0)
We use various strike-price sets (Kj ) and determine the average optimal
one-year parameters. Needless to say, the results are obtained under the
risk-neutral measure. We obtain the risk-neutral implied parameter set in
Table 3.1. which represents a rather high negative skewness and a high
kurtosis.4 The long-term volatility is √ω/θ ≈0.17. Needless to say, these
parameter values vary everyday, but usually remain in the same range.
Robustness Issues for the Cross-Sectional Method
1. For the cross-sectional analysis, we have used a mixing Monte Carlo
method. The Monte Carlo time steps of this method were spaced weekly.
3No discrete dividends were considered.
4We drop the “hat” notations for optimal parameters in this chapter for simplifiction.
For example, instead of ˆω we simply write ω.

The Consistency Problem
191
TABLE 3.1
Average Optimal Heston Parameter Set (Under the Risk-Neutral Dis-
tribution) Obtained via LSE Applied to One-Year SPX Options in January 2002.
Various strike-price sets were used.
ω
θ
ξ
ρ
0.03620
1.1612
0.4202
−0.6735
Therefore, one natural question is how sensitive to this choice the results
are. In order to verify this, we reran the simulations with daily Monte
Carlo time steps and obtained
ˆoptions−daily = (ω = 0.036846 θ = 1.169709
ξ = 0.42112 ρ = −0.67458)
which is close to the original set. We also checked the results with the
volatility-of-volatility series method, as well as the Fourier inversion
method, and obtained comparable parameters.
2. For our cross-sectional calibration, we used call bid prices. It is well
known that calls and put prices are not always consistent. Indeed, as
can be seen in Figure 3.1 the Put and Call implied-volatilities are slightly
0.2
0.205
0.21
0.215
0.22
0.225
0.23
0.235
0.24
1040
1060
1080
1100
1120
1140
1160
1180
1200
Implied Vol
Strike
SPX Put and Call Implied Vols
Call Bid
Call Ask
Put Bid
Put Ask
Average
FIGURE 3.1
Implied Volatilities of Close to ATM Puts and Calls as of 01/02/2002.
Maturity is 2002/12/21 and index at 1154.67 USD’s. The bid–ask spread can clearly
be observed.

192
INSIDE VOLATILITY ARBITRAGE
different, which seems to be a violation of put-call parity.5 However, this
difference is not large enough (the put and call bid–ask spreads actually
overlap), and a profitable arbitrage cannot take place simply based upon
this difference. This is why we consider the midpoint between puts and
calls to be bids and asks.
Our implied volatility is therefore
σimp = 1
4

σimp(CallBid) + σimp(CallAsk) + σimp(PutBid)
+σimp(PutAsk)

Using these “mid” implied volatilities as opposed to the original call bids
we obtain a parameter set
ˆoptions−mid−call−put = (ω = 0.043184
θ = 1.173119 ξ = 0.40258 ρ = −0.64593)
3. If we do include v0 in the set of parameters  = (ω θ ξ ρ v0) , then we
obtain
ˆoptions−mid−call−put = (ω = 0.043224 θ = 1.144957 ξ = 0.482009
ρ = −0.661427 √v0 = 0.224659)
It is possible to see that the optimal √ˆv0 is around 0.20, which corres-
ponds to our initial choice.
4. As already mentioned, further-from-the-money options are less reliable
in terms of pricing and liquidity. However, disregarding them decreases
the cross-sectional sensitivity to the volatility-of-volatility parameter.
Adding to the previous close-to-the-money strikes, additional further-
from-the-money ones, we find
ˆoptions = (ω = 0.035896 θ = 1.149324 ξ = 0.386453
ρ = −0.659319 √v0 = 0.221988)
Again, the drift parameters are stable, and so is v0. The question is, how
are the volatility parameters affected? Interestingly, we do not observe a
great difference from what we had with the previous sets. We therefore
have a good degree of robustness. In any case, we use various sets of
strike prices and take an average over the optimal parameter sets.
5. One issue to consider in the cross-sectional method is how the risk-
neutral implied distribution or, in our case the parameter set  evolves
over time. Needless to say, if the model was perfectly correct these par-
ameters would never change; however, as we know, this is never the case.
5This is most probably due to the illiquidity of ITM options, as explained in [192].

The Consistency Problem
193
The question therefore becomes, how time-homogeneous are these par-
ameters? Considering the same maturity 12/21/2002 but at a date closer
to this maturity, we use close-to-the-money strikes. More accurately, we
stand at 09/03/2002, take the spot at $878.02, and use the yield curve as
of 09/03/2002.
The strikes are
Kset = {775.00 800.00 825.00 850.00 875.00
900.00 925.00 950.00 975.00}
The optimization via Monte Carlo mixing provides
ˆoptions = (ω = 0.0501244 θ = 1.189817 ξ = 0.547149
ρ = −0.661552 √v0 = 0.265441)
which is not too far from the other parameter sets.
Time-Series Results
As mentioned, the first idea is to choose a period corresponding to the life of
the options considered in the previous section. In fact, we would like to see
whether the options are predicting the underlying asset dynamics correctly
during their life. However, this provides us with one year of daily data, or
252 points, which as we know from the previous chapter is highly insufficient
for time-series estimators. In order to obtain more reliable results, we use
various filters (EKF, EPF, etc.) and take the average optimal parameter set. For
a period of 12 years ending on January 2004 (which includes the options’
life) and applying the filters studied in Chapter 2, we obtain the average
results given in Table 3.2.
The results in Table 3.2 show a lower (ξ ρ) and therefore a lower
implied skewness and kurtosis—lower than the ones obtained from the
options markets.
Robustness Issues for the Time-Series Method
Given the above results, it would
be instructive to test the sensitivity of the observations to the drift param-
eters (ω θ) on the one hand, and to the volatility parameters (ξ ρ) on the
TABLE 3.2
Average Optimal Heston Parameter Set (Under the Statistical Distribu-
tion) Obtained via Filtered MLE Applied to SPX between January 1992 and January
2004. Various filters were used in the MLE.
ω
θ
ξ
ρ
0.018620
0.523947
0.096389
−0.132527

194
INSIDE VOLATILITY ARBITRAGE
6.5
6.55
6.6
6.65
6.7
6.75
6.8
6.85
6.9
6.95
0
50
100
150
200
250
Log Stock Price
Days
Sensitivity of Observations to Volatility Parameters
Cross-Sectional Parameters
Time-Series Parameters
FIGURE 3.2
The Observations Have Little Sensitivity to the Volatility Param-
eters. One-year simulation with √v0 = 0.20, ω = 0.04, θ = 0.5. Cross-sectional uses
ξ = 0.036 and ρ = 0.50, whereas time series uses ξ = 0.09 and ρ = −0.80. This is
consistent with what we had seen previously.
other.6 The point is that even if the state vk itself is greatly affected by these
volatility parameters, the impact of these parameters on the observations is
small. However, the impact of the drift parameters is quite large. This could
explain why the cross-sectional and time-series volatility-of-volatility param-
eters are not close. This point can be observed in the simulations represented
in Figures 3.2 through 3.5. Note that this issue is related to the discussion in
Chapter 2 on the sampling distribution. As previously stated, ξ and ρ have a
lesser effect on the observations because they affect the “noise of the noise.”
Financial Interpretation
The current financial econometrics consensus is the following: No matter
which case we consider, the cross-sectional parameters ξ and ρ are always
greater (in absolute value) than the time-series ones. This means that the
skewness and the kurtosis implied from options are stronger than those
implied from the time series. As we will see in the following paragraphs, this
could suggest a trade to take advantage of this inconsistency, supposing that
6Note that we could not have done this separation in a nonparametric model, such
as in [6].

The Consistency Problem
195
0.035
0.04
0.045
0.05
0.055
0.06
0.065
0
50
100
150
200
250
Variance
Days
Sensitivity of the State to Volatility Parameters
Cross-Sectional Parameters
Time-Series Parameters
FIGURE 3.3
The State Has a Great Deal of Sensitivity to the Volatility Param-
eters. One-year simulation with √v0 = 0.20, ω = 0.04, θ = 0.5. Cross-sectional uses
ξ = 0.036 and ρ = 0.50, whereas time series uses ξ = 0.09 and ρ = −0.80.
6.85
6.9
6.95
7
7.05
7.1
7.15
7.2
7.25
7.3
7.35
0
50
100
150
200
250
Log Stock Price
Days
Sensitivity of Observations to Drift Parameters
Cross-Sectional Parameters
Time-Series Parameters
FIGURE 3.4
The Observations Have a Great Deal of Sensitivity to the Drift Param-
eters. One-year simulation with √v0 = 0.20, ξ = 0.036, ρ = 0.50. Cross-sectional uses
ω = 0.04 and θ = 0.50 whereas time series uses ω = 0.08 and θ = 5.0.

196
INSIDE VOLATILITY ARBITRAGE
0.01
0.02
0.03
0.04
0.05
0.06
0.07
0
50
100
150
200
250
Variance
Days
Sensitivity of the State to Drift Parameters
Cross-Sectional Parameters
Time-Series Parameters
FIGURE 3.5
The State Has a Great Deal of Sensitivity to the Drift Parameters. One-
year simulation with √v0 = 0.20, ξ = 0.036, ρ = 0.50. Cross-sectional uses ω = 0.04
and θ = 0.50, whereas time series uses ω = 0.08 and θ = 5.0.
the options are misjudging the spot movements. We can observe the above
statement graphically by plotting the SPX volatility smile from the options
market prices on the one hand, and from the time-series implied parameters
on the other. Note that we need no calibration for the options because we
are using the usual Black-Scholes implied volatility. Figure 3.6 shows the
difference between the two slopes. Again, the options curve has a stronger
(negative) slope, which is consistent with a stronger negative product ξρ.
As explained in [69], the higher moments of the stock-price return can
be calculated from the stochastic-volatility model parameters. Indeed, for a
given parameter set  = (ω θ ξ ρ), we have
skewness =

3ξρe
1
2θT
√
θ



ω
θ

2 −2eθT + θT + θT eθT
−v0

1 + θT −eθT

ω
θ[(1 −θT + θT eθT) + v0(eθT −1)]
3
2


and
kurtosis = 3

1 + ξ2

 ω
θA1 −v0A2
B


The Consistency Problem
197
0.205
0.21
0.215
0.22
0.225
0.23
0.235
1040
1060
1080
1100
1120
1140
1160
1180
1200
Implied Vol
Strike (USD)
Options Implied versus Historic Volatility Smile for SPX as of 01/02/2002
Options
Historic
FIGURE 3.6
Comparing SPX Cross-Sectional and Time-Series Volatility Smiles (with
Historic ξ and ρ) as of January 2, 2002. The spot is at $1154.67.
with y = θT and
A1 =

1 + 4ey −5e2y + 4yey + 2ye2y
+ 4ρ2

6ey −6e2y + 4yey + 2ye2y + y2ey
A2 = 2

1 −e2y + 2yey
+ 8ρ2 
2ey −2e2y + 2yey + y2ey
B = 2θ
ω
θ

1 −ey + yey
+ v0(ey −1)
2
Without entering into the details of the calculations, we can see that for given
ω and θ, higher (ξ |ρ|) correspond to higher skewness and kurtosis. As we
said in the previous chapter, the skewness depends on ω, θ and the product
ξρ, which has a more reliable estimation than the separate values of ξ and ρ.
This makes the estimation of the skewness more trustworthy.
THE PESO THEORY
Background
As [6] mentions, one possibility regarding the cross-sectional versus time-
series observed differences is the following. As we know, the time series
corresponds to one realization of the stock-return stochastic process. Now

198
INSIDE VOLATILITY ARBITRAGE
supposing that the true stock stochastic differential equation (SDE) contains
jumps, there is a possibility that the historic path we are observing does
not contain any of these jumps.7 This is referred to as the peso theory. As
mentioned in [12], this term goes back to Milton Friedman in his analysis of
Mexican peso during the early 1970s. The Mexican interest rates remained
significantly above the U.S. interest rates, although the peso was pegged at
0.08 dollar per peso. Friedman argued that the interest rates reflected an
expectation about a future devaluation of the peso. In August 1976, the
peso was devaluated by 37.5% to a new rate of 0.05 dollar per peso, thus
validating the previous interest rate differential.
This assumption seems reasonable because, as we saw in the previous
tests, the cross-sectional method usually provides higher volatility param-
eters (ξ ρ) and therefore higher skewness (in absolute value) and kurtosis.
Introducing a jump component in the options pricing model should lower
these optimal parameters.
Note that in [3], Aït-Sahalia tries to find out whether the discrete obser-
vations of S&P 500 come from a diffusion, or from a distribution containing
jumps. He derives a criterion for continuity of the paths
∂2
∂x∂y ln (p(t y = Xt+t|x = Xt)) > 0
for every t > 0 and given (x y). Based on the implied cross-sectional dis-
tribution, he finds that S&P 500 options do consider jumps in the paths.
Using the jump diffusion model, as we did in Chapter 2
d ln St =

µS −1
2vt + λj

dt + √vtdBt + ln(1 −j)dNt
dvt = (ω −θvt)dt + ξ√vtdZt
we may very well see no difference introduced from the parameters (λ j) for
the time series and we can even disregard them. However, this does not mean
that the stock process does not contain jumps but rather that this specific
path happens to contain none.
The options, by contrast, always include the possibility of jumps in their
pricing. Adding (λ j) will affect the resulting (ξ ρ) from the cross-sectional
method.
7Jackwerth and Rubinstein [155] refer to this phenomena as crash-o-phobia.

The Consistency Problem
199
Numeric Results
We use the same options and time series as in the previous section. As shown
in Merton’s paper [190], we have for a given volatility path σ = √v
Call =
+∞

n=0
e−λ(1−j)T (λ(1 −j)T )n
n!
CBS(S K T  σ rn)
with
rn = r + λj + n
T ln(1 −j)
We then take the expectation upon the volatility stochastic process as we
usually do in a mixing algorithm.8
We find for the parameter set ˆ = (ω θ ξ ρ λ j) the values
ˆoptions = (ω θ ξ ρ √v0 λ j) = (0.032648 1.165598 0.360646
−0.585302 0.218333 0.008982 0.913772)
instead of the previous pure-diffusion parameter set
ˆoptions−mid−call−put = (ω = 0.043224 θ = 1.144957 ξ = 0.482009
ρ = −0.661427 √v0 = 0.224659)
As we see even with the addition of jump parameters (λ j), the cross-sectional
volatility parameters (ξ ρ) remain significantly above the time-series param-
eters. This is in agreement with the findings of Bakshi, Cao, and Chen [20].
We have a small λ and a j close to one. This means that options are expecting
a large but infrequent jump; that is, they are factoring in the possibility of a
crash.
TRADING STRATEGIES
Supposing that the model we are dealing with is correct, and if the options
are mistaken in evaluating the stock distribution during their lifetime, there
should be an arbitrage opportunity to take advantage of. The ninth chapter
of the Härdle et al. book [128] has a description of these strategies. Note that
both these strategies are European and cannot be changed9 until maturity.
8Note that an alternative method would be to use a Fourier inversion of the known
characteristic function, as Lewis does in [178] or [180].
9As we will see further, we could unwind the deal prior to expiration. However, we
would then be subject to the movements of options prices.

200
INSIDE VOLATILITY ARBITRAGE
At this point we should reiterate that the profit and loss of this trade
could be used as an empirical and model-free measure of how consistent or
inconsistent the information embedded in the options is with the one in the
underlying stocks.
Skewness Trades
To capture an undervalued third moment, we can buy OTM calls and sell
OTM puts. Note that Aït-Sahalia [6] says that the options are overly skewed,
which means that the options skew is larger in absolute value. However, given
the negative sign of the skew, the cross-sectional skew is actually lower than
the one implied by the time series, hence the described strategy.
Note that in order to be immune to parallel shifts of the volatility curve,
we should make the trade as vega-neutral as possible. The correspondence
between the call and the put is usually not one-to-one. Therefore, calling V
the vega, ’s the hedge ratios for C the call and P the put option, then the
hedged portfolio  will be
 = C(St KC) −VC
VP
P (St KP ) −

C −VC
VP
P

St
and the positions in the options should be dynamically adjusted in theory.
However, that would cause too much transaction cost and exposure to the
bid-ask spread.
As we shall see in the paragraph on “exact replication,” more-elaborate
strategies are available to better exploit the third-moment differences.
Kurtosis Trades
To capture an overvalued fourth moment, we need to use the “fat tails”
of the distribution. For this we can, for instance, sell ATM and far OTM
options, and buy close OTM options.
Directional Risks
Despite the delta-hedging, the skewness trade applied to an undervalued
third moment has an exposure to the direction of the markets. A bullish
market is favorable to it, and a bearish one unfavorable. The kurtosis trade
applied to an overvalued fourth moment generates a profit if the market
stays at one point and moves sideways but loses money if there are large
movements.

The Consistency Problem
201
–10
–5
0
5
10
15
70
80
90
100
110
120
130
Pay-Off
Stock Price
Skewness Trading Strategy Pay-Off
Pay-Off
FIGURE 3.7
A Generic Example of a Skewness Strategy to Take Advantage of the
Undervaluation of the Skew by Options. This strategy could be improved upon by
trading additional OTM puts and calls.
This exposure to market conditions is consistent with the peso theory.
The skewness and kurtosis trading strategies above are profitable given the
options’ implied moments, unless the options were actually right in factor-
ing in a large and sudden downward movement. This also makes sense be-
cause the way the options were priced changed only after the crash of 1987.
Prior to that, the volatility negative skew was practically absent altogether.
Figures 3.7 and 3.8 show generic examples of the strategies described above.
Note that as the skew formula in [69] shows, the volatility-of-volatility
ξ affects the skew as much as the correlation ρ does. This explains why
sudden upward movements can hurt us as well. If the overall correlation
is negative but there are large movements in both directions, we will have
large third (in absolute value) and fourth moments, which would make the
options expectations correct. In fact, as we will see in the following example,
a large upward movement can make us lose on our hedge account.
As many, such as [32] and [128], have mentioned, it is possible to
interpret this trade as an insurance selling strategy. The trade will gener-
ate moderate and consistent profits if no crash happens. But if the crash does
happen we could suffer a large loss.
Skewness vs. Kurtosis
The skewness trade seems to be a simpler one and has
a better chance to be realized. Indeed, in order to have a large negative skew,

202
INSIDE VOLATILITY ARBITRAGE
–16
–14
–12
–10
–8
–6
–4
–2
0
2
4
70
80
90
100
110
120
130
Pay-Off
Stock Price
Kurtosis Trading Strategy Pay-Off
Pay-Off
FIGURE 3.8
A Generic Example of a Kurtosis Strategy to Take Advantage of the
Overvaluation of the Kurtosis by Options. This strategy could be improved upon by
trading additional puts and calls.
we need a large volatility-of-volatility ξ (as we do for the kurtosis trade)
and a large negative correlation ρ. In other words, if for a given stock time
series we have a large volatility-of-volatility but a weak correlation, we will
not have a kurtosis trade opportunity but we will have a skewness trade
opportunity. The historic skew will be small and the historic kurtosis high.
Graphically, we could have the following interpretation. For these assets, the
historic distribution does have fat tails, but remains symmetric, whereas the
implied distribution has a fatter left tail. This is why we have a skewness trade
opportunity, even if we do not have a kurtosis trade opportunity. Finally, as
we previously mentioned, the estimation of the skewness from a time series
is more reliable because it depends only on the product of the volatility-
of-volatility and the correlation.
An Exact Replication
These trading strategies can be refined using a Carr-Madan replication. As
explained in [50], we have for any payoff function f () the following identity
E[f (ST)]
= f (F) + erT
 F
0
f
′′(K)P(S0 K t = 0 T )dK
+ erT
 +∞
F
f
′′(K)C(S0 K t = 0 T )dK
with F = S0erT the forward price.

The Consistency Problem
203
In order to get the Das [69] skew and kurtosis calculations, we need to
take for the nth moment
f (ST) = (ZT −E(ZT))n
with
ZT = ln(ST/S0)
However, this trade will clearly have a much higher transaction cost than
the one described in the previous paragraph.
The Mirror Trades
Should we see the opposite conditions in the market, that is, having the skew
(in absolute value) or kurtosis undervalued by the options given a historic
path, we could obviously put on the mirror trades. The inverse of the peso
theory would be as follows. The stock in question has already had a crash and
the options are supposing there probably will not be another one in the near
future. Setting up the overvalued kurtosis trade in the previous paragraph,
we picked up a premium and made an immediate profit and hoped that there
would not be a sudden movement. Here we start by losing money and hope
a crash will happen within the life of the option so that we can generate
a profit. Because jumps and crashes are rare by nature, this trade does not
seem very attractive. Moreover, if there was a recent crash, the possibility of
another one is indeed reduced and we should believe the options prediction.
However, these mirror trades could be considered as buying insurance and
therefore as a protection against a possible crash.
An Example of the Skewness Trade
The algorithm is as follows. For a given date t0 we have S0 and choose the
closest maturity to T = t0 + 0.25 in order to have a three-month trade, we
then take the call and put strikes KC and KP as the closest ones to 1.10S0
and 0.90S0, respectively.
The original cost is therefore
options(0) = CallAsk(S0 KC t0 T ) −PutBid(S0 KP  t0 T )
Note that we buy a call at the offer price and sell the put at the market bid
price. At maturity, the position is worth
options(T ) = MAX(0 ST −KC) −MAX(0 KP −ST)

204
INSIDE VOLATILITY ARBITRAGE
During the trade, we have a delta-hedging cash flow of
hedge = −
T −1

t=0
(St t T )(St+1 −St)
with
(St t T )=Call(St KC t T  σimp(t0 KC))−P ut(St KP t T  σimp(t0 KP ))
where the implied volatilities used in the hedge ratios are using the mid prices
(between bid and ask prices). The interest-rate cash flow is
interest =
T −1

t=0
(St t T )(ertt −1)St
Our final profit or loss (PnL) is therefore
PnL = options(T ) −options(0) + hedge + interest
If the options’ implied skew is indeed higher than justified by the stock move-
ments, then this trade should be profitable. However, in case of a sudden large
movement, this will not be true anymore.
We consider the case of the S&P 500 between 04/04/2002 and
06/22/2002. At that point in time, S0 = $1126.34, which means we can take
KC = $1250 and KP = $1050. We also have CallAsk(t0 K = 1250) = $3.20
and PutBid(t0 K = 1050) = $14.20, as well as the mid implied volatilities
of σimp(KC) = 0.154 and σimp(KP ) = 0.214.
As can be seen in Figures 3.9 and 3.10, the sudden spot movements
generate most of the loss (for instance, around day 50). We have at the end
of the trade
ST = $989.14
hedge = $50.39
interest = $1.32
Therefore, the final PnL (in dollars) is
PnL = [0 −(1050 −989.14)] + (14.20 −3.20) + 50.39 + 1.32 = 1.85
As we can see, we hardly generated a profit, given the “jumps” occurring in
the middle of the trade.
Note that we generated a profit in the beginning by selling an OTM
put that was more expensive than the OTM call we bought. We lost a large
amount because the spot ended below the put strike. However, we compen-
sated that via the hedge.

The Consistency Problem
205
980
1000
1020
1040
1060
1080
1100
1120
1140
0
10
20
30
40
50
60
Spot Price
Days
SPX Movements During the Trade
SPX Price
FIGURE 3.9
Historic Spot Level Movements During the Trade Period.
–30
–20
–10
0
10
20
30
0
10
20
30
40
50
Delta PnL
Days
Hedge PnL During the Trade
Delta PnL
Zero PnL
FIGURE 3.10
Hedging PnL Generated During the Trade Period. As we can see, losses
occur upon jumps.
The Options Bid–Ask Spread
It is important to know where we are buying the
call and selling the put on the start date. Are we buying the call at the offer
price and selling the put at the bid price? If so, we can lose the bid–ask spread,
as compared to the case in which we would buy and sell both options at the

206
INSIDE VOLATILITY ARBITRAGE
–10
0
10
20
30
40
50
60
0
10
20
30
40
50
60
Days
Cumulative Hedge PnL
Cumulative Delta PnL
FIGURE 3.11
Cumulative Hedging PnL Generated During the Trade Period. This
positive PnL will be offset by the option premiums and payoffs.
mid market. This spread averages approximately $1 for 10% OTM SPX
options.
Early Termination
We also should consider an early unwinding of the trade.
Indeed as we get closer to maturity, our hedge-ratio might be close to one,
which will make our hedge account extremely sensitive to adverse stock
movements. In order to have a smoother PnL, we can buy back the put and
sell the call at a date (e.g. one month) prior to maturity. Again, it is important
to know whether we are unwinding the trade by selling the call at the bid
and buying back the put at the offer. If so, we will have suffered from the
bid–ask spread twice: once on the start date and once on the unwinding
(termination) date.
This is not just a small detail, indeed having the right execution (at mid-
market) can change the average sign of the PnL altogether. Furthermore,
regardless of the bid–ask spread, we are subject to the movements of the
options prices. By contrast, if we hold the positions until expiration, we will
have a pure strategy between the original options prices and the spot price
movements.
Implied Volatility Term Structure
Yet another issue to take into account is that,
in our back-testing, we used fixed implied volatilities in order to calcu-
late the hedge ratios during the life of the trade. In reality, the implied

The Consistency Problem
207
0.24
0.25
0.26
0.27
0.28
0.29
0.3
0.31
120
125
130
135
140
Implied Vol
Strike (USD)
Options Implied versus Historic Volatility Smile for MMM as of 03/28/2003
Options
Historic
FIGURE 3.12
A Strong Option-Implied Skew: Comparing MMM (3M Co) Cross-
Sectional and Time-Series Volatility Smiles as of March 28, 2003. The spot is at
$131.66.
0.38
0.39
0.4
0.41
0.42
0.43
0.44
0.45
22.5
23
23.5
24
24.5
25
Implied Vol
Strike (USD)
Options Implied versus Historic Volatility Smile for CUM as of 03/28/2003
Options
Historic
FIGURE 3.13
A Weak Option-Implied Skew: Comparing CMI (Cummins Inc) Cross-
Sectional and Time-Series Volatility Smiles as of March 28, 2003. The spot is at
$24.59.

208
INSIDE VOLATILITY ARBITRAGE
volatilities change every day even if we assume a sticky strike regime, in
which the stock price will not affect the implied volatility level. Even if our
strikes are fixed, the time-to-maturities of the options decreases, and this
will make the implied volatilities vary. For S&P 500 the term structure of
implied volatility is upward-sloping, which means that theoretically all
implied volatilities should come down from their original levels at the
unwinding date.
Which Hedge Ratio should we use?
In the hedging of our skew portfolio, which
 should we apply? In other words, we ask which implied volatility should
we use in the usual
e−q(T −t)N(d1(St K t T  σimp))
If we believe that the volatility predicted by the options is wrong and the
historic levels are correct, we should then use
σimp
stocks(K T ) = C−1
BS

Cmodel(S0 t0 K T  ˆstocks)

where
ˆstocks = ( ˆωopts ˆθopts ˆξstocks ˆρstocks)
Note that this might give us a mismatch in terms of mark-to-market with the
existing option levels in the market. However, if the time series is actually
correct, the skew should eventually collapse before the options mature.10
We should note, however, that using the options’ implied volatilities makes
better practical sense because those are the ones at which the options are
actually traded.
Multiple Trades
The next natural step would be to repeat the previous trade in order to see
whether the trade would be statistically profitable. We use SPX puts and calls
between 01/02/2002 and 02/01/2003 on the expiration month such that the
10Bates [29] suggests the use of an adjusted delta as
 ≈BS −K
S V ∂σ
∂K
where V represents the option vega. However, as he points out, this is the hedge ratio
as perceived by the options market and this perception could very well be wrong.
After all, this is what we are trying to take advantage of: the mispricing of the skew
by the options, supposing that the historic time series has the same dynamics as the
future spot movements.

The Consistency Problem
209
original life of the trade is around three months. We systematically unwind
the trades around 20 business days to expiration. Once again, we buy 10%
OTM calls and we sell 10% OTM puts.
We cover in this manner forty different cases. We calculate the PnL’s as
previously described and take their average.
The results are mixed: If we put the trade on and unwind at the bid and
ask levels, we will actually suffer a loss. However, if we can execute at
the mid, then we will generate a profit.
This shows a lack of decisive proof on an inconsistency between the
options and stock markets.11 Indeed we have used the PnL of this trade as a
measure of discrepancy.12
High Volatility-of-Volatility and High Correlation
As previously discussed, many stocks do have a high historic volatility-of-
volatility ξ; however, given a weak (or even positive) spot-volatility correl-
ation ρ, the historic skew is still very low. This is especially true of “penny”
stocks. Indeed, when these stocks increase in price, in some sense they “come
back to life” and therefore become more volatile. This means that the his-
toric skew is actually positive, which seems to indicate an even stronger
case for a skewness trade. However, given that we are dealing with penny
stocks, the possibility of a crash for these stocks is high, and that is precisely
what causes the negative option–implied skew! The stock GW (Grey Wolf
Inc.) in Figure 3.14 is a good example for this case. This presents a trading
opportunity as shown in Figure 3.15. By contrast, there are cases, such as
MSFT (Microsoft), where we do have a strong historic negative correlation as
well as a high volatility-of-volatility. As the stock price goes down, the asset
becomes riskier and therefore more volatile. We can see this in Figure 3.16.
This justifies the option-implied skew observable in Figure 3.17 and means
that there is no trade opportunity. The safest trade therefore seems to be an
11Note that this trade generates a regular and stable profit and sudden large losses.
This is in agreement with the interpretation of selling insurance and collecting the
premiums. It is very profitable until there is a “disaster.”
12There is a case where a skew trade should be considered. Even if we have an
inefficient estimate of ξ and ρ, we do have their sampling distributions, as seen in
Chapter 2. If, for instance, the average estimate of ξ is 0.03, supposing the lowest
and highest estimates are respectively −0.20 and 0.20, and if ξopt = 0.40, then there
is an inconsistency in a conclusive manner. We would then have our cross-sectional
volatility-of-volatility far superior to its highest possible time-series estimate.

210
INSIDE VOLATILITY ARBITRAGE
2.5
3
3.5
4
4.5
5
5.5
0
50
100
150
200
250
Spot Price
Days
Historic Spot Prices for GW
Spot
FIGURE 3.14
GW (Grey Wolf Inc.) Historic Prices (03/31/2002–03/31/2003) Show
a High Volatility-of-Volatility But a Weak Stock-Volatility Correlation. The resulting
negative skew is low.
0.4
0.45
0.5
0.55
0.6
0.65
0.7
0.75
0.8
2.5
3
3.5
4
4.5
5
Implied Vol
Strike (USD)
Options Implied versus Historic Volatility Smile for GW as of 03/31/2003
Options
Historic
FIGURE 3.15
The Historic GW (Grey Wolf Inc.) Skew Is Low and Not in Agreement
with the Options Prices. There is a skew trading opportunity here.


## Trading Volatility

The Consistency Problem
211
21
22
23
24
25
26
27
28
29
30
31
0
50
100
150
200
250
Spot Price
Days
Historic Spot Prices for MSFT
Spot
FIGURE 3.16
MSFT (Microsoft) Historic Prices (03/31/2002–03/31/2003) Show a
High Volatility-of-Volatility and a Strong Negative Stock-Volatility Correlation. The
resulting negative skew is high.
0.38
0.39
0.4
0.41
0.42
0.43
0.44
0.45
20
22
24
26
28
30
Implied Vol
Strike (USD)
Options Implied versus Historic Volatility Smile for MSFT as of 03/31/2003
Options
Historic
FIGURE 3.17
The Historic MSFT (Microsoft) Skew Is High and in Agreement with
the Options Prices. There is no skew trading opportunity here.

212
INSIDE VOLATILITY ARBITRAGE
800
900
1000
1100
1200
1300
1400
1500
0
50
100
150
200
250
Spot Price
Days
Historic Spot Prices for NDX
Spot
FIGURE 3.18
NDX (Nasdaq) Historic Prices (03/31/2002–03/31/2003) Show a High
Volatility-of-Volatility and a Strong Negative Stock-Volatility Correlation. The result-
ing negative skew is high.
index skewness trade, given that the likelihood of a crash is lower thanks to
the diversification effect.
Note that the strong negative historic skew is not limited to individual
stocks. Taking the case of the NDX index in Figures 3.18 and 3.19, we can
see that there is no trading opportunity available and the historic skewness
is in line with the one implied by the options prices.
Therefore we have two possible reasons13 why a skewness trade oppor-
tunity may exist.
1. Weak historic volatility-of-volatility (e.g., SPX [S&P 500])
2. Weak Historic Correlation (e.g., GW [Grey Wolf Inc.])
If neither of the above is verified (e.g., NDX [Nasdaq] or MSFT [Microsoft]),
there is no skew trading opportunity.
The graphical interpretation seen in Figures 3.12 through 3.19 is based
on the comparison of the observable options-implied skew
σimp
options(K T ) = C−1
BS (Cmkt(S0 t0 K T ))
and the skew implied from historic stock-price movements
σimp
stocks(K T ) = C−1
BS

Cmodel(S0 t0 K T  ˆstocks)

13These tests were performed around the end of March 2003.

The Consistency Problem
213
0.3
0.32
0.34
0.36
0.38
0.4
960
980
1000
1020
1040
1060
1080
1100
1120
1140
Implied Vol
Strike (USD)
Options Implied versus Historic Volatility Smile for NDX as of 03/31/2003
Options
Historic
FIGURE 3.19
The Historic NDX (Nasdaq) Skew is High and in Agreement with the
Options Prices. There is no skew trading opportunity here.
where CBS corresponds the usual Black-Scholes pricing function.
Again we use the option-implied volatility-drift parameters ˆωoptions,
ˆθoptions in ˆstocks. The only assumption here would be that of diffusion
in the processes. Then, according to the Girsanov theorem, the volatility-
of-volatility and the correlation should be the same for the continuous stat-
istical and risk-neutral processes.
NON-GAUSSIAN CASE
As previously discussed, once we start dealing with some of the pure-jump
models, such as VGG, we will no longer have the Girsanov theorem and
cannot compare the parameters directly. However, no matter what the arrival
process is, we still have the VG parameters (σ ν θ) as in
d ln St = (µS + ω)dt + X(dt; σ ν θ)
where, as before, µS is the real-world statistical drift of the stock log-return
and ω = 1ν ln(1 −θν −σ2ν/2). As for X(dt; σ ν θ), it has the following
meaning
X(dt; σ ν θ) = B(γ(dt 1 ν); θ σ)

214
INSIDE VOLATILITY ARBITRAGE
where B(dt; θ σ) would be a Brownian motion with drift θ and volatility σ.
In other words
B(dt; θ σ) = θdt + σ
√
dtN(0 1)
where N(0 1) is a standard Gaussian realization.
Further, we know what the centralized third and fourth moments (skew-
ness and kurtosis) are
skewness =

2θ3ν2 + 3σ2θν

t
kurtosis =

3σ4ν + 12σ2θ2ν2 + 6θ4ν3
t +

3σ4 + 6σ2θ2ν + 3θ4ν2
t2
We therefore can always compare the skewness and kurtosis implied from
time series with those implied from options. However, a mismatch between
the two does not indicate an arbitrage opportunity because once again we
are comparing them under two different measures. Having said this, the
determination of the statistical density p() and the risk-neutral density q()
is still useful in the sense that it could allow us to determine the optimal
position we would take in the derivatives market given a utility function, as
described in [52] and [53].
Indeed, having an increasing concave utility function U(), the idea is
to find the optimal payoff φ(S), maximizing the expected utility at a given
horizon T , and among all possible payoffs f (S)
φ = argmax
 +∞
0
U[f (ST)]p(ST)dST
In addition to this, we have the initial budget W0, which imposes a constraint:
The discounted risk-neutral expected value of the payoff cannot be greater
than this initial budget.
exp(−rT )
 +∞
0
f (ST)q(ST)dST ≤W0
This can be seen by using a “self-financing” portfolio argument, as was done
by Black and Scholes. Using the two foregoing equations, we can write the
Lagrangian
L(f ) =
 +∞
0
U

f (ST)

p(ST)dST −λ exp(−rT )
 +∞
0
f (ST)q(ST)dST
where λ is the Lagrange multiplier. We then can differentiate with respect to
the payoff f () and obtain the optimal payoff satisfying
exp(rT )p(S)
q(S)U ′[φ(S)] = λ

The Consistency Problem
215
or equivalently
φ(S) = (U ′)−1

λ exp(−rT ) q(S)
p(S)

and the constant λ could be determined by a normalization, such as
exp(−rT )
 +∞
0
(U ′)−1

λ exp(−rT ) q(S)
p(S)

q(ST)dST = W0
This would provide us with the optimal payoff function that we would need
to choose in the derivatives market, and therefore motivates the estimation
of the statistical and risk-neutral densities p and q even for the non-Gaussian
case.
VGSA
Unlike VGG and many other pure-jump models, VGSA has a condition-
ally Gaussian arrival rate. This means that the volatility of the arrival-rate
λ should remain the same under the statistical and risk-neutral measures.
We therefore do have an approach that is analogous to the diffusion-based
models for VGSA.
VGSA vs. VG
In their original paper [182], Carr, Madan, and Chang found
comparable results for the VG model applied to the S&P 500 for the period
1992–1994. As previously discussed, the VG model has an integrated dens-
ity, and therefore the MLE could be performed without any filtering. The
statistical (historical) parameters are
(σ = 0.117200 θ = 0.0056 ν = 0.002)
And their risk-neutral parameters are
(σ = 0.1213 θ = −0.1436 ν = 0.1686)
Again we can see that the historical estimate for θ is close to zero, whereas
the risk-neutral one is significantly negative. This negative θ is what creates
the negative skewness observed in cross-sectional estimations.
We can try to reproduce the foregoing parameters with the VGSA model.
The resulting time-series parameter set is
(κ = 79.499687 η = 3.557702 λ = 0.000000)
(σ = 0.049656 θ = 0.006801 ν = 0.008660 µ = 0.030699)

216
INSIDE VOLATILITY ARBITRAGE
0.5
1
1.5
2
2.5
3
3.5
4
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
Simulated Arrival Rates
y
y-bis
FIGURE 3.20
Arrival Rates for Simulated SPX Prices Using  = (κ = 0.0000
η = 0.0000 λ = 0.000000 σ = 0.117200 θ = 0.0056ν = 0.002)
and
 = (κ =
79.499687, η = 3.557702λ = 0.000000σ = 0.049656θ = 0.006801, ν =
0.008660, µ = 0.030699). We can see that they are quite different.
Although the results seem to be very different, upon simulation we can see
that even if the resulting arrival rates and gamma variables are different, the
log stock prices are close. This can be seen in Figures 3.20, 3.21, and 3.22.
An alternative would be to use the EPF algorithm with the VGSA model
over the same period, in which case we would obtain
(κ = 190.409721 η = 3.459288 λ = 5.430759)
(σ = 0.050243 θ = 0.002366 ν = 0.007945 µ = 0.032576)
Once again the most unstable parameters are (κ η λ), or the ones corre-
sponding to the arrival rate. We have seen this many times; the estimation
of the parameters affecting the noise is less reliable. This is in agreement
with what we had observed in Chapter 2 and shows the limitations of these
inference tools.
Cross-Sectional vs. Time-Series VGSA
Applying the particle filtering algorithm
described in Chapter 2 to S&P 500, we find for 2001–2003 period the stati-
stical parameter set
(κ = 55.01778 η = 3.721583 λ = 8.666717
σ = 0.118637 θ = 0.060053 ν = 0.00103)

The Consistency Problem
217
0
0.01
0.02
0.03
0.04
0.05
0.06
0.07
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
Simulated Gamma Times
G
G-bis
FIGURE 3.21
Gamma Times for Simulated SPX Prices Using  = (κ = 0.0000 ,
η = 0.0000λ = 0.000000σ = 0.117200θ = 0.0056ν = 0.002)
and  = (κ =
79.499687 η
=
3.557702λ
=
0.000000σ
=
0.049656θ
=
0.006801ν
=
0.008660, µ = 0.030699).
µS = −0.2910
and for the 1995–1999 period
(κ = 1.151952 η = 5.418226 λ = 2.840461 σ = 0.055811
θ = 0.008626 ν = 0.006021)
µS = 0.249051
A typical cross-sectional risk-neutral parameter set
(κ = 2.72 η = 2.18 λ = 5.68 σ = 0.21 θ = −0.41 ν = 0.06)
As we can see, the implied skew and kurtosis are stronger for the cross-
sectional method compared with the statistical one. This is consistent with
results observed with other diffusion-based models.
We perform more recent parameter estimations corresponding to
06/10/1999–06/10/2003 and 09/10/1999–09/10/2003 (via PF based on 1000
particles) for S&P 500. The results are reported in Table 3.3. As we can see,
the algorithm for the estimation of the statistical parameters seems fairly
stable provided that the initial parameters are chosen sufficiently close to the
optimal ones.

218
INSIDE VOLATILITY ARBITRAGE
4.6
4.65
4.7
4.75
4.8
4.85
4.9
4.95
5
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
Simulated Log Stock Prices
lnS
lnS-bis
FIGURE 3.22
Log Stock Prices for Simulated SPX Prices Using  = (κ = 0.0000 ,
η = 0.0000λ = 0.000000σ = 0.117200θ = 0.0056ν = 0.002)
and  = (κ =
79.499687 η = 3.557702 λ = 0.000000 σ = 0.049656 θ = 0.006801 ν = 0.008660,
µ = 0.030699). Unlike arrival rates, the spot prices are hard to distinguish. This is
consistent with our previous observations.
TABLE 3.3
VGSA Statistical Parameters Estimated via PF. The stock drifts µS are
−0.009999 and −0.010000 respectively.
period
κ
η
λ
σ
θ
ν
990910-030910 5.131967 6.499669 4.360002 0.087000 −0.024862 0.002000
990610-030610 6.514068 6.500001 4.360000 0.085000 −0.025000 0.001800
The cross-sectional results could be computed in the same way as for
diffusion-based models. Quoting the results of Carr et al. [48], we have
Table 3.4. As shown, for some periods the risk-neutral implied λ is much
larger than the statistical one. This implies the possibility of a skewness trade,
as previously discussed.
It therefore seems that, depending on the period, the statistical and risk-
neutral parameters λ may or may not be consistent.
A WORD OF CAUTION
Accuracy issues of the inference tools aside, there are practical considerations
we need to bear in mind. We are applying basic models, such as Heston or

The Consistency Problem
219
TABLE 3.4
VGSA Risk-Neutral Arrival-Rate Parameters Estimated from
Carr et al. [48]
period
κ
η
λ
Mar 2000
4.08
15.99
16.52
Jun 2000
7.24
32.15
24.81
Sep 2000
0.25
0.00
3.76
Dec 2000
2.18
5.71
5.67
VGSA, to a complex and constantly changing market. The true dynamics of
the stock and option markets are unknown, and, even if the above models
approximate them fairly well, there is no guarantee that there will not be a
mutation in future dynamics. The best we can do is to use the information
hitherto available and hope that the future behavior of the assets is not too
different from the past.
Needless to say, as time passes by and new information becomes avail-
able, we need to update our models and parameter values. This could be
done within either a Bayesian or classical framework. Therefore, detecting
an inconsistency between the stock and option markets does not allow us
to make a riskless profit, because we simply do not know what the future
is reserving for us. Once again, the skewness transaction described in this
chapter is more similar to selling insurance than to an arbitrage.
FOREIGN EXCHANGE, FIXED INCOME, AND OTHER MARKETS
Foreign Exchange
It is important to note that everything discussed in this book can be applied
to time series from other asset classes. A popular asset class to which the
Heston and Bates models are often applied is the foreign exchange (FX).
Bates [27] applies his jump diffusion model to the USD/deutsche Mark (now
euro) exchange rate.
Calling Xt the FX rate process, for a Heston model, we would have
under the real-world measure P
d ln Xt =

µX −1
2vt

dt + √vtdBt
dvt = (ω −θvt)dt + ξ√vt

ρdBt +

1 −ρ2dZt


220
INSIDE VOLATILITY ARBITRAGE
TABLE 3.5
The Volatility and Correlation Parameters for the Cross-Sectional and
Time-Series Approaches.
Method
ξ
ρ
Cross-Sectional
0.45
−0.05
Time-Series
0.11
−0.09
with < dBt dZt >= 0. We could therefore apply any of the previously used
filters to the discretization of the above SDE and obtain the optimal param-
eters via MLE.
Under the risk-neutral measure Q, the FX drift is the difference between
the domestic and the foreign interest rates rD and rF . Therefore, we would
have
d ln Xt =

rD(t) −rF (t) −1
2vt

dt + √vtdB(r)
t
dvt = (ω(r) −θ(r)vt)dt + ξ√vt

ρdB(r)
t
+

1 −ρ2dZ(r)
t

with < dB(r)
t  dZ(r)
t
>= 0. Note that the usual Heston closed-form option-
pricing expression is valid for the FX process.
As previously discussed, according to the Girsanov theorem, (ξ ρ) should
be the same under the two measures. It is well known that compared with
equities, FX options markets have a much lower correlation ρ and have a
more symmetric smile. A skewness trade would therefore be more difficult
to carry out in this market, but a kurtosis trade taking advantage of the high
volatility-of-volatility ξ embedded in the options markets could be appropri-
ate (Table 3.5).
Similarly to what we did for the equities, we estimate the model par-
ameters from the three-month EUR/USD options cross-sectionally via a least-
squares method on January 2004. And we estimate the time-series par-
ameters (January 2000 to January 2005) via our second chapter filters. As
before, adding jumps to the Heston model will help lower the cross-sectional
volatility-of-volatility, but it remains insufficient to reconcile them.
Fixed Income
The Time Series
The same principles could be applied to the interest-rate
models with stochastic volatility. Using, for instance, a generalization of the

The Consistency Problem
221
extended-Vasicek [146] short-rate model14, we would have under P
drt = a[µ(t) −rt]dt + √vtdBt
dvt = (ω −θvt)dt + ξ√vt

ρdBt +

1 −ρ2dZt

with < dBt dZt >= 0. The difference between this first SDE and the corres-
ponding ones in FX or equities is that the short-rate process is not directly
observable. What is observable is the bond yield, which has a closed-form
expression as a function of rt. In an extended Vasicek model, for a given path
of vt the price of a forward starting zero-coupon bond is
P (t T ) = A(t T )e−B(tT )r(t)
with
B(t T ) = 1 −e−a(T −t)
a
ln A(t T ) = ln P (0 T )
P (0 t) −B(t T )∂ln P(0 t)
∂t
−1
2

B(t T )∂B(0 t)
∂t
2  t
0

1/∂B(0 u)
∂u
2
vudu
and the bond yield is
R(t T ) = −ln P (t T )
T −t
From the foregoing expressions we can fairly easily deduce that at a given
time t, the short rate simply becomes
r(t) = R(t t) = −∂ln P
∂t
(t t)
Therefore, we can observe the current short rate as the (negative) initial slope
of the yield curve, and we are back to the same framework as for equities
and FX processes.
The Cross Section
For the option pricing under Q we would have
drt = a(r) 
µ(r)(t) −rt

dt + √vtdB(r)
t
dvt = (ω(r) −θ(r)vt)dt + ξ√vt

ρdB(r)
t
+

1 −ρ2dZ(r)
t

14In what follows we consider the speed of mean reversion a fixed. One could
estimate it via a global calibration, for instance.

222
INSIDE VOLATILITY ARBITRAGE
80
90
100
110
120
130
140
0
200
400
600
800
1000
1200
1400
Days
Euro Index Time-Series 2000–2005
Euro Index
FIGURE 3.23
A Time Series of the Euro Index from January 2000 to January 2005.
with < dB(r)
t  dZ(r)
t
>= 0. Naturally because of the randomness of the volatil-
ity, we would lose the closed-form expressions for the options on bonds (or
caps or swaptions). However, we can still value them via a two-factor Monte
Carlo algorithm. Indeed, we have for an option with maturity U on a zero-
coupon bond with maturity T > U
c = E0

exp(−
 T
U
rtdt) −1
+
=
 +∞
0
 +∞
0

exp(−
 T
U
rtdt) −1
+
q(rU vU)drUdvU
where q(r v) represents the joint density of the short rate and its volatility.
Once again, the Girsanov theorem would require the same (ξ ρ) par-
ameters under the real-world and risk-neutral measures. A more negative
correlation in the cross-sectional options market would therefore favor a
skewness trade, and a higher volatility-of-volatility, a kurtosis trade.
One noticeable point is that, for a given level of option maturity U,
we can have many bond maturities. It is known that a swaption can be
modeled and priced as an option on a coupon bond.15 However, there may
be many swap tenors for the same option expiration, which introduces an
15See [146] for instance.

The Consistency Problem
223
extra dimension. But nothing stops us from using many tenors and option
maturities at once for a cross-sectional calibration.
The choice of the time-series period is still to be questioned. Do we
consider the period beginning at our cross-sectional date, or do we consider
a start date before this date? The latter would provide us with more data
points; however, these points would be historic. As we saw, we probably
would need the longer time series in order to have more reliable estimations.

References
[1] Ackerberg D. A. (2000) “Importance Sampling and the Method of Simulated
Moments” Department of Economics, Boston University and NBER.
[2] Aihara S., Bagchi A. (2000) “Estimation of Stochastic Volatility in the Hull-
White Model” Applied Mathematical Finance, 7.
[3] Aït-Sahalia Y. (2001) “Telling from Discrete Data Whether the Under-
lying Continuous-Time Model Is a Diffusion” Journal of Finance, Vol. 57,
No. 5.
[4] Aït-Sahalia Y. (2002) “Maximum Likelihood Estimation of Discretely Sam-
pled Diffusions: A Closed-Form Approximation Approach” Econometrica,
Vol. 70, No. 1.
[5] Aït-Sahalia Y. (2003) “Disentangling Volatility from Jumps” Working Paper,
Princeton University.
[6] Aït-Sahalia Y., Wang Y., Yared F. (2001) “Do Option Markets Correctly Price
the Probabilities of Movement of the Underlying Asset?” Journal of Econo-
metrics, 101.
[7] Alexander C. (1999) “A Primer on the Orthogonal GARCH Model” ISMA
Center, University of Reading.
[8] Alexander C. (2000) “Principles of Skew” RISK.
[9] Alexander C. (2001) “Market Models: A Guide to Financial Data Analysis”
John Wiley & Sons, Ltd.
[10] Alizadeh S., Brandt M. W., Diebold F. X. (2002) “Range-Based Estimation of
Stochastic Volatility Models” Journal of Finance, Vol. 57, No. 3.
[11] Amin K. I., Ng V. (1993) “Option Valuation with Systematic Stochastic
Volatility” Journal of Finance, Vol. 48, Issue 3.
[12] Andersen A. B. (2000) “Quantifying the Peso Problem Bias: A Switching
Regime Approach” Department of Finance, The Aarhus Schools of Business,
Denmark.
[13] Andersen L. B. G., Brotherton-Ratcliffe R. (1997) “The Equity Option Volatil-
ity Smile: An Implicit Finite Difference Approach” Journal of Computational
Finance, Vol. 1(2).
[14] Arulampalam S., Maskell S., Gordon N., Clapp T. (2002) “A Tutorial on Par-
ticle Filters for On-line Non-linear/ Non-Gaussian Bayesian Tracking” IEEE
Transactions on Signal Processing, Vol. 50. No. 2.
[15] Avellaneda M. (2002) “Empirical Aspects of Dispersion Trading in U.S. Equity
Markets” Slides from Presentation at Le Petit Dejeuner de la Finance, Paris.
[16] Avellaneda M., Friedman C., Holmes R., Samperi D. (1997) “Calibrating
Volatility Surfaces via Relative-Entropy Minimization” Applied Mathematical
Finance, 4(1).
224

References
225
[17] Avellaneda M., Levy A., Paras A. (1995) “Pricing and Hedging Deriva-
tive Securities in Markets with Uncertain Volatilities” Applied Mathematical
Finance, 2.
[18] Bachelier L. (1900) “Théorie de la Spéculation” Annales Scientifiques de
l’École Normale Supérieure, Troisième Série, 17.
[19] Bagchi A. (2004) “Volatility Estimation under Heston’s Framework” Super-
visor, University of Twente Working Paper.
[20] Bakshi G., Cao C., Chen Z. (1997) “Empirical Performance of Alternative
Option Pricing Models” Journal of Finance, Vol. 52, Issue 5.
[21] Balland P. (2002) “Deterministic Implied Volatility Models” Quantitative
Finance, Vol. 2.
[22] Barle S., Cakici N. (1995) “Growing a Smiling Tree” RISK Magazine, Vol. 8,
No. 10.
[23] Barndorff-Nielsen O. E., Nicolato E., Shephard N. (2002) “Some Recent
Developments in Stochastic Volatility Modeling” Quantitative Finance, 2.
[24] Barndorff-Nielsen O. E., Shephard N. (2001) “Non-Gaussian Ornstein-
Uhlenbeck-based Models and Some of Their Uses in Financial Economics”
Royal Statistical Society, 63, Part 2.
[25] Barndorff-Nielsen O. E., Shephard N. (2002) “Econometric Analysis of Real-
ized Volatility and Its Use in Estimating Stochastic Volatility Models” Journal
of the Royal Statistical Society, Series B, Vol. 64.
[26] Bates D. S. (1991) “The Crash of 87: Was It Expected? The Evidence from
Options Markets” Journal of Finance, Vol. 46, Issue 3.
[27] Bates D. S. (1996) “Jumps and Stochastic Volatility: Exchange Rate Processes
Implicit in Deutsche Mark Options” Review of Financial Studies, 9.
[28] Bates D. S. (1998) “Pricing Options Under Jump Diffusion Processes” The
Wharton School, University of Pennsylvania.
[29] Bates D. S. (1998) “Hedging the Smirk” University of Iowa & NBER.
[30] Bates D. S. (2000) “Post-87 Crash Fears in the S&P 500 Futures Option Mar-
ket” Journal of Econometrics, 94.
[31] Bates D. S. (2002) “Maximum Likelihood Estimation of Latent Affine Pro-
cesses” University of Iowa & NBER.
[32] Bates D. S. (2002) “Empirical Option Pricing: A Retrospection” Forthcoming
in Journal of Econometrics.
[33] Bensoussan A., Crouhy M. and Galai D. (1995) “Stochastic Equity Volatility
Related to the Leverage Effect I: Equity Volatility Behavior” Applied Mathe-
matical Finance, 1.
[34] Bernardo J., Smith A. F. M. (2001) “Bayesian Theory” John Wiley and Sons.
[35] Bertsekas D. P. (2000) “Dynamic Programming and Optimal Control” (2nd
Edition, Vols. 1 and 2), Athena Scientific.
[36] Blacher G. (1998) “Local Volatility” RISK Conference Presentation.
[37] Black F. (1976) “Studies in Stock Price Volatility Changes” Proceedings of
the 1976 Meeting of the Business and Economics Statistics Section, American
Statistical Association.
[38] Black F., Scholes M. (1973) “The Pricing of Options and Corporate Liabilities”
Journal of Political Economy, 81.

226
REFERENCES
[39] Blinnikov S., Moessner R. (1998) “Expansion for Nearly Gaussian Distribu-
tions” Astronomy and Astrophysics Supplement Series, 130.
[40] Bollerslev T. (1986) “Generalized Autoregressive Conditional Heteroskedas-
ticity” Journal of Econometrics, 31.
[41] Bouchaud J. P., Perelló J., Masoliver J. (2003) “Multiple Time-Scales in Volatil-
ity and Leverage Correlations: A Stochastic Volatility Model” Working Paper,
Centre d’Etudes de Saclay and Universitat de Barcelona.
[42] Bouchouev I. (1998) “Derivatives Valuation for General Diffusion Processes”
The International Association of Financial Engineers (IAFE) Conferences.
[43] Brandt M. W., Santa-Clara P. (2002) “Simulated Likelihood Estimation of
Diffusions with an Application to Exchange Rate Dynamics in Incomplete
Markets” Journal of Financial Economics, 63.
[44] Breeden D. T., Litzenberger R. H. (1978) “Prices of State-Contingent Claims
Implicit in Option Prices” Journal of Business, Vol. 51, No. 4.
[45] Brockhaus O., Long D. (2000) “Volatility Swaps Made Simple” RISK, January
2000.
[46] Buraschi A., Jackwerth A. C. (2001) “The Price of a Smile: Hedging and
Spanning in Option Markets” Review of Financial Studies, 14.
[47] Carr P., Geman H., Madan D., Yor M. (2002) “The Fine Structure of Asset
Returns” Journal of Business, Vol. 75, No. 2.
[48] Carr P., Geman H., Madan D., Yor M. (2003) “Stochastic Volatility for Lévy
Processes” Mathematical Finance, Vol. 13, No. 3.
[49] Carr P., Lewis K. (2002) “Corridor Variance Swaps” Research Papers,
Courant Institute of Mathematical Sciences, New York University.
[50] Carr P., Madan D. (1998) “Toward a Theory of Volatility Trading” Research
Papers, Courant Institute of Mathematical Sciences, New York University.
[51] Carr P., Madan D. (1998) “Option Valuation Using the Fast Fourier Trans-
form” Morgan Stanley and University of Maryland.
[52] Carr P., Madan D. (2001) “Optimal Positioning in Derivative Securities”
Quantitative Finance, Vol. 1.
[53] Carr P., Madan D. (2001) “Optimal Investment in Derivative Securities”
Finance and Stochastics, Vol. 5.
[54] Carr P., Wu L. (2003) “Time-Changed Lévy Processes and Option Pricing”
Journal of Financial Economics.
[55] Casella G., George E. I. (1992) “Explaining the Gibbs Sampler” The American
Statistician, Vol. 46, No. 3.
[56] Chernov M., Ghysels E. (2000) “A Study Toward a Unified Approach to the
Joint Estimation of Objective and Risk-Neutral Measures for the Purpose of
Option Valuation” Journal of Financial Economics, 56.
[57] Chib S., Nadari F., Shephard N. (1998) “Markov Chain Monte-Carlo
Methods for Generalized Stochastic Volatility Models” Washington Univer-
sity and The University of Oxford.
[58] Chib S., Greenberg E. (1995) “Understanding the Metropolis-Hastings Algo-
rithm” The American Statistician, Vol. 49, No. 4.
[59] Chourdakis K. M. (2001) “Volatility Persistence, Regime Switches and Option
Pricing” Department of Economics, University of London.

References
227
[60] Chriss N. A. (1997) “Black Scholes and Beyond: Option Pricing Models”
Irwin/McGraw Hill.
[61] Corradi V. (2000) “Reconsidering the Continuous Time Limit of the
GARCH(1,1) Process” Journal of Econometrics, 96.
[62] Corrado C. J., Su T. (1997) “Implied Volatility Skews and Stock Index Skew-
ness and Kurtosis Implied by S&P 500 Index Option Prices” University of
Missouri at Columbia, University of Miami at Coral-Gables.
[63] Corrado C. J., Su T. (1997) “Implied Volatility Skews and Stock Return Skew-
ness and Kurtosis Implied by Stock Option Prices” The European Journal of
Finance, 3.
[64] Cox J. C. (1996) “The Constant Elasticity of Variance Option Pricing Model”
Journal of Portfolio Management, Special Issue.
[65] Cox J. C., Ross S. (1976) “The Valuation of Options for Alternative Stochastic
Processes” Journal of Financial Economics, 3.
[66] Cox J. C., Ross S., Rubinstein M. (1979) “Option Pricing: A Simplified Ap-
proach” Journal of Financial Economics, 7.
[67] Cox J. C., Rubinstein M. (1985) “Options Markets” Prentice Hall.
[68] Crosbie P. J. (1999) “Modeling Default Risk” KMV Working Papers.
[69] Das S. R., Sundaram R. K. (1997) “Taming the Skew: Higher-Order Moments
in Modeling Asset-Price Processes in Finance” National Bureau of Economic
Research.
[70] DemeterfiK., Derman E., Kamal M., Zou J. (1999) “More than You Ever
Wanted to Know About Volatility Swaps” Goldman Sachs Quantitative Strat-
egy Papers.
[71] Dempster M. A. H., Gotsis G. Ch. (1998) “On the Martingale Problem for
Jumping Diffusions” University of Cambridge and Hellenic Capital Market
Commission.
[72] Deng S. (2000) “Stochastic Models for Energy Commodity Prices and Their
Applications: Mean-Reversion with Jumps and Spikes” Industrial and Sys-
tems Engineering, Georgia Institute of Technology.
[73] Derman E. (1999) “Regimes of Volatility: Some Observations on the Varia-
tions of S&P 500 Implied Volatilities” Goldman Sachs Quantitative Strategy
Papers.
[74] Derman E., Kani I. (1994) “Riding on a Smile” RISK Magazine, 7.
[75] Derman E., Kani I. (1994) “The Volatility Smile and Its Implied Tree” Gold-
man Sachs Quantitative Strategy Papers.
[76] Derman E., Kani I. (1998) “Stochastic Implied Trees: Arbitrage Pricing with
Stochastic Term and Strike Structure of Volatility” International Journal of
Theoretical and Applied Finance, 1.
[77] Derman E., Kani I., Chriss N. (1996) “Implied Trinomial Trees of the Volatility
Smile” Goldman Sachs Quantitative Strategy Papers.
[78] Derman E., Kani I., Zou J. (1995) “The Local Volatility Surface: Unlocking
the Information in Index Option Prices” Goldman Sachs Quantitative Strategy
Papers.
[79] Doucet A., De Freitas N., Gordon N. (2001) “Sequential Monte-Carlo
Methods in Practice” Springer-Verlag.

228
REFERENCES
[80] Doucet A., Gordon N., Krishnamurthy V. (2001) “Particle Filters for State
Estimation of Jump Markov Linear Systems” IEEE Transactions on Signal
Processing, Vol. 49, No. 3.
[81] Dragulescu A. A., Yakovenko V. M. (2002) “Probability Distribution of Re-
turns in the Heston Model with Stochastic Volatility” Department of Physics,
University of Maryland.
[82] Duan J. C. (1995) “The GARCH Option Pricing Model” Mathematical
Finance, 5.
[83] Duan J. C. (1996) “Cracking the Smile” RISK Magazine, 9.
[84] Duan J. C. (1996) “A Unified Theory of Option Pricing Under Stochastic
Volatility: From GARCH to Diffusion” Hong Kong University of Science and
Technology.
[85] Duan J. C. (1997) “Augmented GARCH(p,q) Process and Its Diffusion Limit”
Journal of Econometrics, 79.
[86] Duan J. C. (2001) “Risk Premium and Pricing of Derivatives in Complete
Markets” Rotman School of Management, University of Toronto.
[87] Dufresne Daniel (2001) “The Integrated Square-Root Process” Center for
Actuarial Studies, The University of Melbourne.
[88] Dumas B., Fleming J., Whaley R. E. (1998) “Implied Volatility Functions:
Empirical Tests” Journal of Finance, Vol. 53, Issue 6.
[89] Dupire B. (1994) “Pricing with a Smile” RISK Magazine, 7.
[90] Durrett R. (1996) “Stochastic Calculus: A Practical Introduction” CRC Press,
Boca Raton, Florida.
[91] El-Karoui N., Quenez M. C. (1995) “Dynamic Programming and Pricing of
Contingent Claims in Incomplete Markets” SIAM Journal of Control and
Optimization, 33(1).
[92] Elerian O., Chib S., Shephard N. (2001) “Likelihood Inference for Discretely
Observed Nonlinear Diffusions” Econometrica.
[93] Elliott R. J., Lahaie C. H., Madan D. (1997) “Filtering Derivative Secur-
ity Valuations from Market Prices” University of Alberta, University of
Maryland.
[94] Engle R. F. (1982) “Autoregressive Conditional Heteroskedasticity with Esti-
mates of the Variance of United Kingdom Inflation” Econometrica, Vol. 50,
No. 4.
[95] Engle R. F., Ishida I. (2002) “The Square-Root, the Affine, and the CEV
GARCH Models” Working Paper, New York University and University of
California, San Diego.
[96] Engle R. F., Mezrich J. (1995) “Grappling with GARCH” RISK Magazine, 9.
[97] Engle R. F., Ng V. (1993) “Measuring and Testing the Impact of News on
Volatility” Journal of Finance, Vol. 48, Issue 5.
[98] Eraker B., Johannes M., Polson N. (2003) “The Impact of Jumps in Equity
Index Volatility and Returns” Journal of Finance, 58.
[99] Fama E. (1965) “The Behavior of Stock Market Prices” Journal of
Business, 38.
[100] Fan J., Yao Q. (2003) “Nonlinear Time Series: Nonparametric and Parametric
Methods” Springer.

References
229
[101] Fleming J., Kirby C. (2003) “A Closer Look at the Relation Between GARCH
and Stochastic Autoregressive Volatility” Journal of Financial Econometrics,
Vol. 1, December.
[102] Follmer H., Sondermann D. (1986) “Hedging of Non-Redundant Contingent-
Claims” Contributions to Mathematical Economics, North-Holland.
[103] Forbes C. S., Martin G. M., Wright J. (2002) “Bayesian Estimation of a
Stochastic Volatility Model Using Option and Spot Prices” Department of
Econometrics and Business Statistics, Monash University, Australia.
[104] Fouque J. P., Papanicolaou G., Sircar K. (2000) “Derivatives in Financial
Markets with Stochastic Volatility” Cambridge University Press.
[105] Fouque J. P., Papanicolaou G., Sircar K. (2000) “Mean Reverting Stochastic
Volatility” International Journal of Theoretical and Applied Finance, 3(1).
[106] Fouque J. P., Tullie T. A. (2002) “Variance Reduction for Monte-Carlo
Simulation in a Stochastic Volatility Environment” Quantitative Finance, 2.
[107] Frey R. (1997) “Derivative Asset Analysis in Models with Level-Dependent
and Stochastic Volatility” Department of Mathematics, ETH Zurich.
[108] Fridman M., Harris L. (1998) “A Maximum Likelihood Approach for Non-
Gaussian Stochastic Volatility Models” Journal of Business and Economic
Statistics.
[109] Gallant A. R., Tauchen G. (2001) “Efficient Method of Moments” University
of North Carolina and Duke University.
[110] Galli A. (2000) “Variograms and Cross-Variograms” Ecole des Mines de
Paris, Working Paper.
[111] Galli A., Lautier D. (2001) “Un Modèle de Structure par Terme des
Prix des Matières Premières avec Comportement Asymétrique du Ren-
dement d’Opportunité” École des Mines de Paris & CEREG, Université
Paris IX.
[112] Garcia R., Ghyseles E., Renault E. (2002) “The Econometrics of Option
Pricing” Université de Montreal and University of North Carolina.
[113] Gatheral J. G. (2001) “Stochastic Volatility and Local Volatility” Courant
Institute of Mathematical Sciences, New York University.
[114] Gatheral J. G. (2001) “Fitting the Volatility Skew” Courant Institute of
Mathematical Sciences, New York University.
[115] Gatheral J. G. (2001) “Asymptotics and Dynamics of the Volatility Skew”
Courant Institute of Mathematical Sciences, New York University.
[116] Gatheral J. G. (2001) “Volatility and Variance Swaps” Courant Institute of
Mathematical Sciences, New York University.
[117] Geman H., El-Karoui N., Rochet J. C. (1995) “Changes of Numeraire,
Changes of Probability Measure and Option Pricing” Journal of Applied
Probability, 32(2).
[118] Geman H., Madan D., Yor M. (2001) “Stochastic Volatility, Jumps and
Hidden Time Changes” Finance and Stochastics.
[119] Geske R. (1979) “The Valuation of Compound Options” Journal of Financial
Economics, 7.
[120] Gilks W. R., Richardson S., Spiegelhalter D. J. (1995) “Markov Chain Monte
Carlo in Practice” Chapman & Hall/ CRC.

230
REFERENCES
[121] Gondzio J., Kouwenberg R., Vorst T. (2003) “Hedging Options Under
Transaction Costs and Stochastic Volatility” Journal of Economic Dynamics
and Control, 27.
[122] Gordon N. J., Salmond D. J. Smith A. F. M. (1993) “Novel Approach to
Nonlinear/Non-Gaussian Bayesian State Estimation” IEE Proceedings-F,
Vol. 140, No. 2.
[123] Gourieroux C., A. Monfort, Renault E. (1993) “Indirect Inference” Journal
of Applied Econometrics, 8.
[124] Gourieroux C.,
Jasiak J. (2001) “Financial Econometrics” Princeton
University Press.
[125] Grabbe J. O. (1983) “The Pricing of Put and Call Options on Foreign
Exchange” Journal of International Money and Finance, December.
[126] Hamilton J. D. (1989) “A New Approach to the Econometric Analysis of
Non-stationary Time Series and the Business Cycle” Econometrica, Vol. 57,
No. 2.
[127] Hamilton J. D. (1994) “Time Series Analysis” Princeton University Press.
[128] Härdle W., Kleinow T., Stahl G. (2002) “Applied Quantitative Finance”
Springer-Verlag.
[129] Harvey A. C. (1989) “Forecasting, Structural Time Series Models, and the
Kalman Filter” Cambridge University Press.
[130] Harvey A. C., Ruiz E., Shephard Neil (1994) “Multivariate Stochastic
Variance Models” Review of Economic Studies, Vol. 61, Issue 2.
[131] Harvey C. R., Whaley R. E. (1991) “S&P 100 Index Option Volatility”
Journal of Finance, Vol. 46, Issue 4.
[132] Haug E. G. (1997) “The Complete Guide to Option Pricing Formulas”
McGraw-Hill, New York.
[133] Haykin S. (2001) “Kalman Filtering and Neural Networks” Wiley Inter-
Science.
[134] Heston S. (1993) “A Closed-Form Solution for Options with Stochastic
Volatility with Applications to Bond and Currency Options” Review of
Financial Studies, 6.
[135] Heston S. (2000) “Derivatives on Volatility: Some Simple Solutions Based on
Observables” Federal Reserve Bank of Atlanta, Working Paper.
[136] Heston S., Christoffersen P., Jacobs K. (2004) “Option Valuation with
Conditional Skewness” University of Maryland and McGill University.
[137] Heston S., Nandi S. (1997) “A Closed Form GARCH Option Pricing Model”
Federal Reserve Bank of Atlanta, Working Paper 97-9.
[138] Hipp C., Taksar M. (2000) “Hedging in Incomplete Markets and Optimal
Control” University of Karlsruhe and SUNY at Stony-Brook.
[139] Hirsa A., Javaheri A. (2003) “A Particle Filtering Algorithm for the VGSA
Model” Working Paper, Morgan Stanley and RBC Capital Markets.
[140] Hobson D. G. (1996) “Stochastic Volatility” School of Mathematical Sciences,
University of Bath.
[141] Hobson D. G., Rogers L. C. G. (1998) “Complete Models with Stochastic
Volatility” Mathematical Finance, 8.

References
231
[142] Honoré P. (1998) “Pitfalls in Estimating Jump-Diffusion Models” Department
of Finance, The Aarhus School of Business, Denmark.
[143] Howison S. D., Rafailidis A., Rasmussen H. O. (2000) “A Note on the
Pricing and Hedging of Volatility Derivatives” The University of Oxford,
Kings College London.
[144] Hughston L. P. (2004) “International Models for Interest Rates and Foreign
Exchange: A General Framework for the Unification of Interest Rate Dynam-
ics and Stochastic Volatility” Global Derivatives and Risk Management, May
2004.
[145] Hughston L. P., Rafailidis A. (2004) “A Chaotic Approach to Interest Rate
Modeling” Finance and Stochastic.
[146] Hull J. (1999) “Options, Futures, and Other Derivative Securities” Englewood
Cliffs, 4th Edition.
[147] Hull J., Suo W. (2002) “A Methodology for Assessing Model Risk and its
Application to the Implied Volatility Function Model”Journal of Financial
and Quantitative Analysis.
[148] Hull J., Suo W. (2002) “Modeling the Volatility Surface” University of
Toronto and Queen’s University.
[149] Hull J., White A. (1987) “The Pricing of Options on Assets with Stochastic
Volatility” Journal of Finance, Vol. 42, Issue 2.
[150] Hull J., White A. (1988) “An Analysis of the Bias in Option Pricing Caused
by a Stochastic Volatility” Advances in Futures and Options Research, 3.
[151] Ito K., Xiong K. (1999) “Gaussian Filters for Nonlinear Filtering Prob-
lems” Center for Research in Scientific Computation, North Carolina State
University.
[152] Jackel P. (2002) “Monte-Carlo Methods in Finance” Wiley Series in Finance.
[153] Jackson N., Suli E., Howison S. (1998) “Computation of Deterministic
Volatility Surfaces” Journal of Computational Finance Vol. 2(2).
[154] Jackwerth J. C. (2000) “Option-Implied Risk-Neutral Distributions and
Implied Binomial Trees: A Literature Review” Journal of Derivatives, 7.
[155] Jackwerth J. C., Rubinstein M. (1996) “Recovering Probability Distributions
from Option Prices” Journal of Finance, Vol. 51, Issue 5.
[156] Jacquier E., Polson N. G., Rossi P. E. (1994) “Bayesian Analysis of Stochastic
Volatility Models” Journal of Business and Economic Statistics, Vol. 12,
No, 4.
[157] Jarrow R., Rudd A. (1982) “Approximate Option Valuation for Arbitrary
Stochastic Processes” Journal of Financial Economics, 10.
[158] Javaheri A., Wilmott P., Haug E. G. (2002) “GARCH and Volatility Swaps”
Wilmott, January 2002.
[159] Javaheri A., Lautier D., Galli A. (2003) “Filtering in Finance” Wilmott, Issue 5.
[160] Javaheri A. (2004) “Inference and Stochastic Volatility” Wilmott, Issue 11.
[161] Jex M., Henderson R., Wang D. (1999) “Pricing Exotics Under the Smile”
RISK Magazine.
[162] Jiang G. J., Van der Sluis P. J. (2000) “Index Option Pricing with Stochastic
Volatility and Stochastic Interest Rates” Center for Economic Research.

232
REFERENCES
[163] Johannes M., Polson N. (2002) “MCMC Methods for Financial Econo-
metrics” The Handbook of Financial Econometrics.
[164] Johannes M., Polson N., Stroud J. (2002) “Nonlinear Filtering of Stochastic
Differential Equations with Jumps” Working Paper, Columbia University,
University of Chicago and University of Pennsylvania.
[165] Jones C. S. (2001) “The Dynamics of Stochastic Volatility: Evidence from
Underlying and Options Markets” Simon School of Business, University of
Rochester.
[166] Julier S. J., Uhlmann J. K. (1997) “A New Extension of the Kalman Filter
to Nonlinear Systems” The University of Oxford, The Robotics Research
Group.
[167] Karatzas I., Shreve S. (1991) “Brownian Motion and Stochastic Calculus”
Springer-Verlag, 2nd Edition.
[168] Kennedy P. (1998) “A Guide to Econometrics” MIT Press, 4th Edition.
[169] Kim S., Shephard N., Chib S. (1998) “Stochastic Volatility:
Likelihood
Inference and Comparison with ARCH Models” Review of Economic
Studies, Vol. 65.
[170] Kitagawa G. (1987) “Non-Gaussian State Space Modeling of Non-Stationary
Time Series” Journal of American Statistical Association, 82.
[171] Kitagawa G. (1996) “Monte-Carlo Filter and Smoother for Non-Gaussian
Nonlinear Sate Space Models” Journal of Computational and Graphical
Statistics, Vol. 5, No. 1.
[172] Kou S. (2000) “A Jump Diffusion Model for Option Pricing with Three
Properties: Leptokurtic Feature, Volatility Smile, and Analytical Tractability”
Econometric Society World Congress 2000 Contributed Papers.
[173] Kushner H. J. (1967) “Approximations to Optimal Nonlinear Filters” IEEE
Transactions on Automatic Control, Vol. 12.
[174] Kushner H. J., Budhiraja A. S. (2000) “A Nonlinear Filtering Algorithm Based
on an Approximation of the Conditional Distribution” IEEE Transactions
on Automatic Control, Vol. 45. No. 3.
[175] Lagnado R., Osher S. (1997) “A Technique for Calibrating Derivative
Security Pricing Model: Numerical Solution of an Inverse Problem” Journal
of Computational Finance, Vol. 1(1).
[176] Lee D. S., Chia N. K. K (2002) “A Particle Algorithm for Sequential Bayesian
Parameter Estimation and Model Selection” IEEE Transactions on Signal
Processing, Vol. 50, No. 2.
[177] Lewis A. L. (2000) “Option Valuation under Stochastic Volatility” Finance
Press.
[178] Lewis A. L. (2001) “A Simple Option Formula for General Jump-Diffusion
and Other Exponential Levy Processes” OptionCity.net Publications.
[179] Lewis A. L. (2002) “The Mixing Approach to Stochastic Volatility and Jump
Models” Wilmott, March 2002.
[180] Lewis A. L. (2002) “Fear of Jumps” Wilmott, Issue 2.
[181] Li Y. (2000) “A New Algorithm for Constructing Implied Binomial Trees:
Does the Implied Model Fit Any Volatility Smile?” Journal of Computational
Finance, Vol. 4(2).

References
233
[182] Madan D., Carr P., Chang E. C. (1998) “The Variance-Gamma Process and
Option Pricing” European Finance Review, Vol. 2, No. 1.
[183] Maes K. (2001) “Panel Data Estimating Continuous-Time Arbitrage-
Free Affine Term-Structure Models with the Kalman Filter” International
Economics, Leuven University.
[184] Maheu J. M., McCurdy T. H. (2003) “News Arrival, Jump Dynamics, and
Volatility Components for Individual Stock Returns” University of Toronto.
[185] Markowiz H. M. (1990) “Mean-Variance Analysis in Portfolio Choice and
Capital Markets” Basil Blackwell.
[186] Matacz A. (1997) “Financial Modeling and Option Theory with the Truncated
Levy Process” School of Mathematics and Statistics, University of Sidney.
[187] Matytsin
A.
(1999)
“Modeling
Volatility
and
Volatility
Derivatives”
Columbia Practitioners Conference on the Mathematics of Finance.
[188] Merton R. C. (1973) “The Theory of Rational Option Pricing” Bell Journal
of Economics and Management, 7.
[189] Merton R. C. (1974) “On the Pricing of Corporate Debt: The Risk Structure
of Interest Rates” Journal of Finance, Vol. 29, Issue 2.
[190] Merton R. C. (1976) “Option Pricing When the Underlying Stock Returns
Are Discontinuous” Journal of Financial Economics.
[191] Meyer R., Fournier D. A., Berg A. (2003) “Stochastic Volatility: Bayesian
Computation Using Automatic Differentiation and the Extended Kalman
Filter” Econometrics Journal, Vol. 6.
[192] Muzzioli S., Torricelli C. (2001) “Implied Trees in Illiquid Markets:
A
Choquet Pricing Approach” Universita degli Studi di Modena e Reggio
Emilia, Dipartimento di Economia Politica.
[193] Neftci S. N. (1996) “An Introduction to the Mathematics of Financial
Derivatives” Academic Press, San Diego, CA.
[194] Nelson D. B. (1990) “ARCH Models as Diffusion Approximations” Journal
of Econometrics, 45.
[195] Nelson D. B. (1990) “Conditional Heteroskedasticity and Asset Returns: A
New Approach” Econometrica, 59.
[196] Nelson D. B., Foster D. P. (1994) “Asymptotic Filtering Theory for Univariate
ARCH Models” Econometrica, Vol. 62, Issue 1.
[197] Oksendal B. (1998) “Stochastic Differential Equations: An Introduction with
Applications” Springer-Verlag New York, 5th Edition.
[198] Pan G. (2001) “Equity to Credit Pricing” RISK November 2001.
[199] Pan J. (2002) “The Jump Risk-Primia Implicit in Options: Evidence from an
Integrated Time-Series Study” Journal of Financial Economics, 63.
[200] Parkinson M. (1980) “The Extreme Value Method for Estimating the
Variance of the Rate of Return” Journal of Business, 53.
[201] Pedersen A. R. (1995) “A New Approach to Maximum Likelihood Estima-
tion for Stochastic Differential Equations Based on Discrete Observations”
Scandinavian Journal of Statistics, 22.
[202] Pham H. (2001) “Smooth Solutions to Optimal Investment Models with
Stochastic Volatilities and Portfolio Constraints” CNRS and Université
Paris 7.

234
REFERENCES
[203] Pitt M. K., Shephard N. (1999) “Filtering via Simulation: Auxiliary Particle
Filters” Journal of the American Statistical Association, 94.
[204] Press W. H., Teukolsky S. A., Vetterling W. T., Flannery B. P. (1997) “Numer-
ical Recipes in C: The Art of Scientific Computing” Cambridge University
Press, 2nd Edition.
[205] Reif K., Gunther S., Yaz A. (1999) “Stochastic Stability of the Discrete-Time
Extended Kalman Filter” IEEE Transactions on Automatic Control.
[206] Renault E., Touzi N. (1996) “Option Hedging and Implied Volatilities in a
Stochastic Volatility Model” Mathematical Finance, 6.
[207] Ribiero C., Webber N. (2002) “Valuing Path-Dependent Options in the
Variance-Gamma Model by Monte-Carlo with a Gamma Bridge” Working
Paper, University of Warwick and City University of London.
[208] Ritchken P., Trevor R. (1997) “Pricing Options under Generalized GARCH
and Stochastic Volatility Processes” CMBF Papers, Macquarie University, 19.
[209] Romano M., Touzi N. (1997) “Contingent Claims and Market Completeness
in a Stochastic Volatility Model” Mathematical Finance, 7.
[210] Rubinstein M. (1983) “Displaced Diffusion Option Pricing” Journal of
Finance, Vol. 38, Issue 1.
[211] Samuelson P. A. (1965) “Rational Theory of Warrant Pricing” Industrial
Management Review, 6, 2.
[212] Sandmann G., Koopman S. J. (1998) “Estimation of Stochastic Volatility
Models via Monte-Carlo Maximum Likelihood” Journal of Econometrics, 87.
[213] Schonbucher P. J. (1998) “A Market Model for Stochastic Implied Volatility”
Department of Statistics, Bonn University.
[214] Scott L. O. (1987) “Option Pricing when the Variance Changes Randomly:
Theory, Estimation, and Application” Journal of Financial and Quantitative
Analysis, Dec.
[215] Scott L. O. (1997) “Pricing Stock Options in a Jump-Diffusion Model with
Stochastic Volatility and Interest Rates: Applications of Fourier Inversion
Methods” Mathematical Finance, 7.
[216] Shimko D. (1993) “Bounds on Probability” RISK, 6.
[217] Shimko D., Tejima N., Van Deventer D. R. (1993) “The Pricing of Risky Debt
when Interest Rates are Stochastic” Journal of Fixed Income, September 1993.
[218] Shreve S., Chalasani P., Jha S. (1997) “Stochastic Calculus and Finance”
Carnegie Mellon University.
[219] Silva A. C., Yakovenko V. M. (2002) “Comparison Between the Probability
Distribution of Returns in the Heston Model and Empirical Data for Stock
Indices” Department of Physics, University of Maryland.
[220] Sin C. A. (1998) “Complications with Stochastic Volatility Models” Advances
in Applied Probability, 30.
[221] Smith A. F. M., Gelfand A. E. (1992) “Bayesian Statistics Without Tears: A
Sampling-Resampling Perspective” The American Statistician, Vol. 46, No. 2.
[222] Srivastava A., Grenander U., Jensen G. R., Miller M. I. (2002) “Jump-
Diffusion Markov Processes on Orthogonal Groups for Object Recognition”
Journal of Statistical Planning and Inference, Special Issue.

References
235
[223] Stein E. M., Stein J. (1991) “Stock Price Distributions with Stochastic
Volatility: An Analytic Approach” Review of Financial Studies, 4.
[224] Storvik G. (2002) “Particle Filters in State Space Models with Presence of
Unknown Static Parameters” IEEE Transactions on Signal Processing, 50.
[225] Taleb N. (1996) “Dynamic Hedging: Managing Vanilla and Exotic Options”
John Wiley & Sons, Ltd.
[226] Tavella D., Klopfer W. (2001) “Implying Local Volatility” Wilmott, August
2001.
[227] Tavella D., Randall C. (2000) “Pricing Financial Instruments: The Finite
Difference Method” John Wiley & Sons, Ltd.
[228] Toft K. B., Prucyk B. (1997) “Options on Leveraged Equity: Theory and
Empirical Tests” Journal of Finance Vol. 52, Issue 3.
[229] Van der Merwe R., Doucet A., de Freitas N., Wan E. (2000) “The Unscented
Particle Filter” Oregon Graduate Institute, Cambridge University, and UC
Berkeley.
[230] Varadhan S. R. S. (2000) “Probability Theory” Courant Institute of
Mathematical Sciences, New York University.
[231] Wan E. A., Van der Merwe R. (2000) “The Unscented Kalman Filter for
Nonlinear Estimation” Oregon Graduate Institute of Science and Technology.
[232] Wan E. A., Van der Merwe R., Nelson A. (2000) “Dual Estimation and
the Unscented Transformation” Oregon Graduate Institute of Science and
Technology.
[233] Welch G., Bishop G. (2002) “An Introduction to the Kalman Filter” Depart-
ment of Computer Science, University of North Carolina at Chapel Hill.
[234] Wells C. (1996) “The Kalman Filter in Finance (Advanced Studies in The-
oretical and Applied Econometrics), Vol. 32” Kluwer Academic Publishers.
[235] Whitt W. (2001) “Stochastic Process Limits: An Introduction to Stochastic
Process Limits and Their Application to Queues” AT&T Labs Research,
Springer.
[236] Wiggins J. B. (1987) “Option Values under Stochastic Volatility” Journal of
Financial Economics, 19.
[237] Wilmott P. (2000) “Paul Wilmott on Quantitative Finance” John Wiley &
Sons, Ltd.
[238] Wilmott P., Dewynne J., Howison S. (1993) “Option Pricing: Mathematical
Pricing and Computations” Oxford Financial Press.
[239] Wilmott P., Rasmussen H. O. (2002) “Asymptotic Analysis of Stochastic
Volatility Models” Wilmott Associates.
[240] Zellner A. (2000) “Bayesian and Non-Bayesian Approaches to Scientific Mod-
eling and Inference in Economics and Econometrics” University of Chicago.
[241] Zhang L., Mykland P. A., Aït-Sahalia Y. (2003) “A Tale of Two Time-Scales:
Determining Integrated Volatility with Noisy High-Frequency Data” Working
Paper. Carnegie Melon University, University of Chicago, and Princeton
University.
[242] Zhou C. (1997) “A Jump-Diffusion Approach to Modeling Credit Risk and
Valuing Defaultable Securities” Federal Reserve Board, Washington, DC.

Index
3/2 models, 122, 188
Ackerberg, D.A., 224
Aihara, S., 224
Ait-Sahalia, Y., 159, 187–189,
198, 200, 224, 235
Alexander, C., 224
Alizadeh, S., 224
Amin, K.I., 224
Andersen, A.B., 224
Andersen, L.B., 224
Arbitrage opportunity, 214
Arrival rate, 171, 182
Arrow-Debreu prices, 17
Arulampalam, S., 224
Asset term, elimination, 13
Augmented state, 76
vector, 63
Auto-correlation, usage, 181
Auto-regressive moving average
model, 21
Avellaneda, M., 20, 224, 225
Bachelier, L., 2, 225
Back-testing procedures, 170
Bagchi, A., 224, 225
Bakshi, G., 47, 187, 189,
199, 225
Balland, P., 225
Barle, S., 225
Barndorff-Nielsen, O.E., 225
Bates, D.S., 158, 189, 208, 225
Bates model, 185
EPF application, 162–165
Bayesian approach, 48, 144–156
example, 146–147
Bensoussan, A., 225
Bensoussan-Crouhy-Galai (BCG)
approach, 11–13
model, 1
Berg, A., 233
Bernardo, J., 225
Bertsekas, D.P., 225
Bessel function, 184
Bias test, 54
Bid-ask spread, 71, 206
Binomial tree, usage, 6, 17
Bishop, G., 235
Blacher, G., 225
Black, F., 225
Black-Scholes approach, 5–6
Black-Scholes equation
rederiving, 29
Black-Scholes formula, usage, 15
Black-Scholes implied
volatility, 196
Black-Scholes PDE, 1
Black-Scholes pricing
function, 213
Black-Scholes risk-neutral pricing
formula, 4
Black-Scholes risk-neutrality
argument, usage, 25
Blocking technique, 150
Bollerslev, T., 226
Bouchaud, J.P., 226
236

Index
237
Bouchouev, I., 226
Box-Ljung test, 48, 95–96
Brandt, M.W., 224, 226
Breeden, D.T., 14, 226
Breeden-Litzenberger identity, 14
Brockhaus, O., 226
Brotherton-Ratcliffe, R., 224
Brownian motion, 22, 40, 43
construction, 97
independence, 44, 158
process, 2
spot return variances, 19
Budhiraja, A.S., 232
Buraschi, A., 226
Burn-in period, 76
Cakici, N., 225
Calibration frequency, 19
Cao, C., 47, 189, 199, 225
Carr, P., 215, 226, 232
Carr-Madan replication,
202–203
Chalasani, P., 234
Chang, E.C., 215, 232
Chapman-Kolmogorov equation,
application, 58
Characteristic function, usage,
157–158
Chen, Z., 47, 189, 199, 225
Chernov, M., 226
Chia, N.K.K., 232
Chib, S., 226, 228, 232
Chi-square test, 95
usage, 179–181
Cholesky factorization, usage,
31, 66, 74, 87
Chourdakis, K.M., 159, 226
Chriss, N.A., 227
Christoffersen, P., 230
CIR process, usage, 44
Clapp, T., 224
Close-to-the-money strike prices,
optimization, 50
Close-to-the-money strikes, 192
Conjugate directions, 49
Conjugate priors, 145
Consistency problem, 187
introduction, 187–189
Consistency test, 189–197
cross-sectional results, 190–193
robustness issues, 190–193
setting, 190
Constant elasticity variance
(CEV), 1
approach, 11
Constant volatility approach,
extension, 4
Constraint parameter, 18
Continual recalibration
(CR) strategy, 19
Continuous ideal process,
sample, 3
Continuous SDE, 131
Convergence issues/solutions,
185–186
Corradi, V., 24, 227
Corrado, C.J., 227
Correlation parameter, 156
Covariance matrix, 70, 83, 161
Covered call option, transform
results, 34
Cox, J.C., 7, 11, 227
Cox-Ross-Rubinstein
approach, 6–7
Cramer-Rao bound, 56
Credit spread, link, 10
Cross-sectional VGSA,
time-series VGSA (contrast),
216–218
Crouhy, M., 225

238
INSIDE VOLATILITY ARBITRAGE
Cumulative distribution function
(CDF), 41, 45, 101
Das, S.R., 203, 227
De Freitas, N., 227, 235
Delta hedging, 200, 204
Demeterfi, K., 227
Dempster, M.A.H., 227
Deng, S., 159, 227
Derivative security, payoff
inclusion, 32
Derivatives market, 4–7
Derman, E., 14, 227
Derman-Kani approach, 17
Deterministic volatility, example,
34–35
Dewynne, J., 235
Diagnostics, 95–98
Diebold, F.X., 224
Diffusion limits, 21–24
Diffusion-based model, 47
Direction set method (Powell
method), 49–50, 83–84
Directional risks, 200–202
Discrete GARCH, 23–24
Discrete NGARCH, risk-neutral
version, 26
Diversification argument,
usage, 10
Doucet, A., 227, 235
Dragulescu, A.A., 158, 228
Duan, J.C., 228
Dufresne, Daniel, 228
Dumas, B., 187, 189, 228
Dupire, B., 14, 228
Dupire approach, 14–17
Dupire identity, 14–15
Durrett, R., 228
Early termination, 206
Elerian, O., 228
El-Karoui, N., 27, 228, 229
Elliott, R.J., 228
Engle, R.F., 21, 123, 228
Entropy distance, 18
Eraker, B., 228
Ergodic averaging theorem, 144
Errors, distribution, 50–54
Euler approximation, usage, 23
Euler scheme, 140
EUR/USD options, 220
Extended Kalman filter (EKF),
59–62, 88, 161–162
application, 132, 172–173
convergence, 105
estimation, 85, 139
framework, log-likelihood
function, 140
implementation, 89–94
Jacobians, 77
observability, 75–76
Extended particle filter (EPF),
102, 161–166, 172–176, 179
Fama, E., 228
Fan, J., 228
Feller distribution, 3–4
Feynmann-Kac equation, 6
Filter errors, 84
Filtering, 57–59
errors, 115, 117
normalized/non-normalized
weights, 99
Financial interpretation,
194–197
Firm structure model, usage, 12
Fisher information matrix, 56
Fixed fractional jump size,
158–159
Fixed income, 219–223
Flannery, B.P., 233
Fleming, J., 189, 228

Index
239
Fletcher-Reeves-Polak-Ribiere
method, 49
Fokker-Planck equation, 14–15
Follmer, H., 228
Forbes, C.S., 229
Foreign exchange (FX), 219–220
rate process, 219
Forward Kolmogorov equation,
14–15
Foster, D.P., 233
Fouque, J.P., 21, 96, 229
Fourier transform, inversion, 30
Fournier, D.A., 233
Frey, R., 229
Fridman, M., 229
Friedman, C., 224
Friedman, Milton, 198
Further-from-the-money
options, 192
Future spot prices, 7
Galai, D., 225
Gallant, A.R., 229
Galli, A., 96, 229, 231
Gamma. See Variance gamma
distribution, 41–42, 158, 172
dependence, 170
variables, 216
Gamma-distributed random
variable, 44
Garcia, R., 229
Gatheral, J.G., 16, 229
Gauss-Hermite quadrature of
order, 67
Gauss-Hermite roots of order, 65
Gaussian approximation, 136
Gaussian cases, 59
Gaussian likelihood,
maximization, 82
Gaussian quadrature, 65
Gaussian random variables,
97, 104
Gaussian realization, 40, 214
Gaussian SV models, MCMC
application, 154–156
Gelfand, A.E., 234
Geman, H., 226, 229
Generalized autoregressive
conditional
heteroskedasticity (GARCH),
1, 21–24
diffusion, 137
diffusion-limit model, 94, 121
MLE, 138
process, weak convergence, 21
Generalized Fourier transform,
2, 27–30
Generic particle filter,
160–161, 179
George, E.I., 226
Geske, R., 229
Ghyseles, E., 226, 229
Gibbs sampler, 144–150, 154
Gilks, W.R., 229
Girsanov theorem, 25–26, 188,
213, 220
Gondzio, J., 229
Gordon, N., 224, 227
Gordon, N.J., 229
Gotsis, G.Ch., 227
Gourieroux, C., 229, 230
Grabbe, J.O., 230
Greenberg, E., 226
Grenander, U., 234
Gunther, S., 233
Hamilton, J.D., 159, 230
Hammersley-Clifford
theorem, 144
Härdle, W., 199, 230
Harris, L., 229

240
INSIDE VOLATILITY ARBITRAGE
Harvey, A.C., 135, 230
Harvey-Ruiz-Shephard (HRS)
method, 136, 139
Haug, E.G., 230, 231
Haykin, S., 67, 230
Heaviside function, 16
Hedge ratio usage, selection, 208
Hedged portfolio, 6
Henderson, R., 231
Hermite polynomials, usage, 103
Hessian matrix, 39
Heston, S., 21, 230
Heston state-space model, 47
comparison, 120–127
EPF, application, 105–114
equation, 154–156
particle filtering, application,
105–114
results, 122–125
High correlation, 209–213
High volatility-of-volatility,
209–213
High-frequency data, 185–186
Hipp, C., 230
Hirsa, A., 230
Historic correlation, 212
Historic volatility, 3–4
Hobson, D.G., 230
Holmes, R., 224
Honoré, P., 230
Howison, S.D., 230, 231, 235
Hughston, L.P., 230, 231
Hull, J., 2, 6, 19, 30, 231
Ill-posed inversion problems, 18
Implied volatility term structure,
206–208
Importance sampling technique,
99–100
Incomplete beta function
(IBF), 151
Induction expression, 157
Inference problem, 46
Inference tools
accuracy issues, 218–219
error size, 133–139
high-frequency data, 139–140
observations, frequency,
140–141
parameters, joint estimation,
132–133
performance, 127–144
sample size, 129–132
sampling distribution, 141–144
Information matrix identity, 56
Insurance selling strategy, 201
Inverse Fourier transform, 27
Inverse gamma (IG) CDF,
152–153
Ishida, I., 123, 228
Ito, K., 231
Ito’s lemma, usage, 2, 6, 26
Jackel, P., 19, 231
Jackson, N., 231
Jackwerth, A.C., 226
Jackwerth, J.C., 198, 231
Jacobian calculation, 62, 70,
73–74, 87
Jacobian matrices, defining,
60–61
Jacobs, K., 230
Jacquier, E., 231
Jarrow, R., 231
Jasiak, J., 230
Javaheri, A., 230, 231
Jensen, G.R., 234
Jex, M., 231
Jha, S., 234
Jiang, G.J., 231
Johannes, M., 159, 228, 231

Index
241
Joint filter (JF), 68
time interval, interaction,
78–81
usage, 125
Joint filtering (JF), example,
69–75
Jones, C.S., 231
Julier, S.J., 231
Jump-based models,
non-Gaussianity, 124
Jumps
component, orthogonality,
167
diffusion, 7–10
model, usage, 198
introduction, 158–168
model, 158–160
numeric results, 167
parameters, 167
simulation, Srivastava
approach,
166–167
Kalman filter (KF)
reapplication, 119
usage, 58–59, 86–87, 96, 102
Kalman gain, interpretation, 59,
61, 67
Kamal, M., 227
Kani, I., 14, 227
Karatzas, I., 2, 6, 231
Kennedy, P., 232
Kim, S., 232
Kirby, C., 228
Kitagawa, G., 232
Kleinow, T., 230
Klopfer, W., 234
Koopman, S.J., 234
Kou, S., 8, 232
Kouwenberg, R., 229
Krishnamurthy, V., 227
Kullback-Leibler distance, 18, 55
Kurtosis, trades/trading,
200–203, 222
Kushner, H.J., 65, 232
Kushner algorithm, details,
66–67
Kushner filters, 98
Kushner’s nonlinear filter, 65–67
Lagnado, R., 232
Lagrange multiplier, 18, 214
Lahaie, C.H., 228
Lautier, D., 229, 231
Least-square estimation (LSE)
approach, 30, 53, 54
Least-square estimator (LSE),
46, 49
Lee, D.S., 232
Leptokurticity, 8
Level-dependent volatility, 7,
10–13
Levenberg-Marquardt (LM)
method, 49
Leverage
effect, 8, 22
parameter, 22, 26
Levy, A., 225
Levy process, 10
Lewis, Alan L., 2, 28–29, 34–38,
232
Lewis, K., 226
Li, Y., 232
Liability maturity, 12
Likelihood
evaluation, 57
filtering, 57
function, 54–57, 129, 132
maximization, 81, 161
Line minimization routine, 49
Linear a posteriori estimate, 60
Linear state-space system, 68–69

242
INSIDE VOLATILITY ARBITRAGE
Litzenberger, R.H., 14, 226
Local risk minimization, 27
Local volatility, 14–19
instantaneous volatility,
contrast, 16–17
stability issues, 18
Log-normal process, 2
Long, D., 226
Long-term asymptotic example,
34–40
Madan, D., 40–41, 215, 226,
228–229, 232
Maes, K., 232
Maheu, J.M., 159, 232
Market completeness, 5
Markov chain, creation, 144
Markov chain Monte Carlo
(MCMC), 144
algorithms, distributions
(usage), 151–153
approaches, 154
step, addition, 101
Markov process, 100
Markov property, usage, 58
Markowitz, H.M., 232
Martin, G.M., 229
Martingale, 16
Maskell, S., 224
Masoliver, J., 226
Matacz, A., 232
Matytsin, A., 232
Maximum likelihood estimate
(MLE), 18, 68, 88–89
iteration, 82
justification, 55–56
shortcomings, 129–131
McCurdy, T.H., 159, 232
Mean price error (MPE), 62, 118
reduction, 185
usage, 179
Mean-adjusted stock returns, 57
Measurement
equation, 87–88
noise, uncorrelation, 86–87
update equations, 61, 64, 66
Merton, R.C., 8, 199, 233
Metropolis-Hastings (MH)
accept/reject
technique, 126–127, 156
Metropolis-Hastings (MH)
algorithm, 144, 147–150
enhancement, 119–120
example, 150–151
Metropolis-Hastings (MH)
density, 149
Metropolis-Hastings (MH)
modification, 120
Metropolis-Hastings (MH)
sampling algorithm, 101
Meyer, R., 233
Mezrich, J., 228
MH. See Metropolis-Hastings
Miller, M.I., 234
Mirror trades, 203
Mixing solutions, 30–33
Models, identification,
120–121, 185
Modified model, 80
Monfort, A., 229
Monte Carlo algorithm, 222
Monte Carlo
approximation, 102
Monte Carlo method, usage, 50
Monte Carlo mixing, 193
Monte Carlo process,
obtaining, 23
Monte Carlo sampling,
usage, 100

Index
243
Monte Carlo simulation, 32–33,
98, 169
Monte Carlo time steps, 190
Monte Carlo-based models, 2
Multiple trades, 208–209
Muzzioli, S., 233
Mykland, P.A., 235
Nadari, F., 226
Nandi, S., 21, 230
Neftci, S.N., 233
Nelson, D.B., 233
Ng, V., 224, 228
Nicolato, E., 225
No-default case, 10
Noise
drift, 167
one-dimensional source, 73
Non-Gaussian case, 213–218
Non-Gaussian filters, 160
Non-Gaussian pure jump
model, 47
Non-Gaussianity, 179
Nonlinear asymmetric GARCH
(NGARCH), 22
Nonlinear filter (NLF), 65,
103, 121
Nonlinear Gaussian KF, 161
Nonlinear PDE, 13
Nonlinear transition equation, 60
Numeric tests, 50, 183
Observation
error, 178–179
matrix, 83–84, 87
noise, 75
Oksendal, B., 2, 233
One-dimensional EKF/UKF, 96
One-dimensional Heston model,
114–115
One-dimensional state, 87–94
joint filter, inclusion, 76–78
One-factor diffusion process, 138
One-factor Monte Carlo
technique, 32–33
Optimization algorithm, 168
weakness, 127–128
Option prices, usage, 49–54
Option pricing, cross section,
221–223
Options
bid-ask spread, 205–206
maturity, 6
time-to-maturities,
decrease, 208
Ornstein-Uhlenbeck (OU)
process, 20
Osher, S., 232
Out-of-the-money (OTM)
options, 200
puts/calls, usage, 188, 209
region, Black-Scholes value, 38
Pan, G., 233
Pan, J., 233
Papanicolaou, G., 229
Parameter estimation, 217. See
also Pure jump models
MLE usage, 81–94
example, 82–83
implementation, alternate,
86–87
Parameter learning, 67–81,
125–127
example, 68–69
Parametric SV, 20
Paras, A., 225
Parkinson, M., 3, 233

244
INSIDE VOLATILITY ARBITRAGE
Partial differential equation
(PDE). See
Black-Scholes PDE;
Nonlinear
PDE; Two-factor PDE
pricing, stochastic volatility
(impact), 24–27
risk-neutral version, 2
Particle filter (PF)
algorithm, writing, 169–170
implementation, 160
Particle filtering, 98–120
algorithm, application,
121–122
application. See Heston
space-state model
error size, 116–119
example, 104–105
implementation, 103–104
resampling, 101–103
test results, 114–116
theory, 99–101, 117
Pearson kurtosis, 22
Pedersen, A.R., 233
Penny stocks, skew, 209
Perelló, J., 226
Peso theory, 197–199
background, 197–198
numeric results, 199
Pham, H., 233
Phantom profits, creation, 19
Pitt, M.K., 233
Poisson jumps, 159
Poisson process, 8–9
Poisson random variable, 9
Polson, N.G., 159, 228, 231
Powell algorithm, application, 50
Press, W.H., 31, 50, 233
Prucyk, B., 234
Pure diffusion, 7–9
parameter, 199
Pure jump models, 40–45,
168–184, 215
algorithms, usage, 170–172
diagnostics, 178–179
filtering algorithm, usage,
169–170
numeric results, 176–178
parameter estimation, 170
Quenez, M.C., 27, 228
Rafailidis, A., 230, 231
Randall, C., 234
Rasmussen, H.O., 230
Regression analysis, 153
Reif, K., 233
Rejection probability, 149
Renault, E., 229, 233
Resampling algorithm, 101
Residuals, 62
Reverse Black-Scholes equation,
solving, 7
Reversibility condition, 149–150
Ribiero, C., 233
Richardson, S., 229
Ridge property, 36
Risk, market price, 25
Riskless arbitrage, 6
Risk-neutral GARCH system, 26
Risk-neutral implied
parameter, 190
Risk-neutral parameters, 215
Risk-neutral pricing formula. See
Black-Scholes risk-neutral
pricing formula
Ritchken, P., 234
Robustness, issues. See
Consistency test; Time-series
method
Rochet, J.C., 229

Index
245
Rogers, L.C.G., 230
Romano, M., 32, 234
Romano-Touzi approach, 30–32
Root mean square error (RMSE),
62, 118
reduction, 185
usage, 179
Ross, S., 227
Rossi, P.E., 231
Rubinstein, M., 198, 227,
231, 234
Rudd, A., 231
Ruiz, E., 135, 230
Salmond, D.J., 229
Samperi, D., 224
Sample impoverishment, 119
Samuelson, P. A., 2, 234
Sandmann, G., 234
Santa-Clara, P., 226
Scholes, M., 225
Schonbucher, P.J., 234
Scott, L.O., 234
Self-financing portfolio
argument, usage, 214–215
Sequential importance
sampling, 100
Shephard, N., 135, 225, 226,
228, 232, 233
Shimko, D., 234
Shreve, S., 6, 21, 231, 234
Signal-to-noise ratio (SNR), 138
Silva, A.C., 234
Simple Kalman filter, 59–62
Sin, C.A., 234
Single calibration (SC)
methodology
assumption, 19
Sircar, K., 229
Skewness
kurtosis, contrast, 201–202
trades, 189, 200
example, 203–208
Smith, A.F.M., 225, 229, 234
Sondermann, D., 228
Spiegelhalter, D.J., 229
Spot prices, observation, 183
Spread. See Options bid-ask
spread
Square root model, optimization
constraints, 85–86
Square root SDE, 184
Square root SV model, 37, 69–70
Srivastava, A., 166, 234
Srivastava approach. See Jumps
Stability issues. See Local
volatility
Stahl, G., 230
Standard & Poor’s (S&P), 208
options, 189, 198
S&P 500, 204, 216–218
Stock Index, 4
Stein, E.M., 234
Stein, J., 234
Stochastic differential equation
(SDE), 197–198, 221
Stochastic volatility (SV), 20–24
behavior, 24
example, 35–37, 83–85
formulation, 76
impact. See Partial differential
equation
problem, 78–79
processes, 20–21
time-changed processes,
contrast, 42–43
Stochastic volatility (SV) models,
94, 136
embedded parameters,
inference (problem), 48
Heston state-space model,
comparison, 121–122
parameters, 196

