from os import path
#  Задача 1 *************************************
print('\n Задача 1, решение через декоратор-итератор :-)')
num = True
def iterator(func):
    def wrapper(n):
        for i in range (1,n):
            print(' ', end='')
            global num
            num = True
            func(i)
            if num == True:
                print(i, end='')
    return wrapper

@iterator
def five(x):
    global num
    if (x % 3 == 0):
        print('Fizz', end='')
        num = False
    if (x % 5 == 0):
        print('Buzz', end='')
        num = False
five (100)

print('\n Второй способ решения,короткий')
k = list(range(100))
for i in range (1,100):
    if k[i]%15==0:
        k[i]='FizzBuzz'
    elif k[i]%5==0:
        k[i]='Buzz'
    elif k[i] % 3 == 0:
        k[i] = 'Fizz'
print(k)


# Задача 2 *******************************************
print('\n Задача 2')
f = input('Введите 5-значное число')
f = f.strip()
f = f[0:5]
for i in range (0,5):
    print(str(1+i)+' цифра равна '+f[i])


# Задача 3 *******************************************
print('\n Задача 3')
arr = input('Введите члены массива через запятую:').split(',')
L=len(arr)
for i in range (0,len(arr)):
    narr=arr[i:len(arr)]
    x=narr.index(min(narr))
    m=narr[x]
    narr[x]=narr[0]
    narr[0]=m
    arr[i:len(arr)]=narr
print('Отсортированный массив: '+ str(arr))

# Задача 4 *******************************************
print('\n Задача 4\nВведите путь к файлу (Test.txt) или строку: ')
directory = input()
   # пробелы на Таб и наоборот
if path.exists(directory):
    f=open(directory, "r+", encoding="utf-8")
    print('Распознано как путь к файлу, работать будем с данными в файле\n')
    list = f.readlines()
    print (list)
    f.close()
    for i in range(0, len(list)):
        list[i]=list[i].replace('    ','StringThatWillNeverBeEnteredByUser:Boooo')   # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        list[i] = list[i].replace('\t', '    ')
        list[i] = list[i].replace('StringThatWillNeverBeEnteredByUser:Boooo', '\t')
    f = open(directory, "w", encoding="utf-8")
    print(list)
    f.writelines(list)
    f.close()
else:
    f=directory
    print('Распознано как строка, работать будем с введёнными данными\n')
    f = f.replace('    ', 'StringThatWillNeverBeEnteredByUser:Boooo')  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    f = f.replace('\t', '    ')
    f = f.replace('StringThatWillNeverBeEnteredByUser:Boooo', '\t')
    print(f)

# Задача 5 *******************************************
print('\n Задача 5')
F=input('Введите строку, мы заменим цифры на числительные: ')
d={1:' one ', 2:' two ', 3:' three ',4:' four ', 5:' five ', 6:' six ', 7:' seven ', 8:' eight ', 9:' nine ', 0:' zero '}  # Задаём словарь
for key,value in d.items():
    F=F.replace(str(key), value)
print(F)

# Задача 6 *******************************************
print('\n Задача 6\nДля заданной матрицы столбец с каким элементом Вы хотите удалить?\n')
M=[[1,2],[3,4],[5,6],[7,8],[9,10]]
i=0
n=None
m=None
for j in range (0,len(M[i])):
    for i in range(0, len(M)):
        print(M[i][j], end='  ')
    print()
k=input('Введите цифру: ')
for j in range (0,len(M[i])):
    for i in range(0, len(M)):
        if M[i][j]==int(k):
            n=i
            m=j
            S=M.pop(i)
            break
print('Искомое число находится на позиции: '+str(n)+','+str(m)+'. Удаляем столбец.\nОтвет:')

# for i in range(0, len(M)):
#     for j in range(0, len(M[i])):
#         del M[n][j]

for j in range (0,len(M[i])):
    for i in range(0, len(M)):
        print(M[i][j], end='  ')
    print()

print('\nДомашнее задание оконечено, спасибо.')
