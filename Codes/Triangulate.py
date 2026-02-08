import math

def triangulate_point(p1, brng1, p2, brng2):
    """
    p1, p2: (x, y) coordinates of the known points
    brng1, brng2: Bearings in degrees (clockwise from North)
    """
    x1, y1 = p1
    x2, y2 = p2

    # Convert degrees to radians
    # We adjust the bearing to the Cartesian angle (90 - bearing)
    # A small offset prevents tan(90) or tan(270) from hitting infinity
    def get_slope(bearing):
        angle_rad = math.radians(90 - bearing)
        return math.tan(angle_rad)

    try:
        m1 = get_slope(brng1)
        m2 = get_slope(brng2)

        # If slopes are equal, lines are parallel
        if math.isclose(m1, m2, rel_tol=1e-9):
            return "Lines are parallel; no intersection."

        # Solve for X: x = (y2 - y1 + m1*x1 - m2*x2) / (m1 - m2)
        target_x = (y2 - y1 + m1 * x1 - m2 * x2) / (m1 - m2)
        
        # Solve for Y using the first line equation
        target_y = y1 + m1 * (target_x - x1)

        return (round(target_x, 4), round(target_y, 4))

    except ZeroDivisionError:
        return "Calculation error (possibly vertical lines)."

# Example:
# Point A at (0,0) looking NE (45 deg)
# Point B at (10,0) looking NW (315 deg)
result = triangulate_point((-1642065.46956152, -3665023.83659307), 246.102478, (-1642342.59895136, -3664684.65195924), 139.361144+180)
print(f"Intersection: {result}")