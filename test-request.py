import requests
import json

url = "http://192.168.43.90:9001/pins"
data = {'17': 'true', '18': 'false'}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
r = requests.post(url , data=json.dumps(data), headers=headers)
