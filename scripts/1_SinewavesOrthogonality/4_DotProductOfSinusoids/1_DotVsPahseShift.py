import numpy as np
import matplotlib.pyplot as plt
pi = np.pi

# PARAMETER
PHASE_SHIFT = pi/2 + pi/2

# VECTORS
t = np.linspace(0, 2*pi,30, endpoint=False)

SinRef = np.sin(t)
SinShift = np.sin(t+PHASE_SHIFT)
SinRef_mult_SinShift = SinRef * SinShift
Sin_dot = sum(SinRef_mult_SinShift)

# PLOTS

plt.plot(t, SinRef, '-p', label='Sin', color="blue")
plt.plot(t, SinShift, '-p', label='SinShift', color="green")
plt.xlim(-0.25, 6.25)
plt.ylim(-1.3,1.25)
plt.axhline(y=0,color='yellow')
plt.grid()
plt.legend()
plt.show()


plt.stem(t, SinRef_mult_SinShift, 'p')
plt.xlim(-0.25, 6.25)
plt.ylim(-1.5, 1.25)
plt.axhline(y=0,color='red')
plt.grid()
plt.legend()
plt.show()

print("Dot product: {:.2f}".format(Sin_dot))

