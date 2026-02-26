# Numerical Methods for Option Pricing

!!! info "Source"
    **Computational Finance: Numerical Methods** by Clewlow and Strickland.
    These notes are used for educational purposes.

## Numerical Methods and American Options

Chapter 10
Numeric methods and single asset American
options
10.1
INTRODUCTION
In Chapter 9 we discussed single asset European options and the analytic formulae
which can be used to price them. Here we will consider the valuation of single asset
American style options using both numeric methods and analytic formulae; in
addition we will discuss the use of numerical techniques to value certain European
options. The coverage in this section is as follows:
. Analytic methods applied to perpetual European and American options.
. Analytic approximation techniques for the valuation of American options.
. Binomial lattice techniques used for the valuation of American and European
options.
. The valuation of American and European vanilla and barrier options using finite-
difference grids.
. The valuation of American options via Monte Carlo simulation.
It should be mentioned that although much of the discussion here concerns the
valuation of vanilla European and American puts and calls, the techniques used can
be modified without much difficulty to include more exotic options with customized
payoffs and early exercise features.
10.2
PERPETUAL OPTIONS
10.2.1
The perpetual American put
Here we derive the value, P(S, E), for a perpetual American put with strike price E on
an asset of current value S. This option can be exercised at any time, and so there is no
expiry date. Since the option is perpetual its payoff is time independent (see Merton
(1973)) and the Black–Scholes equation reduces to the following second order ordinary
differential equation:
2S2
2
d2V
dS2 þ ðr  qÞS dV
dS  rV ¼ 0
ð10:1Þ
where as usual S is the asset price, V is the option value,  is the volatility of the asset,
r is the riskless interest rate and q is the continuous dividend yield.

If we substitute S ¼ exp (X) we then have:
dV
dS ¼ dV
dX
dX
dS ¼ expðXÞ dV
dX
d2V
dS2 ¼ dX
dS
d
dX
dV
dX expðXÞ


¼ expð2XÞ d2V
dX2  dV
dX expð2XÞ
Substituting the above results into Equation 10.1 we obtain:
2 expð2XÞ expð2XÞ
2
d2V
dX2  dV
dX


þ ðr  qÞ expðXÞ expðXÞ dV
dX  rV ¼ 0
2
2
d2V
dX2 þ
ðr  qÞ  2
2


dV
dX  rV ¼ 0
So
d2V
dX2 þ
2ðr  qÞ
2
 1


dV
dX  2r
2 V ¼ 0
ð10:2Þ
Equation 10.2 is a homogeneous equation with constant coefficients, so we can look
for solutions of the form V ¼ exp (mX). This gives:
m2 þ
2ðr  qÞ
2
 1


m  2r
2 ¼ 0
ð10:3Þ
which can be solved to yield:
m1 ¼ 1
2
2ðr  qÞ
2
þ 1


þ 1
2
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
2ðr  qÞ
2
 1

2
þ 8r
2
s
ð10:4Þ
and
m2 ¼ 1
2
2ðr  qÞ
2
þ 1Þ


 1
2
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
2ðr  qÞ
2
 1

2
þ 8r
2
s
ð10:5Þ
The general solution to Equation 10.2 is therefore:
VðXÞ ¼ A1 expðm1XÞ þ A2 expðm2XÞ
ð10:6Þ
However, since we are solving Equation 10.1 we would like the solution in terms
of the asset price S. So re-substituting S ¼ exp (X), and using the fact that
exp (aX) ¼ exp (X)a, we obtain:
A1 expðm1XÞ ¼ A1ðexpðXÞÞm1 ¼ A1Sm1
and
A2 expðm2XÞ ¼ A2ðexpðXÞÞm2 ¼ A2Sm2
Numeric methods and single asset American options
117

The general solution of Equation 10.2 as a function of S is therefore:
VðSÞ ¼ A1Sm1 þ A2Sm2
ð10:7Þ
If we assume that (2(r  D)=2) > 1 then m1 > 0 and m2 < 0. (Note: When
(2(r  D)=2) < 1, m1 < 0 and m2 > 0.)
For the perpetual American put as S ! 1 we have P(S, E) ! 0. This means that
the coefficient A1 in Equation 10.7 must be zero, and P(S, E) ¼ A2Sm2. Suppose we
decide that we will exercise the option when S  S	, where S	 is termed the critical
value of S, then the payoff (which is positive) at S ¼ S	 will be
PðS	; EÞ ¼ E  S	
ð10:8Þ
This gives
PðS	; EÞ ¼ A2ðS	Þm2 ¼ E  S	
ð10:9Þ
Solving for A2 gives:
A2 ¼ E  S	
ðS	Þm2
ð10:10Þ
So we have:
PðS; EÞ ¼ ðE  S	Þ
S
S	

m2
ð10:11Þ
We are now going to find the value of S	 which maximizes the option value at any
time before exercise. Differentiating Equation 10.11 and setting the value to zero we
have:
@
@S	
ðE  S	Þ
S
S	

m2


¼ 1
S	
S
S	

m2
S	  m2ðE  S	Þ
f
g ¼ 0
and
S	  m2ðE  S	Þ ¼ 0;
so
S	 ¼
E
1  1=m2
So substituting into Equation 10.10 results in:
A2 ¼ 1
m2
E
1  1=m2

1m2
When there are no dividends, q ¼ 0, we have from Equation 10.5 that
m2 ¼ 1
2
2r
2 þ 1


 1
2
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
2r
2  1

2
þ 8r
2
s
ð10:12Þ
but
2r
2  1

2
þ 8r
2 ¼
1 þ 2r
2

2
118
Pricing Assets

Therefore
m2 ¼ 1
2
 2r
2 þ 1  2r
2  1


and
m2 ¼ 2r
2
ð10:13Þ
Substituting for m2 and A2 in Equation 10.9 we thus obtain the value for a perpetual
American put without dividends as:
PðS; EÞ ¼ 2S2r=2
2r
E
1 þ ð2=2rÞ

1þð2r=2Þ
ð10:14Þ
see Merton (1973), Equation 52, p. 174.
10.2.2
The perpetual American call
Here we derive the value, C(S, E), for a perpetual American call with strike price E
on an asset of current value S. For the perpetual American call as S ! 0 we have
C(S, E) ! 0. In the previous section we mentioned that m2 < 0 which means that the
A2Sm2 ! 1 as S ! 0. Thus if Equation 10.7 is to yield a finite solution for the
perpetual American call we must set A2 ¼ 0 and look for solutions of the form:
CðS; EÞ ¼ A1Sm1
The payoff for the call option is max (S  E, 0), so when S	 ¼ S we have:
CðS	; EÞ ¼ S	  E ¼ A1 S	
ð
Þm1
ð10:15Þ
and
A1 ¼ ðS	  EÞ
ðS	Þm1
ð10:16Þ
This gives
CðS; EÞ ¼ ðS	  EÞ
S
S	

m1
ð10:17Þ
As in Section 10.2.1 we find the value S	 which maximizes the option value by
differentiating Equation 10.17 w.r.t. S	 and setting the value to zero. This yields:
@
@S	
ðE  S	Þ
S
S	

m1


¼ 1
S	
S
S	

m1
S	  m1ðS	  EÞ
f
g ¼ 0
and
S	  m1ðS	  EÞ ¼ 0;
so
S	 ¼
E
1  1=m1
ð10:18Þ
Numeric methods and single asset American options
119

Now using A1 ¼ (S	  E)=(S	)m1 we obtain
A1 ¼
E 1=ð1  1=m1Þ  1
f
g
Em1 ð1  1=m1Þð1  1=m1Þm11
n
o
¼
1
Em11 ð1  1 þ 1=m1Þð1  1=m1Þm11
A1 ¼ 1
m1
1  1=m1
E

m11
¼ 1
m1
E
1  1=m1

1m1
ð10:19Þ
Therefore the value of the perpetual American call option is:
CðS; EÞ ¼ 1
m1
E
1  1=m1

1m1
Sm1
ð10:20Þ
When there are no dividends, q ¼ 0, we have from Equation 10.4 that
m1 ¼ 1
2
2r
2 þ 1


þ 1
2
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
2r
2  1

2
þ 8r
2
s
ð10:21Þ
but
2r
2  1

2
þ 8r
2 ¼
1 þ 2r
2

2
ð10:22Þ
so substituting into Equation 10.21 we obtain
m1 ¼ 1
2
 2r
2 þ 1 þ 2r
2 þ 1


¼ 1
ð10:23Þ
Setting m1 ¼ 1 in Equation 10.18 we thus find that S	 ¼ 1. Therefore from Equa-
tion 10.16:
A1 ¼ ðS	  EÞ
ðS	Þm1
¼ ðS	  EÞ
ðS	Þ
¼ 1
ð10:24Þ
This means that the value of a perpetual American call with zero dividends is:
CðS; EÞ ¼ A1Sm1 ¼ 1  S ¼ S
ð10:25Þ
10.2.3
Perpetual European options
We can easily derive expressions for perpetual European options by using the Black–
Scholes formulae given in Section 9.3.3. It can be seen that as the option maturity, , tends
to infinity d1!1 and d2!1. This means that for perpetual options we should use
N1(d1) 
 1 andN1(d2) 
 0 intheBlack–Scholesformulae. Therefore when q > 0, we have
c(S, E) 
 0 and p(S, E) 
 0. Also when q ¼ 0 we have c(S, E) 
 S and p(S, E) 
 0.
The value of a European call (when q ¼ 0) is therefore:
cðS; EÞ ¼ CðS; EÞ ¼ S
ð10:26Þ
which means that, when there are no dividends, the perpetual American call and the
perpetual European call options have the same value; the current asset price S.
120
Pricing Assets

10.2.4
Perpetual European down and out call
Here we find the value of a perpetual down and out European call barrier option, see
Merton (1973).
Let the exercise price be E and the barrier be at B where B < E.
Since the Black–Scholes partial differential equation governs the price of the
option we can, as before, look for solutions of the form:
cðS; EÞdo ¼ A1Sm1 þ A2Sm2
ð10:27Þ
subject to the boundary conditions: (i) cdo(B, E) ¼ 0 and (ii) c(1, E)do ¼ S, see the
previous section.
From (i) we have:
cdoðB; EÞ ¼ A1B m1 þ A2B m2 ¼ 0;
so
A1 ¼ A2B m2m1
Therefore
cdoðS; EÞ ¼ A2B m2m1Sm1 þ A2Sm2
From (ii), as S ! 1:
cdoðS; EÞ ¼ A2B m2m1Sm1 þ A2Sm2 ¼ S
However, since m2 < 0, we have A2Sm2 ! 0, as S ! 1, giving
cdoðS; EÞ ¼ A2B m2m1Sm1 ¼ S
So
A2 ¼  S1m1
Bm2m1
and
cdoðS; EÞ ¼ S1m1Sm1Bm2m1
Bm2m1
 S1m1Sm2
Bm2m1
which results in:
cdoðS; EÞ ¼ S  S1þm2m1
Bm2m1
ð10:28Þ
When there are no dividends (q ¼ 0) we have already shown in Sections 10.2.1 and
10.2.2 that m1 ¼ 1 and m2 ¼ 2r=2 so the value of a perpetual down and out call is
(see Merton (1973)):
cdoðS; EÞ ¼ S  Sm2
Bm21 ¼ S  B S
B
 2r=2
ð10:29Þ
10.3
APPROXIMATIONS FOR VANILLA AMERICAN OPTIONS
10.3.1
American call options with cash dividends
In this section we will consider the valuation of vanilla American call options with
cash dividends, and discuss both the Roll, Geske, and Whaley method and also the
Black (1975) method. We will first consider the Roll, Geske, and Whaley method.
Numeric methods and single asset American options
121

The Roll, Geske, Whaley approximation
This method uses the work of Roll (1977), Geske (1979), and Whaley (1981). Let S be
the current (time t) price of an asset which pays a single cash dividend D1 at time t1.
At the ex-dividend date, t1, there will be a decrease in the asset’s value from St1 to
St1  D1. Also the current asset price net of escrowed dividends is:
SD ¼ S  D1 expðrðt1  tÞÞ
ð10:30Þ
where r is the riskless interest rate.
Now consider an American call option, with strike price E and expiry time T,
which is taken out on this asset. At t1 there will be a given ex-dividend asset price, S	,
above which the option will be exercised early. This value can be found by solving the
following equation:
cðS	; E; 1Þ ¼ S	 þ D1  E
ð10:31Þ
where c(S	, E, 1) is the Black–Scholes value of a European call option with strike
price E and maturity 1 ¼ T  t1, on an asset with current value S	 at time t1. If just
prior to the ex-dividend date St1 > S	, then the American option will be exercised
and realize a cash payoff of St1 þ D1  E. On the other hand if St1  S	 then the
option is worth more unexercised and it will be held until option maturity at time T.
We can rewrite Equation 10.31 so that S	 is the root of the following equation:
KðS	Þ ¼ cðS	; E; 1Þ  S	  D1 þ E ¼ 0
ð10:32Þ
where K(S	) denotes the function in the single variable S	.
A well-known technique for solving Equation 10.32 is Newton’s method, which in
this case takes the form:
S	
iþ1 ¼ S	
i  KðS	
i Þ
K0ðSiÞ	
ð10:33Þ
where S	
i is the ith approximation to S	, and S	
iþ1 is the improved (i þ 1)th approximation.
If we now consider the terms in Equation 10.33 we have that
KðS	
i Þ ¼ cðS	
i ; E; 1Þ  S	
i  D1 þ E
and
K0ðS	
i Þ ¼ @KðS	
i Þ
@S	
i
¼ @cðS	
i ; E; 1Þ
@S	
i
 1
Also from Equation C.14 in Appendix C.3
@cðS	
i ; E; 1Þ
@S	
i
¼ Nðd1ðS	
i ÞÞ
We note that here the continuous dividend yield, q ¼ 0.
So
K0ðS	
i Þ ¼ @KðS	
i Þ
@S	
i
¼ Nðd1ðS	
i ÞÞ  1;
where
d1 ¼ logðS	
i =EÞ þ ðr þ 2=2Þð1Þ

ffiffiffiffiffiffiffiffiffiffiffiffiffi
T  t1
p
122
Pricing Assets

Substituting these results into Equation 10.33 gives:
S	
iþ1 ¼ S	
i  cðS	
i ; E; 1Þ  ðS	
i þ D1  EÞ
	

Nðd1ðS	
i ÞÞ  1
On rearrangement this yields
S	
iþ1 ¼ S	
i N1ðd1ðS	
i ÞÞ  cðS	
i ; E; 1Þ þ D1  E
N1ðd1ðS	
i ÞÞ  1
;
for
i ¼ 0; . . . ; max iter ð10:34Þ
where a convenient initial approximation is to choose S	
0 ¼ E, and max_iter is the
maximum number of iterations that are to be used.
We will now quote the Roll, Geske, and Whaley formula for the current value of
an American call which pays a single cash dividend D1 at time t1, it is:
CðS; E; Þ ¼ SD N1ðb1Þ þ N2ða1; b1;
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
ðt1  tÞ=
p
Þ
n
o
þ D1 expðrðt1  tÞÞN1ðb2Þ
 E expðrÞ N1ðb2Þ expðrð1ÞÞ þ N2ða2; b2; 
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
ðt1  tÞ=
p
Þ
n
o
ð10:35Þ
where SD is given by Equation 10.30, E is the exercise price, T is the option expiry
date, t represents the current time,  is the option maturity, N1(a) is the univariate
cumulative normal density function with upper integral limit a, and N2(a, b, 	) is the
bivariate cumulative normal density function with upper integral limits a and b and
correlation coefficient 	. The other symbols used in Equation 10.35 are defined as
a1 ¼ logðS=EÞ þ ðr þ 2=2Þ

ffiffiffi
p
;
a2 ¼ a1  
ffiffiffi
p
b2 ¼ logðS=S	Þ þ ðr þ 2=2Þðt1  tÞ

ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
ðt1  tÞ
p
;
b2 ¼ b1  
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
ðt1  tÞ
p
and S is the current (time t) asset price, S	 is found using Equation 10.34, r is the
riskless interest rate,  is the asset’s volatility,  ¼ T  t and 1 ¼ T  t1.
To compute the value of an American call option which pays n cash dividends
Di, i ¼ 1, . . . , n at times ti, i ¼ 1, . . . , n, we can use the fact that optimal exercise
normally only ever occurs at the final ex-dividend date tn, see for example Hull
(1997). Under these circumstances Equation 10.35 can still be shown to value the
American call but now t  1 should be set to tn, D1 should be set to Dn, and SD is
given by:
SD ¼ S 
X
n
i¼1
Di expðrðti  tÞÞ
ð10:36Þ
A program to compute the Roll, Geske, and Whaley approximation for an Ameri-
can call option with multiple cash dividends is given in Code excerpt 10.1. Here the
NAG C library functions s15abc and g01hac are used to calculate the values of
N1(a) and N2(a, b, 	) respectively. Code excerpt 10.3 was used to compute the values
presented in Table 10.1. These compare the Roll, Geske, and Whaley approximation
with the Black approximation, which we will now briefly discuss.
Numeric methods and single asset American options
123

void RGW_approx(double *opt_value, double *critical_value, Integer n_divs, double dividends[],
double Divs_T[], double S0, double X, double sigma, double T, double r, Integer *iflag)
{
/* Input parameters:
n_divs
— the number of dividends
dividends[]
— the dividends: dividends[0] contains the first dividend, dividend[1] the second etc.
Divs_T[]
— the times at which the dividends are paid: Divs_T[0] is the time at which the first
dividend is paid Divs_T[1] is the time at which the second dividend is paid, etc.
S0
— the current value of the underlying asset
X
— the strike price
sigma
— the volatility
T
— the time to maturity
r
— the interest rate
Output parameters:
opt_value
— the value of the option
critical_value
— the critical value
iflag
— an error indicator
*/
double A_1,A_2,S_star,a1,a2,nt1,t1,S;
double b1,b2,d1,alpha,h,div,beta,temp,temp1,temp2,temp3;
double pdf,b,eur_val,fac,tol,loc_q,err,zero¼0.0;
Boolean iterate;
Integer i,iflagx,putx;
static NagError nagerr;
loc_q ¼ 0.0;
temp ¼ 0.0;
for (i¼0; i < n_divs; þþi) { /Check the Divs_T array */
if ((Divs_T[i] <¼ temp) || (Divs_T[i] > T) || (Divs_T[i] <¼ zero)) {
*flag ¼ 2;
return;
}
temp ¼ Divs_T[i];
}
/* calculate the present value of the dividends (excluding the final one) */
temp ¼ 0.0;
for (i¼0; i < n_divs1; þþi) {
temp ¼ fac þ dividends[i] * exp(r*Divs_T[i]);
}
t1 ¼ Divs_T[n_divs1];
/* decrease the stock price by the present value of all dividends */
div ¼ dividends[n_divs-1];
S ¼ S0-temp-div*exp(r*t1);
iterate ¼ TRUE;
tol ¼ 0.000001;
S_star ¼ X;
while (iterate) { /* calculate S_star, iteratively */
/* calculate the Black—Scholes value of a European call */
Table 10.1
A comparison of the computed values for American call options with dividends, using the
Roll, Geske, and Whaley approximation, and the Black approximation. The parameters used were: E ¼ 100:0,
r ¼ 0:04,  ¼ 0:2,  ¼ 2:0 and there is one cash dividend of value 5.0 at time t ¼ 1:0. The current stock price, S,
is varied from 80.0 to 120.0. The results are in agreement with those given in Table 1 of Whaley (1981)
Stock price
Critical price, S	
RGW approximation
Black approximation
80.0
123.582
3.212
3.208
85.0
123.582
4.818
4.808
90.0
123.582
6.839
6.820
95.0
123.582
9.276
9.239
100.0
123.582
12.111
12.048
105.0
123.582
15.316
15.215
110.0
123.582
18.851
18.703
115.0
123.582
22.676
22.470
120.0
123.582
26.748
26.476
124
Pricing Assets

d1 ¼ (log(S_star/X) þ (rþ(sigma*sigma/2.0))*(Tt1))/(sigma*sqrt(Tt1));
putx ¼ 0;
loc_q ¼ 0.0;
black_scholes(&eur_val,NULL,S_star,X,sigma, Tt1,r,loc_q, putx,&iflag);
S_star ¼ (S_star*s15abc(d1)eur_valþdivX)/(s15abc (d1)1.0);
err ¼ FABS(eur_val  (S_star þ div X))/X;
if (err < tol) iterate ¼ FALSE;
}
a1 ¼ (log(S/X) þ (rþ(sigma*sigma/2.0))*T)/(sigma*sqrt(T));
a2 ¼ a1  sigma*sqrt(T);
b1 ¼(log(S/S_star) þ (rþ(sigma*sigma/2.0))*t1)/(sigma*sqrt (t1));
b2 ¼ b1  sigma*sqrt(t1);
nt1 ¼ sqrt(t1/T);
temp1 ¼ S*(s15abc(b1)þg01hac(a1,b1,nt1,&nagerr));
temp2 ¼ X*exp(r*T)*g01hac(a2,b2,nt1,&nagerr)(Xdiv)* exp(r*t1)*s15abc(b2);
*opt_value ¼ temp1þtemp2;
*critical_value ¼ S_star;
}
Code excerpt 10.1
Function to compute the Roll, Geske, and Whaley approximation for the value of an
American call option with discrete dividends
We will now consider the Black approximation.
Black’s approximation
The Black (1975) approximation for an American call with cash dividends is simpler
than the Roll, Geske, and Whaley method we have just described. For an American
call option which expires at time T, with n discrete cash dividends Di, i ¼ 1, . . . , n, at
times ti, i ¼ 1, . . . , n, it involves calculating the prices of European options that
mature at times T, and tn, and then setting the option price to the greater of these
two values, see for example Hull (1997).
The Black approximation, CBL, can be expressed more concisely in terms of our
previously defined notation as:
CBLðS; E; Þ ¼ maxðv1; v2Þ
where v1 and v2 are the following European calls
v1 ¼ cðSD; E; Þ
and
v2 ¼ cðSþ
D; E; 1Þ,
 ¼ T  t
1 ¼ T  tn
and
SD ¼ S 
X
n
i¼1
Di
and
Sþ
D ¼ S 
X
n1
i¼1
Di
Code excerpt 10.2 below computes the Black approximation.
void black_approx(double *value, Integer n_divs, double dividends[], double Divs_T[],
double S0, double X, double sigma, double T, double r, Integer put, Integer *ifail)
{
/* Input parameters:
n_divs
— the number of dividends
dividends[]
— the dividends, dividends[0] contains the first dividend, dividend[1] the second etc.
Divs_T[]
— the times at which the dividends are paid, Divs_T[0] is the time at which the first
dividend is paid Divs_T[1] is the time at which the second dividend is paid, etc.
S0
— the current value of the underlying asset
Numeric methods and single asset American options
125

X
— the strike price
sigma
— the volatility
T
— the time to maturity
r
— the interest rate
put
— if put is 0 then a call option, otherwise a put option
Output parameters:
value
— the value of the option, iflag — an error indicator
*/
double zero ¼ 0.0;
double beta,temp,temp1,temp2,temp3;
double tn,val_T,val_tn,tol,loc_q,err,fac;
Integer i,ifailx;
loc_q ¼ 0.0;
temp ¼ 0.0;
for (i¼0; i < n_divs; þþi) {
if (Divs_T[i] <¼ temp ) printf (‘‘Error in Divs_T array, elements not increasing \n’’);
if (Divs_T[i] > T) printf (‘‘Error in Divs_T array element has a value greater than T \n’’);
if (Divs_T[i] <¼ zero) printf (‘‘Error in Divs_T array element <¼ zero \n’’);
temp ¼ Divs_T[i];
}
/* calculate the present value of the dividends */
fac ¼ 0.0;
for (i¼0; i < n_divs; þþi) {
fac ¼ fac þ dividends[i] * exp(r*Divs_T[i]);
}
temp ¼ S0 - fac;
/* calculate the value of the option on expiry */
black_scholes(&val_T,NULL,temp,X,sigma,T,r,loc_q, put,&ifailx);
/* calculate the value of the option on last dividend date */
tn ¼ Divs_T[n_divs1];
temp ¼ temp þ dividends[n_divs1]*exp(r*tn);
nag_opt_bs(&val_tn,NULL,temp,X,sigma,tn,r,loc_q, putx,&ifailx);
*value ¼ MAX(val_tn,val_T);
}
Code excerpt 10.2
Function to compute the value of the Black approximation for the value of an American
call option with discrete dividends
Code excerpt 10.3 below uses the same values as in Whaley (1981) and compares
the Roll, Geske, and Whaley approximation with that of Black; the results are
presented in Table 10.1.
double q,r,temp,loc_r;
Integer i,m,m2,m_acc;
double S0,E,T,sigma,t1,delta,value,ad_value,put_value;
Integer is_american,ifail,put;
double bin_greeks[5],greeks[5],bin_value,bs_value;
double opt_value, critical_value, E1, E2, crit1, crit2;
double black_value;
double Divs_T[3],dividends[3];
Integer n_divs, put;
E ¼ 100.0;
r ¼ 0.04;
sigma ¼ 0.2;
T ¼ 2.0;
t1 ¼ 1.0;
put ¼ 0;
/* check using the same parameters as in Whaley (1981) */
Divs_T[0] ¼ 1.0;
dividends[0] ¼ 5.0;
n_divs ¼ 1;
printf (‘‘\nPrice S
RGW Approximation
Black Approximation \n\n’’);
for (i¼0; i < 9; þþi) {
put ¼ 0;
S0 ¼ 80.0þ(double)i*5.0;
126
Pricing Assets

opt_RGW_approx(&opt_value,&critical_value, n_divs, dividends,Divs_T,S0,E,sigma,T,r,&ifail);
printf(‘‘%8.4f ’’,S0);
printf(‘‘%12.3f %12.3f ’’,opt_value,critical_value);
opt_black_approx(&black_value,n_divs,dividends, Divs_T, S0,E,sigma,T,r,put,&ifail);
printf(‘‘%12.3f (%8.4e) ’’,black_value);
}
Code excerpt 10.3
Simple test program to compare the results of function opt_RGW_approx with
function opt_black_approx, the parameters used are the same as in Whaley (1981)
We will now consider a more general technique for pricing both American puts
and calls.
10.3.2
The MacMillan, Barone-Adesi, and Whaley method
Here we consider a method of pricing American options which relies on an approximation
that reduces a transformed Black–Scholes equation into a second order ordinary
differential equation, see Barone-Adesi and Whaley (1987) and MacMillan (1986).
It thus provides an alternative way of evaluating American options that can be used
instead of computationally intensive techniques such as finite-difference methods.
Although the method prices American options it is really based on the value of an
American option relative to the corresponding European option value (which can
readily be computed using the Black–Scholes pricing formula).
Since an American option gives more choice its value is always at least that of its
European counterpart. This early exercise premium (
(S, E, )  0) is now defined
more precisely for American puts and calls. If at current time t the asset price is S,
then the early exercise premium for an American call which expires at time T, and
therefore has maturity  ¼ T  t, is:

cðS; E; Þ ¼ CðS; E; Þ  cðS; E; Þ  0
ð10:37Þ
where C(S, E, ) denotes the value of the American call and c(S, E, ) denotes the
value of the corresponding European call. The early exercise premium of an Ameri-
can put option, 
p(S, E, ), is similarly defined as:

pðS; E; Þ ¼ PðS; E; Þ  pðS; E; Þ  0
ð10:38Þ
where P(S, E, ) is the value of the American put, and p(S, E, ) is the value of
the corresponding European put. The key insight provided by the MacMillan,
Barone-Adesi, and Whaley method is that since both the American and European
option values satisfy the Black–Scholes partial differential equation so does the
early exercise premium, 
(S, E, ); see Section 9.3.1. This means that we can
write:
@
@t þ ðr  qÞS @
@S þ 2S2
2
@2
@S2 ¼ r
ð10:39Þ
where as usual S is the asset price, r the continuously compounded interest rate, q the
continuously compounded dividend,  the volatility, and time t increases from the
current time to the expiry time T.
Numeric methods and single asset American options
127

We will now introduce the variable h() ¼ 1  exp (r) and use the factorization

(S, E, ) ¼ h()g(S, E, h). From standard calculus we obtain:
@
@t ¼ g @h
@t þ h @g
@t ¼ rgðh  1Þ þ h @g
@h
@h
@t ¼ rgðh  1Þ þ hrðh  1Þ @g
@h
and also
@
@S ¼ h @g
@S
and
@2
@S2 ¼ h @2g
@S2
Substituting these results into Equation 10.39 yields the following transformed
Black–Scholes equation:
S22h
2
@2g
@S2 þ ðr  qÞSh @g
@S þ rgðh  1Þ þ rhðh  1Þ @g
@h ¼ rgh
ð10:40Þ
which can be further simplified to give:
S22 @2g
@S2 þ 2ðr  qÞS
2
@g
@S  2rg
h2  2rð1  hÞ
2
@g
@h ¼ rgh
ð10:41Þ
or
S2 @2g
@S2 þ S @g
@S  
h g  ð1  hÞ @g
@h ¼ 0
ð10:42Þ
where  ¼ 2r=2 and  ¼ (2(r  q))=2.
We now consider the last term of Equation 10.42 and note that when  is large,
1  h() 
 0. Also when  ! 0 the option is close to maturity, and the value of both
the European and American options converge; which means that 
(S, E, ) 
 0 and
@g=@h 
 0. It can thus be seen that the last term is generally quite small and, the
MacMillan, Barone-Adesi and Whaley approximation assumes that it can be
ignored. This results in the following equation:
S2 @2g
@S2 þ S @g
@S  
h g ¼ 0
ð10:43Þ
which is a second order differential equation with two linearly independent solutions
of the form aS
. They can be found by substituting g(S, E, h) ¼ aS
 into Equation
10.43 as follows:
@g
@S ¼ 
S
1
@2g
@S2 ¼ a
ð
  1ÞS
2 ¼ a
2S
2  a
S
2
so
S2 @2g
@S2 ¼ a
2S
  a
S
 ¼ 
2g  
g
and
S @g
@S ¼ Sa
S
1 ¼ 
S
 ¼ 
g
128
Pricing Assets

When the above results are substituted in Equation 10.43 we obtain the quadratic
equation:

2g  
g þ 
g  =h ¼ gð
2  
 þ ð  1Þ
  =hÞ ¼ 0
or

2  
 þ ð  1Þ
  =h ¼ 0
ð10:44Þ
which has the two solutions

1 ¼ 1
2
ð  1Þ 
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
ð  1Þ2 þ 4ð=hÞ
q


ð10:45Þ
and

2 ¼ 1
2
ð  1Þ þ
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
ð  1Þ2 þ 4ð=hÞ
q


ð10:46Þ
where we note that since =h > 0, we have 
1 < 0 and 
2 > 0.
The general solution to Equation 10.43 is thus:
gðS; E; hÞ ¼ a1S
1 þ a2S
2
ð10:47Þ
We will now derive the appropriate solutions pertaining to American call options
and American put options.
American call options
Here we use the fact that both the value and the early exercise premium
(
c(S, E, ) ¼ hgc(S, E, h)) of an American call tend to zero as the asset price
S ! 0. This means that as S ! 0, gc(S, E, h) ! 0.
However, since 
1 < 0, the only way this can be achieved in Equation 10.47 is if
a1 ¼ 0. So gc(S, E, h) ¼ a2S
2, and the value of an American call is:
CðS; E; Þ ¼ cðS; E; Þ þ ha2S
2
ð10:48Þ
An expression for a2 can be found by considering the critical asset price (point on
the early exercise boundary), S	, above which the American option will be exercised.
For S < S	, the value of the American call is governed by Equation 10.48, and when
S > S	 we have C(S, E, ) ¼ S  E.
Now, since the value of the American option is continuous, at the critical asset
value S	 the following equation applies:
S	  E ¼ cðS	; E; Þ þ ha2S	
2
ð10:49Þ
Furthermore, since the gradient of the American option value is also continuous, at
S	 we have:
@ðS	  EÞ
@S	
¼ @
@S	 cðS	; E; Þ þ ha2S	
2
f
g
ð10:50Þ
Numeric methods and single asset American options
129

which gives:
1 ¼ expðqÞN1ðd1ðS	ÞÞ þ 
2ha2S	ð
21Þ
ð10:51Þ
where we have used the value of the hedge parameter c, see Section 9.3.3, for a
European call
c ¼ @cðS	; E; Þ
@S	
¼ expðqÞN1ðd1ðS	ÞÞ
Equation 10.51 can therefore be written as:
ha2S	
2 ¼ S	

2
f1  expðqÞN1ðd1ðS	ÞÞg
ð10:52Þ
When the left hand side of the above equation is substituted into Equation 10.49 we
obtain the following equation for S	:
S	  E ¼ cðS	; E; Þ þ S	

2
f1  expðqÞN1ðd1ðS	ÞÞg
ð10:53Þ
This equation can be solved for S	 using standard iterative methods (see the section on the
numerical solution of critical asset values). Once S	 has been found Equation 10.52 gives:
ha2 ¼ A2S	
2
where
A2 ¼ S	

2
1  expðqÞN1ðd1ðS	ÞÞ
f
g
From Equation 10.48 the value of an American call is thus of the form:
MacMillan, Barone-Adesi, and Whaley method: American call option
CðS; E; Þ ¼ cðS; E; Þ þ A2
S
S	


2
when S < S	
ð10:54Þ
CðS; E; Þ ¼ S  E when S  S	
ð10:55Þ
American put options
For an American put option we proceed in a similar manner to that for the American
call. We now
use
fact that
both the
value
and early
exercise premium,

p(S, E, ) ¼ hgp(S, E, h), of an American put tend to zero as the asset price
S ! 1. So gp(S, E, h) ! 0 as S ! 1. Since 
2 > 0 the only way this can
be achieved by Equation 10.47 is if a2 ¼ 0. This gives gp(S, E, h) ¼ a1S
1 and the
value of an American put is:
PðS; E; Þ ¼ pðS; E; Þ þ ha1S
1
ð10:56Þ
An expression for a1 can be found by considering the critical asset price, S		, below
which the American option will be exercised. For S > S		 the value of the American
put is given by Equation 10.56, and for S < S		 we have P(S, E, ) ¼ E  S.
Continuity of the American option value at the critical asset price gives:
E  S		 ¼ pðS		; E; Þ þ ha1S		
1
ð10:57Þ
130
Pricing Assets

and continuity of the option value’s gradient at the critical asset price yields:
@ðE  S		Þ
@S		
¼
@
@S		 fpðS		; E; Þ þ ha1S		
1g
ð10:58Þ
which can be simplified to:
1 ¼ N1ðd1ðS		ÞÞ expðqÞ þ 
1a1S		ð
11Þ
ð10:59Þ
where we have used the value of hedge parameter p for a European put (see section
on the greeks):
p ¼ @pðS		; E; Þ
@S		
¼ fN1ðd1ðS		ÞÞ  1g expðqÞ ¼ N1ðd1ðS		ÞÞ expðqÞ
Equation 10.59 can therefore be written as:
ha1S		
1 ¼  S		

1
f1  N1ðd1ðS		ÞÞ expðqÞg
ð10:60Þ
When the left hand side of the above equation is substituted into Equation 10.57 we
obtain the following equation for S		:
E  S		 ¼ pðS		; E; Þ þ f1  expðqÞN½d1ðS		Þg S		

1
ð10:61Þ
which can be solved iteratively to yield S		 (see the section on the numerical solution
of critical asset values). Once S		 has been found Equation 10.60 gives:
ha1 ¼ A1S		
1
where
A1 ¼  S		

1


f1  expðqÞN1ðd1ðS		ÞÞg
We note here that A1 > 0 since, 
1 < 0, S		 > 0 and N1(d1(S		)) exp (q) < 1.
From Equation 10.56 the value of an American put is thus:
MacMillan, Barone-Adesi, and Whaley method: American put option
PðS; E; Þ ¼ pðS; E; Þ þ A1
S
S		


2
when S > S		
ð10:62Þ
PðS; E; Þ ¼ E  S
when S  S		
ð10:63Þ
Numerical solution of critical asset values
We now provide details on how to iteratively solve for the critical asset price in
Equations 10.53 and 10.61.
American call options
For American call options we need to solve Equation 10.53, which is:
S	  E ¼ cðS	; E; Þ þ S	

2
f1  expðqÞN1ðd1ðS	ÞÞg
Numeric methods and single asset American options
131

We denote the ith approximation to the critical asset value S	 by S	
i , and represent
the left hand side of the equation by:
LHSðS	
i ; E; Þ ¼ S	
i  E
and the right hand side of the equation by:
RHSðS	
i ; E; Þ ¼ cðS	
i ; E; Þ þ S	
i

2
f1  expðqÞN1ðd1ðS	
i ÞÞg
If we let K(S	
i , E, ) ¼ RHS(S	
i , E, )  LHS(S	
i , E, ) then we want to find the
value of S	
i which (to a specified tolerance) gives K(S	
i , E, ) 
 0. This can be
achieved with Newton’s root finding method, in which a better approximation,
S	
iþ1, can be found using:
S	
iþ1 ¼ S	
i  KðS	
i ; E; Þ
K0ðS	
i ; E; Þ
ð10:64Þ
where
K0ðS	
i ; E; Þ ¼ @
@S	
i
fRHSðS	
i ; E; Þ  LHSðS	
i ; E; Þg
¼ @
@S	
i
fRHSðS	
i ; E; Þg  @
@S	
i
fLHSðS	
i ; E; Þg
¼ bi  1
Here we have used bi ¼ (@=@S	
i )fRHS(S	
i , E, )g, and the expression for bi is given
by Equation 10.66, which is derived at the end of this section.
Substituting for K(S	
i , E, ) and K0(S	
i , E, ) into Equation 10.64 we therefore
obtain:
S	
iþ1 ¼ S	
i  ðRHSðS	
i ; E; Þ  LHSðS	
i ; E; ÞÞ
ðbi  1Þ
¼ S	
i  ðRHSðS	
i ; E; Þ  ðS	
i  EÞÞ
ðbi  1Þ
¼ biS	
i  RHSðS	
i ; E; Þ  E
ðbi  1Þ
The final iterative algorithm for the American call is therefore:
S	
iþ1 ¼ E þ RHSðS	
i ; E; Þ  biS	
i
ð1  biÞ
ð10:65Þ
where we can use S	
0 ¼ E for the initial estimate of the critical value, see computer
Code excerpt 10.4.
The expression for bi in an American call
Here we derive an expression for the term bi which is used in Equation 10.65.
bi ¼ @cðS	
i ; E; Þ
@S	
i
þ 1

2
1  expðqÞN1ðd1ðS	
i ÞÞ
	

 S	
i

2
@N1ðd1ðS	
i ÞÞ
@d1ðS	
i Þ
@d1ðS	
i Þ
@S	
i
132
Pricing Assets

We will now quote the following results which are derived in Appendix C:
Equation C.3:
@N1ðd1ðS	
i ÞÞ
@d1ðS	
i Þ
¼ nðd1ðS	
i ÞÞ
Equation C.6:
@d1ðS	
i Þ
@S	
i
¼
1
S	
i 
ffiffiffi
p
Equation C.14:
c ¼ @cðS	
i ; E; Þ
@S	
i
¼ expðqÞN1ðd1ðS	
i ÞÞ
Substituting these results into the above expression we obtain:
bi ¼ expðqÞN1ðd1ðS	
i ÞÞ þ 1

2
 expðqÞN1ðd1ðS	
i ÞÞ

2
 expðqÞnðd1ðS	
i ÞÞ

2
ffiffiffi
p
which can be rearranged to yield:
bi ¼ expðqÞN1ðd1ðS	
i ÞÞ 1  1

2


þ 1

2
1  expðqÞnðd1ðS	
i ÞÞ

ffiffiffi
p


ð10:66Þ
American put options
For American put options we need to solve Equation 10.61 which is:
E  S		
i
¼ pðS		
i ; E; Þ  S		
i

1
1  N1ðd1ðS		
i ÞÞ expðqÞ
	

If we let S		
i
denote the ith approximation to the critical asset value S		, then we
can represent the left hand side of the equation by:
LHSðS		
i ; E; Þ ¼ E  S		
i
and the right hand side of the equation by:
RHSðS		
i ; E; Þ ¼ pðS		
i ; Þ  S		
i

1
f1  N1ðd1ðS		
i ÞÞ expðqÞg
¼ pðS		
i ; E; Þ  S		
i

1
f1  ½1  N1ðd1ðS		
i ÞÞ expðqÞg
¼ pðS		
i ; E; Þ  S		
i

1
f1  expðqÞ þ N1ðd1ðS		
i ÞÞ expðqÞg
Numeric methods and single asset American options
133

We then denote K(S		
i , E, ) ¼ RHS(S		
i , E, )  LHS(S		
i , E, ), and using
Newton’s method we obtain:
S		
iþ1 ¼ S		
i
 KðS		
i ; E; Þ
K0ðS		
i ; E; Þ
ð10:67Þ
where as before:
K0ðS		
i ; E; Þ ¼
@
@S		
i
RHSðS		
i ; E; Þ  LHSðS		
i ; E; Þ
	

So K0(S		
i , E, ) ¼ 1 þ bi, where bi ¼ (@(RHS(S		
i , E, ))=@S		
i ), and the expres-
sion for bi is given by Equation 10.69, which is derived at the end of this section.
Equation 10.67 can therefore be written as:
S		
iþ1 ¼ S		
i
 ðRHSðS		
i ; E; Þ  LHSðS		
i ; E; ÞÞ
1 þ bi
¼ S		
i ð1 þ biÞ  RHSðS		
i ; E; Þ þ E  S		
i
1 þ bi
The final iterative algorithm for the American put is therefore:
S		
i
¼ E  RHSðS		
i ; E; Þ þ biS		
i
1 þ bi
ð10:68Þ
where we can use S		
0 ¼ E for the initial estimate of the critical asset value, see
computer Code excerpt 10.4.
The expression for bi in an American put
Here we derive an expression for the term bi which is used in Equation 10.67. Since
bi ¼
@
@S		
i

pðS		
i ; E; Þ  S		
i

1
1  expðqÞ
ð
þ N1ðd1ðS		
i ÞÞ expðqÞ

we have
bi ¼ @pðS		
i ; E; Þ
@S		
i
 1

1
1  expðqÞ
f
g  1

1
expðqÞN1ðd1ðS		
i ÞÞ
 S		
i expðqÞ

1
@N1ðd1ðS		
i ÞÞ
@d1ðS		
i Þ
@d1ðS		
i Þ
@S		
i
We will now quote the following results which are derived in Appendix C:
Equation C.3:
@N1ðd1ðS		
i ÞÞ
@d1ðS		
i Þ
¼ nðd1ðS		
i ÞÞ
134
Pricing Assets

Equation C.6:
@d1ðS		
i Þ
@S		
i
¼
1
S		
i 
ffiffiffi
p
Equation C.16:
p ¼ @pðS		
i ; E; Þ
@S		
i
¼ expðqÞ N1ðd1ðS		
i ÞÞ  1
	

Substituting these results into the above expression we therefore obtain:
bi ¼ expðqÞ N1ðd1ðS		
i ÞÞ  1
	

  1

1
1  expðqÞ þ N1ðd1ðS		
i ÞÞ expðqÞ
	

 S		
i expðqÞ

1
@N1ðd1ðS		
i ÞÞ
@d1ðS		
i Þ
@d1ðS		
i Þ
@S		
i
¼ expðqÞ N1ðd1ðS		
i ÞÞ  1
	

 1

1
1  expðqÞ þ N1ðd1ðS		
i ÞÞ expðqÞ
	

 S		
i expðqÞnðd1ðS		
i ÞÞ

1
ffiffiffi
p
which can be rearranged to yield:
bi ¼ expðqÞN1ðd1ðS		
i ÞÞ 1  1

1


þ 1

1
expðqÞ  1  expðqÞnðd1ðS		
i ÞÞ

ffiffiffi
p


 expðqÞ
ð10:69Þ
The computer code to implement the MacMillan, Barone-Adesi, and Whaley
method is provided below.
void MBW_approx(double *opt_value, double *critical_value, double S0, double X,
double sigma, double T, double r, double q, Integer put, Integer *iflag)
{
/* Input parameters:
S0
— the current value of the underlying asset
X
— the strike price
sigma
— the volatility
T
— the time to maturity
r
— the interest rate
q
— the continuous dividend yield
put
— if put is 0 then a call option, otherwise a put option
Output parameters:
opt_value
— the value of the option
critical_value
— the critical value
iflag
— an error indicator
*/
double A_1,A_2,S_star,gamma_2,gamma_1;
double d1,alpha,h,beta,temp,temp1;
double pdf,pi,b,rhs,eur_val,tol,err;
Boolean iterate;
Integer iflagx,putx;
Numeric methods and single asset American options
135

pi ¼ X01AAC;
beta ¼ 2.0 * (r  q) / (sigma * sigma);
alpha ¼ 2.0 * r / (sigma * sigma);
h ¼ 1.0  exp( r*T);
temp ¼ beta  1.0;
iterate ¼ TRUE;
tol ¼ 0.000001;
if (!put){/* An American call */
gamma_2 ¼ (temp þ sqrt((temp*temp) þ (4.0*alpha/h)));
gamma_2 ¼ gamma_2 / 2.0;
S_star ¼ X;
while (iterate){/* calculate S_star, iteratively */
d1 ¼ log(S_star/X) þ (rqþ(sigma*sigma/2.0))*T;
d1 ¼ d1/(sigma*sqrt(T));
pdf ¼ (1.0/sqrt(2.0*pi))*exp(d1*d1/2.0);
temp ¼ exp (q*T)*s15abc(d1)*(1.0  (1.0/gamma_2));
temp1 ¼ (1.0  ((exp(q*T)*pdf)/(sigma*sqrt(T))))/gamma_2;
b ¼ temp þ temp1;
/* calculate the Black—Scholes value of a European call */
putx ¼ 0;
black_scholes(&eur_val,NULL,S_star,X,sigma, T,r,q,putx,&iflagx);
rhs ¼ eur_valþ(1.0exp (q*T)*s15abc(d1)) *S_star/gamma_2;
S_star ¼ (X þ rhs  b*S_star)/(1.0  b);
err ¼ FABS((S_star  X)  rhs)/X;
if (err < tol) iterate ¼ FALSE;
}
A_2 ¼ (S_star/gamma_2)*(1.0  exp(q*T)*s15abc(d1));
if (S0 < S_star) {
temp1 ¼ S0/S_star;
black_scholes(&temp,NULL,S0,X,sigma,T,r,q,putx, &iflagx);
*opt_value ¼ temp þ A_2 * pow(temp1,gamma_2);
}
else {
*opt_value ¼ S0  X;
}
}
else {/* An American put */
gamma_1 ¼ (temp  sqrt((temp*temp) þ (4.0*alpha/h)));
gamma_1 ¼ gamma_1 / 2.0;
S_star ¼ X;
while (iterate){/* calculate S_star, iteratively */
d1 ¼ log(S_star/X) þ (rqþ(sigma*sigma/2.0))*T;
d1 ¼ d1/(sigma*sqrt(T));
pdf ¼ (1.0/sqrt(2.0*pi))*exp(d1*d1/2.0);
temp ¼ exp(q*T)*(s15abc(d1)*(1.0 (1.0/gamma_1)) 1.0);
temp1 ¼ (exp(q*T) 1.0((exp(q*T)*pdf)/(sigma*sqrt(T))))/gamma_1;
b ¼ temp þ temp1;
/* calculate the Black—Scholes value of a European put */
putx ¼ 1;
black_scholes(&eur_val,NULL,S_star,X,sigma, T,r,q,putx,&iflagx);
rhs ¼ eur_val(1.0exp(q*T)þexp(q*T)*s15abc(d1)) *S_star/gamma_1;
S_star ¼ (X  rhs þ b*S_star)/(1.0 þb);
err ¼ FABS((X  S_star)  rhs)/X;
if (err < tol) iterate ¼ FALSE;
}
A_1 ¼ (S_star/gamma_1)*(1.0  exp(q*T)*s15abc(d1));
if (S0 > S_star) {
temp1 ¼ S0/S_star;
black_scholes(&temp,NULL,S0,X,sigma,T,r,q,putx, &iflagx);
*opt_value ¼ temp þ A_1 * pow(temp1,gamma_1);
}
else {
*opt_value ¼ X  S0;
}
}
*critical_value ¼ S_star;
}
Code excerpt 10.4
The function MBW_approx which computes the MacMillan, Barone-Adesi, and Whaley
approximation for American options
Tables 10.2 and 10.3 present the results of using the function MBW_approx to
compute the values of various American options.
136
Pricing Assets

10.4
LATTICE METHODS FOR VANILLA OPTIONS
10.4.1
Binomial lattice
In this section we will derive equations for a binomial lattice that describes the GBM
movement of asset price changes. The approach that we will adopt is based on the
work of Cox, Ross, and Rubinstein (1979), and will be referred to as the CRR lattice.
From Section 8.3 Equation 8.15 we know that if the price of an asset, St, follows
GBM then the change in value of its price over time interval t, has the following
distribution:
log Stþt
St



 N
r  2
2


t; 2t


Table 10.2
The MacMillan, Barone-Adesi, and Whaley method for American option values computed by the
routine MBW_approx. The parameters used were:  ¼ 0:5, E ¼ 100:0, r ¼ 0:1, q ¼ 0:06,  ¼ 0:2. The
accurate value was calculated using a standard lattice with 2000 time steps, and the error was
the MacMillan, Barone-Adesi, and Whaley estimate minus the accurate value
Call
Put
Stock price
Accurate value
Error
Accurate value
Error
86.0
1.2064
5:54  104
14.0987
3:69  102
89.0
1.8838
1:95  104
11.5120
4:85  102
92.0
2.7890
7:03  104
9.2478
3:58  102
95.0
3.9427
1:16  103
7.3031
1:66  102
98.0
5.3522
1:15  103
5.6674
7:19  104
101.0
7.0119
1:10  103
4.3209
1:35  102
104.0
8.9043
2:21  103
3.2362
2:22  102
107.0
11.0072
2:63  103
2.3823
2:63  102
110.0
13.2905
4:20  103
1.7235
2:80  102
113.0
15.7264
4:77  103
1.2272
2:66  102
Table 10.3
The MacMillan, Barone-Adesi, and Whaley critical asset values for the early exercise
boundary of an American put computed by the routine MBW_approx. The parameters used were:
S ¼ 101:0, E ¼ 101:0, r ¼ 0:1, q ¼ 0:06, and  ¼ 0:20
Time to expiry, 
Critical asset value, S		
Time to expiry, 
Critical asset value, S		
1.0
82.1510
0.50
85.1701
0.95
82.3751
0.45
85.6199
0.90
82.6115
0.40
86.1176
0.85
82.8618
0.35
86.6740
0.80
83.1273
0.30
87.3049
0.75
83.4098
0.25
88.0333
0.70
83.7115
0.20
88.8959
0.65
84.0349
0.15
89.9568
0.60
84.3830
0.10
91.3469
0.55
84.7598
0.05
93.4260
Numeric methods and single asset American options
137

If we use the notation:
X ¼ Stþt
St
;
and
 ¼ ðr  2=2Þt

2 ¼ 2t
the above equation becomes:
logðXÞ 
 Nð; 
2Þ
or equivalently
X 
 ð; 
2Þ
where (, 
2) is the lognormal distribution derived from a Gaussian distribution
with mean , and variance 
2. It is well known, see for example Evans et al. (2000),
that the first two moments of a variable X drawn from a lognormal distribution are
Lognormal mean
E½X ¼ expð þ 
2=2Þ
ð10:70Þ
substituting for  and 
2 gives
E½X ¼ exp
r  2
2


t þ 2
2 t


ð10:71Þ
Lognormal variance
Var½X ¼ E½ðX  E½XÞ2 ¼ E½X2  ðE½XÞ2 ¼ expð2 þ 
2Þ expð
2Þ  1
	

ð10:72Þ
substituting for  and 
2 gives
Var½X ¼ exp 2r r  2
2


t þ 2t


which can be simplified to yield
Var½X ¼ exp 2rt
f
g expð2tÞ  1
	

ð10:73Þ
Since we can assume that the expected value of X grows at the riskless interest rate,
r, we can also write:
E½X ¼ expðrtÞ
ð10:74Þ
The above results can be used to find the first two moments of the asset price
distribution Stþt, given that we know the asset price, St, at time instant t. To do this
we will use, see Appendix F.3 for a proof, the fact that for a random variable G we have:
E½a þ bG ¼ E½a þ bE½G
and
Var½a þ bG ¼ b2Var½G
where a and b are constants. Applying this to the variable X gives:
E½X ¼ E Stþt
St


¼ 1
St
E Stþt
½

ð10:75Þ
138
Pricing Assets

and
Var½X ¼ Var Stþt
St


¼ 1
S2
t
Var Stþt
½

ð10:76Þ
where we have used a ¼ 0 and b ¼ 1/St. Note that it is also easy to show that:
Var½Stþt ¼ Var½S
ð10:77Þ
where the change in asset price over the time interval t is denoted by
S ¼ Stþt  St. This elementary result sometimes is used without proof, see for
example Hull (1997) p. 344. The proof is simple:
Var½Stþt ¼ Var½St þ S ¼ Var½S
where again we have used
Var½a þ bG ¼ b2Var½G
this time with a ¼ 0 and b ¼ 1.
To find expressions for the mean and variance of Stþt we simply substitute
Equation 10.74 into Equation 10.75 and obtain:
E½Stþt ¼ St expðrtÞ
ð10:78Þ
and substitute Equation 10.73 into Equation 10.76 to yield:
Var½Stþt ¼ S2
t expð2rtÞ expð2tÞ  1
	

ð10:79Þ
Since we are modelling asset price movements with a binomial lattice, the asset
price, St, at any given node is only permitted to either jump up or jump down in value
over the next time step t. Here we will assume that the new asset price, Stþt, is Stu
for an up jump and Std for a down jump; where u and d are constants that apply to
all lattice nodes. If we further denote the probability of an up jump by p then the
probability of a down jump must (by definition) be 1  p.
Now that we have specified the lattice parameters we will use these to match the
first two moments of the lognormal distribution. This results in the following
equation for the mean:
E½Stþt ¼ pStu þ ð1  pÞStd ¼ St expðrtÞ
ð10:80Þ
The corresponding equation for the variance requires a little more work:
Var½Stþt ¼ E½ðStþtÞ2  ðE½StþtÞ2
ð10:81Þ
Since
E½ðStþtÞ2 ¼ pðStuÞ2 þ ð1  pÞðStdÞ2 ¼ S2
t pu2 þ ð1  pÞd2


ð10:82Þ
and, from Equation 10.80, we have
ðE½StþtÞ2 ¼ St expðrtÞ
f
g2 ¼ S2
t expð2rtÞ
ð10:83Þ
Numeric methods and single asset American options
139

We can substitute Equations 10.82 and 10.83 into Equation 10.81 to obtain
Var½St þ t ¼ S2
t expð2rtÞ expð2tÞ  1
	

¼ S2
t pu2 þ ð1  pÞd2


 S2
t expð2rtÞ
We therefore have:
expð2rtÞ expð2tÞ  1


¼ pu2 þ ð1  pÞd2  expð2rtÞ
ð10:84Þ
So, restating Equation 10.80 and simplifying Equation 10.84, we obtain the following
two equations:
pu þ ð1  pÞd ¼ expðrtÞ
ð10:85Þ
expð2rt þ 2tÞ ¼ pu2 þ ð1  pÞd2
ð10:86Þ
which we will use to solve for the three parameters u, d, and p. Since there are three
unknowns and only two equations, we can impose an additional constraint to obtain
a unique solution. The constraint used in the CRR binomial model is:
u ¼ 1
d
ð10:87Þ
We now use the following notation:
a ¼ expðrtÞ
and
b2 ¼ expð2rtÞ expð2tÞ  1
	

¼ a2 expð2tÞ  1
	

ð10:88Þ
This means that Equation 10.85 can be written as
a ¼ pu þ ð1  pÞd;
which gives
p ¼ a  d
u  d
ð10:89Þ
From Equation 10.86 we have
expð2rt þ 2tÞ ¼ a2 expð2tÞ ¼ a2 þ b2
and so
a2 þ b2 ¼ pu2 þ ð1  pÞd2
Rearranging we have
pu2 þ ð1  pÞd2  a2 ¼ b2
pu3 þ ð1  pÞd2u  a2u  b2u ¼ 0
but
ð1  pÞd2u ¼ ð1  pÞd ¼ a  pu
so
pu3 ¼ ða  puÞ  a2u  b2u ¼ 0
or
pðu3  uÞ þ a  a2  b2u ¼ 0
Now
pðu3  uÞ ¼ u2pðu  dÞ ¼ u2ða  dÞ ¼ u2a  u
140
Pricing Assets

which gives
au2  u þ a  a2u  b2u ¼ 0
So we obtain the following quadratic equation in u:
au2  uð1 þ a2 þ b2Þ þ a ¼ 0
A solution is:
u ¼
ð1 þ a2 þ b2Þ þ
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
ð1 þ a2 þ b2Þ2  4a2
q
2a
If t is small we can obtain a reasonable approximation to the solution by
neglecting terms of order higher than t.
In these circumstances we have:
a2 þ b2 þ 1 ¼ expð2rtÞ þ expð2rtÞ expð2tÞ  1
	

þ 1

 1 þ 2rt þ ð1 þ 2rtÞ2t þ 1 
 2 þ 2rt þ 2t
Therefore
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
ða2 þ b2 þ 1Þ2  4a2
q

ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
ð2 þ 2rt þ 2tÞ2  4ð1 þ 2rtÞ
q

ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
4 þ 8rt þ 42  4  8rt
p
¼
ffiffiffiffiffiffiffiffiffiffiffiffiffi
42t
p
¼ 2
ffiffiffiffiffiffi
t
p
and so
u 
 2 þ 2rt þ 2t þ 2
ffiffiffiffiffiffi
t
p
2 expðrtÞ
u 
1 þ rt þ 2t
2
þ 
ffiffiffiffiffiffi
t
p


ð1  rtÞ
u 
 1 þ rt þ 2t
2
þ 
ffiffiffiffiffiffi
t
p
 rt ¼ 1 þ 
ffiffiffiffiffiffi
t
p
þ 2t
2
which to order t gives:
u ¼ expð
ffiffiffiffiffiffi
t
p
Þ
ð10:90Þ
since
expð
ffiffiffiffiffiffi
t
p
Þ ¼ 1 þ 
ffiffiffiffiffiffi
t
p
þ 2t
2
þ 3ðtÞ3=2
6
þ   
ð10:91Þ
which gives:
d ¼ 1
u ¼ expð
ffiffiffiffiffiffi
t
p
Þ
ð10:92Þ
It is interesting to note that when r ¼ 0 we have p ! 1/2.
Now that we know the values of the lattice parameters u, d, and p we can use these
to build a lattice with a specified number of time steps. Once this has been con-
structed it can be used to compute the values and Greeks for various types of
financial options. These could simply be American/European vanilla options, or
more exotic options that may incorporate features such as: lockout periods, barriers,
and nonstandard payoff functions.
Numeric methods and single asset American options
141

We will now discuss how to create a lattice which can be used to value American
and European vanilla options.
If the current value of the underlying asset is S, and the duration of the option is 
and we use a lattice with n equally spaced time intervals t, then we have:
t ¼ 
n
The values of the asset price at various nodes in the lattice can easily be computed.
This is illustrated in Figure 10.1, for a lattice with six time steps (that is seven lattice levels).
The asset values at the labelled nodes are:
Lattice level 1: Time t
SR ¼ S
Lattice level 2: Time t þ t
SS ¼ Su
ST ¼ Sd
Lattice level 6: Time t þ 5t
SA ¼ Su5
SB ¼ Su3
SC ¼ Su
SD ¼ Sd
SE ¼ S
SF ¼ Sd5
Lattice level 7: Time t þ 6t
SG ¼ Su6
SH ¼ Su4
SI ¼ Su2
SJ ¼ S
SK ¼ Sd2
SL ¼ Sd4
SM ¼ Sd6
R
S
U
A
G
H
I
J
K
L
M
T
1
0
2
3
4
5
6
F
E
D
C
B
V
W
Figure 10.1
A standard binomial lattice consisting of six time steps. The root lattice node R corresponds
to the current time t, the terminal nodes G to M are those at option maturity; that is time t þ , where  is
the duration of the option. The asset value at node R is S, where S is the current asset value. Asset values at
other nodes are, for example, node S: Su, node T: Sd, node V: S, and node A: Su5. Option values are
computed using a backward iterative process: the option values at nodes A to F on the penultimate time
step are computed from the payouts of the terminal nodes G to M, and this process continues until the root
node is reached; which yields the current value of the option. Here we compute the Greeks using the
following nodes: Delta uses nodes S and T, Gamma uses nodes U, V, and W and Theta uses nodes R and V
142
Pricing Assets

In general, at time t þ it, there are i þ 1, stock prices; these are:
Si; j ¼ Sujdij;
j ¼ 0; 1; . . . ; i
We note, that since u ¼ 1=d, an up movement followed by a down movement gives
the same stock price as a down movement followed by an up movement; for instance
Su2d ¼ Su. This means that the tree recombines, and the number of nodes required
to represent all the different asset prices is significantly reduced.
10.4.2
Constructing and using the binomial lattice
In this section we are concerned with the practical details of how to construct, and
then use, a standard one-dimensional binomial lattice to value American and Euro-
pean options. Since this lattice forms the basis for other one-dimensional and multi
dimensional lattice techniques we will discuss its construction in some detail.
A complete computer program for a standard binomial lattice is given in Code
excerpt 10.11, and we will use this as a basis for our discussions. For easy reference
we will now list the input parameters used by this computer program:
S0
the current price of the underlying asset, S
X
the strike price
sigma
the volatility of the asset
T
the maturity of the option in years
r
the risk free interest rate
q
the continuous dividend yield
put
if put equals 1 then the option is a put option,
if put equals 0 then it is a call option
is_american
if is_american equals 1 then it is an American option,
if is_american equals 0 then it is a European option
M
the number of time steps in the lattice
We will now discuss in more detail the computational issues involved in each stage
of the calculation.
Compute the values of the constants used by the lattice
First calculate the values of various constants that will be used.
Code excerpt 10.5
For convenience, we have used the variables p_u and p_d to store respectively the
up and down jump probabilities discounted by the interest rate r over one time step;
these values will be used later on when we work backwards through the lattice to
calculate the current option value.
dt ¼ T/(double)M;
t1 ¼ sigma*sqrt(dt);
u ¼ exp(t1);
d ¼ exp(t1);
a ¼ exp((r  q)*dt);
p ¼ (a  d)/(u  d);
if ((p < zero) || (p > 1.0)) printf (‘‘Error p out of range\n’’);
discount ¼ exp(r*dt);
p_u ¼ discount*p;
p_d ¼ discount*(1.0p);
Numeric methods and single asset American options
143

Assign the asset values to the lattice nodes
We will now show that the number of different asset prices, LSn, for an n step
recombining lattice is 2n þ 1.
The nodes in a recombining lattice can be considered as being composed of two
kinds: those corresponding to an even time step, and those corresponding to an odd
time step.
This is because the set of node asset values, ET , for an even time step is distinct
from the set of node asset values, OT , for an odd time step. Although ET \ OT ¼ Ø,
the elements of ET and OT for any consecutive pair of time steps, are related by the
simple constant multiplicative factor d. Also for an even time step there is a central
node corresponding to the current asset price SO, and the remaining nodes are
symmetrically arranged about this. These features are illustrated in Figure 10.1, for
a standard lattice with six time steps.
The number of distinct asset prices in a lattice is therefore the sum of the number of
nodes in the last two time steps. Since the number of nodes in the ith time step, Si, is
i þ 1 (see Figure 10.1), for an n time step lattice we have:
Sn ¼ n þ 1
and
Sn1 ¼ n
This means that the number of different asset values in an n time step lattice is:
LSn ¼ Sn þ Sn1 ¼ 2n þ 1
The number of nodes in an n time step lattice, LN n, is:
LN n ¼
X
n
i¼0
ði þ 1Þ ¼ ðn þ 1Þðn þ 2Þ
2
where we have used the fact that LN n is the sum of an arithmetic progression with
first term 1, increment 1 and last term n þ 1.
One might initially think that, in order to price options, it is necessary to store the
asset value of each lattice node; which would entail storing LN n values. However,
this is not the case. We only need to store the number of different asset values in the
lattice; that is LSn values.
Storing LSn values instead of LN n can result in dramatic economies of storage. For
example an accurate, 1000 step lattice, has LN n ¼ 2001  2002  1=2 ¼ 2003001,
while the corresponding value of LSn is only 2  1000 þ 1 ¼ 2001.
Code excerpt 10.6
A code fragment which assigns the different binomial lattice asset values to the storage
array s by using the up and down jump ratios u and d defined in Section 10.4.1. The current asset value S is
assigned to the central array element s[M], where M is the number of time steps in the lattice. The array
elements above centre are S[M + i] ¼ Sui, i ¼ 1, . . . , M, and the array elements below centre are
S[M  i]¼ Sdii ¼ 1, . . . , M
s[M] ¼ S0;
for (i ¼ 1; i <¼ M; þþi) {
s[Mþi] ¼ u*s[Mþi 1];
s[Mi] ¼ d*s[Miþ1];
}
144
Pricing Assets

Compute the option payoff at the terminal nodes
The current value of an option is evaluated by starting at option maturity, the end of
the tree and working backwards. The option values for the terminal nodes of the tree
are just given by the payoff (at maturity) of the option; this is independent of whether
the option is an American or European. For a lattice with n time steps there are n þ 1
terminal nodes, with option values, fn, j, j ¼ 0, . . . , n.
To compute the values of vanilla American and European options, with exercise
price E, then we will start with the following terminal node values:
for put options
fn; j ¼ maxðE  Su jdnj; 0Þ;
j ¼ 0; . . . ; n
and for call options
fn; j ¼ maxðSu jdnj  E; 0Þ;
j ¼ 0; . . . ; n
The computer code used to achieve this is:
Code excerpt 10.7
A code fragment that computes the payouts for puts and calls at the lattice terminal nodes.
The payouts are assigned to elements of the array v and are computed using the strike price, X, and the previously
computed asset values stored in array s, as before M is the number of time steps in the lattice
Iterate backwards through the lattice
The probability of moving from node (i, j) at time it to node (i þ 1, j þ 1) at time
(i þ 1)t is p, and the probability of moving from node (i, j) at time it to the node
(i þ 1, j) at time (i þ 1)t is 1  p. If we assume that there is no early exercise then:
f E
i; j ¼ expðrtÞ pfiþ1; jþ1 þ ð1  pÞfiþ1; j
	

;
j  i  n  1
0  j  i
ð10:93Þ
When early exercise, for an American option, is taken into account we have:
f A
i; j ¼ max E  Si; j; f E
i; j
n
o
ð10:94Þ
if (((Mþ1)/2) ¼¼ (M/2)) {/* then M is even */
if (put)
v[M/2] ¼ MAX(X  s[M], zero);
else
v[M/2] ¼ MAX(s[M]X, zero);
}
P1 ¼ 2*M;
P2 ¼ 0;
for (i ¼ 0; i < (Mþ1)/2; þþi){
if (put){
v[Mi] ¼ MAX(X  s[P1], zero);
v[i] ¼ MAX(X  s[P2], zero);
}
else{
v[Mi] ¼ MAX(s[P1]X, zero);
v[i] ¼ MAX(s[P2]X, zero);
}
P1 ¼ P1  2;
P2 ¼ P2 þ 2;
}
Numeric methods and single asset American options
145

or for an American call option:
f A
i; j ¼ max Si; j  E; f E
i; j
n
o
;
j  i  N  1
0  j  i
ð10:95Þ
where f E
i, j is given by Equation 10.93.
The following code works backward through the lattice and uses the array v to
store the option values.
Code excerpt 10.8
Computer code that works iteratively backward through the lattice computing the
option values at each time step. The array v contains the option values computed from the previous time
step, and these are overwritten with option values computed for the current time step. The iteration stops
at second time step, since we do not want to overwrite values in the array v which are required for
calculating the Greeks in the neighbourhood of the root node
At each time step the newly calculated option values overwrite those computed by
the previous time step. This process is continued until the second time step (m1 ¼ 2)
is reached. A different technique is then used, which doesn’t overwrite the option
values and thus allows the Greeks to be computed in the vicinity of the root lattice
node R. In cases where we are not interested in calculating the Greeks (see for
example Code excerpt 12.6) we continue working backward through the lattice until
the root node R (m1 ¼ 0) is reached, and the current value of the option is then
given by v\[0\](or its multidimensional equivalent).
The option values at all lattice nodes in time steps 0, 1, and 2 are made accessible
by the following code:
P2 ¼ 0;
for (m1 ¼ M1; m1 >¼ 2; m1) {
P2 ¼ P2 þ 1;
P1 ¼ P2;
for (n ¼0; n <¼ m1; þþn){
if ((v[n] ¼¼ zero) && (v[nþ1] ¼¼ zero)){
hold ¼ zero;
}
else
hold ¼ p_d*v[n] þ p_u*v[nþ1];
if (is_american){
if (put)
v[n] ¼ MAX(hold, Xs[P1]);
else
v[n] ¼ MAX(hold, s[P1]X);
}
else
v[n] ¼ hold;
P1 ¼ P1 þ 2;
}
}
jj ¼ 2;
for (m1 ¼ 2; m1 >¼ 1; --m1){
ind ¼ Mm1þ1;
for (n ¼0; n < m1; þþn){
hold ¼ p_d*v[5jj m11] þ p_u*v[5jjm1];
if (is_american) {
if (put)
v[5jj] ¼ MAX(hold, Xs[ind]);
else
v[5jj] ¼ MAX(hold, s[ind]X);
}
else
v[5jj] ¼ hold;
146
Pricing Assets

Code excerpt 10.9
Code fragment illustrating how the option values are stored for the first two time steps
so that the Greeks can be computed in the vicinity of the root node R
Figure 10.2 presents the results for the valuation of an American put option.
Computing the greeks: , , and 
We will now describe how to calculate the option’s hedge statistics (Greeks).
Let the option value and asset value at lattice node k be denoted by fk and Sk
respectively. So, for instance, ST represents the asset price at node T, and fT is the
corresponding option value at node T. Table 10.4 supplies details of the lattice node
values in the vicinity of the root node R.
jj;
ind ¼ ind þ 2;
}
}
*value ¼ v[5];
0.2
0.15
0.1
0.05
0
–0.05
–0.1
–0.15
–0.2
0
10
20
30
40
50
60
70
80
90
100
Number of time steps
Error in estimated value
American put
Figure 10.2
The error in the estimated value, est val, of an American put using a standard binomial lattice.
The parameters used were: T ¼ 1:0, S ¼ 105:0, X ¼ 105:0, r ¼ 0:1, q ¼ 0:02,  ¼ 0:3. The very accurate
value (acc val) was 9.2508 and was computed using a 6000 step standard binomial lattice. The error in the
estimated value was obtained as est val  acc val
Numeric methods and single asset American options
147

The computation of each Greek is now considered.
Delta
The definition of  is the rate of change of the option value with asset price; all other
parameters remaining fixed. Thus
 ¼ @f
@S ¼ f
S
where f is the change option value corresponding to the change in the asset price
S. Ideally we would like to evaluate this partial derivative at the root node R (m1 =0),
however we can’t because we need at least two lattice nodes to compute a value.
The best we can do is to evaluate the derivative at the first time step (m1 = 1) as
follows:
 ¼ fS  fT
SS  ST
¼
v[4]  v[3]
s[M þ 1]  s[M  1]
Gamma
The definition of  is the rate of change of  with asset price; all other parameters
remaining fixed. Thus
 ¼ @2f
@S2 ¼ @
@S
In order to evaluate  we require at least two values of . The nearest this can be
achieved to the root node R is at time step 2, where we have:
 ¼ 	
UV  	
VW
S	
UV  S	
VW
with the midpoints
S	
UV ¼ 1
2 SU þ SV
f
g
and the values of  at the midpoints S	
UV and S	
VW denoted by 	
UV and 	
VW
respectively. Since
Table 10.4
Lattice node values in the vicinity of the root node R
Node
Time step
Asset array element
Asset value
Option array element
R
0
s[M]
S
v[5]
S
1
s[M+1]
Su
v[4]
T
1
s[M1]
Sd
v[3]
U
2
s[M+2]
Su2
v[2]
V
2
s[M]
S
v[1]
W
2
s[M2]
Sd2
v[0]
148
Pricing Assets

	
UV ¼ fU  fV
SU  SV
;
	
VW ¼ fV  fW
SV  SW
and
S	
UV  S	
VW ¼ 1
2 SU  SW
f
g
we have
	
UV ¼
v[2]  v[1]
s[M þ 2]  s[M] ;
	
VW ¼
v[1]  v[0]
s[M]  s[M  2]
The value of  can therefore be approximated as:
 ¼
2 	
UV  	
VW
	

s[M þ 2]  s[M  2]
Theta
The definition of  is the rate of change of option value with time; all other
parameters remaining fixed. Thus
 ¼ @f
@t ¼ f
t
The nearest to the root node R that can be computed is over the time interval from
time step 0 to time step 2. We then obtain the following approximation:
 ¼ fV  fR
2t
¼ v[1]  v[5]
2t
The Code excerpt 10.10 computes the , , and  by using the approximations we
have just discussed.
Vega
The definition of V is the rate of change of the option value with volatility.
V ¼ @f
@
In a standard binomial lattice V cannot be computed directly. A simple approach is
to use two binomial lattices as follows
V ¼ fþ  f

where fþ is the option value computed using a binomial lattice with volatility
 þ  and f is the option value computed using another binomial lattice with a
volatility of ; all other lattice parameters remain constant.
if(greeks){
/* assign the value of delta (obtained from m1 ¼ 1) */
greeks[1] ¼ (v[4]v[3])/(s[Mþ1]s[M1]);
/* assign the value of gamma (use the values at time step m1 ¼ 2) */
Numeric methods and single asset American options
149

dv1 ¼ v[2]  v[1];
ds1 ¼ s[Mþ2]  s[M];
dv2 ¼ v[1]  v[0];
ds2 ¼ s[M]  s[M2];
h ¼ 0.5*(s[Mþ2]  s[M2]);
greeks[0] ¼ ((dv1/ds1)  (dv2/ds2))/h;
/* assign the value of theta */
greeks[2] ¼ (v[1]*value)/(2.0*dt); /* can also write: greeks[2] ¼ (v[1]v[5])/(2.0*dt); */
}
Code excerpt 10.10
A code fragment that computes the values of the Greeks (Delta, Gamma, and Theta)
in the vicinity of the root lattice node R
void standard_lattice(double *value, double greeks[], double S0, double X, double sigma, double T, double r,
double q, Integer put, Integer is_american, Integer M, Integer *iflag)
{
/* Input parameters:
S0
— the current price of the underlying asset
X
— the strike price
sigma
— the volatility
T
— the time to maturity
r
— the interest rate
q
— the continuous dividend yield
put
— if put is 0 then a call option, otherwise a put option
is_american
— if is_american is 0 then a European option, otherwise an American option
M
— the number of time steps
Output parameters:
value
— the value of the option,
greeks[]
— the hedge statistics output as follows: greeks[0] is gamma, greeks[1] is delta,
greeks[2] is theta,
iflag
— an error indicator.
*/



/* Allocate the arrays s[2*Mþ1], and v[Mþ1] */
dt ¼ T/(double)M;
t1 ¼ sigma*sqrt(dt);
u ¼ exp(t1);
d ¼ exp(t1);
a ¼ exp((rq)*dt);
p ¼ (a  d)/(u  d);
if ((p < zero) || (p > 1.0)) printf (‘‘Error p out of range\n’’);
discount ¼ exp(r*dt);
p_u ¼ discount*p;
p_d ¼ discount*(1.0p);
/* assign the 2*Mþ1 asset values */
s[M] ¼ S0;
for (i ¼ 1; i <¼ M; þþi){
s[Mþi] ¼ u*s[Mþi1];
s[Mi] ¼ d*s[Miþ1];
}
/* Find out if the number of time steps, M, is odd or even */
if (((Mþ1)/2) ¼¼ (M/2)){/* then M is even */
if (put)
v[M/2] ¼ MAX(X  s[M], zero);
else
v[M/2] ¼ MAX(s[M]X, zero);
}
/* Calculate the option values at maturity */
P1 ¼ 2*M;
P2 ¼ 0;
for (i ¼ 0; i < (Mþ1)/2; þþi) {
if (put){
v[Mi] ¼ MAX(X  s[P1], zero);
v[i] ¼ MAX(X  s[P2], zero);
}
else {
v[Mi] ¼ MAX(s[P1]X, zero);
v[i] ¼ MAX(s[P2]X, zero);
}
150
Pricing Assets

P1 ¼ P1  2;
P2 ¼ P2 þ 2;
}
/* now work backwards through the lattice to calculate the current option value */
P2 ¼ 0;
for (m1 ¼ M1; m1 >¼2; m1){
P2 ¼ P2 þ 1;
P1 ¼ P2;
for (n ¼0; n <¼m1; þþn){
if ((v[n] ¼¼ zero) && (v[nþ1] ¼¼ zero)) {
hold ¼ zero;
}
else
hold ¼ p_d*v[n] þ p_u*v[nþ1];
if (is_american) {
if (put)
v[n] ¼ MAX(hold, Xs[P1]);
else
v[n] ¼ MAX(hold, s[P1]X);
}
else
v[n] ¼ hold;
P1 ¼ P1 þ 2;
}
}
/* The values v[0], v[1] & v[2] correspond to the nodes for m1 ¼ 2, v[3] & v[4] correspond to the nodes for m1 ¼ 1
and the option value (*value) is the node for m1 ¼ 0, v[5]. For a given time step v[0] corresponds to the
lowest asset price, v[1] to the next lowest etc.. */
jj ¼ 2;
for (m1 ¼ 2; m1 >¼ 1; m1) {
ind ¼ Mm1þ1;
for (n ¼0; n < m1; þþn) {
hold ¼ p_d*v[5jjm11] þ p_u*v[5jjm1];
if (is_american) {
if (put)
v[5jj] ¼ MAX(hold, Xs[ind]);
else
v[5jj] ¼ MAX(hold, s[ind]X);
}
else
v[5jj] ¼ hold;
jj;
ind ¼ ind þ 2;
}
}
*value ¼ v[5];
if(greeks){
/* assign the value of delta (obtained from m1 ¼ 1) */
greeks[1] ¼ (v[4]v[3])/(s[Mþ1]s[M1]);
/* assign the value of gamma (use the values at time step m1 ¼ 2) */
dv1 ¼ v[2]  v[1];
ds1 ¼ s[Mþ2]  s[M];
dv2 ¼ v[1]  v[0];
ds2 ¼ s[M]  s[M2];
h ¼ 0.5*(s[Mþ2]  s[M2]);
greeks[0] ¼ ((dv1/ds1)  (dv2/ds2))/h;
/* assign the value of theta */
greeks[2] ¼ (v[1]*value)/(2.0*dt); /* can also write:y greeks[2] ¼ (v[1]v[5])/(2.0*dt); */
}
Code excerpt 10.11
Function to compute the value of an option using a standard binomial lattice
The implied volatility of American options can be computed using the method
outlined for European options in Section 9.3.4; however in this case the option value
and Greeks are computed using a binomial lattice.
10.4.3
Binomial lattice with a control variate
The control variate technique can be used to enhance the accuracy that a standard
binomial lattice gives for the value of an American vanilla option. It involves using
Numeric methods and single asset American options
151

the same standard binomial lattice to value of both an American option and also the
equivalent European option. The Black–Scholes formula is then used to compute
the accurate value of the European option. If we assume that the error in pricing the
European option is the same as that for the American option we can achieve an
improved estimate for the value of the American option.
When applied to the valuation of an American put option this can be expressed as
follows:
European pricing error,
E ¼ pBSðS; E; Þ  pLðS; E; Þ
American pricing error,
A ¼ P	ðS; E; Þ  PLðS; E; Þ
where as usual S is the current value of the asset, E is the strike price, and  is the
maturity of the option. Also pBS(S, E, ) is the Black–Scholes value of the European
put option, pL(S, E, ) is the binomial lattice estimate of the European put option,
P	(S, E, ) is the (unknown) accurate value of the American put option and
PL(S, E, ) is the binomial lattice estimate of the American put option.
Letting E ¼ A we then have
pBSðS; E; Þ  pLðS; E; Þ ¼ P	ðS; E; Þ  PLðS; E; Þ
which on rearrangement yields:
P	ðS; E; Þ ¼ pBSðS; E; Þ  pLðS; E; Þ þ PLðS; E; Þ
We thus use P	(S, E, ) as the improved, control variate estimate, for the value of
American put option. Of course exactly the same approach can be used to obtain an
improved estimate for the value of an American call.
Code excerpt 10.12 shows the use of the control variate technique in a standard
binomial lattice to provide improved estimates for both the value and the hedge
statistics of an American option.
/* Set up the arrays as in the standard lattice */



for (i ¼ 0; i < (Mþ1)/2; þþi) { /* Calculate the option values at maturity */
if (put){
a_v[Mi] ¼ MAX(X  s[P1], zero);
a_v[i] ¼ MAX(X  s[P2], zero);
}
else {
a_v[Mi] ¼ MAX(s[P1]X, zero);
a_v[i] ¼ MAX(s[P2]X, zero);
}
e_v[i] ¼ a_v[i];
e_v[Mi] ¼ a_v[Mi];
P1 ¼ P1  2;
P2 ¼ P2 þ 2;
}
/* now work backwards through the lattice to calculate the current option value */
P2 ¼ 0;
for (m1 ¼ M1; m1 >¼ 2; m1) {
P2 ¼ P2 þ 1;
P1 ¼ P2;
for (n ¼0; n <¼ m1; þþn){
if ((a_v[n] ¼¼ zero) && (a_v[nþ1] ¼¼ zero))
152
Pricing Assets

hold ¼ zero;
else
hold ¼ p_d*a_v[n] þ p_u*a_v[nþ1];
if (put)
a_v[n] ¼ MAX(hold, Xs[P1]);
else
a_v[n] ¼ MAX(hold, s[P1]X);
if ((e_v[n] ¼¼ zero) && (e_v[nþ1] ¼¼ zero))
e_v[n] ¼ zero;
else
e_v[n] ¼ p_d*e_v[n] þ p_u*e_v[nþ1];
P1 ¼ P1 þ 2;
}
}
/* The American values are stored in the array a_v, and the European values in the array e_v. The array
indexing is the same as for the standard lattice */
jj ¼ 2;
for (m1 ¼ 2; m1 >¼ 1; m1) {
ind ¼ Mm1þ1;
for (n ¼0; n < m1; þþn) {
hold ¼ p_d*a_v[5jjm11] þ p_u*a_v[5jjm1];
if (put)
a_v[5jj] ¼ MAX(hold, Xs[ind]);
else
a_v[5jj] ¼ MAX(hold, s[ind]X);
e_v[5jj] ¼ p_d*e_v[5jjm11] þ p_u*e_v[5jjm1];
jj;
ind ¼ ind þ 2;
}
}
/* v1 ¼ American binomial approximation, v2 ¼ European Binomial approximation, temp ¼ exact (European)
Black—Scholes value */
black_scholes(&temp, bs_greeks, S0, X, sigma, T, r, q, put, &iflagx);
*value ¼ (a_v[5]  e_v[5]) þ temp; /* return the control variate approximation */
if(greeks) {
/* assign the value of delta (obtained from m1 ¼ 1) */
a_delta ¼ (a_v[4]a_v[3])/(s[Mþ1]s[M1]);
e_delta ¼ (e_v[4]e_v[3])/(s[Mþ1]s[M1]);
greeks[1] ¼ a_delta  e_delta þ bs_greeks[1];
/* assign the value of gamma (use the values at time step m1 ¼ 2) */
dv1 ¼ a_v[2]  a_v[1];
ds1 ¼ s[Mþ2]  s[M];
dv2 ¼ a_v[1]  a_v[0];
ds2 ¼ s[M]  s[M2];
h ¼ 0.5*(s[Mþ2]  s[M2]);
a_gamma ¼ ((dv1/ds1)  (dv2/ds2))/h;
dv1 ¼ e_v[2]  e_v[1];
dv2 ¼ e_v[1]  e_v[0];
e_gamma ¼ ((dv1/ds1)  (dv2/ds2))/h;
greeks[0] ¼ (a_gamma  e_gamma) þ bs_greeks[0];
/* assign the value of theta */
a_theta ¼ (a_v[1]a_v[5])/(2.0*dt);
e_theta ¼ (e_v[1]e_v[5])/(2.0*dt);
greeks[2] ¼ (a_theta  e_theta) þ bs_greeks[2];
}
Code excerpt 10.12
Function to compute the value and hedge statistics of an American option using a
binomial lattice with a control variate
Finally we should mention that the control variate technique does not just apply to
American vanilla options. The method is quite general and can be used to obtain impro-
ved estimates for any integral (or exotic option) so long as an accurate (closed form)
solution of a similar integral is known. One common use of the control variate method is
to improve the accuracy of Monte Carlo estimates, see Clewlow and Strickland (1999).
10.4.4
The binomial lattice with BBS and BBSR
Here we consider the binomial Black–Scholes (BBS) method and also the binomial
Black–Scholes method with Richardson extrapolation (BBSR), see Broadie and
Numeric methods and single asset American options
153

DeTemple (1996). As with the control variate method discussed in the previous
section, both of these techniques can be used in conjunction with a standard binomial
lattice to improve the computed results.
We will first discuss the BBS method.
The BBS Method
The BBS method is identical to the standard binomial lattice except that in the last time
step (that is just before option maturity) the Black–Scholes formula is used to calculate
the option values at maturity. For an n time step binomial lattice this involves
evaluating the Black–Scholes formula at each of the n nodes in the penultimate time
step, see Figure 10.1. In Code excerpt 10.13 we define the function bs_lattice
which incorporates the BBS method into a standard binomial lattice. The reader will
have noticed that bbs_lattice is rather lax concerning the amount of storage that is
required, see Section 10.4.2. It uses an array of size LN n rather than LSn to store the
lattice asset prices; the modification to use an array of size LSn is left as an exercise.
void bbs_lattice(double *value, double greeks[], double S0, double X, double sigma, double T, double r,
double q, Integer put, Integer M, Integer *iflag)
{
/* Input parameters:
S0
— the current price of the underlying asset
X
— the strike price
sigma
— the volatility
T
— the time to maturity
r
— the interest rate
q
— the continuous dividend yield
put
— if put is 0 then a call option, otherwise a put option
M
— the number of time steps
Output parameters:
value
— the value of the option, greeks[] the hedge statistics output as follows: greeks[0] is
gamma, greeks[1] is delta, greeks[2] is theta,
iflag
— an error indicator.
*/



/* allocate the arrays s[((Mþ2)*(Mþ1))/2], and v[Mþ1] */
dt ¼ T/(double)M;
t1 ¼ sigma*sqrt(dt);
u ¼ exp(t1);
d ¼ exp(t1);
a ¼ exp((rq)*dt);
p ¼ (a  d)/(u  d);
if ((p < zero) || (p > 1.0)) return; /* Invalid probability */
discount ¼ exp(r*dt);
p_u ¼ p*discount;
p_d ¼ (1.0p)*discount;
jj ¼ 0;
s[0] ¼ S0;
/* The ‘‘higher’’ the value of jj, at a given time instant,
the lower the value of the asset price */
for (m1 ¼ 1; m1 <¼ M1; þþm1){/* Calculate asset values up to (M1)th time step */
for (n ¼ m1; n >¼ 1; n){
þþjj;
s[jj] ¼ u*s[jjm1];
}
þþjj;
s[jj] ¼ d*s[jjm11];
}
154
Pricing Assets

for (n ¼ 0; n <¼ M1; þþn){/* Use Black—Scholes for the final step */
black_scholes(&temp, NULL, s[jj], X, sigma, dt, r, q, put, &iflagx);
v[n] ¼ temp;
jj;
}
for (m1 ¼ M1; m1 >¼ 3; m1){/* work backwards through the lattice */
for (n ¼0; n < m1; þþn){
if ((v[n] ¼¼ zero) && (v[nþ1] ¼¼ zero)){
hold ¼ zero;
}
else
hold ¼ p_d*v[n] þ p_u*v[nþ1];
if (is_american){
if (put)
v[n] ¼ MAX(hold, Xs[jj]);
else
v[n] ¼ MAX(hold, s[jj]X);
}
else
v[n] ¼ hold;
jj;
}
}
/* The values v[0], v[1] & v[2] correspond to the nodes for m1 ¼ 2, v1 & v2 correspond to the nodes for m1 ¼ 1
and the option value (*value) is the node for m1 ¼ 0. For a given time step v[0] corresponds to the lowest
asset price, v[1] to the next lowest etc.. */
hold ¼ p_d*v[0] þ p_u*v[1];
if (is_american){
if (put)
v1 ¼ MAX(hold, Xs[jj]);
else
v1 ¼ MAX(hold, s[jj]X);
}
else
v1 ¼ hold;
jj;
hold ¼ p_d*v[1] þ p_u*v[2];
if (is_american){
if (put)
v2 ¼ MAX(hold, Xs[jj]);
else
v2 ¼ MAX(hold, s[jj]X);
}
else
v2 ¼ hold;
jj;
hold ¼ p_d*v1 þ p_u*v2;
if (is_american){
if (put)
*value ¼ MAX(hold, Xs[0]);
else
*value ¼ MAX(hold, s[0]X);
}
else
*value ¼ hold;
if(greeks){
/* assign the value of delta (obtained from m1 ¼ 1) */
greeks[1] ¼ (v2v1)/(s[1]s[2]);
/* assign the value of gamma (use the values at time step m1 ¼ 2) */
dv1 ¼ v[2]  v[1];
ds1 ¼ s[3]  s[4];
dv2 ¼ v[1]  v[0];
ds2 ¼ s[4]  s[5];
h
¼ 0.5*(s[3]  s[5]);
greeks[0] ¼ ((dv1/ds1)  (dv2/ds2))/h;
/* assign the value of theta */
greeks[2] ¼ (v[1]*value)/(2.0*dt);
}
}
Code excerpt 10.13
The function bbs_lattice which incorporates the BBS method into a standard
binomial lattice. The Black–Scholes formula is evaluated by using the function black_scholes, given in
Section 9.3.3
Numeric methods and single asset American options
155

The benefits of using the BBS approach to price an American call are illustrated in
Figure 10.3. Here we compare the results obtained using the function bbs_lattice
with those computed by the function standard_lattice, the standard binomial
lattice of Code excerpt 10.11. It can be clearly seen that BBS method is significantly
more accurate than the standard binomial lattice approach, in which option pricing
error exhibits pronounced oscillations.
The BBSR Method
The BBSR method applies two point Richardson extrapolation to the computed BBS
values, for more information concerning Richardson extrapolation see Marchuk and
Shaidurov (1983). In this method the option price estimates from two BBS lattice,
with differing number of time steps, are combined to form an improved estimate.
Here we use the following BBSR scheme to compute the value of an American
call option
CBBSRðS; E; ; 2nÞ ¼ 4
3 CBBSðS; E; ; 2nÞ  1
3 CBBSðS; E; ; nÞ
ð10:96Þ
where S is the current asset value, E is the strike price,  is the option maturity,
CBBS(S, E, , n) is the value of the call option computed using a BBS lattice with
American call
Error in estimated value
Number of time steps
0
10
20
30
40
50
60
70
80
90
100
0.2
0.1
0
–0.1
–0.2
–0.3
–0.4
0.3
Standard lattice
BBS lattice
Figure 10.3
The error in the estimated value, est val, of an American call using both a standard binomial
lattice and BBS binomial lattice. The parameters used were: T ¼ 1:0, S ¼ 105:0, E ¼ 105:0, r ¼ 0:1,
q ¼ 0:02,  ¼ 0:3. The very accurate value (acc val) was 16.1697, and was computed using a 6000 step
standard binomial lattice. The error in the estimated value was obtained as est val  acc val
156
Pricing Assets

n time steps, CBBS(S, E, , 2n) is the value of the call option computed using a BBS
lattice with 2n time steps and CBBSR(S, E, , 2n) is the BBSR estimate. We compute
the value of an American put using
PBBSRðS; E; ; 2nÞ ¼ 4
3 PBBSðS; E; ; 2nÞ  1
3 PBBSðS; E; ; nÞ
ð10:97Þ
Figure 10.4 displays the computed BBSR results for an American call option with
S ¼ 105:0,  ¼ 1:0, E ¼ 105:0, q ¼ 0:02, and  ¼ 0:3.
In Tables 10.5 and 10.6 the errors in computing both an American put and an
American call option are presented; the methods used are the standard binomial
lattice, the BBS lattice and the BBSR lattice. It can be seen that the BBSR lattice
gives the most accurate results. This is not surprising since, from Equations 10.96 and
10.97 we see that when we use either an n time step standard binomial lattice or an
n time step BBS lattice the corresponding BBSR estimate is obtained using both an
n time step BBS lattice and also a 2n time step BBS lattice. One way of checking
whether Richardson extrapolation is providing increased accuracy is to compare the
results for a 2n time step BBS lattice with those for an n time step BBSR lattice.
Inspection of the results shows that Richardson extrapolation has in fact led to an
improvement. For example in Table 10.5 the error for a 160 time step BBS lattice is
Richardson extrapolation: American call
0.035
0.03
0.025
0.02
0.015
0.01
0.005
0
0
10
20
30
40
50
60
70
80
90
100
Number of time steps
Error in estimated value
Figure 10.4
The error in the estimated value, est val, of an American call, using a BBSR binomial lattice.
The parameters used were: T ¼ 1:0, S ¼ 105:0, E ¼ 105:0, r ¼ 0:1, q ¼ 0:02,  ¼ 0:3. The very accurate
value (acc val) was 16.1697, and was computed using a 6000 step standard binomial lattice. The error in the
estimated value was obtained as est val  acc val
Numeric methods and single asset American options
157

Table 10.5
The pricing errors for an American call option computed by a standard binomial lattice, a BBS
lattice and also a BBSR lattice. The pricing error is defined as estimated value  accurate value, where the
accurate value, 16.1697, was obtained by using a 6000 step standard binomial lattice. The option parameters
used were: T ¼ 1:0, S ¼ 105:0, E ¼ 105:0, r ¼ 0:1, q ¼ 0:02, and  ¼ 0:3
n steps
Standard lattice
BBS lattice
BBSR lattice
20
1.5075e-001
3.6187e-002
1.2754e-002
30
1.0057e-001
2.4526e-002
8.6771e-003
40
7.5382e-002
1.8612e-002
6.6361e-003
50
6.0244e-002
1.5036e-002
5.4109e-003
60
5.0141e-002
1.2639e-002
4.5939e-003
70
4.2919e-002
1.0922e-002
4.0103e-003
80
3.7499e-002
9.6302e-003
3.5725e-003
90
3.3282e-002
8.6236e-003
3.2320e-003
100
2.9908e-002
7.8171e-003
2.9596e-003
110
2.7146e-002
7.1565e-003
2.7367e-003
120
2.4844e-002
6.6053e-003
2.5509e-003
130
2.2896e-002
6.1385e-003
2.3938e-003
140
2.1226e-002
5.7382e-003
2.2590e-003
150
1.9778e-002
5.3909e-003
2.1423e-003
160
1.8511e-002
5.0869e-003
2.0401e-003
170
1.7393e-002
4.8186e-003
1.9500e-003
180
1.6399e-002
4.5799e-003
1.8698e-003
190
1.5510e-002
4.3663e-003
1.7981e-003
200
1.4710e-002
4.1740e-003
1.7336e-003
Table 10.6
The pricing errors for an American put option computed by a standard binomial lattice, a BBS
lattice and also a BBSR lattice. The pricing error is defined as estimated value  accurate value, where the
accurate value, 9.2508, was obtained by using a 6000 step standard binomial lattice. The option parameters
used were: T ¼ 1:0, S ¼ 105:0, E ¼ 105:0, r ¼ 0:1, q ¼ 0:02, and  ¼ 0:3
n steps
Standard lattice
BBS lattice
BBSR lattice
20
6.1971e-002
2.3917e-002
7.6191e-003
30
4.1648e-002
1.6800e-002
6.0465e-003
40
3.2264e-002
1.1694e-002
4.6165e-003
50
2.6538e-002
8.4790e-003
4.2654e-003
60
2.1069e-002
8.7348e-003
3.2946e-003
70
1.8298e-002
7.2743e-003
2.9633e-003
80
1.5885e-002
6.3858e-003
2.6088e-003
90
1.3977e-002
5.9417e-003
2.2099e-003
100
1.2612e-002
5.3188e-003
2.1793e-003
110
1.1338e-002
4.9652e-003
2.0992e-003
120
1.0239e-002
4.6547e-003
1.8723e-003
130
9.5208e-003
4.1505e-003
1.8808e-003
140
8.6142e-003
4.0411e-003
1.7505e-003
150
8.2382e-003
3.6020e-003
1.7341e-003
160
7.5811e-003
3.5531e-003
1.6411e-003
170
7.1097e-003
3.3726e-003
1.5507e-003
180
6.7887e-003
3.1428e-003
1.5478e-003
190
6.3033e-003
3.1345e-003
1.4134e-003
200
6.0276e-003
2.9642e-003
1.3973e-003
158
Pricing Assets

5:0869  103, while that for an 80 time step BBSR lattice is 3:5725  103; in Table
10.6 the error for an 80 time step BBS lattice is 6:3858  103 and that for a 40 time
step BBSR lattice is 3:5725  103.
10.5
IMPLIED LATTICE METHODS
It is well known that market option prices are not consistent with theoretical prices
derived from the Black–Scholes formula. This has led traders to quote option prices
in terms of a volatility, imp, which makes the Black–Scholes formula value equal to
the observed market price. Here we refer to imp as the implied volatility, to distinguish
it from the theoretical constant volatility ; essentially imp is another way of quoting
option prices. Empirical studies have found that:
. For vanilla options of a given maturity the value of imp decreases with the level of
the strike price, this asymmetry is termed volatility skew.
. For vanilla options of a given strike price the value of imp increases with maturity,
this variation is called the volatility term structure.
Here we follow Derman and Kani (1994) and refer to both the volatility skew and
the volatility term structure as the volatility smile. The precise shape and magnitude
of the volatility smile is dependent on the nature of the option being considered.
We are thus led to consider more sophisticated option pricing methods which capture
the observed deviations from these Black–Scholes formula.
Instead of assuming, as in Section 8.3, that the underlying asset price St follows GBM
with constant drift and volatility, we will now consider the more general GBM process:
dSt
St
¼ ðtÞdt þ ðSt; tÞdZ
ð10:98Þ
where t is the current time, (t) is the time dependent risk neutral drift and (St, t) is an
unknown volatility function which depends on both the stock price and time. If we
make use of Ito’s lemma, and write Stþt for the asset price at time t þ t, Equation
10.84 can be expressed in discretized form as:
log Stþt
St


¼
ðtÞ  2ðSt; tÞ=2
	

t þ ðSt; tÞdZ
ð10:99Þ
or equivalently
log Stþt
St



 N
ðtÞ  2ðSt; tÞ=2
	

t; 2ðSt; tÞt


ð10:100Þ
In this section we will show how the volatility function (St, t) can be evaluated by
ensuring that the option prices calculated using this model agree with those of the smile.
The implied binomial lattice constructed using this extended model will no longer
be a regular lattice (as is the case for the simple Black–Scholes model) but will have a
distorted shape similar to that shown in Figure 10.5 below.
It can be seen that the lattice levels are equispaced in time and are t apart. Lattice
level 1, time t1, corresponds to the root node (1, 1) and is the current time, at which
Numeric methods and single asset American options
159

we want to find the value of the option. Time tn, associated with lattice level n, is
given by:
tn ¼ t1 þ ðn  1Þt ¼ t þ ðn  1Þt
so tn is (n  1)t in the future relative to the current time t.
Construction of the implied lattice requires option prices for the complete range of
strikes and maturities; these values can be obtained via interpolation from known
option prices that are traded on the stock market.
Once the implied lattice has been created it can be used to price a range of
European and American options.
Here we will describe the implied lattice technique developed by Derman and Kani
(1994), and then consider the subsequent refinements proposed by Barle and Cakici
(1995) and Chriss (1997). Of necessity our description of these techniques will be
brief, and will mainly consist of explanatory detail and mathematical proofs that
are not given in the original papers. For more information the reader should consult the
original papers which are available (by kind permission of RISK Magazine) on
the CD ROM which accompanies this book.
(7,6)
(3,3)
(5,2)
(1,1)
S
(7,1)
1
2
3
4
5
6
7
Lattice level (n)
0
1
2
3
4
5
6
Time (in units of ∆t)
Asset price
Figure 10.5
An implied binomial lattice which incorporates the volatility smile observed in traded put and
call options. The ith node at the nth lattice level is denoted by (n, i). The current value (at time t) of the
underlying asset is S, and this is the asset value assigned to the root lattice node (1, 1). The asset values at
the other lattice nodes depend on the technique used to construct the implied lattice
160
Pricing Assets

Before discussing the details of implied binomial lattices we will first consider the
local volatility associated with a particular lattice node.
Local volatility
An expression for the stock volatility at the binomial lattice node (n, i) will now be
derived. At time instant tn the stock value at this node is denoted by si. After time t,
time instant tnþ1, the stock price either has jumped up to Su, at lattice node
(n þ 1, i þ 1), or jumped down to Sd, at lattice node (n þ 1, i). Applying Equation
10.100 to node (n, i) by setting t ¼ tn and St ¼ si then gives
v 
 N
ðtnÞ  2ðsi; tnÞ=2
	

t; 2ðsi; tnÞt


ð10:101Þ
where the variate v can only take the two values v1 ¼ log(Su=si), and v2 ¼ log(Sd=si).
We will let pi denote the probability of taking the value v1, corresponding to an up
jump. The probability of v having the value v2, corresponding to a down jump, is
thus 1  pi.
The quantity (si, tn) will be referred to as the local volatility, loc, associated with
the lattice node (n, i), and using Equation 10.101 we can write
VarðvÞ ¼ 2
loct
ð10:102Þ
An expression for loc can then be obtained in terms of Su, Sd and pi, as follows.
The variance of v is:
VarðvÞ ¼ E½v2  ðE½vÞ2
where
E½v2 ¼ pi
log Su
si



2
þð1  piÞ log Sd
si



2
and
ðE½vÞ2 ¼
pi log Su
si


þ ð1  piÞ log Sd
si



2
which means that
ðE½vÞ2 ¼ p2
i
log Su
si



2
þ ð1  piÞ2
log Sd
si



2
þ 2pið1  piÞ log Su
si


log Sd
si


We can therefore write the variance as
VarðvÞ ¼ pi
log Su
si



2
þ ð1  piÞ log Sd
si



2
 p2
i
log Su
si



2
 ð1  piÞ2
log Sd
si



2
 2pið1  piÞ log Su
si


log Sd
si


Numeric methods and single asset American options
161

which simplifies to
VarðvÞ ¼ pið1  piÞ
log Su
si



2
þ
log Sd
si



2
 2 log Su
si


log Sd
si


"
#
ð10:103Þ
However
log Su
si


 log Sd
si


¼ log Su
Sd


and
log Su
si


 log Sd
si



2
¼
log Su
si



2
þ
log Sd
si



2
 2 log Su
si


log Sd
si


Substituting this into Equation 10.103 we obtain:
VarðvÞ ¼ pið1  piÞ log Su
Sd



2
ð10:104Þ
Therefore combining Equations 10.102 and 10.104 we have
2
loct ¼ pið1  piÞ log Su
Sd



2
and so the local volatility is given by:
Binomial lattice: local volatility
loc ¼ log Su
Sd


ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
pið1  piÞ
t
r
ð10:105Þ
In an implied lattice the transition probabilities, pi, and the ratios Su=Sd are (in
general) different for each lattice node. This generates a volatility surface in which the
local volatility loc varies throughout the lattice. By contrast the CRR binomial
lattice of Section 10.4.1 has the same value of loc for all its lattice nodes. The reason
for this that pi and t are constants, and the up and down jumps are
Su ¼ siu
and
Sd ¼ sid;
where
u ¼ 1
d
This means that
Su
Sd
¼ u2
and the (constant) local volatility is
loc ¼ logðu2Þ
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
pð1  pÞ
t
r
162
Pricing Assets

CRR binomial lattice: local volatility
loc ¼ 2 logðuÞ
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
pð1  pÞ
t
r
ð10:106Þ
where we have denoted the (constant) CRR up jump probability by p.
10.5.1
Derman–Kani implied lattice
We now consider the paper by Derman–Kani (1994), henceforth referred to as DK,
which describes an implied binomial lattice based on the market values of European
put and call options.
The implied lattice (see Figure 10.5) consists of uniformly spaced levels t apart, and
is built using forward iteration. To explain this technique we will assume that the first n
lattice levels have been constructed and that they match the observed volatility smile for
all strike prices and maturities out to time tn. The task is to determine the n þ 1 nodes at
the (n þ 1)th lattice level from the previously calculated n nodes at the nth lattice level.
For convenience we will now give the notation used in the formulae for construct-
ing the lattice nodes in the (n þ 1)th lattice level from the known lattice node values in
the nth lattice level.
r
The known riskless interest rate for lattice level (n þ 1).
si
The known stock price at node (n, i); that is at the ith node on lattice level n.
We also note that si is the strike price for options expiring at lattice level n þ 1.
Fi
The known forward price at lattice level n þ 1 of the known price si at lattice
level n.
Si
The unknown stock price at node (n þ 1, i).
i
The known Arrow-Debreu price at node (n, i).
pi
The unknown risk-neutral up jump transition probability from node (n, i) to
node (n þ 1, i þ 1).
Here the ith node at level n has known stock price si, and is denoted by (n, i). The
probability that the stock price si increases to Siþ1 in lattice level n þ 1 is denoted by pi,
whereas the probability that the stock price decreases to Si in level n þ 1 is given by 1  pi.
The forward price, Fi, of si at lattice level n þ 1 is simply given by the risk neutral
expected value of si one time step later. That is Fi ¼ si exp (rt), or in terms of the up
and down jump probabilities pi and (1  pi) respectively we have:
Fi ¼ piSiþ1 þ ð1  piÞSi;
for i ¼ 1; . . . ; n
ð10:107Þ
where as before Siþ1 is the stock value at lattice level n þ 1 following an up jump and
Si is the stock value at lattice level n þ 1 following a down jump.
The Arrow-Debreu price, i, at each lattice node (n, i) is defined as: the probability
of reaching node (n, i) from the root lattice node (1, 1) discounted by the risk neutral
interest rate between time t1 and time tn.
Numeric methods and single asset American options
163

The Arrow-Debreu price of a lattice node is thus the value of a security that pays
$1 if the stock price reaches that node and zero otherwise. The value of i
corresponding to node (n, i) is computed as the sum, over all paths from the root
node (1, 1) to node (n, i), of the product of the riskless-discounted transition prob-
abilities of nodes along each path from (1, 1) to (n, i). We provide more detail
concerning the computation of i in the example calculation at the end of this
section, and consider the following two methods:
1. Direct calculation of the Arrow-Debreu prices in lattice level n þ 1 by using all
paths from the root lattice node (1, 1).
2. Iterative calculation of the Arrow-Debreu prices in lattice level n þ 1 from the
known Arrow-Debreu prices in lattice level n.
It is shown that direct calculation of the Arrow-Debreu prices becomes substantially
more complicated as the number of lattice level increases. This is because the number of
possible paths from the root node (1, 1) to any given lattice node (n þ 1, i) increases
dramatically with n. The iterative approach is thus the most practical method for
computing Arrow-Debreu prices in lattices containing more than just a few lattice levels.
Let C(K, tnþ1) and P(K, tnþ1) be the current, time t, respective prices of European
call and European put options with strike K and maturity corresponding to lattice
level n þ 1; the values C(K, tnþ1) and P(K, tnþ1) can be obtained via interpolation
from the known market prices. An expression for C(K, tnþ1), can also be computed
by using the binomial node values at lattice level n, and this method yields the
following equation:
CðK; tnþ1Þ ¼ expðrtÞ
X
n
j¼1
jfpj maxðSjþ1  K; 0Þ
þ ð1  pjÞ max ðSj  K; 0Þg
ð10:108Þ
where max (Sj  K, 0) is the payout for the call at the jth lattice node on lattice level
n þ 1 and max (Sjþ1  K, 0) is the payout for the call at the ( j þ 1)th lattice node on
lattice level n þ 1.
When the strike K equals si the above equation becomes
expðrtÞCðsi; tnþ1Þ ¼
X
n
j¼1
jfpj maxðSjþ1  si; 0Þ
þ ð1  pjÞ maxðSj  si; 0Þg
ð10:109Þ
Since the terms that contribute to the value of the call option, C(si, tnþ1), are those
with positive payouts we only need consider j indices in the range i to n, and the ith
term of the summation on the right hand side of Equation 10.109 is:
i pi maxðSiþ1  si; 0Þ þ ð1  piÞ maxðSi  si; 0Þ
f
g ¼ ipiðSiþ1  siÞ
ð10:110Þ
where we have used (see DK Figure 4) the following: Siþ1 > si (Siþ1 is the up jump
stock value from lattice level n to lattice level n þ 1) whereas Si < si (Si is the down
jump stock value from lattice level n to lattice level n þ 1).
164
Pricing Assets

This means that we can rewrite Equation 10.109 as:
expðrtÞCðsi; tnþ1Þ ¼ ipiðSiþ1  siÞ þ
X
n
j¼iþ1
jfpjðSjþ1  siÞ
þ ð1  pjÞðSj  siÞg
ð10:111Þ
If we subtract the constant term si from both sides of Equation 10.107 we obtain:
Fj  si ¼ pj ðSjþ1  siÞ þ ð1  pjÞðSj  siÞ; j ¼ 1; . . . ; n
ð10:112Þ
where we used si ¼ pjsi þ (1  pj)si. Substituting Equation 10.112 into Equation
10.111 gives:
expðrtÞCðsi; tnþ1Þ ¼ ipi ðSiþ1  siÞ þ 
ð10:113Þ
where  ¼ Pn
j¼iþ1 j(Fj  si). The first term in Equation 10.113 depends on the
unknown values of the transition probability pi and stock price Siþ1. The last
term  involves a summation over the known forward prices Fj and known stock
prices si on lattice level n. Since both Fj and C(si, tnþ1) are known, Equations
10.107 and 10.113 can be solved to give the following expressions for Siþ1 and pi,
in terms of Si:
pi ¼ Fi  Si
Siþ1  Si
ð10:114Þ
and
Siþ1 ¼ Si Cðsi; tnþ1Þ expðrtÞ  
	

 isiðFi  SiÞ
Cðsi; tnþ1Þ expðrtÞ  
	

 iðFi  SiÞ
ð10:115Þ
We will now derive these two results.
Proof of Equation 10.114 (DK equation 7)
From Equation 10.107 we have:
Fi ¼ piSiþ1 þ ð1  piÞSi
which gives:
Fi ¼ piðSiþ1  SiÞ þ Si
and
pi ¼ Fi  Si
Siþ1  Si
QED
Proof of Equation 10.115 (DK equation 6)
If we substitute the value of pi from Equation 10.115 into Equation 10.113 we obtain:
Cðsi; tnþ1Þ expðrtÞ ¼ iðFi  SiÞðSiþ1  siÞ
Siþ1  Si
þ 
Numeric methods and single asset American options
165


## Multi-Asset Options

Multiplying both sides by Siþ1  Si yields:
expðrtÞCðsi; tnþ1Þ Siþ1  Si
f
g ¼ iFisi  iSiSiþ1 þ iFiSiþ1 þ iSi þ Siþ1   Si 
so
Siþ1 Cðsi; tnþ1Þ expðrtÞ þ iSi  iFi  
	

¼ SiCðsi; tnþ1Þ expðrtÞ  isiðFi  SiÞ  Si 
or
Siþ1 Cðsi; tnþ1Þ expðrtÞ    iðFi  SiÞ
	

¼ Si Cðsi; tnþ1Þ expðrtÞ  
	

 isiðFi  SiÞ
and finally gives the following expression for Siþ1:
Siþ1 ¼ Si Cðsi; tnþ1Þ expðrtÞ  
	

 isiðFi  SiÞ
Cðsi; tnþ1Þ expðrtÞ  
	

 iðFi  SiÞ
QED
If we know Si at one initial node then Equations 10.114 and 10.115 can be used to
find iteratively the values of Siþ1 and pi for all n=2 þ 1 nodes above the centre of the
lattice on the (n þ 1)th lattice level.
If n þ 1 is odd then the initial value used for Si is the stock value associated with
the central lattice node, that is Si ¼ S. On the other hand if n þ 1 is even then we use
the CRR lattice centering condition (see Section 10.4.1). Let Siþ1 denote the
(n þ 1)th level stock value for the node just above the centre of the lattice, and Si
denote the (n þ 1)th level stock value just below the centre of the lattice. For a CRR
(u ¼ 1=d) lattice these values are related to the central node stock value, S, at lattice
level n by:
Siþ1 ¼ Su
and
Si ¼ Sd ¼ S
u
and therefore
Siþ1Si ¼ S2
ð10:116Þ
Substituting Equation 10.116 into Equation 10.114 gives the following formula for
the stock value at the node just above the centre of the lattice when n þ 1 is even:
Siþ1 ¼ Sð þ iSÞ
iFi   ;
for
i ¼
n þ 1
2


ð10:117Þ
where  ¼ C(S, tnþ1) exp (rt)  .
When n þ 1 is even, Equation 10.117 can thus be used in conjunction with Equa-
tions 10.114 and 10.115 to iteratively compute the node values Siþ1 and probabilities
pi for the (n þ 1)=2 nodes above the lattice centre.
166
Pricing Assets

Proof of Equation 10.117 (DK equation 8)
From Equation 10.114 we have that the probability pi is given by:
pi ¼ Fi  Si
Siþ1  Si
¼ ðFi  SiÞSiþ1
ðSiþ1  SiÞSiþ1
since, in Equation 10.116, SiSiþ1 ¼ S2 we obtain:
pi ¼ FiSiþ1  S2
S2
iþ1  S2 ¼
FiSiþ1  S2
ðSiþ1  SÞðSiþ1 þ SÞ
However from Equation 10.113
expðrtÞCðsi; tnþ1Þ ¼ ipiðSiþ1  siÞ þ 
so
 ¼ ipiðSiþ1  siÞ
ð10:118Þ
When si ¼ S we therefore have:
 ¼ ipiðSiþ1  SÞ ¼ iðFiSiþ1  S2ÞðSiþ1  SÞ
ðSiþ1  SÞðSiþ1 þ SÞ
¼ iðFiSiþ1  S2Þ
Siþ1 þ S
which gives:
Siþ1 þ S ¼ iFiSiþ1  iS2
Siþ1ð  iFiÞ ¼ Sð þ iSÞ
and finally:
Siþ1 ¼ Sð þ iSÞ
iFi  
QED
Similar formulae can be derived, using interpolated put prices, which enable the
stock values and probabilities for nodes below the lattice centre to be computed. The
formula to determine a lower node’s stock value from an upper node’s stock value is:
Si ¼ Siþ1 Pðsi; tnþ1Þ expðrtÞ  	
f
g  isiðFi  Siþ1Þ
Pðsi; tnþ1Þ expðrtÞ  	
f
g  iðFi  Siþ1Þ
ð10:119Þ
where P(si, tnþ1) is the interpolated price of a put with strike si and expiry time tnþ1
and
	 ¼
X
i1
j¼1
jðsi  FjÞ
denotes the sum over all nodes below the node with stock price si at which the put
was struck.
When building the lattice the computed transition probabilities, pi, for each lattice
node must obey the constraint 0  pi  1. The upper limit pi  1 is equivalent to
Numeric methods and single asset American options
167

requiring that the up-node stock price Siþ1 at the next level does not fall below the
forward price Fi. This result comes from Equation 10.114
pi ¼ Fi  Si
Siþ1  Si
where it can easily be seen that if Fi > Siþ1 then pi > 1. Similarly the lower limit
pi  0 can be shown to be equivalent to requiring that the down-node stock price Si is
above the forward price Fi. From Equation 10.114 we now have:
piþ1 ¼ Fiþ1  Siþ1
Siþ2  Siþ1
and so if Siþ1 > Fiþ1 then piþ1 < 0. We thus have:
Fi < Siþ1 < Fiþ1
ð10:120Þ
which is illustrated in Figure 10.6.
Si + 1
Si + 1
Fi + 1
pi + 1
pi
Si + 2
pi – 1
Si – 1
Fi – 1
Si
Fi
Si
Figure 10.6
An implied lattice showing the position of the stock prices in relation to the forward prices,
between the nth and (n þ 1)th lattice levels. The stock prices in lattice level n are denoted by siþ1, si, and
si1, while those in lattice level n þ 1 are represented by Siþ2, Siþ1, and Si. The transition probabilities
between lattice level n and lattice level n þ 1 are piþ1, pi, and pi1, and the forward prices are Fiþ1, Fi, and
Fi1. If the computed stock value is Siþ1 then, in order to obtain valid transition probabilities, it must
satisfy the constraint Fi < Siþ1 < Fiþ1
168
Pricing Assets

Bad probabilities
Figure 10.6 shows the relative positions of the computed stock values, Si, at lattice
level n þ 1, and the forward prices Fi computed from the stock values, si, at lattice
level n. If a computed stock value, Siþ1, violates the constraints imposed by Equation
10.120 then it is necessary to choose an alternative value for which the transition
probability pi is in the permitted range 0 < pi < 1. DK advocates choosing Siþ1 so
that the logarithmic spacing between adjacent lattice nodes is the same as that in the
previous lattice level; that is:
Siþ1
Si
¼ si
si1
This means replacing the value of Siþ1 computed using Equation 10.115 with
Siþ1 ¼ Si
si
si1


ð10:121Þ
If this method still fails to produce a valid pi then Chriss (1997) suggests the following
more drastic measure in which
Siþ1 ¼ Fi þ 
ð10:122Þ
where  is a very small number (say 106). It can be seen from Equation 10.114 that
the transition probability pi will then be a very small positive number.
When we remove bad probabilities in this manner the impact on the implied lattice
will depend on both the Arrow-Debreu price of the node and its payout. Nodes near
the top and bottom of the lattice will have small Arrow-Debreu prices because few
paths lead to them, and thus removing bad probabilities from these nodes will have
little impact on the lattice. When building an implied lattice it is a good idea to count
how many bad nodes have been encountered; this will give some idea of the expected
quality of the implied lattice that has been constructed. A more quantitative method
of assessing the expected performance of an implied lattice is by checking how well it
prices the put and call options that were originally used to create it.
Example calculation
Here we provide more details concerning the example calculation given in the paper
by Derman and Kani (1994). The implied lattice for this example is shown in Figures
10.7 and 10.8. It is assumed that the current stock value is 100.00, the dividend is
zero, and the annually compounded riskless interest rate is 3 per cent a year for all
option maturities. Since we have assumed a constant riskless interest of 3 per cent the
forward price Fi for any node is 1.03 times the node’s stock price, si.
Computation of the Arrow-Debreu prices
We have already mentioned that the Arrow-Debreu price for node (n, i) is computed
as the sum, over all paths from the root node (1, 1) to node (n, i), of the product of
the riskless-discounted transition probabilities of nodes along each path from (1, 1)
Numeric methods and single asset American options
169

100.00
100.00
100.00
110.52
110.60
120.27
130.09
139.78
120.51
90.48
90.42
79.30
79.43
71.39
59.02
Figure 10.7
Implied binomial lattice showing the stock values at each node; from DK Figure 6
1.000
0.364
0.116
0.052
0.015
0.106
0.529
0.329
0.181
0.607
0.402
0.425
0.266
0.381
0.216
0.289
0.711
0.334
0.666
0.322
0.678
0.300
0.700
0.682
0.318
0.624
0.376
0.541
0.459
0.329
0.671
0.318
0.682
0.375
0.625
Figure 10.8
An implied lattice showing the Arrow-Debreu prices (in bold) and also the transition
probabilities between nodes (in a smaller font); from DK Figure 6.
170
Pricing Assets

to (n, i). Here we provide more detail and show how the Arrow-Debreu prices can be
computed for the first four lattice levels.
Level 1: Node (1, 1) 1 ¼ 1:0.
Level 2: Node (2, 2): There is only one route from node (1, 1) to node (2, 2) and path
probability is 0.625. Discounting the path probability by the riskless rate of 3 per cent
gives the Arrow-Debreu price:
2 ¼ 0:625
1:03 ¼ 0:6068
Node (2, 1): As for node (2, 2) there is only one route from node (1, 1) and the path
probability is 1  0:625 ¼ 0:375. Discounting by the riskless rate gives the Arrow-
Debreu price:
1 ¼ 0:375
1:03 ¼ 0:3641
Level 3: Node (3, 3): There is only one route from node (1, 1) to node (3, 3) and the
path probability is 0:625  0:682 ¼ 0:42625. Discounting by the riskless rate of 3 per
cent over two time steps yields the Arrow-Debreu price:
3 ¼
0:42625
1:03  1:03 ¼ 0:40178
Node (3, 2): There are two ways of going from node (1, 1) to node (3, 2). The first way,
route (a) includes the nodes (1, 1), (2, 2), and (3, 2); it has a path probability of
0:625  0:318 ¼ 0:19875. The contribution of route (a) to 2, denoted as a
2, is therefore
a
2 ¼ 0:19875=(1:03  1:03) ¼ 0:18734. The second way, route (b) includes the nodes
(1, 1), (2, 1), and (3, 2); it has a path probability of 0:375  0:671 ¼ 0:2516. The con-
tribution of route (b) to 2, denoted as b
2, is thus b
2 ¼ 0:2516=(1:03  1:03) ¼ 0:23718.
The Arrow-Debreu price, 2, is therefore:
2 ¼ a
2 þ b
2 ¼ 0:18734 þ 0:23718 ¼ 0:4245
Node (3, 1): There is only one route from node (1, 1) to node (3, 1), and the path
probability is 0:375  0:329 ¼ 0:12337. Discounting by the riskless rate of 3 per cent
gives an Arrow-Debreu price:
1 ¼
0:12337
1:03  1:03 ¼ 0:11629
Level 4: Node (4, 4): There is only one route from node (1, 1) to node (4, 4), and the
path probability is 0:625  0:682  0:682 ¼ 0:29070. Discounting by the riskless rate
of 3 per cent over three time steps gives an Arrow-Debreu price:
4 ¼
0:26768
1:03  1:03  1:03 ¼ 0:2660
Node (4, 3): There are three ways of going from node (1, 1) to node (4, 2). The first
way, route (a) includes the nodes (1, 1), (2, 2), (3, 3), and (4, 3). The second way,
route (b) includes the nodes (1, 1), (2, 2), (3, 2), and (4, 3). Finally the third way,
route (c) includes the nodes (1, 1), (2, 1), (3, 2), and (4, 2).
Numeric methods and single asset American options
171

The path probability for route (a) is 0:625  0:682  0:316 ¼ 0:1347, and thus
yields an Arrow-Debreu price a
3 ¼ 0:1347=(1:03  1:03  1:03) ¼ 0:1233. The path
probability for route (b) is 0:375  0:671  0:624 ¼ 0:12402, and gives an Arrow-
Debreu price of b
3 ¼ 0:12402=(1.03  1.03  1.03) ¼ 0.1135.
Finally the path probability for route (c) is 0:375  0:671 0:624 ¼ 0:157014,
and c
3 ¼ 0:157014=(1:03  1:03  1:03) ¼ 0:1437. The Arrow-Debreu price, 3, is
therefore:
3 ¼ a
3 þ b
3 þ c
3 ¼ 0:1233 þ 0:1135 þ 0:1437 ¼ 0:3805
Node (4, 2): There are three ways of going from node (1, 1) to node (3, 2). The first
way, route (a) includes the nodes (1, 1), (2, 2), (3, 2), and (4, 2). The second way,
route (b) includes the nodes (1, 1), (2, 1), (3, 2), and (4, 2). Lastly the third way,
route (c) includes the nodes (1, 1), (2, 1), (3, 1), and (4, 3).
The path probability for route (a) is 0:625  0:318  0:376 ¼ 0:07473, and yields
a
2 ¼ 0:07473=(1:03  1:03  1:03) ¼ 0:06838. The path probability for route (b)
is 0:375  0:671  0:376 ¼ 0:09461, and yields b
2 ¼ 0:09461=(1:03  1:03  1:03) ¼
0:0865824.
Finally the probability for route (c) is 0:375  0:329  0:541 ¼ 0:06674, and
yields c
2 ¼ 0:06674=(1:03  1:03  1:03) ¼ 0:06108. The Arrow-Debreu price, 2, is
therefore:
2 ¼ a
2 þ b
2 þ c
2 ¼ 0:06838 þ 0:0865824 þ 0:06108 ¼ 0:21604
Node (4, 1): There is only one route from node (1, 1) to node (4, 1), and the path
probability is 0:375  0:329  0:459 ¼ 0:05663. This gives an Arrow-Debreu price:
1 ¼
0:05663
1:03  1:03  1:03 ¼ 0:0518
An alternative and simpler method of obtaining the Arrow-Debreu prices for the
nodes in a particular lattice level is to use forward iteration. Here we can use the fact
that the Arrow-Debreu prices for the nodes in a particular level are related, in the
usual binomial fashion, to the values in the previous level and the set of transition
probabilities between levels. Since the Arrow-Debreu price for root node (1, 1) is (by
definition) 1, and we know how to compute the transition probabilities between
levels, all the Arrow-Debreu prices in the (n þ 1)th lattice level can be computed from
those in the nth lattice level.
We will now illustrate this, by showing how to compute the Arrow-Debreu prices
in lattice level 4, i, i ¼ 1, . . . , 4, from the previously computed Arrow-Debreu prices
	
i , i ¼ 1, . . . , 3, in level 3.
4 ¼ p3  	
3
1 þ r ¼ 0:682  0:402
1:03
¼ 0:266
3 ¼
ð1  p3Þ  	
3 þ p2	
2
	

1 þ r
¼ 0:402  0:318 þ 0:425  0:624
f
g
1:03
¼ 0:381
172
Pricing Assets

2 ¼
ð1  p2Þ  	
2 þ p1	
1
	

1 þ r
¼ 0:425  0:376 þ 0:116  0:541
f
g
1:03
¼ 0:216
1 ¼ 1  p1
f
g	
1
1 þ r
¼ 0:459  0:116
1:03
¼ 0:052
As a means of checking the computed Arrow-Debreu prices we can use the fact
that, at any lattice level, the sum of the Arrow-Debreu prices inflated at the riskless
interest rate to the root node is 1. That is for nth lattice level we have:
ð1 þ rÞn1 X
n
i¼1
i ¼ 1
ð10:123Þ
where r is the (constant) riskless interest rate. If we take into account finite computa-
tional precision then Equation 10.123 becomes:
ABS
ð1 þ rÞn1 X
n
i¼1
i
 
!
 1
(
)
 tol
ð10:124Þ
where ABS X
f
g denotes the absolute value of X, and tol is a small number which
reflects the computational accuracy. For nodes on level 4 we have:
ABS ð1:03Þ3ð0:266 þ 0:381 þ 0:216 þ 0:052Þ  1
n
o

 1:5  104
10.5.2
Barle–Cakici implied lattice
Here we briefly describe modifications proposed by Barle and Cakici (1995), hence-
forth denoted BC, to the algorithm used by Derman and Kani for constructing the
implied lattice. These improvements reduce the occurrence of bad transition prob-
abilities and thus lead to better quality lattices.
First modification
The first modification proposed by BC is to use Fi (the forward of si) for the strike
price, K, in Equation 10.109 instead of si. Under these circumstances Equation
10.115 (DK equation 7) becomes:
Siþ1 ¼ Si CðFi; tnþ1Þ expðrtÞ  BC
	

 iFiðFi  SiÞ
CðFi; tnþ1Þ expðrtÞ  BC
	

 iðFi  SiÞ
ð10:125Þ
where
BC ¼
X
n
j¼iþ1
jðFj  FiÞ
Numeric methods and single asset American options
173

Second modification
The second modification is to allow the central spine of the implied lattice to follow
the values dictated by the prevailing interest rate. If the (n þ 1)th lattice level is odd
this involves setting the central node to S exp (r  q)tnþ1, where q is the continuous
dividend yield, and the other symbols have already been defined in the previous
section on the DK lattice. If the (n þ 1)th lattice level is even then the two central
nodes now no longer satisfy Equation 10.116 but
SiSiþ1 ¼ F2
i
ð10:126Þ
where i ¼ (n þ 1)=2.
The asset price at the lower central node Si is then given by:
Si ¼ FiðiFi  BCÞ
iFi þ BC
ð10:127Þ
whereas that at the upper central node Siþ1 is:
Siþ1 ¼ FiðBC þ iFiÞ
iFi  BC
ð10:128Þ
where BC ¼ C(Fi, tnþ1) exp (rt)  BC.
Proof of Equation 10.127 (BC equation 9) and Equation 10.128
From Equation 10.114 we have that the transition probability, pi is:
pi ¼ Fi  Si
Siþ1  Si
multiplying above and below by Siþ1 then gives:
pi ¼ ðFi  SiÞSiþ1
ðSiþ1  SiÞSiþ1
However since we are centering at the forward price, from Equation 10.126, we
have SiSiþ1 ¼ F2
i , and so
pi ¼ FiSiþ1  F2
i
S2
iþ1  F2
i
¼
FiSiþ1  F2
i
ðSiþ1  FiÞðSiþ1 þ FiÞ
ð10:129Þ
However from Equation 10.118 we have
BC ¼ ipiðSiþ1  FiÞ
ð10:130Þ
If we substitute the value of pi from Equation 10.129 into Equation 10.130 we have
BC ¼ ipiðSiþ1  FiÞ ¼ iðFiSiþ1  F2
i ÞðSiþ1  FiÞ
ðSiþ1  FiÞðSiþ1 þ FiÞ
¼ iðFiSiþ1  F2
i Þ
Siþ1 þ Fi
174
Pricing Assets

Rearranging we obtain:
BCSiþ1 þ BCFi ¼ iFiSiþ1  iF2
i
Siþ1ðBC  iFiÞ ¼ FiðBC þ iFiÞ
which gives
Siþ1 ¼ FiðBC þ iFiÞ
iFi  BC
QED
To prove Equation 10.127 we simply substitute Siþ1Si ¼ F2
i into Equation 10.128
and obtain:
Si ¼ F2
i
Siþ1
¼ F2
i ðiFi  BCÞ
FiðBC þ iFiÞ
So
Si ¼ FiðFi  BCÞ
iFi þ BC
QED
Bad probabilities
If bad transition probabilities occur then this can rectified by setting Siþ1 to any value
between Fi and Fiþ1. In these circumstances Barle and Cakici suggest setting Siþ1 to
the average of Fi and Fiþ1.
10.5.3
Chriss implied lattice
Here we will briefly mention an implied lattice, devised by Chriss (1996), which can
be built using the market values of both European and American options. This is in
contrast to the algorithm of Derman–Kani which requires the market values of
European options. We will not describe how to deal with American options; the
reader can refer to the original paper which is available on the CD ROM. The first
part of the paper, is concerned with European options and follows on from
our previous discussions concerning the Derman–Kani and Barle–Cakici implied
lattices.
As supplementary information we will now show how to derive equation (3) in the
original paper, that is:
u ¼

PUT þ K
K expðrtÞ  
PUT
ð10:131Þ
the notation used here is the same as that in Chriss (1996).
Numeric methods and single asset American options
175

Proof of Equation 10.131 (Chriss equation 3)
The transition probability of an up jump from Si1, j to Si, jþ1 is denoted by pj, and
that of the corresponding down jump transition probability 1  pj by q. The forward
for Si1, j is denoted by Fj and, since Si1, j ¼ K, we have:
Fj ¼ Si1; j expðrtÞ ¼ K expðrtÞ
ð10:132Þ
The up jump transition probability, see Equation 10.114, is
pj ¼
Fj  Si; j
Si; jþ1  Si; j
which results in a down jump probability of
1  pj ¼ q ¼ 1 
Fj  Si; j
Si; jþ1  Si; j
¼ Si; jþ1  Fj
Si; jþ1  Si; j
Multiplying top and bottom by Si, j we obtain
q ¼ Si; jþ1  Fj
Si; jþ1  Si; j
¼ ðSi; jþ1  FjÞSi; j
ðSi; jþ1  Si; jÞSi; j
¼ Si; jþ1Si; j  FjSi; j
Si; jþ1Si; j  S2
i; j
We choose to centre at the spot Si, jþ1Si, j ¼ K2 and we have
q ¼ Si; jþ1Si; j  FjSi; j
K2  S2
i; j
¼
Si; jþ1Si; j  FjSi; j
ðK  Si; jÞðK þ Si; jÞ ¼
K2  FjSi; j
ðK  Si; jÞðK þ Si; jÞ
ð10:133Þ
From the derivation of equation (1), on the first page of the original paper by
Chriss, we have:

PUT
i1; j ¼ qðK  Si; jÞ expðrtÞ
ð10:134Þ
We now use Equation 10.133 to substitute for q in Equation 10.134. This gives

PUT
i1; j ¼ qðK  Si; jÞ expðrtÞ ¼ expðrtÞðK2  FjSi; jÞ
K þ Si; j
using Fj ¼ K exp (rt) from Equation 10.132 results in

PUT
i1; j ¼ KðK expðrtÞ  Si; jÞ
K þ Si; j
ð10:135Þ
and multiplying both sides of Equation 10.135 by K þ Si, j we obtain

PUT
i1; jK þ 
PUT
i1; jSi; j ¼ K2 expðrtÞ  KSi; j
ð10:136Þ
Since we centre at the spot we have:
Si; jSi; jþ1 ¼ K2
176
Pricing Assets

so
Si; jþ1 ¼ Ku ¼ K2
Si; j
,
which gives:
u ¼ K
Si; j
ð10:137Þ
Finally, from Equation 10.136, we have
K2 expðrTÞ  K
PUT
i1; j ¼

PUT
i1; j þ K


Si; j
so
1
Si; j
¼

PUT
i1; j þ K
K2 expðrtÞ  K
PUT
i1; j
This results in
K
Si; j
¼ u ¼

PUT
i1; j þ K


K
K2 expðrtÞ  K
PUT
i1; j
or
u ¼

PUT
i1; j þ K
K expðrtÞ  
PUT
i1; j
QED
More information concerning the Chriss implied lattice, and other types of implied
lattices, can be found in Chriss (1997).
10.6
GRID METHODS FOR VANILLA OPTIONS
10.6.1
Introduction
In Section 10.4 we discussed the use of binomial lattice methods for valuing both
European and American options. The lattice methods we described have the advan-
tage that they are fairly easy to implement and can value simple options, such as
vanilla puts and calls, reasonably accurately. The use of up and down jump prob-
abilities at the lattice nodes is also an appealing feature, since they are directly related
to the stochastic process which is being modelled. However, lattice techniques have
the following drawbacks:
. They require small time steps to ensure numerical stability.
. There is little control over where the lattice nodes are located. This can lead to very
poor accuracy when valuing certain types of options; for example those with
barriers at particular asset prices.
Numeric methods and single asset American options
177

One method of avoiding these limitations is through the use of finite-difference
grids. Although this approach no longer has the probabilistic interpretation of the
binomial lattice it has the following advantages:
. Fewer time steps are required to ensure numerical stability, see Appendix L for a
discussion of stability.
. There is complete control over the placement of grid lines, and their associated grid
nodes.
10.6.2
Uniform grids
The Black–Scholes equation for the value of an option, f is given by:
@f
@t þ ðr  qÞS @f
@S þ 1
2 2S2 @2f
@S2 ¼ rf
ð10:138Þ
We want to solve this equation over the duration of the option, that is from the
current time t to the maturity of the option at time t þ . To do this we will use a grid
in
which
the
asset
price
S
takes
ns
uniformly
spaced
values,
Sj ¼ jS,
j ¼ 0, . . . , ns1, where S is the spacing between grid points. If Smax is the maximum
asset value we want to represent then the grid spacing, S	, can be simply calculated as:
S	 ¼
Smax
ðns  1Þ
ð10:139Þ
However, since we would like to solve the option values and Greeks at the current
asset price S0 we would also like an asset grid line to coincide with the current asset
price, see Andersen and Brotherton-Ratcliffe (1998). This avoids the use of inter-
polation which is necessary when the asset value does not correspond to a grid line.
The method by which we achieve this is outlined in Code excerpt 10.12. Here the user
supplies the function opt_gfd with values for Smax and ns  1 from which S	 is
computed using Equation 10.139. We then find the integer, n1, that is just below (or
equal to) the value So=S	, and use this to obtain a new grid spacing S ¼ So=n1.
This leads to the new asset price discretization Sj ¼ jS j ¼ 0, . . . , ns1, where we
have now ensured that Sn1¼ So.
The user also supplies the function opt_gfd with the number of time intervals for
the grid. When there are nt time intervals the grid has nt þ 1 uniformly spaced time
instants, ti ¼ it, i ¼ 0, . . . , nt, and the time step is simply:
t ¼ 
nt
ð10:140Þ
As with the binomial lattice methods of Sections 10.4 and 10.5 we will solve the
equation backwards in time from maturity (at time t þ ) to the present (time t). So
as we solve the equation the time index will start at i ¼ nt (time t þ ) and decrease to
i ¼ 0 (current time t).
Here we discuss the grid method of solving the Black–Scholes equation in terms of:
. The finite-difference approximation.
. The boundary conditions.
178
Pricing Assets

. Computation of the option values at a given time instant.
. Backwards iteration and early exercise.
Each of these aspects will now be considered in turn.
The finite-difference approximation
The option value corresponding to the grid node at which ti ¼ it and Sj ¼ jS
will be denoted by fi, j. We will approximate the partial derivative of fi, j w.r.t. time
simply as:
@f
@t ¼ fiþ1; j  fi; j
t
ð10:141Þ
For the other terms in Equation 10.138 we will use the weighted, m, method. This
technique involves selecting an appropriate choice for m in the range 0  m  1 so
that the contribution from node (i, j) is a weighted sum involving the values at nodes
(i, j) and (i þ 1, j). For instance the term rf ji, j in Equation 10.138 is approximated as:
rf ji; j ¼ r mfiþ1; j þ ð1  mÞfi; j
	

ð10:142Þ
and the term @f =@Sji, j in Equation 10.138 is approximated as:
@f
@S

i; j
¼
m @f
@S

iþ1; j
þ ð1  mÞ @f
@S

i; j
(
)
ð10:143Þ
Using this method we thus obtain, at node (i, j), the following discretized version
of Equation 10.138:
fiþ1; j  fi; j
t
þ ðr  qÞSj m f 0
iþ1; j þ 	
m f 0
i; j
n
o
þ 1
2 2S2
j
m f 00
iþ1; j þ 	
m f 00
i; j
n
o
¼ r m fiþ1; j þ 	
m fi; j
	

ð10:144Þ
where for compactness we have written 	
m ¼ 1  m, and denote the partial deri-
vatives w.r.t. S at node (i, j) as: f 0
i, j ¼ @f =@Sji, j and f 00
i, j ¼ @2f =@S2i, j.
Finite-difference approximations for these derivatives can be obtained by con-
sidering a Taylor expansion about the point fi,j. We proceed as follows:
fi; jþ1 ¼ fi; j þ f 0
i; jS þ 1
2 f 00
i; j S
ð
Þ2
ð10:145Þ
fi; j1 ¼ fi; j  f 0
i; jS þ 1
2 f 00
i; j S
ð
Þ2
ð10:146Þ
Subtracting Equations 10.145 and 10.146 we obtain:
fi; jþ1  fi; j1 ¼ 2f 0
i; jS
and so
f 0
i; j ¼ fi; jþ1  fi; j1
2S
ð10:147Þ
Numeric methods and single asset American options
179

Adding Equations 10.145 and 10.146 we obtain:
fi; jþ1 þ fi; j1 ¼ 2fi; j þ f 00
i; jS2
which gives:
f 00
i; j ¼ fi; jþ1  2fi; j þ fi; j1
S2
ð10:148Þ
The complete finite-difference approximation to the Black–Scholes equation can
then be found by substituting the approximations for the first and second partial
derivatives, given in Equations 10.147 and 10.148, into Equation 10.144. We thus
obtain:
rt m fiþ1; j þ 	
m fi; j
	

¼ fiþ1; j  fi; j þ ðr  qÞjtA1
2
þ 2j2tA2
2
ð10:149Þ
where we have used the fact that Sj ¼ jS, and for compactness have defined the
terms:
A1 ¼ m fiþ1; j þ1  m fiþ1; j1 þ 	
m fi; jþ1  	
m fi; j1
and
A2 ¼ m fiþ1; jþ1 þ m fiþ1; j1  2m fiþ1; j þ 	
m fi; jþ1 þ 	
m fi; j1  2	
m fi; j
Collecting like terms in fi, j, fiþ1, j, etc. results in:
B1 fi; j1 þ B2 fi; j þ B3 fi; jþ1 þ C1 fiþ1; j1 þ C2 fiþ1; j þ C3 fiþ1; jþ1 ¼ 0
ð10:150Þ
where
B1 ¼ 	
mðr  qÞjt
2
þ 	
m2j2t
2
B2 ¼1  rt	
m  	
m2j2t
B3 ¼ 	
mðr  qÞjt
2
þ 	
m2j2t
2
C1 ¼ m2j2t
2
 mðr  qÞjt
2
C2 ¼ 1  rtm  m2j2t
C3 ¼ mðr  qÞjt
2
þ m2j2t
2
Since we are solving the equation backwards in time we want to determine the
option values at time index i from the known option values ( fiþ1, jþ1, fiþ1, j and
180
Pricing Assets

fiþ1, j1) at time index i þ 1. This can be achieved by rearranging Equation 10.150
as follows:
Finite-difference scheme for a uniform grid
aj fi; j1 þ bj fi; j þ cj fi; jþ1 ¼ Riþ1; j
ð10:151Þ
where the right hand side, Riþ1, j, is:
Riþ1; j ¼ aj fiþ1; j1 þ bj fiþ1; j þ cj fiþ1; jþ1
ð10:152Þ
The six coefficients are:
aj ¼ ð1  mÞ t
2
ðr  qÞj  2j2
	

ð10:153Þ
bj ¼ 1 þ ð1  mÞt r þ 2j2
	

ð10:154Þ
cj ¼ ð1  mÞ t
2
ðr  qÞj þ 2j2
	

ð10:155Þ
aj ¼ m t
2
ðr  qÞj  2j2
	

ð10:156Þ
bj ¼ 1  mt r þ 2j2
	

ð10:157Þ
cj ¼ m t
2
ðr  qÞj þ 2j2
	

ð10:158Þ
For each value of j Equation 10.151 gives us a relationship between three option
values, fiþ1, j1, fiþ1, j, fiþ1, jþ1 at time index i þ 1, and three option values fi, j1, fi, j,
fi, jþ1 at time index i.
This situation is shown in Figure 10.9 where we have labelled the grid nodes that
contribute to the option value f5,5 at grid node E. These are the known option values
node A: f6,6, node B: f6,5 and node C: f6,4 and the unknown option values, node D:
f5,6, node E: f5,5 and node F: f5,4.
Before we solve Equation 10.151 we will briefly consider its characteristics for
different values of the weight parameter m.
When m ¼ 1 the values of the coefficients in Equation 10.151 are aj ¼ cj ¼ 0 and
bj ¼ 1. This means that Equation 10.151 reduces to:
fi; j ¼ aj fiþ1; j1 þ bj fiþ1; j þ cj fiþ1; jþ1
This is termed the explicit method, and it can be seen that the unknown option
value fi, j, at the grid node (i, j) is just a weighted sum of the (known) option values
fiþ1, j1, fiþ1, j, fiþ1, jþ1. This is the simplest situation to deal with and actu-
ally corresponds to a trinomial lattice. However, it has poor numerical proper-
ties and usually requires a very small step size to obtain accurate results, see
Smith (1985).
When m 6¼ 1, the unknown option value fi, j depends not only on the known
option values fiþ1, j1, fiþ1, j, fiþ1, jþ1 (as in the explicit method above), but also on the
Numeric methods and single asset American options
181

neighbouring unknown option values fi, j1 and fi, jþ1. It is now necessary to solve a set
of simultaneous in order to compute the value fi, j. This is therefore called an implicit
method, see Smith (1985).
The implicit method m ¼ 0 is also called the fully implicit method, since now the
unknown value fi, j only depends on the neighbouring values fi, j1, fi, jþ1 and its
previous value, fiþ1, j, at time step i þ 1. This can be shown by substituting m ¼ 0
in Equations 10.153 to 10.158. We then obtain aj ¼ cj ¼ 0 and bj ¼ 1, which means
that Equation 10.151 reduces to:
aj fi; j1 þ bj fi; j þ cj fi; jþ1 ¼ fiþ1; j
The implicit method m ¼ 0:5, is also termed the Crank–Nicolson method. This
method, first used by Crank and Nicolson in 1946, see Crank and Nicolson (1947),
computes fi, j by giving equal weight to the contributions from time step i þ 1 and
Time (in units of ∆t )
0
0
2
4
6
8
10
10
15
20
25
30
35
40
45
50
12
14
18
16
20
5
A
B
C
F
E
D
0,f10,10
0,f10,9
0,f10,8
0,f10,7
0,f10,6
0,f10,5
5,f10,4
10,f10,3
15,f10,2
20,f10,1
25,f10,0
Asset price
Figure 10.9
An example uniform grid, which could be used to estimate the value of a vanilla option which
matures in two years time. The grid parameters are: ns ¼ nt ¼ 10, t ¼ 0:2, S ¼ 5, and Smax ¼ 50. The
option parameters are E ¼ 25, So ¼ 20, and  ¼ 2:0. As usual we denote the grid node option values by fi, j,
where i is the time index and j is the asset index. The option values of the grid nodes at maturity for a vanilla
put are thus labelled as val, f10, j, j ¼ 0, . . . ,10, where val is the value of the option at the node; these are shown
on the right hand grid boundary. Since E ¼ 25 only those nodes with j < 5 have nonzero option values
182
Pricing Assets

time step i. Substituting m ¼ 0:5 in Equations 10.153 to 10.149 we obtain the
following Crank–Nicolson coefficients:
aj ¼ aj ¼ t
4
ðr  qÞj  2j2
	

bj ¼ 1 þ t
2
r þ 2j2
	

bj ¼ 1  t
2
r þ 2j2
	

cj ¼ cj ¼  t
4
ðr  qÞj þ 2j2
	

We notice that since we are solving backwards in time, but index time in the forward
direction, our values of m corresponding to implicit and explicit are different from
those normally used. For example in Smith (1985) m ¼ 0 is the explicit method and
m ¼ 1 is the implicit method; the Crank–Nicolson method is still m ¼ 0:5.
The boundary conditions
In order to solve Equation 10.151 at time instant it we need to obtain the option
values at the upper asset boundary, the lower asset boundary and the initial values
that are specified at option maturity.
Here we calculate the boundary values by using the time independent payoff, pj, at
the jth asset index within the grid. If E is the strike price then vanilla call options have
payoffs
pj ¼ maxð jS  E; 0Þ; j ¼ 0; . . . ; ns1
and vanilla put options have payoffs
pj ¼ maxðE  jS; 0Þ; j ¼ 0; . . . ; ns1
Upper asset boundary values.
At the upper boundary j ¼ ns  1, and (ns  1)S ¼
Smax; where we note that for the grid to be useful we require Smax > E. Here we
assume that Smax > E and so for call options
pns1 ¼ Smax  E
and for put options
pns1 ¼ 0
The option value at the upper boundary, denoted by fBU, is set to pns1, and we have
fi, ns1 ¼ fBU, i ¼ 0, . . . , nt.
Lower asset boundary values.
At the lower boundary j ¼ 0, and the value of jS
is zero. So for call options
p0 ¼ 0
Numeric methods and single asset American options
183

and for put options
p0 ¼ E
The option value at the lower boundary, denoted by fBL, is set to p0, and we have
fi, 0 ¼ fBL, i ¼ 0, . . . , nt.
Boundary values at option maturity.
At option maturity (i ¼ nt) the initial option
(boundary) values are the previously mentioned payouts. If E is the strike price then
for vanilla call options
fnt; j ¼ maxð jS  E; 0Þ;
j ¼ 0; . . . ; ns1
and for vanilla put options
fnt; j ¼ maxðE  jS; 0Þ;
j ¼ 0; . . . ; ns1
This is illustrated in Figure 10.9 for a vanilla put option with current asset value
S0 ¼ 20, strike, E ¼ 25 and maturity  ¼ 2. The grid asset price spacing is S ¼ 5,
and the time increment is t ¼ 0:2. At option maturity, corresponding to time index
i ¼ 10, the value of the put option is zero for all asset indices j  5.
Computation of the option values at a given time instant
Having found the option boundary values we are now in a position to solve Equation
10.151 at time instant ti ¼ it.
First we note that since fi,0 ¼ fBL and fi,ns1 ¼ fBU, Equation 10.151 only needs to
be solved for values of the asset index j in the range j ¼ 1 to j ¼ ns2. We now deal
with the following situations:
. CASE 1: j ¼ 1, the asset grid line just above the lower boundary.
. CASE 2: j ¼ ns2, the asset grid line just below the upper boundary.
. CASE 3: all other asset grid lines not included in CASE 1 or CASE 2.
and consider the form that Equation 10.151 takes under each condition.
CASE 1: j ¼ 1
Substituting j ¼ 1, into Equation 10.151 we obtain:
a1 fi;0 þ b1 fi;1 þ c1 fi;2 ¼ a1 fiþ1;0 þ b1 fiþ1;1 þ c1 fiþ1;2
Now, since fi,0 ¼ fBL, this becomes:
b1 fi;1 þ c1 fi;2 ¼ ða1  a1ÞfBL þ b1 fiþ1;1 þ c1 fiþ1;2
or equivalently:
b1 fi;1 þ c1 fi;2 ¼ Riþ1;1
ð10:159Þ
where
Riþ1;1 ¼ ða1  a1Þ fBL þ b1 fiþ1;1 þ c1 fiþ1;2
ð10:160Þ
184
Pricing Assets

CASE 2: j ¼ ns2
Substituting j ¼ ns1 into Equation 10.151 we obtain:
ans2 fi;ns3 þ bns2 fi;ns2 þ cns2 fi;ns1 ¼ ans2 fiþ1;ns3 þ bns2 fiþ1;ns2 þ cns2 fiþ1;ns1
Since fi, ns1 ¼ fBU this gives:
ans2 fi;ns3 þ bns2 fi;ns2 ¼ ans2 fiþ1;ns3 þ bns2 fiþ1;ns2 þ ðcns2  cns2Þ fBU
or equivalently:
ans2 fi;ns3 þ bns2 fi;ns2 ¼ Riþ1;ns2
ð10:161Þ
where
Riþ1;ns2 ¼ ans2 fiþ1;ns3 þ bns2 fiþ1;ns2 þ ðcns2  cns2Þ fBU
ð10:162Þ
CASE 3
In this case the boundary values do not enter into the expressions, and we simply
restate Equation 10.151 as:
aj fi; j1 þ bj fi; j þ cj fi; jþ1 ¼ Riþ1; j;
j ¼ 3; . . . ; ns3
ð10:163Þ
where as before the right hand side, Riþ1, j, is:
Riþ1; j ¼ aj fiþ1; j1 þ bj fiþ1; j þ cj fiþ1; jþ1
ð10:164Þ
We can now gather all the information in Equations 10.159 to 10.164 and represent
it by the following tridiagonal system:
b1
c1
0
0
0
0
a2
b2
c2
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
ans3
bns3
cns3
0
0
0
0
ans2
bns2
0
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
A
fi;1
fi;2
:
:
fi;ns3
fi;ns2
0
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
A
¼
Riþ1;1
Riþ1;2
:
:
Riþ1;ns3
Riþ1;ns2
0
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
A
ð10:165Þ
In matrix notation Equation 10.165 can be written as:
Ax ¼ R
ð10:166Þ
where A is the ns2  ns2 tridiagonal matrix containing the known coefficients
aj, j ¼ 2, . . . , ns2, bj, j ¼ 1, . . . , ns2, and cj, j ¼ 1, . . . , ns3. The vector R denotes
the known right hand side, Riþ1, j, j ¼ 1, . . . , ns2, and the vector x contains the
unknown option values that we wish to compute, fi, j, j ¼ 1, . . . , ns2.
It is well known that, if matrix A is non-singular, Equation 10.166 can be solved
using an LU decomposition. Here we factorize the n  n matrix A as:
A ¼ LU
Numeric methods and single asset American options
185

where L is an n  n lower triangular matrix with 1s on the diagonal and U is an n  n
upper triangular matrix. We illustrate the LU decomposition for a full 4  4 matrix below:
a1;1
a1;2
a1;3
a1;4
a2;1
a2;2
a2;3
a2;4
a3;1
a3;2
a3;3
a3;4
a4;1
a4;2
a4;3
a4;4
0
B
B
@
1
C
C
A ¼
1
0
0
0
l2;1
1
0
0
l3;1
l3;2
1
0
l4;1
l4;2
l4;3
1
0
B
B
@
1
C
C
A
u1;1
u1;2
u1;3
u1;4
0
u2;2
u2;3
u2;4
0
0
u3;3
u3;4
0
0
0
u4;4
0
B
B
@
1
C
C
A
ð10:167Þ
If A is a tridiagonal matrix then the LU decomposition takes the simpler form:
a1;1
a1;2
0
0
a2;1
a2;2
a2;3
0
0
a3;2
a3;3
a3;4
0
0
a4;3
a4;4
0
B
B
@
1
C
C
A ¼
1
0
0
0
l2;1
1
0
0
0
l3;2
1
0
0
0
l4;3
1
0
B
B
@
1
C
C
A
u1;1
u1;2
0
0
0
u2;2
u2;3
0
0
0
u3;3
u3;4
0
0
0
u4;4
0
B
B
@
1
C
C
A
ð10:168Þ
where it can be seen that now both L and U are bidiagonal.
Once the LU decomposition of A has been found it is possible to solve for x in
Equation 10.166 by using a two stage method (see for example Golub and Van Loan
(1989)). Here forward elimination is used to solve Ly ¼ R, and then back-substitu-
tion is applied to Ux ¼ y. We can thus write the procedure as:
Ax ¼ ðLUÞx ¼ LðUxÞ ¼ Ly ¼ R
We will now provide code excerpts which show how to solve the ns2  ns2 tridia-
gonal system represented by Equation 10.166. These excerpts are in fact contained
within the larger Code excerpt 10.18, which displays the complete C code for the option
pricing function opt_gfd. If the reader requires more detail concerning the precise
code used for option pricing then this code should be consulted. (It should be noted that
in Code excerpt 10.18, time is indexed using j and asset price using index i. We have
modified the indices for the smaller code excerpts given below so that, as might be
expected, time is indexed using i, and asset price using j. The author apologizes for any
inconvenience this may cause.) Here, for brevity, we will assume that all the required
arrays have already been allocated and loaded with the relevant information.
First we need to compute the LU decomposition of the tridiagonal matrix A. The
code to achieve this is given in Code excerpt 10.14 below. Here we use the following
three arrays to store the elements of the tridiagonal matrix A: array b contains the
diagonal elements, array c contains the upper diagonal elements, and array a holds
the lower diagonal elements.
Code excerpt 10.14
Computer code which calculates the diagonal elements of the matrix U, in an LU
decomposition of a tridiagonal matrix, A. The elements of matrix A are stored in the following arrays:
array b contains the diagonal elements, array c contains the upper diagonal elements, and array a holds the
lower diagonal elements. The diagonal elements of U are stored in the array u for later use, in Code
excerpts 10.15 and 10.16
u[1] ¼ b[1];
if (u[1] ¼¼ 0.0) printf (‘‘ERROR in array u \n’’);
for(j¼ 2; j <¼ns 2; þþj) {
u[j] ¼ b[j]  a[j]*c[j 1]/u[j 1];
if (u[j] ¼¼ 0.0) printf (‘‘ERROR in array u \n’’);
}
186
Pricing Assets

It should be noted we do not explicitly compute the elements of the matrix L.
This is because all the diagonal elements of L are known to be 1, and the sub-
diagonal elements of L can be computed from the diagonal elements of U by using
l[j]¼ a[j]/u[j1]. Also we do not need to compute the upper diagonal
elements of U since they are known to be the same as the upper diagonal ele-
ments of the original matrix A, and are contained in the array c, see for example
Hager (1988).
Having computed the LU decomposition we can now solve the lower triangular
system Ly ¼ R using forward elimination, this is shown in Code excerpt 10.15.
Code excerpt 10.15
Computer code which uses forward elimination to solve the lower triangular system
Ly ¼ R, where y is stored in the array work
In Code excerpt 10.15 we make use of the following two arrays: the array rhs which
is used to store the elements of the right hand side R, and the array work which is
both used as workspace and to store the computed solution vector y. As previously
mentioned the sub-diagonal elements of L are given by l[j] = a[j]/u[j1]. This
means that in Code excerpt 10.15, the line:
is in fact be equivalent to:
where l[j], j ¼ 2,.., ns2 contains the sub-diagonal elements of L, if we had
(needlessly) decided to allocate space for an extra array called l.
We are now in a position to solve the triangular system Ux ¼ y by using back-
substitution. The code to achieve this is given in Code excerpt 10.16. Here the array
work contains the previously computed values of y, the diagonal elements of U are
contained in the array u, and (as previously mentioned) the upper diagonal elements
of U are stored in the array a.
Code excerpt 10.16
Computer code which uses back-substitution to solve the upper triangular system
Ux ¼ y. At time instant ti ¼ it, the elements of x are the calculated option values fi, j, i ¼ 1, . . . , ns2
In Code excerpt 10.16 the array opt_vals contains the solution vector x. As its
name suggests the contents of the array opt_vals are in fact the computed option
values, fi, j, j ¼ 1, . . . , ns2, in Equation 10.6.2 and represent the solution of the
work[1] ¼ rhs[1];
for(j¼ 2; j<¼ns 2; þþj) {
work[j] ¼ rhs[j]  a[j]*work[j1]/u[j1];
}
work[j] = rhs[j]  a[j]* work[j1]/u[j1];
work[j] = rhs[j]l[j]* work[j1];
opt_vals[ns2] ¼ work[ns2]/u[ns2];
for(j ¼ ns2; j >¼ 1; j)
opt_vals[j] ¼ (work[j]  c[j]opt_vals[jþ 1])/u[j];
Numeric methods and single asset American options
187

Black–Scholes partial differential equation at time instant ti ¼ it; based on the
previously computed option values fiþ1, j, j ¼ 1, . . . , ns2.
Backwards iteration and early exercise
The Black–Scholes equation can be solved over the time interval t to t þ  by
iteratively solving Equation 10.6.2. We iterate backwards in time by solving Equa-
tion 10.6.2 at the ith time step and then using the computed values to solve Equation
10.6.2 for the (i  1)th time step. The option values at current time t are obtained
when time index i ¼ 0 is reached. It can be seen that the grid method yields ns2
option values, f0, j, j ¼ 1, . . . , ns2, which correspond to the current asset prices
Sj
0 ¼ jS;
j ¼ 1; . . . ; ns2
As previously mentioned the asset price S0 coincides with grid index j ¼ n1. There-
fore S0 ¼ Sn1
0 , and the option value for the current asset price S0 is given by f0, n1.
This is in contrast to the lattice methods discussed in Section 10.4 which yield a
single option value corresponding to the root node.
The option values obtained using the grid methods we have just described are for
vanilla European options. However, vanilla European options can be more accu-
rately valued by using the Black–Scholes option pricing formula discussed in Section
9.3.3. The importance of finite-difference grids is that, by slightly modifying our
backward iterative method, we can take into account the possibility of early exercise,
and thus price American options.
This can be achieved by using Code excerpt 10.17 to modify the option prices
contained in the array opt_vals as follows:
Code excerpt 10.17
Computer code which modifies the computed option values contained in array
opt_vals to include the possibility of early exercise; this is required if we are to determine the value of
American options. Here s[ j] contains the asset value at asset index j, opt_vals[j] contains the option
value (computed by Code excerpt 10.16) at asset index j, and E is the strike price
Now we know how to solve the Black–Scholes equation; it is possible to include,
without much difficulty, more exotic features such as lock out periods, barriers,
rebates, etc.
The routine opt_gfd solves the Black–Scholes equation using a uniform grid.
The asset price is set to one of the grid lines, which means that interpolation is not
required.
void opt_gfd(double theta_m, double asset_price, double sigma, double r, double T, double strike,
Integer is_american, Integer put, double *option_value, double greeks[], double q, Integer pns,
Integer nt, double smax, Integer *iflag)
if (put) { /* a put */
for(j¼1; j<¼ns2; þþj)
opt_vals[j] ¼ MAX(opt_vals[j], Es[j]);
}
else { /* a call */
for(j¼ 1; j<¼ns2; þþj)
opt_vals[j] ¼ MAX(opt_vals[j], s[j]E);
}
188
Pricing Assets

{
/* Input parameters:
theta_m
— the value of theta used for the finite difference method,
asset_price
— the current price of the underlying asset,
sigma
— the volatility,
r
— the interest rate,
T
— the time to maturity,
strike
— the strike price,
is_american
— if is_american is 0 then a European option, otherwise an American option,
put
— if put is 0 then a call option, otherwise a put option,
q
— the continuous dividend yield,
pns
— the maximum asset index on the grid, corresponding to the upper boundary,
nt
— the number of time intervals,
smax
— the maximum asset price.
Output parameters:
option_value
— the value of the option,
greeks[]
— the hedge statistics output as follows: greeks[0] is gamma, greeks[1] is delta, and
greeks[2] is theta,
iflag
— an error indicator.
*/
double *a, *b, *c, *a1, *b1, *c1, *opt_vals, *vals, *rhs, *s, *work, *u;
double ds, dt;
Integer i, j;
double tmp, t2, time_2mat;
Integer n1, n2, ind¼0;
double sig2, temp[4];
if (asset_price >¼ smax) printf (‘‘ERROR asset price >¼smax’’);
n1 ¼ floor((asset_price/smax)*(double)pns);
n2 ¼ pns  n1;
ds ¼ asset_price/(double)n1;
dt ¼ T/(double)nt; /* time interval size */
ns ¼ n1þn2 þ 1;
/* Note: Now nps ¼ ns1. Since we define asset grid lines 0 . . . ns1, this is the maximum grid line;
corresponding to the upper boundary. The lower boundary is at the asset grid line 0, and we solve for
option values between the asset grid line 1 and the asset grid line ns 2 */
/* Allocate (all size nsþ 1) the arrays: a, b, c, a1, b1, c1, opt_vals, vals, rhs, s, work and u */



s[0] ¼ 0.0;
s[n1] ¼ asset_price;
for(i¼ 1; i<¼n1 1; þþi ) /* set prices below asset_price */
s[i] ¼ (double)i * ds;
for(i¼ 1; i<¼ n2þ 1; þþi ) /* set prices above asset_price */
s[n1þi] ¼ asset_price þ (double)i * ds;
/* Set up the RHS and LHS coefficients a[], b[] and c[] are the LHS coefficients for the unknown option
values (time step j) a1[], b1[] and c1[] are the values of the RHS coefficients for the known option
prices (time step jþ1).
Note: a1, b1 and c1 are used to form the RHS vector rhs[] of the tridiagonal system. */
sig2 ¼ sigma*sigma;
t2 ¼ dt/2.0;
tmp ¼ 1.0theta_m; /* 1  theta (for theta method) */
for( i ¼ 1; i<¼ns 2; þþi) {/* Assign elements of the (ns 2) *(ns 2) tridiagonal matrix */
a[i] ¼ i*(i*sig2(rq))*t2*tmp;
a1[i] ¼ i*(i*sig2(rq))*t2*theta_m;;
c[i] ¼ i*(i*sig2þ(rq))*t2*tmp;
c1[i] ¼ i*(i*sig2þ(rq))*t2*theta_m;;
b[i] ¼ 1.0þr*dt*tmpþ(i*i*sig2)*dt*tmp;
b1[i]¼ 1.0(i*i*sig2þr)*dt*theta_m;
}
/* Perform LU decomposition of the tridiagonal matrix with:
diagonal elements contained in the array b[], upper diagonal elements contained in the array c[]
and lower diagonal elements in the array a[]. Store the elements of U but not those of L
(they will be computed from U)
Matrix U: The diagonal elements of U are stored in the array u[] and the upper diagonal elements of U
are just c[].
Matrix L: For the lower triangular matrix L, the diagonal elements are 1 and the lower diagonal elements
are l[i] ¼ a[i]/u[i 1], where u[] is the upper diagonal of U. */
u[1] ¼ b[1];
if (u[1] ¼¼ 0.0) printf (‘‘ERROR in array u \n’’);
for(i¼ 2; i <¼ns 2; þþi){
u[i] ¼ b[i]  a[i]*c[i 1]/u[i 1];
if (u[i] ¼¼ 0.0) printf (‘‘ERROR in array u \n’’);
}
Numeric methods and single asset American options
189

/* Set option values at maturity. Note : opt_vals[0] and opt_vals [ns 1] are the lower and upper
(put/call) option price boundary values. */
if (!put){/* a call */
for( i ¼ 0; i<ns; þþi )
opt_vals[i] ¼ MAX(s[i]  strike, 0.0 );
}
else {/* a put */
for( i ¼ 0; i<ns; þþi)
opt_vals[i] ¼ MAX(strike  s[i], 0.0);
}
/* From the option values at maturity (t ¼ nt*dt) calculate values at earlier times (nt 1)*dt etc.. */
for( j¼nt 1; j>¼ 2; --j) {/* Go two steps past current time (0) so that can evaluate theta */
time_2mat ¼ Tj*dt;
for(i¼ 2; i<¼ns 3; þþi) /* set up the rhs of equation for Crank—Nicolson method */
rhs[i] ¼ a1[i]*opt_vals[i 1] þ b1[i]*opt_vals[i] þ c1[i] *opt_vals[iþ 1];
/* Incorporate the boundary conditions at the upper/lower asset value boundaries */
rhs[1] ¼ (a1[1]  a[1])*opt_vals[0]þ b1[1]*opt_vals[1]þ c1[1]*opt_vals[2];
rhs[ns 2]¼a1[ns 2]*opt_vals[ns 3]þb1[ns 2]*opt_vals[ns 2]þ(c1[ns 2] c[ns 2])*opt_vals[ns 1];
/* Solve the lower triangular system Ly ¼ b, where y is stored in array work[].
Compute the elements of L from those of U, l[i] ¼ a[i]/u [i 1]. */
work[1] ¼ rhs[1];
for( i¼ 2; i<¼ns 2; þþi ) {
work[i] ¼ rhs[i]  a[i]*work[i 1]/u[i 1];
}
/* Solve the upper (ns 2)*(ns 2) triangular system Ux ¼ y (where x ¼ opt_vals) */
opt_vals[ns 2] ¼ work[ns 2]/u[ns 2];
for( i ¼ ns 2; i >¼ 1; --i )
opt_vals[i] ¼ (work[i]  c[i]*opt_vals[iþ 1])/u[i];
if (is_american) {/* take into account early exercise for american options */
if (put) {/* a put */
for(i¼ 1; i<¼ns 2; þþi)
opt_vals[i] ¼ MAX(opt_vals[i], strike  s[i]);
}
else {/* a call */
for(i¼ 1; i<¼ns 2; þþi)
opt_vals[i] ¼ MAX(opt_vals[i], s[i]  strike);
}
}
if (j¼¼ 0) {
for (i¼ 0; i < ns; þþi)
vals[i] ¼ opt_vals[i];
}
if ((j¼¼ 1)jj(j¼¼ 2)jj(j¼¼ 1)jj(j¼¼ 2)) {/* Store option values so that can compute theta */
temp[ind] ¼ opt_vals[n1];
þþind;
}
}
if (greeks) {
/* Compute gamma (4th order accuracy) */
greeks[0] ¼ (vals[n1 þ 2]þ 16.0 *vals[n1 þ 1] 30.0*vals[n1]þ
16.0*vals[n1 1]vals[n1  2])/(12.0* ds*ds);
/* Compute delta (4th order accuracy) */
greeks[1] ¼ (vals[n1þ 2]þ 8.0*vals[n1 þ 1] 8.0*vals [n1  1]þ vals[n1  2])/(12.0*ds);
/* Compute theta (4th order accuracy) */
greeks[2] ¼ (temp[0]þ 8.0*temp[1] 8.0*temp[2]þtemp [3])/(12.0*dt);
/* Note: could also compute theta as greeks[2] ¼ (temp[0]þ 4.0* temp[1] 3.0*vals[n1])/
(2.0*dt); */
}
*option_value ¼ vals[n1]; /* Return option value */
}
Code excerpt 10.18
Function to compute the value of a vanilla option using a uniform grid
10.6.3
Nonuniform grids
In the previous section we showed how to solve the Black–Scholes equation using a
uniform grid. Although this approach will provide satisfactory solutions to many
option pricing problems, there are situations in which it is important to be able to
place grid lines at locations which do not correspond to those available in a uniform
190
Pricing Assets

grid. Increasing the density of grid lines in regions of interest can lead to improved
accuracy in both the estimated option values and also the estimates of the hedge
statistics (the Greeks).
Here we provide an example which illustrates the benefits of using nonuniform
grids in the evaluation of down and out call barrier options. Later on in Section
10.6.6 we give a further example which shows the use of nonuniform grids to evaluate
double barrier options.
The purpose of this section is to show how to discretize the Black–Scholes equation
using a nonuniform grid, and to derive an expression, see Equation 10.176, that is
equivalent to Equation 10.151. Although the tridiagonal system of equations we have
to solve in this section will be different from that in Section 10.6.2, the solution
method is exactly the same. This means that once we have derived Equation 10.151
all the other information which we require to evaluate both European and American
options is available in Section 10.6.2 under the headings:
. The boundary conditions.
. Computation of the option values at a given time instant.
. Backwards iteration and early exercise.
We will now consider the finite-difference approximation for a nonuniform grid, and
then show how to value the down and out call barrier option.
The finite-difference approximation
Here we consider how to discretize the Black–Scholes equation using a nonuniform
grid, in which both the asset price interval S and the time step t are not constant
but can vary throughout the grid.
Allowing for a nonconstant time step is quite simple. The time step occurs in both
the first derivative of fi, j, see Equation 10.141, and in the finite-difference equations,
see Equations 10.153 to 10.157, as the constant t. To incorporate a varying time
step, ti, i ¼ 0, nt, thus only requires setting t ¼ ti, at the ith time step and then
continue with the solution method outlined in Section 10.6.2.
The incorporation of nonconstant asset price intervals requires more work. This is
because the finite-difference approximations to the first and second derivatives f 0
i, j
and f 00
i, j, in Equations 10.147 and 10.148, are based on a Taylor expansion about the
point fi, j.
We will now derive expressions for these derivatives. If we let X
j ¼ Sj  Sj1
and Xþ
j ¼ Sjþ1  Sj and then using a Taylor expansion about the fiþ1, j we have
fiþ1; jþ1 ¼ fiþ1; j þ f 0
iþ1; jXþ
j þ 1
2 f 00
iþ1; j Xþ
j

2
ð10:169Þ
and also
fiþ1; j1 ¼ fiþ1; j  f 0
iþ1; jX
j þ 1
2 f 00
iþ1; j X
j

2
ð10:170Þ
Numeric methods and single asset American options
191

Multiplying Equation 10.169 by X
j
and adding it to Xþ
j
times, Equation
10.170 gives
Xþ
j fiþ1; j1 þ X
j fiþ1; jþ1 ¼ X
j fiþ1; j þ Xþ
j fiþ1; j
þ 1
2 f 00
iþ1; j ðXþ
j Þ2X
j þ ðX
j Þ2Xþ
j
n
o
Therefore
1
2 f 00
iþ1; j ¼
Xþ
j fiþ1; j1 þ X
j fiþ1; jþ1  X
j fiþ1; j  Xþ
j fiþ1; j
ðXþ
j Þ2X
j þ ðX
j Þ2Xþ
j
So
f 00
iþ1; j ¼
2 Xþ
j fiþ1; j1 þ X
j fiþ1; jþ1  fiþ1; jðX
j þ Xþ
j Þ
n
o
ðXþ
j Þ2X
j þ ðX
j Þ2Xþ
j
ð10:171Þ
To calculate f 0
iþ1, j we rearrange Equation 10.170 to obtain
f 0
iþ1; jX
j ¼ fiþ1; j1  fiþ1; j  1
2 f 00
iþ1; jðX
j Þ2
and
f 0
iþ1; j ¼ fiþ1; j  fiþ1; j1
X
j
þ 1
2 f 00
iþ1; jX
j
ð10:172Þ
If we now substitute for f 00
iþ1, j, from Equation 10.171, into Equation 10.172 we have
f 0
iþ1; j ¼ fiþ1; j  fiþ1; j1
X
j
þ
Xþ
j fiþ1; j1  ðX
j þ Xþ
j Þfiþ1; j þ X
j fiþ1; jþ1
n
o
X
j
ðXþ
j Þ2X
j þ ðX
j Þ2Xþ
j
which simplifies to give
f 0
iþ1; j ¼
ðXþ
j Þ2ð fiþ1; j  fiþ1; j1Þ  ðX
j Þ2fiþ1; j þ ðX
j Þ2fiþ1; jþ1
ðXþ
j Þ2X
j þ ðX
j Þ2Xþ
j
so that we finally have
f 0
iþ1; j ¼
ðX
j Þ2fiþ1; jþ1 þ ððXþ
j Þ2  ðX
j Þ2Þfiþ1; j  ðXþ
j Þ2fiþ1; j1
ðXþ
j Þ2X
j þ ðX
j Þ2Xþ
j
ð10:173Þ
192
Pricing Assets

As in Section 10.6.2, we can now substitute the expressions for f 0
iþ1, j and f 00
iþ1, j given
in Equations 10.173 and 10.171, into the Equation 10.144; the discretized Black–
Scholes equation. If we let D ¼ (Xþ
j )2X
j þ (X
j )2Xþ
j we then obtain
rtðm fiþ1; j þ 	
m fi; jÞ ¼ fiþ1; j  fi; j þ ðr  qÞSjtA1
D
þ
2S2
j tA2
D
ð10:174Þ
where 	
m ¼ 1  m, and
A1 ¼ m fiþ1; jþ1ðX
j Þ2  fiþ1; j1ðXþ
j Þ2  fiþ1; j
	
ðX
j Þ2  ðXþ
j Þ2
h
i
þ 	
m fi; jþ1ðX
j Þ2  fi; j1ðXþ
j Þ2  fi; j
	
ðX
j Þ2  ðXþ
j Þ2
h
i
and
A2 ¼ m fiþ1; jþ1X
j þ fiþ1; j1Xþ
j  fiþ1; j
	
X
j þ Xþ
j

h
i
þ 	
m fi; jþ1X
j þ fi; j1Xþ
j  fi; j
	
X
j þ Xþ
j

h
i
Collecting like terms we obtain:
B1 fi; j1 þ B2 fi; j þ B3 fi; jþ1 þ C1 fiþ1; j1 þ C2 fiþ1; j þ C3 fiþ1; jþ1 ¼ 0
ð10:175Þ
where
B1 ¼ 	
mðr  qÞSjtðXþ
j Þ2
D
þ
ð1  Þ2S2
j tXþ
j
D
B2 ¼  1  rt	
m 
	
m2S2
j tðX
j þ Xþ
j Þ
D

	
mðr  qÞSjt
	
ðX
j Þ2  ðXþ
j Þ2
D
B3 ¼
	
mðr  qÞSjtðX
j Þ2
D
þ
	
m2S2
j tX
j
D
C1 ¼
m2S2
j tXþ
j
D
 mðr  qÞSjtðXþ
j Þ2
D
C2 ¼1  rtm 
mðr  qÞSjt
	
ðX
j Þ2  ðXþ
j Þ2
D

m2S2
j t X
j þ Xþ
j
n
o
D
C3 ¼
mðr  qÞSjtðX
j Þ2
D
þ
m2S2
j tX
j
D
Since we are solving the Black–Scholes equation backwards in time we will
rearrange Equation 10.175 as:
Finite-difference scheme for a nonuniform grid
aj fi; j1 þ bj fi; j þ cj ¼ Riþ1; j
ð10:176Þ
where the right hand side Riþ1, j is:
Riþ1; j ¼ aj fiþ1; j1 þ bj fiþ1; j þ cj fiþ1; jþ1
ð10:177Þ
Numeric methods and single asset American options
193

and the coefficients are
aj ¼ 	
mt ðr  qÞSjðXþ
j Þ2
D

2S2
j Xþ
j
D
(
)
ð10:178Þ
bj ¼1þt	
m
rþ
2S2
j ðX
j þXþ
j Þ
D
(
þ
ðrqÞSj ðX
j Þ2 ðXþ
j Þ2
n
o
D
9
=
;
ð10:179Þ
cj ¼ 	
mt
ðr  qÞSjðX
j Þ2
D

2S2
j X
j
D
(
)
ð10:180Þ
aj ¼ mt
2S2
j Xþ
j
D
 ðr  qÞSjðXþ
j Þ2
D
(
)
ð10:181Þ
bj ¼ 1  mrt
mt
ðr  qÞSj ðX
j Þ2  ðXþ
j Þ2
n
o
D
þ
2S2
j
X
j þ Xþ
j
n
o
D
8
<
:
9
=
;
ð10:182Þ
cj ¼ mt
ðr  qÞSjðX
j Þ2
D
þ
2S2
j X
j
D
(
)
ð10:183Þ
Here Equation 10.176, as is the case for Equation 10.151 in Section 10.6.2, pro-
vides the relationship between the three option values fiþ1, j1, fiþ1, j, fiþ1, jþ1 at time
index i þ 1, and the three option values fi, j1, fi, j, fi, jþ1 at time index i. It can also
be seen that Equation 10.176 is the nonuniform grid equivalent of Equation 10.151
given in Section 10.6.2. We will now show that Equations 10.176 and 10.151
are identical when a uniform grid is used, that is Xþ
j ¼ X
j . We proceed as
follows:
Let
Xþ
j ¼ X
j ¼ S,
and
Sj ¼ jS
so
D ¼ ðXþ
j Þ2X
j þ ðX
j Þ2Xþ
j ¼ 2ðSÞ3
ðXþ
j Þ2
D
¼
ðX
j Þ2
D
¼ ðSÞ2
2ðSÞ3 ¼
1
2S
194
Pricing Assets

Xþ
j
D
¼
X
j
D
¼
1
2S2
ðXþ
j Þ2  ðX
j Þ2
D
¼ 0
If we substitute the above values into Equations 10.178 to 10.183 we obtain the
following expressions for the coefficients in Equation 10.176.
aj ¼ ð1  mÞt ðr  qÞSj
2S

2S2
j
2S2
(
)
¼ ð1  mÞ t
2
ðr  qÞj  2j2
	

bj ¼ 1 þ tð1  mÞ
r þ
2S2
j
S2
(
)
¼ 1 þ ð1  mÞt r þ 2j2
	

cj ¼ ð1  mÞt ðr  qÞSj
2S

2S2
j
2S2
(
)
¼ ð1  mÞ t
2
ðr  qÞj þ 2j2
	

aj ¼ mt
2S2
j
2S2  ðr  qÞSj
2S
(
)
¼ m t
2
ðr  qÞj  2j2
	

bj ¼ 1  mrt 
m2S2
j t
S2
¼ 1  mt r þ 2j2
	

cj ¼ mt ðr  qÞSj
2S
þ
2S2
j
S2
(
)
¼ m t
2
ðr  qÞj þ 2j2
	

It can be seen that these coefficients are identical to those given in Section 10.6.2,
Equations 10.153 to 10.158.
We now provide examples of using nonuniform grids to evaluate European down
and out call options.
Valuation of a down and out call option
Here the improved accuracy that can be achieved by using nonuniform grids instead
of uniform grids is illustrated in Figures 10.11 and 10.12. The uniform grids are
constructed using the method outlined in Section 10.6.2 and Code excerpt 10.18.
That is an asset grid line is set to coincide with the current asset price S0, and the
other grid lines are positioned above and below S0 with a uniform spacing of S.
The disadvantage of this approach is that there will be an unspecified pricing error
that depends on the distance, ds, of the barrier level, B, to the the nearest asset grid
line. Futhermore, as the number of asset points, ns, increases the magnitude of ds will
oscillate within the range 0 to S=2.
When ds 
 0 the grid will be accurate, but when jdsj 
 S=2 there will be a large
pricing error. This gives rise to the oscillating pricing errors shown in Figures 10.11
and 10.12.
Numeric methods and single asset American options
195

The nonuniform grids are constructed using the techniques mentioned earlier in
this section, and also Code excerpt 10.19. We now, irrespective of ns, arrange for one
asset grid line to coincide with the current asset value, S0, and another asset grid line
to coincide with B, the barrier asset price. In Figure 10.10 this corresponds to setting
BL to B and not using BU.
It can be seen in Figures 10.11 and 10.12 that in this case the pricing error is very
much less, and also doesn’t exhibit the pronounced oscillations that are produced by
a uniform grid. In Code excerpt 10.19 below, we give the computer program which was
used to obtain the nonuniform grid values for the down and out call options presented
in Figures 10.11 and 10.12. Although this program only deals with European options it
can easily be altered, using the same techniques as in Code excerpt 10.18, to deal with
American style options; this is left as an exercise for the reader.
void barrier_downout(double barrier_level, double theta_m, double asset_price, double sigma, double r,
double T, double strike, Integer put, double *option_value, double greeks[], double q, Integer ns,
Integer nt, double smax, Integer *ifail)
{
/* ns  the number of asset intervals
nt  the number of time intervals
*/
double *a, *b, *c, *a1, *b1, *c1, *opt_vals, *vals, *rhs, *s, *work, *u;
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
BL
Bu
Time (in units of ∆t )
Asset price
50
45
40
35
30
25
20
15
10
5
0
Figure 10.10
A nonuniform grid in which the grid spacing is reduced near current time t, and also in the
neighbourhood of the asset price 25; this can lead to greater accuracy in the computed option values and
the associated Greeks. Grid lines are also placed at asset prices of BU and BL, this enables the accurate
evaluation of options which have barriers at these asset prices
196
Pricing Assets

double ds, time_step;
Integer i, j, barrier_index;
double tmp, t2, time_2mat, zero ¼ 0.0;
Integer n1, n2, ind¼0, ns1;
double sig2, temp[4], ds_plus, ds_minus, temp1, temp2, temp3;
double D;
n1 ¼ floor((asset_price/smax)*(double)ns);
if (n1 < 3){
printf (‘‘increase the number of asset points \n’’);
}
n2 ¼ ns  n1;
ds ¼ asset_price/(double)n1;
time_step ¼ T/(double)nt; /* time interval size */
ns1 ¼ n1þn2þ2; /* number of nodes  including extra grid line*/
/* allocate the required arrays (all of size ns1þ1): a, b, c, a1, b1, c1, opt_vals, vals, rhs, s, work, u */



/* set prices below asset_price */
s[0] ¼ zero;
s[n1] ¼ asset_price;
for(i¼1; i < n1; þþi )
s[i] ¼ (double)i * ds;
/* set prices above asset_price */
for(i¼1; i<¼ n2þ2; þþi ){
s[n1þi] ¼ asset_price þ (double)i * ds;
}
/* find out the index corresponding to barrier_level */
barrier_index ¼ 0;
while(barrier_level > s[barrier_index]){
þþbarrier_index;
}
Absolute error in estimated value
Number of asset points, ns
Uniform grid
Nonuniform grid (error × 5)
1.8
1.6
1.4
1.2
0.6
0.8
0.4
0.2
0
1
50
100
150
200
Figure 10.11
The absolute error in the estimated values for a European down and out call barrier option
(B < E) as the number of asset grid points, ns, is varied. Here we show a comparison of the results obtained
using both uniform and nonuniform grids; logarithmic transformations were not employed. The algorithm
for the uniform grid is described in Section 10.6.2, and that for the nonuniform grid is outlined in Section
10.6.3. The Crank–Nicolson method (m ¼ 0:5) was used and the other parameters were E ¼ 50:0, B ¼ 47:5,
S0 ¼ 55:0, Smax ¼ 300:0, T ¼ 0:5,  ¼ 0:2, r ¼ logð1:1Þ, q ¼ 0:0, nt ¼ 100. The correct option value
was 7.6512 which was obtained using the analytic formulae given in Section 9.4 and Code excerpt 9.6
Numeric methods and single asset American options
197

if (barrier_level !¼ s[barrier_index]){/* decrement barrier index */
barrier_index;
}
if (s[barrier_index] !¼ barrier_level){/* then barrier does not correspond to an existing grid line so
create another one*/
for (i¼1; i < ns1barrier_index; þþi){
s[barrier_indexþ1þi] ¼ s[barrier_index] þ (double)i*d s;
}
þþbarrier_index;
s[barrier_index] ¼ barrier_level;
if (n1>barrier_index){
þþn1;
}
}
/* set up the RHS and LHS coefficients a[], b[] and c[] are the LHS coefficients for the unknown option
values (time step j) a1[], b1[] and c1[] are the values of the RHS coefficients for the known option
prices (time step jþ1).
Note: a1, b1 and c1 are used to form the RHS vector rhs[] of the tridiagonal system. */
sig2 ¼ sigma*sigma;
t2 ¼ time_step/2.0;
tmp ¼ 1.0theta_m; /* 1  theta (for theta method) */
/* assign elements of the (ns12)*(ns12) tridiagonal matrix */
for( i¼1; i<¼ns12; þþi){
ds_plus ¼ s[iþ1]s[i];
ds_minus ¼ s[i]  s[i1];
D ¼ ((ds_plus*ds_plus*ds_minus) þ (ds_minus*ds_minus*ds_ plus));
temp1 ¼ tmp*time_step/D;
Absolute error in estimated value
Number of asset points, ns
Uniform grid
Nonuniform grid (error × 5)
50
100
150
200
3.5
3
2.5
2
1.5
1
0.5
0
Figure 10.12
The absolute error in the estimated values for a European down and out call barrier option
(E < B) as the number of asset grid points, ns, is varied. Here we show a comparison of the results obtained
using both uniform and nonuniform grids; logarithmic transformations are not employed. The algorithm
for the uniform grid is described in Section 10.6.2 and that for the nonuniform grid is outlined in Section
10.6.3. The Crank–Nicolson method (m ¼ 0:5) was used and the other parameters were E ¼ 50.0, B ¼ 52.5,
S0 ¼ 65.0, Smax ¼ 300.0, T ¼ 0.5,  ¼ 0.2, r ¼ log (1.1), q ¼ 0.0, nt ¼ 100. The correct option value was
17.0386 which was obtained using the analytic formulae given in Section 9.4 and Code excerpt 9.6
198
Pricing Assets

a1[i] ¼ (temp1*((rq)*s[i]*ds_plus*ds_plus)  temp1* ds_plus*(s[i]*s[i]*sig2));
temp1 ¼ (ds_minus*ds_minus)/D;
temp2 ¼ ds_minus/D;
c[i] ¼ time_step*tmp*(temp1*s[i]*(rq)þ(sig2*s[i]* s[i]*temp2));
c1[i] ¼ time_step*theta_m*(temp1*s[i]*(rq)þ(sig2*s[i] *s[i]*temp2));
temp1 ¼ ((ds_minus*ds_minus)  (ds_plus*ds_plus))/D;
temp2 ¼ (ds_minusþds_plus)/D;
b[i] ¼ 1.0þtime_step *tmp*(rþ((rq)*s[i]*temp1)þ (s[i]* s[i]*sig2)*temp2);
b1[i] ¼ 1.0time_step *theta_m*(rþ((rq)*s[i]*temp1)þ (s[i]*s[i]*sig2)*temp2);
}
/* Perform LU decomposition of the tridiagonal matrix with: diagonal elements contained in the array b[],
upper diagonal elements contained in the array c[] and lower diagonal elements in the array a[].
Store the elements of U but not those of L (they will be computed from U)
Matrix U: The diagonal elements of U are stored in the array u[] and the upper diagonal elements of U are
just c[].
Matrix L: For the lower triangular matrix L, the diagonal elements are 1 and the lower diagonal elements
are l[i] ¼ a[i]/u[i1], where u[] is the upper diagonal of U. */
u[1] ¼ b[1];
if (u[1] ¼¼ zero) printf (‘‘error in array u \n’’);
for( i¼2; i <¼ns12; þþi){
u[i] ¼ b[i]  a[i]*c[i1]/u[i1];
if (u[i] ¼¼ zero) printf (‘‘error in array u \n’’);
}
/* Set option values at maturity. Note : opt_vals[0] amd opt_vals[ns11] are the lower and upper (put/call)
option price boundary values. */
if (!put){/* a call */
for( i¼0; i<ns1; þþi )
opt_vals[i] ¼ MAX(s[i]strike, zero );
/* now modify option values to include the barrier */
for( i¼0; i <¼ barrier_index; þþi )
opt_vals[i] ¼ zero;
}
else{/* a put */
for( i¼0; i<ns1; þþi)
opt_vals[i] ¼ MAX(strike  s[i], zero);
}
/* From the option values at maturity, t ¼ nt*time_step, compute
the values at times (nt1)*time_step to 0 (current time) */
for( j¼nt1; j>¼2; j){/* go two steps past current time so that can evaluate theta */
time_2mat ¼ Tj*time_step;
/* set up the rhs of equation for the Theta method */
for(i¼2; i<¼ns13; þþi)
rhs[i] ¼ a1[i]*opt_vals[i 1]þb1[i]*opt_vals[i]þc1[i]* opt_vals[iþ1];
/* incorporate the boundary conditions1 at the upper/lower asset value boundaries */
rhs[1] ¼ (a1[1]a[1])*opt_vals[0]þ b1[1]*opt_vals[1]þc1[1]*opt_vals[2];
rhs[ns12] ¼ a1[ns12]*opt_vals[ns13]þ b1[ns12]*opt_vals[ns12]þ
(c1[ns12]c[ns12])*opt_vals[ns11];
/* Solve the lower triangular system Ly ¼ b, where y is stored in array work[].
Compute the elements of L from those of U, l[i] ¼ a[i]/u[i1]. */
work[1] ¼ rhs[1];
for( i¼2; i<¼ns12; þþi ){
work[i] ¼ rhs[i]  a[i]*work[i1]/u[i1];
}
/* Solve the upper (ns12)*(ns12) triangular system Ux ¼ y (where x ¼ opt_vals) */
opt_vals[ns12] ¼ work[ns12]/u[ns12];
for( i ¼ ns12; i >¼ 1; i )
opt_vals[i] ¼ (work[i]  c[i]*opt_vals[iþ1])/u[i];
if (j¼¼0){
for (i¼0; i < ns1; þþi)
vals[i] ¼ opt_vals[i];
}
/* store option values so that can compute theta */
if ((j¼¼1)||(j¼¼2)||(j¼¼1)||(j¼¼2)){
temp[ind] ¼ opt_vals[n1];
þþind;
}
/* now modify for barrier */
for( i¼0; i <¼ barrier_index; þþi )
opt_vals[i] ¼ zero;
}
if (greeks){/* assume an irregular grid */
ds_minus ¼ s[n1]s[n11];
ds_plus ¼ s[n1þ1]s[n1];
D ¼ (ds_minus*ds_minus*ds_plus)þ (ds_plus*ds_plus*ds_minus);
temp1 ¼ ds_minus*ds_minus;
Numeric methods and single asset American options
199

temp2 ¼ ds_plus*ds_plus;
temp3 ¼ temp1temp2;
/* GAMMA */
greeks[0] ¼ (ds_minus*vals[n1þ1] þ ds_plus*vals[n11]  vals [n1]*(ds_plusþds_minus))/(0.5*D);
/* DELTA */
greeks[1] ¼ (temp1*vals[n1þ1]  temp2*vals[n11]  vals [n1]*temp3)/D;
/* THETA */
greeks[2] ¼ (temp[0]þ8.0*temp[1] 8.0*temp[2]þtemp[3])/(12.0*time_step);
/* could also compute theta like this:
greeks[2] ¼ (temp[0]þ4.0*temp[1]3.0*vals[n1])/(2.0* time_step); */
}
*option_value ¼ vals[n1]; /* Return option value */
/* deallocate the arrays that were previously allocated */



}
Code excerpt 10.19
Function to compute the value of a European down and out barrier option using
a nonuniform grid
10.6.4
The log transformation and uniform grids
Up to this point we have been dealing with the standard Black–Scholes equation,
which is
@f
@t þ ðr  qÞS @f
@S þ 2S2
2
@2f
@S2 ¼ rf
ð10:184Þ
However, if we introduce the change of variable Z ¼ log S, we obtain the following
equation:
@f
@t þ b @f
@Z þ 2
2
@2f
@Z2 ¼ rf
ð10:185Þ
where b ¼ r  q  (2=2). This has beneficial numerical properties since it does not
contain the original Black–Scholes terms in S and S2.
Derivation of Equation 10.185
We will now derive an expression for the logarithmic Black–Scholes equation, and
show that it agrees with Equation 10.185.
Since Z ¼ log S we have @Z=@S ¼ 1=S. This gives:
@f
@S ¼ @f
@Z
@Z
@S ¼ 1
S
@f
@Z
and
@2f
@S2 ¼ @
@S
@f
@S


¼ 1
S2
@f
@Z þ 1
S
@
@S
@f
@Z


¼  1
S2
@f
@Z þ 1
S
@Z
@S
@
@Z
@f
@Z


@2f
@S2 ¼  1
S2
@f
@Z þ 1
S2
@2f
@Z2
Substituting the above values into Equation 10.184
@f
@t þ ðr  qÞS
S
@f
@Z  2S2
2S2
@f
@Z þ 2S2
2S2
@2f
@Z2 ¼ rf
200
Pricing Assets

and setting b ¼ r  q  2=2 we obtain:
@f
@t þ b @f
@Z þ 2
2
@2f
@Z2 ¼ rf
QED
(10:186)
We will now consider the finite-difference discretization of Equation 10.185.
The finite-difference method
Application of the finite difference method to the log transformed Black–Scholes
equation is very similar to that already outlined in Sections 10.6.2 and 10.6.3.
Use of the m method on Equation 10.185 results in:
fiþ1; j  fi; j
t
þ b m f 0
iþ1; j þ 	
m f 0
i; j
n
o
þ 1
2 2 m f 00
iþ1; j þ 	
m f 00
i; j
n
o
¼ r m fiþ1; j þ 	
m fi; j
	

where 	
m ¼ 1  m. Applying a uniform discretization at node (i, j) we obtain:
fiþ1; j  fi; j þ btA1
2Z þ 2tA2
2Z2 ¼ rt m fiþ1; j þ 	
m fi; j
	

ð10:187Þ
where
A1 ¼ m fiþ1; jþ1  fiþ1; j1
	

þ 	
m fi; jþ1  fi; j1
	

A2 ¼ m fiþ1; jþ1  2fiþ1; j þ fiþ1; j1
	

þ 	
m fi; jþ1  2fi; j þ fi; j1
	

Collecting like terms obtain:
B1 fi; j1 þ B2 fi; j þ B3 fi; jþ1 þ C1 fiþ1; j1 þ C2 fiþ1; j þ C3 fiþ1; jþ1 ¼ 0
where
B1 ¼ 	
mbt
2Z
þ 	
m2t
2Z2
B2 ¼  1  rt	
m  	
m2t
Z2
B3 ¼ 	
mbt
2Z þ 	
m2t
2Z2
C1 ¼ m2t
2Z2  mbt
2Z
C2 ¼1  rtm  m2t
Z2
C3 ¼ mbt
2Z þ m2t
2Z2
Numeric methods and single asset American options
201

If we rearrange we have the following equation:
Finite-difference scheme for a uniform grid and log transformation
aj fi; j1 þ bj fi; j þ cj ¼ aj fiþ1; j1 þ bj fiþ1; j þ cj fiþ1; jþ1
ð10:188Þ
where:
aj ¼ ð1  mÞt
2Z2
bZ  2
	

ð10:189Þ
bj ¼ 1 þ ð1  mÞt r þ 2
Z2


ð10:190Þ
cj ¼  ð1  mÞt
2Z2
bZ þ 2
	

ð10:191Þ
aj ¼  mt
2Z2
bZ  2
	

ð10:192Þ
bj ¼ 1  mt r þ 2
Z2


ð10:193Þ
cj ¼ mt
2Z2
bZ þ 2
	

ð10:194Þ
It can be seen that, unlike in Section 10.6.2, the coefficients in Equations 10.188 to
10.194 are independent of the asset price index j.
When m ¼ 0:5 (the Crank–Nicolson method) we have the following coefficients:
aj ¼ aj ¼
t
4Z2 bZ  2
	

bj ¼ 1 þ t
2
r þ 2
Z2


cj ¼ cj ¼ 
t
4Z2 bZ þ 2
	

bj ¼ 1  t
2
r þ 2
Z2


The method of using the finite-difference grid to compute option prices is identical
to that already outlined in Section 10.6.2, which solves the standard (nonlogarithmic)
Black–Scholes equation. Table 10.7 compares the results obtained with and without
a logarithmic transformation. It is shown in Appendix L.2 that the implicit method,
m ¼ 0, is unconditionally stable.
10.6.5
The log transformation and nonuniform grids
In the previous section we considered the use of a uniform grid to discretize the
logarithmically transformed Black–Scholes equation.
@f
@t þ b @f
@Z þ 2
2
@2f
@Z2 ¼ rf
ð10:195Þ
202
Pricing Assets

where
b ¼ r  q  2
2
and
Z ¼ log S
Here we will generalize these results and use a nonuniform grid to solve Equation
10.195.
Our description will be very brief since most of the details have already been discussed
in previous sections. Here we are only concerned with the finite-difference approxima-
tion and derive the equations that need to be solved at each time step. Later, in Section
10.6.6, we will apply our results to solving a European double knockout barrier option.
The finite-difference approximation
At the grid node (i, j) we have
Z
j ¼ Zj  Zj1
and
Zþ
j ¼ Zj þ 1  Zj
Following Section 10.6.3 the first and second derivatives of f w.r.t. Z are
f 00
iþ1; j ¼
2 Zþ
j fiþ1; j1 þ Z
j fiþ1; jþ1  Z
j fiþ1; j  Zþ
j fiþ1; j
n
o
ðZþ
j Þ2Z
j þ ðZ
j Þ2Zþ
j
Table 10.7
Valuation results and pricing errors for a vanilla American put option using a uniform grid with
and without a logarithmic transformation; the implicit method and Crank–Nicolson method are used. The
accurate values (obtained using a logarithmic transformed grid with m ¼ 0:0, ns ¼ 1000 and nt ¼ 1000) are
presented in the column labelled ‘Value’. The absolute pricing errors (ABS) (accurate value estimated value)
are presented in the column labelled BS were obtained using a standard uniform grid (as outlined in
Section 10.6.2), and those in the column labelled Log BS use a uniform grid and logarithmic transformation
as explained in this section. The maturity of the option was varied from 0.1 to 1.5 years, the other parameters
were: S ¼ 9:0, X ¼ 9:7, r ¼ 0:1, q ¼ 0:0,  ¼ 0:30, Smax ¼ 100:0, ns ¼ 50, and nt ¼ 50
m ¼ 0:0
m ¼ 0:5
Time
Value
BS
Log BS
BS
Log BS
0.1
0.7598
1:5142  102
7:7803  103
1:5077  102
7:6165  103
0.2
0.8334
4:6192  102
1:2924  102
4:5935  102
1:1892  102
0.3
0.8920
6:4526  102
1:4125  102
6:3969  102
1:2426  102
0.4
0.9401
7:4973  102
1:6559  102
7:4030  102
1:4483  102
0.5
0.9810
8:0546  102
1:8471  102
7:9155  102
1:5842  102
0.6
1.0164
8:3022  102
1:9125  102
8:1141  102
1:5845  102
0.7
1.0477
8:3496  102
1:8959  102
8:1098  102
1:5029  102
0.8
1.0755
8:2672  102
1:8408  102
7:9743  102
1:3894  102
0.9
1.1006
8:1012  102
1:7756  102
7:7547  102
1:2736  102
1.0
1.1234
7:8827  102
1:7138  102
7:4829  102
1:1695  102
1.1
1.1442
7:6332  102
1:6643  102
7:1807  102
1:0855  102
1.2
1.1633
7:3671  102
1:6290  102
6:8631  102
1:0217  102
1.3
1.1810
7:0946  102
1:6092  102
6:5404  102
9:7921  103
1.4
1.1973
6:8227  102
1:6042  102
6:2196  102
9:5649  103
1.5
1.2126
6:5559  102
1:6128  102
5:90565  102
9:5098  103
Numeric methods and single asset American options
203

and
f 0
iþ1; j ¼
ðZ
j Þ2fiþ1; jþ1 þ ððZþÞ2  ðZ
j Þ2Þfiþ1; j  ðZþ
j Þ2fiþ1; j1
ðZþ
j Þ2Z
j þ ðZ
j Þ2Zþ
Then discretizing Equation 10.195 in the usual manner we obtain
fiþ1; j  fi; j
t
þ b m f 0
iþ1; j þ 	
m f 0
i; j
n
o
þ 2
2
m f 00
iþ1; j þ 	
m f 00
i; j
n
o
¼ r m fiþ1; j þ 	
m fi; j
	

where 	
m ¼ 1  m. Letting D ¼ (Zþ
j )2Z
j þ (Z
j )2Zþ
j we obtain
rtðm fiþ1; j þ 	
m fi; jÞ ¼ fiþ1; j  fi; j þ btA1
D
þ 2tA2
D
ð10:196Þ
where
A1 ¼ m fiþ1; jþ1ðZ
j Þ2  fiþ1; j1ðZþ
j Þ2  fiþ1; j
	
ðZ
j Þ2  ðZþ
j Þ2
h
i
þ 	
m fi; jþ1ðZ
j Þ2  fi; j1ðZþ
j Þ2  fi; j
	
ðZ
j Þ2  ðZþ
j Þ2
h
i
A2 ¼ m fiþ1; jþ1Z
j þ fiþ1; j1Zþ
j  fiþ1; j
	
Z
j þ Zþ
j

h
i
þ 	
m fi; jþ1Z
j þ fi; j1Zþ
j  fi; j
	
Z
j þ Zþ
j

h
i
Collecting like terms obtain:
B1 fi; j1 þ B2 fi; j þ B3 fi; jþ1 þ C1 fiþ1; j1 þ C2 fiþ1; j þ C3 fiþ1; jþ1 ¼ 0
where
B1 ¼ 	
mbtðZþ
j Þ2
D
þ 	
m2tZþ
j
D
B2 ¼ 1  rt	
m 
	
m2tðZ
j þ Zþ
j Þ
D

	
mbt ðZ
j Þ2  ðZþ
j Þ2
n
o
D
B3 ¼
	
mbtðZ
j Þ2
D
þ 	
m2tZ
D
C1 ¼ m2tZþ
j
D
 mbtðZþ
j Þ2
D
C2 ¼ 1  rtm 
mbt ðZ
j Þ2  ðZþ
j Þ2
n
o
D

m2t Z
j þ Zþ
j
n
o
D
C3 ¼
mbtðZ
j Þ2
D
þ
m2tZ
j
D
204
Pricing Assets

If we rearrange we have the following equation:
Finite-difference scheme for a nonuniform grid and log transformation
aj fi; j1 þ bj fi; j þ cj ¼ aj fiþ1; j1 þ bj fiþ1; j þ cj fiþ1; jþ1
ð10:197Þ
where:
aj ¼ ð1  mÞt
bðZþ
j Þ2
D
 2Zþ
j
D
(
)
ð10:198Þ
bj ¼ 1 þ tð1  mÞ
r 
2ðZ
j þ Zþ
j Þ
D
(

b ðZ
j Þ2  ðZþ
j Þ2
n
o
D
9
=
;
ð10:199Þ
cj ¼ ð1  mÞt
bðZ
j Þ2
D

2Z
j
D
(
)
ð10:200Þ
aj ¼ mt
2Zþ
j
D
 bðZþ
j Þ2
D
(
)
ð10:201Þ
bj ¼ 1  mrt  mt
b ðZ
j Þ2  ðZþ
j Þ2
n
o
D
8
<
:
þ
2 Z
j þ Zþ
j
n
o
D
9
=
;
ð10:202Þ
cj ¼ mt
bðZ
j Þ2
D
þ
2Z
j
D
(
)
ð10:203Þ
The incorporation of boundary conditions and the solution of Equation 10.197 is
similar in manner to that already discussed in Section 10.6.2. If further details are
required Code excerpt 10.19, which uses a nonuniform grid to solve the log trans-
formed Black–Scholes equation, can be consulted.
When a uniform grid is used Zþ
j ¼ Z
j ¼ Z and therefore
D ¼ ðZþ
j Þ2Z
j þ ðZ
j Þ2Zþ
j ¼ 2ðZÞ3
Numeric methods and single asset American options
205

ðZþ
j Þ2
D
¼
ðZ
j Þ2
D
¼ ðZÞ2
2ðZÞ3 ¼
1
2Z
Zþ
j
D
¼
Z
j
D
¼
1
2Z2
and
ðZþ
j Þ2  ðZ
j Þ2
D
¼ 0
In these circumstances
aj ¼ ð1  mÞt
2Z2
bZ  2
	

bj ¼ 1 þ tð1  mÞ r  2
Z2


cj ¼ ð1  mÞt
b
2Z 
2
2Z2


aj ¼  mt
2Z2
bZ  2
	

bj ¼ 1  mt r þ 2
Z2


cj ¼ mt
2Z2
bZ þ 2
	

which are the same as Equations 10.188 to 10.194 in Section 10.6.4.
10.6.6
The double knockout call option
The purpose of this section is to provide an example which illustrates the benefits to
be gained from using both the log transformed Black–Scholes equation and also a
nonuniform grid.
The problem we will consider is the European double knockout call option with
strike price E, and expiry date T. This is a barrier option with both an upper
barrier at BU and a lower barrier at BL. If, during the life of the option, the asset
price either goes above the upper barrier or below the lower barrier then the
option becomes worthless. If, on the other hand, the asset price stays between the
barriers then the option has value max (ST  E, 0), where ST is the asset price at
time T.
This problem has been previously investigated by Boyle and Tian (1998),
henceforth referred to as BT, who used an explicit finite-difference method based
on a modified trinomial lattice. The method we use here is based on the finite-
difference equations given in Section 10.6.5, and all the results in Tables 10.8 to
10.12 were obtained by using the function dko_call which is provided in Code
excerpt 10.19.
206
Pricing Assets

void dko_call(double lower_barrier, double upper_barrier, double theta_m,
double S0, double sigma_array[], double sigma_times[], Integer n_sigma, double r,
double opt_mat, double X, double *option_value, double greeks[], double q,
Integer ns_below_S0, Integer ns_above_S0, Integer nt, Integer *iflag)
{
/* Input parameters:
lower_barrier
— the asset price corresponding to the lower barrier,
upper_barrier
— the asset price corresponding to the upper barrier,
theta_m
— the value of theta used for the finite difference method,
S0
— the current price of the underlying asset,
sigma_array[]
— an array containing values of the volatility: sigma_array[0] is the first value of
the volatility, sigma_array[1] is the second value of the volatility, etc..,
sigma_times[]
— an array containing the times for different volatilities: sigma_ times[0] is the time
corresponding to the first volatility, sigma_times[1] is the time corresponding to the
second volatility, etc..,
n_sigma
— the number of elements in sigma_ array[], and sigma_times [],
r
— the interest rate,
opt_mat
— the time to maturity,
X
— the strike price,
q
— the continuous dividend yield,
ns_below_S0
— the number of asset intervals below the current price S0,
ns_above_S0
— the number of asset intervals above the current price S0,
nt
— the number of time intervals.
Output parameters:
option_value
— the value of the option,
greeks[]
— the hedge statistics output as follows: greeks[0] is gamma, greeks[1] is delta,
and greeks[2] is theta,
iflag
— an error indicator.
*/
double *a, *b, *c, *vals, *a1, *b1, *c1, *opt_vals, *rhs, *z, *delta, *gamma, *work, *u;
double dt, dz, dz1, dz2, zmax, zmin;
Integer i, j;
double tmp, t2, t4, dt2;
Integer ind¼0, n1, n2, ns1;
double ds, log_asset, sig2, alpha, v2, b_fac, temp[4];
double zero ¼ 0.0;
Integer barrier_index, ind2;
double dz_shift, time_step, log_barrier_level1, log_barrier_level2;
double temp1, temp2, ds_plus, ds_minus, bb, D;
double curr_time;
if (S0 >¼ upper_barrier) printf (‘‘ERROR current asset price is greater than upper_barrier \n’’);
if (lower_barrier >¼ S0) printf(‘‘ERROR lower barrier is greater than current asset price \n’’);
if (S0 <¼ zero) printf (‘‘ERROR asset price is not > 0 \n’’);
if (upper_barrier <¼ lower_barrier) printf (‘‘ERROR upper_barrier must be > lower_barrier \n’’);
log_asset ¼ log(S0);
log_barrier_level1 ¼ log(lower_barrier);
log_barrier_level2 ¼ log(upper_barrier);
dz1 ¼ (log_assetlog_barrier_level1)/(double)ns_below_S0;
n1 ¼ ns_below_S0;
/* Include 5 extra points above the asset price so that don’t get discontinuity in grid spacing
which may adversely affect the computation of the greeks */
n2 ¼ ns_above_S0 þ 5;
dz_shift ¼ dz1*5.0; /* shift caused by extra 5 grid points */
dz2 ¼ (log_barrier_level2log_asset dz_shift)/(double) ns_above_S0;
dt ¼ opt_mat/(double)nt; /* time interval size */
time_step ¼ dt;
--n2;
ns1 ¼ n1 þn2 þ 2;
/* Set up the RHS and LHS coefficients a[], b[] and c[] are the LHS coefficients for the unknown option values
(time step j) a1[], b1[] and c1[] are the values of the RHS coefficients for the known option prices (time
step jþ1). Note: a1, b1 and c1 are used to form the RHS vector rhs[] of the tridiagonal system. */
/* Allocate the required arrays (all of size (ns1 þ 2): a, b, c, a1, b1, c1, opt_vals, vals, rhs, z, delta,
gamma, work, u */



/* Set up the RHS and LHS coefficients a[], b[] and c[] are the LHS coefficients for the unknown option values
(time step j) a1[], b1[] and c1[] are the values of the RHS coefficients for the known option prices (time
step j þ 1). Note: a1, b1 and c1 are used to form the RHS vector rhs[] of the tridiagonal system. */
/* Set grid line asset values, set one grid spacing to align with the asset price, then won’t have to
interpolate to get the option value */
z[n1] ¼ log_asset;
for (i ¼ 1; i <¼n1; þþi) /* This should be the fine mesh */
z[n1  i] ¼ log_asset  (double)i*dz1;
Numeric methods and single asset American options
207

for (i¼ 1; i <¼5; þþi) /* Include 5 extra fine mesh points here */
z[n1 þ i] ¼ log_asset þ (double)i*dz1;
for (i ¼ 6; i <¼n2þ2; þþi){/* The coarse mesh */
j ¼ i  5;
z[n1 þ i] ¼ z[n1 þ 5] þ (double)j*dz2;
}
/* Set option values at maturity (for a call). Note : opt_vals[0] and opt_vals[ns1 1] are the lower and upper
(put/call) option price boundary values. */
for( i ¼ 1; i<ns1; þþi ){
opt_vals[i] ¼ MAX(exp(z[i]) X, zero);
}
opt_vals[0] ¼ zero;
opt_vals[ns1 1] ¼ zero;
tmp ¼ 1.0theta_m; /* 1  theta (for theta method) */
curr_time ¼ 1.0;
ind2 ¼ n_sigma  1;
for( j¼nt1; j>¼2; j){/* Iterate from maturity to current time */
if ((ind2 >¼ 0) && (curr_time <¼ sigma_times[ind2])){
sig2 ¼ sigma_array[ind2]*sigma_array[ind2];
t2 ¼ time_step/2.0;
bb ¼ r  q  (sig2/2.0);
--ind2;
for( i ¼ 1; i<¼ns1  2; þþi){/* Assign elements of the (ns12)*(ns12) tridiagonal matrix */
ds_plus ¼ z[iþ1]z[i];
ds_minus ¼ z[i]  z[i1];
D ¼ ((ds_plus*ds_plus*ds_minus) þ (ds_minus *ds_minus *ds_plus));
temp1 ¼ tmp*time_step/D;
a[i] ¼ temp1*(bb*ds_plus*ds_plus)temp1 *ds_plus *(sig2 );
temp1 ¼ theta_m*time_step/D;
a1[i] ¼ temp1*ds_plus*(sig2)temp1*(bb*ds_plus *ds_plus);
temp1 ¼ (ds_minus*ds_minus)/D;
temp2 ¼ ds_minus/D;
c[i] ¼ time_step*tmp*(temp1*bbþ(sig2*temp2));
c1[i] ¼ time_step*theta_m*(temp1*bbþ(sig2*temp2));
temp1 ¼ ((ds_minus*ds_minus)  (ds_plus*ds_plus))/D;
temp2 ¼ (ds_minusþds_plus)/D;
b[i] ¼ 1.0þtime_step*tmp*(rþ(bb*temp1)þ(sig2) *temp2);
b1[i] ¼ 1.0 time_step*theta_m*(rþ(bb*temp1)þ (sig2)*temp2);
}
u[1] ¼ b[1];
if (u[1] ¼¼ zero) printf (‘‘ERROR in array u \n’’);
for( i¼2; i <¼ns1  2; þþi){
u[i] ¼ b[i]  a[i]*c[i  1]/u[i  1];
if (u[i] ¼¼ zero) printf (‘‘ERROR in array u \n’’);
}
}
curr_time ¼ j*dt;
/* Set up the rhs of equation for the theta method */
for(i¼2; i<¼ns13; þþi)
rhs[i] ¼ a1[i]*opt_vals[i1]þb1[i]*opt_vals[i]þ c1[i]*opt_vals[iþ1];
/* Incorporate the boundary conditions1 at the upper/lower asset value boundaries */
rhs[1] ¼ (a1[1]a[1])*opt_vals[0]þ b1[1]*opt_vals[1]þ c1[1]*opt_vals[2];
rhs[ns12] ¼ a1[ns12]*opt_vals[ns13]þb1[ns12] *opt_vals[ns12]þ
(c1[ns12]c[ns12])*opt_vals[ns11];
/* Solve the lower triangular system Ly ¼ b, where y is stored in array work[]. Compute the elements of L from
those of U, l[i] ¼ a[i]/u[i1]. */
work[1] ¼ rhs[1];
for(i ¼ 2; i<¼ns12; þþi){
work[i] ¼ rhs[i]  a[i]*work[i1]/u[i1];
}
/* Solve the upper (ns12)*(ns12) triangular system Ux ¼ y (where x ¼ vold) */
opt_vals[ns12] ¼ work[ns12]/u[ns12];
for(i ¼ ns12; i >¼ 1; i)
opt_vals[i] ¼ (work[i]  c[i]*opt_vals[iþ1])/u[i];
if (j¼¼0){
for (i¼0; i < ns1; þþi)
vals[i] ¼ opt_vals[i];
}
/* Store option values so that can compute theta */
if ((j¼¼1)||(j¼¼2)||(j¼¼1)||(j¼¼2)){
temp[ind] ¼ opt_vals[n1];
þþind;
}
}
if (greeks){
/* Compute gamma and delta (4th order accuracy) */
208
Pricing Assets

greeks[1] ¼ (vals[n1þ2]þ8.0*vals[n1þ1] 8.0*vals[n11]þ vals[n12])/(12.0*dz1);
/* Compute gamma (4th order accuracy)  use chain rule to obtain derivative wrt S */
greeks[0] ¼ (vals[n1þ2]þ16.0*vals[n1þ1] 30.0*vals[n1]þ16.0*vals[n11]vals[n12])/
(12.0*dz1*dz1);
greeks[0] ¼ greeks[0]greeks[1];
greeks[0] ¼ greeks[0]/(S0*S0);
greeks[1] ¼ greeks[1]/S0;
/* Compute theta (4th order accuracy) */
greeks[2]¼(temp[0]þ8.0*temp[1]8.0*temp[2]þtemp[3])/ (12.0*dt);
/* could also compute theta as: greeks[2] ¼ ( temp[0]þ4.0* temp[1] 3.0*vals[n1])/(2.0*dt); */
}
*option_value ¼ vals[n1];
}
Code excerpt 10.19
Function to compute the value and Greeks of a European double knock out call
option using a nonuniform grid and a logarithmic transformation
Inspection of the results shows that that the finite-difference grid method has
both greater accuracy and faster convergence than the method proposed by BT. The
key to the accuracy achieved by dko_call is a combination of:
. The logarithmic transformation of the Black–Scholes equation.
. The ability to place a grid line at both the upper barrier BU, and also at the lower
boundary BL.
. The use of a weighted m finite-difference scheme, 0  m  1, instead of the
numerically unstable explicit finite-difference method used by a trinomial lattice;
which in our notation (see Section 10.6.2) is equivalent to m ¼ 1.
Table 10.8
Estimated value of a European double knock out call option. The values in column
two were computed by the function dko_call, and those in column three are the results reported in
Table 2 of Boyle and Tian (1998). The model parameters were: current asset price S ¼ 95:0, exercise price
E ¼ 100:0, volatility  ¼ 0:25, maturity  ¼ 1:0, interest rate r ¼ 0:1, dividend yield q ¼ 0:0. The upper
barrier level is set at 140.0 and the lower barrier is set at 90.0. The other parameters used by the function
dko_call were: nt ¼ n, ns_below_S0 ¼n/2, ns_above_S0 ¼ n/2, and m ¼ 0:5
(i.e. the Crank–Nicolson method)
Time steps (n)
Estimated value
Boyle and Tian (1998)
50
1.4569
1.4238
100
1.4578
1.4437
200
1.4583
1.4495
300
1.4583
1.4524
400
1.4584
1.4542
500
1.4584
1.4553
600
1.4584
1.4557
700
1.4584
1.4559
800
1.4584
1.4563
900
1.4584
1.4565
1000
1.4584
1.4566
2000
1.4584
1.4576
3000
1.4584
1.4578
4000
1.4584
1.4580
5000
1.4584
1.4581
Numeric methods and single asset American options
209

Table 10.9
The estimated values of European down and out call options calculated
by the function dko_call. The fixed model parameters were: exercise price E ¼ 100:0, volatility
 ¼ 0:25, maturity  ¼ 1:0, interest rate r ¼ 0:1, dividend yield q ¼ 0:0 and the lower barrier is set at 90.0.
The other parameters used by the function dko_call were: nt ¼ n, ns_below_S0 ¼ n/2,
ns_above_S0 ¼ n/2, upper_barrier ¼ 1000.0, lower_barrier ¼ 90.0, and m ¼ 0:5
(i.e. the Crank–Nicolson method)
Stock price
Time steps
92
91
90.5
90.4
90.3
90.2
50
2.5652
1.3046
0.6588
0.5282
0.3971
0.2653
100
2.5221
1.2816
0.6466
0.5182
0.3894
0.2601
200
2.5104
1.2758
0.6435
0.5157
0.3875
0.2588
300
2.5080
1.2747
0.6429
0.5152
0.3871
0.2585
400
2.5072
1.2743
0.6427
0.5150
0.3869
0.2584
500
2.5069
1.2742
0.6426
0.5149
0.3869
0.2584
600
2.5067
1.2741
0.6425
0.5149
0.3868
0.2583
700
2.5066
1.2740
0.6425
0.5149
0.3868
0.2583
800
2.5065
1.2740
0.6424
0.5148
0.3868
0.2583
900
2.5065
1.2739
0.6424
0.5148
0.3868
0.2583
1000
2.5064
1.2739
0.6424
0.5148
0.3868
0.2583
2000
2.5063
1.2738
0.6424
0.5148
0.3868
0.2583
Closed form
2.5063
1.2738
0.6424
0.5148
0.3868
0.2583
Table 10.10
The estimated values of European down and out call options as calculated
by the function dko_call. The fixed parameters used were: exercise price E ¼ 100:0 volatility
 ¼ 0:25, maturity  ¼ 1:0, interest rate r ¼ 0:1, dividend yield q ¼ 0:0, and the lower barrier is set
at 90.0. The other parameters used by the function dko_call were: nt ¼ n, ns_below_S0 ¼ n=2,
ns_above_S0 ¼ n=2, upper_barrier ¼ 1000.0, lower_barrier ¼ 90.0, and m ¼ 0.0 (i.e. the
implicit method)
Stock price
Time steps
92
91
90.5
90.4
90.3
90.2
50
2.5572
1.3005
0.6567
0.5266
0.3958
0.2645
100
2.5181
1.2796
0.6455
0.5174
0.3888
0.2597
200
2.5084
1.2748
0.6429
0.5153
0.3872
0.2586
300
2.5067
1.2741
0.6425
0.5149
0.3869
0.2584
400
2.5062
1.2738
0.6424
0.5148
0.3868
0.2583
500
2.5061
1.2738
0.6424
0.5148
0.3868
0.2583
600
2.5061
1.2737
0.6423
0.5148
0.3867
0.2583
700
2.5060
1.2737
0.6423
0.5147
0.3867
0.2583
800
2.5060
1.2747
0.6423
0.5147
0.3867
0.2583
900
2.5060
1.2737
0.6423
0.5147
0.3867
0.2583
1000
2.5060
1.2737
0.6423
0.5147
0.3867
0.2583
2000
2.5061
1.2737
0.6423
0.5147
0.3867
0.2583
Closed form
2.5063
1.2738
0.6424
0.5148
0.3868
0.2583
210
Pricing Assets

It should be mentioned that the function dko_call could, without much diffi-
culty, be modified to deal with:
. American double knockout call options
. European double knockout put options
. American double knockout put options,
and also a range of other variations which may include lockout periods, rebates, etc.
In particular, options with time varying barrier levels can be dealt with by using grid
lines to locate the barrier position at each time instant.
Table 10.11
The estimated values of European double knock out call options computed by the function
dko_call. In columns 2 and 3 the values given in Boyle and Tian (1998), Table 5, are shown for
comparison. The fixed model parameters were: exercise price E ¼ 100:0, volatility  ¼ 0:25, dividend yield
q ¼ 0:0, maturity  ¼ 1:0, interest rate r ¼ 0:1, the lower barrier is set at 90.0 and the upper barrier is set at
140.0. The other parameters used by the function dko_call were: nt ¼ n, ns_below_S0 ¼ n=2,
ns_above_S0 ¼ n=2, and m ¼ 0:5 (i.e. the Crank–Nicolson method)
Stock price
Time steps
92
91
90.5
90.4
90.3
90.2
50
0.6251 (0.6184)
0.3189 (0.3177)
0.1610
0.1290
0.0969
0.0647
100
0.6260 (0.6212)
0.3194 (0.3184)
0.1613
0.1292
0.0971
0.0649
200
0.6263 (0.6228)
0.3196 (0.3186)
0.1613
0.1293
0.0972
0.0649
300
0.6263 (0.6236)
0.3196 (0.3187)
0.1613
0.1293
0.0972
0.0649
400
0.6263 (0.6242)
0.3196 (0.3189)
0.1613
0.1293
0.0972
0.0649
500
0.6263 (0.6252)
0.3196 (0.3190)
0.1613
0.1293
0.0972
0.0649
600
0.6263 (0.6253)
0.3196 (0.3191)
0.1613
0.1293
0.0972
0.0649
700
0.6263 (0.6253)
0.3196 (0.3191)
0.1613
0.1293
0.0972
0.0649
800
0.6263 (0.6255)
0.3196 (0.3192)
0.1613
0.1293
0.0972
0.0649
900
0.6263 (0.6256)
0.3196 (0.3192)
0.1613
0.1293
0.0972
0.0649
1000
0.6263 (0.6255)
0.3196 (0.3192)
0.1613
0.1293
0.0972
0.0649
2000
0.6263 (0.6260)
0.3196 (0.3195)
0.1613
0.1293
0.0972
0.0649
Table 10.12
The estimated Greeks for European double knock out call options computed by the function
dko_call. The fixed model parameters: the exercise price E ¼ 100:0, volatility  ¼ 0:25, dividend yield
q ¼ 0:0, maturity  ¼ 1:0, interest rate r ¼ 0:1, the lower barrier is set at 90.0 and the upper barrier is set at
140.0. The other parameters used by the function dko_call were: nt ¼ 200, ns_below_S0 ¼ 100,
ns_above_S0 ¼ 100, and m ¼ 0:5 (i.e. the Crank–Nicolson method). The results for m ¼ 0:0 (i.e. the
implicit method) are shown in brackets; see Table 6, Boyle and Tian (1998)
Asset price
Gamma
Delta
Theta
95.0
0.0165 (0.0166)
0.2536 (0.2551)
2.3982 (2.3928)
92.0
0.0141 (0.0141)
0.2998 (0.3016)
1.0268 (1.0242)
91.0
0.0129 (0.0130)
0.3133 (0.3151)
0.5237 (0.5224)
90.5
0.0123 (0.0123)
0.3196 (0.3215)
0.2643 (0.2636)
90.4
0.0121 (0.0122)
0.3208 (0.3227)
0.2119 (0.2113)
90.3
0.0120 (0.0121)
0.3221 (0.3239)
0.1592 (0.1588)
90.2
0.0119 (0.0119)
0.3233 (0.3251)
0.1063 (0.1060)
Numeric methods and single asset American options
211

10.7
PRICING AMERICAN OPTIONS USING A STOCHASTIC LATTICE
In this section, we consider the use of Monte Carlo simulation and stochastic lattices
to price American options. Information on the use of Monte Carlo simulation to
value both single asset and multiasset European options is provided in Sections 11.1
and 12.3. The main difficulty in using simulation to value American options is the
need to incorporate optimal early exercise policies. The standard simulation algo-
rithms for valuing European contracts are forward in time. That is each price path,
which contributes to the value of the option, is generated by stepping forward from
current time, t, to option maturity, t þ , where  is the duration of the option. For
instance if there are n equispaced time steps of size t, and only one underlying asset
then we use the asset values Si, i ¼ 0, . . . , n, where Si corresponds to the asset value
at the ith time instant, ti, and t0 ¼ t. Here Siþ1 is generated from the previous asset
value Si as follows:
Siþ1
Si
¼ dSi;
for
i ¼ 0; . . . ; n  1
ð10:204Þ
where dSi is a random variate taken from a given distribution. When Si follows GBM
we have from Equation 12.5 that:
Siþ1
Si
¼ exp
r  2
i =2


t þ idXi
	

;
i ¼ 0; . . . ; n  1
ð10:205Þ
where dXi 
 N(0, t) and the usual definitions are used for i and r.
For European exotic options (such as time dependent barrier options) the value of
a particular price path will depend on the asset values Si, i ¼ 0, . . . , n. This is not true
of European vanilla options whose value only depends on Sn, the underlying asset
price at option maturity. The Monte Carlo approximation to the value of a European
option is thus:
f ¼
X
nsim
j¼1
pjðnjÞ
nsim
where nsim is the number of simulations used, nj is the number of time steps
associated with the jth price path, and pj(nj) is the value of the jth price path. In
the case of European vanilla options we can use nj ¼ 1, j ¼ 1, . . . , nsim; the accuracy
obviously improves with increasing nsim.
The valuation of American style options, which include the possibility of early
exercise, is more complicated. In Section 10.4, we described the use of binomial lattices
to price American options when the underlying asset price process is GBM. Dynamic
programming was used and the option prices were computed by working backwards in
time through the lattice. The application of Monte Carlo methods for pricing American
options is described in Fu etal. (2001), Tilley (1993), Barraquand and Martineau (1995)
and also Boyle etal. (1997). Here we will outline the stochastic lattice approach
discussed in Broadie and Glasserman (1997), where both a high estimator and a low
estimator of the American option value are calculated. Since both of these biased
estimators converge (with increasing number of simulations and lattice nodes) to the
212
Pricing Assets

true option value we will only consider how to compute the high estimator, H. We
summarize the approach as follows:
. Set the parameters
. Generate the lattice asset prices
. Compute the lattice option prices
. Compute the Monte Carlo estimate.
We will now consider each of these steps in more detail.
Set the parameters
First we set the simulation parameters, that is: nsim is the number of lattice simula-
tions, b is the number of branches per lattice node and d is the number of time
instants in the lattice. Note: This definition of d here is different from that used in the
original paper by Broadie and Glasserman (1997) where d is defined as the number of
time steps in the lattice.
Generate the lattice asset prices
Next we generatethe asset prices for the pth stochastic lattice. This isdoneforwardsin time
by using a modified version of Equation 10.205. Since the lattice is nonrecombining at the
ith lattice time instant there are bi nodes/asset prices. This contrasts with the binomial
lattice of Section 10.4 where the asset prices at a given time step are arranged in ascending
order, that is Sj
i increases with increasing j. We will denote the jth value at the ith time step
by Sj
i. For example in Figure 10.13, where b ¼ 3 and d ¼ 3, we have for the first time step
S1
1 ¼ 115;
S2
1 ¼ 60;
and
S3
1 ¼ 114
and for the second time step
S1
2 ¼ 116;
S2
2 ¼ 90;
S3
2 ¼ 149; . . . ;
S7
2 ¼ 102;
S8
2 ¼ 88;
S9
2 ¼ 80
The kth asset price at the ith time step, Sk
i then generates the following asset prices
at the (i þ 1)th time step:
Sðk1Þbþj
iþ1
Sk
i
¼ dSj;
j ¼ 1; . . . ; b;
k ¼ 1; . . . ; bi
where dSj is, as before, a random variate from a given distribution. When Si follows
GBM we therefore have:
Sðk1Þbþj
iþ1
Sk
i
¼ exp
r  2
i =2


t þ idXi
	

;
j ¼ 1; . . . ; b;
k ¼ 1; . . . ; bi
Compute the lattice option prices
The method used to compute the option values is similar to that used by the
binomial lattice. The main difference is that there are now b branches per node
Numeric methods and single asset American options
213

instead of two. The option values are computed by starting at the lattice terminal
nodes and then iterating backwards. Here we denote the kth option value at the ith
time step by f k
i .
The option values at the terminal nodes, time instant td1, are computed in the
usual manner. For a put we have:
f k
d1 ¼ maxðE  Sk
d1; 0Þ;
k ¼ 1; . . . ; bd1
where E is the exercise price.
The option values at the (i  1)th time step are computed from those at the ith time
step as follows:
f k
i1 ¼ maxðgk
i1; hk
i1Þ
where
hk
i1 ¼ expðrtÞ
b
X
b
j¼1
f ðk1Þbþj
i
60
50
115
114
101
32
102
80
88
48
149
116
90
t2
t1
t0
Figure 10.13
An example showing the asset prices generated for a stochastic lattice with three branches
per node and two time steps, that is b ¼ 3 and d ¼ 3. The current asset value, 101, is at time t0, and the
asset values at option maturity are at time t2
214
Pricing Assets

and
gk
i1 ¼ maxðE  Sk
i1; 0Þ
The option value for the pth stochastic lattice is therefore:
p
H ¼ f 1
0 ¼ expðrtÞ
b
X
b
j¼1
f j
1
Figure 10.14 shows the option values for an American call with strike price E ¼ 100
and interest rate r ¼ 0, when the lattice asset prices in Figure 10.13 are been used. To
make things as clear as possible we will show how the value of each node is computed.
Terminal nodes
The option values at the terminal nodes are:
f 1
2 ¼ maxð116  100; 0Þ ¼ 16;
f 2
2 ¼ maxð90  100; 0Þ ¼ 0;
f 3
2 ¼ maxð149  100; 0Þ ¼ 49
0
0
21.7
14
11.9
0
2
0
0
0
49
16
0
t2
t1
t0
Figure 10.14
The option prices for the b ¼ 3, d ¼ 3 lattice in Figure 10.13 corresponding to an American
put with strike E ¼ 100 and interest rate r ¼ 0. The option values at the lattice nodes are computed
backwards in time from the payoffs at maturity, t2 to the current time t0; the value of the option is 11.9
Numeric methods and single asset American options
215

