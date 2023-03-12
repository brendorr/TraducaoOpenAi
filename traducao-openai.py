import os
import openai
import regex
import requests


os.environ[ 'chave' ] = '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'
openai.api_key = os.getenv('chave')
r = openai.Completion.create(

    model="text-davinci-003",
    prompt='  traduza "16 or become paralyzed with fear for 6 or shaken for the same duration if the target succeeds at the saving throw. Os alvos podem tentar um novo lançamento salvador contra a condição de medo a cada assustado"', 
    max_tokens=3750,
    temperature=0
)

print(r)