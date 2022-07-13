import numpy as np
import matplotlib.pyplot as plt
pi = np.pi

Rx = np.load('TxSignal.npy')

plt.plot(Rx)
plt.axhline(y=0,color='black')
plt.grid()
plt.show()

# PARAMETERS
TIME_VECTOR_SIZE = 60

# CALCULATION
t = np.linspace(0, 2*pi,TIME_VECTOR_SIZE, endpoint=False)

ampl_sin_l = []
ampl_cos_l = []

for f in range(1,7):
    dot_sin = np.dot(Rx, np.sin(2 * f * t))
    dot_cos = np.dot(Rx, np.cos(2 * f * t))
    
    ampl_sin = dot_sin * 2 / TIME_VECTOR_SIZE
    ampl_cos = dot_cos * 2 / TIME_VECTOR_SIZE
    
    ampl_sin_l.append(ampl_sin) 
    ampl_cos_l.append(ampl_cos) 

for a in ampl_sin_l:
    print(f'{a:0.2f}',end=', ')    
print ()    
for a in ampl_cos_l:
    print(f'{a:0.2f}',end=', ')
    
    