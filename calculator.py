from math import * 

def Multiplication(x, y):
  return x * y

def Addition(a, b):
  return  a + b

def Subtraction(c, d):
  return c - d

a = 10
b = 5


sum = Addition(a, b)
print(f"The sum of {a} and {b} is: {sum}")

sub = Subtraction(a, b)
print(f"The difference between {a} and {b} is: {sub}")

mul = Multiplication(a, b)
print(f"The product of {a} and {b} is: {mul}")