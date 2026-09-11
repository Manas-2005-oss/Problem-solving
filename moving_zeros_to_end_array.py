arr = [0, 1, 0, 3, 12]
left = 0
for i in range (len(arr)):
    if arr[i]!=0:
        arr[left],arr[i]=arr[i],arr[left]
        left+=1
print(arr)