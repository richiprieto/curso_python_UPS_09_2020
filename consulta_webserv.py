import json
import requests

# TC, PRES, HUM
data = {"num1": 10, "num2": 22}
data_json = json.dumps(data)
headers = {"content-type": "application/json"}
r = requests.post(
    "http://127.0.0.1:5000/api/v1/suma",
    data=data_json,
    headers=headers
)
respuesta_api = r.json()
print(respuesta_api)
print(respuesta_api["respuesta"])
