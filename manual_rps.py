import random

get_computer_choice = ("Rock", "Paper", "Scissors", "Nothing")
random.choice(get_computer_choice)

 # print (get_computer_choice)


get_user_choice  = input("Choose either Rock, Paper or Scissors. ").lower()
 # print(get_user_choice)

def get_winner(computer_choice, user_choice):
     if computer_choice == "Rock":
        if user_choice == "Rock":
            print("It's a tie!")
        elif user_choice == "Paper":
             print("Congratulations, you won!")
        elif user_choice == "Scissors":
             print("Oh no! You lost!")
        else:
             print("Please select your choice. ")
     if computer_choice == "Paper":
        if user_choice == "Rock":
            print("Oh no! You lost!")
        elif user_choice == "Paper":
            print("It's a tie!")
        elif user_choice == "Scissors":
            print("Congratulations, you won!")
        else:
            print("Please select your choice. ")
     if computer_choice == "Scissors":
        if user_choice == "Rock":
            print("Congratulations, you won!")
        elif user_choice == "Paper":
            print("Oh no! You lost!")
        elif user_choice == "Scissors":
            print("It's a tie!")
        else:
            print("Please select your choice. ")
def play():
    print(get_computer_choice)
    print(get_user_choice)
    print(get_winner)
    play()





   
    

             
           




