from google.cloud import storage
client = storage.Client()

while found==0:
    print("1")
    bucket = client.get_bucket('object28')
    for key in bucket.list_blobs():
      if key.name == 'image.jpg':
        found=1
        print("FOUND")
        break
blob=bucket.blob('image.jpg')
blob.download_to_filename('image.jpg')    
bucket.delete_blob('image.jpg')

#OCR outputs ocr.txt
bucket = client.get_bucket('object28')
blob = bucket.blob('ocr.txt')
blob.upload_from_filename('ocr.txt')
