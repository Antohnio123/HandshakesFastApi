# Написать программу, которая уничтожает файлы и папки по истечении заданного времени.
# Вы указываете указываете  при запуске программы путь до директории, за которой нашему скрипту необходимо следить.
# После запуска программа не должна прекращать работать, пока вы не остановите ее работу с помощью Ctrl+C (подсказка:
# для постоянной работы программы необходим вечный цикл, например, "while True:", при нажатии Ctrl+C автоматически
# остановится любая программа). Программа следит за объектами внутри указанной при запуске папки и удаляет их тогда,
# когда время их существования становится больше одной минуты для файлов и больше двух минут для папок (то есть дата
# создания создания отличается от текущего момента времени больше чем на одну/две минуты). Ваш скрипт должен смотреть
# вглубь указанной папки. Например, если пользователь создаст внутри нее папку, внутри нее еще одну, а внутри внутри этой
# какой-то файл, то этот этот файл должен удалиться первым (так как файлу положено жить только одну минуту, а папкам
# две). Вам понадобятся библиотеки os и shutil. Внимательно перечитайте задание и учтите возможные ошибки.

# Решение:  создаём словарь, в котором ключ - имя папки/файла, значение - время создания. Такой же словарь для файлов.
# В вечном цикле сверяем с текущим временем ключи и если разница больше заданной - удаляем строки словаря И соответствющий файл/папку.
# В этом же цикле проверяем появление новых папок и файлов, елси появились - добавляем их в словарь с ключом, равным времени появления.
# https://dev-gang.ru/article/python-vvedenie-v-modul-os-ojxgrmcxi3/
# http://timgolden.me.uk/python/win32_how_do_i/watch_directory_for_changes.html
# https://python.su/forum/topic/14946/?page=1#post-89574


import os
import shutil
import datetime
import time
ltime = 2             # Время между проверками в секундах
dirtime = 12           # Время жизни папок в секундах
ftime = 6             # Время жизни файлов в секундах
Ddict = dict(one=1)
Fdict = dict(two=2)


dir = input("Введите полный путь с именем тестовой директории:  ")
#     C:\Users\Anton\.PyCharmCE2019.3\config\scratches\Testdir
if os.path.exists(dir):
    pass
else:
    os.makedirs(dir)

while True:
    time.sleep(ltime)
    for root, dirs, files in os.walk(dir):                   # scandir или walk
            for d in dirs:
                if d not in Ddict:
                    Ddict[d] = datetime.datetime.now()
                Lifetime = datetime.datetime.now() - Ddict[d]
                if d in Ddict and Lifetime.seconds > dirtime:
                    for element in os.scandir(dir):
                        if element.is_dir():
                            if element.name == d:
                                shutil.rmtree(element, ignore_errors=True)                      # Если папка не пустая, удаляем её вместе со всеми файлами и подпапками!
                    del Ddict[d]
                    print (d + "  directory was deleted")
                for f in files:
                    if f not in Fdict:
                        Fdict[f] = datetime.datetime.now()
                    Lifetime = datetime.datetime.now() - Fdict[f]
                    if f in Fdict and Lifetime.seconds > ftime:
                        # print(os.path.dirname(f))
                        # os.chdir(os.path.dirname(f))
                        # os.remove(f)
                        for files in os.walk(dir):
                            for F in files:
                                if F == f:
                                    print(os.path.dirname(F))
                                    os.chdir(os.path.dirname(F))
                                    os.remove(F)                     # Строка успешно проходится, но файл по-прежнему на месте!
                                    print(f + "  file was deleted")
                        del Fdict[f]








# Версия, работающая норм, но на первом уровне только:
# while True:
#     time.sleep(ltime)
#     for root, dirs, files in os.walk(dir):                   # scandir или walk
#         for f in files:
#             if f not in Fdict:
#                 Fdict[f] = datetime.datetime.now()
#             Lifetime = datetime.datetime.now() - Fdict[f]
#             if f in Fdict and Lifetime.seconds > ftime:
#                 for element in os.scandir(dir):
#                     if element.is_file():
#                         if element.name == f:
#                             os.remove(element)
#                 del Fdict[f]
#
#         for d in dirs:
#             if d not in Ddict:
#                 Ddict[d] = datetime.datetime.now()
#             Lifetime = datetime.datetime.now() - Ddict[d]
#             if d in Ddict and Lifetime.seconds > dirtime:
#                 for element in os.scandir(dir):
#                     if element.is_dir():
#                         if element.name == d:
#                              shutil.rmtree(element)                              # Если папка не пустая, удаляем её вместе со всеми файлами и подпапками!
#                 del Ddict[d]


