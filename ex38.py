ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
	next_one = more_stuff.pop()
	print("Adding: ", next_one)
	stuff.append(next_one)
	print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[3:5]))


# This is an example the author gave in the book about methods and how they're called.
# In this case python thinks we renamed "self"  to "message" in the class definition.
# Whenever you call a method, it automatically passes the instance as an argument, unless it is a static method.
# So when you call test(), with 'Hello' in it, you are actually passing the arguments: (a, "Hello") to it.
# That's why the error occurs that says: 'test() takes 1 positional argument but 2 were given'
# If you just call a.test() with no arguments, you print the instance itself because we defined it as such in the
# class definition.

class Thing():

	def test(message):
		print(message)


a = Thing()
a.test("Hi")
