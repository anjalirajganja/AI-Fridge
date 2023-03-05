import tensorflow as tf
import RPi.GPIO as GPIO
import MFRC522
import time

# Initialize the RFID tag reader
MIFAREReader = MFRC522.MFRC522()

# Load the TensorFlow model
model = tf.keras.models.load_model('model.h5')

# Define the list of food items
food_items = ['apple', 'banana', 'orange', 'milk', 'cheese']

# Define the initial inventory levels
inventory = {'apple': 0, 'banana': 0, 'orange': 0, 'milk': 0, 'cheese': 0}

# Define the GPIO pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

# Function to update the inventory levels
def update_inventory(food_item):
    inventory[food_item] += 1
    print('Inventory Updated: ', inventory)

# Main loop
while True:
    # Wait for RFID tag
    print('Place RFID tag near the reader...')
    (status, TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    # If RFID tag detected, read the tag
    if status == MIFAREReader.MI_OK:
        # Get the RFID tag data
        (status, uid) = MIFAREReader.MFRC522_Anticoll()

        # If RFID tag read successfully, get the food item name from TensorFlow model
        if status == MIFAREReader.MI_OK:
            # Convert the RFID tag data to a string
            tag_data = ''.join(map(str, uid))

            # Convert the tag data to a TensorFlow input format
            input_data = [float(x) for x in tag_data]

            # Use the TensorFlow model to predict the food item
            prediction = model.predict([input_data])[0]
            food_item = food_items[prediction.argmax()]

            # Update the inventory levels
            update_inventory(food_item)

            # Turn on the LED to indicate successful RFID tag read
            GPIO.output(11, GPIO.H
        print('RFID tag read successfully')
        GPIO.output(13, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(13, GPIO.LOW)
