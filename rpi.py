from google.cloud import storage
client = storage.Client()
#image.jpg is taken from the camera module
bucket = client.get_bucket('object28')
blob = bucket.blob('image.jpg')
blob.upload_from_filename('image.jpg')
found=0
while found==0:
    print("1")
    bucket = client.get_bucket('object28')
    for key in bucket.list_blobs():
      if key.name == 'ocr.txt':
        found=1
        print("FOUND")
        break
blob = bucket.blob('ocr.txt')
blob.download_to_filename('ocr.txt')
bucket.delete_blob('ocr.txt')
#TEXT TO SPEECH
