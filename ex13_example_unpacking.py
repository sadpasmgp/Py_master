from sys import argv

script, x = argv
x = int(x) # argv values are strings by default so we convert them to int values
a = int(input("Enter a base to calculate the exponential values:"))
print("""Exponential value of user provided value
to the power of command line values is: """)
print(a**x)
