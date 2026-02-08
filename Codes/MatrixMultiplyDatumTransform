import numpy as np
import math

# Use a conversion factor for milliarcseconds to radians
# (val / 1000) to get arcseconds, / 3600 to get degrees, then to radians
mas_to_rad = (math.pi / 180) / (3600 * 1000)

t = 29 # Years since epoch
rx = (-25.91467 - 0.06667 * t) * mas_to_rad
ry = (-9.42645 + 0.75744 * t) * mas_to_rad
rz = (-11.59935 + 0.05133 * t) * mas_to_rad

# Translation in meters
tx = 0.99503 + 0.00079 * t
ty = -1.90141 - 0.0006 * t
tz = -0.52285 - 0.00144 * t
translation_array = np.array([[tx], [ty], [tz]])

# Scale (assuming input is ppb)
scale_val = (1.30504 - 0.072 * t) * 1e-9
multiplier = 1 + scale_val

# Coordinate Frame Rotation Matrix (verify if you need Position Vector instead!)
rotation_matrix = np.array([
    [1, -rz, ry],
    [rz, 1, -rx],
    [-ry, rx, 1]
])

starting_array = np.array([[-1641894.2117584937], [-3664915.841055974], [4939937.420870818]])

# Apply transformation
output_array = translation_array + multiplier * (np.matmul(rotation_matrix, starting_array))

print(output_array)