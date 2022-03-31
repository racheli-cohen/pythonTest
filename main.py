
from message import ClassMessage
import time
import multiprocessing

if __name__ == '__main__':

    m = ClassMessage()
    arr = ["print('1')", "time.sleep(3)", "time.sleep(2)", "print('4')", "print('5')", "print(6*6)", "print(sqrt(5))"]
    pool = multiprocessing.Pool(10)
    pool.map(m.add_to_queue, arr)
    pool.close()




