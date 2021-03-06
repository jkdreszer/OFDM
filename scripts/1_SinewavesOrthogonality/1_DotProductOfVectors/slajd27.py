import numpy as np
import matplotlib.pyplot as plt


blue = [0.088, 0.088, 0.088, 0.442, 0.530, 0.000, -0.530, -0.442, -0.088, -0.088, -0.088]

greens = [[0.080, 0.080, 0.080, 0.398, 0.477, 0.000, -0.477, -0.398, -0.080, -0.080, -0.080], 
         [0.129, 0.129, 0.129, 0.514, 0.643, 0.000, 0.129, 0.129, 0.129, 0.129, 0.129], 
         [-0.129, -0.129, -0.129, -0.514, -0.643, -0.000, -0.129, -0.129, -0.129, -0.129, -0.129],
         [-0.080, -0.080, -0.080, -0.398, -0.477, -0.000, 0.477, 0.398, 0.080, 0.080, 0.080],
         [0.000, 0.050, 0.000, -0.050, 0.000, 0.050, 0.000, -0.050, 0.000, 0.050, 0.000],
         [0.500, 0.550, 0.500, 0.450, 0.500, 0.550, 0.500, 0.450, 0.500, 0.550, 0.500],
         [0.500, 0.650, 0.500, 0.350, 0.500, 0.650, 0.500, 0.350, 0.500, 0.650, 0.500],
         [-0.500, -0.350, -0.500, -0.650, -0.500, -0.350, -0.500, -0.650, -0.500, -0.350, -0.500]]



for green in greens:
    dot = 0
    for i in range(len(green)):
        dot = dot + (blue[i]*green[i])
    dot = round(dot, 6)
    print(dot)
    