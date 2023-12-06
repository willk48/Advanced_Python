import time
import threading

start = time.perf_counter()
#random function to illustrate something getting done
def work():
    print(f'This thing takes 3 second(s)...')
    time.sleep(3)
    #real work would be here
    return f'Its Done.'

#list of threads to join
threads = []
#create 5 threads and let them start
for _ in range(5):
    t = threading.Thread(target=work)
    t.start()
    threads.append(t)
#join them all
for thread in threads:
    thread.join()
#calc time
finish = time.perf_counter()
print(f'Finished in {round(finish-start, 2)} second(s)')