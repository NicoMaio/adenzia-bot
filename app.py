from flask import Flask
from telepot import *

import utility
import bot

app = Flask(__name__)


@app.route('/<username>')
def hello_world(username):
    bot.send_message(username)
    print('here')
    # send message
    return 'message sent to '+username


if __name__ == '__main__':
    config = utility.read_config()
    port = config['applicationProperties']['port']
    app.run(port=port)
    bot.run()


