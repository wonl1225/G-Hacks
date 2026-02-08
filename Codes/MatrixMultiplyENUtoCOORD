import numpy as np
import math as math

p = float(input('LATITUDE'))
l = float(input('LONGITUDE'))

x = float(input('E'))
y = float(input('N'))
z = float(input('U'))

lat  = math.radians(p)
lon = math.radians(l)

sphi = math.sin(lat)
cphi = math.cos(lat)
slam = math.sin(lon)
clam = math.cos(lon)

array1 = np.array([[x],[y],[z]])
array2 = np.array([[-sphi*clam, -sphi*slam, cphi],[-slam,clam, 0],[cphi*clam,cphi*slam,sphi]])
array3 = np.transpose(array2)

final = np.matmul(array3, array1)

print(final)