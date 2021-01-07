import requests
import base64
import time

url = 'http://localhost:5000/display'

with open('./face.jpeg', 'rb') as f1:
    f1_bytes = f1.read()

with open('./license_plate.jpeg', 'rb') as f2:
    f2_bytes = f2.read()


for i in range(1):
    data = {
        "status": "STOP",
        "message": "xin chào các bạn",
        "lane_id": "L",
        "is_landscape": "1",
        "license_plate_text": "21G-545" + str(i),
        "profile_image": base64.b64encode(f1_bytes),
    }
    print(i)
    requests.post(url, data=data)
    time.sleep(3)

