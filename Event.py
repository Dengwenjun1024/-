from threading import  Event, Thread
import  logging
import time

FORMAT = '%(asctime)s %(threadName)s %(thread)d %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)

def boss(event:Event):
    logging.info("I'm boss, waiting for U.")
<<<<<<< HEAD
    # 等待
=======
    # 等待，直到flag为True
>>>>>>> 事件（Event）的应用
    event.wait()
    logging.info("Good job.")

def worker(event:Event, count=10):
    logging.info("I'm working for U.")
    cups = []
    while True:
        logging.info("make 1")
        time.sleep(0.5)
        cups.append(1)
        if len(cups) >= count:
<<<<<<< HEAD
            # 通知
=======
            # 通知，将falg设置为True，老板那边就可以继续执行代码了。
>>>>>>> 事件（Event）的应用
            event.set()
            break
    logging.info("I'm finished my job. cups={}".format(cups))

event = Event()
w = Thread(target=worker, args=(event,))
b = Thread(target=boss, args=(event,))
w.start()
b.start()