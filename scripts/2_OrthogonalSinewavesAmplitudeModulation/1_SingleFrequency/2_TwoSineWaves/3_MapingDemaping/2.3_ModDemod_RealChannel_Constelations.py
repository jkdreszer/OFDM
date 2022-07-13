import numpy as np
import matplotlib.pyplot as plt
pi = np.pi

# PARAMETERS
TIME_VECTOR_SIZE = 60

NOISE_DEVIATION = 2

AMPL_VECTOR_SIN = ( 1,-1, 1,-1)
AMPL_VECTOR_COS = ( 1, 1,-1,-1)

TRANSMISION_NR = 10

# CALCULATION
t = np.linspace(0, 2*pi,TIME_VECTOR_SIZE, endpoint=False)

carrier_sin = ref_sin = np.sin(t) 
carrier_cos = ref_cos = np.cos(t) 

amplitudes_sin = list()
amplitudes_cos = list()

for i in range(TRANSMISION_NR):
    for ampl_sin, ampl_cos in zip(AMPL_VECTOR_SIN, AMPL_VECTOR_COS):
        
        # modulation
        Tx = (ampl_sin*carrier_sin) + (ampl_cos*carrier_cos)     
        
        # real channel
        noise = np.random.normal(0, NOISE_DEVIATION, TIME_VECTOR_SIZE)
        Rx = Tx + noise
            
        # demodulation
        ampl = (np.dot(Rx,ref_sin)/TIME_VECTOR_SIZE)*2  
        amplitudes_sin.append(ampl)
        
        ampl = (np.dot(Rx,ref_cos)/TIME_VECTOR_SIZE)*2  
        amplitudes_cos.append(ampl)
        

# PRESENTATION

plt.scatter(amplitudes_cos, amplitudes_sin)
plt.axhline(y=0, color="black")
plt.axvline(x=0, color="black")
plt.xlim(-2, 2)
plt.ylim(-2, 2)
plt.title(label="Rx amplitudes")
plt.xlabel(xlabel="cos amplitude")
plt.ylabel(ylabel="sin amplitude")
plt.grid()
plt.show()


