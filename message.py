import threading
from multiprocessing import Lock
import time
from math import *

mutex = Lock()

class ClassMessage:
    def add_to_queue(self, message):
        print(threading.current_thread())
        print('try to add {} message to the queue'.format(message))
        eval(message)
        print('the message {} was done'.format(message))




