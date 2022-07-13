import numpy as np
import matplotlib.pyplot as plt
from mapper_lib import symbol_to_ampl, ampl_to_symbol 

# PARAMETERS
TIME_VECTOR_SIZE = 60
TRANSMISIONS_NR = 1000

#SYMBOL_NR = 8

t = np.linspace(0, 2*np.pi,TIME_VECTOR_SIZE, endpoint=False)
Carrier = np.sin(t) 
Ref     = Carrier

deviations = np.linspace(0,5,20)

# TRANSMISION-RECEPTION
 
for symbol_nr in 2,4,8:
    symbols_tx = np.random.randint(0,symbol_nr,TRANSMISIONS_NR)
    errorsNr = []
    for deviation in deviations:
        symbols_rx = []
        for symbol in symbols_tx:   
             
            # modulation
            ampl = symbol_to_ampl(symbol_nr, symbol)
            Tx = ampl*Carrier  
             
            # real channel
            noise = np.random.normal(0, deviation, TIME_VECTOR_SIZE)
            Rx = Tx + noise
            
            # demodulation
            ampl = (np.dot(Rx,Ref)/TIME_VECTOR_SIZE)*2  
            symbol = ampl_to_symbol(symbol_nr, ampl)
            
            symbols_rx.append(symbol)
            
        symbols_rx = np.array(symbols_rx) # list to numpy array
        errorsNr.append(sum(symbols_rx != symbols_tx))
    plt.plot(deviations, errorsNr, '-p', label=f"Symbol nr: {symbol_nr}")

plt.legend()    
plt.grid()
plt.xlabel('Noise deviation')
plt.ylabel('Error nr')




