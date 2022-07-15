"""
Created on Thu Jul 14 12:08:11 2022

@author: dreszer
"""
import numpy as np
import matplotlib.pyplot as plt
import lib

#CONSTANTS AND PARAMETERS
PI = np.pi
TIME_VECTOR_SIZE = 8192

signalTime = 1
samplingFreq = 16

#INPUT SIGNAL PARAMETERS
#Frequencies [Hz]
f1 = 1
f2 = 3 
f3 = 4 
f4 = 6 
f5 = 7 

#Amplitudes
ampl0 = 0.25
ampl1 = 1
ampl2 = 0.4
ampl3 = 0.8
ampl4 = 0.1
ampl5 = 0.6

t = np.linspace(0, signalTime, TIME_VECTOR_SIZE)

#CREATING SIGNAL
signal0 = ampl0
signal1 = ampl1 * np.cos(2*PI * f1 * t)
signal2 = ampl2 * np.sin(2*PI * f2 * t)
signal3 = ampl3 * np.sin(2*PI * f3 * t)
signal4 = ampl4 * np.sin(2*PI * f4 * t)
signal5 = ampl5 * np.cos(2*PI * f5 * t)

signal = signal0 + signal1 + signal2 + signal3 + signal4 + signal5 


#SAMPLING
samplingResult = lib.sampling(signal, signalTime, samplingFreq)
samplesTime = samplingResult[0]
sampledSignal = samplingResult[1]


#CALCULATING DFT
DFT = lib.dft(sampledSignal) #own

fft = np.fft.fft(sampledSignal) #numpy fft

#SAVING DATA
reals = np.array(DFT[0])
np.save("reals.npy", reals)

imgs = np.array(DFT[1])
np.save("imgs.npy", imgs)

np.save("fft.npy", fft)


#PRESENTING RESULTS
print("FFT RESULT:")
print("Real value | Imaginary value |")
for real, img in zip(fft.real, fft.imag):
    print(f"{real:10.1f} | {img:15.1f} |")
    
    
print('\n')

print("OWN RESULT:")
print("Real value | Imaginary value |")
for real, img in zip(DFT[0], DFT[1]):
    print(f"{real:10.1f} | {img:15.1f} |")
    

modules = np.array([lib.module(r, i) for r,i in zip(reals, imgs)])
modules = modules/(max(modules))

freqs = [f for f in range(len(reals))]
xticks = [f for f in freqs if modules[f] > 0.05]



plt.stem(freqs, modules)

plt.xlabel("Frequency [Hz]")
plt.xlim(-0.2, len(freqs))
plt.xticks(xticks)

plt.ylabel("Normalized magnitude")
plt.ylim(0, 1.05)

plt.title("Spectrum")
plt.grid()
plt.show()

#PLOTTING SIGNAL AND SAMPLES
plt.plot(t, signal, '-', label = "Original signal")
plt.plot(samplesTime, sampledSignal, 'p', label = "Samples")
plt.xlabel("Time [s]")
plt.ylabel("Magnitude")
plt.legend()
plt.grid()
plt.show()


