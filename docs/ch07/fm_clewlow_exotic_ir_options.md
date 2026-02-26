# Exotic & Interest Rate Options

!!! info "Source"
    **Computational Finance: Numerical Methods** by Clewlow and Strickland.
    These notes are used for educational purposes.

## Exotic Options

f 4
2 ¼ maxð32  100; 0Þ ¼ 0;
f 5
2 ¼ maxð50  100; 0Þ ¼ 0;
f 6
2 ¼ maxð48  100; 0Þ ¼ 0
f 7
2 ¼ maxð102  100; 0Þ ¼ 2;
f 8
2 ¼ maxð88  100; 0Þ ¼ 0;
f 9
2 ¼ maxð80  100; 0Þ ¼ 0
Time step 1
Here we have:
g1
1 ¼ maxð115  100; 0Þ ¼ 15; g2
1 ¼ maxð60  100; 0Þ ¼ 0;
g3
1 ¼ maxð114  100; 0Þ ¼ 14
Since r ¼ 0 we have exp (  rt) ¼ 1 which gives:
h1
1 ¼ 1
3 f 1
2 þ f 2
2 þ f 3
2
	

¼ 1
3 16 þ 0 þ 49
f
g ¼ 21:7
h2
1 ¼ 1
3 f 4
2 þ f 5
2 þ f 6
2
	

¼ 1
3 0 þ 0 þ 0
f
g ¼ 0
h3
1 ¼ 1
3 f 7
2 þ f 8
2 þ f 9
2
	

¼ 1
3 2 þ 0 þ 0
f
g ¼ 0:66
The option values are then computed as follows:
f 1
1 ¼ maxðh1
1; g1
1Þ ¼ maxð21:7; 15Þ ¼ 21:7
f 2
1 ¼ maxðh2
1; g2
1Þ ¼ maxð0; 0Þ ¼ 0
f 3
1 ¼ maxðh3
1; g3
1Þ ¼ maxð0:66; 14:0Þ ¼ 14:0
Time step 0
Here
g1
0 ¼ maxð101  100; 0Þ ¼ 1;
and
h1
0 ¼ 1
3 f 1
1 þ f 2
1 þ f 3
1
	

¼ 1
3 21:7 þ 0 þ 0:66
f
g ¼ 11:9
The final value of the option for this particular lattice is therefore:
f 1
1 ¼ maxðh1
0; g1
0Þ ¼ maxð11:9; 1Þ ¼ 11:9
Compute the Monte Carlo estimate
The Monte Carlo estimate, H, is computed as the average of p
H, p ¼ 1, . . . , nsim,
where nsim is the number of simulations.
H ¼
X
nsim
i¼1
i
H
nsim
216
Pricing Assets

Below, in Code excerpt 10.20, we provide a computer program which prices single
asset American put and call options using a stochastic lattice. The method used by
the program is the depth first procedure outlined in Broadie and Glasserman (1997),
which has the advantage that the memory requirements are only of order b  d; as
before b is the number of branches per node and d is the number of time intervals.
Here it is assumed the underlying asset following GBM and the NAG function
g05ddc(M, S) is used to generate a normal distribution with mean M and standard
deviation S. We can therefore check the acuracy of the simulation with that obtained
by a closed form solution which assumes a lognormal asset distribution, in this case
the formula in Geske and Johnson (1984).
However, the real power of this method is when the underlying asset follows a
more realistic process which is nonGaussian and time varying. The only modification
to the code is to replace the call to g05ddc with that of another probability
distribution and supply the time varying parameters to it.
#include <nag.h>
#include <stdio.h>
#include <nag_stdlib.h>
#include <math.h>
#include <nagg05.h>
// Stochastic lattice for computing the value of American and European options via Monte Carlo simulation.
// Here we assume that the asset prices have a lognormal distribution, and so generate
// normal variates; this assumption can easily be removed.
void__cdecl main()
{
long i, j, jj, is_put, is_american, w[200], num_simulations, b, d, seed;
double T, time_step, sqrt_time_step, opt_value, pay_off, log_fac, asset_price;
double temp, opt_val, hold, sum_opt_val, disc;
double tot_opt_vals, X, drift_term, std_term, S0, q, r, sigma, zero ¼ 0.0;
double v[200][60], opt_v[200][60];
printf(‘‘Stochastic lattice for pricing European and American options \n’’);
is_put ¼ 1;
// If is_put ¼¼ 0 then a call option, otherwise a put option
T ¼ 1.0;
// The time to maturity of the option
is_american ¼ 1;
// If is_american ¼¼ 0 then an European option, otherwise an American option
sigma ¼ 0.2;
// The volatility of the underlying asset
X ¼ 110.0;
// The strike price
S0 ¼ 100.0;
// The current price of the underlying assset
r ¼ 0.1;
// The risk free interest rate
q ¼ 0.05;
// The continuous dividend yield
d ¼ 4;
// The number of time steps, the number time intervals ¼ d  1
b ¼ 50;
// The number of branches per node in the lattice
time_step ¼ T/(double)(d 1); // time step ¼ T/(number of time intervals)
sqrt_time_step ¼ sqrt(time_step);
disc ¼ exp(r*time_step); // The discount factor between time steps
std_term ¼ sigma*sqrt(time_step); // The standard deviation of each normal variate generated
drift_term ¼ (r  q  sigma*sigma*0.5)*time_step; // The mean value of each normal variate generated
seed ¼ 111; // The seed for the random number generator
g05cbc(seed);
tot_opt_vals ¼ zero;
num_simulations ¼ 100;
for (jj ¼ 1; jj <¼ num_simulations; þþjj) {
v[1][1] ¼ S0;
w[1] ¼ 1;
asset_price ¼ S0;
for (j ¼ 2; j <¼ d; þþj){
w[j] ¼ 1;
log_fac ¼ g05ddc(drift_term, std_term); // A normal variate:mean¼¼drift_term, standard
// deviation¼¼std_term
asset_price ¼ asset_price*exp(log_fac); // Compute the new asset price: assuming a lognormal
// distribution
v[1][j] ¼ asset_price;
}
j ¼ d;
Numeric methods and single asset American options
217

while (j > 0){
if ((j ¼¼ d) && (w[j] < b)) { // CASE 1::Terminal node, set asset prices for b branches, and option values
// for b 1 branches
if (is_put) {
pay_off ¼ MAX (X  v[w[j]][j], zero);
}
else {
pay_off ¼ MAX (v[w[j]][j]X, zero);
}
opt_v[w[j]][j] ¼ pay_off;
asset_price ¼ v[w[j 1]][j 1];
log_fac ¼ g05ddc(drift_term, std_term);
v[w[j]þ 1][j] ¼ asset_price*exp(log_fac);
w[j] ¼ w[j] þ 1;
}
else if ((j ¼¼ d) && (w[j] ¼¼ b)) { // CASE 2::Terminal node, set option value for last branch
if (is_put) {
pay_off ¼ MAX (X  v[w[j]][j], zero);
}
else {
pay_off ¼ MAX (v[w[j]][j]X, zero);
}
opt_v[w[j]][j] ¼ pay_off;
w[j] ¼ 0;
j ¼ j  1;
}
else if ((j < d) && (w[j] < b)) { // CASE 3::Internal node,
// calculate option value for node (parent wrt to cases 1 & 2)
sum_opt_val ¼ zero; // Also generate a new terminal node and set asset values.
for (i ¼ 1; i <¼ b; þþi) {
sum_opt_val þ¼ opt_v[i][jþ 1];
}
temp ¼ sum_opt_val/(double)b;
hold ¼ temp*disc;
if (is_american) { // An American option
if (is_put) {
pay_off ¼ MAX(Xv[w[j]][j], zero); // pay off for a put option
}
else {
pay_off ¼ MAX(v[w[j]][j]X, zero); // pay off for a call option
}
opt_val ¼ MAX(pay_off, hold);
}
else { // A European option
opt_val ¼ hold;
}
opt_v[w[j]][j] ¼ opt_val;
if (j > 1) {
asset_price ¼ v[w[j 1]][j 1];
log_fac ¼ g05ddc(drift_term, std_term);
v[w[j]þ1][j] ¼ asset_price*exp(log_fac);
w[j]¼ w[j] þ 1;
for (i ¼ j þ 1; i <¼ d; þþi) { // Generate a new terminal node
log_fac ¼ g05ddc(drift_term, std_term);
asset_price ¼ asset_price*exp(log_fac);
v[1][i] ¼ asset_price;
w[i] ¼ 1;
}
j ¼ d;
}
else {
j ¼ 0;
}
}
else if ((j < d) && (w[j] ¼¼ b)) { // CASE 4::Internal node, calculate the option value for the last branch
sum_opt_val ¼ zero;
for (i ¼ 1; i <¼ b; þþi) {
sum_opt_val þ¼ opt_v[i][jþ 1];
}
temp ¼ sum_opt_val/(double)b;
hold ¼ temp*disc;
if (is_american) { // An American option
if (is_put) {
pay_off ¼ MAX(X  v[w[j]][j], zero); // pay off for a put option
}
else {
218
Pricing Assets

pay_off ¼ MAX(v[w[j]][j]X, zero); // pay off for a call option
}
opt_val ¼ MAX(pay_off, hold);
}
else { // A European option
opt_val ¼ hold;
}
opt_v[w[j]][j] ¼ opt_val;
w[j] ¼ 0;
j ¼ j  1;
}
}
tot_opt_vals ¼ tot_opt_vals þ opt_v[1][1]; // Sum the option values for each simulation
}
opt_value ¼ tot_opt_vals/(double)num_simulations; // Compute the average option value
printf (‘‘The estimated option value ¼ %12.4f\n’’, opt_value);
}
Code excerpt 10.20
A computer program which uses a stochastic lattice to value American
and European options
In Table 10.13 below we present computed values of an American put option
with maturity , that can only be exercised at the following four times:
t, t þ =3, t þ 2=3, and t þ , where t is the current time.
The column labelled MC100
50 presents the results obtained using 100 simulations
of a stochastic lattice with 50 branches per node, and the column labelled MC1
250
presents the values computed using a single stochastic lattice with 250 branches
per node. These values demonstrate that one high accuracy stochastic lattice can
give better results than using the average of 100 lower accuracy lattices. In the
last two columns we present the computed binomial lattice values for the American
put and also the corresponding European put. The binomial lattice had 6000
Table 10.13
American put options values, computed using the stochastic lattice given in Code excerpt
10.20, with four the exercise times t, t þ =3, t þ 2=3, and t þ . The option parameters used were:
r ¼ 0:1, q ¼ 0:05,  ¼ 1:0,  ¼ 0:2, S ¼ 100:0 and E, the strike price, is varied from 70 to 130. The column
labelled MC100
50 refers to the results obtained using d ¼ 4, b ¼ 50, num_simulations ¼ 100, and the column
labelled MC1
250 refers to the results obtained using d ¼ 4, b ¼ 50, num_ simulations ¼ 1. The true values
are those given in Broadie and Glasserman (1997), and were computed with the formula in Geske and
Johnson (1984). The absolute error, ABS(stochastic_lattice_value  true_value), is given in brackets.
The last two columns are the computed results using an accurate (6000 time step) binomial lattice; the
column labelled BLA contains the American put option values, and the column labelled BLE contains
the European put option values. It can be seen that in all cases the American put option has a
significant early exercise premium
E
MC100
50
MC1
250
True
BLA
BLE
70
0.118 (0.003)
0.123 (0.002)
0.121
0.126
0.120
80
0.663 (0.007)
0.672 (0.002)
0.670
0.696
0.654
90
2.317 (0.014)
2.307 (0.004)
2.303
2.389
2.198
100
5.830 (0.099)
5.720 (0.011)
5.731
5.928
5.301
110
11.564 (0.223)
11.361 (0.020)
11.341
11.770
10.155
120
20.205 (0.205)
20.000 (0.000)
20.000
20.052
16.547
130
30.054 (0.054)
30.000 (0.000)
30.000
30.000
24.065
Numeric methods and single asset American options
219

time steps and it was possible to exercise the option at every time step. It can be
seen that the computed binomial option values for the American put are higher
than the true values, which only permit the option to be exercised at four distinct
times. This is in agreement with the extra flexibility present in the binomial
lattice. Inspection of the computed European put and American put binomial
option values also reveals that the American put option has a significant early
exercise premium.
220
Pricing Assets

Chapter 11
Monte Carlo simulation
11.1
INTRODUCTION
Monte Carlo simulation and random number generation are techniques that are
widely used in financial engineering as a means of assessing the level of exposure to
risk. Typical applications include the pricing of financial derivatives and scenario
generation in portfolio management. In fact many of the financial applications that
use Monte Carlo simulation involve the evaluation of various stochastic integrals
which are related to the probabilities of particular events occurring.
For instance in Section 9.1 we gave the value of a European call option as:
cðS; E; Þ ¼ expfrg
Z 1
1
pðSTÞ maxðE  ST; 0ÞdST
and that of a put as:
pðS; E; Þ ¼ expfrg
Z 1
1
pðSTÞ maxðE  ST; 0ÞdST
where E is the strike price, T is the expiry date, t is the current time,  ¼ T  t, r is the
riskless interest rate and p(ST) is the probability that the asset will have market value
ST at maturity.
In many cases however, the assumptions of constant volatility and a lognormal
distribution for ST are quite restrictive. Real financial applications may require a
variety of extensions to the standard Black–Scholes model. Common requirements
are for: nonlognormal distributions, time varying volatilities, caps, floors, barriers,
etc. In these circumstances it is often the case that there is no closed form solution to
the problem. Monte Carlo simulation can then provide a very useful means of
evaluating the required integrals.
When we evaluate the integral of a function, f (x), in the dimensional unit cube, IS,
by the Monte Carlo method we are in fact calculating the average of the function at a
set of randomly sampled points. This means that each point adds linearly to the
accumulated sum that will become the integral and also linearly to the accumulated
sum of squares that will become the variance of the integral.
When there are N sample points the integral is:
 ¼ 1
N
X
N
i¼1
f ðxiÞ
ð11:1Þ

where  is used to denote the approximation to the integral and x1, x2, . . . , xN are the N,
s-dimensional, sample points. If a pseudorandom number generator is used the points
xi will be (should be) independently and identically distributed. From standard statis-
tical results we can then estimate the expected error of the integral as shown below.
If we set i ¼ f (xi) then since xi is independently and identically distributed i is
also independently and identically distributed. The mean of i is  and we will denote
the variance as Var(i) ¼ 2. It is a well-known statistical property that the variance
of  is given by Var() ¼ N12, see Appendix F.1 for further details. We can
therefore conclude that the estimated integral  has a standard error of N1=2.
This means that the estimated error of the integral will decrease at the rate of N1=2.
It is possible to achieve faster convergence than this if the sample points are chosen
to lie on a Cartesian grid. If we sample each grid point exactly once then the Monte
Carlo method effectively becomes a deterministic quadrature scheme, whose
fractional error decreases at the rate of N1 or faster. The trouble with the grid
approach is that it is necessary to decide in advance how fine it should be, and all the
grid points need to be used. It is therefore not possible to sample until some
convergence criterion has been met.
Quasirandom number sequences seek to bridge the gap between the flexibility of
pseudorandom number generators and the advantages of a regular grid. They are
designed to have a high level of uniformity in multidimensional space, but unlike
pseudorandom numbers they are not statistically independent.
11.2
PSEUDORANDOM AND QUASIRANDOM SEQUENCES
Here we consider the generation of multidimensional pseudorandom and quasiran-
dom sequences to approximate the multidimensional uniform distribution over the
interval [0, 1], that is the distribution U(0, 1).
Quasirandom numbers are also called low discrepancy sequences. The discrepancy
of a sequence is a measure of its uniformity and is defined below.
Given a set of points x1, x2, . . . , xN 2 IS and a subset G 	 IS, define the counting
function SN(G) as the number of points xi 2 G. For each x ¼ (x1, x2, . . . , xs) 2 IS, let
Gx be the rectangular s-dimensional region Gx ¼ [0, x1) 
 [0, x2) 
    
 [0, xs), with
volume x1, x2, . . . , xn. Then the discrepancy of the points x1, x2, . . . , xN is given by:
D
Nðx1, x2, . . . , xNÞ ¼ supx2IS SNðGxÞ  Nx1x2; . . . ; xs
j
j
The discrepancy is therefore computed by comparing the actual number of sample
points in a given volume of multidimensional space with the number of sample points
that should be there assuming a uniform distribution.
It can be shown that the discrepancy of the first terms of quasirandom sequence
has the form:
D
Nðx1; x2; . . . ; xNÞ  CSðlog NÞS þ Oððlog NÞS1Þ
for all N  2.
The principal aim in the construction of low-discrepancy sequences is thus to find
sequences in which the constant is as small as possible. Various sequences have been
222
Pricing Assets

constructed to achieve this goal. Here we consider the following quasirandom
sequences proposed by Niederreiter (1992), Sobol (1967), and Faure (1982).
The results of using various random number generators are shown below. Figures 11.1
to 11.3 illustrate the visual uniformity of the sequences. They were created by generating
one thousand, sixteen dimensional U(0, 1), sample points, and then plotting the 4th
dimension component of each point against its 5th dimension component.
In Figure 11.1, it can be seen that the pseudorandom sequence exhibits clustering
of points, and there are regions with no points at all.
Visual inspection of Figures 11.2 and 11.3 show that both the Sobol and Nieder-
reiter quasirandom sequences appear to cover the area more uniformly.
It is interesting to note that the Sobol sequence appears to be a structured lattice
which still has some gaps. The Niederreiter sequence on the other hand appears to be
more irregular and covers the area better. However, we cannot automatically
conclude from this that the Niederreiter sequence is the best. This is because we have
not considered all the other possible pairs of dimensions.
Perhaps the easiest way to evaluate the random number sequences is to use them to
calculate an integral.
In Figure 11.4 Monte Carlo results are presented for the calculation of the
six-dimensional integral:
I ¼
Z 1
0
Z 1
0
Z 1
0
Z 1
0
Z 1
0
Z 1
0
Y
6
i¼1
cosðixiÞdx1dx2dx3dx4dx5dx6
0.9
0.9
0.8
0.8
0.7
0.7
0.6
0.6
0.5
0.5
0.4
0.4
0.3
0.3
0.2
0.2
0.1
0.1
0
0
1
1
Pseudorandom sequences
Figure 11.1
The scatter diagram formed by one thousand points from a sixteen dimensional Uð0, 1Þ
pseudorandom sequence. For each point the 4th dimension component is plotted against the 5th dimension
component
Monte Carlo simulation
223

0.9
0.9
0.8
0.8
0.7
0.7
0.6
0.6
0.5
0.5
0.4
0.4
0.3
0.3
0.2
0.2
0.1
0.1
0
0
1
1
Sobol sequences
Figure 11.2
The scatter diagram formed by one thousand points from a sixteen dimensional Uð0, 1Þ
Sobol sequence. For each point the 4th dimension component is plotted against the 5th dimension
component
0.9
0.9
0.8
0.8
0.7
0.7
0.6
0.6
0.5
0.5
0.4
0.4
0.3
0.3
0.2
0.2
0.1
0.1
0
0
1
1
Niederreiter sequences
Figure 11.3
The scatter diagram formed by one thousand points from a sixteen dimensional Uð0, 1Þ
Niederreiter sequence. For each point the 4th dimension component is plotted against the 5th dimension
component
224
Pricing Assets

The exact value of this integral is:
I ¼
Y
6
i¼1
sinðiÞ
which for i ¼ 6, gives I ¼ 0:0219.
It can be seen that the pseudorandom sequence gives the worst performance. But as the
number of points increases its approximation to the integral improves. Of the quasiran-
dom sequences it can be seen that the Faure sequence has the worst performance, whilst
both the Sobol and Neiderreiter sequences give rapid convergence to the solution.
Finance literature contains many references to the benefits of using quasirandom
numbers for computing important financial integrals. For instance Brotherton-
Ratcliffe (1994) discusses the use of Sobol sequences for the valuation of geometric
mean stock options, and provides results which show that the root mean squared pricing
error obtained using quasirandom numbers is considerably less than that computed
with pseudorandom numbers. Another financial application of quasirandom numbers
is the efficient pricing mortgage backed securities, Caflisch etal. (1997). Here Brownian
bridge techniques are employed to reduce the effective dimension of the problem
and thus provide greater pricing accuracy than if pseudorandom numbers were used.
11.2.1
Portfolio allocation
In this example quasirandom numbers are applied to a Markowitz style portfolio
allocation problem, see Markowitz (1989, 1994). It should be mentioned that many
Sobol
Niederreiter
Faure
Pseudorandom
Number of points (in thousands)
Monte Carlo integration
Value of integral
0.4
–0.4
–0.6
–0.8
–1
–1.2
–1.4
–1.6
0.2
0
–0.2
0
20
40
60
80
100
120
140
160
180
200
Figure 11.4
Monte Carlo integration using random numbers
Monte Carlo simulation
225

portfolio problems can be solved very efficiently using Newton (gradient based)
numerical optimization software to minimize a given object function subject to
certain constraints. However, this approach fails if the gradient of the objective
function is discontinuous; this is not the case when (quasi) random numbers are used.
We will start with an initial portfolio and use quasirandom numbers to plot out the
feasible region in which portfolios must lie in order to satisfy the portfolio constraints
and transaction costs. The asset vector X specifies the amount of each asset in a given
portfolio, and the initial portfolio allocation is denoted by the asset vector XI. In
particular we would like to be able to identify efficient portfolios, that is those which
for a given portfolio return minimize the portfolio risk. The problem of determining
efficient portfolios can be expressed as follows:
minimize V ¼ XTCX
ð11:2Þ
subject to the following constraints:
X
n
i¼1
Xi ¼ 1;
Li < Xi < Ui;
i ¼ 1; . . . ; n
ð11:3Þ
and
E ¼ X 
X
n
i¼1
	iABSðXI
i  XiÞ
ð11:4Þ
where E is the expected portfolio return, V is the portfolio risk,  is the vector of
expected asset returns, C is the covariance matrix of the assets, X is an asset vector
which specifies the amount of each asset ABS(X) is the absolute value of X, and Li,
Ui are the respective lower and upper bounds on the ith asset.
The transaction costs, 	i, that are used in equation are 	i ¼ 	s when XI
i > Xi, and
	i ¼ 	b when XI
i < Xi, where 	s is the cost of selling shares and 	b is the cost of
buying shares.
Here we consider a twenty asset portfolio, n ¼ 20, with either no transaction costs
or 	b ¼ 0:07 and 	s ¼ 0:04. The initial asset vector XI is such that there are equal
amounts of each asset, that is
XI
i ¼ 1
20 ,
i ¼ 1, . . . , 20
Private Sub Command2_Click()
Dim quasi(50), fcall, method1, n As Variant
Dim i, j, k, X, Y, num As Long
Dim XI(100), XP(100), V, E As Double
Dim Ret(100), C(50, 50) As Double
Dim sum As Double
Dim buy_cost, sell_cost As Double
Dim count, maxcount As Long
Dim max_holding(50), min_holding(50) As Double
Picture1.Cls
Picture1.DrawWidth ¼ 4
n ¼ 20
For i ¼ 0 To n  1
’ set up the expected asset returns
Ret(i) ¼ 0.008 * CDbl(i)
Next i
226
Pricing Assets

Ret(n  1) ¼ 0.06
For i ¼ 0 To n  1
’ set up the initial portfolio
XI(i) ¼ 1# / CDbl(n)
Next i
For i ¼ 0 To n  1
’ set up the covariance matrix
For j ¼ 0 To n  1
C(i, j) ¼ 0.01 * CDbl(i þ j)
If (i ¼ j) Then
C(i, j) ¼ CDbl(i) * 0.6
End If
Next j
Next i
C(6, 4) ¼ 0.4
C(4, 6) ¼ C(6, 4)
C(18, 10) ¼ 0.8
C(10, 18) ¼ C(18, 10)
fcall ¼ 1
method1 ¼ 3
’ Use Sobol sequences
COMP11.generate fcall, n, method1, quasi(0)
MsgBox ‘‘Starting quasi-random generation’’
fcall ¼ 0
buy_cost ¼ 0#
’ set the transaction costs
sell_cost ¼ 0#
’buy_cost ¼ 0.07
’sell_cost ¼ 0.04
For i ¼ 0 To n  1
’ set the maximum and minimum constraints
max_holding(i) ¼ 0.1
min_holding(i) ¼ 0.005
Next i
max_holding(0) ¼ 0.4
max_holding(1) ¼ 0.4
max_holding(2) ¼ 0.1
max_holding(18) ¼ 0.7
max_holding(19) ¼ 0.8
count ¼ 0
maxcount ¼ 500000
Do While (count < maxcount)
COMP11.generate fcall, n, method1, quasi(0)
sum ¼ 0#
For j ¼ 0 To n  2
XP(j) ¼ quasi(j) * (max_holding(j)  min_holding(j)) þ min_holding(j)
sum ¼ sum þ XP(j)
Next j
If (sum < ¼ 1) Then
XP(n  1) ¼ 1#  sum
E ¼ 0#
For j ¼ 0 To n  1
E ¼ E þ Ret(j) * XP(j)
Next j
For j ¼ 0 To n  1 ’ transaction costs
If (XP(j) > XI(j)) Then
E ¼ E  buy_cost * (XP(j)  XI(j))
End If
If (XP(j) < XI(j)) Then
E ¼ E  sell_cost * (XI(j)  XP(j))
End If
Next j
V ¼ 0#
For j ¼ 0 To n  1
For k ¼ 0 To n  1
V ¼ V þ C(j, k) * XP(j) * XP(k)
Next k
Next j
Y ¼ 5000  E * 4000 * 8
X ¼ V * 3000
Picture1.PSet (X, Y), RGB(0, 0, 255)
End If
count ¼ count þ 1
Loop
End Sub
Code excerpt 11.1
Visual Basic code which uses a twenty-dimensional quasirandom Sobol sequence to
plot the feasible region of a constrained portfolio consisting of twenty assets, and possible transaction costs
Monte Carlo simulation
227

The basic method is very simple, and full details can be found in Code excerpt 11.1.
We generate a quasirandom asset vector X, and then check that its elements satisfy
the constraints given in Equation 11.3. If they do not then we reject the asset vector X
and generate another one. If the asset vector X does satisfy the constraints
in Equation 11.3 we use Equation 11.2 to calculate the portfolio risk, V,
and Equation 11.4 to calculate the portfolio return, E. The point E, V is
then plotted on the diagram. This process is repeated a specified number of times.
In Code excerpt 11.1 we generate 500,000 vectors Q from a U(0, 1) twenty-
dimensional quasirandom Sobol sequence, and the elements of each vector satisfy
0  Qi  1, for i ¼ 1, . . . , 20. In order to ensure that not too many vectors get rejected
we generate the portfolio allocation vector by using the following transformation:
Xi ¼ QiðUi  LiÞ þ Li;
i ¼ 1; . . . ; 20
where Li and Ui have already been mentioned in Equation 11.3.
The resulting return/risk plots for the portfolios are shown in Figures 11.5 and
11.6. In both cases the efficient frontier is clearly visible and, as expected, the return
in Figure 11.5 without transaction costs is higher than in Figure 11.6 where
transaction costs are included. Furthermore, by examining the components of the
asset vectors X, on the efficient boundary we can find the optimal (minimum risk)
portfolio composition for a given portfolio return.
Figure 11.5
Illustrating the use of a quasirandom Sobol sequence to plot the feasible region of a
constrained portfolio containing twenty assets, with the transaction costs set to zero. The plot was
generated by the Visual Basic Code excerpt 11.1
228
Pricing Assets

11.3
GENERATION OF MULTIVARIATE DISTRIBUTIONS: INDEPENDENT
VARIATES
In this section we show how to generate independent variates from multivariate
distributions; that is the variates have zero correlation.
11.3.1
Normal distribution
The most fundamental distribution is the univariate standard normal distibution,
N(0, 1), with zero mean and unit variance. In the case of p independent variates this
takes the form of a p variate independent normal distribution N(0, Ip) with zero mean
and p 
 p unit covariance matrix Ip.
First we will quote a result concerning multivariate probability density functions,
see Press et al. (1992). If x1, x2, . . . are random variates with a joint probability
density function p(x1, x2, . . . ), and if there are an equal number of y variates
y1, y2, . . . that are functions of the x’s, then the joint probability density function of
the y variates, p( y1, y2, . . . ) is given by the following expression:
pðy1; y2; . . .Þdy1dy2; . . . ¼ pðx1; x2; . . .ÞJ x;ydy1dy1
ð11:5Þ
where J x,y is the Jacobian determinant of the x’s with respect to the y’s.
An important application of this result is the Box Muller transformation, see Box
and Muller (1958), in which a p variate independent normal distribution N(0, Ip) is
generated from a p variate uniform distribution U(0, 1).
Figure 11.6
Illustrating the use of a quasirandom Sobol sequence to plot the feasible region of a
constrained portfolio containing twenty assets, with transaction costs for buy and sell set to 0.07 and 0.04
respectively. The plot was generated by the Visual Basic Code excerpt 11.1
Monte Carlo simulation
229

The method works as follows: Consider two independently distributed N(0, 1)
variables x and y, and use the polar transformation to obtain:
x ¼ r cos ;
y ¼ r sin ;
and
r2 ¼ x2 þ y2
ð11:6Þ
From Equation 11.5 the joint probability density functions f (r, ) and f (x, y) obey
the equation
f ðr; Þ dr d ¼ f ðx; yÞJ xy;r dr d
where the Jacobian is
J xy;r ¼
cos 
sin 
r sin 
r cos 

 ¼ r
We therefore have
f ðr; Þ ¼ rf ðx; yÞ
ð11:7Þ
Furthermore since x and y are independent N(0, 1)
f ðx; yÞ ¼ f ðxÞ f ðyÞ;
where
f ðxÞ ¼ ex2=2
ffiffiffiffiffi
2
p
and
f ðyÞ ¼ ey2=2
ffiffiffiffiffi
2
p
Therefore:
f ðr; Þ ¼ rf ðxÞf ðyÞ ¼ r ex2=2
ffiffiffiffiffi
2
p
ey2=2
ffiffiffiffiffi
2
p
which gives
f ðr; Þ ¼ r
2 eðx2þy2Þ=2 ¼ 1
2 rer2=2 ¼ f ðÞf ðrÞ
ð11:8Þ
where f () ¼ 1=2, f (r) ¼ rer2=2 are independent probability density functions.
The corresponding cumulative probability distribution functions F() and F(r) can
be found by evaluating the following integrals:
FðÞ ¼ 1
2
Z 
0
d ¼ 
2
and
FðrÞ ¼
Z r
0
rer2=2dr ¼ er2=2
h
ir
0¼ 1  er2=2
We can now use the result, see for example Evans et al. (2000), that any variate x
with a probability density function f (x), has a cumulative distribution function
F(x) ¼
R x
1 f (x)dx, which is F(x)  U(0, 1), where U(0, 1) is the uniform distribution
between 0 and 1.
The variables V0
1 ¼ F(r) ¼ 1  er2=2 and V0
2 ¼ F() ¼ =2 are therefore uni-
formly distributed on the interval (0, 1).
For convenience we will define the, U(0, 1), variables
V1 ¼ 1  V0
1 ¼ er2=2
and
V2 ¼ V0
2
230
Pricing Assets

So we have:
V1 ¼ er2=2;
V2 ¼ 
2
Therefore
log V1 ¼ r2=2;
r ¼ ð2 log V1Þ1=2;
and
 ¼ 2V2
Substituting these results into Equation 11.6 gives
x ¼ ð2 log V1Þ1=2 cos 2V2;
y ¼ ð2 log V1Þ1=2 sin 2V2
ð11:9Þ
where x and y are N(0,1).
The Box Muller method is contained in Equation 11.9, which shows that the
N(0, 1) variates are generated in pairs from the uniform distribution U(0, 1) variates
V1 and V2.
Since the N(0, 1) variates are created two at a time, if we want to generate a normal
distribution with an odd number of dimensions, nodd, it is necessary to generate
nodd þ 1 dimensions and discard one of the dimensions.
It is easy to modify Equation 11.9 so that we can specify the means (1 and 2) and
variances (2
1 and 2
2) of the generated variates x and y; this is accomplished as
follows:
The Box–Muller method
x ¼ 1ð2logV1Þ1=2 cos2V2 þ 1;
y ¼ 2ð2logV1Þ1=2 sin2V2 þ 2
ð11:10Þ
where the distributions of x and y are:
x  Nð1; 2
1Þ
and
y  Nð2; 2
2Þ
V1 and V2 are independent variates from the uniform distribution U(0,1).
Code excerpt 11.2 illustrates how to generate quasirandom normal variates with
given means and standard deviations.
long Quasi_Normal_Independent(long fcall, long seq, double xmean[], double std[], long idim, double quasi[])
{
/* Input parameters:
fcall
—
if fcall ¼¼ 1 then it is an initialisation call, if fcall ¼¼ 0 then a continuation call
seq
—
if seq ¼¼ 0 then a Faure sequence, if seq ¼¼ 1 then a Niederreiter sequence,
if seq ¼¼ 2 then a Sobol sequence
xmean[]
—
the means of the independent normal variates
std[]
—
the standard deviations of the independent normal variates
idim
—
the number of independent normal variates, idim must be less than 40
Output parameters:
quasi[]
—
the elements quasi[0], .. quasi[idim1] contain the independent normal variates
*/
long ierr, i, j;
double twopi, v1, v2, pi;
Monte Carlo simulation
231

long ind1, ind2;
#define QUASI(I) quasi[(I) 1]
#define STD(I) std[(I) 1]
#define XMEAN(I) xmean[(I) 1]
if ((idim / 2) * 2 !¼ idim){
printf(‘‘Error on entry, idim is not an even number: idim ¼ ld \n’’, idim);
return 1;
}else if (idim > 40){
printf(‘‘On entry, idim > 40: idim ¼ ld\n’’, idim);
return 1;
}
for (i ¼ 1; i <¼ idim; þþi){
if (STD(i) <¼ 0.0){
printf(‘‘On entry, the standard deviation is not greater than zero: STD(%ld) ¼ %12.4f\n’’, i,STD(i));
return 1;
}
}
pi ¼ 4.0*atan(1.0);
if (fcall){/* first call for initialisation */
if (seq ¼¼ 0){
Generate_Faure_Sequence(fcall, idim, &QUASI(1));
}
else if (seq ¼¼ 1){
Generate_Niederreiter_Sequence(fcall, idim, &QUASI(1));
}
else if (seq ¼¼ 2){
Generate_Sobol_Sequence(fcall, idim, &QUASI(1));
}
}else{/* a continuation call */
if (seq ¼¼ 0){
Generate_Faure_Sequence(fcall, idim, &QUASI(1));
}
else if (seq ¼¼ 1){
Generate_Niederreiter_Sequence(fcall, idim, &QUASI(1));
}
else if (seq ¼¼ 2){
Generate_Sobol_Sequence(fcall, idim, &QUASI(1));
}
for (i ¼ 1; i <¼ idim/2; þþi){/* generate the normal variates */
ind1 ¼ i * 2  1;
ind2 ¼ i * 2;
twopi ¼ pi * 2.0;
v1 ¼ sqrt(log(QUASI(ind1)) *  2.0);
v2 ¼ twopi * QUASI(ind2);
QUASI(ind1) ¼ XMEAN(ind1) þ STD(ind1) * v1 * cos(v2);
QUASI(ind2) ¼ XMEAN(ind2) þ STD(ind2) * v1 * sin(v2);
}
}
return 0 ;
}
Code excerpt 11.2
Generating quasirandom normal variates using the Box–Muller transformation
11.3.2
Lognormal distribution
The lognormal distribution can be generated from the normal distribution dis-
cussed in the previous section by means of a simple transformation. Here we
denote a lognormal distribution with mean m and variance s2 by ( m, s2), and if a
variate ‘  ( m, s2), then log (‘)  N(, 2), where values for  and 2 are given
below.
The lognormal density function, see Aitchison and Brown (1966), is:
f ðxÞ ¼
1
xð2Þ1=2 
 exp
ðlog x  Þ2
22
	

ð11:11Þ
232
Pricing Assets

If zi, i ¼ 1, . . . , p are independent normal variates N(i, 2
i ), i ¼ 1, . . . , p then lognor-
mal variates ‘i, i ¼ 1, . . . , p can be generated using the transformation:
‘i ¼ expðziÞ; i ¼ 1; . . . ; p
ð11:12Þ
where the mean of the ith lognormal variate is
mi ¼ exp i þ 2
i
2
	

ð11:13Þ
and the variance is
s2
i ¼ expð2i þ 2
i Þ expð2
i Þ  1


ð11:14Þ
The ratio of variance to the mean squared is therefore
s2
i
mi
mi2 ¼ expð2
i Þ  1
ð11:15Þ
or equivalently
2
i ¼ log 1 þ s2
i
mi
mi2
	

ð11:16Þ
A lognormal distribution consisting of p independent variates with means
mi, i ¼ 1, . . . , p and variances s2
i , i ¼ 1, . . . , p can thus be generated using the
following procedure.
First generate the p independent normal variates
zi  Nði; 2
i Þ;
i ¼ 1; . . . ; p
where
i ¼ logð miÞ  2
i
2
ð11:17Þ
and
2
i ¼ log 1 þ s2
i
m2
i
	

ð11:18Þ
Then create the independent lognormal variates using
‘i ¼ expðziÞ;
i ¼ 1; . . . ; p
11.3.3
Student’s t distribution
If St(, ) represents the Student’s t distribution with mean  and number of degrees
of freedom , then variates X  St(0, ) can be generated as follows:
X 
Zffiffiffiffiffiffiffiffiffi
Y=
p
ð11:19Þ
Monte Carlo simulation
233

where Z  N(0, 1), and Y  2
. The variance of X is:
E½X2 ¼

  2
Variates X0 from a Student’s t distribution having  degrees of freedom with mean
 and variance s can be generated by modifying Equation 11.19 as follows:
X0   þ
s1=2
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
=ð  2Þ
p
Zffiffiffiffiffiffiffiffiffi
Y=
p
ð11:20Þ
The probability density function, f (x), for X0 is:
f ðxÞ ¼ ðð þ 1Þ=2Þð  2Þ1=2s1=2
1=2ð=2Þ
1 þ ðx  Þ2
sð  2Þ

ðþ1Þ=2
ð11:21Þ
where  > 2.
11.4
GENERATION OF MULTIVARIATE DISTRIBUTIONS: CORRELATED
VARIATES
In this section we will show how to generate multivariate distributions with known
mean and covariance matrix. We will see later that variates from these distributions
are important in Monte Carlo option pricing methods.
Multivariate generalization of univariate distributions, see for example Mardia
et al. (1988).
11.4.1
Normal distribution
Here we consider how to generate a p variate normal distribution with a given mean
and covariance matrix.
We will denote the vector containing the variates of the ith observation from a p variate
zero mean normal distribution by Zi; that is we write a sample of n observations as
Zi  Nð0; CÞ;
i ¼ 1; . . . ; n
ð11:22Þ
where C is the p 
 p covariance matrix.
Further Zi, k is used to denote the kth element of Zi, which contains the value of the
kth variate for the ith observation.
From a computational point of view we can then consider a sample of n observa-
tions to be represented by the n 
 p matrix Z. The ith row of Z contains the values for
ith observation, and the kth column of the ith row, Zi, k, contains the value of the kth
variate for the ith observation.
Also, since the distribution has zero mean, the sample covariance matrix is given
by C ¼ ZZT. To generate variates with covariance matrix C we can use the fact that,
if the matrix C is positive definite, a Cholesky factorisation exists in which:
C ¼ AAT
ð11:23Þ
where A is lower triangular.
234
Pricing Assets

We can therefore generate p variates which have a covariance matrix C as follows.
First generate, by (for example) using the Box Muller method described in Section
11.3.1, the independent normal variates:
X  Nð0; IpÞ
where the vector X contains the p variates, Ip is the unit matrix, and XXT ¼ Ip.
Then, using the Cholseky factorisation of Equation 11.23, form
Y ¼ AX
ð11:24Þ
where Y is a p element vector.
Now since YYT ¼ AX(AX)T ¼ A(XXT)AT ¼ AAT ¼ C, we have that
Y  Nð0; CÞ
Variates that have nonzero means k, k ¼ 1, . . . , p can be obtained by simply
modifying Equation 11.24 to:
Y0 ¼ AX þ 
ð11:25Þ
where Y0 is a p variate vector that is distributed as N(, C), and the p elements of
vector  contain the means of the variates Y0
k, k ¼ 1, . . . , p.
The problem with this approach is that if the matrix C is not positive definite (this
could be caused by highly correlated variates or by rounding errors, etc.) then it is not
possible to compute the Cholesky decomposition.
An alternative method is to use the spectral decomposition of the covariance
matrix C,
C ¼ VVT
where  is a p 
 p diagonal matrix of eigenvalues i, i ¼ 1, . . . , p and the columns of
the p 
 p matrix V are the corresponding eigenvectors.
We can therefore write
C ¼ V1=2T=2VT ¼ AAT
where A ¼ V1=2, and 1=2 ¼
ffiffiffiffi
i
p
, is the square root of the ith eigenvalue.
Equation 11.24 is then:
Y ¼ V1=2X
ð11:26Þ
and Equation 11.25 is
Y0 ¼ V1=2X þ 
ð11:27Þ
If the matrix C is not positive definite then some (say p  r) of the eigenvalues will
be negative. We can construct an approximation to the covariance matrix Cr  C
using only the r positive eigenvalues as follows:
Cr ¼ VrrVT
r ¼ Vr1=2
r
T=2
r
VT
r
where Cr is a p 
 p matrix, Vr is a p 
 r matrix and r is a r 
 r matrix.
Monte Carlo simulation
235

Under these circumstances the p element vectors Y and Y0 are generated using the
following modified versions of Equations 11.26 and 11.27
Y ¼ Vr1=2
r
Xr
and
Y0 ¼ Vr1=2
r
Xr þ 
ð11:28Þ
where the r element vector Xr is just a subset of the p element vector X. A function to
generate correlated normal and lognormal variates is given in Code excerpt 11.3.
long Quasirandom_Normal_LogNormal_Correlated(long fcall, long seq, long lnorm, double means[], long n,
double c[], long tdc, double tol, long *irank, double x[], double work[],long lwk){
/* Input parameters:
fcall
—
if fcall ¼¼ 1 then it is an initialisation call, if fcall ¼¼ 0 then a continuation call
seq
—
if seq ¼¼ 0 then a Faure sequence, if seq ¼¼ 1 then a Niederreiter sequence,
if seq ¼¼ 2 then a Sobol sequence
lnorm
—
if lnorm ¼¼ 1 then it is a lognormal distribution, if lnorm ¼¼ 0 then a normal distribution
n
—
the number of variates, n must be less than 40
c[]
—
a matrix which contains the required covariance matrix, C
tdc
—
the second dimension of the matrix C
tol
—
the tolerance used for calculating the rank of the covariance matrix C
means[]
—
the means of the independent normal variates
std[]
—
the standard deviations of the independent normal variates
lwk
—
the size of the work array, work
Output parameters:
rank
—
the computed rank of the covariance matrix C
x[]
—
the elements x[0], .. x[n 1] contain the variates
Input/Output parameters:
work
—
a work array
*/
double zero ¼ 0.0, one ¼ 1.0, two ¼ 2.0;
long n1, i, j, k, kk;
double mtol, alpha;
long ptrc, ptre, ptrv, ptrw, ptrw0, ptrw1;
#define C(I,J) c[((I) 1) * tdc þ ((J) 1)]
#define MEANS(I) means[(I) 1]
#define X(I) x[(I) 1]
#define WORK(I) work[(I) 1]
if (lwk < (2 þ 3*n þ 2*n*n þ 3)){
printf (‘‘Error lwk is too small \n’’);
return 1;
}
ptre ¼ 2;
ptrv ¼ nþ 2;
ptrw ¼ n*n þ n þ 2;
/* add extra 1 to allow for odd values of n */
ptrw0 ¼ ptrw þ 1 þ n;
ptrw1 ¼ ptrw0 þ 1 þ n;
ptrc ¼ ptrw1 þ n þ 1;
n1 ¼ n;
if (((n/2)*2) !¼ n){/* test for odd n */
n1 ¼ n þ 1;
}
if (fcall){/* first call for initialisation */
if (lnorm){/* lognormal distribution */
for (i ¼ 1; i <¼n; þþi){/* Load the modified covariance matrix into WORK */
for (j ¼ 1; j <¼ n; þþj){
WORK(ptrcþ(i 1)*nþj 1) ¼ log(one þ C(i,j)/(MEANS(i)*MEANS(j)));
}
}
}
else{/* normal distribution */
for (i ¼ 1; i <¼ n; þþi){/* Load the covariance matrix into WORK */
for (j ¼ 1; j <¼ n; þþj){
WORK(ptrcþ(i 1)*nþj  1) ¼ C(i,j);
}
236
Pricing Assets

}
}
/* calculate the eigenvalues and eigenvector of the matrix that has been loaded into WORK */
calc_eigvals_eigvecs (n,&WORK(ptrc),n,&WORK(ptre),&WORK(ptrv),n); /*ThecodeusesNAGroutinef02abc*/
*irank ¼ 0;
/*
printf (‘‘The eigenvalues are \ n’’);
for (j¼n; j >¼ 1; j){
printf (‘‘%12.5f \n’’, WORK(ptreþj 1));
}
*/
for (j¼n; j >¼ 1; j){/* use the eigenvalues to calculate the rank of the matrix */
if (WORK(ptreþj 1) < tol) goto L24;
*irank ¼ *irank þ 1;
}
printf (‘‘*irank ¼ %ld \n’’,*irank);
L24:
mtol ¼ tol;
if (WORK(ptre) < mtol){
printf (‘‘Warning there is an eigenvalue less than %12.4f \n’’,mtol);
}
for (j¼1; j <¼ *irank; þþj){
kk ¼ 1;
for (k¼1; k <¼n; þþk){
if(WORK(ptrvþ(k 1)*nþ(j 1)) !¼ zero) goto L28;
kk ¼ kk þ 1;
}
L28:
/* ensure that all eigenvectors have the same sign on different machines */
alpha ¼ sqrt(WORK(ptreþj 1));
if (WORK(ptrvþ(kk 1)*nþ(j 1)) < zero) alpha ¼ sqrt(WORK(ptreþj 1));
for (i ¼ 1; i <¼ n; þþi){
WORK(ptrvþ(j 1)þ(i 1)*n)¼ WORK(ptrvþ(j 1)þ(i 1)*n)*alpha;
}
}
/*
printf (‘‘The eigenvectors are \n’’);
for (j¼1; j <¼ *irank; þþj){
for (i ¼ 1; i <¼ n; þþi){
printf (‘‘%10.5f ’’, WORK(ptrvþ(j 1)þ(i 1)*n));
}
printf (‘‘\n’’);
}
*/
for (i ¼ 1; i <¼n; þþi){/* store a vector of ones and zeros for generating the quasi-random numbers */
WORK(ptrw0þi 1) ¼ zero;
WORK(ptrw1þi 1) ¼ one;
}
for (i ¼ n; i <¼ n1; þþ i){
WORK(ptrw0þi 1) ¼ zero;
WORK(ptrw1þi 1) ¼ one;
}
}/* end of first call section */
/* generate a vector of n1 random variables from a standard normal distribution, zero mean and unit variance */
Quasi_Normal_Independent(fcall, seq, &WORK(ptrw0), &WORK(ptrw1), n1, &WORK(ptrw));
/* printf (‘‘The quasi random numbers are:\n’’);
for (i ¼ 1; i <¼ n; þþi){
printf (‘‘%12.4f \n’’, WORK(ptrwþ(i 1)));
}
*/
/* Now generate variates with the specified mean and variance */
if (lnorm){/* a lognormal distribution */
for (i ¼ 1; i <¼ n; þþi){
X(i) ¼ log(MEANS(i))  WORK(ptrcþ(i 1)*nþi 1)/two;
for (k ¼ 1; k <¼ *irank; þþk){
X(i)¼X(i)þWORK(ptrvþ(k 1)þ(i 1)*n)* WORK(ptrwþk 1);
}
}
for (i ¼ 1; i <¼ n; þþi){
X(i) ¼ exp(X(i));
}
}
else{/* a normal distribution */
for (i ¼ 1; i <¼ n; þþi){
X(i) ¼ MEANS(i);
for (k ¼ 1; k <¼ * irank; þþk){
X(i)¼X(i)þWORK(ptrvþ(k 1)þ(i 1)*n)* WORK(ptrwþk 1);
Monte Carlo simulation
237

}
}
}
/*
printf (‘‘The generated variates are:\n’’);
for (i ¼ 1; i <¼ n; þþi){
printf (‘‘ %12.4f \n’’, X(i));
}
*/
return 0;
}
Code excerpt 11.3
The functions Quasirandom_Normal_LogNormal Correlated which generates
correlated quasirandom normal variates and correlated quasirandom lognormal variates
In order to visualize the effect of the covariance matrix we will display the results
of using function Quasirandom_Normal_LogNormal_ Correlated to gener-
ate the following variates:
. A vector of three normal independent variates with covariance matrix:
C1 ¼
1:0
0:0
0:0
0:0
1:0
0:0
0:0
0:0
1:0
0
@
1
A
. A vector of three normal variates in which the elements of the covariance matrix
are all positive; the covariance matrix is:
C2 ¼
1:0
0:8
0:8
0:8
1:0
0:8
0:8
0:8
1:0
0
@
1
A
. A vector of three normal variates in which two elements of the covariance matrix
are negative; the covariance matrix is:
C3 ¼
1:0
0:7
0:2
0:7
1:0
0:2
0:2
0:2
1:0
0
@
1
A
In all cases the mean vector is given by:
 ¼
2:0
2:0
2:0
0
@
1
A
The results are displayed in Figures 11.7 to 11.9.
11.4.2
Lognormal distribution
The multivariate lognormal distribution is important because it is the asset returns
distribution assumed by the Black–Scholes equation. We will denote a p variate
vector L which has a lognormal distribution with p element mean vector m and
p 
 p covariance matrix S as:
L  ð m; SÞ
238
Pricing Assets

15
15
10
10
5
5
0
0
–5
–5
–10
–10
Figure 11.7
Scatter diagram for a sample of 3000 observations (Zi, i ¼ 1, . . . , 3000) generated from a
multivariate normal distribution consisting of three variates with covariance matrix C1 and mean . Here
we plot the values of the first variate against the values of the second variate. If we use the notation of
Equation 11.22, then the (x, y) co-ordinates for the points are xi ¼ Zi, 1, i ¼ 1, . . . , 3000 and
yi ¼ Zi, 2, i ¼ 1, . . . , 3000
15
15
10
10
5
5
0
0
–5
–5
–10
–10
Figure 11.8
Scatter diagram for a sample of 3000 observations (Zi, i ¼ 1, . . . , 3000) generated from a
multivariate normal distribution consisting of three variates with covariance matrix C2 and mean . Here
we plot the values of the first variate against the values of the second variate. If we use the notation of
Equation 11.22, then the (x, y) co-ordinates for the points are xi ¼ Zi, 1, i ¼ 1, . . . , 3000 and
yi ¼ Zi, 2, i ¼ 1, . . . , 3000
Monte Carlo simulation
239

This means that:
logðLÞ  Nð; Þ
where  is a p element vector and  is a p 
 p matrix. It can be shown that
i; j ¼ log 1 þ Si; j
mi mj
	

ð11:29Þ
and
i ¼ logð miÞ  i;i
2 ;
i ¼ 1; . . . ; p,
and
j ¼ 1; . . . ; p
ð11:30Þ
For the case of independent variates we then have:
i ¼ logð miÞ  2
i
2 ;
i ¼ 1; . . . ; p
and
i;i ¼ 2
i ¼ log 1 þ s2
i
m2
i
	

;
i ¼ 1; . . . ; p,
and
for i 6¼ j;
i; j ¼ 0
which are just Equations 11.17 and 11.18 given in Section 11.3.2.
15
15
10
10
5
5
0
0
–5
–5
–10
–10
Figure 11.9
Scatter diagram for a sample of 3000 observations (Zi, i ¼ 1, . . . , 3000) generated from a
multivariate normal distribution consisting of three variates with covariance matrix C3 and mean . Here
we plot the values of the first variate against the values of the second variate. If we use the notation of
Equation 11.22, then the (x, y) co-ordinates for the points are xi ¼ Zi, 1, i ¼ 1, . . . , 3000 and
yi ¼ Zi, 2, i ¼ 1, . . . , 3000
240
Pricing Assets

Code excerpt 11.4 shows how to generate a multivariate lognormal distribution
with a given mean m and covariance matrix S. More complete information can be
found in the function Quasirandom_Normal_LogNormal_Correlated which
is provided in Code excerpt 11.3.
double sig[40][40], s[40][40]; /* limit of 40 */
double means[40], x[40], lx[40], tmp;



#define S(I,J) s[(I) 1][(J) 1]
#define SIG(I,J) sig[(I) 1][(J) 1]
#define MEANS(i) means[(I) 1] /* the means of the lognormal distribution */
#define X(I) x[(I) 1] /* normal variates */
#define LX(I) lx[(I) 1] /* lognormal variates */



/* obtain the Gaussian covariance matrix SIG, that corresponds to the lognormal
covariance matrix S. */
for (i¼ 1; i <¼ m; þþi) {
for (j¼1; j <¼ m; þþj) {
tmp ¼ MEANS(i) * MEANS(j);
SIG(i,j) ¼ log( 1 þ (S(i,j)/tmp));
}
}



/* Generate multivariate Gaussian variates X(i), i ¼ 1, . . . ,m, with zero mean
and covariance matrix SIG, using section .. */



/* Generate normal variates with the correct mean */
for (i¼ 1; i <¼ m; þþi) {
X(i) ¼ X(i) þ log(MEANS(i))  SIG(i,i)/2;
}
/* Now exponentiate to create lognormal lognormal variates with mean
XMEAN, and covariance matrix S */
for (i¼1; i <¼ m; þþi) {
LX(i) ¼ exp(X(i));
}
Code excerpt 11.4
Illustrating how to generate variates from a lognormal distribution with a given mean
an covariance matrix
11.4.3
Student’s t distribution
See Dickey (1967), Anderson (1984), and also Glasserman et al. (2000). Here we
show how to generate observations from a multivariate Student’s t distribution.
The probability density function, f (x), for the p variate multivariate Student’s t
distribution with covariance matrix C is:
f ðxÞ ¼ ððm þ Þ=2Þð  2Þ1=2jCj1=21=2
ðÞm=2ð=2Þ
1 þ xTC1x
ð  2Þ

ðmþÞ=2
ð11:31Þ
where C represents the determinant of C, and  > 2.
Let  be a matrix with spectral decomposition  ¼ VVT and T be a vector of p
independent Student’s t variates, each with  degrees of freedom. Then the vector
To ¼ V1=2T has a multivariate Student’s t distribution with zero mean and a
covariance matrix of C ¼ =(  2). So if we want to generate a p variate vector
Monte Carlo simulation
241

T from a multivariate Student’s t distribution with mean vector  and covariance
matrix C we do the following:
Create a scaled covariance matrix
B ¼ C ð  2Þ

Perform the spectral decomposition
B ¼ VVT
Then use the results of Section 11.3.3 to obtain a p variate vector T of independ-
ent Student’s t variates and generate the required vector as
T ¼  þ V1=2T
ð11:32Þ
A multivariate sample of n observations will be denoted by Ti, i ¼ 1, . . . , n, and the
value of the kth variate for the ith observation will be denoted by Ti, k.
Of course, as in Section 11.4.1, we can if required choose to use only r eigenvalues
and eigenvectors. In these circumstances the Equation 11.32 becomes:
T ¼  þ Vr1=2
r
T
r
ð11:33Þ
where Vr is a p 
 r matrix, 1=2
r
is an r 
 r diagonal matrix and the r element vector
T
r is just a subset of vector T.
SUBROUTINE STDENT(FCALL,IGEN,ISEED,RWSAV, MEANS,DF,N,C,LDC,TOL,IRANK, X,WORK,LWK,IFLAG)
IMPLICIT NONE
INTEGER N1,I,J,K,KK,N,LDC,IFLAG,LWK,IRANK
DOUBLE PRECISION ZERO, ONE, TWO
PARAMETER (ZERO ¼ 0.0D0, ONE ¼ 1.0D0, TWO ¼ 2.0D0)
LOGICAL FCALL
DOUBLE PRECISION MEANS(N), RWSAV(9)
DOUBLE PRECISION WORK(LWK)
DOUBLE PRECISION TOL,C(N,N),X(N)
DOUBLE PRECISION MTOL,ALPHA,RND,DF,FAC
INTEGER PTRC,PTRE,PTRV,PTRW,PTRW0,PTRW1
INTEGER IFLAGX, ISEED(4), IGEN
DOUBLE PRECISION G05HKW
EXTERNAL F02ABZ, G05YBF, G05HKW
INTRINSIC SQRT, EXP, LOG
IF (LWK.LT.(2 þ 3*Nþ 2*N*Nþ 3)) THEN
PRINT*,’ERROR: LWK IS TOO SMALL’
END IF
PTRE ¼ 2
PTRV ¼ Nþ 2
PTRW ¼ N*N þ N þ 2
* ADD EXTRA 1 TO ALLOW FOR ODD VALUES OF N
PTRW0 ¼ PTRW þ 1 þ N
PTRW1 ¼ PTRW0 þ 1 þ N
PTRC ¼ PTRW1 þ N þ 1
N1 ¼ N
* TEST FOR ODD N
IF (((N/2)*2).NE.N) THEN
N1 ¼ N þ 1
END IF
IF (FCALL) THEN
RWSAV(1) ¼
1.0D0
RWSAV(2) ¼  1.0D0
242
Pricing Assets

RWSAV(3) ¼
0.0D0
RWSAV(4) ¼
0.0D0
RWSAV(5) ¼
0.0D0
RWSAV(6) ¼
0.0D0
RWSAV(7) ¼
0.0D0
RWSAV(8) ¼
0.0D0
RWSAV(9) ¼
0.0D0
FAC ¼
(DF  TWO)/DF
* SCALE THE COVARIANCE MATRIX BY FAC TO PRODUCE THE EQUIVALENT SIGMA MATRIX
DO 10 I ¼ 1, N
DO 11 J ¼ 1, N
WORK(PTRCþ(I 1)*NþJ 1) ¼ C(I,J)*FAC
11
CONTINUE
10
CONTINUE
CALL F02ABZ(WORK(PTRC),N,N,WORK(PTRE),WORK(PTRV), N,WORK(PTRW),IFLAGX)
*
PRINT*,’THE EIGENVALUES ARE:’
*
DO 3323 J ¼ N, 1,  1
*
PRINT*, J, WORK(PTREþJ 1)
* 3323 CONTINUE
IRANK ¼ 0
DO 23 J ¼ N, 1,  1
IF(WORK(PTREþ J  1).LT.TOL) GOTO 24
IRANK ¼ IRANK þ 1
23
CONTINUE
24
CONTINUE
*
PRINT*,’POINT A THE EIGENVECTORS:’
*
DO 627 J ¼ 1, IRANK
*
WRITE(*,’(10F10.5)’) (WORK(PTRVþ((J 1)*N)þ I 1),I ¼ 1,N)
* 627
CONTINUE
MTOL ¼TOL
IF (WORK(PTRE).LT.MTOL) THEN
PRINT*,’WARNING THERE IS AN EIGENVALUE LESS THAN ’,MTOL
END IF
DO 25 J ¼ 1, IRANK
KK ¼ 1
DO 27 K ¼ 1, N
IF(WORK(PTRVþ K 1þ(J 1)*N).NE.ZERO) GOTO 28
KK ¼ KK þ 1
27
CONTINUE
28
CONTINUE
* ENSURE THAT ALL EIGENVECTORS HAVE THE SAME SIGN ON DIFFERENT MACHINES
ALPHA ¼ SQRT(WORK(PTRE þ J  1))
IF (WORK(PTRV þ KK  1þ(J 1)*N).LT.ZERO)
*
ALPHA ¼  SQRT (WORK (PTRE þJ  1))
DO 29 I ¼ 1, N
WORK (PTRV þ((J  1 )*N )þI 1)¼ WORK (PTRV þ((J 1)*NþI 1)) *ALPHA
29
CONTINUE
25
CONTINUE
*
PRINT*,’THE EIGENVECTORS:’
*
DO 625 J ¼ 1, IRANK
*
WRITE(*,’(10F10.5)’) (WORK(PTRV þ((J 1)*N) þ I 1),I ¼ 1,N)
*625
CONTINUE
END IF
* GENERATE A VECTOR OF N1 INDEPENDENT RANDOM VARIABLES FROM A STUDENT’S T DISTRIBUTION AND STORE THEN IN
VECTOR WORK(PTRW)
IFLAGX ¼ 0
DO 222 I ¼ 0, N1  1
WORK(PTRW þ I) ¼ G05HKW(DF,IGEN, ISEED,RWSAV, IFLAGX)
*
PRINT*,’WORKPTRW þ I) ¼ ’,WORK(PTRW þ I)
222
CONTINUE
IFLAG ¼ IFLAGX
DO 133 I ¼ 1, N
X(I) ¼ MEANS(I)
DO 134 K ¼ 1, IRANK
X(I)¼ X(I)þWORK(PTRV þ((K 1)*N) þ I 1) *WORK(PTRW þ K  1)
134
CONTINUE
133
CONTINUE
END
Code excerpt 11.5
The Fortran 77 function STDENT which generates correlated variates from
a Student’s t distribution
Monte Carlo simulation
243

In order to visualize the effects of both the covariance matrix and the number of
degrees of freedom, , we display results from using the function STDENT to generate
the following variates:
. Three Student’s t variates with covariance matrices C1, C2, C3, mean  and
 ¼ 25:5.
. Three Student’s t variates with covariance matrices C1, C2, C3, mean  and
 ¼ 4:5.
The values of , C1, C2, and C3 are those previously defined in Section 12.4.1.
The results are displayed in Figures 11.10 to 11.13. It can be seen that when
 ¼ 25:5 the distribution of points is very similar to that for the normal distribution;
for example compare Figure 11.7 with Figure 11.3. However, for  ¼ 4:5, the
Student’s t variates have more points in the tail of the distribution than the corres-
ponding normal variates. This has applications in finance where asset return dis-
tributions have been found to exhibit such effects.
15
10
5
5
0
0
–5
–10
15
10
–5
–10
Figure 11.10
Scatter diagram for a sample of 3000 observations (Ti, i ¼ 1, . . . , 3000) generated from a
multivariate Student’s t distribution consisting of three variates with covariance matrix C3, number of
degrees of freedom  ¼ 4:5 and mean , see Section 11.4.1. Here we plot the values of the first variate
against the values of the second variate. The (x, y) co-ordinates for the points are therefore
xi ¼ Ti,1, i ¼ 1, . . . , 3000 and yi ¼ Ti, 2, i ¼ 1, . . . , 3000
244
Pricing Assets

15
15
10
10
5
5
0
0
–5
–5
–10
–10
Figure 11.11
Scatter diagram for a sample of 3000 observations (Ti, i ¼ 1, . . . , 3000) generated from a
multivariate Student’s t distribution consisting of three variates with covariance matrix C1, number of
degrees of freedom  ¼ 4:5 and mean . Here we plot the values of the first variate against the values of the
second variate. The (x, y) co-ordinates for the points are therefore xi ¼ Ti,1, i ¼ 1, . . . , 3000 and
yi ¼ Ti,2, i ¼ 1, . . . , 3000
15
15
10
10
5
5
0
0
–5
–5
–10
–10
Figure 11.12
Scatter diagram for a sample of 3000 observations (Ti, i ¼ 1, . . . , 3000) generated from a
multivariate Student’s t distribution consisting of three variates with covariance matrix C3, number of
degrees of freedom  ¼ 25:5 and mean , see Section 11.4.1. Here we plot the values of the first variate
against the values of the second variate. The (x, y) co-ordinates for the points are therefore
xi ¼ Ti,1, i ¼ 1, . . . , 3000 and yi ¼ Ti,2, i ¼ 1, . . . , 3000
Monte Carlo simulation
245

15
15
10
10
5
5
0
0
–5
–5
–10
–10
Figure 11.13
Scatter diagram for a sample of 3000 observations (Ti, i ¼ 1, . . . , 3000) generated from a
multivariate Student’s t distribution consisting of three variates with covariance matrix C1, number of
degrees of freedom  ¼ 25:5 and mean , see Section 11.4.1. Here we plot the values of the first variate
against the values of the second variate. The (x, y) co-ordinates for the points are therefore
xi ¼ Ti, 1, i ¼ 1, . . . , 3000 and yi ¼ Ti, 2, i ¼ 1, . . . , 3000
246
Pricing Assets

Chapter 12
Multiasset European and American options
12.1
INTRODUCTION
In this section we consider the valuation of multiasset, basket, options within the
Black–Scholes pricing framework. Here we will show how to price options on the
maximum and minimum value of the assets in a basket using:
. Analytic methods
. Monte Carlo methods
. Multidimensional lattices.
Analytic methods can be useful for pricing multiasset European options which
have a known closed form solution. They are particularly appropriate for low
dimensional European options, when the closed form expressions are not too diffi-
cult to evaluate.
Monte Carlo methods have the advantage that they can easily compute the value
of multiasset European options, but have difficultly including the possibility of early
exercise; this is required for American style options.
On the other hand multidimensional lattice techniques allow American options to
be evaluated with ease. However lattices become increasingly difficult to program as
the number of dimensions increases, and the constraint of computer storage limit
their use to problems involving (about) four or less assets.
12.2
THE MULTIASSET BLACK–SCHOLES EQUATION
In Section 8.3 we showed that when the price, S, of a single asset follows GBM the
change in price, dS, over a time interval, dt, is given by:
dS ¼ rSdt þ SdX
where r is the risk free interest rate,  is the volatility of asset S, and dX is drawn from
a normal distribution with mean zero and variance dt.
We also proved, see Equation 8.14 of Section 8.3, using Ito’s lemma that the
process followed by Y ¼ log (S) is:
dY ¼ ðr  2=2Þdt þ dX
where dY is the change in the value of log (S) over the time interval dt. Later on, in
Section 9.3.1, we derived the (Black–Scholes) partial differential equation that is

satisfied by the value, V, of an option written on a single underlying asset follows
GBM; this equation is:
@V
@t þ 2S2
2
@2V
@S2 þ rS @V
@S  rV ¼ 0
The above results for a single asset can be generalized to deal with multiasset
options. For m assets we have the following processes:
dYi ¼ ðr  2
i =2Þdt þ idXi;
i ¼ 1; . . . ; m
ð12:1Þ
where the subscript i refers to the value associated with the ith asset. We can also
write the above equation in vector form by introducing the m element vector dY
which is normally distributed as:
dY  Nð; CÞ
ð12:2Þ
where  is the mean vector and C is the covariance matrix. The elements of the
covariance matrix are:
Cii ¼ 2
i dt;
i ¼ 1; . . . ; m;
Cij ¼ ijij dt;
i 6¼ j; i ¼ 1; . . . ; m; j ¼ 1; . . . ; m
ð12:3Þ
where ij is the correlation coefficient between assets i and j. The elements of the
mean vector  are:
i ¼ r  2
i =2;
i ¼ 1; . . . ; m
ð12:4Þ
The value V of an option written on n assets satisifies the following partial differential
equation:
@V
@t þ 1
2
X
m
i¼1
X
m
j¼1
ijijSiSj @2V
@Si@Sj
þ r
X
m
i¼1
Si @V
@Si
 rV ¼ 0
For a European call on the maximum of m assets the payoff PMAX
c
at maturity (time
) is given by PMAX
c
¼ max ( max (S
1, S
2, . . . , S
m)  E, 0), where S
i , i ¼ 1, . . . , m
denotes the value of the ith asset at maturity, and E represents the strike price.
Similarly a European put option on the minimum of m assets has a payoff, PMIN
p
, at
time , given by PMIN
p
¼ max (E  min (S
1, S
2, . . . , S
m), 0).
12.3
MULTIDIMENSIONAL MONTE CARLO METHODS
We have already mentioned that Monte Carlo simulation can easily price European
multiasset options (also sometimes referred to as basket options or rainbow options)
involving a large number of assets (say 20 or more).
248
Pricing Assets

In addition Monte Carlo simulation can also include the following features into a
option without much difficulty:
. NonGaussian distribution of stock returns; distributions with heavy tails are
usually of interest because they more accurately represent what is observed in the
financial markets.
. Options with path dependency (such as barrier options, etc.); these are known as
exotic options.
. Complex time dependency (e.g. ARMA, GARCH, or Levy processes) of model
parameters such as interest rates, asset prices, etc.
The main drawbacks with Monte Carlo simulation are:
. It is difficult to compute the value of American style options.
. It is difficult (or impossible) to achieve the same accuracy that can be obtained
using finite-difference methods.
In a different section of this book we will show how Monte Carlo simulation can
be used to price American options by using a hybrid Monte Carlo lattice approach
originally developed by Boyle et al. (1997).
In Chapter 11 we showed that when pseudorandom numbers are used the standard
errors of integrals computed via Monte Carlo simulation decrease at the rate N1=2,
where N is the number of simulations. This means that it can require hundreds of
thousands of simulations just to achieve an accuracy of 101 or 102 in the estimated
option price. It is because of this that various Monte Carlo variance reduction
techniques are used to increase the accuracy of the computed integral.
In this section we show how to price a three asset basket option using Monte Carlo
simulation; the accuracy of the results obtained with quasirandom numbers and
pseudorandom numbers is compared.
The options we consider are European put and call options on the maximum and
minimum of three assets. All the options have a maturity of one year, and the other
model parameters used are given in Tables 12.1 and 12.2.
In Code excerpt 12.1 most of the work is done by the routine Quasirandom_
Normal_LogNormal_Correlated, which was described in Section 11.4.1.
This generates a vector of multivariate quasirandom numbers with a particular
covariance matrix. In the program the values of the assets at current time, t are
S1 ¼ S2 ¼ S3 ¼ 100. To compute the asset prices when the option matures, at
T ¼ 1, we make use of Equation 12.1.
Another way of writing Equation 12.1 is
dYi ¼ logðSi;tþdtÞ  logðSi;tÞ ¼ r  2
i =2


dt þ idXi;
i ¼ 1; . . . ; m
where we have used the notation Si, t to denote the value of the ith asset at current
time t, and Si, tþdt to denote the value of the asset at the future time t þ dt. Simple
rearrangement of the above equation gives:
log Si;tþdt
Si;t


¼ r  2
i =2


dt þ idXi;
i ¼ 1; . . . ; m
Multiasset European and American options
249

Taking exponentials of both sides we obtain:
Si;tþdt
Si;t
¼ exp
r  2
i =2


dt þ idXi


;
i ¼ 1; . . . ; m
which is equivalent to:
Si;tþdt ¼ Si;t exp
r  2
i =2


dt þ idXi


ð12:5Þ
.. Header files etc ..
/* Monte Carlo simulation: 3 dimensional Black–Scholes, The results are compared with those of Boyle
et al.,1989 George Levy: 2003
*/
_ _cdecl main()
{
long i,seed, skip, m, lwk, irank, num_simulations;
double sqrt_T, zero ¼ 0.0,half¼ 0.5, r, opt_val;
Table 12.1
The computed values and absolute errors, in brackets, for European options on the maximum
of three assets. Monte Carlo simulation was used with both quasirandom (Sobol) sequences and
pseudorandom sequences. The number of paths used varied from 500 to 3000. The parameters were:
E ¼ 100:0, S1 ¼ S2 ¼ S3 ¼ 100:0, r ¼ 0:1,  ¼ 1:0, 1 ¼ 2 ¼ 3 ¼ 0:2, 12 ¼ 13 ¼ 23 ¼ 0:5,
q1 ¼ q2¼ q3 ¼ 0:0. The accurate values were 0.936 for a put and 22.672 for a call, see Table 12.7
of Section 12.6 and Table 2 of Boyle, Evnine, and Gibbs (1989)
Put
Call
nsim
Quasi
Pseudo
Quasi
Pseudo
500
0.890 ð4:5948 	 102Þ
1.1044 ð1:6839 	 101Þ
22.629 ð4:3231 	 102Þ
22.4089 ð2:6312 	 101Þ
1000
0.924 ð1:1534 	 102Þ
1.0193 ð8:3297 	 102Þ
22.683 ð1:1306 	 102Þ
22.3520 ð3:1998 	 101Þ
1500
0.919 ð1:6807 	 102Þ
0.8957 ð4:0344 	 102Þ
22.670 ð2:2954 	 103Þ
22.6346 ð3:7430 	 102Þ
2000
0.932 ð4:3221 	 103Þ
0.8995 ð3:6488 	 102Þ
22.685 ð1:3299 	 102Þ
22.7675 ð9:5491 	 102Þ
2500
0.932 ð3:5698 	 103Þ
0.8886 ð4:7352 	 102Þ
22.670 ð1:6619 	 103Þ
22.9326 ð2:6058 	 101Þ
3000
0.937 ð1:1376 	 103Þ
0.9025 ð3:3548 	 102Þ
22.679 ð7:2766 	 103Þ
22.8050 ð1:3301 	 101Þ
Table 12.2
The computed values and absolute errors, in brackets, for European options on the minimum
of three assets. Monte Carlo simulation was used with both quasirandom (Sobol) sequences and
pseudorandom sequences. The number of paths used varied from 500 to 3000. The parameters were:
E ¼ 100:0, S1 ¼ S2 ¼ S3 ¼ 100:0, r ¼ 0:1,  ¼ 1:0, 1 ¼ 2 ¼ 3 ¼ 0:2, 12 ¼ 13 ¼ 23 ¼ 0:5,
q1 ¼ q2 ¼ q3 ¼ 0:0. The accurate values were 7.403 for a put and 5.249 for a call, see Table 12.8 of
Section 12.6 and Table 2 of Boyle, Evnine, and Gibbs (1989)
Put
Call
nsim
Quasi
Pseudo
Quasi
Pseudo
500
7.365 ð3:8122 	 102Þ
7.6760 ð2:7298 	 101Þ
5.312 ð6:3431 	 102Þ
5.3086 ð5:9591 	 102Þ
1000
7.425 ð2:1554 	 102Þ
7.7607 ð3:5772 	 101Þ
5.293 ð4:3958 	 102Þ
5.4376 ð1:8857 	 101Þ
1500
7.408 ð5:1232 	 103Þ
7.5654 ð1:6240 	 101Þ
5.253 ð4:0761 	 103Þ
5.4121 ð1:6307 	 101Þ
2000
7.399 ð3:6364 	 103Þ
7.4820 ð7:8995 	 102Þ
5.266 ð1:7236 	 102Þ
5.4029 ð1:5390 	 101Þ
2500
7.407 ð4:1463 	 103Þ
7.3592 ð4:3754 	 102Þ
5.267 ð1:7707 	 102Þ
5.4690 ð2:2005 	 101Þ
3000
7.400 ð2:7166 	 103Þ
7.3997 ð3:3236 	 103Þ
5.245 ð3:5024 	 103Þ
5.4331 ð1:8407 	 101Þ
250
Pricing Assets

double T, the_max, the_min, E, ST1, ST2, ST3, S1, S2, S3;
double disc, sumit_max_put, sumit_max_call, sumit _min_put, sumit_min_call;
double *rvec ¼ (double *)0, rho_12, rho_13, rho_23;
double *c3, *z, *means, tol, *work, tmp1, tmp2, sigma1, sigma2, sigma3;
long lnorm, seq, fcall;
#define MEANS(I) means[(I) 1]
#define WORK(I) work[(I) 1]
#define Z(I) z[(I) 1]
#define C3(I,J) c3[((I) 1) * 3 þ ((J) 1)]
m ¼ 3; // the number of assets
lwk ¼ 100000;
c3 ¼ (double*)malloc((size_t)(sizeof(double)*3*3));
means ¼ (double *)malloc((size_t)(sizeof(double)*3));
z ¼ (double *)malloc((size_t)(sizeof(double)*3));
work¼(double*)malloc((size_t)(sizeof(double)*lwk));
if ((!means) || (!z) || (!work)) {
printf(‘‘Allocation error \n’’);
}
T ¼ 1.0;
// the maturity of the options
r ¼ 0.1;
// the riskless interest rate
sqrt_T ¼ sqrt(T);
disc ¼ exp(r*T);
tol ¼ 1.0e  8;
skip ¼ 1000;
sigma1 ¼ 0.2;
// the volatility of asset 1
sigma2 ¼ 0.2;
// the volatility of asset 2
sigma3 ¼ 0.2;
// the volatility of asset 3
S1 ¼ 100.0;
// the current price of asset 1
S2 ¼ 100.0;
// the cuurent price of asset 2
S3 ¼ 100.0;
// the current price of asset 3
E ¼ 100.0;
// the strike price
rho_12 ¼ 0.5;
// the correlation coefficient between asset 1 and asset 2
rho_13 ¼ 0.5;
// the correlation coefficient between asset 1 and asset 3
rho_23 ¼ 0.5;
// the correlation coefficient between asset 2 and asset 3
C3(1,1) ¼ sigma1*sigma1*T;
// set the elements of the covariance matrix
C3(2,2) ¼ sigma2*sigma2*T;
C3(3,3) ¼ sigma3*sigma3*T;
C3(1,2) ¼ sigma1*sigma2*T*rho_12;
C3(2,3) ¼ sigma2*sigma3*T*rho_23;
C3(1,3) ¼ sigma1*sigma3*T*rho_13;
C3(2,1) ¼ C3(1,2);
C3(3,1) ¼ C3(1,3);
C3(3,2) ¼ C3(2,3);
MEANS(1) ¼ (r  sigma1*sigma1*half)*T;
MEANS(2) ¼ (r  sigma2*sigma2*half)*T;
MEANS(3) ¼ (r  sigma3*sigma3*half)*T;
printf (‘‘THREE ASSET OPTIONS USING QUASIRANDOM NUMBERS \n’’);
fcall ¼ 1;
// initialisation call
seq ¼ 2;
// use Sobol sequences
lnorm ¼ 0;
// generate a normal distribution
Quasirandom_Normal_LogNormal_Correlated(fcall, seq, lnorm, &MEANS(1), m, &C3(1,1), m, tol, &irank,
&Z(1), &WORK(1), lwk);
fcall ¼ 0;
// continuation call
sumit_max_put ¼ zero;
sumit_max_call ¼ zero;
sumit_min_put ¼ zero;
sumit_min_call ¼ zero;
num_simulations ¼ 3000; // the number of simulations to use
for (i ¼ 1; i < ¼ num_simulations ; þþi) {
Quasirandom_Normal_LogNormal_Correlated(fcall, seq, lnorm,&MEANS(1), m,&C3(1,1), m, tol, & irank, &Z(1),
&WORK(1), lwk);
ST1 ¼ S1*exp(Z(1));
// the price of asset 1 at option maturity
ST2 ¼ S2*exp(Z(2));
// the price of asset 2 at option maturity
ST3 ¼ S3*exp(Z(3));
// the price of asset 3 at option maturity
// options on the maximum
tmp2 ¼ MAX(ST1, ST2);
the_max ¼ MAX(tmp2, ST3);
tmp1 ¼ the_maxE;
opt_val ¼ MAX(tmp1, zero);
sumit_max_call þ¼ opt_val*disc;
tmp1 ¼ E-the_max;
opt_val ¼ MAX(tmp1, zero);
sumit_max_put þ¼ opt_val*disc;
// options on the minimum
tmp2 ¼ MIN(ST1, ST2);
the_min ¼ MIN(tmp2, ST3);
Multiasset European and American options
251

tmp1 ¼ the_minE;
opt_val ¼ MAX(tmp1, zero);
sumit_min_call þ¼ opt_val*disc;
tmp1 ¼ Ethe_min;
opt_val ¼ MAX(tmp1, zero);
sumit_min_put þ¼ opt_val*disc;
}
opt_val ¼ sumit_max_put/(double)num_simulations;
printf(‘‘MAX:PUT¼ %12.4 f <%8.4 e> (0.936)\n’’,opt_val, FABS(opt_val 0.936));
opt_val ¼ sumit_max_call/(double)num_simulations;
printf(‘‘MAX:CALL¼%12.4 f<%8.4 e>(22.672) \n’’,opt_val, FABS(opt_val 22.672));
opt_val ¼ sumit_min_put/(double)num_simulations;
printf(‘‘MIN:PUT¼%12.4 f<%8.4 e>(7.403)\n’’,opt_val, FABS(opt_val 7.403));
opt_val ¼ sumit_min_call/(double)num_simulations;
printf(‘‘MIN:CALL¼%12.4 f<%8.4 e>(5.249) \n’’,opt_val, FABS(opt_val 5.249));
}
Code excerpt 12.1
A Monte Carlo simulation computer program, using quasirandom numbers, for
estimating the value of European put and call options on the maximum and minimum of three underlying
assets. The results are presented in Tables 12.1 and 12.2
.. Initialisation of model parameters etc the same as for quasirandom code ..
printf (‘‘PSEUDORANDOM NUMBERS \n’’);
INIT_FAIL(flag);
seed ¼ 111;
// set the seed for the pseudorandom numbers
g05cbc(seed);
g05eac(&MEANS(1),m,&C3(1,1),m,tol,&rvec,&flag);
sumit_max_put ¼ zero;
sumit_max_call ¼ zero;
sumit_min_put ¼ zero;
sumit_min_call ¼ zero;
for (i ¼ 1; i <¼ num_simulations ; þþi) {
g05ezc(&Z(1),rvec);
ST1 ¼ S1*exp(Z(1));
ST2 ¼ S2*exp(Z(2));
ST3 ¼ S3*exp(Z(3));
// options on the maximum
tmp2 ¼ MAX(ST1,ST2);
the_max ¼ MAX(tmp2,ST3);
tmp1 ¼ the_maxE;
opt_val ¼ MAX(tmp1, zero);
sumit_max_call þ¼ opt_val*disc;
tmp1 ¼ Ethe_max;
opt_val ¼ MAX(tmp1, zero);
sumit_max_put þ¼ opt_val*disc;
// options on the minimum
tmp2 ¼ MIN(ST1,ST2);
the_min ¼ MIN(tmp2,ST3);
tmp1 ¼ the_minE;
opt_val ¼ MAX(tmp1, zero);
sumit_min_call þ¼ opt_val*disc;
tmp1 ¼ Ethe_min;
opt_val ¼ MAX(tmp1, zero);
sumit_min_put þ¼ opt_val*disc;
}
opt_val ¼ sumit_max_put/(double)num_simulations;
printf (‘‘PSEUDORANDOM OPTION MAX PUT ¼ %12.4 f <%8.4 e> (0.936)\n’’,opt_val,FABS(opt_val 0.936));
opt_val ¼ sumit_max_call/(double)num_simulations;
printf (‘‘PSEUDORANDOM OPTION MAX CALL ¼ %12.4 f <%8.4 e> (22.672 ) \n’’,opt_val,FABS(opt_val 22.672));
opt_val ¼ sumit_min_put/(double)num_simulations;
printf (‘‘PSEUDORANDOM OPTION MIN PUT ¼ %12.4 f <%8.4 e> (7.403) \n’’,opt_val,FABS(opt_val 7.403));
opt_val ¼ sumit_min_call/(double)num_simulations;
printf (‘‘PSEUDORANDOM OPTION MIN CALL ¼ %12.4 f <%8.4 e> (5.249) \n’’,opt_val,FABS(opt_val 5.249));
}
Code excerpt 12.2
A Monte Carlo simulation computer program, using pseudorandom numbers,
for estimating the value of European put and call options on the maximum and minimum of three
underlying assets. It can be seen that, apart from code concerned with calling the random number
generator, the program is identical to that given in Code excerpt 12.1 above. The results are presented in
Tables 12.1 and 12.2
252
Pricing Assets

12.4
MULTIDIMENSIONAL LATTICE METHODS
Finite-difference lattices can be used to value options on up to about four assets before
they require impossibly large amounts of computer memory. The main advantage of
finite-difference method is that they are able to easily cater for American style early
exercise facilities within the option. This is not true of Monte Carlo methods. They can
easily model complex European options, but have difficulty modelling American style
options.
In this section we use the approach of Kamrad and Ritchken (1991), and Boyle,
Evnine and Gibbs (1989), which we will call the BEGKR method), to price multiasset
options. We first derive expressions for the jump size and jump probabilities for a single
asset, and show that these are equivalent to those of the Cox, Ross, and Rubinstein
binomial lattice (CRR lattice) discussed in Section 10.4.1. We will then give a expres-
sion for the jump sizes and jump probabilities of a general multiasset option.
Finally there will be a brief discussion of two lattice techniques, namely truncated
lattices and recursive lattices, that the author has found useful in computing multi-
asset option values.
To derive the BEGKR equations for one asset we first assume that the asset
follows a lognormal processes with drift  ¼ r  2=2, where r is the riskless interest
rate and  is the instantaneous volatility.
Therefore if St is the price of the asset at time t, and Stþt is the price at time
instant tþt, we then have the following equations:
logðStþtÞ ¼ logðStÞ þ 	t;
	t  Nðt; 2tÞ
or equivalently
log Stþt
St


 Nðt; 2tÞ
where 	t represents a random variable and as usual N(t, 2t) denotes a Gaussian
with mean t and variance 2t.
We will now consider how to construct a binomial lattice by only allowing 	t to
jump up or down by an amount 
 ¼ 
ffiffiffiffiffiffi
t
p
at each lattice node. This means that:
For an up jump
log Stþt
St


¼ 
ffiffiffiffiffiffi
t
p
;
or
Stþt ¼ St expð
ffiffiffiffiffiffi
t
p
Þ
ð12:6Þ
For a down jump
log Stþt
St


¼ 
ffiffiffiffiffiffi
t
p
;
or
Stþt ¼ St expð
ffiffiffiffiffiffi
t
p
Þ
ð12:7Þ
The reader will notice that these expressions are the same as those for the nodes of
the CCR lattice described in Section 10.4.1. That is: for an up jump Stþt ¼ Stu, for a
down jump Stþt ¼ Std, and u ¼ 1=d ¼ exp (
ffiffiffiffiffiffi
t
p
).
Multiasset European and American options
253

The probability of undergoing either an up or down jump occurring can be found
by matching the mean and variance of 	t.
From the mean:
E½	t ¼ 
ðpu  pdÞ ¼ t
ð12:8Þ
and from the variance:
Var½	t ¼ 
2ðpu þ pdÞ ¼ 2t
ð12:9Þ
Eliminating pd from Equations 12.8 and 12.9 gives

t þ 2t ¼ 2
2pu
and so
pu ¼ 1
2
2t

2
þ t

	

which on substituting 
 ¼ 
ffiffiffiffiffiffi
t
p
yields
pu ¼ 1
2
1 þ 
ffiffiffiffiffiffi
t
p

	

ð12:10Þ
pd ¼ 1  pu ¼ 1
2
1  
ffiffiffiffiffiffi
t
p

	

ð12:11Þ
We shall now show that, to first order, the jump probabilities in Equations 12.10
and 12.11 are the same as those for the CRR lattice.
For the CRR lattice (Section 10.4.1, Equation 10.89) we have:
pu ¼ expðrtÞ  d
u  d
expanding exp (rt), u and d to order t we obtain
expðrtÞ  1 þ rt
u ¼ expð
ffiffiffiffiffiffi
t
p
Þ  1 þ 
ffiffiffiffiffiffi
t
p
þ 2
2 t
d ¼ expð
ffiffiffiffiffiffi
t
p
Þ  1  
ffiffiffiffiffiffi
t
p
þ 2
2 t
so
expðrtÞ  d  rt þ 
ffiffiffiffiffiffi
t
p
 2t
2
and
u  d  2
ffiffiffiffiffiffi
t
p
So
pu ¼ expðrtÞ  d
u  d
 rt þ   2=2t
2
ffiffiffiffiffiffi
t
p
254
Pricing Assets

which simplifies to
pu ¼ 1
2
1 þ 
ffiffiffiffiffiffi
t
p

	

and therefore
pd ¼ 1  pu ¼ 1
2
1  
ffiffiffiffiffiffi
t
p

	

which are the expressions for pu and pd given in Equations 12.10 and 12.11 respect-
ively. So we have shown that, to first order in t, both the size of the jump and the
probability of the jump are the same as the CRR binomial lattice.
The attractive feature of the BEGKR binomial lattice model is that it can easily be
generalized to describe a model consisting of k assets. Here we will merely quote the
results in Kamrad and Ritchken (1991). As before, it is assumed that the asset prices
follow a multivariate lognormal distribution. Let i ¼ r  2
i =2, and i be the
instantaneous mean and variance respectively (i ¼ 1, 2, . . . , k) and let ij be the correl-
ation between assets i and j. There are now 2k different jumps from each lattice node
over the time interval t, and
The jump probabilities for a k-asset binomial lattice: Kamrad and Ritchken (1991)
The 2k jump probabilities, pm, m ¼ 1, . . . , 2k, for each lattice node are:
pm ¼ 1
2k
1 þ
ffiffiffiffiffiffi
t
p
X
k
i¼1
xim i
i


þ
X
k1
i¼1
X
k
j¼iþ1
ðxm
ij ijÞ
(
)
;
m ¼ 1; 2; . . . ; 2k;
k  2
ð12:12Þ
where xim ¼ 1 if asset i has an up jump in state m, and xim ¼ 1 if asset i has a
down jump in state m. In addition xm
ij ¼ 1 if assets i and j have jumps in the same
direction in state m, and xm
ij ¼ 1 if assets i and j have jumps in the opposite
direction in state m.
12.4.1
Truncated lattices
The truncated lattice makes use of the fact that not all of the lattice will contribute
significantly to the value of the option. This can be seen by merely considering the
probability of undergoing n jumps in a given direction. It can be seen from Equation
12.12 that, for a k asset lattice, each of the 2k jumps from an individual lattice node
has a probability p  1=2k. The probability of undergoing n jumps in a given
direction is pn, and since p < 1, it follows that pn  0 for large n. This means that
the probability of attaining the very high or very low asset values which occur in the
wings of the lattice is extremely small. This approach is similar to that used in the
Hull and White interest rate model, see Hull and White (1994).
Multiasset European and American options
255

12.4.2
Recursive lattices
The recursive lattice used here is a multiasset extension of the BBS binomial lattice
described in Section 10.4.4, where the analytic Black–Scholes formula was used to
compute the option values of the last lattice step. If we want to use exactly the same
technique then we would need to use some complicated expression involving multi-
dimensional cumulative normal distribution functions, see Section 12.5 where these are
given for two asset options. One way round this problem is to approximate the analytic
solution by using a higher accuracy lattice to compute the last step. This can be
achieved by a recursive call to the original lattice as shown in the code excerpt below
(the complete code for a two-dimensional recursive lattice is given in Appendix D.2).
void RECURSIVE_2D_binomial(double *value, double S1, double S2, double X,
double sigma1, double sigma2, double rho, double T, double r, double q1, double q2,
Integer put, Integer M, Integer opt_type, Integer is_american, Integer recc, Integer *iflag)
{



if (recc ¼¼ 0) { /* called without recursion, assign terminal nodes as for a standard two dimensional
lattice */



}
0
1
2
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
max_index = 4
Figure 12.1
Diagram illustrating a one-dimensional truncated binomial lattice in which max index ¼ 4.
This means that there are only nine different asset values in the lattice: the current asset price, four above
the current asset value and four below the current asset value
256
Pricing Assets

else { /* called with recursive last step */
P1 ¼ 1;
for (i ¼ 0; i <¼ M 1; þþi) {
P2 ¼ 1;
for (j ¼ 0; j <¼ M 1; þþj) {
loc_T ¼ dt;
loc_M ¼ 10;
loc_recc ¼ 0;
loc_iflag ¼ 0;
loc_is_american ¼ is_american;
recursive_2D_binomial(&hold, s1[P1], s2[P2], X, sigma1, sigma2, rho,
loc_T, r, q1, q2, put, loc_M, opt_type, loc_is_american, loc_recc, &loc_iflag);
if (is_american) { /* An american option so use
hold,s1[P1], and s2[P2] to calculate the option value */



}
else {
V(i,j) ¼ hold;
}
P2 ¼ P2 þ 2;
}
P1 ¼ P1 þ 2;
}
}
for (m1 ¼ M 1 recc; m1 >¼ 0; m1) { /* work backwards through the lattice to calculate the option value */
P1 ¼ Mm1;
/* Identical code to the equivalent loop of the standard 2 dimensional binomial lattice
see code excerpt 3.11 */



}
*value ¼ V(0,0);
}
Code excerpt 12.3
Code excerpt showing the recursive calculation for the last time step, using a ten step
lattice over the time interval dt
In Sections 12.5 and 12.6 we present results showing the benefits of using a recursive
lattice for options on the maximum or minimum of two and three assets.
12.5
TWO ASSET OPTIONS
Here we consider options based on the underlying prices of two assets, S1 and S2. We
give analytic formulae to value European options based on the maximum and
minimum of two assets and also show how two-dimensional binomial lattices can
be constructed to value American style options.
12.5.1
European options
We begin by presenting results from Stulz (1982) and Johnson (1987) concerning the
value of European call option on the maximum and minimum of two assets.
Call options on the maximum and minumum of two assets
Let the value of a European call option on the minimum of two assets, S1 and S2,
with strike price E, maturity  and correlation coefficient , be denoted by cmin. The
value of the corresponding call option on the maximum of these assets will be
represented by cmax.
Multiasset European and American options
257

Then, following Stulz (1982) and Johnson (1987), we have:
cmax ¼ S1N2ðd1ðS1; E; 2
1Þ; d0
1ðS1; S2; 2
Þ; 1Þ þ S2N2ðd1ðS2; E; 2
2Þ; d0
1ðS2; S1; 2
Þ; 2Þ
 E expðrÞ 1  N2ðd2ðS1; E; 2
1Þ;

 d2ðS2; E; 2
2Þ; Þg
ð12:13Þ
and
cmin ¼ S1N2ðd1ðS1; E; 2
1Þ; d0
1ðS1; S2; 2
Þ; 1Þ
þ S2N2ðd1ðS2; E; 2
2Þ; d0
1ðS2; S1; 2
Þ; 2Þ
 E expðrÞN2ðd2ðS1; E; 2
1Þ; d2ðS2; E; 2
2Þ; Þ
ð12:14Þ
where N2(a1, b1, c1) is the bivariate cumulative normal with . .. , this can for instance be
computed using the NAG routine g01hac. The other symbols are defined as follows:
2
 ¼ 2
1  212 þ 2
2
d1ðSi; E; 2
i Þ ¼ logðSi=EÞ þ ðr þ 2
i =2Þ
i
ffiffiffi
p
;
i ¼ 1; 2
d2ðSi; E; 2
i Þ ¼ logðSi=EÞ þ ðr  2
i =2Þ
i
ffiffiffi
p
;
i ¼ 1; 2
d0
1ðSi; Sj; 2
Þ ¼ logðSi=SjÞ þ ð2
=2Þ

ffiffiffi
p
;
for
i ¼ 1; j ¼ 2; or i ¼ 2; j ¼ 1
and
1 ¼ 1  2

;
2 ¼ 2  1

It can also be shown that:
cmaxðS1; S2; E; Þ þ cminðS1; S2; E; Þ ¼ cðS1; E; Þ þ cðS2; E; Þ
ð12:15Þ
where c(S, E, ) is the value of a vanilla European call. We will now derive expression
for the value of the corresponding European put options.
Put options on the minimum of two assets
It will now be shown that the price of a European put option on the minimum of two
assets, pmin(S1, S2, E, ) is:
pminðS1; S2; E; Þ ¼ E expðrÞ  cminðS1; S2; 0; Þ þ cminðS1; S2; E; Þ
ð12:16Þ
where the meaning of the symbols has been previously defined. This result can be
proved by considering the following two investments:
Portfolio A
Purchase one put option on the minimum of S1 and S2 with exercise price E.
258
Pricing Assets

Portfolio B
Purchase one discount bond which pays E at maturity. Write (that is sell) one option
on the minimum of S1 and S2 with an exercise price of zero. Purchase one option on
the minimum of S1 and S2 with exercise price E.
We now consider the values of these portfolios at option maturity, time .
If min (S1, S2)  E
Portfolio A: Pays zero
Portfolio B: Pays E  min (S1, S2) þ min (S1, S2)  E ¼ 0
If min (S1, S2) ¼ S1 < E
Portfolio A: Pays E  S1
Portfolio B: Pays E  S1 þ 0 ¼ E  S1
If min (S1, S2) ¼ S2 < E
Portfolio A: Pays E  S2
Portfolio B: Pays E  S2 þ 0 ¼ E  S2
We have therefore shown that, under all possible circumstances, Portfolio A has
the same value as Portfolio B. This means that Equation 12.16 is true.
Put options on the maximum of two assets
It will now be shown that the price of a European put option on the maximum of two
assets, pmax(S1, S2, E, ) is:
pmaxðS1; S2; E; Þ ¼ E expðrÞ  cmaxðS1; S2; 0; Þ þ cmaxðS1; S2; E; Þ
ð12:17Þ
where, as before, the meaning of the symbols has been previously defined. This result
can be proved by considering the following two investments:
Portfolio A:
Purchase one put option on the maximum of S1 and S2 with exercise price E.
Portfolio B:
Purchase one discount bond which pays E at maturity. Write (that is sell) one option
on the maximum of S1 and S2 with an exercise price of zero. Purchase one option on
the maximum of S1 and S2 with exercise price E.
As before we now consider the values of these portfolios at option maturity,
time .
Multiasset European and American options
259

If max (S1, S2)  E
Portfolio A: Pays zero
Portfolio B: Pays E  max (S1, S2) þ max (S1, S2)  E ¼ 0
If max (S1, S2) ¼ S2 < E
Portfolio A: Pays E  S1
Portfolio B: Pays E  S1 þ 0 ¼ E  S1
If max (S1, S2) ¼ S2 < E
Portfolio A: Pays E  S2
Portfolio B: Pays E  S2 þ 0 ¼ E  S2
It therefore follows that, under all possible circumstances, Portfolio A has the same
value as Portfolio B, and this means that Equation 12.17 is true.
void rainbow_bs_2d(double *opt_value, double S1, double S2, double X, double sigma1,
double sigma2, double rho, double opt_mat, double r, Integer is_max, Integer *iflag)
{
/* Input parameters:
S1
— the current price of the underlying asset 1,
S2
— the current price of the underlying asset 2,
X
— the strike price,
sigma1
— the volatility of asset 1,
sigma2
— the volatility of asset 2,
rho
— the correlation coefficient between asset 1 and asset 2,
opt_mat
— the time to maturity,
r
— the interest rate,
is_max
— if is_max is 1 then the option is a call on the maximum of two assets, otherwise the option is a
call on the minimum of two assets.
Output parameters:
opt_value
— the value of the option,
iflag
— an error indicator.
*/
double one¼1.0,two¼ 2.0,zero¼ 0.0;
double eps,d1,d2_1,d2_2,temp,temp1,temp2,pi,np;
double rho_112, rho_212, d1_prime;
double sigma, term1, term2, term3;
static NagError nagerr;
eps ¼ X02AJC;
if(X < eps) printf (‘‘ERROR the strike price is too small\n’’) ;
if (sigma1 < eps) printf (‘‘ERROR the volatility (sigma1) is too small \n’’);
if (sigma2 < eps) printf (‘‘ERROR the volatility (sigma2) is too small \n’’);
if (opt_mat < eps) printf (‘‘ERROR the time to maturity (opt_mat) is too small \n’’);
sigma ¼ sqrt((sigma1*sigma1 þ sigma2*sigma2)  two* sigma1*sigma2*rho);
if (is_max ¼¼ 1) { /* then the maximum of two assets */
/* calculate term1 */
temp ¼ log(S1/X);
d1 ¼ tempþ(rþ(sigma1*sigma1/two))*opt_mat;
d1 ¼ d1/(sigma1*sqrt(opt_mat));
temp ¼ log(S1/S2);
d1_prime ¼ tempþ(sigma*sigma/two)*opt_mat;
d1_prime ¼ d1_prime/(sigma*sqrt(opt_mat));
rho_112 ¼ (sigma1  rho*sigma2) / sigma;
term1 ¼ g01hac(d1,d1_prime,rho_112,&nagerr);
term1 ¼ term1*S1;
/* calculate term2 */
temp ¼ log(S2/X);
d1 ¼ tempþ(rþ(sigma2*sigma2/two))*opt_mat;
d1 ¼ d1/(sigma2*sqrt(opt_mat));
temp ¼ log(S2/S1);
260
Pricing Assets

d1_prime ¼ tempþ(sigma*sigma/two)*opt_mat;
d1_prime ¼ d1_prime/(sigma*sqrt(opt_mat));
rho_212 ¼ (sigma2  rho*sigma1) / sigma;
term2¼S2*g01hac(d1,d1_prime,rho_212,&nagerr);
/* calculate term3 */
temp ¼ log(S1/X);
d2_1 ¼ tempþ(r(sigma1*sigma1/two))*opt_mat;
d2_1 ¼ d2_1/(sigma1*sqrt(opt_mat));
temp ¼ log(S2/X);
d2_2 ¼ tempþ(r(sigma2*sigma2/two))*opt_mat;
d2_2 ¼ d2_2/(sigma2*sqrt(opt_mat));
term3 ¼ g01hac(d2_1,d2_2,rho,&nagerr);
*opt_value¼ term1þterm2X*exp(r*opt_mat)*term3;
}
else { /* the minimum of two assets */
/* calculate term1 */
temp ¼ log(S1/X);
d1 ¼ tempþ(rþ(sigma1*sigma1/two))*opt_mat;
d1 ¼ d1/(sigma1*sqrt(opt_mat));
temp ¼ log(S1/S2);
d1_prime ¼ tempþ(sigma*sigma/two)*opt_mat;
d1_prime ¼ d1_prime/(sigma*sqrt(opt_mat));
rho_112 ¼ (sigma1  rho*sigma2) / sigma;
term1 ¼ g01hac(d1,d1_prime,rho_112,&nagerr);
term1 ¼ term1*S1;
/* calculate term2 */
temp ¼ log(S2/X);
d1 ¼ tempþ(rþ(sigma2*sigma2/two))*opt_mat;
d1 ¼ d1/(sigma2*sqrt(opt_mat));
temp ¼ log(S2/S1);
d1_prime ¼ tempþ(sigma*sigma/two)*opt_mat;
d1_prime ¼ d1_prime/(sigma*sqrt(opt_mat));
rho_212 ¼ (sigma2  rho*sigma1) / sigma;
term2¼S2*g01hac(d1,d1_prime,rho_212,&nagerr);
/* calculate term3 */
temp ¼ log(S1/X);
d2_1 ¼ tempþ(r(sigma1*sigma1/two))*opt_mat;
d2_1 ¼ d2_1/(sigma1*sqrt(opt_mat));
temp ¼ log(S2/X);
d2_2 ¼ tempþ(r(sigma2*sigma2/two))*opt_mat;
d2_2 ¼ d2_2/(sigma2*sqrt(opt_mat));
term3 ¼ g01hac(d2_1,d2_2,rho,&nagerr);
*opt_value¼ term1þterm2X*exp(r*opt_mat)*term3;
}
return;
Code excerpt 12.4
Function to calculate the value of a European call on the maximum or minimum of
two assets using the analytic result of Johnson (1987) and Stulz (1982)
void opt_rainbow_bs_2d(double *opt_value, double S1, double S2, double X, double sigma1,
double sigma2, double rho, double opt_mat, double r, Integer is_max, Integer putcall, Integer *flag)
{
/* Input parameters:
S1
— the current price of the underlying asset 1,
S2
— the current price of the underlying asset 2,
X
— the strike price,
sigma1
— the volatility of asset 1,
sigma2
— the volatility of asset 2,
rho
— the correlation coefficient between asset 1 and asset 2,
opt_mat
— the time to maturity,
r
— the interest rate,
is_max
— if is_max is 1 then the option is on the maximum of two assets, otherwise the option is on
the minimum of two assets,
putcall
— if putcall is 0 then the option is a call, otherwise the option is a put.
Output parameters:
opt_value
— the value of the option,
iflag
— an error indicator.
*/
double temp1;
double temp2;
Multiasset European and American options
261

double fac;
double a_zero ¼ 1.0e 6; /* approximate zero number to prevent overflow in rainbow_bs_2d */
if (putcall) { /* a put option */
fac ¼ X*exp(r*opt_mat);
rainbow_bs_2d(&temp1, S1, S2, a_zero, sigma1, sigma2, rho, opt_mat, r, is_max, flag);
rainbow_bs_2d(&temp2, S1, S2, X, sigma1, sigma2, rho, opt_mat, r, is_max, flag);
*opt_value ¼ fac  temp1 þ temp2;
}else { /* a call option */
rainbow_bs_2d(opt_value, S1, S2, X, sigma1, sigma2, rho, opt_mat, r, is_max, flag);
}
}
Code excerpt 12.5
Function to calculate the value of a European put or call on the maximum or minimum
of two assets using the analytic result of Johnson (1987) and Stulz (1982)
Option prices computed, using a two-dimensional binomial lattice and also the
analytic formula of Johnson and Stulz, are presented in Tables 12.3 and 12.4.
Table 12.3
The computed values and absolute errors for European put and call options on the maximum
of two assets. The results were obtained using a binomial lattice and the analytic formula (Johnson, 1987;
Stulz, 1982). The time to maturity of the option is varied from 0.1 to 0.8 years. The parameters are:
E ¼ 44:0, S1 ¼ 40:0, S2 ¼ 50:0, r ¼ 0:1, 1 ¼ 0:2, 2 ¼ 0:2, q1 ¼ q2 ¼ 0:0,  ¼ 0:5, n steps ¼ 50
Call
Put
Time
Analytic
Lattice
Error
Analytic
Lattice
Error
0.1
6.45320
6.45245
7:4972 	 104
0.01524
0.01451
7:3344 	 104
0.2
6.96192
6.95953
2:3845 	 103
0.08252
0.08001
2:5106 	 103
0.3
7.49587
7.49376
2:1084 	 103
0.15787
0.15580
2:0675 	 103
0.4
8.03710
8.04022
3:1260 	 103
0.22362
0.22680
3:1768 	 103
0.5
8.57808
8.57916
1:0757 	 103
0.27762
0.27683
7:8867 	 104
0.6
9.11529
9.10809
7:2006 	 103
0.32115
0.31872
2:4328 	 103
0.7
9.64700
9.64838
1:3826 	 103
0.35598
0.35714
1:1548 	 103
0.8
10.17238
10.17663
4:2571 	 103
0.38372
0.38711
3:3891 	 103
Table 12.4
The computed values and absolute errors for European put and call options on the minimum
of two assets. The results were obtained using a binomial lattice and the analytic formula (Johnson, 1987;
Stulz, 1982). The time to maturity of the option is varied from 0.1 to 0.8 years. The parameters are:
E ¼ 44:0, S1 ¼ 40:0, S2 ¼ 50:0, r ¼ 0:1, 1 ¼ 0:2, 2 ¼ 0:2, q1 ¼ q2 ¼ 0:0,  ¼ 0:5, n steps ¼ 50
Call
Put
Time
Analytic
Lattice
Error
Analytic
Lattice
Error
0.1
0.10810
0.10753
5:7048 	 104
3.67044
3.66993
5:0955 	 104
0.2
0.40862
0.40781
8:1047 	 104
3.54551
3.54514
3:6961 	 104
0.3
0.74162
0.73418
7:4339 	 103
3.47882
3.47206
6:7642 	 103
0.4
1.06989
1.07299
3:1076 	 103
3.43283
3.43715
4:3214 	 103
0.5
1.38675
1.38909
2:3414 	 103
3.39540
3.40159
6:1826 	 103
0.6
1.69203
1.69025
1:7757 	 103
3.36145
3.35775
3:6964 	 103
0.7
1.98691
1.96939
1:7520 	 102
3.32859
3.31517
1:3417 	 102
0.8
2.27276
2.26274
1:0018 	 102
3.29566
3.29157
4:0885 	 103
262
Pricing Assets

12.5.2
American options
We assume that the prices of assets 1 and 2 follow a lognormal process with drift
terms of 1 ¼ r  2
1=2, and 2 ¼ r  2
2=2 respectively. As before r is the riskless
interest rate and 1 and 2 are the instantaneous volatilities of assets 1 and 2.
If we let S1, t and S2, t denote the respective prices of assets 1 and 2 at time t, then we
can write:
logðS1;tþtÞ ¼ logðS1;tÞ þ 	1;t
ð12:18Þ
and
logðS2;tþtÞ ¼ logðS2;tÞ þ 	2;t
ð12:19Þ
where 	1, t is a random normal variable with mean 1t and variance 2
1t, and 	2, t is
a random normal variable with mean 2t and variance 2
2t.
In the binomial lattice model, over the time interval t, the variate log (S1,t) is only
allowed to jump up or down by an amount 
1 ¼ 1
ffiffiffiffiffiffi
t
p
, and similarly the variate
log (S2,t) is only permitted to jump up and down by the amount 
2 ¼ 2
ffiffiffiffiffiffi
t
p
. We will
denote the probability of both log (S1,t) and log (S2,t) having an up jump over time
interval t by puu, and the probability of log (S1,t) having an up jump and log (S2,t)
having a down jump by pud, etc.
The mean values in Equations 12.18 and 12.19 then give
E½	1;t ¼ 
1ðpuu þ pud  pdd  pduÞ ¼ 1t
ð12:20Þ
E½	2;t ¼ 
2ðpuu þ pud  pdd  pduÞ ¼ 2t
ð12:21Þ
and the variance/covariance terms yields
Var½	1;t ¼ 
2
1ðpuu þ pud þ pdd þ pduÞ ¼ 2
1t
ð12:22Þ
Var½	2;t ¼ 
2
2ðpuu þ pud þ pdd þ pduÞ ¼ 2
2t
ð12:23Þ
E½	1;t	2;t ¼ 
1
2ðpuu  pud þ pdd  pduÞ ¼ 12t
ð12:24Þ
where  is the correlation coefficient between 	1,t and 	2,t.
We therefore obtain:
puu þ pud  pdd þ pdu ¼ 1
ffiffiffiffiffiffi
t
p
1
puu  pud  pdd þ pdu ¼ 2
ffiffiffiffiffiffi
t
p
2
puu þ pud þ pdd þ pdu ¼ 1
puu  pud þ pdd  pdu ¼ 
Multiasset European and American options
263

These lead to the following jump probabilities:
puu ¼ 1
4
1 þ
ffiffiffiffiffiffi
t
p
1
1
þ 2
2


þ 
	

pud ¼ 1
4
1 þ
ffiffiffiffiffiffi
t
p
1
1
 2
2


 
	

pdd ¼ 1
4
1 þ
ffiffiffiffiffiffi
t
p
 1
1
 2
2


þ 
	

pdu ¼ 1
4
1 þ
ffiffiffiffiffiffi
t
p
 1
1
þ 2
2


 
	

In Code excerpt 12.6, we provide the computer code for a standard binomial lattice
which prices options on the maximum and minimum of two assets.
The parameter M is the number of time steps used, and the lattice is constructed
under the assumption that M is even.
void standard_2D_binomial(double *value, double S1, double S2, double X, double sigma1, double sigma2,
double rho, double T, double r, double q1, double q2, Integer put, Integer M, Integer opt_type, Integer
is_american, Integer *iflag)
{
/* Input parameters:
S1
— the current price of the underlying asset 1
S2
— the current price of the underlying asset 2
X
— the strike price
sigma1
— the volatility of asset 1
sigma2
— the volatility of asset 2
rho
— the correlation coefficient between asset 1 and asset 2
T
— the time to maturity
r
— the interest rate
q1
— the continuous dividend yield for asset 1
q2
— the continuous dividend yield for asset 2
put
— if put is 0 then a call option, otherwise a put option
M
— the number of time steps, the zeroth time step is the root node of the lattice
opt_type
— if opt_type is 0 then an option on the maximum of two asset otherwise an option
on the minimum of two assets
is_american — if is_american is 0 then a European option, otherwise an American option
Output parameters:
value
— the value of the option,
iflag
— an error indicator.
*/
double discount,t1,dt,d1,d2,u1,u2;
Integer i,j,m1,n,iflagx,jj,ind;
double zero¼ 0.0,hold;
double temp,ds1,ds2,dv1,dv2,h,tmp;
double *s1, *s2, *v;
double p[4];
Integer P1,P2,tdv;
double sqrt_dt, t, mu1, mu2, jp1, jp2;
double one ¼ 1.0, half ¼ 0.5, quarter ¼ 0.25;
Integer v1;
if (!((Mþ 1)/2 ¼¼ M/2)) {
printf (‘‘ERROR THE NUMBER OF TIME STEPS IS NOT EVEN \n’’);
return;
}
tdv ¼ M þ 1;
264
Pricing Assets

#define V(I,J) v[(I) * tdv þ (J)]
#define UU 0
#define UD 1
#define DD 2
#define DU 3
dt ¼ T/(double)M;
sqrt_dt ¼ sqrt(dt);
jp1 ¼ sigma1*sqrt_dt;
jp2 ¼ sigma2*sqrt_dt;
mu1 ¼ r  q1  sigma1*sigma1*half;
mu2 ¼ r  q2  sigma2*sigma2*half;
u1 ¼ exp(jp1); /* assign the jump sizes */
u2 ¼ exp(jp2);
d1 ¼ exp(jp1);
d2 ¼ exp(jp2);
p[UU] ¼ quarter*(one þ sqrt_dt * ((mu1/sigma1) þ (mu2/sigma2)) þ rho); /* set up the jump probabilities */
p[UD] ¼ quarter*(one þ sqrt_dt * ((mu1/sigma1)  (mu2/sigma2))  rho);
p[DD] ¼ quarter*(one þ sqrt_dt * ((mu1/sigma1)  (mu2/sigma2)) þ rho);
p[DU] ¼ quarter*(one þ sqrt_dt * ((mu1/sigma1) þ (mu2/sigma2))  rho);
for (i ¼ 0; i < 4; þþi) {
if ((p[i] < zero) || (p[i] > 1.0)) printf (‘‘ERROR p out of range\n’’);
}
discount ¼ exp(r*dt);
for (i ¼ 0; i < 4; þþi) {
p[i] ¼ p[i]*discount;
}
/* Allocate the arrays v[(Mþ 1)*(Mþ 1)], s1[2*Mþ 1] and s2[2*Mþ 1] */



s1[M] ¼ S1; /* assign the 2*Mþ 1 asset values for s1 */
for (i ¼ 1; i <¼ M; þþi) {
s1[Mþi] ¼ u1*s1[Mþi 1];
s1[Mi] ¼ d1*s1[Miþ 1];
}
s2[M] ¼ S2; /* assign the 2*Mþ 1 asset values for s2 */
for (i ¼ 1; i <¼ M; þþi) {
s2[Mþi] ¼ u2*s2[Mþi 1];
s2[Mi] ¼ d2*s2[Miþ 1];
}
P1 ¼ 0;
for (i ¼ 0; i <¼ M; þþi) { /* Calculate the option values at maturity */
P2 ¼ 0;
for (j ¼ 0; j <¼ M; þþj) {
if (opt_type ¼¼ 0) { /* Maximum of two assets */
if (put) {
V(i,j) ¼ MAX(X  MAX(s1[P1],s2[P2]),zero);
}
else {
V(i,j) ¼ MAX(MAX(s1[P1],s2[P2])X,zero);
}
}
else {
if (put) { /* Minimum of two assets */
V(i,j)¼ MAX(XMIN(s1[P1],s2[P2]), zero);
}
else {
V(i,j)¼ MAX(MIN(s1[P1],s2[P2])X,zero);
}
}
P2 ¼ P2 þ 2;
}
P1 ¼ P1 þ 2;
}
for (m1 ¼ M 1; m1 >¼ 0; m1) { /* work backwards through the lattice to calculate option value */
P1 ¼ Mm1;
for (i ¼ 0; i <¼ m1; þþi) {
P2 ¼ Mm1;
for (j ¼ 0; j <¼ m1; þþj) {
hold ¼ p[UD]*V(iþ 1,j) þ p[UU]*V(iþ 1,jþ 1) þ p[DU]*V(i,jþ 1) þ p[DD]*V(i,j);
if (is_american) { /* An American option */
if (opt_type ¼¼ 0) { /* Maximum of two assets */
if (put)
V(i,j)¼ MAX(hold, XMAX(s1[P1],s2[P2]));
else
V(i,j)¼ MAX(hold,MAX(s1[P1], s2[P2])X);
}
else { /* Minimum of two assets */
Multiasset European and American options
265

if (put)
V(i,j)¼ MAX(hold,XMIN(s1[P1], s2[P2]));
else
V(i,j)¼ MAX(hold,MIN(s1[P1],s2[P2])X);
}
}
else {
V(i,j) ¼ hold;
}
P2 ¼ P2 þ 2;
}
P1 ¼ P1 þ 2;
}
}
*value ¼ V(0,0);
}
Code excerpt 12.6
Function to calculate the value of a European put or call on the maximum or minimum
of two assets using a standard binomial lattice
The computer code for a truncated two-dimensional binomial lattice is given in
Appendix D.1.
Table 12.5
The computed values and absolute errors for an American put option on the maximum
of two assets. A truncated binomial lattice was used and we show how the accuracy depends on the value
of maxindex. The parameters are: E ¼ 100:0, S1 ¼ S2 ¼ 100:0, r ¼ 0:2,  ¼ 1:0, 1 ¼ 2 ¼ 0:2,  ¼ 0:5,
q1 ¼ q2 ¼ 0:0. The first column gives the value of maxindex, the second column the computational time in
milliseconds, the third column the computed value of the option, and the last column the absolute error. The
accurate value took 280ms to compute and was obtained using a standard lattice with nsteps ¼ 200
max_index
Time (ms)
Value
Error
22
10.0
1.8478
6:3912 	 103
26
20.0
1.8525
1:7179 	 103
40
30.0
1.8542
1:277 	 105
48
40.0
1.8542
5:0338 	 107
52
50.0
1.8542
8:6936 	 108
58
60.0
1.8542
5:1993 	 109
Table 12.6
The computed values and absolute errors for an American put option on the minimum of
two assets. A truncated binomial lattice was used and we show how the accuracy depends on the
value of maxindex. The parameters are: E ¼ 100:0, S1 ¼ S2 ¼ 100:0, r ¼ 0:2,  ¼ 1:0, 1 ¼ 2 ¼ 0:2,
 ¼ 0:5, q1 ¼ q2 ¼ 0:0. The first column gives the value of maxindex, the second column the
computational time in milliseconds, the third column the computed value of the option, and the last
column the absolute error. The accurate value took 311 ms to compute and was obtained using a
standard lattice with nsteps ¼ 200
max_index
Time (ms)
Value
Error
26
10.0
4.7008
3:8500 	 102
32
20.0
4.7301
9:2094 	 103
40
30.0
4.7383
1:0258 	 103
44
40.0
4.7390
2:9951 	 104
48
50.0
4.7392
7:9631 	 105
52
60.0
4.7393
1:9230 	 105
266
Pricing Assets

12.6
THREE ASSET OPTIONS
For three assets we have the following jump probabilities:
puuu ¼ 1
8
1 þ
ffiffiffiffiffiffi
t
p
1
1
þ 2
2
þ 3
3


þ 12 þ 13 þ 23
	

puud ¼ 1
8
1 þ
ffiffiffiffiffiffi
t
p
1
1
þ 2
2
 3
3


þ 12  13  23
	

pudu ¼ 1
8
1 þ
ffiffiffiffiffiffi
t
p
1
1
 2
2
þ 3
3


 12 þ 13  23
	

pudd ¼ 1
8
1 þ
ffiffiffiffiffiffi
t
p
1
1
 2
2
 3
3


 12  13 þ 23
	

pduu ¼ 1
8
1 þ
ffiffiffiffiffiffi
t
p
 1
1
þ 2
2
þ 3
3


 12  13 þ 23
	

pdud ¼ 1
8
1 þ
ffiffiffiffiffiffi
t
p
 1
1
þ 2
2
þ 3
3


 12 þ 13  23
	

pddu ¼ 1
8
1 þ
ffiffiffiffiffiffi
t
p
 1
1
 2
2
þ 3
3


þ 12  13  23
	

pddd ¼ 1
8
1 þ
ffiffiffiffiffiffi
t
p
 1
1
 2
2
 3
3


þ 12 þ 13 þ 23
	

The computer code for a standard three-dimensional lattice is given in Code
excerpt 12.7 below. Code for truncated and recursive lattices is supplied on the
CD ROM.
void standard_3D_binomial (double *value, double S1, double S2, double S3, double X, double sigma1,
double sigma2, double sigma3, double rho_12, double rho_13, double rho_23, double T, double r,
Integer put, Integer M, Integer opt_type, Integer is_american, Integer *iflag)
{
/* Input parameters:
S1
— the current price of the underlying asset 1
S2
— the current price of the underlying asset 2
S3
— the current price of the underlying asset 3
X
— the strike price
sigma1
— the volatility of asset 1
sigma2
— the volatility of asset 2
sigma3
— the volatility of asset 3
rho_12
— the correlation coefficient between asset 1 and asset 2
rho_13
— the correlation coefficient between asset 1 and asset 3
rho_23
— the correlation coefficient between asset 2 and asset 3
T
— the time to maturity
r
— the interest rate
Multiasset European and American options
267

put
— if put is 0 then a call option, otherwise a put option
M
— the number of time steps, the zeroth time step is the root node of the lattice
opt_type
— if opt_type is 0 then an option on the maximum of two asset otherwise an option on the minimum
of two assets
is_american — if is_american is 0 then a European option, otherwise an American option.
Output parameters:
value
— the value of the option,
iflag
— an error indicator.
*/
double discount, t1, dt, d1, d2, d3, u1, u2, u3;
Integer i, j, k, m1, n, iflagx, jj, ind;
double zero¼0.0, hold;
double temp, ds1, ds2, dv1, dv2, h, tmp, tmp1, tmp2;
double *s1, *s2, *s3, *v;
double p[9];
Integer P1, P2, P3, tdv, tdv2;
double sqrt_dt, t, mu1, mu2, mu3, jp1, jp2, jp3;
double one ¼ 1.0, half ¼ 0.5, eighth ¼ 0.125;
Integer v1;
if (!((M þ 1)/2 ¼¼ M/2)) {
printf (‘‘ERROR THE NUMBER OF TIME STEPS IS NOT EVEN \n’’);
return;
}
tdv ¼ M þ 1;
tdv2 ¼ tdv*tdv;
#define V(I, J, K) v[(I) * tdv2 þ (J)*tdv þ (K)]
#define UUU
0
#define UUD
1
#define UDU
2
#define UDD
3
#define DUU
4
#define DUD
5
#define DDU
6
#define DDD
7
dt ¼ T/(double)M;
sqrt_dt ¼ sqrt(dt);
jp1 ¼ sigma1*sqrt_dt;
jp2 ¼ sigma2*sqrt_dt;
jp3 ¼ sigma3*sqrt_dt;
mu1 ¼ r  sigma1*sigma1*half;
mu2 ¼ r  sigma2*sigma2*half;
mu3 ¼ r  sigma3*sigma3*half;
u1 ¼ exp(jp1); /* assign the jump sizes */
u2 ¼ exp(jp2);
u3 ¼ exp(jp3);
d1 ¼ exp(jp1);
d2 ¼ exp(jp2);
d3 ¼ exp(jp3);
/* set up the jump probabilities */
p[UUU] ¼ eighth*(one þ sqrt_dt * ((mu1/sigma1) þ (mu2/sigma2) þ (mu3/sigma3)) þ rho_12 þ rho_13 þ rho_23);
p[UUD] ¼ eighth*(one þ sqrt_dt * ((mu1/sigma1) þ (mu2/sigma2)  (mu3/sigma3)) þ rho_12  rho_13  rho_23);
p[UDU] ¼ eighth*(one þ sqrt_dt * ((mu1/sigma1)  (mu2/sigma2) þ (mu3/sigma3))  rho_12 þ rho_13  rho_23);
p[UDD] ¼ eighth*(one þ sqrt_dt * ((mu1/sigma1)  (mu2/sigma2)  (mu3/sigma3))  rho_12  rho_13 þ rho_23);
p[DUU] ¼ eighth*(one þ sqrt_dt * ((mu1/sigma1) þ (mu2/sigma2) þ (mu3/sigma3))  rho_12  rho_13 þ
rho_23);
p[DUD] ¼ eighth*(one þ sqrt_dt * ((mu1/sigma1) þ (mu2/sigma2)  (mu3/sigma3))  rho_12 þ rho_13 
rho_23);
p[DDU] ¼ eighth*(one þ sqrt_dt * ((mu1/sigma1)  (mu2/sigma2) þ (mu3/sigma3)) þ rho_12  rho_13 
rho_23);
p[DDD] ¼ eighth*(one þ sqrt_dt * ((mu1/sigma1)  (mu2/sigma2)  (mu3/sigma3)) þ rho_12 þ rho_13 þ
rho_23);
for (i ¼ 0; i < 8; þþi) {
if ((p[i] < zero) || (p[i] > 1.0)) printf (‘‘ERROR p[%ld] ¼ %12.4f out of range\n’’, i, p[i]);
}
discount ¼ exp(r*dt);
for (i ¼ 0; i < 8; þþi) {
p[i] ¼ p[i]*discount;
}
/* Allocate the arrays v[(M þ 1)*(M þ 1)*(M þ 1)], s1[2*M þ 1], s2[2*M þ 1], and s3[2*M þ 1] */



s1[M] ¼ S1;
for (i ¼ 1; i <¼ M; þþi) { /* assign the 2*Mþ 1 asset values for s1 */
268
Pricing Assets

s1[Mþi] ¼ u1*s1[M þ i  1];
s1[Mi] ¼ d1*s1[M  i þ 1];
}
s2[M] ¼ S2;
for (i ¼ 1; i <¼ M; þþi) { /* assign the 2*Mþ 1 asset values for s2 */
s2[Mþi] ¼ u2*s2[M þ i  1];
s2[Mi] ¼ d2*s2[M  i þ 1];
}
s3[M] ¼ S3;
for (i¼ 1; i <¼ M; þþi) { /* assign the 2*Mþ 1 asset values for s2 */
s3[Mþi] ¼ u3*s3[M þ i  1];
s3[Mi] ¼ d3*s3[Miþ 1];
}
/* Calculate the option values at maturity */
P1 ¼ 0;
for (i ¼ 0; i <¼ M; þþi) {
P2 ¼ 0;
for (j ¼ 0; j <¼ M; þþj) {
P3 ¼ 0;
for (k ¼ 0; k <¼ M; þþk) {
if (put) { /* put */
if (opt_type ¼¼ 0) { /* Maximum of 3 assets */
tmp ¼ MAX(s1[P1], s2[P2]);
V(i, j, k) ¼ MAX(X  MAX(tmp, s3[P3]), zero);
}
else if (opt_type ¼¼ 1) { /* Minimum of 3 assets */
tmp ¼ MIN(s1[P1], s2[P2]);
V(i, j, k) ¼ MAX(X  MIN(tmp, s3[P3]), zero);
}
}
else { /* call */
** Insert call option code using the supplied put option code as a template **
}
P3 ¼ P3 þ 2;
}
P2 ¼ P2 þ 2;
}
P1 ¼ P1 þ 2;
}
for (m1 ¼ M 1; m1 >¼ 0; m1) { /* work backwards through the lattice to calculate the option value */
P1 ¼ Mm1;
for (i ¼ 0; i <¼ m1; þþi) {
P2 ¼ Mm1;
for (j ¼ 0; j <¼ m1; þþj) {
P3 ¼ Mm1;
for (k ¼ 0; k <¼ m1; þþk) {
hold ¼ p[UUU]*V(i þ 1, j þ 1, k þ 1) þ p[UUD]*V(i þ 1, j þ 1, k) þ p[UDU]*V(iþ 1, j, k þ 1) þ
p[UDD]*V(iþ 1, j, k)þ p[DUU]*V(i, jþ 1, k þ 1) þ p[DUD]*V(i, j þ 1, k) þ
p[DDU]*V(i, j, k þ 1) þ p[DDD]*V(i, j, k);
if (is_american) {
if (put) {
if (opt_type ¼¼ 0) { /* Maximum of 3 assets */
tmp ¼ MAX(s1[P1], s2[P2]);
tmp1 ¼ MAX(tmp, s3[P3]);
tmp2 ¼ MAX(Xtmp1, hold);
V(i, j, k) ¼ MAX(tmp2, zero);
}
else if (opt_type ¼¼1) { /* Minimum of 3 assets */
tmp ¼ MIN(s1[P1], s2[P2]);
tmp1 ¼ MIN(tmp, s3[P3]);
tmp2 ¼ MAX(Xtmp1, hold);
V(i, j, k) ¼ MAX(tmp2, zero);
}
}
else { /* call option */
** Insert call option code using the supplied put option code as a template **
}
}
else { /* European option */
V(i, j, k) ¼ hold;
}
P3 ¼ P3 þ 2;
}
P2 ¼ P2 þ 2;
}
Multiasset European and American options
269

P1 ¼ P1 þ 2;
}
}
*value ¼ V(0, 0, 0);
}
Code excerpt 12.7
Standard three-dimensional binomial lattice
The results of pricing three asset options, in which 13 ¼ 23 ¼ 0:5, are given in
Tables 12.7 to 12.9; standard, truncated, and recursive lattices are used.
Table 12.7
The computed values and absolute errors for European options on the maximum of three
assets. A binomial lattice was used and we show how the accuracy of the results depends on the number of
time steps. The parameters are: E ¼ 100:0, S1 ¼ S2 ¼ S3 ¼ 100:0, r ¼ 0:1,  ¼ 1:0, 1 ¼ 2 ¼ 3 ¼ 0:2,
12 ¼ 13 ¼ 23 ¼ 0:5, q1 ¼ q2 ¼ q3 ¼ 0:0. The accurate values are 0.936 for a put and 22.672 for a call, see
Table 2 Boyle, Evnine, and Gibbs (1989)
Put
Call
n steps
Standard lattice
Recursive lattice
Standard lattice
Recursive lattice
10
0.9112 (2.485 	102)
0.9617 (2.574 	102)
21.8601 (8.119 	101)
22.2488 (4.232 	101)
20
0.9192 (1.678 	102)
0.9463 (1.030 	102)
22.2807 (3.913 	101)
22.4640 (2.080 	101)
30
0.9232 (1.276 	102)
0.9416 (5.640 	103)
22.4137 (2.583 	101)
22.5339 (1.381 	101)
40
0.9254 (1.056 	102)
0.9394 (3.370 	103)
22.4792 (1.928 	101)
22.5686 (1.034 	101)
50
0.9268 (9.180 	103)
0.9380 (2.025 	103)
22.5182 (1.538 	101)
22.5894 (8.259 	102)
60
0.9278 (8.236 	103)
0.9371 (1.135 	103)
22.5441 (1.279 	101)
22.6033 (6.875 	102)
Table 12.8
The computed values and absolute errors for European options on the minimum of three
assets. A binomial lattice was used and we show how the accuracy of the results depends on the number of
time steps. The parameters are: E ¼ 100:0, S1 ¼ S2 ¼ S3 ¼ 100:0, r ¼ 0:1,  ¼ 1:0, 1 ¼ 2 ¼ 3 ¼ 0:2,
12 ¼ 13 ¼ 23 ¼ 0:5, q1 ¼ q2 ¼ q3 ¼ 0:0. The accurate values are 7.403 for a put and 5.249 for a call, see
Table 2 Boyle, Evnine, and Gibbs (1989)
Put
Call
n steps
Standard lattice
Recursive lattice
Standard lattice
Recursive lattice
10
7.0759 (3.271 	101)
7.3658 (3.723 	102)
5.2072 (4.176 	102)
5.2359 (1.312 	102)
20
7.2402 (1.628 	101)
7.3865 (1.653 	102)
5.2263 (2.269 	102)
5.2406 (8.414 	103)
30
7.2953 (1.077 	101)
7.3931 (9.926 	102)
5.2334 (1.560 	102)
5.2429 (6.060 	102)
40
7.3229 (8.015 	102)
7.3963 (6.676 	103)
5.2371 (1.192 	102)
5.2443 (4.749 	103)
50
7.3394 (6.357 	102)
7.3983 (4.741 	103)
5.2393 (9.665 	102)
5.2451 (3.922 	103)
60
7.3505 (5.251 	102)
7.3995 (3.459 	103)
5.2409 (8.143 	103)
5.2456 (3.353 	103)
270
Pricing Assets

The result of pricing three asset options, in which 12 ¼ 13 ¼ 0:5, and 23 ¼ 0:5,
are given in Tables 12.10 to 12.12.
Table 12.9
The computed values and absolute errors for a European put option on the maximum of three
assets. A truncated binomial lattice was used and we show how the accuracy depends on the value of
maxindex. The parameters are: E ¼ 100:0, S1 ¼ S2 ¼ S3 ¼ 100:0, r ¼ 0:1,  ¼ 1:0, 1 ¼ 2 ¼ 3 ¼ 0:2,
12 ¼ 13 ¼ 23 ¼ 0:5, q1 ¼ q2 ¼ q3 ¼ 0:0. The first column gives the value of maxindex, the second
column the computational time in milliseconds and the third column the computed value of the option and
also the absolute error in brackets. The accurate value is 0.9290 (took 1633 ms to compute) and was obtained
using a standard lattice with nsteps ¼ 80
max_index
Time (ms)
Value (error)
14
20
0.3464 (5.8254 	101)
16
30
0.4976 (4.3142 	101)
18
50
0.6344 (2.9458 	101)
20
60
0.7432 (1.8581 	101)
22
81
0.8204 (1.0858 	101)
24
100
0.8700 (5.8935 	102)
26
121
0.8992 (2.9782 	102)
28
140
0.9149 (1.4036 	102)
30
181
0.9228 (6.1763 	103)
32
220
0.9264 (2.5393 	103)
34
270
0.9280 (9.7559 	104)
36
320
0.9286 (3.5018 	104)
38
391
0.9289 (1.1735 	104)
40
441
0.9289 (3.6673 	105)
42
521
0.9290 (1.0672 	105)
Table 12.10
The computed values and absolute errors for European options on the maximum of
three assets. A binomial lattice was used and we show how the accuracy depends on the number of time
steps. The parameters are: E ¼ 100:0, S1 ¼ S2 ¼ S3 ¼ 100:0, r ¼ 0:1,  ¼ 1:0, 1 ¼ 2 ¼ 3 ¼ 0:2,
12 ¼ 0:5, 13 ¼ 0:5, 23 ¼ 0:5, q1 ¼ q2 ¼ q3 ¼ 0:0. The accurate values are 0.0526 for a put and
27.8271 for a call, and were computed using Monte Carlo simulation with 107 paths
Put
Call
n steps
Standard lattice
Recursive lattice
Standard lattice
Recursive lattice
10
0.0122 (4.041 	102)
0.0273 (2.531 	102)
27.3180 (5.091 	101)
27.5666 (2.605 	101)
20
0.0295 (2.314 	102)
0.0396 (1.301 	102)
27.5743 (2.528 	101)
27.6963 (1.308 	101)
30
0.0366 (1.600 	102)
0.0438 (8.770 	103)
27.6589 (1.682 	101)
27.7396 (8.745 	102)
40
0.0404 (1.221 	102)
0.0460 (6.618 	103)
27.7010 (1.261 	101)
27.7614 (6.568 	102)
50
0.0427 (9.868 	103)
0.0473 (5.316 	103)
27.7263 (1.008 	101)
27.7745 (5.258 	102)
60
0.0443 (8.280 	103)
0.0482 (4.444 	103)
27.7431 (8.396 	102)
27.7833 (4.383 	102)
Multiasset European and American options
271

12.7
FOUR ASSET OPTIONS
The jump probabilities for a binomial lattice which computes options on four
assets is given in Appendix D.3, and computer code is available on the CD
ROM. The results of using a four-dimensional binomial lattice to price options
are presented in Tables 12.13 and 12.14.
Table 12.11
The computed values and absolute errors for European options on the minimum of
three assets. A binomial lattice was used and we show how the accuracy depends on the number of time
steps. The parameters are: E ¼ 100:0, S1 ¼ S2 ¼ S3 ¼ 100:0, r ¼ 0:1,  ¼ 1:0, 1 ¼ 2 ¼ 3 ¼ 0:2,
12 ¼ 0:5, 13 ¼ 0:5, 23 ¼ 0:5, q1 ¼ q2 ¼ q3 ¼ 0:0. The accurate values are 9.2776 for a put and 1.5847
for a call, and were computed using Monte Carlo simulation with 107 paths
Put
Call
n steps
Standard lattice
Recursive lattice
Standard lattice
Recursive lattice
10
8.9646 (3.130 	101)
9.2791 (1.457 	103)
1.4047 (1.800 	101)
1.5446 (4.007 	102)
20
9.1231 (1.545 	101)
9.2796 (1.979 	103)
1.4963 (8.836 	102)
1.5634 (2.125 	102)
30
9.1749 (1.027 	101)
9.2792 (1.594 	103)
1.5261 (5.857 	102)
1.5703 (1.440 	102)
40
9.2007 (7.694 	102)
9.2789 (1.299 	103)
1.5409 (4.381 	102)
1.5738 (1.089 	102)
50
9.2161 (6.151 	102)
9.2787 (1.088 	103)
1.5497 (3.499 	102)
1.5759 (8.752 	103)
60
9.2264 (5.123 	102)
9.2785 (9.336 	104)
1.5556 (2.913 	102)
1.5774 (7.317 	103)
Table 12.12
The computed values and absolute errors for a European put option on the maximum
of three assets. A truncated binomial lattice was used and we show how the accuracy depends on the value
of maxindex. The parameters are: E ¼ 100:0, S1 ¼ S2 ¼ S3 ¼ 100:0, r ¼ 0:1,  ¼ 1:0, 1 ¼ 2 ¼
3 ¼ 0:2, 12 ¼ 0:5, 13 ¼ 0:5, 23 ¼ 0:5, q1 ¼ 0:0, q2 ¼ 0:0, q3 ¼ 0:0. The first column gives the value
of maxindex, the second column the computational time in milliseconds and the third column the
computed value of the option and also the absolute error in brackets. The accurate value is 0.0463 (took
1632 ms to compute) and was obtained using a standard lattice with nsteps ¼ 80
max_index
Time (ms)
Value (error)
14
20
0.0328 (1.3545 	102)
16
30
0.0397 (6.6100 	103)
18
41
0.0434 (2.8917 	103)
20
60
0.0452 (1.1577 	103)
22
70
0.0459 (4.2916 	104)
24
100
0.0462 (1.4810 	104)
26
120
0.0463 (4.7659 	105)
28
150
0.0463 (1.4299 	105)
272
Pricing Assets

Table 12.13
The computed values and absolute errors for European options on the maximum of four
assets. A binomial lattice was used and we show how the accuracy depends on the number of time steps.
The parameters are: E ¼ 100:0, S1 ¼ S2 ¼ S3 ¼ S4 ¼ 100:0, r ¼ 0:1,  ¼ 1:0, 1 ¼ 2 ¼ 3 ¼ 4 ¼ 0:2,
12 ¼ 0:5, 13 ¼ 0:5, 23 ¼ 0:5, q1 ¼ q2 ¼ q3 ¼ q4 ¼ 0:0. The accurate values are 0.6309 for a put and
25.2363 for a call, and were computed using Monte Carlo simulation with 107 paths
Put
Call
n steps
Estimated value
Error
Estimated value
Error
4
0.6548
2.386 	102
22.1403
3.096
8
0.6268
4.129 	103
23.8640
1.372
12
0.6246
6.275 	103
24.3630
8.733 	101
16
0.6251
5.836 	103
24.5934
6.429 	101
20
0.6257
5.167 	103
24.7270
5.093 	101
24
0.6263
4.570 	103
24.8144
4.219 	101
28
0.6268
4.074 	103
24.8762
3.601 	101
32
0.6272
3.665 	103
24.9222
3.141 	101
Table 12.14
The computed values and absolute errors for European options on the minimum of four
assets. A binomial lattice was used and we show how the accuracy depends on the number of time steps.
The parameters are: E ¼ 100:0, S1 ¼ S2 ¼ S3 ¼ S4 ¼ 100:0, r ¼ 0:1,  ¼ 1:0, 1 ¼ 2 ¼ 3 ¼ 4 ¼ 0:2,
12 ¼ 0:5, 13 ¼ 0:5, 23 ¼ 0:5, q1 ¼ q2 ¼ q3 ¼ q4 ¼ 0:0. The accurate values are 8.5394 for a put and
4.0662 for a call, and were computed using Monte Carlo simulation with 107 paths
Put
Call
n steps
Estimated value
Error
Estimated value
Error
4
7.8274
7.120 	101
3.5676
4.986 	101
8
8.1571
3.823 	101
3.8528
2.134 	101
12
8.2794
2.600 	101
3.9300
1.362 	101
16
8.3429
1.965 	101
3.9659
1.003 	101
20
8.3815
1.579 	101
3.9868
7.944 	102
24
8.4075
1.319 	101
4.0004
6.577 	102
28
8.4262
1.132 	101
4.0101
5.612 	102
32
8.4402
9.920 	102
4.0173
4.894 	102
Multiasset European and American options
273

Chapter 13
Dealing with missing data
13.1
INTRODUCTION
So far in all our discussions we have assumed that there are no missing values in the
financial data that is used to estimate the asset volatility. In practice this is rarely the
case. Reasons for this include: the variation in trading times of the stock exchanges
across the world, technical problems with storing/retrieving the data, and disruptive
social/economic events in various countries.
Some very simplistic approaches to dealing with missing data include:
. Replacing the missing value by the preceding (known) value.
. Excluding all the data collected at a given time if it contains at least one missing
value.
The last method could result in a large amount of very useful information being
ignored. For example, just because no data is available from one country’s stock
exchange does not mean the data collected from all the other financial markets is not
useful.
Accurately replacing missing data is of great importance if good estimates of the
volatility and covariance of assets are to be obtained, and used as input parameters to
the option pricing and portfolio models that are discussed here.
Here we will consider data with values missing at random, that is when the
probability of a missing variate value is not related to the values of other variates.
The data is assumed to consist of n observations (rows) and p variates (columns), and
takes the form of a n by p matrix. We will let the p element vector Xi denote the ith
observation and the row vector X denote the mean variate values. The kth element of
Xi, Xi,k, represents the value of the kth variate for the ith observation, and the kth
element of X, Xk represents the mean value of the kth variate. If there are no missing
values then we calculate the p  p covariance matrix as follows:
Cjk ¼ 1
n
X
n
i¼1
ðXi;j  XiÞðXi;k  XkÞ
or in more compact notation:
C ¼ 1
n
X
n
i¼1
ðXi  XÞðXi  XÞT

where
X ¼
X
p
i¼1
Xi
However, when the data contains missing values it is not possible to calculate the
covariance matrix in this manner.
In this section two methods of filling in missing data are considered, they are:
. Iterative multivariate regression, which we call MREG.
. The EM algorithm.
We will now describe both of these approaches in more detail.
13.2
ITERATIVE MULTIPLE LINEAR REGRESSION, MREG
This method fills in missing values by performing multiple linear regression on the
columns of the data matrix; see Beale and Little (1975), Orchard and Woodbury
(1972), and Little and Rubin (1987). We will denote the n element column vector
containing the observations of the kth variate by yk.
The procedure is as follows:
Step 1
Replace any missing values in column vectors yk, k ¼ 1, . . . , p by the corresponding
mean value. That is if the kth column vector yk contains nm missing values then these
are replaced by yk, which is calculated as
yk ¼
1
ðn  nmÞ
X
n
i¼1
Xi;k
where Xi,k is taken to be zero if it is missing.
Step 2
Starting with the first column as the dependent variable perform a multiple linear
regression for each variable on the remaining p  1 independent variables. After each
regression update the missing values in the dependent variable with those values
obtained from the regression.
This works as follows: with the first column as the dependent variable the n
element regression vector ^y1 can be written as:
^y1 ¼ C þ 2y2 þ 3y3 þ    þ pyp
where C is a vector of size n with all elements Ci, i ¼ 1, . . . , n ¼ c, and the scalars
i, i ¼ 2, . . . , p are the regression coefficients.
Here we assume that the data has been centred about the origin and use
^y1 ¼ 2y2 þ 3y3 þ    þ pyp
Dealing with missing data
275

We denote the ith element of ^y1 by ^y1
i , and if the ith element of y1 is a missing value,
which is the data element Xi,1, we update using:
Xi;1 ¼ ^y1
i
Similarly when the kth column is the dependent variable we have:
^yk ¼ Y
where Y is a (p  1)  n matrix which contains all the column vectors yj, j ¼ 1, . . . , p,
except yk, and the (p  1) element vector  contains the regression coefficients. If the
ith element of yk, denoted by yk
i , is a missing value, then we update the data using:
Xi;k ¼ ^yk
i
Step 3
We now compute the current mean values of each variable. The mean value of the
kth variable is computed as:
yk ¼ 1
n
X
n
i¼1
Xi;k
If the difference between the current mean values and the previous mean values is
greater than a specified tolerance we repeat step 2. If step 2 has been repeated more
than a specified number of times we stop. The function MREG, which implements
this method, is given in Code excerpt 13.1 below.
void MREG(double x[], long num, long m, double tol, long max_cycle, long *iflag)
{
/* Input parameters:
x[]
— if put is 0 then a call option, otherwise a put option
num
— the number of time steps, the zeroth time step is the root node of the lattice
m
— the number of time steps, the zeroth time step is the root node of the lattice
tol
— if opt_type is 0 then an option on the maximum of two asset otherwise an option on the minimum
of two assets
max_cycle
— if is_american is 0 then a European option, otherwise an American option.
Output parameters:
x[]
— the value of the option,
iflag
— an error indicator.
*/
/* The missing data in the matrix X is overwritten by the estimated values */
double rss;
long row_ptr, col_ptr, i, jj, ip, rank, j, k;
double df, zero ¼ 0.0;
Boolean svd;
Nag_IncludeMean mean;
double loc_tol, tmp, sum, *b;
double *nmeans, *means, *cov, *h, *p, *q, *res, *se, *com_ar, *y;
double *wtptr ¼ (double *)0;
long *sx, dep_var, tdq, count;
NagError loc_fail;
Boolean terminate;
long num_missing, *missing_row, *missing_column;
276
Pricing Assets

#define Y(I) y[(I)1]
#define MISSING_ROW(I) missing_row[(I)1]
#define MISSING_COLUMN(I) missing_column[(I)1]
#define SX(I) sx[(I)1]
#define MEANS(I) means[(I)1]
#define NMEANS(I) nmeans[(I)1]
#define X(I,J) x[((I)1) * m þ ((J)1)]
#define WX(I,J) wx[((I)1) * m þ ((J)1)]
#define RES(I) res[(I)1]
#define B(I) b[(I)1]
mean ¼ 286; /* There is no constant term in the regression, it will pass through the origin */
ip ¼ m  1;
tdq ¼ ip þ 1;
/* Allocate arrays: cov(ip*(ipþ1)/2), b(ip), se(ip), res(num), sx(ip), h(num), y(num), q(num*tdq),
p((2*ip)þ(ip*ip)),com_ar (5*(ip1)þip*ip), means(m), nmeans(m) */
/* Initial processing of the missing data set all missing values to the variable means */
*iflag ¼ 0;
num_missing ¼ 0;
for (j ¼ 1; j <¼m; þþj) {
sum ¼ zero;
for (i ¼ 1; i <¼ num; þþi) {
if(X(i,j) !¼  999.0) {
sum ¼ sum þ X(i,j);
}
else {
þþnum_missing;
}
}
MEANS(j) ¼ sum/(double)(num  num_missing);
}
/* Allocate arrays: missing_row(num_missingþ 1), missing_ column(num_missingþ 1) */
/* Set the indices for the missing data Note: Here (as opposed to the EM) we use column order
addressing  since the algorithm is column based. */
num_missing ¼ 0;
for (j ¼ 1; j <¼m; þþj) {
for (i ¼ 1; i <¼ num; þþi) {
if (X(i,j) ¼¼ 999.0) {
þþnum_missing;
MISSING_ROW(num_missing) ¼ i;
MISSING_COLUMN(num_missing) ¼ j;
}
}
}
dep_var ¼ 1;
count ¼ 0;
terminate ¼ FALSE;
loc_tol ¼ 1.0e 8;
while ((!terminate)&&(count <¼ max_cycle)) { /* outer cycle loop */
/* replace missing variable values with their means */
col_ptr ¼ 1;
row_ptr ¼ 1;
for (j ¼ 1; j <¼ m; þþj) {
for (i ¼ 1; i <¼ num; þþi) {
while ((col_ptr <¼ num_missing) && (MISSING_COLUMN (col_ptr) ¼ ¼ j)) {
i ¼ MISSING_ROW(row_ptr);
X(i,j) ¼ MEANS(j);
þþrow_ptr;
þþcol_ptr;
}
}
/* if (col_ptr > num_missing) printf (‘‘col_ptr > num_ missing /n’’); */
}
col_ptr ¼ 1;
row_ptr ¼ 1;
for (jj ¼ 1; jj <¼ m; þþjj) { /* loop over all the variables selecting one as the dependent */
/* variable for a multiple regression on the others */
for (j¼ 1; j <¼m; þþj) {
SX(j) ¼ 1;
}
SX(dep_var) ¼ 0;
for (i¼ 1; i <¼ num; þþi) { /* load the dependent variable into the vector y */
Y(i) ¼ X(i,dep_var);
}
g02dac(mean, num, &X(1,1), m, m, &SX(1), ip, &Y(1), wtptr, &rss, &df, &B(1),se, cov, &RES(1), h, q, tdq,
&svd, &rank, p, loc_tol, com_ar, &loc_fail);
Dealing with missing data
277

/* load the estimated values back into the data matrix WX */
for (i¼ 1; i <¼ num; þþi) {
if ((MISSING_COLUMN(col_ptr) ¼¼ dep_var) && (MISSING_ ROW(row_ptr) ¼¼ i)) {
k ¼ MISSING_ROW(row_ptr);
þþrow_ptr;
þþcol_ptr;
X(k,dep_var) ¼ Y(i)  RES(i);
}
}
if (loc_fail.code !¼ NE_NOERROR) printf (‘‘ERROR in routine \n’’);
sum ¼ zero;
for (i ¼ 1; i <¼ num; þþi) { /* calculate the new means */
sum ¼ sum þ X(i,dep_var);
}
NMEANS(dep_var) ¼ sum/(double)num;
dep_var ¼ dep_var þ 1;
if (dep_var > m) dep_var ¼ 1;
}
/* now check for the termination criterion */
terminate ¼ TRUE;
for (j ¼ 1; j <¼ m; þþj) {
tmp ¼ FABS(MEANS(j)NMEANS(j));
if (tmp > tol) {
terminate ¼ FALSE;
}
}
for (j ¼ 1; j <¼ m; þþj) {
MEANS(j) ¼ NMEANS(j);
}
if (terminate) printf (‘‘Stop iterating /n’’);
count ¼ count þ 1;
}
}
Code excerpt 13.1
Function MREG, which uses iterative multiple linear regression to fill in
missing values
13.3
THE EM ALGORITHM
The EM algorithm is an iterative method and involves both an Estimation step (or
E-step) and a Prediction step, also known as a Maximum likelihood step (or M-step),
see Dempster et al. (1977) and Little and Rubin (1987).
Here we assume that the incomplete n  p data matrix has been generated by a p
variate normal distribution and we would like to estimate the mean and covariance
matrix of this distribution. Code excerpt 13.2 provides an implementation of the EM
algorithm which uses a one-pass updating technique for both the mean and covar-
iance matrix, see West (1979) and Chan et al. (1982).
The steps are explained below.
The estimation step
Here we estimate the sample mean ~X (also denoted ), and sample covariance matrix
~ using the current sample data values. The estimates, of the mean, sum of squares
about the mean, and the covariance matrix, based on the first i observations are
denoted by X[i], S2
[i] and P[i] respectively.
The updating equations, see Appendix F.5, for these quantities are, for the mean
X½i	 ¼ X½i1	 þ 1
i Xi  X½i1	


ð13:1Þ
278
Pricing Assets

the sum of squares about the mean is updated as
S2
½i	 ¼ S2
½i1	 þ
i  1
i


Xi  X½i1	


Xi  X½i1	


ð13:2Þ
and the sum of cross products about the mean is updated as
P½i	 ¼ P½i1	 þ
i  1
i


Xi  X½i1	


Yi  Y½i1	


ð13:3Þ
The estimated covariance matrix ~, based on the first i observations, is then
obtained using
~ ¼ P½i	
i  1
ð13:4Þ
The prediction step
For each vector Xj with missing values let x(1)
j
denote the missing components and
x(2)
j
denote those components which are known. Thus we have: Xj ¼ [x(1)
j , x(2)
j ] and
 ¼ [(1)
j , (2)
j ]. Given the estimates ~ and ~ from the E-step we use the mean of
the conditional normal distribution of x(1), given x(2), to predict the missing values.
That is:
~xð1Þ
j
¼ Eðxð1Þ
j jxð2Þ
j ; ~; ~Þ ¼ ~ð1Þ þ ~12 ~1
22 ðxð2Þ
j
 ~ð2ÞÞ
ð13:5Þ
In Equation 13.5 we have used the result, see Appendix E, that if:
Xj  Nð; Þ
with  ¼ (1)=(2) and  ¼ (11j12)=(21j22), and j22j > 0 then:
xð1Þ
j
 Nð0; 0Þ
where
0 ¼ ð1Þ þ 121
22 ðxð2Þ  ð2ÞÞ
and
0 ¼ 11  121
22 21
It can thus be seen that the covariance matrix does not depend on the value of the
conditioning variable, x(2).
void EM(double x[], long num, long m, double tol, long max_cycle, long *iflag)
{
long l_count, i, j, k, l, p, q;
double zero ¼ 0.0;
double fac, loc_tol, tmp, tmp1, tmp2, sum;
double *wx, *nmeans, *means, *xmeans, *sigma, *nsigma, *sigma_ kk, *sigma_uu, *sigma_ku;
double *work_mat, *xsigma, *work_vec;
Dealing with missing data
279

long row_ptr, col_ptr, ii, num_missing, id;
double d1;
long *missing_index, *known_index, n_missing, n_known, count, ind, *missing_row, *missing_column;
NagError loc_fail;
Boolean terminate;
/* define for easy referencing of vectors and matrices */
#define MISSING_INDEX(I) missing_index[(I)1]
#define MISSING_ROW(I) missing_row[(I)1]



#define SIGMA_UU(I,J) sigma_uu[((I)1) * m þ ((J)1)]
/* Allocate arrays: sigma(m*m), nsigma(m*m), sigma_kk(m*m), sigma_uu(m*m), means(m), nmeans(m),
work_mat(m*m), work_vec(m), missing_index(m), known_index(m) */
/* initial processing of the missing data set all missing values to the variable means */
num_missing ¼ 0;
for (j ¼ 1; j <¼m; þþj){
sum ¼ zero;
count ¼ 0;
for (i ¼ 1; i <¼ num; þþi){
if(X(i,j) !¼ 999.0) {
sum ¼ sum þ X(i,j);
þþcount;
}
else {
þþnum_missing;
}
}
MEANS(j) ¼ sum/(double)count; /* calculate the overall means */
}
/* Allocate arrays: missing_row(num_missingþ1), missing_column (num_missingþ1) */
/* Set the indices for the missing values */
num_missing ¼ 0;
for (i ¼ 1; i <¼num; þþi) {
for (j ¼ 1; j <¼ m; þþj){
if(X(i,j) ¼¼ 999.0) {
þþnum_missing;
MISSING_ROW(num_missing) ¼ i;
MISSING_COLUMN(num_missing) ¼ j;
X(i,j) ¼ MEANS(j);
}
else {
X(i,j) ¼ X(i,j);
}
}
}
/* Initialise data matrix */
row_ptr ¼ 1;
col_ptr ¼ 1;
for (i ¼ 1; i <¼ num; þþi) { /* Set missing values to the appropriate variate mean */
while ((row_ptr <¼ num_missing) && (MISSING_ROW(row_ptr) ¼ ¼ i)){
j ¼ MISSING_COLUMN(col_ptr);
X(i,j) ¼ MEANS(j);
þþrow_ptr;
þþcol_ptr;
}
}
for (i ¼ 1; i <¼ m; þþi){
for (j ¼ 1; j <¼ m; þþj){
SIGMA(i,j) ¼ zero;
}
}
for (i ¼ 1; i <¼ m; þþi) { /* Estimate the initial matrix SIGMA */
for (j ¼ 1; j <¼ m; þþj){
tmp1 ¼ zero;
for (k ¼ 1; k <¼ num; þþk){
SIGMA(i,j) ¼ SIGMA(i,j)þ (X(k,i)MEANS(i))*(X(k,j) MEANS(j));
}
SIGMA(i,j) ¼ (SIGMA(i,j)/(double)(num));
}
}
count ¼ 0;
terminate ¼ FALSE;
loc_tol ¼ 1.0e8;
while ((!terminate)&&(count <¼ max_cycle)) { /* Outer cycle loop */
for (j ¼ 1; j <¼ m; þþj) { /* initialize NMEANS */
280
Pricing Assets

NMEANS(j) ¼ zero;
}
/* Initialize NSIGMA, it will be used to provide an estimate for a new value of SIGMA,
based on West’s updating method */
for (i ¼ 1; i <¼m; þþi){
for (j ¼ 1; j <¼m; þþj){
NSIGMA(i,j) ¼ zero;
}
}
row_ptr ¼ 1;
col_ptr ¼ 1;
for (ii ¼ 1; ii <¼ num; þþii) { /* Loop over all observations */
n_missing ¼ 0;
n_known ¼ 0;
while ((row_ptr <¼ num_missing) && (MISSING_ROW(row_ptr) ¼ ¼ ii)){
j ¼ MISSING_COLUMN(col_ptr);
þþrow_ptr;
þþcol_ptr;
þþn_missing;
MISSING_INDEX(n_missing) ¼ j;
}
k ¼ 1;
for (j ¼ 1; j <¼m; þþj){
if ((k <¼ n_missing) && (MISSING_INDEX(k) ¼¼ j)){
þþk;
}
else {
þþn_known;
KNOWN_INDEX(n_known) ¼ j;
}
}
if (n_missing > 0) { /* Are there missing values? */
if (n_missing ¼¼ m) { /* deal with the special case in which all the observation is missing */
for (i ¼ 1; i <¼ m; þþi){
X(ii,i) ¼ MEANS(i);
}
}
else { /* Form the partial covariance matrices SIGMA_UU, SIGMA_KK and SIGMA_KU */
for (i ¼ 1; i <¼ n_missing; þþi) { /* SIGMA_UU */
p ¼ MISSING_INDEX(i);
for (j ¼ 1; j <¼ n_missing; þþj){
q ¼ MISSING_INDEX(j);
SIGMA_UU(i,j) ¼ SIGMA(p,q);
}
}
for (i ¼ 1; i <¼ n_known; þþi) { /* SIGMA_KK */
p ¼ KNOWN_INDEX(i);
for (j ¼ 1; j <¼ n_known; þþj){
q ¼ KNOWN_INDEX(j);
SIGMA_KK(i,j) ¼ SIGMA(p,q);
}
}
for (i ¼ 1; i <¼ n_known; þþi) { /* SIGMA_KU */
p¼ KNOWN_INDEX(i);
for (j ¼ 1; j <¼ n_missing; þþj){
q¼ MISSING_INDEX(j);
SIGMA_KU(i,j) ¼ SIGMA(p,q);
}
}
/* Obtain INVERSE(SIGMA_KK) * SIGMA_KU by solving SIGMA _KK * X ¼ SIGMA_KU */
/* Can use cholseky factorisation since SIGMA_KK is positive definite */
f03aec (n_known, &SIGMA_KK(1,1), m, &WORK_VEC(1), &d1, &id, &loc_fail);
if (loc_fail.code !¼ NE_NOERROR){
printf (‘‘Cholesky factorisation error /n’’);
return;
}
else { /* solve the equation */
f04agc(n_known, n_missing, &SIGMA_KK(1,1), m, &WORK_VEC(1),
&SIGMA_KU(1,1), m, &WORK_MAT(1,1), m, &loc_fail);
}
/* Predict the mean values of the missing data in the current observation */
/* These values are stored in the array WORK_VEC */
for (i ¼ 1; i <¼ n_missing; þþi){
WORK_VEC(i) ¼ zero;
sum ¼ zero;
Dealing with missing data
281

for (k ¼ 1; k <¼ n_known; þþk){
p ¼ KNOWN_INDEX(k);
sum ¼ sum þ WORK_MAT(k,i) * (X(ii,p)  MEANS(p));
}
q ¼ MISSING_INDEX(i);
WORK_VEC(i) ¼ MEANS(q) þ sum;
X(ii,q) ¼ WORK_VEC(i); /* store the new estimates */
}
}/* end of else clause */
}/* end of n_missing > 0 clause */
/* Use West’s (1979) algorithm to update the means and predicted the covariance terms corresponding
to the cross product X_U * X_K^T in NSIGMA (Use West’s (1979) algorithm) */
fac ¼ (double)(ii  1)/(double)ii;
fac ¼ fac/(double)num;
for (i ¼ 1; i <¼ n_missing; þþi){
p ¼ MISSING_INDEX(i);
for (j ¼ 1; j <¼ n_missing; þþj){
q ¼ MISSING_INDEX(j);
NSIGMA(p,q) ¼ NSIGMA(p,q) þ (X(ii,p) NMEANS(p)) *(X (ii,q)  NMEANS(q))*fac;
}
}
for (i ¼ 1; i <¼ n_missing; þþi){
p ¼ MISSING_INDEX(i);
for (j ¼ 1; j <¼ n_known; þþj){
q ¼ KNOWN_INDEX(j);
NSIGMA(p,q) ¼ NSIGMA(p,q) þ (X(ii,p) NMEANS(p)) *(X (ii,q) NMEANS(q))*fac;
}
}
for (i ¼ 1; i <¼ n_missing; þþi){
p ¼ MISSING_INDEX(i);
for (j ¼ 1; j <¼ n_known; þþj){
q ¼ KNOWN_INDEX(j);
NSIGMA(q,p) ¼ NSIGMA(p,q);
}
}
/* Now update the covariance matrix using the known values, using West’s (1979) algorithm. */
for (i ¼ 1; i <¼ n_known; þþi){
p ¼ KNOWN_INDEX(i);
for (j ¼ 1; j <¼ n_known; þþj){
q ¼ KNOWN_INDEX(j);
NSIGMA(p,q) ¼ NSIGMA(p,q) þ(X(ii,p) NMEANS(p)) *(X (ii,q) NMEANS(q))*fac;
}
}
for (j ¼ 1; j <¼ n_missing; þþj){
l ¼ MISSING_INDEX(j);
NMEANS(l) ¼ NMEANS(l) þ ((X(ii,l)  NMEANS(l))/ (double )ii);
}
for (j ¼ 1; j <¼ n_known; þþj){
l ¼ KNOWN_INDEX(j);
NMEANS(l) ¼ NMEANS(l) þ ((X(ii,l)  NMEANS(l))/ (double)ii);
}
}/* end of the observation loop (ii) */
/* Now check for the termination criterion */
terminate ¼ TRUE;
for (j ¼ 1; j <¼ m; þþj){
tmp ¼ FABS(MEANS(j)NMEANS(j));
if (tmp > tol){
terminate ¼ FALSE;
}
}
/* get ready for the next iteration through the data */
for (j ¼ 1; j <¼ m; þþj){
MEANS(j) ¼ NMEANS(j);
}
for (i ¼ 1; i <¼ m; þþi){
for (j ¼ 1; j <¼ m; þþj){
SIGMA(i,j) ¼ NSIGMA(i,j);
}
}
if (terminate) printf (‘‘will terminate /n’’);
count ¼ count þ 1;
}
/* count loop */
}
Code excerpt 13.2
Function which uses the EM algorithm to fill in missing values
282
Pricing Assets

To test the accuracy of the missing data algorithms we generate sample data with
known mean s and known covariance matrix Cs. We then remove, at random, a
given percentage of the data, and try to reconstruct the original data using either the
EM algorithm or function MREG, which uses iterative multiple linear regression. If
Cs is the sample covariance matrix of the reconstructed data then the quality of this
estimate can be quantified using the following distance:
D ¼
X
p
i¼1
X
p
j¼1
ðCs
ij  Cs
i;jÞ2
(
)1=2
ð13:6Þ
or in more compact notation:
D ¼ jjCs  Csjj
ð13:7Þ
The sample data was generated from a normal distribution with mean  and
covariance matrix C given by:
Cij ¼ i  j
10 ;
i ¼ 1; . . . ; p; for i 6¼ j
ð13:8Þ
Cii ¼ 1:1i;
i ¼ 1; . . . ; p
ð13:9Þ
and let the variate means be defined by:
i ¼ 2i;
i ¼ 1; . . . ; p
ð13:10Þ
Inspection of the results in Tables 13.1 to 13.3 shows that the time taken by the
EM algorithm increases as the amount of missing data is raised from 5 per cent to
25 per cent; this is in contrast to the time taken by MREG which is almost
Table 13.1
Five per cent of the data is missing at random. A comparison of the accuracy of the estimated
covariance matrix computed using the EM algorithm, given in Code excerpt 13.2, algorithm and the
function MREG, given in Code excerpt 13.1. The n observations were generated from a multivariate
normal distribution Nð, CÞ, with  and C obtained from Equations 13.8 to 13.10, with p ¼ 8. The
computational time is measured in milliseconds and the quality of estimation, D, is defined by
Equation 13.6
MREG
EM
n
Time (ms)
Distance, D
Time (ms)
Distance, D
100
80
0.6528
30
0.6980
400
100
0.6293
60
0.7306
5000
2523
0.6193
540
0.6404
10000
5448
0.6299
1031
0.6642
100000
5561
0.6394
9674
0.6990
300000
165157
0.6396
26758
0.7048
Dealing with missing data
283

independent of the amount of missing data. It can be seen that, for less than 400
observations, the performance of MREG is similar to that of the EM algorithm.
However, as the number of observations is increased the speed of MREG decreases
dramatically; although the accuracy of achieved is still similar to that obtained by
the EM algorithm.
Table 13.2
Ten per cent of the data is missing at random. A comparison of the accuracy of the estimated
covariance matrix computed using the EM algorithm, given in Code excerpt 13.2, and the function
MREG, given in Code excerpt 13.1. The n observations were generated from a multivariate normal
distribution Nð, CÞ, with  and C obtained from Equations 13.8 to 13.10, with p ¼ 8. The computational
time is measured in milliseconds and the quality of estimation, D, is defined by Equation 13.6
MREG
EM
n
Time (ms)
Distance, D
Time (ms)
Distance, D
100
50
1.8500
50
1.7981
400
80
0.9742
100
1.1453
5000
2503
1.0006
871
1.0819
10000
5377
1.0120
1422
1.0814
100000
56141
1.0184
12969
1.0901
300000
164887
1.0165
38885
1.0906
Table 13.3
Twenty per cent of the data is missing at random. A comparison of the accuracy of the
estimated covariance matrix computed using the EM algorithm, given in Code excerpt 13.2, and the
function MREG, given in Code excerpt 13.1. The n observations were generated from a multivariate
normal distribution Nð, CÞ, with  and C obtained from Equations 13.8 to 13.10, with p ¼ 8. The
computational time is measured in milliseconds and the quality of estimation, D, is defined by
Equation 13.6
MREG
EM
n
Time (ms)
Distance, D
Time (ms)
Distance, D
100
30
2.3360
50
2.6281
400
80
1.7587
120
1.6857
5000
2924
1.7648
1191
1.6113
10000
6329
1.7600
2233
1.5871
100000
65454
1.734
18407
1.5729
300000
195611
1.7587
48369
1.5703
284
Pricing Assets

Part III
Financial Econometrics


## Interest Rate Derivatives


Chapter 14
Introduction
Here we are concerned with modelling financial returns, see Section 14.1, which are
generated from share prices, stock market indices, or currency exchange rates.
Here we describe the financial returns data using regression-based models of the
form:
yi ¼ XT
i  þ i;
i ¼ 1; . . . ; n
ð14:1Þ
where n is the length of the time series, yi is the ith return, Xi is a vector of size k,
 is a vector of k regression coefficients and i are the residuals. The variance 2
i
of the ith residual is thus given by 2
i ¼ E[2
i ]. In finance literature the term
volatility depends on context, and refers either to the variance 2
i or the standard
deviation i. Equation 14.1 looks deceptively simple and it hides the fact that we
are really interested in determining the characteristics of i so that we can model
the volatility.
Empirical studies suggest that financial returns have the following characteristics:
(i)
Large returns occur more frequently than expected for a Gaussian distribution. This
means that the unconditional probability distribution for i has fatter tails (and
therefore a larger unconditional kurtosis) than that of a Gaussian distribution.
(ii) The variance (volatility) of the returns exhibit clustering. There are periods of high
volatility separated by regions of low volatility.
(iii) When bad news occurs it is often followed by high volatility. That is negative stock
market returns are usually followed by high volatility. For exchange rate returns data
it is not clear what constitutes bad news, since a large fall in the exchange rate may be
good or bad depending on your point of view.
(iv) In stock market data large negative returns (corresponding to bad news) occur
more frequently than large positive returns. This means that the unconditional
probability distribution of i is asymmetric about zero, and the probabilities on
the negative side of the distribution are higher than the probabilities on the
positive side. This asymmetry can be measured in terms of skewness. We thus
state that stock market data has been found to exhibit negative skewness. Again
there is no reason why exchange rate returns should have any particular sign
associated with the skewness.
In this part of the book we show how points (i) to (iv) can be modelled by using
symmetric and assymmetric GARCH models with the conditional probability

distribution of the residuals, i, having a Gaussian distribution with time varying
conditional variance hi. The standardized residuals Zi ¼ i=
ffiffiffiffihi
p
should then be
distributed as NID(0, 1), and so have a kurtosis of 3. However, it has also been
found that the standardized residuals are non-Gaussian and so other conditional
probability distributions for the residuals such as the Student’s t distribution and the
Generalized Error distribution are also considered.
Estimates of return volatility are used to assess the level of risk associated with
many financial products. Accurate measures and reliable forecasts of volatility are
crucial for option pricing techniques as well as trading and hedging strategies that
arise in portfolio allocation problems.
We assume minimal prior knowledge of statistics and aim to provide mathematical
details and proofs that may be taken for granted or omitted from more advanced
econometric literature. This is especially the case for the information provided
concerning the properties of various statistical distributions. Here the expected
values of the distribution are derived from first principles using integration, rather
than the more usual approach of either quoting standard results or using moment
generating functions. Here we concentrate on standard linear and nonlinear univari-
ate GARCH processes. However, information is also provided concerning other
models such as component GARCH, stochastic volatility models and Levy
processes. The testing of GARCH software is covered and comprehensive informa-
tion is supplied concerning the calculation of the first and second order derivatives of
the log likelihood function.
Before embarking on a detailed study of time series methods and applica-
tions to forecast the volatility of financial assets we will quote from a recent
article by Granger (2002). There reference is made to a survey of 40 papers which
compare the forecasting ability of techniques such as: historical and implied
volatility (see Part II Section 9.3.4), stochastic volatility (SV), and GARCH. It is
stated that:
1. Five papers find that GARCH beats HISTORICAL.
2. Five papers find that HISTORICAL beats GARCH.
3. Only three papers consider SV forecasts; one finds SV better than GARCH, one finds
GARCH better than SV, and a third paper finds SV better that GARCH for stocks but
the reverse for currencies.
4. Thirteen papers compare IMPLIED with HISTORICAL, with twelve preferring
IMPLIED.
5. Fourteen papers compare IMPLIED with GARCH; all but one find that IMPLIED
provides better forecasts. One paper also finds that IMPLIED performs better than SV.
Granger concludes that:
Overall, IMPLIED seems to be the superior technique with GARCH and HISTOR-
ICAL roughly equal second. The result is not really surprising as the IMPLIED fore-
casts are based on a wider information set than the alternatives, not just depending on
the past returns but also on using option prices. On the other hand, suitable options may
not always be available and so these forecasts cannot be used on many occasions.
288
Financial Econometrics

14.1
ASSET RETURNS
The return can be defined in several different ways.
If we let Pt denote the price (or index) at time t, and for simplicity assume a series
of n values Pt, t ¼ 1, . . . , n in which the sampling period is the unit time interval, then
the Simple net return, Rt, between instant t  1 and instant t, is:
SRt ¼ Pt  Pt1
Pt1
¼ Pt
Pt1
 1
ð14:2Þ
the Gross return, Rt, is defined as:
Rt ¼ Pt
Pt1
ð14:3Þ
The gross return compounded over k periods takes the form:
RtðkÞ ¼ Ptþk
Pt1
¼
Pt
Pt1


Ptþ1
Pt


Ptþ2
Ptþ1


	 	 	
Ptþk1
Ptþk2


Ptþk
Ptþk1


An alternative approach is to use the continuously compounded returns (or
logarithmic returns). This is defined using:
rt ¼ log
Pt
Pt1


¼ logðPtÞ  logðPt1Þ
ð14:4Þ
where log denotes the natural logarithm.
The return compounded over k periods is:
rtðkÞ ¼ logðPtþkÞ  logðPt1Þ
¼ logðPtþkÞ  logðPtþk1Þ þ logðPtþk1Þ  	 	 	 þ logðPtÞ  logðPt1Þ
rtðkÞ ¼ rt þ rtþ1 þ 	 	 	 þ rtþk1 þ rtþk
ð14:5Þ
Thus unlike multiperiod gross compounding which is a multiplicative process,
multiperiod continuous compounding is additive.
We also note that:
logðxÞ ¼ ðx  1Þ  1
2 ðx  1Þ2 	 	 	
for 2 
 x > 0
and therefore logðxÞ  x
when
x  1:
Since (Pt)=(Pt1)  1, Equations 14.2 and 14.4 give: rt  Rt: This means that the
simple net return is virtually the same as the logarithmic return. It may also be
convenient to create a scaled return series using:
rt ¼ flogðPtÞ  logðPt1Þg
ð14:6Þ
where  is the scale factor. When  ¼ 100 the series gives the percentage logarithm
returns.
If dividend payments, Dt, are included then Equation 14.4 takes the form:
rt ¼ log Pt þ Dt
Pt


ð14:7Þ
Introduction
289

This can be re-expressed using the following steps:
rt ¼ logðPtÞ  logðPt1Þ þ logðPt þ DtÞ  logðPtÞ
rt ¼ logðPtÞ  logðPt1Þ þ log 1 þ Dt
Pt


rt ¼ pt  pt1 þ log 1 þ expðdt  ptÞ
ð
Þ
ð14:8Þ
where pt ¼ log (Pt) and dt ¼ log (Dt). Equation 14.7 is a nonlinear function of the
logarithm of the dividend to price ratio, 	t ¼ log (Dt=Pt). If we linearize about the
mean value of 	t, 	, we then obtain:
rt ¼ k þ 
 pt þ ð1  
Þ dt  pt1
ð14:9Þ
where

 ¼
1
1 þ expð	Þ
and
k ¼  logð
Þ  ð1  
Þ log 1

  1




It can be seen that the returns rt are computed using a weighted sum of the
logarithm of stock price and the logarithm of the dividend. Empirical studies, see
Campbell et al. (1997), have found that 
 is about 0.96, which means that nearly all of
the contribution to the value of returns is from the stock price.
Proof of Equation 14.9
Since 	t ¼ dt  pt we have from Equation 14.8 that:
rt ¼ pt  pt1 þ f ð	tÞ
ð14:10Þ
where f (	t) ¼ log (1 þ exp (	t)).
Using a Taylor expansion about the mean value 	 we have:
f ð	tÞ ¼ f ð	Þ þ f 0ð	Þð	t  	Þ
ð14:11Þ
Now from elementary calculus we have:
f 0ð	Þ ¼
expð	Þ
1 þ expð	Þ
Substituting into Equation 14.11 we obtain:
f ð	tÞ ¼ f ð	Þ þ
expð	Þ
1 þ expð	Þ 	t  	


ð14:12Þ
letting 
 ¼
1
1 þ exp ( 	) we have:
logð1 þ expð	ÞÞ ¼  logð
Þ;
expð 	Þ ¼
1

  1


and 	 ¼ log 1

  1


Therefore Equation 14.11 gives:
f ð	tÞ ¼  logð
Þ þ
1

  1



ð	t  	Þ
f ð	tÞ ¼  logð
Þ þ ð1  
Þ	t  ð1  
Þ	
290
Financial Econometrics

Substituting into Equation 14.10 we have:
rt ¼ pt  pt1  logð
Þ þ ð1  
Þ	t  ð1  
Þ	
subsituting for 	
rt ¼  logð
Þ  ð1  
Þ log 1

  1




 pt1 þ ð1  
Þdt þ 
pt
which gives
rt ¼ k þ 
 pt þ ð1  
Þdt  pt1
QED
where
k ¼  logð
Þ  ð1  
Þ log 1

  1




Empirical studies have shown that in many instances the logarithm of dividend to
price ratio, Dt=Pt, can be taken as a constant, and in these circumstances we have
	t ¼ 	, t ¼ 1, . . . , n; where 	 is a constant.
14.2
NONSYNCHRONOUS TRADING
The nonsynchronous trading effect arises when data is assumed to be recorded at
certain times when in fact it is collected at other times. As an example the daily
closing security prices, which give the last transaction price for each security on the
previous day, do not occur at the same time each day. By referring to these values as
daily closing prices we incorrectly assume that they occur at equally spaced 24 hour
time intervals. As another example consider two stocks A and B, whose prices are
independent but stock A trades less frequently than B. If stock market news arrives
near the close of trade it is more likely to be reflected in the closing price of stock B
than that of stock A; this is because stock A may not trade after the arrival of the
information. The fact that stock A will respond to the new information after a
significant time lag can induce spurious correlations between the daily returns of
stocks A and B, if these are based on daily closing prices. This lagged response
can also induce negative autocorrelations in the daily returns of A. This is because
when A is not trading its observed return is zero, and when it does trade its returns
revert to the cumulated mean return.
Lo and MacKinlay (1990) have developed a nonsynchronous trading model which
captures these effects. It is assumed that a security has in each time period t an
unobserved or virtual continuously compounded return rt. These virtual returns
represent the changes in the true underlying value of the security; they reflect
changes in value caused by both company information and general stock market
information.
We suppose that at each time period there is the probability  that the security does
not trade; the probability that the security trades is then (1  ). The observed return,
ro
t , depends on whether the security trades or not. If the security does not trade in
period t then ro
t ¼ log (Pt=Pt1) ¼ log (1) ¼ 0. If on the other hand the security trades
Introduction
291

in period t, its observed return is taken as the sum of the virtual returns in period t and
all previous consecutive periods in which the security did not trade.
For example consider a sequence of six consecutive time periods in which the
security trades in periods 1, 2, and 6, but does not trade in periods 3, 4, and 5. The
nontrading model implies that the observed return in period 2 is the virtual return,
ro
2 ¼ r2, the observed return in periods 3, 4, and 5 are zero, ro
3 ¼ ro
4 ¼ ro
5 ¼ 0, and the
observed return in period 6 is the sum of the virtual returns from periods 3 to 6,
ro
6 ¼ r3 þ r4 þ r5 þ r6. Here the impact of news is captured in the virtual returns
process and the lag caused by nontrading is modelled in the observed returns process
ro
t . We will now define the variable kt which is the number of past consecutive
periods, at time t, for which the asset has not been traded. The mean and variance
of kt are related to the nontrading probability, , in the following manner:
E½kt ¼

1   ;
Var½kt ¼

ð1  Þ2
ð14:13Þ
Proof of Equation 14.13
First we will prove the equation for the mean.
E½kt ¼ 0ð1  Þ þ ð1  Þ þ 2ð1  Þ2 þ 3ð1  Þ3 þ 4ð1  Þ4 þ 	 	 	
E½kt ¼ ð1  Þð þ 22 þ 33 þ 44 þ 55 þ 	 	 	Þ
ð14:14Þ
¼  þ 22 þ 33 þ 44 þ 55  2  23  34  45  	 	 	
E½kt ¼  þ 2 þ 3 þ 4 þ 5 þ 	 	 	
ð14:15Þ
This is a Geometric Progression with first term  and common ratio , therefore:
E½kt ¼
X
1
j¼1
j ¼

1  
QED
Now we consider the equation for the variance of kt.
Var½kt ¼ E½k2
t   ðE½ktÞ2
ð14:16Þ
E½k2
t  ¼ 0ð1  Þ þ ð1  Þ þ 4ð1  Þ2 þ 9ð1  Þ3 þ 16ð1  Þ4
þ 25ð1  Þ5 þ 	 	 	
¼ ð1  Þf þ 42 þ 93 þ 164 þ 255 þ 	 	 	g
¼  þ 42 þ 93 þ 164 þ 255 þ 	 	 	  2  43  94  165  	 	 	
E½k2
t  ¼  þ 32 þ 53 þ 74 þ 95 þ 	 	 	
Now from Equation 14.15 we have
ðE½ktÞ2 ¼ ð þ 2 þ 3 þ 4 þ 5 þ 	 	 	Þ2 ¼ 2 þ 23 þ 34 þ 45 þ 	 	 	
So substituting into Equation 14.16
Var½kt ¼  þ 32 þ 53 þ 74 þ 95 þ 	 	 	  2  23  34  45  	 	 	
Var½kt ¼  þ 22 þ 33 þ 44 þ 55 þ 	 	 	
ð14:17Þ
292
Financial Econometrics

From Equations 14.14 and 14.13 we have:
E½kt ¼

1   ¼ ð1  Þð þ 22 þ 33 þ 45 þ 	 	 	Þ
ð14:18Þ
which means that Equation 14.17 can be written as:
Var½kt ¼

ð1  Þ2
QED
Substituting into Equation 14.13 we find that if  ¼ 0:75 then the average number
of consecutive periods of nontrading is three. If the asset trades on every period then
 ¼ 0 and both the mean and variance of kt are zero.
Lo and MacKinlay (1990) consider a virtual returns process of the form:
rt ¼  þ t
ð14:19Þ
where  is a constant drift term, t is zero mean IID noise. In this case:
E½ro
t  ¼ 
Var½ro
t  y ¼ 2 þ
2
1   2
ð14:20Þ
and
Corr½ro
t ro
tþn ¼ 2n
2 þ g2 ;
n > 0
ð14:21Þ
where 2 ¼ Var[rt] and g ¼ 2=ð1  Þ.
We thus conclude that nontrading does not affect the mean of the observed
returns. However, if the expected return of the security is nonzero, then nontrading
increases the observed variance of the security returns, and also induces negative
serial correlation in the returns.
14.3
BID-ASK SPREAD
The presence of the bid-ask spread means that instead of one price for each asset
there are now three: the bid price, the ask price and the actual transaction price which
need not be either the bid or ask price. To account for the impact of the bid-ask
spread Roll (1984) proposed the following model:
Pt ¼ P
t þ It s
2
ð14:22Þ
where Pt is the observed asset price at time t, P
t is the true asset price, s is the bid-ask
spread, and the IID indicator variable It which takes the value þ1 with probability
0.5 (to signify a buyer initiated bid) and the value 1 with probability 0.5 to indicate
a seller initiated ask.
The assumption that P
t is the true value of the security implies that E[It] ¼ 0, and
hence Pr(It ¼ 1) ¼ Pr(It ¼ 1) ¼ 0:5.
If the true security value, P
t , does not change with time then the process for the
price observed changes is:
Pt ¼ ðIt  It1Þ s
2
ð14:23Þ
Introduction
293

which means that:
Var½Pt ¼ s2
2
ð14:24Þ
Cov½Pt1; Pt ¼ s2
4
ð14:25Þ
Cov½Ptk; Pt ¼ 0;
k > 1
ð14:26Þ
Corr½Pt1; Pt ¼  1
2
ð14:27Þ
It can be seen that despite the fact that the true value is fixed Pt has volatility
and also negative correlation. This is caused by the bid-ask bounce. The reason for
this is as follows: If P
t is fixed than the observed price can only take on two
values, the bid price and the ask price. If the current price is the ask then the price
change between the current price and the previous price must either be zero or s,
and the price change between the next price and the current price must either be
zero or s; which induces negative covariance. The same is true if the current price
is the bid price.
If P
t changes with time, and its increments are serially uncorrelated and independ-
ent of It, then Equation 14.25 still applies. However, Equation 14.27 is no longer true,
and the correlation is now given by:
Corr½Pt1; Pt ¼ 
s2=4
s2=2 þ 2
p
ð14:28Þ
where 2
p is the variance of P
t .
The bid-ask spread s can be estimated from the covariance of the price changes
using:
s ¼ 2
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
Cov½Pt1Pt
p
ð14:29Þ
Estimating the bid-ask spread in this manner may seem rather strange when it is
already available from market data. However, the quoted value can differ from the
effective value, and in many cases transactions occur at prices within the bid-ask
spread. This is because discounts may be given to certain customers, and also,
if updating is not frequent enough, the quoted values for s may not be the actual
values used.
Roll’s model assumes that the value for s is a given constant, and is independent of
the value of P
t . For a more sophisticated model of the bid-ask spread see Glosten
and Milgrom (1985).
14.4
MODELS OF VOLATILITY
In this section we provide a brief overview of two methods that are commonly used to
model volatility in finance: stochastic volatility processes and Levy processes.
Here we give a short definition of each process. Section 14.5 gives more information
294
Financial Econometrics

on stochastic autoregressive processes and Section 14.6 provides more information on
the generalized hyperbolic Levy process.
14.4.1
Stochastic volatility models
A continuous standard Brownian process X can be discretized as:
Xt ¼ t þ t;
t  NIDð0; 1Þ
ð14:30Þ
where Xt is the value of the Brownian variate at time t, X0 ¼ 0,  is the constant drift,
and  is the constant volatility.
The stochastic volatility model, see Ghysels et al. (1996) and Taylor (1994), which
permits a time varying volatility, generalizes Equation 14.30 to:
Xt ¼  þ tt;
t  NIDð0; 1Þ
ð14:31Þ
where the time dependent volatility, t, is termed the stochastic volatility. We will
assume that the process t has no causal relationship with the process t. Thus it is
assumed that the process t is not caused by the process t, and also that the process t
does not cause the process t.
We will now consider the following two t processes.
1. t is an independent stochastic process
Here we take t to be a stochastic process that is independent of the information set  t1.
An example is the stochastic random autoregressive (ARV) model, which is dis-
cussed in Section 14.5.
The general form of an ARV(1) model is:
Xt ¼  þ t1t
ð14:32Þ
and
logðtÞ ¼  þ  logðt1Þ þ t
ð14:33Þ
where ,  and  are constants. The variates t and t are from an IID bivariate
normal distribution with correlation coefficient 
.
2. t is a deterministic function of the information set  t1
In this case t is a deterministic function of previous process values, contained in the
information set  t1.
An
example
is the generalized
autoregressive conditional heteroskeolostic
GARCH(p,q) process which is defined as follows:
Xt ¼  þ tt;
t  NIDð0; 1Þ
or equivalently
Xt ¼  þ t;
t  NIDð0; 2
t Þ
Introduction
295

and
2
t ¼ 0 þ
X
q
j¼1
j2
tj þ
X
p
j¼1
jhtj;
t ¼ 1; . . . ; n;
tj t1  NIDð0; 2
t Þ
ð14:34Þ
It can be seen from Equation 14.34 that 2
t is a weighted sum of the previous values
of t and ht.
More information on GARCH models can be found in Chapter 15 and the
following sections.
14.4.2
Levy processes
In constrast to Brownian motion and stochastic volatility models which describe
continuous process, a Levy process Xt consists of discontinuous jumps.
If the first moment is finite then the Levy process can be represented as:
Xt ¼ Zt þ t þ t;
t  NIDð0; 1Þ
ð14:35Þ
where  is the volatility,  is a continuous drift term and Zt is a discontinuous
Martingale process, see Part II Section 8.2, independent of t.
When the term Zt in Equation 14.35 is set to zero we obtain the equation for
continuous Brownian motion; that is:
Xt ¼ t þ t;
t  NIDð0; 1Þ
ð14:36Þ
We now give a more formal definition of a Levy process. The process X is a Levy
process if:
1. X has increments that are independent of the past:
This means that Xt  Xs is independent of F s, 0  s < t < 1, where F s denotes
the history up to time t ¼ s.
2. X has stationary increments:
That is Xt  Xs has the same distribution as Xts, 0  s < t < 1.
3. X is continuous in probability:
So Xt ! Xs as t ! s:
In Section 14.6 we consider the use of generalized hyperbolic Levy motion to
model asset returns.
14.5
STOCHASTIC AUTOREGRESSIVE VOLATILITY, ARV
A popular form of ARV(1) model, see Taylor (1994), is:
logðPtÞ ¼ logðPt1Þ þ  þ t1t
ð14:37Þ
296
Financial Econometrics

and
logðtÞ ¼  þ  logðt1Þ  
f
g þ t
ð14:38Þ
where , , , and  are constants. The pairs (t, t) are IID bivariate normal and the
standard normal variates t and t have correlation coefficient 
. The logarithm of
the volatility follows a stationary AR(1) process when 1 <  < 1.
Since the volatility appears as t1 in Equation 14.37 the process is termed a lagged
ARV(1) model. Another specification, see Taylor (1986), is:
logðPtÞ ¼ logðPt1Þ þ  þ t
X
t
ð14:39Þ
in which case Equations 14.38 and 14.39 define a contemporaneous ARV(1) model.
The stationary ARV(1) has five parameters that need to be estimated: , , , ,
and 
. Estimation of the parameter  is of particular interest because it provides
information concerning the persistence of the volatility shocks. Various techniques
have been used to estimate this parameter, including:
. Moment-matching methods, Taylor (1986).
. The generalized method of moments, Duffie and Singleton (1989) and Melino and
Turnbill (1990).
. ARMA techniques, Chesney and Scott (1989) and Scott (1991).
. Maximum-likelihood techniques, Harvey et al. (1994).
These studies have shown that the value of  is greater than 0.95; which means
that volatility shocks have a high level of persistence.
14.6
GENERALIZED HYPERBOLIC LEVY MOTION
Barndorff-Nielsen (1977) introduced the generalized hyperbolic (GH) distribution
and used it to model the grain size distributions of wind blown sand. It can be shown,
see Barndorff-Nielsen and Halgreen (1977), that the generalized hyperbolic distribu-
tion generates a (discontinuous) Levy process with increments of length 1.
The generalized hyperbolic distribution
The one dimensional density function of the generalized hyperbolic (GH) distribution is:
GHðxÞ ¼ A  ð2 þ ðx  Þ2Þð	1=2Þ=2
 K	1=2 
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
2 þ ðx  Þ2
q


exp

ðx  Þ

ð14:40Þ
where  > 0, 0 
 jj < ,  > 0 and
A ¼
ð2  2Þ	=2
ffiffiffiffiffi
2
p
	1=2	K	 
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
2  2
p


Introduction
297

and K	 is a modified Bessel function of the third kind with index . The integral
representation of K is:
KðxÞ ¼ 1
2
Z 1
0
y1 exp  1
2 xðy þ y1Þ


dy
For 	 ¼ n þ 1=2, n ¼ 0, 2, . . . , the Bessel function K	 is:
Knþ1ðxÞ ¼ 
2 x1=2 expðxÞ 1 þ
X
n
i¼1
ðn þ iÞ!
ðn  iÞ!i! ð2xÞi
 
!
Since K	(x) ¼ K	(x), and K1=2(x) ¼ K1=2(x) ¼
ffiffiffiffiffiffiffiffi
=2
p
x1=2 exp (x); which is
used below to simplify the expressions for the cases 	 ¼ 1, and 	 ¼ 1=2.
From Equation 14.40 it can easily be shown that the generalized hyperbolic log-
likelihood, for n independent observations, Xi, i ¼ 1, . . . , n is:
L ¼ logðAÞ þ
	
2  1
4

 X
n
i¼1
log 2 þ ðXi  Þ2


þ
X
n
i¼1
log K	1=2 
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
2 þ ðXi  Þ2
q


þ ðXi  Þ




ð14:41Þ
The five parameters in the GH density , , , , and 	 allow much more flexibility
in modelling financial data than the Gaussian distribution which only has two
parameters  and . Estimates for the parameter values can be obtained by using
numerical optimization software to maximize the log-likehood function for a par-
ticular set of data values.
The parameter  controls the shape,  the skewness,  the scaling (similar to  in
the normal distribution),  the location and 	 the heaviness of the tails. The normal
distribution is obtained as a limiting case of the generalized hyperbolic distribution
for  ! 1 and = ! 2.
The mean of GH is:
E½X ¼  þ

ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
2  2
p
K	þ1ðÞ
K	ðÞ
ð14:42Þ
the variance of GH is:
Var½X ¼ 2
K	þ1ðÞ
 K	ðÞ þ
2
2  2
K	þ2ðÞ
K	ðÞ 
K	þ1ðÞ
K	ðÞ

2
(
)
 
!
ð14:43Þ
where  ¼ 
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
2  2
p
. The variance term (in large brackets) multiplied by 2 is
independent of  and .
When the GH distribution is centred ( ¼ 0) and symmetric ( ¼ 0) then  ¼ ,
and the mean and variance are simply:
E½X ¼ 0 and Var½X ¼ 

ð14:44Þ
We will now consider two cases of special interest, namely when 	 ¼ 1 and when
	 ¼ 1=2.
298
Financial Econometrics

The hyperbolic distribution
This is the special case when 	 ¼ 1. In these circumstances the generalized hyper-
bolic distribution (GH ) simplifies to the hyperbolic distribution (H ) which has
density:
HðxÞ ¼
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
2  2
p
2K1 
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
2  2
p

 exp 
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
2 þ ðx  Þ2
q
þ ðx  Þ


ð14:45Þ
where 0 
 , and jj < .
The normal inverse Gaussian
This is the special case when 	 ¼ 1=2.
In these circumstances the generalized hyperbolic distribution (GH ) simplifies to
the normal inverse Gaussian distribution (NIG), see Barndorff-Nielsen (1998), which
has the density:
NIGðxÞ ¼ 
 exp 
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
2  2
p
þ ðx  Þ

 K1 
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
2 þ ðx  Þ2
q


ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
2 þ ðx  Þ2
q
ð14:46Þ
where 0 
 , and 0 
 jj 
 .
When the skewness parameter  is zero and also the mean value  is zero, we have
the symmetric centred NIG distribution, NIGsc, which has the density:
NIGscðxÞ ¼ 
 expðÞ K1 
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
2 þ x2
p


ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
2 þ x2
p
ð14:47Þ
An alternative parameterization of Equation 14.47, see Forsberg and Bollerslev
(2002), is:
NIGscðxÞ ¼ 1=2
 expðÞq
x
1=2

1
K1 q
x
1=2




ð14:48Þ
where q(x) ¼ 1=(1 þ x2),  ¼ , and  ¼ 1=2=1=2.
We can show this as follows. Substituting for  and  into Equation 14.48 we
obtain:
NIGscðxÞ ¼ 1=21=21=2
1=2
expðÞq x

 1
K1 q x

 


where we have made use of the fact that 1=2 ¼ . Simplifying further we have:
NIGscðxÞ ¼ 
 expðÞ
1
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
1 þ x2=2
p
K1 
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
1 þ x2=2
q


Introduction
299

and finally:
NIGscðxÞ ¼ y
 expðÞ K1 
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
2 þ x2
p


ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
2 þ x2
p
QED
14.6.1
Modelling asset returns
The empirical distributions of financial returns data show that, compared to the
normal distribution, there is: more mass near the origin, less in the flanks and
considerably more in the tails. This means that tiny price movements occur with
higher frequency, small- and medium-sized movements with lower frequency and big
price changes are much more frequent than that predicted by a Gaussian distribu-
tion. The generalized hyperbolic distribution allows for an almost perfect statistical
match to these empirical distributions, see Prause (1999), Raible (2000), and Eberlein
(2001).
If there are n stock prices and they are modelled as:
Pi ¼ Pi1 expðXiÞ;
i ¼ 1; . . . ; n
where Xi
0 is generalized hyperbolic Levy motion, then
logðPiÞ  logðPi1Þ ¼ Xi;
i ¼ 1; . . . ; n
and the five parameters defining the generalized hyperbolic distribution can be
estimated by maximizing Equation 14.41; the log-likelihood function.
GARCH–NIG model
Although the generalized hyperbolic distribution can adequately capture the fat
tailed unconditional distribution of the returns, it does not take into account vola-
tility clustering. In order to take these effects into account, Forsberg and Bollerslev
(2002) proposed the following GARCH–NIG model.
tj t1  NIGscð2
t ; Þ
ð14:49Þ
2
t ¼ o þ 12
t1 þ 1
2
t1
ð14:50Þ
where we have written the distribution corresponding to the probability density
function NIGsc(x) as NIGsc(2
t , ) to show the dependence on the parameters 2
t
and . Equations 14.49 and 14.50 describe a GARCH(1,1) model, see Section 15.2,
and the parameters 0, 1, 1, and  can be estimated using maximum likelihood
techniques, see Chapter 18.
300
Financial Econometrics

Chapter 15
GARCH models
In this chapter we discuss the properties of linear GARCH models, in terms of the
more fundamental AR and ARMA processes; further details can be found in the Box
and Jenkins (1976), Hamilton (1994), and Engle (1995).
15.1
BOX JENKINS MODELS
This approach concerns the modelling of n observations yi, i ¼ 1, . . . , n in the pre-
sence of white noise i, i ¼ 1, . . . , n. The aim is to explain any observation yi in terms
of the current noise i and also a weighted linear sum of previous (lagged) observa-
tions and noise.
An autoregressive time series model of order p obeys the following equation:
yi ¼ c þ
X
p
j¼1
jyij þ i;
for i ¼ 1; . . . ; n
ð15:1Þ
where the j, j ¼ 1, . . . , p are termed the autoregressive coefficients and i is white
noise satisfying:
E½i ¼ 0;
E½ij ¼ 0;
i 6¼ j;
E½2
i  ¼ 2
0
ð15:2Þ
Such a process is also denoted as AR(p) and it can be shown that yi is covariance
stationary provided the roots, zj, of the polynomial,
PðzÞ ¼ 1  1z  2z2  	 	 	  pzp ¼ 0
ð15:3Þ
all have modulus greater than 1, that is jzjj > 1, for j ¼ 1, . . . , p
If the AR(p) process is covariance stationary then E[ yi] ¼ , for all i, where  is the
unconditional mean of the sequence. Taking expectations of Equation 15.1 and using our
previous results concerning E[ yi] and E[i], we have:
E½yi ¼ c þ
X
p
j¼1
jE½yij þ E½i
ð15:4Þ
 ¼ c þ 
X
p
j¼1
j
ð15:5Þ

We thus have:
The unconditional mean of an AR(p) process is:
 ¼ c
1 
X
p
j¼1
j
(
)1
ð15:6Þ
An autoregressive process can be generalized into a autoregressive moving average
process by the inclusion of extra lagged terms as follows:
yi ¼ c þ
X
p
j¼1
jyij þ
X
q
j¼1
jij þ i;
for i ¼ 1; . . . ; n
ð15:7Þ
where all terms have the same meaning as before and j, j ¼ 1, q are called the
moving average coefficients.
Such a process is also denoted as ARMA(p,q) and it can be shown that the
conditions for yi to be covariance stationary are the same as those for an AR(p)
process. That is the extra q moving average coefficients do not affect the conditions
for the process to be covariance stationary. Taking expectations of Equation 15.7,
and using our previous results concerning E[ yi] and E[i], we have:
E½yi ¼ c þ
X
p
j¼1
jE½yij þ
X
q
j¼1
jE½ij þ E½i
 ¼ c þ 
X
p
j¼1
j
ð15:8Þ
So
The unconditional mean of an ARMA(p,q) process is:
 ¼ c
1 
X
p
j¼1
j
(
)1
ð15:9Þ
which is the same as for an AR(p) process.
E[ yi] denotes the unconditional expectation of yi and E[ yij i1], denotes the
expectation of yi conditional on all relevant information up to instant i  1. Since
neither of these expectations is time-dependent the above process is said to be both
unconditionally and conditionally homoskedastic.
302
Financial Econometrics

15.2
GAUSSIAN LINEAR GARCH
GARCH relaxes this constraint and allows the conditional variance of yi to vary with
time. For example when p ¼ 0 and c ¼ 0 in Equation 15.1 we now have:
yi ¼ 
i;
i ¼ 1; . . . ; n
where E(
2
i ) ¼ hi and hi is the time-dependent conditional variance. However the
unconditional variance of 
i is still constant,
E½
2
i  ¼ E½Eð
2
i j i1Þ ¼ E½hi ¼ 2
0
In a similar manner to the Box Jenkins approach described above in Section 15.1,
we can define an autoregressive conditional heteroskedastic process of order q,
ARCH(q), process, with Gaussian residuals as follows:
hi ¼ 0 þ
X
q
j¼1
j
2
ij;
i ¼ 1; . . . ; n

ij i1  NIDð0; hiÞ
ð15:10Þ
This can then be generalized to a GARCH(p,q) process in the same way that an
ARMA(p,q) is a generalization of an AR(q) process.
In the same way that an ARMA(p,q) is a generalization of an AR(q) process, we
can define a generalized autoregressive conditional heteroskedastic of order (p, q),
GARCH(p,q) as follows:
Linear GARCH(p,q)
hi ¼ 0 þ
X
q
j¼1
j
2
ij þ
X
p
j¼1
jhij;
i ¼ 1; . . . ; n

ij i1  NIDð0; hiÞ
ð15:11Þ
The relationship between GARCH and ARMA processes can be illustrated as
follows:
hi ¼ 0 þ
X
q
j¼1
j
2
ij þ
X
p
j¼1
jhij;
i ¼ 1; . . . ; n
ð15:12Þ
If 
2
i is added to both sides, and the zero term
Xp
j¼1 j
2
ij 
Xp
j¼1 j
2
ij is added
to the right hand side we have:
hi þ 
2
i ¼ 0 þ
X
q
j¼1
j
2
ij þ
X
p
j¼1
j
2
ij þ 
2
i 
X
p
j¼1
jð
2
ij  hijÞ
So

2
i ¼ 0 þ
X

j¼1
ðj þ jÞ
2
ij þ 
2
i  hi 
X
p
j¼1
jð
2
ij  hijÞ
ð15:13Þ
where  ¼ max ( p, q) and we have i ¼ 0, for i > q, and i ¼ 0, for i > p.
GARCH models
303

We notice that hi is the forecast for 
2
i based on its own lagged values. The term
i ¼ 
2
i  hi is the forecast error associated with this forecast, and is therefore a white
noise process. Substituting for i in Equation 15.13 we then have:

2
i ¼ 0 þ
X

j¼1
ðj þ jÞ
2
ij 
X
p
j¼1
jij þ i
ð15:14Þ
Comparing this with the above equation for an ARMA(p,q) process we see that
the sequence 
2
i
is an ARMA(,p) process with  autoregressive coefficients
(j þ j), j ¼ 1, . . . , , and p moving average coefficients j, j ¼ 1, . . . , p. So if the
residuals 
i are described by a GARCH(p,q) process then 
2
i are described by an
ARMA(,p) process, where  ¼ max (p,q).
From standard results for ARMA processes, 
2
i is covariance stationary provided
i has finite variance and the roots, zj, of the polynomial
PðzÞ ¼ 1  ð1 þ 1Þz  ð2 þ 2Þz2  	 	 	  ð þ Þz ¼ 0
ð15:15Þ
all have modulus greater than 1, that is jzjj > 1, for j ¼ 1, . . . , , Box and Jenkins
(1976), and Levi (1942).
If we impose the nonnegativity requirement 0 > 0 and j  0, j  0, for
j ¼ 1, . . . ,  then we will now show that the condition for 
2
i to be covariance
stationary is:
Condition for GARCH to be covariance stationary:
ð1 þ 1Þ þ ð2 þ 2Þ þ 	 	 	 þ ð þ Þ < 1
ð15:16Þ
or more concisely
X

j¼1
ðj þ jÞ < 1
which means that jzjj > 1, for j ¼ 1, . . . , .
The proof is as follows:
1. Show that if
X
j¼1(j þ j)  1 then 
2
i can’t be stationary
If
X
j¼1(j þ j)  1 then because j  0, j  0, P(1) ¼ 1
X
j¼1(j þ j) < 0,
and P(0) ¼ 1 > 0. Since the polynomial has changed sign between 0 and 1 this
means that there is a root in this interval. So under these circumstances we must
have at least one root zj with jzjj < 0, which means that the process is not
covariance stationary.
304
Financial Econometrics

2. Show that if
X
j¼1(j þ j) < 1 then 
2
i must be stationary
If
X
j¼1(j þ j) < 0 and there is a root of P(z), zi, with jzij < 1, then we have
P(zi) ¼ 1 
X
j¼1(j þ j)zj ¼ 0 that is: 1 ¼ j
X
j¼1(j þ j)zjj
But since j  0, j  0 and zj  jzjj we have:
1 ¼ j
X
j¼1(j þ j)zjj 
X
j¼1ðj þ jÞjzjj 
X
j¼1(j þ j) < 1 which is inconsistent:
So if
X
j¼1(j þ j) < 1 then we must have jzjj > 1, for j ¼ 1, . . . ,
QED
We will now assume that 
2
i is covariance stationary and calculate its unconditional
variance by taking expectations in Equation 15.14 as follows:
E½
2
i  ¼ 0 þ
X
j¼1ðj þ jÞE½
2
ij 
Xp
j¼1 jE½ij þ E½i
ð15:17Þ
But since 
2
i is covariance stationary and i is white noise we have:
E½
2
i  ¼ E½
2
ij
and
E½i ¼ E½ij ¼ 0
Therefore:
E½
2
i  ¼ 0 þ
X
j¼1ðj þ jÞE½
2
i 
ð15:18Þ
and
GARCH unconditional variance:
2
0 ¼ E½
2
i  ¼ 0
1 
X

j¼1
ðj þ jÞ
(
)1
ð15:19Þ
15.2.1
The unconditional kurtosis of the residuals
In Equation 15.11 the conditional distribution of the residuals, 
i, was:

ij i1  NIDð0; hiÞ
For convenience we will now rewrite this as:

i ¼
ffiffiffiffi
hi
p
Zi;
where
Zi  NIDð0; 1Þ
Therefore 
4
i ¼ h2
i Z4
i . Using the fact that hi and Zi are independent of each other
we have E[
4
i ] ¼ E[h2
i Z4
i ] ¼ E[h2
i ]E[Z4
i ].
Jensen’s inequality (see Goldberger (1997) and Appendix F.6), states that for a
random variate X, E[X2]  E[X]2, since the function X2 is convex.
GARCH models
305

Using this result we have:
E½h2
i   E½hi2, which gives E½h2
i E½Z4
i   E½hi2E½Z4
i 
Using E[hi] ¼ E[
2
i ] results in E½
4
i  ¼ E½h2
i E½Z4
i   E½
2
i 2E½Z4
i .
Therefore the unconditional kurtosis is:
@ ¼ E½
4
i 
E½
2
i 2  E½Z4
i 
But since Zi comes from a standardized Gaussian distribution it has variance
E[Z2
i ] ¼ 1, and a kurtosis of 3, see Chapter 17. This means that:
E½Z4
i 
E½Z2
i 2 ¼ E½Z4
i  ¼ 3,
so
@ ¼ E½
4
i 
E½
2
i 2  3
This shows that although the residuals have a Gaussian conditional distribution
their unconditional distribution is leptokurtic and therefore non-Gaussian.
In fact we can use Jensen’s inequality in a similar manner to show that for any
arbitrary conditional distribution R(0, hi) the unconditional kurtosis of 
i will be
higher than the kurtosis of R(0, hi).
We will now derive the value of the unconditional kurtosis of an ARCH(1)
process.
Kurtosis for an ARCH(1) process
For an ARCH(1) process we have:

i ¼
0 þ 1
2
i1

1=2Zi;
Zi  NIDð0; 1Þ
Therefore
E½
4
i  ¼ E½ð0 þ 1
2
i1Þ2Z4
i  ¼ E½ð0 þ 1
2
i1Þ2E½Z4
i 
But
E½ð0 þ 1
2
i1Þ2 ¼ E½2
0 þ 2
1
4
i1 þ 201
2
i1
¼ 2
0 þ 2
1E½
4
i1 þ 201E½
2
i1
But since E[
4
i1] ¼ E[
4
i ] and E[
2
i1] ¼ E[
2
i ] we have:
E½
4
i  ¼ 3 2
0 þ 2
1E½
4
i  þ 201E½
2
i 

	
¼ 32
0 þ 32
1E½
4
i  þ 601E½
2
i 
using E[
2
i ] ¼ (0)=(1  1) we have:
E½
4
i ð1  32
1Þ ¼ 3 2
0 þ 22
01
1  1


¼
32
0
ð1  32
1Þ
1 þ 1
1  1


306
Financial Econometrics

which gives:
@ ¼ E½
4
i 
E½
2
i 2 ¼
32
0
ð1  32
1Þ
1 þ 1
1  1

 ð1  2
1Þ2
2
0
So the kurtosis is:
@ ¼ 3 ð1 þ 1Þð1  1Þ
1  32
1
¼ 3 ð1  2
1Þ
1  32
1
For finite values of E[
2
i ] and E[
4
i ], we require 1 < 1 and 31 < 1 respectively.
Since 1  2
1 > 1  32
1 we have @ > 3, which means that the ARCH model has
heavier tails than a Gaussian distribution.
Kurtosis for a GARCH(1,1) process
To derive the unconditional kurtosis of a GARCH(1,1) is quite complicated, so we
simply present the following results, see Bollerslev (1986):
For GARCH(1,1) we have:
Eð
4
i Þ ¼
32
0ð1 þ ð1 þ 1ÞÞ
ð1  ð1  1ÞÞð1  2
1  211  32
1Þ


and from Equation 15.19 the conditional variance is:
E½
2
i  ¼
0
1  ð1 þ 1Þ
Therefore the unconditional kurtosis of a GARCH(1,1) process is:
@ ¼
32
0ð1 þ ð1 þ 1ÞÞ
ð1  ð1  1ÞÞð1  2
1  211  32
1Þ

 ð1  ð1 þ 1ÞÞ2
2
0


¼ 3 þ
62
1
ð1  2
1  211  32
1Þ
For a finite value of E½
4
i , we require 32
1 þ 211 þ 2
1 < 1. When this constraint
is satisfied @ > 3.
15.2.2
Forecasting and mean-reversion in a GARCH(1,1) process
Here we derive an expression for the T step ahead volatility forecast of a
GARCH(1,1) process. Given the information set  i1 the expected volatility
E[hij i1], at instant i as:
E½hij i1 ¼ 0 þ 1
2
i1 þ 1hi1
and at instant i þ 1, E[hiþ1j i1] is thus:
E½hiþ1j i1 ¼ 0 þ 1E½
2
i  þ 1E½hij i1
GARCH models
307

Now since E[
2
i j i1] ¼ E[hij i1] we have:
E½hiþ1j i1 ¼ 0 þ ð1 þ 1ÞE½hij i1
ð15:20Þ
Proceeding in a simliar manner we have:
E½hiþ2j i1 ¼ 0 þ 1E½
2
iþ1j i1 þ 1E½hiþ1j i1
E½hiþ2j i1 ¼ 0 þ ð1 þ 1ÞE½hiþ1j i1
E½hiþ2j ii ¼ 0 þ ð1 þ 1Þ 0 þ ð1 þ 1ÞE½hij i1
f
g
E½hiþ2j i1 ¼ 0 þ 0ð1 þ 1Þ þ ð1 þ 1Þ2E½hij i1
ð15:21Þ
E½hiþ3j i1 ¼ 0 þ 1E½
2
iþ2j i1 þ 1E½hiþ2j i1
E½hiþ3j i1 ¼ 0 þ ð1 þ 1ÞE½hiþ2j i1
E½hiþ3j i1¼ 0 þ ð1 þ 1Þ 0 þ 0ð1 þ 1Þ þ ð1 þ 1Þ2E½hij i1
n
o
E½hiþ3j i1¼ 0 þ 0ð1 þ 1Þ þ 0ð1 þ 1Þ2 þ ð1 þ 1Þ3E½hij i1
ð15:22Þ
So we have:
E½hiþTj i1 ¼ 0 þ 0ð1 þ 1Þ þ 0ð1 þ 1Þ2 þ 	 	 	 þ ð1 þ 1ÞT1
þ ð1 þ 1ÞTE½hij i1
ð15:23Þ
Equation 15.23 is the sum of T terms of a Geometric Progression with first
term 0 and common factor (1 þ 1), and there is also an additional term
(1 þ 1)TE[hij i1]. So
GARCH(1,1) forecast:
E½hiþTj i1 ¼ 0
1  ð1 þ 1ÞT
n
o
1  ð1 þ 1Þ
þ ð1 þ 1ÞTE½hij i1
ð15:24Þ
Since 1 þ 1 < 1 for a stationary sequence, as T ! 1 we have
E½hiþTj i1 ¼
0
1  ð1 þ 1Þ
ð15:25Þ
This is just the unconditional variance of the GARCH sequence. It can thus be
seen from Equations 15.24 and 15.25 that the GARCH volatility forecast is mean
reverting, and that the smaller the value of 1 þ 1 the faster is the reversion
speed.
308
Financial Econometrics

15.3
THE IGARCH MODEL
It has been found that the use of a GARCH(1,1) model on financial data often results
in 1 > 0:7 and 1  1  1. This has motivated the integrated GARCH(p,q), also
termed IGARCH(p,q), in which 1 þ 1 ¼ 1, see Engle and Bollerslev (1986).
From Equation 15.19 it can be seen that the unconditional variance of the
sequence, E(
2
i ), is infinite, and from Equation 15.26 that the sequence is not covar-
iance-stationary. However, Nelson (1990) shows that:
hi ¼ 0
X
i1
j¼1
Y
j
k¼1
ð1ik þ 1Þ
 
!
þ
Y
i
j¼1
ð1ij þ 1Þh0
where
k ¼ 
2
k=hk,
and
that
the
sequence
is
strictly
stationary
if
E[ log (1ij þ 1)] < 0. When this condition is satisfied the effect of the initial value
h0 disappears asymptotically.
15.3.1
Exponentially weighted moving average: EWMA
The exponentially weighted moving average (EWMA) method is a special case of the
IGARCH(1,1) model:
hi ¼ 0 þ 1
2
i1 þ ð1  1Þhi1;
i ¼ 1; . . . ; n
In the case of EWMA we take 0 ¼ 0 and obtain the scheme:
hi ¼ 
2
i1 þ ð1  Þhi1;
i ¼ 1; . . . ; n
ð15:26Þ
where the parameter  is known as the weight, or decay factor. It can be seen that the
value of hi is the weighted average of 
2
i1 and hi1.
Risk metrics, J. P. Morgan (1996) advocate this method of modelling volatility,
and selected  ¼ 0:97 as the optimal value to use.
15.4
THE GARCH-M MODEL
Finance theory suggests that, on average, an asset with a higher risk should have a
higher return.
Engle et al. (1987) proposed the ARCH-M model to capture this effect. A simple
GARCH-M model is:
yi ¼ hi þ 
i
ð15:27Þ

ij i1 ¼ Nð0; hiÞ
ð15:28Þ
hi ¼ 0 þ
X
q
j¼1
j
2
ij þ
X
p
j¼1
jhij;
i ¼ 1; . . . ; n
ð15:29Þ
Here yi is the mean asset return at time i, and hi the variance of 
i, is a measure of
the associated risk. It can be seen that the extra term hi leads to increased returns for
higher values of hi.
GARCH models
309

15.5
REGRESSION-GARCH AND AR-GARCH
Up to now we have used GARCH models with variables defined as yi ¼ 
i.
We will now include linear regression into the GARCH model.
A regression-GARCH(p,q) sequence containing n terms with Gaussian shocks, 
i,
takes the following form:
yi ¼ b0 þ XT
i b þ 
i;

ij i1  NIDð0; hiÞ
ð15:30Þ
hi ¼ 0 þ
X
q
j¼1
j
2
ij þ
X
p
j¼1
jhij;
i ¼ 1; . . . ; n
ð15:31Þ
This process is described by q þ 1 coefficients j, j ¼ 0, . . . , q, p coefficients
j, j ¼ 1, . . . , p, mean b0, k linear regression coefficients bj, j ¼ 1, . . . , k, endogen-
ous/exogenous variables yi and Xi respectively, shocks 
i, hi the conditional variance,
and the set of all information up to time i,  i. The conditional probability distribu-
tion of 
i is denoted by P(0, hi), a distribution with zero mean and time-varying
variance hi.
Here Xi denotes the k element row vector of exogenous variables at time i, and b
refers to the k element column vector or regression coefficients. We also use XT
i
to
indicate the column vector formed by the transpose of Xi, and the k individual
elements of Xi are denoted by Xj
i , j ¼ 1, . . . , k.
It should be noted that the n term regression-GARCH(p,q) model above can easily
be used to model an n–m term AR(m)–GARCH(p,q) sequence defined as follows:
yi ¼ c þ
X
p
j¼1
jyij þ 
i;
i ¼ m þ 1; . . . ; n
ð15:32Þ
hi ¼ 0 þ
X
q
j¼1
j
2
ij þ
X
p
j¼1
jhij;
i ¼ m þ 1; . . . ; n
ð15:33Þ
where the terms yi, i ¼ 1, . . . , m are used as the pre-observed values for the
AR(m)–GARCH(p,q) sequence.
If we let k ¼ m then the mean term b0 is identified as c and the k time-dependent
exogenous variables are replaced by the lagged values of yi. That is the row vector
Xi ¼ ( yi1, yi2, . . . , yim).
310
Financial Econometrics

Chapter 16
Nonlinear GARCH
The standard GARCH model assumes that both positive and negative shocks of equal
magnitude have an identical effect on future volatility. However, empirical studies on
stock returns have shown that they are characterized by increased volatility following
negative shocks (bad news). This leverage effect was first recognized by Black (1976), who
reasoned that it is connected with the way in which firms are financed. When the value of
a firm’s stock decreases the debt-to-equity ratio increases, which leads to an increase in
the volatility of the returns on equity. The leverage effect suggests that positive and
negative shocks have an asymmetric impact on the conditional volatility of subsequent
observations. It has been found that the returns for different asset classes display different
leverage characteristics. The returns for equities and equity indices have negative leverage
(negative shocks increase subsequent volatility). By contrast the returns for commodities
and commodity futures exhibit both positive and negative leverage effects, McKenzie
etal. (2001). Finally exchange rate returns, where the concept of good/bad news is less
well defined, have no leverage effects at all. This is because a return series of currency X in
terms of currency Y can be inverted (negative shocks now transformed into positive
shocks) to yield a return series of currency Y in terms of currency X.
Since linear GARCH models cannot capture these effects various nonlinear
GARCH extensions have been proposed. These models include: Exponential
GARCH (EGARCH) (Nelson, 1991), Asymmetric GARCH (AGARCH) (Engle
and Ng, 1993), GJR–GARCH (Glosten et al., 1993), Markov-Switching GARCH
(MSW-GARCH) (Dueker, 1997), and Asymmetric Nonlinear Smooth Transition
GARCH (ANST-GARCH) (Anderson et al., 1999). Hentschel (1995) provides a
more comprehensive overview of nonlinear GARCH models.
Empirical studies have also found that both the conditional and unconditional
distributions of financial returns exhibit leptokurtosis (have fatter tails than a normal
distribution). A popular choice, Bollerslev (1987), Engle and Gonzalez-Rivera
(1991), is to assume that, instead of a Gaussian distribution, the errors i have a
Student’s t distribution with  degrees of freedom.
Here we consider asymmetric effects in AGARCH-I, AGARCH-II, and GJR–
GARCH sequences, which can be modelled by the inclusion of an extra asymmetry
parameter, . The mathematical definition of these processes is as follows:

AGARCH-I
hi ¼ 0 þ
X
q
j¼1
jðij þ Þ2 þ
X
p
j¼1
jhij;
i ¼ 1; . . . ; n
ð16:1Þ
AGARCH-II
hi ¼ 0 þ
X
q
j¼1
jðjijj þ ijÞ2 þ
X
p
j¼1
jhij;
i ¼ 1; . . . ; n
ð16:2Þ
GJR–GARCH
hi ¼ 0 þ
X
q
j¼1
ðj þ SijÞ2
ij þ
X
p
j¼1
jhij;
i ¼ 1; . . . ; n
ð16:3Þ
where Si ¼ 1, if i < 0 and Si ¼ 0, if i  0:
EGARCH
logðhiÞ ¼ 0 þ
X
q
j¼1
jZij þ
X
q
j¼1
	iðjZijj  E½jZijj
Þ
þ
X
p
j¼1
j logðhijÞ;
i ¼ 1; . . . ; n
ð16:4Þ
where Zi ¼ i=
ffiffiffiffihi
p
and E[jZijj] denotes the expected value of jZijj.
In AGARCH-I the asymmetric effects are modelled via the extra parameter. For
example, in the standard GARCH(1,1) model when hi1 is fixed hi ¼ h(i1) is a
parabola with a minimum at i1 ¼ 0. The introduction of the additional parameter 
shifts the parabola horizontally so that the minimum occurs at i1 ¼ . The
conditional variance following negative shocks can therefore be enhanced by choos-
ing  < 0, so that h(i1) > h(i1) for i1 > 0.
In an AGARCH-II model the inclusion of  can also result in an enhancement of
hi following a negative shock i1. For a GARCH(1,1) model h(i1) > h(i1) for
 > 0 and  < 0.
Similarly in the GJR–GARCH(1,1) model the value of hi is increased above the
symmetric case when i1 < 0 and  > 0.
312
Financial Econometrics

For EGARCH, asymmetric response arises from the term Pq
j¼1 jZij. In an
EGARCH(1,1), if 1 < 0 then a negative shock i1 increases the value of hi, that
is log {h(Zi1)} > log {h(Zi1)}.
16.1
AGARCH-I
From Equation 16.1 the AGARCH-I process is defined as:
hi ¼ 0 þ
X
q
j¼1
jðij þ Þ2 þ
X
p
j¼1
jhij;
i ¼ 1; . . . ; n
Since (ij þ )2 ¼ 2
ij þ 2ij þ 2 we have
hi ¼ 0 þ
X
q
j¼1
j2
ij þ
X
p
j¼1
jhij þ 2
X
q
j¼1
ij þ
X
q
j¼1
j2
Following the same procedure as in Section 16.2 we have
2
i ¼ 0 þ
X

j¼1
ðj þ jÞ2
ij 
X
p
j¼1
jij þ i þ 2
X
q
j¼1
ij þ
X
q
j¼1
j2
where  ¼ max ( p,q) and we have i ¼ 0, for i > q and i ¼ 0, for i > p.
Taking expectations gives:
E½2
i 
 ¼ 0 þ
X

j¼1
ðj þ jÞE½2
ij
 
X
p
j¼1
jE½ij
 þ E½i
þ 2
X
q
j¼1
E½ij
 þ
X
q
j¼1
j2
ð16:5Þ
Now since E[i] ¼ 0 and E[i] ¼ 0 we have:
E½2
i 
 ¼ 0 þ
X

j¼1
ðj þ jÞE½2
ij
 þ
X
q
j¼1
j2
This is an AR() process and the condition for 2
i to be covariance stationary is:
X

j¼1
ðj þ jÞ < 1
ð16:6Þ
which is the same condition as for the standard linear GARCH(p,q) process.
Assuming that 2
i is covariance stationary we have 2
0 ¼ E[2
i ] ¼ E[2
ij] and so
E½2
i 
 ¼ 0 þ 2 X
q
j¼1
j þ
X

j¼1
ðj þ jÞE½2
i 
which results in
Nonlinear GARCH
313

AGARCH-I unconditional variance
2
0 ¼ E½2
i 
 ¼
ð0 þ 2 Pq
j¼1 jÞ
ð1  P
j¼1ðj þ jÞÞ
ð16:7Þ
16.1.1
Kurtosis
We will now calculate the kurtosis for an AGARCH-I(0,1) process:
i ¼
0 þ 1ði1 þ Þ2
n
o1=2
Zi;
Zi  NIDð0; 1Þ
Therefore
E½4
i 
 ¼ E½ð0 þ 1ði1 þ Þ2Þ2Z4
i 
 ¼ E½ð0 þ 1ði1 þ Þ2Þ2
E½Z4
i 
We will assume that process is covariance stationary and use the fact that the
expectation of odd powers of i is zero and that E[Z4
i ] ¼ 3:
E½4
i 
 ¼ 3 2
0 þ 2012 þ 2
14 þ 210E½2
i 
 þ 62
i 2E½2
i 
 þ 2
1E½4
i 


which gives
E½4
i 
ð1  32
1Þ ¼ 3 ð0 þ 12Þ2 þ E½2
i 
ð62
12 þ 210Þ
n
o
substituting for E[2
i ] we have:
E½4
i 
ð1  32
1Þ ¼ 3ð0 þ 12Þ ð0 þ 12Þ þ ð62
12 þ 210Þ
ð1  1Þ

	
¼ 3ð0 þ 12Þ
ð1  1Þ
ð0 þ 12Þð1  1Þ

þ ð62
12 þ 210Þ

But
ð0 þ 12Þð1  1Þ þ ð62
12 þ 210Þ ¼ ð0 þ 12Þð1 þ 1Þ þ 42
12
Therefore
E½4
i 
 ¼
3ð0 þ 12Þ
ð1  32
1Þð1  1Þ ð0 þ 12Þð1 þ 1Þ þ 42
12


So the kurtosis is:
@ ¼
E½4
i 
ðE½2
i 
Þ2 ¼ 3ð1  2
1 þ FÞ
1  32
1
;
where
F ¼ 42
12ð1  1Þ
0 þ 12
ð16:8Þ
It is therefore evident that when  ¼ 0 we have F ¼ 0, and the kurtosis is the same
as for the linear ARCH(1). However, for any non-zero value of  the kurtosis will be
greater than that for the standard ARCH(1). Furthermore, since F increases mono-
tonically with the absolute value of , the unconditional kurtosis increases with .
314
Financial Econometrics

16.1.2
Skewness
We assume the non-negativity constraints 0 > 0 and 1 > 0.
i ¼
0 þ 1ði1 þ Þ2
n
o1=2
Zi;
Zi  Rð0; 1Þ
where Zi is an arbitrary symmetric distribution.
Therefore:
E½3
i 
 ¼ E
0 þ 1ði1 þ Þ2
n
o3=2
Z3
i


;
Zi  Rð0; 1Þ
By decomposing this expectation into the part with i  0, and the part with i < 0,
we have:
E½3
i 
 ¼ E
0 þ 1ðji1j  Þ2
n
o3=2


E Z3þ
i


þ E
0 þ 1ðji1j þ Þ2
n
o3=2


E Z3
i


where because R(0, 1) is symmetric we have E[Z3
i ] ¼ 0 ¼ E Z3þ
i


þ E Z3
i


.
This means that:
E½3
i 
 ¼
(
E
0 þ 1ðji1j  Þ2
n
o3=2


 E
0 þ 1ðji1j þ Þ2
n
o3=2

)
E Z3þ
i


Since E[2
i ] > 0, the skewness is:
S ¼
E½3
i 
E½2
i 
3=2
ð16:9Þ
It can be seen that the skewness is zero for  ¼ 0, and becomes increasingly
negative as the value of  is raised.
16.1.3
Forecasting and mean-reversion in an AGARCH-I(1,1) process
Here we derive an expression for the T step ahead volatility forecast of an
AGARCH-I(1,1) process. Given the information set  i1 we can forecast the
expected volatility E[hij i1] at time instant i as:
E½hij i1
 ¼ 0 þ 1ði1 þ Þ2 þ 1hi1
and at instant i þ 1, E[hiþ1j i1] is:
E½hiþ1j i1
 ¼ 0 þ 1E½2
i j i1
 þ 1E½hij i1 þ 12 þ 2E½ij i1
Now since E[ij i1] ¼ 0, and E[2
i j i1] ¼ E[hij i1] we have:
E½hiþ1j i1
 ¼ 0 þ 12 þ ð1 þ 1ÞE½hij i1
ð16:10Þ
Nonlinear GARCH
315

Proceeding in a similiar manner we have:
E½hiþ2j i1
¼0 þ 1E½2
iþ1j i1
 þ 1E½hiþ1j i1
 þ 12 þ 2E½iþ1j i1
E½hiþ2j i1
¼0 þ 12 þ ð1 þ 1ÞE½hiþ1j i1
E½hiþ2j i1
¼0 þ 12 þ ð1 þ 1Þ 0 þ 12 þ ð1 þ 1ÞE½hij i1


E½hiþ2j i1
¼ð0 þ 12Þ 1 þ ð1 þ 1Þ
f
g þ ð1 þ 1Þ2E½hij i1
ð16:11Þ
E½hiþ3j i1
 ¼ 0 þ 1E½2
iþ2j i1
 þ 1E½hiþ2j i1
 þ 12 þ 2E½iþ2j i1
E½hiþ3j i1
 ¼ 0 þ 12 þ ð1 þ 1ÞE½hiþ2j i1
E½hiþ3j i1
 ¼ 0 þ 12 þ ð1 þ 1Þ

ð0 þ 12Þð1 þ ð1 þ 1Þ þ ð1 þ 1Þ2E½hij i1
n
o
E½hiþ3j i1
 ¼ ð0 þ 12Þ 1 þ ð1 þ 1Þ þ ð1 þ 1Þ2
n
o
þ ð1 þ 1Þ3E½hij i1
ð16:12Þ
So in general we have:
E½hiþTj i1
 ¼ ð0 þ 12Þ 1 þ ð1 þ 1Þ þ    þ ð1 þ 1ÞT1
n
o
þ ð1 þ 1ÞTE½hij i1
ð16:13Þ
Equation 16.13 is the sum of T terms of a Geometric Progression with first term
0 þ 12 and common factor (1 þ 1), and also additional term (1 þ 1)T
E [hi|i1]. So
AGARCH-I(1,1) forecast:
E½hiþTj i
 ¼
0 þ 12  ð1 þ 1ÞT
n
o
1  ð1 þ 1Þ
þ ð1 þ 1ÞTE½hij i1
ð16:14Þ
Since 1 þ 1 < 1 for a stationary process, as T ! 1 we have
E½hiþTj i1
 ¼
0 þ 12
1  ð1 þ 1Þ
ð16:15Þ
which is just the unconditional variance of the GARCH sequence. It can be seen
from Equations 16.13 and 16.15 that the volatility forecast is mean reverting, and
that the smaller the value of 1 þ 1 the faster is the reversion speed.
16.2
AGARCH-II
The AGARCH-II process is defined by:
hi ¼ 0 þ
X
q
j¼1
jðjijj þ ijÞ2 þ
X
p
j¼1
jhij;
i ¼ 1; . . . ; n
316
Financial Econometrics

Following the same procedure as in Section 15.2 we have
2
i ¼ 0 þ
X

j¼1
ðj þ j þ 2jÞ2
ij 
X
p
j¼1
jij þ i þ 2
X
q
j¼1
jjijjij
where  ¼ max ( p, q) and we have j ¼ j ¼ 0, for j > q, j ¼ 0, for j > p, and
j ¼ 1 for j  q. Taking expectations gives:
E½2
i 
 ¼ 0 þ
X

j¼1
ðj þ j þ 2jÞE½2
ij
since E[i] ¼ 0 and E[jiji] ¼ 0:
This is an AR() process, and the condition for 2
i to be covariance stationary is :
X

j¼1
ðj þ j þ 2jÞ < 1
ð16:16Þ
Assuming that 2
i is covariance stationary we have 2
0 ¼ E[2
i ] ¼ E[2
ij] and so
E½2
i 
 ¼ 0 þ
X

j¼1
ðj þ j þ 2jÞE½2
i 
which results in
AGARCH-II unconditional variance
2
0 ¼ E½2
i 
 ¼
0
ð1  P
j¼1ðj þ j þ 2jÞÞ
ð16:17Þ
16.3
GJR–GARCH
The GJR–GARCH(p,q) process is defined as:
hi ¼ 0 þ
X
q
j¼1
ðj þ SijÞ2
ij þ
X
p
j¼1
jhij;
i ¼ 1; . . . ; n
where Si ¼ 1, if i < 0 and Si ¼ 0, if i  0.
Following the same procedure as in Section 15.2 we have
2
i ¼ 0 þ
X

j¼1
ðj þ j þ SijjÞ2
ij 
X
p
j¼1
jij þ i
where  ¼ max ( p, q) and we have j ¼ j ¼ 0, for j > q, j ¼ 0, for j > p, and
j ¼ 1 for j  q. Taking expectations gives:
E½2
i 
 ¼ 0 þ
X

j¼1
ðj þ j þ E½Sij
jÞE½2
ij
Nonlinear GARCH
317

E½2
i 
 ¼ 0 þ
X

j¼1
ðj þ j þ 
2 jÞE½2
ij
Since the probability distribution for i is symmetric about zero we have the
probability for i < 0 is 1=2 and E[Si] ¼ 1=2.
This is an AR() process, and the condition for 2
i to be covariance stationary is :
X

j¼1
ðj þ j þ 
2 jÞ < 1
ð16:18Þ
Assuming that 2
i is covariance stationary we have 2
0 ¼ E[2
i ] ¼ E[2
ij] and so
E½2
i 
 ¼ 0 þ
X

j¼1
ðj þ j þ 
2 jÞE½2
i 
We therefore have
GJR–GARCH unconditional variance
2
0 ¼ E½2
i 
 ¼ 0
1 
X

j¼1
ðj þ j þ 
2 jÞ
(
)1
ð16:19Þ
318
Financial Econometrics

Chapter 17
GARCH conditional probability distributions
Here we give some useful results concerning various conditional probability distribu-
tions that are commonly used in GARCH models. For each distribution we give the
following information:
. The probability density function, f (i).
. The quantity Li(), which is minus the log likelihood (see Chapter 18). Here  is the
vector of GARCH model parameters, and the subscript i indicates the contribution
from the i term in the sequence. The sample log likelihood for the complete n term
GARCH sequence is L() ¼ n
i¼1Li(). In this section we assume that vector 
contains the model parameters for a non-linear regression-GARCH(p,q) process in
which the residuals, i, are described by a single asymmetry parameter, , and a
given conditional probability density function. Thus the parameter vector  given
here is correct for AGARCH-I, AGARCH-II, and GJR–GARCH processes, but
would require extra elements for an EGARCH process. More information con-
cerning the use of Li() in parameter estimation can be found in Chapter 18.
. The value of E[jij], which is used in the EGARCH model.
. The value of the kurtosis, which indicates how thick the tails of the distribution are.
17.1
GAUSSIAN DISTRIBUTION
17.1.1
The probability density function
The probability density function for Gaussian shocks, i, with zero mean and
variance hi is:
Gaussian probability density function
f ðiÞ ¼
1ffiffiffiffiffiffiffiffiffi
2hi
p
exp  2
i
2hi


ð17:1Þ
17.1.2
The kurtosis
The kurtosis for a Gaussian distribution is 3. This can be proved as follows:
E½2
i 	 ¼
1ffiffiffiffiffiffiffiffiffi
2hi
p
Z 1
1
2
i exp  2
i
2hi


di ¼
2ffiffiffiffiffiffiffiffiffi
2hi
p
Z 1
0
2
i exp  2
i
2hi


di

Using the standard integral results in Appendix K, and the substitution a ¼ 1=2hi
we have:
E½2
i 	 ¼
4hi
4
ffiffiffiffiffiffiffiffiffi
2hi
p
ffiffiffiffiffiffiffiffiffi
2hi
p
¼ hi
Similarly
E½4
i 	 ¼
1ffiffiffiffiffiffiffiffiffi
2hi
p
Z 1
1
4
i exp  2
i
2hi


di ¼
2ffiffiffiffiffiffiffiffiffi
2hi
p
Z 1
0
4
i exp  2
i
2hi


di
E½4
i 	 ¼
2ffiffiffiffiffiffiffiffiffi
2hi
p
12h2
i
8
ffiffiffiffiffiffiffiffiffi
2hi
p
¼ 3h2
i
Therefore
Gaussian kurtosis
@ ¼
E½4
i 	
ðE½2
i 	Þ2 ¼ 3h2
i
h2
i
¼ 3
ð17:2Þ
17.1.3
The log likelihood
If we take the logarithm of the probability density function in Section 17.1.1 we
obtain the following expression for the log likelihood:
LiðÞ ¼ 1
2 logð2Þ þ 1
2 logðhiÞ þ 1
2
2
i
hi
ð17:3Þ
or ignoring the constant term:
Gaussian log likelihood
LiðÞ ¼ 1
2 logðhiÞ þ 1
2
2
i
hi
ð17:4Þ
where  ¼ (!T, b0, bT), !T ¼ (0, 1, . . . , q, 	1, . . . , 	p, ) and bT ¼ (b1, . . . , bk).
17.1.4
Calculation of E [jij]
E½jij	 ¼
1ffiffiffiffiffiffiffiffiffi
2hi
p
Z 1
1
jij exp  2
i
2hi


di
¼
2ffiffiffiffiffiffiffiffiffi
2hi
p
Z 1
0
i exp  2
i
2hi


di
320
Financial Econometrics

Using the standard integral results given in Appendix K, and on the substitution of
y ¼ i=
ffiffiffiffiffiffi
2hi
p
we have:
E½jij	 ¼
2hi
ffiffiffiffiffiffiffiffiffi
2hi
p
1
2 ¼
ffiffiffiffiffiffi
2hi

r
ð17:5Þ
17.2
STUDENT’S t DISTRIBUTION
17.2.1
The probability density function
The probability density function for shocks i following a Student’s t distribution
with 
 degrees of freedom, zero mean, and variance hi is (DeGroot, 1970):
Student’s t distribution probability density function
f ðiÞ ¼ ðð
 þ 1Þ=2Þð
  2Þ1=2h1=2
i
1=2ð
=2Þ
1 þ
2
i
hið
  2Þ

ð
þ1Þ=2
;
where 
 > 2
ð17:6Þ
17.2.2
The kurtosis
The kurtosis is (see Appendix J):
Student’s t distribution kurtosis
@ ¼ 3ð
  2Þ
ð
  4Þ ;
where 
 > 4
ð17:7Þ
For convenience we now tabulate the kurtosis, @, for different values of 
:

@
4.2
33.000
5.0
9.000
10.0
4.000
20.0
3.375
50.0
3.1304
100.0
3.0625
It can be seen that @ is always greater than the kurtosis for a Gaussian distribution.
However, for values of 
 below about 5 the tails are very thick compared to a
Gaussian distribution, while when 
 is above about 20.0 they are almost identical
to a Gaussian distribution.
GARCH conditional probability distributions
321

17.2.3
The log likelihood
The log likelihood is obtained by taking the logarithm of the probability density
function given in Section 17.2.1, and is:
LiðÞ ¼  logððð
 þ 1Þ=2ÞÞ þ logðð
=2ÞÞ þ 1
2 logðÞ þ 1
2 logð
  2ÞÞ
þ 1
2 logðhiÞ þ 
 þ 1
2
log 1 þ
2
i
ð
  2Þhi


ð17:8Þ
or ignoring the constant term:
Student’s t distribution log likelihood
LiðÞ ¼  logððð
 þ 1Þ=2ÞÞ þ logðð
=2ÞÞ þ 1
2 logð
  2ÞÞ
þ 1
2 logðhiÞ þ 
 þ 1
2
log 1 þ
2
i
ð
  2Þhi


ð17:9Þ
where  ¼ (!T, 
, b0, bT), !T ¼ (0, 1, . . . , q, 	1, . . . , 	p, ), and bT ¼ (b1, . . . , bk).
17.2.4
Calculation of E [jij]
As previously stated the Student’s t distribution density function is:
f ðiÞ ¼ K 1 þ
i2
hið
  2Þ

ð
þ1Þ=2
where
K ¼ ðð
 þ 1Þ=2Þð
  2Þ1=2h1=2
i
1=2ð
=2Þ
we have:
E½jij	 ¼ K
Z 1
1
1 þ
2
i
hið
  2Þ

ð
þ1Þ=2
jijdi
¼ 2K
Z 1
0
idi
1 þ 2
i =ðhið
  2ÞÞ
ð
Þð
þ1Þ=2
¼ 2K hið
  2Þ
ð
Þð
þ1Þ=2
Z 1
0
idi
ðhið
  2Þ þ 2
i Þð
þ1Þ=2
322
Financial Econometrics

Using the value of the integral
R 1
0 (a
i di)=((m þ b
i )c) in Appendix K, with
a ¼ 1, b ¼ 2, c ¼ ð
 þ 1Þ=2 and m ¼ (
  2)hi we have:
mðaþ1bcÞ=b
b
¼ hið
  2Þ
ð
Þð1
Þ=2
2
;  a þ 1
b


¼ ð1Þ ¼ 1;  c  a þ 1
b


¼  
  1
2


; ðcÞ ¼  
 þ 1
2


This gives:
E½jij	 ¼ 2K hið
  2Þ
ð
Þð
þ1Þ=2 hið
  2Þ
ð
Þð1
Þ=2
2
ðð
  1Þ=2Þ
ðð
 þ 1Þ=2Þ
Substituting for K and cancelling similar terms we obtain:
E½jij	 ¼ ðð
  2ÞhiÞ1=2ðð
  1Þ=2Þ
1=2ð
=2Þ
Using ((
  1)=2)((
  1)=2) ¼ ((
  1)=2 þ 1) ¼ ((
 þ 1)=2) we obtain
E½jij	 ¼ 2ðð
  2ÞhiÞ1=2ðð
 þ 1Þ=2Þ
1=2ð
=2Þð
  1Þ
ð17:10Þ
Note: This corrects an error in the literature (Taylor, 1994) which, for hi ¼ 1, gives
the expression as:
E½jij	 ¼ 2ðð
  2ÞÞ1=2ðð
=2 þ 1ÞÞ
1=2ð
=2Þð
  1Þ
17.3
GENERAL ERROR DISTRIBUTION
This distribution is also known as: the exponential power distribution, the error
distribution and the generalized error distribution. The distribution is symmetric
about the mean, and the kurtosis can be varied by the altering the value of the
distribution’s shape parameter.
17.3.1
The probability density function
The general error distribution function, see for example Nelson (1991), is:
General error distribution probability density function
f ðiÞ ¼
a
 2ð1þ1=aÞð1=aÞ exp  1
2
i



a


ð17:11Þ
where  is the scale factor, a is the exponent (or shape parameter), and the
distribution has zero mean.
GARCH conditional probability distributions
323

Sometimes this equation is written in the form:
f ðiÞ ¼
1
2ð1þ1=aÞð1 þ 1=aÞ exp  1
2
i



a


ð17:12Þ
where we have used 1=a (1=a) ¼ (1 þ 1=a).
Another form, see for example Good (1979) and Tadikamalla (1980), is:
f ðiÞ ¼
1
2 ð1 þ 1=aÞ exp  i
j ja
ð
Þ
ð17:13Þ
This is just Equation 17.11 with a scale factor  ¼ 1=21=a.
If the variance of the distribution is hi then we have (see Appendix I.1):
 ¼
22=a  ð1=aÞ hi
ð3=aÞ

1=2
ð17:14Þ
17.3.2
The kurtosis
The kurtosis of the distribution (see Appendix I.2) is:
General error distribution kurtosis
@ ¼ ð5=aÞð1=aÞ
ð3=aÞð3=aÞ
ð17:15Þ
We will now illustrate how the kurtosis of the distribution changes with the shape
parameter, a.
When a ¼ 1, then f (i) becomes the Laplace distribution (double-sided exponential
distribution), since:
f ðiÞ ¼ 1
2 exp  i





where  ¼ 2 is the width of the distribution, and  ¼
(1)hi
4(3)

1=2
¼ 1
2
ffiffiffiffi
hi
6
r
.
The kurtosis of a Laplace distribution is 6. This can be verified by using
(n) ¼ (n  1)!, and substituting a ¼ 1 into Equation 17.15:
@ ¼ ð5Þ ð1Þ
ð3Þ ð3Þ ¼ 4  3  2  1
2  2
¼ 6
324
Financial Econometrics

When
a ¼ 2,
then
f (i)
simplifies
to
the
Gaussian
distribution:
 ¼ (21(1=2)hi)=((3=2))

1=2¼
ffiffiffiffihi
p ,
using
(3=2) ¼ (1=2)(1=2)
and
since
(1=2) ¼
ffiffiffi
p
we have:
f ðiÞ ¼
2h1=2
i
23=2ð1=2Þ exp  2
i
2hi


¼
1ffiffiffiffiffiffiffiffiffi
2hi
p
exp  2
i
2hi


The kurtosis of a Gaussian distribution is 3. This can easily be verified by using
(3=2) ¼
ffiffiffi
p =2, (5=2) ¼ 3
ffiffiffi
p =4, and substituting a ¼ 2 into Equation 17.15:
@ ¼ ð5=2Þ ð1=2Þ
ð3=2Þ ð3=2Þ ¼
3=4
ffiffiffi
p
ffiffiffi
p
1=2
ffiffiffi
p
1=2
ffiffiffi
p
¼ 3
When a!1, then we have (Nelson, 1991 and Appendix I.3):
f ðiÞ! Uðð3hiÞ1=2; ð3hiÞ1=2Þ
where U(a, b) is a uniform distribution with lower and upper limits a and b respect-
ively, and a kurtosis of 9/5.
In summary then, when a < 2, the distribution is leptokurtic (has tails that are
thicker than those for a Gaussian), and when a > 2 the distribution is platykurtic (has
tails that are thinner than those for a Gaussian).
17.3.3
The log likelihood
The log likelihood is obtained by taking the logarithm of the probability density
function given in Section 17.3.1, and is:
LiðÞ ¼  logðaÞ þ logðÞ þ ð1 þ 1=aÞ logð2Þ þ logðð1=aÞÞ þ 1
2
i



a
or ignoring the constant term, log(2), we have:
General error distribution log likelihood
LiðÞ ¼  logðaÞ þ logðÞ þ 1
a logð2Þ þ logðð1=aÞÞ þ 1
2
i



a
ð17:16Þ
where  ¼ (!T, a, , b0, bT), !T ¼ (0, 1, . . . , q, 	1, . . . , 	p, ),
and bT ¼ (b1, . . . , bk).
17.3.4
Calculation of E [jij]
E½jij	 ¼ K
Z 1
1
jij exp  1
2
i



a


di ¼ 2K
Z 1
0
i exp  1
2
i

 a


di
Using the standard integral results in Appendix K with n ¼ 1, p ¼ a, and
b ¼ (1=2)(1=)a gives:
E½jij	 ¼ 2K
a  2
a
 
1
2
1

 a

2=a
GARCH conditional probability distributions
325

After some simplification this yields:
E½jij	 ¼ 22K
a
 2
a
 
1
2
 2=a
and substituting for K we then have:
E½jij	 ¼ ð2=aÞ21=a
ð1=aÞ
ð17:17Þ
326
Financial Econometrics

Chapter 18
Maximum likelihood parameter estimation
In this chapter we will discuss how the model parameter vector  for a
GARCH sequence can be estimated. For a standard linear GARCH(p,q) with
regression terms we have  ¼ (!T, bT), where !T ¼ (0, 1, . . . , q, 1, . . . , p) and
bT ¼ (b1, . . . , bk):
18.1
THE CONDITIONAL LOG LIKELIHOOD
Assume we have a standard linear GARCH(p,q) sequence of length n, in which the
observations yi, i ¼ 1, . . . , n are given by:
yi ¼ b0 þ XT
i b þ i;
ij i1  Rð0; hiÞ
ð18:1Þ
hi ¼ 0 þ
X
q
j¼1
j2
ij þ
X
p
j¼1
jhij;
i ¼ 1; . . . ; n
ð18:2Þ
The residuals, i, are independently distributed according to the arbitrary prob-
ability distribution R(0, hi), which has zero mean and time-dependent variance hi.
The notation  i1 has been used to denote information content up to and including
time instant i  1, that will affect the conditional distribution of i. In this case  i1
represents the information that affects the variance hi of R(0, hi). The syntax ij i1 is
used to indicate that the PDF of the residual i is conditional on  i1. For the
GARCH models considered here it is only the variance hi of the PDF for i that is
affected by the information  i1. Also, since i is independently distributed to i1 we
have that E(2
i j i1) ¼ 0 and E(2
i j i12
i1j i2) ¼ E(2
i j i1) E(2
i1j i2).
The joint density distribution for a sample of independently distributed variables
can be obtained by taking the product of the individual probability densities.
This means that the joint probability density distribution of the first two residuals
in a GARCH sequence is:
f ð2; 1; Þ ¼ f ð2j 1; Þ f ð1j 0; Þ
where we have used the notation f (2j 1; ) to indicate that the distribution of 2 is
conditional on  1 and depends on the parameter vector .
Similarly the joint probability density distribution of the first three residuals in a
GARCH sequence is:
f ð3; 2; 1; Þ ¼ f ð3j 2; Þ f ð2j 1; Þ f ð1j 0; Þ

Continuing this process for all the residuals in the sequence yields the sample joint
probability density function, F(), for the residuals of the complete series:
FðÞ ¼ f ðn; . . . ; 1; Þ ¼
Y
n
i¼1
f ðij i1; Þ
Taking natural logarithms we obtain:
logðFðÞÞ ¼
X
n
i¼1
logð f ðij i1; ÞÞ
ð18:3Þ
If Equation 18.2 is conditioned using known pre-observed values i, 2
i , hi, i 	 0,
(see Section 20.1 for more details) then we can use the parameter vector 
to iteratively evaluate the time dependent variance h1, . . . , hn and also determine
the
information
content
 1, . . . ,  n1.
This
means
that
we
can
substitute
i ¼ yi  b0  XT
i b into the PDF for R(0, hi) and thus obtain the probabilities
f (ij i1; ).
We can then evaluate the sample log likelihood, L(), using:
 logðFðÞÞ ¼ LðÞ ¼
X
n
i¼1
LiðÞ
where Li() ¼  log ( f (ij i1; )), see Chapter 17.
The maximum likelihood estimator, ^, for the parameter vector  is that which
minimises L() (see Section 18.2) and is the solution to the likelihood equations:
@LðÞ
@
¼ 0
At the minimum the Hessian @2L()=@T is a positive definite matrix. However,
care needs to be exercised since this does not guarantee that a global minimum rather
than a local minimum has been reached.
18.2
THE COVARIANCE MATRIX OF THE PARAMETER ESTIMATES
In this section we will show how the covariance matrix of the maximum likelihood
parameter estimates are related to the Hessian of the log likelihood function. For
convenience we have adopted the D operator convention:
DLðÞ ¼ @LðÞ
@
and
D2LðÞ ¼ @2LðÞ
@2
We will assume that the log likelihood is locally well behaved about its minimum and
also that the minimum is far enough away from any boundaries that have been imposed
during the optimization process. If 0 is the true value for the model parameter vector 
and ^ is the maximum likelihood estimator for  then we can use a Taylor expansion
for the value of the log likelihood about the true value as follows:
Lð^Þ  Lð0Þ þ ð^  0ÞDLð0Þ þ ð^  0Þ2
2
D2Lð0Þ
328
Financial Econometrics

Where DL(0) is the gradient evaluated at 0 and D2L(0) is the Hessian evaluated
at 0. We can also expand the gradient DL() about the true value 0 as:
DLð^Þ  DLð0Þ þ ð^  0ÞD2Lð0Þ
However, at a minimum (which is a solution of the likelihood equations in Section
18.1) we must have DL(^) ¼ 0. This gives:
ð^  0ÞD2Lð0Þ ¼ DLð0Þ
and the estimation error of (^  0) is:
ð^  0Þ   DLð0Þ
D2Lð0Þ
ð18:4Þ
We will now assume that  is a scalar and show how the variance of (^  0) is
related to D2L(0).
For a sample of n observations we must, by definition, have:
Z 1
1
. . .
Z 1
1
Fd1; . . . ; dn ¼ 1
where for convenience the sample joint probability density function F() from
Section 18.1 has been denoted by F.
Differentiating w.r.t  we have:
@
@
Z 1
1
. . .
Z 1
1
Fd1; . . . ; dn ¼
Z 1
1
. . .
Z 1
1
@F
@ d1; . . . ; dn ¼ 0
Now since (@ log (F))=(@) ¼ (@ log (F)=(@F))(@F=@) ¼ (1=F)(@F=@) we have:
Z 1
1
. . .
Z 1
1
1
F
@F
@


Fd1; . . . ; dn ¼
Z 1
1
. . .
Z 1
1
@ logðFÞ
@


Fd1; . . . ; dn
so
E @ logðFÞ
@


¼
Z 1
1
. . .
Z 1
1
@ logðFÞ
@


Fd1; . . . ; dn ¼ 0
Differentiating again w.r.t  we have:
@
@
Z 1
1
. . .
Z 1
1
1
F
@F
@


Fd1; . . . ; dn ¼
Z 1
1
. . .
Z 1
1
F @
@
1
F
@F
@



þ
1
F
@F
@


@F
@
	
d1; . . . ; dn ¼ 0
But (@2 log (F))=@ ¼ (@=@)((1=F)(@F=@)) so we have:
Z 1
1
. . .
Z 1
1
@2 logðFÞ
@2
þ
1
F
@F
@

2
(
)
Fd1; . . . ; dn ¼ 0
which gives
Z 1
1
. . .
Z 1
1
@2 logðFÞ
@2
þ
@ logðFÞ
@

2
(
)
Fd1; . . . ; dn ¼ 0
Maximum likelihood parameter estimation
329

So we have:
Z 1
1
. . .
Z 1
1
@ logðFÞ
@

2
Fd1; . . . ; dn ¼ 
Z 1
1
. . .
Z 1
1
@2 logðFÞ
@2


Fd1; . . . ; dn
which using Equation 18.3 gives:
E
X
n
i¼1
@ logð f ðij i1; ÞÞ
@

	2
"
#
¼ E
X
n
i¼1
@2 logð f ðij i1; ÞÞ
@2
"
#
¼ F 
This can be restated as:
1
n
@LðÞ
@

	2
¼ 1
n
@2LðÞ
@2
¼ F 
or equivalently: D2LðÞ ¼ nF 
ð18:5Þ
where F  is the average variance of the independent random variables
@ logð f ðij i1; Þ
@
;
i ¼ 1; . . . ; n
If we denote the variance of the ith variable by 2
i and the sum of these variables by
2
n then:
2
n ¼
logð f ðij i1; ÞÞ
@

	2
and
2
n ¼
X
n
i¼1
2
i ¼ nF 
For convenience we will also use:
Sn ¼
X
n
i¼1
logð f ðij i1; ÞÞ
@
¼ DLðÞ
Now the generalized central limit theorem (Feller, 1971) states that as n!1 the
variable Sn=n becomes distributed as N(0, 1). So at  ¼ 0 we have:
 ¼  DLð0Þ
ðnF 0Þ1=2
ð18:6Þ
where   N(0, 1)
However, from Equations 18.4 and 18.5, we have:
^  0 ¼  DLð0Þ
D2Lð0Þ ¼  DLð0Þ
nF 0
ð18:7Þ
So using Equation 18.6 to substitute for DL(0) in Equation 18.7 we obtain:
^  0 ¼

ðnF 0Þ1=2
ð18:8Þ
This means that:
0  Nð0; n1F 1
0 Þ
330
Financial Econometrics

where 0 ¼ ^  0. The maximum likelihood estimate ^ is therefore distributed about
the true value 0 as:
^ ¼ Nð0; n1F 1
0 Þ
ð18:9Þ
The value F 0 was called by Fisher (1925) the information about 0, see Silvey
(1975), and Cox and Hinkley (1979). The justification for this is simply that when
there is more Fisher information the variance of the estimate ^ will be lower and
therefore the maximum likelihood estimate will improve.
We have just considered the estimation of a single parameter  and thus F 0 is a
scalar. In the more general case  is a vector of Np model parameters and the Np  Np
matrix F 0 is termed the Fisher information matrix. Under these circumstances
Equation 18.5 then becomes:
E @LðÞ
@
@LðÞ
@T


¼ E @2LðÞ
@@T


¼ F 
ð18:10Þ
and in Equation 18.9 n1F 1
0 is the inverse of an Np  Np matrix which yields the
covariance matrix, C, of the estimated parameter vector .
At first sight the preceding discussion seems to have provided us with a very useful
result. There is however a major problem. We don’t know the true parameter vector
0, and so we can’t evaluate F 0. Indeed if we did know the value of 0 it would be
rather pointless computing ^.
The only way forward is to use some kind of approximation to F 0. The most
obvious is to evaluate F  at  ¼ ^, and then use F 0  F ^.
We can now rewrite Equation 18.9 in the following usable form:
^ ¼ Nð0; n1F 1
^ Þ,
where
n1F 1
^
is
@2LðÞ
@@T

1
¼^
ð18:11Þ
In the next section we will discuss numerical optimization and show how F 1
^
occurs naturally in the equations that are used to maximize the log likelihood.
18.2.1
The standard errors and significance
The variance of each estimated parameter is contained in the corresponding diagonal
element of the covariance matrix C. So for a model with Np parameters the standard
errors of the estimated parameters are:
i ¼
ffiffiffiffiffiffi
Ci;i
p
;
i ¼ 1; . . . ; Np
where Ci, i is used to denote the ith diagonal element of the covariance matrix. The
standardized parameter estimate, t statistic, of the estimated value is given by the
estimated value divided by the estimated standard error. So for the ith estimated
parameter we have a t statistic of ti ¼ ^i=i.
We can use the value of ti to provide evidence against the null hypothesis, H0, that
the actual parameter value is zero. That is H0 assumes that the distribution of the ith
standardized parameter estimate is N(0, 1).
Maximum likelihood parameter estimation
331

To illustrate how ti can be used we will now use the following data for a standard-
ized Gaussian distribution:
Prðti  0:52Þ ¼ 0:3;
Prðti  1:64Þ ¼ 0:05
Prðti  1:96Þ ¼ 0:025;
Prðti  2:57Þ ¼ 0:005
where Pr(ti  X) is the probability that the value of ti will be greater or equal to X.
For instance if the estimated value of ti is 2.57 then, the probability of obtaining
this value or greater from H0 is only 0.5 per cent. Under these conditions we should
reject the null hypothesis, and the estimated parameter value i is then said to be
significant at the 0.5 per cent level.
If however the estimated value of ti is only 0.52 then, the probability of obtaining
this value or greater from H0 is 30 per cent (which is quite high). We therefore cannot
reject the null hypothesis that the value of i is zero. The estimated value of i is then
said to be not significant.
18.3
NUMERICAL OPTIMIZATION
The GARCH model parameters  can be estimated by using numerical optimization to
maximize the conditional log likelihood, or equivalently the value of  which minimizes
minus the log likelihood. From now on we will denote minus the log likelihood by L(),
and for simplicity refer to this quantity as the log likelihood, see Section 18.1.
Most optimization procedures use gradient information (either analytic or
numeric) in order to iterate to a global maximum (or minimum).
In most gradient algorithms the kth iteration used to minimize L() takes the form:
^ k ¼ ^ k1  H1DLð^ k1Þ
ð18:12Þ
where ^ k1 is the estimate of the parameter vector obtained after k  1 iterations, H
is some approximation to the Hessian computed at ^k1, which determines the
direction of the kth step,  is a scalar which specifies the step size in the given
direction and DL(^k1) the gradient is computed at ^ k1.
Some commonly used approximations to H are as follows:
. The actual Hessian @2L()=@@T.
. The conditional expectation of the Hessian.
. A positive definite matrix that is an approximation to the Hessian.
. The outer product (@L()=@)(@L()=@T).
When the Hessian is approximated by the outer product the method is known as
the BHHH algorithm, see Berndt et al. (1974).
We note that when  ¼ 1 and H is the actual Hessian @2L()=@@T then the
optimization algorithm is called Newton–Raphson or simply Newton.
In maximum likelihood estimation it is often convenient to approximate the
Hessian by n F , where F  is the Fisher information matrix. When this is done we
have the method of scoring, and Equation 18.12 then becomes:
^k ¼ ^k1  n1F 1
^ DLð^k1Þ
ð18:13Þ
332
Financial Econometrics

This technique is likely to have a lower convergence rate than a straightforward
Newton method because the information matrix is only an approximation to the
Hessian. However, in may instances the information matrix has a simple form and is
much easier to compute than the complete Hessian. Also the information matrix will
always be positive definite and so its inverse can be computed, this is not necessarily
the case for the actual Hessian.
Quasi-Newton methods do not require the Hessian to be explicitly evaluated
(Gill et al., 1981; Murtagh and Saunders, 1983). The iterative scheme is of the
form of Equation 18.12 and the matrix H must be a positive definite. At each
iteration H is updated in such a way as to yield a series of positive definite
matrices which eventually converge to the inverse of the Hessian. The initial
H matrix can be any positive definite matrix, and a common choice is the
identity matrix.
In Chapter 21 results are presented which show the relative advantages/disadvan-
tages of using numeric/analytic gradients during maximum likelihood optimization.
These results are from GARCH software which used a general purpose quasi-
Newton nonlinear optimization routine. First derivatives could be supplied either
in analytic form or computed numerically by finite-difference techniques. The optim-
ization process relied on a Hessian which was always computed internally by the
nonlinear optimizer. However, it was possible to retrieve the Hessian at the solution
point ^, and thus use it as an approximation to the Fisher information matrix.
GARCH stationary conditions could be ensured by imposing the linear constraint
Pq
j¼1 j þ Pp
j¼1 j < 1 during the numerical optimization.
In Chapter 21 the following approximations to the Fisher information matrix were
used:
. The second-derivative estimate, based on the actual value of the Hessian at the
solution point ^, that is (@2L())=(@@T
¼^). This is calculated numerically using
finite differences.
. The second-derivative estimate, based on the conditional expectation of the Hessian
at the solution point ^, that is E((@2L())=(@@T))¼^.
The difficulty of modelling a GARCH(p,q) sequence depends on both p and q and
also on how much volatility memory there is in the process. Higher values of the
parameters j, j ¼ 1, . . . , p, give rise to more volatility memory and are therefore
harder to model accurately. Increasing the number of model parameters will also
make the model more difficult to model simply because there are more variables to
numerically optimize. This suggests the following order of difficulty ARCH(1),
ARCH(2), ARCH(3), GARCH(1,1), GARCH(1,2), GARCH(2,2), etc.
In Chapter 19 information is given on how to compute the analytic gradients for
a regression GJR–GARCH(p,q) sequence. Chapter 20 elaborates on the informa-
tion in Chapter 19, and provides complete pseudocode that enables the reader to
write computer programs to calculate both the conditional log likelihood and its
gradients.
Maximum likelihood parameter estimation
333

18.4
SCALING THE DATA
Numerical optimization procedures can have difficulty in minimizing a function in
which the magnitudes of the individual variables differ by a large factor (say 106 or
greater).
This
can
occur
in
GARCH(p,q)
processes
where
the
parameters
i, i ¼ 1, . . . , p, i, i ¼ 1, . . . , q are usually in the range 0.1 to 1, but the parameter
0 can be very small. In these circumstances scaling the observations, yi, i ¼ 1, . . . , n,
by  will result in a time series in which 0 is multiplied by the factor 2. For instance
if 0 is 106 in the original sequence, then scaling the data by 100 gives a new series
with 0 ¼ 102.
Here we will consider data scaling for both linear and nonlinear GARCH models,
and show how the model parameters for the scaled data are related to those of the
original data.
18.4.1
Scaling a linear GARCH process
Here we consider the effect of scaling the GARCH process:
yi ¼ XT
i b þ b0 þ i;
ij i1  Rð0; hiÞ
hi ¼ 0 þ
X
q
j¼1
j2
ij þ
X
p
j¼1
jhij;
i ¼ 1; . . . ; n
If the observations yi are scaled by the factor  then we have the new GARCH
process:
Yi ¼ XT
i B þ B0 þ Ei;
Eij i1  Rð0; HiÞ
Hi ¼ L0 þ
X
q
j¼1
jE2
ij þ
X
p
j¼1
jHij;
i ¼ 1; . . . ; n
where Yi ¼ yi, L0 ¼ 20, B ¼ b, B0 ¼ b0, Ei ¼ i, and Hi ¼ 2hi.
The GARCH model parameter vector, , of the scaled process is:
 ¼ ðL0; i; i ¼ 1; . . . ; q; i; i ¼ 1; . . . ; p; B; B0Þ
18.4.2
Scaling an AGARCH-I process
Referring to the AGARCH-I process specification in Chapter 16, and proceeding in
a similar manner to Section 18.3.1, we have:
Yi ¼ XT
i B þ B0 þ Ei;
Eij i1  Rð0; HiÞ
Hi ¼ L0 þ
X
q
j¼1
jðEij þ GÞ2 þ
X
p
j¼1
jHij;
i ¼ 1; . . . ; n
where  is the scale factor and Yi ¼ yi, Hi ¼ 2hi, L0 ¼ 20, Ei ¼ ii, G ¼ ,
B ¼ b, and B0 ¼ b0.
The GARCH model parameter vector, , of the scaled process is then:
 ¼ ðL0; i; i ¼ 1; . . . ; q; i; i ¼ 1; . . . ; p; G; B; B0Þ
334
Financial Econometrics

18.4.3
Scaling an AGARCH-II process
Referring to the AGARCH-II process specification in Chapter 16, and proceeding in
a similar manner to Section 18.3.1, we have:
Yi ¼ XT
i B þ B0 þ Ei;
Eij i1  Rð0; HiÞ
Hi ¼ 0 þ
X
q
j¼1
jðjEijj þ EijÞ2 þ
X
p
j¼1
jHij;
i ¼ 1; ::; n
where  is the scale factor, and L0 ¼ 20, Hi ¼ 2hi, Ei ¼ ii, B ¼ b, and
B0 ¼ b0.
The GARCH model parameter vector, , of the scaled process is then:
L0; i; i ¼ 1; . . . ; q; i; i ¼ 1; . . . ; p; ; B and B0
18.4.4
Scaling a GJR–GARCH process
Referring to the GJR–GARCH process specification in Chapter 16, and proceeding
in a similar manner to Section 18.3.1, we have:
Yi ¼ XT
i B þ B0 þ Ei;
Eij i1  Rð0; HiÞ
Hi ¼ L0 þ
X
q
j¼1
ðj þ SijÞE2
ij þ
X
p
j¼1
jHij;
i ¼ 1;…; n
where  is the scale factor and Si ¼ 1, if Ei < 0, and Si ¼ 0, if Ei  0: The scaled
parameters are now: L0 ¼ 20, Hi ¼ 2hi, Ei ¼ ii, B ¼ b, and B0 ¼ b0.
The GARCH model parameter vector, , of the scaled process is then:
L0, i, i ¼ 1, . . . , q, i, i ¼ 1, . . . , p, , B and B0.
Maximum likelihood parameter estimation
335

Chapter 19
Analytic derivatives of the log likelihood
In this chapter we show how to calculate analytic expressions for the first and
second order partial derivatives of the log likelihood function. As previously
mentioned in Section 18.3 these partial derivatives are used by Newton type
numerical optimizers to minimize the log likelihood and thus obtain an estimate
for the GARCH model parameter vector, . The analytic second derivative is used
to as an approximation to the Fisher information matrix, and as a means of
calculating the standard errors.
Information on how to compute the analytic derivatives of a standard regression-
GARCH(p,q) process with Gaussian residuals is available in the literature, Fiorentini
et al. (1996).
In Section 19.1 we show how to compute the first derivatives of a regression-
GARCH(p,q) process which has either Gaussian distributed residuals or Student’s t
distributed residuals.
In Section 19.2 we show how to compute the conditional expectation of the
Hessian for a regression-GARCH(p,q) process with Gaussian distributed residuals.
This is used as an approximation for the Fisher information matrix.
The results of this section will be used in Chapter 20 to derive computational
algorithms which compute the derivatives of a regression-GJR–GARCH model. The
results are also used in Appendix H to compute the derivatives of a regression-
AGARCH-I model.
19.1
THE FIRST DERIVATIVES
19.1.1
Gaussian distribution
Here we obtain expressions for the partial derivatives of the Gaussian log likelihood,
Equation 17.4.
Partial derivatives w.r.t. the parameter vector !:
@LiðÞ
@!
¼ 1
2
@ðlog hiÞ
@hi
@hi
@! þ 2
i
2
@ð1=hiÞ
@hi
@hi
@!
@LiðÞ
@!
¼ 1
2hi
@hi
@!  2
i
2h2
i
@hi
@!
ð19:1Þ

Partial derivative w.r.t. the parameter b0:
@LiðÞ
@b0
¼ 1
2
@ logðhiÞ
@b0
þ 1
2
@2
i
@b0
1
hi
þ 2
i
2
@ð1=hiÞ
@hi
@hi
@b0
¼ 1
2hi
@hi
@b0
þ 1
2hi
@2
i
@b0
 2
i
2h2
i
@hi
@b0
ð19:2Þ
But since i ¼ yi  XT
i b  b0 we obtain:
@2
i
@b0
¼ 2i @i
@b0
¼ 2i
@ðyi  XT
i b  b0Þ
@b0
¼ 2i
@LiðÞ
@b0
¼ 1
2hi
@hi
@b0
 i
hi
 2
i
2h2
i
@hi
@b0
@LiðÞ
@b0
¼  i
hi
 1
2hi
@hi
@b0
2
i
h2
i
 1


ð19:3Þ
Similarly we obtain the partial derivative w.r.t. the parameter vector b:
@LiðÞ
@b
¼ 1
2
@ logðhiÞ
@b
þ 1
2
@2
i
@b
1
hi
þ 2
i
2
@ð1=hiÞ
@hi
@hi
@b
¼ 1
2hi
@hi
@b þ 1
2hi
@2
i
@b  2
i
2h2
i
@hi
@b
ð19:4Þ
Since
@2
i
@b ¼ 2i @i
@b ¼ 2i
@ðyi  XT
i b  b0Þ
@b
¼ 2iXi
@LiðÞ
@b
¼ 1
2hi
@hi
@b  iXi
hi
 2
i
2h2
i
@hi
@b
@LiðÞ
@b
¼  iXi
hi
 1
2hi
@hi
@b
2
i
h2
i
 1


ð19:5Þ
In summary we have:
Gaussian log likelihood partial derivatives
@LðÞ
@!
¼ 
X
n
i¼1
1
2hi
@hi
@!
2
i
hi
 1




ð19:6Þ
@LðÞ
@b0
¼ 
X
n
i¼1
i
hi
þ 1
2hi
@hi
@b0
2
i
hi
 1




ð19:7Þ
@LðÞ
@b
¼ 
X
n
i¼1
iXi
hi
þ 1
2hi
@hi
@b
2
i
hi
 1




ð19:8Þ
Analytic derivatives of the log likelihood
337

19.1.2
Student’s t distribution
Here we obtain expressions for the partial derivatives of the log likelihood when the
series shocks have a Student’s t distribution. Using Equation 17.8 we have:
Partial derivatives w.r.t. the parameter vector !:
@LiðÞ
@!
¼ 1
2hi
@hi
@! þ ð þ 1Þ
2
@ log 1 þ 2
i =ðð  2ÞhiÞ


@ 1 þ 2
i =ðð  2ÞhiÞ
ð
Þ
@ 1 þ 2
i =ðð  2ÞhiÞ


@!
¼ 1
2hi
@hi
@! þ
 þ 1
2 1 þ 2
i =ðð  2ÞhiÞ
ð
Þ
@ 2
i =ðhið  2ÞÞ


@!
¼ 1
2hi
@hi
@! 
 þ 1
2 1 þ 2
i =ðð  2ÞhiÞ
ð
Þ
2
i
h2
i ð  2Þ
@hi
@!
¼ 1
2hi
@hi
@! 
ð þ 1Þ2
i
2h2
i ð  2Þ þ 2
i =hi
ð
Þ
@hi
@!
@LiðÞ
@!
¼ 1
2hi
@hi
@!  2
i
2h2
i
@hi
@! G;
where
G ¼
ð þ 1Þ
ð  2Þ þ ð2
i =hiÞ
ð19:9Þ
Similarly we obtain the partial derivative w.r.t. the mean term, b0:
@LiðÞ
@b0
¼  i
hi
G þ 1
2hi
1  G 2
i
hi


@hi
@b0
ð19:10Þ
Partial derivatives w.r.t. the parameter vector b:
@LiðÞ
@b
¼ 1
2
@ðlog hiÞ
@hi
@hi
@b þ
ð þ 1Þ
2 1 þ 2
i =ðð  2ÞhiÞ
ð
Þ
@ 1 þ 2
i =ðð  1ÞhiÞ


@b
¼ 1
2hi
@hi
@b þ
 þ 1
2hið  2Þ
1
1 þ 2
i =ðð  2ÞhiÞ

 @2
i
@b
þ ð þ 1Þ2
i
2ð  2Þ
1
ð1 þ 2
i =ðð  2ÞhiÞÞ

 @ð1=hiÞ
@b
ð19:11Þ
Since @(1=hi)=@b ¼ (1=h2
i )(@hi=@b) we obtain:
@LiðÞ
@b
¼ 1
2hi
@hi
@b  ð þ 1Þ2
i
2h2
i ð  2Þ
1
1 þ 2
i =ðð  2ÞhiÞ


@hi
@b
 2iXið þ 1Þ
2hið  2Þ
1
1 þ 2
i =ðð  2ÞhiÞ


¼  iXið þ 1Þ
ð  2Þhi
1
1 þ 2
i =ðð  2ÞhiÞ


þ 1
2hi
1  2
i ð þ 1Þ
hið  2Þ
1
1 þ 2
i =ðð  2ÞhiÞ




@LiðÞ
@b
¼  iXi
hi
G þ 1
2hi
1  G 2
i
hi


@hi
@b
ð19:12Þ
338
Financial Econometrics

Partial derivative w.r.t. the number of degrees of freedom, :
Since (@( log (x)))=@x ¼  (x) we have the following, Abramowitz and Stegun
(1968):
@ log ðð þ 1Þ=2Þ
ð
Þ
@
¼ 1
2   þ 1
2


and @ log ð=2Þ
ð
Þ
@
¼ 1
2  
2
 	
Using this we obtain:
@LiðÞ
@
¼  1
2   þ 1
2


þ 1
2  ð=2Þ þ
1
2ð  2Þ þ 1
2 log 1 þ
2
i
ð  2Þhi



 þ 1
2 1 þ 2
i =ðð  2ÞhiÞ
ð
Þ
2
i
hið  2Þ2
@LiðÞ
@
¼  1
2   þ 1
2


þ 1
2  
2
 	
þ
1
2ð  2Þ
þ 1
2 log 1 þ
2
i
ð  2Þhi



2
i
2ð  2Þhi
G
ð19:13Þ
In summary we have:
Student’s t distribution log likelihood partial derivatives
@LðÞ
@!
¼ 
X
n
i¼1
1
2hi
@hi
@!
2
i
hi
G  1




ð19:14Þ
@LðÞ
@
¼ 
X
n
i¼1
K  1
2 log 1 þ
2
i
ð  2Þhi


þ
2
i
2ð  2Þhi
G


ð19:15Þ
@LðÞ
@b0
¼ 
X
n
i¼1
i
hi
G þ 1
2hi
@hi
@b0
2
i
hi
G  1




ð19:16Þ
@LðÞ
@b
¼ 
X
n
i¼1
iXi
hi
G þ 1
2hi
@hi
@b
2
i
hi
G  1




ð19:17Þ
where G ¼
ð þ 1Þ
ð  2Þ þ 2
i =hi


and
K ¼ 1
2   þ 1
2


 1
2  
2
 	

1
2ð  2Þ
19.2
THE SECOND DERIVATIVES
As previously mentioned the Hessian of the log likelihood can be used as an
approximation to the Fisher information matrix. Here we will assume that the con-
ditional PDF of the residuals is Gaussian and calculate the conditional expectation of
Analytic derivatives of the log likelihood
339

the Hessian. We will use the result (Engle, 1982) that the off-diagonal block elements
of this matrix are zero, and will only compute the diagonal block elements.
We
will
denote
the
standardized
residuals
i=
ffiffiffiffihi
p
by
Zi.
So
we
have
Zij i1  NID(0, 1). Further we will use following results:
EðZij i1Þ ¼ 0; EðZ2
i j i1Þ ¼ 1; and EðZ2
i j i1  1Þ ¼ 0
ð19:18Þ
We note, j and k, k 6¼ j are independent, and since in a GARCH(p,q) process hi
only depends on past values of the residuals, i, i ¼ 1, . . . , q, we have that hi and Zi
are independent.
Using this gives:
E Z2
i
h2
i


¼ EðZ2
i ÞE
1
h2
i


¼ 1
h2
i
ð19:19Þ
Calculation of the diagonal block @2Li()/@!@!T
Recalling from Section 19.1 that the first derivative is:
@LiðÞ
@!
¼  1
2hi
@hi
@!
2
i
hi
 1


Taking second derivatives w.r.t. ! we have:
@2LiðÞ
@!@!T ¼  2
i
hi
 1


@
@!T
1
2hi
@hi
@!


 1
2hi
@hi
@!
@
@!T
2
i
hi
 1


¼  2
i
hi
 1


@
@!T
1
2hi
@hi
@!


 2
i
2hi
@hi
@!
@ð1=hiÞ
@hi
@hi
@!T
¼  2
i
hi
 1


@
@!T
1
2hi
@hi
@!


þ 2
i
2h3
i
@hi
@!
@hi
@!T
which expressed using standardized residuals is:
@2LiðÞ
@!@!T ¼  Z2
i  1

 @
@!T
1
2hi
@hi
@!


þ Z2
i
2h2
i
@hi
@!
@hi
@!T
Therefore the conditional expectation of the block at time instant i is:
E @2LiðÞ
@!@!T


¼ E  Z2
i  1

 @
@!T
1
2hi
@hi
@!


þ EðZ2
i Þ
2h2
i
@hi
@!
@hi
@!T


E @2LiðÞ
@!@!T


¼ E
Z2
i  1



 @
@!T
1
2hi
@hi
@!


þ 1
2h2
i
@hi
@!
@hi
@!T
340
Financial Econometrics

which gives
E @2LiðÞ
@!@!T


¼ 1
2h2
i
@hi
@!
@hi
@!T
The sample diagonal block is therefore:
E @2LðÞ
@!@!T


¼
X
n
i¼1
1
2h2
i
@hi
@!
@hi
@!T
ð19:20Þ
Calculation of the diagonal block @2Li()=@b@bT
Recalling from Section 19.1 that the first derivative is:
@LiðÞ
@b
¼  iXi
hi
þ 1
2hi
@hi
@b
2
i
hi
 1


Taking second derivatives w.r.t. to b we have:
@2LiðÞ
@b@bT ¼  Xi
hi
@i
@bT  iXi @ð1=hiÞ
@hi
@hi
@bT  1
2
@ð1=hiÞ
@hi
@hi
@bT
@hi
@b
2
i
hi
 1


 1
2hi
@hi
@b
@
@bT
2
i
hi
 1


But since i ¼ yi  XT
i b  b0
@i
@bT ¼ @ðyi  XT
i b  b0Þ
@bT
¼ XT
i
and
@2
i
@bT ¼ 2iXi
We have:
@2LiðÞ
@b@bT ¼ XiXT
i
hi
þ iXi
h2
i
@hi
@bT  1
2
@ð1=hiÞ
@hi
@hi
@bT
@hi
@b
2
i
hi
 1


þ iXi
h2
i
@hi
@bT þ 2
i
2h3
i
@hi
@b
@hi
@bT
Therefore using standardized residuals and taking conditional expectations of the
block at time instant i we have:
@2LiðÞ
@b@bT


¼ XiXT
i
hi
þ EðiÞXi
h2
i
@hi
@bT  1
2
@ð1=hiÞ
@hi
@hi
@bT
@hi
@b E
Z2
i  1




þ EðiÞXi
h2
i
@hi
@bT þ EðZ2
i Þ
2h2
i
@hi
@b
@hi
@bT
which gives:
E @2LiðÞ
@b@bT


¼ XiXT
i
hi
þ 1
2h2
i
@hi
@b
@hi
@bT
Analytic derivatives of the log likelihood
341

The sample diagonal block is therefore:
E @2LðÞ
@b@bT


¼
X
n
i¼1
XiXT
i
hi
þ 1
2h2
i
@hi
@b
@hi
@bT


ð19:21Þ
Calculation of the diagonal block @2Li()=@b0@bT
0
Recalling from Section 19.1 that the first derivative is:
@LiðÞ
@b0
¼  i
hi
þ 1
2hi
@hi
@b0
2
i
hi
 1


Taking second derivatives w.r.t. to b0 we have:
@2LiðÞ
@b0@bT
0
¼  1
hi
@i
@bT
0
 i @ð1=hiÞ
@hi
@hi
@bT
0
 1
2
@ð1=hiÞ
@hi
@hi
@bT
0
@hi
@b0
2
i
hi
 1


 1
2hi
@hi
@b0
@
@bT
0
2
i
hi
 1


But since i ¼ yi  XT
i b  b0
@i
@bT
0
¼ @ðyi  XT
i b  b0Þ
@bT
0
¼  @b0
@b0
¼ 1
and
@2
i
@bT ¼ 2i
We have:
@2LiðÞ
@b0@bT
0
¼ 1
hi
þ i
h2
i
@hi
@bT
0
 1
2
@ð1=hiÞ
@hi
@hi
@bT
0
@hi
@b0
2
i
hi
 1


þ i
h2
i
@hi
@bT
0
þ 2
i
2h3
i
@hi
@b0
@hi
@bT
0
Therefore using standardized residuals and taking conditional expectations of the
block at time instant i we have:
E @2LiðÞ
@b0@bT
0


¼ 1
hi
þ EðiÞ
h2
i
@hi
@bT
0
 1
2
@ð1=hiÞ
@hi
@hi
@bT
0
@hi
@b0
E
Z2
i  1




þ EðiÞ
h2
i
@hi
@bT
0
þ EðZ2
i Þ
2h2
i
@hi
@b0
@hi
@bT
0
which gives:
E @2LiðÞ
@b0@bT
0


¼ 1
hi
þ 1
2h2
i
@hi
@b0
@hi
@bT
0
The sample diagonal block is therefore:
E
@2LðÞ
@b0@bT
0


¼
X
n
i¼1
1
hi
þ 1
2h2
i
@hi
@b0
@hi
@bT
0


ð19:22Þ
342
Financial Econometrics

In summary we obtain:
The blocks of the Fisher information matrix
E @2LðÞ
@!@!T


¼
X
n
i¼1
1
2h2
i
@hi
@!
@hi
@!T
ð19:23Þ
E
@2LðÞ
@b0@bT
0


¼
X
n
i¼1
1
hi
þ 1
2h2
i
@hi
@b0
@hi
@bT
0


ð19:24Þ
E @2LðÞ
@b@bT


¼
X
n
i¼1
XiXT
i
hi
þ 1
2h2
i
@hi
@b
@hi
@bT


ð19:25Þ
It can be seen that these diagonal blocks of the information matrix involve the
outer product of the following first derivative vectors n
i¼1@hi=@!, n
i¼1@hi=@b, and
also the square of the scalar derivative n
i¼1@hi=@b0. Once these terms have been
computed it is easy to calculatethe information matrix. Chapter 20 provides details
on how this can be accomplished.
Analytic derivatives of the log likelihood
343

Chapter 20
GJR–GARCH algorithms
We will now use the information in Chapter 19 to show how the partial derivatives of
the log likelihood can be computed. Practical details concerning initial estimates and
pre-observed values are discussed. Pseudocode is also provided to facilitate computer
implementations of the regression-GJR–GARCH model.
The notation used in this section is as follows:
num
the number of terms in the GARCH sequence, num is synonymous with
the mathematical symbol n.
mn
indicates whether the mean term b0 is included in the model. If mn¼¼1
then b0 is included, otherwise it is not.
nreg
the number of regression terms in the model, nreg is synonymous with
the mathematical symbol k.
npar
the number of heteroskedastic parameters in a standard symmetric
Gaussian GARCH model, that is 1 þ p þ q.
^b
the initial estimate for b, the k element vector of regression coefficients.
^b0
the initial estimate for b0, the mean term.
^k
the kth element of the regression-GARCH parameter vector . The order
of the elements is the same as given in Chapter 17. That is:
1 ¼ 0, kþ1 ¼ k, k ¼ 1, . . . ,q, 1þqþk ¼ k, k¼ 1, . . . ,p,
nparþ1 ¼ ; etc:
H(i  k)
a function which has the value 1 when i > k and zero otherwise.
Np
the total number of parameters to estimate. In the Gaussian
regression-GJR–GARCH Np ¼ 2 þ p þ q þ mn þ nreg, and in the
Student’s t distribution Np ¼ 3 þ p þ q þ mn þ nreg.
All other symbols have been previously defined in Chapters 14 and 15.
20.1
INITIAL ESTIMATES AND PRE-OBSERVED VALUES
In this section we consider how to estimate the initial values that are required for
computing both the log likelihood and its partial derivatives.
The initial estimates of the regression coefficients, ^bibi, i ¼ 1  mn, . . . , k, can be
obtained using linear regression.

If mn is 1 then the residuals are calculated as:
i ¼ yi  Xi ^b  ^b0;
i ¼ 1; . . . ; n
ð20:1Þ
otherwise they are:
i ¼ yi  Xi ^b;
i ¼ 1; . . . ; n
ð20:2Þ
In all GARCH processes the conditional variance hi satisifies a recursive equation.
For instance the basic linear GARCH model has:
hi ¼ 0 þ
X
q
j¼1
j2
ij þ
X
p
j¼1
jhij;
t ¼ 1; . . . ; n
This means that the conditional variance for the term h1 is given by:
h1 ¼ 0 þ
X
q
j¼1
j2
1j þ
X
p
j¼1
jh1j
which relies on the terms 2
0, 2
1, . . . , 2
1j, and h0, h1, . . . , h1j, that refer to times
before the sequence started. We will call this terms pre-observed values. There are
various methods of providing estimates for these values.
One simple approach is to model an alternative time series which starts at the data
point i ¼ max ( p, q) and has the reduced length n  max ( p, q). The first max ( p, q)
terms are then used to calculate the pre-observed values.
The pre-observed values of i can now use the actual values, and 2
i can be used as
an estimate for hi.
However, this method is not entirely satisfactory as we are not modelling the true
data and also the single value 2
i is unlikely to be a good estimate of the conditional
variance hi.
Here we use a different technique. The initial value for the variance, 	2
0, is taken as
the average value of 2
i using the first 
 terms of the sequence:
	2
0 ¼ 1

X

i¼1
2
i
ð20:3Þ
The optimal value of 
 to use will depend on the nature of the data. If the sequence
has high initial volatility then 
 should be short enough to capture this. For
sequences with less initial variation the estimate 	2
0 will benefit from an increased
value of 
.
Here we used, the compromise value 
 ¼ Np. This value is used in Equation 20.3 to
calculate the pre-observed conditional variance and residuals squared, i.e.:
2
i ¼ hi ¼ 	2
0;
i  0
The pre-observed values for the residuals, i, are taken as:
i ¼ E½j	 ¼ 0;
where i  0
and
j ¼ 1; . . . ; n
GJR–GARCH algorithms
345

Since @hi=@k is calculated recursively from previous terms such as p
j¼1j(@hij=@k)
and q
j¼1j(@2
ij)=(@k) we can make use of the fact that @2
i =@k ¼ @hi=@k ¼ 0,
k ¼ 1, . . . , Np, i  0, i.e.:
@2
i
@! ¼ @2
i
@b0
¼ @2
i
@b ¼ 0;
i  0
ð20:4Þ
and
@hi
@! ¼ @hi
@b0
¼ @hi
@b ¼ 0;
i  0
ð20:5Þ
Note: Although this is correct for a Gaussian distribution it is not strictly true for a
Student’s t distribution, since the derivative term @hi=@ does not depend on its
previous value.
Using the above results, for i  q we now have:
X
q
j¼1
j
@2
ij
@k
¼
X
i1
j¼1
j
@2
ij
@k
ð20:6Þ
and
X
p
j¼1
j
@hij
@k
¼
X
p
j¼1
j
@hij
@k
Hði  jÞ
ð20:7Þ
Further details are provided in the pseudocode provided in the following section.
20.2
GAUSSIAN DISTRIBUTION
20.2.1
The log likelihood
Deal with the first q terms of the sequence:
 ¼ ^
LðÞ ¼ 0
For i ¼ 1 To num
If (mn ¼¼ 1) i ¼ yi  XT
i ^b
If (mn ¼¼ 0) i ¼ yi  ^b0  XT
i ^b
Next i
For i ¼ 1 To q
hi ¼ 0 þ
X
i1
j¼1
ðj þ SijÞ2
ij þ
X
q
j¼i
j	2
0 þ
X
p
k¼1
hikk
Store the current value of hi and keep all the previous values of hi.
LðÞ ¼ LðÞ þ 1
2
logðhiÞ þ 2
i
hi


Next i
346
Financial Econometrics

Deal with the remaining terms of the sequence:
For i ¼ q þ 1 To num
hi ¼ 0 þ
X
q
j¼1
ðj þ SijÞ2
ij þ
X
p
k¼1
hikk
Store the current value of hi and keep Np previous values of hi.
LðÞ ¼ LðÞ þ 1
2
logðhiÞ þ 2
i
hi


Next i
20.2.2
The first derivatives of the log likelihood
Algorithm for the first q terms of the sequence:
@LðÞ
@k
¼ 0;
k ¼ 1; . . . ; Np
For i ¼ 1 to q
@hi
@0
¼ 1 þ
X
p
k¼1
k
@hik
@0
For j ¼ 1 to i  1
@hi
@j
¼ 2
ij
Next j
For j ¼ i to q
@hi
@j
¼ 	2
0
Next j
For j ¼ 1 to q
@hi
@j
¼ @hi
@j
þ
X
p
k¼1
k
@hik
@j
Next j
For j ¼ 1 to p
@hi
@j
¼ hij þ
X
p
k¼1
j
@hik
@k
Next j
@hi
@ ¼
X
i1
j¼1
2
ij þ
X
p
k¼1
k
@hik
@
GJR–GARCH algorithms
347

hi ¼ 0 þ
X
p
k¼1
hikk þ
X
i1
j¼1
ðj þ SijÞ2
ij þ
X
q
j¼i
j	2
0
if (mn ¼¼ 1) then
@hi
@b0
¼ 2
X
i1
k¼1
ðk þ SikÞik þ
X
p
k¼1
k
@hik
@b0
Hði  kÞ
end if
For j ¼ 1 to nreg
@hi
@bj
¼ 2
X
i1
k¼1
ðk þ SikÞikXj
ik þ
X
p
k¼1
k
@hik
@bj
Hði  kÞ
Next j
Store the current values of hi and @hi=@ and keep all the previous values of hi and
@hi=@.
For k ¼ 1 to npar þ 1
@LðÞ
@k
¼ @LðÞ
@k
 1
2hi
2
i
hi
 1


@hi
@k
Next k
if (mn ¼¼ 1) then
@LðÞ
@b0
¼ @LðÞ
@b0
 i
hi
 1
2hi
2
i
hi
 1


@hi
@b0
end if
For k ¼ 1 to nreg
@LðÞ
@bk
¼ @LðÞ
@bk
 Xk
i i
hi
 1
2hi
2
i
hi
 1


@hi
@bk
Next k
Next i
Algorithm for the remaining terms of the sequence:
For i ¼ qþ 1 to num
@hi
@0
¼ 1 þ
X
p
k¼1
k
@hik
@0
For j ¼ 1 to q
@hi
@j
¼ 2
ij
348
Financial Econometrics

Next j
For j ¼ 1 to q
@hi
@j
¼ @hi
@j
þ
X
p
k¼1
k
@hik
@j
Next j
For j ¼ 1 to p
@hi
@j
¼ hij þ
X
p
k¼1
j
@hik
@k
Next j
@hi
@ ¼
X
q
j¼1
2
ij þ
X
p
k¼1
k
@hik
@
hi ¼ 0 þ
X
p
k¼1
hikk þ
X
q
j¼1
ðj þ SijÞ2
ij
if (mn ¼¼ 1) then
@hi
@b0
¼ 2
X
q
k¼1
ðk þ SikÞik þ
X
p
k¼1
k
@hik
@b0
Hði  kÞ
end if
For j ¼ 1 to nreg
@hi
@bj
¼ 2
X
q
k¼1
ðk þ SikÞikXj
ik þ
X
p
k¼1
k
@hik
@bj
Hði  kÞ
Next j
Store the current values of hi and @hi=@ and keep Np previous values of hi and @hi=@.
For k ¼ 1 to npar þ 1
@LðÞ
@k
¼ @LðÞ
@k
 1
2hi
2
i
hi
 1


@hi
@k
Next k
if (mn ¼¼ 1) then
@LðÞ
@b0
¼ @LðÞ
@b0
 i
hi
 1
2hi
2
i
hi
 1


@hi
@b0
end if
For k ¼ 1 to nreg
@LðÞ
@bk
¼ @LðÞ
@bk
 Xk
i i
hi
 1
2hi
2
i
hi
 1


@hi
@bk
Next k
Next i
GJR–GARCH algorithms
349

20.3
STUDENT’S t DISTRIBUTION
20.3.1
The log likelihood
Deal with the first q terms of the sequence:
 ¼ ^
L() ¼ 0
M ¼ log((( þ 1)=2))  log((=2))  1
2 log(  2)
For i ¼ 1 To num
If mn ¼¼ 1
i ¼ yi  XT
i ^b
If mn ¼¼ 0
i ¼ yi  ^b0  XT
i ^b
Next i
For i ¼ 1 To q
hi ¼ 0 þ
X
i1
j¼1
ðj þ SijÞ2
ij þ
X
q
j¼i
j	2
0 þ
X
p
k¼1
khik
Store the current value of hi and keep all the previous values of hi.
LðÞ ¼ LðÞ  M þ 1
2 logðhiÞ þ  þ 1
2
log 1 þ
2
t
ð  2Þhi


Next i
Deal with the remaining terms of the sequence:
For i ¼ q þ 1 To num
hi ¼ 0 þ
X
q
j¼1
ðj þ SijÞ2
ij þ
X
p
k¼1
khik
Store the current value of hi and keep Np previous values of hi.
LðÞ ¼ LðÞ  M þ 1
2 logðhiÞ þ  þ 1
2
log 1 þ
2
t
ð  2Þhi


Next i
20.3.2
The first derivatives of the log likelihood
Algorithm for the first q terms of the sequence:
@LðÞ
@k
¼ 0;
k ¼ 1; . . . ; Np
For i ¼ 1 to q
350
Financial Econometrics

Compute hi as described in Section 20.2.1. Also calculate the derivatives @hi=@j,
j ¼ 1, . . . , Np, as described for a Gaussian distribution in Section 20.1.2. Store hi and
@hi=@j, j ¼ 1, . . . , Np, and keep all the previous values of hi and @hi=@.
Set G ¼
( þ 1)
(  2) þ 2
i =hi)


For k ¼ 1 to npar þ 1
@LðÞ
@k
¼ @LðÞ
@k
 1
2hi
1  2
i
hi
G


@hi
@k
Next k
@LðÞ
@
¼ @LðÞ
@
 1
2   þ 1
2


þ 1
2  
2
 
þ
1
2ð  2Þ
þ 1
2 log 1 þ
2
i
ð  2Þhi



2
i
2ð  2Þhi
G
if (mn ¼¼ 1) then
@LðÞ
@b0
¼ @LðÞ
@b0
 i
hi
G  1
2hi
2
i
hi
G  1


@hi
@b0
end if
For k ¼ 1 to nreg
@LðÞ
@bk
¼ @LðÞ
@bk
 Xk
i i
hi
G  1
2hi
2
i
hi
G  1


@hi
@bk
Next k
Next i
Algorithm for the remaining terms of the sequence:
For i ¼ qþ 1 to num
Compute
hi
as
described
in
Section
20.2.1.
Also
calculate
the
derivatives
@hi=@j, j ¼ 1, . . . , Np, as described for a Gaussian distribution in Section 20.1.2. Store
hi and @hi=@j, j ¼ 1, . . . , Np, and keep Np previous values of hi and @hi=@.
Set G ¼
ð þ 1Þ
ð  2Þ þ 2
i =hi


For k ¼ 1 to npar þ 1
@LðÞ
@k
¼ @LðÞ
@k
 1
2hi
1  2
i
hi
G


@hi
@k
Next k
GJR–GARCH algorithms
351

@LðÞ
@
¼ @LðÞ
@
 1
2   þ 1
2


þ 1
2  
2
 
þ
1
2ð  2Þ
þ 1
2 log 1 þ
2
i
ð  2Þhi



2
i
2ð  2Þhi
G
if (mn ¼¼ 1) then
@LðÞ
@b0
¼ @LðÞ
@b0
 i
hi
G  1
2hi
2
i
hi
G  1


@hi
@b0
end if
For k ¼ 1 to nreg
@LðÞ
@bk
¼ @LðÞ
@bk
 Xk
i i
hi
G  1
2hi
2
i
hi
G  1


@hi
@bk
Next k
Next i
352
Financial Econometrics

Chapter 21
GARCH software
In this chapter we will describe some of the expected capabilities of practical
GARCH software, and also how to test whether the software performs as expected.
21.1
EXPECTED SOFTWARE CAPABILITIES
To illustrate we will consider the requirements for the regression-GJR–GARCH
model discussed in Chapter 20. We will assume a GARCH modelling component is
to be developed and will list some important input and output properties that should
be considered in its design.
Inputs
. The conditional probability distribution to use, i.e. Gaussian distribution,
Student’s t distribution, etc.
. The required initial estimates for the model parameters.
. The input data, yi, i ¼ 1, . . . , n, and Xi, i ¼ 1, . . . , n.
. The number of GARCH model parameters, j, j ¼ 0, . . . , q, j ¼ 1, . . . , p, regres-
sion coefficients bj, j ¼ 1, . . . , k, and mean term b0.
. A flag to indicate whether the GARCH stationary constraint is to be enforced.
. A flag to indicate whether the user wants to provide initial estimates for the
regression coefficients bj, j ¼ 1, . . . , k, mean term b0, and pre-observed conditional
variance 2
0, or let the component calculate these.
Outputs
. The estimated GARCH model parameters, ^.
. The value of the minimized log likelihood, L(^).
. The estimated conditional variances, hi, i ¼ 1, . . . , n.
. The estimated residuals, i, i ¼ 1, . . . , n.
. The standard errors associated with each estimated parameter.
. The covariance matrix of the estimated GARCH model parameters ^.
It is also useful to have information concerning the underlying numerical
optimization of the log likelihood, such as the maximum number of iterations
allowed for convergence, and also the tolerance used during the optimization
process.

The software could also provide the scores for each estimated GARCH model
parameter, @L()=@i ¼^. In the absence of constraints all these partial derivatives, at
L(^) should be nearly zero. However, when the stationary constraint is imposed, a
high value for the kth score indicates that the feasible boundary for this parameter
has been reached. This means that it has not been possible to optimize L() any
further through variation of the parameter k.
21.2
TESTING GARCH SOFTWARE
We will now give details concerning the implementation and testing, see Levy (2000),
of regression-GJR–GARCH estimation software, developed using the algorithms
outlined in Chapter 20. The log likelihood was minimized using a general purpose
quasi-Newton type numerical optimizer, see Gill et al. (1981), and Murtagh and
Saunders (1983), which employed either analytic or numeric derivatives (calculated
using finite differences). The optimizer also had the capability of returning a finite-
difference approximation to the Hessian at the solution point, ^, which was used as
the second-derivative estimate of the Fisher information matrix, F. All the results
presented here are based on Monte Carlo simulations involving the generation and
parameter estimation of 200 regression-GJR–GARCH sequences. Each sequence
was created using the NAG routine G05HMF and estimated with the following
optimization settings:
. The maximum number of iterations required for convergence to a solution set
to 100.
. GARCH stationary condition enforced.
. The optimality tolerance set to 108, that is, the optimimal value of the log likeli-
hood has eight figure accuracy.
The simulation results are shown in Tables 21.1 to 21.10. The first column
labelled ‘Estimated Value’ refers to the average parameter estimate using 200
simulations. The second column labelled ‘Estimated Standard Error’ refers to the
average of the standard errors computed by the GARCH software. The third
column labelled ‘Standard Error of Estimates’ refers to the actual standard error
of the parameter estimates. The parameters are output in the order in which they
occur in , i.e.:
. A Gaussian process has  ¼ (!T, b0, bT).
. A Student’s t distribution has  ¼ (!T, 	, b0, bT).
Here !T ¼ (0, 1, . . . , q, 1, . . . , p, 
) and bT ¼ (b1, . . . , bk).
Each table also reports the total CPU time in seconds required to estimate the
model parameters for the 200 GARCH sequences. The tables labelled Numeric
Derivatives refer to results obtained using a finite-difference approximation to both
the gradient and the Hessian. Those labelled Analytic Derivatives refer to results
obtained using the algorithms of Chapter 20 and an approximation to the Fisher
354
Financial Econometrics

information matrix based on the conditional expectation of the Hessian at the
solution point, ^.
21.2.1
Gaussian distribution
In Tables 21.1 to 21.6 we present the results of Monte Carlo simulations to check the
parameter
estimation
software
for
the
following
Gaussian
regression-GJR–
GARCH(1,1) process:
k ¼ 2
0 ¼ 0:01
1 ¼ 0:1
1 ¼ 0:8

 ¼ 0:2
b0 ¼ 1:1
b1 ¼ 1:5
b2 ¼ 2:5
X1
i ¼ 1
100 þ 0:7  sin
i
100


;
X2
i ¼ 1
2 þ
i
1000


;
for
i ¼ 1; . . . ; n
where the value of 1 was taken as realistically high for a financial time series.
The initial values for the regression coefficients, bi, i ¼ 0, . . . , k, and the pre-
observed conditional variance 2
0 were estimated using OLS regression, as outlined
in Section 20.1. The initial estimates for the elements of the parameter vector ! were
all set to 0.1.
Numeric derivatives
Table 21.1
Sequence length 300, CPU time ¼ 111:1 s
Estimated value
Estimated standard error
Standard error of estimates
Correct values
0.0167
0.0155
0.0139
0.01
0.0869
0.0679
0.4217
0.10
0.7911
0.0801
0.3019
0.80
0.2075
0.0975
0.2788
0.20
1.1225
0.3737
1.1738
1.10
1.5211
0.1910
0.6548
1.50
2.4646
0.6003
1.4521
2.50
Table 21.2
Sequence length 1000, CPU time ¼ 380:7 s
Estimated value
Estimated standard error
Standard error of estimates
Correct values
0.0111
0.0037
0.0038
0.01
0.0956
0.0336
0.0304
0.10
0.8001
0.0301
0.0269
0.80
0.2014
0.0531
0.0511
0.20
1.0976
0.0639
0.0623
1.10
1.5008
0.0356
0.0361
1.50
2.5004
0.0613
0.0585
2.50
GARCH software
355

Analytic derivatives
Table 21.3
Sequence length 3000, CPU time ¼ 1246:0 s
Estimated value
Estimated standard error
Standard error of estimates
Correct values
0.0105
0.0020
0.0020
0.01
0.1000
0.0173
0.0174
0.10
0.7982
0.0163
0.0152
0.80
0.2015
0.0290
0.0296
0.20
1.0990
0.0210
0.0240
1.10
1.5000
0.0180
0.0190
1.50
2.5004
0.0096
0.0180
2.50
Table 21.4
Sequence length 300, CPU time ¼ 141:8 s
Estimated value
Estimated standard error
Standard error of estimates
Correct values
0.0167
0.0155
0.0097
0.01
0.0870
0.0677
0.0538
0.10
0.7910
0.0799
0.0559
0.80
0.2074
0.0976
0.0899
0.20
1.1228
0.3734
0.2577
1.10
1.5209
0.1911
0.1627
1.50
2.4639
0.5997
0.3922
2.50
Table 21.5
Sequence length 1000, CPU time ¼ 520:2 s
Estimated value
Estimated standard error
Standard error of estimates
Correct values
0.0111
0.0037
0.0036
0.01
0.0956
0.0336
0.0286
0.10
0.8001
0.0301
0.0260
0.80
0.2014
0.0531
0.0470
0.20
1.0976
0.0639
0.0586
1.10
1.5008
0.0356
0.0339
1.50
2.5004
0.0613
0.0554
2.50
Table 21.6
Sequence length 3000, CPU time ¼ 1597:3 s
Estimated value
Estimated standard error
Standard error of estimates
Correct values
0.0105
0.0020
0.0019
0.01
0.1000
0.0173
0.0165
0.10
0.7982
0.0163
0.0147
0.80
0.2015
0.0290
0.0270
0.20
1.0990
0.0210
0.0225
1.10
1.5000
0.0180
0.0179
1.50
2.5004
0.0096
0.0103
2.50
356
Financial Econometrics

It can be seen that the estimated values are in agreement with the actual values, and
as expected, the standard error of the parameter estimates decreases as the GARCH
sequence length increases.
It is also evident that, for small sample sizes, the use of analytic derivatives leads to
significantly better estimates of the standard errors. As the sequence length is
increased both the numeric and analytic results become very similar. Here the
numeric approach has the advantage of being considerably faster. This is because
finite-difference approximations to the derivatives can be achieved by merely evalu-
ating the log likelihood at several points in the neighbourhood of the current estimate
for the parameter vector . This is in contrast to analytic derivatives, which are
computed recursively using all the terms in the GARCH sequence.
21.2.2
Student’s t distribution
In Tables 21.7 to 21.10 we present the results of Monte Carlo simulations to check
the parameter estimation software for the following Student’s t regression-GJR–
GARCH(1,2) process:
k ¼ 2
0 ¼ 0:08
1 ¼ 0:05
2 ¼ 0:1
1 ¼ 0:4

 ¼ 0:2
	 ¼ 4:2;
b0 ¼ 1:1
b1 ¼ 1:5
b2 ¼ 2:5
X1
i ¼ 1
100 þ 0:7  sin
i
100


;
X2
i ¼ 1
2 þ
i
1000


;
for
i ¼ 1; . . . ; n
The initial values for the regression coefficients, bi, i ¼ 0, . . . , k and the pre-
observed conditional variance 2
0 were estimated using OLS regression, as outlined in
Section 20.1. The initial estimates for all the elements of the parameter vector ! were all
set to 0.1. In addition the initial value for the number of degrees of freedom for the
Student’s t distribution, 	, was taken as 100.0, which effectively assumes a Gaussian
distribution as the starting approximation.
Numeric derivatives
Table 21.7
Sequence length 800, CPU time ¼ 555:2 s
Estimated value
Estimated standard error
Standard error of estimates
Correct values
0.0820
0.0241
0.0354
0.08
0.0921
0.0726
0.1683
0.10
0.1064
0.0716
0.1941
0.10
0.3863
0.1138
0.2033
0.40
0.2176
0.0841
0.1451
0.20
4.4595
0.8290
0.8984
4.20
1.1016
0.0581
0.0726
1.10
1.4973
0.0311
0.0354
1.50
2.4970
0.0619
0.0767
2.50
GARCH software
357

Analytic Derivatives
The characteristics of these tables are similar to those of Section 21.2.1. However,
here nine GARCH model parameters are estimated in contrast to the seven model
parameters in Section 21.2.1. It is also interesting to note the high standard error
associated with the Student’s t distribution parameter 	.
Table 21.8
Sequence length 3000, CPU time ¼ 1933:2 s
Estimated value
Estimated standard error
Standard error of estimates
Correct values
0.0802
0.0124
0.0108
0.08
0.0969
0.0371
0.0328
0.10
0.1007
0.0416
0.0394
0.10
0.3974
0.0645
0.0565
0.40
0.2059
0.0441
0.0404
0.20
4.2642
0.3563
0.3307
4.20
1.0972
0.0176
0.0190
1.10
1.4985
0.0158
0.0152
1.50
2.5011
0.0081
0.0087
2.50
Table 21.9
Sequence length 800, CPU time ¼ 770:9 s
Estimated value
Estimated standard error
Standard error of estimates
Correct values
0.0820
0.0241
0.0257
0.08
0.0922
0.0724
0.1189
0.10
0.1063
0.0716
0.1116
0.10
0.3863
0.1138
0.1376
0.40
0.2176
0.0841
0.1056
0.20
4.4596
0.8289
0.8229
4.20
1.1016
0.0581
0.0634
1.10
1.4973
0.0311
0.0314
1.50
2.4970
0.0619
0.0678
2.50
Table 21.10
Sequence length 3000, CPU time ¼ 2987:6 s
Estimated value
Estimated standard error
Standard error of estimates
Correct values
0.0802
0.0124
0.0123
0.08
0.0969
0.0371
0.0390
0.10
0.1007
0.0416
0.0531
0.10
0.3974
0.0645
0.0706
0.40
0.2059
0.0441
0.0425
0.20
4.2642
0.3563
0.3287
4.20
1.0972
0.0176
0.0189
1.10
1.4985
0.0158
0.0150
1.50
2.5011
0.0081
0.0086
2.50
358
Financial Econometrics

It has been shown that analytic derivatives provide more accurate results than
numeric derivatives for short GARCH sequences. However, numeric derivatives are
considerably faster. This suggests that practical GARCH software should have the
ability to switch from analytic to numeric derivatives when appropriate. The precise
benefits to be gained from using analytic derivatives will depend on the numerical
optimization software used and the accuracy of the finite-difference approximations
to the derivatives.
The results demonstrate that good GARCH model estimates can be obtained even
when the initial parameter estimates are simple, see Section 22.5. This suggests the
construction of easy to use software packages in which initial estimates (for ! and 	)
are not required from the user.
GARCH software
359

Chapter 22
GARCH process identification
In this chapter we consider the practical aspects of GARCH modelling. We deal with the
statistical tests that can be performed on the modelled data in order to identify the best
GARCH process. The results of using a GJR–GARCH model on S&P 500 index data are
presented. Also two GARCH windows demonstrations are discussed which illustrate the
practical use of the mathematics given earlier in this chapter. Each demonstration either
uses a standard linear GARCH model or an AGARCH-I model, and the conditional
probability distribution of the residuals is assumed to be Gaussian. Detailed information
concerning the construction of these applications is provided elsewhere in the book.
22.1
LIKELIHOOD RATIO TEST
A popular approach for testing the significance of parameters estimated using max-
imum likelihood techniques is the likelihood ratio test. It is useful in the following
situation.
Suppose we have modelled data using a GARCH process Np parameters, k,
k ¼ 1, . .. , Np, and have obtained a maximized log likelihood L(^). We now want to
know if by increasing the number of model parameters to Np þ m we can obtain a
significantly better model to the data. If we let the (improved) maximized log likelihood
using the increased number of parameters be L(), then we can use the result that:
2 LðÞ  Lð^Þ
h
i
 2ðmÞ
22.2
SIGNIFICANCE OF THE ESTIMATED PARAMETERS
As described in Section 18.2.1 the significance of an estimated parameter can be
determined by the value of its t statistic. For the ith parameter estimate ^i the t
statistic is ^i=i, where i is the standard error.
It is common practice to reject the null hypothesis of no significance at the 0.5
per cent level, in which case estimates with t statistic values greater than 2.57 are
considered significant.
22.3
THE INDEPENDENCE OF THE STANDARDIZED RESIDUALS
In Section 15.2 we showed that the GARCH(p,q) process:
hi ¼ 0 þ
X
q
j¼1
j2
ij þ
X
p
j¼1
jhij;
i ¼ 1; . . . ; n;
i  Rð0; hiÞ

Gives rise to an ARMA(	, p) process in 2
i of the form:
2
i ¼ 0 þ
X
	
j¼1
ðj þ jÞ2
ij 
X
p
j¼1
j
ij þ 
i
where 	 ¼ max(p, q). If the model is correctly specified then the standardized
sequence Z2
i ¼ 2
i =hi, i ¼ 1, n should constitute white noise. This can be checked by
computing the sample autocorrelations.
The statistical independence of the elements Z2
i can be checked by computing the
values of the sample autocorrelations.
The kth sample autocorrelation is defined as:
rk ¼
X
n
i¼1
Z2
i Z2
ik;
i ¼ k þ 1; . . . ; n
ð22:1Þ
The Box–Pierce Q – statistic is defined as:
Qstat ¼
X
P
k¼1
rk
ð22:2Þ
If the model is correctly specified then Qstat has a 2
2 distribution with P  	  q
degrees of freedom. High values of Qstat lead to reject of the hypothesis that the
standardized residuals are independently distributed.
22.4
THE DISTRIBUTION OF THE STANDARDIZED RESIDUALS
The standardized residuals Zi ¼ i=
ffiffiffiffihi
p , i ¼ 1, . . . , n should have the distribution
R(0, 1).
In the case of R(0, 1) being a Gaussian distribution N(0, 1) we can check for non-
normality in the following manner.
Remembering that the kurtosis is defined as:
@ ¼ E½4
i 
2
and that the skewness is defined as:
S ¼ E½3
i 
3
where E[4
i ] ¼ 1
n
X
n
i¼1
4
i ,
E[3
i ] ¼ 1
n
X
n
i¼1
3
i ,
and
2 ¼ 1
n
X
n
i¼1
2
i
For large samples we have:
S  Nð0; 6=nÞ
and
@  Nð3; 24=nÞ
A test statistic for non-normality of the residuals is given by:
Nstat ¼ n
6 S2 þ n
24 @  3
ð
Þ
ð22:3Þ
GARCH process identification
361

Under the null hypothesis Nstat has a 2
2 distribution, Harvey (1990). In practical
terms this means that if Nstat < 3 then we can reject the alternative hypothesis of non-
normality in favour of normality.
22.5
MODELLING THE S&P 500 INDEX
This section concerns the use of GJR–GARCH to model 3000 daily returns from the
S&P 500 index, for the years 1960–1972; see Levy (2003) for more details.
Analytic derivatives were used in the numerical optimization, and the shocks were
either from a Gaussian distribution or a Student’s t distribution. Tables 22.1 and 22.2
show the maximized log likelihood, LGF(), and parameter estimates for GJR–
GARCH(1,1), AR(1)–GJR–GARCH(1,1), and AR(2)–GJR–GARCH(1,1) models.
The format of these results is
^ (^) [t]
n
o
, where ^ is the vector of estimated model
parameters, ^ is the vector of estimated standard errors, and t is the vector of
significance statistics, t ¼ ^=^. Here we consider parameters with t > 1:96 (i.e. 2.5
per cent probability level) as significant.
It is evident from Table 22.1 that the preferred Gaussian model for the S&P 500
index
data
is
AR(1)–GJR–GARCH(1,1),
with
0 ¼ 0:0196,
1 ¼ 0:0716,
1 ¼ 0:7938,  ¼ 0:1851, c ¼ 0:0267, and 1 ¼ 0:2280:
The results for the Student’s t distribution in Table 22.2 show that the log like-
lihood surface is very flat, and the parameters 1, and 2 are not significant at the
2.5 per cent probability level. Here the preferred model for the S&P 500 index data
is GJR–GARCH(1,1), with 0 ¼ 0:0128, 1 ¼ 0:0545, 1 ¼ 0:8373,
 ¼ 0:1568,

 ¼ 8:1160, and c ¼ 0:0483:
It was found that the optimized parameter estimates did not depend strongly on
the initial estimates. This observation was investigated by studying the shape of the
log likelihood surface for both the Gaussian distribution AR(1)–GJR–GARCH(1,1)
model, and the Student’s t distribution GJR–GARCH(1,1) model. Figures 22.1 and
22.2 show the results for analytic derivatives. Here the value of LGF() is plotted
as each GARCH parameter is individually incremented in steps of 0.04, while all
Table 22.1
Gaussian distribution, estimated model parameters. ^ is the vector of estimated model
parameters, ^ is the vector of estimated standard errors, t ¼ ^=^ is the vector of significance statistics,
and LGFð^Þ is the value of the maximized log likelihood at ^
Parameters
GJR–GARCH(1,1)
LGFð^Þ ¼ 132:716
AR(1)–GJR–GARCH(1,1)
LGFð^Þ ¼ 198:32
AR(2)–GJR–GARCH(1,1)
LGFð^Þ ¼ 134:23

^
^
t
^
^
t
^
^
t
0
0.0189
(0.0028)
[6.78]
0.0196
(0.0028)
[6.83]
0.0184
(0.0027)
[6.71]
1
0.0680
(0.0131)
[5.19]
0.0716
(0.0132)
[5.41]
0.0663
(0.0129)
[5.12]
1
0.8106
(0.0162)
[50.01]
0.7938
(0.0167)
[47.35]
0.8135
(0.0160)
[50.07]

0.1524
(0.0203)
[7.48]
0.1851
(0.0243)
[7.60]
0.1533
(0.0205)
[7.46]
c
0.0458
(0.0087)
[5.23]
0.0267
(0.0085)
[3.11]
0.0420
(0.0089)
[4.72]
1
0.2280
(0.0191)
[11.94]
0.0180
(0.0201)
[0.89]
2
0.0279
(0.0197)
[1.41]
362
Financial Econometrics

Table 22.2
Student’s t distribution, estimated model parameters. ^ is the vector of estimated model
parameters, ^ is the vector of estimated standard errors, t ¼ ^=^ is the vector of significance
statistics, and LGFð^Þ is the value of the maximized log likelihood at ^
Parameters
GJR–GARCH(1,1)
LGFðÞ ¼ 2554:96
AR(1)–GJR–GARCH(1,1)
LGFðÞ ¼ 2554:95
AR(2)–GJR–GARCH(1,1)
LGFðÞ ¼ 2553:17

^
^
t
^
^
t
^
^
t
0
0.0128
(0.0029)
[4.35]
0.0128
(0.0030)
[4.21]
0.0125
(0.0032)
[3.92]
1
0.0545
(0.0149)
[3.65]
0.0544
(0.0153)
[3.55]
0.0521
(0.0147)
[3.54]
1
0.8373
(0.0208)
[40.21]
0.8373
(0.0216)
[38.81]
0.8402
(0.0224)
[37.43]

0.1568
(0.0236)
[6.64]
0.1570
(0.0236)
[6.65]
0.1573
(0.0705)
[2.23]

8.1160
(1.0360)
[7.83]
8.1260
(1.0910)
[7.44]
8.1080
(3.0980)
[2.61]
c
0.0483
(0.0092)
[5.27]
0.0481
(0.0095)
[5.04]
0.0451
(0.0264)
[1.71]
1
0.0021
(0.0194)
[0.11]
0.0010
(0.1001)
[0.01]
2
0.0351
(0.1191)
[0.29]
1000
–1000
–1500
–2000
–2500
500
0
–500
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
Log likelihood
Parameter value
LF(α0)
LF(α1)
LF(β1)
LF(γ)
LF(c)
LF(φ1)
Figure 22.1
The partial log likelihood surface for the Gaussian AR(1)–GJR–GARCH(1,1) model
presented in Table 22.1. In order to display the results on a single graph symbols have been used which
incorporate various scale factors. The symbol definitions are as follows: LF(0) ¼ LGF(0j^),
LF(1) ¼ 0:5  LGF(1j^), LF(1) ¼ 0:2  LGF(1j^), LF() ¼ 3  LGF(j^), LF(c) ¼ LGF(cj^),
LF(1) ¼ 4  LGF(1j^). The parameter values range from 0 to 0.76, with an increment of 0.04
GARCH process identification
363

the other GARCH parameters are held fixed at the values which maximize the log
likelihood function. For the kth GARCH model parameter, k, we will denote this
partial log likelihood function by LGF(kj^). Inspection of Figures 22.1 and 22.2
shows that, to within the step tolerance, the location of the partial log likelihood
maxima are in agreement with the parameter estimates given in Tables 22.1 and 22.2.
It can also be seen that the partial log likelihood surface is both smooth and convex.
This explains why a Newton-type numerical optimizer can converge to a global
maximum even when poor initial estimates are supplied.
22.6
EXCEL DEMONSTRATION
This demonstration is concerned with modelling currency exchange rate returns data.
It illustrates how to identify the best GARCH model to suit a particular time series,
and is composed of the following components:
. Two ActiveX plot controls, to display the orginal data and also the modelled
standardized residuals Zi ¼ i=
ffiffiffiffihi
p , i ¼ 1, . . . , n.
. Microsoft TextBox controls to allow the user to select the order of the GARCH model.
–2.5
–2
–1.5
–1
–0.5
0
0.5
1× 104
0.1
0.2
0.3
0.4
0.5
0.6
0.7
Parameter value  
Log likelihood
LF(α0)
LF(α1)
LF(β1)
LF(γ)
LF(ν+)
LF(c)
Figure 22.2
The partial log likelihood surface for the Student’s t GJR–GARCH(1,1) model
presented in Table 22.2. In order to display the results on a single graph symbols have been used which
incorporate various scale factors and offsets. The symbol definitions are as follows:
LF(0) ¼ 4[4000þLGF(0j^)], LF(1) ¼ 4[4000þLGF(1j^)], LF(1) ¼ 4000þ LGF(1j^),
LFðÞ ¼ 6[4000þLGF( j^)], LF(c) ¼ 3[4000þLGF(cj^)], LF(
þ) ¼ 100 [2500þLGF(
j^)], where

 ¼ 25
þ þ2. The parameter values range from 0.04 to 0.76, with an increment of 0.04. This gives values of

 which range from 3 to 21, and (for example) a parameter value of 
þ ¼ 0:4 corresponds to 
 ¼ 12
364
Financial Econometrics

. Microsoft Radio controls to allow the user to select the type of GARCH model.
. Microsoft Button controls to perform actions such as: Clear, Calculate, and Show
Data.
. A Microsoft Grid control to display the modelled values and parameter estimates.
It can be seen that the user has the choice of selecting either an AGARCH-I or an
AGARCH-II model, and there is also an asymmetry option. It should be noted that
when AGARCH-I is used without asymmetry this is equivalent to the standard linear
GARCH model. All the results presented here are for an AGARCH-I model either
with or without asymmetry.
We found the Microsoft Grid control to be a very versatile means of showing informa-
tion. In this example it was used to display the following results:
. The initial parameter estimates. Although they were all automatically set to 0.1,
they could if required be edited to different values.
. The computed parameter estimates, ^k, k ¼ 1, . . . , Np.
. The standard errors, k, k ¼ 1, . . . , Np.
. The significance statistics for the estimated parameters, T k ¼ ^k=k, k ¼ 1, . . . , Np.
. The value of the log likelihood for the estimated parameter values, L(^).
. The partial derivatives (also termed scores) @L()=@k, k ¼ 1, . . . , Np for the
estimated parameters.
. The normality test statistic Nstat described in Section 22.4.
The top graph in Figures 22.3 to 22.7 plots the exchange rate returns data, and is
identical in each figure. It can be seen that the data clearly exhibits volatility clustering.
The bottom graph in Figures 22.3 to 22.7 plots the standardized residuals
Zi ¼ i=
ffiffiffiffihi
p , i ¼ 1, . .. , n. If the data has been modelled well then these values should
have the distribution NID(0,1). This means that the closer the lower graph corresponds
to white noise the better the GARCH model. Of course it may be difficult to perform this
appraisal visually, so that is why we also report the normality test statistic. We could also
look at the autocorrelation structure, but we have not done that here.
Figure 22.3 shows the results of using a simple GARCH(0,1), that is ARCH(1),
on the data. The log likelihood is 4122.57 and the normality test statistic, Nstat, is
1499.48. This value of Nstat is very large, and we can clearly see clustering in the
lower graph. In Figures 22.4 and 22.5 we experiment with using high order ARCH
models to describe the data.
Figure 22.4 shows the results of using a GARCH(0,10). Here the log likelihood is
4337.0 and the normality test statistic, Nstat is 2.922. It can be seen that only the
parameters 0, 1, 2, and 5 have t statistic values above 3.0. This model is certainly
better than the simple GARCH(0,1) model since the log likelihood is higher and also
Nstat is considerably lower.
Figure 22.5 shows the results of using an AGARCH-I(0,10). The inclusion of
asymmetry has improved on the GARCH(0,10) model, since the log likelihood has
now increased to 4353.97 and Nstat has reduced to 1.562. It can be seen that the
parameters 0, 1, 2, 4, 5, and the asymmetry parameter  have t statistic values
above 3.
GARCH process identification
365


## Credit Derivatives and Risk

Figure 22.3
Modelling the data with GARCH(0,1)
Figure 22.4
Modelling the data with GARCH(0, 2)
366
Financial Econometrics

Figure 22.5
Modelling the data with GARCH(0,10)
Figure 22.6
Modelling the data with GARCH(1,1)
GARCH process identification
367

In Figures 22.6 and 22.7 we see if a GARCH(1,1) models will do better than the
ARCH(10) models.
Figure 22.6 shows the results of using a GARCH(1,1). Here the likelihood is
4340.95 and the normality test statistic, Nstat is 12.39. All the parameters have
t statistic values above 3, and the value 1 is 56.922. However, these results are not
as good those we obtained from the AGARCH-I(0,10) model.
Figure 22.7 shows the results of using an AGARCH-I(1,1). Here the likelihood is
4357.67 and the normality test statistic, Nstat is 0.575. All the parameters have
t statistic values above 3, and the value 1 is 59.886. Clearly this is the preferred
model is an AGARCH-I(1,1) model with:
0 ¼ 5:55  105;
1 ¼ 0:128;
1 ¼ 0:852;
 ¼ 0:0175
It is interesting to note that the asymmetry parameter  is positive. This is
because we are modelling currency exchange rate returns data and (since it is not
clear that negative exchange rate returns indicate bad news) there is no preference
in the sign of the asymmetry. However, if we were modelling stock market returns
data we would expect  to be negative.
22.7
INTERNET EXPLORER DEMONSTRATION
This demonstration illustrates how GARCH modelling could be carried out with a
Web Browser on an Internet Web page.
Figure 22.7
Modelling the data with AGARCH(1,1)
368
Financial Econometrics

It shows how ActiveX components on a Web page can be used to model the
volatility of the share price for a particular company. This Web page contains the
following ActiveX components:
. Three Microsoft ActiveX button controls
. Two ActiveX graphical controls, called Plot1 and Plot2
. The GARCH modelling ActiveX control, GARCH1.
All the data input and computation is performed by the aggregated ActiveX
component GARCH1. This control was created using Visual Basic and uses textboxes
to input the model parameters and company name. It also extracts company share
returns from a Microsoft Access database and models this data by calling computa-
tional GARCH routines contained within a Visual Cþþ DLL.
Figures 22.8 to 22.10 show how this demonstration is used. Appropriate values of
p, q and the company name are entered into the textboxes of GARCH1. The data
corresponding to the selected company (in this case it is merely called ASSET ) is
displayed on the lower plot region by clicking the button labelled ‘Show Data’.
This runs the subroutine Show_Data_ Click() which calls the EXTRACT_DATA
property of GARCH1 to retrieve data from the Access database and then display it
using the ActiveX component Plot2. When the button labelled ‘Calculate’ is
clicked Calculate_GARCH_Click() is run and a GARCH(p,q) process used to
model the data. If the user wishes to try alternative value of p and q, then clicking the
‘Clear’ button deletes the previous results and the data can be remodelled.
Figure 22.8
The original data displayed on the Web page
GARCH process identification
369

Figure 22.9
Modelling the data with ARCH(1)
Figure 22.10
Modelling the data with ARCH(4)
370
Financial Econometrics

Chapter 23
Multivariate time series
So far we have been concerned with modelling the volatility of single assets. However,
most practical financial applications consist of portfolios containing many assets,
and it is therefore necessary to model multivariate time series and their associated
time varying covariance matrices.
One of the main problems connected with doing this is the number of parameters
that may require estimating. For instance a typical portfolio consisting of 100 assets
has a 100  100 covariance matrix which is described by 5050 terms. One way round
this problem is to use principal component analysis to reduce the number of para-
meters which describe the multivariate process.
23.1
PRINCIPAL COMPONENT GARCH
Principal component or orthogonal GARCH provides a parsimonious way in which
to model multivariate time series, see Ding (1994) and Alexander (2000).
Consider T observations of m variables and let these be represented by the T  m
matrix Y, so that the ith column of Y, Yi, contains the T observations of the ith
variable. We will also denote the row vector containing the values of the m variables
at instant t by Yt. If the unconditional mean of the Yi is i then we can construct the
matrix X, where the ith column of X is Xi ¼ Yi  i, and the m  m covariance
matrix, C, of the data matrix Y is given by:
C ¼ XTX
ð23:1Þ
Since the covariance matrix is symmetric and positive definite we can obtain the
following spectral decomposition
C ¼ W WT
ð23:2Þ
where the columns of the m  m matrix W contain the eigenvectors of C and the
elements of the m  m diagonal matrix  contain the corresponding eigenvalues,
i, i ¼ 1, . . . , m.
If k of the eigenvalues are much greater than the other m  k eigenvalues, then a
good approximation to the covariance matrix is:
C  WkkWk
T

where k is the k  k diagonal matrix containing the kth largest eigenvalues, and Wk
is the m  k matrix of eigenvectors formed using the appropriate k columns of W.
The time-dependent scores, Si
t, t ¼ 1, . . . , T, corresponding to the ith eigenvector
(principal component) are calculated as:
Si
t ¼ XtWi;
t ¼ 1; . . . ; T
where Si
t is the (T  1) score vector at time instant t corresponding to the ith
eigenvalue, Xt is the the row of the (T  m) matrix X in Equation 23.1 corresponding
to time t, and Wi is the corresponding (m  1) eigenvector.
In matrix notation, if the k largest eigenvalues are used, then we obtain the
following scores matrix:
S ¼ XWk
ð23:3Þ
where S is now a T  k matrix, X is a T  m matrix, and Wk is a m  k matrix.
All the columns of S (that is the score vector corresponding to each principal
component) are orthogonal, and so STS results in the diagonal matrix . This can
easily be shown as follows:
STS ¼ ðXWÞTXW
¼ WTðXTXÞW
¼ WTCW
¼ 
ð23:4Þ
The variance of the score vector for the ith principal component is thus equal to the
ith eigenvalue, i. That is:
E½SiTSi ¼
X
T
t¼1
Si
tSi
t ¼ i;
i ¼ 1; . . . ; k
The instantaneous covariance matrix at time t, Vt, can thus be approximated as
follows:
Vt ¼ Xt
TXt
where Xt is the row of matrix X corresponding to time t.
From Equation 23.3 we have S ¼ XW and therefore:
SWT ¼ XWWT ¼ X;
since
WWT ¼ I
Thus X ¼ SWT and XTX ¼ WSTSWT.
Since STS is diagonal we can write Vt as:
Vt ¼ WtWT;
t ¼ 1; . . . ; T
ð23:5Þ
where each time dependent variance, i
t, i ¼ 1, . . . , k, in the diagonal matrix t is
modelled using a univariate GARCH process. Note: The eigenvectors W are assumed
to be time independent.
372
Financial Econometrics

For example, suppose we want to model the time dependent covariance matrix of
three exchange rate return series ri
j, i ¼ 1, . . . , 3, j ¼ 1, . . . , T, then we would employ
the steps explained below.
Construct the covariance matrix, C
The value of the element in the ith row and jth column of matrix C is:
Ci; j ¼
X
T
k¼1
ðri
k  riÞðr j
k  r jÞ;
i ¼ 1; . . . ; 3;
j ¼ 1; . . . ; 3
where ri is the mean value of the ith return series,
Form the eigenvalue decomposition
From Equation 23.2 we have:
C ¼ WWT
where the ith eigenvector is the column vector Wi ¼ (Wi
1,Wi
2,Wi
3)T. We will assume
that 1 	 2, and 1 >> 3, so k ¼ 2.
Use the eigenvectors to form the scores
From Equation 23.1 the scores are given by S ¼ XWk, where k ¼ 2
The scores for the first principal component are:
S1
1 ¼ X1
1W1
1 þ X 2
2W1
2 þ X3
1W1
3
S1
2 ¼ X1
2W1
1 þ X2
2W1
2 þ X3
2W1
3
S1
3 ¼ X1
3W1
1 þ X2
3W1
2 þ X3
3W1
3
:
:
:
:
:
:
S1
T ¼ X1
TW1
1 þ X2
TW 1
2 þ X3
TW1
3
The scores for the second principal component are:
S2
1 ¼ X2
1W2
1 þ X2
2W2
2 þ X3
1W2
3
S2
2 ¼ X1
2W2
1 þ X2
2W2
2 þ X3
2W2
3
S2
3 ¼ X1
3W2
1 þ X2
3W2
2 þ X3
3W2
3
:
:
:
:
:
:
S2
T ¼ X1
TW2
1 þ X2
TW2
2 þ X3
TW2
3
Multivariate time series
373

Model the univariate scores using GARCH
Use an appropriate univariate GARCH process to model the variance of the scores,
hi
t ¼ (Si
t)2 ¼ i
t, i ¼ 1, . . . , k, t ¼ 1, . . . , T for each sequence Si
t, t ¼ 1, . . . , T, where
i  k. So, using k ¼ 2 and assuming a basic GARCH(p,q) process, then the two
diagonal elements (1
t and 2
t ) of t are modelled as follows:
The GARCH(p1,q1) process for the first principal component score vector is:
1
t ¼ ðS1
t Þ2 ¼ h1
t ¼ 1
0 þ
X
q1
j¼1
1
j 2
tj þ
X
p1
j¼1
1
j htj;
t ¼ 1; . . . ; T
and the GARCH(p2,q2) process for the second principal component score vector is:
2
t ¼ ðS2
t Þ2 ¼ h2
t ¼ 2
0 þ
X
q2
j¼1
2
j 2
tj þ
X
p2
j¼1
1
j htj;
t ¼ 1; . . . ; T
Compute the time dependent covariance matrix
From Equation 23.5 we use:
Vt ¼ WtWT;
t ¼ 1; . . . ; T
For this example it is easy to perform the matrix multiplications as follows:
Vt ¼
V11
V12
V13
V21
V22
V23
V31
V32
V33
0
B
@
1
C
A ¼
W1
1
W2
1
W1
2
W2
2
W1
3
W2
3
0
B
@
1
C
A
h1
t
0
0
h2
t
 
!
W1
1
W1
2
W1
3
W2
1
W2
2
W2
3
 
!
¼
W1
1
W2
1
W1
2
W2
2
W1
3
W2
3
0
B
@
1
C
A
h1
t W1
1
h1
t W1
2
h1
t W1
3
h2
t W2
1
h2
t W2
2
h2
t W2
3
 
!
This yields the orthogonal GARCH estimate of the time dependent covariance
matrix as:
Vt ¼
h1
t W1
1W1
1 þ h2
t W2
1W2
1
h1
t W1
1W1
2 þ h2
t W2
1W2
2
h1
t W1
1W1
3 þ h2
t W2
1W2
3
h2
t W1
2W1
1 þ h2
t W1
2W1
2
h1
t W1
2W1
2 þ h2
t W2
2W2
2
h1
t W1
2W1
3 þ h2
t W2
2W2
3
h1
t W1
3W1
1 þ h2
t W2
3W2
1
h1
t W1
3W1
2 þ h2
t W2
3W2
2
h1
t W1
3W1
3 þ h2
t W2
3W3
3
0
B
B
@
1
C
C
A
More details concerning orthogonal GARCH models can be found in Van der Weide
(2002).
374
Financial Econometrics

APPENDICES


Appendix A
Computer code for Part I
This Appendix contains complete code for the examples referenced in the main text.
A.1
THE ODL FILE FOR THE DERIVATIVE PRICING CONTROL
The complete ODL file for the derivative pricing control used in Section 3.3 and
Chapter 4 is given below.
// NAGDBS.odl : type library source for ActiveX Control project.
// This file will be processed by the Make Type Library (mktyplib) tool to
// produce the type library (NAGDBS.tlb) that will become a resource in
// NAGDBS.ocx.
#include <olectl.h>
#include <idispids.h>
[uuid(8B7F2A94—E828—11D2—AD08—0060087ED9F1),version(1.0),
helpfile(‘‘NAGDBS.hlp’’),
helpstring(‘‘NAGDBS ActiveX Control module’’),
control ]
library NAGDBSLib
{
importlib(STDOLE_TLB);
importlib(STDTYPE_TLB);
typedef enum
{
[helpstring(‘‘Call’’)] Call ¼ 0,
[helpstring(‘‘Put’’)] Put ¼ 1
}
PUTCALLTYPE;
typedef enum
{
[helpstring(‘‘European’’)] European ¼ 0,
[helpstring(‘‘American’’)] American ¼ 1,
[helpstring(‘‘Cntrl_American’’)] Cntrl_American ¼ 2
}
EXTYPE;
typedef enum
{
[helpstring(‘‘Lattice u ¼ 1/d’’)] Lattice_standard ¼ 0,
[helpstring(‘‘Lattice p ¼ 1/2’’)] Lattice_prob_half ¼ 1,
[helpstring(‘‘Analytic’’)] Analytic ¼ 2
}
METHODTYPE;
// Primary dispatch interface for CNAGDBSCtrl
[uuid(8B7F2A95—E828—11D2—AD08—0060087ED9F1),
helpstring(‘‘Dispatch interface for NAGDBS Control’’), hidden ]
dispinterface_DNAGDBS
{
properties:
// NOTE — ClassWizard will maintain property
// information here.
// Use extreme caution when editing this section.
//{{AFX_ODL_PROP(CNAGDBSCtrl)
[id(1)] METHODTYPE method;
[id(2)] EXTYPE extype;
[id(3)] double sigma;
[id(4)] long numsteps;

[id(5)] double intrate;
[id(6)] double dividends;
[id(7)] double curval;
[id(8)] double optval;
[id(9)] double strike;
[id(10)] PUTCALLTYPE putcall;
[id(11)] double maturity;
[id(DISPID_CAPTION), bindable, requestedit] BSTR Caption;
[id(DISPID_BACKCOLOR), bindable, requestedit] OLE_COLOR BackColor;
[id(DISPID_FORECOLOR), bindable, requestedit] OLE_COLOR ForeColor;
//}}AFX_ODL_PROP
methods:
// NOTE — ClassWizard will maintain method information here.
// Use extreme caution when editing this section.
//{{AFX_ODL_METHOD(CNAGDBSCtrl)
[id(12)] void Calculate();
[id(13)] void greeks(double* greekvals);
//}}AFX_ODL_METHOD
[id(DISPID_ABOUTBOX)] void AboutBox();
};
// Event dispatch interface for CNAGDBSCtrl
[ uuid(8B7F2A96—E828—11D2—AD08—0060087ED9F1),
helpstring(‘‘Event interface for NAGDBS Control’’) ]
dispinterface_DNAGDBSEvents
{
properties:
// Event interface has no properties
methods:
// NOTE — ClassWizard will maintain event information here.
// Use extreme caution when editing this section.
//{{AFX_ODL_EVENT(CNAGDBSCtrl)
[id(DISPID_CLICK)] void Click();
[id(DISPID_MOUSEMOVE)] void MouseMove(short Button, short Shift,
OLE_XPOS_PIXELS x, OLE_YPOS_PIXELS y);
//}}AFX_ODL_EVENT
};
// Class information for CNAGDBSCtrl
[ uuid(8B7F2A97—E828—11D2—AD08—0060087ED9F1),
helpstring(‘‘NAGDBS Control’’), control ]
coclass NAGDBS
{
[default] dispinterface_DNAGDBS;
[default,source] dispinterface_DNAGDBSEvents;
};
//{{AFX_APPEND_ODL}}
//}}AFX_APPEND_ODL}}
};
378
Appendix A

Appendix B
Some more option pricing formulae
In this section we list some more derivative pricing formula; use is made of the
following symbols:
d1 ¼ logðS=EÞ þ ðr  q þ 2=2Þ

ffiffiffi
p
ðB:1Þ
d2 ¼ logðS=EÞ þ ðr  q  2=2Þ

ffiffiffi
p
¼ d1  
ffiffiffi
p
ðB:2Þ
B.1
BINARY OPTIONS
A binary cash or nothing call option pays nothing if the stock price ends up below the
the strike and an amount Q if it ends up above the strike price. The value is:
Vc ¼ Q expðrÞN1ðd2Þ
ðB:3Þ
A binary asset or nothing call option pays nothing if the stock price ends up
below the strike and the stock price itself if it ends up above the strike price. The
value is:
Vc ¼ S expðrÞN1ðd1Þ
ðB:4Þ
B.2
OPTION TO EXCHANGE ONE ASSET FOR ANOTHER
V ¼ S2 expðq2ÞN1ðd1Þ  S1 expðq1ÞN1ðd2Þ
ðB:5Þ
where
d1 ¼ logðS2=S1Þ þ ðq1  q2 þ 2=2Þ

ffiffiffi
p
d2 ¼ d1  
ffiffiffi
p
and
 ¼
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
2
1 þ 2
2  212
q
It is interesting to note that this formula is independent of the interest rate r.

B.3
LOOKBACK OPTIONS
The value of a European lookback call at time zero is:
Vc ¼ S expðqÞ N1ða1Þ 
2
2ðr  qÞ N1ða1Þ


 Smin expðrÞ N1ða2Þ 
2
2ðr  qÞ expðY1ÞN1ða3Þ


ðB:6Þ
where
a1 ¼ logðS=SminÞ þ ðr  q þ 2=2Þ

ffiffiffi
p
;
a2 ¼ a1  
ffiffiffi
p
a3 ¼ logðS=SminÞ þ ðr þ q þ 2=2Þ

ffiffiffi
p
;
Y1 ¼  logðS=SminÞ2ðr  q  2=2Þ
2
and Smin is the minimum stock price achieved to date. If the lookback option has just
been originated then Smin ¼ S and the valuation simplifies to:
Vc ¼ S expðqÞ N1ðg1Þ  WN1ðg1Þ
f
g  S expðrÞfN1ðg2Þ  WN1ðg2Þg
ðB:7Þ
where
W ¼
2
2ðr  qÞ ;
g1 ¼ ðr  q þ 2=2Þ

ffiffiffi
p
;
g2 ¼ g1  
ffiffiffi
p
The value of a European lookback put is:
Vp ¼ S expðqÞ N1ðb2Þ þ
2
2ðr  qÞ N1ðb2Þ


þ Smax expðrÞ N1ðb1Þ 
2
2ðr  qÞ expðY2ÞN1ðb3Þ


ðB:8Þ
where
b1 ¼ logðSmax=SÞ þ ðr þ q þ 2=2Þ

ffiffiffi
p
;
b2 ¼ b1  
ffiffiffi
p
b3 ¼ logðSmax=SÞ þ ðr  q  2=2Þ

ffiffiffi
p
;
Y2 ¼  logðSmax=SÞ2ðr  q  2=2Þ
2
and Smax is the maximum stock price achieved to date. If the lookback option has just
been originated then Smax ¼ S and the valuation simplifies to:
Vp ¼ S expðqÞfN1ðb2Þ þ WN1ðb2Þg þ S expðrÞfN1ðb1Þ WN1ðb1Þg
ðB:9Þ
where
W ¼
2
2ðr  qÞ ;
b1 ¼ ðr þ q þ 2=2Þ

ffiffiffi
p
;
b2 ¼ b1  
ffiffiffi
p
380
Appendix B

Appendix C
Derivation of the Greeks for vanilla
European options
C.1
INTRODUCTION
In this section we will present some useful results which will be used later on to derive
expressions for the Greeks.
A fundamental result of calculus is that:
@
@x
Z
f ðxÞdx ¼ f ðxÞ
ðC:1Þ
Also the indefinite integral,
R
f ðxÞdx, can be expressed as a definite integral with
variable upper bound as follows:
Z
f ðxÞdx ¼
Z x
a
f ðxÞdx þ c
so
@
@x
Z x
a
f ðxÞdx ¼ f ðxÞ
ðC:2Þ
We can now use this result to obtain the derivative of the cumulative distribution
function:
N1ðxÞ ¼
1ffiffiffiffiffi
2
p
Z x
1
expðx2=2Þdx
which gives
@N1ðxÞ
@x
¼ nðxÞ
ðC:3Þ
where
nðxÞ ¼
1ffiffiffiffiffi
2
p
expðx2=2Þ
We now derive various results for the parameters d1 and d2 which appear in the
Black–Scholes equation, see Part I Section 2.3.3.
d1 ¼ logðS=EÞ þ ðr  q þ 2=2ÞðT  tÞ

ffiffiffiffiffiffiffiffiffiffiffi
T  t
p
ðC:4Þ

and
d2 ¼ logðS=EÞ þ ðr  q  2=2ÞðT  tÞ

ffiffiffiffiffiffiffiffiffiffiffi
T  t
p
¼ d1  
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
ðT  tÞ
p
ðC:5Þ
We have:
@d2
@S ¼ @d1
@S ¼
1
S
ffiffiffiffiffiffiffiffiffiffiffi
T  t
p
ðC:6Þ
@d2
@ ¼ @d1
@ 
ffiffiffiffiffiffiffiffiffiffiffi
T  t
p
ðC:7Þ
@d1
@r ¼ @d2
@r ¼
ffiffiffiffiffiffiffiffiffiffiffi
T  t
p

ðC:8Þ
@d2
@t ¼ @d1
@t þ

2ðT  tÞ
ðC:9Þ
Also:
nðd2Þ ¼
1ffiffiffiffiffi
2
p
expðd2
2=2Þ
¼
1ffiffiffiffiffi
2
p
expðd2
1=2Þ exp d1
ffiffiffiffiffiffiffiffiffiffiffi
T  t
p
 2ðT  tÞ=2Þ
n
o
¼ nðd1Þ exp logðS=EÞ þ ðr  q þ 2=2ÞðT  tÞ  2ðT  tÞ=2


so
nðd2Þ ¼ S
E nðd1Þ expðrðT  tÞÞ expðqðT  tÞÞ
ðC:10Þ
C.2
GAMMA
Gamma is defined as the second derivative of the option value with respect to the
underlying stock price. This means, see Section C.3, it is the rate of change of Delta
with the underlying stock price.
For a European call the value of Gamma is:
c ¼ @2c
@S2 ¼ @c
@S ¼ @
@S N1ðd1Þ expðqðT  tÞÞ
f
g
where the value of c, is given in Section C.3. So
c ¼ expðqðT  tÞÞ @N1ðd1Þ
@S
¼ expðqðT  tÞÞnðd1Þ @d1
@S
Therefore:
c ¼
nðd1Þ
S
ffiffiffiffiffiffiffiffiffiffiffi
T  t
p
expðqðT  tÞ
ðC:11Þ
The value of Gamma for a European put can be calculated similarly:
p ¼ @2p
@S2 ¼ @p
@S ¼ @
@S fðN1ðd1Þ  1Þ expðqðT  tÞÞg
382
Appendix C

where we have used the value of p, derived in Section C.3. Therefore:
p ¼ expðqðT  tÞÞ @ðN1ðd1Þ  1Þ
@S
¼ expðqðT  tÞÞnðd1Þ @d1
@S
So
p ¼ c ¼
nðd1Þ
S
ffiffiffiffiffiffiffiffiffiffiffi
T  t
p
expðqðT  tÞÞ
ðC:12Þ
So the value of Gamma for both a put and a call is the same.
C.3
DELTA
Delta is defined as the rate of change of option value with the underlying stock price.
For a European call we have:
c ¼ @c
@S ¼ @
@S fS expðqðT  tÞÞN1ðd1Þ  E expðrðT  tÞÞN1ðd2Þg
So
c ¼ expðqðT  tÞÞ N1ðd1Þ þ Snðd1Þ @d1
@S
	

 E expðrðT  tÞÞnðd2Þ @d2
@S
ðC:13Þ
Substituting for nðd2Þ, and @d2=@S we obtain:
c ¼ expðqðT  tÞÞN1ðd1Þ
ðC:14Þ
In similar manner we have for a European put:
p ¼ @p
@S ¼ @
@S fE expðrðT  tÞÞð1  N1ðd2ÞÞ S expðqðT  tÞÞð1  N1ðd1ÞÞg
So
p ¼  E expðrðT  tÞÞnðd2Þ @d2
@S
 expðqðT  tÞÞ ð1  N1ðd1ÞÞ þ Snðd1Þ @d1
@S
	

ðC:15Þ
substituting for nðd2Þ, and @d2=@S we obtain:
p ¼ expðqðT  tÞÞfN1ðd1Þ  1g
ðC:16Þ
C.4
THETA
Theta is defined as the rate of change of the option value with time.
For a European call option we have:
c ¼ @c
@t ¼ @
@t S expðqðT  tÞÞN1ðd1Þ  E expðrðT  tÞÞN1ðd2Þ
f
g
¼ q expðqðT  tÞÞSN1ðd1Þ þ expðqðT  tÞÞSnðd1Þ @d1
@t
 rE expðrðT  tÞÞN1ðd2Þ  E expðrðT  tÞÞnðd2Þ @d2
@t
Appendix C
383

substituting for nðd2Þ and @d2=@t we obtain:
c ¼q expðqðT  tÞÞSN1ðd1Þ  rE expðrðT  tÞÞN1ðd2Þ
þ expðqðT  tÞÞSnðd1Þ@d1
@t  E expðrðT  tÞÞnðd1Þ

 S
E expðrðT  tÞÞexpðqðT  tÞÞ @d1
@t þ

2ðT  tÞ
	

¼q expðqðT  tÞÞSN1ðd1Þ  rE expðrðT  tÞÞN1ðd2Þ Snðd1Þ expðqðT  tÞÞ
2
ffiffiffiffiffiffiffiffiffiffiffi
T  t
p
Therefore the value of theta is:
c ¼ expðqðT  tÞÞ q  SN1ðd1Þ Snðd1Þ
2
ffiffiffiffiffiffiffiffiffiffiffi
T  t
p
	

 rE expðrðT  tÞÞN1ðd2Þ
ðC:17Þ
For a put we can similarly show that
p ¼ @p
@t ¼ @
@t E expðrðT  tÞÞð1  N1ðd2ÞÞ
f
 S expðqðT  tÞÞð1  N1ðd1ÞÞg
p ¼ rE expðrðT  tÞÞð1  N1ðd2ÞÞ  E expðrðT  tÞnðd2Þ @d2
@t
 qS expðqðT  tÞÞð1  N1ðd1ÞÞ þ S expðqðT  tÞnðd1Þ @d1
@t
substituting for nðd2Þ and @d2=@t we obtain:
p ¼ rE expðrðT  tÞÞN1ðd2Þ  qS expðqðT  tÞÞN1ðd1Þ
 E expðrðT  tÞÞ expðrðT  tÞÞ expðqðT  tÞÞ

 nðd1Þ S
E
@d1
@t þ
@
2ðT  tÞ
	

þ S expðqðT  tÞÞnðd1Þ @d1
@t
So we have:
p ¼  expðqðT  tÞÞ qSN1ðd1Þ þ Snðd1Þ
2
ffiffiffiffiffiffiffiffiffiffiffi
T  t
p
	

þ rE expðrðT  tÞÞN1ðd2Þ
ðC:18Þ
C.5
RHO
Rho is the rate of change of the option value with interest rate.
For a call we have:
c ¼ @c
@r ¼ @
@r S expðqðT  tÞÞN1ðd1Þ  E expðrðT  tÞÞN1ðd2Þ
f
g
¼ S expðqðT  tÞÞnðd1Þ @d1
@r þ EðT  tÞN1ðd2Þ  E expðrðT  tÞÞnðd2Þ @d2
@r
substituting for nðd2Þ and @d2=@r we obtain:
c ¼ EðT  tÞN1ðd2Þ
ðC:19Þ
384
Appendix C

For a European put we have:
p ¼ @p
@r ¼ @
@r E expðrðT  tÞÞð1  N1ðd2ÞÞ
f
 S expðqðT  tÞÞð1  N1ðd2ÞÞg
¼  EðT  tÞð1  N1ðd2ÞÞ  E expðrðT  tÞÞnðd2Þ @d2
@r
þ S expðqðT  tÞÞnðd1Þ @d1
@r
¼  EðT  tÞN1ðd2Þ  E expðrðT  tÞÞnðd2Þ @d2
@r
þ S expðqðT  tÞÞnðd1Þ @d1
@r
substituting for nðd2Þ and @d2=@r we obtain:
p ¼  EðT  tÞN1ðd2Þ
ðC:20Þ
C.6
VEGA
Vega is the rate of change of option value with volatility. For a call we have:
Vc ¼ @c
@
¼ @
@ S expðqðT  tÞÞN1ðd1Þ  E expðrðT  tÞÞN1ðd2Þ
f
g
¼ S expðqðT  tÞÞnðd1Þ @d1
@  E expðrðT  tÞÞnðd2Þ @d2
@r
ðC:21Þ
substituting for nðd2Þ and @d2=@ we obtain:
Vc ¼ S expðqðT  tÞÞnðd1Þ @d1
@  Snðd1Þ expðqðT  tÞÞ @d1
@ 
ffiffiffiffiffiffiffiffiffiffiffi
T  t
p
	

Therefore
Vc ¼ S expðqðT  tÞÞnðd1Þ
ffiffiffiffiffiffiffiffiffiffiffi
T  t
p
ðC:22Þ
For a European put we have:
Vp ¼ @c
@
¼ @
@ E expðrðT  tÞÞð1  N1ðd2ÞÞ  S expðqðT  tÞÞð1  N1ðd1ÞÞ
f
g
¼  E expðrðT  tÞÞnðd2Þ @d2
@ þ S expðqðT  tÞÞnðd1Þ @d1
@
ðC:23Þ
substituting for nðd2Þ and @d2=@ we obtain:
Vp ¼ S expðqðT  tÞÞnðd1Þ
ffiffiffiffiffiffiffiffiffiffiffi
T  t
p
ðC:24Þ
which is the same as for a call.
Appendix C
385

Appendix D
Multiasset binomial lattices
D.1
TRUNCATED TWO ASSET BINOMIAL LATTICE
void truncated_2D_binomial(double *value, double tol, double S1, double S2,
double X, double sigma1, double sigma2, double rho, double T, double r, double q1,
double q2, Integer put, Integer M, Integer opt_type, Integer is_american, Integer *iflag)
{
/* Input parameters:
tol
—
the parameter which controls when lattice truncation occurs
S1
—
the current price of the underlying asset 1
S2
—
the current price of the underlying asset 2
X
—
the strike price
sigma1
—
the volatility of asset 1
sigma2
—
the volatility of asset 2
rho
—
the correlation coefficient between asset 1 and asset 2
T
—
the time to maturity
r
—
the interest rate
q1
—
the continuous dividend yield for asset 1
q2
—
the continuous dividend yield for asset 2
put
—
if put is 0 then a call option, otherwise a put option
M
—
the number of time steps, the zeroth time step is the root node of the lattice
opt_type
—
if opt_type is 0 then an option on the maximum of two asset, otherwise an option on the
minimum of two assets,
is_american
—
if is_american is 0 then a European option, otherwise an American option
Output parameters:
value
—
the value of the option,
iflag
—
an error indicator.
*/
double discount,t1,dt,d1,d2,u1,u2;
Integer i,j,m1,n,iflagx,jj,ind;
double zero¼0.0,hold;
double temp,ds1,ds2,dv1,dv2,h,tmp;
double *s1, *s2, *v;
double p[4];
Integer max_index, P1,P2,tdv;
double sqrt_dt, t, mu1, mu2, jp1, jp2;
double one ¼ 1.0, half ¼ 0.5, quarter ¼ 0.25;
Integer v1, array_size;
Boolean odd_step;
if (!((Mþ1)/2 ¼¼ M/2)){
printf (‘‘ERROR THE NUMBER OF TIME STEPS IS NOT EVEN \n’’);
return;
}
#define UU 0
#define UD 1
#define DD 2
#define DU 3
dt ¼ T/(double)M;
sqrt_dt ¼ sqrt(dt);
jp1 ¼ sigma1*sqrt_dt;
jp2 ¼ sigma2*sqrt_dt;
mu1 ¼ r  q1  sigma1*sigma1*half;
mu2 ¼ r  q2  sigma2*sigma2*half;
u1 ¼ exp(jp1); /* assign the jump sizes */
u2 ¼ exp(jp2);

d1 ¼ exp(jp1);
d2 ¼ exp(jp2);
p[UU] ¼ quarter*(one þ sqrt_dt * ((mu1/sigma1) þ (mu2/sigma2)) þ rho); /* set up the jump probabilities */
p[UD] ¼ quarter*(one þ sqrt_dt * ((mu1/sigma1)  (mu2/sigma2))  rho);
p[DD] ¼ quarter*(one þ sqrt_dt * ((mu1/sigma1)(mu2/sigma2)) þ rho);
p[DU] ¼ quarter*(one þ sqrt_dt * ((mu1/sigma1)þ(mu2/sigma2))  rho);
for (i ¼ 0; i < 4; þþi){
if ((p[i] < zero) || (p[i] > 1.0)) printf (‘‘ERROR p out of range\n’’);
}
temp ¼ floor(log(tol)/log(p[UU])); /* calculate the maximum index to use */
max_index ¼ (Integer)temp þ 1;
if (!((max_indexþ1)/2 ¼¼ max_index/2)){/*then max_index is odd, so make it even */
max_index ¼ max_index þ 1;
}
tdv ¼ max_indexþ1;
#define V(I,J) v[(I) * tdv þ (J)]
discount ¼ exp(r*dt);
for (i ¼ 0; i < 4; þþi){
p[i] ¼ p[i]*discount;
}
/* Allocate the arrays v[(max_indexþ1)*(max_indexþ1)], s1[2*max_indexþ1] and s2[2*max_indexþ1] */



/* assign the 2*max_indexþ1 asset values for s1 */
s1[max_index] ¼ S1;
for (i ¼ 1; i <¼ max_index; þþi){
s1[max_indexþi] ¼ u1*s1[max_indexþi1];
s1[max_indexi] ¼ d1*s1[max_indexiþ1];
}
/* assign the 2*max_indexþ1 asset values for s2 */
s2[max_index] ¼ S2;
for (i ¼ 1; i <¼ max_index; þþi){
s2[max_indexþi] ¼ u2*s2[max_indexþi1];
s2[max_indexi] ¼ d2*s2[max_indexiþ1];
}
P1 ¼ 0;
for (i ¼ 0; i <¼ max_index; þþi){/* Calculate the option values at maturity */
P2 ¼ 0;
for (j ¼ 0; j <¼ max_index; þþj){
if (opt_type ¼¼ 0){/* Maximum of two assets */
if (put){
V(i,j) ¼ MAX(X  MAX(s1[P1],s2[P2]),zero);
}
else{
V(i,j) ¼ MAX(MAX(s1[P1],s2[P2])X,zero);
}
}
else{/* Minimum of two assets */
if (put){
V(i,j) ¼ MAX(X  MIN(s1[P1],s2[P2]),zero);
}
else{
V(i,j) ¼ MAX(MIN(s1[P1],s2[P2])X,zero);
}
}
P2 ¼ P2 þ 2;
}
P1 ¼ P1 þ 2;
}
/* now work backwards through the lattice to calculate the current option value */
odd_step ¼ FALSE;
for (m1 ¼ M  1; m1 >¼ 0; m1){
odd_step ¼ !odd_step;
if (m1 < max_index){/* use normal lattice */
P1 ¼ max_indexm1;
for (i ¼ 0; i <¼ m1; þþi){
P2 ¼ max_indexm1;
for (j ¼ 0; j <¼ m1; þþj){
hold ¼ p[UD]*V(iþ1,j) þ p[UU]*V(iþ1,jþ1) þ p[DU]*V(i,jþ1) þ p[DD]*V(i,j);
if (is_american){
**Insert code fragment 4.1 to deal with option type: put/call, max/min **
}
else{
V(i,j) ¼ hold;
}
P2 ¼ P2 þ 2;
}
Appendix D
387

P1 ¼ P1 þ 2;
}
}
else{/* using a restricted lattice */
if (odd_step){/* compute the option values in reverse order */
/*((only to index 1) so that don’t overwrite storage */
array_size ¼ max_index;
P1 ¼ 2*max_index  1;
for (i ¼ array_size; i >¼ 1; i){
P2 ¼ 2*max_index  1;
for (j ¼ array_size; j >¼ 1; j){
hold ¼ p[UD]*V(i,j1) þ p[UU]*V(i,j) þ p[DU]*V(i1,j) þ p[DD]*V(i1,j1);
if (is_american){
**Insert code fragment 4.1 to deal with option type: put/call, max/ min**
}
else{
V(i,j) ¼ hold;
}
P2 ¼ P2  2;
}
P1 ¼ P1  2;
}
}
else{/* even time step, grow extra nodes at the top and bottom. Compute the */
/* option values in forward order making sure that don’t overwrite storage */
array_size ¼ max_index þ 1;
P2 ¼ 0;
P1 ¼ 0;
for (i ¼ 0; i <¼ array_size  1; þþi){
P2 ¼ 0;
for (j ¼ 0; j <¼ array_size  1; þþj){
if ( i ¼¼ 0){
hold ¼ p[UU]*V(1,j);
}
else if (j ¼¼ 0){
hold ¼ p[UU]*V(i,1);
}
else if (i ¼¼ array_size  1){
hold ¼ p[DD]*V(array_size  1,j);
}
else if (j ¼¼ array_size  1){
hold ¼ p[DD]*V(i,array_size  1);
}
else{
hold¼p[UD]*V(iþ1,j) þ p[UU] *V(iþ1,jþ1) þ
p[DU]*V(i,jþ1) þ p[DD]*V(i,j);
}
if (is_american){
** Insert code fragment 4.1 to deal with option type: put/call, max/min **
}
else{
V(i,j) ¼ hold;
}
P2 ¼ P2 þ 2;
}
P1 ¼ P1 þ 2;
}
}
}
}
tmp ¼ V(0,0);
*value ¼ tmp;
}
Code excerpt D.1
Function that uses a truncated binomial lattice to compute options on the maximum
and minimum of two assets
D.2
RECURSIVE TWO ASSET BINOMIAL LATTICE
Here, in Code excerpt D.2, we show the code for a recursive binomial lattice to price
options on the maximum or minimum of two assets.
388
Appendix D

The parameter M is the number of time intervals used, and the lattice is constructed
under the assumption that M is even. The parameter recc control whether or not a
recursive call to the function is made.
void RECURSIVE_2D_binomial( double *value, double S1, double S2, double X,
double sigma1, double sigma2, double rho, double T, double r, double q1, double q2,
Integer put, Integer M, Integer opt_type, Integer is_american, Integer recc, Integer *iflag)
{
/* Input parameters:
S1
—
the current price of the underlying asset 1
S2
—
the current price of the underlying asset 2
X
—
the strike price
sigma1
—
the volatility of asset 1
sigma2
—
the volatility of asset 2
rho
—
the correlation coefficient between asset 1 and asset 2
T
—
the time to maturity
r
—
the interest rate
q1
—
the continuous dividend yield for asset 1
q2
—
the continuous dividend yield for asset 2
put
—
if put is 0 then a call option, otherwise a put option
M
—
the number of time steps, the zeroth node is the root node of the lattice
opt_type
—
if opt_type is 0 then an option on the maximum of two asset, otherwise an option on the
minimum of two assets
is_american
—
if is_american is 0 then a European option, otherwise an American option
recc
—
if recc is 0 then not a recursive call, otherwise a recursive call
Output parameters:
value
—
the value of the option,
iflag
—
an error indicator.
*/
double discount,t1,dt,d1,d2,u1,u2;
Integer i,j,m1,n,iflagx,jj,ind;
double zero¼0.0,hold;
double temp,ds1,ds2,dv1,dv2,h,tmp;
double *s1, *s2, *v;
double p[4];
Integer P1,P2,tdv;
double loc_T, sqrt_dt, t, mu1, mu2, jp1, jp2;
double one ¼ 1.0, half ¼ 0.5, quarter ¼ 0.25;
Integer v1;
Integer loc_M, loc_recc, loc_iflag;
Integer loc_is_american;
if (!((Mþ1)/2 ¼¼ M/2)){
printf (‘‘ ERROR THE NUMBER OF TIME STEPS IS NOT EVEN \n’’);
return;
}
if (!((recc ¼¼ 0) || (recc ¼¼ 1))){
printf (‘‘ERROR IN THE VALUE OF RECC recc ¼ %ld \n’’, recc);
return;
}
tdv ¼ M þ 1;
#define V(I,J) v[(I) * tdv þ (J)]
#define UU 0
#define UD 1
#define DD 2
#define DU 3
dt ¼ T/(double)M;
sqrt_dt ¼ sqrt(dt);
jp1 ¼ sigma1*sqrt_dt;
jp2 ¼ sigma2*sqrt_dt;
mu1 ¼ r  q1  sigma1*sigma1*half;
mu2 ¼ r  q2  sigma2*sigma2*half;
u1 ¼ exp(jp1);
u2 ¼ exp(jp2);
d1 ¼ exp(jp1);
d2 ¼ exp(jp2);
p[UU] ¼ quarter*(one þ sqrt_dt * ((mu1/sigma1) þ (mu2/sigma2)) þ rho);
p[UD] ¼ quarter*(one þ sqrt_dt * ((mu1/sigma1)  (mu2/sigma2))  rho);
p[DD] ¼ quarter*(one þ sqrt_dt * ((mu1/sigma1)  (mu2/sigma2)) þ rho);
p[DU] ¼ quarter*(one þ sqrt_dt * ((mu1/sigma1) þ (mu2/sigma2))  rho);
for (i ¼ 0; i < 4; þþi){
Appendix D
389

if ((p[i] < zero) || (p[i] > 1.0)) printf (‘‘ERROR p out of range\n’’);
}
discount ¼ exp(r*dt);
for (i ¼ 0; i < 4; þþi){
p[i] ¼ p[i]*discount;
}
/* Allocate the arrays v[(Mþ1)*(Mþ1)], s1[2*Mþ1] and s2[2*Mþ1] */



s1[M] ¼ S1;
for (i ¼ 1; i <¼ M; þþi){/* assign the 2*Mþ1 asset values for s1 */
s1[Mþi] ¼ u1*s1[Mþi1];
s1[Mi] ¼ d1*s1[Miþ1];
}
s2[M] ¼ S2;
for (i ¼ 1; i <¼ M; þþi){/* assign the 2*Mþ1 asset values for s2 */
s2[Mþi] ¼ u2*s2[Mþi1];
s2[Mi] ¼ d2*s2[Miþ1];
}
/* Calculate the option values at maturity */
if (recc ¼¼ 0){/* called without recursion */
P1 ¼ 0;
for (i ¼ 0; i <¼ M; þþi){
P2 ¼ 0;
for (j ¼ 0; j <¼ M; þþj){
if (opt_type ¼¼ 0){/* Maximum of two assets */
if (put){
V(i,j) ¼ MAX(X  MAX(s1[P1],s2[P2]),zero);
}
else{
V(i,j) ¼ MAX(MAX(s1[P1],s2[P2])X,zero);
}
}
else{/* Minimum of two assets */
if (put){
V(i,j) ¼ MAX(X  MIN(s1[P1],s2[P2]),zero);
}
else{
V(i,j) ¼ MAX(MIN(s1[P1],s2[P2])X,zero);
}
}
P2 ¼ P2 þ 2;
}
P1 ¼ P1 þ 2;
}
}
else{/* called with recursive last step */
P1 ¼ 1;
for (i ¼ 0; i <¼ M1; þþi){
P2 ¼ 1;
for (j ¼ 0; j <¼ M1; þþj){
loc_T ¼ dt;
loc_M ¼ 10;
loc_recc ¼ 0;
loc_iflag ¼ 0;
loc_is_american ¼ is_american;
recursive_2D_binomial(&hold, s1[P1], s2[P2], X, sigma1, sigma2, rho,
loc_T, r, q1, q2, put, loc_M, opt_type, loc_is_american, loc_recc, &loc_iflag);
if (is_american){
if (opt_type ¼¼ 0){/* Maximum of two assets */
if (put)
V(i,j) ¼ MAX(hold,XMAX(s1[P1],s2[P2]));
else
V(i,j) ¼ MAX(hold,MAX(s1[P1],s2[P2])X);
}
else{/* Minimum of two assets */
if (put)
V(i,j) ¼ MAX(hold,XMIN(s1[P1],s2[P2]));
else
V(i,j) ¼ MAX(hold,MIN(s1[P1],s2[P2])X);
}
}
else{
V(i,j) ¼ hold;
}
P2 ¼ P2 þ 2;
}
390
Appendix D

P1 ¼ P1 þ 2;
}
}
for (m1 ¼ M1recc; m1 > ¼ 0; m1){/* work backwards through the lattice to calculate the option value */
P1 ¼ Mm1;
/* Identical code to the equivalent loop of the standard 2 dimensional binomial lattice
see code excerpt 5.7 */



}
*value ¼ V(0,0);
}
Code excerpt D.2
Function that uses a recursive binomial lattice to compute options on the maximum
and minimum of two assets
D.3
FOUR ASSET JUMP PROBABILITIES
The jump probabilities for a binomial lattice which models four assets are given
below:
puuuu ¼ 1
16

1 þ
ffiffiffiffiffiffi
t
p
1
1
þ 2
2
þ 3
3
þ 4
4


þ 12 þ 13 þ 14 þ 23 þ 24 þ 34

puuud ¼ 1
16

1 þ
ffiffiffiffiffiffi
t
p
1
1
þ 2
2
þ 3
3
 4
4


þ 12 þ 13  14 þ 23  24 þ 34

puudu ¼ 1
16

1 þ
ffiffiffiffiffiffi
t
p
1
1
þ 2
2
 3
3
þ 4
4


þ 12  13 þ 14  23 þ 24  34

puudd ¼ 1
16

1 þ
ffiffiffiffiffiffi
t
p
1
1
þ 2
2
 3
3
 4
4


þ 12  13  14  23  24 þ 34

puduu ¼ 1
16

1 þ
ffiffiffiffiffiffi
t
p
1
1
 2
2
þ 3
3
þ 4
4


 12 þ 13 þ 14  23  24 þ 34

pudud ¼ 1
16

1 þ
ffiffiffiffiffiffi
t
p
1
1
 2
2
þ 3
3
 4
4


 12 þ 13  14  23 þ 24  34

puddu ¼ 1
16

1 þ
ffiffiffiffiffiffi
t
p
1
1
 2
2
 3
3
þ 4
4


 12  13 þ 14 þ 23  24  34

puddd ¼ 1
16

1 þ
ffiffiffiffiffiffi
t
p
1
1
 2
2
 3
3
 4
4


 12  13  14 þ 23 þ 24 þ 34

pduuu ¼ 1
16

1 þ
ffiffiffiffiffiffi
t
p
 1
1
þ 2
2
þ 3
3
þ 4
4


 12  13  14 þ 23 þ 24 þ 34

pduud ¼ 1
16

1 þ
ffiffiffiffiffiffi
t
p
 1
1
þ 2
2
þ 3
3
 4
4


 12  13 þ 14 þ 23  24  34

pdudu ¼ 1
16

1 þ
ffiffiffiffiffiffi
t
p
 1
1
þ 2
2
 3
3
þ 4
4


 12 þ 13  14  23 þ 24  34

Appendix D
391

pdudd ¼ 1
16

1 þ
ffiffiffiffiffiffi
t
p
 1
1
þ 2
2
 3
3
 4
4


 12 þ 13 þ 14  23  24 þ 34

pdduu ¼ 1
16

1 þ
ffiffiffiffiffiffi
t
p
 1
1
 2
2
þ 3
3
þ 4
4


þ 12  13  14  23  24 þ 34

pddud ¼ 1
16

1 þ
ffiffiffiffiffiffi
t
p
 1
1
 2
2
þ 3
3
 4
4


þ 12  13 þ 14  23 þ 24  34

pdddu ¼ 1
16

1 þ
ffiffiffiffiffiffi
t
p
 1
1
 2
2
 3
3
þ 4
4


þ 12 þ 13  14 þ 23  24  34

pdddd ¼ 1
16

1 þ
ffiffiffiffiffiffi
t
p
 1
1
 2
2
 3
3
 4
4


þ 12 þ 13  14 þ 23 þ 24 þ 34

392
Appendix D

Appendix E
Derivation of the conditional mean and
covariance for a multivariate normal
distribution
Let
X ¼ [X1=X2]
be
distributed
as
Np(, )
with
 ¼ [1=2]
and
 ¼ [ (11j12)=(21j22)] and j22j > 0.
We will prove that the conditional distribution of X1, given that X2 ¼ x2, is normal
and has:
Mean ¼ 1 þ 111
22 ðx2  2Þ, and covariance ¼ 11  121
22 21. Let the
inverse of  be 1, where:
1 ¼
11
12
21
22


ðE:1Þ
So 1 ¼ Ip, where Ip represents the p  p unit matrix, and:
11
12
21
22


11
12
21
22


¼
Iq
0
0
Ipq


ðE:2Þ
Multiplying out these matrices yields the following equations:
1111 þ 2121 ¼ Iq
ðE:3Þ
2111 þ 2222 ¼ 0
ðE:4Þ
1112 þ 1222 ¼ 0
ðE:5Þ
2112 þ 2222 ¼ Ipq
ðE:6Þ
Multiplying Equation E.5 on the left by ð11Þ1 and on the right by 1
22 gives:
ð11Þ112 ¼ 121
22
ðE:7Þ
Multiplying Equation E.3 on the left by ð11Þ1 yields
11 þ ð11Þ11221 ¼ ð11Þ1
ðE:8Þ
and substituting for ð11Þ112 from Equation E.7 into Equation E.8 gives
ð11Þ1 ¼ 11  121
22 21
ðE:9Þ
The joint probability density function of x is:
f ðxÞ ¼ ð2Þp=2jj1=2 exp  1
2 ðx  ÞT1ðx  Þ



writing x,  and 1 in their partitioned form and expanding gives:
f ðxÞ ¼ ð2Þp=2jj1=2 exp  1
2
ðx1  1ÞT11ðx1  1Þ
n

þ2ðx1  1ÞT12ðx2  2Þ þ ðx2  2ÞT22ðx2  2Þ
oi
ðE:10Þ
The conditional distribution of x1 given the value of x2 is thus obtained by dividing
this density by the marginal density of x2, and treating x2 as constant in the resulting
expression. The only portion of the resultant that is not constant is the portion
involving terms in x1. It can easily be shown that:
f ðx1jx2Þ / exp
"
 1
2
n
ðx1  1ÞT11ðx1  1Þ þ 2ðx1  1ÞT 12ðx2  2Þ
o
where the constant of proportionality is obtained using
R
f ðx1jx2Þdx1 ¼ 1.
If we let
G ¼ ðx1  1ÞT11ðx1  1Þ þ 2ðx1  1ÞT12ðx2  2Þ
we then obtain:
G ¼ðx1 1ÞT11ðx1 1Þþðx1 1ÞT12ðx2 2Þþðx2 2ÞT21ðx1 1Þ
G ¼ x1 1 þð11Þ112ðx2 2Þ
n
oT
11 x1 1 þð11Þ112ðx2 2Þ
n
o
ðx2 2ÞT21ð12Þ1ðx2 2Þ
ðE:11Þ
where, for instance we have used, the fact that the scalar quantity
ðx1  1ÞT12ðx2  2Þ
n
oT
¼ ðx2  2ÞT21ðx1  1Þ
Since the last term in Equation E.11 only involves constants (as far as f ðx1jx2Þ is
concerned), it follows that:
f ðx1jx2Þ / exp  1
2
x1  1 þ ð11Þ112ðx2  2Þ
n
oT

 11 x1  1 þ ð11Þ112ðx2  2Þ
n
o
which is the density of a multivariate normal distribution that has a mean of
1  ð11Þ112ðx2  2Þ,
which
from
Equation
E.7
can
be
expressed
as
1 þ 121
22 ðx2  2Þ. The covariance matrix is ð11Þ1, which from Equation E.9
can be written as 11  121
22 21.
394
Appendix E

Appendix F
Standard statistical results
F.1
THE LAW OF LARGE NUMBERS
Let X1, X2, . . . be a sequence of independent, identically distributed random variables
(IID), each with expected value  and variance 2. Define the sequence of averages
Yn ¼ X1 þ X2 þ    þ Xn
n
;
n ¼ 1; 2; . . .
Then Yn converges to  as n ! 1.
We will not rigorously prove this theorem but show that it is plausible. For the
mean of Yn we have:
E½Yn ¼ 1
n E½X1 þ E½X2 þ þ    þ E½Xn
ð
Þ ¼ 1
n n ¼ 
For the variance of Yn we have:
VarðYnÞ ¼
X
n
i¼1
Var Xi
n


¼
X
n
i¼1
2
n2 ¼ 2
n
where we have used the fact that the variance of the sum of independent random
variables is the sum of their variances, see Section F.2.
So as n ! 1, we have Var(Yn) ! 0.
F.2
THE CENTRAL LIMIT THEOREM
This is similar to the Law of Large numbers. In this case we divide by
ffiffin
p
instead
of n, which prevents the variance of Yn converging to zero as n ! 1.
Let X1, X2, . . . be a sequence of independent, identically distributed random vari-
ables (IID), each with expected value  and variance 2. Define:
Zn ¼ ðX1  Þ þ ðX2  Þ þ . . . þ ðXn  Þ
ffiffin
p
;
n ¼ 1; 2; . . .
so that each Zn has expected value zero and variance
VarðZnÞ ¼
X
n
i¼1
Var ðXi  Þ
ffiffin
p


¼
X
n
i¼1
2
n ¼ 2

The central Limit Theorem states that as n ! 1 the distribution of Zn approaches
that of a normal random variable (say x) with mean zero and variance 2. In other
words the probability density function of Zn is:
PðZnÞ !
1

ffiffiffiffiffi
2
p
exp  x2
22


as n ! 1
F.3
THE MEAN AND VARIANCE OF LINEAR FUNCTIONS OF RANDOM
VARIABLES
Let X be a variate from a given distribution, and Z be the following linear function of
this variate:
Z ¼ a þ bX
where a and b are constants. Then
E½Z ¼ E½a þ E½bX ¼ a þ bE½X
and
Var½Z ¼ E½ðZ  E½ZÞ2
¼ E½ða þ bX  a  bE½XÞ2
¼ E½ðbX  bE½XÞ2
¼ E½b2ðX  E½XÞ2
¼ b2E½ðX  E½XÞ2
Therefore the mean is bE[X], and the variance is b2Var[X].
The variance of the sum of random identical independently distributed variables
(IID).
F.3.1
The sum of 2 variables
Let Z2 ¼ X1 þ X2, where X1 and X2 are IID variables. Then we have:
Var½Z2 ¼ E½ððX1 þ X2Þ  E½X1 þ X2Þ2
¼ E½ððX1  E½X1Þ þ ðX2  E½X2ÞÞ2
¼ E½ðX1  E½X1Þ2 þ ðX2  E½X2Þ2 þ 2ðX1  E½X1ÞðX2  E½X2Þ
¼ E½ðX1  E½X1Þ2 þ E½ðX2  E½X2Þ2
¼ Var½X1 þ Var½X2;
where
we
have
used
the
fact
that,
since
the
variables
are
independent
E[(X1  E[X1])(X2  E[X2])] ¼ 0. Therefore:
Var½X1 þ X2 ¼ Var½X1 þ Var½X2
396
Appendix F

F.3.2
The sum of 3 variables
Let Z3 ¼ X1 þ X2 þ X3, where X1, X2, and X3 are IID variables. Then we have:
Var½Z3 ¼ E½ððX1 þ X2 þ X3Þ  E½X1 þ X2 þ X3Þ2
¼ E½ððX1  E½X1 þ ðX2  E½X2Þ þ ðX3  E½X3ÞÞ2
¼ E½ðX1  E½X1Þ2 þ ðX2  E½X2Þ2 þ ðX2  E½X2Þ2
þ 2ðX1  E½X1ÞðX2  E½X2Þ þ 2ðX1  E½X1ÞðX3  E½X3Þ
þ 2ðX2  E½X2ÞðX3  E½X3Þ
¼ E½ðX1  E½X1Þ2 þ E½ðX2  E½X2Þ2 þ E½ðX3  E½X3Þ2
¼ Var½X1 þ Var½X2 þ Var½X3
where, as before, we have used the fact that E[(Xi  E[Xi]) (Xj  E[Xj])] ¼ 0,
i ¼ 1, . . . , 3, j ¼ 1, . . . , 3, i 6¼ j. Therefore:
Var½X1 þ X2 þ X3 ¼ Var½X1 þ Var½X2 þ Var½X3
F.3.3
The sum of n variables
Let Zn ¼ P
n
i¼1
Xi
Then we have:
Var½Zn ¼ E
X
n
i¼1
Xi  E½Xi
(
)2
2
4
3
5
¼
X
n
i¼1
E½ðXi  E½XiÞ2 þ
X
n
i¼1
X
n
j¼1ð j6¼iÞ
E½ðXi  E½XiÞðXj  E½XjÞ
¼
X
n
i¼1
E½ðXi  E½XiÞ2
¼
X
n
i¼1
Var½Xi
Therefore:
Var
X
n
i¼1
Xi
"
#
¼
X
n
i¼1
Var½Xi
F.4
STANDARD ALGORITHMS FOR THE MEAN AND VARIANCE
In this section we provide standard results concerning the computation of the mean
and variance (covariance) of the observations contained in a given data set.
The variance of X is defined as:
Var½X ¼ E½ðX  E½XÞ2
Appendix F
397

The simplest way of computing the variance is to use a two pass method. We
illustrate this with a simple Monte Carlo program which is designed to stop when the
result has attained a given accuracy.
double result[1000000]
// need to provide a large array to store the results



tol ¼ 0.1
mean_X ¼ 0.0
i ¼ 1
while (variance > tol){
// keep going until the variance is smallenough
//call a Monte Carlo function, with n parameters, which return the current estimate
result[i] ¼ my_monte_carlo(param_1, param_2, . . . , param_n)
mean_X ¼ (mean_X þ result[i])/i
// first pass to calculate the mean
for (j¼ 1, j <¼i; þþi){
// second pass to calculate the variance
variance ¼ (result[i]  mean_X)*(result[i]  mean_X)
}
variance ¼ variance/(double)i
i ¼i þ 1
}
Although numerical stable (West, 1979) this approach requires the allocation of
the very large array result, and also contains a nested for loop.
We can get round this problem by expanding the terms in the variance as follows:
Var½X ¼ E½ðX  E½XÞ2
¼ E½X2 þ ðE½XÞ2  2XE½X
¼ E½X2 þ ðE½XÞ2  2ðE½XÞ2
ðF:1Þ
Therefore Var[X] ¼ E[X2]  (E[X])2. This approach leads to the so-called text-
book algorithm which allows the variance to be computed by using only one pass
through the data. The program for our original problem then becomes:
tol ¼ 0.1
mean_X ¼ 0.0
mean_X_squared ¼ 0.0
i ¼ 1.0
while (variance > tol){// keep going until the variance is small enough
// call a Monte Carlo function, with n parameters, which return the current estimate
result ¼ my_monte_carlo(param_1, param_2, . . . ,param_n)
// calculate the running mean
mean_X ¼ (mean_X þ result)/i
// calculate the running mean value of the square of the result
mean_X_squared ¼ (mean_X_squared þ result*result)/i
// calculate the running variance
variance ¼ mean_X_squared  (mean_X*mean_X)
i ¼ i þ 1.0
}
Although this method doesn’t require extra memory allocation and doesn’t require
a second pass through the data, it is numerically unstable (Chan et al., 1982;
West, 1979) and the algorithm given in Section F.5 should be used if accurate results
are required.
398
Appendix F

The textbook algorithm can easily be extended to compute the covariance rather
than the variance.
If we consider two random variates X and Y then the covariance, COV[X, Y], is
defined as:
COV½X; Y ¼ E½ðX  E½XÞðY  E½YÞ
This can be expanded as follows:
COV½X; Y ¼ E½ðX  E½XÞðY  E½YÞ
¼ E½XY þ E½XE½Y  YE½X  XE½Y
¼ E½XY þ E½XE½Y  E½YE½X  E½XE½Y
Therefore the covariance is given by the following equation:
COV½X; Y ¼ E½XY  E½XE½Y
ðF:2Þ
F.5
THE HANSON AND WEST ALGORITHM FOR THE MEAN AND VARIANCE
Here we describe a method of computing the mean and variance (covariance) of a
data set that is more numerically stable than the textbook algorithm given in Section
F.4, West (1979).
We will consider an n  p data matrix of n observations on p variates. The
observations are represented by the p element vector Xi, i ¼ 1, . . . , n.
Let the mean of the first i  1 observations be denoted by X[i1] ¼ i1
k¼1Xk=i  1:
Then we have:
X½i ¼
P
i
k¼1
Xk
i
¼ Xi
i þ
P
i1
k¼1
Xk
i
¼ Xi
i þ i  1
i
P
i1
k¼1
Xk
i  1
Therefore:
X½i ¼ Xi
i þ i  1
i
Xi1 ¼ X½i1 þ 1
i Xi  X½i1


ðF:3Þ
Let 2
[i1] be the variance of the first i  1 observations. This means that the sum of
squares about the mean S2
[i1], of the first i  1 observations is S2
[i1] ¼ (i  1)2
[i1].
Now from the definition of variance we have:
S2
½i1
i  1 ¼ 2
½i1 ¼
1
i  1
X
i1
k¼1
X2
k
 
!

X½i1

2
so
X
i1
k¼1
X2
k ¼ S2
½i1 þ ði  1Þ X½i1

2
Appendix F
399

Now the inclusion of the ith observation Xi results in the new sum of squares about
the mean S2
[i]:
S2
½i ¼
X
i
k¼1
X2
k
 
!
 i X½i

2
S2
½i ¼
X
i1
k¼1
X2
k
 
!
þ X2
i  i X½i

2
S2
½i ¼ S2
i1 þ ði  1Þ X½i1

2þX2
i  i X½i

2
ðF:4Þ
But
i X½i

2 ¼ i
i2 Xi þ ði  1Þ X½i1

2
i X½i

2 ¼ 1
i
ði  1Þ2 X½i1

2þ 2ði  1ÞXi X½i1 þ X2
i
n
o
ðF:5Þ
So we have:
S2
½i ¼ S2
½i1 þ ði  1Þ X½i1

2þX2
i  ði  1Þ2
i
X½i1

2 2ði  1Þ
i
Xi X½i1  X2
i
i
¼ S2
½i1 þ ði  1Þ 1  i  1
i


X½i1

2þ 1  1
i


X2
i  2ði  1Þ
i
Xi X½i1
Therefore
S2
½i ¼ S2
½i1 þ ði  1Þ
i
X½i1

2þ i  1
i


X2
i  2ði  1Þ
i
Xi X½i1
ðF:6Þ
The above equation can be written in more compact form since:
i  1
i


Xi  X½i1

Xi  X½i1

¼ i  1
i
X2
i þ i  1
i

X½i1
2
2 i  1
i


Xi X½i1
which gives the final updating equation for the sum of squares about the mean as:
S2
½i ¼ S2
½i1 þ
i  1
i


Xi  X½i1

Xi  X½i1

ðF:7Þ
This useful equation gives the sum of squares about the mean S2
[i], given the
previous sum of squares about the mean S2
[i1], the previous mean X[i1], and the
new data point Xi.
The estimated variance, Var[X], computed using the data Xi, i ¼ 1, . . . , n, is there-
fore given by:
Var½X ¼
S2
½n
n  1
The following code excerpt shows how the algorithm works in practice
tol ¼ 0.1
// call a Monte Carlo function, with n parameters, which return the current estimate
result ¼ my_monte_carlo(param_1, param_2, . . . ,param_n)
400
Appendix F

mean_X ¼ result
SS_X ¼ 0.0
i ¼ 2.0
while (variance > tol){// keep going until the variance is small enough
// call a Monte Carlo function, with n parameters, which return the current estimate
result ¼ my_monte_carlo(param_1, param_2, . . . ,param_n)
temp ¼ result  mean_X
// calculate the running mean
mean_X ¼ mean_X þ (temp/i)
// calculate the running sum of squares about the mean, SS_X
SS_X ¼ SS_X þ (((i 1.0)/i) * temp * temp)
variance ¼ SS_X/i
i ¼ i þ 1.0
}
The above method can easily be extended to compute the covariance of two
variables X and Y. The covariance is defined as follows:
COVðX; YÞ ¼
1
n  1
X
n
i¼1
ðXi  XÞðYi  YÞ
where
X ¼ 1
n
X
n
i¼1
Xi;
Y ¼ 1
n
X
n
i¼1
Yi
Xi and Yi denote the ith data values of X and Y respectively, and the expression
(Xi  X)(Yi  Y) is termed the ith cross product about the means X and Y. As before
we will also let Xi and Yi denote the running means of the first i observations, of the
X and Y variables respectively.
The ith sum of the cross products about the means is updated according to the
following equation:
P½i ¼ P½i1 þ
i  1
i


Xi  X½i1


Yi  Y½i1


ðF:8Þ
where P[i] denotes the updated sum of the cross products about the mean, P[i1]
denotes the previous sum of the cross products about the mean, X[i1] is the previous
mean of the variable X, Y[i1] is the previous mean of the variable Y, and the new
variate values are Xi and Yi.
The estimated covariance, COV[X, Y], computed using the data Xi, i ¼ 1, . . . , n,
and Yi, i ¼ 1, . . . , n, is therefore given by:
COV½X; Y ¼ P½n
n  1
F.6
JENSEN’S INEQUALITY
This states that if the function h(X) of a random variable X is convex and E[X] ¼ ,
then E[h(X)]  h().
Appendix F
401

F.6.1
Proof
Let X be a random variable with expected value E[X] ¼  and the variable Y be a
nonlinear function of X, Y ¼ h(X). Then @Y=@X ¼ h0(X). If Z is the tangent to h(X)
at the point  then:
Z ¼ hðÞ þ h0ðÞðX  Þ
Since h() and h0() are constants we have that:
E½Z ¼ hðÞ þ h0ðÞE½ðX  Þ ¼ hðÞ þ h0ðÞðE½X  Þ ¼ hðÞ
If the function h(X) is convex then Y  Z everywhere. Then regardless of the
distibution of X we have:
E½Y  E½Z; but E½Z ¼ hðÞ
so
E½Y  hðÞ
Therefore for a convex function h(X) we have that:
E½hðXÞ  hðÞ
For a concave function we obviously have:
E½hðXÞ  hðÞ
An example of a convex function is h(X) ¼ X2. So regardless of the distribution of
X we have that E(X2)  (E[X])2.
An example of a concave function is h(X) ¼ log (X). So regardless of the distribu-
tion of X we have that E( log (X))  log (E[X]).
402
Appendix F

Appendix G
Derivation of barrier option integrals
G.1
THE DOWN AND OUT CALL
We will now derive the formula for the value, cdo, of a down and out call option
which was given in Part I Section 2.4.2.
cdo ¼ expðrÞ

ffiffiffi
p
ffiffiffiffiffi
2
p
Z 1
X¼logðE=SÞ
S expðXÞ  E
f
g f ðX > BÞdX
ðG:1Þ
where
f ðX > BÞ ¼
1

ffiffiffi
p
ffiffiffiffiffi
2
p
exp  X  ðr  2=2Þ

2
22
 
!
	
1  exp 2 logðB=SÞðX  logðB=SÞ
2


	

We will represent this integral as:
cdo ¼ IA þ IB
where
IA ¼ expðrÞ

ffiffiffi
p
ffiffiffiffiffi
2
p
Z 1
X¼logðE=SÞ
S expðXÞ  E
f
g exp  X  ðr  2=2Þ

2
22
 
!
dX
and
IB ¼  expðrÞ

ffiffiffi
p
ffiffiffiffiffi
2
p
Z 1
X¼logðE=SÞ
S expðXÞ  E
f
g exp  X  ðr  2=2Þ

2
22
 
!
	 exp 2 logðB=SÞðX  logðB=SÞÞ
2


dX
G.1.1
Evaluation of integral IA
Now comparing IA with Equation 2.34 in Part I Section 2.3.3 we can identify IA as
c(S,E,), the price of a European call. That is:
IA ¼ SN1ðd1Þ  E expðrÞN1ðd2Þ
ðG:2Þ

where:
d1 ¼ logðS=EÞ þ ðr þ 2=2Þ

ffiffiffi
p
and
d2 ¼ logðS=EÞ þ ðr  2=2Þ

ffiffiffi
p
G.1.2
Evaluation of integral IB
We will now consider the integral IB, and let IB ¼ IC þ ID where:
IC ¼  S expðrÞ

ffiffiffi
p
ffiffiffiffiffi
2
p
Z 1
X¼logðE=SÞ
expðXÞ exp  X  ðr  2=2Þ

2
22
 
!
	 exp 2 logðB=SÞðX  logðB=SÞÞ
2


dX
and
ID ¼ E expðrÞ

ffiffiffi
p
ffiffiffiffiffi
2
p
Z 1
X¼logðE=SÞ
exp  X  ðr  2=2Þ

2
22
 
!
	 exp 2 logðB=SÞðX  logðB=SÞÞ
2


dX
G.1.3
Evaluation of integral ID
We will first consider ID and factor the integrand as follows:
 exp  X  ðr  2=2Þ

2
22
 
!
exp 2 logðB=SÞðX  logðB=SÞÞ
2


¼ exp  X  ðr  2=2Þ

2  4 logðB=SÞðX  logðB=SÞÞ
22
 
!
¼ exp  X  ðr  2=2Þ  2 logðB=SÞ

2
22
 
!
exp 4ðr  2=2Þ logðB=SÞ
22


ðG:3Þ
This means that ID can be expressed as:
ID ¼ B
S
 2ðr2=2Þ=2E expðrÞ

ffiffiffi
p
ffiffiffiffiffi
2
p
	
Z 1
X¼logðE=SÞ
exp  X  ðr  2=2Þ  2 logðB=SÞ

2
22
 
!
dX
Letting u ¼ (X  (r  2=2)  2 log (B=S))/
ffiffiffi
p
we have dX ¼ 
ffiffi
(
p
)du and
404
Appendix G

ID ¼
B
S
 2ðr2=2Þ=2E expðrÞ

ffiffiffi
p
ffiffiffiffiffi
2
p
Z 1
u¼k3
exp  u2
2


du
where
k3 ¼ logðE=SÞ  ðr  2=2Þ  2 logðB=SÞ

ffiffiffi
p
¼ logðES=B2Þ  ðr  2=2Þ

ffiffiffi
p
So
ID ¼
B
S
 2r=21
E expðrÞN1ðk3Þ
ðG:4Þ
Letting d3 ¼ k3 we have:
ID ¼
B
S
 2r=21
E expðrÞN1ðd3Þ;
where d3 ¼ logðB2=SEÞ þ ðr  2=2Þ

ffiffiffi
p
ðG:5Þ
G.1.4
Evaluation of integral IC
Now consider the term
IC ¼ S expðrÞ

ffiffiffi
p
ffiffiffiffiffi
2
p
Z 1
X¼logðE=SÞ
expðXÞ exp  X  ðr  2=2Þ

2
22
 
!
	 exp 2 logðB=SÞðX  logðB=SÞÞ
2


dX
Now we have:
expðXÞ exp  ðX  ðr  2=2ÞÞ2
22


exp 2 logðB=SÞðX  logðB=SÞ
2


¼ exp
 ðX  ðr  2=2ÞÞ2  22X  4logðB=SÞX þ 4ðlogðB=SÞÞ2
n
o
22
0
@
1
A
¼ exp ð2Þ2 þ 2ðr  2=2Þ22 þ 4ðr  2=2Þ logðB=SÞ þ 42 logðB=SÞ
22


	 exp  X  ðr  2=2Þ  2  2logðB=SÞ

2
22
 
!
¼ expðrÞexp
2r
2 þ 1
	

logðB=SÞ


exp  X  ðr  2=2Þ  2  2logðB=SÞ

2
22
 
!
¼ expðrÞ B
S
 2r=2þ1
exp  X  ðr  2=2Þ  2  2logðB=SÞ

2
22
 
!
Appendix G
405

So we have:
IC ¼  B
S
 2r=2þ1
S

ffiffi
p
ffiffiffiffiffi
2
p
	
Z 1
X¼logðE=SÞ
exp  X  ðr  2=2Þ  2  2 logðB=SÞ

2
22
 
!
dX
Letting u ¼ ðX  ðr  2=2Þ  2  2 logðB=SÞÞ=ð
ffiffiffi
p Þ we have dX = 
ffiffiffi
p du
and
IC ¼ S B
S
 2r=2þ1
N1ðk4Þ
ðG:6Þ
where
k4 ¼ logðE=SÞ  ðr  2=2Þ  2  2 logðB=SÞ

ffiffiffi
p
¼ logðES=B2Þ  ðr þ 2=2Þ

ffiffiffi
p
which gives
IC ¼ S B
S
 2r=2þ1
N1ðk4Þ
or letting d4 ¼ k4 we have
IC ¼ S B
S
 2r=2þ1
N1ðd4Þ;
where
d4 ¼ logðB2=ESÞ þ ðr þ 2=2Þ

ffiffiffi
p
ðG:7Þ
Therefore the value for the down and out call option is: cdo ¼ IA þ IC þ ID which,
on collecting all the terms, yields:
Value of the down and out call option
cdo ¼ S
N1ðd1Þ  N1ðd4Þ B
S
 2r=2þ1
 
!
 E expðrÞ N1ðd2Þ  N1ðd3Þ B
S
 2r=21
 
!
ðG:8Þ
G.2
THE UP AND OUT CALL
We will now derive the formula for the value, cuo, of an up and out call option which
was given in Part I Section 2.4.3.
cuo ¼ expðrÞ

ffiffiffi
p
ffiffiffiffiffi
2
p
Z logðB=SÞ
X¼logðE=SÞ
S expðXÞ  E
f
g f ðX < BÞdX
ðG:9Þ
406
Appendix G

where
f ðX < BÞ ¼
1

ffiffiffi
p
ffiffiffiffiffi
2
p
ffiffiffi
2

r
exp  X  ðr  2=2Þ

2
22
 
!
	
1  exp 2 logðB=SÞðX  logðB=SÞ
2


	

ðG:10Þ
We will represent this integral as:
cuo ¼ IA þ IB
where:
IA ¼ expðrÞ

ffiffiffi
p
ffiffiffiffiffi
2
p
Z logðB=SÞ
X¼logðE=SÞ
S expðXÞ  E
f
g exp  X  ðr  2=2Þ

2
22
 
!
dX
and
IB ¼  expðrÞ

ffiffiffi
p
ffiffiffiffiffi
2
p
Z logðB=SÞ
X¼logðE=SÞ
S expðXÞ  E
f
g exp  X  ðr  2=2Þ

2
22
 
!
	 exp 2 logðB=SÞðX  logðB=SÞÞ
2


dX
G.2.1
Evaluation of integral IA
Letting IA ¼ I1 þ I2 where
I1 ¼ S expðrÞ

ffiffiffi
p
ffiffiffiffiffi
2
p
Z logðB=SÞ
X¼logðE=SÞ
expðXÞ exp  X  ðr  2=2Þ

2
22
 
!
dX
and
I2 ¼ E expðrÞ

ffiffiffi
p
ffiffiffiffiffi
2
p
Z logðB=SÞ
X¼logðE=SÞ
exp  X  ðr  2=2Þ

2
22
 
!
dX
From our previous derivation of the Black–Scholes formula in Part I Section 2.3.3
we have:
I1 ¼ S expðrÞ

ffiffiffi
p
ffiffiffiffiffi
2
p
Z k2
u¼k1
exp  u2
2


du ¼ S N1ðk2Þ  N1ðk1Þ
f
g
where
k1 ¼ logðE=SÞ  ðr þ 2=2Þ

ffiffiffi
p
and
k2 ¼ logðB=SÞ  ðr þ 2=2Þ
ffiffiffi
p
I2 ¼ E expðrÞ

ffiffiffi
p
ffiffiffiffiffi
2
p
Z k4
u¼k3
exp  u2
2


du ¼  E expðrÞ N1ðk4Þ  N1ðk3Þ
f
g
Appendix G
407

where
k3 ¼ logðE=SÞ  ðr  2=2Þ

ffiffiffi
p
and
k4 ¼ logðB=SÞ  ðr  2=2Þ

ffiffiffi
p
Therefore
IA ¼ S N1ðk2Þ  N1ðk1Þ
f
g  E expðrÞ N1ðk4Þ  N1ðk3Þ
f
g
ðG:11Þ
Letting IB ¼ IC þ ID where:
IC ¼  S expðrÞ

ffiffiffi
p
ffiffiffiffiffi
2
p
Z logðB=SÞ
X¼logðE=SÞ
expðXÞ exp  X  ðr  2=2Þ

2
22
 
!
	 exp 2 logðB=SÞðX  logðB=SÞÞ
2


dX
and
ID ¼ E expðrÞ

ffiffiffi
p
ffiffiffiffiffi
2
p
Z logðB=SÞ
X¼logðE=SÞ
exp  X  ðr  2=2Þ

2
22
 
!
	 exp 2 logðB=SÞðX  logðB=SÞÞ
2


dX
G.2.2
Evaluation of integral ID
In a similar manner to that in Section G.1 we have:
ID ¼
B
S
 2ðr2=2Þ=2E expðrÞ

ffiffiffi
p
ffiffiffiffiffi
2
p
	
Z logðB=SÞ
X¼logðE=SÞ
exp  X  ðr  2=2Þ  2 logðB=SÞ

2
22
 
!
dX
Letting u ¼ X  ðr  2=2Þ  2 logðB=SÞ

ffiffiffi
p
gives
ID ¼
B
S
 2ðr2=2Þ=2E expðrÞ

ffiffiffi
p
ffiffiffiffiffi
2
p
Z k6
u¼k5
exp  u2
2


du
ðG:12Þ
where
k5 ¼ logðE=SÞ  ðr  2=2Þ  2 logðB=SÞ

ffiffiffi
p
¼ logðES=B2Þ  ðr  2=2Þ

ffiffiffi
p
and
k6 ¼ logðB=SÞ  ðr  2=2Þ  2 logðB=SÞ

ffiffiffi
p
¼ logðS=BÞ  ðr  2=2Þ

ffiffiffi
p
408
Appendix G

Therefore:
ID ¼
B
S
 2r=21
E expðrÞN1ðk6Þ  N1ðk5Þ
f
g
ðG:13Þ
G.2.3
Evaluation of integral IC
Now consider the term
IC ¼  S expðrÞ

ffiffiffi
p
ffiffiffiffiffi
2
p
Z logðB=SÞ
X¼logðE=SÞ
expðXÞ exp  X  ðr  2=2Þ

2
22
 
!
	 exp 2 logðB=SÞðX  logðB=SÞÞ
2


dX
In a similar manner to that in Section G.1 we have:
IC ¼  B
S
 2r=2þ1
S

ffiffiffi
p
ffiffiffiffiffi
2
p
	
Z logðB=SÞ
X¼logðE=SÞ
exp  X  ðr  2=2Þ  2  2 logðB=SÞ

2
22
 
!
dX
Letting u ¼ ðX  ðr  2=2Þ  2  2 logðB=SÞÞ=ð
ffiffiffi
p Þ gives
IC ¼ S B
S
 2r=2þ1
N1ðk8Þ  N1ðk7Þ
f
g
ðG:14Þ
where
k7 ¼ logðE=SÞ  ðr  2=2Þ  2  2 logðB=SÞ

ffiffiffi
p
¼ logðES=B2Þ  ðr þ 2=2Þ

ffiffiffi
p
k8 ¼ logðB=SÞ  ðr  2=2Þ  2  2 logðB=SÞ

ffiffiffi
p
¼ logðS=BÞ  ðr þ 2=2Þ

ffiffiffi
p
So we have: cuo ¼ IA þ IC þ ID, which on collecting terms gives:
Value of the up and out call option
cuo ¼ S B
S
 2r=2þ1
N1ðk7Þ  N1ðk8Þ
f
g 
B
S
 2r=21
	 E expðrÞ N1ðk5Þ  N1ðk6Þ
f
g
þ S N1ðk2Þ  N1ðk1Þ
f
g  E expðrÞ N1ðk4Þ  N1ð2k3Þ
f
g
ðG:15Þ
Appendix G
409

Appendix H
Algorithms for an AGARCH-I process
Here we provide pseudocode which calculates the log likelihood and is partial
derivatives for a regression-AGARCH-I process. We consider residuals which have
either a Gaussian distribution or a Student’s t distribution. The notation used is the
same as that given in Section 20 of PART III.
H.1
GAUSSIAN DISTRIBUTION
H.1.1
The log likelihood
Deal with the first q terms of the sequence:
 ¼ ^
LðÞ ¼ 0
For i ¼ 1 To num
If (mn ¼¼ 1) i ¼ yi  XT
i ^b
If (mn ¼¼ 0) i ¼ yi  ^b0  XT
i ^b
Next i
For i ¼ 1 To q
hi ¼ 0 þ
X
i1
j¼1
jðij þ Þ2 þ
X
q
j¼i
j2
0 þ
X
p
k¼1
hikk
Store the current value of hi and keep all the previous values of hi.
LðÞ ¼ LðÞ þ 1
2
logðhiÞ þ 2
i
hi


Next i
Deal with the remaining terms of the sequence:
For i ¼ q þ 1 To num
hi ¼ 0 þ
X
q
j¼1
jðij þ Þ2 þ
X
p
k¼1
khik

Store the current value of hi and keep Np previous values of hi.
LðÞ ¼ LðÞ þ 1
2
logðhiÞ þ 2
i
hi


Next i
H.1.2
The first derivatives of the log likelihood
Algorithm for the first q terms of the sequence:
@LðÞ
@k
¼ 0;
k ¼ 1; . . . ; Np
For i ¼ 1 to q
@hi
@0
¼ 1 þ
X
p
k¼1
k @hik
@0
For j ¼ 1 to i  1
@hi
@j
¼ ðij þ Þ2
Next j
For j ¼ i to q
@hi
@j
¼ 2
0
Next j
For j ¼ 1 to q
@hi
@j
¼ @hi
@j
þ
X
p
k¼1
k @hik
@j
Next j
For j ¼ 1 to p
@hi
@j
¼ hij þ
X
p
k¼1
j @hik
@k
Next j
@hi
@ ¼
X
i1
j¼1
2ðij þ Þj þ
X
p
k¼1
k @hik
@
hi ¼ 0 þ
X
p
k¼1
hikk þ
X
i1
j¼1
jðij þ Þ2 þ
X
q
j¼i
j2
0
if (mn ¼¼ 1) then
@hi
@b0
¼ 2
X
i1
k¼1
ðik þ Þk þ
X
p
k¼1
k @hik
@b0
Hði  kÞ
Appendix H
411

end if
For j ¼ 1 to nreg
@hi
@bj
¼ 2
X
i1
k¼1
ðik þ ÞkX j
ik þ
X
p
k¼1
k @hik
@bj
Hði  kÞ
Next j
Store the current values of hi and @hi=@ and keep all the previous values of hi and
@hi=@.
For k ¼ 1 to npar þ 1
@LðÞ
@k
¼ @LðÞ
@k
 1
2hi
2
i
hi
 1


@hi
@k
Next k
if (mn ¼¼ 1) then
@LðÞ
@b0
¼ @LðÞ
@b0
 i
hi
 1
2hi
2
i
hi
 1


@hi
@b0
end if
For k ¼ 1 to nreg
@LðÞ
@bk
¼ @LðÞ
@bk
 Xk
i i
hi
 1
2hi
2
i
hi
 1


@hi
@bk
Next k
Next i
Algorithm for the remaining terms of the sequence:
For i ¼ q þ 1 to num
@hi
@0
¼ 1 þ
X
p
k¼1
k @hik
@0
For j ¼ 1 to q
@hi
@j
¼
X
p
k¼1
k @hik
@j
Next j
For j ¼ 1 to p
@hi
@j
¼ hij þ
X
p
k¼1
j @hik
@k
Next j
412
Appendix H

@hi
@ ¼ @hi
@ þ
X
q
j¼1
2ðij þ Þj þ
X
p
k¼1
k @hik
@
hi ¼ 0 þ
X
p
k¼1
hikk þ
X
q
j¼1
jðij þ Þ2
if (mn ¼¼ 1) then
@hi
@b0
¼ 2
X
q
k¼1
ðik þ Þk þ
X
p
k¼1
k @hik
@b0
Hði  kÞ
end if
For j ¼ 1 to nreg
@hi
@bj
¼ 2
X
q
k¼1
ðik þ ÞkXj
ik þ
X
p
k¼1
k @hik
@bj
Hði  kÞ
Next j
Store the current values of hi and @hi=@ and keep Np previous values of hi and
@hi=@.
For k ¼ 1 to npar þ 1
@LðÞ
@k
¼ @LðÞ
@k
 1
2hi
2
i
hi
 1


@hi
@k
Next k
if (mn ¼¼ 1) then
@LðÞ
@b0
¼ @LðÞ
@b0
 i
hi
 1
2hi
2
i
hi
 1


@hi
@b0
end if
For k ¼ 1 to nreg
@LðÞ
@bk
¼ @LðÞ
@bk
 Xk
i i
hi
 1
2hi
2
i
hi
 1


@hi
@bk
Next k
Next i
H.2
STUDENT’S t DISTRIBUTION
H.2.1
The log likelihood
Deal with the first q terms of the sequence:
 ¼ ^
LðÞ ¼ 0
M
 ¼ logððð
 þ 1Þ=2ÞÞ  logðð
=2ÞÞ  1
2 logð
  2Þ
Appendix H
413

For i ¼ 1 To num
If (mn ¼ ¼ 1)
i ¼ yi  XT
i ^b
If (mn ¼ ¼ 0)
i ¼ yi  ^b0  XT
i ^b
Next i
For i ¼ 1 To q
hi ¼ 0 þ
X
i1
j¼1
jðij þ Þ2 þ
X
q
j¼i
j2
0 þ
X
p
k¼1
hikk
Store the current value of hi and keep all the previous values of hi.
LðÞ ¼ LðÞ  M
 þ 1
2 logðhiÞ þ 
 þ 1
2
log 1 þ
2
t
ð
  2Þhi


Next i
Deal with the remaining terms of the sequence:
For i ¼ q þ 1 To num
hi ¼ 0 þ
X
q
j¼1
jðij þ Þ2 þ
X
p
k¼1
khik
Store the current value of hi and keep Np previous values of hi.
LðÞ ¼ LðÞ  M
 þ 1
2 logðhiÞ þ 
 þ 1
2
log 1 þ
2
t
ð
  2Þhi


Next i
H.2.2
The first derivatives of the log likelihood
Algorithm for the first q terms of the sequence:
@LðÞ
@k
¼ 0;
k ¼ 1; . . . ; Np
For i ¼ 1 to q
Compute hi as described in Section H.2.1. Also calculate the derivatives @hi=@j,
j ¼ 1, . . . , Np as described for a Gaussian distribution in Section H.1.2.
Store hi and @hi=@j, j ¼ 1, . . . , Np, and keep all the previous values of hi and @hi=@.
Set
G ¼
ð
 þ 1Þ
ð
  2Þ þ ð2
i =hiÞ


For k ¼ 1 to npar þ 1
414
Appendix H

@LðÞ
@k
¼ @LðÞ
@k
 1
2hi
1  2
i
hi
G


@hi
@k
Next k
@LðÞ
@
¼ @LðÞ
@
 1
2  
 þ 1
2


þ 1
2  
2
 
þ
1
2ð
  2Þ
þ 1
2 log 1 þ
2
i
ð
  2Þhi



2
i
2ð
  2Þhi
G
if (mn ¼¼ 1) then
@LðÞ
@b0
¼ @LðÞ
@b0
 i
hi
G  1
2hi
2
i
hi
G  1


@hi
@b0
end if
For k ¼ 1 to nreg
@LðÞ
@bk
¼ @LðÞ
@bk
 Xk
i i
hi
G  1
2hi
2
i
hi
G  1


@hi
@bk
Next k
Next i
Algorithm for the remaining terms of the sequence:
For i ¼ qþ1 to num
Compute hi as described in Section H.2.1. Also calculate the derivatives @hi=@j,
j ¼ 1, . . . , Np as described for a Gaussian distribution in Section H.1.2.
Store hi and @hi=@j, j ¼ 1, . . . , Np, and keep Np previous values of hi and @hi=@.
Set
G ¼
ð
 þ 1Þ
ð
  2Þ þ ð2
i =hiÞ


For k ¼ 1 to npar þ 1
@LðÞ
@k
¼ @LðÞ
@k
 1
2hi
1  2
i
hi
G


@hi
@k
Next k
@LðÞ
@
¼ @LðÞ
@
 1
2  
 þ 1
2


þ 1
2  
2
 
þ
1
2ð
  2Þ
þ 1
2 log 1 þ
2
i
ð
  2Þhi



2
i
2ð
  2Þhi
G
Appendix H
415

if (mn ¼¼ 1) then
@LðÞ
@b0
¼ @LðÞ
@b0
 i
hi
G  1
2hi
2
i
hi
G  1


@hi
@b0
end if
For k ¼ 1 to nreg
@LðÞ
@bk
¼ @LðÞ
@bk
 Xk
i i
hi
G  1
2hi
2
i
hi
G  1


@hi
@bk
Next k
Next i
416
Appendix H

Appendix I
The general error distribution
This section proves various relations for the general error distribution.
The density function for the general error distribution is:
f ðiÞ ¼ K exp  1
2
i



a


;
where
K ¼
a
2ð1þ1=aÞð1=aÞ
ðI:1Þ
I.1
VALUE OF  FOR VARIANCE hi
Calculation of the scale factor  required for a general error distribution with mean
zero and variance hi.
The variance of the distribution, Eð2
i Þ, is given by:
Eð2
i Þ ¼ K
Z 1
1
2
i exp  1
2
i



a


di ¼ 2K
Z 1
0
2
i exp  1
2
i

 a


di
Using the standard integrals in Appendix K.1 with n ¼ 2, p ¼ a and b ¼ 1=2(1=)a
gives:
hi ¼ 2K
a  3
a
 
1
2
1

 a

3=a
Which after some simplification yields:
hi ¼ 2K23=a3
a
 3
a
 
Substituting for K and simplifying then gives:
hi ¼ 222=a  3=a
ð
Þ
 1=a
ð
Þ
The required value of  is therefore:
 ¼
hi22=a  1=a
ð
Þ
 3=a
ð
Þ

1=2
I.2
THE KURTOSIS
Eð4
i Þ ¼ K
Z 1
1
4
i exp  1
2
i



a


di
¼ 2K
Z 1
0
4
i exp  1
2
i

 a


di

However from standard mathematical tables:
Z 1
0
4
i exp bp
i
ð
Þ ¼ ðkÞ
pbk
where p ¼ a, b ¼ ð1=2Þ 1=
ð
Þa and k ¼ 5=a which gives:
E½4
i 	 ¼ 2K25=a5
a
 5
a
 
¼ 22=a2hi ð5=aÞ
ð3=aÞ
From Appendix I.1 we have:
E½2
i 	 ¼ hi ¼ 2K23=a3
a
 3
a
 
and
2 ¼ hi22=að1=aÞ
ð3=aÞ
Therefore:
E½4
i 	 ¼ h2
i
ð5=aÞð1=aÞ
ð3=aÞð3=aÞ
Which gives the kurtosis as:
@ ¼
E½4
i 	
ðE½2
i 	Þ2 ¼ h2
i
h2
i
ð5=aÞð1=aÞ
ð3=aÞð3=aÞ ¼ ð5=aÞð1=aÞ
ð3=aÞð3=aÞ
I.3
THE DISTRIBUTION WHEN THE SHAPE PARAMETER, a IS VERY LARGE
If the distribution has variance hi then, from Appendix I.1:
 ¼
22=að1=aÞhi
ð3=aÞ

1=2
Now for 0 < x < 1 we have ð1 þ xÞ ¼ 1 þ a1x þ a2x2 þ a3x3 þ    þ, where the
coefficients are jaij < 1, see Abramowitz and Stegun (1968).
Since xðxÞ ¼ ð1 þ xÞ we have, so to third order in x:
xðxÞ ¼ 1 þ a1x þ a2x2 þ a3x3
This gives ðxÞ ¼ ð1=xÞ þ a1 þ a2x þ a3x2, and ðxÞ  1=x as x!0.
So as a!1 we have the following:
2ð1þ1=aÞ  2;
22=a  1;
1
ð1=aÞ  1
a ;
ð1=aÞ
ð3=aÞ  3a
a ¼ 3;
and
ð5=aÞ
ð3=aÞ  3a
5a ¼ 3
5
The kurtosis is then:
@ ¼ ð5=aÞð1=aÞ
ð3=aÞð3=aÞ ¼ 9
5
418
Appendix I

Also as a!1   ð3hiÞ1=2, and for the range ð3hiÞ1=2 < i < ð3hiÞ1=2, we have:
i



a

i
ð3hiÞ1=2

  0
and therefore
exp  1
2
i



a


 1
Substituting the above results into Equation I.1 the probability density function
reduces to:
f ðiÞ 
1
2ð3hiÞ1=2
which is a uniform distribution Uðð3hiÞ1=2, ð3hiÞ1=2Þ, with lower limit ð3hiÞ1=2 and
upper limit ð3hiÞ1=2.
Appendix I
419

Appendix J
The Student’s t distribution
J.1
THE KURTOSIS
This section derives an expression for the kurtosis of the Student’s t distribution.
Since the Student’s t distribution density function is:
f ðiÞ ¼ K 1 þ
2
i
hið  2Þ

ðþ1Þ=2
where
K ¼ ðð þ 1Þ=2Þð  2Þ1=2h1=2
i
1=2ð=2Þ
we have:
E½2
i  ¼ 2K
Z 1
0
2
i di
1 þ 2
i =ðhið  2ÞÞ
ð
Þðþ1Þ=2
¼ 2K hið  2Þ
ð
Þðþ1Þ=2
Z 1
0
2
i di
ðhið  2Þ þ 2
i Þðþ1Þ=2
Using the standard integrals in Appendix K with a ¼ 2, b ¼ 2, c ¼ ( þ 1)=2 and
m ¼ (  2)hi gives:
mðaþ1bcÞ=b
b
¼ hið  2Þ
ð
Þð2Þ=2
2
;
 a þ 1
b


¼ ð3=2Þ;
 c  a þ 1
b


¼    2
2


;
ðcÞ ¼   þ 1
2


This gives
E½2
i  ¼ 2K hið  2Þ
ð
Þðþ1Þ=2
hið  2Þ
ð
Þð2Þ=2
ffiffiffi
p ðð  2Þ=2Þ
4ðð þ 1Þ=2Þ
(
)
Substituting for K and simplifying we obtain:
E½2
i  ¼ hið  2Þðð  1Þ=2Þ
ð=2Þ

But
  2
2


   2
2


¼    1
2
þ 1


¼  
2
	 
So
E½2
i  ¼ hið  2Þð=2Þ
2ð  2Þð=2Þ ¼ hi
Similarly we have:
E½4
i  ¼ 2K
Z 1
0
4
i di
1 þ 2
i =ðhið  2ÞÞ
ð
Þðþ1Þ=2
¼ 2K hið  2Þ
ð
Þ
ðþ1Þ
2
Z 1
0
4
i di
ðhið  2Þ þ 2
i Þðþ1Þ=2
Using the standard integrals in Appendix K with: a ¼ 4, b ¼ 2, c ¼ ( þ 1)=2 and
m ¼ (  2)hi gives:
mðaþ1bcÞ=b
b
¼ hið  2Þ
ð
Þð4Þ=2
2
;
 a þ 1
b


¼ ð5=2Þ;
 c  a þ 1
b


¼    4
2


;
ðcÞ ¼   þ 1
2


and
E½4
i  ¼ 2K hið  2Þ
ð
Þðþ1Þ=2
hið  2Þ
ð
Þð4Þ=23
ffiffiffi
p ðð  4Þ=2Þ
8ðð þ 1Þ=2Þ
(
)
Substituting for K and simplifying we obtain:
E½4
i  ¼ 3hið  2Þ2ðð  4Þ=2Þh2
i
4ð=2Þ
But
  4
2


   4
2


¼    2
2


and
  2
2


   2
2


¼  
2
	 
Therefore:
   4
2


¼
4ð=2Þ
ð  4Þð  2Þ
Appendix J
421

So
E½4
i  ¼ 3ð  2Þ24ð=2Þh2
i
4ð=2Þð  4Þð  2Þ ¼ 3ð  2Þh2
i
ð  4Þ
The kurtosis is then:
@ ¼
E½e4
i 
ðE½e2
i Þ2 ¼ 3ð  2Þh2
i
ð  4Þh2
i
¼ 3ð  2Þ
ð  4Þ
ðJ:1Þ
422
Appendix J

Appendix K
Mathematical reference
K.1
STANDARD INTEGRALS
Here we quote some useful standard integrals, see for example Beyer (1982).
Z 1
0
y exp ay2


dy ¼ 1
2
Z 1
0
y2 exp ay2


dy ¼ 1
4a
ffiffiffi

a
r
Z 1
0
y4 exp ay2


dy ¼ 3
8a2
ffiffiffi

a
r
Z 1
0
y2n exp ay2


dy ¼ 1  3  5    ð2n  1Þ
2nþ1an
ffiffiffi

a
r
Z 1
0
n
i exp b p
i
ð
Þ ¼ ðkÞ
pbk ;
where n > 1; p > 0; b > 0
and
k ¼ ðn þ 1Þ
p
Z 1
0
a
i di
ðm þ b
i Þc ¼ mðaþ1bcÞ=b
b
 ða þ 1Þ=b
ð
Þ c  ða þ 1Þ=b
ð
Þ
ðcÞ
where a > 1, b > 0, m > 0, and c > (a þ 1)=b.
K.2
GAMMA FUNCTION
ð1 þ xÞ ¼ x!
xðxÞ ¼ ðx þ 1Þ
 1
2
 
¼
ffiffiffi
p
 3
2
 
¼
ffiffiffi
p
2
 5
2
 
¼ 3
ffiffiffi
p
4
@ðxÞ
@x
¼  ðxÞ

For 0 
 x 
 1 we have
ð1 þ xÞ ¼ 1 þ a1x þ a2x2 þ a3x3 þ a4x4 þ a5x5
where a1 ¼ 0:5748, a2 ¼ 0:9512, a3 ¼ 0:6998, a4 ¼ 0:4245, and a5 ¼ 0:1010:
K.3
THE CUMULATIVE NORMAL DISTRIBUTION FUNCTION
In this section we show that the cumulative normal distribution function, N1(x), is
related to the complementary error function, erfc(x), by the following equation:
N1ðxÞ ¼ 1
2 erfcðx=
ffiffi
2
p
Þ
ðK:1Þ
If we let the error function be represented by erf(x) then we have:
erfðxÞ ¼ 2ffiffiffi
p
Z 1
0
expðt2Þdt
Now we have the following:
erfcðxÞ ¼ 1  erfðxÞ;
erfðxÞ ¼ erfðxÞ;
erfð1Þ ¼ 1
and
erfcðxÞ ¼ 2  erfcðxÞ
We will consider the integral
IðxÞ ¼ 2ffiffiffi
p
Z x
1
expðt2Þdt ¼ 2ffiffiffi
p
Z 0
1
expðt2Þdt þ 2ffiffiffi
p
Z x
0
expðt2Þdt
Since
2ffiffiffi
p
Z 0
1
expðt2Þdt ¼ 1
We therefore have
IðxÞ ¼ 1 þ erfðxÞ ¼ 1 þ 1  erfcðxÞ
f
g ¼ 2  erfcðxÞ
Substituting for erfc(x) we obtain:
IðxÞ ¼ 2  2  erfcðxÞ
f
g ¼ erfcðxÞ
So we have
erfcðxÞ ¼ 2ffiffiffi
p
Z x
1
expðt2Þdt
ðK:2Þ
Now the cumulative normal distribution is defined as
N1ðxÞ ¼
1ffiffiffiffiffi
2
p
Z x
1
expðt2Þdt
Letting u ¼ t
ffiffi
2
p
, we have du ¼
ffiffi
2
p
dt and for the upper limit we have x ¼ t
ffiffi
2
p
or
t ¼ x=
ffiffi
2
p
.
424
Appendix K

This integral becomes
N1ðxÞ ¼
1ffiffiffiffiffi
2
p
Z t¼x= ffiffi
2
p
1
expðt2Þ
ffiffi
2
p
dt
ðK:3Þ
So from Equation K.2 we have
N1ðxÞ ¼ 1
2 erfcðx=
ffiffi
2
p
Þ
QED
K.4
ARITHMETIC AND GEOMETRIC PROGRESSIONS
K.4.1
Arithmetic progression
The sum of the first n terms of an arithmetic progression is:
sn ¼ n
2 2a1 þ ðn  1Þd
f
g
ðK:4Þ
where a1 is the first term, and d is the common difference; that is the terms in the
sequence are: a1, a1 þ d, a1 þ 2d, a1 þ 3d, . . .
K.4.2
Geometric progression
The sum of the first n terms of geometric progression is:
sn ¼ a1ð1  r nÞ
1  r
ðK:5Þ
where a1 is the first term, and r is the common ratio; that is the terms in sequence are:
a1, a1r, a1r2, a1r3, . . .
Appendix K
425

Appendix L
The stability of the Black–Scholes
finite-difference schemes
L.1
THE GENERAL CASE
In this section we consider the stability of the finite-difference schemes described in
Part II Section 10.6.4. It is assumed that the grid contains ns asset points, and we will
denote the time dependent option values at the ith and (i þ 1)th time instants by the
ns2 element vectors Xi and Xiþ1 respectively. We can therefore write:
T1Xi ¼ T2Xiþ1
ðL:1Þ
where T1 and T2 are ns2  ns2 tridiagonal matrices, and xi
k, k ¼ 1, . . . , ns2 will be
used to denote the elements of the vector Xi.
The option values at the ith time instant are computed from those at the (i þ 1)th
time instant by using
Xi ¼ T1
1 T2Xiþ1
ðL:2Þ
However Equation L.2 is only stable if the eigenvalues of the ns2  ns2 matrix
T1
1 T2 all have modulus less than one, see Smith (1985).
L.2
THE LOG TRANSFORMATION AND A UNIFORM GRID
We will now prove that the implicit finite-difference method, m ¼ 0, when used on
the log transformed Black–Scholes equation with a uniform grid is unconditionally
stable; which means that the stability does not depend on the values of , t,
Z, etc.
From Part II Section 10.6.4 the finite-difference scheme is described by the follow-
ing tridiagonal system:
B
C
0
0
0
0
A
B
C
0
0
0
0
0
:
:
0
0
0
0
0
:
:
0
0
0
0
A
B
C
0
0
0
0
A
B
0
B
B
B
B
B
B
B
B
B
@
1
C
C
C
C
C
C
C
C
C
A
xi
1
xi
2
:
:
xi
s1
xi
s2
0
B
B
B
B
B
B
B
B
B
B
@
1
C
C
C
C
C
C
C
C
C
C
A
¼
B
C
0
0
0
0
A
B
C
0
0
0
0
0
:
:
0
0
0
0
0
:
:
0
0
0
0
A
B
C
0
0
0
0
A
B
0
B
B
B
B
B
B
B
B
B
B
@
1
C
C
C
C
C
C
C
C
C
C
A
xiþ1
1
xiþ1
2
:
:
xiþ1
s3
xiþ1
s2
0
B
B
B
B
B
B
B
B
B
B
@
1
C
C
C
C
C
C
C
C
C
C
A

where
A ¼ ð1  mÞt
2Z2
fbZ  2g
ðL:3Þ
B ¼ 1 þ ð1  mÞt r þ 2
Z2


ðL:4Þ
C ¼  ð1  mÞt
2Z2
fbZ þ 2g
ðL:5Þ
A ¼  mt
2Z2 fbZ  2g
ðL:6Þ
B ¼ 1  mt r þ 2
Z2


ðL:7Þ
C ¼ mt
2Z2 fbZ þ 2g
ðL:8Þ
As in Part II Section 10.6, b ¼ r  q  (2=2) and r > 0.
Substituting m ¼ 0 into Equations L.3 to L.8 we have A ¼ C ¼ 0, B ¼ 1 and
A ¼
t
2Z2 fbZ  2g;
B ¼ 1 þ t r þ 2
Z2


;
C ¼ 
t
2Z2 fbZ þ 2g
The finite-difference scheme is thus represented by the equations
B
C
0
0
0
0
A
B
C
0
0
0
0
0
:
:
0
0
0
0
0
:
:
0
0
0
0
A
B
C
0
0
0
0
A
B
0
B
B
B
B
B
B
B
B
B
@
1
C
C
C
C
C
C
C
C
C
A
xi
1
xi
2
:
:
xi
s1
xi
s2
0
B
B
B
B
B
B
B
B
B
@
1
C
C
C
C
C
C
C
C
C
A
¼
1
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
:
:
0
0
0
0
0
:
:
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
1
0
B
B
B
B
B
B
B
B
B
@
1
C
C
C
C
C
C
C
C
C
A
xiþ1
1
xiþ1
2
:
:
xiþ1
s3
xiþ1
s2
0
B
B
B
B
B
B
B
B
B
@
1
C
C
C
C
C
C
C
C
C
A
or in matrix notation
Xi ¼ T1
1 Xiþ1
ðL:9Þ
where T2 ¼ I in Equation L.2.
As mentioned in Section L.1, Equation L.9 is stable if the modulus of all the
eigenvalues of T1
1
are less than one. We will now show that this is in fact the case.
If the eigenvalues of T1 are k, k ¼ 1, . . . , ns2, then the eigenvalues of T1
1
are
1
k , k ¼ 1, . . . , ns2. This means that the system is stable if all the eigenvalues of
T1 have a modulus greater than one. This result can be proved by considering
the eigenvalue with the smallest modulus, min. If jminj > 1 then the result is
proved.
Appendix L
427

Now the eigenvalues of T1, see Smith (1985), are given by:
k ¼ 1 þ t r þ 2
Z2
	

þ 2
ffiffiffiffiffiffiffi
AC
p
cos
k
ns2 þ 1
	

;
k ¼ 1; . . . ; ns2
ðL:10Þ
where the term
2
ffiffiffiffiffiffiffi
AC
p
¼
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
t2ð4  b2Z2Þ
Z4
r
ðL:11Þ
It can be seen that if b2Z2 > 4 then the eigenvalues are complex and if
4  b2Z2 then eigenvalues are real. We will consider each of these cases in turn.
L.2.1
Complex eigenvalues: b2Z 2 > 4
We will represent the kth complex eigenvalue as:
k ¼ R þ iY
where the real part is
R ¼ 1 þ t r þ 2
Z2
	

and the imaginary part is
Y ¼ 2
ffiffiffiffiffiffiffi
AC
p
cos
k
ns2 þ 1
	

Since
jkj > jRj þ jYj
and
jRj > 1
we conclude that
jminj > 1
L.2.2
Real eigenvalues: 4  b2Z 2
In this case the kth eigenvalue is real, and from Equation L.10 we have:
k > 1 þ t r þ 2
Z2
	

 2
ffiffiffiffiffiffiffi
AC
p
Since b22 > 0 from Equation L.11 we have
2
ffiffiffiffiffiffiffi
AC
p
<
ffiffiffiffiffiffiffiffiffiffiffiffi
4t2
Z4
r
or
2
ffiffiffiffiffiffiffi
AC
p

 < 2t
Z2
So
min > 1 þ t r þ 2
Z2
	

 2t
Z2
Therefore we have
jminj > 1 þ rt
and since r > 0; we have:
jminj > 1
428
Appendix L

Glossary of terms
The notation used is as follows:
 ðxÞ
The psi function, also called the digamma function, ð@ðlog ðxÞÞÞ=@x ¼  ðxÞ
ðxÞ
The gamma function. If x is an integer then ðxÞ ¼ ðn  1Þ!
logðxÞ
The natural logarithm of x.
EðxÞ
The conditional expectation value of x.
E½x
The unconditional expectation value of x.
NIDða; bÞ
Normally and independently distributed variates, with mean a and variance b.
Rða; bÞ
An arbitrary distribution, with mean a and variance b.
IIDða; bÞ
Independently and identically distributed, with lower limit a and upper limit b.
Uða; bÞ
The uniform distribution, with lower limit a and upper limit b.
OLS
Ordinary least squares.
jxj
The absolute value of the variable x.
PDF
The probability density function of a given distribution.
DLðÞ
ð@LðÞÞ=@
D2LðÞ
ð@2LðÞÞ=@2
Leptokurtic
The distribution has a kurtosis greater than 3. This implies that the tails of the
distribution are thicker than those of a Gaussian.
Platykurtic
The distribution has a kurtosis less than 3. This implies that the tails of the
distribution are thinner than those of a Gaussian.
^
The vector of estimated GARCH model parameters.
^i
The estimated value of the ith GARCH model parameter.

Computing reading list
Ammeraal, L. (2001) Cþþ for Programmers, Third Edition, Wiley.
Barwell, F. et al. (2002) Professional VB.NET, Second Edition, Wrox Press.
Birbeck, M. (2001) Professional XML, Second Edition, Wrox Press Ltd.
Black, F. and Scholes, M. (1973) The pricing of corporate liabilities, Journal of Political
Economy, 81, 637–657.
Box, D. (1998) Essential COM, Addison-Wesley.
Brockschmidt, K. (1995) Inside OLE, Microsoft Press.
Cagle, K. et al. (2001) Professional XSL, Wrox Press Ltd.
Challa, S. and Laksberg, A. (2002) Essential Guide to Managed Extensions for Cþþ, Apress.
Conard, J. et al. (2000) Introducing .NET, Wrox Press Ltd.
Darnell, R. et al. (1998) HTML 4 Unleashed, Sams.net.
Denning, A. (1997) ActiveX Controls Inside Out, Microsoft Press.
Ellis, M. A. and Stroustrup, B. (1990) The Annotated Cþþ Reference Manual, Addison-Wesley.
Flowers, B. H. (1995) An Introduction to Numerical Methods in Cþþ, Clarendon Press,
Oxford.
Hull, J. C. (1997) Options Futures and Other Derivatives, Prentice Hall.
Inprise Corporation (1998) Delphi 4, Inprise Corporation.
Koenig, A. and Moo, B. E. (2000) Accelerated Cþþ, Addison-Welsey.
Kruglinski, D., Shepherd, G. and Wingo, S. (1998) Programming Microsoft Visual Cþþ,
Microsoft Press.
Levy, G. F. (1997) Mathematics, Visual Systems Journal, 3, 28–36.
Levy, G. F. (1997) Mathematics part II, Visual Systems Journal, 4, 26–35.
Levy, G. F. (1997) Summing up, Visual Systems Journal, 6, 6–8.
Levy, G. F. (1998) Calling 32-bit NAG C DLL Functions from Visual Basic 5 and Microsoft
Office, NAG Technical Report, TR2/98.
Levy, G. F. (2001) Numeric ActiveX components, Software – Practice and Experience, 31,
1–43; 31(2), 147–189.
Levy, G. F. (2003) Wrapping C with Cþþ in .NET, C/Cþþ Users Journal.
Markowitz, H. M. (1994) The general mean-variance portfolio selection problem, Phil. Trans.
R. Soc. Lond. A, 347, 543–549.
Meyers, S. (1996) More Effective Cþþ, Addison-Wesley.
Meyers, S. (1998) Effective Cþþ, Second Edition, Addison-Wesley.
Meyers, S. (2001) Effective STL, Addison-Wesley.
Microsoft Corporation (1995) Excel/Visual Basic Programmers Guide, Microsoft Corporation.
Microsoft Corporation (1996) ActiveX Control Pad, Microsoft Corporation.
Microsoft Corporation (1997) Visual Basic 5, Component Tools Guide, Microsoft Corporation.
NAG Ltd (2001) The Fortran 77 Library Mark 20, NAG Ltd, Oxford.
NAG Ltd (2002) The C Library Mark 7, NAG Ltd, Oxford.

NAG Ltd (2003) The NAG C Library Mark 7, NAG Ltd.
O’Brien, T. M., Pogge, S. J. and White, G. E. (1997) Microsoft Access 97 Developer’s Hand-
book, Microsoft Press.
Petroutsos, B., Schongar, E. et al. (1997) VBScript Unleashed, Sams.net.
Rebonato, R. (1998) Interest-rate Option Models, Second Edition, John Wiley.
Robinson, S. et al. (2001) Professional C#, Wrox Press Ltd.
Rogerson, D. (1997) Inside COM, Microsoft Press.
Stroustrup, B. (1991) The Cþþ Programming Language, Second Edition, Addison-Wesley.
Computing reading list
431

Mathematics and finance references
REFERENCES
Abramowitz, M. and Stegun, I. A. (1968) Handbook of Mathematical Functions, Dover Pub-
lications.
Aitchison, J. and Brown, J. A. C. (1966) The Lognormal Distribution, Cambridge University
Press.
Alexander, C. O. (2000) A Primer on the Orthogonal GARCH Model, ISMA Centre, University
of Reading.
Andersen, L. B. G. and Brotherton-Ratcliffe, R. (1998) The equity option volatility smile: an
implicit finite-difference approach, Journal of Computational Finance, 1(2), 5–37.
Anderson, H. M., Nam, K. and Vahid, F. (1999) Asymmetric nonlinear smooth transition
GARCH models, in Nonlinear Time Series Analysis of Economic and Financial Data,
P. Rothman (ed.), Kluwer, Boston, 191–201.
Anderson, T. W. (1984) An Introduction to Multivariate Statistical Analysis, Second Edition,
Wiley, New York.
Bachelier, L. (1900) Theory de la speculation, Ann. Sci. Ecole. Norm. Sup., 17, 21–86.
Barle, S. and Cakici, N. (1995) Growing a smiling tree, Risk, 8(10), October, 76–81.
Barndorff-Nielsen, O. E. (1977) Exponentially decreasing distributions for the logarithm of
particle size, Proceedings of the Royal Society of London A, 353, 401–419.
Barndorff-Nielsen, O. E. (1998) Processes of normal inverse Gaussian type, Finance and
Stochastics, 2, 41–68.
Barndorff-Nielsen, O. E. and Halgreen, O. (1977) Infinite divisibility of the hyperbolic and
generalized inverse Gaussian distributions, Zeitschrift fur Wahrscheinlichkeitstheorie und
verwandte Gebiete, 38, 309–312.
Barone-Adesi, G. and Whaley, R. E. (1987) Efficient analytic approximation of American
option values, The Journal of Finance, 42(2), 301–320.
Barraquand, J. and Martineau, D. (1995) Numerical valuation of high dimensional multi-
variate American securities, Journal of Financial and Quantitative Analysis, 30, 383–405.
Beale, E. M. L. and Little, R. J. A. (1975) Missing values in multivariate analysis, J. R. Stat.
Soc., 37, 129–145.
Berndt, E. K., Hall, B. H., Hall, R. E. and Hausman, J. A. (1974) Estimation and inference in
nonlinear structural models, Annals of Economic and Social Measurement, 3(4), 653–665.
Beyer, W. H. (1982) CRC Standard Mathematical Tables, CRC Press, Florida.
Black, F. (1975) Fact and fantasy in the use of options and corporate liabilities, Financial
Analysts Journal, 31, 36–41, 61–72.
Black, F. (1976) Studies in stock price volatility changes, Proceedings of the 1976 Business Meeting
of Business and Economics Statistics Section, American Statistical Association, 177–181.

Black, F. and Scholes, M. (1973) The pricing of corporate liabilities, Journal of Political
Economy, 81, 637–657.
Bollerslev, T. P. (1987) A conditionally heteroskedastic time series model for speculative prices
and rates of return, Review of Economics and Statistics, 69, 542–547.
Box, G. E. P. and Jenkins, G. M. (1976) Time Series Analysis: Forecasting and Control,
Holden-Day, San Francisco.
Box, G. E. P. and Muller, M. E. (1958) A note on the generation of random normal deviates,
Ann. Math. Stat., 29, 610–611.
Boyle, P. P. and Tian, Yisong (1998) An explicit finite difference approach to the pricing of
barrier options, Applied Mathematical Finance, 5, 17–43.
Boyle, P. P., Broadie, M. and Glasserman, P. (1997) Monte Carlo methods for security pricing,
Journal of Economic Dynamics and Control, 21, 1267–1321.
Boyle, P. P., Evnine, J. and Gibbs, S. (1989) Numerical evaluation of multivariate contingent
claims, The Review of Management Studies, 2(2), 241–250.
Broadie, M. and DeTemple, J. (1996) American option valuation: new bounds, approxima-
tions, and a comparison of existings methods, The Review of Financial Studies, 9(4),
1211–1250.
Broadie, M. and Glasserman, P. (1997) Pricing American-style securities using simulation,
Journal of Economic Dynamics and Control, 21, 1323–1352.
Brotherton-Ratcliffe, R. (1994) Monte Carlo Motoring, Risk, 7(12), 53–58.
Bunch, J. R. and Kaufman, L. C. (1980) A computational method for the indefinite quadratic
programming problem, Linear Algebra and its Applications, 34, 341–370.
Caflisch, R. E., Morokoff, W. and Owen, A. (1997) Valuation of mortgage-backed securities
using Brownian bridges to reduce effective dimension, The Journal of Computational
Finance, 1(1), 27–46.
Campbell, J. Y., Lo, A. W. and MacKinlay, A. C. (1997) The Econometrics of Financial
Markets, Princeton University Press.
Chan, T. F., Golub, G. H. and Leveque, R. J. (1982) Updating Formulae and a Pairwise
Algorithm for Computing Sample Variances, Compstat 1982, Physica-Verlag.
Chesney, M. and Scott, L. O. (1989) Pricing European currency options: a comparison of the
modified Black–Scholes model and a random variance model, J. Financial Quant. Anal.,
24, 267–284.
Chriss, N. (1996) Transatlantic trees, Risk, 9(7), 45–48.
Chriss, N. (1997) Black–Scholes and Beyond, IRWIN.
Clewlow, L. and Strickland, C. (1999) Implementing Derivative Models, John Wiley.
Cox, D. R. and Hinkley, D. V. (1979) Theoretical Statistics, Chapman and Hall.
Cox, J. C., Ross, S. A. and Rubinstein, M. (1979) Option pricing: a simplified approach,
Journal of Financial Economics, 7, 229–263.
Crank, J. and Nicolson, P. (1947) A practical method for numerical evaluation of solutions of
partial differential equations of the heat conduction type, Proc. Camb. Phil. Soc., 43, 50–67.
DeGroot, M. H. (1970) Optimal Statistical Decisions, McGraw-Hill, New York.
Dempster, A. P., Laird, N. M. and Rubin, D. B. (1977) Maximum likelihood from incomplete
data via the EM algorithm, J. R. Statist Soc. Series B, Methodological, 39, 1–22.
Derman, E. and Kani, I. (1994) Riding on a smile, Risk, 7(2), 32–39.
Dickey, J. M. (1967) Matricvariate generalizations of the multivariate t distribution and the
inverted t distribution, Ann. Math. Stat., 38(2), 511–518.
Ding, Z. (1994) Time Series Analysis of Speculative Returns, PhD dissertation, University of
California San Diego.
Mathematics and finance references
433

Dueker, M. J. (1997) Markov switching in GARCH processes and mean-reverting stock
market volatility, Journal of Business and Economic Statistics, 15, 26–34.
Duffie, D. and Singleton, K. J. (1989) Simulated Moment Estimation of Markov Models of
Asset Prices, Stanford Graduate School of Business.
Eberlein, E. (2001) Applications of generalized hyperbolic levy motion to finance, in Levy
Processes, Theory and Applications, O. E. Barndorff-Nielsen, T. Mikosch and S. I. Resnick
(eds), Birkhauser.
Einstein, A. (1905) On the movement of small particles suspended in a stationary liquid
demanded by the molecular-kinetic theory of meat, Ann. Physik, 17.
Engle, R. F. (1982) Autoregressive conditional heteroskedasticity with estimates of the var-
iance of United Kingdom inflation, Econometrica, 50, 987–1008.
Engle, R. F. (1995) ARCH selected readings, Advanced Texts in Econometrics, Oxford Uni-
versity Press.
Engle, R. F. and Bollerslev, T. P. (1986) Modelling the persistence of conditional variances,
Econometric Reviews, 5, 1–50.
Engle, R. F. and Gonzalez-Rivera (1991) Semiparametric ARCH models, Journal of Business
and Economics, 9, 345–360.
Engle, R. F. and Ng, V. (1993) Measuring and testing the impact of news on volatility, Journal
of Finance, 48, 1749–1777.
Engle, R. F., Lilien, D. M. and Robins, P. R. (1987) Estimating time varying risk premia in the
term structure: The ARCH-M model, Econometrica, 55, 391–407.
Evans, M., Hastings, N. and Peacock, B. (2000) Statistical Distributions, John Wiley, Third
Edition.
Faure, H. (1982) Discrepance de suites associees a un systeme de numeration (en dimensions),
Acta Arith., 41, 337–351.
Feller, W. (1971) An Introduction to Probability Theory and its Applications, II, John Wiley and
Sons.
Fiorentini, G., Calzolari, G. and Panattoni, L. (1996) Analytic derivatives and the computa-
tion of GARCH estimates, Journal of Applied Econometrics, 11, 399–417.
Fisher, R. A. (1925) Theory of statistical estimation, Proc. Cambridge Philos. Soc., 22, 700–725.
Forsberg, L. and Bollerslev, T. (2002) Bridging the GAP between distribution of realised
(ECU) volatility and ARCH modelling (of the EURO): the GARCH-NIG model, Journal
of Applied Econometrics, 17, 535–548.
Freedman, D. (1983) Brownian Motion and Diffusion, Springer-Verlag, New York.
Fu, M. C., Laprise, S. B., Madan, D. B., Su, Y. and Wu, R. (2001) Pricing American options: a
comparison of Monte Carlo simulation approaches, Journal of Computational Finance, 4(3),
39–88.
Geske, R. (1979) A note on an analytic valuation formulae for unprotected American call
options on stocks with known dividends, Journal of Econometrics, 7, 375–380.
Geske, R. and Johnson, H. E. (1984) The American put options valued analytically, Journal of
Finance, 39, 1511–1524.
Ghysels, E., Harvey, A. C. and Renault, E. (1996) Stochastic volatility, Handbook of Statistics
14:Statistic Methods in Finance, North-Holland, 119–191.
Gill, P. E., Murray, W. and Wright, M. H. (1981) Practical Optimization, Academic Press.
Glasserman, R. P., Heidelberger, P. and Shahabuddin, P. (2000) Variance reduction techniques
for value-at-risk with heavy-tailed risk factors, in Proceedings of the 2000 Winter Simulation
Conference, J. A. Joines, R. R. Barton, K. Kang and P. A. Fishwick (eds).
Glosten, L. and Milgrom, P. (1985) Bid, ask and transaction prices in a specialist market with
heterogeneously informed traders, Journal of Financial Economics 14, 71–100.
434
Mathematics and finance references

Glosten, L., Jagannathan, R. and Runkle, D. (1993) Relationship between the expected value
and the volatility of nominal excess return on stocks, Journal of Finance, 48, 1779–1801.
Goldberger, A. S. (1997) A Course in Econometrics, Havard University Press.
Golub, G. H. and Van Loan, C. F. (1989) Matrix Computation, The John Hopkins University Press.
Good, I. J. (1979) Computer generation of the exponential power distribution, Journal of
Statistical Computation and Simulation, 9(3), 239–240.
Granger, C. W. J. (2002) Some comments on risk, Journal of Applied Econometrics, 15, 447–456.
Hager, W. (1988) Applied Numerical Linear Algebra, Prentice Hall.
Hamilton, J. (1994) Time Series Analysis, Princeton University Press.
Harvey, A. (1990) The Econometric Analysis of Time Series, Philip Allan.
Harvey, A. C., Ruiz, E. and Shephard, N. (1994) Multivariate stochastic variance models,
Review of Economic Studies, 61, 247–264.
Hentschel, L. F. (1995) All in the family: nesting linear and nonlinear GARCH models,
Journal of Financial Economics, 39, 139–164.
Hull, J. C. (1997) Options Futures and Other Derivatives, Prentice Hall.
Hull, J. C. and White, A. (1994) Numerical procedures for implementing term structure models I,
The Journal of Derivatives, 2, 7–16.
Johnson, H. (1987) Options on the maximum or the minimum of several assets, Journal of
Financial and Quantitative Analysis, 22(3), 277–283.
Kamrad, B. and Ritchken, P. (1991) Multinomial approximating models for options with k
state variables, Management Science, 37(12), 1640–1652.
Karatzas, I. and Shreve, S. (1988) Brownian Motion and Stochastic Calculus, Springer-Verlag,
New York.
Levi, F. W. (1942) Algebra, University of Calcutta.
Levy, G. F. (2000) Software implementation and testing of GARCH models, NAG Technical
Report, TR4/2000, NAG Ltd, Oxford.
Levy, G. F. (2003) Analytic derivatives of asymmetric GARCH models, Journal of Computa-
tional Finance, 6(3).
Levy, P. (1939) Sur certain processus stochastiques homogenes, Compositio Math., 7, 283–339.
Levy, P. (1948) Processus Stochastiques et Mouvement Brownian, Gauthier-Villar, Paris.
Little, R. J. A. and Rubin, D. B. (1987) Statistical Analysis with Missing Data, John Wiley.
Lo, A. W. and MacKinlay, A. C. (1990) An econometric analysis of nonsynchronous-Trading,
Journal of Econometrics, 45, 181–212.
McIntyre, R. (1999) Black–Scholes will do, Energy & Power Risk Management, November, 26–27.
McKenzie, M. D., Mitchell, H., Brooks, R. D. and Faff, R. W. (2001) Power ARCH modelling
of commodities futures data on the London Metal Exchange, The European Journal of
Finance, 7, 22–28.
MacMillan, L. W. (1986) Analytic approximation for the American put option, Advances in
Futures and Options Research, 1, 119–139.
Marchuk, G. I. and Shaidurov, V. V. (1983) Difference Methods and their Extrapolations,
Springer-Verlag.
Mardia, K. V., Kent, J. T. and Bibby, J. (1988) Multivariate analysis, Probability and Math-
ematical Statistics, Academic Press, London.
Markowitz, H. M. (1989) Mean Variance Analysis in Portfolio Choice and Capital Markets,
Basil Blackwell.
Markowitz, H. M. (1994) The general mean-variance portfolio selection problem, Phil. Trans.
R. Soc. Lond. A., 347, 543–549.
Melino, A. and Turnbill, S. M. (1990) Pricing Foreign Currency Options with Stochastic
Volatility, J. Econometrics, 45, 239–265.
Mathematics and finance references
435

