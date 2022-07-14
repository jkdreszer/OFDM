"""
Created on Thu Jul 14 12:45:00 2022

@author: dreszer
"""
import numpy as np

def sampling(input_signal, signal_time, sampling_freq):
    step = int(len(input_signal) / signal_time / sampling_freq)
    end = int(len(input_signal-step))
    
    t = np.linspace(0, signal_time, len(input_signal))[:end:step]
    sampledSignal = input_signal[:end:step]
    
    return (t, sampledSignal)


def dft(input_signal, N, startFreq,timeInput):
    
    t = np.linspace(0, timeInput, len(input_signal))
    
    freqs = []
    realVector = []
    imaginaryVector = []
    
    for k in range(N):
        cosinus = np.cos(2*np.pi * startFreq * k * t)
        sinus = (-1) * np.sin(2*np.pi * startFreq * k * t)
        
        dotCos = np.round(np.dot(input_signal, cosinus), 1)
        dotSin = np.round(np.dot(input_signal, sinus), 1)
        
        amplCos = dotCos * 2 / len(input_signal)
        amplSin = dotSin * 2 / len(input_signal)
        
        freqs.append(startFreq * k)
        realVector.append(amplCos)
        imaginaryVector.append(amplSin)        
    
    return (freqs, realVector, imaginaryVector)


def idft(freqs, amplR, amplI, time):
    
    signal = np.zeros(1000)
    t = np.linspace(0, time, 1000)
    
    for f, a in zip(freqs, amplR):
        cos = a * np.cos(2*np.pi * f * t)
        signal = signal + cos
    
    for f, a in zip(freqs, amplI):
        sin = -a * np.sin(2*np.pi * f * t)
        signal = signal + sin
        
    return signal
        
    
    
