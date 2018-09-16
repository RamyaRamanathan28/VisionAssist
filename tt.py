import speech_recognition as sr
from gtts import gTTS
import os
import re
import requests
from key import key
import json
import os
import numpy as np
import time
import pyglet
from pprint import pprint
import requests



def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print("Say something!")
        audio = r.listen(source,phrase_time_limit=5)

    try:
        recognisedSpeech=r.recognize_google(audio)
        print("You said: " + recognisedSpeech)
        k=0
    except sr.UnknownValueError:
        print("Could not understand audio. Try Again.")
        recognisedSpeech = "again"
        k=1
        print(recognisedSpeech)
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        k=1
    return str(recognisedSpeech), k

def robustListen():
    k=1
    command, k=listen()
    time.sleep(2)
    while command=="again" and k:
        speak("Please repeat")
        command, k =listen()
        time.sleep(2)
        
    return command

def speak(mytext):
    language = 'en'
    mytext = re.sub('[<][^>]*[>]', '', mytext)
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("welcome.mp3")
##    music = pyglet.resource.media('welcome.mp3')
##    music.play()
##  os.system("afplay welcome.mp3")
    
    os.system("play welcome.mp3")
    
    time.sleep(2)
    
def watspeak(mytext):
    text_to_speech = TextToSpeechV1(
    username='c7f77f05-d0d0-4b9c-8344-487b4e3a9d81',
    password='ma1M8GmcFKZn')
    with open(join(dirname(__file__), 'output.mp3'),'wb') as audio_file:
        audio_file.write(
        text_to_speech.synthesize(mytext, accept='audio/wav',
                                  voice="en-US_AllisonVoice").content)
    os.system("omxplayer -o local output.mp3")
def getDistanceTime(origin, destination):
    search_url = "https://maps.googleapis.com/maps/api/distancematrix/json"
    search_payload = {"key": key, "origins": origin, "destinations": destination}
    search_req = requests.get(search_url, params=search_payload)
    search_json = search_req.json()
    distance = search_json["rows"][0]["elements"][0]["distance"]["text"]
    timetaken = search_json["rows"][0]["elements"][0]["duration"]["text"]
    print(("The distance is " + distance))
    print("The time taken is " + timetaken)

    return distance, timetaken

def getDirections(origin,destination, i=0):
    search_url = "https://maps.googleapis.com/maps/api/directions/json"
    search_payload = {"key": key, "origin": origin, "destination": destination}
    search_req = requests.get(search_url, params=search_payload)
    search_json = search_req.json()
    directions = search_json["routes"][0]["legs"][0]["steps"][i]['html_instructions']
    return directions

def maps(i, origin="", destination="", resume = False):
    if resume==True:
        next="next"
        s = 1
        while s:
            if next == "next":
                i = i + 1
                directions = getDirections(origin, destination, i)
                speak(directions)
                next = ""
            else:
                if next == "repeat":
                    directions = getDirections(origin, destination, i)
                    speak(directions)
                    
                    next=robustListen()
                else:
                    c = input()
                    next = robustListen()
                    if next == "go back":
                        s = 0
        return i, origin, destination
    start = "Please state your origin"
    speak(start)
    
    origin = robustListen()
    stop = "please state your destination"
    speak(stop)
    
    destination = robustListen()
    dist,time = getDistanceTime(origin, destination)
    speak("The distance is " + dist + "and estimated time taken is" + time)
    speak("Would you like directions?")
    
    resp = robustListen()
    if resp=='yes':
        directions=getDirections(origin,destination,i)
        speak(directions)
    else:
        return i, origin, destination
    
    next = robustListen()
    while next not in ["next" , "repeat" , "go back"]:
        speak("Unrecognised Command. Please repeat")
        next=robustListen()
    s=1
    while s:
        if next=="next":
            i=i+1
            directions=getDirections(origin,destination,i)
            speak(directions)
            next = ""
        else:
            if next=="repeat":
                directions=getDirections(origin,destination,i)
                speak(directions)
            else:
                
                next=robustListen()
                if next=="go back":
                    s=0
    return i,origin, destination

def captureImage():
    # initialize the camera
    os.system("raspistill -o /home/pi/Desktop/Captured/image.jpg")

def weather():
    r=requests.get('http://api.openweathermap.org/data/2.5/weather?q=Bangalore&APPID=1d56657f6707d603f0e3f001841131cd')
    w=r.json()
    maxtemp=w["main"]["temp_max"]
    mintemp=w["main"]["temp_min"]
    speak("The temperature will range between " + str(mintemp) + " and " + str(maxtemp) + "farenheit")
    desc = w['weather'][0]['description']
    speak("The weather has " + desc)
    print(desc)

global i
global origin
global destination
i=0

speak('Welcome to Vision Assist')
time.sleep(3)
while 1:
##    input()
##    time.sleep(2)
    maincommand = robustListen()
    if maincommand=="map":
         i, origin, destination = maps(i=0)
    if maincommand=="resume":
        maps(i, origin, destination, True)
    if maincommand=="capture":
        captureImage()
    
        time.sleep(3)
        speak("Capturing Image")
        time.sleep(3)
##    speak("Do you want to read?")
##    time.sleep(20)
        
        os.system("export GOOGLE_APPLICATION_CREDENTIALS=/home/pi/Desktop/key.json" + '\n' + "python3 rpi.py")
        
##    subcommand=robustListen()
    
    if maincommand=="read":
        os.system("export GOOGLE_APPLICATION_CREDENTIALS=/home/pi/Desktop/key.json" + '\n' + "python3 read.py")
        time.sleep(20)
##        os.system("python read.py")
##    speak("Do you want to describe?")
##    time.sleep(3)
##    subcommand2=robustListen()
    if maincommand=="describe":
        os.system("python image_captioning2.py")
        time.sleep(10)
        
        
##    speak("Please wait")
##    time.sleep(10)
        
        
    if maincommand=="weather":
        weather()
        
        
        
        
        
        
        
        
        
        
        
##        danger=isDanger()
        #if danger=="danger":
##        speak("There could be danger nearby. Please ask for help")
##        speak("Please wait")
##        os.system("cd tensorflow/models/research/object_detection" + '\n' +
##                  "python detection.py")
##        croppedbillboard = cv2.imread("tensorflow/models/research/object_detection/cropped_billboards/0.jpg")
##        time.sleep(10)
##        if croppedbillboard.any!=None:
##            speak("There are signs in your vicinity.")
##            speak("Would you like them read")
##            
##            resp=robustrobustListen()
##            if resp=="yes":
               #uncomment the following lines to run OCR
               #make sure to put your AZURE pass details in the ocr.py file
               # os.system("cd tensorflow/models/research/object_detection/cropped_billboards" + '\n' +
               #           "python ocr.py")
##                f=open("tensorflow/models/research/object_detection/cropped_billboards/Output.txt", "r")
##                contents=f.read()
##                speak("The sign says " + contents)


