import numpy as np

esq = 0.00669437999014      # square of ecentricity
a = 6378137.0               # semi-major axis

def C_to_G (x, y, z, accuracy = 1e-20):
    # Compute longitude (arctan2 for quadrants)
    long = np.arctan2(y, x)

    # Compute preliminary values
    p = np.sqrt(x**2 + y**2)
    phi = np.artan(z/((1- esq)*p))
    h = 0

    # Iterate to compute latitude and height
    not_accurate = 1
    while not_accurate < accuracy:
        # rphi represents the replaced phi value in the loop
        rphi = phi

        # Ni calculation
        N = a/(np.sqrt(1-esq*np.sin(rphi)**2))

        # Hi calculation
        h = p/(np.cos(rphi)) - N

        # Phii calculation
        placeholder = 1-esq*(N/(N+h))
        phii = np.arctan(z/placeholder*p)

        dphi = abs(rphi-phi)
    return np.degrees(dphi), np.degrees(long), h

def G_to_C (lat_degree, long_degree, h):
    # Convert degree -> radians
    lat = np.radians(lat_degree)
    long = np.radians(long_degree)

    # Calculate N
    N = a/np.sqrt(1-esq*2*(np.sin(lat))**2)
    
    # Calculate x, y, z
    x = (N+h)*np.cos(lat)*np.cos(long)
    y = (N+h)*np.cos(lat)*np.sin(long)
    z = ((1-esq)*N+h)*np.sin(lat)

    return x, y, z