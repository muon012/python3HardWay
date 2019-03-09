e = 0
numbers = []


def call_while(limit: int, increments: int):
	i = 0
	while i < limit:
		print(f"At the top i is {i}")
		numbers.append(i)

		i = i + increments
		print("Numbers now: ", numbers)
		print(f"At the bottom i is {i}")


call_while(20, 2)
print("The numbers: ")

for num in numbers:
	print(num)
print("\n\n")

for i in range(20)[::2]:
	i += 1
	print(i)