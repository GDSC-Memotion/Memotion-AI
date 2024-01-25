import requests
API_URL = "https://api-inference.huggingface.co/models/tae898/emoberta-large"
headers = {"Authorization": f"Bearer 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"}
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()
data = query("Can you please let us know more details about your ")
'''
import requests
API_URL = "https://api-inference.huggingface.co/models/gpt2"
headers = {"Authorization": f"Bearer {API_TOKEN}"}
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()
data = query("Can you please let us know more details about your ")
'''