import numpy as np
import matplotlib.pyplot as plt
pi = np.pi

# PARAMETERS
TIME_VECTOR_SIZE = 60
AMPL_VECTOR = (1.2, -3.4, 4.5, -1.2, 3.4)

# CALCULATION
t = np.linspace(0, 2*pi,TIME_VECTOR_SIZE, endpoint=False)

# modulation
Carrier = np.sin(t)

plt.plot(Carrier)
plt.show()

Tx = np.array([])
for amp in AMPL_VECTOR:
    Tx = np.append(Tx, Carrier * amp)

# channel
Rx=Tx # ideal one    

# demodulation
RxPeriods = np.reshape(Rx,(5,60))

amplitudes_l = []
t = np.linspace(0, 2*pi,TIME_VECTOR_SIZE, endpoint=False)
Ref = np.sin(t)

for RxPeriod in RxPeriods:
    dot  = np.dot(RxPeriod, Ref) 
    ampl = dot * 2 / TIME_VECTOR_SIZE #decode amplitude
    
    amplitudes_l.append(ampl) #add amplitude to list

# PRESENTATION  

#Tx plot
plt.plot(Rx)
plt.axhline(y=0,color='black')
plt.grid(axis='y')
plt.show()

#  
print(f'received amplitudes: {amplitudes_l}')


