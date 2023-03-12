import openai
import regex
import os
import requests

# teste for handling multiples ssh keys

openai.api_key = os.getenv("OPENAI_API_KEY")
r = openai.Completion.create( 
  model="text-davinci-003",
  prompt="Say this is a test",
  max_tokens=7,
  temperature=0
)

print(r['choices'][0]["text"])

