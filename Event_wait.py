from threading import Event, Thread
import logging
logging.basicConfig(level=logging.INFO)

def do(event:Event, interval:int):
    # 每interval检测flag是否为True
    while not event.wait(interval):
        logging.info("do sth.")

e = Event()
Thread(target=do, args=(e, 3)).start()

e.wait(10)
e.set()
print('main exit')

# INFO:root:do sth.
# INFO:root:do sth.
# INFO:root:do sth.
# main exit