import os

BASE_URL='https://gorest.co.in/'
BASE_PATH='public/'
VERSION='v2/'

USERS='users/'
POSTS='posts/'

def users():
    return BASE_URL+BASE_PATH+VERSION+USERS

def access_token():
    return os.getenv('access_token')

