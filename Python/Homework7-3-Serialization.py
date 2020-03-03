# Создать класс Human с 5-10 атрибутами (имя, фамилия, возраст, меcто жительства и т.д.). Написать функцию, которая
# создавала бы указанное количество экземпляров, сериализовывала их и сохраняла в файл human.data,
# и другую функцию, которая бы читала файл human.data, десериализовывала его содержимое и выводила результат на печать.
# Примечание:чтоб у экземпляров Human были разные значения атрибутов, можно воспользоваться воспользоваться функциями
# random.randint и  random.choice.

import random
import pickle
NameSeq = ("Andrew", "Alex", "John", "Ivan", "Judy", "Mark", "Manny", "Bob", "Peter", "Kate")
SurnameSeq = ("Peters", "Boldowin", "Black", "Blue", "Red", "Myers", "Pitt", "Dalton", "Kim")
BSeq = ("Moscow", "London", "Paris", "Prohorovka", "Kozmodemyansk", "Mexico", "North Pole", "Syktywkar", "Washington", "Madrid")
LivingSeq = ("Glasgow", "London", "Barcelona", "Moscow", "Rome", "San Francisco", "Memphis", "New York", "Kanberra")
CompSeq = ("Pepsi", "Mars", "Toyota", "AutoVAZ", "KamAZ", "Spartak FC", "Zenit FC", "Almaz", "NefteGaz", "GazMyas")
JobSeq = ("Engineer", "Marketolog", "Dentist", "Accounter", "Chief Manager", "Manager", "PR Specialist")
class Human:
    Name = "Unknown"
    Surname = "Unknown"
    Age = 0
    Birthplace = "Unknown"
    Livingplace = "Unknown"
    Company = "Unknown"
    JobTitle = "Unknown"
    Salary = 0
    def __init__ (self):
        self.Name = random.choice(NameSeq)
        self.Surname = random.choice(SurnameSeq)
        self.Age = random.randint(20,70)
        self.Birthplace = random.choice(BSeq)
        self.Livingplace = random.choice(LivingSeq)
        self.Company = random.choice(CompSeq)
        self.JobTitle = random.choice(JobSeq)
        self.Salary = random.randint(50000,150000)
    def info (self):
        print("Имя: {}. Фамилия: {}. Возраст: {}. Место рождения: {}. Место жительства: {}. Компания: {}. Должность: {}. Оклад: {}."
              .format(self.Name,self.Surname,self.Age,self.Birthplace,self.Livingplace,self.Company, self.JobTitle, self.Salary))

def Pack ():
    number = int(input("Введите число создаваемых персон "))
    persons = []
    with open ("human.data", "wb") as file:
        for i in range (0,number):
            man = Human()
            persons.append(man)
        pickle.dump(persons, file)


def Unpack ():
    file_path = input('Введите путь к файлу или просто нажмите Enter, чтобы открыть human.data:  ')
    if file_path == "":
        # global file_path
        file_path = "human.data"
    with open (file_path, "rb") as file:             # Пытался расшифровывать по 1 строке, как запаковывал, но Питон не даёт итерироваться по строкам файла
        persons = pickle.load(file)
        for i in persons:
            i.info()    #   Не удается нормально вывести на печать: либо ошибки, либо просто Human object по адресу такому-то...
        # with open (persons, "r+"):
        #     for args in persons.args():
        #         print (args)

Pack ()
Unpack ()




