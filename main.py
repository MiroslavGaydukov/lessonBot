import requests
import pprint
with open("token.txt") as f:
    token = f.read()
# getMe
endPoint = f"https://api.telegram.org/bot{token}/getUpdates"
response = requests.get(endPoint).json()['result']
pprint.pprint(response)

userinfo = dict()
for i in response:
    chatID = i['message']['chat']['id']
    userName = i['message']['chat']['first_name']
    if 'text' in i['message']:
        userText = i['message']['text']
    userinfo[chatID] = [userName, userText]


print(userinfo)
# Отправить сообщение в чат
endPoint = f"https://api.telegram.org/bot{token}/sendMessage"
for user in userinfo:
    mes = f'Привет, {userinfo[user][0]}'
    params = {'chat_id': chatID, 'text': mes}
    res = requests.get(endPoint, params=params)

# endPoint = f"https://api.telegram.org/bot{token}/getUpdates"
# res = requests.get(endPoint).json()
# pprint.pprint(res)
# chatID = res['result'][0]['message']['chat']['id']

# # User_name = res['result'][0]['message']['chat']['id']['first_name']

# print(chatID)
# endPoint = f"https://api.telegram.org/bot{token}/sendMessage"
# params = {'chat_id': chatID, 'text': 'Привет, как дела?!'}
# res = requests.get(endPoint, params=params).json()
