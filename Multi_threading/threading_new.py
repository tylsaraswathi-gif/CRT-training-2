'''
join():mainthread-->owner
    worker thread-->worker

'''
import threading
import time
def task():
    time.sleep(3)
    print("Thread finished")
t=threading.Thread(target=task)
t.start()
t.join()
print("Main thread ends here")

#multiple threads with join
def task(name):
    print(name,"started")
    time.sleep(2)
    print(name,"finished")
t1=threading.Thread(target=task,args="A")
t2=threading.Thread(target=task,args="B")
t1.start()
t2.start()
t1.join()
t2.join()
print("All threads completed")

#Exapmle on naming threads
def task():
    print(threading.current_thread().name,"started")
    time.sleep()
    print(threading.current_thread().name,"Finished")
t1=threading.Thread(target=task,name="Download thread")
t2=threading.Thread(target=task,name="Upload thread")
t1.start()
t2.start()



