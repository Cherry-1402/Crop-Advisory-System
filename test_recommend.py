import requests

url = "http://127.0.0.1:5000/recommend"

# Example input data
data = {
    "N": 90,
    "P": 42,
    "K": 43,
    "temperature": 20.8,
    "humidity": 82,
    "ph": 6.5,
    "rainfall": 200
}

response = requests.post(url, json=data)

if response.status_code == 200:
    print("Recommended crop:", response.json().get("recommended_crop"))
else:
    print("Error:", response.json())
