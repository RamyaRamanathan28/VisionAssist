# Vision Assist

The structure of Vision Assist is as follows:

templates folder consists of:

blind.html : the main interface page for the emergency contacts \n 
map.html : displays the map with a marker showing the user's current location to the contacts
register.html : page for the emergency contacts to register themselves 
signin.html : page for the emergency contacts to sign in
track.html : page which helps the emergency contacts to see the travel time and distance between their current location and user's current location

(screen shots are provided)


Python Scripts:

ui2.py : User interface script for emergency contacts
tts_test2.py : text to speech using IBM Watson
rpi.py : script which uploads images captured by the camera to the GCP bucket and downloads the OCR result from 
ocr.py : script which carries out OCR
maps.py : computes distance and time between the user's current position and the contact person's current position using Google Distance Matrix API
laptop.py : downloads the image captured by the PI from the GCP bucket and uploads the OCR result on to the GCP bucket
image_captioning.py : describes the image uploaded using Microsoft Azure cognitive services
email2.py : when the user informs the device about an emergency situation, the selected contacts are sent an email notification about the user's current location


Some of these run on the Pi, while some run on the server (laptop) 
the main functions of the above scripts are : 
object detection
OCR
Navigation
weather report
Image captioning
Emergency Help

Laptop and Pi both access the cloud, and upload/download files as needed.(egs rpi.py)  This is used for networking. 
Cloud is also interfaced with pir front end for tracking and regular updates. 