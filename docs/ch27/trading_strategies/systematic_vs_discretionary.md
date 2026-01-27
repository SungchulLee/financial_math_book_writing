# Systematic vs. Discretionary Weather Trading

## Learning Objectives

By the end of this section, you will be able to:

- Compare rule-based automated trading with discretionary approaches
- Understand the strengths and weaknesses of each methodology
- Learn from real-world case studies of both approaches
- Design a hybrid framework appropriate for weather-based strategies

---

## 1. The Fundamental Choice

Weather-based commodity trading presents a unique challenge: **Should signals be traded automatically or require human judgment?**

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    THE TRADING APPROACH SPECTRUM                            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  FULLY SYSTEMATIC                                      FULLY DISCRETIONARY  │
│        │                                                        │           │
│        ▼                                                        ▼           │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐  ┌──────────┐│
│  │Algorithm │    │ Rules +  │    │  Human   │    │ Intuition│  │  Pure    ││
│  │  Only    │───▶│ Override │───▶│ + Models │───▶│ + Data   │──▶│ Judgment ││
│  │          │    │          │    │          │    │          │  │          ││
│  └──────────┘    └──────────┘    └──────────┘    └──────────┘  └──────────┘│
│                                                                             │
│  Examples:                                                                  │
│  - HFT weather   - Most hedge  - Experienced  - Old-school  - "Feel" the   │
│    arbitrage       funds        meteorologist   traders       market        │
│  - Simple HDD    - Commodity    traders       - News-based                  │
│    mean revert     trading                                                  │
│                    advisors                                                 │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Systematic (Rule-Based) Approach

### 2.1 How It Works

```python
class SystematicWeatherTrader:
    """
    Fully automated weather-based trading system
    
    Signal Detection → Risk Check → Order Generation → Execution
    All without human intervention
    """
    
    def __init__(self, config: dict):
        self.hdd_threshold = config['hdd_z_threshold']  # e.g., 2.0
        self.model_agreement_threshold = config['model_agreement']  # e.g., 0.7
        self.max_position = config['max_position']
        self.stop_loss_pct = config['stop_loss_pct']
        
    def run_trading_loop(self):
        """Main trading loop - runs continuously"""
        while market_is_open():
            # 1. Fetch latest weather data
            weather_data = self.fetch_weather_models()
            
            # 2. Calculate signal (no human input)
            signal = self.calculate_signal(weather_data)
            
            # 3. Check risk limits
            if self.passes_risk_checks(signal):
                # 4. Generate and execute order
                order = self.generate_order(signal)
                self.execute_order(order)  # Automatic execution
            
            # 5. Monitor positions
            self.check_stop_losses()
            
            time.sleep(300)  # Check every 5 minutes
    
    def calculate_signal(self, weather_data: dict) -> dict:
        """
        Pure rule-based signal generation
        
        Rules:
        1. HDD z-score > threshold → LONG
        2. HDD z-score < -threshold → SHORT
        3. Model agreement > threshold → Full size
        4. Otherwise → No trade
        """
        hdd_z = weather_data['hdd_z_score']
        model_agreement = weather_data['model_agreement']
        
        # Strict rules, no exceptions
        if abs(hdd_z) < self.hdd_threshold:
            return {'direction': 'FLAT', 'size': 0}
        
        if model_agreement < self.model_agreement_threshold:
            return {'direction': 'FLAT', 'size': 0}
        
        direction = 'LONG' if hdd_z > 0 else 'SHORT'
        size = int(self.max_position * model_agreement)
        
        return {'direction': direction, 'size': size, 'z_score': hdd_z}
```

### 2.2 Advantages of Systematic Trading

| Advantage | Description | Impact |
|-----------|-------------|--------|
| **Emotion-Free** | No fear, greed, or hesitation | Consistent execution |
| **Speed** | Millisecond reaction to data | First-mover advantage |
| **Scalability** | Monitor 100+ signals simultaneously | Broader coverage |
| **Backtestable** | Precise historical performance | Strategy validation |
| **Consistency** | Same rules every time | Repeatable process |
| **24/7 Operation** | No sleep, no breaks | Never miss a signal |

### 2.3 Disadvantages of Systematic Trading

| Disadvantage | Description | Real-World Impact |
|--------------|-------------|-------------------|
| **Black Swan Blindness** | Can't adapt to unprecedented events | 2021 Texas: Models failed completely |
| **Overfitting Risk** | Backtest ≠ live performance | Many "profitable" systems fail live |
| **Model Degradation** | Markets adapt, edges disappear | Requires constant updating |
| **Infrastructure Risk** | Server down = missed trades | Single point of failure |
| **Garbage In, Garbage Out** | Bad data → bad trades | Weather data delays/errors |

---

## 3. Discretionary Approach

### 3.1 How It Works

```python
class DiscretionaryWeatherTrader:
    """
    Human-in-the-loop weather trading
    
    Signal Detection → Human Analysis → Decision → Manual Execution
    """
    
    def __init__(self, config: dict):
        self.alert_thresholds = config['alert_thresholds']
        self.notification_channels = config['notifications']
        
    def run_monitoring_loop(self):
        """Monitor and alert, but human decides"""
        while True:
            # 1. Fetch weather data
            weather_data = self.fetch_weather_models()
            
            # 2. Check for alert conditions
            alerts = self.check_alert_conditions(weather_data)
            
            if alerts:
                # 3. Send alert to human trader
                self.send_alert(alerts)
                
                # 4. HUMAN DECIDES what to do
                # - Review the data
                # - Check additional sources (news, satellite, etc.)
                # - Consider factors not in the model
                # - Make trading decision
                # - Execute manually (or not)
            
            time.sleep(300)
    
    def human_decision_factors(self) -> list:
        """
        Factors a discretionary trader considers beyond the model
        """
        return [
            "Is this weather pattern similar to anything I've seen before?",
            "What are other traders saying on Twitter/Bloomberg chat?",
            "Is there news the model doesn't capture (pipeline outage, etc.)?",
            "Does the price action 'feel' right for this setup?",
            "Am I emotionally compromised right now?",
            "What's my conviction level on a 1-10 scale?",
            "If I'm wrong, what's the worst case?",
            "Is this a 'fat pitch' I should swing big on?"
        ]
```

### 3.2 Advantages of Discretionary Trading

| Advantage | Description | Impact |
|-----------|-------------|--------|
| **Adaptability** | Can handle novel situations | Better in Black Swans |
| **Context Awareness** | Integrates non-quantifiable info | Richer analysis |
| **Pattern Recognition** | Human intuition from experience | Catches model failures |
| **Selective Engagement** | Only trade high-conviction setups | Quality over quantity |
| **Loss Limits** | Can override system in crisis | Capital preservation |

### 3.3 Disadvantages of Discretionary Trading

| Disadvantage | Description | Real-World Impact |
|--------------|-------------|-------------------|
| **Emotional Bias** | Fear, greed, FOMO, revenge trading | Inconsistent results |
| **Slow Reaction** | Minutes vs. milliseconds | Miss fast-moving opportunities |
| **Fatigue** | Can't monitor 24/7 | Miss overnight signals |
| **Inconsistency** | Different decisions on same setup | Hard to evaluate edge |
| **Hindsight Bias** | "I knew it" after the fact | Overconfidence |

---

## 4. Real-World Case Studies

### 4.1 Case Study: The 2014 Polar Vortex — Systematic Success

**Background**: January 2014 saw a severe polar vortex event that sent natural gas prices from $4.20 to $5.70 (+36%).

**The Systematic Trader's Experience:**

```
Timeline:
Day -7:  GFS model shows extreme cold signal
         System detects: HDD z-score = 2.8
         Model agreement: 0.65 (moderate)
         ACTION: System initiates 50% position (rules say wait for higher agreement)

Day -5:  ECMWF confirms cold blast
         Model agreement rises to 0.85
         ACTION: System adds to 100% position automatically at 2:15 AM
         (Trader was asleep)

Day -3:  Media coverage begins
         Price already up 15%
         ACTION: System holds per rules (no exit signal)

Day 0:   Cold arrives
         Price up 30%
         ACTION: System begins scaling out per profit-taking rules

Result:  Captured 25% of the 36% move
         No emotional decisions
         Executed at 2:15 AM when human would be asleep
```

**Key Insight**: The system's advantage was **speed and consistency**. It added to the position at 2:15 AM when the ECMWF model updated — a time when discretionary traders were asleep.

---

### 4.2 Case Study: The 2021 Texas Freeze — Systematic Failure

**Background**: February 2021 saw unprecedented cold in Texas, causing power grid collapse and natural gas spot prices to spike from $3 to $400+.

**The Systematic Trader's Experience:**

```
Timeline:
Day -7:  Models show cold signal for Texas
         System detects: Regional HDD z-score = 3.2
         ACTION: System goes LONG natural gas futures

Day -5:  Cold forecast intensifies
         System adds to position (per rules)
         Maximum position reached

Day -3:  Forecast shows -10°F in Dallas (unprecedented)
         System has NO RULE for "unprecedented"
         ACTION: System holds position, no adjustment

Day -1:  ERCOT issues emergency alert
         System doesn't process ERCOT alerts (not in model)
         ACTION: No change

Day 0:   Grid collapse begins
         Spot prices spike to $50, then $100, then $200
         Futures move "only" to $15 (contango collapses)
         System's futures position gains 150%
         
Day +1:  Margin calls across the market
         System's broker raises margin requirements 5x
         FORCED LIQUIDATION at worst possible time
         System gives back most gains

Day +2:  Spot prices hit $400
         System has no position (was liquidated)
         Trader (human) is furious

Post-Event Analysis:
- System made money initially but couldn't adapt
- Didn't understand "grid collapse" as a category
- Couldn't anticipate margin call risk
- No rule for "exit everything, this is unprecedented"
```

**What a Discretionary Trader Did:**

```
Day -3:  Sees forecast, but also:
         - Reads about poor Texas grid winterization
         - Remembers 2011 Texas cold event (smaller scale)
         - Thinks: "This could be much worse than models show"
         ACTION: LONG natural gas, but also:
                 - Buys OTM call options (tail hedge)
                 - Reduces position size (uncertainty)
                 - Sets alert for ERCOT grid status

Day -1:  ERCOT emergency alert
         Human judgment: "This is going to be a disaster"
         ACTION: Adds to option position
                 Moves some capital to spot exposure (ETF)
                 Calls broker about margin requirements

Day 0:   Grid collapse
         Human trader stays calm (expected chaos)
         ACTION: Takes profits on options (+500%)
                 Holds futures (smaller position)
                 Avoids margin call (had buffer)

Result:  Discretionary trader made 3x what systematic made
         Key advantage: Could process "unprecedented" information
```

**Key Insight**: The discretionary trader's edge was **contextual awareness**. They knew about Texas grid vulnerabilities from reading news, something no weather model captures.

---

### 4.3 Case Study: The "Boy Who Cried Wolf" — Discretionary Failure

**Background**: Winter 2019-2020 saw multiple false cold signals that never materialized as forecasted.

**The Discretionary Trader's Experience:**

```
November 2019:
- Models show cold blast coming
- Trader goes LONG
- Cold fails to materialize (models wrong)
- Loss: -8%

December 2019:
- Models show another cold signal
- Trader hesitates (burned before)
- Takes smaller position
- Cold fails again
- Small loss: -3%

January 2020:
- Models show strong cold signal (legitimate this time)
- Trader thinks: "These models keep failing"
- SKIPS THE TRADE (discretionary override)
- Cold actually arrives
- Would have been +20% gain
- Trader feels sick

February 2020:
- Another cold signal
- Trader now has no confidence
- Paralysis: Can't decide
- Misses another +10% move

Result: Discretionary trader's emotions led to:
        - Taking losses on weak signals
        - Missing profits on strong signals
        - Complete loss of confidence
        - Revenge trading later (more losses)
```

**What the Systematic Trader Did:**

```
Same period, systematic trader:
- Took ALL signals per rules
- November: -8%
- December: -5%
- January: +18%
- February: +12%
- Net: +17%

The system didn't "remember" past failures emotionally.
It just executed the rules every time.
When the rules were right, it captured the gains.
```

**Key Insight**: Discretionary trading suffers from **recency bias** and **loss aversion**. After a few losses, humans become gun-shy precisely when they should be executing.

---

## 5. The Hybrid Approach: Best of Both Worlds

### 5.1 Framework Design

The optimal approach for weather trading combines systematic signal generation with discretionary oversight:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        HYBRID TRADING FRAMEWORK                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  LAYER 1: SYSTEMATIC (Always Running)                                       │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  • Weather model ingestion (GFS, ECMWF, etc.)                       │   │
│  │  • Signal calculation (HDD z-score, model agreement)                │   │
│  │  • Risk metrics computation                                         │   │
│  │  • Alert generation                                                 │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                              │                                              │
│                              ▼                                              │
│  LAYER 2: RULES-BASED EXECUTION (Automatic for "Normal" Signals)           │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  IF signal meets all criteria AND no override flags:                │   │
│  │     → Execute automatically at predefined size                      │   │
│  │  IF signal is borderline OR override flag set:                      │   │
│  │     → Pass to Layer 3 for human review                              │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                              │                                              │
│                              ▼                                              │
│  LAYER 3: DISCRETIONARY OVERRIDE (Human Reviews Edge Cases)                 │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  Human reviews when:                                                │   │
│  │  • Signal strength is extreme (z > 4) — potential Black Swan        │   │
│  │  • External factors present (grid alerts, geopolitical, etc.)       │   │
│  │  • Position would exceed risk limits                                │   │
│  │  • Market conditions are abnormal (VIX spike, liquidity crisis)     │   │
│  │                                                                     │   │
│  │  Human can:                                                         │   │
│  │  • Approve the trade                                                │   │
│  │  • Modify position size                                             │   │
│  │  • Reject the trade                                                 │   │
│  │  • Add hedges (options, etc.)                                       │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 5.2 Implementation

```python
class HybridWeatherTrader:
    """
    Combines systematic signal generation with discretionary oversight
    """
    
    def __init__(self, config: dict):
        self.systematic_engine = SystematicEngine(config)
        self.human_oversight = HumanOversightModule(config)
        
        # Thresholds for automatic vs. human review
        self.auto_execute_z_range = (1.5, 3.5)  # Auto-execute in this range
        self.human_review_z_threshold = 3.5     # Review if above this
        self.external_factor_keywords = [
            'ERCOT', 'grid emergency', 'pipeline explosion',
            'force majeure', 'unprecedented'
        ]
    
    def process_signal(self, weather_data: dict, market_context: dict) -> dict:
        """
        Main decision logic
        """
        # Step 1: Systematic signal generation
        signal = self.systematic_engine.calculate_signal(weather_data)
        
        # Step 2: Check if automatic execution is appropriate
        requires_human_review = self.check_human_review_required(
            signal, market_context
        )
        
        if not requires_human_review:
            # AUTOMATIC EXECUTION
            return {
                'action': 'AUTO_EXECUTE',
                'signal': signal,
                'reason': 'Standard signal within normal parameters'
            }
        else:
            # HUMAN REVIEW REQUIRED
            review_packet = self.prepare_human_review(signal, weather_data, market_context)
            human_decision = self.human_oversight.request_review(review_packet)
            
            return {
                'action': 'HUMAN_REVIEWED',
                'signal': signal,
                'human_decision': human_decision,
                'modifications': human_decision.get('modifications', None)
            }
    
    def check_human_review_required(self, signal: dict, context: dict) -> bool:
        """
        Determine if human review is needed
        """
        reasons = []
        
        # Check 1: Extreme signal strength
        if abs(signal.get('z_score', 0)) > self.human_review_z_threshold:
            reasons.append(f"Extreme z-score: {signal['z_score']:.2f}")
        
        # Check 2: External factors in news
        news_text = context.get('recent_news', '')
        for keyword in self.external_factor_keywords:
            if keyword.lower() in news_text.lower():
                reasons.append(f"External factor detected: {keyword}")
        
        # Check 3: Abnormal market conditions
        if context.get('vix', 0) > 30:
            reasons.append(f"Elevated VIX: {context['vix']}")
        
        # Check 4: Liquidity concerns
        if context.get('bid_ask_spread', 0) > context.get('normal_spread', 0) * 2:
            reasons.append("Abnormal bid-ask spread")
        
        # Check 5: Position would exceed soft limits
        if signal.get('size', 0) > self.systematic_engine.max_position * 0.8:
            reasons.append("Large position size")
        
        if reasons:
            signal['review_reasons'] = reasons
            return True
        
        return False
    
    def prepare_human_review(self, signal: dict, weather: dict, context: dict) -> dict:
        """
        Prepare comprehensive packet for human review
        """
        return {
            'signal': signal,
            'weather_summary': {
                'hdd_z_score': weather['hdd_z_score'],
                'model_agreement': weather['model_agreement'],
                'forecast_confidence': weather.get('ensemble_spread', 'N/A'),
                'models': {
                    'GFS': weather.get('gfs_temp'),
                    'ECMWF': weather.get('ecmwf_temp'),
                    'consensus': weather.get('consensus_temp')
                }
            },
            'market_context': context,
            'review_reasons': signal.get('review_reasons', []),
            'historical_analogs': self.find_historical_analogs(weather),
            'risk_metrics': self.calculate_risk_metrics(signal),
            'recommended_action': self.systematic_engine.get_recommendation(signal),
            'timestamp': datetime.now(),
            'urgency': 'HIGH' if abs(signal.get('z_score', 0)) > 4 else 'NORMAL'
        }
```

### 5.3 When to Use Each Approach

| Scenario | Recommended Approach | Rationale |
|----------|---------------------|-----------|
| Normal HDD signal (z = 1.5-3) | **Systematic** | Bread-and-butter trades, consistency matters |
| Extreme cold (z > 4) | **Hybrid** | Potential Black Swan, need human context |
| Model disagreement | **Discretionary** | Uncertainty too high for rules |
| EIA report trading | **Systematic** | Speed critical, milliseconds matter |
| Infrastructure alerts (ERCOT) | **Discretionary** | External factor, models don't capture |
| Overnight/weekend | **Systematic** | Human not available |
| First trade with new strategy | **Discretionary** | Build confidence before automating |
| High VIX environment | **Hybrid** | Normal rules may not apply |

---

## 6. Practical Recommendations

### 6.1 For Individual Traders

#### Understanding "Discretionary Overlay"

Before discussing recommendations, let's clarify what "Discretionary Overlay" means:

**Overlay** = "위에 덮다", "겹쳐 놓다" (like Photoshop layers)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    SYSTEMATIC CORE + DISCRETIONARY OVERLAY                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   ┌─────────────────┐                                                       │
│   │ Discretionary   │  ← 투명한 레이어 (필요할 때만 개입)                     │
│   │    Overlay      │     Human intervenes only when needed                 │
│   ├─────────────────┤                                                       │
│   │                 │                                                       │
│   │   Systematic    │  ← 기본 레이어 (항상 실행)                              │
│   │      Core       │     Always running as the "base engine"               │
│   │                 │                                                       │
│   └─────────────────┘                                                       │
│                                                                             │
│   KEY INSIGHT:                                                              │
│   • Systematic Core = "Default" (기본값)                                    │
│   • Discretionary Overlay = "Exception handling" (예외 처리)                │
│   • Human doesn't replace the system, just adjusts it when necessary        │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Concrete Examples of Overlay in Action:**

```
═══════════════════════════════════════════════════════════════════════════════

CASE 1: Normal Situation (No Overlay)
─────────────────────────────────────
System Signal: LONG 10 contracts
Overlay: (no intervention)
Final Execution: LONG 10 contracts  ← System executes as-is

═══════════════════════════════════════════════════════════════════════════════

CASE 2: Human Adds Conviction (Overlay Increases Size)
──────────────────────────────────────────────────────
System Signal: LONG 10 contracts
Human Judgment: "I saw ERCOT grid vulnerability news, this could be bigger"
Overlay: +5 contracts added
Final Execution: LONG 15 contracts  ← System + Human judgment

═══════════════════════════════════════════════════════════════════════════════

CASE 3: Human Has Concerns (Overlay Reduces Size)
─────────────────────────────────────────────────
System Signal: LONG 10 contracts  
Human Judgment: "Lost on same signal last week, model confidence looks low"
Overlay: -5 contracts reduced
Final Execution: LONG 5 contracts  ← System signal reduced

═══════════════════════════════════════════════════════════════════════════════

CASE 4: Human Rejects (Overlay Cancels)
───────────────────────────────────────
System Signal: LONG 10 contracts
Human Judgment: "Black Swan feeling, something's off, I'll pass"
Overlay: CANCEL
Final Execution: NO TRADE  ← System signal ignored

═══════════════════════════════════════════════════════════════════════════════

CASE 5: Human Adds Hedge (Overlay Complements)
──────────────────────────────────────────────
System Signal: LONG 10 contracts (futures)
Human Judgment: "Could be extreme like 2021 Texas, need tail risk hedge"
Overlay: + Buy 5 OTM Call options (tail hedge)
Final Execution: LONG 10 contracts + 5 Call options  ← System + Hedge

═══════════════════════════════════════════════════════════════════════════════
```

**Key Distinction:**

| Term | Meaning | Analogy |
|------|---------|---------|
| **Override** | Complete replacement | Turn off system, human decides everything |
| **Overlay** | Adjust on top | System keeps running, human tweaks when needed |

**Real-World Analogy**: Think of it like a self-driving car. It drives automatically most of the time, but in dangerous situations, the human can grab the steering wheel. The human doesn't drive all the time, nor do they fully delegate—it's a **hybrid** approach.

**A Day in the Life of an Advanced Trader Using Overlay:**

```
09:00  System: No signal
       Overlay: (no intervention)
       
10:30  System: LONG signal after EIA report (z=2.1)
       Overlay: (normal range, no intervention)
       → Auto-executed
       
14:00  System: Additional LONG signal (z=2.8)
       Overlay: (normal range, no intervention)
       → Auto-executed
       
16:00  System: Strong LONG signal (z=4.5) ⚠️ EXTREME
       Trader: "z=4.5? I need to review this"
       News check: "ERCOT may issue emergency alert tomorrow"
       Overlay: Reduce size 50% + Buy OTM Calls
       → Modified trade executed
       
20:00  System: Additional signal (z=2.3)
       Trader: (went home, sleeping)
       Overlay: (no intervention - automatic)
       → Auto-executed
```

#### Trader Profile Recommendations

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                  RECOMMENDATION BY TRADER PROFILE                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  BEGINNER (< 2 years experience):                                           │
│  → Start DISCRETIONARY with systematic alerts                               │
│  → Learn why signals work before automating                                 │
│  → Keep position sizes small                                                │
│  → Journal every trade decision                                             │
│                                                                             │
│  INTERMEDIATE (2-5 years):                                                  │
│  → Move to HYBRID approach                                                  │
│  → Automate routine signals                                                 │
│  → Reserve discretion for edge cases                                        │
│  → Develop rules from your discretionary patterns                           │
│                                                                             │
│  ADVANCED (5+ years):                                                       │
│  → SYSTEMATIC as core                                                       │
│  → Discretionary overlay for regime changes                                 │
│  → Multiple strategy portfolio                                              │
│  → Focus on system improvement, not individual trades                       │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 6.2 Key Questions to Ask Yourself

Before choosing your approach, answer honestly:

1. **Can I watch markets 24/7?** If no → Need systematic component
2. **Do I revenge trade after losses?** If yes → Systematic better
3. **Can I code and maintain systems?** If no → Discretionary or outsource
4. **Do I have edge cases knowledge (grid ops, etc.)?** If yes → Discretionary value
5. **Is my capital small or large?** Small → Discretionary OK; Large → Need systematic scale
6. **What's my reaction time?** Slow → Systematic for fast markets

### 6.3 The Ultimate Hybrid Rule

!!! tip "The 80/20 Hybrid Rule"
    **80% Systematic**: Let the rules handle routine signals. Don't second-guess the system on normal trades. This captures the consistency advantage.
    
    **20% Discretionary**: Reserve human judgment for:
    
    - Extreme signals (z > 4)
    - External factors not in the model
    - Position sizing for conviction trades
    - Emergency stop-losses ("something feels wrong")
    
    The key discipline: **Don't let the 20% discretionary creep into the 80%**. If you find yourself overriding the system on routine trades, either fix the system or admit you're running a discretionary strategy.

---

## 7. Summary

| Approach | Best For | Worst For |
|----------|----------|-----------|
| **Systematic** | Consistent execution, scalability, overnight | Black swans, unprecedented events |
| **Discretionary** | Context awareness, adaptation, novel situations | Emotional control, consistency |
| **Hybrid** | Combining strengths, professional operations | Requires discipline to maintain boundaries |

The weather trading edge comes from **information processing speed** (favors systematic) combined with **contextual understanding** (favors discretionary). The optimal approach uses both, with clear rules about when each applies.

---

## References

1. Kavajecz, K. & Odders-White, E. (2004). "Technical Analysis and Liquidity Provision." *Review of Financial Studies*
2. Menkhoff, L. (2010). "The Use of Technical Analysis by Fund Managers." *Journal of Banking & Finance*
3. Covel, M. (2009). *Trend Following: How Great Traders Make Millions in Up or Down Markets*. FT Press.
4. Schwager, J. (2012). *Market Wizards: Interviews with Top Traders*. Wiley.
5. Lo, A. (2017). *Adaptive Markets: Financial Evolution at the Speed of Thought*. Princeton University Press.

---

!!! info "Next Section"
    Continue to [Risk Management for Weather Trading](../risk_management/weather_trading_risk_management.md) to understand how to protect capital in both approaches.
