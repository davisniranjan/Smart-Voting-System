from tkinter import *
from tkinter import filedialog
from keras.models import load_model
import cv2
import numpy as np
import tkinter
from tkinter.ttk import *

temp='1' 
#valid voter id details 
valid_voter_details = {
    '0': {'name': 'Chitresh', 'age': 17, 'address': 'Race course St'},
    '1': {'name': 'Jaii', 'age': 17, 'address': '456 Thudiyalur St'},
    '2': {'name': 'Aishwarya', 'age': 18, 'address': '789 Peelamedu St'},
    '3': {'name': 'Kavya', 'age': 18, 'address': '789 Saibaba St'},
    '4': {'name': 'Loga srinithi', 'age': 18, 'address': '799 Saravanampatti St'} ,
    '5': {'name': 'Josikasri', 'age': 18, 'address': '776 Anna St'}
}

parties = {
    "Party A": 0,
    "Party B": 0,
    "Party C": 0,
    "Party D": 0
}

valid_voter_ids = ["0", "1", "2", "3", "4","5"]


def vote():
    def submit_vote():
        voter_id = voter_id_entry.get()
        if voter_id in valid_voter_ids:
            party = selected_party.get()
            parties[party] += 1
            print(f"{voter_id} voted for {party}.")
        else:
            print("Invalid Voter ID.Please enter a valid one")

    label = tkinter.Label(window, text="Select Party:")
    label.pack()
    label.place(x=710,y=330)
    selected_party = tkinter.StringVar()


    for i, party in enumerate(parties):
        party_radio_button = tkinter.Radiobutton(window, text=party, variable=selected_party, value=party)
        party_radio_button.place(x=720, y=350+i*30)

    submit_button = tkinter.Button(window, text="Submit", command=submit_vote)
    submit_button.pack()
    submit_button.place(x=660,y=500)
    

#button for getting voter details 
def get_voter_details():
    global temp
    voter_id = voter_id_entry.get()
    if voter_id in valid_voter_details:
        voter_details = valid_voter_details[voter_id]
        voter= voter_details['name']
        temp=voter
        name_label.config(text="Name: " + voter_details['name'])
        age_label.config(text="Age: " + str(voter_details['age']))
        address_label.config(text="Address: " + voter_details['address'])
        result_label.config(text="Valid voter ID.", fg="green")
    else:
        name_label.config(text="")
        age_label.config(text="")
        address_label.config(text="")
        result_label.config(text="Invalid voter ID.", fg="red")
        
# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = load_model("D:\keras_model.h5", compile=False)

# Load the labels
class_names = open("D:\labels.txt", "r").readlines()

# Create a window
window = Tk()
window.title("Smart voting system")
window.geometry("500x200")

# Create a label for the webcam image
image_label = Label(window, text="Voter ID verification")
image_label.pack()

# Create a label for the voter ID entry field
voter_id_label = tkinter.Label(window, text="Enter your voter ID:")
voter_id_label.pack()


# Create an entry field for the voter ID
voter_id_entry = tkinter.Entry(window)
voter_id_entry.pack()


# Create a button to get the voter details
get_details_button = tkinter.Button(window, text="Get Details", command=get_voter_details)
get_details_button.pack()


# Create a label for the voter name
name_label = tkinter.Label(window, text="")
name_label.pack()


# Create a label for the voter age
age_label = tkinter.Label(window, text="")
age_label.pack()

# Create a label for the prediction result
result_label = Label(window, text="")
result_label.pack()




# Create a label for the voter address
address_label = tkinter.Label(window, text="")
address_label.pack()


# Create a label for the verification result
result_label = tkinter.Label(window, text="")
result_label.pack()

# Create a label for the webcam image
face_label = Label(window, text="Face Verification")
face_label.pack()


# Create a function to capture the webcam image and make a prediction
def capture_image():
    # Grab the webcamera's image.
    ret, image = camera.read()

    # Resize the raw image into (224-height,224-width) pixels
    image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)

    # Show the image in a label
    cv2.imshow("Webcam Image", image)

    # Make the image a numpy array and reshape it to the models input shape.
    image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)

    # Normalize the image array
    image = (image / 127.5) - 1

    # Predicts the model
    prediction = model.predict(image)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    # Print prediction and confidence score
    result_label.config(text="Class: " + class_name[2:] + " Confidence Score: " + str(np.round(confidence_score * 100))[:-2] + "%")
    confidence_per=int(str(np.round(confidence_score * 100))[:-2])
    
    # Create a label for the verification
    veri_label = Label(window, text="Verified Sucessfully ! you are eligible to vote...")
    veri_label.pack()
    veri_label.place(x=650,y=300)
            
            

    # Listen to the keyboard for presses.
    keyboard_input = cv2.waitKey(1)

    # 27 is the ASCII for the esc key on your keyboard.
    if keyboard_input == 27:
        window.destroy()

    # Call this function again after 10ms (i.e. update the webcam image)
    window.after(10, capture_image)

# Create a function to start the webcam
def start_webcam():
    global camera
    camera = cv2.VideoCapture(0)
    # Call the capture_image function after 10ms (i.e. start updating the webcam image)
    window.after(10, capture_image)
# Create a function to stop the webcam

selected_party = tkinter.StringVar()


def submit_vote():
    voter_id = voter_id_entry.get()
    if voter_id in valid_voter_ids:
        party = selected_party.get()
        parties[party] += 1
        print(f"{voter_id} voted for {party}.")
    else:
        print("Invalid Voter ID.")
    im_label = Label(window, text="Thanks for Voting!!!")
    im_label.pack()
    im_label.place(x=700,y=550)

def vote():
    
    label = tkinter.Label(window, text="Select Party:")
    label.pack()
    label.place(x=710,y=330)
    


    for i, party in enumerate(parties):
        party_radio_button = tkinter.Radiobutton(window, text=party, variable=selected_party, value=party)
        party_radio_button.place(x=720, y=350+i*30)

    submit_button = tkinter.Button(window, text="Submit", command=submit_vote)
    submit_button.pack()
    submit_button.place(x=730,y=500)


    
def stop_webcam():
    camera.release()
    cv2.destroyAllWindows()
    vote()

    

    
# Create a button to start the webcam
start_button = Button(window, text="Start Webcam", command=start_webcam)
start_button.pack()

# Create a button to stop the webcam
stop_button = Button(window, text="Stop Webcam", command=stop_webcam)
stop_button.pack()


#button place


stop_button.place(x=760,y=260)#
start_button.place(x=660,y=260)#
face_label.place(x=710,y=240)#
address_label.place(x=700,y=180)#
result_label.place(x=700,y=200)#
age_label.place(x=700,y=160)#
name_label.place(x=700,y=140)#
voter_id_label.place(x=700,y=50)#
image_label.place(x=700,y=20)#
get_details_button.place(x=720,y=100)#
voter_id_entry.place(x=690,y=70)#
# Run the window
window.mainloop()
