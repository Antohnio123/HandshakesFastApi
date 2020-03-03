# В задаче не говорится сделать СВОЙ метод, свою реализацию...  не запрещено использовать существующий метод .count
# def count_symbol(string, sym):
#     res=string.count(sym)
#     return res
# Если всё-таки нужно свою реализацию, то вот так:-----------------------------------------
def count_symbol(string, sym):
    L=list(string)
    res=0
    for n in L:
        if n ==sym:
            res+=1
    return res
# Код закончен, теперь проверка: ------------------------------------------------------------

s = " a sdgdhgdhrthn,la sndgklja nga sgfa smndgksdg"
print(count_symbol(s, 'a'))
