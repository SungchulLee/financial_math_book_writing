# Visualize Fast Fourier Transform Low Pass Filter

## Background

Visualize Fft Low Pass

Educational script demonstrating visualize fft low pass concepts.

---

## Code

```python
"""
Visualize Fft Low Pass

Educational script demonstrating visualize fft low pass concepts.
"""

# ============================================================================
# VISUALIZE_FFT_LOW_PASS_FILTER.py
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
    frequencies = np.fft.fftfreq(N, d=1/fs)
    low_pass_filter = np.exp( - 4 * np.pi**2 * frequencies**2 * 0.00001 )
    signal_fft *= low_pass_filter

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
The low-pass filter used is $H(f) = \exp(-4\pi^2 f^2 \cdot \alpha)$ with $\alpha = 10^{-5}$. Explain why this is called a Gaussian low-pass filter and what determines the cutoff frequency.

??? success "Solution to Exercise 1"
    The filter $H(f) = \exp(-4\pi^2 \alpha f^2)$ is a Gaussian function of frequency $f$. It attenuates high frequencies more than low frequencies because $|H(f)|$ decreases with $|f|$.

    The effective cutoff frequency $f_c$ is where the filter magnitude drops to $e^{-1} \approx 0.37$: $4\pi^2 \alpha f_c^2 = 1$, giving $f_c = 1/(2\pi\sqrt{\alpha})$. For $\alpha = 10^{-5}$: $f_c = 1/(2\pi \cdot 0.00316) \approx 50.3$ Hz. This means the 50 Hz component is barely attenuated while the 120 Hz component is significantly reduced.

---

**Exercise 2.**
After applying the low-pass filter, the reconstruction no longer matches the original signal. Compute the expected attenuation of the 120 Hz component with $\alpha = 10^{-5}$.

??? success "Solution to Exercise 2"
    The attenuation at 120 Hz is

    $$
    H(120) = \exp(-4\pi^2 \cdot 10^{-5} \cdot 120^2) = \exp(-4\pi^2 \cdot 0.144) \approx \exp(-5.685) \approx 0.0034
    $$

    So the 120 Hz component is reduced to about 0.34% of its original amplitude -- essentially removed.

    For comparison, at 50 Hz: $H(50) = \exp(-4\pi^2 \cdot 10^{-5} \cdot 2500) = \exp(-0.987) \approx 0.373$. The 50 Hz component is attenuated to about 37%.

---

**Exercise 3.**
Explain the connection between this Gaussian low-pass filter and the heat equation. What role does the parameter $\alpha$ play?

??? success "Solution to Exercise 3"
    The Gaussian filter $\exp(-4\pi^2 D k^2 t)$ is exactly the frequency-domain response of the heat equation $u_t = Du_{xx}$. Here $\alpha$ plays the role of $Dt$ (diffusivity times time).

    Applying the filter to a signal is equivalent to evolving it under the heat equation for time $t = \alpha/D$. Larger $\alpha$ means more diffusion (stronger smoothing). This connection explains why the heat equation is a natural model for smoothing and denoising: it exponentially damps high-frequency components while preserving low-frequency structure.

---

**Exercise 4.**
Design a band-pass filter (using the FFT) that passes only frequencies between 100 Hz and 150 Hz. Write the filter function $H(f)$.

??? success "Solution to Exercise 4"
    A sharp band-pass filter is

    $$
    H(f) = \begin{cases} 1 & \text{if } 100 \le |f| \le 150 \\ 0 & \text{otherwise} \end{cases}
    $$

    A smoother version using Gaussians:

    $$
    H(f) = \exp\!\Bigl(-\frac{(|f| - 125)^2}{2 \cdot 25^2}\Bigr)
    $$

    This is centered at 125 Hz with bandwidth controlled by the denominator. In code: `H = np.exp(-((np.abs(frequencies) - 125)**2) / (2 * 25**2))`. Applying this filter to the test signal would retain only the 120 Hz component and suppress the 50 Hz component.
