# Probability Theory for Finance

!!! info "Source"
    **An Introduction to Quantitative Finance** by Robert R. Reitano, MIT Press.
    These notes are used for educational purposes.

## Discrete Probability Theory

7 Discrete Probability Theory
7.1
The Notion of Randomness
In this chapter some basic ideas in probability theory are introduced and applied
within a discrete distribution context. In chapter 10 these ideas will be generalized
to continuous and so-called mixed distributions. The last step of the progression
to ‘‘measurable’’ distributions will be deferred, since it requires the tools of real
analysis.
Probability theory is the mathematical discipline that provides a framework for
modeling and developing insights to the random outcomes of experiments developed
in a laboratory or a staged setting or observed as natural or at least unplanned phe-
nomenon. By random is meant that the outcome is not perfectly predictable, even
when many of the features of the event are held constant or otherwise controlled
and accounted for. By discrete probability theory is meant this theory as applied to
situations for which there are only a finite or countably infinite number of outcomes
possible. Later generalizations will extend these models and methods to situations for
which an uncountable collection of outcomes are envisioned and accommodated.
It may seem surprising that the definition of ‘‘random’’ above states that the
outcome is not perfectly predictable, rather than not predictable. This language is
motivated by the fact that in many applications the outcome of an experiment or ob-
servation logically considered to be random may not be completely random in the
stronger sense that we have no idea of what the outcome will be, but only random
in the weaker sense that we have an imperfect idea of what the outcome will be.
For example, imagine that the observation to be made is the change in a major US
stock market index, such as the S&P 500 Index, but simplified and reduced to a bi-
nary variable: 1 for a down market, and þ1 for an up market. Most observers
would agree that the result of this observation would appear to be a random out-
come on a given day, at least as of the beginning of the day. However, just before
the US market opens, stock markets in Japan and Asia have recently closed,
Europe’s trading day is half over, and based on their binary results it would appear
that one could make a better guess of the subsequent US binary result than what
would be possible without this information. Not a perfect prediction, of course, and
the US result would still be considered random, but it would not be considered per-
fectly random.
Even more to the point, an hour before the US market closes, the binary result of
this market remains random, but in a real sense, less random than at the opening bell
because of the emergence of information throughout the trading hours. And this
result one hour before market close is in turn apparently less random than the result
as of the prior evening, before the Asian markets have traded.

So the definition of randomness given here allows all such observations to be mod-
eled as random, until the moment in time when the outcome is perfectly predictable,
which in this example, is moments after the ‘‘closing bell’’ when final trades are pro-
cessed. Degrees of randomness is one of the ideas that can be quantified in probabil-
ity theory. The notion of randomness here is admittedly informal, and it is to a large
extent formalized only as a mathematical creation. But in the presence of the multi-
tude of real world events that appear random, this informality is not fatal and the
mathematical discipline of probability theory proves to be very useful.
For example, the flip of a ‘‘fair coin,’’ by which is meant a coin for which it is
equally likely to achieve a head, H, or a tail, T, is considered a standard model of
randomness. On the assumption that the coin in question is perfectly fair, probability
theory can address questions about a real or imagined experiment such as:
1. In 100 flips, how likely is it that exactly 80 Hs will occur?
2. In 10,000 flips, how likely is it that the number of Hs will exceed 5800?
3. In each case, what does ‘‘likely’’ mean?
In the absence of absolute knowledge of the fairness of the coin, probability theory
can address questions on observations like:
1. In 10 flips, does 7 Hs provide ‘‘certain’’ evidence that the coin is ‘‘biased’’ and not
fair?
2. In 10,000 flips, how large (or small) would the number of Hs have to be in order
to be ‘‘certain’’ that the coin in question is not fair?
3. In each case, what does ‘‘certain’’ mean?
In real life one might think of the occurrences of car accidents, or untimely ends of
life, as random outcomes within groups of individuals, though often not a perfectly
random outcome in a given example. The modeling of these events is critical for
property and casualty insurance and life insurance companies, respectively. In fi-
nance, virtually all observed market variables are also considered random, although
generally not perfectly random. Prices of stock and bond market indexes, individual
stocks and bonds, levels of interest rates, realized price or wage inflation indexes, cur-
rency exchange rates, commodity prices, and so forth, are all examples, as are events
such as bond issuer defaults or bankruptcies or natural disasters.
Once mathematical models are produced for these variables, probability theory
provides a framework for understanding the possible outcomes and answering ques-
tions such as those above, adapted to the given contexts.
232
Chapter 7
Discrete Probability Theory

7.2
Sample Spaces
7.2.1
Undefined Notions
As in every mathematical theory there must be some notions in probability theory
that are considered ‘‘primitive’’ and hence will be left formally undefined. However,
in the same way that most can work e¤ectively in geometry without a formal defini-
tion of point, line, or plane, most can work e¤ectively in probability theory without a
formal definition of ‘‘sample space’’ or ‘‘sample points.’’ In either case, the lack of
formal definitions is made acceptable by the intuitive framework one can bring to
bear on the subject.
For example, when one encounters point, line, or plane in geometry, a picture im-
mediately comes to mind, and all statements about these terms understood, or at
least interpreted, in the context of these pictures, however imperfectly. One’s mental
pictures of these terms in fact sharpen with time as their properties, developed in the
context of the emerging theory, are revealed. So too for sample space and sample
points, which are intended to provide a ‘‘set theory’’ structure to probability theory.
In that context the sample space is understood as the ‘‘universe’’ of possible out-
comes of a given experiment or natural phenomenon, and sample points understood
to be the smallest possible units into which the sample space is decomposed, namely
the individual outcomes or events. In this context the sample space can be viewed as
a set of sample points, appropriately defined for the given application. By discrete
sample space is meant, a sample space with a finite, or countably infinite, collection
of sample points.
Example 7.1
1. Returning to the coin flip examples above, if we are interested in understanding the
possible outcomes of a 10-flip experiment, the sample space could be envisioned as the
set of all 10-flip outcomes, and the sample points the individual sequences of 10 Hs and
Ts. Similarly one could contemplate the sample space for the 100- and 10,000-flip
questions.
2. In a di¤erent context with playing cards, one could envision a sample space of all
5-card hands that can be dealt from a single deck of cards, as would be relevant to a
poker player. Similarly a sample space of all n-card hands that can be dealt from
a multiple deck of cards, with point total less than 21, would be relevant in Black-
jack. Especially relevant is the likelihood in any such case, that the ðn þ 1Þth card
brings the point total above 21. The significance of the single deck versus multiple
7.2
Sample Spaces
233

deck models is that the latter allows repeated cards in a single hand, whereas the former
does not.
3. A related model for many probability problems is the ‘‘urn’’ problem, in which one
envisions an urn that contains several colors of balls, with various numbers of each
color. For example, the urn contains 25 balls: 2 red, 11 blue, and 12 green. One can
then imagine an experiment where one selects 3 balls ‘‘at random’’ and forms the asso-
ciated sample space of ball triplets. This sample space di¤ers depending on how we as-
sume that the 3 balls are selected:
 With replacement:
Each of the 3 balls selected is returned to the urn after selection,
so for each of the 3 draws, the urn contains the same 25 balls.
 Without replacement:
Selected balls are not returned, so the balls in the urn for the
second draw depend on the first ball drawn, and similarly for the third draw.
For example, 3 red balls are a sample point of the sample space with replacement, but
not in the space without replacement, since the urn contains only 2 red balls.
7.2.2
Events
We continue the set theory analogy. An event is defined to be a subset of the sample
space. In the discrete models contemplated here, whereby one could feasibly list all
possible sample points in the finite case, or produce a formula for the listing of all
outcomes in the countably infinite case, the collection of events could be defined as
the set of all subsets of the sample space. In other words, every subset of the sample
space could be defined as an event. In later applications, beginning in chapter 10,
where the idea of a sample space will be generalized, it will not be possible to allow
all subsets of the sample space to qualify as events. Consequently we introduce ideas
here, in a context where they are admittedly not strictly needed, in order to facilitate
the generalization we will see later in chapter 10 and need in more advanced treat-
ments. For subsets of the sample space to qualify as events, the specific question we
need to address is: If the collection of events defined does not equal the collection of
all subsets of the sample space, what minimal properties should this collection satisfy
in order to be useful in applications?
The answer is as follows:
Definition 7.2
Given a sample space, S, a collection of events, E ¼ fA j A HSg, is
called a complete collection if it satisfies the following properties:
1. j;S A E.
2. If A A E then ~
A A E.
3. If Aj A E for j ¼ 1; 2; 3; . . . , then 6j Aj A E.
234
Chapter 7
Discrete Probability Theory

In other words, we require that a complete collection of events contain the ‘‘null
event,’’ j, and the ‘‘certain event,’’ S, the complement of any event, and that it be
closed under countable unions. However, while item 3 is stated only for countable
unions, it is also true for countable intersections because of item 2 and De Morgan’s
laws (see exercise 1). So it is also the case that 7j Aj A E. Similarly, if A; B A E, then
A @ B A E, where A @ B 1 fx A S j x A A and x B Bg, since A @ B ¼ A V ~B.
Remark 7.3
1. In a discrete sample space, E usually contains each of the sample points, and hence
all subsets of S, and is consequently always a complete collection. In other words, E is
the power set of S.
2. The use of the term ‘‘complete collection’’ is not standard but is introduced for sim-
plicity. The three conditions in the definition above are general requirements for E to be
a so-called sigma algebra as will be seen in chapter 10 and more advanced treatments.
In discrete probability theory this extra formality may seem absurd, since we can
so easily just list all possible events and work within this total collection in all appli-
cations. For example, in the sample space of 10 flips of a fair coin, the sample points
are strings of 10 Hs and Ts, which we could list, even though there are 210 such
points. Also we could at least imagine the power set of this sample space, the col-
lection of all subsets of sample points, of which there are 2210 (recall exercise 4 in
chapter 4).
If the sample space is defined as the collection of Hs and Ts in n flips of a coin for
all n, or defined as all sequences that emerge from flips that terminate on the occur-
rence of the first H, or the mth H, then these sample spaces have countably many
sample points, and although significantly more complicated, one could envision the
collection of all subsets as events.
However, if the sample space is defined as the collection of Hs and Ts in a count-
ably infinite number of flips, this space has the same cardinality as the real numbers
(recall exercise 5 in chapter 4), and the prospect of defining events as every subset
of this space becomes hopeless, as can be proved using the tools of real analysis.
Consequently the definition above is needed in such cases, and identifies the minimal
properties for an event space for the next step, which is the introduction of event
probabilities.
7.2.3
Probability Measures
The intuition behind the notion of the ‘‘probability’’ of an event is a simple one.
One approach is sometimes deemed the ‘‘frequentist’’ interpretation. That is, the
7.2
Sample Spaces
235

probability of an event is the long-term proportion of times the event would be
observed in a repeated trials of an experiment that was designed to result in two
outcomes:
Event A observed;
Event A not observed.
In this interpretation it is assumed that each trial is ‘‘independent’’ of the others,
which is to say, that its outcome neither influences nor is influenced by the outcomes
of the other trials.
Example 7.4
In the 10-flip coin sample space S, define the event A as the subset of the
sample space that has HH as the first two flips. Intuitively, a fair coin makes every se-
quence equally likely, and it is easy to see that 25% of the sequences in S begin with
HH. So if we designed an experiment that flipped a coin 10 times, and recorded the
results after many trials, the expectation would be that in 25% of the tests, A would be
observed. The term ‘‘frequentist’’ probability comes from the idea that 25% is the rela-
tive frequency of event A in a long string of such trials. It is the relative frequency that
would be observed in the long run.
An alternative interpretation is related to games of chance, or gambling, which
was a primary motivator for the original studies of probability by Abraham de
Moivre (1667–1754), who published an early treatise on the subject in 1718 called
The Doctrine of Chances. The gambling perspective for this example can be phrased
as: For a $1 bet, what should the payo¤ be when event A occurs so that a gambler’s
wealth can be expected to not change in the long run? Such a bet would be called a
‘‘fair bet.’’ There is of course a frequentist flavor to this interpretation, since present
are the notions of ‘‘repeated trials’’ and ‘‘in the long run.’’
So, if p denotes the probability of event A occurring and N is a large integer, then
in N bets the gambler will bet $1 and lose about ð1  pÞN bets and $ð1  pÞN, and
the gambler will win about Np bets and $Npw if w is the associated payo¤ or ‘‘win-
nings’’ for a $1 bet. This bet will be a fair bet if won and lost bets are equal, which
happens when
w ¼ 1  p
p
:
ð7:1Þ
Example 7.5
In the coin-flip example above, the gambler’s winnings for a $1 bet, to
ensure that it is a fair bet, must be w ¼ $3. That is, the gambler wins $3 if the coin-
flip sequence is HH . . . , and he loses $1 otherwise.
236
Chapter 7
Discrete Probability Theory

The formula for w in (7.1) really only makes sense for p values of 0 < p < 1. Oth-
erwise, the bet degenerates to a sure win or sure loss, and it cannot be made ‘‘fair’’ in
the sense above. On this domain, w ¼ 1
p  1 is seen to decrease as p increases, is un-
bounded as p ! 0, and decreases to 0 as p ! 1, consistent with intuition.
Note that (7.1) also encodes information about the ‘‘probability’’ we seek, and can
be rewritten as
p ¼
1
w þ 1 :
ð7:2Þ
Example 7.6
Again in the coin-flip example, if participants agreed that the correct
payo¤ was w ¼ 3, then we would conclude that the probability of the sequence HH . . .
is 0:25 or 25%.
This intuitive framework provides a starting point for formalizing the notion of
probability. Probabilities are logically associated with events and can therefore be
identified with a function on the collection of events, denoted PrðAÞ for A A E. Fur-
thermore the value of this function must be between 0 and 1 for any event, and these
extremes should be achieved on the null event, j, and the full sample space, S, re-
spectively. Finally, we expect this function to behave logically on the collection of
events. For example, if A H B are events, we want PrðAÞ a PrðBÞ, and if A V B ¼ j,
then PrðA U BÞ ¼ PrðAÞ þ PrðBÞ, and so forth.
We collect the necessary properties in the following, and note in advance that in a
discrete sample space, PrðsÞ is typically defined for all s A S since E contains the indi-
vidual sample points.
Definition 7.7
Given a sample space, S, and a complete collection of events, E ¼
fA j A HSg, a probability measure is a function Pr : E ! ½0; 1 that satisfies the follow-
ing properties:
1. PrðSÞ ¼ 1.
2. If A A E, then PrðAÞ b 0 and Prð ~
AÞ ¼ 1  PrðAÞ.
3. If Aj A E for j ¼ 1; 2; 3; . . . are mutually exclusive events, that is, with Aj V Ak ¼ j
for all j 0 k, then Prð6j AjÞ ¼ P PrðAjÞ.
In this case the triplet ðS;E; PrÞ is called a probability space.
Definition 7.8
An event A A E is a null event under Pr if PrðAÞ ¼ 0. If A is a null
event and every A0 H A satisfies A0 A E, then the triplet ðS;E; PrÞ is called a complete
probability space.
7.2
Sample Spaces
237

Some properties of this probability measure are summarized next.
Proposition 7.9
If Pr is a probability measure on a complete collection of events E,
then:
1. PrðjÞ ¼ 0.
2. If A; B A E, with A H B, then PrðAÞ a PrðBÞ.
3. If Aj A E for j ¼ 1; 2; 3; . . . , then
max
j
fPrðAjÞg a Pr 6
j
Aj
 
!
a
X
j
PrðAjÞ:
4. If Aj A E for j ¼ 1; 2; 3; . . . , then
Pr 7
j
Aj
 
!
a min
j fPrðAjÞg:
Proof
See exercise 26.
n
Remark 7.10
Note that in property 2 of the proposition above, it might be expected
that if B A E, and A H B, then automatically it is true that A A E. In the special case of
this chapter of discrete probability spaces, this is virtually always true in applications,
since then E typically contains all the sample points and hence contains all possible sub-
sets of S. In the general case of what is called a ‘‘complete’’ collection of events, or gen-
erally a sigma algebra, subsets of events need not be events.
7.2.4
Conditional Probabilities
Given a sample space S, a complete collection of events E ¼ fA j A HSg, and a
probability measure Pr : E ! ½0; 1, there are many situations in which we are inter-
ested in probability values that reflect additional information. For example, if the
sample space is the collection of all 10-flip sequences of a fair coin, we know that
the probability of every one of the 210 sample points is
1
2
 10. Similarly, if we define
an event B as the collection of sample points with exactly 1-H and 9-Ts, then
PrðBÞ ¼ 10 1
2
 10 since we know there are exactly 10 such sequences.
Now imagine that we know that event B is true. How would that knowledge alter
our calculation of the probabilities of all the events in E? Perhaps simpler, how would
that knowledge alter our calculation of the probabilities of all the sample points in S?
In other words, what is PrðA conditional on the knowledge that B is true), where A
denotes any sample point or event? In probability theory, this is called a conditional
probability, and is written
238
Chapter 7
Discrete Probability Theory

PrðA j BÞ;
and read, ‘‘the probability of A given B,’’ or ‘‘the probability of A conditional on B.’’
Example 7.11
The sample points are somewhat easier to address first. Since we want
Prð j BÞ to be a genuine probability measure on E, we need PrðS j BÞ ¼ 1, and since S is
the disjoint union of its sample points, we must have that the sum of all the conditional
probabilities of the sample points is also 1. Now, if A is any event with more or less
than 1 H, it must be the case that PrðA j BÞ ¼ 0. What about the 10 sample points,
each with 1 H? Since each is equally likely in E, it is logical to define PrðA j BÞ ¼ 1
10
for each such point. Similarly, if A is a general event that contains none of these
1-H points, we define PrðA j BÞ ¼ 0, while if A contains j of these points, we define
PrðA j BÞ ¼
j
10 .
In this simple context the notion of conditional probability is somewhat transpar-
ent. The general definition is intended to formalize this idea to be more applicable in
more complex situations, and provide a calculation that explicitly references the orig-
inal probabilities of events under Pr.
Definition 7.12
Given a discrete sample space S, a complete collection of events E ¼
fA j A HSg, a probability measure Pr : E ! ½0; 1, and an event B A E with PrðBÞ > 0,
then for any A A E, the conditional probability of A given B, denoted PrðA j BÞ, is
defined by
PrðA j BÞ ¼ PrðA V BÞ
PrðBÞ
;
PrðBÞ 0 0:
ð7:3Þ
It is a straightforward exercise that for any such event B, that Prð j BÞ defines a
true probability measure on S as given in the definition above (see exercise 5). One
can also review the example above in the formalized context of (7.3) and see that
the respective intuitive results are reproduced.
Law of Total Probability
Another important application of these ideas is exemplified as follows:
Example 7.13
Imagine an urn containing 10 balls, 5 each of red (R) and blue (B),
from which 2 are to be selected. Let C1 denote the color of the first ball drawn, and
C2 the color of the second. Then construct two sample spaces of the pair of balls drawn,
ðC1; C2Þ: one space defined under the assumption that the draws are done with replace-
ment, and the other reflecting no replacement. In the sample space with replacement, it
is easy to see that PrðC2 j C1Þ ¼ PrðC2Þ. For example, PrðR2Þ 1 PrðC2 ¼ RÞ ¼ 0:5,
and PrðR2 j C1Þ ¼ 0:5 whether C1 ¼ R or C1 ¼ B.
7.2
Sample Spaces
239

In the sample space without replacement, it is never the case that PrðC2 j C1Þ ¼
PrðC2Þ. For example, PrðR2 j R1Þ ¼ 4
9 and PrðR2 j B1Þ ¼ 5
9 , and we now show that
PrðR2Þ ¼ 0:5. To this end, first note that PrðR1 j R2Þ 0 1
2 , as might be expected given
that R1 happens ‘‘first’’ when there are five of each color. But that is not the meaning of
PrðR1 j R2Þ. The question is, looking at the outcomes for which C2 ¼ R, what is the
probability that C1 ¼ R? There are two such outcomes:
PrðR1 V R2Þ ¼ 4
18
and
PrðB1 V R2Þ ¼ 5
18 ;
from which we conclude that PrðR1 j R2Þ ¼ 4
9 . An application of (7.3) now shows that
PrðR2Þ ¼ PrðR1 V R2Þ
PrðR1 j R2Þ ¼ 0:5. This probability could have also been more easily calculated
from the respective conditional probabilities using a method discussed next.
Let fBjg be a collection of mutually exclusive events with 6 Bj ¼ S. Then for
any event A, fA V Bjg are also mutually exclusive, and have union A. By the third
property of the probability measure, we have that PrðAÞ ¼ Prð6½A V BjÞ ¼
P PrðA V BjÞ. Also, by (7.3), PrðA V BjÞ ¼ PrðA j BjÞ PrðBjÞ. Combining, we get the
law of total probability:
PrðAÞ ¼
X
j
PrðA j BjÞ PrðBjÞ:
ð7:4Þ
This law has widespread application because it is often easier to calculate conditional
probabilities of an event than the direct probability because each ‘‘condition’’ pro-
vides a restriction on the sample points that need be considered.
Example 7.14
In the urn problem of example 7.13 without replacement, PrðR2Þ ¼ 0:5
could have been more easily derived using this law of total probability. The mutually
exclusive events fBjg are the events C1 ¼ R and C1 ¼ B, and each of these events has
probability equal to 0:5. Consequently, using the respective conditional probabilities, we
can write
PrðR2Þ ¼ PrðR2 j R1Þ PrðR1Þ þ PrðR2 j B1Þ PrðB1Þ;
again producing PrðR2Þ ¼ 0:5.
7.2.5
Independent Events
The notion of stochastic independence is a property of pairs of events under a given
probability measure Pr. Intuitively we say that A and B are stochastically indepen-
dent, or simply independent, if their probabilities are not changed by conditioning
240
Chapter 7
Discrete Probability Theory

on each other. This idea is a simple one, except for the formality that in order for the
various conditional probabilities to be defined, it is necessary that both events have
nonzero probability.
To circumvent this technicality, observe that the desired condition: PrðA j BÞ ¼
PrðAÞ, which requires that PrðBÞ 0 0 to be well defined, is by (7.3) equivalent to
PrðA V BÞ ¼ PrðAÞ PrðBÞ, which does not require a condition on PrðBÞ or PrðAÞ to
be well defined. This latter formulation of the idea of independence also has the im-
mediate advantage of reflexivity; that is, A is independent of B i¤ B is independent of
A. Formally, we state:
Definition 7.15
Events A1; A2 A E are stochastically independent, or simply indepen-
dent, under the probability measure Pr, if
PrðA1 V A2Þ ¼ PrðA1Þ PrðA2Þ:
ð7:5Þ
More generally, a collection of events: fAjgn
j¼1, where n may be y, are mutually inde-
pendent, if for any integer subset J H f1; 2; . . . ; ng we have that
Pr 7
J
Aj
 
!
¼
Y
J
PrðAjÞ:
ð7:6Þ
This definition makes sense even if Ak is a null event, PrðAkÞ ¼ 0 for some k. In
either setting, we have from property 2 of the proposition above on probability mea-
sures that Prð7J AjÞ ¼ 0 as well if k A J. So formally, null sets are independent of all
other sets.
In the case where one or both of A or B have nonzero probability, the notion of
independence can be reformulated using conditional probabilities. For example, if A
and B are independent, and PrðBÞ 0 0, then
PrðAÞ ¼ PrðA j BÞ:
In other words, if A and B are independent, their probabilities are una¤ected by
knowledge of the occurrence of the other event.
In the urn examples above, with C1 denoting the color of the first ball drawn and
C2 the color of the second, it was seen that in the sample space with replacement,
these events were independent, whereas without replacement, these events are not
independent.
7.2.6
Independent Trials: One Sample Space
One of the most important applications of the notion of independence is in the
formalization of the idea of a random sample from a discrete sample space, or
7.2
Sample Spaces
241

equivalently, a series of independent trials from a discrete sample space. Given a sam-
ple space S with associated probability measure Pr, a random sample of size n, or a
sequence of n trials, is defined as a sample point in another sample space, S n, which
is formalized in:
Definition 7.16
Given a discrete sample space S, a complete collection of events E ¼
fA j A HSg containing the sample points, and a probability measure Pr : E ! ½0; 1,
the associated n-trial sample space, denoted S n, is defined by
S n ¼ fðs1; s2; . . . ; snÞ j sj A Sg:
The collection of events, denoted E n, is defined by
E n ¼ fðA1; A2; . . . ; AnÞ j Aj A E and by unions of such eventsg:
The associated probability measure, Pn, is defined on E n by
Pn½ðs1; s2; . . . ; snÞ ¼
Y
n
j¼1
PrðsjÞ;
ð7:7Þ
as extended additively to events, for A A E n,
PnðAÞ ¼
X
ðs1;s2;...;snÞ A A
Pn½ðs1; s2; . . . ; snÞ:
ð7:8Þ
The goal of the next proposition is to confirm that the collection of events in n-trial
sample space is a complete collection, and that Pn is indeed a probability measure on
S n. Most important, we confirm that any event in E can be identified in a natural but
not unique way with an event in E n, and that under this identification, n events in E
are mutually independent as events in E n. This identification and associated indepen-
dence result provides a formal meaning to the notion of independent trials, or inde-
pendent draws, from a given sample space.
Before stating this proposition, we note that the multiplicative rule in (7.7) extends
to events in E n. That is, with A 1 ðA1; A2; . . . ; AnÞ, Aj A E,
Pn½A ¼
X
ðs1;s2;...;snÞ A A
Y
n
j¼1
PrðsjÞ
242
Chapter 7
Discrete Probability Theory

¼
Y
n
j¼1
X
sj A Aj
PrðsjÞ
2
4
3
5
¼
Y
n
j¼1
PrðAjÞ:
That is, for fAjgn
j¼1 HE,
Pn½ðA1; A2; . . . ; AnÞ ¼
Y
n
j¼1
PrðAjÞ:
ð7:9Þ
Remark 7.17
In the definition of n-trial sample space it is assumed that the event
space E contained all the sample points. In fact, while this assumption is almost always
true in discrete probability theory, it is more of a convenience here than a necessity.
With this assumption, E n then contains all the n-tuples of sample points, ðs1; s2; . . . ;
snÞ, whose probabilities are defined by (7.7), and the probability measure Pn is then
easily generalized to all events in E n by (7.8). In the more general case where E does
not contain all the sample points, but is a complete collection of events as defined
above, a similar construction is possible but more di‰cult. In this case E n is defined as
above to include all n-tuples of events, ðA1; A2; . . . ; AnÞ, and then expanded to include
all unions of these n-tuples and their complements so that E n becomes complete. The
probability measure Pn is defined on n-tuples of events, ðA1; A2; . . . ; AnÞ, using (7.9)
and then extended to all of E n. It is not possible to define this extension directly using
a generalization of (7.8) because of a technicality that is avoided with our convenient
assumption. And that technicality is, if an event A HE n is a union of n-tuples of events,
fðAk1; Ak2; . . . ; AknÞgN
k¼1, where N may be y, these events need not be disjoint, and so a
direct application of a formula such as (7.8) may involve multiple counts. This problem
is avoided when E n contains all n-tuples of sample points, ðs1; s2; . . . ; snÞ. This general
construction is subtle and developed in advanced studies using the tools of real analysis.
Proposition 7.18
Given a discrete sample space S, a complete collection of events
E ¼ fA j A HSg containing the sample points, and Pr a probability measure on E, then:
1. Every event A HE can be identified with n-events in E n, any one if denoted A, satis-
fies Pn½A ¼ PrðAÞ.
2. Under the identification in 1, every collection of up to n-events in E can be identified
with mutually independent events in S n. That is, for any collection of events in E,
fAkgn
k¼1, there are associated fAkgn
k¼1 HE n, so that for any K H f1; 2; . . . ; ng:
7.2
Sample Spaces
243

Pn
7
k A K
Ak
"
#
¼
Y
k A K
Pn½Ak ¼
Y
k A K
P½Ak:
3. E n is a complete collection of events.
4. Pn defined in (7.7) and (7.8) is a probability measure on E n.
Proof
1. The n identifications as noted above are simply A $ ðA;S; . . . ;SÞ; ðS; A;S; . . . ;
SÞ . . . ðS; . . . ;S; AÞ, and for each identification by (7.9) we have Pn½A ¼ PrðAÞ, since
PrðSÞ ¼ 1.
2. Given fAkgn
k¼1 we associate each with Ak where the event Ak is assigned to the
kth component of Ak, and S assigned to the other components as in 1 above. Now,
if K H f1; 2; . . . ; ng, 7k A K Ak equals the event in E n : ðA0
1; A0
2; . . . ; A0
nÞ, where each
A0
j equals Aj or S, and the result follows from (7.9).
3. Both S n 1 ðS;S; . . . ;SÞ and j 1 ðj; j; . . . ; jÞ are elements of E n, by definition.
Also, since E n contains all n-tuples of sample points, ðs1; s2; . . . ; snÞ, if A A E n, then
also ~
A A E n. Similarly, if Aj A E n, then 6 Ak A E n.
4. By definition of Pn, we have Pn½j ¼ 0, and
Pn½S n ¼
X
ðs1;s2;...;snÞ AS n
Y
n
j¼1
PrðsjÞ
"
#
¼
X
sj AS
PrðsjÞ
2
4
3
5
n
¼ 1:
Now, if A ¼ 6M
k¼1ðsk1; sk2; . . . ; sknÞ, then A U ~
A ¼ S n, and we can rewrite the identity
above for Pn½S n as
1 ¼
X
ðs1;s2;...;snÞ AS n
Y
n
j¼1
PrðsjÞ
"
#
¼
X
ðs1;s2;...;snÞ A A
Y
n
j¼1
PrðsjÞ
"
#
þ
X
ðs1;s2;...;snÞ A ~
A
Y
n
j¼1
PrðsjÞ
"
#
:
¼ PnðAÞ þ Pnð ~
AÞ:
Hence Pnð ~
AÞ ¼ 1  PnðAÞ. Finally, if fBkgm
k¼1 are mutually exclusive events, mean-
ing that for any K H f1; 2; . . . ; mg,
7
k A K
Bk ¼ j;
244
Chapter 7
Discrete Probability Theory

then by (7.8),
Pnð6 BkÞ ¼
X
ðs1;s2;...;snÞ A 6 Bk
Y
n
j¼1
PrðsjÞ
¼
X
k
X
ðs1;s2;...;snÞ A Bk
Y
n
j¼1
PrðsjÞ
¼
X
k
PnðBkÞ;
where
the
second
equality
is
due
to
mutual
exclusivity:
P
ðs1;s2;...;snÞ A 6Bk ¼
P
k
P
ðs1;s2;...;snÞ A Bk.
n
*7.2.7
Independent Trials: Multiple Sample Spaces
The construction of an n-trial sample space S n, reflecting independent samples from
a given sample space S, is readily generalized to the notion of an n-trial sample space
reflecting independent samples from a collection of di¤erent sample spaces. To this
end, we start with a definition.
Definition 7.19
Given a collection of discrete sample spaces fSjgn
j¼1, complete collec-
tions of events fEjgn
j¼1 where each Ej ¼ fA j A HS jg contains all the sample points of
S j, and associated probability measures Prj : Ej ! ½0; 1, the associated generalized n-
trial sample space, denoted SðnÞ, is defined by
S ðnÞ ¼ fðs1; s2; . . . ; snÞ j sj A Sjg:
The collection of events, denoted EðnÞ, is defined by
EðnÞ ¼ fðA1; A2; . . . ; AnÞ j Aj A Ej and unions of such eventsg:
The associated probability measure, PðnÞ, is defined on EðnÞ by
PðnÞ½ðs1; s2; . . . ; snÞ ¼
Y
n
j¼1
PrjðsjÞ;
ð7:10Þ
as extended additively to events, for A A EðnÞ:
7.2
Sample Spaces
245

PðnÞðAÞ ¼
X
ðs1;s2;...;snÞ A A
PðnÞ½ðs1; s2; . . . ; snÞ:
ð7:11Þ
The proofs of the results in proposition 7.18 in the special case where Sj ¼ S and
Ej ¼ E for all j carry over to this more general case without material change other
than notational. This is because, with one exception, nowhere in the derivations
above was it necessary to use the fact that the sample spaces, collections of events,
and probability measures underlying the various components of an n-trial sample
point were identical. The single exception is related to the identifications of events in
S with events in S n. In the simpler case above, each event in A HS could be identi-
fied with n events in S n, all of which had the same probability under Pn, and this
common probability equaled PrðAÞ, the probability in S. In the general case it is nat-
ural to assume that the given sample spaces are ordered. Hence each event A HS j is
identified with a unique element A HSðnÞ, and that is defined with A in the jth com-
ponent, and the various Sk spaces used as events in the other components, in order.
Of course the ordering is a convenience more than a necessity, and di¤erent order-
ings do not produce fundamentally di¤erent spaces.
As an example of how a result above generalizes to this setting, we note that (7.10)
generalizes in the same way that (7.7) generalizes to (7.9). Specifically, with the same
derivation, and for Aj A Ej,
PðnÞ½ðA1; A2; . . . ; AnÞ ¼
Y
n
j¼1
PrjðAjÞ:
ð7:12Þ
Finally, we state without proof the fundamental result that generalizes the propo-
sition above to this setting, and note that remark 7.17 in that section, regarding the
assumption that each Ej contains the sample points, applies here as well.
Proposition 7.20
Given a collection of discrete sample spaces fS jgn
j¼1, complete col-
lections of events fEjgn
j¼1 that contain the sample points, and associated probability
measures Prj : Ej ! ½0; 1, then:
1. Every event A HEj can be identified with a unique event in A HEðnÞ that satisfies
PðnÞ½A ¼ PrjðAÞ.
2. Under the identification in 1, every collection of events Ak HEk, 1 a k a n, can
be identified with mutually independent events in S ðnÞ. That is, for any such collec-
tion of events fAkgn
k¼1, there are associated fAkgn
k¼1 HEðnÞ so that for any
K H f1; 2; . . . ; ng,
246
Chapter 7
Discrete Probability Theory

PðnÞ
7
k A K
Ak
"
#
¼
Y
k A K
PðnÞ½Ak ¼
Y
k A K
Pk½Ak:
3. EðnÞ is a complete collections of events.
4. PðnÞ defined in (7.10) and (7.11) is a probability measure on SðnÞ.
7.3
Combinatorics
To determine the values of PrðAÞ in various sample space applications, it is often
necessary to be able to e‰ciently count the sample points in the event A as well as
those in the sample space S, and such calculations can be both subtle and di‰cult.
The mathematical discipline of combinatorics, or combinatorial analysis, provides a
structured framework for addressing these types of problems, and we only scratch
the surface of this discipline here with the most common applications.
7.3.1
Simple Ordered Samples
In many applications we require the number of ways that m items can be selected
from a collection of n b m distinguishable items. For example, an urn may contain
n balls, all distinguishable by color or other markings, and we seek to determine how
many distinct m-ball collections can be drawn from this urn. As we have seen from
the examples above, we need to distinguish between whether this is an urn problem
with replacement or without replacement.
With Replacement
On the first draw there are n possible outcomes, and due to replacement, each succes-
sive draw has the same number of possible outcomes. So we conclude that there are
nm total possibilities. This can be formalized by observing that for m ¼ 2 we can
explicitly enumerate the outcomes, and then proceed by induction. That is, we as-
sume the truth of the formula for m, and verify the truth for m þ 1 based on the ex-
plicit pairings of each m-tuple with each last draw.
Without Replacement
On the first draw there are again n possible outcomes, but since the first draw is not
returned to the urn, the second draw has fewer possible outcomes, namely n  1. This
process continues to the mth draw for which there are n  ðm  1Þ ¼ n  m þ 1 pos-
sible outcomes. Using the same logic and proof as above, we see that there are
nðn  1Þ . . . ðn  m þ 1Þ possible outcomes. This sequential product is common in
combinatorics, and it is worthwhile to note that it can easily be expressed in terms
7.3
Combinatorics
247

of the factorial function. Recall that n factorial is defined n! ¼ nðn  1Þðn  2Þ    2  1,
and so
nðn  1Þ . . . ðn  m þ 1Þ ¼
n!
ðn  mÞ! :
In some texts this partial factorial, which contains m terms, is denoted ðnÞm 1
nðn  1Þ . . . ðn  m þ 1Þ. Of course, in this notation, ðnÞn ¼ n!.
7.3.2
General Orderings
Here we seek an approach to determining how many distinguishable ways a given
collection of n objects can be ordered. The answer depends on how many subset
types are represented by the n objects, where all objects in each subset are identical.
For example, if there is one subset type, and all n objects are identical, there is
only one distinguishable ordering. If each of the objects are themselves distinguish-
able, which is n subset types, this is equivalent to the without replacement model
and m ¼ n, and we have from the section above that there are n! distinguishable
orderings.
Two Subset Types
Next assume that there are two subsets of indistinguishable objects, say n1 of one
type and n2 ¼ n  n1 of the other. Envision a collection of n1 1s and n2 0s to be or-
dered, or n1 red balls and n2 blue balls. What distinguishes this example from that
where all the objects di¤er is that here, the collection of all orderings will contain
multiple counts. For example, if we start with the collection f1; 2; 3; 4g, there are
4! ¼ 24 possible orderings, but if we begin with f1; 1; 1; 4g, there are only 4 order-
ings. This is because we only have to choose the position for the one 4-digit, for the
other digits will all be 1s. This can also be deduced by observing that in the 4! order-
ings of the 4 digits in this second set, each distinct outcome will be seen 3! times,
reflecting the indistinguishable orderings of the three 1s.
Analogously in this general case, the number of orderings is
ðn1 þ n2Þ!
n1!n2!
¼
n!
n1!n2! :
The logic of this formula, as will be analyzed in more detail next, is that the numer-
ator reflects the number of orderings of the n objects, temporarily treating them as if
all are distinguishable. The denominator then adjusts for multiple counts, since there
will be n1! orderings with the n1 objects of the first type in the same locations but with
di¤erent orderings of these actual objects. Likewise for each of these orderings there
248
Chapter 7
Discrete Probability Theory

will be n2 objects of the second type in the same locations but with di¤erent orderings
of these actual objects.
Binomial Coe‰cients
The formula above has many applications in mathematics, especially with respect
to coin-flip and associated binomial models, where ‘‘binomial’’ means with two out-
comes. The two outcomes represent the two subset types discussed above. Because of
its prevalence, this formula has been given a special notation.
As a traditional binomial example, imagine that a coin is flipped n times. What is
the total number of sample points in the associated sample space that have exactly m
heads, for m ¼ 0; 1; 2; . . . ; n? This question is identical to that of a general ordering of
n objects, where there are m of one type, the Hs, and n  m of the other type, the Ts.
The analysis above shows that there will be
n!
ðnmÞ!m! such sample points, and the gen-
eral notation is
n
m


¼
n!
ðn  mÞ!m! :
ð7:13Þ
This factor is sometimes denoted nCm, and read, ‘‘n choose m,’’ and we recall that by
convention, 0! ¼ 1.
For any n, these constants,
n
m
 

n
m¼0, are known as binomial coe‰cients, for a rea-
son that will be apparent below. The terminology ‘‘n choose m’’ is shorthand for ‘‘the
number of ways of choosing m positions from n positions.’’ In the example above,
the m positions chosen are of course equal to the locations of the m-Hs, with the
remaining positions filled with Ts.
Example 7.21
As another example of an application of ‘‘n choose m,’’ consider
explicitly choosing all possible subsets of a set of n distinguishable objects. For any
m ¼ 0; 1; 2; . . . ; n, there are
n
m
 
possible subsets that can be selected. This is just a
reformulation of the earlier model in that we can envision these n objects as n positions,
and the selection of a subset of m objects as equivalent to the selection of m of these
positions. When m ¼ 0, we are selecting the empty subset j, and there is only one way
to do this. If we seek the total number of subsets of all sizes, which is the number of sets
in the power set, the answer must therefore be equal to Pn
m¼0
n
m
 
. But we also know
from exercise 4 in chapter 4, that the number of sets in the power set of a set of n ele-
ments is 2n. So we must have
X
n
m¼0
n
m


¼ 2n:
ð7:14Þ
7.3
Combinatorics
249

The Binomial Theorem
Formula (7.14) is a special case of the so-called binomial theorem, which is yet an-
other application of ‘‘n choose m.’’ This theorem addresses the expansion of an inte-
ger power of a binomial, such as ða þ bÞn. The problem posed is a ‘‘chooser’’
problem because in this multiplication we have to choose an a or a b from each of
the n factors of ða þ bÞ and multiply the selected n terms. Consequently the general
term in the product is of the form ambnm for m ¼ 0; 1; 2; . . . ; n. The question is, how
many times will each such factor arise? Of course, the answer is
n
m
 
times, since for
each m there are
n
m
 
ways of selecting the m a-factors from these n binomial factors.
Consequently the binomial theorem states that
ða þ bÞn ¼
X
n
m¼0
n
m


ambnm:
ð7:15Þ
From (7.15), the special case of (7.14) is easily derived by setting a ¼ b ¼ 1.
Also of interest, for a ¼ 1, b ¼ 1, the sum of the alternating binomial coe‰cients
is seen to equal 0:
X
n
m¼0
n
m


ð1Þm ¼ 0:
Finally, if a þ b ¼ 1, this theorem assures us that
X
n
m¼0
n
m


ambnm ¼ 1;
which is important in the binomial distribution below where it is also assumed that
0 a a; b a 1.
The coe‰cients of the factors in these expressions are easily generated by a method
developed by Blaise Pascal (1623–1662) and known as Pascal’s triangle. It is based
on the iterative formula (see exercise 33)
n
m


¼
n  1
m  1


þ
n  1
m


:
ð7:16Þ
The associated ‘‘triangle’’ is developed row by row, with the nth row correspond-
ing to the coe‰cients in the expansion of ða þ bÞn. The coe‰cients up to ða þ bÞ6 are
in (7.17), and these may be familiar from elementary algebra:
250
Chapter 7
Discrete Probability Theory

1
1
1
1
2
1
1
3
3
1
1
4
6
4
1
1
5
10
10
5
1
1
6
15
20
15
6
1
. . .
(7.17)
Notice that for any n,
n
0
 
¼
n
n
 
¼ 1 and how, with clever spacing, each term of a row
equals the sum of the terms right above it, implementing the iterative formula in
(7.16).
r Subset Types
Now assume that there are r subsets of distinguishable objects, with nj of type-j,
nj b 0, and with P nj ¼ n. Then the logic above carries forward identically, and we
see that the number of such orderings is
nCn ¼
n!
n1!n2! . . . nr! ;
ð7:18Þ
where the nonstandard notation nCn is intended to connote that the choice made of
the n objects is a vector n 1 ðn1; n2; . . . ; nrÞ. For a given n the collection of the num-
ber of such orderings
nCn j n ¼ ðn1; n2; . . . ; nrÞ;
X
nj ¼ n
n
o
are known as the multinomial coe‰cients.
The logic behind this formula is that there are n! orderings of the n objects, mo-
mentarily considered to be distinct. For example, temporarily label the type-1 objects
with numbers 1; 2; . . . ; n1, and so forth. Now select any one of these n! orderings, and
observe the positions of the type-1 objects. When this particular ordering was
achieved, there were n1! possible orderings in which these type-1 objects could have
been selected and placed into the given positions. Similarly, for any type-j, there
would be nj! possible orderings in which these objects could have been selected and
7.3
Combinatorics
251

placed into the given positions of the selected ordering. In other words, the n! order-
ings contain n1!n2! . . . nr! copies of every distinct ordering, and hence one needs to di-
vide by this factor to eliminate the redundancies.
Example 7.22
Assume that we are given the 10-digit collection,
f1; 1; 2; 2; 2; 5; 5; 5; 5; 7g:
How many di¤erent base-10 numbers can be formed using all the digits? As before,
there are 10! possible orderings, but with many multiple counts. Adjusting for these,
we see that the total collection of distinct integers formed will be
10!
2!3!4!1! ¼ 12;600:
Multinomial Theorem
In the same way that the binomial coe‰cients can be found in the general expansion
of the binomial ða þ bÞn so too can the multinomial coe‰cients in (7.18) be found in
the general expansion of a multinomial ðPr
i¼1 aiÞn. Specifically, we have that
X
r
i¼1
ai
 
!n
¼
X
n1;n2;...nr
n!
n1!n2! . . . nr! an1
1 an2
2 . . . anr
r ;
ð7:19Þ
where this summation is over all distinct r-tuples ðn1; n2; . . . ; nrÞ so that nj b 0 and
Pr
j¼1 nj ¼ n.
As for the binomial theorem above, special identities are produced with simple
applications of (7.19) in the special cases where Pr
i¼1 ai ¼ 0 or Pr
i¼1 ai ¼ 1. The lat-
ter case has an important application to the multinomial distribution below, where it
is also assumed that 0 a ai a 1 for all i.
7.4
Random Variables
7.4.1
Quantifying Randomness
Notions of sample space, events, and probability measures are often introduced in
the colorful and intuitive imagery of card hands dealt from one or more well-shu¿ed
decks of cards, collections of colored balls drawn from an urn containing di¤erent
numbers of colored balls with or without replacement, and sequences of flips of a
fair or biased coin. While interesting, these models do not lend themselves to mathe-
matical analysis very well because these contexts can obscure similarities or create
252
Chapter 7
Discrete Probability Theory

misleading connections. If a problem is solved in the context of an urn problem, will
it be apparent that the same procedure might be applied and the same result obtained
in the very di¤erent context of dealt card hands? Or if a problem is solved in the con-
text of flips of a biased coin, will it be apparent that the same procedure might be
applied and result obtained in the very di¤erent context of the modeling of the prices
of a common stock in discrete time steps?
The notion of a random variable was introduced for the purpose of stripping away
the context of these problems, to reveal the common mathematical structures under-
lying them. In e¤ect a random variable transfers the probabilities associated with
these colorful events to probabilities associated with numerical values in R. A few
simple examples will illustrate the point.
Example 7.23
1. Let’s return to the sample space S of 10-flip sequences of a fair coin that, as we have
seen, contains 210 sample points and 2210 possible events, all with associated probabil-
ities. We now define a function on the original sample space, as follows:
XðsÞ ¼ n;
where n is the number of Hs in s A S. So X is a function, X : S ! f0; 1; 2; . . . ; 10g.
Note that for any n A f0; 1; 2; . . . ; 10g, the inverse X 1ðnÞ 1 An A E is a well-defined
event of sample points with n Hs, and hence we can define implied probabilities on these
integers by
PðnÞ ¼ Pr½An:
Of course, this particular random variable provides only one quantitative insight to this
sample space, its events, and the associated probability structure, and there are many
other insights that remain hidden. However, there are many more random variables
that can be defined, each providing certain insights and hiding others. The particular
definition of the random variable used is determined in such a way that the properties
of S that are of interest to the analyst are revealed.
2. As another example, one could imagine a game whereby after 10 flips of a fair coin,
producing sample point s, the player receives a payo¤ of YðsÞ ¼ Pn
j¼0 10 j, where n is
the number of Hs in s. Now
Y : S ! f1; 11; 111; . . . ; 11111111111g:
The range of Y here di¤ers dramatically from the random variable X above, but the
probabilities of the range values are the same in the sense that for any n,
7.4
Random Variables
253

Pr Y 1
X
n
j¼0
10 j
 
!
"
#
¼ Pr½X 1ðnÞ;
since in both cases these implied probabilities are defined by Pr½An, the probability of
the event in S defined by n Hs.
3. One can also change the probability structure by defining, for example, ZðsÞ ¼
P10
j¼1 sj10 j, where sj denotes the jth flip, with sj ¼ 0 for a T, and sj ¼ 1 for a H. Now
the range of Z di¤ers significantly from that of Y, containing every integer that can be
constructed with 10 digits, each of which is 0 or 1. There are consequently 210 points in
the range of Z, in contrast to 11 points in the range of X and Y. Also the probabilities
on the range of Z depend not only on the total number of heads in a given sample point
but also on the order of these heads in the sequence. So each event An above is split into
10
n
 
events by Z. In essence, Z maps each sample point in S to a distinct integer and
assigns a probability to this integer equal to the probability of the associated sample
point.
7.4.2
Random Variables and Probability Functions
Because this chapter addresses discrete probability theory, which is the theory as it
applies to finite and countably infinite sample spaces, it is possible that the range of
a random variable is any countable subset of R such as N, Z, or Q, so we introduce
a more economical way of demanding that X 1ðrÞ A E for every r in the range of the
random variable X. The idea is to use open intervals, ða; bÞ, that are either bounded
or unbounded. Then in every case, X 1½ða; bÞ must be an event either because it is
the finite or countable union of events of the form X 1ðrÞ for r A ða; bÞ, or because
it is the null event, j, if this interval is disjoint from the range of X.
Use of open intervals in this definition is just a convention, of course, since
X 1½ða; bÞ A E for all open intervals if and only if X 1½½a; b A E for all closed inter-
vals. To see this, first note that X 1½ða; bÞ A E for all bounded or unbounded inter-
vals implies that X 1½ðy; bÞ A E and hence the complement in S, which is
X 1½½b; yÞ A E. Similarly X 1½½a; yÞ A E. Also, if X 1½½b; yÞ A E and X 1½½a; yÞ
A E, then the intersection, X 1½½b; yÞ V X 1½½a; yÞ 1 X 1½½a; b A E. The reverse
implication is demonstrated similarly.
Next we formalize the definition with this open set convention:
Definition 7.24
Given a discrete sample space S and a complete collection of events
E ¼ fA j A HSg, a discrete random variable (r.v.) is a function
X : S ! R;
254
Chapter 7
Discrete Probability Theory

with X½S ¼ fxjgn
j¼1, where possibly n ¼ y, so that for any bounded or unbounded in-
terval, ða; bÞ H R:
X 1½ða; bÞ A E:
The probability density function (p.d.f.) or probability function associated with X,
denoted f or fX, is defined on the range of X by
f ðxjÞ ¼ Pr½X 1ðxjÞ:
ð7:20Þ
The distribution function (d.f.), or cumulative distribution function (c.d.f.) associated
with X, denoted F or FX, is defined on R by
FðxÞ ¼ Pr½X 1ðy; x:
ð7:21Þ
Note that the c.d.f. is the sum of the p.d.f. values, since Pr½X 1ðy; x ¼
P
xjax Pr½X 1ðxjÞ, and so
FðxÞ ¼
X
xjax
f ðxjÞ:
ð7:22Þ
Graphically, when the sample space is finite, the c.d.f. has a ‘‘jump’’ at each value of
xj in the range of X, and the graph of FðxÞ is horizontal otherwise. Such a function is
often called a step function for apparent reasons. When the sample space is countably
infinite, the c.d.f. will again look like a step function in the case of sparsely spaced
range, fxjg, such as the case for the positive integers. For a range with accumulation
points, fxjg, such as for the rationals in ½0; 1, the c.d.f. again would have jumps at
each rational, but no flat spots or steps per se.
Remark 7.25
Note that given any discrete random variable on S, with X½S ¼ fxjgn
j¼1,
where possibly n ¼ y, the collection of events defined by fX 1½xjgn
j¼1 are mutually
exclusive, and hence for any collection of points,
Pr 6 X 1½xj


¼
X
Pr½X 1½xj:
Example 7.26
Let S be defined as the sample space of 3 flips of a fair coin, and
X : S ! R defined by XðsÞ equals the number of Hs in s. So the range of X, as in def-
inition 2.2.3, Rng½X ¼ f0; 1; 2; 3g. The sample space S contains 23 ¼ 8 sample points,
1 each with 0 or 3 Hs, and 3 each with 1 or 2 Hs. This follows directly from the
values of
3
j
 	
. The probability of each sample point is 1
8 . Consequently the associated
probability density function is defined by
7.4
Random Variables
255

n:
0 1
2
3
f ðnÞ:
1
8
3
8
3
8
1
8
The graph of the cumulative distribution function, FðxÞ, is seen in figure 7.1.
7.4.3
Random Vectors and Joint Probability Functions
We begin with the simplest example and definition, and generalize later. Imagine that
there are two random variables defined on the given sample space: X; Y : S ! R,
which we think of as being combined into a random vector or a vector-valued random
variable:
ðX; YÞ : S ! R2:
Here, for a given sample point s A S, we define ðX; YÞ : s ! ðXðsÞ; YðsÞÞ.
Generalizing the notion of open interval in the definition of random variable, we
define the bounded or unbounded open rectangle, denoted ða; bÞ, where a ¼ ða1; a2Þ,
b ¼ ðb1; b2Þ and where a1 < b1 and a2 < b2, by
ða; bÞ ¼ fðx; yÞ j a1 < x < a2; b1 < y < b2:
ð7:23Þ
A closed rectangle, ½a; b, or a semi-closed (or semi-open) rectangle, ½a; bÞ or ða; b, is
defined similarly.
Figure 7.1
FðxÞ for Hs in three flips
256
Chapter 7
Discrete Probability Theory

The requirement to qualify as a random vector is that the pre-image of all open
rectangles be events, where for any point ðx; yÞ, the pre-image under ðX; YÞ is
defined as
ðX; YÞ1½ðx; yÞ ¼ X 1ðxÞ V Y 1ðyÞ:
With this setup we can define the joint probability density function or joint probabil-
ity function, f ðxj; yjÞ, as the probability of the event X 1ðxjÞ V Y 1ðyjÞ, and cor-
respondingly define the joint cumulative distribution function or joint distribution
function, Fðx; yÞ, as the probability of the event that is the pre-image of ðy; b,
where b ¼ ðx; yÞ. Then
Fðx; yÞ ¼
X
ðxj;yjÞaðx;yÞ
f ðxj; yjÞ;
with the understanding that ðxj; yjÞ a ðx; yÞ is shorthand for xj a x and yj a y. This
setup then easily generalizes to collections of 3 or more random variables, and we
state the formal definition in this generality:
Definition 7.27
Given a discrete sample space S, a complete collection of events
E ¼ fA j A HSg, and a collection of random variables on S, fXkgn
k¼1, a discrete ran-
dom vector is a function
X : S ! Rn;
where XðsÞ ¼ ðX1ðsÞ; X2ðsÞ; . . . ; XnðsÞÞ, with Xk½S ¼ fxkjgnk
j¼1, and possibly nk ¼ y,
for some or all k. For any bounded or unbounded open rectangle, ða; bÞ H Rn, we re-
quire that
X 1ðða; bÞÞ 1
6
x A ða;bÞ
X 1ðxÞ A E;
where X 1ðxÞ is defined for x ¼ ðx1; x2; . . . ; xnÞ by
X 1ðxÞ ¼ X 1
1 ðx1Þ V X 1
2 ðx2Þ V    V X 1
n ðxnÞ:
The joint probability density function (p.d.f.), or joint probability function, associated
with X, denoted f or fX, is defined on the range of X by
f ðx1; x2; . . . ; xnÞ ¼ Pr½X 1
1 ðx1Þ V X 1
2 ðx2Þ V    V X 1
n ðxnÞ:
ð7:24Þ
7.4
Random Variables
257

The joint cumulative distribution function (c.d.f.), or joint distribution function (d.f.)
associated with X, denoted F or FX, is defined on Rn by
FðxÞ ¼ Pr½X 1ðy; x:
ð7:25Þ
As was the case for random variables above, because Pr½X 1ðy; x ¼
P
x 0ax Pr½X 1ðx0Þ, where x0 a x is shorthand for x0
j a xj for all j, and x0 is in the
range of X, the counterpart to (7.22) is
FðxÞ ¼
X
x 0ax
f ðx0Þ:
ð7:26Þ
Example 7.28
1. On the sample space of 10-flip sequences of a fair coin, we could define random vari-
ables, fXjg10
j¼1 on s A S by
XjðsÞ ¼
1;
sj ¼ H;
1;
sj ¼ T:

In other words, each Xj is defined entirely in terms of the value of the jth flip. The
range of X is then the 210 vectors in R10 defined by RngðXÞ ¼ fx A R10 j xj ¼G1
for all jg. In this simple example the event X 1
1 ðx1Þ contains all sequences with an H
for the first flip if x1 ¼ 1, and all sequences with a T for the first flip if x1 ¼ 1,
and similarly for other components. In addition X 1ðxÞ ¼ X 1
1 ðx1Þ V X 1
2 ðx2Þ V    V
X 1
10 ðx10Þ is a unique sample point for every x A RngðXÞ and correspondingly,
f ðxÞ ¼ 210 for each such point.
2. Define Y1ðsÞ ¼ P5
j¼1 XjðsÞ and Y2ðsÞ ¼ P10
j¼6 XjðsÞ, where XjðsÞ is defined in case
1. Now with Y 1 ðY1; Y2Þ, we have RngðYÞ ¼ fy A R2 j y1; y2 ¼G5;G3;G1g. The
number of sample points in Y 1
j
ðyjÞ now varies by the value of yj. For instance,
Y 1
1 ð5Þ is the event of all 25-flip sequences starting with HHHHH, whereas Y 1
1 ð1Þ is
the event of all flip sequences with 3-Hs and 2-Ts in the first five flips, of which there
are
5
3
 
25 ¼ 5  26 sample points. Correspondingly the value of f ðyÞ ¼ Pr½Y 1
1 ðy1Þ V
Y 1
2 ðy2Þ also varies over the range of Y.
7.4.4
Marginal and Conditional Probability Functions
Once a joint probability density function is defined on a sample space, it is natural
to consider additional probability functions. To set the stage, we start with an
example.
258
Chapter 7
Discrete Probability Theory

Example 7.29
Consider the random variables Y1ðsÞ ¼ P3
j¼1 XjðsÞ and Y2ðsÞ ¼
P6
j¼4 XjðsÞ defined on the sample space of 6-flip sequences of a fair coin. As in case 1
in example 7.28 above, for s A S, XjðsÞ is defined by
XjðsÞ ¼
1;
sj ¼ H,
1;
sj ¼ T.

The joint p.d.f. of the pair, Y 1 ðY1; Y2Þ, is defined on RngðYÞ ¼ fy A R2 j y1; y2 ¼
G1;G3g, which contains 16 points. The associated probabilities are given by
ðy1; y2Þ:
ðG1;G1Þ ðG1;G3Þ ðG3;G1Þ ðG3;G3Þ
f ðy1; y2Þ:
9
26
3
26
3
26
1
26
where there are 4 sample points represented in each numerical column. It is easy to
see that the probabilities of the points in each column are the same by symmetry. For
example, switching all H $ T gives a 1:1 correspondence between the ð1; 1Þ and
ð1; 1Þ, while switching H $ T only for the first 3 flips identifies ð1; 1Þ and ð1; 1Þ.
Interchanging the first 3 and last 3 flips identifies ð1; 3Þ and ð3; 1Þ, and so forth.
Since Y1 and Y2 are perfectly good random variables on their own, we can also de-
fine the p.d.f.s f ðy1Þ and f ðy2Þ, which by symmetry will have the same values on the
same 4 points:
yj:
G1
G3
f ðyjÞ:
3
23
1
23
When calculating f ðyjÞ, intuition suggests that the original sample space was not
necessary, and that it would have been easier to consider the sample space of 3-flip
sequences of a fair coin. On the other hand, if the calculation was implemented in the
original sample space S, every 3-flip outcome for the given y1, say, would be counted
23 times, since in S, such an outcome would be associated with all 23 possible 3-flip
sequences underlying y2. Put another way, every 3-flip outcome for the given y1
would be associated with all possible outcomes of y2. Consequently we must have
f ðy1Þ ¼
X
y2
f ðy1; y2Þ
and
f ðy2Þ ¼
X
y1
f ðy1; y2Þ:
A simple calculation relating these values to the defining probability measure on S,
Pr, demonstrates that this is the case. In this context, f ðy1Þ and f ðy2Þ are called the
marginal probability density functions of the joint p.d.f. f ðy1; y2Þ.
7.4
Random Variables
259

Another calculation of interest is for the so-called conditional probability functions
of the joint p.d.f. f ðy1; y2Þ, denoted f ðy1 j y2Þ and f ðy2 j y1Þ. Focussing on f ðy1 j y2Þ
for specificity, this p.d.f. is defined relative to the probability of the conditional event
A j B, where A ¼ fs j Y1ðsÞ ¼ y1g and B ¼ fs j Y2ðsÞ ¼ y2g. In other words, the
conditional p.d.f. f ðy1 j y2Þ is defined as the probability of the conditional event
A j B:
f ðy1 j y2Þ ¼ Pr½A j B ¼ Pr½Y 1
1 ðy1Þ j Y 1
2 ðy2Þ:
Once again, this conditional p.d.f. must be related to the joint p.d.f, f ðy1; y2Þ,
which provides probabilities for each event, Pr½Y 1
1 ðy1Þ V Y 1
2 ðy2Þ ¼ Pr½A V B.
Now in the preceding section on conditional events, we have from (7.3) that if
Pr½B 0 0, then Pr½A j B ¼ Pr½AVB
Pr½B . Replacing this event notation with the corre-
sponding p.d.f. notation, we conclude that
f ðy1 j y2Þ ¼ f ðy1; y2Þ
f ðy2Þ
for f ðy2Þ 0 0;
with a corresponding formula for f ðy2 j y1Þ.
Before formalizing these ideas in a definition, note that for a more general joint
p.d.f., f ðy1; y2; . . . ; ynÞ, there are in fact 2n  2 possible marginal p.d.f.s. Specifi-
cally, there are
n
1
 
of the form f ðyjÞ,
n
2
 
of the form f ðyj; ykÞ for j 0 k, and so
forth. We get the 2 adjustment to the count because if no yj is chosen,
P
ðy1;y2;...;ynÞ f ðy1; y2; . . . ; ynÞ ¼ 1, which is not a probability function, whereas if all
yj are chosen, the original joint p.d.f. is produced.
In addition, for every such marginal p.d.f., one could define an associated condi-
tional p.d.f., such as f ðy1; y2 j y3; . . . ; ynÞ. However, the notation quickly becomes
cumbersome, so the following definition will be presented both in the more limited
generality of two random variables, a common framework for applications, and
then for the general case:
Definition 7.30
Given a random vector Y ¼ ðY1; Y2Þ on a discrete sample space, S,
and associated joint probability distribution function f ðy1; y2Þ, the marginal probabil-
ity density functions, denoted f ðy1Þ and f ðy2Þ, are defined by
f ðy1Þ ¼
X
y2
f ðy1; y2Þ;
ð7:27aÞ
f ðy2Þ ¼
X
y1
f ðy1; y2Þ:
ð7:27bÞ
260
Chapter 7
Discrete Probability Theory

The associated conditional probability density functions, denoted
f ðy1 j y2Þ and
f ðy2 j y1Þ, are defined by
f ðy1 j y2Þ ¼ f ðy1; y2Þ
f ðy2Þ
when f ðy2Þ 0 0;
ð7:28aÞ
f ðy2 j y1Þ ¼ f ðy1; y2Þ
f ðy1Þ
when f ðy1Þ 0 0:
ð7:28bÞ
Note that the law of total probability, stated in the context of events in (7.4), can
also be stated in terms of the joint, marginal, and conditional p.d.f. Specifically, we
have from (7.28a) that f ðy1; y2Þ ¼ f ðy1 j y2Þf ðy2Þ, and also from (7.27a) that f ðy1Þ
¼ P
y2 f ðy1; y2Þ. Combining, we obtain the law of total probability:
f ðy1Þ ¼
X
y2
f ðy1 j y2Þ f ðy2Þ;
ð7:29Þ
and the analogous identity for f ðy2Þ.
For the more general definition, we introduce the notion of a partition of the
random vector Y ¼ ðY1; Y2; . . . ; YnÞ into two nonempty subsets of random variables
Y1 ¼ ðYj1; Yj2; . . . ; YjmÞ, and Y2 ¼ ðYi1; Yi2; . . . ; YinmÞ, where this cumbersome nota-
tion is intended to imply that every Yk is in one of Y1 and Y2 but not both.
Definition 7.31
Given a random vector Y ¼ ðY1; Y2; . . . ; YnÞ on a discrete sample
space, S, an associated joint probability distribution function f ðy1; y2; . . . ; ynÞ, and a
partition, Y ¼ ðY1; Y2Þ, the marginal probability density function, denoted f ðy1Þ is
defined by
f ðy1Þ ¼
X
y2
f ðy1; y2; . . . ; ynÞ:
ð7:30Þ
The associated conditional probability density function, denoted f ðy2 j y1Þ, is defined by
f ðy2 j y1Þ ¼ f ðy1; y2; . . . ; ynÞ
f ðy1Þ
when f ðy1Þ 0 0:
ð7:31Þ
We note that these general formulas also provide general versions of the law of
total probability, but leave it to the reader to develop these formulas.
7.4.5
Independent Random Variables
Because a random variable X is defined so that the pre-image of open intervals
X 1½ða; bÞ are events in E with associated probabilities under the probability measure
7.4
Random Variables
261

Pr, it is natural to say that two random variables are independent if their pre-images
of all intervals are stochastically independent as events in E.
Definition 7.32
Random variables X1, X2 on the discrete sample space S are inde-
pendent random variables if for any intervals ðaj; bjÞ H R, bounded or unbounded,
X 1
1 ½ða1; b1Þ and X 1
2 ½ða2; b2Þ are stochastically independent events in E as in (7.5).
Equivalently, if X1 : S ! fx1jg and X2 : S ! fx2kg, then X1 and X2 are inde-
pendent if X 1
1 ½x1j and X 1
2 ½x2k are stochastically independent events for all x1j
and x2k.
More generally, a collection of random variables fXjgn
j¼1, where n may be y, are
mutually independent random variables if every collection of events of the form
fX 1
j
½ðaj; bjÞgn
j¼1 are mutually independent events as in (7.6), or equivalently,
fX 1
j
½xjkgn
j¼1 are mutually independent for any xjk A Rng½Xj.
Example 7.33
1. Define S as the sample space of all pairs of results achieved by rolling a fair die
twice. Specifically, S ¼ fðd1; d2Þ j 1 a dj a 6g, where d1 denotes the result on the first
roll, and d2 the result on the second. By the assumption of fairness, each numerical
value is equally likely and has probability of 1
6 of occurrence, and consequently the
probability function for S is defined as Pr½ðd1; d2Þ ¼ 1
36 for every such sample point.
Note that the values of this probability measure are influenced by the fact that the die
throws were sequential, and hence order counts. On this ordered sample space, define
first the random variables X; Y : S ! N by
X½ðd1; d2Þ ¼ d1;
Y½ðd1; d2Þ ¼ d2:
Intuition indicates that X and Y are independent random variables. To demonstrate
this, note that for any d1; d2 A f1; 2; . . . ; 6g, both X 1ðd1Þ and Y 1ðd2Þ are events in S
of 6 points with measures under Pr of 1
6 . Also X 1ðd1Þ V Y 1ðd2Þ contains a unique
sample point, specifically, ðd1; d2Þ, which has measure 1
36 under Pr. In other words, for
all ðd1; d2Þ,
Pr½X 1ðd1Þ V Y 1ðd2Þ ¼ Pr½X 1ðd1Þ Pr½Y 1ðd2Þ:
2. Now define a new random variable Z on S above as follows:
Z½ðd1; d2Þ ¼ d1 þ d2:
262
Chapter 7
Discrete Probability Theory

Intuitively we expect X and Z not to be independent. That is because, if Z½ðd1; d2Þ ¼
12 (or 2), it must be the case that X½ðd1; d2Þ ¼ 6 (or 1). More formally, Z assumes
all integer values 2 a k a 12, and the event defined by Z1ðkÞ has probabilities
k:
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
Pr½Z1ðkÞ:
1
36
2
36
3
36
4
36
5
36
6
36
5
36
4
36
3
36
2
36
1
36
It is apparent that the numerator of Pr½Z1ðkÞ also represents the number of sample
points in the associated event. As noted above, for each 1 a j a 6, X 1ðjÞ contains 6
sample points, and Pr½X 1ðjÞ ¼ 1
6 for all j. Now it is straightforward to justify that
X 1ð jÞ V Z1ðkÞ contains one sample point or none. For example, X 1ð1Þ V Z1ð12Þ
¼ j, while X 1ð4Þ V Z1ð7Þ ¼ ð4; 3Þ. More generally, if d1 ¼ j and d1 þ d2 ¼ k,
there is a unique point provided that 1 a k  j a 6, and no point otherwise. Hence
Pr½X 1ð jÞ V Z1ðkÞ equals 0 or 1
36 , which can equal the product of probabilities of the
respective events only when k ¼ 7. Consequently X and Z are not independent.
3. If instead of as in case 1, a pair of dice were thrown without keeping track of order,
then the sample space, S 0, would contain only 21 rather than 36 sample points. One re-
alization of this space is S 0 ¼ fðd1; d2Þ j 1 a d1 a d2 a 6g where d1 denotes the smaller
result, d2 the larger. The associated probability measure is then given by
Pr½ðd1; d2Þ ¼
1
36
d1 ¼ d2;
1
18
d1 < d2:
(
Define the random variables U; W : S 0 ! N by
U½ðd1; d2Þ ¼ minðd1; d2Þ;
W½ðd1; d2Þ ¼ maxðd1; d2Þ:
Now U and W are not independent. For example, Pr½U1ð1Þ ¼ 11
36 , since this event
contains the sample point
U1ð1Þ ¼ fð1; dÞ j 1 a d a 6g;
which has measure 11
36 by the above given probability measure on S 0. On the other
hand, Pr½W 1ð1Þ ¼ 1
36 , since W 1ð1Þ ¼ ð1; 1Þ. Also U1ð1Þ V W 1ð1Þ ¼ W 1ð1Þ.
Consequently
Pr½U1ð1Þ V W 1ð1Þ 0 Pr½U1ð1Þ Pr½W 1ð1Þ:
7.4
Random Variables
263

The notion of independent random variables can also be defined in terms of the
joint, conditional and marginal probability distribution functions.
Definition 7.34
Given a random vector Y ¼ ðY1; Y2Þ on a discrete sample space S
and associated joint probability density function f ðy1; y2Þ, the random variables Y1
and Y2 are independent random variables if
f ðy1; y2Þ ¼ f ðy1Þ f ðy2Þ;
ð7:32aÞ
or equivalently if f ðy2Þ 0 0,
f ðy1 j y2Þ ¼ f ðy1Þ:
ð7:32bÞ
More generally, given a random vector Y ¼ ðY1; Y2; . . . ; YnÞ on the discrete sample
space S, with associated joint probability density function f ðy1; y2; . . . ; ynÞ, the ran-
dom variables fYjg are mutually independent random variables if given any partition
Y ¼ ðY1; Y2Þ
f ðy1; y2; . . . ; ynÞ ¼ f ðY1Þf ðY2Þ;
ð7:33aÞ
or equivalently if f ðY2Þ 0 0,
f ðY1 j Y2Þ ¼ f ðY1Þ:
ð7:33bÞ
In particular, we then have
f ðy1; y2; . . . ; ynÞ ¼ f ðy1Þ f ðy2Þ . . . f ðynÞ:
ð7:34Þ
7.5
Expectations of Discrete Distributions
7.5.1
Theoretical Moments
The definitions and notation for moments here closely parallel that given in sec-
tion 3.3.2 for moments of sample data. This is no coincidence, as will be discussed
below.
Expected Values
The general structure of the formulas below is seen repeatedly in probability theory.
These calculations represent what are known as expected value calculations, and
sometimes referred to as taking expectations. The general case is defined first, then
specific examples are presented.
264
Chapter 7
Discrete Probability Theory

Definition 7.35
Given a discrete random variable, X : S ! R, and function gðxÞ
defined on the range of X, Rng½X H R, the expected value of gðXÞ, denoted E½gðXÞ,
is defined as
E½gðXÞ ¼
X
sj AS
gðXðsjÞÞ PrðsjÞ:
ð7:35Þ
If fxjg H R denotes the range of X, and the p.d.f. of X is denoted by f ðxÞ so that
f ðxjÞ 1 PrðsjÞ with xj 1 XðsjÞ, then this expected value can be defined by
E½gðXÞ ¼
X
j
gðxjÞf ðxjÞ:
ð7:36Þ
In either case, this expectation is only defined when the associated summation is abso-
lutely convergent, and so in the notation of (7.36), since f ðxjÞ b 0, it is required that
X
j
jgðxjÞj f ðxjÞ < y:
ð7:37Þ
If (7.37) is not satisfied, we say that E½gðXÞ does not exist.
Remark 7.36
1. The condition in (7.37) is automatically satisfied if the fxjg is finite. The purpose of
this restriction in the countably infinite case is to avoid the problem discussed in section
6.1.4, that if only conditionally convergent, the value of this summation is not well
defined and depends on the order in which the summation is carried out.
2. All expectation formulas can be stated in terms of the random variable X, the sam-
ple space S, and its probability measure Pr, or directly in terms of the p.d.f. associated
with X. In general, we will only provide the p.d.f. versions as in (7.36) and leave it as
an exercise for the reader to formulate the sample space versions as in (7.35).
3. It is to be explicitly understood without further repetition that expectation defini-
tions are valid only when the respective absolute convergence conditions as in (7.37)
are satisfied.
4. When needed for clarity, a subscript is placed on the expectations symbol to identify
what variable is involved in the expectation. For example, given p.d.f. f ðxÞ, the mean-
ing of E½X is unambiguous, so expressing this as EX½X is redundant. On the other
hand, the meaning of E½XY is ambiguous, since it is not clear which variable is
involved. So in this case one would clarify as EX½XY or EY½XY or EXY½XY.
7.5
Expectations of Discrete Distributions
265

Of course, all expectations of random variables in finite sample spaces exist when
gðxÞ is defined and hence finitely valued on the range of X. However, for random
variables on countably infinite sample spaces, expected values may not exist even
when gðxÞ is defined on the range of X.
Example 7.37
If S is countally infinite, X : S ! N is defined by XðsjÞ ¼ j with range
equal to the positive integers, and f ðjÞ is given by f ðjÞ ¼ c
j 2 , where c is chosen so that
P
j f ð jÞ ¼ 1, then E½X does not exist, since E½X ¼ P
j j c
j 2 ¼ P
j
c
j is a multiple of the
harmonic series and hence not finite. If instead X is defined by XðsjÞ ¼ ð1Þ jj, then
again E½X does not exist. This is because, although E½X is conditionally convergent,
it is not absolutely convergent. Similarly it is easy to find p.d.f.s with finite expected
values up to some exponent: gðxÞ ¼ xn, but with no finite expected values with larger
exponents using power harmonic series from example 6.9 to define f ðjÞ.
On the assumption that expected values exist, they are easy to work with in terms
of addition and scalar multiplication.
Proposition 7.38
If gðxÞ and hðxÞ are functions for which E½gðxÞ and E½hðxÞ exist,
and a, b, c are real numbers, then E½agðxÞ þ bhðxÞ þ c exists and
E½agðxÞ þ bhðxÞ þ c ¼ aE½gðxÞ þ bE½hðxÞ þ c:
ð7:38Þ
Proof
This result is immediate from the definition, but we must first verify that
agðxÞ þ bhðxÞ þ c satisfies (7.37). This, of course, follows from the triangle inequality
jagðxÞ þ bhðxÞ þ cj a jaj jgðxÞj þ jbj jhðxÞj þ jcj;
and the assumption that E½gðxÞ and E½hðxÞ exist.
n
On the other hand, expected values do not work well with multiplication and divi-
sion, and as might be expected,
E½ f ðxÞgðxÞ 0 E½ f ðxÞE½gðxÞ;
E f ðxÞ
gðxÞ


0 E½ f ðxÞ
E½gðxÞ :
Conditional and Joint Expectations
Expected value calculations can also be defined with respect to joint probability den-
sity functions, as well as conditional probability density functions. For example, if
X ¼ ðX1; X2Þ is a random vector with joint p.d.f. f ðx1; x2Þ, and gðx1; x2Þ is defined
on Rng½X H R2, we define the joint expectation of gðx1; x2Þ by
266
Chapter 7
Discrete Probability Theory

E½gðX1; X2Þ ¼
X
ðx1;x2Þ
gðx1; x2Þf ðx1; x2Þ:
ð7:39Þ
Many such calculations are possible with di¤ering values of gðx1; x2Þ. One impor-
tant application of this type of formula is in the case where fXjg are independent
trials from a given p.d.f. Another important example is for the covariance of two ran-
dom variables. Both are addressed below.
If f ðx1 j x2Þ is one of the associated conditional p.d.f.s, and gðxÞ is given, then the
conditional expected value or conditional expectation is defined as
E½gðX1Þ j X2 ¼ x2 ¼
X
x1
gðx1Þf ðx1 j x2Þ:
ð7:40Þ
Sometimes for clarity, though cumbersome, the conditional expectation symbol is
written with a subscript of X1 j X2 as in EX1 j X2½gðX1Þ j X2 or E½gðX1Þ j X2.
Remark 7.39
Unlike most expected values, which provide numerical results, a condi-
tional expectation can be interpreted as a function on the original sample space S,
defined by s ! E½gðX1Þ j X2ðsÞ. It is in fact a random variable on S, since the pre-
image of an open interval ða; bÞ H R is just the union of countably many events, which
is an event in E. It is then the case that the expectation of this random variable under
the p.d.f. f ðx2Þ equals the expectation of gðxÞ using f ðx1Þ. In other words,
EX2½EX1 j X2½gðX1Þ j X2 ¼ EX1½gðX1Þ:
ð7:41Þ
The demonstration of this somewhat tediously notated formula is actually simple. By
absolute convergence, we can reverse the order of the double summation and apply the
law of total probability:
EX2½EX1 j X2½gðX1Þ j X2 ¼
X
x2
X
x1
gðx1Þf ðx1 j x2Þ
"
#
f ðx2Þ
¼
X
x1
gðx1Þ
X
x2
f ðx1 j x2Þf ðx2Þ
"
#
¼
X
x1
gðx1Þf ðx1Þ:
This interpretation of E½gðX1Þ j X2 as a random variable on S is critical in advanced
probability theory.
7.5
Expectations of Discrete Distributions
267

Mean
The mean of X, denoted m, is defined as m ¼ E½X,
m ¼
X
i
xi f ðxiÞ:
ð7:42Þ
In some applications, the random variable X may be defined in a complicated way,
perhaps dependent on another random variable Y, and for which the conditional ex-
pectation, E½X j Y is simpler to evaluate. An immediate application of (7.41) with
gðXÞ ¼ X leads to the following identity between E½X and the various conditional
expectations E½X j Y, which is known as the law of total expectation:
E½X ¼ E½E½X j Y:
ð7:43Þ
While this formula may at first appear ambiguous, a moment of reflection justifies
that it is well defined even without the subscript clutter of (7.41). The inner expecta-
tion can only be defined relative to the conditional p.d.f. f ðx j yÞ as E½X j Y ¼
P
i xi f ðxi j YÞ. Once this expectation is performed, the remaining term is a function
of Y alone, and hence the outer expectation must be calculated relative to the mar-
ginal p.d.f., f ðyÞ. In other words,
E½E½X j Y ¼
X
j
X
i
xi f ðxi j yjÞf ðyjÞ:
Variance
The variance of X, denoted s2, is defined as E½ðX  mÞ2:
s2 ¼
X
i
ðxi  mÞ2f ðxiÞ;
ð7:44Þ
and the standard deviation, denoted s, is the positive square root of the variance. It is
often more convenient to denote the variance by Var½X, and standard deviation by
s.d.½X, as this notation has the advantage of making the random variable explicit. In
addition one can also use the notation s2
X and sX.
It is often easier to calculate variance by first expanding ðxi  mÞ2 ¼ x2
i  2mxi þ
m2, and then using (7.38) to obtain
s2 ¼ E½X 2  E½X2:
ð7:45Þ
As noted above in the discussion of the mean, it may be the case that the random
variable X is defined in a complicated way, perhaps dependent on another random
268
Chapter 7
Discrete Probability Theory

variable Y, and that Var½X is di‰cult to estimate directly, yet the conditional vari-
ance Var½X j Y is simpler. Of course, this conditional variance is well defined as the
variance of X, utilizing the conditional p.d.f. f ðx j yÞ. In other words,
Var½X j Y ¼
X
i
ðxi  mX j YÞ2f ðxi j YÞ;
where the conditional mean is defined, mX j Y ¼ E½X j Y.
The question then becomes, can Var½X be recovered from the conditional vari-
ances Var½X j Y the same way that the mean can be recovered from the conditional
means via (7.43)? The answer is ‘‘yes,’’ but with a slightly more complicated formula,
known as the law of total variance:
Var½X ¼ E½Var½X j Y þ Var½E½X j Y:
ð7:46Þ
Before addressing the derivation, note that the formula above is again well defined.
As Var½X j Y and E½X j Y are functions only of Y, E½Var½X j Y and Var½E½X j Y
must be calculated using the marginal p.d.f. f ðyÞ, and the variance term is defined as
in (7.44), with m ¼ E½E½X j Y ¼ E½X. Summarizing, we have
E½Var½X j Y ¼
X
i
Var½X j yi f ðyiÞ;
Var½E½X j Y ¼
X
i
ðE½X j yi  mÞ2f ðyiÞ:
To derive (7.46), we use the variance formula in (7.45), and substitute the law of
total expectation in (7.41):
Var½X ¼ E½X 2  ðE½XÞÞ2
¼ E½E½X 2 j Y  ðE½E½X j YÞ2:
Now another application of (7.45) is
E½X 2 j Y ¼ Var½X j Y þ E½X j Y2;
which is inserted into the formula above to produce:
Var½X ¼ E½Var½X j Y þ E½E½X j Y2  ðE½E½X j YÞ2:
7.5
Expectations of Discrete Distributions
269

Finally, the last two terms are equal to Var½E½X j Y by another application of
(7.45), completing the derivation.
Because the laws of total probability, expectation, and variance are so important,
the next proposition brings these results together:
Proposition 7.40
Let X and Y be random variables on a discrete probability space
S, with associated joint p.d.f. f ðx; yÞ, marginal p.d.f.s f ðxÞ and f ðyÞ, and conditional
p.d.f. f ðx j yÞ. Then:
1. Law of total probability,
f ðxÞ ¼
X
y
f ðx j yÞf ðyÞ:
ð7:47Þ
2. Law of total expectation,
E½X ¼ E½E½X j Y:
ð7:48Þ
3. Law of total variance,
Var½X ¼ E½Var½X j Y þ Var½E½X j Y:
ð7:49Þ
Example 7.41
Let X denote the number of heads obtained in Y flips of a fair coin,
where Y is the number of dots obtained in a roll of a fair die. The goal is to calculate
E½X and Var½X. To formalize a sample space, define S as the space of n-flips of a fair
coin for n ¼ 1; 2; 3; . . . ; 6. So S ¼ fðF1; F2; . . . ; FnÞ j 1 a n a 6g. Here Fj ¼ 1 for an H
on the jth flip, and 0 otherwise, so S contains P6
n¼1 2n ¼ 27  1 sample points. The
probability measure is defined on each point by
Pr½ðF1; F2; . . . ; FnÞ ¼ 1
6
1
2n :
Now X and Y are defined on S by
Y½ðF1; F2; . . . ; FnÞ ¼ n;
X½ðF1; F2; . . . ; FnÞ ¼
X
n
j¼1
Fj;
and so Rng½Y ¼ f1 a n a 6g and Rng½X ¼ f0 a m a 6g. Also f ðnÞ ¼ 1
6 for all n.
For E½X j Y ¼ n and Var½X j Y ¼ n, we use formulas below in (7.99) from sec-
tion 7.6.2 on the binomial distribution. Then E½X j Y ¼ n ¼ n
2 , and from (7.48),
E½X ¼ E n
2
 
, so
270
Chapter 7
Discrete Probability Theory

E½X ¼ 1
12
X
6
n¼1
n ¼ 21
12 :
Next, Var½X j Y ¼ n ¼ n
4 , so E½Var½X j Y ¼ 21
24 . Also from E½X j Y ¼ n ¼ n
2 we ob-
tain that
Var½E½X j Y ¼ E n2
4



E n
2
 

2
¼ 1
24
X
6
n¼1
n2 
21
12

2
¼ 105
144 :
Finally, using (7.49) obtains
Var½X ¼ 21
24 þ 105
144 ¼ 231
144 :
Covariance and Correlation
As noted above, there are many expected values that can be defined with a joint
p.d.f. One common set of expectations, given f ðx1; x2; . . . ; xnÞ, is to evaluate the
covariance between any two of these random variables. With the associated marginal
densities f ðxjÞ, the respective means mj and variances s2
j of each Xj can be calculated
as discussed above. To calculate the covariance between Xi and Xj requires the
joint p.d.f. f ðxi; xjÞ. Although the notation is not standardized, we denote this
expectation by sij, and sometimes CovðXi; XjÞ, the covariance is defined by
E½ðXi  miÞðYj  mjÞ:
sij ¼
X
k;l
ðxk  miÞðxl  mjÞf ðxk; xlÞ:
ð7:50Þ
With a slight abuse of notation, we can define sjj 1 s2
j ¼ Var½Xj.
Note that a calculation produces a result analogous to (7.45):
sij ¼ E½XiYj  E½XiE½Yj:
ð7:51Þ
Also, if Xi and Xj are independent, then f ðxi; xjÞ ¼ f ðxiÞf ðxjÞ, and it is apparent
that sij ¼ 0, since
7.5
Expectations of Discrete Distributions
271

X
kl
ðxk  miÞðxl  mjÞf ðxk; xlÞ ¼
X
k
ðxk  miÞf ðxkÞ
X
l
ðxl  mjÞ f ðxlÞ:
The correlation between xi and xj, denoted rij, and sometimes CorrðXi; XjÞ, is
defined as
rij ¼ sij
sisj
;
ð7:52Þ
which is equivalently calculated as rij ¼ P
k;l
xkmi
si

	
xlmj
sj

	
f ðxk; xlÞ. The random
variables are said to be uncorrelated if rij ¼ 0, they are positively correlated if rij > 0,
whereas they are said to be negatively correlated if rij < 0. As noted above, indepen-
dent random variables are uncorrelated, and hence have rij ¼ 0.
However, being uncorrelated is a weaker condition on two random variables than
being independent.
Example 7.42
Define f ðx; yÞ by
f ðx; yÞ ¼
1
3 ;
ðx; yÞ ¼ ð1; 1Þ,
1
3 ;
ðx; yÞ ¼ ð0; 0Þ,
1
3 ;
ðx; yÞ ¼ ð1; 1Þ.
8
>
>
<
>
>
:
Then f ðxÞ ¼ 1
3 for x ¼ 1; 0; 1, and f ðyÞ ¼ 2
3 for y ¼ 1 and f ðyÞ ¼ 1
3 for y ¼ 0. Con-
sequently X and Y are not independent, since f ðx; yÞ 0 f ðxÞ f ðyÞ. On the other hand,
X and Y are uncorrelated, since E½XY ¼ 0, E½X ¼ 0 and E½Y ¼ 2
3 imply that sXY ¼
E½XY  E½XE½Y ¼ 0, and so rxy ¼ 0.
An important application of the Cauchy–Schwarz inequality is as follows:
Proposition 7.43
Given random variables X, Y with joint p.d.f. f ðx; yÞ,
jsXYj a sXsY:
ð7:53Þ
In other words,
1 a rXY a 1:
ð7:54Þ
Proof
Since f ðx; yÞ b 0, we have
sXY ¼
X
i; j
ðxi  mXÞðyj  mYÞf ðxi; yjÞ
¼
X
i; j
ðxi  mXÞ
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
f ðxi; yjÞ
q
h
i
ðyj  mYÞ
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
f ðxi; yjÞ
q
h
i
:
272
Chapter 7
Discrete Probability Theory

This second summation is seen to be an inner product, and by the Cauchy–Schwarz
inequality, the square of this inner product is bounded by the product of the sums of
squares:
s2
XY a
X
i; j
ðxi  mXÞ
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
f ðxi; yjÞ
q
h
i2X
i; j
ðyj  mYÞ
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
f ðxi; yjÞ
q
h
i2
¼
X
i; j
ðxi  mXÞ2f ðxi; yjÞ
X
i; j
ðyj  mYÞ2f ðxi; yjÞ
¼
X
i
ðxi  mXÞ2f ðxiÞ
X
j
ðyj  mYÞ2f ðyjÞ ¼ s2
Xs2
Y:
n
The covariance also arises in the variance calculation of the sum of random vari-
ables, X ¼ Pn
j¼1 ajXj for constants fajg. The associated p.d.f. used in the expected
value calculation is the joint p.d.f., f ðx1; x2; . . . ; xnÞ. With this we see that
E
X
n
j¼1
ajXj
"
#
¼
X
n
j¼1
ajE½Xj:
ð7:55Þ
Also
ðX  E½XÞ2 ¼
X
n
j¼1
aj½Xj  E½Xj
 
!2
¼
X
n
i¼1
X
n
j¼1
aiaj½Xi  E½Xi½Xj  E½Xj:
After expectations are taken, this leads to
Var
X
n
j¼1
ajXj
"
#
¼
X
n
i¼1
X
n
j¼1
aiajsij
ð7:56aÞ
¼
X
n
j¼1
a2
j s2
j þ 2
X
i<j
aiajrijsisj:
ð7:56bÞ
Note that when the component random variables are independent, or simply
uncorrelated:
7.5
Expectations of Discrete Distributions
273

Var
X
n
j¼1
ajXj
"
#
¼
X
n
j¼1
a2
j s2
j :
ð7:57Þ
General Moments
Generalizing the definition of the mean of a random variable, the nth moment,
denoted m0
n, is defined as E½X n for n b 0:
m0
n ¼
X
i
xn
i f ðxiÞ;
ð7:58Þ
so in particular, m0
0 ¼ 1, m0
1 ¼ m, and m0
2 ¼ s2 þ m2 as noted in (7.45).
Note that a direct application of (7.41) with gðXÞ ¼ X n produces
E½X n ¼ E½E½X n j Y;
as was used in the derivation of the law of total variance.
General Central Moments
Generalizing the definition of variance of a random variable, the nth central moment,
denoted mn, is defined as E½ðX  mÞn for n b 0:
mn ¼
X
i
ðxi  mÞnf ðxiÞ;
ð7:59Þ
so in particular, m0 ¼ 1, m1 ¼ 0, and m2 ¼ s2.
Absolute Moments
When n is odd, the value of the moments E½X n and/or E½ðX  mÞn can reflect the
cancellation of positive and negative terms. The notion of absolute moments is used
to value the associated absolutely convergent series. The nth absolute moment,
denoted m0
jnj, is defined as E½jXjn for n b 0:
m0
jnj ¼
X
i
jxijnf ðxiÞ;
ð7:60Þ
and the nth absolute central moment, denoted mjnj, is defined as E½jX  mjn for n b 0:
mjnj ¼
X
i
jxi  mjnf ðxiÞ:
ð7:61Þ
This notation is descriptive but not standard.
274
Chapter 7
Discrete Probability Theory

Because of the condition in (7.37), absolute moments always exist when the corre-
sponding moments exist. Of course, for n even, the absolute moments agree with the
respective moments defined above. For n odd, the moments may agree with the ab-
solute moments, for instance, if the range of X is positive, but the central moments
and absolute central moments will not agree, since fxi  mg will always have both
positive and negative terms.
Moment-Generating Function
The moment-generating function (m.g.f.), as the name implies, reflects an expected
value calculation that produces a function rather than a numerical constant. Denoted
MðtÞ, or MXðtÞ, it is defined as E½eXt:
MXðtÞ ¼
X
i
exitf ðxiÞ:
ð7:62Þ
Of course, MXð0Þ ¼ 1, so the question of existence of the m.g.f. relates to existence
for some interval, jtj < T. It is important to note at the outset that MðtÞ does not
always exist.
As we have seen before and will prove in chapter 9, the exponential function can
be expanded into the power series:
ex ¼
X
y
n¼0
xn
n! :
ð7:63Þ
This series converges absolutely for all x by the ratio test,
x nþ1
ðnþ1Þ!
x n
n!


 ¼
x
n þ 1


 ! 0
as n ! y;
so what needs to be shown in chapter 9 is that the function of x defined by this series
is indeed equal to ex.
Substituting the corresponding expression for exit into (7.62), and using the arith-
metic properties of expected value noted above and the assumption of absolute con-
vergence justified by the existence of MXðtÞ, we derive
MXðtÞ ¼
X
i
X
y
n¼0
ðxitÞn
n!
f ðxiÞ ¼
X
y
n¼0
tn
n!
X
i
xn
i f ðxiÞ;
and hence
7.5
Expectations of Discrete Distributions
275

MXðtÞ ¼
X
y
n¼0
m0
ntn
n! :
ð7:64Þ
Of course, since all terms in the summation are positive, all these manipulations
require the assumption that MXðtÞ actually exists and so the series in (7.62) con-
verges and hence converges absolutely. This is always the case for finite sample
spaces, but not necessarily the case when the sample space is countably infinite. As
seen in section 6.1.4, it is the absolute convergence of this series that justifies the
manipulations in the double series and the reversal of the order of the summations.
In chapter 9 we will see that the moments fm0
ng can in turn be recovered from the
moment-generating function, or better said, ‘‘generated’’ from the m.g.f., if it con-
verges in an interval containing 0. Specifically, with MðnÞ
X ðtÞ denoting the nth deriva-
tive of the function MXðtÞ with respect to t, we will see that
m0
n ¼ MðnÞ
X ð0Þ:
ð7:65Þ
A simple modification to the definition of the m.g.f. can be introduced that will
generate the central moments. Specifically, since X  m has the same p.d.f. as does
X, its moment-generating function is defined by MXmðtÞ ¼ P
i eðximÞtf ðxiÞ. Apply-
ing (7.63) obtains
MXmðtÞ ¼
X
y
n¼0
mntn
n! ;
ð7:66Þ
from which is produced
mn ¼ MðnÞ
Xmð0Þ:
ð7:67Þ
For a joint probability density function, f ðx1; x2; . . . ; xnÞ, the moment-generating
function is analogously defined. The definition above where MXðtÞ 1 E½eXt is gener-
alized so that the m.g.f. is now a function of ðt1; t2; . . . ; tnÞ, and defined with the aid
of boldface vector notation as MXðtÞ 1 E½eXt, where X  t denotes the inner product.
In other words,
MXðtÞ ¼
X
ðx1;x2;...;xnÞ
eT xitif ðx1; x2; . . . ; xnÞ:
ð7:68Þ
If the random variables in the definition of f ðx1; x2; . . . ; xnÞ are independent, then
(7.34) is satisfied, so
276
Chapter 7
Discrete Probability Theory

MXðtÞ ¼
Y
n
i¼1
MXiðtiÞ:
If the random variables are independent and identically distributed, then with Y ¼
Pn
i¼1 Xi we derive from (7.34) and directly from MYðtÞ ¼ E et T Xi


that
MYðtÞ ¼ ½MXðtÞn:
ð7:69Þ
Characteristic Function
The characteristic function (c.f.) is defined similarly to the m.g.f., and it will again be
possible to generate moments from it, but it has the advantage that it always exists.
The disadvantage to some is that while MXðtÞ is a function MXðtÞ : R ! R, the
characteristic function, denoted CXðtÞ, is a function CXðtÞ : R ! C. Specifically,
CXðtÞ ¼ E½eiXt, where i denotes the ‘‘imaginary unit’’ i ¼
ffiffiffiffiffiffi
1
p
, producing
CXðtÞ ¼
X
j
eixjtf ðxjÞ:
ð7:70Þ
It is straightforward to confirm that CXðtÞ exists for all t A R, since the summation
converges absolutely. This is demonstrated using the triangle inequality and a conse-
quence of Euler’s formula: that jeixjtj ¼ 1 for all t and xj. Specifically,
jCXðtÞj a
X
j
jeixjtf ðxjÞj ¼
X
j
f ðxjÞ ¼ 1:
Unlike the case of the m.g.f., which may not exist but is di¤erentiable when it does
exist, the characteristic function always exists, but it need not be di¤erentiable. How-
ever, if all moments exist, then using the same manipulations above, justified by ab-
solute converge, produces
CXðtÞ ¼
X
y
n¼0
m0
nðitÞn
n!
;
ð7:71Þ
and once again the moments can be recovered from this function as in (7.65). With
analogous notation,
m0
n ¼ 1
in CðnÞ
X ð0Þ:
ð7:72Þ
Central
moments
can
again
be
generated
if
they
exist
using
CXmðtÞ ¼
P
j eiðxjmÞtf ðxjÞ; then
7.5
Expectations of Discrete Distributions
277

CXmðtÞ ¼
X
y
n¼0
mnðitÞn
n!
;
ð7:73Þ
mn ¼ 1
in CðnÞ
Xmð0Þ:
ð7:74Þ
For a joint probability density function f ðx1; x2; . . . ; xnÞ, the characteristic func-
tion is analogously defined. The definition above where CXðtÞ ¼ E½eiXt is generalized
so that the c.f. is a function of ðt1; t2; . . . ; tnÞ, and defined with the aid of boldface
vector notation as CXðtÞ 1 E½eiXt. In other words,
CXðtÞ ¼
X
ðx1;x2;...;xnÞ
ei T xjtjf ðx1; x2; . . . ; xnÞ:
ð7:75Þ
Remark 7.44
An important property of the moment-generating and characteristic
functions is that they ‘‘characterize’’ the discrete probability density function (a prop-
erty we will prove in chapter 8 but only in the case of finite discrete random variables).
The proof in the more general cases requires the tools of real analysis and complex
analysis. What ‘‘characterize’’ means is that if CXðtÞ ¼ CYðtÞ or MXðtÞ ¼ MYðtÞ for
random variables X and Y, and for t A I where I is any open interval containing 0, then
the discrete probability density functions are equal: f ðxÞ ¼ gðyÞ. In the finite discrete
case this means that if fxign
i¼1 and fyjgm
j¼1 are the respective domains of these proba-
bility functions, arranged in increasing order, then n ¼ m, xi ¼ yi and f ðxiÞ ¼ gðyiÞ
for all i. The m.g.f. and c.f. also characterize the p.d.f. of random variables in the
more general cases to be developed later. Since the characteristic function always
exists, this result can be applied to any p.d.f. and in any context.
*7.5.2
Moments of Sample Data
An important application of the general random vector expectation formula (7.39) is
to so-called sample data expectations. In this section we provide a theoretical frame-
work for the sample statistics introduced in section 3.3.2.
Given a sample space S, we have the theoretical framework for a random sample
or independent trials introduced in section 7.2.6 above. Specifically, recall that a ran-
dom sample of size n was identified with a sample point in a new n-trial sample
space, denoted S n, that was given a probability structure defined in (7.7). In this sec-
tion we apply this structure to random samples of a given random variable, and de-
rive some important formulas related to the moments of these samples.
In the space S we assume that there is given a random variable X, and define a
random vector X ¼ ðX1; X2; . . . ; XnÞ on S n. For s ¼ ðs1; s2; . . . ; snÞ A S n, we define
278
Chapter 7
Discrete Probability Theory

XjðsÞ ¼ XðsjÞ. In the same way that ðs1; s2; . . . ; snÞ represents a random sample of n
possible sample points, with probability in S n defined so that PnðsÞ ¼ Qn
j¼1 PrðsjÞ,
the random vector of values, XðsÞ ¼ ðX1ðsÞ; X2ðsÞ; . . . ; XnðsÞÞ A Rn is a random sam-
ple of the values assumed by X on S. In other words, the components of this random
vector are independent in the formal meaning given in (7.34) above.
To see this, let f ðx1; x2; . . . ; xnÞ be the joint p.d.f. defined on the Rng½X. That is,
f ðx1; x2; . . . ; xnÞ ¼ PnðX 1
1 ðx1Þ; X 1
2 ðx2Þ; . . . ; X 1
n ðxnÞÞ:
Then by (7.7),
f ðx1; x2; . . . ; xnÞ ¼
Y
n
j¼1
PrðX 1
j
ðxjÞÞ
¼
Y
n
j¼1
f ðxjÞ;
where f ðxÞ is the p.d.f. of the random variable X.
In summary, we see that if a random variable X on S is generalized as above to a
random vector X on the n-trial sample space S n, then the collection of component
random variables fXjðsÞg comprises independent random variables on S in the sense
defined above, and
f ðx1; x2; . . . ; xnÞ ¼
Y
n
j¼1
f ðxjÞ:
ð7:76Þ
Initially this construction of a random sample may appear overly formal and un-
necessary. In applications the random variable X is usually defined as the outcome of
an experiment, or as an observation, and the notion of independent trials is under-
stood as meaning that the experiment is repeated many times, or other observations
are made. In such cases the truth of the identity in (7.76) would appear obvious to
anyone that has flipped a coin, or rolled dice, and so forth. And in many applications
this is a perfectly legitimate intuitive framework for what a random sample is, and
perfectly legitimate justification for the meaning of independent sample.
But intuition does not always guarantee that a rigorous development is possible.
So the construction above provides a rigorous construction, in a discrete sample
space context, of what a random sample from a sample space represents, and also,
what n independent trials of a random variable means. And better than our intuition,
7.5
Expectations of Discrete Distributions
279

this formality will lead the way to the corresponding ideas in the less intuitive
frameworks.
Definition 7.45
1. Given a discrete sample space S and a random variable X : S ! R, the terminology
that fXjgn
j¼1 are n-independent and identically distributed (i.i.d.) random variables will
mean that X 1 ðX1; X2; . . . ; XnÞ is a random vector on S n, where for s ¼ ðs1; s2; . . . ; snÞ
A S n the component random variables are defined by XjðsÞ ¼ XðsjÞ. In other words, the
collection fXjgn
j¼1 consists of independent random variables in that the joint p.d.f.,
f ðx1; x2; . . . ; xnÞ, satisfies (7.76), and each component random variable has the same
probability density function as X. When n ¼ y, the terminology that fXjgy
j¼1 are inde-
pendent and identically distributed (i.i.d.) random variables means that this is true of
fXjgn
j¼1 for any n.
2. The terminology that fxjgn
j¼1 is a random sample from X of size n means that there
is an s ¼ ðs1; s2; . . . ; snÞ A S n, selected according to the probability measure Pn on S n so
that ðx1; x2; . . . ; xnÞ ¼ ðXðs1Þ; Xðs2Þ; . . . ; XðsnÞÞ. In practice, this sample can be gener-
ated iteratively by first selecting independent fsjgn
j¼1 HS (see section 7.7 on generating
random samples), and defining ðx1; x2; . . . ; xnÞ as above.
Remark 7.46
It is standard notation in probability theory that a capital letter is used
for the a random variable, such as X, while a lowercase letter, such as x, is used to rep-
resent a realization, or sample point, of the random variable selected according to the
probabilities implied by the probability density function of X. Also note that the equiv-
alence of the approaches to a random sample in 2 of definition 7.45 above is due to the
probability measure Pn satisfying (7.7).
Sample Mean
If fXjgn
j¼1 are n independent and identically distributed (i.i.d.) random variables on
S, the sample mean, denoted ^X, is a random variable ^X : S n ! R defined by
^X 1 1
n
X
n
j¼1
Xj;
ð7:77Þ
with probability density function given by f ðx1; x2; . . . ; xnÞ ¼ Qn
j¼1 f ðxjÞ, where
f ðxÞ is the p.d.f. of X.
When a specific sample is drawn or observed, that is, when fXjgn
j¼1 ¼ fxjgn
j¼1, the
application of (7.77) to these data yields the numerical value denoted ^m or m in sec-
tion 3.3.2.
280
Chapter 7
Discrete Probability Theory

The distinction here is the explicit recognition that any such observation fxjgn
j¼1 is
simply based on one sample point in the sample space S n, and that in more general
terms, the calculation produces not a single and unique numerical value but only one
of many possible values that the random variable ^X assumes on this sample space.
Considered as a random variable, it is natural to inquire into its moments, as we do
next.
Mean of the Sample Mean
By definition, we have that
E½ ^X ¼
X
ðx1;x2;...;xnÞ
1
n
X
n
j¼1
xj
 
!
f ðx1; x2; . . . ; xnÞ:
This formula simplifies using (7.76) and the observation that for any xj,
X
ðx1;x2;...;xnÞ
xj
Y
n
k¼1
f ðxkÞ ¼
X
xj
xjf ðxjÞ ¼ E½X;
since P
xk f ðxkÞ ¼ 1 for k 0 j. Combining, we get that
E½ ^X ¼ E½X;
ð7:78Þ
provided that E½X exists. In other words, the expected value of the sample mean is
the expected value of the original random variable X.
Variance of the Sample Mean
Denoting E½X by m, we have that
Var½ ^X ¼ E½ð ^X  mÞ2
¼
X
ðx1;x2;...;xnÞ
1
n
X
n
j¼1
ðxj  mÞ
 
!2
f ðx1; x2; . . . ; xnÞ:
Again using (7.76), we get
Var½ ^X ¼ 1
n2
X
n
j¼1
ðxj  mÞ2f ðxjÞ
"
#
¼ s2
n :
This result is due to the fact that the mixed terms such as ðxj  mÞðxk  mÞf ðxjÞf ðxkÞ,
with j 0 k, have expectation of 0, since the summations can be done sequentially.
7.5
Expectations of Discrete Distributions
281

Summarizing, we get
Var½ ^X ¼ s2
X
n ;
ð7:79Þ
provided that s2
X exists, and correspondingly
s:d:½ ^X ¼ sXffiffin
p :
ð7:80Þ
m.g.f. of Sample Mean
Noting that et ^
X ¼ Qn
j¼1 etXj=n, and applying the same
method as above, we get that
M ^
XðtÞ ¼ MX
t
n
 

n
;
ð7:81Þ
provided that MX
t
n
 
exists.
Sample Variance
If fXjgn
j¼1 are n independent and identically distributed (i.i.d.) random variables on
S, the unbiased sample variance is defined as
^V ¼
1
n  1
X
n
j¼1
ðXj  ^XÞ2;
ð7:82Þ
where ^X ¼ 1
n
Pn
j¼1 Xj. ^V is again a random variable ^V : S n ! R with a probability
density function given by f ðx1; x2; . . . ; xnÞ ¼ Qn
j¼1 f ðxjÞ, where f ðxÞ is the p.d.f. of
X. Note that the sample variance is defined with the sample mean ^X, and not the
theoretical mean m. As we will see, this is the reason that it is necessary to use
1
n1 in
the formula above rather than the more natural value of 1
n .
As was the case for the sample mean ^X, when a specific sample is drawn or
observed—that is, when fXjgn
j¼1 ¼ fxjgn
j¼1—the application of (7.82) to these data
yields the numerical value denoted ^s2 or s2 in section 3.3.2, there defined with n  1
rather than n. However, once again the perspective here is that any such observation
fxjgn
j¼1 is simply one sample point in the sample space S n, and that in more general
terms, the calculation produces not a single and unique numerical value but only one
of many possible values that the random variable ^V assumes on this sample space.
Considered as a random variable, it is natural to inquire into its moments, as we do
next.
282
Chapter 7
Discrete Probability Theory

Mean of Sample Variance
The calculation of E½ ^V is complicated by the fact that
the random variables appear in two places in the squared terms, explicitly in the Xj
terms, and implicitly in the ^X term. A simple trick is to write Xj  ^X ¼ ðXj  mÞ 
ð ^X  mÞ and ^X  m ¼ 1
n
Pn
k¼1ðXk  mÞ, from which we get
ðXj  ^XÞ2 ¼ ðXj  mÞ2  2ðXj  mÞð ^X  mÞ þ ð ^X  mÞ2
¼ ðXj  mÞ2  2
n
X
n
k¼1
½ðXj  mÞðXk  mÞ þ 1
n2
X
n
i¼1
X
n
k¼1
½ðXi  mÞðXk  mÞ:
Summed over j, the second and third term then combine, producing
X
n
j¼1
ðXj  ^XÞ2 ¼
X
n
j¼1
ðXj  mÞ2  1
n
X
n
i¼1
X
n
k¼1
½ðXi  mÞðXk  mÞ:
Assuming that s2 exists, and taking expectations, we get
E
X
n
j¼1
ðXj  ^XÞ2
"
#
¼ ðn  1Þs2;
since the expectation of mixed terms in the double sum, when i 0 k, is 0 because of
independence. This identity is equivalent to
E½ ^V ¼ s2:
ð7:83Þ
It is this identity that motivates the use of the term ‘‘unbiased’’ for the sample vari-
ance formula given above. It is unbiased in the sense that the expected value of this
statistic is the theoretical value of what is being estimated. In that sense, from (7.78)
it is also the case that ^X is an unbiased estimator of the theoretical mean m 1 E½X,
but this formula is never called the unbiased sample mean.
It is easy to check that if the theoretical mean, m, is known and the sample variance
defined as in (7.82) but with m rather than ^X, then the correct coe‰cient in (7.82)
would be 1
n , in that with this coe‰cient (7.83) would again be derived. But in most
applications this is not relevant since sampling implies limited knowledge of the the-
oretical distribution and its theoretical moments, so it may be illogical to assume that
m is known.
Remark 7.47
As it turns out, there is another calculation of sample variance that uses
1
n in its formulation rather than
1
n1 , and yet also uses ^X. This particular formulation is
7.5
Expectations of Discrete Distributions
283

known as the maximum likelihood estimator of the sample variance, and since the no-
tation is not standardized, we use
^s2
MLE ¼ 1
n
X
n
j¼1
ðxj  ^XÞ2;
ð7:84Þ
where ^X ¼ 1
n
Pn
j¼1 xj. By the analysis above, if this version of a sample variance is
defined as a random variable on S n analogously to ^V, it is biased on the small side, in
that
E½^s2
MLE ¼ n  1
n
s2:
ð7:85Þ
The idea behind the MLE calculation is way ahead of our mathematical development,
but it can be presented in an intuitive way. Assume that a sample has been drawn or
observed, fxjgn
j¼1, and for various reasons we believe a particular form for the p.d.f. of
the observed random variable, f ðxÞ. In this case as in many, the assumed p.d.f. is that
of the normal distribution, which is formally introduced in chapter 8 and studied in
chapter 10. This distribution will be seen to be characterized by only two moments, m
and s2. The question is then, given this assumed distribution, what estimates for m and
s2 will maximize the probability of the observed sample? In other words, What esti-
mates for m and s2 will maximize the likelihood of observing the given sample?
Since the sample p.d.f. is f ðx1; x2; . . . ; xnÞ ¼ Qn
j¼1 f ðxjÞ, as seen in (7.76), and f ðxÞ
only depends on m and s2, this question reduces to determining the values of these
parameters that maximize Qn
j¼1 f ðxjÞ, the probability of the sample point ðx1; x2; . . . ;
xnÞ under this distributional assumption. This function to be maximized is actually a
function of the parameters m and s2, since the sample point ðx1; x2; . . . ; xnÞ is fixed
and known. Determining the maximum value of a function is an application of calculus
and will be seen in chapter 9 for one variable functions, while this particular application
with two variables requires multivariate calculus. As it turns out, the MLE estimators
for m and s2 are ^X and ^s2
MLE.
Variance of Sample Variance
Because of (7.83) the needed calculation is that of
Var½ ^V ¼ E½ð^s2  s2Þ2, which involves some messy algebra and some determination
on the part of the analyst. To make this calculation reasonably tractable, we use the
approach in (7.45) that variance equals the second moment less the mean squared,
which becomes Var½ ^V ¼ E½ ^V 2  ðE½ ^VÞ2 ¼ E½ ^V 2  s4. From the algebra in the
derivation of the mean of the sample variance, recall that
284
Chapter 7
Discrete Probability Theory

ðn  1Þ ^V ¼
X
n
j¼1
ðXj  ^XÞ2 ¼
X
n
j¼1
Y 2
j  1
n
X
n
i¼1
X
n
k¼1
YiYk;
where we simplify notation with Yj ¼ Xj  m. The key is that E½Yj ¼ 0, and so in
any expression in which there is at least one Yj term to the first power, the expecta-
tion will be zero and can be ignored.
This expression squared, which equals ðn  1Þ2 ^V 2, is then
X
n
j¼1
ðXj  ^XÞ2
"
#2
¼
X
n
j¼1
Y 2
j
"
#2
 2
n
X
n
j¼1
Y 2
j
X
n
i¼1
X
n
k¼1
YiYk þ 1
n2
X
n
i¼1
X
n
k¼1
YiYk
"
#2
:
While initially ominous looking, we are only interested in determining how many
terms of each ‘‘type’’ there are. For example, the squared first expression produces a
sum of Y 2
j Y 2
k terms, which fall into two types: one if j ¼ k and another if j 0 k. Any
term of the first type has expectation m4, the fourth central moment of X, and any of
the second type have expectation m2
2 ¼ s4.
Using the combinatorics discussed earlier, we have n terms of the first type and
nðn  1Þ of the second, since every j can be paired with ðn  1Þ-ks. Hence the first
expression becomes
E
X
n
j¼1
Y 2
j
"
#2
¼ nm4 þ nðn  1Þs4:
The second expression produces four types of terms:
Y 4
j ;
Y 3
j Yi;
Y 2
j Y 2
k ;
Y 2
j YiYk;
where the subscripts are meant to di¤er. These terms have expectations of m4, 0, s4,
and 0, respectively, since E½Yk ¼ 0. The challenge is then counting the types, and all
we are concerned with is the first and third type. Again, we draw on combinatorics
and determine that there are n of the first type and nðn  1Þ of the third. Combined,
the second expression becomes
E  2
n
X
n
j¼1
Y 2
j
X
n
i¼1
X
n
k¼1
YiYk
"
#
¼ 2m4  2ðn  1Þs4:
The third expression produces five di¤erent types of terms, the four above and
YiYjYkYl. Of these five, we only need to evaluate the first and third, since all others
7.5
Expectations of Discrete Distributions
285

have expectation of 0. Again, there are n of the first type, but for the third, the com-
binatorics for this expression are di¤erent. First o¤, ½Pn
i¼1
Pn
k¼1 YiYk2 ¼ ½Pn
i¼1 Yi4,
and from the multinomial formula in (7.19), the coe‰cient of every Y 2
j Y 2
k term is
4!
2!2! ¼ 6, and as there are nðn1Þ
2
di¤erent such terms with j 0 k, the total count is
3nðn  1Þ. Combining produces the third expression:
E
1
n2
X
n
i¼1
X
n
k¼1
YiYk
"
#2
2
4
3
5 ¼ 1
n m4 þ 3ðn  1Þ
n
s4:
Finally, the three expressions are combined to
E
X
n
j¼1
ðXj  ^XÞ2
"
#2
2
4
3
5 ¼ nm4 þ nðn  1Þs4  2m4  2ðn  1Þs4 þ 1
n m4 þ 3ðn  1Þ
n
s4
¼
n  2 þ 1
n


m4 þ ðn  2Þðn  1Þ þ 3ðn  1Þ
n


s4:
Dividing by ðn  1Þ2 produces E½ ^V 2, and subtracting ðE½ ^VÞ2 ¼ s4 gives the final
result:
Var½ ^V ¼ 1
n m4 
n  3
nðn  1Þ s4;
ð7:86Þ
as well as the associated result for ^s2
MLE, interpreted as a random variable, by multi-
plying (7.86) by ðn1Þ2
n2
:
Var½^s2
MLE ¼ ðn  1Þ2
n3
m4  ðn  1Þðn  3Þ
n3
s4:
ð7:87Þ
Other Sample Moments
Higher Order Moments
Due to the messiness of estimating the central moments, as
observed for the estimates above related to the sample variance, we focus on esti-
mates of the moments m0
k. Given an independent and identically distributed sample
fXjgn
j¼1, the general higher sample moment estimation formula is
^m0
k ¼ 1
n
X
n
j¼1
X k
j :
ð7:88Þ
The derivations of the following are assigned in exercise 13:
286
Chapter 7
Discrete Probability Theory

E½ ^m0
k ¼ m0
k;
ð7:89aÞ
Var½ ^m0
k ¼ 1
n ½m0
2k  ðm0
kÞ2;
ð7:89bÞ
provided that m0
k and m0
2k exist.
Remark 7.48
The identities in exercise 12 between theoretical moments fm0
kg and
fmkg do not apply in the context of sample moments because, in that context, mk is typ-
ically defined relative to the sample mean ^X and not the theoretical mean m. These for-
mulas do apply if central moments are defined relative to the theoretical mean m, but
this is impractical in most circumstances, as noted above.
Moment-Generating Function
Given an independent and identically distributed
sample fXjgn
j¼1, the sample moment-generating function estimation formula is
^
MXðtÞ ¼ 1
n
X
n
j¼1
etXj:
ð7:90Þ
The function ^
MXðtÞ can be interpreted as a random variable on S n for each t.
In exercise 34 are assigned the following:
E½ ^
MXðtÞ ¼ MXðtÞ;
ð7:91aÞ
Var½ ^
MXðtÞ ¼ 1
n ½MXð2tÞ  M 2
XðtÞ:
ð7:91bÞ
These functions are interpreted as valid for each t, provided that MXðtÞ and MXð2tÞ
exist.
7.6
Discrete Probability Density Functions
Clearly, a random variable X conveys some but not all of the information about a
sample space S, its complete collection of events E, and associated probability mea-
sure Pr, and it transfers this information to a collection of real numbers fxjg in the
range of the random variable. In particular, a random variable allows us to think of
the values in the range of X as ‘‘occurring’’ with certain probabilities. This is a good
way to proceed for mathematical analysis because we can then study probability den-
sity functions and their properties objectively without having to reference the context
of the original sample space or defining random variable. Indeed it is common to use
7.6
Discrete Probability Density Functions
287

a generic random variable X to define a given p.d.f., without reference to the defining
sample space or events or to the functional form of X, in order to provide an objec-
tive language for investigating the properties of f ðxÞ.
However, it is important to remember that the number xj occurs with probability
f ðxjÞ not in isolation but because the event defined by X 1ðxjÞ A E occurs with prob-
ability Pr½X 1ðxjÞ in a given sample space S.
In this section we list several of the most common examples of discrete p.d.f.s. Of
course, there are infinitely many possible probability functions. In the finite case, if
fxjgn
j¼1 H R and ffjgn
j¼1 is any collection of real numbers, then one can define a
p.d.f. by
f ðxjÞ ¼
j fjj
Pn
k¼1 j fkj :
In the countably infinite case, if fxjgy
j¼1 H R and ffjgy
j¼1 A l1 as defined in chapter
6, then a p.d.f. can analogously be defined by
f ðxjÞ ¼
j fjj
Py
k¼1 j fkj :
Consequently any l1-sequence can be used to define a p.d.f. in a countably infinite
context. Of course, we use j fjj to ensure that f ðxjÞ b 0 for all j. In either the finite
or countable case, the associated c.d.f.s are then defined by (7.22).
While these general constructions are useful to exemplify the range of potential
p.d.f.s and some of their properties, there is a far more limited number of examples
found in common practice.
7.6.1
Discrete Rectangular Distribution
The simplest probability density that can be imagined is one that assumes the same
value on every sample point. The domain of this distribution is arbitrary but is con-
ventionally taken as
j
n
n on
j¼1 or
j
nþ1
n
on
j¼0, so in either case Dmn½ f ðxÞ H ½0; 1, where
‘‘Dmn’’ denotes the domain of the function as in definition 2.23. Rather than present
two sets of formulas, we focus on the former definition and leave it as a general exer-
cise to translate these to the latter setting if needed.
For a given n, the p.d.f. of the discrete rectangular distribution, sometimes called
the discrete uniform distribution, is defined on
j
n
n on
j¼1 by
f R
j
n
 
¼ 1
n ;
j ¼ 1; 2; . . . ; n:
ð7:92Þ
288
Chapter 7
Discrete Probability Theory

It is a relatively easy calculation to derive the mean and variance of this distribu-
tion, using the formulas
X
n
j¼1
j ¼ nðn þ 1Þ
2
;
X
n
j¼1
j2 ¼ nðn þ 1Þð2n þ 1Þ
6
;
which can be easily proved by mathematical induction. Implementing the necessary
algebra, we derive
mR ¼ n þ 1
2n ;
ð7:93aÞ
s2
R ¼ n2  1
12n2 :
ð7:93bÞ
Similarly the moment-generating function can be calculated as the sum of a geomet-
ric series, since 1
n
Pn
j¼1 e jt=n ¼ 1
n
Pn
j¼1ðet=nÞ j, producing
MRðtÞ ¼ e½1þð1=nÞt  et=n
nðet=n  1Þ
:
ð7:94Þ
It is apparent from (7.93) that as n ! y, mR ! 1
2 and s2
R ! 1
12 . Less apparent is
what happens in the limit for the moment-generating function, due to the denomina-
tor, as it is clear that the numerator approaches et  1. For the denominator we once
again use the series expression for the exponential, to be proved in chapter 9, that
et=n ¼ Py
j¼0
t
n
  j 1
j! . From this the denominator is seen to equal t þ hnðtÞ
n , where hnðtÞ
is bounded as n ! y, so this denominator is seen to approach t. Hence as n ! y,
MRðtÞ ! e t1
t . As will be seen in chapter 10, these limiting values are the correspond-
ing expressions for the continuous counterpart to the rectangular distribution defined
on ½0; 1.
One of the most important applications of this distribution will be to the problem
of generating random samples from other distributions, a problem that is addressed
in section 7.7 below.
This distribution can also be defined on an arbitrary closed interval ½a; b, general-
izing the model above defined on ½0; 1. The probability density is now defined on
7.6
Discrete Probability Density Functions
289

a þ ðb  aÞ j
n
n
on
j¼1 with values as in (7.92), and from (7.55) and (7.56) or directly we
obtain
mRa; b ¼ n  1
2n a þ n þ 1
2n b;
ð7:95aÞ
s2
Ra; b ¼ ðb  aÞ2 n2  1
12n2 :
ð7:95bÞ
Limits as n ! y are then mRa; b ¼ aþb
2 and s2
Ra; b ¼ ðbaÞ2
12
.
7.6.2
Binomial Distribution
For a given p, 0 < p < 1, the standard binomial random variable is defined as
X B
1 : S ! f0; 1g, where the associated p.d.f. is defined on f0; 1g by f ð1Þ ¼ p,
f ð0Þ ¼ p0 1 1  p. This is often economically expressed as
X B
1 ¼
1;
Pr ¼ p,
0;
Pr ¼ p0,

or to emphasize the associated p.d.f.,
f ðX B
1 Þ ¼
p;
X B
1 ¼ 1,
p0;
X B
1 ¼ 0.

ð7:96Þ
A simple application for this random variable is the single coin flip so that S ¼
fH; Tg, and where a probability measure has been defined on S by PrðHÞ ¼ p and
PrðTÞ ¼ p0 so that X B
1 ðHÞ 1 1 and X B
1 ðTÞ 1 0. This random variable is sometimes
referred to as a Bernoulli trial, and the associated c.d.f. as the Bernoulli distribution,
after Jakob Bernoulli (1654–1705).
This standard formulation is then easily transformed to a shifted standard binomial
random variable: Y B
1 ¼ b þ ða  bÞX B
1 , which is defined as
Y B
1 ¼
a;
Pr ¼ p,
b;
Pr ¼ p0,

where the example of a ¼ 1, b ¼ 1, is common in discrete stock price modeling.
Similarly this model can be extended to accommodate sample spaces of n-coin
flips, producing the general binomial random variable, which now has two parame-
ters, p and n A N. That is, S ¼ fðF1F2 . . . FnÞ j all Fj ¼ H or Tg, and X B
n is defined
as the ‘‘head-counting’’ random variable:
290
Chapter 7
Discrete Probability Theory

X B
n ðF1F2 . . . FnÞ ¼
X
n
j¼1
X B
1 ðFjÞ:
It is apparent that X B
n assumes values 0; 1; 2; . . . ; n, and that using the combinatorial
analysis above, the associated probabilities are given by
X B
n ¼
j; Pr ¼
n
j


p jð1  pÞnj;
j ¼ 0; 1; . . . ; n;

or to emphasize the associated p.d.f.,
f Bð jÞ ¼
n
j


p jð1  pÞnj;
j ¼ 0; 1; . . . ; n:
ð7:97Þ
To derive these probabilities, we observe that if ðF1F2 . . . FnÞ A S is any sample
point with j Hs, then PrðF1F2 . . . FnÞ ¼ p jð1  pÞnj. Moreover, for any j, there are
n
j
 	
such sample points. Consequently the event ½X B
n 1ðjÞ in E has probability as
given in (7.97). Of course, Pn
j¼0 f BðjÞ ¼ 1 by the binomial theorem in (7.15) with
a ¼ p and b ¼ p0, since then a þ b ¼ 1.
Finally, the mean, variance and moment-generating function of f Bð jÞ are easier to
handle using the fact, as was seen above, that X B
n ¼ Pn
j¼1 X B
1j , where fX B
1j g are n in-
dependent, identically distributed standard binomials. For the standard binomial we
readily obtain
mB ¼ p;
s2
B ¼ pq;
MBðtÞ ¼ pet þ q:
ð7:98Þ
Using the method of independent sums as seen in section 7.5.1 above on moments,
also summarized in (7.38), (7.57), and (7.69), produces for any n the moments of the
general binomial:
mB ¼ np;
s2
B ¼ npq;
MBðtÞ ¼ ðpet þ qÞn:
ð7:99Þ
Note that the formulas in (7.99) at first appear inconsistent with those from the
preceding section on the sample mean. This is because here we are working with
a simple summation, while the earlier analysis was applied to the average of a
summation.
It is sometimes necessary to be able to determine the mode of this distribution,
defined as the value of j for which f Bð jÞ is maximized, and which we denote by ^j.
We now show that the mode is any integer that satisfies
pðn þ 1Þ  1 a ^j a pðn þ 1Þ;
ð7:100Þ
7.6
Discrete Probability Density Functions
291

so in general, it is possible to have two modes, and this occurs only when pðn þ 1Þ is
an integer. Otherwise, ^j is unique.
This result is derived from the identity
fBð j þ 1Þ ¼
pðn  jÞ
ð1  pÞð j þ 1Þ fBð jÞ:
From this formula it is apparent that fBðj þ 1Þ b fBðjÞ if and only if
pðn jÞ
ð1pÞð jþ1Þ b 1.
A bit of algebra produces that this occurs when j a pðn þ 1Þ  1. In other words, the
last j for which fBðj þ 1Þ b fBð jÞ, and the value of j that maximizes fBðj þ 1Þ satis-
fies j a pðn þ 1Þ  1. From that point forward these probabilities begin to decrease.
So the mode must satisfy ^j ¼ j þ 1, and from this analysis we conclude that
^j a pðn þ 1Þ.
Now, if ^j  1 ¼ pðn þ 1Þ  1 is an integer, then this coe‰cient ratio is exactly
1. Hence fBð ^j  1Þ ¼ fBð ^jÞ, and the binomial has two modes, one at each of
pðn þ 1Þ  1 and pðn þ 1Þ.
7.6.3
Geometric Distribution
For a given p, 0 < p < 1, the geometric distribution is defined on the nonnegative
integers, and its p.d.f. is given by
f Gð jÞ ¼ pð1  pÞ j;
j ¼ 0; 1; 2; . . . :
ð7:101Þ
This distribution is related to the standard binomial distribution in a natural way.
The underlying sample space can be envisioned as the collection of all coin-flip
sequences that terminate on the first H. So
S ¼ fH; TH; TTH; TTTH; . . .g;
and the random variable X is defined as the number of flips before the first H. Con-
sequently f GðjÞ above is the probability in S of the sequence of j-Ts and then 1-H,
that is, the probability that the first H occurs after j-Ts.
Remark 7.49
The geometric distribution is sometimes parametrized as
f G 0ð jÞ ¼ pð1  pÞ j1;
j ¼ 1; 2; . . . ;
and then represents the probability of the first head in a coin flip sequence appearing
on flip j. These representations are conceptually equivalent, but mathematically distinct
due to the shift in domain. The result is that the moments for f G 0ðjÞ di¤er from those
of f Gð jÞ in that for m b 1,
292
Chapter 7
Discrete Probability Theory

m0
mð f GÞ ¼ ð1  pÞm0
mðf G 0Þ;
although coincidentally the variance remains the same.
Note that Py
j¼0 f GðjÞ ¼ 1 as this geometric series can be summed with the meth-
ods of chapter 6. That is,
X
y
j¼0
ð1  pÞ j ¼ 1
p :
The mean, variance, and moment-generating function of the geometric distribu-
tion can be calculated using various approaches, but the easiest of these to derive,
surprisingly, is the m.g.f. as this is just another geometric series. Specifically:
MGðtÞ ¼ p
X
y
j¼0
ð1  pÞ je jt ¼ p
X
y
j¼0
½ð1  pÞet j;
which is convergent by the ratio test if ð1  pÞet < 1. Using the usual geometric se-
ries approach, we obtain
MGðtÞ ¼
p
1  ð1  pÞet :
ð7:102Þ
The mean and variance can be derived from this expression with a bit of calculus
from chapter 9 using (7.65), or directly (see exercise 15). This produces, with p0 1
1  p,
mG ¼ p0
p ;
s2
G ¼ p0
p2 :
ð7:103Þ
7.6.4
Multinomial Distribution
The multinomial distribution reflects the combinatorial analysis in section 7.3.2
above for general orderings with r-subset types. For given fpjgr
j¼1, 0 < pj < 1 with
Pr
j¼1 pj ¼ 1, and fixed n A N, the multinomial p.d.f. is defined on every integer r-
tuple, ðn1; n2; . . . ; nrÞ, with 0 a nj and P nj ¼ n, by
f Mðn1; n2; . . . ; nrÞ ¼ n!pn1
1 pn2
2 . . . pnr
r
n1!n2! . . . nr! :
ð7:104Þ
7.6
Discrete Probability Density Functions
293

There are several intuitive models for this distribution. One can imagine that at
target practice, a girl scout with n arrows is shooting down-field at r  1 targets of
di¤erent sizes, and has probability pj of hitting the jth target, and probability pr ¼
1  Pr1
j¼1 pj of missing them all. The sample space is the collection of all r-tuples of
results, where each nj denotes the number of arrows hitting the respective target
(where j ¼ r denotes hitting the ground).
An alternative model can be achieved with the binomial model in (7.97). Now
imagine that N sequences of n coin flips are to be generated. The question becomes,
how many of these sequences will end up in each of the r 1 n þ 1 ‘‘head-count buck-
ets’’ implied by this model? Better said, for any nonnegative ðn þ 1Þ-tuple: ðN0; N1;
N2; . . . ; NnÞ with P Nj ¼ N, what is the probability that exactly Nj sequences will
have j-Hs for all j? In this application the probability of ending up in the j-heads
bucket is given by pj ¼
n
j
 	
p jð1  pÞnj, j ¼ 0; 1; . . . ; n.
In either sample space interpretation, we develop the p.d.f. formula in (7.104)
using the same approach as for the binomial. For any r-tuple, ðn1; n2; . . . ; nrÞ, the
probability of any specific such sequence is pn1
1 pn2
2 . . . pnr
r . We now need to count
how many of the sample points in the sample space have exactly this cell count.
From section 7.3.2 on general orderings with r-subset types, the number is
n!
n1!n2!...nr! ,
so the probability of the event defined by having exactly this many of each type is the
product of this count factor with the probability above, which is formula (7.104).
Note that
X
n1;n2;...;nr
f Mðn1; n2; . . . ; nrÞ ¼ 1;
by the multinomial theorem in (7.19), since Pr
j¼1 pj ¼ 1; hence ½Pr
j¼1 pjn ¼ 1.
It is not di‰cult to show that if ðN1; N2; . . . ; NrÞ is multinomial, with parameters
fpjgr
j¼1 and n, then each of the variables Nj has a binomial distribution. For exam-
ple, calculating the marginal density of N1, we have
f ðn1Þ ¼
X
n2;...;nr
n!pn1
1 pn2
2 . . . pnr
r
n1!n2! . . . nr!
¼
n!pn1
1
ðn  n1Þ!n1!
X
n2;...;nr
ðn  n1Þ!pn2
2 . . . pnr
r
n2! . . . nr!
;
where this summation is over all ðr  1Þ-tuples, ðn2; . . . ; nrÞ, with Pr
j¼2 nj ¼ n  n1.
Now this summation has exactly the structure of a multinomial distribution, with
294
Chapter 7
Discrete Probability Theory

parameters fpjgr
j¼2 and n  n1 ¼ Pr
j¼2 nj, but it cannot add up to 1 by the multi-
nomial theorem because Pr
j¼2 pj ¼ 1  p1 0 1. This can be fixed by dividing each
such pj by 1  p1, so the summation is identically 1. Fixing this division outside the
summation proceeds as follows:
f ðn1Þ ¼ n!pn1
1 ð1  p1Þnn1
ðn  n1Þ!n1!
X
n2;...;nr
ðn  n1Þ!
p2
1p1

	n2 . . .
pr
1p1

	nr
n2! . . . nr!
¼
n
n1


pn1
1 ð1  p1Þnn1;
which is the binomial density with parameters n and p1. Consequently we know that
every variable is similarly binomial, and by (7.99),
E½Nj ¼ njpj;
Var½Nj ¼ njpjð1  pjÞ:
ð7:105Þ
In the same way the marginal density of any group of distinct variables can be
shown to be multinomial. For example, with two variables,
f ðn1; n2Þ ¼
X
n3;...;nr
n!pn1
1 pn2
2 . . . pnr
r
n1!n2! . . . nr!
¼ n!pn1
1 pn2
2 ð1  p1  p2Þnn1n2
n1!n2!

X
n2;...;nr
ðn  n1  n2Þ!
p3
1p1p2

	n3 . . .
pr
1p1p2

	nr
n3! . . . nr!
¼ n!pn1
1 pn2
2 ð1  p1  p2Þnn1n2
n1!n2!ðn  n1  n2Þ!
:
This is a multinomial with parameters fp1; p2; 1  p1  p2g and n. A similar formula
is derived for f ðni; njÞ, i 0 j. This joint p.d.f. is used in exercise 35 to derive the cal-
culation that
Cov½Ni; Nj ¼ npipj:
ð7:106Þ
Finally, the moment-generating function of the multinomial distribution can be
easily derived with the help of the multinomial theorem in (7.19). Using the definition
7.6
Discrete Probability Density Functions
295

in (7.68), where as above the summation is over all nonnegative r-tuples, ðn1; n2; . . . ;
nrÞ, with P nj ¼ n, produces
MMðtÞ ¼
X
ðn1;n2;...;nrÞ
eT niti n!pn1
1 pn2
2 . . . pnr
r
n1!n2! . . . nr!
¼
X
ðn1;n2;...;nrÞ
n!ðp1et1Þn1 . . . ðpretrÞnr
n1!n2! . . . nr!
:
Finally, applying the multinomial theorem, we obtain
MMðtÞ ¼
X
r
j¼1
pjetj
 
!n
:
ð7:107Þ
The characteristic function is derived analogously, using (7.75).
7.6.5
Negative Binomial Distribution
The name of this distribution calls out yet another connection to the binomial dis-
tribution, and here we generalize the idea behind the geometric distribution. There
f Gð jÞ was defined as the probability of j-Ts before the first H. The negative bi-
nomial, f NBð jÞ introduces another parameter, k, and is defined as the probability
of j-Ts before the kth-H. So when k ¼ 1, the negative binomial is the same as the
geometric. With that as an introduction, the p.d.f. is defined with parameters p,
0 < p < 1, and k A N as follows:
f NBð jÞ ¼
j þ k  1
k  1


pkð1  pÞ j;
j ¼ 0; 1; 2; . . . :
ð7:108Þ
This formula can be derived analogously to the geometric by considering in the
sample space of all coin-flip sequences, those that are terminated on the occurrence
of the kth-H. The probability of any such sequence with j-Ts and k-Hs is of course
pkð1  pÞ j. Next we must determine the number of such sequences in the sample
space. First o¤, since every such sequence terminates with an H, there are only the
first j þ k  1 positions that need to be addressed. Each such sequence is then deter-
mined by the placement of the first ðk  1Þ-Hs, and so the total count of these
sequences is
jþk1
k1


. Multiplying the probability and the count, we have (7.108).
As stated above, the negative binomial generalizes the geometric distribution and
reduces to that distribution when the parameter k ¼ 1. This is easily confirmed by
296
Chapter 7
Discrete Probability Theory

comparing (7.108) with k ¼ 1 to (7.101), recalling that
j
0
 
¼ 1 for all j b 0 since
0! 1 1.
Finally,
to
demonstrate
that
Py
j¼0 f NBð jÞ ¼ 1,
which
is
equivalent
to
Py
j¼0
jþk1
k1


ð1  pÞ j ¼ pk, we establish the following proposition. To simplify no-
tation, we define q ¼ 1  p.
Proposition 7.50
For 0 < q < 1 and integer k b 1,
ð1  qÞk ¼
X
y
j¼0
j þ k  1
k  1


q j:
ð7:109Þ
Proof
We demonstrate this by induction, but first we must confirm that the series
on the right of (7.109) actually converges. Defining aj ¼
jþk1
k1


q j, we derive the
absolute value of the ratio of successive terms as
ajþ1
aj


 ¼ j þ k
j þ 1 jqj:
By the ratio test this series converges absolutely for jqj < lim supj!y
jþ1
jþk ¼ 1. As an
absolutely convergent series, we are now able to manipulate the terms freely.
We use an induction proof, and first note that for k ¼ 1, (7.109) reduces to
ð1  qÞ1 ¼ Py
j¼0 q j, which is easily derived as a geometric summation from chapter
6. Next assume that this formula is true for a given k, as well as for k ¼ 1. Then we
have that for k þ 1,
ð1  qÞk1 ¼ ð1  qÞ1ð1  qÞk
¼
X
y
i¼0
qi X
y
j¼0
j þ k  1
k  1


q j
¼
X
y
i¼0
X
y
j¼0
j þ k  1
k  1


q jþi
¼
X
y
l¼0
alql;
where the coe‰cient al is the sum of all the coe‰cients in the prior double sum
for which i þ j ¼ l. So for given l b 0, al ¼ Pl
j¼0
jþk1
k1


, since for each such j there
is a corresponding i ¼ l  j. We finally need to show that al ¼
lþk
k


, as this is the
7.6
Discrete Probability Density Functions
297

appropriate coe‰cient in (7.109) for exponent k þ 1. To do this, we apply (7.16) to
each term with j > 0. We conclude that
X
l
j¼0
j þ k  1
k  1


¼ 1 þ
X
l
j¼1
j þ k
k



j þ k  1
k




¼ 1 þ
X
l
j¼1
j þ k
k



X
l1
j¼0
j þ k
k


¼
l þ k
k


;
as was to be proved.
n
Moments of the negative binomial are di‰cult to develop directly, as could be pre-
dicted from the length of the justification that Py
j¼0 f NBðjÞ ¼ 1. However, like the
geometric distribution, the moment-generating function is easily manageable using
(7.109), as we now demonstrate.
By definition,
M NBðtÞ ¼
X
y
j¼0
j þ k  1
k  1


pkð1  pÞ je jt
¼ pk X
y
j¼0
j þ k  1
k  1


½ð1  pÞet j:
Comparing the summation here with that in (7.109), we see that as long as q 1
ð1  pÞet < 1, it must be the case that Py
j¼0
jþk1
k1


½ð1  pÞet j ¼ ð1  qÞk. Com-
bining, we obtain
MNBðtÞ ¼
p
1  ð1  pÞet

k
:
ð7:110Þ
Using this formula and (7.65) with the tools of chapter 9 produces the following
results, with q 1 1  p:
mNB ¼ kq
p ;
s2
NB ¼ kq
p2 :
ð7:111Þ
298
Chapter 7
Discrete Probability Theory

7.6.6
Poisson Distribution
The Poisson distribution is named for Sime´on-Denis Poisson (1781–1840), who dis-
covered its p.d.f. and its properties. This distribution is characterized by a single pa-
rameter l > 0, and its p.d.f. is defined on the nonnegative integers by
f Pð jÞ ¼ el l j
j! ;
j ¼ 0; 1; 2; . . . :
ð7:112Þ
That Py
j¼0 f PðjÞ ¼ 1 is an immediate application of (7.63), to be proved in chapter
9, since from that formula is produced el ¼ Py
j¼0
l j
j! . Unfortunately, in order to de-
velop other properties, we need to make an assumption of another result that will not
be formally proved until chapter 9.
One important application of the Poisson distribution is that it provides a good ap-
proximation to the binomial distribution when the binomial parameter p is ‘‘small.’’
Specifically, the binomial probabilities in (7.97) can be approximated by the Poisson
probabilities above, with l ¼ np. Then for p small, and n large,
n
j


p jð1  pÞnj F enp ðnpÞ j
j!
:
ð7:113Þ
This approximation was far more useful in pre-computer days, and comes from the
result:
Proposition 7.51
For l ¼ np fixed, then as n ! y, binomial probabilities satisfy
n
j


p jð1  pÞnj ! el l j
j! :
ð7:114Þ
In other words, as n increases and p decreases so that the product np is fixed and equal
to l, each of the probabilities of the binomial distribution will converge to the respective
probabilities of the Poisson distribution.
Proof
First o¤,
n
j


p jð1  pÞnj ¼ nðn  1Þ . . . ðn  j þ 1Þ
j!
l
n
 j
1  l
n

n
1  l
n

j
¼ nðn  1Þ . . . ðn  j þ 1Þ
n j
l j
j!
1  l
n

n
1  l
n

j
:
7.6
Discrete Probability Density Functions
299

Now the second term is fixed and independent of n, and the last is seen to converge
to 1 as n ! y, as the exponent j is fixed. The first term equals the fixed product of
j-terms Q j1
k¼0 1  k
n


, and this product also converges to 1. The major subtlety here,
and one we will not prove until chapter 9, is the result that for any real number l,
we have that
1  l
n

n ! el as n ! y. With that limit assumed, the proposition is
proved.
n
Remark 7.52
The requirement that p be small is typically understood as the condition
that p < 0:1, or by symmetry, p > 0:9, while n large is understood as n b 100 or so.
Another important property of the Poisson distribution is that it is the unique
p.d.f. that characterizes arrivals during a given period of time under reasonable and
frequently encountered assumptions. For example, the model might be one of auto-
mobile arrivals at a stop light or toll booth, telephone calls to a switchboard, internet
searches to a server, radio-active particles to a Geiger counter, insurance claims of
any type (injuries, deaths, automobile accidents, etc.) from a large group of policy-
holders, defaults from a large portfolio of loans or bonds, and so forth.
The required assumptions about such arrivals are that:
1. Arrivals in any interval of time are independent of arrivals in any other distinct
interval of time.
2. For any interval of time of length 1
n , measured in fixed units of time, the probabil-
ity of one arrival is l
n þ k1
n2 as n ! y for some constants l and k1.
3. The probability of two or more arrivals during any one of n intervals of time of
length 1
n can be ignored as n ! y
We now show that under these conditions, if f ð jÞ denotes the probability of j
arrivals during this unit interval of time, then with l defined from assumption 2,
f ð jÞ ¼ f Pð jÞ:
As will be seen below, the parameter l in the Poisson p.d.f. equals mP and hence in
this context the average number of arrivals during one unit of time.
The derivation begins by dividing the unit time interval into n-parts. Then
f ð jÞ ¼ f1ð jÞ, where f1ðjÞ denotes the probability of j-arrivals with at most one ar-
rival in each subinterval, since by assumption 3 we can ignore in the limit the event
that 2 or more arrivals occur in any subinterval. We then have that f1ðjÞ is a general
binomial probability because of the interval independence assumption in 1, and it
equals the probability of one arrival in j-intervals, and none in ðn  jÞ-intervals.
This binomial probability is given in assumption 2. With the appropriate binomial
coe‰cient we obtain
300
Chapter 7
Discrete Probability Theory

f1ð jÞ ¼
n
j

 l
n þ k1
n2

j
1  l
n  k1
n2

nj
:
Using the same approach as in proposition 7.51, we derive that f1ðjÞ ! f PðjÞ as
n ! y. Here, however, we have that p ¼ l
n þ k1
n2 , so np ¼ l þ k1
n , and we require a
generalized version of the above unproved fact that
1  l
n  k1
n2

	n
! el. In other
words, the probability adjustment of k1
n2 is irrelevant in this limit as will be demon-
strated in chapter 9.
Remark 7.53
In many applications l is defined as the average number of arrivals in
a unit of time such as a minute, a month, or a year, depending on the application, and
then the appropriate parameter for a period of length T-units of time is l0 ¼ lT for
any T.
Turning next to expectations, we note that the moment-generating function is
somewhat easier to derive than are the mean and variance. Specifically, MPðtÞ ¼
el Py
j¼0
l j
j! e jt ¼ el Py
j¼0
ðle tÞ j
j!
, where this summation is recognizable from (7.63) as
ele t. Consequently we obtain
MPðtÞ ¼ elðe t1Þ:
ð7:115Þ
The mean and variance of the Poisson can then be derived from the m.g.f. or by a
direct method assigned in exercise 16:
mP ¼ l;
s2
P ¼ l:
ð7:116Þ
7.7
Generating Random Samples
In certain contexts random samples are observed, such as the daily market close
prices, the periodic returns of a given security or investment index, the weekly rain-
fall in a given forest, the height measurements of girls upon their fourteenth birthday,
or the number of hits on a Geiger counter in 30 seconds, or the number of bond
defaults in a year, or the proportion of males just turning 65 years of age that
will survive one year. Indeed the world is full of observations that can be construed
by the observer as representing random sample points from an unknown probability
distribution. The mathematical discipline of statistics concerns itself with the collec-
tion of such data, as well as the analysis and interpretation of these data.
On the other hand, past observations, often with a healthy dose of intuition and
sometimes mathematical convenience, can lead one to assume that a given random
variable of interest is in fact governed by a given probability density function. For
7.7
Generating Random Samples
301

example, an individual bond default or death could logically be assumed to be mod-
eled by a standard binomial distribution, or the number of bond defaults or deaths
perhaps modeled by a general binomial distribution or a Poisson approximation,
while the average of many collections of observed random variables may be assumed
to be normally distributed (see chapter 8). Such distributional assumptions can then
be ‘‘calibrated’’ to observed data by choosing the distribution’s parameters appropri-
ately, or calibrated to characteristics assumed to hold in the future.
Once such a transition is made, from observing a random variable to assuming
that the given random variable is governed by a given p.d.f., it is possible in theory
to generate additional samples that can be studied. Such generated samples are used
for insights that may not be possible based on observable data, often due to the
sparseness of the observations or because one assumes that the p.d.f.s parameters in
the future will di¤er from those underlying past observations.
For example, Chebyshev’s inequality discussed in the next chapter assures that it is
very unlikely to observe a random variable that is far from its mean when measured
in units of standard deviations, but for many applications in finance, it is exactly the
extreme events that are of most interest in the modeling. As another example, a mar-
ket model calibrated during a bear market would need to have parameters modified
to be applicable in a bull market.
So while the assumed p.d.f. has the potential to provide all the details on such ex-
treme and other events neither observed nor perhaps observable, it does so with the
inherent risk to the investigator that in most applications, such a p.d.f., is, after all,
only an assumption. Nature almost never truly reveals underlying p.d.f.s nor prom-
ises to keep the parameters in any p.d.f.s constant. Nature doesn’t even commit to
using p.d.f.s, but in practice, it is convenient to assume such a commitment has
been made, and to be mindful of the inherent risks of such an assumption.
That said, the purpose of this section is to present a very handy result with imme-
diate application to the generation of random samples of the values of any random
variable, given an assumed probability density function. First a definition.
Definition 7.54
A collection frjgn
j¼1 H ½0; 1 is a uniformly distributed random sample
if:
1. For any subinterval ha; bi H ½0; 1, where h i is intended to mean open, closed or
mixed, Pr½rj A ha; bi ¼ b  a.
2. For any collection of subintervals fhaj; bjign
j¼1, haj; bji H ½0; 1 for all j,
Pr½rj A haj; bji for all j ¼
Y
n
j¼1
ðbj  ajÞ:
ð7:117Þ
302
Chapter 7
Discrete Probability Theory

It should be noted that part 1 of definition 7.54 implies that for any given a A ½0; 1,
Pr½r ¼ a ¼ 0. The term ‘‘uniform’’ means that the probabilities governing the loca-
tion of each rj value are proportional to the length of the interval in which such a
value is sought. In addition the use of ‘‘random’’ is identical with that given in (7.9),
where the probability of a joint event equals the product of the probabilities of the
individual events. This is the essence of (7.117).
Remark 7.55
This model can be imagined as the limiting situation for the discrete
uniform p.d.f. as n ! y. This is because as n ! y, while the probabilities of individ-
ual points decrease to 0 under the discrete uniform p.d.f., the total probability of r A
ha; bi approaches b  a. In theory, however, the notion of uniformly distributed ran-
dom sample is intended as a notion of continuous probability theory, as was the case
noted above for the normal distribution. But, in practice, there is little di¤erence be-
tween the uniform distribution above and the discrete uniform distribution for n large.
Indeed all computers work in finite decimal (or binary) point precision, so in a given
application, they are incapable of distinguishing x from x þ 10m for m b M, where
M is generally about 16 or so. So with n b 10M, the discrete uniform and continuous
uniform are identical to your computer.
The result in this section is simply that if frjgn
j¼1 H ½0; 1 is a uniformly distributed
random sample, then fF 1ðrjÞgn
j¼1 ¼ fXjgn
j¼1 will be a random sample of the random
variable X. In other words, fXjgn
j¼1 are independent, identically distributed random
variables in the sense of (7.34). So the problem of generating a random sample for
any discrete random variable can be reduced to the problem of generating a uni-
formly distributed random sample from the interval ½0; 1, which is a problem that is
solved in virtually any mathematical or calculation software.
The inverse distribution function of a discrete random variable, F 1ðrÞ, is defined:
Definition 7.56
Let X be a random variable defined on a discrete sample space S with
range fxjg and cumulative distribution function FðxÞ. Then for r A R,
F 1ðrÞ ¼ minfxj j r a FðxjÞg:
ð7:118Þ
Example 7.57
For simplicity, let X denote the binomial random variable,
f ðxÞ ¼
0:25;
x ¼ 0;
0:75;
x ¼ 1;

with distribution function
7.7
Generating Random Samples
303

FðxÞ ¼
0;
x < 0;
0:25;
0 a x < 1;
1:0;
1 a x:
8
<
:
The graph of FðxÞ is seen in figure 7.2.
From (7.118) the inverse distribution function is defined as
F 1ðrÞ ¼
0;
0 a r a 0:25;
1;
0:25 < r a 1:0:

So, if frjgn
j¼1 is a uniformly distributed sample from the interval ½0; 1, then for any rj,
Pr½rj A ½0; 0:25 ¼ 0:25, and hence Pr½F 1ðrjÞ ¼ 0 ¼ 0:25. Similarly Pr½rj A ð0:25; 1:0
¼ Pr½rj A ½0:25; 1:0 ¼ 0:75. Hence Pr½F 1ðrjÞ ¼ 1 ¼ 0:75.
The proof of a simpler version of the general statement follows identically with this
example, and is presented for completeness. By ‘‘simpler’’ is meant that we assume
that the range of the random variable, which equals the domain of the probability
density function, is sparse, meaning it has no accumulation points. The general state-
ment and proof will then follow.
Proposition 7.58
Let X be a discrete random variable on a sample space S with
sparse range fxjg and distribution function FðxÞ. Then, if frjgn
j¼1 H ½0; 1 is a uni-
formly distributed random sample, fF 1ðrjÞgn
j¼1 is a random sample of X in the sense
of (7.34).
Figure 7.2
Binomial c.d.f.
304
Chapter 7
Discrete Probability Theory

Proof
If the collection fxjg is sparse and hence has no accumulation points, then
enumerating in increasing order, we have that for any rj 0 0 there is a unique xk
so that rj A ðFðxkÞ; Fðxkþ1Þ. Since Pr½rj ¼ 0 ¼ 0, we ignore this case. Now, since
F 1ðrjÞ ¼ xkþ1, we have that by the definition of uniformly distributed sample,
Pr½F 1ðrjÞ ¼ xkþ1 ¼ Pr½rj A ðFðxkÞ; Fðxkþ1Þ ¼ Fðxkþ1Þ  FðxkÞ ¼ f ðxkþ1Þ:
In other words, through F 1, a uniformly distributed sample is transformed into a
collection of outcomes of X with the correct probabilities. To demonstrate indepen-
dence of fF 1ðrjÞgn
j¼1, let any collection fxkjgn
j¼1 be given; then
f ðxk1; xk2; . . . ; xknÞ ¼ Pr½F 1ðr1Þ ¼ xk1; F 1ðr2Þ ¼ xk2; . . . ; F 1ðrnÞ ¼ xkn
¼ Pr½r1 A ðFðxk11Þ; Fðxk1Þ; . . . ; rn A ðFðxkn1Þ; FðxknÞ
¼
Y
n
j¼1
½FðxkjÞ  Fðxkj1Þ
¼
Y
n
j¼1
f ðxkjÞ;
where the third equality comes from the definition of frjgn
j¼1 as a uniformly distrib-
uted random sample.
n
Example 7.59
To generate a random sample of Poisson variables with l ¼ 2, we first
calculate the appropriate half-open intervals for the r-values. Let FðnÞ ¼ Pn
j¼0 e2 2 j
j!
for n ¼ 0; 1; 2; . . . and define the associated half-open intervals: In ¼ ðFðn  1Þ; FðnÞ,
for n ¼ 0; 1; 2; . . . , where we note that Fð1Þ ¼ 0 by definition. Then the length of In
is given by jInj ¼ FðnÞ  Fðn  1Þ ¼ f ðnÞ 1 e2 2 n
n! , and it is clear that Py
j¼0 jIjj ¼
Py
j¼0 f ðnÞ ¼ 1. For any collection frjgn
j¼1 H ½0; 1 generated using common software
such as Randð Þ in Excel, the random sample of Poisson variables fF 1ðrjÞgn
j¼1 are
defined by
F 1ðrjÞ ¼ n
if rj A In:
Note that if the range of the random variable fxjg has accumulation points, the
proof above becomes compromised. For example, imagine a discrete random vari-
able with range equal to the rational numbers in ½0; 1, ordered in some way. In this
case FðxÞ is well defined as in (7.22), but it is no longer true that fxjg can be enu-
merated in increasing order, nor is it true that for any rj 0 0 there is a unique xk so
7.7
Generating Random Samples
305

that rj A ðFðxkÞ; Fðxkþ1Þ. The implication of this observation is not that the conclu-
sion of the proposition above is false in this case, but that a somewhat more subtle
argument is needed to demonstrate its truth.
Proposition 7.60
Let X be a discrete random variable on a sample space S, with
range fxkg, and distribution function FðxÞ. Then, if frjgn
j¼1 H ½0; 1 is a uniformly dis-
tributed random sample, fF 1ðrjÞgn
j¼1 is a random sample of X in the sense of (7.34).
Proof
Let xk be given. As above, our first goal is to show that Pr½F 1ðrjÞ ¼ xk ¼
f ðxkÞ. Consider the half-open interval about xk, defined by In ¼ xk  1
n ; xk þ 1
n


.
Now, by (7.118), for r A ½0; 1, F 1ðrÞ A In if and only if xk  1
n < minfxj j r a FðxjÞg
a xk þ 1
n . That is, F 1ðrÞ A In if and only if,
r A F
xk  1
n


; F
xk þ 1
n




:
So by the definition of uniformly distributed sample,
Pr½F 1ðrÞ A In ¼ F
xk þ 1
n


 F
xk  1
n


¼
X
xk1=n<xjaxkþ1=n
f ðxjÞ:
Finally, as n ! y, Pr½F 1ðrÞ A In ! Pr½F 1ðrÞ ¼ xk, and the summation above
reduces to f ðxkÞ, demonstrating that Pr½F 1ðrjÞ ¼ xk ¼ f ðxkÞ. To demonstrate in-
dependence of fF 1ðrjÞgm
j¼1, let any collection fxkjgm
j¼1 be given, and define Inj as
above for each xkj. Then
f ðxk1; xk2; . . . ; xkmÞ ¼ Pr½F 1ðrjÞ A Inj for all j
¼ Pr rj A
F
xkj  1
n


; F
xkj þ 1
n




for all j


¼
Y
m
j¼1
F
xkj þ 1
n


 F
xkj  1
n




¼
Y
m
j¼1
X
xkj 1=n<xlaxkj þ1=n
f ðxlÞ
2
4
3
5;
306
Chapter 7
Discrete Probability Theory

where the second equality comes from the definition of uniformly distributed sample.
Finally, letting n ! y, we obtain
f ðxk1; xk2; . . . ; xkmÞ ¼
Y
m
j¼1
f ðxkjÞ:
n
7.8
Applications to Finance
7.8.1
Loan Portfolio Defaults and Losses
An example of a combination coin-flip and urn problem in finance that is typically
implemented with computer algorithms is bond or loan default and loss modeling.
Imagine a portfolio of n bonds, all with the same credit rating, say Baa=BBB. As-
sume that the event of a default in a given year is generated by an H-flip of a biased
coin that produces heads, on average, in 75 of 1000 flips. We toss this coin n times,
and record the number of heads; say it is nH. We then go to the portfolio urn of
bonds and select nH bonds without replacement. These are the defaulted bonds in
this trial, and the total par defaulted is denoted FH. From this defaulted portfolio,
losses can be modeled in terms of a fixed loss of lFH, with 0 a l a 1 denoting a fixed
loss ratio, or a loss given default (LGD) model can be implemented whereby losses
vary according to some probability density function.
A simple example of how one might generate nonconstant losses is that with each
defaulted bond, a die is rolled. So one dot represents a loss of 1
6 , or about 16:6% of
par, and so forth to a roll of 6 dots, which represents a loss of 100%. More realisti-
cally one could use a variety of probability density functions calibrated to historic
data, or create a sample space of losses constructed directly from all past defaults.
In the former case, random losses are produced by first generating a uniform random
sample on ½0; 1, then applying the approach of the last section. In the latter model
this historic loss collection would be another urn containing the collection of LGDs
experienced historically in percentage terms. Then with each bond selected from the
original urn for default, an LGD is drawn from this second urn to determine the
associated loss. This second urn would logically be sampled with replacement.
Individual Loss Model
More formally, let fjk denote the loan amount of the jth bond or loan, in risk class k.
Risk classes might be defined in terms of credit ratings for bonds or internal risk as-
sessment criteria for other loans. For each risk class define the default random vari-
able Djk for this loan as a binomial with
7.8
Applications to Finance
307

Djk ¼
1;
Pr ¼ qk,
0;
Pr ¼ 1  qk.

Here the probability of default in the period is denoted qk. The probability of con-
tinued payments during the period is pk ¼ 1  qk.
Note that the random variable Djk will typically not depend on the loan other than
through the risk class, and that the notational device of the subscript j is simply to
confirm that each of the loans in the same risk class will have separate and indepen-
dent coin flips. Notational use of Dk might suggest that all loans in a class default or
do not default together, an unrealistic assumption.
Finally, the loss given default random variable, or loss ratio, for each loan,
denoted Ljk, is again defined only by risk class as a random variable with range in
the interval ½0; 1 and the same notational convention as for Djk. Sometimes the loan
recovery Rjk is modeled, representing the relative amount recovered from a borrower
on default. Of course, Ljk ¼ 1  Rjk.
Total losses can now be notationally represented as the random variable that is
given by the individual loss model:
L ¼
X
j;k
fjkDjkLjk:
ð7:119Þ
For each loan the random variable Djk is generated, and for each loan for which
Djk ¼ 1, the random variable Ljk is generated. Both random variables can be gener-
ated with the methodology of section 7.7 using uniformly distributed random sam-
ples from ½0; 1, since we want the collection fDjkg to be independent random
variables, as well as the collection fLjk j Djk ¼ 1g. Of course, the collections fDjkg
and fLjkg cannot be independent, since Djk ¼ 0 implies that Ljk ¼ 0, although there
is no harm, other than with respect to wasted computational time, of generating
fLjkg for all combinations of jk, and generating these as independent random vari-
ables that are also independent of the collection fDjkg.
Specifically, for fixed k we generate frjkg H ½0; 1, one for each bond, and denoting
by Bk the c.d.f. of the binomial with parameter qk, we have
Djk 1 B1
k ðrjkÞ ¼
1;
rjk a qk;
0;
rjk > qk:

Similarly, from another collection, fr0
jkg H ½0; 1, one for each default, losses are gen-
erated using the assumed loss c.d.f. for each risk class. In other words, Ljk ¼ F 1
k ðr0
jkÞ,
where Fk is the cumulative loss given default distribution function for risk class k.
308
Chapter 7
Discrete Probability Theory

Of course, such values need only be generated for those jk combinations for which
B1
k ðrjkÞ ¼ 1.
From this model one can calculate the mean and variance of losses using the con-
ditional expectation formulas in (7.43) and (7.46). For example, conditioning on the
random variable Djk obtains
E½L ¼
X
j;k
E½ fjkDjkLjk
¼
X
j;k
E½E½ fjkDjkLjk j Djk:
Now
E½ fjkDjkLjk j Djk ¼ 0 ¼ 0
and
E½ fjkDjkLjk j Djk ¼ 1 ¼ fjkE½Ljk ¼ fjkE½Lk,
since fjk is a constant and the loss distribution depends only on the risk class. Said
another way, for each risk class, fLjkg are independent and identically distributed
with c.d.f. Fk. These ‘‘inner’’ conditional expectations can be expressed conveniently
by
E½ fjkDjkLjk j Djk ¼ fjkE½LkDjk:
Consequently, since E½Djk ¼ qk,
E½L ¼
X
j;k
qk fjkE½Lk
ð7:120aÞ
¼
X
k
qk fkE½Lk;
ð7:120bÞ
where fk ¼ P
j fjk, the total loan amount in this risk class.
Variance is similarly calculated with a conditioning approach. With the assump-
tions above regarding the generation of the collections fDjkg and fLjkg, the losses
on bonds are independent random variables. So the variance of the sum is the sum
of the variances, and each of these variances is calculated by conditioning. In other
words,
Var½L ¼
X
j;k
Var½E½ fjkDjkLjk j Djk þ
X
j;k
E½Var½ fjkDjkLjk j Djk:
Now from the conditional expectation for E½ fjkDjkLjk j Djk above, and Var½Djk ¼
qkð1  qkÞ, we get
Var½E½ fjkDjkLjk j Djk ¼ qkð1  qkÞf 2
jkE½Lk2:
7.8
Applications to Finance
309

Next, from Var½ fjkDjkLjk j Djk ¼ 0 ¼ 0 and Var½ fjkDjkLjk j Djk ¼ 1 ¼ f 2
jk Var½Lk, we
conclude that Var½ fjkDjkLjk j Djk ¼ f 2
jk Var½LkDjk. Hence
E½Var½ fjkDjkLjk j Djk ¼ qk f 2
jk Var½Lk:
Combining, we have
Var½L ¼
X
j;k
qkð1  qkÞf 2
jkE½Lk2 þ
X
j;k
qk f 2
jk Var½Lk
ð7:121aÞ
¼
X
k
qkð1  qkÞf ð2Þ
k E½Lk2 þ
X
k
qk f ð2Þ
k
Var½Lk:
ð7:121bÞ
Here we define f ð2Þ
k
¼ P
j f 2
jk, which of course is not the same as f 2
k for fk defined
above in (7.120b). These formulas can be rewritten if desired using Var½Lk ¼
E½L2
k  E½Lk2.
Aggregate Loss Model
If the loan amounts in each risk class are similar and narrowly distributed, loan
losses can also be modeled in what is called an aggregate loss model, or collective
loss model. In each risk class, say class k, the collection of actual loan amounts
f fjkg, which contains nk loans, is modeled as a portfolio of nk loans of the same
amount given by the average fk 1 1
nk
P
j fjk. Total losses can now be expressed as
L ¼
X
j;k
fkDjkLjk ¼
X
k
fk
X
j
DjkLjk:
Note that for each k, Nk 1 P
j Djk is a random variable with a binomial distribu-
tion with parameters nk and qk, and by (7.99) we have E½Nk ¼ nkqk and Var½Nk ¼
nkqkð1  qkÞ. Also P
j DjkLjk can be rewritten as
X
j
DjkLjk ¼
X
Djk00
Ljk
¼ NkL0
k:
Here the random variable L0
k is given by
L0
k ¼ 1
Nk
X
Nk
j¼1
Ljk
for 1 a Nk a nk;
310
Chapter 7
Discrete Probability Theory

and defined as the average loss ratio for class k, conditional on Nk b 1. In other
words, L0
k is the average loss ratio conditional on there being a loss. This is consistent
with the definition of Ljk, which is the loss ratio on loan j in class k given that a loss
occurred, meaning that Djk ¼ 1.
Combining results, we have that in the case of loan amounts that are narrowly dis-
tributed by risk class, the individual loss model can be rewritten as an aggregate loss
model:
L ¼
X
k
fkNkL0
k:
ð7:122Þ
Here Nk has binomial distribution with parameters nk and qk, fk is the average loan
amount in class k, and L0
k is a random variable equal to the average loss ratio in class
k, conditional on Nk b 1.
We will now see that not surprisingly, L0
k has the same expected value as does the
individual loss ratio random variable for class k, which is denoted Lk in the individ-
ual loss model above. On the other hand, L0
k will have a smaller variance than Lk,
intuitively because L0
k is defined in terms of averages of the original fLjkg, whereas
Lk reflects no averaging.
First, E½L0
k can be evaluated using the conditioning argument of (7.43), where
subscripts are put on the expectation operators for clarity:
E½L0
k ¼ EN EL
1
Nk
X
Nk
j¼1
Ljk


Nk ¼ n b 1
"
#
"
#
¼ EN
1
n
X
n
j¼1
E½Lk


n b 1
"
#
¼ E½LkEN½1 j n b 1
¼ E½Lk
X
nk
n¼1
Pr½Nk ¼ n j n b 1:
For the last step, it must be remembered that Nk is a binomial random variable, but
conditional on the restriction that Nk b 1. So here Pr½Nk ¼ n j n b 1 ¼
Pr½Nk¼n
1Pr½Nk¼0 ,
and so Pnk
n¼1 Pr½Nk ¼ n j n b 1 ¼ 1. Consequently
E½L0
k ¼ E½Lk:
ð7:123Þ
7.8
Applications to Finance
311

Next, while L0
k is a random variable with the same mean as Lk for each k fixed, it
has a smaller variance. This is again derived from a conditioning argument in (7.46)
as follows: From the mean calculation above, we have that EL
1
Nk
PNk
j¼1 Ljk j Nk ¼
h
n b 1 ¼ E½Lk, a constant. Consequently the variance of this conditional expectation
is 0.
On the other hand, for the conditional variance,
Var
1
Nk
X
Nk
j¼1
Ljk


Nk ¼ n b 1
"
#
¼ Var 1
n
X
n
j¼1
Ljk
"
#
¼ 1
n2
X
n
j¼1
Var½Ljk
¼ 1
n Var½Lk:
Combining and evaluating the expectation of this conditional variance obtains
Var½L0
k ¼ Var½LkEN
1
Nk


Nk b 1


;
ð7:124Þ
where Nk has binomial distribution with parameters nk and qk, but conditional on
Nk b 1. Apparently E
1
Nk j Nk b 1
h
i
< 1, since by the conditional binomial probabil-
ities, Pr½Nk ¼ n j n b 1 ¼
Pr½Nk¼n
1Pr½Nk¼0 :
E
1
Nk


Nk b 1


¼
X
nk
n¼1
1
n
nk
n

 qn
kð1  qkÞnkn
1  ð1  qkÞnk :
So Var½L0
k < Var½Lk, since the summation is a weighted average Pnk
n¼1
1
n wn where
Pnk
n¼1 wn ¼ 1.
The random variable Nk can also be modeled as Poisson for, in general, the asso-
ciated qk are quite small and satisfy in all but the most extreme cases the condition
qk a 0:1. In this case the Poisson parameter for risk class k is given by lk ¼ nkqk,
and the E
1
Nk j Nk b 1
h
i
calculated accordingly.
The mean and variance of L within the aggregate loss model can again be devel-
oped using the conditioning arguments. In exercise 17 is assigned the derivation of
the following formulas, where E½L0
k is used for notational consistency, but recall
from above that E½L0
k ¼ E½Lk:
312
Chapter 7
Discrete Probability Theory

E½L ¼
X
k
fkE½NkE½L0
k;
ð7:125Þ
Var½L ¼
X
k
f 2
k E½L0
k2 Var½Nk þ
X
k
f 2
k E½N 2
k  Var½L0
k:
ð7:126Þ
Note that in these formulas, E½Nk and Var½Nk reflect the whole distribution of
Nk, and not the conditional distribution reflecting Nk b 1 as was used for the L0
k
moments. Specifically, E½Nk ¼ nkqk whether Nk is modeled as binomial or Poisson,
since for the latter, lk ¼ nkqk. However, Var½Nk will equal nkqkð1  qkÞ with the
binomial, and nkqk with the Poisson approximation. Also, while E½L0
k can be cal-
culated directly from the assumed distribution for Ljk with k fixed, as was derived
above, Var½L0
k will be smaller than Var½Lk, due to the multiplicative factor of
E
1
Nk j Nk b 1
h
i
.
As was the case for the individual loss model, the random variable L can be simu-
lated using (7.122) and the approach in section 7.7 above to generating random sam-
ples from a distribution function. In this formula, for instance, Nk has binomial
distribution with parameters nk and qk, or a Poisson distribution with lk ¼ nkqk. In
either case each simulation for class k involves first generating one uniformly distrib-
uted random variable r A ½0; 1 from which Nk 1 F 1
N ðrÞ, with FNðxÞ denoting the
cumulative distribution for Nk. Then, if Nk > 0, another Nk uniformly distributed
variables are generated, frjgNk
j¼1, from which loss ratios are defined by fLjkgNk
j¼1 ¼
fF 1
Lk ðrjÞgNk
j¼1, with FLkðxÞ the cumulative distribution function for Lk. The average
loss ratio is then L0
k ¼ 1
Nk
PNk
j¼1 Ljk: Each simulation then proceeds the same way.
7.8.2
Insurance Loss Models
With only a change in the definitions of the random variables, the individual and ag-
gregate loss models can be used in a wide variety of insurance claims applications.
For example, within a life insurance claims context, risk classes would typically be
defined at least by age groups, with gender and/or insurance ‘‘ratings’’ classes not un-
common. Life insurance ratings are analogous to credit ratings on loans, only that
here the goal is to identify individuals relative to mortality risk rather than the risk
of default. Consequently, in this application, qk is the probability of death in a pe-
riod, often in a year, and fjk denotes the life insurance policy ‘‘face amount’’ on a
‘‘net amount at risk’’ basis payable on death.
This so-called net amount at risk is an adjustment to the policy face amount that
reflects the fact that for many insurance contracts, particularly those with level pre-
miums paid by the insured, the insurer holds ‘‘reserves’’ backed by accumulated
7.8
Applications to Finance
313

excess premiums. In many policies, while the net exposure amounts vary year to
year, they are not random variables per se. In other words, there is no need for the
random variable Ljk in a traditional life insurance model, since the ‘‘loss’’ on death is
known in advance. When Djk ¼ 1, the entire net policy amount is paid, and hence
Ljk ¼ 1 as well.
It is also of interest to apply these models, and those below, over a multiple-year
modeling horizon, changing model parameters each year. In such an application a
random sequence is generated, and this is a special case of a stochastic process. Also
note that with a multiple-year model, the present value of all losses could be modeled
as a random variable, by introducing appropriate interest rates for discounting.
These future interest rates could be modeled as fixed or as random variables.
For life insurance policies for which the death benefit is not fixed, such as is the
case with variable life insurance, Ljk is once again a random variable. But in this
application Ljk is a ‘‘multiplier’’ applied to the original policy face amount, and it
usually reflects the performance in the financial markets, often with a minimum guar-
antee. It is also natural to allow Ljk > 1 in this model to accommodate favorable
market environments.
These loss models also apply to various types of insurance policies for which the
benefits are not fixed. For example, with a disability insurance policy, qk would be
the probability of disability in a period, again often a year, and the claim paid, sym-
bolically fjkLjk, would be based on a probability distribution that reflects both past
insurer claims patterns and trends, as well as amount limitations defined in the pol-
icy. It would be common practice to model the value of the claim as a present value
of expected payments over the expected disability period. Specifically, fjk could be
modeled as the present value of the maximum claim allowed by the policy, and Ljk
a loss ratio, 0 < Ljk a 1, in the sense above.
Various types of health insurance benefits could be handled similarly, as could var-
ious benefits payable under property and casualty insurance policies, which include
automobile insurance and home-owners or renters insurance.
7.8.3
Insurance Net Premium Calculations
Generalized Geometric and Related Distributions
Recall that the geometric density in (7.101) defined by
f GðjÞ ¼ pð1  pÞ j,
j ¼ 0; 1; 2; . . . , provided the probability that j-Ts precede the first H in a sequence
of binomial trials with Pr½H ¼ p. The negative binomial distribution generalized
this definition in that a new parameter k is introduced, and then f NBðjÞ represented
the probability that j-Ts precede the kth-H in a sequence of binomial trials with
Pr½H ¼ p.
314
Chapter 7
Discrete Probability Theory

Another way of generalizing the geometric distribution is to allow the probability
of a head to vary with the sequential number of the coin flip. Specifically, if
Pr½H j jth flip ¼ pj, then with a simplifying change in notation to exclude the case
j ¼ 0, a generalized geometric distribution can be defined by the p.d.f.
f GGð jÞ ¼ pj
Y
j1
k¼1
ð1  pkÞ;
j ¼ 1; 2; 3; . . . ;
ð7:127Þ
where f GGð jÞ is the probability of the first head appearing on flip j. By convention,
when j ¼ 1, Q0
k¼1ð1  pkÞ ¼ 1.
Of course, as was demonstrated above, if pk ¼ p > 0 for all k, then f GðjÞ is in-
deed a p.d.f. in that Py
j¼0 pð1  pÞ j ¼ 1. With nonconstant probabilities, this conclu-
sion is true but not obvious. Note, however, that if 0 < a a pk a b < 1 for all j, then
the summation is finite, since f GGðjÞ < bð1  aÞ j1 and Py
j¼1 f GGðjÞ < b
a by a geo-
metric series summation.
In addition, letting c0 ¼ 1 and cj ¼ Q j
k¼1ð1  pkÞ for j b 1, we have that
f GGð jÞ ¼ cj1  cj;
and Py
j¼0 cj a Py
j¼0ð1  aÞ j ¼ 1
a . Consequently the alternating series version of this
absolutely convergent series can be rearranged, producing
X
y
j¼1
f GGð jÞ ¼
X
y
j¼1
ðcj1  cjÞ
¼ c0 þ
X
y
j¼1
ðcj  cjÞ
¼ 1:
This probability density function is the essence of a survival model, although the
notation switches from
pk ¼ Pr½H on kth flip j all Ts before kth flip
to
qk ¼ Pr½death in year k j survival for first k  1 years;
where as expected, year 1 extends from time t ¼ 0 to t ¼ 1, and so forth. Conse-
quently this conditional probability can also be expressed qk ¼ Pr½death by time k j
7.8
Applications to Finance
315

alive at time k  1. In practice, for the group being modeled, fqkg 1 fqxþk1g,
where x ¼ current age, and the standard actuarial notation: qxþk1 ¼ Prfperson age
x þ k  1 will die within one yearg. However, to simplify notation, we generally
avoid the age-based notation unless it is needed for emphasis.
This definition of qk may appear odd in that a natural reaction to the condition
‘‘alive at time k  1’’ might well be ‘‘of course, they are alive at the beginning of the
year, as that is what it means to die in year j!’’ But this obvious point is not the pur-
pose of the condition.
Population census data as well as various insurance company and pension plan
data usually present the probabilities of death on the basis of the qk model definition.
That is, among a group of individuals with comparable mortality risk that are alive
at a point in time, say grouped by age x, what is the proportion that will die during
the period? So ^qx, based on the sample, is just the ratio of those that die during the
period to those alive and age x at the start of the period. From such studies various
statistical methods are used to develop estimates of the underlying probabilities of
death during the period by risk class, and this is denoted qx for the various ages or
otherwise defined risk classes.
The question of interest now, and one that a survival p.d.f. is intended to answer
is, of an individual member of a group alive at time 0, say aged x, what is the prob-
ability of death in year k for k ¼ 1; 2; 3 . . . ? The answer to this question is not a
qxþk1-value, as this is only the probability of a death in a year k given survival to
the beginning of that year. The necessary adjustment to qxþk1 is to multiply by
Qk1
j¼1 ð1  qxþj1Þ, since this now combines the probability of survival for the first
k  1 years, with the probability of death in year k.
For example, this model implies that two persons of age 25 and 30 can be expected
to have di¤erent probabilities of death between ages 30 and 31, meaning between the
30th and 31st birthdays, and for the younger person the probability is smaller. This
is not due to any projected favorable trends in the probabilities of death fqxg over
time, but simply that for the younger individual there is some chance that life will
terminate prior to reaching age 30. So the respective probabilities, using age-based
notation, are Q4
k¼0ð1  q25þkÞq30 and q30, respectively. So the younger person has a
lower chance of death in this year of age simply because they may not survive to the
beginning of it!
The mortality probability density, f MðjÞ, is therefore defined for j ¼ 1; 2; 3; . . . ,
and it denotes the probability that a person now alive will survive j  1 years and
die in year j, as is given by
f Mð jÞ ¼ qj
Y
j1
k¼1
ð1  qkÞ;
j ¼ 1; 2; 3; . . . :
ð7:128Þ
316
Chapter 7
Discrete Probability Theory

Again, within an actuarial context, the notation for this probability would be
ð j1Þjqx ¼ qxþj1
Y
j1
k¼1
ð1  qxþk1Þ
for j b 1;
where ð j1Þjqx denotes the probability of a person now age x will survive ðj  1Þ-
years and die in year j, and so 0jqx ¼ qx.
Associated with the p.d.f. f MðjÞ is the mortality distribution function, F MðjÞ ¼
P j
k¼1 f MðkÞ, and the survival function, S MðjÞ ¼ 1  F MðjÞ, which gives the proba-
bility that an individual survives j years.
Life Insurance Single Net Premium
One simple application of a survival model is to determine the expected present value
of an insurance payment of $1 to a person at the end of their year of death. This is a
whole life insurance contract, meaning the coverage does not expire as of a specified
point in time as is the case for term life insurance. Let I denote the random variable
that equals the present value of this insurance payment. The expected value of I con-
ditional on the death occurring in year j, denoted E½I j j, equals v j 1 ð1 þ iÞj for a
constant annual rate of interest i. The expected value of I equals the expected value
of these conditional expectations under f Sð jÞ by (7.43), and hence
E½I ¼
X
y
j¼1
v jqj
Y
j1
k¼1
ð1  qkÞ:
Here the use of y is merely a notational convenience.
The calculated value of E½I is the expected value of this whole life insurance pay-
ment in units of present value at rate i. It is often denoted Ax in standard actuarial
notation to identify the dependency on age x. It is a ‘‘single’’ premium, in that it
reflects what would need to be received at t ¼ 0 and invested at rate i to provide for
the expected benefit. Put another way, if received from a large group of individuals of
the same mortality risk and invested, all benefits would be payable with nothing left
‘‘in the end.’’
Also E½I is a ‘‘net’’ premium in that it provides only for the expected benefit; it
does not provide for the various risks that would be assumed with such a contract
(mortality, interest rate, etc.), nor does it provide for various levels of expenses asso-
ciated with selling and maintaining this policy, nor the associated profits that the in-
surer requires as a return on risk capital invested.
To
calculate
the
variance
of
I
using
conditioning
and
(7.46),
let
Qj ¼
qj
Q j1
k¼1ð1  qkÞ. Then from the calculation above that E½I j j ¼ v j 1 ð1 þ iÞj, we
have
7.8
Applications to Finance
317

Var½E½I j j ¼ E½ðE½I j jÞ2  ðE½E½I j jÞ2
¼
X
y
j¼1
v2jQj 
X
y
j¼1
v jQj
"
#2
:
Also the conditional variance is given by Var½I j j ¼ 0, and so E½Var½I j j ¼ 0.
Combining, we get
Var½I ¼
X
y
j¼1
v2jQj 
X
y
j¼1
v jQj
"
#2
:
This basic life insurance benefit can be modified in various ways and handled sim-
ilarly (see exercise 37).
Pension Benefit Single Net Premium
The survival function can also be used to evaluate, again on a single net premium
basis, the cost to provide for an annual pension benefit to an individual, payable at
the beginning of every year as long as the individual survives. This is an example of
what is called a life annuity contract. Let B denote the random variable that equals
the present value of these pension benefits or annuity payments. Then letting E½B j j
denote the expected value of this random variable conditional on death in year j we
obtain E½B j j ¼ P j
k¼1 vk1 ¼ ð1 þ iÞaj;i in the notation of (2.11) of chapter 2. In
other words, aj;i ¼ 1ð1þiÞj
i
. Using (7.43), we have
E½B ¼ ð1 þ iÞ
X
y
j¼1
aj;iqj
Y
j1
k¼1
ð1  qkÞ:
This value is a single net premium in the same sense as was E½I above, providing
for neither risks, expenses, nor profit. In exercise 19 is assigned the demonstration
that E½B can also be expressed in terms of the survival function S Mð jÞ. Using the
same approach as for insurance benefits, we derive
Var½B ¼ ð1 þ iÞ2 X
y
j¼1
a2
j;iQj  ð1 þ iÞ
X
y
j¼1
aj;iQj
"
#2
:
Life annuity benefits can be guaranteed payable for a minimum of m years,
and called an m-year certain life annuity, so that am is payable with probability
1  Pmþ1
j¼1 Qj, and thereafter for as long as life continues. Also annuity benefits need
318
Chapter 7
Discrete Probability Theory

not be payable for the remainder of an individual’s life; the annuity may be only pay-
able for survival up through n years, and called an n-year temporary life annuity con-
tract, or be guaranteed payable for a minimum of m years independent of survival to
a maximum of n years, and called an m-year certain, n-year temporary life annuity,
where logically m < n. Any of these annuity benefits can also be deferred k years,
and called k-year deferred . . . . See exercises 20 and 21.
Life Insurance Periodic Net Premiums
It is common that whole life insurance is paid for not as a single premium but as
a periodic premium, which we model as annually payable, although other payment
frequencies are common. Denoting by p the net premium payable annually for the
whole life insurance contract above, at the beginning of the year as long as the in-
sured survives, we derive from pE½B ¼ E½I,
p ¼
Py
j¼1 v jQj
ð1 þ iÞ Py
j¼1 aj;iQj
:
These periodic payments can also be structured to be payable only several years.
Pension and annuity contracts can also be paid for with periodic payments when
the annuity payments are deferred, as long as the payment period is less than or
equal to the deferral period, and that for death during the deferral period there is a
return of some fraction of payments with interest.
7.8.4
Asset Allocation Framework
The fundamental questions of asset allocation are:
1. Given a collection of risky assets, how does one model and evaluate the implica-
tions of allocating a given amount of wealth to each of these assets and a risk-free
asset in di¤erent ways?
2. Can certain allocations be said to be ‘‘preferred’’ to others in the sense that their
properties would be seen to be superior by any rational investor? Given allocations
W and V, examples of this preference for W over V would be, where we infor-
mally define risk in terms of the investor failing to achieve the desired investment
objectives:
W produces returns that are better than those of V no matter what happens in the
market.
W and V have the same risk, but W has more expected return.
W and V have the same expected returns, but W has less risk.
7.8
Applications to Finance
319

3. Can certain allocations, W, be said to be ‘‘relatively optimally preferred’’ to
others? For example:
W has a better expected return than any other allocation with the same risk.
W has less risk than any other allocation with the same expected return.
4. Can a certain allocation, W, be said to be ‘‘optimally preferred’’ in the sense that
of all relatively optimally preferred allocations, W would be seen to be superior by
any rational investor?
In this section we begin the analysis of asset allocation by addressing a framework
for such investigations, which is the essence of question 1 above. We will return to
this subject in later chapters with additional results as additional tools are developed.
The most general analyses require the tools of multivariate calculus and linear
algebra.
To this end, assume that a given finite collection of risky assets fAjgn
j¼1 and a sin-
gle risk-free asset T are given. By risky is meant that the return over the investor’s
horizon is uncertain, and risk-free means the return is certain over the investment ho-
rizon. Consequently the risk-free asset depends on the investor and the investment
horizon. While a one-month T-bill in the United States is risk-free for a US dollar
investor with a one-month investment horizon, it is neither risk-free for a US dollar
‘‘day trader’’ nor is it risk-free for euro investor with a one-month investment
horizon.
Given this notion, it must be the case that for any investor group with a common
investment horizon, there is e¤ectively one risk-free investment vehicle, which is to
say, any two such vehicles would share a common and unique return. This is because
if there were two such investments with di¤erent returns, investors would sell the
lower return investment and buy the higher return investment to create a risk-free
arbitrage, or simply, arbitrage. Sales pressure on the former would lower its price
and increase its return, while demand pressure on the latter would increase price
and decrease return, until return equilibrium was achieved.
An asset allocation is a vector W ¼ ðw0; w1; . . . ; wnÞ, where w0 represents the in-
vestment in T, and wj the investment in Aj. This vector can be unitized in relative
terms, where Pn
j¼0 wj ¼ 1, and correspondingly wj denotes the proportion of total
wealth invested in the given asset, or in absolute terms, where Pn
j¼0 wj ¼ W0 and cor-
respondingly wj denotes the actual wealth invested in the given asset, with W0 repre-
senting total initial wealth. The mathematical development in the two cases is similar,
di¤ering in predictable ways. To simplify notation, we assume that W is unitized in
relative terms, and will explicitly acknowledge total wealth of W0 when necessary.
320
Chapter 7
Discrete Probability Theory

To set notation, let Rj denote the random return from asset Aj over the investment
horizon, which can be assumed to be discrete if for no other reason than investors’
limited appetite for long decimal expressions in return reports, and let rF denote the
fixed risk-free return for the period. To simplify, assume that the investment horizon
is one year, and that all rates are expressed as annual returns. Unless wj ¼ 0 for
j b 1, it is apparent that the return on this portfolio allocation, R, is risky, and can
be represented as
R ¼ w0rF þ
X
n
j¼1
wjRj:
ð7:129Þ
The return R is a discrete random variable with probability function f ðRÞ, the do-
main values of which depend on the given allocation as well as the p.d.f.s of the var-
ious Rj.
Given an asset allocation, the theoretical connection between f ðRÞ and f f ðRjÞg is,
in general, complicated even when the latter are explicitly known. A counterexample
where simplicity prevails is when the collection fRjg is assumed to have a multivari-
ate normal distribution, which is not discrete, but then R will have a normal distribu-
tion. But this statement is way ahead of the tools developed so far.
Without additional tools it is also very di‰cult to even empirically simulate the
implied p.d.f. for R, since this requires the simulation of collections fRjg of risky
asset returns. While a random sample of returns on any one risky asset Aj can be
simulated from its c.d.f. using the method described in section 7.7, the di‰culty asso-
ciated with generating the collection of returns for all assets is that it is virtually
never the case that these returns are ‘‘independent,’’ or the weaker statement,
‘‘uncorrelated.’’ In other words, between virtually any two risky assets one evaluates
historically, it is the case that the correlation between returns r is generally nonzero;
in almost all nontrivial cases, it is positive, so r > 0. By a trivial case is meant that if
one asset is a long position and the other a short position in a given security, then
artificially one will have constructed a case with r < 0, and in fact r ¼ 1. But
most examples of long positions display positive correlations and more generally
nonzero correlations, and consequently an empirical simulation of returns on the
risky assets needs to reflect these correlations.
One popular approach to simulation is known as historical simulation, whereby
one has access to contemporaneous return series for each of the assets in question:
fðRðkÞ
1 ; RðkÞ
2 ; . . . ; RðkÞ
n Þ j k ¼ 1; 2; . . . ; Ng. This notation implies that for each sequen-
tial time period k, which would be chosen in length to equal the investment horizon
of interest, ðRðkÞ
1 ; RðkÞ
2 ; . . . ; RðkÞ
n Þ denotes the respective returns of the given assets
7.8
Applications to Finance
321

during this period. For the same historical periods one would also identify the
returns of the risk-free asset, denoted frðkÞ
F g. With these data series two simulations
are possible:
1. Simulation of historical returns for the given allocation,
RðkÞ ¼ w0rðkÞ
F þ
X
n
j¼1
wjRðkÞ
j :
2. Simulation of potential returns for the next period, where rF is known,
RðkÞ ¼ w0rF þ
X
n
j¼1
wjRðkÞ
j ;
which is in e¤ect the model in (7.129).
From either model and a specified allocation fwjgn
j¼0, a return data series is simu-
lated, fRðkÞg, from which all moments of R can be calculated and f ðrÞ estimated.
However, if it is desired to evaluate explicitly how these moments depend on the al-
location parameters, an alternative approach is needed.
Specifically, sample moments from the historical return data can be used to esti-
mate the various moments of the random variable R, without needing to fix the
allocation parameters or explicitly calculate f ðRÞ. For example, applying (7.38) to
(7.129), we derive
E½R ¼ w0rF þ
X
n
j¼1
wjmj;
mj 1 E½Rj;
ð7:130Þ
and applying (7.56),
Var½R ¼
X
n
i¼1
X
n
j¼1
wiwjsisjrij;
ð7:131aÞ
s2
j 1 Var½Rj;
rij 1 Corr½Ri; Rj:
ð7:131bÞ
Of course, if the goal is to calculate the mean and variance of end of period
wealth, defined as W1 ¼ W0ð1 þ RÞ, these would be calculated as
E½W1 ¼ W0½1 þ m;
Var½W1 ¼ W 2
0 s2;
ð7:132Þ
where m and s2 are commonly used notation for E½R and Var½R, respectively.
322
Chapter 7
Discrete Probability Theory

Higher moments can similarly be estimated from the higher joint sample moments
of the historical data. For example, the third central moment, m3 1 E½ðR  mÞ3, is
developed from R  m ¼ Pn
j¼1 wjðRj  mjÞ, and hence
ðR  mÞ3 ¼
X
n
i¼1
X
n
j¼1
X
n
k¼1
wiwjwkðRi  miÞðRj  mjÞðRk  mkÞ:
This formula requires a bit of combinatorial manipulation, but the expectation will
clearly involve terms as follows, where the subscripts are now intended to be distinct:
E½ðRi  miÞðRj  mjÞðRk  mkÞ;
E½ðRi  miÞðRj  mjÞ2;
E½ðRi  miÞ3:
The analysis of these risk and return statistics, especially in terms of their behav-
iors for di¤erent allocation vectors, W, is now a question of evaluating these
moments as functions of ðw0; w1; . . . ; wnÞ considered as a point in Rnþ1. Such an
analysis requires the more powerful tools of multivariate calculus and linear algebra
to be complete. Still here we can appreciate what is to come with an informal analy-
sis of the issue raised in question 2 above.
Given allocations W and V, there are many ways to define that W is ‘‘preferred’’
over V. For example, given the allocation W ¼ ðw0; w1; . . . ; wnÞ define an epsilon
switch allocation Wij
 as equal to W except that wi is increased by , and wj is
decreased by . Let R denote the random return under W; and Rij
 the return under
Wij
 . An easy calculation produces
E½Rij
   E½R ¼ ðmi  mjÞ;
where for notational convenience we denote rF by m0. Clearly, for  > 0 the expected
return is increased or decreased according to whether mi > mj or mi < mj.
For the variance analysis, the notation is simplified by noting that (7.131a) can be
expressed as
Var½R ¼
X
n
i¼0
X
n
j¼0
wiwjsij;
sij 1 Cov½Ri; Rj;
sjj 1 Var½Rj;
ð7:133Þ
since for any j 0 0, s0j ¼ sj0 ¼ 0 and s2
0 ¼ 0. With this formula the change in vari-
ance can be calculated, although in a more complicated way. The trick is to split the
summation into terms that include i or j,
2wi
X
k0i; j
wksik þ 2wj
X
k0i; j
wkskj þ 2wiwjsij þ w2
i s2
i þ w2
j s2
j ;
7.8
Applications to Finance
323

and into terms that exclude both i and j,
X
k0i; j
X
l0i; j
wkwlskl:
With this splitting, since only wi and wj are changed, we obtain with a bit of
algebra
Var½Rij
   Var½R ¼ 2
X
k0i; j
wkðsik  skjÞ þ 2½ðwi  wjÞ  2sij
þ 2ðs2
i þ s2
j Þ þ 2ðwis2
i  wjs2
j Þ
¼ 2½s2
i þ s2
j  2sij þ 2
X
n
k¼0
wkðsik  skjÞ þ 2ðwi  wjÞsij
"
#
:
In other words, given any i and j, Var½Rij
   Var½R is a quadratic function of  that
goes through the origin. So for fixed constants A and B that depend on i and j,
Var½Rij
   Var½R ¼ A2 þ 2B:
Now in the proof of (7.54) it was shown by use of the Cauchy–Schwarz inequality,
that s2
ij a s2
i s2
j . From this we conclude that sisj a sij a sisj, and hence A b 0.
Specifically,
0 a ðsi  sjÞ2 a A a ðsi þ sjÞ2:
Now, if B ¼ 0, then Var½Rij
   Var½R b 0 for all  and the epsilon switch creates the
same or more risk. If B 0 0, this inequality for A implies that there is an interval for
 for which Var½Rij
   Var½R < 0, which is to say, that the variance has been
decreased. Specifically, if B > 0, the variance reduction interval is  A  2B
A ; 0


,
whereas if B < 0, the variance reduction interval is
0; 2B
A


. In both cases the point
of maximal reduction is the interval midpoint.
This simple analysis can provide one answer to question 2 on an allocation being
‘‘preferred.’’ Namely, if there is an i and j for which the expected return can be
increased, E½Rij
  > E½R, and variance of return decreased, Var½Rij
  < Var½R, then
this would appear to be a reasonable basis to claim that Wij
 is preferred to W. Of
course, this is only a reasonable basis, since it ignores higher moments of these ran-
dom variables with the two allocations.
324
Chapter 7
Discrete Probability Theory

7.8.5
Equity Price Models in Discrete Time
Stock Price Data Analysis
Let S0 denote the price of an equity security at time zero. Many problems in finance
relate to modeling the probability density functions and related characteristics of
prices at a point in the future, or the evolution of such prices through time. Essential
to this model is the notion that future stock prices, as well as the prices of futures
contracts, currencies, interest rates, and so forth, are fundamentally random vari-
ables at time zero, even though their movements may well be fully or at least par-
tially explainable after the fact. This is sometimes described by saying that future
prices are random ex ante, but deterministic and possibly explainable ex post. These
perspectives are not at odds.
Being explainable ex post means that one can develop certain cause and e¤ect
arguments that make the price e¤ect understandable and even compelling, whereas
being random ex ante means that one cannot predict what the future causes of price
movements will be. In general, these causes evolve with the markets’ information pro-
cesses, which is the general model of how information emerges and travels through
the markets. Randomness of price movements therefore reflects the randomness in
the discovery, release, and dissemination of market relevant information.
Historical analysis also reinforces this view of randomness. If fSjg denotes a given
stock price series evaluated at the market’s close on a daily, weekly, or other regu-
larly spaced basis over a reasonably long period of time, say 10 years or so, the col-
lection of period returns fRjg 1
Sjþ1Sj
Sj
n
o
can be plotted as a sequence, called a time
series, and will generally appear to have many of the characteristics of a coin-flip se-
quence. Specifically, about 50:50 positive and negative results, with positive and neg-
ative runs of varying lengths.
Also, while one observes runs, a calculation of the correlation between successive
returns, Rj and Rjþ1, produces a so-called autocorrelation that is typically near 0. By
autocorrelation is meant the correlation of a random variable with itself over time.
An autocorrelation near 0 implies that on average, Rj provides little predictability
to the value or even the sign of Rjþ1, again like a series of coin flips. It is also the
case that grouping ranges of returns, and plotting the associated approximate p.d.f.
in a histogram, provides a familiar bell-shaped curve, seemingly almost normally dis-
tributed. But closer analysis proves that this distribution often has fat tails in the
sense that the probabilities of normalized returns far from 0 exceed that allowed by
the normal distribution.
These same characteristics are often observed in the growth rate series or log-ratio
return series, frjg 1
ln
Sjþ1
Sj

	
n
o
1 flnð1 þ RjÞg. The log-ratio returns tend to be the
7.8
Applications to Finance
325

more popular for modeling, since in this case Sjþ1 ¼ Sjerj, whereas in terms of period
returns, Sjþ1 ¼ Sjð1 þ RjÞ. While this may appear of little mathematical conse-
quence, the distinction comes from the modeling of prices n-periods forward:
Return model:
Sn ¼ S0
Y
n1
j¼0
ð1 þ RjÞ;
ð7:134Þ
Growth model:
Sn ¼ S0eT n1
j¼0 rj:
ð7:135Þ
From these formulas it should be apparent that using frjg as the collection of re-
turn variables requires the modeling of sums of random variables, whereas with fRjg,
we will be required to work with products. The log-ratio return parametrization is to
be preferred simply because the mathematical analysis is more tractable in these
terms.
Binomial Lattice Model
Now let m and s2 denote the mean and variance of the log-ratio return series, where
these parameters of necessity reflect some period of time, say Dt ¼ 1, separating the
data points. Knowing from history that frjg has a bell-shaped distribution for small
time intervals, one can approximate the log-ratio returns with binomial returns in an-
ticipation of results of chapter 8:
Sjþ1 ¼ SjeBj:
Here fBjg are a random collection of i.i.d. binomials defined by
B ¼
u;
Pr½u ¼ p,
d;
Pr½d ¼ p0,

where p0 1 1  p and p, u, and d are ‘‘calibrated’’ to achieve the desired moments
from historical data as follows.
To derive all three model parameters from historical data will require three con-
straints. In practice, the analysis is often simplified by introducing one reasonable
constraint judgementally. For example, by choosing p ¼ 1
2 , E½B ¼ 1
2 ðu þ dÞ, E½B2 ¼
1
2 ðu2 þ d 2Þ, and Var½B ¼ 1
4 ðu  dÞ2. Consequently, in order to produce the two his-
torical moments, it is required that
1
2 ðu þ dÞ ¼ m;
326
Chapter 7
Discrete Probability Theory

1
4 ðu  dÞ2 ¼ s2;
which is easily solved to produce the stock model
Sjþ1 ¼
Sjemþs;
p ¼ 1
2,
Sjems;
p0 ¼ 1
2.
(
ð7:136Þ
An alternative calibration is to constrain d ¼ 1
u ; then using only mean and variance
again, determine the parameters p and u.
From this p ¼ 1
2 model, stock prices in n time steps are seen to be binomially dis-
tributed with parameters n and p. This is because (7.135), with rj ¼ m þ bjs and
bj ¼
1;
Pr ¼ 1
2,
1;
Pr ¼ 1
2,
(
produces
Sn ¼ S0enmþs T n1
j¼0 bj;
ð7:137Þ
where Pn1
j¼0 bj assumes values of fn þ 2kgn
k¼0 with probabilities f n
k
  1
2 ngn
k¼0.
This observation allows a notationally simpler parametrization of stock prices as
follows:
Sn ¼ S0enðmsÞþ2sBn ¼ S0endþðudÞBn;
ð7:138aÞ
Pr½Bn ¼ j ¼
n
j

 1
2n ¼
n
j


p jð1  pÞnj;
j ¼ 0; 1; . . . ; n:
ð7:138bÞ
This formula is the basis of the binomial lattice model of stock prices whereby from
an initial price of S0 two prices are possible at t ¼ 1, three prices are possible at
t ¼ 2; . . . , and finally, n þ 1 prices are possible at time n. Not uncommonly, these
prices are represented in a positive integer lattice, with time plotted on the horizontal,
and ‘‘state,’’ or random stock price, along the vertical, as seen in figure 7.3.
The graph shown in the figure is usually oriented in the logical way, with lowest
stock prices plotted at the bottom and associated with Bn ¼ 0. From any ‘‘time-
state’’ price, there are two possibilities in the next period, with the price directly
to the right representing d, and the price to the northeast representing u, both with
probability 1
2 with this calibration. With the calibration assigned in exercise 23,
the probability of the price directly to the right equals 1  p, while the price to the
7.8
Applications to Finance
327

northeast has probability p. Looked at another way, the collection of n þ 1 prices at
time n are distributed as binomial variables with parameters n and 1
2 , as is indicated
in (7.138), or more generally in exercise 23, distributed as binomial variables with
parameters n and p. This provides a bell-shaped distribution of returns defined
as ln½Sn=S0, which is consistent with historical data. This will be formalized in chap-
ter 8.
Binomial Scenario Model
An alternative and equally useful way to both conceptualize the evolution of stock
prices, as well as to perform many types of calculations, is to generate stock price
paths, or stock price scenarios. In contrast to the binomial lattice approach, which
generates all possible prices up to time n under this model, the scenario approach
generates one possible price path at a time. An example of a single price path is
seen in figure 7.4.
Each such path requires the generation of n prices, since S0 is given. In contrast,
the generation of a complete lattice requires Pnþ1
j¼2 j ¼ ðnþ1Þðnþ2Þ2
2
prices. The motiva-
tion for the scenario-based approach is often not combinatorial. Since there are 2n
possible paths, to generate them all requires 2nn calculations when done methodi-
cally, and this materially exceeds ðnþ1Þðnþ2Þ2
2
in total e¤ort. In the typical situation
the motivation for scenarios might be that the given problem cannot be solved within
a lattice framework but can only be solved with generated paths.
Figure 7.3
Binomial stock price lattice
328
Chapter 7
Discrete Probability Theory

For example, the price of a simple European or American option on a given com-
mon stock can be estimated on a lattice of stock prices. On the other hand, if the
value of a European option at expiry reflects values of the stock’s prices along what-
ever price path it followed, lattice-based methods do not work, and this calculation
must be estimated with scenario-based calculations.
Scenario methods are also necessary in certain lattice models that are nonrecombin-
ing. The lattice model above is recombining in that from any given price the same
price is produced two periods hence if the intervening returns were ðu; dÞ or ðd; uÞ.
Not all lattices have this property. A nonrecombining lattice is one for which
Sðu;dÞ 0 Sðd;uÞ. In such a case generation of the entire lattice may be impossible, since
the number of such prices is now Pnþ1
j¼1 2 j ¼ 2nþ2  1. For a nonrecombining model,
even if lattice-based methods are theoretically possible, as in European option pric-
ing, they are infeasible for large n, and scenario-based methods are required.
7.8.6
Discrete Time European Option Pricing: Lattice-Based
One-Period Pricing
Remark 7.61
In this and other sections on option pricing, or more generally deriva-
tives pricing, the underlying asset, denoted S, will be called a common stock. How-
ever, all of this theory applies to derivatives on any asset in which investors can take
short positions. Of course, all assets allow investors to take long positions by simply
Figure 7.4
Binomial stock price path
7.8
Applications to Finance
329

acquiring them, so allowing a short position is somewhat restrictive. It is common lan-
guage to call assets that can be shorted, investment assets, since these are assets com-
monly held in inventory by investors for their appreciation potential. Common stocks
and stock indexes, fixed income investments and indexes, currencies, precious metals
like gold and platinum, and all futures contracts are examples of investment assets;
the general framework developed here is adaptable to derivatives on these assets. Other
assets are called consumption assets, since these are assets that rarely are held in inven-
tory except for consumption purposes; hence they are not available for lending and
shorting. Examples include most commodities other than precious metals.
Suppose that on a given stock with current value S0, which will be assumed to pay
no dividends, we seek to price a European option or other derivative security that
expires in one period, and whose payo¤ is given by an arbitrary function of price at
that time, denoted LðS1Þ. Recall that the terminology ‘‘European’’ means that the
option provides for no early exercise; it can only be exercised on the expiry date.
For example, if this option is a European call or a put with a strike price of K, the
payo¤ function to the holder of the option is given:
Call option:
LðS1Þ ¼ maxðS1  K; 0Þ;
ð7:139aÞ
Put option:
LðS1Þ ¼ maxðK  S1; 0Þ;
ð7:139bÞ
where the use of the ‘‘max’’ function is conventional and shorthand for the fact that
the holder of the option, or the ‘‘long position,’’ will either receive a positive payo¤
or nothing.
For the purposes here, the payo¤ function LðS1Þ can be arbitrary without a¤ecting
the mathematical development, but it is common in the market that LðS1Þ b 0 for
the long position, and LðS1Þ a 0 for the short. Again, the mathematics does not re-
quire this, but the terminology is simplified in this case. An example of a derivatives
security in the market that has both positive and negative payo¤s is a futures con-
tract, for which a long futures contract is equivalent to a long call and short put,
and conversely, and either side of the contract can be paid or required to pay at
expiry. To simplify the language below, we will assume that we are taking the per-
spective of the long position.
Assume that the stock price in one period is modeled,
S1 ¼
S0eu;
Pr ¼ p,
S0ed;
Pr ¼ 1  p,

330
Chapter 7
Discrete Probability Theory

for suitable p, u, d. Then the option payo¤ is either LðS0euÞ or LðS0edÞ, which we
denote by Lu and Ld, respectively. Naturally the price of this option at time 0, L0,
cannot equal or exceed the present value of the greater payo¤, nor be equal to or less
than the present value of the lesser payo¤. In the former case, an investor would try
to sell these options, and in the latter, buy them, thereby creating a chance (perhaps
certain chance) of profit with no risk, which is an arbitrage, or a risk-free arbitrage.
In theory, such a purchase would be financed by shorting T-bills, and the sale of
options invested in T-bills, thereby insulating the trader from all risk.
Let r denote the continuous risk-free interest rate for this period, on a Treasury bill
say. Note that it is nonstandard to quote r in other than annual units, and we correct
this in chapter 8 where the appropriate time context is addressed. These bounds on
L0 can be expressed as
er min½Lu; Ld < L0 < er max½Lu; Ld:
Consequently there must be a unique real number q that can be called a probability,
since 0 < q < 1, so with q0 ¼ 1  q,
L0ðS0Þ ¼ er½qLu þ q0Ld:
ð7:140Þ
In other words, the market price must equal the expected present value of the payo¤s
at some as yet unspecified ‘‘probability’’ q.
It turns out that q can be derived because this option can be replicated. The idea of
replication is that one can construct a portfolio of traded assets that has the same
payo¤ as does the option. Hence the price of the option must equal the price of this
portfolio, or else there will be an arbitrage opportunity. If the option was more ex-
pensive than the replicating portfolio, the savvy trader would sell the option, buy
the portfolio for an immediate profit, and settle at expiry with no out of pocket
cost. Similarly, if the option was cheaper than the replicating portfolio, the opposite
trade would be implemented.
The replicating portfolio turns out to be a mix of stock and risk-free assets, usually
referred to as T-bills. To see this, construct a portfolio of a shares of stock, and $b
invested in T-bills, so the portfolio, denoted P0, is
P0 ¼ faS0; bTg;
where T denotes a $1 investment in a T-bill. This portfolio costs aS0 þ b at time 0,
and at time 1 will have values
7.8
Applications to Finance
331

P1 ¼
aS0eu þ ber;
Pr ¼ p,
aS0ed þ ber;
Pr ¼ p0:

It is not di‰cult to determine the correct values of a, b so that aS0eu þ ber ¼ Lu
and aS0ed þ ber ¼ Ld. Specifically, we derive
a ¼
Lu  Ld
S0ðeu  edÞ ;
b ¼ er euLd  edLu
eu  ed
:
ð7:141Þ
With these coe‰cients, a bit of algebra shows that the price of this portfolio at
time 0, which is
L0ðS0Þ ¼ aS0 þ b;
ð7:142Þ
can be expressed as in (7.140) with
q ¼ er  ed
eu  ed :
ð7:143Þ
It must be the case that 0 < q < 1, since the stock is a risky asset. Hence ed <
er < eu, or else an arbitrage opportunity would exist.
We collect these results in a proposition:
Proposition 7.62
Let LðSÞ denote the payo¤ function for a one-period European
derivatives contract on an investment asset with current price S0, for which the end of
period prices follow a binomial distribution as given in (7.138) with n ¼ 1. Then the
price of this derivatives contract L0ðS0Þ equals the price of the replicating portfolio
given in (7.142), with coe‰cients given in (7.141). Alternatively, this price can be
expressed as in (7.140) with probability q defined in (7.143).
Remark 7.63
This ‘‘probability’’ q is known as the risk-neutral probability of an up-
state, since this is what the probability of an upstate must be in a risk-neutral world to
justify the stock price of S0. To better see this, first note that q is the unique probability
that prices the current value of the common stock, S0, to be equal to the risk-free pres-
ent value of its expected future prices:
S0 ¼ er½qS0eu þ q0S0ed:
ð7:144Þ
So why does this matter? We will see more on risk preference models in chapter 9,
but the conclusion will be that risk-neutral investors do not charge for risk, as the term
implies, and consequently they require the same return on all investments. Logically
332
Chapter 7
Discrete Probability Theory

this implies that the same return they require for all assets is the risk-free return. But
what does ‘‘require the same return’’ mean if an asset has risk? The answer is that each
investor can summarize risk through their own ‘‘utility function,’’ and in general, will
price assets in order to maximize the expected value of the utility of their wealth. This
is usually called maximizing expected utility. For a risk-neutral investor, utility maxi-
mization turns out to be equivalent to pricing assets based on expected payo¤s. Rewrit-
ing the stock-pricing formula above, we have
S0er ¼ ½qeu þ q0edS0;
which shows that the expected payo¤ on S0 under q provides the risk-free return.
Of course, no one believes investors to be risk neutral, but this is a good framework
for describing how q can be interpreted. Indeed the model suggests that if investors ex-
pect a log-ratio return of m, they likely believe that the probability of prices rising to
S0eu is p, and not q. It is not di‰cult by example to show that q 0 p, and this can be
proved with methods of chapter 9.
Multi-period Pricing
A two-period European option with payo¤ function LðS2Þ can be priced with the
same methodology. If we know the prices of this option at time 1 in both stock price
‘‘states,’’ LðS u
1 Þ and LðS d
1 Þ, then the price at time 0 is given by (7.140) with risk-
neutral probability q in (7.143):
L0ðS0Þ ¼ er½qLðS u
1 Þ þ q0LðS d
1 Þ:
ð7:145Þ
The argument is the same. This is the correct price because a replicating portfolio can
be purchased for this amount that provides the correct future values whether the
stock price rises or falls.
On the other hand, LðS u
1 Þ can also be evaluated by this formula based on the pay-
o¤s at time 2,
LðS u
1 Þ ¼ er½qLðS2u
2 Þ þ q0LðS uþd
2
Þ;
and similarly for LðS d
1 Þ,
LðS d
1 Þ ¼ er½qLðS dþu
2
Þ þ q0LðS2d
2 Þ:
These formulas again follow, since these are the prices of the respective replicating
portfolios. Note that the subscript in these formulas denotes time, and superscript
denotes the stock state. For example, S2u
2 ¼ S0e2u, and so forth.
7.8
Applications to Finance
333

Inserting the second two formulas into the first, we see that L0ðS0Þ is again equal
to the expected present value of the t ¼ 2 payo¤s, where the expectation is calculated
with binomial probability q, and the present value at the risk-free rate r, producing
L0ðS0Þ ¼ e2r½q2LðS2u
2 Þ þ 2qq0LðS dþu
2
Þ þ ðq0Þ2LðS2d
2 Þ:
ð7:146Þ
In exercise 39 is assigned the proof of the generalized version of this formula, for a
European option with expiry in n time steps. The formula becomes
L0ðS0Þ ¼ enr X
n
j¼0
n
j


q jð1  qÞnjLðS j
nÞ;
S j
n ¼ S0e juþðnjÞd:
ð7:147Þ
This price can also be expressed as the price of a replicating portfolio that repli-
cates option prices at time 1-period, where the option prices are in turn given by an
application of this same formula with n  1 periods to expiry:
LðS u
1 Þ ¼ eðn1Þr X
n1
j¼0
n  1
j


q jð1  qÞn1jLðS uj
n1Þ;
ð7:148aÞ
LðS d
1 Þ ¼ eðn1Þr X
n1
j¼0
n  1
j


q jð1  qÞn1jLðS dj
n1Þ;
ð7:148bÞ
where
S uj
n1 ¼ S u
1 e juþðn1jÞd;
S dj
n1 ¼ S d
1 e juþðn1jÞd:
In other words, L0ðS0Þ in (7.147) satisfies (7.145) with these values of LðS u
1 Þ and
LðS d
1 Þ, and from the preceding section we know that this is the same price as that
of a replicating portfolio that replicates these option values. This result can be dem-
onstrated directly by an application of (7.16).
By (7.147), the price of the option can be expressed as an expected present value
under the assumption that the calculated value of q in (7.143) is the correct binomial
probability of an upstate return of eu. This will di¤er from the binomial probability
of p that we started with, that reproduced the mean and variance of the stock’s log-
ratio returns.
Of course, the price in (7.147) is the theoretically correct price under the assump-
tions of this lattice. If two analysts calibrate their lattices to di¤erent assumptions of
stock price behavior, or even the same assumptions but calibrated with di¤erent time
steps of Dt, di¤erent prices will result, possibly materially di¤erent.
334
Chapter 7
Discrete Probability Theory

In finance, the p-model is referred to as the real world model, since it produces the
statistical properties observed or believed to be valid in the real world, and the q-
model is referred to as the risk-neutral model, since these probabilities correctly price
the stock in a world where investors are risk neutral.
We collect these results in a proposition:
Proposition 7.64
Let LðSÞ denote the payo¤ function for an n-period European deriv-
atives contract on an investment asset with current price S0, for which the end of period
prices follow a binomial distribution as given in (7.138). Then the price of this deriva-
tives contract, L0ðS0Þ, is given in (7.147) with probability q defined in (7.143). This
price also equals that of the replicating portfolio given in (7.142), with coe‰cients
given in (7.141), where the derivatives prices at time 1-period are given by (7.148).
Remark 7.65
It is important to recognize that while the pricing formula in (7.147)
can be understood to provide a risk-neutral present value of option payo¤s, this inter-
pretation does not provide a compelling reason why the number produced is the theoret-
ically correct market price. The logic that compels this conclusion is that L0ðS0Þ as
given in that formula also satisfies the equation in (7.145):
L0ðS0Þ ¼ er½qLðS u
1 Þ þ q0LðS d
1 Þ:
So by the analysis of the one-period model, this is the price of a portfolio that replicates
the value of this option at the end of the first period. Each of these prices in turn equals
what is needed to create a portfolio that replicates option prices in the next period, and
so forth. In other words, by ‘‘rebalancing’’ the replicating portfolio each period after
the first, and realizing this can be done with no additional costs, these replicating port-
folios will track the emerging values of the option up to the final period in which the last
replicating portfolio will replicate the actual option payo¤s. That said, this argument
ignores all real world market ‘‘friction’’ caused by trading costs and taxes, so the real
world price will need to be adjusted somewhat for this.
Of course, the replication argument relies on the assumption that this option is
on an investment asset as noted above. The reason for this is twofold. First o¤, the
actual replicating portfolio will involve a short position in S when a < 0 in (7.141),
which occurs when Lu < Ld. This is the case for a put option, for instance. Second,
this argument does not in and of itself compel the conclusion that options must be
sold at this price, it merely demonstrates that they could be sold near this price be-
cause the seller can hedge his risk with a replicating portfolio. In other words, selling
the option creates a short position for the seller that can be hedged with a
long position in the replicating portfolio. By ‘‘near this price’’ is meant adjusted for
7.8
Applications to Finance
335

transactions costs and buyer convenience. Now, if the seller attempts to sell an
option on an investment asset at a price materially di¤erent from the replicating
portfolio cost, one of two things happen. Some investors will buy ‘‘cheap options’’
and hedge their position with short positions in the replicating portfolio. Some other
investors will sell ‘‘dear options’’ and hedge with a long position in the replicating
portfolio. In either case, the buying pressures would increase prices, and selling pres-
sures would decrease prices. So in both cases investors move toward the price of the
replicating portfolio, as adjusted for transactions costs.
7.8.7
Discrete Time European Option Pricing: Scenario Based
If N-paths are randomly generated, and fS j
ngn
j¼0 denotes the n þ 1 possible stock
prices in the recombining lattice above at time n, it is of interest to analyze the num-
ber of paths that arrive at each final state. In theory, we know from the lattice anal-
ysis above that the distribution of stock prices at time n is binomially distributed
with parameters n, p in general, and hence Pr½Sn ¼ S j
n ¼
n
j
 	
p jð1  pÞnj. Here p
denotes the probability of a u-return, and stock prices are parametrized so that
j ¼ 0 corresponds to the lowest price, S0
n ¼ endS0, and j ¼ n corresponds to the
highest price, S n
n ¼ enuS0. On the other hand, we have shown that for the purposes
of option pricing, we continue to use the stock price returns of eu and ed but switch
the assumed probability of an upstate return from p to q given in (7.143).
In the lattice-based model, these q probabilities provide the likelihood of each final
state for option pricing. Consequently, if from a sample of N-paths, Nj denotes the
number that terminate at price S j
n so that P Nj ¼ N, then the ðn þ 1Þ-tuple of inte-
gers ðN0; N1; . . . ; NnÞ has a multinomial distribution with parameters N and fQjgn
j¼0,
where Qj ¼
n
j
 	
q jð1  qÞnj. In other words, from (7.105) and (7.106) we conclude
that
E½Nj ¼ NQj;
ð7:149aÞ
Var½Nj ¼ NQjð1  QjÞ;
ð7:149bÞ
Cov½Qj; Qk ¼ NQjQk:
ð7:149cÞ
In a nonrecombining lattice, Qj is again defined as the risk-neutral probability of
terminating at price S j
n, only in this case there are 2n stock prices rather than n þ 1.
The multinomial distribution is again applicable as are the moment formulas above.
As an application we develop the methodology for estimating the price of an n-
period European option using the scenario-based methodology. For simplicity, we
focus on the recombining lattice model, although the development is equally applica-
336
Chapter 7
Discrete Probability Theory

ble in the more general case. To this end, let LðS j
nÞ denote the exercise value of the
option at time n when the stock price, S j
n, prevails. Given N-paths, define a random
variable ON, the sample option price,
ON ¼ enr
N
X
n
j¼0
NjLðS j
nÞ:
ð7:150Þ
Intuitively the random variable ON is an estimate of the true option price based
on a price scenario sample of size N. Although this formula at first looks completely
di¤erent from the exact formula given in (7.147), the formulas are quite similar. Be-
cause of (7.149a), it is apparent that
E Nj
N


¼ Qj 1
n
j


q jð1  qÞnj;
and consequently the option price in (7.147) can be rewritten as
L0ðS0Þ ¼ enr X
n
j¼0
E Nj
N


LðS j
nÞ:
In this form it is apparent that the di¤erence between L0ðS0Þ and ON is that for
the former, the option exercise price of LðS j
nÞ is given the theoretically correct weight
E
Nj
N
h i
, while for the latter, this weight is replaced by a sample-based estimate
Nj
N . We
should then expect that since the paths are generated in such a way as to arrive at
each final stock price with the correct probability, the expected value of this random
variable ought to equal L0ðS0Þ, and this will be the case.
Even more important, it will turn out that as N increases, the probability that we
are in error by any fixed amount goes to 0. These results are demonstrated in chapter
8. In addition the relationship of this pricing approach to the replication-based pric-
ing above will be evaluated.
Exercises
Practice Exercises
1. Demonstrate that if E is a complete collection of events, and Aj A E for j ¼ 1; 2;
3; . . . , then 7j Aj A E.
2. Confirm that in the sample space S of sequences of 10 flips of a fair coin, the event
A ¼ fx j x ¼ HH . . .g contains exactly 25% of the total number of sequences, where
Exercises
337

this notation means that only the first two outcomes are fixed. In this demonstration,
if you ignore what happens after the first 2 flips, justify explicitly that this is valid.
3. On the sample space of 10-flip sequences of a fair coin S:
(a) Define three di¤erent random variables, X : S ! R. (Hint: For simplicity, iden-
tify an H with a 1, and a T with a 0.)
(b) Determine the associated ranges of these functions.
(c) Calculate PrðaÞ for one a in the range of each X.
4. Generalize (7.2) and (7.1) in the following way:
(a) If a gambler is asked to bet m for a chance to win n, what is the probability of
winning that will make this bet fair? Confirm that m ¼ 1 gives (7.2).
(b) If the gambler knows that the probability of a win is p, what ratio of amount bet
to amount won, m
n from part (a), will make this a fair bet? Confirm that m ¼ 1 gives
(7.1).
(c) Show that if p is irrational in part (b), a fair bet requires an irrational value for
m
n . Conclude that since bets and payo¤s must be rational numbers, a bet with an ir-
rational probability of winning can never be fair.
5. Show that if an event B A E satisfies PrðBÞ 0 0, then Prð j BÞ satisfies all the defini-
tional properties of a probability measure on the sample space S.
6. Consider the sample space of 5 flips of a fair coin, where we identify an H with a
1, and a T with a 0. Define events A and B as
A ¼
s A S


X
3
i¼1
si ¼ 2
(
)
and
B ¼
s A S


X
5
i¼3
si ¼ 1
(
)
:
(a) List the sample points in each event.
(b) Determine the probability of each event.
(c) What points are in the event A V B?
(d) Verify that Pr½A V B ¼ Pr½A j B Pr½B.
7. Define the events Ck; Bj HS, the sample space in exercise 6, by Ck ¼ fs A S j
P2
i¼1 si ¼ kg, and Bj ¼ fs A S j P5
i¼3 si ¼ jg. Show for all j, k that Ck and Bj are in-
dependent events.
8. An urn contains 20 white, and 30 red balls.
(a) What is the probability of getting 8 or fewer red balls in a draw of 10 balls from
this urn, with replacement? (Hint: Pr½A ¼ 1  Pr½ ~
A.)
338
Chapter 7
Discrete Probability Theory

(b) What is the probability of getting 8 or fewer red balls in a draw of 10 balls from
this urn, without replacement? (Hint: In addition to the part (a) hint, note that while
the individual probabilities associated with getting 9 red and 1 white ball reflect
order, their product does not.)
9. Consider a simultaneous roll of two dice, and a sample space defined as S ¼
fðn1; n2; . . . ; n6Þg, where nj denotes the number of dice showing j dots.
(a) Let X ¼ P6
j¼1 jnj, the total number of dots showing on a roll, and determine the
range of X and associated p.d.f., f ðxjÞ.
(b) Develop a graph of the c.d.f. of X: FðxÞ
10. In the sample space in exercise 9, define Y ¼ P3
j¼1 jnj, and consider the pair of
random variables ðX; YÞ.
(a) Determine the range of ðX; YÞ and associated p.d.f. f ðx; yÞ.
(b) Calculate the marginal p.d.f.s f ðxÞ and f ðyÞ.
(c) Calculate the conditional p.d.f.s f ðx j yÞ and f ðy j xÞ, and confirm the law of
total probability, that f ðxÞ ¼ P
y f ðx j yÞf ðyÞ and f ðyÞ ¼ P
x f ðy j xÞ f ðxÞ.
11. Demonstrate that the two definitions of independence of a collection of random
variables are equivalent where one is framed in terms of independence of pre-image
events in S as in definition 7.32, and the other in terms of joint and marginal proba-
bility distribution functions as in definition 7.34.
12. Given a random variable with moments up to order N, demonstrate that the col-
lections of moments and central moments can each be derived from the other. Specif-
ically, using properties of expectations, show that for n a N:
(a) mn ¼ Pn
j¼0ð1Þnj
n
j
 	
m0
jmnj (Hint: Use the binomial theorem.)
(b) m0
n ¼ Pn
j¼0
n
j
 	
mjmnj (Hint: X ¼ ½X  m þ m.)
13. Given a sample, fxjgn
j¼1, and ^m0
k defined in (7.88), show the following under the
assumption of the existence of the stated moments:
(a) E½ ^m0
k ¼ m0
k
(b) Var½ ^m0
k ¼ 1
n ½m0
2k  ðm0
kÞ2
14. Develop the details for deriving the formulas in (7.99) for the standard binomial
X B
n . Generalize this derivation to the analogously defined general binomial Y B
n ¼
Pn
j¼1 Y B
1j , where
Y B
1 ¼
a;
Pr ¼ p,
b;
Pr ¼ p0.

Exercises
339

15. For the geometric distribution, let m0
m 1 E½ j m ¼ p Py
j¼0 j mð1  pÞ j for m A N
and m b 1, and analogously, m0
0 ¼ 1.
(a) Show that these moments can be produced iteratively by
m0
m ¼ 1  p
p
X
m1
j¼0
m
j


m0
j:
(Hint: Show that for m b 1, Py
j¼1 j mð1  pÞ j ¼ ð1  pÞ½1 þ Py
j¼1ðj þ 1Þmð1  pÞ j,
and use the binomial theorem.)
(b) Derive the mean and variance formulas in (7.103) from part (a).
16. For the Poisson distribution with parameter l, show that:
(a) mP ¼ l (Hint: j l j
j! ¼ l l j1
ð j1Þ! .)
(b) s2
P ¼ l (Hint: j2 l j
j! ¼ lðj  1Þ l j1
ð j1Þ! þ l l j1
ð j1Þ! .)
17. Derive the mean and variance formulas for the aggregate loss model in (7.125)
and (7.126) using a conditioning argument. (Hint: Classes are independent, so derive
for class k by conditioning on Nk. Recall that here, Nk is binomial or Poisson, but it
is not conditional on Nk b 1.)
18. An automobile insurer wants to model claims for collision costs on 10,000 in-
sured automobiles, 2000 ‘‘luxury class’’ and 8000 ‘‘standard class.’’ It estimates that
the annual probability of a collision on any given auto is 0.10 for standard class and
0.06 for luxury class. The average value of insured autos is $25,000 for luxury and
$10,000 for standard. Experience dictates that when an accident occurs, the cost to
repair is uniformly distributed as a percentage of car value, and is 25–75% for lux-
ury, and 50–100% for standard. Total repair costs in the two classes are assumed to
be independent.
(a) Create an individual loss model for the insurer, and with it determine the mean
and variance of repair costs.
(b) Create an aggregate loss model for the insurer using the Poisson distribution, and
with it determine the mean and variance of repair costs.
(Hint: The mean and variance of the uniform distribution equal the limits of these
moments for the discrete rectangular distribution as n ! y. See (7.95) and also
chapter 10.)
19. Demonstrate that the expected value of a life annuity can also be expressed in
terms of the survival function by
340
Chapter 7
Discrete Probability Theory

E½B ¼
X
y
j¼0
v jS Mð jÞ:
20. Calculate E½B and Var½B using a conditioning argument in the following cases:
(a) Let B denote the random variable that equals the present value of annuity pay-
ments that are payable at the end of each year survived for life, but guaranteed pay-
able for a minimum of m years, independent of survival. This is an ‘‘m-year certain
life annuity.’’
(b) Let B denote the random variable that equals the present value of annuity pay-
ments that are only payable for survival up through the end of n years. This is an ‘‘n-
year temporary life annuity.’’
(c) Let B denote the random variable that equals the present value of annuity pay-
ments that are only payable for survival up through the end of n years, but guaran-
teed payable for a minimum of m years, independent of survival, where m < n. This
is an ‘‘m-year certain, n-year temporary life annuity.’’
21. Let B denote the random variable in each of parts (a) through (c) of exercise 20,
but redefined to allow for a k year deferral of benefits. So each annuity is ‘‘k-year
deferred’’ version of the annuity defined above. Consider the case where:
(a) No benefit is paid if death occurs during the first k years.
(b) A benefit of $1 is paid at the end of year of death if death occurs during the first
k years.
(c) Show that the benefit in part (b) equals the benefit in part (a) plus a k year term
life policy from exercise 37(a).
22. Assume that: rF ¼ 0:05, m1 ¼ 0:065, m2 ¼ 0:09, m3 ¼ 0:15, s2
1 ¼ ð0:07Þ2, s2
2 ¼
ð0:12Þ2, s2
3 ¼ ð0:18Þ2, r12 ¼ 0:35, r23 ¼ 0:4, and r13 ¼ 0:25:
(a) Develop formulas for the mean and variance of portfolio returns for an arbitrary
allocation to three risky assets and the risk-free asset.
(b) Define W ¼ ð0:25; 0:25; 0:25; 0:25Þ, and evaluate an epsilon shift between the
risk-free and third risky asset. Graph both E½R03
   E½R and Var½R03
   Var½R as
functions of  for 0:25 a  a 0:25.
23. Generalize the calibration of the growth model for stock prices in (7.136) to de-
velop formulas for u and d for arbitrary p, 0 < p < 1, where p ¼ Pr½u, being explicit
about the binomial probabilities that govern the associated price lattice in (7.138).
(Hint: Proceed as before, showing that with the binomial B defined as in section
7.8.5, and p0 1 1  p, E½B ¼ pu þ p0d and Var½B ¼ pu2 þ p0d 2  ðpu þ p0dÞ2.)
Exercises
341

24. Price a 2-year European call, with strike price of 100, in the ways noted below.
The stock has S0 ¼ 100, and based on time steps of Dt ¼ 0:25 years, the quarterly
log-ratios have been estimated to have mQ ¼ 0:02 and s2
Q ¼ ð0:07Þ2. The annual con-
tinuous risk-free rate is r ¼ 0:048, and so for Dt ¼ 0:25 years, you can assume that
rQ ¼ 0:012.
(a) Develop a real world lattice of quarterly stock prices, with p ¼ 1
2 , and price this
option using (7.147).
(b) Evaluate the two prices of this option at time t ¼ 0:25 from part (a), and con-
struct a replicating portfolio at t ¼ 0 for these prices. Demonstrate that the cost of
this replicating portfolio equals the price obtained in part (a).
(c) Using exercise 23, price this option using (7.147) with the appropriate value of q
based on a lattice for which p ¼ 0:25.
(d) Generate one hundred 2-year paths in the risk-neutral world, each with quarterly
time steps and using the model of part (a). Then estimate the price of this option
using (7.150), by counting how many scenarios end in each stock price at time 2
years.
25. Demonstrate that the conclusion following (7.143), that 0 < q < 1, follows from
ed < er < eu, and that this latter conclusion is demanded by an arbitrage argument.
(Hint: Show that if er a ed or er b eu, then there would be a trade at time 0 that
costs nothing, has no probability of a loss, and a positive probability of a profit
over the period.)
Assignment Exercises
26. Prove the following properties of a probability measure based on the properties
in definition 7.7:
(a) PrðjÞ ¼ 0
(b) If A; B A E, A H B, then PrðAÞ a PrðBÞ. (Hint: Split B into disjoint sets.)
(c) If Aj A E for j ¼ 1; 2; 3; . . . , then Prð6j AjÞ a P PrðAjÞ. (Hint: Split 6j Aj into
disjoint sets.)
(d) If Aj A E for j ¼ 1; 2; 3; . . . , then Prð7j AjÞ a minjfPrðAjÞg. (Hint: 7j Aj H Ak
for all k.)
27. Generalize exercise 2 and confirm that in the sample space S of sequences of n
flips of a fair coin, the event A defined by specifying the values of any m a n out-
comes, contains exactly 100
2m % of the total number of sequences. As before, if you
ignore what happens outside of these m flips, justify explicitly that this is valid.
342
Chapter 7
Discrete Probability Theory

28. Answer exercise 4 in the case of a lottery rather than a bet. (Hint: A lottery is the
same as a bet with di¤erent payo¤s.)
(a) If a gambler buys the lottery ticket for m, and either wins 0 or n, what is the
probability of winning that will make this lottery fair?
(b) If the gambler knows that the probability of a win is p, what ratio of the cost of a
ticket to amount won, m
n from part (a), will make this a fair lottery?
(c) Show that if p is irrational in part (b), a fair lottery requires an irrational value
for m
n . Conclude that since ticket prices and payo¤s must be rational numbers, a lot-
tery with an irrational probability of winning can never be fair.
29. Generalize the event B in exercise 6 to Bj ¼ fs A S j P5
i¼3 si ¼ jg.
(a) What points are in the event A V Bj for all j?
(b) Show that 6 Bj ¼ S.
(c) Confirm the law of total probability, that Pr½A ¼ P
j Pr½A j Bj Pr½Bj.
30. Consider a simultaneous roll of 21 dice, and a sample space defined as S ¼
fðn1; n2; . . . ; n6Þg, where nj denotes the number of dice showing j dots. Develop for-
mulaic or numerical solutions to the following:
(a) What is the probability of the sample point s ¼ ð1; 2; 3; 4; 5; 6Þ?
(b) What is the probability of the event A ¼ fs j n6 ¼ 12 and n3 ¼ 2g? (Hint: Can
this event be defined in terms of ðn3; n6; notherÞ with adjusted probabilities?)
31. Consider a simultaneous flip of 5 unfair coins, Pr½H ¼ 0:3, and a sample space
defined as S ¼ fðn1; n2Þ j n1 denotes the number of Hs, and n2 the number of Tsg.
(a) Let X ¼ 0:01 P2
j¼1 10 jnj, and determine the range of X and associated p.d.f.
f ðxjÞ.
(b) Develop a graph of the c.d.f. of X: FðxÞ.
32. In the sample space in exercise 31, define Y ¼ n1, and consider the pair of ran-
dom variables ðX; YÞ.
(a) Determine the range of ðX; YÞ and associated p.d.f. f ðx; yÞ.
(b) Calculate the marginal p.d.f.s f ðxÞ and f ðyÞ.
(c) Calculate the conditional p.d.f.s f ðx j yÞ and f ðy j xÞ, and confirm the law of
total probability, that f ðxÞ ¼ P
y f ðx j yÞf ðyÞ and f ðyÞ ¼ P
x f ðy j xÞ f ðxÞ.
33. Demonstrate algebraically the iterative formula in (7.16) underlying Pascal’s tri-
angle:
n
m
 
¼
n1
m1


þ
n1
m


.
34. Given a sample fxjgn
j¼1, and ^
MXðtÞ defined in (7.90), show the following under
the assumption of the existence of the stated moments:
Exercises
343

(a) E½ ^
MXðtÞ ¼ MXðtÞ
(b) Var½ ^
MXðtÞ ¼ 1
n ½MXð2tÞ  M 2
XðtÞ
35. Using the 2-variable joint p.d.f. derived for the multinomial distribution and
(7.50), show that for any two components with i 0 j: Cov½Ni; Nj ¼ npipj. (Hint:
First justify:
E½N1N2 ¼
X
n1
n1¼1
X
nn1
n2¼1
n1n2
n!pn1
1 pn2
2 ð1  p1  p2Þnn1n2
n1!n2!ðn  n1  n2Þ!
:
Then split this summation as the product
X
n1
n1¼1
n1
n!pn1
1 ð1  p1Þnn1
n1!ðn  n1Þ!

X
nn1
n2¼1
n2
ðn  n1Þ!
n2!ðn  n1  n2Þ!
p2
1  p1

n2
1  p1  p2
1  p1

nn1n2
;
and note that this second summation is E½n2 with a certain binomial distribution.
Alternatively, start with the double summation above, simplify
n1n2
n1!n2! , and look for
the binomial theorem.)
36. A bond portfolio quantitative analyst wants to model credit losses on a $750 mil-
lion portfolio, which includes three classes of credit risk: $250 million ‘‘low risk,’’
$350 million ‘‘medium risk,’’ and $150 million ‘‘high risk,’’ where in each class the
manager has maintained a $5 million average par investment exposure per credit.
Annual default probabilities are 0.002, 0.009, and 0.025. Experience dictates that
when a default occurs, the loss is uniformly distributed as a percentage of par value,
and is 25–50% for low risk, 25–75% for medium risk, and 50–100% for high risk.
Total credit losses in the three classes are assumed to be independent.
(a) Create an individual loss model for the analyst, and with it determine the mean
and variance of credit losses.
(b) Create an aggregate loss model for the analyst using the Poisson distribution,
and with it determine the mean and variance of credit losses.
(Hint: The mean and variance of the uniform distribution equal the limits of these
moments for the discrete rectangular distribution as n ! y. See (7.95) and also
chapter 10.)
37. Calculate E½In and Var½In using a conditioning argument in the following cases:
(a) Let In denote the random variable which equals the present value of a life insur-
ance payment at the end of the year of death, but where a payment is made only if
death occurs in the first n years. This is an ‘‘n-year term insurance’’ contract.
344
Chapter 7
Discrete Probability Theory

(b) Let In denote the random variable that equals the present value of a life insur-
ance payment at the end of the year of death if death occurs in the first n years, or a
payment of $1 at time t ¼ n if the individual survives the n years. This is an ‘‘n-year
endowment’’ contract.
38. Assuming that: rF ¼ 0:03, m1 ¼ 0:095, m2 ¼ 0:19, m3 ¼ 0:15, s2
1 ¼ ð0:12Þ2,
s2
2 ¼ ð0:25Þ2, s2
3 ¼ ð0:18Þ2, r12 ¼ 0:55, r23 ¼ 0:4, and r13 ¼ 0:20:
(a) Develop formulas for the mean and variance of portfolio returns for an arbitrary
allocation to three risky assets and the risk-free asset.
(b) Define W ¼ ð0:25; 0:25; 0:25; 0:25Þ, and evaluate an epsilon shift between the sec-
ond and third risky asset. Graph both E½R23
   E½R and Var½R23
   Var½R as func-
tions of  for 0:25 a  a 0:25.
39. Prove the formula in (7.147) using mathematical induction. (Hint: The formula is
proved for n ¼ 1; 2 already. Assume it to be true for n, and show it is true for n þ 1
by applying the assumed formula to the two values of the option at time 1, LðS u
1 Þ
and LðS d
1 Þ. Recall exercise 33.)
40. Price a 2-year European put, with strike price of 100, in the ways noted below.
The stock has S0 ¼ 100, and based on time steps of Dt ¼ 0:25 years, the quarterly
log-ratios have been estimated to have mQ ¼ 0:025, and s2
Q ¼ ð0:09Þ2. The annual
continuous risk-free rate is r ¼ 0:06, and so for Dt ¼ 0:25 years you can assume that
rQ ¼ 0:015.
(a) Develop a real world quarterly lattice of stock prices, with p ¼ 1
2 , and price this
option using (7.147).
(b) Evaluate the two prices of this option at time t ¼ 0:25 from part (a), and con-
struct a replicating portfolio at t ¼ 0 for these prices. Demonstrate that the cost of
this replicating portfolio equals the price obtained in part (a).
(c) Using exercise 23, price this option using (7.147) with the appropriate value of q
based on a lattice for which p ¼ 0:35.
(d) Generate one hundred 2-year paths in the risk-neutral world, each with quarterly
time steps and using the model of part (a), and estimate the price of this option using
(7.150), by counting how many scenarios end in each stock price at time 2 years.
41. Using (7.147), if LC
0 and LP
0 denote the t ¼ 0 prices of European call and put
options, respectively, both with a strike price of K and maturity of T, show that
these prices satisfy put-call parity:
LC
0 þ KerT ¼ LP
0 þ S0;
ð7:151Þ
where r denotes the risk-free rate in units of T.
Exercises
345



## Fundamental Probability Theorems

8 Fundamental Probability Theorems
In this chapter is introduced several of the very important theorems from probability
theory. Although a number of these results are somewhat challenging to demon-
strate, they all have a great many applications. This is due to the great generality of
the conclusions and the relatively minimal assumptions needed to produce them.
8.1
Uniqueness of the m.g.f. and c.f.
In this section we demonstrate a limited version of the result quoted in chapter 7,
that if CXðtÞ ¼ CYðtÞ or MXðtÞ ¼ MYðtÞ for discrete random variables X and Y,
and for some open interval I, containing 0, then the probability density functions
are equal: fXðxÞ ¼ gYðxÞ. The narrower version of this result contemplated here
assumes that these random variable have finite ranges. This result can be shown to
be true in a more general context than finite discrete p.d.f.s, or even discrete p.d.f.s,
but requires the tools of real analysis and complex analysis.
Proposition 8.1
Let X and Y be finite discrete random variables with associated
probability functions f ðxÞ and gðyÞ, and respective domains of fxign
i¼1 and fyjgm
j¼1,
arranged in increasing order. If either CXðtÞ ¼ CYðtÞ or MXðtÞ ¼ MYðtÞ for t A I,
where I is an open interval containing 0, then m ¼ n, xi ¼ yi, and f ðxiÞ ¼ gðyiÞ for
all i.
Proof
If MXðtÞ ¼ MYðtÞ for t A I, then P etxif ðxiÞ ¼ P etyigðyiÞ. Consequently
there are collections of real numbers fakg and fbkg, where the fbkg are all distinct,
so that
X
N
k¼1
aketbk ¼ 0
for t A I:
ð8:1Þ
In other words, for cases where xi ¼ yj for some i and j, ak ¼ f ðxiÞ  gðyjÞ and
bk ¼ xi ¼ yj. In all other cases, ak is either an f ðxiÞ or a gðyjÞ term, and the associ-
ated bk is xi, respectively yj. We now show that if (8.1) holds, then ak ¼ 0 for all k.
This provides the result, since it means that for any xi ¼ yj, it must be the case that
f ðxiÞ ¼ gðyjÞ, whereas for any xi or yj with no ‘‘match,’’ f ðxiÞ ¼ 0 or gðyjÞ ¼ 0, re-
spectively. The proof proceeds by induction on N. The result is apparently true for
N ¼ 1, since a1etb1 ¼ 0 for t A I clearly implies that a1 ¼ 0. This result is also appar-
ent for N ¼ 2, since in this case it is concluded that a2etðb2b1Þ ¼ a1, but this is impos-
sible unless a1 ¼ a2 ¼ 0, since b2  b1 0 0. Assume next that the result holds for N,
and that we seek to demonstrate the result for N þ 1. Now PNþ1
k¼1 aketbk ¼ 0 implies
that PN
k¼1 aketck ¼ aNþ1 for t A I, where ck ¼ bk  bNþ1, and fckg are all distinct
and, importantly, all nonzero, since the fbkg are all distinct by assumption. Now, if

s; t A I, this equation implies that PN
k¼1 aketck ¼ PN
k¼1 akesck. This result can then be
expressed as follows if s 0 t:
X
N
k¼1
akesck eðtsÞck  1
t  s


¼ 0:
Now from (7.63) note that eðtsÞck 1
ts
¼ ck þ ðt  sÞ
c2
k
2 þ Xk
h
i
, where Xk is an absolutely
convergent summation of terms, all of which contain positive powers of ðt  sÞ. Con-
sequently, using the identities above obtains
X
N
k¼1
akckesck ¼
X
N
k¼1
ak ck  eðtsÞck  1
t  s


esck
¼ ðt  sÞ
X
N
k¼1
ak
c2
k
2 þ Xk


:
Now as t ! s, since each Xk ! 0 as noted above, we conclude that
X
N
k¼1
akckesck ¼ 0:
From the induction step for N we conclude that akck ¼ 0 for 1 a k a N, and since
ck 0 0, it must be the case that ak ¼ 0 for 1 a k a N. Finally, this implies that
aNþ1 ¼ 0 by substitution. To extend this proof to characteristic functions is immedi-
ate, with one subtlety, and that is the applicability of (7.63) to an exponential of the
form eix, where i ¼
ffiffiffiffiffiffi
1
p
and x A R. In this case the resulting power series is again
seen to be absolutely convergent by the ratio test, and this series is equal to eix be-
cause that is how eix is defined!
n
Remark 8.2
The proof above cannot be adapted to a countably infinite discrete prob-
ability function, and for that case an entirely di¤erent approach is needed, requiring a
new and advanced set of tools. These tools will also handle this result for p.d.f.s that are
not discrete. The problem is that while we could again conclude (8.1) with N ¼ y, and
the trick employed above adapted, this would only yield
X
y
k¼2
akckesck ¼ 0;
which provides no real simplification.
348
Chapter 8
Fundamental Probability Theorems

8.2
Chebyshev’s Inequality
Chebyshev’s inequality, sometimes spelled as Chebychev or Tchebyshe¤, applies to
any probability density function that has a mean and variance, and hence it is quite
generally applicable. It is named for its discoverer, Pafnuty Chebyshev (1821–1894).
Chebyshev was a Russian mathematician, and hence the many transliterations of his
name in English.
This inequality can be stated in many ways, and Chebyshev is actually a name
now given to a family of inequalities as will be seen below. But this inequality is often
applied as stated in the following proposition, when we are interested in an upper
bound for the probability of the random variable being far from its mean, where
‘‘far’’ is measured in two common ways. Although the Chebyshev inequalities are
stated here for discrete f ðxÞ, it is an easy exercise to generalize these to continuous
f ðxÞ using the tools of chapter 10.
Proposition 8.3 (Chebyshev’s inequality)
If f ðxÞ is a discrete probability function
with mean m and variance s2, then for any real number t > 0,
Pr½jX  mj b ts a 1
t2 :
ð8:2Þ
Equivalently,
Pr½jX  mj b s a s2
s2 :
ð8:3Þ
Proof
By definition, s2 ¼ P
xiðxi  mÞ2f ðxiÞ b P
jximjbtsðxi  mÞ2f ðxiÞ. In other
words, in this last summation, only the xi terms that satisfy jxi  mj b ts are
included.
This
second
summation
now
satisfies
P
jximjbtsðxi  mÞ2f ðxiÞ b
ðtsÞ2 P
jximjbts f ðxiÞ, and this last summation is seen to equal Pr½jX  mj b ts.
Combining the inequalities and dividing by s2 provides the first result. The second
result is implied by the first with the substitution t ¼ s
s .
n
Note that for any t with t a 1, this inequality provides no real limit on the associ-
ated probability, since in such a case, 1
t2 b 1. However, using integral multiples of the
standard deviation we obtain
Pr½jX  mj b 2s a 1
4 ¼ 0:25;
Pr½jX  mj b 3s a 1
9 A0:11;
8.2
Chebyshev’s Inequality
349

Pr½jX  mj b 4s a 1
16 A0:06;
and so forth.
For example, if X B has the binomial distribution with parameters n and p, then
Pr½jX B  npj b s a npð1  pÞ
s2
:
Similarly, for the negative binomial distribution with parameters p and k, we con-
clude that
Pr
X P  kð1  pÞ
p


b s


a kð1  pÞ
s2p2
:
This inequality can be generalized in many ways. For example, an estimate of a
probability of the form Pr½jXj b s can be made with the same formula, except with
m0
2 used instead of s2 ¼ m2. The proof above also readily applies to the case of m2n for
any n, which then bounds the associated probabilities in terms of higher order central
moments. In the case of odd central moments the proof only works when absolute
values are introduced. We state the generalization in the form of absolute values,
though the absolute value is redundant for even moments.
Proposition 8.4
If f ðxÞ is a discrete probability function, with mean m and absolute
central moment mjnj 1 E½jX  mjn for n b 1, then for any real number t > 0,
Pr½jX  mj b t a
mjnj
tn :
ð8:4Þ
Proof
By definition,
mjnj ¼
X
xi
jxi  mjnf ðxiÞ b
X
jximjbt
jxi  mjnf ðxiÞ b tn Pr½jX  mj b t;
and the result follows by division.
n
Once again, probabilities of the form Pr½jXj b t can be bounded by the corre-
sponding formula, with m0
jnj 1 E½jXjn. In this case, if the random variable has its
range in the nonnegative real numbers, these estimates apply without the absolute
values, that is, by using the moments m0
n directly.
In exercise 1 is assigned the development of a probability estimate utilizing the
moment-generating function MXðtÞ.
350
Chapter 8
Fundamental Probability Theorems

Remark 8.5
1. Note that when n ¼ 1, the inequality in (8.4) restated in terms of m0
j1j 1 E½jXj is
known as Markov’s inequality, named for Andrey Markov (1856–1922), a student of
Chebyshev. In other words,
Pr½jXj b t a E½jXj
t
:
ð8:5Þ
2. Note also that if f ðxÞ is a p.d.f. with mjnj ¼ 0 for some n b 1, then it must be the
case that Pr½X ¼ m ¼ 1. In other words, the random variable X assumes only the value
m. This is because in (8.4) the inequality states that Pr½jX  mj b t a 0 for any t > 0,
but since probabilities are nonnegative, we conclude that Pr½jX  mj b t ¼ 0 for any
t > 0 and therefore Pr½X ¼ m ¼ 1. Such a random variable is referred to as a degener-
ate random variable, and the associated p.d.f., a degenerate probability density, with no
insult intended.
There is also a one-sided version of the Chebyshev inequality that is useful when
the focus of the investigation is on one and not both tails of the distribution. For in-
stance, if we are modeling losses in a credit portfolio, we are interested in the proba-
bility of losses being large and positive relative to expected losses, and not so much
interested in the probability that losses could be either large or small relative to this
expected value. The following result gives a better bound than (8.3) in this case, and
the amount of improvement grows with s2:
Proposition 8.6 (Chebyshev’s One-Sided Inequality)
If f ðxÞ is a discrete probability
function, with mean m and variance s2, then for any real number s > 0,
Pr½X  m b s a
s2
s2 þ s2 :
ð8:6Þ
Proof
For any value of t, we have
Pr½X  m b s ¼ Pr½X  m þ t b s þ t a Pr½ðX  m þ tÞ2 b ðs þ tÞ2:
This is because the last probability statement also encompasses Pr½ðX  m þ tÞ a
ðs þ tÞ. Now, by the Markov inequality in (8.5) and a little algebra,
Pr½ðX  m þ tÞ2 b ðs þ tÞ2 a E½ðX  m þ tÞ2
ðs þ tÞ2
¼ s2 þ t2
ðs þ tÞ2 :
Summarizing we obtain
8.2
Chebyshev’s Inequality
351

Pr½X  m b s a s2 þ t2
ðs þ tÞ2
for any t > 0:
Since t can be chosen arbitrarily, we do so to make the bound s2þt2
ðsþtÞ2 as small as pos-
sible. Using the methods of calculus discussed in chapter 9, we find the value of t that
minimizes this bound to be t ¼ s2
s , and a substitution demonstrates that this produces
the bound in (8.6).
n
This one-sided inequality can also be expressed in units of the variance as in (8.2)
as follows:
Pr½X  m b ts a
1
t2 þ 1 :
ð8:7Þ
8.3
Weak Law of Large Numbers
The so-called weak law of large numbers is actually a very powerful and general re-
sult with wide applicability but with the misfortune to be a relative of an even more
general result, known as the strong law of large numbers. Like the Chebyshev in-
equality, it has the power of being applicable to virtually any probability distribu-
tion. Unlike the Chebyshev inequality, which requires that these distributions have
both a mean and variance, the weak law requires only the existence of the first mo-
ment, but it is far easier to prove when the variance also exists.
Before giving its statement, recall that if a random variable X is defined on a dis-
crete sample space S, then a random sample of size n of this random variable can be
associated with a sample point in the n-trial sample space, denoted S n, with probabil-
ity structure defined in (7.7). The components of this sample point are then called in-
dependent and identically distributed (i.i.d.) random variables.
Proposition 8.7 (Weak Law of Large Numbers)
For any n, let fXign
i¼1 be indepen-
dent and identically distributed random variables with common mean m. Define the ran-
dom variable ^X as the average, ^X ¼ 1
n
Pn
i¼1 Xi. Then for any  > 0:
Pr½j ^X  mj >  ! 0
as n ! y:
ð8:8Þ
Remark 8.8
Note that if fXign
i¼1 are defined on the discrete sample space S, then ^X is
a random variable defined on the n-trial sample space S n. The formal meaning of the
statement in (8.8) is that for any fixed  > 0, the events V n
 HS n in the n-trial sample
spaces S n, defined by
352
Chapter 8
Fundamental Probability Theorems

V n
 ¼ fðX1; . . . ; XnÞ j j ^X  mj > g;
satisfy Pr½V n
  ! 0 as n ! y.
The intuitive meaning of the statement in (8.8) can be described as follows: Suppose
that for any n we can easily generate as many samples fXign
i¼1 as desired, and for each
sample calculate the associated sample average ^X. On the real line we then plot the
collection of averages and determine the proportion of these that are outside the inter-
val ½m  ; m þ . The weak law asserts that for any  > 0, the proportion of sample
averages outside this interval converges to 0 as n ! y. In general, the weak law pro-
vides no information on the speed at which this proportion converges, but see below the
case where X also has a finite variance.
Proof
We prove this result in two cases. In applications the first case is often
satisfied.
1. If the random variable X also has a variance s2, the weak law is an immediate
consequence of Chebyshev’s inequality and the formulas above for sample moments.
As developed in (7.78) and (7.79), we have E½ ^X ¼ m, and Var½ ^X ¼ s2
n , which when
substituted into (8.3) provides the result
Pr½j ^X  mj >  a s2
n2 :
ð8:9Þ
This implies more than (8.8), and assures that this probability converges to 0 with a
rate at least as fast as c
n for c ¼ s2
2 .
2. In the general case we introduce the method of truncation, whereby, for each n and
arbitrary but fixed l > 0, the collection fXign
i¼1 is truncated and split as
Yi ¼
Xi  m;
jXi  mj a ln;
0;
jXi  mj > ln;

Zi ¼
0;
jXi  mj a ln;
Xi  m;
jXi  mj > ln:

So Xi  m ¼ Yi þ Zi. Now with ^Y and ^Z defined as the associated averages, note
that (see exercise 15)
Pr½j ^X  mj >  a Pr j ^Yj > 
2


þ Pr j ^Zj > 
2


:
8.3
Weak Law of Large Numbers
353

The weak law follows if it can be shown that for some l > 0, the two probabilities on
the right can be made as small as desired. For the first probability, note that since
jY1j a ln,
E½ðY1Þ2 a lnE½jY1j < lnmj1j;
where mj1j ¼ E½jX1  mj. Now fYign
i¼1 are independent because of the independence
of fXign
i¼1, and
Var½ ^Y ¼ 1
n Var½Y1 a 1
n E½ðY1Þ2 < lmj1j:
Then by Chebyshev’s inequality,
Pr j ^Y  E½ ^Yj > 
2


a
4lmj1j
2
:
But E½ ^Y ! E½ ^X  m ¼ 0 as n ! y. So by choosing l small, we can make
Pr j ^Yj > 
2


as small as desired for any  as n ! y.
For the second probability, we show that Pr½j ^Zj > 0 ! 0 as n ! y for any l.
By a consideration of the associated events and the independence of fZign
i¼1, we
write
Pr½j ^Zj > 0 a
X
Pr½jZij > 0 ¼ n Pr½jZ1j > 0:
But, by definition,
Pr½jZ1j > 0 ¼ Pr½jXi  mj > ln
¼
X
jximj>ln
f ðxiÞ
a 1
ln
X
jximj>ln
jxi  mj f ðxiÞ:
Then, combining, we have
Pr½j ^Zj > 0 a 1
l
X
jximj>ln
jxi  mj f ðxiÞ;
which converges to 0 for any l as n ! y.
n
354
Chapter 8
Fundamental Probability Theorems

In the common application to a random variable with mean and variance, this law
also provides a lower bound for the probability that the estimate will be close to the
expected value. In other words, if m and s2 exist, then
Pr½j ^X  mj a  > 1  s2
n2 ;
ð8:10Þ
which is only useful, of course, when s2
n2 a 1 or  b
sffiffin
p . In the general case all that
can be said is that
Pr½j ^X  mj a  ! 1
as n ! y:
ð8:11Þ
The formulation in (8.10) can then be understood in the context of providing a
general confidence interval for the theoretical mean m, which we may be interested in
estimating using a sample mean ^X. Specifically, define the closed interval I by
I 1 ½ ^X  ; ^X þ :
ð8:12Þ
Then the weak law of large numbers says that if fXign
i¼1 are independent and identi-
cally distributed random variables with common mean m and variance s2, then
Pr½m A I > 1  s2
n2 :
ð8:13Þ
To be clear, in any given application with sample statistic ^X, it will be the case that
either m A I or m B I. The probability statement in (8.13) needs to be interpreted in
the context of n-trial sample space S n. Specifically, for ðX1; X2; . . . ; XnÞ A S n, let
^X ¼ 1
n
Pn
i¼1 Xi, and define the event f
V n

V n
 A E, the complement in S n of the event in re-
mark 8.8 above, by
f
V n

V n
 1 fðX1; X2; . . . ; XnÞ A S n j m A ½ ^X  ; ^X þ g;
where m is the mean of the random variable X. Then (8.13) states that for any  > 0,
Pr
h
f
V n

V n

i
> 1  s2
n2 ;
ð8:14Þ
where s2 is the variance of X.
The weak law, with exactly the same proof and interpretations, applies to all of
the sample moment estimates developed earlier, since all that was assumed in the
proof above was that ^X is a random variable defined on n-trial sample space S n and
8.3
Weak Law of Large Numbers
355

that the m and s2 in (8.9) are, respectively, the mean and variance of this random
variable.
Example 8.9
With ^s2 ¼
1
n1
Pn
j¼1ðXj  ^XÞ2, the unbiased variance estimator, since
E½^s2 ¼ s2, we have that for any random sample of size n,
Pr½j^s2  s2j >  a ðn  1Þm4  ðn  3Þs4
nðn  1Þ2
;
where the upper bound for this probability reflects Var½^s2. For higher moments, with
higher moment estimators defined by ^m0
k ¼ 1
n
Pn
j¼1 X k
j , we have that for any random
sample of size n,
Pr½j^m0
k  m0
kj >  a m0
2k  ðm0
kÞ2
n2
:
Here again it is used that E½ ^m0
k ¼ m0
k, and the upper bound for this probability reflects
Var½ ^m0
k.
The critical observation on all these probability estimates is that each probability
is proportional to 1
n , which is favorable as we can select n ! y, but is also propor-
tional to
1
2 , which is unfavorable if we desire to have  ! 0. But for any desired
margin of error , we can use these formulas to determine how large the sample size
n needs to be so that the sample estimator will be within that margin of error with
any probability that is desired.
Example 8.10
To estimate the parameter l ¼ E½XP for a Poisson distribution, the
statement above produces
Pr½j ^X  lj >  a l
n2 ;
which is initially a bit of a problem due to the presence of the unknown l ¼ VarðXPÞ
in the probability upper bound. However, it is commonly the case that a crude upper
bound can be used successfully. For example, if a given sample produced ^X ¼ 3, we
might be comfortable assuming l a 5, and hence the probability statement above
becomes
Pr½j ^X  lj >  a 5
n2 :
356
Chapter 8
Fundamental Probability Theorems

In order to have 1 decimal point accuracy on the estimate for l, we choose  ¼ 0:05 and
derive
Pr½j ^X  lj > 0:05 a 2000
n
;
from which, with n ¼ 200;000, a random sample will have less than a 1% probability of
producing an error in the first decimal place. Of course, if a smaller upper bound is
assumed for l, and/or a lower level of confidence desired, smaller samples will su‰ce.
Remark 8.11
This example reflects a practical constraint on the use of the weak law
in empirical estimates. While this law provided a calculation of n ¼ 200;000 to achieve
the desired result, most statisticians would agree that this is an enormous sample, and
almost certainly a sample size that is far bigger than what is truly needed. The problem
is that the empirical weakness of this law is caused by its theoretical strength. Specifi-
cally, this law applies to every random variable that has a finite mean, or in the appli-
cations above, every random variable with finite mean and variance. Because of this
generality, it would be unlikely that the formula provided would be e‰cient empirically
when applied to any given random variable, which in many cases will have many more
finite moments than the law requires. Consequently the weak law tends to be applied far
more often in theoretical estimates than in empirical estimations.
8.4
Strong Law of Large Numbers
The weak law of large numbers makes a statement about every n-trial sample space
S n associated with a random variable X with mean m. Specifically, this law asserts
that for any  > 0 the random variable ^X ¼ 1
n
Pn
i¼1 Xi with i.i.d. fXign
i¼1, ‘‘splits’’
this sample space into the event V n
 , of those sample points that are far from the
mean in that j ^X  mj > , and the event f
V n

V n
 , of those sample points that are close to
the mean in that j ^X  mj a .
If we fix  and assume that X has variance s2, the event V n
 has probability no
more than s2
n2 , which goes to 0, and event f
V n

V n
 has probability greater than 1  s2
n2 ,
which goes to 1, both as n ! y. Without the assumption of the existence of s2, the
same conclusions hold but without the information on rate of convergence.
Alternatively, for a fixed n, attempting to let  ! 0 in the case of finite variance
provides ine¤ective probability bounds in that the event V n
 has probability bounded
above by a quantity that goes to y mathematically but to 1 logically. Likewise f
V n

V n

has probability bounded below by a quantity that goes to y mathematically but to
0 logically.
8.4
Strong Law of Large Numbers
357

On the other hand, if we choose  ! 0 carefully, say n ¼ n½að1=2Þ for 0 < a < 1
2 ,
then we can simultaneously have that the probability of V n
n goes to zero as n ! y,
and the error tolerance n goes to zero. That is, with ^Xn denoting the sample mean
random variable in S n, and m the corresponding theoretical mean, we obtain that as
n ! y,
Pr½j ^Xn  mj > n½að1=2Þ a s2
n2a ! 0:
We formalize this in a proposition.
Proposition 8.12
Let S be a sample space and fXign
i¼1 independent, identically dis-
tributed with mean m and variance s2. If ^Xn ¼ 1
n
Pn
i¼1 Xi denotes the average as a ran-
dom variable in S n, and V n
 HS n is defined by
V n
 ¼ fðX1; . . . ; XnÞ j j ^Xn  mj > g;
then there is a sequence n ! 0 so that
Pr½V n
n ! 0
as n ! y;
and correspondingly
Pr
 f
V n
n
V n
n

! 1
as n ! y:
Proof
Choose n ¼ n½að1=2Þ where 0 < a < 1
2 , and apply the weak law of large
numbers.
n
Since this result gives that Pr
h
f
V n

V n

i
! 1 as n ! y, it would be tempting to make
the bold assertion that Pr½ ^Xn ! m ¼ 1 as n ! y. But the proposition above is silent
on the connection between the terms of any such sequence f ^Xng. Each sequential ^Xn
term could be generated in at least one of two ways:
1. Model 1
Each sequential ^Xn term is generated and independent of the sample
points that are chosen for ^Xj with j < n, meaning that for each n a new independent
sample ðX1; X2; . . . ; XnÞ A S n is produced.
2. Model 2
Each sequential
^Xn term is generated but dependent on the sam-
ple points that are chosen for ^Xj with j < n, so that ^Xnþ1 is defined with the same
points as ^Xn, which is ðX1; X2; . . . ; XnÞ, plus a new and independent sample point
Xnþ1.
358
Chapter 8
Fundamental Probability Theorems

The proposition above on the events V n
 gives no apparent statement on which
model if either would allow the conclusion that Pr½ ^Xn ! m ¼ 1 as n ! y. This
proposition simply provides a statement about the probabilities of events defined in
the sequential sample spaces S n and confirms that these successive probabilities con-
verge to 1. In either of these models of how f ^Xngy
n¼1 might be generated, we do not
have a sample space with an associated probability structure, within which the collec-
tion f ^Xngy
n¼1 can be measured.
To better understand this point, we pursue these models in more detail. We will
then see that model 2 is the model underlying the strong law of large numbers, and
that this result is able to finesse a conclusion of Pr½ ^Xn ! m ¼ 1 as n ! y, without
the explicit construction of a probability space in which f ^Xngy
n¼1 can be measured.
8.4.1
Model 1: Independent { ^Xn}
Intuitively for model 1 we need an ‘‘infinite product’’ sample space:
S ðyÞ 1S  S 2  S 3  S 4     ;
where each S n denotes the n-trial sample space of sample points Xn 1 ðX1; X2; . . . ;
XnÞ and associated probability structure on which the random variable ^Xn ¼ 1
n
P Xj
is defined. The probability structures of the S n would then need to be combined to a
probability measure on this infinite product space in a way that is analogous to how
the probability structure of S n 1S  S  S  S      S (n-times) was defined rela-
tive to the probability measure Pr on S. For any finite product SðMÞ ¼ S  S 2  S 3 
S 4      S M, this sample space would be an example of a generalized M-trial sam-
ple space introduced in section 7.2.7, but for this model, this earlier construction
must be generalized further to M ¼ y.
The sequence f ^Xngy
n¼1 could then be defined in terms of a sample point in this
product space ðX1; X2; . . . ; Xn; . . .Þ, and the assertion Pr½ ^Xn ! m ¼ 1 would have
meaning. Namely Pr½ ^Xn ! m ¼ 1 would mean that Pr½A ¼ 1, where the event
A HSðyÞ is defined as the collection of all sequences that so converge:
A 1 fðX1; X2; . . . ; Xn; . . .Þ j ^Xn ! mg;
where each ^Xn is defined relative to the components of Xn.
Alternatively, to attempt to avoid the construction of this sample space, let’s recall
the definition of limit. The statement ^Xn ! m means that for any  > 0 there is an in-
teger N so that j ^Xn  mj <  for n b N. We could say that within this model, the ex-
pression Pr½ ^Xn ! m is defined as the probability that for any  > 0 there is an integer
N so that j ^Xn  mj <  for n b N.
8.4
Strong Law of Large Numbers
359

Now by the weak law of large numbers, applied to the case where X has a finite
variance, we know from (8.10) that for a given n this probability is greater than or
equal to 1  s2
n2 . In other words,
Pr½j ^Xn  mj <  b 1  s2
n2


:
So by independence,
Pr½j ^Xn  mj <  for n b N ¼
Y
y
n¼N
½Prj ^Xn  mj < 
b
Y
y
n¼N
1  s2
n2


:
Unfortunately, this leads to a dead end. Although beyond the tools we have devel-
oped so far the theory of infinite products is well developed in mathematics. As it
turns out, the convergence of this infinite product to a number greater than 0 is re-
lated to the absolute convergence of the series
s2
n2
n
o
. Specifically, it will be shown in
chapter 9 that given fxngy
n¼1 with xn > 0 and xn ! 0 as n ! y,
Y
y
n¼1
ð1  xnÞ ¼
0;
if P xn diverges,
c > 0;
if P xn converges.

Of course here xn is a multiple of the harmonic series, and we know from chapter 6
that P xn diverges. This implies that this infinite product has value 0 independent of
N. In other words, we can only conclude what was obvious without any work, that
in model 1, for any  > 0 and any N,
Pr½j ^Xn  mj <  for n b N b 0:
Equivalently, all that can be derived from the weak law is that
Pr½ ^Xn ! m b 0;
which is not a very deep insight.
8.4.2
Model 2: Dependent { ^Xn}
In the second model for how f ^Xngy
n¼1 might be generated, we need a di¤erent sample
space, one that is in e¤ect the countably infinite version of S n,
360
Chapter 8
Fundamental Probability Theorems

S y 1S  S  S  S     ;
with appropriate probability structure so that a sample point of the form ðX1; X2; . . . ;
Xn; . . .Þ
can
be
selected,
and
associated
sample
mean
sequence
f ^Xngy
n¼1 1
1
n
Pn
j¼1 Xj
n
oy
n¼1 defined. Within such a space we could then define the event A HSy
as the collection of all sequences ðX1; X2; . . . ; Xn; . . .Þ A Sy with associated mean se-
quences that satisfies ^Xn ! m. Then the statement that Pr½ ^Xn ! m ¼ 1 would mean
that Pr½A ¼ 1, where
A 1 fðX1; X2; . . . ; Xn; . . .Þ A S y j ^Xn ! mg:
The construction of this sample space would seem to be easy. We simply assert
that
S y 1 fðX1; X2; . . . ; Xn; . . .Þ j Xj A S for all jg:
The hard part, however, is the imposition of a probability measure. What is easy to
demonstrate is that any attempt to generalize from (7.8) is hopeless. To attempt to
define a probability function on Sy by Py½ðs1; s2; . . .Þ ¼ Qy
j¼1 PrðsjÞ provides the
immediate conclusion that Py½ðs1; s2; . . .Þ ¼ 0 for all ðs1; s2; . . .Þ A S y. Specifically,
if ðs1; s2; . . .Þ is any sample point, then in any nondegenerate space S it will be the
case that Pr½sj a p < 1 for all j, and so QN
j¼1 PrðsjÞ < pN, which converges to 0 as
N ! y. The only counterexample to this conclusion is for a degenerate probability
space S ¼ fsg with one point in which Pr½s ¼ 1. So another definitional approach is
needed.
But any such approach will have to abandon the idea that sample points have non-
zero probabilities since it can never be the case that such an Sy will be countable.
Indeed, even for the simplest nondegenerate space, S 1 f0; 1g underlying the stan-
dard binomial, Sy so defined contains the equivalent of the base-2 expansions of all
real numbers in the interval ½0; 1 and hence is an uncountably infinite space. Assign-
ing nonzero probabilities to an uncountable collection of sample points with the hope
that these probabilities will add up to 1 is then doomed at the start. Why?
Because from the Cantor diagonalization approach in chapter 2, we know that
every summation of the probabilities of sample points will of necessity omit many
points, and hence any such sum must be unbounded and hence infinite. The only pos-
sible solution is to somehow identify a countable subcollection of points within
S y, assign nonzero probabilities, and simply declare all other sample points to have
probability 0. But since S y is truly uncountable, it is clear that using such a construc-
tion to conclude that Pr½ ^Xn ! m ¼ 1 would not answer the original question.
8.4
Strong Law of Large Numbers
361

So another big idea is needed, but we do not have the necessary tools for such a
product space with methods of this chapter. We will begin work on that big idea
somewhat in chapter 10, which will address continuous probability theory, but the
complete theory requires the tools of real analysis. It turns out that the strong law
of large numbers addresses the desired result, produces a strong assertion, and avoids
the construction of this infinite dimensional space. It addresses the sequence f ^Xngy
n¼1,
which is defined in terms of a given sequence of independent X sample points
fXjgy
j¼1 HS, without constructing the sample space Sy. But, if the strong law
assures the conclusion that Pr½ ^Xn ! m ¼ 1, without the space Sy, what exactly
does this conclusion mean?
8.4.3
The Strong Law Approach
The approach taken in the strong law of large numbers will be to strengthen the con-
clusion above, where it was shown that when s2 exists, there exists n ! 0 so that the
events
V n
n 1 fðX1; . . . ; XnÞ j j ^Xn  mj > ng HS n
satisfy pn 1 Pr½V n
n ! 0 as n ! y. The idea was to choose n ¼ nað1=2Þ, 0 < a < 1
2 .
While this result is meaningful, these probabilities do not converge to 0 very
quickly. Indeed there is no N for which Py
n¼N pn < y, since pn ¼ s2
n2a , where 0 <
2a < 1. In other words, the probabilities pn ! 0 slower than the terms of the har-
monic series, which we have seen does not converge. This is important because
Py
n¼N pn ¼ Py
n¼N Pr½V n
n. So if this summation could be made to converge, it would
mean we could make this summation of probabilities as small as we want by choos-
ing N big enough, and below we will see that this is enough to provide the desired
conclusion in a logical way.
The problem of slow convergence is only partially caused by the goal of having the
error tolerance, n ¼ nað1=2Þ, also converge to 0 as n increases. Even for fixed  > 0
we have seen from the weak law of large numbers that pn 1 Pr½V n
  ¼ s2
n2 by (8.9).
While pn ! 0 as n ! y, there again is no N so that Py
n¼N pn < y. In other words,
the best we can assert on the basis of the weak law is that for fixed  > 0, these prob-
abilities decrease to 0 no faster than 1
n for a random collection f ^Xng.
The strong law of large numbers will apply to a collection of random variables
fXngy
n¼1 defined on S and the associated sample mean sequence
^Xn 1 1
n
X
n
j¼1
Xj:
362
Chapter 8
Fundamental Probability Theorems

It will improve the results above in two ways:
1. The collection fXngy
n¼1 must be independent but need not be identically distrib-
uted. However, if not i.i.d., the collection of variances, fs2
i g must not grow too fast
with i.
2. It will be shown that with ^mk 1 1
k
Pk
j¼1 mj, then for any  > 0,
X
y
n¼1
pn < y;
where pn ¼ pnðÞ is defined by
pn ¼ Pr½j ^Xk  ^mkj >  for at least one k with 2n1 < k a 2n:
Hence for any d > 0 there is an N so that Py
n¼N pn < d.
The strong law of large numbers then ‘‘finesses’’ the conclusion that Pr½ ^Xn ! m ¼ 1
without the construction of Sy because of the critical statement in 2 which could not
be derived from the weak law. First o¤, by definition,
X
y
n¼N
pn ¼ Pr½j ^Xk  ^mkj >  for at least one k > 2N1:
So from 2 above we can state that for any d > 0 there is an N ¼ NðÞ so that
Pr½j ^Xk  ^mkj >  for at least one k > 2N1 < d:
In other words, for any d > 0 there is an N so that
Pr½j ^Xk  ^mkj a  for all k > 2N1 b 1  d:
We return to this analysis after the statement and proof of the strong law of large
numbers.
*8.4.4
Kolmogorov’s Inequality
In order to prove the strong law, we need another and stronger inequality than Che-
byshev’s inequality, called Kolmogorov’s inequality, named for Andrey Kolmogorov
(1903–1987) who was also responsible for introducing an axiomatic framework for
probability theory. Extending Chebyshev’s inequality, Kolmogorov’s inequality
8.4
Strong Law of Large Numbers
363

addresses a collection of random variables fXign
i¼1 and provides a probability state-
ment regarding their maximum summation.
Kolmogorov’s inequality is stated for simplicity, under the assumption that
E½Xj ¼ 0 for all j. However, this is not a true restriction. That is, if we are given
fYjgn
j¼1 with E½Yj ¼ mj, we can apply the result to Xj 1 Yj  mj, since it is clear
that Var½Xj ¼ Var½Yj. And while this result requires that fXjgn
j¼1 be independent
random variables, it does not require that they be identically distributed, so it allows
for di¤ering variances.
Proposition 8.13 (Kolmogorov’s inequality)
Let fXign
i¼1 be independent random vari-
ables with E½Xj ¼ 0 and Var½Xj ¼ s2
j . Then for t > 0,
Pr
max
1aian
X
i
j¼1
Xj


 > t
(
)
a
X
n
j¼1
s2
j
t2 :
ð8:15Þ
Remark 8.14
Note that the event defined in (8.15) is an event in S n, where S is the
common sample space on which fXign
i¼1 are defined and independent. Note also that
Kolmogorov’s inequality is considerably stronger than is Chebyshev’s inequality applied
to this probability statement. The Chebyshev inequality would state that for any i, with
1 a i a n,
Pr
X
i
j¼1
Xj


 > t
(
)
a
X
i
j¼1
s2
j
t2 ;
since
for
independent
random
variables
VarðPi
j¼1 XjÞ ¼ Pi
j¼1 s2
j .
Of
course,
Pi
j¼1
s2
j
t2 a Pn
j¼1
s2
j
t2 , so at first these inequalities appear similar. However, Chebyshev’s
inequality provides probability statements on n separate events, and it is silent on the
question of the simultaneous occurrence of these n events. Kolmogorov’s inequality
says that the largest of the n Chebyshev probability bounds is su‰cient to bound the
probability of the worst case of these n events. Alternatively, Kolmogorov’s inequality
says that the largest of the n Chebyshev probability bounds is su‰cient to bound the
probability that all inequalities are satisfied simultaneously.
Proof
The idea of this proof is to eliminate the maximum function by introducing a
new random variable that identifies the first summation for which jPi
j¼1 Xjj > t, and
then use a conditioning argument on this random variable. Consider the sequence
ðPi
j¼1 XjÞ2, i ¼ 1; 2; . . . ; n. For any collection of random variables fXign
i¼1, define a
new random variable N ¼ minfi j ðPi
j¼1 XjÞ2 > t2g, but if ðPi
j¼1 XjÞ2 a t2 for all
i a n, define N ¼ n. Then the events in S n defined by
364
Chapter 8
Fundamental Probability Theorems

max
1aian
X
i
j¼1
Xj
 
!2
> t2
8
<
:
9
=
;;
X
N
j¼1
Xj
 
!2
> t2
8
<
:
9
=
;;
are identical events with equal probabilities. Now by the Markov inequality applied
to the second event, we get
Pr
X
N
j¼1
Xj
 
!2
> t2
8
<
:
9
=
;a
E½ðPN
j¼1 XjÞ2
t2
:
Because
of
the
assumption
that
E½Xj ¼ 0,
we
have
that
E½ðPN
j¼1 XjÞ2 ¼
Var½PN
j¼1 Xj, and so the proof will be complete if we can show that
Var
X
N
j¼1
Xj
"
#
a
X
n
j¼1
s2
j :
Note that this is a bit subtle because while fXigN
i¼1 H fXign
i¼1, N is a random vari-
able, and hence we cannot simply assert that Var½PN
j¼1 Xj a Pn
j¼1 s2
j . To demon-
strate this upper bound, we use the law of total variance. First, for the conditional
variance, Var½PN
j¼1 Xj j N ¼ k ¼ Var½Pk
j¼1 Xj ¼ Pk
j¼1 s2
j . Next, for the conditional
mean, E½PN
j¼1 Xj j N ¼ k ¼ E½Pk
j¼1 Xj ¼ 0. We now have by (7.49),
Var
X
N
j¼1
Xj
"
#
¼ E
X
k
j¼1
s2
j
"
#
þ Var½0:
For this last expectation, if ak ¼ Pr½N ¼ k, then, since Pn
j¼1 ak ¼ 1,
E
X
k
j¼1
s2
j
"
#
¼
X
n
k¼1
ak
X
k
j¼1
s2
j
"
#
a
X
n
j¼1
s2
j ;
which follows by reversing the double summation: Pn
k¼1
Pk
j¼1 ¼ Pn
j¼1
Pn
k¼j.
n
*8.4.5
Strong Law of Large Numbers
We next turn to the statement of the strong law of large numbers. The primary re-
quirement is that while the collection of variances fs2
i g do not need to be bounded,
8.4
Strong Law of Large Numbers
365

if unbounded, they cannot increase too fast. We provide this statement in both the
simpler case of independent and identically distributed random variables, since that
is the statement that is often su‰cient for applications as well as in the more general
case.
Proposition 8.15 (Strong Law of Large Numbers 1)
Let fXjgy
j¼1 be independent,
identically distributed random variables with mean m and variance s2, and define
^Xk ¼ 1
k
Pk
j¼1 Xj. For any  > 0 define the event An HS 2 n,
An ¼ fX j j ^Xk  mj >  for at least one k with 2n1 < k a 2ng;
where X 1 ðX1; X2; . . . ; X2 nÞ A S 2 n. Then
X
y
n¼1
Pr½An < y;
and hence for any d > 0 there is an N so that Py
n¼N Pr½An < d.
Proposition 8.16 (Strong Law of Large Numbers 2)
Let fXjgy
j¼1 be a sequence of mu-
tually independent random variables with means fmjgy
j¼1 and variances fs2
j gy
j¼1 with
Py
j¼1
s2
j
j 2 < y. Define ^Xk ¼ 1
k
Pk
j¼1 Xj and ^mk ¼ 1
k
Pk
j¼1 mj. For any  > 0 define the
event An HS 2 n,
An ¼ fX j j ^Xk  ^mkj >  for at least one k with 2n1 < k a 2ng;
ð8:16Þ
where X 1 ðX1; X2; . . . ; X2 nÞ A S 2 n. Then
X
y
n¼1
Pr½An < y;
ð8:17Þ
and hence for any d > 0 there is an N so that Py
n¼N Pr½An < d.
Proof
The event An can equivalently be defined as the event
An ¼
max
2 n1<ka2n
X
k
j¼1
Yj


 > k
"
#
;
where Yj ¼ Xj  mj. In other words, j ^Xk  ^mkj >  for at least one k with 2n1 <
k a 2n if and only if maxð2 n1<ka2 nÞjPk
j¼1 Yjj > k. Note that Pr½An < Pr½A0
n, where
A0
n is defined in terms of 2n1 rahter than k. By Kolmogorov’s inequality, the prob-
ability of this latter event is given by
366
Chapter 8
Fundamental Probability Theorems

Pr½A0
n <
1
22n2
X
2 n
j¼1
s2
j
2 :
Hence
X
y
n¼1
Pr½An < 4
2
X
y
n¼1
1
22n
X
2 n
j¼1
s2
j :
Note that in this double summation, each s2
j is counted multiple times. In partic-
ular,
X
y
n¼1
1
22n
X
2 n
j¼1
s2
j ¼
X
y
j¼1
s2
j
X
y
2nbj
1
22n
a 2
X
y
j¼1
s2
j
j2 ;
since Py
2nbj
1
22n a Py
n¼j
1
2n ¼
1
2 j1 a 2
j 2 for j b 4. Hence Py
n¼1 Pr½An < y.
n
Remark 8.17
The assumption in the general version of the strong law, that
Py
j¼1
s2
j
j 2 < y, is certainly an assumption about the growth rate of s2
j as j ! y. For
example, if s2
j ¼ s2, which is the assumption of no growth, then, since Py
j¼1
1
j 2 < y
from chapter 6, the strong law applies. On the other hand, if s2
j ¼ js2, so the standard
deviation grows like
ffiffij
p , the strong law does not apply, since again from chapter 6,
PN
j¼1
1
j ! y with N. Consequently linear variance growth, or equivalently, square
root growth in standard deviation, is just a bit too fast for the strong law to apply.
However, if s2
j ¼ j as2 for any a < 1, the strong law applies, since Py
j¼1
s2
j
j 2 ¼
s2 Py
j¼1
1
j 2a < y for 2  a > 1.
Corollary 8.18
Let fXjgy
j¼1 be independent random variables with means fmjgy
j¼1
and variances s2
j with Py
j¼1
s2
j
j 2 < y, and for any k define ^Xk ¼ 1
k
Pk
j¼1 Xj and ^mk ¼
1
k
Pk
j¼1 mj. Then for any  > 0 and d > 0 there is an N so that
Pr½j ^Xk  ^mkj >  for any k > 2N < d:
Equivalently, for any  > 0 and d > 0 there is an N so that
Pr½j ^Xk  ^mkj a  for all k > 2N > 1  d:
ð8:18Þ
8.4
Strong Law of Large Numbers
367

Proof
This follows from the observation that
½j ^Xk  ^mkj >  for any k > 2N ¼
6
nbNþ1
An;
and the conclusion that Py
n¼1 Pr½An < y. Hence for any d > 0 there is an N so that
Py
n¼Nþ1 Pr½An < d.
n
Remark 8.19
Note that in this corollary, ½j ^Xk  ^mkj >  for any k > 2N is not an
event in any of the n-trial sample spaces defined so far. Indeed, since this ‘‘event’’ is re-
lated to the entire collection of random variables, it would have to exist in Sy, which
we have not defined. In essence, with the strong law, we can avoid the construction of
this event in Sy and finesse the result by defining this event as a union of the respective
events in the S 2 n spaces for n b N þ 1. And this corollary estimates that the sum of the
measures of all such events in all such sample spaces can be made as small as desired.
And it is in this light that the strong law of large numbers provides the conclusion
Pr½ ^Xn  ^mn ! 0 ¼ 1, or in the case of identically distributed Xn-values, the conclusion
Pr½ ^Xn ! m ¼ 1.
8.5
De Moivre–Laplace Theorem
The De Moivre–Laplace theorem is a special case of a very general result discussed
below, known as the central limit theorem. The theorem of this section addresses the
question of the ‘‘limiting distribution’’ of the binomial distribution as n ! y. Specif-
ically, if X ðnÞ 1 Pn
j¼1 X B
j
is a binomially distributed random variable with parame-
ters n and p, where X B
j are i.i.d. standard binomial variables, we have from (7.97) the
probability that for integers a and b,
Pr½a a X ðnÞ a b ¼
X
b 0
j¼a 0
n
j


p jð1  pÞnj;
where a0 ¼ maxða; 0Þ and b0 ¼ minðb; nÞ.
In this form it is di‰cult to specify what happens to this distribution as n ! y be-
cause the range of the random variable is ½0; n which varies with n. Put another way,
we have from (7.99) that E½X ðnÞ ¼ np and Var½X ðnÞ ¼ npð1  pÞ, so both the mean
and variance of X ðnÞ grow without bound as n ! y. In order to investigate quanti-
tatively the probabilities under this distribution as n ! y, some form of scaling is
necessary to stabilize results.
368
Chapter 8
Fundamental Probability Theorems

The approach used by Abraham de Moivre (1667–1754) in the special case of
p ¼ 1
2 , and many years later generalized to all p, 0 < p < 1, by Pierre-Simon Laplace
(1749–1827), was to consider what is now called the normalized random variable,
Y ðnÞ, defined by
Y ðnÞ ¼ X ðnÞ  E½X ðnÞ
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
Var½X ðnÞ
p
:
ð8:19Þ
The random variable Y ðnÞ has the same binomial probabilities as does X ðnÞ, of
course, since for any n, E½X ðnÞ and
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
Var½X ðnÞ
p
are constants. However, its range is
now
jE½X ðnÞ
ffiffiffiffiffiffiffiffiffiffiffiffiffi
Var½X ðnÞ
p


 0 a j a n


, and a simple calculation using (7.38) yields that
E½Y ðnÞ ¼ 0;
Var½Y ðnÞ ¼ 1:
Consequently, with mean and variance both constant and independent of n, the ques-
tion of investigating and potentially identifying the limiting distribution of Y ðnÞ as
n ! y is better defined and its pursuit more compelling.
To this end, we first note two elementary but important results on Y ðnÞ:
Proposition 8.20
Given Y ðnÞ defined as in (8.19) where the binomial probability p
satisfies 0 < p < 1:
1. The range of Y ðnÞ is unbounded both positively and negatively as n ! y.
2. If y A R, there is a sequence fyng with yn ! y, and each yn is in the range of Y ðnÞ.
Proof
1. Since 0 a j a n, a simple calculation shows that with q 1 1  p,

ffiffin
p
ffiffiffip
q
r
a j  E½X ðnÞ
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
Var½X ðnÞ
p
a
ffiffin
p
ffiffiffiq
p
r
:
This result reduces to the unbounded symmetric interval ½n; n when p ¼ 1
2 , and it is
unbounded and asymmetrical otherwise as n ! y.
2. Let N denote the smallest integer so that y A 
ffiffiffiffi
N
p
ffiffi
p
q
q
;
ffiffiffiffi
N
p
ffiffi
q
p
q

	
, where again
q ¼ 1  p. This result is always possible, since these intervals grow without bound
with N. Now it must be the case that there is a j, perhaps two such values, so that
y A
jNp
ffiffiffiffiffiffi
Npq
p
; jþ1Np
ffiffiffiffiffiffi
Npq
p


, since the collection of these intervals covers 
ffiffiffiffi
N
p
ffiffi
p
q
q
;
ffiffiffiffi
N
p
ffiffi
q
p
q
h
i
.
We then define y0 as the left endpoint of this interval. For each value of N þ n,
where n b 1, now define yn as the left endpoint of the interval for which y A
8.5
De Moivre–Laplace Theorem
369

jðNþnÞp
ffiffiffiffiffiffiffiffiffiffiffiffiffiffi
ðNþnÞpq
p
; jþ1ðNþnÞ p
ffiffiffiffiffiffiffiffiffiffiffiffiffiffi
ðNþnÞpq
p


. There is again at least one such interval, since these intervals
collectively cover 
ffiffiffiffiffiffiffiffiffiffiffiffi
N þ n
p
ffiffi
p
q
q
;
ffiffiffiffiffiffiffiffiffiffiffiffi
N þ n
p
ffiffi
q
p
q
h
i
. Since the length of the interval in this
nth step is
1
ffiffiffiffiffiffiffiffiffiffiffiffiffiffi
ðNþnÞpq
p
, which converges to 0 as n ! y, it is apparent by construction
that jy  ynj a
1
ffiffiffiffiffiffiffiffiffiffiffiffiffiffi
ðNþnÞpq
p
, and we can conclude that yn ! y.
n
Remark 8.21
In this construction for the proof of 2, the right end points work equally
well, as does a random selection from the two end points of each interval. In other
words, there are infinitely many such sequences.
Consequently for any y A R we can investigate the existence of a probability den-
sity function gðyÞ defined as
gðyÞ 1 lim
n!y PrfY ðnÞ ¼ yng;
where fyng is constructed so that yn ! y. To be sure that such a pursuit is justified,
one needs to ascertain that this limit makes sense and answers the original question:
Is such a gðyÞ the limiting density of the binomial p.d.f. for Y ðnÞ as n ! y?
A moment of reflection demonstrates that this limit may well not answer this ques-
tion, since it is the case that for any such sequence, fyng,
Pr½Y ðnÞ ¼ yn ¼ Pr½X ðnÞ ¼ jn;
where jn ¼ yn
ffiffiffiffiffiffiffi
npq
p
þ np. So as yn ! y, we see that jn ! y, and hence it would ap-
pear logical that
lim
n!y Pr½Y ðnÞ ¼ yn ¼ 0
for any y. In other words, as defined above, it would appear to be the case that
gðyÞ ¼ 0 for all y.
Before investigating this further, note that this conclusion is also compelled by the
fact that if gðyÞ is defined as above for every y A R, then it would not make sense to
have gðyÞ > 0 for more than a countable subset of R. This is because if gðyÞ > 0 for
an uncountable set, then P gðyÞ over all such values would have to be infinite and
never equal 1 as is needed for a probability density. This follows from an argument
analogous to the Cantor diagonalization process, that any attempt to enumerate and
add up all such gðyÞ values would of necessity omit all but a countable subcollection.
Hence any such summation would of necessity be unbounded.
370
Chapter 8
Fundamental Probability Theorems

To formally show that gðyÞ ¼ 0 for all y where gðyÞ is defined above is somewhat
di‰cult, but this conclusion will be an immediate consequence of the proof of the De
Moivre–Laplace theorem that we now pursue. As will be seen, in order to get a true
p.d.f. from the limit of the p.d.f.s of the associated Y ðnÞ random variables, an adjust-
ment factor is needed in the definition above of gðyÞ. Specifically, each probability
PrfY ðnÞ ¼ yng will be multiplied by
ffiffiffiffiffiffiffi
npq
p
, and the product will then be shown to
converge to the desired probability density function hðyÞ. In addition this proof
will establish the speculation above that PrfY ðnÞ ¼ yng ! 0, since
ffiffiffiffiffiffiffi
npq
p
! y and
ffiffiffiffiffiffiffi
npq
p
PrfY ðnÞ ¼ yng ! hðyÞ clearly implies this result.
The proof of this theorem depends on a famous approximation formula for n!,
known as Stirling’s formula, or Stirling’s approximation, named for its discoverer,
James Stirling (1692–1770), which is of interest in itself.
8.5.1
Stirling’s Formula
To establish this approximation formula, we require another power series expansion
from chapter 9 for the natural logarithm function lnð1 þ xÞ. The proof of this will
depend on the same mathematical tools that will be used to prove the power series
expansion of ex noted in (7.63). The needed expansion here is
lnð1 þ xÞ ¼
X
y
n¼1
ð1Þnþ1 1
n
 
xn
for jxj < 1:
ð8:20Þ
As was the case for the series expansion for ex, the ratio test confirms absolute con-
vergence of this series, since
ð1Þnþ2
1
nþ1

	
xnþ1
ð1Þnþ1 1
n
 
xn


¼
x
nþ1
n


 ! jxj
as n ! y;
and consequently the restriction jxj < 1 assures absolute convergence. As x ! 1,
this series approaches the negative of the harmonic series  Py
n¼1
1
n , which diverges
to y. On the other hand, we will see in chapter 10 that as x ! 1, this series is well
defined.
Note also that this formula can be written with x, using lnð1  xÞ ¼ ln
1
1x


,
ln
1
1  x


¼
X
y
n¼1
1
n
 
xn
for jxj < 1:
ð8:21Þ
When combined with (8.20), this yields
8.5
De Moivre–Laplace Theorem
371

1
2 ln 1 þ x
1  x


¼
X
y
n¼1
1
2n  1


x2n1
for jxj < 1;
ð8:22Þ
since ln 1þx
1x


¼ lnð1 þ xÞ  lnð1  xÞ, and absolute convergence justifies rearranging
the terms of these two series into a single series.
Proposition 8.22 (Stirling’s Formula)
As n ! y, we have the relative approximation
n! @
ffiffiffiffiffi
2p
p
nnþð1=2Þen, in the sense that
n!
ffiffiffiffiffi
2p
p
nnþð1=2Þen ! 1
as n ! y:
ð8:23Þ
Moreover the relative error in this approximation is given by
e1=ð12nþ1Þ <
n!
ffiffiffiffiffi
2p
p
nnþð1=2Þen < e1=12n:
ð8:24Þ
Proof
We first show that there is a constant C so that n! @ eCnnþð1=2Þen has the
noted properties. To this end, define fn ¼ ln
n!
nnþð1=2Þen

	
, which can be rewritten using
properties of the logarithm
fn ¼ ln n! 
n þ 1
2


ln n þ n:
We now show that there is a constant C so that fn ! C. By exponentiation, this will
then establish (8.23) with eC in place of
ffiffiffiffiffi
2p
p
. To do this, consider fn  fnþ1. A calcu-
lation shows that
fn  fnþ1 ¼
n þ 1
2


ln n þ 1
n


 1:
Expressing nþ1
n ¼ 1þx
1x , where x ¼
1
2nþ1 , and using (8.22) with index m produces
fn  fnþ1 ¼
X
y
m¼1
1
2m þ 1


x2m;
which demonstrates that fn  fnþ1 > 0. Hence the sequence f fng is decreasing. Fur-
ther, since
1
2mþ1

	
< 1
3 except for m ¼ 1, in which case we have equality
fn  fnþ1 < 1
3
X
y
m¼1
x2m
372
Chapter 8
Fundamental Probability Theorems

¼
1
3½ð2n þ 1Þ2  1
¼ 1
12n 
1
12ðn þ 1Þ :
The last inequality shows that fn 
1
12n < fnþ1 
1
12ðnþ1Þ , so fn 
1
12n is increasing.
Since
1
12n ! 0, this implies that there is a constant C for which fn ! C. The upper
error bound in (8.24) also comes from this analysis. Because fn 
1
12n is increasing
with limit C, we have fn < C þ
1
12n , and this can be exponentiated to the desired
result. For the lower bound, the series expansion for fn  fnþ1 above, using only
the first term implies fn  fnþ1 > 1
3
1
2nþ1

	2
>
1
12nþ1 
1
12ðnþ1Þþ1 . As a result fn 
1
12nþ1 is
increasing and consequently fn > C þ
1
12nþ1 . The final step is the demonstration that
eC ¼
ffiffiffiffiffi
2p
p
, which we only sketch here and defer the details to chapter 10. This con-
clusion is a consequence of what is known as Wallis’ product formula for p
2 , named
for its discoverer, John Wallis (1616–1703), which is
p
2 ¼
Y
y
n¼1
ð2nÞ2
ð2n  1Þð2n þ 1Þ :
ð8:25Þ
A calculation with much cancellation shows that
Y
m
n¼1
ð2nÞ2
ð2n  1Þð2n þ 1Þ ¼
24mðm!Þ4
ð2mÞ!ð2m þ 1Þ! :
So this result can be written as
p
2 ¼ lim
m!y
24mðm!Þ4
ð2mÞ!ð2m þ 1Þ! :
Substituting the approximations for the factorial functions derived above, which are
in the form n! @ eCnnþð1=2Þen completes the derivation that eC ¼
ffiffiffiffiffi
2p
p
. The proof of
Wallis’ formula involves mathematical tools of chapter 10 and an application of in-
tegration by parts.
n
Remark 8.23
1. Note that the approximation in Stirling’s formula only converges in terms of relative
error, and not in terms of absolute error. In fact from (8.24) we can conclude only that
8.5
De Moivre–Laplace Theorem
373

ðe1=ð12nþ1Þ  1Þ
ffiffiffiffiffi
2p
p
nnþð1=2Þen < n! 
ffiffiffiffiffi
2p
p
nnþð1=2Þen < ðe1=12n  1Þ
ffiffiffiffiffi
2p
p
nnþð1=2Þen;
which is an error interval that grows without bound.
2. Also note that the convergence of the Wallis’ product formula for p
2 is painfully
slow. Indeed, defining aN ¼ QN
n¼1
ð2nÞ2
ð2n1Þð2nþ1Þ , we have that aN ¼
ð2NÞ2
ð2N1Þð2Nþ1Þ aN1, and
the successive multiplicative factors
ð2NÞ2
ð2N1Þð2Nþ1Þ ¼
1
1
1
4N 2 converge to 1 very quickly.
8.5.2
De Moivre–Laplace Theorem
With the aid of this approximation for n!, we can now address the primary result in
this section.
Proposition 8.24 (De Moivre–Laplace Theorem)
Let X ðnÞ be a binomial random vari-
able with parameters p and n, with 0 < p < 1, and let Y ðnÞ denote the normalized ran-
dom variable in (8.19). For any y A R, and fyng constructed so that yn A Rng½Y ðnÞ
and yn ! y, we have as n ! y,
ffiffiffiffiffiffiffi
npq
p
PrfY ðnÞ ¼ yng !
1ffiffiffiffiffi
2p
p
ey2=2:
ð8:26Þ
Proof
As noted above, with jn ¼ yn
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
Var½X ðnÞ
p
þ E½X ðnÞ, we have that PrfY ðnÞ ¼
yng ¼ PrfX ðnÞ ¼ jng. Consequently
ffiffiffiffiffiffiffi
npq
p
PrfY ðnÞ ¼ yng ¼
ffiffiffiffiffiffiffi
npq
p
n
jn


p jnð1  pÞnjn:
Using Stirling’s formula applied to
n
j
 	
, we write
n!
j!ðn  jÞ! @
ffiffiffiffiffi
2p
p
nnþð1=2Þen
ffiffiffiffiffi
2p
p
j jþð1=2Þej
ffiffiffiffiffi
2p
p
ðn  jÞðnjÞþð1=2ÞeðnjÞ
¼
1ffiffiffiffiffi
2p
p
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
n
jðn  jÞ
r
n
n  j

nj
n
j
 j
:
In this analysis we shortcut with ‘‘@’’ the more technically accurate use of ‘‘<’’ and
the necessary insertion of error terms in each of the Stirling approximations. We
know from (8.24) that these approximations are collectively bounded above and
below by exponential terms that converge to 1 as n ! y, since then jn ! y.
With this restatement of the combinatorial term, the proof has two parts, since the
1ffiffiffiffi
2p
p
term is apparently accounted for:
374
Chapter 8
Fundamental Probability Theorems

1. The first step is to show that
ffiffiffiffiffiffiffi
npq
p
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
n
jnðn  jnÞ
r
! 1:
To this end, note that
ffiffiffiffiffiffiffiffiffiffiffiffi
jnðnjnÞ
n
q
¼
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
n
jn
n
 	
1  jn
n

	
r
. But jn
n ¼ p þ yn
ffiffiffiffi
pq
n
q
, and 1  jn
n ¼
q  yn
ffiffiffiffi
pq
n
q
, so
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
n
jn
n


1  jn
n


s
¼
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
npq þ ðq  pÞyn
ffiffiffiffiffiffiffi
pqn
p
 y2
n pq
q
:
The ratio of
ffiffiffiffiffiffiffi
npq
p
to this term converges to 1 as n ! y, since yn ! y, completing
the first step.
2. The second step is to show that as n ! y,
n
n  jn

njn
n
jn

jn
p jnð1  pÞnjn ¼
n  jn
nq

ðnjnÞ
jn
np

jn
! ey2=2:
To do this, we first take 1 times the logarithm of the second expression and
show that the resulting expression converges to y2
2 . From part 1 we have that jn ¼
np þ yn
ffiffiffiffiffiffiffi
pqn
p
, and n  jn ¼ nq  yn
ffiffiffiffiffiffiffi
pqn
p
, from which
jn
np ¼ 1 þ yn
ffiffiffi
q
np
q
and njn
nq ¼
1  yn
ffiffiffi
p
nq
q
. Hence
ln
nq
n  jn

njn
np
jn

jn
"
#
¼ ðnq  yn
ffiffiffiffiffiffiffi
pqn
p
Þ ln 1  yn
ffiffiffiffiffip
nq
r


þ ðnp þ yn
ffiffiffiffiffiffiffi
pqn
p
Þ ln 1 þ yn
ffiffiffiffiffiq
np
r


:
Next we apply the first three terms of the power series expansions for the logarithm
in (8.20) to the expressions above, multiply, and collect terms. The ‘‘trick’’ in such a
calculation is to not worry about any terms that will ultimately contain a factor of
n1=2, or n1, and so forth, since these converge to 0 in the limit as n ! y. Since
the terms in front of the logarithms contain a factor of n, the logarithm series is
needed up to its third term, which is up to a factor of n3=2, and the product of this
term with n will go to 0, as will all higher powers in the series.
8.5
De Moivre–Laplace Theorem
375

Implementing this messy bit of algebra, and recalling that yn ! y, produces
ln
nq
n  jn

njn
np
jn

jn
"
#
¼ 1
2 y2
n þ n1=2EðnÞ
! 1
2 y2;
with E denoting the remainder of the series’ terms. This limit as n ! y is justified by
the observation that EðnÞ is an absolutely convergent series with constant first term,
and all other terms of the form cjnaj for some aj > 0.
n
8.5.3
Approximating Binomial Probabilities I
The De Moivre–Laplace theorem provides another handy way to approximate bi-
nomial probabilities, in addition to the Poisson distribution discussed in chapter 7.
Rewriting (8.26) provides the approximation
PrfY ðnÞ ¼ yng F
1
ffiffiffiffiffi
2p
p
ffiffiffiffiffiffiffi
npq
p
ey2
n=2:
ð8:27Þ
In a given binomial application, a common calculation needed is one of the form
Pr½a a X ðnÞ a a þ b, where a and b are integers, and X ðnÞ is binomially distributed
with parameters n and p. Specifically,
Pr½a a X ðnÞ a a þ b ¼
X
aþb
j¼a
n!
j!ðn  jÞ! p jqnj:
This expression reflects the assumption that 0 a a < a þ b a n; otherwise, the sum-
mation begins at j ¼ 0 and ends at j ¼ n, as appropriate. While this is only an arith-
metic calculation, for n large and the range ½a; a þ b wide, this calculation can be
di‰cult even with advanced computing power.
To approximate this probability in such a case for n large, the Poisson p.d.f. can be
used if p is small, say p < 0:1, as noted in chapter 7. In general, this approximation
can also be implemented using (8.27) by converting this probability statement to a
statement in the normalized variable Y ðnÞ ¼ X ðnÞnp
ffiffiffiffiffi
npq
p
. Specifically,
Pr½a a X ðnÞ a a þ b ¼ Pr a  np
ffiffiffiffiffiffiffi
npq
p
a Y ðnÞ a a þ b  np
ffiffiffiffiffiffiffi
npq
p


:
376
Chapter 8
Fundamental Probability Theorems

Using the approximation in (8.27) above, with y0 ¼ anp
ffiffiffiffiffi
npq
p
and yk ¼ yk1 þ
1ffiffiffiffiffi
npq
p
, we
get
Pr½a a X ðnÞ a a þ b F
1
ffiffiffiffiffi
2p
p
ffiffiffiffiffiffiffi
npq
p
X
b
k¼0
ey2
k=2;
ð8:28Þ
which is a more manageable calculation. As noted above, this formula needs to be
adjusted if either a < 0 and/or a þ b > n to ensure that the original summation
includes at most the range j ¼ 0; 1; . . . ; n.
Remark 8.25
Note that while the De Moivre–Laplace theorem is stated in terms
of sums of the standard binomial X ðnÞ 1 Pn
j¼1 X B
j , where fX B
j g are i.i.d. with
Pr½X B
j ¼ 1 ¼ p and Pr½X B
j ¼ 0 ¼ 1  p, it is equally true for sums of shifted binomial
random variables, where Pr½X B0
j
¼ c ¼ p and Pr½X B0
j
¼ d ¼ 1  p. This is because
this variable can be expressed as
X B0
j
¼ ðc  dÞX B
j þ d:
Consequently E½X B0
j  ¼ ðc  dÞE½X B
j  þ d, and Var½X B0
j  ¼ ðc  dÞ2 Var½X B
j . Apply-
ing this to the normalized sums, we obtain
Pn
j¼1 X B0
j
 E½Pn
j¼1 X B0
j 
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
Var½Pn
j¼1 X B0
j 
q
¼
Pn
j¼1 X B
j  E½Pn
j¼1 X B
j 
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
Var½Pn
j¼1 X B
j 
q
¼ Y ðnÞ:
In other words, the normalized summation of shifted binomial random variables equals
the normalized summation of standard binomial random variables. Hence the De
Moivre–Laplace theorem applies and (8.28) is adapted accordingly.
8.6
The Normal Distribution
8.6.1
Definition and Properties
The function
f ðxÞ ¼
1ffiffiffiffiffi
2p
p
ex2=2;
ð8:29Þ
is in fact a continuous probability density function, although we will not have the
mathematical tools to verify in what way this is true until chapter 10. This function
8.6
The Normal Distribution
377

is called the normal density function, and sometimes the unit or standardized normal
density function. There is an associated distribution function, the normal distribution
function, which again requires the tools of chapter 10 to formally define. When not
specifically referring to either the density or distribution functions, it is common to
simply refer to the normal distribution, particularly in reference to the graph of the
density function in figure 8.1.
The normal distribution is also referred to as the Gaussian distribution, named for
Johann Carl Friedrich Gauss (1777–1855), who used it as a model of measurement
errors. The implied random variable, often denoted Z, is apparently not of the dis-
crete type because it assumes all real values. In other words, Rng Z ¼ R. This dis-
tribution is of continuous type, and it may be the most celebrated example of a
continuous probability distribution. The mathematics required for continuous distri-
butions, and some more general distributions, will be developed in chapters 9 and 10,
and we will return to study probability theory in these contexts.
It will be seen in chapter 10 that
E½Z ¼ 0;
Var½Z ¼ 1;
MZðtÞ ¼ et2=2;
CZðtÞ ¼ et2=2;
ð8:30Þ
and we express this p.d.f. relationship as Z @ Nð0; 1Þ. If X is a random variable so
that Xm
s
¼ Z, then X is said to have a general normal distribution, denoted X @
Nðm; s2Þ, and using properties of expectations, one derives that
Figure 8.1
f ðxÞ ¼
1ffiffiffiffi
2p
p
ex2=2
378
Chapter 8
Fundamental Probability Theorems

E½X ¼ m;
Var½X ¼ s2;
MXðtÞ ¼ emtþs2t2=2;
CZðtÞ ¼ eimts2t2=2:
ð8:31Þ
The graph of this density function is the familiar bell-shaped curve in figure 8.1.
As will be seen, associated with the normal p.d.f. is the normal distribution func-
tion FðxÞ, defined as in the discussion leading up to (7.22),
FðxÞ ¼ Pr½Z1ðy; x
¼ Pr½Z a x:
The calculation of FðxÞ from f ðxÞ used in (7.22) requires generalization here, where-
by the summation of f ðxÞ values is replaced by the integral of f ðxÞ developed in
chapter 10.
However, even with that mathematical insight and the needed tools, the normal
distribution function FðxÞ cannot be calculated exactly from the density function
f ðxÞ ¼
1ffiffiffiffi
2p
p
ex2=2 and must be numerically approximated. Consequently it is com-
mon that many mathematical software packages supply this distribution function
as a built-in formula, and also mandatory that every book in probability theory or
statistics provides a table of Nð0; 1Þ values at least for x > 0, often referred to as
the standard normal table.
Such tables are easy to use because of the apparent symmetry of this function
around the point x ¼ 0. In other words, it is apparent that Pr½Z a a ¼ Pr½Z b a.
Also Pr½Z a a ¼ 1  Pr½Z < a ¼ 1  Pr½Z a a, since Pr½Z ¼ a ¼ 0. That is,
FðaÞ ¼ 1  FðaÞ. Consequently we calculate from the standard normal tables
Pr½a a Z a b ¼
FðbÞ  FðaÞ;
if 0 < a < b,
FðbÞ  ½1  FðaÞ;
if a < 0 < b,
FðaÞ  FðbÞ;
if a < b < 0.
8
>
<
>
:
ð8:32Þ
Of course, if we have a table with positive and negative x values, or a computer built-
in function, it is always the case that for a < b, Pr½a a Z a b ¼ FðbÞ  FðaÞ.
8.6.2
Approximating Binomial Probabilities II
Normal distribution tables can be used to approximate binomial probabilities as
noted in (8.28), but a small adjustment is required. From that formula, it would be
natural to assume that
Pr a  np
ffiffiffiffiffiffiffi
npq
p
a Y ðnÞ a a þ b  np
ffiffiffiffiffiffiffi
npq
p


F F
a þ b  np
ffiffiffiffiffiffiffi
npq
p


 F
a  np
ffiffiffiffiffiffiffi
npq
p


;
8.6
The Normal Distribution
379

and of course, the presence of ‘‘F’’ suggests this to be a ‘‘true’’ statement. However,
it is not true that this approximation is as accurate as is possible. The problem with
this approximation can be best observed by letting b ! 0, in which case the left-hand
side becomes Pr Y ðnÞ ¼ anp
ffiffiffiffiffi
npq
p
h
i
, and the right-hand side becomes F
anp
ffiffiffiffiffi
npq
p

	
 F
anp
ffiffiffiffiffi
npq
p

	
¼ 0. This simple example highlights the error and illustrates the problem.
The binomial distribution for X ðnÞ allocates a total probability of 1 among n þ 1
real values 0; 1; 2; . . . ; n. In turn the binomial distribution for Y ðnÞ allocates a total
probability of 1 among n þ 1 real values
np
ffiffiffiffiffiffiffi
npq
p
; 1  np
ffiffiffiffiffiffiffi
npq
p
; 2  np
ffiffiffiffiffiffiffi
npq
p
; . . . ;
nq
ffiffiffiffiffiffiffi
npq
p
:
From (8.27) we have that Pr Y ðnÞ ¼ anp
ffiffiffiffiffi
npq
p
n
o
F
1
ffiffiffiffi
2p
p
ffiffiffiffiffi
npq
p
eððanpÞ= ffiffiffiffiffi
npq
p
Þ2=2, where we note
that the multiplicative term
1ffiffiffiffiffi
npq
p
is exactly equal to the distance between any two suc-
cessive Y ðnÞ values. In other words, this binomial probability is being approximated
by the normal distribution, not at the point anp
ffiffiffiffiffi
npq
p
but over an interval around this
point of length
1ffiffiffiffiffi
npq
p
.
Consequently one has for some 0 a l a 1,
Pr Y ðnÞ ¼ a  np
ffiffiffiffiffiffiffi
npq
p


F Pr a  np  ð1  lÞ
ffiffiffiffiffiffiffi
npq
p
a Z a a  np þ l
ffiffiffiffiffiffiffi
npq
p


:
The usual convention is to take the symmetric value of l ¼ 1
2 , and hence
Pr Y ðnÞ ¼ a  np
ffiffiffiffiffiffiffi
npq
p


F F
a  np þ 1
2
ffiffiffiffiffiffiffi
npq
p


 F
a  np  1
2
ffiffiffiffiffiffiffi
npq
p


:
This is often referred to as the half-interval adjustment, or half-integer adjustment.
Extending this conventional approximation for a single probability, the binomial
probability statement above, written in terms of the original binomial X ðnÞ, becomes
Pr½a a X ðnÞ a a þ b F F
a þ b  np þ 1
2
ffiffiffiffiffiffiffi
npq
p


 F
a  np  1
2
ffiffiffiffiffiffiffi
npq
p


:
ð8:33Þ
Notation 8.26
Because the normal distribution is so important in probability theory, it
has inherited special notation that is almost universally recognized. As noted above, the
standard normal random variable is usually denoted as Z, while the probability density
function is denoted with the Greek letter phi, jðzÞ 1
1ffiffiffiffi
2p
p
ez2=2, and the distribution
function either with the Greek capital phi, FðzÞ, or as NðzÞ.
380
Chapter 8
Fundamental Probability Theorems

*8.7
The Central Limit Theorem
There are many versions of the central limit theorem. All of them generalize the De
Moivre–Laplace theorem in one remarkable way or another. In essence, what any
version states and what makes any version indeed the ‘‘central’’ limit theorem is
that under a wide variety of assumptions, the p.d.f. of the sum of n independent vari-
ables, after normalizing as in (8.19), converges to the normal distribution as n ! y.
Remarkably these random variables need not be identically distributed, just inde-
pendent, although the need for normalization demands that these random variables
have at least two moments: means and variances. When not identically distributed,
there is a requirement that the sequence of variances does not grow too fast to pre-
clude latter terms in the random variable series from increasingly dominating the
summation, as well as a requirement that they do not converge to 0 so quickly that
the average variance converges to 0.
These theorems can be equivalently stated in terms of the sum of these random
variables, or their average. This is because from (7.38) we have
Pn
j¼1 Xj  E½Pn
j¼1 Xj
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
Var½Pn
j¼1 Xj
q
¼
1
n
Pn
j¼1 Xj  E 1
n
Pn
j¼1 Xj
h
i
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
Var 1
n
Pn
j¼1 Xj
h
i
r
;
since E 1
n
Pn
j¼1 Xj
h
i
¼ 1
n E½Pn
j¼1 Xj and Var 1
n
Pn
j¼1 Xj
h
i
¼ 1
n2 Var½Pn
j¼1 Xj. So while
the ranges of the sum and average of random variables are quite di¤erent, the asso-
ciated normalized random variables are identical.
Consequently central limit theorems, in general, and the De Moivre–Laplace the-
orem, in particular, apply to the sums of random variables if and only if they apply
to the averages of random variables. And similar to the result explored above for
sums of general binomial random variables, the central limit theorem applies to
Pn
j¼1 Xj for i.i.d. fXjg, and it applies to Pn
j¼1 Yj where Yj ¼ aXj þ b for constants a
and b.
Central limit theorems apply to all probability distributions that satisfy the given
requirements, whether discrete, continuous, or mixed. Because of this generality there
is no hope that a proof of such a result can proceed along the lines of the proof of the
De Moivre–Laplace theorem, which relied heavily on the exact form of the binomial
p.d.f. The tool used for these general proofs represents a sophisticated application of
properties of the moment-generating function (m.g.f.), or more generally, the charac-
teristic function (c.f.).
8.7
The Central Limit Theorem
381

To set the stage, we provide a simplified proof of the central limit theorem in the
case of independent, identically distributed discrete random variables that have
moments of all orders and a convergent moment-generating function, and hence
(7.66) applies. Mechanically, the proof works in settings other than discrete, but it
requires manipulation properties of the moment-generating function that have only
been proved in a discrete setting but are valid more generally. The proof can also be
generalized to discrete distributions with only a few moments, and this will be dis-
cussed below.
That the conclusion of this theorem is consistent with the normal distribution
depends on a fact that cannot be proved until chapter 10, that the moment-
generating function of the unit normal distribution satisfies: MZðtÞ ¼ et2=2. In ad-
dition, as has been noted many times, and partially proved in section 8.1, the
moment-generating function truly characterizes this and every distribution when
it exists, so the standard normal distribution is the only distribution with the m.g.f.
MZðtÞ ¼ et2=2.
Proposition 8.27 (Central Limit Theorem)
Let X be a discrete random variable with
moments of all orders and a convergent moment-generating function, and let fXjgn
j¼1
be independent and identically distributed random variables. Denote by X ðnÞ the aver-
age of this collection, X ðnÞ ¼ 1
n
Pn
j¼1 Xj, and by Y ðnÞ the normalized version, Y ðnÞ ¼
X ðnÞm
sffin
p
. If MY ðnÞðtÞ denotes the moment-generating function of Y ðnÞ, then
MY ðnÞðtÞ ! et2=2
as n ! y:
ð8:34Þ
Proof
First note two properties of moment-generating functions that follow from
the definition and properties of expectations (see exercise 8):
1. MX=bðtÞ ¼ MX
t
b
 
.
2. MT XiðtÞ ¼ Q MXiðtÞ if fXig are independent.
From these it follows that with Y ðnÞ ¼ Pn
j¼1
Xjm
ffiffin
p s

	
, we have
MY ðnÞðtÞ ¼
Y
n
j¼1
MðXjmÞ
tffiffin
p s


¼
MðXmÞ
tffiffin
p s



n
;
where this last step follows from fXjgn
j¼1 being i.i.d. Now, by (7.66),
382
Chapter 8
Fundamental Probability Theorems

MðXmÞ
tffiffin
p s


¼
X
y
j¼0
1
j! mj
tffiffin
p s

j
:
Recalling that m0 ¼ 1, m1 ¼ 0 and m2 ¼ s2, we get
MðXmÞ
tffiffin
p s


¼ 1 þ s2
2
tffiffin
p s

2
þ n3=2EðnÞ
¼ 1 þ t2
2n þ n3=2EðnÞ;
where EðnÞ ¼ Py
j¼3
1
j! mj
t
s
  jnð3jÞ=2. Now, since MXðtÞ is assumed convergent for
jtj < T say, MXmðtÞ ¼ emtMXðtÞ has the same interval of convergence, and hence
EðnÞ is convergent for jtj < sT. As is true for MXðtÞ, it is also true that EðnÞ is a
di¤erentiable function of t, and hence a continuous function that attains its maxi-
mum and minimum on any closed interval jtj a sT   (see proposition 9.39). Let
K be defined so that jEðnÞj a K for all n on one such interval.
This expression can now be raised to the nth power, and a logarithm taken. The
same trick is used here as in the proof of the De Moivre–Laplace theorem, in which
we keep track of only the powers of n that are needed for the final limit, sometimes
invoking a sample calculation to determine how many terms will be needed. This
produces
ln MY ðnÞðtÞ ¼ n ln 1 þ t2
2n þ n3=2EðnÞ


¼ n
t2
2n þ n3=2EðnÞ


 1
2
t2
2n þ n3=2EðnÞ

2
þ   
"
#
;
where in the second step is invoked the power series expansion for lnð1 þ xÞ from
(8.20) with
x ¼ t2
2n þ n3=2EðnÞ. Now, since
jEðnÞj a K,
we
have
that
jxj a
t2
2n þ n3=2K < 1 for n large, and lnð1 þ xÞ is absolutely convergent. Next the series
above can be expanded and rearranged to produce
ln MY ðnÞðtÞ ¼ 1
2 t2 þ FðnÞ:
Now FðnÞ ¼ n1=2EðnÞ þ n1 ~EðnÞ is absolutely convergent for the same range of t, is
continuous, and hence is bounded on closed subintervals. From this last step we con-
clude that ln MY ðnÞðtÞ ! 1
2 t2 as n ! y, and hence MY ðnÞðtÞ ! et2=2.
n
8.7
The Central Limit Theorem
383

The fact that this theorem allows a variety of generalizations can now be under-
stood. For example, the assumption that X had ‘‘moments of all orders’’ was not
really needed. What was needed was knowledge that MðXmÞ
tffiffin
p s

	
could be approxi-
mated by
MðXmÞ
tffiffin
p s


¼ 1 þ t2
2n þ n3=2EðnÞ;
and where EðnÞ is a bounded function of t on an interval jtj a C as n ! y.
To reach a comparable conclusion in the case of a limited number of moments,
one must work with the characteristic function, which always exists, and with that
function it will be enough to assume that X has three moments using the tools of
chapter 9 adapted to complex-valued functions such as CXðtÞ.
Moreover, looking at the calculation above, we did not really need to have
the error term, E 0ðnÞ ¼ n3=2EðnÞ, with a factor of n3=2. If this coe‰cient was
n1a for any a > 0, this would be enough to again force the conclusion because
then the leading coe‰cient of FðnÞ would be nE 0ðnÞ ¼ naEðnÞ. It turns out that
we can ‘‘almost’’ reach this conclusion if X has only two moments. The conclusion
that can be reached, again with the adapted tools of chapter 9, is that this leading
coe‰cient of FðnÞ satisfies nE 0ðnÞ ! 0 as n ! y, and this again is enough for the
conclusion.
As another example of a direction for generalization, suppose that fXjgn
j¼1 are in-
dependent and have moments of all orders and convergent m.g.f.s but are not identi-
cally distributed. The normalized random variable Y ðnÞ is defined as
Y ðnÞ ¼ X ðnÞ  mðnÞ
sðnÞffiffin
p
;
where mðnÞ ¼ 1
n
Pn
j¼1 mj and ½sðnÞ2 ¼ 1
n
Pn
j¼1 s2
j . Then all the steps up to MY ðnÞðtÞ ¼
Qn
j¼1 MðXjmjÞ
tffiffin
p sðnÞ

	
go through without any obstacle.
This approach produces, with the aid of (7.66) and taking of logarithms,
ln MY ðnÞðtÞ ¼
X
n
j¼1
ln 1 þ
s2
j
2
tffiffin
p sðnÞ

2
þ n3=2EjðnÞ
"
#
¼
X
n
j¼1
ln 1 þ t2
2n
sj
sðnÞ

2
þ n3=2EjðnÞ
"
#
384
Chapter 8
Fundamental Probability Theorems

¼ t2
2
1
n
X
n
j¼1
sj
sðnÞ

2
"
#
þ FðnÞ
¼ t2
2 þ FðnÞ;
where the last step is justified by the definition of sðnÞ.
Although everything looks harmless in this last expression, a closer examination of
the new FðnÞ expression reveals that this comes from summations and products of
terms of the form EjðnÞ ¼ Py
k¼3
1
k! mjk
t
sðnÞ

	k
nð3kÞ=2, where mjk denotes the kth central
moment of Xj. As above, this can be reduced to essentially 1
3! mj3
t
sðnÞ

	3
þ n1=2 ~EjðnÞ,
which means that the first term in FðnÞ is
n3=2 X
n
j¼1
1
3! mj3
t
sðnÞ

3
¼ 1
3! t3 n3=2 Pn
j¼1 mj3
1
n
Pn
j¼1 s2
j

	3=2
¼ 1
3! t3
Pn
j¼1 mj3
ðPn
j¼1 s2
j Þ3=2 :
So in order to be assured that FðnÞ can be dismissed, it is necessary to assume that
the absolute value of this ratio converges to 0. Now, by the triangle inequality ap-
plied twice,
X
n
j¼1
mj3


a
X
n
j¼1
jmj3j a
X
n
j¼1
mj j3j;
where mj j3j denotes the third absolute central moment of Xj, which is mj j3j 1
E½jXj  mjj3.
To assure this needed absolute convergence, it is common to define the condition
in terms of the relative size of third absolute central moments to the variance terms:
Pn
j¼1 mj j3j
ðPn
j¼1 s2
j Þ3=2
 
!1=3
¼
ðPn
j¼1 mj j3jÞ1=3
ðPn
j¼1 mj2Þ1=2 ! 0
as n ! y:
This assumption is a special case of what is known as Lyapunov’s condition, after
Aleksandr Lyaponov (1857–1918).
8.7
The Central Limit Theorem
385

Note that in the case where fXjgn
j¼1 are independent and identically distributed,
Pn
j¼1 mj j3j
ðPn
j¼1 s2
j Þ3=2 ¼
nmj3j
ðns2Þ3=2 ¼ mj3j
ffiffin
p s3 ;
and then Lyapunov’s condition is automatically satisfied.
8.8
Applications to Finance
8.8.1
Insurance Claim and Loan Loss Tail Events
For both the loan loss models and claims models of chapter 7, in which the mean
and variance of the distributions were estimated, there is a natural interest in evalu-
ating the probability of severe loss events, which in both cases is the probability
Pr½L b A, or, Pr½L  E½L b C for various values of assets A or capital C. In this
notation one might envision A to be the assets allocated to cover all losses and insur-
ance claims in a given period, or if E½L has been placed on this balance sheet as a
liability representing a provision for expected losses and claims, C then represents
the capital allocated to cover excess losses. In this simple balance sheet framework,
A ¼ E½L þ C for each risk.
Of course, in the one-period model that we investigate the random loss variable L
has two components in general:
 Insurance liability payments
 Credit losses on assets
So, if A denotes an asset portfolio at time 0, and LA and LI denote losses on assets
and insurance payments respectively, then Pr½L b A is shorthand for
Pr½L b A 1 Pr½LI þ LA > A;
and Pr½L  E½L b C is shorthand for
Pr½L  E½L b C 1 Pr½LI  E½LI þ LA  E½LA > C;
where C 1 A  E½LI  E½LA.
If assets are risk free, then adding more assets to A creates the same increase in C
and this change has no e¤ect on the volatility of losses.
However, when assets are risky, E½LA depends on A. Then adding assets to A cre-
ates a smaller increase in C, and also a¤ects the volatility of losses. In this case it is
386
Chapter 8
Fundamental Probability Theorems

simpler to think of E½LA in terms of a loss ratio random variable RA, in that
LA ¼ ARA. Hence we can define
Pr½L b A 1 Pr½LI þ ARA > A;
ð8:35Þ
and with C 1 Að1  E½RAÞ  E½LI,
Pr½L  E½L b C 1 Pr½LI  E½LI þ AðRA  E½RAÞ > C:
When such models are applied to a single business unit, the total entity is modeled
as
A ¼ L þ C;
where A denotes total assets of the firm, L total liabilities representing provisions for
all expected claims and losses, and C is total capital. Intuitively A ¼ P Aj, and sim-
ilarly for L and C, but the adequacy of corporate capital or assets cannot be assessed
in terms of the capital or assets needs of each unit or risk separately.
Indeed, if Cj denotes the capital needed for the jth risk, in general, one has that
C < P Cj because risks are not perfectly correlated. Hence tail events will not, in
general, be realized together. To evaluate the entity in total, explicit assumptions
are needed on the joint distribution of all risks. We ignore the broader question here
and focus on the adequacy of assets or capital for the risks modeled in chapter 7,
which were related to insurance claims or loan losses during a given fixed period.
We consider three approaches and introduce these in the model with risk-free
assets so that LA ¼ 0. We then turn to the more general asset case.
Risk-Free Asset Portfolio
Chebyshev I
If insurance claims are modeled as in chapter 7, and E½L and Var½L
calculated as in (7.120) and (7.121) for the individual loss model, or (7.125) and
(7.126) for the aggregate loss model, the one-sided Chebyshev inequality in (8.6) can
be used to deduce that for A b E½L,
Pr½L b A a
Var½L
ðA  E½LÞ2 þ Var½L
:
ð8:36Þ
Since A ¼ E½L þ C, this probability upper bound can also be expressed in terms
of C b 0:
Pr½L  E½L b C a
Var½L
C2 þ Var½L :
ð8:37Þ
8.8
Applications to Finance
387

Still this estimate can be considered crude because it is an estimate that applies to
all distributions, and not necessarily one that specifically applies to the distribution at
hand. In addition this estimate only reflects two moments of the given loss distribu-
tion, and no special information about the tail probabilities in this model.
Loss Simulation
As noted in chapter 7, insurance claims under either the individual
or aggregate loss model can be simulated using the approach in section 7.7 on gener-
ating random samples. These models are very general, and need to be adapted to a
specific claims context as noted in chapter 7, but we discuss the general case.
Specifically, for the individual model in (7.119), losses are given by
L ¼
X
j;k
fjkDjkLjk;
where k denotes the risk class, j an enumeration of the individual exposures in this
class, and fjk the exposure on the jth exposure in class k.
To implement one simulation of L, one uniformly distributed random variable
rjk A ½0; 1 is first generated for each exposure of amount fjk to determine if a loss
occurred. If rjk < qk, with qk the probability of a loss, then Djk ¼ 1 and there is a
loss; otherwise, Djk ¼ 0. This procedure is equivalent to defining Djk ¼ F 1
Bk ðrjkÞ,
where FBkðxÞ is the distribution function for this binomial.
In addition for each exposure for which Djk ¼ 1, a new uniformly distributed ran-
dom variable r0
jk A ½0; 1 is generated, and using the c.d.f. of the class k loss ratio
random variable FkðxÞ, we define the sampled loss ratio by Ljk ¼ F 1
k ðr0
jkÞ. This pro-
cedure then generates one simulation of the random variable L, and it can be
repeated as many times as is desired.
Similarly, from (7.122) for the aggregate loss model,
L ¼
X
k
fkNkL0
k;
each of the random variables Nk and L0
k needs to be generated. Here fk denotes the
average of the nk exposures in class k. Since Nk denotes the total number of claims
from this class, it can be modeled either as a binomial distribution with parameters
nk and qk or as a Poisson distribution with lk ¼ nkqk. In either case one simula-
tion for class k requires first generating one uniformly distributed random variable
r A ½0; 1, from which we define Nk 1 F 1
N ðrÞ, where FNðxÞ denotes the assumed
cumulative distribution for Nk. If Nk > 0, then another Nk uniformly distributed
variables frjgNk
j¼1 are generated from which are defined the loss ratios fLjkgNk
j¼1 ¼
388
Chapter 8
Fundamental Probability Theorems

fF 1
k ðrjÞgNk
j¼1, with FkðxÞ the cumulative distribution function for Lk. The average
loss ratio is then L0
k ¼
1
Nk
PNk
j¼1 Ljk. Each additional simulation proceeds in the same
way and is repeated as many times as is desired.
From these simulations one can now estimate Pr½L b A directly from the gener-
ated data. Namely, if M denotes the total number of simulations, and M A the num-
ber for which L b A, then
Pr½L b A A M A
M :
ð8:38Þ
If there is a shortcoming in this procedure, it is that for A large there may be very
few sample points generated for which L b A. For example, if Pr½L b A ¼ pA, then
given a simulation of M sample points for L,
E½M A ¼ MpA;
Var½M A ¼ MpAð1  pAÞ:
Consequently the mean and standard deviation of this probability estimate are
E M A
M


¼ pA;
s:d: M A
M


¼
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
pAð1  pAÞ
M
r
;
and so by the De Moivre theorem, the 100ð1  aÞ% confidence interval for M A
M is
approximately
pA
1  za=2
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
ð1  pAÞ
MpA
s
 
!
a M A
M a pA
1 þ z1ða=2Þ
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
ð1  pAÞ
MpA
s
 
!
;
where za=2 and z1ða=2Þ denote the respective percentiles on Nð0; 1Þ. This result can be
better stated in terms of the relative error of the estimate:
1  za=2
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
ð1  pAÞ
MpA
s
a
M A
M
pA a 1 þ z1ða=2Þ
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
ð1  pAÞ
MpA
s
:
Example 8.28
If pA ¼ 0:001 and a ¼ 0:05, then the range of the ratio of the estimate
M A
M to the actual value pA, for a 95% confidence interval, is 2z0:975
ffiffiffiffiffiffiffiffiffiffiffi
ð1p AÞ
Mp A
q
F 123:9
ffiffiffiffi
M
p
,
8.8
Applications to Finance
389

since z0:975 F 1:96. So to have this range equal to pA, for a 50% relative estimate error
‘‘on average,’’ requires, M F 1:5  1010 simulations. If pA F 0:01, we have that
2z0:975
ffiffiffiffiffiffiffiffiffiffiffi
ð1p AÞ
Mp A
q
F 39:0ffiffiffiffi
M
p
, so to again have this range equal to pA, for a 50% relative error
requires M F 15:2 million. Finally, for pA F 0:1, we require M F 13;830, and for
pA F 0:2, the number of simulations reduces to M F 1537.
Simulations and Chebyshev II
To avoid the estimation problem noted above when
Pr½L b A is small, which is the anticipated case for most problems of interest in
assessing asset or capital adequacy, we use the simulation above to calibrate a new
Chebyshev estimate. To this end, we first choose an initial asset level, A0, so that
pA0 1 Pr½L b A0 is relatively large, say in the range: 0:10 a pA 0 a 0:20. Then
approximately 10–20% of the simulations will produce losses in excess of this initial
level.
Define L0 to be the generated losses above this threshold. Specifically, L0 is a con-
ditional random variable:
L0 ¼ L j ðL > A0Þ:
Formulaically, the distribution function of L0 is given in terms of the distribution
function of L by
FL0ðxÞ ¼ FLðxÞ  FLðA0Þ
1  FLðA0Þ
;
x b A0:
From the simulated data, E½L0 and Var½L0 can be estimated, and from the one-
sided Chebyshev inequality, we have for A > E½L0,
Pr½L0 > A a
Var½L0
ðA  E½L0Þ2 þ Var½L0
:
ð8:39Þ
Note that Pr½L > A0 is also estimated from the simulations as M A0
M , and this is used
next.
By the law of total probability, for any values of A and A0,
Pr½L > A ¼ Pr½L > A j L < A0 Pr½L < A0 þ Pr½L > A j L > A0 Pr½L > A0:
For A > A0, we have that Pr½L > A j L < A0 ¼ 0. Also Pr½L > A j L > A0 ¼
Pr½L0 > A, and therefore
Pr½L > A ¼ Pr½L0 > A Pr½L > A0:
390
Chapter 8
Fundamental Probability Theorems

Finally, for A > E½L0, we have from (8.39) and (8.38) that
Pr½L > A a M A 0
M
Var½L0
ðA  E½L0Þ2 þ Var½L0
:
ð8:40Þ
Since A ¼ E½L þ C, this probability upper bound can also be expressed in terms
of C:
Pr½L  E½L b C a M A 0
M
Var½L0
ðC þ E½L  E½L0Þ2 þ Var½L0
ð8:41Þ
Risky Assets
Using (8.35), we write
Pr½L b A 1 Pr½LI þ ARA > A;
the new challenge is the estimation of the moments of the random variable L 1
LI þ ARA from two respective models. Of course, LI is modeled as above in the
risk-free asset case. For RA the same models can be applied to a representative risky
asset portfolio of amount A0, and we then define the random variable RA by
RA ¼ LA0
A0
:
We can then determine the mean and variance of RA from the mean and variance of
LA0, and simulate RA from simulations of LA0.
The critical question in this context is the correlation between the random vari-
ables LI and RA. In some applications, such as for life insurance and credit losses,
the assumption of independence seems justifiable. In others, for example, disability
insurance and credit losses, or variable life insurance claims and stock portfolio
losses, a nonzero correlation assumption is needed. This is because disability claims
can be negatively correlated with the economy as are credit losses, so there is a posi-
tive correlation between LI and RA. Likewise variable life insurance minimum guar-
antees are more costly when equity markets are falling, so again there is a positive
correlation between LI and RA.
We only investigate here the case of uncorrelated LI and RA and leave the more
general development as an exercise. In this case,
E½L ¼ E½LI þ AE½RA;
Var½L ¼ Var½LI þ A2 Var½RA:
8.8
Applications to Finance
391

Consequently the direct application of Chebyshev’s inequality in (8.36) becomes for
Að1  E½RAÞ > E½LI, or A >
E½LI
1E½R A :
Pr½L b A a
Var½LI þ A2 Var½RA
ðAð1  E½RAÞ  E½LIÞ2 þ Var½LI þ A2 Var½RA
:
ð8:42Þ
For simulations, the random variables LI and RA are generated in pairs, and now
(8.38) is applied directly, where M A is again the number of paired scenarios for
which L b A, which is equivalent to
LI b Að1  RAÞ:
Finally, the combined simulation and Chebyshev estimate works as above. First
o¤, A0 is defined so that pA 0 1 Pr½L b A0 is again in the range 0:1 a pA 0 a 0:2
where
Pr½L b A0 ¼ Pr½LI b A0ð1  RAÞ:
Then L0 is defined as the total loss random variable conditional on L b A0:
L0 ¼ L j ðL > A0Þ;
where L ¼ LI þ ARA.
The moments E½L0 and Var½L0 can be estimated from paired simulations, as can
Pr½L > A0 ¼ M A 0
M . Note, however, that in general, there is no formulaic relationship
between the conditional mean and variance of L0 and the conditional means and
variances of the components losses LI and ARA.
Finally, for A > E½L0, (8.40) again applies.
8.8.2
Binomial Lattice Equity Price Models as Dt ? 0
Let m and s2 denote the mean and variance of the log-ratio return series as in chapter
7, where these parameters of necessity reflect the period of time separating the data
points. By convention, and independent of the time period reflected in the data, these
return statistics are always denominated in units of years. In other words,
m ¼ E ln Stþ1
St




;
s2 ¼ Var ln Stþ1
St




;
where the time parameter of these equity price observations, t, is denominated in
years. Of course, if the raw data are spaced di¤erently, say weekly or monthly, there
392
Chapter 8
Fundamental Probability Theorems

may be a question as to how these estimates are defined if one chooses not to dis-
regard most of the data. This question is addressed below.
Given this historical data series of annual log-ratio returns, which we now index
with the natural numbers
Rj ¼ ln Sjþ1
Sj


;
the density function usually appears bell-shaped, and tests confirm that this series
appears reasonably uncorrelated. So one approximate model for projecting into the
future assumes independent normally distributed returns. If fzjg denotes a random
collection of standard normal variables, with E½zj ¼ 0, Var½zj ¼ 1, then fRjg 1
fm þ zjsg will be normally distributed and have the correct mean and variance, and
the projection model becomes
Sjþ1 ¼ Sjemþzjs:
While we have not proved this yet (see chapter 10), these standard normal variables
are produced the same way as are discrete variables. That is, by starting with a uni-
formly distributed collection fxjg H ½0; 1, and defining zj ¼ N1ðxjÞ with NðxÞ the
standard normal distribution function.
Alternatively, if the goal of the projection is to model prices in the distant future,
we could approximate the log-ratio returns in this normal model with binomial
returns, Rj F Bj, defining
Sjþ1 ¼ SjeBj:
In this case fBjg are a random collection of binomials as in chapter 7,
Bj ¼
u;
Pr½u ¼ p,
d;
Pr½d ¼ 1  p,

and here u and d are calibrated to achieve the desired moments of m and s2.
The justification for these models being used as alternatives is that at a distant
future point in time, Pn
j¼1 Bj will be nearly normally distributed by the De Moivre–
Laplace theorem, as long as n is large. Alternatively, if these models could be trans-
lated into models with small time steps of size Dt, the binomial approximation to the
normal would be justified even for short-term projections, as long as Dt was small
enough.
But how do the parameters m and s2 depend on Dt?
8.8
Applications to Finance
393

Parameter Dependence on Dt
Since the modeling period is often fixed as ½0; T, say, n large is equivalent to Dt 1 T
n
being small. But, of course, if Dt is taken as small, it may well be smaller than
the original periods of time separating the data points on which m and s2 were de-
veloped. Consequently in this section we first investigate a reasonable model for
mðDtÞ and s2ðDtÞ, or the relationship between the log-ratio return mean and variance
and the length of the time interval. For specificity, one may assume the intuitive
model that m and s2 are defined as annualized statistics so that the units of Dt are
years, but all that is needed mathematically is that the statistics m and s2 correspond
to Dt ¼ 1.
Specifically, assume that m and s2 denote the mean and variance of the log-ratio
return series fRjg for Dt ¼ 1, and that Bj has been calibrated to the binomial model
as in chapter 7. As derived in exercise 27 of that chapter, the general formulas for u
and d, which define Bj for general p, 0 < p < 1, equal
u ¼ m þ
ffiffiffiffi
p0
p
s
"
#
s;
d ¼ m 
ffiffiffiffip
p0
r


s:
ð8:43Þ
Now for Dt ¼ 1
m , so that there are m time steps in a given period, ½ j; j þ 1, let
fBkðDtÞgm
k¼1 denote the associated subinterval random variables, defined by
Sjþk=m ¼ Sjþðk1Þ=meBkðDtÞ;
k ¼ 1; 2; . . . ; m:
If this model is applied iteratively to obtain Sjþ1 ¼ SjeT BkðDtÞ, then it is apparent
upon comparing it to the original model that
X
m
k¼1
BkðDtÞ ¼ Bj:
In the same way that the collection fBjg were assumed in the model to be indepen-
dent and identically distributed, it is logical to extend this assumption to fBkðDtÞg.
Namely we assume that for any Dt, the collection of subperiod log-ratio returns is
independent and identically distributed.
Recall that the mean of a sum of random variables is the sum of the means, and
the variance of an independent sum of random variables is the sum of the variances.
Consequently we obtain mmðDtÞ ¼ m and ms2ðDtÞ ¼ s2 for the binomial model, and
since Dt ¼ 1
m , this can be expressed as
394
Chapter 8
Fundamental Probability Theorems

mðDtÞ ¼ mDt;
ð8:44aÞ
s2ðDtÞ ¼ s2Dt:
ð8:44bÞ
For example, the binomial stock price model in time steps of Dt a 1 units for p ¼ 1
2
becomes
StþDt ¼
StemDtþs ffiffiffi
Dt
p
;
Pr ¼ 1
2,
StemDts ffiffiffi
Dt
p
;
Pr ¼ 1
2,
(
ð8:45Þ
with the analogous formula for general p using (8.43).
The normally distributed log-ratio return model can also be recalibrated to the new
time interval with the same result based on the same calculation, that Pm
k¼1 RkðDtÞ ¼
Rj, again producing (8.44).
Distributional Dependence on Dt
If fRjg are assumed to be independent and normally distributed, so too will be the
subperiod returns fRkðDtÞg. In other words,
StþDt ¼ SteRtðDtÞ;
where again, the collection fRjðDtÞg are i.i.d. and NðmDt; s2DtÞ. That is, for any
time t,
RtðDtÞ ¼ mDt þ zts
ffiffiffiffiffi
Dt
p
;
where fztg are i.i.d. and Nð0; 1Þ.
This is demonstrated by the uniqueness of the moment-generating function or
characteristic function as was introduced above. For example, if fRjg are normally
distributed, R 1 Rj @ Nðm; s2Þ, then from (8.31) we have MRðsÞ ¼ emsþs2s2=2. On
the other hand, because of independence it must be the case that MT RkðDtÞðsÞ ¼
½MRkðDtÞðsÞm. Since Pm
k¼1 RkðDtÞ ¼ R and Dt ¼ 1
m , we derive
MRkðDtÞðsÞ ¼ ½emsþs2s2=21=m
¼ emDtsþs2Dts2=2:
This confirms both the mean and variance result in (8.44), as well as the result that
RkðDtÞ @ NðmDt; s2DtÞ.
In exercise 9 is assigned the demonstration that this result does not hold for bi-
nomially distributed Bj, despite the fact that we still have the moments result in
8.8
Applications to Finance
395

(8.44). In other words, there is a theoretical inconsistency in assuming for each Dt
that log-ratio returns are independent and binomially distributed. However, we will
now show that as Dt ! 0, this inconsistent binomial model converges and gives the
same probability distribution of stock prices as does the assumption of normal log-
ratio returns, which is consistent.
Real World Binomial Distribution as Dt ? 0
In this section we address the question of the limiting distribution of equity prices
under the real world binomial model. Later, using the tools of chapter 9, we will be
able to generalize this calculation to the question of the limiting distribution of equity
prices under the risk-neutral binomial model. Such a derivation is of necessity more
di‰cult, and hence the need for additional tools, since despite assuming the same
values for future equity prices, the probabilities of the u and d returns change from
numerically fixed values of p and p0 to risk-neutral probabilities q and q0 that depend
on Dt.
For a fixed T > 0, where T is denominated in units of the time interval associated
with m and s2, we now investigate the limiting probability density function of ST as
Dt ! 0. For any given integer n, define Dt ¼ T
n , and calibrate the n-step binomial lat-
tice from t ¼ 0 to t ¼ T. Since T ¼ nDt, we have that for general p, as in (8.43),
SðnÞ
T ¼ S0eT Bj;
ð8:46aÞ
Bj ¼
mDt þ as
ffiffiffiffiffi
Dt
p
;
Pr ¼ p,
mDt  1
a s
ffiffiffiffiffi
Dt
p
;
Pr ¼ p0,
j ¼ 1; 2; . . . ; n,
(
ð8:46bÞ
a ¼
ffiffiffiffi
p0
p
s
:
ð8:46cÞ
In other words, ln½SðnÞ
T =S0 ¼ Pn
j¼1 Bj is a sum of n independent binomial random
variables. Also, since E½Bj ¼ mDt and Var½Bj ¼ s2Dt, we obtain the following result,
which is independent of n by construction:
E
X
n
j¼1
Bj
"
#
¼ mT;
Var
X
n
j¼1
Bj
"
#
¼ s2T:
Now remark 8.25 following the proof of the de Moivre–Laplace theorem, here
with c ¼ mDt þ as
ffiffiffiffiffi
Dt
p
and d ¼ mDt  1
a s
ffiffiffiffiffi
Dt
p
and general p, does not directly imply
that the normalized summation of fBjg has a distribution that converges to the unit
normal distribution as n ! y. The reason is that c and d are not constants here but
396
Chapter 8
Fundamental Probability Theorems

change with n, since Dt ¼ T
n . In other words, here we have c ¼ mT
n þ as ffiffiffi
T
p
ffiffin
p
and d ¼
mT
n  s ffiffiffi
T
p
a ffiffin
p .
So this summation of random variables is completely di¤erent from that accom-
modated by either the De Moivre–Laplace theorem or the central limit theorems,
since here the basic random variables in the summation di¤er for each n, in that
Bj 1 BðnÞ
j . Also there is no way to ‘‘freeze’’ these random variables to be independent
of n. In the application at hand it is important for these random variables to change
as n ! y so that over the time interval ½0; T the expected value of the sum is fixed
at mT, and the variance of the sum is fixed at s2T.
Still we can construct the normalized random variable Y ðnÞ as in remark 8.25 and
demonstrate that the unit normal is again produced in the limit. Specifically:
Proposition 8.29
For Bj defined as in (8.46), let
Y ðnÞ ¼
Pn
j¼1 Bj  mT
s
ffiffiffiffi
T
p
:
ð8:47Þ
Then as n ! y,
MY ðnÞðsÞ ! es2=2:
ð8:48Þ
In other words, by (8.30), Y ðnÞ ! Nð0; 1Þ.
Proof
Note that with Yj ¼ BjmDt
s ffiffiffi
T
p
, we have Y ðnÞ ¼ Pn
j¼1 Yj. Also, since
Yj ¼
affiffin
p ;
Pr ¼ p;

1
a ffiffin
p ;
Pr ¼ p0,
(
with a ¼
ffiffiffi
p 0
p
q
, we obtain with exp A 1 eA,
MYjðsÞ ¼ p exp
asffiffin
p


þ p0 exp 
s
a
ffiffin
p


:
Using (7.63) and simplifying notation with mj 1 pa j þ ð1Þ jp 0
a j
leads to
MYjðsÞ ¼
X
y
j¼0
mj
s j
j! nj=2
¼ 1 þ s2n1
2
þ n3=2EðnÞ;
8.8
Applications to Finance
397

since m0 ¼ 1, m1 ¼ 0, and m2 ¼ 1. The rearrangement of these series is justified by
their absolute convergence. The error term EðnÞ is then also an absolutely convergent
series for all n, and that as n ! y, we have that EðnÞ ! m3 s3
6 . Consequently, since
the fYjg are independent, the m.g.f. of Y ðnÞ ¼ Pn
j¼1 Yj is this expression raised to the
nth power. Now, taking logarithms, we obtain
ln MY ðnÞðsÞ ¼ n ln 1 þ s2n1
2
þ n3=2EðnÞ


:
Next we apply (8.20) with x ¼ s2n1
2
þ n3=2EðnÞ. This series is absolutely convergent
for x < 1, which is to say, for n large enough. Then rearranging and keeping track
of only the first few terms of the series, as the rest will converge to 0 as n ! y, we
obtain
ln MY ðnÞðsÞ ¼ n
X
y
j¼1
ð1Þ jþ1 1
j
 
x j
¼ n s2n1
2
þ n3=2EðnÞ


þ n1E 0ðnÞ
¼ s2
2 þ n1=2½EðnÞ þ n1=2E 0ðnÞ;
where E 0ðnÞ is also absolutely convergent, and with E 0ðnÞ !
s2
2
h i2
as n ! y. Finally,
we see from this expression that as n ! y,
ln MY ðnÞðsÞ ! s2
2 ;
and from this we conclude (8.48) because of the continuity of the exponential func-
tion. So Y ðnÞ ! Nð0; 1Þ, the standard normal variable by (8.30).
n
Of course, since
Y ðnÞ ¼ ln½SðnÞ
T =S0  mT
s
ffiffiffiffi
T
p
;
we can apply the properties of the m.g.f. from exercise 8 to ln½SðnÞ
T =S0 ¼ s
ffiffiffiffi
T
p
Y ðnÞ þ
mT, to obtain
Mln½SðnÞ
T =S0ðsÞ ¼ emTsMY ðnÞðss
ffiffiffiffi
T
p
Þ:
ð8:49Þ
398
Chapter 8
Fundamental Probability Theorems

The proposition above then asserts that as n ! y,
Mln½SðnÞ
T =S0ðsÞ ! emTsþs2Ts2=2;
and so
ln SðnÞ
T
S0
"
#
! NðmT; s2TÞ:
This formula can be written as ln SðnÞ
T ! ln ST as n ! y, where
ln ST @ Nðln S0 þ mT; s2TÞ:
ð8:50Þ
In other words, in the limit of the real world binomial lattice model as n ! y, or
equivalently as Dt ! 0, ln ST will be normally distributed with a mean of ln S0 þ mT
and variance of s2T. This can equivalently be expressed as follows:
Corollary 8.30
With SðnÞ
T
defined as in (8.46), then SðnÞ
T ! ST as n ! y with
ST ¼ S0eX;
ð8:51Þ
where X @ NðmT; s2TÞ.
Written in this form, ST is said to have a lognormal distribution, which will be seen
again in chapter 10.
Remark 8.31
1. It was noted in section 7.8.5 and developed in exercise 23 of that chapter, that for
any p with 0 < p < 1, a binomial lattice with unit step-size can be calibrated with up
and down state returns, u and d, so that E½Stþ1=St ¼ m and Var½Stþ1=St ¼ s2 for ar-
bitrary m and s2. In section 8.8.2 this point was generalized to binomial lattices with
step-size of Dt, so that now with uðDtÞ and dðDtÞ, we obtain E½StþDt=St ¼ mDt and
Var½StþDt=St ¼ s2Dt. Further proposition 8.29 demonstrates that for any such choice
of p and corresponding calibration, as n 1 T
Dt ! y, the distribution of the binomial
prices at time T, denoted SðnÞ
T
satisfies
ln SðnÞ
T ! Nðln S0 þ mT; s2TÞ:
It is natural to wonder if the selection of p influences the speed of this convergence. A
closer inspection of the proof of proposition 8.29 provides an insight. With the notation
of that proof, we have
8.8
Applications to Finance
399

ln MY ðnÞðsÞ ¼ s2
2 þ n1=2EðnÞ þ n1E 0ðnÞ;
where the EðnÞ series equals m3s3=6 þ Oðn1=2Þ, and the E 0ðnÞ series equals ½s2=22 þ
Oðn1=2Þ. Consequently the speed of convergence could be improved from Oðn1=2Þ to
Oðn1Þ if p could be selected to make m3 ¼ 0, and this is seen to occur when p ¼ 1=2.
In remark 9.158 we will return to this issue and there see that p ¼ 1=2 also plays a par-
tial role in improving the speed of convergence of the distribution of prices under the
risk-neutral probability qðDtÞ.
2. If returns are assumed to be normally distributed in each period, where
Rj ¼ mDt þ zjs
ffiffiffiffiffi
Dt
p
, with Dt ¼ T
m , then it is easy to see that at time T, independent
of m,
ST ¼ S0eTm
j¼1Rj
¼ S0eTm
j¼1½mDtþzjs ffiffiffi
Dt
p

¼ S0emTþzs ffiffiffi
T
p
¼ S0eX;
where X @ NðmT; s2TÞ. In the third line of this calculation Pm
j¼1 zj @ Nð0; mÞ is used,
and hence Pm
j¼1 zj ¼
ffiffiffiffim
p z, where z @ Nð0; 1Þ, as can be verified by considering
moment-generating functions. So the real world binomial lattice model converges as
Dt ! 0 to exactly the same model of stock prices as does the normal return model.
Interestingly this convergence occurs despite the fact that the assumption on subperiod
returns having independent binomial distributions for all Dt is an inconsistent distribu-
tional assumption, as noted at the end of the last section.
Although providing the same equity price model in the limit, the advantage of the
binomial model is that it provides a simpler framework within which to contemplate
option pricing, which we address next.
8.8.3
Lattice-Based European Option Prices as Dt ? 0
The Model
In (7.147) was derived the lattice-based price of a European option, or other
European-type derivative security with payo¤ function LðSTÞ, by way of a replicat-
ing portfolio argument,
400
Chapter 8
Fundamental Probability Theorems

L0ðS0Þ ¼ enr X
n
j¼0
n
j


q jð1  qÞnjLðS j
nÞ;
S j
n ¼ S0e juþðnjÞd:
Here n denotes the number of time steps to the exercise date T, and the risk-neutral
probability q is a function of the binomial stock returns u and d, as well as the period
risk-free rate r. Recall from (7.143) that this relationship is given by
q ¼ er  ed
eu  ed :
Further recall the binomial stock returns calibrated in (8.43) to equal
u ¼ m þ
ffiffiffiffi
p0
p
s
"
#
s;
d ¼ m 
ffiffiffiffip
p0
r


s;
where 0 < p < 1, p0 1 1  p, and m and s2 denote the mean and variance of the log-
ratio series for one time step. These formulas for u and d generalize those in (7.136),
which were u ¼ m þ s, d ¼ m  s, when p ¼ p0 ¼ 1
2 .
Naturally, in this revised setting where T is fixed and time steps are defined by
Dt ¼ T
n , all these formulas are applicable with adjusted stock returns as in (8.44)
and an adjusted risk-free rate. In other words, for the definition of q, we have
qðDtÞ ¼ erðDtÞ  edðDtÞ
euðDtÞ  edðDtÞ ;
ð8:52Þ
where
uðDtÞ ¼ mDt þ
ffiffiffiffi
p0
p
s
"
#
s
ffiffiffiffiffi
Dt
p
;
ð8:53aÞ
dðDtÞ ¼ mDt 
ffiffiffiffip
p0
r


s
ffiffiffiffiffi
Dt
p
:
ð8:53bÞ
While not completely defensible, the common model for the risk-free rate is that
with r denoting the rate for Dt ¼ 1, which equals one year in practice,
rðDtÞ ¼ rDt:
ð8:54Þ
8.8
Applications to Finance
401

This model reflects the idea that the applicable continuous risk-free rate r is e¤ec-
tively fixed and that any investment for period Dt a 1 earns this same rate. This e¤ec-
tively ignores the term structure of risk-free investments, which can be observed
historically to sometimes be a normal term structure for which rðDtÞ < rDt, sometimes
an inverted term structure for which rðDtÞ > rDt, and sometimes a flat term structure
for which rðDtÞ ¼ rDt. That said, refinements to the assumption in (8.54) have little
e¤ect in practice, at least for common options with maturities within a few months.
European Call Option Illustration
To illustrate the behavior of the price of a European option as Dt ! 0, we assume
that LðS j
nÞ is the exercise price of a call option: LðS j
nÞ ¼ maxðS j
n  K; 0Þ. Inserting
this exercise function into the formula above for L0ðS0Þ, and recalling that S j
n ¼
S0e juþðnjÞd and nDt ¼ T, we get
LC
0 ðS0Þ ¼ enrDt X
n
j¼0
n
j


q jð1  qÞnj maxðS j
n  K; 0Þ
¼ erT X
n
j¼a
n
j


q jð1  qÞnjS j
n  K
X
n
j¼a
n
j


q jð1  qÞnj
"
#
¼ S0
X
n
j¼a
n
j


ðqeuerDtÞ j½ð1  qÞederDtnj  erTK
X
n
j¼a
n
j


q jð1  qÞnj:
Here a is defined by
a ¼ minfj j S j
n b Kg:
Note that if we define
q ¼ qeuerDt;
ð8:55Þ
then a calculation shows that 1  q ¼ ð1  qÞederDt. In other words,
LC
0 ðS0Þ ¼ S0
X
n
j¼a
n
j


q jð1  qÞnj  erTK
X
n
j¼a
n
j


q jð1  qÞnj
¼ S0 Pr½Sn b K j Binðq; nÞ  erTK Pr½Sn b K j Binðq; nÞ;
402
Chapter 8
Fundamental Probability Theorems

where Binðq; nÞ is shorthand for the binomial distribution with parameters q and n,
and similarly for Binðq; nÞ. For both binomials, the subperiod stock returns are given
by uðDtÞ and dðDtÞ above, where q and q, respectively, denote the probability of the
return uðDtÞ.
In more detail, the random variable Sn
can be expressed with notation
expðAÞ 1 eA:
Sn ¼ S0 exp
X
n
i¼1
Bi
"
#
;
where fBig are independent and identically distributed binomial variables that as-
sume values of uðDtÞ and dðDtÞ. In the Binðq; nÞ model, Pr½uðDtÞ ¼ q, while in the
Binðq; nÞ model, Pr½uðDtÞ ¼ q. With Pn
i¼1 Bi denoted by BðnÞ in the Binðq; nÞ model,
and by BðnÞ in the Binðq; nÞ model, the result above can be expressed as
LC
0 ðS0Þ ¼ S0 Pr BðnÞ b ln K
S0




 erTK Pr BðnÞ b ln K
S0




:
Finally, we normalize the binomial random variables in the expression above for
L0ðS0Þ, subtracting the means of mn and mn, respectively, and dividing by the stan-
dard deviations of sn and sn, respectively. Call these normalized binomials B0
ðnÞ and
B0
ðnÞ, to produce
LC
0 ðS0Þ ¼ S0 Pr B0
ðnÞ b
ln K
S0
h i
 mn
sn
2
4
3
5
 erTK Pr B0
n b
ln K
S0
h i
 mn
sn
2
4
3
5:
ð8:56Þ
Remark 8.32
As noted in chapter 7, q is called the risk-neutral probability. Utility
functions will be discussed in chapter 9, but it will be seen there that q is a risk-averter
probability. Unlike the risk-neutral probability, which is unique, any probability ^q > q
is a risk-averter probability. So q is simply one example, since uðDtÞ > rDt implies
q > q, and we will refer to it as the special risk-averter probability. However, despite
the presence of a risk-averter probability in this option price, it is essential to under-
stand that option pricing will be shown to be entirely independent of risk preferences,
and the presence of q in the formula above is merely a mathematical artifact that sim-
plifies the ultimate solution.
8.8
Applications to Finance
403

To see this, note that the formula above for L0ðS0Þ can be expressed as
LC
0 ðS0Þ ¼ erT X
n
j¼0
n
j


q jð1  qÞnj maxðS j
n  K; 0Þ
¼ erTE½maxðSn  K; 0Þ j Binðq; nÞ:
Clearly, in this formulation only the risk-neutral probability is needed for the option
price. Restating this formula in terms of q and q just facilitates the study we discuss
next and in chapter 9.
Black–Scholes–Merton Option-Pricing Formulas I
Because u, d, q, and q, the parameters underlying B0
n and B0
n, are all functions of
Dt ¼ T
n , there will be some work ahead to determine what are the limits of the two
complicated probability expressions in (8.56) as Dt ! 0. We cannot, however, con-
sider pursuing this analysis until we have some additional tools at our disposal from
chapter 9, and even then the derivation will be seen to be subtle and somewhat chal-
lenging. We will also develop another approach using the chapter 10 tools, which cir-
cumvents the explicit analysis of u, d, q, and q as functions of Dt, or rather, studies
this dependence from a di¤erent perspective using a new set of tools. This analysis
will also be seen to be subtle and somewhat challenging. Both derivations will stand
as testament to the depth and insight of the Black–Scholes–Merton results.
However, given the result above in section 8.8.2 on the limiting distribution of eq-
uity prices in the real world binomial lattice, it should not surprise the reader that
both binomial random variables in (8.56) will be shown to converge in chapter 9 to
normal variables:
BðnÞ ! N
r þ 1
2 s2


T; s2T


;
BðnÞ ! N
r  1
2 s2


T; s2T


;
as n ! y, or equivalently, as Dt ! 0.
Remark 8.33
Interestingly, within the real world binomial lattice analysis, the random
variable that was normalized, Pn
j¼1 Bj, was a summation of binomials for which the
probability p of u was fixed and independent of n but where the two values assumed
by each Bj, u and d, changed with n. In the binomial models needed for option pricing,
the random variable that is normalized is again of the form Pn
j¼1 Bj, with each Bj the
404
Chapter 8
Fundamental Probability Theorems

same binomial as before, but where the probabilities that Bj ¼ uðDtÞ, which are q or q,
also now change with n.
Assume for now this conclusion about the limiting distributions of the variables
BðnÞ and BðnÞ. Then B0
ðnÞ and B0
ðnÞ converge to the unit normal distribution. In other
words,
Pr B0
ðnÞ b
ln K
S0
h i
 mn
sn
2
4
3
5 ! Pr Z b
ln K
S0
h i
 r þ 1
2 s2


T
s
ffiffiffiffi
T
p
2
4
3
5:
Because of the symmetry of the unit normal distribution, we have from (8.32) that
Pr½Z b d1 ¼ Pr½Z a d1 ¼ Fðd1Þ, where F denotes the unit normal distribution
function. Similarly the second probability statement can be expressed as Pr½Z b
d2 ¼ Pr½Z a d2 ¼ Fðd2Þ.
Putting everything together, one arrives at the famous Black–Scholes–Merton for-
mula for the price of a European call option, named for Fischer Black (1938–1995),
Myron S. Scholes (b. 1941), and Robert C. Merton (b. 1944), for research published
in papers by Black and Scholes, and Merton in the early 1970s, and for which Mer-
ton and Scholes received the 1997 Nobel Prize in Economics (sadly, such awards are
not made posthumously).
The final result for a European call option is
LC
0 ðS0Þ ¼ S0Fðd1Þ  erTKFðd2Þ;
ð8:57aÞ
d1 ¼ ln S0
K þ r þ 1
2 s2


T
s
ffiffiffiffi
T
p
;
ð8:57bÞ
d2 ¼ ln S0
K þ r  1
2 s2


T
s
ffiffiffiffi
T
p
:
ð8:57cÞ
The related result for a European put option is
LP
0 ðS0Þ ¼ erTKFðd2Þ  S0Fðd1Þ:
ð8:58Þ
The approach used by Black–Scholes and Merton was close in spirit to that above,
in the sense that they were able to replicate the option with a portfolio of stock and
T-bills. They then concluded that the option must have a price equal to the price of
this replicating portfolio. However, they used the advanced tools of stochastic calcu-
lus for this development (which will not be addressed until my next book, Advanced
8.8
Applications to Finance
405

Quantitative Finance, as mentioned in the Introduction). The approach taken here
and in chapter 7, which used a binomial lattice approximation to stock price move-
ments, and then replicated the option and evaluated the limit as Dt ! 0, is known as
the Cox–Ross–Rubinstein binomial lattice model for option pricing. It was developed
in a paper in the late 1970s by John C. Cox, Stephen A. Ross, and Mark Rubinstein.
Remark 8.34
Using a binomial lattice with time step Dt to evaluate the price of a Eu-
ropean option or other derivative security, which results in an application of (7.147),
produces a price L0ðS0Þ 1 L0ðS0; DtÞ. This price reflects what is known as discretiza-
tion error. In other words, the theoretically correct answer is obtained as Dt ! 0, and
the lattice produces an error eDðDtÞ ¼ L0ðS0; 0Þ  L0ðS0; DtÞ, which is caused by dis-
cretizing time and the p.d.f. of stock price movements. One consequence of this dis-
cretization is that for any Dt, the calculated value of L0ðS0; DtÞ explicitly reflects the
stock’s mean log-ratio return m as well as the real world probability used in the calibra-
tion, p, through the formulas for q, u, and d. For any Dt, the calculated value of the
derivatives price will consequently vary somewhat as these parameters change. How-
ever, as one can explicitly appreciate in the Black–Scholes–Merton formulas, and will
be seen to be true generally as Dt ! 0, these dependencies of option price on both m and
p disappear. Indeed in the formulas above there is no vestige of either parameter pres-
ent, and in chapter 9 we will return to this point and observe this transition. In contrast,
the variance of the stock’s log-ratio return, s2, is quite evident in the final formulas, as
is the risk-free rate, r.
8.8.4
Scenario-Based European Option Prices as N ? T
The Model
If N-paths are randomly generated, and fS j
ngn
j¼0 denotes the n þ 1 possible stock
prices in the recombining lattice in section 8.8.3 above at time nDt ¼ T, it is of inter-
est to analyze the number of paths that arrive at each final state. In theory, we know
from the lattice analysis in section 8.8.2 that the distribution of stock prices at time n
is binomially distributed in the real world with parameters n, p in general, and hence
Pr½Sn ¼ S j
n ¼
n
j
 	
p jð1  pÞnj. As in chapter 7, p denotes the probability of a u-
return, p0 ¼ 1  p the probability of a d-return, and stock prices are parametrized
so that j ¼ 0 corresponds to the lowest price, S0
n ¼ endS0, and j ¼ n corresponds to
the highest price, S n
n ¼ enuS0.
On the other hand, we have shown that for the purposes of option pricing, we con-
tinue to use the stock price returns of eu and ed but switch the assumed probability of
an upstate return from the real world probability p to the risk-neutral probability q
given in (8.52) above.
406
Chapter 8
Fundamental Probability Theorems

In the lattice-based model these q-probabilities determine the likelihood of each
final equity price state that is relevant for option pricing. Consequently, if Nj denotes
the number that terminate at price S j
n from a sample of N paths so that P Nj ¼ N,
then the ðn þ 1Þ-tuple of integers ðN0; N1; . . . ; NnÞ has a multinomial distribution
with parameters N and fQjgn
j¼0, where Qj ¼
n
j
 	
q jð1  qÞnj. From (7.105) and
(7.106) we conclude that
E½Nj ¼ NQj;
Var½Nj ¼ NQjð1  QjÞ;
Cov½Qj; Qk ¼ NQjQk:
In a nonrecombining lattice, Qj is again defined as the risk-neutral probability of ter-
minating at price S j
n; only then there are 2n stock prices rather than n þ 1. The multi-
nomial distribution is again applicable in this case, as are the moment formulas above.
We now formalize the methodology for pricing an n-period European option using
the scenario-based methodology introduced in section 7.8.7. For simplicity, we focus
on the recombining lattice model, although the development is equally applicable in
the more general case. To this end, let LðS j
nÞ denote the exercise value of the option
or other derivative at time n when the stock price S j
n prevails. Also assume that a
time step of Dt 1 T
n has been chosen as in section 8.8.3, and that the binomial lattice
is calibrated as in (8.52), (8.53), and (8.54).
Given N paths, define a random variable ON, the sample option price, as in (7.150):
ON ¼ erT
N
X
n
j¼0
NjLðS j
nÞ:
ð8:59Þ
The random variable ON is an estimate of the true option price based on a sample of
size N. As was noted in section 7.8.7, the actual lattice-based price can be expressed
L0ðS0Þ ¼ erT X
n
j¼0
E Nj
N


LðS j
nÞ;
and so the sample option price replaces the correct probability weight of E
Nj
N
h i
¼ Qj
with the sample-based estimate of Nj
N .
Option Price Estimates as N ? T
We would expect that since the paths are generated in such a way as to arrive at each
final stock price with the correct probability, the expected value of this random vari-
able ought to equal L0ðS0Þ, the value produced on the lattice with (7.147). Even
more important, as N increases, we will prove that the probability that we are in
error by any given amount goes to 0. The main result is as follows:
8.8
Applications to Finance
407

Proposition 8.35
With ON defined as in (8.59):
1. The expected value of ON equals the lattice-based option price
E½ON ¼ L0ðS0Þ:
ð8:60Þ
2. If Var½LðS j
nÞ < y, where this variance is defined under fQjg, then for any  > 0,
Pr½jON  L0ðS0Þj >  ! 0
as N ! y:
ð8:61Þ
Proof
For property 1,
E½ON ¼ erT X
n
j¼0
E Nj
N


LðS j
nÞ ¼ L0ðS0Þ;
since E
Nj
N
h i
¼ Qj by (7.105). To demonstrate property 2, we use the Chebyshev in-
equality, which requires the variance of ON. To this end, first note that using (7.56)
obtains
Var½ON ¼ e2rT
N 2
X
n
j¼0
Var½NjL2ðS j
nÞ þ 2e2rT
N 2
X
j<k
Cov½Nj; NkLðS j
nÞLðS k
n Þ
¼ e2rT
N 2
X
n
j¼0
NQjð1  QjÞL2ðS j
nÞ  2
X
j<k
NQjQkLðS j
nÞLðS k
n Þ
"
#
¼ e2rT
N
X
n
j¼0
QjL2ðS j
nÞ 
X
n
j¼0
QjLðS j
nÞ
 
!2
2
4
3
5
¼ e2rT
N
Var½LðS j
nÞ:
Note that in the last step we used the identity that under fQjg, Var½LðS j
nÞ ¼
E½L2ðS j
nÞ  ½E½LðS j
nÞ2. From this derivation we conclude that as N ! y, we
have Var½ON ! 0. Now, by Chebyshev’s inequality, since E½ON ¼ L0ðS0Þ by prop-
erty 1,
Pr½jON  L0ðS0Þj >  < Var½ON
2
;
completing the proof.
n
408
Chapter 8
Fundamental Probability Theorems

Remark 8.36
1. The price of a European derivative security obtained with the scenario-based model
above will contain two types of error compared to the theoretically correct price.
Denoting the price obtained with N-paths and time steps of Dt by ONðDtÞ, the errors
are
 Discretization error, which is identical to that produced by the underlying lattice-
based calculation and depends on Dt. This error is defined in remark 8.34 as
eDðDtÞ ¼ L0ðS0; 0Þ  L0ðS0; DtÞ:
 Estimation error, which is defined as
eEðDtÞ ¼ L0ðS0; DtÞ  ONðDtÞ;
is the error between the scenario-based option price estimate and the lattice-based
value.
2. As was seen in the proof above, the estimation error decreases with 1
N in the sense
that
Pr½jL0ðS0; DtÞ  ONðDtÞj >  < e2rT Var½LðS j
nÞ
N2
:
Consequently, as was observed in proposition 8.12, we can choose N ! 0 in such a
way that N2
N ! y and thereby ensure that as N ! y, all estimation error is theoret-
ically eliminated. In practice, however, this elimination of error will be a slow and pain-
ful process, since in order for N2
N ! y it will be necessary to have N ! 0 slowly
and/or have N2
N ! y slowly. For example, if  ¼
1
N a for 0 < a < 1
2 , both objectives
are achieved, where a @ 1
2 provides faster N ! 0 and slower N2
N ! y, and a @ 0
does the opposite.
Scenario-Based Prices and Replication
As the last question for this section on scenario-based option pricing, we investigate
the connection between option pricing based on sample scenarios and option pricing
based on replication. First o¤, from (7.145), we know that replication-based prices
can be rebalanced period to period. Rewriting that formula to reflect a period of
length Dt produces
L0ðS0Þ ¼ erDt½qLðS u
1 Þ þ q0LðS d
1 Þ:
8.8
Applications to Finance
409

Consequently, from the first conclusion of the proposition above, with the analogous
notation
E½ON ¼ erDt½qE½Ou
N þ q0E½Od
N;
the expected values of the scenario-based prices can also be rebalanced.
To investigate the one-period rebalancing of ON to one of Ou
N and Od
N, an assump-
tion needs to be made about the collection of scenarios used for the latter calcula-
tions. We first assume that Ou
N is evaluated on the subset of the N original paths
that start with a u, of which there are N u, and similarly assume that Od
N is evaluated
on the subset of the N original paths that start with a d, of which there are N d, and
so N u þ N d ¼ N.
Next rewrite (8.59) as
ON ¼ erT
N
X
n
j¼1
N u
j LðS j
nÞ þ
X
n1
j¼0
N d
j LðS j
nÞ
"
#
;
where fN u
j g is defined as the number of paths from the N u subset that end at S j
n, and
similarly for fN d
j g, where it is apparent by definition that N u
0 ¼ N d
n ¼ 0.
Now to price Ou
N and Od
N on these subsets of paths, we derive that
Ou
N u ¼ erðTDtÞ
N u
X
n
j¼1
N u
j LðS j
nÞ;
Od
N d ¼ erðTDtÞ
N d
X
n1
j¼0
N d
j LðS j
nÞ:
Finally, with a bit of algebra is obtained
ON ¼ erDt½q½auOu
N u þ q0½adOd
N d;
ð8:62Þ
where
au ¼ N u
Nq ;
ad ¼ N d
Nq0 :
In summary, with Ou
N and Od
N priced on the subsets of the original paths, ON is the
price of a replicating portfolio that will rebalance to auOu
N and adOd
N in the next
period, and not Ou
N and Od
N. So there is additional error in this rebalancing related
to how far from 1 the au and ad terms are. Of course,
410
Chapter 8
Fundamental Probability Theorems

E½au ¼ E½ad ¼ 1;
Var½au ¼ q0
Nq ;
Var½ad ¼
q
Nq0 ;
so for large N the rebalancing error over one period will be small. However, the pro-
cess cannot be repeated to maturity because in each step the estimated prices are
based on fewer and fewer paths.
Alternatively, if Ou
N and Od
N are priced on new collections of N-paths each, there
will be additional rebalancing error. Specifically, we obtain
ON ¼ erDt½q½buOu
N þ q0½bdOd
N;
ð8:63Þ
where
bu ¼ auOu
N u
Ou
N
;
bd ¼ adOd
N u
Od
N
:
In other words, ON will equal the price of a portfolio that replicates values of buOu
N
and bdOd
N.
Exercises
Practice Exercises
1. Show that if f ðxÞ is a discrete probability function, with m.g.f. MðtÞ, then for any
real number t > 0,
Pr½X b t a MðtÞ
et2 :
(Hint: MðtÞ b P
jxijbt etxif ðxiÞ.)
2. Market observers sometimes talk about 5-sigma or 10-sigma events, where sigma
is the standard deviation. Such a statement is often used in the context of, ‘‘who
could have possibly predicted this event?’’ as if all random variables were known to
be normally distributed, and for which the probabilities of such events are indeed
miniscule.
(a) Using the Chebyshev inequality, calculate the upper bound for the probability of
a 5-sigma or worse event. A 10-sigma or worse event.
(b) Repeat part (a) using the one-sided Chebyshev inequality.
Exercises
411

3. Apply the weak law of large numbers to determine the necessary sample size in
the following cases to have 95% confidence:
(a) For the standard binomial distribution, estimate p to three decimal places
ð ¼ 0:0005Þ if it is known that 0:1 a p a 0:5.
(b) For the negative binomial distribution with k ¼ 10, estimate m to two decimal
places, where it is known that p a 0:1.
4. Using
the
De
Moivre–Laplace
theorem
(Hint:
Recall
the
half-interval
adjustment.):
(a) Approximate the probability that in one million flips of a biased coin with
Pr½H ¼ 0:65, the number of heads will be between 649,500 and 650,000.
(b) Approximate the probability that the number of tails will be 700,000 or more.
5. Using the central limit theorem (Hint: Recall the half-interval adjustment.):
(a) Approximate the probability of ^X b 79 in a Poisson distribution with l ¼ 75,
where ^X is a sample average of 50 independent trials.
(b) Approximate the probability of 76 a ^X a 78, with ^X based on a sample of 100.
6. Generalize the calibration of the growth model for stock prices in (8.45) to de-
velop formulas for u and d for arbitrary p, 0 < p < 1, and Dt.
7. Using the result of exercise 6, express SmDt in terms of S0 in two ways, paralleling
the formulas in (7.137) and (7.138) but for general p and Dt, and being explicit about
the binomial probabilities that govern the associated price lattice.
8. Demonstrate the following two properties of moment-generating functions, where
X and Xi are discrete random variables, using the definition and properties of
expectations:
(a) MaþbXðtÞ ¼ eatMXðbtÞ
(b) MT XiðtÞ ¼ Q MXiðtÞ if fXig are independent.
9. Using properties of the moment-generating function, show that if fBjg in the bi-
nomial lattice model are assumed to be independent and binomially distributed, then
this will not imply that fBkðDtÞg are binomially distributed. (Hint: See exercise 8(b).)
10. Recall the claims model of exercise 18 of chapter 7:
(a) For both the individual and aggregate risk model estimates of the mean and vari-
ance of claims, apply the Chebyshev inequality in (8.36) to estimate the probability
that claims exceed $8 million, $9.5 million, and $11 million.
(b) Estimate the probabilities from part (a) directly by a simulation method, with
1000 simulations, using (8.38).
412
Chapter 8
Fundamental Probability Theorems

(c) Using the simulations from part (b), and C0 ¼ $7.5 million, estimate the condi-
tional means and variances of the two models, and with these results estimate the
probabilities in part (a) using (8.40).
11. (Compare with exercise 24 of chapter 7Þ Price a two-year European call, with
strike price of 100, in the following ways. The stock price is S0 ¼ 100, and based on
time steps of Dt ¼ 0:25 years, the quarterly log-ratios have been estimated to have
mQ ¼ 0:02, and s2
Q ¼ ð0:07Þ2. The annual continuous risk-free rate is r ¼ 0:048.
(a) Develop a real world lattice of stock prices, with p ¼ 1
2 and time steps with
Dt ¼ 0:05, and price this option using (7.147) with the appropriate value of q.
(b) Evaluate the two prices of this option at time t ¼ 0:05 from part (a), and con-
struct a replicating portfolio at t ¼ 0 for these prices. Demonstrate that the cost of
this replicating portfolio equals the price obtained in part (a).
(c) Price this option using (7.147) with the appropriate value of q based on a lattice
for which p ¼ 0:75.
(d) Generate 500 two-year paths in the risk-neutral world using the same model as
part (a), and estimate the price of this option using (7.150) by counting how many
scenarios end in each stock price at time 2 years.
12. Generate another 99 prices for the exercise in 11(d) above, by generating another
99 batches of 500 two-year paths.
(a) Calculate the estimated price ON using all N ¼ 50;000 paths, and show that this
is equivalent to simply averaging the 100 batch prices.
(b) Calculate the variance of the 100 batch prices, Var½O500, and use this to estimate
the variance of the estimated price in part (a), Var½ON. (Hint: Recall that as a ran-
dom variable ON is the average of 100 prices.)
(c) With L0ðS0Þ defined as the lattice price obtained in exercise 11(a), and using
Var½O500 from part (b), compare for various values of  the proportion of the 100
prices that satisfy jO500  L0ðS0Þj >  to the upper bound for the probability of this
event, Var½O500
2
, developed in proposition 8.35.
Assignment Exercises
13. Let X be a discrete random variable.
(a) Prove that if mjnj a C for all n, then Pr½jX  mj b t ¼ 0 for any t > 1. In other
words, it must be the case that Pr½jX  mj a 1 ¼ 1: (Hint: Chebyshev.)
(b) Generalize part (a). Prove that if mjnj a C n for all n, then Pr½jX  mj b t ¼ 0 for
any t > C.
Exercises
413

(c) Conclude that if X has unbounded range, then it cannot be the case that
mjnj a C n for any C.
14. Apply the weak law of large numbers to determine the necessary sample size in
the following cases to have 95% confidence:
(a) For the geometric distribution, estimate the unbiased variance to one decimal
place, where it is know that p > 0:25 (Hint: For the geometric, m4 ¼ q
p2
1 þ 9q
p2

	
.)
(b) For the Poisson distribution, estimate l to two decimal places where it is known
that l > 2.
15. Demonstrate that in the proof of the weak law of large numbers:
Pr½j ^X  mj >  a Pr j ^Yj > 
2


þ Pr j ^Zj > 
2


:
(Hint: By the triangle inequality, j ^X  mj a j ^Yj þ j ^Zj, and hence, if both j ^Yj a 
2 and
j ^Zj a 
2 ,
then
j ^X  mj a .
Define
events
A; B; C HS
by
A ¼ fðX1; . . . ; XnÞ j
j ^Xn  mj a g, B ¼ ðX1; . . . ; XnÞ j j ^Yj a 
2


, and C ¼ ðX1; . . . ; XnÞ j j ^Zj a 
2


. Then
justify B V C H A, and use De Morgan’s laws.)
16. Using
the
De
Moivre–Laplace
theorem
(Hint:
Recall
the
half-interval
adjustment.):
(a) Approximate the probability that in one million flips of a biased coin with
Pr½H ¼ 0:15, the number of heads will be between 0 and 145,000 or between
149,500 and 150,000.
(b) Approximate the probability that the number of heads will be within 100 of the
expected value.
17. Assuming that all the properties of expectations developed for discrete random
variables apply to continuous random variables as well, derive (8.31) from (8.30).
18. Using the central limit theorem (Hint: Recall the half-interval adjustment.):
(a) Approximate the probability of ^X b 10 in a geometric distribution with p ¼ 0:15,
where ^X represents an average from a sample of 40 trials.
(b) Approximate the probability of 4 a ^X a 8 where ^X is based on a sample of 60
from the same geometric distribution.
19. Demonstrate the following two properties of characteristic functions, where
X and Xi are discrete random variables, using the definition and properties of
expectations:
(a) CaþbXðtÞ ¼ eiatCXðbtÞ
(b) CT XiðtÞ ¼ Q CXiðtÞ if fXig are independent
414
Chapter 8
Fundamental Probability Theorems

20. Recall the credit model of exercise 36 of chapter 7:
(a) For both the individual and aggregate risk model estimates of the mean and vari-
ance of losses, apply the Chebyshev inequality in (8.36) to estimate the probability
that losses exceed $8 million, $11 million, and $14 million.
(b) Estimate the probabilities from part (a) directly by a simulation method, with
1000 simulations, using (8.38).
(c) Using the simulations from part (b), and C0 ¼ $6 million, estimate the condi-
tional means and variances of the two models, and with these results estimate the
probabilities in part (a) using (8.40).
21. (Compare with exercise 40 of chapter 7:Þ Price a two-year European put, with
strike price of 100, in the following ways. The stock price is S0 ¼ 100, and based on
time steps of Dt ¼ 0:25 years, the quarterly log-ratios have been estimated to have:
mQ ¼ 0:025, and s2
Q ¼ ð0:09Þ2. The annual continuous risk-free rate is r ¼ 0:06.
(a) Develop a real world lattice of stock prices, with p ¼ 1
2 and time steps with
Dt ¼ 0:05, and price this option using (7.147) with the appropriate value of q.
(b) Evaluate the two prices of this option at time t ¼ 0:05 using the same method as
part (a), and construct a replicating portfolio at t ¼ 0 for these prices. Demonstrate
that the cost of this replicating portfolio equals the price obtained in part (a).
(c) Price this option using (7.147) with the appropriate value of q based on a lattice
for which p ¼ 0:25.
(d) Generate 500 two-year paths in the risk neutral world using the same model as
part (a), and estimate the price of this option using (7.150) by counting how many
scenarios end in each stock price at time 2 years.
22. Generate another 99 prices to the exercise in 21(d) above, by generating another
99 batches of 500 two-year paths.
(a) Calculate the estimated price ON using all N ¼ 50;000 paths, and show that this
is equivalent to simply averaging the 100 batch prices.
(b) Calculate the variance of the batch prices, Var½O500, and use this to estimate the
variance of the estimated price in part (a), Var½ON. (Hint: Recall that as a random
variable ON is the average of 100 prices.)
(c) With L0ðS0Þ defined as the lattice price obtained in exercise 21(a), and using
Var½O500 from part (b), compare for various values of  the proportion of the 100
prices that satisfy jO500  L0ðS0Þj >  to the upper bound for the probability of this
event, Var½O500
2
, developed in proposition 8.35.
Exercises
415


