import numpy as np
import matplotlib.pyplot as plt
from scipy import signal 


pi = np.pi 

# time vector.
# from zero to 2pi in 30 steps
t = np.linspace(0, 4*pi,50, endpoint=False) #


# sinusoid with amplitude equal to 2 and time shift qual to pi/4
sinus = 1.75*np.sin(t+pi)

# triangular waveforms
#"0.5" denotes proportion between positive and negative slope

triangle = 2.75*signal.sawtooth(t, 0.5)

s = sinus + triangle


# PLOTS CUSTOMIZATION

# adding waveforms to figure
plt.plot(t,sinus, 'p', label='sinusoid', color='blue')
plt.plot(t,triangle,'-p', label='triangle', color='green')
plt.plot(t,s,'--', label='sum', color='brown')

# customizing figure
plt.title('Triangle + sinus')
plt.xlabel('time[s]')
plt.ylabel('amplitude[a.u.]')
plt.xlim(0,10)
plt.ylim(-4,6)
plt.axhline(y=0,color='yellow')
plt.grid()
plt.legend()

# drawing figure
plt.show()

