arr = [-5, 3, -2, 8, 0, 7, -1]
count=0
for num in arr:
    if num>0:
        count+=1
        print(num, " is positive no")
    elif num==0:
        print(num ," is neutral no")
print("total positive no ", count)