import numpy as np
import math

def triangle_thing(theta, c):
    # convert degrees to radians
    theta_rad = math.radians(theta)

    E = c * math.cos(theta_rad)
    N = c * math.sin(theta_rad)

    return N, E


n, e = triangle_thing(153.371958, 128.5967)
print(f"the delta North is: {e} and the delta East is : {n}")