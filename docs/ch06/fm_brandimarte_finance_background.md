# Finance Background & Numerical Foundation

!!! info "Source"
    **Numerical Methods in Finance and Economics** by Paolo Brandimarte, Wiley, 2nd ed., 2006.
    These notes are used for educational purposes.

## Financial Background

Part I 
~~ 
Background 

This Page Intentionally Left Blank

Mo tiva t io n 
Cornnion wisdom would probably associate the ideas of numerical methods 
aiid number crunching to problems in science and engineering, rather than 
finance. This irit.uit.ive view is contradicted by the relatively large number of 
books and scicritific journals devoted to computational finance; even more so, 
hy thc fact, that, these methods are not confined to academia, but are actually 
usrd in real life. As a result, there has been a steady increase in the number 
of academic programs devoted to quantitative finance, both at Master’s and 
Pt1.D. level, and they usually include a course on numerical methods. Fur- 
thermore, riiany people with a quantitative or numerical analysis background 
have started working in finance, including engineers, mathematicians, and 
physicists. 
Indeed, as the tern1 financial engineering may suggest, computational fi- 
nance is a field where different cultures meet. Hence, a wide array of students 
and practitioners, with diverse background, will hopefully be interested in a 
book on riurrirrical methods for finance. On t,he one hand, this is good news 
for the author. On the other one, the first difficult task is to get evcryonc 
on coniriion ground as far as financial theory and the basics of numerical 
aiialysis are concerned; if treatment is too brief, there is a significant risk of 
losing a considerable subset of readers along the way; if it is too detailed, 
aiiot,her subset will be considerably bored. The aim of the first three chapters 
is t,o “synchronize” readers with a background in Finance and readers with 
it scient.ific background, including students in Engineering, Mathematics, and 
Physics. In chapter 2, we will give the second subset of readers an overview 
of coiicept,s in finance, with an emphasis on asset pricing and portfolio man- 
3 

4 
MOT/VAT/ON 
agement. The first subset of readers will find a reasonably self-contained 
treatment on classical topics of numerical analysis in chapter 3. 
In this introductory chapter we want to give a preview of the problems we 
will deal with, along with some motivation. The reader who is unfamiliar with 
some topics just outlined here should not be worried, as they are not taken 
for granted and will be treated thoroughly in the next chapters. We want to 
make three points: 
1. In financial engineering we need numerical methods (section 1.1). 
2. We need sophisticated and user-friendly numerical computing environ- 
ments, such as MATLAB' (section 1.2), even if this does not prevent at 
all the use of (relatively) low-level languages such as Fortran or C++ or 
spreadsheets such as Microsoft Excel. 
3. Whatever software tool we select, we need a reasonably strong theoreti- 
cal background, as we must often select among competing methods and 
many things may go wrong with them (section 1.3). 
1.1 NEED FOR NUMERICAL METHODS 
Probably, the best-known result in financial engineering is the Black-Scholes 
formula to price options on stocks.2 Options are a class of derivatives, i.e., 
financial assets whose value depends on another asset, called the underlying. 
The underlying can also be a non-financial asset, such as a commodity, or an 
arbitrary quantity representing a risk factor to someone, such as weather, so 
that setting up a market to transfer risks makes sense. Options are contracts 
with very specific rules for issuing, trading, and accounting. For instance, 
a European-style call option on a stock gives the holder the right, but not 
the obligation, of buying a given stock at a given time (maturity, denoted 
by T ) ,  for a prespecified price (the strike price, denoted by K ) .  Similarly, 
a put option gives the right to sell the underlying asset at a predetermined 
strike price. In European-style derivatives, the right specified in the contract 
can only be exercised at maturity T; in American-style derivatives, one can 
exercise her right at any time before T ,  which in this case plays the role of the 
expiration date of the option. 
In the case of a European-style call option, if the asset price at maturity is 
S(T), then the payoff is max{S(T) - K ,  0). The rationale here is that, under 
idealized assumptions on financial markets, the option holder could purchase 
'MATLAB is a registered trademark of The Mathworks, Inc. For more information, see 
http://vvv.mathvorks.com. 
2The formula was published by Fisher Black and Myron Scholes in 1973. A similar research 
line had been pursued by Robert Merton, and in fact Scholes and Merton were awarded the 
Nobel prize in Economics in 1997. By that time, unfortunately, Fisher Black was deceased. 

NEED FOR NUMERICAL METHODS 
5 
the underlying asset at the prevailing price S(T) and immediately sell it at 
price K .  Clearly, the option holder will do so only if this results in a positive 
profit. Actually, market imperfections, such as transaction costs or bid-ask 
spreads, prevent such an idealized trade: even if S(T) is the last quoted price, 
there is no guarantee that the option holder can actually buy the stock at 
that price. In the book we will neglect such issues, which are related to the 
micro-structure of financial markets. 
If we are at a time instant t < T ,  we would like to assign a value, or a fair 
price, to the option. However, what we know is only the current price S(t) 
of the underlying asset, whereas its price S(T) at maturity is not known. If 
we build some mathematical model for the dynamics of the price S(t) as a 
function of time, we may regard S(T) as a random variable; hence, the payoff 
is random as well, and there seems to be no trivial way to price this contract. 
Let f (S(t), t )  be the price of the option at time t if the current price of the 
underlying asset is S(t); to ease the notation burden we will usually write it 
as f (S, t). It can be shown that, under suitable assumptions, the value of the 
contract really depends only on t and S, and it satisfies the following partial 
differential equation (PDE): 
af 
1 
2 2d2f 
af 
at 
2 
as2 
as 
-+--a 
S - + r S - - r f  
= O ,  
where r is the risk-free interest rate, i.e., the rate of interest one can earn by 
investing her money in a safe account, and -a is a parameter related to the 
volatility of the price of the underlying asset, which is a risky asset. Typically, 
we are interested in the current value f(So,O), 
where So = S(0). Equation 
(1.1), with the addition of suitable boundary conditions linked to the type of 
option, may be solved analytically in some cases. For instance, if we denote 
the cumulative distribution function3 for the standard normal distribution by 
N ( z )  = P{Z 5 z } ,  where 2 is a standard normal variable, the price CO for a 
European call option at time t = 0 is 
CO = S O N ( ~ ~ )  - ~ e - ' ~ ~ ( d 2 ) ,  
(1.2) 
where 
ln(So/K) + (r + -a2/2)T 
ln(So/K) + (r - -a2/2)T 
dl = 
U J T  
mm 
1 
d2 
= 
= dl --a&. 
This formula is easy to evaluate, but in general we are not so lucky. The com- 
plexity of the PDE or of some additional conditions, which we must impose to 
fully characterize a specific option, may require numerical methods. We will 
3See appendix B for a refresher on Probability and Statistics. 

6 
MOTNATION 
cover relatively simple numerical methods for solving PDEs, based on finite 
differences, in chapter 5, and applications to option pricing will be illustrated 
in chapter 9. Using finite differences, in turn, may call for the repeated solu- 
tion of systems of linear equations, which is among the topics of chapter 3 on 
numerical analysis. 
Apart from the obvious computational advantage, analytical formulas are 
of great importance in gaining insights into how different factors affect option 
prices. They also allow quick calculation of price sensitivities with respect to 
such factors, which are relevant for risk management. In the book, we will 
use analytical formulas quite often in order to validate numerical methods, 
by comparing the numerical result with the theoretically correct one. This is 
of no practical value by itself, but it is very instructive. Finally, we will also 
see that when a complex option cannot be priced analytically, knowing an 
analytical pricing formula for a related simpler option can be of great value. 
In option pricing by Monte Carlo simulation (see below), analytical pricing 
formulas may yield control variates useful to reduce variance in the estimate 
of price. 
Nevertheless, we should note that the distinction between numerical and 
analytical methods is sometimes a bit blurred. It may happen that analytical 
formulas are quite complicated. As an example, let us consider the following 
formula, which we give without much explanation4: 
This is a formula for the price of a European-style call option when price 
jumps are included in the model. The Black-Scholes model assumes contin- 
uous paths for prices, and this formula by Robert Merton generalizes to a 
model in which jumps occur according to a compound Poisson process. Here 
CBLS(S, 
T, K ,  u2, r )  is the standard Black-Scholes formula with the usual in- 
put arguments; X is related to the rate of jumps, i.e., the expected number of 
jumps per unit time; X ,  is a random variable related to the size of jumps, and 
expectation in the formula is with respect to this variable; x is a number which 
is also related to the probability distribution of jump sizes. Even without fully 
understanding this formula, which goes beyond the scope of this introductory 
book, it is clear that evaluating it is not so trivial and calls for some computa- 
tional approximation. Nevertheless, it gives an explicit representation of the 
effect of each factor affecting price, whereas in a purely numerical approach 
this important information is lost. 
Even in the simple case of equation (1.2), some numerical method is actu- 
ally applied, since we have to evaluate the function: 
J' 
e-y2I2 dy, 
N ( 2 )  = - 
1 
J23; -ca 
4See [5, page 3201 for details. 

NEED FOR NUMERICAL METHODS 
7 
where the integral cannot be solved in closed form. Here, we may evaluate 
the integral by quite efficient ad hoc approximation formulas, rather than by 
general-purpose methods for numerical integration. Sometimes, however, we 
have to compute or approximate integrals in multiple dimensions. In fact, 
thanks to a result known as Feynman-KaE formula, the solution of a PDE 
such as (1.1) can be expressed as an expected value. This and other pricing 
arguments imply that option prices may be expressed as expected values, 
which boil down to an integral. Unfortunately, when expectation is taken with 
respect to many random variables, standard methods to compute integrals in 
low-dimensional spaces fail. 
In other problem settings, we have to approximate a function defined by 
an integral. For instance, consider a function g ( x ,  y) and define a function of 
b 
x by 
F ( x )  = 
d X l  Y)fY(Y) dY- 
Such a situation occurs often in stochastic optimization, when x is a decision 
variable influencing the result, which is only partially under our control be- 
cause of the effect of a random “disturbance” Y ,  
whose density is fy(y) over 
the support [a, b] (possibly (-a, 
+o;))). The function F(x) can be consid- 
ered as the expected cost or profit resulting from our decisions. We will see 
concrete examples in chapters 10 and 11. 
Since computing integrals is so important, chapter 4 is entirely devoted to 
this topic. Apart from deterministic integration methods, we will also deal 
extensively with random sampling methods known as Monte Carlo integration 
or Monte Carlo simulation. Monte Carlo simulation has a incredibly wide 
array of applications, including option pricing and risk management. For 
instance, it can be shown that the price of a European call option at time 
t = 0 is given by the following expected value: 
c = EQ [eprT max{ST - K, 
0}] , 
where ST is the (random) price of the underlying asset at maturity, and the 
expected value is taken under a suitably chosen probability measure (denoted 
by a). In other words, the option value is the expected value of the payoff, 
discounted back to time t = 0, under a certain probability measure. If we are 
able to generate A4 independent random samples Sg), j = 1,. . . , M ,  of the 
asset price, under probability measure Q, then by the law of large numbers 
we could estimate the expected value by the sample mean 
This is the essence of Monte Carlo simulation, and a number of tricks of the 
trade are needed in order to obtain a reliable and computationally efficient es- 

8 
MOTIVATION 
timate.5 Variance reduction methods and alternative integration approaches 
based on low-discrepancy sequences will be introduced in chapter 4, and ap- 
plications to option pricing are illustrated in chapter 8. 
Another widely applied approach to option pricing is based on binomial 
or trinomial lattices. These can be regarded as a sort of clever discretization 
of the underlying stochastic process. From this point of view, they are a 
deterministic way to generate sample paths, whereas Monte Carlo is based on 
random sample path generation. Another point of view is that certain finite 
difference approaches can be regarded as generalization of trinomial lattices. 
We will see applications of these methods in chapter 7. 
Another major topic of the book is optimization, which is introduced in 
chapter 6. Optimization models and methods play many different roles in 
finance. In the option pricing context, optimization is at the core of pricing 
American-style options. Since American-style options may be exercised at any 
time before expiration, optimal exercise strategies must be accounted for in 
pricing. For instance, in an American-style call option, it would be tempting 
to exercise the option as soon as it gets in-the-money, i.e., when S(t) > K for 
a call option and you could earn an immediate profit. However, one should 
also wonder if it could be better to wait for a better opportunity. This is 
not a trivial problem; indeed, it can be shown that it is never optimal to 
exercise an American-style call option on a stock, unless it pays dividends 
before expiration. 
An older type of application of optimization methods is portfolio manage- 
ment. Given a set of assets in which one can invest her wealth, we must 
decide how much should be allocated to each one of them, given some char- 
acterization of the uncertainty in assets return. The best-known portfolio 
optimization model is based on the idea of minimizing the variance of port- 
folio return (a measure of risk), while meeting a constraint on its expected 
value. This leads to mean-variance portfolio theory, a topic pioneered by 
Harry Markowitz in the 1950s. While somewhat idealized, this model had 
an enormous practical and theoretical impact, eventually earning Markowitz 
a Nobel prize in Economics in 1990.6 Since then, many different approaches 
to portfolio optimization have been developed, and they will be illustrated in 
chapters 10, 11, and 12. 
5As we mentioned, option pricing by solving a partial differential equation or by computing 
an expectation are theoretically equivalent approaches, via Feynman-KaE formula. How- 
ever, they can be quite different in computational terms. It is interesting to note that, 
historically, Black-Scholes formula was first obtained by solving the pricing PDE analyti- 
cally, whereas the recent tendency is to use expectation based approaches because of their 
generality. 
6Markowitz shared the prize with Merton Miller and William Sharpe. What is probably 
less known is that he was among the developersof SimScript, one of the first programming 
languages for discrete-event simulation. By the way, Robert Merton had a background in 
engineering. This shows how artificial the barriers between Economics and Engineering 
may be. 

NEED FOR NUMERICAL COMPUTING ENVIRONMENTS: WHY MATLAB? 
9 
It is also important to note that asset pricing and portfolio optimization are 
not necessarily disjoint topics. Many Financial Economics theories are based 
on portfolio optimization models which in turn lead to asset pricing models. 
We will not cover these topics, however, both because of space limitations and 
because they are not strictly related to numerical methods. 
There are still other kinds of application of optimization methods, which 
may more instrumental, such as parameter fitting or model calibration. In 
complex markets, asset prices may depend on a set of unobservable parame- 
ters, and one would like to introduce and price a new asset, in a way which 
is coherent with observed prices for other traded assets. To do so, a typical 
approach is the following. First we build a theoretical pricing model, depend- 
ing on such parameters. Then we try to find values for these Parameters, 
which are as coherent as possible with observed prices. Let a be the vector 
of unknown parameters; according to the asset pricing model, the theoretical 
price of asset j should be Pj(a), 
whereas the observed price is P:. 
We would 
like to get a vector of parameters yielding the best fit. A standard way to do 
so is solving the following optimization model: 
Then, given the optimal set of parameters, we may proceed to price new as- 
sets using the theoretical model. This type of approach is essential in pricing 
interest-rate derivatives. Interest-rate derivatives are considerably more diffi- 
cult to analyze than options on stocks and are outside the scope of this book; 
we will just outline the related issues in section 2.8. 
As expected, some simple optimization models may be solved analytically, 
yielding quite useful insights. However, as a rule, very sophisticated compu- 
tational approaches are needed. 
1.2 NEED FOR NUMERICAL COMPUTING ENVIRONMENTS: WHY 
MATLAB? 
MATLAB is an interactive computing environment, providing both basic and 
sophisticated functions. You may use built-in functions to solve possibly com- 
plex but standard problems, or you may devise your own programs by writing 
them as M-files, i.e., as text files including sequences of instructions written 
in a high-level matrix-oriented language. Moreover, MATLAB has a rich set 
of graphical capabilities, which we will use in a very limited fashion, includ- 
ing the ability of quickly developing graphical user interfaces. The unfamiliar 
reader is referred to appendix A for a quick tour of MATLAB programming. 
Some classical numerical problems are readily solved by MATLAB func- 
tions. They include: 
0 Solving systems of linear equations 

10 
MOTIVATION 
0 Solving non-linear equations in a single unknown variable (including 
polynomial equations as a special case) 
0 Finding minima and maxima of functions of a single variable 
0 Approximating and interpolating functions 
0 Computing definite integrals (in low-dimensional spaces) 
0 Solving ordinary differential equations, as well as some simple PDEs 
This and much more is included in the basic MATLAB core. More complex 
versions of these problems may be solved by other MATLAB ready-to-use 
functions, but you have to get the appropriate toolbox. A toolbox is simply a 
set of functions written in the MATLAB language, and it is usually provided 
in source form, so that the user may customize or use the code as a starting 
point for further work. For instance, the Optimization toolbox is needed to 
solve complex optimization problems, involving several decision variables and 
possibly complex constrains, as well as to solve systems of non-linear equa- 
tions. Another relevant toolbox for finance is the Statistics toolbox, which 
includes many more functions than we will use. In particular, it offers func- 
tions to generate pseudorandom numbers that are needed to carry out Monte 
Carlo simulations. Based on the Statistics and Optimization toolboxes, a 
Financial toolbox was first devised a few years ago, which included differ- 
ent groups of functionalities. Some were low-level functions aimed a.t date 
and calendar manipulation or finance-oriented charting, which are building 
blocks for real-life applications; others dealt with simple fixed-income assets, 
portfolio optimization, and derivatives pricing. 
After this first toolbox, others were introduced which are directly related 
to finance: 
0 GARCH toolbox 
0 Financial time series toolbox7 
0 Financial derivatives toolbox 
0 Fixed-income toolbox 
We will not deal with such toolboxes in the book, but information can be ob- 
tained by browsing The Mathworks’ Web site (http: //www .mathworks. corn). 
We should also mention that other toolboxes, which were not specifically de- 
veloped for financial applications, could be useful, such as the PDEs toolbox 
’At the time of writing, the functionalities of this toolbox have been included in the Finan- 
cial toolbox. 

NEED FOR NUMERICAL COMPUTING ENVIRONMENTS: WHY MATLAB? 
11 
or the genetic and direct search toolbox.8 Other more instrumental tools are 
useful to develop professional applications, such as Excel link, Web server, 
the compiler, or the Datafeed module enabling web connections to different 
financial web sites. 
Now the question is: Why choose MATLAB for this book? Indeed, there 
are different competitors, at different levels: 
0 User-friendly spreadsheets, such as Microsoft Excel. In fact, there are 
spreadsheet-based books showing how optimization and simulation meth- 
ods may be applied to financial problems. Spreadsheets are equipped 
with solvers able to cope with small-scale mathematical programming 
problems, and extensions are available to run Monte Carlo simulations 
or optimization by genetic algorithms. 
0 On the opposite side of the spectrum, one could use low-level languages 
such as C++ or Fortran. C++ seem a favorite, if you look at the number 
of books on computational finance based on this language, but there 
are people maintaining that the recent versions of Fortran do still have 
some advantages. C++ or Fortran may be used either to implement the 
algorithms directly or to call available scientific computing libraries. 
0 There are also specialized libraries or environments, such as statistical 
or optimization tools. 
How does MATLAB compare against such alternatives? The obvious answer 
is that the choice is largely a matter of taste, and it depends on your aim. 
Sure, when you have to carry out simple computations, there's little point in 
resorting to a full-fledged computing environment, and probably spreadsheets 
are the best choice. However, the extra effort in learning a programming 
language pays off when you have to program a complex numerical method 
which goes beyond what is standard and readily available. Actually, there 
is no way to really learn numerical methods without some knowledge of a 
programming language, and in any case, even if you use a spreadsheet as the 
front end, it is quite likely that you have to write some code in Visual Basic 
or C++. 
Compiled languages such as Fortran and C++ are certainly the most effi- 
cient option, in terms of execution speed.9 If you have to write really lightning- 
fast code, this is the best choice. 
'Genetic algorithms and direct search methods are optimization methods which do not 
require computing derivatives of the objective function. This makes them very flexible for 
some types of optimization models, as we will see in chapters devoted to optimization. 
9A compiled language is based on the translation of source level code to machine level 
language. You need a compiler to do that; optimized compilers are able to obtain extremely 
fast code. An interpreter does not translate to machine level code, but to some internal form 
which is then executed. Usually an interpreter has some advantage in terms of debugging 
and flexibility, which is paid in terms of execution speed. 

12 
MOTIVATION 
MATLAB is an interpreted language, and even if it is quite efficient, there 
is some difference. However, the performance gap is being bridged by increas- 
ingly fast MATLAB versions. Furthermore, executable libraries can be gener- 
ated from MATLAB code by using the MATLAB compiler; these libraries can 
then be linked within the application just as any C++ code. But the most 
important advantage of MATLAB is that it is a very simple, yet powerful, 
programming language. Unlike C++, you may avoid bothering with issues 
such as memory allocation, variable declaration, etc. MATLAB is an excellent 
rapid prototyping tool: You may implement a quite complex algorithm with 
a very limited amount of lines. Simple code means less time to develop and 
less chances for programming bugs. Then, if it is really needed, you may go 
on by translating the prototyped code to, e.g., C++. This is obviously im- 
portant in a practical setting, but it is not really essential in a didactic book 
like the present one. When learning a numerical method, being distracted by 
too many programming details is certainly bad. 
MATLAB can be thought of as a suitable compromise between conflicting 
requirements. The increasing number of toolboxes and books using MATLAB 
is a good proof of that. Needless to say, this does not imply that MATLAB has 
no definite limitations. When one has to deal with large-scale optimization 
problems, it is necessary to resort to specialized packages such as CPLEX,1° 
against which MATLAB is unlikely to be competitive (it should be noted 
that the Optimization toolbox is aimed at general non-linear programming, 
whereas some optimization packages deal only with linear and quadratic pro- 
gramming). Furthermore, mixed-integer programming problems" cannot be 
solved, at present, by MATLAB.12 Even worse, when you have a large op- 
timization model, loading the data in a form suitable to a numerical library 
function is a difficult and error-prone task without the support of algebraic 
modeling languages such as AMPL.I3 This is one of the reasons why, in the 
chapters on optimization models, we will sometimes solve them using AMPL. 
This should not place any burden on the reader, since a free demo version can 
be downloaded from the AMPL web site. See appendix C for a quick tour of 
AMPL. 
By the same token, if one is interested in statistical computing applied to 
finance, it is quite likely than some of the many econometric packages are 
'OCPLEX is a registered trademark of ILOG. See http: //www. ilog.com. 
' Mixed-integer programming models are optimization models in which some decision vari- 
ables are restricted to integer, rather than real, values. They are dealt with in chapter 12. 
See also example 1.2 on page 15. 
lZWe should mention that the latest release of the Optimization Toolbox does include a 
solver for certain pure binary (0/1) linear programming. However, this is not suitable to 
large scale mixed-integer programming. 
13AMPL (A Mathematical Programming Language) was originally developed at Bell Lab- 
oratories. At present it is available in many versions through different sellers, including 
ILOG, under license from the copyright owner. See http: //www. ampl. corn. 

NEED FOR THEORY 
13 
better suited to the task. The point is that none of these offers the many 
functionalities of MATLAB within a single integrated environment. 
To summarize, we may argue that a product like MATLAB is the best single 
tool to lay down good foundations in numerical methods. Cheap MATLAB 
student editions are available, and its use in finance is spreading. So we believe 
that learning MATLAB is definitely an asset for students and practitioners in 
financial engineering. 
A last choice had to be made in writing the book: To which extent should 
toolboxes be used? On the one hand, using too many toolboxes would place 
some burden on the reader, who may not have access to all of them. On the 
other hand, using only the MATLAB core would probably limit what we can 
do, So, again, a compromise must be reached. Our choice has been to use 
a very limited subset of functions from the Statistical and Financial toolbox, 
which can be easily replicated. We will sometimes use functions from the 
Optimization toolbox, but the same results can be obtained by the free AMPL 
demo version. We will use neither advanced financial toolboxes nor the Partial 
Differential Equations Toolbox. This choice is somewhat contradictory: Why 
use the Optimization toolbox and not the PDEs one? The point is that there 
is a wide gap between a conceptual statement of optimization methods, and 
a robust working implementation. It is not the aim of this book to bridge 
that gap, so we will avoid a detailed treatment of most optimization methods, 
limiting ourselves to the principles behind them. On the contrary, simple 
finite difference methods are relatively easy to implement, and can be treated 
in detail. Finally, we should also note that typical computational finance 
courses do cover basic finite difference methods for solving PDEs, but not 
sophisticated optimization methods. 
1.3 
NEED FOR THEORY 
Now that we established that we are going to use MATLAB in the book, an- 
other question may arise: Why should we bother learning numerical methods, 
when they are already available in professionally crafted, ready-to-use code? 
Can we get rid of theory? Although, in most cases, there is no need for a deep 
knowledge of numerical analysis in order to use MATLAB, there are at least 
three reasons to gain a basic understanding of the theoretical background of 
numerical methods. 
1. Without a sound background, you cannot go on developing your own 
solutions when the available methods are not enough. 
2. Without a sound background, you cannot choose the most appropriate 
algorithm when alternatives are given. 
3. Without a sound background, you cannot use methods properly and, 
most important, you cannot understand what is going wrong when re- 
sults are not reasonable or you get weird error messages. 

14 
MOT/VAT/ON 
In particular, we need some understanding of fundamental issues like “con- 
ditioning of a numerical problem” and “stability of an algorithm.” These 
concepts are briefly discussed in chapter 3. Here we give some simple exam- 
ples of the trouble one can get into without a sound knowledge of the pitfalls 
of numerical computing. 
Example 1.1 Consider the following expression: 
9.8.1 + 8.1 
Everyone would agree that this is just a complicated way to write 10 x 8.1 = 
81. Let us try it on a computer, using MATLAB: 
>> 9 * 8.1 + 8.1 
ans = 
81.0000 
Everything seems right. Now, there is a built-in function in MATLAB, fix, 
which can be used to round a number to the integer nearest to zero.14 Note 
that fix does not round to the nearest integer: 
>> fix(4.1) 
4 
>> fix(4.9) 
4 
ans = 
ans = 
Let us try it on the expression above: 
>> fix(9*8.1 + 8.1) 
ans = 
80 
Now something seems quite wrong. Actually, the point is that the first result 
is not what it looks like. This may be seen by changing the visualization 
format of numbers and trying again: 
>> format long 
>> 9 * 8.1 + 8.1 
ans = 
80.99999999999999 
Actually, there was some warning, since MATLAB printed 81.0000 rather 
than 81, as it happens with 
14The reader is urged to explore the differences between f i x  and the related functions 
floor, c e i l ,  and round. 

NEED FOR THEORY 
15 
>> 10 * 8.1 
81 
ans = 
The problem is that an innocent-looking number like 8.1 is not represented 
exactly on a computer. This is because a computer works with a finite pre- 
cision arithmetic based on a binary representation, which can represent some 
numbers only approximately, even if their representation is finite in another 
system, like the decimal system we are used to. 
0 
In this example we see a large effect of a small error. This happens because 
of the non-linear character of the fix operator. The example may look a bit 
artificial, and one could be tempted to think that such difficulties do not arise 
in practice. In the next example we see the relevant effect of similar small 
errors in a concrete setting. 
Example 1.2 Let us consider a trivial model for capital budgeting deci- 
sions. We must allocate a given amount W of money to a set of N potential 
investments. For each investment opportunity, we know 
0 The initial capital outlay Ci, i = 1,. . . , N 
0 The revenue Ri that we will get from the investment (which we assume 
certain) 
We would like to select the subset of investments yielding the largest revenue, 
subject to a budget constraint. This looks like a portfolio optimization model, 
the key difference being that our decision must be ‘Lall-or-nothing.ll For each 
investment opportunity we may decide weather we take it or leave it, but we 
cannot buy a fractional share of it. In typical portfolio optimization models, 
assets are assumed infinitely divisible, which may often be a reasonable ap- 
proximation, e.g., for stocks, but not in this case. It may be helpful to think 
of our investments as projects that can be started or not. 
The decision variables must reflect the logical nature of our decision. This 
is obtained by restricting the decision variables as follows: 
1 if we invest in project i 
{ 0 otherwise. 
xa = 
Now it is easy to build an optimization model: 
N 
i=l 
N 

16 
MOTlVATlON 
This model is grossly simplified, but it is a first example of an integer program- 
ming model. It is also well known as the knapsack problem, as each investment 
may be interpreted as an object of given value Ri and volume Ci, and we want 
to determine the maximum value subset of objects that may fit the knapsack 
capacity W .  A model like this looks deceptively simple. However, it cannot be 
solved by ordinary optimization methods for continuous optimization models. 
One could think of simply enumerating all of the feasible solutions, which are 
a finite set, in order to spot the best one. Unfortunately, this is not feasible 
in general, as the number of feasible solutions may be very large, even though 
finite. To see this, notice that there are N variables which can take two values; 
hence, there are 2N possible variable assignments. Many of them would be 
ruled out by the budget constraints, but we see that the computational effort 
of complete enumeration grows exponentially with the size of the problem. A 
possible solution approach would be ordering the items in decreasing order of 
their return Ri/Ci and selecting them until the budget allows. This would 
work with divisible assets, but it does not guarantee the optimal solution in 
the discrete case. As a counterexample, consider the following problem: 
max 
loxl + 7~ + 25x3 + 24x4 
s.t. 
221 + 1 2 2  + 6x3 + 524 5 7 
xi E (0,l). 
The returns are, respectively, 5.00,7.00,4.17,4.80. Hence, according to this 
logic we would select investment 2 first, then investment 1, and we would 
stop there, with a revenue 17, because no other investment fits the residual 
budget. This is a really bad solution, leaving much budget unused. There are 
two solutions which exploit the whole budget: [I, 0, 0,1], with total revenue 
34, and [0,1,1,0], with total revenue 32. In this trivial case it is easy to 
see that the first one is optimal. Unfortunately, in general, a problem like 
this can only be tackled by non-convex optimization methods, such as branch 
and bound,15 described in chapter 12; in that chapter we will see that logical 
decision variables may be useful in capturing various types of constraints in 
realistic portfolio management models. 
The main limitation of the model above is that uncertainty is not considered 
at all. Another issue is that in general there might be some interaction among 
different projects. For instance, it could be the case that a given project, say 
project Po, may be started only if projects PI, P2,. . . , PN are started as well. 
This logical constraint is easily modeled using the binary decision variables 
we have just introduced. One possibility is to express the constraint in the 
15This problem may be also solved by some form of dynamic programming; see [7, pp. 
72-74]. In chapter 10 we only consider dynamic programming for certain stochastic op- 
timization problems, but the principle is much more general and powerful and it. can be 
applied to some combinatorial optimization problems as well. 

NEED FOR THEORY 
17 
following form: 
If we start all the N required activities, the right-hand side of this inequality 
is simply N / N  = 1, so that we may start Po, since the constraint boils down 
to the redundant bound 20 5 1. If some required project is missing, the 
constraint amounts to something like 2 0  5 a < 1, which, together with the 
binary requirement 20 E (0, l}, enforces 20 = 0. In principle, the idea is 
fine, but does it really work on a computer? Well, in many cases it does, but 
consider what happens with N = 3. Project Po will never be selected. In 
fact, in this case, you should read the constraint above as 
1 
1 
1 
3 
3 
3 
50 5 - 2 1  + -22 + -23, 
but unfortunately, even if all the xi variables are set to 1, due to the finite 
precision of the computer we have something like 
2 0  5 0.3333333 + 0.3333333 + 0.3333333 = 0.9999999 < 1, 
where the number of decimals depends on the numerical precision of the ma- 
chine and on the software involved. Actually, sophisticated optimization soft- 
ware for integer programming does not incur this trouble, since some integral- 
ity tolerance is introduced, and 0.9999999 is considered just like 1. Similar 
considerations apply to any high-quality numerical software, such as MAT- 
LAB, but the result can be somewhat unpredictable, as the following snapshot 
shows: 
>> fix(l/3 + 1/3 + 1/31 
ans = 
1 
>> fix(l/7 + 1/7 + 1/7 + 1/7 + 1/7 
ans = 
0 
Furthermore, if the optimization problem 
+ 1/7 + 1/71 
is first written to a text file, which 
is then loaded by an optimization solver, it may be the case that the number 
of digits is too small.16 So it is better to avoid the trouble with division in 
the first place, by rewriting the constraint as 
“For instance, if you solve the model within a modeling system like AMPL, calling a solver 
like CPLEX, there is no trouble. But if you write an MPS file and load the file with 
CPLEX, the result will not be correct. MPS files are text files representing optimization 
models according to standard rules; they are read by many optimization software packages. 

18 
MOTIVATION 
or, even better, in the disaggregated form 
20 5 xi, 
i = 1,. . . , N .  
Why this is the preferred form is counterintuitive: after all, the disaggregated 
form entails more constraints, and one would think that the less constraints 
we have, the easier an optimization model is to solve. This need not be 
true in computational optimization, and it also depends on how mixed-integer 
programming problems are solved by branch and bound methods. More on 
this in chapter 12. 
0 
Numerical errors may affect the precision in representing numbers, but this 
issue is not much trouble in itself; after all, a derivative price will not be quoted 
in millionths of a dollar. But how about the propagation of errors within a 
numerical algorithm? If you have a non-linear operator like f i x ,  a small 
error gets immediately amplified. The same may happen when you execute a 
long sequence of operations, such that small errors cumulate, growing without 
bound. The effect may well be a huge negative price for an option, as we will 
see in chapter 9. In the next example we consider a well-known example, 
linked to the solution of a system of linear equations. 
Example 1.3 Let us consider a system of linear equations: 
Hx = b, 
for some right-hand side vector b, where H is a peculiar matrix known as the 
Hilbert matrix 
H =  
1 
1 
3 
n 
1 
1 
1 
1 
1 ; - 
... 
- 
I I 
- 
... - 
2
3
 4 
n+l 
I 
I 
- 
... - 
3
4
 5 
n+2 
.
.
 
1
1
 1 
1 
n 
n + l  
n+2 
2n-1 
- - - . . . - 
The Hilbert matrix may look a bit artificial, but it may arise in certain function 
approximation problems (see example 3.20 on page 190). 
MATLAB provides us with a function, hilb, to build a Hilbert matrix 
directly. Now, let us try solving the system for n = 20; we cheat a little here, 
since we assume that the solution is known, and we build the corresponding 
right-hand side b; then we check if that solution is obtained by solving the 
system. Let the solution be 

NEED FOR THEORY 
19 
where we use ’ to denote vector (or matrix) transposition. Using MATLAB, 
we obtain something like17 
>> H = hilb(20); 
>> b = H+x; 
>> H\b 
Warning: Matrix is close to singular or badly scaled. 
Results may be inaccurate. RCOND = 1.995254e-019 
>> x = (1:20)’; 
ans = 
1.0000 
2.0000 
3.0018 
3.9392 
5.8903 
-1.1035 
41.0915 
-94.0458 
196.5770 
82.1903 
12.1684 
140.5377 
-265.11 17 
309.7053 
-328.9234 
485.5373 
-401.3571 
215.1260 
-17.0274 
-181.1961 
We see that the result doesn’t look quite as it should. 
0 
In the last example we see the typical effect of propagation of numerical 
errors, giving rise to numerical instability. In fact, this is detected by MAT- 
LAB, which issues a warning message. However, we need some theoretical 
background in order to get the meaning of this warning. One could think 
that similar difficulties arise whenever a matrix is close to singular. Clearly, if 
you try doing something like x = A-’b in order to solve the system Ax = b, 
17The actual result may depend on the MATLAB version and the hardware you use. This 
is not the case for usual problems, but it does happen when numerical instability issues 
arise. 

20 
MOTIVATION 
you are likely to be in trouble if A is close to singular. This may be true, but 
it is somewhat misleading: 
1. You may have difficulties even when the matrix is not singular at all 
(see example 3.8 on page 151). We need to study issues such as problem 
conditioning in order to understand what really happens. 
2. In practice, there is no need to invert a matrix to solve a system of linear 
equations, as this would be much more work than necessary. Compu- 
tational mathematics may be quite different from “pencil-and-paper” 
mathematics. 
At this point, the reader will hopefully be convinced that some background 
in numerical analysis is needed, if we are to solve problems in real life. 
For further reading 
In the literature 
0 Another MATLAB-based textbook is [6]. It is more aimed at appli- 
cations in Economics, but it offers an interesting Computational Eco- 
nomics toolbox which may be downloaded for free. 
0 Readers interested in details on the development and release of Microsoft 
Windows components for financial applications may have a look at [4]. 
0 Financial modeling within Microsoft Excel is described, e.g., in [2]. 
0 C++ programmers will find [l] and [3] very useful. 
0 Many journals devoted to quantitative finance publish papers on com- 
putational issues. We should mention at least 
- Journal of Computational Finance 
http://www.thejournalofcomputationalfinance.com 
- Journal of Derivatives 
http://www.iijod.com 
- Quantitative Finance 
http://www.tandf.co.uk 
On the Web 
0 To consult a full and updated listing of MATLAB toolboxes, see 
http://www.mathworks.com. 
0 For more information on CPLEX and related software, see 

REFERENCES 
21 
http://www.ilog.corn. 
0 The web page for AMPL is http : //www . ampl. corn, where you will find 
a list of vendors and compatible solvers and a free student version for 
download. 
0 Two web sites we should also mention are 
http : //www . gams .corn, where an alternative product to AMPL is de- 
scribed, which has found fairly widespread use among economists, 
and http : //www . nag. corn where a well-known numerical analysis li- 
brary is described, for use with programming languages like Fortran 
and C++. 
REFERENCES 
1. D.J. Duffy. Financial Instrument Pricing Using C++. Wiley, New York, 
2004. 
2. M. Jackson and M. Staunton. Advanced Modelling in Finance using Excel 
and VBA. Wiley, New York, 2001. 
3. M.S. Joshi. C++ Design Patterns and Derivatives Pricing. Cambridge 
University Press, Cambridge, 2004. 
4. G. Levy. Computational Finance. Numerical Methods for Pricing Finan- 
cial Instruments. Elsevier Butterworth-Heinemann, Oxford, 2004. 
5. R.C. Merton. Continuous- Time Finance. Blackwell Publishers, Malden, 
MA, 1990. 
6. M.J. Miranda and P.L. Fackler. Applied Computational Economics and 
Finance. MIT Press, Cambridge, MA, 2002. 
7. L.A. Wolsey. Integer Programming. Wiley, New York, 1998. 

This Page Intentionally Left Blank

2 
Financial Theory 
This chapter is a reasonably brief introduction to some basic problems in 
finance. It is mostly aimed at readers with a scientific or engineering back- 
ground, but with little previous exposure (if any) to the theory of finance. 
The complementary set of readers, i.e., those with a background in finance 
may wish to have a cursory look at the material, or maybe to refer back to 
this chapter for a quick refresher when needed. 
The treatment here is purely instrumental to motivating and stating cer- 
tain problems to which we may apply numerical methods. So, it is certainly 
not meant to be a substitute for a good book on finance (see the references at 
the end of the chapter), and it is not aimed at giving a complete overview of 
financial theory. Furthermore, many concepts such as bond portfolio immu- 
nization, mean-variance efficiency, and Value at Risk have many well-known 
limitations and have been the subject of quite a bit of controversy. We will 
point out the limitations of each approach, and we do not suggest that they 
should be used as they are stated; we use them just to pave the way for further 
developments. 
Actually, there 
is a third one, information, which is important in advanced models which 
are beyond the scope of this book. Time is important since, under normal 
economic conditions, one dollar now is worth more than one dollar tomorrow. 
Even if we do not consider inflation, it is reasonable to expect that if we have 
one dollar now and we do not need it for immediate consumption, we could go 
to a bank, deposit our dollar, and recover a larger sum later on. If, after one 
year, we get 1 + r dollars, we say that r is the annual interest rate. We may 
see it the other way around: if we borrow one dollar now, in the future we 
23 
The main themes in finance are time and uncertainty. 

24 
FINANCIAL THEORY 
will have to give back some more. In fact, one function of financial markets 
is just to shift consumption over time by borrowing or lending money. In 
practice, the rates for borrowing and lending are not really the same, as there 
is a bid-ask spread,’ but for our instrumental purposes we will mostly neglect 
such issues. 
If we are investing money over a relatively short time period, we could 
assume that we know the interest rate that will be applied for that period. 
This may not be the case for longer periods, as interest rates are subject to 
uncertainty. If the interest rate is periodically reset according to prevailing 
conditions, then the investment is subject to uncertainty which may be con- 
sidered as a reinvestment risk. Even if a given nominal rate is agreed to hold 
for the entire period, the real rate will be subject to inflation. An even larger 
uncertainty is typically associated to investing in stocks, which are often sub- 
ject to significant price volatility. Our first task is to introduce different ways 
to model uncertainty (section 2.1). There is no “best” way to model uncer- 
tainty, as this may depend on our aim, but there is no doubt that uncertainty 
is pervasive in finance. 
Uncertainty is strongly linked to risk. Any investor has some implicit risk 
tolerance. For instance, common wisdom dictates that older investors should 
invest in relatively safe assets, whereas younger ones may afford the risk of 
investing in stock. Apart from individual investors, there are institutional 
investors, such as pension funds, or even non-financial firms which use financial 
assets to modify their exposure to some risk factors. In fact, another function 
of financial markets is to transfer risk among market participants, who can 
be grossly classified as speculators or hedgers. Speculators have some view on 
how prices will move in the future, and they perceive risk as an opportunity 
to place bets. Speculation has a somewhat negative connotation, but without 
speculators, markets would not exist in their present form. The other side 
of the coin is the set of hedgers, who use certain types of assets as a sort of 
insurance in order to avoid or reduce uncertainty. In some sense, hedgers sell 
volatility to speculators. 
In modern financial markets, there is huge variety of assets in which we 
may invest our money. The main assets we will deal with may be classified 
as bonds, stocks, and derivatives. We will introduce these assets in section 
2.2. There, we also introduce the three main problems we are concerned with: 
asset pricing, portfolio optimization, and risk management. We will also see 
that these basic problems are strictly related. 
After this general introduction, we deal with simple fixed-income instru- 
ments (bonds) in section 2.3, where we also consider sensitivity measures 
related to interest-rate risk, such as duration and convexity. Section 2.4 is 
‘The bid price how much a dealer bids (is willing to pay) for an asset; hence, from the point 
of view of an investor, it is the price at which she may sell. The ask price is the price at 
which the investor may buy, i.e., the price asked for by a dealer. 

MODELING UNCERTAINTY 
25 
dedicated to stock portfolio management. The main concepts we illustrate 
there are utility theory for decision making under uncertainty, the theory of 
mean-variance efficient portfolios, and risk measures such as Value at Risk. To 
deal with derivative pricing, we need first to lay some foundations in modeling 
by continuous-time stochastic processes: Stochastic integrals and stochastic 
differential equations are introduced in section 2.5, together with the funda- 
mental Ito’s lemma. Then we proceed to illustrate the basics of arbitrage-free 
pricing in section 2.6, where the celebrated Black-Scholes formula for pricing 
European-style vanilla options is presented, along with basic issues in pricing 
American-style options. We expand the treatment of options in section 2.7, 
where we outline a few types of exotic options which will be used in later 
chapters to illustrate different numerical methods for pricing. Finally, in sec- 
tion 2.8 we give a very brief introduction to interest rate derivatives and the 
related problems. 
In the course of the exposition we will use short MATLAB snapshots in 
order to illustrate the material with examples and to make it immediately 
useful. Sometimes, we will use functions from the Financial toolbox. The 
reader without access to this toolbox should not worry: these examples are 
just used for concreteness, but most of the book is just based on the MATLAB 
core. 
A final remark is in order. A large part of modern theory of pricing deriva- 
tives is based on the concept of martingale, i.e., a specific type of stochastic 
process. However, the reader will not find any mention of martingale measures 
and the like in what follows. Given the increasingly large number of excel- 
lent texts covering martingale pricing, we have decided to omit such concepts, 
which are not strictly necessary to introduce numerical methods. The main 
consequence of this choice is the lack of coverage of interest-rate derivatives, 
which cannot be dealt with adequately without solid foundations; but this 
would require much more space than we can afford. 
2.1 
MODELING UNCERTAINTY 
Before considering “modeling,” we must understand what “uncertainty” is. 
The familiar tools of probability and statistics are what we need to cope with 
the simplest kind of uncertainty. We assume that a variable, say the price 
of a stock or a commodity, can be modeled as a random variable, whose 
probability distribution is known, possibly inferred from available data; the 
probability distribution encodes the knowledge we have (or think we have) 
about uncertainty. This may already look complicated, but it is often far 
worse in practice. To begin with, we will only consider purely exogenous 
uncertainty. This means that our actions do not influence the distribution of 
the relevant random variables. This is true if we are small investors or the 
asset is very liquid and in large supply. In thin markets, however, buying and 
selling an asset may have a significant impact on its price, and uncertainty 

26 
FINANCIAL THEORY 
Fig. 2.1 A binoniial model for uncertainty. 
is partially endogenous. For instance, a trade executed by a large pension 
fund inay have a significant impact on markets; sometimes, to avoid adverse 
effects, orders are split in different time steps. Another issue is related to 
“subjectiveii rather than “objective” uncertainty. We will implicitly assume 
an objective description of uncertainty, but sometimes an investor has some 
very specific views, leading to a subjective assessment of uncertainty. The 
subjective view niay be updated whenever we get new information. This 
is typical of the Bayesian approach to statistics; which has been applied to 
portfolio management too. Again, given our instrumental point of view, we 
will avoid such issues. It is important to understand that if we use statistics to 
identify a probability distribution from past data, and we use that distribution 
for the future, we are implicitly assuming that, in some sense, history will 
repeat itself. 
To lie specific, let us consider possible ways of modeling uncertainty in the 
price of an asset. The simplest model of uncertainty is the binomial model. 
We know the current price S,), at time t = 0, and we assume that the price 
S1, at, some future time instant t = 1; can take only two values, S;L and Si‘; 
with probahility p”’ and p d ,  respectively (see figure 2.1). A common choice 
is to represent uncertainty by a multiplicative shock, i.e., S;l = uS0 and 
Sf = dS;, where the letters u and d suggest “up” and LLdown,’’ 
respectively 
(hence, d < u). Apparently, this model is very crude, but it is the building 
block of very useful models. 
A more refined model can be built by allowing for more future states. We 
may consider a sort of tree, like the one depicted in figure 2.2. It is a two-stage 
tree. in the sense that it represents the world now by the single node on the 
left, of the figure, and possible states of the world at one time instant in the 
fubure; this st,ructiirc is sometimes referred to as a fun, and it may be used 
to define a set, of discrete scenarios. In this case the random variable S1 may 
take values Si“), k = 1, . . . , in, with probabilities ~(‘1). An obvious consistency 
condition is 
711 Zp(C 
= 1. , 
o < p ( ’ ) ) < l  
k = 1 ,  ..., m. 
!i=l 
The hinomial model or the fan of scenarios are discrete-state models, rep- 
resenting uncertainty in a relevant state variable by a discrete probability 
distribution. Tlie state could be the level of an interest rate, or any underly- 

MODELING UNCERTAINTY 
27 
Fig. 2.2 A two-stiige tree model 
s:"') 
for uncertainty. 
Fig. 2.3 A rnultistage scenario tree 
ing state variable influencing the price of assets.' These models are also the 
siinplest, discrete-time models, as only two time instants are considered. This 
inay bc iritercstirig if wc w e  following a, buy and hold strategy, whcret)y we 
t,ra.tlc some iissets now, and then we just wait for the outcome at sonie time in 
t,hc f1itur.c. If tlic portfolio will be later rebalanced with some given frequency, 
we might tie interested in a niultiperiod model. 
A discrete-state, discrete-time, multiperiod model can be depicted as the 
scmario t,rw in figure 2.3. This is sometimes called a bushy t,ree. In a bushy 
tree, the nuriiber of nodes following a parent node is called brunching fuctor. 
The larger the branching factor, the more accurate the representation of un- 
certuiiity. However, with large branching factors, the number of nodes tends 
to grow very quickly. Scenario generation is the art of building a suitable tree 
'Strictly speaking. a state variable has the property that knowledge of its value at a time 
iiistaiit is all we need to characterize future evolution. We could have situations in which 
the whole history of a variable is needed to this purpose. Since this proper use of the term 
is only relevalit for a few topics in the hook, we will use the term in the loose sense. 

28 
FlNANClAL THEORY 
fig. 2.4 A recombining lattice. 
with the minimum number of nodes; note also that there is 110 need that the 
branching fact,or is constant over time, or across nodes. One may use niorc 
branches now, and less branches in the future, if it is more important to rep- 
resent immediate uncertainty. This is important in stochastic programming 
niodels (chapter 11). Another point is that the time step involved in a mul- 
tiperiocl model need not be homogeneous. Usually, in a discrete-time model 
we discretize a time horizon of length T in intervals of length 6t, such that 
T = A 1  . 6t. When we refer to time instant t = k; what we really mean is 
t = k . 6t. However, the time step may change; in such a case, the first t,irne 
period is short, and tinie step increases in later periods. 
Sometimes, t,o keep computational effort limited, we prefer using a recorn.- 
baning lattice. A recombining binomial lattice is illustrated in figure 2.4. This 
is obtained if we generalize the binomial model with multiplicative shocks. 
Since udSo = duSo, we see that an up-jump followed by a down-jump is 
the same as a down-jump followed by an up-jump. In the figure, node S;" 
could also be denoted as S$'. In the special case 2~ = l/d, we also have, 
e.g.; So = S;d and S;l = S:(ud. The number of nodes grows linearly with the 
niunher of periods: We start with one node at t = 0, then we have two at 
time t = 1; three at time t = 2, and T + 1 nodes at time T .  In a binary tree 
we have an exponential growth, as we have 2T nodes at time T .  Note that 
we are assuming that the multiplicative shocks are always the same, which 
makes sense if the process is stationary and time step is constant. Lattices 
may take many different forms, such as trinomial lattices, where each node 
has three successors. Recombining lattices are very convenient from a compu- 
tational point of view (see chapter 7). However, they are not always suitable, 
especially when there are many stochastic factors, calling for larger branching 
factors and making recoinhination more difficult to achieve. 
Sonietiines it is convenient to model Uncertainty using a continuous distri- 
liution, siicli as the normal or lognormal distribution. If we think of prices, 
a continuous distribution is certainly an idealization, since no price is quoted 
with too many decimal digits. In fact, stock prices are quoted in the USA in 
fractions of a point, which may be one-eighth or one-sixteenth of a dollar. For 

MODELING UNCERTAINTY 
29 
1- 0 
0.2 
0.4 
0.6 
0.8 
1 
time t 
Fig. 2.5 Sample path of a Wiener process. 
instance, the price of a stock could be $20i or $20;, but not $20.19. A similar 
consideration applies to interest rates. Nevertheless, using a continuous-state 
model may be convenient, if it results in simple modeling of uncertainty and, 
maybe, in analytical formulas. 
By the same token, we may also resort to continuous-time models, which 
may be thought of as the limit of a discrete-time model when the time step 
tends to zero. In the deterministic case, a standard continuous-time model is 
a differential equation, like 
-- 
dB(t) - rB(t) 
dt 
with initial condition B(0) = Bo. The solution of this equation is B ( t )  = 
Boert; in section 2.3.1 we will see that this is the equation of a wealth, ini- 
tially amounting to Bo, invested at a rate T ,  with continuous-time compound- 
ing of interest. Again, this could be just a convenient approximation. To 
model uncertainty, differential equations must be extended by introducing a 
random element, typically represented by some convenient class of stochastic 
processes. Unlike discrete-time models, we deal in this case with continuous- 
time stochastic processes (see appendix B). The usual building block is the 
Wiener process W(t), 
which is defined later, and is characterized by jagged 
sample paths like the one depicted in figure 2.5. This process may look funda- 
mentally different from a binomial lattice, but it can be shown that the Wiener 
process is the continuous-time limit of a certain random walk described by a 
binomial lattice. By putting Wiener processes and differential equation to- 
gether in some sensible way, we get stochastic differential equations, which are 
a rather thorny object to deal with, but are a fundamental tool in financial 
engineering. We will describe stochastic differential equations in section 2.5. 

30 
FlNANClAL THEORY 
2.2 
BASIC FINANCIAL ASSETS AND RELATED ISSUES 
There is a large number of securities in which an investor may be interested. 
Many of them are standardized, publicly quoted, and traded on exchanges. 
Some are engineered for a specific need of an investor, or firm, and are traded 
over the counter (OTC); OTC securities are usually less liquid than standard- 
ized assets. Despite this virtually infinite variety, we may start by classifying 
the fundamental securities as 
bonds 
stocks 
derivatives 
2.2.1 
Bonds 
Bonds are one of the instruments that firms and public administrations may 
use to fund their activities; they are debt instruments which, unlike stocks, 
do not imply any ownership of a firm on the part of the buyer. Basically, 
the buyer of a bond lends some money to the issuer, over some time span 
ending at bond maturity. At maturity the issuer will pay the bond owner an 
amount of money corresponding to the face value, also called the par value, 
of the bond. This could be, e.g., an amount like $100 or $1000. In addition, 
periodic payments may be made, called coupons for historical  reason^.^ In 
the simplest bonds, coupons are fixed and expressed as a percentage of face 
value; coupons are usually paid annually or semi-annually. For instance, if the 
bond has $100 face value, and the coupon rate is 6%, then the bond owner 
will receive $6 each year, up to and including maturity, when she well receive 
$106. If coupons are paid semi-annually, the bond owner will receive $3 every 
six months, up to and including maturity. 
There is another class of bonds, which just promise the payment of face 
value at maturity. They are called zero-coupon bonds, and are typically char- 
acterized by shorter maturities. We will see that zero-coupon bonds are fun- 
damental in bond pricing. Sometimes, long-term zero-coupon bonds are built 
by stripping coupons from a long-term bond and selling them separately. 
The basic type of fixed-coupon bond explains why bonds are usually clas- 
sified as fixed-income securities. Actually, coupons may depend on some un- 
derlying variable, but the term “fixed-income” is used for such securities as 
well. Generally, fixed-income securities are assets whose price depends on the 
level of interest rates. 
It is also important to note that bonds are not necessarily purchased at a 
price corresponding to face value. This may be the case when bond are first 
3Bonds were physical pieces of paper, and to get the periodic payment the bond owner had 
to detach a coupon from the document. 

BASIC FINANCIAL ASSETS AND RELATED ISSUES 
31 
issued, and the coupon rate is chosen in order to reflect current interest rates. 
Since there is a well-developed secondary market for bonds, there is no need 
to buy a bond right when it is issued, nor to keep it until maturity. If a bond 
is traded after issue date, we must be able to determine a fair price. This will 
be the subject of section 2.3.2. Bond prices are quoted as a percentage of the 
face value, so the actual face value is not so relevant. Assume the face value 
is 100. If the bond is traded at price larger than 100, we say that it trades 
above par; if the price is smaller, it trades below par; otherwise it trades at 
par. 
If the 
coupon rate is not fixed, but it depends on some random quantity, analyzing a 
bond may be difficult. Even if the coupon rate is fixed, bond prices may differ 
depending on the probability of default. Default occurs if the bond issuer 
is not able to honor his debt and stops paying coupons, or he repays just a 
fraction of face value. There are different types of default, which represent a 
risk factor for the investor. This factor is called credit risk. Bonds issued by 
some governments may be considered risk-free, but corporate bonds cannot; 
the role of rating agencies is precisely to analyze the financial situation of 
firms in order to assess how risky their bonds are. Bonds affected by credit 
risk must sell at lower prices, or promise higher coupon rates. It should also 
be noted that bonds may be classified in legal terms which are relevant when 
the firms defaults. We will not consider default issues and credit risk in this 
book. Furthermore, some bonds have embedded options which complicate the 
analysis. For instance, a callable bond may be redeemed by the issuer before 
maturity at a certain price; again, since the issuer may redeem the bond when 
she finds this advantageous, this must be somehow reflected in the bond price 
and/or the coupon rate. In this case, the investor is exposed to reinvestment 
risk, as it is quite likely that she will be forced to reinvest the proceeds from 
early bond reimbursement in a situation of unfavorable interest rates. 
Actually, there are many complicating factors in bond pricing. 
2.2.2 
Stocks 
Unlike bonds, stocks entitle the owner to a share of the issuing firm. This 
raises a potentially troublesome legal issue. If you are a stock owner of a firm, 
and the firm gets involved in a lawsuit, whereby it is liable to pay for some 
significant damage its products have caused, what is your position? Luckily, 
stocks are limited liability assets; in practice, this means that the worst that 
may happen is that the stock price goes to zero and you lose all of your 
investment. 
Another difference between stocks and bonds is that the formers do not 
have a predefined maturity (although the firm can well go out of business). 
They also entitle the owner to some stream of payments under the form of 
dividends. Unlike fixed bond coupons, dividends are by their very nature 
stochastic. They depend on how well the firm is faring, and on the dividend 
policy which is followed by the firm, which may distribute or reinvest its 

32 
FINANCIAL THEORY 
profit. The dividend policy, and the decisions of financing by equity (issuing 
stocks) or debt (issuing bonds) pertain to a body of knowledge called corporate 
finance. 
If you buy a stock share at a price SO, and then you sell it at a price S1, 
you may have a loss or a gain. If you also receive a dividend D, total return 
is 
Si + D  
s o  
SI + D - SO 
and the rate of return is 
SO 
Strictly speaking, we should also consider the timing of dividend payments in 
order to account for the time value of money, but let us leave this issue aside 
for now by assuming that dividends are paid exactly when you sell the stock. 
Since stocks are limited liability assets, the worst-case rate of return is -1. 
This means that whenever we use a normal distribution to model uncertainty 
in stock returns, we are committing an error; however, the approximation, 
per se, could be an acceptable one if the probability of an unfeasible return is 
negligible.4 
In this book we will not consider pricing issues for stocks. This means that 
stock prices will be modeled by some stochastic process (see section 2.5) or 
by some probability distribution, but we will take these as exogenously given. 
There are “rational” models aimed at suggesting a correct stock value by 
analyzing the fundamentals of a firm, but they are based on rather uncertain 
data, and prices may be quite irrational. Nevertheless, such models are useful 
when trying to assess if some stock is under- or over-priced with respect to 
other assets, and this is certainly relevant in portfolio management. However, 
since this is not a matter necessarily dealt with by sophisticated numerical 
methods, and it calls for integration with qualitative insights, we will leave it 
aside. 
In principle, one would think that an investor buys a stock if she thinks 
that its price will increase. Actually, with certain limitations, an investor can 
exploit a strategy called short-selling if she thinks the stock price will sink. 
Example 2.1 (Short-selling) Suppose a stock is currently selling for $20, 
and you think that in the near future it will sell for a lower price. In such 
a case, you may borrow the stock from someone who owns it, and sell it 
immediately on the market. After a while, you will have to give the stock 
back to the owner, but if you were right and the price went down to $18, you 
might buy the stock for this price and close your position. In this case, your 
return would be (-18 + 20)/20 = 10%. If the stock pays dividend during the 
4Another implicit assumption, when using a normal distribution to model returns, is that 
these are symmetric, which may not really be the case. 

BASIC FINANCIAL ASSETS AND RELATED ISSUES 
33 
time period over which the stock is lent, dividends must also be paid to the 
stock lender. 
Short-selling is not this easy, as there are several rules constraining it to 
avoid excessive speculation. Furthermore, it is restricted to certain types of 
traders; some institutional investors such as pension funds cannot use short- 
selling because of its speculative nature. Short-selling is very risky: If you are 
wrong and the price goes up, you may be forced to give the stock back at the 
worst possible time (this is called short-squeezing). 
0 
2.2.3 
Derivatives 
Derivatives are a broad family of financial contracts, owing their name to the 
dependency of their payoff on the value of some underlying variable, which 
may be a stock price, a set of stock prices, an interest rate, an index, or a 
generic non-financial asset. Suppose that the value of the underlying asset, 
say a stock which does not pay dividends, is modeled by a stochastic process 
S(t), depending on time t. 
The most common derivatives are forward/future contracts and options. 
A forward contract binds two parties to, respectively, buy and sell a certain 
asset, in a certain quantity, at a certain date T ,  and at a fixed forward price F .  
The party agreeing to buy is said to hold the long position, whereas the seller 
holds the short position. By entering a forward contract you basically lock in a 
fixed price for the underlying asset. You may have two quite different reasons 
for doing that. You might wish to eliminate, or reduce, risk; in fact, by locking 
the price for an asset you have to buy or sell, you eliminate the effect of price 
uncertainty. This does not mean that the final outcome will necessarily be 
more favorable. If you hold the long position in a forward contract specifying 
a price F ,  and the price of the asset when the delivery takes place turns out 
to be S(T) < F ,  in a sense you have lost an amount F - S(T); if, on the 
contrary, S(T) > F ,  you have gained a corresponding amount. The point is 
that if you really need to buy or sell that asset, it may be wise to lock in a 
certain price rather than taking chances. This type of policy is called hedging. 
Hedging may not be this easy, as you may have difficulties in finding a forward 
contract for the underlying asset you are interested in, in which case you could 
settle for a somewhat correlated asset; furthermore, delivery date might differ 
from the one you would like; finally, one could also decide for a partial hedge, 
depending on risk attitude. However, you could also be a speculator with a 
very precise idea of where the price S(T) is going to be, and you may enter 
a forward contract as a bet. The payoff of a forward contract is depicted in 
figure 2.6(a) for a long position, in which case it is S(T) - F (it is F - S(T) 
for the short position). This payoff depends on the random price S(T), and 
the forward contract is the simplest example of a derivative. Since the payoff 
is random, we need some way to value a forward contract. We will do this in 
section 2.6. Here we just note that there is no initial payment with forward 
contracts; at time t = 0 the forward price F is determined in such a way that 

34 
FlNANClAL THEORY 
K 
Fig 2 6 Payoff tliagraiiis for t h c s  long position in it forward c:orit,rac.t (a), h call optiori 
(1)). a i d  n. put optioii (c). 
t,he initial value of the contract is zero to both parties. However, at a later 
time, the value of the contract will not be zero in general. 
Derivatives may he privat,e contracts issued by two parties for possibly 
very peculiar and specific reasons. Alternatively, they may be traded actively 
on exchanges and quoted on newspapers. In this case, some standardization 
and regulation is needed to make sure that the derivatives are sufficiently 
liquid to trade. This is not really the case for forwards, where there is some 
possibility of default on the part on the part losing money; for this reason 
future contracts have been devised. A future contract is similar to a forward 
contract; the main difference is that there is an intermediation process such 
that the detailed working is different. Rather than collecting the payoff at 
maturity, there is a. daily transfer of cash between the two parties, depending 
on the movement of the underlying asset price. This mechanism is a protection 
for traders and makes pricing of futures more difficult than forwards, and we 
refer the reader to references for cletails on this. It can be shown that prices 
for futures and forwards are the saiiie if interest rates are deterministic. From 
a practical point of view, standardized future contracts make trading easier, 
but hedging more difficult. It may be impossible to find t,he exact cont,ract 
you need in terms of time of delivery or underlying asset; in such a case, 
hedging will eliminate only part of the risk. Nevertheless, futures are a very 
liquid tool: and it is also interesting to note that, by taking a position with 

BASIC FINANCIAL ASSETS AND RELATED ISSUES 
35 
futures, one may also emulate short-selling on assets for which this would be 
otherwise impossible. 
A common feature of forward and future contracts is that the two parties 
are compelled to buy and sell the asset at delivery (unless you sell the contract 
to someone else before maturity, as is usually the case with futures). With an 
option, you get the right, but not the obligation, to buy or sell a certain asset 
for a specified price. The two simplest option contracts are the European 
style call and put options. When you buy a call option, you get the right 
to buy the underlying asset for a price K ,  called the exercise price (or strike 
price), at a certain date T ,  called expiration date or maturity. If at maturity 
the actual price S(T) of the underlying asset is larger than the exercise price 
K ,  you would exercise the option and buy the stock, since you may sell the 
stock immediately and gain S(T) - K .  If the contrary holds, you would not 
exercise the option, which expires worthless. Thus, the payoff of this option 
is 
max{S(T) - K ,  0) 
and is depicted in figure 2.6(b). If at time t we have S(t) > K ,  we say that 
the call option is in-the-money; this means that we would get an immediate 
profit by exercising the option. If S(t) < K ,  the call option is said to be 
out-of-the-money. If S(t) = K ,  the option is said to be a t - t h e - m ~ n e y . ~  
With 
a put option, you have the right to sell the stock. In this case, you would 
exercise the option only if the exercise price is larger than the actual price. 
So the payoff is 
max{K - S(T), 
O}. 
The payoff diagram for a vanilla European put option is depicted in figure 
2.6. (c). 
With a European option you may exercise your right only at maturity; an 
American option may be exercised whenever you wish within a prescribed 
time. European or American call and put options on a single underlying asset 
are called vanilla options, owing their name to their simplicity. A Bermudan 
option is halfway between an American and a European option: It may be 
exercised at a set of prescribed dates within the horizon. Asian options have 
a payoff depending on the average price of a stock (or some other underlying 
variable); thus they depend on a set of stock prices. Indeed, quite complex 
exotic options are actually designed and traded; we will describe the simplest 
exotic options in section 2.7. 
Observing the payoff diagrams for the vanilla European call and put, we see 
that they cannot be negative, unlike a forward contract. Does this imply that 
you cannot lose money? Well, as you can imagine, the option comes with a 
price. With a forward contract, you pay nothing when you enter the contract, 
5A simplistic consideration would suggest that an at-the-money option is not worth exercis- 
ing; however, when considering the transaction costs involved in purchasing a stock, we see 
that there are circumstances where exercising an at-the-money option may be interesting. 

36 
FINANCIAL THEORY 
whereas the option has a price depending on several factors including the strike 
price. Hence, figures 2.6(b) and 2.6(c) are not quite correct, as the payoffs 
should be shifted down to account for the option price. Indeed, finding this 
price is the major concern with options, and this is why numerical methods 
are so important. 
Why are options traded? As with futures and forwards, there are two basic 
reasons. On the one hand, they can be used to control risks. If you hold a 
stock in your portfolio and you are worried about the possibility of a large 
drop in its price, you may reduce the risk by buying a protective put. If you 
hold a portfolio consisting of a stock and a put with strike price K ,  then the 
value of the portfolio at option maturity is 
S(T) + max{K - S(T), 0) = max{K, S(T)} 
from which we see that the downside risk is limited. This insurance comes 
with a price, since the option is not free, but in this way you avoid the risk 
of a large loss. By the same token, you may reduce the interest-rate risk of a 
fixed-income portfolio by buying interest-rate derivatives. On the other hand, 
options may also be used for speculation, as shown in the following example. 
Example 2.2 Suppose that a stock price is $50, and you believe that it will 
rise in the near future. You could then buy the stock anticipating a large 
return. Let’s say that you are right and the price rises to $55. Then your rate 
of return will be 
55 - 50 
____ = 10%. 
50 
But now imagine that a call option is available with a strike price $50, and 
that this option costs $5 (this may or may not be a reasonable price, but let 
us take it as given for the sake of the argument). In this case you will exercise 
the option, and the rate of return will be much larger: 
55 - 50 
- 
= 100%. 
5 
This effect is called leverage or gearing. As you may expect, there is another 
side to the coin. If you are wrong and the stock price drops to $49, then by 
buying the stock you will lose $1, i.e., 2% of the investment; with the call 
option you will lose 100%. You are also exposed to other sources of risk if you 
are interested in selling the option before maturity, as unfavorable movements 
in the factors determining the option value may have an adverse impact on 
the value of your portfolio. 
0 
Pricing options on stocks is a major topic in the book, and we will see 
that, depending on the complexity of the model of the underlying asset price 
dynamics, it may be a rather straightforward task or not. Interest-rate deriva- 
tives are definitely more complex, and we will just have an outlook on them 

BASIC FINANCIAL ASSETS AND RELATED ISSUES 
37 
in section 2.8. We should observe that if we consider stochastic interest rates, 
bonds too can be considered as derivatives, as their price is heavily dependent 
on interest rates. 
2.2.4 
Asset pricing, portfolio optimization, and risk management 
We have seen that we need some model to price assets such as bonds and 
options. In principle, prices are the result of an equilibrium between demand 
and supply of an asset. Equilibrium pricing models are an attempt to capture 
this equilibrium resulting from the preferences and, possibly, the initial wealth 
of investors. In the next example we try to illustrate the approach by a very 
simple example from Microeconomics. 
Example 2.3 (Equilibrium pricing in a pure exchange economy) Let 
us consider a pure exchange economy. In such an economy, we have a set of 
goods and a set of agents, and production is not considered. Each agent has 
some endowment of each good, and a preference for consumption of each good. 
For instance, let us assume that we have two agents, a and b, and two goods. 
Let the initial endowments for the two agents be, respectively, 
The two agents would probably like to exchange part of the goods they own, 
at some price which we want to determine. Let p l  and p2 be the prices of the 
two goods. To express the preferences of the two agents, we may introduce a 
utility function. For instance, let us assume a so-called Cobb-Douglas utility 
form: 
P 
1-0 
ua(Zla, Z 2 a )  = xyaxi,", 
Ub(Z1bi ZZb) = ZlbZZb 
where x z j  is the consumption of good i = 1 , 2  by agent j = a, b, and a, ,O E 
(0,l) are parameters specifying the preferences of the two agents. Nota that 
this utility function indeed models preference for consumption bundles con- 
sisting of both goods, thus agents have an incentive to exchange. We have 
an equilibrium if each agent solves his optimal consumption problem and if 
markets "clear," i.e. , consumption equals availability of each good. 
For given prices, agent a will determine optimal consumption by maximiz- 
ing his utility, subject to a budget constraint. Formally, he should solve the 
optimization problem: 
where W, = p l  is his initial wealth, i.e., the value of his (unit) endowment 
of good 1 given price p l .  Strictly speaking, the budget constraint should 
be written as an inequality, but given the form of utility functions we may 

38 
FlNANClAL THEORY 
assume that non-satiation applies: This means that the two agents are always 
happier if they can consume some more. By the same token, we should also 
include non-negativity constraints on consumption (xij 2 0), but given the 
form of utility we may assume an interior solution, i.e., a solution in which 
consumption of each good is strictly positive. The optimal solution6 is 
By the same token, agent b solves 
where wb = p z ,  yielding 
However, prices should be compatible with market clearing, i.e., total demand 
for a good is equal to its total availability. Hence, we must have: 
Requiring market clearing for the second good yields the same condition. This 
is reasonable as only the ratio of prices matters: a proportional increase in 
both prices will increase initial wealth without changing the problem. We 
could normalize prices by setting p l  = 1, i.e., by selecting good 1 as a nu- 
me raire. 
0 
We see that, in principle, we could find equilibrium prices if we knew the 
preferences of each agent. Clearly, this does not look very practical. Fur- 
thermore, in finance we must also account for time and uncertainty. This 
means that we should know how investors value immediate consumption rela- 
tive to future consumption, as well as their attitude towards risk. The task is 
even more difficult if we take information asymmetries or heterogeneous be- 
liefs into account. Unless very specific hypotheses are made, there is no hope 
to come up with a feasible pricing approach. However, by making suitable 
assumptions, interesting equilibrium pricing models have been devised. For 
stock prices, this leads, e.g., to the Capital Asset Pricing Model (CAPM); 
equilibrium models have been also proposed for interest-rate dynamics. 
61n this specific case, we could simply get rid of one decision variable by eliminating the 
equality constraint and enforcing the first-order condition, i.e., by requiring the first-order 
derivative of the utility function is zero at optimum. We will give a solution by the method 
of Lagrangian multipliers in chapter 6, page 352. 

BASIC FINANCIAL ASSETS AND RELATED ISSUES 
39 
Nevertheless, in financial engineering a much less ambitious attitude is 
usually taken. We take the prices of a set of assets as given (and observable in 
the market), and we try to find the price of other assets in such a way to avoid 
obvious inconsistencies, like the one illustrated in the following example. 
Example 2.4 (Arbitrage in a binomial model) Consider a binomial 
model of uncertainty, like the one in figure 2.1, and an economy consisting 
of two assets. The first asset is risk-free, in the sense that its price now is 
$1, and it will be $1.1 in both future states. We may think of this risk-free 
asset as a bank account offering a 10% interest rate for the period of time we 
consider. The second asset is risky: its current price is $1 too, and its future 
price could be $2 or $3 with equal probability. 
It is easy to see that these prices are not consistent. If an investor borrows 
$1 from the bank in order to buy the risky asset, she will be sure to have 
a profit: in the worst-case scenario she will gain $(2 - 1.1) = 0.9, and she 
will make even more money if the price of the risky asset turns out to be $3. 
Assuming that unlimited borrowing is allowed, she could make an unbounded 
amount of money, without incurring any risk. This is an example of an ar- 
bitrage opportunity. Loosely speaking, an arbitrage opportunity is a money 
making machine. Such a free lunch is not compatible with economic theory 
or, for that matter, with common sense. 
In general, if we assume a binomial model with multiplicative shocks u and 
d, and there is a risk-free interest rate denoted by rf, the following inequalities 
Clearly, the assumptions in the example are not quite reasonable, as unlimited 
borrowing is not possible and assets are available in limited supply. However, 
those prices are not reasonable, as they cannot be equilibrium prices, since 
investors taking advantage of arbitrage opportunity will influence prices. In 
practice, limited arbitrage opportunities are sometimes available, and there 
are traders taking advantage of them, but they tend to disappear quickly and 
are only feasible for very special  trader^.^ Hence, typical models for asset 
pricing are based on the assumption that arbitrage is not possible. 
Ruling out arbitrage opportunities leads to arbitrage-free, or relative, pric- 
ing. We price assets in such a way that their prices are consistent with ob- 
served prices for other assets. We will not investigate the relationships be- 
tween equilibrium and lack of arbitrage, but it is intuitive that arbitrage op- 
portunities are not compatible with equilibrium. The advantage of arbitrage 
pricing is that it does not rely on too many critical assumptions about the 
behavior of investors. Their aggregate risk attitude may somehow be taken 
into account by parameters which are inferred by observing market prices; this 
model calibration concept is fundamental to deal with interest-rate derivatives. 
should apply: d < 1 + rf < u. 
0 
7Transaction costs may make arbitrage opportunities unprofitable, and so they allow for 
some slight mispricing; large institutional investors may have to pay very small transaction 
costs making arbitrage available to them. 

40 
FlNANClAL THEORY 
A large part of the book is devoted to asset pricing under the no-arbitrage 
hypothesis. The second large body of applications is portfolio optimization. 
Actually, asset pricing and portfolio optimization, from a theoretical point 
of view, are not disjoint. After all, allocating wealth to assets in a portfolio 
generates demand for such assets, and demand contributes to determine asset 
prices. In financial economics, equilibrium asset pricing models are based on 
optimization models which are generalizations of the pure exchange economy 
of example 2.3. However, in everyday portfolio management, it is common to 
treat uncertainty as purely exogenous. This means that we need first to model 
uncertainty, and then to select a suitable model for portfolio optimization, 
together with some computationally feasible way of solving it. Actually, there 
is much more to that and portfolio optimization is just one part of portfolio 
management. For instance, risks must be assessed by some sensitivity analysis 
with respect to the assumed model of uncertainty, which must be somehow 
stress-tested. Portfolio optimization is only part of a decision process involving 
different actors with different organizational responsibilities. 
In its basic form, portfolio optimization entails some form of stochastic op- 
timization. By selecting a portfolio, we implicitly select a probability distri- 
bution for its return or, equivalently, for future wealth. How can we compare 
probability distributions corresponding to different portfolio choices? One 
trivial approach would be to maximize the expected value of return. The fol- 
lowing examples show that this would result in unreasonable portfolio choices. 
Example 2.5 (Putting all of your eggs in one basket) Consider an 
investor who must allocate her wealth to n assets. The return of each asset, 
indexed by i = 1,. . . , n, is a random variable Ri with expected value pi = 
E[Ri]. The asset allocation decision may be modeled by introducing a set of 
decision variables xi representing the fraction of wealth invested in asset i. If 
we rule out short-selling, these decision variables are naturally bounded by 
0 5 xi 5 1. The expected value of return from our portfolio is 
l
n
 
n 
Li=1 
J 
i=l 
i=l 
Hence, we should solve the following optimization model: 
n 
max 
'&xi 
i=l 
n 
s.t. 
c x i  = 1 
i=l 
whose solution is quite trivial: we should simply pick up the asset with max- 
imum expected return, i* = argmaxi=1,..,,,,ui1 and set xi* = 1. It is easy 

BASIC FINANCIAL ASSETS AND RELATED ISSUES 
41 
to see that this portfolio is a very dangerous bet; in practice, portfolios are 
diversified, which means that there must be something else beyond expected 
values. In practice, one would also have some constraints on portfolio compo- 
sition, limiting exposure to certain geographical areas or types of industry, and 
this would make the trivial solution above not feasible. However, if we take 
only expected return into account, the solution is basically shaped by these 
constraints. By the way, if short-selling is allowed, the decision variables are 
unrestricted, and the expected value of future wealth goes to infinity. In fact, 
one would short-sell assets with low expected return, to make money to be 
invested in the most promising asset. This is clearly unreasonable. 
0 
Example 2.6 (St. Petersburg paradox) Consider the following proposi- 
tion. You are offered a lottery, whose outcome is determined by flipping a fair 
and memoryless coin. The coin is flipped until it lands tail. Let k be the num- 
ber of times the coin lands head; then, the payoff you get is $ 2 k .  Now, how 
much should you be willing to pay for this lottery? The reader is invited to 
consider this problem as a pricing problem: the lottery is a sort of derivative 
with respect to some random outcome. We could consider the expected value 
of the payoff as the fair price for this rather peculiar asset. The probability 
of winning $2'" is the probability of having k consecutive heads followed by 
one tail, which stops the game, after k + 1 flips of the coin. Given indepen- 
dence of events, the probability of this sequence is 1/2k+1, i.e., the product 
of individual event probabilities. Then, the expected value of the payoff is 
m 
0 0 .  
k=O 
k=O 
This game looks so beautiful that we should be willing to pay any amount of 
money to play it! No one would probably do so. Again, we see that expected 
value does not tell the whole story. 
0 
These two examples show that expected values must be complemented by 
some other information, such as variance or quantiles, in order to take sensible 
decisions. More generally, we need a way to model decision making under 
uncertainty, and this calls for a way to model risk aversion. One way to do so 
is to introduce the concept of expected utility, which is done in section 2.4.1. 
Expected utility is an interesting concept, with some theoretical and practical 
pitfalls. In fact, it basically postulates that decision makers are very rational, 
consistent, and very well informed, all of which is often contradicted. But 
even if we believe that decision makers are consistently rational, it is difficult 
to elicit the utility function from any investor. A practical way out is to define 
suitable risk measures, which can be accounted for in formulating portfolio 
optimization models. A typical approach is to constrain the expected return 
of the portfolio, and then to minimize a suitably chosen risk measure. By 
varying expected return, we can trace a set of reasonable portfolios among 
which the decision maker may select the best compromise solution, trading off 

42 
FINANCIAL THEORY 
expected return against risk. If we measure risks by the variance of return, we 
obtain a well-known theory based on mean-variance efficiency (section 2.4.2). 
Recently, different risk measures have been adopted, such as Value at Risk, 
which is described in section 2.4.5. This leads to another important body of 
finance, risk management, which may take advantage from numerical methods 
as well. We should emphasize again that portfolio optimization models are 
only a part of the more general portfolio management process, which also 
includes risk assessment and management. 
We have said that asset pricing is somewhat related to portfolio optimiza- 
tion, which in turn is related to risk management. It is also important to 
understand the link between asset pricing and risk management. On the one 
hand, we need to understand the sensitivity of asset prices to random fluctu- 
ations in underlying factors, so that hypothetical scenarios for the evolution 
of the underlying factors can be mapped to changes in portfolio value. Fur- 
thermore, we would like to devise approaches to design our portfolio in such a 
way that sensitivity to such changes is minimized. For instance, we may want 
to understand how interest rates affect bond prices, and to devise portfolios 
which are at least partially immunized against shocks; this is the subject of 
the next section. 
On the other hand, however, there is a much less obvious link, which will 
be apparent when we treat option pricing in section 2.6. Consider the point 
of view of the option writer, i.e., the guy who sells an option. Options may 
be risky for people buying them, but they are even riskier for the party who 
sells them; in fact the option holder has a right to exercise, but the option 
writer must comply with this right. To get the point, consider the extreme 
case of a call option with strike price K = 20 which is exercised when the 
underlying asset price is ST = 80; this is trouble for the writer if he has to 
buy the underlying stock at 80 to sell it at 20. Hence, the option writer needs 
a reliable way to hedge against such risks. We will see that, in an idealized 
world, the option price is basically the price of a hedging strategy for the 
option writer. 
2.3 FIXED-INCOME SECURITIES: ANALYSIS AND PORTFOLIO 
I M M U N IZATION 
In this section we deal only with “really fixed” income assets, i.e., fixed-coupon 
and zero-coupon bonds. Even in this simple setting we may introduce several 
useful concepts. 
2.3.1 
In order to understand bond pricing, the first concepts we need are related to 
interest rates and how they are compounded. Assume you have wealth WO 
Basic theory of interest rates: compounding and present value 

f IXED-IN COM E SECURITIES: ANAL YSlS AND PORTFOLIO IMMUNIZATION 
43 
and you invest it in, say, a bank account for one year. After this period, you 
will get an amount of money Wl > WO. Hence, you could measure the rate 
of return of your investment by 
W1- Wo 
Wo 
. 
r =  
In other words, at the end of the investment period you collect an amount of 
money which is the sum of the principal, the original amount you owned, plus 
interest: 
W, = Wo + rW0 = (1 + r)Wo. 
The quantity r is referred to as interest rate over the time period we are 
considering. Now assume that you leave your money in the bank account for 
two years and that the same interest rate r applies for both years. How much 
money will you get? If the simple interest rule applies, you will get twice the 
interest: 
Wz = (1 + 2r)Wo. 
If the period of your investment is n years, the simple interest rule yields 
W,, = (1 + nr)Wo. 
In the general case including fractions of years, one possible rule assumes 
proportionality: 
Wt = (1 + tr)Wo, 
where t is any real number. More often than not, however, you earn interest on 
interest; after the first year, the interest you earned is added to the original 
wealth, and the interest rate for the next year will be applied to the new 
wealth: 
WZ = (1 + r)W1 = (1 + r)2Wo. 
In this case we speak of compound interest, and for n years we have 
W,, = (1 + r)"Wo. 
Note that, in the case of compounding, wealth grows more rapidly, according 
to a geometric progression. 
Compounding can occur at any frequency. For instance, let us assume 
that you get interest every six months. Typically, a nominal interest rate r 
is quoted yearly, but it is applied dividing it by the number of periods in the 
year: 
"1 = (1 + r/2)' w,. 
We obtain the effective yearly rate by equating wealth at the end of the year: 
(1 + r/2)' ~o = (1 + r,)Wo 
* 
re = r + r2/4 > r. 

44 
FlNANClAL THEORY 
If interest is compounded m times per year, we have 
Wl = ( 1  + r/m)m Wo. 
For a given nominal rate, the more frequent the compounding, the faster the 
growth and the higher the effective yearly rate. What happens if, in the 
limit, interest is compounded continuously? By taking the limit as m goes to 
infinity, and using a well-known result from calculus, we get 
Wi = lim (1 + r/m)"Wo = e' Wo. 
m+m 
Continuous compounding looks a bit artificial, but in this case many things 
turn out to be simpler, including the application of an interest rate to an 
arbitrary period of time t. We may think of dividing the time interval t in 
small slices of length l / m  years, i.e., t M k/m for some integer k. Using 
discrete-time compounding and then taking the limit we get: 
Again, we may find the effective yearly rate re corresponding to the continu- 
ously compounded rate r: re = e' - 1. 
Another fundamental concept in the basic theory of interest rates is the 
present value of a stream of cash flows in time. We will see that absence 
of arbitrage implies that the price of a bond must be the present value of a 
cash flow stream. Consider a cash flow stream, i.e., a sequence of periodic 
payments Ct at discrete-time instants t = 0,1, . . . , n. Given an interest rate r 
with discrete compounding, applied over each time period, the present value 
of the cash flow stream is defined a s  
P V = C -  ct 
t=O (1 + r ) t '  
Note that cash flows need not be positive; for instance, in investment analysis 
we typically have Co < 0, corresponding to an initial cash outlay. We say 
that cash flows are discounted, reflecting the fact that the value of $1 in the 
future is something less now; the discount factor by which each cash flow is 
multiplied is smaller for distant periods. When the nominal interest rate is 
quoted yearly but the payments occur more frequently, the formula may be 
easily adapted following the previous treatment. If there are m payments per 
year at regular time intervals, we have 
P V = C  
ck 
(1 + r / m ) k '  
k=O 
where k indexes the time periods and n is the number of periods, i.e., the 
number of years times the number of periods within one year. 

FIXEDINCOME SECURITIES: ANALYSIS AND PORTFOLIO IMMUNIZATION 
45 
All of the considerations we have made on compounding apply here. If the 
interest rate is continuously compounded, present value is 
n 
PV = C Cte-Tt. 
t =o 
Continuous compounding is very convenient when cash flows are not regular 
in time. Let us denote by ti, i = 1,. . . , n, the time at which cash flow C, is 
received. Then 
n 
i=O 
In the case of discrete compounding, one possible convention is using fraction 
of years. For instance, the present value P of cash flow C occurring in nine 
months could be expressed by 
C 
(1 + r)9/12’ 
P =  
if we assume that all months consist of the same number of days. 
It is important to note that we have assumed that the same interest rate 
r, however it is quoted, is applied to any time interval. This need not be the 
case actually, as we will see later. Furthermore, it is also worth stressing that 
we have not considered inflation. When inflation is taken into account, we 
should distinguish between nominal and real interest rate, but we will always 
disregard inflation in this book. The calculations above, possibly adjusted 
to cope with these issues, are very common and have been implemented in a 
large number of software packages, including MATLAB. Typical functions of 
this kind have been included in the Financial Toolbox. 
Example 2.7 The Financial toolbox includes different functions to analyze 
cash flow streams, including pvvar, which computes the present value of a 
stream, given an interest rate. Consider for instance the cash flow stream 
corresponding to a bond maturing in five years, with face value 100, and a 
8% coupon rate. This cash flow can be represented by the following vector: 
>> cf=[O 8 8 8 8 1081 
cf = 
0 
8 
8 
8 
8 
108 
The zero in the first position corresponds to an immediate cash flow, which in 
this case is zero, as the first coupon will be paid in one year (you may think 
that a coupon have just been paid). What is the present value of this stream 
if we discount it by an interest rate corresponding to the coupon rate? Not 
surprisingly, present value is equal to face value: 
>> pvvar (cf ,O .08) 

46 
FINANCIAL THEORY 
function pv = mypvvar(cf,r) 
% get number of periods 
n = length(cf) ; 
1 get vector of discount factors 
df = l./(l+r).-(O:n-l); 
% compute result 
pv = dot(cf,df); 
Fig. 2.7 Function to compute present value with discrete compounding and regular 
cash flows. 
ans = 
100.0000 
If we increase that discount rate, present value is decreased: 
>> pvvar(cf ,0.09) 
ans = 
96.1103 
On the contrary, if the discount rate is decreased, present value is increased: 
>> pvvar(cf ,0.07) 
ans = 
104.1002 
Indeed, we will see that when interest rates rise, bond prices fall, whereas 
bond prices increase when interest rates drop. A major task in bond portfolio 
management is to take interest-rate risk into account. 
How can we evaluate present value without the Financial Toolbox? Func- 
tion mypvvar in figure 2.7 is a possible answer. Note that, in computing the 
vector of discount factors, we must use a vector from 0 to length n minus 
1; also note the use of the dot operator both in the division (. /) and in the 
power (.^). The function dot computes the dot product of vectors: 
m 
X'Y = C XiYi, 
k = l  
provided that the vectors have the same number m of elements. The advantage 
of using dot is that we do not need worrying whether vectors are row or column 
vectors, as is the case when we use matrix multiplication. 
>> cf = [O 8 8 8 8 1081; 
>> mypvvar (cf , 0 .08) 
ans = 

FIXED- INCOME SECURITIES: A NA LYSIS AND PO R TFO L 10 IMM U NlZA TI0 N 
4 7 
100.0000 
>> mypvvar (cf ,O .09) 
ans = 
96.1103 
>> mypvvar(cf,0.07) 
ans = 
104.1002 
Another quite common concept linked to analyzing cash flow streams is the 
internal rate of return. Given a stream of cash flows Ct (t = 0,1,2,. . . , n), 
the internal rate of return is defined as a value p such that the present value of 
the stream is zero. In other words, it is a solution of the non-linear equation 
ct 
t =o 
Clearly, in order to find a solution, we must assume that at least one cash flow 
is negative. Typically, t,his is the initial cash flow Co, which may correspond to 
an investment or to the price you pay to purchase a bond. MATLAB provides 
us with useful functions to compute the internal rate of return. 
Example 2.8 We will describe methods to solve general non-linear equa- 
tions in section 3.4. However, the equation defining internal rate of return may 
be easily transformed to a specific non-linear equation, a polynomial equation, 
which is relatively easy to solve. With the change of variable h = 1/(1 + p), 
we may rewrite equation (2.2) as 
n 
C C t h t  = 0, 
t =o 
which is readily solved by the MATLAB function roots. All we have to do is 
to represent a cash flow stream as a vector, as done in the following MATLAB 
interaction snapshot. 
>> cf=[-lOO 8 8 8 8 1081 
cf = 
>> h=roots(fliplr(cf)) 
h =  
-0.8090 + 0.58781 
-0.8090 - 0.5878i 
0.3090 + 0.9511i 
0.3090 - 0.9511i 
0.9259 
-100 
8 
8 
8 
8 
108 

48 
FINANCIAL THEORY 
>> rho=l./h -1 
rho = 
-1.8090 - 0.5878i 
-1.8090 + 0.5878i 
-0.6910 - 0.9511i 
-0.6910 + 0.9511i 
0.0800 
A few comments are in order. First, we define a variable cf and we associate a 
cash flow to it. Then, in a single command line, we flip the cash flow from left 
to right with the function f liplr and we invoke the roots function to assign 
the roots of the resulting polynomial to the variable h. Flipping the cash flow 
vector is necessary since roots assumes that a polynomial is represented by 
a vector in which the first components correspond to the highest power terms 
in the polynomial, whereas when we represent cash flows we put such terms 
at the end. After obtaining the solution in terms of h, we go back to the 
original variable p (note that the dot in . / is necessary since h is a vector of 
solutions). Since in this example n = 5, we have a vector of five roots: four 
are complex conjugates, and the one we are interested in is the real one, i.e., 
p = 0.08. Indeed, it can be shown that for a cash flow stream with CO < 0 and 
Ct 2 0 (t = 1,. . . , n) and Cy=, Ct > 0, we have a unique real and positive 
solution of the non-linear equation (see, e.g., [15, chapter 21). 
If we want to devise a function filtering complex roots away, we may use 
the MATLAB find function, which returns the indexes of the elements in a 
vector meeting some condition: 
>> index = find(abs(imag(rh0)) < 0.001) 
index = 
>> rho (index) 
0.0800 
5 
ans = 
What we have done here is finding the indexes of elements in rho such that 
the absolute value of their imaginary part is less than a specified tolerance; 
then we get the elements from the vector. It is tempting to think that we 
should look for elements such that the imaginary part is exactly zero, but 
this type of “exact thinking” should be avoided when numerical computing is 
involved. To get the point, consider the trivial equation 
(X - 1)3 = x3 - 300~’ + 30,000~ - 1,000,000 = 0 
and use roots to solve it: 
>> v = [l -300 30000 -10000001; 
>> h=roots(v) 
h =  

FIXED-INCOME SECURITIES: ANALYSIS AND PORTFOLIO IMMUNIZATION 
49 
1.0e+002 * 
1.0000 + 0.OOOOi 
1.0000 - 0.OOOOi 
I .  0000 
>> index = find(abs(imag(h1) == 0) 
index = 
3 
The nasty thing occurring here is that multiple real roots may turn out as 
complex conjugates with a very small imaginary part. This is arguably un- 
likely to occur when computing internal rates of return of non-pathological 
cash flow streams, but it is a good example of pitfalls in numerical computing 
and it points out the care we need to take. All the work above (including filter- 
ing complex roots out) is done by the irr function available in the Financial 
toolbox: 
>> irr(cf) 
ans = 
0.0800 
We urge the reader to try writing a function doing all of this automatically; 
then, readers having access to the Financial Toolbox may compare their func- 
tion with irr. 
0 
With rwpect to present value, when computing internal rate of return we 
are going the other way around, in some sense. Moreover, the present value 
may be computed using a set of discount factors linked to different interest 
rates applied over time periods differing in length; the internal rate of return 
is one rate which, applied over all of the time periods, would give the same 
present value. 
2.3.2 
Pricing a zero-coupon bond Consider a zero-coupon bond, with a face value 
F ,  maturing in one year, which is currently sold at price P. If we purchase 
this security and we keep it until maturity, we will have a total return 
Basic pricing of fixed-income securities 
F 
R =  - 
P 
An obvious relationship between T ,  F ,  and P is 
F 
pz- 
1 S T '  

50 
FlNANClAL THEORY 
We may see this relationship the other way around. If we fix F and r, this 
may be interpreted as a pricing relationship. 
What rate r should we use in pricing? If the bond is default-free, as is 
usually the case with government bonds, this should be the prevailing risk- 
free interest rate: no more, no less. To see why, we may use a common 
principle in finance, i.e., the no-arbitrage principle. Assume that the bond is 
underpriced, i.e., it sells for a price PI such that 
F 
P 1 < P = -  I + r ’  
and that we may take out a loan at the risk-free interest rate r (we are 
assuming that borrowing and lending rates are equal). Then we can borrow 
an amount L and use it to purchase LIP1 bonds. Note that the immediate 
net cash flow is zero. Then, at maturity, we must pay L(1+ r )  to our money 
lender, and we get an amount FLIP1 when the face value is redeemed for 
each bond. But since, by hypothesis, 
F 
- > l + r ,  
Pl 
the net cash flow at maturity will be 
Hence, we pay nothing at the beginning and receive a positive amount in the 
future; sincc the bargain is an interesting one, we might well exploit it, in 
the limit, to ensure an unbounded profit for increasing L. This is a simple 
example of arbitrage. Of course, limitless borrowing is not available; more 
important, purchasing a huge amount of those bonds would raise their prices, 
and the arbitrage opportunity would soon disappear. Indeed, a common as- 
sumption in many financial problems is that arbitrage opportunities do not 
exist. Note that this does not imply that they actually do not exist; on the 
contrary, it is the very fact that many people are out there to exploit those 
opportunities which tends to eliminate them quickly. The argument may be 
repeated similarly if the inequality is reversed and the bond is overpriced: 
F 
P , > P = -  1 +r’ 
In this case we should borrow the bond itself, rather than the cash needed to 
buy it. This is accomplished by selling the bond short (see example 2.1 on 
page 32 for an illustration of short-selling a stock). There are many limitations 
to short-selling in practice, but for pricing models it is often (not always) 
reasonable to assume that it is possible. Then we may sell the overpriced 
bond and invest the proceeds at the risk-free rate; let us assume that we 
borrow bonds for a total value L, we sell them at price PI, and we invest the 

FIXEDINCOME SECURITIES: ANALYSIS AND PORTFOLIO IMMUNIZATION 
51 
money we obtain. The immediate net cash flow is again zero. At maturity, 
we get L(1-t r )  from our investment, and we have to pay the face value F to 
the owner for each bond that we have borrowed. Hence the net cash flow at 
maturity is again positive: 
We have also implicitly assumed that transaction costs are negligible and that 
we may lend or borrow money at the same rate. Again, these assumptions are 
violated in practice, but they may be close enough to reality, at least for some 
large investors, to warrant their use. The reader may have the impression that 
the arbitrage argument is, at least in this case, an unnecessary complication to 
obtain an almost obvious result: the price is obtained by taking the present 
value of its future cash flows. However, the no-arbitrage principle is used, 
with some modification, to price quite complex securities where uncertainty 
is involved and intuition does not help (as in the case of options; see section 
2.6.2). 
No-arbitrage and linearity of pricing 
Before proceeding and considering pric- 
ing coupon-bearing bonds, it is useful to point out a couple of important 
implications of the no-arbitrage principle. 
The first implication is the law of one price. Different assets cannot sell 
for different prices, in idealized markets, otherwise an immediate arbitrage 
opportunity arises. In practice, markets are not perfect, and we all know that 
the same product may be sold at different prices in different countries. In this 
case, arbitrage opportunities are eliminated by transportation costs, taxes, 
etc. Financial markets, also thanks to Internet, are closer to perfect markets, 
and for modeling purposes we may assume that the law of one price makes 
sense. We will also see that it makes sense when uncertainty is involved. 
Another implication is that pricing is a linear operator. To get the point, 
let us denote by P(.) an abstract pricing operator that maps assets to prices. 
Linearity means that the price of a portfolio of assets should be the weighted 
sum of the prices of each single asset. Formally, if we denote an asset by X,, 
i = 1,. . . , n, we have 
where P(X,) is the price of asset i and ai is the number of assets of type i 
in the portfolio. To see this, let us break the argument in two parts. If we 
consider one asset, we should have P ( 2 X )  = 2 P ( X ) .  If, for instance, P ( 2 X )  < 
2 P ( X ) ,  we may make an immediate profit by purchasing two assets and selling 
them separately. A similar consideration applies if P ( 2 X )  > 2 P ( X ) .  The 
same reasoning can be applied with an arbitrary number of assets, at least in 
idealized markets with no friction; in real markets, transaction costs, round 

52 
FlNANClAL THEORY 
lots, etc., make the argument only approximately valid. By the same token, 
we must have P(X1+ X2) = P(X1) + P(X2). 
If, for instance, P(X1 + X z )  < 
P(X1) + P(X,), we may buy the bundle of two assets and then make an 
immediate profit by selling them separately. Again, reality is a bit different. 
Prices may be non-linear when transaction costs are involved or when assets 
are in limited supply and markets are thin. 
Linearity of pricing has an important implication on pricing coupon-bearing 
bonds; if we regard such a bond as a portfolio of zero-coupon bonds, it is 
immediate to see that we may price each coupon as a zero-coupon bond and 
sum the results. 
Pricing a coupon-bearing bond Linearity of pricing implies that a bond may 
be priced by pricing vach coupon separately, including payment of face value 
at maturity. Consider a bond with face value F ,  paying a coupon C per 
period. Pricing is very simple, if we assume that the bond is default-free, so 
that a riskless interest rate may be applied, and that this rate can be applied 
to any period length (provided that we account for compounding). It is easy 
to see that the fair bond price may be obtained by computing the present 
value of its cash flow stream: 
F 
+- 
"
c
 
z=1 ( l + r ) z  ( l + r ) n '  
PV=C--- 
This is the basic principle, which links present values and prices. As expected, 
several complications may arise in practice. 
0 If r is quoted yvarly and there is more than one coupon payment per 
year, the formulit could be adjusted in the same vein as equation (2.1). 
If m coupons an' paid in a year: 
n 
Clm 
+ 
F 
PV = c 
(1 + r / m ) z  
(1 + r/m)" 
i=l 
where n is the number of periods. 
0 Another fundamental issue is that different interest rates are typically 
associated to different time horizons. This implies that bond pricing 
requires knowledge of several discount factors. If we denote by rt the 
interest rate which applies from now to time t, i.e., the spot rate, we 
should discount oach coupon C, appropriately: 
The set of rates rt is related to the term structure of interest rates. The 
idea is depicted in figure 2.8, where we see an upward-sloping structure; 

FIXED-IN CO ME SECURITIES: ANALYSIS AND PORTFOLIO I M  M UNlZATlON 
53 
0 
fig. 2.8 
and the corresponding (percentage) spot interest rates are plotted. 
Term structureof the interest rate; years are reported on the horizontal axis, 
this corresponds to the intuitive notion that longer interest rates are 
usually associated with longer terms. Actually, other shapes are possible 
in general. A downward sloping curve is usually associated to recession, 
whereby interest rates are expected to drop in the future. Note that an 
upward sloping curve does not necessarily imply that interest rates are 
expected to rise. 
0 If these simple formulas were generally applicable, any bond with the 
same coupon rate and maturity date should have the same price, which 
is actually not the case. A first point is that not all bonds are issued 
by institutions with the same credit rating. Although a bond issued by 
some governments may be default-free, a corporate bond may not be of 
the same quality; hence, all other things being equal, you would require 
a lower price for it. This difference may be captured by the bond yield, 
which is introduced in the next section. 
Measuring return of a bond: yield to maturity We have seen that the price of a 
fixed-coupon bond is basically the present value of its cash flow stream, which 
may depend on a whole set of interest rates. But how can we measure the 
return of a bond of given price by a single number? One possible idea is to 
compute the internal rate of return of the bond. The internal rate of return 
of a bond is called the yield,' 
and for a bond with price P it is the solution, 
6hctually, there are different concepts of yield (see, e.g., [6] or [7]), but we will stick t o  this 
one for the sake of simplicity, even though it may be subject to some criticism. 

54 
FlNANClAL THEORY 
A, of the following equation: 
F 
(1 + A)i + (1 + A)n* 
i=l 
If more than one coupon payment is made during a year, the equation defining 
yield is immediately adapted: 
n 
Clm 
+ 
F 
P = X  (1 + A/rn)% (1 + A/m).' 
i=l 
From these equations it is easy to see that bond prices will drop if there is 
an increase in required yield A, and vice versa. Required yield may increase 
if bond rating gets worse, which calls for some risk premium, or if the general 
level of interest rates rises. Analyzing the relationship between price and yield 
is relatively easy, but it is just an approximation. A full term structure of 
interest rates should be taken into account, as the curve may not only go up 
or down, but it may also twist and change its qualitative shape. Nevertheless, 
an approximate analysis is often valuable, as we will see shortly. 
Issues in bond portfolio management: interest-rate risk Intuitively, the higher 
the required yield, the lower the price, and higher yields must be offered for 
risky bonds. If the credit rating of the bond issuer changes, the bond price 
will change accordingly to reflect the new situation. But is credit risk the 
only source of risk for bonds? Unfortunately, the answer is no. To begin 
with, coupon rates may depend on some other economic or financial variable, 
resulting in some uncertainty in the cash flow, so we have a form of financial 
risk. Another point is that some bonds have embedded options which may 
be unfavorable for the holder; for instance, the issuer may call the bond, 
that is, redeem it before maturity, which results in reinvestment risk since we 
would have to reinvest the cash we receive from the bond issuer (bonds with 
embedded options may be analyzed using techniques we discuss later when 
we deal with options). 
But even if all of these risks are ruled out, there may still be a form of 
risk, depending on the intended use of the security. The point is that any 
portfolio of bonds has some purpose, and the portfolio risk must be evaluated 
with reference to this purpose. A common use of a bond portfolio is to enable 
some institution (e.g., a pension fund) to comply with a stream of future 
liabilities. To be more concrete, assume that we have to pay a sequence of 
liabilities over a time horizon which is discretized in T periods and that the 
liability in period t = 1,. . . , T is Lt. Now, we could just purchase bonds in 
such a way as to meet all the liabilities. In fact, this is possible, at least in 
principle. Consider a set of N bonds, each with a price Pi (i = 1,. . . , N ) .  If 
the cash flow from a unit of security i at time t is represented by Fit, we may 

FIXED-INCOME SECURITIES: ANALYSIS AND PORTFOLIO IMMUNIZATION 
55 
consider the following cash flow matching model: 
N 
r = l  
N 
s.t. 
vt 
Here the decision variable xi represents the amount of bond i purchased 
(rather than the weight in the portfolio). If we neglect the possibility of 
default and assume that the liabilities are known in advance, the resulting 
portfolio would certainly meet the obligations; unfortunately, it is likely to 
be quite expensive. Unless bond maturities are matched to the liabilities, we 
will have to meet the obligations with coupon payments, requiring a possibly 
large number of bonds. Note also that liabilities are taken into account by an 
inequality constraint, which may turn out to be strict, since it is unlikely that 
a perfect match of cash flows and liabilities may be obtained with a given set 
of bonds. In the case of a long planning horizon, the lack of suitable long-term 
bonds may compound these difficulties. 
Hence, we must manage our bond portfolio in a more dynamic manner, 
buying and selling bonds along the way. But here comes the trouble. Bond 
prices are related to interest rates, and these may change in unpredictable 
ways. For instance, is a five-year zero-coupon bond riskless? 
Example 2.9 Consider a five-year zero-coupon bond, with face value 100, 
sold with required yield r1 = 0.08. Which is the percentage change in its price 
if the yield is increased immediately after purchase to r2 = 0.09? 
>> r1=0.08; 
>> r2=0.09; 
>> P1=100/(l+r1)-5 
PI = 
>> ~2=100/ 
(I+r2) 
-5 
P2 = 
64.9931 
>> (P2-P1)/P1 
-0.0450 
68.0583 
ans = 
We see that we have a 4.5% decrease the value of the bond. Note that this 
loss occurs only if you have to sell the bond before maturity. No harm is done 
if you keep the bond to maturity, but this makes sense only if the liability 
you want to match coincides with maturity. Now what if the maturity is 20 
rather than five years? 

56 
NNANClAL THEORY 
>> P1=100/(1+r1)^20 
Pl = 
>> P2=100/(l+r2)-20 
P2 = 
>> (P2-Pl)/Pl 
-0.1683 
21.4548 
17.8431 
ans = 
We see that the loss is now much larger, almost 17%. Although zero-coupon 
bonds with long maturities may not be available easily, it is a general rule 
that the longer the maturity, the more sensitive to yield changes the bond 
price is. Coupon rates play some role, too. We may compare two bonds with 
coupon rates of 4% and 8%, respectively. 
>> cfl=[O 8 8 8 8 8 8 8 8 8 1081; 
>> cf2=[0 4 4 4 4 4 4 4 4 4 1041; 
>> P1=pvvar(cfl,0.08) 
P1 = 
>> P2=pvvar (cf 1 , O .  09) 
P2 = 
100.0000 
93.5823 
>> (P2-Pl)/Pl 
-0.0642 
ans = 
>> Pl=pvvar(cf2,0.08) 
P1 = 
>> ~2=pvvar(cf2,0.09) 
P2 = 
67.9117 
>> (P2-P1)/Pl 
73.1597 
ans = 
-0.0717 
We see that a lower coupon rate implies a larger sensitivity. 
0 
The problem is that the interest rates are not constant over time; they 
may change, depending, e.g., on inflation or general economic conditions. The 
changes in interest rates may be complex, as we should take a whole curve 
of spot rates into account. The curve may shift up or down, but it may also 
change shape, as it may steepen or flatten. In the example above we have 
just captured these complex changes with one measure, yield. If rates move 
up, a higher yield will be required for new bonds of the same characteristics. 

FIXED-INCOME SECURITIES: ANALYSIS AND PORTFOLIO IMM U NlZATlON 
57 
For bonds issued in the past and traded on secondary markets, an increase in 
the yield results in a decrease in the price at which they may be sold. On the 
contrary, if interest rates drop, we may gain something from the decrease in 
the required yield, which results in an increase in the price. Depending on the 
maturity and the coupon rate, we have seen that a bond may be more or less 
sensitive to yield changes. We need a formal way to measure the interest-rate 
risk associated with bonds, in order to figure out a way to shape a fixed- 
income portfolio. A relatively simple answer is represented by the duration 
and convexity concepts discussed in the next section. 
2.3.3 
Imagine that you are an investor facing a stream of known liabilities in the 
future and you want to hold a portfolio of bonds such that you may meet the 
liabilities. On the one hand, you would like to do it at minimum cost, but you 
would also like to hold a portfolio that is not likely to get you in trouble in 
case of changes in the interest rates. As a simple example, imagine that you 
have one liability L to be paid in five years. If you may find a safe zero-coupon 
bond maturing in five years, with face value F ,  you may just buy an amount 
LIF of these bonds. However, if the bond maturity is less than five years, 
you will face reinvestment risk; if the bond maturity is more than five years, 
you will face interest rate risk, as we have seen in example 2.9. Ideally, you 
would like to find a zero-coupon bond with maturity corresponding exactly to 
the date of each liability. Unfortunately, it is practically impossible to do so, 
and we must find another way to protect the bond portfolio against interest 
rate uncertainty. Immunization is a possible, and simple, solution. 
Formally, we have a function P(A) that gives the relationship between the 
yield and the price of a bond. We may draw this curve (how this may be done 
in MATLAB is explained in example 2.11), obtainingsomething like the curve 
illustrated in figure 2.9. We see that the curve is c o n ~ e x , ~  
which is actually 
the case for usual bonds. Now, consider small movements in the required 
yield; we would like to find out a way to approximate the change in price with 
respect to a change in yield. Indeed, there are two concepts, duration and 
convexity, which can be used to this aim. 
Given a stream of cash flows occurring at times to, tl, . . . , t,, the duration 
of the stream is defined as 
Interest rate sensitivity and bond portfolio immunization 
PV(t0)to + PV(t1)tl + PV(t2)tz + . . . + PV(t,)t, 
D =  
1 
PV 
where PV is the present value of the whole stream and PV(ti) is the present 
value of cash flow ci occurring at time ti, i = 0,1, . . . , n. In some sense, the 
gFormally, a function f is convex on a set if, for any choice of x and y in that set, f(Ax + 
(1 - X)y) 5 Xf(x) + (1 - X)f(y) holds for 0 5 X 5 1; more on this in supplement S6.1. 

58 
NNANClAL THEORY 
Fig. 2.9 Price-yield curve. 
duration looks like a weighted average of cash flow times, where the weights 
are the present values of the cash flows. Note that for a zero-coupon bond, 
which has a single cash flow, the duration is simply the time to maturity. 
When we consider a generic bond and use the yield as the discount rate in 
computing the present values, we get Macaulay duration: 
"
k
 
Ck 
C m (1 + X/m)k 
C 
k=l (1 + X/m)k 
D = k=l 
n 
1 
ck 
where it is assumed that there are m coupon payments per year. In order 
to see why duration is useful, let us compute the derivative of the price with 
respect to yield: 
d 
- 
dP 
dX 
- -  
If we define the modified duration DM = D/(1+ X/m), we get 
- 
= -DMP. 
dP 
dX 

FIXED- INCOME SECURI TIES: ANAL YSlS AND PO R TFO L 10 IM M U NIZA TI0 N 
59 
Thus, we see that the modified duration is related to the slope of the price- 
yield curve at a given point; technically speaking, it is the price elasticity of 
the bond with respect to changes in the yield. This suggests the opportunity 
of using a first-order approximation: 
6P M -DMP 6.A. 
An even better approximation may be obtained by using a second-order ap- 
proximation. This may be done by defining the convexity: 
1 d2P 
C = - -  
P dX2 
It turns out that, for a bond with m coupons per year, 
C =  
m2 
( l + X / r n ) k ’  
k = l  
Note that the unit of measure of convexity is time squared. Convexity is 
actually a desirable property of a bond, since a large convexity implies a slower 
decrease in value when the required yield increases, and a faster increase in 
value if the required yield decreases. Using both convexity and duration, we 
have the second-order approximation 
PC 
2 
6P M -DMP 6X + - ( c ~ X ) ~ .  
Example 2.10 We may check the quality of the price change approximation 
based on duration and convexity with a simple example. Let us consider a 
stream of four cash flows (10,10,10,10) occurring at times t = 1,2,3,4. We 
may compute the present values of this stream under different yield values 
using MATLAB function pvvar: 
>> cf = [lo 10 10 101 
cf = 
>> pl=pvvar( [O, cf] , 0.05) 
10 
10 
10 
10 
p l  = 
35.4595 
>> p2=pvvar ( [O, cf 1 , 0.055) 
p2 = 
>> p2-pi 
35.0515 
ans = 
-0.4080 
Note that we have to add a 0 in front of the cash flow vector cf since pvvar 
assumes that the first cash flow occurs at time 0. We see that increasing the 

60 
FlNANClAL THEORY 
yield by 0.005 results in a price drop of 0.4080. Now we may compute the 
modified duration and the convexity using the functions cfdur and cf conv. 
The function cfdur returns both Macauley and modified duration; for our 
purposes, we must pick up the second output value. 
>> [dl dml = cfdur(cf,0.05) 
dl = 
d m =  
>> cv = cfconv(cf,0.05) 
2.4391 
2.3229 
cv = 
8.7397 
>> -dm*pl*0.005 
ans = 
-0.4118 
>> -dm*p1*0.005+0.5*cv*p1*(0.005)-2 
ans = 
-0.4080 
We see that at least for a small change in the yield, the first-order approxima- 
tion is satisfactory and the second-order approximation is practically exact. 
0 
We have defined duration and convexity for a single bond; what about a 
bond portfolio? If the yield is the same for all the bonds, it can be shown that 
the duration of the portfolio is simply a weighted average of all the durations 
(the weight is given by the weight of each bond within the portfolio). This is 
not exactly true if yields are not the same; however, the weighted average of 
the durations may be used as an approximation. How can we take advantage 
of this? In the case of asset liability management, one possible approach is to 
match the duration (and possibly the convexity) of the portfolio of bonds and 
the portfolio of liabilities. This process is called immunization. To carry out 
the necessary calculations, we may use the functions available in the Financial 
toolbox. 
2.3.4 
MATLAB functions to deal with fixed-income securities 
When turning our attention from simple cash flows streams to real-life bonds, 
various complications arise. The first one is that in order to represent the 
settlement date and the maturity date of a bond correctly, we must be able 
to cope with a calendar, taking leap years into account. MATLAB has an 
internal way of dealing with dates, which is based on converting a date to 
an integer number. For instance, if we type today, MATLAB replies with a 
number corresponding to the current date; this number may be converted to 
a more meaningful string by using datestr: 

FIXED-INCOME SECURITIES: ANALYSIS AND PORTFOLIO IMMUNIZATION 
61 
>> today 
ans = 
732681 
>> datestr (today) 
ans = 
04-Jan-2006 
You may wish to check which date corresponds to day 1. The inverse of 
datestr is datenum: 
>> datenum(’04-Jan-2006’) 
ans = 
732681 
There is a wide variety of string formats that you may use to input a date in 
MATLAB; the one you see above is only one of them (note that it is neces- 
sary to enclose the string between quotes). Dates must be taken into account 
for different reasons. Consider buying a bond after it is issued; if you buy a 
bond at a date between two coupon payments, the time elapsed from the last 
coupon payment date must be taken into account. If not, you would receive 
a coupon benefit to which the previous owner is partially entitled. Actually, 
by computing the present value of the cash flow stream you would take it into 
account; however, the market convention is to quote a bond price without 
considering this issue. What you read is the clean price, to which accrued 
interest must be added in order to obtain the correct price. Accrued interest 
may be computed by prorating the coupon payment over the period between 
two payments. Roughly speaking, if coupons are paid every six months and 
you buy a bond two months before the next coupon payment, you owe some- 
thing like two-thirds of the coupon to the previous owner. However, there 
are different day count conventions to make the necessary calculations. These 
issues are considered in the bndprice function, which is used to price a bond, 
for a given yield value. To understand the input arguments required, we may 
use the online help (we have included only the first few lines appearing on the 
screen): 
>> help bndprice 
BNDPRICE Price a fixed income security from yield to maturity. 
Given NBONDS with SIA date parameters and semi-annual yields to 
maturity, return the clean prices and the accrued interest due. 
[Price, AccruedInt] = bndprice(Yield, CouponRate, Settle, Maturity) 
[Price, AccruedInt] = bndprice(Yield, CouponRate, Settle, . .  
Maturity, Period, Basis, EndMonthRule, IssueDate, ... 
FirstCouponDate, LastCouponDate, StartDate, Face) 
We see that, as usual in MATLAB, this function may be called with a minimal 
set of input arguments, which are required yield, coupon rate, settlement date 

62 
FlNANClAL THEORY 
(i.e., when the bond is purchased), and maturity date. The two output values 
are the clean price and the accrued interest, which must be summed in order 
to get the real (dirty) price: 
>> [clPr accrInt] = bndprice(0.08, 0.1. ’10-aug-2007’, ’31-dec-2020’) 
clPr = 
116.2366 
accrInt = 
1.1141 
>> clPr+accrInt 
ans = 
117.3507 
When calling the function this way, all the other arguments take a default 
value. For instance, the Period parameter] which is the number of coupon 
payments per year, is assumed to be two, and the face value (Face) is assumed 
to be 100. Another possibly important parameter is Basis, which controls 
the day count convention in computing the accrued interest; the default value 
is 0, which corresponds to the actuallactual convention; if the parameter is 
set to 1, the convention is 301360 (i.e., it is assumed that all months consist of 
30 days). To appreciate the difference between the day count conventions, we 
may compute the number of days between two dates by the 301360 convention 
and the actual number of days: 
>> days360(’27-Feb-2006’, ’4-Apr-2006’) 
ans = 
37 
>> daysact(’27-Feb-2006’, ’4-Apr-2006’) 
ans = 
36 
Other day count conventions are possible and used for different securities (see, 
e.g., [i’]). The remaining parameters are related to the coupon structure and 
are described in the Financial toolbox manual. 
Example 2.11 To obtain the priceyield curve of figure 2.9, we may use the 
following code fragment: 
settle 
= ’19-Mar-2000’; 
maturity 
= ’15-Jun-2015’; 
face 
= 1000; 
couponRate = 0.05; 
yields = 0.01:0.01:0.20; 
CcleanPrices , accrIntsl = bndprice(yields, couponRate, settle, ... 
plot (yields, cleanPrices+accrInts) ; 
grid on 
Note that when we have to provide a function with an optional argument] 
such as the face value, but we do not want to use optional arguments which 
maturity, 2, 0, C1 , [I , [I , [I, [I , face); 

FIXED- INCOME SECURITIES: ANAL YSlS AND POR TFOL 10 IMMUNIZATION 
63 
should occur before that one, we have to pass empty vectors represented by 
[I so that the arguments are properly matched. 
0 
For now, we have computed a price given a required yield. We may also 
go the other way around; we may compute the yield given the price, using 
another predefined function: 
>> Cleanprices = 195 100 1051; 
>> bndyield(CleanF'rices, 0.08, datenum( '31-Jan-2006'), '31-Dec-2015') 
ans = 
0.0876 
0.0800 
0.0728 
The minimal set of parameters for the bndyield function are: the clean price, 
with no accrued interest; the coupon rate; the settlement date; and the matu- 
rity date. In this case we have used a common feature of MATLAB functions. 
If a vector is passed as an argument, where a scalar would be used in the 
simplest case, the output is, typically, the vector of the results obtained by 
applying the function to each component of the input vector. Here we have 
used different prices, and we see that a bond selling below par (95) has a 
yield higher than the coupon rate; yield and coupon rate are equal for a bond 
selling at par (100); yield is lower for a bond selling above par (105). Optional 
parameters may be passed to bndyield, which are similar to the parameters 
of bndprice. 
Other useful functions may be used to compute duration and convexity, 
given the price or the yield of a bond. They are best illustrated by a simple 
immunization example. 
Example 2.12 A common problem in bond portfolio management is to 
shape a portfolio with a given (modified) duration D and convexity C. Sup- 
pose that we have a set of three bonds; we would like to find a set of portfolio 
weights wl, w2, and 203, one for each bond, such that 
3 
i=l 
? 
E C i W i  = c 
i=l 
3 CWi = 1, 
i=l 
where Ci and Di are the bond durations and convexities, respectively (i = 
1,2,3). Note that we have assumed that both the duration and the convex- 
ity of the portfolio can be computed as weighted combinations of the bond 
characteristics; actually, this is not true in general, but for the moment we 

64 
FINANCIAL THEORY 
% SET BOND FEATURES (bondimmun.m) 
settle 
= ’28-Aug-2007’; 
maturities 
= [’15-Jun-2012’ ; ’31-Oct-2017’ ; ’01-Mar-2027’1; 
couponRates = c0.07 ; 0.06 ; 0.081 ; 
yields = C0.06 ; 0.07 ; 0.0751 ; 
% COMPUTE DURATIONS AND CONVEXITIES 
durations = bnddury(yields, couponRates, settle, maturities); 
convexities = bndconvy(yields, couponRates, settle, maturities); 
% COMPUTE PORTFOLIO WEIGHTS 
A = [durations’ 
convexities’ 
1 1  11; 
b = [ 1 0  
160 
weights = A\b 
11 ; 
Fig. 2.10 Simple code for bond portfolio immunization. 
will consider this as a simple approximation. All we have to do is to compute 
the coefficients Ci and Di and to solve a system of three equations and three 
unknowns. This is easily accomplished by the script in figure 2.10. Note that 
we have assumed a given yield, and that we have used the functions bnddury 
and bndconvy to compute durations and convexities. It is possible to carry 
out a similar computation starting from the clean bond prices; we have just 
to use functions bnddurp and bndconvp. By running the script, we obtain the 
following solution: 
weights = 
0.1209 
-0.4169 
1.2960 
Note that we have to sell bond 2 short, which may not be feasible. 
0 
2.3.5 
Critique 
The naive immunization and cash flow matching models, that we have just 
discussed, leave room for many criticisms. 
To begin with, duration is only an approximate measure of bond price 
sensitivity. It is a correct measure only if the term structure is flat (i.e., 
the same rate applies to any period length) or if there is a parallel shift on 

STOCK PORTFOLIO OPTIMIZATION 
65 
the term structure. In practice, shape changes are possible, calling for more 
sophisticated sensitivity measures and immunization approaches. 
Another issue is that immunization protects against small changes in the re- 
quired yield. But after such a change, the duration and convexity are changed 
and the portfolio is no longer immunized. In fact, we are not paying due atten- 
tion to the dynamic character of portfolio management. In the limit, consider 
a portfolio consisting of two bonds, one with a short and the other with a 
long duration, bracketing the target duration. It may be the case that the 
first bond has a short maturity; when maturity is reached, we are left with 
only one bond and a portfolio that is far from immunized. Continuous port- 
folio rebalancing may lead to nervous trading and high transaction costs. An 
alternative is to use dynamic optimization models, accounting for uncertainty 
in the interest rates and for dynamic trading. This leads to stochastic pro- 
gramming models, which are described in chapter 11. With such models, the 
stochastic nature of liabilities can also be accounted for. 
Apart from using more sophisticated models, one can use more sophisti- 
cated assets. In fact, the need for interest-rate risk management has produced 
a vast array of interest-rate derivatives (see section 2.8). Both pricing such 
derivatives and managing interest-rate risk requires modeling the term struc- 
ture of interest rates; this is a vast and difficult topic, which is actually beyond 
the introductory aim of this book. 
2.4 
STOCK PORTFOLIO OPTIMIZATION 
Unlike bonds and derivatives, we do not consider pricing problems for stocks. 
There are models aimed at finding a “rational” price for a stock share of a 
firm, but they are beyond the scope of the book. Hence, we will consider stock 
prices as exogenous and we will only consider stock portfolio management. 
There is a set of n stocks and we must allocate our wealth among them. For 
simplicity, we do not consider dividend issues nor consumption, and we tackle 
a simple single-period problem, leaving multi-period portfolio optimization to 
later chapters. Our basic assumption is that uncertainty can be modeled by a 
probability distribution, which we treat as it were objective, and likely built on 
the basis of historical data. This need not be the case in portfolio management, 
as one could have some view, or information, which should be reflected in the 
decision problem. By selecting a portfolio, we select a probability distribution 
of future wealth, which is a random variable. We have seen in examples 
2.5 and 2.6 on page 40 that using plain expected values in decision making 
under uncertainty may lead to unreasonable results. We must find a sensible 
way to model preferences under uncertainty, which essentially means that 
we must express risk aversion. The simplest approach to do so is based on 
utility theory, which is introduced in section 2.4.1. Since finding the utility 
function of a decision maker is no trivial task, practical approaches have been 
proposed based on risk measures. The best-known concept is mean-variance 
efficiency, which is dealt with in section 2.4.2; in section 2.4.3 we also illustrate 

66 
FINANCIAL THEORY 
a few MATLAB functions to cope with mean-variance portfolio optimization. 
Alternative risk measures, most notably Value at Risk, are discussed in section 
2.4.5. 
2.4.1 
Utility theory 
The idea that most investors are risk averse is intuitively clear, but what does 
risk aversion really mean? A theoretical answer, commonly used in economic 
theory, can be found by assuming that decision makers order uncertain out- 
comes by some utility function. To introduce the concept, let us consider 
simple lotteries, which may be regarded as investments under uncertainty. If 
a lottery has discrete outcomes, then it corresponds to a random variable X ,  
with possible values xi and probabilities p i ,  and it can be represented by a fan 
like figure 2.2. The decision maker should select among alternative lotteries 
or she may also combine them, forming new random variables. For instance, 
consider an agent who has to choose between the following two lotteries: lot- 
tery a l ,  which is actually deterministic and ensures a payoff p, and lottery 
a2, which has two equally likely payoffs p + 6 and p - 6. The two lotteries 
are clearly equivalent in terms of expected payoff, but a risk-averse agent will 
arguably select lottery al. More generally, if we have a random variable X 
and we add a mean-preserving spread, i.e., a random variable E with E[E] = 0, 
this addition is not welcome by a risk-averse decision maker. 
Given a set of lotteries, the agent should be able to pick up the preferred 
one; or, given any pair of lotteries, the agent should be able to tell which one 
she prefers or to decide that she is indifferent among them. In this case, we 
would have a preference relationship among lotteries. Since preference rela- 
tionships are a bit cumbersome and are not easy to deal with, we could map 
each lottery to a number, measuring the utility of that lottery to the agent, 
and use the standard ordering of numbers to sort lotteries. For arbitrary pref- 
erence relationships, a function representing them may not exist, but under a 
set of more or less reasonable assumptions,1° such a mapping does exist and it 
can be represented by a utility function. A particularly simple form of utility 
function, which looks reasonable but is justified by specific hypotheses on the 
preference relationship it models, is the Von Neumann-Morgenstern utility: 
n 
i=l 
for some function u(.), 
where a is a lottery with outcomes xi and probabilities 
pi. The function u(.) 
is the utility of a certain payoff, and U(.) is clearly 
the expected utility. If u(x) = x, then the utility function boils down to the 
'OThe discussion of these assumptions is best left to books on Microeconomics; we should 
mention that most of them look rather innocent and reasonable under most circumstances, 
but they may lead to surprising effects in paradoxical examples. 

STOCK PO R TFO L 10 0 
P TI MlZA TI0 N 
6 7 
rxpec'tecl value of the payoff, but by selecting the utility u we may model 
differcwt attitiides towards risk. For our problems, it is reasonat)le to assuirie 
that utilitv u(.) is an increasing function, since we prefer inore wealth to less. 
111 the case of the two lotteries above, preference for a1 is expressed by 
Siiiw t,lie iiieqiidit,y is not, strict, we should say that lottery a1 is at least 
iis prcferretl as (12, as t,he agent could he indifferent between the two. More 
goilc!rally, if we have t,wo possible outcomes 2 1  and 22, with probabilities 
p~ = p nnrl p a  = 1 - p ,  a risk-averse decision rnaker would prefer not taking 
Cll iL1 Ices: 
u(E[X]) = '7/(lJ:t:] + (1 - P ) : C ~ )  2 ~ H L ( : c ~ )  
+ (1 - ? ) ) I L ( : C ~ )  = E[7r(X)]. 
Tliis coiitlitioii I>iisi(:idly stat,cs tliat the function u(.) 
is C O ~ C ~ V J C .  
Wc sec that 
(YJll('ilVit,y is linked to ronvexity, a s  the two concepts are related by tt chttnge 
in tlw seiise of the inequality, and a function f(.) is concave if and only if the 
fiinctioii -f(.) is coiivcx (see supplcrnent S6.1). Figure 2.11 illustrates the 
role of ctoiiwvit,y. It can he shown that for a continuoiis or discrete randoni 
vniiablc. tlio following .Jenseii's inequality holds for a concave function: 
It is f\lntl;iinrntid to ohscrve that the exact nutiierical valuc of the utility 
;issigiiatl t,o lottcrios is irrclcvnnt; only tlic relative orderiiig of altcriiiitivcs is 
twseiitinl. Iii fiwt, we speak of ordinal rather than cardinal utility. Giveii the 
linciirity of c~xl,c":t,~Lt,ion, 
we also see that an affiiie transforination of utility 
Fig.2.11 How concave utility functions imply risk aversion: the certainty equvalent
is also shown.

68 
FINANCIAL THEORY 
has no effect, provided it is increasing: if we use au(z) + b instead of u(z), 
the ordering is preserved, provided that a > 0. 
How can we say something about the properties of a specific utility func- 
tion? In particular, we would like to come up with some way to measure 
risk aversion. We have said that a risk-averse agent would prefer a certain 
payoff rather than an uncertain one, when the expected values are the same. 
She would take the gamble only if the expected value of the risky lottery 
were suitably larger than the certain payoff. In other words, she requires a 
risk premium. The risk premium depends partly on the risk attitude of the 
agent, partly on the uncertainty of the gamble itself. We will denote the risk 
premium by pu(X); note that it is a number, which a decision maker with 
utility u(.) 
associates to a random variable X. The risk premium is defined 
by requiring 
@[XI - PU.(X)) = U ( X ) .  
(2.8) 
The risk premium implicitly defines a certainty equivalent, i.e. a certain payoff 
such that the agent would be indifferent between the lottery and this payoff 
Note that the certainty equivalent is smaller than the expected value, and the 
difference is larger when the risk premium is larger. These concepts may be 
better grasped by looking again at figure 2.11. 
A difficulty with the risk premium concept is that it mixes the intrinsic risk 
of a lottery with the risk attitude of the agent. We might wish to separate 
the two sides of the coin. Consider a lottery X = x + El, where x is a given 
number and El is a random variable with E[El] = 0 and Var(El) = a’. Assume 
that the random variable El is a “small” perturbation, in the sense that each of 
its realizations 6 is a relatively small number.“ Hence, we may approximate 
both sides of equation (2.8) by Taylor expansions. Consider for instance the 
expression u(z + 6 ) .  Since only numbers are involved here, we may write 
By writing the same approximation for the random variable El and taking 
expected values, we may approximate the right-hand side of (2.8): 
1 
E[U(X)] M E u(x) + Zu’(z) + li2u‘’(z) 
2 
1 
= u(x) + E[Ell~‘(z) + -E[E12]u”(x) 
2 
‘lFor the sake of convenience, in this section we denote by E a random variable and by E 
a realization of that variable. This notation is common in Economics; in Statistics, one 
typically uses X and I with the corresponding pair of meanings. 

STOCK PO R TFO L 10 OP TlMlZA TlON 
69 
1 
2 
= ~ ( x )  
+ O . d ( x )  + -Var(E)d’(x) 
1 
2 
= U(X) + -ff2U1yx). 
In the second-to-last line we have used Var(2) = E[C2] - E2[E] = E[Z2] - 0. We 
may also approximate the left-hand side of (2.8), which only involves numbers, 
by a first-order expansion around E[X] = x: 
Equating both sides and rearranging yields 
1 U ” ( X )  
2 Ul(X) 
p u ( X )  = 
ff2 
Since we assume utility is concave and increasing, the right-hand side is pos- 
itive.” We may also see that the risk premium is factored as the product of 
one term depending on agent’s risk aversion and of another one depending 
on uncertainty. This justifies the definition of the coefficient of absolute risk 
aversion: 
(2.9) 
We have said that, given the linearity of the expectation operator, an (increas- 
ing) affine transformation of a utility function ~ ( x )  
is inconsequential. The 
definition of the risk-aversion coefficient is consistent with this observation, 
as it is easy to see that the coefficients for u(x) and au(z) + b are the same. 
Note that rt(x) does not depend on uncertainty, but it does depend on the 
expected value of the lottery. From an investor’s point of view, this implies 
that risk aversion depends on the current level of wealth. The more concave 
the utility function, the larger risk aversion. 
By the same token, we may define a coefficient of relative risk aversion. 
This is motivated by considering a multiplicative, rather than additive, shock 
on an expected value x: X = x(1 + 2). Using a similar reasoning, we get: 
1 U ” ( X )  
2 
p u ( X )  = 2 d(X) xff I 
which motivates the definition 
(2.10) 
12A useful property of differentiable concave function of one variable is u”(r) 5 0; see 
supplement S6.1. 

70 
NNANClAL THEORY 
Example 2.13 (A few standard utility functions) A typical utility 
function is logarithmic ~ t i l i t y ' ~ :  
u(x) = log(x) 
Clearly this makes sense only for positive values of wealth. It is easy to check 
that for the logarithmic utility we have 
1 
R E ( X )  = -, 
RL(X) = 1. 
X 
Hence, logarithmic utility has decreasing absolute risk aversion, but constant 
relative risk aversion. We say that logarithmic utility belongs to the families of 
DARA (decreasing absolute risk aversion) and CRRA (constant relative risk 
aversion) utility functions. We will see that this has important implications 
in portfolio optimization. 
Another common utility function is quadratic utility: 
A
2
 
u(x) = x - n x  . 
(2.11) 
L 
Note that this function is not monotonically increasing and makes only sense 
for x E [O,l/X]. Another odd property of quadratic utility is that it is IARA 
(increasing absolute risk aversion): 
> 0. 
x 2  
dR"(x) - 
x 
Rt(X) = - 
j 
- 
1 - Ax 
dx 
(1 -AX)' 
This is usually considered at odds with typical behavior of investors. Never- 
theless, we may also see that quadratic utility emphasizes the role of variance, 
since for this utility 
x 
x 
2 
2 
U(X) = E[X - -X2] = E[X] - - (Var(X) + E2[X]). 
A decision maker with quadratic utility is basically concerned only with the 
expected value and the variance of an uncertain outcome. We will see how 
quadratic utility is linked to mean-variance portfolio optimization. 
0 
Armed with the utility function concept, we may formalize portfolio optimiza- 
tion problems. In a single period portfolio optimization problem, we have an 
investor with given initial wealth Wo, which must be allocated to different 
assets, in such a way to maximize expected utility. Let t$ be the wealth in- 
vested in asset i = 1, . . . , n, and let Ri be the random return of the asset. The 
131n the following we will use the notation log, rather than In, to denote the natural loga- 
rithm. 

STOCK PORTFOLIO OPTIMIZATION 
71 
simplest formulation of the portfolio optimization problem is: 
n 
(2.12) 
The formulation is single-period, in the sense that no rebalancing is involved: 
a buy and hold strategy is assumed over the time period of interest. If short- 
selling is ruled out, we should also add non-negativity restrictions & > 0. It is 
common to include in the model a risk-free asset, whose return is deterministic, 
but this does not affect the form of the optimization model (it may affect the 
solution, of course). 
In general, we should not take for granted that the above optimization 
model has a solution. For instance, if the model of uncertainty is not ar- 
bitrage free, we may expect an unbounded solution exploiting the arbitrage 
opportunity. But for non-pathological cases, an optimal portfolio (not neces- 
sarily unique) exists. It is important to note that the optimal portfolio may 
depend on the initial wealth WO. Quite often, we may see models in which the 
decision variables are the weights wi 
&/Wo of each asset in the portfolio, 
and the budget constraint (2.12) is rewritten as 
n 
c w i  = 1. 
i=l 
The drawback of such a model formulation is that we do not see clearly the 
effect of initial wealth on the optimal solution. Since risk aversion depends 
on wealth, the optimal solution does depend on WO. There are exceptions, 
however, as shown by the following example. 
Example 2.14 Consider the following portfolio optimization problem: 
0 Uncertainty is modeled by a binomial distribution: There are two pos- 
sible states of the world in the future, the up and down state, with 
probabilities p and q, respectively. 
There are two assets: one is risk-free, the other one is risky. 
0 The risk-free asset has total return R f  in both states (total return is 
one plus interest rate). 
0 Current price for the risky asset is So and its total return is u in the 
up-state and d in the down-state. 
0 Initial wealth is Wo and the investor has logarithmic utility. 

72 
FINANCIAL THEORY 
In this problem, there is actually one decision variable, which we may take 
as 6, the number of stock shares purchased by the investor. To get rid of 
the budget constraint, we observe that 65’0 is the wealth invested in the risky 
asset, and WO - 6So is invested in the risk-free asset. Then, future wealth will 
be, for each of the two possible states: 
wu = 
w, 
6Sou + (Wo - 6SO)Rf = SSo(u - Rf) 
+ WORf 
6Sod + (WO - 6SO)Rf = 6So(d - Rf) + WORf, 
= 
and expected utility is plog(W,) + qlog(Wd). The problem is then 
A necessary condition for optimality is stationarity (the first-order derivative 
vanishes): 
So(u - Rf) 
So(d- Rf) 
= 0. 
P6so(u - Rf) + WORf + %o(d - Rf) + WORf 
In order to solve for 6, we may rewrite the equation a bit: 
SSo(u - Rf) + WORf - - 6S,(d - Rf) + WORf 
- 
PSO(U - Rf) 
qSo(d - Rf) 
Straightforward manipulations yield 
6 
WORf 
WORf - 
- -- - 
6 - +  
P 
PSo(u-Rf) 
q 
qSo(d-Rf) 
and 
WORf [q(d - Rf) 
f d u  - Rf)l 
and, finally 
-- 
&so 
Rf [UP + dq - Rf] 
Wo 
(. - Rf)(Rf - 4 .  
- 
This relationship implies that the fraction of initial wealth invested in the 
risky asset does not depend on the initial wealth itself. We have derived this 
property in a simplified setting, but it holds more generally for logarithmic 
utility, and is essentially due to its CRRA characteristic. 
0 
Specifying a utility function may be a difficult task, since assessing the trade- 
off between risk and return is far from trivial. This may be no concern in 
Economics, if the aim is to build a model explaining some observed behavior 
and qualitative insights are of interest; however, in Financial Engineering and 
operational decision making, this is a difficulty. A relatively simple approach 
is based on the idea of restricting the choice to “reasonable” portfolios. If you 

STOCK PORTFOLIO OPTlMlZATlON 
73 
fix the expected return you want to get from the investment, you would like 
to find the portfolio achieving that expected return with minimal risk. By 
the same token, if you fix the level of risk you are willing to take, you would 
like to select a portfolio maximizing the expected return. This approach 
leads to mean-variance portfolio theory, which, despite considerable criticism, 
underlies quite a significant part of financial theory. 
2.4.2 
Mean-variance portfolio optimization 
Let us go back to the asset allocation problem, when only two risky assets 
are available. Let us denote by F2, F , ,  and ui the random rate of return for 
asset i = 1 , 2  and its expected value and standard deviation respectively. It 
is tempting to say that the problem is trivial when 
> f 2  and 01 < ~ 7 2 .  In 
this case, stock 1 has a larger expected return than stock 2, and it is also 
less risky; hence, a naive argument would lead to the conclusion that asset 2 
should not be considered at all. Actually, this may not be the case, since we 
have neglected the possible correlation between the two assets. The inclusion 
of asset 2 may, in fact, be beneficial in reducing risk, if its return is negatively 
correlated with the return of asset 1. So we see that there is some need for 
formalization in order to solve the problem. 
Assume that we are interested in defining the portfolio weights, w1 and w2 
in our case. A natural constraint is 
w1+ w2 = 1. 
Note that we are not considering the initial wealth level Wo, since we deal 
with the allocation of fractions of wealth. If we want to rule out short-selling, 
we must also require wi 2 0. Elementary probability theory tells us that the 
portfolio rate of return will be 
r = W l F l +  W2F2, 
and the expected return will be 
F = w1r1 + w2F2, 
More generally, when we must devise a portfolio of n risky assets, the expected 
return is given by 
n 
a = ]  
The variance of F is given, for the two-asset case, by 
2 
o = Var(wlrl+ ~ 2 7 - 2 )  = w f ~ f  
+ 2 ~ 1 ~ 2 ~ 7 1 ~  
+ w,2u,2, 
where u12 is the covariance between r1 and 7-2. For n assets we have 
n 

74 
FINANCIAL THEORY 
where all covariances uij have been collected in the covariance matrix !Z. 
By choosing the weights wi, we will get different portfolios characterized 
by the expected value of the return and by its variance or standard deviation, 
which we may assume as a risk measure. Any investor would like both to 
maximize the expected return and to minimize variance. Since these two 
objectives are, in general, conflicting, we must find a trade-off. The exact 
trade-off will depend on the degree of risk aversion, which is hard to assess, 
but it is reasonable to assume that for a given target value FT of the expected 
return, one would like to minimize variance. This is obtained by solving the 
following optimization problem: 
min 
W'CW 
(2.13) 
i=l 
Wi 2 0 .  
This is a quadratic programming problem, which may be solved by numerical 
methods described in chapter 6, where we also show how to use MATLAB 
functions provided by the Optimization Toolbox. The Financial Toolbox also 
includes functions to solve mean-variance portfolio optimization problems, 
which are described in the next section. 
By changing the target expected return, one may obtain a set of eficient 
portfolios. Roughly speaking, a portfolio is efficient if it is not possible to 
obtain a higher expected return without increasing risk. There are infinite 
efficient portfolios in general, and it is reasonable to assume that the preferred 
portfolio will be one of them. 
2.4.3 
MATLAB functions to deal with mean-variance portfolio 
optimization 
MATLAB includes a set of functions based on mean-variance portfolio the- 
ory. They rely on the Optimization toolbox to solve optimization problem 
(2.13) for different values of expected return. The first function we consider 
is f rontcon. In the simplest case, f rontcon receives three arguments: the 
vector of expected rates of return, covariance matrix, and the number of effi- 
cient portfolios we wish to find. The last argument is actually the number of 
risk minimization subproblems we wish to solve; this yields a finite subset of 
the efficient frontier, which may be enough to trace a good plot. The output 
arguments are: a vector of expected portfolio risks (standard deviation) for 
each efficient portfolio; expected rates of return; portfolio weights for each 
asset in each portfolio. It is instructive to go back to the case of two assets. 
Assume the following data: 
F1 = 0.2 
r;! = 0.1 

STOCK PORTFOLlO O f  JlMlZAJlON 
75 
2 
a: = 0.2 
0 1 2  = -0.1. 
u2 = 0.4 
Note that asset 2 is apparently useless, but it is negatively correlated with 
asset 1; hence, when asset 1 performs poorly, we may hope that asset 2 will 
perform well (and vice versa). Hence, including asset 2 may result in some 
beneficial diversification. Let us find a set of efficient portfolios: 
>> r = CO.2 0.11; 
>> s = [0.2 -0.1; -0.1 
>> [PRisk, PRoR, PWts] 
>> [PWts, PRoR, PRisk] 
ans = 
0.6250 
0.3750 
0.6667 
0.3333 
0.7083 
0.2917 
0.7500 
0.2500 
0.7917 
0.2083 
0.8333 
0.1667 
0.8750 
0.1250 
0.9167 
0.0833 
0.9583 
0.0417 
1.0000 
0 
0.41 ; 
= frontcon(r,s,lO); 
0.1625 
0.2958 
0.1667 
0.2981 
0.1708 
0.3051 
0.1750 
0.3162 
0.1792 
0.3312 
0.1833 
0.3496 
0.1875 
0.3708 
0.1917 
0.3944 
0.1958 
0.4200 
0.2000 
0.4472 
Here we display a table showing expected rate of return, in the first column, 
standard deviation, and portfolio weights. Each line correspond to one of 
the ten portfolios we wanted to find. The last line correspond to the riskiest 
portfolio, yielding the largest expected return. As we could expect, return 
is maximized by investing 100% of our wealth in the first asset, with 
and 
01 = 
= 0.4472 (recall that we are forbidding short sales in this model). 
It is interesting to note that it is possible to obtain portfolios whose standard 
deviation of return is lower than the standard deviation of both assets, which 
is due to negative correlation between returns in this case. The first portfolio 
displayed in the first line corresponds to the portfolio of minimal risk. We may 
also plot the efficient frontier by calling f rontcon without output arguments: 
>> frontcon(r, s ,  10) ; 
We get the plot in figure 2.12. 
We may repeat the experiment with more complex portfolios: 
>> ExpRet = [ 0.15 0.2 0.081; 
>> CovMat = [ 0.2 0.05 -0.01 ; 0.05 0.3 0.015 ; . . .  
>> [PRisk, PRoR, PWts] = frontcon(ExpRet, CovMat, 10); 
>> [PWts, PRoR, PRisk] 
ans = 
-0.01 0.015 0.11; 

76 
FINANCIAL THEORY 
Mean-Variance-Efficient Frontier 
O 205 7-
0 16' 
I 
I 
I 
, 
i 
i 
i 
i 
028 
0 3  
032 
034 
036 
038 
0 4  
042 
044 
046 
Risk(Standard Deviation) 
fig. 2.12 Efficient frontier for a portfolio with two risky assets. 
0.2914 
0.3117 
0.3320 
0.3524 
0.3727 
0.3930 
0.4133 
0.3811 
0.1905 
0 
0.1155 
0.1831 
0.2506 
0.3181 
0.3857 
0.4532 
0.5207 
0.6189 
0.8095 
1.0000 
0.5931 
0.5052 
0.4174 
0.3295 
0.2417 
0.1538 
0.0659 
0 
0 
-0.0000 
0.1143 
0.1238 
0.1333 
0.1428 
0.1524 
0.1619 
0.1714 
0.1809 
0.1905 
0.2000 
0.2411 
0.2456 
0.2588 
0.2794 
0.3060 
0.3370 
0.3714 
0.4093 
0.4682 
0.5477 
By the way, we should not get fooled by the apparent negative weight of an 
asset in the last portfolio: 
>> PWts(l0,3) 
ans = 
-1.4461e-017 
This is a typical example of small numerical errors that we must expect. 
Like any professionally crafted code, f rontcon is safe in the sense that some 
consistency checks are carried out on the input arguments. For instance, a 
covariance matrix must be positive semidefinite. The reader is urged to try 
f rontcon with the following covariance matrix: 

STOCK PORTFOLIO OPTIMIZATION 
77 
CovMat = E0.2 0.1 -0. I ; 0.1 0.2 0.15 ; -0. I 0.15 0.21 
We have considered trivial portfolio optimization problems with no additional 
constraints. In real life, it is typical to have some constraints enforcing lower 
and upper bounds on the allocation to single assets or groups of assets. This 
may make sense if you want to limit the exposure to certain risky stocks or to 
market sectors (eg., telecommunications or energy). The f rontcon function 
is able to cope with such constraints, which may be represented by using 
additional arguments. However, a richer function, from this point of view, is 
portopt, which is able to cope with more general constraints. 
To illustrate, consider a problem involving five assets. Suppose that you 
do not want to consider short-selling and that the following upper bounds are 
given on each asset weight in the portfolio: 
0.35 
0.3 
0.3 
0.4 
0.5. 
Furthermore, the assets can be partitioned into two groups, consisting of assets 
1 and 2 and of assets 3, 4, and 5, respectively. You might wish to enforce 
both lower and upper bounds on asset allocation to each group; say the lower 
bounds are 0.2 and 0.3 and the upper bounds are 0.6 and 0.7. Formally, this 
would result in a constraint set like the following, which should be added to 
our quadratic programming problems: 
0 5 WI 5 0.35 
0 5 ~4 5 0.4 
0.2 5 201 + w:! 5 0.6 
0.3 5 ~3 + ~4 + ws 5 0.7. 
0 5 ~2 5 0.3 
0 5 ~3 5 0.3 
0 5 ws 5 0.5 
The optimization functions available in MATLAB can easily cope with such 
constraints, but they must be represented in matrix form. In other words, it is 
customary to specify (linear) constraints as systems of equations Aeqw = be, 
or inequalities Aw 5 b. Writing constraints in such a form is conceptually 
simple, but practically difficult. In the past, persons working on numerical 
optimization had to write matrix generators in order to solve large problems 
by numerical libraries. Then, to ease a tedious and error-prone task, algebraic 
languages have been developed, such as AMPL, which is used in chapters 11 
and 12 (see also appendix C). Algebraic languages allow us to express an 
optimization model in a quite natural way. In MATLAB there is no high- 
level way to express optimization models, but for mean-variance problems 
there is a sort of specialized matrix generator, called portcons. 
For our small example, we would call this function as illustrated in figure 
2.13, obtaining the constraint matrix in figure 2.14.14 Note that we must 
"We should note that frontcon can also be used for such a problem, but we prefer using 
portcons and portopt to illustrate a more general point related to matrix generators. 

78 
FlNANClAL THEORY 
% Cal1Portcons.m 
NAssets = 5; 
AssetMin = NaN; 
AssetMax = 10.35 0.3 0.3 0.4 0.51; 
Groups = [l 1 0  0 0 ; 0 0 1 1 11; 
GroupMin = [ 0.2 0.3 1; 
GroupMax = [ 0.6 0.7 1 ; 
ConstrMatrix = portcons(’Default’, NAssets, ... 
’AssetLirns’, AssetMin, AssetMax, NAssets, ... 
’GroupLirns’, Groups, GroupMin, GroupMax) 
~~~~ 
~~ 
~ 
Fig. 2.13 How to use portcons to build the constraint matrix 
ConstrMatrix = 
1.0000 
1.0000 
-1.0000 
-1.0000 
-1.0000 
0 
0 
-1.0000 
0 
0 
0 
0 
0 
0 
1.0000 
0 
0 
1.0000 
0 
0 
0 
0 
0 
0 
-1.0000 -1.0000 
0 
0 
1.0000 
1.0000 
0 
0 
1.0000 
-1.0000 
0 
0 
-1.0000 
0 
0 
0 
0 
1.0000 
0 
0 
0 
-1.0000 
0 
1.0000 
1.0000 
-1.0000 
0 
0 
0 
-1.0000 
0 
0 
0 
0 
1.0000 
0 
0 
-1.0000 
0 
1.0000 
1.0000 
-1.0000 
0 
0 
0 
0 
-1.0000 
0 
0 
0 
0 
1.0000 
0 
-1.0000 
0 
1.0000 
1.0000 
-1.0000 
0 
0 
0 
0 
0 
0.3500 
0.3000 
0.3000 
0.4000 
0.5000 
-0.2000 
-0.3000 
0.6000 
0.7000 
Fig. 2.14 Sample constraint matrix built by portcons. 

STOCK PORTFOLlO OPTlMlZATlON 
79 
Ca1lPortopt.m 
CallPortcons; 
ExpRet = C0.03 0.06 0.13 0.14 0.151; 
CovMat = [ 
0.01 
0 
0 
0 
0 
0 
0.04 -0.05 
0 
0 
0 
-0.05 
0.30 
0 
0 
0 
0 
0 
0.40 
0.20 
0 
0 
0 
0.20 
0.40 1; 
[PRisk, PRoR, PWts] = portopt (ExpRet , CovMa 
[PRoR, PRisk] 
PWt s 
, 10, [I, ConstrMa cix) ; 
Fig. 2.15 Calling portopt. 
include a 'Default' argument in order to specify that the sum of weights 
does not exceed 1 and short selling is ruled out. This is why we use NaN 
(not-a-number) as a lower bound on asset allocation AssetMin: otherwise, we 
would have twice the same constraints w, 2 0. Also note how the equality 
constraint Cz=l 
wz 
= 1 is represented by two inequalities, x:=l 
w, 5 1 and 
z:=l 
(-wz) 5 -1. This is because portopt assumes inequality constraints 
only. Then the matrix may be used by calling portopt as illustrated in figure 
2.15 (some optional arguments are omitted; see MATLAB online help). 
5 
Using that script, we get the following output: 
ans = 
0.0816 
0.0860 
0.0904 
0.0948 
0.0991 
0.1035 
0.1079 
0.1122 
0.1166 
0.1210 
PWts = 
0.3000 
0.2623 
0.2220 
0.1816 
0.1413 
0.1487 
0.1620 
0.1762 
0.1906 
0.2054 
0.2203 
0.2361 
0.2526 
0.2799 
0.3995 
0.3000 
0.2250 
0.0875 
0.0875 
0.3000 
0.2309 
0.0905 
0.1163 
0.3000 
0.2496 
0.0998 
0.1286 
0.3000 
0.2683 
0.1091 
0.1410 
0.3000 
0.2870 
0.1185 
0.1533 

80 
FlNANClAL THEORY 
0.1017 
0.3000 
0.3000 
0.1299 
0.1684 
0.0639 
0.3000 
0.3000 
0.1463 
0.1899 
0.0260 
0.3000 
0.3000 
0.1627 
0.2113 
0.0000 
0.3000 
0.2650 
0.1075 
0.3275 
0 
0.3000 
0 
0.2000 
0.5000 
It is useful to check that the maximum return portfolio allocates 50% of wealth 
to asset 5, which is the maximum return asset; the upper bound wg 5 0.5 
prevents us from investing all of our wealth in this asset. Then 20% is allocated 
to asset 4 and nothing to asset 3, because wg + w4 + w5 5 0.7. The last 30% 
is allocated to asset 2. 
Another consideration we should point out is that portcons generates a full 
matrix with many zero entries. Good optimization solvers deal with sparse 
matrices, which avoid storing zero entries in order to save memory space. 
Algebraic languages exploit this possibility, which is essential to deal with 
large-scale problems with special structure. 
A last function we describe here may be used to find an optimal portfolio. 
So far, we have dealt with efficient portfolios, leaving the risk/return trade-off 
unresolved. We may resolve this trade-off by linking mean-variance portfolio 
theory to the more general utility theory illustrated in section 2.4.1. Actually, 
mean-variance theory is not necessarily compatible with an arbitrary utility 
function: An optimal portfolio for some utility function need not be on the 
mean-variance efficient frontier. It can be shown that this inconsistency does 
not arise if the returns are normally distributed or if the utility function is 
quadratic (see, e.g., [ll] or [15]). The last point implies that if may specify a 
quadratic utility function such as (2.11), the optimal solution will be a mean- 
variance efficient portfolio. All we have to do is to choose the X parameter 
according to our degree of risk aversion. In the Financial toolbox the function 
portalloc is provided, which yields the optimal portfolio assuming quadratic 
utility with some risk-aversion parameter; its default value is 3 and suggested 
alternative values range between 2 and 4. There is still another issue that we 
have neglected so far. We have considered mean-variance efficient portfolios, 
assuming that only risky assets were available. However, we may obtain a 
known return by investing in a bank account with a fixed interest rate or in 
a safe zero-coupon bond (with maturity equal to our investment horizon, to 
avoid interest rate risk issues). What is the effect of the inclusion of such 
a risk-free asset in our portfolio? A detailed analysis of this issue is rich in 
implications in financial theory, but it would lead us too far. For our purposes 
it is sufficient to say that the optimal portfolio will be a combination of the 
risk-free asset and one particular efficient portfolio. The amounts invested in 
the risk-free asset and in the risky portfolio depend on our risk aversion, but 
the risky portfolio involved does not. An important implication of this, if we 
believe in the theory, is that investors could live with just one “mutual” fund, 
mixing it with the risk-free asset. The p o r t a l l oc  function yields the optimal 
combination of the risky portfolio and the risk-free asset; it assumes further 

STOCK PORTFOLlO OPTlMlZATlON 
81 
% CallPortAl1oc.m 
ExpRet = [ 0.18 0.25 0.21; 
CovMat = [ 0.2 0.05 -0.01 ; 0.05 0.3 0.015 ; ... 
RisklessRate = 0.05; 
BorrowRate = NaN; 
RiskAversion = 3; 
-0.01 0.015 0.11; 
[PRisk, PRoR, PWts] = frontcon(ExpRet, CovMat, 100) ; 
[RiskyRisk , RiskyReturn, RiskyWts. RiskyFraction, . . .  
PortRisk, PortReturn] = portalloc(PRisk, PRoR, PWts, ... 
AssetAllocation = [I-RiskyFraction, RiskyFraction*RiskyWts] 
RisklessRate, BorrowRate. RiskAversion); 
Fig. 2.16 Calling portalloc. 
that cash may be borrowed at some rate. Figure 2.16 illustrates a script to 
call this function. 
Some explanation is in order. First, we give the vector of the expected 
rates of return and the covariance matrix, which are used by frontcon to 
generate an approximation of the efficient frontier with a given number of 
points. We also give a riskless rate (for investing) and a risk-aversion coeffi- 
cient. The borrowing rate is set to NaN since we do not consider the possibility 
of borrowing. There are several output returned by portalloc: RiskyRisk, 
RiskyReturn, and RiskyWts are the risk, the expected return, and the com- 
position of the ideal fund. RiskyFraction is the fraction we should invest in 
the risky portfolio; PortRisk and PortReturn are the risk and return of the 
portfolio consisting of the risky portfolio and the risk-free asset. 
Callingportalloc with these parameters will produce the following output: 
>> CallPortAlloc 
AssetAllocation = 
0.1401 
0.2004 
0.1640 
0.4954 
One could wonder why we should compute first the efficient frontier. In 
fact, this is due to the way portalloc is built. We can formulate and solve an 
optimization problem directly, using the concepts we will illustrate in chapter 
6 (see also section C.2). 
2.4.4 
Critical remarks 
Mean-variance portfolio theory leads to relatively simple numerical problems. 
However, despite its prominent role in financial theory, the approach has been 

82 
FINANCIAL THEORY 
the subject of widespread criticism. We have pointed out that mean-variance 
portfolio theory is consistent with the utility function framework in the case 
of normally distributed returns and in the case of a quadratic utility function. 
Both conditions may be debated.15 
One important feature of the normal distribution is its symmetry. If the 
return distribution is symmetric, then using variance or standard deviation as 
a measure of risk may make sense; in fact, variance takes into account returns 
that are both higher and lower than the average. The former are actually 
desirable, but in the case of normal distribution a potential for good perfor- 
mance is exactly counterbalanced by the risk of underperformance. However, 
if the distribution is not symmetric, we must distinguish the upside potential 
from the downside risk. While symmetric returns may be assumed for stocks, 
derivative assets, such as those we shall describe shortly, may lead to more 
complex distributions. As for the quadratic utility function, we have seen that 
it implies increasing absolute risk aversion, which is itself a counterintuitive 
behavior for the usual investor. A solution to both issues would be the use of a 
carefully chosen utility function, which is hard to come up with, when dealing 
with real investors. We could also enforce constraints on the probability of 
large losses; if L is the random variable modeling the portfolio loss, we could 
require something like 
P{L > w} 5 a, 
where a is a small probability and w is a threshold parameter; such a prob- 
abilistic constraint is known as chance constraint. All of these ideas lead to 
more complex optimization problems, namely stochastic programming prob- 
lems, which are dealt with in chapter 11. 
A further reason for using stochastic programming models is another dif- 
ficulty in mean-variance theory. The covariance matrix is assumed to be 
constant over time. Unfortunately, it is likely that correlation may rise when 
stock market crashes occur, just when diversification should help. So we 
should use more complex models in describing the uncertainty. Stochastic 
programming does so by building a set of multiperiod scenarios, like the tree 
in figure 2.3 on page 27. This also enables us to consider another feature 
that is disregarded by mean-variance models: the dynamic nature of portfolio 
management, which is not considered in single-period models. Portfolios are 
revised in time, and the impact of transaction costs should not be neglected. 
Modeling transaction costs exactly may be rather difficult. They depend in 
a non-trivial way on the amounts traded. For instance, it may be preferable 
to buy and sell stocks in round lots, since trading in odd lots may increase 
transaction costs. It might also be advisable to avoid a portfolio with a very 
15See, e.g., [13] for a discussion of alternative utility functions in portfolio optimization. 
We should also mention that mean-variance theory is justified not only when returns are 
assumed normally distributed, but in the more general case of elliptic distributions, which 
include the normal; see [ll]. 

STOCK PORTFOLIO OPTIMIZATION 
83 
small weight on some assets; the benefit of diversification will probably be lost 
because of increasing transaction costs. So we could require that if a stock 
enters the portfolio, it does so with a minimal weight. We may also look for 
portfolios including no more than a predetermined number of assets. Such 
constraints require the introduction of integer programming models, which 
are the subject of chapter 12. 
2.4.5 
Alternative risk measures: Value at Risk and quantile-based 
measures 
Mean-variance portfolio theory is based on the use of variance or standard 
deviation as risk measures. We have already pointed out that this may not be 
always appropriate, but another practical issue is that they may be difficult 
to interpret by a portfolio manager. This is why alternative risk measures 
have been proposed and adopted, based on the concept of a portfolio loss. In 
general, a risk measure is a function mapping a random variable to a number; 
the larger this number, the riskier the distribution. More specifically, some 
measures are based on quantiles of the probability distribution of portfolio 
loss. The most widely known such measure is Value at Risk, or VaR (not to 
be confused with variance or, for people with a background in Econometrics, 
with a Vector Auto-Regressive, VAR, model). 
The VaR concept was introduced as an easy-to-understand measure of port- 
folio risk. In fact, measuring, monitoring, and managing risk are fundamental 
activities for any portfolio manager. Bonds and stocks involve different forms 
of risk, and derivatives, if used for speculation, may be even riskier. Basically, 
VaR aims at measuring the maximum portfolio loss one could suffer, over a 
given time horizon, within a given confidence level. Technically speaking, it is 
a quantile of the probability distribution of future wealth. Suppose that our 
initial wealth is Wo and the future (random) wealth is, at the end of the time 
horizon, 
where i: is the random rate of return. We are interested in characterizing the 
potential loss, which occurs when the wealth increment 
w = Wo(1 + T), 
6W = w - w, 
= WoT 
turns out to be negative. The VaR at confidence level a is implicitly defined 
by the following condition: 
P(6W 5 -VaR} = 1 - a, 
(2.14) 
which shows that VaR is, disregarding the change in sign to make it positive, 
a quantile with confidence level a. Typical values for the confidence level 
could be a = 0.95 or a = 0.99. To be precise, the definition above holds 
for a continuous probability distribution, but it can be extended to a discrete 
probability distribution. 

84 
FINANCIAL THEORY 
Let f (r) be the probability density of the rate of return. Then we should 
look for a critical rate of return rl--a such that 
T* 
P{F 5 
= 
f(r) dr = 1 - a. 
L 
The quantile ~1~~ is obviously linked to a critical wealth ~
1
-
~
,
 
since from 
equation (2.14) we may deduce 
W I - ~  
- WO = -VaR, 
which in turn implies 
VaR = WO - 
= -WOrl--a. 
Note that the critical return is usually negative and VaR is positive. Some- 
times VaR is defined with respect to the expected future wealth: 
VaR = E[W] - ~
1
-
~
 
= - W ~ ( r l - ~  
- E[R]). 
The two definitions may give approximately the same value for a short time 
horizon, say a few days. In this case volatility dominates drift16 and E[W] M 
WO. This assumption is not unreasonable, as regulations suggest using a risk 
measure in order to set aside enough cash to be able to cover short-term losses. 
Computing VaR is easy if one assumes that returns are normally distributed 
and we are considering short time periods, so that the rate of return over a few 
successive periods is the sum of returns on each period (i.e., the compounding 
effect is negligible). For simplicity, assume that we hold N shares of an asset 
whose current price is S. Let u be the daily volatility for that asset; hence, for 
a period of length bt days, volatility is u f i ,  if we assume daily returns are 
independent on each other. Since, by summing normal random variables, we 
get another normal variable, the return over the time period bt is normal too, 
and to get the quantile we need we may standardize as usual. Hence, given a 
confidence level a, we have to obtain the quantile ~
1
-
~
 
of the standard normal 
distribution by inverting its cumulative distribution function. For instance, if 
a is 99% and 95%: 
>> z = norminv( LO.01 0.051, 0 ,  1) 
z =  
-2.3263 
-1.6449 
16The terms “volatility” and “drift” will be clarified in the next sections on stochastic 
differential equations. Intuitively, drift is related to expected return and volatility is related 
to standard deviation. On a short time interval of length 6t, drift scales linearly with 6t, 
whereas volatility is proportional to a, 
which means that when the time interval tends 
to zero, drift goes to zero faster than volatility. 

STOCK POR TFOL 10 0 P TI M IZA TI0 N 
85 
For the VaR over the time period 6t, with a confidence level a, we have 
VaR = - z ~ - ~ ~ & N S ,  
(2.15) 
where the term NS is the current wealth W,. If the time horizon is longer, 
we should not neglect the drift due to the expected return. In such a case, we 
should modify (2.15) as follows: 
VaR = NS(p6t - Z I - ~ U ~ ) ,  
where p is the expected daily return. For a portfolio of assets, computing VaR 
is again easy if normality is assumed. We have just to evaluate the portfolio 
risk as in mean-variance theory. 
Example 2.15 Suppose that we hold a portfolio of two assets. The portfolio 
weights are w1 = 213 and w2 = 113, respectively; the two daily volatilities are 
u1 = 2% and u2 = 1%, and the correlation is p = 0.7. Let the time horizon 
6t be 10 days. To obtain the portfolio risk, we compute the variance: 
hence u = 0.05011. Assuming that the overall portfolio value is $10 million, 
and that the confidence level is 99%, 
Var = lo7 .2.3263. 0.05011 = $1,165,709. 
The same result can be obtained by using the MATLAB functions portstats 
and portvrisk. The first one, given the expected return vector for each asset, 
the covariance matrix, and the portfolio weights, computes the portfolio risk 
and the expected return: 
[PRisk, PReturn] = portstats (ExpReturn, CovMat, Wts). 
The second one computes the VaR, given the expected portfolio return, its 
risk, the risk threshold 1 - Q, and the portfolio current value: 
VaR = portvrisk(PReturn, PRisk, RiskThreshold, PValue) 
Using these functions, we get 
>> 
>> 
>> 
>> 
>> 
>> 
>> 
format bank 
si = 0.02 * sqrt(l0); 
s2 = 0.01 * sqrt(l0); 
rho = 0.7; 
CovMat = [ sl-2 rho*sl*s2 ; rho*sl*s2 s2-21; 
s = PortStats([O 03, CovMat, [2/3 1/31); 
var = portvrisk(0,s,0.01,10000000) 

86 
NNANClAL THEORY 
var = 
1165755.90 
Note that the previous result was a bit different because of truncation errors 
in the pencil-and-paper calculation. 
0 
The general formula for a portfolio of n assets with current price Si, i = 
1,. . . , n, daily volatility c i ,  correlation pij between assets i and j ,  where we 
hold a number Ni of shares for each asset is 
I 
n. 
n 
Needless to say, this formula holds if normality is assumed. But what if the 
assumption is not warranted? Indeed, empirical data do not suggest that 
stock returns are normally distributed. Furthermore, we may have to deal 
with assets which depend on risk factors, and even if a risk factor is normally 
distributed, non-linear dependence of the price with respect to the underlying 
factor will destroy normality. A familiar example is the non-linear dependence 
of a bond price with respect to required yield. In this case, however, if we 
recall equation (2.6), we may settle for a duration-based approximation like 
6P 
DM P 6X. 
Hence, if 6X is normally distributed, 6P will be too, and normality holds 
approximately. Similar considerations apply in the case of derivatives, if we 
are able to compute suitable sensitivities of the price of the derivative with 
respect to the price of the underlying asset. 
If we look for a better approximation, we must give up normality and deal 
with the consequences. Indeed, in this case there are many issues. To begin 
with, we cannot find the quantile of the wealth distribution by looking at 
the quantile of the standard normal distribution. In this case, a numerical 
solution can rely on Monte Carlo simulation (see chapter 4). A thornier issue 
concerns the way we model the dependence among the different risk factors. 
In fact, correlation tells the whole story when normality is assumed, but not in 
general. This requires the adoption of more sophisticated statistical models, 
such as copula theory, which is beyond the scope of this book (see references). 
Even if we leave all such modeling and computational issues aside, and we 
assume that we can compute VaR, there is something wrong with the VaR 
concept itself. For instance, a quantile cannot distinguish between different 
distributions. Consider figure 2.17. The plot on the left shows the normal 
case; if we assume a sort of truncated distribution like the one on the right, 
VaR will be the same, since the area under the density function to its left is 
the same. However, the potential loss in the second case is quite different. 
In particular, it is different the expected value of loss conditional on being 

STOCK PORTFOLIO OPTIMIZATION 
87 
oii t,lic lcft, (iiiilucky) 
of the portfolio value tlistribut,ioii. This hiis let1 t.o 
tlie drfinit~ion of alt,ernative risk nieasIirrs, such as Conditional Value at. Risk 
(CVttR). wliich is tlic cxpcct,cd valnt: of loss, coriditional on being to tlie left 
of VaR. 
R h k  mcasures like VaR. or CVaR could be also used in portfolio optimiza- 
tioii by solving opt,irnization probleins with t,he same structure as 2.13, with 
variance replaced tjy such measures. The resulting problem can be rather 
coiiiplcx. In particular it, may lack coiivexity properties that arc so important 
in 1111Iileri(:id optimization (see c:liapter 6). It tunis out that mininiizirig VaR 
wh(w unccrt,aiiity is motlrled hy a finite set of scenarios (which may hc usrful 
t,o cill)tlirc coiiiplcx tlist,rit)iit,ioiis iilld dcpcndcncies aiiioiig asset priccs) is it 
Iliist,Y iioii-convex probleni, whereas mininiizing CVaR is (numerically) easier. 
Tliero is on(! hst issiic with VaR that deserves mention. Intuitively, risk 
is rctluc:e:tl by diversificat,ion. This should be reflected by any risk measure 
p ( . )  we consider. A little inore fornially, we should require a subadditivity 
wntlitioii likc 
P(A + B )  5 P(A) + P(B), 
wliere ,4 ant1 B arc taw portfolio positioiis. The following counter-example is 
oftw iisc.tl t,o show that ViiR lack this propcrty. 
Example 2.16 Lct us consider two corporate t)oiids; A and B, whose issucrs 
niay tfefaiilt wit,h probability 4%. Say that, in thc case of default, we lose $100 
(in practice. we might partially recover the face value of the bond). Let 11s 
coinputc thc VaR of each bond with confidence level 95%. 
Before doing so: we should clarify what Van is, when uncertainty is riiodeled 
I)y a discwt,e distribution. Definition (2.14) can be extended by defining Van 
its t , l i ~  srnollc.sl vdlic 7 sticll tliat, 
P(0W 5 -7) 2 1 -a. 
Basic:ally, with il tliscret,c’ distribution we niay not find a value such that 
cyuatioii (2.14) is satisfied aiid we must resort to an inequality. Since default 
proi)itl)ilit,v is oiily 4%: and 1 - 0.04 = 0.96 > 0.95, we have in our case 
VaR(A) = VaR(l3) = VaR(A) + VaR(B) = 0. 
ain
Fig. 2.17 Value at risk can be the same in different cases.

88 
FINANCIAL THEORY 
Now what happens if we hold both bonds, and assume independent defaults? 
We will suffer 
0 a loss 0, with probability 0.962 = 0.9216; 
0 a loss 200, with probability 0.042 = 0.0016; 
0 a loss 100, with probability 2 x 0.96 x 0.04 = 0.0768. 
Hence, with that confidence level, VaR(A + B) = 100 > VaR(A) + VaR(B), 
which means that diversification increases risk, if we measure it by VaR. 
0 
Subadditivity is one of the properties that sensible risk measures should 
enjoy. The term coherent risk measure has been introduced to label a risk 
measure that meets a set of sensible requirements. VaR is not a coherent risk 
measure, whereas it can be shown that CVaR is. 
2.5 
MODELING THE DYNAMICS OF ASSET PRICES 
In mean-variance portfolio theory we have considered a buy-and-hold portfo- 
lio. Hence, we were not interested in modeling the dynamics of asset prices, 
but only the distribution of return at the end of a given time interval. For 
more complex portfolio management models, we do need a dynamic model of 
asset prices. This is also required to solve option pricing models, as we will 
see in section 2.6. A model of the dynamics of asset prices must reflect the 
random nature of price movements, and the asset price S(t) must be described 
as a stochastic process. This could be a discrete- or a continuous-time pro- 
cess. It turns out that for option pricing purposes, a continuous-time model is 
most useful, based on random walks. In this section with deal with modeling 
asset prices as stochastic processes in continuous time, which will lead us to 
consider stochastic differential equations and stochastic integrals. 
2.5.1 
From discrete to continuous time 
It is a good idea to start with a discrete-time model and then derive a 
continuous-time model. Consider a time interval [0, TI, and imagine that 
we discretize the interval with a time step 6t such that T = N ' 6t; we may 
index the discrete-time instants by t = 0,1,2,. . . , N .  Let St be the stock price 
at time t. One possible and reasonable model is the multiplicative form: 
St+l = WStr 
(2.16) 
where ut is a nonnegative random variable and the initial price So is known. 
If we consider continuous random variables ut, the model is continuous-state. 
The random variables ut are assumed identically distributed and independent. 

MODELING THE DYNAMICS OF ASSET PRICES 
89 
Independency is an assumption linked to market efficiency. Under this (debat- 
able and debated) assumption, current prices reflect all information available 
so far. 
The multiplicative model is reasonable since it ensures that prices will stay 
nonnegative, which is an obvious requirement for stock prices. If we used an 
additive model such as St+l = ut + S,, we should admit negative values for 
the random variables ut to model price drops, and we would not have the 
guarantee St 2 0. With the multiplicative form, a price drops when ut < 1, 
but it stays positive. Furthermore, the actual price change depends on the 
present stock price (a $1 increase is different if the present price is $100 rather 
than $ 5 ) ,  and this is easily accounted for by the multiplicative form. 
In order to determine a plausible probability distribution for the random 
variables ut, it is helpful to consider the natural logarithm of the stock price: 
logSt+1 =logSt+logut=logSt+zt. 
The random variable .zt is the increment in the logarithm of price, and a 
common assumption is that it is normally distributed, which implies that ut 
is 10gnormal.l~ Starting from the initial price SO and unfolding (2.16), we get 
t-I 
k=O 
which implies that 
t-1 
log st = log SO + c 
zk. 
k=O 
Since the sum of normal random variables is still a normal variable (see ap- 
pendix B), we have that logst is normally distributed, which in turn implies 
that, according to this model, stock prices are lognormally distributed. Using 
notation 
E[ztI = V, 
Var(zt) = 2, 
we see that 
t-1 
E[logSt] = E logs0 4- 
zk 
[ 
k=O 1 
t-1 
= l O g S o + ~ E [ z k ]  
=log&+Ut 
(2.17) 
k=O 
/ 
t-1 
\ 
t-1 
171f X is a normal random variable, then taking the exponential exp(X) yields a lognormal 
random variable; see appendix B. 

90 
NNANClAL THEORY 
where intertemporal independence of zt is used in computing variance. The 
important point to see here is that the expected value and the variance of the 
increment in the logarithm of the stock price scale linearly with time; this 
implies that the standard deviation scales with the square root of time. 
The next step is to obtain a model in continuous time. In the deterministic 
case, when you take the limit of a difference equation, you get a differential 
equation. Informally, in the deterministic case, we may recast what we have 
seen in discrete time as 
6 logS(t) = log S(t + 6t) - log S(t) = u 6t 
(note that we are basically working with the expected values, since for the 
moment we do not include randomness). If we take the limit as 6t -+ 
0, we 
obtain: 
dlogS(t) = v dt. 
Integrating both differentials over the interval [0, t] yields 
This is coherent with the discrete time result. Actually, in the deterministic 
case, it is customary to write the differential equation as 
d log S( t) 
dt 
= v  
or, equivalently, as 
= VS(t), 
dt 
where we have used calculus to rewrite the differential 
(2.20) 
We see that u is linked to the continuously compounded return of the asset. 
that we should write the equation in the form 
When we include noise, there are a few important changes. The first, is 
dlogS(t) = v d t + a d W ( t ) ,  
(2.21) 
where dW(t) can be considered as the increment of a stochastic process over 
the interval [t,t + dt]. This is a rather tricky object, called a stochastic dzf- 
ferential equation. It is reasonable to guess that the solution of a stochastic 
differential equation is a stochastic process, rather than a deterministic func- 
tion of time. However, this topic is quite difficult to deal with rigorously, as it 
requires some background in measure theory and stochastic calculus (see the 
references at the end of the chapter). We will limit ourselves to a reasonably 
detailed treatment. 

MODELING THE DYNAMICS OF ASSET PRICES 
91 
The first thing we need is to investigate which type of continuous-time 
stochastic process W ( t )  we can use as a building block. In the next section 
we introduce such a process, called the Wiener process, which plays more or 
less the same role as process zt above. It turns out that this process is not 
differentiable, whatever this may mean for a stochastic process. Hence, we 
cannot write the stochastic differential equation as 
d log S(t) 
dW(t) 
=v+a- 
d t  
dt 
’ 
Actually, a stochastic differential equation must be interpreted as a shorthand 
for an integral equation much like (2.19), involving increments of a stochastic 
process. This calls for the definition of a stochastic integral and the related 
stochastic calculus. A consequence of the definition of the stochastic integral 
is that working with differentials as in equation (2.20) is not possible. We 
need a way to generalize the chain rule for differentials from the deterministic 
to the stochastic case. This leads to a fundamental tool of stochastic calculus 
called Ito’s lemma. 
2.5.2 
Standard Wiener process 
In the discrete-time model, we have assumed normally distributed increments 
in logarithmic prices, and we have also seen that the expected value of the 
increment of the logarithm of price scales linearly with time, whereas standard 
deviation scales with the square root of time. 
In discrete time, we could consider the following process as a building block: 
Wt+l = wt + Et&, 
where E t  is a sequence of independent standard normal variables. We see that, 
for Ic > j ,  
k - l  
.
.
 
a =J 
which implies that 
Passing to continuous time, we may define the standard Wiener process as 
a continuous-time stochastic process characterized by the following properties. 
1. W(0) = 0, which is actually a convention. 
2. Given any time interval [s, tIl the increment W ( t )  - W ( s )  is distributed 
as N(0, t - s), a normal random variable with zero expected value and 

92 
FINANCIAL THEORY 
fig. 2.18 Sample paths of a “degenerate” stochastic process. 
standard deviation fi. 
Increments are stationary, as they do not 
depend on where the time interval is, but only on its width. 
3. Increments are independent: If we take time instants tl < t 2  5 t 3  < 
t 4 ,  then W(t2) - W(t1) and W(t4) - W(t3) are independent random 
variables. 
To see the importance of the independent increments assumption, let us com- 
pare the sample path of the Wiener process, which was shown in figure 2.5 
on page 29, with the sample paths of a process defined as Q(t) = e d ,  with 
e - N(0, l), which are shown in figure 2.18. This is a “degenerate” stochastic 
process, since knowledge of one point on a sample path implies knowledge of 
the whole sample path, which makes the process quite predictable. However, 
if we just look at the marginal distribution of Q(t), it seems just like the 
Wiener process, since 
E[Q(t)l = 0 = E[W(t)l 
Var[Q(t)] = t = Var[W(t)]. 
It is lack of independence that makes the difference. From figure 2.5, we also 
see that sample paths of the Wiener process look continuous, but not differ- 
entiable. This may be stated precisely, but it is not very easy. Introducing 
continuity and differentiability rigorously calls for specifying some concept of 
stochastic convergence. In fact, we should say that the Wiener process is 
nowhere differentiable with probability 1. To get an intuitive feeling for this 
fact, let us consider the incremental ratio: 
dW(t) - W(t + dt) - W(t) 
-- 
bt 
dt 

MODELING THE DYNAMICS OF ASSET PRICES 
93 
Given the above properties, it is easy to see that 
Var [W(t + 6t) - W(t)] - 1 
_ -  
(W2 
bt . 
Var (T) 
= 
If we take the limit for 6t --+ 0, this variance goes to infinity. Strictly speaking, 
this is no proof of non-differentiability of W(t), 
but it does suggest that there 
is some trouble in using something like dW(t)/dt; indeed, you will never see a 
notation like this. We only use the differential dW(t) of the Wiener process. 
Informally, we may think of d W ( t )  as a random variable with distribution 
N(0, dt). Actually, we should think of this differential as an increment, which 
may be integrated as follows: 
dW(7) = W(t) - W ( S ) .  
This looks reasonable, doesn’t it? We may even go further and use W ( t )  as 
the building block of stochastic differential equations. For instance, given real 
numbers a and b, we may imagine a stochastic process X ( t )  satisfying the 
equation 
d X ( t )  = adt + b dW(t). 
This is a generalized Wiener process and straightforward integration yields 
X ( t )  = X ( 0 )  + at + bW(t). 
d X ( t )  = a(t, X ( t ) )  d t  + b(t, X ( t ) )  dW(t) 
But if we consider something more complicated, like 
(2.22) 
things are not that intuitive. A process satisfying an equation like (2.22) is 
called an Ito process. We could argue that the solution should be something 
like 
(2.23) 
Here the first integral looks like a standard Riemann integral of a function over 
time, but what about the second one? We need to assign a precise meaning 
to it, and this leads to the definition of a stochastic integral. 
t 
~ ( t )  
= X ( O )  + 1 a(s, ~ ( s ) )  
ds + 
b(7, ~ ( 7 ) )  
d ~ ( 7 ) .  
I” 
2.5.3 
In a stochastic differential equation defining a process X ( t ) ,  where a Wiener 
process W ( t )  is the driving factor, we may assume that the value X ( t )  depends 
only on the history of W(t) over the time interval from 0 to t. Technically 
speaking, we say that process X ( t )  is adapted to process W(t). Now let us 
consider a stochastic integral like 
Stochastic integrals and stochastic differential equations 

94 
FINANCIAL THEORY 
How can we assign a meaning to this expression? To begin with, it is rea- 
sonable to guess that a stochastic integral is a random variable. If we inte- 
grate a deterministic function of time we get a number; so, it is natural to 
guess that, by integrating a stochastic process over time, we should get a ran- 
dom variable. Furthermore, the stochastic integral above looks related to the 
sample paths of process W(t), and an approximation could be obtained by 
partitioning the integration interval in small subintervals by selecting points 
0 = to, tl, t 2 , .  . . , tn = T and considering the sum 
n-1 
X(tk) [W(tk+l) - W(tk)] 
* 
(2.24) 
k=O 
It is very important to notice how we select the time instants in the expression 
above: X ( t k )  is a random variable which is independent from the increment 
W(tk+l) - W(tk) by which it is multiplied. This is actually one possible 
choice, which may be motivated as follows. 
Example 2.17 Consider a set of n assets, whose prices are modeled by 
stochastic processes S,(t), i = 1,. . . , n, which are described by stochastic 
differential equations like (2.22), and assume that we have a portfolio strat- 
egy represented by functions h,(t). These functions represent the number of 
stock shares we hold in the portfolio. But which functions make sense? An 
obvious requirement is that functions h, (.) should not be anticipative: h, (t) 
may depend on all the history so far, over the interval [0, t], but clairvoyance 
should be ruled out. Furthermore, we should think of h,(t) as the number of 
shares we hold over a time interval of the form [t, t + dt). 
Now, assume that we have some initial wealth that we invest in our port- 
folio, whose initial value, depending on portfolio strategy h, is 
n 
Vh(0) = c 
h,(O)S,(O) = h’(O)S(O), 
z=1 
where we have grouped h, and S, in vectors and use notation h’S to denote 
inner vector product. What about the dynamics of the portfolio value? If the 
portfolio is self-financing, i.e., we can trade assets but we do not invest (nor 
withdraw) any more cash after t = 0, it can be shown that the portfolio value 
will satisfy the equation 
n 
dVh(t) = C h,(t) dS,(t) = h’(t) dS(t) 
2 = 1  
This looks fairly intuitive and convincing, but some careful analysis is needed 
to prove it.” In particular, we may guess that the wealth at time t = T will 
lsSee, e.g., [l, chapter 61. 

MODELING THE DYNAMICS OF ASSET PRICES 
95 
be: 
Vh(T) = Vh(0) + 
h’(t)dS(t). 
I’ 
However, it is fundamental to interpret the stochastic integral as the limit of 
an approximation like (2.24), i.e., 
,.T 
n-1 
The number of stock shares we hold at time tk does not depend on future 
prices S(tk+l). First we allocate wealth, and then we observe return. This 
is why Ito stochastic integrals are defined the way they are, and this makes 
financial sense. 
0 
Now, if we take approximation (2.24) and consider finer and finer partitions 
of the interval [ O , t ] ,  letting n -+ 
00, what do we obtain? The answer is 
technically involved. We must select some concept of stochastic convergence 
and check that everything makes sense. Using mean square convergence, it 
can be shown that the definition makes indeed sense, and we get the so-called 
stochastic integral in the sense of Ito. 
The definition of stochastic integral has some important consequences. To 
begin with, what is the expected value of the integral above? We may get a 
clue by considering approximation (2.24): 
n- 1 
= x E { X ( t k )  [W(tk+l) - W(tk)]) 
k=O 
n-1 
= 
E [X(tk)] ’ E [W(tk+l) - W(tk)] = 0, 
k=O 
where we have used independence of X(tk) from the increments of the Wiener 
process, along with the fact that the expected value of the increments is zero. 
The definition of stochastic integral does not yield a precise way to compute 
it. We may try, however, to consider a specific case to get some intuition. The 
following example illustrates one nasty consequence of the way we have defined 
the stochastic integral. 
Example 2.18 (The chain rule does not apply to stochastic differ- 
entials) Say that we want to “compute” the stochastic integral 

96 
FlNANClAL THEORY 
Analogy with ordinary calculus would suggest using the chain rule of differen- 
tiation to obtain a differential which can be integrated directly. Specifically, 
we might guess that 
dW2(t) = 2W(t) dW(t). 
This would suggest 
l
T
 
1 
0 
2 
lT 
W(t) dW(t) = 5 1 dW2(t) = -W2(T). 
But this cannot be true. We have just seen that the expected value of the 
integral is zero, but 
1 
T 
2 
2 
= - {Var[W(T)] + E2 [W(T)]} = - # 0. 
We see that the expected values do not match. 
0 
The last example shows that the chain differentiation rule does not work in 
Ito stochastic calculus. To proceed further, we need to find the right rule, and 
the answer is Ito’s lemma which is introduced below. 
We close this section by noting that we started from differential equation 
(2.22) and we ended up studying the equivalent integral form (2.23). Actually, 
from a mathematical point of view, only the latter makes sense, and we should 
regard the differential form as a shorthand notation for the integral form. An 
obvious advantage of the differential form is its readability; working on this 
form helps intuition, which is essential in devising sensible models for asset 
prices and interest rates. 
2.5.4 
Ito’s lemma 
We now give an informal argument (following [lo, chapter lo]) to obtain 
Ito’s lemma. Recall that an Ito process X ( t )  satisfies a stochastic differential 
equation such as 
dX = u(X, t )  dt + b(X, t )  dW, 
(2.25) 
which is in some sense the continuous limit of 
6X = u ( X ,  t)bt + b(X, t)E(t)&, 
(2.26) 
where E N N(0, 1)1 i.e., it has a standard normal distribution. Our aim is to 
derive a stochastic differential equation for a function F ( X ,  t )  of X ( t ) .  One 
key ingredient is the formula for the differential of a function G(z, y )  of two 
variables: 
dG 
dG 
dX 
dY 
dG = -dx + -dy, 

MODELING THE DYNAMICS OF ASSET PRICES 
97 
which may be obtained from Taylor expansion, 
d2 G 6x 6y + . . ’ 
dG 
dG 
1 d2G 
1 d2G 
6G = - 
6x + - 
6y + --(6x)’ 
4- a by)^ + - 
ax dy 
2 aY 
d X  
dY 
2 8x2 
when 6x, 6g + 0. Now we may apply this Taylor expansion to F(X, 
t), lim- 
iting it to the leading terms. In doing so it is important to notice that the 
term fi 
in equation (2.26) needs careful treatment when squared. In fact, 
we have something like 
which implies that the term in (SX)’ cannot be neglected in the approxima- 
tion. Since c is a standard normal variable, we have E[c2] = 1 and E[c2 6t] = 6t. 
A delicate point is the following. It can be shown that, as bt tends to zero, 
the term c2 6t can be treated as non-stochastic, and it is equal to its expected 
value. A useful way to remember this point is the formal rule 
(SX)’ = b2c26t + . . . , 
(dW)’ = dt. 
(2.27) 
Hence, when St tends to zero, in the Taylor expansion we have 
(SX)’ 
+ b2dt. 
Neglecting higher-order terms and taking the limit as both 6X and 6t tend 
to zero, we end up with 
d F  
d F  
1 d 2 F  
d F  = -ddX 
+ -dt 
+ --b2 
dt, 
ax 
at 
2 8x2 
which, substituting for d X ,  becomes the celebrated Ito’s lemma: 
(2.28) 
dF 
) dt + bEdW. 
d F  
dF 
1 2 d 2 F  
a-+-+-b- 
ax 
at 
2 8x2 
Although this proof is far from rigorous, we see that all the trouble is due to 
the term of order fi 
linked to the Wiener process. Indeed, if we set b = 0, 
i.e., there is no random term due to the Wiener process in the differential 
equation, Ito’s lemma boils down the chain rule for derivatives 
d F  
d F d x  
d F  
+ - 1  
dt 
dx dt 
dt 
and thus, given differential equation (2.22) for x, 
- 
- - -- 
dF 
dF 
dX 
at 
d F  = a-dt 
+ -dt. 
In Ito’s lemma we have an extra term in d W ,  which is expected given the 
input stochastic process, and an unexpected term: 
l b 2 d 2 F  
2 
8x2 
- -  

98 
FINANCIAL THEORY 
In the deterministic case, second-order derivatives occur in second-order terms 
linked to (bt)2, which can be neglected; but here we have a term of order d& 
which must be taken into account even when it is squared. In order to grasp 
Ito’s lemma, we should try a couple of examples. 
Example 2.19 Let us consider again example 2.18. In order to compute 
the stochastic integral of W2(t), 
we may simply apply Ito’s lemma to the case 
X(t) = W(t), 
by setting a ( X ,  t )  = 0, b(X, t )  = 1, and F ( X ,  t) = X 2 ( t ) .  Hence 
we have: 
dF 
- = o  
dt 
dF - 
= 2x 
d X  
(2.29) 
(2.30) 
(2.31) 
It is important to point out that in equation (2.29) the partial derivative with 
respect to time is zero; it is true that F(X(t),t) depends on time through 
X(t), but here we have no direct dependence on t, thus the partial derivative 
with respect to time vanishes. 
Ito’s lemma tells us 
dF = d(W2) = dt + 2WdW. 
It is instructive to note that dt is the term which we would not expect by 
applying the usual chain rule. But this term allows us to get the correct 
expected value of W2(T), 
since 
T 
w2p) = w2(0) + 
dW2(t) = 0 + l T d t  + 
W(t) dW(t). 
Taking expected values we get 
E[W2(T)] 
= T, 
which is coherent with what we have seen in example 2.18. 
0 
Ito’s lemma may be used to find the solution of a stochastic differential equa- 
tion, at least in relatively simple cases. A most important one is geometric 
Brownian motion. 
Example 2.20 Geometric Brownian motion. Geometric Brownian mo- 
tion is defined by the stochastic differential equation 
dS(t) = pS(t) dt + uS(t) dW(t), 

MODELING THE DYNAMICS OF ASSET PRICES 
99 
where p and u are constant parameters referred to as drift and volatility, 
respectively. Intuition would suggest to rewrite the equation as 
and then to consider the differential of d log S, which would be dS/S in deter- 
ministic calculus, to get the integral. However, we know that some extra care 
is needed. Nevertheless, it is useful to find the stochastic differential equa- 
tion for F ( S , t )  = logS(t). To apply Ito's lemma, we first compute partial 
derivatives: 
from which we may write 
dF 
dt + asas dW 
dY = 
dF 
( - - + ~ S - + - C T ~ S ~ -  
d F  
1 
at 
as 
2 
as2 
= (p-;)dt+udW 
Now we see that our guess was not that bad, as this equation may be integrated 
and vields 
logS(t) = logS(0) + p - - t + uW(t). 
( 3 
Recalling that W(t) has a normal distribution, as it can be written as W ( t )  = 
cfi, where E N N(0, l), we see that the logarithm of price is normally dis- 
tributed: 
logS(t) " 
pOgs(0) + (P - f) 
t, 
0211 
We can rewrite the solution in terms of S(t): 
or 
This shows that prices, according to the geometric Brownian motion model, 
are lognormally distributed. Recalling the relationships between normal and 
lognormal variables (see appendix B), we may also conclude that 
E[S(t)] = S(O)ep', 

100 
FINANCIAL THEORY 
from which we see that the drift parameter p is linked to continuously com- 
pounded return. The volatility parameter (T is related to standard deviation 
of the increment of logarithm of price. 
The roles of drift and volatility can also be grasped intuitively by consid- 
ering the following approximation of the equation defining Brownian motion: 
6S 
S - 
M p6t + u6W, 
where 6S/S is the return of the asset over small time interval 6t. According 
to this approximation, we see that return can be approximated by a normal 
variable with expected value p 6t and standard deviation u f i .  Actually, this 
normal distribution is only a local approximation of the “true” (according to 
the model) lognormal distribution. 
0 
Example 2.21 In the next sections we will apply Ito’s lemma to pricing 
options written on an underlying asset whose price follows geometric Brownian 
motion. Assuming that the option price at time t is a function of time and 
price only, i e . ,  a function f (S, t), let us write a differential equation for the 
value of an option. Applying again Ito’s lemma, with a = pS and b = US, 
yields 
df 
= 
- 
- d f d t + - d S +  
af 
-0 
1 2 S 2d2f 
-dt. 
at 
dS 
2 
as2 
(2.32) 
This seems an intractable object, since it looks like a partial differential equa- 
tion involving a stochastic process. Actually, by exploiting the no-arbitrage 
principle, it can be simplified and transformed to a deterministic partial dif- 
ferential equation, which is amenable to solution by numerical methods. In 
some cases it may even be solved analytically. 
0 
2.5.5 
Generalizations 
Geometric Brownian motion is not the only type of stochastic process relevant 
in finance, and the Wiener process is not the only relevant building block. 
One of the main features of these processes is the continuity of sample paths. 
However, discontinuities do occur sometimes, such as jumps in prices. In this 
case, different building blocks are used, such as the Poisson process, which is 
used to count events occurring with a certain rate. We should also note that 
continuous sample paths do not make sense for certain state variables such as 
credit rating. Another point is that the lognormal distribution, that we get 
from geometric Brownian motion, is a consequence of the normality associated 
to the Wiener process. Distributions with fatter tails are typically observed, 
questioning the validity of the models we have seen so far. However, dealing 
with sophisticated stochastic processes is beyond the scope of this book. 

MODELING THE DYNAMICS OF ASSET PRICES 
101 
What we should consider, at least, is generalizing the Wiener process to a 
multidimensional process; we should also point out different forms of stochas- 
tic differential equations, leading to qualitatively different processes, such as 
mean reverting processes. 
Correlated Wiener processes and multidimensional Ito's lemma When an option 
depends on more than one underlying asset, the simplest model is a general- 
ization of geometric Brownian motion. According to this approach, we assume 
that the price Sz(t) of asset i = 1, . . . , n satisfies 
dSz(t) = p2sz(t) 
dt + ozS,(t) dW,(t), 
where the Wiener processes WZ(t) 
are not necessarily independent. They 
are characterized by a set of instantaneous correlation coefficients pa, , whose 
meaning can be grasped by an extension of the usual formal rule: 
dW, ' dW, = pZJ dt. 
Another point of view is that when simulating correlated Wiener processes, we 
must generate standard normal variates E, which are correlated; how this can 
be accomplished will be explained in the chapter on Monte Carlo simulation. 
It is relatively easy to generalize the results of example 2.21 to an option 
whose price at time t depends on time and a set of asset prices. To generalize 
Ito's lemma, we write the differential of f(Sl(t), 
Sz(t), . . . , S n l  t), using Taylor 
expansion to get 
where terms have been included or neglected according to the formal multi- 
plication rules: 
(dt)' = 0 
dt.dW, = O  
Qi 
dW, ' dW, = pa, dt 
'di, j 
and pz2 = 1. 
multidimensional Ito's lemma: 
If we plug the equation of geometric Brownian motion here, we get the 
Mean reverting processes With geometric Brownian motion, the expected 
value of a price should go to infinity as time goes by, which is not really 

102 
FINANCIAL THEORY 
what happens in practice. In fact, stocks pay dividends, and no-arbitrage 
arguments show that the stock price should drop when dividends are paid. 
Other relevant variables, such as interest rates, cannot grow without bound. 
On the contrary, they tend to swing around long-term values, depending on 
economic conditions. We say that interest rates are characterized by mean 
reversion. Modeling interest rates is needed when dealing with interest rate 
derivatives which are used to control risk in fixed-income portfolios. We will 
have a brief look at such models in section 2.8. We just note here that we 
could model interest rates, and any variable showing mean reversion, by a 
stochastic differential equation like 
dr = a ( i  - r )  dt + CJ dW, 
where a > 0. There is much to say about a model like this, since we should 
investigate consistency with the entire term structure of interest rates and 
with no-arbitrage properties. Actually, a model like this is only concerned 
with the short term interest rate. Yet it is easy to see that the process r(t) 
tends to swing around the value P. If r > i, the drift term is negative, 
and r(t) tends to drop; if r < P ,  the drift term is positive and r(t) tends to 
increase. Variations of such a model may be needed in order to make sure 
that the output is consistent with observed dynamics and that interest rates 
stay positive. 
Similar considerations hold when modeling a stochastic and time-varying 
volatility a(t). Indeed, geometric Brownian motion assumes constant volatil- 
ity, whereas in practice we may observe time periods in which volatility is 
higher than usual. One possible model for stochastic volatility consists of a 
pair of stochastic differential equations: 
dS(t) = pS(t) dt + CJ(t)S(t) dW1 (t) 
dV(t) = a(V - V(t)) 
dt + E r n d W : ! ( t )  
where V(t) = a2(t), V is a long-term value, and different assumptions can be 
made on the correlation of the two driving Wiener processes. According to 
this model, volatility displays mean reversion, and it can be shown that the 
square root term prevents negative values of V(t). Complex models may also 
link volatility to price. 
2.6 
DERIVATIVES PRICING 
There are two basic issues in dealing with derivatives. The first issue is pricing. 
What is the fair price of a forward or an option contract? The second issue 
is hedging. Suppose that you are the writer of an option rather than the 
holder. In some sense the holder is at an advantage, since she is not forced 
to exercise the option if the circumstances are unfavorable (although example 
2.2 on page 36 shows that careless management of an option portfolio may 

DERIVATIVES PRICING 
103 
lead to a disaster). If you are the writer of an option and this is exercised, you 
have to meet your obligation, and in principle there may be no limit to your 
loss. Thus, you are interested in trading policies to reduce the risk to which 
you are exposed. We will not pursue real-life hedging in any detail in this 
book (see, e.g., [26]), but it is worth noting that, at least in theory, hedging 
is related to pricing. 
A key role in pricing is played by the no-arbitrage argument we have already 
used, in a trivial situation, for bond pricing. This is best illustrated by a couple 
of examples. In the first one we derive the price of a forward contract. In the 
second one we derive a fundamental relationship between the price of a call 
and the price of a put, called put-call parity. 
Example 2.22 Consider a forward contract for delivery at time T of an 
asset whose spot price now is S(0). The spot price S(T) at delivery is a 
random variable; hence, it would seem that randomness is involved in finding 
the fair forward price F that the holder of the long position of the forward 
will have to pay to the holder of the short position to purchase the underlying 
asset. Actually, a simple arbitrage argument shows that this is not the case. 
Suppose that we hold the short position in the contract, and consider the 
following portfolio. We may borrow an amount S(0) at the risk-free interest 
rate r, assuming continuous compounding, to buy the asset. The net cash 
flow now is zero. Then, at time T we may deliver the asset at price F ,  and we 
must pay back S(0)eTT. Despite the randomness in the spot price, the value 
of our portfolio at T is deterministic and given by F - S(0)erT. But since 
the portfolio value at time t = 0 is zero, the same must hold at time t = T .  
Hence, 
F = S(0)erT. 
Any different forward price would lead to an arbitrage opportunity. If F > 
S(0)erT , the portfolio above will lead to a safe gain F -  S(0)erT , with no initial 
commitment. If F < S(0)erTl we may reverse the portfolio by short-selling 
the asset and investing the proceeds. The reasoning assumes that short-selling 
the asset is possible and that no storage charge is paid for keeping the asset. 
See [lo] for a full account of forward pricing. 
It is interesting to note that a simple-minded approach would suggest a 
guess like F = E[S(T)], i.e., that the fair forward price is the expected price 
of the underlying in the future. This could look reasonable, assuming risk 
neutrality (linear utility function). The trouble with a reasoning like this 
is that we know most individual decision makers are characterized by some 
degree of risk aversion, but coming up with the “market” risk aversion, on 
the basis of individual utility functions, is awkward. Actually, in the idealized 
case we are considering, risk aversion does not play any role. This does not 
mean that risk aversion is not important, but that in this case we are using a 
sort of relative pricing, in which the attitude towards risk is irrelevant. 
Finally, we should note that we could write the forward price as an expected 
value, if we assume that the underlying asset price S(t) satisfies an equation 

104 
NNANClAL THEORY 
like 
dS(t) = rS(t) dt + aS(t) dW(t), 
where the “true” drift has been replaced by the risk free rate. Indeed, in a 
risk neutral world investors would not care about risk and they would not 
require a risk premium. Hence, all assets would have the same return r. We 
begin seeing here a powerful principle: risk-neutral pricing. 
II 
Example 2.23 Consider a call and a put options, both European-style, writ- 
ten on an underlying asset whose current price is S(O), with the same exercise 
price K and maturity T. For now, we are not able to figure out the fair prices 
C and P of the two options, but it is easy to see that a precise relationship 
must hold between them. Consider two portfolios: 
1. Portfolio P1 consists of one European call option and an amount of cash 
equal to Ke-rT, where r is the risk-free interest rate. 
2. Portfolio PZ consists of one European put option and one share of the 
The value of portfolio P1 at time t = 0 is C + Ke-TT; the value of portfolio 
PZ at time t = 0 is P + S(0). At time T ,  we may have two cases, depending 
on the price S(T). If S(T) > K ,  the call option will be exercised and the put 
option will not. Hence, under this hypothesis, portfolio PI at time t = T will 
be worth 
underlying stock. 
[S(T) - K )  + K = S(T), 
and portfolio PZ will be worth 
0 + S(T) = S(T). 
If S(T) < K ,  the put option will be exercised and the call option will not. In 
this case, portfolio P1 is worth 
O + K = K  
and portfolio Pz 
In both cases, the two portfolios have the same value at time T. Hence, their 
values at time t = 0 must be equal; otherwise, there will be an arbitrage 
opportunity. We have shown that the following put-call parity relationship 
must hold: 
[K - S(T)] + S(T) = K. 
C + Ke-TT = P + S(0). 
This implies that if we are able to find the fair price for one of the two options, 
the other one is obtained as well. 
0 
We will see that the use of arbitrage arguments leads to pricing equations 
in the form of partial differential equations. These may sometimes be solved 

DERIVATIVES PRICING 
105 
Fig. 2.19 Siinple single-period linomial lattice. 
analytically to yield a pricing formula in closed form, as in the case of Black 
and Scholes. In other cases, an analytical approach to option pricing may lead 
to useful approximate pricing formillas. In general, however: we need to resort 
to numerical procedures. There are basically three numerical approaches to 
price it derivative: 
0 Solving a partial differential equation, e.g., by finite difference approxi- 
mations 
0 Monte Carlo simulation 
0 Binomial or trinomial lattices 
All of thein will be pursued in later chapters. 
The first ingredient of an option pricing model is a model for the dynamics 
of the underlying asset price. The simplest such model, in continuous time, 
is gcomctric Brownian motion. which we have introduced in example 2.20. 
However: it is best to start with an even simpler representation model of price 
uncertainty: a one-step binomial model. 
2.6.1 
Consider a single time step of length at. We know the asset price So at the 
beginning of the tinie step; thc price S1 at the end of the period is a random 
variable. The simplest model we may think of specifies only two possible 
values, accounting, e.g., for the possibility of an increase and a decrease in 
the stock price. To be specific, let us consider figure 2.19. We start with a 
price So; at the next time instant we assume that the price may take either 
valiie So?/. or Sod, where d < 11, with probabilities pu and p d ,  rcspect,ively. 
Note the siiriiliirity with the niultiplicative model of equation (2.16); this is 
it discrete-time model as well, but it is also discrete-state. Now, imagine an 
opt,ioii whosc unknown value now is denoted by fo. If the option can only 
be exercised after h’t, it is easy to find it,s values f i L  and fd corresponding to 
the two outcomes. They are simply the option payoffs, which are determined 
Simple binomial model for option pricing 

106 
FINANCIAL THEORY 
by the type of contract. How can we find fo? We may again exploit the 
no-arbitrage principle. Let us set up a portfolio consisting of two assets: a 
riskless bond, with initial price BO = 1 and future price B1 = er.bt, and the 
underlying asset with initial value SO. We denote the number of stock shares 
in the portfolio by A and the number of bonds by Q. The initial value of this 
portfolio is 
and its future value, depending on the realized state, will be either 
no = AS0 + 9, 
rI, = A S o u  + 9eT'6t, 
or 
Now let us try to find a portfolio which will exactly replicate the option payoff, 
i.e., 
n d  = ASod + Qer'6t. 
A S o u  + QeT'6t = f, 
A S o d  + Qer'6t = fd. 
Solving this system of two linear equations in two unknown variables, we get 
= e-r.6t u f d  - df, 
U - d  
* 
But in order to avoid arbitrage, the initial value of this portfolio must be 
exactly fo: 
f o  = AS0 + Q  
(2.34) 
It is important to note that this relationship does not depend on the objective 
probabilities p ,  and p d .  In particular, the option price is not the, discounted, 
expected value of the payoff, which could have been a seemingly reasonable 
guess. If we think again at example 2.22 on forward pricing, we could wonder 
if we can nevertheless interpret equation (2.34) as an expected value. Indeed, 
if we set 
u - eT.6t 
ITd = 
d 
eT.6t - 
IT, = ~
-
d
 
' 
u - d  ' 
we may notice that 
IT,+ITd=1 
0 IT, and ITd are positive if d < eT'6t < u, 
which must be the case if there 
is no arbitrage strategy involving the riskless and the risky asset; hence, 
we may interpret IT, and ITd as probabilities; 

DERIVATIVES PRICING 
107 
the option price (2.34) can be interpreted as the discounted expected 
value of payoff under those probabilities: 
fo = e-T.bt E[fi] 
A 
e-T’6t(7ruf, -I- n d f d ) ,  
(2.35) 
where notation E is used to point out that expectation is taken with 
respect to a different probability measure; 
the expected value of S1 under probabilities T, and 7rd is 
E[S1] = 7ruSou + TdSod = SgeT’bt. 
The last observation explains why the “artificial probabilities” 7ru and 7rd are 
called risk-neutral. What we have found is coherent with pricing of a forward 
contract and suggests that derivatives can be priced by taking expectations 
under a risk-neutral measure. The objective probability measure does not 
play any role here, as the option payoff can be perfectly replicated by the 
two “primary” assets. When a set of “primary” assets allows us to replicate 
an arbitrary payoff, we say that the market is complete. It can be proved 
that a risk-neutral measure exists if arbitrage is impossible and it is unique if 
the market is complete. The risk-neutral valuation principle has far-reaching 
consequences; we refer the reader to a book like [20] for a deeper, yet readable, 
analysis. 
What we have seen is a typical pricing argument based on replication. We 
may obtain the same result by taking a slightly (but equivalent) view. Assume 
that we have written a call option on a stock. How can we hedge against our 
risk? One possibility would be to purchase one stock share, so that if the 
holder will exercise the option, our position is covered. However, this strategy 
may be too conservative and expensive, if the option expires worthless. We 
could try to find the “right” number of shares to hold. Say that we purchase 
A stock shares to cover the writer’s risk for a generic option with payoffs f u  
and fd. If we have written the option, the initial value of our portfolio is 
Note that the option value, fo, has a minus sign because we have a short 
position in the option, whose value in the future is a liability. The possible 
portfolio values after time period 6t are 
In the replication argument, we have built a synthetic option using the stock 
and the riskless asset. Here we may replicate the riskless asset by choosing A 
such that 
f u  - f d  
II, = IId =+ A = So(U - d )  

108 
FINANCIAL THEORY 
must hold. But due to the no-arbitrage principle, if this portfolio is riskless, 
it must earn the risk-free interest rate r. Assuming continuous compounding, 
we must have 
SoA - fo = (AuSo - fu)e-"'6t, 
or 
= AuSo - e"6tSoA - fu. 
Substituting the expression for A and rearranging, we obtain equation (2.34) 
again. 
We may interpret A as a hedging parameter, in the sense that it is the 
number of stock shares we should hold in order to hedge risk away. It is also 
useful to interpret 
as a discretized approximation of the derivative of the option value with re- 
spect to changes in the underlying price, i.e., A = d f 1%'. In the next section 
we show that, in the continuous-time and continuous-state case, this interpre- 
tation is indeed correct. 
2.6.2 
Black-Scholes model 
In the single-step binomial model, we are able to price an option assuming 
that future prices of the underlying will take one of two values. Hence, using 
only two assets, we are able to replicate any payoff. But two states make a 
rather crude model of uncertainty. What if we want to use a better probabil- 
ity distribution? One possibility would be to use more assets for replication, 
but this may be rather impractical. An alternative is to allow for trading at 
intermediate times. We should model asset prices not only now and at ma- 
turity, but also along the whole way. This can be done by using the binomial 
scheme recursively and devising a full recombining binomial lattice; this route 
yields interesting numerical schemes which are treated in chapter 7. Multi- 
stage binomial lattices are discrete-state and discrete-time models. But what 
if we want to account for a continuous distribution of future prices, such as 
the lognormal distribution associated with geometric Brownian motion? The 
answer is that we should allow for trading at infinite times, which calls for a 
continuous-time, continuous-state model. Curiously enough, this apparently 
complex model may yield simple solutions in closed form. 
Consider a vanilla option like a European-style call option written on a non- 
dividend paying stock, whose price S(t) follows a geometric Brownian motion. 
Since increments in the driving Wiener process are independent, we may say 
that future history does not depend on the past. And we may also show that 
the value of the option at a time t before maturity will depend only on time 
(more precisely, time to maturity) and current price of the underlying. If we 
denote this value by f(S(t),t), 
we have seen in example 2.21 that it satisfies 

DERIVATIVES PRICING 
109 
the stochastic differential equation: 
df = -dt+ 
af 
-dS+ 
df 
-0 
1 2 S 2d2f 
-dt. 
at 
dS 
2 
dS2 
(2.36) 
What we know is that, at maturity, the option value is just the payoff, 
F(S(T), T )  = max{S(T) - K ,  O}, 
and what we would like to know is f(S(O), 0), the fair option price now. Equa- 
tion (2.36) does not suggest an immediate way to find the option price, but it 
would look a little bit nicer without the random term dS. Remember that by 
using no-arbitrage arguments, we have obtained deterministic relationships 
in examples 2.22 and 2.23, despite the randomness involved. To get rid of 
randomness, we may try to use options and stock shares to build a portfolio 
whose value is deterministic, just as we did in the simple binomial setting. 
Consider a portfolio consisting of a short position in an option and a long po- 
sition in a certain number, say A, of stock shares. The value of this portfolio 
is 
I I = A . S -  f(S,t). 
Differentiating II and using equation (2.32), we get 
d I I = A d S - d f =  
We may eliminate the term in dS by choosing 
With this choice of A, our portfolio is riskless; hence, by no-arbitrage argu- 
ments, it must earn the risk-free interest rate r: 
dII = rIIdt. 
(2.38) 
Eliminating drI between equations (2.37) and (2.38), we obtain 
and finally 
af 
af 
1 
d2f 
- + rS- + -u2s2- 
- r f  = 0. 
at 
dS 
2 
dS2 
(2.39) 
Now we have a deterministic partial differential equation describing an option 
value f (S, t). This equation applies to any option whose payoff depends only 
on the current price of the underlying asset, or its price at maturity. When 
the payoff depends on the whole history of prices, as in the case of Asian 
options, we get a slightly more complex equation. Typical partial differential 

110 
FlNANClAL THEORY 
equations need boundary and initial conditions to pin down a specific solution. 
In our case we have final conditions. For a vanilla European call we have a 
final condition at time T: 
f(s, 
T )  = max{S - K ,  0). 
By the same token, the terminal condition for a put is 
f(S, T )  = max{S - K ,  0). 
A remarkable and counterintuitive feature of equation (2.39) is that the drift 
p of the underlying asset does not play any role. Only the risk-free interest 
rate T is involved. This is not really a surprise, given what we have seen 
for a forward or for an option under the single-step binomial model, and it 
is another example of the general and far-reaching principle of risk-neutral 
pricing. 
In general, a partial differential equation is too difficult to use to get a 
solution in closed form, and it must be solved by numerical approaches; the 
difficulty stems partly from the equation itself and partly from the boundary 
conditions. We illustrate rather simple methods in chapter 5, and their appli- 
cation to option pricing is described in chapter 9. However, there are a few 
cases where equation (2.39) can be solved analytically. The most celebrated 
case is due to Black and Scholes, who were able to show that the solution for 
a European call is 
C = SoN(d1) - Ke-'TN(d2), 
(2.40) 
where 
log(So/K) + (T + u2/2)T 
U J T  
U J T  
dl 
= 
10g(so/K) + (' - g2/2)T = dl - gJ?;, 
dz = 
and N is the distribution function for the standard normal distribution: 
N ( z )  = - 
1 Ix 
e-y2/2 dy. 
6 
-03 
By using put-call parity, it can be shown that the value of a vanilla European 
put is 
P = K e C T N ( - d 2 )  - SoN(-dl). 
(2.41) 
It is also possible to give a value to the number A of shares we should sell 
short to build the riskless portfolio II: 

DERIVATIVES PRICING 
111 
For a generic option of value f (S, t ) ,  
measures the sensitivity of the option price to small variations in the stock 
price. Other sensitivities may be obtained, such as 
These sensitivities, collectively nicknamed the Greeks, may be used to evaluate 
the risk involved in holding a portfolio of options. They are known in closed 
form for some options and must be estimated numerically in general. A and 
r play a somewhat similar role to that of duration and convexity in bond 
portfolios. 0 measures the change in option value as the expiration date is 
approached, whereas p and V (vega) measure the sensitivity to changes in the 
riskless rate and in volatility. A is particularly significant due to its role in 
the riskless portfolio we have used to derive the Black-Scholes equation. In 
fact, the writer of an option might use that portfolio to hedge the option. In 
principle, this requires a continuous portfolio rebalancing since A will change 
in time; since practical considerations and transaction costs make continuous 
rebalancing impossible, some hedging error would result. In practice, hedging 
is not just based on option A; furthermore, a whole portfolio of options must 
be typically hedged. 
2.6.3 
In the case of the simple binomial model, we have found that the option 
value is the discounted expected value of future payoff, under a risk-neutral 
measure. But in continuous time, so far, we have relied on an apparently 
different framework, based on partial differential equations. Actually, they 
are two sides of the same coin, and the gap can be bridged by one version of 
the Feynman-KaE formula. 
THEOREM 2.1 Feynman-KaC representation theorem. Consider the 
partial diflerential equation 
Risk-neutral expectation and Feynman-KaE formula 
aF 
dF 
1 
d2F 
- 
+p(x,t)- + -u (x,t)- 
= rF, 
at 
ax 
2 
a x 2  
and let F = F ( x ,  t )  be a solution, with boundary condition 
F ( T ,  X )  = @(x). 
Then, under technical conditions, F ( x ,  t )  can be represented as 

112 
NNANClAL THEORY 
where X ( t )  is a stochastic process satisfying the differential equation 
d X ,  = p(x,, T )  dT + ff(xT, 
T )  dW, 
with initial condition Xt = x. 
The notation E,J points out that this is a conditional expectation, given that 
at time t the value of the stochastic process is X ( t )  = 2. From a mathematical 
point of view, the theorem is a consequence of how Ito stochastic integral is 
defined (see [l] for a clear proof). From a physical point of view, it is a 
consequence of the connection between Brownian motion (which is a diffusion 
process) and a certain type of PDEs which can be transformed into the heat 
equation.lg 
Applying this representation theorem to Black-Scholes equation, for an 
option with payoff function a(.), immediately yields 
which is consistent with (2.35). We point out that expectation is taken under a 
risk-neutral measure, which essentially means that we work as if the stochastic 
differential equation for S(t) were 
dS = rSdt -+- oSdW. 
It is interesting to note that changing measure in this case means changing 
the drift coefficient, whereas volatility is not affected.20 
We should recall that according to the geometric Brownian motion model, 
a positive drift means that expected price in the future goes to infinity. This 
does not happen because dividends are paid, which cause a corresponding 
decrease in the stock price. It s fairly easy to show by no-arbitrage arguments 
that the price should fall by an amount corresponding to the paid dividend. 
Options on stocks paying lump sums at certain time instants can be priced by 
numerical methods such as binomial lattices. Black-Scholes model is easily 
extended if we assume that dividends are paid as a continuous stream at a 
rate q (the rate is applied to the current stock price, just like a continuously 
compounded interest rate). In this case, the risk neutral dynamics can be 
described by the equation 
dS = (r - q)Sdt + crSdW. 
(2.42) 
A continuous dividend yield is a useful idealization in many circumstances. 
We may think of a stock index, which aggregates many stocks: Their discrete 
dividend cash flows may be aggregated to one dividend yield. 
19We will introduce parabolic PDEs and the heat equation in chapter 5. 
20Formally, this is a consequence of a theorem due to Girsanov; see [l]. 

DERIVATIVES PRICING 
113 
2.6.4 
Black-Scholes model in MATLAB 
Implementing the Black-Scholes formula in MATLAB is quite easy. We may 
take advantage of the normcdf function provided by the Statistics toolbox to 
compute the cumulative distribution function for the standard normal distri- 
bution. Straightforward translation of equation (2.40) gives 
dl = (log(SO/K)+(r+sigma^2/2)*T) / (sigma * sqrt(T)); 
d2 = dl - (sigma*sqrt(T)); 
C = SO * normcdf(d1) - K * (exp(-r*T)*normcdf(d2)); 
P = K*exp(-r*T) * normcdf (-d2) - SO * normcdf (-dl); 
where the variables SO, K, R, T, sigma are self-explanatory. The Finan- 
cial toolbox function blsprice implements these formulas with a couple of 
extensions. First, it may take vector arguments to compute a set of option 
prices at once; second, it may take into account a continuous dividend rate 
q (whose default value is zero). It is easy to adjust the Black-Scholes model 
and the related pricing formula to cope with a continuous dividend rate (see 
[28, chapter 51). The following is an example of calling blsprice: 
>> SO = 50; 
>> K = 52; 
>> r = 0.1; 
>> T = 5/12; 
>> sigma = 0.4; 
>> [C, P] = blsprice(S0, K, r, T, sigma, q) 
C =  
P =  
>> q = 0; 
5.1911 
5.0689 
It is interesting to plot the value of an option, say a vanilla European call, 
for different values of the current stock price while approaching the maturity. 
Running the code illustrated in figure 2.20, we get the plot of figure 2.21. We 
see that as time progresses, the plot approaches the kinky payoff diagram.21 
An important point is that we have to be consistent in specifying the risk-free 
interest rate, the volatility, and the expiration date. In the snapshot above 
everything is expressed in a yearly base; hence, the expiration date is in five 
months. Similar functions are available to compute the Greeks, too; they are 
best illustrated through a simple example. 
Example 2.24 The Greeks may be used to approximate the change in an 
option value with respect to risk factors, just like duration and convexity for 
21See section A.2 to see how to get a surface, rather a set of plots. 

114 
FlNANClAL THEORY 
X P1otBLS.m 
SO = 30:1:70; 
K = 50; 
r = 0.08; 
sigma = 0.4; 
f o r  T=2:-0.25:O 
plot (SO ,blsprice (SO ,K,r ,T, 
sigma)) ; 
hold on; 
end 
axis( [30 70 -5 351 1 ; 
grid on 
Fig. 2.20 Valuing a European call for different current prices of the underlying stock 
while approaching the expiration date. 
30 - 
25 - 
20 - 
15 - 
10 - 
-5 
I 
I 
I 
I 
I 
I 
I 
30 
35 
40 
45 
50 
55 
60 
65 
70 
Fig. 2.21 Option value approaching the expiration date. 

DERIVATIVES PRICING 
115 
a bond portfolio, where the main risk factor is interest rate uncertainty. For 
instance, consider the change in the price of a call option due to an increase 
in the price of the underlying asset. Using a second-order Taylor expansion, 
we get the following approximation of this change: 
(2.43) 
In MATLAB we may use such an approximation by exploiting the functions 
blsdelta and blsgamma. It is important to note that, unlike the other two 
functions, blsgamma returns only one argument, as it can be shown that 
is 
the same for a call and a put. A simple MATLAB snapshot shows that the 
approximation is fairly good: 
>> CO = blsprice(50, 50, 0.1, 5/12, 0.3) 
co = 
4.8851 
>> dS = 2; 
>> C1 = blsprice(50+dS, 50, 0.1, 5/12, 0.3) 
c1 = 
>> delta = blsdelta(50, 50, 0.1, 5/12, 0.3) 
delta = 
>> gamma = blsgamma(50, 50, 0.1, 5/12, 0.3) 
gamma = 
>> CO + delta*dS + 0.5*gamma*dS-2 
ans = 
6.2057 
0.6225 
0.0392 
6.2086 
Greeks, as we have said, may play a role in hedging, and A and r play 
the same role as duration and convexity for bonds. We may come up with 
strategies to build portfolios of options which are A-neutral, which means 
that the overall value of the portfolio will not change for small changes in the 
underlying price. Actually, from a practical point of view, small changes is 
not enough, and it is arguably better to have an imperfect hedging for large 
perturbations than a perfect hedging for infinitesimal perturbations. 
Leaving hedging aside, we should note that Greeks also have a role in risk 
management. Consider estimating Value at Risk for a portfolio of options. 
Even if we assume that risk factors such as stock price perturbations bS are 
normally distributed, the pricing formula is non-linear in So, and this will 
destroy normality. However, if we use a A-based approximation like 6C M A ' 
6s we see that normality is preserved, resulting in easy calculations. Actually, 
more accurate models and better descriptions of statistical dependence which 

116 
NNANClAL THEORY 
go beyond correlation require numerical evaluation methods, such as Monte 
Carlo simulation. 
2.6.5 
A few remarks on Black-Scholes formula 
The Black-Scholes formula has been a remarkable achievement and has played 
a fundamental role in the development of a huge and increasingly sophisticated 
market. However, there is a little fly in the ointment. If the Black-Scholes 
formula were “really correct,” there would be no market for derivatives. The 
reason is disarmingly simple: The formula is based on replicating the option 
with two basic assets, and if this were really that easy, there would be no need 
for derivatives altogether. A little more formally, in a complete market there 
is no need for further assets, which would be redundant by definition. But 
of course, markets are not complete. The replication (or hedging) argument 
we have used assumes a rather idealized market, whereas, in practice, perfect 
hedging is made impossible by issues such as transaction costs, stochastic 
volatility, jumps in asset prices, etc. Geometric Brownian motion does not 
account for all of these features. 
Furthermore, if we assume that perfect replication is feasible, there is no 
need to consider risk aversion; in fact the machinery we have developed in 
section 2.4.1 on utility theory does not play any role in simple option pricing 
models. In fact, several alternative pricing models have been developed, based 
on more sophisticated models of the dynamics of the underlying asset price. 
Moreover, while lack of arbitrage implies that a risk-neutral measure exists, 
market incompleteness implies that it is not unique. Hence, there is a range 
of prices which are compatible with lack of arbitrage. Which one is the right 
one? It depends on risk. From a theoretical point of view, we cannot get rid 
of issues related to decision making under uncertainty. 
From a practical point of view, the simplicity and intuitive appeal of the 
Black-Scholes formula should not be discarded, however. Indeed, rather than 
resorting to overly complex models, the common practical approach is to use 
the Black-Scholes framework in a slightly different way, whose aim is to get 
relative prices; in other words, given prices we observe in financial markets, 
we use the arbitrage-free pricing machinery to price other assets in a way 
that is consistent with observed prices. Indeed, the Black-Scholes formula is 
sometimes considered as a sort of “interpolation” formula. 
One common way to use the formula is by computing implied volatility. In 
a naive view, the volatility parameter u in the formula should be estimated 
by analyzing the time series of prices of the underlying asset; this is what we 
mean by historical volatility. Implied volatility is computed the other way 
around: We observe option prices, and compute the volatility that makes the 
prices from the Black-Scholes formula consistent with the observed prices. 
This looks a bit like chasing our tail, but it allows to price new instruments 
in a consistent way. In practice, volatility surfaces are estimated as implied 

DERIVATIVES PRICING 
11 7 
volatility depends on multiple factors, including time to maturity and strike 
price. 
Another way to extend the machinery we have just developed to cope with 
incomplete market is by calibrating models directly under the risk-neutral 
measure, which is implicitly chosen by the market. We will motivate the 
idea in section 2.8, where we see that the Black-Scholes approach can be 
generalized by introducing a market price of risk. Roughly speaking, for each 
possible value of the market price of risk there is a risk-neutral measure, and 
a price under that measure. By observing prices, we may try to recover the 
market price of risk, or alternatively the risk-neutral measure; then, we may 
proceed pricing other instruments whose value depends on interest rates. One 
way to do so is to analyze bond prices to calibrate a model which can be used 
to price interest-rate derivatives. 
2.6.6 
Pricing American options 
Unlike their European counterparts, American options can be exercised at 
any date prior to expiration. This seemingly innocent variation makes the 
analysis of American options much more complex. One easy conclusion is 
that an American option has a larger value than the corresponding European 
option, as it gives more opportunity for exercise. From a theoretical point of 
view, valuing an American option entails the solution of a dynamic stochastic 
optimization problem. If you hold such an option, you must decide, for each 
time instant, if it is optimal or not to exercise the option. You should compare 
the intrinsic value of the option, i.e., the immediate payoff you would get from 
exercising the option early, and the continuation value, which is linked to the 
possibility of waiting for better opportunities. 
Formally, the price of an American option can be written as 
(2.44) 
where function @ is the option payoff, expectation is taken under a risk- 
neutral measure, and 7- is a stopping time. The term “stopping time” has a 
very precise meaning in the theory of stochastic processes, but here we may 
simply interpret stopping time as the time at which we exercise the option. 
The time of early exercise (if this occurs) is a random variable depending only 
on the history of prices so far. 
Clearly, early exercise will not occur if the option is not in-the-money. For 
a put option, we do not exercise the option at time t if S(t) > K. But 
even if S(t) < K ,  it may be better to keep the option and wait. Early 
exercise will occur only if the option is LLenough’’ 
in-the-money; by how much, 
it will generally depend on time to expiration, and we may expect that when 
expiration gets closer, we are more willing to exercise early. Qualitatively, for 
an American put option we would expect an early exercise boundary like the 
one depicted in figure 2.22. This boundary specifies a stock price S ( t )  such 

118 
NNANClAl THEORY 
fig 2 22 Qua1it;Ltive sketch of the early exercise boundary for a vanilla Aiiiericaii 
pit. The option is exerrised within the shaded area. 
that if S(t) < S*(t), i.e., the option is sufficiently deep in-the-money, then 
we are in the exercise region and it is optimal to exercise the option." If we 
are above the boundary, we are in the continuation region, and we keep the 
option. 
Finding this boundary is part of the problem and it is what makes it diffi- 
cult. Unlike European options, we cannot simply compute an expected value: 
and this makes the use of hlonte Carlo methods for pricing American-style op- 
tions much more difficult. In the past, this was considered impossible, but we 
will see relatively simple approaches in chapter 10. Within the partial differen- 
tial equation framework, this reasoning translates to a free boundary problem, 
which is contrasted against typical problems in which boundary conditions 
are given. However, in the context of finite difference methods of chapter 9, 
we will see that this essentially boils down to comparing the intrinsic and the 
continuation value to take a decision. 
2.7 
INTRODUCTION TO EXOTIC AND PATH-DEPENDENT 
OPTIONS 
Thc variety of options that have been conceived in the past years seems to 
have no limit. You have options on stocks, commodities, and even options 
on options. Interest-rate derivatives play a fundamental role in interest-rate 
risk management. Some options are rather peculiar and are traded over-the- 
counter for specific needs." 
"For a detailed treatment of the exercise boundary for American options, see, e.g., [14, 
chapter 41. 
"As we mentioned, this means that they are not traded on an organized exchange. 

INTRODUCTION TO EXOTIC AND PATH-DEPENDENT OPTIONS 
119 
Exotic options on stocks may be designed by introducing a certain degree 
of path dependency. The idea is that, unlike a vanilla European option, 
the payoff depends not only on the underlying asset price at expiration, but 
also on its whole path. In the following we briefly describe barrier, Asian, 
and lookback options. They are of particular interest in learning and testing 
numerical methods. 
2.7.1 
Barrier options 
In barrier options, a specific asset price sb is selected as a barrier value. During 
the life of the option, this barrier may be crossed or not. In knock-out options, 
the contract is canceled if the barrier value is crossed at any time during the 
whole life; on the contrary, knock-in options are activated only if the barrier 
is crossed. The barrier sb may be above or below the current asset price SO: 
if s b  > So, we have an up option; if &, < SO, we have a down option. These 
features may be combined with the payoffs of call and put options to define 
an array of barrier options. 
For instance, a down-and-out put option is a put option that becomes void 
if the asset price falls below the barrier Sb; in this case sb < SO, and sb < K .  
The rationale behind such an option is that the risk for the option writer is 
reduced. So, it is reasonable to expect that a down-and-out put option is 
cheaper than a vanilla one. From the point of view of the option holder, this 
means that the potential payoff is reduced; however, if you are interested in 
options to manage risk, and not as a speculator, this also means that you may 
get cheaper insurance. By the same token, an up-and-out call option may be 
defined. 
Now, consider a down-and-in put option. This option is activated only if 
the barrier level s b  < SO is crossed. Holding both a down-and-out and a 
down-and-in put option is equivalent to holding a vanilla put option. So we 
have the following parity relationship: 
where P is the price of the vanilla put, and Pdi and Pdo are the prices for the 
down-and-in and the down-and-out options, respectively. Sometimes a rebate 
is paid to the option holder if the barrier is crossed and option is canceled; in 
such a case the parity relationship above is not correct. 
In principle, the barrier might be monitored continuously; in practice, pe- 
riodic monitoring may be applied (e.g., the price could be checked each day 
at the close of trading). This may affect the price, as a lower monitoring 
frequency makes crossing the barrier less likely. 
Analytical pricing formulas are available for certain barrier options. As an 
example, consider a down-and-out put with strike price K ,  expiring in T time 
units, with a barrier set to s b .  The following formulas are known (see, e.g., 
[28, pp. 250-2511), where SO, 
T ,  
have the usual meaning. 

120 
FINANCIAL THEORY 
where 
and 
log(SoK/S,2) - (?- - u2/2)T 
U J T  
d7 
= 
log(soK/s;) - (?- + u2/2)T 
U J T  
d8 = 
A MATLAB code implementing these formulas is given in figure 2.23. 
>> [Call, Put] = blsprice (50,50,0. I ,  5/12,0.4) ; 
>> Put 
Put = 
>> DOPut (50,50,0.1,5/12,0.4,40) 
4.0760 
ans = 
0.5424 
>> DOPut (50,50,0. I ,  5/12,0.4,35) 
ans = 
1.8481 

INTRODUCVON TO EXOTlC AND PATH-DEPENDENT O f  TlONS 
121 
% Down0utPut.m 
function P = DownOutPut (SO,K,r,T,sigma,Sb) 
a = (Sb/SO)^(-l + (2*r / sigma-2)); 
b = (Sb/SO)^(l + (2*r / sigma-2)); 
dl = (log(SO/K) + (r+sigma-2 / 2)* T) / (sigma*sqrt(T>>; 
d2 = (log(SO/K) + (r-sigma-2 / 2)* T) / (sigma*sqrt(T)>; 
d3 = (log(SO/Sb) + (r+sigma-2 / 2)* T) / (sigma*sqrt(T)); 
d4 = (log(SO/Sb) + (r-sigma-2 / 2)* T) / (sigma*sqrt(T)>; 
d5 = (log(SO/Sb) - (r-sigma-2 / 2)* T) / (sigma*sqrt(T>); 
d6 = (log(SO/Sb) - (r+sigma-2 / 2)* T) / (sigma*sqrt(T)); 
d7 = (log(SO*K/Sb-2) - (r-sigma-:! / 2)* T) / (sigma*sqrt(T)); 
d8 = (log(SO*K/Sb-2) - (r+sigma-2 / 2)* T) / (sigma*sqrt(T)); 
P = K*exp (-r*T) * (normcdf (d4) -normcdf (d2) - . . . 
a*(normcdf(d7)-normcdf(d5))) 
... 
- SO* (normcdf (d3) -normcdf (dl) - . . . 
b* (normcdf (d8) -normcdf (d6) ) ) ; 
fig. 2.23 Implementing the analytical pricing formula for a down-and-out 
put option. 
>> DOPut (50,50,0.1,5/12 
,O. 4,30) 
ans = 
3.2284 
>> DOPut(50,50,0.1,5/12,0.4,1) 
ans = 
4.0760 
We see that the down-and-out put is indeed cheaper than the vanilla put; the 
price of the barrier option tends to that of the vanilla put as Sb tends to zero. 
It is also interesting to see what happens with respect to volatility: 
>> [Call, Put] = blsprice(50,50,0.1,5/12,0.4); 
>> Put 
Put = 
>> [Call, Put] = blsprice(50,50,0.1,5/12,0.3); 
>> Put 
Put = 
>> DOPut(50,50,0.1,5/12,0.4,40) 
4.0760 
2.8446 
ans = 
0.5424 
>> DOPut (50,50,0.1,5/12,0.3,40) 
ans = 

122 
NNANClAL THEORY 
0.8792 
>> DOPut(50,50,0.1,5/12,0.4,30) 
ans = 
3.2284 
>> DOPut (50,50,0. 
I, 5/12,0.3,30) 
ans = 
2.7294 
For a vanilla put, less volatility implies a lower price, as there is less uncer- 
tainty; for the barrier option, less volatility may imply a higher price since 
breaching the barrier may be less likely. We see that the dominating effect 
depends on the barrier level. 
In the formula above, it is assumed that barrier monitoring is continuous. 
When monitoring discrete, we should expect that the price for a down-and-out 
option is increased, since breaching the barrier is less likely. An approximate 
correction has been suggested (see [2] or [14, p. 2661). The idea is using the 
analytical formula above, correcting the barrier ~ 1 s  follows: 
where the term 0.5826 derives from the Riemann zeta function, 6t is time 
elapsing between two consecutive monitoring time instants, and the sign f 
depends on the option type. For a down-and-out put we should take the minus 
sign, as the barrier level should be lowered to reflect the reduced likelihood 
of crossing the barrier. For instance, if we monitor the barrier each day, the 
prices above change approximately as follows: 
>> DOPut (50,50,0. 
I, 5/12,0.4,40) 
ans = 
0.5424 
>> DOPut(50,50,0.1,5/12,0.4,40*exp(-0.5826*0.4*sqrt(1/12/30))) 
ans = 
0.6380 
>> DOPut(50,50,0.1,5/12,0.4,30) 
ans = 
3.2284 
>> D0Put(50,50,0.1,5/12,0.4,30*exp(-0.5826*0.4*sqrt(1/12/30~~~ 
ans = 
3.3056 
We have assumed here that each month consists of 30 days. It should be noted 
that alternative analytical methods for discrete-time barrier options have been 
developed, but we will stick to this one because of its conceptual simplicity. 

lNTRODUCTlON TO EXOTK AND PATH-DEPENDENT OPTlONS 
123 
2.7.2 
Asian options 
Barrier options exhibit a weak degree of path dependency. A stronger degree 
of path dependency is typical of Asian options, as the payoff depends on the 
average asset price over the option life. 
Different Asian options may be devised, depending on how the average is 
computed. Sampling may be discrete or (in principle) continuous. Further- 
more, the average may be arithmetic or geometric. The discrete arithmetic 
average is 
l
n
 
Ada = - 
s(ti), 
n i = l  
where ti, i = 1,. . . , n, are the discrete sampling times. The geometric average 
is 
If continuous sampling is assumed, we get 
A,, 
= f 1' S(t) dt 
A,, 
= e x p [ $ l  T log S(t)dt] 
Given some way to measure the average A, you may use it to define a rate or 
a strike. An average rate call has a payoff given by 
max{A - K, 0}, 
whereas for an average strike call we have 
max{S(T) - A, 0). 
By the same token, we may define an average rate put: 
max{K - A, 0), 
or an average strike put: 
max{A - S(T), 0). 
Early exercise features may also be defined in the contract. 
2.7.3 
Lookback options 
Lookback options come in many forms, just like Asian options. The basic 
difference is that a maximum (or a minimum) value is monitored during the 

124 
FINANCIAL THEORY 
option life, Assuming continuous monitoring, we may measure the maximum 
and the minimum asset price: 
A European style lookback call has a payoff given by 
whereas in the case of a lookback put we have 
Just as in the Asian option case, you may use the maximum and minimum 
to define rates or strikes, and you may also add early exercise features. As- 
suming continuous monitoring, some analytical pricing formulas are known 
for lookback options. 
2.8 
AN OUTLOOK O N  INTEREST-RATE DERIVATIVES 
In this book we will only deal with pricing equity options, as this is enough to 
introduce and motivate the numerical methods we are interested in.24 How- 
ever, there is a huge market of interest-rate derivatives, and in this section we 
would like to point out why they are important and why they are so difficult 
to deal with. Actually, any bond is an interest-rate derivative, since its value 
depends on interest rates; if we model interest rates as stochastic processes, 
we may apply the option pricing machinery to pricing a zero-coupon bond. 
This may look like “overkill,” but it may play a fundamental role in pricing 
more complex interest-rate derivatives, as we will see. 
The following is a non-exhaustive list of the most basic assets that can be 
classified as interest-rate derivatives. 
Interest-rate swaps. A swap is an arrangement between two parties, 
which agree to exchange cash flows at predetermined dates in the future. 
In the vanilla swap, one party will pay cash flows given by a fixed interest 
rate applied to a nominal amount of money (the notional principal). The 
other party will pay an amount given by a variable interest rate, applied 
to a given interval of time (the tenure), on the same notional principal. 
The net cash flow will depend on the level of future interest rates. 
24This section is included for the sake of completeness, but it can be safely skipped by 
readers just interested in numerical methods. 

AN OUTLOOK ON INTEREST-RATE DERIVATIVES 
125 
Bond options. A call option on a bond works more or less like a call 
option on a stock, with a different underlying asset. In this case we 
have two maturities: the maturity T of the option, at which the option 
can be exercised, and the maturity S of the bond. Obviously, we must 
have T < S. The payoff of the option will depend on the bond price 
at T ,  which in turn depends on uncertain interest rates. Call options 
are actually embedded in certain types of bonds. A callable bond can 
be redeemed before maturity by the issuer, if prevailing interest rates 
make this choice attractive, i.e., when interest rates drop and the bond 
issuer may refinance its debt at lower rates. In this case, the investor 
purchasing the bond implicitly sells a call option to the bond issuer. 
Hence, the callable bond must cost less than its non-callable counterpart. 
Interest-rate caps. A cap offers protection against a rise in interest 
rates. This may be interesting to someone who wants to borrow money 
at a variable rate. A cap is a portfolio of caplets, applying to different 
time intervals in the future. If L is a notional principal and RK is the 
cap rate, a caplet applying to a time interval of length bt gives a payoff 
L . bt ' max(0, R - RK}, 
where R is the interest rate prevailing for that interval. Should interest 
rates rise in the future, the owner of the cap will receive a payoff covering 
the payment interest above the cap rate. It can be shown that caps are 
equivalent to portfolios of bond options. 
Interest-rate floors. A floor is similar to a cap, but it offers protection 
against a drop in interest rates. The payoff of a floorlet is 
L .  bt . max(0, RK - R}. 
The list of available interest-rate derivatives is increasing because of their use- 
fulness as interest-rate risk management tools. They are, at least potentially, 
more powerful than older-style practices based on immunization. 
The elementary interest-rate derivatives we have just described can be 
priced using fairly simple models, if some assumptions are made. But this 
does not hold in general, and more sophisticated models are needed, either 
to account for the complexity in the dynamics of interest rates, or to price 
complex derivatives. In the following sections we will just offer some intuition 
about the reasons behind such a complexity. In the Black-Scholes model for 
stock options, we have assumed constant interest rates and constant volatility 
for the price of the underlying asset. Of course the first assumption does not 
make any sense for interest-rate derivatives. But also the second one cannot 
be reasonable: The bond price, when maturity is approaching, is less and less 
volatile (the duration gets smaller and smaller). 

126 
FlNANClAL THEORY 
2.8.1 Modeling interest-rate dynamics 
Several models have been proposed over the years to capture the uncertain 
dynamics of interest rates. They differ in the following basic features: 
0 The number of stochastic factors. In the simplest models, we describe 
the dynamics of the short rate r(t), which is essentially a rate applying 
for a very short time span (t,t + bt) in the future. However, we know 
that bond prices depend on a whole term structure of interest rates. If 
we build a one-factor model, we are essentially assuming that we may 
capture the dynamics of the whole term structure just by the short rate 
and its future evolution. Actually, it is difficult to get a realistic model 
based on one factor only, and more complex models based on a set of 
factors should be built, with a corresponding increase in difficulty. 
0 The focus on equilibrium or arbitrage. It is possible to pursue the some- 
what ambitious idea of building an economically sound model, which 
yields interest rates as a consequence of market equilibrium. An alter- 
native idea is trying to build models which match the currently observed 
term structure. This is less ambitious, but it may better replicate ob- 
served prices. In fact, a basic requirement of a credible model is that 
it replicates the prices of basic assets, which may be observed in the 
market. In general, arbitrage based approach aim at this idea of relative 
pricing. 
As a result, there is a significant variety of models, with advantages and 
disadvantages, and there is no obvious choice among them. We do not want 
to venture into this difficult domain but, given our knowledge of Ito processes, 
we may at least sketch a few models based on stochastic differential equations 
for the short rate. 
The general structure of such models is 
dr(t) = p[t, r(t)] dt + u[t, r(t)] dW(t), 
(2.45) 
where W(t) is a standard Wiener process. Multifactor models use multidi- 
mensional Wiener processes. Geometric Brownian motion is a clearly inade- 
quate model, at least in the long term, as interest rates cannot grow without 
bound. Mean reversion is a common feature of many models, among which 
we mention: 
1. VasiEek: 
dr = (b - ar) dt + u dW, 
where a > 0. 
2. Cox-Ingersoll-Ross (CIR): 
dr = a(b - r )  dt + ufidW. 

AN OUTLOOK ON INTEREST-RATE DERIVATIVES 
127 
3. Black-Derman-Toy (BDT): 
dr = O(t)r dt + a(t)r dW. 
4. Hull-White (extended CIR): 
dr = [o(t) 
- a(t)r] dt + a(t)&dW, 
where a(t) > 0. 
VasiEek model exhibits mean reversion, but the rate can get negative. Avoid- 
ing negative rates is the rationale behind the fi term in the CIR model. The 
BDT model includes time-varying functions: On the one hand, this makes the 
model more complicated, but it allows to match the current term structure 
(which can be done only approximately with simpler models). The Hull- 
White extension of CIR model, in some sense, puts all of the above ideas 
toget her. 
In the next chapters, we will see how continuous-time stochastic models 
may be exploited computationally, either by Monte Carlo simulation or by 
building discretized approximations such as binomial lattices or trees. The 
same ideas, with significant complications may be applied to interest rate 
models. For instance, the MATLAB Financial derivatives toolbox includes 
functions to build trees for the BDT short rate model and the Heat-Jarrow- 
Morton (HJM) model, which the best-known multifactor model. Whatever 
model and computational technique we use, we must calibrate the parameters 
of the models above. One would think that to accomplish this task, we should 
gather market data for interest rates and use some numerical procedure to fit 
model parameters to observed data. The next section shows that this is not 
really the case. 
2.8.2 
We have already pointed out that an apparently paradoxical feature of Black- 
Scholes formula is that it prices an option under the very assumption that 
options are no use. This is due to the fact the markets are assumed complete, 
thus options can be replicated using a risk-free asset and the underlying asset. 
In practice, this is not true for many reasons, including market imperfections 
(e.g., transaction costs) and stochastic volatility. This does not imply that 
the theory is useless: On the contrary, it is used to build internally coherent 
prices by exploiting concepts such as implied volatility and volatility surfaces. 
When we consider interest-rate derivatives, however, we are facing an im- 
mediate difficulty: The interest rate is not an asset that can be included in 
a portfolio. Hence, we cannot build a replicating portfolio. A similar diffi- 
culty is faced with certain derivatives written on commodities which are not 
investment goods and which cannot be included in an investment portfolio 
leading to replication arguments. The fundamental difficulty is that markets 
Incomplete markets and the market price of risk 

128 
FlNANClAL THEORY 
are incomplete. Hence, while no-arbitrage conditions imply that a risk-neutral 
measure exists, market incompleteness implies that it is not unique. All we 
can do is to build an internally coherent price system, which is consistent with 
some observed prices and is arbitrage-free. In other words, we need to pin 
down a risk-neutral measure which is linked to observed prices. 
When dealing with interest-rate derivatives, the simplest asset we may work 
with is a zero-coupon bond. Actually, we need a set of zero-coupon bonds, 
one for each possible maturity. Let us assume that a market exists for zero- 
coupon bonds of any maturity. We may work with a short rate model like 
(2.45) to explore the consequences of no-arbitrage. Let p ( t ,  T )  be the price at 
time t of a zero-coupon bond with maturity T. Given a model for the short 
rate, it is reasonable to assume that this price is a function of time t and the 
current short rate r(t): 
As we have seen with pricing stock options, we need some boundary or termi- 
~ ( t ,  
T )  = F(t, r(t); T). 
nal condition. 
condition is 
for any value 
bond by FT. 
application of 
If we assume that the face value of the bond is $1, the terminal 
F(T, r; T )  = 1, 
of r. To ease the notation, we will denote the price of this 
Assuming that the short rate is modeled by equation (2.45), 
[to’s lemma yields 
= vTFTdt + J T F ~  
dW, 
where, for the sake of convenience, we have introduced 
c dFT 
FT dr ‘ 
~- 
<T = 
If we consider another bond, with maturity S, we have 
dFS = vsFSdt + <sFsdW, 
where W ( t )  is the same Wiener process, as both bonds depend on the same 
underlying factor. Hence, we may eliminate the term dW by forming the 
following portfolio of bonds: 
II = ( D ~ F ~ ) F ~  
- ( e T ~ T ) ~ S .  
It is important to realize that the expressions between parentheses are the 
amounts of each bond we hold, which do not change over a short time period 

AN OUTLOOK ON INTEREST-RATE DERIVATIVES 
129 
d t ,  whereas the bond value does. Hence, differentiation in the Ito sense yields 
dll = ( o s F S )  dFT - ( ~ T F ~ )  
dFS 
= ( p ~ o s F ~ F ~  
- p s a ~ F  
T
S
 
F ) dt. 
But since this is a risk-free portfolio, lack of arbitrage opportunities implies 
d l l  = rlldt, 
which in turn gives 
~ T U S  - ~ S U T  = rus - r q .  
This equality must hold for any maturity. This means that if our bond market 
is arbitrage free, there must exist a process X ( t )  such that 
(2.46) 
for any maturity T. The process X(t) is called the market price of risk. If 
we write p = r + Xa, we may understand the reason behind this name: the 
drift p is the risk free rate plus a compensation depending on volatility and 
the price of risk. If the price of risk is X = 0, as in the usual risk neutral 
world, we have p = r, which is exactly the drift we use when pricing options 
in the Black-Scholes world. 
If we substitute p~ and (TT in (2.46), we get the following PDE: 
rFT = 0. 
dFT 
dFT 
1 2a2FT 
at 
dr 
2 
dr2 
- 
+ (p - Xu)- 
+ -u - 
- 
This PDE, together with the boundary condition FT(T, r )  = 1, is called term 
structure equation. Application of the Feynman-KaE formula to this PDE 
yields the price of the zero-coupon bond as an expected value: 
where notation E f r  means that we are taking a conditional expectation given 
t and r(t), under a risk-neutral measure Q, and the process ~ ( s )  
satisfies the 
stochastic differential equation: 
dr(s) = { p  - Xa} ds + a dW(s), 
with initial condition r(t) = r. 
Using a similar procedure we could price other interest-rate derivatives, 
provided we use the appropriate market price of risk. To spot the right A, we 
should calibrate the model, in the sense that we should find the market price 
of risk that fits the observed prices of zero-coupon bonds. This means that 
we should find a stochastic differential equation describing the dynamics of 

130 
FINANCIAL THEORY 
the short rate directly in the risk-neutral world. Doing so basically requires 
the solution of an inverse problem: Given bond prices and the term structure 
equation, we should find the market price of risk. This task may be relatively 
easy or not, depending on the model we assume for the short rate. Some 
models result in an analytical solution, some do not. Of course, if a model 
depends on three numerical parameters (like CIR), we cannot hope to find an 
exact fit. 
In practice, model calibration based on zero-coupon bonds is not that easy 
because of the lack of enough assets. Actually, what we need is a model en- 
abling coherent pricing with traded assets; hence, any asset related to interest 
rates is a possible data source for calibration. Recently, many market models 
have been developed which do not claim to be economically motivated mod- 
els, but aim at making practical pricing easier. In fact, the short rate is a 
mathematically convenient object, but it is not directly observable. Other 
rates, such as LIBOR,25 are more convenient from this point of view. 
For further reading 
In the literature 
0 A book dealing with investments in general and their mathematical 
modeling is [15]. It is comprehensive and quite readable. A higher-level 
treatment can be found in [ll]. Another general reference is (281, which 
has a sharper focus on derivatives. 
0 If you are interested in how a stock exchange actually works, see [27]. 
0 More specific references for bond markets and fixed-income-related as- 
sets are [6], [7], [8], and [25]. See also [16]. 
0 Portfolio theory is covered in [5]; you might wish to have a look at 
chapter 10 there to gain a deeper understanding of utility theory. 
0 Advanced issues in portfolio management are dealt with in [23]. 
0 The classical reference for options and derivatives in general is (10). For 
a more formal treatment, see, e.g., [14]. 
0 A good reference on Value at Risk is [12]. 
0 A book dealing extensively with the intricacies of option hedging is [26]; 
it is not very readable for the uninitiated, but it gives a precise idea of 
practical option trading. 
25London Inter-Bank Offer Rate 

REFERENCES 
131 
0 There is a growing literature on continuous-time stochastic calculus in 
finance. Many books in this vein are quite hard to read; but if you want 
to find a good compromise between intuition and mathematical rigor, 
take a look at [17] or [19]. A more recent text is [24]. 
0 Discrete-time models are dealt with in [20], which is an excellent refer- 
ence for an understanding of the relationship between risk-neutral prob- 
ability measures and the no-arbitrage hypothesis. 
0 Readers interested in a broader view of Financial Economics should 
consult [4]. 
Another readable reference is [3]. 
0 Interest-rate derivatives are also covered in books on fixed-income secu- 
rities such as [16]. A book which is more focused on this class of assets 
is [21]. Recent market models are described in [22]. 
0 For a mathematically rigorous yet readable treatment of the theoretical 
background of interest-rate derivatives, see [ 11. 
0 Readers interested in the use of derivatives for interest-rate risk man- 
agement are [9] and [18]. 
On the Web 
0 A site where you may find a list many interesting resources for finance 
is http://fisher.osu.edu/fin/journal/jofsites.htm. 
0 An academic society that could be of interest to you is IAFE (Inter- 
national Association of Financial Engineers, http : //www . iaf e .  org). 
Another interesting academic society is the Bachelier Finance Society 
(http://www.bachelierfinance.com). 
REFERENCES 
1. T. Bjork. Arbitrage Theory in Continuous Time (2nd ed.). Oxford Uni- 
versity Press, Oxford, 2004. 
2. M. Broadie, P. Glasserman, and S.G. Kou. A Continuity Correction for 
Discrete Barrier Options. Mathematical Finance, 7:325-349, 1997. 
3. J. CvitaniC and F. Zapatero. Introduction to the Economics and Mathe- 
matics of Financial Markets. MIT Press, Cambridge, MA, 2004. 
4. J.-P. Danthine and J.B. Donaldson. Intermediate Financial Theory (2nd 
ed.). Academic Press, San Diego, CA, 2005. 

132 
FINANCIAL THEORY 
5. E.J. Elton and M.J. Gruber. Modern Portfolio Theory and Investment 
Analysis (5th ed.). Wiley, New York, 1995. 
6. F. J. Fabozzi. Bond Markets: Analysis and Strategies. Prentice Hall, 
Upper Saddle River, NJ, 1996. 
7. F. J. Fabozzi. Fixed Income Mathematics: Analytical and Statistical Tech- 
niques (3rd ed.). McGraw-Hill, New York, 1997. 
8. F.J. Fabozzi and G. Fong. Advanced Fixed Income Portfolio Management: 
The State of the Art. McGraw-Hill, New York, 1994. 
9. B.E. Gup and R. Brooks. Interest Rate Risk Management: The Banker's 
Guide to Using Futures, Options, Swaps, and Other Derivative Instru- 
ments. Irwin Professional Publishing, New York, 1993. 
10. J.C. Hull. Options, Futures, and Other Derivatives (5th ed.). Prentice 
Hall, Upper Saddle River, NJ, 2003. 
11. J.E. Ingersoll, Jr. Theory of Financial Decision Making. Rowman & 
Littlefield, Totowa, NJ, 1987. 
12. P. Jorion. Value at Risk: The New Benchmark for Controlling Derivatives 
Risk. McGraw-Hill, New York, 1997. 
13. J.G. Kallberg and W.T. Ziemba. Comparison of Alternative Utility F'unc- 
Management Science, 29: 1257- 
tions in Portfolio Selection Problems. 
1276, 1983. 
14. Y.K. Kwok. Mathematical Models of Financial Derivatives. Springer- 
Verlag, Berlin, 1998. 
15. D.G. Luenberger. Investment Science. Oxford University Press, New 
York, 1998. 
16. L. Martellini, P. Priaulet, and S. Priaulet. Fixed-Income Securities: VaZ- 
uation, Risk Management, and Portfolio Strategies. Wiley, Chichester, 
2003. 
17. T. Mikosch. Elementary Stochastic Calculus with Finance in View. World 
Scientific Publishing, Singapore, 1998. 
18. S.K. Nawalkha, G.M. Soto, and N.A. Beliaeva. Interest Rate Risk Model- 
ing. Wiley, Hoboken, NJ, 2005. 
19. S. Neftci. A n  Introduction to the Mathematics of Financial Derivatives 
(2nd ed.). Academic Press, San Diego, CA, 2000. 
20. S.R. Pliska. Introduction to Mathematical Finance: Discrete Time Mod- 
els. Blackwell Publishers, Malden, MA, 1997. 

REFERENCES 
133 
21. R. Rebonato. Interest-Rate Option Models (2nd ed.). Wiley, Chichester, 
2000. 
22. R. Rebonato. Modern Pricing of Interest-Rate Derivatives: the LIBOR 
Market Model and Beyond. Princeton University Press, Princeton, NJ, 
2002. 
23. B. Scherer and D. Martin. Introduction to Modern Portfolio Optimization 
with NuOPT, S-Plus, and PBayes. Springer, New York, 2005. 
24. S. Shreve. Stochastic Calculus for Finance (vols. I B II). Springer-Verlag, 
New York, 2003. 
25. S.M. Sundaresan. Fixed Income Markets and Their Derivatives. South 
Western College Publishing, Cincinnati, OH, 1997. 
26. N. Taleb. Dynamic Hedging: Managing Vanilla and Exotic Options. Wi- 
ley, New York, 1996. 
27. S.R. Veale, editor. Stocks, Bonds, Options, Futures: Investments and 
their Markets. New York Institute of Finance / Prentice Hall, Paramus, 
NJ, 1987. 
28. P. Wilmott. Quantitative Finance (vols. I and II). Wiley, Chichester, 
West Sussex, England, 2000. 

This Page Intentionally Left Blank

