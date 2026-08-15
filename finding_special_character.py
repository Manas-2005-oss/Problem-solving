s = "Python@2026#AI!"
count=0
for ch in s:
    if ch.isalnum()==False:
        count+=1
print(count)