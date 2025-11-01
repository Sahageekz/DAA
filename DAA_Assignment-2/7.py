#Implement closest pair algorithm using divide and conquer
import math

def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def brute_force(points):
    min_d = float('inf')
    pair = None
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            d = dist(points[i], points[j])
            if d < min_d:
                min_d = d
                pair = (points[i], points[j])
    return min_d, pair

def closest_pair(points):
    if len(points) <= 3:
        return brute_force(points)
    mid = len(points) // 2
    left = points[:mid]
    right = points[mid:]
    d1, p1 = closest_pair(left)
    d2, p2 = closest_pair(right)
    d = min(d1, d2)
    pair = p1 if d == d1 else p2

    mid_x = points[mid][0]
    strip = [p for p in points if abs(p[0] - mid_x) < d]
    strip.sort(key=lambda x: x[1])

    for i in range(len(strip)):
        for j in range(i + 1, min(i + 7, len(strip))):
            dist_strip = dist(strip[i], strip[j])
            if dist_strip < d:
                d = dist_strip
                pair = (strip[i], strip[j])
    return d, pair

points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
points.sort()
distance, closest = closest_pair(points)
print("Closest Pair:", closest)
print("Distance:", distance)
