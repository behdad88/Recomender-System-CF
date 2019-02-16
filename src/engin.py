import math

Coppola_Brando = [(5.0,5.0),(5.0,4.29)]
Coppola_Dreyfuss = [(5.0, 1.07), (5.0, 0.63)]
Really_liked = [(5.0,5.0),(5.0,5.0)]

# points are pair of tuples
def euclidean_distance(points):
    squared_diffs = [(point[0] - point[1]) ** 2 for point in points]
    summed_squared_diffs = sum(squared_diffs)
    distance = math.sqrt(summed_squared_diffs)
    return distance

def similarity(points):
    return 1/(1 + euclidean_distance(points))