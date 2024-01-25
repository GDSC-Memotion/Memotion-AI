import requests
 
API_URL = "https://api-inference.huggingface.co/models/tae898/emoberta-large"
API_TOKEN = "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"
 
headers = {"Authorization": f"Bearer {API_TOKEN}"}
data = {"inputs": "i am so sad"}
 
response = requests.post(API_URL, headers=headers, json=data)
 
if response.status_code == 200:
    result = response.json()
    rounded_result = round(result, 3)  # Round to 3 decimal places
    print(rounded_result)
    print(result)
else:
    print(f"Error: {response.status_code}")