import numpy as np
import matplotlib.pyplot as plt
pi = np.pi

# PARAMETERS
TIME_VECTOR_SIZE = 60
AMPL_VECTOR = (1.2, -3.4, 4.5, -1.2)
NOISE_DEAVIATION = 2
TRANSMISION_NR = 100

# CALCULATION
t = np.linspace(0, 2*pi,TIME_VECTOR_SIZE, endpoint=False)

# MODULATION AND DEMODULATION
Carrier = np.sin(t)
Ref = Carrier

demodulated_amplitudes = []

for i in range(TRANSMISION_NR):
    amp = AMPL_VECTOR[i%4]
    Tx = Carrier * amp #modulation
    
    #channel
    noise = np.random.normal(0, NOISE_DEAVIATION, TIME_VECTOR_SIZE)
    Rx = Tx + noise

    #demodulation
    dot = np.dot(Rx, Ref)
    ampl = dot * 2 / TIME_VECTOR_SIZE
    demodulated_amplitudes.append(ampl)


# PRESENTATION  

#Tx plot
plt.plot(range(TRANSMISION_NR), demodulated_amplitudes, 'p')
plt.axhline(y=0,color='black')
plt.grid(axis='y')
plt.show()


