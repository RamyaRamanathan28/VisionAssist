from google.cloud import storage
import speech_recognition as sr
import re
from gtts import gTTS
import os
import time


def speak(mytext):
    language = 'en'
    mytext = re.sub('[<][^>]*[>]', '', mytext)
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("welcome.mp3")
    os.system("play welcome.mp3")
    
    time.sleep(2)
print("here")
client = storage.Client()
#image.jpg is taken from the camera module
bucket = client.get_bucket('object28')
##blob = bucket.blob('image.jpg')
##blob.upload_from_filename('Captured/image.jpg')
found=0
while found==0:
    print("1")
    bucket = client.get_bucket('object28')
    for key in bucket.list_blobs():
      if key.name == 'read.txt':
        print("inside")
        found=1
        print("FOUND")
        f=open("read.txt", "r")
        v=f.read()
        speak(v)
        break
blob = bucket.blob('read.txt')
blob.download_to_filename('read.txt')

##bucket.delete_blob('read.txt')
#TEXT TO SPEECH