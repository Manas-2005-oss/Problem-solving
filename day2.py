# # problem1
# n =int(input("Enter the number:"))
# if n % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# # problem2
# n=int(input("Enter the number: "))
# if n > 0:
#     print("Positive")
# elif n < 0:
#     print("Negative")
# else:
#     print("Zero")

# # problem3
# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
# if a>b:
#     print("a is greater than b")
# elif a==b:
#     print("Both are equal")
# else:
#     print("b is greater than a")

# # # problem4
# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
# if a<b:
#     print("a is lesser than b")
# elif a==b:
#     print("Both are equal")
# else:
#     print("b is lesser than a")


# # problem5
# age = int(input("Enter your age:"))
# if(age>=18):
#     print("eligible for vote")
# else:
#     print("not eligible for vote")

# # problem6
# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
# c = int(input("Enter the third number: "))
# if a>b and a>c:
#     print(a," is greater ")  
# elif b>c and b>a:
#     print(b," is greater ")
# elif c>a and c>b:
#     print(c," is greater ")
# elif(a==b and a>c):
#     print("a and b are equal and greater than c")
# elif(a==c and a>b):
#     print("a and c are equal and greater than b")
# elif(b==c and b>a):
#     print("b and c are equal and greater than a")
# else:
#     print("all are equal")


# # problem7
# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
# c = int(input("Enter the third number: "))
# if a<b and a<c:
#     print(a," is lesser ")
# elif b<c and b<a:
#     print(b," is lesser ")
# elif c<a and c<b:
#     print(c," is lesser ")
# elif(a==b and a<c):
#     print("a and b are equal and lesser than c")
# elif(c==b and c<a):
#     print("c and b are equal and lesser than a")
# elif(a==c and a<b):
#     print("a and c are equal and lesser than b")

# # problem8
# year = int(input("Enter a year:"))
# if year % 4 == 0 and year % 100 !=0 or year % 400 == 0 :
#     print("It is a leap year")
# else:
#     print("It is not a leap year")

# # problem9
# word = (input("Enter a letter:"))
# if word in ("a", "e", "i", "o", "u"):
#     print("It is a vowel")
# else:
#     print("It is a consonant")

# # problem10
# n = int(input("Enter a no:"))
# if n % 5 == 0 and n % 11 == 0:
#     print("It is divisible by both 5 and 11")
# else:
#     print("It is not divisible by 5 and 11")

# problem12
# angle1 = int(input("Enter the first angle: "))
# angle2 = int(input("Enter the second angle: "))
# angle3 = int(input("Enter the third angle: "))
# if (angle1 + angle2 + angle3 ==180) and (angle1>0 and angle2>0 and angle3>0):
#     print(f"the sum is {angle1+angle2+angle3} and it can form triangle")
# else:
#     print(f"the sum is {angle1+angle2+angle3} and cannot form triangle")





# problem11
a = int(input("Enter the number: "))
b = int(input("Enter the number: "))
c = int(input("Enter the number: "))
if (a<b and a>c) or (a>b and a<c):
    print("a is the second largest number")
elif(b>a and b<c) or (b<a and b>c):
    print("b is the second largest number")
elif(c>a and c<b) or (c<a and c>b):
    print("c is the second largest number")