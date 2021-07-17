Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import threading
>>> import time
>>> exitFlag = 0
>>> 
>>> class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print("Starting " + self.name)
        print_time(self.name, 5, self.counter)
        print( "Exiting " + self.name)

        
>>> def print_time(threadName, counter, delay):
     while counter:
        if exitFlag:
            threadName.exit()
            time.sleep(delay)
            print("%s: %s" % (threadName, time.ctime(time.time())))
            counter -= 1

            
>>> thread1 = myThread(1, "Thread-1", 1)
>>> thread2 = myThread(2, "Thread-2", 2)
>>> thread1.start()
Starting Thread-1
>>> 

>>> thread2.start()
Starting Thread-2
>>> 

>>> print("Exiting Main Thread")
Exiting Main Thread
>>> 
