import numpy as np
import matplotlib.pyplot as plt

num_symbols = 1000

x_int = np.random.randint(0, 4, num_symbols) # 0 to 3
x_degrees = x_int * 360.0/4.0 + 45
x_rad = x_degrees*np.pi/180.0
x_symb = np.cos(x_rad) + 1j*np.sin(x_rad)

# create noise
n = (np.random.randn(num_symbols) + 1j*np.random.randn(num_symbols))/np.sqrt(2)
n_pwr = 0.01

# add noise to symbols
r = x_symb + (n * np.sqrt(n_pwr))

# Phase noise example (comment the previous line)
# phase_noise = np.random.randn(len(x_symb)) * 0.1 # adjust multiplier for "strength" of phase noise
# r = x_symb * np.exp(1j*phase_noise)

plt.plot(np.real(r), np.imag(r), '.')
plt.grid(True)
plt.show()