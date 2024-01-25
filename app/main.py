import requests
from fastapi import FastAPI

app = FastAPI()

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

'''
@app.post("/process_input_and_output")
async def process_input_and_output(data: dict):
    try:
        user_input = data["input"]

        # Perform inference with the received input
        headers = {"Authorization": f"Bearer {API_TOKEN}"}
        model_data = {"inputs": user_input}

        # Send output to the same server
        output_response = requests.post(API_URL, headers=headers, json=model_data)

        if output_response.status_code == 200:
            result = output_response.json()
            rounded_result = round(result, 3)  # Round to 3 decimal places

            # Return the rounded result
            return {"output": rounded_result}
        else:
            return {"error": f"Error from model server: {output_response.status_code}"}

    except KeyError:
        return {"error": "Input not provided"}
'''