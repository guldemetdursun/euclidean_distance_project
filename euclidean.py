import math

def euclidean_distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

points = [(1, 2), (2, 3),(7, 8), (9, 10), (4, 6), (8, 9)]
min_distance = float('inf')
p1, p2 = None, None

for a in points:
    for b in points:
        if a != b:
            dist = euclidean_distance(a, b)
            if dist < min_distance:
                min_distance = dist
                p1, p2 = a, b

print("Minimum distance:", min_distance, "between", p1, "and", p2)