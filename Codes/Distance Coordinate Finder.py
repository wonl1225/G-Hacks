import math

def find_viable_points(p1, dist_a, p2, dist_b):
    x1, y1 = p1
    x2, y2 = p2
    
    # Distance between the two centers
    dx, dy = x2 - x1, y2 - y1
    d = math.sqrt(dx**2 + dy**2)
    
    # Check if a solution is physically possible
    if d > (dist_a + dist_b):
        return "Too far apart: No overlap."
    if d < abs(dist_a - dist_b):
        return "Too close: One point is inside the other's radius without touching."
    if d == 0:
        return "Points are identical: No unique intersection."

    # Solve for the intersection points
    # d1 is the distance from p1 to the point where the intersection line crosses the center line
    d1 = (dist_a**2 - dist_b**2 + d**2) / (2 * d)
    
    # h is the perpendicular distance from the center line to the intersection points
    h = math.sqrt(max(0, dist_a**2 - d1**2))
    
    # The point on the line between centers
    x_mid = x1 + (d1 * dx / d)
    y_mid = y1 + (d1 * dy / d)
    
    # The offsets for the two points
    rx = -dy * (h / d)
    ry = dx * (h / d)
    
    intersection_1 = (round(x_mid + rx, 3), round(y_mid + ry, 3))
    intersection_2 = (round(x_mid - rx, 3), round(y_mid - ry, 3))
    
    return list(set([intersection_1, intersection_2]))

# Example: Point A at (0,0) dist 10, Point B at (12,0) dist 4
results = find_viable_points((-78.52759564000002, -234.15663522), 126.6901, (15.35086781, -131.41616198), 168.5144)
print(f"The viable points are: {results}")