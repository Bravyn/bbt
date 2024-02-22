#This script is the result of my
#experimentation with multiprocessing
#and multithreading in python
import time
from multiprocessing import Process

number1 = 25
number2 = 30

def add( number1, number2):
    try:
        print("Sum is: ", number1 + number2)
        time.sleep(10)
    except Exception as e:
        print(e)

def subtract(number1, number2):
    try:
        print("Subtraction result is: ", number1 - number2)
        time.sleep(20)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    #create an addition process
    #and  sub function
    addition_process = Process(target=add, args= ( number1, number2))
    subtraction_process = Process(target=subtract, args = (number1, number2))

    #start the processes
    subtraction_process.start()

    addition_process.start()

    #wait until they are all done
    addition_process.join()
    subtraction_process.join()
