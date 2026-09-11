arr = [2,7,11,15]
target = 9
left=0
right=len(arr)-1
while left<right:
    total=arr[left]+arr[right]
    if total==target:
        print(total,"found it",arr[left],arr[right])
        break
    elif total>target:
        right-=1
    elif total<target:
        left+=1
