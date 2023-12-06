import threading
import time
import random

#a program to determine how many workers should be on staff in a textile factory at any given time
#based on the current work orders. The user or admin will edit the time and wage values for their staff
#and the program will output the amount of time it will take for different amounts of staff to complete 
#the order and the wage payout at each tier. Demonstrating threading by allowing for different distributions
#of processes and different execution orders. 

EMPLOYEES=["Dave","Sam","Alex","Liz"]
WAGE=1.10
S_TIME=0.4
P_TIME=0.9
H_TIME=0.5

def shirt():
    print("Starting:  t_shirt...")
    time.sleep(S_TIME)
    print("Completed: t_shirt.")

def pants():
    print("Starting:  pants...")
    time.sleep(S_TIME)
    print("Completed: pants.")

def hat():
    print("Starting:  hat...")
    time.sleep(S_TIME)
    print("Completed: hat.")

def divide_labor(num=0, orders_list=[]):
    for i in range(0, num):
        yield orders_list[i::num]

def do_work(num=0,choices=[shirt,pants,hat]):
    for i in range(num):
        random.choice(choices)()

def main():
    '''test_l=divide_labor(4,["test", "different one", "third one", "fourth one", "fifth one"])
    for i in range(4):
        print(next(test_l))'''
    
    how_many=int(input("How many items in queue? (Suggested < 15): "))
    print("======================================================================================")
    print("                             One Employee on Staff")
    start1=time.perf_counter()
    do_work(how_many)
    finish1=time.perf_counter()
    print(f"Time Spent: {round(finish1-start1,2)} second(s)")
    print(f"Wages Owed: {(round(WAGE*(finish1-start1), 2))}")
    print("======================================================================================")
    print("                             Two Employees on Staff")
    start2=time.perf_counter()
    threads = []
    if (how_many%2==0):
        for _ in range(2):
            t = threading.Thread(target=do_work(how_many//2))
            t.start()
            threads.append(t)
        for thread in threads:
            thread.join()
        finish2=time.perf_counter()
    else:
        ...
        finish2=time.perf_counter()
    print(f"Time Spent: {round(finish2-start2,2)} second(s)")
    print(f"Wages Owed: {(round(WAGE*(finish2-start2), 2))}")

if __name__ == '__main__':
    main()