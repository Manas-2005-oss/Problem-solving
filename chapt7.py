# loops
i= 1
while (i<51):
    print(i)
    i += 1 

for i in range(1,51):
    print(i)
    
#  list printing

l1 =[1,2,"manas","manas","lokesh","sai","rohit",8,9]
i = 0
while (i < len(l1)):
    print(l1[i])
    i += 1

l1 =(1,2,"manas","manas","lokesh","sai","rohit",8,9)
for item in l1:
    print(item)

# break statement
for i in range(1,50,2):
    if i ==25:
        break
    print(i)
     
# continue statement
for i in range(1,50):
    if i ==25:
        continue
    print(i)

# pass statement
for i in range (0,10):
    pass

# i=0 
# while(i<10):
#     print(i)
#     i+=1

# any = int(input("enter the number"))
# for i in range (1,11):
#     print(f"{any} x {i} = {any*i}")
# l = ["Manas","Rohit","Man","Lokesh","sai"]
# for i in l:
#     if i.startswith("M"):
#         print(i)

# any = int(input("enter the number"))
# i=1
# while (i<11):
#     print(f"{any} x {i} = {any*i}")
#     i+=1
  
# n = int(input("Enter the number: "))
# i= 1
# sum =0 
# while (i<=n):
#     sum +=i
#     i+=1
# print(sum)

# factorial
# n= int(input("Enter the number: "))
# fact = 1
# for i in range (1,n+1):
#     fact = fact *i
# print(f"Factorial of {n} is {fact}")
# n = int(input("Enter the number: "))
# fact = 1
# i=1
# while  (i<=n):
#     fact =fact*i
#     i+=1
# print(f"Factorial of {n} is {fact}")

# star patterns
n = 5
for i in range (5,0,-1):
    print(" " , end="")
    print("*" * (2*i-1), end="")
    print("")

'''
***
* *
***
'''
# n=3
# for i in range (1,n+1):
#    if i==1 or i==n:
#     print("*"*n)
#    else:
#      print("*", end="")
#      print(" "*(n-2), end="" )
#      print("*", end="")
#    print("")

# n = int(input("Enter the number: "))
# for i in range (1,11):
#     print(f"{n} x {11-i} = {n*(11-i)}") 
