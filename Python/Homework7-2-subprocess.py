# С помощью библиотеки subprocess прочитать содержимое произвольного файла с использованием утилиты cat в Linux или
# type в Windows (имя файла должно передаваться как в вашу функцию)

import subprocess
def TypeOpen(name):
    command = "Type "+str(name)
    subprocess.call(command, shell=True)
    print("\nOpened  " + str(name))
Name = input("Введите полный путь к файлу: ")
TypeOpen(Name)


# subprocess.call("C:\Windows\system32\cmd.exe")
# program = "notepad.exe"
# subprocess.Popen("%s %s" % (program, name))   # - работающий код с любой простой программой, но не с cmd

# C:\Users\Anton\.PyCharmCE2019.3\config\scratches\Test-7-2-Subprocess.txt   - путь к файлу.