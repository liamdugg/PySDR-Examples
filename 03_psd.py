import numpy as np
import matplotlib.pyplot as plt

fs = 300
ts = 1/fs
N = 2048

t = ts*np.arange(N)
x = np.exp(1j*2*np.pi*50*t) # 50 hz sine wave

# complex noise with unity power
n = (np.random.randn(N) + 1j*np.random.randn(N)/np.sqrt(2))
noise_pwr = 2

r = x + n*np.sqrt(noise_pwr)

psd = np.abs(np.fft.fft(r)**2 / (N*fs)) # div by N*fs for scaling
psd_db = 10.0*np.log10(psd)
psd_shifted = np.fft.fftshift(psd_db)

# frequency x axis
f = np.arange(-fs/2.0, fs/2.0, fs/N)

plt.plot(f, psd_shifted)
plt.xlabel("Frequency [Hz]")
plt.ylabel("Magnitude [dB]")
plt.grid(True)
plt.show()
