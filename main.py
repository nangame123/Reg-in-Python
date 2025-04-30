import time
import os
import random as rd
import hashlib
from setings import *

def new_user_file():
    if not os.path.exists('users.txt'):
        with open('users.txt', 'w'):
            pass

def new_user(login: str, password: str) -> bool:
    with open('users.txt', 'r') as f:
        users = f.read().splitlines()

    for user in users:
        args = user.split(':')
        if login == args[0]:
            return False

    with open('users.txt', 'a') as f:
        f.write(f'{login}:{password}\n')
    return True

def get_user(login: str, password: str) -> bool:
    with open('users.txt', 'r') as f:
        users = f.read().splitlines()

    for user in users:
        args = user.split(':')
        if login == args[0] and password == args[1]:
            return True
    return False


def main(login: str):
    p(f'Привет, {login}!')

new_user_file()

login = input('Логин: ')
password = input('Пароль: ')
password_repeat = input('Повторите пароль:' )

if password != password_repeat:
    p('Пароли не совпадают!')
    #continue
result = new_user(login, hashlib.sha256(
    password.encode()).hexdigest())  # Вызываем функцию добавления пользователя. И хешируем пароль(безопасность)
if not result:
    p('Пользователь уже существует')
else:
    p('Регистрация успешно!')

