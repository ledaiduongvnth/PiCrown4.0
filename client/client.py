import requests
import base64
import time

url = 'http://localhost:5000/display'

with open('./face.jpeg', 'rb') as f1:
    f1_bytes = f1.read()

with open('./license_plate.jpeg', 'rb') as f2:
    f2_bytes = f2.read()


for i in range(5):
    data = {
        "status": "OK",
        "message": "xin chào các bạn",
        "lane_id": "L",
        "is_landscape": "1",
        "title": str(i),
        "profile_image": base64.b64encode(f1_bytes),
        "license_plate_image": base64.b64encode(f2_bytes)
    }
    print(i)
    requests.post(url, data=data)
    time.sleep(2)

