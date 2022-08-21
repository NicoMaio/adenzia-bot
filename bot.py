
#
# import
from threading import Thread

from telepot import *
import _thread
import time
import utility
import UsersMap
from ops import *

config = utility.read_config()

telegram_bot_token = config['bot']['token']

bot = Bot(telegram_bot_token)


def on_chat_message(msg):
    content_type, chat_type, chat_id = glance(msg)

    # switch sul tipo di messaggio ricevuto
    if content_type == 'text':
        username = msg["from"]["username"]
        print(msg)
        text = msg['text']
        txt = text.lower()

        # helper
        if txt == '/help' or txt == '/start':
            send_helper(chat_id, bot)

        elif text == '/signup':
            signup(chat_id, username, bot)


def send_message(username):
    send_message_op(bot, username)


class listener(Thread):
    def run(self):
        bot.message_loop(on_chat_message)


def run():
    listener().start()


run()
#
# avvio loop per gestire richieste

