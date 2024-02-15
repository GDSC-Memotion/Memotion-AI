from openai import openai
client = OpenAI()

completion = client.chat.completions.create(
    #model = "gpt-3.5-turbo-1106",
    model="gpt-4-0613",
    
    messages=[
        {"role":"system","content":"programmer"},
        {"role":"user","content":"hey"}
    ]
)
print(completion.choices[0].message.content)