import numpy as np

def get_transformation_params(p1_leg, p1_curr, p2_leg, p2_curr):
    # Setup system of equations: Ax = B
    # x = [a, b, Te, Tn] where a = s*cos(theta), b = s*sin(theta)
    A = np.array([
        [p1_leg[0], -p1_leg[1], 1, 0],
        [p1_leg[1],  p1_leg[0], 0, 1],
        [p2_leg[0], -p2_leg[1], 1, 0],
        [p2_leg[1],  p2_leg[0], 0, 1]
    ])
    B = np.array([p1_curr[0], p1_curr[1], p2_curr[0], p2_curr[1]])
    
    a, b, Te, Tn = np.linalg.solve(A, B)
    
    scale = np.sqrt(a**2 + b**2)
    theta = np.degrees(np.arctan2(b, a))
    
    return a, b, Te, Tn, scale, theta

st1_leg = (150, 225)
st1_curr = (123.2447, 489.4949)
st2_leg = (450, 600)
st2_curr = (170.0614, 1063.8712)

# Solve parameters
a, b, Te, Tn, s, angle = get_transformation_params(st1_leg, st1_curr, st2_leg, st2_curr)

# Legacy offset E to F
de_leg, dn_leg, dh_leg = 33.6304, -151.2606, -3.6288

# Transform offset (vector)
de_curr = a * de_leg - b * dn_leg
dn_curr = b * de_leg + a * dn_leg

print(f"--- Transformation Parameters ---")
print(f"Scale: {s:.4f} | Rotation: {angle:.2f}°")
print(f"Translation: E={Te:.4f}, N={Tn:.4f}\n")
print(f"--- Transformed Offset (E to F) ---")
print(f"ΔE: {de_curr:.4f} m")
print(f"ΔN: {dn_curr:.4f} m")
print(f"ΔH: {dh_leg:.4f} m")