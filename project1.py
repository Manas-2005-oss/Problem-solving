# snake water gun game
import random

'''
1=snake
-1 water
0 gun'''

computer = random.choice([1,-1,0])
user = input("Enter your choice(s,w,g): ")
dict = {"s":1,"w":-1,"g":0}
reverse_dict ={1:"snake",-1:"water",0:"gun"}
user =dict[user]

print(f"Computer choice is {reverse_dict[computer]}\n and user choice is {reverse_dict[user]}")

if computer == user:
    print("Its a tie!")
else:
    if(computer == 1 and user ==-1):
        print("Computer wins")
    elif(computer == 1 and user ==0):
        print("User wins")
    elif(computer ==-1 and user ==1):
        print("user wins")
    elif(computer ==-1 and user==0):
        print("computer wins")
    elif(computer == 0 and user ==1):
        print("computer wins")
    elif(computer == 0 and user ==-1):
        print("user wins")
    else:
        print("error")