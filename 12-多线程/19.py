import multiprocessing
from time import sleep, ctime


def clock(interval):
    while True:
        print("The time is %s" % ctime())
        sleep(interval)



if __name__ == '__main__':
    p = multiprocessing.Process(target = clock, args = (5,))   # 这5表示的就是5秒钟，就是参数interval
    p.start()

    while True:
        print('sleeping.......')
        sleep(1)

