def circumcenter(point1, point2, point3):
    ax, ay = point1
    bx, by = point2
    cx, cy = point3
    d = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
    if (d == 0): return (50.0,50.0) # The three points were colineal, therefore the heuristic is not applicable
    ux = ((ax * ax + ay * ay) * (by - cy) + (bx * bx + by * by) * (cy - ay) + (cx * cx + cy * cy) * (ay - by)) / d
    uy = ((ax * ax + ay * ay) * (cx - bx) + (bx * bx + by * by) * (ax - cx) + (cx * cx + cy * cy) * (bx - ax)) / d
    return (ux, uy)


