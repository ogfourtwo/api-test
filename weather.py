import requests
import json

api_key = 'your_api_key_here'

city = input('enter city name: ')
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

response=requests.get(url)

if response.status_code == 200:
    data = response.json()
    temp = data['main']['temp']
    feel = data['main']['feels_like']
    dsc = data['weather'][0]['description']
    hum = data['main']['humidity']
    print(f'The temperature is {temp} C but feels like {feel} C.')
    print(f'{dsc.capitalize()} with a humidity of {hum}')

    with open('weather_res.json','w') as file:
        json.dump(data, file)

else:
    print('could not fetch data')