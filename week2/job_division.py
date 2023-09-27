from names_hat import make_list
import random

print()
print("     This program will take a list of names and jobs")
print("         and randomly pair a person with a job")
print()
names_list = make_list("How many people are there? ", "Enter a Name: ")
print()
jobs_list = make_list("How many jobs are there to do? ","Enter a Job: ")
names_list_burned = []
print()

for i in range(0,len(names_list)):
    if len(jobs_list) == 0:
        break
    if len(names_list) == 0 and len(jobs_list) != 0:
        names_list.append(random.choice(names_list_burned))
    curr_job = random.choice(jobs_list)
    curr_person = random.choice(names_list)
    print(curr_person+" , you got "+curr_job)
    jobs_list.remove(curr_job)
    names_list_burned.append(curr_person)
    names_list.remove(curr_person)
    
