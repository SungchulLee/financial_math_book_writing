# Visualize Fast Fourier Transform

## Background

Visualize Fft

Educational script demonstrating visualize fft concepts.

---

## Code

```python
"""
Visualize Fft

Educational script demonstrating visualize fft concepts.
"""

# ============================================================================
# VISUALIZE_FFT.py
# ============================================================================
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np

# Time domain: sample 1 second of signal at 1000 Hz


if __name__ == "__main__":
    fs = 1000  # Sampling frequency (samples per second)
    T = 1      # Total time in seconds
    N = fs * T # Total number of samples
    t = np.linspace(0, T, N, endpoint=False)  # Time array

    # Signal: combination of 50 Hz and 120 Hz sinusoids
    freqs = (50, 120)
    mags = (1, 0.5)

    signal = np.zeros_like(t)
    for mag, freq in zip(mags, freqs):
        signal += mag * np.sin(2 * np.pi * freq * t)

    # FFT and frequency bins
    signal_fft = np.fft.fft(signal)
    frequencies = np.fft.fftfreq(N, d=1/fs) # d = t[1] - t[0]

    # IFFT reconstruction
    signal_reconstructed = np.fft.ifft(signal_fft)
    print("Reconstruction matches original:", np.allclose(signal, signal_reconstructed.real))

    # Set up custom layout: 2 rows, 2 columns
    fig = plt.figure(figsize=(14, 6))
    gs = gridspec.GridSpec(2, 2, height_ratios=[1, 1])

    # First row: original vs reconstructed
    ax0 = fig.add_subplot(gs[0, :])
    ax0.plot(t, signal, label='Original Signal', alpha=0.8)
    ax0.plot(t, signal_reconstructed.real, '--', label='Reconstructed Signal (IFFT)', alpha=0.8)
    ax0.set_title("Original vs Reconstructed Signal")
    ax0.set_xlabel("Time (s)")
    ax0.set_ylabel("Amplitude")
    ax0.legend()
    ax0.grid(True)

    # Second row, left: positive frequencies
    half_N = N // 2
    ax1 = fig.add_subplot(gs[1, 0])
    ax1.plot(frequencies[:half_N], np.abs(signal_fft[:half_N]) / N)
    ax1.set_title("Magnitude Spectrum (Positive Frequencies)")
    ax1.set_xlabel("Frequency (Hz)")
    ax1.set_ylabel("Magnitude")
    ax1.grid(True)

    # Second row, right: full spectrum
    ax2 = fig.add_subplot(gs[1, 1])
    ax2.plot(frequencies, np.abs(signal_fft) / N)
    ax2.set_title("Full Magnitude Spectrum (Including Negative Frequencies)")
    ax2.set_xlabel("Frequency (Hz)")
    ax2.set_ylabel("Magnitude")
    ax2.grid(True)

    plt.tight_layout()
    plt.show()
```

## Exercises

**Exercise 1.**
A signal is composed of two sinusoids at frequencies 50 Hz and 120 Hz with amplitudes 1 and 0.5. Write the mathematical expression for this signal and compute its FFT analytically.

??? success "Solution to Exercise 1"
    The signal is $x(t) = \sin(2\pi \cdot 50\,t) + 0.5\sin(2\pi \cdot 120\,t)$.

    The FFT of a sinusoid $\sin(2\pi f_0 t)$ produces peaks at $\pm f_0$ with magnitude $N/2$ (where $N$ is the number of samples). After normalization by $N$, the magnitude spectrum shows peaks of height $1/2$ at $\pm 50$ Hz and $0.25$ at $\pm 120$ Hz.

    The negative frequencies are a consequence of the real-valued signal: by Euler's formula, $\sin(\omega t) = (e^{i\omega t} - e^{-i\omega t})/(2i)$, producing symmetric positive and negative frequency components.

---

**Exercise 2.**
Explain the Nyquist theorem. With a sampling frequency of $f_s = 1000$ Hz, what is the maximum frequency that can be represented without aliasing?

??? success "Solution to Exercise 2"
    The Nyquist theorem states that a signal can be perfectly reconstructed from its samples if the sampling rate $f_s$ exceeds twice the highest frequency component: $f_s > 2f_{\max}$.

    The Nyquist frequency is $f_N = f_s / 2 = 500$ Hz. Any frequency component above 500 Hz would be aliased -- it would appear as a spurious lower-frequency component in the sampled signal. In this example, both signal frequencies (50 Hz and 120 Hz) are well below 500 Hz, so no aliasing occurs.

---

**Exercise 3.**
The code verifies that `np.allclose(signal, signal_reconstructed.real)` is `True`. Explain why IFFT perfectly reconstructs the original signal.

??? success "Solution to Exercise 3"
    The DFT and IDFT are exact inverses: $\text{IDFT}(\text{DFT}(x)) = x$ up to floating-point precision. This is because the DFT represents the signal as a sum of complex exponentials, and the IDFT reconstructs the signal from these coefficients.

    Mathematically: $X_k = \sum_{n=0}^{N-1} x_n e^{-2\pi i kn/N}$ and $x_n = \frac{1}{N}\sum_{k=0}^{N-1} X_k e^{2\pi i kn/N}$. The orthogonality of complex exponentials ensures exact inversion. The `np.allclose` check confirms that numerical round-off errors are negligible (typically on the order of $10^{-15}$).

---

**Exercise 4.**
Why does the magnitude spectrum show both positive and negative frequencies? How do you interpret the negative frequency components for a real-valued signal?

??? success "Solution to Exercise 4"
    The DFT produces coefficients for frequencies $f_k = k \cdot f_s / N$ for $k = 0, 1, \ldots, N-1$. Frequencies $k > N/2$ correspond to negative frequencies (by the periodicity of the DFT, $f_k = f_k - f_s$ for $k > N/2$).

    For a real-valued signal, the DFT satisfies the conjugate symmetry property: $X_{N-k} = X_k^*$. This means positive and negative frequency components have equal magnitudes. The physical content is fully captured by the positive frequencies; the negative frequencies are redundant but necessary for the inverse transform to produce a real-valued result.
