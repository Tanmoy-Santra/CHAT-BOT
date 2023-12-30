
import json

def read_credentials():
    with open('D:\main.json', 'r') as file:
        data = json.load(file)
        return data.get('user_credentials', {})
def login(username, password):
    user_credentials1=read_credentials()
    if username in user_credentials1 and user_credentials1[username] == password:
        return True
    return False



