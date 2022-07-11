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

# rx time slots plot and decoding
for RxPeriod in RxPeriods:
    plt.plot(RxPeriod)
    plt.ylim(-2,2)
    plt.grid()    
    plt.show()
    
    t = np.linspace(0, 2*pi,PERIOD_VECTOR_SIZE, endpoint=False)
    Ref  = ...     
    dot  = ...
    ampl = ...      
    print(...)
    



