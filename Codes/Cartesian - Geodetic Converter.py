import math

def ecef_to_geodetic(x, y, z):
    # WGS84 ellipsoid constants
    a = 6378137.0                # Semi-major axis
    e2 = 0.00669437999014        # Square of first eccentricity
    precision = 1e-12            # Convergence threshold

    # 1. Compute Longitude
    # atan2 is used to correctly handle all four quadrants
    lambda_rad = math.atan2(y, x)
    
    # 2. Compute Preliminary Values
    p = math.sqrt(x**2 + y**2)
    
    # Initial guess for latitude (phi_0)
    phi_prev = math.atan2(z, (1 - e2) * p)
    
    # 3. Iterate To Compute Latitude and Height
    # We loop until the change in latitude is smaller than our precision
    while True:
        sin_phi = math.sin(phi_prev)
        cos_phi = math.cos(phi_prev)
        
        # Radius of curvature in the prime vertical
        N_i = a / math.sqrt(1 - e2 * sin_phi**2)
        
        # Compute height
        h_i = (p / cos_phi) - N_i
        
        # Compute new latitude using the specific iterative formula
        phi_i = math.atan2(z, (1 - e2 * (N_i / (N_i + h_i))) * p)
        
        # Check for convergence
        if abs(phi_i - phi_prev) < precision:
            phi_final = phi_i
            h_final = h_i
            break
            
        phi_prev = phi_i

    # Convert radians to degrees for readability
    latitude = math.degrees(phi_final)
    longitude = math.degrees(lambda_rad)
    
    return latitude, longitude, h_final

x_test, y_test, z_test = -1641950.82390876, -3665089.36276137, 4939785.8960614605
lat, lon, alt = ecef_to_geodetic(x_test, y_test, z_test)

print(f"Results:\nLatitude: {lat:.6f}°\nLongitude: {lon:.6f}°\nHeight: {alt:.3f} m")