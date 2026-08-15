# Functions
# def greet_user():
#     print("Hi")
# greet_user()

# passing arguments to functions
# def greet(name,end):
#     print("Good morning," +name )
#     print(end)
# greet("Manas", "Thank you")
# greet("Sai", "Thank you")

# with return statement
# def greet(name,end):
#     print("Good morning," +name )
#     print(end)
#     return "Done executed"

# a = greet("Manas", "Thank you")
# b = greet("Sai", "Thank you")
# print(a)
# print(b)

# default arguments/parameters
# def greet_user(name,end="Thank you"):
#     print("Hi,"+name)
#     print(end)
# greet_user("Manas")
# greet_user("Sai","Have a nice day")

# recurrsion
# def fact(n):
#     if n==0 or n==1:
#         return 1
#     return n * fact (n-1)

# n = int(input("Enter a number:"))
# print(f"Factorial of no {n} is {fact(n)}")


# Greatest of 3 numbers
# def greatest(a,b,c):
#     if a>b and a>c:
#         return a
#     elif b>a and b> c:
#         return b
#     else:
#         return c

# a = int(input("Enter the first no:"))
# b = int(input("Enter the second no:"))
# c = int(input("Enter the Third no:"))
# print(f"The greatest no in {a}, {b}, {c} is {greatest(a,b,c)}")

# celsus to fahrenheit
# c = 5*(f-32)/9

# def c_to_f(f):
#     c = 5*(f-32)/9
#     return c

# f = int(input("Enter the temperature in fahrenheit:"))
# print(c_to_f(f), "°C")

# sum of n natural numbbers 
# def sum(n):
#     if n==1:
#         return 1
#     return sum (n-1)+n


# print(sum(4))

# def pattern(n):
#     if n==0:
#         return
#     print("*"*n)
#     pattern(n-1)

# pattern(5)

# inch to cm 
# def inch_to_cm(inch):
#     return inch *2.54
# inch = int(input("Enter the length in inch:"))
# print(inch_to_cm(inch),"cm")

# multiplication table
def table(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")

table(5)