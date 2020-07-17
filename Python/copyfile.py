import os

def copyfile(source, destination):
    class NoSourceExeption(Exception):
        pass

    def sourcecheck(source):
        if not os.path.exists(source):
            raise NoSourceExeption()

    class DestExeption(Exception):
        pass

    def destcheck(destination):
        if os.path.exists(destination):
            raise DestExeption()

    try:
        sourcecheck(source)
        destcheck(destination)
    except NoSourceExeption:
        print('Источника не существует, программа закрывается')
        exit()
    except DestExeption:
        print('Файл назначения уже существует, менять его мы не уполномочены, программа закрывается')
        exit()

    with open(source, "rb", encoding='utf-8') as Sfile:
        r = Sfile.readlines()
        with open(destination, "wb", encoding='utf-8') as Dfile:
            Dfile.writelines(r)
    return(0)


s = "source.txt"
d = 'dest.txt'
copyfile(s, d)