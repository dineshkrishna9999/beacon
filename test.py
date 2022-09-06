import requests,json

from dgen import datafunction

headers = { 'Accept' : 'application/json', 'Content-Type' : 'application/json'}
contents=datafunction.f
r = requests.post('http://127.0.0.1:5000/', data=json.dumps(contents), headers=headers)

print(f"Status Code: {r.status_code}, Response: {r.json()}")