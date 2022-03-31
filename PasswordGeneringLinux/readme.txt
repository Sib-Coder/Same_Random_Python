пример создания юзеров
for (( i=101; i < 301; i++ )); do useradd -m user$i ; done

пример задания паролей
for i in $(cat text.txt); do echo $i | chpasswd; done

удаление юзеров
for (( i=1; i < 10; i++ )); do userdel -f user$i ; done

скрипт на питоне для генерации пользователей
main.py
