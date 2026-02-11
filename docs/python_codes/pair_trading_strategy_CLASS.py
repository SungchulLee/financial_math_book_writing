import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import statsmodels.api as sm

class PairTradingStrategy:
    def __init__(self, ticker_a="KO", ticker_b="PEP", start_date="2020-01-01", end_date="2023-12-31",
                 z_entry=2.0, z_exit=0.5, delta_threshold=0.002):
        self.ticker_a = ticker_a
        self.ticker_b = ticker_b
        self.start_date = start_date
        self.end_date = end_date
        self.z_entry = z_entry
        self.z_exit = z_exit
        self.delta_threshold = delta_threshold
        self.data = None
        self.returns = None
        self.beta = None
        self.zscore = None
        self.delta_spread = None
        self.ret_A_test = None
        self.ret_B_test = None

    def load_data(self):
        data = yf.download([self.ticker_a, self.ticker_b], start=self.start_date, end=self.end_date)["Close"].dropna()
        returns = np.log(data / data.shift(1)).dropna()
        self.data = data
        self.returns = returns
        ret_A, ret_B = returns[self.ticker_a], returns[self.ticker_b]
        split = len(returns) // 2
        self.ret_A_train, self.ret_A_test = ret_A[:split], ret_A[split:]
        self.ret_B_train, self.ret_B_test = ret_B[:split], ret_B[split:]

    def estimate_beta(self):
        X = sm.add_constant(self.ret_B_train)
        model = sm.OLS(self.ret_A_train, X).fit()
        self.beta = model.params.iloc[1]

    def construct_spread(self):
        spread = self.ret_A_test - self.beta * self.ret_B_test
        self.zscore = (spread - spread.mean()) / spread.std()
        self.delta_spread = spread.diff()

    def generate_positions(self, strategy="mean_reversion"):
        pos = pd.DataFrame(0.0, index=self.zscore.index, columns=[self.ticker_a, self.ticker_b])
        if strategy == "mean_reversion":
            pos.loc[self.zscore < -self.z_entry, self.ticker_a] = 1
            pos.loc[self.zscore < -self.z_entry, self.ticker_b] = -self.beta
            pos.loc[self.zscore > self.z_entry, self.ticker_a] = -1
            pos.loc[self.zscore > self.z_entry, self.ticker_b] = self.beta
            pos[self.zscore.abs() < self.z_exit] = 0
        elif strategy == "momentum":
            dz = self.delta_spread
            pos.loc[dz > self.delta_threshold, self.ticker_a] = 1
            pos.loc[dz > self.delta_threshold, self.ticker_b] = -self.beta
            pos.loc[dz < -self.delta_threshold, self.ticker_a] = -1
            pos.loc[dz < -self.delta_threshold, self.ticker_b] = self.beta
        elif strategy == "reverse_momentum":
            dz = self.delta_spread
            pos.loc[dz > self.delta_threshold, self.ticker_a] = -1
            pos.loc[dz > self.delta_threshold, self.ticker_b] = self.beta
            pos.loc[dz < -self.delta_threshold, self.ticker_a] = 1
            pos.loc[dz < -self.delta_threshold, self.ticker_b] = -self.beta
        pos = pos.shift(1).ffill().fillna(0)
        return pos

    def backtest(self, positions):
        pnl = positions[self.ticker_a] * self.ret_A_test + positions[self.ticker_b] * self.ret_B_test
        cum_ret = pnl.cumsum()
        value = 100 * np.exp(cum_ret)
        ann_ret = pnl.mean() * 252
        ann_vol = pnl.std() * np.sqrt(252)
        sharpe = ann_ret / ann_vol
        return pnl, cum_ret, value, ann_ret, ann_vol, sharpe

    def plot_equity_curve(self, value_dict):
        plt.figure(figsize=(12, 6))
        for strategy, value in value_dict.items():
            plt.plot(value["equity"], label=f"{strategy} (Sharpe={value['sharpe']:.2f})")
        plt.title("Equity Curve: Value of $100 Over Time")
        plt.xlabel("Date")
        plt.ylabel("Portfolio Value ($)")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    def run(self):
        self.load_data()
        self.estimate_beta()
        self.construct_spread()

        strategies = ["mean_reversion", "momentum", "reverse_momentum"]
        results = {}

        for strategy in strategies:
            pos = self.generate_positions(strategy)
            pnl, cum_ret, value, ann_ret, ann_vol, sharpe = self.backtest(pos)
            results[strategy] = {
                "pnl": pnl,
                "cum_return": cum_ret,
                "equity": value,
                "ann_return": ann_ret,
                "ann_vol": ann_vol,
                "sharpe": sharpe
            }

        self.plot_equity_curve(results)
        return results