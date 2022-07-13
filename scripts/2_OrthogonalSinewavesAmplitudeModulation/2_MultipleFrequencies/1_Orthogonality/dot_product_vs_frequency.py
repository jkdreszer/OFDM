import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2*np.pi,30, endpoint=False)
sin_blue  = np.sin(t)

dot_l = list()
freq_l = np.linspace(0, 8, 1000)
for freq in freq_l:    
    sin_green = np.sin(freq*t)
    dot_l.append(np.dot(sin_blue, sin_green))
    

i = 0
zeroFreqs = []
while (i < len(dot_l) - 1):
    if (dot_l[i] * dot_l[i+1] < 0):
        zeroFreqs.append(np.round(freq_l[i], 1))
    i+=1

plt.plot(freq_l, dot_l, color='green')
plt.axhline(y=0,color='black')
plt.xticks(ticks=zeroFreqs)
plt.xlim(0, 8)
plt.title('dot of "blue" and "green" frequencies when "blue" frequency equals to 1')
plt.xlabel('"green" frequency')
plt.ylabel('dot')
plt.grid()
plt.show()

