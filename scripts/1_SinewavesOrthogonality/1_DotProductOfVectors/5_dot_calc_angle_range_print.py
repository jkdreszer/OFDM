import numpy as np
from lib import rotate_vector

green = [0,1]
blue =[0,1]

for degree in range(0, 370, 10):
    blue= rotate_vector(blue, degree)
    dot = np.dot(green, blue)
    print(f"{degree:03d}: {dot:+0.3f}")
