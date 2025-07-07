
from abc import ABC, abstractmethod #required modules ABC :- base class for defining abstract class
									#@abstractmethod:- to declare the method as abstract 
"""1. Create an abstract class with abstract and non-abstract methods. """
class Shape(ABC):
    
    @abstractmethod
    def area(self):
        """Abstract method - must be implemented by subclass"""
        pass

    @abstractmethod
    def perimeter(self):
        """Another abstract method"""
        pass

    def describe(self):
        """Concrete method - optional override by class"""
        return "This is a 2D shape."
    def colour(self):
        """This method should be implemented or overridden"""
        pass
		
""" Now Shape is abstract class. Cannot implement directly/ consider abstract is parent
Any subclass must implement abstract methods.
decribe() is regular method"""


class Rectangle(Shape):
    def __init__(self, length, width,color):
        self.length = length
        self.width = width
        self.color  = color

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)
        
    def colour(self):
        return f"The shape is in {self.color} color"

		
        
rect = Rectangle(10,5,"white")
print(rect.area())
print(rect.perimeter())
print(rect.describe())
#shape = Shape() #Raises Type Error

sqr = Rectangle(10,10,"Blue")
print(sqr.area())
print(sqr.colour())

#---------------------------------------------------------------------------------------
"""2. Create a sub class for an abstract class. Create an object in the child class for the  
abstract class and access the non-abstract methods """

class Animals(ABC):
    
    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def food_type(self):
        pass

    def domestic_wild(self):
        pass


class Wild(Animals):
    def __init__(self,type_):
        self.type_ = type_
		
    def sound(self):
        return "A Sound is declared in instance"

    def food_type(self):
        return "food type is declared in instance"

    def describe(self):
        return f"Yes, it's a {self.type_} animal"

    def domestic_wild(self):
        return self.describe()


class Animal(Animals):
    def __init__(self,name,sound_,food_type_,type_):
        self.name = name
        self.sound_ = sound_
        self.food_type_ = food_type_
        self.wild = Wild(type_)  # using Wild class which inherits Animal

    def sound(self):
        return f"The {self.name} sounds like {self.sound_}."

    def food_type(self):
        return f"It eats {self.food_type_}."

    def domestic_wild(self):
        return self.wild.describe()

print("\n\n")
# 🔍 Test the Animal
lion = Animal("lion","growls","meat","wild")
print(lion.sound())
print(lion.food_type())
print(lion.domestic_wild())

print("\n")
dog = Animal("dog","bow-bow","veg and non-veg","pet")
print(dog.sound())
print(dog.food_type())
print(dog.domestic_wild())


"""3. Create an instance for the child class in child class and call abstract methods """
"""4. Create an instance for the child class in child class and call non-abstract methods """
class Dog(Animal):
    def sound(self):
        return "Bark"

    def food_type(self):
        return "Kibble"

class DogTrainer(Animal):
    def __init__(self):
        self.dog = Dog()  # Instantiating a child class inside another child class

    def sound(self):
        return self.dog.sound()  # Calling abstract method from inner instance

    def food_type(self):
        return self.dog.food_type()  # Same here

    def show_behavior(self):
        print(self.dog.sound())       # Abstract method from Dog
        print(self.dog.food_type())   # Abstract method from Dog
        print(self.dog.sleep())       # Non-abstract method from Animal

trainer = DogTrainer()
trainer.show_behavior()
