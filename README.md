# Reg-in-Python

Спасибо всем, кто посетил эту страницу. Я рад, что это мой первый проект, о котором я опубликовал статью github.com.
Я надеюсь, что я был полезен.

## Как создать новый файл в Python 


    if not os.path.exists('users.txt'):
        with open('users.txt', 'w'):
            pass
            
---------------

## Проверка на наличие логина


    for user in users:
        args = user.split(':')
        if login == args[0]:  
            return False 
            
--------------
## Добавление пользователя


    with open('users.txt', 'a') as f:
        f.write(f'{login}:{password}\n') 
    return True
