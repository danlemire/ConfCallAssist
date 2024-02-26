import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()



genai.configure(api_key=os.environ['GEMINI_API_KEY'])

model = genai.GenerativeModel('gemini-pro')
response = model.generate_content('what is the capital of Texas?')

print(response.text)