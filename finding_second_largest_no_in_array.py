arr=[12,5,18,7,20,3]
largest=arr[0]
second_largest=arr[1]
for num in arr:
    if num>largest:
        second_largest=largest
        largest=num
    elif num>second_largest and num!=largest:
        second_largest=num
print(f"the second largest element is {second_largest} and largest is {largest}")