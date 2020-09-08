import threading
import time


def whaite(v):
    global sema
    print("launch {}".format(v))
    time.sleep(v)
    print("finish {}".format(v))
    sema.release()
    pass

sema = None

if __name__ =="__main__" :
    sema = threading.Semaphore(5)
    for i in range(20):
        t1 = threading.Thread(target=whaite, args=(i,))
        sema.acquire()
        t1.start()
    print("fini")
    pass
