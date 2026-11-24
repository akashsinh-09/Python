class Movie:

    def __init__(self, movie_name, director, release_year, rating, language):
        self.movie_name = movie_name
        self.director = director
        self.release_year = release_year
        self.rating = rating
        self.language = language

    def display(self):

        print("Movie Name:", self.movie_name)
        print("Director:", self.director)
        print("Release Year:", self.release_year)
        print("Rating:", self.rating)
        print("Language:", self.language)


movie1 = Movie("3 Idiots", "Rajkumar Hirani", 2009, 8.4, "Hindi")
movie2 = Movie("Dangal", "Nitesh Tiwari", 2016, 8.3, "Hindi")
movie3 = Movie("Inception", "Christopher Nolan", 2010, 8.8, "English")
movie4 = Movie("RRR", "S. S. Rajamouli", 2022, 7.8, "Telugu")
movie5 = Movie("Interstellar", "Christopher Nolan", 2014, 8.7, "English")

movie1.display()
print("----------------------")

movie2.display()
print("----------------------")

movie3.display()
print("----------------------")

movie4.display()
print("----------------------")

movie5.display()