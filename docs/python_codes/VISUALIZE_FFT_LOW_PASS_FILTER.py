# ============================================================================
# VISUALIZE_FFT_LOW_PASS_FILTER.py
# ============================================================================
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np

# Time domain: sample 1 second of signal at 1000 Hz
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