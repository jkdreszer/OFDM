import numpy as np
import matplotlib.pyplot as plt
pi = np.pi

# PARAMS
TIME_VECTOR_SIZE = 15

AMP_A = 1
AMP_B = 2

# CALCULATIONS
t = np.linspace(0, 2*pi,TIME_VECTOR_SIZE, endpoint=False)

Sin_A = AMP_A * np.sin(t)
Sin_B = AMP_B * np.sin(t)
dot = np.dot(Sin_A,Sin_B)
amp_B = dot * 2 / TIME_VECTOR_SIZE / AMP_A

# PRESENTATION
print(f'AMP_A = {AMP_A}')
print(f'AMP_B = {AMP_B}')
print(f'dot = {dot:0.2f}')
print(f'Measured AMP_B= {amp_B:0.2f}')
