import requests
import json

word = input('Enter a word: ')

url = f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}'
response=requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(f'\"{word}\" means {data[0]['meanings'][0]['definitions'][0]['definition']}')
    print(f'It is a {data[0]['meanings'][0]['partOfSpeech']}.')
else:
    print('could not fetch data')