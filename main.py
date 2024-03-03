import requests
import json
import pprint
with open("token.txt") as f:
    token = f.read()


def giveAnimation(answer: str) -> str:
    endPoint = f'https://yesno.wtf/api?force={answer}'
    res = requests.get(endPoint).json()
    return res['image']
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile

# Создаем объекты бота и диспетчера
bot = Bot(token=token)
dp = Dispatcher()


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')

# Этот хэндлер будет срабатывать на команду "/help"
@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(
        'Напиши мне что-нибудь и в ответ '
        'я пришлю тебе твое сообщение'

    )

def checkMsg(message: Message) -> bool:
    res = False
    with open('banWords.txt', encoding='utf-8') as f:
        banWords = f.read().split()
    userText = message.text.split()
    for word in userText:
        if word in banWords:
            res = True
        if message.text:
            userText = message.text.split()
            for word in userText:
                if word in banWords:
                    res = True
        return res
def banFilter(userText: str) -> str:
    with open('banWords.txt', encoding='utf-8') as f:
        banWords = f.read().split()
    filteredMes = userText
    for word in userText.split():
        if word in banWords:
            filteredMes = filteredMes.replace(word, "*" * len(word))
    return filteredMes

@dp.message(checkMsg)
async def process_ban(message: Message):
    await message.answer(text="Так нельзя!")
    photo = FSInputFile('img/1.jpg')
    textReplace = (f'{message.from_user.first_name} просил передать: \n'
                   f'<i>{banFilter(message.text)}</i>')
    await message.delete()
    #await message.answer(userText="****")
    #await message.delete()

    await bot.send_photo(chat_id=message.from_user.id, photo=photo)
    await bot.send_message(chat_id=message.from_user.id, text=textReplace, parse_mode='HTML')
@dp.message(lambda message: message.text == "Как дела?")
async def process_dela(message: Message):
    await message.answer(text="Нормально")

# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения,
# кроме команд "/start" и "/help"
@dp.message()
async def send_echo(message: Message):
    print(message.model_dump_json(indent=4, exclude_none=True))
    # exclude_none = True в print только те которые не null
    await message.send_copy()
#    await message.reply(text=message.text)


if __name__ == '__main__':
    dp.run_polling(bot) #бесконечный цикл по получению аптейдов сервера Telegram

# import time
# offset = -2
# while True:
#     #получить информацию по всем событиям (апдейтам)
#     endPoint = f'https://api.telegram.org/bot{token}/getUpdates'
#     param = {'offset': offset + 1}
#     response = requests.get(endPoint, params=param).json()
#     if response['result']:
#         offset = response['result'][0]['update_id']
#         userText = response['result'][0]['message']['text']
#         chatID = response['result'][0]['message']['chat']['id']
#
#         endPoint = f'https://api.telegram.org/bot{token}/sendAnimation'
#         params = {'chat_id': chatID, "animation": giveAnimation(userText)}
#         res = requests.get(endPoint, params=params)
#         pprint.pprint(response['result'])

# import requests
# import pprint
# with open("token.txt") as f:
#     token = f.read()
#
# def giveAnimation(answer: str) -> str:
#     endPoint = f'https://yesno.wtf/api?force={answer}'
#     res = requests.get(endPoint).json()
#     return res['image']
#
# import time
# offset = -2
# while True:
#     #получить информацию по всем событиям (апдейтам)
#     endPoint = f'https://api.telegram.org/bot{token}/getUpdates'
#     param = {'offset': offset + 1}
#     response = requests.get(endPoint, params=param).json()
#     if response['result']:
#         offset = response['result'][0]['update_id']
#         userText = response['result'][0]['message']['text']
#         chatID = response['result'][0]['message']['chat']['id']
#         userText = 'yes'
#         endPoint = f'https://api.telegram.org/bot{token}/sendAnimation'
#         params = {'chat_id': chatID, "animation": giveAnimation(userText)}
#         res = requests.get(endPoint, params=params)
#         pprint.pprint(response['result'])
#
#
#
#     time.sleep(1)


# endPoint = f"https://api.telegram.org/bot{token}/getUpdates"
# param = {'offset': - 1}
# response = requests.get(endPoint, params=param).json()
# pprint.pprint(response)
## offset работает как срезы в питоне
# a = [1,2,3,4,5,6,7,8]
# print(a[-1:])


# def givePhoto(date: str):
#     endPoint = 'https://api.nasa.gov/planetary/apod'
#     params = {'api_key': 'DEMO_KEY', 'date': date}
#     res = requests.get(endPoint, params=params).json()
#     explanation = res['explanation']
#     urlPhoto = res['url']
#     return (urlPhoto, explanation)
# # print(explanation)
# # print(urlPhoto)
# # endPoint = f"https://api.telegram.org/bot{token}/getUpdates"
# # res = requests.get(endPoint)
# # pprint.pprint(res.json())
# #получить информацию по всем событиям (апдейтам)
# endPoint = f"https://api.telegram.org/bot{token}/getUpdates"
# params = {'offset': -1}
# response = requests.get(endPoint, params=params).json()
# pprint.pprint(response)
# def checkDate(date: str) -> bool:
#     if len(date) != 10:
#         return False
#     lst = date.split('-')
#     if len(lst) != 3:
#         return False
#     if not all([len(lst[0]) == 4, len(lst[1]) == 2, len(lst[2]) == 2]):
#         return False
#     for item in lst:
#         if not all(map(lambda x: x.isdigit(), item)):
#             return False
#     year, month, day = int(lst[0]), int(lst[1]), int(lst[2])
#     if not all([2000 <= year <= 2024, 1 <= month <= 12, 1 <= day <= 31]):
#         return False
#     return True
#
# import time
# offset = -2
# while True:
#     # getMe
#     endPoint = f"https://api.telegram.org/bot{token}/getUpdates"
#     param = {'offset': offset + 1}
#     response = requests.get(endPoint, params=param).json()
#     if response['result']:
#         offset = response['result'][0]['update_id']
#         userText = response['result'][0]['message']['text']
#         chatID = response['result'][0]['message']['chat']['id']
#         if checkDate(userText):
#             photoURL, photoExp = givePhoto(userText)
#             endPoint = f"https://api.telegram.org/bot{token}/sendPhoto"
#             params = {'chat_id': chatID, 'photo': photoURL}
#             res = requests.get(endPoint, params=params)
#             #pprint.pprint(response)
#             endPoint = f"https://api.telegram.org/bot{token}/sendMessage"
#             params = {'chat_id': chatID, 'text': photoExp}
#             res = requests.get(endPoint, params=params)
#         else:
#             endPoint = f"https://api.telegram.org/bot{token}/sendMessage"
#             params = {'chat_id': chatID, 'text': 'Нужна дата в формате ГГГГ-ММ-ДД'}
#             res = requests.get(endPoint, params=params)
#     time.sleep(1)


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
