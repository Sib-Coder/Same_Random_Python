# Проект таймер
import time

dn = 0 + int(input("Введите колличество дней: "))
ch = 0 + int(input("Введите колличество часов: "))
min = 0 + int(input("Введите колличество минут: "))


def timering(minutes, chas, dni):
    ful_minutes = minutes + chas * 60 + dni * 24 * 60
    while ful_minutes > 0:
        time.sleep(60)
        ful_minutes -= 1
        if (ful_minutes == 0):
            print("Время кончилось детка")


timering(min, ch, dn)
