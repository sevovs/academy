import sys

number_of_movies = int(input())
total_rating = 0
max_rating = -sys.maxsize
min_rating = sys.maxsize
movie_max_rating = ""
movie_min_rating = ""
for num in range(1, number_of_movies + 1):
    movie_name = input()
    rating = float(input())
    if rating > max_rating:
        max_rating = rating
        movie_max_rating = movie_name
    if rating < min_rating:
        min_rating = rating
        movie_min_rating = movie_name
    total_rating += rating
total_rating /= number_of_movies
print(f"{movie_max_rating} is with highest rating: {max_rating:.1f}")
print(f"{movie_min_rating} is with lowest rating: {min_rating:.1f}")
print(f"Average rating: {total_rating:.1f}")

