# counting repearted elements in array   
arr = [5, 2, 5, 8, 5, 3]
target = 5
count = 0
for num in arr:
    if num == target:
        count+=1
print(count)

# counting repearted multiple elements in array 
arr = [5, 2, 5, 8, 5, 9, 3, 9]
target1 = 5
target2= 9
count1 = 0
count2 = 0
for num in arr:
    if num == target1:
        count1+=1
    if num== target2:
        count2+=1
print(count1)
print(count2)

