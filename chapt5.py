d={
    "anand": "happy",
    "ajja": "come",
    2: "two"
}
dict=(input("Enter the key: "))
print(d[dict])

# set
s = {1,5,7,8,9,2,6,10}
print(s)

set = set(input("Enter the numbers: "))
print(set)

s= set()
n = int(input("Enter the number of elements: "))
s.add(n)
n = int(input("Enter the number of elements: "))
s.add(n)
n = int(input("Enter the number of elements: "))
s.add(n)
n = int(input("Enter the number of elements: "))
s.add(n)
n = int(input("Enter the number of elements: "))
s.add(n)
n = int(input("Enter the number of elements: "))
s.add(n)
n = int(input("Enter the number of elements: "))
s.add(n)
n = int(input("Enter the number of elements: "))
s.add(n)
print(s)

s = set()
s.add(18)
s.add("18")
print(s)

d={}
name=input("Enter the name: ")
lang = input("Enter the language: ")
d.update({name:lang})
name=input("Enter the name: ")
lang = input("Enter the language: ")
d.update({name:lang})
name=input("Enter the name: ")
lang = input("Enter the language: ")
d.update({name:lang})
name=input("Enter the name: ")
lang = input("Enter the language: ")
d.update({name:lang})
print(d)
