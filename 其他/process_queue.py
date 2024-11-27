import multiprocessing
import time


def product(q):
    kind=("猪肉","白菜","豆沙")
    for i in range(3):
        print(multiprocessing.current_process().name,"包子生产者开始生产包子。。。")
        time.sleep(1)
        q.put(kind[i%3])
        print(multiprocessing.current_process().name,"包子生产者包子做完了。。。")


def consumer(q):
    while True:
        print(multiprocessing.current_process().name,"吃包子。。。")
        time.sleep(1)
        t=q.get()
        print("消费者吃了一个{}包子".format(t))

if __name__=="__main__":
    q=multiprocessing.Queue()
    multiprocessing.Process(target=product,args=(q,)).start()
    multiprocessing.Process(target=consumer,args=(q,)).start()