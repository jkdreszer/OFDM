import numpy as np
import matplotlib.pyplot as plt
from mapper_lib import symbol_to_ampl, ampl_to_symbol 

# PARAMETERS
TIME_VECTOR_SIZE = 60
TRANSMISIONS_NR = 1000

SYMBOL_NR = 8

t = np.linspace(0, 2*np.pi,TIME_VECTOR_SIZE, endpoint=False)
Carrier = np.sin(t) 
Ref     = Carrier

# TRANSMISION-RECEPTION
symbols_tx = np.random.randint(0,SYMBOL_NR,TRANSMISIONS_NR)    
print(f"SYMBOL_NR: {SYMBOL_NR}\n")
print("noise dev : error nr")
for deviation in np.linspace(0, 2, 10):
    symbols_rx = []
    for symbol in symbols_tx:   
         
        # modulation
        ampl = symbol_to_ampl(SYMBOL_NR, symbol)
        Tx = ampl*Carrier  
         
        # real channel
        noise = np.random.normal(0, deviation, TIME_VECTOR_SIZE)
        Rx = Tx + noise
        
        # demodulation
        ampl = (np.dot(Rx,Ref)/TIME_VECTOR_SIZE)*2  
        symbol = ampl_to_symbol(SYMBOL_NR, ampl)
        
        symbols_rx.append(symbol)

# PRESENTATION   
    symbols_rx = np.array(symbols_rx) # list to numpy array
    
    print(f"{(np.round(deviation,2))} : {sum(symbols_rx != symbols_tx)}")




