# INHERITANCE vs COMPOSITION

# =========================================== INHERITANCE ===========================================
# Implicit Inheritance
# The child class inherits and uses methods from the Parent class even though they're not defined in the Child class.
class Parent(object):

	def implicit(self):
		print("PARENT implicit()")


class Child(Parent):
	pass


dad = Parent()
son = Child()

dad.implicit()
son.implicit()
print("+" * 20)

# Override Explicitly
# The child overrides a method inherited from the Parent class by defining it inside itself(Child class).
class Parent(object):

	def override(self):
		print("PARENT override()")


class Child(Parent):

	def override(self):
		print("CHILD override()")


dad = Parent()
son = Child()

dad.override()
son.override()
print("+" * 20)


# Alter Before or After
# Using super()
class Parent(object):

	def altered(self):
		print("PARENT altered()")


class Child(Parent):

	def altered(self):
		print("CHILD before PARENT altered()")
		super(Child, self).altered()
		print("CHILD after PARENT altered()")


dad = Parent()
son = Child()

dad.altered()
son.altered()

# -------------- super() BEST PRACTICE ------------------
# super() enables you to access the methods and members of a parent class without referring to the parent class by name.
# For a single inheritance situation the first argument to super() should be the name of the current child class
# calling super(), and the second argument should be self, that is, a reference to the current object calling super().


# =========================================== COMPOSITION ===========================================
class Other(object):

	def override(self):
		print("OTHER override()")

	def implicit(self):
		print("OTHER implicit()")

	def altered(self):
		print("OTHER altered()")


class Child(object):

	def __init__(self):
		self.other = Other()

	# Remember that 'sef.other' is now a class, so we are using another class here and calling its implicit method.
	def implicit(self):
		self.other.implicit()

	def override(self):
		print("CHILD override()")

	def altered(self):
		print("CHILD before OTHER altered()")
		self.other.altered()
		print("CHILD after OTHER altered()")


son = Child()

print("\nCOMPOSITION\n")
son.implicit()
son.override()
son.altered()