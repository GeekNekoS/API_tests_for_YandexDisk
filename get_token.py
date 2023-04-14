from requests_oauthlib import OAuth2Session
from settings import *


client_id = os.environ["CLIENT_ID"]
client_secret = os.environ["CLIENT_SECRET"]
auth_url = "https://oauth.yandex.ru/authorize"
token_url = "https://oauth.yandex.ru/token"


def get_token():
    oauth = OAuth2Session(client_id=client_id)
    authorization_url, state = oauth.authorization_url(auth_url, force_confirm="true")
    print("Перейдите по ссылке, авторизуйтесь и скопируйте код:", authorization_url)
    code = input("Вставьте одноразовый код для получения токена: ")
    token = oauth.fetch_token(token_url=token_url, code=code, client_secret=client_secret)
    print(token["access_token"])


get_token()
