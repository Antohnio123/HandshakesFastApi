import socket
import threading

# Задачу усложнил.
# Во-первых, сервер не просто выводит данные подключённого пользователя, а создает объект класса User у себя
# под этого пользователя с его данными.  И вызывает у этого объекта метод  "Представиться" = .introduce

# Во-вторых, просто вывести данные пользователей было скучно, поэтому в коде реализована функциональность словаря
# для всех подключённых пользователей. Как в 1 задаче, все они могут задавать сервру слова для перевода и получать ответ.
# Также все пользователи могут отключаться, вводя слово 'close' и подключаться снова.  Ошибки сервреа при этом обработаны
# try - except и не выдаются.  Вместо них на сервере выводится красивое уведомление об отключении пользователя.

# И кстати, код клиента совсем не обязательно усложнять, как было в лекциях.  Тут код клиентов оставлен простым
# и прекрасно работает.

D = dict(кошка='cat', собака='dog', слон = 'elephant', птица = 'bird', рыба = 'fish', волк = 'wolf', змея = 'snake')


class User(object):
    q = 0
    name = 'Unknown'
    country = 'Unknown'
    age = 0
    date_joined = '2020-01-01'
    L=[0]
    def __init__(self, list):
        User.q += 1                     # Счётчик экземпляров юзеров в классе
        self.q = User.q
        self.name = list[0]
        self.country = list[1]
        self.age = int(list[2])
        self.date_joined = list[3]
    def introduce(self):
        print('User connected: name = '+str(self.name)+'. Country = '+ str(self.country) + '. Age = ' + str(self.age) + '. Date joined = '+ self.date_joined)

class ClientThread(threading.Thread):
    def __init__(self, conn, addr):
        super().__init__()
        self._conn = conn
        self._addr = addr
        print('Server got the connection. Address = {}'.format(self._addr))
        self.intro = self._conn.recv(1024).decode()
        self.List = self.intro.split('/')                               # Получаем представление от подключившегося клиента!!!
        self.user = User(self.List)
        self.user.introduce()
    def run (self):
        while True:
            try:
                ask = self._conn.recv(1024)
                ask = ask.decode()
                if ask.lower() == 'close':
                    self._conn.close()
                    print('Client aborted the connection. Address = {}'.format(self._addr))
                elif ask in D:
                    Res = D[ask]
                    self._conn.send('Перевод: {}'.format(Res).encode())
                else:
                    Res = 'Ошибка! Такого слова нет в словаре'
                    self._conn.send(Res.encode())
            except (OSError, ConnectionResetError) as e:
                pass

class TcpServer:
    N=5
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = None
        self. running = False
    def run (self):
        self._socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._socket.bind((self.host, self.port))
        self._socket.listen(self.N)
        self._running = True
        print('Server is running')
        while self._running:
            conn, addr = self._socket.accept()
            ClientThread(conn, addr).start()
    def stop (self):
        self._running = False
        self._socket.close()
        print('Server is down')


if __name__ == '__main__':
    srv = TcpServer(host='127.0.0.1', port=53023)
    try:
        srv.run()
    except KeyboardInterrupt:
        srv.stop()
        print('Server is stopped')



# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# host = '127.0.0.1'
# port = 53023
# s.bind((host, port))
# N=5
# s.listen(N)
# Users = [x for x in range (N)]
# for i in range (1, N):
#     Users[i] = threading.Thread(target = Dict())
    # except ConnectionResetError:
    #     pass
