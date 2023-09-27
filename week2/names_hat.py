import random

def make_list(prompt, items):
    lst = []
    num = int(input(prompt))
    for i in range(0,num):
        name = input(items)
        lst.append(name)
    return lst

def main():
   print()
   print("      Enter names in any order (seperated by a return)")
   print("         and I will select 1 name from the group")
   print()
   unlucky = random.choice(make_list("How many people are there? ", "Enter a Name: "))
   print()
   print("Sorry * "+unlucky+" *, you drew the short straw :(")

if __name__ == '__main__':
  main()