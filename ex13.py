from sys import argv
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

x = input("Type something now....")
print("You typed this: \n{}\nas an input not as a command-line argument.".format(x))