# finding index of the element in array
arr = [12, 5, 18, 7, 20]
target = 7
for i in range(len(arr)):
    if target == arr[i]:
        print(i)
        break




# finding the index of repeated or duplicated elements
arr = [5,2,5,8,5,3]
target=5
for i in range(len(arr)):
    if arr[i] == target:
        print(i)