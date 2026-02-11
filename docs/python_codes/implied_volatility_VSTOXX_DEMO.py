import numpy as np
import matplotlib.pyplot as plt

# Requires: ImpliedVol class
# Data: vstoxx_data_31032014.h5
# Download from: https://github.com/psygement/financepy/blob/master/part1/ch03/source/vstoxx_data_31032014.h5

def main():
    S = 17.6639 # 2014-03-31 VSTOXX Close
    # K read from data
    # T read from data
    r = 0.01
    # sigma will be computed in this code

    iv = ImpliedVol(S, r, tol=0.5)
    iv.compute_implied_volatility()
    # read only rows with implied volatility computed
    # if not computed, corresponding 'IMP_VOL' is np.NaN
    df = iv.options_data
    df.dropna(subset='IMP_VOL',inplace=True)

    maturities = sorted(set(df['MATURITY']))

    fig, ax = plt.subplots(figsize=(12,5))
    for maturity in maturities: # maturity --- Timestamp object, for example Timestamp('2014-04-18 02:00:00')
        data = df[df.MATURITY == maturity] # select data for this maturity
        ax.plot(data['STRIKE'], data['IMP_VOL'], label=maturity.date(), lw=0.7, alpha=0.9, ls="--",
                marker='.',
                markersize=5,
                markeredgecolor='black',
                markeredgewidth=0.1,
                markerfacecolor='black')
    ax.grid()
    ax.set_xlabel('strike')
    ax.set_ylabel('implied volatility')
    ax.legend()
    plt.show()

if __name__ == "__main__":
    main()