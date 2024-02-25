import requests
import pprint
with open("token.txt") as f:
    token = f.read()

# endPoint = f"https://api.telegram.org/bot{token}/getUpdates"
# param = {'offset': - 1}
# response = requests.get(endPoint, params=param).json()
# pprint.pprint(response)
## offset работает как срезы в питоне
# a = [1,2,3,4,5,6,7,8]
# print(a[-1:])

def givePhoto(date: str):
    endPoint = 'https://api.nasa.gov/planetary/apod'
    params = {'api_key': 'DEMO_KEY', 'date': date}
    res = requests.get(endPoint, params=params).json()
    explanation = res['explanation']
    urlPhoto = res['url']
    return (urlPhoto, explanation)
# print(explanation)
# print(urlPhoto)
# endPoint = f"https://api.telegram.org/bot{token}/getUpdates"
# res = requests.get(endPoint)
# pprint.pprint(res.json())
#получить информацию по всем событиям (апдейтам)
endPoint = f"https://api.telegram.org/bot{token}/getUpdates"
params = {'offset': -1}
response = requests.get(endPoint, params=params).json()
pprint.pprint(response)

import time
offset = -2
while True:
    # getMe
    endPoint = f"https://api.telegram.org/bot{token}/getUpdates"
    param = {'offset': offset + 1}
    response = requests.get(endPoint, params=param).json()
    if response['result']:
        offset = response['result'][0]['update_id']
        userText = response['result'][0]['message']['text']
        chatID = response['result'][0]['message']['chat']['id']
        photoURL, photoExp = givePhoto(userText)
        endPoint = f"https://api.telegram.org/bot{token}/sendPhoto"
        params = {'chat_id': chatID, 'photo': photoURL}
        res = requests.get(endPoint, params=params)
        #pprint.pprint(response)
        endPoint = f"https://api.telegram.org/bot{token}/sendMessage"
        params = {'chat_id': chatID, 'text': photoExp}
        res = requests.get(endPoint, params=params)
        # endPoint = f"https://api.telegram.org/bot{token}/sendMessage"
        # params = {'chat_id': chatID, 'text': userText}
        # res = requests.get(endPoint, params=params)
    time.sleep(1)


# response = requests.get(endPoint).json()['result']
# userText = response[0]['message']['text']
# chatID = response[0]['message']['chat']['id']
# pprint.pprint(response)

# userinfo = dict()
# for i in response:
#     chatID = i['message']['chat']['id']
#     userName = i['message']['chat']['first_name']
#     if 'text' in i['message']:
#         userText = i['message']['text']
#     userinfo[chatID] = [userName, userText]
#
#
# print(userinfo)
# # Отправить сообщение в чат
# endPoint = f"https://api.telegram.org/bot{token}/sendMessage"
# for user in userinfo:
#     mes = f'Привет, {userinfo[user][0]}'
#     params = {'chat_id': chatID, 'text': mes}
#     res = requests.get(endPoint, params=params)


# endPoint = f"https://api.telegram.org/bot{token}/getUpdates"
# res = requests.get(endPoint).json()
# pprint.pprint(res)
# chatID = res['result'][0]['message']['chat']['id']

# # User_name = res['result'][0]['message']['chat']['id']['first_name']

# print(chatID)
# endPoint = f"https://api.telegram.org/bot{token}/sendMessage"
# params = {'chat_id': chatID, 'text': 'Привет, как дела?!'}
# res = requests.get(endPoint, params=params).json()
