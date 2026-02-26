# Stochastic Integrals & Differential Equations

!!! info "Source"
    **The Mathematics of Financial Modeling and Investment Management** by Sergio M. Focardi and Frank J. Fabozzi, Wiley, 2004.
    These notes are used for educational purposes.

## Stochastic Integrals

I 
CHAPTER 8 
Stochastic Integrals 
n Chapter 4, we explained definite and indefinite integrals for deter-
ministic functions. Recall that integration is an operation performed 
on single, deterministic functions; the end product is another single, 
deterministic function. Integration defines a process of cumulation: The 
integral of a function represents the area below the function. However, 
the usefulness of deterministic functions in economics and finance the-
ory is limited. Given the amount of uncertainty, few laws in economics 
and finance theory can be expressed through them. It is necessary to 
adopt an ensemble view, where the path of economic variables must be 
considered a realization of a stochastic process, not a deterministic 
path. We must therefore move from deterministic integration to stochas-
tic integration. In doing so we have to define how to cumulate random 
shocks in a continuous-time environment. These concepts require rigor-
ous definition. This chapter defines the concept and the properties of 
stochastic integration. Based on the concept of stochastic integration, 
Chapter 10 defines stochastic differential equations. 
Two observations are in order:
 ■ While ordinary integrals and derivatives operate on functions and 
yield either individual numbers or other functions, stochastic integra-
tion operates on stochastic processes and yield either random vari-
ables or other stochastic processes. Therefore, while a definite 
integral is a number and an indefinite integral is a function, a stochas-
tic integral is a random variable or a stochastic process. A differential 
equation—when equipped with suitable initial or boundary condi-
tions—admits as a solution a single function while a stochastic differ-
ential equations admits as a solution a stochastic process. 
217 

218 
The Mathematics of Financial Modeling and Investment Management
 ■ Moving from a deterministic to a stochastic environment does not 
necessarily require leaving the realm of standard calculus. In fact, all 
the stochastic laws of economics and finance theory could be 
expressed as laws that govern the distribution of transition probabili-
ties. We will see an example of this mathematical strategy when we 
introduce the Fokker-Planck differential equations (Chapter 20). The 
latter are deterministic partial differential equations that govern the 
probability distributions of prices. Nevertheless it is often convenient 
to represent uncertainty directly through stochastic integration and 
stochastic differential equations. This approach is not limited to eco-
nomics and finance theory: it is also used in the domain of the physi-
cal sciences. In economics and finance theory, stochastic differential 
equations have the advantage of being intuitive: thinking in terms of 
a deterministic path plus an uncertain term is easier than thinking in 
terms of abstract probability distributions. There are other reasons 
why stochastic calculus is the methodology of choice in economics 
and finance but easy intuition plays a key role. 
For example, a risk-free bank account, which earns a deterministic 
instantaneous interest rate f(t), evolves according to the deterministic law: 
y = Aexp( f t( ) t
d )
∫ 
which is the general solution of the differential equation: 
------ = f t
dy 
( ) t
d 
y 
The solution of this differential equation tells us how the bank account 
cumulates over time. 
However if the rate is not deterministic but is subject to volatility— 
that is, at any instant the rate is f(t) plus a random disturbance—then 
the bank account evolves as a stochastic process. That is to say, the 
bank account might follow any of an infinite number of different paths: 
each path cumulates the rate f(t) plus the random disturbance. In a sense 
that will be made precise in this chapter and in Chapter 10 on stochastic 
differential equations, we must solve the following equation: 
------ = f t
dy 
( )dt plus random disturbance 
y 

219 
Stochastic Integrals 
Here is where stochastic integration comes into play: It defines how the 
stochastic rate process is transformed into the stochastic account pro-
cess. This is the direct stochastic integration approach. 
It is possible to take a different approach. At any instant t, the 
instantaneous interest rate and the cumulated bank account have two 
probability distributions. We could use a partial differential equation to 
describe how the probability distribution of the cumulated bank 
account is linked to the interest rate probability distribution. 
Similar reasoning applies to stock and derivative price processes. In 
continuous-time finance, these processes are defined as stochastic pro-
cesses which are the solution of a stochastic differential equation. 
Hence, the importance of stochastic integrals in continuous-time finance 
theory should be clear. 
Following some remarks on the informal intuition behind stochastic 
integrals, this chapter proceeds to define Brownian motions and outlines 
the formal mathematical process through which stochastic integrals are 
defined. A number of properties of stochastic integrals are then estab-
lished. After introducing stochastic integrals informally, we go on to 
define more rigorously the mathematical process for defining stochastic 
integrals. 
THE INTUITION BEHIND STOCHASTIC INTEGRALS 
Let’s first contrast ordinary integration with stochastic integration. A 
definite integral 
b 
A = ∫f
 
x
( ) x
d 
a 
is a number A associated to each function f(x) while an indefinite inte-
gral 
x 
( ) = f s
y x
( ) s
d 
∫ 
a 
is a function y associated to another function f. The integral represents 
the cumulation of the infinite terms f(s)ds over the integration interval. 
A stochastic integral, that we will denote by 

220 
The Mathematics of Financial Modeling and Investment Management 
b 
W = ∫XtdBt 
a 
or 
b 
W = ∫XtºdBt 
a 
is a random variable W associated to a stochastic process if the time 
interval is fixed or, if the time interval is variable, is another stochastic 
process Wt. The stochastic integral represents the cumulation of the sto-
chastic products XtdBt. As we will see in Chapter 10, the rationale for 
this approach is that we need to represent how random shocks feed back 
into the evolution of a process. We can cumulate separately the deter-
ministic increments and the random shocks only for linear processes. In 
nonlinear cases, as in the simple example of the bank account, random 
shocks feed back into the process. For this reason we define stochastic 
integrals as the cumulation of the product of a process X by the random 
increments of a Brownian motion. 
Consider a stochastic process Xt over an interval [S,T]. Recall that a 
stochastic process is a real variable X(ω)t that depends on both time and 
the state of the economy ω. For any given ω, X(⋅)t is a path of the process 
from the origin S to time T. A stochastic process can be identified with 
the set of its paths equipped with an appropriate probability measure. A 
stochastic integral is an integral associated to each path; it is a random 
variable that associates a real number, obtained as a limit of a sum, to 
each path. If we fix the origin and let the interval vary, then the stochas-
tic integral is another stochastic process. 
It would seem reasonable, prima facie, to define the stochastic inte-
gral of a process X(ω)t as the definite integral in the sense of Rieman-
Stieltjes associated to each path X(⋅)t of the process. If the process X(ω)t 
has continuous paths X(⋅,ω), the integrals 
T 
(
)
 = 
X s ω 
, ) s
d 
W ω
∫
( 
S 
exist for each path. However, as discussed in the previous section, this is 
not the quantity we want to represent. In fact, we want to represent the 
cumulation of the stochastic products XtdBt. Defining the integral 

221 
Stochastic Integrals 
b 
W = ∫XtdBt 
a 
pathwise in the sense of Rieman-Stieltjes would be meaningless because 
the paths of a Brownian motion are not of finite variation. If we define 
stochastic integrals simply as the limit of XtdBt sums, the stochastic 
integral would be infinite (and therefore useless) for most processes. 
However, Brownian motions have bounded quadratic variation. 
Using this property, we can define stochastic integrals pathwise through 
an approximation procedure. The approximation procedure to arrive at 
such a definition is far more complicated than the definition of the Rie-
man-Stieltjes integrals. Two similar but not equivalent definitions of sto-
chastic integral have been proposed, the first by the Japanese 
mathematician Kyosi Itô in the 1940s, the second by the Russian physi-
cist Ruslan Stratonovich in the 1960s. The definition of stochastic inte-
gral in the sense of Itô or of Stratonovich replaces the increments ∆xi 
with the increments ∆Bi of a fundamental stochastic process called 
Brownian motion. The increments ∆Bi represent the “noise” of the pro-
cess.1 The definition proceeds in the following three steps:
 ■ Step 1. The first step consists in defining a fundamental stochastic pro-
cess—the Brownian motion. In intuitive terms, a Brownian motion 
Bt(ω) is a continuous limit (in a sense that will be made precise in the 
following sections) of a simple random walk. A simple random walk is 
a discrete-time stochastic process defined as follows. A point can move 
one step to the right or to the left. Movement takes place only at dis-
crete instants of time, say at time 1,2,3,…. At each discrete instant, the 
point moves to the right or to the left with probability ¹₂. 
The random walk represents the cumulation of completely uncer-
tain random shocks. At each point in time, the movement of the point 
is completely independent from its past movements. Hence, the 
Brownian motion represents the cumulation of random shocks in the 
limit of continuous time and of continuous states. It can be demon-
strated that a.s. each path of the Brownian motion is not of bounded 
total variation but it has bounded quadratic variation. 
1 The definition of stochastic integrals can be generalized by taking a generic square 
integrable martingale instead of a Brownian motion. Itô defined stochastic integrals 
with respect to a Brownian motion. In 1967 H. Kunita and S. Watanabe extended 
the definition of stochastic integrals to square integrable martingales. 

222 
The Mathematics of Financial Modeling and Investment Management 
Recall that the total variation of a function f(x) is the limit of the 
sums 
(
) – f xi
f xi
( 
– 1)
∑ 
while the quadratic variation is defined as the limit of the sums 
∑ 
2
(
) – f xi
f xi
( 
– 1) 
Quadratic variation can be interpreted as the absolute volatility of a 
process. Thanks to this property, the ∆Bi of the Brownian motion 
provides the basic increments of the stochastic integral, replacing the 
∆xi of the Rieman-Stieltjes integral.
 ■ Step 2. The second step consists in defining the stochastic integral for a 
class of simple functions called elementary functions. Consider the time 
interval [S,T] and any partition of the interval [S,T] in N subintervals: 
≡ 
t1
S
t0 <
 < …ti < …tN ≡T . An elementary function φ is a function 
defined on the time t and the outcome ω such that it assumes a constant 
value on the i-th subinterval. Call I[ti+1,ti) the indicator function of the 
interval [ti+1,ti). The indicator function of a given set is a function that 
assumes value 1 on the points of the set and 0 elsewhere. We can then 
write an elementary function φ as follows: 
φ(t, ω) = ∑εi ω
[
+ 1,
)
(
)I ti 
ti
i 
In other words, the constants εi(ω) are random variables and the 
function φ(t,ω) is a stochastic process made up of paths that are con-
stant on each i-th interval. 
We can now define the stochastic integral, in the sense of Itô, of 
elementary functions φ(t,ω) as follows: 
T 
W = ∫φ(t, ω)dBt(
) = ∑εi ω
ω
(
)]
ω
(
)[Bi + 1(
) – Bi ω
S
i 
where B is a Brownian motion. 
It is clear from this definition that W is a random variable ω → 
W(ω). Note that the Itô integral thus defined for elementary functions 

223 
Stochastic Integrals 
cumulates the products of the elementary functions φ(t,ω) and of the 
increments of the Brownian motion Bt(ω). 
It can be demonstrated that the following property, called Itô 
isometry, holds for Itô stochastic integrals defined for bounded ele-
mentary functions as above: 

2 
T

T 
ω
φ(t, ω)dBt(
) 
= E ∫φ(t, ω)2 t
d 
E ∫ 

S
S 
The Itô isometry will play a fundamental role in Step 3.
 ■ Step 3. The third step consists in using the Itô isometry to show that 
each function g which is square-integrable (plus other conditions that 
will be made precise in the next section) can be approximated by a 
sequence of elementary functions φn(t,ω) in the sense that 
T 
E ∫[g – φ (t, ω)]2 t
d →0
n 
S 
If g is bounded and has a continuous time-path, the functions φn(t,ω) 
can be defined as follows: 
(
[
φ (t, ω) = ∑g ti , ω)I ti + 1, ti )
n 
i 
where I is the indicator function. We can now use the Itô isometry to 
define the stochastic integral of a generic function f(t,ω) as follows: 
T
T 
f t, ω)dBt(
) = lim φ (t, ω)dBt(
)
n
∫(
ω
n →∞∫ 
ω
S
S 
The Itô isometry insures that the Cauchy condition is satisfied 
and that the above sequence thus converges. 
In outlining the above definition, we omitted an important point 
that will be dealt with in the next section: The definition of the stochas-
tic integral in the sense of Itô requires that the elementary functions be 
without anticipation—that is, they depend only on the past history of 

224 
The Mathematics of Financial Modeling and Investment Management 
the Brownian motion. In fact, in the case of continuous paths, we wrote 
the approximating functions as follows: 
( 
ω
(
)]
φ (t, ω) = ∑g ti, ω)[Bi + 1(
) – Bi ω
n 
i 
taking the function g in the left extreme of each subinterval. 
However, the definition of stochastic integrals in the sense of Stra-
tonovich admits anticipation. In fact, the stochastic integral in the sense 
of Stratonovich, written as follows: 
T 
(
ω
f t, ω)°dBt(
)
∫ 
S 
uses the following approximation under the assumption of continuous 
paths: 
( * 
ω
(
)]
φ (t, ω) = ∑g ti , ω)[Bi + 1(
) – Bi ω
n 
i 
where 
– ti
ti + 1
*ti = -------------------
2 
is the midpoint of the i-th subinterval. 
Whose definition—Itô’s or Stratonovich’s—is preferable? Note that 
neither can be said to be correct or incorrect. The choice of the one over 
the other is a question of which one best represents the phenomena 
under study. The lack of anticipation is one reason why the Itô integral 
is generally preferred in finance theory. 
We have just outlined the definition of stochastic integrals leaving 
aside mathematical details and rigor. The following two sections will 
make the above process mathematically rigorous and will discuss the 
question of anticipation of information. While these sections are a bit 
technical and might be skipped by those not interested in the mathemat-
ical details of stochastic calculus, they explain a number of concepts 
that are key to the modern development of finance theory. 

225 
Stochastic Integrals 
BROWNIAN MOTION DEFINED 
The previous section introduced Brownian motion informally as the 
limit of a simple random walk when the step size goes to zero. This sec-
tion defines Brownian motion formally. The term “Brownian motion” is 
due to the Scottish botanist Robert Brown who in 1828 observed that 
pollen grains suspended in a liquid move irregularly. This irregular 
motion was later explained by the random collision of the molecules of 
the liquid with the pollen grains. It is therefore natural to represent 
Brownian motion as a continuous-time stochastic process that is the 
limit of a discrete random walk. 
Let’s now formally define Brownian motion and demonstrate its 
existence. Let’s first go back to the probabilistic representation of the 
economy. Recall from Chapter 6 that the economy is represented as a 
probability space (Ω,ℑ,P), where Ω is the set of all possible economic 
states, ℑ is the event σ-algebra, and P is a probability measure. Recall 
that the economic states ω ∈ Ω are not instantaneous states but repre-
sent full histories of the economy for the time horizon considered, 
which can be a finite or infinite interval of time. In other words, the eco-
nomic states are the possible realization outcomes of the economy. 
Recall also that, in this probabilistic representation of the economy, 
time-variable economic quantities—such as interest rates, security prices 
or cash flows as well as aggregate quantities such as economic output— 
are represented as stochastic processes Xt(ω). In particular, the price and 
dividend of each stock are represented as two stochastic processes St(ω) 
and dt(ω). 
Stochastic processes are time-dependent random variables defined 
over the set Ω. It is critical to define stochastic processes so that there is no 
anticipation of information, i.e., at time t no process depends on variables 
that will be realized later. Anticipation of information is possible only 
within a deterministic framework. However the space Ω in itself does not 
contain any coherent specification of time. If we associate random vari-
ables Xt(ω) to a time index without any additional restriction, we might 
incur in the problem of anticipation of information. Consider, for instance, 
an arbitrary family of time-indexed random variables Xt(ω) and suppose 
that, for some instant t, the relationship Xt(ω) = Xt+1(ω) holds. In this case 
there is clearly anticipation of information as the value of the variable 
Xt+1(ω) at time t+1 is known at an earlier time t. All relationships that lead 
to anticipation of information must be treated as deterministic. 
The formal way to specify in full generality the evolution of time and 
the propagation of information without anticipation is through the con-
cept of filtration. Recall from Chapter 6 that the concept of filtration is 
based on identifying all events that are known at any given instant. It is 

226 
The Mathematics of Financial Modeling and Investment Management 
assumed that it is possible to associate to each moment t a σ-algebra of 
events ℑt ⊂ ℑ formed by all events that are known prior to or at time t. It 
is assumed that events are never “forgotten,” i.e., that ℑt ⊂ ℑs, if t < s. 
An increasing sequence of σ-algebras, each associated to the time at 
which all its events are known, represents the propagation of informa-
tion. This sequence (called a filtration) is typically indicated as ℑt. 
The economy is therefore represented as a probability space (Ω,ℑ,P) 
equipped with a filtration {ℑt}. The key point is that every process Xt(ω) 
that represents economic or financial quantities must be adapted to the 
filtration {ℑt}, that is, the random variable Xt(ω) must be measurable 
with respect to the σ-algebras ℑt. In simple terms, this means that each 
event of the type Xt(ω) ≤ x belongs to ℑt while each event of the type 
Xs(ω) ≤ y for t ≤ s belongs to ℑs. For instance, consider a process Pt(ω) 
which might represent the price of a stock. Any coherent representation 
of the economy must ensure that events such as {ω: Ps(ω) ≤ c} are not 
known at any time t < s. The filtration {ℑt} prescribes all events admissi-
ble at time t. 
Why do we have to use the complex concept of filtration? Why can’t 
we simply identify information at time t with the values of all the vari-
ables known at time t as opposed to identifying a set of events? The 
principal reason is that in a continuous-time continuous-state environ-
ment any individual value has probability zero; we cannot condition on 
single values as the standard definition of conditional probability would 
become meaningless. In fact, in the standard definition of conditional 
probability (see Chapter 6) the probability of the conditioning event 
appears in the denominator and cannot be zero. 
It is possible, however, to reverse this reasoning and construct a fil-
tration starting from a process. Suppose that a process Xt(ω) does not 
admit any anticipation of information, for instance because the Xt(ω) 
are all mutually independent. We can therefore construct a filtration ℑt 
as the strictly increasing sequence of σ-algebras generated by the process 
Xt(ω). Any other process must be adapted to ℑt. 
Let’s now go back to the definition of the Brownian motion. Sup-
pose that a probability space (Ω,ℑ,P) equipped with a filtration ℑt is 
given. A one-dimensional standard Brownian motion is a stochastic 
process Bt(ω) with the following properties:
 ■ Bt(ω) is defined over the probability space (Ω,ℑ,P).
 ■ Bt(ω) is continuous for 0 ≤ t < ∞.
 ■ B0(ω) = 0.
 ■ Bt(ω) is adapted to the filtration ℑt.
 ■ The increments Bt(ω) –Bs(ω) are independent and normally distributed 
with variance (t–s) and zero mean. 

227 
Stochastic Integrals 
The above conditions2 state that the standard Brownian motion is a 
stochastic process that starts at zero, has continuous paths and normally 
distributed increments whose variance grows linearly with time. Note 
that in the last condition the increments are independent of the σ-alge-
bra ℑs and not of the previous values of the process. As noted above, 
this is because any single realization of the process has probability zero 
and it is therefore impossible to use the standard concept of conditional 
probability: conditioning must be with respect to a σ-algebra ℑs. Once 
this concept has been firmly established, one might speak loosely of 
independence of the present values of a process from its previous values. 
It should be clear, however, that what is meant is independence with 
respect to a σ-algebra ℑs. 
Note also that the filtration ℑt is an integral part of the above defini-
tion of the Brownian motion. This does not mean that, given any proba-
bility space and any filtration, a standard Brownian motion with these 
characteristics exists. For instance, the filtration generated by a discrete-
time continuous-state random walk is insufficient to support a Brown-
ian motion. The definition states only that we call a one-dimensional 
standard Brownian motion a mathematical object (if it exists) made up 
of a probability space, a filtration and a time dependent random vari-
able with the properties specified in the definition 
However it can be demonstrated that Brownian motions exist by 
constructing them. Several construction methodologies have been pro-
posed, including methodologies based on the Kolmogorov extension 
theorem or on constructing the Brownian motion as the limit of a 
sequence of discrete random walks. To prove the existence of the stan-
dard Brownian motion, we will use the Kolmogorov extension theorem. 
The Kolmogorov theorem can be summarized as follows. Consider 
the following family of probability measures 
[(
µt1, …, t (H1 
… 
× 
× H ) = P
Xt1 ∈ H1, …, Xt ∈ H ), Hi ∈ Bn ]
m
m
m
m 
for all t1,...,tk ∈ [0,∞), k ∈ N and where the Hs are n-dimensional Borel 
sets. Suppose that the following two consistency conditions are satisfied 
2 The set of conditions defining a Brownian motion can be more parsimonious. If a 
process has stationary, independent increments and continuous paths a.s. it must 
have normally distributed increments. A process with stationary independent incre-
ments and with paths that are continuous to the right and limited to the left (the cad-
lag functions), is called a Levy process. In Chapter 13 we will generalize Brownian 
motion to α-stable Levy processes that admit distributions with infinite variance and/ 
or infinite mean. 

228 
The Mathematics of Financial Modeling and Investment Management 
( H1 
…
× 
× H ) = µ t1 … 
…
×
× H σ –1(
))
…
µ tσ( ), 
, tσ(
)
 
m 
, 
, t
1
1
m
m( H σ –1( )  
m
for all permutations σ on {1,2,...,k}, and 
µ t1 …
( H1 
…
× 
× Hk) = µ t1, 
, 
, 
, 
, t ( H1 
…
× 
× Hk × Rn 
…
× 
× Rn)
, 
, tk 
…
… tk tk + 1 
m 
for all m. The Kolmogorov extension theorem states that, if the above 
conditions are satisfied, then there is (1) a probability space (Ω ,ℑ ,P) and 
(2) a stochastic process that admits the probability measures
µ t1 …
( H1 
…
× 
× H ) = P
Xt1 ∈ H1, 
, Xtm ∈ H ), Hi ∈ Bn]
[( 
… 
, 
, t
m 
m
m 
as finite dimensional distributions. 
The construction is lengthy and technical and we omit it here, but it 
should be clear how, with an appropriate selection of finite-dimensional 
distributions, the Kolmogorov extension theorem can be used to prove 
the existence of Brownian motions. The finite-dimensional distributions 
of a one-dimensional Brownian motion are distributions of the type 
µ t1 …
( H1 
…
× 
× Hk)
, 
, tk 
p  t x x1) p t2 – t1, 
, x2)… p tk – 
,
, xk) dx1… dxk 
= 
∫ ( ,
,
 
( 
x1 
( 
tk – 1 xk – 1 
H1 
…
× 
× Hk 
where 
1 
– --
2
2 
x
y
– 

( ,
,
p  t x y) = ( 2π t) 
exp
 – -----------------
2t  
and with the convention that the integrals are taken with respect to the 
Lebesgue measure. The distribution p(t,x,x1) in the integral is the initial 
distribution. If the process starts at zero, p(t,x,x1) is a Dirac delta, that 
is, it is a distribution of mass 1 concentrated in one point. 
It can be verified that these distributions satisfy the above consis-
tency conditions; the Kolmogorov extension theorem therefore ensures 
that a stochastic process with the above finite dimensional distributions 
exists. It can be demonstrated that this process has normally distributed 
independent increments with variance that grows linearly with time. It 
is therefore a one-dimensional Brownian motion. These definitions can 
be easily extended to a n-dimensional Brownian motion. 

---------
229 
Stochastic Integrals 
In the initial definition of a Brownian motion, we assumed that a fil-
tration ℑ t was given and that the Brownian motion was adapted to the 
filtration. In the present construction, however, we reverse this process. 
Given that the process we construct has normally distributed, station-
ary, independent increments, we can define the filtration ℑ t as the filtra-
B
tion ℑ t generated by Bt(ω ). The independence of the increments of the 
Brownian motion guarantee the absence of anticipation of information. 
Note that if we were given a filtration ℑ t larger than the filtration ℑ B
t , 
Bt(ω ) would still be a Brownian motion with respect to ℑ t. 
As we will see in Chapter 10 when we cover stochastic differential 
equations, there are two types of solutions of stochastic differential equa-
tions—strong and weak—depending on whether the filtration is given or 
generated by the Brownian motion. The implications of these differences 
for economics and finance will be discussed in the same section. 
The above construction does not specify uniquely the Brownian 
motion. In fact, there are infinite stochastic processes that start from the 
same point and have the same finite dimensional distributions but have 
totally different paths. However it can be demonstrated that only one 
Brownian motion has continuous paths a.s. Recall that a.s. means 
almost surely, that is, for all paths except a set of measure zero. This 
process is called the canonical Brownian motion. Its paths can be identi-
fied with the space of continuous functions. 
The Brownian motion can also be constructed as the continuous limit 
of a discrete random walk. Consider a simple random walk Wi where i are 
discrete time points. The random walk is the motion of a point that moves 
∆ x to the right or to the left with equal probability ¹₂ at each time incre-
ment ∆ x. The total displacement Xi at time i is the sum of i independent 
increments each distributed as a Bernoulli variable. Therefore the random 
variable X has a binomial distribution with mean zero and variance: 
∆ 2 x 
∆ t
Suppose that both the time increment and the space increment 
approach zero: ∆ t → 0 and ∆ x → 0. Note that this is a very informal 
statement. In fact what we mean is that we can construct a sequence of 
n
random walk processes Wi , each characterized by a time step and by a 
time displacement. It can be demonstrated that if 
∆ 2 x 
---------
σ 
→ 
∆ t

230 
The Mathematics of Financial Modeling and Investment Management 
(i.e., the square of the spaced interval and the time interval are of the 
same order) then the sequence of random walks approaches a Brownian 
motion. Though this is intuitive as the binomial distributions approach 
normal distributions, it should be clear that it is far from being mathe-
matically obvious. 
Exhibit 8.1 illustrates 100 realizations of a Brownian motion 
approximated as a random walk. The exhibit clearly illustrates that the 
standard deviation grows with the square root of the time as the vari-
ance grows linearly with time. In fact, as illustrated, most paths remain 
confined within a parabolic region. 
PROPERTIES OF BROWNIAN MOTION 
The paths of a Brownian motion are rich structures with a number of 
surprising properties. It can be demonstrated that the paths of a canoni-
cal Brownian motion, though continuous, are nowhere differentiable. It 
can also be demonstrated that they are fractals of fractal dimension ³₂. 
EXHIBIT 8.1 
Illustration of 100 Paths of a Brownian Motion Generated as an 
Arithmetic Random Walk 

231 
Stochastic Integrals 
The fractal dimension is a concept that measures quantitatively how a 
geometric object occupies space. A straight line has fractal dimension 
one, a plane has fractal dimension two, and so on. Fractal objects might 
also have intermediate dimensions. This is the case, for example of the 
path of a Brownian motion which is so jagged that, in a sense, it occu-
pies more space than a straight line. 
The fractal nature of Brownian motion paths implies that each path is 
a self-similar object. This property can be illustrated graphically. If we 
generate random walks with different time steps, we obtain jagged paths. 
If we allow paths to be graphically magnified, all paths look alike regard-
less of the time step with which they have been generated. In Exhibit 8.2, 
samples paths are generated with different time steps and then portions of 
the paths are magnified. Note that they all look perfectly similar. 
This property was first observed by Benoit Mandelbrot in sequences 
of cotton prices in the 1960s. In general, if one looks at asset or com-
modity price time series, it is difficult to recognize their time scale. For 
EXHIBIT 8.2 
Illustration of the Fractal Properties of the Paths of a Brownian Motiona 
a Five paths of a Brownian motion are generated as random walks with different time 
steps and then magnified. 

232 
The Mathematics of Financial Modeling and Investment Management 
instance, weekly or monthly time series look alike. Recent empirical and 
theoretical research work has made this claim more precise as we will 
see in Chapter 13. 
Let’s consider a one-dimensional standard Brownian motion. If we 
wait a sufficiently long period of time, every path except a set of paths 
of measure zero will return to the origin. The path between two consec-
utive passages through zero is called an excursion of the Brownian 
motion. The distribution of the maximum height attained by an excur-
sion and of the time between two passages through zero or through any 
level have interesting properties. The distribution of the time between 
two passages through zero has infinite mean. This is at the origin of the 
so-called St. Petersburg paradox described by the Swiss mathematician 
Bernoulli. The paradox consists of the following. Suppose a player bets 
increasing sums on a game which can be considered a realization of a 
random walk. As the return to zero of a random walk is a sure event, 
the player is certain to win—but while the probability of winning is one, 
the average time before winning is infinite. To stay the game, the capital 
required is also infinite. Difficult to imagine a banker ready to put up 
the money to back the player. 
The distribution of the time to the first passage through zero of a 
Brownian motion is not Gaussian. In fact, the probability of a very long 
waiting time before the first return to zero is much higher than in a nor-
mal distribution. It is a fat-tailed distribution in the sense that it has 
more weight in the tail regions than a normal distribution. The distribu-
tion of the time to the first passage through zero of a Brownian motion 
is an example of how fat-tailed distributions can be generated from 
Gaussian variables. We will come back on this subject in Chapter 13 
where we deal with the question of how the fat-tailed distributions 
observed in financial markets are generated from a large number of 
apparently independent events. 
STOCHASTIC INTEGRALS DEFINED 
Let’s now go back to the definition of stochastic integrals, starting with 
one-dimensional stochastic integrals. Suppose that a probability space 
(Ω,ℑ,P) equipped with a filtration ℑt is given. Suppose also that a 
Brownian motion Bt(ω) adapted to the filtration ℑt is given. We will 
define Itô integrals following the three-step procedure outlined earlier in 
this chapter. We have just completed the first step defining Brownian 
motion. The second step consists in defining the Itô integral for elemen-
tary functions. 

233 
Stochastic Integrals 
Let’s first define the set Φ(S,T) of functions Φ(S,T) ≡ {f(t,ω): [(0,∞) × 
Ω → R]} with the following properties:
 ■ Each f is jointly B × ℑ measurable.
 ■ Each f(t,ω) is adapted to ℑt.
 ■ 
. 3
E
f2 t( 
) 
S 
T 
∫ 
ω 
, 
t
d 
∞ 
< 
This is the set of paths for which we define the Itô integral. 
Consider the time interval [S,T] and, for each integer n, partition 
the interval [S,T] in subintervals: S
t0 < t1 < …ti < …t < …tN ≡ T in
≡ 
n 
this way: 
k2 –n 
if S
k2 –n ≤ T
≤

n
tk = tk = S 
if k2 –n < S
 
T 
if k2 –n > T 
This rule provides a family of partitions of the interval [S,T] which can 
be arbitrarily refined. 
Consider the elementary functions φ(t,ω) ∈ Φ which we write as 
(
)I ti
φ(t ω 
, ) = ∑εi ω
[ + 1 – ti ) 
i 
As φ(t,ω) ∈ Φ, εi(ω) are ℑti measurable random variables. 
We can now define the stochastic integral, in the sense of Itô, of ele-
mentary functions φ(t,ω) as 
T 
W = ∫φ(t ω 
, )dBt(
)
 = ∑εi ω
ω
(
)]
ω
(
)[Bi + 1(
)
 
– Bi ω
S
i ≥ 0 
where B is a Brownian motion. Note that the εi(ω) and the increments
j ω
(
)
 are independent for j > i. The key aspect of this definition
B (
)
 
– Bi ω
that was not included in the informal outline is the condition that the 
εi(ω) are ℑti measurable. 
For bounded elementary functions φ(t,ω) ∈ Φ the Itô isometry holds 
3 This condition can be weakened. 

234 
The Mathematics of Financial Modeling and Investment Management 
 
2 
T
 
T 
φ( t ω 
, ) dBt ω
(
) 
= E ∫φ( t ω 
, ) 2 t
d 
E ∫ 

 S
S 
The demonstration of the Itô isometry rests on the fact that 
 0 if  i
j
≠ 
E[ε iε j( Bti 
– Bti)( Bt
– Btj)] = (
) if i = j
+ 1 
j + 1 
 E ε 2
i 
This completes the definition of the stochastic integral for elementary 
functions. 
We have now completed the introduction of Brownian motions and 
defined the Itô integral for elementary functions. Let’s next introduce 
the approximation procedure that allows to define the stochastic inte-
gral for any φ (t,ω ). We will develop the approximation procedure in the 
following three additional steps that we will state without demonstra-
tion:
 ■ Step 1. Any function g(t,ω ) ∈ Φ that is bounded and such that all its 
time paths φ (·,ω ) are continuous functions of time can be approximated 
by 
(
[
φ ( t ω 
, ) = ∑ g ti ω 
, ) I ti + 1 – ti )
n 
i 
in the sense that: 
T 
[( g – φ ) 2 t
d ] → 0 , n → ∞ , ∀ω
E∫ 
n 
S 
where the intervals are those of the partition defined above. Note that
φ ( t ω 
, ) ∈Φ given that g t ω 
, ) ∈Φ .
(
n 
■ Step 2. We release the condition of time-path continuity of the 
(
φ ( t ω 
, ) . It can be demonstrated that any function h t ω 
, ) ∈Φ which
n 
is bounded but not necessarily continuous can be approximated by 
functions gn( t ω 
, ) ∈Φ which are bounded and continuous in the sense 
that 

235
Stochastic Integrals 
T 
E ∫( h – gn ) 2 t
d → 0 
S 
■ Step 3. It can be demonstrated that any function f t ω 
, ) ∈Φ , not nec-
( 
essarily bounded or continuous, can be approximated by a sequence of 
bounded functions h ( t ω 
, ) ∈Φ in the sense that
n 
T 
E ∫( f – h ) 2 t
d → 0
n 
S 
We now have all the building blocks to complete the definition of 
Itô stochastic integrals. In fact, by virtue of the above three-step 
approximation procedure, given any function f t ω 
, ) ∈Φ , we can
( 
choose a sequence of elementary functions φ ( t ω 
, ) ∈Φ such that the
n 
following property holds: 
T 
E ∫( f – φ ) 2 t
d → 0
n 
S 
Hence we can define the Itô stochastic integral as follows: 
T
T 
(
[ ](
)
w
= 
f t ω 
, ) dBt ω
(
)
 = lim 
φ ( t ω 
, ) t
d 
n
I f
∫ 
n →∞∫ 
S
S 
The limit exists as 
T 
∫φ n( t ω 
, ) dBt ω
(
)
 
S 
forms a Cauchy sequence by the Itô isometry, which holds for every 
bounded elementary function. 
Let’s now summarize the definition of the Itô stochastic integral: 
Given any function f t ω 
, ) ∈Φ , we define the Itô stochastic integral
( 
by 

236 
The Mathematics of Financial Modeling and Investment Management 
T
T 
(
[ ](
)
w
= 
f t ω 
, ) dB ω
(
)
 = lim 
φ ( t ω 
, ) dt
n
I f
∫ 
t
n →∞∫ 
S
S 
where the functions φ ( t ω 
, ) ∈Φ are a sequence of elementary functions
n 
such that 
T 
E ∫( f – φ ) 2dt → 0
n 
S 
The multistep procedure outlined above ensures that the sequence 
φ ( t ω 
, ) ∈Φ exists. In addition, it can be demonstrated that the Itô
n 
isometry holds in general for every f t ω 
, ) ∈Φ
( 
 
2 
T
 
T 
E ∫ ( 
t 
(
f t ω 
, ) dB ω
(
) 
= E
f t ω 
, ) 2dt
∫


S
S 
SOME PROPERTIES OF ITÔ STOCHASTIC INTEGRALS 
Suppose that f g ∈ Φ( S T
,
)  and let 0 < S < U < T. It can be demon-
, 
strated that the following properties of Itô stochastic integrals hold: 
T 
U
T 
f Bt = 
f Bt + ∫ f B  for a.a. ω
d 
∫ d 
d
t
∫ 
S 
S
U 
T 
d
E
f
 Bt = 0
∫ 
S 
T 
T
T 
( cf + dg) dB = c f  Bt + ∫ d 
d 
d g  B , for a.a. ω, ,c d constants
t 
S 
S
S 
∫ 
t 
∫ 
If we let the time interval vary, say (0,t), then the stochastic integral 
becomes a stochastic process: 

237 
Stochastic Integrals 
=
It ω
(
)
 
t 
∫ f B
d t 
0 
It can be demonstrated that a continuous version of this process exists. 
The following three properties can be demonstrated from the definition 
of integral: 
t 
∫ dB
= Bt
s 
0 
t 
∫ 
t – 
t 
∫ 
s B
tB
d 
= 
B ds
s 
s 
0
0 
t 
∫
1
2
1
B dB
= --Bt – --t
s
s 
2
2 
0 
The last two properties show that, after performing stochastic integra-
tion, deterministic terms might appear. 
SUMMARY
 ■ Stochastic integration provides a coherent way to represent that instan-
taneous uncertainty (or volatility) cumulates over time. It is thus funda-
mental to the representation of financial processes such as interest 
rates, security prices or cash flows as well as aggregate quantities such 
as economic output.
 ■ Stochastic integration operates on stochastic processes and produces 
random variables or other stochastic processes.
 ■ Stochastic integration is a process defined on each path as the limit of a 
sum. However, these sums are different from the sums of the Riemann-
Lebesgue integrals because the paths of stochastic processes are gener-
ally not of bounded variation.
 ■ Stochastic integrals in the sense of Itô are defined through a process of 
approximation.
 ■ Step 1 consists in defining Brownian motion, which is the continuous 
limit of a random walk. 

238 
The Mathematics of Financial Modeling and Investment Management
 ■ Step 2 consists in defining stochastic integrals for elementary functions 
as the sums of the products of the elementary functions multiplied by 
the increments of the Brownian motion.
 ■ Step 3 extends this definition to any function through approximating 
sequences. 


## Differential Equations

I 
CHAPTER 9 
Differential Equations and 
Difference Equations 
n Chapter 4, we explained how to obtain the derivative of a function. 
In this chapter we will introduce differential equations. In nontechnical 
terms, differential equations are equations that express a relationship 
between a function and one or more derivatives (or differentials) of that 
function. 
It would be difficult to overemphasize the importance of differential 
equations in modern science: they are used to express the vast majority 
of the laws of physics and engineering principles. In economics and 
finance, differential equations are used to express various laws and con-
ditions including the following:
 ■ The laws of deterministic quantities such as the accumulation of risk-
free bank deposits. 
■ The laws that govern the evolution of price probability distributions.
 ■ The solution of economic variational problems, such as intertemporal 
optimization.
 ■ Conditions of continuous hedging, such as the Black-Scholes equation 
that we will describe in Chapter 15. 
A large number of properties of differential equations have been 
established over the last three centuries. This chapter provides only a 
brief introduction to the concept of differential equations and their 
properties, limiting our discussion to the principal concepts. 
239 

240 
The Mathematics of Financial Modeling and Investment Management 
DIFFERENTIAL EQUATIONS DEFINED  
A differential equation is a condition expressed as a functional link 
between one or more functions and their derivatives. It is expressed as 
an equation (that is, as an equality between two terms). 
A solution of a differential equation is a function that satisfies the 
given condition. For example, the condition 
Y″( )  αY′( )  βY x
( ) = 0
x + 
x + 
( ) – b x
equates to zero a linear relationship between an unknown function Y(x), 
its first and second derivatives Y′(x),Y″(x), and a known function b(x).1 
The unknown function Y(x) is the solution of the equation that is to be 
determined. 
There are two broad types of differential equations: ordinary differ-
ential equations and partial differential equations. Ordinary differential 
equations are equations or systems of equations involving only one 
independent variable. Another way of saying this is that ordinary differ-
ential equations involve only total derivatives. In contrast, partial differ-
ential equations are differential equations or systems of equations 
involving partial derivatives. That is, there is more than one indepen-
dent variable. 
As we move from deterministic equations to stochastic equations, 
we introduce stochastic differential equations. In these differential equa-
tions, a random or stochastic term is included. 
ORDINARY DIFFERENTIAL EQUATIONS 
In full generality, an ordinary differential equation (ODE) can be expressed 
as the following relationship: 
F x Y x
x
( ) x
[ , ( ), Y 1( ), …, Y n ( )] = 0 
where Y(m)(x) denotes the m-th derivative of an unknown function Y(x). If 
the equation can be solved for the n-th derivative, it can be put in the form: 
( ) x
( ) x
Y(n – 1)( )]
Y n ( ) = G x Y x
[ , ( ), Y 1 ( ), …, 
x
1 In some equations we will denote the first and second derivatives by a single and 
double prime, respectively. 

241 
Differential Equations and Difference Equations 
Order and Degree of an ODE 
A differential equation is classified in terms of its order and its degree. 
The order of a differential equation is the order of the highest derivative 
in the equation. For example, the above differential equation is of order n 
since the highest order derivative is Y(n)(x). The degree of a differential 
equation is determined by looking at the highest derivative in the differen-
tial equation. The degree is the power to which that derivative is raised. 
For example, the following ordinary differential equations are first 
degree differential equations of different orders: 
(1)(x
Y
) – 10Y(x) + 40 = 0 
(order 1) 
(3)(x
(2)(x
(1)(x
4Y
) + Y
) + Y
) – 0.5Y(x) + 100 = 0 
(order 3) 
The following ordinary differential equations are of order 3 and fifth 
degree: 
(3)(x
(2)(x
(1)(x
4 [Y
)]5 + [Y
)]2 + Y
) – 0.5Y(x) + 100 = 0 
(3)(x
(2)(x
(1)(x
4 [Y
)]5 + [Y
)]3 + Y
) – 0.5Y(x) + 100 = 0 
When an ordinary differential equation is of the first degree, it is said to 
be a linear ordinary differential equation. 
Solution to an ODE 
Let’s return to the general ODE. A solution of this equation is any function 
y(x) such that: 
n
F x y x
1 ( ), …, y( ) x
[ , ( ), y( ) x
( )] = 0 
In general there will be not one but an infinite family of solutions. For 
example, the equation 
( ) x
( )
Y 1 ( ) = αY x
admits, as a solution, all the functions of the form 
y x
( ) = C exp(αx) 
To identify one specific solution among the possible infinite solu-
tions that satisfy a differential equation, additional restrictions must be 

242 
The Mathematics of Financial Modeling and Investment Management 
imposed. Restrictions that uniquely identify a solution to a differential 
equation can be of various types. For instance, one could impose that a 
solution of an n-th order differential equation passes through n given 
points. A common type of restriction—called an initial condition—is 
obtained by imposing that the solution and some of its derivatives 
assume given initial values at some initial point. 
Given an ODE of order n, to ensure the uniqueness of solutions it 
will generally be necessary to specify a starting point and the initial 
value of n–1 derivatives. It can be demonstrated, given the differential 
equation 
( ) x
F x  Y x
( ) x
[ , ( ), Y 1 ( ), …, Y n ( )] = 0 
that if the function F is continuous and all of its partial derivatives up to 
order n are continuous in some region containing the values y0,..., 
y( 
0 
n – 1) , then there is a unique solution y(x) of the equation in some 
Y(n–1)(x0).2
interval I = (M ≤x ≤L) such that y0 = Y(x0),...,y( 
0 
n – 1) = 
Note that this theorem states that there is an interval in which the solu-
tion exists. Existence and uniqueness of solutions in a given interval is a 
more delicate matter and must be examined for different classes of 
equations. 
The general solution of a differential equation of order n is a func-
tion of the form 
y = ϕ(x C1, …, C )
, 
n 
that satisfies the following two conditions:
 ■ Condition 1. The function y = ϕ(x,C1,...,Cn) satisfies the differential 
equation for any n-tuple of values (C1,...,Cn).
 ■ Condition 2. Given a set of initial conditions y(x0) = y0,...,y(n–1)(x0) = 
y( 
0 
n–1) that belong to the region where solutions of the equation exist, 
it is possible to determine n constants in such a way that the function y 
= ϕ(x,C1,...,Cn) satisfies these conditions. 
The coupling of differential equations with initial conditions embod-
ies the notion of universal determinism of classical physics. Given initial 
2 The condition of existence and continuity of derivatives is stronger than necessary. 
The Lipschitz condition, which requires that the incremental ratio be uniformly 
bounded in a given interval, would suffice. 

243 
Differential Equations and Difference Equations 
conditions, the future evolution of a system that obeys those equations is 
completely determined. This notion was forcefully expressed by Pierre-
Simon Laplace in the eighteenth century: a supernatural mind who 
knows the laws of physics and the initial conditions of each atom could 
perfectly predict the future evolution of the universe with unlimited pre-
cision. 
In the twentieth century, the notion of universal determinism was 
challenged twice in the physical sciences. First in the 1920s the develop-
ment of quantum mechanics introduced the so called indeterminacy 
principle which established explicit bounds to the precision of measure-
ments.3 Later, in the 1970s, the development of nonlinear dynamics and 
chaos theory showed how arbitrarily small initial differences might become 
arbitrarily large: the flapping of a butterfly’s wings in the southern hemi-
sphere might cause a tornado in northern hemisphere. 
SYSTEMS OF ORDINARY DIFFERENTIAL EQUATIONS 
Differential equations can be combined to form systems of differential 
equations. These are sets of differential conditions that must be satisfied 
simultaneously. A first-order system of differential equations is a system 
of the following type: 
dy1
-------- = f1(x y1 …
,
,
,
 
yn)
dx 
dy2
-------- = f2(x y1 …
dx 
,
,
,
 
yn) 
 
.
 .
 
. 
dyn 
-------- = f (x y1 …
dx 
,
,
,
 
yn)
n 
 
3 Actually quantum mechanics is a much deeper conceptual revolution: it challenges 
the very notion of physical reality. According to the standard interpretation of quan-
tum mechanics, physical laws are mathematical recipes that link measurements in a 
strictly probabilistic sense. According to quantum mechanics, physical states are 
pure abstractions: they can be superposed, as the celebrated “Schrodinger’s cat” 
which can be both dead and alive. 

244 
The Mathematics of Financial Modeling and Investment Management 
Solving this system means finding a set of functions y1,...,yn that satisfy 
the system as well as the initial conditions: 
(
) = y10,
,
 
yn(
) = yn0
y1 x0
…
x0
Systems of orders higher than one can be reduced to first-order systems 
in a straightforward way by adding new variables defined as the deriva-
tives of existing variables. As a consequence, an n-th order differential 
equation can be transformed into a first-order system of n equations. 
Conversely, a system of first-order differential equations is equivalent to 
a single n-th order equation. 
To illustrate this point, let’s differentiate the first equation to obtain 
d2 y1 
∂f1 
∂f1 dy1 
∂f1 dyn 
----------- = ------- + ---------------- + … + ----------------
∂x 
∂y1 dx 
∂yn dx
dx2 
Replacing the derivatives 
dy1 
dyn 
--------,
,
 
--------
… 
dx 
dx 
with their expressions f1,...,fn from the system’s equations, we obtain 
d2 y1 
----------- = F2(x y1 …
,
,
,
 
yn) 
dx2 
If we now reiterate this process, we arrive at the n-th order equation: 
( )
d n y1 
,
,
,
 
yn)
--------------- = F (x y1 …
( )  
n 
dx n
We can thus write the following system: 

245 
Differential Equations and Difference Equations 
dy1
-------- = f1(x y1 …
,
,
,
 
yn)
dx 
 
d2 y1
----------- = F2(x y1 …
,
,
,
 
yn)
dx2 
 
. 
 .
 
. 
d n
( )
 
y1 
--------------- = F (x y1 …
,
,
,
 
yn)
( )  
n 
dx n
 
We can express y2,...,yn as functions of x y1 y′
…
,
,
 ,
,
 
y( 
1 
n – 1) by solving, 
if possible, the system formed with the first n – 1 equations: 
1 
 
,
,
 ,
,
 
y( 
1 
n – 1))
y2 = ϕ2(x y1 y′
…
1 
 
,
,
 ,
,
 
y( 
1 
n – 1))
y3 = ϕ3(x y1 y′
…
1 
 .
 
. 
 .
 
 
n 
,
,
 ,
,
 
y( 
1 
n – 1))
1
yn = ϕ (x y1 y′
…
Substituting these expressions into the n-th equation of the previous sys-
tem, we arrive at the single equation: 
( )
d n y1 
,
 ,
,
 
y( 
1 
n – 1))
--------------- = Φ(x y′
…
1
( )
dx n
Solving, if possible, this equation, we find the general solution 
y1 = y1(x C1 …
,
 ,
,
 
Cn) 
Substituting this expression for y1 into the previous system, y2,...,yn can 
be computed. 

246 
The Mathematics of Financial Modeling and Investment Management 
CLOSED-FORM SOLUTIONS OF ORDINARY 
DIFFERENTIAL EQUATIONS 
Let’s now consider the methods for solving two types of common differ-
ential equations: equations with separable variables and equations of lin-
ear type. Let’s start with equations with separable variables. Consider the 
equation 
------ = f x
( )
dy 
( )g y
dx 
This equation is said to have separable variables because it can be writ-
ten as an equality between two sides, each depending on only y or only 
x. We can rewrite our equation in the following way: 
dy 
( )dx 
g y
---------- = f x
( )  
This equation can be regarded as an equality between two differentials 
in y and x respectively. Their indefinite integrals can differ only by a 
constant. Integrating the left side with respect to y and the right side 
with respect to x, we obtain the general solution of the equation: 
∫
dy
---------- = ∫f x
( ) x
d
 
+ C 
g y
( )  
For example, if g(y) ≡y, the previous equation becomes 
------ = f x
dy 
( )dx 
y 
whose solution is 
y
d 
----- = ∫f x
( ) x
d + C ⇒y = A exp( f x
∫y 
( ) x
d + C ⇒log y = ∫f
 
x
∫( ) x
d ) 
where A = exp(C). 
A differential equation of this type describes the continuous com-
pounding of time-varying interest rates. Consider, for example, the 
growth of capital C deposited in a bank account that earns the variable 
but deterministic rate r = f(t). When interest rates Ri are constant for dis-

247 
Differential Equations and Difference Equations 
crete periods of time ∆ti, compounding is obtained by purely algebraic 
formulas as follows: 
C ti
(
( ) – C ti – ∆ti) 
Ri∆ti = -----------------------------------------
(
C ti – ∆ti) 
Solving for C(ti): 
C ti
(
( ) = (1 + Ri∆ti)C ti – ∆ti) 
By recursive substitution we obtain 
( ) = (1 + Ri∆ti)(1 + 
∆ti – 1)…(1 + R1∆t1)C t0
C ti
(
)
Ri – 1 
However, market interest rates are subject to rapid change. In the 
limit of very short time intervals, the instantaneous rate r(t) would be 
defined as the limit, if it exists, of the discrete interest rate: 
C t  + ∆t) – C t
( 
( )
r t( ) = lim ----------------------------------------
→ 
∆ 
0 
∆tC t
t 
( )  
The above expression can be rewritten as a simple first-order differential 
equation in C: 
dC t
r t
( ) = --------------
dt
( )C t
( )  
In a simple intuitive way, the above equation can be obtained consider-
ing that in the elementary time dt the bank account increments by the 
amount dC = C(t)r(t)dt. In this equation, variables are separable. It 
admits the family of solutions: 
C = A exp( r t( ) t
d )
∫ 
where A is the initial capital. 
Linear Differential Equation 
Linear differential equations are equations of the following type: 

248 
The Mathematics of Financial Modeling and Investment Management 
n
1
x
a ( )y( )+ an–1( )y(n–1) 
( )y( )+ a0 x
+ ( ) = 0
x
+ … + a1 x
( )y
b x
n 
If the function b is identically zero, the equation is said to be homoge-
neous. 
In cases where the coefficients a’s are constant, Laplace transforms 
provide a powerful method for solving linear differential equation. Con-
sider, without loss of generality, the following linear equation with con-
stant coefficients: 
n
( ) + an – 1 
(n – 1) 
( )  
( )
n
1
a y 
y 
+ … + a1y 
+ a0y = b x
together with the initial conditions: y(0) = y0,...,y(n–1)(0) = y(n–1) . In cases in 
0 
which the initial point is not the origin, by a variable transformation we 
can shift the origin. 
Let’s recall the formula to Laplace-transform derivatives presented 
in Chapter 4. For one-sided Laplace transforms the following formulas 
hold: 
L
df x
-------------= sL[f x
( )
dx  
( ) 
( )] – f 0
n
L
d f x
0
… f(n – 1)( )
----------------= s L[f x
dxn  
( ) 
n
( )] – sn – 1f' ( ) –
– 
0
Suppose that a function y = y(x) satisfies the previous linear equation 
with constant coefficients and that it admits a Laplace transform. Apply 
one-sided Laplace-transform to both sides of the equation. If Y(s) = 
L[y(x)], the following relationships hold: 
( 
n
1
[ ( )]
L a y( ) + an – 1y(n – 1) + … + a1y( ) + a0y) = L b x
n
( ) 0
a [snY s
1
0
( ) – sn – 1 y 
( ) – … – y(n – 1)( )]
n 
+ an – 1[sn – 1
1
Y s
( ) 0
0
( ) – sn – 2 y 
( ) – … – y(n – 2)( )] 
( ) = B s
+ … + a0Y s
( )  

249 
Differential Equations and Difference Equations 
Solving this equation for Y(s), that is, Y(s) = g[s,y(t)(0),...,y(n–1)(0)] the 
inverse Laplace transform y(t) = L–1[Y(s)] uniquely determines the solu-
tion of the equation. 
Because inverse Laplace transforms are integrals, with this method, 
when applicable, the solution of a differential equation is reduced to the 
determination of integrals. Laplace transforms and inverse Laplace 
transforms are known for large classes of functions. Because of the 
important role that Laplace transforms play in solving ordinary differ-
ential equations in engineering problems, there are published reference 
tables.4 Laplace transform methods also yield closed-form solutions of 
many ordinary differential equations of interest in economics and 
finance. 
NUMERICAL SOLUTIONS OF ORDINARY 
DIFFERENTIAL EQUATIONS 
Closed-form solutions are solutions that can be expressed in terms of 
known functions such as polynomials or exponential functions. Before 
the advent of fast digital computers, the search for closed-form solu-
tions of differential equations was an important task. Today, thanks to 
the availability of high-performance computing, most problems are 
solved numerically. This section looks at methods for solving ordinary 
differential equations numerically. 
The Finite Difference Method 
Among the methods used to numerically solve ordinary differential 
equations subject to initial conditions, the most common is the finite 
difference method. The finite difference method is based on replacing 
derivatives with difference equations; differential equations are thereby 
transformed into recursive difference equations. 
Key to this method of numerical solution is the fact that ODEs sub-
ject to initial conditions describe phenomena that evolve from some 
starting point. In this case, the differential equation can be approxi-
mated with a system of difference equations that compute the next point 
based on previous points. This would not be possible should we impose 
boundary conditions instead of initial conditions. In this latter case, we 
have to solve a system of linear equations. 
4 See, for example, “Laplace Transforms,” Chapter 29 in Milton Abramowitz and 
Irene A. Stegun (eds.), Handbook of Mathematical Functions with Formulas, 
Graphs, and Mathematical Tables (New York: Dover, 1972). 

-----
250 
The Mathematics of Financial Modeling and Investment Management 
To illustrate the finite difference method, consider the following 
simple ordinary differential equation and its solution in a finite interval: 
f ′( ) = f x
x
( )  
df 
= dx
f 
( ) = x
C
log f x
+ 
f x
+
( ) = exp(x
C) 
As shown, the closed-form solution of the equation is obtained by separa-
tion of variables, that is, by transforming the original equation into 
another equation where the function f appears only on the left side and 
the variable x only on the right side. 
Suppose that we replace the derivative with its forward finite differ-
ence approximation and solve 
( 
(
)
f xi + 1) – f xi
------------------------------------ = f xi
(
)
 
– xi
xi + 1 
( 
(
)
f xi 
= [1 + (xi + 1 – xi)]f xi
+ 1) 
If we assume that the step size is constant for all i: 
(
) = [1 + ∆x]if x0
f xi
(
)
 
The replacement of derivatives with finite differences is often called the 
Euler approximation. The differential equation is replaced by a recur-
sive formula based on approximating the derivative with a finite differ-
ence. The i-th value of the solution is computed from the i–1-th value. 
Given the initial value of the function f, the solution of the differential 
equation can be arbitrarily approximated by choosing a sufficiently 
small interval. Exhibit 9.1 illustrates this computation for different val-
ues of ∆x. 
In the previous example of a first-order linear equation, only one ini-
tial condition was involved. Let’s now consider a second-order equation: 
x
( ) = 0
f ″( ) + kf x

251 
Differential Equations and Difference Equations 
EXHIBIT 9.1 
Numerical Solutions of the Equation f ′ = f with the Euler 
Approximation for Different Step Sizes 
This equation describes oscillatory motion, such as the elongation of a 
pendulum or the displacement of a spring. 
To approximate this equation we must approximate the second 
derivative. This could be done, for example, by combining difference 
quotients as follows: 
( 
( )
f x + ∆x) – f x
f ′( ) ≈---------------------------------------
∆x
x
f x + 2∆x) – f x + ∆x)
(
(
f ′(x + ∆x) ≈---------------------------------------------------------
∆x

252 
The Mathematics of Financial Modeling and Investment Management 
f ′(x + ∆x) – f ′( )
x
f ″( ) ≈---------------------------------------------
∆x
( 
(
(
( )  
x
f x + 2∆x) – f x + ∆x) f x + ∆x) – f x
--------------------------------------------------------- – ---------------------------------------
∆x
∆x
= --------------------------------------------------------------------------------------------------------
∆x
f x + 2∆x) – 2f x + ∆x) + f x
( 
(
( )
= -----------------------------------------------------------------------------
(∆x)2 
With this approximation, the original equation becomes 
f″( ) + kf x
f x + 2∆x) – 2f x + ∆x) + f x
x
( ) ≈----------------------------------------------------------------------------- + kf x
( 
( 
( )
( ) = 0 
(∆x)2 
( 
( 
(∆
( ) = 0
f x + 2∆x) – 2f x + ∆x) + (1 + k
x)2)f x
We can thus write the approximation scheme: 
f x + ∆x) = f x
x
( 
( ) + ∆xf ′( )  
( 
( 
(∆
( )
f x + 2∆x) = 2f x + ∆x) – (1 + k
x)2)f x
Given the increment ∆x and the initial values f(0),f ′(0), using the above 
formulas we can recursively compute f(0 + ∆x), f(0 + 2∆x), and so on. 
Exhibit 9.2 illustrates this computation. 
In practice, the Euler approximation scheme is often not sufficiently 
precise and more sophisticated approximation schemes are used. For 
example, a widely used approximation scheme is the Runge-Kutta 
method. We give an example of the Runge-Kutta method in the case of 
the equation f ′′ + f = 0 which is equivalent to the linear system: 
x′ = y 
y′ = –x 
In this case the Runge-Kutta approximation scheme is the following: 
= hy i( )
k1 
= –hx i( )
h1 

253 
Differential Equations and Difference Equations 
EXHIBIT 9.2 
Numerical Solution of the Equation f ′′ + f = 0 with the Euler 
Approximation 
= h y i
1 
( ) + --h
k2
1
2 
1 
= –h x i
1
( ) + --k
h2 
2 
= h y i
1 
( ) + --h
k3
2
2 
1 
= –h x i
2
( ) + --k
h3 
2 
= h y i
[ ( ) + h
k4
3 ] 

254 
The Mathematics of Financial Modeling and Investment Management 
= –h[x i( ) + k
h4
3] 
x i + 1) = x i
1
( 
( ) + --(k1 + 2k2 + 2k3 + k4)
6 
y i + 1) = y i
1
( 
( ) + --(h1 + 2h2 + 2h3 + h4)
6 
Exhibits 9.3 and 9.4 illustrate the results of this method in the two cases 
f ′ = f and f ′′ + f = 0. 
As mentioned above, this numerical method depends critically on our 
having as givens (1) the initial values of the solution and (2) its first deriv-
ative. Suppose that instead of initial values two boundary values were 
given, for instance the initial value of the solution and its value 1,000 
steps ahead, that is, f(0) = f0, f(0 + 1,000∆x) = f1000. Conditions like these 
are rarely used in the study of dynamical systems as they imply foresight, 
EXHIBIT 9.3 
Numerical Solution of the Equation f ′ = f with the Runge-Kutta 
Method After 10 Steps 

255 
Differential Equations and Difference Equations 
EXHIBIT 9.4 
Numerical Solution of the Equation f ″ + f = 0 with the Runge-Kutta 
Method 
that is, knowledge of the future position of a system. However, they often 
appear in static systems and when trying to determine what initial condi-
tions should be imposed to reach a given goal at a given date. 
In the case of boundary conditions, one cannot write a direct recur-
sive scheme; it’s necessary to solve a system of equations. For instance, we 
could introduce the derivative f ′(x) = δ as an unknown quantity. The dif-
ference quotient that approximates the derivative becomes an unknown. 
We can now write a system of linear equations in the following way: 
∆
(f
x
∆x
) 
δ ∆x
= f0 +










 
2
( 
) 
∆
(
2f
x
∆x
) ( 
( ∆x ) ) f 
2 
1
f
k
+
= 
– 
0 
2
( ∆x ) 
( 
) ( 
( ∆x ) ) 
)
∆
(f
x
3 
2f 2 
1
f
k
+
= 
– 
. 
. 
. 
2
f1000 = 2f ( 999 ∆x ) – ( 1 + k ( ∆x ) ) f ( 998 ∆x ) 

256 
The Mathematics of Financial Modeling and Investment Management 
This is a system of 1,000 equations in 1,000 unknowns. Solving the 
system we compute the entire solution. In this system two equations, the 
first and the last, are linked to boundary values; all other equations are 
transfer equations that express the dynamics (or the law) of the system. 
This is a general feature of boundary value problems. We will encounter it 
again when discussing numerical solutions of partial differential equations. 
In the above example, we chose a forward scheme where the derivative 
is approximated with the forward difference quotient. One might use a dif-
ferent approximation scheme, computing the derivative in intervals cen-
tered around the point x. When derivatives of higher orders are involved, 
the choice of the approximation scheme becomes critical. Recall that when 
we approximated first and second derivatives using forward differences, we 
were required to evaluate the function at two points (i,i + 1) and three 
points (i,i + 1,i + 2) ahead respectively. If purely forward schemes are 
employed, computing higher-order derivatives requires many steps ahead. 
This fact might affect the precision and stability of numerical computations. 
We saw in the examples that the accuracy of a finite difference 
scheme depends on the discretization interval. In general, a finite differ-
ence scheme works, that is, it is consistent and stable, if the numerical 
solution converges uniformly to the exact solution when the length of 
the discretization interval tends to zero. Suppose that the precision of an 
approximation scheme depends on the length of the discretization inter-
( ) – f x
val ∆x. Consider the difference δf = fˆ x
( ) between the approxi-
mate and the exact solutions. We say that δf →0 uniformly in the 
interval [a,b] when ∆x →0 if, given any ε arbitrarily small, it is possible 
to find a ∆x such that δf < ε , ∀x ∈[a b] .
, 
NONLINEAR DYNAMICS AND CHAOS 
Systems of differential equations describe dynamical systems that evolve 
starting from initial conditions. A fundamental concept in the theory of 
dynamical system is that of the stability of solutions. This topic has 
become of paramount importance with the development of nonlinear 
dynamics and with the discovery of chaotic phenomena. We can only 
give a brief introductory account of this subject whose role in econom-
ics is still the subject of debate. 
Intuitively, a dynamical system is considered stable if its solutions 
do not change much when the system is only slightly perturbed. There 
are different ways to perturb a system: changing parameters in its equa-
tions, changing the known functions of the system by a small amount, 
or changing the initial conditions. 

257 
Differential Equations and Difference Equations 
Consider an equilibrium solution of a dynamical system, that is, a 
solution that is time invariant. If a stable system is perturbed when it is 
in a position of equilibrium, it tends to return to the equilibrium posi-
tion or, in any case, not to diverge indefinitely from its equilibrium posi-
tion. For example, a damped pendulum—if perturbed from a position of 
equilibrium—will tend to go back to an equilibrium position. If the pen-
dulum is not damped it will continue to oscillate forever. 
Consider a system of n equations of first order. (As noted above, 
systems of higher orders can always be reduced to first-order systems by 
enlarging the set of variables.) Suppose that we can write the system 
explicitly in the first derivatives as follows: 
dy1
-------- = f1(x y1 …
,
,
,
 
yn)
dx 
dy2
-------- = f2(x y1 …
dx 
,
,
,
 
yn) 
 
.
 .
 
. 
dyn 
-------- = f (x y1 …
dx 
,
,
,
 
yn)
n 
 
If the equations are all linear, a complete theory of stability has been 
developed. Essentially, linear dynamical systems are stable except possi-
bly at singular points where solutions might diverge. In particular, a 
characteristic of linear systems is that they incur only small changes in 
the solution as a result of small changes in the initial conditions. 
However, during the 1970s, it was discovered that nonlinear sys-
tems have a different behavior. Suppose that a nonlinear system has at 
least three degrees of freedom (that is, it has three independent nonlin-
ear equations). The dynamics of such a system can then become chaotic 
in the sense that arbitrarily small changes in initial conditions might 
diverge. This sensitivity to initial conditions is one of the signatures of 
chaos. Note that while discrete systems such as discrete maps can 
exhibit chaos in one dimension, continuous systems require at least 
three degrees of freedom (that is, three equations). 
Sensitive dependence from initial conditions was first observed in 
1960 by the meteorologist Edward Lorenz of the Massachusetts Institute 
of Technology. Lorenz remarked that computer simulations of weather 
forecasts starting, apparently, from the same meteorological data could 

258 
The Mathematics of Financial Modeling and Investment Management 
yield very different results. He argued that the numerical solutions of 
extremely sensitive differential equations such as those he was using pro-
duced diverging results due to rounding-off errors made by the computer 
system. His discovery was published in a meteorological journal where it 
remained unnoticed for many years. 
Fractals 
While in principle deterministic chaotic systems are unpredictable 
because of their sensitivity to initial conditions, the statistics of their 
behavior can be studied. Consider, for example, the chaos laws that 
describe the evolution of weather: while the weather is basically unpre-
dictable over long periods of time, long-run simulations are used to pre-
dict the statistics of weather. 
It was discovered that probability distributions originating from cha-
otic systems exhibit fat tails in the sense that very large, extreme events 
have nonnegligible probabilities.5 It was also discovered that chaotic sys-
tems exhibit complex unexpected behavior. The motion of chaotic sys-
tems is often associated with self-similarity and fractal shapes. 
Fractals were introduced in the 1960s by Benoit Mandelbrot, a 
mathematician working at the IBM research center in Yorktown Heights, 
New York. Starting from the empirical observation that cotton price 
time-series are similar at different time scales, Mandelbrot developed a 
powerful theory of fractal geometrical objects. Fractals are geometrical 
objects that are geometrically similar to part of themselves. Stock prices 
exhibit this property insofar as price time-series look the same at differ-
ent time scales. 
Chaotic systems are also sensitive to changes in their parameters. In 
a chaotic system, only some regions of the parameter space exhibit cha-
otic behavior. The change in behavior is abrupt and, in general, it can-
not be predicted analytically. In addition, chaotic behavior appears in 
systems that are apparently very simple. 
While the intuition that chaotic systems might exist is not new, the 
systematic exploration of chaotic systems started only in the 1970s. The 
discovery of the existence of nonlinear chaotic systems marked a con-
ceptual crisis in the physical sciences: it challenges the very notion of the 
applicability of mathematics to the description of reality. Chaos laws 
are not testable on a large scale; their applicability cannot be predicted 
5 See W. Brock, D. Hsieh, and B. LeBaron, Nonlinear Dynamics, Chaos, and Insta-
bility (Cambridge, MA: MIT Press, 1991) and D. Hsieh, “Chaos and Nonlinear Dy-
namics: Application to Financial Markets,” Journal of Finance 46 (1991), pp. 1839– 
1877. 

259 
Differential Equations and Difference Equations 
analytically. Nevertheless, the statistics of chaos theory might still prove 
to be meaningful. 
The economy being a complex system, the expectation was that its 
apparently random behavior could be explained as a deterministic cha-
otic system of low dimensionality. Despite the fact that tests to detect 
low-dimensional chaos in the economy have produced a substantially 
negative response, it is easy to make macroeconomic and financial 
econometric models exhibit chaos.6 As a matter of fact, most macroeco-
nomic models are nonlinear. Though chaos has not been detected in eco-
nomic time-series, most economic dynamic models are nonlinear in 
more than three dimensions and thus potentially chaotic. At this stage 
of the research, we might conclude that if chaos exists in economics it is 
not of the low-dimensional type. 
PARTIAL DIFFERENTIAL EQUATIONS 
To illustrate the notion of a partial differential equation (PDE), let’s 
start with equations in two dimensions. A n-order PDE in two dimen-
sions x,y is an equation of the form 
∂( )

∂f ∂f 
i f 
 
, , ------, -----,  ,  -------------------------------= 0 0  k
i
≤≤ 
, 
F x  y  
… 
≤
≤
 
, 
0 i
n
k
–

∂x ∂y 
∂( )x∂(i
k)y 
A solution of the previous equation will be any function that satisfies 
the equation. 
In the case of PDEs, the notion of initial conditions must be 
replaced with the notion of boundary conditions or initial plus bound-
ary conditions. Solutions will be defined in a multidimensional domain. 
To identify a solution uniquely, the value of the solution on some sub-
domain must be specified. In general, this subdomain will coincide with 
the boundary (or some portion of the boundary) of the domain. 
Diffusion Equation 
Different equations will require and admit different types of boundary 
and initial conditions. The question of existence and uniqueness of solu-
6 See W.A. Brock, W.D. Dechert, J.A. Scheinkman, and B. LeBaron, “A Test for In-
dependence Based on the Correlation Dimension,” Econometric Reviews, 15(3) 
(1996); and W. Brock and C. Hommes, “A Rational Route to Randomness,” Econo-
metrica 65 (1997), pp. 1059–1095. 

260 
The Mathematics of Financial Modeling and Investment Management 
tions of PDEs is a delicate mathematical problem. We can only give a 
brief account by way of an example. 
Let’s consider the diffusion equation. This equation describes the 
propagation of the probability density of stock prices under the ran-
dom-walk hypothesis: 
∂f 
2 ∂2f 
---- = a --------
∂t 
∂x 2 
The Black-Scholes equation, which describes the evolution of option 
prices (see Chapter 15), can be reduced to the diffusion equation. 
The diffusion equation describes propagating phenomena. Call 
f(t,x) the probability density that prices have value x at time t. In 
finance theory, the diffusion equation describes the time-evolution of the 
probability density function f(t,x) of stock prices that follow a random 
walk. 7 It is therefore natural to impose initial and boundary conditions 
on the distribution of prices. 
In general, we distinguish two different problems related to the diffu-
sion equation: the first boundary value problem and the Cauchy initial 
value problem, named after the French mathematician Augustin Cauchy 
who first formulated it. The two problems refer to the same diffusion 
equation but consider different domains and different initial and bound-
ary conditions. It can be demonstrated that both problems admit a 
unique solution. 
The first boundary value problem seeks to find in the rectangle 0 ≤x 
≤l, 0 ≤t ≤T a continuous function f(t,x) that satisfies the diffusion equa-
tion in the interior Q of the rectangle plus the following initial condition, 
f(0, x) = φ x
x
l
( ), 0 ≤
≤
 
and boundary conditions, 
( 
( ), f t  l) = f2 t
t
T
f t, 0) = f1 t
( , 
( ), 0 ≤
≤
 
The functions f1, f2 are assumed to be continuous and f1(0) = φ(0), f2(0) 
= φ(l). 
The Cauchy problem is related to an infinite half plane instead of a 
finite rectangle. It is formulated as follows. The objective is to find for 
7 In physics, the diffusion equation describes phenomena such as the diffusion of par-
ticles suspended in some fluid. In this case, the diffusion equation describes the den-
sity of particles at a given moment at a given point. 

261 
Differential Equations and Difference Equations 
any x and for t ≥0 a continuous and bounded function f(t,x) that satis-
fies the diffusion equation and which, for t = 0, is equal to a continuous 
and bounded function f(0,x) = φ(x), ∀x. 
Solution of the Diffusion Equation 
The first boundary value problem of the diffusion equation can be 
solved exactly. We illustrate here a widely used method based on the 
separation of variables which is applicable if the boundary conditions 
on the vertical sides vanish (that is, if f1(t) = f2(t) = 0). The method 
involves looking for a tentative solution in the form of a product of two 
functions, one that depends only on t and the other that depends only 
on x: f(t,x) = h(t)g(x). 
If we substitute the previous tentative solution in the diffusion equation 
∂f 
2 ∂2f 
---- = a --------
∂t 
∂x 2 
we obtain an equation where the left side depends only on t while the 
right side depends only on x: 
dh t
( )
-------------g x
( )-----------------
( ) ( ) = a 2h t d2 g x
dt 
dx2 
( )  1
2d2 g x
dh t
( )  1 
---------------------- = a ---------------------------
dt
h t
dx2 g x
( )  
( )  
This condition can be satisfied only if the two sides are equal to a con-
stant. The original diffusion equation is therefore transformed into two 
ordinary differential equations: 
1 dh t( )  
( )
----- ------------- = bh t
2 dt
a 
d2 g x
( )  
( )
----------------- = bg x
dx2 

262 
The Mathematics of Financial Modeling and Investment Management 
with boundary conditions g(0) = g(l) = 0. From the above equations and 
boundary conditions, it can be seen that b can assume only the negative 
values, 
2
k2π
b = – -----------, k = 1 2
,
, … 
l2 
while the functions g can only be of the form 
kπ 
g x
( ) = 
sin------x
Bk
l 
Substituting for h, we obtain 
2
2 
a k2π
( ) = Bk′ exp – ----------------- t 
 
l2 
 
h t
Therefore, we can see that there are denumerably infinite solutions of 
the diffusion equation of the form 
a 2k2π2  
kπ
fk(t x) = 
exp– ----------------- tsin ------x
, 
Ck
 
l2 
 
l 
All these solutions satisfy the boundary conditions f(t,0) = f(t,l) = 0. By 
linearity, we know that the infinite sum 
∞ 
∞
a 2k1π2  
kπ
( , 
,
f t x  ) = ∑fk(t x) = ∑Ck exp– ----------------- tsin ------x 
 
l2 
 
l
k = 1 
k = 1 
will satisfy the diffusion equation. Clearly f(t,x) satisfies the boundary 
conditions f(t,0) = f(t,l) = 0. In order to satisfy the initial condition, 
given that φ(x) is bounded and continuous and that φ(0) = φ(l) = 0, it can 
be demonstrated that the coefficients Cs can be uniquely determined 
through the following integrals, which are called the Fourier integrals: 

263 
Differential Equations and Difference Equations 
L 
2 
πk  
Ck = ---∫φ ξ
( )sin ------ξdξ
L 
L 
0 
The previous method applies to the first boundary value problem 
but cannot be applied to the Cauchy problem, which admits only an ini-
tial condition. It can be demonstrated that the solution of the Cauchy 
problem can be expressed in terms of a convolution with a Green’s func-
tion. In particular, it can be demonstrated that the solution of the 
Cauchy problem can be written in closed form as follows: 
1 
∞ 
( )  
(x – ξ)2 
( , 
----------exp– -------------------dξ 
t 
 
4t 
 
f t  x) = ---------- ∫
φ ξ
2 π–∞ 
for t > 0 and f(0,x) = φ(x). It can be demonstrated that the Black-Scholes 
equation (see Chapter 15), which is an equation of the form 
∂f 
1
2 ∂2f 
∂f 
---- + --σ2 x -------- + rx------ – rf = 0 
∂x
∂t 
2 
∂x 2 
can be reduced through transformation of variables to the standard dif-
fusion equation to be solved with the Green’s function approach. 
Numerical Solution of PDEs 
There are different methods for the numerical solution of PDEs. We 
illustrate the finite difference methods which are based on approximat-
ing derivatives with finite differences. Other discretization schemes, 
such as finite elements and spectral methods are possible but, being 
more complex, they go beyond the scope of this book. 
Finite difference methods result in a set of recursive equations when 
applied to initial conditions. When finite difference methods are applied 
to boundary problems, they require the solution of systems of simulta-
neous linear equations. PDEs might exhibit boundary conditions, initial 
conditions or a mix of the two. 
The Cauchy problem of the diffusion equation is an example of initial 
conditions. The simplest discretization scheme for the diffusion equation 
replaces derivatives with their difference quotients. As for ordinary differ-
ential equations, the discretization scheme can be written as follows: 

264 
The Mathematics of Financial Modeling and Investment Management 
∂f 
f t + ∆t, x) – f t x  )
( 
( ,
---- ≈ ------------------------------------------------
∂t 
∆t
∂2f 
f t x  + ∆x) – 2f t x  ) + f t x  – ∆x)
( , 
( ,
( ,
-------- ≈ ----------------------------------------------------------------------------------------
∂x 2 
(∆x)2 
In the case of the Cauchy problem, this approximation scheme 
defines the forward recursive algorithm. It can be proved that the algo-
rithm is stable only if the Courant-Friedrichs-Lewy (CFL) conditions 
(∆x)2 
∆t < --------------
2a 2 
are satisfied. 
Different approximation schemes can be used. In particular, the for-
ward approximation to the derivative used above could be replaced by 
centered approximations. Exhibit 9.5 illustrates the solution of a Cauchy 
problem for initial conditions that vanish outside of a finite interval. The 
simulation shows that solutions diffuse in the entire half space. 
EXHIBIT 9.5 
Solution of the Cauchy Problem by the Finite Difference Method 

265 
Differential Equations and Difference Equations 
EXHIBIT 9.6 
Solution of the First Boundary Problem by the Finite Difference Method 
Applying the same discretization to a first boundary problem would 
require the solution of a system of linear equations at every step. 
Exhibit 9.6 illustrates this case. 
SUMMARY
 ■ Derivatives can be combined to form differential equations.
 ■ Differential equations are conditions that must be satisfied by their 
solutions.
 ■ Differential equations generally admit infinite solutions.
 ■ Initial or boundary conditions are needed to identify solutions uniquely.
 ■ Differential equations are the key mathematical tools for the develop-
ment of modern science; in finance they are used in arbitrage pricing, to 
define stochastic processes, and to compute the time evolution of aver-
ages.
 ■ Ordinary differential equations include only total derivatives; partial 
differential equations include partial derivatives.
 ■ Differential equations can be solved in closed form or with numerical 
methods. 

266 
The Mathematics of Financial Modeling and Investment Management
 ■ Finite difference methods approximate derivatives with difference quo-
tients.
 ■ Initial conditions yield recursive algorithms.
 ■ Boundary conditions require the solution of linear equations. 


## Stochastic Differential Equations

CHAPTER 10 
Stochastic Differential Equations 
C
hapter 8 introduced stochastic integrals, a mathematical concept 
used for defining stochastic differential equations, the subject of this 
chapter. Stochastic differential equations solve the problem of giving 
meaning to a differential equation where one or more of its terms are 
subject to random fluctuations. For instance, consider the following 
deterministic equation: 
dy
------ = f t( )y
dt 
We know from our discussion on differential equations (Chapter 9) 
that, by separating variables, the general solution of this equation can 
be written as follows: 
y = A exp[ f t( ) t
d ]
∫ 
A stochastic version of this equation might be obtained, for instance, by 
perturbing the term f, thus resulting in the “stochastic differential equa-
tion” 
------ = [f t +
dy 
( )  ε]dt 
y 
where ε is a random noise process. 
As with stochastic integrals, in defining stochastic differential equa-
tions it is necessary to adopt an ensemble view: The solution of a stochas-
tic differential equation is a stochastic process, not a single function. We 
267 

268 
The Mathematics of Financial Modeling and Investment Management 
will first provide the basic intuition behind stochastic differential equa-
tions and then proceed to formally define the concept and the properties. 
THE INTUITION BEHIND STOCHASTIC DIFFERENTIAL EQUATIONS 
Let’s go back to the equation 
------ = [f t +
dy 
( )  ε]y
dt 
where ε is a continuous-time noise process. It would seem reasonable to 
define a continuous-time noise process informally as the continuous-
time limit of a zero-mean, IID sequence, that is, a sequence of indepen-
dent and identically distributed variables with zero mean (see Chapter 
6). In a discrete time setting, a zero-mean, IID sequence is called a white 
noise. We could envisage defining a continuous-time white noise as the 
continuous-time limit of a discrete-time white noise. Each path of ε is a 
function of time ε(⋅,ω). It would therefore seem reasonable to define the 
solution of the equation pathwise, as the family of functions that are 
solutions of the equations, 
------ = [f t +
dy 
( )  ε(t ω 
, )]y
dt 
where each equation corresponds to a specific white noise path. 
However this definition would be meaningless in the domain of 
ordinary functions. In other words, it would generally not be possible to 
find a family of functions y(⋅,ω) that satisfy the above equations for each 
white-noise path and that form a reasonable stochastic process. 
The key problem is that it is not possible to define a white noise pro-
cess as a zero-mean stationary stochastic process with independent 
increments and continuous paths. Such a process does not exist in the 
domain of ordinary functions.1 In discrete time the white noise process 
is obtained as the first-difference process of a random walk. Anticipat-
ing concepts that will be developed in Chapter 12 on time series analy-
sis, the random walk is an integrated nonstationary process, while its 
first-difference process is a stationary IID sequence. 
1 It is possible to define a “generalized white noise process” in the domain of “tem-
pered distributions.” See Bernd Oksendal, Stochastic Differential Equations: Third 
Edition (Berlin: Springer, 1992). 

269 
Stochastic Differential Equations 
The continuous-time limit of the random walk is the Brownian 
motion. However the paths of a Brownian motion are not differentiable. 
As a consequence, it is not possible to take the continuous-time limit of 
first differences and to define the white noise process as the derivative of 
a Brownian motion. In the domain of ordinary functions in continuous 
time, the white noise process can be defined only through its integral, 
which is the Brownian motion. The definition of stochastic differential 
equations must therefore be recast in integral form. 
A sensible definition of a stochastic differential equation must 
respect a number of constraints. In particular, the solution of a stochas-
tic differential equation should be a “perturbation” of the associated 
deterministic equation. In the above example, for instance, we want the 
solution of the stochastic equation 
------ = [f t +
dy 
( )  ε(t ω 
, )]dt 
dy 
to be a perturbation of the solution 
y = A exp( f t( ) t
d )
∫ 
of the associated deterministic equation 
dy 
( )dt
------ = f t
y 
In other words, the solution of a stochastic differential equation should 
tend to the solution of the associated deterministic equation in the limit 
of zero noise. In addition, the solutions of a stochastic differential equa-
tion should be the continuous-time limit of some discrete-time process 
obtained by discretization of the stochastic equation. 
A formal solution of this problem was proposed by Kyosi Itô in the 
1940s and, in a different setting, by Ruslan Stratonovich in the 1960s. 
Itô and Stratonovich proposed to give meaning to a stochastic differen-
tial equation through its integral equivalent. The Itô definition proceeds 
in two steps: in the first step, Itô processes are defined; in the second 
step, stochastic differential equations are defined. 
■ Step 1: Definition of Itô processes. Given two functions ϕ(t ω 
, ) and 
ψ(t ω 
, ) that satisfy usual conditions to be defined later, an Itô pro-
cess—also called a stochastic integral—is a stochastic process of the 
form: 

270 
The Mathematics of Financial Modeling and Investment Management 
t
t 
(
Z t ω 
, ) = ϕ( s ω 
, ) s
d + ∫ψ( s ω 
, ) dB ( s ω 
, )
∫ 
s 
0
0 
An Itô process is a process that is the result of the sum of two sum-
mands: the first is an ordinary integral, the second an Itô integral. Itô 
processes are stable under smooth maps, that is, any smooth function 
of an Itô process is an Itô process that can be determined through the 
Itô formula (see Itô processes below).
 ■ Step 2: Definition of stochastic differential equations. As we have seen, 
it is not possible to write a differential equation plus a white-noise term 
which admits solutions in the domain of ordinary functions. However 
we can meaningfully write an integral stochastic equation of the form 
t
t 
(
,
X t ω 
, ) = ϕ( s X) s
d + ∫ψ( s X
,
) dB
∫ 
s 
0
0 
It can be demonstrated that this equation admits solutions in the 
sense that, given two functions ϕ and ψ , there is a stochastic process X 
that satisfies the above equation. We stipulate that the above integral 
equation can be written in differential form as follows: 
(
,
,
dX t ω 
, ) = ϕ( t X) t
d + ψ( t X) dBt 
Note that this is a definition; a stochastic differential equation 
acquires meaning only through its integral form. In particular, we can-
not divide both terms by dt and rewrite the equation as follows: 
(
dX t ω 
, ) 
dBt 
---------------------- = ϕ( t X) + ψ( t X) --------
dt 
,
, 
t
d 
The above equation would be meaningless because the Brownian 
motion is not differentiable. This is the difficulty that precludes writ-
ing stochastic differential equations adding white noise pathwise. The 
differential notation of a stochastic differential equation is just a 
shorthand for the integral notation. 
However we can consider a discrete approximation: 
,
,
∆ X( t ω 
, ) = ϕ *( t X)∆ t + ψ *( t X)∆ Bt 

271 
Stochastic Differential Equations 
,
,
Note that in this approximation the functions ϕ *( t X) , ψ *( t X) will 
,
,
not coincide with the functions ϕ( t X) , ψ( t X) . Using the latter would 
(in general) result in a poor approximation. 
The following sections will define Itô processes and stochastic dif-
ferential equations and study their properties. 
ITÔ PROCESSES 
Let’s now formally define Itô processes and establish key properties, in 
particular the Itô formula. In the previous section we stated that an Itô 
process is a stochastic process of the form 
t
t 
(
( 
( 
B(
Z t ω 
, ) = a s ω 
, ) ds + ∫ b s ω 
, ) d
s ω 
, )
∫ 
0
0 
To make this definition rigorous, we have to state the conditions 
under which (1) the integrals exist and (2) there is no anticipation of 
information. Note that the two functions a and b might represent two 
stochastic processes and that the Riemann-Stieltjes integral might not 
exist for the paths of a stochastic process. We have therefore to demon-
strate that both the Itô integral and the ordinary integral exist. To this 
end, we define Itô processes as follows. 
Suppose that a 1-dimensional Brownian motion Bt is defined on a 
probability space (Ω ,ℑ ,P) equipped with a filtration ℑ . The filtration
t
might be given or might be generated by the Brownian motion B . Sup-
t
pose that both a and b are adapted to ℑ t and jointly measurable in ℑ × R. 
Suppose, in addition, that the following two integrability conditions hold: 
t 
P
b2( s ω 
, ) ds < ∞ for all t ≥ 0 = 1
∫ 
0 
and 
t 
P
 a s ω 
, )
( 
ds < ∞ for all t ≥ 0 = 1
∫ 
0 
These conditions ensure that both integrals in the definition of Itô pro-
cesses exist and that there is no anticipation of information. We can 
therefore define the Itô process as the following stochastic process: 

272 
The Mathematics of Financial Modeling and Investment Management 
t
t 
(
( 
(
Z t  ω
, ) = a s  ω
, ) s
d + ∫ b s  ω
, ) dB ( s ω
, )
∫ 
s 
0
0 
Itô processes can be written in the shorter differential form as 
dZt = adt + bdBt 
It should be clear that the latter formula is just a shorthand for the inte-
gral definition. 
THE 1-DIMENSIONAL ITÔ FORMULA 
One of the most important results concerning Itô processes is a formula 
established by Itô that allows one to explicitly write down an Itô process 
which is a function of another Itô process. Itô’s formula is the stochastic 
equivalent of the change-of-variables formula of ordinary integration. 
We will proceed in two steps. First we will introduce Itô’s formula for 
functions of Brownian motion and then for functions of general Itô pro-
cesses. Suppose that the function g(t,x) is twice continuously differentia-
ble in [0,∞ ) × R and that Bt is a one-dimensional Brownian motion. The 
function Yt = g(t,Bt) is a stochastic process. It can be demonstrated that 
the process Yt = g(t,Bt) is an Itô process of the following form 
∂ g 
1 ∂ 2 g 

∂ g
dYt =  -----( t Bt) + -- --------( t Bt) dt + ------( t Bt) dBt
∂ t , 
2∂ x 2 ,
 
∂ x , 
The above is Itô’s formula in the case the underlying process is a Brown-
ian motion. For example, let’s suppose that g(t,x) = x2. In this case we 
can write 
∂ g 
∂ g 
∂ 2 g
----- = 0 , ------ = 2x , -------- = 2 
∂ t 
∂ x 
∂ x 2 
2
Inserting the above in Itô’s formula we see that the process Bt can be 
represented as the following Itô process 
dYt = dt + 2BtdBt 
or, explicitly in integral form 

273 
Stochastic Differential Equations 
t 
Yt = t + 2∫B dB
s
s 
0 
The nonlinear map g(t,x) = x2 introduces a second term in dt. Note that 
we established the latter formula at the end of Chapter 8 in the form 
t 
1
2
1
B dB
= --Bt – --t
s
∫ s 
2
2 
0 
Let’s now generalize Itô’s formula. 
Suppose that Xt is an Itô process given by dXt = adt + bdBt. As Xt is 
a stochastic process, that is, a function X(t,ω) of both time and the 
state, it makes sense to consider another stochastic process Yt, which is 
a function of the former, Yt = g(t,Xt). Suppose that g is twice continu-
ously differentiable on [0,∞) × R. 
It can then be demonstrated (we omit the detailed proof) that Yt is 
another Itô process that admits the representation 
∂g 
1 ∂2 g
dYt = -----
∂g-(t Xt)dt + ------(t Xt)dXt + -- --------(t Xt)(dXt)2 
,
2
∂t 
,
∂x 
, 
2∂x 
where differentials are computed formally according to the rules2 
dt ⋅ dt = dt ⋅ dBt = dBt ⋅ dt = 0, dBt ⋅ dBt = dt 
Itô’s formula can be written (perhaps more) explicitly as 
∂g 
∂g 
1 ∂2 g 
∂g
dYt = ----- + ------a + -- --------b2
 
dt + ------bdBt
∂t 
∂x 
2 

∂x
2∂x 
This formula reduces to the ordinary formula for the differential of a com-
pound function in the case where b = 0 (that is, when there is no noise). 
As a second example of application of Itô’s formula, consider the 
geometric Brownian motion: 
dXt = µXtdt + σXtdBt 
2 These rules are known as the Box algebra. 

274 
The Mathematics of Financial Modeling and Investment Management 
where µ ,σ are real constants, and consider the map g(t,x) = log x. In this 
case, we can write 
∂ g 
∂ g 
1 ∂ 2 g 
1 
----- = 0 , ------ = -- , -------- = -----
2
∂ t 
∂ x
x ∂ x 2 
x 
and Itô’s formula yields 
1
dYt = dlog X = 
µ – --σ 2 dt + σ dBt
t 
2 
 
STOCHASTIC DIFFERENTIAL EQUATIONS 
An Itô process defines a process Z(t,ω ) as the sum of the time integral of 
the process a(t,ω ) plus the Itô integral of the process b(t,ω ). Suppose 
that two functions ϕ (t,x), ψ (t,x) that satisfy conditions established 
below are given. Given an Itô process X(t,ω ), the two processes ϕ (t,X), 
ψ (t,X) admit respectively a time integral and an Itô integral. It therefore 
makes sense to consider the following Itô process: 
t
t 
( 
,
( 
,
(
Z t ω
, ) = ϕ[ s X s ω
, )] ds + ∫ψ[ s X s ω
, )] dB
∫ 
s 
0
0 
The term on the right side transforms the process X into a new process 
Z. We can now ask if there are stochastic processes X that are mapped 
into themselves such that the following stochastic equation is satisfied: 
t
t 
( 
,
( 
,
(
X t ω
, ) = ϕ[ s X s ω
, )] ds + ∫ψ[ s X s ω
, )] dB
∫ 
s 
0
0 
The answer is positive under appropriate conditions. It is possible 
to prove the following theorem of existence and uniqueness. Suppose 
that a 1-dimensional Brownian motion Bt is defined on a probability 
,
,
 
P) equipped with a filtration ℑ t and that Bt is adapted to
space (Ωℑ 
the filtration ℑ t. Suppose also that the two measurable functions ϕ (t,x), 
ψ (t,x) map [0,T] × R → R and that they satisfy the following conditions: 
2 
2 
) 2
ϕ( t x)
, 
+ 
,
ψ( t x) ≤ C( 1 + x 
, t ∈[ 0, T] , x ∈ R 

275 
Stochastic Differential Equations 
and 
ϕ( t x)
, 
– ϕ( t y) +
, 
ψ( t x)
, 
– ψ( t y) ≤ D x  – y
,
( 
) , t ∈[ 0, T] , x ∈ R 
for appropriate constants C,D. The first condition is known as the lin-
ear growth condition, the last condition is the Lipschitz condition that 
we encountered in ordinary differential equation (see Chapter 9). Sup-
pose that Z is a random variable independent of the σ -algebra ℑ gener-
∞
2
ated by Bt for t ≥ 0 such that E Z
( 
) < ∞ . Then there is a unique 
stochastic process X, defined for 0 ≤ t ≤ T, with time-continuous paths 
such that X0 = Z and such that the following equation is satisfied: 
t
t 
X t ω 
, ) = X0 + ϕ[ s X  s  ω 
, )] s
d + ψ[ s X  s  ω 
, )] dB
( 
,
( 
∫
,
( 
s
∫ 
0
0 
The process X is called a strong solution of the above equation. 
The above equation can be written in differential form as follows: 
( 
,
( 
,
(
dX t ω 
, ) = ϕ[ t X  t  ω 
, )] t
d + ψ[ t X  t  ω 
, )] dBt 
The differential form does not have an independent meaning; a differen-
tial stochastic equation is just a short albeit widely used way to write 
the integral equation. 
The key requirement of a strong solution is that the filtration ℑ t is 
given and that the functions ϕ ,ψ are adapted to the filtration ℑ t. From 
the economic (or physics) point of view, this requirement translates the 
notion of causality. In simple terms, a strong solution is a functional of 
the driving Brownian motion and of the “inputs” ϕ ,ψ . A strong solution 
at time t is determined only by the “history” up to time t of the inputs 
and of the random shocks embodied in the Brownian motion. 
These conditions can be weakened. Suppose that we are given only 
the two functions ϕ (t,x), ψ (t,x) and that we must construct a process Xt, 
a Brownian motion Bt, and the relative filtration so that the above equa-
tion is satisfied. The equation still admits a unique solution with respect 
to the filtration generated by the Brownian motion B. It is however only 
a weak solution in the sense that, though there is no anticipation of 
information, it is not a functional of a given Brownian motion.3 Weak 
and strong solutions do not necessarily coincide. However, any strong 
solution is also a weak solution with respect to the same filtration. 
3 See, for instance, Ioannis Karatzas and Steven E. Shreve, Brownian Motion and Sto-
chastic Calculus (New York: Springer, 1991). 

276 
The Mathematics of Financial Modeling and Investment Management 
Note that the solution of a differential equation is a stochastic pro-
cess. Initial conditions must therefore be specified as a random variable 
and not as a single value as for ordinary differential equations. In other 
words, there is an initial value for each state. It is possible to specify a sin-
gle initial value as the initial condition of a stochastic differential equa-
tion. In this case the initial condition is a random variable where the 
probability mass is concentrated in a single point. 
We omit the detailed proof of the theorem of uniqueness and exist-
ence. Uniqueness is proved using the Itô isometry and the Lipschitz con-
dition. One assumes that there are two different solutions and then 
demonstrates that their difference must vanish. The proof of existence 
of a solution is similar to the proof of existence of solutions in the 
domain of ordinary equations. The solution is constructed inductively 
by a recursive relationship of the type 
t
t 
(
X k + 1)(t ω 
, ) = ϕ[s Xk(s ω 
, )] s
d + ∫ψ[s Xk(s ω 
, )]dB
∫ 
,
, 
s 
0
0 
It can be shown that this recursive relationship produces a sequence of 
processes that converge to the unique solution. 
GENERALIZATION TO SEVERAL DIMENSIONS 
The concepts and formulas established so far for Itô (and Stratonovich) 
integrals and processes can be extended in a straightforward but often cum-
bersome way to multiple variables. The first step is to define a d-dimen-
sional Brownian motion. 
Given a probability space (Ωℑ
,
, P) equipped with a filtration {ℑt}, a 
d-dimensional standard Brownian motion Bt(ω), is a stochastic process 
with the following properties:
 ■ Bt(ω) is a d-dimensional process defined over the probability space
(Ωℑ
,
, P) that takes values in Rd .
 ■ Bt(ω) has continuous paths for 0 ≤t ≤∞.
 ■ B0(ω) = 0.
 ■ Bt(ω) is adapted to the filtration ℑt.
 ■ The increments Bt(ω) – Bs(ω) are independent of the σ-algebra ℑand
s 
have a normal distribution with mean zero and covariance matrix (t – 
s)Id, where Id is the identity matrix. 

277 
Stochastic Differential Equations 
The above conditions state that the standard Brownian motion is a sto-
chastic process that starts at zero, has continuous paths, and has nor-
mally distributed increments whose variances grow linearly with time. 
The next step is to extend the definition of the Itô integral in a 
multi-dimensional environment. This is again a straightforward but 
cumbersome extension of the 1-dimensional case. Suppose that the fol-
lowing r× d-dimensional matrix is given: 
v 
v11 · v1d 
· 
· 
· 
vr1 
· vrd 
= 
where each entry vij = vij(t,ω ) satisfies the following conditions: 
1. vij are Bd 
ℑ 
× 
measurable. 
2. vij are ℑ t-adapted. 
t 
3. P ∫(
)
vij
2 s
d < ∞ for all t ≥ 0 = 1 . 
0 
Then, we define the multidimensional Itô integral 
t 
t v11 · v1d 
B
d 1 
v B
d 
= ∫ ·
·
· 
·
∫ 
0
0 vr1
· vrd 
B
d
d 
as the r-dimensional column vector whose components are the following 
sums of 1-dimensional Itô integrals: 
d
t 
∑∫ vij( s ω 
, ) dBj( s ω 
, ) 
i = 10 
Note that the entries of the matrix are functions of time and state: 
they form a vector of stochastic processes. Given the previous definition 
of Itô integrals, we can now extend the definition of Itô processes to the 
multidimensional case. Suppose that the functions u and v satisfy the 
conditions established for the one-dimensional case. We can then form a 
multidimensional Itô process as the following vector of Itô processes: 

278 
The Mathematics of Financial Modeling and Investment Management 
dX1 = u1dt + v11dB1 + … + v1ddBd 
… 
dX1r = u dt + vr1dB1 + … + vrddBd
r
or, in matrix notation 
dX = udt + vdB 
After defining the multidimensional Itô process, multidimensional sto-
chastic equations are defined in differential form in matrix notation as 
follows: 
,
dX( t ω
, ) = u[ t X1( t ω
, ), …, Xd( t ω
, )] dt 
,
+ v[ t X1( t ω
, ), …, Xd( t ω
, )] dB 
Consider now the multidimensional map: g(t,x) ≡ [g1(t,x), …, 
gd(t,x)], which maps the process X into another process Y = g(t,X). It 
can be demonstrated that Y is a multidimensional Itô process whose 
components are defined according to the following rules: 
,
,
∂ gk( t X) 
∑
∂ gk( t X) 
1 
∂ 2 gk( t X)
dYk = -----------------------dt + 
-----------------------dXi + --
--------------------------dXidXj
∂ t 
∂ Xi 
2∑∂ Xi∂
, 
X
i j
j
i 
, 
dBidB = 1 if  i = j, 0 if  i
j
≠ , dBidt = dtdBi = 0
j 
SOLUTION OF STOCHASTIC DIFFERENTIAL EQUATIONS 
It is possible to determine an explicit solution of stochastic differential 
equations in the linear case and in a number of other cases that can be 
reduced to linear equations through functional transformations. Let’s 
first consider linear stochastic equations of the form: 
dXt = [ A t
( )] dt + σ( )  
t dBt , 0 ≤ t < ∞
( )  Xt + a t
X0 = ξ 
where B is an r-dimensional Brownian motion independent of the d-
dimensional initial random vector ξ and the (d× d), (d× d), (d× r) matrices 
A(t), a(t), σ (t) are nonrandom and time dependent. 

279 
Stochastic Differential Equations 
The simplest example of a linear stochastic equation is the equation 
of an arithmetic Brownian motion with drift, written as follows: 
dXt = µdt + σdBt , 0 ≤t < ∞ 
X0 = ξ, µ, σ constants 
In linear equations of this type, the stochastic part enters only in an 
additive way through the terms σij(t)dBt. The functions σ(t) are some-
times called the instantaneous variances and covariances of the process. 
In the example of the arithmetic Brownian motion, µ is called the drift 
of the process and σ the volatility of the process. 
It is intuitive that the solution of this equation is given by the solu-
tion of the associated deterministic equation, that is, the ordinary differ-
ential equation obtained by removing the stochastic part, plus the 
cumulated random disturbances. Let’s first consider the associated 
deterministic differential equation 
dx 
------ = A t
+ ( ) , 0 ≤t < ∞
( )x
a
 
t
dt 
where x(t) is a d-dimensional vector with initial conditions x(0) = ξ. 
It can be demonstrated that this equation has an absolutely continu-
ous solution in the domain 0 ≤t < ∞. To find its solution, let’s first con-
sider the matrix differential equation 
dΦ 
------- = A t( )Φ , 0 ≤t < ∞ 
dt 
This matrix differential equation has an absolutely continuous solution 
in the domain 0 ≤t < ∞. The matrix Φ(t) that solves this equation is 
called the fundamental solution of the equation. It can be demonstrated 
that Φ(t) is a nonsingular matrix for each t. Lastly, it can be demon-
strated that the solution of the equation: 
dx 
------ = A t
+ ( ) , 0 ≤t < ∞
( )x
a
 
t
dt 
with initial condition x(0) = ξ, can be written in terms of the fundamen-
tal solution as follows: 

280 
The Mathematics of Financial Modeling and Investment Management 
t 
x t
( ) x 0
s
( ) s
d , 0 ≤t < ∞
( ) = Φ t
( ) + ∫Φ–1( )a s
0 
Let’s now go back to the stochastic equation 
dXt = [A t
( )]dt + σ t
( )Xt + a t
( )dBt , 0 ≤t < ∞ 
X0 = ξ 
Using Itô’s formula, it can be demonstrated that the above linear sto-
chastic equation admits the following unique solution: 
t
t 
X t
( ) ξ  + Φ–1( )a s
s
( )dB
, 0 ≤t < ∞
( ) = Φ t
s
( ) s
d + ∫Φ–1( )σ s
s
∫ 
0
0 
This effectively demonstrates that the solution of the linear stochastic 
equation is the solution of the associated deterministic equation plus the 
cumulated stochastic term 
t 
s
( )dB
∫Φ–1( )σ s
s 
0 
To illustrate this, below we now specialize the above solutions in the 
case of arithmetic Brownian motion, Ornstein-Uhlenbeck processes, and 
geometric Brownian motion. 
The Arithmetic Brownian Motion 
The arithmetic Brownian motion in one dimension is defined by the fol-
lowing equation: 
dXt = µdt + σdBt 
In this case, A(t) = 0, a(t) = µ, σ(t) = σ and the solution becomes 
X = µt + σB 
The Ornstein-Uhlenbeck Process 
The Ornstein-Uhlenbeck process in one dimension is a mean-reverting 
process defined by the following equation: 

281 
Stochastic Differential Equations 
dXt = –αXtdt + σdBt 
It is a mean-reverting process because the drift is pulled back to zero by 
a term proportional to the process itself. In this case, A(t) = –α, a(t) = 0, 
σ(t) = σ and the solution becomes 
∫ 
t 
– α(t
s
– )
Xt = X0 + e – αt + σ e 
dBs 
0 
The Geometric Brownian Motion 
The geometric Brownian motion in one dimension is defined by the fol-
lowing equation: 
dX = µXdt + σXdB 
This equation can be easily reduced to the previous linear case by the 
transformation: 
Y = log X 
Let’s apply Itô’s formula 
∂g 
∂g 
1 ∂2 g 
∂g
dYt = ----- + ------a + -- --------b2
 
dt + ------bdBt
∂t 
∂x 
2 

∂x
2∂x 
where 
∂g 
1 ∂2 g 
1
( ,
g t  x) = logx, -----
∂g- = 0, ----- = --, --------
–
= -----
2
∂t 
∂t
x ∂x 2 
x 
We can then verify that the logarithm of the geometric Brownian motion 
becomes an arithmetic Brownian motion with drift 
1
µ′ = µ – --σ2 
2 
The geometric Brownian motion evolves as a lognormal process: 

282 
The Mathematics of Financial Modeling and Investment Management 
1 
 
Xt = x0exp
µ – --σ2 t + σBt  
 
2 

 
SUMMARY
 ■ Stochastic differential equations give meaning to ordinary differential 
equations where some terms are subject to random perturbation.
 ■ Following Itô and Stratonovich, stochastic differential equations are 
defined through their integral equivalent: the differential notation is 
just a shorthand.
 ■ Itô processes are the sum of a time integral plus an Itô integral.
 ■ Itô processes are closed with respect to smooth maps: a smooth func-
tion of an Itô process is another Itô process defined through the Itô for-
mula.
 ■ Stochastic differential equations are equations established in terms of 
Itô processes.
 ■ Linear equations can be solved explicitly as the sum of the solution of 
the associated deterministic equation plus a stochastic cumulative 
term. 

