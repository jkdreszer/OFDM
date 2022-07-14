"""
Created on Thu Jul 14 12:08:11 2022

@author: dreszer
"""
import numpy as np
import matplotlib.pyplot as plt
import lib

#CONSTANTS AND PARAMETERS
PI = np.pi
TIME_VECTOR_SIZE = 10000

signalTime = 3
samplingFreq = 16

#INPUT SIGNAL PARAMETERS
#Frequencies [Hz]
f1 = 1 
f2 = 3 
f3 = 5 
f4 = 7 

#Amplitudes
ampl1 = 1
ampl2 = 0.3
ampl3 = 0.2
ampl4 = 0.1

t = np.linspace(0, signalTime, TIME_VECTOR_SIZE)

#CREATING SIGNAL
signal1 = ampl1 * np.sin(2*PI * f1 * t)
signal2 = ampl2 * np.sin(2*PI * f2 * t)
signal3 = ampl3 * np.sin(2*PI * f3 * t)
signal4 = ampl4 * np.sin(2*PI * f4 * t)

signal = signal1 + signal2 + signal3 + signal4

#SAMPLING
samplingResult = lib.sampling(signal, signalTime, samplingFreq)
samplesTime = samplingResult[0]
sampledSignal = samplingResult[1]

#PLOTTING SIGNAL AND SAMPLES
plt.plot(t, signal, '-', label = "Original signal")
plt.plot(samplesTime, sampledSignal, 'p', label = "Samples")
plt.xlabel("Time [s]")
plt.legend()
plt.show()

#CALCULATING DFT AND PRESENTING RESULTS
DFT = lib.dft(sampledSignal, 16, f1, signalTime)

print("\nFrequency[Hz] | Real value | Imaginary value |")
for freq, real, img in zip(DFT[0], DFT[1], DFT[2]):
    print(f"{freq:13d} | {real:10.1f} | {img:15.1f} |")
    

freqs = np.array(DFT[0])
np.save("freqs.npy", freqs)

reals = np.array(DFT[1])
np.save("reals.npy", reals)

imgs = np.array(DFT[2])
np.save("imgs.npy", imgs)



