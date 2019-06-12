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