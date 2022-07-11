import numpy as np
from lib import rotate_vector

green = [0,1]
blue =[0,1]

for d in range(0, 370, 10):
    blue= rotate_vector(blue, d)
    dot = np.dot(green, blue)
    print("{:3d}: {:.4f}".format(d, dot))
