# define the countdown func.
def countdown(t):
    
    while t:
        mins, secs = divmod(t, 3)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
      
    print('Rock, paper, scissors, shoot!')



def get_computer_choice():
    return random.choice(["Rock", "Paper", "Scissors"])

     
def get_winner(computer_choice, user_choice, user_wins, computer_wins):
    
        if computer_choice == "Rock":
            if user_choice == "Rock":
                print(f"You chose: {user_choice}")
                print("It's a tie!")
                user_wins = user_wins + 1
                computer_wins = computer_wins + 1
                print(f"The score is {computer_wins} points to computer and the score is {user_wins} to user")
        elif user_choice == "Paper":
            print(f"You chose: {user_choice}")
            print("Congratulations, you won!")
            user_wins = user_wins + 1
            print(f"The score is {computer_wins} points to computer and the score is {user_wins} to user")
        else:
            print(f"You chose: {user_choice}")
            print("Oh no! You lost!")
            computer_wins = computer_wins + 1
            print(f"The score is {computer_wins} points to computer and the score is {user_wins} to user")
        if computer_choice == "Paper":
            if user_choice == "Rock":
                print(f"You chose: {user_choice}")
                print("Oh no! You lost!")
                computer_wins = computer_wins + 1
                print(f"The score is {computer_wins} points to computer and the score is {user_wins} to user")
            elif user_choice == "Paper":
                print(f"You chose: {user_choice}")
                print("It's a tie!")
                computer_wins = computer_wins + 1
                user_wins = user_wins + 1
                print(f"The score is {computer_wins} points to computer and the score is {user_wins} to user")
            else:
                print(f"You chose: {user_choice}")
                print("Congratulations, you won!")
                user_wins = user_wins + 1
                print(f"The score is {computer_wins} points to computer and the score is {user_wins} to user")
        if computer_choice == "Scissors":
            if user_choice == "Rock":
                print(f"You chose: {user_choice}")
                print("Congratulations, you won!")
                print(f"The score is {computer_wins} points to computer and the score is {user_wins} to user")
            elif user_choice == "Paper":
                print(f"You chose: {user_choice}")
                print("Oh no! You lost!")
                computer_wins = computer_wins + 1
                print(f"The score is {computer_wins} points to computer and the score is {user_wins} to user")
            else:
                print(f"You chose: {user_choice}")
                print("It's a tie!")
                computer_wins = computer_wins + 1
                user_wins = user_wins + 1
                break

            
def get_user_choice():
    while True:
        user_choice = input("Choose either Rock, Paper or Scissors: ").lower()
        return (f" You chose: {user_choice} ")   
    

def play(get_winner, get_user_choice, get_computer_choice, get_computer_wins, get_user_wins):
    computer_wins = get_computer_wins()
    user_wins = get_user_wins()
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    winner = get_winner(computer_choice, user_choice)
    print(winner)
    print(user_wins)
    print(computer_wins)

    
import cv2
   
# import the time module
import time
  
import random

# input time in seconds
t = input("Enter the time in seconds: ")
  
# function call
countdown(int(t))



from keras.models import load_model
import numpy as np
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

user_options = ["Rock", "Paper", "Scissors", "Nothing"]
while True: 
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    # innerlist
    user_choice = prediction[0] 
    # index of highest value 
    user_choice = np.argmax(user_choice)
    # option to index
    user_choice = user_options [user_choice]
    cv2.imshow('frame', frame)
    # Press q to close the window
    print(user_choice)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
            
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()

     
user_wins = 0
computer_wins = 0
     
print (play(user_wins, computer_wins))

print (get_user_choice())
        
print (play(get_winner, get_user_choice, get_computer_choice))

get_winner()




