from threading import  Event, Thread
import  logging
import time

FORMAT = '%(asctime)s %(threadName)s %(thread)d %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)

def boss(event:Event):
    logging.info("I'm boss, waiting for U.")
    # 等待
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
            # 通知
            event.set()
            break
    logging.info("I'm finished my job. cups={}".format(cups))

event = Event()
w = Thread(target=worker, args=(event,))
b = Thread(target=boss, args=(event,))
w.start()
b.start()

# 2019-06-12 22:30:14,285 Thread-1 8796 I'm working for U.
# 2019-06-12 22:30:14,286 Thread-1 8796 make 1
# 2019-06-12 22:30:14,286 Thread-2 8516 I'm boss, waiting for U.
# 2019-06-12 22:30:14,786 Thread-1 8796 make 1
# 2019-06-12 22:30:15,286 Thread-1 8796 make 1
# 2019-06-12 22:30:15,787 Thread-1 8796 make 1
# 2019-06-12 22:30:16,287 Thread-1 8796 make 1
# 2019-06-12 22:30:16,787 Thread-1 8796 make 1
# 2019-06-12 22:30:17,287 Thread-1 8796 make 1
# 2019-06-12 22:30:17,787 Thread-1 8796 make 1
# 2019-06-12 22:30:18,287 Thread-1 8796 make 1
# 2019-06-12 22:30:18,787 Thread-1 8796 make 1
# 2019-06-12 22:30:19,287 Thread-1 8796 I'm finished my job. cups=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# 2019-06-12 22:30:19,287 Thread-2 8516 Good job.