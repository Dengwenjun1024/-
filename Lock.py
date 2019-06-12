
import threading
import logging

logging.basicConfig(level=logging.INFO)

cups = []

lock = threading.Lock()
# lock:threading.Lock,
def worker(lock:threading.Lock, task=10):
    while True:
        lock.acquire() # 加锁
        count = len(cups)
        lock.release() # 解锁
        if count >= task:
            break
        lock.acquire()
        cups.append(1)
        lock.release()
        logging.info("{} make 1".format(threading.current_thread().name))
    logging.info("{}".format(len(cups)))

for _ in range(10):
    threading.Thread(target=worker, args=(lock,)).start()

# INFO:root:Thread-1 make 1
# INFO:root:Thread-1 make 1
# INFO:root:Thread-1 make 1
# INFO:root:Thread-1 make 1
# INFO:root:Thread-1 make 1
# INFO:root:Thread-1 make 1
# INFO:root:Thread-1 make 1
# INFO:root:Thread-1 make 1
# INFO:root:Thread-1 make 1
# INFO:root:Thread-1 make 1
# INFO:root:10
# INFO:root:10
# INFO:root:10
# INFO:root:10
# INFO:root:10
# INFO:root:10
# INFO:root:10
# INFO:root:10
# INFO:root:10
# INFO:root:10
