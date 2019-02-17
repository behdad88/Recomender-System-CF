import math
import operator

from review_data import review_data

#Returning a list of common movies
def get_common_movies(criticA, criticB):
    return [movie for movie in review_data[criticA] if movie in review_data[criticB]]

#Returning a list of reviews of common movies
def get_reviews(criticA, criticB):
    common_movies = get_common_movies(criticA, criticB)
    return [(review_data[criticA][movie], review_data[criticB][movie]) for movie in common_movies]

#Calculating the Euclidean Distance between points
def euclidean_distance(points):
    squared_diffs = [(point[0] - point[1]) ** 2 for point in points]
    summed_squared_diffs = sum(squared_diffs)
    distance = math.sqrt(summed_squared_diffs)
    return distance

#Calculating Similarity between points
def similarity(reviews):
    return 1 / (1 + euclidean_distance(reviews))

#Calculating Similarity Between two Critics Given
def get_critic_similarity(criticA, criticB):
    reviews = get_reviews(criticA, criticB)
    return similarity(reviews)


def recommend_movies(critic, num_suggestions):
    #return a list of tuples of similarity between Critic given and the others
    similarity_scores = [(get_critic_similarity(critic, other), other) for other in review_data if other != critic]

    #Sorting the Highest similarity to Lowest
    similarity_scores.sort()
    similarity_scores.reverse()

    #selecting similarity scores from the highest to number of suggests that has given
    similarity_scores = similarity_scores[0:num_suggestions]

    #making the recommendation for the Critic
    recommendations = {}

    for simularity, other in similarity_scores:
        reviewed = review_data[other]

        for movie in reviewed:
            if movie not in review_data[critic]:
                weight = simularity * reviewed[movie]

                if movie in recommendations:
                    sim, weights = recommendations[movie]
                    recommendations[movie] = (sim + simularity, weights + [weight])
                else:
                    recommendations[movie] = (simularity, [weight])

    for recommendation in recommendations:
        simularity, movie = recommendations[recommendation]
        recommendations[recommendation] = sum(movie) / simularity

    sorted_recommendations = sorted(recommendations.items(), key=operator.itemgetter(1), reverse=True)

    return sorted_recommendations
