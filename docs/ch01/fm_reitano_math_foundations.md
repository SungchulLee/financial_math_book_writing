# Mathematical Foundations for Quantitative Finance

!!! info "Source"
    **An Introduction to Quantitative Finance** by Robert R. Reitano, MIT Press.
    These notes are used for educational purposes.

## Mathematical Logic

1 Mathematical Logic
1.1
Introduction
Nearly everyone thinks they know what logic is but will admit the di‰culty in for-
mally defining it, or will protest that such a formal definition is not necessary because
its meaning is obvious. For example, we all like to stop an adversary in an argument
with the statement ‘‘that conclusion is illogical,’’ or attempt to secure our own vic-
tory by proclaiming ‘‘logic demands that my conclusion is correct.’’ But if compelled
in either instance, it may be di‰cult to formalize in what way logic provides the
desired conclusion.
A legal trial can be all about attempts at drawing logical conclusions. The prose-
cution is trying to prove that the accused is guilty based on the so-called facts. The
defense team is trying to prove the improbability of guilt, or indeed even innocence,
based on the same or another set of facts. In this example, however, there is an asym-
metry in the burden of proof. The defense team does not have to prove innocence.
Of course, if such a proof can be presented, one expects a not guilty verdict for the
accused. The burden of proof instead rests on the prosecution, in that they must
prove guilt, at least to some legal standard; if they cannot do so, the accused is
deemed not guilty.
Consequently a defense tactic is often focused not on attempting to prove inno-
cence but rather on demonstrating that the prosecution’s attempt to prove guilt is
faulty. This might be accomplished by demonstrating that some of the claimed facts
are in doubt, perhaps due to the existence of additional facts, or by arguing that even
given these facts, the conclusion of guilt does not necessarily follow ‘‘logically.’’ That
is, the conclusion may be consistent with but not compelled by the facts. In such a
case the facts, or evidence, is called ‘‘circumstantial.’’
What is clear is that the subject of logic applies to the drawing of conclusions, or
to the formulation of inferences. It is, in a sense, the science of good reasoning. At its
simplest, logic addresses circumstances under which one can correctly conclude that
‘‘B follows from A,’’ or that ‘‘A implies B,’’ or again, ‘‘If A, then B.’’ Most would
informally say that an inference or conclusion is logical if it makes sense relative to
experience. More specifically, one might say that a conclusion follows logically from
a statement or series of statements if the truth of the conclusion is guaranteed by, or
at least compelled by, the truth of the preceding statement or statements.
For example, imagine an accused who is charged with robbing a store in the dark
of night. The prosecution presents their facts: prior criminal record; eyewitness ac-
count that the perpetrator had the same height, weight, and hair color; roommate
testimony that the accused was not home the night of the robbery; and the accused’s
inability to prove his whereabouts on the evening in question. To be sure, all these

facts are consistent with a conclusion of guilt, but they also clearly do not compel
such a conclusion. Even a more detailed eyewitness account might be challenged,
since this crime occurred at night and visibility was presumably impaired. A fact
that would be harder to challenge might be the accused’s possession of many expen-
sive items from the store, without possession of sales receipts, although even this
would not be an irrefutable fact. ‘‘Who keeps receipts?’’ the defense team asserts!
The world of mathematical theories and proofs shares features with this trial ex-
ample. For one, a mathematician claiming the validity of a result has the burden of
proof to demonstrate this result is true. For example, if I assert the claim,
For any two integers N and M, it is true that M þ N ¼ N þ M,
I have the burden of demonstrating that such a conclusion is compelled by a set of
facts. A jury of my mathematical peers will then evaluate the validity of the assumed
facts, as well as the quality of the logic or reasoning applied to these facts to reach
the claimed conclusion. If this jury determines that my assumed facts or logic is inad-
equate, they will deem the conclusion ‘‘not proved.’’ In the same way that a failed
attempt to prove guilt is not a proof of innocence, a failed proof of truth is not a
proof of falsehood. Typically there is no single judge who oversees such a mathemat-
ical process, but in this case every jury member is a judge.
Imagine if in mathematics the burden of proof was not as described above but in-
stead reversed. Imagine if an acceptable proof of the claim above regarding N and M
was: ‘‘It must be true because you cannot prove it is false.’’ The consequence of this
would be parallel to that of reversing the burden of proof in a trial where the prose-
cution proclaims: ‘‘The accused must be guilty because he cannot prove he is inno-
cent.’’ Namely, in the case of trials, many innocent people would be punished, and
perhaps at a later date their innocence demonstrated. In the case of mathematics,
many false results would be believed to be true, and almost certainly their falsity
would ultimately be demonstrated at a later date. Our jails would be full of the inno-
cent people; our math books, full of questionable and indeed false theory.
In contrast to an assertion of the validity of a result, if I claim that a given state-
ment is false, I simply need to supply a single example, which would be called a
‘‘counterexample’’ to the statement. For example, the claim,
For any integer A, there is an integer B so that A ¼ 2B,
can be proved to be false, or disproved, by the simple counterexample: A ¼ 3.
What distinguishes these two approaches to proof is not related to the asserted
statement being true or false, but to an asymmetry that exists in the approach to the
presentation of mathematical theory. Mathematicians are typically interested in
2
Chapter 1
Mathematical Logic

whether a general result is always true or not always true. In the first case, a general
proof is required, whereas in the second, a single counterexample su‰ces. On the
other hand, if one attempted to prove that a result is always false, or not always
false, again in the first case, a general proof would be required, whereas in the sec-
ond, a single counterexample would su‰ce. The asymmetry that exists is that one
rarely sees propositions in mathematics stated in terms of a result that is always false,
or not always false. Mathematicians tend to focus on ‘‘positive’’ results, as well as
counterexamples to a positive result, and rarely pursue the opposite perspective. Of
course, this is more a matter of semantic preference than theoretical preference. A
mathematician has no need to state a proposition in terms of ‘‘a given statement is
always false’’ when an equivalent and more positive perspective would be that ‘‘the
negative of the given statement is always true.’’ Why prove that ‘‘2x ¼ x is always
false if x 0 0’’ when you can prove that ‘‘for all x 0 0, it is true that 2x 0 x.’’
What distinguishes logic in the real world from the logic needed in mathematics
is that in the real world the determination that A follows from B often reflects the
human experience of the observers, for example, the judge and jury, as well as rules
specified in the law. This is reinforced in the case of a criminal trial where the jury is
given an explicit qualitative standard such as ‘‘beyond a reasonable doubt.’’ In this
case the jury does not have to receive evidence of the guilt of the accused that con-
vinces with 100 percent conviction, only that the evidence does so beyond a reason-
able doubt based on their human experiences and instincts, as further defined and
exemplified by the judge.
In mathematics one wants logical conclusions of truth to be far more secure than
simply dependent on the reasonable doubts of the jury of mathematicians. As math-
ematics is a cumulative science, each work is built on the foundation of prior results.
Consequently the discovery of any error, however improbable, would have far-
reaching implications that would also be enormously di‰cult to track down and rec-
tify. So not surprisingly, the goal for mathematical logic is that every conclusion will
be immutable, inviolate, and once drawn, never to be overturned or contradicted in
the future with the emergence of new information. Mathematics cannot be built as a
house of cards that at a later date is discovered to be unstable and prone to collapse.
In contrast, in the natural sciences, the burden of proof allowed is often closer to
that discussed above in a legal trial. In natural sciences, the first requirement of a
theory is that it be consistent with observations. In mathematics, the first requirement
of a theory is that it be consistent, rigorously developed, and permanent. While it is
always the case that mathematical theories are expanded upon, and sometimes be-
come more or less in vogue depending on the level of excitement surrounding the de-
velopment of new insights, it should never be the case that a theory is discarded
1.1
Introduction
3

because it is discovered to be faulty. The natural sciences, which have the added bur-
den of consistency with observations, can be expected to significantly change over
time and previously successful theories even abandoned as new observations are
made that current theories are unable to adequately explain.
1.2
Axiomatic Theory
From the discussion above it should be no surprise that structure is desired of every
mathematical theory:
1. Facts used in a proof are to be explicitly identified, and each is either assumed
true or proved true given other assumed or proved facts.
2. The rules of inference, namely the logic applied to these facts in proofs, are to be
‘‘correct,’’ and the definition of correct must be objective and immutable.
3. The collection of conclusions provable from the facts in item 1 using the logic in
item 2 and known as theorems, are to be consistent. That is, for no statement P will
the collection of theorems include both ‘‘statement P is true’’ and ‘‘the negation of
statement P is true.’’
4. The collection of all theorems is to be complete. That is, for every statement P, ei-
ther ‘‘statement P is a theorem’’ or ‘‘the negation of statement P is a theorem.’’ A
related but stronger condition is that the resulting theory is decidable, which means
that one can develop a procedure so that for any statement P, one can determine if
P is true or not true in a finite number of steps.
It may seem surprising that in item 1 the ‘‘truth’’ of the assumed facts was not the
first requirement, but that these facts be explicitly identified. It is natural that identi-
fication of the assumed facts is important to allow a mathematical jury to do its re-
view, but why not an absolute requirement of ‘‘truth’’? The short answer is, there are
no facts in mathematics that are ‘‘true’’ and yet at the same time dependent on no
other statements of fact. One cannot start with an empty set of facts and somehow
derive, with logic alone, a collection of conclusions that can be demonstrated to be
true.
Consequently some basic collection of facts must be assumed to be true, and these
will be the axioms of the theory. In other words, all mathematical theories are axiom-
atic theories, in that some basic set of facts must be assumed to be true, and based on
these, other facts proved. Of course, the axioms of a theory are not arbitrary. Math-
ematicians will choose the axioms so that in the given context their truth appears un-
deniable, or at least highly reasonable. This is what ensures that the theorems of the
4
Chapter 1
Mathematical Logic

mathematical theory in item 3, that is, the facts and conclusions that follow from
these axioms, will be useful in that given context.
Di¤erent mathematical theories will require di¤erent sets of axioms. What one
might assume as axioms to develop a theory of the integers will be di¤erent from
the axioms needed to develop a theory of plane geometry. Both sets will appear un-
deniably true in their given context, or at least quite reasonable and consistent with
experience. Moreover, even within a given subject matter, such as geometry, there
may be more than one context of interest, and hence more than one reasonable
choice for the axioms.
For example, the basic axioms assumed for plane geometry, or the geometry that
applies on a ‘‘flat’’ two-dimensional sheet, will logically be di¤erent from the axioms
one will need to develop spherical geometry, which is the geometry that applies on
the surface of a sphere, such as the earth. Which axioms are ‘‘true’’? The answer is
both, since both theories one can develop with these sets of axioms are useful in the
given contexts. That is, these sets of axioms can legitimately be claimed to be ‘‘true’’
because they imply theories that include many important and deep insights in the
given contexts.
That said, in mathematics one can and does also develop theories from sets of axi-
oms that may seem abstract and not have a readily observable context in the real
world. Yet these axioms can produce interesting and beautiful mathematical theories
that find real world relevance long after their initial development.
The general requirements on a set of axioms is that they are:
1. Adequate to develop an interesting and/or useful theory.
2. Consistent in that they cannot be used to prove both ‘‘statement P is true’’ and
‘‘the negation of statement P is true.’’
3. Minimal in that for aesthetic reasons, and because these are after all ‘‘assumed
truths,’’ it is desirable to have the simplest axioms, and the fewest number that ac-
complish the goal of producing an interesting and/or useful theory.
It is important to understand that the desirability, and indeed necessity, of framing
a mathematical theory in the context of an axiomatic theory is by no means a
modern invention. The earliest known exposition is in the Elements by Euclid of
Alexandria (ca. 325–265 BC), so Euclid is generally attributed with founding the ax-
iomatic method. The Elements introduced an axiomatic approach to two- and three-
dimensional geometry (called Euclidean geometry) as well as number theory. Like the
modern theories this treatise explicitly identifies axioms, which it classifies as ‘‘com-
mon notions’’ and ‘‘postulates,’’ and then proceeds to carefully deduce its theorems,
1.2
Axiomatic Theory
5

called ‘‘propositions.’’ Even by modern standards the Elements is a masterful exposi-
tion of the axiomatic method.
If there is one significant di¤erence from modern treatments of geometry and other
theories, it is that the Elements defines all the basic terms, such as point and line, be-
fore stating the axioms and deducing the theorems. Mathematicians today recognize
and accept the futility of attempting to define all terms. Every such definition uses
words and references that require further expansion, and on and on. Modern devel-
opments simply identify and accept certain notions as undefined—the so-called prim-
itive concepts—as the needed assumptions about the properties of these terms are
listed within the axioms.
1.3
Inferences
Euclid’s logical development in the Elements depends on ‘‘rules of inference’’ but
does not formally include logic as a theory in and of itself. A formal development
of the theory of logic was not pursued for almost two millennia, as mathematicians,
following Euclid, felt confident that ‘‘logic’’ as they applied it was irrefutable. For
instance, if we are trying to prove that a certain solution to an equation satisfies
x < 100, and instead our calculation reveals that x < 50, without further thought
we would proclaim to be done. Logically we have:
‘‘x < 50 implies that x < 100’’ is a true statement.
‘‘x < 50’’ is a true statement by the given calculation.
‘‘x < 100’’ is a true statement, by ‘‘deduction.’’
Abstractly: if P ) Q and P, then Q. Here we use the well-known symbol ) for
‘‘implies,’’ and agree that in this notation, all statements displayed are ‘‘true.’’ That
is, if P ) Q and P are true statements, then Q is a true statement. This is an example
of the direct method of proof applied to the conditional statement, P ) Q, which is
also called an implication.
In the example above note that even as we were attempting to implement an objec-
tive logical argument on the validity of the conclusion that x < 100, we would likely
have been simultaneously considering, and perhaps even biased by, the intuition we
had about the given context of the problem. In logic, one attempts to strip away all
context, and thereby strip away all intuition and bias. The logical conclusion we
drew about x is true if and only if we are comfortable with the following logical
statement in every context, for any meanings we might ever ascribe to the statements
P and Q:
6
Chapter 1
Mathematical Logic

If P ) Q and P, then Q.
In logic, it must be all or nothing. The rule of inference summarized above is known
as modus ponens, and it will be discussed in more detail below.
Another logical deduction we might make, and one a bit more subtle, is as follows:
‘‘x < 50 implies that x < 100’’ is a true statement.
‘‘x < 100’’ is not a true statement by demonstration.
‘‘x < 50’’ is not a true statement, by deduction.
Again, abstractly: if P ) Q and @Q, then @P. Here we use the symbol @Q to mean
‘‘the negation of Q is true,’’ which is ‘‘logic-speak’’ for ‘‘Q is false.’’ This is similar to
the ‘‘direct method of proof,’’ but applied to what will be called the contrapositive of
the conditional P ) Q, and consequently it can be considered an indirect method of
proof. Again, we can apply this logical deduction in the given context if and only if
we are comfortable with the following logical statement in every context:
If P ) Q and @Q, then @P.
The rule of inference summarized above is known as modus tollens, and will also be
discussed below.
Clearly, the logical structure of an argument can become much more complicated
and subtle than is implied by these very simple examples. The theory of mathemati-
cal logic creates a formal structure for addressing the validity of such arguments
within which general questions about axiomatic theories can be addressed. As it
turns out, there are a great many rules of inference that can be developed in mathe-
matical logic, but modus ponens plays the central role because other rules can be
deduced from it.
1.4
Paradoxes
One may wonder when and why mathematicians decided to become so formal with
the development of a mathematical theory of logic, collectively referred to as mathe-
matical logic, requiring an axiomatic structure and a formalization of rules of infer-
ence. An important motivation for increased formality has been the recognition that
even with early e¤orts to formalize, such as in Euclid’s Elements, mathematics has
not always been formal enough, and the result was the discovery of a host of para-
doxes throughout its history. A paradox is defined as a statement or collection of
statements which appear true but at the same time produce a contradiction or a
1.4
Paradoxes
7

conflict with one’s intuition. Some mathematical paradoxes in history where solved
by later developments of additional theory. That is, they were indicative of an incom-
plete or erroneous understanding of the theory, often as a consequence of erroneous
assumptions. Others were more fatal, in that they implied that the theory developed
was e¤ectively built as a house of cards and so required a firmer and more formal
theoretical foundation.
Of course, paradoxes also exist outside of mathematics. The simplest example is
the liar’s paradox:
This statement is false.
The statement is paradoxical because if it is true, then it must be false, and con-
versely, if false, it must be true. So the statement is both true and false, or neither
true nor false, and hence a paradox.
Returning to mathematics, sometimes an apparent paradox represents nothing
more than sleight of hand. Take, for instance, the ‘‘proof’’ that 1 ¼ 0, developed
from the following series of steps:
a ¼ 1;
a2 ¼ 1;
a2  a ¼ 0;
aða  1Þ ¼ 0;
a ¼ 0;
1 ¼ 0:
The sleight of hand here is obvious to many. We divided by a  1 before the fifth step,
but by the first, a  1 ¼ 0. So the paradoxical conclusion is created by the illegitimate
division by 0. Put another way, this derivation can be used to confirm the illegiti-
macy of division by zero, since to allow this is to allow the conclusion that 1 ¼ 0.
Sometimes the sleight of hand is more subtle, and strikes at the heart of our lack of
understanding and need for more formality. Take, again, the following deduction
that 1 ¼ 0:
A ¼ 1  1 þ 1  1 þ 1  1 þ 1    
¼ ð1  1Þ þ ð1  1Þ þ ð1  1Þ þ   
¼ 0:
8
Chapter 1
Mathematical Logic

A ¼ 1  ð1  1Þ  ð1  1Þ  ð1  1Þ    
¼ 1;
so once more, A ¼ 1 ¼ 0. The problem with this derivation relates to the legitimacy
of the grouping operations demonstrated; once grouped, there can be little doubt that
the sum of an infinite string of zeros must be zero. Because we know that such group-
ings are fine if the summation has only finitely many terms, the problem here must be
related to this example being an infinite sum. Chapter 6 on numerical series will de-
velop this topic in detail, but it will be seen that this infinite alternating sum cannot
be assigned a well-defined value, and that such grouping operations are mathemati-
cally legitimate only when such a sum is well-defined.
An example of an early and yet more complex paradox in mathematics is Zeno’s
paradox, arising from a mythical race between Achilles and a tortoise. Zeno of Elea
(ca. 490–430 BC) noted that if both are moving in the same direction, with Achilles
initially behind, Achilles can never pass the tortoise. He reasoned that at any mo-
ment that Achilles reaches a point on the road, the tortoise will have already arrived
at that point, and hence the tortoise will always remain ahead, no matter how fast
Achilles runs. This is a paradox for the obvious reason that we observe faster runners
passing slower runners all the time. But how can this argument be resolved?
Although this will be addressed formally in chapter 6, the resolution comes from
the demonstration that the infinite collection of observations that Zeno described be-
tween Achilles and the tortoise occur in a finite amount of time. Zeno’s conclusion of
paradox implicitly reflected the assumption that if in each of an infinite number of
observations the tortoise is ahead of Achilles, it must be the case that the tortoise is
ahead for all time. A formal resolution again requires the development of a theory in
which the sum of an infinite collection of numbers can be addressed, where in this
case each number represents the length of the time interval between observations.
Another paradox is referred to as the wheel of Aristotle. Aristotle of Stagira (384–
322 BC) imagined a wheel that has inner and outer concentric circles, as in the inner
and outer edges of a car tire. He then imagined a fixed line from the wheel’s hub
extending through these circles as the wheel rotates. Aristotle argued that at every
moment, there is a one-to-one correspondence between the points of intersection of
the line and the inner wheel, and the line and the outer wheel. Consequently the inner
and outer circles must have the same number of points and the same circumference, a
paradox. The resolution of this paradox lies in the fact that having a 1:1 correspon-
dence between the points on these two circles does not ensure that they have equal
lengths, but to formalize this required the development of the theory of infinite sets
many hundreds of years later. At the time of Aristotle it was not understood how two
1.4
Paradoxes
9

sets could be put in 1:1 correspondence and not be ‘‘equivalent’’ in their size or mea-
sure, as is apparently the case for two finite sets. Chapter 2 on number systems will
develop the topic of infinite sets further.
The final paradox is unlike the others in that it e¤ectively dealt a fatal blow to an
existing mathematical theory, and made it clear that the theory needed to be redevel-
oped more formally from the beginning. It is fair to say that the paradoxes above
didn’t identify any house of cards but only a situation that could not be appropri-
ately explained within the mathematical theory or understanding of that theory
developed to that date. The next paradox has many forms, but a favorite is called
the Barber’s paradox. As the story goes, in a town there is a barber that shaves
all the men that do not shave themselves, and only those men. The question is:
Does the barber shave himself? Similar to the liar’s paradox, we conclude that the
barber shaves himself if and only if he does not shave himself. The problem here
strikes at the heart of set theory, where it had previously been assumed that a set
could be defined as any collection satisfying a given criterion, and once defined, one
could determine unambiguously whether or not a given element is a member of the
set. Here the set is defined as the collection of individuals satisfying the criterion that
they don’t shave themselves, and we can get no logical conclusion as to whether or
not the barber is a member of this set.
An equivalent form of this paradox, and the form in which it was discovered by
Bertrand Russell (1872–1970) in 1901 and known as Russell’s paradox, makes this
set theory connection explicit. Let X denote the set of all sets that are not elements
of themselves. The paradox is that one concludes X to be an element of itself if and
only if it is not an element of itself. This discovery was instrumental in identifying the
need for, and motivating the development of, a more careful axiomatic approach to
set theory. Of course, the need for the development of a more formal axiomatic
theory for all mathematics was equally compelled, since if mathematics went astray
by defining an object as simple and intuitive as a set, who could be confident that
other potential crises didn’t loom elsewhere?
1.5
Propositional Logic
1.5.1
Truth Tables
Much of mathematical logic can be better understood once the concept of truth table
is introduced and basic relationships developed. The starting point is to define a
statement in a mathematical theory as any declarative sentence that is either true or
false, but not both. For example, ‘‘today the sky is blue’’ and ‘‘5 < 7’’ are statements.
An expression such as ‘‘x < 7’’ is not a statement because we cannot assign T or F to
10
Chapter 1
Mathematical Logic

it without knowing what value the variable x assumes. Such an expression will be
called a formula below. While a formula is not a statement because the variable x is
a free variable, it can be made into a statement by making x a bound variable. The
most common ways of accomplishing this is with the universal quantifier, E, and ex-
istential quantifier, b, defined as follows:
 Ex denotes: ‘‘for all x.’’
 bx denotes: ‘‘there exists an x such that.’’
For example, Ex ðx < 7Þ and bx ðx < 7Þ are now statements. The first, ‘‘for all x,
x is less than 7’’ is assigned an F; the second, ‘‘there exists an x such that x is less
than 7’’ is a T.
A truth table is a mechanical device for deciphering the truth or falsity of a
complicated statement based on the truth or falsity of its various substatements.
Complicated statements are constructed using statement connectives in various com-
binations. Of course, from the discussion above it should be no surprise that the
initial collection of true statements for a given mathematical theory would be the
‘‘assumed facts’’ or axioms of the theory. Truth tables then provide a mechanism
for determining the truth or falsity of more complicated statements that can be for-
mulated from these axioms and, as we will see, also provide a framework within
which one can evaluate the logical integrity of a given inference one makes in a
proof.
If P and Q are statements, we define the following statement connectives and pres-
ent the associated truth tables. Negation is a unary or singulary connective, whereas
the others are binary connectives. In each case the truth table identifies all possible
combinations of T or F for the given statements, denoted P or Q, and then assigns
a T or F to the defined statements.
1. Negation:
@P denotes the statement ‘‘not P.’’
P
@P
T
F
F
T
2. Conjunction:
P5Q denotes the statement ‘‘P and Q.’’
P
Q
P5Q
T
T
T
T
F
F
F
T
F
F
F
F
1.5
Propositional Logic
11

3. Disjunction:
P4Q denotes the statement ‘‘P or Q’’ but understood as ‘‘P
and/or Q.’’
P
Q
P4Q
T
T
T
T
F
T
F
T
T
F
F
F
4. Conditional:
P ) Q denotes the statement ‘‘P implies Q.’’
P
Q
P ) Q
T
T
T
T
F
F
F
T
T
F
F
T
5. Biconditional:
P , Q denotes the statement ‘‘P if and only if Q.’’
P
Q
P , Q
T
T
T
T
F
F
F
T
F
F
F
T
In other words, we have the following truth assignments, which are generally con-
sistent with common usage:
 @P has the opposite truth value as P.
 P5Q is true only when both P and Q are true.
 P4Q is true when at least one of P and Q are true.
 P ) Q is true unless P is T, and Q is F.
 P , Q is true when P and Q have the same truth values.
There may be two surprises here. First o¤, in mathematical logic the disjunctive ‘‘or’’
means ‘‘and/or.’’ In common language, ‘‘P or Q’’ usually means ‘‘P or Q but not
both.’’ If you are told, ‘‘your money or your life,’’ you do not expect an unfavorable
outcome after handing over your wallet. Obviously, if the thief is a mathematician,
there could be an unpleasant surprise.
12
Chapter 1
Mathematical Logic

An important consequence of this interpretation, which would not be true for the
common language notion, is that there is a logical symmetry between conjunction
and disjunction when negation is applied:
@ðP5QÞ , ð@PÞ4ð@QÞ;
@ðP4QÞ , ð@PÞ5ð@QÞ:
That is, the statement ‘‘P5Q’’ is false if and only if ‘‘either P is false or Q is false,’’
and the statement ‘‘P4Q’’ is false if and only if ‘‘both P is false and Q is false.’’
The equivalence of these statements follows from a truth table analysis that utilizes
the basic properties above. For example, the truth table for the first statement is:
P
Q
@(P5Q)
(@P)4(@Q)
@(P5Q) , (@P)4(@Q)
T
T
F
F
T
T
F
T
T
T
F
T
T
T
T
F
F
T
T
T
This demonstrates that the two statements always have the same truth values.
The second surprise relates to the conditional truth values in the last two rows of
the table, when P is false. Then, whether Q is true or false, the conditional P ) Q is
declared true. For example, let
P : There is a mispricing in the market,
Q : I will attempt to arbitrage.
So P ) Q is a statement I might make:
‘‘If there is a mispricing in the market, then I will attempt to arbitrage.’’
The question becomes, How would you evaluate whether or not my statement is
true? The truth table declares this statement true when P and Q are both true, and
so would you. In other words, if there was a mispricing and I attempted to arbitrage,
you would judge my statement true. Similarly, if P was true and I did not make this
attempt, you would judge my statement false, consistent with the second line in the
truth table.
Now assume that there was not a mispricing in the market today, and yet I was
observed to be attempting an arbitrage. Would my statement above be judged false?
What if in the same market, I did not attempt to arbitrage, would my statement be
deemed false? The truth table for the conditional states that in both cases my original
1.5
Propositional Logic
13

statement would be deemed true, although in the real world the likely conclusion
would be ‘‘not apparently false.’’ In other words, in these last two cases my actions
do not present evidence of the falsity of my statement, and hence the truth table
deems my statement ‘‘true.’’ Simply said, the truth table holds me truthful unless
proved untruthful, or innocent unless proved guilty.
A consequence of this truth table assignment for the conditional is that
ðP ) QÞ , @ðP5@QÞ:
In other words, P ) Q has exactly the same truth values as does @ðP5@QÞ. The
associated truth table is as follows:
P
Q
P ) Q
@(P5@Q)
(P ) Q) , @(P5@Q)
T
T
T
T
T
T
F
F
F
T
F
T
T
T
T
F
F
T
T
T
This truth table analysis and the one above were somewhat tedious, especially
when all the missing columns are added in detail, but note that they were entirely me-
chanical. No intuition was needed; we just apply in a methodical way the logic rules
as defined by the truth tables above.
These truth tables have another interpretation, and that is, for any statements P
and Q, and any truth values assigned, the statement
@ðP5QÞ , ð@PÞ4ð@QÞ;
is a tautology, which is to say that it is always true. The same can be said for the
biconditional statements illustrated above. Tautologies will be seen to form the foun-
dation for developing and evaluating rules of inference, and more specifically, the
logical integrity of a given proof.
There are many other tautologies possible, in fact infinitely many. One reason for
this is that there is redundancy in the list of connectives above:
@;5;4; ); ,:
In a formal treatment of mathematical logic, only @ and ) need be introduced, and
the others are then defined by the following statements, all of which are tautologies
in the framework above:
P4Q , @P ) Q;
14
Chapter 1
Mathematical Logic

P5Q , @ðP ) @QÞ;
ðP , QÞ , ðP ) QÞ5ðQ ) PÞ:
Note that the last statement can in turn be expressed in terms of only @ and ) using
the second tautology.
There is also redundancy between the universal and existential quantifiers. In
formal treatments one introduces the universal quantifier E and defines the existential
quantifier b by
bxPðxÞ , @Exð@PðxÞÞ:
In other words, ‘‘there exists an x so that statement PðxÞ is true’’ is the same as ‘‘it is
false that for all x the statement PðxÞ is false.’’
Admittedly, such definitional connections require one to pause for understanding,
and one might wonder why all the terms are simply not defined straightaway instead
of in the complicated ways above. The reason was noted earlier in the discussion on
axioms. One goal of an axiomatic structure is to be minimal, or at least parsimoni-
ous. The cost of this goal is often apparent complexity, as one might spend consider-
able e¤ort proving a statement that virtually everyone would be more than happy
just accepting as another axiom. But the goal of mathematical logic is not the avoid-
ance of complexity by adding more axioms; it is the illumination of the theory and
the avoidance of potential paradoxes by minimizing the number of axioms needed.
The fewer the axioms, the more transparent the theory becomes, and the less likely
the axioms will be in violation of another important goal of an axiomatic structure.
And that is consistency.
1.5.2
Framework of a Proof
In later chapters various statements will be made under the heading proposition,
which is the term used in this book for the more formal sounding theorem. These
terms are equivalent in mathematics, and the choice reflects style rather than sub-
stance. In virtually all cases, a ‘‘proof’’ of the statement will be provided. A lemma
is yet another name for the same thing, although it is generally accepted that a lemma
is considered a relatively minor result, whereas a proposition or theorem is a major
result. Some authors distinguish between proposition and theorem on the same basis,
with theorem used for the most important results.
This terminology is by no means universally accepted. For example, students of fi-
nance will undoubtedly encounter Ito’s lemma, and soon discover that in the theory
underlying the pricing of financial derivatives like options, this lemma is perhaps the
most important theoretical result in quantitative finance.
1.5
Propositional Logic
15

Now the typical structure for the statement of a proposition is
If P, then Q.
The statement P is the hypothesis of the proposition, and in some cases it will be a
complex statement with many substatements and connectives, while the statement Q
is the conclusion. The goal of this and the next section is to identify logical frame-
works for such proofs.
First o¤, a proof of the statement ‘‘If P, then Q’’ is not equivalent to a proof of
the statement ‘P ) Q’ despite their apparent equivalence in informal language. Spe-
cifically,
‘‘If P, then Q’’ means ‘‘if statement P is true, then statement Q is true,’’
whereas
‘P ) Q’ means ‘‘the statement P implies Q is true.’’
Of course, one is hardly interested in proving statements such as ‘P ) Q’ unless Q
can be asserted to be a true statement. That is the true goal of a proposition, to
achieve the conclusion that Q is true. However, the statement P ) Q was seen to be
true in three of the four cases displayed in the truth table above, and in only one of
these three cases is Q seen to be true. Namely the truth of ‘P ) Q’ assures the truth
of Q only when P is true. Consequently, if we want to prove the typical propositional
structure above, which is to say that we can infer the truth of statement Q from the
truth of statement P, we can prove the following:
If P and P ) Q, then Q.
If this statement is written in the notation of logic, it is in fact a tautology, and al-
ways true. That is, in the truth table of
P5ðP ) QÞ ) Q;
ð1:1Þ
we have that for any assignment of the truth values to P and Q, this statement has
constant truth value of ‘‘true.’’
This statement is the central rule of inference in logic, and it is known as modus
ponens. It says that:
If statement P is true, and the statement P ) Q is demonstrated as true, then Q
must be true.
This is the formal basis of many mathematical proofs of ‘‘If P, then Q.’’ Of course,
the language of the proof usually focuses on the development of the truth of the im-
16
Chapter 1
Mathematical Logic

plication: P ) Q, while the truth of the statement P, which is the hypothesis of the
theorem, is simply implied. Moreover, if P were false, the demonstration of the truth
of P ) Q would be for naught, since in this case Q could be true or false, as the truth
table above attests.
In the next section we investigate proof structures in more detail. The central idea
is every logical structure for a valid proof must be representable as a tautology, such
as the modus ponens structure in (1.1). As we have seen, it is straightforward and me-
chanical, though perhaps tedious, to verify that a given proof structure, however
complicated, is indeed a tautology. Here are a few other possible proof structures
that are tautologies intuitively, as well as relatively easy to demonstrate in a truth
table. Each is simply related to a single line on one of the basic truth tables given
for the connectives:
P5ðP5QÞ ) Q;
ðP4QÞ5@Q ) P;
ðP , QÞ5@Q ) @P:
For example, on the truth table for P5Q, the only row where both P and P5Q
are true is the row where Q is also true. In any other row, one or both of P and P5Q
are false, and hence the conjunction P5ðP5QÞ is false, assuring that the conditional
P5ðP5QÞ ) Q is true. That is exactly how this statement becomes a tautology,
and this logic will be seen to hold in all such cases. Specifically, when the hypothesis
of the proposition is a conjunction, as is typically the case, we only really have to
evaluate the case where all substatements are true, and assure that the conclusion is
then true in this case. In all other cases the conjunction will be false and the condi-
tional automatically true.
1.5.3
Methods of Proof
With modus ponens in the background, the essence of virtually any mathematical
proof is a demonstration of the truth of the implication P ) Q. To this end, the first
choice one has is to prove the direct conditional statement P ) Q, or its contraposi-
tive @Q ) @P. These statements are logically equivalent, which is to say that they
have the same truth values in all cases. In other words, the statement
ðP ) QÞ , ð@Q ) @PÞ
ð1:2Þ
is a tautology, in that for any assignment of the truth values to P and Q, this state-
ment has constant truth value of ‘‘true.’’
1.5
Propositional Logic
17

If modus ponens is applied to this contrapositive, we arrive at
@Q5ð@Q ) @PÞ ) @P:
ð1:3Þ
However, because of (1.2), this can also be written as
@Q5ðP ) QÞ ) @P;
ð1:4Þ
which is a rule of inference known as modus tollens and exemplified in section 1.2 on
axiomatic theory. It is not an independent rule of inference, of course, as it follows
from modus ponens. In words, (1.4) states that if P ) Q is true, and @Q is true,
meaning Q is false, then @P is also true, or P false.
In some proofs, the direct statement lends itself more easily to a proof, in
others, the contrapositive works more easily, while in others still, both are easy,
and in others still yet, both seem to fail miserably. The only general rule is, if the
method you are attempting is failing, try the other. Experience with success and
failure improves the odds of identifying the more expedient approach on the first
attempt.
For example, assume that we wish to prove P ) Q, where
P : a ¼ b;
Q : a2 ¼ b2:
The direct proof might proceed as
a ¼ b ) ½a2 ¼ ab and ab ¼ b2 ) a2 ¼ b2:
The contrapositive proof proceeds by first identifying the statement negations
@P : a 0 b;
@Q : a2 0 b2;
and constructing the proof as
@Q ) a2  b2 0 0
) ða þ bÞða  bÞ 0 0
) ½ða þ bÞ 0 0 and ða  bÞ 0 0
) a 0 b:
18
Chapter 1
Mathematical Logic

In the last statement we also can conclude that a 0 b, but this is extra information
not needed for the given demonstration.
Once a choice is made between the direct statement and its contrapositive, there
are two common methods for proving the truth of the resulting implication. To sim-
plify notation, we denote the implication to be proved as A ) C, where A denotes
either P or @Q, and C denoted either Q or @P, respectively.
The Direct Proof
The first approach is what we often think of as the use of ‘‘deductive’’ reasoning,
whereby if we cannot prove A ) C in one step, we may take two or more steps.
For example, proving that for some statement B that A ) B and B ) C, it would
seem transparent that A ) C. One expects that such a partitioning of the demonstra-
tion ought to be valid, independent of how many intermediate implications are devel-
oped, and indeed this is the case. It is based on a result in logic that is called a
syllogism and forms the basis of what is known as a direct proof. Specifically, we
have that
ðA ) BÞ5ðB ) CÞ ) ðA ) CÞ
ð1:5Þ
is a tautology. That is, for any assignment of the truth values to A, B, and C, this
statement has constant truth value of ‘‘true.’’
This direct method is very powerful in that it allows the most complicated implica-
tions to be justified through an arbitrary number of smaller, and more easily proved,
implications. In the proof above that P ) Q, this method was in fact used without
mention as follows:
A : a ¼ b;
B : a2 ¼ ab5ab ¼ b2;
C : a2 ¼ b2:
Proof by Contradiction
The second approach to proving an implication is considered an indirect proof, and is
also known as reductio ad absurdum, as well as proof by contradiction. In its simplest
terms, proof by contradiction proceeds as follows:
To prove P, assume @P. If R5@R is derived for any R, deduce P.
In other words,
If @P ) ðR5@RÞ; then P:
1.5
Propositional Logic
19

If @P ) ðR5@RÞ is true, then since R5@R is always false, it must be the case
that @P is also false, and hence P is true. The logical structure of this is the tauto-
logy
½@P ) ðR5@RÞ ) P:
ð1:6Þ
Remark 1.1
It is often the case that in a given application, what is called a proof by
contradiction appears as
If @P ) R; and R is known to be false; then P:
ð1:7Þ
For example, one might derive that @P ) R, where R is the statement 1 0 1. Implic-
itly, the truth of the statement @R, that 1 ¼ 1, does not need to be explicitly identified,
but is understood. Also note that the truth of a statement like 1 ¼ 1 does not need to
‘‘follow’’ in some sense from the statement @P. That (1.7) is a valid conclusion can
also be formalized by explicitly identifying the truth of @R in the tautology
½ð@P ) RÞ5@R ) P;
which except for notation is equivalent to modus tollens in (1.4). This approach also
justifies the terminology of a reductio ad absurdum, namely from the assumed truth of
@P one deduces an absurd conclusion, R, such as 1 0 1.
The indirect method of proof may appear complex, but with some practice, it is
quite simple. The central point is that for any statement R, it is the case that R5@R
is always false. This is because its negation, @R4R, is always true and
@ðR5@RÞ , @R4R
ð1:8Þ
is a tautology. That is, for any statement R, either R is true or @R is true. This is
known as the law of the excluded middle.
Before formalizing this further, let’s apply this approach to the earlier simple ex-
ample, taking careful steps:
Step 1
State what we seek to prove: a ¼ b ) a2 ¼ b2.
Step 2
Develop the negation of this implication. Looking at the truth table for the
conditional, an implication A ) C is false only when A is true, and C is false. So the
negation of what we seek to prove is
a ¼ b
and
a2 0 b2:
Step 3
What can we conclude from this assumed statement? This amounts to ‘‘play-
ing’’ with some mathematics and seeing what we get:
20
Chapter 1
Mathematical Logic

a2 0 b2 , a2  b2 0 0
, ða þ bÞða  bÞ 0 0
, a þ b 0 0
and
a  b 0 0;
whereas
a ¼ b , a  b ¼ 0:
Step 4
Identify the contradiction: we have concluded that both a  b ¼ 0 and
a  b 0 0.
Step 5
Claim victory: a ¼ b ) a2 ¼ b2 is true.
Admittedly, this may look like an ominous process, but with a little practice the
logical sequence will become second nature. The payo¤ to practicing this method is
that this provides a powerful and frequently used alternative approach to proving
statements in mathematics as will be often seen in later chapters.
Summarizing, we can rewrite (1.6) in the way it is most commonly used in mathe-
matics, and that is when the statement P is in fact an implication A ) C. To do this,
we use the result from step 2 as to the logical negation of an implication. That is,
@ðA ) CÞ , A5@C:
It is also the case that the most common contradiction one arrives at in (1.6) is not a
general statement R, but as in the example above, it is a contradiction about A. We
express this result first in the common form:
If ðA5@CÞ ) @A; then A ) C:
ð1:9Þ
Tautology: ½ðA5@CÞ ) @A ) ðA ) CÞ:
In the more general case,
If ðA5@CÞ ) R5@R; then A ) C:
ð1:10Þ
Tautology: ½ðA5@CÞ ) ðR5@RÞ ) ðA ) CÞ:
Remark 1.2
As in remark 1.1 above, (1.10) can also be applied in the context of
ðA5@CÞ ) R, where R is known to be false. The conclusion of the truth of A ) C
again follows.
Proof by Induction
A proof by induction is an approach frequently used when the statement to be proved
encompasses a (countably) infinite number of statements (more on countably infinite
1.5
Propositional Logic
21

sets in chapter 2 on number systems). A somewhat complicated example is the state-
ment in the introduction: For any two integers M and N, we have that M þ N ¼
N þ M. This is complicated because this statement involves two general quantities,
and each can assume an infinite number of values. In other words, this statement is
an economical way of expressing an infinite number of equalities (1 þ 9 ¼ 9 þ 1,
4 þ 37 ¼ 37 þ ð4Þ, etc.).
A simpler example involving only one such quantity is as follows:
If N is a positive integer; then 1 þ 2 þ    þ N ¼ NðN þ 1Þ
2
:
ð1:11Þ
This has the form of an equality, P ¼ Q, but neither P nor Q is a simple declarative
statement. Instead, both are indexed by the positive integers. That is, we seek to
prove
EN; PðNÞ ¼ QðNÞ;
ð1:12Þ
where we define
PðNÞ ¼ 1 þ 2 þ    þ N;
QðNÞ ¼ NðN þ 1Þ
2
:
Obviously, for any fixed value of N, the proof requires no general theory, and the
result can be demonstrated or contradicted by a hand or computer calculation. A
proof by induction provides an economical way to demonstrate the validity of
(1.12) for all N. The idea can be summarized as follows:
If
Pð1Þ ¼ Qð1Þ;
and
½PðNÞ ¼ QðNÞ ) ½PðN þ 1Þ ¼ QðN þ 1Þ;
ð1:13Þ
then
EN; PðNÞ ¼ QðNÞ:
In other words, proof by induction has two steps:
Step 1 (Initialization Step)
Show the statement to be true for the smallest value of
N needed, say N ¼ 1 (sometimes N ¼ 0).
Step 2 (Induction Step)
Show that if the result is true for a given N, it must also be
true for N þ 1.
The logic is self-evident. From the initialization step, the induction step assures the
truth for N ¼ 2, which when applied again assures the truth of N ¼ 3, and so forth.
22
Chapter 1
Mathematical Logic

Example 1.3
To show (1.11), we see that the result is apparently true for N ¼ 1.
Next, assuming the result is true for N, we get
1 þ 2 þ    þ N þ ðN þ 1Þ ¼ NðN þ 1Þ
2
þ N þ 1
¼ NðN þ 1Þ
2
þ 2ðN þ 1Þ
2
¼ ðN þ 1ÞðN þ 2Þ
2
;
which is the desired result.
*1.6
Mathematical Logic
Mathematical logic is one of the most abstract and symbolic disciplines in mathe-
matics. This is quite deliberate. As exemplified above, the goal of mathematical logic
is to define and develop the properties of deductive systems that are context free. We
cannot be certain that a given logical development is correct if our assessment of it is
encumbered by our intuition in a given application to a field of mathematics. So the
goal of mathematical logic is to strip away any hint of a context, eliminate all that is
familiar in a given theory, and study the logical structure of a general, and unspeci-
fied, mathematical theory.
To do this, mathematical logic must first erase all familiar notations that imply a
given context. Also its symbolic structure needs to be very general so that it allows
application to a wide variety of mathematical disciplines or contexts. As a result
mathematical logic is highly symbolic, highly stylized, leaving the logician with noth-
ing to guide her except the rules allowed by the structure. This way every deduction
can be verified mechanically, e¤ectively as an appropriately structured computer pro-
gram. This program then declares a symbolic statement to be ‘‘true’’ if and only if it
is able to construct a symbol sequence, using only the axioms or assumed facts and
rules of inference that results in the deductive construction of the statement. No con-
text is assumed, and no intuition is needed or desired.
The preceding section’s informal introduction to the mathematical logic of state-
ments, which is referred to as statement calculus or propositional logic, is a small sub-
set of the discipline of mathematical logic. The axiomatic structure of statement
calculus includes:
1.6
Mathematical Logic
23

1. Certain formal symbols made up of logical operators (@ and ), but excluding E
and b), punctuation marks (e.g., parentheses), and other symbols that are undefined,
but in terms of which other needed concepts such as variable, predicate, formula, op-
eration, statement, and theorem are defined.
2. Axioms that identify the basic formula structures that will be assumed true.
3. A rule of inference: modus ponens.
The resulting theory can then be shown to be complete because it is decidable. The
algorithm for determining if a given statement is true or not is the construction of the
associated truth table, any one of which requires only a finite number of steps to de-
velop. The key to this result is that a statement is a theorem in statement calculus,
meaning it can be deduced from the axioms with modus ponens if and only if the
statement is a tautology in the sense of the associated truth table.
For many areas of mathematics, however, statement calculus is insu‰cient in that
it excludes statements of the form
ExPðxÞ
or
bxPðxÞ
that are central to the statements in most areas of mathematics. The mathematical
theory developed to accommodate these notions is called first-order predicate calcu-
lus, or simply first-order logic.
Landmark results in first-order logic are Go¨del’s incompleteness theorems, pub-
lished in 1931 by Kurt Go¨del (1906–1978). Although far beyond the boundaries of
this book, the informal essence of Go¨del’s first theorem is this: In any consistent
first-order theory powerful enough to develop the basic theory of numbers, one can
construct a true statement that is not provable in this system. In other words, in any
such theory one cannot hope to confirm or deny every statement that can be made
within the theory, and hence every such theory is ‘‘incomplete.’’
The informal essence of Go¨del’s second theorem is this: In any consistent first-
order theory powerful enough to develop the basic theory of numbers, it is impossi-
ble to prove consistency from within the theory. In other words, for any such theory
the proof of consistency will of necessity have to be framed outside the theory.
1.7
Applications to Finance
The applications of mathematical logic discussed in this chapter to finance are
both specific and general. First o¤, there are many specific instances in finance
when one has to develop a proof of a given result. Typically the framework for this
24
Chapter 1
Mathematical Logic

proof is not a formally stated theorem as one sees in a research paper. The proof is
more or less an application of, and sometimes the adaptation of, a given theory to a
situation not explicitly anticipated by the theory, or entirely outside the framework
anticipated.
Alternatively, one might be developing and testing the validity of a variety of hy-
pothetical implications that appear reasonable in the given context. In such specific
applications the investigation pursued often requires a very formal process of deriva-
tion, logical deduction, and proof, and the tools described in the sections above can
be helpful in that they provide a rigorous, or at least semi-rigorous, framework for
such investigations.
More specifically, a truth table can often be put to good use to investigate the va-
lidity of a subtle logical derivation involving a series of implications and, based on
the various identities demonstrated, to provide alternative approaches to the desired
result. For example, a proof by contradiction applied to the contrapositive of the
desired implication can be subtle in the language provided by the context of the
problem. Just as in mathematics, isolating the logical argument from the context pro-
vides a better framework for assessing the former without the necessary bias that the
latter might convey. In addition, when the investigation ultimately reduces to the
proof of a given implication, as often arises in an attempt to evaluate the truth of a
reasonable and perhaps even desired implication, the various methods of proof pro-
vide a framework for the attack.
There is also a general application of the topics in this chapter to finance, and
more broadly, any applied mathematical discipline, and that is as a cautionary tale.
All too often the power and rigor of mathematics is interpreted to imply a certain
robustness. That is, one assumes that the true results in mathematics are ‘‘so true’’
that they are robust enough to remain true even when one alters the hypotheses a
bit, or is careless in their application to a given situation. Actually nothing could be
further from the truth.
The most profound thought on this point I recall was made long ago by my thesis
advisor and mentor, Alberto P. Caldero´n (1920–1998), during a working visit made
to his o‰ce. What he said on this point, as perhaps altered by less than perfect recall,
was: ‘‘The most interesting and powerful theorems in mathematics are just barely
true.’’ In other words, the conclusions of the ‘‘best theorems’’ in mathematics are
both solid in their foundation and yet fragile; they represent a delicate relationship
between the assumed hypothesis and the proved conclusion. In the ‘‘best’’ theorems
the hypothesis is in a sense very close to the minimal assumption needed for the con-
clusion, or said another way, the conclusion is very close to the maximal result
1.7
Applications to Finance
25

possible that follows from the given hypothesis. The ‘‘more true’’ a theorem is, in the
sense of excessive hypotheses or suboptimal conclusions, the less interesting and
important it is. Such theorems are often revisited in the literature in search of a
more refined and economical statement.
The implication of this cautionary tale is that it is insu‰cient to simply memorize
a general version of the many results in mathematics without also paying close atten-
tion to the assumptions made to prove these results. A slight alteration of the as-
sumptions, or an attempt to broaden the conclusions, can and will lead to periodic
disasters. But more than just the need to carefully utilize known results, it is impor-
tant to understand the proof of how the given hypotheses provide the given conclu-
sions since, in practice, the researcher is often attempting to alter one or the other,
and evaluate what part of the original conclusion may still be valid.
The snippets of mathematical history alluded to in this chapter, and the paradoxes,
support this perspective of the fragility of the best results, and the care needed to get
them right and in balance. As careful as mathematicians were in the development of
their subjects, pitfalls were periodically identified and ultimately had to be overcome.
And perhaps it is obvious, but a great many of these mathematicians were intellec-
tual giants, and leaders in their mathematical disciplines. The pitfalls were far less a
reflection of their abilities than a testament to the subtlety of their discipline.
As a simple example of this cautionary tale, it is important that in any mathe-
matical pursuit, any quantitative calculation, and any logical deduction, one must
keep in mind that the truth of statement Q as promised by modus ponens, de-
pends on both the truth of the hypothesis P and the truth of the implication P ) Q.
The truth of the latter relies on the careful application of many of the principles dis-
cussed above, and it is often the focus of the investigation. But modus ponens cau-
tions that equally important is to do what is often the more tedious part of the
derivation, and that is to check and recheck the validity of the assumptions, the
validity of P.
A simple example is the principle of arbitrage, which tends to fascinate new fi-
nance students. In an arbitrage, one is able to implement a market trade at no cost,
that is risk free over some period of time, and with positive likelihood of producing
a profit at the end of the period and no chance of loss. Invariably, students will
perform long, detailed, and very creative calculations that identify arbitrages in the
financial markets. In other words, they are very detailed and creative in their deriva-
tions of the truths of the statements P ) Q, where in their particular applications, P
is the statement ‘‘I go long and short various instruments at the market prices I see in
the press or online,’’ and Q is the statement ‘‘I get embarrassingly rich as the profits
come rolling in.’’
26
Chapter 1
Mathematical Logic

Of course, the poorly trained students make mistakes in this proof of P ) Q, using
the wrong collection of instruments, or not identifying the risks that exist post trade.
But the better students produce perfect and sometimes subtle trade analyses. Invari-
ably the finance professor is left the job of bursting bubbles with the question: ‘‘How
sure are you that the securities are tradable at the prices assumed?’’ In other words,
how sure are you that P is true?
The answer to this question comes from a logical analysis of the following argu-
ment using syllogism and modus tollens:
If finance students’ arbitrages worked,
there would be numerous, embarrassingly rich finance students.
If finance students could trade at the assumed prices,
their arbitrages would work.
There are not numerous embarrassingly rich finance students.
Exercises
Practice Exercises
1. Create truth tables to evaluate if the following statements, A , B, are tauto-
logies:
(a) P4Q , @P ) Q
(b) ðP4QÞ4ðP ) QÞ , P5Q
(c) ðP , QÞ , ðP ) QÞ5ðQ ) PÞ
(d) ½P ) ðQ4RÞ5½Q ) ðP4RÞ , R
2. It was noted that the truth of P ) Q does not necessarily imply the truth of Q.
Confirm this with a truth table by showing that ðP ) QÞ ) Q is not a tautology.
Create real world applications by defining statements P and Q illustrating a case
where ðP ) QÞ ) Q is true, and one where it is false.
3. The contrapositive provides an alternative way to demonstrate the truth of the im-
plication P ) Q. Confirm that ðP ) QÞ , ð@Q ) @PÞ is a tautology. Give a real
world example.
4. Confirm that the structure of the proof by contradiction,
½ðA5@CÞ ) @A ) ðA ) CÞ;
is a tautology.
Exercises
27

5. Comedically, the logical deduction
½ðP ) QÞ5Q ) P
ð1:14Þ
is known as modus moronus. Show that this statement is not a tautology, and provide
a real world example of statements P and Q for which the hypothesis is true and con-
clusion false.
6. Show by mathematical induction that for any integer n b 0:
X
n
i¼0
2i ¼ 2nþ1  1:
7. Develop a direct proof of the formula in exercise 6. (Hint: Define S ¼ Pn
i¼0 2i,
consider the formula for 2S, and then subtract.)
8. Develop a proof by contradiction in the form of (1.6) of the formula in exercise 6.
(Hint: The formula is apparently true for n ¼ 0; 1; 2, and other values of n. Let N be
the first integer for which it is false. From the truth for n ¼ N  1, and falsity for
n ¼ N, conclude that 2N 0 2N and recall the remark after (1.6).)
9. It is often assumed that the initialization step in mathematical induction is un-
necessary, and that only the induction step need be confirmed. Show that the for-
mula
X
n
i¼0
2i ¼ 2nþ1 þ c
satisfies the induction step for any c, but that only for c ¼ 1 does it satisfy the ini-
tialization step.
10. Show by mathematical induction that
X
n
j¼1
j2 ¼ nðn þ 1Þð2n þ 1Þ
6
:
11. A bank has made the promise that for some fixed i > 0, an investment with it
will grow over every one-year period as Fjþ1 ¼ Fjð1 þ iÞ, where Fj denotes the fund
at time j in years. Prove by mathematical induction that if an investment of F0 is
made today, then for any n b 1,
Fn ¼ F0ð1 þ iÞn:
28
Chapter 1
Mathematical Logic

12. Develop a proof using modus tollens in the structure of (1.4) that if at some time
n years in the future, the bank communicates Fn 0 F0ð1 þ iÞn, then the bank at some
point must have broken its promise of one-year fund growth noted in exercise 11.
(Hint: Define P : Fjþ1 ¼ Fjð1 þ iÞ for all j; Q : Fn ¼ F0ð1 þ iÞn for all n b 1. What
can you conclude from ðP ) QÞ5@Q?)
Assignment Exercises
13. Create truth tables to evaluate if the following statements, A , B or A ) B, are
tautologies:
(a) P5Q , @ðP ) @QÞ
(b) ðP4QÞ5@Q ) P
(c) ðP ) QÞ5ðP5RÞ ) Q5R
(d) @P4ðQ5RÞ , ð@R4@QÞ5P
14. Modus ponens identifies the necessary additional fact to convert a proof of the
truth of the implication, P ) Q, into a proof of the conclusion, Q. Confirm that
P5ðP ) QÞ ) Q is a tautology. Demonstrate by real world examples as in exercise
2 that while ðP ) QÞ ) Q can be true or false, P5ðP ) QÞ ) Q is always true.
15. Show that modus ponens combined with the contrapositive yields @Q5ðP ) QÞ
) @P, and show directly that this statement is a tautology. Give a real world
example.
16. Identify and label (A, B, etc.) the statements in the argument at the end of this
chapter, convert the argument to a logical structure, and demonstrate what conclu-
sion can be derived using syllogism and modus tollens.
17. Show by mathematical induction that for i > 0 and integer n b 1,
X
n
j¼1
ð1 þ iÞj ¼ 1  ð1 þ iÞn
i
:
18. Develop a direct proof of the formula in exercise 17. (Hint: See exercise 7.)
19. Show by mathematical induction that
X
n
j¼1
j3 ¼
X
n
j¼1
j
"
#2
:
20. A bank has made the promise that for some fixed i > 0, an investment with it
will grow over every one-year period as Fjþ1 ¼ Fjð1 þ iÞ, where Fj denotes the fund
Exercises
29

at time j in years. Develop a proof by contradiction in the form of (1.9) that for any
n b 1,
Fn ¼ F0ð1 þ iÞn:
(Hint: Define A : Fjþ1 ¼ Fjð1 þ iÞ for all j b 0; C : Fn ¼ F0ð1 þ iÞn for all n b 1. If
A5@C and N is the smallest n that fails in C, what can you conclude about FN,
which provides a contradiction, and about the conclusion A ) C?)
30
Chapter 1
Mathematical Logic


## Number Systems and Functions

2 Number Systems and Functions
2.1
Numbers: Properties and Structures
2.1.1
Introduction
In this chapter some of the detailed proofs on number systems are omitted. The rea-
son is that to provide a rigorous framework for the fundamental properties of num-
ber systems summarized below would require the development of both subtle and
detailed mathematical tools for which we will have no explicit use in subsequent
chapters. The mathematics involved, however, gives beautiful examples of the ex-
traordinary power and elegance of mathematics, and provides an intuitive context
for many of the generalizations in later chapters.
This statement of the ‘‘power and elegance’’ of this theory might surprise a reader
who is tempted to think that the power of mathematics is only revealed in the devel-
opment of new and complex theory. However, the development of a rigorous frame-
work to prove statements about properties of numbers that we have been taught as
‘‘true’’ since pre-school can be even more complex. For example, how would one set
out to prove that for any integers n and m,
n þ m ¼ m þ n?
Who but a mathematician would think that such an ‘‘obvious’’ statement would re-
quire proof, and who but a mathematician would commit to the e¤ort of developing
the necessary tools and mathematical framework to allow this and other such state-
ments an objective and critical analysis?
As discussed in chapter 1, such a framework must introduce certain undefined
terms, the formal symbols. It must also explicitly address what will be assumed within
the axioms about these terms and symbols and the system of numbers under study. It
will need to ensure that despite the strong belief system people have about properties
of numbers learned since childhood, all demonstrations of statements within theory
rely explicitly and exclusively on axioms, or on other results that follow from these
axioms. Such provable statements are then called the theorems or propositions of the
theory (terms used interchangeably), and the rigorous demonstrations of these state-
ments’ validity are called the proofs of the theory.
The modern axiomatic approach to natural numbers was introduced by Giuseppe
Peano (1858–1932) in 1889, when he developed what has come to be known as
Peano’s axioms, which simplified a 1888 axiomatic treatment by Richard Dedekind
(1831–1916).

2.1.2
Natural Numbers
Perhaps the simplest collection of numbers is that of natural numbers or counting
numbers, denoted N, and defined as
N ¼ f1; 2; 3; . . .g
or
f0; 1; 2; 3; . . .g:
To give a flavor for the axiomatic structure for N, we introduce Peano’s axioms in
the framework that provides the basic arithmetic structure. The formal symbols are
self-evident except for the symbol 0. Intuitively, for any natural number n, the symbol
n0 denotes its successor, which in concrete terms can be thought of as n þ 1.
1. Formal Symbols:
¼, 0, þ, , 0
2. Axioms:
 A1: EmEnðm0 ¼ n0 ) m ¼ nÞ
 A2: Emðm0 0 0Þ
 A3: Emðm þ 0 ¼ mÞ
 A4: EmEnðm þ n0 ¼ ðm þ nÞ0Þ
 A5: Emðm  0 ¼ 0Þ
 A6: EmEnðm  n0 ¼ m  n þ mÞ
 A7: For any formula PðmÞ: ½Pð0Þ5EmðPðmÞ ) Pðm0ÞÞ ) EmPðmÞ
We note that the formal symbols include the familiar addition (þ), multiplication
(), and equality (¼) symbols, as well as one numerical constant 0. There is also the
prime symbol (0), which, as can be inferred from the axioms, is meant to denote
‘‘successor.’’ In layman’s terms, m0 stands for m þ 1, but in the more abstract axiom-
atic setting, m0 simply denotes the successor of m.
Axiom 1 says that the ‘‘successor’’ is unique; two di¤erent elements of N cannot
have the same successor, while axiom 2 formally puts 0 at the front of the successor
chain. Axioms 3 and 4 form the foundation for how addition works while axioms 5
and 6 do the same for multiplication. Also axiom 6 reveals our layman understand-
ing that m0 ¼ m þ 1. To deduce this formally, we need to define 1 ¼ 00, then prove
that m ¼ 1  m, as well as prove that we can factor m  n þ m ¼ m  ðn þ 1Þ. Finally,
axiom 7 is the ‘‘induction’’ axiom, which provides a framework to prove general for-
mulas about N. Namely, if one proves that a formula is true for 0, and that its truth
for m implies truth for m0, then the formula is true for all m. This idea was intro-
duced in chapter 1 as ‘‘proof by induction.’’ We will not pursue this formal axiomatic
development further.
32
Chapter 2
Number Systems and Functions

Returning to the informal setting, we note that the natural numbers are useful pri-
marily for counting and ordering objects. There are an infinite number of elements of
the set N, of course, and to distinguish this notion of infinity, we say that the set N
is countable or denumerable. More generally, a collection X is said to denumerable if
there is a 1:1 correspondence between X and N, denoted
X $ N;
meaning that there exists an enumeration of the elements of X,
X ¼ fx1; x2; x3; . . .g;
that includes all of the elements of X exactly once. Alternatively, each element of X
can be paired with a unique element of N.
Note, however, that to prove that a set is countable, it is sometimes easier to
explicitly demonstrate a correspondence that contains multiple counts where all ele-
ments of X are counted at least once. Such a demonstration implies the desired re-
sult, of course, and oftentimes there will be no reason to refine the argument to get
an explicit correspondence ‘‘which includes all of the elements of X exactly once.’’
Proposition 2.1
If the collections Xi are countable for i ¼ 1; 2; . . . ; n, then X ¼
fx j x A Xi for some ig is also countable.
Proof
The necessary correspondence X $ N is defined by associating the elements
of each Xi 1 fxi1; xi2; xi3; . . . ; xij; . . .g with fi þ ð j  1Þn j j ¼ 1; 2; . . .g. In other
words, the first elements of the fXig are counted sequentially, then the second ele-
ments, etc.
n
Remark 2.2
In the next chapter we introduce sets and operations on sets such as
unions and intersections, but for those already familiar with these concepts, it is appar-
ent that X above is defined as the union of the Xi. It is the case that the proposition
above holds even if there are a countable number of Xi. A proof of this statement will
be seen below when it is demonstrated that the rational numbers are countable.
As a collection the natural numbers are closed under addition and multiplication,
meaning that these operations produce results that are again natural numbers,
n1; n2 A N ) n1 þ n2 A N
and
n1  n2 A N;
but are not closed under subtraction or division. An important property of N under
multiplication (), and one known to the ancient Greeks, is that of unique factoriza-
tion. We first set the stage.
2.1
Numbers: Properties and Structures
33

Definition 2.3
A number n A N is prime if n > 1 and
n ¼ n1  n2
implies
n1 ¼ 1
and
n2 ¼ n;
or conversely:
A number n > 1 is composite if it is not prime. That is, n ¼ n1  n2 and neither factor nj,
equals 1.
Note that n ¼ 1 is neither prime nor composite by this definition. That is a matter
of personal taste, and one can define it to be prime without much consequence, other
than needing to be a bit more careful in the definition of ‘‘unique factorization,’’
which will be discussed below.
Proposition 2.4
The collection of primes is infinite.
Proof
Following Euclid of Alexandria (ca. 325–265 BC), who presented the proof
in Euclid’s Elements, we use the method of proof by contradiction. If the conclu-
sion were false and n1; n2; n3; . . . ; nN were the only primes, then define n ¼ n1  n2 
n3  . . .  nN þ 1. So either n is prime, which would be a contradiction as it is clearly
bigger than any of the original primes, or it is composite, meaning that it is evenly
divisible by one of the original set of primes. But this too is impossible given the for-
mula for n, since 1 is not evenly divisible by any prime.
n
We now return to the notion of unique factorization. By this we simply mean that
every natural number can be expressed as a product of prime numbers in only one
way.
Definition 2.5
The set N satisfies unique factorization if for every n, there exists a
collection of primes fpjgN
j¼1 so that n ¼ Ppj, and if there exist collections of primes
fpjgN
j¼1 and fqkgM
k¼1 so that
n ¼ Ppj ¼ Pqk;
then N ¼ M, and when these primes are arranged in nondecreasing order, pj ¼ qj for
all j.
Remark 2.6
1. In the definition above, Ppj is shorthand for the product
Ppj ¼ p1p2p3 . . . pN;
and analogously for Pqk. When necessary for clarity, this product will be expressed as
QN
j¼1 pj.
34
Chapter 2
Number Systems and Functions

2. The notion here of a nondecreasing arrangement seems awkward at first. We tend to
think of increasing and decreasing as opposites, so we expect a nondecreasing arrange-
ment to be an increasing one. But this definition must allow for cases where the primes
are not all distinct, and hence the arrangement can not be truly ‘‘increasing.’’ In other
contexts, the notion of ‘‘nonincreasing’’ will have the same intent.
3. If the natural number 1 is defined above to be a prime number, the definition of
unique factorization would have to be a bit more complicated to allow for any number
of factors equaling 1.
Proposition 2.7 (Fundamental Theorem of Arithmetic)
N satisfies unique factori-
zation.
Proof
The complexity of this proof lies in the proof of a much simpler idea: if a
prime divides a composite number, then given any factorization of that number, this
prime must divide at least one of its factors. This is known as Euclid’s lemma (after
Euclid of Alexandria), which we discuss below. Once this lemma is demonstrated, the
proof then proceeds by induction. The proposition is clearly true for n ¼ 2, which is
prime. Assume next that it is true for all n < N, and that N has been factored:
N ¼ Ppj ¼ Pqj, where, for definitiveness, the primes have been arranged in nonde-
creasing order. Of course, we can assume that N is composite, since all primes satisfy
unique factorization by definition. Now by Euclid’s lemma, if p1 divides N ¼ Pqj, it
must divide one of the factors. Because the qj are prime, it must be the case that
p1 ¼ qi for some i. Similarly, because q1 must divide Ppj and the pj are prime, it
must be the case that q1 ¼ pk for some k. Consequently, by the assumed arrange-
ments of primes, we must have q1 ¼ p1, and this common factor can be eliminated
from the expressions by division. We now have two prime factorizations for
N=p1 ¼ N=q1, a number which is less that N. Hence by the induction step, unique
factorization applies, and the result follows.
n
Remark 2.8
1. Euclid’s Lemma
The modern idea behind Euclid’s lemma, in contrast to the origi-
nal proof, is that if p and a are natural numbers that have no common factors, one can
find natural numbers x and y so that
1 ¼Gðpx  ayÞ:
In other words, if p and a have no common factors, one can find multiples of these
numbers that di¤er by 1. This result is a special case of Be´zout’s identity, named for
E´ tienne Be´zout (1730–1783), and discussed below. Assuming this lemma, if p is a
2.1
Numbers: Properties and Structures
35

prime that divides n ¼ ab but does not divide a, we know that p and a have no common
factors, so the identity above holds. Multiplying through by b, we conclude that
b ¼Gðbpx  abyÞ;
and hence p divides b, since it clearly divides bpx, and also divides aby ¼ ny, since p
divides n by assumption.
2. Be´zout’s Identity
Be´zout’s identity states that given any natural numbers a and b,
if d denotes the greatest common divisor, d ¼ gcdða; bÞ, then there are natural numbers
x and y so that
d ¼Gðax  byÞ:
In other words, one can find multiples of these numbers that di¤er by the greatest com-
mon division of these numbers. If a and b have no common factors, then d ¼ 1, and this
becomes Euclid’s lemma utilized above. The proof of this result comes from another
very neat construction of Euclid.
3. Euclid’s Algorithm
Euclid’s algorithm provides an e‰cient process for finding d,
the greatest common divisor of a and b. To understand the basic idea, let’s assume
b > a, and write
b ¼ q1a þ r1;
where q1 is a natural number including 0, and r1 is a natural number satisfying 0 a
r1 < a. Euclid’s critical observation is that any number that divides a and b must also
divide r1, since r1 ¼ b  q1a. Consequently the number gcdða; bÞ must also divide r1,
and hence
gcdða; bÞ ¼ gcdðr1; aÞ:
We now repeat the process with a and r1:
a ¼ q2r1 þ r2;
r1 ¼ q3r2 þ r3;
r2 ¼ q4r3 þ r4; . . . ;
where in each step, 0 a rjþ1 < rj. We continue in this way until a remainder of 0 is
obtained, which must happen because the remainders must decrease. The second to
last remainder must then be d because of the critical observation above. In other words,
we eventually get to the last two steps:
36
Chapter 2
Number Systems and Functions

rn1 ¼ qnþ1rn þ rnþ1;
rn ¼ qnþ2rnþ1 þ 0:
Since gcdða; bÞ ¼ gcdðrnþ1; 0Þ ¼ rnþ1, it must be the case that rnþ1 ¼ d. We then ob-
tain x and y by reversing the steps above. For example, assume that the process stops
with a remainder of 0 on the third step so that r3 ¼ 0 and r2 ¼ d. Then
d ¼ a  q2r1
¼ a  q2ðb  q1aÞ
¼ ð1 þ q2q1Þa  q2b:
Example 2.9
To show that gcdð68013; 6172Þ ¼ 1:
68013 ¼ 11  6172 þ 121;
6172 ¼ 51  121 þ 1;
121 ¼ 121  1 þ 0:
Reversing the steps obtains
1 ¼ 6172  51  121
¼ 6172  51  ð68013  11  6172Þ
¼ 51  68013 þ 562  6172:
2.1.3
Integers
The set of integers, denoted Z, and defined as
Z ¼ f. . . ; 3; 2; 1; 0; 1; 2; 3; . . .g;
is closed under both addition and subtraction, as well as multiplication. In fact,
under the operation of þ, the integers have the structure of a commutative group,
ðZ; þÞ, which we state without proof.
Definition 2.10
A set X is a group under the operation ?, denoted ðX; ?Þ if:
1. X is closed under ?: that is, x; y A X ) x ? y A X.
2. X has a unit: there is an element e A X so that e ? x ¼ x ? e ¼ x.
3. X contains inverses: for any x 0 e, there is x1 A X so that x1 ? x ¼ x ? x1 ¼ e.
4. ? is associative: for any x; y; z A X: ððx ? yÞ ? zÞ ¼ ðx ? ðy ? zÞÞ.
2.1
Numbers: Properties and Structures
37

Definition 2.11
ðX; ?Þ is an abelian or commutative group if X is a group and for all
x; y A X,
x ? y ¼ y ? x:
Of course, in ðZ; þÞ, the unit e ¼ 0, and the inverses x1 ¼ x.
Also the set Z is denumerable, since it is the union of three denumerable sets, the
natural numbers and their negatives, and f0g. It is also the case that unique factori-
zation holds in Z once one accounts for the possibility of products of G1, since we
clearly must allow for examples such as 2  3 ¼ ð2Þ  ð3Þ. In other words, the Fun-
damental Theorem of Arithmetic holds for both positive and negative natural num-
bers, but for prime factorization the conclusion must allow for the possibility that
pj ¼Gqj
for all j:
Finally, one sometimes sees the notation Zþ and Z to denote the positive and
negative integers, respectively, although there is not a reliable convention as to
whether Zþ contains 0, which is similar to the case for N.
2.1.4
Rational Numbers
The group Z is not closed under division, but it can be enlarged to the collection of
rational numbers, denoted Q, and defined as
Q ¼
n
m


 n; m A Z; m 0 0
(
)
:
The collection Q is a group under both addition (þ) and multiplication (). In ðQ; þÞ,
as in ðZ; þÞ, the unit is e ¼ 0 and inverses are x1 ¼ x, whereas in ðQ; Þ, e ¼ 1 and
x1 ¼ 1=x. In fact ðQ; þ; Þ has the structure of a field.
Definition 2.12
A set X under the operations þ and  is a field, denoted ðX; þ; Þ, if:
1. ðX; þÞ is a commutative group.
2. ðX; Þ is a commutative group.
3. ðÞ is distributive over ðþÞ: for any x; y; z A X: x  ðy þ zÞ ¼ x  y þ x  z.
The set Q is denumerable as can be demonstrated by a famous construction of
Georg Cantor (1845–1918). Express all positive rational numbers in a grid such as
1
1
1
2
1
3
1
4
  
2
1
2
2
2
3
2
4
  
38
Chapter 2
Number Systems and Functions

3
1
3
2
3
3
3
4
  
4
1
4
2
4
3
4
4
  
...
...
...
...
...
It is clear that this is a listing of all positive rational numbers, with all rationals
counted infinitely many times. However, even with this redundancy, these numbers
can be enumerated by starting in the upper left-hand cell, and weaving through the
table in diagonals:
1
1 7! 1
2 7! 2
1 7! 3
1 7! 2
2 7! 1
3 7! 1
4 7!    :
All rationals are then countable as the union of countable sets: positive and negative
rationals and f0g.
Remark 2.13
As noted above, this demonstration applies to the more general state-
ment that the union of a countable number of countable collections is countable, since
these collections can be displayed as rows in the table above and the enumeration
defined analogously.
While closed under the arithmetic operations of þ, , ,o, the set of rationals Q is
not closed under exponentiation of positive numbers. In other words,
x > 0
and
y A Q 6) xy A Q;
where ‘‘6)’’ is shorthand here for ‘‘does not necessarily imply.’’ The simplest demon-
stration that there exist numbers that are not rational comes from Greece around 500
BC, some 200 years before Euclid’s time. The original result was that
ffiffi
2
p
was not
rational. The general result is that only perfect squares of natural numbers have ra-
tional square roots, only perfect cubes have rational cube roots, and so forth. We
demonstrate the square root result on natural numbers next.
Proposition 2.14
If n A N and n 0 m2 for any m A N, then
ffiffin
p B Q.
Proof
Again, using proof by contradiction, assume that
ffiffin
p
is rational, with
ffiffin
p ¼
a
b A Q. Then nb2 ¼ a2. Now if a ¼ Ppj and b ¼ Pqk are the respective unique fac-
torizations, we get
nPq2
k ¼ Pp2
j :
2.1
Numbers: Properties and Structures
39

However, since nb2 also has unique factorization, it must be the case that the collec-
tion of primes on the left and right side of this equality are identical, which means
that after cancellation, there is a remaining set of primes so that n ¼ Pr2
j . That is,
n ¼ m2 for m ¼ Prj, contradicting the assumption that n 0 m2 for any m.
n
This proposition can be generalized substantially, with exactly the same proof.
Specifically, if r A N and r > 1, the only time the rth root of a rational number is ra-
tional is in the most obvious case, when both the numerator and denominator are rth
powers of natural numbers.
Proposition 2.15
Let
n0
m 0 A Q, expressed with no common divisors and
n 0
m 0 0 0. If
n 0
m 0 0 n r
m r for some n; m A N, and r A N, r > 1, then
ffiffiffiffi
n 0
m 0
rq
B Q.
Proof
Follow the steps of the special case above.
n
The set Q has four interesting, and perhaps not surprising, properties that provide
insight to the ultimate expansion below to the real numbers. As will be explained in
chapter 4, these properties can be summarized to say that within the collection of real
numbers, the rational numbers are a dense subset, as is the collection of numbers that
are not rational, called the irrational numbers. However, these number sets will later
be seen to di¤er in a dramatic and surprising way.
Proposition 2.16
1. For any q1; q2 A Q with q1 < q2, there is a q A Q with q1 < q < q2.
2. For any q1; q2 A Q with q1 < q2, there is an r B Q with q1 < r < q2.
3. For any r1; r2 B Q with r1 < r2, there is a q A Q with r1 < q < r2.
4. For any r1; r2 B Q with r1 < r2, there is an r B Q with r1 < r < r2.
Proof
The first statement is easy to justify by construction, by letting q ¼
0:5ðq1 þ q2Þ, or more generally, q ¼ pðq1 þ q2Þ for any rational number p, 0 < p <
1. For the second statement we demonstrate with a proof by contradiction. Assume
that all such r are in fact rational numbers. Then it is also the case that for any
p A Q, we have that all r with q1 þ p < r < q2 þ p are also rational, since rationals
are closed under addition. Choosing p ¼ q1, we arrive at a contradiction as fol-
lows: The proposition above shows that if n 0 m2 for any m, then
ffiffin
p B Q, and hence
1ffiffin
p
B Q. However, we clearly have values of
1ffiffin
p satisfying 0 <
1ffiffin
p < q2  q1. The third
statement has the same demonstration as the second. Specifically, if we assume that
all such q are irrational, then we can translate this collection by a rational number p,
to conclude that all numbers q with r1 þ p < q < r2 þ p are not rational (it is an easy
40
Chapter 2
Number Systems and Functions

exercise that the sum of a rational number and an irrational number is again irratio-
nal). But then we can easily move this range to capture an integer, or any rational
number of our choosing. Finally, the fourth statement follows from the observation
that the construction for the third statement can produce two rationals between r1
and r2, to which we can apply the second statement.
n
Consequently the collection of rational numbers can be informally thought of as
being ‘‘infinitely close,’’ with no ‘‘big holes,’’ but at the same time, containing infi-
nitely many ‘‘small holes’’ that are also infinitely close. The same is true for the col-
lection of irrational numbers. One might guess that this demonstrates that there are
an equal number of rational and irrational numbers. In other words, we might guess
that the above proposition implies that both sets are denumerable. We will see
shortly that this guess would be wrong.
2.1.5
Real Numbers
The rational numbers can be expanded to the real numbers, denoted R, which
includes the rationals and irrationals, although the actual construction is subtle.
This construction of R was introduced by Richard Dedekind (1831–1916) in a 1872
paper, using a method that has come to be known as Dedekind cuts. Although we
will discuss ‘‘sets’’ in chapter 4, we note that j is the universal symbol for the ‘‘empty
set,’’ or the set with no elements.
The idea in this construction is to capitalize on the one common property that
rationals and irrationals share, which follows from the proposition above as gener-
alized in exercises 2 and 17. That is, for any r A Q or r B Q there is a sequence of ra-
tional numbers, q1; q2; q3; . . . so that qn gets ‘‘arbitrarily close’’ to r as n increases
without bound, denoted n ! y.
Definition 2.17
A Dedekind cut is a subset a H Q with the following properties:
1. a 0 j, and a 0 Q.
2. If q A a and p A Q with p < q, then p A a.
3. There is no p A a so that a ¼ fq A Q j q a pg.
That is, a cut can neither be the empty set nor the set of all rationals, it must con-
tain all the rationals smaller than any member rational, and it contains no largest ra-
tional. Dedekind’s idea was to demonstrate that the collection of cuts form a field,
denoted R, that contains the field Q. Of course, he also needed to create an identifi-
cation between cuts and real numbers. That identification was
r A R $ ar 1 fq A Q j q < rg:
2.1
Numbers: Properties and Structures
41

Put another way, each real number r is identified with the least upper bound (or
l.u.b.) of the cut ar, defined as the minimum of all upper bounds:
r ¼ l:u:b:fp j p A arg
¼ minfq A Q j q > p for all p A arg:
Intuitively, this minimum is an element of Q if and only if r A Q. For example,
1
2 ¼ l:u:b:fp j p A a1=2g
¼ minfq A Q j q > p for all p A a1=2g;
ffiffi
2
p
¼ l:u:b:fp j p A a ffiffi
2
p g
¼ minfq A Q j q > p for all p A a ffiffi
2
p g:
In 1872 Augustin Louis Cauchy (1789–1857) introduced an alternative construc-
tion of R, using the notion of Cauchy sequences studied in chapter 5, and showed
that the field of real numbers could be identified with a field of Cauchy sequences
of rational numbers. In e¤ect, each real number is identified with the limit of such a
sequence. To make this work, Cantor needed to ‘‘identify as one sequence’’ all se-
quences with the same limit, but then for the purpose of the identification with ele-
ments of R, any sequence from each association class worked equally well.
Like Q, the set R is also a field that is closed under þ, , , o, and while closed
under exponentiation if applied to positive reals, it is not closed under exponentiation
if applied to negative reals. Also unlike Q, the set R is not countable.
Proposition 2.18
There exists no enumeration R ¼ frngy
n¼1.
Proof
The original proof was discovered by Georg Cantor (1845–1918), published
in 1874, and proceeds by contradiction as follows. It has come to be known as Can-
tor’s diagonalization argument. Assume that such an enumeration was possible, and
that the reals between 0 and 1 could be put into a table:
0:a11a12a13a14a15a16   
0:a21a22a23a24a25a26   
0:a31a32a33a34a35a36   
0:a41a42a43a44a45a46   
42
Chapter 2
Number Systems and Functions

0:a51a52a53a54a55a56   
0:a61a62a63a64a65a66   
..
.
Here each digit, aij, is an integer between 0 and 9. Cantor’s idea was that the enumer-
ation above could not be complete. His proof was that one could easily construct
many real numbers that could not be on this list. Simply define a real number a by
a ¼ ~a11~a22~a33~a44~a55 . . . ;
where each digit of the constructed number ~ajj, denotes any number other than the ajj
found on the listing above. For each j, we then have nine choices for ~ajj, and infi-
nitely many combinations of choices, and none of these constructed real numbers
will be on the list. Consequently the listing above cannot be complete and hence R
is not countable.
n
On first introduction to this notion of a nondenumerably infinite, or an uncountably
infinite collection, it is natural to be at least a bit skeptical. Perhaps it would be easier
to use a number base other than decimal, with fewer digits, so that we could be more
explicit about this listing. Naturally, since any number can be written in any base,
the question of countability or uncountability is also independent of this base.
Standard decimal expansions, also called base-10 expansions, represent a real num-
ber x A ½0; 1 as
x ¼ 0:x1x2x3x4x5x6 . . .
¼ x1
10 þ x2
102 þ x3
103 þ x4
104 þ    ;
where each xj A f0; 1; 2; . . . ; 9g. Similarly a base-b expansion of x is defined, for b a
positive integer, b b 2:
xðbÞ ¼ 0:a1a2a3a4a5a6 . . .
1 a1
b þ a2
b2 þ a3
b3 þ a4
b4 þ a5
b5 þ    ;
ð2:1Þ
where each aj A f0; 1; 2; . . . ; b  1g. Each aj is defined iteratively by the so-called
greedy algorithm as the largest multiple of 1
b j that is less than or equal to what is left
after the prior steps. That is, the largest multiple less than or equal to x  P j1
k¼1
ak
b k .
2.1
Numbers: Properties and Structures
43

Other real numbers x A R are accommodated by applying this algorithm using both
positive and negative powers of b in the expression, as is done for base-10.
In particular, with b ¼ 2, the base-2 or binary system is produced, and all aj A
f0; 1g, so one easily imagines a well-defined and countable listing of the real numbers
x A ½0; 1 by an explicit ordering as follows:
0:000000000000 . . .
0:100000000000 . . .
0:010000000000 . . .
0:110000000000 . . .
0:001000000000 . . .
0:011000000000 . . .
0:101000000000 . . .
0:111000000000 . . . ;
and so forth. It seems apparent that such a careful listing represents all possible reals,
and hence the reals are countable.
Unfortunately, the logic here comes up short. Since every number on this list has
all 0s from a fixed binary position forward, every such number is a finite summation
of the form Pn
k¼1
ak
2 k , with ak A f0; 1g, and hence is rational. So we have simply
developed a demonstration that this proper subset of the rationals is countable. It is
a proper subset, since it does not contain 1
3 , for instance, which has no such finite ex-
pansion in base-2. Once infinite binary expansions are added to the listing, we can
again apply the Cantor diagonalization argument as before and find infinitely many
missing real numbers.
An interesting observation is that despite the analysis in the section on rational
numbers that seemed to imply that rational and irrational numbers are e¤ectively
interspersed, the rational numbers are countable, and yet the irrational numbers are
uncountable; otherwise, the real numbers would be countable as well. This observa-
tion will have interesting and significant implications in later chapters.
*2.1.6
Complex Numbers
The real numbers form a field, ðR; þ; Þ, that is closed under the algebraic operations
of þ, , , o, as well as exponentiation, xy, if x > 0, but it is not closed under expo-
44
Chapter 2
Number Systems and Functions

nentiation of negative reals. The simplest case is
ffiffiffiffiffiffi
1
p
, since the square of every real
number is nonnegative. More generally, not all polynomials with real coe‰cients
have solutions in R, again the simplest example being
x2 þ 1 ¼ 0:
Remarkably, one only needs to augment R by the addition of the so-called imagi-
nary unit, denoted ı ¼
ffiffiffiffiffiffi
1
p
, in an appropriate way, and all polynomials are then
solvable.
Definition 2.19
The collection of complex numbers, denoted C, is defined by
C ¼ fz j z ¼ a þ bı; a; b A R; ı ¼
ffiffiffiffiffiffi
1
p
g:
The term a is called the real part of z, denoted ReðzÞ, and the term b is called the imag-
inary part of z, and denoted ImðzÞ. Also the complex conjugate of z, denoted z, is
defined as
z ¼ a  bı;
if z ¼ a þ bı:
The absolute value of z, denoted jzj, is defined as
jzj ¼
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
a2 þ b2
p
¼
ffiffiffiffi
zz
p
;
ð2:2Þ
where the positive square root is taken by convention.
It is common to identify the complex ‘‘number line’’ with the two-dimensional real
space, also known as the Cartesian plane, denoted R2 (see chapter 3):
z $ ða; bÞ:
This way ReðzÞ is plotted along the traditional x-axis, and ImðzÞ is plotted along the
y-axis. The absolute value of z can then be seen to be a natural generalization of the
absolute value of x, jxj, for real x:
jxj ¼
ffiffiffiffiffi
x2
p
¼
x;
x b 0,
x;
x < 0,

ð2:3Þ
again with the positive square root taken by convention.
This absolute value can be interpreted as the distance from x to the origin, 0. Like-
wise jzj is the distance from the point z ¼ ða; bÞ to the origin, ð0; 0Þ, by the Pythago-
rean theorem applied to a right triangle with side lengths jaj and jbj. For example, in
figure 2.1 is displayed the case where a > 0 and b > 0.
2.1
Numbers: Properties and Structures
45

Another interesting connection between C and the Cartesian plane comes by way
of the so-called polar coordinate representation of a point ða; bÞ A R2. The identifica-
tion is ða; bÞ $ ðr; tÞ, where r denotes the distance to the origin, and t is the ‘‘radian’’
measure of the angle a that the ‘‘ray’’ from ð0; 0Þ to ða; bÞ makes with the positive x-
axis, measured counterclockwise. By convention, the measurement of a is limited to
one revolution so that 0 a a < 360, or in the usual radian measure, 0 a t < 2p. The
connection between an angle of a and the associated ‘‘radian measure of t’’ is that
the radian measure of an angle equals the arc length of the sector on a circle of radius
1, with internal angle a. Such a circle is commonly called a unit circle. Numerically,
canceling the degrees units obtains t ¼ 2pa
360 .
The polar coordinate representation is then defined as
ða; bÞ ¼ ðr cos t; r sin tÞ;
ð2:4aÞ
r ¼
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
a2 þ b2
p
;
ð2:4bÞ
t ¼
arctan b
a ;
0 a y < 2p; a 0 0,
p
2 ;
a ¼ 0; b > 0,
3p
2 ;
a ¼ 0; b < 0.
8
>
<
>
:
ð2:4cÞ
In figure 2.2 is shown a graphical depiction of these relationships when a > 0 and
b > 0. For a ¼ b ¼ 0, t can be arbitrarily defined. In other words, ð0; 0Þ $ ð0; tÞ for
all t.
Figure 2.1
Pythagorean theorem: c ¼
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
a2 þ b2
p
46
Chapter 2
Number Systems and Functions

By this idea it is natural to also associate the complex number z ¼ a þ bı ¼
jzjðcos t þ i sin tÞ. However, an even more remarkable result is known as Euler’s for-
mula, after Leonhard Euler (1707–1783). He derived this formula based on methods
of calculus presented in chapter 9. Specifically, for z ¼ a þ bı,
ez ¼ eaðcos b þ i sin bÞ;
ð2:5Þ
which for z ¼ bı implies that jebij ¼ 1 for all b. This is because by (2.2), jebij2 ¼
cos2 b þ sin2 b ¼ 1.
In addition, when applied to z ¼ pi, this formula provides the most remarkable,
and perhaps most famous, identity in all of mathematics. It is called Euler’s identity,
and follows from (2.5), since cos p ¼ 1, and sin p ¼ 0:
epi ¼ 1:
ð2:6Þ
More generally, Euler’s formula has other interesting trigonometric applications (see
exercise 5), and it is a ‘‘lifesaver’’ for those of us who struggled with the memoriza-
tion of the many complicated formulas known as ‘‘identities’’ in trigonometry.
We next show that for either (2.2) or (2.3) the so-called triangle inequality is
satisfied.
Proposition 2.20
Under either (2.2) or (2.3), we have that
jx þ yj a jxj þ jyj:
ð2:7Þ
Figure 2.2
a ¼ r cos t, b ¼ r sin t
2.1
Numbers: Properties and Structures
47

Proof
We will demonstrate (2.7) by using the definition of absolute value in (2.2),
which is equivalent to (2.3) for real numbers x and y. We then have
jx þ yj2 ¼ ðx þ yÞðx þ yÞ
¼ xx þ xy þ yx þ yy
¼ jxj2 þ 2 ReðxyÞ þ jyj2
a jxj2 þ 2jxj jyj þ jyj2
¼ ðjxj þ jyjÞ2:
Note that in the third step it was used that yx ¼ xy, and that z þ z ¼ 2 ReðzÞ, where-
as for the fourth, ReðxyÞ a jxyj ¼
ffiffiffiffiffiffiffiffiffiffi
xyxy
p
¼
ffiffiffiffiffiffiffiffiffiffi
xxyy
p
¼ jxj jyj.
n
As it turns out, ðC; þ; Þ is a field under the usual laws of arithmetic because
ı2 ¼ 1. For example, multiplication proceeds as
ða þ bıÞ  ðc þ dıÞ ¼ ðac  bdÞ þ ðad þ bcÞı:
ð2:8Þ
The one item perhaps not immediately obvious is the multiplicative inverse for z A C,
where z 0 0. It is easy to check that with
z1 ¼ z
jzj2 ¼ a  b
a2 þ b2 ;
ı
we have zz1 ¼ 1.
With these definitions, we can identify the real number field R as a ‘‘subfield’’ of
the field C:
R $ fða; bÞ j b ¼ 0g;
completing the list of inclusions
N H Z H Q H R H C:
Remarkably, as alluded to above, C is the end of the number field ‘‘chain’’ for the
vast majority of mathematics, at least in part due to a result first proved (in his doc-
toral thesis!) by Johann Carl Friedrich Gauss (1777–1855) in 1799 after more than
200 years of study by other great mathematicians. We state this result without proof,
and mention that there are numerous demonstrations of this result using many di¤er-
ent mathematical disciplines.
48
Chapter 2
Number Systems and Functions

Proposition 2.21 (Fundamental Theorem of Algebra)
Let PðzÞ be an nth-degree poly-
nomial with complex coe‰cients
PðzÞ ¼
X
n
j¼0
cjz j:
Then the equation PðzÞ ¼ 0 has exactly n complex roots, fwjg H C, counting multiplic-
ities, and PðzÞ can be factored:
PðzÞ ¼ cn
Y
n
j¼0
ðz  wjÞ:
Remark 2.22
1. The expression, ‘‘counting multiplicities,’’ means that the collection of roots is not
necessarily distinct, and that some may appear more than once. An example is PðzÞ 1
z2  2z þ 1 ¼ ðz  1Þ2, which has two roots, 1 and 1, counting multiplicities.
2. This important theorem is often expressed with the assumption that PðzÞ has a lead-
ing coe‰cient, cn ¼ 1, which then eliminates the coe‰cient in the factorization above.
3. If PðzÞ has real coe‰cients, then the complex roots, namely those with w ¼ a þ bi
and b 0 0, come in conjugate pairs. That is,
PðwÞ ¼ 0
i¤
PðwÞ ¼ 0;
where the abbreviation i¤ is mathematical shorthand for ‘‘if and only if.’’ It denotes the
fact that the two statements are both true, or both false, and in this respect is the com-
mon language version of the logical symbol , of chapter 1. The complete logical state-
ment is that
PðwÞ ¼ 0
if
PðwÞ ¼ 0
and only if
PðwÞ ¼ 0:
This result on conjugate pairs is easily demonstrated by showing that for real coe‰-
cients, PðwÞ ¼ PðwÞ because conjugation satisfies the following properties:
 If w ¼ w1 þ w2, then w ¼ w1 þ w2,
 If w ¼ w1  w2, then w ¼ w1  w2.
2.2
Functions
Definition 2.23
A function is a rule by which elements of two sets of values are asso-
ciated. There is only one restriction on this association and that is that each element of
2.2
Functions
49

the first set of values, called the domain, must be identified with a unique element of a
second set of values, called the range.
For many applications of interest in this book, both the domain and range of a
function are subsets of the real numbers or integers, but these may also be defined
on more general sets as will be seen below. The rule is then typically expressed by a
formula such as
f ðxÞ ¼ x2 þ 3:
Here x is an element of the domain of the function f , while f ðxÞ is an element of
the range of f . Functions are also thought of and ‘‘visualized’’ as mappings between
their domain and range, whereby x is mapped to f ðxÞ, and this imagery is intuitively
helpful at times. In this context one might use the notation
f : X ! Y;
where X denotes the domain of f , and Y the range. It is also common to write f ðxÞ
for both the function, which ought to be denoted only by f , and the value of the
function at x. This bit of carelessness will rarely cause confusion. Finally, Dmnðf Þ
and Rngð f Þ are commonly used as abbreviations for the domain and range of the
function.
In many applications, f will be a multivariate function, also called a function of
several variables, meaning that the domain of f is made up of n-tuples of variables:
ðx1; x2; . . . ; xnÞ, where each of the variables xj, is defined on the reals, or complexes,
and so forth. For example, f ðx; y; zÞ ¼ 1  xy þ yz is a function of three variables,
and illustrates the notational convention that when n is small, the n-tuple is denoted
as ðx; yÞ, or ðx; y; zÞ, avoiding subscripts. To distinguish the special case of 1-variable
functions, such functions are sometimes called univariate.
In general mathematical language, the word ‘‘function’’ typically implies that the
range of f , or Y, is a subset of one of the number systems defined above. When
Y H R, the function f is called a real-valued function, and one similarly defines the
notions of complex-valued function, integer-valued function, and so forth. This termi-
nology applies to both multivariate and univariate functions. Similarly, if X H R,
the function f is referred to as a function of a real variable, and one similarly defines
the notion of a function of a complex variable, and so forth. When necessary, this
terminology might be modified to univariate function of a real variable, or multivari-
ate function of a real variable, for example, but the context of the discussion is usually
adequate to avoid such cumbersome terminology. In the more general case, where X
and Y are collections of n-tuples, perhaps with di¤erent values of n, f is typically re-
ferred to as a transformation from X to Y.
50
Chapter 2
Number Systems and Functions

It is important to note that while the definition of a function requires that f ðxÞ be
unique for any x, it is not required that x be unique for any f ðxÞ. For instance, the
function, f ðxÞ ¼ x2 þ 3, above has f ðxÞ ¼ f ðxÞ for any x > 0. Another way of
expressing this is that a function can be a many-to-one rule, or a one-to-one rule, but
it cannot be a one-to-many rule. A function that is in fact one to one has the special
property that it has an ‘‘inverse’’ that is also a function.
Definition 2.24
If f is a one-to-one function, f : X ! Y, the inverse function,
denoted f 1, is defined by
f 1 : Y ! X;
ð2:9aÞ
f 1ðyÞ ¼ x
i¤
f ðxÞ ¼ y:
ð2:9bÞ
The example, f ðxÞ ¼ x2 þ 3, above has no inverse if defined as a function with do-
main equal to all real numbers where it is many to one, but the function does have an
inverse if the domain is restricted to any subset of the nonnegative or nonpositive real
numbers, since this then makes it one to one.
Naturally, a function can also relate nonnumerical sets of values. For example, the
domain could be the set of all strings of heads (H) and tails (T) that arise from 10
flips of a fair coin. A function f could then be defined as the rule that counts the
number of heads for a given string. So this is a function
f : fstrings of 10 Ts and=or Hsg ! f0; 1; 2; . . . ; 9; 10g;
where f ðstringÞ ¼ number of Hs in the string.
2.3
Applications to Finance
2.3.1
Number Systems
This may seem too obvious, but ultimately finance is all about money, in one or sev-
eral currencies, and money is all about numbers. One hardly needs to say more on
this point. Admittedly, finance would seem to be only about rational numbers, since
who ever earned a profit on an investment of $
ffiffiffiffiffiffiffi
200
p
? On the other hand, when one is
dealing with rates of return or solving financial problems and their equations, the ra-
tional numbers are inadequate, and this is true even if all the inputs to the problem,
or terms in the resulting equations, are in fact rational numbers.
For example, if one had an investment that doubled in n years, the implied annual
return is irrational for any natural number n > 1. For n ¼ 5 and an initial investment
of $1000, say, one solves the equation
2.3
Applications to Finance
51

1000ð1 þ rÞ5 ¼ 2000;
r ¼
ffiffi
2
5p
 1:
Well that’s the theory, but no one in the market would quote a return of
100ð
ffiffi
2
5p
 1Þ%. It would be rounded to a rational return of 14.87%, or if one wanted
to impress, 14.869836%. Most people would be satisfied with the former answer, and
yet if we use a rational approximation, and the dollar investment is large enough, we
begin to see di¤erences between the actual return and the approximated return using
the approximate rational yield.
For example, using the return r ¼ 0:1476, we would have a positive error of $14.30
or so with a $1 million investment. Such discrepancies are commonly observed in the
financial markets. Not a big deal, perhaps, for so-called retail investors with modest
sums to invest, but for institutional investors with millions or billions, this rounding
error creates ambiguities and the need for conventions. It is also important to note
that as one uses rational approximations in the real world, it comes at a cost: round-
ing errors begin to appear in our calculations. In other words, if we solve an equation
and use a rational approximation to the solution, this solution will not exactly repro-
duce the desired result unless amounts are so small that the rounding error is less
than the minimum currency unit. Our theoretical calculations don’t balance with
the real world in other cases. When complex calculations are performed, the error
can be big enough to complicate our debugging of the computer program, since we
need to determine if the discrepancy is a rounding problem or an as yet undiscovered
error.
But are even the real numbers all that is needed? We are all likely to say so because
of an inherent suspicion of the complex numbers that is certainly reinforced by lack
of familiarity and compounded by the unfortunate terminology of ‘‘imaginary’’ num-
bers versus ‘‘real’’ numbers. But consider that some investment strategies can pro-
duce a negative final fund balance, even though this may be disguised if the investor
has posted margin.
For example, if a hedge fund manager with $100 million of capital is leveraged
10:1 by borrowing $1 billion, and investing the $1.1 billion in various strategies,
one of which loses $20 million in an investment of $10 million, what is the fund re-
turn to the capital investors on this strategy? Naturally the broker would require
margin for such a strategy, so the negative final fund balance would be reflected in
the reduction of the margin account and overall fund capital. One can similarly de-
velop investment strategies in the derivatives market directly, by going long and/or
short futures contracts on commodities or other ‘‘underlying’’ investments, or imple-
menting long/short strategies in the options markets. One invests $100, say, and has
52
Chapter 2
Number Systems and Functions

a final balance on delivery or exercise date of $100, again in reality observed by a
reduction in margin balances of $100.
For the period, we could argue that the return was 200%, or a period return of
r ¼ 2:00. On the other hand, if one desires to put this return on an annual rate
basis, di‰culties occur. For example, if this investment occurred over a month, the
annual return satisfies
100ð1 þ rÞ1=12 ¼ 100;
ð1 þ rÞ1=12 ¼ 1;
which has no solutions in R but, as it turns out, 12 distinct solutions in C. Note that
exponentiation provides an illusory escape from C:
ð1 þ rÞ ¼ ð1Þ12;
r ¼ 0:
However, while r ¼ 0 solves the algebraically transformed equation, it does not solve
the original equation. Such a solution is sometimes called a spurious solution.
Alternatively, if this return occurred over a year and we sought to determine the
return for this investment on a monthly nominal rate basis discussed below, we obtain
100 1 þ r
12

12
¼ 100;
1 þ r
12 ¼
ffiffiffiffiffiffi
1
12p
;
r ¼ 12½
ffiffiffiffiffiffi
1
12p
 1;
a decidedly complex return, and as above, it has 12 distinct solutions in C. On the
other hand, by squaring the original equation, we can again produce the spurious
solution of r ¼ 0. But this, of course, will not work if substituted into the equation
above.
So what is the correct answer? Despite possible discomfort, any one of the 12 pos-
sible values of r ¼ 12½
ffiffiffiffiffiffi
1
12p
 1 is the actual complex return on a monthly nominal
basis, since each solves the required equation, and there are correspondingly 12 pos-
sible complex returns that can be articulated on an annual basis.
To be sure, the market can always avoid this problem by simply using the lan-
guage that the return was r ¼ 200% ‘‘over the period.’’
2.3
Applications to Finance
53

2.3.2
Functions
The other major area of application for this chapter is related to functions. Functions
are everywhere! Not just in finance but in every branch of the natural sciences, as
well as in virtually every branch of the social sciences, and indeed in every human
endeavor. This is because virtually every branch of human inquiry contains recipes,
or formulas, that describe relationships between quantities that are either provable in
theory or based on observations and considered approximate models of a true under-
lying theory. It is these formulas that help us understand the theories by revealing
relationships in the theories. We note a truism:
Every formula is a function in disguise.
The di¤erence between a formula and a function is simply based on the objective
of the user. For example, if we seek the area of a circle of radius, r ¼ 2, we recall or
look up the formula, which is
area equals p times radius squared,
and with the approximation pA3:1416, we estimate that AA12:5664. On the other
hand, if we seek to understand the relationship between area and radius, the pre-
ferred perspective is one of a function:
AðrÞ ¼ pr2:
We can now see clearly that if the radius doubles, the area quadruples. We can
also easily determine that a large 17-inch pizza has just about the same area as two
small 12-inch pizzas, an important observation when thinking about feeding the fam-
ily. This is especially useful given that a large pizza is often much less expensive than
two small pizzas, which is an application to finance, of course.
Returning to other areas of finance, we consider several examples. In every case it
is purely a matter of taste and purpose which of the parameters in the given formula
are distinguished as variables of the associated function. The general rule of thumb is
that one wants to frame each function in as few variables as possible, but su‰ciently
many to allow the intended analysis.
Present Value Functions
If a payment of $100 is due in five years, the value today, or present value, can be
represented as a function of the assumed annual interest rate, r:
VðrÞ ¼ 100ð1 þ rÞ5;
54
Chapter 2
Number Systems and Functions

which easily generalizes to a payment of F due in n years as
VðrÞ ¼ Fð1 þ rÞn ¼ Fvn:
ð2:10Þ
The present value function in (2.10) is often written in the shorthand of VðrÞ ¼ Fvn,
where v is universally understood as the discount factor for one period, so here
v ¼ ð1 þ rÞ1.
More generally, if a series of payments of amount F are due at the end of each of
the next n years, the present value can be represented as a function of an assumed
annual rate:
VðrÞ ¼ F
X
n
j¼1
ð1 þ rÞj;
¼ F 1  ð1 þ rÞn
r
:
This last formula is derived in exercises 17 and 18 of chapter 1.
Because this present value factor is so common in finance, representing the present
value of an annuity of n fixed payments, it warrants a special notation:
an;r 1 1  ð1 þ rÞn
r
¼ 1  vn
r
:
ð2:11Þ
Note that an;r is a function of n and r, and could equally well have been denoted
aðn; rÞ.
Accumulated Value Functions
If an investment of F at time 0 is accumulated for n years at an assumed annual in-
terest rate r, the accumulated value at time n is given as
AðrÞ ¼ Fð1 þ rÞn:
ð2:12Þ
The accumulated value at time n of a series of investments of amount F at the end of
each of the next n years can be represented as
AðrÞ ¼ F
X
n1
j¼0
ð1 þ rÞ j;
¼ F ð1 þ rÞn  1
r
;
2.3
Applications to Finance
55

where this last formula is derived with the same trick as was used for (2.11). Again,
as this accumulated factor is so commonly used in finance, it is often accorded the
special notation:
sn;r 1 ð1 þ rÞn  1
r
;
ð2:13Þ
and as a function of n and r it could equally well have been denoted sðn; rÞ.
Although one could formally identify VðrÞ with the multivariate function Vðr; FÞ,
and similarly for AðrÞ, there is little point to this formalization since the dependence
of the valuation on F is fairly trivial. However, there are applications whereby the
functional dependence on n is of interest, and one sees this notation explicitly in the
an;r and sn;r functions.
Nominal Interest Rate Conversion Functions
The financial markets require the use of interest rate bases for which the compound-
ing frequency is other than annual. The conventional system is that of nominal inter-
est rates, whereby rates are quoted on an annualized basis, but calculations are
performed in the following way, generalizing the monthly nominal rate example
above.
In the same way that an annual rate of r means that interest is accrued at 100r%
per year, if r is a semiannual rate, interest is accrued at the rate of 100 r
2
 
% per half
year, while a monthly rate is accrued at 100
r
12
 
% per month, and so forth. In each
case the numerical value quoted pertains to an annual period, as it is virtually never
the case in finance that an interest rate is quoted on the basis of a period shorter or
longer than a year. An interest rate of 6% on a monthly basis, or simply 6% monthly,
does not mean that 6% is paid or earned over one month; rather, it is the market con-
vention for expressing that 0:5% will be paid or earned over one month. Similarly 8%
semiannual means 4% per half year, and so forth. Consequently one can introduce
the notion of a rate r, on an mthly nominal basis, meaning that 100
r
m
 
% is paid or
accrued every 1
mth of a year.
Nominal interest rates simplify the expression and calculation of present and accu-
mulated values where payments are made other than annually. For example, a bond’s
payments are typically made semiannually in the United States. If payments of F are
made semiannually for n years, the present value is expressible in terms of an annual
rate by
VðrÞ ¼ F
X
2n
j¼1
ð1 þ rÞj=2;
56
Chapter 2
Number Systems and Functions

or more simply in terms of a semiannual rate
VðrÞ ¼ F
X
2n
j¼1
1 þ r
2

j
¼ Fa2n;r=2;
making the application of the present value and accumulated value functions in
(2.11) and (2.13) more flexible.
Finally, one can introduce the notion of equivalence of nominal rates, meaning that
accumulating or present-valuing payments using equivalent rates produces the same
answer. If rm is on an mthly nominal basis, and rn is on an nthly nominal basis, in
order for the present value of F payable at time N years to be the same with either
rate requires
F
1 þ rm
m

Nm
¼ F
1 þ rn
n

Nn
;
and we immediately conclude that the notion of equivalence is independent of the
cash flow F and time period N. The resulting identity between rn and rm equals that
produced by contemplating accumulated values rather than present values. Of course,
this identity between rn and rm can be converted to a function such as rmðrnÞ. This
tells us that for any rn on an nthly nominal basis, the equivalent rm on an mthly nom-
inal basis is given as
rmðrnÞ ¼ m
1 þ rn
n

n=m
 1
"
#
:
ð2:14Þ
Bond-Pricing Functions
The application of the formulas and functions above to fixed income instruments
such as bonds and mortgages is relatively straightforward. For example, under the
US convention of semiannual coupons quoted at a semiannual rate r, the coupon
paid is F r
2 per half year, where F denotes the bond’s par value. If the bond has a ma-
turity of n years, the price of the bond at semiannual yield i is given by
PðiÞ ¼ F r
2 a2n;i=2 þ Fv2n
i=2:
ð2:15Þ
Here vi=2 again denotes the the discount factor for one period, v ¼ 1 þ i
2

1, but with
a subscript for notational consistency. Sometimes this yield is expressed as in to em-
phasize that this is the yield on an n-year bond.
2.3
Applications to Finance
57

This formula allows a simple analysis of the relationship between PðiÞ and F, or
price and par. From (2.11) applied to a2n;i=2 we derive that v2n
i=2 ¼ 1  i
2 a2n;i=2. When
substituted into (2.15), this price function becomes
PðiÞ ¼ F 1 þ 1
2 ðr  iÞa2n;i=2


:
ð2:16Þ
From this expression we conclude the following:
 PðiÞ > F, and the bond sells at a premium, i¤ r > i.
 PðiÞ ¼ F, and the bond sells at par, i¤ r ¼ i.
 PðiÞ < F, and the bond sells at a discount, i¤ r < i.
Notice that the bond price function as expressed in either (2.15) or (2.16) can be
thought of as a function of time. Identifying the given formulas as the price today
when the bond has n years to maturity, and denoted P0ðiÞ, the price at time j
2 , imme-
diately after the jth coupon, denoted Pj=2ðiÞ, is given by
Pj=2ðiÞ ¼ F 1 þ 1
2 ðr  iÞa2nj;i=2


;
ð2:17Þ
using the format of (2.16), with a similar adjustment to express this in the format of
(2.15). This formula is correct at time 0, of course, as well as at time n, where it
reduces to F. In other words, immediately after the last coupon, the bond has value
equal to the outstanding par value then payable.
The price of this bond between coupons, for instance, at time t, 0 < t < 1
2 , can be
derived prospectively, as the present value of remaining payments at that time, or
retrospectively, in terms of the value required by the investor to ensure that a return
of i is achieved. In either case one derives PtðiÞ ¼ 1 þ i
2

2tP0ðiÞ, which generalizes to
Pð j=2ÞþtðiÞ ¼
1 þ i
2

2t
Pj=2ðiÞ;
0 a t < 1
2 ;
ð2:18Þ
which demonstrates that for fixed yield rate i, the price of a bond varies ‘‘smoothly’’
between coupon dates and abruptly at the time of a coupon payment. In the lan-
guage of chapter 9, this price function is continuous between coupon payments and
discontinuous at coupon dates.
More generally, we may wish to express P as a function of 2n yield variables,
allowing each cash flow to be discounted by the appropriate semiannual spot rate,
in which case we obtain
58
Chapter 2
Number Systems and Functions

Pði0:5; i1; . . . ; inÞ ¼ F r
2
X
2n
j¼1
1 þ ij=2
2

j
þ F
1 þ in
2

2n
:
ð2:19Þ
The domain of all these bond-pricing functions would logically be understood to
be real numbers with 0 a i < 1 or 0 a ij < 1 for most applications, although the
functions are mathematically well defined for 1 þ i
m > 0, where i is an mthly nominal
yield.
Mortgage- and Loan-Pricing Functions
The same way that bonds often have a semiannual cash flow stream, mortgages and
other consumer loans are often repaid with monthly payments, and consequently
rate quotes are typically made on a monthly nominal basis. If a loan of L is made,
to be repaid with monthly payments of P over n years, the relationship between L
and P depends on the value of the loan rate, r. Specifically, the loan value must equal
the present value of the payments at the required rate. Using the tools above, this
becomes
L ¼ Pa12n;r=12;
producing a monthly repayment of
Pðr; nÞ ¼
Lr
12ð1  v12n
r=12Þ :
ð2:20Þ
Here the monthly repayment is expressed as a function of both r and n. In some
applications, where n is fixed, the notation is simplified to PðrÞ.
Note that the identity between the value of the loan and the remaining payments
can also be used to track the progress of the loan’s outstanding balance over time ei-
ther immediately after a payment is made, as in (2.17), or in between payment dates,
as in (2.18) (see exercise 13).
Preferred Stock-Pricing Functions
A so-called perpetual preferred stock is e¤ectively a bond with maturity n ¼ y. That
is, there is a par value, F, a coupon rate, r, that is typically quoted on a semiannual
basis and referred to as the preferred’s dividend rate, but the financial instrument has
no maturity and hence no repayment of par. At a given semiannual yield of i, the
price of this instrument can be easily inferred from (2.15) by considering what hap-
pens to each of the present value functions as the term of the bond, n, grows without
bound. This subject of ‘‘limits’’ will be addressed more formally in chapters 5 and 6,
but here we present an informal but compelling argument.
2.3
Applications to Finance
59

Since it is natural to assume that the market yield rate i > 0, it is apparent that
1 þ i
2 > 1, and hence v2n
i=2 decreases to 0 as n increases to y. Using (2.11) modified
to a semiannual yield, it is equally apparent that as v2n
i=2 decreases to 0, the annuity
factor a2n;i=2 increases to
1
i=2 , which can be denoted ay;i=2. Combining, and canceling
the 1
2 terms, we have that the pricing function for a perpetual preferred stock, is given
by
PðiÞ ¼ Fr
i :
ð2:21Þ
From (2.21) we see that when the dividend rate and yield rate are both on a semian-
nual basis, the price does not explicitly reflect this basis. Generalizing, the same price
would be obtained if r and i were quoted on any common nominal basis.
It is also clear that a perpetual preferred will be priced at a premium, par or at a
discount in exactly the same conditions as was observed above for a given bond, and
that was if r > i, r ¼ i, or r < i, respectively.
Common Stock-Pricing Functions
The so-called discounted dividend model for evaluating the price of a common stock,
often shortened to DDM, is another function of several variables. The basic idea of
this model is that the price of the stock equals the present value of the projected div-
idends. Since a common stock has no ‘‘par’’ value, the dividends are quoted and
modeled in dollars or the local currency, although it is common to unitize the calcu-
lation to a ‘‘per share’’ basis.
If D denotes the annual dividend just paid (per share), and it is assumed that an-
nual dividends will grow in the future at annual rate of g, and investors demand an
annual return of r, then in its most general notational form, the price of the stock can
be modeled as a function of all these variables:
VðD; g; rÞ ¼ D 1 þ g
r  g ;
r > g:
ð2:22Þ
The derivation of (2.22) is similar to that for the preferred stock above, but with a
small trick. That is, the present value of the dividends can be written
D
X
y
j¼1
ð1 þ rÞjð1 þ gÞ j;
and since ð1 þ rÞjð1 þ gÞ j ¼
1 þ rg
1þg

	j
, this present value becomes a preferred
stock with dividend D, valued with a yield of rg
1þg . Consequently (2.22) follows from
60
Chapter 2
Number Systems and Functions

(2.21), and where the requirement that r > g is simply to ensure that in (2.11),
1 þ rg
1þg

	n
decreases to 0 as n increases to y.
In many applications one thinks of this price function as a function of a single
variable. For example, if we think of D and r as fixed, we can express the stock value
as a function of the assumed growth rate, VðgÞ, and so forth. This illustrates the im-
portant point noted above. The functional representation of a quantity is usually not
uniquely defined; it is typically best defined based on the objectives of the user. As
was the case for the price of a bond, one could also allow either g and/or r to vary
by year, further expanding the multivariate nature of this price function, or modify
this derivation to allow for dividends payable other than annually.
Portfolio Return Functions
If the return on asset A1 is projected to be r1, and that of A2 projected to be r2, we
can define a function f ðwÞ to represent the projected return on a portfolio of both
assets, with 100w% allocated to A1, and 100ð1  wÞ% to A2. We then have
f ðwÞ ¼ wr1 þ ð1  wÞr2
¼ r2 þ wðr1  r2Þ:
While this may be initially modeled with the understanding that 0 a w a 1, it is a
perfectly sensible function outside this domain by understanding a ‘‘negative invest-
ment’’ to represent a short sale.
A short sale is one whereby the investor borrows and sells an asset for the cash
proceeds, with the future obligation to repurchase the asset in the open market to
cover the short, which is to say, return the asset to the original owner. Such short
sales require the posting of collateral in a margin account, typically in addition to
the cash proceeds or the securities purchased with these proceeds.
This model is easily generalized to the case of n assets, whereby our asset choices
are fAjgn
j¼1 with projected returns of frjgn
j¼1 and asset allocations of fwjgn
j¼1 with
0 a wj a 1 and Pn
j¼1 wj ¼ 1. One then sees that the projected portfolio return is a
function of these asset allocation weights:
f ðw1; w2; . . . ; wnÞ ¼
X
n
j¼1
wjrj:
ð2:23Þ
Once again, with short sales allowed, the domain of this function can be expanded
beyond the original restricted domains of 0 a wj a 1 for all j.
As a final comment, it may seem odd that with 2 assets, f was a function of 1
variable, yet with n assets, f is a function of n variables. This provides another
2.3
Applications to Finance
61

example of the flexibility one has in such representations. As currently expressed, it
must be remembered in the analysis that logically Pn
j¼1 wj ¼ 1, and hence these n
variables are constrained, meaning that the domain of this function is not the ‘‘n-
dimensional cube,’’ fðw1; w2; . . . ; wnÞ j 0 a wj a 1 for all jg, but a subset of this cube,
fðw1; w2; . . . ; wnÞ j 0 a wj a 1 for all j and Pn
j¼1 wj ¼ 1g. To eliminate the need to
remember this constraint, it can be built into the definition of the function, as was
done in the 2-asset model. For example, writing wn ¼ 1  Pn1
j¼1 wj, we can rewrite
the projected return function as a function of n  1 variables:
f ðw1; w2; . . . ; wn1Þ ¼ rn þ
X
n1
j¼1
wjðrj  rnÞ:
The domain of this function is now defined to either preclude or allow short sales.
Naturally this functional representation also makes sense when the rj values are
not initially defined as constants but instead represent values that will only be
revealed at the end of the period. This perspective then lends itself to thinking about
these returns as random variables, as will be discussed in chapter 7 on probability
theory. Within that framework, good analysis can be done with this function, and
the asset allocation will be seen to influence properties of the randomness of the port-
folio return.
Forward-Pricing Functions
As a final example, consider a forward contract on an equity, with current price S0. A
forward contract is a contract that obligates the long position to purchase the equity,
and the short position to sell the equity, at forward time T > 0, measured in years
say, and at a price agreed to today, denoted F0. No cash changes hands at time 0,
whereas at time T one share of the stock is exchanged for F0. The natural question
is, What should be the value of F0 and on what variables should it depend?
As it turns out, the long position can replicate this contract in theory, which means
that the long can implement a trade at time 0 that provides the obligation to ‘‘buy’’
the stock at time T, and this can be done without finding another investor that is
willing to take on the short position. Similarly a short position can be replicated, so
an investor can implement this contract without finding another investor that is will-
ing to take on the long position.
The replication of the long position is accomplished by purchasing the equity to-
day for a price of S0, and acquiring the cash to do so by short-selling a T-period
Treasury bill. Imagine for clarity that the equity is placed in the margin account
required for the short position, along with other investor funds, so the investor
62
Chapter 2
Number Systems and Functions

doesn’t actually have possession of it at the time of this trade. At time T, the short
sale will be covered at a cost of S0ð1 þ rTÞT, the value of the T-bill to the original
owner at that time, where rT denotes the annual return on the T-period T-bill, and
T is in units of years. Because the short position has been covered, the margin ac-
count is released and the investor takes possession of the stock, implicitly for the
price of covering the short.
Similarly a short forward can be replicated with a short position in the stock and
an investment in T-bills, and the same cost of S0ð1 þ rTÞT is derived. In both cases
the position is replicated with no out-of-pocket cost at time 0 for the investor.
So in either case we conclude that the forward price, F0, that makes sense today
with no money now changing hands, if it is to be agreed to by independent parties
each of whom could in theory replicate their positions, is a function of 3 variables:
F0ðS0; rT; TÞ ¼ S0ð1 þ rTÞT:
ð2:24Þ
In some applications one might think of one or two of these variables as fixed, and
the forward price function expressed with fewer variables. The reason this is the
‘‘correct price’’ is that if forwards were o¤ered at a di¤erent price, it would be possi-
ble for investors to make riskless profits by committing to forwards and then replicat-
ing the opposite position (see exercise 15).
Once the forward contract is negotiated and committed to, there arises the ques-
tion of the value of the contract to the long and to the short at time t where
0 < t a T. For definitiveness, let F0 denote the price agreed to at time t ¼ 0. At
time t, we know from the formula above that the forward price will be
FtðSt; rTt; T  tÞ ¼ Stð1 þ rTtÞTt:
ð2:25Þ
So the long position is committed to buy at time T at price F0, but today’s market
indicates that the right price is Ft. That’s good news for the long if F0 a Ft, and bad
news otherwise. The sentiments of the short position are opposite. So the value at
time t is ‘‘plus or minus’’ the present value of the di¤erence between the two prices
F0 and Ft, that is, G½Ft  F0ð1 þ rTtÞðTtÞ, which for the long position can be
expressed as
VtðSt; rTt; T  tÞ ¼ St  F0ð1 þ rTtÞðTtÞ:
ð2:26Þ
The function representing the value of this contract to the short position is simply the
negative of the function in (2.26).
2.3
Applications to Finance
63

Exercises
Practice Exercises
1. Apply Euclid’s algorithm to the following pairs of integers to find the greatest
common divisor (g.c.d.), and express the g.c.d. in terms of Bezout’s identity:
(a) 115 and 35
(b) 4531 and 828
(c) 1915 and 472
(d) 46053 and 3042
2. In a remark after the proof of the existence of nonrational numbers, or irrational
numbers, it was demonstrated that between any two rational numbers is a rational
number and an irrational number. Prove by construction, or by contradiction, that
in both cases there are infinitely many rationals and irrationals between the two
given rationals. (Hint: For intermediate irrationals, note that for n 0 m2, we know
that
ffiffin
p B Q, and hence
1ffiffin
p B Q. Note also that
1ffiffin
p ! 0 as n ! y:Þ
3. Prove that the irrationals are uncountable. (Hint: Consider a proof by con-
tradiction based on the countability of the rationals and uncountability of the
reals.)
4. Express the following real numbers in the indicated base using the greedy algo-
rithm either exactly or to four digits to the right of the ‘‘decimal point’’:
(a) 100:4 in base-6
(b) 0:1212121212 . . . in base-2
(c) 125;160:256256256 . . . in base-12
(d) 127:33333333 . . . in base-7
5. Demonstrate that if a number’s decimal expansion either terminates, or ends with
an infinite repeating cluster of digits such as 12:12536363636 1 12:12536, then this
number is rational. (Hint: If the number in this example is called x, compare 1000x
and 100;000x. Generalize.)
6. Euler’s formula gives a practical and easy way to derive many of the trigonomet-
ric identities involving the sine and cosine trigonometric functions. Verify the follow-
ing (Hint: e2ai ¼ ðeaiÞ2):
(a) cos 2a ¼ cos2 a  sin2 a
(b) sin 2a ¼ 2 sin a cos a
64
Chapter 2
Number Systems and Functions

7. If an annual payment annuity of 100 is to be received from time 8 to time 20,
show that the value of this 7-year deferred, 13-year annuity can be represented in ei-
ther of the following ways:
(a) 100ða20;r  a7;rÞ
(b) 100ð1 þ rÞ7a13;r
8. What is the domain and range of the following functions? Note that the domain
may include real numbers that would not make sense in a finance application.
(a) Annuity present value: VðrÞ ¼ F Pn
j¼1ð1 þ rÞj (If this is written in the equiva-
lent form VðrÞ ¼ F 1ð1þrÞn
r
, the domain initially looks di¤erent. Convince yourself
by numerical calculation, or analysis, that r ¼ 0 is not really a problem for this func-
tion even in the second form, since the r in the denominator ‘‘cancels’’ an r in the
numerator, much like 3r=r:Þ
(b) Bond price: PðiÞ ¼ F r
2 a2n;i=2 þ Fv2n
i=2
(c) Loan repayment: Pðr; nÞ ¼ Lðr=12Þ
1v12n
r=12
9. Use the nominal equivalent yield formula and demonstrate numerically for an-
nual ‘‘rates’’ r1 ¼ 0:01; 0:10; 0:25; 1:00, that as m ! y, the equivalent yield rmðr1Þ
gets closer and closer to lnð1 þ r1Þ. Consider m up to 1000, say. Show algebraically
that if this limiting result is true for all r1, and n and rn are fixed, then as m ! y, the
equivalent yield, rmðrnÞ, again gets closer and closer to lnð1 þ r1Þ where r1 is the an-
nual rate equivalent to rn. (Note: These results can be proved with the tools of chap-
ter 5, once the notion of the limit of a sequence is formally introduced, and chapter 9,
which provides Taylor series approximations to the function ln x.)
10. Complete the rows of the following table with equivalent nominal rates:
r1
r2
r4
r12
r365
0.05
0.10
0.0825
0.0450
0.0775
11. You are given a 5-year and a 30-year bond, each with a par of 1000 and a semi-
annual coupon rate of 8%. Calculate the price of each at an 8% semiannual yield,
and graph each price function over the range of semiannual yields 0% a i a 16% on
the same set of axes. What pattern do you notice between the graphs?
Exercises
65

12. For the 5-year bond in exercise 11, start with prices calculated at 6% and 10%:
(a) Develop graphs of these bond prices over time using (2.18)
(b) Show that in the case of the 6% valuation, that the successive ratios of the bond’s
write downs, defined as the quantities Pj=2ð0:06Þ  Pð jþ1Þ=2ð0:06Þ, have a constant
ratio of 1:03.
(c) Show similarly that for the 10% valuation, the successive ratios of the bond’s
write ups, defined as the quantities Pð jþ1Þ=2ð0:10Þ  Pj=2ð0:10Þ, have a constant ratio
of 1:05.
(d) Derive algebraically using (2.16), the general formula for a write up or write
down and show that the common ratio is 1 þ i
2 , where i denotes the investor’s yield.
13. You are considering a 10-year loan for $100,000 at a monthly nominal rate of
7.5%.
(a) Calculate the monthly payment for this loan.
(b) Calculate the outstanding balance of this loan over the first year immediately fol-
lowing each of the required 12 payments as well as the changes in these balances,
called loan amortizations. (Hint: recall that the loan balance equals the present value
of remaining payments)
(c) Confirm that the ratio of successive amortizations are in constant ratio of
1 þ 0:075
12 .
(d) Derive algebraically the general formula for the loan amortizations and confirm
that the ratio of successive values is a constant 1 þ i
12 .
(e) Demonstrate that given the formula derived for the values of the amortizations,
they indeed add up to the original loan value, L.
14. What is the DDM price for a common stock with quarterly dividends, where the
last dividend of 2:50 was paid yesterday:
(a) If dividends are assumed to grow at a quarterly nominal rate of 9% and the in-
vestor requires a return of 15% quarterly?
(b) If dividends are assumed to grow at a quarterly nominal rate of 9% only for 5
years, and then to a grow at a rate of 4%, again on a quarterly basis? (Hint: Show
that the dividends can be modeled as a 5-year annuity at one rate, followed by a 5-
year deferred perpetuity [i.e., an infinite annuity] at another rate, where by ‘‘deferred’’
means the first payment is one-quarter year after t ¼ 5. See also exercise 7.).
15. A common stock trades today at S0 ¼ 15, and the risk free rate is 6% on a semi-
annual basis.
66
Chapter 2
Number Systems and Functions

(a) What is the forward price of this stock for delivery in one year?
(b) Replicate a long position in this forward contract with a portfolio of stock and
T-bills, giving details on the initial position as well as trade resolution in 1 year.
(c) If the market traded long and short 1-year forwards on this stock with a price of
15:10, develop an arbitrage to take advantage of this mispricing, giving details on the
initial position as well as trade resolution in 1 year. (Hint: Go long the forward if this
price is low, and short if this price is high. O¤set the risk with replication.)
(d) If an investor goes short the forward in part (a), what is the investor’s gain or loss
at 3 months’ time when the contract is ‘‘o¤set’’ in the market (i.e., liquidated for the
then market value) if the stock price has fallen to 13:50, and the 9-month risk-free
rate is 7:50% (semiannual)?
Assignment Exercises
16. Apply Euclid’s algorithm to the following pairs of integers to find the greatest
common divisor (g.c.d.), and express the g.c.d. in terms of Bezout’s identity:
(a) 697 and 221
(b) 7500 and 2412
(c) 21423 and 3441
(d) 79107 and 32567
17. (See exercise 2.) In a remark after the proof of the existence of nonrational num-
bers, or irrational numbers, it was demonstrated that between any two irrational
numbers is a rational and an irrational. Prove by construction, or by contradiction,
that in both cases there are infinitely many rationals and irrationals between the two
irrational numbers.
18. Express the following real numbers in the indicated base using the greedy algo-
rithm either exactly or to four digits to the right of the ‘‘decimal’’ point:
(a) 25:5 in base-2
(b) 150:151515 . . . in base-5
(c) 237;996:1256 in base-12
(d) 2;399:27 in base-9
19. (See exercise 5.) Explain why it is the case that if a number is rational, its decimal
expansion either terminates or, after a certain number of digits, ends with an infinite
repeating cluster of digits such as 12:12536. Specifically, explain that if this rational
number is given by n
m where n and m have no common divisors, then the decimal
Exercises
67

expansion will terminate by the mth decimal digit, or there will be repeating cluster
that will begin on or before the mth decimal digit, and in this case, the repeating clus-
ter can contain at most m  1 digits. (Hint: Think about the remainders you get at
each division step.)
20. Euler’s formula gives a practical and easy way to derive many of the trigonomet-
ric identities involving the sine and cosine trigonometric functions. Verify the follow-
ing (Hint: eðaþbÞi ¼ eaiebi):
(a) cosða þ bÞ ¼ cos a cos b  sin a sin b
(b) sinða þ bÞ ¼ cos a sin b þ cos b sin a
21. (See exercise 7.) If an annual payment annuity of 100 is to be received from time
n þ 1 to time n þ m, show that the value of this n-year deferred, m-year annuity can
be represented as either of the following:
(a) 100ðanþm;r  an;rÞ
(b) 100ð1 þ rÞnam;r
22. What is the domain and range of the following functions? Note that the domain
may include real numbers that would not make sense in a finance application:
(a) Nominal equivalent rate: rmðrnÞ ¼ m

1 þ rn
n

n=m1

(b) Common stock price: VðD; g; rÞ ¼ D 1þg
rg
(c) Forward price: FtðSt; rTt; T  tÞ ¼ Stð1 þ rTtÞTt
23. Complete the rows of the following table with equivalent nominal rates:
r1
r2
r4
r12
r365
0.16
0.045
0.0955
0.0150
0.025
24. A $25 million, 10-year commercial mortgage is issued with a rate of 8% on a
monthly nominal basis.
(a) What is the monthly repayment, P, over the term of the mortgage?
(b) If Bj denotes the outstanding balance on this loan immediately after the jth pay-
ment, with B0 ¼ 25 million, show that
68
Chapter 2
Number Systems and Functions

Bj ¼ Pað120jÞ;0:08=12
¼ ½B0  Paj;0:08=12 1 þ 0:08
12

j
:
(c) If Pj denotes the principal portion of the jth payment, show that
Pj ¼ P  0:08
12 Bj1:
(d) Show that Pjþ1 ¼ 1 þ 0:08
12


Pj for j b 1.
(e) From part (d), confirm that P Pj ¼ 25 million.
25. A common stock trades today at S0 ¼ 50, and the risk-free rate is 5% on a semi-
annual basis.
(a) What is the forward price of this stock for delivery in 6 months?
(b) Replicate a long position in this forward contract with a portfolio of stock and
T-bills, giving details on the initial position as well as the trade resolution in 6 months.
(c) If the market traded long and short 6-month forwards on this stock with a price
of 53, develop an arbitrage to take advantage of this mispricing, giving details on the
initial position as well as the trade resolution in 6 months.
(d) If an investor goes long the forward in part (a), how much does the investor
make or lose at 3 months’ time when the contract is o¤set in the market if the stock
price has risen to 52, and the 3-month risk-free rate is at 4:50% (semiannual)?
Exercises
69



## Euclidean and Other Spaces

3 Euclidean and Other Spaces
3.1
Euclidean Space
3.1.1
Structure and Arithmetic
The notion of a Euclidean space of dimension n is a generalization of the two-
dimensional plane and three-dimensional space studied by Euclid in the Elements.
Definition 3.1
Denoted Rn or sometimes E n, n-dimensional Euclidean space, or Eucli-
dean n-space, is defined as the collection of n-tuples of real numbers, referred to as
points:
Rn 1 fðx1; x2; . . . ; xnÞ j xj A R for all jg:
ð3:1Þ
Arithmetic operations of pointwise addition and scalar multiplication in Rn are defined
by
1. x þ y ¼ ðx1 þ y1; x2 þ y2; . . . ; xn þ ynÞ.
2. ax ¼ ðax1; ax2; . . . ; axnÞ, where a A R.
In other words, addition and multiplication by so-called scalars a A R, are defined
componentwise. Because points in Rn have n components and are thought of as gen-
eralizing the corresponding notion in familiar two- and three-dimensional space, they
are typically referred to as points and sometimes vectors, and are either notated in
boldface, x, as will be used in this book, or with an overstrike arrow, ~x. The compo-
nents of these points, the fxjg, are called coordinates, and a given xj is referred to as
the jth coordinate.
The terminology of n-tuple may seem a bit strange at first. It is but a generaliza-
tion of the typical language for such groupings whereby, following ‘‘twin’’ and ‘‘trip-
let,’’ one says quadruple, quintuple, sextuple, and so forth. For specific values of n,
the language would be 2-tuple, 3-tuple, and on and on.
Note that the notation for Euclidean space, Rn, is more than just a fanciful play
on the notation for the real numbers, R. This notation rather stems from that for a
product space defined in terms of a direct or Cartesian product:
Definition 3.2
If X and Y are two collections, the direct or Cartesian product of X
and Y, denoted: X  Y is defined as
X  Y ¼ fðx; yÞ j x A X; y A Yg:
ð3:2Þ
That is, X  Y is the collection of ordered pairs, which is to say that X  Y 0 Y  X
in general, and the order of the terms in the product matter. One similarly defines
X  Y  Z, etc., and refers to all such constructions as product spaces.

When X ¼ Y, it is customary to denote X  X by X 2, X  X  X by X 3, etc.
Consequently the notation for Euclidean space, which is the original example of a
product space, is consistent with this notational convention:
Rn 1 R  R      R;
with n factors:
One similarly defines Cn, n-dimensional complex space; Zn, n-dimensional integer
space or the n-dimensional integer lattice; and so forth.
In general, Euclidean space does not have the structure of a field as was the case
for Q, R, and C in chapter 2. This reason is not related to the ‘‘addition’’ in Rn but
to the problem of defining a multiplication of vectors with the required properties.
However, Euclidean space has the structure of a vector space, and it is easily demon-
strated that Rn is a vector space over the real field R. In this book we will almost
exclusively be interested in real vector spaces that are defined by F ¼ R:
Definition 3.3
A collection of points or vectors, X, is a vector space over a field F , if:
1. X is closed under pointwise addition and scalar multiplication:
If x; y A X and a A F , then x þ y A X and ax A F .
2. There is a zero vector: 0 ¼ ð0; 0; . . . ; 0Þ A X such that
x þ 0 ¼ 0 þ x ¼ x
for all x A X:
3. Point addition is commutative and associative: Given x; y; z A X,
x þ y ¼ y þ x;
x þ ðy þ zÞ ¼ ðx þ yÞ þ z:
4. Scalar multiplication satisfies the distributive law over addition: For x; y A X and
a A F ,
aðx þ yÞ ¼ ðx þ yÞa ¼ ax þ ay:
As was noted in chapter 2, one can define a multiplication and a field structure on
R2 by the identification with the complex numbers:
R2 $ C : ða; bÞ $ a þ bı.
Then multiplication is defined using (2.8):
ða; bÞ  ðc; dÞ ¼ ðac  bd; ad þ bcÞ;
72
Chapter 3
Euclidean and Other Spaces

and multiplicative inverses follow from the formula for z1:
ða; bÞ1 ¼
a
a2 þ b2 ;
b
a2 þ b2


:
It is natural to wonder if such an identification can be made for Rn, with n > 2, and
other fields produced. The answer is that yes, identifications do exist for some n > 2,
but these do not produce the structure of fields.
For example, the first of these identifications was discovered by Sir William Rowan
Hamilton (1805–1865) in 1843, and called the quaternions. The quaternions can be
identified with R4, and have the appearance of ‘‘generalized’’ complex numbers.
That is, having a ‘‘real’’ component and three ‘‘imaginary’’ components i, j, k, and
the identification is
ða; b; c; dÞ $ a þ bi þ cj þ dk;
i2 ¼ j2 ¼ k2 ¼ ijk ¼ 1:
The resulting structure falls short of a field structure because multiplication is not
commutative. This follows from ijk ¼ 1, which implies that ij ¼ ji. The resulting
structure is called an associative normed division algebra.
The quaternions can in turn be generalized and an identification made with R8,
known as the octonions, which were independently discovered by John T. Graves
(1806–1870) in 1843 and Arthur Cayley (1821–1895) in 1845. Although octonions
form a normed division algebra, in contrast to the quaternions, multiplication in the
octonions is neither commutative nor associative. Further generalizations to R2 n are
possible for all n, each successive term in the sequence derived from the former term
through what is known as the Cayley–Dickson construction, also after Leonard
Eugene Dickson (1874–1954).
3.1.2
Standard Norm and Inner Product for Rn
Besides an arithmetic on Rn, there is the need for a notion of length, or magnitude,
of a point. In mathematics this notion is called a ‘‘norm.’’
Definition 3.4
The standard norm on Rn, denoted jxj or kxk, is defined by
jxj 1
ffiffiffiffiffiffiffiffiffiffiffiffi
X
n
j¼1
x2
i
v
u
u
t
;
ð3:3Þ
where the positive square root is implied.
3.1
Euclidean Space
73

This norm generalizes the Pythagorean theorem and the notion of the length of a
vector in the plane or in 3-space, which in turn generalizes the notion of length on the
real line or 1-space achieved by the absolute value of x: jxj, defined in (2.3).
Another useful notion on Rn that generalizes to other vector spaces is that of an
inner product, whose formula generalizes the notion of a dot product of vectors in
the plane and 3-space:
Definition 3.5
The standard inner product on Rn, denoted x  y or ðx; yÞ, is defined for
x; y A Rn as
x  y ¼
X
n
j¼1
xiyi:
ð3:4Þ
Inner products are intimately connected with norms. As may be apparent from the
definitions above, the standard norm for Rn satisfies
jxj ¼ ðx  xÞ1=2;
or
jxj2 ¼ jx  xj:
ð3:5Þ
Remark 3.6
The notion of an inner product is one that will reappear in later chapters
and studies in a variety of contexts. As it turns out, there are many possible inner prod-
ucts on Rn that satisfy the same critical properties as the standard inner product above.
Here we identify these defining properties and leave their verification for the standard
inner product as an exercise. Note that item 4 below follows from properties 2 and 3,
but is listed for completeness.
Definition 3.7
An inner product on a real vector space X, is a real-valued function
defined on X  X with the following properties:
1. ðx; xÞ b 0 and ðx; xÞ ¼ 0 if and only if x ¼ 0.
2. ðx; yÞ ¼ ðy; xÞ.
3. ðax1 þ bx2; yÞ ¼ aðx1; yÞ þ bðx2; yÞ for a; b A R.
4. ðx; ay1 þ by2Þ ¼ aðx; y1Þ þ bðx; y2Þ for a; b A R.
Definition 3.8
If ðx; yÞ is an inner product on a real vector space X, the norm associ-
ated with this inner product is defined by (3.5).
*3.1.3
Standard Norm and Inner Product for Cn
We note for completeness that in order to appropriately generalize (2.2) to an n-
dimensional complex vector space, the inner product and norm definitions are modi-
74
Chapter 3
Euclidean and Other Spaces

fied when the space involved, such as Cn, and its underlying field, have complex
values. We provide the definition here:
Definition 3.9
The standard inner product on Cn, denoted x  y or ðx; yÞ is defined for
x; y A Cn,
x  y ¼
X
n
j¼1
xi yi;
ð3:6Þ
where yi denotes the complex conjugate of yi. The standard norm for Cn is defined as
jxj ¼ ðx  xÞ1=2
or
jxj2 ¼ jx  xj:
ð3:7Þ
Remark 3.10
In the context of a complex space, there are again many possible inner
products satisfying the critical properties of the standard inner product above. These
properties are identical to those listed for Rn, with the necessary adjustments for the
complex conjugate on the second term. As before, 5 follows from 3 and 4, and also
here 1 follows from 3, but these properties are listed for completeness.
Definition 3.11
An inner product on a complex vector space X, is a complex-valued
function defined on X  X with the following properties:
1. ðx; xÞ A R for all x.
2. ðx; xÞ b 0 and ðx; xÞ ¼ 0 if and only if x ¼ 0.
3. ðx; yÞ ¼ ðy; xÞ.
4. ðax1 þ bx2; yÞ ¼ aðx1; yÞ þ bðx2; yÞ for a; b A C.
5. ðx; ay1 þ by2Þ ¼ aðx; y1Þ þ bðx; y2Þ for a; b A C.
3.1.4
Norm and Inner Product Inequalities for Rn
An important property of inner products is the Cauchy–Schwarz inequality, which
was originally proved in 1821 in the current finite-dimensional context by Augustin
Louis Cauchy (1759–1857), and generalized 25 years later to all ‘‘inner product
spaces’’ by Hermann Schwarz (1843–1921).
Throughout this section, results on inner products are derived in the context of
the ‘‘standard’’ inner products in (3.4) or (3.6) for specificity. However, it should be
noted that the proofs of these results rely only on the properties identified above for
general inner products, and consequently these results will remain true for all inner
products once defined.
3.1
Euclidean Space
75

Proposition 3.12 (Cauchy–Schwarz Inequality)
With x  y defined as in (3.4) or (3.6),
jx  yj a jxj jyj:
ð3:8Þ
In other words, the absolute value of an inner product is bounded above by the product
of the vector norms.
Proof
Consider x  ay. By definition of a norm, we have for any real number a:
jx  ayj b 0:
However, a calculation produces
jx  ayj2 ¼ ðx  ay; x  ayÞ
¼ x  x  2ax  y þ a2y  y
¼ jxj2 þ a2jyj2  2ax  y:
Choosing a ¼ xy
jyj2 , and combining, we get
jxj2  ðx  yÞ2
jyj2
b 0;
and the result follows.
n
Remark 3.13
We can remove the absolute values from x  y, and the result remains
true since, by definition, x  y ¼Gjx  yj a jx  yj. We use this below.
The general notion of a norm is a fundamental tool in mathematics and is formal-
ized as follows:
Definition 3.14
A norm on a real vector space X, is a real-valued function on X with
values, denoted jxj or kxk, satisfying:
1. jxj A R.
2. j0j ¼ 0, and jxj > 0 for x 0 0.
3. jaxj ¼ jaj jxj for a A R.
4. (Triangle inequality) jx þ yj a jxj þ jyj.
Definition 3.15
A normed vector space is any real vector space, X, on which there is
defined a norm, jxj. For specificity, a normed space is sometimes denoted ðX; jxjÞ or
ðX; kxkÞ.
76
Chapter 3
Euclidean and Other Spaces

Remark 3.16
Item 4 is known as the triangle inequality because it generalizes the
result in (2.7) that the length of any side of a triangle cannot exceed the sum of the
lengths of the other two sides. Also note that item 4 is easily generalized by an iterative
application to
X
n
j¼1
xi


 a
X
n
j¼1
jxij:
ð3:9Þ
Remark 3.17
A norm can be equally well defined on a vector space over a general
field F , such as the complex field C, where jaj denotes the norm of a A F . But we will
have no need for this generalization.
The general definition of a norm was intended to capture the essential properties
known to be true of the standard norm jxj defined on Rn. Not surprisingly, we there-
fore have:
Proposition 3.18
jxj defined in (3.3) is a norm on Rn.
Proof
Only the triangle inequality needs to be addressed as the others follow imme-
diately from definition. From (3.5) we have that
jx þ yj2 ¼ ðx þ y; x þ yÞ
¼ x  x þ 2x  y þ y  y
a jxj2 þ 2jxj jyj þ jyj2
¼ ðjxj þ jyjÞ2;
and the result follows. Note that in the third step, the Cauchy–Schwarz inequality
was used because it implies that x  y a jxj jyj.
n
*3.1.5
Other Norms and Norm Inequalities for Rn
It turns out that there are many norms that can be defined on Rn in addition to the
standard norm in (3.3).
Example 3.19
1. For any p with 1a p < y, the so-called lp-norm, pronounced ‘‘lp-norm,’’ is de-
fined by
3.1
Euclidean Space
77

kxkp 1
X
n
j¼1
jxijp
 
!1=p
:
ð3:10Þ
2. Extending to p ¼ y, the so-called lT-norm, pronounced ‘‘l infinity norm,’’ is
defined by
kxky ¼ max
i
jxij:
ð3:11Þ
Remark 3.20
We still have to prove that these lp-norms are true norms by the defini-
tion above, but note that for p ¼ 2, the l2-norm is identical to the standard norm
defined in (3.3). So the lp-norms can be seen to generalize the standard norm by gen-
eralizing the power and root used in the definition. Also, as will be seen below, while
appearing quite di¤erently defined, the ly-norm will be seen to be the ‘‘limit’’ of the
lp-norms as p increases to y.
The challenge of demonstrating that these examples provide true norms is to show
the triangle inequality to be satisfied, since the other needed properties are easy to
verify. For the ly-norm in (3.11) the triangle inequality follows from (2.7), since the
ly-norm is a maximum of absolute values. That is, jxi þ yij a jxij þ jyij for any i by
(2.7), and we have that
max
i
jxi þ yij a max
i
ðjxij þ jyijÞ a max
i
jxij þ max
i
jyij:
Similarly the l1-norm again satisfies the triangle inequality due to (2.7), since the l1-
norm is a sum of absolute values, and
X
n
j¼1
jxi þ yij a
X
n
j¼1
jxij þ
X
n
j¼1
jyij:
For the lp-norm with 1 < p < y, the proof will proceed in a somewhat long series
of steps that should be simply scanned on first reading, focusing instead on the flow
of the logic. The proof proceeds in steps:
1. First o¤, the triangle inequality in this norm is called the Minkowski inequality
or Minkowski’s inequality, and was derived by Hermann Minkowski (1864–1909) in
1896. The proof of this inequality requires a generalization of the Cauchy–Schwarz
inequality, which is called the Ho¨lder inequality or Ho¨lder’s inequality, derived by
Otto Ho¨lder (1859–1937) in 1884 in a more general context than presented here.
2. To derive Ho¨lder’s inequality, we require Young’s inequality, which was derived
by W. H. Young (1863–1942) in 1912.
78
Chapter 3
Euclidean and Other Spaces

Reversing the steps to a proof, we begin with Young’s inequality. It introduces a
new notion that arises often in the study of lp-norms, and that is the notion of an
index q being the conjugate index to p. Specifically, given 1 < p < y, the index q is
said to be conjugate to p if 1
p þ 1
q ¼ 1. It is then easy to see that q ¼
p
p1 also satisfies
1 < q < y, and that p is also conjugate to q. In some cases this notion of conjugacy
is extended to 1 a p a y, where one defines
1
y 1 0, and hence p ¼ 1 and q ¼ y
are conjugate. This notion highlights the uniqueness of the index p ¼ 2, namely that
this is the only index conjugate to itself, a fact that will later be seen to be quite
significant.
Before turning to the statement and proof of Young’s inequality, note that the nat-
ural logarithm is a concave function, which means that for any x; y > 0,
t ln x þ ð1  tÞ ln y a lnðtx þ ð1  tÞyÞ
for 0 a t a 1:
ð3:12Þ
Graphically, for given points x; y > 0, say y > x > 0 for definiteness, the straight
line connecting the points ðx; ln xÞ and ðy; ln yÞ never exceeds the graph of the func-
tion f ðzÞ ¼ ln z for x a z a y. This line in fact is always below the graph of this
function except at the endpoints, where the curve and line intersect. This is a prop-
erty called ‘‘strictly concave.’’
This property is di‰cult to prove with the tools thus far at our disposal, but as will
be seen in chapter 9, the tools there will make this an easy derivation. At this point
we simply note that the inequality in (3.12) is equivalent to the arithmetic mean–
geometric mean inequality whenever t is a rational number. This familiar inequality,
which is also developed in chapter 9, states that for any collection of positive num-
bers, fxign
i¼1, that AM b GM, or notationally,
1
n
X
n
i¼1
xi b
Y
n
i¼1
xi
 
!1=n
:
ð3:13Þ
If t ¼ a
b , a rational number in ½0; 1, apply (3.13) with a of the xi equal to x, and
b  a of the xi equal to y, producing
a
b x þ
1  a
b


y b xa=by1ða=bÞ:
Taking logarithms of this inequality is equivalent to (3.12) for rational t A ½0; 1.
While it is compelling that (3.12) is proved true for all rational t, the tools of chapter
9 are still needed to extend this to all t A ½0; 1. For now, we assume (3.12) and defer a
proof to chapter 9.
3.1
Euclidean Space
79

Proposition 3.21 (Young’s Inequality)
Given p, q so that 1 < p; q < y, and 1
p þ 1
q ¼
1, then for all a; b > 0,
ab a ap
p þ bq
q :
ð3:14Þ
Proof
Assuming the concavity of ln x, and with t ¼ 1
p in (3.12), we derive
lnðabÞ ¼ ln ap
p
þ ln bq
q
a ln ap
p þ bq
q


:
The result in (3.14) follows by exponentiation.
n
Remark 3.22
The notion of concave function in (3.12) makes sense for any function
f : X ! R, and not just where X is the one-dimensional real line. All that is required is
that X is a vector space over R so that the addition of vectors in the inequality makes
sense. In other words, a function f is concave if for x; y A X,
tf ðxÞ þ ð1  tÞ f ðyÞ a f ðtx þ ð1  tÞyÞ
for 0 a t a 1:
ð3:15Þ
As noted above, the next result generalizes the Cauchy–Schwarz inequality, which
is now seen as the special case: p ¼ q ¼ 2.
Proposition 3.23 (Ho¨lder’s Inequality)
Given p, q so that 1 a p; q a y, and 1
p þ 1
q ¼
1, where notationally, 1
y 1 0, we have that
jx  yj a kxkpkykq:
ð3:16Þ
In other words, the absolute value of the standard inner product is bounded above by the
product of the lp- and lq-norms of the vectors, if ðp; qÞ are a conjugate pair of indexes.
Proof
First, if p ¼ 1 and q ¼ y or conversely, then by the triangle inequality for
absolute value in (2.7) applied to (3.4),
jx  yj a
X
n
i¼1
jxiyij a max
i
jxij
X
n
i¼1
jyij ¼ kxkykyk1:
Otherwise, we apply Young’s inequality n-times to each term of the summation with
ai 1 jxij
kxkp , and bi 1 jyij
kykq , which produces
80
Chapter 3
Euclidean and Other Spaces

X
n
i¼1
jxij
kxkp
 jyij
kykq
a 1
p
X
n
i¼1
jxijp
kxkp
p
þ 1
q
X
n
i¼1
jyijq
kykq
q
¼ 1
p þ 1
q ¼ 1;
and consequently, Pn
i¼1 jxij jyij a kxkpkykq. Now since jx  yj a Pn
i¼1 jxij jyij by the
triangle inequality, the result follows.
n
Finally, the goal of this series of results, that the lp-norms satisfy the triangle in-
equality, can now be addressed:
Proposition 3.24 (Minkowski’s Inequality)
Given p with 1 a p a y,
kx þ ykp a kxkp þ kykp:
ð3:17Þ
Proof
The cases of p ¼ 1; y, were handled above, so we assume that 1 < p < y.
We then have by (2.7),
kx þ ykp
p ¼
X
n
i¼1
jxi þ yijp1jxi þ yij
a
X
n
i¼1
jxi þ yijp1jxij þ
X
n
i¼1
jxi þ yijp1jyij:
We can now apply Ho¨lder’s inequality to the last two summations:
X
n
i¼1
jxi þ yijp1jxij a kxkp
X
n
i¼1
jxi þ yijðp1Þq
 
!1=q
¼ kxkpkx þ ykp=q
p ;
X
n
i¼1
jxi þ yijp1jyij a kykp
X
n
i¼1
jxi þ yijð p1Þq
 
!1=q
¼ kykpkx þ ykp=q
p ;
since ðp  1Þq ¼ p. Combining, we get
kx þ ykp
p a ðkx þ ykp=q
p Þðkykp þ kxkpÞ;
and the result follows by division by kx þ ykp=q
p
since p  p
q ¼ 1.
n
Admittedly, quite a lot of machinery was needed to demonstrate that the definition
above for kxkp produced a true norm. However, there will be a significant payo¤ in
later chapters as these norms are the basis of important spaces of series, and in later
studies, important spaces of functions.
3.1
Euclidean Space
81

Remark 3.25
Note that despite its appearance the ly-norm, kxky, is the limit of the
lp-norms kxkp as p ! y. That is,
kxkp ! kxky
as p ! y:
To see this, assume that the ly-norm of x satisfies kxky ¼ jxjj. That is, no component
is larger in absolute value than the jth element. Then
kxkp
kxky
¼
X
n
i¼1
jxijp
kxkp
y
 
!1=p
¼
X
n
i¼1
lp
i
 
!1=p
:
Now, since lj ¼ 1 and all other li a 1, we have 1 a Pn
j¼1 lp
i a n, and hence the pth
root of this sum approaches 1 as p ! y.
3.2
Metric Spaces
3.2.1
Basic Notions
An important application of the notion of a norm is that it provides the basis for
defining a distance function or a metric, which will be seen to have many applications.
On Rn, the standard metric is defined in terms of the standard norm by
dðx; yÞ 1 jx  yj:
ð3:18Þ
Just as the general definition of norm was intended to capture the essential proper-
ties of the standard norm jxj defined on Rn, so too is the general definition of dis-
tance or metric intended to capture the essential properties of jx  yj defined on Rn.
The connection between norms and metrics is discussed below, but note that in order
for a set X to have a norm defined on it, this set must have an arithmetic structure so
that quantities like x þ y, and ax make sense. Consequently norms are defined on
vector spaces that allow such an arithmetic structure. On the other hand, a metric
can be defined on far more general sets than vector spaces.
Definition 3.26
A distance function or metric on an arbitrary set X is defined as a
real-valued function on X 2 1 X  X, and denoted dðx; yÞ or dðx; yÞ, with the following
properties:
1. dðx; xÞ ¼ 0.
2. dðx; yÞ > 0 if x 0 y.
82
Chapter 3
Euclidean and Other Spaces

3. dðx; yÞ ¼ dðy; xÞ.
4. (Triangle inequality) dðx; yÞ a dðx; zÞ þ dðz; yÞ for any z A X.
If X is a vector space over F , a distance function is called translation invariant if for
any z A X:
5. dðx; yÞ ¼ dðx þ z; y þ zÞ.
A distance function is called homogeneous if for any a A F :
6. dðax; ayÞ ¼ jajdðx; yÞ.
Definition 3.27
A metric space is any collection of points X on which there is defined
a distance function or metric dð ; Þ. For clarity, a metric space may be denoted ðX; dÞ.
Remark 3.28
The name ‘‘triangle inequality’’ will be momentarily shown to be consis-
tent with the same notion defined in the context of norms.
Proposition 3.29
If dðx; yÞ is a given metric, then:
1. d 0ðx; yÞ 1 ldðx; yÞ is a metric for any real l > 0.
2. d 0ðx; yÞ 1
dðx;yÞ
1þdðx;yÞ is a metric.
Proof
The first statement follows easily from the definition, and in this case, the
new metric d 0 can be thought of as measuring distances in a di¤erent set of units.
For example, if d measures distances in units of meters, then with l ¼ 100, d 0 pro-
vides distances in centimeters. For the second statement, only the triangle inequality
requires examination. To show that
dðx; yÞ
1 þ dðx; yÞ a
dðx; zÞ
1 þ dðx; zÞ þ
dðz; yÞ
1 þ dðz; yÞ ;
we simply cross-multiply, since all denominators are positive, and cancel common
terms.
n
This second metric is interesting because under this definition, the distance between
any two points of X is less than 1. More specifically, for any l, 0 a l < 1,
d 0ðx; yÞ ¼ l
if and only if
dðx; yÞ ¼
l
1  l ;
ð3:19aÞ
dðx; yÞ ¼ l
if and only if
d 0ðx; yÞ ¼
l
1 þ l :
ð3:19bÞ
3.2
Metric Spaces
83

3.2.2
Metrics and Norms Compared
Because the definitions of norm and metric appear so related, it is natural to wonder
about the connection between the two concepts. Can we make norms out of metrics
and metrics out of norms? First, we have to be careful because, as noted above,
norms are always defined on vector spaces while a metric can be defined on an arbi-
trary set. Norms require an arithmetic structure on the set X, since one item in the
definition required that j0j ¼ 0, and hence we needed to have 0 A X well defined.
Given x; y A X and a A R, we also require in the definition of norm that x þ y A X
and ax A X be well defined. So, by definition, a normed space must have this mini-
mal arithmetic structure, and the vector space structure is a natural requirement as
noted in the norm definition.
On the other hand, a metric can be defined on any set, as long as the distance func-
tion dðx; yÞ satisfies the required properties. There are no arithmetic operations on
the elements of X as part of the definition of metric. So the better question is, Given
a vector space X, can we make norms out of metrics and metrics out of norms?
The following shows that if the metric satisfies the additional properties 5 and 6
above, that a norm can be constructed.
Proposition 3.30
If dðx; yÞ is a metric on a vector space X that is homogeneous and
translation invariant, then kxk 1 dðx; 0Þ is a norm and is said to be induced by the
metric d.
Proof
Property 1 in the norm definition, that jxj A R, follows from a metric being a
real-valued function, while norm property 2, that j0j ¼ 0, and jxj > 0 for x 0 0, fol-
lows from 1 and 2 in the metric definition. Finally, norm property 3, that jaxj ¼
jaj jxj for a A R, follows from the assumed homogeneity of d, while norm property
4, that jx þ yj a jxj þ jyj is a consequence of translation invariance and homogene-
ity. Specifically,
jx þ yj ¼ dðx þ y; 0Þ ¼ dðx; yÞ a dðx; 0Þ þ dð0; yÞ ¼ jxj þ jyj:
n
The reverse implication is easier: on a vector space, a norm always gives rise to a
distance function.
Proposition 3.31
If kxk is a norm on a vector space X, then
dðx; yÞ 1 kx  yk;
ð3:20Þ
is a metric on X, and in particular, ðX; dÞ is a metric space. The metric d is said to be
induced by the norm k k.
84
Chapter 3
Euclidean and Other Spaces

Proof
Only distance property 4, which is again called the triangle inequality,
requires comment. Rewriting, we seek to prove that
dðx; yÞ a dðx; zÞ þ dðz; yÞ;
kx  yk a kx  zk þ kz  yk:
Letting x0 ¼ x  z, and y0 ¼ z  y, we have that x0 þ y0 ¼ x  y, and this inequality
for d is equivalent to the triangle inequality for the associated norm applied to x0, y0
and x0 þ y0.
n
Corollary 3.32
dðx; yÞ 1 jx  yj defined in (3.3) is a metric on Rn, and consequently
ðRn; dÞ is a metric space. In addition dðx; yÞ 1 jx  yj defined in (2.2) is a metric on
C, and consequently ðC; dÞ is a metric space.
Proof
The proof follows immediately from the proposition above.
n
The corollary above provides the ‘‘natural’’ metric on Rn, but there are many
more that are definable in terms of the various lp-norms:
Corollary 3.33
Given any lp-norm kxkp for 1 a p a y on Rn, then
dpðx; yÞ 1 kx  ykp;
1 a p a y;
ð3:21Þ
is a metric on Rn, and consequently ðRn; dpÞ is a metric space.
Proof
The proof follows immediately from the proposition above, since Rn is a vec-
tor space.
n
Remark 3.34
Of course, d2ðx; yÞ in this corollary is just the standard metric dðx; yÞ
on Rn defined in (3.3). The metrics defined in (3.21) are referred to as lp-metrics, or
metrics induced by the lp-norms.
To understand the structure of these lp-metrics, dpðx; yÞ, we investigate R2 where
visualization is simple but instructive. Specifically, it is instructive to graph the closed
lp-ball of radius 1 about 0,
Bp
1ð0Þ ¼ fx A R2 j dpðx; 0Þ 1 kxkp a 1g;
ð3:22Þ
for various values of p, 1 a p a y. Analogously, one can define the closed lp-ball of
radius r about y by
Bp
r ðyÞ ¼ fx A R2 j dpðx; yÞ 1 kx  ykp a rg:
ð3:23Þ
3.2
Metric Spaces
85

The corresponding open lp-ball of radius 1 about 0 is defined as
Bp
1ð0Þ ¼ fx A R2 j dpðx; 0Þ 1 kxkp < 1g;
ð3:24Þ
and the open lp-ball of radius r about y by
Bp
r ðyÞ ¼ fx A R2 j dpðx; yÞ 1 kx  ykp < rg:
ð3:25Þ
Note that all these lp-ball definitions makes sense in any Rn. Of course, for p ¼ 2,
the closed l2-ball of diameter 1 is truly a ‘‘2-dimensional ball,’’ and it represents the
familiar circle of radius 1, including its interior. In R3, it is indeed a ball, or sphere of
radius 1, again including its interior. The corresponding open balls are just the inte-
riors of these closed balls.
For other values of p, these figures do not resemble any ball we would ever con-
sider playing with, but mathematicians retain the familiar name anyway. For exam-
ple, lp-balls about 0 for p ¼ 1; 1:25; 2; 5, and y in R2 are seen in figure 3.1. These
can be understood to be open or closed balls depending on whether or not the
‘‘boundary’’ of the ball is included.
For p ¼ 1, this innermost ‘‘ball’’ has corners at its intersection points with the
coordinate axes, while for p > 1, these corners round out, approaching a circle as
p ! 2. For p > 2, these balls again begin to square o¤ in the direction of the diago-
nal lines in the plane, y ¼Gx. It is clear from this figure that these balls very quickly
Figure 3.1
lp-Balls: p ¼ 1; 1:25; 2; 5; y
86
Chapter 3
Euclidean and Other Spaces

converge to the ly-ball, which is the square with sides parallel to the axes, and four
corners at ðG1;G1Þ.
Even more generally, given any metric space ðX; dÞ or normed space, ðX; kxkÞ,
one can define the closed ball of radius r about y by
BrðyÞ ¼ fx A X j dðx; yÞ a rg;
ð3:26Þ
or
BrðyÞ ¼ fx A X j kx  yk a rg;
ð3:27Þ
as well as the associated open ball of radius r about y, denoted BrðyÞ, using strict in-
equality <, rather than the inequalitya.
One thing that each of these balls has in common with a true ball, if 1 a p a y, is
that they are all convex sets. This means that if x1; x2 A Bp
r ðyÞ, then the straight line
segment joining these points also lies in Bp
r ðyÞ. That is,
If x1; x2 A Bp
r ðyÞ; then tx1 þ ð1  tÞx2 A Bp
r ðyÞ for 0 a t a 1:
ð3:28Þ
The same is true for a closed ball in a general normed space, as well as in a metric
space X that is also a vector space, so in (3.28), tx1 þ ð1  tÞx2 makes sense. And
similarly open balls are convex:
If x1; x2 A Bp
r ðyÞ; then tx1 þ ð1  tÞx2 A Bp
r ðyÞ for 0 a t a 1:
ð3:29Þ
Use of this terminology and of the word ‘‘convex’’ is related to the notion of a
concave function defined in (3.12). Analogously, the lp-ball above and the general
normed ball are convex because a norm, interpreted as a function f ðxÞ ¼ kxk, is a
convex function. That is, given x1, x2,
ktx1 þ ð1  tÞx2k a tkx1k þ ð1  tÞkx2k
for 0 a t a 1:
ð3:30Þ
This inequality follows directly from the triangle inequality. Stated more generally, a
function f ðxÞ is a convex function if for x1; x2 A X,
f ðtx1 þ ð1  tÞx2Þ a tf ðx1Þ þ ð1  tÞf ðx2Þ
for 0 a t a 1:
ð3:31Þ
Note that here the inequality is reversed compared to the definition of concave func-
tion in (3.15) above.
Graphically, when X is the real line and x < y, the inequality in (3.31) states that
on the interval ½x; y, the value of the function never rises above the line segment
connecting ðx; f ðxÞÞ and ðy; f ðyÞÞ. This insight on convexity provides a geometric
3.2
Metric Spaces
87

interpretation of the implication of the triangle inequality as required in the defini-
tion of norm. That is, the triangle inequality assures that all balls defined by norms
are convex sets. Also the reason why no attempt was made to define an lp-norm for
0 < p < 1 is that in these cases the triangle inequality is not satisfied and geometri-
cally, as is easily demonstrated, the associated lp-balls are not convex.
For example, with p ¼ 0:5, we have B0:5
1 ð0Þ in figure 3.2. If we choose x1 ¼ ð1; 0Þ
and x2 ¼ ð0; 1Þ, it is clear that ktx1 þ ð1  tÞx2k0:5 ¼ kðt; 1  tÞk0:5 > 1 for 0 < t < 1,
and this point is outside the ball. However, tkx1k0:5 þ ð1  tÞkx2k0:5 ¼ 1. Conse-
quently this ball is not convex by definition, as is also visually apparent.
*3.2.3
Equivalence of Metrics
Two metrics on a metric space X, say d1 and d2, may produce di¤erent numerical
values of distance between arbitrary points x; y A X, but they may be fundamentally
‘‘equivalent’’ in terms of conclusions that might be drawn from certain observations
on the space. A trivial example on R would be where d1ðx; yÞ ¼ jx  yj, the standard
metric, and d2ðx; yÞ ¼ ld1ðx; yÞ, where l is a positive real number. As noted above,
d2 is a metric for any positive number l. Also, while all such metrics produce di¤er-
ent numerical values of distance, such as miles and kilometers, they are fundamen-
tally the same in many ways.
For this example, if fxn; yg H X is a collection of points so that d1ðxn; yÞ ! 0 as
n ! y, we would observe the same property under d2 for any positive l. Corre-
Figure 3.2
lp-Ball: p ¼ 0:5
88
Chapter 3
Euclidean and Other Spaces

spondingly d2ðxn; yÞ ! 0 as n ! y would imply the same thing about d1. Note that
a formal definition of what d2ðxn; yÞ ! 0 means will be presented in the chapter 5,
but the intuition for this idea is adequate for our purposes here.
In general, two metrics are defined as equivalent when this simultaneous conver-
gence property is satisfied. The following definition provides a neat way of ensuring
this conclusion:
Definition 3.35
Two metrics, d1 and d2, on a metric space X are Lipschitz equivalent
if there exists positive real constants l1 and l2 so that for all x; y A X,
l1d1ðx; yÞ a d2ðx; yÞ a l2d1ðx; yÞ:
ð3:32Þ
Lipschitz equivalence is named for Rudolf Lipschitz (1832–1903), who introduced
a related notion of Lipschitz continuity that will be studied in chapter 9.
It is clear from this definition that the original objective is satisfied. That is, it
would seem clear that
d1ðxn; yÞ ! 0
i¤
d2ðxn; yÞ ! 0;
based on our current informal understanding of the definition of convergence. But
logically, and this will be made rigorous in chapter 5, the result is forced by the
inequalities in (3.32).
Note that every metric is Lipschitz equivalent to itself, and also it is easy to see
that this notion of Lipschitz metric equivalence is symmetric. That is, if (3.32), then
1
l2
d2ðxn; yÞ a d1ðxn; yÞ a 1
l1
d2ðxn; yÞ:
ð3:33Þ
This notion is also transitive: if d1 and d2 are Lipschitz equivalent, and d2 and d3 are
Lipschitz equivalent, then d1 and d3 are Lipschitz equivalent.
An important concept in mathematics is one of an equivalence relation, defined on an
arbitrary set. The simplest equivalence relation is equality, where xRy denotes x ¼ y.
Definition 3.36
An equivalence relation on a set X, denoted xRy or x @ y as short-
hand for ‘‘x is related to y,’’ is a binary relation on X; that is:
1. Reflexive:
xRx for all x A X.
2. Symmetric:
xRy if and only if yRx.
3. Transitive:
if xRy and yRz, then xRz.
The importance of equivalence relations is that one can form equivalence classes of
elements of X. An equivalence class is a collection of elements related to each other
3.2
Metric Spaces
89

under R. It is defined so that any two elements from a given class are equivalent,
while any two elements from di¤erent classes are not equivalent.
For example, the collections of Lipschitz equivalent metrics on a given space X are
equivalence classes. For many applications it matters not which element of the class
is used. For example, continuing with some informality, if we define xn ! y by
dðxn; yÞ ! 0 for a given metric d, we could equally well define xn ! y relative to
any metric in the equivalence class of d. That is, the notion xn ! y depends not so
much on d as on the equivalence class of d. If this property is true for a given d, it is
also true for an other d 0 that is Lipschitz equivalent, d @L d 0, while if this property is
false for a given d, it is also false for an other d 0 with d @L d 0. However, in neither
case can one draw a conclusion about the truth or falsity of this property for metrics
outside the given equivalence class.
Proposition 3.37
If dðx; yÞ is a metric on X, then:
1. ldðx; yÞ @L dðx; yÞ for any real l > 0.
2. d 0ðx; yÞ 1
dðx;yÞ
1þdðx;yÞ @L dðx; yÞ if and only if dðx; yÞ a M for all x; y A X.
Proof
In defining d2ðx; yÞ ¼ ldðx; yÞ and d1ðx; yÞ ¼ dðx; yÞ, it is apparent that
(3.32) is satisfied with l1 ¼ l2 ¼ l, proving part 1. The second statement is initially
less obvious, but it follows directly from the one-to-one correspondence between d
and d 0 distances in (3.19). With d2ðx; yÞ ¼ d 0ðx; yÞ and d1ðx; yÞ ¼ dðx; yÞ, we derive
from (3.19b) that d 0ðx; yÞ a dðx; yÞ, which is consistent with l2 ¼ 1 in (3.32). For the
other inequality we have from (3.19b) that if dðx; yÞ a M, then d 0ðx; yÞ a
M
Mþ1 ,
which is algebraically equivalent to
1
1d 0ðx;yÞ a 1 þ M. Then from (3.19a),
dðx; yÞ ¼
d 0ðx; yÞ
1  d 0ðx; yÞ a ð1 þ MÞd 0ðx; yÞ;
and so the second inequality in (3.32) is satisfied with l1 ¼
1
Mþ1 . If dðx; yÞ is un-
bounded, there can be no l1 for which l1dðx; yÞ a d 0ðx; yÞ, since d 0ðx; yÞ a 1.
n
In addition to these examples of equivalent metrics, it may be surprising but it
turns out that the various lp-norms, for 1 a p a y, are equivalent in Rn.
Proposition 3.38
On Rn, all distances given by the lp-norms in (3.21) for 1 a p a y
are Lipschitz equivalent.
Proof
We first show that if 1 a p < y, that the lp-distance is Lipschitz equivalent
to the ly-distance. For given x ¼ ðx1; x2; . . . ; xnÞ and y ¼ ðy1; y2; . . . ; ynÞ, we have
that
90
Chapter 3
Euclidean and Other Spaces

max
i
jxi  yijp a
X
n
i¼1
jxi  yijp a n max
i
jxi  yijp:
That is, taking pth roots:
dyðx; yÞ a dpðx; yÞ a n1=pdyðx; yÞ;
and so every lp-distance is Lipschitz equivalent to the ly-distance if 1 a p < y.
Since Lipschitz equivalence is transitive, we conclude that dpðx; yÞ is equivalent to
dp 0ðx; yÞ for any 1 a p; p0 a y. In fact, using (3.32) and (3.33), we can infer bounds
between dpðx; yÞ and dp 0ðx; yÞ:
n1=p0dp 0ðx; yÞ a dpðx; yÞ a n1=pdp 0ðx; yÞ:
ð3:34Þ
n
Remark 3.39
1. Note that the l1 and l2 bounds between dpðx; yÞ and dyðx; yÞ are sharp in that these
bounds can be achieved by examples and hence cannot be improved upon. The left-
hand bound is attained, for example, with x ¼ ðx; 0; . . . ; 0Þ and y ¼ ðy; 0; . . . ; 0Þ, or
with x and y being similarly defined to be on the same ‘‘axis.’’ We can in fact observe
this equality in figure 3.1, where the five lp-balls about 0 for p ¼ 1; 1:25; 2; 5; y, are
seen to intersect at the axes. On the other hand, the right-hand bound is attained for
x ¼ ðx; x; . . . ; xÞ and y ¼ ðy; y; . . . ; yÞ, as well as other point combinations with
jxi  yij ¼ c > 0—that is, on the ‘‘diagonals’’ of Rn, which is again seen on figure
3.1. However, the inequalities between dpðx; yÞ and dp 0ðx; yÞ in (3.34) are not sharp,
as is easily verified by considering the case p ¼ p0. With a more detailed analysis using
the tools of multivariate calculus, we would obtain the sharp bounds with 1 a p a
p0 a y,
dp 0ðx; yÞ a dpðx; yÞ a nð p0pÞ=pp0dp0ðx; yÞ;
and these bounds would again be seen to be achieved on the axes and diagonals of Rn,
respectively.
2. Note also that the Lipschitz equivalence of dpðx; yÞ and dyðx; yÞ, and more gener-
ally, of dpðx; yÞ and dp 0ðx; yÞ, depends on the dimension of the space n in a way that
precludes any hope that this equivalence will be preserved as n ! y (as will be formal-
ized in chapter 6 on series). In other words, an informal consideration of the notion of
an Ry suggests that the various lp-distances will not be Lipschitz equivalent.
3.2
Metric Spaces
91

3. Not all metrics are Lipschitz equivalent to those in this proposition. For example,
define
dðx; yÞ ¼
0;
x ¼ y
1;
x 0 y

:
It is easy to show that this is indeed a metric on Rn that is not Lipschitz equivalent to
the lp-distances.
4. It was noted above that every norm on a vector space induces a metric on that space.
Consequently it is common to say that two such norms are Lipschitz equivalent if the
respective induced metrics are equivalent in the above-described sense.
As a final comment regarding Lipschitz equivalence of metrics, we note that there
is a simple and natural geometric interpretation of this concept. First, we introduce a
more general notion of metric equivalence, sometimes called topologically equiva-
lent. The term ‘‘topology’’ will be addressed in chapter 4, and is related to the notion
of open sets in a space.
Definition 3.40
Two metrics on a metric space X, say d1 and d2, are equivalent, and
sometimes topologically equivalent for specificity, if for any x A X and r > 0, Bð2Þ
r ðxÞ
defined relative to d2 both contains an open d1-ball and is contained in an open d1-
ball. That is, there are real numbers r1, r2, both formally functions of r and x, so that
Bð1Þ
r1 ðxÞ H Bð2Þ
r ðxÞ H Bð1Þ
r2 ðxÞ;
ð3:35Þ
where Bð jÞ
r ðxÞ denotes an open ball defined relative to dj, and A H B denotes ‘‘set inclu-
sion’’ and means that every point in A is also contained in B.
Proposition 3.41
In a metric space X, if d1 and d2 are Lipschitz equivalent as in
(3.32), then they are topologically equivalent as in (3.35).
Proof
If we are given x A X and r > 0, and Bð2Þ
r ðxÞ ¼ fy j d2ðx; yÞ < rg, by (3.32) we
conclude that for any y A Bð2Þ
r ðxÞ,
l1d1ðx; yÞ a d2ðx; yÞ a l2d1ðx; yÞ;
so (3.35) is satisfied with r2 ¼ r=l1 and r1 ¼ r=l2.
n
This geometric statement is simple to see in figure 3.1. Notice that any lp-ball can
be envisioned as containing, and being contained in, two lp 0-balls for any p0. A more
specific example is seen in figure 3.3 where the l2-ball of radius 1 contains the l1-ball
92
Chapter 3
Euclidean and Other Spaces

of radius 1, and is contained in the l1-ball of radius
ffiffi
2
p
, and this l1-ball in turn is con-
tained in the l2-ball of radius
ffiffi
2
p
.
Remark 3.42
The notion of metric equivalence, or ‘‘topological equivalence,’’ is more
general than Lipschitz equivalence, since it allows the relationship between these met-
rics to vary with x A X since the numbers r1, r2 depend on x. For Lipschitz equivalence
this relationship is fixed for all x, as noted in the proof above.
3.3
Applications to Finance
3.3.1
Euclidean Space
Euclidean space provides a natural framework in any discipline in which one is try-
ing to solve problems that involve several parameters, and such problems exist in
many areas of finance. For example, in asset allocation problems one is attempting
to divide a given total investment fund between certain available asset classes, how-
ever defined, and the solution to such a problem can naturally be identified with a
point, or allocation vector, in a Euclidean space. The dimension of this space is logi-
cally equal to the number of available asset classes. In the fixed income markets the
very notion of a yield curve, which is defined in terms of the yields on a collection of
reference bonds of increasing maturities, compels the interpretation of a yield curve
Figure 3.3
Equivalence of l1- and l2-metrics
3.3
Applications to Finance
93

vector in an appropriately dimensioned Euclidean space. Such yield vectors can then
be translated to spot rate or forward rate vectors as needed by the given application,
or used in a price risk analysis. Finally, a given security or portfolio of securities can
be modeled in terms of projected cash flows, and these cash flow vectors, whether
fixed or variable, can then be used in a variety of portfolio modeling applications.
Asset Allocation Vectors
An asset allocation problem involves determining a vector of dollar amounts: ðx1;
x2; . . . ; xnÞ, where n denotes the number of available assets, xi denotes the dollar in-
vestment in the ith asset, and P xi ¼ A, the total amount to be invested. In certain
applications, all xi satisfy xi b 0 and represent long positions, but we can allow
xi < 0 in cases where short-selling is possible. Equivalently, we can parametrize the
solution to the problem in percentage units so that xi denotes the proportion of the
portfolio to be invested in the ith asset, again long or short, and then P xi ¼ 1.
Alternatively, the n-tuple ðx1; x2; . . . ; xnÞ might represent a portfolio trade, whereby
xi > 0 implies a purchase and xi < 0 a sale of jxij units of the ith asset, and now
P xi ¼ 0 unless the trade is intended to also increase or decrease the portfolio bal-
ance due to net deposits or redemptions. In all such cases it is only natural to think
of the feasible n-tuples as residing in some collective structure such as Rn. This is es-
pecially true in the trading model, since the vector space arithmetic properties of Rn
exactly reflect arithmetic operations for such trades. Scalar multiplication by 2, say,
which doubles the trading done, doubles each individual trade, which is to say, is
reflected componentwise in the trade vector. If one trade is implemented after an-
other, the net trade is equivalent to the componentwise sum of the trade vectors.
However, this may appear to be a case of overkill. Admittedly, in all such cases the
real world feasible solution space is a finite collection of points, which clearly Rn is
not. The real world provides a finite solution set because first, no portfolio can be ar-
bitrarily large, nor can a trade be implemented in arbitrarily large volumes. Second,
even the maximally detailed solution cannot be implemented in units of less than
$.01 in the United States, or 1< in Japan, or .01@ in the European Union, and so
there are only finitely many portfolio allocations, or trades, to consider. More realis-
tically, assets cannot be acquired in such units. For instance, we cannot acquire an
extra $.01 of a given US asset, and so the feasible solution set is far cruder than this
maximally detailed solution set implies.
Ironically, most problems in finance are harder to solve if one explicitly recognizes
the finiteness of this solution set. That is, if the objective of the asset allocation or
portfolio trade is to optimize a given function, referred to as the objective function,
it can be very di‰cult to solve this problem over the finite ‘‘grid’’ of feasible solu-
94
Chapter 3
Euclidean and Other Spaces

tions, other than by a brute-force search. The di‰culty arises because despite its
finiteness, the feasible solution set can be quite large. In most cases it is far easier to
make believe that one can trade any amount of any asset and solve the problem at
hand using the methods of later chapters that take advantage of the structure of Rn.
It is then reasonable to assume that the approximate implementation in the real
world of this too-detailed solution will be quite close to that which would have been
obtained had the finite feasibility set been explicitly recognized at the outset.
That is, by interpreting our problem in an artificially refined setting of Rn, we sim-
plify the solution, but we are then required to assume that the approximate imple-
mentation of the exact solution is close to the exact solution obtained had we begun
with the finite feasible solution set. In many cases this assumption can be checked.
That is, once we solve the more detailed problem, we can investigate to what extent
its approximate implementation is an optimal or near-optimal solution among feasi-
ble alternatives. Even this analysis can be simpler than searching for a best solution
on the grid at the outset.
Interest Rate Term Structures
There are three common bases for describing the term structures of interest rates,
where by ‘‘structure’’ is meant the functional dependence of rates on the term of the
implied loan. In practice, the most readily available data for loans exist in the bond
markets. The three term structure bases are:
1. Bond Yields:
The interest rates that equate each coupon bond’s price to the pres-
ent value of the bond’s scheduled cash flows.
2. Spot Rates:
The bond yields on real or hypothetical zero coupon bonds.
3. Forward Rates:
The bond yields on ‘‘forward’’ zero coupon bonds, which is to
say, the yield today for future investments in zero coupon bonds.
The bond market provides insights to these structures, but for the term structure to
be meaningful, it is important that as many of the bond characteristics as possible are
controlled for, so that only the dependency on the bond’s terms remain.
For example, it is common to group bonds by currency and credit quality, avoid-
ing when possible unusual cash flow structures that get special pricing, or bonds with
embedded options. One special class in every major currency is the class of all risk-
free Treasury bonds issued by the country’s central government. Bonds at the next
highest credit rating, often denoted AAA or Aaa, are then grouped, as are the next
level of AA or Aa, and so forth. With enough bonds in a given group, a term struc-
ture can be inferred in any of the three bases. When bond data are sparse, interpola-
tion techniques are often used to estimate missing data.
3.3
Applications to Finance
95

For a bond yield or spot rate, there is one implied time parameter determined by
the maturity of the bond. For forward rates, there are two time parameters: one
establishes the time of the investment in the forward zero coupon bond, and the sec-
ond determines the time of maturity of this bond.
To illustrate the calculation of these term structures, we assume that bonds have
semiannual coupons and that there are bonds available at all maturities from 0:5 to
n-years. As noted above, interpolation is often necessary to infer information at
maturities that have no market representatives. We also implement all calculations
with semiannual nominal rates, but note that these calculations can be implemented
in any nominal basis.
Bond Yields
Using (2.15), bond yields at each maturity are derived by solving the
following equations for fijg, the semiannual bond yields:
Pj ¼ Fj
rj
2 a2j;ij=2 þ Fjv2j
ij=2;
j ¼ 0:5; 1:0; 1:5; . . . ; n:
ð3:36Þ
Here j denotes the term of the bond in years; fPjg are the bonds’ prices, frjg the
semiannual coupon rates, and fFjg the bonds’ par values. It is typical to fix
Fj ¼ 100, and so Pj denotes the price per 100 par. The result is the bond yield term
structure: ði0:5; i1; . . . ; inÞ, which can be envisioned as a vector in R2n.
One numerical approach to solving these equations, called interval bisection, is dis-
cussed in chapters 4 and 5.
Spot Rates
From the same data used to determine the bond yield term struc-
ture, one can in theory calculate the spot rate structure, since a coupon bond is
nothing but a portfolio of zero coupon bonds. Using (2.19), the price Pj must reflect
spot rates: ðs0:5; s1; . . . ; sjÞ, each appropriate to discount a single cash flow of the
bond:
Pj ¼ Fj
rj
2
X
2j
k¼1
1 þ sk=2
2

k
þ Fj
1 þ sj
2

2j
:
ð3:37Þ
Notation 3.43
In this summation the present value of the cash flow at time k-years is
calculated with the factor
1 þ sk
2

2k
;
but then the summation above would be expressed in the nonstandard notation as
96
Chapter 3
Euclidean and Other Spaces

X
j
k¼0:5
1 þ sk
2

2k
;
where it would be hoped that the reader understood that the index values must be incre-
mented by 0:5. To avoid this notational ambiguity, we use standard natural number
indexing, and consequently we need to halve the index values to obtain the correct
result.
Forward Rates
As noted above, forward rates are functions of two time parameters,
defining the investment date in the zero coupon bond and the maturity date. In other
words, a forward can be denoted, fj;k, where j; k A f0; 0:5; 1:0; 1:5; . . . ; ng, with
k > j. In this notation, fj;k denotes the yield today for a ðk  jÞ-year zero coupon
bond, which is to be acquired at time j-years. Consequently f0;k ¼ sk. The forward
rate fj;k would be described as the ðk  jÞ-year forward rate at time j-years.
In the same way that sk is appropriate for discounting a cash flow from time k-
years to time 0, the forward rate fj;k is appropriate for discounting a cash flow from
time k-years to time j-years. With this interpretation, it must be the case that one can
discount from time k-years to time 0 either with the spot rate sk, or a sequence of
forward rates:
f0;0:5; f0:5;1:0; f1:0;1:5; . . . ; fk0:5;k:
Of course, if k is an integer, one could also use the forward rates:
f0;1:0; f1:0;2:0; . . . ; fk1;k:
Specifically, using the first sequence, and recalling the notational comment above,
obtains
1 þ sk=2
2

k
¼
Y
k
i¼1
1 þ fði1Þ=2;i=2
2

1
:
ð3:38Þ
So the price of a bond can be written in the messy but unambiguous notation
Pj ¼ Fj
rj
2
X
2j
k¼1
Y
k
i¼1
1 þ fði1Þ=2;i=2
2

1
þ F
Y
2j
i¼1
1 þ fði1Þ=2;i=2
2

1
:
ð3:39Þ
In general, forward rates are calculated in series for applications, since from these
any forward fj;k can be calculated in the same way one calculates spot rates. Revert-
ing to the original notation with j; k A f0:5; 1:0; 1:5; . . . ; ng obtains
3.3
Applications to Finance
97

1 þ fj;k
2

2ðkjÞ
¼
Y
2k
i¼2jþ1
1 þ fði1Þ=2;i=2
2

1
:
ð3:40Þ
Equivalence of Term Structures
What is apparent from the three bond pricing for-
mulas (3.36), (3.37), and (3.39) is that if a term structure is given in any of the three
bases, all coupon bonds can be priced. What is also apparent is that these term struc-
tures must be consistent and produce the same prices, or else risk-free arbitrage is
possible.
For example, the price of zeros must be consistent with the pricing of coupon
bonds of the same issuer, since a coupon bond is a portfolio of zeros, and hence,
in theory, one can buy coupon bonds and sell zeros, or sell coupon bonds and
buy zeros. The first transaction is called coupon stripping, and the second, bond
reconstitution.
Similarly forward bond prices must be consistent with zero coupon pricing, since
by (3.38), a zero coupon bond is equivalent to a series of forward bonds. For exam-
ple, one could invest 100 in a 3-year zero, or invest this money in a 0:5-year zero,
and at the same time commit to a forward contract from time 0:5 to time 1:0 years,
and another from time 1:0 to 1:5 years, and so forth. The investment amount for
each forward contract would be calculated as the original 100 compounded with the
interest earned to that time, which is known. For example, if the 0:5-year spot rate is
2%, and the 0:5-year forward rate at time 0:5 is 2:2%, the investment amount for the
time 0:5-year forward contract would be 101, and the investment amount for the
time 1-year forward contract would be 102:11 to 2 decimals.
There is also a direct way to ‘‘replicate’’ a forward on a zero with a long/short
market trade in zero coupon bonds.
Example 3.44
Assume that a 5-year zero has semiannual yield 4%, and a 2-year zero
has yield 2%. To create a ‘‘long’’ forward contract from time 2 to time 5 years, mean-
ing an investment opportunity, we proceed as follows: In order to be able to invest 100
at time 2 years, we ‘‘short’’ 100ð1:01Þ4 of the 2-year zero, and go long an equivalent
amount of the 5-year zero. So at time 0, no out-of-pocket money is required other than
perhaps a margin account deposit, which is not a cost. At time 2 years, we ‘‘cover the
short’’ position with an ‘‘investment’’ of 100. At time 5 years, we mature the original 5-
year zero for 100ð1:01Þ4ð1:02Þ10, or 117:14 to 2 decimals. It is easy to show that if all
decimals are carried, then the rate obtained on this 100 investment at time 2 is exactly
equal to the 3-year forward rate at time 2 years, or 5:344%, implied by (3.40) and
(3.38):
98
Chapter 3
Euclidean and Other Spaces

1 þ fj;k
2

2ðkjÞ
¼ 1 þ sk
2

2k
1 þ sj
2

2j :
ð3:41Þ
So spot rates and forward rates must be equivalent because one can transact to
create zeros from forwards and forwards from zeros. Mathematically the associated
rates must satisfy (3.38), to create spot rates from forward rates, and (3.41), to create
forward rates from spot rates.
To convert between bond yields and spot rates is done as follows:
1. Spot Rates to Bond Yields:
This is the easier direction, since spot rates provide
bond prices by (3.37), and one then calculates the associated bond yields by solving
(3.36) for ij (see interval bisection in chapters 4 and 5).
2. Bond Yields to Spot Rates:
This methodology is known as bootstrapping or the
bootstrap method. First, all bond prices can be calculated from the bond yields using
(3.36). To derive the spot rates, the bootstrap method is an iterative procedure
whereby one spot rate is calculated at a time using (3.37). Specifically, one starts
with j ¼ 0:5, and this produces
P0:5 ¼ F0:5 1 þ r0:5
2


1 þ s0:5
2

1
;
from which s0:5 is easily calculated. One next calculates s1 from P1 using
P1 ¼ F1
r1
2
X
2
k¼1
1 þ sk=2
2

k
þ F1 1 þ s1
2

2
;
which can be solved since s0:5 is known from the first step. This process continues in
that once ðs0:5; s1; . . . ; sjÞ is calculated, (3.37) is used to calculate sjþ0:5 from Pjþ0:5,
which is straightforward as this is then the only unknown in this equation.
Bond Yield Vector Risk Analysis
Besides portfolio allocation vectors, or trade vectors, another natural application of
n-tuples in finance is where ðx1; x2; . . . ; xnÞ represents one of the term structures of
interest rates discussed above. For example, these might be the yields of a collection
of benchmark bonds at certain maturities in increasing order, with interpolation used
for the other yields, or a complete collection of bond yields or spot rates, or a se-
quence of forwards.
The prices of other bonds might then be modeled as a function:
Pðx1; x2; . . . ; xnÞ:
3.3
Applications to Finance
99

Within this model, one then envisions moment-to-moment changes in the term struc-
ture as vector increments to this initial yield curve:
Dx ¼ ðDx1; Dx2; . . . ; DxnÞ:
In turn, as this yield curve evolves over time, so too does the price of the portfolio,
and the change in this price can be modeled:
DPðx1; x2; . . . ; xnÞ 1 Pðx1 þ Dx1; x2 þ Dx2; . . . ; xn þ DxnÞ  Pðx1; x2; . . . ; xnÞ:
In practice, a spot rate structure is sometimes the most transparent approach. This
is because the connection between Dx and DP is then clearly visible for option-free
bonds. But there is far less transparency for bonds with embedded options. Also, al-
though spot rates can be readily calculated, they are not typically visible in market
trades, so a model that better connects DP with market observations might be a
bond yield model, whereby the mathematics needed to transform Dx on a bond yield
basis to Dy say, on a spot rate basis needed for pricing, is just part of the computer
model calculations, and then DP is modeled in terms of Dx.
Within this model, price sensitivities and hedging strategies can be evaluated. For-
mal methods for this risk analysis will be introduced in chapters 9 and 10.
Again, using an Rn-based model for such yield curve analyses is overkill formally,
as yields are rarely if ever quoted with even six decimal precision, which is equivalent
to ‘‘hundreths of a basis point’’ (1 basis point ¼ 0:01% ¼ 0:0001). However, just as in
the case of portfolio allocation and trading, most problems are easier to solve within
the framework of Rn than the discrete framework of feasible yield curves and yield
curve changes.
Cash Flow Vectors and ALM
As another example, the vector ðx1; x2; . . . ; xnÞ might represent the period-by-period
cash flows in a fixed income security such as a bond or a mortgage-backed security
(MBS). Because of the prepayment options a¤orded borrowers in MBS and callable
bonds, there can be significant variability in future cash flow which reflects the evolu-
tion of future interest rates, among other factors. Similarly, even a simple bullet bond
with no call option, where cash flows are, in theory, known with certainty at issue,
may experience variability due to the presence of credit risk and the potential for de-
fault and loss.
At a portfolio level, one might model the cash flow vectors representing the assets
and liabilities of a firm such as a life insurance or property and casualty insurance
company, commercial or investment bank, or pension plan. The liabilities could re-
flect explicit contractual obligations of the firm, or implicit liabilities associated with
100
Chapter 3
Euclidean and Other Spaces

short positions in investment securities or financial derivatives. In any such case, these
cash flows may contain embedded options or credit risks, as well as changes due to
the issuance of new liabilities and portfolio management of assets.
Once so modeled, the firm is in a better position to evaluate its asset–liability man-
agement risk, or ALM risk, which is the residual risk to firm capital caused by any
risks in assets and liabilities that are not naturally o¤setting or otherwise hedged.
Interest rate risk noted in the last section is often a major component of ALM risk.
In each case, one can embed the possible cash flow structures in Rn and begin the
risk analysis and evaluation of hedging strategies with the advantage of the structure
this space a¤ords.
3.3.2
Metrics and Norms
Truthfully, the most prevalent norms and metrics in finance are of lp-type for
p ¼ 1; 2, and y. However, it is no easier to develop the necessary theory for these
three needed cases than it is to develop the general lp theory. So rather than expend
the e¤ort to develop three special cases and leave the reader thinking that these are
isolated and special metrics, this book takes the position that for the given e¤ort, it is
better to understand that p ¼ 1; 2, and y are simply three special points in a contin-
uum of metrics spanning: 1 a p a y.
And who knows, you may discover a natural application in finance of a di¤erent
lp-metric, and you will be ready with all the necessary tools.
One exception to the p ¼ 1; 2, and y rule is for the analysis of sample data.
Sample Statistics
Of the given three common lp-norms, l2 is the most frequently used. As is well known
and will be further developed in the chapter 7 on statistics, the most common mea-
sure of risk in finance is defined in terms of the measure known as variance, and its
square root, standard deviation, and both reflect an l2-type measurement. These are
special cases of what are known as the moments of the sample, and in general, sample
statistics utilize the full range of lp-norms for integer p.
For example, assume that x ¼ ðx1; x2; . . . ; xnÞ represents a ‘‘sample’’ of observa-
tions of a random variable of interest. In finance, a common example would be
observations of sequential period returns of an asset or portfolio of interest. For ex-
ample, the monthly returns of a given common stock, or a benchmark portfolio such
as the S&P 500 Index, would be natural candidates for analysis. Alternatively, these
observations might reflect equally spaced observations of a currency exchange rate,
or interest rate, or price of a given commodity. In any such case, the variable of in-
terest might be the actual observation, or the change in the observed value measured
3.3
Applications to Finance
101

in absolute or relative percentage units. The so-called moments of the sample are all
defined in a way which can be seen to be equivalent to an lp-norm:
1. Moments about the Origin
Mean:
The mean of the sample is defined as
^m ¼ 1
n
X
n
j¼1
xj:
ð3:42Þ
If all observations xj b 0, the sample mean is equivalent to an l1-norm, ^m ¼ 1
n kxk1. In
general, however, this is not true as the ‘‘sign’’ of xj is preserved in the definition of a
mean, but not preserved in the definition of an l1-norm.
Higher Moments:
For r a positive integer, the so-called rth moment of the sample is
defined as
^m0
r ¼ 1
n
X
n
j¼1
xr
j ;
ð3:43Þ
so we see that ^m ¼ ^m0
1. Also, when the observations are nonnegative, or in the general
case where r is an even integer, this moment is related to the lr-norm, and we have
that ^m0
r ¼ 1
n kxkr
r.
Notation:
To distinguish between the moments of the sample and those of the un-
known theoretical distribution of all such data, of which the sample is just a subset,
one sometimes sees the notation of m or x for the sample mean, and m0
r for the
rth sample moment about the origin, with m and m0
r preserved as notation for the
moments of the theoretical distributions. A caret over a variable, such as ^m, is also
standard notation to signify that its value is based on a sample estimate and not the
theoretical distribution.
2. Moments about the Mean
Variance and Standard Deviation:
The ‘‘unbiased’’ variance of the sample is denoted
^s2, and the standard deviation is the positive square root, denoted ^s, where
^s2 ¼
1
n  1
X
n
j¼1
ðxj  ^mÞ2:
ð3:44Þ
In some applications (see chapter 7), ^s2 is defined with a divisor of n rather than
n  1. If we denote by ^m the vector with constant components equal to ^m,
102
Chapter 3
Euclidean and Other Spaces

^m ¼ ð^m; ^m; . . . ; ^mÞ;
the variance is related to the l2-norm, and we have that ^s2 ¼
1
n1 kx  ^mk2
2.
General Moments:
The rth moment about the mean is denoted ^mr and defined by
^mr ¼ 1
n
X
n
j¼1
ðxj  ^mÞr
ð3:45Þ
so that ^s2 ¼ n1
n ^m2. When r is an even integer, we have that ^mr ¼ 1
n kx  ^mkr
r.
Notation:
As noted above, to distinguish between the moments of the sample and
those of the unknown theoretical distribution of all such data, of which the sample
is a subset, one sometimes sees the notation of s2 for the variance, and s for the stan-
dard deviation. There is no standard notation for the rth moment about the mean,
although analogous to the notational comment above, mr would be a logical choice.
Constrained Optimization
It turns out that many mathematical problems in finance, especially those related to
optimizing an objective function given certain constraints, are more easily solvable
within an l2-type measurement framework for reasons related to the tools of multi-
variate calculus, although these constraints may in fact be more accurately repre-
sented in terms of other norms.
Optimization with an l1-Norm
An example of an l1-norm occurs within a trading
model. Assume that we have a portfolio within which we are trying to change some
portfolio attribute through a trade. Typically there are infinitely many trades that
can provide the desired objective. What is clear is that trading can be expensive due
to the presence of bid–ask spreads as well as other direct costs. If one evaluates the
portfolio value after a trade represented by the n-tuple x ¼ ðx1; x2; . . . ; xnÞ, whereby
xi > 0 implies a purchase, and xi < 0 a sale of a dollar amount of jxij of the ith asset
and P xi ¼ 0, the portfolio value after the trade can be represented as
Pðx1; x2; . . . ; xnÞ ¼ P  e
X
jxij:
Here e denotes the average cost per currency unit of trading, and P the current port-
folio market value.
Consequently one problem to be solved can be stated:
Of all ðx1; x2; . . . ; xnÞ that achieve portfolio objectives,
Minimize:
X
jxij ¼ kxk1.
3.3
Applications to Finance
103

Typically the condition of achieving portfolio objectives can also be expressed in
terms of an equation involving the terms ðx1; x2; . . . ; xnÞ. For example, if b denotes
the current portfolio beta value, and b0 the desired value, the constraint on traded
assets to achieve the target could be expressed as
b þ
P xibi
P
¼ b0;
ð3:46Þ
where bi denotes the beta of the ith asset traded.
Summarizing, we see that this trading problem becomes one of finding a solution
of this equation with minimal l1-norm. That is, rewriting objectives results in
Minimize:
kxk1
given
ðx; bÞ ¼ Pðb0  bÞ;
ð3:47Þ
X
xi ¼ 0:
Here b denotes the vector of tradable asset betas, and we used inner product notation
ðx; bÞ ¼ P xibi. This is an example of a constrained optimization in that we are opti-
mizing, and in this case minimizing, the l1-norm with the constraint that the solution
satisfies two given equations.
We can envision the problem in (3.47) geometrically. Of the set of all x that satisfy
the given constraints, find the value that is closest to the origin in terms of the l1-
norm.
Optimization with an lT-Norm
An example of the same type but with an ly-norm
occurs when one is trying to control the total amount of any asset traded. Such a
constraint may occur because of illiquid markets and the desire to avoid a trade
that moves prices, or because one has an investment policy constraint on the concen-
tration in any given asset. In the simplest form, where all traded assets have the same
limitation, the objective would be one of finding a solution to equation (3.46) with
ly-norm bounded by this common limit: kðx1; x2; . . . ; xnÞky a L.
More realistically, one is generally not so much interested in limiting the maximum
trade as the maximum portfolio exposure post-trade. Consequently one would
instead look for solutions to equation (3.46) with the limit: kðp1; p2; . . . ; pnÞ þ
ðx1; x2; . . . ; xnÞky a L, where xi is the amount of each trade, and pi the initial port-
folio exposure. Since there are potentially many such solutions, an optimization is
still possible, and the problem becomes
104
Chapter 3
Euclidean and Other Spaces

Minimize:
kxk1
given
ðx; bÞ ¼ ðb 0  bÞP;
X
xi ¼ 0;
ð3:48Þ
kp þ xky a L;
where p ¼ ðp1; p2; . . . ; pnÞ.
Optimization with an l2-Norm
Although in both types of problems above the use of
l1-norms and ly-norms is more natural, one might actually solve the problem using
an l2-norm instead. The reason relates to the tools of multivariate calculus and is one
of mathematical tractability. That is, explicit solutions to such problems with an l2-
norm can often be derived analytically, whereas with other norms one must typically
utilize numerical procedures. Obviously, given the prevalence and power of com-
puters today, one could hardly imagine that obtaining an explicit mathematical ex-
pression, rather than a numerical solution, would be worth much. However, the
popularity of l2-norm methods was certified long before the ‘‘computer age,’’ and still
has merit.
The advantage of representing the solution as an explicit mathematical expression
is that the functional relationship between the problem’s inputs and the output solu-
tion is explicitly represented in a form that allows further analysis. For example, one
can easily perform a sensitivity analysis that quantifies the dependence of the solution
on changes to various constraints, and the addition of constraints. Such analyses are
also possible with numerical solutions, but they require the development of solutions
over a ‘‘grid’’ of input assumptions from which sensitivities can be estimated.
Tractability of the lp-Norms: An Optimization Example
A simple example of the mathematical tractability of l2-norms is as follows: Assume
we are given a collection of data points fxign
i¼1, which we may envision either as dis-
tributed on the real line R or as a point x ¼ ðx1; x2; . . . ; xnÞ in Rn. The goal is to find
a single number ap that best approximates these points in the lp-norm, where p b 1.
That is,
Find ap so that kðx1  ap; x2  ap; . . . ; xn  apÞkp is minimized.
Assume that for notational simplicity that we have arranged the data points in
increasing order: x1 a x2 a    a xn. This problem can be envisioned as a problem
in R, such as for p < y,
3.3
Applications to Finance
105

Minimize:
f ðaÞ ¼
X
n
i¼1
jxi  ajp
 
!1=p
;
ð3:49Þ
or as a problem in Rn, for any p,
Minimize:
f ðaÞ ¼ kx  akp;
ð3:50Þ
where x 1 ðx1; x2; . . . ; xnÞ and a 1 ða; a; . . . ; aÞ is a point on the ‘‘diagonal’’ in Rn.
Geometrically, for the problem statement in Rn, we seek the smallest lp-ball cen-
tered on x, Bp
r ðxÞ, that intersects this diagonal. The point or points of intersection
are then the values of ap that minimize f ðaÞ, and the ‘‘radius’’ of this minimal ball
is the value of f ðapÞ.
In either setting, minimizing the stated functions, or their pth powers to eliminate
the pth-root, are equivalent, since p b 1 and hence gðyÞ ¼ yp is an increasing func-
tion on ½0; yÞ. Consequently, if y 1 f ðaÞ and y0 1 f ða0Þ, then y a y0 if and only if
gðyÞ a gðy0Þ.
What is easily demonstrated is that any solution must satisfy x1 a a a xn. For ex-
ample, if a > xn,
f ðaÞp ¼
X
jxi  ajp ¼
X
ða  xiÞp;
which is an increasing function on ½xn; yÞ, so we must have a a xn. Similarly,
for a < x1, we have that f ðaÞp ¼ Pðxi  aÞp which is a decreasing function on
ðy; x1, and so a b x1.
The analytical solution of this general problem is somewhat di‰cult and with three
exceptions requires the tools of calculus from chapter 9. In fact, at this point, it is not
even obvious that in the general case a solution exists, or if it does, that it is unique.
However, in the special cases of p ¼ 1; 2, and y, this problem can be solved with
elementary methods, and this is easiest when p ¼ 2, which we address first. In chap-
ter 9, the other cases will be addressed.
l2-Solution
Given the points fxign
i¼1, define the simple average consistently with the
sample mean in (3.42):
x ¼ 1
n
X
xi:
By writing,
xi  a ¼ ðxi  xÞ þ ðx  aÞ;
106
Chapter 3
Euclidean and Other Spaces

a simple algebraic calculation leads to
f ðaÞ 1
X
ðxi  aÞ2 ¼
X
ðxi  xÞ2 þ nðx  aÞ2;
where f ðaÞ denotes now the l2-norm squared. So it is clear that a2 ¼ x gives the l2-
norm minimizing point, since then nðx  aÞ2 ¼ 0.
In other words, the sample mean of a collection of points minimizes the l2-norm in
the sense of (3.49). Since this l2-norm is related to the sample variance in (3.44), this
result can be restated. Considering ^m in the definition of sample variance as undefined
for a moment, the analysis above implies that the value of the sample variance is
minimized when ^m equals the sample mean, which it does.
l1-Solution
The case of p ¼ 1 is more di‰cult but still tractable. Because x1 a
x2 a    a xn, we can relabel these to be distinct points y1 < y2 <    < ym. Now,
letting ni denote the number of occurrences of yi, so that Pm
i¼1 ni ¼ n, we write
f ðaÞ 1
X
jxi  aj ¼
X
nijyi  aj:
We know that if yj a a a yjþ1, then jyi  aj ¼ yi  a for i b j þ 1, and jyi  aj ¼
a  yi for i a j. Consequently
f ðaÞ ¼ cj 
n  2
X
j
i¼1
ni
 
!
a;
where cj is a constant in each interval, and specifically, cj ¼ Pn
i¼jþ1 niyi  P j
i¼1 niyi.
So the graph of f ðaÞ is linear between any consecutive distinct points, is decreasing if
n  2 P j
i¼1 ni > 0, is increasing if n  2 P j
i¼1 ni < 0, and is constant if n  2 P j
i¼1 ni
¼ 0. We can therefore conclude:
1. If n ¼ 2m þ 1 is odd, then there is no value of j for which n  2 P j
i¼1 ni ¼ 0, and
hence there is a unique value of j with n  2 P j
i¼1 ni > 0 and n  2 P jþ1
i¼1 ni < 0.
Consequently a1 ¼ xjþ1 is the l1-norm minimizing point, since f ðaÞ is decreasing
when a < xjþ1 and increasing when a > xjþ1. When all ni ¼ 1, then a1 ¼ xmþ1.
2. If n ¼ 2m, then the solution will be unique if there is no value of j for which
n  2 P j
i¼1 ni ¼ 0, and in this case the value of a1 is calculated as above. However,
if there is a value of j for which n  2 P j
i¼1 ni ¼ 0, then any a1 with yj a a1 a yjþ1
will gives the same value for f ða1Þ, namely cj, so the solution will not be unique.
When all ni ¼ 1, then the solution is never unique, and any a1 with xm a a1 a xmþ1
is a solution.
3.3
Applications to Finance
107

As a simple graphical illustration of non-uniqueness in the even case when all
ni ¼ 1, let x1 ¼ 5, and x2 ¼ 15. The graph of f ðaÞ as a function on R is seen in
figure 3.4.
Considered as a problem of in R2, the minimal l1-Ball centered on ð5; 15Þ that
intersects the diagonal in R2 is presented in figure 3.5. As can be seen, this minimal
l1-ball intersects the diagonal line over the same range of x-values that minimize the
function in figure 3.4.
Remark 3.45
The earlier l1-norm trading problem is similar to this problem. How-
ever, the ‘‘admissible’’ set of solutions there is not defined as the Rn diagonal, unless
we wish to trade the same amount in all assets, an unlikely scenario. The admissible
set is instead the collection of points that satisfy the beta-constraint in (3.46). In addi-
tion, rather than look for the point on the admissible set that is ‘‘closest’’ to some initial
point x ¼ ðx1; x2; . . . ; xnÞ, we seek the trading point on the admissible set that is closest
to 0 ¼ ð0; 0; . . . ; 0Þ in the l1-norm.
lT-Solution
The case p ¼ y is considered next, and in this special example the so-
lution is immediate, though often this is not the case. Here the goal is to determine a
that minimizes
f ðaÞ ¼ maxfjxi  ajg;
Figure 3.4
f ðaÞ ¼ j5  aj þ j15  aj
108
Chapter 3
Euclidean and Other Spaces

and this is easily seen to be a ¼ ðxn  x1Þ=2, the midpoint of the interval x1 a x a xn.
This is because the ly-norm must be attained at one of the end points, so to minimize
this distance, the interval midpoint is optimal.
General lp-Solution
In general, framing this lp-norm problem as a problem in R or
Rn are identical problems, but the intuitive framework di¤ers between the two Eucli-
dean settings. The geometry and intuition in R can be exemplified by a simple graph.
Here we illustrate the problem with xi values of 5, and 15, and p ¼ 3 in figure 3.6.
The function we aim to minimize is graphed in a bold line, and equals the cube of
the l3-norm. This function is seen to equal the sum of the two component functions
defined as fiðaÞ ¼ jxi  aj3, graphed in light lines. Clearly, the minimum appears to
be at a ¼ 5, and this is easily confirmed. Letting a ¼ 5 þ b, and assuming b < 10
say to make the absolute value unambiguous, we get that f ðaÞ ¼ 2000 þ 60b2, which
is minimized when b ¼ 0.
In R2 this problem can be written as one of minimizing the cube of the l3-norm
between ð5; 15Þ and ða; aÞ:
Minimize:
kð5; 15Þ  ða; aÞk3
3:
Geometrically, we are looking for a point on the diagonal of R2: fðx; yÞ j x ¼ yg that
is closest to the point ð5; 15Þ in the l3-norm. Intuitively, we imagine l3-balls centered
Figure 3.5
jx  5j þ jy þ 15j ¼ 20
3.3
Applications to Finance
109

on ð5; 15Þ of various radius values, and seek the smallest one that intersects this di-
agonal. Graphically, the solution is seen in figure 3.7. If the radius of this ball is less
than
ffiffiffiffiffiffiffiffiffiffi
2000
3p
A12:6, there is no intersection, while if is greater, there are two points of
intersection.
Without more powerful tools, however, we are not able to confirm that such prob-
lems have solutions for general p and n, nor if they do, if and when such solutions
are unique. Even if a solution is known to be unique, there may be no ‘‘closed-form
solution’’ to the problem whereby the value of ap can be expressed as an explicit
function of p and the initial collection fxig.
In the cases p ¼ 1; 2, and y, it was shown that the solution of the problems in
(3.49) and (3.50) were always uniquely and explicitly solvable, except in the case
where p ¼ 1 and n is even, where although explicitly solvable, there could be infi-
nitely many solutions.
General Optimization Framework
Optimization problems are everywhere in finance, and they usually take the follow-
ing form:
Problem 3.46
Of all values of x ¼ ðx1; x2; . . . ; xnÞ that satisfy
f ðxÞ ¼ c;
find the value that optimizes (i.e., minimizes or maximizes)
Figure 3.6
f ðaÞ ¼ j5  aj3 þ j15  aj3
110
Chapter 3
Euclidean and Other Spaces

kx  akp;
where c is a constant, and a is a point, perhaps 0, and p is typically 1, 2, or y.
In the more general case, the norm minimization is replaced:
Problem 3.47
Of all values of x ¼ ðx1; x2; . . . ; xnÞ that satisfy
f ðxÞ ¼ c;
find the value that optimizes (i.e., minimizes or maximizes)
gðxÞ;
where gðxÞ is a given function.
Note that in both cases the problem is known as a constrained optimization and is
defined by:
 One or more constraint functions: The function that provides constraints on the
solution.
 An objective function: The function that is to be optimized.
Depending on the application, one or both of these functions may reflect one or more
lp-norms, as well as a variety of other financial functions of interest.
Figure 3.7
jx  5j3 þ jy þ 15j3 ¼ 2000
3.3
Applications to Finance
111

Exercises
Practice Exercises
1. Calculate the lp-norms of the following vectors in Rn, for p ¼ 1; 2; 5, and y and a
a positive real number:
(a) a ¼ ðGa;Ga; . . . ;GaÞ
(b) a ¼ ðGa; 0; 0; . . . ; 0Þ
(c) a ¼ ða1; a2; . . . ; anÞ where one aj ¼Ga, all others are 0.
2. Calculate the inner product of the following pairs of vectors and confirm Ho¨lder’s
inequality in (3.16) (which is the Cauchy–Schwarz inequality for p ¼ 2Þ for p ¼ 1; 2;
5; 10, and y:
(a) x ¼ ð5; 3Þ and y ¼ ð2; 8Þ
(b) x ¼ ð1; 2; 3Þ and y ¼ ð1; 1; 20Þ
(c) x ¼ ð2; 12; 3; 3Þ and y ¼ ð10; 3; 2; 0Þ
(d) x ¼ ð3; 3; 5; 10; 1Þ and y ¼ ð2; 5; 10; 20; 1Þ
3. For the vector pairs in exercise 2, verify the Minkowski inequality in (3.17) for
p ¼ 1; 2; 5; 10, and y.
4. For the vector pairs in exercise 2:
(a) Calculate the lp-distances for p ¼ 1; 2; 5; 10, and y.
(b) Demonstrate explicitly that for each pair of vectors, the lp-distance gets closer to
the ly-distance as p increases without bound. (Hint: Recall remark 3.25 following
the proof of the Minkowski inequality.)
5. Develop graphs of the lp-balls in R2, Bp
r ð0Þ, for p ¼ 1; 2, and y, and r-values
r ¼ 0:10; 0:5 and 1. Evaluate the relationship between the di¤erent balls for various
r by comparing l1- and l2-balls, then l2- and ly-balls.
(a) Demonstrate the equivalence of the l1- and l2-norms by showing how one can
choose the associated r-values to verify (3.35).
(b) Demonstrate the equivalence of the l2- and ly-norms by showing how one can
choose the associated r-values to verify (3.35).
6. Show that if ðx; yÞ is an inner product on a real vector space X, all the properties
of a norm are satisfied by jxj as defined by (3.5), and hence the terminology ‘‘norm
associated with this inner product’’ is justified.
7. If x and y are two vectors in Rn, n ¼ 2; 3 and z 1 y  x:
112
Chapter 3
Euclidean and Other Spaces

(a) Demonstrate kzk2
2 ¼ kxk2
2 þ kyk2
2  2x  y. (Hint: Use (3.5) and properties of
inner products.)
(b) Show that if y < p denotes the angle between x and y, then
cos y ¼
x  y
kxk2kyk2
:
ð3:51Þ
(Hint: the law of cosines from trigonometry states that
c2 ¼ a2 þ b2  2ab cos y;
ð3:52Þ
where a, b, c are the sides of a triangle, and y is the radian measure of the angle be-
tween sides a and b. Now create a triangle with sides x, y, and z.)
(c) Show that if y < p denotes the angle between x and y, then x  y ¼ 0 i¤ y ¼ 90,
so x and y are ‘‘perpendicular.’’ (Note: The usual terminology is that x and y are
orthogonal, and this is often denoted x ? y.)
Remark 3.48
Note that for n > 3, the formula in (3.51) is taken as the definition of
the cosine of the angle between x and y, and logically represents the true angle between
these vectors in the two-dimensional plane in Rn that contain them. As was noted in the
section on inner products, the derivations in (a) and (b) remain true for a general inner
product and associated norm, and hence the notion of ‘‘orthogonality’’ can be defined in
this general context.
8. Show that if fxjgn
j¼1 is a collection of mutually orthogonal, unit vectors in Rn,
namely xj  xk ¼ 0 for j 0 k, and jxjj2 ¼ xj  xj ¼ 1 for all j, then for a vector y A Rn
that can be expressed as a linear combination of these vectors
y ¼
X
n
j¼1
ajxj;
ð3:53Þ
the constants aj must satisfy aj ¼ xj  y. (Hint: Consider an inner product of each side
with xj.)
Remark 3.49
The usual terminology is that the collection of vectors, fxjgn
j¼1, are
orthonormal. With the tools of linear algebra, it can be shown that all vectors y A Rn
can be represented as in (3.53).
9. Given a vector of sample data: x ¼ ðx1; x2; . . . ; xnÞ, demonstrate that ^s2 ¼
^m0
2  ^m2, where here ^s2 is defined with n rather than n  1.
Exercises
113

10. Given semiannual coupon bond data with prices expressed per 100 par:
Term
0.5 years
1.0 years
1.5 years
2.0 years
Coupon
2.0%
2.2%
2.6%
3.0%
Price
99.5
100.0
100.5
101.0
(a) Bootstrap this data to determine semiannual market spot rates for 0.5, 1.0, 1.5,
and 2.0 years.
(b) What is the semiannual forward rate between 0.5 and 1.5 years?
11. Demonstrate that the forward rate in exercise 10(b) can be realized by an inves-
tor desiring to invest $1 million between time 0.5 and 1.5 years, by constructing an
appropriate portfolio of long and short zero coupon bonds. Assume that these zeros
are trading with the spot rates from 10(a).
12. Given a portfolio of three stocks with market values in $millions of 350, 150, and
500, and respective betas of 1.0, 0.9, and 1:1:
(a) Calculate the beta of the portfolio, where b ¼ P xibi= P xi and xi denotes the
amount invested in stock i.
(b) Find the trade in R3 that changes the portfolio beta to 1:08 that has the lowest
transaction fee, assuming that this fee is proportional to the market value bought and
sold, and that all final positions must be long. (Hint: See (3.47), but note that while
the constraint P xi ¼ 0 allows you to analytically consider this a problem in R2, be-
cause x3 ¼ x1  x2, the norm minimization in R2 will not work in general.)
(c) Repeat part (b) but now with a beta target of 0:935, and where final positions can
be long or short.
(d) Achieve the same objective in part (c), but adding the constraint that the invest-
ment policy maximum for any stock is 600 on a long or short basis.
Assignment Exercises
13. Calculate the inner product of the following pairs of vectors, and confirm Ho¨ld-
er’s inequality in (3.16) (which is the Cauchy–Schwarz inequality for p ¼ 2) for
p ¼ 1; 2; 5; 10, and y:
(a) x ¼ ð11; 133Þ and y ¼ ð12; 28Þ
(b) x ¼ ð10; 2; 13Þ and y ¼ ð10; 101; 30Þ
(c) x ¼ ð1; 24; 3; 13Þ and y ¼ ð1; 23; 21; 10Þ
(d) x ¼ ð10; 53; 53; 10; 21Þ and y ¼ ð1; 15; 10; 25; 11Þ
114
Chapter 3
Euclidean and Other Spaces

14. For the vector pairs in exercise 13, verify the Minkowski inequality in (3.17) for
p ¼ 1; 2; 5; 10, and y.
15. For the vector pairs in exercise 13:
(a) Calculate the lp-distances for p ¼ 1; 2; 5; 10, and y.
(b) Demonstrate explicitly that for each pair of vectors, the lp-distance gets closer to
the ly-distance as p increases without bound (Hint: Recall remark 3.25 following the
proof of the Minkowski inequality.)
16. Develop a graph of the lp-balls in R2, Bp
r ð0Þ, for p ¼ 1; 5, and y, and r-values
r ¼ 0:10, 0:5, and 1. Evaluate the relationship between the di¤erent balls for various
r by comparing l1- and l5-balls, then l5- and ly-balls.
(a) Demonstrate the equivalence of the l1- and l5-norms by showing how one can
choose the associated r-values to verify (3.35).
(b) Demonstrate the equivalence of the l5- and ly-norms by showing how one can
choose the associated r-values to verify (3.35).
17. For fixed a; b > 0, say a ¼ 3, b ¼ 5, develop a graph of the function for
1 < p < y:
f ðpÞ ¼ ap
p þ bq
q ;
where q ¼
p
p1 is conjugate to p. Confirm Young’s inequality that ab a f ðpÞ for all
p. What happens if a ¼ b?
18. Not all metrics are equivalent to the lp-metrics. Show that
dðx; yÞ ¼
0;
x ¼ y
1;
x 0 y

;
is a metric on Rn that is not equivalent to the lp-metrics.
19. Given a portfolio of 100; 000 par of 6% semiannual (s.a.) coupon, 10-year bonds, and
250,000 par of 4:5% s.a. coupon, 3-year bonds, let ði; jÞ A R2 denote the market yield
vector,whereiisthes.a.yieldforthe3-yearbond,and j thes.a.yieldforthe10-yearbond.
(a) Develop the formula for the portfolio price function, Pði; jÞ, using (2.15) or an
equivalent formulation, and calculate the initial portfolio market value assuming
that ði0; j0Þ ¼ ð0:04; 0:055Þ.
(b) Assume that the initial yield vector shifts, ði0; j0Þ ! ði; jÞ, where ði; jÞ ¼ ði0 þ Di;
j0 þ DjÞ. Consider only shifts, ðDi; D jÞ, that have the same lp-norm as the shift vector
ð0:01; 0:01Þ for p ¼ 1; 2; y. Show by examples that the portfolio gain/loss Pði0 þ Di;
j0 þ DjÞ  Pði0; j0Þ is not constant in any of these norms. (Hint: Consider shifts
Exercises
115

on the lp-balls in R2, Bp
r ð0:04; 0:055Þ where r ¼ kð0:01; 0:01Þkp. Try shift vectors,
ðDi; D jÞ where Di ¼GDj, or where one or the other is 0, to get started.)
(c) For each p-value, estimate numerically the yield shift vectors that provide the
largest portfolio gain and loss.
20. For the portfolio in exercise 19, implement a market-value neutral trade at the
initial yields, selling 75,000 par of the 10-year and purchasing an equivalent dollar
amount of the 3-year bonds.
(a) Express this trade as a vector-shift in R20, where the initial vector C0 is the orig-
inal cash flow vector, and C the vector after the trade.
(b) Repeat exercise 19(b) and 19(c) for the traded portfolio, comparing results.
21. Given semiannual coupon bond data with prices expressed per 100 par:
Term
0.5 years
1.0 years
1.5 years
2.0 years
Coupon
3.0%
2.8%
2.4%
2.0%
Price
100.0
100.5
101.0
101.5
(a) Bootstrap this data to determine semiannual market spot rates for 0.5, 1.0, 1.5,
and 2.0 years.
(b) What is the semiannual forward rate between 1.0 and 2.0 years?
22. Demonstrate that the forward rate in exercise 21(b) can be realized by an inves-
tor desiring to borrow $100 million between time 1.0 and 2.0 years, by constructing
an appropriate portfolio of long and short zero coupon bonds. Assume that these
zeros are trading with the spot rates from 21(a).
23. Given a portfolio of 3 bonds with market values in $millions of: 200, 450, and
350, and respective durations of 3.5, 5.0, and 8:5.
(a) Calculate the duration of the portfolio, where D ¼ P xiDi= P xi and xi denotes
the amount invested in bond i.
(b) Find the trade in R3 that changes the portfolio duration to 4:0 that has the low-
est transaction fee, assuming that this fee is proportional to the market value bought
and sold, and that all final positions must be long. (Hint: See (3.47), but note that
while the constraint P xi ¼ 0 allows you to analytically consider this a problem in
R2, because x3 ¼ x1  x2, the norm minimization in R2 will not work in general.)
(c) Repeat part (b) but now with a duration target of 6:5, and where final positions
can be long or short.
(d) Achieve the same objective in part (c), but adding the constraint that the invest-
ment policy maximum for any bond is 462 on a long or short basis.
116
Chapter 3
Euclidean and Other Spaces


## Set Theory and Topology

4 Set Theory and Topology
4.1
Set Theory
4.1.1
Historical Background
In this section we formalize the notion of sets and their most common operations.
Ironically, the definition of a ‘‘set’’ is more complex than it first appears. Before the
early 1900s, a set was generally accepted as being definable as any collection of
objects that satisfy a given property,
X ¼ fa j a satisfies property Pg;
and an axiomatic structure was developed around this basic concept. This approach
has come to be known perhaps unfairly as naive set theory, despite the fact that it was
developed within a formal axiomatic framework.
In 1903 Bertrand Russell (1872–1970) published a paradox he discovered in 1901,
which has come to be known as Russell’s paradox, by proposing as a ‘‘set’’ the
following:
X ¼ fR j R is a set; and R B Rg:
In other words, X is the ‘‘set’’ of all sets which are not a member of themselves.
The paradox occurs in attempting to answer the question
Is X A X?
If X A X, then by the defining property above it is a set that is not an element of it-
self. However, if we posit that X B X, then again by definition, X should be one of
the sets R that are included in X. In summary,
X A X
i¤
X B X:
This is a situation that gives mathematicians great anxiety and rightfully so! What
is causing this unexpected result? Are there others? Could such paradoxes be avoided?
How? Defining a set as a ‘‘collection satisfying a property’’ certainly works fine most
of the time, but apparently not this time.
What was needed was an even more careful and formal articulation of the axioms
of set theory and the fundamental properties that would be assumed. With this,
mathematicians would be able to develop a theory that was, on the one hand, ‘‘famil-
iar,’’ but on the other, paradox free. This approach has come to be known as axiom-
atic set theory.
A number of axiomatic approaches have been developed. The first approach was
introduced by Ernst Zermelo (1871–1953) in 1908, called the Zermelo axioms, and

produced Zermelo set theory. This axiomatic structure was later improved upon by
Adolf Fraenkel (1891–1965) in 1922, and produced the Zermelo–Fraenkel axioms,
and the Zermelo–Fraenkel set theory, or ZF set theory. This is the approach largely
used to this day.
In essence, sets are defined as those collections that can be constructed based on
the 10 or so ZF axioms, and the paradox above is resolved because it is not possible
to construct the Russell collection X as a set within this axiomatic structure. It is also
not possible to construct the set of all sets, which underlies another paradox. How-
ever, these axioms have been shown to be adequate to construct virtually all of the
types of sets one needs in mathematics, and that for these sets, set manipulations
can proceed just as if these sets were defined via naive set theory, as collections of
objects which satisfy given criteria.
*4.1.2
Overview of Axiomatic Set Theory
To give a flavor for the axiomatic structure of set theory, we introduce the Zermelo–
Fraenkel axioms, including the so-called axiom of choice, which collectively produce
what is referred to as ZFC set theory. This structure is presented below in a simplified
framework that omits many of the quantifiers necessary to make statements formal,
and is presented in both plain and informal English and approximately formal sym-
bolic language.
In this structure it will be noted that the intuitive notions of ‘‘set’’ and ‘‘element’’
are formalized as relative terms, not absolute terms. A set may be an element of an-
other set, and an element of a set may itself be a set that contains elements. In addi-
tion the expression PðxÞ will denote a statement that may be true or false for any
given set x, and PðXÞ will denote that the statement is true for a given set X. For
example, if
PðxÞ : x contains an integer as an element,
then PðNÞ. Also Pðx; yÞ will denote a conditional statement in that given a set x,
there is a unique set y so that Pðx; yÞ is true, and then PðX; YÞ denotes that the
statement is true for X, Y. For example,
Pðx; yÞ : y contains the elements of x plus the integers as elements.
Finally, we recall the logical symbols: E (for all), b (there exists), @ (not), C: (such
that),4(or),5(and), ) (implies), and , (if and only if ).
1. Formal Symbols:
j; A; f; g; X; Y; Z; . . . .
2. Axioms
118
Chapter 4
Set Theory and Topology

 ZF1 (Extensionality):
Two sets are equal means they contain the same elements,
X ¼ Y , ðZ A X , Z A YÞ:
 ZF2 (Empty Set):
There exists a set with no elements,
bj ¼ f g:
 ZF3 (Pairing):
Given any two sets, there exists a set that contains these as
elements,
X; Y ) bZ ¼ fX; Yg:
 ZF4 (Union):
Given two sets, there exists a set that contains as elements exactly
the elements of the original sets,
X; Y ) bZ C: W A Z , W A X4W A Y:
 ZF5 (Infinity):
There exists a set with an infinite number of elements, in that it
contains the empty set as an element, and for any element Y that it contains, it also
contains the element fY; fYgg,
bX C: j A X5ðY A X ) fY; fYgg A XÞ:
 ZF6 (Subset):
Given any set and any statement, there is a set that contains all the
elements of the original set for which the statement is true,
X; PðxÞ ) bY C: Z A Y , Z A X5PðZÞ:
 ZF7 (Replacement):
Given any set and conditional statement, there is a set that
contains as elements the unique sets associated with the elements of the original set
as defined by the conditional statement,
X; Pðx; yÞ ) bY C: Z A Y , bW A X5PðW; ZÞ:
 ZF8 (Power Set):
For any set, there is a set that contains as elements any set that
contains elements of the original set. In other words, this new set, called the power
set, contains all the ‘‘subsets’’ of the original set,
X ) bY C: Z A Y , ðW A Z ) W A XÞ:
 ZF9 (Regularity):
Any set that is not empty contains an element that has no ele-
ments in common with the original set,
X 0 j ) bY C: Y A X5@bWðW A X5W A YÞ;
where @b is shorthand for ‘‘there does not exist.’’
4.1
Set Theory
119

 ZF10 (Axiom of Choice):
For any set, there is a set that contains as elements an
element from each nonempty element of the original set,
X ) bY C: EZ A XðZ 0 jÞbW A Y5W A Z:
These axioms fall into four categories.
1. Axiom 1 introduces the notion of equality of ‘‘sets,’’ and indirectly provides a
context for the undefined term A. Although the notion of subset is not explicitly
defined, we see that this is implicitly referenced in axiom 8, which suggests that the
condition on Z is one of ‘‘subset’’:
Z H X , ðW A Z ) W A XÞ:
2. Axioms 2 and 5 are existence axioms, on the one hand, declaring the existence
of an empty set and, on the other, the existence of a set with an infinite number of
elements.
3. All the other axioms except axiom 9 identify how one can make new sets from old
sets, or from sets and statements. For example, axiom 3 states that a set can be
formed to include as members two other sets, while axiom 4 states that the union of
sets is a set. Axioms 6 and 7 state that sets can be formed from sets and statements. A
simple application of axiom 6 is that the intersection of X and Y must be a set since
we can use the statement: PðZÞ : ðZ A YÞ. Axiom 8 introduces the power set, or the
set of all subsets of a given set, and axiom 10 states that there is a set that contains
one element from every nonempty element of a given set. In other words, from the
elements of X, we can form a set which ‘‘chooses’’ one element from each such ele-
ment, and hence the name, ‘‘axiom of choice.’’
4. Finally, axiom 9 puts a limit on what a set can be, and can be shown to preclude
the ‘‘set of all sets’’ from being a set in this theory. It states that any nonempty set
contains an element that is disjoint from the original set.
In what follows, we will treat sets as if definable as collections of objects that sat-
isfy certain statements or formulaic properties, and this can generally be justified by
axiom 6. More specifically, the ZFC set theory states that defining a set as a collec-
tion of objects that satisfy certain properties will avoid paradoxes if the original col-
lection of objects is itself a set or a subcollection of a set. That is, if A is a set,
fx j x A A and PðxÞg;
is a set for any ‘‘statement’’ P, by axiom 6. However, although beyond the scope of
this introduction to set theory, one needs to be careful as to exactly what kinds of
120
Chapter 4
Set Theory and Topology

‘‘statements’’ are appropriate in this axiom, as it can be shown that for a general
property P, paradoxes are still possible.
4.1.3
Basic Set Operations
As a collection of objects, and with the axiomatic structure in the background, we
distinguish between the notions: ‘‘element of,’’ ‘‘subset of,’’ and ‘‘equal to’’:
1. Membership:
‘‘x is an element of A,’’ denoted x A A, is only defined indirectly in
the axioms, but understanding this notion in terms of the heuristic
A 1 fx j x A Ag
is consistent with the axioms and operationally e‰cient.
2. Subset:
‘‘B is a subset of A,’’ denoted B H A, and defined by x A B ) x A A.
3. Equality:
‘‘B equals A,’’ denoted A ¼ B, and defined by B H A and A H B.
Given sets A and B, the basic set operations are:
1. Union:
A U B ¼ fx j x A A and=or x A Bg.
2. Intersection:
A V B ¼ fx j x A A and x A Bg.
3. Complement:
~
A ¼ fx j x B Ag. Ac is an alternative notation, especially if A is a
complicated expression. Note that ~~
A~
A ¼ A.
4. Di¤erence:
A @ B ¼ fx j x A A and x B Bg. Note that A @ B ¼ A V ~B.
Union and intersection are similarly defined for any indexed collection of sets:
fAa j a A Ig, where I denotes any indexing set which may be finite, or denumerably
or uncountably infinite (recall chapter 2):
6
a
Aa ¼ fx j x A Aa for some a A Ig;
7
a
Aa ¼ fx j x A Aa for all a A Ig:
It is straightforward to justify the so-called De Morgan’s laws, named after Augus-
tus De Morgan (1806–1871), who formalized a system of ‘‘relational algebra’’ in
1860. Examples are:
1.
g
6a Aa
6a Aa ¼ 7a f
Aa
Aa.
2.
g
7a Aa
7a Aa ¼ 6a f
Aa
Aa.
4.1
Set Theory
121

3. B V ½6a Aa ¼ 6a½Aa V B.
4. B U ½7a Aa ¼ 7a½Aa U B.
To demonstrate the first example in detail, we use the definitions above:
x A g
6
a
Aa
6
a
Aa
, x B 6
a
Aa
, x B Aa
for all a
, x A f
Aa
Aa
for all a
, x A 7
a
f
Aa
Aa:
4.2
Open, Closed, and Other Sets
4.2.1
Open and Closed Subsets of R
The reader is undoubtedly familiar with the notion of an interval in R, as well as
the various types of intervals. First o¤, an interval is a subset of R that has ‘‘no
holes.’’
Definition 4.1
An interval I is a subset of R that has the property:
If x; y A I, then for all z : x a z a y we have that z A I.
There are four types of intervals, as we list next. Interval notation is universal.
1. Open:
ða; bÞ ¼ fx j a < x < bg.
2. Closed:
½a; b ¼ fx j a a x a bg.
3. Semi-open or Semi-closed:
ða; b and ½a; bÞ.
In some applications, where it is unimportant if the interval contains its endpoints,
the ‘‘generic interval’’ will be denoted: ha; bi, meaning that it can be any of the four
examples above without consequence in the given statement.
Any of these interval types may be bounded—meaning that y < a; b < y—and
that all but the closed interval may be unbounded. For example,
ða; yÞ;
ðy; bÞ;
ðy; yÞ;
ðy; b;
½a; yÞ:
122
Chapter 4
Set Theory and Topology

Each of these characteristics of an interval: open, closed, bounded, and unbounded,
can be generalized, and each is important in mathematics for reasons that will
emerge over coming chapters. The notions of open and closed subsets of R are gen-
eralized next.
Definition 4.2
Given x A R, a neighborhood of x of radius r, or open ball about x of
radius r, denoted BrðxÞ, is defined as
BrðxÞ ¼ fy A R j jx  yj < rg:
ð4:1Þ
A subset G H R is open if given x A G, there is an r > 0 so that BrðxÞ H G. A subset
F H R is closed if the complement of F, ~F, is open.
Intuitively, an open set only contains ‘‘interior’’ points, in that every point can be
surrounded by an open ball that fits entirely inside the set. In contrast, a closed set
will contain at least one point that is not interior to the set. In other words, no matter
how small an open ball one constructs that contains this point, this ball will always
contain points outside the set. But while, by definition, the existence of such a point
is ensured for a closed set, the existence of such a point does not ensure that the set is
closed, and hence the need to define closed in terms of the complement of the set be-
ing open. The problem is that a set can be neither open nor closed.
A useful exercise is to think through how an interval like ð1; 1Þ is open by this
definition, whereas the interval ½1; 1 is closed. On the other hand, the interval
½1; 1Þ has one exceptional point that prevents it from being open, yet this set is
also not closed since ðy; 1Þ U ½1; yÞ is not open.
That open and closed sets are fundamentally di¤erent can be first appreciated by
observing how di¤erently they behave under set operations.
Proposition 4.3
If fGag is any collection of open sets, Ga H R, with a A I an arbitrary
indexing set, then
6 Ga is an open set:
If this collection is finite, then 7 Ga is an open set. If fFag is any collection of closed
sets, Fa H R, then
7 Fa is a closed set:
If this collection is finite, then 6 Fa is a closed set.
Proof
If x A 6 Ga, then x A Ga for some a. Since each Ga is open, there is an r > 0
so that BrðxÞ H Ga H 6 Ga, proving the first statement. If the collection is finite, and
4.2
Open, Closed, and Other Sets
123

x A 7 Gn, then for every n there is an rn so that BrnðxÞ H Gn, and therefore
BrðxÞ H 7 Gn, where r ¼ min rn. The second statement on closed sets follows from
De Morgan’s laws and the first result. That is, the complement of this general inter-
section is open, since
g
7 Fa
7 Fa ¼ 6 eFa
Fa;
which is a union of open sets by assumption. Similarly, if the collection is finite, the
complement of the union is an intersection of a finite collection of open sets, which is
open.
n
This proposition cannot be extended to a statement about the general intersection
of open sets, or the general union of closed sets. For example,
Gn ¼
 1
n ; 1 þ 1
n


has intersection equal to ½0; 1, whereas
Fn ¼ 1
n ; 1  1
n


has union ð0; 1Þ (see exercise 3).
Other examples are easy to generate where openness and closeness are preserved,
or where semi-openness/closeness is produced (see exercise 15). In other words, any-
thing is possible when an infinite collection of open sets are intersected or closed sets
are unioned.
It turns out that open sets in R can be characterized in a simple and direct way,
but not so closed sets.
Proposition 4.4
G H R is an open set i¤ there is a countable collection of disjoint
open intervals, fIng, so that G ¼ 6 In.
Proof
Clearly, if G is a countable union of open intervals, it is open by the propo-
sition above. On the other hand, for any x A G, let fIða;bÞðxÞg be the collection of
open intervals that contain x and that are contained in G. This family is not empty,
since by definition of open, Iðxr;xþrÞðxÞ 1 BrðxÞ is in this collection for some r > 0.
Define IðxÞ ¼ 6 Iða;bÞðxÞ. By the proposition above, IðxÞ is an open set. But also
we have that IðxÞ must be an open interval: IðxÞ ¼ Iða0;b 0ÞðxÞ. To show this, let
y; z A IðxÞ, with y < z for definitiveness. We must show that ½y; z H IðxÞ. Now since
y A Iða;bÞðxÞ for some ða; bÞ, all points between x and y are also in Iða;bÞðxÞ. Similarly
124
Chapter 4
Set Theory and Topology

all points between x and z are in some other interval, Iðc;dÞðxÞ, say. So we conclude
that
½y; z H Iða;bÞðxÞ U Iðc;dÞðxÞ H IðxÞ:
Finally, to show that fIðxÞg can be collected into disjoint intervals, assume that for
some x 0 y, IðxÞ V IðyÞ 0 j. That is, assume that two such open intervals have non-
empty intersection. Then it must be the case that IðxÞ ¼ IðyÞ, since otherwise,
IðxÞ U IðyÞ would be a larger interval for each of x and y, contradicting the maxi-
mality of the individual intervals. That this collection is countable follows from the
observation that each of the disjoint open intervals constructed must contain a ratio-
nal number.
n
From this result we can redefine closed sets by reverse reasoning:
F H R is closed i¤ ~F is a countable collection of disjoint open intervals.
Unlike an open set, which is always a union of a finite or countably infinite number
of disjoint open intervals, closed sets can di¤er greatly. Any singleton set, fxg, is
closed, as is any finite set, fxjgn
j¼1. Countably infinite closed sets can be sparsely
spaced in R, like the integers, or with accumulation points, such as
m þ 1
n j m; n A

Z; n > 0g U Z. A closed set can even contain uncountably many points, and yet con-
tain no interval. A famous example is the Cantor ternary set, named for its discoverer
Georg Cantor (1845–1918).
The Cantor set, K, is a subset of the interval ½0; 1 and is defined as the intersection
of a countable number of closed sets, fFng, so K ¼ 7 Fn and K is closed. Each suc-
cessive closed set is defined as the prior set, with the open ‘‘middle third’’ intervals
removed. For example,
F0 ¼ ½0; 1;
F1 ¼ ½0; 1 @ 1
3 ; 2
3


;
F2 ¼ F1 @
1
9 ; 2
9


U
7
9 ; 9
9




;
..
.
Interestingly, the total length of the open intervals removed is 1, the length of the
original interval ½0; 1. This can be derived by noting that in the first step, one interval
of length one-third is removed, then two intervals of length one-ninth, then four of
4.2
Open, Closed, and Other Sets
125

length one-twenty-seventh, and so forth. The total length of these intervals can be
expressed as
X
y
n¼0
2n
3nþ1 ¼ 1
3
X
y
n¼0
2
3
 n
¼ 1:
This last summation is accomplished using the informal methodology introduced
in chapter 2 in the applications section for pricing a preferred stock. Recall, if
S 1 Py
n¼0
2
3
 n, then 2
3 S ¼ Py
n¼1
2
3
 n. Subtracting, we conclude that 1
3 S ¼ 1, and
the result follows. (See also the chapter 6 discussion of geometric series for a formal
justification.)
Because the complement of the Cantor ternary set in ½0; 1 has length 1, the Cantor
ternary set is said to be a set of measure 0. The intuition, which will be formalized in
chapter 10 is that a set of measure zero can be contained in, or ‘‘covered by’’ a col-
lection of intervals, the total length of which is as small as desired. In this case the
closed sets Fn provide just such a sequence of sets, as each is a collection of intervals,
each covers K, and by the analysis above, the total length of the intervals in Fn is
1  Pn1
j¼0
2 j
3 jþ1 , which is as small as we want by taking n large enough.
That the Cantor ternary set is in fact uncountable is not at all obvious, since it is
easy to believe that all that will be left in this set are the endpoints of the intervals
removed, and these form a countable collection. The demonstration of uncountability
relies on the base-3 expansion of numbers in the interval ½0; 1, introduced in chapter 2.
Paralleling the decimal expansion, the base-3 expansion uses the digits 0, 1, and 2:
xð3Þ ¼ 0:a1a2a3a4 . . .
1
X
y
j¼1
aj
3 j ;
where aj ¼ 0; 1; 2:
It turns out that the removal of the ‘‘middle thirds’’ is equivalent to eliminating the
possibility of aj ¼ 1, so the Cantor ternary set is made up of all numbers in ½0; 1 with
base-3 expansions using only 0s and 2s. This at first seems counterintuitive because
1
3 A K, and yet the base-3 expansion of 1
3 is 0.1. The same is true for the left endpoints
of the leftmost intervals removed at each step, which are all of the form 1
3 j . But these
can all be rewritten as
1
3 j ¼
X
y
n¼jþ1
2
3n ;
as can be verified using the derivation above.
126
Chapter 4
Set Theory and Topology

By dividing each aj term by 2, all such expansions can then be identified in a 1:1
way with the base-2 expansions of all numbers in ½0; 1, which are uncountable as was
seen in section 2.1.5. Specifically, the identification is
If
X
y
n¼1
aj
3 j A K;
then
X
y
n¼1
aj
3 j $
X
y
n¼1
aj=2
2 j :
4.2.2
Open and Closed Subsets of Rn
Generalizing the ideas from R in the natural way to Rn, we have the following:
Definition 4.5
Given x A Rn, a neighborhood of x of radius r, or open ball about x of
radius r, denoted BrðxÞ, is defined as
BrðxÞ ¼ fy A Rn j jx  yj < rg;
ð4:2Þ
where jxj denotes the standard norm on Rn. A subset G H Rn is open if, given x A G,
there is an r > 0 so that BrðxÞ H G. A subset F H Rn is closed if the complement of F,
~F, is open.
The proposition above on unions and intersections of open and closed sets in R
carries over to Rn without modification. We state this result without proof.
Proposition 4.6
If fGag is any collection of open sets, Ga H Rn, then
6 Ga is an open set:
If this collection is finite, then 7 Ga is an open set. If fFag is any collection of closed
sets, Fa H Rn, then
7 Fa is a closed set:
If this collection is finite, then 6 Fa is a closed set.
It is also the case that one cannot generalize this result to arbitrary intersections of
open sets, nor arbitrary unions of open sets, and the examples above easily generalize
to this setting (see exercise 16).
Remark 4.7
Note that ‘‘open’’ was defined in terms of open balls, and in turn by the
standard metric in Rn, also called the l2-metric in chapter 3. However, as might be
guessed from that chapter, we could have used any metric equivalent to the standard
metric and obtained the same open and closed sets due to (3.35). We formalize this
observation in the following:
4.2
Open, Closed, and Other Sets
127

Proposition 4.8
Let d 0ðx; yÞ be any metric on Rn equivalent to the standard metric
dðx; yÞ ¼ jx  yj given in (3.18), and let open sets be defined relative to open d 0-balls.
Then G H Rn is open relative to d 0 i¤ it is open relative to d.
Proof
We demonstrate one implication only, as the other is analogous. Assume
that G is open relative to d 0, and let x A G. Then, by definition, there is an r0 > 0 so
that B0
r0ðxÞ H G. By (3.35), there is an r > 0 so that
BrðxÞ H B0
r0ðxÞ:
and hence BrðxÞ H G and so G is open relative to dðx; yÞ.
n
It is important to note that this proposition cannot be expanded arbitrarily. If d
and d 0 are metrics that are not equivalent, it will generally be the case that the asso-
ciated notions of open and closed will also not be equivalent.
Remark 4.9
Because as proved in proposition 3.41, Lipschitz equivalence of metrics
implies equivalence, any result stated concerning equivalent metrics is automatically
true for Lipschitz equivalent metrics.
*4.2.3
Open and Closed Subsets in Metric Spaces
The definition of a neighborhood, or open ball about x A Rn, is fundamentally a
metric notion. Namely an open ball of radius r about x is defined to be equal to
all points within a distance of r from x. Consequently, for any metric space, whether
familiar like C or an exotic construction, we can likewise define open ball, and
open and closed sets, in terms of the distance function—or metric—that defines the
space.
Definition 4.10
Given x A X, where ðX; dÞ is a metric space, a neighborhood of x or
open ball about x of radius r, denoted BrðxÞ is defined as
BrðxÞ ¼ fy j dðx; yÞ < rg:
ð4:3Þ
A subset G H X is open, and sometimes d-open, if given x A G, there is an r > 0 so that
BrðxÞ H G. A subset F H R is closed if the complement of F, ~F, is open.
For example, let X ¼ C, the complex numbers under the metric defined by the
norm in (2.2), and let BrðxÞ be defined as in (4.3). Then, if x ¼ a þ bı and y ¼
c þ dı, we have y A BrðxÞ i¤ jx  yj < r. That is, by (2.2),
½ða  cÞ2 þ ðb  dÞ21=2 < r:
128
Chapter 4
Set Theory and Topology

Note that under the identification C $ R2, a þ bı $ ða; bÞ, we can define y A BrðxÞ
on C i¤ y A BrðxÞ defined on R2 under this identification. That is, the identifica-
tion C $ R2 preserves the metrics defined on these respective spaces, as well as the
notions of open and closed.
We note that in the general context of a metric space, as was demonstrated for
R, C, and Rn, the concept of an open set is not as metric-dependent as it first
appears.
Proposition 4.11
Let X be a metric space under two equivalent metrics, d1 and d2.
Then a set G H X is open in ðX; d1Þ i¤ G is open in ðX; d2Þ.
Proof
The proof, based on (3.35), is identical to that above in Rn.
n
*4.2.4
Open and Closed Subsets in General Spaces
In a more general space without a metric, one can specify the open sets of X by
defining a so-called topology on X as follows:
Definition 4.12
Given a space X, a topology is a collection of subsets of X, =, which
are the open sets, with the following properties:
1. j; X A =,
2. If fGag H =, then 6 Ga A =,
3. If fGng H =, a finite collection, then 7 Gn A =.
Hence a topology identifies the collection of open sets and demands that this col-
lection behaves the same way under union and intersection as we have shown open
sets to behave in the familiar settings of R, C, Rn or a general metric space X. In
particular, in any of these special spaces, if we define = as the collection of open
sets under the definition of open as a metric space, then = is a topology by the above
definition. Such a topology is said to be induced by the metric d.
Closed sets are then defined by
F H X
is closed i¤
~F A =;
and we see that this collection of closed sets again behaves in a familiar way under
unions and intersections, based on De Morgan’s laws.
Equivalent topologies can then be defined as follows:
Definition 4.13
Two topologies =1 and =2 on a space X are equivalent if for any
G1 H =1, there is a G2 H =2 with G2 H G1, and conversely, for any G2 H =2, there is
a G1 H =1 with G1 H G2.
4.2
Open, Closed, and Other Sets
129

Not surprisingly, especially given the terminology, we have immediately from the
above proposition in a general metric space:
Corollary 4.14
Let X be a metric space under two equivalent metrics, d1 and d2. Then
the topologies induced by d1 and d2 are equivalent.
Remark 4.15
This corollary provides the motivation for the use of the language as
noted in chapter 3, that d1 and d2 are ‘‘topologically equivalent,’’ as an alternative to
the terminology, d1 and d2 are ‘‘equivalent.’’ The point is, such metrics provide the
equivalent topologies on the space.
Finally, we note that if a space X has a topology, =, and Y H X is a subset, then
there is a natural topology on Y called the relative topology or induced topology,
denoted =Y, which is defined as
=Y ¼ fY V G j G A =g:
For example, if we consider R as a topological space with open sets defined by the
standard metric, and Y ¼ ½0; 1, then the induced topology on Y contains sets of the
form ½0; bÞ, ða; bÞ, ðb; 1, where 0 < a < b < 1, as well as ½0; 1.
4.2.5
Other Properties of Subsets of a Metric Space
In the preceding sections it was clear that the notions of open and closed could be
defined in any metric space using nearly identical definitions, the only di¤erence re-
lated to the particular space’s notion of distance as given by that space’s metric. In
this section, rather than repeat the same development for other important properties
of sets from an initial definition in R, to one in Rn, to a general metric space X, we
introduce the definitions directly in a general metric space, and leave it to the reader
to reformulate these definitions in the other special cases.
Many of these notions also have meaning in a general topological space, but we
will not have need for this development.
Definition 4.16
In a metric space X with metric d:
1. If x A X, the closed ball about x of radius r > 0 is defined by
BrðxÞ ¼ fy j dðx; yÞ a rg:
ð4:4Þ
2. If E H X, then x A X is a limit point of E, a cluster point of E, or an accumulation
point of E, if for any r > 0, BrðxÞ V E 0 j. So every x A E is a limit point, but if there
is an r > 0 with BrðxÞ V E 1 x, the point x is also said to be an isolated point of E. We
denote by E the set of limit points of E, or the closure of E, and note that E H E.
130
Chapter 4
Set Theory and Topology

3. E H X is dense in X if every x A X is a limit point of E.
4. E H X is bounded if for any x A X, there is a number r ¼ rðxÞ so that E H BrðxÞ,
and is unbounded otherwise. In the special case of X ¼ R, one also has the notion of
bounded from above and bounded from below. In the former case, there exists xmax so
that x < xmax for all x A E, whereas in the latter case, there exists xmin so that x > xmin
for all x A E.
5. Given E H X, a collection of open sets, fGag, is an open cover of E if E H 6a Ga.
6. E H X is compact if given any open cover of E, fGag, which may be uncountably
infinite, there is a finite subcollection, fGjgm
j¼1 so that
E H 6
jam
Gj:
7. E H X is connected if given any two open sets, G1 and G2, with E H G1 U G2, we
have G1 V G2 0 j. E H X is disconnected if there exists open sets, G1 and G2, with
E H G1 U G2, and G1 V G2 ¼ j.
Several of the important properties related to these notions are summarized in the
following proposition, stated in the general metric space context. However, on first
reading the intuition may be more easily developed if one envisions R as the given
metric space, rather than X.
Proposition 4.17
Let X be a metric space, then:
1. If E H X is closed and x is a limit point of E, then x A E, and hence E ¼ E. Con-
versely, if E ¼ E, then E is closed.
2. If x A X is a limit point of E H X that is not an isolated point, then for any r > 0
there is a countable collection fxng H BrðxÞ V E, with xn 0 x.
3. If E H X is compact, then E is closed and bounded.
4. (Heine–Borel theorem) E H Rn is compact i¤ E is closed and bounded.
5. If fxag H E is a countable or uncountable infinite set, and E is compact, then fxag
has a limit point x A E.
Proof
We prove each statement in turn:
1. If E H X is closed, and x B E, then x A ~E, which is open, and hence by definition,
there is an r > 0 so that BrðxÞ H ~E. So it must be the case that BrðxÞ V E ¼ j, and
therefore x cannot be a limit point of E. Hence, if x is a limit point of E, we must
have x A E and so E ¼ E. Conversely, if E ¼ E, and x A ~E ¼ ~E, then since x is not a
4.2
Open, Closed, and Other Sets
131

limit point, there is an r > 0 so that BrðxÞ V E ¼ j. That is, ~E is open and hence E is
closed.
2. Choose a sequence rn ! 0. Then by assumption that x A X is a limit point of E
that is not isolated, BrnðxÞ V E 0 j for all n, and each such intersection contains at
least one point other than x. Choose xn A BrnðxÞ V E with xn 0 x. Then fxng must
be countably infinite, since for any n, there is rN < minjan dðx; xjÞ, and hence xN
must be distinct from fxjgn
j¼1.
3. If E H X is compact, it is bounded, since we can define an open cover of E by
fB1ðxÞ j x A Eg. Then by compactness, there is a finite collection fB1ðxjÞ j j ¼ 1; . . . ;
ng. Let D ¼ max dðxj; xkÞ. Next, given any x A X, if y A E, then y A B1ðxkÞ for some
k, and we can derive from the triangle inequality that
dðx; yÞ a dðx; x1Þ þ dðx1; xkÞ þ dðxk; yÞ
a dðx; x1Þ þ D þ 1;
and hence E H BRðxÞ for R ¼ dðx; x1Þ þ D þ 1 and E is bounded. To show that E is
closed, we demonstrate that ~E is open. To this end, let x A ~E. Then for any y A E, let
eðyÞ ¼ dðx; yÞ=2 and construct BeðyÞðyÞ. Clearly, by construction, fBeðyÞðyÞg is an
open cover of E. Since E is compact, let fBeðynÞðynÞg be the finite subcollection,
which is again a cover of E, and define e ¼ 1
2 min eðynÞ. By construction, BeðxÞ V
ð6 BeðyÞðynÞÞ ¼ j. So since E H 6 BeðyÞðynÞ, we get that BeðxÞ H ~E, and hence ~E is
open and E closed.
4. From step 3 we only have to prove the ‘‘only if’’ part, that in Rn, closed and
bounded implies compact. To that end, assume that E H Rn is closed and bounded.
Since it is bounded, we have that for some R > 0, E H BRð0Þ. Also BRð0Þ H CRð0Þ,
the closed cube about 0 of diameter 2R defined by
CRð0Þ ¼ fx j R a xj a R; all jg:
ð4:5Þ
We will prove below that the closed cube, CRð0Þ, is compact for any R, and this will
prove that E is compact as follows. Given any open cover of E, it can be augmented
to become an open cover of CRð0Þ by addition of the open set CRþ1ð0Þ @ E. Here
CRþ1ð0Þ is the open cube defined as in (4.5) but with strict inequalities, and since E
is closed, CRþ1ð0Þ @ E ¼ CRþ1ð0Þ V ~E is open. Now once CRð0Þ is proved to be com-
pact, this cover will have a finite subcover that then covers E without the added
set CRþ1ð0Þ @ E, and hence E is compact. We now prove that CRð0Þ is compact by
contradiction—assuming that CRð0Þ is not compact. Then there is an open cover
fGjg for which no finite subcover exists. Subdivide CRð0Þ into 2n closed cubes by
halving each axis,
132
Chapter 4
Set Theory and Topology

CRð0Þ ¼ 6
2 n
j¼1
Cj;
where each Cj is defined by one of the 2n combinations of positive and negative
coordinates:
Cj ¼ fx j for each i; 0 a xi a R or R a xi a 0g:
Then at least one of these Cj has no finite subcover from fGjg, for if all did, then
CRð0Þ would have a finite cover and hence be compact. Choose this Cj and subdivide
it into 2n closed cubes,
Cj ¼ 6
2n
k¼1
Cjk;
by again halving each axis, and choose any one of these cubes that has no finite sub-
cover. Continuing in this way, we have an infinite collection of closed cubes: CRð0Þ I
Cj I Cjk I Cjkl I   , none of which have a finite subcover from fGjg. By construc-
tion, the intersection of all such cubes is a single point x, but since x A Gj for some j,
and Gj is open, there is a BrðxÞ H Gj. Beyond a given point this ball must then con-
tain all the subcubes in the sequence above, since at each step the sides of the cube
are halved and decrease to 0. This contradicts that no subcube has a finite subcover,
and hence all such cubes have a finite subcover and CRð0Þ is compact.
5. Assume that fxag H E, and E is compact, but that fxag has no limit point in E.
Then for any a there is an open ball BraðxaÞ that contains no other point in the se-
quence than xa. Indeed, if there was such an xa so that BrðxaÞ always contained at
least one other point for any r ! 0, then this xa would be a limit point of the se-
quence by definition. Now fBraðxaÞg is an infinite collection of open sets, to which
we can add the open set A 1 X @ ½6 Bra=2ðxaÞ, which is open since the complement
of A in X is the closed set ½6 Brn=2ðxnÞ. We hence have an open cover of E with no
finite subcover by construction, contradicting the compactness of E.
n
Note that in the proof of the Heine–Borel theorem there is a construction that can
easily be generalized to demonstrate:
Corollary 4.18
If X is a metric space, E H X is compact and F H E is closed, then F
is also compact.
Proof
If fGjg is an open cover of F, then fGjg U ~F is an open cover of E that has
a finite subcover by compactness. This finite subcover, excluding the set ~F, is then a
finite subcover of F.
n
4.2
Open, Closed, and Other Sets
133

Corollary 4.19 (Heine–Borel Theorem)
E H C is compact i¤ E is closed and
bounded.
Proof
We have seen that the identification C , R2 preserves the respective metrics
in these spaces, and hence the closed and open balls defined in (4.4) and (4.3) are
identical in both spaces. In R2 we have shown that the closed cube is compact, and
by the corollary above, any closed ball within this cube is also compact. Conse-
quently every closed ball in C is also compact and the above proof can be stream-
lined. If a closed and bounded E H C had an open cover with no finite subcover,
then this cover could be augmented with the open set BRþ1ð0Þ @ E ¼ BRþ1ð0Þ V ~E;
here, as above, we assume that E H BRð0Þ. We have now constructed an open cover
of BRð0Þ with no finite subcover, contradicting the compactness of this closed ball.
n
The Heine–Borel theorem is named after Eduard Heine (1821–1881) and E´ mile
Borel (1871–1956). Borel formalized the earlier work of Heine in an 1895 publication
that applied to the notion of compactness, which was then defined in terms of count-
ably infinite open covers. Specifically, compact meant that every countable open
cover had a finite subcover. This in turn was generalized by Henri Lebesgue (1875–
1941) in 1898 to the notion of compactness defined in terms of an arbitrary infinite
open cover, and this is the definition now used.
Remark 4.20
The reader reviewing the propositions above may notice a glaring omis-
sion. On the one hand, in every metric space a compact set is closed and bounded.
On the other hand, the subject of the Heine–Borel theorem, that closed and bounded
implies compact, is only stated as true in Rn and C. While Heine–Borel is also true in
Cn, we do not prove this as we have no need for this result. But it is only natural to
wonder if Heine–Borel can be extended to all metric spaces. The answer is no, although
the development of such an example will take us too far afield to be justified given that
we will not make use of this in what follows.
4.3
Applications to Finance
4.3.1
Set Theory
In general, knowledge of the axiomatic structure of set theory, or even the need for
an axiomatic structure, is not directly applicable to finance except as a cautionary
tale, as was discussed in chapter 1. While one’s intuition can be a valuable facilitator
in the development of an idea, or the pursuit of a solution to a problem, it is rarely
134
Chapter 4
Set Theory and Topology

adequate in and of itself even when the topic at hand appears elementary, and cau-
tion seems unwarranted. The ideal approach to problems in finance is where the
development is mathematically formal but enlightened with intuition.
In finance as in all mathematical applications, one sometimes has a compelling in-
tuitive argument as to how a problem ought to be solved, and then perhaps struggles
to make this intuition precise. On the other hand, one sometimes discovers (or stum-
bles upon) a formal mathematical relationship and then struggles with an intuitive
understanding. Both approaches are common, and both are valuable. The key is
that until one has both, mathematical rigor and intuition, one hasn’t really solved
the problem. That is, a true ‘‘solution’’ requires a quantitative derivation of the solu-
tion to the problem as well as an intuitive understanding of why this solution works.
Of course, the tools of set theory are necessary and important simply because
many problems in finance can be articulated in terms of sets, and so call for formal
understanding and working knowledge of the set operations as well as their
properties.
4.3.2
Constrained Optimization and Compactness
The constrained optimization problems discussed in chapter 3 on Euclidean spaces
can be posed in terms of sets. For example, consider the constrained maximization
problem in Rn:
max gðxÞ;
given that
f ðxÞ ¼ c:
Now define the sets
A ¼ fx A Rn j f ðxÞ ¼ cg;
B ¼ fgðxÞ j x A Ag:
Then A H Rn is clearly the constraint set, and B H R is the set of values the objec-
tive function takes on this constraint set. For example, A might denote the portfolio
allocations that provide a given level of ‘‘risk’’ appropriately defined, and B then
evaluates the average or return ‘‘expected’’ from these allocations.
Now, if B is unbounded from above, then the constrained optimization obviously
has no solution. Hence, within this framework, solvability is seen to depend at the
minimum on conditions on A and gðxÞ, which assure that B is bounded from above.
Of course, if we seek a minimum, we need B to be bounded from below.
However, while boundedness is necessary, it is not su‰cient. If B is an open subset
of R, it will not contain its minimum or maximum points. This comes from the def-
inition of open, which is to say, if x A E an open set, then there is an r > 0 so that
4.3
Applications to Finance
135

BrðxÞ H E, and no x can be a maximum or a minimum. Hence within this frame-
work, solvability is also seen to depend at the minimum on conditions on A and
gðxÞ, which assure that B is bounded and closed—which is to say, by the Heine–
Borel theorem, that B is compact. In that case, if xopt A B is the optimized value,
either the maximum or the minimum, then by definition there is an xopt A A so that
gðxoptÞ ¼ xopt. Hence, if B is compact, there is in theory a solution to the constrained
optimization problem. Uniqueness will then depend on conditions on gðxÞ.
Logically, the condition(s) on A and gðxÞ that assure compactness of B are in fact
conditions on the constraint function f ðxÞ and the objective function gðxÞ. More
generally, the constraint set A may be defined as
A ¼ fx j f ðxÞ A Cg;
where C is a given constraint set, C H R. Alternatively, A may be defined in terms of
multiple constraints, as the intersection of sets of the form fx j fiðxÞ A Cig:
A ¼ fx j fiðxÞ A Ci for all 1 a i a mg:
So we see that in this general case the compactness of the objective function’s
range B reflects conditions on the functions f and g, as well as the constraint set C.
Notationally, if f is one-to-one, we can express A ¼ f 1ðCÞ and B ¼ gðAÞ, and
hence
B ¼ gð f 1ðCÞÞ:
So we seek conditions on C, f , and g that ensure that B is compact.
When f is not one-to-one, we seek conditions on g and A to ensure that gðAÞ is
compact, and in turn conditions on f and C to ensure that the needed conditions
on A are satisfied.
To explore this, we need to study additional properties of functions that will pro-
vide answers to these and related questions. The first steps will be taken in chapter 9
on calculus I, which addresses di¤erential calculus on R, but this will not be enough
for the question above despite the fact that both B and C are subsets of R. The prob-
lem, of course, is that in going from C to B we need to ‘‘travel’’ through A H Rn, so
for a complete answer, multivariate calculus is required.
That said, there is still the issue of determining a solution. The analysis above
would provide what in mathematics is known as a qualitative theory and solution
to the constrained optimization problem. What is meant by ‘‘qualitative’’ is that the
theory demonstrates that a solution exists and whether or not it is unique. There is
then the question of developing a quantitative theory and solution. That is, either an
explicit formula or procedure that provides the answer, or a numerical algorithm that
136
Chapter 4
Set Theory and Topology

will ‘‘converge’’ to the given solution after infinitely many iterations. In the latter
case, since we only have finitely much time, our goal would be to perform enough
iterations to assure accuracy to some level of tolerance.
This raises the question of ‘‘convergence’’ and rate of convergence, issues intro-
duced in the next two chapters on sequences and series. This discussion will then be
expanded in chapter 9, where the relationship between properties of sets and proper-
ties of functions on R and related questions will be addressed.
4.3.3
Yield of a Security
In chapter 2 a number of formulas were derived for the prices of various securities,
expressed as functions of variables that define the security’s cash flow characteristics
as well as of the investors’ required yields. Put another way, given the cash flow
structure, price can be thought of as a function of yield. One application of these for-
mulas is to determine the price investors are willing to pay, given their yield require-
ments. Oftentimes in the financial markets, however, an investor faces a di¤erent
question, and that is, given the market price of a security, what is the implied inves-
tor yield.
Such questions can arise in terms of a bid price, the price that a dealer is willing to
pay on a purchase from an investor, or an o¤er (or ask) price, the price that a dealer
requires on a sale to an investor. In both cases the investor is interested in the yield
implications of the trade.
The o¤er price is always more, of course, and hence the o¤er yield is less than the
associated bid yield. It is common to be interested in the so-called bid–ask spread, or
bid–o¤er spread, defined as the di¤erence between the higher bid yield and the lower
ask–o¤er yield. This yield di¤erential provides information to the investor on the li-
quidity of the security. A small bid–ask spread is usually associated with high liquid-
ity, and increasingly larger spreads are associated with increasingly less liquidity.
In this context the notion of liquidity implies the commonly understood meaning
as a measure of ‘‘ease of sale,’’ since the dealer can encourage or discourage investor
sales by favorable or unfavorable pricing. Narrow spreads are associated with deep
markets of actively traded securities, and wide spreads with thin or narrow markets.
In e¤ect, a wide spread is compensation to the dealer for the expected delayed o¤set-
ting transaction, and the risks or hedge costs incurred during the intervening period.
But more important, liquidity is a measure of the fairness of the transaction’s
price. A small spread implies pricing is fair, since dealers are willing to transact either
way at similar prices, whereas a wide spread implies that an investor sale may be well
below a fair price, and purchase well above a fair price. Of course, fairness is like
beauty; it is in the eye of the investor. Nonetheless, all market participants agree
4.3
Applications to Finance
137

that the size of the spread tells a lot about both the ease of transacting and the fair-
ness of pricing.
If PðiÞ denotes the pricing function for a given security, and P0 the price quoted,
the security’s implied yield, or in the case of a fixed income security, implied yield to
maturity, is the solution i0 to the equation
PðiÞ ¼ P0:
ð4:6Þ
In this section we informally introduce the method of interval bisection in solving
(4.6) for i0, and return to this methodology with greater formality in later chapters.
First o¤, one can do a qualitative analysis of this equation to determine if a solu-
tion is feasible. In virtually all markets one expects that all yields on securities are
greater than 0%, and less than 100%, so a very simple qualitative assessment for the
existence of a solution is that
Pð1:0Þ a P0 a Pð0Þ;
where i ¼ 0 and 1:0 mean that the respective discount factors in the pricing formula,
v ¼ ð1 þ iÞ1, are 1 and 1
2 . From this assessment we can posit that i0 A ½0; 1 1 F0. In
practice, this first step could well produce a much smaller initial solution interval,
such as ½0:05; 0:1, but for notational simplicity, we ignore this refinement.
Next we could evaluate Pð0:5Þ, or in general, the price function at the midpoint of
the initial interval. We then have either
Pð1:0Þ a P0 a Pð0:5Þ
or
Pð0:5Þ a P0 a Pð0Þ:
From this we conclude that either i0 A ½0:5; 1 or i0 A ½0; 0:5, respectively, and choose
the appropriate interval and label it F1. Of course, if P0 ¼ Pð0:5Þ, we are done.
Continuing in this way, one of two things happens:
1. We develop a sequence of closed intervals Fn, with i0 A Fn for all n, and lengths
jFnj ¼ 1
2 n .
2. Or the process serendipitiously stops in a finite number of steps, since i0 is an end-
point of one of the Fn.
Assuming the process does not stop, we can identify ‘‘approximate’’ solutions to
the equation in (4.6) by simply choosing the midpoints of the respective intervals.
Specifically, defining in as the midpoint of Fn, it must be the case, since i0 A Fn and
jFnj ¼ 1
2 n , that
jin  i0j <
1
2nþ1 :
138
Chapter 4
Set Theory and Topology

Also, since fFng are closed sets, and the length jFnj decreases to 0, then 7 Fn is
closed and hence must be a single point. That is, it must be the case that
i0 ¼ 7 Fn:
Or does it?
If Fn ¼ ½an; bn, all we know is that PðbnÞ a P0 a PðanÞ for all n, and that bn  an
¼ 1
2 n . But how do we know that there is a unique value in this interval, which we de-
note i0, on which P0 is achieved by PðiÞ? Let’s summarize the assumptions made to
draw this desired conclusion:
1. We implicitly assumed that the price function was decreasing, or more generally,
that it is monotonic (increasing or decreasing), since at each step we assumed, in the
notation above, that the value at the midpoint was ‘‘between’’ the endpoint values:
PðbnÞ a PðinÞ a PðanÞ:
Then we could choose one or the other of the subintervals ½an; in or ½in; bn in the next
step. We know, or at least intuit, that this is true for most pricing functions in fi-
nance, and this can be demonstrated with the tools of chapter 9. But in a more gen-
eral application, PðinÞ could exceed either endpoint value, or be less than either. In
such a case there could be more than one solution, and we would have to choose
which interval(s) we search to find them.
2. We implicitly assumed that the price function varies in a smooth and predictable
way, a property that will be called continuity in chapter 9. Specifically, we know from
the values of jFnj that the intersection of these closed sets will produce a unique
point, call it i0. We also know that by construction, PðbnÞ a P0 a PðanÞ, and given
the assumption of monotonicity, that PðbnÞ a PðinÞ a PðanÞ, where in is the midpoint
of Fn. But to conclude from in ! i0 that PðinÞ ! Pði0Þ requires an assumption on the
continuity of the price function PðiÞ, which thankfully, is true for pricing functions as
will also be seen.
We will return to the analysis of interval bisection in chapter 5.
Exercises
Practice Exercises
1. Russell’s paradox is equivalently formulated as the Barber Paradox: In a town
there is a barber who shaves all the men that do not shave themselves, and only those
men. Define ‘‘set’’ A as the set of all men in the town that the barber shaves.
Exercises
139

(a) Is the barber a member of this set? Show that the barber’s set membership cannot
be determined as we would conclude the paradox that the barber shaves himself if
and only if he does not shave himself.
(b) Note that the paradox works because at the time, the barber was assumed to be
male. Show that if the barber were female, we could conclude that the barber is not a
member of this set, whether she shaves or not.
2. Prove De Morgan’s laws 2 to 4, using the operational definitions.
3. Demonstrate the following, using operational definitions:
(a) If Gn 1  1
n ; 1 þ 1
n


, then 7 Gn ¼ ½0; 1, so the intersection of open sets can be
closed.
(b) If Fn 1
1
n ; 1  1
n


, then 6 Fn ¼ ð0; 1Þ, so the union of closed sets can be open.
4. Show that if a set A contains n-elements, that the power set of A, defined as the set
of all subsets of A, contains 2n elements. (Hint: Label the elements of A as
x1; x2; . . . ; xn, and define a chooser function on the power set that produces decimal
expansions as follows:
f ðBÞ ¼ 0:a1a2a3a4 . . . an;
where
aj ¼
0;
xj B B,
1;
xj A B.

Show that f ðBÞ ¼ f ðB0Þ i¤ B ¼ B0, and that the range of f has 2n elements.)
5. Generalize exercise 4 to the case where A contains a countably infinite number of
elements, and show that with an abuse of notation, there are 2y elements in the
power set, where this symbol denotes the uncountable infinity of real numbers in the
interval ½0; 1. (Hint: Use the construction in exercise 4, and recall the binary expan-
sions of reals x A ½0; 1.)
6. Demonstrate that the points in the Cantor set can be identified with base-3
expansions, 0:a1a2a3a4 . . . , where aj ¼ 0; 2. (Hint: Show that points in F1 all begin
as 0:0a2a3a4 . . . or 0:2a2a3a4 . . . , then show that points in F2 are of the form:
0:a1a2a3a4 . . . , where a1a2 ¼ 00; 02; 20; 22, etc.)
7. Develop another proof that the Cantor set has measure 0, using the fact that if we
denote by jFnj the total length of the intervals in Fn, then by the construction,
jFnþ1j ¼ 2
3 jFnj. (Hint: K ¼ 7y
j¼0 Fj, but 7n
j¼0 Fj ¼ Fn.)
8. Show that the following sets have measure 0 by constructing a covering with inter-
vals that have arbitrarily small total length. (Hint: Recall that Py
n¼1
1
2n ¼ 1.)
140
Chapter 4
Set Theory and Topology

(a) The integers Z
(b)
1
n j n ¼ 1; 2; 3; . . .


(c) The rationals Q V ð0; 1Þ
9. For 1 a p a y, define a set, G H R2 to be ‘‘lp-open’’ if for any x A G there is an
r > 0 so that BðpÞ
r ðxÞ H G where BðpÞ
r ðxÞ ¼ fy j kx  ykp < rg, and where kx  ykp
denotes the lp-norm. The usual definition of open is then l2-open.
(a) Show that G is open if and only if it is l1-open. (Hint: Recall the graphs of equiv-
alent metrics in chapter 3.)
(b) Generalize part (a) to show that G is open if and only if it is lp-open for all p.
10. Define a set G H Rn to be open if for any x A G, there is an r > 0 so that
BðdÞ
r ðxÞ H G, where BðdÞ
r ðxÞ ¼ fy j dðx; yÞ < rg.
(a) Exercise 18 of chapter 3 introduced a metric on Rn that was not equivalent to the
lp-metrics. Specifically,
dðx; yÞ ¼
0;
x ¼ y,
1;
x 0 y.

Determine all the open sets in Rn.
(b) Define:
dðx; yÞ ¼ f0;
all x; y:
Prove that there is only one open set, and determine what it is.
11. The Heine–Borel theorem assures that a set is compact in Rn if and only if it is
closed and bounded. Explain how to choose the finite subcovers of the following
open covers of the given sets:
(a) F ¼ ½0; 1 H 6 BrðxjÞ, where fxjg is an arbitrary enumeration of the rational
numbers in the interval and r > 0 is an arbitrary constant.
(b) F ¼ ½0; 1 H 6 BrjðxjÞ, where fxjg is an arbitrary enumeration of the rational
numbers in the interval, and rj > 0 are arbitrary values. If rj > r > 0, this can be
solved as in part (a), so assume that 0 is an accumulation point of frjg.
(c) F ¼ CRð0Þ H 6 CrðxjÞ in R2, where CR denotes the closed 2-cube, or square,
about 0 of diameter 2R, and CrðxjÞ denotes the open cubes about points xj, with ra-
tional coordinates, of fixed diameter 2r > 0.
12. Show that the interval ð0; 1Þ is not compact by constructing an infinite open
cover for which there is no finite subcover. (Hint: Construct an open cover sequen-
tially, with Ij H Ijþ1.)
Exercises
141

13. Use the method of interval bisection to determine the yields of the following
securities to four decimals (i.e., to basis points). Solve each in the appropriate nomi-
nal rate basis:
(a) A 10 year bond with 5% semiannual coupons, with a price of 98:75 per 100 par.
(b) An annual dividend common stock, last dividend of $10 paid yesterday and
assumed to grow at 8% annually, selling for $115:00.
(c) A 5-year monthly pay commercial mortgage, with loan amount $5 million and
amortization schedule developed with a monthly rate of 6%, selling in the secondary
market for $5:2 million.
Assignment Exercises
14. Simplify the following expressions by applying De Morgan’s laws, and then
demonstrate that the expression derived is correct using the operational definitions.
(a) ðA V ~BÞc U C
(b) ðB V ½6a AaÞc
(c) ð6a AaÞc U ð7b ~BbÞc
Recall that ðCÞc denotes ~C.
15. Generalize exercise 3:
(a) Provide an example of a countably infinite collection of open Gn H R so that
7 Gn is open.
(b) Repeat part (a) so that 7 Gn is neither open nor closed.
(c) Provide an example of a countably infinite collection of closed Fn H R so that
6 Fn is closed.
(d) Repeat part (c) so that 6 Fn is neither open nor closed.
16. Develop examples in R2 of the results illustrated in:
(a) Exercise 3
(b) Exercise 15
Can your constructions in parts (a) and (b) be applied in Rn?
17. Generalize exercise 5 and show that if A is a set of any ‘‘cardinality,’’ the power
set of A has greater cardinality; that is to say, its elements cannot be put into one-to-
one correspondence with the elements of A. (Hint: Assume there is such a correspon-
dence, and define f ðaÞ as the 1:1 function that connects A and its power set. In other
words, f ðaÞ ¼ Aa, the unique subset of A associated with a. Consider the set
A0 ¼ fa j a B Aag. Then there is an a0 A A so that this collection is produced by
f ða0Þ; that is, A0 ¼ Aa 0. Show that a0 A Aa 0 i¤ a0 B Aa0.)
142
Chapter 4
Set Theory and Topology

Remark 4.21
In Cantor’s theory of infinite cardinal numbers, where ‘‘cardinal’’ is in-
tended as a generalization of the idea of the ‘‘number’’ of elements in a set, the symbol
@0 and read ‘‘Aleph-naught,’’ denotes the cardinality of the integers, or ‘‘countably in-
finite.’’ Then @1 denotes the next greater cardinality, @2 the next, and so forth, and
Cantor proved with the construction of this exercise that there is an infinite sequence
of cardinal numbers so that no one-to-one correspondence could be produced between
any two sets with di¤erent cardinalities. For example, we have already seen that a set
of cardinality @0 cannot be put into one-to-one correspondence with the set of real num-
bers, so the cardinality of the reals must exceed @0. Now the cardinality of the power
set of a set of cardinality @0 is the same as the cardinality of the collection of all func-
tions from a set of cardinality @0, to the 2-element set, f0; 1g. This follows from the
construction in exercise 5, since every set in the power set implies a function that has
value 1 on every element in this set, and value 0 on every element not in this set. The
notation used for the cardinality of this class of functions is 2@0 and exercise 5 assures
that @0 < 2@0 and that 2@0 ¼ c, the uncountable infinity of the real numbers, also called
the continuum. The power set of a set of cardinality @1 again has greater cardinality by
exercise 17, equal to the 2@1, and so @1 < 2@1. This process continues, in turn producing
an infinite sequence of increasingly large infinite cardinals, since for all j, @j < 2@j. The
continuum hypothesis, which is a statement that has been proved to be independent of
ZFC set theory (the 10 Zermelo–Fraenkel axioms with the axiom of choice), is that
there is no cardinal strictly between @0 and c ¼ 2@0, and hence the next greater cardinal
@1 is 2@0. In other words, @1 ¼ 2@0. The generalized continuum hypothesis states that
there is no cardinal strictly between @j and 2@j for any j and so @jþ1 ¼ 2@j. It has been
proved that this hypothesis is also independent of the ZFC set theory, and hence can
neither be proved nor disproved in that theory. In other words, mathematicians have
the option to add these hypotheses or their negative to the theory, and in each case
derive a consistent theory of cardinals.
18. Denote the Cantor set developed in this chapter by K2=3 to signify that in
each step, each closed interval from the prior step is divided equally into three-
subintervals, and the second open subinterval is removed. Define a generalized Can-
tor set, denoted Km=n, for n, m integers, n b 3, m ¼ 1; 2; . . . ; n, analogously. That is,
at each step, each closed interval of the form
k
n j ; kþ1
n j


from the prior step is divided
equally into n-subintervals, and the mth open subinterval removed.
(a) Defining Km=n as the intersection of all the sets produced in these steps, confirm
that Km=n is closed.
(b) Show that Km=n has measure 0 using the approach of exercise 7. Note the com-
plexity of proving this result by considering the sum of the lengths of the intervals
removed.
Exercises
143

(c) Show that Km=n is uncountable by identifying points in this set with base-n expan-
sions, but without the digit m  1. (Hint: Identify these expansions with base-ðn  1Þ
expansions of all real numbers in ½0; 1.)
19. Demonstrate that the exercise 18(c) construction does not work if n ¼ 2.
(a) Show that Km=2 is a closed set of measure 0.
(b) Prove that Km=2 is countable and identify explicitly the elements of these two sets,
where m ¼ 1 or m ¼ 2.
20. Generalizing exercise 8, show that the following sets in R2 have measure 0,
which means that the set can be covered by a collection of balls with total area as
small as we choose.
(a) The ‘‘integer lattice’’: fðn; mÞ j n; m A Zg
(b)
1
n ; 1
m


j n; m A Z; n; m 0 0


(c) fðq; rÞ j q; r A Qg
21. Generalize exercise 9 to Rn. (Hint: Recall (3.34).)
22. Show that the following sets are not compact by constructing an infinite open
cover for which there is no finite subcover.
(a) fðx; yÞ H R2 j jxj þ jyj < 1g
(b) fðx; yÞ H R2 j x2 þ y2 < Rg for R > 0.
(c) fx H Rn j x1 0 0g where x ¼ ðx1; x2; . . . ; xnÞ (Hint: Try n ¼ 2 first.)
23. Prove that:
(a) Q1 H Rn defined as Q1 ¼ fx H Rn j xj A Q for all jg is dense for any n.
(b) For any k A N, the set Qk H Rn defined as Qk ¼ fx H Rn j xk
j A Q for all jg is
dense for any n. (Hint: Show Q1 H Qk.)
24. Use the method of interval bisection to determine the yields of the following
securities to four decimal places (i.e., to basis points). Solve each in the appropriate
nominal rate basis:
(a) A 15-year bond with 3% semiannual coupons, with a price of 92:50 per 100 par.
(b) A semiannual dividend common stock, last dividend of $6 paid yesterday and
assumed to grow at a 5% semiannual rate, selling for $66:00.
(c) A perpetual preferred stock with quarterly dividends at a quarterly dividend rate
of 7%, priced at 105:25 per 100 par.
144
Chapter 4
Set Theory and Topology


## Sequences and Their Convergence

5 Sequences and Their Convergence
5.1
Numerical Sequences
5.1.1
Definition and Examples
The mathematical concept of a numerical sequence is deceptively simple, and yet its
study provides a solid foundation for a great many deep and useful results as we will
see in coming chapters.
Definition 5.1
A numerical sequence, denoted fxng, fzjg, and so forth, is a countably
infinite collection of real or complex numbers for which a numerical ordering is
specified:
fxng 1 x1; x2; x3; . . . :
For specificity, the sequence may be called a real sequence or a complex sequence. A
numerical sequence is said to be bounded if there is a number B so that jxnj a B for
all n. A subsequence of a numerical sequence is a countably infinite subcollection that
preserves order. That is, fymg is a subsequence of fxng if
ym ¼ xnm
and
nmþ1 > nm
for all m:
Remark 5.2
In some applications a numerical sequence is indexed as fxngy
n¼0 rather
than fxngy
n¼1.
Note that the notion of a numerical sequence requires both a countable infinite
collection of numbers as well as an ordering on this collection. For example, while
the collection of rational numbers is, as we have seen, a countably infinite collection
of real numbers, it is not a numerical sequence until an ordering has been imposed.
One such ordering was introduced in section 2.1.4 on rational numbers to prove
countability, although this ordering counted each rational infinitely many times.
However, there are infinitely many other orderings, in fact uncountably many.
Order is particularly important because one is generally interested in whether or
not the numerical sequence ‘‘converges’’ as n ! y. For example, even without a for-
mal definition of convergence, it is intuitively clear that the following sequences be-
have as indicated:
Example 5.3
1. ym 1 1
m converges to 0 as m ! y.
2. xn 1 ð1Þ n
n
converges to 0 as n ! y.
3. aj 1 j1
j converges to 1 as j ! y.

4. cj 1 ð1Þ j j1
j does not converge as j ! y.
5. zn 1
2n5
4nþ1000 þ
3n3
5n3þ6 { converges to 0:5 þ 0:6{ as n ! y.
6. bn 1
m;
n ¼ 2m
m;
n ¼ 2m þ 1

does not converge as n ! y.
7. wk 1 k diverges to y as k ! y.
8. uj ¼ j2 diverges to y as j ! y.
On an intuitive level, cases 1 and 3 of example 5.3 not only converge, but converge
monotonically, which is to say that both sequences get closer to their respective limits
at each increment of the index. Case 2 also converges but not monotonically because
of the alternating signs. Case 4 ‘‘almost’’ converges, in that ‘‘half’’ of the sequence is
converging to a limit of þ1, while the other half is converging to a limit of 1. Spe-
cifically, case 4 has two convergent subsequences:
fyng 1 fc2ng ! 1;
fy0
ng 1 fc2n1g ! 1:
That case 5 converges is made more transparent by rewriting the rational func-
tions, for example,
2n  5
4n þ 1000 ¼
2  5
n
4 þ 1000
n
;
which converges to 1
2 . Cases 6, 7, and 8 all ‘‘explode’’ in a sense, but cases 7 and 8
seem to be reasonable candidates for a definition of converge to y, or converge to
y, for which we will use the language diverge toGy.
These examples provide a range of sample behaviors for numerical sequences.
After formalizing the definition of convergence that will capture the intuition of all
convergent examples, we will develop several properties of numerical sequences and
see that the comment above on case 4 generalizes. That is, any bounded numerical
sequence has at least one convergent subsequence.
5.1.2
Convergence of Sequences
The following definition of convergence of a numerical sequence is formal, and will
be discussed below to provide additional intuition. But at this point, we note the key
intuitive idea that this formality is attempting to capture. The notion of convergence
xn ! x means more than just ‘‘as n increases, there are terms xn that get arbitrarily
146
Chapter 5
Sequences and Their Convergence

close to x.’’ This is a notion that is weaker than convergence and will be addressed
below. The stronger property defined here is that ‘‘as n increases, all terms xn get ar-
bitrarily close to x.’’ More precisely:
Definition 5.4
A numerical sequence fxng converges to the limit x as n ! y if for
any  > 0 there is an N 1 NðÞ so that
jxn  xj < 
whenever
n b N:
ð5:1Þ
In this case we write
lim
n!y xn ¼ x
or
xn ! x:
In (5.1) the notation jxn  xj is to be interpreted in terms of the standard norm in R
and C given in (2.3) and (2.2), respectively. A real sequence fxng diverges to y as
n ! y if for any M > 0 there is N 1 NðMÞ so that
xn b M
whenever
n b N;
and diverges to y as n ! y if for any M > 0 there is N 1 NðMÞ so that
xn a M
whenever
n b N:
In these cases we write, as appropriate,
lim
n!y xn ¼Gy
or
xn !Gy;
In all other cases we say that fxng diverges as n ! y, or simply, does not converge.
Definition 5.5
A real sequence fxng is monotonic if any of the following conditions
are satisfied:
xn < xnþ1 for all n: strictly increasing
xn a xnþ1 for all n: increasing, or nondecreasing
xn > xnþ1 for all n: strictly decreasing
xn b xnþ1 for all n: decreasing, or nonincreasing
A real sequence fxng converges monotonically to the limit x as n ! y if fxng is mono-
tonic and converges to the limit x as n ! y.
Note that while convergence of a complex sequence is easily defined with the same
notation as that for a real sequence, as was noted in section 2.1.6 on complex num-
bers, there is no ordering of C as there is in R, and hence one does not have the
5.1
Numerical Sequences
147

notion of a monotonic complex sequence or that of monotonic convergence. Note
also that again with the exception of monotonicity, these definitions generalize with-
out change to vector sequences xn A Rn, only where (2.3) is replaced by the standard
norm in (3.3). Moreover this notion of convergence only depends on the norm up to
equivalence. So, if xn ! x under the standard norm, it will also converge relative to
the lp-norms for 1 a p a y, or any other equivalent norm. This more general notion
will be discussed below.
Remark 5.6
The concept in the definition above, that ‘‘for any  > 0 there is an
N 1 NðÞ,’’ can be a di‰cult one to grasp initially. But this theme is repeated time
and again in the following chapters, so we pause a moment here to develop it a bit fur-
ther. The di‰culty some have is that the intuitive notion of a limit, that
“xn gets closer to x as n gets large”
seems simple enough. But the detail that needs to be addressed is:
 Does convergence mean that we can find values of xn that get arbitrarily close to x?
 Or does convergence mean that all values of xn eventually get arbitrarily close to x?
For some purposes, the former weaker definition may su‰ce, and this idea is essen-
tially captured in the notion of accumulation point or limit point introduced in section
4.2.5. But for many applications we want the stronger definition of convergence in that
not just some xn get arbitrarily close to x as n ! y, but all xn get arbitrarily close to x
as n ! y. This is the reason to insist that jxn  xj <  for all n b N.
The formal definition of convergence may seem to suggest that we can randomly
generate any , and as long as there is an associated N with the needed property, we
are done and have proved convergence. Actually the terminology ‘‘for any  > 0
there is an N 1 NðÞ’’ is not to be interpreted as if  is arbitrarily selected by the
mathematician. The idea is instead that the mathematician wants to be sure that
there is a sequence of epsilons j ! 0, for example, j ¼ 1
j , so that for every term in
that sequence, an associated Nj 1 NðjÞ can be found, resulting in jxn  xj < j
whenever n b Nj. In other words, for any such j there is an Nj so that all terms of
the sequence from term xNj onward are closer to x than j. Logically, as j ! 0, we
expect to have that Nj ! y. That is, as one insists that sequence values be increas-
ingly close to their limit, it may be necessary to exclude more and more of the
sequence’s initial terms. So a good intuitive model for the expression ‘‘for any  > 0
there is an N 1 NðÞ so that . . .’’ is that ‘‘there is a sequence of epsilons, j ! 0, and
associated Nj 1 NðjÞ, so that . . . .’’
148
Chapter 5
Sequences and Their Convergence

The payo¤ from this definition is that one immediately has error bounds
j < x  xn < j
as long as n b Nj, so any such xn could be used as an approximation to x with the
error bounded as noted.
Example 5.7
Let’s prove the convergence of cases 3 and 5 in example 5.3 above to the
intuited limits of 1 and 0:5 þ 0:6i. First o¤, for case 3,
jaj  1j ¼ 1
j :
Given  > 0, to have jaj  1j <  then requires that j > 1
 . So N is chosen as any inte-
ger that exceeds this value. For case 5 of example 5.3, we use the triangle inequality,
and recalling that jij ¼ 1, we write
jzn  ð0:5 þ 0:6iÞj ¼
555
4n þ 1000 
0:36
5n3 þ 6 i


a
555
4n þ 1000 þ
0:36
5n3 þ 6
<
556
4n þ 1000 :
This last inequality follows since 5n3 þ 6 > 4n þ 1000 for n > 10, say, and this is good
enough. Given  > 0, to have jzn  ð0:5 þ 0:6iÞj <  requires that n > 5561000
4
. So N is
chosen to exceed this value.
5.1.3
Properties of Limits
The first observation about the definition of convergence, which is not true for the
weaker notion of accumulation point, is that if a numerical sequence converges, the
limit must be unique.
Proposition 5.8
If limn!y xn ¼ x and limn!y xn ¼ x0, then x ¼ x0.
Proof
This result is obvious if x ¼Gy: by definition, a sequence cannot have both
a finite limit and diverge to Gy, nor can it have both y and y as limits. If x and
x0 are both finite, then for any  > 0, there is an N 1 NðÞ so that jxn  xj <  and
jxn  x0j <  for n b N. Actually the definition of limit assures the existence of N1
and N2, one for each limit, so we simply define N ¼ maxðN1; N2Þ. By the triangle
inequality,
5.1
Numerical Sequences
149

jx  x0j a jx  xnj þ jxn  x0j < 2:
As this is true for any  > 0, we conclude that x ¼ x0.
n
The next observation concerning convergence is that convergence implies
boundedness.
Proposition 5.9
Let fxng be a convergent numerical sequence with xn ! x; then fxng
is bounded.
Proof
Fix any  > 0, for example,  ¼ 1, and let N be the associated integer so that
jxn  xj < 1 whenever n b N. Then by the triangle inequality,
jxnj ¼ jxn  x þ xj < 1 þ jxj
for n b N:
For n < N, jxnj a maxnaNjxnj, which is also finite. So all jxnj are bounded by the
larger of 1 þ jxj and maxnaNjxnj.
n
Remark 5.10
Note that case 4 of example 5.3 above shows that boundedness does not
guarantee convergence.
It is relatively easy to show that the notion of convergence is preserved under
arithmetic operations:
Proposition 5.11
Let fxng and fyng be convergent numerical sequences with xn ! x,
and yn ! y, and let a be a real or complex number. Then:
1. axn ! ax.
2. xn þ yn ! x þ y.
3. xnyn ! xy.
4.
1
yn ! 1
y as long as y 0 0, and yn 0 0 for all n.
5. xn
yn ! x
y as long as y 0 0, and yn 0 0 for all n.
Proof
In each case we show that convergence is guaranteed by convergence of the
original sequences:
1. jaxn  axj ¼ jaj jxn  xj by either (2.3) or (2.2), so assuming a 0 0, jaxn  axj < 
if jxn  xj < 
jaj . If a ¼ 0, there is nothing to prove.
2. jðxn þ ynÞ  ðx þ yÞj a jxn  xj þ jyn  yj by the triangle inequality in (2.7), so
jðxn þ ynÞ  ðx þ yÞj <  if each of the absolute values on the right-hand side are
bounded by 
2 .
150
Chapter 5
Sequences and Their Convergence

3. Again,
by
the
triangle
inequality,
jxnyn  xyj a jxnyn  xnyj þ jxny  xyj ¼
jxnj jyn  yj þ jyj jxn  xj. So if y 0 0, jxnyn  xyj <  if jyn  yj < 
2B , where B is
an upper bound for fjxnjg, and jxn  xj <

2jyj . If y ¼ 0, the second term drops out.
4.


 1
yn  1
y


 ¼


yny
yyn


. Now, since y 0 0 and yn 0 0 for all n, we can take  ¼ 0:5jyj.
We know that by convergence yn ! y, there is an N so that jyn  yj < 0:5jyj for
n > N0. Now for n > N0, jynj > 0:5jyj, and so jynyj > 0:5jyj2 and


 1
yn  1
y


 < 2jynyj
jyj2
.
Given arbitrary  > 0, we have that


 1
yn  1
y


 <  for n b maxðN; N0Þ, if N is chosen to
have jyn  yj < 0:5jyj2.
5. This follows from parts 3 and 4, since xn
yn ¼ xn
1
yn
 	
.
n
While we have seen by example that boundedness does not guarantee convergence,
we have the following result that boundedness assures the existence of a convergent
subsequence, generalizing case 4 of example 5.3 above.
Proposition 5.12
Let fxng be a bounded numerical sequence. Then there is a subse-
quence fymg H fxng and y so that ym ! y.
Proof
Because both R and C are metric spaces under the standard norms defined
in (2.3) and (2.2), we have by proposition 5.9 that there is a closed ball in R or C so
that fxng H BRð0Þ for some R. By the Heine–Borel theorem, closed balls are com-
pact in both R and C, so we can apply proposition 4.17 that any infinite collection
of points in a compact set must have an accumulation point. That is, fxng has an
accumulation point y A BRð0Þ. So for any r > 0, BrðyÞ V fxng 0 j. Next we choose
rm ! 0, and for each m choose an arbitrary ym A BrmðyÞ V fxng. Then ym ! y, since
for any  > 0 we can choose any rN < , and by construction, ym A BrNðyÞ for all
m b N. That is, jym  yj <  for all m b N.
n
The apparent arbitrariness in this proof implied by ‘‘choose an arbitrary ym A
BrmðyÞ V fxng’’ may surprise the reader. However, not only will there be for a given
y many sequences fymg with ym ! y, but there may also be many such accumula-
tion points y. For example, every point of the sequence can be an accumulation
point, and moreover the total number of such accumulation points may be uncount-
ably infinite.
Example 5.13
Let fxng be an arbitrary enumeration of the rational numbers in ½0; 1.
Then every y A ½0; 1 is an accumulation point. This is easily seen by taking an arbi-
trary y ¼ 0:d1d2d3 . . . as a decimal expansion. If y is a rational number ending in all
0s, we first rewrite this as an equivalent decimal ending in all 9s. For example, 0:5 ¼
0:49999 . . . . The subsequence is then formed by looking at the rational truncations of r:
5.1
Numerical Sequences
151

0:d1; 0:d1d2; 0:d1d2d3; 0:d1d2d3d4; . . . :
Define y1 ¼ 0:d1. Clearly, 0:d1 ¼ xn1 for some n1. The next term of the subsequence,
y2, is the first decimal truncation, 0:d1d2d3 . . . dm, so that 0:d1d2d3 . . . dm ¼ xn2, where
n2 > n1. Continuing in this way, we obtain a subsequence fymg with ym ! y.
*5.2
Limits Superior and Inferior
The preceding example illustrates that a bounded numerical sequence not only has
an accumulation point as well as a subsequence convergent to that accumulation
point, but that it may have a great many such accumulation points. For this reason
the notions of limit superior and limit inferior of a sequence have been introduced.
These are defined to equal the least upper bound or l.u.b., and greatest lower bound,
or g.l.b., respectively, of the collection of accumulation points, although unfortu-
nately, not in an immediately transparent way. A small but important application
of these notions will be seen in chapter 6 in the statement of the ratio test for series
convergence.
In addition these notions of limits have great utility in the advanced topic of real
analysis. But rather than deferring their introduction to that more abstract context,
we introduce limits superior and inferior here where the essence of these ideas is
more transparent.
Before defining formally and justifying the interpretations of limits superior and
inferior, we first define the l.u.b. and g.l.b. and introduce alternative notation.
Definition 5.14
Let fxag be a collection of real numbers. The least upper bound or
supremum is defined by
l:u:b:fxag ¼ supfxag 1 minfx j x b xa for all ag:
ð5:2Þ
If fxag is unbounded from above, we define l:u:b:fxag ¼ supfxag 1 y. The greatest
lower bound or infimum is defined by
g:l:b:fxag ¼ inffxag 1 maxfx j x a xa for all ag:
ð5:3Þ
If fxag is unbounded from below, we define g:l:bfxag ¼ inffxag 1 y.
Notation 5.15
It is common to write l:u:b: as lub and g:l:b: as glb.
Next we state the formal definitions of the limits superior and inferior, and then
work toward the demonstration that these achieve the stated objective concerning
the g.l.b. and l.u.b. of accumulation points of the given sequence.
152
Chapter 5
Sequences and Their Convergence

Unfortunately, this is another example of where a lot of carefully positioned words
are needed to define an idea that has a relatively simple intuitive meaning.
Definition 5.16
Let fxng be a numerical sequence. If supfxng ¼ y, meaning there
exists no U so that xn a U for all n, then we define the limit superior of fxng to be
y, and denote this as
lim sup
n!y
xn ¼ y:
If there exists a U so that xn a U for all n, let Un ¼ supmbnfxmg and define
lim sup
n!y
xn ¼ lim
n!y Un:
ð5:4Þ
Similarly, if inffxng ¼ y, meaning there exists no L so that L a xn for all n, then we
define the limit inferior of fxng to be y, and denote this as
lim inf
n!y
xn ¼ y:
If there exists an L so that L a xn for all n, let Ln ¼ infmbnfxmg and define
lim inf
n!y
xn ¼ lim
n!y Ln:
ð5:5Þ
Notation 5.17
In some mathematical references, the limit superior of fxng is denoted
by limn!y xn, and the limit inferior of fxng is denoted by limn!y xn, but throughout
this book we will use the more explicit notation above.
Before demonstrating that these rather abstract definitions provide the l.u.b. and
the g.l.b. of the collection of accumulation points of the sequence, we address a tech-
nicality within the definition above. That is, both the definition of lim sup in (5.4) and
that of lim inf in (5.5) involve limits of sequences as n ! y. It is natural to wonder
why such limits exist when nothing but one-sided boundedness is assumed of the
original sequence fxng.
The following proposition provides the missing detail because both sequences, Un
and Ln, are monotonic as can be demonstrated by
Un ¼ sup
mbn
fxmg b
sup
mbnþ1
fxmg ¼ Unþ1;
ð5:6aÞ
Ln ¼ inf
mbnfxmg a
inf
mbnþ1fxmg ¼ Lnþ1:
ð5:6bÞ
Consequently Un is monotonically decreasing, and Ln monotonically increasing, al-
though in neither case must this monotonicity be strict.
5.2
Limits Superior and Inferior
153

The next result is that a monotonic sequence either converges, or diverges to Gy,
depending on whether it is bounded or unbounded.
Proposition 5.18
If fxng is monotonically decreasing, then limn!y xn ¼ y if this
sequence is unbounded from below; otherwise, there is an x such that limn!y xn ¼ x.
Similarly, if fxng is monotonically increasing, we have that limn!y xn ¼ y or
limn!y xn ¼ x, depending on whether this sequence is unbounded from above or
bounded, respectively.
Proof
The unbounded cases are straightforward. For example, if unbounded from
below, we have for any positive integer M there is an N so that xN a M, but by the
decreasing monotonicity assumption, we conclude that
xn a M
whenever
n b N;
and we have limn!y xn ¼ y. If bounded, we know from proposition 5.12 that
fxng has an accumulation point x and a subsequence fymg so that ym ! x. By defi-
nition of this convergence, we have that for any  > 0 there is an N 1 NðÞ so that
jym  xj <  when m b N. We now show that x is in fact the limit of the original se-
quence, and indeed limn!y xn ¼ x. First, choose N 0 defined by xN 0 ¼ yNþ1. Next, if
fxng is monotonically decreasing, for any n b N 0 choose ymðnÞ and ymðnÞþ1 so that
and ymðnÞþ1 a xn a ymðnÞ. Then
jxn  xj a jymðnÞ  xj < ;
since by assumption mðnÞ b N. The result is analogously proved in the opposite
monotonicity case, except that we have ymðnÞ a xn a ymðnÞþ1 and
jxn  xj a jymðnÞþ1  xj < :
n
We now return to the relationship between limits superior and inferior, and the ac-
cumulation points of the sequence fxng. Given the formality in the definitions, it may
not be apparent how the definition of limit superior and limit inferior captures the
intention set out earlier, that being, to define the g.l.b. and the l.u.b. of all the accu-
mulation points of fxng. The next proposition establishes this connection.
Proposition 5.19
Given a sequence fxng, let fzkg denote the set of accumulation
points. Then
lim sup
n!y
xn ¼ l:u:b:fzkg;
ð5:7aÞ
lim inf
n!y
xn ¼ g:l:b:fzkg:
ð5:7bÞ
154
Chapter 5
Sequences and Their Convergence

Proof
First o¤, if the sequence fxng is unbounded from above, then by defini-
tion, there is a subsequence fyng so that yn ! y and hence y A fzkg, but also
lim supn!y xn ¼ y. Similarly, if unbounded below, there is a subsequence fy0
ng so
that y0
n ! y, and we conclude that y A fzkg, but also lim infn!y xn ¼ y. So
in these cases the intended goal regarding the collection of accumulation points is
achieved. On the other hand, if bounded above, then since the sequence fUng must
be monotonically decreasing, it has a finite limit or diverges to y by the proposi-
tion above. If Un ! U 0, a finite limit, we claim that U 0 is the supremum or l.u.b. of
all accumulation points. To see this, we have by definition of Un ! U 0, that for any
 > 0 there is an N so that jUn  U 0j <  for n b N. Now, since Un ¼ supmbnfxmg,
we can find a value of xmðnÞ so that jUn  xmðnÞj < 1
n , say. Define yn 1 xmðnÞ. Then we
have that yn ! U 0, since by the triangle inequality,
jyn  U 0j a jyn  Unj þ jUn  U 0j <  þ 1
n ;
and hence U 0 A fzkg. Also there can be no subsequence fy0
ng so that y0
n ! U 00 with
U 00 > U 0, since by definition of Un we have Un b supfy0
j j y0
j ¼ xm and m b ng.
Hence, since Un ! U we cannot have y0
n ! U 00 with U 00 > U 0.
The cases where Un ! y, Ln ! L0 < y, and Ln ! y are reasoned similarly.
n
Example 5.20
Define the sequence
xn ¼
3  ð1=nÞn;
n ¼ 3m,
ð1Þnððn þ 1Þ=nÞ;
n ¼ 3m þ 1
ð3=4Þn;
n ¼ 3m þ 2.
8
>
<
>
:
; m ¼ 0; 1; 2; . . . ;
This sequence has four accumulation points. The subsequence with n ¼ 3m converges to
3, the subsequence with n ¼ 3m þ 1 has two subsequences that converge to 1 and þ1,
and the subsequence with n ¼ 3m þ 2 converges to 0. So we conclude that by the prop-
osition above, it must be the case that lim supn!y xn ¼ 3 and lim infn!y xn ¼ 1.
Now
Un ¼ sup
mbn
fxmg ¼ 3 þ
1
n0

n 0
;
Ln ¼ inf
mbnfxmg ¼  n00 þ 1
n00
;
5.2
Limits Superior and Inferior
155

where n0 ¼ minf3m j 3m b n and 3m is eveng and n00 ¼ minf3m þ 1 j 3m þ 1 b n and
3m þ 1 is oddg. We see that each of fUng and fLng are convergent monotonic se-
quences, and that Un ! 3 and Ln ! 1.
In summary, we conclude from this proposition that the limit superior equals the
supremum of all accumulation points, and the limit inferior the infimum of all ac-
cumulation points of fxng. Based on this result, the following proposition’s conclu-
sion cannot be a surprise. In theoretical applications this result can provide a useful
and powerful way of finding the limit of a convergent sequence, since it is sometimes
the case that the limits superior and inferior are easier to estimate than the ac-
tual limit itself, as each allows one to focus on what is often a more manageable
subsequence.
Proposition 5.21
Let fxng be a numerical sequence. Then, for y a x a y,
limn!y xn ¼ x if and only if
lim inf
n!y
xn ¼ lim sup
n!y
xn ¼ x:
Proof
We consider three cases. The proof is a good example of ‘‘following the def-
inition’’ to the logical conclusion:
1. For x ¼ y, if xn ! y, then for any M there is an N so that xn b M for n b N.
Hence fxng is unbounded from above and lim supn!y xn ¼ y. Also Ln ¼
infmbnfxmg b M, for n > N, so Ln ! y as n ! y. That is, lim infn!y xn ¼ y.
Conversely, if lim infn!y xn ¼ lim supn!y xn ¼ y, then Ln ¼ infmbnfxmg ! y as
n ! y. That is, for any M there is an N so that Ln b M for n b N. Hence, by def-
inition of Ln; xn b M for n b N and xn ! y.
2. For x ¼ y, the argument is identical.
3. For y < x < y, if xn ! x, then for any  there is an N so that jxn  xj <  for
n b N. That is, x   < xn < x þ  for n b N, and hence x   < Ln, Un < x þ , and
we conclude that lim infn!y xn ¼ lim supn!y xn ¼ x. Conversely, lim infn!y xn ¼
lim supn!y xn ¼ x implies that for any  there is an N so that jLn  xj <  and
jUn  xj <  for n b N, and hence by the definition of Un and Ln, we conclude that
jxn  xj <  for n b N and xn ! x.
n
The next result says that the interval with endpoints equal to the limits superior
and inferior, if expanded arbitrarily little, will contain all but finitely many values of
the original sequence fxng.
156
Chapter 5
Sequences and Their Convergence

Proposition 5.22
If LS ¼ lim supn!y xn and LI ¼ lim infn!y xn, then for any  > 0
there is an N so that for all n b N,
LI   a xn a LS þ :
ð5:8Þ
Proof
We proceed with a proof by contradiction, illustrating the upper inequality.
Assume that for some  > 0 there are infinitely many sequence terms satisfying
xj > LS þ . Then, for any n, Un ¼ supmbnfxmg > LS þ , and hence lim supn!y xn
¼ limn!y Un b LS þ , contradicting the definition of LS.
n
Example 5.13 discussed above, on an arbitrary enumeration of rationals in ½0; 1,
also introduces an issue that will play a critically important role in subsequent chap-
ters. That being, if a sequence fxng H X, where X is a subset of R or C and where
xn ! x, is x necessarily an element of this subset? The answer is ‘‘no,’’ and we pro-
vide two examples of what can happen.
Example 5.23
1. If X ¼ ð0; 1Þ, then both
1
n
 
and
1  1
n


converge, but not to a point in X. On the
other hand, any convergent sequence fxng H ½a; b H ð0; 1Þ must converge to a point
in X.
2. If X ¼ Q, the rational numbers, then as example 5.13 demonstrates, some sequences
converge to a point in X and some converge to a point outside X.
In the next section we generalize the notion of sequence to an arbitrary metric
space where x A X becomes an explicit component of the criterion for convergence.
*5.3
General Metric Space Sequences
The preceding section focused on properties of numerical sequences. However, if one
reviews the various proofs, it becomes clear that with one exception, no special prop-
erty of R or C is used other than the existence of a metric or distance function,
dðx; yÞ ¼ jx  yj, which was used as a measure of ‘‘closeness.’’ The one special prop-
erty of R or C we used was the Heine–Borel theorem, which assures us that a
bounded sequence lies in a compact set and hence has a convergent subsequence.
Consequently it should be expected that we can define sequences fxng H Rn and
their convergence under the standard metric, defined by (3.18), or under any one of
the lp-norms defined in (3.10). This notion of convergence would satisfy all the prop-
erties in the preceding section, since in this context we once again have the benefit
5.3
General Metric Space Sequences
157

of the Heine–Borel theorem. Moreover the notion of convergence under equivalent
metrics d and d 0 are identical. Namely xn ! x under d if and only if xn ! x under d 0.
More generally, if fxng H X, where ðX; dÞ is a general metric space, convergence
can again be defined, and virtually all properties are satisfied. In this general context,
however, the definition of convergence must explicitly require that x A X. That is be-
cause for a general metric space if fxng H X and x B X, the notion of dðxn; xÞ <  is
not well defined. Also we note that we have two issues in this general metric space
setting that do not exist in R, Rn, or C:
1. In a general metric space, numerical operations like addition may not be defined.
If they are defined, the proposition above on arithmetic operations on sequences with
limits remains valid.
2. In a general metric space, we do not necessarily have the Heine–Borel theorem.
That is, a closed and bounded set need not be compact (the converse is true as
proved in proposition 4.17). Consequently a bounded sequence need not be con-
tained in a compact set, and hence it need not have a convergent subsequence.
In this section we document definitions and properties, the latter generally without
proof, which the reader can supply as an exercise by redeveloping the arguments
above.
Definition 5.24
Let ðX; dÞ be a metric space. A sequence, denoted fxng, fzjg, and so
forth, is a countably infinite collection of elements of X for which a numerical ordering
is specified:
fxng 1 x1; x2; x3; . . . :
A sequence is bounded if there is a number D and an element y A X so that dðy; xnÞ a D
for all n. A subsequence of a sequence is a countably infinite subcollection that pre-
serves order. That is, fymg is a subsequence of fxng if
ym ¼ xnm
and
nmþ1 > nm
for all m:
We begin by noting that in the definition of bounded, there is nothing special
about the identified y.
Proposition 5.25
If fxng H X, a metric space, and fxng is bounded, then for any
y0 A X there is a Dðy0Þ so that dðy0; xnÞ a Dðy0Þ for all n.
Proof
Let y and D be given as in the definition of bounded, and let y0 A X be arbi-
trary. Then by the triangle inequality,
158
Chapter 5
Sequences and Their Convergence

dðy0; xnÞ a dðy0; yÞ þ dðy; xnÞ a dðy0; yÞ þ D:
Hence Dðy0Þ ¼ dðy0; yÞ þ D.
n
Next we define convergence.
Definition 5.26
A sequence fxng H ðX; dÞ, a metric space, converges to a limit x A X
as n ! y if for any  > 0 there is an N 1 NðÞ so that
dðxn; xÞ < 
whenever
n b N;
ð5:9Þ
and in this case we write
lim
n!y xn ¼ x
or
xn ! x:
If fxng does not converge, we say it diverges as n ! y, or simply does not converge.
We note in the general context of a metric space, which of course includes R, C,
and Rn, that the concept of convergence is not as metric dependent as it first appears.
We state the result for equivalent metrics, also called topologically equivalent, but
recall this will also be true for Lipschitz equivalent metrics, since this latter notion
implies the former by proposition 3.41.
Proposition 5.27
Let X be a metric space under two equivalent metrics, d1 and d2.
Then a sequence fxng H X converges to x in ðX; d1Þ i¤ fxng converges to x in ðX; d2Þ.
Proof
Since xn ! x in ðX; d1Þ, we have that for any 0 > 0 there is an N 1 Nð0Þ
so that d1ðxn; xÞ < 0 whenever n b Nð0Þ. In other words, fxngy
n¼Nð 0Þ H Bð1Þ
 0 ðxÞ, the
open ball about x of d1-radius 0. To show convergence in ðX; d2Þ, let  > 0 be given.
By (3.35) there is an 0 so that Bð1Þ
 0 ðxÞ H Bð2Þ
 ðxÞ. But from above, we have for this 0,
fxngy
n¼Nð 0Þ H Bð1Þ
 0 ðxÞ H Bð2Þ
 ðxÞ;
so d2ðxn; xÞ <  for n b Nð0Þ. The reverse demonstration is identical.
n
We now record these convergence results in this general context, where ðX; dÞ is a
given metric space.
Proposition 5.28
If fxng H X is a convergent sequence with limn!y xn ¼ x and
limn!y xn ¼ x0, then x ¼ x0.
Proposition 5.29
If fxng H X is a convergent sequence with fxng ! x, then fxng is
bounded.
5.3
General Metric Space Sequences
159

The next proposition requires a caveat, because a general metric space need not
have arithmetic operations. Recall that by definition, X can be any collection of
points on which a metric is defined. However, many metric spaces of interest are vec-
tor spaces that at least allow addition and scalar multiplication, so we record this
result without proof as the proof is identical to that above. These vector spaces are
called (real or complex) linear metric spaces, depending on whether the vector space
structure is over the real or complex numbers. Of course, Rn is the classic example of
a real linear metric space, and correspondingly Cn is the classic example of a com-
plex linear metric space.
Proposition 5.30
Let fxng and fyng be convergent sequences in a linear metric space
X with fxng ! x, and fyng ! y, and let a be a scalar. Then we have:
1. axn ! ax.
2. xn þ yn ! x þ y.
As noted above, a bounded sequence in a general metric space need not be con-
tained in a compact subset of that metric space. It will be contained in a closed and
bounded subset, but in general, this does not necessarily imply compact. Hence, if
this sequence is not contained in a compact set, it need not have an accumulation
point and hence need not have a convergent subsequence. One approach to ensuring
that every bounded sequence is contained in a compact subset is to introduce the no-
tion of a compact metric space.
Definition 5.31
A metric space ðX; dÞ is compact if every open cover of X contains a
finite subcover.
Proposition 5.32
Let fxng H Rn be a bounded sequence, or fxng H X a general se-
quence in a compact metric space. Then there is a subsequence fymg H fxng so that
ym ! y where y A Rn in the first case, and y A X in the second.
Proof
In the first case, boundedness implies that fxng H BRðxÞ for any x A Rn,
where R in general depends on x. Now in Rn, BRðxÞ is closed and bounded and
hence compact by the Heine–Borel theorem, so an accumulation point exists in
BRðxÞ by proposition 4.17. Consequently a convergent subsequence can be con-
structed as in proposition 5.12. If X is compact, we argue by contradiction and as-
sume that there is no such accumulation point. Then about each point xn, an open
ball can be constructed, BrnðxnÞ, that contains no other point of the sequence. We de-
fine the set A by A 1 X @ ½6 Brn=2ðxnÞ, which is open since the complement of A in
160
Chapter 5
Sequences and Their Convergence

X is the closed set ½6 Brn=2ðxnÞ. With A and fBrnðxnÞg we now have an open cover
of X that admits no finite subcover, since each BrnðxnÞ contains only one point of X.
This contradicts that X is compact, and hence fxng must have an accumulation point
in X.
n
It may not be surprising, at least on an intuitive level, that in a compact
metric space a sequence has a subsequence that clusters around some point and
‘‘wants’’ to converge to this point. What should be surprising in this general case is
that this subsequence converges to a point y A X. The question is, why can X have
no ‘‘holes’’ so that the bounded sequence converges to the hole and not to a point
in X?
Example 5.33
Using the standard metric, imagine the ‘‘apparently compact’’ metric
space X 1 ½0; 1 V Q made up of all rational numbers q with 0 a q a 1. It is easy to
produce a sequence in X that converges to a hole, which would be an irrational
y A ½0; 1, simply by defining this sequence in terms of the rational decimal approxima-
tions to y. This appears to contradict proposition 5.32, so it is best to evaluate our
assumptions more carefully. Since X is clearly a metric space under the standard met-
ric, it must be compactness that is in question. Is X compact?
To be compact, it must be the case that any open cover of X admits a finite open
subcover. So there must be an infinite open cover that cannot be so reduced. Recall
how such a cover was constructed in exercise 12 of chapter 4 to show that ð0; 1Þ was
not compact. The trick was that since 0 did not need to be covered, a collection of
slightly overlapping open intervals could be constructed that collectively covered all
real numbers between 0 and 1, but no finite subcover accomplished this. That same trick
works here, since we can split X using any irrational y as
X ¼ ½½0; yÞ V Q U ½ðy; 1 V Q:
Now the construction of that exercise can be applied to ½0; yÞ and ðy; 1 since neither is
compact, producing an open cover of ½0; yÞ U ðy; 1 that has no finite subcover. As this is
also now an open cover for X that has no finite subcover, we have demonstrated that X
is not compact.
An alternative and simpler argument to show that a compact metric space can
have no holes is to apply what we know from proposition 4.17, that a compact set
is closed and hence it must contain all its limit points. It is apparent that X in the
example above does not contain all its limit points, so it is not closed and cannot be
compact.
5.3
General Metric Space Sequences
161

5.4
Cauchy Sequences
5.4.1
Definition and Properties
In practice, given a sequence fxng H X, where X is Euclidean or a metric space, the
principal challenge in applying the definition for convergence is that this definition
requires knowledge of the limiting value x. The notion of a Cauchy sequence, named
for Augustin Louis Cauchy (1759–1857), allows one to determine in many cases if a
sequence converges without first knowing its limiting value. The key defining idea is
that all pairs of points in the sequence will be found to be arbitrarily close if the index
values are required to exceed some value. Specifically:
Definition 5.34
A sequence fxng H X, where ðX; dÞ is a metric space, is a Cauchy
sequence, or satisfies the Cauchy criterion, if for any  > 0, there is an N ¼ NðÞ so
that
dðxn; xmÞ < 
whenever
n; m b N:
ð5:10Þ
Example 5.35
1. Consider the sequence in case 3 of example 5.3: aj 1 j1
j . Then by the triangle
inequality,
jan  amj ¼ n  m
mn


a 1
n þ 1
m :
Consequently, to have jan  amj < , choose n; m > 2
 . In other words, define N as any
integer which exceeds 2
 .
2. Consider the sequence defined by the harmonic series: xn ¼ Pn
j¼1
1
j . Then given m,
consider n ¼ 2m:
jx2m  xmj ¼
X
2m
j¼mþ1
1
j > m
1
2m


¼ 1
2 :
In other words, no matter how large m is, the sum of the terms from m to 2m exceeds 1
2 ,
so this sequence is not a Cauchy sequence and cannot converge. Since this sequence is
apparently monotonically increasing, we conclude that xn ! y.
We note that in the general context of a metric space, which of course includes R,
C, Rn, and Cn, the concept of a Cauchy sequence is not as metric-dependent as it
first appears.
162
Chapter 5
Sequences and Their Convergence

Proposition 5.36
Let X be a metric space under two equivalent metrics, d1 and d2.
Then a sequence fxng H X is a Cauchy sequence in ðX; d1Þ i¤ fxng is a Cauchy se-
quence in ðX; d2Þ.
Proof
The proof is identical to that in proposition 5.27 for convergence of a se-
quence and is given as exercise 13(a).
n
The definition of a Cauchy sequence is somewhat more complex than that of con-
vergence to x because the condition in (5.10) applies to all pairs ðn; mÞ of indexes that
exceed N rather than the simpler statement concerning all single indexes that exceed
N. This definition can be reframed in a logically more simple statement, although
this is rarely if ever so noted. The proof of the equivalence of these definitions is
assigned in exercise 7.
Definition 5.37
A sequence fxng H X, where ðX; dÞ is a metric space, is a Cauchy
sequence, or satisfies the Cauchy criterion, if for any  > 0, there is an N ¼ NðÞ so
that
dðxN; xnÞ < 
whenever
n b N:
ð5:11Þ
We next investigate the relationship between the property of a sequence converg-
ing and the property of a sequence being a Cauchy sequence. First o¤, we show that
just like convergent sequences, every Cauchy sequence in a metric space is bounded.
Proposition 5.38
If ðX; dÞ is a metric space and fxng H X a Cauchy sequence, then
fxng is bounded.
Proof
Let  > 0 be arbitrarily chosen. Since fxng is a Cauchy sequence, there is an
N so that dðxn; xmÞ <  whenever n; m b N. In particular, dðxn; xNÞ <  whenever
n b N. Now, if B ¼ maxn<N dðxn; xNÞ, then with x ¼ xN we have dðxn; xÞ <
maxð; BÞ for all n, and hence fxng is bounded.
n
It is easy to show that every convergent sequence is in fact a Cauchy sequence:
Proposition 5.39
If fxng H X, where X is a metric space and xn ! x, then fxng is a
Cauchy sequence.
Proof
By the triangle inequality,
dðxn; xmÞ a dðxn; xÞ þ dðx; xmÞ:
Now, if  > 0 is given, choose N so that dðxn; xÞ < 
2 for n b N. By the inequality
above we then have dðxn; xmÞ <  for n; m b N.
n
5.4
Cauchy Sequences
163

While this last result is of interest, the result of greater value in applications has to
do with the reverse implication. Namely, when does a Cauchy sequence converge?
The answer can be readily seen to be: ‘‘not necessarily.’’
Example 5.40
1. Let fxng ¼
1
n
 
in the metric space X ¼ ð0; 1Þ H R under the standard metric in
(3.18). This is a Cauchy sequence, and one readily verifies that dðxn; xmÞ <  whenever
n; m b N for any N > 1
 . However, it is clear that this sequence does not converge in
X. It is also clear that in this case X can be enlarged somewhat or completed, to its
closure X ¼ ½0; 1 in R, and in this metric space we obtain convergence.
2. In example 5.33 was introduced X ¼ Q V ½0; 1, under the standard metric, where it
was shown that for any real number y A ½0; 1 there was a sequence fyng H X so that
yn ! y. By the proposition above, all such sequences are Cauchy sequences. However,
these sequences only converge in X if y is chosen to be rational. Again, we see that this
metric space can be completed by enlarging it to X ¼ ½0; 1, and then all these Cauchy
sequences converge to a point in X.
To motivate the result below, note that we have shown that if fxng H X is a
Cauchy sequence in any metric space, then it is bounded. So the question of conver-
gence is closely related to the existence of an accumulation point, and we have seen
from the above that such an accumulation point can be assured if X ¼ R; C; Rn (as
well as Cn, though not proved) or if X is a compact metric space. Although the
results below that rely on the Heine–Borel theorem are also true in Cn, we will drop
this reference since this theorem was not proved in this case, and we do not need this
result in this book.
Proposition 5.41
If fxng H X is a Cauchy sequence, where X ¼ R; C; Rn, or X is a
compact metric space, then there is an x A X so that xn ! x.
Proof
In all cases we know that fxng is bounded. Also for any  > 0 there is an N
so that jxn  xmj <  for n; m b N. That is,
fxngy
n¼N A BðxNÞ:
Choose j ¼ 1
j , and let Nj be the associated integer. Then as j ! y,
fxngy
n¼Nj A B1=jðxNjÞ:
We now claim that there is a unique x A X so that 7j B1=jðxNjÞ ¼ x, and that xn ! x.
Of course, the latter conclusion follows from the existence of x, since we can con-
clude that for any j, x A BjðxNjÞ and hence for n > Nj,
164
Chapter 5
Sequences and Their Convergence

dðx; xnÞ a dðx; xNjÞ þ dðxn; xNjÞ < 2
j :
To demonstrate the intersection claim, first note that every finite collection of these
closed balls has a nonempty intersection, since all contain fxngy
n¼N where N ¼
maxfNjg, and this maximum is finite for any finite collection. Also the intersection
of all such balls cannot contain more than one point since the radius of these balls,
j ¼ 1
j converges to 0. To complete the proof, we show by contradiction that this infi-
nite intersection cannot be empty, and hence it contains the unique point x. Assume
that 7j B1=jðxNjÞ ¼ j and, in particular, f7jb2 B1=jðxNjÞg V B1ðxN1Þ ¼ j. Then with
Ac 1 ~
A, denoting the complement of A,
B1ðxN1Þ H
7
jb2
B1=jðxNjÞ
(
)c
¼ 6
jb2
~B1=jðxNjÞ;
by De Morgan’s laws. Now the set B1ðxN1Þ is compact either by Heine–Borel if
X ¼ R; C; Rn or as a closed set in the compact metric space X, and it is covered by
a union of open sets f ~B1=jðxNjÞgjb2. It therefore has a finite subcover, so B1ðxN1Þ H
6jaM ~B1=jðxNjÞ for some M. Again, using De Morgan’s laws, we conclude that
f72ajaM B1=jðxNjÞg V B1ðxN1Þ ¼ j, contradicting the observation above that every
finite collection of these balls has nonempty intersection.
n
Unfortunately, many of the general metric spaces of interest are not compact.
Hence we cannot, in general, conclude that Cauchy sequences converge to a point
in the space. Of course, R, C, and Rn are also metric spaces of great interest, and
are not compact, yet we have seen that in these cases Cauchy sequences do converge.
So compactness is not a necessary condition for the convergence of Cauchy se-
quences, but it is a su‰cient condition.
*5.4.2
Complete Metric Spaces
Because the property that Cauchy sequences converge to a point of the space is so
important in mathematics, special terminology has been introduced for metric spaces
that have this property.
Definition 5.42
Let ðX; dÞ be a metric space. Then X is said to be complete under d if
every Cauchy sequence in X converges to a point in X.
It should be noted that this notion of being complete is not just a property of the
space X, but it is explicitly specified as ‘‘complete under d.’’ This is because by the
5.4
Cauchy Sequences
165

very definition in (5.10) or (5.11) above, the metric d determines which sequences are
Cauchy sequences and therefore determines which sequences must converge in order
to satisfy the completeness criterion. However, as was seen above, the dependence on
the metric d is only up to metric equivalence. That is, X is complete under d if and
only if it is complete under d 0 for any metric equivalent to d.
Example 5.43
1. We have seen from the analysis above that R, C, and Rn are all complete under the
standard metrics defined in (2.3), (2.2), and (3.3), respectively.
2. Rn is also complete under all the lp-norms in (3.10) and (3.11), since these norms
are equivalent to the standard metric.
3. Every compact metric space is complete under its metric.
4. The metric space Q is not complete under the standard metric, nor is Q V ½0; 1, nor
is any bounded open interval, ða; bÞ.
5. The metric space Qn H Rn of rational n-tuples is not complete under the standard
metric, nor is Qn V BRðxÞ for any R and x, nor is BRðxÞ.
Because completeness of a metric space is so important in applications, yet so
often it is the case that a metric space of interest is not complete, it is of no surprise
that the question of completing a metric space has received considerable attention. In
the various examples above, it was obvious why the given spaces failed to be com-
plete, and equally obvious how one could solve this problem by adding to the space
the ‘‘missing’’ points that prevented the space from being complete in the first place.
For the examples above we note that what is interesting about these informal com-
pletions of the given spaces was that within the resulting completed spaces, the orig-
inal spaces were dense. In addition distances between points of the original spaces
were preserved in the completed spaces.
Alternatively, by looking at the incomplete space as a subspace of a larger space,
we could interpret the completion of the original space as the closure of that space in
the larger space that contained it. The completions in e¤ect just added the original
space’s accumulation points. For example, ða; bÞ is not complete, but the closure of
this interval in the metric space R, which is ða; bÞ ¼ ½a; b, is complete. Similarly,
while Q and Q V ½0; 1 are not complete metric spaces, we can create their closures
in R, where Q ¼ R, and Q V ½0; 1 ¼ ½0; 1, and these are complete. We can do the
same for Qn, Qn V BRðxÞ, and BRðxÞ in Rn.
The next proposition, which we state without proof, indicates that these examples
illustrate the general case. Namely every metric space can be embedded in a complete
166
Chapter 5
Sequences and Their Convergence

metric space in a way that preserves distances, and where the original space is dense
in the larger space. In addition, if the original space is already contained within a
complete metric space, then this completion is equivalent to the closure of the origi-
nal space.
Proposition 5.44
Let ðX; dÞ be a metric space. Then there is a complete metric space
ðX 0; d 0Þ so that ðX; dÞ is isometric to a dense subset of ðX 0; d 0Þ. That is, there is a dense
subset X 00 H X 0 and a one-to-one identification X 00 , X so that for any x00; y00 A X 00,
and identifications: x00 , x and y00 , y, with x; y A X, we have that
d 0ðx00; y00Þ ¼ dðx; yÞ:
Also, if under d there is a complete metric space, Y, with X H Y, then X 00 is isometric
to X, the closure of X in Y.
This proposition guarantees that any metric space ðX; dÞ of interest can be com-
pleted in a way that does not change the original space very much, which is the
meaning of the isometric identification. Also, if we are working with a space ðX; dÞ
that we know to be a subspace of a larger complete space Y, we can accomplish this
completion by forming the closure of X in Y, as was seen to be the case in the earlier
simpler examples.
5.5
Applications to Finance
The results of this chapter are to a large extent needed as an introduction to concepts
that underlie applicable mathematics in later chapters. For example, the notion of
convergence will be seen to be fundamental to much of what is to come. More di-
rectly, the notion of convergence of a sequence provides a context for understanding
what it means for an iterative numerical calculation to converge to the correct an-
swer, where in each step the calculation provides an approximate solution to a fi-
nance problem.
We return to the example of interval bisection next, extending the analysis origi-
nally introduced in section 4.3.3 for the evaluation of the yield to maturity of a
bond or other security o¤ered at a given price. Here we illustrate the general proce-
dure with a detailed bond yield example.
5.5.1
Bond Yield to Maturity
Assume that we are o¤ered a 1000 par, 10-year, 8% semiannual coupon bond at a
price of 1050. First o¤, we easily confirm that the yield to maturity (YTM) is less
5.5
Applications to Finance
167

than 8% on a semiannual basis because this bond is selling at a premium. The cash
flows on this bond are 40 per half year for 10 years, with an extra payment of 1000 at
time 10. So if r is the yield on a semiannual basis, we have from (2.16) that
PðrÞ ¼ 1000 þ 1000½0:5ð0:08  rÞa20;0:5r:
From this equation it is apparent that in order to have Pðr0Þ ¼ 1050, we need
r0 < 0:08.
We now detail an interval bisection approximation procedure and construct a se-
quence frjg, which we will prove is a Cauchy sequence. Consequently, without
knowing to what value this sequence converges, we will be able to assert that this se-
quence will indeed converge because R is complete. Moreover, because of the nature
of the approximation procedure, we will be able to calculate the rate at which con-
vergence is achieved, and hence how many steps are needed for any given degree of
accuracy. All this is doable without our ever knowing the exact answer.
To this end, for the first step we require two trial values of r, denoted rþ and r so
that
PðrþÞ < 1050 < PðrÞ:
In other words, since rþ provides too small a price, rþ > r0, where r0 is the desired
exact value, and similarly r < r0. That is,
r < r0 < rþ:
For this step we choose somewhat arbitrarily, since this process will always con-
verge, but not naively, since to do so increases the number of steps needed to get a
good approximation. An example of a naive initial set of values is rþ ¼ 1:00 (i.e.,
100%) and r ¼ 0. We can with a moment of thought do better with rþ ¼ 0:08 and
r ¼ 0:07, producing PðrþÞ ¼ 1000, and PðrÞ ¼ 1071:0620165. The first estimate of
r0 is then
r1 ¼ 0:5ðrþ þ rÞ;
which produces r1 ¼ 0:075.
For the second step, the process is to now evaluate Pðr1Þ. If Pðr1Þ < 1050,
r1 becomes the new rþ and we retain the former r. Otherwise, r1 becomes the
new r and we retain the former rþ. In either case we calculate the second estimate
of r0 as
168
Chapter 5
Sequences and Their Convergence

r2 ¼ 0:5ðrþ þ rÞ;
and the process continues into the third step and beyond. If at any step we find that
the calculated rn serendipitiously equals the exact answer, r0, the process stops. How-
ever, this virtually never happens to anyone, so we have no need to dwell on this
outcome.
The implementation of this algorithm to the bond yield problem yields the table of
results in table 5.1, where for visual appeal, yields are presented in percentage units,
on a semiannual nominal basis:
Now at each step, we have rn A ðr; rþÞ by definition, and for any r0 A ðr; rþÞ,
jr0  rnj a rþ  r
2
:
Since the lengths of these intervals halve at each step by construction, and for n ¼ 1
we have rþ  r ¼ 0:01, we conclude that for any r0 A ðr; rþÞ at the nth step,
jr0  rnj a 0:01
2n :
From this estimate we demonstrate that the sequence frjg is a Cauchy sequence, and
hence because R is complete by the analysis above, we conclude that there is an
r0 A ðr; rþÞ for all such intervals and that rj ! r0.
To this end, let m and n > m be given; then for r0 A In 1 ðr; rþÞ defined as the in-
terval produced as of the nth step, we also have r0 A Im 1 ðr; rþÞ defined as of the
mth step since In H Im. By the triangle inequality, with r0 A In V Im,
Table 5.1
Interval bisection for bond yield
Step
r
PðrÞ
rþ
PðrþÞ
rj
rþ  r
1
7.0000%
1071.06202
8.00000%
1000.00000
7.50000%
1.00000%
2
7.0000%
1071.06202
7.50000%
1034.74051
7.25000%
0.50000%
3
7.2500%
1052.69870
7.50000%
1034.74051
7.37500%
0.25000%
4
7.2500%
1052.69870
7.37500%
1043.66959
7.31250%
0.12500%
5
7.2500%
1052.69870
7.31250%
1048.17157
7.28125%
0.06250%
6
7.2813%
1050.43198
7.31250%
1048.17157
7.29688%
0.03125%
7
7.2813%
1050.43198
7.29688%
1049.30099
7.28906%
0.01562%
8
7.2813%
1050.43198
7.28906%
1049.86629
7.28516%
0.00781%
9
7.2852%
1050.14908
7.28906%
1049.86629
7.28711%
0.00391%
10
7.2871%
1050.00767
7.28906%
1049.86629
7.28809%
0.00195%
5.5
Applications to Finance
169

jrn  rmj a jrn  r0j þ jr0  rmj
a 0:01
2n þ 0:01
2m :
From this estimate we can, for any , choose N so that 0:01
2 N < 
2 , and conclude that
jrn  rmj < 
for n; m > N:
In other words, frjg is a Cauchy sequence, and hence there is an r0 A ðr; rþÞ for all
such intervals with rj ! r0.
From the error estimate above, true for all r0 A In, we derive the error estimate for
r0 by letting m ! y:
jr0  rnj a 0:01
2n :
ð5:12Þ
From (5.12) we can choose n to provide any given level of accuracy. For example, to
have k-decimal point accuracy, we need the error to be less than 5ð10k1Þ ¼ 10k
2 ,
that is,
0:01
2n < 10k
2
:
From this point we conclude that n must be chosen so that 2n1 > 10k2, which is
easily solved with logarithms.
This simple, yet powerful algorithm is known as the interval bisection algorithm. It
has the property that the error decreases geometrically with a factor of 1
2 . Note that
although the error in each step halves as is illustrated in the last column in table 5.1,
it is not the case that the sequence of estimators, frjg, monotonically converge to r,
as is seen from the second last column of this table. This conclusion is logical, since
in each step one of the values of r and rþ is replaced, and one is used in the next
step. Consequently, if r is replaced in a given step, that step’s estimate will exceed
the prior step’s estimate, and conversely.
5.5.2
Interval Bisection Assumptions Analysis
As was observed in section 4.3.3, the usefulness of this algorithm relies on subtle
assumptions about the objective function, here PðrÞ, but in general, f ðxÞ, where we
are attempting to solve
f ðxÞ ¼ c
170
Chapter 5
Sequences and Their Convergence

for some value c. The interval bisection algorithm produces a Cauchy sequence, fxjg,
which then has the property that xj ! x for some x A R typically, where by construc-
tion, for every sequence point either f ðxjÞ > c or f ðxjÞ < c.
The first subtlety in the application of interval bisection is that we are assuming
that because fxjg is a Cauchy sequence, this implies that f f ðxjÞg is a convergent se-
quence. This appears to be the case for the bond yield example in table 5.1, but
should this always be the case? Consider the next example where it is not initially fea-
sible to produce a complete picture of what the graph of a given function looks like.
Imagine that it is a complicated function that has been programmed in terms of
an iterative process. All that is possible is that by crunching the program for a given
value of y, the value of f ðyÞ can be calculated. You are attempting to find a value of
x so that f ðxÞ ¼ c. You know from sample calculations that c is within the range of
sample values of f ðyÞ so far calculated. You proceed to program the interval bisec-
tion algorithm, and let it run. At each step, either f ðxjÞ > c or f ðxjÞ < c, and it is
apparent that xj ! x for some x 0 0. However, it is also apparent that f ðxjÞ is not
converging. To see what is going wrong, a graphical depiction of this function must
be laboriously estimated, and it appears to be given by
f ðyÞ ¼
1  2y;
y < x,
1 þ 2y;
y b x.

In this case a subsequence of ff ðxjÞg is approaching 1  2x, another subsequence is
approaching 1 þ 2x, and of course, 1  2x < c < 1 þ 2x.
The second subtle assumption needed for the usefulness of the interval bisection
method is that if xj ! x, and we observe f ðxjÞ to be converging in that there is
some c with
j f ðxjÞ  cj ! 0;
then it must be the case that f ðxÞ ¼ c. But this conclusion is really just another as-
sumption about the behavior of the function, f ðxÞ. That is, the assumption that
xj ! x and f ðxjÞ ! c implies that f ðxÞ ¼ c.
As it turns out, both assumptions are valid for an important, and fortuitously
abundant and commonly encountered collection of functions, known as the continu-
ous functions. These functions satisfy both properties needed. Namely, if f ðxÞ is con-
tinuous on an interval, and fxj; xg are contained in this interval, then from xj ! x
we can conclude that:
1. ff ðxjÞg converges.
2. ff ðxjÞg converges to f ðxÞ.
5.5
Applications to Finance
171

Continuous functions will be investigated in more detail, along with other impor-
tant properties of functions, in chapter 9 on calculus I.
Exercises
Practice Exercises
1. Evaluate the convergence or lack of convergence of the following. In the cases of
convergence, attempt to determine the formula for NðÞ for arbitrary  > 0, while for
divergence to Gy, do the same for NðMÞ. (Hint: The formulas for NðÞ and NðMÞ
do not have to be the ‘‘best possible,’’ so estimate the results.)
(a) cn ¼
ffiffiffiffiffiffiffiffiffiffiffi
n þ 1
p

ffiffin
p (Hint: Multiply by
ffiffiffiffiffiffi
nþ1
p
þ ffiffin
p
ffiffiffiffiffiffi
nþ1
p
þ ffiffin
p .)
(b) bm ¼
ffiffiffiffiffiffiffi
mþ1
p
 ffiffiffim
p
ffiffiffiffiffiffiffi
mþ3
p
(c) di ¼ a i
i! , where a > 1 (Hint: diþ1 ¼
a
iþ1 di.)
(d) xk ¼ k k
k! (Hint: Consider ln xk.)
(e) zj ¼
4j
j 2þ ffij
p
(f ) ym ¼ 3m25m
8m2þ5m
2. Let fxng be a convergent sequence and fyng an arbitrary bounded sequence:
(a) Prove that if xn ! 0, then ynxn ! 0.
(b) Show by example that if xn ! x 0 0, then ynxn need not be convergent. (Hint:
Consider yn with alternating signs.)
(c) Repeat part (b), showing that we need not have ynxn convergent even if all
yn b 0.
3. How does taking absolute values influence convergence?
(a) If xn ! x is convergent, must jxnj be convergent? Does the answer depend on
whether x ¼ 0 or x 0 0?
(b) If jxnj ! x is convergent, must xn be convergent? Does the answer depend on
whether x ¼ 0 or x 0 0?
4. For n ¼ 0; 1; 2; 3; . . . , consider the sequence defined by
ym ¼
1
ðnþ1Þ! ;
m ¼ 3n,
ð1Þn10 þ ð1Þ nþ1n
2ðnþ1Þ ;
m ¼ 3n þ 1,
ð1Þnþ1 þ
ð1Þ n
10ðnþ1Þ ;
m ¼ 3n þ 2.
8
>
>
>
<
>
>
>
:
172
Chapter 5
Sequences and Their Convergence

(a) Determine all the limit points of this sequence and the associated convergent
subsequences.
(b) Determine the formula for Un and Ln, as given in the definition of limits su-
perior and inferior, and evaluate the limits of these monotonic sequences to derive
lim sup ym and lim inf ym, respectively.
(c) Confirm that the limit superior and limit inferior, derived in part (b), correspond
to the l.u.b. and g.l.b. of the limit points in part (a).
5. Let fqng denote an ordering of all rational numbers in ½0; 1.
(a) For the ordering implied by Cantor’s construction in section 2.1.4, including or
excluding multiple counts, demonstrate that for every n, Un ¼ 1, Ln ¼ 0, and hence
lim sup qm ¼ 1 and lim inf qm ¼ 0.
(b) Generalize the result on part (a) by showing that the same conclusion follows for
an arbitrary ordering.
6. Demonstrate that the sequence in exercise 4 is not a Cauchy sequence, and draw
the otherwise obvious conclusion that this sequence does not converge.
7. Prove that the two definitions given for Cauchy sequence in (5.10) and (5.11) are
equivalent. (Hint: That (5.10) ) (5.11) is true follows by definition. For the reverse
implication, express dðxn; xmÞ using the triangle inequality.)
8. Identify which of the following sequences are Cauchy sequences and hence must
converge, even in cases where their limiting values may be unknown.
(a) dn ¼
n
nþ1
(b) xn ¼ 2n24
4n2þ10
(c) yn ¼ Pn
j¼1ð1Þ jþ1
(d) xn ¼ Pn
j¼1ð1Þ jþ12j
(e) fn ¼ Pn
j¼1ð1Þ jþ1aj, a > 1
(f ) ck ¼ k þ 1
k
9. For the following securities, implement the interval bisection method to produce a
tabular analysis as in table 5.1, and determine how many steps are needed to assure
six decimal place yield accuracy.
(a) A 7-year, 3.5% s.a. coupon bond with a price of 92.50 per 100 par.
(b) A 2% annual dividend perpetual preferred stock with a price of 87.25 per 100 par.
(c) A $1 million mortgage repayment loan, issued at 8% monthly, at a price of
$997,500.
Exercises
173

Assignment Exercises
10. Evaluate the convergence or lack of convergence of the following. In the cases of
convergence, attempt to determine the formula for NðÞ for arbitrary  > 0, while for
divergence to Gy, do the same for NðMÞ.
(a) cn ¼
ffiffiffiffiffiffiffiffiffiffiffi
n þ 1
mp

ffiffin
mp for m A N, m > 1 (Hint: Confirm that
am  bm ¼ ða  bÞ
X
m1
j¼0
a jbm1j
 
!
;
ð5:13Þ
and compare to exercise 1(a).)
(b) zj ¼
j!þ j
ð jþ1Þ!
(c) wm ¼ ð1Þmþ1 ln 1 þ 1
m


(d) xn ¼ ðn þ 1Þ! þ ð1Þnþ1n!
(e) ak ¼ ð1Þkþ1
2 k
10kþk
(f ) bi ¼ ð1Þiþ1ði5  i3 þ 10iÞ
(g) un ¼ ð1Þ nþ1np
a n
, p A R, a > 1 (Hint: Consider the value of


unþ1
un


:Þ
11. Consider the rational numbers in ½0; 1. Under an arbitrary enumeration, fqng,
this set is a bounded sequence. Show that:
(a) As proposition 5.12 states, this sequence has a convergent subsequence.
(b) This sequence has a countably infinite number of convergent sequences.
(c) This sequence has an uncountably infinite number of convergent sequences.
(d) These results remain true if we require all sequences to be monotonic.
12. For n ¼ 0; 1; 2; 3; . . . , consider the sequence defined by
xm ¼
ð1Þ n
nþ1 ;
m ¼ 5n,
1 þ ð1Þ nn
2ðnþ1Þ ;
m ¼ 5n þ 1,
1 þ ð1Þ n
nþ1 ;
m ¼ 5n þ 2,
n2 þ n;
m ¼ 5n þ 3,
10en;
m ¼ 5n þ 4.
8
>
>
>
>
>
>
>
>
<
>
>
>
>
>
>
>
>
:
(a) Determine all the limit points of this sequence and the associated convergent
subsequences.
174
Chapter 5
Sequences and Their Convergence

(b) Determine the formula for Un and Ln, as given in the definition of limits superior
and inferior, and evaluate the limits of these monotonic sequences to derive
lim sup xm and lim inf xm, respectively.
(c) Confirm that the limit superior and limit inferior, derived in part (b), correspond
to the l.u.b. and g.l.b. of the limit points in part (a).
13. Consider the notion of Cauchy sequence under di¤erent metrics.
(a) Prove proposition 5.27 in the form: In a metric space X under two equivalent
metrics, d1 and d2, a sequence fxng H X is a Cauchy sequence in ðX; d1Þ i¤ fxng is
a Cauchy sequence in ðX; d2Þ.
(b) Give an example of a metric on Rn, d, so that sequences that are Cauchy under d
are di¤erent than sequences that are Cauchy under the standard metric. (Hint: Con-
sider a nonequivalent metric, like d in exercise 18 in chapter 3:Þ
14. Identify which of the following sequences are Cauchy sequences and hence must
converge, even in cases where their limiting values may be unknown.
(a) aj ¼ P j
n¼1
1
n! (Hint: Show that n! > 2n for n b 4.)
(b) aj ¼ P j
n¼1
ð1Þnþ1
n!
(c) yn ¼ ð1Þnþ1
n
(d) bk ¼ Pk
n¼1
1
n2 (Hint: n2 > nðn  1Þ.)
(e) bk ¼ Pk
n¼1
ð1Þ nþ1
n2
(f ) fzng H R, increasing and bounded.
15. For the following securities, implement the interval bisection method to produce
a tabular analysis as in table 5.1. Determine how many steps need to be implemented
to assure six decimal place yield accuracy.
(a) A 10-year zero-coupon bond with a price of 66.75 per 100 par, priced with a
semiannual yield.
(b) A 10-year, 4% annual coupon bond, with a ‘‘sinking fund’’ payment of 50% of
par at time 5 years, with a price of 101 per 100 par.
(c) A $25 million, 30-year mortgage repayment loan, issued at 6% monthly, at a
price of $25.525 million.
Exercises
175



## Series and Their Convergence

6 Series and Their Convergence
6.1
Numerical Series
6.1.1
Definitions
While a series can be defined in any space X that allows addition, and convergence
defined in any such space that also has a metric, we will focus on numerical series
defined on R or C. More general definitions can be inferred now, and will be made
in later chapters as needed.
Definition 6.1
Given a numerical sequence fxjg, the infinite series associated with
fxjg is notationally represented by
X
y
j¼1
xj:
For fxjg H R, if all xj > 0, the series is called a positive series, if all xj < 0, the series
is called a negative series, whereas if the signs of the consecutive terms alternate, most
commonly with x1 > 0, the series is called an alternating series. The partial sums of a
numerical series, denoted sn, are defined as
sn ¼
X
n
j¼1
xj:
The infinite series is said to converge to a numerical value s if the sequence of partial
sums converges to s. That is, we define
X
y
j¼1
xj ¼ s
if and only if
lim
n!y sn ¼ s:
An infinite series that does not converge is said to diverge or be divergent.
A series is said to converge absolutely or be absolutely convergent if the series
Py
j¼1 jxjj converges, and is said to converge conditionally or be conditionally conver-
gent if Py
j¼1 xj converges yet Py
j¼1 jxjj diverges. If a series diverges in the sense that
limn!y sn ¼Gy, we will often write Py
j¼1 xj ¼Gy and say that Py
j¼1 xj diverges to
Gy.
Remark 6.2
1. For some examples, an infinite series will be indexed as Py
j¼0 xj rather than
Py
j¼1 xj.

2. By definition, every convergent positive or negative series is absolutely convergent,
but in general convergence does not imply absolute convergence (see cases 3 and 6 in
examples 6.9 and 6.10 below).
This definition implies that to be convergent it must be the case that xj ! 0 as
j ! y (see exercise 1). This property alone is not enough to assure convergence as
will be seen. However, while xj ! 0 as j ! y does not assure the convergence of
Py
j¼1 xj in general, it does assure convergence when the series is alternating, as will
be demonstrated in proposition 6.20.
Applying the definition of convergence of a sequence to this series context, we
have that:
Definition 6.3
Py
j¼1 xj ¼ s if for any  > 0 there is an N so that jsn  sj <  whenever
n b N. That is,
X
y
j¼nþ1
xj


 < 
whenever
n b N:
In other words, a numerical series converges when it can be shown that by discard-
ing a finite number of terms, here the first N terms, the residual summation can be
made as small as desired. Alternatively, because a numerical sequence converges if
and only if it is a Cauchy sequence, we can state that:
Definition 6.4
Py
j¼1 xj ¼ s if for any  > 0 there is an N so that jsn  smj <  when-
ever n; m b N. That is, assuming n > m,
X
n
j¼mþ1
xj


 < 
whenever
n; m b N:
6.1.2
Properties of Convergent Series
In this section three simple, useful results are presented. More subtle properties will
be investigated in section 6.1.4 on rearrangements. The first result reinforces the
intuitive conclusion that absolute convergence is a stronger condition than conver-
gence. In the examples below we will see that this implication cannot, in general, be
reversed.
Proposition 6.5
If Py
j¼1 xj is absolutely convergent, then it is convergent.
Proof
We show that sn ¼ Pn
j¼1 xj is a Cauchy sequence. By the assumption of ab-
solute convergence, s0
n ¼ Pn
j¼1 jxjj is Cauchy, and hence for any  > 0 there is an N
178
Chapter 6
Series and Their Convergence

so that js0
n  s0
mj <  whenever n; m b N. Now, by the triangle inequality, say n > m
for specificity,
jsn  smj ¼
X
n
j¼mþ1
xj


a
X
n
j¼mþ1
jxjj ¼ js0
n  s0
mj;
so jsn  smj <  whenever n; m b N.
n
Next we see that convergent sequences combine well in terms of sums and scalar
multiples.
Proposition 6.6
Let Py
j¼1 xj and Py
j¼1 yj be convergent series with respective summa-
tions of s and s0, then for any constants a; b A R, the series faxj þ byjg is convergent,
and Py
j¼1ðaxj þ byjÞ ¼ as þ bs0.
Proof
The proof follows directly from the earlier result on sequences. The assumed
convergence of the series implies that as sequences, sn 1 Pn
j¼1 xj and s0
n 1 Pn
j¼1 yj,
converge to s and s0, respectively; hence asn þ bs0
n ! as þ bs0 from proposition 5.11.
n
Finally, we consider the termwise product sequence fxjyjg.
Proposition 6.7
Let Py
j¼1 xj and Py
j¼1 yj be absolutely convergent series. Then for
any a, b (real or complex):
1. Py
j¼1½axj þ byj is absolutely convergent.
2. Py
j¼1 xjyj is absolutely convergent.
Proof
The first statement follows from the triangle inequality, since
X
y
j¼1
jaxj þ byjj a jaj
X
y
j¼1
jxjj þ jbj
X
y
j¼1
jyjj:
For the second, we show that sn 1 Pn
j¼1 jxjyjj is a Cauchy sequence. Given  > 0,
there is an N so that Pm
j¼n jxjj <  and Pm
j¼n jyjj <  for n; m > N. Now Pm
j¼n jxjyjj
< Pm
j¼n jxjj Pm
j¼n jyjj < 2 for n > N, and the result follows.
n
Remark 6.8
If the assumption on Py
j¼1 xj and Py
j¼1 yj is reduced to conver-
gent, rather than absolutely convergent, then Py
j¼1½axj þ byj is convergent as noted in
proposition 6.6, but Py
j¼1 xjyj need not be convergent. This will be assigned as exercise
21.
6.1
Numerical Series
179

6.1.3
Examples of Series
Example 6.9
1. If xn ¼ an, a geometric sequence, then the associated geometric series converges if
and only if jaj < 1, as can be demonstrated since the partial sums can be explicitly cal-
culated. Specifically, if a 0 1, from sn ¼ Pn
j¼1 a j and asn ¼ Pnþ1
j¼2 a j, we can solve for
sn by subtraction and obtain
sn ¼ anþ1  a
a  1
:
It is apparent that if a > 1, then sn ! y, and anþ1 grows without bound; while if
a < 1, then sn alternates sign between G, and jsnj ! y. Similarly, if a ¼ 1, then by
the definition we have that sn ¼ n, which diverges, and if a ¼ 1, sn alternates between
1 and 0. Hence this series does not converge in any case for which jaj b 1. If jaj < 1,
we conclude anþ1 ! 0, and hence
X
y
j¼1
a j ¼
a
1  a ;
ð6:1Þ
equivalently, Py
j¼0 a j ¼
1
1a . Of course, this is exactly the calculation introduced in the
pricing of perpetual preferreds in section 2.3.2, with a ¼ ð1 þ iÞ1.
2. If xj ¼
1
jð jþ1Þ , then again by explicit calculation we can conclude that the sum
Py
j¼1
1
jð jþ1Þ converges. Since
1
jð jþ1Þ ¼ 1
j 
1
jþ1 , we derive that sn ¼ Pn
j¼1
1
j  Pnþ1
j¼2
1
j ,
which reduces to
sn ¼ 1 
1
n þ 1 ;
and hence Py
j¼1
1
jð jþ1Þ ¼ 1.
3. If xj ¼ 1
j , the harmonic series, then surprisingly, Py
j¼1
1
j ¼ y. This result is justifi-
ably the most surprising example of divergence of a series. The surprise stems from
thinking about an arbitrarily large integer N, say the number of subatomic particles in
the known universe. Then it is apparent that PN
j¼1
1
j is finite, and the next omitted term
1
Nþ1 is an unimaginably small number, and the rest smaller yet. However, the divergence
of the harmonic series implies that despite this unimaginable smallness, Py
j¼Nþ1
1
j is not
finite. There are many proofs of this well-known fact; one seen in example 5.35 in chap-
ter 5, but perhaps the simplest two are as follows:
180
Chapter 6
Series and Their Convergence

 For an arbitrary integer m > 1, write
X
y
j¼1
1
j ¼
X
m
j¼1
1
j þ
X
2m
j¼mþ1
1
j þ
X
3m
j¼2mþ1
1
j þ    :
Now every summation on the right has m terms, and because the harmonic series is
decreasing, each of these finite sums is strictly greater than m times the last term. That is,
X
y
j¼1
1
j > m
1
m
 
þ m
1
2m


þ m
1
3m


þ   
¼
X
y
j¼1
1
j :
So if Py
j¼1
1
j is finite, we can divide this inequality by this value to derive the absurd re-
sult 1 > 1, or subtract to derive 0 > 0. So via proof by contradiction we conclude that
the harmonic series diverges.
 Alternatively, we can manipulate this summation another way using a similar trick:
X
y
j¼1
1
j ¼
X
m
j¼1
1
j þ
X
m2
j¼mþ1
1
j þ
X
m3
j¼m2þ1
1
j þ   
> m
1
m
 
þ ðm2  mÞ
1
m2


þ ðm3  m2Þ
1
m3


þ   
¼ 1 þ
1  1
m


þ
1  1
m


þ
1  1
m


þ    ;
from which the divergence is apparent since each term after the first equals the constant
1  1
m .
4. If xj ¼ 1
j a for a > 1, then the power harmonic series, Py
j¼1
1
j a , converges. Using the
second trick above for the harmonic series, we create an upper bound with the first term
of each group:
X
y
j¼1
1
j a ¼
X
m
j¼1
1
j a þ
X
m2
j¼mþ1
1
j a þ
X
m3
j¼m2þ1
1
j a þ   
< mð1Þ þ ðm2  mÞ
1
ðm þ 1Þa þ ðm3  m2Þ
1
ðm2 þ 1Þa þ   
6.1
Numerical Series
181

< m þ m2  m
ma
þ m3  m2
m2a
þ   
¼ m þ ðm  1Þ
X
y
j¼1
m jð1aÞ:
The last summation is a convergent geometric series if m1a < 1. That is, if a > 1. Of
course, as a ! 1, this last summation becomes increasingly large, as the given series
approaches a summation of 1s, and the original series approaches the harmonic series.
In all these cases, note that the analysis done for the harmonic series was to infer
divergence by manipulating the terms to produce a smaller and yet obviously diver-
gent series, while the approach taken in the first two examples was to explicitly derive
the summation. In many ways the harmonic series analysis is a more realistic exam-
ple of analytics done in practice. The reason is that although there are many exam-
ples of series that can be evaluated explicitly, most of these require advanced methods
of later chapters. In addition it is common to be confronted with a series that cannot
be so evaluated even with more advanced techniques. In many of these cases this
inability to find an exact value is not a problem since the primary question is related
to the convergence or divergence of the series, and not to the exact value that the
series converges to. If one can prove convergence, it is usually possible to develop a
numerical approximation to the summation, or reasonable upper and lower bounds
adequate for the purposes at hand.
There are many ways to prove convergence of series without an explicit evaluation
of its summation. The most direct is the strategy employed for the geometric har-
monic series, namely, to demonstrate that the series is smaller than one that appar-
ently converges.
Example 6.10
5. If xj ¼ ln j
j 3 , then Py
j¼1 xj converges. To demonstrate this convergence without
explicitly evaluating the actual summation, we show that this series is smaller than a
simpler series that is readily seen to converge. First o¤, ln j < j, and so xj < 1
j 2 . Hence
X
y
j¼1
ln j
j3 <
X
y
j¼1
1
j2 < y:
This second summation converges as in case 4 of example 5.9 with a ¼ 2. Alternatively,
by noting that 1
j 2 <
1
jð j1Þ for j b 2, and with case 2 we conclude that this series con-
verges to a value less than 2.
182
Chapter 6
Series and Their Convergence

6. If xj ¼ ð1Þ jþ1
j
, the alternating harmonic series, then Py
j¼1 xj converges. Taking this
series in pairs, we obtain for n ¼ 1; 3; 5; . . . that xn þ xnþ1 ¼
1
nðnþ1Þ , which equals the
odd terms of the series in case 2. Consequently
X
n
j¼1
ð1Þ jþ1
j
¼
Pm
j¼1
1
2jð2j1Þ ;
n ¼ 2m,
Pm
j¼1
1
2jð2j1Þ 
1
2mþ1 ;
n ¼ 2m þ 1.
(
Therefore the even partial sums of the alternating harmonic series equal the partial
sums of a subseries of the convergent series of case 2, while the odd partial sums equal
this same convergent series but minus a term that converges to 0. The even and odd par-
tial sums of this series must therefore converge to the same value. Yet, this series is only
conditionally convergent, since the absolute value of this series is the harmonic series
that diverges. As we will see as an application of a result from calculus in chapter 10,
it turns out that Py
j¼1
ð1Þ jþ1
j
¼ ln 2, the natural logarithm of 2, which is approximately
0:69315.
It is important to note that a subseries of a convergent series need not converge.
The conclusion in case 6 is justified because the original convergent series in case 2
had all positive terms. More generally, what is needed is that the original series is ab-
solutely convergent. An example of what can go wrong in the conditionally conver-
gent case follows:
Example 6.11
7. If xj ¼ ð1Þ jþ1
j
, the (convergent) alternating harmonic series, then Py
j¼1 x2j and
Py
j¼1 x2j1 both diverge. First o¤,
X
y
j¼1
x2j ¼  1
2
X
y
j¼1
1
j ;
which is a multiple of the harmonic series. Similarly
X
y
j¼1
x2j1 ¼
X
y
j¼1
1
2j  1 >
X
y
j¼1
1
2j ¼ 1
2
X
y
j¼1
1
j ;
another multiple of the harmonic series.
Cases 3, 4, 5, 6, and 7 of the examples above present an application of the com-
parison test for a series. This and other tests are presented below in section 6.1.5 on
tests of convergence. However, the next section provides two important results
on absolutely versus conditionally convergent series.
6.1
Numerical Series
183

*6.1.4
Rearrangements of Series
In attempting to evaluate the sum of a series or even to prove convergence, it is often
desirable to be able to rearrange the order of the series. This is especially true for
double series as will be seen below. But while a valid manipulation for finite sums,
it is not always the case that an infinite sum can be rearranged without changing its
value, or indeed changing whether or not it even converges. This section analyzes the
relationship between convergence of a series and convergence of its rearrangements,
as well as the associated summations.
To introduce the notion of a rearrangement formally, we introduce the notion of
a rearrangement function, pðnÞ, defined on the index collection J 1 fjgy
j¼0 or J 1
f jgy
j¼1, with the property that p : J ! J as a one-to-one and onto function. These
words reflect three notions that can be reduced to the intuitive idea that p creates a
‘‘shu¿e’’ of the set J:
 A ‘‘function’’ J ! J means that for any j A J, pðjÞ is a unique element of J.
 ‘‘One-to-one’’ means that there cannot be j; k A J with pð jÞ ¼ pðkÞ. Each j is
mapped to a di¤erent point.
 ‘‘Onto’’ means that for any element k A J, there is a j A J, with pðjÞ ¼ k.
Given a series fxjg the focus of this section has to do with the value of Py
j¼1 xj
versus the value of Py
j¼1 xpð jÞ for an arbitrary rearrangement function p. Before pre-
senting the results, let us consider two examples that highlight what can happen.
Example 6.12
1. Recall the alternating harmonic series in example 6.11, xj ¼ ð1Þ jþ1
j
, which con-
verges but is not absolutely convergent. As was demonstrated, both Py
j¼1 x2j and
Py
j¼1 x2j1 diverge, so the conditional convergence of this series occurs because of the
cancellation that occurs between one subseries that is accumulating to þy, and the
other subseries that is accumulating to y. Intuition warns that rearranging this series
could cause trouble. Indeed, if we simply rearrange the series with all the positive terms
first, and all the negatives last, we arrive at a meaningless conclusion that Py
j¼1 xj ¼
y  y, and we are justifiable cautious about concluding that this sum is 0. However,
with a bit of ingenuity it is possible to rearrange this series so that the rearranged series
converges conditionally to any real number, or even to Gy. This seems impossible, but
it is not too di‰cult to demonstrate. Let r A R be given, and assume that r b 0. Choose
N1 to be the first integer so that PN1
j¼1 x2j > r. Next choose M1 to be the first integer so
that PN1
j¼1 x2j þ PM1
j¼1 x2j1 < r. Both choices are possible since the positive and nega-
184
Chapter 6
Series and Their Convergence

tive series grow without bound. Now choose N2 > N1 to be the first integer so that
PN1
j¼1 x2j þ PM1
j¼1 x2j1 þ PN2
j¼N1þ1 x2j > r, and M2 > M1 to be the first integer so that
PN1
j¼1 x2j þ PM1
j¼1 x2j1 þ PN2
j¼N1þ1 x2j þ PM2
j¼M1þ1 x2j1 < r, and so forth. We can
therefore show that this implied rearrangement of the series,
x2; . . . ; x2N1; x1; . . . ; x2M11; x2ðN1þ1Þ; . . . ;
converges conditionally to r. For example, at the last step above, since M2 was the first
integer to produce the desired property, it is the case that
X
N1
j¼1
x2j þ
X
M1
j¼1
x2j1 þ
X
N2
j¼N1þ1
x2j þ
X
M21
j¼M1þ1
x2j1 > r;
and hence
r 
X
N1
j¼1
x2j þ
X
M1
j¼1
x2j1 þ
X
N2
j¼N1þ1
x2j þ
X
M2
j¼M1þ1
x2j1
 
!


 < jx2M2j:
In other words, at each step the di¤erence between the partial summation and r is
bounded by the absolute value of the last term added. Consequently, as these last added
terms converge to 0 absolutely, conditional convergence is proved. If r < 0, the process
is simply reversed. If r ¼Gy, think about how this construction can be modified (an-
swer is below in the proof of the Riemann series theorem).
2. Consider an alternating geometric series, xj ¼ ð1Þ ja j, j b 0, where 0 < a < 1.
This series is absolutely convergent by example 6.9 above, so it is also convergent. Let
the summation be denoted: s ¼ Py
j¼0ð1Þ ja j. Then with s1 ¼ Py
j¼0 a2j ¼
1
1a2 and
s2 ¼ Py
j¼0 a2jþ1 ¼ as1 ¼
a
1a2 , we have s ¼ s1  s2 ¼
1
1þa . Let p be a given rearrange-
ment, and consider Py
j¼0ð1Þpð jÞapð jÞ. The goal is to show that Py
j¼0ð1Þpð jÞapð jÞ ¼ s
and has the same value as the original series. To do so, for a given  > 0 we need
to show that there is an N so that js  Pn
j¼0ð1Þpð jÞapð jÞj <  for n b N. To this end,
we focus on the positive and negative series separately. Since s1 ¼ Py
j¼0 a2j, choose N1
so that js1  Pn
j¼0 a2jj < 
3 for n b N1, and choose N2 so that js2  Pn
j¼0 a2jþ1j < 
3
for n b N2. Also, since this series is absolutely convergent, we can apply the Cauchy
criteria and choose N3 so that jPm
j¼n a jj < 
3 for n; m > N3. Now note that for any
n, fpðjÞgn
j¼0 can be split into even and odd integers, and we choose N large enough
so that fpð jÞgN
j¼0 contains f jgmaxðNjÞ
j¼0
. Then for n b N we have by the triangle
inequality,
6.1
Numerical Series
185

s 
X
n
j¼0
ð1Þpð jÞapð jÞ


¼ ½s1  s2 
X
maxðNjÞ
j¼0
a2j 
X
maxðNjÞ
j¼0
a2jþ1
"
#
þ
X
pð jÞbmaxðNjÞ
ð1Þpð jÞapð jÞ


a s1 
X
maxðNjÞ
j¼0
a2j


 þ s2 
X
maxðNjÞ
j¼0
a2jþ1


 þ
X
pð jÞbmaxðNjÞ
apð jÞ


< 
3 þ 
3 þ 
3 ¼ :
The following propositions summarize the results illustrated in the examples
above. The proofs will be brief since they follow closely the developments given in
these special cases. The first result is named for Bernhard Riemann (1826–1866).
Proposition 6.13 (Riemann Series Theorem)
Let fxjgy
j¼1 be a conditionally conver-
gent series, Py
j¼1 xj ¼ s. Then for any r A R, as well as r ¼Gy, there is a rearrange-
ment function p so that Py
j¼1 xpð jÞ ¼ r.
Proof
Since fxjgy
j¼1 is not absolutely convergent, it must be the case that there are
infinitely many terms in the series that are both positive and negative. This is because
if either set was finite, say fxjgn
j¼1 were the positive terms, then since Py
j¼1 xj ¼
Pn
j¼1 xj þ Py
j¼nþ1 xj, we derive that Py
j¼nþ1 xj ¼ s  Pn
j¼1 xj. Now since all xj < 0
for j > n, we have that Py
j¼nþ1 jxjj ¼ Pn
j¼1 xj  s. This implies that Py
j¼1 jxjj ¼
2 Pn
j¼1 xj  s, contradicting that fxjgy
j¼1 is not absolutely convergent. So both posi-
tive and negative subseries are infinite. Next, denoting by fxþ
j gy
j¼1 and fx
j gy
j¼1 these
infinite collections of positive and negative terms represented in their respective
orderings, it must be the case that both Py
j¼1 xþ
j ¼ y and Py
j¼1 x
j ¼ y. Again,
if either were finite, the conditional convergence of fxjgy
j¼1 would imply its absolute
convergence, a contradiction. Now with these divergent positive and negative sub-
series, the proof is identical to the derivation above for the alternating harmonic se-
ries if r A R. In the case r ¼ y, choose N1 so that PN1
j¼1 xþ
j b 10jx
1 j, then choose N2
so that PN2
j¼N1þ1 xþ
j b 10jx
2 j, and so forth. The rearrangement is xþ
1 ; . . . ; xþ
N1; x
1 ;
xþ
N1þ1; . . . ; xþ
N2; x
2 ; . . . . By construction, the summation of each block of positives
and one negative term, x
j , exceeds 9jx
j j, and hence Pn
j¼1 xpð jÞ grows like
9 Pm
j¼1 jx
j j, where m is the subscript of the largest Nj with Nj a n. A similar type of
construction produces the result for r ¼ y.
n
186
Chapter 6
Series and Their Convergence

It is interesting to note that the rearrangements implied by this proposition have a
special and initially not obvious property. Namely the collection of ‘‘forward shifts,’’
fpð jÞ  jg, must be unbounded in the construction above for the summation of the
series to shift from the original value of s to any new value r. In other words, in order
to get the desired results, the rearrangement implied by this construction needs to
map the elements of the index set fjg farther and farther from their initial positions
to new forward positions.
To investigate this, note that the construction in the proof above creates a series
xþ
1 ; . . . ; xþ
N1; x
1 ; . . . ; x
M1; xþ
N1þ1; . . . ; xþ
N2; x
M1þ1; . . . ; x
M2; . . .
within which the forward shifts for positive terms appear to be unbounded, since they
grow in relation to P Mj as caused by the insertion of groups of negative terms. Sim-
ilarly the forward shifts of negative terms appear unbounded as caused by the inser-
tion of groups of positive terms.
But we need to be skeptical of this argument. The positive and negative terms were
interspersed somehow initially, and perhaps interspersed similarly to what the con-
struction called for. So this construction likely only changed the order a small
amount, and not in the claimed unbounded way.
The next result shows in fact that if the rearrangement function only moves
indexes by a limited amount, then the rearranged series converges to the original
summation value and cannot be changed.
Proposition 6.14
Let fxjgy
j¼1 be a conditionally convergent series, Py
j¼1 xj ¼ s, and p
a rearrangement function with the property that for some integer P and all j, pðjÞ a
j þ P. Then Py
j¼1 xpð jÞ ¼ s.
Proof
Consider the partial sums, Pn
j¼1 xj and Pn
j¼1 xpð jÞ. By the given assumption
on p that pðjÞ a j þ P, it must be the case that
fxpð jÞgnP
j¼1 H fxjgn
j¼1:
It is also possible that some or all of fxpð jÞgn
j¼nPþ1 are also included in fxgn
j¼1, but
this will not matter for the proof. So we can conclude that
X
n
j¼1
xj 
X
n
j¼1
xpð jÞ ¼
X
n
j¼nPþ1
xj 
X
n
j¼nPþ1
xpð jÞ;
where by assumption, n  P þ 1 a pð jÞ a n þ P for n  P þ 1 a j a n. Denoting
fpð jÞgn
j¼nPþ1 by fn  P þ njgP
j¼1 for integers 1 a nj a 2P, we derive by the triangle
inequality,
6.1
Numerical Series
187

X
n
j¼1
xj 
X
n
j¼1
xpð jÞ


a
X
P
j¼1
jxnPþjj þ
X
P
j¼1
jxnPþnjj:
Now, since fxjgy
j¼1 is a convergent series, we have that xj ! 0 as j ! y, so the sum
of the 2P terms in this upper bound also converges to 0. More formally, for any
 > 0, choose N so that jxjj < 
2P for j > N. Then choose n above so that n 
P þ 1 > N.
n
The implication of this result is that rearrangements of conditionally convergent
series are allowable as long as the rearrangement is limited to index movements that
are bounded in the sense above, whereby for all j, pðjÞ a P þ j for some fixed P.
As an application, if a series is presented for evaluation of convergence, any num-
ber of rearrangements are possible within the rule that pðjÞ a P þ j for some fixed P.
If such manipulations then provide a basis for concluding convergence, then one can
be assured that the original series converges to the same value. In other words, this
result can be applied backward in that if a bounded rearrangement produces a con-
vergent series, then the original series must be convergent to the same value. As the
proposition demonstrated, however, with unbounded rearrangements, anything can
happen.
The conclusion for absolutely convergent series is completely general, in that such
a series can be rearranged in any way without changing the value of the sum.
Proposition 6.15
Let fxjgy
j¼1 be an absolutely convergent series, Py
j¼1 xj ¼ s, and p
any rearrangement function. Then Py
j¼1 xpð jÞ ¼ s.
Proof
The goal is to reproduce the proof used for the alternating geometric series in
case 2 of example 6.12, but we first need to show that this series can be split into a
positive and negative subseries, and that each of these converges to values that in
turn sum to s. To this end, define fxþ
j gy
j¼1 and fx
j gy
j¼1 by
xþ
j ¼ maxfxj; 0g;
x
j ¼ maxfxj; 0g:
For the alternating geometric series above, this definition produces xþ
2j ¼ a2j,
x
2j1 ¼ a2j1, and both subseries are 0 for other indexes. Now note that xj ¼
xþ
j  x
j , and jxjj ¼ xþ
j þ x
j . Since this series is absolutely convergent, both subseries
xþ
j ¼ 1
2 ½xj þ jxjj and x
j ¼ 1
2 ½jxjj  xj are absolutely convergent to s1 and s2, respec-
tively. Therefore
X
n
j¼1
xj  ðs1  s2Þ


a
X
n
j¼1
xþ
j  s1


 þ
X
n
j¼1
x
j  s2


;
188
Chapter 6
Series and Their Convergence

which implies that Py
j¼1 xj ¼ s1  s2 ¼ s. With this setup the proof of this result for
the alternating geometric series now can be implemented identically, by substituting
xþ
j and x
j in the roles of the positive and negative terms in example 6.12.
n
Example 6.16
Two common and important applications of this last result are:
1. If a series is given with only positive or negative terms, or one with only a finite num-
ber of terms of one sign and the remainder of the other, then such a series is convergent
if and only if it is absolutely convergent. Consequently one can apply completely arbi-
trary rearrangements to the series in search of evidence of convergence because, once
such evidence is found, one concludes absolute convergence, justifies the rearrangement
by the proposition above, and knows that the original series must have the same sum-
mation as that developed for the rearrangement.
2. Since the rearrangement functions contemplated by the proposition above are com-
pletely general, one could in theory split such a series into a series of even terms fol-
lowed by a series of odd terms, or in three collections
x1; x4; . . . ; x2; x5; . . . ; x3; x6; . . .
or any number of countably infinite subseries. An important application of this observa-
tion is to a ‘‘multiple’’ series, such as the double series,
X
y
j¼1
X
nð jÞ
i¼1
xij;
where nð jÞ is some function of j, or simply nðjÞ ¼ y, for all j. A common example is
nð jÞ ¼ j. Of course, triple, quadruple, and higher order series are similarly defined,
though less common in applications. These summations are always intended to be per-
formed from the outer summation inward so that in the example above,
X
y
j¼1
X
nð jÞ
i¼1
xij ¼
X
nð1Þ
i¼1
xi1 þ
X
nð2Þ
i¼1
xi2 þ
X
nð3Þ
i¼1
xi3 þ
X
nð4Þ
i¼1
xi4 þ    :
One can envision these index points on the positive integer lattice in R2, where xij is
defined at each point ði; jÞ, i; j > 0 as in figure 6.1. The double summation is then envi-
sioned as summing along rows, starting with j ¼ 1 and summing the first row from
i ¼ 1 to nð1Þ, then the second row, from i ¼ 1 to nð2Þ, and so forth. It is often conve-
nient to be able to reverse the order of the summation, to in e¤ect sum by columns first.
For example,
6.1
Numerical Series
189

X
y
j¼1
X
y
i¼1
xij
becomes
X
y
i¼1
X
y
j¼1
xij;
X
y
j¼1
X
j
i¼1
xij
becomes
X
y
i¼1
X
y
j¼i
xij:
In the second summation, the integer lattice model simplifies the setting of the limits for
the reversed summations by providing a visual representation. The question that arises
is, can summations be switched in such a manner? Intuitively, if the series is only condi-
tionally convergent, there is little hope of a positive conclusion, since it is apparent that
such rearrangements move series terms by arbitrarily large distances. On the other
hand, if the series has terms of one sign, or all but a finite number of one sign, then
again it will be convergent if and only if absolutely convergent. In such cases, the result
above on absolute convergence is again applied backward; that is, if one rearranges as
necessary and convergence is justified, so too is absolute convergence. So we can con-
clude that the original multiple series has the same summation as the rearranged series.
6.1.5
Tests of Convergence
There are many tests of convergence for a series, and at first their large number may
seem odd. Just how many tests does one need? The problem is that no test is stated in
the unambiguous language:
Figure 6.1
Positive integer lattice
190
Chapter 6
Series and Their Convergence

The series Py
j¼1 xj converges if and only if . . . ;
that is, except the test in the definition itself, which then goes on to require for the
Cauchy condition that
. . . for every  > 0, bN with jPm
j¼1 xj  Pn
j¼1 xjj <  for n; m > N.
So the definition of convergence provides an ‘‘i¤’’ test of convergence, but in many
cases there is no easy way to demonstrate that there is a value of N 1 NðÞ that will
work.
The various tests of convergence provide the benefit of relative ease of implemen-
tation, but at the cost of so-called indeterminate cases. To be more precise, all tests
provide the following schema, either explicitly or implicitly:
1. The series Py
j¼1 xj converges if condition A is satisfied.
2. The series Py
j¼1 xj diverges if condition B is satisfied.
3. No information on convergence is provided in other cases.
So every test divides the collection of all series fPy
j¼1 xj j xj A R or Cg, into these
three groups according to that test’s conditions. A given series may be in the indeter-
minate group for one test, and demonstrated to converge or diverge with another. Of
course, it will never be the case that one test assures convergence, another divergence,
or conversely.
The reason for the multitude of tests is that each varies in terms of ease of imple-
mentation for a given series, as well as in terms of the specific members of the group
of series that remain indeterminate. Tests can be intuitively thought of as stronger
if they provide a smaller indeterminate set, but there is no generally accepted order-
ing for the strength of such tests unless one test’s indeterminate set is contained in
another’s.
So far, no test other than the definition itself has been discovered that has j, the
empty set, as its indeterminate collection. In this section we identify a few of the
best and easiest to implement tests. Also a very useful test will be added in chapter
10, using a method involving Riemann integrals. The first test is probably the most
widely used because it a¤ords the analyst a great deal of flexibility in its application.
Proposition 6.17 (The Comparison Test)
If Py
j¼1 xj is absolutely convergent, and
Py
j¼1 yj is any series with jyjj a jxjj, for j b N for some N, then Py
j¼1 yj converges
absolutely. Conversely, if Py
j¼1 xj and Py
j¼1 yj are any series with jyjj a jxjj, for some
j b N, and Py
j¼1 jyjj ¼ y, then Py
j¼1 jxjj ¼ y.
6.1
Numerical Series
191

Proof
For the convergence condition, if sn ¼ Pn
j¼1 jyjj, then for n b N,
sn a
X
N
j¼1
jyjj þ
X
n
j¼Nþ1
jxjj a
X
N
j¼1
jyjj þ
X
y
j¼1
jxjj:
In other words, the absolute partial sums of the series fyjg are both increasing with
n, and bounded. Because these partial sums are bounded, they must have an accumu-
lation point. So there is an s such that for any  > 0 there is an MðÞ with jsM  sj <
. However, since the sequence fsng is increasing, jsn  Sj <  for n b M, and hence s
is the limit of the partial sums. That is, Py
j¼1 jyjj ¼ s. For the divergence condition, it
is clear by assumption that the absolute partial sums, sn ¼ Pn
j¼1 jyjj, are unbounded.
Consequently, since all but a finite number of jxjj exceed jyjj, the partial sums of this
series must also be unbounded, and hence Py
j¼1 jxjj ¼ y.
n
Remark 6.18
1. Note that for the purpose of establishing convergence by the comparison test, or di-
vergence, one can ignore any finite number of terms of the respective sequences. In
other words, the relationship between jyjj and jxjj, for j a N and any fixed N, is irrel-
evant to the conclusions.
2. Note also that the assumption in the comparison test for convergence is that for
some N and j b N,
jxjj a yj a jxjj:
That is, that all but finitely many terms of fyjg are bounded by two convergent series.
This can be generalized. Namely, if there are two convergent series Py
j¼1 xj and
Py
j¼1 zj so that
xj a yj a zj
for j b N for some N;
then
Py
j¼1 yj
is
convergent.
This
is
because
0 a zj  yj a zj  xj,
and
since
Py
j¼1ðzj  xjÞ converges by assumption, and hence converges absolutely because the
terms are nonnegative, we conclude that Py
j¼1ðzj  yjÞ converges, and in fact converges
absolutely. Subtracting the convergent Py
j¼1 zj implies the result.
Example 6.19
Consider Py
n¼1
1
n! , where as usual, n! 1 nðn  1Þðn  2Þ    2  1 is
called n factorial. Note that for n b 4,
nðn þ 1Þ
n!
¼ n þ 1
n  1
1
ðn  2Þ! a 5
3  1
2 < 1:
192
Chapter 6
Series and Their Convergence

In other words, 1
n! <
1
nðnþ1Þ for n b 4, and consequently, Py
n¼1
1
n! converges by the com-
parison test because Py
n¼1
1
nðnþ1Þ converges by case 2 in example 6.9.
The next test generalizes the result observed for the alternating harmonic series in
example 6.10.
Proposition 6.20 (Alternating Series Convergence Test)
If Py
j¼1 xj is an alternating
series, and for some N we have jxjþ1j a jxjj for j b N and xj ! 0, then Py
j¼1 xj con-
verges. If s denotes the summation, we have the partial sum error estimate with
sn ¼ Pn
j¼1 xj:
jsn  sj a jxnþ1j
for n b N:
Proof
Since PN1
j¼1 xj ¼ s0 is finite, and for n b N,
sn ¼
X
n
j¼N
xj þ s0;
we can ignore these exceptional terms and assume that jxjj monotonically decreases
to 0 for all j. For specificity, assume that x1 > 0. We first show that the odd partial
sums form a decreasing sequence that is bounded below. This follows from
s2nþ1 ¼ s2n1 þ x2n þ x2nþ1
a s2n1;
since x2n a 0 a x2nþ1 and jx2nþ1j a jx2nj by the monotonicity assumption. In addi-
tion this sequence is bounded below by 0, since we have that every s2nþ1 can be
expressed as a summation of nonnegative terms by s2nþ1 ¼ x2nþ1 þ Pðx2j þ x2j1Þ,
where the summation is from j ¼ 1 to n.
Similarly the even partial sums form an increasing sequence that is bounded
above. By proposition 5.18, both sequences are convergent, say to E and O for even
and odd. But since js2nþ1  s2nj ¼ jx2nþ1j ! 0, we have E ¼ O ¼ s and sn ! s. Now
by this discussion,
s2n a s a s2nþ1
for all n;
so 0 a s  s2n a s2nþ1  sn ¼ x2nþ1. Similarly 0 a s2nþ1  s a s2nþ1  s2nþ2 a x2nþ2,
and the error bounds follow.
n
Example 6.21
As a simple application to the alternating harmonic series, if we desire
an estimate of the summation that is within  of the true sum, we simply choose N so
6.1
Numerical Series
193

that
1
Nþ1 < . We then know from the proposition above that sN ¼ PN
j¼1
ð1Þ jþ1
j
will be
within  of the correct answer. As noted above, using methods of calculus, we will derive
that s ¼ ln 2, and we can conclude that
ln 2 
X
N
j¼1
ð1Þ jþ1
j


a
1
N þ 1 :
To get the correct Mth decimal place of ln 2, which is to say that we want an error of
less that
0:5
10Mþ1 , requires about N A2ð10Mþ1Þ terms of this summation. In other words,
although this series converges, it does so very slowly.
Next are two tests for convergence that depend on ratios. The first uses ratios of
the given series’ terms with those of an absolutely convergent series; the second uses
ratios of consecutive terms from the given series.
Proposition 6.22 (Comparative Ratio Test)
If Py
j¼1 xj is an absolutely convergent
series, and fyjg is a sequence so that limj!y
jyjj
jxjj exists, then Py
j¼1 yj is absolutely
convergent.
Proof
The existence of this limit implies that
jyjj
jxjj
n
o
is a bounded sequence, and
hence jyjj a Bjxjj for all j. Since Py
j¼1 Bxj is absolutely convergent by assumption,
the result follows by the comparison test in proposition 6.17.
n
Remark 6.23
This innocent looking result provides a powerful intuitive conclusion
about convergence. First o¤, if Py
j¼1 xj is an absolutely convergent series, it is apparent
that jxjj ! 0. Therefore for any  > 0 there is an N so that jxjj <  for j b N. The
comparative ratio test says that if fyjg is any sequence that converges as fast or faster
to 0, that is,
lim
j!y
jyjj
jxjj ¼ C b 0;
then Py
j¼1 yj is also absolutely convergent.
In other words, any absolutely convergent series provides a ‘‘speed benchmark’’ for
the rate at which the absolute value of its terms converge to 0 in that every series that
converges as fast or faster must also be absolutely convergent.
Although there are many other tests of convergence, we end with one of the most
useful, as will be seen in the next section.
194
Chapter 6
Series and Their Convergence

Proposition 6.24 (Ratio Test)
If Py
j¼1 xj is a series so that
lim sup
n!y
jxnþ1j
jxnj


¼ L < 1;
then Py
j¼1 xj is absolutely convergent. On the other hand, if
lim inf
n!y
jxnþ1j
jxnj


¼ L > 1;
then Py
j¼1 xj diverges. If L ¼ 1 in either case, no conclusion can be drawn.
Remark 6.25
Recall the intuitive definition of limits superior and inferior. That is,
consider all values of the sequential ratios
jxnþ1j
jxnj
n
o
, as well as all possible accumulation
points. The ratio test says that if the largest such accumulation point is less than 1, the
series must be absolutely convergent, and if the smallest is greater than 1, the series
diverges. This test is powerful because it does not require the existence of the limit
of these ratios, it only depends on values of the smallest and largest accumulation
points.
Of course, if the limit of these ratios exists, then the series converges absolutely
or diverges according to whether the limit is less than or greater than 1. The in-
definite case of L ¼ 1 is easy to illustrate. From cases 3 and 4 of example 6.9,
we know that P 1
j diverges and P 1
j 2 converges, and yet for both, L ¼ 1 as is easily
verified.
Proof
In the first case where lim supn!y
jxnþ1j
jxnj
n
o
¼ L < 1, by proposition 5.22, for
any  there is an N so that
jxnþ1j
jxnj
n
o
< L þ  for n b N. Choose  < 1  L; then for
any m b 1,
jxNþmj
jxNj
¼ jxNþmj
jxNþm1j
jxNþm1j
jxNþm2j . . . jxNþ1j
jxNj
< ðL þ Þm:
In other words, jxNþmj < ðL þ ÞmjxNj for all m b 1, so fjxNþmjg is bounded above
by a geometric series. Now, since L þ  < 1 by construction, this geometric series
must converge, and so too the original series by the comparison test. The limit
inferior result is similar, only we conclude that jxNþmj > ðL  ÞmjxNj, where  is
chosen as  < L  1, so this sequence is bigger than a divergent geometric series
as L   > 1.
n
6.1
Numerical Series
195

6.2
The lp-Spaces
6.2.1
Definition and Basic Properties
The primary reason to introduce the notion of the lp-spaces is that they represent an
accessible introduction to an idea that will find more application with the notion of
Lp function spaces studied in real analysis. In addition lp-spaces provide an interest-
ing and important counterpoint to the conclusion drawn in chapter 3, that all lp-
norms are equivalent in Rn. We now study what happens to this conclusion when
n ! y.
Notation 6.26
While one can easily distinguish between lp-space and Lp-space in writ-
ing, it is more di‰cult to do so in conversation, since both are pronounced ‘‘lp space.’’
For this reason one sometimes hears ‘‘little lp space’’ and ‘‘big lp space’’ in a discussion.
Definition 6.27
For 1 a p a y the space lp is defined by
lp ¼ fx ¼ fxjgy
j¼1 j kxkp < yg;
where, consistent with the lp-norms defined for Euclidean space,
kxkp 1
X
jxjjp

	1=p
;
1 a p < y;
ð6:2aÞ
kxky 1 sup
j
fjxjjg:
ð6:2bÞ
Real lp-space and complex lp-space are defined according to whether fxjgy
j¼1 H R or
fxjgy
j¼1 H C. The absolute values jxjj in (6.2) are defined according to xj being real
or complex, as in (2.3) and (2.2), respectively.
Intuitively, one can imagine real lp-space as an infinite Euclidean space, Ry, under
the previously defined lp-norms. That is a good starting point for our intuition, in
that we will see that the lp-spaces are vector spaces just as was Euclidean space, and
that the lp-norms defined above are indeed norms in the sense of chapter 3.
There is a dramatic di¤erence, however. Earlier we saw that all lp-norms are equiv-
alent in Rn for 1 a p a y. Switching from one norm to another changed the numer-
ical value of our norm measurements, but in every real sense the spaces were
identical. By definition, the basic collection of points in Rn were the same, and the
notions of open and closed, as well as convergence, were identical under any of these
norms.
For example, G H Rn is open with respect to one lp-norm if and only if it is open
with respect to all lp-norms. Similarly a sequence fxng H Rn converges to x A Rn in
196
Chapter 6
Series and Their Convergence

one lp-norm if and only if it converges with respect to all lp-norms. Put another way,
fxng H Rn is a Cauchy sequence with respect to one lp-norm if and only if it is a
Cauchy sequence with respect to all lp-norms.
On the other hand, the lp-norms are not equivalent in Ry. In fact, for any p with
1 a p < y, it is easy to produce a sequence fxjgy
j¼1 so that fxjgy
j¼1 A lp 0 for all p0
with p < p0 a y but fxjgy
j¼1 B lp. The simplest example uses case 4 in example 6.9.
For p given, define
x ¼ fxjgy
j¼1 1
1
j
 1=p
(
)y
j¼1
:
Then in lp, the norm of this point is the pth-root of the sum of the harmonic series,
and hence it cannot have finite lp-norm. However, by case 4, this point has finite
lp 0-norm for any p0 > p with p0 < y. In addition kxky ¼ 1. This generalizes to:
Proposition 6.28
If 1 a p < p0 a y, then lp H lp0, and the inclusion is strict.
Proof
Let x ¼ fxjgy
j¼1 A lp be given. Then the finiteness of kxkp implies that all but
a finite number of xj satisfy jxjj < 1. Now, if p0 > p and p0 < y, then
X
jxjjp 0 ¼
X
jxjj<1
jxjjp0 þ
X
jxjjb1
jxjjp0 <
X
jxjj<1
jxjjp þ C:
Consequently kxkp 0 is finite and fxjgy
j¼1 A lp 0. For p0 ¼ y, it is apparent that kxky ¼
supjfjxjjg is finite since P jxjjp is finite. Hence, in all cases, lp H lp 0. That this inclu-
sion is strict was exemplified in the case of the power harmonic series for p0 < y.
The case p0 ¼ y is easily handled by the example x ¼ fxjgy
j¼1, where all xj ¼ 1,
say. Clearly, x A ly but in no other lp-space for p < y.
n
More surprisingly, there exists an infinite collection of sequences that are in all the
lp-spaces and are in fact dense in all the lp-spaces for 1 a p < y. So the di¤erences
between these spaces is caused entirely by the ‘‘completion’’ of the common collec-
tion of sequences in the various norms. To be more precise each lp-space can be cre-
ated by adding to this common collection of sequences the limiting values obtained
by forming convergent sequences in the various norms.
To illustrate such a construction first in a more familiar setting, consider Qn H Rn,
defined as the n-tuples of rational numbers. That is,
Qn ¼ fx 1 ðx1; x2; . . . ; xnÞ j xj A Q for all jg;
6.2
The lp-Spaces
197

which is a vector space over the rational numbers. Next, define Rn
p by
Rn
p ¼ fx A Rn so that bfxjg H Qn with kx  xjkp ! 0; 1 a p a yg:
ð6:3Þ
Proposition 6.29
For any n, Rn
p ¼ Rn for all p, 1 a p a y.
Proof
By definition, Rn
p H Rn, so only the reverse inclusion need be proved. Let
x A Rn be given. Define xj A Qn so that the integer parts, and the first j-decimals of
the components of xj agree with those of x, and the decimal expansions of the com-
ponents of xj are all 0s past this jth position. Clearly, fxjg H Qn. It is also clear that
for p < y, using the geometric series summation approach illustrated in example 6.9
above obtains
kx  xjkp a 9
X
y
k¼jþ1
10kp
 
!1=p
¼ 9
10ð jþ1Þ
ð1  10pÞ1=p
 
!
;
which converges to 0 as j ! y. For p ¼ y, kx  xjky a 9ð10ð jþ1ÞÞ, which again
converges to 0. Hence Rn H Rn
p for all p, 1 a p a y, and Rn
p ¼ Rn.
n
In other words, starting with this common vector space, Qn, if we complete this
space with respect to any of the lp-norms, the same vector space arises, namely Rn.
Put yet another way, Qn is dense in Rn with respect to every lp-norm. We next show
that there is also a common vector space that is dense in all the lp-spaces, and that
each lp-space arises by completing this common space with respect to the associated
norm. To this end, we introduce the following:
Definition 6.30
Ry and Cy are formally defined as the collection of sequences:
Ry ¼ fx 1 ðx1; x2; . . . ; xn; . . .Þ j xj A R for all jg;
ð6:4aÞ
Cy ¼ fx 1 ðx1; x2; . . . ; xn; . . .Þ j xj A C for all jg:
ð6:4bÞ
Similarly Ry
0 and Cy
0 are formally defined as ‘‘truncated’’ sequences:
Ry
0 ¼ fx A Ry j xj ¼ 0 for all j > N; some Ng;
ð6:5aÞ
Cy
0 ¼ fx A Cy j xj ¼ 0 for all j > N; some Ng:
ð6:5bÞ
Addition and scalar multiplication are defined pointwise:
x þ y 1 ðx1 þ y1; x2 þ y2; . . . ; xn þ yn; . . .Þ;
198
Chapter 6
Series and Their Convergence

ax 1 ðax1; ax2; . . . ; axn; . . .Þ;
where a A R for Ry and Ry
0 , and a A C for Cy and Cy
0 .
Remark 6.31
It is easy to see that Ry and Ry
0 are vector spaces over R, and that
Cy and Cy
0 are vector spaces over C, based on definition 3.3 in chapter 3. Also, by
the definition of the lp-spaces, it is clear that for every p, 1 a p a y, Ry
0 H lp H Ry
in the real case, and Cy
0 H lp H Cy in the complex case. We study the lp-spaces in the
next section, but first demonstrate an interesting point. For conciseness, we limit the
following statement to the real lp-spaces, but it is equally valid in the complex case:
Proposition 6.32
The vector space Ry
0 is dense in every lp-space, 1 a p < y. That is,
given any x A lp, there is a sequence, fxng H Ry
0 so that kx  xnkp ! 0.
Proof
Given x 1 ðx1; x2; . . . ; xn; xnþ1; . . .Þ, define xn ¼ ðx1; x2; . . . ; xn; 0; 0; 0; . . .Þ.
In other words, xn is defined to have n nonzero components equal to the first n-
components of x. Now for p < y, x A lp implies that kxkp
p ¼ Py
j¼1 jxjjp < y. By
definition, this implies that for any  > 0 there is an N so that Py
j¼n jxjjp <  for
n > N. However, kx  xnkp
p ¼ Py
j¼nþ1 jxjjp, and hence kx  xnkp
p ! 0 as n ! y. n
It is important to note that this result does not extend to p ¼ y, as a simple
example demonstrates. If x ¼ ð1; 1; 1; 1; 1; . . .Þ, the constant vector, kx  xnky ¼
supj>nfjxjjg ¼ 1, so no convergence occurs in the ly-norm.
*6.2.2
Banach Space
For lp-spaces to be really useful, there are two as yet unanswered questions that need
to be addressed:
1. While lp-space is closed under addition and scalar multiplication as a vector space,
is it closed as a normed space? In other words, if x; y A lp, must it be true that
x þ y A lp, and so x þ y has a finite lp-norm?
2. Are the lp-spaces complete? That is, if fxng H lp is a Cauchy sequence, must there
be an x A lp so that
kx  xnkp 1
X
y
j¼1
ðxj  xnjÞp
"
#1=p
! 0?
These questions are addressed in this section, and both are answered in the a‰r-
mative. First, the a‰rmative result on closure under addition.
6.2
The lp-Spaces
199

Proposition 6.33
Real lp-space is a normed linear space over the real numbers, R, and
complex lp-space is a normed linear space over the complex numbers, C. In addition in
both spaces we have the Minkowski inequality:
kx þ ykp a kxkp þ kykp:
ð6:6Þ
Proof
Because these collections are defined as subsets of the vector spaces Ry and
Cy, all that is left to prove is that these spaces are closed under the above-given def-
initions of addition and scalar multiplication, and that the lp-norms defined in (6.2)
are indeed norms in the sense of chapter 3. Of course, closure under scalar multipli-
cation is immediate, since for any p, kaxkp ¼ jaj kxkp. The more subtle question is
addition, and for this, we demonstrate the Minkowski inequality. As in Euclidean
space, the Minkowski inequality is the name given to the triangle inequality under
the lp-norm. This result is apparent for p ¼ y since
sup
j
fjxj þ yjjg a sup
j
fjxjjg þ sup
j
fjyjjg;
and for p ¼ 1 by the triangle inequality,
jxj þ yjj a jxjj þ jyjj;
which implies by summation that kx þ yk1 a kxk1 þ kyk1. For 1 < p < y the subtle
issue to address is the finiteness of kx þ ykp. If its finiteness is demonstrated, the
proof of the inequality in (6.6) for Rn and Cn in proposition 3.24 in chapter 3, for
which finiteness was guaranteed, goes through step by step.
To demonstrate the finiteness of kx þ ykp, we note that for 1 < p < y, the func-
tion f ðxÞ ¼ xp is convex, which consistent with (3.31) means that
f ðtz1 þ ð1  tÞz2Þ a tf ðz1Þ þ ð1  tÞf ðz2Þ
for 0 a t a 1:
This function is also increasing for t A ½0; yÞ. This can be readily demonstrated with
the tools in chapter 9 on calculus, although it is intuitively apparent from sam-
ple graphs. We will assume this result and let z1 ¼ jxjj, z2 ¼ jyjj, and t ¼ 0:5. We
get by the triangle inequality that ð0:5jxj þ yjjÞp a ð0:5jxjj þ 0:5jyjjÞp since p b 1,
and
ð0:5jxjj þ 0:5jyjjÞp 1 f ð0:5jxjj þ 0:5jyjjÞ:
By the convexity of f ðxÞ above,
f ð0:5jxjj þ 0:5jyjjÞ a 0:5ðjxjjp þ jyjjpÞ:
200
Chapter 6
Series and Their Convergence

That is, ð0:5jxj þ yjjÞp a 0:5ðjxjjp þ jyjjpÞ, and hence
kx þ ykp a ð0:5Þð1pÞ=pðkxkp
p þ kykp
pÞ1=p;
which is finite. Following the exact steps of the proof of proposition 3.24, we then
derive the better estimate of the upper bound for kx þ ykp. Consequently lp-space is
closed under addition. Finally, the Minkowski inequality is also the critical step in
proving that the lp-norms are indeed norms in the sense of chapter 3, which is to
say that the triangle inequality is satisfied, since the other norm requirements are
immediate.
n
Because lp-space is a vector space, and k kp a norm, we can define a distance func-
tion or metric on lp, the lp-metric, consistent with this norm, just as it was defined in
Euclidean space, Rn and complex space Cn.
Definition 6.34
The lp-metric, dpðx; yÞ, is defined on lp by
dpðx; yÞ 1 kx  ykp
for 1 a p a y:
ð6:7Þ
The final critical property of the lp-spaces to verify is that they are complete in the
sense of chapter 4. That is, every Cauchy sequence in lp-space converges to a point in
that lp-space. In the proposition above it was proved that lp-space is closed under ad-
dition, but this gives no insight to the completeness question.
A simple example is the space of rational numbers, Q H R. Clearly, Q is closed
under addition, but equally clearly, as was seen in example 5.13, it is not complete.
That is, while a Cauchy sequence in Q may well converge to a rational number, it is
also possible that a sequence of rationals can converge to an irrational number. In
fact, because Q is dense in R, every number in R can be achieved by Cauchy se-
quences in Q.
As it turns out, the lp-spaces are complete for 1 a p a y.
Proposition 6.35
If 1 a p a y, lp is a complete normed linear space. That is, if
fxng H lp is a Cauchy sequence, then there exists x A lp so that dpðxn; xÞ 1 kxn  xkp
! 0.
Proof
The assumption that fxng is a Cauchy sequence means that for any  > 0
there is an N so that kxn  xmkp <  for n; m b N. Now, if p < y, this means that
Py
j¼1 jxnj  xmjjp < p, where xnj denotes the jth component of xn. This implies that
jxnj  xmjjp < p for every j, and so the jth components of fxng form Cauchy se-
quences in R for every j. Since R is complete, there exists xj A R so that xnj ! xj
for all j. A similar conclusion holds in the case of p ¼ y where the Cauchy property
6.2
The lp-Spaces
201

means that supjjxnj  xmjj <  for n; m b N. Defining x ¼ ðx1; x2; . . .Þ, the vector of
componentwise limits, we must now show that x A lp and that kxn  xkp ! 0. The
convergence of xn to x is immediate from the Cauchy assumption, since for any
 > 0 there is an N so that kxn  xmkp <  for n; m b N. Letting m ! y, we con-
clude that for any  > 0 there is an N so that kxn  xkp <  for n b N. Finally, to
show that x A lp, note that kxkp a kx  xNkp þ kxNkp by the Minkowski inequality,
from which we derive that kxkp a  þ kxNkp and so kxkp is finite. That is, x A lp.
n
The notion of complete normed linear space is so important in mathematics that it
warrants a special name, after Stefan Banach (1892–1945), who first identified and
studied properties of this special class of spaces:
Definition 6.36
A normed linear space, ðX; k kÞ, that is complete is called a Banach
space.
Remark 6.37
To identify our list of Banach spaces so far, we include Rn and Cn,
under any of the lp-norms, 1 a p a y, as well as all the real and complex lp-spaces,
again for 1 a p a y. In real analysis this list will be expanded to the function space
counterparts to the lp-spaces, denoted the Lp-spaces.
*6.2.3
Hilbert Space
The preceding analysis shows that all the lp-spaces are Banach spaces for 1 a p a y,
which is to say, complete normed linear spaces. As it turns out, there is one lp-space
that is more special than the rest. Specifically, l2 has the additional property that its
norm is given by an ‘‘inner product,’’ and in that respect, l2 is most like ordinary
Euclidean space Rn, or its complex counterpart Cn, for which the same point was
made concerning the ‘‘standard norm.’’ Recall from chapter 3 that the inner product
between two vectors can be defined as in (3.4) and (3.6), and that there is an intimate
relationship between these inner products and the standard norms in these spaces as
in (3.5) and (3.7), as summarized by
jxj ¼ ðx  xÞ1=2:
In the context of l2-space we formally revise these inner product definitions by
x  y ¼
X
y
j¼1
xiyi;
x; y A l2 ðrealÞ;
ð6:8Þ
x  y ¼
X
y
j¼1
xiyi;
x; y A l2 ðcomplexÞ:
ð6:9Þ
202
Chapter 6
Series and Their Convergence

To the extent these definitions can be shown to make sense, one has immediately as
in (3.5) and (3.7) for the standard l2-norms in Rn and Cn, that in either real or com-
plex l2-space:
kxk2 ¼ ðx  xÞ1=2:
ð6:10Þ
This inner product construction can be implemented in l2 and only in l2. The sub-
tlety, of course, is the demonstration that the inner products above actually converge,
since in contrast to the case for Rn and Cn, now n ¼ y. If convergence is demon-
strated, it will be straightforward to demonstrate that this inner product satisfies the
same four properties as did the inner products in Rn and Cn highlighted in defini-
tions 3.7 and 3.11 in chapter 3. That is, (6.8) satisfies the same properties as (3.4),
while (6.9) satisfies the same properties as (3.6).
To this end, the critical insight to the convergence of the series in (6.8) and (6.9) is
an inequality that was seen in chapter 3, and that was Ho¨lder’s inequality. In that
chapter this inequality was demonstrated as one of the steps toward the proof of the
Minkowski inequality. As noted above, the proof of the Minkowski inequality in lp is
identical to that in Rn and Cn, subject only to the demonstration above that kx þ ykp
is in fact finite for x; y A lp, 1 a p a y. Consequently, as a step in that proof, the
Ho¨lder inequality is also valid, and we state this without additional proof.
Proposition 6.38 (Ho¨lder’s Inequality)
Given p, q so that 1 a p; q a y, and 1
p þ 1
q
¼ 1, where notationally, 1
y 1 0, then for x A lp, y A lq,
jðx; yÞj a kxkpkykq;
ð6:11Þ
where x  y is defined in (6.8) or (6.9).
It is easy to see that this result highlights the special case of p ¼ 2. That is, this is
the only case where both x and y can be selected from the same lp-space and an inner
product defined. In this case the inner product is well defined, and has absolute value
bounded by the product of the associated l2-norms:
jðx; yÞj a kxk2kyk2;
x; y A l2:
ð6:12Þ
Another important interpretation of (6.11) that is valuable in the future context of
function spaces is that the componentwise product of two series from l2 is a series in
l1. That is, if we momentarily define the componentwise product
x  y 1 ðx1y1; x2y2; x3y3; . . .Þ;
ð6:13Þ
6.2
The lp-Spaces
203

then if x; y A l2 we have that x  y A l1 and by the Holder inequality
kx  yk1 a kxk2kyk2:
ð6:14Þ
The power of having this inner product in l2 is that is provides a basis for defining
when two points are perpendicular, or in the language of such spaces, orthogonal.
This is a natural generalization of this same notion in chapter 3 (see exercises 7 and
8 in that chapter):
Definition 6.39
If x; y A l2, then we say x and y are orthogonal, denoted x ? y; if
ðx; yÞ ¼ 0.
Of course, orthogonality is a generalization of the notion of perpendicularity in Rn
and Cn, in which ðx; yÞ ¼ 0 is also the defining relation using the standard inner
product in those spaces. The classical collection of orthogonal vectors are those
defined by the coordinate axes. For example, in Rn we have the set of n vectors
ð1; 0; 0; . . . ; 0Þ; ð0; 1; 0; . . . ; 0Þ; ð0; 0; 1; 0; . . . ; 0Þ . . . ð0; 0; 0; . . . ; 0; 1Þ;
denoted ej, for j ¼ 1; . . . ; n, and it is apparent that these vectors are orthogonal and
have unit norm or length
ðej; ekÞ ¼
0;
j 0 k,
1;
j ¼ k,

where of course, ðej; ejÞ ¼ kejk2
2, the square of the norm of ej.
Such a collection of vectors is said to be orthonormal. Here ‘‘ortho’’ is short for
orthogonal, and ‘‘normal’’ means of unit length. In this case this collection is actually
an orthonormal basis where by ‘‘basis’’ is meant that with these vectors, every other
vector in Rn can be generated using linear combinations of these. In other words, we
have for any vector x ¼ ðx1; x2; . . . ; xnÞ,
x ¼
X
n
j¼1
xjej;
where the coe‰cients, fxjg are used as scalars in what is called a linear combination
of vectors.
This construction generalizes to l2, for which an infinite sequence of vectors,
fejgy
j¼1 can be correspondingly defined. In l2, however, the meaning given to the rep-
resentation above for x is with xn 1 Pn
j¼1 xjej:
204
Chapter 6
Series and Their Convergence

x ¼
X
y
j¼1
xjej
i¤ kx  xnk2 ! 0 as n ! y:
ð6:15Þ
In both cases, Rn and l2, the norm of x can be derived from the scalar coe‰cients by
kxk2
2 ¼
X
y
j¼1
x2
j :
This perhaps feels a bit like a notational sleight of hand, as the orthonormal basis
fejgy
j¼1 is pretty trivial, and so is the expansion of x in terms of this basis and the
corresponding identity for kxk2
2. But in reality, this is just the tip of the iceberg. It
turns out that l2-space has infinitely many orthonormal bases, although we do not
prove this. The following is then a critical result on these bases.
Proposition 6.40
If fejgy
j¼1 is any orthonormal basis in Rn, Cn or l2-space, then for
any x in the respective space defined by
x ¼
X
y
j¼1
yjej;
ð6:16Þ
the coe‰cients are given by
yj ¼ ðx; ejÞ;
ð6:17Þ
and
kxk2
2 ¼
X
y
j¼1
jyjj2:
ð6:18Þ
Proof
We focus on the l2-space result, and leave Rn and Cn as an exercise. First o¤,
the expression for yj follows from (6.15), since by (6.12) we have as n ! y,
jðx  xn; ejÞj a kx  xnk2kejk2 ! 0;
and so ðxn; ejÞ ! ðx; ejÞ. But then ðxn; ejÞ ¼ yj for n b j, using the orthonormal
properties above, proving (6.17). Also, for (6.18), first note that (6.15) implies that
kxnk2 ! kxk2 as n ! y. That is, recalling that kxnk2
2 ¼ ðxn; xnÞ,
kxnk2
2  kxk2
2 ¼ kxn  xk2
2 þ 2ðx; xn  xÞ:
6.2
The lp-Spaces
205

So from (6.12) we have
jkxnk2
2  kxk2
2j a kxn  xk2
2 þ 2kxk2kxn  xk2;
and the result follows. Then, again using the orthonormal properties above, we de-
rive (6.18), since
kxnk2
2 ¼ ðxn; xnÞ ¼
X
n
j¼1
jyjj2:
n
Remark 6.41
1. The purpose of the absolute value in the identity in (6.18) is to indicate that in com-
plex l2-spaces, it is the square of the norms of these complex numbers that are summed.
2. The identity in (6.18) is known as Parseval’s identity, after Marc-Antoine Parseval
(1755–1836), who derived this identity in the more general content of L2 function
spaces. In that context, the collection of orthonormal functions used in (6.16) gave rise
to what is known as the Fourier series representation of the ‘‘function’’ x, named for
Jean Baptiste Joseph Fourier (1768–1830), who studied such functional expansions.
In real analysis this additional inner product structure in l2 is repeated in the function
space counterpart L2, and this structure has important consequences there as well,
similar to what was illustrated above.
The notion of complete normed linear space with a compatible inner product is so
important in mathematics that it warrants a special name, after David Hilbert (1862–
1943), who first identified and studied properties of this special class of infinite di-
mensional Euclidean spaces.
Definition 6.42
A normed linear space, ðX; k kÞ, that is complete and has a compati-
ble inner product is called a Hilbert space.
Remark 6.43
To identify our list of Hilbert spaces so far, we include Rn and Cn,
under the standard or l2-norm, as well as the real and complex l2-spaces. There will be
another identified later, but not until the study of real analysis, where we will be intro-
duced to the function space counterpart to the l2-spaces, denoted L2-space.
6.3
Power Series
In this section we introduce the notion of a power series that will justifiably get more
attention in chapter 9 on calculus in the study of Taylor series. Here we focus on
206
Chapter 6
Series and Their Convergence

power series of a single variable, although one can imagine that multivariate versions
are also possible, and as it turns out, important.
Definition 6.44
Given a real numerical sequence, fcngy
n¼0, the power series associated
with this sequence is notationally defined as a real function of x (or y, z, etc.), by
f ðxÞ ¼
X
y
n¼0
cnxn:
ð6:19Þ
In other words, a power series can be thought of as an infinite polynomial function
of x, defined on R. Not surprisingly, the central question to address here is the con-
vergence of the expression given in (6.19), outside of the obvious point of conver-
gence of x ¼ 0 for which f ð0Þ ¼ c0. In the later chapters on calculus, we will also
address questions such as:
1. Given a function f ðxÞ, when can this function be represented as in (6.19) for some
sequence fcngy
n¼0?
2. Given a function f ðxÞ, when can this function be approximated by a finite version
of this series, and what is the nature of the error in this case?
Utilizing the results above on the convergence of numerical series, the following
result is easily demonstrated.
Proposition 6.45
Given the power series, f ðxÞ ¼ Py
n¼0 cnxn, define
L ¼ lim sup
n!y
jcnþ1j
jcnj


:
ð6:20Þ
Then with R ¼ 1
L , this power series converges absolutely for jxj < R, diverges for
jxj > R, and is indeterminate for jxj ¼ R.
Proof
By the ratio test, the requirement for absolute convergence is that
lim sup
n!y
jcnþ1xnþ1j
jcnxnj


< 1;
which occurs exactly when jxj < R with R as defined. Similarly we conclude diver-
gence when jxj > R and that jxj ¼ R is an indeterminate case.
n
Remark 6.46
R is called the radius of convergence of the power series, and the inter-
val, jxj < R is called the interval of convergence.
6.3
Power Series
207

Example 6.47
1. If f ðxÞ ¼ Py
n¼0
x n
n! , then L ¼ lim supn!y
1
nþ1
n
o
¼ 0. Therefore R ¼ y, and this
power series converges for all x A R. In chapter 9 we will see that f ðxÞ ¼ ex.
2. If f ðxÞ ¼ Py
n¼0ð1Þn x n
nþ1 , then L ¼ lim supn!y
nþ1
nþ2
n
o
¼ 1. Therefore R ¼ 1, and
this power series converges for jxj < 1. This series diverges for x ¼ 1, producing the
harmonic series but converges for x ¼ 1 by the alternating series test. In chapter 9 we
will see that f ðxÞ ¼ lnð1 þ xÞ.
3. If f ðxÞ ¼ Py
n¼0ð1Þn 3 nx n
ðnþ1Þ a , a > 1, then L ¼ lim supn!y 3
nþ1
nþ2

	a
n
o
¼ 3. There-
fore R ¼ 1
3 , and this power series converges for jxj < 1
3 . It is also convergent for x ¼ 1
3
by the alternating series test, and for x ¼  1
3 , producing a power harmonic series.
4. If f ðxÞ ¼ Py
n¼0 xn, then L ¼ lim supn!yf1g ¼ 1. Therefore R ¼ 1, and this power
series converges for jxj < 1. This series is easily seen to diverge for x ¼ 1, and not con-
verge for x ¼ 1. In chapter 9 we will see that f ðxÞ ¼
1
1x , although this is easily
derivable as follows. Since we have convergence for jxj < 1, we can infer that xf ðxÞ ¼
Py
n¼1 xn and hence f ðxÞ  xf ðxÞ ¼ 1.
5. If f ðxÞ ¼ Py
n¼0 n!xn, then L ¼ lim supn!yfn þ 1g ! y. Therefore R ¼ 0, and
this series converges only for x ¼ 0.
An alternative approach to power series convergence comes from the Comparison
test.
Proposition 6.48
Given the power series, f ðxÞ ¼ Py
n¼0 cnxn, if f ðxÞ converges abso-
lutely for x ¼ a, then it converges absolutely for all x with jxj a jaj.
Proof
If jxj a jaj, then it is obvious that jcnxnj a jcnanj for all n, and since
Py
n¼0 jcnanj converges, so does Py
n¼0 jcnxnj by the comparison test. That is, f ðxÞ is
absolutely convergent.
n
A simple application of this last result is that every absolutely convergent numeri-
cal series gives rise to a power series that is absolutely convergent for jxj a 1. To see
this, assume that Py
n¼0 cn is an absolutely convergent numerical series. Define the
power series f ðxÞ ¼ Py
n¼0 cnxn. By assumption, f ð1Þ is absolutely convergent, so
the result follows.
Example 6.49
It was demonstrated in case 4 of example 6.9 that if xj ¼ 1
j a for a > 1,
then the power harmonic series Py
j¼1
1
j a converges, and since all terms are positive, it
converges absolutely. Consequently it is immediate that the power series
208
Chapter 6
Series and Their Convergence

f ðxÞ ¼
X
y
j¼1
x j
j a
converges absolutely at least for jxj a 1. Calculating the radius of convergence from
the previous proposition, we obtain L ¼ lim supn!y
n
nþ1

	a
n
o
¼ 1, and R ¼ 1
L ¼ 1. So
in these cases the indeterminate case of jxj ¼ R converges, although this is not deter-
minable by the ratio test.
As a final note, it will often be the case that the definition of power series requires
a small adjustment for the applications coming in chapter 9 on calculus.
Definition 6.50
Given a real numerical sequence fcngy
n¼0 and a constant a, the power
series centered on a associated with this sequence is notationally defined as a real func-
tion of x, by
f ðxÞ ¼
X
y
n¼0
cnðx  aÞn:
ð6:21Þ
The analysis above on power series convergence can be applied in this context,
with one adjustment:
Proposition 6.51
Given the power series f ðxÞ ¼ Py
n¼0 cnðx  aÞn, define
L ¼ lim sup
n!y
jcnþ1j
jcnj


:
Then f ðxÞ converges absolutely for jx  aj < R, diverges for jx  aj > R, and is inde-
terminate for jx  aj ¼ R, where R ¼ 1
L .
Proof
The proof is an immediate application of proposition 6.45 above, or can be
derived directly from the ratio test.
n
In other words, for these power series the radius of convergence is independent of a,
but the interval of convergence is shifted from being ‘‘centered on 0’’ with jxj < R, to
being ‘‘centered on a’’ with jx  aj < R, justifying the name.
*6.3.1
Product of Power Series
The discussion in this section relates to the product of two functions given by power
series. Obviously, if f ðxÞ and gðxÞ are any two functions, the function hðxÞ 1
f ðxÞgðxÞ is well defined. The question here is, if f ðxÞ and gðxÞ are given as convergent
6.3
Power Series
209

power series centered on a, with respective radii of convergence of R and R0, what is
the power series representation of hðxÞ and what is its radius of convergence? The
following proposition addresses this question:
Proposition 6.52
Let f ðxÞ and gðxÞ be given as convergent power series centered
on a,
f ðxÞ ¼
X
y
n¼0
bnðx  aÞn;
gðxÞ ¼
X
y
n¼0
cnðx  aÞn;
with respective radii of convergence of R and R0. Then hðxÞ 1 f ðxÞgðxÞ is given by the
power series
hðxÞ ¼
X
y
n¼0
dnðx  aÞn;
ð6:22Þ
where
dn ¼
X
n
j¼0
bjcnj:
ð6:23Þ
Further the radius of convergence of hðxÞ is R00 ¼ minðR; R0Þ.
Proof
The formula for the coe‰cients in (6.23) follows immediately from the obser-
vation that when multiplying these series, the only way that the product of a
bjðx  aÞ j term from the expansion of f ðxÞ and a ckðx  aÞk term from the expan-
sion of gðxÞ can contribute to the coe‰cient of ðx  aÞn is to have j þ k ¼ n. So
we see that this formula for dn simply accounts for all such products. The question
of convergence of (6.22) is the more di‰cult question which is addressed next. To
simplify notation, let fmðxÞ denote the partial summation
fmðxÞ ¼
X
m
n¼0
bnðx  aÞn;
and ~fmðxÞ ¼ f ðxÞ  fmðxÞ, which is given by the summation
~fmðxÞ ¼
X
y
n¼mþ1
bnðx  aÞn:
210
Chapter 6
Series and Their Convergence

Using similar notation for gðxÞ and hðxÞ, and noting that the finite double summa-
tions such as Pm
n¼0
Pn
j¼0 can be reversed to Pm
j¼0
Pm
n¼ j, we have for jx  aj < R00,
due to the convergence of both f ðxÞ and gðxÞ,
hmðxÞ ¼
X
m
n¼0
X
n
j¼0
ðbjðx  aÞ jÞðcnjðx  aÞnjÞ
"
#
¼
X
m
j¼0
bjðx  aÞ j X
m
n¼j
cnjðx  aÞnj
¼
X
m
j¼0
bjðx  aÞ jgmjðxÞ
¼ gðxÞ
X
m
j¼0
bjðx  aÞ j 
X
m
j¼0
ðbjðx  aÞ jÞ~gmjðxÞ:
Now
Pm
j¼0 bjðx  aÞ j ! f ðxÞ
as
m ! y.
If
it
can
be
shown
that
Pm
j¼0 bjðx  aÞ j ~gmjðxÞ ! 0 absolutely, the proof will be complete since then
hmðxÞ  gðxÞ
X
m
j¼0
bjðx  aÞ j


 ! 0:
Now since ~gnðxÞ ! 0, for any  > 0 there is an N so that j~gnðxÞj <  for n > N. To
have j~gmjðxÞj <  requires j < m  N, and so for m large enough,
X
m
j¼0
bjðx  aÞ j ~gmjðxÞ


a
X
mN1
j¼0
jbjðx  aÞ j ~gmjðxÞj þ
X
m
j¼mN
jbjðx  aÞ j ~gmjðxÞj
< 
X
y
j¼0
jbjðx  aÞ jj þ
X
m
j¼mN
jbjðx  aÞ j ~gmjðxÞj
¼ KðxÞ þ
X
N
j¼0
jbmjðx  aÞmj ~gjðxÞj
a KðxÞ þ max
0ajaN j~gjðxÞj
max
0ajaN jbmjðx  aÞmjj:
6.3
Power Series
211

Note that the first summation converged to a finite value, KðxÞ say, for any x, be-
cause the power series for f ðxÞ is absolutely convergent. Also the second term con-
verges to 0 as m ! y because the finite collection f~gjðxÞgN
j¼0 is bounded for any
x, and the maximum of the finite collection fjbmjðx  aÞmjjgN
j¼0 converges to 0 as
m ! y, again because the power series for f ðxÞ is absolutely convergent.
n
*6.3.2
Quotient of Power Series
One important application of the proposition above is to generate the coe‰cients
of the reciprocal of a power series, or the quotient of two power series. Specifically,
the proposition above assures that if
f ðxÞgðxÞ ¼ hðxÞ;
X
y
n¼0
bnðx  aÞn X
y
n¼0
cnðx  aÞn ¼
X
y
n¼0
dnðx  aÞn;
then the coe‰cients fdng satisfy (6.23). Consequently, if f ðxÞ and hðxÞ are given, and
if coe‰cients fcng can be found that satisfy (6.23) and produce a convergent power
series, then we can conclude that
X
y
n¼0
cnðx  aÞn ¼ hðxÞ
f ðxÞ :
And in the special case where hðxÞ 1 1, the reciprocal of f ðxÞ is produced.
Of course, to have any hope that the resultant expansion is convergent in an inter-
val of a, we require that f ðaÞ 0 0, which is equivalent to b0 0 0. In such a case the
equations in (6.23) can be solved for fcng iteratively, producing after re-indexing for
visual appeal,
c0 ¼ d0
b0
;
cn ¼ 1
b0
dn 
X
n1
j¼0
bnjcj
"
#
;
n b 1:
ð6:24Þ
We now show that the condition b0 0 0 is su‰cient to ensure that Py
n¼0 cnðx  aÞn
is an absolutely convergent power series.
212
Chapter 6
Series and Their Convergence

Proposition 6.53
Let f ðxÞ and hðxÞ be given as convergent power series centered
on a:
f ðxÞ ¼
X
y
n¼0
bnðx  aÞn;
hðxÞ ¼
X
y
n¼0
dnðx  aÞn;
with common radius of convergence of R, and where f ðaÞ ¼ b0 0 0. Then gðxÞ 1 hðxÞ
f ðxÞ
is given by the power series
gðxÞ ¼
X
y
n¼0
cnðx  aÞn;
where fcng satisfy (6.24), and this series is absolutely convergent on jx  aj < R0 for
some R0 > 0.
Proof
We prove this proposition in two steps.
1. Assume that we can prove this result for hðxÞ 1 1, where fc0
ng satisfy (6.24) with
d0 ¼ 1 and dn ¼ 0 for all n b 1. In other words,
1
f ðxÞ ¼
X
y
n¼0
c0
nðx  aÞn
is absolutely convergent, where
c0
n ¼
1
b0 ;
n ¼ 0,
1
b0
Pn1
j¼0 bnjc0
j;
n b 1.
8
<
:
ð6:25Þ
Then by the proposition above, gðxÞ ¼ hðxÞ
1
f ðxÞ is well defined:
gðxÞ ¼
X
y
n¼0
cnðx  aÞn;
where by (6.23), stated in terms of fc0
ng and fdng,
cn ¼
X
n
j¼0
djc0
nj ¼
d0
b0 ;
n ¼ 0,
1
b0 ½dn  Pn1
j¼0 dj
Pnj1
k¼0
bnjkc0
k;
n b 1.
8
<
:
6.3
Power Series
213

We must now show that this definition of cn is equivalent to (6.24). In this summa-
tion for n b 1, we define a new index variable l ¼ j þ k and observe that given j, we
have j a l a n  1. Therefore
X
n1
j¼0
X
nj1
k¼0
djbnjkc0
k ¼
X
n1
j¼0
X
n1
l¼ j
bnldjc0
lj
¼
X
n1
l¼0
bnl
X
l
j¼0
djc0
lj
¼
X
n1
l¼0
bnlcl;
where we reversed the double summation Pn1
j¼0
Pn1
l¼ j ¼ Pn1
l¼0
Pl
j¼0 in the second
line. Substituting this final result into the definition above for cn produces (6.24) as
desired.
2. To prove (6.24) in the special case of hðxÞ 1 1, first note that we can assume that
b0 ¼ 1, since this term can be factored out of the series without changing conver-
gence properties, and factored back in as 1
b0 after the inversion. Now since the power
series for f ðxÞ converges for jx  aj ¼ r < R, its terms must converge to 0. Hence its
terms are bounded, jbnjrn a M. Therefore
jbnj a M
rn :
For convenience below we take M > 1. With c0
n defined as the coe‰cients of
1
f ðxÞ
above with b0 ¼ 1, we now show by induction that
jc0
nj a 2n M n
rn :
Since c0
0 ¼ 1, we assume this statement is true for n and evaluate c0
nþ1. Then by (6.25),
jc0
nþ1j ¼
X
n
j¼0
bnþ1jc0
j


a
X
n
j¼0
M
rnþ1j 2 j M j
r j
214
Chapter 6
Series and Their Convergence

< M nþ1
rnþ1
X
n
j¼0
2 j
< 2nþ1 M nþ1
rnþ1 :
Since the power series coe‰cients for
1
f ðxÞ are bounded in absolute value by a geomet-
ric series, we conclude that this series converges if
2n M n
rn jx  ajn < 1:
So the interval of absolute convergence contains
jx  aj <
r
2M :
n
6.4
Applications to Finance
6.4.1
Perpetual Security Pricing: Preferred Stock
The most apparent application of numerical series to finance is the evaluation of the
price of common stock or nonredeemable preferred stock, both ‘‘perpetual’’ secu-
rities. A preferred stock with par value of 1000 and dividend rate of 5% on an annual
basis pays 50 per year to the investor in perpetuity. In general, with par value of F
and dividend rate d on an annual basis, the investor receives Fd per year in perpetu-
ity. For an investor desiring a fixed yield of r on an annual basis, and assuming the
next dividend is one year into the future, the appropriate price function is given as
PðrÞ ¼ Fd
X
y
j¼1
ð1 þ rÞj:
ð6:26Þ
From the methods above on numerical series we conclude that for any r > 0, this
price function converges absolutely as noted in section 2.3.2, to
PðrÞ ¼ Fd
r :
This model is easily generalized to di¤erent dividend payment frequencies and/or
yield nominal bases.
6.4
Applications to Finance
215

A more general model of yearly varying yields is easily handled formally. Now the
price is a function of a sequence of yields, frjg, and
PðfrjgÞ ¼ Fd
X
y
j¼1
ð1 þ rjÞj:
ð6:27Þ
But the question of convergence is more subtle. Clearly, if there is an r > 0 so that
rj b r for all j, then by the comparison test, PðfrjgÞ converges and PðfrjgÞ a PðrÞ.
Consequently the only question is, if rj > 0 for all j, but rj ! 0, does this price
converge? However, the question is not really about the stronger condition of con-
vergence of rj ! 0; it is only about the weaker condition of frjg having 0 as a possi-
ble accumulation point. This can be problematic, since it is then possible that
infinitely many terms in the summation are large enough to cause divergence. As
was seen in section 5.2, this accumulation point condition can be expressed as
lim infj!y rj ¼ 0.
To investigate the question of convergence, we apply the ratio test to this series.
The criterion for convergence is that
lim sup
n!y
ð1 þ rjþ1Þj1
ð1 þ rjÞj
(
)
¼ L < 1:
By proposition 5.22 this condition is satisfied if and only if for any  > 0 there is
an N so that j b N,
ð1 þ rjþ1Þ jþ1 b ð1 þ rjÞ j
L þ 
:
Choosing  so that L þ  < 1 and iterating, we derive that with j ¼ N þ k and
k b 1:
ð1 þ rNþkÞNþk b ð1 þ rNÞN
ðL þ Þk :
That is,
rNþk b ð1 þ rNÞN=ðNþkÞ
ðL þ Þk=ðNþkÞ  1;
which appears to be a bound on the rate at which rj ! 0.
216
Chapter 6
Series and Their Convergence

But closer inspection reveals more. As k ! y, it is clear that
k
Nþk ! 1 and hence
ðL þ Þk=ðNþkÞ ! L þ . Also,
N
Nþk ! 0, and assuming that rN > 0, we conclude that
ð1 þ rNÞN=ðNþkÞ ! 1. Consequently the lower bound for rNþk converges to
1
Lþ  1 ¼
1L
Lþ , which exceeds 0 if L þ  < 1.
Hence we obtain that as k ! y, the ratio test assures convergence of the preferred
stock price only when for some L0 ¼ L þ  < 1,
lim inf
j!y
rj b 1  L0
L0
;
and hence we return to the case where the sequence is bounded away from 0. That is,
this condition implies that for any  > 0 there is an N so that rj > 1L 0
L0   for all
j b N.
Of course, this does not prove that there is no sequence frjg with lim infj!y rj ¼ 0
for which the preferred stock price converges, it only proves that there is no such se-
quence for which convergence is verifiable by the ratio test.
With a similar analysis, one could anticipate the convergence of this pricing func-
tion for nonconstant dividends. Again, if these dividends are bounded from above,
dj a d for all j, the price function PðrÞ ¼ F Py
j¼1 djð1 þ rÞj is easily seen to con-
verge by the comparison test. For unbounded dividends, the answer is more subtle,
but insights can often be developed with the aid of the ratio test.
6.4.2
Perpetual Security Pricing: Common Stock
A similar analysis can be implemented for the price of common stock under the dis-
counted dividend model introduced in section 2.3.2. From (2.22) we have that the
price—as a function of the last annual dividend assumed to have been just paid D,
the annual dividend growth rate g, and the investor required yield r—is
VðD; g; rÞ ¼ D
X
y
j¼1
ð1 þ rÞjð1 þ gÞ j
¼ D
X
y
j¼1
1 þ r  g
1 þ g

j
:
For fixed r and g, the analysis above for preferred stock indicates that this price con-
verges as long as r > g, and in this case we have as in (2.22),
6.4
Applications to Finance
217

VðD; g; rÞ ¼ D 1 þ g
r  g ;
r > g:
To generalize this in contemplation of a growth rate sequence fgjg and yield se-
quence frjg, we apply the same considerations as for preferred stock. Convergence
by the ratio test is assured if the e¤ective discount rates are bounded away from 0,
that is, rjgj
1þgj b r > 0. But this approach may be challenged if these rates converge
to 0.
6.4.3
Price of an Increasing Perpetuity
In addition to pricing formulas for perpetuities with constant and geometrically
increasing payments discussed above, we can apply double summations methods to
value a linearly increasing payment stream with a fixed annual rate. Generalizations
to this payment model are then discussed.
First, if the perpetuity payment at time j is Dj ¼ aj þ b for constants a and b, then
by linearity,
VðDj; rÞ ¼ a
X
y
j¼1
jð1 þ rÞj þ b
X
y
j¼1
ð1 þ rÞj;
and only the first summation has not yet been evaluated. Writing j ¼ P j
i¼1 1, we
have
X
y
j¼1
jð1 þ rÞj ¼
X
y
j¼1
X
j
i¼1
ð1 þ rÞj
¼
X
y
i¼1
X
y
j¼i
ð1 þ rÞj:
Reversing the summations will be justified once we demonstrate convergence, which
will imply absolute convergence.
Now
X
y
j¼i
ð1 þ rÞj ¼ ð1 þ rÞiþ1 X
y
j¼1
ð1 þ rÞj ¼ ð1 þ rÞiþ1
r
:
Substituting into the double sum, we obtain
218
Chapter 6
Series and Their Convergence

X
y
j¼1
jð1 þ rÞj ¼ 1 þ r
r2
:
ð6:28Þ
The last answer makes sense because 1
r is the value of a perpetuity of 1s payable
annually from t ¼ 1 forward, so 1
r2 is the value of a perpetuity of perpetuities, where-
by 1
r is paid annually from t ¼ 1 forward. The first such perpetuity provides for a se-
ries of 1s annually from t ¼ 2 forward, the second for a series of 1s annually from
t ¼ 3 forward, so it is clear that the total payment is growing linearly. However, 1
r2
starts payment one year later than desired, so the multiplicative factor of 1 þ r
adjusts for this. Combining results, we obtain
VðDj; rÞ ¼ að1 þ rÞ
r2
þ b
r ;
Dj ¼ aj þ b:
ð6:29Þ
The double-summations approach can be generalized to present values of the form
Pn 1 Py
j¼1 j nð1 þ rÞj. However, rather than obtaining an explicit formula as in the
case of n ¼ 0; 1, we derive an iterative formula whereby we give Pn in terms of
fP0; P1; . . . ; Pn1g. Of course, here P0 ¼ 1
r , and P1 ¼ 1þr
r2 .
There are two ways to develop this iterative formula. First, we can proceed as
above and write multiple series:
X
y
j¼1
j nð1 þ rÞj ¼
X
y
j¼1
X
j n
i¼1
ð1 þ rÞj
¼
X
y
i¼1
X
y
j¼nðiÞ
ð1 þ rÞj;
where nðiÞ ¼ k þ 1 for k n þ 1 a i a ðk þ 1Þn and for k b 0. In other words, we have
nðiÞ ¼
1;
i ¼ 1,
2;
2 a i a 2n,
3;
2n þ 1 a i a 3n,
..
.
..
.
k þ 1;
k n þ 1 a i a ðk þ 1Þn.
8
>
>
>
>
>
>
<
>
>
>
>
>
>
:
Then the inner sums can be collected into groups for fixed nðiÞ, and the outer sum
converted to index k b 0, producing
6.4
Applications to Finance
219

X
y
j¼1
j nð1 þ rÞj ¼
X
y
k¼0
½ðk þ 1Þn  k n
X
y
j¼kþ1
ð1 þ rÞj
¼
X
y
k¼1
X
n1
i¼0
n
i


k i
"
#
ð1 þ rÞk
r
þ 1
r
¼ 1
r
X
n1
i¼0
n
i

 X
y
k¼1
k ið1 þ rÞk þ 1
"
#
;
since Py
j¼kþ1ð1 þ rÞj ¼ ð1 þ rÞk Py
j¼1ð1 þ rÞj ¼ ð1þrÞk
r
.
Note that a bit of care is necessary for the k-summation, which is split as Py
k¼0 ¼
Py
k¼1 þ P
k¼0, to avoid 00 in the second step where the binomial theorem (see chap-
ter 8 for details) was used. This theorem states that with n! (‘‘n factorial’’) defined by
n! ¼ nðn  1Þðn  1Þ . . . ð2Þð1Þ and with 0! 1 1,
ðk þ 1Þn ¼
X
n
i¼0
n
i


k i;
n
i


1
n!
i!ðn  iÞ! :
So rewriting, we obtain
Pn ¼ 1
r
X
n1
i¼0
n
i


Pi þ 1
"
#
;
n ¼ 2; 3; . . . ;
ð6:30Þ
where
P0 ¼ 1
r ;
P1 ¼ 1 þ r
r2
:
This formula is also valid for n ¼ 1, with only the initial value P0 ¼ 1
r .
See exercise 15 for an alternative derivation.
6.4.4
Price of an Increasing Payment Security
The price of a security such as a bond or mortgage, or a fixed term annuity with lin-
early increasing payments, is now easily handled. Specifically, with Dj ¼ aj þ b for
j ¼ 1; . . . ; n,
220
Chapter 6
Series and Their Convergence

VðDj; rÞ ¼ a
X
n
j¼1
jð1 þ rÞj þ b
X
n
j¼1
ð1 þ rÞj:
Now the second summation equals an:r by (2.11), while
X
n
j¼1
jð1 þ rÞj ¼
X
y
j¼1
jð1 þ rÞj 
X
y
j¼nþ1
jð1 þ rÞj:
Here the first summation is the perpetuity above in (6.28), while the second splits as
X
y
j¼nþ1
jð1 þ rÞj ¼
X
y
j¼1
ðj þ nÞð1 þ rÞjn
¼ ð1 þ rÞn n
X
y
j¼1
ð1 þ rÞj þ
X
y
j¼1
jð1 þ rÞj
"
#
:
Combining and simplifying, and using notation from chapter 2, we derive for the first
summation
X
n
j¼1
jð1 þ rÞj ¼ ð1 þ rÞ an:r
r  nð1 þ rÞn
r
:
ð6:31Þ
This formula can again be intuited from the component parts. The term an:r
r pro-
vides a perpetuity that pays an:r at each of times 1; 2; 3; . . . , each of which is in turn
equivalent to a series of n payments of 1 starting one year later. So collectively this
perpetuity provides for a payment stream that grows from 1 to n at times 2 to n þ 1,
and is then frozen at level n from time n þ 2 forward. The 1 þ r factor puts these
increasing payments at times 1 to n, and the frozen payments of n from time n þ 1
onward. The second term eliminates the payments of n from time n þ 1 onward,
since n
r is a perpetuity of n per year starting at time 1 and the ð1 þ rÞn factor moves
these payments to start at time n þ 1.
By defining Am ¼ Pn
j¼1 j mð1 þ rÞj, we can again split this increasing annuity as
Am ¼
X
y
j¼1
j mð1 þ rÞj 
X
y
j¼nþ1
j mð1 þ rÞj
¼ Pm  ð1 þ rÞn X
y
j¼1
ðj þ nÞmð1 þ rÞj:
ð6:32Þ
6.4
Applications to Finance
221

The binomial theorem can be applied to the second summation, producing a formula
involving fPjgm
j¼0 (see exercise 28).
6.4.5
Price Function Approximation: Asset Allocation
The primary application of power series in finance is to the problem of modeling and
understanding the behavior of a complicated function f ðxÞ in a neighborhood of
some fixed point a A R, or in the more general case, a multivariate function f ðxÞ in
a neighborhood of a A Rn. For example, f ðxÞ might denote the price of a bond when
x is the bond’s yield to maturity (YTM), and a denotes the yield today. Of course, as
this price function is not very complicated, one could argue that to understand its
behavior as the YTM changes from a to x, we simply can generate additional prices.
However, this prospect becomes more daunting if one is managing a portfolio of
such bonds, or if the price calculations are made more complex by the presence of
embedded options like calls (i.e., early prepayment option for the issuer).
In more general multivariate cases, f ðxÞ might reflect a given bond’s or bond port-
folio’s price as a function of a given yield curve, parametrized as a vector of values
x A Rn as noted in section 3.3.1, with f ðaÞ the value on the current yield curve as
parametrized by the vector a. Prices of preferred stock, or common stock with the
formulas above, can also be contemplated as a single variable or as multivariate
functions. In each case the vector a denotes the collection of parameters that deter-
mine today’s prices, and we are interested in approximating how prices change as
these parameters change from a to x.
A di¤erent kind of problem might be contemplated in the context of asset alloca-
tion. For example, for a given allocation vector a denoting the proportionate alloca-
tion to the various asset classes, one might develop a function f ðaÞ that quantifies
return expectations, and another function gðaÞ that quantifies risk expectations, given
the current allocation vector. The analysis undertaken is one of understanding the
behaviors of these functions in a neighborhood of a to investigate the possibilities of
improving both return and risk through allocation changes, or at least to quantify
the trade-o¤ between risk and return.
In all such cases, as the complexity of the calculations increases, the utility and
attractiveness of developing reasonable approximations also increases. To this end,
methods discussed in chapter 9 on calculus will provide a basis for determining a
sequence of coe‰cients, fcjg, which may be finite or infinite. In the special infinite
case, we will have
f ðxÞ ¼
X
y
n¼0
cnðx  aÞn;
222
Chapter 6
Series and Their Convergence

while in the finite case,
f ðxÞA
X
N
n¼0
cnðx  aÞn:
Both cases easily support approximations when x is ‘‘close to’’ a.
For example, assume that with either expansion above, with N > 2 say, that we
attempt a linear approximation:
f ðxÞAc0 þ c1ðx  aÞ:
Then in either case we conclude that the absolute error in this approximation, using
the triangle inequality, is bounded by
j f ðxÞ  ½c0 þ c1ðx  aÞj a jc2jðx  aÞ2 X
N
n¼2
cn
c2
ðx  aÞn2


:
That is, as x ! a the relative error satisfies
j f ðxÞ  ½c0 þ c1ðx  aÞj
jc2jðx  aÞ2
! 1:
ð6:33Þ
This implies that for x @ a, the absolute error is of order of magnitude jc2jðx  aÞ2.
Similarly one can show that the absolute error in the approximation f ðxÞAc0 is
of order of magnitude jc1j jx  aj, and similarly for approximations using higher
order polynomials in ðx  aÞ. Ultimately the ability to approximate f ðxÞ depends
on how many terms in the series above the given function allows. When only finitely
many terms are possible, approximation accuracy is limited but may still be adequate
for applications. Otherwise, any given degree of accuracy is possible in theory as
long as the analyst is willing to calculate additional terms in the approximating
polynomial.
6.4.6
lp-Spaces: Banach and Hilbert
The importance of these series spaces in finance is really that they provide an intro-
duction to some subtle and important concepts in higher mathematics in an intuitive
and accessible environment. The power of these concepts will only achieve full appli-
cability in later studies on real analysis and stochastic processes, where these spaces
are re-introduced as the Lp function spaces in general, and most important for sto-
chastic processes, the special Hilbert space L2. Consequently, while not of imme-
diate application, these spaces and their properties, in addition to the examples of
6.4
Applications to Finance
223

Euclidean and complex spaces Rn and Cn, will provide a solid foundation of exam-
ples that can be used to aid intuition in these admittedly more abstract settings.
In other words, the goal of this material in this chapter is to make the important
but necessarily more remote setting of Lp-space better understood as a generalization
of an accessible and familiar idea, than as an isolated and abstract construction.
Exercises
Practice Exercises
1. Show that if Py
n¼1 bn is a convergent series, then as a sequence, bn ! 0. (Hint:
Consider the Cauchy criterion.)
2. Use the comparison test to demonstrate the absolute convergence of the following
series, by comparing them to series shown to converge in this chapter:
(a) Py
n¼1
ðln nÞ2
n4
(b) Py
n¼1
ln n
n p for p > 2
(c) Py
n¼1ð1Þnþ1 sinðnÞ
n p , for p > 1, where for sinðnÞ, n is understood in radians (i.e., p
radians ¼ 180)
(d) Py
n¼1ð1Þnþ1an for 0 < a < 1
3. Use the alternating series test or other means to demonstrate that the following
converge and determine which converge absolutely:
(a) Py
n¼1
ð1Þ nþ1
lnðnþ1Þ
(b) Py
n¼1
ð1Þ nþ1 lnðn!Þ
n!
(c) Py
n¼1
ð1Þ nþ1 lnðnÞ
n p
for p b 1
(d) Py
n¼1ð1Þnþ1 ln nþ1
n


4. For each series in exercise 2, demonstrate absolute convergence using the compar-
ative ratio test. In other words, in each case determine an absolutely convergent se-
ries Py
i¼1 cn so that if an denotes the original series, janj
jcnj converges as n ! y.
5. For the series in exercises 2 and 3, identify which would be declared as absolutely
convergent using the ratio test, which would be not convergent, and which would be
inconclusive.
6. Given a real number x A ½0; 1, with decimal expansion x ¼ 0:a1a2a3 . . . , where
each aj A f0; 1; 2; . . . ; 9g, identify x with the sequence, x A Ry defined by x ¼ ðx1;
x2; . . . ; xj; . . .Þ, where xj ¼
aj
10 j .
224
Chapter 6
Series and Their Convergence

(a) Confirm that so defined, x A lp for all p, 1 a p a y.
(b) Show that the truncated point sequence xn A Ry
0 , defined by xn ¼ ðx1; x2; . . . ; xn;
0; 0; 0; . . .Þ, converges to x in the l1-norm.
(c) Generalize part (b) to show that kx  xnkp ! 0 for all p, 1 a p a y.
(d) Show that if the real number x is identified with the sequence y A Ry, defined by
y ¼ ða1; a2; . . . ; aj; . . .Þ, that y A lp only for p ¼ y, yet even in this case, ky  ynky n
0, where yn ¼ ða1; a2; . . . ; an; 0; 0; 0; . . .Þ unless y A Ry
0 .
7. Using the Minkowski inequality, demonstrate that the following series are abso-
lutely convergent:
(a) Py
n¼1
n1:5
ðnþ2Þ2  ð1Þ nþ1
ffiffin
p


p
for p > 2.
(b) Py
k¼1
ð1Þ kþ1ðkþ1Þ
kðkþ10Þ
 ln k
k2  ð0:5Þk


p
for p > 1.
8. Determine the radius of convergence and interval of convergence for the following
power series:
(a) uðzÞ ¼ Py
n¼1
z n
n
(b) f ðxÞ ¼ Py
m¼0ð1Þmðx  1Þm
(c) gðyÞ ¼ Py
n¼1ð1Þnþ1npðy þ 2Þn for p > 0
(d) hðzÞ ¼ Py
k¼1
ðz4Þ k
k
(e) wðxÞ ¼ Py
j¼1 a jðx þ 1Þ j, a > 0
(f ) vðyÞ ¼ Py
m¼0
ð y10Þ m
ðmþ1Þðmþ2Þ
(g) kðyÞ ¼ Py
n¼1 nnðy þ 4Þn
(h) mðuÞ ¼ Py
n¼1
2 nu n
n
9. With f ðxÞ ¼ Py
n¼0
x n
n! , develop the series expansion for ðf ðxÞÞ2 using (6.23), and
show that ð f ðxÞÞ2 ¼ f ð2xÞ. (Hint: As will be demonstrated in (7.14) in chapter 7,
2n ¼ Pn
j¼0
n!
j!ðn jÞ! using the binomial theorem.)
10. Generalize exercise 9 to show that for all n A N, ðf ðxÞÞn ¼ f ðnxÞ. (Hint: Use
induction.)
11. Confirm that for a preferred stock or common stock with nonconstant dividends
fdjg, where dj ¼ a1j þ a0, a1; a0 b 0, the price function PðrÞ ¼ Py
j¼1 djð1 þ rÞj is ab-
solutely convergent for r > 0. (Hint: Consider the ratio test.)
12. Consider the preferred or common stock pricing function applied to the case of
general nonconstant dividends PðrÞ ¼ Py
j¼1 djð1 þ rÞj. Use the ratio test to develop
bounds on the greatest rate of dividend growth allowable, which will ensure conver-
gence for r > 0.
Exercises
225

13. With a semi-annual yield rate of r ¼ 0:10:
(a) Value a semiannual payment perpetuity that pays 10j þ 15 at time j ¼ 0:5; 1:0;
1:5 . . . .
(b) What is the semiannual payment increase for a 20 year $10 million semiannual
payment mortgage where the borrower wants the payments to increase by equal
amounts each payment and the first payment to be $0:25 million?
14. With an annual rate of 15%:
(a) Price a common stock with an annual dividend growth rate of 10% if the next
dividend, due tomorrow, is expected to be $5.
(b) What is the price of the stock in part (a) if dividends are projected to grow for
only 5 years at the 10% rate, then decrease to a growth rate of 5%?
15. With Pn defined as in the chapter by Pn 1 Py
j¼1 j nð1 þ rÞj:
(a) Derive (6.30),
Pn ¼ 1
r
X
n1
i¼0
n
i


Pi þ 1
"
#
:
(Hint: Note that
X
y
j¼1
j nð1 þ rÞj ¼ ð1 þ rÞ1 þ ð1 þ rÞ1 X
y
j¼1
ðj þ 1Þnð1 þ rÞj
and expand ðj þ 1Þn with the binimial theorem of (7.15) as seen in this chapter’s
derivation.)
(b) Develop explicit formulas for Pn, n ¼ 2; 3; 4; 5 using P0 ¼ 1
r and P1 ¼ 1þr
r2 .
16. Starting with the powers series, f ðxÞ ¼ Py
n¼0
x n
n! , consider the linear approxima-
tion f1ðxÞ ¼ 1 þ x. As indicated in (6.33),
f ðxÞ  ð1 þ xÞ
x2
2
! 1;
as x ! 0. Demonstrate this result by calculating the power series for this ratio func-
tion, and confirming that it is absolutely convergent, which then justifies a substitu-
tion of x ¼ 0.
226
Chapter 6
Series and Their Convergence

Assignment Exercises
17. Use the comparison test to demonstrate the absolute convergence of the follow-
ing series, by comparing them to series shown to converge in this chapter:
(a) Py
n¼1 cnan for 0 < a < 1 and any bounded sequence fcng
(b) Py
j¼1ð1Þ jþ1
1
j
 	q
ln j for q > 2
(c) Py
k¼1
ðkþ2Þ2
kðkþ1Þðkþ10Þ2
(d) Py
k¼1
ð1Þ kðkþ2Þ3
k!
18. Use the alternating series test to demonstrate that the following converge and de-
termine which converge absolutely:
(a) Py
n¼1
ð1Þ nþ1 lnðnþ1Þ
n4
(b) Py
n¼1
ð1Þ nþ1np
a n
, p A R, a > 1
(c) Py
n¼1
ð1Þ nþ1n2
n3þ1
(d) Py
n¼1
ð1Þ nþ1n
ln½ðnþ1Þ n
19. For each series in exercise 17, demonstrate absolute convergence using the com-
parative ratio test. In other words, in each case determine an absolutely convergent
series Py
i¼1 cn so that if an denotes the original series, then janj
jcnj converges as n ! y.
20. For the series in exercises 17 and 18, identify which would be declared as abso-
lutely convergent using the ratio test, which would be not convergent, and which
would be inconclusive.
21. Proposition 6.7 states that if Py
j¼1 xj and Py
j¼1 yj are absolutely convergent,
then so too is Py
j¼1 xjyj.
(a) Show that if Py
j¼1 xj is absolutely convergent, and Py
j¼1 yj conditionally conver-
gent, then again Py
j¼1 xjyj is absolutely convergent.
(b) Give an example of conditionally convergent Py
j¼1 xj and Py
j¼1 yj for which
Py
j¼1 xjyj is not convergent. (Hint: Can xj and yj be defined to satisfy the assump-
tions yet with xjyj ¼ 1
j ?)
22. Prove that parts (c) and (d) of Exercise 6 have nothing to do with the base-10
assumption in the decimal expansion. In other words, if b is any positive integer,
b b 2, and each such x A ½0; 1 is expanded in base-b so that x ¼ 0:a1a2a3 . . . , where
each aj A f0; 1; 2; . . . ; b  1g, then again:
(a) With x A Ry defined by x ¼ ðx1; x2; . . . ; xj; . . .Þ, where xj ¼ aj
b j , and xn A Ry
0 is
defined as before, we have that kx  xnkp ! 0 for all p, 1 a p a y.
Exercises
227

(b) With y A Ry defined by y ¼ ða1; a2; . . . ; aj; . . .Þ, where xj ¼ aj, we have that y A lp
only for p ¼ y; yet even in this case ky  ynky n 0, where yn ¼ ða1; a2; . . . ; an; 0; 0;
0; . . .Þ unless y A Ry
0 .
23. Consider two sequences, x ¼ ðx1; x2; . . . ; xj; . . .Þ, where xj ¼ aj, and y defined
by yj ¼ bj, where a; b > 1:
(a) Confirm that x; y A lp for all p, 1 a p a y, and calculate the associated lp-
norms.
(b) Calculate the inner product ðx; yÞ, which is well defined.
(c) Develop the implication of Ho¨lder’s inequality, that for 1 a p; q a y, with
1
p þ 1
q ¼ 1, where notationally,
1
y 1 0, we have jðx; yÞj a kxkpkykq. Express the in-
equality in terms of one parameter, say with q ¼
p
p1 .
(d) Express the inequality in part (c) in the special case of p ¼ q ¼ 2.
24. Determine the radius of convergence and interval of convergence for the follow-
ing power series:
(a) f ðxÞ ¼ Py
m¼1
ð1Þ mðx5Þ m
m
(b) gðyÞ ¼ Py
n¼1 npðy  6Þn for p > 0
(c) hðzÞ ¼ Py
k¼1
ðz4Þ k
k!
(d) tðzÞ ¼ Py
k¼1ð1Þk ðzþ1Þk
k!
(e) wðxÞ ¼ Py
j¼1 ajðx  2Þ j, a > 0
(f ) vðyÞ ¼ Py
m¼0
ðyþ2Þm
ðmþ1Þ2
(g) kðzÞ ¼ Py
n¼1 n!ðz þ 1000Þn
(h) nðuÞ ¼ Py
n¼1
c nu n
n , c > 0
25. Generalize exercise 11 to an arbitrary polynomial growth dividend model dj ¼
Pn
k¼0 ak j k, ak b 0 for all k.
26. With an monthly rate of r ¼ 0:06:
(a) Value a monthly payment perpetuity that pays 12j þ 3 at time j.
(b) What is the monthly payment increase for a 30-year, $5 million monthly pay-
ment mortgage, where the borrower wants the payments to increase by equal
amounts each payment, and the first payment to be $10,000?
27. With an annual rate of 18%:
(a) Price a common stock with a semiannual nominal dividend growth rate of 8% if
the next dividend, due tomorrow, is expected to be $15.
228
Chapter 6
Series and Their Convergence

(b) What is the price of the stock in part (a) if dividends are projected to grow for
only 3 years at the 8% rate and then increase to a growth rate of 12%?
28. Defining the increasing n-pay annuity, Am ¼ Pn
j¼1 j mð1 þ rÞj, use the formula
in (6.32) and show that
Am ¼ Pm  ð1 þ rÞn X
m
k¼0
m
k


nmkPk;
where fPkg are given in exercise 15.
Exercises
229


