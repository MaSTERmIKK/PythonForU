# Python program showing
# abstract base class work
 
from abc import ABC, abstractmethod
 
class Polygon(ABC):
 
    @abstractmethod
    def noofsides(self):
        pass
 
class Triangle(Polygon):
 
    # overriding abstract method
    def noofsides(self):
        print("I have 3 sides")
 
class Pentagon(Polygon):
 
    # overriding abstract method
    def noofsides(self):
        print("I have 5 sides")
 
class Hexagon(Polygon):
 
    # overriding abstract method
    def noofsides(self):
        print("I have 6 sides")
 
class Quadrilateral(Polygon):
 
    # overriding abstract method
    def noofsides(self):
        print("I have 4 sides")
 
# Driver code
R = Triangle()
R.noofsides()
 
K = Quadrilateral()
K.noofsides()
 
R = Pentagon()
R.noofsides()
 
K = Hexagon()
K.noofsides()









# Python program showing
# abstract base class work
 
from abc import ABC, abstractmethod
class Animal(ABC):
 
    def move(self):
        pass
 
class Human(Animal):
 
    def move(self):
        print("I can walk and run")
 
class Snake(Animal):
 
    def move(self):
        print("I can crawl")
 
class Dog(Animal):
 
    def move(self):
        print("I can bark")
 
class Lion(Animal):
 
    def move(self):
        print("I can roar")
         
# Driver code
R = Human()
R.move()
 
K = Snake()
K.move()
 
R = Dog()
R.move()
 
K = Lion()
K.move()