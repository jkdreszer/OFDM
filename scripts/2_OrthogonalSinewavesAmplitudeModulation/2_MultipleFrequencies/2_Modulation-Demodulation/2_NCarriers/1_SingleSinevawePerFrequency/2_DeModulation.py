import numpy as np
import matplotlib.pyplot as plt
pi = np.pi

# loading Rx vector from file and..
Rx = np.load('TxSignal.npy')

# .. ploting it
plt.plot(Rx)
plt.axhline(y=0,color='black')
plt.grid()
plt.show()

# PARAMETERS
TIME_VECTOR_SIZE = 60

# CALCULATION
t = np.linspace(0, 2*pi,TIME_VECTOR_SIZE, endpoint=False)

ampl_l = ...
for f in range(1,...):
    dot  = ... 
    ampl = ...
    ampl_l.append(...) 

# PRESENTATION
for a in ...:
    print(f'{a:0.2f}',end=', ')
    
    