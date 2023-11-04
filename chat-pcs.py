import paho.mqtt.client as mqtt
import random
import time
# List of predefined messages
messages = ["Hello Kundwa, how are you?",
            "Good morning!", "What's up?", "How's it going?"]


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("/kundwa")


def on_message(client, userdata, msg):
    print("Kundwa: " + str(msg.payload.decode()))


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("82.165.97.169", 1883, 60)
# Start the network loop
client.loop_start()
while True:
    # Select a random message from the array
    random_message = random.choice(messages)
    print("Sending: " + random_message)
    client.publish("/rita", random_message)
    time.sleep(5)  # Send a message every 5 seconds
