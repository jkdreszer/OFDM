"""
Created on Thu Jul 14 15:40:32 2022

@author: dreszer
"""
import numpy as np
import matplotlib.pyplot as plt
import lib


#Parameters
time = 1

#Loading data 
reals = np.load("reals.npy")
imgs = np.load("imgs.npy")

fft = np.load("fft.npy")

#IDFT
signal = lib.idft2(reals, imgs, time) #own continous
signalD = lib.idft(reals, imgs) #own discrete
signalNp = np.fft.ifft(fft) #numpy fft

#Plotting
t = np.linspace(0, 1, len(signal))
tD = np.linspace(0,1, len(signalD))

plt.plot(tD, signalNp, '-p', color="orange")
plt.title(label="Numpy FFT")
plt.xlabel("Time [s]")
plt.ylabel("Magnitude")
plt.grid()
plt.show()

plt.plot(tD, signalD, '-p')
plt.title(label="Own - discrete")
plt.xlabel("Time [s]")
plt.ylabel("Magnitude")
plt.grid()
plt.show()

plt.plot(t, signal, '-')
plt.title(label="Own - continous")
plt.xlabel("Time [s]")
plt.ylabel("Magnitude")
plt.grid()
plt.show()
