import numpy as np

esq = 0.00669437999014      # square of ecentricity
a = 6378137.0               # semi-major axis

def C_to_G (x, y, z, accuracy = 1e-20):
    # Compute longitude (arctan2 for quadrants)
    long = np.arctan2(y, x)

    # Compute preliminary values
    p = np.sqrt(x**2 + y**2)
    phi = np.arctan(z/((1- esq)*p))
    h = 0

    # Iterate to compute latitude and height
    not_accurate = 1.0
    while not_accurate > accuracy:
        # rphi represents the replaced phi value in the loop
        rphi = phi

        # Ni calculation
        N = a/(np.sqrt(1-esq*np.sin(rphi)**2))

        # Hi calculation
        h = p/(np.cos(rphi)) - N

        # Phii calculation
        placeholder = 1-esq*(N/(N+h))
        phi = np.arctan(z/(placeholder*p))

        dphi = abs(rphi-phi)
    return np.degrees(dphi), np.degrees(long), h

def G_to_C (lat_degree, long_degree, h):
    # Convert degree -> radians
    lat = np.radians(lat_degree)
    long = np.radians(long_degree)

    # Calculate N
    N = a/np.sqrt(1-esq*(np.sin(lat))**2)
    
    # Calculate x, y, z
    x = (N+h)*np.cos(lat)*np.cos(long)
    y = (N+h)*np.cos(lat)*np.sin(long)
    z = ((1-esq)*N+h)*np.sin(lat)

    return x, y, z

# obtain user inputs and execute functions
print("MENU")
print("1. Cartesian(x, y, z) -> Geodetic(latitude, longitude, height)")
print("2. Geodetic(latitude, longitude, height) -> Cartesian(x, y, z)")
user_choice = input("Enter an option: 1 or 2 ->")

# Case where user wants to convert cartesian to geodetic
if user_choice == '1':
    x = float(input("Enter X (m): "))
    y = float(input("Enter Y (m): "))
    z = float(input("Enter Z (m): "))
    lat, lon, alt = C_to_G(x, y, z)
    print(f"\nCartesian -> Geodetic:")
    print(f"Latitude:  {lat}°")
    print(f"Longitude: {lon}°")
    print(f"Height:    {alt}m")

# Case where user wants to convert geodetic to cartesian
elif user_choice == '2':
    lat = float(input("Enter Latitude (degrees): "))
    lon = float(input("Enter Longitude (degrees): "))
    h = float(input("Enter Height (meters): "))
    x, y, z = G_to_C(lat, lon, h)
    print(f"\nGeodetic -> Cartesian:")
    print(f"X: {x} m")
    print(f"Y: {y} m")
    print(f"Z: {z} m")

# Case where the user input is invalid
else:
    print("Invalid input! The only options are 1 or 2. Please restart the program")