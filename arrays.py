import numpy as np
array = np.array([1,2,3,4,5])
max_value = array[0]
for num in array:
    if num > max_value:
        max_value = num
print(max_value)


#find min value in array
import numpy as np
arr = np.array([9,5,8,2,5])
min_element = arr[0]
for num in arr:
    if num < min_element:
        min_element = num
print(min_element)

import numpy as np
arr1 = np.array([9,5,8,2,5])
arr2 = np.array([10,5,8,2,5])

avg = (arr1+arr2)/2
print(avg)




import numpy as np
array = np.array([1,2,3,4,5])
total = 0
for num in array:
    total= total+num
    
print(total)

arr = [5, 10, 15, 20, 25]
for num in arr:
    print(num)

sum of arr
arr=[5, 10, 15, 20, 25]
sum=0
for num in arr:
    sum+=num
print(sum)

arr = [5, 2, 9, 3, 7]
largest=arr[0]
for num in arr:
    if num>largest:
        largest=num   
print(largest)
