'''
1.Raice condition
2.Synchronization
3.Lock
4.Rlock
'''
#why we need synchronization?
'''
balance=1000
Thread-1--withdread 500
Thread-2--withdraw 700
both are accessing same variable
without proper control
Incorrect balance
Wrong Transactions
data corrupt

to avoid the above we use :
synchronization:
it is a process of controlling access to shared resources 
so that only one thread modifies at a time

Lock:
shared resources:any variable,file,database,object

Example:
count=0
if multiple threads modifies count simultaneously

#Race condition:
occurs when multiple threads access and modify shared data simultaneously 
causing unpredictable outputs

'''
count=0
count+=1
print(count)

#threads
import threading

count = 0
threads = []

def increment():
    global count
    count += 1
for i in range(1000):
    t = threading.Thread(target=increment)
    threads.append(t)
    t.start()
for t in threads:
    t.join()
print(count)
'''
Critical Section:
code section where shared resources are accessed is called critical section 
count+=1--->crotical section

To avoid the race condition?
one thread should enter critical section at a time:

solution:Lock

what is a lock?
synchronization Mechanism
that allows only one thread to execute a critical section at a time

Thread A acquires a lock
other Thread will wait
Thred A releases lock
next thread gets lock

import threading
lock=threading.Lock()

#to apply lock
lock.acquire()

#to release 
lock.release()

'''
import threading
count=0
lock=threading.Lock()
def increment():
    global count
    for i in range(10000):
        with lock:
            count+=1
        
t1=threading.Thread(target=increment)
t2=threading.Thread(target=increment)
t1.start()
t2.start()

t1.join()
t2.join()

print(count)


#Bank example:

import threading

class Bank:
    def __init__(self):
        self.balance = 1000
        self.lock = threading.Lock()

    def withdraw(self, amount):
        with self.lock:
            if self.balance >= amount:
                self.balance -= amount
                print(amount, "withdrawn")
            else:
                print("Insufficient balance")

bank = Bank()

t1 = threading.Thread(target=bank.withdraw, args=(700,))
t2 = threading.Thread(target=bank.withdraw, args=(500,))

t1.start()
t2.start()

t1.join()
t2.join()

print("Balance:",bank.balance)

'''
Dead Lock:
where the threads wait forever for lock
Thread 1
Lock A
waiting for lock B
Thread 2:
Lock B
waiting for lock A

Thread 1-->waiting for Lock A
Thread 2-->waiting for Lock B
dead lock

Rlock:recursive lock
a thread can acquire same
locks multiple times


Why RLock?
Normal lock
acquire lock
release lock

if same thread acquire again 
deadlock

'''
#import threading
#lock=threading.Lock()
#def outer():
    #lock.acquire()
    #inner()
    #lock.release()
#def inner():
    #lock.acquire()
    #print("Inner")
    #lock.release()
#outer()
'''
Outer() acquire the lock
inner() trying to acquire same lock 
lock is already head above
wait forever

'''
lock=threading.RLock()
def inner():
    with lock:
        print("Inner")
def Outer():
    with lock:
        print("outer")
        inner()
Outer()
'''
outer acquire
count=1
outer releases

inner acquire
count=2
outer releases


'''