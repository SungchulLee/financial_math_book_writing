# Monte Carlo Methods & Simulation

!!! info "Source"
    **Numerical Methods in Finance and Economics** by Paolo Brandimarte, Wiley, 2nd ed., 2006.
    These notes are used for educational purposes.

## Monte Carlo Simulation in Finance

Part IV 
Advanced Optimization 
Models and Methods 

This Page Intentionally Left Blank

I0 
Dynamic Programming 
Dynamic programming is arguably the most powerful principle in optimiza- 
tion and it can be applied to a wide range of problems with radically different 
features. As its name suggests, dynamic programming was originally con- 
ceived as a method to solve dynamic optimization models over time. As such, 
it can be applied to discrete- and continuous-time models, deterministic and 
stochastic models, and finite- and infinite-horizon models. Actually, with a 
little creativity, it can also be applied to non-dynamic problems. For instance, 
it can be used to tackle a combinatorial optimization problem like the knap- 
sack model.’ All of this potential comes with a price. To begin with, dynamic 
programming is a principle, rather than a well-defined and ready-to-use al- 
gorithm. It must be customized to the problem at hand. Furthermore, it 
may be computationally quite expensive. This is not always true: in some 
cases, application of the principle yields quite efficient numerical algorithms, 
or even analytical solutions. Even when dynamic programming does not yield 
the solution itself, it can be most valuable in characterizing its qualitative 
properties, which can provide us with very valuable insights. But in many 
practical cases, straightforward application of the principle is not possible 
because of the so-called “curse-of-dimensionality.” 
Some tricks of the trade can be used to reduce problem dimensionality, 
but dynamic programming is often considered a typically academic concept. 
Nevertheless, there are very good reasons why we have decided to include a 
chapter on this topic. 
’See, e.g., [16]. 
495 

496 
DYNAMIC PROGRAMMING 
0 Having a basic grasp of dynamic programming is needed to understand 
recently developed approaches to price high-dimensional American op- 
tions by Monte Carlo methods. Finite difference and lattice based meth- 
ods are very well suited to price American options, but they do not cope 
well with high-dimensionality. On the other hand, Monte Carlo methods 
deal easily with high-dimensionality, but not with early exercise. Ex- 
ploiting early exercise opportunities optimally requires going backward 
in time, since at each point in the state space we must compare the 
value of immediate exercise with the value of keeping the option, which 
is simply the price of the option at that point. Hence, it would seem 
that one has to chase her tail a bit, since while running a simulation 
forward in time, we should already know the option value. Indeed, until 
a few years ago, it was a common belief that simulation could not be 
applied to American-style options, but the situation has changed. 
0 While a literal application of dynamic programming may be overly diffi- 
cult, approximate strategies have been developed which are very promis- 
ing in terms of their ability to tackle real problems. Clearly, the increase 
in computational power of hardware plays a role here, but it is not the 
only factor. 
0 Understanding dynamic programming also sheds some light on stochas- 
tic programming, which is the topic of next chapter. 
A comprehensive treatment of dynamic programming in one chapter is out 
of the question. Our main aim is to illustrate Monte Carlo methods to price 
American options. A secondary aim is to outline how the idea can be applied 
to portfolio optimization over a finite time horizon. Given our limited scope, 
we will only cover discrete-time and finite-horizon models. In section 10.1 we 
first illustrate the principle behind dynamic programming with the simplest 
example, the shortest path problem in a network. Then, in section 10.2, we 
show the connection between this simple example and more general determin- 
istic sequential decision processes. In this section we get acquainted with the 
dynamic programming principle in a deterministic setting. In section 10.3 we 
illustrate how the principle can be extended to stochastic problems. Finally, a 
regression-based Monte Carlo method to price American options is illustrated 
in section 10.4. 
10.1 THE SHORTEST PATH PROBLEM 
The easiest way to introduce dynamic programming is by considering one of its 
most natural applications, i.e., finding the shortest path in a network. Graph 
and network optimization are not customary topics in Finance or Economics, 
but a quick look at figure 10.1 is enough to understand what we are talking 
about. A network consists of a set of nodes (numbered from 0 to 7 in our 

THE SHORTEST PATH PROBLEM 
497 
\6 
Fig. 10.1 A shortest p i t h  pmI)leiri. 
t.oy example) and a set of arcs joiiiing pairs of nodes. Arcs are labeled by a 
riuiiibcir wliicli can he intcrprctcd as thc arc length (or cost). Our purpose 
is firirlirig H path in t,he network, starting from node 0 and leading to node 
7; such that the pat,h has tota.1 iiiiniinal length. For instance, summing tlie 
iirc kiigths we visit on the path (0, 1, 4, 7 ) :  we see tliat its total length is 18; 
wlieims path (0. I 3, 5 ,  7 )  has lengt,h 16. At each node, we must choose the 
iicxt, iiotlc t,o visit,. We rriay iiiirrictlint,cly apprcciatc that this probleiii bears 
soiw reseriil)lancx: to dyiiamic decision making; given some state we are in. we 
hhoultl dccitlc wliat, to do in order to optiniizc an outcome that depends on 
t,ht: whole path. A greedy decision need not be the optimal one; for instance, 
tlie rlosest node to the starting point 0 in our network is node 2, but there is 
no guararit,cc t,hat t,liis a.rc is on an optiiiial path. 
Of course, we coiild simply enumerate all the possible paths to spot the 
optimal one: here we have just a finite set of alt,ernatives ancl there is no 
iiiiwrtaiiity iiivolved, so the approach is conceptually feasible. However, this 
nppronrli I)rcoiiies quickly infeasihle iii practice, as the network size incrrases. 
So wc must coirie up wit,li some clever way to avoid exhaustive enumeration. 
Dyiiariiic prt)grit1ririiilig is one possible approach to accomplish this aim. It 
is worth rioting that more efficient algorithms are available for the shortest 
pith prol)leiii. h i t  the itlea we illustrate here can he extended to problenis 
ft?aturing infinite state spaces (countable or not) and uncertain data. 
Let n/ = {0,1,2,. . . , N }  be the node set and A be the arc set; let the start 
aiid filial riotlw be 0 and N .  respectively. For simplicity; we assuirie that the 
iirt,work is acyclic arid that the arc lengths crJ: i , j  E N ;  are non-negative: If 
wc Iiatl t,hc possibility of get,t,iiig trappcd iii a loop of negative length arcs, the 
optiinal cost would be --oc ancl we do not want to consider such pathological 
(‘ilSFS. 

498 
DYNAMIC PROGRAMMING 
The starting point is to find a characterization of the optimal solution, that 
can be translated into a constructive algorithm. Let V, be the length of the 
shortest path from node i E hf to node N (denoted by i A N ) .  Assume 
that, for a specific i E N, 
node j lies on the optimal path i 5 N .  Then the 
following property holds: j 
N is a subpath of i 5 N. In other words, the 
optimal solution for a problem is obtained by assembling optimal solutions 
for subproblems. To understand why, consider the decomposition of i -?, N 
into the subpaths i -t j and j + N .  The length of i A N is the sum of the 
lengths of the two subpaths: 
V, = L(i + j )  + L ( j  -+ N). 
(10.1) 
Note that the second subpath is not affected by how we go from i to j. This 
is strongly related to the concept of state in Markovian dynamic systems: 
how we get to state j has no influence on the future. Now, assume that the 
subpath j -+ N is not the optimal path from j to N .  Then we could improve 
the second term of (10.1) by considering the path consisting of i + j followed 
by j -r, N. The length of this new path would be 
L(i + j )  + L(j 
N )  < L(i -+ 
j )  + L ( j  + N) 
= V,, 
which is a contradiction, as we assumed that V, was the optimal path length. 
This observation leads to the following recursive equation for the shortest 
path from a generic node i to the terminal node N: 
(10.2) 
In other words, to find the optimal path from node i to node N, we should 
consider the immediate cost cij of going from i to all of its immediate suc- 
cessors j ,  plus the optimal cost of going from j to the terminal node. Note 
that we do not only consider the immediate cost, as in a greedy decision rule. 
We also add the future cost of the optimal sequence of decisions starting from 
each state we can visit next; this is what makes the approach non myopic. The 
function V, is called cost-to-go or value function and is defined recursively 
by equation (10.2). The value function, for each point in the state space, tells 
us what the future optimal cost would be, if we reach that state and go on 
with an optimal policy. This kind of recursive equation, whose exact form 
depends on the problem at hand, is the heart of dynamic programming and is 
an example of a functional equation. In the shortest path problem, we have 
a finite set of states, and the value function is a vector; in an continuous-state 
model, the value function is an infinite-dimensional object. 
Solving the problem requires finding the value function Vo for the initial 
node, and to do that we should go backward in time.2 We can associate a 
2We are considering here only the backward version of dynamic programming. For the 
shortest path, and other deterministic combinatorial optimization problems, we could also 

THE SHORTEST PATH PROBLEM 
499 
terminal condition VN = 0 to our functional equation. Then we unfold the 
recursion by considering the immediate predecessors i of the terminal node 
N ;  for each of them, finding the optimal path length is trivial, as this is just 
C,N. Then we proceed backward, labeling each node with the corresponding 
value function. In this unstructured network, we may label a node only when 
all of its successors have been labeled; we can always find the correct ordering 
in acyclic networks. 
Example 10.1 Let us find the shortest path for the network depicted in 
Figure 10.1. We have the terminal condition V7 = 0 for the terminal node, 
and we look for its immediate predecessors 4 and 6 (we cannot label node 5 
yet, because node 6 is one of its successors). We have 
v4 = c47 + v7 = 10 + 0 = 10 
v6 = C67 f v7 = 8 f 0 = 8. 
Now we may label node 5: 
v5 =,in{ 
c56 f v6 } =min{ 5 + o  
l + 8  } = 5 .  
c57 + v7 
Then we consider node 3 and its immediate successors 4, 5, and 6: 
c34 + v4 
3+10 
c36 + v6 
1 + 8  
.=.;.in{ 
C 3 5 f f i  } =min{ 
2 + 5  } = 7 .  
By the same token we have: 
~ l = m i n {  c13 + v3 } = m i n i  2 + 7  } = 9  
c14 f v4 
1 + 10 
~2 =min{ c23 + v3 } =min{ 4 + 7  
7 + 5  } = 11 
c25 + v5 
co1 + Vl 
7 f 9  
c02 + v2 
6 +  11 
Vo = min { 
} = min { 
} = 16. 
Apart from getting the optimal length, which is 16, we may find the optimal 
path by looking for the nodes optimizing each single decision, starting from 
node 0: 
o +  1 - - + 3 + 5 - + 7 .  
0 
This might seem like a clumsy approach, but even in our simple shortest path 
problem this is better than an exhaustive enumeration of the alternatives. 
Furthermore, the same idea may be applied when uncertainty is involved and 
the value function is defined as an expected value. 
apply a fornard equation (see, e.g., [3, appendix D]). We consider only backward DP because 
of its relevance in stochastic decision making. 

500 
DYNAMIC PROGRAMMING 
10.2 SEQUENTIAL DECISION PROCESSES 
In this section we generalize the functional equation approach that we have 
just introduced for the shortest path problem. Consider a discrete-time dy- 
namic system modeled by the state equation: 
where xt is the vector of the state variables at the beginning of time interval 
t and ut is the vector of the control variables applied during time interval 
t. No uncertainty is considered here: Given the current value of the state 
variable xt, after selecting the control variable ut we know exactly what the 
future state will be, according to the time-varying dynamics described by the 
ht functions. If system dynamics does not change in time, we can drop the 
subscript t from ht. The initial state xo is given and we consider a finite 
time horizon from t = 0 to t = T. We want to find an optimal sequence of 
controls (u;, u;, . . . , u>-~), 
to which an optimal trajectory (x;, x;, . . . , x;) 
corresponds, in such a way as to minimize the objective function: 
T- 1 c 
ft(Xt, .t) + FT(XT). 
We have assumed an additive form, which makes the application of the dy- 
namic programming principle easier, but other forms lend themselves to a 
decomposition approach. The objective function consists of a trajectory cost 
and a cost linked to the terminal state. The optimization must be carried out 
subject to the dynamic constraints (10.3) and, possibly, to constraints on the 
control variables and/or the state variables. 
(10.4) 
t=l 
Example 10.2 As an example of deterministic sequential decision process 
we consider a stylized consumption-saving problem. We have an initial wealth 
Wo, and we must decide how much to save and how much to consume, at 
time instants t = 0,1,2. . . , T - 1. What we save can be invested at a risk-free 
interest rate T .  Furthermore, we have an income stream over the planning 
horizon. The state variable is Wt, the current wealth level. The control 
variable is immediate consumption Ct; if we rule out borrowing money, we 
must have Ct 5 Wt. The (exogenous) income stream is It. The state dynamics 
is 
Wt+i = (Wt - Ct)( 1 + T )  + It, 
t = 0, 1, . . . , T - 1. 
We may want to maximize an additive utility function including a time dis- 
count factor D < 1: 

SEQUENTlAL DECISION PROCESSES 
501 
where u is some concave utility function and B(.) is the utility from bequest, 
valuing terminal wealth. If we do not consider the utility from bequest, the 
last decision is clearly to consume all available wealth. There is no uncertainty 
in this model, but the concavity of the utility function tends to enforce some 
regularity in the consumption ~ t r e a m . ~  
In some cases, the terminal valuation function B must be selected in such a 
way to overcome myopic behavior due to end-of-horizon effects. This happens 
when our planning horizon is truncated to make the problem manageable or 
to avoid planning for time periods so far that we cannot even characterize 
uncertainty in probabilistic terms. However, infinite time horizon models are 
often used in Economics: 
m 
t =o 
Here, discounting is essential to get a bounded objective function. The average 
cost/profit criterion may be also be used: 
but this more common in Engineering applications. 
0 
This sequential decision problem can be solved by ordinary mathematical 
programming techniques, such as those discussed in chapter 6. However, 
understanding how we can tackle it by dynamic programming is helpful to 
develop approaches which can also be applied in more general settings. 
10.2.1 
The objective function (10.4) is separable, in the sense that, for a given number 
r, the contribution of the last r decision stages depends only on the current 
state X T - ~  
and the r controls U T - ~ ,  . . . , U T - ~ .  Furthermore, a similar sepa- 
ration property (known as Murkovian state property) holds for the trajectory, 
in the sense that the state xt+l reached from xt by applying the control ut 
depends only on xt and ut, and not on the past history XO, . . . , xt-1. AS a 
consequence of such separation properties, we obtain the optimality prin- 
ciple. 
The optimality principle and solving the functional equation 
A n  optimal policy (u;, u;, . . . , u > - ~ )  
is such that, whatever the initial 
state xo and the first control u;, the next controls (u:, . . . , u>-~) 
are 
an optimal policy for the (T - 1)-stage problem with initial state xi, 
obtained by applying the first control u;. 
30ne may actually argue that such a simple additive function does not capture habit for- 
mation effects. 

502 
DYNAMIC PROGRAMMING 
Therefore, we may write a recursive functional equation to obtain the optimal 
policy: 
vt(Xt) = min {ft(Xt, 
U t )  + Vt+l(ht(Xt, 4)) 
, 
(10.5) 
where the minimization is possibly carried out taking into account constraints 
on the control variable. This equation is known as Bellman equation, after 
the pioneer in dynamic programming. The value function &(xt) is the total 
cost we incur by applying the optimal policy starting from state xt at time 
t . This is a again a backward functional equation which must be solved to 
obtain the initial value function Vo(x0). 
The functional equation has a boundary condition that helps to start un- 
folding the recursion: 
Then we step back to t = T - 1 and, for each possible state X T - ~ ,  
we solve 
the following optimization problem: 
Ut 
VT (XT ) = FT (XT ) * 
This is, for each value of the state variable XT-1, a possibly constrained 
optimization problem: we have eliminated the dynamic constraint (10.3), but 
we could have constraints on state and/or control variables. Assuming we 
know the value function VT-~ 
(.), we may step back to build the value function 
VT-~(.), 
by solving: 
VT-~(XT-~) 
= min { f ~ - - 2 ( ~ ~ - 2 ,  
U T - 2 )  + VT-l(hT-2(XT-2, 
U T - - 2 ) ) )  
. 
UT--2 
Going backward to the initial state XO, we solve the overall problem, one stage 
at a time. Note that if we knew the whole set of value functions, we could find 
the optimal control at each decision stage, given the current state we observe 
before making our decision. 
We should wonder where this sequential decision problem differs from the 
previous shortest path problem: 
0 the state space is continuous 
0 there is an explicit time dynamics 
0 the set of available controls can be continuous, whereas in the shortest 
path problem the set of control actions was finite, as there was a finite 
set of successor nodes 
Having a continuous state space means that, in principle, we should solve 
an infinite set of optimization problems for each time period. This can be 
avoided in a few lucky cases where we can find an analytical solution, but this 
is the exception rather than the rule. A possible approach is to discretize the 
state space. If we imagine doing that for each time period, we may see some 

SEQUENTIAL DECISION PROCESSES 
503 
'T- 1 
- -  
I
.
 
I 
, 
similarity with the shortest, path problem by looking at figure 10.2, whcre a 
network of discrete states is drawn. In order to emphasize the similarity with 
the shortest path problem: tlie network has been drawn under tlie assumption 
that tlie t,errriinnl sttate x r  is fixed. In this case we see that we have no difficulty 
with labeling nodes as the network is layered. The arc lengths are given by 
tlie cost of the corresponding state transitions. 
Clearly, if we may find a suitable discretization of the state space, we have 
a corriputatioiially feasible approach. But we already know, from chapter 4, 
t,hat. tliscrc:t,iziIig highdimensional state spaces with regular grids niay be dif- 
ficult,. This is known as the curse of dimensionality in dynamic programming. 
Nevertheless, we niay also see tliat the real issue is approximating the value 
fiinction. If we know the set of value functions, or a suitable approximation; 
we can find the optimal control at any point of the state space. Using concept,s 
introduced in section 3.3, we can approximate each value function as a linear 
coin1)iniLtioii of a set of basis functions: 
M 
v,(Xt) = C n k . t 3 k ( X d 1  
(10.6) 
h=1 
where we have assunietl that tlie set of basis functions does not change over 
tirric. hut t,lic set> of wcights ( Y ~ J  does. Hence, an infinite-dirnensional prob- 
l ~ m  
boils down to the finite-dimensional problem of finding a suitable set of 
weights, possibly determined by interpolation or least squares. The quality of 
Fig. 10.2 A sliortcst p t l i  rqmxiitation of a finitc scqueiitinl dccisioii proc:ess (for 
c,liirit,p, not it11 t,riiiisitioiis are slioaii); tho filial stsate is assunled fixcd. 

504 
DYNAMIC PROGRAMMING 
the solution we find depends on our choice of basis functions and on the choice 
of nodes in the state space, which we use to solve the function approximation 
problem. This is not easy and it is rather problem-dependent, but we see that 
the numerical techniques we have considered in the previous chapters, such 
as function approximation and numerical optimization, are building blocks in 
numerical dynamic programming. If we also introduce uncertainty, numerical 
integration comes into play as well. 
10.3 SOLVING STOCHASTIC DECISION PROBLEMS BY DYNAMIC 
PROGRAMMING 
In the deterministic setting, we may find the optimal control sequence and the 
corresponding state trajectory. But in a stochastic problem, the current state 
xt and the control ut we apply do not determine the next state, but only 
its conditional probability distribution. In a discrete-state setting, we may 
introduce a set of controlled transition probabilities. To ease the notation, let 
us assume that the transition probabilities are time-independent: 
(lij(U) = P{Xt+l = j I Xt = j ,  Ut = u}. 
where Xt+l is the next state (a random variable) and we have indexed states 
by integer numbers for conveniency. In the continuous-state case, we may 
think of dynamic equations such as 
Xt+l = hbt, Ut, E t + l ) ,  
(10.7) 
where Et+l is a random shock; this random variable has a subscript t + 1 to 
emphasize that it is realized after we decide the control action u t .  We cannot 
anticipate the control sequence, which is implicitly determined by the solution 
of recursive equations such as 
vt(Xt) = min{f(xt,ut) +Et [Vt+l(h(Xt,Ut,.t+l)])}, 
(10.8) 
This is a straightforward generalization of equation (10.5). In the stochastic 
case, the future cost term is a conditional expectation; the notation E t  points 
out that expectation is carried out with respect to what we know now (the 
current state). 
U t  
Example 10.3 To illustrate (10.7) and (10.8), we may generalize example 
10.2 by including a risky asset in the set of investment opportunities. Assume 
we have a risky asset, whose price S t  follows, in continuous-time, the familiar 
geometric Brownian motion with drift p and volatility u. In discrete-time, we 
have: 
P 
S t + l  = S t e  

SOLVING STOCHASTIC DECISION PROBLEMS BY DYNAMIC PROGRAMMING 
505 
where $' N N ( ( p  - 02/2)6t , od& and 6t is the length of the time step. We 
) 
use here the notation 
to point out what is random at time t, and what is 
not. If we denote by at E [0, 11 the fraction of saved wealth that is invested 
in the risky asset, the wealth dynamics is 
1 
%+I 
%+I 
= (Wt -Ct) 0- 
+ (1 - C y ) ( l + ? - )  
+It. 
[ st 
The recursive Bellman equation is, at time t, 
with terminal condition 
VT(W7-1 = B(WT). 
In deterministic sequential processes, we want the optimal control path. In 
stochastic dynamic programming, what we really need is the set of value 
functions, one for each decision stage. Given the value function, at each 
decision stage we observe the current state and, given the value function, find 
the optimal control by solving a one-step optimization problem. The value 
function is what we need to avoid myopic decisions. Hence, we implicitly 
obtain the optimal control in feedback form: ut = &(xt). 
As we already mentioned, in a continuous-state model the value function 
is an infinite-dimensional object, and we must somehow reduce it to a finite- 
dimensional object. Interpolation or approximation by a set of basis function 
are typically used to this aim. As we have seen in section 3.3, placing nodes is 
important in function approximation. This means that we should devise a grid 
in the state space, and using an evenly spaced one need not be the best idea.4 
In the stochastic case, an additional difficulty is given by the conditional ex- 
pectation in (10.8). If the random shocks are continuously distributed random 
variables, our recursive equation involves a numerical integration problem. As 
we have seen in chapter 4, we may use deterministic or stochastic approaches, 
such as Gaussian quadrature or Monte Carlo sampling. It is important to 
note that here we want to approximate a function defined by an expectation, 
and not just an expected value as typical in option pricing. The following 
example shows how Gaussian quadrature can be extremely valuable in the 
discretization of conditional e~pectation.~ 
4See, e.g., (51 for numerical tricks useful in solving discrete-time DP models. 
5This is strongly linked to scenario generation issues in stochastic programming with re- 
course; see section 11.3. 

506 
DYNAMIC PROGRAMMING 
Example 10.4 Let us consider an extremely stylized asset allocation prob- 
lem. An investor has a current wealth WO that she can invest at a continuously 
compounded risk free rate r, locking a total return R = eTT over a time hori- 
zon of length T. As an alternative, she can consider a risky stock whose 
current price is SO. The risky asset price at T will be a random variable &-; 
assuming geometric Brownian motion, we can express this future price as 
where 
is normally distributed with expected value (p-a2/2)T and variance 
u2T. In section 4.1.2 we have described how Gauss-Hermite quadrature can 
be used to discretize such a random variable, and we have also implemented 
a MATLAB function, GaussHermite, to this aim. As an alternative, we may 
adopt plain Monte Carlo sampling. 
We consider in this example a buy-and-hold strategy, with no intermediate 
consumption. Hence, the only decision variable is the fraction 6 of wealth 
that our investor should allocate to the risky stock; we do not consider either 
borrowing or short-selling, hence 6 must lie in the interval [0,1]. Assuming a 
concave utility function u(.) 
the problem is 
where future wealth WT is 
+ (1 - 6)R = Wo 
(e’ 
- R) + R] 
1 
and the term e’ 
- R can be interpreted as an excess return over the risk-free 
(total) return R. To discretize the problem, we should generate K scenarios, 
characterized by a realization Y k  and a probability Irk. If we use Monte 
Carlo sampling, we have 7rk = 1/K; if we use Gauss-Hermite quadrature, the 
probability is the weight in the quadrature formula. The resulting problem is 
K 
Such a simple optimization problem can be tackled by the MATLAB function 
f minbnd. MATLAB code implementing Monte Carlo sampling is displayed 
in figure 10.3. The function receives self-explanatory arguments including a 
function argument utilf which is the utility function. If we assume logarith- 
mic utility, here is the solution we may get: 
>> randn(’state’,O) 
>> share = OptFolioMC(1000,50 ,O. 1,0.4,0.05.1,10000,Qlog) 
share = 

SOLVING STOCHASTIC DECISION PROBLEMS BY DYNAMIC PROGRAMMING 
507 
function share = OptFolioMC(WO,SO,mu,sigma,r,T,NScen,utilf) 
muT = (mu - 0.5*sigma-2)*T; 
sigmaT = sigmatsqrt (T) ; 
R = exp(r*T); 
Normsamples = muT + sigmaT*randn(NScen,l); 
ExcessRets = exp(NormSamples1 - R; 
MExpectedUtility = @(XI 
-mean(utilf(WO*((x*ExcessRets) + R))); 
share = fminbnd(MExpectedUtility, 0, 1); 
Fig. 10.3 Simple asset allocation problem under uncertainty: Monte Carlo sampling. 
0.3092 
>> share = OptFo1ioMC(1000,50,0.1,0.4,0.05,1,10000,@1og~ 
share = 
>> share = OptFolioMC(1000,50,0.1,0.4,0.05,1,10000,@log) 
share = 
>> share = OptFolioMC(1000,50,0.l,O.4,O.O5,1,lOOOO,~log~ 
share = 
>> share = OptFolioMC(1000,50,0.l,O.4,O.O5,1,lOOOO,@log) 
share = 
>> share = OptFolioMC(1000,50,0.l,O.4,O.O5,1,lOOOO,@log~ 
share = 
>> share = OptFolioMC(1000,50,0.l,O.4,O.O5,l,lOOOO,@log~ 
share = 
0.3246 
0.3112 
0.3763 
0.3341 
0.3436 
0.2694 
There is a striking variability in the solution, which is due to sampling vari- 
ability in scenario generation. Even 10000 samples do not seem reliable. If 
we increase the number of scenarios, the solution does stabilize: 
>> randn(’state’,O) 
>> share = OptFo1ioMC(1000,50,0.1,0.4,0.05,1,5000000,@1og) 
share = 
>> share = 0ptFo1ioMC(1000,50,0.1,0.4,0.05,1,5000000,@1og~ 
share = 
>> share = OptFo1ioMC(1000,50,0.1,0.4,0.05,1,5000000,@1og~ 
share = 
0.3049 
0.3067 
0.3074 

508 
DYNAMIC PROGRAMMING 
function share = OptFolioGauss(WO,SO,mu,sigma,r,T,NScen,utilf) 
muT = (mu - 0.5*sigma^2)*T; 
sigmaT = sigma*sqrt (TI ; 
R = exp(r*T); 
[x,u] = GaussHermite(muT,sigmaT-2,NScen) ; 
ExcessRets = exp(x) - R; 
MExpectedUtility = @(XI 
-dot(w, 
share = fminbnd(MExpectedUtility, 0, 1); 
utilf (WO*((x*ExcessRets) + R))) ; 
Fig. 10.4 Simple asset allocation problem under uncertainty: Gauss-Hermite quadra- 
ture. 
However, we cannot afford such a huge number of scenarios in a complex 
problem, even less when we have to solve such a problem repeatedly within 
a numerical dynamic programming scheme. Hence, we may try to improve 
things using Gauss-Hermite quadrature. Using the function GaussHermite 
from chapter 4, we get the code in figure 10.4. Using clever scenario genera- 
tion, we need much less scenarios to get a reliable solution: 
>> share = OptFolioGauss (1000,50 ,O. 1 ,O. 4,O .05,1,2,@10g) 
share = 
>> share = OptFolioGauss (1000,50 ,O. 1 ,O .4,0.05,1,3,@1og) 
share = 
>> share = 0ptFo1ioGauss(1000,50,0.1,0.4,0.05,1,4,@1og) 
share = 
>> share = 0ptFo1ioGauss(1000,50,0.1,0.4,0.05,1,5,@1og~ 
share = 
>> share = OptFolioGauss (1000,50,0.1,0.4,0.05,1,100,@log) 
share = 
0.3139 
0.3061 
0.3064 
0.3064 
0.3064 
This little experiment just shows that Gaussian quadrature is a most valuable 
tool for numerical dynamic programming. Of course, apart from playing with 
numbers, one should try to understand some qualitative properties of the 
optimal solution by more analytical approaches. For instance, we have seen 
in example 2.14 (page 71) that logarithmic utility is a CRRA (constant relative 
risk aversion) function. Hence, we should expect that the solution does not 
depend on the current wealth Wo. Numerical experimentation confirms (but 
does not prove) this: 
>> share = OptFolioGauss(100.50,O.l,O.4,O.O5,1,5,@log~ 

SOLVING STOCHASTIC DECISION PROBLEMS BY DYNAMIC PROGRAMMING 
509 
share = 
>> share = OptFolioGauss (10,50,0.1 
,O. 4,O .05,1,5 
,@log) 
share = 
0.3064 
0.3064 
We may also play with different utility functions, such as power utility u(W) = 
W1-Y/(l - y), to see the effect of risk aversion: 
>> gamma = 0.3;, powU = @(W) 
W.-(l-gamma)/(l-gamma); 
>> share = 0ptFo1ioGauss(1000,50,0.1,0.4,0.05,1,5,powU) 
share = 
>> gamma = 0.4;, powU = @(W) W.^(l-gamma)/(l-gamma); 
>> share = OptFolioGauss (1000,50 
,O. 1,O. 4,0.05,1,5,powU) 
share = 
>> gamma = 0.5;, powU = @(W) 
W.^(l-gamma)/(l-gamma); 
>> share = OptFolioGauss (1000,50 
,O. 1 ,O. 4 ,O .05,1,5 
,powU) 
share = 
0.9999 
0.7887 
0.6295 
Note the use of the dot (.) operator in the definition of powU and the fact that, 
if we change gamma, we have to redefine the function, because the function is 
bound to the current value of gamma when the function is defined. 
0 
In the example above, we have just played with numbers on a possible sub- 
problem of dynamic programming. We may also take this opportunity to 
stress the fact that, by analyzing the Bellman equations, we may obtain im- 
portant insights into the structure of the optimal solution. For instance, ap- 
plying dynamic programming to a consumption-saving problem like the one 
we have described in example 10.3, it can be shown that logarithmic utility 
implies that a fixed fraction of wealth is consumed at each decision stage.6 
Generalizing the example, if we apply Gaussian quadrature to discretize 
conditional expectation, equation (10.8) becomes 
Even though Gaussian quadrature is very helpful, it does not solve all of our 
difficulties. In high-dimensional problems, we may still be forced to use Monte 
Carlo sampling. Furthermore, we have to discretize the state space and to 
solve possibly difficult optimization problems. But all of this is very easy if we 
%ee, e.g., [8, chapter 111 for a careful analysis of intertemporal consumption and portfolio 
choices with logarithmic and power utilities. 

510 
DYNAMIC PROGRAMMING 
are able to find a suitable discretization of the state space and if the control 
decision is very simple, as the following example shows. 
Example 10.5 Now that we are acquainted with dynamic programming, it 
is very useful to reinterpret the binomial lattice approach to price American 
options (see section 7.2). Indeed, equation (7.6), which we recall here for 
convenience, is a very simple case of a dynamic programming recursion: 
It is so easy because we have a finite state space, arising from a moment 
matching discretization of geometric Brownian motion, and because the set 
of control decisions is finite: either we continue, or we exercise the option. 
The value function is fi,j, i.e., the option value for asset price i at time 
j. Maximization over control decisions just requires to choose if we want 
to exercise, and grab the intrinsic value, or we want to continue. In the 
second case, the continuation value is the discounted expected value function, 
computed over the two successor states of the current one, under the risk 
neutral measure. 
0 
We close this section by giving a few clues about how one can handle infinite- 
horizon dynamic programs, assuming a discount factor is used.? A fairly 
natural guess is that the recursive equation (10.8) can be applied by dropping 
the time subscripts: 
V(x) = min{f(x, u) + E [V(h(x, u, Z)])} . 
U 
(10.9) 
The intuition here is that in an infinite-horizon problem we may look for a 
stationary policy, i.e., a policy such that a control decision is associated to each 
state; on the contrary, in a finite-horizon problem the policy can change when 
we are approaching the end of the time horizon. Existence of a stationary 
optimal policy should not be taken for granted,8 but the approach can be 
rigorously justified under some hypotheses. It is also interesting to note that, 
in this case, solving the Bellman equation calls for finding a fixed point of an 
operator; iterative methods are available to this purpose. 
In the finite-dimensional case the Bellman equation boils down to a set of 
non-linear equations: 
r 
N 
1 
(10.10) 
’The average cost/profit case is more difficult; see, e.g., 111. 
8A rather odd case may occur when chance constraints are enforced on states, i.e., when 
we require that the probability of visiting a subset of “bad” states is low. It may happen 
that the optimal policy is randomized, i.e., when we are in certain states we should select 
the control action according to a probability distribution. See, e.g., [14, pp. 255-2571. 

AMERICAN OPTION PRICING BY MONTE CARLO SIMULATION 
511 
where q i j  (u) is an element of the (control dependent) transition probability 
matrix. This system can be tackled by iterative methods, including variants 
of Newton's method. In the infinite-dimensional case, we may resort to the 
collocation method that we have introduced in section 3.4.4. This requires 
choosing a set of basis functions and collocation nodes to approximate the 
value function: 
M 
If we consider A4 basis functions, we should select M collocation nodes XI, . . . , 
xM. We should also discretize the random shocks. Assume we adopt Gaussian 
quadrature with weights I'rk and nodes € k ,  k = 1,. . . , K .  Then, Bellman 
equation for each state x, reads 
1 
K
M
 
i 
k = l  j=1 
M 
c Q j $ j ( X i )  =min 
U 
f
(
x
i
,
~
)
f
@
~
~
A
k
~
j
$
'
j
 
(h(xi,u,Ek)) . 
j=1 
This is a set of non-linear equation in the unknown weights ~
j
.
 
It can be 
tackled, e.g., by Newton's m e t h ~ d . ~  
10.4 AMERICAN OPTION PRICING BY MONTE CARLO 
SI M U LATlO N 
Example 10.5 shows that if we discretize geometric Brownian motion using a 
lattice, dynamic programming boils down to a simple pricing approach. How- 
ever, discretization with respect to time means that we are actually pricing 
a Bermudan option; since the exercise opportunities are restricted to a set of 
discrete times, what we get is actually a lower bound on the option price. We 
may actually apply a dynamic programming framework in continuous-time, 
but this essentially leads to the Black-Scholes partial differential equation 
with a free boundary. This may be tackled, e.g., by finite differences. Both 
lattices and finite differences are limited in their ability to cope with multiple 
stochastic factors, which is what Monte Carlo simulation is good at. Hence, 
it is natural to wonder if Monte Carlo simulation can be applied to option 
pricing with early exercise features. The answer is that indeed we can apply 
Monte Carlo, within a stochastic dynamic optimization framework. In this 
section we describe an approach due to Longstaff and Schwartz [lo], which 
should be interpreted as a way to approximate the value function of dynamic 
programming by linear regression against a set of basis functions. Since we 
9We refer the reader to [I21 for more details, a set of examples, and a MATLAB-based 
toolbox accomplishing this task. 

512 
DYNAMIC PROGRAMMING 
approximate the value function, what we expect is a suboptimal solution; fur- 
thermore, time is discretized; hence, we should expect some low bias in our 
estimate of price. Approaches to get high-biased estimators are described in 
the literature, and are useful to bound the price. 
For the sake of simplicity, we will just consider a vanilla American put 
option on a single, non-dividend paying stock. Clearly, the approach makes 
sense in more complex settings. As usual with Monte Carlo simulation, we 
generate sample paths (SO, S1,. . . , Sj,. . . , SN), where we use j as a discrete 
time index, Sj = S(j 6t), and T = M 6t is the expiration time of the option. 
If we denote by Ij (Sj) the intrinsic value of the option at time j, the dynamic 
programming recursion for the value function V, (Sj) is 
(10.11) 
In the case of a vanilla American put, we have Ij (Sj) = max{ K - Sj , 0). This 
is the generalization to a continuous-state model of the recursive equation in 
example 10.5. Having to cope with continuous prices is the only difficulty we 
have here, as time is discretized and the set control actions is finite: either 
exercise, or continue. It is important to realize that we cannot take this 
decision along individual sample paths; if we are at a given point of a sample 
path generated by Monte Carlo sampling, we cannot exploit knowledge of 
future prices along that path, as this would imply clairvoyance.1° What we 
can do is using our set of scenarios to build an approximation of the conditional 
expectation in equation ( l O . l l ) ,  for some choice of basis functions $ J k ( S j ) ,  
Ic = 1, . . . , K. The simplest choice we can think of is regressing the conditional 
expectation against a basis of monomials: $Jl(S) = 1, $z(S) = S, $3(S) = S2, 
etc. In practice, orthogonal polynomials can also be used. Note that we are 
using the same set of basis function for each time instant, but the weights in 
the linear combination will depend on time: 
The weights "kj can be found by linear regression, going backward in time; 
the approximation is non-linear in Sj, but it is linear in terms of the weights. 
In order to illustrate the method, we should start from the last time period. 
Assume we have generated N sample paths, and let us denote by Sji the price 
at time j on sample path i = 1,. . . , N .  When j = M ,  i.e., at expiration, the 
value function is trivially: 
'OThis point will also be appreciated in section 11.2, where we discuss the role of non- 
anticipativity in multistage stochastic programming. See also section 4.5.4 where we use 
Monte Carlo simulation to price a chooser option. 

AMERICAN OPTION PRlClNG BY MONTE CARL0 SIMULATION 
513 
for each sample path i. These values can be used, in a sense, as the Y-values 
in a linear regression, where the X values are the prices at time j = A4 - 1. 
More precisely, we may consider the regression model: 
where ei is the residual for each sample path. We may find the weights (Yk,M-l 
by the usual least squares approach, minimizing the sum of squared residuals. 
Note that we are considering the discounted payoff, so that we may then 
compare it directly against the intrinsic value. 
In the regression above, we have considered all of the generated sample 
paths. Actually, it is much better to consider only the subset of sample paths 
for which we have a decision to take at time j = A4 - 1. This subset is 
simply the set of sample paths in which the option is in the money at time 
j = M - 1. In fact, if the option is not in the money, we have no reason to 
exercise; using only the sample paths for which the option is in the money 
is called the “moneyness” criterion and it improves the performance of the 
overall approach. Denoting this subset by Z M - ~  
and assuming K = 3, we 
would have to solve the following least squares problem: 
The output of this problem is a set of weights, which allow us to approximate 
the continuation value. Note that the weights are linked to the time period, 
and not to sample paths. Using the same approximation for each sample path 
in Z M - ~ ,  
we may decide if we exercise or not. 
We should pause and illustrate what we have seen so far by a little numerical 
example. We will use the same example as the original reference [lo], where 
the eight sample paths given in table 10.1 are considered for a vanilla American 
put with strike price K = 1.1. For each sample path, we also have a set of 
cash flows at expiration; cash flows are positive where the option is in the 
money. Cash flows are discounted back to time j = 2 and used for the first 
linear regression. Assuming a risk free rate of 6% per period, the discount 
factor is e-0.06 = 0.94176. The data for the regression are given in table 
10.2; X corresponds to current underlying asset price and Y corresponds to 
discounted cash flows in the future. We see that only the sample paths in 
which the option is in the money at time j = 2 are used. The following 
approximation is obtained: 
E[Y I X ]  M -1.070 + 2.983X - 1.813X2. 

514 
DYNAMIC PROGRAMMING 
Table 10.1 
put. 
Sample path and cash flows at option expiration for a vanilla American 
Path 
1 
2 
3 
4 
5 
6 
7 
8 
j = o  
j = 1  
1.00 
1.09 
1.00 
1.16 
1.00 
1.22 
1.00 
0.93 
1.00 
1.11 
1.00 
0.76 
1.00 
0.92 
1.00 
0.88 
j = 2  
1.08 
1.26 
1.07 
0.97 
1.56 
0.77 
0.84 
1.22 
j = 3  
1.34 
1.54 
1.03 
0.92 
1.52 
0.90 
1.01 
1.34 
- 
Path j = l  j = 2  j = 3  
. 00 
.oo 
.07 
.18 
.oo 
.20 
.09 
.oo 
Table 10.2 Regression data for time j = 2. 
Path 
Y 
X 
.oo 
.07 
.18 
.20 
.09 
x .94176 
x .94176 
x .94176 
x .94176 
x .94176 
1.08 
1.07 
0.97 
0.77 
0.84 

AMERICAN OPTION PRICING BY MONTE CARL0 SIMULATION 
515 
Table 10.3 Comparing intrinsic and continuation value at time j = 2, and resulting 
cash flow matrix. 
Path 
Exercise 
Continue 
Path 
j = l  j = 2  j = 3  
.02 
.0369 
.03 
.046 1 
.13 
,1176 
.33 
.1520 
.26 
.1565 
.oo 
.oo 
.oo 
.oo 
.OO 
.07 
.13 
.oo 
.oo 
.oo 
.33 
.oo 
.26 
.OO 
.oo 
.oo 
Now, based on this approximation, we may compare at time j = 2 the intrinsic 
value and the continuation value. This is carried out in table 10.3. Given the 
exercise decisions, we update the cash flow matrix. Note that the exercise 
decision does not exploit knowledge of the future. Consider sample path 4: 
we exercise, making $0.13; on that sample path, we would regret our decision, 
because we could make $0.18 at time j = 3. We should also note that on 
some paths we exercise at time j = 2, and this is reflected by the updated 
cash flow matrix in the table. 
The process is repeated going backward in time. To carry out the regres- 
sion, we must consider the cash flows on each path, resulting from the early 
exercise decisions. Say we are at time step j ,  and consider path i. For each 
path i, there will be an exercise time j $ ,  which we set conventionally to M + 1 
if the option will never be exercised in the future. Then the regression problem 
(10.12) should be rewritten, for the generic time period j, as: 
(10.13) 
Since there can be at most one exercise time for each path, it may be the 
case that after comparing the intrinsic value with the continuation value on 
a path, the exercise time jz is reset to a previous period. Stepping back to 
time j = 1, we have the regression data of table 10.4. The discount factor 
e-2'o.06 = 0.88692 is applied on paths 1 and 8. Since the cash flow there is 
zero, the discount factor is irrelevant, but we prefer using this to point out 
that we are discounting cash flows from time period j = 3; if we had a positive 
cash flow at j = 3 and zero cash flow at j = 2, this is the discount factor we 

516 
DYNAMlC PROGRAMMING 
Table 10.4 Regression data for time j = 1. 
Path 
1 
2 
3 
4 
5 
6 
7 
8 
Y 
.OO x .88692 
.13 x .94176 
.33 x .94176 
.26 x .94176 
.OO x .88692 
X 
1.09 
- 
0.93 
0.76 
0.92 
0.88 
Table 10.5 Comparing intrinsic and continuation value at time j = 1, and resulting 
cash flow matrix. 
Path 
Exercise 
Continue 
Path 
j = 1  j = 2  j = 3  
.01 
.0139 
.17 
.lo92 
.34 
.2866 
.18 
.1175 
.22 
.1533 
.oo 
.oo 
.oo 
.17 
.oo 
.34 
.18 
.22 
.oo 
.oo 
.oo 
.oo 
.OO 
.07 
.oo 
.oo 
.oo 
.oo 
.oo 
.oo 
.oo 
.oo 
.oo 
.oo 
should use. Least squares yield the approximation: 
E[Y I XI x 2.038 - 3.335X + 1.356X2. 
This approximation may seem unreasonable, as we expect smaller payoffs for 
larger asset prices, yet the highest power of the polynomial has a positive 
coefficient here. It can be verified that, for the range of X values we are 
considering, the function is decreasing. Based on this approximation of the 
continuation value, we obtain the exercise decisions illustrated in table 10.5. 
Discounting all cash flows back to time j = 0 and averaging over the eight 
sample paths, we get an estimate of the continuation value of $0.1144, which is 
larger than the intrinsic value $0.1; hence, the option should not be exercised 
immediately. In the next section we illustrate how MATLAB can be used to 
implement this procedure. 

AMERICAN OPTION PRICING BY MONTE CARL0 SIMULATION 
51 7 
10.4.1 
To carry out linear regression, there are at least two possibilities. One is to use 
the regress function from the Statistics toolbox. This function also returns a 
lot of statistically relevant information; however, since we are using regression 
only as a function approximation tool, and not all readers have access to that 
toolbox, we will use the familiar backslash \ operator. When used with a 
square matrix A and a correspondingly sized vector b, this operator solves 
the system Ax = b. Otherwise, it returns a least squares solution, which is 
what we are looking for. 
A first step is writing a function which replicates the toy example we have 
just considered. The MATLAB code is displayed in figure 10.5; it is written 
as a function, but in fact it is a script. The sample paths from the example 
are assigned to matrix SPaths, where we do not include the initial price So. 
The cash flow matrix is stored in the vector CashFlows. We use a vector, 
since there can be at most one positive entry on each row in this matrix; we 
use another vector, ExerciseTime, to store the times at which the option 
is exercised on each path; this corresponds to time subscript j,* above, and 
is used to select the appropriate discount factor in the vector discountvet. 
If the option is never exercised along a sample path, we can set j l  to the 
number of steps, since we are discounting zero for that path. The main f o r  
loop proceeds backward in time. The vector InMoney contains the indexes of 
sample paths which are in the money at the time step we are considering; we 
carry out regression by least squares using the relevant data, obtaining the 
coefficient vector alpha which is used to compute the continuation value for 
each point. The vector Index contains the indexes of the in-the-money sample 
paths on which we exercise; these indexes are relative to the subset of these 
sample paths (which are in one-to-one correspondence to the rows of matrix 
RegrMat) and do not correspond to the original sample path indexes; these 
are recovered in vector ExercisePaths. After carrying out all regressions, 
we average the discounted cash flows to get the continuation value at time 
j = 0; this should be checked against the immediate intrinsic value to yield 
the option price. The reader is urged to step through this function using the 
debugger to check the calculations in the toy example. 
Now it is fairly easy to extend this function to price an American put option 
using an arbitrary set of basis functions. The code for GenericLS and a script 
to check it against binomial lattices are given in figure 10.6. Sample paths are 
generated by function AssetPaths from section 8.1.1, and we get rid of the 
initial price. The function is much like ExampleLS, and the only difference is 
that we use a cell array, fhandles, of function handles to contain the set of 
basis functions. Each element in the set of basis function is used to evaluate 
a column in the regression matrix. To this aim, we use the feval MATLAB 
function; this is, in some sense, a higher-order function taking as arguments 
another function and a set of arguments on which this should be evaluated. 
Function handles are built in the script using the @ operator and can be stored 
A MATLAB implementation of the least squares approach 

518 
DYNAMIC PROGRAMMING 
function price = ExampleLS; 
% this function replicates example 1 on pages 115-120 of the 
% original paper by Longstaff and Schwartz 
SO = 1; K = 1.1; r = 0.06; T = 3; 
NSteps = 3; dt = T/NSteps; 
discountvet = exp(-r*dt*(l:NSteps) '1 ; 
% generate sample paths 
NRepl = 8; 
SPaths = [ 
1.09 1.08 1.34 
1.16 1.26 1.54 
1.22 1.07 1.03 
0.93 0.97 0.92 
1.11 1.56 1.52 
0.76 0.77 0.90 
0.92 0.84 1.01 
0.88 1.22 1.34 
I ;  
% 
alpha = zeros(3,l) ; % regression parameters 
CashFlows = max (0, K - SPaths ( : , NSteps) ) ; 
ExerciseTime = NSteps*ones(NRepl,l); 
for step = NSteps-1:-l:l 
InMoney = find(SPaths(: ,step) < K); 
XData = SPaths(InMoney,step); 
RegrMat = [ones(length(XData), 11, XData, XData.-21; 
YData = CashFlows(InMoney).*discountVet(ExerciseTime(InMoney)-step); 
alpha = RegrMat \ YData; 
Intrinsicvalue = K - XData; 
ContinuationValue = RegrMat * alpha; 
Index = f ind(IntrinsicValueXontinuationVa1ue) ; 
Exercisepaths = InMoney(1ndex); 
CashFlows(ExercisePaths) = IntrinsicValue(1ndex); 
ExerciseTime(ExercisePaths) = step; 
end % for 
price = max( K-SO, mean(CashFlows.*discountVet(ExerciseTime)) 
); 
fig. 10.5 MATLAB function to replicate example 1 from [lo]. 

AMERICAN OPTION PRICING BY MONTE CARL0 SIMULATION 
519 
either in cell arrays or structs, not in ordinary arrays; we have chosen the first 
possibility. 
Now we may check the results we obtain by least squares Monte Carlo 
against those provided by lattice based binprice function: 
>> CheckLS 
priceLS = 
6.8074 
priceBIN = 
6.8129 
10.4.2 
In the previous example, we have used a simple quadratic polynomial. In 
more complex cases, we should be careful in the selection of basis functions. 
In the case of multiple assets, say S1 and Sz, one could consider regressing 
against polynomials involving cross-products such as S1S2, SyS2, S1 S& etc. 
There is a non-trivial trade-off between accuracy and complexity. 
The reader may also have noticed that we did not evaluate a confidence 
interval for the price. Actually, this can and should be done, but we must be 
careful in considering the bias in our estimator. Least-squares Monte Carlo, 
when properly used, yields a low-biased estimator. As we have already noted, 
one source of bias, for truly American options, comes from the fact that 
we are considering a subset of the available exercise opportunities. This is 
not a problem for Bermudan options, and Richardson extrapolation has been 
proposed to improve accuracy for American options. Another source of bias 
comes from suboptimality. We have seen a similar issue when pricing a chooser 
option in section 4.5.4. But to have a clear bias, we should actually use least 
squares Monte Carlo first to generate an early exercise strategy; then we 
should simulate the application of that (suboptimal) strategy to estimate the 
average discounted payoff. Alternative, more sophisticated, approaches have 
been proposed to compute high-biased estimators. One way to do so could be 
simulating early exercise with clairvoyance: along each path, we take exercise 
decisions knowing what comes next along each sample path. This is not 
feasible in practice, and corresponds to relaxing obvious non-anticipativity 
constraints on our decisions, and it results in a upper bound on the option 
price. 
Having 
confidence intervals from low- and high-biased estimators, we may build an 
overall confidence interval for the price. 
In least squares Monte Carlo, we have built an exercise strategy based on 
the value of continuation. A possible alternative is trying to find the exercise 
boundary directly, e.g., using splines or a suitably parameterized family of 
functions. This is clearly feasible for simple options; for the vanilla put, we 
should get something like figure 2.22 on page 118. But this is not easy in 
general, since the early exercise region need not be connected: We may have 
to find multiple surfaces describing a complicated region. 
Some remarks and alternative approaches 
However, this bound may be rather weak, i.e., too large. 

520 
DYNAMIC PROGRAMMING 
function price = GenericLS(SO,K,r,T,sigma,NSteps,NRepl,fhandles) 
dt = T/NSteps; 
discountvet = exp(-r*dt* (1 : NSteps) '1 ; 
NBasis = length(fhand1es); % number of basis functions 
alpha = zeros(NBasis,l); % regression parameters 
RegrMat = zeros (NRepl , NBasis) ; 
X generate sample paths 
SPaths=AssetPaths(SO,r,sigma,T,NSteps,NRepl); 
SPaths(: ,1) = [I ; 1 get rid of starting prices 
% 
CashFlows = max (0, K - SPaths ( : , NSteps) ; 
ExerciseTime = NSteps*ones (NRepl, 1) ; 
for step = NSteps-1:-l:l 
InMoney = find(SPaths(: ,step) < K); 
XData = SPaths(InMoney,step); 
RegrMat = zeros(length(XData) , NBasis) ; 
for k=l:NBasis 
end 
YData = CashFlows(InMoney).*discountVet(ExerciseTime(InMoney)-step); 
alpha = RegrMat \ YData; 
Intrinsicvalue = K - XData; 
ContinuationValue = RegrMat * alpha; 
Index = f ind(IntrinsicVa1ue > ContinuationValue) ; 
Exercisepaths = InMoney(1ndex) ; 
CashFlows(ExercisePaths) = IntrinsicValue(1ndex); 
ExerciseTime(ExercisePaths) = step; 
RegrMat(:, k) = feval(fhandlesCk1, XData) ; 
end % for 
price = max(K-SO, mean(CashF1ows .*discountvet (ExerciseTime))) ; 
% CheckLS.m 
SO = 50; K = 50; r = 0.05; 
sigma = 0.4; T = 1; NSteps = 50; 
NRepl = 10000; 
randn( 'state' ,O) 
fhandles = (@(x)ones(length(x) 
,1), @(x)x, @(x)x.-2>; 
priceLS = GenericLS (SO ,K ,r , T, sigma,NSteps ,NRepl ,fhaudles) 
[LatS, LatPrice]=binprice(SO,K,r,T,T/NSteps,sigma,O); 
priceBIN = LatPrice(1,l) 
Fig. 10.6 MATLAB function to price a vanilla American put by least squares Monte 
Carlo and a script to check it. 

FOR FURTHER READING 
521 
In recent years, many alternative approaches have been proposed for pricing 
American or Bermudan options by random sampling. In section 4.5.4 we have 
seen a simple case in which we build a bushy tree; given the need to generate a 
large number of samples, the approach may be feasible when a limited number 
of exercise opportunities are given. Alternative discretization strategies based 
on a recombining mesh have been proposed; for all of this we refer the reader 
to the specific literature. 
For further reading 
In the literature 
0 Dynamic programming is arguably the most powerful concept in op- 
timization, and its many potential applications are well illustrated in 
PI. 
a To overcome the curse of dimensionality, a great deal of effort has been 
devoted to the development of approximate solution methods [l, 21, 
which also include simulation-based methods. This has paved the way to 
simulation-based pricing for high-dimensional American-style options. 
An example of this line of research is [15]. 
0 In the original paper [lo], the reader may also find some treatment of 
convergence issues, which we have neglected. 
0 The best treatment of Monte Carlo for American options is [6, chapter 
81. See also [13, chapter 61 or [7]. 
0 Numerical dynamic programming for applications in Economics is dealt 
with in [9] and [12]. 
Continuous-time models are quite useful when the model is reasonably 
simple and an analytical solution can be found, usually yielding valu- 
able insights into the nature of the problem. An excellent reference on 
continuous-time dynamic programming in finance is [ll]. 
0 Another valuable reference is [4], where stylized models are used to gain 
insights into household long-term saving behavior. There, the value of 
approximate analytical solutions is also emphasized. 
On the Web 
The MATLAB toolbox for computational economics, which is associated 
to [12], can be downloaded from 
http://www4.ncsu.edu/Npfackler/compecon/ 

522 
DYNAMIC PROGRAMMING 
0 Useful lecture notes on numerical dynamic programming, and some 
(Mathematica) code, can be downloaded from 
http://www.econ.jhu.edu/people/ccarroll/index.html 
REFERENCES 
1. D.P. Bertsekas. Dynamic Programming and Optimal Control (2nd ed., 
Vols. 1 and 2). Athena Scientific, Belmont, MA, 2001. 
2. D.P. Bertsekas and J.N. Tsitsiklis. Neuro-Dynamic Programming. Athena 
Scientific, Belmont, MA, 1996. 
3. P. Brandimarte and A. Villa. Advanced Models for Manufacturing Sys- 
tems Management. CRC Press, Boca Raton, FL, 1995. 
4. J.Y. Campbell and L.M. Viceira. Strategic Asset Allocation. Oxford Uni- 
versity Press, Oxford, 2002. 
5. C. Carroll. Solving Microeconomic Dynamic Stochastic Optimization 
Problems. Lecture Notes downloadable from 
http://www.econ.jhu.edu/people/ccarroll/index.html. 
6. P. Glasserman. Monte Carlo Methods in Financial Engineering. Springer- 
Verlag, New York, NY, 2004. 
7. P. Jaeckel. Monte Carlo Methods in Finance. Wiley, Chichester, 2002. 
8. J.E. Ingersoll, Jr. Theory of Financial Decision Making. Rowman & 
Littlefield, Totowa, NJ, 1987. 
9. K.L. Judd. Numerical Methods in Economics. MIT Press, Cambridge, 
MA, 1998. 
10. F.A. Longstaff and E.S. Schwartz. Valuing American Options by Simula- 
tion: a Simple Least-Squares Approach. The Review of Financial Studies, 
14~113-147, 2001. 
11. R.C. Merton. Continuous- Time Finance. Blackwell Publishers, Malden, 
MA, 1990. 
12. M. J. Miranda and P.L. Fackler. Applied Computational Economics and 
Finance. MIT Press, Cambridge, MA, 2002. 
13. D. Tavella. Quantitative Methods in Derivatives Pricing: Introduction to 
Computational Finance. Wiley, New York, 2002. 

REFERENCES 
523 
14. H.C. Tijms. A First Course in Stochastic Models. Wiley, Chichester, 
2003. 
15. J.N. Tsitsiklis and B. Van Roy. Optimal Stopping of Markov Processes: 
Hilbert Space Theory, Approximation Algorithms, and an Application to 
Pricing High-Dimensional Financial Derivatives. IEEE Transactions on 
Automatic Control, 44:1840-1851, 1999. 
16. L.A. Woisey. Integer Programming. Wiiey, New York, 1998. 

This Page Intentionally Left Blank

Linear Stochastic 
Programming Models 
with Recourse 
In the last chapter we have considered dynamic programming as a way to 
tackle dynamic stochastic optimization problems. Dynamic programming is, 
in principle, a very powerful framework, which is able to cope with a wide 
variety of problems, but it is plagued by the curse of dimensionality. An 
alternative framework is represented by stochastic programming models with 
recourse. Among economists, stochastic programming models are arguably 
much less widespread than dynamic programming approaches. Nevertheless, 
there is a rich literature concerning financial applications, and we do believe 
that having at least some familiarity with this modeling framework is useful, 
even if we cannot dwell too deeply in the severe computational challenges 
stochastic programming must face. We will only consider linear models; this 
is a limitation, but non-linear models can often be approximated using linear 
programming modeling tricks. 
Stochastic programming models are introduced in section 11.1 as an exten- 
sion of the linear programming models we have described in chapter 6. We will 
see that stochastic programming with recourse is just one possible modeling 
framework; however, since it is arguably the most common one, we will iden- 
tify this subclass of models with “stochastic programming models” for the sake 
of brevity. We will see a few toy portfolio management models in section 11.2, 
just to show the potential for applications. A fundamental issue in stochastic 
programming is scenario generation, which is outlined in section 11.3. A po- 
tentially large scenario tree is needed to represent uncertainty, resulting in a 
large-scale optimization model. Sometimes, special-purpose methods can be 
applied, which rely on the special structure of stochastic programming mod- 
els to devise decomposition approaches. We will outline the basic method in 
525 

526 
LINEAR STOCHASTIC PROGRAMMING MODELS WITH RECOURSE 
this vein, L-shaped decomposition, in section 11.4. This will also shed some 
light on the differences and similarities between stochastic programming with 
recourse and dynamic programming, an issue which is briefly discussed in 
section 11.5. 
11.1 LINEAR STOCHASTIC PROGRAMMING MODELS 
We have introduced linear programming (LP) models in chapter 6. An LP 
model in canonical form is 
min c‘x 
s.t. Ax 
b 
x 2 0. 
When we formulate a model like this, we assume that we have exact knowledge 
of all the model parameters embedded in matrix A and in vectors c and b. 
However, in finance there are several sources of uncertainty, and this modeling 
framework may be insufficient to tackle general optimization problems, such as 
portfolio optimization. One naive attempt to extend LP models to cope with 
uncertainty would be to replace the given parameters with random variables, 
yielding the model below: 
“min” c(w)’x 
x 2 0. 
s.t. 
A(w)x 2 b(w) 
(11.1) 
Here the data c(w), A(w), and b(w) depend on random events w. The “min” 
notation is used to point out that this problem actually does not make sense, 
since minimizing a random variable has no meaning. We could define a sen- 
sible objective function by taking its expected value: 
E[c(w)’x] = E[c(w)]’x. 
An objection here may concern risk neutrality, but the real trouble is feasibility 
of the solution. Finding a solution x such that the constraints (1 1.1) are always 
satisfied may be impossible, or it could lead to a poor solution. By the way, 
this is why we did not consider LP problems in standard form, i.e., involving 
equality constraints. A possible approach is to relax the constraints a bit and 
to accept the fact that, in some cases, the constraints could not be met; we 
might just ask that this undesirable event is unlikely enough. This leads to 
chance-constrained models such as 
min c’x 
s.t. Ax 2 b 
P{G(w)x L h(w)) L 
x 2 0 ,  

LINEAR STOCHASTIC PROGRAMMING MODELS 
527 
where we have separated the deterministic constraints from those involving 
uncertainty. Such models trade off the cost of the solution with its reliability, 
or robustness. We will not consider the computational challenge of solving 
such a model. This task may be relatively easy, if the problem above turns 
out to be a convex model. This may happen, depending on the probability 
distribution of the uncertain parameter. In general, the problem may be non- 
convex, which makes it much more difficult to cope with. 
But even if we leave computational issues aside, there is another potential 
difficulty. Chance-constrained models may fully capture decision making un- 
der uncertainty in many cases of practical relevance, but they lack the ability 
of modeling a dynamic decision process in which decisions are revised when 
more and more information is acquired. In a truly dynamic decision process, 
we take a set of decisions here-and-now, based on limited information, but 
then we may adjust the decisions when the uncertainty is resolved. Of course, 
adjusting the decisions will imply some additional costs, and we would like to 
take good decisions minimizing the immediate costs as well as the expected 
value of the adjustment costs we will pay in the future. This idea leads to 
stochastic programming models with recourse. As an example, we may con- 
sider a two-stage stochastic linear programming model, which is usually stated 
as follows. The first-stage problem, involving the decisions x that we must 
take here and now, is 
min c’x + E[h(x, w)] 
s.t. AX = b 
x 2 0. 
The first-stage problem involves a set of deterministic constraints and the 
expected cost of adjusting the solution at the second stage. The second- 
stage problem, involving the adjustments, or recourse variables y, defines the 
function h(x, w): 
h(x,w) = min q(w)’y 
W(w)y = r(w) - T(w)x 
y 2 0. 
s.t. 
There are a few things to point out as far as the second-stage problem is 
concerned. 
0 We have written the problem in its most general form, allowing random- 
ness in all the parameters, but this need not be the case. For instance, if 
the recourse matrix W is deterministic, we have afixed recourse problem. 
Some algorithms may only be applied if the recourse is fixed and if the 
recourse cost vector q is deterministic as well; other solution algorithms 
have no such limitations. 
0 The overall problem can be thought of as a non-linear programming 
problem involving a recourse function H(x) = E[h(x, w)]. 
Such a func- 

528 
LINEAR STOCHASTIC PROGRAMMING MODELS WITH RECOURSE 
Fig. 11.1 Scenario t,ree for a two-stage stochastic optimization probleni. 
tion may seem intractable, as it involves the multidimensional integra- 
tion of a function implicitly defined through an optimization problem. 
However; it may be shown that in the relevant cases the recourse func- 
tion is convex. So, even if we do not know how to express H ( x )  in a 
simple analytical form, we may still be able both to evaluate (or es- 
timate) it5 value and to find a subgradient at a given point x. On 
the coiitrary; chance-constrained problems are not convex problems in 
general. 
0 Depending on its structure, the second-stage problem may have a fea- 
sible solution for any first-stage vector x and for any random event w ,  
or not. In t8he second case, the second-stage problem implicitly defines 
home further constraints on x. 
0 The approach may be generalized to multiple stages. We will see how 
in the next section. 
In principle, we can define a stochastic programming model based on a contin- 
uoiis distribution of the uncertain parameters. However; although there are 
methods which a,re devised to solve approximately such problems, they are 
beyond the scope of this introduction. A natural alternative, given our knowl- 
edge of Monte Carlo sampling, is to approximate the continuous distribution 
by a discrete scenario tree like the one depicted in figure 11.1. We repeat that 
picture here, hut we have already met this type of representation in figure 2.2 
and we know that, the idea can be generalized to multiple stages as shown 
in figure 2.3. The root, node of the tree represents the present state of the 
world, from which different future states branch, corresponding to possible 
realizat,ioiis of the uncertain data. We have to take first-stage decisions here 
and now; i.e., in the root of the tree; then, when the uncertainty is revealed, 
wc' will have the chance to take second-stage decisions to adapt to the circum- 

LINEAR STOCHASTIC PROGRAMMING MODELS 
529 
stances; each possible contingency is represented by a leaf node in the tree. 
The overall problem entails taking a good first-stage decision, which should 
be robust, in that it should leave room for not too costly adaptations at the 
second-stage. Assume that we have a set of scenarios, indexed by s E S, each 
with associated probability p,. Then the two-stage stochastic LP problem 
boils down to a large-scale LP problem: 
3ES 
s.t. 
AX = b 
T,x + W3y3 = r3 
XlYS 2 0. 
Vs E 5’ 
In principle, This problem could be simply tackled by standard LP tech- 
niques; however, its size and its peculiar structure suggest the adoption of 
more specific approaches, one of which is described in section 11.4. Now a 
natural question is: Since solving a stochastic LP looks like a non-trivial task, 
why bother? Shouldn’t we simply take the expected values of the data and 
solve a much simpler deterministic problem? Indeed, in some cases, solving 
a stochastic LP is a wasted effort. To characterize the cases in which the 
added effort is worthwhile, we may consider the VSS (value of the stochastic 
solution) concept. 
Let us define the individual scenario problem 
min 
s.t. 
AX = b 
z(x, w) = c’x + min{q,y 
1 W, = rw - Tux, y 2 0 )  
x 2 0. 
Note that this scenario problem assumes knowledge of the future event w. 
The recourse problem we have just considered amounts to solving 
RP = minE,[z(x,w)]. 
X 
Solving a deterministic problem, based on the expected values ij = E[w] of 
the data, corresponds to the expected value problem: 
EV = minz(x,ij), 
X 
which yields a solution X(ij). However, this solution should be checked in the 
real context; this means that we should evaluate the expected cost of using 
the EV solution, which calls for some adjustments anyway: 
EEV = E,[z(X(G),w)]. 

530 
LINEAR STOCHASTIC PROGRAMMING MODELS WITH RECOURSE 
The VSS is defined as' 
VSS = EEV - RP. 
It can be shown that VSS 2 0. A large VSS value suggests that solving 
the stochastic problem is well worth the effort; a small value suggests the 
opportunity to take the much simpler deterministic approach. As expected, 
it turns out that finance is a typical field in which the stochastic character 
of the problem cannot be neglected. Furthermore, by a proper choice of 
the recourse function, different risk attitudes of the decision makers may be 
represented. 
11.2 MULTISTAGE STOCHASTIC PROGRAMMING MODELS FOR 
PORTFOLIO MANAGEMENT 
The best way to introduce multistage stochastic models is by using a simple 
asset-liability management model. We use the same basic problem and data 
as (2, pp. 20-281. We have an initial wealth Wo now, and in the future we 
will have to pay an amount L, which is our only liability. We should devise 
an investment strategy to meet the liability; if possible, we would like to end 
up with a final wealth larger than L; however, we should account properly 
for risk aversion, since there could be some chance to end up with a terminal 
wealth which is not sufficient to pay for the liability, in which case we will 
have to borrow some money. A non-linear, strictly concave utility function of 
the difference between the terminal wealth and the liability would do the job, 
but this would lead to a non-linear programming model. As an alternative, 
we may build a piecewise linear utility function like that illustrated in figure 
11.2. The utility is zero when the terminal wealth W matches the liability 
exactly. If the slope T penalizing the shortfall is larger than q, this function 
is concave, but not strictly. 
The portfolio consists of a set of I assets. For simplicity, we assume that we 
may rebalance it only at a discrete set of time instants t = 1, . . . , T, with no 
transaction cost; the initial portfolio is chosen at time t = 0, and the liability 
must be paid at time T + 1. Time period t is the period between time instants 
t - 1 and t. In order to represent uncertainty, we may build a tree like that 
in figure 11.3, which is a generalization of the two-stage tree of figure 11.1. 
Each node n k  corresponds to an event, where we should take some decision. 
We have an initial node no corresponding to time t = 0. Then, for each 
event node, we have two branches; each branch is labeled by a conditional 
probability of occurrence, P { n k  I ni}, where ni = a ( n k )  is the immediate 
predecessor of node n k .  Here, we have two nodes at time t = 1 and four at 
time t = 2, where we may rebalance our portfolio on the basis of the previous 
'A related but different concept is the expected value of perfect information (EVPI); see, 
e.g., 12, chapter 4). 

MULTISTAGE STOCHASTIC PROGRAMMING MODELS 
531 
t=O 
< 
I 
f/g. 11.2 Pircewise linear coric;ave utility fiirictioii. 
t= I 
t=2 
t=3 
Fig 11 3 
Sr(JIlii1 io 1 ree for a. simple asset arid liability iiiaiiageiiieiit probleni. 

532 
LINEAR STOCHASTIC PROGRAMMING MODELS WITH RECOURSE 
asset returns. Finally, in the eight nodes corresponding to t = 3, we just 
compare our final wealth to the liability and we evaluate our utility function. 
Each node of the tree is associated with the set of asset returns during the 
corresponding time period. A scenario consists of an event sequence, i.e., a 
sequence of asset returns. We have eight scenarios in figure 11.3. For instance, 
scenario 2 consists of the node sequence (no, 711,123, ns). The probability of 
each scenario depends on the conditional probability of each node on its path. 
If each branch at each node is equiprobable, i.e., the conditional probability is 
1/2, each scenario in the figure has probability 118. The branching factor may 
be arbitrary in principle; the more branches we use, the better our ability to 
model uncertainty; unfortunately, the number of nodes grows exponentially 
with the number of stages, as well as the computational effort. 
At each node in the tree, we must take a set of decisions. In practice, 
we are interested in the decisions that must be implemented here and now, 
i.e., those corresponding to the first node of the tree; the other (recourse) 
decision variables are instrumental to the aim of devising a robust plan, but 
they are not implemented in practice, as the multistage model is solved on a 
rolling horizon basis. This suggests that, in order to model the uncertainty as 
accurately as possible with a limited computational effort, a possible idea is to 
branch many paths from the initial node, and less from the subsequent nodes. 
Each decision at each stage may depend on the information gathered so far, 
but not on the future; this requirement is called non-anticipativity condition. 
There are two basic ways to build a multistage stochastic programming model: 
the split-variable and the compact formulations, which are described in the 
next sections. They depend on how the non-anticipativity requirement is 
modeled. The suitability of each modeling approach also depends on the 
solution algorithm. 
The numerical parameters, which are common to both model formulations, 
are as follows: 
a The initial wealth is 55. 
a The target liability is 80. 
There are two assets, stocks and bonds. 
a In the scenario tree of figure 11.3 we have up and down branches; in the 
up (lucky) branches, the (total) return is 1.25 for stocks and 1.14 for 
bonds; in the down (bad) branches, the (total) return is 1.06 for stocks 
and 1.12 for bonds. 
a The reward for excess wealth above the target liability is 1. 
0 The penalty for the shortfall below the target liability is 4. 
11.2.1 Split-variable model formulation 
In the split-variable approach, the decision variables are defined as follows: 

MULTISTAGE STOCHASTIC PROGRAMMING MODELS 
533 
t=O 
t= 1 
t=2 
t=3 
1 
1 
1 
Fig. 11.4 Split-varial)le view of a sceriario tree 
0 z;'t is the ainount invested in asset i at the beginning of time period t 
in sceniirio S .  
By the same token, R:t is the (total) return of asset i in scenario s = 1, . . . , S 
during time period t. It is important to understand that, if we define the de- 
cision variables in this way; we must enforce the non-anticipativity constraint 
(3xplic:itly. The issue may be understood by looking at figure 11.4. Wc have 
a set of decision variables for each node; however, the decision variables cor- 
responding to different scenarios at the same time t must be equal if the two 
scenarios are indistinguishable at time t. This is represented by the dotted 
lines in figure 11.4. To begin with, the initial portfolio must be the same for 
all scenarios. Hence: 
Now conhider tiirie f = 1 and node n1 of the original event tree as depicted 
in figure 11.3: the scenarios s = 1,2,3,4 pass through this node and are 
i1itlihtiIigUisliaI)lc at time t = 1. Hence. we niust have 
4 
.fl = 
= 
= 2 , 1 ,  
i = 1 , . . . , I .  

534 
LINEAR STOCHASTIC PROGRAMMING MODELS WITH RECOURSE 
In fact, node n1 corresponds to four nodes in the split view of the tree. By 
the same token, at time t = 2 we have constraints like 
5
-
 
6 
522 - xz2, 
i = 1,. . . , I .  
More generally, it is customary to denote by {s}t the set of scenarios which 
are not distinguishable from s up to time t. For instance: 
(110 
= (1, 2,3,4,5,6,7,8) 
(211 = {1,2,3,41 
(512 = {5,6}. 
Then the non-anticipativity constraints may be written as 
XZt = x;; 
vi, t, s, s' E { S } t .  
This is not the only way of expressing the non-anticipativity requirement, and 
the best approach depends on the chosen solution algorithm. Now we may 
write the following model for the basic asset-liability management problem: 
(11.2) 
S 
I 
s.t. Ex;o 
= wo 
v s  E s 
(11.3) 
i=l 
I E RZ,T+lx;T 
= L + W$ - wS. 
Vs E S 
(11.5) 
Z=l 
x;t = xi; 
x;t, w;, w: 2 0. 
vi, t, s, s' E { S } t  
Here w; is the surplus at the end of the planning horizon, with reward q, 
and w5 is the shortfall, with penalty T .  The objective function (11.2) is the 
expected value of the utility function; ps is the probability of each scenario; 
the utility function is concave if T > q. Equation (11.3) states that our initial 
wealth WO is allocated among the different assets. The portfolio rebalancing 
constraints (11.4) say that the wealth at time t is reallocated. In equation 
(11.5) we evaluate how we did, by comparing the final wealth with the liability 
L, and setting the proper surplus and shortfall values. Then we add non- 
anticipativity and non-negativity constraints. Note that, since the variables 
w; and WE are restricted by non-negativity constraints, we will have w$.wE = 
0 in the optimal solution (i.e., only one variable may be different than 0 in 
each scenario). The non-negativity requirements on xft may be relaxed if we 
allow short selling. 

MULTISTAGE STOCHASTIC PROGRAMMING MODELS 
535 
In this modeling approach, we introduce a large set of variables, which are 
then linked by non-anticipativity constraints. Hence, one could wonder if this 
really makes sense. The answer depends on the solution algorithm. If one 
wants to adopt an algorithm like the L-shaped decomposition, the compact 
formulation explained in the following section must be used. The split-variable 
approach may be exploited with interior point methods aimed at stochastic 
programming. Furthermore, relaxing the non-anticipativity constraints by a 
set of Lagrange multipliers, we obtain a set of independent subproblems, one 
per scenario (much in the same vein as example 6.10). Pursuing this idea 
leads to scenario aggregation algorithms. 
Representing the split-variable formulation in AMPL The split-variable formu- 
lation is easily expressed in an algebraic language like AMPL, which is intro- 
duced in appendix C, to which we refer the reader interested in a quick tour. 
It is customary to set up two files: The first one contains the model structure, 
which is illustrated in figure 11.5, and the other one contains the data for a 
particular model instance, as illustrated in figure 11.6. 
The way we express a model in AMPL is almost self-explanatory. All the 
characters after the # character are treated as a comment; note also that in an 
algebraic language, one prefers longer names than in the usual mathematical 
notation. As is customary in AMPL models, we have to define sets, param- 
eters, decision variables, the objective function, and the constraints. Most 
of the following reflects what we illustrate in the simple introductory models 
described in the appendix, but there are a few new things. Let us check the 
model file first (figure 11.5). 
The sets involved in our formulation are introduced by the keyword set. 
Here we have a simple set, assets. 
0 The numerical parameters are introduced by the keyword param. Most 
of them are scalar values, with the exception of scenario probabilities, 
which are contained in the vector parameter prob, and returns, which 
are contained in the tridimensional array return. 
0 A new element is the indexed collection of sets links. For each time 
period, we have a set of pairs; each pair consists of two scenarios, which 
are not distinguishable up to that time period. As we have said, this is 
where we enforce non-anticipativity. 
The decision variables are introduced by the var keyword and corre- 
spond clearly to the variables in the mathematical statement of the 
model. 
Then the objective function is expressed and the solver is instructed to 
maximize its value. Note how the sum notation is used to express sums 
over an index in a very natural way. 

536 
LINEAR STOCHASTIC PROGRAMMING MODELS WITH RECOURSE 
set assets; 
# set of available assets 
param initwealth; 
# initial wealth 
param scenarios; 
# number of scenarios 
param T; 
param target; 
param reward; 
param penalty; 
# return of each asset during each period in each scenario 
param returnCassets, 1.. scenarios, 1. .TI; 
param prob{l..scenarios); 
# probability of each scenario 
# the indexed set points out which scenarios 
# are linked at each period t in O..T-1 
set links{O..T-l) within {l..scenarios, l..scenarios); 
# number of time periods 
# target value (liability) at time T 
# reward for wealth beyond target value 
# penalty for not meeting the target 
# DECISION VARIABLES 
# amount invested in each asset at each period of time 
# in each scenario 
var invest{assets,l..scenarios,O..T-1) >= 0; 
var above-target{l..scenarios)>=O; # amount above final target 
var below-target{l..scenarios)>=O; 
# amount below final target 
# OBJECTIVE FUNCTION 
maximize exp-value: 
sumCi in 1. .scenarios) prob[il *(reward*above-target [i] 
- penalty*below-target [i]) ; 
# CONSTRAINTS 
# initial wealth is allocated at time 0 
subject to budgetCi in l..scenarios): 
# portfolio rebalancing at intermediate times 
subject to balanceCj in l..scenarios, t in l..T-l) : 
sum{k in assets) (invest[k,i,O]) 
= initwealth; 
(sumCk in assets) return[k,j,tl*invest[k,j,t-11) = 
sumCk in assets) invest [k, j ,t] ; 
# check final wealth against liability 
subject to scenario-value{j in l..scenarios) : 
(sumCk in assets) return[k,j,Tl*investCk,j,T-ll) 
- above-target [j] + below-target "j] = target; 
# this makes all investments non-anticipative 
subject to linkscenarios 
Ck in assets, t in O..T-1, (sl,s2) in linksCt1) : 
invest [k, sl, tl = invest [k, s2, tl ; 
Fig. 11.5 AMPL model for the split variable formulation (SplitALM.mod). 

MULTISTAGE STOCHASTIC PROGRAMMING MODELS 
537 
set assets := stocks bonds; 
param initwealth := 55; 
param scenarios := 8; 
param T := 3; 
param target := 80; 
param reward := 1; 
param penalty := 4; 
param return := 
[stocks, 1, *I 1 1.25 2 1.25 3 1.25 
[stocks, 2, *I 1 1.25 2 1.25 3 1.06 
[stocks, 3, *I 1 1.25 2 1.06 3 1.25 
[stocks, 4, *I 1 1.25 2 1.06 3 1.06 
[stocks, 5, *I 1 1.06 2 1.25 3 1.25 
[stocks, 6, *I 1 1.06 2 1.25 3 1.06 
[stocks, 7, *I 1 1.06 2 1.06 3 1.25 
[stocks, 8, *I 1 1.06 2 1.06 3 1.06 
[bonds, 1, *I 1 1.14 2 1.14 3 1.14 
[bonds, 2, *I 1 1.14 2 1.14 3 1.12 
[bonds, 3, *I 1 1.14 2 1.12 3 1.14 
[bonds, 4, *I 1 1.14 2 1.12 3 1.12 
[bonds, 5, *I 1 1.12 2 1.14 3 1.14 
[bonds, 6, *I 1 1.12 2 1.14 3 1.12 
[bonds, 7, *I 1 1.12 2 1.12 3 1.14 
[bonds, 8, *I 1 1.12 2 1.12 3 1.12; 
param prob default 0.125; 
Fig. 11.6 AMPL data file for the split variable model formulation (SplitALM.dat). 

538 
LlNEAR STOCHASTK PROGRAMMlNG MODELS WlTH RECOURSE 
The constraints are introduced by the subject t o  keywords. For each 
constraint we list a name first (which may be used to get the dual 
variables for each constraint after solving the model); then, we specify 
the index values for which the constraint should be replicated (which 
corresponds to universal quantification, such as ‘ds, in mathematical 
notation); finally, we express the constraints themselves. 
An interesting piece of syntax is the last constraint, where we model 
non-anticipativity by enforcing the constraint for each time period and 
for each scenario pair in the indexed collection for that time period. We 
have a small glimpse of how powerful the AMPL syntax is to work with 
sets. 
Now let us check the data file (figure 11.6). 
The set of assets and the scalar parameters are specified with a simple 
syntax. 
With respect to what we illustrate in the appendix on AMPL, one new 
element is how we specify the timeindexed collection links of sets of 
pairs. Again the syntax is rather natural and self-explanatory. 
Another new element is how we list asset returns, indexed by asset, 
scenario, and time period. In this case, what we have illustrated in 
the appendix for vector and matrix data is not enough, as we have a 
tridimensional array. We basically %lice” the tridimensional array in 
two matrices. A notation like [stocks, 1, *I means that values of the 
third index, to which the wildcard corresponds, will be listed together 
with the corresponding entries: Given an asset and a scenario, we list 
the return for each time period. 
The last parameter, prob, is assigned using a shorthand notation; since 
the probability for all the scenarios is 0.125, we use the default keyword 
to streamline notation. 
Now we are ready to load the two files, solve the model, and display the 
solution: 
ampl: model SplitALM.mod; 
ampl: data SplitALM.dat; 
ampl: solve; 
CPLEX 9.1.0: optimal solution; objective -1.514084643 
20 dual simplex iterations (13 in phase I) 
ampl: display invest; 
invest [bonds, * , *I 
1 
13.5207 
2.16814 
0 
2 
13.5207 
2.16814 
0 
0 
1 
2 
:= 

MULTISTAGE STOCHASTIC PROGRAMMING MODELS 
539 
3 
13.5207 
2.16814 
71.4286 
4 
13.5207 
2.16814 
71.4286 
5 
13.5207 
22.368 
71.4286 
6 
13.5207 22.368 
71.4286 
7 
13.5207 22.368 
0 
8 
13.5207 22.368 
0 
[stocks, *, *I 
0 
1 
1 
41.4793 65.0946 
2 
41.4793 
65.0946 
3 
41.4793 
65.0946 
4 
41.4793 
65.0946 
5 
41.4793 
36.7432 
6 
41.4793 
36.7432 
7 
41.4793 
36.7432 
8 
41.4793 36.7432 
2 
:= 
83.8399 
83.8399 
0 
0 
0 
0 
64 
64 
We see quite clearly the non-anticipative nature of the solution: The first 
column of each table shows one number, since the initial decision, in the root 
of the tree, is common to all scenarios; the second column shows two values, 
corresponding to the decisions in nodes n1 and n2; at time period 2, we have 
four nodes, and four different values. We may notice that in the last period 
the portfolio is not diversified, since the whole wealth is allocated to one asset, 
and we should wonder if this makes sense. Actually, it is a consequence of 
two features of this toy model: 
0 We are approximating a non-linear utility function by a piecewise linear 
function, and this may imply “local” risk neutrality; we should either 
use a non-linear programming model or a more accurate representation 
with more pieces. 
0 The scenario tree has a very low branching factor, and this does not 
represent uncertainty accurately. 
However, the portfolio allocation in the last time period is not necessarily a 
critical output of the model: the real stuff is the initial portfolio allocation. 
The decision variables for future stages have the purpose of avoiding a myopic 
policy, but they are not meant to be implemented. Nevertheless, the possi- 
ble impact of poor modeling in the last stages should be assessed; in fact, 
for problems involving a short time horizon, end-effects may be detrimental. 
Unlike dynamic programming, we do not get the solution in feedback form: 
We do not have a good recipe to take optimal decisions in the future, as a 
multistage stochastic program should be re-run in a rolling horizon fashion 
whenever we need taking more decisions. More on this in section 11.5. 
Finally, we should note that the solution has been obtained using CPLEX 
as a solver, but this need not be the case. If you have the AMPL student demo 

540 
LINEAR STOCHASTIC PROGRAMMING MODELS WITH RECOURSE 
version, you could also use MINOS. By the way, MINOS should be used if you 
want to use a truly non-linear utility function. Other linear and non-linear 
solvers are available for use with AMPL.' 
11.2.2 Compact model formulation 
The split-variable formulation is based on a large number of variables, which 
are then linked together by the non-anticipativity constraints. This may 
be useful for algorithms based on decomposition into independent scenarios, 
which could be accomplished by dualizing non-anticipativity constraints. But 
if we want to apply a generalization of the L-shaped method (section 11.4) to 
multistage stochastic programs, the model must be written in a different way. 
A more compact formulation may be obtained directly by associating decision 
variables to the nodes in the tree. Let us introduce the following notation: 
N is the set of event nodes, in our case 
Each node n E N ,  apart from the root node no, has a unique direct 
predecessor node, denoted by u(n): for instance, u(n3) = n1. 
There is a set S c N of leaf (terminal) nodes, in our case 
S = (727,. . . , n ~ } ;  
for each node s E S we have surplus and shortfall variables w$ and WE. 
There is a set T c N of intermediate nodes, where portfolio rebalancing 
may occur after the initial allocation in node no; in our case 
T = (121,. . . , ns}; 
for each node n E {no} U T there is an investment variable xin, corre- 
sponding to the amount invested in asset a at node n. 
With this notation, the model may be written as follows: 
SES 
I 
s.t. 
C x i , n o  = wo 
i=l 
I 
1 
i=l 
i=l 
'See http: www. ampl. corn and the other web sites listed at the end of appendix C. 

MULTISTAGE STOCHASTIC PROGRAMMING MODELS 
541 
where Ri,n is the total return for asset i during the period that leads to node n, 
and p" is the probability of reaching the terminal node s E S; this probability 
is the product of all the conditional probabilities on the path that leads from 
node no to s. 
Representing the compact formulation in AMPL The compact formulation can 
also be easily expressed in AMPL. The structure of the model file is similar 
to the split-variable formulation. The main differences are: 
We introduce the three sets of nodes: the set of initial nodes, initnode, 
which is actually a singleton; the set of intermediate nodes intermnodes; 
and, finally, the set of terminal nodes termnodes, which correspond to 
the eight scenarios. 
For each node, apart from no, we have a predecessor; we use an array 
pred of singleton sets to store the predecessor; this is needed if we want 
to treat nodes as sets of symbols, but we could also use an array of 
numerical values to index nodes. 
Return and decision variables are now indexed by nodes, rather than by 
a (scenario, time) pair as we did in the split-variable model formulation. 
The objective function and the constraints are a straightforward trans- 
lation of the mathematical model. 
The data file is also fairly self-explanatory. We may see how the three node 
subsets are listed. The only noteworthy point is the use of transposition 
(keyword tr) to assign the return table; in fact, return is defined in the 
model file as a table indexed by assets and nodes, and we must transpose the 
table if we want to swap the two indexes in order to improve readability in 
the data file. 
Now we are ready to solve the model and to check that we get the same 
solution we obtained by the alternative model formulation: 
ampl: model CompactALM.mod; 
ampl: data CompactALM.dat; 
ampl: solve; 
CPLEX 9.1.0: optimal solution; objective -1.514084643 
20 dual simplex iterations (13 in phase I) 
ampl: display invest; 
invest := 
bonds nO 
13.5207 
bonds nl 
2.16814 

542 
LINEAR STOCHASTIC PROGRAMMING MODELS WITH RECOURSE 
set assets; 
param initwealth; 
# initial wealth 
param target; 
param reward; 
param penalty; # shortfall penalty 
# available investment options 
# target liability at time T 
# reward for excess wealth beyond target value 
# NODE SETS 
set init-node; 
# initial node 
set interm-nodes; 
# intermediate nodes 
set term-nodes; 
# terminal nodes 
# immediate predecessor node 
set prediinterm-nodes union term-nodes) 
within (init-node union interm-nodes); 
param prob(term-nodes); 
# probability of each scenario 
# return of each investment option at the end of time periods 
param returnfassets, interm-nodes union term-nodes); 
# DECISION VARIABLES 
# amount invested in trading nodes 
var invest{assets,init-node union interm-nodes) >= 0; 
var above-target{term-nodes)>=O; 
var below-target(term-nodes)>=O; 
# amount above final target 
# amount below final target 
# OBJECTIVE FUNCTION 
maximize exp-value: 
sum{s in term-nodes) prob [s] * (reward*above-target [s] 
- penalty*below-target[s]); 
# CONSTRAINTS 
# initial wealth is allocated in the root node 
subject to budget{nO in init-node) : 
# portfolio rebalancing at intermediate nodes 
subject to balanceCn in interm-nodes, a in pred[n]) 
: 
(sumCk in assets) return[k,n] *invest [k,a]) = 
sum(k 
in assets) invest [k,n] ; 
sumCk in assets) (invest Ck,nOl) = initwealth; 
# check final wealth against target 
subject to scenario-value{s in term-nodes, a in pred[sl) : 
(sumCk in assets) returnCk,s]*invest [k,a]) 
- above-target [s] + below-target Is] = target; 
fig. 11.7 AMPL model for the compact formulation (CompactALM.mod). 

MULTISTAGE STOCHASTIC PROGRAMMING MODELS 
543 
s e t  assets := stocks bonds; 
param initwealth := 55; 
param target := 80; 
param reward := 1; 
param penalty := 4; 
s e t  init-node := no; 
s e t  interm-nodes := n l  n2 n3 n4 n5 n6; 
s e t  term-nodes := n7 n8 n9 n10 n l l  n12 n13 n14; 
param return ( t r ) :  
n l  
1.25 
1.14 
n2 
1.06 
1.12 
n3 
1.25 
1.14 
n4 
1.06 
1.12 
n5 
1.25 
1.14 
n6 
1.06 
1.12 
n7 
1.25 
1.14 
n8 
1.06 
1.12 
n9 
1.25 
1.14 
n10 
1.06 
1.12 
n l l  
1.25 
1.14 
n12 
1.06 
1.12 
n13 
1.25 
1.14 
n14 
1.06 
1.12 ; 
stocks 
bonds : = 
param prob default 0.125; 
# immediate predecessors 
s e t  pred[nl] := no; 
s e t  predCn21 := no; 
s e t  predln31 := n l ;  
s e t  pred[n4] := n l ;  
s e t  pred[n5] := n2; 
s e t  pred[n6] := n2; 
s e t  pred[n71 := n3; 
s e t  predCn81 := n3; 
s e t  predCn91 := n4; 
s e t  pred[nlOl := n4; 
s e t  pred[nll] := n5; 
s e t  predCnl21 := n5; 
s e t  pred[nl3] := n6; 
s e t  pred[nl4] := n6; 
~~~ 
Fig. 11.8 AMPL data file for the compact model formulation (CompactALM.dat). 

544 
LINEAR STOCHASTK PROGRAMMING MODELS WITH RECOURSE 
bonds n2 
22.368 
bonds n3 
0 
bonds n4 
71.4286 
bonds n5 
71.4286 
bonds n6 
0 
stocks nO 
41.4793 
stocks n l  
65.0946 
stocks n2 
36.7432 
stocks n3 
83.8399 
stocks n4 
0 
stocks n5 
0 
stocks n6 
64 
, 
It is worth noting that writing the data file manually, in particular the in- 
formation representing the scenario tree structure, is out of the question for 
realistically sized problem instances. One possibility is writing a MATLAB 
function to do that. A few modeling tools for stochastic programming have 
also been developed; although they are mostly research products at present, 
the situation is likely to change in the future. 
11.2.3 
To give the reader an idea of how to build non-trivial financial planning mod- 
els, we generalize a bit the compact formulation of the preceding section. The 
assumptions and the limitations behind the model are the following: 
Asset and liability management with transaction costs 
0 We are given a set of initial holdings for each asset; this is a more 
realistic assumption, since we should use the model to rebalance the 
portfolio periodically according to a rolling horizon strategy. 
0 We take linear transaction costs into account; the transaction cost is a 
percentage c of the traded value, both for buying and selling. 
0 We want to maximize the expected utility of the terminal wealth. 
0 There is a stream of uncertain liabilities that we have to meet. 
a We do not consider the possibility of borrowing money; we assume all 
of the available wealth at each rebalancing period is invested in the 
available assets; actually, the possibility of investing in a risk-free asset 
is implicit in the model. 
0 We do not consider the possibility of investing new cash at each rebal- 
ancing date (as would be the case, e.g., for a pension fund). 
Some of the limitations of the model may easily be relaxed. The important 
point we make is that when transaction costs are involved, we have to intro- 
duce new decision variables to express the amount of assets held, sold, and 

MULTISTAGE STOCHASTIC PROGRAMMING MODELS 
545 
bought at each rebalancing date. We use a notation which is similar to that 
used in the compact formulation: 
0 N is the set of nodes in the tree; no is the initial node. 
0 The (unique) predecessor of node n E N\{no} is denoted by a(n); the 
set of terminal nodes is denoted by S; as in the previous formulation, 
each of these nodes corresponds to a scenario, which is the unique path 
leading from no to s E S, with probability p s .  
0 T = N\({no} U S) is the set of intermediate trading nodes. 
0 L" is the Iiability we have to meet in node n E N .  
0 c is the percentage transaction cost. 
0 zyo is the initial holding for asset i = 1,. . . , I at the initial node. 
0 P," 
is the price for asset i at node n. 
0 zp is the amount of asset i purchased at node n. 
y l  is the amount of asset i sold at node n. 
0 xl is the amount of asset i we hold at node n, after rebalancing. 
0 W s  is the wealth at node s E S. 
0 V (  W )  is the utility for wealth W .  
Based on this notation, we may write the following model: 
(11.6) 
(11.7) 
(11.8) 
I 
I 
(1 - c) c P,'" yp - (1 + c) c P,'".zp = L" 
V n  E T U {no} 
i=l 
i=l 
(11.9) 
I 
w s  
= c P:x;(s) 
- L" 
vs E s 
(11.10) 
i=l 
51, 
zz", y;, w s  
2 0. 
(1 1.11) 
The objective (11.6) is the expected utility of the terminal wealth; if we 
approximate this non-linear concave function by a piecewise linear concave 
function, we get an LP problem (as we did in section 12.1.1). Equation (11.7) 
expresses the initial asset balance, taking the current holdings into account; 

546 
LINEAR STOCHASTIC PROGRAMMING MODELS WITH RECOURSE 
the asset balance at intermediate trading dates is taken into account by equa- 
tion (11.8). Equation (11.9) makes sure that enough cash is generated by 
selling assets in order to meet the liabilities; we may also reinvest the pro- 
ceeds of what we sell in new asset holdings; note how the transaction costs are 
expressed for selling and purchasing. Equation (11.10) is used to estimate the 
final wealth; note that here we have not taken into account the need to sell 
assets to generate cash to meet the last liability. If we assume that the entire 
portfolio is liquidated at the end of the planning horizon, we could rewrite 
equation (11.10) as 
I 
W" = (1 - c) c P,ax;(") - L". 
i=l 
In practice, we would repeatedly solve the model on a rolling horizon basis, 
so the exact expression of the objective function is a bit debatable. 
This model can be generalized in a number of ways, which are left as an 
exercise to the reader. The most important point is that we have assumed that 
the liabilities must be met. This may be a very hard constraint; if extreme 
scenarios are included in the formulation, as they should be, it may well be the 
case that the model above is infeasible. So the formulation should be relaxed 
in a sensible way; we could consider the possibility of borrowing cash; we could 
also introduce suitable penalties for not meeting the liabilities. In principle, 
we could also require that the probability of not meeting the liabilities is small 
enough; this leads to chance-constrained formulations, for which we refer the 
reader to the literature. 
11.3 SCENARIO GENERATION FOR MULTISTAGE STOCHASTIC 
PROGRAMMING 
The quality of the solution obtained by solving a multistage stochastic pro- 
gram depends on how well the scenario tree represents the inherent uncer- 
tainty influencing the decision problem. To generate scenarios in the financial 
domain, the necessary starting point is a sensible model describing the evolu- 
tion of relevant quantities, such as interest rates, stock prices, inflation, etc. 
Stochastic differential equations are a possible modeling framework, in which 
case we should discretize time according to the structure of our scenario tree. 
Alternatively, discrete-time models may be built directly, such as time se- 
ries models. A class of simple discrete-time models are vector autoregressive 
models (VAR, which should not be confused with Value at Risk). Let ht be 
a vector of economic and financial variables at time t. An example of a VAR 
model is 
where c and S2 are model parameters, and E - N ( 0 ,  E) is a vector of jointly 
normal random variables with zero mean and covariance matrix E. 
ht = c + S2ht-1 + ~
t
,
 t = 1,. . . ,T, 

SCENARIO GENERATION FOR MULTISTAGE STOCHASTIC PROGRAMMING 
547 
Given a dynamic model in some form, generating a scenario tree requires 
some form of sampling. However, especially in multistage problems, there is 
the danger of an exponential growth in size of the tree. Note that we cannot 
exploit recombination, as we did with binomial lattices, because we have to 
take path-dependent decisions at each stage. Hence, due attention must be 
paid to scenario generation. In this section we first review clever mechanisms 
that have been proposed to keep the size of the tree limited. We should bear 
in mind that the purpose of scenario trees is not really to yield a 100% faithful 
representation of the underlying uncertainty over the whole planning horizon, 
as there is little hope to achieve this goal while keeping the optimization model 
to a computationally tractable size. The real aim is to get robust first-stage 
decisions. Then we illustrate issues related to arbitrage, which is obviously 
relevant in a financial domain. 
11.3.1 
The first decision to take is the shape of the scenario tree, i.e., the branching 
factor which is applied at each node. A typical approach is to have a larger 
branching factor at early stages, as representing uncertainty there accurately 
may be more important in getting robust first stage decisions. A further 
observation is that the time step need not be the same for each stage; it may 
be reasonable to use larger time steps in later time periods, where aggregate 
decisions may be considered. 
Given a scenario tree structure, we have to decide which outcomes we 
should associate to nodes in the tree, and possibly the (conditional) probabil- 
ities associated to each branch in the tree. The techniques we have already 
met in chapter 4 can be used here. 
Sampling for scenario tree generation 
0 The first possibility that we may think of is naive Monte Carlo sampling. 
In this case, the probability distribution for future nodes branching from 
current node is uniform. This approach may be sensible for two-stage 
models, but it is not quite feasible for multistage models due to the 
number of nodes we need to capture uncertainty. Variance reduction 
techniques may be useful. Antithetic sampling is the simplest option; 
importance sampling has been proposed in [5] and [13]. In the last 
case, probabilities should be adjusted to reflect the change in measure. 
Stratified sampling may also be used. 
0 Numerical integration methods are an alternative. In particular, Gaus- 
sian quadrature is a suitable way to discretize a continuous probability 
distribution; we have seen in example 10.4 how Gaussian quadrature 
may capture uncertainty much more efficiently than crude Monte Carlo 
sampling. Low-discrepancy sequences may also be used, but this again 
looks feasible for two-stage models. See, e.g., (161. 

548 
LINEAR STOCHASTIC PROGRAMMING MODELS WITH RECOURSE 
0 Antithetic sampling, in the case of symmetric distributions, leads to a 
sample that matches odd moments of the underlying density; for in- 
stance, expected value is matched, and the symmetric sampling leads 
to zero skewness. It is natural to consider sampling in such a way that 
other moments are matched as well, such as variances, covariances, and 
kurtosis. In general, matching all moments exactly will be impossible 
with a limited number of samples, but we can try to match them as 
well as possible, in a least squares sense, This leads to an approach to 
generate a set of “optimized” scenarios. To illustrate the idea, consider 
a random variable X which has a multivariate normal distribution. As- 
sume that we know the expected values pi of each component Xi, as 
well as the variance u: and the set of covariances uij for each pair (i, j )  
of variables (uii = a:). Furthermore, since we are dealing with a nor- 
mal distribution, we know that skewness = E[(J- P ) ~ / u ~ ]  
should be 
zero and that kurtosis x = E[(J- ~ ) ~ / a ~ ]  
should be 3 (here we are 
considering the marginal distribution of each random variable). 
Let us denote by x! the sample of Xi in node s belonging to a cer- 
tain branching of size S. For the sake of simplicity, we assume that 
all conditional probabilities of branches are equal, but we know from 
Gaussian quadrature that there are potential advantages in setting such 
probabilities with care. Natural requirements are 
We should point out, e.g., in the second requirement related to covari- 
ance, that we divide by number of sample S, and not by S - 1 as typical 
with sample variance, since the parameters are known a priori and not 
estimated from the data. Approximate moment matching is obtained 
by minimizing the following squared error: 

SCENARlO GENERATlON FOR MULTlSTAGE STOCHASTK PROGRAMMlNG 
549 
(11.12) 
The objective function includes four weights Wk, which may be used to 
fine tune performance. It should be mentioned that the resulting sce- 
nario optimization problem need not be convex. However, if we manage 
to find any solution with a low value of the “error” objective function, 
this is arguably a satisfactory solution, even though it is not necessarily 
the globally optimal one [12]. 
The moment matching approach is a flexible and intuitively appealing 
way of generating scenarios. Nevertheless, it has been argued that it 
lacks a sound theoretical background. Indeed, counterexamples can be 
built, showing that quite different probability distributions may share 
the first moments [ll]. In order to find a scenario generation approach 
resting on a sound basis, some researchers have proposed formal ap- 
proaches relying on stability concepts and the definition of probability 
metrics. These methods require a high level of mathematical sophistica- 
tion; hence, in this introductory chapter, we limit ourselves to provide 
the reader with a basic feeling for the overall idea (see, e.g., [20], for 
a thorough treatment). To begin with, we should try to formalize the 
concept of stability. To this aim, let us consider an abstract view of a 
stochastic optimization problem: 
Here x is the set of decision variables, constrained on a set X. The 
random data are represented by <, which belongs to set Z on which a 
probability measure P is defined. The optimal value of this stochastic 
program depends on the probability measure P , as pointed out by the 
notation u(P). What happens if we perturb the measure P? A possible 
reason for the perturbation is that we have unreliable data, which means 
that we actually ignore the “true” measure P and we consider another 
measure Q instead. Alternatively, we may be forced to resort to an 
approximate measure Q, in the sense that we use a scenario tree which 
approximates the true measure P. Whatever the reason, we must first 
define a probability metric in order to quantify the distance between 
two probability measures. 
There are many ways to do so. One possibility has its roots in the Monge 
transportation problem, which asks for the optimal way of transporting 
mass (e.g., soil, when we are building a road). The problem has a prob- 
abilistic interpretation, which was pointed out by Kantorovich, when 

550 
LINEAR STOCHASTIC PROGRAMMING MODELS WITH RECOURSE 
Fig. 11.9 Two simple sceiiario trees for asset price paths. 
we interpret mass in a probabilistic sense (see [19], for more details). In 
order to define a concept of distance between two probability measur~b, 
we may define a transportation functional: 
Here c(., .) is a suitably chosen cost function; the problem calls for find- 
ing the minimum of the integral over all joint measures 7, defined on 
the Cartesian product Z x E, 
whose marginals coincide with P and Q; 
respectively (7rl and 7r2 represent projection operators). In the case of 
two discrete measures P and Q, this boils down to the classical trans- 
portation problem with a linear programming formulation. Under some 
tcclinical conditions, a form of Lipschitz continuity can be proved: 
In practical terms, what one can do is selecting a cost function c : 
Z x Z -+ IR in order to define a probability metric. Then we look 
for an approxirnate distribution PtTrf.. 
i.e., the scenario tree, such that 
1-1, (P, Pt,p,) < f. This leads to algorithms to reduce the scenario tree. In 
[9] it scenario rediiction procedure is described, based on the theoretical 
concepts above. The idea is sampling a large tree, and then reducing its 
size to a manageable level. 
11.3.2 
Arbitrage free scenario generation 
The considerations we have done so far apply to a generic stochastic program. 
U l e n  WP deal with itri application in finance, there is still another issue: 
arbitrage. Consider the data of the toy problem we have solved in section 11.2. 
Art. they sensible data? To uridcrstand the issue, consider the two siniple trees 
tlepictd in figure 11.9. The first one corresponds to the scenarios we have 
used in the example. If we assume that the initial prices are 1 for both assets, 

SCENARIO GENERATION FOR MULTISTAGE STOCHASTIC PROGRAMMING 
551 
the total returns we used in the toy example can be regarded as prices in the 
two scenarios. Sensible scenarios should not only reflect the information we 
have, but they should also rule out arbitrage opportunities. One way to define 
an arbitrage opportunity is the following. We have an arbitrage opportunity 
if there exists a portfolio which is guaranteed to have a non-negative value at 
the end of the holding period in any scenario, but which has a negative value 
at the beginning. Formally, let p E RT be the vector of the initial prices for n 
assets, x E R" the portfolio holdings for each asset, and R E R")" the return 
of each asset in each of the m scenarios (i.e., Rij is the return of asset j in 
scenario i). Then an arbitrage opportunity is a portfolio x such that 
Rx 2 0 
and 
p'x< 0. 
(1 1.13) 
Another form of arbitrage opportunity is the following3: 
Rx 2 0 
and 
p'x=O, 
(1 1.14) 
where at least one inequality is strict. In other words, we are sure that we 
will not lose any money in any scenario and there is at least one scenario in 
which we gain something. 
In order to exploit an arbitrage opportunity to gain an infinite profit, we 
should be able to do some short selling; if the optimization model forbids 
short selling, we will not see such a blatant error as an unbounded solution, 
but what we get could be not very sensible anyway. 
It is easy to see that the scenario tree in figure 11.9b leads to an arbitrage 
opportunity like (11.14). With those asset prices, an initial portfolio has zero 
value if 
z1+ 2 2  = 0. 
We may use this condition to express the final portfolio value in the two 
scenarios: 
1.2521 + 1.1422 = (1.25 - 1.14)Sl 
1.1521 + 1.1222 = (1.15 - 1.12)21. 
It is easy to see that we should sell the second asset short, so that 2 1  > 0, 
to get an arbitrage opportunity. The same does not hold in the case of figure 
11.9a. 
But how can we be sure that a set of scenarios is arbitrage-free? An answer 
is given by the following theorem. 
THEOREM 11.1 There is no arbitrage opportunity of the form (11.13) if 
and only if there exists a vector y such that 
R'y = p 
and 
y 2 0. 
3See [14, chapter 2) for a discussion about the relationships between the two forms of 
arbitrage. 

552 
LINEAR STOCHASTIC PROGRAMMING MODELS WITH RECOURSE 
Proof. Consider the following linear programming problem: 
max 
O’y 
s.t. 
R’y = p 
Y 2 0. 
If this problem is solvable, so is its dual: 
min 
p’x 
set. 
Rx 2 0. 
But in this case, the optimal objective values are both equal to zero. Then we 
see that if there exists a feasible vector y for the primal problem, we cannot 
have p‘x < 0. 
0 
On the one hand, the theorem suggests a way to make scenarios arbitrage 
free. We could simply add a node in such a way that the conditions of the 
theorem are met. The full details of this idea are given in [6]. It should be 
noted that finding the best way to generate scenarios is still an open issue, as 
we may well generate arbitragefree scenarios which do not fit the assumed 
distributions at all. On the other hand, by reasoning along the lines of the 
theorem, we may get a grasp on the relationships between the absence of ar- 
bitrage opportunities and the existence of risk-neutral probability  measure^.^ 
To begin with, we should note that if a vector p of initial prices satisfies 
theorem 11.1, then any vector Xp, X > 0, does, too. So there is a degree of 
freedom in pricing; in fact, we have only considered risky assets. What if we 
consider a risk-free asset with a risk-free rate r? To characterize arbitrage 
when a risk-free asset is available, let us consider a two-stage scenario tree: 
the initial node is 0 and there are N nodes at the second stage. Let Pi0 
be the current price of asset i, i = 1,. . . , I, and Pi, the price if scenario n, 
n = 1,. . . , N ,  occurs. For each asset, we may define the discounted gain for 
asset i in scenario n, with respect to the risk-free asset: 
pi, 
2n l + r  Pi0 
R? =-- 
Vi, n. 
Note that if a discounted gain is positive, it means that the risky asset has 
performed better than the risk-free asset. Given a set of portfolio holdings xi, 
we may define the overall discounted gain in node n: 
I 
*The rest of this section can be safely skipped; we include this topic to point out another 
use of linear programming duality, but it is not essential for the following. The treatment 
follows [17], 
to which we refer the interested reader for more details. 

SCENARIO GENERATlON FOR MULTISTAGE STOCHASTIC PROGRA MMlNG 
553 
which is the realization of a random variable G* in scenario n. Now it is 
intuitive that an arbitrage opportunity may be characterized by the conditions 
Sn * - 
> O  
V n  
E[G*] > 0. 
This means that the portfolio is expected to gain more than the risk-free 
asset on the average, but it cannot gain less in any possible scenario. To find 
a condition ruling out arbitrage, we may try to reason as in theorem 11.1. We 
may rewrite the arbitrage conditions as 
N
I
 
C C R,*,xi = 1 
n=l i=l 
I CRT,X~ 
2 o 
Vn. 
i=l 
The first condition may look a bit arbitrary, but its purpose is to make sure 
that at least one of the g: is strictly positive; since an arbitrage opportunity 
may be scaled arbitrarily, setting the double sum value to 1 serves the purpose. 
Now, to apply linear programming duality, we should rewrite these conditions 
in the standard form: 
A x = b  
x 2 0. 
(1 1.15) 
We may simply express each portfolio holding, which may be negative if short- 
selling is allowed, as 
X i = +  
2, - , 
xT,xL.+ 2 0, 
and introduce a set of non-negative auxiliary variables  XI+^, n = 1,. . . , N :  
I 
I 
X I + n  = C R ; ~ x ~  
= C (R,*,x+ - R:,,x;) 
Vn. 
i=l 
i=l 
So we have a vector of non-negative decision variables: 
- 
x = [XT 2; 22' . . ' X I  XI+1 . . . X I + N ] ' .  
Now the existence of an arbitrage is linked to the existence of a solution to 
the system (11.15), where 
A =  

554 
LlNEAR STOCHASTK PROGRAMMlNG MODELS WlTH RECOURSE 
and 
b = [1,0,. . .,O]’. 
If there is a feasible solution of (11.15), there cannot be a solution of the 
following system: 
A‘y I 0  
b’y > 0. 
(11.16) 
This is a direct consequence of linear programming duality. In fact, the ex- 
istence of a solution of system (11.16) would imply that there is direction y 
along which we may arbitrarily increase the objective function b’y without 
violating the constraints A’y 5 c, for an arbitrary vector c. Hence, the dual 
linear program would be unbounded, and the primal could not be feasible. 
Seeing it the other way around, if there is a solution to system (11.16), there 
is no arbitrage opportunity. It is possible to find an important interpretation 
of system (11.16), taking the forms of A and b into account. Let us denote 
the dual variable corresponding to the first primal constraint by yo; we also 
have a dual variable yn for each primal constraint corresponding to scenario 
n. Now let us write the dual constraints A’y 5 0 explicitly. For each asset i, 
we have a pair of inequalities: 
Together, they imply that for all assets i we have 
N 
(11.17) 
n=l 
Furthermore, considering the last n columns of matrix A, we also have 
YO -Yn 5 0 
Vn. 
This, together with second condition in system (11.16), has the following 
implications: 
b’y>O * y 0 > 0  + 
Let us rescale the dual solution as follows: 
Yn > 0 
Vn. 
Vn. 
(11.18) 

L-SHAPED METHOD FOR TWO-STAGE LINEAR STOCHASTIC PROGRAMMING 
555 
We see that the vector T may be interpreted as a probability measure, since 
the components are non-negative and their sum is 1. Moreover, it is a risk- 
neutral probability measure, according to which any scenario is possible (it 
has strictly positive probability) and any asset gains the risk-free return on 
the average. To see this, we may plug equation (11.18) into equation (11.17) 
to obtain 
N 
n=l 
This means that, under this probability measure, the expected discounted 
gain for any asset is zero, which in turn implies 
En[Pz] = (1 + r ) h .  
Now we may see a little better why risk-neutral probability measures play a 
role in option pricing under the no-arbitrage assumption, at least in a two- 
period economy with discrete states of the world. Rigorous treatment with 
continuous time and continuous asset prices requires the tools of stochastic 
calculus. 
11.4 L-SHAPED METHOD FOR TWO-STAGE LINEAR STOCHASTIC 
PROGRAMMING 
In the first sections of this chapter, we have formulated a few simple stochastic 
LP models, and we have seen that they can be tackled by the simplex method; 
interior point methods are a possible alternative. In other words, by using a 
discretized representation of uncertainty we obtain a deterministic equivalent 
program. However, given the number of scenarios we need to generate, the 
sheer size of the resulting model may be overwhelming and it can exceed 
the capabilities of the best available solvers. This is why clever scenario 
generation is so important. Another difficulty which is not so evident, is that 
even moderately sized stochastic programs may be difficult to solve because of 
their structure: it may happen that the progress made by the simplex method 
is very slow. Interior point methods may be a suitable alternative in some 
cases, and another possibility is the development of specific solution methods 
which take advantage of the structure of stochastic programs. This is a very 
active and technically challenging area of research. What we would like to 
do is to give an idea of how structure can be exploited to devise solution 
algorithms based on decomposition. We will describe a simplified version of 
L-shaped decomposition, which was the first specific algorithm developed to 
cope with large-scale two-stage stochastic programs. 
Consider a two-stage problem with a fixed recourse matrix W: 
min 
c’x + C p,qbys 

556 
LINEAR STOCHASTIC PROGRAMMING MODELS WITH RECOURSE 
s.t. 
AX = b 
W y ,  + T,x = rs 
X,Y, 2 0, 
Qs E S 
where p ,  is the probability of scenario s. It may be seen that the problem 
lends itself to a decomposition approach: in fact, once the first-stage decisions 
x are fixed, the problem is decomposed into a set of small subproblems, one 
for each scenario s. This point may be appreciated by looking at the sparse 
structure of the overall technological matrix for this problem: 
This matrix is almost block-diagonal. The recourse function is 
s E S  
where 
h,(x) = min q‘,ys 
s.t. 
W y ,  = rs - Tsx 
(1 1.19) 
Ys 2 0. 
Evaluating the recourse function for a given first-stage decision 2 entails solv- 
ing a set of independent LP problems. For simplicity, we assume here that all 
these problems are solvable, i.e., h,(x) < +m for any scenario s, for any x 
that is feasible with respect to the first-stage constraints. We say in this case 
that the problem has relatively complete recourse. This may be a reasonable 
assumption in financial problems. Consider, for instance, an asset-liability 
management problem; if we include extreme and pessimistic financial scenar- 
ios in our model, it might be the case that some liabilities are not always met; 
in such a case, we may relax the constraints by suitable shortfall penalties 
(like we did section 11.2). These penalties make the recourse complete. If 
the recourse is not complete, the approach we describe here may easily be 
extended. 
It can be shown that the recourse function H(x) is convex; hence we may 
consider the application of Kelley’s cutting plane algorithm, which was il- 
lustrated in section 6.3.4. To this end, let us rewrite the two-stage problem 
as 
min 
c’x+ e 

L-SHAPED METHOD FOR TWO-STAGE LINEAR STOCHASTIC PROGRAMMING 
557 
(11.20) 
We may relax the constraint (11.20), obtaining a relaxed master problem, and 
then add cutting planes of the form 
e 2 ~
I
X
 
+ p. 
The coefficients of each cut are obtained by solving the scenario subproblems 
for given first-stage decisions. To see how, let i be the optimal solution of the 
initial master problem. Consider the dual of problem (11.19): 
h , ( i )  = max (r, - Tsk)’7r, 
s.t. 
W’T, 5 g,. 
(11.21) 
Given an optimal dual solution +,, it is easy to see that the following rela- 
tionships hold: 
/Z,(E?) = (r, - T,X)’+, 
(1 1.22) 
h,(x) 2 (r, - T,x)’+, 
V X .  
(1 1.23) 
The inequality (11.23) derives from the fact that +, is the optimal dual solu- 
tion for x, but not for a generic x. Summing (11.23) over the scenarios, we 
Hence, we may add the cutting plane 
S E S  
The L-shaped decomposition algorithm is obtained by iterating the solution 
of the relaxed master problem, which yields 8 and 2, and of the corresponding 
scenario subproblem. At each iteration, cuts are added to the master problem. 
The algorithm stops when the optimal solution of the master problem satisfies 
9 5 H(E?). 
This condition may be relaxed if a near-optimal solution is good enough for 
our purposes. 
If the recourse is not complete, some of scenario subproblems may be in- 
feasible for certain first-stage decisions. In this case we may again exploit the 
dual of the scenario subproblem. Note that the feasibility region of this dual 
does not depend on the first-stage decisions, since 2 does not enter constraints 
(11.21). Thus, if a dual problem is infeasible, it means that the second-stage 

558 
LlNEAR STOCHASTIC PROGRAMMING MODELS WITH RECOURSE 
problem for the corresponding scenario will be infeasible for any first-stage 
decision. Ruling out this case, which is likely to be due to a modeling error, 
when the primal problem is infeasible, the dual will be unbounded. Hence, 
there is an extreme ray of the dual feasible set along which the optimal solu- 
tion goes to infinity. In this case we may easily add an infeasibility cut to the 
master, cutting the first-stage decisions which lead to an infeasible second- 
stage problem. Thus, at any iteration, we discover either an extreme point 
or an extreme ray of the dual feasible sets of each second-stage subproblem. 
The finite convergence of the method derives from the fact that any polyhe- 
dron has a finite number of extreme points and extreme rays (see supplement 
S6.1.2). 
We have just outlined the basic principles of one possible approach to cope 
with stochastic programs. Other approaches have been pursued, but we would 
like to point out that this idea can also be generalized to multistage stochastic 
programs. Furthermore, the idea of cutting planes is the foundation of some 
methods which are able to cope with continuous distributions. In the modeling 
approach we have pursued we first sample a set of scenarios, and then we 
solve an optimization model. It is also possible to integrate sampling within 
the optimization algorithm, to generate cutting planes, in such a way that a 
problem with continuously distributed parameters can be tackled (see [lo]). 
11.5 
A COMPARISON WITH DYNAMIC PROGRAMMING 
In the last chapter, we have considered dynamic programming as a framework 
to tackle dynamic decision making under uncertainty, and it is natural to won- 
der about connections or differences between that approach and stochastic 
programming with recourse. Indeed, the concept of recourse function looks 
quite similar to the concept of value function or cost-to-go in dynamic pro- 
gramming. While the two approaches are clearly related, they are actually 
complementary. 
0 Dynamic programming approaches require finding the value function, 
as a function of state variables, for each decision stage. Stochastic pro- 
gramming methods based on L-shaped decomposition aim at finding 
only a local approximation of the recourse function. 
0 Dynamic programming methods, after computing the value functions, 
allow for a simulation of the whole decision process over the planning 
horizon. Stochastic programming methods aim at finding the solution 
for the first stage only, even though in principle further stage decision 
variables represent a feedback policy. In this sense stochastic program- 
ming is a more operational approach. Indeed, the use of dynamic pro- 
gramming models is the rule whenever one wants to use an optimization 
model to gain insights in a problem, possibly by a stylized model, rather 
than actually solving it in operational terms. This is quite common in 

FOR FURTHER READlNG 
559 
Economics. For instance, dynamic programming has been used to in- 
vestigate strategic allocation between risky and risk-free assets for a 
long-term investor, for varying income profiles over time [3]. This is 
certainly important in Pension Economics, but it is probably not what 
the manager of a pension fund would use for operational decisions. 
0 Dynamic programming methods are able to cope with infinite-horizon 
problems, whereas stochastic programming methods are not. Again, 
this is typical of dynamic models in Economics. 
0 Dynamic programming models, in some cases, may be solved analyt- 
ically, maybe approximately. The usefulness of insights from approx- 
imate analytical solutions is illustrated, e.g., in [3]. On the contrary, 
stochastic programming approaches are numerical in nature. 
0 Dynamic programming models assume some condition on the under- 
lying uncertainty, since the disturbance process should be Markovian 
(actually, often one can get around this difficulty by augmenting the set 
of state variables). In principle, any type of uncertainty and any type 
of intertemporal dependence can be tackled by stochastic programming, 
provided we are able to generate a scenario tree. 
Given these differences, it is no surprise that dynamic programming is more 
common in the Economics community, whereas stochastic programming is 
more familiar to the Operations Research community. However, a broader 
knowledge of pro and cons of both approaches is most valuable. For instance, 
the regression-based approach to pricing American options by Monte Carlo 
simulation can be better understood if we interpret the procedure as a way 
to enforce non-anticipativity of decisions under uncertainty. 
For further reading 
In the literature 
0 An early reference on stochastic programming with recourse is [4]. 
Introductions to modeling with stochastic programming can be found 
in (211 and [23]. 
0 Textbook treatments, covering also solution methods, are available in 
[2] and [15]. 
0 A survey about solution methods can also be found in [l]. 
0 The L-shaped method is described in the original reference [24]. 
0 We have only covered stochastic programming models with recourse. 
For an introduction to chance-constrained models, see [18]. 

560 
LINEAR STOCHASTIC PROGRAMMING MODELS WITH RECOURSE 
0 Since scenario generation is only an approximate way to represent un- 
certainty, we should wonder how errors may affect the solution. Theo- 
retical results are surveyed in [20]; a sensitivity analysis approach based 
on “contamination” between different scenario trees is described in [7]. 
0 Scenario generation is one of the topics covered in [6] and [12]. The first 
reference also addresses arbitrage issues in financial scenario generation. 
0 For a thorough discussion on arbitrage and risk-neutral probability mea- 
sures, see [14] and [17]. 
0 The AMPL language is described in [8]. 
0 A reference describing many portfolio optimization models, including 
stochastic programming models, is the two-volume set [25] and [26]. 
0 Stochastic programming for portfolio management is also covered by 
[221* 
On the Web 
The AMPL site is http: //www. amp1 . com. 
The main web reference for stochastic programming is 
http://stoprog.org. 
0 Other pointers to stochastic programming, including financial applica- 
tions, can be found by browsing http : //mat. gsia. cmu. edu. 
REFERENCES 
1. J.R. Birge. Stochastic Programming Computation and Applications. IN- 
FORMS Journal of Computing, 9:111-133, 1997. 
2. J.R. Birge and F. Louveaux. Introduction to Stochastic Programming. 
Springer-Verlag, New York, 1997. 
3. J.Y. Campbell and L.M. Viceira. Strategic Asset Allocation. Oxford Uni- 
versity Press, Oxford, 2002. 
4. G.B. Dantzig. Linear Programming under Uncertainty. Management Sci- 
ence, 1:197-206, 1955. 
5. M.A.H. Dempster and R.T. Thompson. EVPI-Based Importance Sam- 
pling Solution Procedures for Multistage Stochastic Linear Programmes 
on Parallel MIMD Architectures. Annals of Operations Research, 90: 161- 
184, 1999. 

REFERENCES 
561 
6. C. Dert. Asset Liability Management for Pension Funds: A Multistage 
Chance Constrained Programming Approach. Ph.D. thesis, Erasmus Un- 
versity, Rotterdam, The Netherlands, 1995. 
7. J. DupaEovB. Stability and Sensitivity Analysis for Stochastic Program- 
ming. Annals of Operations Research, 27, 1990. 
8. R. Fourer, D.M. Gay, and B.W. Kernighan. AMPL: A Modeling Language 
for Mathematical Programming. Boyd and Fraser, Danvers, MA, 1993. 
9. H. Heitsch and W. Roemisch. Scenario Reduction Algorithms in Stochas- 
tic Programming. Computational Optimization and Applications, 24: 187- 
206, 2003. 
10. J.L. Higle and S. Sen. Stochastic Decomposition. Kluwer Academic Pub- 
lishers, Dordrecht, 1996. 
11. R. Hochreiter and G.Ch. Pflug. Scenario Tree Generation as a Multidi- 
mensional Facility Location Problem. Aurora Technical Report, Univer- 
sity of Wien, 2002 (paper downloadable from 
http://www.vcpc.univie.ac.at/aurora/publications/). 
12. K. Hoyland and S.W. Wallace. Generating Scenario Trees for Multistage 
Decision Problems. Management Science, 47:296-307, 2001. 
13. G. Infanger. Planning under Uncertainty: Solving Large-Scale Stochastic 
Linear Programs. Boyd and Fraser, Danvers, MA, 1994. 
14. J.E. Ingersoll, Jr. Theory of Financial Decision Making. Rowman & 
Littlefield, Totowa, NJ, 1987. 
15. P. Kall and S.W. Wallace. Stochastic Programming. Wiley, Chichester, 
1994. 
16. M. Koivu. Variance reduction in sample approximations of stochastic 
programs. Mathematical Programming, 103:463-485, 2005. 
17. S.R. Pliska. Introduction to Mathematical Finance: Discrete Time Mod- 
els. Blackwell Publishers, Malden, MA, 1997. 
18. A. Prkkopa. Probabilistic Programming. In A. RuszczyIiski and A. Shapiro, 
editors, Stochastic Programming. Elsevier, Amsterdam, 2003. 
19. S.T. Rachev. Probability Metrics and the Stability of Stochastic Models. 
Wiley, Chichester, 1991. 
20. W. Roemisch. Stability of Stochastic Programming Problems. In A. Rusz- 
czyriski and A. Shapiro, editors, Stochastic Programming. Elsevier, Ams- 
terdam, 2003. 

562 
LlNEAR STOCHASTIC PROGRAMMING MODELS WITH RECOURSE 
21. A. Ruszczyriski and A. Shapiro. Stochastic Programming Models. In 
A. Ruszczydski and A. Shapiro, editors, Stochastic Programming. Else- 
vier, Amsterdam, 2003. 
22. B. Scherer and D. Martin. Introduction to Modern Portfolio Optimization 
with NuOPT, S-Plus, and SeBayes. Springer, New York, 2005. 
23. S. Sen and J.L. Higle. An Introductory Tutorial on Stochastic Program- 
ming Models. Interfaces, 29:33-61, 1999. 
24. R. Van Slyke and R.J-B. Wets. L-Shaped Linear Programs with Applica- 
tion to Optimal Control and Stochastic Programming. SIAM Journal on 
Applied Mathematics, 17:638-663, 1969. 
25. S. Zenios, editor. A Library of Financial Optimization Models. Blackwell 
Publishers, Oxford, 2006. 
26. S. Zenios. Practical Financial Optimization. Blackwell Publishers, Ox- 
ford, 2006. 

12 
Non- Convex 
Op timixa ti o n 
All of the optimization models we have considered so far have a common 
characteristic: They are convex, which means that we are minimizing a con- 
vex objective function (or maximizing a concave one) over a convex feasible 
set. In principle, convex optimization problems are easy. In practice, they 
can prove numerically difficult to deal with because of hard non-linearities 
or because of their sheer size (as is the case with large-scale stochastic pro- 
gramming models). Nevertheless, the optimal solution of convex problems is 
characterized by some relatively simple properties. Hence, if we are handed 
a solution by someone claiming it is the optimal one, it is usually easy to 
check the claim. In non-convex problems, even checking optimality is a hard 
task. Hence, solution methods for non-convex problems are far less efficient 
and much less standardized. Many of them are actually heuristics aimed at 
finding a good solution with a reasonable computational effort, without any 
claim about optimality. 
In fact, non-convex optimization methods are typically outside the bag 
of customary tools of people in Economics and Finance. Despite all of these 
difficulties, there are good reasons why we should have at least a grasp of them. 
There are a variety of issues in portfolio management, which are neglected 
in classical mean-variance models, that could be tackled fruitfully within an 
integer programming framework: 
0 Limited diversification portfolio 
0 Minimum portfolio weights for assets 
0 Minimum transaction lots 
563 

564 
NON-CONVEX OPT/M/ZAT/ON 
0 Fixed or piecewise linear transaction costs 
While the resulting models were very hard to solve some years ago, astonishing 
progress both in computing hardware and commercially available solvers has 
made their practical use feasible. 
Non-convexity can arise because the feasible region is non-convex. The 
most common case arises because some decision variables are restricted to 
integer values, possibly the set (0,l). This happens when decision variables 
model logical decisions, which are by their very nature discrete: Either I do 
something or I do not. In section 12.1 we introduce mixed-integer program- 
ming models. First we show the most common “modeling tricks” based on 
logical decision variables; then we outline portfolio optimization models in- 
cluding logical variables. 
Another way non-convexity can arise is in the objective function. For in- 
stance, an objective function represented by a polynomial is likely to have a lot 
of local minima. This is why such problems are known m global optimization 
problems. In section 12.2 we show a portfolio optimization model based on a 
fixed-mix, which gives rise to a non-convex problem over continuous decision 
variables. 
Then we consider solution methods for non-convex models. We will ac- 
tually only consider branch-and-bound methods in section 12.3. Branch and 
bound is the standard approach for mixed-integer models, and it is available 
in most commercial solvers. MATLAB, at present, has a limited ability to 
cope with such models, and this is why we will mainly use AMPL and CPLEX 
to illustrate how models can be solved. Branch and bound can also be applied 
to some continuous global optimization models. However, global optimization 
methods are far less standardized. There is a wide variety of methods which 
are specific to subclasses of global optimization models. Apart from their 
conceptual difficulty, most of them are not available in commercial packages, 
and this is another reason why we will not deal with them in detail. 
Finally, in section 12.4 we will cover some general-purpose principles that 
can be used to devise heuristics. In fact, non-convex problems may be a very 
hard nut to crack. In extreme cases, a practical alternative is to give up op- 
timality and to look for a reasonably good solution. We will consider local 
search heuristics, such as simulated annealing, tabu search, and genetic algo- 
rithms. They are fairly general and flexible approaches, and indeed they have 
been implemented in commercial solvers which have been successfully inte- 
grated with simulation packages to tackle some optimization problems, where 
complexity precludes the mathematical formulation of an objective function. 
12.1 
MIXED-INTEGER PROGRAMMING MODELS 
We have already met an integer programming model in example 1.2 on page 
15, where we introduced the knapsack problem as a very rough representation 

MIXED-INTEGER PROGRAMMING MODELS 
565 
of capital budgeting: 
n 
max 
C Rzxi 
i = l  
N 
i=l 
xi E (0,l). 
This is actually a linear programming model with an additional restriction on 
the decision variables, which may take values only within a discrete set; this 
is what makes the problem non-convex. 
A more general form of a mixed-integer linear programming model is 
min 
C’X+ d’y 
s.t. Ax +Dy 2 b 
~ 2 0 ,  ~ E Z + = { 0 , 1 , 2 , 3  
,... } 
The name stems from the fact that we mix continuous variables x and integer 
variables y. When all of the decision variables must take integer values, we 
speak of pure integer programming models. A very common case arises when 
a decision variable is binary, i.e., it must take values within the set (0,l). This 
is typical of logical decision variables, as we will illustrate in the next section. 
Moreover, using binary variables is a very powerful modeling trick to represent 
non-trivial constraints. When all the decision variables are binary, we have a 
pure binary programming model. The knapsack problem is such a case. 
General integer variables may arise, e.g., when an asset must be purchased 
in multiples of a base lot. If the number of such multiples is large, then a 
continuous approximation is reasonable; otherwise the discrete nature of the 
investment must be properly reflected in the optimization model. However, 
the most common model is a linear mixed-integer model in which all integer 
variables are actually logical. Non-linear mixed-integer programming models 
can be formulated, but efficient solvers are not that widespread commercially, 
although they are actually available. An exception is quadratic mixed-integer 
programming. Recent releases of ILOG CPLEX are able to tackle this class 
of models, which allow us to generalize mean-variance portfolio optimization 
models, as we shall see. 
12.1.1 Modeling with logical variables 
It is useful to point out a few situations that require the introduction of binary 
decision variables. 
Logical constraints Consider a set of N activities, perhaps investment oppor- 
tunities. Starting an activity or not is modeled by a corresponding binary 

566 
NON-CONVEX OPTIMIZATION 
decision variable xi, i = 1,. . . , N .  You might wish to enforce some logical 
constraints involving subsets of activities. Here are a few examples: 
Exactly one activity within a subset S must start (exclusive “or”): 
c x j  = 1. 
j € S  
0 At least one activity within a subset S must start (inclusive “or”): 
c x j  2 1. 
j € S  
At most one activity within a subset S may start: 
j € S  
If activity j is started, then activity k must start, too: 
xj 5 xk, 
All the constraints above may be generalized to more complex situations, 
which are relevant, for instance, if you want to enforce qualitative constraints 
on a portfolio of investments. 
Fixed-charge problem and semicontinuous decision variables We obtain LP mod- 
els when we assume, among other things, that the cost of carrying out a set 
of activities depend linearly on the activity levels. In some cases, the cost 
structure is more complex; the fixed-charge problem is one such case. We 
are given a set of activities, indexed by i = 1,. . . , N .  The level of activity i 
is measured by a non-negative continuous variable xi; the activity levels are 
subject to a set of constraints, formally expressed as x E S. Each activity has 
a cost proportional to the level xi and a fixed cost fi, which is paid whenever 
xi > 0. The fixed cost does not depend on the activity level. It is interesting 
to note that the cost function is in this case discontinuous at the origin, but 
a simple modeling trick allows us to build a mixed-integer model. 
Assume that we know an upper bound Mi on the level of activity i, and 
introduce a set of binary variables yi such that 
1 if zi > 0 
0 otherwise. 
Yi = { 
We can build the following model: 
N 
i=l 
s.t. 
xi 5 Miyi 
Vi 
X € S  
yi E (0, l} 
Vi. 
(12.1) 

MIXED-INTEGER PROGRAMMING MODELS 
567 
The inequality (12.1) is a common way to model fixed-charge costs. If yi = 0, 
necessarily xi = 0; if yi = 1, then we obtain xi 5 Mi, which is a non-binding 
constraint if Mi is large enough. Apparently, the constraint (12.1) allows a 
non-logical choice: pay the fixed charge, but let xi = 0. However, this is ruled 
out by the minimization of the objective function. 
Another common requirement on the level of an activity is that, if it is 
undertaken, its level should be in the interval [mi, Mi]. Note that this is not 
equivalent to requiring that mi 5 xi 5 Mi. Rather, we want something like 
which is a non-convex set (recall that the union of convex sets need not be 
convex). Using the same trick as above, we may just write 
These constraints define a semicontinuous decision variable. Semicontinuous 
variables may be used when the amount of an asset in a portfolio must be 
above a minimum threshold if the asset is included in the portfolio. 
Piecewise linear functions Sometimes we have to model a non-linear depen- 
dency between two variables; to name one case, transaction costs may depend 
in a non-obvious way on the trading volume. Although it is possible to adopt 
non-linear programming methods to cope with this case, it may be advisable 
to avoid the issue by approximating the non-linear function by a piecewise 
linear function; in other words, we may try a linear interpolation (see section 
3.3). Piecewise linear functions may arise quite naturally in applications. A 
few examples are shown in figure 12.1, where the points di) are the break- 
points separating the linearity intervals. There are different reasons for doing 
so. If the non-linear function occurs in an equality constraints, the problem is 
non-convex; the practical implication is that a non-linear optimizer may get 
stuck in a local optimum. The same happens if the objective function is non- 
linear and non-convex. Here we show that these cases may be transformed 
into mixed-integer programming problems which are non-convex but can be 
solved by branch and bound methods yielding a global optimum. Further- 
more, it may be the case that the model involves integer decision variables, 
in which case it may be preferable to keep the model linear, as non-linear 
mixed-integer programming problems may be overly difficult to solve. 
Consider a function like 
0 5 x 5 
f(x) = 
cz(x - x(1)) + C l Z ( l ) ,  
x(1) 5 x 5 x(2) 
{ c3(x 
clxl - x @ ) )  + c1x(1) + c2(x(2) - x
q
 x(2) 5 x 5 x(3). 
If c1 < c2 < c3 (increasing marginal costs), then f(x) is convex (figure 12.la); 
if c1 > c2 > cg (decreasing marginal costs), the function is concave (figure 

568 
NON-CONVEX OPTIMIZATION 
Fig. 12.1 Piecewise linear functions: (a) convex, (b) concave, (c) neither convex nor 
Co11CH.ve. 

MIXED-INTEGER PROGRAMMING MODELS 
569 
Fig. 12.2 hlotlelirig a piecewise linear function. 
12.111); for arbitrary slopes c7 the function is neither convex nor concave (figure 
The convex case is easy and it can be coped with by continuous LP models. 
Tlie function f(x) can be converted to a linear form by introducing three 
auxiliary variables y1, l ~ 2 ,  
l~:$ and substituting: 
2 = Y1 + Y2 + 93 
12.k). 
0 5 711 5 dl) 
0 5 y2 5 ( 2 3 2 )  - d 1 ) )  
0 5 yJ 5 (d 
%) - z(2)). 
T1ir.n wo ciiii cxprcss 
f(.) = CllJl + czy2 + C31J:3, 
sirice c'1 < ('2, ?/a is positive iii the optimal solution only if y1 is set to its upper 
Imintl. Sirriilarly, y:{ is ac:tivat,ed only if both y1 and y2 are satiirated to tlieir 
upper boiintls. If tlie function is not convex, this is not guaranteed, and we 
inust, cornc! iip with a rnodcling t,rick based on binary decision variables. 
To get a clue on how a general piecewise linear function may be modeled; 
assiiirir: that tlie function is described by the knots (zi,yi), y7 = f(zi), 
z = 
0,1,2: 3; as in figure 12.2. Any point on the line from (zz, pi) to (zi+lr y2+l) 
can l x  expressed as a convex combination: 
z =  
Xz, + (1 - X)Zi+l 
y 
= 
XlJi + (1 - X)y,+1, 
wlicw 0 5 X 5 1. Now wliat about foriiiiiig a convex combination of tlie four 
knots? 
3 
z = c x i z ;  
2 =o 

570 
NON-CONVEX OPTIMIZATION 
3 EX2 = 1, 
xi LO. 
i=O 
This is not really what we want, since this is the convex hull of the four 
knots (the shaded area in figure 12.2; see supplement S6.1). However, we are 
close; we have just to allow only pairs of adjacent coefficients Xi to be strictly 
positive. This is accomplished by introducing a binary decision variable si, 
i = 1,2,3, for each line segment (i - 1,i): 
3 
x = C xixi 
i=O 
3 
i=O 
0 I 
A0 I s1 
0 I 
A1 I s1 + s2 
0 I 
A2 L 32 + s3 
0 L A3 L 33 
3 
i=l 
In practice, optimization software packages and languages, such as AMPL, 
provide the user with an easier but equivalent way to express piecewise linear 
functions. 
Example 12.1 Assume we want to model a piecewise linear objective func- 
tion like those depicted in figure 12.1, where we have two breakpoints and 
three slopes. To express this in AMPL, we should use the keyword param to 
declare parameters corresponding to breakpoints and slopes, say xi, x2, cl, 
c2, and c3, and the keyword var to introduce a decision variable, say x. In 
AMPL, the objective function would include a term like: 
<<xl, x2; cl, c2, c3>> x 
We see that slopes are always one more than breakpoints: the first slope cl 
applies to values of x smaller than xl, and c3 applies to values larger than x2. 
AMPL detects automatically if, given the characteristics of the function and 
the sense of optimization (min or max), a continuous or a discrete optimization 
method is required. 
0 

MIXED-INTEGER PROGRAMMING MODELS 
571 
12.1.2 
Mixed-integer portfolio optimization models 
An efficient mean-variance portfolio may include a large set of assets, and some 
of them may account for a tiny part of the overall asset allocation. While this 
is, at least in principle, beneficial for diversification, there are a few downsides 
in a too diversified portfolio. One issue is the amount of transaction costs we 
have to pay, making small transactions unattractive. Another issue is the 
effort that is required in analyzing the historical data for too many assets, 
in order to control the portfolio risk. These requirements are particularly 
important for passively-managed funds, which cannot be expensive, since they 
just aim at tracking some target. We could extend the mean-variance model 
by constraining the portfolio cardinality, i.e., the number of assets included. 
Writing a constraint stating that at most k assets out of the I available may 
be included in the portfolio is easily accomplished by introducing, for each 
asset i = 1, . . . , I ,  the following binary variable: 
1 
0 otherwise. 
if asset i is included in the portfolio, 
6, = { 
Then all we have to do is to add the following constraints to the model: 
x, 5 Mt6, 
Vi 
(12.2) 
I 
(12.3) 
i=l 
where Mi is an upper bound on the weight of asset i. This is actually the same 
trick we have just described to model fixed costs in the fixed-charge problem. 
Another requirement could be enforcing a minimal limit to an asset weight 
if positive. This requirement cannot be enforced within a continuous linear 
or quadratic programming model. However, it is easy to extend constraint 
(12.2): 
mi& 5 xi 5 Midi 
Vi. 
This is an example of a semicontinuous variable. By the way, xi need not be 
the weight in a portfolio; it could be the amount of stock traded, in which 
case mi would be the minimal tradeable lot. We could even go further and 
require, in such a case, that xi is a general integer variable, in order to avoid 
the additional costs involved in trading odd lots. Putting all of this together, 
we can trace the efficient frontier by solving a set of mixed-integer quadratic 
programs like the following: 
i=l 

572 
NON-CONVEX OPTIMIZATION 
T 
risk 
b 
Fig. 12.3 Qiinlitativc skrtcli of a c.;lrdiriality-c.oristrairied efficient froiit,ic.r. 
i=l 
w; 2 0, si E (0,l) 
vz, 
where 
is the expected return of asset i, aij is the covariance between the re- 
turns of assets i and j ,  and 7~ is a target return. By varying the target return 
we would trace the efficient frontier. It is also important to realize that the 
efficient frontier will be qualitatively different from the usual one, which was 
illustrat.et1 in figure 2.12. A qualitative sketch of the cardinality-const,rained 
efficient, frontier is illustrated in figure 12.3. This plot may he understood by 
imagining of t,raciiig the efficient sets for each portfolio consisting of a suh- 
set of cardinality k ,  and then patching all of them together. One difficulty 
with the formulation above is that it is a mixed-integer quadratic, rather than 
linmr, problem. In principle, and in practice as well, it can be solved by 
the saine branch and bound algorithm illustrated in section 12.3.1; the only 
difference is t,hat the lower bounds are computed by solving a quadratic pro- 
gramming problem. Nowadays, commercial codes are available to tackle such 
prohlems efficiently; however, the computational requirements could turn out 
t,o be prohihitrive for a large-scale application. Still, different alternatives may 
lie tried. 
0 We may trace only the relevant part of the efficient set, given our risk 
aversion. 
0 In [3] ad hoc methods are discussed for mixed-integer quadratic pro- 
gramming; taking a route like this may be advantageous, but it requires 
writing our own code. 

MIXED-INTEGER PROGRAMMING MODELS 
573 
Another possibility is to simplify the model by reducing the data re- 
quirements, e.g., by assuming that all the correlations are equal. See 
[17] for an approach like this, and for additional references as well. 
Metaheuristics such as genetic algorithms and simulated annealing (sec- 
tion 12.4) may also be used [4]. 
If one wants to use MILP codes, it is also possible to devise a different 
representation of risk. In [9] the use of the mean absolute deviation has 
been advocated: 
where R, is the random return of asset i. This definition is quite similar 
to variance; an absolute deviation is used rather than a squared devia- 
tion. This objective may be translated in linear terms, and MILP meth- 
ods, exact or heuristic, may be applied. Suppose in fact that we have a 
set of historical returns rZt for each asset in time periods t = 1,. . . , T .  
Then we may estimate E[R,] = F, = (l/T) E:=l rZt and set 
N 
By the same token, we may approximate the objective function as 
This objective function may be expressed in linear form by introducing 
a set of auxiliary variables yt. The model will include, among other 
things, the following objective function and constraints: 
1 '  
min 
-Cyt 
t=1 
T 
N 
i = l  
N 
.. 
yt - C(rzt 
- F,)xz 2 0 
vt. 
i = l  
For instance, this approach is taken in [ll], where minimum transac- 
tion lots are dealt with. This approach does not require any statistical 

574 
NON-CONVEX OPT/M/ZAT/ON 
modeling, but we should mention that there is a risk of overfitting with 
respect to historical data. 
0 Finally, the MILP model may not really be aimed at building a portfolio 
from scratch. Rather, one could devise a target portfolio by whatever 
technique, subject to variety of constraints related to critical market 
exposure and liquidity. Then the target is approximated by enforcing 
some practical requirements, such as minimizing the number of assets 
included in the real portfolio. This is the approach taken in [2] to cope 
with a real-life case. 
A final important remark is that the difficulty of solving a mixed-integer 
problem depends on the strength of its relaxation (see section 12.3.1). The 
least one should do is to reduce the Mi bounds in constraints like (12.2). 
Thanks to careful modeling, computational times on the order of a few minutes 
are reported in [2] for problems involving something like 1500 assets (using 
what is now an old version of CPLEX). 
A last point is that classical mean-variance models neglect transaction 
costs. This is debatable in a single-period model, and is even more ques- 
tionable in a multiple-period model, since excessive trading may disrupt any 
advantage gained by optimizing the portfolio. The simplest idea is to use a 
linear model of the transaction cost; i.e., if we trade an amount xi of an asset, 
we pay a proportional cost o i x i ,  where the proportionality constant may de- 
pend on the asset liquidity. This results in a linear programming model, and 
one such formulation was given in section 11.2.3. However, a linear model 
fails to account for the dependence of transaction costs on the volume traded. 
Different assumptions can be made, depending on the nature of the traded 
asset, leading to different model formulations. In the case of fixed transaction 
costs, we may simply adopt the binary variable trick used earlier and treat it 
as a fixed cost. If transaction costs are non-linear, they may be approximated 
by piecewise linear functions, along the lines we illustrated at the beginning 
of this chapter. If we assume that transaction costs increase marginally with 
the traded volume (maybe because the asset is highly illiquid and it is difficult 
to deal with the sale/purchase order), the function is convex and can be dealt 
with by ordinary LP methods. However, in the case of concave costs, this is 
no longer the case, and mixed-integer models must be used. See also [lo] for 
an example of how a model involving fixed transaction costs may be tackled. 
Example 12.2 We illustrate here how AMPL can be used to express risk 
minimization subject to constraints on maximum cardinality of the portfolio 
and on target expected return. This is a fairly simple extension of the mean- 
variance model we illustrated in section C.2, in appendix C. The model file is 
illustrated in figure 12.4. We see that binary decision variables delta are in- 
troduced and linked to portfolio weights by the constraint LogicalLink. The 
maximum cardinality MaxAssets is enforced in constraint MaxCardinality. 
The corresponding data file is given, for a toy problem instance, in figure 12.5. 

MIXED-INTEGER PROGRAMMING MODELS 
575 
param NAssets > 0, integer; 
param MaxAssets > 0, integer; 
param ExpRet{l..NAssets); 
param CovMatCl. .NAssets, 1. .NAssets); 
param TargetRet ; 
var W{l..NAssets) 
>= 0; 
var delta{l..NAssets) binary; 
minimize Risk: 
sum Ci in 1. .NAssets, j in 1. .NAssets) W[il*CovMat[i,jl*W[j]; 
subject to SumToOne: 
sum {i in 1. .NAssets) W[i] = 1; 
subject to MinReturn: 
sum (i in 1. . NAssets) ExpRet [i] *W [i] = TargetRet ; 
subject to LogicalLink {i in l..NAssets): 
W[i] <= delta[i]; 
subject to MaxCardinality : 
sum {i in l..NAssets) deltari] <= MaxAssets; 
Fig. 12.4 AMPL model file for limited cardinality portfolio (MeanVarCard .mod). 
param NAssets = 3; 
param MaxAssets = 2; 
param ExpRet := 
1 0.15 
2 0.2 
3 0.08; 
param CovMat: 
1 
0.2000 
0.0500 
-0.0100 
2 
0.0500 
0.3000 
0.0150 
3 
-0.0100 
0.0150 
0.1000; 
1 
2 
3 
.= 
param TargetRet := 0.1; 
Fig. 12.5 AMPL data file for limited cardinality portfolio (MeanVarCard.dat) 

5 76 
NON- CON VEX 0 
PTlMlZA TI0 N 
Using AMPL, we may compare what happens here against what we have 
obtained in section C.2: 
AMPL Version 20021038 (x86-win32) 
ampl: model MeanVarCard.rnod; 
ampl: data MeanVarCard.dat; 
ampl: option cplex-options 'mipdisplay 2'; 
ampl: solve; 
CPLEX 9.1.0: mipdisplay 2 
MIP emphasis: balance optimality and feasibility 
Root relaxation solution time = 
0.05 sec. 
Nodes 
Cuts/ 
Node Left 
Objective IInf Best Integer 
Best Node ItCnt 
Gap 
0
0
 0.0631 
1 
0.0631 
7 
* 
o+ 
0 
0 
0.0633 
0.0631 
7 
CPLEX 9.1.0: optimal integer solution; objective 0.06326530612 
9 MIP simplex iterations 
1 branch-and-bound nodes 
ampl: display W; 
w [*I := 
1 0.285714 
2
0
 
3 0.714286 
, 
0.27% 
The first thing we should notice is that branch and bound is invoked, rather 
than just a barrier solver. We also see that asset 2 does not enter the portfolio, 
and that the cardinality constraint also implies an increase in risk. This 
increase is moderate here, but it should traded off against simplified portfolio 
management and the reduction in transaction costs in a real setting. 
0 
12.2 FIXED-MIX MODEL BASED ON GLOBAL OPTIMIZATION 
In the multistage stochastic programming models we have illustrated in sec- 
tion 11.2, we have assumed that the portfolio could be freely rebalanced at 
specified time instants. A different type of model is obtained if we assume 
that the asset mix is held constant over the whole period. This means that 
the proportion of wealth that we allocate to each asset is kept constant; thus, 
we trade according a sell-high/buy-low strategy. Using the same notation as 
in section 11.2.1, we have a discrete set of scenarios, each with a probability 
p,, s = 1 . .  . , S, where the returns are represented by R:t. Now, the decision 
variables are simply the proportion of wealth allocated to each asset, denoted 
by xi; note that since there is no recourse action, the scenarios need not be 
structured according to a tree, as the non-anticipativity condition is immedi- 
ately satisfied, given the definition of the decision variables. The model we 

FIXED-MIX MODEL BASED ON GLOBAL OPTIMIZATION 
577 
describe here is due to [12], to which we refer the reader for further informa- 
tion and for computational experiments, and is basically an extension of the 
mean-variance framework; no liability is considered, and we base our objective 
function on the terminal wealth. 
Let WO be the initial wealth. Then the wealth at the end of time period 1 
in scenario s will be 
I 
i=l 
Note that the wealth is scenario-dependent, but the asset allocation is not. In 
general, when we consider two consecutive time periods, we have 
I 
vt, s. 
i=l 
The wealth at the end of the planning horizon is 
Within a mean-variance framework, we may build a quadratic utility function 
depending on the terminal wealth. Given a parameter X linked to our risk 
aversion, the objective function will be something like 
max XE[WT] - ( 1  - A )  Var(WT). 
To express the objective function, we must recall that Var(X) = E[X2] - 
E2[X], and we may write the model as 
s=l 
Lt=1 \i=1 
/ J  
I 
s.t. 
E
X
i
 = 1 
i=l 
0 5 zz _< 1. 
This looks like a very complex problem; however, while the objective function 
is a bit messy, the constraints are quite simple. The real difficulty is that this 
is a non-convex problem. To see why, just note that the objective turns out to 

5 78 
NON- CO N VEX OP TlMlZA TI0 N 
be a polynomial in the decision variables; since polynomials may have many 
minima and maxima, we have a non-linear non-convex problem. 
The problem may be tackled by the branch and bound methods described 
in section 12.3. In particular, the idea of bounding a non-convex function by 
a convex underestimator is used in [12]. If complicating features are added 
to the model, this may turn out a quite difficult mixed-integer non-linear 
problem; in this case, the use of metaheuristics such as tabu search may be 
the best option [6]. 
It is useful to interpret this approach within an integration framework of 
simulation and optimization. Actually, simulation is separated from optimiza- 
tion, since scenarios are generated beforehand; we evaluate the solutions on 
the same set of scenarios, which is consistent with variance reduction by com- 
mon random numbers. After the optimization, simulation could be used to 
evaluate the solution we obtain on a larger set of scenarios, possibly includ- 
ing stress test scenarios; in other words, we may carry out an out-of-sample 
analysis to check the robustness of the solution. This is easily accomplished 
for a fixed-mix policy, but not for a dynamic policy, as this would require the 
repeated solution of difficult multistage stochastic programs. In fact, even if 
a fixed-mix policy is in principle an inferior policy with respect to a dynamic 
one, it may be more robust in practice; what’s more important, it is easier 
to prove its robustness with respect to an arbitrary set of scenarios, and to 
persuade a manager to adopt it. 
Selection of the best portfolio management policy is actually an open is- 
sue, but it is worth noting that the fixed-mix policy is only the simplest 
policy structure that we may consider for the integration of simulation and 
optimization. More complex policies could be devised, depending on a set of 
numerical parameters, whose value may be set by the integration of simulation 
and optimization methods. 
12.3 BRANCH AND BOUND METHODS FOR NON-CONVEX 
0 
PTI M I Z AT1 0 N 
Consider a generic optimization problem 
P ( S )  : 
and assume that it is a difficult one, as either the objective function or the 
feasible set is non-convex. Consider figure 12.6; in the first case, the objective 
function has local minima; in the second case, the feasible set is discrete, 
and hence non-convex. While solving non-convex problems is very difficult in 
general, in some cases it could be made a straightforward task if a suitable 
convexification were available. For instance, if S is convex but f is not, we 
could take the convex hull of the epigraph of f ,  as illustrated in figure 12.7. 
Taking the convex hull of the epigraph of f yields a function h such that: 

BRANCH AND BOUND METHODS FOR NON-CONVEX OPTlMlZATlON 
579 
w 
IX
fig. 12.6 N(JII-COIIV~Y. 
ol).jer.(ive function and discrete non-coiivex feasible set. 
X 

580 
NON-CONVEX OPT/M/ZAT/ON 
X 
b 
XI 
b 
Fig 12.8 Convex lower l)oiinding function and a relaxation of a discrete feasible sct. 
0 h is convex on S. 
0 h(x) 5 f(x) for any x E S 
0 If y is a convex function such that g(x) 5 f(x) for any x E S, then 
In this case, we could think of replacing f by h and solve the problem by 
convex optimization techniques. By the same token, consider a linear integer 
pi ogramining problem: 
y(x) 5 17(x) for any x E S. 
(PI) 
rniri 
c'x 
s.t. 
Ax 5 b 
x E zi;. 
The feasihle set is a discrete set much like that in figure 12.6. If we knew its 
coiivcx hull, illustrated in figure 12.7, we could simply tackle the problem as 
an ordinary LP prohleni by the simplex method. In fact, the convex hull of a 
discrete set of points is a polyhedron; if the points have integer coordinates, 
tliw the cxtrerne points of the convex hull will be integer too, and one of them 
will turn out to be the optimal solution returned by the simplex method.' 
Uiifortunatcly, we arc rarely in the lucky position of heing able to find such 
a convexification easily. However, we might he able to find weaker convex 
objects, as illustrated in figure 12.8. They are exploited to define a relaxation 
of the original problem. 
DEFINITION 12.1 An optzmizatzon problem, 
RP(T) : 
niinh(x), 
XET 
'We recall from section 6.5.1 that interior point methods, when alternative optima exist, 
tend to yield a solution on the center of a face of the polyhedron defining the feasible set. 

BRANCH AND BOUND METHODS FOR NON-CONVEX OPTIMIZATION 
581 
is a relaxation of problem P(S) if: 
0 S c T .  
0 h(x) 5 f(x), f o r  any x E S. 
Solving a relaxation does not yield the optimal solution of the original 
problem in general, but it gives a lower bound for its optimal value. 
Example 12.3 Consider a non-convex function f (x) on a hyperrectangle S 
defined by the bounds 
l j < x J 5 u j ,  
j = l  ,..., n. 
Assume that f is twice continuously differentiable. In supplement S6.1.1 
we stated that a twice continuously differentiable function is convex if its 
Hessian matrix is positive semidefinite, which is equivalent to requiring that 
its eigenvalues are non-negative. We may build a convex underestimating 
function for f by adding an additional term and considering 
n 
i=l 
for some a > 0. It is easy to see that the additional term is nonpositive on 
the region S and that it is zero on its boundary. Thus h is an underestimator 
for f. It will be convex if a is large enough. To see this, consider how the 
Hessian H of h is related to the Hessian Hf of the original objective f: 
d2 f 
ax: 
- + f a ,  
i = l ,  ..., n 
- -  
- 
d2h 
The eigenvalues of h are the solution of the following equation: 
det(Hf + 2aI - p1) = det(Hf - ( p  - 2a)I) = 0. 
It is easy to see that, if the eigenvalues of Hf are Xi, i = 1,. . . , n, then the 
eigenvalues of the Hessian of h are simply 
pz = Xi + 2a, 
which may be made positive by choosing a suitably large value of a. We will 
see shortly that a relaxation should be as tight as possible. This means that 
the underestimating function should be as large as possible and that a should 
be as small as possible. Guidelines for the selection of a are given in the 
original reference [ 131. 
0 

582 
NON-CONVEX OPTIMIZATION 
Example 12.4 Consider the integer programming problem (IP). A convex 
relaxation of the feasible set 
S = {x : Ax 5 b;x E ZS;) 
can be obtained by dropping the integrality requirement: 
T = {X : AX 5 b; x E Ry}. 
This yields an LP problem which is readily solved by the simplex method. 
In general, some components of the solution of the relaxed problem will be 
fractional; this implies that the solution we obtain is not feasible, but we get 
a lower bound on the optimal value of the objective function. 
0 
We have seen, in the two examples above, that when the relaxed problem is 
convex, it is easily solved, but it will only yield a lower bound on the optimal 
value of the objective function. 
A possible solution strategy is to decompose the original problem P(S) by 
splitting the feasible set S into a collection of subsets S1,. . . , S, such that 
s = s1 u s2 u 
* . . u s,; 
then we have 
The rationale behind this decomposition of the feasible set is that we may 
expect that solving the problems over smaller sets is easier; or, at least, the 
lower bounds obtained by solving the relaxed problems will be tighter. For 
efficiency reasons it is advisable, but not strictly necessary, to partition the 
set S in such a way that 
Si n Sj = 0, 
i fj. 
This type of decomposition is called brunching. 
Example 12.5 Consider the binary programming problem: 
min 
c'x 
s.t. 
x E S = {X 1 AX 2 b; ~j E (0,l)). 
The problem may be decomposed in two subproblems by picking a variable 
xp and fixing it to 1 and 0: 
s1 = {x E s xp = 0) 
s2 = {x E s; xp = 1). 
The resulting problems P(S1) and P(S2) can be decomposed in turn, until 
eventually all the variables have been fixed. The branching process can be 
pictorially represented as a search tree, as shown in figure 12.9. 
0 

BRANCH AND BOUND METHODS FOR NON-CONVEX OPTIMIZATION 
583 
Fig. 12.9 Search tree for a binary prograruming problem. 
The 1)ranching process leads to easier problems. In the example, the leaves 
of the search tree are trivial problems, since all variables are fixed to one 
of the t.wo fmsible values; actually, the search tree is, in this case, just a 
way to eniiinerttte the possible solutions. Unfortunately; there are a large 
nunher of letaves: if x E (0, l } N ,  
there are 2N possible solutions. Actually, 
the constraints Ax b rule out many of them, but a brute-force enumeration 
is not feasihle except for the smallest problems. 
To reduce the computational burden, one can try to eliminate a subproblem 
P(S,+) or, equivalently, a node of the tree, by showing that it cannot lead to 
the optimal solution of P(S). This can be accomplished if it is possible to 
cwnpute a lower bound for each subproblem by a convex relaxation or by 
whatever method. Let ~ [ P ( S A J ]  
denote the optimal value of problem P(SA.). 
The lower bound /3[P(Sk)] is such that 
Now assume that we know a feasible, but not necessarily optiinal solution x 
of P(S). Such a solution, if any exists, is eventually found while searching the 
tree (with the exception of pathological cases). The value f(x) is an upper 
1)ound 011 the optimal value v* = v[P(S)]. 
Clearly, there is 110 point in solving 
ii siibprol)lcm P(Sk) if 
0[P(Sk)I L f(2). 
(12.4) 
In fact. solving this subprobleiri cannot yield an improvement with respect to 
feasible solution x that we already know. In this case, we can eliminate P(Sk) 
from further considcration; this elimination, called futhornzng, corresponds to 
pruning a branch of the search tree. Note that P(Sk) can be fathomed only by 
comparing the lower bound P[P(Sk)] with an upper bound on v[P(S)]. 
It is 

584 
NON-CONVEX OPTIMIZATION 
not correct to fathom P(Sk) on the basis of a comparison with a subproblem 
P(S,) such that 
P[p(Sz)] < P[P(sk)]* 
The branching and fathoming mechanism is the foundation of a wide class of 
algorithms known as branch and bound methods. In the next subsection we 
outline the basic structure of branch and bound methods for mixed-integer 
linear programming (MILP) problems. These methods are widely available 
in commercial optimization software libraries. On the contrary, branch and 
bound methods for non-convex continuous problems require ad hoc coding in 
practice. 
12.3.1 LP-based branch and bound for MILP models 
The fundamental branch and bound algorithm can be outlined as follows. 
At each step we work on a list of open subproblems, corresponding to nodes 
of a search tree, and we try to generate a sequence of improving incumbent 
solutions until we can prove that an incumbent solution is the optimal one. 
At intermediate steps, the incumbent solution is the best feasible (integer) 
solution found so far; the incumbent solution, for a minimization problem, 
provides us with an upper bound on the value of the optimal solution. We give 
the algorithm for a minimization problem; it is easy to adapt the algorithm 
to a maximization problem. 
Fundamental branch and bound algorithm 
1. Initialization. The list of open subproblems is initialized to P(S); the 
value of the incumbent solution v* is set to +oo. 
2. Selecting a candidate subproblem. If the list of open subproblems is 
empty, stop: the incumbent solution x*, if any has been found, is opti- 
mal; if v* = +oo, the original problem was infeasible. Otherwise, select 
a subproblem P(sk) from the list. 
3. Bounding. Compute a lower bound p(Sk) on v[P(Sk)] by solving a 
relaxed problem P(sk). Let Fk be the optimal solution of the relaxed 
subproblem. 
4. Prune by optimality. If Xk is feasible, prune subproblem P(sk). Fur- 
thermore, if f (Xk) < v*, update the incumbent solution x* and its value 
v*. Go to step 2. 
5. Prune by infeasibility. If the relaxed subproblem P(sk) is infeasible, 
eliminate P(sk) from further consideration. Go to step 2. 
6. Prune by bound. If P(Sk) 2 v*, eliminate subproblem P(Sk) and go to 
step 2. 

BRANCH AND BOUND METHODS FOR NON-CONVEX OPTlMlZATlON 
585 
7. Branching. Replace P(Sk) in the list of open subproblems with a list of 
child subproblems P(Skl), P(Sks),. . ., P(Skq), obtained by partitioning 
s k ;  go to step 2. 
To apply this algorithm successfully, we must cope with the following issues: 
How to compute a strong lower bound efficiently 
0 How to branch to generate subproblems 
0 How to select the right candidate from the list of open subproblems 
The last issue is very important and calls for selecting a strategy to explore 
the tree. One possibility is to explore the most promising node first, in terms 
of lower bound; this yields the best-bound strategy. Another possibility is 
the depth-first strategy, whereby the last generated node is explored first; 
this strategy may have the merit of limiting the memory space required to 
store the search tree. In practice, we should also pay attention to how far the 
solution of a relaxed problem is from integrality. In example 12.8 below we 
will also check the effect of these choices. 
Commercial branch and bound procedures compute bounds by the follow- 
ing LP-based (continuous) relaxation. Given a MILP problem 
P(S) 
min 
c'xfd'y 
s.t. 
Ax + Ey 5 b 
XEW;', 
Y E Z ? ,  
the continuous relaxation is obtained by relaxing the integrality constraints: 
P ( s )  
min 
c'x+d'y 
s.t. 
Ax + Ey 5 b 
[j 
E W;'+? 
Ideally, the relaxed region 
should be as close as possible to the convex hull 
of S; the smaller 3, 
the larger the lower bound. Tighter lower bounds make 
pruning by bound easier. To this end, careful model formulation may help. 
Example 12.6 Consider a fixed-charge model in which the level of activity i 
is measured by the continuous decision variable xi and the decision of starting 
that activity is modeled by the binary decision variable 6i E (0,l). To relate 
the two decision variables, we may write the constraint 
where Mi is an upper bound on the level x i .  When we solve the continuous 
relaxation, we drop the integrality constraint on S i ,  and we replace it by 

586 
NON-CONVEX OPTIMIZATION 
6i E [0, 11. In principle, Mi may be a very large number, but to get a tight 
relaxation, we should select Mi as small as possible. 
0 
Example 12.7 In example 1.2 we have considered how the basic knapsack 
model can be extended to deal with interactions among activities: in the 
example, activity 0 may be started only if all of the activities within a certain 
subset may be started. A possible constraint to model this requirement is 
N 
where xo E (0,l) models the decision of starting activity 0, and xi E ( 0 , l )  is 
related to the N activities in the subset conditioning activity 0. An alternative 
and equivalent formulation is 
X O < Z ~ ,  
i = l ,  ... , N .  
On the one hand, this disaggregated form entails more constraints and prob- 
ably require more work in solving the continuous relaxation. However, when 
we consider the continuous relaxation, all the points that are feasible for the 
disaggregate formulation are feasible for the aggregate constraint, but not vice 
versa. Hence, the feasible set for the relaxation of the disaggregate formula- 
tion is smaller, and the lower bound is tighter. Such a reformulation, as well as 
others, is carried out automatically by some packages (..gel CPLEX) and may 
cut the computational effort of a branch and bound algorithm considerably. 
0 
As to branching, the following strategy is commonly applied to general in- 
teger variables. Assume that an integer variable y j  takes a non-integer value 
$j in the optimal solution of the relaxed subproblem (one must exist; other- 
wise, we would prune by feasibility). Then two subproblems are generated; in 
the down-child we add the constraint 
to the formulation; in the up-child we add 
yj L LYj] + 1. 
For instance, if yj = 4.2, we generate two subproblems with the addition of 
constraints y j  5 4 (for the down-child) and y j  2 5 (for the up-child). 
A thorny issue is which variable we should branch on. Similarly, we should 
decide which subproblem we select from the list at step 2 of the branch and 
bound algorithm. As is often the case, there is no general answer; software 
packages offer different options to the user, and some experimentation may 
be required to come up with the best strategy. 

BRANCH AND BOUND METHODS FOR NON-CONVEX OPTIMIZATION 
587 
Quite impressive improvements have been made in commercial branch and 
bound packages. Despite this, some large-scale problems cannot be solved 
to optimality within a reasonable amount of time. If this is the case, one 
possibility is to run branch and bound with a suboptimality tolerance. Instead 
of pruning a subproblem P(Sk) only if the lower bound is larger than or equal 
to the incumbent, P(Sk) 2 u*, we may introduce a tolerance parameter E and 
eliminate a node in the tree whenever 
Doing so, we have only the guarantee of finding a near-optimal solution, but we 
have a bound on the level of suboptimality. In exchange, we may considerably 
reduce the computational effort. Whet we get is a mathematically motivated 
heuristic. Of course, heuristics need not be based on mathematical principles, 
but before considering heuristics, we would like to illustrate branch and bound 
in some detail. 
Example 12.8 In section (2.3 (page 652) we show how the following knap- 
sack problem can be solved by AMPL: 
max 
s.t. 
10x1 + 7x2 + 25x3 + 24x4 
221 + 1x2 + 6x3 + 524 5 7 
xi E (0,l). 
The same problem can be solved by MATLAB using bintprog. A script for 
doing so is illustrated in figure 12.10. The script is very simple; the only 
noteworthy point is strategy selection. In the first run we use the depth-first 
exploration strategy, whereas the second run uses best-node. Strategies are 
selected as usual in the Optimization toolbox, building a option structure 
by optimset. We may also see that there is some difference between the two 
strategies: 
>> knapsack 
Optimization terminated. 
Optimization terminated. 
Optimal solution: 1 0 0 1 
Value: 34 
Nodes with depth-first : 9 
Nodes with best-node: 7 
A fair number of nodes is explored to find the optimal solution and prove 
its optimality. It is very instructive to try doing branch and bound manually 
using linprog. We must use the simplex algorithm in this case, because of its 
tendency to yield extreme solutions, when multiple ones exist, which means 
that they tend to be integer. 
We first solve the root problem (Po) in the tree, which is the continuous 
relaxation of the binary problem: 

588 
NON-CONVEX OPTlMlZATlON 
% Knapsack.m 
A = [2 1 6  51; 
b = 7; 
c = - [lo 7 25 241; 
options = optimset(’NodeSearchStrategy’,’df’); 
[x, value, exitflag, outputdf] = bintprog(c,A,b, [I, [I, [I ,options); 
options = optimset(’NodeSearchStrategy’,’bn’); 
[x, value, exitflag, outputbn] = bintprog(c,A,b, [I, [I, [I ,options); 
fprintf(1,’Optimal solution: ’, x ’ ) ;  
fprintf(l,’%d ’, x’); 
fprintf(l,’\nValue: %d\n’, -value); 
fprintf (1,’Nodes with depth-first: %d\n’, outputdf .nodes); 
fprintf (1, ’Nodes with best-node: %d\n’, outputbn.nodes) ; 
Fig. 12.10 MATLAB script to solve a simple knapsack problem. 
>> options = optimset(’LargeScale’, ’off’, ’Simplex’, ’on’); 
>> A = [2 1 6  51; 
>> b = 7; 
>> c = - 
>> lb = zeros(4,l) ; 
>> ub = ones(4,l); 
>> [x, val] = linprog(c,A,b, [I, [I ,lb,ub, [I ,options) 
Optimization terminated. 
[lo 7 25 241; 
x =  
1.0000 
1.0000 
0 
0.8000 
-36.2000 
Val = 
We see that the value of the objective is 36.2, which is an upper bound on the 
optimal value 34 (recall that we are maximizing and that there is a change in 
the sign of the objective), and that 2 4  is fractional. We may branch on this 
variable by generating subproblems PI, where 2 4  = 0, and Pz, where 24 = 1. 
Let us solve P1 first: 
>> Aeq = [O 0 0 11; 
>> beq = 0; 
>> [x, vall = linprog(c,A,b,Aeq,beq,lb,ub, [I ,options) 
Optimization terminated. 
x =  
1.0000 
1.0000 
0.6667 

BRANCH AND BOUND METHODS FOR NON-CONVEX OPTIMIZATION 
589 
0 
Val = 
-33.666 
We see that the solution is getting worse because of the additional constraints. 
Solving P2, we get 
>> Aeq = [O 0 0 11; 
>> beq = 1; 
>> [x, val] = linprog(c,A, b ,Aeq, beq, lb,ub, [I ,options) 
Optimization terminated. 
x =  
0.5000 
1.0000 
0 
1.0000 
Val = 
-36 
This relaxation looks more promising, so we branch from here, generating 
subproblems P3, where 5 1  = 0, and P4, where 2 1  = 1. It is easy to see that 
P4 yields the integer solution x1 = 2 4  = 1, 2 2  = 23 = 0, with value 34. Now 
we may eliminate PI, since its bound shows that this subproblem cannot yield 
the optimal solution. However, we have not finished yet, because subproblem 
P3 yields a promising fractional solution: 
>> Aeq = [O 0 0 1; 1 0  0 01; 
beq = [1;01 ; 
[x, val] = linprog(c,A,b,Aeq,beq,lb,ub,[],options) 
Optimization terminated. 
x =  
0 
1.0000 
0.1667 
1.0000 
-35.1667 
Val = 
We leave to the reader the task of verifying that branching on 53 = 0, we get 
a solution with value 32, whereas 2 3  = 1 yields an unfeasible problem (we 
have three items in the knapsack, exceeding its capacity). Hence, we have 
proven that the optimal solution has value 34, after exploring a few nodes. It 
is important to notice that a brute force enumeration strategy would require 
the exploration of 24 = 16 possible solutions. Now what about AMPL? Well, 
you can see from the appendix that AMPL/CPLEX uses zero branch and 
bound nodes: 
amp1 : model Knapsack .mod; 

590 
NON-CONVEX OPTIMIZATION 
ampl: data Knapsack.dat; 
ampl: options cplex-options 'mipdisplay 2'; 
ampl: solve; 
CPLEX 9.1.0: mipdisplay 2 
Clique table members: 2 
MIP emphasis : balance optimality and feasibility 
Root relaxation solution time = 
0.02 sec. 
Nodes 
Cuts/ 
Node Left 
Objective IInf Best Integer Best Node ItCnt 
Gap 
0
0
 36.2000 
1 
36.2000 
1 
* 
34.0000 
0 
34.0000 
Cuts: 3 
3 0.00% 
* 
o+ 
0 
0 
32.0000 
36.2000 
1 13.12% 
Cover cuts applied: 1 
Implied bound cuts applied: 1 
CPLEX 9.1.0: optimal integer solution; objective 34 
3 MIP simplex iterations 
0 branch-and-bound nodes 
How is this possible? If we check the budget constraint, it is easy to see that 
item 1 and 3 cannot be both selected, as their total capacity is 8 and it exceeds 
the available budget. Hence we might add the constraint: 
which is obviously redundant in the discrete domain, but is not redundant 
in the continuous relaxation. By the same token, we could add the following 
constraints 
2 3  + 2 4  I 1 
21 + 2 2  + 2 4  I 2 
Such additional constraints are called cover inequalities and may contribute 
to strengthen the bound from the LP relaxation, cutting the CPU time con- 
siderably. If we try solving the LP relaxation in MATLAB, adding the three 
cover inequalities, we get 
> > A l = [ 2 1 6 5 ;  1 0 1 0 ; 0 0 1 1 ;  1 1 0 1 1 ;  
bl = [7;1;1;21; 
c = -  110 7 25 241; 
lb = zeros(4,l); 
ub = ones(4,l); 
[x, val] = linprog(c,Al,bl, [I, [I ,lb,ub, [I ,options) 
Optimization terminated. 
x =  
0.3333 
1.0000 

HEURISTIC METHODS FOR NON-CONVEX OPTIMIZATION 
591 
0.3333 
0.6667 
V a l  = 
-34.6667 
We see how cover inequalities my strengthen the relaxation. Now we may 
conclude that the optimal solution cannot be worth more than 34, since all 
the coefficients in the model are integer. AMPL/CPLEX is able to exploit 
this and other type of inequalities to reduce the computational requirements 
of branch and bound. The automatic generation of inequalities is also called 
cut generation, as we aim at cutting the relaxed feasible region in order to 
get as close as possible to the convex hull of integer solutions. Efficient cut 
generation is not trivial, as it is important to generate only the effective cuts; 
the reader may play with MATLAB to check that in the toy example above, 
not all the cover inequalities are really helpful as some are actually redundant. 
[I 
In the example above, we may appreciate the sophistication of state-of-the-art 
packages for mixed-integer programming. We should also stress that heuristics 
may actually be integrated within a branch-and-bound procedure. The role 
of heuristics is to generate, given a nearly-integer solution, a feasible solution; 
if this is of good quality, it will improve the incumbent solution and the upper 
bound against which we compare lower bounds. In the ILOG CPLEX trace 
above whenever you see an asterisk (*) in a row, it means that the search 
process has found a new incumbent. When you also see a plus (+), it means 
that it was found by a heuristic. One possibility to devise such heuristics is 
clever rounding; rounding does not work in general, if we use it to find an 
optimal solution, but when the continuous relaxation is tight enough, it may 
yield very good solutions. Another principle that can be exploited is local 
search, which is introduced in the next section. 
12.4 
HEURISTIC METHODS FOR NON-CONVEX OPTIMIZATION 
When a branch and bound method is not able to yield an optimal or near- 
optimal solution with a reasonable effort, we may settle for a quick heuristic 
method able to provide us with a good solution. For any specific problem 
it is possible to devise an ad hoc method. However, it is interesting to con- 
sider relatively general principles which, with some adaptation, may yield 
good heuristics for a wide class of problems. Local search metaheuristics’ are 
quite popular and have also been proposed for financial problems. They were 
originally developed for discrete optimization problems; however, they may 
’This name reflects the relatively general nature of the principle. In practice, a good deal 
of customization is needed to come up with a truly effective method for a specific problem. 

592 
NON-CONVEX OPTIMIZATION 
also be applied to continuous non-linear programming when the objective is 
non-convex. 
Local search algorithms are similar to the gradient method for non-linear 
programming. The basic idea is to improve a known solution by applying a 
set of local perturbations. Consider a generic optimization problem 
defined over a discrete set S. Given a feasible solution x, a neighborhood 
n/(x) is defined as the set of solutions obtained by applying a set of sim- 
ple perturbations to x. Different perturbations yield different neighborhood 
structures. 
The simplest local search algorithm is local improvement. Given a current, 
or incumbent, solution 3, an alternative (candidate) solution xo is searched 
for in the neighborhood of the incumbent, such that 
f(xo) = min f(x). 
XEN(Z) 
If the neighborhood structure N(.) 
is simple enough, the minimization above 
can be performed by an exhaustive search; we speak of a best-improving 
method since we try to find the best solution in the neighborhood. Clearly, 
there is a trade-off between the effectiveness of the neighborhood structure 
(the larger the better) and the efficiency of the algorithm. If f(xo) < f(3), 
then xo is set as the new current solution and the process is iterated. If 
f ( x o )  2 f(3), the algorithm is stopped. A possible variation is to partially 
explore the neighborhood of the current solution until an improving solution 
is found; this approach is known as first-improving, since we do not explore 
the entire neighborhood before committing to a new current solution. 
The neighborhood structure is problem dependent. In the case of discrete 
optimization problems, devising a neighborhood structure may be relatively 
straightforward. For instance, in a capital budgeting problem, the solution is 
represented by the subset of selected projects. The neighborhood might be 
generated by exchanging a project within the current subset with a project 
not included in it. In a general programming problem with binary variables, 
one might consider complementing each variable in turn. Actually, devising a 
clever and effective neighborhood is not as trivial as it might seem, since due 
attention must be paid to constraints. In the case of continuous variables, a 
further complication arises; we may generate neighboring points by moving 
along a set of directions, but we must find a way to select the step size. To 
this aim, dynamic strategies have been devised (see, e.g., [6] for a financial 
application). 
This basic idea is generally easy to apply, but it has one major drawback: 
The algorithm usually stops in a locally (with respect to the neighborhood 
structure) optimal solution. This is the same difficulty we face when applying 
the gradient method to a non-convex objective function; the reason behind 

HEURISTIC METHODS FOR NON-CONVEX OPTIMIZATION 
593 
the trouble is that only improving perturbations [i.e., such that A f = f (x') - 
f(z) < 01 are accepted. To avoid getting stuck in a local optimum, we must 
relax this assumption. 
In the following we describe three local search approaches that have been 
proposed to overcome the limitations of local improvement: simulated anneal- 
ing, tabu search, and genetic algorithms. 
Simulated annealing It has been pointed out that to overcome the problem 
of local minima, we have to accept, in some disciplined way, non-improving 
perturbations, i.e., perturbations for which Af > 0. Simulated annealing is 
based on an analogy between cost minimization in discrete optimization and 
energy minimization in physical systems. The local improvement strategy 
behaves much like physical systems do, according to classical mechanics. It 
is impossible for a system to have a certain energy at a certain time and to 
increase it without external input: If you place a ball in a hole, it will stay 
there. This is not true in thermodynamics and statistical mechanics; according 
to these physical models, at a temperature above absolute zero, thermal noise 
makes an increase in the energy of a system possible. An increase in energy is 
more likely to occur at high temperatures. The probability P of this upward 
jump depends on the amount of energy AE acquired and the temperature T ,  
according to the Boltzmann distribution 
P(AE, T )  = exp -- 
( iET), 
where K is the Boltzmann constant. 
Annealing is a metallurgical process by which a melted material is slowly 
cooled in order to obtain good (low-energy) solid-state configurations. If the 
temperature is decreased too fast, the system gets trapped in a local energy 
minimum, and a glass is produced. But if the process is slow enough, random 
kinetic fluctuations due to thermal noise allow the system to escape from local 
minima, reaching a point very close to the global optimum. 
In strict analogy with statistical mechanics, in the simulated annealing 
method a perturbation of the current solution yielding Af < 0 is always 
accepted; a perturbation with A f > 0 is accepted with a probability given by 
a Boltzmann-like probability distribution 
P ( A f , T )  = e x p ( - F ) .  
This probability distribution is a decreasing exponential in A f ,  whose shape 
depends on the parameter T ,  acting as a temperature (see figure 12.11). The 
probability of accepting a non-improving perturbation decreases as the dete- 
rioration of the solution increases. For a given A f ,  the acceptance probability 
is higher at high temperatures. For T -+ 
0 the probability collapses into a 
step function, and the method behaves like local improvement. For T + +oo 

594 
NON-CONVEX OPTIMIZATION 
T decreasing s 
Fig. 12.11 Ac cqttti1c.e probabilities as a funct,ian of cost increase for tliffertliit t,rrii- 
perat tires. 
the probability is 1 everywhere, and we have a random exploration of the 
solutions space. The parameter T allows balancing the need to expZoit the 
solut,ion a.t hand by improving it and the need to explore the solution space. 
The simulated annealing method simply substitutes the deterministic ac- 
ceptance rule of local improvement with a probabilistic rule. The temperatmure 
is set to a relatively high initial value T I ,  and the algorithm is iterated using 
at step I; a temperature T k  until some termination criterion is satisfied. The 
strategy by which the temperature is decreased is called the cooling schedule. 
The simplest cooling schedule is 
Ti: = a T k - 1 ,  
0 < (Y < 1. 
In practice, it is advisable to keep the temperature constant for a certain num- 
her of skps, in order to reach a thermodynamic equilibrium before changing 
the coiitrol paramet.er. More sophisticated adaptive cooling strategies have 
tieen proposed, biit, t,he increasc in complexity does not always seem justi- 
fictl. A very siniple implementation of the annealing algorithm could be the 
following: 
Step 1. Choose an initial solution Zold, an initial temperature T I ,  and 
a decrease parameter a; let k = 1, fold = f(z,ld); let f = fC,lc1 
and 2 = z,ld be the current optimal value and optimal solution, 
respectively. 
Step 2. Randomly choose a candidate solution xncw from the neigh- 
liorhootl of zc,lcl , and compute its value f,,c.w. 
Step 3. Set, the acceptance probability 

H EURlSTlC ME TH ODs FOR N ON-CON VEX OPTlM IZATION 
595 
Step 4. Accept the new solution with probability P; if accepted, set 
xold = xnew and fold = fnew; if necessary, update f and 2. 
Step 5. If some termination condition is met, stop; otherwise, set 
k = k + 1, set the new temperature according to the cooling 
schedule, and go to step 2. 
The probabilistic acceptance is easy to implement. P is evaluated according 
to the Boltzmann distribution; then a pseudorandom number U ,  uniformly 
distributed between 0 and 1, is generated and the move is accepted if U 5 P 
(pseudorandom number generation is dealt with in section 4.3). 
The termination condition could be related to a maximum iteration num- 
ber, to a minimum temperature, or to a maximum number of steps in which 
the current solution remains unchanged. Note that we do not explore the en- 
tire neighborhood of the current solution; the method is of the first-improving 
type. If a candidate solution is rejected, we select another candidate in the 
neighborhood of the current solution. In principle, it is possible to visit the 
same solution twice; if the neighborhood structure is rich enough, this is un- 
likely. It is necessary to save the best solution found, since the freezing point 
(the last current solution) need not be the best solution visited. 
An implementation of the annealing algorithm is therefore characterized 
by the solution space, the neighborhood structure, the rule by which the 
neighborhood is explored, and the cooling schedule. It can be shown that un- 
der some conditions, the method asymptotically converges (in a probabilistic 
sense) to the global optimum. The convergence property is a reassuring one, 
but it is usually considered of little practical value, since its conditions would 
require impractical running times. However, the experience suggests that 
in many practical settings, very good solutions (often optimal) are actually 
found. The running time of the algorithm to obtain high-quality solutions, 
however, is problem dependent. 
Tabu search Like simulated annealing, tabu search is a neighborhood search- 
based metaheuristic aimed at escaping local minima. Unlike simulated an- 
nealing, tabu search tries to keep the search biased toward good solutions. 
The basic idea of tabu search is that the best solution in the neighborhood 
N of the current solution should be chosen as the new current solution, even 
if this implies increasing the cost. If we are in a local minimum, this means 
accepting a non-improving perturbation. The problem with this basic idea is 
that the possibility of cycling arises. If we try to escape from a local minimum 
by choosing the best solution in its neighborhood, it might well be the case 
that at the next iteration, we fall back into the local minimum, since this 
could be the best solution in the new neighborhood. 
To prevent cycling, we must prevent revisiting solutions. One way would be 
to keep a record of the already visited solutions; however, this would be both 
memory- and time-consuming, since checking a candidate solution against the 
list of visited ones would require a substantial effort. A better idea could be 

596 
N ON- CON VEX OPTIMIZATION 
to record only the most recent solutions. A practical alternative is to keep in 
memory only some attributes of the solutions or of the applied perturbations; 
such attributes are called tabu. For instance, the reverse of the selected pertur- 
bation at each step can be marked as tabu, restricting the neighborhood to be 
considered. Consider a pure integer program involving only binary variables; 
if we complement variable xi, in the next few iteration we might forbid any 
perturbation complementing this variable again. As an alternative, a tabu 
attribute of a solution could be the value of the objective function. In prac- 
tice, it is necessary to keep only a record of the most recent tabu attributes to 
avoid cycling; the data structure implementing this function is the tabu list. 
The basic tabu navigation algorithm can be described as follows: 
Step 1. Choose an initial current solution xcur, a tabu list size; let 
k = 1, .f = f(xcur)l 2 = xcur. 
Step 2. Evaluate the neighborhood N(xcur); 
update the current so- 
lution with the best non-tabu solution in the neighborhood; if 
necessary, update the current optimal solution 2 and the current 
optimal value f. 
Step 3. Add some attribute of the new solution or of the applied 
perturbation to the tabu list. 
Step 4. If the maximum iteration number has been reached, stop; 
otherwise, set k = k + 1, and go to step 2. 
Note that, unlike simulated annealing, this version of tabu search explores 
the entire neighborhood of the current solution; basic tabu search is a strategy 
of the best-improving rather than first-improving type. However, it is possible 
to restrict the neighborhood to reduce the computational burden. 
There are several issues and refinements to consider in order to implement 
an effective and efficient algorithm. They are rather problem specific; this 
shows that, although local search metaheuristics are general-purpose, a certain 
degree of “customization’l is necessary. 
Genetic algorithms Unlike simulated annealing and tabu search, genetic al- 
gorithms work on a set of solutions rather than a single point. In this sense 
they are similar to the simplex search method of section 6.2.4. The idea is 
based on the survival-of-thefittest mechanism of biological evolution. Each 
solution is represented by a string of numbers or symbols; strings are subject 
to random evolution mechanisms which change the current population. One 
evolution mechanism is mutation; an attribute of a string is randomly se- 
lected and modified using a neighborhood structure. Mutation is very similar 
to the usual local search mechanism, but there is another mechanism which 
is peculiar to genetic algorithms: crossover. In the crossover mechanism, two 
elements of the current set of solutions are selected and merged in some way. 

FOR FURTHER READING 
597 
Given two strings, we select a “breakpoint” position k and merge the strings 
as follows: 
21, 
221 ’ . . I  Zk, Ykfl, . ., Yn 
YllY21~. 
.,Yk,Zk+lr * .  .,Zn 
21rZZi...iXkiZk+lr..rZn 
Y11 Yz,. . ., Yk, Yk+lr.. ., Yn 
Different variations are possible; for instance, a double crossover may be ex- 
ploited, in which two breakpoints are selected for the crossover. 
The set of solutions is updated at each iteration, selecting the “best” in- 
dividuals for mutation and crossover and/or letting only the best individuals 
survive. Rather than selecting the best individuals deterministically, based 
on the value of the objective function, random selection mechanisms are em- 
ployed to avoid freezing the population to a locally optimal solution. Genetic 
algorithms may be integrated with local search strategies; one idea is to use 
genetic mechanisms to find a set of initial points from which a local improve- 
ment search is carried out. 
The idea of genetic algorithms certainly has a good potential for solving 
quite complex problems; the evident downside is that considerable experimen- 
tation may be needed to come up with the best strategy and the best setting 
of numerical parameters regulating the evolution mechanisms. The potential 
of this class of methods is also proved by the recent introduction of the Ge- 
netic Algorithm and Direct Search toolbox, which extends the functionalities 
of the MATLAB Optimization toolbox. 
For further reading 
In the literature 
0 A comprehensive reference on mixed-integer programming is [16]. A 
more recent treatment, including developments in automatic model strength- 
ening, is [19]. 
0 The use of mixed-integer programming models in portfolio management 
is the subject of an increasing number of papers including [2], [3], [4], 
[lo], [ll], and [17]. 
0 For a textbook treatment, see also [18]. 
0 The AMPL language is described in [5]. 
0 Global optimization techniques for optimization of a fixed-mix portfolio 
are discussed in [12]; the model is extended and tackled by metaheuris- 
tics in [6]. 
0 For a broader view of the principles behind global optimization algo- 
rithms see, e.g., [8]. 

598 
NON-CONVEX OPTIMIZATION 
0 Tabu search is covered in depth by [7]. See, e.g., [l] for an application 
to global optimization. 
0 A textbook on genetic algorithms is [15]. An application to global opti- 
mization is described in [14]. 
On the Web 
0 The AMPL web site is http : //www . ampl. com. 
0 See also http : //www . ilog . corn. 
0 Meta-heuristics are the algorithmic foundation of an optimization en- 
gine, OptQuest, which thanks to its flexibility has been integrated with 
many simulation packages. See http: //www. optquest. corn. The tool 
has also been applied to portfolio management problems, too. 
0 The Genetic Algorithm and Direct Search toolbox is described on The 
Mathworks’ web site http: //www .mathworks. corn 
REFERENCES 
1. R. Battiti and G. Tecchiolli. The Continuous Reactive Tabu Search: 
Blending Combinatorial Optimization and Stochastic Search for Global 
Optimization. Annals of Operations Research, 63:153-188, 1996. 
2. D. Bertsimas, C. Darnell, and R. Stoucy. Portfolio Construction through 
Mixed-Integer Programming at Grantham, Mayo, Van Otterloo and Com- 
pany. Interfaces, 29:49-66, 1999. 
3. D. Bienstock. Computational Study of a Family of Mixed-Integer Quadratic 
Programming Problems. Mathematical Programming, 74:121-140, 1996. 
4. T.-J. Chang, N. Meade, J.E. Beasley, and Y.M. Sharaiha. Heuristics for 
Cardinality Constrained Portfolio Optimization. Computers and Opera- 
tions Research, 27:1271-1302, 2000. 
5. R. Fourer, D.M. Gay, and B.W. Kernighan. AMPL: A Modeling Language 
for Mathematical Programming. Boyd and F’raser, Danvers, MA, 1993. 
6. F. Glover, J.M. Mulvey, and K. Hoyland. Solving Dynamic Stochastic 
Control Problems in Finance Using Tabu Search with Variable Scaling. 
In I.H. Osman and J.P. Kelly, editors, Meta-Heuristics: Theory and Appli- 
cations, pages 429-448. Kluwer Academic, Dordrecht, The Netherlands, 
1996. 

REFERENCES 
599 
7. F.W. Glover and M. Laguna. Tabu Search. Kluwer Academic, Dordrecht, 
The Netherlands, 1998. 
8. R. Horst, P.M. Pardalos, and N.V. Thoai. Introduction to Global Opti- 
mization. Kluwer Academic, Dordrecht, The Netherlands, 1995. 
9. H. Konno and H. Yamazaki. Mean-Absolute Deviation Portfolio Opti- 
mization Model and Its Application to Tokyo Stock Market. Management 
Science, 37:519-53 1, 1991. 
10. M.S. Lobo, M. Fazel, and S. Boyd. Portfolio Optimization with Linear and 
Fixed Transaction Costs and Bounds on Risk. Unpublished manuscript 
(available at h t t p :  //www. stanford. edu/-boyd), 1999. 
11. R. Mansini and M.G. Speranza. Heuristic Algorithms for the Portfolio 
Selection Problem with Minimum Transaction Lots. European Journal of 
Operational Research, 114:219-233, 1999. 
12. C.D. Maranas, I.P. Androulakis, C.A. Floudas, A.J. Berger, and J.M. 
Mulvey. Solving Long-Term Financial Planning Problems via Global Op- 
timization. Journal of Economic Dynamics and Control, 21:1405-1425, 
1997. 
13. C.D. Maranas and C.A. Floudas. Global Minimum Potential Energy Con- 
formations of Small Molecules. Journal of Global Optimization, 4: 135-170, 
1994. 
14. Z. Michalewicz. Evolutionary Computation Techniques for Nonlinear Pro- 
gramming Problems. International Transactions of Operations Research, 
1:223-140, 1994. 
15. Z. Michalewicz. Genetic Algorithms + Data Structures = Evolution Pro- 
grams. Springer-Verlag, Berlin, 1996. 
16. G.L. Nemhauser and L.A. Wolsey. Integer Programming and Combinato- 
rial Optimization. Wiley, Chichester, West Sussex, England, 1998. 
17. J.K. Sankaran and A.A. Patil. On the Optimal Selection of Portfolios 
under Limited Diversification. Journal of Banking and Finance, 23: 1655- 
1666, 1999. 
18. B. Scherer and D. Martin. Introduction to Modern Portfolio Optimization 
with NuOPT, S-Plus, and PBayes. Springer, New York, 2005. 
19. L.A. Wolsey. Integer Programming. Wiley, New York, 1998. 

This Page Intentionally Left Blank


## Stochastic Programming

Part V 
A p p e n d i ce s 


Appendix A 
Introduction to 
MATLAB Programming 
We give here a brief outline of the MATLAB basics, referring to the user 
manual for a full treatment. You may also type demo to see a demonstration 
of both MATLAB and the toolboxes you are interested in. Actual use of the 
features we describe is illustrated in the remainder of the book. A rich online 
documentation is available in the MATLAB environment; the reader should 
take advantage of this whenever a piece of code in the book is not clear. 
A.l 
MATLAB ENVIRONMENT 
0 MATLAB is an interactive computing environment. You may enter 
expressions and obtain an immediate evaluation: 
>> rho = l+sqrt(5)/2 
rho = 
2.1180 
By entering a command like this, you also define a variable rho which is 
added to the current environment and may be referred to in any other 
expression. 
603 

604 
INTRODUCTION TO MATLAB PROGRAMMING 
There is a rich set of predefined functions. Try typing help elf un, help 
elmat, and help ops to get information on elementary mathematical 
functions, matrix manipulation, and operators, respectively. For each 
predefined function there is an online help: 
>> help sqrt 
SQRT 
Square root. 
SQRT(X) is the square root of the elements of X. Complex 
results are produced if X is not positive. 
See also sqrtm, realsqrt, hypot. 
Reference page in Help browser 
doc sqrt 
The help command should be used when you know the name of the 
function you are interested in, but you need additional information. 
Otherwise, lookf o r  may be tried: 
>> lookfor sqrt 
REALSQRT Real square root. 
SQRT 
Square root. 
SQRTM 
Matrix square root. 
We see that lookf o r  searches for functions whose online help documen- 
tation includes a given string. Recent MATLAB releases include an 
extensive online documentation which can be accessed by the command 
doc. 
0 MATLAB is case sensitive (Pi and p i  are different). 
>> pi 
ans = 
3.1416 
>> Pi 
??? Undefined function or variable 'Pi'. 
MATLAB is a matrix-oriented environment and programming language. 
Vectors and matrices are the basic data structures, and more complex 
ones have been introduced in the more recent MATLAB versions. Func- 
tions and operators are available to deal with vectors and matrices di- 
rectly. You may enter row and column vectors as follows: 
>> V1=[22, 5, 31 
v1 = 
22 
5
3
 

MATLAB ENVIRONMENT 
605 
>> v2 = c33; 7; 11 
v2 = 
33 
7 
1 
We may note the difference between comma and semicolon; the latter is 
used to terminate a row. In the example above, commas are optional, 
as we could enter the same vector by typing V1= 122 5 31. 
0 The who and whos commands may be used to check the user defined 
variables in the current environment, which can be cleared by the clear 
command. 
>> who 
Your variables are: 
v1 
v2 
>> whos 
Name 
Size 
Bytes Class 
v1 
1x3 
24 double array 
v2 
3x 1 
24 double array 
Grand total is 6 elements using 48 bytes 
>> clear V1 
>> whos 
Name 
Size 
Bytes Class 
v2 
3x 1 
24 double array 
Grand total is 3 elements using 24 bytes 
>> clear 
>> whos 
>> 
0 You may also use the semicolon to suppress output from the evaluation 
of an expression: 
>> V1=[22, 5, 31 ; 
>> v2 = [33; 7; 11; 
>> 
Using semicolon to suppress output is important when we deal with 
large matrices (and in MATLAB programming as well). 
0 You may also enter matrices (note again the difference between ‘;’ and 
L, ’): 
>> A = [ l  2 3; 4 5 61 
A =  

606 
lNTRODUCTlON TO MATLAB PROGRAMMING 
1 
2 
3 
4 
5 
6 
>> B=[V2 , V21 
B =  
33 
33 
7 
7 
1 
1 
>> C=[V2 ; v21 
C =  
33 
7 
1 
33 
7 
Also note the effect of the following commands: 
>> Ml=zeros(2,2) 
M1 = 
0 
0 
0 
0 
>> Ml=rho 
M1 = 
2.1180 
>> Ml=zeros(2,2) ; 
>> Ml(:,:)=rho 
M1 = 
2.1180 
2.1180 
2.1180 
2.1180 
0 The colon ( : ) is used to spot subranges of an index in a matrix. 
>> Ml=zeros(2,3) 
M 1  = 
0 
0 
0 
0 
0 
0 
>> M1(2,:)=4 
M1 = 
0 
0 
0 
4
4
 4 
>> M1(1,2:3)=6 
M 1  = 
0 
6 
6 
4 
4 
4 
0 The dots (. . .) may be used to write multiline commands. 

MATLAB ENVIRONMENT 
607 
>> M=ones(2, 
??? M=ones (2, 
Missing variable or function. 
>> M=ones(2, . . .  
2) 
M =  
1 
1 
1 
1 
0 The zeros and ones commands are useful to initialize and preallocate 
matrices. This is recommended for efficiency. In fact, matrices are 
resized automatically by MATLAB whenever you assign a value to an 
element beyond the current row or column range, but this may be time 
consuming and should be avoided when possible. 
>> M = [l 2; 3 41; 
>> M(3,3) = 5 
M =  
1 
2 
0 
3 
4 
0 
0 
0 
5 
It should be noted that this flexible management of memory is a double- 
edged sword: It may increase flexibility, but it may make debugging 
difficult. 
0 [I is the empty vector. You may also use it to delete submatrices: 
M1 = 
0 
6 
6 
4 
4 
4 
>> M1(: ,2)=[1 
M1 = 
0 
6 
4 
4 
0 Another use of the empty vector is to pass default values to MATLAB 
functions. Unlike other programming languages, MATLAB is rather 
flexible in its processing of input arguments to functions. Suppose we 
have a function f taking three input parameters. The standard call 
would be something like f (XI, x2, x3). If we call the function with 
one input arguments, f (xi), the missing ones are given default values. 
Of course this does not happen automatically; the function must be 

608 
INTRODUCTION TO MATLAB PROGRAMMING 
programmed that way, and the reader is urged to see how this is accom- 
plished by opening predefined MATLAB functions with the editor. 
Now suppose that we want to pass only the first and the third argument. 
We obviously cannot simply call the function like f (XI, x31, since x3 
would be assigned to the second input argument of the function. To 
obtain what we want, we should use the empty vector: f (xi, [I , x3). 
0 Matrices can be transposed and multiplied easily (if dimensions fit): 
>> M1’ 
ans = 
0
4
 
6 
4 
>> M2=rand(2,3) 
M2 = 
0.9501 
0.6068 
0.8913 
0.2311 
0.4860 
0.7621 
>> M1*M2 
ans = 
1.3868 
2.9159 
4.5726 
4.7251 
4.3713 
6.6136 
>> M1+1 
ans = 
1 
7 
5 
5 
The rand command yields a matrix with random entries, uniformly 
distributed in the (0,l) interval. 
0 Note the use of the dot . to operate element by element on a matrix: 
>> A=O .5*ones (2,2) 
A =  
0.5000 
0.5000 
0.5000 
0.5000 
>> M 1  
M1 = 
0 
6 
4 
4 
>> Ml*A 
ans = 
3 
3 
4
4
 
>> Ml.*A 
ans = 
0 
3 
2 
2 

MATLAB EN VlRON M EN T 
609 
>> I=[l 2; 3 41 
I =  
1 
2 
3 
4 
>> 1-2 
ans = 
7 
10 
15 
22 
>> 1.-2 
ans = 
1 
4 
9 
16 
Subranges may be used to build vectors. For instance, to compute the 
factorial: 
>> 1:lO 
ans = 
1 
2 
3 
4 
5 
6 
7 
a 
9 
10 
>> prod(1: 10) 
ans = 
3628800 
>> sUm(1:lO) 
ans = 
55 
You may also specify an optional increment step in these expressions: 
>> 1:0.8:4 
ans = 
i . 0000 
1. aooo 
2.6000 
3.4000 
The step can be negative too: 
>> 5:-1:0 
ans = 
5 
4 
3 
2 
1 
0 
0 One more use of the colon operator is to make sure that a vector is a 
column vector: 
>> V1 = 1:3 
v1 = 
>> V2 = (1:3IJ 
v2 = 
1 
2 
3 
1 
2 

610 
INTRODUCTION TO MATLAB PROGRAMMING 
1 
2 
3 
>> V2(:) 
ans = 
1 
2 
3 
The same effect cannot be obtained by transposition, unless one writes 
code using the function size to check matrix dimensions: 
>> [m,n] = size(V2) 
m =  
3 
n =  
1 
0 Note the use of the special quantities Inf (infinity) and NaN (not a 
number): 
>> 1=1/0 
Warning: Divide by zero. 
1 =  
>> 1 
1 =  
>> prod(l:200) 
Inf 
Inf 
ans = 
Inf 
>> 1/0 - prod(l:200) 
Warning: Divide by zero. 
ans = 
NaN 
0 Useful functions to operate on matrices are: eye, inv, eig, det, rank, 
and diag: 
>> eye(3) 
ans = 
1 
0 
0 
0 
1 
0 
0 
0 
1 

MATLAB ENVIRONMENT 
611 
>> K=eye(3)*[1 2 31 ’ 
K =  
1 
3 
>> K=inv(K) 
K =  
1.0000 
0 
0 
0 
0.5000 
0 
0 
0 
0.3333 
>> eig(K) 
ans = 
1.0000 
0.5000 
0.3333 
>> rank(K) 
3 
ans = 
>> det(K) 
ans = 
0.1667 
>> K=diag([l 2 31) 
K =  
1 
0 
0 
0 
2 
0 
0 
0 
3 
We should note a sort of dual nature in diag. If it receives a vector, it 
builds a matrix; if it receives a matrix, it returns a vector: 
>> A = [1:3 ; 4:6 ; 7:91; 
>> diag(A) 
1 
5 
9 
ans = 
Some functions operate on matrices columnwise: 
> > A = C 1 3 5 ; 2 4 6 ] ;  
>> sum(A) 
ans = 
>> maan(A) 
3 
7 
11 
ans = 
1.5000 
3.5000 
5.5000 
The last example may help to understand the rationale behind this 
choice. If the matrix contains samples from multiple random variables, 

612 
lNTRODUCTlON TO MATLAB PROGRAMMING 
and we want to compute the sample mean, we should arrange data in 
such a way that variables corresponds to columns, and joint realizations 
corresponds to rows. However, it is possible to specify the dimension 
along which these functions should work: 
>> sum(A,2) 
9 
12 
>> mean(A,2) 
3 
4 
ans = 
ans = 
Another useful function in this vein computes cumulative sums: 
>> cumsum(l:5) 
ans = 
1 
3 
6 
10 
15 
Systems of linear equations are easily solved: 
>> A = [3 5 -1; 9 2 4; 
4 -2 -91; 
>> b = (1:3)’; 
>> X = A\b 
X =  
0.3119 
-0.0249 
-0.1892 
>> A*X 
ans = 
1.0000 
2.0000 
3.0000 
The efficiency of a function may be checked by using the commands t i c  
and toc as follows: 
>> tic, inv(rand(500,500)) ;, toc 
Elapsedtime is 0.472760 seconds. 
We will see in section A.3 how MATLAB code can be developed in 
order to compute complicated functions. However, when the function 
is a relatively simple expression it may be preferable to define functions 
in a more direct way. One possibility is using the inline mechanism, 
which builds a function based on a string: 

MATLAB ENVIRONMENT 
613 
>> f = inline(’exp(2*x) .*sin(y) ’1 
f =  
Inline function: 
f (x,y) = exp(2*x) .*sin(y) 
>> f(2,3) 
ans = 
7.7049 
Note the use of the dot operator to make sure the function works on 
vector inputs and how inline determines automatically the name and 
the order of the input arguments. If one wants to change that order, an 
explicit list of arguments can be given: 
>> f = inline(’exp(2*foo).*sin(fee)’) 
f =  
Inline function: 
f (fee,foo) = exp(2*foo) .*sin(fee) 
>> g = inline( ’exp(2*foo). *sin(fee) ’ , ’foo ’ , ’fee ’1 
g =  
Inline function: 
g(foo,fee) = exp(2*foo) .*sin(fee) 
0 An alternative approach to inline is based on the function handle op- 
erator @: 
We see that the operator is used to LLabstractll 
a function from an ex- 
pression.’ The @ operator is also useful to define anonymous functions 
which may be passed to higher-order functions, i.e., functions which re- 
ceive functions as inputs (e.g., to compute integrals or to solve non-linear 
equations). 
We may also fix some input parameters to obtain function of the re- 
maining arguments: 
‘Readers, like myself, with a little background in theoretical computer science or mathe- 
matical logic will notice some similarity with the notation used in A-calculus. 

614 
INTRODUCTION TO MATLAB PROGRAMMING 
7.7049 
0 In this book we will practically use only matrices, but MATLAB has 
included many more data structures over the years. We can deal with 
strings (delimited by quotes) and structures (called (‘struct”’ ) with ar- 
bitrary fields: 
>> p.name = ’Donald Duck’ 
>> p.age = 55; 
>> P 
P =  
name: ’Donald Duck’ 
age: 55 
Structures are used by some functions to group output data in one 
structure, avoiding an excessive number of output arguments. 
0 Cell arrays may also be used to implements ragged arrays, i.e., arrays 
containing vectors with different lengths (which cannot be accomplished 
by traditional matrices): 
>> M = ce11(2,1); 
>> MC1) = 
1 2 3 1 ;  
>> M(2) 
= C 4 5 6 7 8 1 ;  
>> M 
M =  
[1x3 double] 
[1x5 double] 
>> MC1) 
ans = 
1 
2
3
 
Note the use of braces rather than standard parentheses. 
A.2 
MATLAB GRAPHICS 
0 Plotting a function of a single variable is easy. Try the following com- 
mands: 
>> x = O:O.O1:2*pi; 
>> plot(x,sin(x)) 
>> axis( CO 2*pi -1 11 ) 
The axis command may be used to resize plot axes at will. There is 
also a rich set of ways to annotate a plot. 

MATLAB GRAPHICS 
615 
0 Different types of plots may be obtained by using optional parameters 
of the p l o t  command. Try with 
0 To obtain a tridimensional surface, the surf command may be used. 
>> f = a(x,y) exp(-3*(x.-2 + y.*2)).*(sin(5*pi*x)+ 
cos(lO*pi*y)); 
>> [X Y1 = meshgrid(-l:O.Ol:l , -1:O.Ol:l); 
>> surf (X,Y,f (X,Y)) 
Some explanation is in order here. The function surf must receive three 
matrices, corresponding to the x and y coordinates in the plane, and to 
the function value (the ‘z’ coordinate). A first requirement is that the 
function we want to draw should be encoded in such a way that it can 
receive matrix inputs; use of the dot operator is essential: Without the 
dots ‘ . I, input matrices would be multiplied row by column, as in linear 
algebra, rather than element by element. To build the two matrices 
of coordinates, meshgrid is used. To understand what this function 
accomplishes, let us consider a small scale example: 
>> [X,Y] = meshgrid(l:4,1:4) 
X =  
1 
2 
3 
4 
1 
2 
3 
4 
1 
2 
3 
4 
1 
2 
3 
4 
1 
1 
1 
1 
2 
2 
2 
2 
3 
3
3
 3 
4 
4 
4 
4 
Y =  
We see that, for each point in the plane, we obtain matrices containing 
each coordinate. 
0 We may close this section with a more practical example: plotting the 
Black-Scholes price of a vanilla call option, for time to maturity T rang- 
ing from one year down to zero, initial price SO ranging from 30 to 70, 
strike price K = 50, risk-free rate r = 0.1, and volatility o = 0.4. The 
following commands produce the surface in figure A.l: 
>> T = 1:-0.05:O; 
>> SO = 30:70; 
>> K = 50; 

616 
INTRODUCTION T O  MATLAB PROGRAMMING 
fig. A.l 
asset price. 
Price of a call option as a function of time to maturity and initial underlying 
>> sigma = 0.4; 
>> r = 0.1; 
>> [X,Y] = meshgrid(T,SO); 
>> f = Q(time,price) blsprice(price, 50, 0.1, time, 0.4); 
>> surf (X,Y,f (X,Y)> 
Of course we are relying on the fact that the blsprice function, available 
in the Financial toolbox, has been properly coded to handle matrix 
inputs. 
A.3 
MATLAB PROGRAMMING 
a MATLAB toolboxes extend considerably the capabilities of the MAT- 
LAB core. They consist of a set of functions that are coded in the 
MATLAB programming language. They are contained in M-files, which 
are plain text files with default extension * .m. It is quite instructive to 
open some of these files in the MATLAB editor to see how a robust and 
flexible code is written. 
You may also write your own functions. You have simply to open the 
MATLAB editor and save the file in a directory which is on the MAT- 
LAB path. 
0 A simple function is displayed in figure A.2. The function consists of the 
function header, which specifies the input and output arguments. Note 

MATLAB PROGRAMMING 
61 7 
function Cxout, youtl = samplefile(x,y) 
x a simple M-file to do some pointless computation 
1 this comment is printed by issuing the help samplefile 
X command 
[m,nl = size(x); 
[p,ql = size(y); 
z = rand(lO,m)*x*rand(n,lO) 
+ rand(lO,p)*y*rand(q,lO); 
xout = sum(z); 
yout = sin(z); 
Fig. A.2 Typical structure of a MATLAB function. 
how multiple output arguments are expressed. The comments below 
the function heading are displayed if you ask for some help about the 
function: 
>> help samplefile 
a simple M-file t o  do some pointless computation 
this comment is printed by issuing the help samplefile 
command 
Then the function body is given, which may contain further comment 
lines and arbitrarily complex control structures. 
0 In general, you may write a function in which some input arguments are 
optional and are given default parameters. To see a simple example, try 
typing the following commands: 
>> help mean 
and 
>> type mean.m 
Alternatively, you may open mean.m within the MATLAB editor. 
0 The function body includes a sequence of instructions, which in turn are 
built by: 
- Using control structures common to any other programming lan- 
guage, such as if, for, while, etc. 
- Calling other predefined functions. 

618 
lNTRODUCTlON T O  MATLAB PROGRAMMING 
function p = myprimes(N1 
found = 0; 
trynumber = 2; 
while (found < N) 
p = [I; 
if isprime(trynumber) 
p = [p , trynumber]; 
found = found + 1; 
end 
trynumber = trynumber + 1; 
end 
Fig. A.3 MATLAB function to return the first N prime numbers. 
- Building expressions based on the familiar arithmetic, relational, 
and logical operators. 
For instance, suppose you want to write a function that returns the 
first N prime numbers. MATLAB provides the user with two related 
functions, primes and isprime. The function primes returns the prime 
numbers that are less than or equal to an input number: 
>> primes(l1) 
ans = 
2 
3 
5 
7 
11 
whereas isprime returns 1 if the input number is prime, 0 otherwise: 
>> isprime(C3 4 51) 
ans = 
1 
0 
1 
Unfortunately, primes is not what we need, since we want the first N 
prime numbers. One way to accomplish our aim is illustrated in figure 
A.3. Note how the if statement treats 1 as “true” and 0 as “false.” 
>> myprimes ( 8 )  
ans = 
2 
3 
5 
7 
11 
13 
17 
19 
The function can and should be improved. To begin with, even numbers 
larger than 2 cannot be prime and should not be checked; furthermore, 

MATLAB PROGRAMMING 
619 
the vector p should be preallocated, rather than dynamically resized. 
These improvements are left as an exercise. 
0 A typical way to improve performance of MATLAB code is vectorization. 
This means that one should try to avoid for loops working on elements 
of vectors and matrices, which should be acted on as a whole block. As 
an example, we may write different functions to build a Hilbert matrix. 
This matrix is introduced in example 1.3 on page 18, and its elements 
are 
In figure A.4 we illustrate different functions to build a Hilbert matrix 
of order N :  MyHilbDumb is based on two nested loops, without matrix 
preallocation; MyHilb is the same, but it preallocates the output matrix; 
MyHilbV is partially vectorized, as rows are built and assigned as vectors. 
Let us compare the performance of the three functions: 
>> tic, 
Elapsed 
>> tic, 
Elapsed 
>> tic, 
Elapsed 
>> tic, 
Elapsed 
>> tic, 
Elapsed 
MyHilbDumb(1000) ; , toc 
time is 10.565729 seconds. 
MyHilb(1000) ; , toc 
time is 0.053242 seconds. 
MyHilbV(1000);, toc 
time is 0.063986 seconds. 
MyHilb(5000) ; , toc 
time is 1.245170 seconds. 
MyHilbV(5000) ; , toc 
time is 1.202888 seconds. 
We see how fundamental preallocation is. Vectorization does not seem 
an impressive technique here (the reader is urged to check the perfor- 
mance of the built-in function hilb, which is fully vectorized). In older 
MATLAB versions vectorized code typically worked much better that 
non-vectorized code; improvements in the MATLAB interpreter have 
made this practice less important in some cases, but not always. 
The following example shows that when the overhead of a function call 
is involved, vectorization may be useful: 
>> prices = 30:0.1:70; 
>> N = length(prices1; 
>> calls = zeros(N,l); 
>> tic, calls = blsprice(prices,50,0.1,1,0.4);, toc 
Elapsed time is 0.012505 seconds. 
>> tic, ... 
f o r  i=l:N, calls(i)=blsprice(prices(i) ,50,0.1,1,0.4);, 
end, toc 
Elapsed time is 0.397540 seconds. 

620 
lNTRODUCT/ON TO MATLAB PROGRAMMING 
function H = MyHilbDumb(N1 
for i=l:N 
for j=l:N 
end 
H(i,j) = l/(i+j-l); 
end 
function H = MyHilb(N) 
H = zeros(N,N); 
for i=l:N 
for j=l:N 
end 
H(i,j) = l/(i+j-l); 
end 
function H = MyHilbV(N1 
H = zeros(N,N) ; 
for i=l:N 
end 
H(i,:) = l./(i:(i+N-l)); 
Fig. A.4 Three ways to build a Hilbert matrix. 

MATLAB PROGRAMMING 
621 
0 Useful operators to vectorize code are any and find: 
>> v = [ 1 3 -4 9 -2 11 
V =  
1 
3 
-4 
9 
-2 
1 
>> any(V > 9) 
>> any(V >= 7) 
ans = 
0 
ans = 
1 
>> Sum(V<O) 
2 
ans = 
>> find(V < 0 )  
ans = 
3 
5 
>> V(find(V<O))=[I 
V =  
1 
3 
9 
1 
0 When developing M-files, a most useful tool is the interactive debugger. 
We refer the reader to the manual for details. 

This Page Intentionally Left Blank

Appendix B 
Refresher on Probability 
Theory and Statistics 
In this appendix we recall very briefly some basic facts about probability 
theory and parameter estimation. This is not meant as a substitute for a 
thorough treatment, for which we refer the reader to the references. We will 
not use measure theoretic concepts and will mostly rely on intuition. We 
also give information on some functions provided by the MATLAB Statistics 
toolbox. 
6.1 SAMPLE SPACE, EVENTS, AND PROBABILITY 
Probability is defined based on random events that take place within a sample 
space. A sample space S contains the possible outcomes of a random exper- 
iment or a sequence of random experiments. An event E is a subset of the 
sample space S. Which subsets are events may depend on the application, 
what we are interested in, and the available information on random outcomes. 
The empty set 0 is a particular event. For any event El we may consider its 
complement EC; since the sample space S contains all the possible outcomes, 
we have S" = 0. Given any two events El and E2, we may consider their 
623 

624 
REFRESHER ON PROBABILITY THEORY AND STATISTICS 
union El U E2 and their intersection El n E2; to ease notation, we will de- 
note intersection by E1E2. If the intersection of two events is empty, i.e., if 
ElE2 = 0, we say that the two events are mutually exclusive. More generally, 
we may consider the union and the intersection of an arbitrary number of 
events. 
For each event E on a sample space S, we define a probability measure 
P(E) which must satisfy the following three conditions: 
1. 
2. 
3. 
0 5 P ( E )  5 1. 
P(S) = 1. 
For any sequence of mutually exclusive events El, E2, E3,. . . (i.e., such 
that EiEj = 0, for i # j ) ,  we have 
Different properties may be proven as a consequence of these conditions. For 
instance, it can be shown that 
P(E) + P(E") = 1 
and that 
P(E1 U Ez) = P(E1) + P(E2) - P(EiE2). 
Often we are interested in the probability of an event E conditional on the 
occurrence of another event F ,  denoted by P ( E  I F). It is natural to define 
the conditional probability as1 
This follows from the observation that if we know that the event F has oc- 
curred, the new sample space is F ,  so that probabilities must be adjusted 
accordingly. Finally, we say that two events are independent if 
P(EF) = P(E)P(F), 
which in turn implies that 
P ( E  1 F )  = P(E). 
So, for independent events, knowing that F has occurred tells us nothing 
about the probability of the occurrence of E. Note that mutually exclusive 
events are not independent; if we know that one has occurred, we know that 
the other cannot. 
'This definition is not completely satisfactory: It does not work with events with zero 
probability. Conditioning is treated at a higher level in advanced probability texts, but we 
do not really need that machinery for this introductory textbook. Hence we will stick to 
this intuitive definition. 

RANDOM VARIABLES, EXPECTATION. AND VARIANCE 
625 
B.2 
RANDOM VARIABLES, EXPECTATION, AND VARIANCE 
When we associate numerical values of one or more variables to events, we 
obtain random variables. Random variables may be thought of as mappings 
from events to real or integer numbers. Usually, a random variable is denoted 
by a capital letter such as X ;  the value assumed by a random variable on a 
particular realization of the events is denoted by a lowercase letter such as x. 
A different notation is common in economics, and it may be preferable when 
dealing with the Greek alphabet: For instance, we may use C for a random 
variable, and 6 for its realizations. When X takes values on a finite or count- 
able domain, such as non-negative integer numbers, we speak of a discrete 
random variable. For a discrete random variable, we define the probability 
mass function p ( . )  for each possible outcome value x i :  
p(x2) = P { X  = xi}. 
00 
We have 
i=l 
We also define the (cumulative) distribution function F(.): 
F(a) = P { X  5 a }  = c 
p(zz), 
.;<a 
It is easy to see that the distribution function for a discrete random variable 
is a piecewise constant, nondecreasing function. 
Example B.l A typical example of discrete probability distribution is the 
Poisson random variable, with parameter A. In this case the random variable 
X takes values in the set {0,1,2,3,. . .}, and its probability mass function is 
We may check that this is indeed a probability mass function: 
U. 
i=O 
i=O 
In practice, one usually works with a parameter At, where X is the rate at 
which certain events occurs over time and t is the length of the time interval 
we observe. For instance, this could model the number of shocks we observe 
over a time interval on the price of a stock or the credit rating of a bond 
issuer. 
0 
If the random variable may take values over a continuous set, such as a 
bounded interval on the real line, say (a, b), or the entire line (-a, 
fm), we 

626 
REFRESHER ON PROBABILITY THEORY AND STATISTICS 
have a continuous random variable. In this case, we cannot define a probability 
mass function; since the outcome values are infinite and uncountable, the 
probability that X takes a specific value will be zero.' 
We must define a 
non-negative probability density function f(x) for z E (--00, 
+m) such 
that for a given subset B of real numbers, 
P { X  E B }  = 
f (x)  dx. 
J, 
+W 
s_,f (XI dx = 1. 
P { X  E (5, x + AX)} 
= I 
f (Y) = fb) 
A x ,  
To understand what the probability density means, consider the following: 
x+Ax 
for a small Ax. So we see that density cannot be interpreted as a probability, 
but it does give a measure of how likely given values of the random variable are 
and is needed to define probability of sets. We may also define the distribution 
function: 
F(a) = P{X 5 a} = 
from which we obtain3 
-- 
dF(x) - f ( x ) .  
dx 
Given a random variable, we may compute its expected value using the 
probability mass function or the density function. In the discrete case we 
have 
i 
and, for the continuous case, 
+W 
E[X] = 1, xf(x) dx. 
An important property of the expectation operator is 
E[aX + b] = aE[X] + b. 
'We are not considering mixed probabilitydistributions, which are a hybrid between discrete 
and continuous distributions. 
3The distribution function is not everywhere differentiablein the case of mixed distributions, 
which we do not consider. 

RANDOM VARIABLES, EXPECTATION, AND VARIANCE 
627 
Example B.2 Let us compute the expected value of a Poisson random vari- 
able. Applying the definition yields 
00 
Xi-' 
O0 
Aa 
E[X] = 
ie-' 7 
= Ae-' - 
a. 
( a  - l)! 
i=O 
i=l 
This may be interpreted as follows. If events occur at a rate of A events per 
time unit, the expected number of events over a unit interval is actually the 
rate A. By the same token, the expected number of events occurring over an 
interval of length t is At. 
0 
The expected value of a random variable gives a measure of location of the 
entire distribution, but it does not tell anything about its dispersion. The 
typical measure of dispersion is variance: 
Var(X) = E[(X - E[X])2] 
The variance of a random variable X is often denoted by r&. 
Unfortunately, 
variance has not the same unit of measure of the random variable itself; hence, 
the square root of variance, O X ,  called standard deviation, is often used. 
A couple of properties of the variance are the following: 
Var(X) = E[X2] - E2[X] 
Var(uX + b) = u2 Var(X). 
We see immediately that, unlike the expectation, the variance operator is not 
linear. Indeed, it is not true in general that the variance of a sum of random 
variables is the sum of their variances (see later). 
Example B.3 Consider a random variable X such that 
E[X] = p 
and 
Var(X) = 02. 
If we define another random variable 
cl 
it is easy to see that the properties above imply 
E[Z] = 0 
and 
Var(2) = 1. 
0 

628 
REFRESHER ON PROBABILITY THEORY AND STATISTICS 
It is also natural to define the expected value of a function g(X) of a random 
variable: 
g(xi)p(xi) 
for the discrete case 
E[g(X)I = { j.6. 
g(x)f(x) dx 
It is important to note that, in general, 
for the continuous case. 
If the function g is convex, then the following Jensen’s inequality holds: 
Another fundamental concept linked to probability distributions is the quan- 
tile. In the continuous case, the quantile qp is linked to a probability level ,f3 
as follows: 
P{X 5 Qp} = P. 
We see that the quantile is the solution of the equation 
If there are multiple solutions to this equation, we take the smallest one as 
the quantile. This does not happen in common probability distributions, as 
the distribution function is strictly monotonically increasing over the support 
of the distribution. In the discrete case, the cumulative distribution ‘?jumps” 
and we may fail to find a solution to this equation. In this case we adapt the 
definition as follows: The quantile is the smallest number qp such that 
8.2.1 
Common continuous random variables 
Uniform random variable A random variable is distributed uniformly over the 
interval (a, b) if its density function is 
A typical case is the uniform distribution 
see that 
E[X] = lb & 
dx = 
if x E (a, b) 
otherwise. 
over the interval (0,l). It is easy to 
b2-a2 
b f a  
2 ( b -  a) 
2 
- 

RANDOM VA RlABL €5, EXPECTATION, AND VARIANCE 
629 
and 
2 
x2 
u f b  
Var(X) = E[X2] - E2[X] = / - 
dx - (I> 
a b - a  
- b3 - u3 
( b f  
- ( b -  u ) ~  
- 
3(b - U) 
4 
12 
Exponential random variable 
sume non-negative values, and its density is given by 
The exponential random variable may only as- 
i f x > O  
if x < 0, 
f(x) = { O”e+ 
for some parameter A > 0. The distribution function is 
F(a) = lo 
Ae-Xz dx = 1 - e-xa. 
The expected value is 
1 
and the variance is 1/A2. It is interesting to note that if the time elapsing 
between events is exponentially distributed with parameter A, the events occur 
at a rate A, and the distribution of the number of events over a time interval 
of length t is a Poisson random variable with parameter At. 
Normal random variable The normal random variable has an infinite support, 
i.e., it may take values over the whole real line, and its density function is the 
bell-shaped function: 
for given parameters p and u2. The distribution function for the normal 
distribution is not known in closed form, but it can be computed by numerical 
approximations (see section 3.3.1). With some calculations it can be shown 
that the parameters p and u have indeed a precise meaning: 
E[X] = p, 
Var[X] = u2. 
We use the notation X N N(p,u2) to say that X has normal distribution 
with given expected value and variance. A variable 2 N N(0,l) is called a 
unit or standard normal variable. 
Example B.4 The parameter p influences where the maximum of the den- 
sity is located, whereas the variance u2, or the standard deviation u, tells how 

630 
REFRESHER ON PROBABILITY THEORY AND STATISTICS 
0.4 
' 
' 
. 
0.35 . 
0.3 . 
0.25 . 
0.15. 
-10 -8 -6 -4 -2 
0 2 
4 
6 
8 10 
Fig. B.l Normal density functions for p = 0 and u = 1 or u = 3. 
stretched the function is. We may plot the density functions for two normal 
distributions with p = 0 and u = 1 or u = 3. 
>> x=-10:0.1:10; 
>> plot(x, normpdf(x,O,l)) 
>> hold on 
>> plot(x, normpdf (x,0,3)) 
The result is plotted in figure B.l. The Statistics toolbox includes functions to 
compute the probability functions for all of the main probability distributions. 
0 
An important property of the normal distribution is that if X is normally 
distributed with parameters p and u2, then ax + p is normally distributed 
with parameters ap +P and a2u2. 
In particular, Z = (X - p)/u is a standard 
normal. 
The importance of the standard normal distribution is apparent if we think 
of computing the distribution function or the quantiles for a generic normal 
variable. By working with standard normal variables, we are actually able to 
deal with the more general case. For instance, to compute the distribution 
function for an arbitrary normal variable, it is sufficient to come up with an 
approximation for the standard case: 
J x  
e-22/2dz. 
N ( z )  = - 
1 6 
--oo 
Let zp be the P-quantile for the standard normal: 
P{Z 5 zp} = N ( z p )  = p. 
Knowing zg, it is easy to find the P-quantile for a normal variable X N 
N(p, u2): 
P = P { X 5 4 p )  

RANDOM VA RlABL €5, EXPECTATION, AND VARIANCE 
631 
from which we get 
qp = p + zpu. 
In statistics, we are typically interested in quantiles of the form ~ 1 - ~ ,  
where 
a is a relatively small number, such as 0.01 or 0.05. Quantiles and values of 
N ( z )  are tabulated or computed using suitable approximations. 
Example B.5 The function normcdf (x, sigma,mu) yields the distribution 
function. To compute the probability that a standard normal variable lies in 
the interval (-2,2): 
>> p = normcdf ([-2 21) ; 
>> p(2) - p(1) 
ans = 
0.9545 
Similarly: 
>> p = normcdf (C-3 31 1 ; 
>> p(2)-p(l) 
ans = 
0.9973 
from which we see that for a normal distribution, the probability of falling 
outside the interval ( p  - 3c7, p + 30) is quite small. In fact, the normal dis- 
tribution is a debatable model for asset returns, as in practice these exhibit 
fat tails, i.e., the occurrence of extreme values is more likely than it should 
be with the normal distribution. 
You may also invert the distribution function. Compare x and xnew in the 
following: 
>> x=r-3:0.2:0.31; 
>> xnew=norminv(normcdf(x,O, 1) ,o, 1) ; 
0 
The importance of normal variables, apart from their many properties, 
stems from the central limit theorem. Roughly speaking, it states that if 
we sum many identically distributed and independent random variables, their 
sum tends to have a normal distribution as the number of summed random 
variables goes to infinity. 
Lognormal random variable Due to the central limit theorem, a normal ran- 
dom variable may be thought of as the limit of a sum of random variables. 
The lognormal variable may be thought of as the limit of a product of ran- 
dom variables. Formally, we say that a random variable Z is lognormally 

632 
REFRESHER ON PROBABILITY THEORY AND STATISTICS 
distributed if log2 is normally distributed; put another way, if X is normal, 
then ex is lognormal. 
The following formulas illustrate the relationships between the parameters 
of a normal and a lognormal distribution. If X N N(p, 2) and Z = ex, then 
E[Z] = ep+02/2 
var(2) = e2p+u(eaZ - 1). 
In particular, we see that 
Since the exponential is a convex function, this is a consequence of Jensen’s 
inequality. 
8.3 
JOINTLY DISTRIBUTED RANDOM VARIABLES 
When considering jointly distributed random variables, we may follow the 
same route as in the scalar case. We illustrate in the bidimensional case, as 
the generalization is straightforward. Given two random variables X and Y ,  
we may define the joint distribution function: 
In the discrete case we also consider the probability mass function: 
whereas continuous variables are characterized by a density f (2, y) such that, 
for a region D in the plane, 
From the joint distribution we may derive the marginal distributions for the 
single variables. For instance 
P { X  E A }  = P{X E A, Y E (--00, +w)} = J, l+j 
(2, Y) dY dx 
where 

INDEPENDENCE, COVARIANCE, AND CONDlUONAL EXPECTATlON 
633 
is the marginal density for the random variable X; the other density fy(y) 
may be defined similarly. 
The computation of expected values is quite similar to the scalar case. 
Given a function g(X, Y) of the two random variables, we have 
in the discrete case 
g(xl y)f(z, y) dy d x  
From the linearity of these operations, it is easy to see that the expected value 
of a linear combination of random variables, 
in the continuous case. 
n 
z 
= c xixi, 
i=l 
is the same linear combination of the expected values: 
n 
i = l  
However, a similar result does not hold, in general, for variance. Similarly, 
for jointly distributed variables it is not true in general that 
E[S(X)h(Y)I = E[S(X)lE[W-)l. 
To investigate this matter we must deal with the dependence or independence 
between the random variables. 
B.4 
INDEPENDENCE, COVARIANCE, AND CONDITIONAL 
EXPECTATION 
Two random variables X and Y are independent if the two events {X 5 a }  
and {Y 5 b} are independent, i.e., 
F(a, b) = P{X 5 a, Y 5 b} = P{X 5 a}P{Y 5 b} = Fx(a)Fy(b). 
This in turn implies that 
for discrete and continuous variables, respectively. If the variables are inde- 
pendent, it is easy to show that 

634 
REFRESHER ON PROBABILITY THEORY AND STATISTICS 
holds. 
If there is some degree of dependence between random variables, we should 
try to measure it somehow. One measure of mutual dependence is the co- 
variance: 
COV(X, Y) = E[(X - E[X])(Y - E[Y])] = E[XY] - E[X]E[Y]. 
If X and Y are independent, their covariance is zero (but the converse is not 
necessarily true, as the covariance is only one measure of dependence). If 
Cov(X,Y) > 0, Y tends to be large when X is, and small when X is. More 
precisely, when X is above its expected value, then Y is too, and when X 
is below its expected value, then Y is too. As a result, the expected value 
of (X - E[X])(Y - E[Y]) is positive because the two factors tend to have 
the same sign. A similar observation holds when covariance is negative. The 
following properties of the covariance are useful: 
0 Cov(X, X) = Var(X), 
0 Cov(X, Y) = Cov(Y, X), 
0 Cov(aX, Y) = a Cov(Y, X), 
0 Cov(X, Y + 2) = Cov(X, Y) + Cov(X, 2). 
Using these properties (or the definitions), it can be shown that 
Var(X) + Var(Y) + 2 Cov(X, Y), 
Var(X) + Var(Y) - 2 Cov(X, Y). 
Var(X + Y) 
Var(X - Y) 
= 
= 
More generally, 
/ n  
\ 
n 
n 
Thus, for mutually independent variables, the variance of a sum is the sum of 
the variances. 
Example B.6 We often have to work with multivariate normals. Let 
be a vector of normal random variables with expected value p and covariance 
matrix 
X = E[(X - p)(X - /A)’]. 

INDEPENDENCE, COVARIANCE, AND CONDITlONAL EXPECTATION 
635 
Then the joint density function is given by 
where I C I is the determinant of the covariance matrix. If the normal vari- 
ables are mutually uncorrelated, then both the matrix C and its inverse are 
diagonal. This implies that the density function may be factorized into sep- 
arate components, one for each Xi ; hence, uncorrelated normal variables are 
also independent. 
Another property of jointly normal variables is that they may combined 
linearly to yield other jointly normal variables. Given a matrix T E R"?" 
TX is a vector of m jointly normal variables. 
0 
The value of the covariance depends on the magnitude of the random vari- 
ables involved. Often, a normalized measure of dependence is preferred, the 
coefficient of correlation: 
Cov(X, Y )  
pxy = JvqqJviqYJ' 
It can be shown that pxy E [-1,1]. 
Example B.7 Correlation is often used in finance. However, it is important 
to realize its limitations. Consider the following example. 
>> x = -1:0.001:1; 
>> y = sqrt(l-x.^2); 
>> cov(x,y) 
ans = 
0.3338 
0.0000 
0.0000 
0.0501 
Here we have a random variable X which is distributed uniformly on (-1, l), 
and a random variable Y which is deterministically linked to X, 
as 
Y = JZ. 
However, the covariance and the correlation are zero, since 
COV(X, Y) = E[XY] - E[X]E[Y], 
but E[X] = 0, and (because of symmetry) 
1 
E[XY] = 1, 
x J
s
d
x
 = 0. 
The key issue is that the correlation is a measure of linear dependence. Here 
the dependence is non-linear, as the points (X, 
Y )  lie on the upper half of the 
unit circle X 2  + Y 2  = 1. 
0 

636 
REFRESHER ON PROBABILITY THEORY AND STATISTICS 
If two variables are not independent, then knowing something about the 
value taken by one of them can give us valuable information about the other 
one. This leads us to investigate conditioning. Just as we have defined con- 
ditional probabilities for events, we may define conditional expectation. 
This means that we want to know how an event like (Y = y )  influences the 
distribution of X. For discrete random variables we have 
Similarly, for continuous variables 
Conditioning is a useful way to solve many problems. A fundamental property 
is the following: 
In practice, this may be used when fixing the value of a random variable 
makes working with another one easier. Equation (B.l) may be rewritten, in 
concrete, as 
E[X] = E[E[X I Y]]. 
(B.1) 
C E [ X  I Y = yj]P{Y = y j }  in the discrete case 
E [ X ]  = [ j 
E[X I y = 9lfY(Y) dY 
in the continuous case. 
We may also define a conditional variance: 
Var(X I Y )  = E [(X - E[X I Y ] ) 2  
I Y ]  . 
The following formula may be proved for the conditional variance: 
Var(X) = E[Var(X I Y ) ]  + Var(E[X 1 Y]). 
(B.2) 
This formula may be used to compute variance by conditioning, but it also 
implies that 
Var(X) 2 E[Var(X I Y ) ]  
Var(X) 2 Var(E[X I Y ] ) ,  
since variance is a non-negative quantity by definition. These properties may 
be used for variance reduction in Monte Carlo simulation (see section 4.5). 
We would like to close this section by pointing out that our treatment 
of conditioning, apart from being very brief by necessity, has followed the 
classical lines of basic textbooks on probability theory. A solid understanding 
of conditioning and of the role of information in probability requires advanced 
tools which are beyond the scope of this book (see the references). 

PARA METER ESTIMATION 
637 
6.5 
PARAMETER ESTIMATION 
In the theory of probability, we assume a lot of knowledge about a set of 
random variables, and we ask questions about the probability of some events, 
about expected values of functions of those variables, etc. However, the knowl- 
edge required to get those answers, i.e., the whole probability distribution, is 
a scarce commodity. Even the expected value and variance are typically un- 
known, and must be estimated on the basis of samples. The sample data 
might come from the real world (e.g., stock prices) or from a Monte Carlo 
simulation. Typical parameters we want to estimate are the expected value, 
the variance, or the covariance matrix; furthermore, we would also like to 
quantify the reliability of the estimate. 
A random sample should be thought as a set XI , X2, . . . , X, of independent 
and identically distributed random variables, drawn from the same underlying 
distribution. Say that the expected value of the underlying population is p 
and the variance is a2; 
these parameters are unknown, and we would like to 
come up with a reasonable estimate of them. An intuitive way to estimate p 
is to use the sample mean: 
l
n
 
x = - E X i .  
Z=l 
Note that the expected value is an unknown number, whereas the sample 
mean is a random variable. It is a reasonable estimator, in the sense that it 
is unbiased: 
E[X] = p. 
The more samples we get, the better, in the sense that the variance of the 
estimator decreases: 
It is fundamental to understand that in this derivation we have assumed the 
independence of the samples; if the samples are not independent, reasoning 
this way may lead to underestimate the uncertainty in the e ~ t i m a t e . ~  
We 
see from the last formula that, if n goes to infinity, the variance of the es- 
timator goes to zero. So, in some sense, the sample mean should "tend" to 
the unknown expected value. To state this in a mathematically precise way, 
we should introduce concepts of stochastic convergence. In fact, the law of 
large numbers comes in two forms, weak and strong, depending on the kind of 
stochastic convergence we use. We will not consider this issue and settle for 
an intuitive understanding. Another interesting property of the sample mean 
4See, e.g., [2] for a clear discussion of this point. 

638 
REFRESHER ON PROBABILITY THEORY AND STATISTICS 
stems from the central limit theorem. Roughly speaking, when the number 
of samples grow, X tends to be distributed normally. More precisely, we have 
that the distribution of 
x - p  
D l f i  
tends to the standard normal distribution. How many samples it takes to have 
an approximately normal distribution depends on the distribution of the Xi. If 
they are normal, then the sample mean is always normal. If it is symmetric, a 
few samples may be enough; if it is strongly asymmetric (skewed), then many 
samples may be needed. This is not an issue in this book, as we apply these 
ideas to Monte Carlo simulation, where many thousands of samples are taken. 
We should recall again that all of the ideas above rely on the assumption of 
independence between samples. 
Another difficulty derives form the fact that the variance is typically un- 
known too. If we knew p, we could estimate u2 by averaging squared devia- 
tions: 
Since we must use an estimate of p, the estimator of u' 
is the sample vari- 
ance: 
1
"
 
s2 = - 
c 
[Xi -XI2. 
n - 1 .  
z=1 
Note the l/(n - 1) factor, which is essentially due to the use of an estimate of 
p. It can be shown that this factor is needed to make the estimator unbiased 
(E[S'] = u'). By a similar expression we may estimate the covariance between 
two random variables X and Y: 
1
"
 
sxy = - c (Xi - X) (K - F) 
I 
n - 1 
It can be shown that E [ S x y ]  = Cov(X, Y). We can also estimate the corre- 
lation coefficient: 
These tasks are accomplished by MATLAB functions. The basic versions are 
available in the MATLAB core; some advanced functionalities are included 
only in the Statistics toolbox. 

PARAMETER ESTIMATION 
639 
Example B.8 The function mean yields the sample mean. For instance, 
let us use the normrnd function to generate a set of independent normally 
distributed data values5: 
>> randn(’state’,O) 
>> x=normrnd(2,3,1000,2) ; 
>> mean(x) 
ans = 
1.8708 
2.1366 
The first two parameters of normrnd are the expected value and the standard 
deviation of the normal variable; the remaining two are optional and define 
the size of the matrix to generate. The matrix, which here has 1000 rows and 
two columns, is interpreted columnwise, as 1000 realizations of two random 
variables. This is why two means are estimated, one per column of the data 
matrix. The function cov(x> estimates the covariance matrix (assuming a 
column-oriented data matrix). 
>> randn(’state’ ,O) 
>> x=normrnd(l0,2,10000,4) ; 
>> cov(x) 
ans = 
4.0091 
0.0480 
0.0204 -0.0457 
0.0480 
4.0291 
0.0374 -0.0050 
0,0204 
0.0374 
4.0390 
0.0193 
-0.0457 -0.0050 
0.0193 
4.0464 
Note that the values on the diagonal are close to the “correct” variance u2 = 4 
for each of the four independent variables; off-diagonal elements should be 
zero, as the samples should be independent. Given the limited number of 
samples, it is not surprising that the results do not match exactly what we 
would expect in theory. 
Consider 
drawing 100 samples from a normal distribution with known parameters and 
checking if the sample mean corresponds to the known expected value. Let 
us repeat ten of these experiments: 
In practice, estimating parameters may be a tough problem. 
5We use the instruction randn(’state’,O) to make sure you will get the same numbers 
shown here. Otherwise, the numbers you get may differ from the following ones, depending 
on the current state of the random number generator; the issue is explained in section 4.3. 
Furthermore, if you repeat the experiment, you will get different outcomes. 

640 
REFRESHER ON PROBABILITY THEORY AND STATISTICS 
0.0460 
0.1437 
0.2803 
0.0048 
0.1646 
0.4143 
0.1915 
0.4961 
0.0013 
You see that the estimated mean va.Je may be quite different ,,om the correct 
value p = 0.3. Actually, if you repeat the experiment a few times, you will 
even get negative sample means. This is due to the fact that the expected 
value is small with respect to the variance of the data; if you think of esti- 
mating stock returns over short periods, using historical data when volatility 
is high, you will realize that this is not a hypothetical circumstance. This 
phenomenon, called meun blur, is described, e.g., in [3, chapter 81. Another 
point worth mentioning is that if you use historical data, you might question 
the validity of the old data; however, using only the recent ones may lead 
to unreliable estimates. The Financial toolbox includes a more sophisticated 
function (ewstats) to compute a covariance matrix by applying a “forgetting 
factor,” reducing the weight of the old data. 
0 
Given the remarkable amount of variability in the estimator, which is evident 
in the last example, it is clear that we need some way to measure the reliability 
of our estimate. Consider (B.3) and assume we know the (1 - a/2)-quantile 
from the standard normal distribution, i.e., the number 2 1 - a / 2  such that 
where 2 N N(0,l). Then, given the symmetry of the standard normal distri- 
bution, we see that 
This is only approximately true unless the Xi are normal, but given the central 
limit theorem, it will be a good approximation when a large number of samples 
are taken. Rearranging the above inequality, we see that, with probability 
close to 1 - a, we have 
In other words, we may build a confidence interval that, with a suitable 
degree of confidence, will contain the unknown parameter p. Unfortunately, 

PARA METER ESTIMATION 
641 
this is not really true, since we have to estimate u2 by the sample variance. 
Hence, we should consider the distribution of the random quantity: 
It turns out that the distribution is not really standard normal. If the Xi are 
normal, then this ratio is distributed according to a Students’s t distribution 
with n - 1 degrees of freedom. This distribution is qualitatively similar to 
a standard normal distribution, as it is bell shaped and symmetric around 
the origin, but it has fatter tails. In practice, in building the confidence 
interval, we should use the quantiles t n - l , l - a / 2  
from this distribution, where 
tn-l,l-ap > ~ 1 - ~ / 2 .  
This basically means that the confidence interval should 
be wider, which makes sense given the need to estimate more parameters. It 
turns out that when n is large, the t distribution tends to the standard normal 
distribution. Again, all of this is only approximately true in general, since the 
samples are not necessarily normal themselves. However, when the number of 
samples is large, thanks to the central limit theorem, we may use the following 
approximate confidence interval: 
The idea is that if we repeat the sampling and estimation procedure over and 
over, the percentage of cases in which the “true” value falls within this interval 
should be 100 x (1 - a). Typical values of a are 0.05 and 0.01. 
Example B.9 Calling the function [muhat, sigmahat, muci, sigmacil 
= normfit(x) yields an estimate of the expected value and the standard 
deviation and the respective 95% confidence intervals. 
>> randn(’state’,O) 
>> x=normrnd(1,2,100,1); 
>> [mu,s,mci,scil = normfit(x) 
mu = 
1.0959 
1.7370 
0.7512 
1.4405 
1.5251 
2.0178 
s =  
mci = 
sci = 
This function assumes normal samples and uses the quantiles from the t dis- 
tribution. Keeping the above warnings in mind, we may use this function to 
build confidence intervals for parameters we estimate by Monte Carlo simula- 
tion. It is possible to specify a different confidence level by calling the function 
with an optional parameter: normf it (x, alpha). 
0 

642 
REFRESHER ON PROBABlLlTY THEORY AND STATISTICS 
8.6 
LINEAR REGRESSION 
Linear regression by the method of least squares is a two-fold technique. On 
the one hand, we may consider it as a function approximation technique. Say 
that we have a set of n data points (xi, yi), i = 1,. . . , n. We may assume a 
functional form y = f ( x )  linking the data, and we look for the function f(.) 
that yields the best fitting. Linear regression is the case in which we assume 
a linear form: 
y = f ( x )  = a + bx. 
If we define the residual ei as 
ei = yi - f(xi) = yi - (a + bzi), 
(B.4) 
we may look for the optimal parameters a and b minimizing the sum of squared 
residuals: 
n 
n 
e = 
e; = 
(yi - a - bxi)’. 
03.5) 
i=l 
i=l 
Straightforward calculus yields 
where 1 and jj are formally equivalent to sample means, and 
n 
n 
n 
n x x i y i  - C x i  . C y i  
b =  
i=l 
i=l 
i=l 
2
-
 
i=l 
i=l 
All of this has nothing to do with statistics, and it is just a simple case of the 
more general problem of function approximation (see section 3.3). However, 
the expression for b looks suspiciously like the ratio of a sample covariance over 
a sample variance. The following manipulations show that this interpretation 
is not unreasonable: 
n 
n 
1 
n - 1  
c 
( X i  - L1) ( X i  - z) 
- 
C ( X i  - q2 
i=l 
i=l 

LINEAR REGRESSION 
643 
Here we have somewhat misused the notations Sxy 
and 5’2, since we have 
no statistical interpretation of these quantities. A statistical interpretation 
can be given if we assume that our data come from a statistical model. One 
possible model is 
Y,=a+pxa+Ez, 
2’1, 
..., 72, 
03.9) 
where 
the parameters a and ,B are (in practice) unknown numbers; 
E ,  is a random variable such that 
E[Q] = 0, 
Var(ci) = a2, 
i = 1,. . . , n; 
this implies that the errors ~i are identically distributed; 
the random variables ~i are mutually independent and do not depend 
on the associated value of xi; 
the values x, are given numbers. 
The last observation makes sense when the xi is under our control; hence, 
Y, is random due to the impact of the random error, but xi is not. In other 
statistical models, we consider random variables Xi, but the general approach 
does not change that much. 
Under these hypotheses, it can be shown that the regression coefficients 
a and b are unbiased estimators of the parameters a and p. Note that the 
regression coefficients are random because they are influenced by the errors. 
Under additional assumptions on the distribution of the errors, which are 
typically assumed normal, we may build confidence intervals for the estimates. 
Example B.10 The Statistics toolbox offers a function to perform multiple 
linear regression, i.e., linear regression where there are multiple “x” variables. 
It is interesting to carry out a little experiment to understand the nature of 
the problem. Let us assume a linear model: 
Y = 1 0 + 5 ~ + ~  
where E N N(O,4). We consider ten values of x: 
xi = 1 +0.2 x i ,  
i = 0 , l  I..., 9, 
and generate ten random samples as errors. Then we check if the estimates 
we get are close to the known values: 
>> randn(’state’,O) 

644 
REFRESHER ON PROBABILITY THEORY AND STATISTICS 
>> errors=normrnd(0,2,10,1) ; 
>> x = 1 + 0.2*(0:9)’ 
x =  
1.0000 
1.2000 
1.4000 
1.6000 
1.8000 
2.0000 
2.2000 
2.4000 
2.6000 
2.8000 
>> y = 10 + 5*x + errors 
Y -  
14.1349 
12.6688 
17.2507 
18.5754 
16.7071 
22.3818 
23.3783 
21.9247 
23.6546 
24.3493 
>> v = regress(y, [ones(lO,l), XI) 
v =  
7.2801 
6.4328 
What we get, a = 7.2801 and b = 6.4328, is fairly distant from what we know. 
This is due to the amount of noise, but there is another factor. Let us repeat 
the experiment with different x values: 
>> x = (1:lO)’; 
>> y = 10 + 5*x + errors; 
>> v = regress(y, [ones(lO,l), XI) 
v =  
8.4264 
5.2866 
Here the estimates look a bit better. The reason is that the values of x are 
more widespread, and the errors have a smaller impact. If we could reduce 
noise, we would get really close to the correct value: 
>> y = 10 + 5*x + normrnd(O,l,l0,1); 
>> v = regress(y, Cones(lO,l), XI) 
v =  
10.6117 

FOR FURTHER READING 
645 
4.9308 
Of course, we have cheated and this is not what happens in a real setting, 
and confidence intervals for the estimates should be derived. 
0 
We will only use regression in pricing American-style options, and this is why 
we just give this very sketchy overview of an important topic. However, we 
should at least mention the following caveats about linear regression: 
Regression describes association, not causation: we tend to interpret x 
as a cause and Y as an effect, but this need not be true. 
Due to sampling variability we may "see" relationships which are not 
really supported by data. 
On the other hand, since the b parameter is linked to covariance, and 
covariance is only a measure of linear association (see example B.7), 
linear regression may not properly account for more complex, non-linear, 
associations. 
For further reading 
There are many excellent books on probability theory, ranging from the ele- 
mentary to the very sophisticated. 
An introductory book characterized by a remarkable clarity, plenty of 
insightful examples, and a wide range of topics is [5], which does not 
rely on measure-theoretic concepts. 
If you are interested in a more advanced treatment, based on rigorous 
axiomatic foundations, see, e.g., [6]. 
A less encyclopedic, but perhaps more readable, treatment can be found 
in [l]. 
Apart from good statistics books, such as [4], 
a quick and readable 
introduction to parameter estimation may be found in simulation books 
such as [2]. 
REFERENCES 
1. M. Capinski and T. Zastawniak, editors. Probability through Problems. 
Springer-Verlag, Berlin, 2000. 

646 
REFRESHER ON PROBABILITY THEORY AND STATISTICS 
2. A.M. Law and W.D. Kelton. Simulation Modeling and Analysis (3rd ed.). 
McGraw-Hill, New York, 1999. 
3. D.G. Luenberger. 
Investment Science. Oxford University Press, New 
York, 1998. 
4. S .  Ross. Introduction to Probability and Statistics for Engineers and Sci- 
entists (2nd ed.). Academic Press, San Diego, CA, 2000. 
5. S. Ross. Introduction to Probability Models (8th ed.). Academic Press, 
San Diego, CA, 2002. 
6. A.N. Shiryaev. Probability (2nd ed.). Springer-Verlag, New York, 1996. 

Appendix C 
Introduction to A MPL 
In this brief appendix, we want to introduce the basic syntax of AMPL. We 
use AMPL only in the last chapters on optimization models, and the syntax 
is almost self explanatory. Hence, we will just describe a few basic examples, 
so that the reader can get a grasp of the basic language elements. The reader 
is referred to the original reference [l], written by the developers of AMPL. 
Unlike MATLAB, AMPL is not a procedural language. There is a part of the 
language which is aimed at writing scripts, which behave like any program 
based on a sequence of control statements and instructions. But the core 
of AMPL is a declarative syntax to describe a mathematical programming 
model and the data to instantiate it. The optimization solver is separate: 
You can write a model in AMPL, and solve it with different solvers, possibly 
implementing different algorithms. Actually, AMPL interfaces have been built 
for many different solvers; in fact, AMPL is more of a language standard which 
has been implemented and is sold by a variety of providers. 
A demo version is currently available on the web site http: //www . amp1 . corn. 
The reader with no access to a commercial implementation can get the student 
demo and install it following the instructions. This student demo comes with 
two solvers: MINOS and CPLEX. MINOS is a solver for linear and nonlinear 
programming models with continuous variables, developed at Stanford Uni- 
versity. CPLEX is a solver for linear and mixed-integer programming models. 
Originally, CPLEX was a university product, but it is now developed and dis- 
64 7 

648 
/NTRODUCT/ON TO AMPL 
tributed by ILOG. Recent CPLEX versions are able to cope with quadratic 
programming models, both continuous and mixed-integer. All the examples 
in this book have been solved using CPLEX. 
Clearly, software choice is a very subjective matter. I personally work a lot 
integrating MATLAB and ILOG AMPL/CPLEX. But for the sake of fairness, 
alternative modeling languages are listed in the references. 
C . l  RUNNING OPTIMIZATION MODELS IN AMPL 
Typically, optimization models in AMPL are written using two separate files. 
0 A model file, with standard extension * .mod, contains the description 
of parameters (data), decision variables, constraints, and the objective 
function. 
0 A separate data file, with standard extension * . dat, contains data val- 
ues for a specific model instance. These data must match the description 
provided in the model file. 
Both files are normal ASCII files which can be created using any text editor, 
including MATLAB editor (if you are using word processors, be sure you are 
creating plain text files, with no hidden control characters for formatting). It 
is also possible to describe a model in one file, but separating structure and 
data is a good practice, enabling to solve multiple instances of the same model 
easily. 
When you start AMPL, you get a DOS-like window' with a prompt like: 
ampl : 
To load a model file, you must enter a command like: 
ampl: model mymodel.mod; 
where the semicolon must not be forgotten, as it marks the end of a command 
(otherwise AMPL waits for more input by issuing a prompt like am~l?).~ 
To 
load a data file, the command is 
ampl : data mymodel. dat ; 
Then we may solve the model by issuing the command: 
ampl: solve; 
'The exact look of the window and the way you start AMPL depend on the AMPL version 
you use. 
2Here we are assuming that the model and data files are in the same directory as the AMPL 
executable, which is not good practice. It is much better to place AMPL on the DOS path 
and to launch it from the directory where the files are stored. See the manuals for details. 

MEAN VARlANCE EFFlClENT PORTFOLIOS IN AMPL 
649 
To change data without loading a new model, you should do something like: 
ampl: reset data; 
ampl : data mymodel. dat ; 
Using reset ; unloads the model too, and it must be used if you want to load 
and solve a different model. This is also important if you get error messages 
because of syntax errors in the model description. If you just correct the 
model file and load the new version, you will get a lot of error messages about 
duplicate definitions. 
The solver can be select using the option command. For instance, you 
may choose 
ampl: option solver minos; 
or 
ampl: option solver cplex; 
Many more options are actually available, as well as ways to display the solu- 
tion and to save output to files. We will cover only the essential in the follow- 
ing. We should also mention that the commercial AMPL versions include a 
powerful script language, which can be used to write complex applications in 
which several optimization models are dealt with, whereby one model provides 
input to another one. 
C.2 
MEAN VARIANCE EFFICIENT PORTFOLIOS IN AMPL 
The best way to get acquainted with AMPL syntax is by considering a simple 
but relevant example. We describe the theory of mean-variance efficient port- 
folios in section 2.4.2. This framework leads to the solution of the following 
quadratic program: 
min 
w'Xw 
s.t. 
w'F = FT 
n 
AMPL syntax for this model is given in figure C.l. First we define model 
parameters: the number of assets NAssets, the vector of expected return 
(one per asset), the covariance matrix, and the target return. Note that each 
declaration must be terminated by a semicolon, as AMPL does not consider 
end of line characters. The restriction NAssets > 0 is not a constraint of the 
model: It is an optional consistency check that is carried out when data are 
loaded, before issuing the solve command. Catching data inconsistencies as 

650 
lNTRODUCTlON TO AMPL 
param NAssets > 0; 
param ExpRetCl. .NAssets); 
param CovMat(1. .NAssets, 1. .NAssets); 
param TargetRet; 
var WCl..NAssets> >= 0; 
minimize Risk: 
sum (i in 1. .NAssets, j in 1. .NAssets) W[il*CovMatCi,jI*W[jl; 
subject to SumToOne: 
sum Ci in 1. .NAssets) W[il 
= 1; 
subject to MinReturn: 
sum (i in 1. .NAssets> ExpRet [il *WCi] = TargetRet; 
param NAssets := 3; 
param ExpRet := 
10.15 
2 0.2 
3 0.08; 
param CovMat: 
1 
2 
3 
.= 
1 
0.2000 
0.0500 -0.0100 
2 
0.0500 
0.3000 
0.0150 
3 
-0.0100 
0.0150 
0.1000; 
param TargetRet := 0.1; 
Fig. C.1 AMPL model (MeanVar.mod) and data (MeanVar.dat) files for mean- 
variance efficient portfolios. 

MEAN VARIANCE EFFICIENT PORTFOLIOS IN AMPL 
651 
early as possible may be very helpful. Also note that in AMPL it is typical 
(but not required) to assign long names to parameters and variables, which 
are more meaningful than the terse names we use in mathematical models. 
Then the decision variable W is declared; this variable must be non-negative 
to prevent short-selling, and this bound is associated to the variable, rather 
than being declared as a constraint. Finally, the objective function and the 
two constraints are declared. In both cases we use the sum operator, with a 
fairly natural syntax. We should note that braces ({}) are used when declaring 
vectors and matrices, whereas squares brackets ([I) are used to access ele- 
ments. Objectives and constraints are always given a name, so that later we 
can access information such as the objective value and dual variables. Expres- 
sions for constraints and objective can be entered freely. There is no natural 
order in the declarations: We may interleave any type of model elements, 
provided what is used has already been declared. 
In the second part of figure C.l we show the data file. The syntax is fairly 
natural, but you should notice its basic features: 
0 Blank and newline characters do not play any role: We must assign 
vector data by giving both the index and the value; this may look a bit 
involved, but it allows quite general indexing. 
0 Each declaration must be closed by a semicolon. 
0 To assign a matrix, a syntax has been devised that allows to write data 
as a table, with rows and columns arranged in a visually clear way. 
Now we are ready to load and solve the model, and to display the solution: 
ampl: model MeanVar.mod; 
ampl : data MeanVar . dat ; 
ampl: solve; 
CPLEX 9.1.0: optimal solution; objective 0.06309598494 
18 QP barrier iterations; no b a s i s .  
ampl: display W ;  
w [*I := 
1 0.260978 
2 0.0144292 
3 0.724592 
We see that a barrier solver is used, hence, no basis is available; see section 
6.4 to understand this point. We can also evaluate expressions based on the 
output from the optimization models, as well as checking dual variables of 
constraints: 
ampl: display Risk; 
Risk = 0.063096 
ampl : display sqrt (Risk) ; 

652 
INTRODUCTION TO AMPL 
sqrt(Risk) = 0.251189 
ampl: display MinReturn.dua1; 
MinReturn.dua1 = -0.69699 
ampl : display sum {k in 1. . NAssets) W [k] *ExpRet [kl ; 
sum{k in 1 . . NAssets) W[k]*ExpRet Ckl = 0.1 
C.3 THE KNAPSACK MODEL IN AMPL 
We have considered the knapsack model as a trivial model for capital budget- 
ing (example 1.2 on page 15). This is a pure binary programming model: 
i=l 
N 
s.t. 
~
C
i
X
i
 
5 w 
i=l 
xz E {O,l}. 
The corresponding AMPL model is displayed in figure C.2. Again, the syntax 
is fairly natural, and we should just note a couple of points: 
The decision variables are declared as binary. 
In the data file, the two vectors of parameters are assigned at the same 
time to save on writing; you should compare carefully the syntax used 
here against the syntax used to assign a matrix (see the covariance 
matrix in the previous example). 
Now we may solve the model and check the solution (we must use reset to 
unload the previous model): 
ampl: reset; 
ampl: model Knapsack.mod; 
ampl : data Knapsack. dat ; 
ampl: solve; 
CPLEX 9.1.0: optimal integer solution; objective 34 
3 MIP simplex iterations 
0 branch-and-bound nodes 
ampl: display x; 
x [*I := 
1
1
 
2
0
 
3
0
 
4
1
 
, 
In this case, branch and bound is invoked (see chapter 12). In fact, if you are 
using the student demo, you cannot solve this model with MINOS; CPLEX 
must be selected using 

THE KNAPSACK MODEL IN AMPL 
653 
param NItems > 0; 
param Value{l..NItems) >= 0; 
param Cost{l..NItems) >= 0; 
param Budget >= 0; 
var x{l..NItems) binary; 
maximize Totalvalue : 
sum {i in 1. . NItems) Value [il *x [il ; 
subject to AvailableBudget: 
sum {i in 1. .NItems) Cost[il*x[i] <= Budget; 
param NItems = 4; 
param: Value Cost := 
1 
10 
2 
2 
7
1
 
3 
25 
6 
4 
24 
5; 
param Budget := 7; 
Fig. C.2 AMPL model (Knapsack.mod) and data (Knapsack.dat) files for the knap- 
sack model. 

654 
INTRODUCTION TO AMPL 
anpl: option solver cplex; 
If you use MINOS, you will get the solution for the continuous relaxation 
of the model above, i.e., a model in which the binary decision variables are 
relaxed: z E [0,1], instead of z E (0,l). The same can be achieved in ILOG 
AMPL/CPLEX by issuing appropriate commands: 
ampl: option cplex-options 'relax'; 
ampl: solve; 
CPLEX 9.1.0: relax 
Ignoring integrality of 4 variables. 
CPLEX 9.1.0: optimal solution; objective 36.2 
1 dual simplex iterations ( 0  in phase I) 
anpl: display x; 
x [*I := 
1
1
 
2
1
 
3
0
 
4 0.8 
, 
Here we have used the relax option to solve the relaxed model. We may also 
use other options to gain some insights on the solution process: 
ampl: option cplex-options 'mipdisplay 2 ' ;  
ampl: solve; 
CPLEX 9.1.0: mipdisplay 2 
MIP start values provide initial solution with objective 34.0000. 
Clique table members: 2 
MIP emphasis: balance optimality and feasibility 
Root relaxation solution time = 
0.00 sec. 
Nodes 
cuts/ 
Node Left 
Objective IInf Best Integer 
Best Node ItCnt 
Gap 
0 
0 
36.2000 
1 
34.0000 
36.2000 
1 6.47% 
cutoff 
34.0000 
Cuts: 2 
2 0.00% 
Cover cuts applied: 1 
CPLEX 9.1.0: optimal integer solution; objective 34 
2 MIP simplex iterations 
0 branch-and-bound nodes 
To interpret this output, the reader should have a look at chapter 12, where 
the branch and bound method is explained. 

CASH FLOW MATCHING 
655 
param NBonds >0, integer; 
param TimeHorizon >O, integer; 
param BondPriceCl. .NBonds); 
param CashFlow{l..NBonds, l..TimeHorizon); 
param Liability{l..TimeHorizon); 
var x{l. .NBonds) >= 0; 
minimize PortfolioCost: 
sum {i in 1. . NBonds) BondPrice [i] *x [i] ; 
subject to MeetLiability It in l..TimeHorizon): 
sum {i in 1. . NBonds) CashFlow [i, t] *x [i] >= Liability It]; 
Fig. C.3 AMPL model file for simple cash flow matching. 
C.4 
CASH FLOW MATCHING 
As a final example, we consider a cash flow matching model (see section 2.3.2) 
N 
min 
C P ~ X ~  
i = l  
N 
i=l 
xi 2 0. 
The only new point here, with respect to previous models, is the constraint 
which must be replicated for each time period within the planning horizon. 
How this can be accomplished is illustrated in the AMPL model of figure C.3. 
Also note that a few parameters have been restricted to integer variables; the 
integer keyword can also be used to specify general integer decision variables. 
For further reading 
In the literature 
0 AMPL was introduced in [l] by its developers. 
0 There are many other modeling languages. A notable one is GAMS, 
which are similar in spirit to AMPL, in the sense that it is not linked to 
a specific solver. See http : //www . gams . com. GAMS is probably more 

656 
lNTRODUCTlON TO AMPL 
familiar to people in Economics, and it is also used in [2, 31 to develop 
financial optimization models. 
On the Web 
0 The AMPL student version and additional material can be found on 
http: //www . amp1 .corn. There you may also see the list of solvers com- 
patible with AMPL. 
0 For the commercial ILOG AMPL version and the CPLEX solver, see 
http://www.ilog.corn. 
0 MINOS and other optimization solvers from Stanford University are 
described in http : //www . sbsi-sol-opt imize . corn. 
0 We should mention that there are other languages such as LINGO. This 
is a more of a “proprietary” system, as it is linked to a specific opti- 
mization library. See http: //www . lindo. corn. 
REFERENCES 
1. R. Fourer, D.M. Gay, and B.W. Kernighan. AMPL: A Modeling Language 
for Mathematical Programming. Boyd and Fraser, Danvers, MA, 1993. 
2. S. Zenios, editor. A Library of Financial Optimization Models. Blackwell 
Publishers, Oxford, 2006. 
3. S. Zenios. Practical Financial Optimization. Blackwell Publishers, Ox- 
ford, 2006. 

Index 
acceptancerejection method, 233, 
active set method, 365, 378 
ADI, see Alternating Direction Im- 
algorithm 
Alternating Direction Implicit method, 
antithetic 
arbitrage, 71, 103, 126, 415, 486, 
opportunity, 39, 104, 129, 551 
235, 237, 247, 276, 458 
plici t met hod 
polynomial, 145 
319 
sampling, 244, 447, 547 
550 
arc (in a network), 497 
arithmetic 
finite precision, 15 
asset allocation, 73, 77, 506 
asset-liability management, 530, 534, 
augmented Lagrangian method, 351 
556 
backsubstitution, 154 
barrier 
function, 349, 375 
logarithmic, 375 
monitoring, 122 
option, see option, barrier 
binary, 138 
decimal, 138 
in Halton sequence, 270 
feasible solution, 369 
solution, 369 
variable, 369 
function, 174, 204, 503, 512, 
monomial, 175 
base 
basic 
basis, 370 
517 
Bayesian statistics, 26 
Bellman equation, 502, 510 
bias, 259, 512 
biased low estimator, 259 
bid-ask spread, 24 
binary 
binomial 
decision variable, 565 
lattice, see lattice, binomial 
657 

658 
lNDEX 
model, 26 
bisection method, 192, 410 
Black-Derman-Toy (BDT) model, 
Black-Scholes 
127 
equation, 290, 292, 307, 511 
formula, 110, 173, 224 
above par, 31 
at par, 31 
below par, 31 
callable, 31, 125 
convexity, 59 
coupon, 30 
coupon rate, 30 
embedded options, 31 
face value, 30 
option, 125 
par value, 30 
portfolio, 380 
pricing, 52 
yield, 53 
zero-coupon, 30, 49, 124, 128 
condition, 110, 292, 477 
free, 486 
Neumann condition, 478 
Box-Muller method, 236,247, 276, 
branch and bound, 572, 578, 584 
LP-based, 584 
branching, 582, 586 
branching factor, 27 
Brownian bridge, 440, 462 
Brownian motion, see geometric Brow- 
nian motion 
butterfly spread, 248 
buy and hold, 88 
bond, 30 
boundary 
458 
c++, 11 
calibration 
Cox, Ross, and Rubinstein (CRR), 
405, 411 
Jarrow-Rudd, 405 
lattice, 417 
model, 9 
of a binomial lattice, 403 
canonical form (of LP problem), 526 
caplet, 125 
cash flow 
central limit theorem, 236, 241, 631 
central path, 377 
certainty equivalent, 68 
chance constraint, 82, 510 
chance-constrained model, 526 
C heby shev 
matching, 55, 655 
node, 180 
polynomial, 183 
factor, 238, 444 
factorization, see factorization 
Cholesky 
clean price, 381 
code vectorization, 434, 436 
collocation method, 511 
combination 
convex, 390 
linear, 369 
combinatorial optimization, 495 
common random numbers, 251,470, 
compact model formulation, 540 
complementary slackness, 354,355, 
360, 374,377 
complexity, 144, 155 
exponential, 145, 377 
polynomial, 368, 377 
function, 334, 391, 530, 567 
optimization problem, 334 
578 
concave 
condition number, 142, 150 
conditional 
density, 266 
distribution, 504 
expectation, 504,509,512,636 
Monte Carlo, 447, 448 
probability, 530 
Value at Risk (CVaR), 87 
variance, 255, 636 
conditioning, 20, 142, 255 

lNDfX 
659 
confidence 
interval, 240, 640 
level, 83 
consistency, 320 
consistent numerical scheme, 323 
constraint 
active, 333, 354, 366 
bounding, 333 
dualization, 373 
dualized, 358 
equality, 333, 347, 357, 381 
inactive, 333, 354 
inequality, 333, 347, 358, 381 
integrality, 337 
qualification, 351, 353 
consumption-saving problem, 500 
continuation 
region, 118 
value, 117, 414, 419 
continuous-time 
dynamic system, 332 
contraction mapping, 161 
control variate, 253, 447, 455 
convection term, 304 
convection-diffusion equation, 304 
convergence, 168 
global, 204 
linear, 143, 193 
quadratic, 143, 195 
rate of, 143 
combination, 169,300,309,390, 
function, 334, 390, 528, 567 
hull, 342, 368, 390, 394, 570, 
optimization problem, 334 
problem, 527, 528 
set, 334, 335, 390 
convex 
394, 569 
578 
convex hull, 578, 591 
convexity, 63, 113, 334, 359, 389 
correlation, 73, 82, 86, 253, 417 
bond, 380 
coefficient, 638 
coefficient of, 635 
instantaneous, 101, 444 
negative, 244 
positive, 252 
cost-to-go, 498 
covariance, 73, 337, 451, 548, 634 
cover inequality, 590 
covered position, 435 
Cox-Ingersoll-Ross (CIR) model, 
126 
Crank-Nicolson method, 313, 485, 
488 
cumulative distribution function, see 
distribution, function 
cut generation, 591 
cutting plane, 557 
cycling, 371 
matrix, 238, 337, 444 
decision variable, 329 
binary, 565 
semicontinuous, 567, 571 
decomposition, see factorization 
LU, 483 
default, 31, 87 
delta-hedging, 435 
derivative, 4, 33 
descent direction, 338 
diagonal dominance, 163, 168 
differentiable function, 334 
diffusion 
Over the Counter (OTC), 30 
partial differential equation, 292 
term, 304 
direction number, 281 
discounted gain, 552 
discrepancy, 269 
discrete-time 
model, see model 
system, 500 
t, 241 
beta, 234 
conditional, 440 
discrete empirical, 232 
exponential, 231 
distribution 

660 
INDEX 
function, 110, 173, 230, 233, 
625, 626 
joint, 632 
431 
lognormal, 89, 100, 219, 403, 
marginal, 548, 632 
multivariate normal, 238, 548 
normal, 80, 82, 235 
standard normal, 110,173,638 
Student’s t, 641 
symmetric, 82 
uniform, 228 
dividend, 31, 112, 417 
yield, 112, 417 
domain of influence, 302 
drift, 84, 112, 435 
dual 
feasibility, 374 
function, 358, 360, 373 
problem, 358, 373, 552, 557 
variable, 352, 554 
strong, 359, 360 
theory, 358 
weak, 359 
Macauley, 58 
modified, 58 
duality, 372 
duration, 57, 63, 86, 113, 125, 380 
dynamic programming, 210, 332, 
401, 415, 539, 558 
average cost, 501 
discounted, 501 
discrete state, 510 
finite horizon, 502 
infinite horizon, 510 
stochastic, 504 
early exercise, 117, 414, 486 
efficient frontier, 74, 75, 383, 571 
eigenvalue, 148, 162, 163, 239, 311, 
eigenvector, 149 
epigraph, 391, 392, 578 
equation 
boundary, 117 
312, 393, 581 
linear system, 18, 483 
non-linear, 142, 191, 410 
polynomial, 47, 142, 191 
Cournot, 201 
pricing, 37 
absolute, 162, 241 
approximation, 174 
discretization, 430 
function, 178 
relative, 140, 141, 241 
roundoff, 140, 173 
sampling, 430 
truncation, 140, 212 
biased, 469 
high-biased, 519 
low-biased, 519 
unbiased, 637, 643 
equilibrium, see market, equilibrium 
error, 150 
estimator 
Euler scheme, 431 
event, 623 
independent, 624 
excess return, 506 
expected return, see return 
expected value, 626 
explicit method, 305 
extreme 
of a function, 209, 628, 633 
point, 368, 370, 378, 394, 558 
ray, 368, 394, 558 
factorization 
Cholesky, 159, 238 
LU, 157 
QR, 366 
Faure sequence, 472 
feasible 
region, 365, 564 
set, 329 
feedback control, 505 
Feynman-KaE formula, 11 1, 129 
finite difference, 251, 468 
Alternating Direction Implicit, 
319 

lNDEX 
661 
backward, 294, 476 
central, 294, 470, 476 
Crank-Nicolson method, 313 
explicit method, 305, 478 
forward, 294, 476, 482 
fully implicit method, 482 
implicit method, 309 
method, 402, 496 
stability, 423 
symmetric, see finite difference, 
central, see finite differ- 
ence, central 
first-order optimality condition, 334 
fixed point, 510 
fixed-charge problem, 566, 571 
fixed-income 
portfolio, 102 
security, 30 
fixed-mix portfolio, 576 
fixed-point iteration, 161 
floorlet, 125 
Fortran, 11 
forward contract, 33, 35, 103 
Fourier analysis, 302 
free boundary, 118, 293, 511 
function 
affine, 335, 363 
approximation, 173, 505 
concave, 67, 361 
distribution, 84, 178 
indicator, 210, 266 
interpolation, 175 
inverse demand, 201 
non-convex, 581 
non-differentiable, 334, 340 
piecewise linear, 545, 567, 574 
Runge, 180, 186 
strictly concave, 530 
strictly convex, 390, 393 
utility, 176, 530 
function approximation, 642 
functional equation, 498 
future contract, 34 
Gauss-Seidel method, 488 
Gaussian 
elimination, 154 
quadrature, see quadrature 
gearing, 36 
genetic algorithm, 389, 596 
geometric Brownian motion, 98, 116, 
126, 430, 441, 477, 482, 
504 
bidimensional, 443 
global optimization, 564 
gradient 
conjugate, 173 
method, 387 
graph optimization, 496 
Gray code, 283 
Greek, see option, sensitivity 
grid, 476 
notation, 295, 476 
Halton sequence, 269, 276, 458 
heat equation, 292, 303 
bidimensional, 314 
physical interpretation, 304 
hedging, 33, 108, 435 
heuristic method, 591 
homotopy, 205 
Hull-White model, 127 
continuation, 206, 377 
ill-conditioning, 151 
immunization, 63, 125 
importance sampling, 261,450,547 
inadmissibility form, 372 
independent increment, 92, 108 
indicator function, 447 
infinitetime horizon, 501 
initial condition, 292 
inner product, 188, 215 
integer programming, see program- 
integration 
interest 
ming, integer 
numerical, 448 
accrued, 61 
compound, 43 

662 
INDEX 
continuously compounded, 44 
simple, 43 
interest rate, 43 
spot, 52, 56 
term structure, 52, 64 
interest-rate 
cap, 125 
derivative, 9, 124 
dynamics, 126 
floor, 125 
risk management, 125 
swap, 124 
interior point method, 375, 378 
internal rate of return, 47, 53 
interpolation, 212, 503 
intrinsic value, 117, 414, 419 
inverse transform method, 230,234, 
237, 247, 277, 458 
iterative method, 488, 511 
It0 
linear, 479 
lemma, 96, 128, 417, 431 
multidimensional lemma, 101 
stochastic differential equation, 
stochastic integral, 95 
430 
Jacobian 
determinant, 236 
matrix, 197 
Jensen’s inequality, 628, 632 
jump 
in asset price, 6 
Kelley’s cutting planes algorithm, 
knapsack problem, 16,144,337,495, 
Kuhn-Tucker conditions, 351 
kurtosis, 548 
L-shaped decomposition, 365, 540, 
Lagrange 
364, 556 
564, 587, 652 
555, 557 
multiplier, 352, 356, 366, 375, 
535 
polynomial, 212 
function, 351, 354, 358, 375 
multiplier, see Lagrange, mul- 
Lagrangian 
tiplier 
large numbers 
lattice, 214 
strong law of, 222 
binomial, 28, 489, 510 
implied, 426 
method, 496 
recombining, 28 
structure in LCG, 228, 237 
trinomial, 422, 481 
law of large numbers, 637 
law of one price, 51 
Lax’s equivalence theorem, 323 
LCG, see linear congruential gen- 
least squares, 147, 175, 388, 503, 
leverage, 36 
liability, 54, 57, 530 
uncertain, 544 
LIBOR, 130 
likelihood ratio, 262, 450 
limited liability (assets), 31, 32 
line search, 339 
linear congruential generator, 226, 
linear programming, see program- 
erator 
513, 548,642 
267 
ming, linear 
canonical form, 367 
duality, 553 
standard form, 367 
linear regression, 147,388,512,642 
local improvement, 592 
local search, 591, 592 
best-improving, 592 
first-improving, 592 
low-discrepancy sequence, 269,458, 
547 
Halton, 269 
Sobol, 281 
lower bound, 572, 581, 583 

INDEX 
663 
LU decomposition, 310 
marginal density, 633 
market 
complete, 107 
efficiency, 89 
equilibrium, 126 
incomplete, 117, 128 
model, 130 
dynamic system, 498 
state property, 501 
Markovian 
martingale, 25 
matrix 
block-diagonal, 556 
diagonal, 451 
diagonally dominant, 163 
Hessian, 334, 341, 356, 392, 
Hilbert, 18, 150, 191, 619 
orthogonal, 366 
permutation, 156 
positive definite, 239, 341, 393 
positive semidefinite, 337,392, 
393 
singular, 151 
sparse, 80, 160, 556 
triangular, 366 
tridiagonal, 159, 308, 310, 483 
bond, 30 
option, 4, 35 
393, 581 
maturity 
mean absolute deviation, 573 
mean blur, 640 
mean reversion, 102, 127 
mean-variance 
efficient portfolio, 383, 649 
framework, 577 
portfolio optimization, 571 
metaheuristic, 389, 578, 591 
metarnodel, 388 
method 
direct, 144, 154 
Gauss-Seidel, 168, 169 
iterative, 143, 161 
Jacobi, 163 
Microsoft Excel, 11 
MILP, 584 
minimizer, 329 
minimum 
minimum lot, 573 
model 
variance portfolio, 383 
binomial, 39, 105 
calibration, 39, 117 
continuous-state, 29 
continuous-time, 29 
discrete-state, 26 
discrete-time, 27 
modulus 
in LCG, 226 
moment matching, 214, 401, 510, 
548 
monomial, 190 
monomial basis, 512 
Monte Carlo 
integration, 222 
sampling, 528, 547 
Monte Carlo sampling, 505 
multiplier 
in LCG, 226 
naked position, 435 
neighborhood structure, 592 
Nelder-Mead method, 342 
network optimization, 496 
Newton’s method, 195, 197, 204, 
377, 511 
for optimization, 341 
argument, 103 
principle, 50, 51, 106 
node (in a network), 496 
non-anticipativity, 256 
condition, 532, 576 
constraint, 533 
function, 387 
problem, 577 
set, 567 
no-arbitrage 
non-convex 

664 
lNDEX 
non-differentiability, 361 
norm 
L,, 146 
compatible, 148, 163 
Euclidean, 146, 172 
Frobenius, 148 
matrix, 147 
spectral, 148, 150 
subordinate, 149 
vector, 146 
multivariate, 159 
standard distribution, 84 
variate, 247 
normal 
normed linear space, 188 
not-a-knot condition, 184, 188 
null space, 365 
numeraire 
numerical 
good, 38 
instability, 19, 169, 300, 480 
stability, 307, 320 
ture, 504 
numerical integration, see quadra- 
objective function, 329 
separable, 501 
optimal control, 332, 500 
optimal stopping, 414 
optimality principle, 501 
optimization, 198 
discrete, 390 
global, 576 
problem, 172 
optimization method 
active set, 366, 368 
gradient, 339 
interior point, 535 
steepest descent, 339 
subgradient, 340 
trust region, 341 
optimization problem 
concave, see convex 
constrained, 333, 346 
convex, see convex 
dual, 358 
finite-dimensional, 329 
infeasible, 329, 331 
infinite-dimensional, 332 
non-smooth, 347 
relaxed, 358, 581 
unbounded, 329, 331 
unconstrained, 333, 338 
optimizer, 329 
optimum 
global, 329, 334 
local, 329, 334 
American, 4,35, 117,256,478, 
496, 510 
American call, 8 
American put, 414, 486 
American put , 488 
American spread, 417 
as-you-like-it, 255 
Asian, 35, 109 
arithmetic, 454 
arithmetic average, 123 
average rate, 454 
geometric, 457 
geometric average, 123 
at-the-money, 35 
barrier, 119, 446, 478, 486 
Bermudan, 35, 511 
call, 35 
chooser, 255, 519 
continuation value, 117 
delta, 108, 109, 115, 478 
down-and-in put, 119, 447 
down-and-out put, 119, 446, 
485 
European call, 4,110,219,242, 
247, 276, 406, 435, 477, 
615 
European put, 110, 477 
exchange, 443 
exotic, 35, 119 
expiration, 117 
gamma, 115 
Greek, 111, 210 
option, 4, 35 

INDEX 
665 
in-the-money, 35, 117, 266,435, 
477, 513 
intrinsic value, 117, 486 
lookback, 123, 425 
multidimensional, 417 
on a bond, 125 
out-of-the-money, 35,266,435, 
477 
path dependent, 123 
pay-later, 410 
put, 35 
sensitivity, 251, 468, 479 
spread, 444 
weakly path-dependent, 446 
elements, 189 
matrix, 366 
polynomial, 191, 215, 512 
projection, 190 
system, 189 
polynomial, 217 
system, 189 
method, 168, 488 
parameter, 491 
orthogonal 
orthonormal 
overrelaxation 
parity 
for barrier options, 119 
put-call, 104 
partial differential equation, 109 
elliptic, 291 
first-order, 291 
hyperbolic, 291 
linear, 291 
order of, 291 
parabolic, 291, 307 
quasilinear, 291 
second-order, 290 
path generation, 430 
pathwise estimator, 471 
PDE, see partial differential equa- 
Peaceman-Rachford method, 319 
penalty function, 346, 375 
tion 
barrier, 349 
exact, 347 
exterior, 347 
interior, 349, 375 
perturbation analysis, 389 
pivoting, 156 
point 
Poisson 
extreme, 558 
distribution, 625 
process, 6, 100, 232 
random variable, 627 
coordinate, 236 
rejection, 237, 276 
bounded, 394 
function, 329 
interpolating, 212 
interpolation, 179 
Lagrange, 179, 183 
primitive, 281 
polar 
polyhedron, 393 
polynomial 
polytope, 394 
portfolio 
cardinality-constrained, 571 
efficient, 74, 385 
management, 380 
mean-variance optimization, 337 
optimization, 15, 40, 71 
rebalancing, 534 
covered, 435 
long, 33 
naked, 435 
short, 33 
power utility, 509 
predecessor node, 540 
present value, 44, 45, 52, 59 
price 
position 
clean, 61 
dirty, 62 
spot, 103 
linearity of, 51 
pricing 

