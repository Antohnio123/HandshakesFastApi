class Money(object):
    value = 0.0
    USDexRate=65.31
    Rubles=True
    def __str__(self):
        A = self.value//1
        B  = self.value%1*101
        return (str(int(A))+","+str(int(B)))
    def __add__(self, other):
        self.value += other
        return self.value
    def __sub__(self, other):
        self.value -= other
        return self.value
    def __mul__(self, other):
        self.value *= other
        return self.value
    def __truediv__(self, other):
        self.value /= other
        return self.value
    def __eq__(self, other):
        return self.value==other
    def __ne__(self, other):
        return self.value != other
    def __lt__(self, other):
        return self.value < other
    def __gt__(self, other):
        return self.value > other
    def __le__(self, other):
        return self.value <= other
    def __ge__(self, other):
        return self.value >= other
    def Compare(self, other):
        if not isinstance(other, int) and not isinstance(other, float):
            print('Вы ввели не число, сравнить нельзя')
        elif self.value == other:
            print ('Значение равно ' + str(other))
        elif self.value > other:
            print('Значение больше ' + str(other))
        elif self.value < other:
            print('Значение меньше ' + str(other))
    def ChangeCurrency(self):
        if self.Rubles:
            self.value=self.value/self.USDexRate
            print('Переведено из рублей в доллары, составляет ' + self.__str__() + ' доллара(ов)')
        else:
            self.value = self.value * self.USDexRate
            print('Переведено из долларов в рубли, составляет ' + self.__str__() + ' рубля(ей)')
        self.Rubles = not self.Rubles
# Код закончен, теперь проверка: ---------------------------------------------------------------------


Salary = Money()
Salary.value = float(input('Введите сумму Значения с копейками через точку:  '))
print(Salary)
Salary+4000
print("Прибавим к Значению 4000, будет " + str(Salary))
Salary-34547
print("Вычтем из Значения 34547, будет " + str(Salary))
Salary*3
print("Умножим Значение на 3, будет " + str(Salary))
Salary/2
print("Разделим Значение на 2, будет " + str(Salary))

k = float(input("Введите число, с которым сравнить Значение:  "))
Salary.Compare(k)
print('Значение равно '+ str(k) +"?  "+ str(Salary == k))
print('Значение больше '+ str(k) +"?  "+ str(Salary >= k))
print('Значение меньше '+ str(k) +"?  "+ str(Salary <= k))

Salary.ChangeCurrency()
Salary.ChangeCurrency()