import numpy as np
import matplotlib.pyplot as plt
pi = np.pi

# PARAMETERS
TIME_VECTOR_SIZE = 60

AMPL_F1 = 4.3 
AMPL_F2 = 2.1 

# CALCULATION
t = np.linspace(0, 2*pi,TIME_VECTOR_SIZE, endpoint=False)

carrier_f1 = np.sin(t)
carrier_f2 = np.sin(2*t)

tx_f1 = AMPL_F1 * carrier_f1
tx_f2 = AMPL_F2 * carrier_f2

Tx = tx_f1 + tx_f2

# PRESENTATION
plt.plot(Tx, color='black')
plt.axhline(y=0,color='black')
plt.grid()
plt.show()

# SAVING
np.save('TxSignal',Tx)

