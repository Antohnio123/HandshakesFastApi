import threading
import time

class Mythread (threading.Thread):
    def __init__(self, a, b, c = 10):
        self.mutex = threading.RLock()
        threading.Thread.__init__(self, name = str(a)+'-' + str(b)+'-'+str(c))
        self.__a = a
        self.__b = b
        self.__c = c
    def run(self):
        print(threading.current_thread().name)
        print('a = ' + str(self.__a) + ', b = ' + str(self.__b) + ', c = '+str(self.__c))
        for i in range (1, self.__c):
            time.sleep(i)
            self.__a*=self.__b
            i+=1
            print(self.__a)

if __name__ == '__main__':
    t1=Mythread(1, 2)
    t2=Mythread(2, 3, 5)
    t3=Mythread(5, 4, 6)
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()




