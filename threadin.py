import threading
import time
num1 = 25
num2 = 30

def add ( a, b):
    print("Inside add function\n")
    print("Waiting for 20 seconds before adding")
    time.sleep(20)
    print("Addition resuts: ", a + b)


def sub(a, b):
    print("Inside the subtract function")
    print("Subtraction value is : " , a - b)
    print("Waiting for 10s in subtract\n")
    time.sleep(10)

#threads for adding and sub function
    
add_thread = threading.Thread(target=add, args= (num1, num2))
sub_thread = threading.Thread(target=sub, args = ( num1, num2))

#start both threads

add_thread.start()
sub_thread.start()

#wait until they complete the job
add_thread.join()
sub_thread.join()

print("Job complete")