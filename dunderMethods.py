class Movie:
    def __init__(self, name, release_year):
        self.name = name
        self.release_year = release_year

    def __str__(self) :
        return self.name

    def __lt__(self, other_object):
        return self.release_year < other_object.release_year 

    def __call__(self) :
        return "say hello to my dear friend ! "

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


scarface = Movie('scarface' , 2013)
#scarface()
# we will have : 
# TypeError: 'Movie' object is not callable
# how to make it callable ? : 

# __cal__ :

#after adding __cal__ : 
print(scarface())
print(scarface.__call__())


# lets go for more usable Dunder methods : 


class FootballTeam:
    def __init__(self, name, cups_number):
        self.name = name
        self.cups_number = cups_number

    def __add__(self, other_object):
        return self.cups_number + other_object.cups_number

    
ss = FootballTeam('Esteghlal' , 20)
loung = FootballTeam('pirouzi' , 17)

print(ss + loung)
print(ss.__add__(loung))

# a + b	                    __add__
# تفریق	a - b	              __sub__
# ضرب	a * b	            __mul__
# تقسیم اعشاری	a / b	     __truediv__
# تقسیم صحیح	a // b  	__floordiv__
# باقی‌مانده	a % b	         __mod__
# توان	a ** b             	  __pow__
# شیفت چپ	a << b	        __lshift__
# شیفت راست	a >> b	        __rshift__
# AND	a & b	            __and__
# OR	a ا b	             __or__
# XOR	a ^ b	            __xor__
# NOT	~a	               __invert__


# another one : __len__ , __iter__ , __next__ 


