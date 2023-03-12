import os
import openai
import regex
import requests


os.environ[ 'chave' ] = 'chave de acesso vai aqui'
openai.api_key = os.getenv('chave')
r = openai.Completion.create(

    model="text-davinci-003",
    prompt='traduza      "{g|Encyclopedia:DC}DC{/g} 16 {g|Encyclopedia:Saving_Throw}Will save{/g} or become paralyzed with fear for 6 {g|Encyclopedia:Combat_Round}rounds{/g} or shaken for the same duration if the target succeeds at the saving throw. Targets can attempt new saving throw against frightened condition every round."',
    max_tokens=3750,
    temperature=0
)

print(r)