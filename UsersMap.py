user_map = {}


def addUser(username, chat_id):
    user_map[username] = chat_id


def findUser(user_map, username):
    return user_map[username]
