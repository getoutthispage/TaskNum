import time

interval = int(input("Введите промежуток времени в днях"))
print(str(interval * 24) + " Часов " + str((interval * 24) * 60) + " Минут " + str(
    ((interval * 24) * 60) * 60) + " Секунд")
input()