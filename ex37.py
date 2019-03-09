# Review symbols

# assert
# The assert statement, not function, tests a condition, and immediately triggers an error if the condition is false.
# You can also add a message if the error is triggered.
# Never type 'assert (2 + 2 == 5, "Houston we've got a problem")' as this is evaluating assert on an non-empty tuple,
# and non-empty tuples are True in python so you're basically doing 'assert True' when you use parentheses, and commas
# inside the parentheses, like that.
x = 0
assert x == 0, "trigger THIS message if the condition is False"


# exec()
# The function exec() takes string, that is python code, and runs it.
exec('print("Hello")')

# float()
# Remember you can use float() function to convert integers, numerical strings, into floating point numbers
print(float(2))
print(float("5"))
