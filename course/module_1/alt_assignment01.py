import random 

user_choice = int(input("What do u want to choose? Type 0 for rock, 1 for paper and 2 for sissors"))
computer_choice = random.randint(0,2)

print(f"Computer chose: {computer_choice}")

if user_choice == 0 and computer_choice == 0 :
    print("Its a tie")
elif user_choice == 0 and computer_choice == 1 :
    print("Computer WON!!")
elif user_choice == 0 and computer_choice == 2 :
    print("You WON!!!")
elif user_choice == 1 and computer_choice == 0 :
    print("You WON!!!")
elif user_choice == 1 and computer_choice == 1 :
    print("Its a tie")
elif user_choice == 1 and computer_choice == 2 :
    print("Computer WON!!!")
elif user_choice == 2 and computer_choice == 0 :
    print("Computer WON!!!")
elif user_choice == 2 and computer_choice == 1 :
    print("You WON!!!")
elif user_choice == 2 and computer_choice == 2 :
    print("Its a tie")
if user_choice not in [0, 1, 2]:
    print("You chose the wrong option!") 
    