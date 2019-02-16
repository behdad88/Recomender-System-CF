import math

# points are pair of tuples
def euclidean_distance(points):
    squared_diffs = [(point[0] - point[1]) ** 2 for point in points]
    summed_squared_diffs = sum(squared_diffs)
    distance = math.sqrt(summed_squared_diffs)
    return distance
