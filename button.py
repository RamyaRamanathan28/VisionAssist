import RPi.GPIO as GPIO
import time
import requests
import json


import os

from google.cloud import storage
client = storage.Client()

bucket = client.get_bucket('object28')




GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
f=open("pos.txt","r+");

while True:
    input_state = GPIO.input(18)
    print('Inside')
    if input_state == False:
        print('Button Pressed')
        send_url = 'http://freegeoip.net/json'
        r = requests.get(send_url)
        j = json.loads(r.text)
        lat = j['latitude']
        lon = j['longitude']
        f.write(str(lat)+',');
        f.write(str(lon));
        blob = bucket.blob('pos.txt')
        blob.upload_from_filename('pos.txt')
        time.sleep(0.2)