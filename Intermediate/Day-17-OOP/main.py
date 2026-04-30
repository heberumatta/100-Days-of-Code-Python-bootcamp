class Dog:
    pass
#Here we use PascalCase for class name and snake_case for all other variables and functions. This is a convention in Python.
#now we can create an instance of the Dog class. An instance is an individual object of a class.
#We can create multiple instances of the same class, each with its own unique properties and behaviors.

my_dog = Dog()
my_dog.name = "Buddy"
my_dog.age = 3

#But if we want to create multiple dogs, we would have to repeat the same code for each dog, which is not efficient.
#To avoid this, we can define a constructor method in the Dog class that initializes the properties. 
#A constructor is a special method that is called when an instance of the class is created. In Python, the constructor method is defined using the __init__ method.
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

#Now we can create multiple instances of the Dog class without repeating the code for each dog.
my_dog = Dog("Buddy", 3)
your_dog = Dog("Max", 5)
