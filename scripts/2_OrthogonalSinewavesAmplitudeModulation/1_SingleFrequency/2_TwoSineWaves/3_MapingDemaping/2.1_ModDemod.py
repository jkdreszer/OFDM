import numpy as np
import matplotlib.pyplot as plt
pi = np.pi

# PARAMETERS
TIME_VECTOR_SIZE = 60

AMPL_VECTOR_SIN = ( 0.12, -3.4, 5.6, -7.8)
AMPL_VECTOR_COS = ( 8.7,   6.5, 4.3,  2.1)

# CALCULATION
t = np.linspace(0, 2*pi,TIME_VECTOR_SIZE, endpoint=False)

carrier_sin = ref_sin = np.sin(t) 
carrier_cos = ref_cos = np.cos(t) 

amplitudes_sin = list()
amplitudes_cos = list()

for ampl_sin, ampl_cos in zip(AMPL_VECTOR_SIN, AMPL_VECTOR_COS):
    
    # modulation
    Tx =  ...   
    
    # channel
    Rx = ... # ideal
        
    # demodulation
    ampl = ...
    amplitudes_sin.append(ampl)
    
    ampl = ...
    amplitudes_cos.append(ampl)

# PRESENTATION
# presentation
amplitudes_sin = np.array(amplitudes_sin) # convert list to numpy 1D array
amplitudes_cos = np.array(amplitudes_cos) # ...
np.set_printoptions(precision=2)          # set numpy array print precision

print(f'amplitudes_sin = {amplitudes_sin}')
print(f'amplitudes_cos = {amplitudes_cos}')

