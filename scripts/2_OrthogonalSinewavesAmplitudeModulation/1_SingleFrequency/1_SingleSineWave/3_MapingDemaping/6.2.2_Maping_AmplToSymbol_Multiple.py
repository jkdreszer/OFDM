import numpy as np
import matplotlib.pyplot as plt
from mapper_lib import ampl_to_symbol



amplitudes_l = np.linspace(-1, 1, 100)
for symbol_nr in 2,4,8:
    symbols_l =[]
    for amplitude in amplitudes_l:
        symbol = ampl_to_symbol(symbol_nr, amplitude)
        symbols_l.append(symbol)    
    plt.plot(amplitudes_l,symbols_l,'-p', label=f"symbol nr = {symbol_nr}")     
    
plt.legend()    
plt.grid()
plt.xlabel('Amplitude')
plt.ylabel('Symbol')
