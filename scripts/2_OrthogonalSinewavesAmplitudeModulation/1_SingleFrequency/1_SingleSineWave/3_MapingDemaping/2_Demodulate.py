import numpy as np
import matplotlib.pyplot as plt
pi = np.pi

# parameters
PERIOD_VECTOR_SIZE = 60
PERIOD_NUMBER = 5

# loading Rx vector from file and..
Rx = np.load('TxSignal.npy')

# .. ploting it
plt.plot(Rx)
plt.grid()
plt.show()

# spliting vector into time slots coresponding to single periods
RxPeriods = np.reshape(Rx,(5,60))

# decoding amplitudes of Rx time slots

amplitudes = [] # create amplitude list
t = np.linspace(0, 2*pi,PERIOD_VECTOR_SIZE, endpoint=False)
Ref = np.sin(t)


for RxPeriod in RxPeriods:
    dot  = np.dot(RxPeriod, Ref) 
    ampl = dot * 2 / PERIOD_VECTOR_SIZE #decode amplitude
    
    amplitudes.append(ampl) #add amplitude to list
    
print(amplitudes)  # print list
    