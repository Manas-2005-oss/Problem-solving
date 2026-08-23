arr = [10, 15, 25, 35, 45]
target = 50
left = 0
right = len(arr) - 1
while left < right:
    total = arr[left] + arr[right]
    if total == target:
        print(total, arr[left], arr[right], "found")
        break
    elif total < target:
        left+=1
    else:
        right-=1