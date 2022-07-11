import numpy as np
import matplotlib.pyplot as plt
pi = np.pi

# PARAMETERS
TIME_VECTOR_SIZE = 60

AMPL_F1_SIN =  8.7
AMPL_F1_COS = -6.5

AMPL_F2_SIN = -4.3
AMPL_F2_COS =  2.1

# CALCULATION
t = np.linspace(0, 2*pi,TIME_VECTOR_SIZE, endpoint=False)

carrier_f1_sin = ...
carrier_f1_cos = ...

carrier_f2_sin = ...
carrier_f2_cos = ...

tx_f1_sin = ...
tx_f1_cos = ...
tx_f2_sin = ...
tx_f2_cos = ...

Tx = ...

# PRESENTATION
plt.plot(Tx)
plt.axhline(y=0,color='black')
plt.grid()
plt.show()

# SAVING
np.save('TxSignal',Tx)

