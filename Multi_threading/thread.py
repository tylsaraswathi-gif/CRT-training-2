'''
what is a program?
A program is a set of instruction stored on a desk


print("hello")

storing on a disk???

python hello.py

hello
what is process?

when a program starts excuting it becomes a process

running?
python hello.py
hello


os-operating system
chrome:
vs code:
spotify:
each one is a seperate process

Characteristics:
1.Independent
2.seperate memory:
chrome :1.8GB vscode-500MB
3.heavy weight:
memory allocations
resource allocation
cpu sheduling


What is a thread?
A thread is smallest unit execution inside a process

Restaurant==Process
Workers inside res=threads
worker 1- Taking the orders
worker 2-cooking
worker 3-billing
worker 4-cleaning

Visully:
process:
chrome:
    +thread 1
    +thread 2
    +thread 3

process                     thread
1.Independent               part of process
2.Heavy weight              Light weight
3.seperate memory           shared memory
4.slow                      fast
5.expensive                 cheap
6.communication:difficult   easy

why threads are faster?
threads will share the memory
process needs separate memory allocation

concurrency?
teacher checking the notebooks

Student A
Student B
Student C


concurrency:
A
B
C
A
B 
C
one at a time
rapidly switching
appears simultaneously

parallelism:
cashier 1:customer 1
cashier 2:customer 2
cashier 3:customer 3

truly simultaneously
CPU1-->task a
CPU2-->task b
CPU3-->task c
concurrency:
A
B
A
B
A
B

parallelism:
cpu1-AAA
cpu2-BBB

one chef cooking:
soup
noodles
fried rice
parallelism:
chef 1:soup
chef 2:noodles
chef 3:fried rice

python threads will use--->concurrency
due to GIL-->Global INterpreter Lock

'''
#creation of threads:
import threading
#function created(do's nothing)
def display():
    print("Hello")
#thread object creation
t=threading.Thread(target=display)
t.start()

#multiple threads:
import threading
def task():
    print("Thread running")
t1=threading.Thread(target=task)
t2=threading.Thread(target=task)
t3=threading.Thread(target=task)
t1.start()
t2.start()
t3.start()

'''
Main Thread
        + t1
        + t2
        + t3
all executes independently

'''
#threads with loops:
def numbers():
    for i in range(5):
        print(i)
t=threading.Thread(target=numbers)
t.start()

#Two threads with diff task
def even():
    for i in range(0,10,2):
        print("even:",i)
def odd():
    for i in range(1,10,2):
        print("odd:",i)

t1=threading.Thread(target=even)
t2=threading.Thread(target=odd)
t1.start()
t2.start()

'''
os shedular decides:
which thread to run first

'''
import threading

print(threading.current_thread())

def task():
    print("Hello")
    print(threading.current_thread().name)

t = threading.Thread(target=task, name="Student_Thread")
t.start()

#passing arguments
def square(n):
    print(n*n)
t=threading.Thread(target=square,args=(5,))
t.start()

#to delay the threads
import time
time.sleep(1)

print("start")
time.sleep(2)
print("end")

import threading
import time
def task():
    for i in range(5):
        print(i)
        time.sleep(1)
t=threading.Thread(target=task)
t.start()

#retry mechanism:
#while True:
    #try:
        #connect()
    #except:
        #time.sleep(3)


