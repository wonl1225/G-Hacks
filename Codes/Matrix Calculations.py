import numpy as np
import math

def triangle_thing(theta, c):
    # convert degrees to radians
    theta_rad = math.radians(theta)

    N = c * math.cos(theta_rad)
    E = c * math.sin(theta_rad)

    return N, E


x, y = triangle_thing(36.87, 5)
print(f"{x} haha {y}")