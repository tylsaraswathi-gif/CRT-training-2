'''
create a package 
utilities
    calculator.py
    greetings.py
main.py
import from utilities and use them


'''
from utilities.calculator import add
print("Addition =", add(10, 5))
from utilities.greetings import greet
greet("Yamini")

import math
print(math.__name__)
print(math.__doc__)

import math


import sys
print(sys.path)

print(dir(math))


#pip-->python package manager

#1.sys
#multiple projects
# canteen--numpy(version-1.0)
#library--numpy(version-2.0)
#bus--numpy(version-1.5)


#python virtual environment

#python-m venv env/garden
#env\scripts\Activate.ps1
#Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
import os
from reportutils.analyzer import (
    calculate_average,
    highest_mark,
    lowest_mark
)

class FileNotFoundCustomError(Exception):
    pass

try:
    filename = "marks.txt"

    if not os.path.exists(filename):
        raise FileNotFoundCustomError("Marks file not found!")

    with open("marks.txt", "r") as file:
        marks = [int(mark) for mark in file.read().split()]

    print("Average:", calculate_average(marks))
    print("Highest:", highest_mark(marks))
    print("Lowest:", lowest_mark(marks))

except FileNotFoundCustomError as e:
    print("Error:", e)

except ValueError:
    print("Marks file contains invalid data.")

except Exception as e:
    print("Unexpected Error:", e)


from log_file_inspector.logtools import *

filename = "log.txt"

print("Lines:", count_lines)
print("Words:", count_words)
print("Characters:", count_characters)
