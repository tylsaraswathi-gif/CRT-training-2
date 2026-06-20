import threading
def evaluate_student(name, math, physics, chemistry):
    total = math + physics + chemistry
    average = total / 3
    if average >= 40:
        result = "PASS"
    else:
        result = "FAIL"
    print(name, total, result)
n = int(input("Enter number of students: "))
threads = []
for _ in range(n):
    data = input().split()
    name = data[0]
    math = int(data[1])
    physics = int(data[2])
    chemistry = int(data[3])
    t = threading.Thread(
        target=evaluate_student,
        args=(name, math, physics, chemistry)
    )
    threads.append(t)
    t.start()
for t in threads:
    t.join()
print("Result Processing Completed")





#secure bank transactions
import threading

balance = 0
lock = threading.Lock()

def withdraw(amount):
    global balance

    with lock:
        if balance >= amount:
            balance -= amount
            print(amount, "withdrawn")
        else:
            print("Insufficient Balance")


balance = int(input("Enter initial balance: "))
n = int(input("Enter number of withdrawals: "))
threads = []
for _ in range(n):
    amount = int(input())
    t = threading.Thread(
        target=withdraw,
        args=(amount,)
    )
    threads.append(t)
    t.start()
for t in threads:
    t.join()
print("Final Balance:", balance)