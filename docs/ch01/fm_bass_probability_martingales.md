# Probability, Martingales & Binomial Models

!!! info "Source"
    **The Basics of Financial Mathematics** by Richard F. Bass, University of Connecticut, Spring 2003.
    These notes are used for educational purposes.

## 1. Introduction

1. Introduction.
In this course we will study mathematical finance. Mathematical finance is not
about predicting the price of a stock. What it is about is figuring out the price of options
and derivatives.
The most familiar type of option is the option to buy a stock at a given price at
a given time. For example, suppose Microsoft is currently selling today at $40 per share.
A European call option is something I can buy that gives me the right to buy a share of
Microsoft at some future date. To make up an example, suppose I have an option that
allows me to buy a share of Microsoft for $50 in three months time, but does not compel
me to do so. If Microsoft happens to be selling at $45 in three months time, the option is
worthless. I would be silly to buy a share for $50 when I could call my broker and buy it
for $45. So I would choose not to exercise the option. On the other hand, if Microsoft is
selling for $60 three months from now, the option would be quite valuable. I could exercise
the option and buy a share for $50. I could then turn around and sell the share on the
open market for $60 and make a profit of $10 per share. Therefore this stock option I
possess has some value. There is some chance it is worthless and some chance that it will
lead me to a profit. The basic question is: how much is the option worth today?
The huge impetus in financial derivatives was the seminal paper of Black and Scholes
in 1973. Although many researchers had studied this question, Black and Scholes gave a
definitive answer, and a great deal of research has been done since. These are not just
academic questions; today the market in financial derivatives is larger than the market
in stock securities. In other words, more money is invested in options on stocks than in
stocks themselves.
Options have been around for a long time. The earliest ones were used by manu-
facturers and food producers to hedge their risk. A farmer might agree to sell a bushel of
wheat at a fixed price six months from now rather than take a chance on the vagaries of
market prices. Similarly a steel refinery might want to lock in the price of iron ore at a
fixed price.
The sections of these notes can be grouped into five categories. The first is elemen-
tary probability. Although someone who has had a course in undergraduate probability
will be familiar with some of this, we will talk about a number of topics that are not usu-
ally covered in such a course: σ-fields, conditional expectations, martingales. The second
category is the binomial asset pricing model. This is just about the simplest model of a
stock that one can imagine, and this will provide a case where we can see most of the major
ideas of mathematical finance, but in a very simple setting. Then we will turn to advanced
probability, that is, ideas such as Brownian motion, stochastic integrals, stochastic differ-
ential equations, Girsanov transformation. Although to do this rigorously requires measure
theory, we can still learn enough to understand and work with these concepts. We then
return to finance and work with the continuous model. We will derive the Black-Scholes
formula, see the Fundamental Theorem of Asset Pricing, work with equivalent martingale
measures, and the like. The fifth main category is term structure models, which means
models of interest rate behavior.
I found some unpublished notes of Steve Shreve extremely useful in preparing these
notes. I hope that he has turned them into a book and that this book is now available.
The stochastic calculus part of these notes is from my own book: Probabilistic Techniques
in Analysis, Springer, New York, 1995.
I would also like to thank Evarist Gin´e who pointed out a number of errors.


## 2. Review of Elementary Probability

2. Review of elementary probability.
Let’s begin by recalling some of the definitions and basic concepts of elementary
probability. We will only work with discrete models at first.
We start with an arbitrary set, called the probability space, which we will denote
by Ω, the capital Greek letter “omega.” We are given a class F of subsets of Ω. These are
called events. We require F to be a σ-field.
Definition 2.1. A collection F of subsets of Ωis called a σ-field if
(1) ∅∈F,
(2) Ω∈F,
(3) A ∈F implies Ac ∈F, and
(4) A1, A2, . . . ∈F implies both ∪∞
i=1Ai ∈F and ∩∞
i=1Ai ∈F.
Here Ac = {ω ∈Ω: ω /∈A} denotes the complement of A. ∅denotes the empty set, that
is, the set with no elements. We will use without special comment the usual notations of
∪(union), ∩(intersection), ⊂(contained in), ∈(is an element of).
Typically, in an elementary probability course, F will consist of all subsets of
Ω, but we will later need to distinguish between various σ-fields.
Here is an exam-
ple. Suppose one tosses a coin two times and lets Ωdenote all possible outcomes. So
Ω= {HH, HT, TH, TT}. A typical σ-field F would be the collection of all subsets of Ω.
In this case it is trivial to show that F is a σ-field, since every subset is in F. But if
we let G = {∅, Ω, {HH, HT}, {TH, TT}}, then G is also a σ-field. One has to check the
definition, but to illustrate, the event {HH, HT} is in G, so we require the complement of
that set to be in G as well. But the complement is {TH, TT} and that event is indeed in
G.
One point of view which we will explore much more fully later on is that the σ-field
tells you what events you “know.” In this example, F is the σ-field where you “know”
everything, while G is the σ-field where you “know” only the result of the first toss but not
the second. We won’t try to be precise here, but to try to add to the intuition, suppose
one knows whether an event in F has happened or not for a particular outcome.
We
would then know which of the events {HH}, {HT}, {TH}, or {TT} has happened and so
would know what the two tosses of the coin showed. On the other hand, if we know which
events in G happened, we would only know whether the event {HH, HT} happened, which
means we would know that the first toss was a heads, or we would know whether the event
{TH, TT} happened, in which case we would know that the first toss was a tails. But
there is no way to tell what happened on the second toss from knowing which events in G
happened. Much more on this later.
The third basic ingredient is a probability.
Definition 2.2. A function P on F is a probability if it satisfies
(1) if A ∈F, then 0 ≤P(A) ≤1,
(2) P(Ω) = 1, and
(3) P(∅) = 0, and
(4) if A1, A2, . . . ∈F are pairwise disjoint, then P(∪∞
i=1Ai) = P∞
i=1 P(Ai).
A collection of sets Ai is pairwise disjoint if Ai ∩Aj = ∅unless i = j.
There are a number of conclusions one can draw from this definition.
As one
example, if A ⊂B, then P(A) ≤P(B) and P(Ac) = 1 −P(A). See Note 1 at the end of
this section for a proof.
Someone who has had measure theory will realize that a σ-field is the same thing
as a σ-algebra and a probability is a measure of total mass one.
A random variable (abbreviated r.v.) is a function X from Ωto R, the reals. To
be more precise, to be a r.v. X must also be measurable, which means that {ω : X(ω) ≥
a} ∈F for all reals a.
The notion of measurability has a simple definition but is a bit subtle. If we take
the point of view that we know all the events in G, then if Y is G-measurable, then we
know Y . Phrased another way, suppose we know whether or not the event has occurred
for each event in G. Then if Y is G-measurable, we can compute the value of Y .
Here is an example. In the example above where we tossed a coin two times, let X
be the number of heads in the two tosses. Then X is F measurable but not G measurable.
To see this, let us consider Aa = {ω ∈Ω: X(ω) ≥a}. This event will equal





Ω
if a ≤0;
{HH, HT, TH}
if 0 < a ≤1;
{HH}
if 1 < a ≤2;
∅
if 2 < a.
For example, if a = 3
2, then the event where the number of heads is 3
2 or greater is the
event where we had two heads, namely, {HH}. Now observe that for each a the event Aa
is in F because F contains all subsets of Ω. Therefore X is measurable with respect to F.
However it is not true that Aa is in G for every value of a – take a = 3
2 as just one example
– the subset {HH} is not in G. So X is not measurable with respect to the σ-field G.
A discrete r.v. is one where P(ω : X(ω) = a) = 0 for all but countably many a’s,
say, a1, a2, . . ., and P
i P(ω : X(ω) = ai) = 1. In defining sets one usually omits the ω;
thus (X = x) means the same as {ω : X(ω) = x}.
In the discrete case, to check measurability with respect to a σ-field F, it is enough
that (X = a) ∈F for all reals a. The reason for this is that if x1, x2, . . . are the values of
x for which P(X = x) ̸= 0, then we can write (X ≥a) = ∪xi≥a(X = xi) and we have a
countable union. So if (X = xi) ∈F, then (X ≥a) ∈F.
Given a discrete r.v. X, the expectation or mean is defined by
E X =
X
x
xP(X = x)
provided the sum converges. If X only takes finitely many values, then this is a finite sum
and of course it will converge. This is the situation that we will consider for quite some
time. However, if X can take an infinite number of values (but countable), convergence
needs to be checked. For example, if P(X = 2n) = 2−n for n = 1, 2, . . ., then E X =
P∞
n=1 2n · 2−n = ∞.
There is an alternate definition of expectation which is equivalent in the discrete
setting. Set
E X =
X
ω∈Ω
X(ω)P({ω}).
To see that this is the same, look at Note 2 at the end of the section. The advantage of the
second definition is that some properties of expectation, such as E (X + Y ) = E X + E Y ,
are immediate, while with the first definition they require quite a bit of proof.
We say two events A and B are independent if P(A∩B) = P(A)P(B). Two random
variables X and Y are independent if P(X ∈A, Y ∈B) = P(X ∈A)P(X ∈B) for all A
and B that are subsets of the reals. The comma in the expression P(X ∈A, Y ∈B) means
“and.” Thus
P(X ∈A, Y ∈B) = P((X ∈A) ∩(Y ∈B)).
The extension of the definition of independence to the case of more than two events or
random variables is not surprising: A1, . . . , An are independent if
P(Ai1 ∩· · · ∩Aij) = P(Ai1) · · · P(Aij)
whenever {i1, . . . , ij} is a subset of {1, . . . , n}.
A common misconception is that an event is independent of itself. If A is an event
that is independent of itself, then
P(A) = P(A ∩A) = P(A)P(A) = (P(A))2.
The only finite solutions to the equation x = x2 are x = 0 and x = 1, so an event is
independent of itself only if it has probability 0 or 1.
Two σ-fields F and G are independent if A and B are independent whenever A ∈F
and B ∈G. A r.v. X and a σ-field G are independent if P((X ∈A) ∩B) = P(X ∈A)P(B)
whenever A is a subset of the reals and B ∈G.
As an example, suppose we toss a coin two times and we define the σ-fields G1 =
{∅, Ω, {HH, HT}, {TH, TT}} and G2 = {∅, Ω, {HH, TH}, {HT, TT}}. Then G1 and G2 are
independent if P(HH) = P(HT) = P(TH) = P(TT) = 1
4. (Here we are writing P(HH)
when a more accurate way would be to write P({HH}).) An easy way to understand this
is that if we look at an event in G1 that is not ∅or Ω, then that is the event that the first
toss is a heads or it is the event that the first toss is a tails. Similarly, a set other than ∅
or Ωin G2 will be the event that the second toss is a heads or that the second toss is a
tails.
If two r.v.s X and Y are independent, we have the multiplication theorem, which
says that E (XY ) = (E X)(E Y ) provided all the expectations are finite. See Note 3 for a
proof.
Suppose X1, . . . , Xn are n independent r.v.s, such that for each one P(Xi = 1) = p,
P(Xi = 0) = 1 −p, where p ∈[0, 1]. The random variable Sn = Pn
i=1 Xi is called a
binomial r.v., and represents, for example, the number of successes in n trials, where the
probability of a success is p. An important result in probability is that
P(Sn = k) =
n!
k!(n −k)!pk(1 −p)n−k.
The variance of a random variable is
Var X = E [(X −E X)2].
This is also equal to
E [X2] −(E X)2.
It is an easy consequence of the multiplication theorem that if X and Y are independent,
Var (X + Y ) = Var X + Var Y.
The expression E [X2] is sometimes called the second moment of X.
We close this section with a definition of conditional probability. The probability
of A given B, written P(A | B) is defined by
P(A ∩B)
P(B)
,
provided P(B) ̸= 0. The conditional expectation of X given B is defined to be
E [X; B]
P(B) ,
provided P(B) ̸= 0. The notation E [X; B] means E [X1B], where 1B(ω) is 1 if ω ∈B and
0 otherwise. Another way of writing E [X; B] is
E [X; B] =
X
ω∈B
X(ω)P({ω}).
(We will use the notation E [X; B] frequently.)
Note 1. Suppose we have two disjoint sets C and D. Let A1 = C, A2 = D, and Ai = ∅for
i ≥3. Then the Ai are pairwise disjoint and
P(C ∪D) = P(∪∞
i=1Ai) =
∞
X
i=1
P(Ai) = P(C) + P(D)
(2.1)
by Definition 2.2(3) and (4). Therefore Definition 2.2(4) holds when there are only two sets
instead of infinitely many, and a similar argument shows the same is true when there are an
arbitrary (but finite) number of sets.
Now suppose A ⊂B. Let C = A and D = B −A, where B −A is defined to be
B ∩Ac (this is frequently written B \ A as well). Then C and D are disjoint, and by (2.1)
P(B) = P(C ∪D) = P(C) + P(D) ≥P(C) = P(A).
The other equality we mentioned is proved by letting C = A and D = Ac. Then C and
D are disjoint, and
1 = P(Ω) = P(C ∪D) = P(C) + P(D) = P(A) + P(Ac).
Solving for P(Ac), we have
P(Ac) = 1 −P(A).
Note 2.
Let us show the two definitions of expectation are the same (in the discrete case).
Starting with the first definition we have
E X =
X
x
xP(X = x)
=
X
x
x
X
{ω∈Ω:X(ω)=x}
P({ω})
=
X
x
X
{ω∈Ω:X(ω)=x}
X(ω)P({ω})
=
X
ω∈Ω
X(ω)P({ω}),
and we end up with the second definition.
Note 3.
Suppose X can takes the values x1, x2, . . . and Y can take the values y1, y2, . . ..
Let Ai = {ω : X(ω) = xi} and Bj = {ω : Y (ω) = yj}. Then
X =
X
i
xi1Ai,
Y =
X
j
yj1Bj,
and so
XY =
X
i
X
j
xiyi1Ai1Bj.
Since 1Ai1Bj = 1Ai∩Bj, it follows that
E [XY ] =
X
i
X
j
xiyjP(Ai ∩Bj),
assuming the double sum converges. Since X and Y are independent, Ai = (X = xi) is
independent of Bj = (Y = yj) and so
E [XY ] =
X
i
X
j
xiyjP(Ai)P(Bj)
=
X
i
xiP(Ai)
h X
j
yjP(Bj)
i
=
X
i
xiP(Ai)E Y
= (E X)(E Y ).


## 3. Conditional Expectation

3. Conditional expectation.
Suppose we have 200 men and 100 women, 70 of the men are smokers, and 50 of
the women are smokers. If a person is chosen at random, then the conditional probability
that the person is a smoker given that it is a man is 70 divided by 200, or 35%, while the
conditional probability the person is a smoker given that it is a women is 50 divided by
100, or 50%. We will want to be able to encompass both facts in a single entity.
The way to do that is to make conditional probability a random variable rather
than a number. To reiterate, we will make conditional probabilities random. Let M, W be
man, woman, respectively, and S, Sc smoker and nonsmoker, respectively. We have
P(S | M) = .35,
P(S | W) = .50.
We introduce the random variable
(.35)1M + (.50)1W
and use that for our conditional probability. So on the set M its value is .35 and on the
set W its value is .50.
We need to give this random variable a name, so what we do is let G be the σ-field
consisting of {∅, Ω, M, W} and denote this random variable P(S | G). Thus we are going
to talk about the conditional probability of an event given a σ-field.
What is the precise definition?
Definition 3.1. Suppose there exist finitely (or countably) many sets B1, B2, . . ., all hav-
ing positive probability, such that they are pairwise disjoint, Ωis equal to their union, and
G is the σ-field one obtains by taking all finite or countable unions of the Bi. Then the
conditional probability of A given G is
P(A | G) =
X
i
P(A ∩Bi)
P(Bi)
1Bi(ω).
In short, on the set Bi the conditional probability is equal to P(A | Bi).
Not every σ-field can be so represented, so this definition will need to be extended
when we get to continuous models. σ-fields that can be represented as in Definition 3.B are
called finitely (or countably) generated and are said to be generated by the sets B1, B2, . . ..
Let’s look at another example. Suppose Ωconsists of the possible results when we
toss a coin three times: HHH, HHT, etc. Let F3 denote all subsets of Ω. Let F1 consist of
the sets ∅, Ω, {HHH, HHT, HTH, HTT}, and {THH, THT, TTH, TTT}. So F1 consists
of those events that can be determined by knowing the result of the first toss. We want to
let F2 denote those events that can be determined by knowing the first two tosses. This will
include the sets ∅, Ω, {HHH, HHT}, {HTH, HTT}, {THH, THT}, {TTH, TTT}. This is
not enough to make F2 a σ-field, so we add to F2 all sets that can be obtained by taking
unions of these sets.
Suppose we tossed the coin independently and suppose that it was fair. Let us
calculate P(A | F1), P(A | F2), and P(A | F3) when A is the event {HHH}.
First
the conditional probability given F1. Let C1 = {HHH, HHT, HTH, HTT} and C2 =
{THH, THT, TTH, TTT}. On the set C1 the conditional probability is P(A∩C1)/P(C1) =
P(HHH)/P(C1) = 1
8/ 1
2 = 1
4. On the set C2 the conditional probability is P(A∩C2)/P(C2)
= P(∅)/P(C2) = 0. Therefore P(A | F1) = (.25)1C1. This is plausible – the probability of
getting three heads given the first toss is 1
4 if the first toss is a heads and 0 otherwise.
Next let us calculate P(A | F2). Let D1 = {HHH, HHT}, D2 = {HTH, HTT}, D3
= {THH, THT}, D4 = {TTH, TTT}. So F2 is the σ-field consisting of all possible unions
of some of the Di’s. P(A | D1) = P(HHH)/P(D1) = 1
8/ 1
4 = 1
2. Also, as above, P(A |
Di) = 0 for i = 2, 3, 4. So P(A | F2) = (.50)1D1. This is again plausible – the probability
of getting three heads given the first two tosses is 1
2 if the first two tosses were heads and
0 otherwise.
What about conditional expectation? Recall E [X; Bi] = E [X1Bi] and also that
E [1B] = 1 · P(1B = 1) + 0 · P(1B = 0) = P(B). Given a random variable X, we define
E [X | G] =
X
i
E [X; Bi]
P(Bi) 1Bi.
This is the obvious definition, and it agrees with what we had before because E [1A | G]
should be equal to P(A | G).
We now turn to some properties of conditional expectation. Some of the following
propositions may seem a bit technical. In fact, they are! However, these properties are
crucial to what follows and there is no choice but to master them.
Proposition 3.2. E [X | G] is G measurable, that is, if Y = E [X | G], then (Y > a) is a
set in G for each real a.
Proof. By the definition,
Y = E [X | G] =
X
i
E [X; Bi]
P(Bi) 1Bi =
X
i
bi1Bi
if we set bi = E [X; Bi]/P(Bi). The set (Y ≥a) is a union of some of the Bi, namely, those
Bi for which bi ≥a. But the union of any collection of the Bi is in G.
An example might help. Suppose
Y = 2 · 1B1 + 3 · 1B2 + 6 · 1B3 + 4 · 1B4
and a = 3.5. Then (Y ≥a) = B3 ∪B4, which is in G.
Proposition 3.3. If C ∈G and Y = E [X | G], then E [Y ; C] = E [X; C].
Proof. Since Y = P E [X;Bi]
P(Bi) 1Bi and the Bi are disjoint, then
E [Y ; Bj] = E [X; Bj]
P(Bj) E 1Bj = E [X; Bj].
Now if C = Bj1 ∪· · · ∪Bjn ∪· · ·, summing the above over the jk gives E [Y ; C] = E [X; C].
Let us look at the above example for this proposition, and let us do the case where
C = B2. Note 1B21B2 = 1B2 because the product is 1 · 1 = 1 if ω is in B2 and 0 otherwise.
On the other hand, it is not possible for an ω to be in more than one of the Bi, so
1B21Bi = 0 if i ̸= 2. Multiplying Y in the above example by 1B2, we see that
E [Y ; C] = E [Y ; B2] = E [Y 1B2] = E [3 · 1B2]
= 3E [1B2] = 3P(B2).
However the number 3 is not just any number; it is E [X; B2]/P(B2). So
3P(B2) = E [X; B2]
P(B2) P(B2) = E [X; B2] = E [X; C],
just as we wanted. If C = B1 ∪B4, for example, we then write
E [X; C] = E [X1C] = E [X(1B2 + 1B4)]
= E [X1B2] + E [X1B4] = E [X; B2] + E [X; B4].
By the first part, this equals E [Y ; B2]+E [Y ; B4], and we undo the above string of equalities
but with Y instead of X to see that this is E [Y ; C].
If a r.v. Y is G measurable, then for any a we have (Y = a) ∈G which means that
(Y = a) is the union of one or more of the Bi. Since the Bi are disjoint, it follows that Y
must be constant on each Bi.
Again let us look at an example. Suppose Z takes only the values 1, 3, 4, 7. Let
D1 = (Z = 1), D2 = (Z = 3), D3 = (Z = 4), D4 = (Z = 7). Note that we can write
Z = 1 · 1D1 + 3 · 1D2 + 4 · 1D3 + 7 · 1D4.
To see this, if ω ∈D2, for example, the right hand side will be 0+3·1+0+0, which agrees
with Z(ω). Now if Z is G measurable, then (Z ≥a) ∈G for each a. Take a = 7, and we
see D4 ∈G. Take a = 4 and we see D3 ∪D4 ∈G. Taking a = 3 shows D2 ∪D3 ∪D4 ∈G.
Now D3 = (D3 ∪D4) ∩Dc
4, so since G is a σ-field, D3 ∈G. Similarly D2, D1 ∈G. Because
sets in G are unions of the Bi’s, we must have Z constant on the Bi’s. For example, if it
so happened that D1 = B1, D2 = B2 ∪B4, D3 = B3 ∪B6 ∪B7, and D4 = B5, then
Z = 1 · 1B1 + 3 · 1B2 + 4 · 1B3 + 3 · 1B4 + 7 · 1B5 + +4 · 1B6 + 4 · 1B7.
We still restrict ourselves to the discrete case. In this context, the properties given
in Propositions 3.2 and 3.3 uniquely determine E [X | G].
Proposition 3.4. Suppose Z is G measurable and E [Z; C] = E [X; C] whenever C ∈G.
Then Z = E [X | G].
Proof. Since Z is G measurable, then Z must be constant on each Bi. Let the value of Z
on Bi be zi. So Z = P
i zi1Bi. Then
ziP(Bi) = E [Z; Bi] = E [X; Bi],
or zi = E [X; Bi]/P(Bi) as required.
The following propositions contain the main facts about this new definition of con-
ditional expectation that we will need.
Proposition 3.5. (1) If X1 ≥X2, then E [X1 | G] ≥E [X2 | G].
(2) E [aX1 + bX2 | G] = aE [X1 | G] + bE [X2 | G].
(3) If X is G measurable, then E [X | G] = X.
(4) E [E [X | G]] = E X.
(5) If X is independent of G, then E [X | G] = E X.
We will prove Proposition 3.5 in Note 1 at the end of the section. At this point it
is more fruitful to understand what the proposition says.
We will see in Proposition 3.8 below that we may think of E [X | G] as the best
prediction of X given G. Accepting this for the moment, we can give an interpretation of
(1)-(5). (1) says that if X1 is larger than X2, then the predicted value of X1 should be
larger than the predicted value of X2. (2) says that the predicted value of X1 + X2 should
be the sum of the predicted values. (3) says that if we know G and X is G measurable,
then we know X and our best prediction of X is X itself. (4) says that the average of the
predicted value of X should be the average value of X. (5) says that if knowing G gives us
no additional information on X, then the best prediction for the value of X is just E X.
Proposition 3.6. If Z is G measurable, then E [XZ | G] = ZE [X | G].
We again defer the proof, this time to Note 2.
Proposition 3.6 says that as far as conditional expectations with respect to a σ-
field G go, G-measurable random variables act like constants: they can be taken inside or
outside the conditional expectation at will.
Proposition 3.7. If H ⊂G ⊂F, then
E [E [X | H] | G] = E [X | H] = E [E [X | G] | H].
Proof.
E [X | H] is H measurable, hence G measurable, since H ⊂G. The left hand
equality now follows by Proposition 3.5(3). To get the right hand equality, let W be the
right hand expression. It is H measurable, and if C ∈H ⊂G, then
E [W; C] = E [E [X | G]; C] = E [X; C]
as required.
In words, if we are predicting a prediction of X given limited information, this is
the same as a single prediction given the least amount of information.
Let us verify that conditional expectation may be viewed as the best predictor of
a random variable given a σ-field. If X is a r.v., a predictor Z is just another random
variable, and the goodness of the prediction will be measured by E [(X −Z)2], which is
known as the mean square error.
Proposition 3.8. If X is a r.v., the best predictor among the collection of G-measurable
random variables is Y = E [X | G].
Proof.
Let Z be any G-measurable random variable. We compute, using Proposition
3.5(3) and Proposition 3.6,
E [(X −Z)2 | G] = E [X2 | G] −2E [XZ | G] + E [Z2 | G]
= E [X2 | G] −2ZE [X | G] + Z2
= E [X2 | G] −2ZY + Z2
= E [X2 | G] −Y 2 + (Y −Z)2
= E [X2 | G] −2Y E [X | G] + Y 2 + (Y −Z)2
= E [X2 | G] −2E [XY | G] + E [Y 2 | G] + (Y −Z)2
= E [(X −Y )2 | G] + (Y −Z)2.
We also used the fact that Y is G measurable. Taking expectations and using Proposition
3.5(4),
E [(X −Z)2] = E [(X −Y )2] + E [(Y −Z)2].
The right hand side is bigger than or equal to E [(X −Y )2] because (Y −Z)2 ≥0. So the
error in predicting X by Z is larger than the error in predicting X by Y , and will be equal
if and only if Z = Y . So Y is the best predictor.
There is one more interpretation of conditional expectation that may be useful. The
collection of all random variables is a linear space, and the collection of all G-measurable
random variables is clearly a subspace. Given X, the conditional expectation Y = E [X | G]
is equal to the projection of X onto the subspace of G-measurable random variables. To
see this, we write X = Y + (X −Y ), and what we have to check is that the inner product
of Y and X −Y is 0, that is, Y and X −Y are orthogonal. In this context, the inner
product of X1 and X2 is defined to be E [X1X2], so we must show E [Y (X −Y )] = 0. Note
E [Y (X −Y ) | G] = Y E [X −Y | G] = Y (E [X | G] −Y ) = Y (Y −Y ) = 0.
Taking expectations,
E [Y (X −Y )] = E [E [Y (X −Y ) | G] ] = 0,
just as we wished.
If Y is a discrete random variable, that is, it takes only countably many values
y1, y2, . . ., we let Bi = (Y = yi). These will be disjoint sets whose union is Ω. If σ(Y )
is the collection of all unions of the Bi, then σ(Y ) is a σ-field, and is called the σ-field
generated by Y . It is easy to see that this is the smallest σ-field with respect to which Y
is measurable. We write E [X | Y ] for E [X | σ(Y )].
Note 1. We prove Proposition 3.5. (1) and (2) are immediate from the definition. To prove
(3), note that if Z = X, then Z is G measurable and E [X; C] = E [Z; C] for any C ∈G; this
is trivial. By Proposition 3.4 it follows that Z = E [X | G];this proves (3). To prove (4), if we
let C = Ωand Y = E [X | G], then E Y = E [Y ; C] = E [X; C] = E X.
Last is (5).
Let Z = E X.
Z is constant, so clearly G measurable.
By the in-
dependence, if C ∈G, then E [X; C] = E [X1C] = (E X)(E 1C) = (E X)(P(C)).
But
E [Z; C] = (E X)(P(C)) since Z is constant. By Proposition 3.4 we see Z = E [X | G].
Note 2. We prove Proposition 3.6. Note that ZE [X | G] is G measurable, so by Proposition
3.4 we need to show its expectation over sets C in G is the same as that of XZ. As in the
proof of Proposition 3.3, it suffices to consider only the case when C is one of the Bi. Now Z
is G measurable, hence it is constant on Bi; let its value be zi. Then
E [ZE [X | G]; Bi] = E [ziE [X | G]; Bi] = ziE [E [X | G]; Bi] = ziE [X; Bi] = E [XZ; Bi]
as desired.


## 4. Martingales

4. Martingales.
Suppose we have a sequence of σ-fields F1 ⊂F2 ⊂F3 · · ·. An example would be
repeatedly tossing a coin and letting Fk be the sets that can be determined by the first
k tosses. Another example is to let Fk be the events that are determined by the values
of a stock at times 1 through k. A third example is to let X1, X2, . . . be a sequence of
random variables and let Fk be the σ-field generated by X1, . . . , Xk, the smallest σ-field
with respect to which X1, . . . , Xk are measurable.
Definition 4.1. A r.v. X is integrable if E |X| < ∞. Given an increasing sequence of
σ-fields Fn, a sequence of r.v.’s Xn is adapted if Xn is Fn measurable for each n.
Definition 4.2. A martingale Mn is a sequence of random variables such that
(1) Mn is integrable for all n,
(2) Mn is adapted to Fn, and
(3) for all n
E [Mn+1 | Fn] = Mn.
(4.1)
Usually (1) and (2) are easy to check, and it is (3) that is the crucial property. If
we have (1) and (2), but instead of (3) we have
(3′) for all n
E [Mn+1 | Fn] ≥Mn,
then we say Mn is a submartingale. If we have (1) and (2), but instead of (3) we have
(3′′) for all n
E [Mn+1 | Fn] ≤Mn,
then we say Mn is a supermartingale.
Submartingales tends to increase and supermartingales tend to decrease.
The
nomenclature may seem like it goes the wrong way; Doob defined these terms by anal-
ogy with the notions of subharmonic and superharmonic functions in analysis. (Actually,
it is more than an analogy: we won’t explore this, but it turns out that the composition
of a subharmonic function with Brownian motion yields a submartingale, and similarly for
superharmonic functions.)
Note that the definition of martingale depends on the collection of σ-fields. When
it is needed for clarity, one can say that (Mn, Fn) is a martingale. To define conditional
expectation, one needs a probability, so a martingale depends on the probability as well.
When we need to, we will say that Mn is a martingale with respect to the probability P.
This is an issue when there is more than one probability around.
We will see that martingales are ubiquitous in financial math. For example, security
prices and one’s wealth will turn out to be examples of martingales.
The word “martingale” is also used for the piece of a horse’s bridle that runs from
the horse’s head to its chest. It keeps the horse from raising its head too high. It turns out
that martingales in probability cannot get too large. The word also refers to a gambling
system. I did some searching on the Internet, and there seems to be no consensus on the
derivation of the term.
Here is an example of a martingale. Let X1, X2, . . . be a sequence of independent
r.v.’s with mean 0 that are independent. (Saying a r.v. Xi has mean 0 is the same as
saying E Xi = 0; this presupposes that E |X1| is finite.) Set Fn = σ(X1, . . . , Xn), the
σ-field generated by X1, . . . , Xn. Let Mn = Pn
i=1 Xi. Definition 4.2(2) is easy to see.
Since E |Mn| ≤Pn
i=1 E |Xi|, Definition 4.2(1) also holds. We now check
E [Mn+1 | Fn] = X1 + · · · + Xn + E [Xn+1 | Fn] = Mn + E Xn+1 = Mn,
where we used the independence.
Another example: suppose in the above that the Xk all have variance 1, and let
Mn = S2
n −n, where Sn = Pn
i=1 Xi. Again (1) and (2) of Definition 4.2 are easy to check.
We compute
E [Mn+1 | Fn] = E [S2
n + 2Xn+1Sn + X2
n+1 | Fn] −(n + 1).
We have E [S2
n | Fn] = S2
n since Sn is Fn measurable.
E [2Xn+1Sn | Fn] = 2SnE [Xn+1 | Fn] = 2SnE Xn+1 = 0.
And E [X2
n+1 | Fn] = E X2
n+1 = 1. Substituting, we obtain E [Mn+1 | Fn] = Mn, or Mn is
a martingale.
A third example: Suppose you start with a dollar and you are tossing a fair coin
independently. If it turns up heads you double your fortune, tails you go broke. This is
“double or nothing.” Let Mn be your fortune at time n. To formalize this, let X1, X2, . . .
be independent r.v.’s that are equal to 2 with probability 1
2 and 0 with probability 1
2. Then
Mn = X1 · · · Xn. Let Fn be the σ-field generated by X1, . . . , Xn. Note 0 ≤Mn ≤2n, and
so Definition 4.2(1) is satisfied, while (2) is easy. To compute the conditional expectation,
note E Xn+1 = 1. Then
E [Mn+1 | Fn] = MnE [Xn+1 | Fn] = MnE Xn+1 = Mn,
using the independence.
Before we give our fourth example, let us observe that
|E [X | F]| ≤E [|X| | F].
(4.2)
To see this, we have −|X| ≤X ≤|X|, so −E [|X| | F] ≤E [X | F] ≤E [|X| | F]. Since
E [|X| | F] is nonnegative, (4.2) follows.
Our fourth example will be used many times, so we state it as a proposition.
Proposition 4.3. Let F1, F2, . . . be given and let X be a fixed r.v. with E |X| < ∞. Let
Mn = E [X | Fn]. Then Mn is a martingale.
Proof. Definition 4.2(2) is clear, while
E |Mn| ≤E [E [|X| | Fn]] = E |X| < ∞
by (4.2); this shows Definition 4.2(1). We have
E [Mn+1 | Fn] = E [E [X | Fn+1] | Fn] = E [X | Fn] = Mn.


## 5. Properties of Martingales

5. Properties of martingales.
When it comes to discussing American options, we will need the concept of stopping
times. A mapping τ from Ωinto the nonnegative integers is a stopping time if (τ = k) ∈Fk
for each k.
An example is τ = min{k : Sk ≥A}. This is a stopping time because (τ = k) =
(S1, . . . , Sk−1 < A, Sk ≥A) ∈Fk. We can think of a stopping time as the first time
something happens. σ = max{k : Sk ≥A}, the last time, is not a stopping time. (We will
use the convention that the minimum of an empty set is +∞; so, for example, with the
above definition of τ, on the event that Sk is never in A, we have τ = ∞.
Here is an intuitive description of a stopping time. If I tell you to drive to the city
limits and then drive until you come to the second stop light after that, you know when
you get there that you have arrived; you don’t need to have been there before or to look
ahead. But if I tell you to drive until you come to the second stop light before the city
limits, either you must have been there before or else you have to go past where you are
supposed to stop, continue on to the city limits, and then turn around and come back two
stop lights. You don’t know when you first get to the second stop light before the city
limits that you get to stop there. The first set of instructions forms a stopping time, the
second set does not.
Note (τ ≤k) = ∪k
j=0(τ = j). Since (τ = j) ∈Fj ⊂Fk, then the event (τ ≤k) ∈Fk
for all k. Conversely, if τ is a r.v. with (τ ≤k) ∈Fk for all k, then
(τ = k) = (τ ≤k) −(τ ≤k −1).
Since (τ ≤k) ∈Fk and (τ ≤k −1) ∈Fk−1 ⊂Fk, then (τ = k) ∈Fk, and such a τ must
be a stopping time.
Our first result is Jensen’s inequality.
Proposition 5.1. If g is convex, then
g(E [X | G]) ≤E [g(X) | G]
provided all the expectations exist.
For ordinary expectations rather than conditional expectations, this is still true.
That is, if g is convex and the expectations exist, then
g(E X) ≤E [g(X)].
We already know some special cases of this: when g(x) = |x|, this says |E X| ≤E |X|;
when g(x) = x2, this says (E X)2 ≤E X2, which we know because E X2 −(E X)2 =
E (X −E X)2 ≥0.
For Proposition 5.1 as well as many of the following propositions, the statement of
the result is more important than the proof, and we relegate the proof to Note 1 below.
One reason we want Jensen’s inequality is to show that a convex function applied
to a martingale yields a submartingale.
Proposition 5.2. If Mn is a martingale and g is convex, then g(Mn) is a submartingale,
provided all the expectations exist.
Proof. By Jensen’s inequality,
E [g(Mn+1) | Fn] ≥g(E [Mn+1 | Fn]) = g(Mn).
If Mn is a martingale, then E Mn = E [E [Mn+1 | Fn]] = E Mn+1.
So E M0 =
E M1 = · · · = E Mn. Doob’s optional stopping theorem says the same thing holds when
fixed times n are replaced by stopping times.
Theorem 5.3. Suppose K is a positive integer, N is a stopping time such that N ≤K
a.s., and Mn is a martingale. Then
E MN = E MK.
Here, to evaluate MN, one first finds N(ω) and then evaluates M·(ω) for that value of N.
Proof. We have
E MN =
K
X
k=0
E [MN; N = k].
If we show that the k-th summand is E [Mn; N = k], then the sum will be
K
X
k=0
E [Mn; N = k] = E Mn
as desired. We have
E [MN; N = k] = E [Mk; N = k]
by the definition of MN. Now (N = k) is in Fk, so by Proposition 2.2 and the fact that
Mk = E [Mk+1 | Fk],
E [Mk; N = k] = E [Mk+1; N = k].
We have (N = k) ∈Fk ⊂Fk+1. Since Mk+1 = E [Mk+2 | Fk+1], Proposition 2.2 tells us
that
E [Mk+1; N = k] = E [Mk+2; N = k].
We continue, using (N = k) ∈Fk ⊂Fk+1 ⊂Fk+2, and we obtain
E [MN; N = k] = E [Mk; N = k] = E [Mk+1; N = k] = · · · = E [Mn; N = k].
If we change the equalities in the above to inequalities, the same result holds for sub-
martingales.
As a corollary we have two of Doob’s inequalities:
Theorem 5.4. If Mn is a nonnegative submartingale,
(a)
P(maxk≤n Mk ≥λ) ≤1
λE Mn.
(b)
E (maxk≤n M 2
k) ≤4E M 2
n.
For the proof, see Note 2 below.
Note 1.
We prove Proposition 5.1. If g is convex, then the graph of g lies above all the
tangent lines. Even if g does not have a derivative at x0, there is a line passing through x0
which lies beneath the graph of g. So for each x0 there exists c(x0) such that
g(x) ≥g(x0) + c(x0)(x −x0).
Apply this with x = X(ω) and x0 = E \[X | G\](ω). We then have
g(X) ≥g(E [X | G]) + c(E [X | G])(X −E [X | G]).
If g is differentiable, we let c(x0) = g′(x0). In the case where g is not differentiable, then we
choose c to be the left hand upper derivate, for example. (For those who are not familiar with
derivates, this is essentially the left hand derivative.) One can check that if c is so chosen,
then c(E [X | G]) is G measurable.
Now take the conditional expectation with respect to G. The first term on the right is
G measurable, so remains the same. The second term on the right is equal to
c(E [X | G])E [X −E [X | G] | G] = 0.
Note 2.
We prove Theorem 5.4. Set Mn+1 = Mn. It is easy to see that the sequence
M1, M2, . . . , Mn+1 is also a submartingale. Let N = min{k : Mk ≥λ} ∧(n + 1), the first
time that Mk is greater than or equal to λ, where a ∧b = min(a, b). Then
P(max
k≤n Mk ≥λ) = P(N ≤n)
and if N ≤n, then MN ≥λ. Now
P(max
k≤n Mk ≥λ) = E [1(N≤n)] ≤E
hMN
λ ; N ≤n
i
(5.1)
= 1
λE [MN∧n; N ≤n] ≤1
λE MN∧n.
Finally, since Mn is a submartingale, E MN∧n ≤E Mn.
We now look at (b). Let us write M ∗for maxk≤n Mk. If E M 2
n = ∞, there is nothing
to prove. If it is finite, then by Jensen’s inequality, we have
E M 2
k = E [E [Mn | Fk]2] ≤E [E [M 2
n | Fk] ] = E M 2
n < ∞
for k ≤n. Then
E (M ∗)2 = E [ max
1≤k≤n M 2
k] ≤E
h
n
X
k=1
M 2
k

< ∞.
We have
E [MN∧n; N ≤n] =
∞
X
k=0
E [Mk∧n; N = k].
Arguing as in the proof of Theorem 5.3,
E [Mk∧n; N = k] ≤E [Mn; N = k],
and so
E [MN∧n; N ≤n] ≤
∞
X
k=0
E [Mn; N = k] = E [Mn; N ≤n].
The last expression is at most E [Mn; M ∗≥λ]. If we multiply (5.1) by 2λ and integrate over
λ from 0 to ∞, we obtain
Z ∞
2λP(M ∗≥λ)dλ ≤2
Z ∞
E [Mn : M ∗≥λ]
= 2E
Z ∞
Mn1(M ∗≥λ)dλ
= 2E
h
Mn
Z M ∗
dλ
i
= 2E [MnM ∗].
Using Cauchy-Schwarz, this is bounded by
2(E M 2
n)1/2(E (M ∗)2)1/2.
On the other hand,
Z ∞
2λP(M ∗≥λ)dλ = E
Z ∞
2λ1(M ∗≥λ)dλ
= E
Z M ∗
2λ dλ = E (M ∗)2.
We therefore have
E (M ∗)2 ≤2(E M 2
n)1/2(E (M ∗)2)1/2.
Recall we showed E (M ∗)2 < ∞. We divide both sides by (E (M ∗)2)1/2, square both sides,
and obtain (b).
Note 3. We will show that bounded martingales converge. (The hypothesis of boundedness
can be weakened; for example, E |Mn| ≤c < ∞for some c not depending on n suffices.)
Theorem 5.5. Suppose Mn is a martingale bounded in absolute value by K. That is,
|Mn| ≤K for all n. Then limn→∞Mn exists a.s.
Proof. Since Mn is bounded, it can’t tend to +∞or −∞. The only possibility is that it
might oscillate. Let a < b be two rationals. What might go wrong is that Mn might be larger
than b infinitely often and less than a infinitely often. If we show the probability of this is 0,
then taking the union over all pairs of rationals (a, b) shows that almost surely Mn cannot
oscillate, and hence must converge.
Fix a < b, let Nn = (Mn −a)+, and let S1 = min{k : Nk ≤0}, T1 = min{k > S1 :
Nk ≥b −a}, S2 = min{k > T1 : Nk ≤0}, and so on. Let Un = max{k : Tk ≤n}. Un
is called the number of upcrossings up to time n. We want to show that maxn Un < ∞a.s.
Note by Jensen’s inequality Nn is a submartingale. Since S1 < T1 < S2 < · · ·, then Sn+1 > n.
We can write
2K ≥Nn −NSn+1∧n =
n+1
X
k=1
(NSk+1∧n −NTk∧n) +
n+1
X
k=1
(NTk∧n −NSk∧n).
Now take expectations. The expectation of the first sum on the right and the last term are
greater than or equal to zero by optional stopping. The middle term is larger than (b −a)Un,
so we conclude
(b −a)E Un ≤2K.
Let n →∞to see that E maxn Un < ∞, which implies maxn Un < ∞a.s., which is what we
needed.
Note 4. We will state Fatou’s lemma in the following form.
If Xn is a sequence of nonnegative random variables converging to X a.s., then E X ≤
supn E Xn.
This formulation is equivalent to the classical one and is better suited for our use.


## 6. The One-Step Binomial Asset Pricing Model

6. The one step binomial asset pricing model.
Let us begin by giving the simplest possible model of a stock and see how a European
call option should be valued in this context.
Suppose we have a single stock whose price is S0. Let d and u be two numbers with
0 < d < 1 < u. Here “d” is a mnemonic for “down” and “u” for “up.” After one time unit
the stock price will be either uS0 with probability P or else dS0 with probability Q, where
P + Q = 1. We will assume 0 < P, Q < 1. Instead of purchasing shares in the stock, you
can also put your money in the bank where one will earn interest at rate r. Alternatives
to the bank are money market funds or bonds; the key point is that these are considered
to be risk-free.
A European call option in this context is the option to buy one share of the stock
at time 1 at price K. K is called the strike price. Let S1 be the price of the stock at time
1. If S1 is less than K, then the option is worthless at time 1. If S1 is greater than K, you
can use the option at time 1 to buy the stock at price K, immediately turn around and
sell the stock for price S1 and make a profit of S1 −K. So the value of the option at time
1 is
V1 = (S1 −K)+,
where x+ is max(x, 0). The principal question to be answered is: what is the value V0 of
the option at time 0? In other words, how much should one pay for a European call option
with strike price K?
It is possible to buy a negative number of shares of a stock. This is equivalent to
selling shares of a stock you don’t have and is called selling short. If you sell one share
of stock short, then at time 1 you must buy one share at whatever the market price is at
that time and turn it over to the person that you sold the stock short to. Similarly you
can buy a negative number of options, that is, sell an option.
You can also deposit a negative amount of money in the bank, which is the same
as borrowing. We assume that you can borrow at the same interest rate r, not exactly a
totally realistic assumption. One way to make it seem more realistic is to assume you have
a large amount of money on deposit, and when you borrow, you simply withdraw money
from that account.
We are looking at the simplest possible model, so we are going to allow only one
time step: one makes an investment, and looks at it again one day later.
Let’s suppose the price of a European call option is V0 and see what conditions
one can put on V0. Suppose you start out with V0 dollars. One thing you could do is
buy one option.
The other thing you could do is use the money to buy ∆0 shares of
stock. If V0 > ∆0S0, there will be some money left over and you put that in the bank. If
V0 < ∆0S0, you do not have enough money to buy the stock, and you make up the shortfall
by borrowing money from the bank. In either case, at this point you have V0 −∆0S0 in
the bank and ∆0 shares of stock.
If the stock goes up, at time 1 you will have
∆0uS0 + (1 + r)(V0 −∆0S0),
and if it goes down,
∆0dS0 + (1 + r)(V0 −∆0S0).
We have not said what ∆0 should be. Let us do that now. Let V u
1 = (uS0 −K)+
and V d
1 = (dS0 −K)+. Note these are deterministic quantities, i.e., not random. Let
∆0 = V u
1 −V d
uS0 −dS0
,
and we will also need
W0 =
1 + r
h1 + r −d
u −d
V u
1 + u −(1 + r)
u −d
V d
i
.
In a moment we will do some algebra and see that if the stock goes up and you had
bought stock instead of the option you would now have
V u
1 + (1 + r)(V0 −W0),
while if the stock went down, you would now have
V d
1 + (1 + r)(V0 −W0).
Let’s check the first of these, the second being similar. We need to show
∆0uS0 + (1 + r)(V0 −∆0S0) = V u
1 + (1 + r)(V0 −W0).
(6.1)
The left hand side of (6.1) is equal to
∆0S0(u −(1 + r)) + (1 + r)V0 = V u
1 −V d
u −d
(u −(1 + r)) + (1 + r)V0.
(6.2)
The right hand side of (6.1) is equal to
V u
1 −
h1 + r −d
u −d
V u
1 + u −(1 + r)
u −d
V d
i
+ (1 + r)V0.
(6.3)
Now check that the coefficients of V0, of V u
1 , and of V d
1 agree in (6.2) and (6.3).
Suppose that V0 > W0. What you want to do is come along with no money, sell
one option for V0 dollars, use the money to buy ∆0 shares, and put the rest in the bank
(or borrow if necessary). If the buyer of your option wants to exercise the option, you give
him one share of stock and sell the rest. If he doesn’t want to exercise the option, you sell
your shares of stock and pocket the money. Remember it is possible to have a negative
number of shares. You will have cleared (1 + r)(V0 −W0), whether the stock went up or
down, with no risk.
If V0 < W0, you just do the opposite: sell ∆0 shares of stock short, buy one option,
and deposit or make up the shortfall from the bank. This time, you clear (1+r)(W0 −V0),
whether the stock goes up or down.
Now most people believe that you can’t make a profit on the stock market without
taking a risk. The name for this is “no free lunch,” or “arbitrage opportunities do not
exist.” The only way to avoid this is if V0 = W0. In other words, we have shown that the
only reasonable price for the European call option is W0.
The “no arbitrage” condition is not just a reflection of the belief that one cannot get
something for nothing. It also represents the belief that the market is freely competitive.
The way it works is this: suppose W0 = $3. Suppose you could sell options at a price
V0 = $5; this is larger than W0 and you would earn V0 −W0 = $2 per option without risk.
Then someone else would observe this and decide to sell the same option at a price less
than V0 but larger than W0, say $4. This person would still make a profit, and customers
would go to him and ignore you because they would be getting a better deal. But then a
third person would decide to sell the option for less than your competition but more than
W0, say at $3.50. This would continue as long as any one would try to sell an option above
price W0.
We will examine this problem of pricing options in more complicated contexts, and
while doing so, it will become apparent where the formulas for ∆0 and W0 came from. At
this point, we want to make a few observations.
Remark 6.1. First of all, if 1 + r > u, one would never buy stock, since one can always
do better by putting money in the bank. So we may suppose 1 + r < u. We always have
1 + r ≥1 > d. If we set
p = 1 + r −d
u −d
,
q = u −(1 + r)
u −d
,
then p, q ≥0 and p + q = 1. Thus p and q act like probabilities, but they have nothing to
do with P and Q. Note also that the price V0 = W0 does not depend on P or Q. It does
depend on p and q, which seems to suggest that there is an underlying probability which
controls the option price and is not the one that governs the stock price.
Remark 6.2.
There is nothing special about European call options in our argument
above. One could let V u
1 and V 1
d be any two values of any option, which are paid out if the
stock goes up or down, respectively. The above analysis shows we can exactly duplicate
the result of buying any option V by instead buying some shares of stock. If in some model
one can do this for any option, the market is called complete in this model.
Remark 6.3.
If we let P be the probability so that S1 = uS0 with probability p and
S1 = dS0 with probability q and we let E be the corresponding expectation, then some
algebra shows that
V0 =
1 + rE V1.
This will be generalized later.
Remark 6.4.
If one buys one share of stock at time 0, then one expects at time 1 to
have (Pu + Qd)S0. One then divides by 1 + r to get the value of the stock in today’s
dollars. (r, the risk-free interest rate, can also be considered the rate of inflation. A dollar
tomorrow is equivalent to 1/(1 + r) dollars today.) Suppose instead of P and Q being the
probabilities of going up and down, they were in fact p and q. One would then expect to
have (pu+qd)S0 and then divide by 1+r. Substituting the values for p and q, this reduces
to S0. In other words, if p and q were the correct probabilities, one would expect to have
the same amount of money one started with. When we get to the binomial asset pricing
model with more than one step, we will see that the generalization of this fact is that the
stock price at time n is a martingale, still with the assumption that p and q are the correct
probabilities. This is a special case of the fundamental theorem of finance: there always
exists some probability, not necessarily the one you observe, under which the stock price
is a martingale.
Remark 6.5. Our model allows after one time step the possibility of the stock going up or
going down, but only these two options. What if instead there are 3 (or more) possibilities.
Suppose for example, that the stock goes up a factor u with probability P, down a factor
d with probability Q, and remains constant with probability R, where P + Q + R = 1.
The corresponding price of a European call option would be (uS0 −K)+, (dS0 −K)+, or
(S0 −K)+. If one could replicate this outcome by buying and selling shares of the stock,
then the “no arbitrage” rule would give the exact value of the call option in this model.
But, except in very special circumstances, one cannot do this, and the theory falls apart.
One has three equations one wants to satisfy, in terms of V u
1 , V d
1 , and V c
1 . (The “c” is
a mnemonic for “constant.”) There are however only two variables, ∆0 and V0 at your
disposal, and most of the time three equations in two unknowns cannot be solved.
Remark 6.6.
In our model we ruled out the cases that P or Q were zero. If Q = 0,
that is, we are certain that the stock will go up, then we would always invest in the stock
if u > 1 + r, as we would always do better, and we would always put the money in the
bank if u ≤1 + r. Similar considerations apply when P = 0. It is interesting to note that
the cases where P = 0 or Q = 0 are the only ones in which our derivation is not valid.
It turns out that in more general models the true probabilities enter only in determining
which events have probability 0 or 1 and in no other way.


## 7. The Multi-Step Binomial Asset Pricing Model

7. The multi-step binomial asset pricing model.
In this section we will obtain a formula for the pricing of options when there are n
time steps, but each time the stock can only go up by a factor u or down by a factor d.
The “Black-Scholes” formula we will obtain is already a nontrivial result that is useful.
We assume the following.
(1) Unlimited short selling of stock
(2) Unlimited borrowing
(3) No transaction costs
(4) Our buying and selling is on a small enough scale that it does not affect the market.
We need to set up the probability model. Ωwill be all sequences of length n of H’s
and T’s. S0 will be a fixed number and we define Sk(ω) = ujdk−jS0 if the first k elements
of a given ω ∈Ωhas j occurrences of H and k −j occurrences of T. (What we are doing is
saying that if the j-th element of the sequence making up ω is an H, then the stock price
goes up by a factor u; if T, then down by a factor d.) Fk will be the σ-field generated by
S0, . . . , Sk.
Let
p = (1 + r) −d
u −d
,
q = u −(1 + r)
u −d
and define P(ω) = pjqn−j if ω has j appearances of H and n −j appearances of T. We
observe that under P the random variables Sk+1/Sk are independent and equal to u with
probability p and d with probability q. To see this, let Yk = Sk/Sk−1. Thus Yk is the
factor the stock price goes up or down at time k. Then P(Y1 = y1, . . . , Yn = yn) = pjqn−j,
where j is the number of the yk that are equal to u. On the other hand, this is equal to
P(Y1 = y1) · · · P(Yn = yn). Let E denote the expectation corresponding to P.
The P we construct may not be the true probabilities of going up or down. That
doesn’t matter - it will turn out that using the principle of “no arbitrage,” it is P that
governs the price.
Our first result is the fundamental theorem of finance in the current context.
Proposition 7.1. Under P the discounted stock price (1 + r)−kSk is a martingale.
Proof. Since the random variable Sk+1/Sk is independent of Fk, we have
E [(1 + r)−(k+1)Sk+1 | Fk] = (1 + r)−kSk(1 + r)−1E [Sk+1/Sk | Fk].
Using the independence the conditional expectation on the right is equal to
E [Sk+1/Sk] = pu + qd = 1 + r.
Substituting yields the proposition.
Let ∆k be the number of shares held between times k and k + 1. We require ∆k
to be Fk measurable. ∆0, ∆1, . . . is called the portfolio process. Let W0 be the amount
of money you start with and let Wk be the amount of money you have at time k. Wk is
the wealth process. If we have ∆k shares between times k and k + 1, then at time k + 1
those shares will be worth ∆kSk+1. The amount of cash we hold between time k and k +1
is Wk minus the amount held in stock, that is, Wk −∆kSk. At time k + 1 this is worth
(1 + r)[Wk −∆kSk]. Therefore
Wk+1 = ∆kSk+1 + (1 + r)[Wk −∆kSk].
Note that in the case where r = 0 we have
Wk+1 −Wk = ∆k(Sk+1 −Sk),
or
Wk+1 = W0 +
k
X
i=0
∆i(Si+1 −Si).
This is a discrete version of a stochastic integral. Since
E [Wk+1 −Wk | Fk] = ∆kE [Sk+1 −Sk | Fk] = 0,
it follows that in the case r = 0 that Wk is a martingale. More generally
Proposition 7.2. Under P the discounted wealth process (1 + r)−kWk is a martingale.
Proof. We have
(1 + r)−(k+1)Wk+1 = (1 + r)−kWk + ∆k[(1 + r)−(k+1)Sk+1 −(1 + r)−kSk].
Observe that
E [∆k[(1 + r)−(k+1)Sk+1 −(1 + r)−kSk | Fk]
= ∆kE [(1 + r)−(k+1)Sk+1 −(1 + r)−kSk | Fk] = 0.
The result follows.
Our next result is that the binomial model is complete. It is easy to lose the idea
in the algebra, so first let us try to see why the theorem is true.
For simplicity let us first consider the case r = 0. Let Vk = E [V | Fk]; by Propo-
sition 4.3 we see that Vk is a martingale. We want to construct a portfolio process, i.e.,
choose ∆k’s, so that Wn = V . We will do it inductively by arranging matters so that
Wk = Vk for all k. Recall that Wk is also a martingale.
Suppose we have Wk = Vk at time k and we want to find ∆k so that Wk+1 = Vk+1.
At the (k + 1)-st step there are only two possible changes for the price of the stock and so
since Vk+1 is Fk+1 measurable, only two possible values for Vk+1. We need to choose ∆k
so that Wk+1 = Vk+1 for each of these two possibilities. We only have one parameter, ∆k,
to play with to match up two numbers, which may seem like an overconstrained system of
equations. But both V and W are martingales, which is why the system can be solved.
Now let us turn to the details. In the following proof we allow r ≥0.
Theorem 7.3. The binomial asset pricing model is complete.
The precise meaning of this is the following.
If V is any random variable that is Fn
measurable, there exists a constant W0 and a portfolio process ∆k so that the wealth
process Wk satisfies Wn = V . In other words, starting with W0 dollars, we can trade
shares of stock to exactly duplicate the outcome of any option V .
Proof. Let
Vk = (1 + r)kE [(1 + r)−nV | Fk].
By Proposition 4.3 (1 + r)−kVk is a martingale. If ω = (t1, . . . , tn), where each ti is an H
or T, let
∆k(ω) = Vk+1(t1, . . . , tk, H, tk+2, . . . , tn) −Vk+1(t1, . . . , tk, T, tk+2, . . . , tn)
Sk+1(t1, . . . , tk, H, tk+2, . . . , tn) −Sk+1(t1, . . . , tk, T, tk+2, . . . , tn).
Set W0 = V0, and we will show by induction that the wealth process at time k equals Vk.
The first thing to show is that ∆k is Fk measurable. Neither Sk+1 nor Vk+1 depends
on tk+2, . . . , tn. So ∆k depends only on the variables t1, . . . , tk, hence is Fk measurable.
Now tk+2, . . . , tn play no role in the rest of the proof, and t1, . . . , tk will be fixed,
so we drop the t’s from the notation. If we write Vk+1(H), this is an abbreviation for
Vk+1(t1, . . . , tk, H, tk+2, . . . , tn).
We know (1 + r)−kVk is a martingale under P so that
Vk = E [(1 + r)−1Vk+1 | Fk]
(7.1)
=
1 + r[pVk+1(H) + qVk+1(T)].
(See Note 1.) We now suppose Wk = Vk and want to show Wk+1(H) = Vk+1(H) and
Wk+1(T) = Vk+1(T). Then using induction we have Wn = Vn = V as required. We show
the first equality, the second being similar.
Wk+1(H) = ∆kSk+1(H) + (1 + r)[Wk −∆kSk]
= ∆k[uSk −(1 + r)Sk] + (1 + r)Vk
= Vk+1(H) −Vk+1(T)
(u −d)Sk
Sk[u −(1 + r)] + pVk+1(H) + qVk+1(T)
= Vk+1(H).
We are done.
Finally, we obtain the Black-Scholes formula in this context. Let V be any option
that is Fn-measurable. The one we have in mind is the European call, for which V =
(Sn −K)+, but the argument is the same for any option whatsoever.
Theorem 7.4. The value of the option V at time 0 is V0 = (1 + r)−nE V .
Proof. We can construct a portfolio process ∆k so that if we start with W0 = (1+r)−nE V ,
then the wealth at time n will equal V , no matter what the market does in between. If
we could buy or sell the option V at a price other than W0, we could obtain a riskless
profit. That is, if the option V could be sold at a price c0 larger than W0, we would sell
the option for c0 dollars, use W0 to buy and sell stock according to the portfolio process
∆k, have a net worth of V + (1 + r)n(c0 −W0) at time n, meet our obligation to the buyer
of the option by using V dollars, and have a net profit, at no risk, of (1 + r)n(c0 −W0).
If c0 were less than W0, we would do the same except buy an option, hold −∆k shares at
time k, and again make a riskless profit. By the “no arbitrage” rule, that can’t happen,
so the price of the option V must be W0.
Remark 7.5.
Note that the proof of Theorem 7.4 tells you precisely what hedging
strategy (i.e., what portfolio process) to use.
In the binomial asset pricing model, there is no difficulty computing the price of a
European call. We have
E (Sn −K)+ =
X
x
(x −K)+P(Sn = x)
and
P(Sn = x) =

n
k

pkqn−k
if x = ukdn−kS0. Therefore the price of the European call is
(1 + r)−n
n
X
k=0
(ukdn−kS0 −K)+

n
k

pkqn−k.
The formula in Theorem 7.4 holds for exotic options as well. Suppose
V =
max
i=1,...,n Si −
min
j=1,...,n Sj.
In other words, you sell the stock for the maximum value it takes during the first n time
steps and you buy at the minimum value the stock takes; you are allowed to wait until
time n and look back to see what the maximum and minimum were. You can even do this
if the maximum comes before the minimum. This V is still Fn measurable, so the theory
applies. Naturally, such a “buy low, sell high” option is very desirable, and the price of
such a V will be quite high. It is interesting that even without using options, you can
duplicate the operation of buying low and selling high by holding an appropriate number
of shares ∆k at time k, where you do not look into the future to determine ∆k.
Let us look at an example of a European call so that it is clear how to do the
calculations. Consider the binomial asset pricing model with n = 3, u = 2, d = 1
2, r = 0.1,
S0 = 10, and K = 15. If V is a European call with strike price K and exercise date n, let
us compute explicitly the random variables V1 and V2 and calculate the value V0. Let us
also compute the hedging strategy ∆0, ∆1, and ∆2.
Let
p = (1 + r) −d
u −d
= .4,
q = u −(1 + r)
u −d
= .6.
The following table describes the values of the stock, the payoffV , and the probabilities
for each possible outcome ω.
ω
S1
S2
S3
V
Probability
HHH
10u
10u2
10u3
p3
HHT
10u
10u2
10u2d
p2q
HTH
10u
10ud
10u2d
p2q
HTT
10u
10ud
10ud2
pq2
THH
10d
10ud
10u2d
p2q
THT
10d
10ud
10ud2
pq2
TTH
10d
10d2
10ud2
pq2
TTT
10d
10d2
10d3
q3
We then calculate
V0 = (1 + r)−3E V = (1 + r)−3(65p3 + 15p2q) = 4.2074.
V1 = (1 + r)−2E [V | F1], so we have
V1(H) = (1 + r)−2(65p2 + 10pq) = 10.5785,
V1(T) = (1 + r)−25pq = .9917.
V2 = (1 + r)−1E [V | F2], so we have
V2(HH) = (1 + r)−1(65p + 5q) = 24.5454,
V2(HT) = (1 + r)−15p = 1.8182,
V2(TH) = (1 + r)−15p = 1.8182,
V2(TT) = 0.
The formula for ∆k is given by
∆k = Vk+1(H) −Vk+1(T)
Sk+1(H) −Sk+1(T),
so
∆0 = V1(H) −V1(T)
S1(H) −S1(T) = .6391,
where V1 and S1 are as above.
∆1(H) = V2(HH) −V2(HT)
S2(HH) −S2(HT) = .7576,
∆1(T) = V2(TH) −V2(TT)
S2(TH) −S2(TT) = .2424.
∆2(HH) = V3(HHH) −V3(HHT)
S3(HHH) −S3(HHT) = 1.0,
∆2(HT) = V3(HTH) −V3(HTT)
S3(HTH) −S3(HTT) = .3333,
∆2(TH) = V3(THH) −V3(THT)
S3(THH) −S3(THT) = .3333,
∆2(TT) = V3(TTH) −V3(TTT)
S3(TTH) −S3(TTT) = 0.0.
Note 1. The second equality is (7.1) is not entirely obvious. Intuitively, it says that one has
a heads with probability p and the value of Vk+1 is Vk+1(H) and one has tails with probability
q, and the value of Vk+1 is Vk+1(T).
Let us give a more rigorous proof of (7.1). The right hand side of (7.1) is Fk measurable,
so we need to show that if A ∈Fk, then
E [Vk+1; A] = E [pVk+1(H) + qVk+1(T); A].
By linearity, it suffices to show this for A = {ω = (t1t2 · · · tn) : t1 = s1, . . . , tk = sk}, where
s1s2 · · · sk is any sequence of H’s and T’s. Now
E [Vk+1; s1 · · · sk] = E [Vk+1; s1 · · · skH] + E [Vk+1; s1 · · · skT]
= Vk+1(s1 · · · skH)P(s1 · · · skH) + Vk+1(s1 · · · skT)P(s1 · · · skT).
By independence this is
Vk+1(s1 · · · skH)P(s1 · · · sk)p + Vk+1(s1 · · · skT)P(s1 · · · sk)q,
which is what we wanted.


## 8. American Options in Discrete Time

8. American options.
An American option is one where you can exercise the option any time before some
fixed time T. For example, on a European call, one can only use it to buy a share of stock
at the expiration time T, while for an American call, at any time before time T, one can
decide to pay K dollars and obtain a share of stock.
Let us give an informal argument on how to price an American call, giving a more
rigorous argument in a moment. One can always wait until time T to exercise an American
call, so the value must be at least as great as that of a European call. On the other hand,
suppose you decide to exercise early. You pay K dollars, receive one share of stock, and
your wealth is St −K. You hold onto the stock, and at time T you have one share of stock
worth ST , and for which you paid K dollars. So your wealth is ST −K ≤(ST −K)+. In
fact, we have strict inequality, because you lost the interest on your K dollars that you
would have received if you had waited to exercise until time T. Therefore an American
call is worth no more than a European call, and hence its value must be the same as that
of a European call.
This argument does not work for puts, because selling stock gives you some money
on which you will receive interest, so it may be advantageous to exercise early. (A put is
the option to sell a stock at a price K at time T.)
Here is the more rigorous argument. Suppose that if you exercise the option at time
k, your payoffis g(Sk). In present day dollars, that is, after correcting for inflation, you
have (1+r)−kg(Sk). You have to make a decision on when to exercise the option, and that
decision can only be based on what has already happened, not on what is going to happen
in the future. In other words, we have to choose a stopping time τ, and we exercise the
option at time τ(ω). Thus our payoffis (1 + r)−τg(Sτ). This is a random quantity. What
we want to do is find the stopping time that maximizes the expected value of this random
variable. As usual, we work with P, and thus we are looking for the stopping time τ such
that τ ≤n and
E (1 + r)−τg(Sτ)
is as large as possible. The problem of finding such a τ is called an optimal stopping
problem.
Suppose g(x) is convex with g(0) = 0. Certainly g(x) = (x−K)+ is such a function.
We will show that τ ≡n is the solution to the above optimal stopping problem: the best
time to exercise is as late as possible.
We have
g(λx) = g(λx + (1 −λ) · 0) ≤λg(x) + (1 −λ)g(0) = λg(x),
0 ≤λ ≤1.
(8.1)
By Jensen’s inequality,
E [(1 + r)−(k+1)g(Sk+1) | Fk] = (1 + r)−kE
h
1 + rg(Sk+1) | Fk
i
≥(1 + r)−kE
h
g

1 + rSk+1

| Fk
i
≥(1 + r)−kg

E
h
1 + rSk+1 | Fk
i
= (1 + r)−kg(Sk).
For the first inequality we used (8.1). So (1 + r)−kg(Sk) is a submartingale. By optional
stopping,
E [(1 + r)−τg(Sτ)] ≤E [(1 + r)−ng(Sn)],
so τ ≡n always does best.
For puts, the payoffis g(Sk), where g(x) = (K −x)+. This is also convex function,
but this time g(0) ̸= 0, and the above argument fails.
Although good approximations are known, an exact solution to the problem of
valuing an American put is unknown, and is one of the major unsolved problems in financial
mathematics.

