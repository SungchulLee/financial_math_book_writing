# Credit Risk Modeling

!!! info "Source"
    **The Mathematics of Financial Modeling and Investment Management** by Sergio M. Focardi and Frank J. Fabozzi, Wiley, 2004.
    These notes are used for educational purposes.

## Credit Risk Modeling and Credit Derivatives

I 
CHAPTER 22 
Credit Risk Modeling and 
Credit Default Swaps* 
n Chapter 2, we described the different forms of credit risk–default risk, 
credit spread risk, and downgrade risk. Credit derivatives are financial 
instruments that are designed to transfer the credit risk exposure of an 
underlying asset or assets between two parties. With credit derivatives, 
market participants can either acquire or reduce credit risk exposure. The 
ability to transfer credit risk and return provides a new tool for market par-
ticipants to improve performance. Using credit derivatives, banks may sell 
concentrated credit risks in their portfolios while keeping the loans of their 
customers on their books; these loans are otherwise not transferable due to 
relationship management issues or due to legal agreements. Credit deriva-
tives include credit default swaps, asset swaps, total return swaps, credit 
linked notes, credit spread options, and credit spread forwards.1 By far the 
most popular credit derivatives is the credit default swap. In this chapter we 
describe credit risk modeling and the valuation of credit default swaps. We 
begin with a discussion of the basic features of credit default swaps. 
CREDIT DEFAULT SWAPS 
In a credit default swap, the documentation will identify the reference 
entity or the reference obligation. The reference entity is the issuer of 
1 For a discussion of each of these credit derivatives, see Mark J.P. Anson, Frank J. 
Fabozzi, Moorad Choudhry, and Ren-Raw Chen, Credit Derivatives: Instruments, 
Applications, and Pricing (Hoboken, NJ: John Wiley & Sons, 2003). 
* This chapter is coauthored with Professor Ren-Raw Chen of Rutgers University. 
679 

680 
The Mathematics of Financial Modeling and Investment Management 
the debt instrument. It could be a corporation, a sovereign government, 
or a bank loan. In contrast, a reference obligation is a specific obligation 
for which protection is being sought. 
In a credit default swap, the protection buyer pays a fee, the swap 
premium, to the protection seller in return for the right to receive a pay-
ment conditional upon the default of the reference obligation or the refer-
ence entity. Collectively, the payments made by the protection buyer are 
called the premium leg; the contingent payment that might have to be 
made by the protection seller is called the protection leg. 
In the documentation of a trade, a default is defined in terms of a 
credit event and we shall use the terms “default” and “credit event” inter-
changeably throughout this book. Should a credit event occur, the protec-
tion seller must make a payment. 
Credit default swaps can be classified as follows: single-name credit 
default swaps and basket swaps. We’ll discuss the difference between 
these types of swaps next. 
Single-Name Credit Default Swaps 
The interdealer market has evolved to where single-name credit default 
swaps for corporate and sovereign reference entities are standardized. 
The parties to the trade specify at the outset when the credit default swap 
will terminate. If no credit event has occurred by the maturity of the 
credit swap, then the swap terminates at the scheduled termination date— 
a date specified by the parties in the contract. However, the termination 
date under the contract is the earlier of the scheduled termination date or 
a date upon which a credit event occurs and notice is provided. Therefore, 
notice of a credit event terminates a credit default swap. 
The termination value for a credit default swap is calculated at the 
time of the credit event, and the exact procedure that is followed to calcu-
late the termination value will depend on the settlement terms specified in 
the contract. This will be either cash settlement or physical settlement. 
A credit default swap contract may specify a predetermined payout 
value on occurrence of a credit event. This may be the nominal value of 
the swap contract. Alternatively, the termination value can be calculated 
as the difference between the nominal value of the reference obligation 
and its market value at the time of the credit event. This arrangement is 
more common with cash-settled contracts. 
With physical settlement, on occurrence of a credit event the buyer 
delivers the reference obligation to the seller, in return for which the seller 
pays the face value of the delivered asset to the buyer. The contract may 
specify a number of alternative issues of the reference entity that the 
buyer can deliver to the seller. These are known as deliverable obligations. 

681 
Credit Risk Modeling and Credit Default Swaps 
This may apply when a credit default swap has been entered into on a ref-
erence entity rather than a specific obligation issued by that entity (i.e., 
when there is a reference entity rather than a reference obligation). 
Where more than one deliverable obligation is specified, the protection 
buyer will invariably deliver the one that is the cheapest on the list of eligi-
ble deliverable obligations. This gives rise to the concept of the cheapest-
to-deliver. In practice, the protection buyer will deliver the cheapest-to-
deliver bond from the deliverable basket. This delivery option has debat-
able value in theory, but significant value in practice. 
The standard contract for a single-name credit default swap in the 
interdealer market calls for a quarterly payment of the swap premium. 
Typically, the swap premium is paid in arrears. The quarterly payment is 
determined using one of the day count conventions in the bond market. 
A day count convention indicates the number of days in the month and 
the number of days in a year that will be used to determine how to pro-
rate the swap premium to a quarter. The day count convention used for 
credit default swaps is actual/360. A day convention of actual/360 
means that to determine the payment in a quarter, the actual number of 
days in the quarter are used and 360 days are assumed for the year. 
Basket Default Swaps 
In a basket default swap, there is more than one reference entity. Typically, 
in a basket default swap, there are three to five reference entities. There are 
different types of basket default swap. They are classified as follows:
 ■ Nth to default swaps
 ■ Subordinate basket default swaps
 ■ Senior basket default swaps 
Below we describe each type. 
Nth to Default Swaps 
In an Nth-to-default swap, the protection seller makes a payment to the 
protection buyer only after there has been a default for the Nth refer-
ence entity and no payment for default of the first (N – 1) reference enti-
ties. Once there is a payout for the Nth reference entity, the credit 
default swap terminates. That is, if the other reference entities that have 
not defaulted subsequently do default, the protection seller does not 
make any payout. 
For example, suppose that there are five reference entities. In a first-
to-default basket swap a payout is triggered after there is a default for 
only one of the reference entities. There are no other payouts made by the 

682 
The Mathematics of Financial Modeling and Investment Management 
protection seller even if the other four reference entities subsequently have 
a credit event. If a payout is triggered only after there is a second default 
from among the reference entities, the swap is referred to as a second-to-
default basket swap. So, if there is only one reference entity for which 
there is a default over the tenor of the swap, the protection seller does not 
make any payment. If there is a default for a second reference entity while 
the swap is in effect, there is a payout by the protection seller and the 
swap terminates. The protection seller does not make any payment for a 
default that may occur for the three remaining reference entities. 
Subordinate and Senior Basket Credit Default Swaps 
In a subordinate basket default swap there is (1) a maximum payout for 
each defaulted reference entity and (2) a maximum aggregate payout 
over the tenor of the swap for the basket of reference entities. For exam-
ple, assume there are five reference entities and that (1) the maximum 
payout is $10 million for a reference entity and (2) the maximum aggre-
gate payout is $10 million. Also assume that defaults result in the fol-
lowing losses over the tenor of the swap: 
Loss result from default of first reference entity 
=
 $6 million 
Loss result from default of second reference entity = $10 million 
Loss result from default of third reference entity 
= $16 million 
Loss result from default of fourth reference entity = $12 million 
Loss result from default of fifth reference entity 
= $15 million 
When there is a default for the first reference entity, there is a $6 
million payout. The remaining amount that can be paid out on any sub-
sequent defaults for the other four reference entities is $4 million. When 
there is a default for the second reference entity of $10 million, only $4 
million will be paid out. At that point, the swap terminates. 
In a senior basket default swap there is a maximum payout for each 
reference entity but the payout is not triggered until after a specified 
threshold is reached. To illustrate, again assume there are five reference 
entities and the maximum payout for an individual reference entity is 
$10 million. Also assume that there is no payout until the first $40 mil-
lion of default losses (the threshold). Using the hypothetical losses 
above, the payout by the protection seller would be as follows. The 
losses for the first three defaults is $32 million. However, because the 
maximum loss for a reference entity, only $10 million of the $16 million 
is applied to the $40 million threshold. Consequently, after the third 
default, $26 million ($6 million + $10 million + $10 million) is applied 

683 
Credit Risk Modeling and Credit Default Swaps 
toward the threshold. When the fourth reference entity defaults, only 
$10 million is applied to the $40 million threshold. At this point, $36 
million is applied to the $40 million threshold. When the fifth reference 
entity defaults in our illustration, only $10 million is relevant since the 
maximum payout for a reference entity is $10 million. The first $4 mil-
lion of the $10 million is applied to cover the threshold. Thus, there is a 
$6 million payout by the protection seller. 
LEGAL DOCUMENTATION 
Credit derivatives are privately negotiated agreements traded over the 
counter. The International Swaps and Derivatives Association (ISDA) 
has recognized the need to provide a common format for credit deriva-
tive documentation. In addition to the definitions of credit events, ISDA 
developed the ISDA Master Agreement. This is the authoritative con-
tract used by industry participants because it established international 
standards governing privately negotiated derivative trades (all deriva-
tives, not just credit derivatives). 
The most important section of the documentation for a credit 
default swap is what the parties to the contract agree constitutes a credit 
event that will trigger a credit default payment. Definitions for credit 
events are provided by the ISDA. First published in 1999, there have 
been periodic supplements and revisions of these definitions 
The 1999 ISDA Credit Derivatives Definitions (referred to as the 
“1999 Definitions”) provides a list of eight possible credit events: (1) 
bankruptcy; (2) credit event upon merger; (3) cross acceleration; (4) 
cross default; (5) downgrade; (6) failure to pay; (7) repudiation; and (8) 
restructuring. These eight events attempt to capture every type of situa-
tion that could cause the credit quality of the reference entity to deterio-
rate, or cause the value of the reference obligation to decline. 
The parties to a credit default swap may include all of these events, 
or select only those that they believe are most relevant. There has been 
standardization of the credit events that are used in credit default swaps 
in the United States and Europe. Nevertheless, this does not preclude a 
credit protection buyer from including broader credit protection. 
CREDIT RISK MODELING: STRUCTURAL MODELS 
To value credit derivatives it is necessary to be able to model credit risk. 
Models for credit risks have long existed in the insurance and corporate 

684 
The Mathematics of Financial Modeling and Investment Management 
finance literature. Those models concentrate on default rates, credit rat-
ings, and credit risk premiums. These traditional models focus on diver-
sification and assume that default risks are idiosyncratic and hence can 
be diversified away in large portfolios. Models of this kind are along the 
line of portfolio theory that employs the capital asset pricing model 
(CAPM). In the CAPM, only the systematic risk, or market risk, matters. 
For single isolated credits, the models calculate risk premiums as 
mark-ups onto the risk-free rate. Since the default risk is not diversified 
away, a similar model to the CAPM called the security market line 
(described in Chapter 17) is used to compute the correct markup for 
bearing the default risk. The Sharpe ratio is commonly used to measure 
how credit risks are priced.2 
Modern credit derivative models can be partitioned into two groups 
known as structural models and reduced form models. Structural mod-
els were pioneered by Black and Scholes3 and Merton.4 The basic idea, 
common to all structural-type models, is that a company defaults on its 
debt if the value of the assets of the company falls below a certain 
default point. For this reason, these models are also known as firm-
value models. In these models it has been demonstrated that default can 
be modeled as an option and, as a result, researchers were able to apply 
the same principles used for option pricing to the valuation of risky cor-
porate securities. The application of option pricing theory avoids the 
use of risk premium and tries to use other marketable securities to price 
the option. The use of the option pricing theory set forth by Black-
Scholes-Merton (BSM) hence provides a significant improvement over 
traditional methods for valuing default risky bonds. It also offers not 
only much more accurate prices but provides information about how to 
hedge out the default risk which was not obtainable from traditional 
methods. Subsequent to the work of BSM, there have been many exten-
sions and these extensions are described in this chapter. 
The second group of credit models, known as reduced form models, 
are more recent. These models, most notably the Jarrow-Turnbull5 and 
2 Robert Merton, “Option Pricing When Underlying Stock Returns Are Discontinu-
ous,” Journal of Financial Economics 3 (1976), pp. 125–144. 
3 Fischer Black and Myron Scholes, “The Pricing of Options and Corporate Liabili-
ties,” Journal of Political Economy 81, no. 3 (1973), pp. 637–654. 
4 Robert Merton, “Theory of Rational Option Pricing,” Bell Journal of Economics 
(Spring 1973), pp. 141–183, and Robert Merton, “On the Pricing of Corporate 
Debt: The Risk Structure of Interest Rates,” Journal of Finance 29, no. 2 (1974), pp. 
449–470. 
5 Robert Jarrow and Stuart Turnbull, “Pricing Derivatives on Financial Securities 
Subject to Default Risk,” Journal of Finance 50, no. 1 (1995), pp. 53–86. 

685 
Credit Risk Modeling and Credit Default Swaps 
Duffie-Singleton6 models, do not look inside the firm. Instead, they 
model directly the likelihood of default or downgrade. Not only is the 
current probability of default modeled, some researchers attempt to 
model a “forward curve” of default probabilities which can be used to 
price instruments of varying maturities. Modeling a probability has the 
effect of making default a surprise—the default event is a random event 
which can suddenly occur at any time. All we know is its probability. 
There is no standard model for credit. Part of the reason why this is 
so is that each of the models has its own set of advantages and disad-
vantages, making the choice of which to use depend heavily on what the 
model is to be used for. 
The Black-Scholes-Merton Model 
The earliest credit model that employed the option pricing theory can be 
credited to BSM. Black-Scholes, explicitly articulated that corporate lia-
bilities can be viewed as a covered call: own the asset but short a call 
option. In the simplest setting, where the company has only one zero-
coupon debt, at the maturity of the debt the debt holder either gets paid 
the face value of the debt—in such a case, the ownership of the com-
pany is transferred to the equity holder—or takes control of the com-
pany—in such a case, the equity holder receives nothing. The debt 
holder of the company therefore is subject to default risk for he or she 
may not be able to receive the face value of his or her investment. BSM 
effectively turned a risky debt evaluation into a covered call evaluation 
whereby the option pricing formulas can readily apply. 
In BSM, the company balance sheet consists of issued equity with a 
market value at time t equal to E(t). On the liability side is debt with a 
face value of K issued in the form of a zero-coupon bond that matures 
at time T. The market value of this debt at time t is denoted by D(t,T). 
The value of the assets of the firm at time t is given by A(t). 
At time T (the maturity of the debt), the market value of the issued 
equity of the company is the amount remaining after the debts have 
been paid out of the firm’s assets; that is, 
(
) = max{A T
E T
(
) – K, 0} 
This payoff is identical to that of a call option on the value of the firm’s 
assets struck at the face value of the debt. The payoff is graphed as a 
function of the asset value in Exhibit 22.1. The holders of the risky cor-
6 Darrell Duffie and Kenneth Singleton, “Modeling the Term Structure of Default-
able Bonds,” working paper, Stanford University, 1997. 

686 
The Mathematics of Financial Modeling and Investment Management 
porate debt get paid either the face value, K, under no default or take 
over the firm, A, under default. Hence the value of the debt on the 
maturity date is given by 
( , 
(
), K}
D T T  ) = min{A T
(
) – max{A T
= A T
(
) – K, 0} 
(22.1) 
= K – max{K
A T
– (
), 0} 
(22.2) 
The equations provide two interpretations. Equation (22.1) decom-
poses the risky debt into the asset and a short call. This interpretation 
was first given by Black and Scholes that equity owners essentially own 
a call option of the company. If the company performs well, then the 
equity owners should call the company; or otherwise, the equity owners 
let the debt owners own the company. Equation (22.2) decomposes the 
risky debt into a risk-free debt and a short put. This interpretation 
explains the default risk of the corporate debt. The issuer (equity own-
ers) can put the company back to the debt owner when the performance 
is bad.7 The default risk hence is the put option. These relationships are 
shown in Exhibit 22.1. Exhibits 22.1(a) and 22.1(b) explain the rela-
tionship between equity and risky debt and Exhibits 22.1(b) and 22.1(c) 
explain the relationship between risky and risk-free debts. 
Note that the value of the equity and debt when added together must 
equal the assets of the firm at all times, that is, A(t) = E(t) + D(t,T). Clearly, 
at maturity, this is true as we have 
EXHIBIT 22.1 
Payoff Diagrams at Maturity for Equity, Risky Debt, and 
Risk-Free Debt 
7 A covered call is a combination of a selling call option and owning the same face 
value of the shares which might have to be delivered should the option expire in the 
money. If the option expires in the money, a net profit equal to the strike is made. If 
the option expires worthless, then the position is worth the stock price. 

687 
Credit Risk Modeling and Credit Default Swaps 
E T
( , 
(
) – K, 0} + min{A T
(
) + D T  T  ) = max{A T
(
), K} 
= A T
(
)
 
as required. 
Since any corporate debt is a contingent claim on the firm’s future 
asset value at the time the debt matures, this is what we must model in 
order to capture the default. BSM assumed that the dynamics of the 
asset value follow a lognormal stochastic process of the form 
dA t
-------------- = rdt + σdW t
( )  
( )  
(22.3) 
A t( )  
where r is the instantaneous risk-free rate which is assumed constant, σ 
is the percentage volatility, and W(t) is the Wiener process under the 
risk neutral measure (see Chapter 15).8 This is the same process as is 
generally assumed within equity markets for the evolution of stock 
prices and has the property that the asset value of the firm can never go 
negative and that the random changes in the asset value increase pro-
portionally with the asset value itself. As it is the same assumption used 
by Black-Scholes for pricing equity options, it is possible to use the 
option pricing equations developed by BSM to price risky corporate lia-
bilities. 
The company can default only at the maturity time of the debt when 
the payment of the debt (face value) is made. At maturity, if the asset 
value lies above the face value, there is no default, else the company is in 
bankruptcy and the recovery value of the debt is the asset value of the 
firm. While we shall discuss more complex cases later, for this simple 
one-period case, the probability of default at maturity is 
K 
p = 
φ[A T
(
) = 1 – N d2
(
)]dA T
(
)
 
(22.4)
∫ 
–∞ 
where φ(⋅) represents the log normal density function, N(⋅) represents 
the cumulative normal probability, and 
8 The discussions of the risk neutral measure and the change of measure using the 
Girsanov theorem can be found in standard finance texts. See, for example, Darrell 
Duffie, Dynamic Asset Pricing (New Jersey: Princeton Press, 2000), and John Hull, 
Options, Futures, and Other Derivatives (New York: Prentice Hall, 2002). 

688 
The Mathematics of Financial Modeling and Investment Management 
( ) – lnK + (r – σ2 ⁄ 2)(T
t)
lnA t
– 
= ----------------------------------------------------------------------------------
d2 
σ T
t
– 
Equation (22.4) implies that the risk neutral probability of in the 
money N(d2) is also the survival probability. To find the current value of 
the debt, D(t,T) (maturing at time T), we need to first use the BSM 
result to find the current value of the equity. As shown above, this is 
equal to the value of a call option: 
( ) = A t
(
) – e –r T  t  )KN d
E t
( )N d
( – 
(
)
 
(22.5)
1
2
where d1 =
+ σ T
t . The current value of the debt is a covered call
–
d2 
value: 
( , 
( ) – E t
D t T  ) = A t
( )  
(22.6) 
= A t
( )N d
( – 
(
)]
( ) – [A t
(
) – e –r T  t  )KN d
1
2
( )[1 – N d
( – 
(
)
= A t
(
)] + e –r T  t  )KN d
1
2
Note that the second term in the last equation is the present value of 
probability-weighted face value of the debt. It means that if default does 
not occur (with probability N(d2)), the debt owner receives the face 
value K. Since the probability is risk neutral, the probability-weighted 
value is discounted by the risk-free rate. The first term represents the 
recovery value. The two values together make up the value of debt. 
The yield of the debt is calculated by solving D(t,T) = Ke–y(T–t) for y to 
give 
lnK – lnD t T  )
( , 
y = ---------------------------------------
(22.7)
T
t
– 
Consider the case of a company which currently has net assets 
worth $140 million and has issued $100 million in debt in the form of a 
zero-coupon bond which matures in one year. By looking at the equity 
markets, we estimate that the volatility of the asset value is 30%. The 
risk-free interest rate is at 5%. We therefore have 
A(t) 
= $140 million 
K 
= $100 million 
σ 
= 30% 

689 
Credit Risk Modeling and Credit Default Swaps 
T – t = 1 year 
r 
= 5%  
Applying equation (22.5), the equity value based upon the above 
example is, 
ln140 – ln100 + (0.05 – 0.32 ) × 1 
= ------------------------------------------------------------------------------------- = 1.4382
d2 
0.3 1 
= 1.4382 – 0.30 = 1.1382
d1 
E t( ) = 140 × N(1.1382) – e –0.05 × 100 × N(1.4382) 
= $46.48 million 
and market debt value, by equation (22.6) is 
( , 
( ) – E t
D t T  ) = A t
( ) = 140 – 46.48 = $93.52 million 
Hence, the yield of the debt is, by equation (22.7): 
ln100 – ln93.52 
y = ----------------------------------------- = 6.70% 
1 
which is higher than the 5% risk-free rate by 170 basis points. This “credit 
spread” reflects the 1-year default probability from equation (22.4): 
p = 1 – N(1.4382) = 12.75% 
and the recovery value of 
( )(1 – N d
A t
(
)) = $17.85
1
if default occurs. 
From above, we can see that, as the asset value increases, the firm is 
more likely to remain solvent, the default probability drops. When default 
is extremely unlikely, the risky debt will be surely paid off at par, the risky 
debt will become risk free, and yield the risk-free return (5% in our exam-
ple). In contrast, when default is extremely likely (default probability 
approaching 1), the debt holder is almost surely to take over the company, 
the debt value should be the same as the asset value which approaches 0. 

690 
The Mathematics of Financial Modeling and Investment Management 
Implications of BSM Model 
As we can see from this example, the BSM model captures some impor-
tant properties of risky debt; namely, the risky yield increases with the 
debt-to-asset leverage of the firm and its asset value volatility. Using the 
above equations, one can also plot the maturity dependency of the 
credit spread, defined as the difference between the risky yield and the 
risk-free rate. 
What is appealing about this model is that the shapes of the credit 
spread term structures resemble those observed in the market. The highly 
leveraged firm has a credit spread which starts high, indicating that if the 
debt were to mature in the short term, it would almost certainly default 
with almost no recovery. However as the maturity increases, the likeli-
hood of the firm asset value increasing to the point that default does not 
occur increases and the credit spread falls accordingly. For the medium 
leveraged firm, the credit spread is small at the short end—there are just 
sufficient assets to cover the debt repayment. As the maturity increases, 
there is a rapid increase in credit spread as the likelihood of the assets 
falling below the debt value rises. For the low leveraged company, the 
initial spread is close to zero and so can only increase as the maturity 
increases and more time is allowed for the asset value to drop. The gen-
eral downward trend of these spread curves at the long end is due to the 
fact that on average the asset value grows at the riskless rate and so given 
enough time, will always grow to cover the fixed debt. 
Empirical evidence in favor of these term structure shapes has been 
reported by Fons who observed similar relationships between spread term 
structure shapes and credit quality.9 Contrary evidence was reported by 
Helwege and Turner who observed that the term structure of some low-
quality firms is upward sloping rather than downward sloping.10 
Geske Compound Option Model 
If the company has a series of debts (zero coupon), then it is quite easy 
for the BSM model to characterize default at different times. The trick is 
to use the compound option model by Geske.11 A compound option is 
9 Jerome Fons, “Using Default Rates to Model the Term Structure of Credit Risk,” 
Financial Analysts Journal (September/October 1994), pp. 25–32. 
10 Jean Helwege and Christopher Turner, “The Slope of the Credit Yield Curve for 
Speculative-Grade Issuers,” Federal Reserve Bank of New York Working Paper 
no.97-25 (1997). 
11 See Geske, “The Valuation of Debt as Compound Options,” and Robert Geske 
and Herbert Johnson, “The Valuation of Corporate Liabilities as Compound Op-
tions: A Correction,” Journal of Financial and Quantitative Analysis 19, no. 2 
(1984), pp. 231–232. 

691 
Credit Risk Modeling and Credit Default Swaps 
an option on another option. The main point is that defaults are a series 
of contingent events. Later defaults are contingent upon prior no-
default. Hence, layers of contingent defaults build up a series of sequen-
tial compound options, one linking to the other. 
For example, suppose there are two zero-coupon bonds expiring in 
one year and two years, respectively. Both bonds have a $100 face 
value. The asset value is $200 today and follows the diffusion process 
given by equation (22.3). If the asset value falls below the face value in 
year 1, the company is technically under default. The company may seek 
additional capital to keep it alive or the company may simply declare 
default and let the holders of the two debts liquidate the company. In 
this case we have 
A(t) = $200 million 
r 
= 5%  
= $100 million 
T1 – t = 1 year 
K1 
= $100 million 
T2 – t = 2 years 
K2 
σ 
= 20% 
The default point of a two-year model is the key to the problem. 
The recovery further complicates the problem. For example, the com-
pany may default when it fails to pay the first debt ($100); or the com-
pany may default if its asset value falls below the market value of the 
total debt, which is the face value of the first debt ($100) and the market 
value of the second debt. This happens at a situation where the second 
debt owner can audit the asset value of the firm. Furthermore, a fixed 
recovery of these debts simplifies the problem. But oftentimes recoveries 
of debts depend on claims on the assets at different priority levels. 
Take a simple example where the company defaults when it fails to 
pay its first debt. In this case the default probability is 
ln 200 ln 
– 
100 + (5% – 0.22 ⁄ 2) × 1 
= ------------------------------------------------------------------------------------------- = 3.6157
d2 
0.2 1 
p = 1 – N(3.6157) = 0.015% 
If we further assume that the first debt has a recovery rate of 0, then the 
debt value is 
( ,
D t T1) = (1 – 0.015% )e –5% × 1 × 100 = 95.11 

692 
The Mathematics of Financial Modeling and Investment Management 
If we calculate the yield as before, we find that the spread to the risk-
free rate is 1.5 basis points. If the recovery is the asset value, then we do 
need to follow equation (22.5) and the debt value is 
ln200 – ln100 + (0.05 – 0.22) × 1 
= ------------------------------------------------------------------------------------- = 3.6157
d2 
0.2 1 
= 3.6157 + 0.2 = 3.8157
d1 
E t( ) = 200 × N(3.8157) – e –0.05 × 100 × N(3.6157) 
= 104.877 
D t T
( , 
1) = 200 – 104.8777 = 95.1223 
The small difference in the two results is because the default probability 
is really small (only 0.015%). When the default probability gets bigger, 
the debt value difference will get larger. 
The second bond is more complex to evaluate. It can be defaulted in 
t = 1 when the first debt is defaulted or t = 2 when only itself is defaulted. 
The retiring of the first debt can be viewed as the dividend of the stock. 
Under the lognormal model described above, we can write the firm 
value at the end of the two-year period as 
( , 
2) = [A t T
(r–σ2⁄2)(T1 –t)+ σW T1
A t T
( , 
1) – K1]e 
(
)
 
= A t
(r–σ2⁄2)(T2 –t)+σW T2
( )e 
(
)
 
– K1e 
(r–σ2⁄2)(T1 –t)+ σW T1
(
)
 
where K1 is the face value of the 1-year debt and 
W u
( ) = 
t d ( )du
W t
∫0 
The default probability of the second debt is the sum of the first year 
default probability and the second year default probability as follows: 
(
(
Pr[A T
< K1] + Pr[A(T
> K1 and (A T
< K2)]
1) 
1) 
2) 

693 
Credit Risk Modeling and Credit Default Swaps 
If the company survives the first period, it has to pay off the first 
debt, which clearly causes the asset price to be discontinuous. The dis-
continuity of the asset value makes the valuation of the second debt 
more difficult. Geske suggests that the if the firm issues equity to pay for 
the first debt, then the asset value should remain continuous and a 
closed-form solution can be achieved. Here, we simply show the result: 
( , 
1) = e 
–r(T1 – t)
– 
( 
( )[1 – N d+
D t T
K1N d11) + A t
( 11)] 
+
( , 
2) = A t
( 11) – M d+ , d22)]
D t T
( )[N d+ 
( 12 
–r(T2 – t)
–
– 
+ e
K2M d
, d
( 12 
22) 
–
– 
+ e 
–r(T1 – t)K1[N d12) – N d11)]
(
( 
where 
ln A 0
( )
ln 
– 
Kij + (r ± σ2 ⁄ 2)
± = -----------------------------------------------------------------------
dij 
σ Tij 
K12 is the internal solution to E(T1) = K11 which is given as the face 
value of the first debt (maturing at t = 1 year) and K22 is the face value 
of the second debt (maturing at t = 2). This formulation can be extended 
to include any number of debts, T
= T1 = 1 and T22 = 2. The
11 = T12 
correlation in the bivariate normal probability functions is the square 
root of the ratio of two maturity times. In this case, it is 
¹⁄₂ . 
Note that the total debt values add to 
( , 
1) + D t T
D t T
( , 
2) 
( 
+
– 
= A t
12 
(
( )[1 – M d+ , d22)] + e 
–r(T1 – t)K1N d12) 
–r(T2 – t)
–
– 
+ e
K2M d
, d
( 12 
22) 
– 
which implies that the one-year survival probability is 
(
) and
N d12 
–
– 
two-year is 
(
, d
 which is a bivariate normal probability func-
M d12 
22) 
tion with correlation 
T1 ⁄ T2 . The equity value, which is the residual 
value 

694 
The Mathematics of Financial Modeling and Investment Management 
( ) = A t
( , 
1) – D t T
E t
( ) – D t T
( , 
2) 
– 
= A t
( 
+ 
(
( )M d+ , d22) – e 
–r(T1 – t)K1N d12)
12 
–r(T2 – t)
–
– 
– e
K2M d
, d
( 12 
22) 
which is precisely the compound option formula derived by Geske. The 
two debt values in the example are $95.12 and $81.27, respectively. The 
equity is $23.61. 
Using the information given in our earlier example, we solve for the 
“internal strike price”—the asset price at time 1 for E(1) = K11 to be 
$195.12. In other words, if the asset price at time 1, A(1), exceeds this 
value, the company survives; otherwise the company defaults. As a 
result, we can calculate the default probability of the first year to be 
(
(
Pr(A T
K
) = 1 – N d12) = 1 – 0.6078 = 0.3922
1) < 
12 
The two-year total default probability is the one whereby the com-
pany defaults in year 1 or it survives the first year but defaults the sec-
ond year: 
–
– 
Pr[A T
K
∪A T2) K
] = 1 – M d12, d
(
( 
(
1) < 
12 
< 
22 
22) 
= 1 – 0.6077 = 0.3923 
The default probability therefore between the first year and the second 
year is only 0.0001. In other words, the Geske model indicates that the 
majority default probability is in the first year, and then the company 
can survive with almost certainty. 
In general, structural models are not easy to calibrate since informa-
tion regarding the size and priority of claimants on a company’s assets is 
not readily available. Typically companies only publish details of their 
balance sheets at most quarterly, and some companies, particularly 
those facing severe financial difficulties, do not disclose the full picture. 
Instead, practitioners tend to take equity volatility as a proxy for the 
asset value volatility.12 
Barrier Structural Models 
In addition to the Geske (compound option) model, another series of 
models have also evolved to extend the BSM model to multiple periods. 
12 For example, KMV uses 
= (A E)N d
⁄ 
(
)σ
, where 
is the volatility of eq-
σE 
1
A 
σE 
uity and 
is the volatility of the asset.
σA 

695 
Credit Risk Modeling and Credit Default Swaps 
Pioneered by Black and Cox,13 these models view default as a knockout 
(down-and-out barrier) option14 where default occurred the moment the 
firm value crossed a certain threshold. 
More recently Longstaff and Schwartz15 examined the effect of sto-
chastic interest rates as did Briys and de Varenne16 who modeled the 
default as being triggered when the forward price of the firm value hits a 
barrier. Few studies within the structural approach of credit risk valua-
tion have incorporated jumps in the firm value process, because of lack 
of analytic tractability. Zhou17 incorporates jumps into a setting used in 
Longstaff and Schwartz.18 However, this model is very computation 
intensive. 
Huang and Huang propose a jump-diffusion structural model which 
allows for analytically tractable solutions for both bond prices and 
default probabilities and is easy to implement.19 The presence of jumps 
overcomes two related limitations of the BSM approach. First, it makes 
it possible for default to be a surprise since the jump cannot be antici-
pated as the asset value process is no longer continuous. Jumps also 
make it more likely that firms with low leverage can suddenly default in 
the short term and so enable them to have wider spreads at the short 
end than previously possible.20 
13 Fischer Black and John Cox, “Valuing Corporate Securities: Some Effects of Bond 
Indenture Provisions,” Journal of Finance 31, no. 2 (1976), pp. 351–367. 
14 A barrier option is a path dependent option. For such options both the payoff of 
the option and the survival of the option to the stated expiration date depends on 
whether the price of the underlying or the underlying reference rate reaches a speci-
fied level over the life of the option. Barrier options are also called down-and-out 
barrier options. Knockout options are used to describe two types of barrier options: 
knock-out options and knock-in options. The former is an option that is terminated 
once a specified price or rate level is realized by the underlying. A knock-in option is 
an option that is activated once a specified price or rate level is realized by the un-
derlying. 
15 Francis Longstaff and Eduardo Schwartz, “A Simple Approach to Valuing Risky 
Fixed and Floating Rate Debt,” Journal of Finance 50, no. 3 (1995), pp. 789–819. 
16 Eric Briys and Francois de Varenne, “Valuing Risky Fixed Rate Debt: An Exten-
sion,” Journal of Financial and Quantitative Analysis 32, no. 2 (1997), pp. 239–248. 
17 Chunsheng Zhou, “An Analysis of Default Correlations and Multiple Defaults,” 
Review of Financial Studies (2001), pp. 555–576. 
18 Longstaff and Schwartz, “A Simple Approach to Valuing Risky Fixed and Floating 
Rate Debt.” 
19 Ming Huang and Jay Huang, “How Much of the Corporate-Treasury Yield 
Spread is Due to Credit Risk?” working paper, Stanford University (2002). 
20 For a discussion of barrier-based models, see Chapter 8 in Anson, Fabozzi, 
Choudhry, and Chen, Credit Derivatives: Instruments, Applications, and Pricing. 

696 
The Mathematics of Financial Modeling and Investment Management 
Advantages and Drawbacks of Structural Models 
Structural models have many advantages. First, they model default on 
the very reasonable assumption that it is a result of the value of the 
firm’s assets falling below the value of its debt. In the case of the BSM 
model, the outputs of the model show how the credit risk of a corporate 
debt is a function of the leverage and the asset volatility of the issuer. 
The term structure of spreads also appear realistic and empirical evi-
dence argues for and against their shape. Some of the more recent struc-
tural models have addressed many of the limitations and assumptions of 
the original BSM model. 
However structural models are difficult to calibrate and so are not 
suitable for the frequent marking to market of credit contingent securi-
ties. Structural models are also computationally burdensome. For 
instance, as we have seen, the pricing of a defaultable zero-coupon bond 
is as difficult as pricing an option. Just adding coupons transforms the 
problem into the equivalent of pricing a compound option. Pricing any 
subordinated debt requires the simultaneous valuation of all of the more 
senior debt. Consequently, structural models are not used where there is 
a need for rapid and accurate pricing of many credit-related securities. 
Instead, the main application of structural models is in the areas of 
credit risk analysis and corporate structure analysis. As explained later 
in this chapter, a structural model is more likely to be able to predict the 
credit quality of a corporate security than a reduced form model. It is 
therefore a useful tool in the analysis of counterparty risk for banks 
when establishing credit lines with companies and a useful tool in the 
risk analysis of portfolios of securities. Corporate analysts might also 
use structural models as a tool for analyzing the best way to structure 
the debt and equity of a company. 
CREDIT RISK MODELING: REDUCED FORM MODELS 
The name reduced form was first given by Darrell Duffie to differentiate 
from the structural form models of the BSM type. Reduced form models 
are mainly represented by the Jarrow-Turnbull21 and Duffie-Singleton22 
models. Both types of models are arbitrage free and employ the risk-
neutral measure to price securities. The principal difference is that 
21 Robert Jarrow and Stuart Turnbull, “Pricing Derivatives on Financial Securities 
Subject to Default Risk,” Journal of Finance (March 1995), pp. 53–86. 
22 Darrell Duffie and Kenneth Singleton, “Modeling the Term Structure of Default-
able Bonds” (1997), working paper, Stanford University. 

697 
Credit Risk Modeling and Credit Default Swaps 
default is endogenous in the BSM model while it is exogenous in the Jar-
row-Turnbull and Duffie-Singleton models. As we will see, specifying 
defaults exogenously greatly simplifies the problem because it ignores 
the constraint of defining what causes default and simply looks at the 
default event itself. The computations of debt values of different maturi-
ties are independent, unlike in the BSM model that defaults of the later-
maturity debts are contingent on defaults of earlier-maturity debts. 
The Poisson Process 
The theoretical framework for reduced form models is the Poisson pro-
cess.23 To see what it is, let us begin by defining a Poisson process that 
at time t has a value Nt. The values taken by Nt are an increasing set of 
integers 0, 1, 2, … and the probability of a jump from one integer to the 
next occurring over a small time interval dt is given by 
[ 
+
– Nt = 1] = λdt
Pr Nt
dt
 
where λ is known as the intensity parameter in the Poisson process. 
Equally, the probability of no event occurring in the same time 
interval is simply given by 
[ 
+
– Nt = 0] = 1 – λdt
Pr Nt
dt
 
For the time being we shall assume the intensity parameter to be a fixed 
constant. In later discussions and especially when pricing is covered in the 
next chapter, we will let it be a function of time or even a stochastic vari-
able (known as a Cox process24). These more complex situations are 
beyond the scope of this chapter. It will be seen shortly that the intensity 
parameter represents the annualized instantaneous forward default prob-
ability at time t. As dt is small, there is a negligible probability of two 
jumps occurring in the same time interval. 
The Poisson process can be seen as a counting process (0 or 1) for 
some as yet undefined sequence of events. In our case, the relationship 
between Poisson processes and reduced form models is that the event 
which causes the Poisson process to jump from zero to 1 can be viewed 
as being a default. 
23 A Poisson process is a point process. Point processes were briefly introduced in 
Chapter 13. 
24 David Lando, “On Cox Processes and Credit Risky Securities,” Review of Deriv-
atives Research 2 (1998), pp. 99–120. Cox processes were briefly covered in Chapter 
13 of this book. 

698 
The Mathematics of Financial Modeling and Investment Management 
Another way to look at the Poisson process is to see how long it 
takes until the first default event occurs. This is called the default time 
distribution. It can be proven that the default time distribution obeys an 
exponential distribution as follows: 
– 
>
Pr(T
t) = e –λ(T
t) 
This distribution function also characterizes the survival probability 
before time t: 
– 
( , 
>
Q t  T  ) = Pr(T
t) = e –λ(T
t) 
The Jarrow-Turnbull Model 
The Jarrow-Turnbull model is a simple model of default and recovery 
based on the Poisson default process described above.25 In their model, 
Jarrow and Turnbull assume that no matter when default occurs, the 
recovery payment is paid at maturity time T. Then the coupon bond 
value can be written as 
T
n 
B t
( , 
(
)∫–dQ t  u  ) u
d + ∑P t  Tj)cje 
–λ(Tj – t)
( ) = P t  T  )R T
( , 
( , 
t
j = 1 
n 
– 
= P t  T  )R T
( ,
( , 
(
)(1 – e –λ(T
t)) + ∑P t  Tj)cje 
–λ(Tj – t) 
j = 1 
where: 
P(t,T) = the risk-free discount factor 
cj 
= the j-th coupon 
Q(t,T) = the survival probability up to time t 
R 
= the recovery ratio 
It is seen that the conditional default probability is integrated out and dis-
appears from the final result. As a consequence, by assuming recovery 
payment to be at maturity, Jarrow and Turnbull assume away any depen-
dency between the bond price and the conditional default probability. 
It is worth noting that when the recovery rate is 0, for a zero-cou-
pon bond the value of the intensity parameter is also the bond’s forward 
25 Jarrow and Turnbull, “Pricing Derivatives on Financial Securities Subject to De-
fault Risk.” 

699 
Credit Risk Modeling and Credit Default Swaps 
yield spread. This is so because in any one-period interval in the bino-
mial model, we have 
– 
( , 
( ,
D t T  ) = P t T  )e –λ(T
t) 
= P t T  )Q t T  )
( , 
( , 
This is known as the risky discount factor, which is the present value of 
$1 if there is no recovery (i.e., the recovery ratio is zero, R = 0). 
The Jarrow-Turnbull model is usually modified when it is used in 
practice. One modification is to allow the Poisson intensity λ to be a 
function of time and the other is to allow recovery to be paid upon 
default. As a result the bond equation is modified as follows: 
T 
n 
( , 
( )(–d ( )) + ∑P t Tj)cjQ t Tj)
( ) = 
P t u  )R u
Q u
( , 
( ,
B t
∫ 
t
j = 1 
T
u λ w 
(
)dw
–∫
(
)dw
n 
–∫
Tjλ w
t
( , 
( )λ u
t 
( ,
P t u  )R u
( )e 
+ ∑P t Tj)cje
= ∫ 
t 
j = 1 
To actually implement this equation, it is usually assumed that λ fol-
lows a step function. That is between any two adjacent time points, λ is a 
constant. Furthermore, it is also, as a matter of mathematical tractabil-
ity, assumed that default can occur only at coupon times.26 As a result of 
this further assumption, the above equation can be simplified as 
j 
n 
– ∑λ(Tk) 
– ∑λ(Tk) 
(
)e 
n
n 
k = 1 
( , 
k = 1
B t
( , 
(
)λ T
( ) = ∑P t Tj)R Tj
j
+ ∑P t Tj)cje 
j = 1 
j = 1 
The major advantage of the Jarrow-Turnbull model is calibration. 
Since default probabilities and recovery are exogenously specified, one 
can use a series of risky zero-coupon bonds to calibrate out a default 
probability curve and hence a spread curve. 
Calibration has become a necessary first step in fixed-income trad-
ing recently for it allows traders to clearly see relative prices and hence 
be able to construct arbitrage trading strategies. The ability to quickly 
calibrate is the major reason why reduced form models are strongly 
favored by real-world practitioners in the credit derivatives markets. 
26 This assumption is not unreasonable because between two coupon times, if the 
company is not audited, the company should not have any reason to default. 

700 
The Mathematics of Financial Modeling and Investment Management 
The Calibration of Jarrow-Turnbull Model 
Exhibit 22.2 best represents the Jarrow-Turnbull model.27 The branches 
that lead to default will terminate the contract and incur a recovery pay-
ment. The branches that lead to survival will continue the contract which 
will then face future defaults. This is a very general framework to describe 
how default occurs and contract terminates. Various models differ in how 
the default probabilities are defined and the recovery is modeled. 
Since a debt contract pays interest under survival and pays recovery 
upon default, the expected payment is naturally the weighted average of 
the two payoffs. For the ease of exposition, we shall denote the survival 
probability from now to any future time as Q(0,t) where t is some 
future time. As a consequence, the difference between two survival 
times, Q(0,s) – Q(0,t) where s > t, by definition, is the default probabil-
ity between the two future time points t and s. 
The above binomial structure can be applied to both structural 
models and reduced form models. The default probabilities can be easily 
computed by these models. The difference resides in how they specify 
recovery assumptions. In the Geske model, the asset value at the time is 
EXHIBIT 22.2 
Tree-Based Diagram of Binomial Default Process for a 
Debt Instrument 
27 As recent articles by Ren-Raw Chen and Jinzhi Huang [“Credit Spread Bonds and 
Their Implications for Credit Spread Modeling,” Rutgers University and Penn State 
University (2001)] and Ren-Raw Chen [“Credit Risk Modeling: A General Frame-
work,” Rutgers University (2003)] show, the binomial process is also applicable to 
structural models. 

701 
Credit Risk Modeling and Credit Default Swaps 
recovered. In the Duffie-Singleton model, a fraction of the market debt 
value is recovered. And in the Jarrow-Turnbull and other barrier mod-
els, an arbitrary recovery value is assumed (it can be beta distributed).28 
From the observed bond prices, we can easily retrieve default proba-
bilities from bond prices. Suppose there are two bonds, a one-year bond 
trading at $100 with a $6 annual coupon and a two-year bond trading 
at $100 with a $7 annual coupon. Assuming a recovery of $50 per $100 
par value, the first bond price is calculated as 
,
,
p(0 1) × 50 + 106 × (1 – p(0 1))
100 = -------------------------------------------------------------------------------------
1
5%
 
+ 
The default probability is then found by solving for p(0,1): 
,
105 = 106 – 56 × p(0 1) 
p(0 1) = 1.79% 
, 
We use pt to represent the forward/conditional default probability at 
time t. Hence, p1 is the default probability of the first period. In the first 
period, the survival probability is simply 1 minus the default probability: 
,
,
Q(0 1) = 1 – p(0 1) = 1 – 1.79% = 98.21% 
and therefore 
λ = –ln 0.9821 = 1.8062% 
The second bond is priced, assuming a recovery of $20 out of $100: 
,
,
 
p(1 2) × 20 + (1 – p(1 2)) × 107 
p(0 1) × 20 + Q(0 1) × 7 + ------------------------------------------------------------------------------------- 
 
1.05 

,
, 
100 = ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
1.05 
,
,
 
p(1 2) × 20 + (1 – p(1 2)) × 107 
1.79% × 20 + 98.21% × 7 + ------------------------------------------------------------------------------------- 
 
1.05 
 
= ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
1.05 
28 For more details, see Chen, “Credit Risk Modeling: A General Framework.” 

702 
The Mathematics of Financial Modeling and Investment Management 
Solving for the second-period default probability one obtains p(1,2) = 
14.01%. 
The total survival probability till two years is surviving through the 
first year (98.21%) and the second year (1 – 14.01% = 85.99%): 
,
, 
,
Q(0 2) = Q(0 1)(1 – p(1 2)) = 98.21% × (1 – 14.01% ) = 84.45% 
λ1 + λ2 = –ln 0.8445 = 16.9011% 
λ2 = 16.9011% – λ1 = 16.9011% – 1.8062% = 15.0949% 
The total default probability is either defaulting in the first period 
(1.79%) or surviving through the first year (98.21%) and defaulting in 
the second (14.01%). 
1.79% + 98.21% × 14.01% = 15.55% 
This probability can be calculated alternatively by 1 minus the two-
period survival probability: 
1 – Q(0,2) = 1 – 84.45% = 15.55% 
It should be noted that any forward default probability is the differ-
ence of two survivals weighted by the previous survival as shown below: 
( 
Q(0, j – 1) – Q(0, j)
p j  – 1, j) = ---------------------------------------------------
(22.8) 
Q(0, j – 1) 
For example, the second period default probability is 
p(0,2) = 1 – Q(0,2)/Q(0,1) 
To express this more clearly, let us examine a two-period binomial 
tree shown in Exhibit 22.3. It should be clear how the recovery amount 
can change the default probabilities. Take the one-year bond as an 
example. If the recovery were higher, the default probability would be 
higher. This is because for a higher recovery bond to be priced at the 
same price (par in our example), the default probability would need to 
be higher to compensate for it. If the default probability remains the 
same, then the bond should be priced above par. 
So far we have not discussed any model. We simply adopt the spirit 
of the reduced form models and use the market bond prices to recover 

703 
Credit Risk Modeling and Credit Default Swaps 
EXHIBIT 22.3 
Immediate Recovery 
risk-neutral probabilities. This is very similar to the bootstrapping 
method in calibrating the yield curve. The probabilities are solved recur-
sively. 
No matter which model is used, the model has to match the default 
probabilities implied by the bond prices observed in the market. It can 
be seen in the above section that there is no closed-form solution. The 
reason is that the recovery amount is the liquidation value of the com-
pany and can change as time changes (so called “stochastic recovery”). 
Transition Matrix 
The binomial structure can be extended to multinomial to incorporate 
various credit classes. It is as easy to specify n states (different credit rat-
ings) instead of just two states (default and survival). The probabilities 
can always be given exogenously. Hence, instead of a single default for 
default (and survival), there can be a number of probabilities, each for 
the probability of moving from one credit rating to another credit rat-
ing. Based upon this idea, Jarrow, Lando, and Turnbull,29 extend the 
Jarrow-Turnbull model to incorporate the so-called migration risk. 
Migration risk is different from default risk in that a downgrade in 
credit ratings only widens the credit spread of the debt issuer and does 
not cause default. No default means no recovery to worry about. This 
way, the Jarrow-Turnbull model can be more closely related to spread 
products, whereas as a model of default it can only be useful in default 
products. One advantage of ratings transition models is the ability to 
use the data published by the credit rating agencies. 
29 Robert Jarrow, David Lando, and Stuart Turnbull, “A Markov Model for the 
Term Structure of Credit Spreads,” Review of Financial Studies 10 (1997), pp. 481– 
532. 

704 
The Mathematics of Financial Modeling and Investment Management 
For a flavor of how a rating transition model can be obtained, con-
sider a simple three-state model. At each time interval an issuer can be 
upgraded, downgraded or even jump to default. This process is shown 
in Exhibit 22.4. This time, the tree is more complex. From a “live” 
state, the issuer can be upgraded or downgraded, or even jump to 
default. The default state, on the other hand, is an absorbing barrier 
which cannot become live again. In terms of Exhibit 22.4, a movement 
from “good rating” to “middle rating” is downgrade, and vice versa. 
To best describe the situation, we can establish the following transi-
tion matrix: 
Future state 
2
1 
0 
2 p22 p21 p20 
Current state 1 p12 p11 p10 
0
0 
0 
1 
where 0 is the default state, 1 is the middle credit rating state, and 2 is 
good credit rating state. pij is the transition probability to move from 
the current state i to future state j. The sum of the probabilities of each 
current state should be 1, that is 
2 
∑ pij = 1 
j = 0 
The last row of the matrix is all 0’s except for the last column. This 
means that once the asset is in default, it cannot become live again and 
it will remain in default forever. 
EXHIBIT 22.4 
Multistate Default Process 

705 
Credit Risk Modeling and Credit Default Swaps 
To make the model mathematically tractable, Jarrow-Lando-Turn-
bull assume that the transition matrix follows a Markov chain; that is, 
the n-period transition is the above matrix raised to the n-th power. The 
main purpose to derive such a matrix is that we can calibrate it to the 
historical transition matrix published by rating agencies. Note that the 
historical transition matrix consists of real probabilities which are dif-
ferent from the risk-neutral probabilities in the tree. Hence, Jarrow-
Lando-Turnbull make a further assumption that the risk-neutral proba-
bilities are proportional to the actual ones. For a risk averse investor, 
the risk-neutral default probabilities are larger than the actual ones 
because of the risk premium. 
Since historical default probabilities are observable, we can then 
directly compute the prices of credit derivatives. For example, let the 
transition probability matrix for a 1-year period be 
Future state 
2 
1
0 
2 0.80 0.15 0.05 
Current state 1 0.15 0.70 0.15 
0
0 
0 
1 
Then, for a one-year, 0-recovery coupon bond, if the current state is 
1, it has 85% to receive the coupon and 15% to go into default in the 
next period. So the present value of the next coupon is 
0.85 × $6 
------------------------ = $4.81 
1.06 
In the second period, the bond could be upgraded with probability of 
15% or remain the same with probability of 70%. If it is at the good rat-
ing, then the probability of survival is 95% and if it is at the bad rating, the 
probability of survival is 85%. Hence, the total probability of survival is 
0.15 × 0.95 + 0.7 × 0.85 = 0.7375 = 73.75% 
Therefore, the present value of the maturity cash flow (coupon and face 
value) is 
0.7375 × 106 
---------------------------------- = $69.58 
1.062 

706 
The Mathematics of Financial Modeling and Investment Management 
The bond price today is 
$4.81 + $69.58 = $74.39 
Similar analysis can be applied to the case where the current state is 2. In 
the above example, it is quite easy to include various recovery assumptions. 
It is costly to include the ratings migration risk in the Jarrow-Turn-
bull model. It is very difficult to calibrate the model to the historical 
transition matrix. First of all, the historical probabilities computed by 
the rating agencies are actual probabilities while the probabilities that 
are used for computing prices must be risk neutral probabilities that we 
introduced in Chapter 14. The assumption by Jarrow, Lando, and Turn-
bull that there is a linear transformation does not necessarily provide a 
good fit to the data. Second, there are more variables to solve for than 
the available bonds. In other words, the calibration is an underidentifi-
cation problem. Hence, more restrictive assumptions about the proba-
bilities need to be made. In general, migration risk is still modeled by 
the traditional portfolio theory (non-option methodology). But the 
model by Jarrow, Lando, and Turnbull is a first attempt at using the 
option approach to model the rating migration risk. 
The Duffie-Singleton Model 
Obviously, the Jarrow-Turnbull assumption that recovery payment can 
occur only at maturity is too far from reality. Although it generates a 
closed-form solution for the bond price, it suffers from two major draw-
backs in reality: recovery actually occurs upon (or soon after) default 
and the recovery amount can fluctuate randomly over time.30 
Duffie and Singleton take a different approach.31 They allow the 
payment of recovery to occur at any time but the amount of recovery is 
restricted to be the proportion of the bond price at default time as if it 
did not default. That is 
( ) = δD t  T  )
R t
( , 
where R is the recovery ratio, δ is a fixed ratio, and D(t,T) represents the 
debt value if default did not occur. For this reason the Duffie-Singleton 
model is known as a fractional recovery model. The rationale behind this 
approach is that as the credit quality of a bond deteriorates, the price 
falls. At default the recovery price will be some fraction of the final price 
30 Recovery fluctuates because it depends on the liquidation value of the firm at the 
time of default. 
31 Duffie and Singleton, “Modeling the Term Structure of Defaultable Bonds.”  

707 
Credit Risk Modeling and Credit Default Swaps 
immediately prior to default. In this way we avoid the contradictory sce-
nario which can arise in the Jarrow-Turnbull model in which the recovery 
rate, being an exogenously specified percentage of the default-free payoff, 
may actually exceed the price of the bond at the moment of default. 
The debt value at time t is32 
1
( ,
[
( 
[
(
D t T  ) = -----------------{pδE D t + ∆t, T)] + (1 – p)E D t + ∆t, T)]}
1 + r t
∆ 
By recursive substitutions, we can write the current value of the 
bond as its terminal payoff if no default occurs: 
( , 
1 – p t
n
∆(1 – δ) 
(
)
D t T  ) = -----------------------------------
X T
1 + r t
∆ 
Note that the instantaneous default probability being p∆t is consis-
tent with the Poisson distribution, 
–dQ
----------- = p t
∆ 
Q 
Hence, recognizing ∆t = T/n, 
D t T  ) = ------------------------------------------X T
+ 
(
)
 
(22.9) 
exp(rT)
( , 
exp(–p(1 – δ)T) (
) = exp(–(r
s)T)X T
When r and s are not constants, we can write the Duffie-Singleton 
model as 

T 
 
D t T  ) = Et exp–∫[r u
( )]duX T
( , 
( ) + s u
(
)

 
t 
where s(u) = p (1 – δ). Not only does the Duffie-Singleton model have a
u
closed-form solution, it is possible to have a simple intuitive interpretation 
of their result. The product p(1 – δ) serves as a spread over the risk-free 
discount rate. When the default probability is small, the product is small 
32 The probability, p, can be time dependent in a more general case. 

708 
The Mathematics of Financial Modeling and Investment Management 
and the credit spread is small. When the recovery is high (i.e., 1 – δ is 
small), the product is small and the credit spread is small. 
Consider a two-year zero coupon bond. Assume that the probability 
of defaulting each year is 4%, conditional on surviving to the beginning 
of the year. If the bond defaults we assume that it loses 60% of its mar-
ket value. We also assume that risk-free interest rates evolve as shown in 
Exhibit 22.5 where an up move and a down move have an equal proba-
bility of 50%. At any node on the tree the price is the risk-free dis-
counted expectation of the payoff at the next time step. Therefore at the 
node where the risk-free rate has climbed to 7%, the value of the secu-
rity is given by 
1 
-----------[(1 – 0.04) × $100 + 0.04 × ($100 – $60)] = $91.25 
1.07 
Using the relationship 
EXHIBIT 22.5 
Valuation of a Two-Year Defaultable Zero-Coupon Bond Using 
Duffie-Singleton 

709 
Credit Risk Modeling and Credit Default Swaps 
1
1 
-------------------- = -----------[pδ + (1 – p)]
1 +
+
r
s
1 + r 
this implies an effective discounting rate of r + s = 9.63% over the time 
step from the 7% node. In this way we can proceed to value the other 
nodes and roll back to calculate an initial price for the bond equal to 
$84.79. On each node in Exhibit 22.5 is also shown the effective dis-
counting rate. Knowing these we can equally price the bond as though it 
were default free but discounted at r + s rather than at the risk-free rate. 
The Duffie-Singleton model has one very important advantage. The 
above result implies that it can be made compatible with arbitrage-free 
term structure models such as Cox-Ingersoll-Ross33 and Heath-Jarrow-
Morton.34 The difference is that now the discounting is spread adjusted. 
Just like the yield curve for the risk-free term structure, the spread curve 
is added to the risk-free yield curve and we arrive at a risky yield curve. 
The spread curve is clearly based upon the probability curve (pt for all t) 
and the recovery rate (δ). 
Although the Duffie-Singleton model seems to be superior to the 
Jarrow-Turnbull model, it is not generic enough to be applied to all 
credit derivative contracts. The problem with the Duffie-Singleton 
model is that if a contract that has no payoff at maturity such as a credit 
default swap, their model implies zero value today, which is of course 
not true. Recall that credit default swaps pay nothing if default does not 
occur. If recovery is proportional to the no-default payment, then it is 
obvious that the contract today has no value. It is quite unfortunate that 
the Duffie-Singleton model is not suitable for the most popular credit 
derivative contracts. Hence, the proportionality recovery assumption is 
not very general. 
The calibration of the Duffie-Singleton model is as easy as the Jarrow-
Turnbull model. The two calibrations are comparable. However, there 
are significant differences. Note that in the Jarrow-Turnbull model, the 
recovery assumption is separate from the default probability. But this is 
not the case in the Duffie-Singleton model—the recovery and the default 
probability together become an instantaneous spread. While we can cal-
ibrate the spreads, we cannot separate the recovery from the default 
probability. On the other hand, in the Jarrow-Turnbull model, the 
33 John Cox, Jonathan Ingersoll, and Stephen Ross, “A Theory of the Term Structure 
of Interest Rates,” Econometrica 53 (1985), pp. 385–407. 
34 David Heath, Robert Jarrow, and Andrew Morton, “Bond Pricing and the Term 
Structure of Interest Rates: A New Methodology,” Econometrica 59 (February 
1992), pp. 77–105. 

710 
The Mathematics of Financial Modeling and Investment Management 
default probability curve can be calibrated to only if a particular recov-
ery assumption is adopted. Hence the default probability is a function 
of the assumed recovery rate. 
General Observations on Reduced Form Models 
While the reduced form models lay a solid theoretical foundation, as 
they attempt to model the underlying risk-neutral probability of default 
which is not a market observable, they are not as intuitive as one might 
like. They also suffer from the constraint that default is always a sur-
prise. While this is true under some rare circumstances, Both Moody’s 
and Standard & Poor’s data show that there are very few defaults 
straight out of investment-grade quality bonds. Default is usually the 
end of a series of downgrades and spread widenings and so can be antic-
ipated to a large extent. Hence, although more and more financial insti-
tutions are starting to implement the Jarrow-Turnbull and Duffie-
Singleton models, spread-based diffusion models remain very popular. 
The Jarrow-Turnbull and Duffie-Singleton models assume that defaults 
occur unexpectedly and follow the Poisson process. This assumption 
greatly reduces the complexity since the Poisson process has very nice 
mathematical properties. In order to further simplify the model, Jarrow-
Turnbull and Duffie-Singleton respectively make other assumptions so 
that there exist closed-form solutions to the basic underlying asset. 
PRICING SINGLE-NAME CREDIT DEFAULT SWAPS 
There are two approaches to pricing default swaps—static replication 
and modeling. The former approach is based on the assumption that if 
one can replicate the cash flows of the structure which one is trying to 
price using a portfolio of tradable securities, then the price of the struc-
ture should equal the value of the replicating portfolio. This is accom-
plished through what is known as an asset swap; however, there are 
limitations of using of asset swaps for pricing.35 In situations where 
either the nature of the instrument we are trying to price cannot be rep-
licated or that we do not have access to prices for the instruments we 
would use in the replicating portfolio, it becomes necessary to use a 
modeling approach. That is the approach explained below for pricing 
credit default swaps. 
35 See Chapter 4 in Anson, Fabozzi, Choudhry, and Chen, Credit Derivatives: Instru-
ments, Applications, and Pricing. 

711 
Credit Risk Modeling and Credit Default Swaps 
Several models have been suggested for pricing single-name credit 
default swaps.36 These products (before we take into account the valua-
tion of counterparty risk) are generally regarded as the “cash product” 
that can be directly evaluated off the default probability curves. No 
parametric modeling is necessary. This is just like the coupon bond val-
uation which is model free because the zero-coupon bond yield curve is 
all that is needed to price coupon bonds. 
General Framework 
To value credit derivatives it is necessary to be able to model credit risk. 
The two most commonly used approaches to model credit risk are struc-
tural models and reduced form models. The latter do not look inside the 
firm. Instead, they model directly the likelihood of a default occurring. 
Not only is the current probability of default modeled, some researchers 
attempt to model a “forward curve” of default probabilities which can 
be used to price instruments of varying maturities. Modeling a probabil-
ity has the effect of making default a surprise—the default event is a 
random event which can suddenly occur at any time. All we know is its 
probability of occurrence. 
Reduced form models are easy to calibrate to bond prices observed 
in the marketplace. Structural-based models are used more for default 
prediction and credit risk management.37 
Both structural and reduced form models use risk-neutral pricing to 
be able to calibrate to the market. In practice, we need to determine the 
risk-neutral probabilities in order to reprice the market and price other 
instruments not currently priced. In doing so, we do not need to know 
or even care about the real-world default probabilities. 
36 See, for example, John Hull and Alan White, “Valuing Credit Default Swaps I,” 
working paper, University of Toronto (April 2000) and “Valuing Credit Default 
Swaps II: Counterparty Default Risk,” working paper, University of Toronto (April 
2000); and Dominic O’Kane, “Credit Derivatives Explained: Markets Products and 
Regulations,” Lehman Brothers, Structured Credit Research (March 2001) and “In-
troduction to Default Swaps,” Lehman Brothers, Structured Credit Research (Janu-
ary 2000). 
37 Increasingly, investors are seeking consistency between the markets that use differ-
ent modeling approaches, as the interests in seeking arbitrage opportunities across 
various markets grows. Ren-Raw Chen has demonstrated that all the reduced form 
models described above can be regarded in a non-parametric framework. This non-
parametric format makes the comparison of various models possible. Furthermore, 
as Chen contends, the non-parametric framework focuses the difference of various 
models on recovery. See Ren-Raw Chen, “Credit Risk Modeling: A General Frame-
work,” working paper, Rutgers University, 2003. 

712 
The Mathematics of Financial Modeling and Investment Management 
Since in reality, a default can occur any time, to accurately value a 
default swap, we need a consistent methodology that describes the fol-
lowing: (1) how defaults occur; (2) how recovery is paid; and (3) how 
discounting is handled. 
Survival Probability and Forward Default Probability: 
A Recap 
Earlier in this chapter we introduced two important analytical con-
structs: survival probability and forward default probability. We recap 
both below since we will need them in pricing credit default swaps. 
Assume the risk-neutral probabilities exist. Then we can identify a 
series of risk-neutral default probabilities so that the weighted average 
of default and no-default payoffs can be discounted at the risk-free rate. 
Let Q(t,T) to be the survival probability from now t till some future 
time T. Then Q(t,T) – Q(t,T + τ) is the default probability between T and 
T + τ (i.e., survive till T but default at T + τ). Assume defaults can only 
occur at discrete points in time, T1, T2, ..., T . Then the total probability
n
of default over the life of the credit default swap is the sum of all the per 
period default probabilities: 
n 
( ,
( , 
( 
(
)
∑Q t Tj) – Q t Tj + 1) = 1 – Q Tn) = 1 – Q T
j = 0 
where t = T0 < T1 < ... < T = T and T is the maturity time of the credit
n 
default swap. Note that the sum of the all the per-period default proba-
bilities should equal one minus the total survival probability. 
The survival probabilities have a useful application. A $1 “risky” 
cash flow received at time T has a risk-neutral expected value of Q(t,T) 
and a present value of P(t,T)Q(t,T) where P is the risk-free discount fac-
tor. A “risky” annuity of $1 can therefore be written as 
∑ 
n 
P t Tj)Q t Tj)
( , 
( , 
j = 1 
A “risky” bond with no recovery upon default and a maturity of n 
can thus be written as 
n 
( ) = ∑P t Tj)Q t Tj)cj + P t T )Q t T )
B t
( ,
( , 
( , 
( ,
n
n 
j = 1 

713 
Credit Risk Modeling and Credit Default Swaps 
This result is similar to the risk-free coupon bond where only risk-free 
discount factors are used. 
The “forward” default probability is a conditional default probabil-
ity for a forward interval conditional on surviving until the beginning of 
the interval. This probability can be expressed as 
( , 
( ,
Q t Tj – 1) – Q t Tj)
p Tj
(
) = ------------------------------------------------------
(22.10)
( ,
Q t Tj – 1) 
Credit Default Swap Value 
A credit default swap takes the defaulted bond as the recovery value and 
pays par upon default and zero otherwise. 
µr s
–∫
( )ds
V = E e
 
e 
1µ < T[1 – R µ
( )] 
where µ is default time. 
Hence the value of the credit default swap (V) should be the loss upon 
default weighted by the default probability: 
n 
V = ∑P t Tj)[Q t Tj – 1) – Q t Tj)][1 – R Tj
( ,
( , 
( , 
(
)] 
(22.11) 
j = 1 
where P(·) is the risk-free discount factor and R(·) is the recovery rate. 
In equation (22.2) it is implicitly assumed that the discount factor is 
independent of the survival probability. However, in reality, these two 
may be correlated—usually higher interest rates lead to more defaults 
because businesses suffer more from higher interest rates. Equation 
(22.2) has no easy solution.
From the value of the credit default swap, we can derive a spread 
(s), which is paid until default or maturity: 
V 
s = --------------------------------------------------
(22.12) 
n 
∑P t Tj)Q t Tj)
( , 
( , 
j = 1 
Exhibit 22.6 depicts the general default and recovery structure. The 
payoff upon default of a default swap can vary. In general, the owner of 

714 
The Mathematics of Financial Modeling and Investment Management 
EXHIBIT 22.6 
Payoff and Payment Structure of a Credit Default Swap 
the default swap delivers the defaulted bond and in return receives prin-
cipal. Many default swaps are cash settled and an estimated recovery is 
used. In either case, the amount of recovery is randomly dependent 
upon the value of the reference obligation at the time of default. Models 
differ in how this recovery is modeled.38 
To illustrate how to use the above formulation of credit default 
swap pricing, assume (1) two “risky” zero-coupon bonds exist with one 
and two years to maturity and (2) no recovery upon default. From equa-
tion (22.10) we know the credit spreads of these two “risky” zeros are 
approximately their default probabilities. For example, assume the one-
year zero has a spread of 100 basis points and the two-year has a spread 
of 120. The survival probabilities can be computed from equation 
(22.10). For the one-year bond whose yield spread is 100 basis points, 
the (one year) survival probability is 
1% = –ln Q(0 1)
, 
Q(0 1) = e –1% = 0.9900
, 
For the two-year zero-coupon bond whose yield spread is 120 basis 
points, the (two year) survival probability is: 
,
1.2% × 2 = –lnQ(0 2) 
,
Q(0 2) = e –1.2% × 2 = 0.9763 
38 We provide an example where the two variables are independent and the defaults 
follow a Poisson process. The simple solution exists under the continuous time as-
sumption. The analysis is provided in the appendix to Chapter 10 in Anson, Fabozzi, 
Choudhry, and Chen, Credit Derivatives: Instruments, Applications, and Pricing. 

715 
Credit Risk Modeling and Credit Default Swaps 
These survival probabilities can then be used to compute forward 
default probabilities defined in equation (22.8): 
p 1
,
,
Q(0 0) – Q(0 1) 
1 – 99.00% 
( ) = --------------------------------------------- = ------------------------------ = 1.00% 
Q(0 0) 
1
, 
and 
p 2
,
,
Q(0 1) – Q(0 2) 
99.00% – 97.63% 
( ) = --------------------------------------------- = ------------------------------------------------ = 1.39% 
Q(0 1) 
99.00% 
, 
Since we assume a 5% flat risk-free rate for two years, the risk-free dis-
count factors are 
P(0 1) = e –5% 
, 
,
P(0 2) = e –5% × 2 
for one and two years, respectively. Assuming a 20% recovery ratio, we 
can then calculate, using equation (22.11), what the total protection 
value (V) of the default swap contract is providing 
–5% × 2
V = e –5%(1 – 0.99)(1 – 0.2) + e 
(0.99 – 0.9763)(1 – 0.2) 
= 0.00761 + 0.010134 
= 0.017744 = 177.44 basis points 
As mentioned, the default swap premium is not paid in full at the 
inception of the swap but paid in a form of spread until either default or 
maturity, whichever is earlier. From equation (22.12), we can compute 
the spread of the default swap as follows: 
0.017744 
s = ---------------------------------------------------------------------------------------------------------------------
0.99 × exp(–0.05) + 0.9763 × exp(–0.05 × 2) 
0.017744 
= ------------------------ = 0.009724 
1.824838 
which is 9.724 basis points for each period, provided that default does not 
occur. This is a payment in arrears. That is, if default occurs in the first 
period, no payment is necessary. If default occurs in the second period, 
there is one payment; if default never occurs, there are two payments. 

716 
The Mathematics of Financial Modeling and Investment Management 
No Need For Stochastic Hazard Rate or Interest Rate 
The analysis above demonstrates that to price a default swap, we only need 
a recovery rate, the risk-free yield curve (the P-curve), and the survival 
probability curve (the Q-curve). This implies that regardless of which model 
is used to justify the P-curve or the Q-curve, default swaps should be priced 
exactly the same. This further implies that there is no need to be concerned 
if the risk-free rate and the hazard rate are stochastic or not, because they 
do not enter into the valuation of the default swap. In other words, random 
interest rates and hazard rates are “calibrated out” of the valuation.39 
Delivery Option in Default Swaps 
As explained earlier in this chapter, a credit default swap trade can spec-
ify a reference entity or a reference obligation. In the former case, the 
protection buyer has the option to deliver one of severable deliverable 
obligations of the reference entity. This effectively creates a similar situ-
ation to the well-known quality option for Treasury note and bond 
futures contracts where more than one bond can be delivered. In this 
case, the value of the credit default swap is 
n 
( , 
( ,
j – 1) – Q t  Tj )][1 – minR Tj
V = ∑P
 
t
 
Tj )[Q t  T
( , 
(
)] 
j = 1 
The difference between the above equation and equation (22.11) is the 
recovery. The delivery of the lowest recovery bond, min{R(Tj)}, for all j 
bonds is what the payoff is. 
It is natural that the worst quality bond should be delivered upon 
default. For a credit default swap, the one with the lowest recovery 
should be delivered. Unlike Treasury bond and note futures where the 
cheapest-to-deliver issue can change due to interest rate changes, recovery 
is mostly determined contractually and usually the lowest priority bond 
will remain the lowest priority for the life of the contract. The only uncer-
tainty in determining the cheapest-to-deliver issue is the future introduc-
tion of new bonds. This is largely related to the capital structure of the 
company and beyond the scope of risk-neutral pricing. The model that 
can incorporate capital structure issues (i.e., using debt to optimize capi-
tal structure) needs to be a structural model with wealth maximization.40 
39 For the stochastic hazard rate model, see Daniel Lando, “On Cox Processes and 
Credit Risky Securities,” Review of Derivatives Research (1998), pp. 99–120. 
40 Issues about optimal capital structure and default risk are discussed in Hayne E. Le-
land and Klaus Bjerre Toft, “Optimal Capital Structure, Endogenous Bankruptcy, and 
the Term Structure of Credit Spreads,” Journal of Finance (July 1996), pp. 987–1019. 

717 
Credit Risk Modeling and Credit Default Swaps 
Default Swaps with Counterparty Risk 
Counterparty risk is a major concern for credit default swap investors 
because major participants in the market are financial firms, which are 
themselves subject to default risk.41 Most bank/dealer counterparties 
are single A or at most AA rated. If the reference entity name is a AAA 
rated company, then the default probability of the bank/dealer is so 
much higher than the reference entity that the bank/dealer may default 
well before the reference entity. In this case, the protection buyer in a 
credit default swap is more concerned with the counterparty default risk 
than the default risk of the reference entity. In this section, we shall 
extend the previous risk-neutral methodology to account for counter-
party risk, with the assumption that the default of the reference entity 
and the default of the counterparty are uncorrelated. 
We label the survival probability of the reference entity Q1(t,T) and 
that of the counterparty Q2(t,T). The default probabilities of the reference 
entity and counterparty in the jth period in the future are Q1(t,T ) –
j
Q1(t,T +1) and Q2(t,T ) – Q2(t,T +1), respectively. The default of either one is 
j
j
j
,
, 
,
j + 1)Q2(t T
Q1(t Tj)Q2(t Tj) – Q1(t T
,
j + 1) 
The above equation represents a situation that both the reference 
entity and counterparty jointly survive till Tj but not Tj+1. Hence one of 
them must have defaulted in the period (Tj,Tj+1). Subtracting the coun-
terparty default probability from the probability of either default gives 
rise to the probability of the case that only the reference entity (but not 
the counterparty) defaults. Hence the total probability of only the refer-
ence entity defaulting is 
n 
,
,
j 
,
j + 1)Q2(t T
,
,
j + 1)]
∑[Q1(t Tj)Q2(t T ) – Q1(t T
,
j + 1)] – [Q2(t Tj) – Q2(t T
j = 0 
When recovery and discounting are included, we have the credit 
default swap value as 
n 
( , 
(
)][Q1(t Tj)Q2(t Tj) – Q1(t T
,
j + 1)
V = ∑P t Tj)[1 – R Tj
,
, 
,
j + 1)Q2(t T
j = 0 
,
j 
,
j + 1)}]
–{Q2(t T ) – Q2(t T
41 See also Hull and White, “Valuing Credit Default Swaps II: Counterparty Default 
Risk.” 

718 
The Mathematics of Financial Modeling and Investment Management 
The default swap valued under the counterparty risk requires two 
default curves, one for the reference entity and one for the counterparty. 
This default swap should be cheaper than the default swap with only 
default risk for the reference entity. The difference is the value of the 
default swap that protects the joint default. An investor who buys such 
a default swap owns a default swap on the reference entity and has 
implicitly sold a default swap of joint default back to the counterparty. 
When the defaults of the reference entity and the counterparty are 
correlated, the solution becomes much more complex. When the corre-
lation is high, it is more likely that the counterparty should default 
before the reference entity, and the credit default swap should have very 
little value. On the other hand, when the correlation is low (negative), 
the situation where the reference entity defaults almost guarantees the 
survival of the counterparty. Consequently, in such instances the coun-
terparty risk is not a concern. 
VALUING BASKET DEFAULT SWAPS 
In the previous section we presented a model for valuing single-name 
credit default swaps. Unlike a single-name credit default swap, which 
provides protection for one bond, a basket default swap provides pro-
tection against a basket of bonds. As with single-name credit default 
swaps, the protection buyer of a basket default swap makes a stream of 
spread payments until either maturity or default. In the event of default, 
the protection buyer receives a single lump-sum payment. 
Default baskets have become popular because purchasing individual 
basket default swaps for a collection of bonds can be very expensive, 
especially considering how unlikely it is that all the bonds in a given 
basket will default simultaneously. Buying a basket default swap, 
instead, provides a much cheaper solution. The most popular default 
basket swap contract is the first-to-default basket. In this contract, the 
seller pays (the default event occurs) when the first default is observed 
among the bonds in the basket. 
In this section, we describe how to extend the model to basket 
default swaps. The key in the extension is estimating default correla-
tions. We begin with the valuation model and then discuss how to 
model default correlations. 
The Pricing Model 
The number of issuers (or issues) contained in a default basket typically 
varies (three to five). The payoff of a default basket contract can be a 

719 
Credit Risk Modeling and Credit Default Swaps 
fixed amount or loss based. The first-to-default basket pays principal 
minus the recovery value of the first defaulted bond in the basket. 
Hence, for pricing the default basket, we can generalize the default 
swap valuation as follows: 
–∫
min(uk)
( ) s
d 
r s
 
V = Ee
t 
1min uk
(
)]Nk 
(22.13)
(
) < T[1 – Rk uk

 
where 1 is the indicator function, uk is the default time of the k-th bond, Rk 
is recovery rate of the k-th bond, and Nk is the notional of the k-th bond. 
The basket pays when it experiences the first default, that is, min (uk).42 
Equation (22.13) has no easy solution when the default events (or 
default times, uk) are correlated. For the sake of exposition, we assume 
two default processes and label the survival probabilities of the two credit 
names as Q1(t,T) and Q2(t,T). In the case of independence, the default 
probabilities at some future time t are –dQ1(t,T) and –dQ2(t,T) respec-
tively. The default probability of either bond defaulting at time t is 
[
, 
,
–d Q1(t T)Q2(t T)] 
(22.14) 
The above equation represents a situation wherein both credit names 
jointly survive until t, but not until the next instant of time; hence one 
of the bonds must have defaulted instantaneously at time t. Subtracting 
the default probability of the first credit name from the probability of 
42 In either the default swap or default basket market, the premium is usually paid in 
a form of spreads. The spread is paid until either the default or maturity, whichever 
is earlier. From the total value of the default swap, we can convert it to a spread that 
is paid until default or maturity: 
V 
s = ------------------------------------------------------
n 
( , 
,
∑P t  Tj)Q*(t Tj) 
j = 1 
where Q*(t,Tj) is the survival probability of no default of all bonds in the basket. 
Under independence assumption, 
N 
,
,
Q*(t Tj) = ∏Qk(t Tj) 
k = 1 
where N is the number of bonds in the basket. When bonds are correlated, we need 
to use materials in the following section to compute Q*. 

720 
The Mathematics of Financial Modeling and Investment Management 
either defaulting gives rise to the probability that only the second name 
(but not the first) defaults: 
T 
[
– d Q1(0, t)Q2(0, t)] + dQ1(0, t)
∫ 
0 
= [1 – Q1(0, T)Q2(0, T)] – [1 – Q1(0, T)] 
= Q1(0, T)[1 – Q2(0, T)] 
(22.15) 
This probability is equal to the probability of survival of the first name 
and default of the second name; thus, it is with this probability that the 
payoff to the second name is paid. By the same token, the default prob-
ability of the first name is 1 – Q1(0,T), and it is with this probability 
that the payoff regarding to the first name is paid. 
In a basket model specified in equation (22.13), the final formula for 
the price of an N bond basket under independence is 
T
N 
k
k – 1 
V = ∫∑P(0, t) – d ∏Ql(0, t) + d ∏Ql(0, t) [1 – Rk t 
( )] 
(22.16) 
0 k = 1 
l = 1 
l = 0 
where Q0(t) = 1 and hence dQ0(t) = 0. Equation (22.16) assumes that 
the last bond (i.e., bond N) has the highest priority in compensation, 
that is, if the last bond jointly defaults with any other bond, the payoff 
is determined by the last bond. The second to last bond has the next 
highest priority in a sense that if it jointly defaults with any other bond 
but the last, the payoff is determined by the second to last bond. This 
priority prevails recursively to the first bond in the basket. 
Investment banks that sell or underwrite default baskets are them-
selves subject to default risks. If a basket’s reference entities have a 
higher credit quality than their underwriting investment bank, then it is 
possible that the bank may default before any of the issuers. In this case, 
the buyer of the default basket is subject to not only the default risk of 
the issuers of the bonds in the basket, but also to that of the bank as 
well—that is, the counterparty risk. If the counterparty defaults before 
any of the issuers in the basket do, the buyer suffers a total loss of the 
whole protection (and the spreads that had been paid up to that point in 
time). We modify equation (22.16) to incorporate the counterparty risk 
by adding a new asset with zero payoff to the equation: 
TN + 1 
k
k – 1 
V = ∫∑P(0, t) – d ∏Qj(0, t) + d ∏Ql(0, t) [1 – Rk t 
( )] 
(22.17) 
0 k = 1 
l = 1 
l = 0 

721 
Credit Risk Modeling and Credit Default Swaps 
where the first asset represents the counterparty whose payoff is zero, 
that is, 
( ) = 0 for all t 
(22.18)
1 – R1 t
Note that the counterparty payoff has the lowest priority because the 
buyer will be paid if the counterparty jointly defaults with any issuer. 
The default swap is a special case of the default basket with N = 1 
discussed earlier. However, with a default swap, the counterparty risk is 
more pronounced than that with a basket deal. With only one issuer, 
equation (22.17) can be simplified to 
T 
( )]
V = ∫P(0, t){–dQ1(0, t)[1 – R1 t 
0 
( )]}
+ [– dQ1(0, t)Q2(0, t) + dQ1(0, t)][1 – R2 t
T 
P(0, t){[– dQ1(0, t)Q2(0, t) + dQ1(0, t)][1 – R2 t( )]} (22.19)
= ∫ 
0 
Equation (22.19) implies that the investor who buys a default swap on 
the reference entity effectively sells a default swap of joint default back 
to the counterparty. 
When the defaults of the issuers (and the counterparty) are corre-
lated, the solution to equation (22.16) becomes very complex. When the 
correlations are high, issuers in the basket tend to default together. In 
this case, the riskiest bond will dominate the default of the basket. 
Hence, the basket default probability will approach the default proba-
bility of the riskiest bond. On the other hand, when the correlations are 
low, individual bonds in the basket may default in different situations. 
No bond will dominate the default in this case. Hence, the basket 
default probability will be closer to the sum of individual default proba-
bilities. 
To see more clearly how correlation can impact the basket value, 
think of a basket that contains only two bonds of different issuers. In 
the extreme case where the default correlation is 1, the two bonds in the 
basket should default together. In this case, the basket should behave 
like a single bond. On the other extreme, if the correlation is –1 (the 
bonds are perfect compliments of one another), default of one bond 
implies the survival of the other and vice versa. In this case, the basket 
should reach the maximum default probability: 100%. 

722 
The Mathematics of Financial Modeling and Investment Management 
How to Model Correlated Default Processes43 
Default correlation is not an easy concept to define or measure. Put in 
simple terms, it is a measurement of the degree to which default of one 
asset makes more or less likely the default of another asset. One can 
think of default correlation as being jointly due to (1) a macroeconomic 
effect which tends to tie all industries into the common economic cycle; 
(2) a sector specific effect, and (3) a company specific effect. 
The first contribution implies that default correlation should in gen-
eral be positive even between companies in different sectors. Within the 
same sector we would expect companies to have an even higher default 
correlation since they have more in common. For example, the severe 
fall in oil prices during the 1980s resulted in the default of numerous 
oil-producing industries. On the other hand, the fall in the price of oil 
would have made the default of oil-using industries less likely as their 
energy costs fell, thereby reducing their likelihood of default and reduc-
ing the default correlation. However the sheer lack of default data 
means that such assumptions are difficult to verify with any degree of 
certainty. 
It is simple enough to define pure default correlation. Basically, this 
number must correspond to the likelihood that should one asset default 
within a certain time period, how more or less likely is another asset to 
also default. In the case of default correlation, it is important to specify 
the horizon which is being considered. 
The pairwise default correlation between two assets A and B is a 
measure of how more or less likely two assets are to default than if they 
were independent. 
Specifying Directly Joint Default Distribution 
Let two firms, A and B, follow the following joint Bernoulli distribution 
(letting superscripts denote complement sets): 
Firm A 
0 
1 
Firm B 
0 
1 
p AC ∩BC
( 
) 
p AC 
B
∩
( 
) 
1 p A
(
)
– 
p A  ∩BC
( 
) 
p A  B
∩
( 
) 
p A
(
)
 
1 
1 p B
(
)
– 
p B
(
)
 
43 This discussion draws from Ren-Raw Chen and Ben J. Sopranzetti, “The Valua-
tion of Default-Triggered Credit Derivatives,” Journal of Financial and Quantitative 
Analysis (June 2003). 

723 
Credit Risk Modeling and Credit Default Swaps 
where 
p AC ∩B) = p B
(
( 
(
) – p A ∩B) 
p A ∩BC) = p A
(
( 
(
) – p A ∩B) 
p AC
(
∩BC) = 1 – p B
(
(
) – p A ∩BC) 
The default correlation is 
cov 1A, 1B) 
p B  
(
( 
(
) – p A
(
)
A)p A
(
)p B
-------------------------------------------- = -----------------------------------------------------------------------------------
var 1A)var 1B) 
p A
(
)p B
(
))
( 
( 
(
)(1 – p A
(
))(1 – p B
For example, suppose that A is a large automobile manufacturer 
and B is a small auto part supplier. Assume their joint default distribu-
tion is given as follows: 
Firm A 
0
1 
Firm B 
0 
80%
 0%
 80% 
1 
10% 
10%
 20% 
90% 
10% 
100% 
In this example where A defaults should bankrupt B but not vice 
versa, B contains A and 
( 
(
)
p A ∩B) = p A
The dependency of the part supplier on the auto manufacturer is 
p A ∩B) 
p A
( 
(
)
A) = ----------------------- = ------------ = 100% 
p B
( 
(
)
 
p A
p A
(
)
 
and the dependency of the auto manufacturer on the part supplier is 
p A ∩B) 
p A
( 
(
)
B) = ----------------------- = ------------ = 50% 
p A
( 
(
)
 
p B
p B
(
)
 

-----------------------------------------------------------------------------------
724 
The Mathematics of Financial Modeling and Investment Management 
The default correlation is 
p B
( 
A)p A
(
)p B
(
) – p A
(
)
 
p A
(
)p B
(
))
(
)(1 – p A
(
))(1 – p B
10% – 10% × 20% 
= --------------------------------------------------------------------------
10% × 90% × 20% × 80% 
0.08 
2 
= --------------------- = --
0.0144 
3 
This examples demonstrates that perfect dependency does not imply 
perfect correlation. To reach perfect correlation, p(A) = p(B). Similarly, 
perfectly negative dependency does not necessarily mean perfect nega-
tive correlation. To see that, consider the following example: 
Firm A 
0
1 
Firm B 
0 
70% 
10%
 80% 
1 
20%
 0%
 20% 
90% 
10% 
100% 
It is clear that given A defaults, B definitely survives: p BC
( 
A) = 1 , 
and p B
( 
A) = 0 . But the default correlation is only –0.25. To reach 
perfect negative correlation of –100%, p(A) + p(B) = 1. 
The reason that perfect dependency does not result in perfect corre-
lation is because correlation alone is not enough to identify a unique 
joint distribution. Only a normal distribution family can have a uniquely 
identified joint distribution when a correlation matrix is identified. This 
is not true for other distribution families.44 
Having now defined default correlation, one can begin to show how 
it relates to the pricing of credit default baskets. 
We represent the outcomes of the two defaultable assets A and B 
using a Venn diagram as shown in Exhibit 22.7. The left circle corre-
sponds to all scenarios in which asset A defaults before time T. Its area 
is therefore equal to pA, the probability of default of asset A. Similarly, 
the area within the circle labeled B corresponds to the probability of 
default of asset B and equals pB. The area of the shaded overlap corre-
44 For an extension of the above two-company analysis to multiple companies, see 
Chen and Sopranzetti, “The Valuation of Default-Triggered Credit Derivatives.” 

-------------------------------
725 
Credit Risk Modeling and Credit Default Swaps 
EXHIBIT 22.7 
Venn Diagram Representation of Correlated Default for Two Assets 
sponds to all scenarios in which both assets default before time T. Its 
area is the probability of joint default, pAB. 
The probability of either asset defaulting is 
Ω= pA + pB – pAB 
In the zero correlation limit, when the assets are independent, the prob-
ability of both assets defaulting is given by pAB = pA pB. Substituting 
this into the above formula for the default correlation shows when the 
assets are independent, ρD(T) = 0 as expected (see Exhibit 22.8). 
In the limit of high default correlation, the default of the stronger 
asset always results in the default of the weaker asset. In the limit the 
joint default probability is given by pAB = min[pA,pB]. This is shown in 
Exhibit 22.9 in the case where pA > pB. In this case we have a maximum 
default correlation of 
ρ 
pB 1 pA 
–
( 
) 
pA 1 pB 
–
( 
) 
-
= 
Once again, the price of a first-to-default basket is the area enclosed by 
the circles. In this case one circle encloses the other and the first-to-
default basket price becomes the larger of the two probabilities: 
=
= pA + pB – pAB = max[pA, pB]
Ωρ
ρ
 

726 
The Mathematics of Financial Modeling and Investment Management 
EXHIBIT 22.8 
Independent Assets 
Outcome 
In Venn Diagram 
Probability 
Both asset A and asset B 
Anywhere in overlap of 
pAB 
default 
both circles
Asset B defaults and asset A 
Anywhere in B but not in 
pB – pAB 
does not default 
overlap 
Asset A defaults and asset B 
Anywhere in A but not in 
pA – pAB 
does not default 
overlap 
Neither asset defaults 
Outside both circles
 1 – (pA + pB – pAB) 
Either asset A or asset B or 
Anywhere within outer 
pA + pB – pAB 
both assets default 
perimeter of circles 
EXHIBIT 22.9 
Case of High Default Correlation 
In the case default of the stronger asset is always associated with default of the weak-
er asset. 

727 
Credit Risk Modeling and Credit Default Swaps 
If pA equals pB then pAB = pA and default of either asset results in 
default of the other. In this instance the correlation is at its maximum of 
100%. 
As correlations go negative, a point arrives at which there is zero 
probability of both assets defaulting together. Graphically, there is no 
intersection between the two circles, as shown in Exhibit 22.10, and we 
have pAB = 0. The correlation becomes 
– pApB
ρ = ----------------------------------------
1 – pA 1 – pB 
A negative correlation of –100% can only occur if pA = 1 – pB—that is, 
for every default of asset A, asset B survives and vice versa. 
The price of the first-to-default basket is simply the area of the two 
nonoverlapping circles 
= pA + pB
Ωρ = ρ 
This is when the default basket is most expensive. 
We have seen above the price of a basket in the limits of low, high, 
and zero correlation. Given that Ω = pA + pB – pAB , we can write the 
price of a basket in terms of the default correlation as 
2
2
Ω = pA + pB – pApB – ρ pA – pA pB – pB 
EXHIBIT 22.10 
Negative Default Correlation Case 
As the default correlation becomes negative, the two circles separate implying that 
the joint default probability has fallen to zero. 

728 
The Mathematics of Financial Modeling and Investment Management 
As more assets are considered, more default combinations become 
possible. With just three assets we have the following eight possibilities:
 ■ No assets default
 ■ Only asset A defaults
 ■ Only asset B defaults
 ■ Only asset C defaults
 ■ Asset A and asset B default
 ■ Asset B and asset C default
 ■ Asset A and asset C default
 ■ Asset A and asset B and asset C default 
To price this basket we either need all of the joint probabilities or 
the pairwise correlations ρAB, ρBC, and ρAC (see Exhibit 22.11). The 
probability that the basket is triggered is given by 
Ω = pA + pB + pC –
–
–
pAB pBC pAC + pABC 
Joint Poisson Process 
Recent evidence (for example, Enron, WorldCom, and Quest) demon-
strated that severe economic hardship and publicity can cause chain 
defaults for even very large firms. Hence, incorporating default correla-
tion is an important task in valuing credit derivatives. 
As stated above, the period-end joint default probability by two ref-
erence entities is as follows: 
Pr(A ∩ B) = E[1A 
= 
∩ B] 
pAB 
EXHIBIT 22.11 
Venn Diagram for Three Issuers 

729 
Credit Risk Modeling and Credit Default Swaps 
where 1 is the indicator function.45 
The BSM model is particularly useful in modeling correlated 
defaults. If two firms do business together, it is likely that the two firms 
may have a certain relationship between their defaults. The BSM model 
provides an easy explanation as to how that may be modeled: 
(
) < KA ∩AB T
Pr(AA T
(
) < KB ) 
A bivariate diffusion of firm A and firm B can easily provide what we 
need. Under the BSM model, logarithm of asset price is normally distrib-
uted. Hence, the previous equation is the tail probability of a bivariate 
normal distribution. The correlation between the two normally distrib-
uted log asset prices characterizes the default correlation. When the corre-
lation in the bivariate normal is 100%, the distribution becomes a 
univariate normal distribution and the two firms default together. When 
the correlation is –100%, one firm defaulting implies the survival of the 
other firm; so there is always one that is live and one that is dead. 
While the BSM model cleverly explains how default risk is priced in 
the corporate debt conceptually, it remains a practical problem in that it 
cannot price today’s complex credit derivatives. Hence, researchers 
recently have developed a series of reduced form models that simplify 
the computations of the prices. 
Using Common Factors to Model Joint Defaults 
There are two ways to model joint defaults in a reduced form model. 
One way, proposed by Duffie and Singleton, is to specify a “common 
factor.”46 When this common factor jumps, all firms default. Firms also 
can do so on their own. The model can be extended to multiple common 
factors: market factor, industry factor, sector factor, and so on to cap-
ture more sophisticated joint defaults. 
Formally, let a firm’s jump process be47 
45 Recall from Chapter 6 that for any random variable X the following relationship 
[
] = 
X P . If X is the indicator function of the event A, X = 1A we can
holds: E X
∫
d 
write 
Ω 
(
)
E[1A ] = 
1A P
d 
= 
P
d 
= P A
∫
∫ 
Ω 
A 
46 Darrell Duffie and Kenneth Singleton, “Econometric Modeling of Term Structure 
of Defaultable Bonds,” Review of Financial Studies (December 1999), pp. 687–720. 
47 Darrell Duffie and Kenneth Singleton, unpublished lecture notes on credit deriva-
tives; and Darrell Duffie and Kenneth Singleton, “Simulating Correlated Defaults,” 
working paper, Stanford University (September 1998). 

730 
The Mathematics of Financial Modeling and Investment Management 
Ji = aiqM + qi 
where qM is the market jump process and qi is the idiosyncratic jump 
process. The coefficient ai is to capture different correlation levels. The 
joint event is then 
corr(Ji, Jj) = aiajvar[qM] 
Correlating Default Times 
Before we discuss how the default correlation is introduced, we need to 
discuss how single issuer default is modeled. The approach used is 
equivalent to the Jarrow-Turnbull model.48 A hazard rate, λ(t), is intro-
duced where λ(t)dt is the probability of defaulting in a small time inter-
val dt. This leads to the definition of the survival probability 
Q(0, T) = exp–∫ 
T 
λ s
 
0 ( ) s
d 
 
The probability of surviving to a time T and then defaulting in the 
next instant is therefore given by the density function: 
(
)exp–∫ 
T 
λ s
–dQ = λ T
 
0 ( ) s
d 
dT 
In the simple case when the hazard rate is constant over time so that 
λ(t) = λ we have 
–dQ = λexp(–λT)dT 
From this we see that the probability of defaulting at time T as 
given by –dQ shows that default times are exponentially distributed. By 
extension, the average time to default is given by computing 
∞ 
1
〈〉= λ Texp(–λT)dT = --
T
∫
λ
0 
48 Robert Jarrow and Stuart Turnbull, “Pricing Derivatives on Financial Securities 
Subject to Default Risk,” Journal of Finance 20, no. 1 (1995), pp. 53–86. 

731 
Credit Risk Modeling and Credit Default Swaps 
Knowing that defaults are normally distributed makes it easy to 
simulate default times for independent assets. We need to generate uni-
form random numbers in the range [0,1] and then given a term structure 
for the hazard rate, imply out the corresponding default time. For exam-
ple, if we denote the uniform random draw by u, the corresponding 
default time T* is given by solving 
u = exp(–λT*) 
to give 
log u
( )
T* = – ---------------
λ 
This is an efficient method for simulating default. Every random draw 
produces a corresponding default time. In terms of its usefulness, the 
only question is whether the default time is before or after the maturity 
of the contract being priced. 
There are many ways to introduce a default correlation between the 
different reference entities in a credit default basket. One way is to cor-
relate the default times. This correlation is defined as 
〈TATB〉– 〈TA〉TB
〈
 〉
 
ρ(TA, TB) = -----------------------------------------------------------------------------
2
〈 2 
TB 
TB
TA〉– 〈TA〉2 〈
 〉
 
– 〈
 〉2 
It is important to stress that this is not the same as the default corre-
lation. Although correlating default times has the effect of correlating 
default, there are two reasons they are not equivalent. First, there is no 
need to define a default horizon when correlating default times. To mea-
sure this correlation, we would observe a sample of assets over a long 
(infinite) period and compute the times at which each asset defaults. 
There is no notion of a time horizon for this correlation. 
Second, since the default time correlation equals 100% when Tj = Ti 
and when Tj = Ti + ϑ, it is possible to have 100% default time correla-
tion with assets defaulting at fixed intervals. 
Under a Poisson assumption,
1
1
〈TA〉= ------ and 〈
 〉
 
= -----
TB
λA 
λB 

732 
The Mathematics of Financial Modeling and Investment Management 
and
2 
2
1
TA 
〈 
〉2 = ------ and 
〈 
〉– TB
〈 
〉– TA 
1 
TB 
〈 
〉2 = -----
λA 
λB 
so we have 
ρ(TA, TB) = 〈TATB〉λAλ – 1
B 
Copula Function 
To generate correlated default times, we use the normal Copula function 
methodology as proposed by Li.49 A Copula function (see Chapter 6) is 
simply a specification of how the univariate marginal distributions com-
bine to form a multivariate distribution. For example, if we have N cor-
related uniform random variables U1, U2, …, UN then 
( 
u2 … 
…
C u1, 
, 
, uN) = Pr{U1 < u1, U2 < u2, 
, UN < uN} 
is the joint distribution function that gives the probability that all of the 
uniforms are in the specified range. 
In a similar manner we can define the Copula function for the default 
times of N assets: 
( 
…
C F1(T1), F2(T2), 
, FN(TN)) 
… 
= Pr{U1 < F1(T1), U2 < F2(T2), 
, UN < FN(TN)} 
where Fi(Ti) = Pr{ti < t}. 
There are several possible choices but here we define the Copula 
function Θ to be the multivariate normal distribution function with cor-
relation matrix ρ. We also define Φ–1 as the inverse of a univariate nor-
mal function. The Copula function is therefore given by 
–1
C u
= 
u1
–1 u2
u3
u4
…
( )  Θ(Φ–1(
), Φ
(
), Φ–1(
), Φ
(
), 
Φ–1(uN), ρ) 
where ρ is the correlation matrix. 
What this specification says is that in order to generate correlated 
default times, we must first generate N correlated multivariate gaussians 
denoted by u1, u2, u3, …, uN—one for each asset in the basket. These 
49 David X. Li, Credit Metrics Monitor, Risk Metrics Group (April 1999). 

733 
Credit Risk Modeling and Credit Default Swaps 
are then converted into uniform random variables by cumulative proba-
bility functions. 
Once we have the vector of correlated random uniforms u we can 
calculate the corresponding default times knowing that asset i defaults 
in trial n at time T given by 
lnuin 
= – ------------
Tin 
λi 
Comparing Default Correlation and Default Time Correlation 
In addition to correlating default times, we could correlate default 
events. There is no simple way to do this directly. It is better to correlate 
the assets using some other mechanism and then measure the default 
correlation a posteriori. The question is: If we implement a model which 
correlates default times, how does the correlation relate to default cor-
relation as defined above. 
In common with the case of default correlation, it is only possible 
to have a 100% pairwise correlation in default times between two 
assets if both assets have the same default probabilities. Otherwise, the 
distributions are centered around different average default times and 
having equal default times and different average default times is not 
compatible. 
If we assume that in both cases all assets have the same default 
probability, what is the difference between correlating default times and 
correlating default events? In the limit of zero correlation there is no dif-
ference as the assets default independently. In the limit of 100% correla-
tion there is a fundamental difference: If default times have a 100% 
correlation, then assets must default either simultaneously or with a 
fixed time difference.50 However, if there is 100% default correlation, 
then this means that the default of one asset within a certain horizon 
always coincides with the default of the other within the same horizon. 
In general, we would expect a 100% default correlation to imply that 
both assets default together, but this is not a strict requirement. In prac-
tice, the default of one asset may occur at any time and be followed by 
default of the other asset at the end of the horizon. Default correlation 
is 100%, but default times have a lower correlation. 
Consider also the effect of the default horizon. Given that default 
times are exponentially distributed, extending the default horizon 
50 Since the default time correlation of 100% is preserved under translations of the 
form Tj = Ti + ϑ. 

734 
The Mathematics of Financial Modeling and Investment Management 
makes it more likely for defaults to occur. Extending the default horizon 
therefore has the effect of increasing the measured default correlation. 
Indeed we must be careful to specify the horizon when we quote a 
default correlation. On the other hand, correlation of default times is 
independent of the trade horizon (i.e., the tenor of the default swap). 
There is also a link between default correlation and the hazard rate. 
For a fixed horizon, increasing the hazard rate for all assets makes 
default more likely within that horizon. If the assets are correlated, the 
measured default correlation must increase. However, the increase in 
default probability makes the distribution of default times more 
weighted towards earlier defaults. Yet, the default time correlation can 
remain unchanged. 
The analysis below shows that the default correlation is always 
lower than the default time correlation. This can be understood in quali-
tative terms as follows: To have the same basket price we have the same 
number of defaults before maturity. As default correlation is a direct 
measurement of the likelihood of two assets to default within a fixed 
horizon, it is more closely linked with the pricing of a basket default 
swap than a correlation of default times. Indeed, as we have shown in the 
one-period model above, the value of the basket default swap is a linear 
function of the default correlation. Though a correlation of default times 
introduces a tendency for assets to default within a given trade horizon, 
it is an indirect way to do this. As a result, a simulation of defaults with 
a certain default time correlation will always tend to have a lower default 
correlation. In other words, less default correlation is required in order 
to have the same effect as a correlation of default times.51 
SUMMARY
 ■ There are different forms of credit risk: default risk, spread risk, and 
downgrade risk.
 ■ Credit derivatives are financial instruments designed to transfer credit 
risk between two parties.
 ■ Credit default swaps are the most popular credit risk derivatives.
 ■ In a credit default swap, the protection buyer pays a fee, the swap pre-
mium, to the protection seller in return for the right to receive a pay-
ment conditional upon a default, also called a credit event. 
51 Numerical examples for pricing credit default swap baskets in the single-period 
and multi-period cases are provided in Chapter 10 in Anson, Fabozzi, Choudhry, 
and Chen, Credit Derivatives: Instruments, Applications, and Pricing. 

735
Credit Risk Modeling and Credit Default Swaps 
■ Credit default swaps for corporate and sovereign reference entities are 
standardized.
 ■ The International Swaps and Derivatives Association (ISDA) developed 
the ISDA Master Agreement which establishes international standards 
governing privately negotiated derivative trades (all derivatives).
 ■ The 1999 ISDA Credit Derivatives Definitions provides a list of eight 
possible credit events.
 ■ Credit derivative models can be partitioned into structural models and 
reduced form models.
 ■ Structural-type models represent default as an option: a company 
defaults on its debt if the value of the assets of the company falls below 
a certain default point.
 ■ Reduced form models model directly the likelihood of default or down-
grade.
 ■ Structural models use option theory.
 ■ Structural models model default on very reasonable assumption but are 
difficult to calibrate and computationally burdensome.
 ■ Structural models use Poisson processes to model the time of default.
 ■ A transition matrix defines the probability of transition between any 
two credit rating states.
 ■ Default correlation is a concept difficult to define.
 ■ Default correlation can be modeled with copula functions that model 
the correlation between the times of default. 


