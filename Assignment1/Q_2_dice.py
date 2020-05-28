from random import randint

while(1):
    x = int(input("Enter 1 to play and 0 to quit\n"))
    if x == 1:
        a = (randint(1,6))
        print(a)
    elif x == 0:
        print("Exit")
        break
    else:
        print("Invalid input!! Try again")