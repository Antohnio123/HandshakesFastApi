import time
import random
import tempfile
import os
# Задача 1*****************************************
print ("\n Задача 1.")
class Man:
    def __init__(self, name):
        self.name = name
    def Solve_task(self):
        print ("I'm not ready yet :-)")
John = Man("John")
John.Solve_task()


# Задача 2*****************************************
print ("\n Задача 2.")
random.seed()
class Pupil (Man):
    def Solve_task(self):
        time.sleep(random.randint(3,6))
        print ("I'm not ready yet :-)")
Dave = Pupil("Dave")
print ("Dave, solve this problem, please")
Dave.Solve_task()

# Задача 3*****************************************
print ("\n Задача 3.")
class WrapStrToFile(object):
    TMPFile = None
    filepath = None
    Str = ""
    def __init__(self):
        self.Str = "тут должна была быть ошибка, но с функцией mstemp ошибки не бывает." \
                       "Бывает пустой файл. \n Но так как я написал эту строку, файл будет содежать как минимум её"
        self.TMPFile, self.filepath =tempfile.mkstemp()


    @property
    def content(self):
        try:
            f = open(self.filepath, "r+", encoding="utf-8")
            self.Str = f.read()
            os.close(self.TMPFile)
            return(self.Str)
        except FileNotFoundError:
            print ("File doesn't exist")
    @content.setter
    def content (self, value):
        with open (self.filepath, "r+", encoding="utf-8") as f:
            f.write (str(value))
            f.close()
    @content.deleter
    def content(self):
        os.remove(self.filepath)
        print ("Временный файл удалён")

WSTF = WrapStrToFile()
print (WSTF.content)
WSTF.content = 'test str'
print (WSTF.content)
WSTF.content = 'text 2'
print (WSTF.content)
del WSTF.content









