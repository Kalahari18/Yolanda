import threading
import time


def get_web(url):
    time.sleep(3)
    print(url)

class MyThread(threading.Thread):
    def __init__(self,name,url):
        super().__init__()
        self.name=name
        self.url=name
    def run(self) -> None:
        time.sleep(3)
        print(self.url)

        
if __name__=="__main__":
    t1=MyThread("t1",url="baidu.com")
    # start_time=time.time()
    # t1=threading.Thread(target=get_web,args=("www.baidu.com",))
    # t2=threading.Thread(target=get_web,args=("www.google.com",))
    # t1.start()
    # t2.start()
    # t1.join()
    # t2.join()
    # print("程序运行结束！")
    # end_time=time.time()
    # print(f"时间:{end_time-start_time}")


