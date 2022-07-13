import numpy as np
import matplotlib.pyplot as plt
from mapper_lib import ampl_to_symbol

SYMBOL_NR = 8

amplitudes_l = np.linspace(-1, 1, 100)
symbols_l =[]
for amplitude in amplitudes_l:
    symbol = ampl_to_symbol(SYMBOL_NR, amplitude)
    symbols_l.append(symbol)    
plt.plot(amplitudes_l, symbols_l,'p')    
    
plt.grid()
plt.title(f'Symbol nr: {SYMBOL_NR}')
plt.xlabel('Amplitude')
plt.ylabel('Symbol')



