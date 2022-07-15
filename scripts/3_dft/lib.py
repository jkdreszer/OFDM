"""
Created on Thu Jul 14 12:45:00 2022

@author: dreszer
"""
import numpy as np


def sampling(input_signal, signal_time, sampling_freq):
    step = int(len(input_signal) / signal_time / sampling_freq)
    #end = int(len(input_signal-step))
    
    t = np.linspace(0, signal_time, len(input_signal))[::step]
    sampledSignal = input_signal[::step]
    
    return (t, sampledSignal)


def dft(input_signal):
    
    N = len(input_signal)
    
    realVector = []
    imaginaryVector = []
    
    for k in range(N):
        cosProducts = []
        sinProducts = []
        for n in range(N):
            cosinus = np.cos(2*np.pi * (n/N) * k)
            sinus = (-1) * np.sin(2*np.pi * (n/N) * k)
            
            cosProducts.append(input_signal[n] * cosinus)
            sinProducts.append(input_signal[n] * sinus)
            
        realVector.append(sum(cosProducts))
        imaginaryVector.append(sum(sinProducts))
    
    return (realVector, imaginaryVector)


def idft(amplR, amplI):
    N = len(amplR)
    signal = []

    for n in range(N):
        sample = 0
        for k in range(N):
            cos = amplR[k] * np.cos(2*np.pi * (n/N) * k)
            sin = -amplI[k] * np.sin(2*np.pi * (n/N) * k)
            
            sample += cos + sin
            
        signal.append(sample/N)

    return signal


def idft2(amplR, amplI, time):
    
    signal = np.zeros(1000)
    t = np.linspace(0, time, 1000)
    
    amplR = amplR[:len(amplR)//2]
    amplI = amplI[:len(amplI)//2]
    
    for k, real, img in zip(range(len(amplR)), amplR, amplI):
        cos = real  / len(amplR) * np.cos(2*np.pi * k * t)
        sin = -img  / len(amplR) * np.sin(2*np.pi * k * t)
        signal = signal + cos + sin

    return signal

def module(real, img):
    return (real**2 + img**2)**(1/2)
        
    
#-------------------------------------------------------------- 
'''
def dft(input_signal, N, startFreq, timeInput):
    
    t = np.linspace(0, timeInput, len(input_signal))
    
    freqs = []
    realVector = []
    imaginaryVector = []
    
    for k in range(N):
        cosinus = np.cos(2*np.pi * startFreq * k * t)
        sinus = (-1) * np.sin(2*np.pi * startFreq * k * t)
        
        dotCos = np.dot(input_signal, cosinus)
        dotSin = np.dot(input_signal, sinus)
        
        amplCos = dotCos * 2 / len(input_signal)
        amplSin = dotSin * 2 / len(input_signal)
        
        freqs.append(startFreq * k)
        realVector.append(amplCos)
        imaginaryVector.append(amplSin)        
    
    return (freqs, realVector, imaginaryVector)
'''
    
'''
def idft(freqs, amplR, amplI, time):
    
    signal = np.zeros(1000)
    t = np.linspace(0, time, 1000)
    
    for f, real, img in zip(freqs, amplR, amplI):
        cos = real * np.cos(2*np.pi * f * t)
        sin = -img * np.sin(2*np.pi * f * t)
        signal = signal + cos + sin

    return signal
'''