# Animal is-a object. Animal inherits from the class Object of python
class Animal(object):

	def print_classification(self, classification):
		print("This animal is a member of the {} family".format(classification))


# class Dog is-a Animal
class Dog(Animal):

	def __init__(self, name):
		# Dog has-a __init__ function with self, name as params
		self.name = name

	def bark(self):
		print("Woof")


# class Cat is-a Animal
class Cat(Animal):

	def __init__(self, name):
		# Cat has-a __init__ function with self, name as params
		self.name = name

	def meow(self):
		print("meow")


class Person(object):

	def __init__(self, name):
		self.name = name
		# Person has-a pet of some kind
		self.pet = None

	def greet(self, greeting):
		print(greeting)


# Employee is-a Person
class Employee(Person):

	def __init__(self, name, salary):
		# ?? what is this strange music?
		super(Employee, self).__init__(name)
		self.salary = salary

	def increase_salary(self):
		self.salary += 1000
		print("This employee's salary is now: {}".format(self.salary))


class Fish(object):

	def __init__(self, name, size, water_type):
		self.name = name
		self.size = size
		self.water_type = water_type


class Salmon(Fish):

	def print_type(self):
		print("This Salmon is of {} water.".format(self.water_type))


class Halibut(Fish):

	def print_type(self):
		print("This Halibut is of {} water.".format(self.water_type))


rover = Dog("Rover")

satan = Cat("Satan")

mary = Person("Mary")

mary.pet = satan

frank = Employee("Frank", 120000)

frank.pet = rover

flipper = Fish("Flipper", 12, "fresh")

crouse = Salmon("Crouse", 23, "Salt")

harry = Halibut("Harry", 8, "salt")

# Calling a method from the parent function Animal in the Dog instance:
rover.print_classification("Vertebrate")

# These next 2 lines are the same.
rover.bark()
Dog.bark(rover)

frank.salary = 1000
print(frank.salary)
frank.increase_salary()

# Using a class like an object?
Dog.bark(Animal)
