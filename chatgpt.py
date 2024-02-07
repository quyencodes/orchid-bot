from openai import OpenAI
import os

client = OpenAI(
    api_key = os.environ.get("OPENAI_API_KEY")
)

def query_chatgpt(system_prompt, user_prompt):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )
    
    return completion.choices[0].message.content
