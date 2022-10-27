# Computer-vision-rock-paper-scissors

For now, I have created a visual image model for the game Rock, paper scissors using Teachable machine.

from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = load_model('keras_Model.h5', compile=False)

# Load the labels
class_names = open('labels.txt', 'r').readlines()

# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1.
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

# Replace this with the path to your image
image = Image.open('<IMAGE_PATH>').convert('RGB')

#resize the image to a 224x224 with the same strategy as in TM2:
#resizing the image to be at least 224x224 and then cropping from the center
size = (224, 224)
image = ImageOps.fit(image, size, Image.ANTIALIAS)

#turn the image into a numpy array
image_array = np.asarray(image)

# Normalize the image
normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

# Load the image into the array
data[0] = normalized_image_array

# run the inference
prediction = model.predict(data)
index = np.argmax(prediction)
class_name = class_names[index]
confidence_score = prediction[0][index]

print('Class: ', class_name, end='')
print('Confidence Score: ', confidence_score)

In this project so far I have created a virtual environment and created code for the rock paper scissors game utilising if-elif-else statements:

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





   
    

             
           





