import socket

D = dict(кошка='cat', собака='dog', слон = 'elephant', птица = 'bird', рыба = 'fish', волк = 'wolf', змея = 'snake')
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 53023
s.bind((host, port))
s.listen(3)
while True:
    conn, addr = s.accept()
    print('Server got the connection. Address = {}'.format(addr))
    ask = conn.recv(1024)
    ask = ask.decode()
    if ask.lower() == 'close':
        conn.close()
        print('Client aborted the connection. Address = {}'.format(addr))

    elif ask in D:
        Res = D[ask]
        conn.send('Перевод: {}'.format(Res).encode())
    else:
        Res = 'Ошибка! Такого слова нет в словаре'
        conn.send('Перевод: {}'.format(Res).encode())



