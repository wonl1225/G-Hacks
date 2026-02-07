import numpy as np
import math

e = np.e

def C_to_G (x, y, z):
    # Compute Longitude
    long = np.arctan(y/x)

    # Compute Preliminary Values
    p = np.sqrt(x^2 + y^2)
    phi = np.artan(z/(1- e**2*p))

    # Iterate to compute latitude and height
    Ni = a/(np.sqrt(1-e**2*np.sin()**2))

    
    return

def G_to_C ():
    return