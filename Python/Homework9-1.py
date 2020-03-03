import datetime
import threading
import multiprocessing
# import Timer from Homework6

class Timer:
    t1=0
    def __enter__(self):
        self.t1=datetime.datetime.now()
    def __exit__(self, exc_type, exc_val, exc_tb):
        t2 = datetime.datetime.now()
        print("Время внутри таймера = "+str(t2-self.t1))

def find_primes(start =1, end = 3):
    L=[]
    for i in range (start, end):
        for j in range (2, i-1):
            if i//j ==0:
                L.append(i);
    return L

if __name__ == '__main__':
    print("Начинаем мультипроцессинговый расчёт")
    with Timer():
        m1 = multiprocessing.Process(target = find_primes, args=(3, 10000))
        m2 = multiprocessing.Process(target = find_primes, args=(10001, 20000))
        m3 = multiprocessing.Process(target = find_primes, args=(20001, 30000))
        m1.start()
        m2.start()
        m3.start()
        m1.join()
        m2.join()
        m3.join()


    with Timer():
        print("\nНачинаем мультиПОТОКОВЫЙ расчёт")
        t1 = threading.Thread(target = find_primes, args=(3, 10000))
        t2 = threading.Thread(target = find_primes, args=(10001, 20000))
        t3 = threading.Thread(target = find_primes, args=(20001, 30000))
        t1.start()
        t2.start()
        t3.start()
        t1.join()
        t2.join()
        t3.join()

    with Timer():
        print("\nНачинаем обычный расчёт")
        find_primes(3, 10000)
        find_primes(10001, 20000)
        find_primes(20001, 30000)