import numpy as np
import matplotlib.pyplot as plt
pi = np.pi

# PARAMETERS
TIME_VECTOR_SIZE = 60
AMPL_VECTOR = (1.2, -3.4, 4.5, -1.2)

# CALCULATION
t = np.linspace(0, 2*pi,TIME_VECTOR_SIZE, endpoint=False)

# MODULATION AND DEMODULATION
Carrier = np.sin(t)
Ref = Carrier

demodulated_amplitudes = []

for amp in AMPL_VECTOR:
    Tx = Carrier * amp #modulation
    
    Rx=Tx #ideal channel

    #demodulation
    dot = np.dot(Rx, Ref)
    ampl = dot * 2 / TIME_VECTOR_SIZE
    demodulated_amplitudes.append(ampl)


# PRESENTATION  

#Tx plot
plt.plot(Rx)
plt.axhline(y=0,color='black')
plt.title(label="Last period")
plt.grid(axis='y')
plt.show()

#Print amplitudes
print(f'received amplitudes: {demodulated_amplitudes}')


