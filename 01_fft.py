import numpy as np
import matplotlib.pyplot as plt

fs = 1 	# Hz
N = 100 # Points to sim (and fft size)

t = np.arange(N)
s = np.sin(0.15*2*np.pi*t)

# fft behaves as if the last sample of the slice connects back to the first sample.
# for an fft of 100 samples, using np.fft.fft(x), we want x[0] and x[99] to be equal or close in value.
# we use one of several "windowing" functions. for now we use the Hamming windowing function.
s = s * np.hamming(N)

# fft returns the array as
# DC value - positive freqs - negative freqs

# Use fftshift to show it as Neg-DC-Pos
S = np.fft.fftshift(np.fft.fft(s))
S_mag = np.abs(S)
S_phase = np.angle(S)

# New x axis labels
f = np.arange(fs/-2, fs/2, fs/N)

plt.figure(0)
plt.plot(f,S_mag)

plt.figure(1)
plt.plot(f,S_phase)
plt.show()