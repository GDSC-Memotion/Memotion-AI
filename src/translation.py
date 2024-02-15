'''
import requests
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
import openai
import requests

url = "http://localhost:8000/emotion"
data = {"user_input": "i am so sad"}
response = requests.post(url, json=data)
print(response.json())

app = FastAPI()

API_URL = "https://api-inference.huggingface.co/models/tae898/emoberta-large"
API_TOKEN = "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"

translator = pipeline("translation", model="Helsinki-NLP/opus-mt-fr-en")

class InputData(BaseModel):
    user_input: str

@app.post("/emotion")
async def process_input_and_output(data: InputData):
    try:
        user_input = data.user_input

        translated_input = translator(user_input)[0]['translation_text']
        headers = {"Authorization": f"Bearer {API_TOKEN}"}
        model_data = {"inputs": translated_input}

        output_response = requests.post(API_URL, headers=headers, json=model_data)

        if output_response.status_code == 200:
            result = output_response.json()
            rounded_result = round_recursive(result)
            print(rounded_result)
            return {"output": rounded_result}
        else:
            return {"error": f"Error from model server: {output_response.status_code}"}

    except KeyError:
        return {"error": "Input not provided."}

def round_recursive(item):
    if isinstance(item, (int, float)):
        return "{:.2f}".format(item * 100).zfill(5)
    elif isinstance(item, list):
        return [round_recursive(sub_item) for sub_item in item]
    elif isinstance(item, dict):
        return {key: round_recursive(value) for key, value in item.items()}
    else:
        return item

MODEL = "gpt-3.5-turbo"
SUMMARY_PROMPT = '''
'''
MAX_LEN = 1024

def callGPT(prompt):
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        temperature=0,
    )
    return response

@app.post("/gpt-summary")
async def generate_summary(data: InputData):
    user_input = data.user_input
    prompt = SUMMARY_PROMPT + user_input
    response = callGPT(prompt)
    return {"summary": response.choices[0].text.strip()}


'''

import requests
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline
import openai
import os

openai_api_key = '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'


app = FastAPI()

API_URL = "https://api-inference.huggingface.co/models/tae898/emoberta-large"
API_TOKEN = "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"

translator = pipeline("translation", model="Helsinki-NLP/opus-mt-fr-en")

class InputData(BaseModel):
    user_input: str

@app.post("/emotion")
async def process_input_and_output(data: InputData):
    try:
        user_input = data.user_input

        translated_input = translator(user_input)[0]['translation_text']
        headers = {"Authorization": f"Bearer {API_TOKEN}"}
        model_data = {"inputs": translated_input}

        output_response = requests.post(API_URL, headers=headers, json=model_data)

        if output_response.status_code == 200:
            result = output_response.json()
            rounded_result = round_recursive(result)
            print(rounded_result)
            return {"output": rounded_result}
        else:
            return {"error": f"Error from model server: {output_response.status_code}"}

    except KeyError:
        return {"error": "Input not provided."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def round_recursive(item):
    if isinstance(item, (int, float)):
        return "{:.2f}".format(item * 100).zfill(5)
    elif isinstance(item, list):
        return [round_recursive(sub_item) for sub_item in item]
    elif isinstance(item, dict):
        return {key: round_recursive(value) for key, value in item.items()}
    else:
        return item

MODEL = "gpt-3.5-turbo"
SUMMARY_PROMPT = '''
'''
MAX_LEN = 1024

def callGPT(prompt):
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        temperature=0,
    )
    return response

@app.post("/gpt-summary")
async def generate_summary(data: InputData):
    try:
        user_input = data.user_input
        prompt = SUMMARY_PROMPT + user_input
        response = callGPT(prompt)
        return {"summary": response.choices[0].text.strip()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
