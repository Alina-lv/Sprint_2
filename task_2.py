class Movies:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)

class Comedy(Movies):
    def add_movie(self, movie):
        super().add_movie(movie)
        movies_list = ', '.join(self.movies)
        return f"Комедии: {movies_list}"

class Drama(Movies):
    def add_movie(self, movie):
        super().add_movie(movie)
        movies_list = ', '.join(self.movies)
        return f"Драмы: {movies_list}"

# Тестирование
comedy = Comedy()
print(comedy.add_movie('Большой куш'))
print(comedy.add_movie('Маска'))

drama = Drama()
print(drama.add_movie('Оружейный барон'))
print(drama.add_movie('Зелёная миля'))
