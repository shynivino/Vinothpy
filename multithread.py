import threading
import time
lock = threading.Lock()

def calc_square(number1,number2):
    #lock.acquire() # acquire the lock to finish first square definition
    for i in range(number1,number2):
        time.sleep(1)
        print('Square:' , i * i)
    #lock.release() # release the lock to once square definition execution finishes
        
def calc_cube(number1,number2):
    #lock.acquire() # acquire the lock to finish first cube definition
    for i in range(number1,number2):
        time.sleep(1)
        print('Cube:' , i * i * i)
    #lock.release() # release the lock to once cube definition execution finishes

def call_wait():
    while True:
        time.sleep(1)
        print("Entered in Waiting Thread")


number1 = 5
number2 = 10
thread1 = threading.Thread(target=calc_square, args=(number1,number2))
thread2 = threading.Thread(target=calc_cube, args=(number1,number2))
thread3 = threading.Thread(target=call_wait,daemon=True) # This thread stops Immediately  when main thread completes its execution irrespective of its completion. 

# Will execute 3 threads in parallel
thread1.start()
thread2.start()
thread3.start()

# Joins threads back to the parent process, which is this
thread1.join()
thread2.join()

print("completed main")
