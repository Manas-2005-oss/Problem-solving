n =int(input("Enter the number: "))
if n % 2 == 0:
    print("Even")
else:
    print("Odd")

"""n=int(input("Enter the number: "))
if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")"""

"""
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
if a>b :

    print("a is greater than b")
else:

    print("b is greater than a")

"""
"""
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
if a>b and a>c:
    print(a," is greater ")
elif b>c and b>a:
    print(b," is greater ")
else:
    print(c," is greater ")"""
'''
list = [1,2,3,4,5,6,7,8,9]
no = int(input("Enter the number: "))
if no in list:
    print("Number is present in the list")
else:    print("Number is not present in the list")'''


# greatest of 4 numbers
'''
a1 = int(input("Enter the first number: "))
a2 = int(input("Enter the second number: "))
a3 = int(input("Enter the third number: "))
a4 = int(input("Enter the fourth number: "))

if (a1> a2 and a1> a3 and a1> a4):
    print(a1," is the greatest number")

elif (a2> a1 and a2> a3 and a2> a4):
    print(a2," is the greatest number")
elif (a3> a1 and a3> a2 and a3> a4):
    print(a3," is the greatest number")
else:
    print(a4," is the greatest number")'''

# find pass or fail
'''
m1 = int(input("Enter marks m1:"))
m2 = int(input("Enter marks m2:"))
m3 = int(input("Enter marks m3:"))

total_percantage = (m1+m2+m3)/300*100

if (total_percantage >=40):
    print("Pass")
else:    
    print("Fail")'''


# detection of spam
'''
p1= "make a lot of money"
p= "but now"
comment = input("Enter a comment:")
if (p1 in comment) or (p in comment):
    print ("This is a spam message")
else:
    print("This is not a spam message")'''


# username less than 10 characters
username = input("Enter the username:")
if (len(username)<10):
    print("username Invalid")
else:
    print("username is valid")
