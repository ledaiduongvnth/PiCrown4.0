import requests

url = 'http://172.16.10.236:5000/sound'
requests.get(url, params={"command":"wrong_ticket"})