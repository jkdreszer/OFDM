import matplotlib.pyplot as plt
import numpy as np

PI = np.pi

t = np.linspace(0, PI, 9)
for i in range(len(t)):
    t[i] = np.rad2deg(t[i])
    i += 1 
dots = [15, 13.86, 10.61, 7.5, 0, -5.74, -10.61, -12.99, -15]


plt.plot(t, dots, '-p')
plt.xlabel("Shift [degrees]")
plt.xticks(range(0, 190, 10))
plt.xlim(0, 180)
plt.ylabel("Dot")
plt.axhline(y=0,color='black')
plt.grid()

plt.show()
