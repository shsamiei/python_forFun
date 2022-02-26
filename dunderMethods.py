class Movie:
    def __init__(self, name, release_year):
        self.name = name
        self.release_year = release_year

    def __str__(self) :
        return self.name



movie = Movie('122 angry man' , 1997)

#when we call print the __str__ method will call 

print(movie.__str__)
print(str(movie))
print(movie)



