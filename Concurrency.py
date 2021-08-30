#----------------------
# Concurrency
#----------------------    
- ability to run multiples task in parallel
    
    Thread  : instruction/statement/command is executed called Thread. Once thread runs in single core.
    Process : Program (group of instruction scommands) is executed called Process. Process - no. of core + Resources (CPU/network/filesystem etc)


# Usecase :
 - You need to run background or I/O-oriented tasks without stopping your main thread’s execution. 
 - You need to spread your workload across several CPUs.
   

   
# Advantage :
  - multiple independent task can be performed at same time and saves time.
      #e.g, load data into 3 tables from single file,
              #read file into dataframe and filter out , then load into tables, repeat for other 2.  
   - fetch data from multiple source and dump at once into database.





#------------------------------------------
# Multithreading
#------------------------------------------

- Multithreading is ability to run multiple threads at a time. Hence, enable Parallelism/concurrency to performance improvement.

- By default, Python processes run on only one thread, called the main thread. This thread executes code on a single processor.

- Main modules for multithreading in python 
    1.thread - low-level and deprecated from python 3.X and uses __thread for backward compatibility
    2.threading - high level module 
    3.concurrent.futures


# Main functions of threading module :
    activeCount()	: Returns the count of Thread objects which are still alive
    currentThread()	: Returns the current object of the Thread class.
    enumerate()	    : Lists all active Thread objects.
    isDaemon()	    : Returns true if the thread is a daemon.
    isAlive()	    : Returns true if the thread is still alive.

    #Thread Class methods:
    start()	        : Starts the activity of a thread. It must be called only once for each thread because it will throw a runtime error if called multiple times.
    run()	        : This method denotes the activity of a thread and can be overridden by a class that extends the Thread class.
    join()	        : It blocks the execution of other code until the thread on which the join() method was called gets terminated.






#-------------------------------------------------
# Create single thread
#-------------------------------------------------

# 1. using simple function
import threading

def thread_function(wait_sec):
    print('Starting thread')
    time.sleep(wait_sec)
    print('Finished thread')
    
t=threading.Thread(target=thread_function,args=[5]) # args=[] , if you want to pass any argument to function  ( Thread - Class)
t.start() # calls the run method of Thread




# 2. using subclass of class Thread in threading module
from threading import Thread

class thread_class(Thread):
    #def __init__()  
    """can also be used to set some parameter for run"""
    
    def run(self): # overiding run function of threading
        print('Starting thread')
        time.sleep(4)
        print('Finished thread')

t = thread_class()
t.start()


# 3. using class
from threading import Thread

class thread_class():
    def thread_function(self): # overiding run function of threading
        print('Starting thread')
        time.sleep(4)
        print('Finished thread')

TC = thread_class()
t = threading.Thread(target=TC.thread_function())
t.start()





#-------------------------------------------------
# Create multiple threads
#-------------------------------------------------
    
   
# Supoose T1(5min), T2(5min) , in a process (T1+T2) will take 10 mins 
#, by running conncurrently same can be done in 5mins

def load( dataframe , table , SID , thread_id):
    """insert into <table> select * from dataframe"""
  
def main()
    print('starting main thread')
    t1=threading.Thread(target=load,args=[df1,table_name,db,'thread-1'])
    t2=threading.Thread(target=load,args=[df1,table_name,db,'thread-2'])
    
    #both thread will be started at same time
    t1.start()
    t2.start()
    
    #wait before marking process to be completed
    t1.join()
    t2.join()
    print('finishing main thread')
  


# create n threads
    threads = []
    
    # 1. start all threads, store their refereneces
    for i in range(n-1):    
        t = threading.Thread(target= load )
        t.start()
        threads.append(t)
        
    # 2. Check completion of threads
    for t in threads:
        t.join()
    
  
  
#Return the number of Thread objects currently alive     
threading.active_count() 

# Current thread name , main or thread 1 etc
threading.current_thread().getName()
#threading.main_thread(),getName()   #MainThread
  
  
t1.is_alive()  # check if thread is alive



#-----------------------------------------------------------------------------
#Global Interpreter Lock (GIL) 
#                   - only one thread run at the time in python
#-----------------------------------------------------------------------------

#CPU bound code - code basically runs on CPU Core, e,g code with arithmetic calculations
#I/O bound code - code that access file system.

    - lock ( or mutex) that allows only one thread to have control on python interpreter.
    - In the multi-threaded version, the GIL prevented the CPU-bound threads from executing in parellel ( Hence, no 2 threads can run 
      at same time in python ).And, Sometimes also increases time in overall program due to lock aquire and release. Hence, multithreading is not a good idea.
      [ can be verified with Top or Task manager that only single python process is running ]
    - However,we can deal with GIL to improve performance by using multiprocessing instead of multithreading.
      Each process will gets its own memory , python interpreter/GIL and thread. [ multiple python processes will be opened]

# CPU Cores - allows Multiprocessing  

#Note:
    - Each thread may run on signle CPU core and multiple core system , multhreading may be achieved  ( checked for sleep(5) )


#-----------------------------------------------
# multithreading problems 
#-----------------------------------------------
    #Critical Section
        - It is a part of code that accesses or modifies shared variables and must be performed as an atomic transaction.

    #Context Switch
        - It is the process that a CPU follows to store the state of a thread before changing from one task to another 
          so that it can be resumed from the same point later.


# Disadvantage of Multithreading :-
    #Deadlock : in concurrent system , when different threads or processes try to acquire the same shared resources at the same time

    #Race Condition : when threads tries to modifies shared variable  in critical section at same time, then threads execution is unexpected and ordering.
                    Suppose withdrawl scenario : t1 - withdrawl thread , t2 - balance update ,Account balance is shared variable in this case
                    then due to race condition t2 may run first.



""" Race condition Example"""
import threading, time


def load(n1):
    print('invoking thread id {}'.format(n1))
    time.sleep(5)
    print('invoked thread id {}'.format(n1))


def main():
    print('starting main thread')
    start = time.perf_counter()  # return seconds in fraction of performance counter
    t1 = threading.Thread(target=load, args=['thread-1'])
    t2 = threading.Thread(target=load, args=['thread-2'])
    t3 = threading.Thread(target=load, args=['thread-3'])
    t4 = threading.Thread(target=load, args=['thread-4'])
    t5 = threading.Thread(target=load, args=['thread-5'])


    # both thread will be started at same time
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()

    # wait before marking process to be completed
    result1 = t1.join()
    result2 = t2.join()
    result3 = t3.join()
    result4 = t4.join()
    result5 = t5.join()

    finish = time.perf_counter() - start
    print('finishing main thread in {}.....'.format(finish))

main()
"""
starting main thread
invoking thread id thread-1
invoking thread id thread-2
invoking thread id thread-3
invoking thread id thread-4
invoking thread id thread-5
invoked thread id thread-5
invoked thread id thread-3  <----- see race condition
invoked thread id thread-1  <----- see race condition
invoked thread id thread-2
invoked thread id thread-4
finishing main thread in 5.016072100000001.....
"""



    - To avoid Deadlock and Race Condition, we can use thread synchronisation of threading module.
    - Synchronisation thread:
        1. Locks
        2. RLocks
        3. Semaphores
        4. Conditions
        5. Events
        6. Barriers


#------------------------
# locks     
#------------------------
    - Lock has 2 states : locked and unlocked
    - lock has 2 methods : acquire(), release() . By default, the lock has the unlocked status until you acquire it.
    - lock.acquire() - acquire lock
    - lock.release() - release lock


    # e.g, 
        import threading
        lock = threading.Lock()
        
        def first_function():
            for i in range(5):
                lock.acquire()
                print ('Executing the first funcion')
                lock.release()
        
        def second_function():
            for i in range(5):
                lock.acquire()
                print ('Executing the second funcion')
                lock.release()
        
        if __name__=="__main__":
            t1 = threading.Thread(target=first_function)
            t2 = threading.Thread(target=second_function)
        
            t1.start()
            t2.start()
        
            t1.join()
            t2.join()

       # Note:
            - first_function() should be executed first then second_function() , but due to race condition second_function may execute first.
            - to avoid race condition, Locks are used.

  



#--------------------------------------
# states in threads
#--------------------------------------
import threading

counter=0

def increment_counter():
    global counter
    counter=counter+1
    print('counter value is {}'.format(counter))

for i in range(5):
    t = threading.Thread(target=increment_counter)
    print('calling :'+str(i))
    t.start()


calling :0
counter value is 1
calling :1
counter value is 2
calling :2
counter value is 3
calling :3
counter value is 4
calling :4
counter value is 5

# Essentially, above code is working sequentially, as calling function is so quick that when we start new thread , previous is getting completed












#---------------------------------------------
# concurrent.futures 
#---------------------------------------------
    - Supports both Threads and Processes:
        - Multiprocess : ProcessPoolExecutor, each process has its own python interpreter  ( best for CPU bound tasks)
        - MultiThread  : ThreadPoolExecutor , multithreading using same process , shares Python interpreter and memory ( works best for I/O operations)
    - Standard library for high level asynchronous tasks , has abstract class - Executor , can be only used with subclasses - ProcessPoolExecutor, ThreadPoolExecutor.
    - simplified version of threading module.
    - can return values and exceptions from worker thread to main thread

    #-------------------------------
    # ThreadPoolExecutor
    #-------------------------------
        - creates pool of threads without targets and allows to execute functions/task


     from concurrent.futures import ThreadPoolExecutor
     
     with ThreadPoolExcecutor(max_workers=2) as executor: # DEFAULT MAX_WORKERS = MIN(32,OS.CPU_cOUNT+4)
        executor.submit(f1)
        executor.submit(f2)
     
     # executor.shutdown()  # waits for pool to get complete , since we have used WITH it implicity run executor.shutdown() to free resource ocuupied by threads
     
     
     
     # Most used way
     with ThreadPoolExcecutor(max_workers=2) as executor:
        funcs = [ f1 , f2, f3 , f4 , f5 ]
        threads = [ executor.submit(func) for func in funcs]
        
        for f in concurrent.futures.as_Completed(threads): # as_Completed() - yields the thread when they are done
            print(f.results()) # results() - gives return value of function , throws an exception in case of failure
     
     
     
     
     # if same function need to be called with different arguments
     with ThreadPoolExcecutor(max_workers=2) as executor:
        res = executor.map(<func>,<args>)
     return res
     
     

     

    #--------------------------------
    # Multiprocessing
    #--------------------------------
    import multiprocessing 
    
    p1 = multiprocessing.Process(target= Func1, args =)
    p2 = multiprocessing.Process(target= Func2, args =)
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    # supports locks - acquire and release too

    
    
    # with ThreadProcessExecutor
    from concurrent.futures import ProcessPoolExecutor
    with ProcessPoolExecutor(max_workers=2) as pool:
            pool.submit(f1)
            pool.submit(f2)
