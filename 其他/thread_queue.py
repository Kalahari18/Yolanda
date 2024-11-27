from queue import Queue
import threading
import time

def product(q):
    kind=("猪肉","白菜","豆沙")
    for i in range(3):
        print(threading.current_thread().name,"包子生产者开始生产包子。。。")
        time.sleep(1)
        q.put(kind[i%3])
        print(threading.current_thread().name,"包子生产者包子做完了。。。")


def consumer(q):
    while True:
        print(threading.current_thread().name,"吃包子。。。")
        time.sleep(1)
        t=q.get()
        print("消费者吃了一个{}包子".format(t))

if __name__=="__main__":
    q=Queue(maxsize=1)
    threading.Thread(target=product,args=(q,)).start()
    threading.Thread(target=consumer,args=(q,)).start()