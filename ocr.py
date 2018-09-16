#from PIL import Image
import pytesseract
import argparse
#import cv2
import os
import sys
import subprocess
import numpy as np
import requests


subscription_key = "f2d0c65da1964ea6abe416720d3801a0"
assert subscription_key



ocr_url=r'https://westcentralus.api.cognitive.microsoft.com/vision/v1.0/ocr'
headers  = {'Content-Type':'application/octet-stream','Ocp-Apim-Subscription-Key': '48619f06b744435b8856d53c8903ff21'}
params   = {'language': 'en', 'detectOrientation ': 'true'}
img_file=r'C:\Users\User\Desktop\billboard1.jpg'
with open(img_file,'rb') as f:
        img_data=f.read()
response = requests.post(ocr_url, headers=headers, params=params, data=img_data)

print(response.text)
response.raise_for_status()



analysis = response.json()
line_infos = [region["lines"] for region in analysis["regions"]]
word_infos = []
for line in line_infos:
    for word_metadata in line:
        for word_info in word_metadata["words"]:
            word_infos.append(word_info)
for word in word_infos:
    print(word["text"])
'''
TESSDATA_PREFIX = 'C:\\Tesseract-OCR'
tessdata_dir_config='--tessdata-dir "C:\\Tesseract-OCR\\tessdata"'
tesseract_cmd = 'C:\\Tesseract-OCR\\tesseract'
image = cv2.imread("download19.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# check to see if we should apply thresholding to preprocess the
# image
#gray = cv2.threshold(gray, 155, 200,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

 #img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply dilation and erosion to remove some noise
kernel = np.ones((1, 1), np.uint8)
gray = cv2.dilate(gray, kernel, iterations=1)
gray = cv2.erode(gray, kernel, iterations=1)
 
# make a check to see if median blurring should be done to remove
# noise

gray = cv2.medianBlur(gray, 3)

 
# write the grayscale image to disk as a temporary file so we can
# apply OCR to it
filename = "{}.jpg".format(os.getpid())
cv2.imwrite(filename, gray)
print(filename)
src=r'C:\\Users\\User\\Desktop\\codefundo\\'
img = Image.open(src+filename)

pytesseract.pytesseract.tesseract_cmd = 'C:\\Tesseract-OCR\\tesseract'
text = pytesseract.image_to_string(img)
#os.remove(filename)
print(text)
''' 
# show the output images
        
