import threading
import time

def coding(num):
    for i in range(num):
        print("coding")
        time.sleep(0.2)
def music(count):
    for i in range(count):
        print("musing")
        time.sleep(0.3)
class Thread_Test:
    def __init__(self) -> None:
        pass
    def test(self):
        t1=time.time()
        thread1=threading.Thread(target=coding,args=(3,),daemon=True)
        thread2=threading.Thread(target=music,kwargs={"count":3},daemon=True)
        # coding()
        # music()
        thread1.start()
        thread2.start()
        # thread1.join()
        # thread2.join()
        t2=time.time()
        print(t2-t1)

if __name__=="__main__":
    tt=Thread_Test()
    tt.test()
    print((3,))