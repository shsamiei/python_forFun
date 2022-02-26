class Movie:
    def __init__(self, name, release_year):
        self.name = name
        self.release_year = release_year

    def __str__(self) :
        return self.name

    def __lt__(self, other_object):
        return self.release_year < other_object.release_year 


movie = Movie('122 angry man' , 1997)

# checking Dunder(magic) methods

# __str__ : 
 
#when we call print the __str__ method will call 

# print(movie.__str__)
# print(str(movie))
# print(movie)


# __it__ : 


hungergame = Movie('hungergame' , 2009)
se7en = Movie('se7en' , 1995)

print(se7en.__lt__(hungergame))

print(se7en > hungergame)

# we have some other methods for operator overloading 
# __lt__  for :    a < b
# __gt__  for :    a > b
# __le__  for :    a <= b
# __ge__  for :    a >= b
# __eq__  for :    a == b
# __ne__  for :    a != b 
