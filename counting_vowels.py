# counting vowels in a string
s = "Programming"
count=0
for ch in s:
    if ch in "aeiou":
        count+=1
print(count)
