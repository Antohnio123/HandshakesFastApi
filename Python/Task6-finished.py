def myformat (string, *args):
    simple = False
    numerate = False
    class WrongPositions(Exception):
        pass
    def Poscheck():
        if simple == numerate == True:
            raise WrongPositions()

    if not isinstance(string, str):
        print("Введённые аргументы не являются строками, передайте строки в функцию.")
        return (1)
    A=list(args)
    S=list(string)                  # Перевели строку в лист знаков
    Pos = []
    i=0
    while "{" in S and "}" in S:
        Ind1 = S.index('{')
        Ind2 = S.index('}')
        # print(str(Ind1)+ "  " + str(Ind2))              # Проверка 1 - индексы
        p = ''.join((S[Ind1:(Ind2 + 1)]))
        # print(p)                                # Проверка 2
        if p == "{}":
            simple = True
            try:
                Poscheck()
            except WrongPositions:
                print(
                    "В строке пристутствуют нумерованные и простые позиции, должно быть что-то одно, программа закрывается.")
                exit(code=1)
            S[Ind1:(Ind2 + 1)] = A[i]
            i+=1
        k = p.replace("{", "")
        k = k.replace("}", "")
        if k.isdigit():
            numerate = True
            try:
                Poscheck()
            except WrongPositions:
                print(
                    "В строке пристутствуют нумерованные и простые позиции, должно быть что-то одно, программа закрывается.")
                exit(code=1)
            S[Ind1:(Ind2 + 1)] = A[int(k)]
    Res = ''.join(S)
    return Res
# Код завершён!  Ниже - проверка --------------------------------------------------------------------------

s = "dfghdhsh {} jfsfjh {} shgs {} hsg   hfdgdfg"
print(s.format('AAAA', 'BBBB', 'CCCC', 'DDDD'))
print(myformat(s, 'AAAA', 'BBBB', 'CCCC', 'DDDD'))
