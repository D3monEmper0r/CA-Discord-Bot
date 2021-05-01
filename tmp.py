import requests
import sqlite3
import json

clientId = '35937'
clientSecret = 'MD-aXHuLtFMk7oJ.dqDgouG2E.OzZmSjttioK-CZmHI'

token = requests.post(f'https://www.bungie.net/en/oauth/authorize?client_id={clientId}&client_secret={clientSecret}&grant_type=authorization_code&code=SplxlOBeZQQYbYS6WxSbIA')
#oauth = 'https://www.bungie.net/en/oauth/authorize?client_id=35937&response_type=code&state=MD-aXHuLtFMk7oJ.dqDgouG2E.OzZmSjttioK-CZmHI'
apiKey = {"X-API-Key":'2a4e11c2d7b54394bbedcc1c42cfae34', 'Authorization': f'Bearer {token}'}
vendors = 'https://bungie.net/Platform/Destiny2/Vendors/?components=400'
xur = 'https://bungie.net/Platform/Destiny2/3/Profile/4611686018492295220/Character/2305843009687814087/Vendors/2190858386/?components=402'
player = 'https://bungie.net/Platform/Destiny2/SearchDestinyPlayer/3/TheD3monEmper0r/?components=200'
chars = 'https://bungie.net/Platform/Destiny2/3/Profile/4611686018492295220/?components=200'

#page = requests.get(xur, headers=apiKey).json()
#page = requests.get(player, headers=apiKey).text
#print(page['Response']['characters']['data'])
#for item in page['Response']['characters']['data']:
#    print(f'{item} \n\n')
#print(page)
print(token)