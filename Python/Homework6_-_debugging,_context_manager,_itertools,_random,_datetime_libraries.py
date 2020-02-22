import datetime
import time
import random
import itertools
print ("\n Задача 1.")
def chargen():
    # while True:    - лишний элемент, зацикливающий на вечно генератор, не даёт yield выйти на корневой уровень
    for c in '0123456789':
        yield c
words = [c+c for c in chargen()]
print(str(words))
#************************************************************
print ("\n Задача 2.")
# В данном случае enumerate является излишним, так как он работает с индексами членов массива,
# а нам нужны только их значения. Кроме того, переменная result - лишняя.

def multiplier2 (m=1, source=[1,2,3]):
    for i in range(len(source)):
        source[i] = m * source[i]
    return source
print(multiplier2 (5))
print(multiplier2 (12, [1,2]))

#************************************************************
print ("\n Задача 3.")
class Timer:
    t1=0
    def __enter__(self):
        self.t1=datetime.datetime.now()
    def __exit__(self, exc_type, exc_val, exc_tb):
        t2 = datetime.datetime.now()
        print("Время внутри таймера = "+str(t2-self.t1))

with Timer():
    time.sleep(random.randint(1, 3))

#************************************************************
print ("\n Задача 4.******************************************")
print ("\n Функция 1.")
list1=[1,2,3]
list2=[4,5]
list3=[6,7]
Superlist=list(itertools.chain(list1,list2,list3))
print(Superlist)
# #************************************************************
print ("\n Функция 2.")
def MoreThan4(x):
    return len(x)<5
enter=['hello','i', 'write','cool','code']
print(list(itertools.filterfalse(MoreThan4,enter)))

#************************************************************
print ("\n Функция 3.")
iterable='password'
r=4
for item in itertools.combinations_with_replacement(iterable, r):
    print(''+str(item))