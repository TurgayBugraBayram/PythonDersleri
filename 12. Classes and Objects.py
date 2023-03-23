"""
Python is an object-oriented programming language, which means that it supports the creation and manipulation of objects.
An object is an instance of a class, and a class is a blueprint for creating objects. Classes can have attributes (data) and methods (functions),
and can be used to represent real-world concepts or entities in code.
Here's an example of a simple class in Python:
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello, my name is {self.name} and I'm {self.age} years old.")


person1 = Person("Alice", 30)
person1.say_hello()

"""
Iterators:
In Python, an iterator is an object that implements the iterator protocol, which consists of the iter and next methods. 
The iter method returns the iterator object itself, and the next method returns the next value from the iterator. 
Here's an example of an iterator in Python:
"""
class MyIterator:
    def __init__(self, data):
        self.index = 0
        self.data = data

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value

data = [1, 2, 3, 4, 5]
my_iterator = MyIterator(data)
for value in my_iterator:
    print(value)

"""
Inheritance:
Inheritance is a feature of object-oriented programming that allows one class to inherit properties and methods from another class. 
The class that inherits properties and methods is called the "subclass",and the class that is being inherited from is called the "superclass". 
Here's an example of inheritance in Python
"""
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

dog = Dog("Fido")
dog.make_sound()

cat = Cat("Whiskers")
cat.make_sound()
