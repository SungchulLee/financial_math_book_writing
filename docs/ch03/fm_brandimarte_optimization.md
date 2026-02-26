# Optimization Methods in Finance

!!! info "Source"
    **Numerical Methods in Finance and Economics** by Paolo Brandimarte, Wiley, 2nd ed., 2006.
    These notes are used for educational purposes.

## Linear, Quadratic and Nonlinear Programming

Part 111 
Pricing Equity Options 

This Page Intentionally Left Blank

7 
Option Pricing by 
Binomial and Trinomial 
Lattices 
In this chapter we deal with binomial and trinomial lattices for option pric- 
ing. Binomial lattices were introduced in section 2.1 as a basic way to model 
uncertainty in prices. They rely on a discretization of the underlying stochas- 
tic process and exploit recombination to keep computational and memory 
requirements to a manageable level. We have also seen in section 2.6.1 that 
pricing options by a no-arbitrage argument is rather simple in a single step 
binomial lattice. In order to get a practical pricing procedure, we must extend 
the idea to a multistep lattice, but first we have to find a way to calibrate 
the lattice so that it reflects the underlying model which is a continuous-time, 
continuous-state stochastic differential equation. Then we can generalize to 
multidimensional binomial lattices and to trinomial lattices. 
In section 7.1 we start by showing how a simple binomial lattice may be 
calibrated by matching moments of the discrete probability distribution of 
prices to drift and volatility of the stochastic process. F’rom this point of view, 
it is important to understand the connection between lattice techniques and 
Monte Carlo simulation: Moment matching is a variance reduction strategy, 
and it can be regarded as a sort of clever sampling. Then we discuss how 
memory-efficient implementations may be devised. Pricing American options 
is the subject of section 7.2. Again, it is important to see connections with 
other techniques. What we do here is essentially a very simple application 
of the dynamic programming principle which is fully developed in chapter 
10. In section 7.3 we consider the generalization to an option depending on 
two underlying assets; this is only the simplest case, but we see that efficient 
memory management is fundamental in this case. Another generalization is 
represented by trinomial lattices 7.4; trinomial lattices can be regarded as a 
401 

402 
OPT/ON PRICING BY BINOMIAL AND TRINOMIAL LATTICES 
Fig. 7.1 Simple single-period binomial lattice. 
particular case of the more general finite difference approach (t,his is discussed 
in section 9.2.1). Finally, we consider advantages and disadvantages of lat#tices 
in section 7.5. 
7.1 PRICING BY BINOMIAL LATTICES 
In sectioii 2.G.1, we have considered arbitrage-free pricing of an option by a 
single step I>inomial lattice, which is recalled in figure 7.1 for convenience. 
The idea was to replicate the option with two assets, a risk-free asset and the 
untlerlying stork. With two assets, we may replicate any payoff defined over 
two states. If we model uncertainty with two possible multiplicative shocks u 
and d. we have seen that, the fair option price fo is 
where f i L  and f,l are the option payoffs in the up and down states, respectively, 
and p is the risk-neutral probability of the up step: 
e r 4 t  - d  
u-(1 . 
p = 
To allow for a better model of uncertainty, we should increase the number of 
states; to replicate the option payoff, we can either use more assets or allow for 
trading at intermediate dates. The second possibility is more practical and it is 
essential, e.g., to price American options, which allow for early exercise at any 
tinie during optioii life. In the limit, this leads to a continuous time model and 
to the Black--%holes framework. When the Black-Scholes framework does not 
lend to an analytical solution, we must resort to some discretization approach, 
which can he sampling hy Monte Carlo simulation, to estimate the risk-neutral 
expectat,ion, or setting up a grid an apply finite difference methods to solve 
t,he corresponding PDE. A multistage binomial lattice, like the one shown in 
figure 7.2, is an alternative discretization approach; we could also consider 
trees, but recornhination keeps computational effort to a manageable level. 

PRICING BY BINOMIAL LATTICES 
403 
SU' 
SU? 
8 
s u  
Su'd 
s a  
a
s
 
1 
* Sud2 
Sd 
V 
SdL 
Sd3 
Fig. 7.2 Recombining binoniial lattice 
Here we have adopted the convenient choice u = l/d. This is not necessary, 
a s  w(: will SCY shortly, Init, iii this way, ail l i p  st,cp followed by a clown step 
yicllds t,lic: siiiiic! init,ial priw 
SCl nd = S ( & L  
= Si,. 
As MT iiiily SCC form the figurel, riot, only we have recombination, hut, thr 
I;ttt,ic:e iises a liiiiited number of prices too. This may he an advantage wlien 
iiiil)lCiiiciiit,iiig t.lic nicthod. How can we select sensible values for u. and d'? WL' 
shoiiltl calilnxt,c the lattice in siich a way that it approximates the underlying 
coiitiiiiioiis-t,irrio proccss. 
7.1.1 Calibrating a binomial lattice 
Tlie 1)iiioiriinl Iat t,ic:e shorilrl t x  a good approximation of the risk-neutral pro- 
t l S  = 7.s /it + 0s dkV. 
€ I c m ~ .  
~
(
3
 
slioultl find paramc%ers t,o set, up the lattice, in s;uch a way t , h t  
sonit: esscritial properties of the continuous-time model are preserved. This 
proross is callctl r:nlib~ntion. St,art,irig from S t ,  after a small t,iine iiiterviil bt . 
\w h o w  froin srctioii 2.5 thnt tlie new price is a randoni variatde St+,st such 
('CSS 
t,liil t 
log(S/,+,j//S/) 
N N ( ( T  - g2/2) ht, ~ ' h t )  
. 
Usiiig properties of t,he logriorrrial tlistrilxition (see appendix B) , we have 
E[sL+,j/ /S~I 
= eT "" 
(7.2) 
iLil(1 
9 . 
(7.3) 

404 
OPJlON PRlClNG BY BINOMIAL AND TRlNOMlAL LAJJlCES 
A reasonable requirement on the discretized dynamics is that it should match 
these moments. Note that these are two conditions, but we have three pa- 
rameters: p ,  u, 
and d. So we have one degree of freedom, and we may choose 
u = l / d .  This is a convenient choice from a computational point of view, but 
it is not the only possibility. 
On the lattice, we have 
which, together with (7.2), yields 
Note that p is a risk-neutral probability, which does not depend on the true 
drift. To match variance, we see that, on the lattice, 
2 e2r 6t 
Var(St+st) = E[S?+bt] - E2[St+6t] = S?(pu2 + (1 -p)d2) - S, 
. 
From (7.3) we also see 
~ a r [ ~ t + s t ]  
= S?e2'6t (em2'' - 1 )  , 
and putting the last two equations together we get 
S?e2r6t (eUzbt - 1) = S?(pu2 + ( 1  - p)d2) - S?e2r6t, 
which boils down to 
eZr 6t+u26t = pu2 + ( 1  - p)&. 
Substituting p in the right-hand side of the last equation and simplifying: 
erst - d 
u - er6t 
u2 + 
~ 
d2 
u - d  
u - d  
u2eT6t - u2d + U d 2  - d2er6t 
- 
- 
21-d 
(u2 - d2)er6, - (u - d )  
- 
- 
= (u + d)erdt - 1, 
u - d  
we end up with the equation 
e~r6t+uz 6t - 
- (u + d)erbt - 1, 
which, using u = l / d ,  can be transformed into the quadratic equation: 
) + erst = 0. 

PRICING BY BINOMIAL LATTICES 
405 
A root of the equation is 
Using first-order expansions, limited to powers of order 6t, we may simplify 
the expression. Starting from the term under square root, we get 
(1 + e2r6t+u26t - 4eZTbt M (2 + (27- + 
- 4(1 + 2 r 6 t )  M 4026t. 
Hence, 
1 + T 6t + "'st + U J s t  (1 - T 6t) 
= (  
2 
1 
0 2  
u2 
2 
2 
M 1 + T 6t + -6t + a& - r 6t = 1 + U J b t  + -6t. 
But this, to the second order, is the expansion of eua. 
We end up with the 
parameterization 
(7.4) 
which is known as CRR (Cox, ROSS, and Rubinstein). 
It should be stressed that this is not the only plausible approach, and that 
alternative parameters are proposed in the literature. For instance, we could 
arbitrarily choose p = 0.5, which, after some calculations, leads to 
(7.- g) 
b t + o f i  
= e(T-g)6t-u6t 
u = e  
1 
p = -  
2 '  
, 
, 
which is known as Jarrow-Rudd parameterization. Furthermore, we have been 
grappling with rather involved calculations involving non-linear equations. By 
working on logarithms of price we may try to avoid these difficulties; we will 
pursue this approach later. 
Assuming that the risk-free interest rate and volatility are constant in time, 
the parameters we have obtained apply to the entire lattice. To price an 
option, we should build (explicitly or implicitly) a lattice for the underlying 
asset prices, and then we should proceed backward in time. In fact, the 
option value is known at maturity, where it is given by the option payoff. 
Then we should apply equation (7.1) recursively, going backward one step at 
a time, until we reach the initial node. The binomiaI Iattice approach is best 
illustrated by its application to a vanilla European call option. 

406 
OPTlON PRlClNG BY BlNOMlAL AND TRlNOMlAL LATTlCES 
Example 7.1 Suppose that we want to find the price of a vanilla European 
call with SO = K = 50, T = 0.1, 0 = 0.4, and maturity in five months. From 
the Black-Scholes model, we know the solution: 
>> call=blsprice(50,50,0.1,5/12,0.4) 
call = 
6.1165 
If we want to approximate the result by a binomial lattice, we must first set 
up the lattice parameters. Suppose that each time step is one month. Then 
bt = 1/12 = 0.0833 
u = eua 
= 1.1224 
d = 1/21 = 0.8909 
The resulting lattices for the stock price and the option value are shown 
in figure 7.3. The rightmost layer in the call price lattice is obtained by 
computing the option payoff. To clarify the calculations, let us consider how 
the uppermost node in the second-to-last time layer is obtained: 
e - ~ , 6 t  [p. 39.07 + (1 - p )  .20.77] 
- 
- e-0.1,0.0833 [0.5073. 39.07 + 0.4927.20.771 M 29.77. 
Going on recursively, we see that the resulting option price is about 6.36, 
which is not too close to the exact price; a smaller time step is needed to get 
a good approximation. 
To implement the approach in MATLAB we require an algebraic expression 
of the backward evaluation process. Let fij be the option value in node (i,j), 
where j refers to time instant j bt (j = 0,. . . , N )  and i is the ith node in period 
j (node numbers increase going up in the lattice, i = 0,. . . , j ,  so we should 
think of turning the lattice upside down). N is the number of time steps we 
consider; hence, there are N + 1 time layers in the lattice and N6t = T ,  the 
option maturity. With these conventions, the price of the underlying asset in 
node (i, j )  is S u i d j - i .  At maturity we have 
f i , N  = max(0, SuidN-i - K } ,  
i = O , l ,  ..., N. 
Going backward in time (decreasing time subscript j), we get 
f i j  = e-r 6 t [ p j i + l , j + l  + (1 -p)fi,j+l]. 
(7.5) 
The implementation in MATLAB is straightforward, and the resulting code 
is shown in figure 7.4. The only point worth noting is that matrix indexes 
start from 1 in MATLAB, which requires a little adjustment. The function 

PRlClNG BY BlNOMlAL LATTKES 
407 
Fig.7.3 Binomial lattices for the European call option of example 7.1.

408 
OPTION PRICING BY BINOMIAL AND TRINOMIAL LATTICES 
function [price, lattice] = LatticeEurCall(SO,K,r,T,sigma,N) 
deltaT = T/N; 
u=exp(sigma * sqrt (deltaT)) ; 
d=l/u; 
p=(exp(r*deltaT) - d)/(u-d) ; 
lattice = zeros(N+l,N+l); 
for i=O:N 
end 
for j=N-1 : -1 : 0 
for i=O:j 
lattice(i+l,N+l)=max(O , SO*(u-i)*(d-(N-i)) - K); 
lattice(i+l,j+l) = exp(-r*deltaT) * ... 
(p * lattice(i+2,j+2) + (1-p) * lattice(i+l,j+2)); 
end 
end 
price = lattice(1,l) ; 
Fig. 7.4 MATLAB code for pricing a European call by a binomial lattice. 
Latt iceEurCall receives the usual arguments, with the addition of the num- 
ber of time steps N. By increasing the last parameter, we see that we get a 
more accurate price (with an increase in the computing time): 
>> call=LatticeEurCall(50,50,0.1,5/12,0.4,5) 
call = 
>>call=LatticeEurCal1(50,50 ,O. 1,5/12,0.4,500) 
call = 
6.3595 
6.1140 
It is interesting to investigate how the price computed by the binomial lattice 
converges to the correct price. This may be accomplished by the script in 
figure 7.5, which produces the output shown in figure 7.6. In this case, the 
error exhibits an oscillatory behavior as the number of time steps increases. 
0 
The implementation we have just discussed has a number of weaknesses. To 
begin with, it uses a large matrix to store the lattice, almost half of which is 
left empty. We also return the whole lattice as an output argument, which 
may be useful to check the correspondence with figure 7.3, but may be useless 
in practice. Actually, we need only two consecutive time layers to store the 
required information, so some improvement can be obtained. Furthermore, 
we keep multiplying the discount factor times the risk-neutral probabilities 
inside the loop; time can be saved by moving this computation outside the 

PRICING BY BINOMIAL LATTICES 
409 
C0mpLatticeBLS.m 
SO = 50; 
K = 50; 
r = 0.1; 
sigma = 0.4; 
T = 5/12; 
N=50 ; 
BlsC = blsprice (SO,K,r ,T, 
Sigma) ; 
LatticeC = zeros(1,N); 
for i=(l:N) 
end 
plot(l:N, ones(l,N)*BlsC); 
hold on; 
plot(l:N, LatticeC); 
Latt iceC (i) = Latt iceEurCal1 (SO, K , r , T, sigma, i) ; 
Fig. 7.5 Script to check the accuracy of the binomial lattice for decreasing 6t. 
7
4
-
 
I 
7 2 -  
7 -  
6 6 -  
6.4 - 
6 2 -  
6 -  
5 6  
I 
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
5.4 I 
Fig. 7.6 Exact and approximate prices for increasing number of steps in a binomial 
lattice. 

410 
OPTION PRlClNG BY BlNOMIAL AND TRINOMIAL LATTICES 
loop. We will pursue these improvements in section 7.1.3; in the next section 
we show an application of binomial lattices to a non-standard option. 
7.1.2 
We consider here a pay-later call option on a non-dividend paying stock.' The 
feature of the pay-later option is that no premium is paid up front, when the 
contract is entered; it will be paid later. If the option is in the money at 
expiration, the option must be exercised and a premium is paid to the writer. 
Otherwise, the option expires worthless and no premium is due. Note that the 
net payoff for the option holder can be negative, when the option is not deeply 
in the money, so that the payoff is smaller than the premium; it is easy to see 
by no-arbitrage arguments that if the net payoff were always non-negative, we 
could not have a contract with zero value at time t = 0. How can we find the 
fair premium value? 
Putting two things together: pricing a pay-later option 
Given a premium P ,  the payoff will be 
ST-K-P 
i f S r 2 K  
f(ST,P) = { 
otherwise. 
For a given P we may find the value of the option using a binomial lattice. 
Now we must find a value P such that the risk-neutral expectation of the 
payoff, with respect to ST, is zero: 
Note that here the discount factor, provided interest rate is constant over 
time, does not play any role. To solve this equation for P, we may couple 
the binomial lattice with the bisection method to solve non-linear equations 
(see section 3.4.1). First we prepare a function to evaluate the expectation for 
given P; the MATLAB code is shown in figure 7.7. Let us consider an option 
on a stock whose current price is $12, with volatility 20%; the risk-free rate is 
10%; the strike price is $14; maturity is 10 months. We use a binomial lattice 
with a time step corresponding to one month; hence the number of time steps 
is 10. We may build an anonymous function returning the discounted payoff 
when P is given, and then we apply bisection using fzero and a starting 
premium for the search: 
>> f = @(PI Lll(P,12,14,0.1, 0.2, 10/12, 10) 
f =  
@(P) Lll(P,l2,14,0.1, 0.2, 10/12, 10) 
>> fzero(f ,2) 
2.0432 
ans = 
'This example is based on [5, chapter 13, exercise 111. 

PRICING BY BINOMIAL LATTICES 
411 
1 exercise 11 chapter 13 from Luenberger, Investment Science 
function ExpPayoff = Lll(premium,SO,K,r,sigma,T,N) 
deltaT = T/N; 
u=exp(sigma * sqrt (deltaT)) ; 
d=l/u; 
p=(exp(r*deltaT) - d)/(u-d) ; 
lattice = zeros(N+l,N+l) ; 
for i=O:N 
if (SO*(u*i)*(d^(N-i)) 
>= K) 
end 
lattice(i+l,N+l)=SO*(u^i)*(d-(N-i)) 
- K - premium; 
end 
for j=N-1 : -1 : 0 
for i=O: j 
end 
lattice(i+l, j+l) = p*lattice(i+2, j+2) + (l-p)*lattice(i+l, j+2) ; 
end 
ExpPayoff = lattice(1,l); 
Fig. 7.7 MATLAB code to price a pay-later option by a binomial lattice. 
We see how fzero could be used in all those cases in which an analytical 
pricing formula is not known, even without relying on derivatives (which may 
be hard to compute for a binomial lattice, but it could be approximated 
numerically). 
7.1.3 
The implementation of binomial lattices we have used so far can be improved, 
both from the point of view of CPU time and memory requirements. To begin 
with, there is no need to repeat calculation of discounted probabilities in the 
f o r  loop; we can multiply discount factor and probabilities once. F’urther- 
more, we may also see that with the CRR lattice calibration, whereby ud = 1, 
we may save memory by using a vector to store the underlying asset prices, 
rather than a two-dimensional matrix. For instance, we see in figure 7.3 that 
only eleven different values are used for the underlying asset price. With this 
lattice calibration, if there are N time steps, we have 2N + 1 different price 
values. Hence they can be stored in a single array, with considerable saving. 
If we require 1000 steps for an accurate evaluation, there is a big difference 
between requiring a matrix with 1000 x 1000 elements or a vector with 2001 
entries. A possible scheme to store prices is shown in figure 7.8. The numbers 
shown in the picture are locations in the vector. In element 1 we store the 
lowest value, resulting from a sequence of down steps only. We see that odd- 
An improved implementation of binomial lattices 

412 
OPTlON PRICING BY BINOMIAL AND TRINOMIAL LATTICES 
Fig. 7.8 Saving memory for bimniial lattices. 
nunihcred entries correspond to the last time layer, whcreas even-numbered 
entries correspond to the second-to-last time layer. The root of the lattice 
may be even or odd-numbered depending on the number of time steps. 
The same scheme may be adopted to store option values. In principle, we 
should use two vectors corresponding to two consecutive time layers; however, 
we may exploit the fact that even numbered elements belong to a layer, and 
odd-nuinhered elements belong to another one, in order to use one vector of 
2N + 1 elements. The resulting code is shown in figure 7.9. A few comments 
are in order. 
0 We precompute invariant quantities, including discounted probabilities, 
in the first section of the code. 
0 When we write the vector SVals of underlying asset prices, we start 
with the smallest element, which is SodN; then we multiply by u; for 
nuinerical accuracy it would be somewhat better to store " 3 ~ ~  
in element 
SVals (N+i) which is the mid-element, and then proceed both up and 
down. 
0 Note that when we work with call values (CVals) we step by two over 
the index, which amounts to alternating odd- and even-indexed values 
corresponding to consecutive time layers. 
0 When time to maturity is 7, we need to consider only the 2(N - 7) + 1 
innermost elements of the array CVals. The option price is stored in 
the root of the lattice, which corresponds to position N+i. 
M'e may check that the computation here is a bit more efficient than with the 
previoiis version: 
>> blsprice(50,50,0.1,5/12,0.4) 
ans = 

PRICING BY BINOMIAL LATTICES 
413 
function price = SmartEurLattice(SO,K,r,T,sigma,N) 
% Precompute invariant quantities 
deltaT = T/N; 
u=exp(sigma * sqrt (deltaT)) ; 
d=l/u; 
p=(exp(r*deltaT) - d)/(u-d) ; 
discount = exp(-r*deltaT); 
p-u = discount*p; 
p-d = discount*(l-p); 
7, set up S values 
SVals = zeros(2*N+1,1> ; 
SVals(1) = SO*d-N; 
f o r  i=2:2*N+1 
end 
1 set up terminal CALL values 
CVals = zeros (2*N+1,1> ; 
for i=1:2:2*N+1 
end 
% work backwards 
for tau=l : N 
SVals(i) = u*SVals(i-l); 
CVals(i) = max(SVals(i)-K,O) ; 
for i= (tau+l):2: (2*N+l-tau) 
end 
CVals(i) = p-u*CVals(i+l) + p-d*CVals(i-l) ; 
end 
price = CVals(N+l); 
Fig. 7.9 Improved code for pricing a European call by a binomial lattice. 

414 
OPTION PRICING BY BINOMIAL AND TRINOMIAL LATTICES 
6.1165 
>> tic,LatticeEurCa11(50,50,0.1,5/12,0.4,2000~,t0c 
ans = 
6.1159 
Elapsed time is 0.262408 seconds. 
>> tic,SmartEurLattice(50,50,0.1,5/12,0.4,2000),toc 
ans = 
6.1159 
Elapsed time is 0.069647 seconds. 
We could try looking for some further improvements by vectorizing code, 
or by taking a different approach. We will not pursue this in order to avoid 
obscure code, and to make further developments easier to grasp. The saving 
in CPU time may not look impressive, but this memory saving approach is 
essential when we deal with multidimensional options. 
7.2 
PRICING AMERICAN OPTIONS BY BINOMIAL LATTICES 
Pricing an American option by the binomial lattice technique that we have 
illustrated in the last section is fairly easy. The only critical point is how we 
should account for early exercise. We deal here with a vanilla American-style 
put option on a non-dividend paying stock.’ Consider a point (i, N )  on the 
last time layer of the lattice. If the option is in the money at expiration, it is 
obviously optimal to exercise it. Hence, in the last time layer we have 
f i N  = max{K - si~,O}, 
where S ~ N  
= SuidNPi is the underlying asset price on that node. Now con- 
sider a point in the second-to-last time layer. If the option is not in the 
money, i.e., if Si,N-l > K, we do not exercise. But if the option is in the 
money, we should wonder about the opportunity of taking an immediate profit 
K - Si,~-l, 
rather than waiting for possibly better opportunities in the fu- 
ture. In other words, we have to solve an optimal stopping problem, whereby 
at each time step we must observe the state of a dynamical system and decide 
whether we should stop the game, and just grab the money we can immedi- 
ately, or we should go on. 
We do this in a simple way, by comparing the immediate payoff (the in- 
trinsic value of the option) against the continuation value. If we continue and 
keep the option, we have an asset whose value is 
’The corresponding call is not interesting, as it can be shown that it is never optimal to 
exercise it early, unless dividends are paid during the option life. 

PRICING AMERICAN OPTIONS BY BINOMIAL LATTICES 
415 
where p ,  and p d  are risk-neutral probabilities. We should exercise if the 
intrinsic value exceeds the continuation value. Hence, the option value in 
each node in the second-to-last time layer is 
f l , N - l  = max{K - S i , N - l r  e - T b t ( p u f i + l , N  + p d f i , N ) ) .  
The same argument may be repeated in a recursive fashion for any time layer. 
This means that we should start from the last time ayer, where the option 
value is just the option payoff, and we should proceed backward in time using 
a slight modification of the usual discounted expectation scheme of equation 
(7.5): 
(7.6) 
f .  
z , J  . - 
- m a x { ~  
- s i j ,  e - T b t ( p j i + i , j + i  + (1 - ~ ) f i , j + l ) ) .  
This idea looks deceptively simple, but it is an application of a very general 
principle called dynamic programming. We will see in chapter 10 that the 
dynamic programming principle is extremely powerful in theory, but it is 
sometimes difficult to apply because of the “curse of dimensionality.” In 
the binomial lattice case, we use a computationally cheap discretization of 
the underlying stochastic process, and dynamic programming looks almost 
trivial. However, the application of this principle should be carefully justified 
along the lines of section 2.6.6. In fact, the reasoning we have followed is 
somewhat misleading, as we have taken the point of view of the option holder 
who wants to exercise her option optimally. But we should wonder why we 
are just using expected values, ignoring risk aversion. A careful justification 
is not so trivial, and it should involve no-arbitrage arguments and the point 
of view of the option writer who should care about his worst case, which is 
when the option holder exercises optimally her rights. 
Leaving theoretical issues aside, it is actually easy to adapt the code that 
we have developed for the European-style call to an American-style put. The 
resulting code is shown in figure 7.10. We initialize the lattice in a slightly 
different way, but the only significant change is in backward time-stepping, 
where we compare the hold value against intrinsic value. 
The Financial toolbox provides us with a function, binprice, which prices 
vanilla American puts and calls, allowing for the possibility of continuous and 
lumpy dividends. We may compare binprice with AmPutLattice to check 
our implementation: 
>> SO = 50; 
>> K = 50; 
>> r = 0 . 0 5 ;  
>> T = 5/12; 
>> sigma = 0.4; 
>> N = 1000; 
>> price = AmPut Lattice (SO, K, r , T , sigma, N) 
price = 
>> [p, 01 = binprice(SO,K,r,T,T/N,sigma,O); 
4.6739 

416 
OPTION PRICING BY BINOMIAL AND TRINOMIAL LATTICES 
function price = AmPutLattice(SO,K,r,T,sigma,N) 
% Precompute invariant quantities 
deltaT = T/N; 
u=exp(sigma * sqrt(de1taT)) ; 
d=l/u; 
p=(exp(r*deltaT) - d)/(u-d) ; 
discount = exp(-r*deltaT); 
p-u = discount*p; 
p-d = discount*(l-p) ; 
% set up S values 
SVals = zeros (2*N+1,1> ; 
SVals(N+l) = SO; 
for i=l:N 
SVals(N+l+i) = u*SVals(N+i); 
SVals (N+l-i) = d*SVals (N+2-i) ; 
end 
% set up terminal values 
PVals = zeros (2*N+1,1) ; 
for i=1:2:2*N+1 
end 
% work backwards 
for tau=l:N 
PVals(i) = max(K-SVals(i) ,O) ; 
for i= (tau+l) :2: (2*N+l-tau) 
hold = p-u*PVals(i+l) + p-d*PVals(i-l); 
PVals(i) = max(hold, K-SVals(i)); 
end 
end 
price = PVals(N+l); 
Fig. 7.10 MATLAB code for pricing an American put by a binomial lattice. 

PRICING BlDlMENSlONAL OPTIONS BY BINOMIAL LATTICES 
41 7 
>> o ( l , l )  
ans = 
4.6739 
The function binprice requires a flag indicating if the option is a put (flag set 
to 0) or a call (flag set to 1). This parameter is the last one in the snapshot 
above. Also note that binprice requires both option expiration date T and 
time step d t  as inputs; we have set d t  = T/N. We have omitted the optional 
parameters that may be used to account for dividends. The output from 
binprice is in the form of two lattices, one for the underlying asset price and 
one for the option value; it is important, when the time step is small, to use 
the semicolon to suppress output on the screen. 
7.3 
PRICING BlDlMENSlONAL OPTIONS BY BINOMIAL LATTICES 
To illustrate the extension of lattice techniques to multidimensional options, 
we consider here an American spread option on two assets. The payoff of this 
option is 
max(S1 - S2 - K ,  0). 
The basic approach can be extended to more general options, provided we do 
not include complex path dependencies. As a further generalization, we also 
consider continuous dividend yields q1 and 92. Actually this does not change 
the problem that much, as we have only to adjust the risk-neutral dynamics, 
which are given by the equations [see also equation (2.42)]: 
where the two Wiener processes are correlated, and the formal rule dW1 d W 2  = 
p d t  applies (see section 2.5.5). 
To avoid the difficulties we had with non-linearities in the calibration 
process, it is convenient to work with logarithms of asset prices. Setting 
2% = log Si and using Ito’s lemma, we get the two stochastic differential equa- 
tions: 
where ui = T - qi - ~2212, i = 1,2. 
Now, as typical in binomial lattices, we assume that both assets may go up 
or down by an amount Sxi, in terms of logarithm of prices. To calibrate the 
lattice, we match first- and second-order moments. We have two stocks which 
may jump up or down. Hence, each node in the lattice has four successors and 

418 
OPTION PRICING BY BINOMIAL AND TRINOMIAL LATTICES 
we must also find four probabilities: puu, P u d ,  p d u ,  and p d d .  We first require 
a matching condition on the expected values of the increments 6Xi: 
E [ 6 X 1 ]  = (Puu + p u d ) 6 x 1  - ( p d u  + p d d ) d X l  = v1 bt 
E [ d X 2 ]  = (Puu + P d u ) & Z 2  - ( p u d  f P d d ) b x 2  = v2 bt, 
where we distinguish between random variables 6Xi and their realizations 
f 6 x i .  Then, we require a similar condition for second-order moments: 
E [ ( ~ X I ) ~ ]  
= (PUU + p u d  + p d u  + P d d ) ( b Z i ) 2  = Uf 6t + V;(6t)2 M Of 6t 
E [ ( ~ X L ? ) ~ ]  
= (PUU + p u d  + p d u  + p d d ) ( 6 X : 2 ) 2  = Ug 6t + V i ( 6 t ) 2  M Ug 6t, 
where we have used the usual identity Var(X) = E(X2] - E2[X] and we 
have neglected higher-order terms in 6t. These equations are immediately 
simplified, since probabilities must add up to 1: 
6 x 1  = O1&, 
6 x 2  = u,&. 
We should also account for covariance or, equivalently, for the cross product: 
E [ 6 X 1  . b X 2 ]  = (Puu - p u d  - p d u  + p d d )  6 x 1  6x2 
= p a l o 2  6t + v p 2 ( 6 t ) 2  M p u l a 2  6t. 
Now we have a system of four equations with four unknown probabilities: 
Puu - P u d  - p d u  + p d d  = p 
p u u + p u d + p d u + P d d =  
1. 
These equations may be solved by inverting the matrix numerically, or by 
taking suitable linear combinations of equations: 
1 -1 
-1 
1
1
 1
1
 
-1 
-1 
-1 
which yields: 

PRICING BlDlMENSlONAL OPTIONS BY BINOMIAL LATTICES 
419 
These conditions have an intuitive interpretation. The probability of having 
two up jumps is large when the two drifts are large (with respect to the 
corresponding volatilities) and when correlation is positive. In the probability 
of an up jump in S1 and a down jump in S2, the drift p2 occurs with a minus 
sign (the larger the drift, the less likely a down jump), and negative correlation 
makes this joint movement more likely. A similar consideration applies to pdu, 
whereas p d d  is smaller when drifts are large and is larger when correlation is 
positive. 
The implementation of this bidimensional lattice really requires careful 
memory management: We cannot simply store a large tridimensional matrix. 
Since up and down jumps in the two asset prices are the same in absolute value, 
we may exploit the same ideas we have used in section 7.1.3. The resulting 
code is displayed in figure 7.11 Input parameters are self-explanatory. First 
we compute invariant quantities. Note that in the lattice we work with prices, 
and not their logarithm. Hence, the up jumps are given by 
and d, = l/ui, i = 1,2. Probabilities are discounted outside the main loop. 
The values of the two underlying assets are stored in two vectors S l v a l s  and 
S2vals, which work exactly like their counterpart in the vanilla option on 
one asset. The price of the option is stored in a bidimensional matrix Cvals, 
which is initialized with the option payoff here subscript i refers to asset 
1, and j refers to asset 2. We can use one matrix for two consecutive time 
layers because odd- and even-numbered positions are alternatively used for 
consecutive time layers. Since the option is American, we compute the con- 
tinuation value hold as a risk-neutral expectation and we compare it against 
the intrinsic value. 
To check the implementation we use the following example3: 
>> s10 = 100; 
>> s20 = 100; 
>> K = 1; 
>> r = 0 . 0 6 ;  
>> sigmal = 0.2; 
>> sigma2 = 0.3; 
>> rho = 0.5; 
>> ql = 0.03; 
>> q2 = 0.04; 
>> AmSpreadLattice (S10 ,S20 ,K,r ,T, 
sigmal , sigma2,rho ,ql .q2,N) 
>> T = 1; 
>> N = 3 ;  
ans = 
10.0448 
3This is the same example used in (1, pp. 47-51]. 

420 
OPTION PRICING BY BINOMIAL AND TRINOMIAL LATTICES 
function price = AmSpreadLattice 610, 
S20 ,K ,r ,T, sigma1 , sigma2 ,rho ,ql, q2, N) 
1 Precompute invariant quantities 
deltaT = T/N; 
nu1 = r - ql - 0.5*sigmal-2; 
nu2 = r - q2 - 0.5*sigma2-2; 
ul = exp(sigmal*sqrt(deltaT)) ; 
dl = l / u l ;  
u2 = exp(sigma2*sqrt(deltaT)); 
d2 = l/u2; 
discount = exp(-r*deltaT) ; 
p-uu = discount*O.25*(1 + sqrt(deltaT)*(nul/sigmal + nu2/sigma2) + rho); 
p-ud = discount*O.25*(1 + sqrt(deltaT)*(nul/sigmal - nu2/sigma2) - rho); 
p-du = discount*0.25*(1 + sqrt(deltaT)*(-nul/sigmal + nu2/sigma2) - rho); 
p-dd = discount*O.25*(1 + sqrt(deltaT)*(-nul/sigmal - nu2/sigma2) + rho); 
% set up S values 
Slvals = zeros(2*N+l,l); 
S2vals = zeros(2*N+1,1) ; 
Slvals(1) = SlO*dl-N; 
S2vals(l) = S20*d2-N; 
for i=2:2*N+1 
Slvals(i) = ul*Slvals(i-l) ; 
S2vals(i) = u2*S2vals(i-l) ; 
end 
% set up terminal values 
Cvals = zeros(2*N+1,2*N+i); 
for i=1:2:2*N+1 
for j=1: 2 : 2*N+1 
end 
end 
% roll back 
for tau= 1 : N 
Cvals(i, j) = max(Slvals(i)-S2vals(j)-K,O); 
for i= (tau+l) :2: (2*N+l-tau) 
for j= (tau+l) :2: (2*N+l-tau) 
hold = p-uu * Cvals(i+l,j+l) + p-ud * Cvals(i+l,j-1) + ... 
p-du * Cvals(i-l,j+l) + p-dd * Cvals(i-1,j-1); 
Cvals(i,j) = max(ho1d. Slvals(i) - S2vals(j) - K); 
end 
end 
end 
price = Cvals(N+l,N+l); 
Fig. 7.11 
binomial lattice. 
MATLAB code for pricing an American spread option by a bidimensional 

PRlClNG BlDlMENSlONAL OPTIONS BY BINOMIAL LATTICES 
421 
Clearly, three steps are not enough to get an acceptable approximation, 
but we may use this toy example to understand how the matrix Cvals is 
managed to store the lattice, by checking what happens layer by layer. In 
MATLAB, this can be done by stepping with the debugger, and we display 
here the essential information we get. The initial lattice is the following; for 
clarity, we have used an asterisk * to spot irrelevant data (when displaying 
Cvals with the debugger you would see some number there): 
10.2473 
* 
0 
* 
0 
* 
0 
28.6198 
* 3.9982 
* 
0 
* 
0 
51.7652 
* 27.1436 
* 
0 
* 
0 
80.9233 
* 56.3017 
* 21.4873 
* 
0 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
After the first iteration, with one time step to maturity, the relevant data are 
* 
* 
* 
* 
* 
* 
* 
* 9.3123 
* 0.5653 
* 
0 
* 
* 28.2778 
* 5.3263 
* 
0 
* 
* 54.2561 
* 25.8626 
* 3.0381 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
Note that the new values are obtained as averages of four neighboring values 
which store data for the next time layer. Then, going back one step, we have 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 9.4563 
* 0.9635 
* 
* 28.1353 
* 6.7420 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
and the final result is, in the root of the lattice: 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 10.0448 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
We may see that we are working with a sort of recursive pyramidal structure, 
which suffers from a small but acceptable memory waste. 

422 
OPTION PRICING BY BINOMIAL AND TRINOMIAL LATTICES 
fig. 7.12 Siiigle-period trinomial lattice. 
7.4 
PRICING BY TRINOMIAL LATTICES 
Thc idea of a trinomial lattice arises quite naturally as a generalizat,ioii of 
1)inoniial lat,tices. Each node has three successors, corresponding to the price 
going up, down; or staying the same (this is just one possible choice, actually). 
The lattice is calibrated in such a way to allow for recombination and to 
match the first two moments of the underlying continuous random variables. 
The additional degrees of freedom may be used to improve convergence or 
to impose additional conditions. A situation in which this may be useful is 
pricing a barrier option; in such a case we may require that the barrier price 
is on the latt,ice. 
Here too it, is convenient to work with the equation describing the stochas- 
X ( t )  = logs@). Over a small time step bt we may move in thrce 
directions: corresponding to iiicreriients +bx, 0, or -62 in the logarithm of 
price: corresponding to multiplicative shocks on the price itself. The thrce 
alternatives occur with risk-neutral probabilities p,, p,,, and p d ,  respectively. 
The structure of the hranching is shown in figure 7.12. Given the usual equa- 
t,ioii 
dX = v dt + adW, 
wherc v = 7’ - a2/2, we writc the iiioment matching equations: 
E[6X] = P?~CSX + p,,O - p d 6 ~  
= v St 
E[(CSX)’] = ~ , , ( S X ) ~  
+ p7,0 + pd(6~)’ = 026t + v2(6t)’ 
ps + plrl + P d  = 1. 
Solving t,his systciii yiclds 
1 a26t + v2(bt)2 + ”) 
( 
1 a26t + V 2 ( b t ) 2  - EE) , 
P, - 
- - 
2 ( 
(bx)2 
b X  
( 6 5 ) 2  
62 
a2bt + v2(6t)2 
( b x y  
Pu = - 
2 
P7‘ = 1 - 
(7.7) 

PRlClNG BY TRINOMIAL LATTICES 
423 
Fig. 7.13 Full example of triiioinial lattice. 
where we see that an additional degree of freedom is left to choose Sx. In 
fact,, it, t.uriis out t,liat one ca.nnot choose bx and bt independently. A cominoii 
rille of t,liiinil) is d:r; = 3 6 .  This relationship will he appreciated when we 
tlral wit,h stahility of finite diffrrrnce schemes. We should also riot,e that) a. 
careless c:hoic~ may result in negative probabilities. As an example; consider 
pricing a Eiiropem call option on a no11 dividend paying stock with: 5’0 = 100; 
li = 100; 7‘ = 0.06, T = 1, and 0 = 0.3. If wc build a three-step lattice, with 
hx = 0.2: we get, the lat,t,ice in figure 7.13, where 
p,, = 0.3878, 
p , ,  = 0.2494, 
pd = 0.3628 
T\,IATI,AB code to accomplish calculations on a trinomial lattice is sliowii in 
figure 7.14. As usual, discountrd probabilitics are computed outsidc tlic iiiain 
f o r  loops. Therc is ,jiist oiie observation iieeded here: unlike binomial lattices, 
W(I niust store at, least, two consccuttive time layers of the latt,ice, since there 
is iio alteriiatiori lxtween odd- and even-indexed entries in the arrays. Hence, 
we iise a. two-column array, with 2N + 1 rows, where the roles of the colunins 
~ i i i i y  l x  Lbi~ow’’ 
or ”fiiturc.” Wc use increments modulo 2 to swap t,he roles 
of t,ht: two 1itYel.s: which are indexed by variables know and kthen, taking the 
values 1 aiitl 2 altcrnatively. Here is the computation for the previous lattice: 
>> S O = l O O ;  
>> K=100; 
>> r=0.06; 
>> T = l ;  
>> sigma=0.3; 
>> deltaX = 0.2; 
>> EuCallTrinomial(SO,K,r,T,sigma,N,deltaX) 
ans = 
>> N=3; 
14.6494 

424 
OPTION PRICING BY BINOMIAL AND TRINOMIAL LATTICES 
function price = EuCallTrinomial(SO,K,r,T,sigma,N,deltaX) 
% Precompute invariant quantities 
deltaT = T/N; 
nu = r - 0.5*sigma-2; 
discount = exp(-r*deltaT) ; 
p-u = discount*0.5*((sigma^2*deltaT+nu^2*deltaT-2)/deltaX^2 + ... 
nu*deltaT/deltaX) ; 
p-rn = discount*(l - (sigma^2*deltaT+nu^2*deltaT-2)/deltaX-2); 
p-d = discount*0.5*((sigma^2*deltaT+nu^2*deltaT^2)/deltaX^2 - ... 
% set up S values (at maturity) 
Svals = zeros(2*N+l, 1) ; 
Svals(1) = SO*exp(-N*deltaX); 
exp-dX = exp(de1taX); 
for j=2: 2*N+1 
Svals(j) = exp-dX*Svals(j-1) ; 
end 
% set up lattice and terminal values 
Cvals = zeros(2*N+1,2); 
t = mod(N,2)+1; 
for j=1:2*N+1 
end 
for t=N-1 : -1 : 0 ; 
nu*delt aT/delt ax) ; 
Cvals(j ,t) = rnax(Svals(j)-K,O); 
know = mod(t.2)+1; 
knext = mod(t+l,2)+1; 
for j = N-t+l:N+t+l 
Cvals(j ,know) = p-d*Cvals(j-l,knext)+p-m*Cvals(j,knext)+. . . 
p-u*Cvals(j+l,knext); 
end 
end 
price = Cvals(N+1,1); 
Fig. 7.14 MATLAB code for pricing a European call by a trinomial lattice. 

SUMMARY 
425 
We mentioned that proper choice of Sx is an issue here. Playing with numbers 
as follows we see that the rule of thumb Sx = a& 
does make sense: 
>> blspr ice (SO, K , r , T, sigma) 
ans = 
14.7171 
>> N=100; 
>> deltaX = 0.2; 
>> EuCallTrinomial(SO,K,r,T,sigma,N,delta)() 
ans = 
14.0715 
>> deltaX = 0.5; 
>> EuCallTrinomial(SO,K,r,T,sigma,N,deltaX) 
ans = 
10.9345 
>> deltaX = sigma*sqrt (T/N) ; 
>> EuCallTrinomial(SO,K,r,T,sigma,N,delta;[) 
ans = 
14.6869 
>> N=1000; 
>> deltaX = sigma*sqrt (T/N) ; 
>> EuCallTrinomial(SO,K,r,T,sigma,N,delt~) 
ans = 
14.7141 
7.5 
SUMMARY 
Binomial lattices are typically the first numerical method one meets when 
learning about option pricing, which is reasonable given the apparent sim- 
plicity of the approach. We have preferred to describe the approach at a 
later stage in order to place it within a more generic framework. Lattices are 
actually related to Monte Carlo and finite difference methods. 
With respect to Monte Carlo methods, binomial and trinomial lattice rep- 
resent a clever deterministic sampling based on moment matching; moment 
matching is one of the many variance reduction techniques which have been 
proposed over the years. An advantage of lattice techniques with respect to 
Monte Carlo simulation is computational speed, when the problem dimen- 
sionality is small. Lattice methods are not easily applied when complex path 
dependencies are built in the option. Clever techniques may be used and have 
been proposed, e.g., for lookback options, but they may suffer from poor con- 
vergence. Hence, for complex and/or high dimensional options, Monte Carlo 
simulation can well be the only practical approach. On the other side of the 
coin, lattice methods easily deal with early exercise features. 
Some authors regard explicit finite difference schemes as a generalization 
of trinomial lattices. In fact, this will be apparent in section 9.2.1, where 
we see that numerical instability in an explicit scheme is linked to a bad 

426 
OPTlON PRlClNG BY BlNOMlAL AND TRlNOMlAL LATTKES 
discretization, essentially leading to a trinomial lattice with negative proba- 
bilities. Hence, it may be argued that the additional flexibility of grids and 
the possibility to use implicit and accurate schemes may supersede lattice 
techniques. But actually, as we have already pointed out, this is sometimes 
a matter of taste. With good calibrations (we have just scratched the sur- 
face here), accurate pricing may be obtained by lattice techniques in many 
practical cases. 
We should also point out that we have worked under the idealized assump- 
tion of complete markets, deterministic volatility, etc. Furthermore, we have 
basically worked with the historical volatility, whereas we know that implied 
volatility is often considered as the relevant one. Lattice techniques have been 
proposed which are calibrated against market prices, resulting in the so-called 
implied lattices. We refer to the literature for more on this advanced topics, 
but we should keep in mind that the conceptual simplicity and the compu- 
tational efficiency of lattice methods may be extremely useful to generalize 
option pricing beyond the Black-Scholes framework. 
For further reading 
0 A very good source on lattice techniques is [l]. There you may also 
find a careful analysis of the relationship between finite differences and 
trinomial lattices. 
0 The classical reference [3] includes many variations on the basic tech- 
niques we have considered, including lattices for barrier and lookback 
options, adaptive node placement, etc. In the chapters on numerical 
methods you may also find the background on pricing options on stocks 
paying discrete dividends by binomial lattices. This is the basis of the 
implementation provided by the Financial toolbox function binprice. 
0 You may also consult [4], which also includes implied lattices and ideas 
for efficient implementations. 
0 If you want to dig deeply into the issue of implementing binomial lattices 
in MATLAB, you should have a look at [2]. 
REFERENCES 
1. L. Clewlow and C. Strickland. Implementing Derivatives Models. Wiley, 
Chichester, West Sussex, England, 1998. 
2. D.J. Higham. Nine Ways to Implement the Binomial Method for Option 
Valuation in MATLAB. SIAM Review, 44:661-677, 2002. 

REFERENCES 
427 
3. J.C. Hull. Options, Futures, and Other Derivatives (5th ed.). Prentice 
Hall, Upper Saddle River, NJ, 2003. 
4. G. Levy. Computational Finance. Numerical Methods for Pricing Finan- 
cial Instruments. Elsevier Butterworth-Heinemann, Oxford, 2004. 
5. D.G. Luenberger. Investment Science. Oxford University Press, New 
York, 1998. 

This Page Intentionally Left Blank

8 
Option Pricing by Monte 
Carlo Methods 
Monte Carlo simulation is an important tool in computational finance: It may 
be used to evaluate portfolio management rules, to price options, to simulate 
hedging strategies, and to estimate Value at Risk. Its main advantages are 
generality, relative ease of use, and flexibility. It may take stochastic volatil- 
ity and many complicating features of exotic options into account, and it 
lends itself to treating high-dimensional problems, where the lattice and PDE 
framework cannot be applied. The potential disadvantage of Monte Carlo 
simulation is its computational burden. An increasing number of replications 
is needed to refine the confidence interval of the estimates we are interested 
in. The problem may be partially solved by variance reduction techniques or 
by resorting to low-discrepancy sequences. The aim of this chapter is to illus- 
trate the application of these techniques to a few examples, including some 
path-dependent options. This chapter is a direct extension of chapter 4, where 
we dealt with Monte Carlo integration. It must be emphasized that even if 
we use the more appealing terms “simulation” or “sampling,”, Monte Carlo 
methods are conceptually a numerical integration tool. This must be kept in 
mind when applying low-discrepancy sequences rather than pseudo-random 
generators. 
When possible, we will compare the results of simulation with analytical 
formulas. Clearly, our aim in doing so is a purely didactic one. If you have to 
compute the area of a rectangular room, you just multiply the room length 
times the room width; you would never count how many times a standard 
tile fits the surface. However, you should learn first to use simulation in easy 
cases, where we may check the consistency of results; moreover, we will also 
429 

430 
OPTlON PRICING BY MONTE CARL0 METHODS 
see that simulating options for which analytical formulas are available may 
yield powerful control variates for variance reduction purposes. 
The starting point in the application of Monte Carlo simulation is sam- 
ple path generation, given a stochastic differential equation describing the 
dynamics of a price (or an interest rate). In section 8.1 we illustrate path 
generation for geometric Brownian motion; two hedging strategies are simu- 
lated as a concrete example, and we also deal with Brownian bridge, which is 
an alternative to simulating sample paths by going forward in time. Section 
8.2 deals with an exchange option, which is used as a simple illustration of 
how the approach can be extended to multidimensional processes. In section 
8.3 we consider an example of weakly path-dependent option, a down-and-out 
put option; we apply both conditional Monte Carlo and importance sampling 
to reduce variance. A strongly path-dependent option is dealt with in section 
8.4, where we show the application of control variates and low-discrepancy 
sequences to pricing an arithmetic average Asian option. We close the chap- 
ter by outlining the basic issues in estimating option sensitivities by Monte 
Carlo sampling; in section 8.5 we consider the simple case of the option A for 
a vanilla call. 
Another application of stochastic simulation to option pricing is given in 
section 10.4, which is dedicated to American options; the early exercise feature 
makes a straightforward simulation approach infeasible, and the problem must 
be cast within the framework of stochastic dynamic optimization. 
8.1 PATH GENERATION 
The starting point for the application of Monte Carlo methods to option 
pricing is the generation of sample paths of the underlying factors. In vanilla 
options, there is really no need for path generation, as we have seen in chapter 
4: only the price of the underlying asset at maturity is of concern. But if the 
option is path-dependent, we need the whole path or, at least, a sequence of 
values at given time instants. With geometric Brownian motion, we are facing 
a very lucky case. In fact, it must be understood that we have two potential 
sources of errors in path generation: 
sampling error, 
discretization error. 
Sampling error is due to random nature of Monte Carlo methods, and it can be 
mitigated using variance reduction strategies. To understand what discretiza- 
tion error is, let us consider how we can discretize a typical continuous-time 
model, i.e., an Ito stochastic differential equation: 
dSt = a(St, t )  d t  + b(St, t )  dWt. 

PATH GENERATION 
431 
The simplest discretization approach, known as Euler scheme, yields the fol- 
lowing discrete-time model: 
sst = St+st - s, = a(&, t)6t + b(St, t ) & E ,  
where 6t is the discretization step and E N N(0,l). This scheme is conceptu- 
ally linked to finite differences and its application to a deterministic differential 
equation would yield a truncation error, which is arguably negligible when the 
discretization step is small.’ Convergence is a critical concept in stochastic 
differential equations, as we are dealing with stochastic processes, but we 
may guess that, by sampling realizations of the random variable E from the 
standard normal distribution, we should be able to simulate a discrete-time 
stochastic process which is well related to the solution of the continuous-time 
equation. Increasing the number of sample paths, or replications, we should 
also be able to reduce sampling error. 
While the above reasoning can be justified more formally, we should realize 
that the discretization error may even change the probability distributions 
characterizing the solution. For instance, consider the geometric Brownian 
motion model: 
dSt = p&dt + OStdWt. 
(8.1) 
The Euler scheme yields 
St+st = (1 + pbt)St + O S t A E .  
This is very easy to grasp and to implement, but the marginal distribution 
of each value Si = S(i 6t) is normal, rather than lognormal. Actually, taking 
a very small 6t we may reduce the error, but this is time consuming. In 
this specific case, we may get rid of the discretization error altogether by a 
straightforward application of Ito’s lemma, but this is not true in general. 
With complicated stochastic differential equations, we may have to generate 
the whole sample path, even if we are only interested in values at maturity, 
just to reduce the discretization error. In such a case, it may be advisable to 
use the more refined discretization schemes available in the literature. 
8.1.1 Simulating geometric Brownian motion 
Using Ito’s lemma, we may transform (8.1) into the following form: 
We also recall that, using properties of the lognormal distribution2 and letting 
u = p - a2/2, 
we obtain: 
‘We have seen in chapter 5 that convergence of discretization schemes is not that trivial. 
2See appendix B. 

432 
OPTlON PRICING BY MONTE CARL0 METHODS 
E[log(S(~)/S(O))l = vt 
~ a r [ l o g ( ~ ( t ) / ~ ( ~ ) ) ]  
= a2t 
E[S(t)/S(O)] = ept 
(8.3) 
var[s(t)/s(o)l = e 2 ~ t ( e ~ z t  
- 1)- 
(8.4) 
Equation (8.2) is particularly useful as it can be integrated exactly, yielding: 
To simulate the path of the asset price over an interval (0, T ) ,  we must dis- 
cretize time with a time step St. From the last equation, and recalling the 
properties of the standard Wiener process (see section 2.5), we get 
where E N N(0,l) is a standard normal random variable. Based on equation 
(8.5), it is easy to generate sample paths for the asset price. 
A straightforward code to generate sample paths of asset prices following 
geometric Brownian motion is given in figure 8.1. The function AssetPaths 
yields a matrix of sample paths, where the replications are stored row by row 
and columns correspond to time instants. The first column contains the same 
value, the initial price, for all sample paths. We have to provide the function 
with the initial price SO, the drift mu, the volatility sigma, the time horizon T, 
the number of time steps NSteps, and the number of replications NRepl. Note 
that the function takes the drift parameter p as input and then it computes 
the parameter v. 
For instance, let us generate and plot three one-year sample paths for an 
asset with an initial price $50, drift 0.1, and volatility 0.3 (on a yearly basis), 
assuming that the time step is one day3: 
>> randn(’state’,O>; 
>> paths=AssetPaths(50,0.1,0.3,1,365,3>; 
>> plot(l:length(paths) ,paths(l, :)> 
>> hold on 
>> plot(l:length(paths) ,paths(2, : ) I  
>> hold on 
>> plot(l:length(paths) ,paths(3, :>> 
The result is plotted in figure 8.2. If you start the random number generator 
3We assume here that a year consists of 365 trading days. How to treat non-trading days 
is a bit controversial (see, e.g., [ll, pp. 251-2521). 

PATH GENERATlON 
433 
function SPaths=AssetPaths(SO,mu,sigma,T,NSteps,NRepl) 
SPaths = zeros(NRep1, l+NSteps); 
SPaths(:,l) = SO; 
dt = T/NSteps; 
nudt = (mu-0.5*sigma-2)*dt; 
sidt = sigma*sqrt(dt) ; 
for i=l:NRepl 
for j=1: NSteps 
end 
SPaths(i,j+l)=SPaths(i,j)*exp(nudt + sidt*randn); 
end 
Fig. 8.1 MATLAB code to generate asset price paths by Monte Carlo simulation. 
35 - 
30 - 
25 ' 
I 
0 
50 
100 
150 
2W 
250 
3W 
350 
400 
Fig. 8.2 Sample paths generated by Monte Carlo simulation. 

434 
OPT/ON PRlClNG BY MONTE CARL0 METHODS 
function SPaths=AssetPathsV(SO,mu,sigma,T,NSteps,NRepl) 
dt = T/NSteps; 
nudt = (mu-O.5*sigma^2)*dt; 
sidt = sigma*sqrt (dt) ; 
Increments = nudt + sidt*randn(NRepl, NSteps); 
LogPaths = cumsum( Clog(S0) *ones (NRepl, 1) 
SPaths = exp(LogPaths) ; 
Spaths(:,l) = SO; 
Increments] , 2) ; 
Fig. 8.3 Vectorized code to generate asset price paths. 
for standard normals randn with another seed state, you will get different 
results. 
The code in figure 8.1 is based on two nested for loops. Sometimes, effi- 
ciency can be achieved in MATLAB by vectorizing code. In order to vectorize 
the code, it is convenient to rewrite equation (8.5) as 
log St+& - log st = v 6t + a& 
6. 
We may generate the differences in the logarithm of the asset prices and 
then use the cumsum function with an optional parameter set to 2 in order 
to compute the cumulative sums over the rows (the default is summing over 
columns). The resulting function AssetPathsV is illustrated in figure 8.3. We 
should note that in the last line we write the initial asset price in the first 
column. To see why, check the following snapshot: 
>> format long 
>> exp(log(50)) 
ans = 
49.99999999999999 
It is better to avoid this error (which is apparently negligible, but see later). 
We may compare the two implementations in terms of speed: 
>> tic, paths=AssatPaths(50,0.1,0.3,1,~~~,1~~~);, 
toc 
Elapsed time is 0.029226 seconds. 
>> tic, paths=AssetPathsV(5010.1,0.31~,~~~,~~~~);, 
toc 
Elapsed time is 0.034177 seconds. 
In this case we do not see advantages in vectorizing code. We should keep 
in mind that the elapsed time returned by tic and toc is subject to some 
variability due to the background tasks carried out by the operating system, 
but when the first edition of this book was written, there was a striking 
advantage in vectorizing code. And, in fact, there are many situations in 
which this is true. The point is that improvements in hardware and in software 

PATH GENERATKIN 
435 
(in this case, MATLAB interpreter has been arguably improved) may make 
certain programming practices obsolete. Sometimes a fully vectorized code 
requires huge matrices, which do not fit the main memory of the computer. 
In such a case, using disk space as virtual memory may slow the execution. 
So we should be aware of all possible tricks of the trade, but an empirical 
efficiency check has the ultimate say in the matter. 
8.1.2 
Simulating hedging strategies 
Armed with a function to generate sample paths, we may try a first experiment 
in comparing hedging strategies for a vanilla European call option. We know 
from chapter 2 that the option price is essentially the cost of a delta-hedging 
strategy and that the continuous-time hedging strategy for the call option 
requires holding an amount A of the underlying asset. A simpler strategy is 
the stop-loss ~ t r a t e g y . ~  
The idea is that we should have a covered position 
(hold one share) when the option is in the money, and a naked position (hold 
no share) when it is out of the money. In practice, we could buy a share 
when the asset price goes above the strike price K ,  and we should sell it 
when it goes below. This strategy makes intuitive sense, but it is not that 
trivial to analyze in continuous time.5 Nevertheless, we may evaluate its 
performance in discrete time by Monte Carlo simulation. The problem with 
an implementation in discrete time is that we cannot really buy or sell at the 
strike price: We buy at a price larger than K ,  when we detect that the price 
went above that critical value, and we sell at a price which is slightly lower. So, 
even without considering transaction costs, that would affect delta-hedging as 
well, we see a potential trouble with the stop-loss strategy. 
A MATLAB function to estimate the average cost of a stop-loss strategy is 
given in figure 8.4. The function receives a matrix of sample Paths, possibly 
generated by function AssetPaths. Note that in this case, unlike option 
pricing, the real drift mu must be used in the simulation. In checking the 
code, we should note that the true number of steps (time intervals) is one 
less the number of columns in matrix Paths. If we need to buy shares of the 
underlying stock, we may need to borrow money, which should be taken into 
account. But, since we assume deterministic and constant interest rates, we 
will not account for borrowed money, since we can simply record cash flows 
from trading and discount them back to time t = 0, having precomputed 
discount factors in the vector DiscountFactors. We use a state variable 
Covered to detect when we cross the strike price going up or down. Since 
cash Aow is negative when we buy, and positive when we sell, the option 
“price” is evaluated as the average total discounted cash flow, with a change 
in sign. We should also pay attention to what happens at maturity: If the 
4See [ll, pp, 300-3021. 
5See 151. 

436 
OPTION PRICING BY MONTE CARL0 METHODS 
function P = StopLoss(SO,K,mu,sigma,r,T,Paths) 
[NRepl, NSteps] = size (Paths) ; 
NSteps = NSteps - 1; % true number of steps 
Cost = zeros(NRep1,l); 
dt = T/NSteps; 
DiscountFactors = exp(-r*(O:l:NSteps)*dt); 
for k=l:NRepl 
CashFlows = zeros (NSteps+l, 1) ; 
if (Paths(k,l) >= K) 
Covered = 1; 
CashFlows(1) = -Paths(k,l) ; 
else 
Covered = 0; 
end 
for t=2:NSteps+l 
if (Covered == 1) 8 (Paths(k,t) < K) 
% Sell 
Covered = 0; 
CashFlows(t) = Paths(k,t) ; 
% Buy 
Covered = 1; 
CashFlows(t) = -Paths(k,t); 
elseif (Covered == 0) & (Paths(k,t) > K) 
end 
end 
if Paths(k,NSteps + 1) >= K 
% Option is exercised 
CashFlows(NSteps + 1) = ... 
CashFlows(NSteps + 1) + K; 
end 
Cost(k) = -dot(DiscountFactors, CashFlows); 
end 
P = mean(Cost1; 
fig. 8.4 Evaluating the cost of a stop-loss hedging strategy. 
option is in the money, the option holder will exercise her right and we will 
also get the strike price, which should be included in the cash flows. 
Since we know that sometimes vectorizing code is beneficial, we also show 
a vectorized version of this code in figure 8.5. The main trick here is using a 
vector OldPrice, which is essentially a shifted copy of Paths to spot where 
the price crosses the critical level, going up or down. Times at which we go 
up are recorded in vector UpTimes, and there we have a negative cash flow; a 
similar consideration applies to DownTimes. 

PATH GENERATION 
437 
function P = StopLossV(SO,K,mu,sigma,r,T,Paths) 
[NRepl,NSteps] = size(Paths1; 
NSteps = NSteps - 1; 
Cost = zeros(NRep1,l); 
CashFlows = zeros(NRepl,NSteps+l); 
dt = T/NSteps; 
DiscountFactors = exp(-r*(O:l:NSteps)*dt); 
OldPrice = [zeros(NRepl,l), Paths(: ,l:NSteps)l; 
UpTimes = find(0ldPrice < K & Paths >= K); 
DownTimes = find(0ldPrice >= K 6 Paths < K); 
CashFlows (UpTimes) = -Paths (UpTimes) ; 
CashFlows(DownTimes) = Paths(DownTimes1; 
ExPaths = find(Paths(:,NSteps+l) >= K); 
CashFlows(ExPaths,NSteps+l) = CashFlows(ExPaths,NSteps+l) + K; 
Cost = -CashFlows*DiscountFactors’; 
P = mean(Cost1; 
Fig. 8.5 Vectorized code for the stop-loss hedging strategy. 
Now we may check if the two function are actually consistent, and if there 
is any advantage in vectorization: 
>> SO = 50; 
>> K = 50; 
>> mu = 0.1; 
>> sigma = 0.4; 
>> r = 0.05; 
>> T = 5/12; 
>> NRepl =100000; 
>> NSteps = 10; 
>> randn( ’state’ ,0) ; 
>> Paths=AssetPaths(SO,mu, sigma,T,NSteps,NRepl) ; 
>> tic, StopLoss(SO,K,mu,sigma,r,T,Paths), toc 
ans = 
5.5780 
Elapsed time is 3.100619 seconds. 
>> tic, StopLossV(SO,K,mu,sigma,r,T.Paths), toc 
ans = 
5.5780 
Elapsed time is 0.735455 seconds. 
Here, unlike asset path generation, we see an advantage from vectorization. 
We may also appreciate here why, with the vectorized function to generate 
asset paths, it may be important to assign the initial asset price correctly, as 
we did in the last line of the code in figure 8.3. In this case the option is at 

438 
OPTION PRICING BY MONTE CARL0 METHODS 
function P = DeltaHedging(SO,K,mu,sigma,r,T,Paths) 
[NRepl,NSteps] = size(Paths1; 
NSteps = NSteps - 1; 
Cost = zeros(NRepl.1); 
CashFlows = zeros(l,NSteps+l) ; 
dt = T/NSteps; 
DiscountFactors = exp(-r*(O:l:NSteps)*dt); 
for i=l:NRepl 
Path = Paths(i,:); 
Position = 0; 
Deltas = blsdelta(Path(1 :NSteps) ,K,r ,T-(0 :NSteps-1) *dt ,sigma) ; 
for j=l:NSteps; 
CashFlows(j) = (Position - Deltas(j))*Path(j); 
Position = Deltas (j 1 ; 
end 
if Path(NSteps+l) > K 
else 
end 
Cost(i) = -CashFlows*DiscountFactors’; 
CashFlows(NSteps+l) = K - (1-Position)*Path(NSteps+l); 
CashFlows(NSteps+l) = Position*Path(NSteps+l); 
end 
P = mean(Cost); 
Fig. 8.6 Evaluating the performance of delta-hedging. 
the money, and we always buy the stock initially; but if the initial stock price 
is 49.9999 we don’t do that, and an apparently negligible error has serious 
consequences in the analysis. 
Now we should compare the cost of the stop-loss strategy with the cost of 
delta-hedging, and with the theoretical option price. A code to estimate the 
average cost of delta-hedging is displayed in figure 8.6. The code is similar 
to the stop-loss strategy, but it is not vectorized. The only vectorization we 
have done is in calling blsdelta once to get the option A for each point on 
the sample path. Note that A must be computed using the current asset 
price and the current time to maturity; we use the blsdelta function of the 
Financial toolbox. The current Position in the stock is updated given the 
new A, generating cash flows which are discounted. 
Figure 8.7 displays a script to compare performances of the two hedging 
strategies. Running the script, we get the following: 
>> Hedgingscript 
true price = 4.732837 
cost of stop/loss (S) = 4.826756 
cost of delta-hedging = 4.736975 

PATH GENERATION 
439 
% HedgingScript.m 
SO = 50; 
K = 52; 
mu = 0.1; 
sigma = 0.4; 
r = 0.05; 
T = 5/12; 
NRepl =10000; 
NSteps = 10; 
1 
C = blsprice(SO,K,r,T, sigma); 
fprintf(1, ’%s %f\n’, ’true price = ’, C); 
% 
randn( ’state’ ,O) ; 
Paths=AssetPaths(SO,mu,sigma,T,NSteps.NRepl) ; 
SL = StopLossV(SO,K,mu,sigma,r,T,Paths); 
fprintf(1, ’cost of stop/loss (S) = %f\n’, SL); 
DC = DeltaHedging(SO,K,mu,sigma,r,T,Paths); 
fprintf(1, ’cost of delta-hedging = %f\n’, DC); 
% 
NSteps = 100; 
randn ( ’ state ’ , 0) ; 
Paths=AssetPaths(SO,mu,sigma,T,NSteps,NRepl); 
SL = StopLossV(S0, K ,mu, sigma, r, T,Paths) ; 
fprintf (1, ’cost of stop/loss (S) = %f\n’. SL); 
DC = DeltaHedging(SO,K,mu,sigma,r,T,Paths); 
fprintf(1, ’cost of delta-hedging = %f\n’, DC); 
fig. 8.7 A script to compare hedging strategies. 
cost of stop/loss (S) = 4.828571 
cost of delta-hedging = 4.735174 
where in the first pair of runs we use ten hedging steps and one hundred 
in the second pair. We see that the stop-loss strategy does not seem to 
converge to the true option price, unlike the cost of delta-hedging. Actually, 
the comparison should be made in different settings, and it should also involve 
the variability of the hedging cost. 
8.1.3 Brownian bridge 
In the previous sections we generated asset paths according to a natural pro- 
cess, which proceeds forward in time. Actually, the Wiener process enjoys 
some peculiar properties which allow us to generate the sample paths in a 

440 
OPTION PRICING BY MONTE CARL0 METHODS 
different way. Consider a time interval with left and right end points tl and 
t,, respectively, and an intermediate time instant s, such that tl < s < t,. 
In standard path generation, we would generate the Wiener process in the 
natural order: W(tl), W(s), and finally W(t,). Using the so-called Brown- 
ian bridge, we may generate W(s) conditional on the values w1 = W(tl) and 
w, = W(t,). It can be shown that W(s), conditional on those two values, is 
a normal variable with expected value 
(tr - s)w1+ (S - tl)wr 
tr - tl 
and variance 
This is a consequence of some properties of the conditional distribution of a 
multivariate normal distribution. We will not prove the formulas above,6 but 
they are fairly intuitive: The conditional expected value of W(s) is obtained 
by linear interpolation through w1 and w,; 
the variance is low near the two 
end points tl and t,, and is maximum in the middle of the interval. 
Using Brownian bridge, we may generate sample paths by a sort of bisection 
strategy. Given W(0) = 0, we sample W(T); 
then we sample W(T/2). Given 
W(0) and W(T/2) we sample W(T/4); given W(T/2) and W ( T )  we sample 
W(3T/4), etc. Actually, we may generate sample paths in any order we wish, 
with non-homogeneous time steps. One could wonder why this complicated 
construction could be useful. There are at least two reasons. 
1. It may help in using variance reduction by stratification. It is difficult to 
use stratification in multiple dimensions, but we may use stratification 
just on the terminal value of asset price, and maybe an intermediate 
point. Then we generate intermediate values using the bridge. 
2. The Brownian bridge construction is also useful when used in conjunc- 
tion with low-discrepancy sequences. We have seen in section 4.6 that 
application of simple low discrepancy sequences in high-dimensional do- 
mains may be difficult, because some dimensions are not well-covered. 
Using Brownian bridge, we may use high quality sequences to outline the 
paths of the Wiener process, by sampling points acting as milestones; 
then we can fill the trajectory using other sequences, or even Monte 
Carlo sampling. 
In figure 8.8 we illustrate a MATLAB function to generate paths of the stan- 
dard Wiener process using the Brownian bridge technique, but only in the 
specific case in which the time interval [O,T] is bisected (i.e., the number of 
‘See, e.g., [8, pp. 82-84] for a readable proof. 

PATH GENERATlON 
441 
intervals is a power of 2); the technique may be applied in more general set- 
tings. In this case, we may simplify the formulas above to sample W ( s ) ;  if we 
let 6t = tl - t,, we have 
w r + w l  
1 
W ( S )  = ~ 
+ z&Z, 
2 
where Z is a standard normal variable. The function receives the length T of 
the time interval and the number NSteps of sub-intervals in which it must be 
partitioned, and it returns a vector containing one sample path. Assume that 
the number of intervals is 8 (it must be a power of two). Then we must carry 
out 3 bisections. 
0 Given the initial condition W(t0) = 0, we must first sample W(t8), 
which means “jumping” over an interval of length T ,  which is TJump 
in the program. Since we store elements in a vector of nine elements 
(starting with index 1, and including W(t,)), we must jump eight places 
in this vector to store the new value. The number of places to jump is 
stored in IJump. 
0 Then we start the first for loop. In the first pass we must only sample 
W(t4), 
given W(t0) and W(t8). Given positions left = I and right = 
IJump + 1 we must generate a new value and store that value in position 
i = IJump/2 + I, which is 4+1 = 5 in this case. Here we generate only 
one value, and we divide both jumps by 2. 
0 In the second iteration we must sample W(t,), given W(t0) and W(t4), 
and W(ts), given W(t4) and W(t8). The nested loop will be executed 
twice, and indexes left, right, and i are incremented by 4. 
0 In the third and final iteration we generate the remaining four values. 
We urge the reader to step through the function using the debugger to verify 
the pattern we have just described. In figure 8.8 we also give a script to check 
that the marginal distributions of the stochastic process we generate are the 
correct ones. Expected values should be zero, and standard deviation should 
be the square root of time: 
>> CheckBridge 
m =  
sdev = 
0.0025 
0.0015 
0.0028 
0.0030 
0.5004 
0.7077 
0.8646 
0.9964 
ans = 
0.5000 
0.7071 
0.8660 
1.0000 
We see that, apart from sampling errors, the result looks correct. Given a way 
to generate standard Wiener process, it is easy to simulate geometric Brownian 
motion. The function is given in figure 8.9, and it uses a similar approach as 

442 
OPTlON PRICING BY MONTE CARL0 METHODS 
function WSamples = WienerBridge(T, NSteps) 
NBisections = log2 (NSteps) ; 
if round(NBisecti0ns) I= 
NBisections 
fprintf(’ERR0R in WienerBridge: NSteps must be a power of 2\n’); 
return 
end 
WSamples = zeros(NSteps+l,l); 
WSamples(1) = 0 ;  
WSamples(NSteps+l) = sqrt(T)*randn; 
TJump = T; 
IJump = NSteps; 
for 
end 
k=l:NBisections 
left = 1; 
i = IJump/2 + 1; 
right = IJump + 1; 
for j=l:2-(k-l) 
a = 0.5*(WSamples(left) 
+ WSamples(right)); 
b = 0.5*sqrt(TJump); 
WSamples(i) = a + b*randn; 
right = right + IJump; 
left = left + IJump; 
i = i + IJump; 
end 
IJump = IJump/2; 
TJump = TJump/2; 
% CheckBridge.m 
randn(’state’,O); 
NRepl = 100000; 
T = 1; 
NSteps = 4; 
WSamples = zeros(NRep1, l+NSteps) ; 
for i=l:NRepl 
end 
m = mean(WSamples(:,2:(1+NSteps))) 
sdev = sqrt(var(WSamples(:,2:(1+NSteps)))) 
sqrt((l:NSteps).*T/NSteps) 
WSamples(i,:) = WienerBridgecT, NSteps); 
fig. 8.8 Implementing and checking path generation for the standard Wiener process 
by a Brownian bridge. 

PRICING AN EXCHANGE OPTION 
443 
function SPaths = GBMBridge(S0, mu, sigma, T, NSteps, NRepl) 
if round(log2(NSteps)) -= log2(NSteps) 
fprintf(’ERR0R in GBMBridge: NSteps must be a power of 2\n’); 
return 
end 
dt = TINSteps; 
nudt = (mu-0.5*sigmam2)*dt; 
SPaths = zeros(NRep1, NSteps+l); 
for k=l:NRepl 
W = WienerBridge(T,NSteps); 
Increments = nudt + sigma*diff (W’) ; 
LogPath = cumsum( [log(SO) , Increments] ; 
SPaths(k,:) = exp(LogPath1; 
end 
Spaths(:,l) = SO; 
Fig. 8.9 Sampling geometric Brownian motion by a Brownian bridge 
the vectorized version AssetPathsV. One thing we should note is the use of the 
function diff to generate the vector of Increments in the logarithmic asset 
price. In fact, in standard Monte Carlo we generate the underlying Wiener 
process by successive increments; with the Brownian bridge construction we 
build directly the values of the process at different time instants, and we must 
use the function dif f to obtain the relative differences. In some sense, d i f  f 
works in the opposite way to cumsum, as shown by the following example: 
8.2 
PRICING AN EXCHANGE OPTION 
The purpose of this section is to show that Monte Carlo simulation may 
be easily adapted to multidimensional options. We will use a very simple 
example, so that we may compare our estimates against the exact value for 
illustration purposes. We want to price a European-style exchange option 
written on two assets whose price, under the risk neutral measure, is modeled 
as a bidimensional geometric Brownian motion: 
dU(t) = TU(t) dt + auU(t) dWU(t) 
dV(t) = TV(t) d t  + uvV(t) dWv(t), 

444 
OPTlON PRlClNG BY MONTE CARL0 METHODS 
function p = Exchange(VO,UO,sigmaV,sigmaU,rho,T,r) 
sigmahat = sqrt(sigmaU-2 + sigmaV-2 - 2*rho*sigmaU*sigmaV); 
dl = (log(VO/UO) + 0.5*T*sigmahat^2)/(sigmahat*sqrt(T)); 
d2 = dl - sigmahat*sqrt(T); 
p = VO*normcdf (dl) - UO*normcdf (d2) ; 
Fig. 8.10 Code to price an exchange option analytically. 
where the two Wiener processes have instantaneous correlation p. The option 
payoff at maturity T is max(VT -UT, 0). We see that this option is a particular 
case of a spread option, whose payoff depends on the difference between two 
asset prices (we considered an American spread option in section 7.3). It is 
called “exchange” because it allows us to exchange one asset for the other at 
maturity. For instance, if we hold asset U and one exchange option, the payoff 
at maturity will be 
UT + max( VT - UT , 0) = max( VT, UT). 
For this option, there is an analytical pricing formula which is a fairly straight- 
forward generalization of the Black-Scholes formula: 
8 = ~u;+uZ,-2puvurr 
The reason why we get this type of formula is that the payoff has a homo- 
geneous form, which allows to simplify the corresponding partial differential 
equation by considering the ratio V/U of the two prices7 MATLAB code 
implementing this formula is shown in figure 8.10. 
The only point we need to consider in order to apply Monte Carlo is how 
to generate sample paths for two correlated Wiener processes. We may ap- 
ply the same idea we have seen in section 4.3.4 for the multivariate normal 
distribution. We should find the Cholesky factor for the covariance matrix 
corresponding to two standard normal variables with correlation p: 
7See, e.g., [2, pp. 184-1881 for a proof. 

PRlClNG AN EXCHANGE OPTlON 
445 
function [p, ci] = ExchangeMC(V0 ,UO , sigmaV, sigmaU, rho, T, 
r, NRepl) 
epsl = randn(1,NRepl); 
eps2 = rho*epsl + sqrt(l-rho^2)*randn(l,NRepl); 
VT = VO*exp((r - 0.5*sigmaVA2)*T + sigmaV*sqrt(T)*epsl); 
UT = UO*exp((r - 0.5*sigmaU"2)*T + sigmaU*sqrt(T)*eps2); 
DiscPayoff = exp(-r*T)*max(VT-UT, 0) ; 
[p, s, ci] = normf it (Discpayof f 1 ; 
Fig. 8.11 Code to price an exchange option by Monte Carlo simulation. 
It may be verified by straightforward multiplication that I= = LL', where 
O
I
 
L =  [ 1 
P d W  
Hence, to simulate bidimensional correlated Wiener processes, we must gen- 
erate two independent standard normal variates 21 and 2 2  and use 
to drive path generation. 
In our case, we only need to generate joint samples of the two asset prices 
at maturity. The resulting MATLAB code is displayed in figure 8.11. We may 
check our results as usual: 
>> VO = 50; 
>> UO = 60; 
>> sigmaV = 0.3; 
>> sigmaU = 0.4; 
>> rho = 0.7; 
>> T = 5/12; 
>> r = 0.05; 
>> Exchange (VO ,UO, 
sigmav, sigmau, rho, T ,r) 
ans = 
>> NRepl = 200000; 
>> randn('state', 0 )  
>> [p,ci] = ExchangeMC(VO,UO,sigmaV,sigmaU,rho,T,r,NRepl) 
P =  
ci = 
0.8633 
0.8552 
0.8444 
0.8660 

446 
OPTION PRICING BY MONTE CARL0 METHODS 
% D0PutMC.m 
function [P,CI,NCrossed] = DOPutMC(SO,K,r,T,sigma,Sb,NSteps,NRepl) 
% Generate asset paths 
[Call,Putl = blsprice(SO,K,r,T,sigma); 
Payoff = zeros(NRep1,l); 
NCrossed = 0; 
for i=l:NRepl 
Path=AssetPaths (SO, r , sigma, T, NSteps ,1) ; 
crossed = any(Path <= Sb); 
if crossed == 0 
else 
Payoff(i) = max(0, K - Path(NSteps+l)); 
Payoff(i) = 0; 
NCrossed = NCrossed + 1; 
end 
end 
[P , aux, CI] = normf it ( exp (-r*T) * Payoff ) ; 
fig. 8.12 Crude Monte Carlo simulation for a discrete barrier option. 
8.3 PRICING A DOWN-AND-OUT P U T  OPTION 
In this section, we consider an example of weakly path-dependent option, 
i.e., a down-and-out put option, under the assumption that the barrier is 
checked at the end of each trading day. We have seen in section 2.7.1 how the 
analytical formula for continuous monitoring can be adjusted to reflect discrete 
monitoring; we will use the function DOPut to check the result of Monte Carlo 
simulation. An important point is that barrier options in practice may be 
very sensitive to stochastic volatility; Monte Carlo simulation could be used 
together with a model of stochastic volatility to price a barrier option. 
8.3.1 Crude Monte Carlo 
A code implementing crude Monte Carlo simulation is given in figure 8.12. 
The parameter NSteps is used to determine how many times the stock price 
should be checked against the barrier level sb. The payoff is set to 0 whenever 
the barrier is crossed. Note that we always simulate the complete path even if 
the barrier is crossed during the option life; some part of the path is actually 
useless, but doing so we can streamline code by using AssetPaths and the any 
vector operator. The DOPutMC function also returns the number NCrossed of 
paths in which the barrier has been crossed. 

PRICING A DOWN-AND-OUT PUT OPTION 
447 
Let us price an option with two months to maturity, assuming that each 
month consists of 30 days and that the barrier is checked each day. The barrier 
Sb is $40: 
>> DOPut(50,50,0.1,2/12,0.4,40*exp(-0.5826*0.4*sqrt~1/12/30~~~ 
ans = 
1.3629 
>> randn( seed ,O) 
>> [P,CI,NCrossed]=DOPutMC(50,50,0.1,2/12,0.4,40,60,50000~ 
P =  
CI = 
1.3600 
1.3393 
1.3808 
NCrossed = 
7392 
8.3.2 
Conditional Monte Carlo 
From section 4.5.1 we know that antithetic sampling may be not very effective 
in this case, because the payoff is nonmonotonic with respect to the asset price 
at expiration. Things are more complicated here, as the complete asset price 
path matters. Control variates may also be used; a natural candidate as a 
control variate is the price of a vanilla put, which may be computed by the 
Black-Scholes formula. However, the strength of the correlation between the 
two options is questionable. Hence, we try a different approach, i.e., variance 
reduction by conditioning, which was explained in section 4.5.4. To this end, 
we will see that is convenient to consider the price Pdi of the down-and-in 
put. Pricing this knock-in option is equivalent to pricing the corresponding 
knock-out option, since we know that 
Assume that we discretize the option life in time intervals of width bt (in our 
case, one day), so that T = Mbt, and consider the asset price path for days 
i ,  i = l ,  ..., M :  
s = {sly 
sz, . . . , S M } .  
Based on this path, we estimate the option price as 
Pdi = e-TTEII(S)(K - s ~ ) ' ] ,  
where the indicator function I is 
1 
0 otherwise. 
if Sj < Sb for some j 
I ( S )  = { 
Now let j *  be the index of the time instant at which the barrier is first crossed; 
by convention, let j *  = M + 1 if the barrier is not crossed during the option 

448 
OPTION PRICING BY MONTE CARL0 METHODS 
life. At time j * &  the option is activated, and from now on it behaves just like 
a vanilla put. So, conditional on the crossing time t* = j*bt and the price Sj. 
at which we detect barrier crossing,8 we may use the Black-Scholes formula 
to estimate the expected value of the payoff. Hence, if the barrier is crossed 
before maturity, we have 
where Bp(Sj*, 
K ,  T - t*) is the Black-Scholes price for a vanilla put with 
strike price K ,  initial underlying price Sj*, and time to maturity T - t*; 
the exponential term takes discounting into account, from maturity back to 
crossing time. Given a simulated path S, this suggests using the following 
estimator: 
I(S)e-Tt*Bp(Sj*, 
K ,  T - t*). 
Unlike antithetic sampling, conditional Monte Carlo exploits specific knowl- 
edge about the problem; the more we know, the less we leave to numerical 
integration. The function DOPutMCCond in figure 8.13 implements this vari- 
ance reduction method. The only point worth noting is that, for efficiency 
reasons, it is advisable to call the blsprice function only once with a vector 
argument, rather than once per replication. So, when the barrier is crossed, 
we record the time Times at which the down-and-in put has been activated, 
and the stock price StockVals. When the barrier is not crossed, the estimator 
is simply 0. Also note that the vectors passed to blsprice have NCrossed el- 
ements, whereas the size of the vector Payof f containing the estimator values 
is NRepl. 
>> DOPut(50,52,0.1,2/12,0.4,30*exp(-0.5826*0.4*sqrt(1/12/30))) 
ans = 
3.8645 
>> randn(’seed’,O) 
>> [P,CI,NCrossed] = DDPutMC(50,52,0.1,2/12,0.4,30,60,200000) 
P =  
CI = 
3.8751 
3.8545 
3.8957 
NCrossed = 
249 
>> randn(’seed’,O) 
>> [P,CI,NCrossed] = D0PutMCCond(50,52,0.1,2/12,0.4,30,60,200000~ 
P =  
CI = 
3.8651 
‘With continuous monitoring, we would immediately detect crossing when S(t*) = S,, but 
this is not the case with discrete monitoring. 

PRlClNG A DOWN-AND-OUT PUT OPTlON 
449 
% D0PutMCCond.m 
function [Pdo,CI,NCrossed] = ... 
dt = T/NSteps; 
[Call,Put] = blsprice(SO,K,r,T,sigma); 
% Generate asset paths and payoffs for the down and in option 
NCrossed = 0; 
Payoff = zeros(NRep1,l) ; 
Times = zeros(NRep1,l); 
StockVals = zeros(NRep1,l); 
for i=l:NRepl 
DOPutMCCond(SO,K,r,T,sigrna,Sb,NSteps,NRepl) 
Path=AssetPaths(SO,r,sigma,T,NSteps,l); 
tcrossed = min(find( Path <= Sb 1); 
if not (isempty(tcrossed)) 
NCrossed = NCrossed + 1; 
Times(NCrossed) = (tcrossed-1) * dt; 
StockVals(NCrossed) = Path(tcrossed); 
end 
end 
if (NCrossed > 0 )  
[Caux, Paux] = blsprice(StockVals(l:NCrossed),K,r, ... 
Payoff(1:NCrossed) = exp(-r*Times(l:NCrossed)) .* Paux; 
T-Times(1:NCrossed) ,sigma) ; 
end 
[Pdo, aux, CI] = normfit(Put - Payoff); 
Fig. 8.13 Conditional Monte Carlo simulation for a discrete barrier option. 

450 
OPTION PRICING BY MONTE CARL0 METHODS 
3.8617 
3.8684 
NCrossed = 
249 
8.3.3 
Importance sampling 
The last run shows that variance reduction by conditioning may indeed be 
helpful, but we should not get too excited. To begin with, one lucky run does 
not prove anything. Even worse, we have run a huge number of replications 
(200,000), but the barrier has been crossed only in 249 replications. This 
means that most of the replications are a wasted e f f ~ r t . ~  
In other words, with 
the data for this option, crossing the barrier is a rare event. This is a typical 
case in which importance sampling may help (see section 4.5.6). 
One possible idea is changing the drift of the asset price in such a way that 
crossing the barrier is more likely.'' We should go a step back and consider 
what we do in order to generate an asset price path S .  For each time step, 
we generate a normal variate Zj with expected value 
and variance IT' 6t. All these variates are mutually independent, and the asset 
price is generated by setting 
10gsj - logs,-1 = zj. 
Let Z be the vector of the normal variates, and let f(Z) be its joint density. 
If we use the modified expected value 
u - b, 
we may expect that the barrier will be crossed more often. Let g(Z) be the 
joint density for the normal variates generated with this modified expected 
value. Then we must find out a correction term, the likelihood ratio, to come 
up with the correct importance sampling estimator. Combining importance 
sampling with the conditional expectation we have just described, we have (if 
the barrier is crossed before maturity): 
'It can also be argued that in this case we are doing a good job only because the option 
price is slightly less than the Black-Scholes price, which we use in conditioning, because 
crossing the barrier is unlikely. 
"The treatment here follows the approach of [18]. 

PRlClNG A DOWN-AND-OUT PUT OPT/ON 
451 
In the expressions above, we should note the difference between z and 2; the 
first samples, given conditioning information, are actually numbers and are 
taken outside the expectation. In practice, we should generate the normal 
variates with expected value (v - b), and multiply the conditional estimator 
by the likelihood ratio, which from the sampling point of view is a random 
variable." The only open problem is how to compute the likelihood ratio. In 
appendix B we consider the joint distribution of a multivariate normal with 
expected value p and covariance matrix E: 
In our case, due to the mutual independence of the random variates Zj, the 
covariance matrix is a diagonal matrix with elements a' bt, and the vector of 
the expected values has components 
for the density f and p - b for the density g. So we have 
f(z1, . . . , zj * ) 
g ( z l , . . * , z j * )  
[-2(z1~ - p)b - b2] 
I) 
=exp{ -A 
[ - 2 b ~ z k + 2 j * p b - j * b 2  
j' 
k=l 
Readers with a background in stochastic calculus will recall that the Radon-Nikodym 
derivative is a random variable. 

452 
OPTION PRICING BY MONTE CARL0 METHODS 
=exp 
- c L k - -  
j * b  ( 
a2) 
j*b2 } 
a2 ‘-y +- 
. 
2a2 St 
k = l  
The resulting code is illustrated in figure 8.14. The function DOPutMCCondIS is 
similar to DOPutMCCond; the difference is that we must generate the asset price 
path and record the normal variates in vector vetZ, so that we may compute 
the likelihood ratio which is stored in the vector ISRatio. We compute the 
Black-Scholes price only at the end of the main loop. Finding the parameter 
b is a matter of trial and error. In the function DOPutMCCondIS we assume 
that the user provides a percentage bp, and the modified expected value is 
computed as 
(1 - bp)(r-0.5*sigmaA2)*dt 
Thus the parameter b is given as a percentage of the correct expected value. 
Note that we may use a value for bp which is larger than 1, to lower the drift 
rate at will. Now we may experiment a bit with importance sampling. 
>> randn(’seed’,O) 
>> [P,CI,NCrossed] 
P =  
CI = 
3.8698 
3.7778 
3.9618 
NCrossed = 
12 
>> randn(’seed’,O) 
>> [P,CI ,NCrossed] 
P =  
CI = 
3.8661 
3.8513 
3.8810 
NCrossed = 
12 
>> randn(’seed’,O) 
>> [P, CI , NCrossedl 
P -  
CI = 
3.8651 
3.8570 
3.8733 
NCrossed = 
43 
>> randn(’seed’,O) 
>> [P,CI,NCrossed] 
P =  
= DOPutMC(50,52,0.1,2/12,0.4,30,60,10000) 
= DOPutMCCond1S(50,52,0.1,2/12,0.4,30,60,10000,0~ 
= DOPutMCCond1S(50,52,0.1,2/12,0.4,30,60,10000,20) 
= DOPutMCCond1S(50,52,0.1,2/12,0.4,30,60,10000,50) 

PRlClNG A DOWN-AND-OUT PUT O f  T/ON 
453 
% DOPutMCCond1S.m 
function [Pdo,CI,NCrossed] = ... 
dt = T/NSteps; 
nudt = (r-0.5*sigma-2)*dt; 
b = bp*nudt; 
sidt = sigma*sqrt(dt); 
[Call,Put] = blsprice(SO,K,r,T,sigma); 
% Generate asset paths and payoffs for the down and in option 
NCrossed = 0; 
Payoff = zeros(NRep1,l); 
Times = zeros (NRepl ,I) ; 
StockVals = zeros(NRep1,l) ; 
ISRatio = zeros (NRepl ,1) ; 
for i=l :NRepl 
% generate normals 
vetZ = nudt - b + sidt*randn(l,NSteps); 
LogPath = cumsum( [log(SO), vet21 ; 
Path = exp(LogPath) ; 
jcrossed = min(find( Path <= Sb 1); 
if not (isempty(jcrossed)) 
DOPutMCCondIS(SO,K,r,T,sigma,Sb,NSteps,NRepl,bp) 
NCrossed = NCrossed + 1; 
TBreach = jcrossed - 1; 
Times(NCrossed) = TBreach * dt; 
StockVals(NCrossed) = Path(jcrossed1; 
ISRatio(NCrossed) = exp( TBreach*bA2/2/sigmaA2/dt +... 
b/sigma-2/dt*sum(vetZ(I:TBreach)) - ... 
TBreach*b/sigmaA2*(r - sigma-2/2)); 
end 
end 
if (NCrossed > 0) 
[Caux, Paux] = blsprice(StockVals(l:NCrossed),K,r, ... 
Payoff(1:NCrossed) = exp(-r*Times(l:NCrossed)) .* Paux ... 
T-Times (1 : NCrossed) ,sigma) ; 
.* ISRatio(1:NCrossed); 
end 
[Pdo, aux, CI] = normf it (Put - Payoff) ; 
Fig. 8.14 
rier option. 
Using conditional Monte Carlo and importance sampling for a discrete bar- 

454 
OPT/ON PRlClNG BY MONTE CARL0 METHODS 
3.8634 
3.8596 
3.8671 
NCrossed = 
225 
>> randn(’seed’,O) 
>> [P, CI , NCrossed] 
P =  
CI = 
CI = 
3.8637 
3.8629 
3.8645 
NCrossed = 
8469 
= D0PutMCCond1S(50,52,0.1,2/12,0.4,30,60,10000,200~ 
Calling DOPutMCCondIS with the parameter bp set to zero is just like calling 
DOPutMCCond; by increasing bp we see that the barrier is crossed in more and 
more replications, and the quality of the estimate is improved. Note that this 
does not necessarily imply that the larger b, the better; suggestions for setting 
this parameter are given in [IS]. 
8.4 
PRICING AN ARITHMETIC AVERAGE ASIAN OPTION 
We consider here pricing an Asian average rate call option with discrete arith- 
metic averaging. The option payoff is 
where the option maturity is T years, ti = a&, and 6t = TIN. For the sake 
of simplicity we assume that the contract prescribes taking sample prices at 
equally spaced time instants, but this need not be the case. In a crude Monte 
Carlo approach, we must simply generate asset price paths and average the 
discounted payoff as usual. The code is illustrated in figure 8.15; the only 
thing worth noting is that NSamples is the number N of sampled points 
to compute the arithmetic average, which should not be confused with the 
number of replications NRepl. In this case, we have to generate whole sample 
paths; we need samples only at the time instants specified by the contract, 
but we may still have to generate a large amount of data. This is why the 
code is not vectorized: to avoid trouble with possibly large matrices. In the 
following sections we consider variance reduction by control variates and use 
of low discrepancy sequences. 

PRICING AN ARITHMETIC AVERAGE ASIAN OPTION 
455 
function [P ,CI] = AsianMC(S0, K,r ,T,sigma,NSamples ,NRepl) 
Payoff = zeros(NRep1,l); 
for i=l:NRepl 
Path=AssetPaths (SO, r, sigma.T,NSamples, 1) ; 
Payoff (i) = max(0, mean(Path(2: (NSamples+l))) - K); 
end 
[P,aux,CI] = normfit( exp(-r*T) * Payoff); 
Fig. 8.15 Monte Carlo simulation for an Asian option. 
8.4.1 
Control variates 
This crude Monte Carlo sampling may be improved by using control variates. 
In this case, we have different possibilities. 
0 As a first control variate, we could use the sum of the asset prices12: 
N 
i =O 
This is a plausible control variate, because we are able to compute its 
expected value, and Y is clearly correlated to the option payoff. Note 
that the sum includes SO, which is not random at all; we could eliminate 
that from the sum, but we prefer not doing that just to ease the following 
notation. 
0 A second possibility would be using the vanilla call option, whose ana- 
lytical price is known. However, the option payoff of this control variate 
depends only on the price at maturity. 
0 A third, more sophisticated, control variate is the payoff of a geometric 
average option. This is also known analytically, and it looks much more 
promising than the vanilla call. 
We will illustrate the application of the first and the third idea. 
(under the risk-neutral measure): 
The expected value of the sum of the stock prices Y, 
as defined in (8.6), is 
N 
12This is the approach suggested in [17, chapter 91. 

456 
OPTION PRICING BY MONTE CARL0 METHODS 
function [P, CI] = AsianMCCV(S0, K ,r ,T, sigma,NSamples, 
NRepl , NPilot) 
% pilot replications to set control parameter 
TryPath=AssetPaths(SO,r,sigma,T,NSamples,NPilot); 
StockSum = sum(TryPath,2) ; 
PP = mean(TryPath( : ,2: (NSamples+l)) , 2) ; 
TryPayoff = exp(-r*T) * max(0, PP - K); 
MatCov = cov(StockSum, Trypayoff); 
c = - MatCov(l,2) / var(StockSum); 
dt = T / NSamples; 
ExpSum = SO * (1 - exp((NSamp1es + l)*r*dt)) / (1 - exp(r*dt)); 
% MC run 
ControlVars = zeros(NRep1,l) ; 
for i=l:NRepl 
StockPath = AssetPaths(SO,r, sigma,T,NSamples, 
1) ; 
Payoff = exp(-r*T) * max(0, mean(StockPath(2: (NSamples+l))) - K) ; 
ControlVars(i) = Payoff + c * (sum(StockPath) - ExpSum); 
end 
[P, aux, CI] = normf it (ControlVars) ; 
fig. 8.16 Monte Carlo simulation with control variates for an Asian option. 
where we have used the following formula: 
N 
CQi 
= - 
1-Q 
ffN+l* 
i=O 
The MATLAB code in figure 8.16 implements this variance reduction strategy. 
The user must fix the number of pilot replications NPilot, needed to set the 
control parameter c in the control variates procedure. The following runs give 
an idea of the improvement we may obtain: 
>> randn(’state’ ,O) 
[P,CI] = AsianMC(50,50,0.1,5/12,0.4,5,50000) 
P =  
CI = 
3.9939 
3.9418 
4.0460 
>> CI(2) - CI(1) 
ans = 
0.1042 
>> [P,CI] = AsianMCCV(50,50 ,O .1,5/12,0.4,5,45000,5000) 
P =  
CI = 
3.9562 

PRICING AN ARITHMETIC AVERAGE ASIAN OPTION 
457 
3.9336 
3.9789 
>> CI(2) - CI(1) 
ans = 
0.0453 
The alternative control variate is based on the exploitation of much deeper 
knowledge. The payoff of the discretetime, geometric average Asian option 
is 
Since the product of lognormal random variables is still lognormal, it is possi- 
ble to find an analytical formula for the price of the geometric average option, 
which looks like a modified Black-Scholes formula. We report the formula as 
given in [6, pp. 118-1191, where m is the last time at which we observed the 
price of the underlying asset, q is the continuous dividend yield, and Gt is the 
current geometric average: 
PGA = e-rT [ea+bbN(x) - K N  
where 
m 
N 
N 
a = - 
log(Gt) + ___ 
1
2
 
2 
u = r - 9 -  -a 
a - log(K) + b 
6 
X =  
The formula gets considerably simplified if we just consider the option price 
at its inception, i.e., at time t = 0. In such a case m = 0, and the resulting 
MATLAB implementation is illustrated in figure 8.17. 
Using the geometric average option as a control variate is fairly simple; 
we have to adapt the code in figure 8.16, obtaining the function displayed in 
figure 8.18. The figure also includes a script to compare crude Monte Carlo 
against the two control variates: 
>> CompareAsian 
P1 = 
CI1 = 
3.6276 
3.4814 
3.7738 

458 
OPTlON PRICING BY MONTE CARL0 METHODS 
function P = GeometricAsian (SO, K ,r ,T, sigma,delta,NSamples) 
dT = T/NSamples; 
nu = r - sigmaA2/2-de1ta; 
a = log(SO)+nu*dT+O.5*nu*(T-dT); 
b = sigma^2*dT + sigma^2*(T-dT)*(2*NSamples-l)/6/NSamples; 
x = (a-log(K)+b)/sqrt(b) ; 
P = exp(-r*T)*(exp(a+b/2)*normcdf (x) - K*normcdf (x-sqrt(b))) ; 
Fig. 8.1 7 MATLAB code for the analytical pricing formula of a geometric average 
Asian option. 
P2 = 
CI2 = 
3.4694 
3.3907 
3.5480 
3.4452 
3.4356 
3.4549 
P3 = 
C13 = 
The advantage of a control variate embodying sophisticated knowledge is 
pretty evident. 
8.4.2 
Using Halton sequences 
Another tool that we may use to improve pricing an Asian option is quasi- 
Monte Carlo simulation based on low-discrepancy sequences. We will use 
here Halton sequences to generate uniform “quasi-random” numbers and the 
inverse transform method to transform them to samples from the standard 
uniform distribution. This is just the simplest possibility, as we could use 
Sobol or other sequences, and maybe the Box-Muller transformation to gen- 
erate normal variates. 
The first issue to tackle is the generation of sample paths of geometric 
Brownian motion using Halton sequences. Say that we want to price an Asian 
option maturing in one year and we must sample price monthly. What is the 
dimension of the space over which we are integrating? We are integrating in 
a twelve-dimensional space, and we need a Halton sequence based on twelve 
Van der Corput sequences. It is very important to understand that each se- 
quence must be assigned to a time instant. Sequences are not associated to 
sample paths. By the way, should we use Box-Muller approach to transform 
uniform numbers to standard normal variates, we would need twice as much 
sequences. Also note that we cannot use rejection-based approaches to gen- 

PRKING AN ARITHMETIC AVERAGE ASIAN O f  TION 
459 
function [P,CI] = AsianMCGeoCV(SO,K,r,T,sigma,NSamples,NRepl,NPilot) 
% precompute quantities 
DF = exp(-r*T); 
GeoExact = GeometricAsian(SO,K,r ,T, 
sigma,O ,NSamples) ; 
GeoPrices = zeros(NPilot,l); 
AriPrices = zeros(NPilot,l); 
for i=l:NPilot 
pilot replications to set control parameter 
Path=AssetPaths(SO,r,sigma,T,NSamples,l) ; 
GeoPrices (i) =DF*max (0, (prod (Path (2 : (NSamples+l) ) ) ) (l/NSamples) - K) ; 
AriPrices (i)=DF*max(O,mean(Path(2 : (NSamples+l))) - K) ; 
end 
MatCov = cov(GeoPrices, AriPrices); 
c = - MatCov(l,2) / var(GeoPrices); 
% MC run 
ControlVars = zeros(NRep1,l); 
for i=l:NRepl 
Path = AssetPaths(SO,r, sigma,T, 
NSamples ,1) ; 
GeoPrice = DF*max(O, (prod(Path(2: (NSamples+l))))^(l/NSamples) - K) ; 
AriPrice = DF*max(O, mean(Path(2: (NSamples+l))) - K); 
ControlVars(i) = AriPrice + c * (GeoPrice - GeoExact); 
end 
[P, aux ,CI] = normf it (ControlVars) ; 
% C0mpareAsian.m 
randn ( ’ st ate ’ , 0) 
SO = 50; 
K = 55; 
r = 0.05; 
sigma = 0.4; 
T = 1; 
NSamples = 12; 
NRepl = 9000; 
NPilot = 1000; 
[Pl,CIl] = AsianMC(SO,K,r,T,sigma,NSamples,NRepl+NPilot) 
[P2,CI21 = AsianMCCV(SO,K,r,T,sigma,NSamples,NRepl,NPilot) 
[P3,CI3] = AsianMCGeoCV(SO,K,r,T,sigma,NSamples,NRepl,NPilot) 
Fig. 8.18 Using the geometric average Asian option as a control variate. 

460 
OPT/ON PRKING BY MONTE CARL0 METHODS 
function SPaths=HaltonPaths(SO,mu,sigma,T,NSteps,NRepl) 
dt = T/NSteps; 
nudt = (mu-O.5*sigma^2)*dt; 
sidt = sigma*sqrt(dt) ; 
1 Use inverse transform to generate standard normals 
NormMat = zeros(NRep1, NSteps); 
Bases = myprimes(NSteps) ; 
for i=l:NSteps 
H = GetHalton(NRepl,Bases(i)) ; 
RandMat ( : , i) = norminv (HI ; 
end 
Increments = nudt + sidt*RandMat; 
LogPaths = cumsum( [log(SO)*ones(NRepl, 1) , Increments] , 2) ; 
SPaths = exp(LogPaths1; 
SPaths(:,l) = SO; 
Fig. 8.19 Generating asset price paths by Halton sequences. 
function P = AsianHalton(SO,K,r,T,sigma,NSamples,NRepl) 
Payoff = zeros(NRep1,l); 
Path=HaltonPaths (SO ,r , sigma,T ,NSamples , NRepl) ; 
Payoff = max(0, mean(Path(: ,2: (NSamples+l)),2) - K); 
P = mean( exp(-r*T) * Payoff); 
Fig. 8.20 Pricing an Asian option by Halton sequences. 
erate variates, as in that case the dimension of the space is not well-defined. 
For each dimension, we need a prime number to be used as the basis. To gen- 
erate the first N prime numbers, we may use the myprimes function which is 
discussed in section A.3. The function HaltonPaths illustrated in figure 8.19 
is an extension of the vectorized function AssetPathsV to generate random 
sample paths. The idea is generating each column of matrix NormMat using 
one dimension of the Halton sequence, corresponding to one prime number. 
We see replications along the rows of the matrix, and each column corresponds 
to a time instant. Given this, we compute increments in the natural logarithm 
of the asset price, which are then cumulated and transformed to asset prices. 
Based on sample paths generated by HaltonPaths, it is very easy to write 
a function to price the arithmetic Asian option, as shown in figure 8.20. We 
may see the potential of low-discrepancy sequences from the following runs, 
in which we first compute a very accurate price using a large number of 
replications with crude Monte Carlo to have a reliable benchmark: 

PRICING AN ARITHMETIC AVERAGE ASIAN OPTION 
461 
>> randn(’state’,O) 
>> [P ,CI] = AsianMC(50,50,0.1,5/12 
,O. 4,5,500000) 
P =  
CI = 
3.9639 
3.9474 
3.9803 
>> AsianHalton(50,50,0.1,5/12 ,O. 4,5,1000) 
ans = 
>> AsianHalton(50,50,0.1,5/12 
,O. 4,5,3000) 
ans = 
>> AsianHalton(50,50,0.1,5/12 ,O. 4,5,10000) 
ans = 
>> AsianHalton(50,50,0.1,5/12 ,O. 4,5,50000) 
3.8450 
3.9103 
3.9461 
ans = 
3.9605 
We cannot associate a confidence interval to the estimate obtained by the 
quasi-random a p p r ~ a c h , ’ ~  
but we see that with a limited number of replica- 
tions we get an acceptable result. Here we have considered an option maturing 
in five months, with monthly sampling. Let us check what happens if we in- 
crease maturity to two years, with a corresponding increase in the number of 
monthly samples: 
>> randn( ’state’ ,0) 
>> [P ,CI] = AsianMC(50,50,0.1,2,0.4,24,500OOO) 
P =  
CI = 
8.3859 
8.3495 
8.4222 
>> AsianHalton(50,50,0.1,2,0.4,24,1000) 
ans = 
>> AsianHalton(50,50,0.1,2,0.4,24,5000) 
6.6219 
ans = 
7.9257 
>> AsianHalton(50,50,0.1,2,0.4,24,50000) 
ans = 
8.3424 
We see that in this case the performance of Halton sequences is much worse. 
This is due to the fact that we need 24 bases, which are large prime numbers, 
13The randomization of quasi-Monte Carlo scheme is one of the actively pursued research 
directions to get confidence bounds when using low discrepancy sequences. 

462 
OPTlON PRlClNG BY MONTE CARL0 METHODS 
and we have seen in section 4.6 that using large prime numbers yields poor 
results. We may expect that if the contract is characterized by more samples 
the situation will get even worse. 
One possible solution is using more sophisticated approaches, such as Sobol 
sequences. Another idea, is using the Brownian bridge construction. Using 
the Brownian bridge, we associate the "good" small bases to time instants 
acting as milestones. Large bases are used to fill the sample paths, but we 
may hope that this will not have a too detrimental effect. In what follows we 
use Brownian bridge with Halton sequences, for the sake of simplicity, but of 
course the same idea can be used with any low-discrepancy sequence. We also 
consider the possibility of using low-discrepancy sequences for milestone time 
instants, and pseudo-random numbers to fill the sample paths. 
The first step is simulating the standard Wiener process by Halton se- 
quences and the Brownian bridge. We extend function WienerBridge of fig- 
ure 8.8 to obtain the code in figure 8.21. The function WienerHaltonBridge 
differs from WienerBridge in a few basic features: 
0 It is partially vectorized, as it is convenient to generate all of the sample 
points on each time layer, in order to use Halton sequences in a more 
compact and readable way; the function returns a matrix, containing 
several replications, rather than only one. 
0 The matrix NormMat contains samples from standard normal distribu- 
tion, which are used just like in function HaltonPaths; each column is 
associated to one prime number and one time instant. 
0 The input arguments also include the number of replications NRepl and 
a parameter Limit; this is used to limit the number of dimensions of the 
Halton sequence which are used; note how the variable HUse is incre- 
mented within the main for loop to pick successive dimensions, associ- 
ated to increasingly large prime numbers; when HUse exceeds Limit, we 
switch to random sampling (just to fill sample paths which have been 
already outlined). 
Please note that our function is very limited, in that we can only use Brownian 
bridge when the number of time instants is a power of two. This is a limitation 
of our implementation, but not of the technique in itself. 
The second step is transforming the standard Wiener process to a geometric 
Brownian motion. The function GBMHaltonBridge of figure 8.22 works much 
like the function GBMBridge of figure 8.9. We should only note that it is 
vectorized and that this requires a different use of the diff function, which 
has to work horizontally on a matrix. In order to compute Increments, 
we call diff (W, 1,2) on the matrix W containing the paths of the standard 
Wiener process: The argument 1 means that we want to compute first-order 
differences, and the argument 2 means that we want to work along the rows of 
the matrix, whereas the default is along columns (just like mean or cumsum). 

PRICING AN ARITHMETIC AVERAGE ASIAN OPTION 
463 
function WSamples = WienerHaltonBridge(T, NSteps, NRepl, Limit) 
NBisections = log2(NSteps) ; 
if round(NBisecti0ns) -= NBisections 
fprintf(’ERR0R in WienerHB: NSteps must be a power of 2\n’); 
return 
end 
NormMat = zeros (NRepl , NSteps) ; 
Bases = myprimes (NSteps) ; 
for i=l:NSteps 
Generate standard normal samples 
H = GetHalton(NRepl,Bases(i)); 
NormMat ( : , i) = norrninv(H) ; 
end 
% Initialize extreme points of paths 
WSamples = zeros(NRepl,NSteps+l); 
WSamples(:,l) = 0; 
WSamples(:,NSteps+l) = sqrt(T)*NormMat(:,l); 
% Fill paths 
HUse = 2; 
TJump = T; 
IJump = NSteps; 
for k=l:NBisections 
left = 1; 
i = IJump/2 + 1; 
right = IJump + 1; 
for j=1: 2-(k-1) 
a = 0.5*(WSamples(: ,left) + WSamples(: ,right)); 
b = 0.5*sqrt(TJump); 
if HUse <= Limit; 
else 
end 
right = right + IJump; 
left = left + IJump; 
i = i + IJump; 
WSamples ( : , i) = a + b*NormMat ( : ,HUse) ; 
WSamples(:,i) = a + b*randn(NRepl,l); 
end 
IJump = IJump/2; 
TJump = TJump/2; 
HUse = HUse + 1; 
end 
fig. 8.21 
nian bridge. 
Siniulating the standard Wiener process by Halton sequences and the Brow- 

464 
OPTION PRlClNG BY MONTE CARL0 METHODS 
function Paths=GBMHaltonBridge(SO,mu,sigma,T,NSteps,NRepl,Limit) 
if round(log2(NSteps)) -= logZ(NSteps) 
fprintf(’ERFl0R in GBMBridge: NSteps must be a power of 2\n’); 
return 
end 
dt = T/NSteps; 
nudt = (mu-O.5*sigma-2)*dt; 
W = WienerHaltonBridge(T,NSteps,NRepl,Limit); 
Increments = nudt + sigma*diff(W,1,2); 
LogPath = cumsum( [log(SO) *ones(NRepl, 1) , Increments] , 2) ; 
Paths = exp(LogPath1; 
Paths(:,l) = SO; 
Fig. 8.22 Simulating geometric Brownian motion by Halton sequences and the Brow- 
nian bridge. 
Now we should pause a little and use our knowledge of geometric Brownian 
motion, represented by equations (8.3) and (8.4) to check if we do generate 
a process with the correct expected values and variances at different time 
instants. In particular, we may wish to check the relative error of the sample 
mean and sample variance of the process generated by Monte Carlo and Halton 
sequences, with and without the Brownian bridge, against the theoretically 
correct values. In order to do so, it is convenient to use the function of figure 
8.23. Given a matrix of sample paths, the function returns a two-column 
matrix; the first column contains, for each time instant (contained in vector 
Tvet), the relative percentage error in the mean, whereas the second column 
returns the error in variance. In the same figure we also provide the reader 
with a script to compare results. The script prints a table with six columns 
and sixteen rows. 
>> CheckHaltonScript 
ans = 
0.2510 
0.4838 
0.5893 
0.3609 
0.5580 
0.4847 
0.5960 
0.8787 
1.2209 
1.1240 
0.8548 
1.0240 
0.9923 
0.0269 
0.0701 
0.1042 
0.1651 
0.2644 
0.3787 
0.4814 
0.6607 
0.8061 
1.0044 
1.2322 
1.4891 
1.6941 
0.0927 
0.0983 
0.1685 
0.1235 
0.2351 
0.2251 
0.2826 
0.2053 
0.3353 
0.3299 
0.3945 
0.2976 
0.4268 
0.9473 
0.4045 
0.9765 
0.8147 
0.4233 
1.1434 
1.0490 
1.9696 
0.9005 
3.1095 
1.0232 
4.2511 
3.7522 
5.4619 
4.4059 
7.5672 
5.3788 
9.6047 
2.8125 
11.1005 
0.0401 
12.3976 
1.0730 
14.0780 
0.7693 
14.5632 
1.0480 
1.1005 
1.9098 
1.4138 
2.7626 
2.8336 
3.3645 
2.5914 
4.1374 
4.4781 
5.2199 
4.1875 
5.9899 

PRlClNG AN ARlTHMETlC AVERAGE ASIAN OPTlON 
465 
1.2271 
1.9678 
0.3922 
3.2472 
15.2210 
5.8546 
1.1193 
2.2621 
0.4274 
0.8804 
16.4125 
6.2836 
1.5650 
2.6552 
0.3018 
0.1313 
18.6872 
4.9231 
The first three columns give the relative errors in the estimate of expected 
value at each of the sixteen time instants, for Monte Carlo, Halton sequences 
without Brownian bridge, and Halton sequences with Brownian bridge, re- 
spectively. If we look at the second column, we see that the error tends to 
grow in time if we do not use the bridge; this makes sense, as we use large 
"bad" bases for later time intervals. If we compare the first and the third 
column, we see that the error with Halton sequences and the bridge com- 
pares favorably against the error with Monte Carlo. The last three columns 
display a similar pattern for variance, in the sense that there is a significant 
error that tends to increase over time if we use Halton sequences without the 
bridge. The error with Monte Carlo does not display a clear pattern. We 
may also see that Halton sequences with the bridge does not seem so superior 
to Monte Carlo in terms of matching variances. This is not that surprising 
given the simplicity of Halton sequences; nevertheless the reader is invited to 
verify that if we increase the number of sample paths we have a significant 
improvement. 
After all of this work, it is easy to write a function to price the arithmetic 
Asian option based on Halton sequences and the Brownian bridge. The code 
is illustrated in figure 8.24, and we may check the advantage over a straight- 
forward use of low-discrepancy sequences. To this purpose, we may use the 
script in figure 8.25. The idea here is 
1. to evaluate first the option price by plain Monte Carlo with a large 
number of replications (500,000); 
2. then to calculate the price with straightforward Halton sequences, on a 
limited number of replications (10,000); 
3. to check what we obtain with plain Monte Carlo with the small number 
of replications, repeating the procedure twenty times and collecting the 
average price and its standard deviation; 
4. to compare the two prices above with what we obtain using the Brown- 
ian bridge with different mixes of Halton and random sequences; when 
only Halton sequences are used, the experiment is not repeated and no 
standard deviation is reported, as there is no variability in that case. 
The result is the following (the script takes some time to execute): 
>> CompareAsiadl 
Extended MC 9.068486 
Halton 8.800511 
MC mean 9.135870 st .dev 0.135540 
HB (limit: 1) mean 9.074675 st.dev 0.077153 

466 
OPTlON PRICING BY MONTE CARL0 METHODS 
function PercErrors = CheckGBMPaths(S0, mu, sigma, T, Paths) ; 
[NRepl, NTimes] = size(Paths1; 
NSteps = NTimes-1; 
Tvet = (l:NSteps).*T/NSteps; 
SampleMean = mean(Paths(: ,2:NTimes)); 
TrueMean = SO * exp(mu*Tvet) ; 
RelErrorM = abs((Samp1eMean - TrueMean)./TrueMean); 
SampleVar = var(Paths(: ,2: (I+NSteps))); 
TrueVar = SO-2 * exp(2*mu*Tvet) .* (exp((sigma-2) * Tvet) - 1) ; 
RelErrorV = abs( (SampleVar - TrueVar) ./TrueVar) ; 
PercErrors = 100* [RelErrorM’ , RelErrorV’l ; 
X CheckHa1tonScript.m 
randn ( ’ state ’ , 0) 
NRepl = 10000; 
T = 5; 
NSteps = 16; 
Limit = NSteps; 
SO = 50; 
mu = 0.1; 
sigma = 0.4; 
Paths = AssetPaths(S0, mu, sigma, T, NSteps, NRepl); 
PercErrorsl = CheckGBMPaths(S0, mu, sigma, T, Paths) ; 
Paths = HaltonPaths(S0, mu, sigma, T, NSteps, NRepl); 
PercErrors2 = CheckGBMPaths(S0, mu, sigma, T. Paths) ; 
Paths = GBMHaltonBridge(S0, mu, sigma, T, NSteps, NRepl, Limit); 
PercErrors3 = CheckGBMPaths(S0, mu, sigma, T, Paths); 
[PercErrorsl(: ,1), PercErrors2(: ,I), PercErrors3(: ,1), . . . 
PercErrorsl(: ,2), PercErrors2(: ,2), PercErrors3(: ,211 
fig. 8.23 MATLAB function and script to evaluate sampling errors in the generation 
of geometric Brownian motion. 
function P = AsianHaltonBridge(SO,K,r,T,sigma,NSamples,NRepl.Limit) 
Payoff = zeros(NRep1,l); 
Path=GBMHaltonBridge(SO,r,sigma,T,NSamples,NRepl,Limit); 
Payoff = max(0, mean(Path(: ,2: (NSamples+l)) ,2) - K); 
P = mean( exp(-r*T) * Payoff); 
fig. 8.24 Pricing the arithmetic Asian option by Halton sequences and the Brownian 
bridge. 

PRICING AN ARITHMETIC AVERAGE ASIAN OPTlON 
467 
% C0mpareAsianH.m 
randn ( ’ state ’ , 0) 
SO = 50; 
K = 55; 
r = 0.05; 
sigma = 0.4; 
T = 4; 
NSamples = 16; 
NRepl = 500000; 
aux = AsianMC(S0 ,K,r,T,sigma,NSamples 
,NRepl) ; 
fprintf(1,’Extended MC %f\n), aux); 
NRepl = 10000; 
aux = AsianHalton( SO, K , r ,TI 
sigma, 
NSamples , NRepl) ; 
fprintf(1,’Halton %f\n’, aux); 
for i=1:20 
end 
fprintf(1,’MC mean %f st.dev %f\nJ, mean(aux), sqrt(var(aux))); 
Limit = 1; 
for i=1:20 
end 
fprintf(1,’HB (limit: %d) mean %f st.dev %f\n’, ... 
Limit = 2 ;  
for i=1:20 
end 
fprintf(1,’HB (limit: %d) mean %f st.dev %f\n’, ... 
Limit = 4; 
for i=1:20 
end 
fprintf(1,’HB (limit: %d) mean %f st.dev %f\nJ, ... 
Limit = 16; 
aux = AsianHaltonBridge (SO, K ,r ,T, 
sigma, 
NSamples ,NRepl ,Limit) ; 
fprintf(1,’HB (limit: %d) %f\n’, Limit, aux); 
aux(i) = AsianMC(SO,K,r,T,sigma,NSamples,NRepl); 
aux(i) = AsianHaltonBridge(SO,K,r,T,sigma,NSamples,NRepl,Limit); 
Limit, mean(aux), sqrt(var(aw))) 
; 
aux (i) = AsianHaltonBridge (SO, K, r ,T, 
sigma,NSamples, 
NRepl ,Limit) ; 
Limit, mean(aux), sqrt(var(aux1)) ; 
aux(i) = AsianHaltonBridge(SO,K,r,T,si~a,NSamples,NRepl,Limit); 
Limit, mean(aux), sqrt(var(aux))) 
; 
~~~ 
~ 
Fig. 8 25 Comparing Monte Carlo and Halton sequences with Brownian bridge. 

468 
OPTlON PRlClNG BY MONTE CARLO METHODS 
HB (limit: 2) mean 9.017819 st.dev 0.035962 
HB (limit: 4) mean 9.307306 st.dev 0.010279 
HB (limit: 16) 9.367783 
We see that straightforward use of Halton sequences does not give a satisfac- 
tory result and that Monte Carlo with few replications is fairly acceptable. 
We should note that since the payoff is defined by an average, there is much 
less variability than with the corresponding vanilla option depending only on 
price at maturity. Using an Halton sequence only for the terminal price of the 
underlying asset, filling the trajectory by Brownian bridge and random vari- 
ates yields good results with limited variability. Using more Halton sequences 
kills variability, of course, but it also tends to introduce a bias. In fact, using 
only Halton sequences with the Brownian bridge does not seem to work, and 
we overestimate the price. To understand why, we should carry out a more 
detailed analysis, which we do not report in detail, on the average price of the 
underlying asset generated by Halton sequences with the Brownian bridge. 
On the average, it is not too different from what we obtain by simple Monte 
Carlo sampling, but it is somewhat right-skewed which means that it tends 
to generate larger payoffs on the tail where the option is in-the-money. 
To summarize this section, we see that Halton sequences are not very sat- 
isfactory, and we should look for alternatives. Nevertheless, the idea of the 
Brownian bridge looks like tool one should keep in mind. The best results we 
have obtained in the last experiment are actually due to a sort of stratifica- 
tion effect on the terminal price, and Brownian bridge allows to exploit such 
a mechanism. 
8.5 
ESTIMATING GREEKS BY MONTE CARLO SAMPLING 
So far, we have only considered option pricing problems. However, estimating 
option sensitivities is another quite important task. We deal here with the 
estimation of A for a vanilla call, for the sake of simplicity. This section is 
linked to section 6.6, where we considered the interplay between simulation 
and optimization. We recall here the general framework. We have a function 
f(So), which in our case is the price of an option depending on the initial 
underlying asset price So, and the sensitivity we want to estimate is 
df(S0) 
f(S0 + 6So) - f (So) 
A = - 
= lim 
dSrJ 
6.90-o 
6SO 
Since we are estimating the option price by Monte Carlo simulation, the first 
approach coming to mind is to take sample paths and estimate A by the 
sample mean of finite differences between discounted payoffs. This approach 
can be implemented as illustrated in figure 8.26. 
However, this idea is too naive. To begin with, some care is needed, since 
what we are doing is swapping an expectation and a limit. In fact, what we 

ESTIMATING GREEKS BY MONTE CARL0 SAMPLING 
469 
function [Delta, CI] = BlsDeltaMCNaive(SO,K,r,T,sigma,dS,NRepl) 
nuT = (r - 0.5*sigma*2)*T; 
siT = sigma * sqrt(T) ; 
Payoff1 = max(0, SO*exp(nuT+siT*randn(NRepl,l))-K); 
Payoff2 = max(0, (SO+dS)*exp(nuT+siT*randn(NRepl.l))-K); 
SampleDiff = exp(-r*T)*(Payoff2 - Payoffl)/dS; 
[Delta, dummy, CI] = normf it (SampleDiff) ; 
fig. 8.26 Estimating the option A by crude Monte Carlo. 
are interested in is 
Eu[C(So + 6So,w>l - Eu[C(So,w)l 
lim 
Isso-0 
SSO 
1 
where C(S0,w) is the discounted payoff of the call with initial price SO, for a 
sample path corresponding to event w .  But what we are really computing is: 
Even if we accept the approximation of the limit by a finite difference, we 
should not take for granted that swapping the two operators is legal. To see 
a potential trouble intuitively, we should think that we are interested in the 
derivative of a function defined by an integral (the expected value). But the 
integral is a ‘‘smoothing” operator; hence, even if the function we integrate is 
not quite regular, the derivative of the integral may be no trouble. However, if 
we integrate the derivative, we may run into difficulties. In statistical terms, 
commuting the two operators may result in a biased e~timator.’~ 
Even if we disregard these subtle issues, it is easy to see that the function 
above is far from satisfactory. If we compare the estimate we get against the 
exact value provided by taking the derivative of the Black-Scholes formula, l5 
we see that the estimate is quite poor: 
>> S0=50; K=52; r=0.05; T=5/12; sigmal0.4; 
>> blsdelta(S0, K ,r , T, sigma) 
ans = 
0.5231 
>> randn( ’state’ ,O) 
>> NRepl=50000; 
>> dS = 0.5; 
I4See [B, chapter 71 for a full treatment. 
15The function blsdelta is available in the Financial Toolbox. 

470 
OPTION PRICING BY MONTE CARL0 METHODS 
function [Delta, CI] = BlsDeltaMCNaive(SO,K,r,T,sigma,dS,NRepl) 
nuT = (r - O.5*sigmae2)*T; 
siT = sigma * sqrt (T) ; 
Payoff1 = max(0, SO*exp(nuT+siT*randn(NRepl,l))-K); 
Payoff2 = max(0, (SO+dS)*exp(nuT+siT*randn(NRepl,l))-K); 
SampleDiff = exp(-r*T)*(Payoff2 - Payoffl)/dS; 
[Delta, dummy, CI] = normfit(Samp1eDiff) ; 
Fig. 8.27 Improving the estimate of the option A by Common Random Numbers. 
>> [Delta, CI] = BlsDeltaMCNaive (SO, K , r , T, sigma, dS , NRepl) 
Delta = 
CI = 
0.3588 
0.1447 
0.5729 
Actually, it is not too difficult to improve the estimator. From the theory of 
finite differences (section 5.2) we know that taking a central difference may 
be preferable: 
C(S0 + 6 S 0 , W )  - C(S0 - 6 S 0 , W )  
26690 
In our case, this may also reduce the effect of noise in our random sampling. 
Another point is that, to reduce variance, we may rely on common random 
numbers (section 4.5.2). In other words, we should use the same samples from 
the standard normal distribution when generating the two option payoffs. The 
related code is displayed in figure 8.27. We may verify that using these two 
tricks, we definitely improve the estimate of A: 
>> randn( 'state' ,O) 
>> [Delta, CI] = BlsDeltaMC(S0, K ,r ,T, sigma,dS ,NRepl) 
Delta = 
CI = 
0.5296 
0.5241 
0.5350 
We see that the least one should do to estimate option sensitivities is using 
central differences, when it makes sense, and using common random numbers. 
However, we see that if we are also interested in the option price, we basically 
have to repeat the same computations three times, for SO and SO f 
6690. The 
computational burden is actually larger, since we are typically interested in 
other sensitivities as well, and we have also to bother wondering about the 
right step 6690. It would be much nicer if we could just use one run to estimate 

ESTlMATlNG GREEKS BY MONTE CARL0 SAMPLING 
471 
both the option price and A. In fact, this may be done in many cases, if we 
analyze more carefully what we are doing.16 
Our discounted option payoff is a random variable 
c = ePrT max{ST - K, 01, 
where 
(r-u2 /2)T+uOZ 
ST = Soe 
and 2 is a standard normal variable. Using the chain rule for differentiation, 
we have 
The last derivative is easy: 
dST - ST 
_ _ -  
- 
dSo 
so ’ 
The first derivative is a bit more problematic, but we may see that 
0, i f x < K  
1, if x > K 
d - 
max{x - K, 0} = 
dx 
There is some trouble when x = K ,  as the function as a kink there. It 
turns out that, since this event has probability zero, this difficulty can be 
disregarded. Hence, we may conclude 
where I is the usual indicator function. Putting everything together, we obtain 
the following estimator of A: 
ST 
SO 
e-‘T-I{Sr 
> K }  
This type of estimator, because of the way it is built, is called pathwise es- 
timator. We should stress that this is not the only available approach, and 
that we have cut a few delicate corners in its explanation. However, the 
implementation is straightforward and is illustrated in figure 8.28. 
>> randn(’state’,O) 
>> [Delta, CI] = BlsDeltaMCPath(S0 ,K, r, TI 
sigma. NRepl) 
Delta = 
0.5297 
CI = 
0.5241 
0.5352 
“The treatment here follows [8, pp. 388-3891, 

472 
OPTlON PRlClNC BY MONTE CARL0 METHODS 
function [Delta, CI 1 = B1 sDe 1 t aMCPath (SO, K , r , T , sigma, NRepl 1 
nuT = (r - 0.5*sigma-2)*T; 
siT = sigma * sqrt (T) ; 
VLogn = exp(nuT+siT*randn(NRepl,l)); 
SampleDelta = exp(-r*T) .* VLogn .* (SO*VLogn > K); 
[Delta, dummy, CI] = normfit(SampleDe1ta); 
Fig. 8.28 Estimating the option A by a pathwise estimator. 
This snapshot shows that the estimator actually works. The careful reader 
will notice that in this run the true value falls outside the confidence interval; 
this may actually happen, because of the way confidence interval are built. 
The reader is urged to run the experiment a few times in order to check that 
the true value usually falls within the bounds of the confidence interval. 
For further reading 
In the literature 
Path generation and numerical solution of stochastic differential equa- 
tions are extensively treated in [14]. See also [lo] for an introduction 
including MATLAB code. 
The main reference for Monte Carlo methods in finance is [8]. You may 
also see [ 61 and [ 121. 
An early paper on using Monte Carlo simulation in option pricing is [3]. 
An updated survey is given in [4]. 
A nice collection of papers, gathered from the otherwise scattered liter- 
ature, is [7]. 
Interesting sources on the use of low-discrepancy sequences for deriva- 
tives pricing are [15] and [16]. See also [l] and [19] for specific issues 
such as path generation in high-dimensional problems and quantifying 
the estimation error. 
Another interesting paper on quasi-Monte Carlo simulation in finance is 
[ 131, where Faure low-discrepancy sequences, which we did not consider, 
are discussed. 
In this chapter we have only considered applications to option pricing. 
However, another important application field for Monte Carlo simulation 
is estimating Value at Risk. In [9], and related references, you may find 

REFERENCES 
473 
some information on the use of variance reduction methods to speed up 
VaR computations. 
On the Web 
a A Web page related to Monte Carlo and quasi-Monte Carlo methods is 
http://www.mcqmc.org. 
a Some information on using low-discrepancy sequences in finance can be 
also obtained by browsing the following pages: 
http://www.cs.columbia.edu/’traub 
http://www.cs.columbia.edu/”ap/html/info~ation.html 
REFERENCES 
1. F. Akesson and J.P. Lehoczky. Path Generation for Quasi-Monte Carlo 
Simulation of Mortgage-Backed Securities. Management Science, 46: 1171- 
1187, 2000. 
2. T. Bjork. Arbitrage Theory in Continuous Time (2nd ed.). Oxford Uni- 
versity Press, Oxford, 2004. 
3. P. Boyle. Options: A Monte Carlo Approach. Journal of Financial Eco- 
nomics, 4:323-338, 1977. 
4. P. Boyle, M. Broadie, and P. Glasserman. Monte Carlo Methods for 
Security Pricing. Journal of Economics Dynamics and Control, 21: 1267- 
1321. 1997. 
5 .  P.P. Carr and R.A. Jarrow. The Stop-Loss Start-Gain Paradox and Op- 
tion Valuation: a New Decomposition into Intrinsic and Time Value. The 
Review of Financial Studies, 3~469-492, 1990. 
6. L. Clewlow and C. Strickland. Implementing Derivatives Models. Wiley, 
Chichester, West Sussex, England, 1998. 
7. B. Dupire, editor. Monte Carlo. Methodologies and Applications for Pric- 
ing and Risk Management. Risk Books, London, 1998. 
8. P. Glasserman. Monte Carlo Methods in Financial Engineering. Springer- 
Verlag, New York, NY, 2004. 
9. P. Glasserman, P. Heidelberger, and P. Shahabuddin. Variance Reduction 
Techniques for Estimating Value-at-Risk. Management Science, 46:1349- 
1364, 2000. 

474 
OPTION PRICING BY MONTE CARL0 METHODS 
10. D.J. Higham. An Algorithmic Introduction to Numerical Simulation of 
Stochastic Differential Equations. SIAM Review, 43:525-546, 2001. 
11. J.C. Hull. Options, Futures, and Other Derivatives (5th ed.). Prentice 
Hall, Upper Saddle River, NJ, 2003. 
12. P. Jaeckel. Monte Carlo Methods in Finance. Wiley, Chichester, 2002. 
13. C. Joy, P.P. Boyle, and K.S. Tan. Quasi-Monte Carlo Methods in Numer- 
ical Finance. Management Science, 42:926-938, 1996. 
14. P.E. Kloeden and E. Platen. Numerical Solution of Stochastic Differential 
Equations. Springer-Verlag, Berlin, 1992. 
15. S.H. Paskov. New Methodologies for Valuing Derivatives. In S.R. Pliska 
and M.A.H. Dempster, editors, Mathematics of Derivative Securities, pages 
545-582. Cambridge University Press, Cambridge, 1997. 
16. S.H. Paskov and J.F. Traub. Faster Valuation of Financial Derivatives. 
Journal of Portfolio Management, 22:113-120, Fall 1995. 
17. S. Ross. A n  Introduction to Mathematical Finance: Options and Other 
Topics. Cambridge University Press, Cambridge, 1999. 
18. S.M. Ross and J.G. Shanthikumar. Monotonicity in Volatility and Effi- 
cient Simulation. Probability in the Engineering and Informational Sci- 
ences, 14:317-326, 2000. 
19. K.S. Tan and P.P. Boyle. Applications of Randomized Low Discrepancy 
Sequences to the Valuation of Complex Securities. Journal of Economic 
Dynamics and Control, 24:1747-1782, 2000. 

9 
~ 
~~ 
Option Pricing by Finite 
Difference Methods 
In this chapter we give a few simple examples of how the Partial Differential 
Equation (PDE) framework may be exploited in option pricing. The idea is 
applying the finite difference methods illustrated in chapter 5 to solve the 
Black-Scholes PDE. We start in section 9.1 by recalling derivatives approxi- 
mation schemes and by pointing out how suitable boundary conditions may 
be set up in order to model a specific option. In section 9.2 we apply a 
straightforward explicit scheme to the pricing of a vanilla European option; 
as we already know, this scheme is prone to numerical instabilities, which 
we may also interpret from a financial point of view. In section 9.3 we see 
how a fully implicit method may overcome the instability issue. The Crank- 
Nicolson method, which may be regarded as a hybrid between the explicit 
and the fully implicit approach, is applied in section 9.4 to a barrier option. 
Finally, in section 9.5 we see how iterative overrelaxation methods may be 
exploited to tackle an American option with a fully implicit method, which 
is not trivial due to the presence of a free boundary due to the possibility of 
early exercise. 
9.1 APPLYING FINITE DIFFERENCE METHODS TO THE 
BLACK-SCHOLES EQUATION 
We have shown in section 2.6.2 that the value at time t of an option written 
on an underlying asset whose price is S(t) is a function f(S, t )  satisfying the 
4 75 

476 
OPTION PRlClNG BY FINITE DIFFERENCE METHODS 
partial differential equation 
af 
af 
1 2 2d2f 
-+frS-+--a 
s - = r f ,  
at 
as 
2 
as2 
(9.1) 
with suitable boundary conditions that characterize the type of option. Dif- 
ferent equations may be written if the hypotheses are changed and if path 
dependency is introduced, but this equation is the starting point to learn how 
to apply numerical methods based on finite differences for option pricing. 
As we have seen in chapter 5 ,  to solve a PDE by finite difference methods 
we must set up a discrete grid, in this case with respect to time and asset 
prices. Let T be option maturity and S,, 
a suitably large asset price, that 
cannot be reached by S(t) within the time horizon we consider. We need S,,,, 
since the domain for the PDE is unbounded with respect to asset prices, but 
we must bound it in some way for computational purposes; S,, 
plays the 
role of $00. The grid consists of points (S, t) such that 
S = 0,6S, 2 65’7.. . , M 6 s  
Smax, 
t = 0,6t,26t,. .., N 6 t  G T. 
We will use the grid notation f i , j  = f (i bS, j 6t). 
tives in equation (9.1): 
Let us recall the different ways we have to approximate the partial deriva- 
a Forward difference: 
a Backward difference: 
a Central (or symmetric) difference: 
a As to the second derivative, we have 
Depending on which combination of schemes we use in discretizing the equa- 
tion, we end up with different approaches, explicit or implicit, which we ex- 
periment with in the following sections. 

APPLYING FINITE DIFFERENCE METHODS TO THE BLACK-SCHOLES EQUATION 
477 
Another issue, which we must take care of, is setting the boundary condi- 
tions. The terminal condition at expiration is 
f ( S , T )  =max{S- K,O} 
VS 
for a call with strike price K, and 
f (S, T )  = max{ K - S, 0) 
VS 
for a put. When we consider boundary conditions with respect to asset prices, 
the problem is not so trivial, since we have to solve the equation numerically 
on a bounded region, whereas the domain is unbounded with respect to asset 
prices. We may use a few examples to clarify this issue. 
Example 9.1 Let us consider first a vanilla European put option. When 
the asset price S(t) is very large, the option is worthless, since we may be 
(almost) sure that it will stay out-of-the-money: 
f (smax, t )  = 0. 
The value of S,,, 
must be relatively large for this boundary condition to 
work properly. When the asset price is S(t) = 0, we may say that, given 
our geometric Brownian motion model for asset dynamics, the asset price will 
remain zero. So the payoff at expiration will be K; discounting back to time 
t, we have 
f (0, t) = Ke-'(T-t). 
In grid notation: 
fi,N = max[K - iSS,O], 
f0,j = Ke- 
i = 0,1,. . . , M  
, 
j = O , l ,  ..., N 
r ( N - j ) a t  
fM,j = 0, 
j = 0, 1,. . . , N. 
0 
Example 9.2 We may deal with a vanilla European call by reasoning as in 
example 9.1. When the asset price is S(t) = 0, at any time t, the option will 
expire worthless: 
For a large asset price S(t), we may be sure that it will be in-the-money at 
expiration and we will get a payoff S(T) - K. The value at time t requires 
discounting back the term K and considering that the arbitrage-free price 
at time t for the underlying asset is simply S(t). Then a suitable boundary 
condition is 
f (S,,,, 
t )  = S,,, - Ke-'(T-t). 
f (0, t )  = 0. 
In grid notation: 
f i , N  = max[iSS - K,O], 
f o , j = o ,  
j = o , 1 ,  ..., N 
f M , j  = M dS - Ke-'(N-j)6t , 
i = 0,1,. . ., M 
j = O , l , . . . ,  N .  

478 
OPTION PRICING BY FINITE DIFFERENCE METHODS 
An alternative boundary condition for large values of S would be requir- 
ing that the option A is 1; in such a case we have a boundary condition 
on the derivative of the unknown function, rather than the function itself. 
This is called a Neumann boundary condition and is common in mathemat- 
ical physics. We will not pursue this approach, because it complicates the 
numerical solution a bit. 
0 
When dealing with barrier options, things may be easier. In the case of 
a knock-out option, such as a down-and-out put, the option value is 0 on 
the barrier. The case of an up-and-out call is similar, with the additional 
advantage that the domain we must consider is naturally bounded. American 
options are more complex to deal with because of the early exercise boundary; 
we should take into account for which asset prices and at which times (if any) 
it is optimal to exercise the option. Thus we have a free boundary that must 
be discovered in the solution process. A variety of boundary conditions must 
be required for exotic options; figuring out the correct boundary conditions 
and approximating them within the numerical scheme is an option-dependent 
issue. 
9.2 
PRICING A VANILLA EUROPEAN OPTION BY AN EXPLICIT 
METHOD 
As a first attempt to solve equation (9.1), let us consider a vanilla European 
put option. We approximate the derivative with respect to S by a central 
difference and the derivative with respect to time by a backward difference. 
This is not the only possibility, but any choice must be somehow compatible 
with the boundary conditions. The result is the following set of equations: 
to be solved with the boundary conditions of example 9.1. It should be noted 
that, since we have a set of terminal conditions, the equations must be solved 
backward in time. Let j = N in equation (9.2); given the terminal condition, 
we have one unknown quantity, f i , N - l ,  expressed as a function of three known 
quantities. If we imagine going backward in time the same consideration holds 
for each time layer. Rewriting the equations, we get an explicit scheme: 
f , .  
a,j-1 -
*
 
- ai fi-1,j + bj*fi,j + cj*.fi+l,j 
j ~ N - 1 , N - 2 , . . . , 1 , 0 ~  
i = 1 , 2  ,..., M-1, 
(9.3) 
where 
1 
2 
a: 
= -6t(a2i2 -Ti) 

PRlClNG A VANlLLA EUROPEAN OPTlON BY AN EXPLlClT METHOD 
479 
function price = EuPutExpl (SO ,K, r, T, 
sigma, Smax. dS , dt) 
% set up grid and adjust increments if necessary 
M = round(Smax/dS); 
dS = Smax/M; 
N = round(T/dt) ; 
dt = T/N; 
matval = zeros(M+l,N+l); 
vets = linspace(O,Smax,M+l)’; 
veti = 0:M; 
vetj = 0:N; 
% set up boundary conditions 
matval(:,N+l) = max(K-vetS,O); 
matval(1, : 
matval(M+l,:) = 0; 
% set up coefficients 
a = 0.5*dt*(signa-2*veti - r).*veti; 
b = 1- dt*(signa^2*veti.-2 + r); 
c = 0.5*dt*(sigma-2*veti + r).*veti; 
% solve backward in time 
for j=N: -1 : 1 
f o r  i=2:M 
= K*exp(-r*dt*(N-vetj) 1 ; 
matval(i,j) = a(i)*matval(i-l,j+l) 
+ b(i)*matval(i, j+l)+ . . . 
c(i)*matval(i+l,j+l); 
end 
end 
% return price, possibly by linear interpolation outside the grid 
price = interpl(vetS, matval(:,l), SO); 
Fig. 9.1 
scheme. 
MATLAB code to price a European vanilla put by a straightforwardexplicit 
bf 
= 1 - bt(a2i2 + T )  
1 
2 
c: 
= -6t(o2i2 + Ti). 
This scheme is rather straightforward to implement in MATLAB. The code 
is illustrated in figure 9.1, and it requires the value S,,, 
as well as the two 
discretization steps. The only point requiring some care is that in the math- 
ematical notation it is convenient to uses indexes starting from 0, whereas 
matrix indexes start from 1 in MATLAB. Moreover, if the initial asset price 
does not lie on the grid, we must interpolate between the two neighboring 
points. We have used here a crude linear interpolation; more sophisticated 
splines could be a better alternative, especially if we are interested in approx- 
imating option price sensitivities (as it is always the case in practice). 
>> [c,p] = blsprice(50.50.0.1,5/12,0.4); 

480 
OPT/ON PRlClNG BY FlNlTE D/FF€R€NCE METHODS 
(a) 
(b) 
Fig 9.2 View of explicit (a) aiitl implicit (h) schemes to solve the Black-Scholes PDE. 
>’ P 
P =  
>> EuPutExpl(50,5OI0.1,5/12 
,O .4,100,2,5/1200) 
ans = 
>> [ c  ,p] = blsprice (50,50,0.1,5/12 
,O. 3) ; 
>> P 
P =  
>> EuPutExp1(50,50,0.1,5/12,0.3,100,2,5/1200~ 
4.0760 
4.0669 
2.8446 
ans = 
2.8288 
We see that the numerical method gives fairly accurate results. We might try 
to improve them by using a finer grid. 
>> EuPutExp1(50,50,0.1,5/12,0.3,100,1.5,5/1200~ 
ans = 
2.8597 
>> EuPutExp11(50,50,0.1,5/12,0.3,100,1,5/1200~ 
ans = 
-2.8271e+022 
What we see here is another example of the numerical instability that we 
have analyzed in chapter 5. One possibility to avoid the trouble is to resort 
t80 implicit methods. Another one is to carry out a stability analysis and to 
derive honnds on the discretization steps. We will not pursue the second way 
here, which would be quite similar to what we have done in chapter 5 for the 
simpler transport and heat equations. Rather, in the next section we describe 
a financial interpretation of instability, which suggests still another possibility: 
rewriting the equation with a change of variables. 

PRICING A VANILLA EUROPEAN OPTION BY AN EXPLICIT METHOD 
481 
9.2.1 
In the explicit scheme, we obtain an option value f (S, t )  as a combination of 
the values f ( S  +6S, 
t + 6t), f (S, t +6t), and f(S -bS, t +bt). This looks a bit 
like a trinomial lattice method, which we have described in section 7.4 (see 
figure 9.2a). We can make this interpretation clearer by deriving an alternative 
version of the explicit method. Following [l, chapter 181, we assume that the 
first- and second-order derivatives with respect to S at point ( i , j )  are equal 
to those at point ( i , j  + 1): 
Financial interpretation of the instability of the explicit method 
af - fi+l,j+l - fZ-l,j+l 
-
_
 
dS 
265 
An alternative way to obtain the same scheme is substituting the right-hand 
term f i , j  in equation (9.2) by f1,j-l. This introduces an error which is bounded 
and tends to zero as the grid is refined.' 
The finite difference equation is now 
which may be rewritten (for i = 1,2,. . ., M - 1 and j = 0, 1, . . ., N - 1) as 
f .  . - 
2 , J  - k f - l , j + l  + i, f,,j+l + 2.1 fa+l,j+l, 
where 
Ea 
= --(-r26t+-02i26t 
1 
1 .  
1 
=- 
1 
1 + r 6 t  
2 
2 
) 
l + r 6 t T u .  
This scheme is again explicit and is subject to numerical instabilities as well. 
However, the coefficients 61, iZ, 
and 2.1 lend themselves to a nice interpretation. 
Recall that, in a binomial or a trinomial lattice, we obtain an option value 
in a node as the discounted expected value of the values in the successor 
nodes, where expectation is taken with respect to a risk-neutral probability 
measure. In fact, the coefficients above include a 1 / ( 1  + r 6 t )  term, which 
'A similar line of reasoning was used when deriving the AD1 method in section 5.4. 

482 
OPT/ON PRlClNG BY FINITE DIFFERENCE METHODS 
may be interpreted as a discount factor over a time interval of length 6t. 
Furthermore, we have 
‘7rd +TO +nu = 1. 
This suggests interpreting the coefficients as probabilities, times a discount 
factor. Are they risk-neutral probabilities? We should first check the expected 
value of the increase in the asset price during the time interval 6t: 
which is exactly what we would expect in a risk-neutral world. As to the 
variance of the increment, we have 
Hence, for small 6t 
Var[A] = E[A2] - E2[A] = a2S2 bt - r2S2(bt)2 M n2S2 6t, 
which is also coherent with geometric Brownian motion in a risk-neutral world. 
Thus we see that indeed the explicit method could be regarded as a trinomial 
lattice approach, except for a little problem. The “probabilities” 7?d and r o  
may be negative. The careful reader will see a recurring pattern, since in 
chapter 5 we have already met stability conditions linked to the coefficients 
of a linear combination; in both transport and heat equations, we must make 
sure that this combination is convex, i.e., that the coefficients are positive and 
sum up to one, just like a discrete probability distribution. 
One possibility to avoid the trouble, described in [l], is to change variables. 
By rewriting the Black-Scholes equation in terms of 2 = Ins, simple condi- 
tions for stability may be derived. However, a change of variables may not 
be a good idea for certain exotic options. In the next section we implement a 
fully implicit approach that avoids the stability issue altogether. 
9.3 PRICING A VANILLA EUROPEAN OPTION BY A FULLY 
IMPLICIT METHOD 
To overcome the stability issues of the explicit method, we may resort to an 
implicit method. This is obtained by using a forward difference to approxi- 
mate the partial derivative with respect to time. We get the grid equations 

PRlClNG A VANILLA EUROPEAN OPTION BY A FULLY IMPLICIT METHOD 
483 
- 
f l j  
f 2 j  
f33 
f M - 2 , j  
f M - 1 , j  
which we may rewrite (for i = 1,2,. . . , M - 1 and j = 0,1,. . . , N - 1) as 
- 
alfo,j 
0 
0 
0 
c M - l f M , j  - 
where, for each i, 
1 .  
1 
2 
2 
--ri 6t - -a2i2 
6t. 
ai 
= -rz6t - -a2i26t 
b, 
= 1+a2i’6t+r6t 
c, = 
1 
1 
2 
2 
Here we have three unknown values linked to one known value (see figure 
9.2b). First note that, for each time layer, we have M - 1 equations in A4 - 1 
unknowns; the boundary conditions yield the two missing values for each time 
layer and the terminal conditions give the values in the last time layer. As in 
the explicit case, we must go backward in time, solving a sequence of systems 
of linear equations for j = N - 1,. . . , O  . The system for time layer j is the 
following: 
fl,j+l 
f2,j+l 
f3,jfl 
f M - Z , j + l  
f M - l , j + l  
We may note that the matrix is tridiagonal and that it is constant for each 
time layer i. So we may speed up the computation by resorting to a LU- 
factorization.’ All of this is accomplished by the MATLAB code in figure 
9.3. 
>> [c,pl = blsprice(50,50,0.1,5/12,0.4); 
>> P 
P =  
2Due to the sparse structure of the matrix, it would be much better to write a specific 
code to solve the sequence of linear systems. Here we use just the ready-to-use MATLAB 
functionalities. 

484 
OPTION PRICING BY FINITE DIFFERENCE METHODS 
function price = EuPutImpl(SO,K.r,T,sigma,Smax,dS,dt) 
2 set up grid and adjust increments if necessary 
M = round(Smax/dS); 
dS = Smax/M; 
N = round(T/dt) ; 
dt = T/N; 
matval = zeros(M+l ,N+1) ; 
vets = linspace(O,Smax,M+l) ’; 
veti = 0:M; 
vetj = 0:N; 
% set up boundary conditions 
matVal(: ,N+1) = max(K-vetS,O) ; 
matval(1, :) = K*exp(-r*dt*(N-vetj)); 
matval(M+l, :> = 0; 
% set up the tridiagonal coefficients matrix 
a = 0.5*(r*dt*veti-sigma-2*dt*(veti.^2)); 
b = l+sigma^2*dt*(veti.^2)+r*dt; 
c = -0.5*(r*dt*veti+sigma-2*dt*(veti.^2)); 
coeff = diag(a(3:M) ,-1) + diag(b(2:M)) 
+ diag(c(2:M-l),1) ; 
[L,Ul = lu(coeff); 
% solve the sequence of linear systems 
aux = zeros(M-1.1); 
for j=N:-1:l 
aux(1) = - a(2) * matval(1,j); % other term from BC is zero 
matval(2:M,j) = U \ (L \ (matval(2:M,j+l) + aux)); 
end 
% return price, possibly by linear interpolation outside the grid 
price = interpi (vets, matVal( : ,I>, SO) ; 
Fig. 9.3 MATLAB code to price a vanilla European option by a fully implicit method. 

PRICING A BARRIER OPTION BY THE CRANK-NICOLSON METHOD 
485 
4.0760 
>> EuPut1mp1(50,50,0.1.5/12,0.4,100,0.5,5/2400) 
ans = 
4.0718 
The results are fairly accurate and may be improved by a refined grid with- 
out the risk of running into numerical instabilities. Another way to improve 
accuracy is to exploit the Crank-Nicolson method; we will do this in the next 
section for a barrier option. 
9.4 
PRICING A BARRIER OPTION BY THE CRANK-NICOLSON 
METHOD 
The Crank-Nicolson method has been introduced in section 5.3.3 as a way to 
improve accuracy by combining the explicit and implicit methods. Applying 
this idea to the Black-Scholes equation leads to the following grid equation: 
r 
r 
2 
- 
- - f z , j - 1  
+ Zhj. 
These equations may be rewritten as 
-azfz-l,j-l + (1 - Pi)fz,j-l - Yifi+l,J-l = Wfi-1,j + (1 + P i M j  + Yifi+l,j, 
(9.5) 
where 
bt 
a, = -((a2i2 - ri) 
4 
6t 
pi = --(a2i2 + r )  
2 
6t 
4 
~i 
= - ( 2 i 2  +ri). 
We consider here the down-and-out put option, that we have introduced in 
section 2.7.1, assuming continuous barrier monitoring. In this case we need 
only to consider the domain Sb 5 S 5 Smax; 
the boundary conditions are 
f ( s m a x ,  t )  = 01 
f (sb, t )  = 0. 
Taking these boundary conditions into account, we may rewrite equation (9.5) 
in matrix form: 
Mlfj-1 = Mzfj, 
(9.6) 

where 
486 
OPTION PRICING BY FINITE DIFFERENCE METHODS 
-71 
- a 3  
l-p3 
-y3 
1 - P 2  
-72 
-ffM-2 
1 - P M - 2  
- 7 M - 2  
-ffM-l 
1-OM-1 
71 
1 + P z  
72 
ff3 
1 f P 3  
73 
f f M - 2  
1 + P M - 2  
YM-2 
ffM-1 
1 + P M - l  
T 
.,.fM-l,j] 
. 
The MATLAB code is displayed in figure 9.4. The result may be compared 
with those obtained by the analytical pricing formula of section 2.7.1: 
>> DOPut (50,50,0.1,5/12,0.4,40) 
ans = 
0.5424 
>> D0PutCK(50,50,0.1,5/12,0.4,40,100,0.5,1/1200~ 
ans = 
0.5414 
Barrier options come in a variety of forms; more on the application of PDEs 
to barrier options may be found in [9]. 
9.5 
DEALING WITH AMERICAN OPTIONS 
While pricing a vanilla European option by finite differences is certainly in- 
structive, it is not very practical. We may apply the idea to American options, 
for which exact formulas are not available. The main difficulty in pricing an 
American option is the existence of a free boundary due to the possibility of 
early exercise. To avoid arbitrage, the option value at each point in the (S, t) 
space cannot be less than the intrinsic value (i.e., the immediate payoff if the 
option is exercised). For a vanilla American put, this means 
f(S, t) 2 max{K - S(t), 0). 
From a strictly practical point of view, taking this condition into account is 
not very difficult, at least in an explicit scheme. We could simply apply the 

DEALING WITH AMERICAN OPTIONS 
487 
function price = DOPutCK(SO,K,r,T,sigma,Sb,Smax,dS,dt) 
% set up grid and adjust increments if necessary 
M = round( (Smax-Sb) /dS) ; 
dS = (Smax-Sb)/M; 
N = round(T/dt); 
dt = T/N; 
matval = zeros(M+l,N+l); 
vets = linspace(Sb,Smax,M+l)’; 
veti = vets / dS; 
vetj = 0:N; 
% set up boundary conditions 
matVal(: ,N+1) = max(K-vetS,O); 
matval(1,:) = 0 ;  
matval(M+l,:) = 0; 
% set up the coefficients matrix 
alpha = 0.25*dt*( sigmaA2*(veti.-2) - r*veti 1; 
beta = -dt*0.5*( sigma^2*(veti.^2) + r 1; 
gamma = 0.25*dt*( sigmaA2*(veti.-2) + r*veti 1; 
M1 = -diag(alpha(S:M) ,-1) + diag(1-beta(2:M)) - diag(gamma(2:M-1) ,1) ; 
[L,Ul = lu(M1); 
M2 = diag(alpha(3:M) ,-1) + diag(l+beta(2:M)) 
+ diag(gamma(2:M-1) ,1); 
% solve the sequence of linear systems 
for j=N: 
-1 : 1 
end 
X return price, possibly by linear interpolation outside the grid 
price = interpl(vetS, matval(:,l), SO); 
matval(2:M,j) = U \ (L \ (M2*matval(2:M,j+l))); 
Fig. 9.4 
met hod. 
MATLAB code to price a down-and-out put option by the Crank-Nicolson 

488 
OPTION PRICING BY FINITE DIFFERENCE METHODS 
procedure of section 9.2 with a small modification. After computing fij, we 
should check for the possibility of early exercise, and set 
just like we do with binomial lattices. Due to instability issues, we might prefer 
adopting an implicit scheme. In this case, there is an additional complication, 
as the relationship above requires knowing fij already, which is not the case 
in an implicit scheme. To get past this difficulty, we may resort to an iterative 
method to solve the linear system rather than to a direct method based on 
LU-factorization. In section 3.2.5 we considered the Gauss-Seidel method 
with overrelaxation. We recall the idea here for convenience. Given a system 
of linear equations such as 
Ax = b, 
we should apply the following iterative scheme, starting from an initial point 
x(0): 
where k is the iteration counter and w is the overrelaxation parameter, until 
a convergence criterion is met, such as 
where E is a tolerance parameter. 
Now, suppose that we want to apply the Crank-Nicolson method to price 
an American put option. We have to solve more or less the same system 
as (9.6), but here the boundary conditions are a bit different, since there is 
no barrier on which the option value is zero. The systems we should solve 
backward in time look like 
Mlfj-1 = rj, 
where the right-hand side is 
rj = M2fj + a1 
f0,j-1 0 + f0,j 
0 
The additional term takes the customary boundary conditions for a put into 
account. The overrelaxation scheme should take into account the tridiagonal 
nature of the matrix MI, and it should also be adjusted for early exercise. 
Let g2, i = 1,. . . , M - 1, be the intrinsic value when S = ibS. For each time 

DEALING WITH AMERICAN OPTIONS 
489 
When passing from a time layer to the next one, it may be reasonable to 
initialize the iteration with a starting vector equal to the outcome of the 
previous time layer. The resulting code is displayed in figure 9.5. The code is 
a bit tricky because MATLAB starts indexing vectors from 1, but it should 
be clear enough. In this case we have not set up a matrix to contain all of 
the fij values, and the sparse matrix M1 has not been stored; the iterations 
above are best carried out by using the vectors a, 
p, and -y directly. 
The code may be compared with the binprice function, available in the Fi- 
nancial toolbox, which prices American options by a binomial lattice method 
(see section 7.1). 
>> tic, [pr, opt] = binprice(50,50 ,O. 1.5/12,1/1200,0.4 
,O) ; , toc 
Elapsed time is 0.408484 seconds. 
>> opt(1,l) 
ans = 
4.2830 
>> tic ,AmPutCK (50,50,0.1,5/12 
,O .4,100,1,1/600,1.5,0.001), 
toc 
ans = 
4.2815 
Elapsed time is 0.031174 seconds. 
>> tic,AmPutCK(50,50,0.1,5/12,0.4,100,1,1/600,1.8,0.001) 
,toc 
ans = 
4.2794 
Elapsed time is 0.061365 seconds. 
>> tic,AmPutCK(50,50,0.1,5/12,0.4,100,1,1/600,1.2,0.001) 
,toc 
ans = 
4.2800 
Elapsed time is 0.023053 seconds. 
>> tic,AmPutCK(50,50,0.1,5/12,0.4,100,1,1/1200,1.2,0.001), 
toc 
ans = 
4.2828 

490 
OPTION PRICING BY FINITE DIFFERENCE METHODS 
function price = AmPutCK(SO,K,r,T,sigma,Smax,dS,dt,omega,tol) 
M = round(Smax/dS); dS = Smax/M; % set up grid 
N = round(T/dt); dt = T/N; 
oldval = zeros(M-1,l); % vectors for Gauss-Seidel update 
newval = zeros(M-l,l) ; 
vets = linspace(O,Smax,M+l)’; 
veti = 0:M; vetj = 0:N; 
% set up boundary conditions 
payoff = max (K-vets (2 : M) ,O> ; 
pastval = payoff; % values for the last layer 
boundval = K*exp(-r*dt*(N-vetj)); 
% boundary values 
alpha = 0.25*dt*( sigmaa2*(veti.^2) - r*veti 1; 
beta = -dt*0.5*( sigmaA2*(veti.-2) + r ); 
gamma = 0.25*dt*( sigma^2*(veti.^2) + r*veti 1; 
M2 = diag(alpha(3:M) ,-1) + diag(l+beta(2:M)) 
+ diag(gamma(2:M-1) ,1); 
X solve the sequence of linear systems by SOR method 
aux = zeros (M-l,l) ; 
for j=N: -1 : 1 
set up the coefficients and the right hand side matrix 
aux(1) = alpha(2) * (boundval(1,j) + boundval(l,j+l)); 
% set up right hand side and initialize 
rhs = MZ*pastval(: 
+ aux; 
oldval = pastval; 
error = realmax; 
while to1 < error 
newval(1) = max ( payoff (I), . . . 
oldval(1) + omega/(l-beta(2)) 
* (... 
rhs(1) - (l-beta(2))*oldval(l) 
+ gamma(2)*oldval(2))) 
; 
for k=2 : M-2 
newval(k) = max ( payoff (k), . . . 
oldval(k) + omega/(l-beta(k+l)) 
* (. . . 
rhs(k) + alpha(k+l)*newval(k-l) - ... 
(1-beta(k+l))*oldval(k) 
+ gamma(k+l)*oldval(k+l))) ; 
end 
newVal(#-1) = max( payoff (M-11, . . . 
oldVal(#-1) + omega/(l-beta(M)) 
* (... 
rhs(M-1) + alpha(M)*newval(M-2) - ... 
(1-beta(M) ) *oldVal (M-1) 1) ; 
error = norm(newva1 - oldval); 
oldval = newval; 
end 
pastval = newval; 
end 
newval = [boundval(l) ; newval ; 01 ; % add missing values 
1 return price, possibly by linear interpolation outside the grid 
price = interpl(vetS, newval, SO); 
Fig. 9.5 MATLAB code to price an American put option by Crank-Nicolson method. 

FOR FURTHER READlNG 
491 
Elapsed time is 0.036693 seconds. 
>> tic,AmPutCK(50,50,0.1,5/12,0.4,100,1,1/100,1.2,0.001) 
,toc 
a s  = 
4.2778 
Elapsed time is 0.009989 seconds. 
From these examples we see that the overrelaxation parameter w has a signifi- 
cant effect on the convergence of the iterative methods. In terms of computa- 
tional speed, the finite difference approach seems even faster than the binomial 
lattice approach, but we must be very careful here. We are comparing im- 
plementations of approaches, and both could be improved. Furthermore, the 
CPU requirements are possibly affected by the way the MATLAB interpreter 
works.3 Anyway, having a whole grid of values, rather than nodes on a bino- 
mial lattice, allows us to obtain better estimates of some of the sensitivities 
(those involved in the Black-Scholes equation). Furthermore, the finite differ- 
ence approach may be preferable when dealing with complex exotic options. 
For further reading 
0 Many examples of how the PDE approach may be exploited in financial 
engineering are given in [6] or [7], which include interesting chapters on 
finite difference methods. You may also find [2] useful. 
0 We have used the finite difference approach on the Black-Scholes equa- 
tion directly; however, a change of variables may be helpful in analyzing 
stability. See, e.g., the related chapters in [3]. In that book you also 
find a treatment on finite element methods, which are considerably more 
refined than simple-minded finite difference schemes. 
0 Books aimed specifically at finite differences in financial engineering are 
[4] and [B]. 
0 See also (51 if you are interested in the finite element method. 
REFERENCES 
1. J.C. Hull. Options, Futures, and Other Derivatives (5th ed.). Prentice 
Hall, Upper Saddle River, NJ, 2003. 
3Reader owning a copy of the first edition of this book will find that quite different com- 
putational results were reported there: binprice took 14.17 seconds and the first run of 
AmPutCK took 59.48 seconds. We see that there is a speed-up which cannot be attributed 
only to faster hardware; the improvement in the MATLAB interpreter has been impressive 
too. 

492 
OPTION PRIClNG BY FINITE DIFFERENCE METHODS 
2. Y.K. Kwok. Mathematical Models of Financial Derivatives. Springer- 
Verlag, Berlin, 1998. 
3. R. Seydel. Tools for Computational Finance. Springer-Verlag, Berlin, 
2002. 
4. D. Tavella and C. Randall. Pricing Financial Instruments: The Finite 
Diflerence Method. Wiley, New York, 2000. 
5. J. Topper. Financial Engineering with Finite Elements. Wiley, New York, 
2005. 
6. P. Wilmott. Derivatives: The Theory and Practice of Financial Engineer- 
ing. Wiley, Chichester, West Sussex, England, 1999. 
7. P. Wilmott. Quantitative Finance (vols. I and II). Wiley, Chichester, 
West Sussex, England, 2000. 
8. Y.-I. Zhu, X. Wu, and I.-L. Chern. Derivative Securities and Difference 
Methods. Springer, New York, 2004. 
9. R. Zvan, K.R. Vetzal, and P.A. Forsyth. PDE Methods for Pricing Bar- 
rier Options. Journal of Economic Dynamics and Control, 24: 1563-1590, 
2000. 

