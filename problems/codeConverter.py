import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.environ.get("API_KEY"))

model = genai.GenerativeModel('gemini-1.5-flash')

code = '''n = 5
for i in range(n):
    print(" "*(n-i) + "* "*(i+1))'''
language = "javascript"
prompt = f"Convert this code {code} to {language}"

response = model.generate_content(prompt)

if response and response.candidates:
    converted_code = response.candidates[0].content.parts[0].text
    print(converted_code)
else:
    print("No valid response received.")