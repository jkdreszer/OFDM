import numpy as np
import matplotlib.pyplot as plt
pi = np.pi

# PARAMETERS
TIME_VECTOR_SIZE = 60

#loading signal from file
Rx = np.load("TxSignal.npy")

#plotting signal
plt.plot(Rx)
plt.axhline(y=0,color='black')
plt.grid()
plt.show()


# calculation
t = np.linspace(0, 2*pi,TIME_VECTOR_SIZE, endpoint=False)

ref_f1 = np.sin(t)
ref_f2 = np.sin(2*t)

dot_f1 = np.dot(Rx, ref_f1)
dot_f2 = np.dot(Rx, ref_f2)

ampl_f1 = dot_f1 * 2 / TIME_VECTOR_SIZE
ampl_f2 = dot_f2 *2 / TIME_VECTOR_SIZE

# presentation
print(f"ampl_f1 = {ampl_f1}")
print(f"ampl_f2 = {ampl_f2}")

