import random

computer = random.choice([-1,0,1])
print("enter s for stone")
print("enter p for paper")
print("enter ss for sisscor")

youstr = input("Enter your choice: ")
youdict = {"s": 1, "p": -1, "ss":0}
reversedict = {1: "Stone", -1:"Paper", 0: "sissor"}
you = youdict[youstr]
print(f"you chose:{reversedict[you]}\ncomputer chose {reversedict[computer]}")
if computer == you:
    print("It's a draw")
else:
    if (computer == -1 and you in [0, 1]) or (computer == 1 and you == 0):
        print("You lose!")
    elif computer == 1 and you == -1:
        print("You win!")
    else:
        print("Something went wrong")
