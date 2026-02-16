# Getting Started

Welcome to Quant Finance with Python! This page helps you set up your environment and get the most out of the course material.

## Python Environment Setup

### System Requirements

- **Python:** 3.8 or higher (3.9+ recommended)
- **OS:** Windows, macOS, or Linux
- **RAM:** 4 GB minimum (8 GB recommended)

### Core Dependencies

```bash
pip install numpy scipy pandas matplotlib
pip install sympy statsmodels scikit-learn
pip install cvxpy jupyter notebook
pip install yfinance pandas-datareader
pip install beautifulsoup4 lxml mplfinance requests selenium webdriver-manager
```

### Optional Advanced Libraries

```bash
pip install quantlib-python   # Advanced pricing
pip install torch tensorflow  # Deep learning (Ch 24)
pip install arch              # GARCH models
```

### Virtual Environment (Recommended)

```bash
python -m venv finmath_env

# Activate:
# Windows:  finmath_env\Scripts\activate
# Mac/Linux: source finmath_env/bin/activate

pip install -r requirements.txt
```

## How to Use This Course

### For Students (Self-Study)

1. **Read the chapter overview** (`index.md`) for context and learning objectives
2. **Work through the theory pages** in each section sequentially
3. **Study the Python Examples** section — run each `.py` file and understand the output
4. **Modify parameters** and observe how results change
5. **Refer to the Study Paths page** to choose a focus area

### For Instructors

1. **Semester planning:** Each chapter is designed for 1–3 weeks of lectures
2. **Homework:** Assign Python examples to modify and extend
3. **Projects:** Combine chapters (e.g., calibrate Heston model to real data using Ch 16–17)
4. **Exams:** Mix theoretical derivations with coding implementations

### Running Code Examples

Some Python scripts are **standalone** and can be run directly:

```bash
python docs/ch02/codes/brownian_motion_beginner_tutorial.py
```

Others require additional dependencies and must be executed from within the `python_code` folder where those dependencies are provided.

## Common Issues

### Import Errors

```bash
pip install --upgrade <package-name>
```

### Matplotlib Not Displaying

- Check backend: `matplotlib.use('TkAgg')`
- Or use `%matplotlib inline` in Jupyter

### Numerical Instabilities

- Check input parameters are within valid ranges
- Verify mathematical conditions (e.g., Feller condition for CIR model in Ch 18)
- Ensure time steps are small enough for explicit FD schemes (Ch 8)

## Project Ideas

### Derivatives Pricing

- Build a complete option pricing library covering BS, binomial trees, and Monte Carlo
- Implement and compare all three FD schemes (explicit, implicit, Crank–Nicolson) for European and American options
- Create an interactive implied volatility surface visualizer

### Volatility and Calibration

- Calibrate the Heston model to real SPX option data
- Compare local vol, stochastic vol, and rough vol models on the same data set
- Build a SABR calibration pipeline for swaption smiles

### Risk Management

- Implement a comprehensive VaR/ES system with historical, parametric, and Monte Carlo methods
- Build a CVA calculator using Hull–White interest rate simulation
- Create a portfolio risk dashboard with stress testing

### Machine Learning

- Train a neural network to approximate Black–Scholes pricing (Ch 24)
- Implement deep hedging and compare with classical delta hedging (Ch 24)
- Use reinforcement learning for dynamic portfolio optimization (Ch 24)

## Assessment Suggestions

### Problem Sets (40%)

- Weekly assignments combining theory and coding
- Mix of analytical derivations and Python implementations

### Midterm Projects (20%)

- First half: Build a complete option pricing library
- Second half: Implement a calibration or risk management system

### Final Project (20%)

- Research-oriented investigation with original implementation
- Written paper plus documented code
- Oral presentation

### Participation (10%)

- Code contributions and discussion of methods
