
users_map = {}


def send_helper(chat_id, bot):
    bot.sendMessage(chat_id, 'write /signup to sign up on notify service')


def signup(chat_id, name, bot):
    if name not in users_map.keys():
        users_map[name] = chat_id
        bot.sendMessage(chat_id, 'correctly signed up')
    else:
        bot.sendMessage(chat_id, 'already signed up')


def send_message_op(bot, username):
    if username in users_map.keys():
        bot.sendMessage(users_map[username], "hai un nuovo incarico!")
    else: 
        print("username: "+username+" not signed")
