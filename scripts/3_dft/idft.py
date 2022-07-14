# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 15:40:32 2022

@author: dreszer
"""
import numpy as np
import matplotlib.pyplot as plt
import lib


#Parameters
time = 3

#Loading data and cutting mirror reflections
freqs = np.load("freqs.npy")[:9:] #final index depends on size of DFT
reals = np.load("reals.npy")[:9:]
imgs = np.load("imgs.npy")[:9:]

#IDFT
signal = lib.idft(freqs, reals, imgs, 3)

#Plotting
t = np.linspace(0, time, 1000)

plt.plot(t, signal, '-')
plt.xlabel("Time [s]")
plt.show()
