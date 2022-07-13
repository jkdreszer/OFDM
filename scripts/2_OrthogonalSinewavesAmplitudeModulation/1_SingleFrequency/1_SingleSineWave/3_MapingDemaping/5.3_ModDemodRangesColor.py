import numpy as np
import matplotlib.pyplot as plt
pi = np.pi

# PARAMETERS
TIME_VECTOR_SIZE = 60
AMPL_VECTOR = np.linspace(0, 5, 8)
NOISE_DEAVIATION = 0.3
TRANSMISION_NR = 100

# CALCULATION
t = np.linspace(0, 2*pi,TIME_VECTOR_SIZE, endpoint=False)

# MODULATION AND DEMODULATION
Carrier = np.sin(t)
Ref = Carrier

demodulated_amplitudes = []

for i in range(TRANSMISION_NR):
    amp = AMPL_VECTOR[i%8]
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
plt.plot(demodulated_amplitudes[::8], 'p', color='r')
plt.plot(demodulated_amplitudes[1::8], 'p', color='g')
plt.plot(demodulated_amplitudes[2::8], 'p', color='b')
plt.plot(demodulated_amplitudes[3::8], 'p', color='c')
plt.plot(demodulated_amplitudes[4::8], 'p', color='m')
plt.plot(demodulated_amplitudes[5::8], 'p', color='y')
plt.plot(demodulated_amplitudes[6::8], 'p', color='pink')
plt.plot(demodulated_amplitudes[7::8], 'p', color='palegreen')

plt.yticks(AMPL_VECTOR)
plt.axhline(y=0,color='black')
plt.grid(axis='y')
plt.title(label = f"NOISE DEVIATION = {NOISE_DEAVIATION}")
plt.show()

print(f"Transmited amplitudes {AMPL_VECTOR}")


