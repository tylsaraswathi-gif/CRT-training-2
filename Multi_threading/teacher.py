import threading
import time
def student(name):
    print(name,"started the exam")
    time.sleep(3)
    print(name,"submitted paper")
t1 = threading.Thread(target=student, args=("Yamini",),name="student-1")
t2 = threading.Thread(target=student, args=("Priya",),name="student-2")
t1.start()
t2.start()
t1.join()
t2.join()
print("All students have submitted their papers")


