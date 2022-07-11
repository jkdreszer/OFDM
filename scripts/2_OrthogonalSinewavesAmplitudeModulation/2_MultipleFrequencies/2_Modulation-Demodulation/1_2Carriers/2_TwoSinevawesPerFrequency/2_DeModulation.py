import numpy as np
import matplotlib.pyplot as plt
pi = np.pi

# parameters
PERIOD_VECTOR_SIZE = 60

# loading Rx vector from file and..
Rx = np.load('TxSignal.npy')

# .. ploting it
plt.plot(Rx)
plt.axhline(y=0,color='black')
plt.grid()
plt.show()

# CALLCULATION
t = np.linspace(0, 2*pi,PERIOD_VECTOR_SIZE, endpoint=False)

# references
ref_f1_sin = ...
ref_f1_cos = ... 

ref_f2_sin = ...
ref_f2_cos = ...

# dot products
dot_f1_sin = ... 
dot_f1_cos = ... 

dot_f2_sin = ... 
dot_f2_cos = ... 

# amplitudes
amp_f1_sin = ...  
amp_f1_cos = ... 

amp_f2_sin = ... 
amp_f2_cos = ... 

# PRESENTATION
print(f'amp_f1_sin={amp_f1_sin:0.1f}')
...

