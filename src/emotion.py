'''
import requests
API_URL = "https://api-inference.huggingface.co/models/tae898/emoberta-large"
headers = {"Authorization": f"Bearer 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"}
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()
data = query("Can you please let us know more details about your ")
'''
import requests
 
API_URL = "https://api-inference.huggingface.co/models/tae898/emoberta-large"
API_TOKEN = "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"
 
headers = {"Authorization": f"Bearer {API_TOKEN}"}
data = {"inputs": "i am so sad"}
def round_recursive(item):
    if isinstance(item, (int, float)):
        return "{:.2f}".format(item * 100).zfill(5)
    elif isinstance(item, list):
        return [round_recursive(sub_item) for sub_item in item]
    elif isinstance(item, dict):
        return {key: round_recursive(value) for key, value in item.items()}
    else:
        return item

response = requests.post(API_URL, headers=headers, json=data)

if response.status_code == 200:
    result = response.json()
    rounded_result = round_recursive(result)
    print(rounded_result)
else:
    print(f"Error: {response.status_code}")
