name = input("type your name! ")
print("welcome", name, "to this adventure!")

answer = input("you are on a dirt road that ends. You can go left or right. Which way do you wanna go? ").lower()

if answer == "left":
    answer == input("you come across river, walk around or swim across? ")
    if answer == "swim":
        print("you swam across and were killed.")
    elif answer == "walk":
        print("you walked around and won the game. ")
    else:
        print("not a valid option. you loose!")
    
    
elif answer == "right":
    answer == input("you come across bridge, cross or run? ")
    if answer == "cross":
        print("you crossed and lived happily ever after. ")
    elif answer == "run":
        print("you ran and lost the game. ")
    else:
        print("not a valid option. you loose!")
        
else:
    print("not a valid option. you loose!")
    
print("Thank you for playing")