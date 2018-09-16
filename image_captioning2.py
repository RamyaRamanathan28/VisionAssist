#assert subscription_key
vision_base_url = r'https://westcentralus.api.cognitive.microsoft.com/vision/v1.0/analyze'
img_file=r'C:/Users/User/Desktop/dog.jpg'
with open(img_file,'rb') as f:
        img_data=f.read()
import requests
headers  = {'Content-Type':'application/octet-stream','Ocp-Apim-Subscription-Key': '2c96f76702f84d42953ed54fa1df65ad' }
params   = {'visualFeatures': 'Categories,Description,Color'}
response = requests.post(vision_base_url, headers=headers, params=params, data=img_data)
print(response.text)
response.raise_for_status()
analysis = response.json()
image_caption = analysis["description"]["captions"][0]["text"].capitalize()
print(image_caption)
