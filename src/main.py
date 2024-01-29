import requests
from fastapi import FastAPI

app = FastAPI()

API_URL = "https://api-inference.huggingface.co/models/tae898/emoberta-large"
API_TOKEN = "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"

@app.post("/process_input_and_output")
async def process_input_and_output(data: dict):
    try:
        user_input = data["input"]

        # Perform inference with the received input
        headers = {"Authorization": f"Bearer {API_TOKEN}"}
        model_data = {"inputs": user_input}

        def round_recursive(item):
            if isinstance(item, (int, float)):
                return "{:.2f}".format(item * 100).zfill(5)
            elif isinstance(item, list):
                return [round_recursive(sub_item) for sub_item in item]
            elif isinstance(item, dict):
                return {key: round_recursive(value) for key, value in item.items()}
            else:
                return item

        # Send output to the same server
        output_response = requests.post(API_URL, headers=headers, json=model_data)

        if output_response.status_code == 200:
            result = output_response.json()
            rounded_result = round_recursive(result)
            print(rounded_result)
        else:
            return {"error": f"Error from model server: {output_response.status_code}"}

    except KeyError:
        return {"error": "Input not provided"}
