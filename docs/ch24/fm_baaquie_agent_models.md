# Agent-Based Modeling of Financial Markets

!!! info "Source"
    **Quantitative Finance for Physicists: An Introduction** by Belal E. Baaquie, Academic Press, 2004.
    These notes are used for educational purposes.

## Agent-Based Modeling of Financial Markets

Chapter 12
Agent-Based Modeling
of Financial Markets
12.1 INTRODUCTION
Agent-based modeling has become a popular methodology in
social sciences, particularly in economics.1 Here we focus on the
agent-based modeling of financial markets [1]. The very idea of
describing markets with models of interacting agents (traders, invest-
ors) does not fit well with the classical financial theory that is based
on the notions of efficient markets and rational investors. However, it
has become obvious that investors are neither perfectly rational nor
have homogeneous expectations of the market trends (see also Section
2.3). Agent-based modeling proves to be a flexible framework for a
realistic description of the investor adaptation and decision-making
process.
The paradigm of agent-based modeling applied to financial markets
implies that trader actions determine price. This concept is similar to
that of statistical physics within which the thermodynamic (macro-
scopic) properties of the medium are described via molecular inter-
actions. A noted expansion of the microscopic modeling methodology
into social systems is the minority game (see [2] and references therein).
Its development was inspired by the famous El Farol’s bar problem [3].
This problem considers a number of patrons N willing to attend a bar
with a number of seats Ns. It is assumed that Ns < N and every patron
prefers to stay at home if he expects that the number of people
129

attending the bar will exceed Ns. There is no communication among
patrons and they make decisions using only information on past
attendance and different predictors (e.g., attendance today is the
same as yesterday, or is some average of past attendance).
The minority game is a simple binary choice problem in which
players have to choose between two sides, and those on the minority
side win. Similarly to the El Farol’s bar problem, in the minority
game there is no communication among players and only a given set
of forecasting strategies defines player decisions. The minority game
is an interesting stylized model that may have some financial implica-
tions [2]. But we shall focus further on the models derived specifically
for describing financial markets.
In the known literature, early work on the agent-based modeling of
financial markets can be traced back to 1980 [4]. In this paper, Beja and
Goldman considered two major trading strategies, value investing and
trend following. In particular, they showed that system equilibrium
may become unstable when the number of trend followers grows.
Since then, many agent-based models of financial markets have
been developed (see, e.g., reviews [1, 5], the recent collection [6] and
references therein). We divide these models into two major groups. In
the first group, agents make decisions based on their own predictions
of future prices and adapt their beliefs using different predictor func-
tions of past returns. The principal feature of this group is that price is
derived from the supply-demand equilibrium [7–10].2 Therefore, we
call this group the adaptive equilibrium models. In the other group, the
assumption of the equilibrium price is not employed. Instead, price is
assumed to be a dynamic variable determined via its empirical relation
to the excess demand (see, e.g., [11, 12]). We call this group the non-
equilibrium price models. In the following two sections, we discuss two
instructive examples for both groups of models, respectively. Finally,
Section 12.4 describes a non-equilibrium price model that is derived
exclusively in terms of observable variables [13].
12.2 ADAPTIVE EQUILIBRIUM MODELS
In this group of models [7–10], agents can invest either in the risk-
free asset (bond) or in the risky asset (e.g., a stock market index). The
risk-free asset is assumed to have an infinite supply and a constant
130
Agent-Based Modeling of Financial Markets

interest rate. Agents attempt to maximize their wealth by using some
risk aversion criterion. Predictions of future return are adapted using
past returns. The solution to the wealth maximization problem yields
the investor demand for the risky asset. This demand in turn deter-
mines the asset price in equilibrium. Let us formalize these assump-
tions using the notations from [10]. The return on the risky asset at
time t is defined as
rt ¼ (pt  pt1 þ yt)=pt1
(12:2:1)
where pt and yt are (ex-dividend) price and dividend of one share of
the risky asset, respectively. Wealth dynamics of agent i is given by
Wi, tþ1 ¼ R(1  pi, t)Wi, t þ pi, tWi, t(1 þ rtþ1)
¼ Wi, t[R þ pi, t(rtþ1  r)]
(12:2:2)
where r is the interest rate of the risk-free asset, R ¼ 1 þ r, and pi, t is
the proportion of wealth of agent i invested in the risky asset at time t.
Every agent is assumed to be a taker of the risky asset at price that is
established in the demand-supply equilibrium. Let us denote Ei, t and
Vi, t the ‘‘beliefs’’ of trader i at time t about the conditional expect-
ation of wealth and the conditional variance of wealth, respectively. It
follows from (12.2.2) that
Ei, t[Wi, tþ1] ¼ Wi, t[R þ pi, t(Ei, t[rtþ1]  r)],
(12:2:3)
Vi, t[Wi, tþ1] ¼ p2
i, tW2
i, tVi, t[rtþ1]
(12:2:4)
Also, every agent i believes that return of the risky asset is normally
distributed with mean Ei, t[rtþ1] and variance Vi, t[rtþ1]. Agents choose
the proportion pi, t of their wealth to invest in the risky asset, which
maximizes the utility function U
max
pi, t {Ei, t[U(Wi, tþ1)]}
(12:2:5)
The utility function chosen in [9, 10] is
U(Wi, t) ¼ log (Wi, t)
(12:2:6)
Then demand pi, t that satisfies (12.2.5) equals
pi, t ¼ Ei, t[rtþ1]  r
Vi, t[rtþ1]
(12:2:7)
Agent-Based Modeling of Financial Markets
131

Another utility function used in the adaptive equilibrium models
employs the so-called constant absolute risk aversion (CARA) function
[7, 8]
U(Wi, t) ¼ Ei, t[Wi, tþ1]  a
2 Vi, t[Wi, tþ1]
(12:2:8)
where a is the risk aversion constant. For the constant conditional
variance Vi, t ¼ s2, the CARA function yields the demand
pi, t ¼ Ei, t[rtþ1]  r
as2
(12:2:9)
The number of shares of the risky asset that corresponds to demand
pi, t equals
Ni, t ¼ pi, tWi, t=pt
(12:2:10)
Since
the
total
number
of
shares
assumed
to
be
fixed
 P
i
Ni, t ¼ N ¼ const

, the market-clearing price equals
pt ¼ 1
N
X
i
pi, t Wi, t
(12:2:11)
The adaptive equilibrium model described so far does not contradict
the classical asset pricing theory. The new concept in this model is the
heterogeneous beliefs. In its general form [7, 10]
Ei, t[rtþ1] ¼ fi(rt1, . . . , rtLi),
(12:2:12)
Vi, t[rtþ1] ¼ gi(rt1, . . . , rtLi)
(12:2:13)
The deterministic functions fi and gi depend on past returns with lags
up to Li and may vary for different agents.3
While variance is usually assumed to be constant (gi ¼ s2), several
trading strategies fi are discussed in the literature. First, there are
fundamentalists who use analysis of the business fundamentals to
make their forecasts on the risk premium dF
EF, t[rtþ1] ¼ r þ dF
(12:2:14)
In simple models, the risk premium dF > 0 is a constant but it can be a
function of time and/or variance in the general case. Another major
strategy is momentum trading (traders who use it are often called
chartists). Momentum traders use history of past returns to make
their forecasts. Namely, their strategy can be described as
132
Agent-Based Modeling of Financial Markets

EM, t[rtþ1] ¼ r þ dM þ
X
L
k¼1
akrtk
(12:2:15)
where dM > 0 is the constant component of the momentum risk
premium and ak > 0 are the weights of past returns rtk. Finally,
contrarians employ the strategy that is formally similar to the momen-
tum strategy
EC, t[rtþ1] ¼ r þ dC þ
X
L
k¼1
bkrtk
(12:2:16)
with the principal difference that all bk are negative. This implies that
contrarians expect the market to turn around (e.g., from bull market
to bear market).
An important feature of adaptive equilibrium models is that agents
are able to analyze performance of different strategies and choose the
most efficient one. Since these strategies have limited accuracy, such
adaptability is called bounded rationality.
In the limit of infinite number of agents, Brock and Hommes offer
a discrete analog of the Gibbs probability distribution for the fraction
of traders with the strategy i [7]
nit ¼ exp [b(Fi, t1  Ci)]=Zt, Zt ¼
X
i
exp [b(Fi, t1  Ci)] (12:2:17)
In (12.2.17), Ci  0 is the cost of the strategy i, the parameter b is
called the intensity of choice, and Fi, t is the fitness function that
characterizes the efficiency of strategy i. The natural choice for the
fitness function is
Fi, t ¼ gFi, t1 þ wi, t, wi, t ¼ pi, t(Wi, t  Wi, t1)=Wi, t1
(12:2:18)
where 0  g  1 is the memory parameter that retains part of past
performance in the current strategy.
Adaptive equilibrium models have been studied in several direc-
tions. Some work has focused on analytic analysis of simpler models.
In particular, the system stability and routes to chaos have been
discussed in [7, 10]. In the meantime, extensive computational model-
ing has been performed in [9] and particularly for the so-called Santa
Fe artificial market, in which a significant number of trading strat-
egies were implemented [8].
Agent-Based Modeling of Financial Markets
133

12.3 NON-EQUILIBRIUM PRICE MODELS
The concept of market clearing that is used in determining price of
the risky asset in the adaptive equilibrium models does not accurately
reflect the way real markets work. In fact, the number of shares
involved in trading varies with time, and price is essentially a dynamic
variable. A simple yet reasonable alternative to the price-clearing
paradigm is the equation of price formation that is based on the
empirical relation between price change and excess demand [4].
Different agent decision-making rules may be implemented within
this approach. Here the elaborated model offered by Lux [11] is
described. In this model, two groups of agents, namely chartists and
fundamentalists, are considered. Agents can compare the efficiency of
different trading strategies and switch from one strategy to another.
Therefore, the numbers of chartists, nc(t), and fundamentalists, nf(t),
vary with time while the total number of agents in the market N is
assumed constant. The chartist group in turn is sub-divided into
optimistic (bullish) and pessimistic (bearish) traders with the numbers
nþ(t) and n(t), respectively
nc(t) þ nf(t) ¼ N, nþ(t) þ n(t) ¼ nc(t)
(12:3:1)
Several aspects of trader behavior are considered. First, the chartist
decisions are affected by the peer opinion (so-called mimetic conta-
gion). Secondly, traders change strategy while seeking optimal per-
formance. Finally, traders may exit and enter markets. The bullish
chartist dynamics is formalized in the following way:
dnþ=dt ¼ (npþ  nþpþ)(1  nf=N) þ
mimetic contagion
nfnþ(pþf  pfþ)=N þ
changes of strategy
(b  a)nþ
market entry and exit
(12:3:2)
Here, pab denotes the probability of transition from group b to group
a. Similarly, the bearish chartist dynamics is given by
dn=dt ¼ (nþpþ  npþ)(1  nf=N) þ
mimetic contagion
nfn(pf  pf)=N þ
changes of strategy
(b  a)n
market entry and exit
(12:3:3)
It is assumed that traders entering the market start with the chartist
strategy. Therefore, constant total number of traders yields the
134
Agent-Based Modeling of Financial Markets

relation b ¼ aN=nc. Equations (12.3.1)–(12.3.3) describe the dynam-
ics of three trader groups (nf, nþ, n) assuming that all transfer
probabilities pab are determined. The change between the chartist
bullish and bearish mood is given by
pþ ¼ 1=pþ ¼ n1exp(U1),
U1 ¼ a1(nþ  n)=nc þ (a2=n1)dP=dt
(12:3:4)
where n1, a1 and a2 are parameters and P is price. Conversion of
fundamentalists into bullish chartists and back is described with
pþf ¼ 1=pfþ ¼ n2 exp(U21),
U21 ¼ a3((r þ n1
2 dP=dt)=P  R  sj(Pf  P)=Pj)
(12:3:5)
where n2 and a3 are parameters, r is the stock dividend, R is the
average revenue of economy, s is a discounting factor 0 < s < 1, and
Pf is the fundamental price of the risky asset assumed to be an input
parameter. Similarly, conversion of fundamentalists into bearish
chartists and back is given by
pf ¼ 1=pf ¼ n2 exp(U22),
U22 ¼ a3(R  (r þ n1
2 dP=dt)=P  sj(Pf  P)=Pj)
(12:3:6)
Price P in (12.3.4)–(12.3.6) is a variable that still must be defined.
Hence, an additional equation is needed in order to close the system
(12.3.1)–(12.3.6). As it was noted previously, an empirical relation
between the price change and the excess demand constitutes the
specific of the non-equilibrium price models4
dP=dt ¼ bDex
(12:3:7)
In the model [11], the excess demand equals
Dex ¼ tc(nþ  n) þ gnf(Pf  P)
(12:3:8)
The first and second terms in the right-hand side of (12.3.8) are the
excess demands of the chartists and fundamentalists, respectively;
b, tc and g are parameters.
The system (12.3.1)–(12.3.8) has rich dynamic properties deter-
mined by its input parameters. The system solutions include stable
equilibrium, periodic patterns, and chaotic attractors. Interestingly,
the distributions of returns derived from the chaotic trajectories
may have fat tails typical for empirical data. Particularly in [14], the
Agent-Based Modeling of Financial Markets
135

model [11] was modified to describe the arrival of news in the market,
which affects the fundamental price. This process was modeled with
the Gaussian random variable e(t) so that
ln Pf(t)  ln Pf(t  1) ¼ e(t)
(12:3:9)
The modeling results exhibited the power-law scaling and temporal
volatility dependence in the price distributions.
12.4 THE OBSERVABLE VARIABLES MODEL
12.4.1 THE FRAMEWORK
The models discussed so far are capable of reproducing important
features of financial market dynamics. Yet, one may notice a degree
of arbitrariness in this field. The number of different agent types and
the rules of their transition and adaptation vary from one model to
another. Also, little is known about optimal choice of the model
parameters [15, 16]. As a result, many interesting properties, such as
deterministic chaos, may be the model artifacts rather than reflections
of the real world.5
A parsimonious approach to choosing variables in the agent-based
modeling of financial markets was offered in [17]. Namely, it was
suggested to derive agent-based models exclusively in terms of observ-
able variables. Note that the notion of observable data in finance
should be discerned from the notion of publicly available data. While
the transaction prices in regulated markets are publicly available, the
market microstructure is not (see Section 2.1). Still, every event in the
financial markets that affects the market microstructure (such as
quote submission, quote cancellation, transactions, etc.) is recorded
and stored for business and legal purposes. This information allows
one to reconstruct the market microstructure at every moment. We
define observable variables in finance as those that can be retrieved or
calculated from the records of market events. Whether these records
are publicly available at present is a secondary issue. More import-
antly, these data exist and can therefore potentially be used for
calibrating and testing the theoretical models.
The numbers of agents of different types generally are not observ-
able. Indeed, consider a market analog of ‘‘Maxwell’s Demon’’ who is
136
Agent-Based Modeling of Financial Markets

able to instantly parse all market events. The Demon cannot discern
‘‘chartists’’ and ‘‘fundamentalists’’ in typical situations, such as when
the current price, being lower than the fundamental price, is growing.
In this case, all traders buy rather than sell. Similarly, when the
current price, being higher than the fundamental price, is falling, all
traders sell rather than buy.
Only price, the total number of buyers, and the total number of
sellers are always observable. Whether a trader becomes a buyer or
seller can be defined by mixing different behavior patterns in the
trader decision-making rule. Let us describe a simple non-equilibrium
price model derived along these lines [17]. We discern ‘‘buyers’’ (þ)
and ‘‘sellers’’ (). Total number of traders is N
Nþ(t) þ N(t) ¼ N
(12:4:1)
The scaled numbers of buyers, nþ(t) ¼ Nþ(t)=N, and sellers, n(t)
¼ N(t)=N, are described with equations
dnþ=dt ¼ vþn  vþnþ
(12:4:2)
dn=dt ¼ vþnþ  vþn
(12:4:3)
The factors vþ and vþ characterize the probabilities for transfer
from seller to buyer and back, respectively
vþ ¼ 1=vþ ¼ n exp (U), U ¼ ap1dp=dt þ b(1  p)
(12:4:4)
Price p(t) is given in units of its fundamental value. The first term in
the utility function, U, characterizes the ‘‘chartist’’ behavior while the
second term describes the ‘‘fundamentalist’’ pattern. The factor n has
the sense of the frequency of transitions between seller and buyer
behavior. Since nþ(t) ¼ 1  n(t), the system (12.4.1)–(12.4.3) is re-
duced to the equation
dnþ=dt ¼ vþ(1  nþ)  vþnþ
(12:4:5)
The price formation equation is assumed to have the following
form
dp=dt ¼ gDex
(12:4:6)
where the excess demand, Dex, is proportional to the excess number of
buyers
Dex ¼ d(nþ  n) ¼ d(2nþ  1)
(12:4:7)
Agent-Based Modeling of Financial Markets
137

12.4.2 PRICE-DEMAND RELATIONS
The model described above is defined with two observable vari-
ables, nþ(t) and p(t). In equilibrium, its solution is nþ ¼ 0:5 and
p ¼ 1. The necessary stability condition for this model is
adgn  1
(12:4:8)
The typical stable solution for this model (relaxation of the initially
perturbed values of nþ and p) is given in Figure 12.1. Lower values of
a and g suppress oscillations and facilitate relaxation of the initial
perturbations. Thus, the rise of the ‘‘chartist’’ component in the utility
function increases the price volatility. Numerical solutions with the
values of a and g that slightly violate the condition (12.4.8) can lead to
the limit cycle providing that the initial conditions are very close to
the equilibrium values (see Figure 12.2). Otherwise, violation of the
condition (12.4.8) leads to system instability, which can be interpreted
as a market crash.
The basic model (12.4.1)–(12.4.7) can be extended in several
ways. First, the condition of the constant number of traders (12.4.1)
0.8
0.85
0.9
0.95
1
1.05
1.1
1.15
1.2
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
Time
Price
−0.4
−0.3
−0.2
−0.1
0
0.1
0.2
0.3
0.4
Dex
Price
Dex
Figure 12.1 Dynamics of excess demand (Dex) and price for the model
(12.4.5)–(12.4.7) with a ¼ b ¼ g ¼ 1, nþ(0) ¼ 0.4 and p(0) ¼ 1.05.
138
Agent-Based Modeling of Financial Markets

can be dropped. The system has three variables (nþ, n, p) and
therefore may potentially describe deterministic chaos (see Chapter
7). Also, one can randomize the model by adding noise to the utility
function (12.4.4) or to the price formation equation (12.4.6). Interest-
ingly, the latter option may lead to a negative correlation between
price and excess demand, which is not possible for the deterministic
equation (12.4.6) [17].
12.4.3 WHY TECHNICAL TRADING MAY BE SUCCESSFUL
A simple extension of the basic model (12.4.1)–(12.4.7) provides
some explanation as to why technical trading may sometimes be
successful [18]. Consider a system with a constant number of traders
N that consists of ‘‘regular’’ traders NR and ‘‘technical’’ traders
NT: NT þ NR ¼ N ¼ const. The ‘‘regular’’ traders are divided into
buyers, Nþ(t), and sellers, N(t): Nþ þ N ¼ NR ¼ const. The rela-
tive
numbers
of
‘‘regular’’
traders,
nþ(t) ¼ Nþ(t)=N
and
n(t) ¼ N(t)=N, are described with the equations (12.4.2)–(12.4.4).
The price formation in equation (12.4.6) is also retained. However,
0.2
0.4
0.6
0.8
1
1.2
1.4
1.6
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
55
60
Time
Price
−1
−0.8
−0.6
−0.4
−0.2
0
0.2
0.4
0.6
0.8
1
Dex
Price
Dex
Figure 12.2 Dynamics of excess demand (Dex) and price for the model
(12.4.5)–(12.4.7) with a ¼ 1.05, b ¼ g ¼ 1, nþ(0) ¼ 0.4 and p(0) ¼ 1.05.
Agent-Based Modeling of Financial Markets
139

the excess demand, in contrast to (12.4.7), incorporates the ‘‘tech-
nical’’ traders
Dex ¼ d(nþ  n þ FnT)
(12:4:9)
In (12.4.9), nT ¼ NT=N and function F is defined by the technical
trader strategy. We have chosen a simple technical rule ‘‘buying on
dips – selling on tops,’’ that is, buying at the moment when the price
starts rising, and selling at the moment when price starts falling
F(k) ¼
1,
p(k) > p(k  1) and p(k  1) < p(k  2)
1,
p(k) < p(k  1) and p(k  1) > p(k  2)
0,
otherwise
8
<
:
(12:4:10)
Figure 12.3 shows that inclusion of the ‘‘technical’’ traders in the
model strengthens the price oscillations. This result can be easily
interpreted. If ‘‘technical’’ traders decide that price is going to fall,
they sell and thus decrease demand. As a result, price does fall and
the ‘‘chartist’’ mood of ‘‘regular’’ traders forces them to sell. This
suppresses price further until the ‘‘fundamentalist’’ motivation of
0.92
0.94
0.96
0.98
1
1.02
1.04
1.06
1.08
1
5
9
13
17
21
25
29
33
37
41
45
49
Time
Price
nT = 0
nT = 0.005
Figure 12.3 Price dynamics for the technical strategy (12.4.10) for
a ¼ g ¼ d ¼ n ¼ 1 and b ¼ 4 with initial conditions nþ(0) ¼ 0.4 and p(0)
¼ 1.05.
140
Agent-Based Modeling of Financial Markets

‘‘regular’’ traders becomes overwhelming. The opposite effect occurs
if ‘‘technical’’ traders decide that it is time to buy: they increase
demand and price starts to grow until it notably exceeds its funda-
mental value. Hence, if the ‘‘technical’’ traders are powerful enough in
terms of trading volumes, their concerted action can sharply change
demand upon ‘‘technical’’ signal. This provokes the ‘‘regular’’ traders
to amplify a new trend, which moves price in the direction favorable
to the ‘‘technical’’ strategy.
12.4.4 THE BIRTH OF A LIQUID MARKET
Market liquidity implies the presence of traders on both the bid/ask
sides of the market. In emergent markets (e.g., new electronic
auctions), this may be a matter of concern. To address this problem,
the basic model (12.4.1)–(12.4.7) was expanded in the following way
[19]
dnþ=dt ¼ vþn  vþnþ þ SRþi þ rþ
(12:4:11)
dn=dt ¼ vþnþ  vþn þ SRi þ r
(12:4:12)
The functions Ri(i ¼ 1, 2, . . . , M) and r are the deterministic and
stochastic rates of entering and exiting the market, respectively. Let us
consider three deterministic effects that define the total number of
traders.6 First, we assume that some traders stop trading immediately
after completing a trade as they have limited resources and/or need
some time for making new decisions
Rþ1 ¼ R1 ¼ bnþn, b > 0
(12:4:13)
Also, we assume that some traders currently present in the market will
enter the market again and will possibly bring in some ‘‘newcomers.’’
Therefore, the inflow of traders is proportional to the number of
traders present in the market
Rþ2 ¼ R2 ¼ a(nþ þ n), a > 0
(12:4:14)
Lastly, we account for ‘‘unsatisfied’’ traders leaving the market.
Namely, we assume that those traders who are not able to find the
trading counterparts within a reasonable time exit the market
Agent-Based Modeling of Financial Markets
141

Rþ3 ¼
c(nþ  n)
if nþ > n
0,
if nþ  n

R3 ¼
c(n  nþ)
if n > nþ
0,
if n  nþ

(12:4:15)
We call the parameter c > 0 the ‘‘impatience’’ factor. Here, we neglect
the price variation, so that vþ ¼ vþ ¼ 0. We also neglect the sto-
chastic rates r. Let us specify
nþ(0)  n(0) ¼ d > 0:
(12:4:16)
Then equations (12.4.11)–(12.4.12) have the following form
dnþ=dt ¼ a(nþ þ n)  bnþn  c(nþ  n)
(12:4:17)
dn=dt ¼ a(nþ þ n)  bnþn
(12:4:18)
The equation for the total number of traders n ¼ nþ þ n has the
Riccati form7
dn=dt ¼ 2an  0:5bn2 þ 0:5bd2 exp (2ct)  cd exp (ct)
(12:4:19)
Equation (12.4.19) has the asymptotic solution
n0 ¼ 4a=b
(12:4:20)
An example of evolution of the total number of traders (in units of n0)
is shown in Figure 12.4 for different values of the ‘‘impatience’’
factor. Obviously, the higher the ‘‘impatience’’ factor, the deeper the
minimum of n(t) will be. At sufficiently high ‘‘impatience’’ factor, the
finite-difference solution to equation (12.4.19) falls to zero. This
means that the market dies out due to trader impatience. However,
the exact solution never reaches zero and always approaches the
asymptotic value (12.4.20) after passing the minimum. This demon-
strates the drawback of the continuous approach. Indeed, a non-zero
number of traders that is lower than unity does not make sense. One
way around this problem is to use a threshold, nmin, such that
n  (t) ¼ 0 if n  (t) < nmin
(12:4:21)
Still, further analysis shows that the discrete analog of the system
(12.4.17)–(12.4.18) may be more adequate than the continuous model
[19].8
142
Agent-Based Modeling of Financial Markets

12.5 REFERENCES FOR FURTHER READING
Reviews [1, 5] and the recent collection [6] might be a good starting
point for deeper insight into this quickly evolving field.
12.6 EXERCISES
**1. Discuss the derivation of the GARCH process with the agent-
based model [21].
**2. Discuss the insider trading model [22]. How would you model
agents having knowledge of upcoming large block trades?
**3. Discuss the parsimony problem in agent-based modeling of
financial markets (use [16] as the starting point).
**4. Discuss the agent-based model of business growth [23].
**5. Verify if the model (12.4.1)–(12.4.7) exhibits a price distribu-
tion with fat tails.
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
0
2
4
6
8
10
12
14
16
Time
n/no
1
2
3
Figure 12.4 Dynamics of the number of traders described with equation
(12.4.19) with a ¼ 0.25, b ¼ 1, nþ(0) ¼ 0.2, and n(0) ¼ 0.1: 1 - c ¼ 1; 2 - c ¼
10; 3 - c ¼ 20.
Agent-Based Modeling of Financial Markets
143

This page intentionally left blank 

