import requests

url = 'http://localhost:5000/display'
files = {
    'profile_image': open('/home/d/Pictures/Screenshot from 2020-11-20 15-10-40.png', 'rb')
}
data = {
    "id": "id",
    "lane_id": "R",
    "is_landscape": "1",
    "title": "title"
}

requests.post(url, files=files, data=data)