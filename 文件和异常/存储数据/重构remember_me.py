import json

def get_stored_username():
    """如果储存了用户名，就获取它"""
    filename = 'username.json'

    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def greet_user():
    '''问候用户，并指出其名字'''
    username = get_stored_username()
    if username:
         print("Welcome back, " + username + "!")
    else:
        username = input("What's your name?")
        with open('username.json', 'w') as f_obj:
            json.dump(username, f_obj)
            print("We'll remember you when you come back, " + username + "!")



greet_user()
