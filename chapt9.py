# 'File I/O'

# # Open a file for reading
# # f= open("file.txt")
# # b=f.read()
# # print(b)
# # f.close()

# # Open file for Reading
# b = "Manas Ippalpalli is Senior Developer who earning with package in crores and happily enjoying is life with his family and friends"

# f = open("filee.txt", "w")
# f.write(b)
# f.close()


# 1.
# f = open ("file.txt")
# c =f.read()
# if "twinkle" in c:
#     print("Twinkle is present in the file")
# else:
#     print("not present")
# f.close()

# 2.
import random

def game():
    print("you are playing a game ")
    s = random.randint(1,50)
    with open("score.txt") as f:
        score =f.read()
        if (score!= ""):
            score = int(score)
        else:
            score = 0
    print(f"the score is{score}")
    if s>score:
        with open("score.txt","w") as f:
            f.write(str(s))
    return s

game()
    