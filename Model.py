import cv2
from keras.models import load_model
import numpy as np
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

while True: 
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    cv2.imshow('frame', frame)
    # Press q to close the window
    print(prediction)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
            
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()

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



