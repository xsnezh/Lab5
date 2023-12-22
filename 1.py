"""
Задача 1.

1.	Дано список кортежів, кожен з яких містить два значення:
назва фільму (рядок) і рейтинг (дійсне число). Напишіть функцію(ї)
для сортування кортежів в порядку зростання рейтингу.
Вхідні дані:
Список із кортежів
Вихідні дані:
[('Captain Marvel', 7.0), ('Aladdin', 7.4),
('Toy Story 4', 8.2), ('Avengers: Endgame', 8.7)]

Автор: Новосад Сніжана
"""


def sort_list_last(movies):
    return sorted(movies, key=lambda movie: movie['rating'])

movies = [
    {'title': 'Avengers: Endgame', 'rating': 8.7},
    {'title': 'Aladdin', 'rating': 7.4},
    {'title': 'Toy Story 4', 'rating': 8.2},
    {'title': 'Captain Marvel', 'rating': 7.0}
]

sorted_movies = sort_list_last(movies)

for movie in sorted_movies:
    print(f"{movie['title']}: {movie['rating']}")
