import threading
import time
import random

WAGE=1.10
S_TIME=0.4
P_TIME=0.9
H_TIME=0.5


def shirt(v=False):
    if (v==False):
        return S_TIME
    else:
        print("Starting:  t_shirt...")
        print("Completed: t_shirt.")
        return S_TIME

def pants(v=False):
    if (v==False):
        return P_TIME
    else:
        print("Starting:  pants...")
        print("Completed: pants.")
        return P_TIME

def hat(v=False):
    if (v==False):
        return H_TIME
    else:
        print("Starting:  hat...")
        print("Completed: hat. ☻")
        return H_TIME

def half_list(a_list):
    len_half = len(a_list)//2
    return a_list[:len_half], a_list[len_half:]

def run_tuple(tup):
    total = 0
    for item in tup:
        total = total + item()
    return total

def run_tuple_no_v(tup):
    for item in tup:
        item()

def main():
    
    
    how_many=int(input("How many items in queue? (Suggested < 15): "))
    print("======================================================================================")
    print("                             One Employee on Staff")
    orderlst=[]
    for i in range(how_many):
        choices = [hat,pants,shirt]
        orderlst.append(random.choice(choices))
    final_orderlst=tuple(orderlst)
    start1=time.perf_counter()
    time_spent = run_tuple(final_orderlst)
    finish1=time.perf_counter()
    
    print(f"Time Spent: {round(time_spent,2)} second(s)")
    print(f"Wages Owed: ${(round(WAGE*(time_spent), 2))}")
    print("======================================================================================")
    print("                             Two Employees on Staff")
    orderlst2=[]
    for i in range(how_many):
        choices = [hat,pants,shirt]
        orderlst2.append(random.choice(choices))
    b, c = half_list(orderlst2)
    persona_orders = tuple(b)
    personb_orders = tuple(c)
    start2=time.perf_counter()
    threads = []
    a = threading.Thread(target=run_tuple_no_v(persona_orders))
    threads.append(a)
    b = threading.Thread(target=run_tuple_no_v(personb_orders))
    threads.append(b)
    a.start()
    b.start()
    for thread in threads:
        thread.join()
    finish2=time.perf_counter()
    if (run_tuple(persona_orders)>run_tuple(personb_orders)):
        time_spent2=run_tuple(persona_orders)
    elif (run_tuple(persona_orders)<run_tuple(personb_orders)):
        time_spent2=run_tuple(personb_orders)

    print(f"Time Spent: {round(time_spent2,2)} second(s)")
    print(f"Wages Owed: ${(round(WAGE*(time_spent2), 2))}, x2 ${((round(WAGE*(time_spent2), 2))*2)}")
    '''print("======================================================================================")
    print("                             4 Employees on Staff")
    orderlst3=[]
    for i in range(how_many):
        choices = [hat,pants,shirt]
        orderlst3.append(random.choice(choices))
    t,u = half_list(orderlst3)
    d,e = half_list(t)
    f,g = half_list(u)
    per1 = tuple(d)
    per2 = tuple(e)
    per3 = tuple(f)
    per4 = tuple(g)
    
    threads = []
    a1 = threading.Thread(target=run_tuple(d))
    threads.append(a1)
    b1 = threading.Thread(target=run_tuple(e))
    threads.append(b1)
    c1 = threading.Thread(target=run_tuple(f))
    threads.append(c1)
    d1 = threading.Thread(target=run_tuple(g))
    threads.append(d1)
    a1.start()
    b1.start()
    c1.start()
    d1.start()

    for thread in threads:
        thread.join()
    time_spent3=0
    if (run_tuple(d)>run_tuple(e)):
        time_spent3=run_tuple(d)
    elif (run_tuple(d)<run_tuple(e)):
        time_spent3=run_tuple(e)

    print(f"Time Spent: {round(time_spent3,2)} second(s)")
    print(f"Wages Owed: ${(round(WAGE*(time_spent3), 2))}, x4 ${((round(WAGE*(time_spent3), 2))*4)}")'''
if __name__ == '__main__':
    main()