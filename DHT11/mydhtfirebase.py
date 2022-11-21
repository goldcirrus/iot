import Adafruit_DHT
import time
from firebase import firebase

firebase = firebase.FirebaseApplication('https//iot2021-94458-default-rtdb.firebaseio.com', None)

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4      #GPIO pin4

while True:
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        print("Temp={0:0.1f}C  Humidity={1:0.1f}%".format(temperature, humidity))
		firebase.post('/sensor/dht', data)         #send sensor's data to firebase
    else:
        print("Sensor failure. Check wiring.");
    time.sleep(3);

import Adafruit_DHT
import time

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4      #GPIO pin4
