# Reg-in-Python

Спасибо всем, кто посетил эту страницу. Я рад, что это мой первый проект, о котором я опубликовал статью github.com.
Я надеюсь, что я был полезен.

## Как создать новый файл в Python 
Чтобы сделать это, вам нужно:


    if not os.path.exists('users.txt'):
        with open('users.txt', 'w'):
            pass
            
---------------

## Проверка на наличие логина
Чтобы сделать это, вам нужно:


    for user in users:
        args = user.split(':')
        if login == args[0]:  
            return False 
