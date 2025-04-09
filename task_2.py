class Movies:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)


class Comedy(Movies):
    def add_movie(self, movie):
        self.movies.append(movie)
        return f"Комедии: {self.movies}"


class Drama(Movies):
    def add_movie(self, movie):
        self.movies.append(movie)
        return f"Драмы: {self.movies}"


# Тестирование
comedy_movie = Comedy()
print(comedy_movie.add_movie('Большой куш'))

drama_movie = Drama()
print(drama_movie.add_movie('Оружейный барон'))
