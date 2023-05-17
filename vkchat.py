
# короче прив это инструкция по скрипту
# шаг 1 - заходишь на ссылку
# https://oauth.vk.com/authorize?client_id=2685278&scope=1073737727&redirect_uri=https://api.vk.com/blank.html&display=page&response_type=token&revoke=1
# разрешаешь - готово
# снизу, на строке vk_session вводишь свой логин и пароль там где написано login и password
# скрипт работает через kate mobile, данные в безопасности акк я никак не взломаю

# шаг 2 - как запустить, и чтобы всегда работало?
# www.pythonanywhere.com
# в общем, регаешь там аккаунт. у тебя появляется интерфейс "Dashboard".
# сначала нажимаешь на Bash console (в разделе consoles), и вводишь туда команду pip install vk_api
# ждешь пока загрузится, потом выходишь на главную страницу (dashboard)
# потом нужно закинуть этот файл в files - (Files - Browse files), там у тебя появится этот скрипт. его нужно запустить нажатием мыши.
# готово поздравляю у вас спид

import vk_api
from vk_api.utils import get_random_id
from time import sleep

# шаг 3 - снизу вводишь пароль логин  (app_id не менять, это kate mobile, через который происходит отправка сообщений)

vk_session = vk_api.VkApi('login', 'password', app_id=2685278)
vk_session.auth(token_only=True)

vk = vk_session.get_api()

while True:
    try:
        while True:
    # шаг 4 - здесь пишешь что тебе нужно чтоб бот отправлял
    # на место chat_id пишешь чат айди (да), находится в адресной строке когда заходишь в диалог беседы
    # ну и логично что на место message пишешь сообщение которое отправить
            print(vk.messages.send(chat_id=0, message='эээ', random_id=get_random_id()))
    # шаг 5 - снизу (там где sleep) кол-во СЕКУНД которые должны пройти после сообщения.
    # лучше не делать менее 5 секунд, т.к. может сработать капча
    # https://dev.vk.com/method - тут подробно написано про все команды
            sleep(5)
    except Exception:
        # если капча все же возникла, бот остановится на 30 секунд. это значение можно поменять в sleep()
        print('error((')
        sleep(30)

