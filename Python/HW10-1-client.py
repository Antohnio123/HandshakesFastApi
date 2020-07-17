import socket


while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 53023
    s.gettimeout()
    s.connect((host, port))
    ask = input('\nВведите запрашиваемое слово: ')
    s.send(ask.encode())
    if ask.lower() == 'close':
        s.close()
        exit()
    else:
        Res = s.recv(1024)
        print('Ответ сервера: {}'. format(Res.decode()))
        s.close()

