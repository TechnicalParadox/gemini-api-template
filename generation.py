import google.generativeai as genai
import os
from google.generativeai.types import HarmCategory, HarmBlockThreshold

from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.environ.get('API_KEY'))
PRO_MODEL = 'gemini-1.5-pro-latest'
NO_SAFETY = {
    HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
    HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
    HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
    HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE
}

sys_instructions = 'You are an expert storyteller.'
prompt = 'Write a short story.'

model = genai.GenerativeModel(model_name=PRO_MODEL, safety_settings=NO_SAFETY, system_instruction=sys_instructions)
response = model.generate_content(prompt)
print(response.text)