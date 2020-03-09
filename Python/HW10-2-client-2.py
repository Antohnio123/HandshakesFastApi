import socket


class User(object):
    name = 'Unknown'
    country = 'Unknown'
    age = 0
    date_joined = '2020-01-01'
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def __init__(self, name, country, age =30, date_joined = '1990-01-01'):
        self.name = name
        self.country = country
        self.age = age
        self.date_joined = date_joined
    def introduce(self):
        L = [self.name, self.country, str(self.age), self.date_joined]
        stroka = '/'.join(L)
        self.s.send(stroka.encode())
    def info(self):
        print('User connected: name = '+str(self.name)+'. Country = '+ str(self.country) + '. Age = ' + str(self.age) + '. Date joined = '+ self.date_joined)

    def connect(self, host, port):
        self.s.connect((host, port))
        self.introduce()                     # Тут отправляем данные юзверя, сериализованные, закодированные self.s.send(pickle.dump(self.L, List).encode())
        # self.s.gettimeout()
        while True:
            ask = input('\nВведите запрашиваемое слово: ')              # Далее юзверь обслуживается на сервере
            # self.s.gettimeout()
            self.s.send(ask.encode())
            if ask.lower() == 'close':                              # Пока не введёт 'close'
                self.s.close()
                exit()
            else:
                Res = self.s.recv(1024)
                print('Ответ сервера: {}'.format(Res.decode()))
    def disconnect(self):
        self.s.close()


# user1 = User('John', 'USA', 32, '2020-03-05')
user2 = User('Helen', 'Canada', 23, '2019-01-01')
# user3 = User('Alexey', 'Russia ', 17, '2018-02-23')

# user1.connect('127.0.0.1', 53023)
user2.connect('127.0.0.1', 53023)
# user3.connect('127.0.0.1', 53023)

# user1.disconnect()
# user2.disconnect()
# user3.disconnect()