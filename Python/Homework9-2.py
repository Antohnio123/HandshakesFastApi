import multiprocessing

a = "Это строка"
b = "Это тоже строка"
c = "... и даже это - тоже строка"
x = 0.32561636351
y = 12358.02
z = 56398
L=[1,2,453,35,1134,34656,45,54,64,6,23,234,245,2,52,5,235,235,2,5,3,2345]
K=[23,34,2345,5,5,64,554,345,3245,6,457,9,89,6,6,56,7,345,636,3,645,645]
M=[3,242,52,53,4,4567,6767,87,79,89,87,67,67,76,87,67,56,56,7456,7,45,323,21311,45]


def Sum (*args):
    Integer = False
    List = False
    String = False
    for arg in args:
        if isinstance(arg, int):
            Integer = True
        elif isinstance(arg, str):
            String = True
        elif isinstance(arg, list):
            List = True
    Res = 0
    if Integer == False and String==True and List==False:
        Res = ''
    elif Integer == False and String == False and List == True:
        Res = []
    for arg in args:
        Res += arg
    print(Res)
    return Res


if __name__ == '__main__':
    print("Начинаем мультипроцессинговый расчёт")
    m1 = multiprocessing.Process(target = Sum, args=(a,b,c))
    m2 = multiprocessing.Process(target = Sum, args=(x,y,z))
    m3 = multiprocessing.Process(target = Sum, args=(K,L,M))
    m1.start()
    m2.start()
    m3.start()
    m1.join()
    m2.join()
    m3.join()

