# -*- coding: utf-8 -*-

import requests
from fastapi import FastAPI
from transformers import pipeline

app = FastAPI()

API_URL = "https://api-inference.huggingface.co/models/tae898/emoberta-large"
API_TOKEN = "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"

translator = pipeline("translation", model="Helsinki-NLP/opus-mt-fr-en")

@app.post("/emotion")
async def process_input_and_output(data: dict):
    try:
        user_input = data["input"]

        # 번역된 입력을 사용하여 추론 수행
        translated_input = translator(user_input)[0]['translation_text']
        headers = {"Authorization": f"Bearer {API_TOKEN}"}
        model_data = {"inputs": translated_input}

        # 서버로 요청을 보내고 결과를 처리
        output_response = requests.post(API_URL, headers=headers, json=model_data)

        if output_response.status_code == 200:
            result = output_response.json()
            
            # 결과를 반올림 처리
            rounded_result = round_recursive(result)
            print(rounded_result)

            # 반올림된 결과 반환
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
