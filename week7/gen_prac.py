import collections
#practice using generators to solve previous solutions
#fibonacci
def fib_gen(up_to):
    a=0
    b=1
    for i in range(up_to):
        yield a
        a,b = b, a+b
    

if __name__ == '__main__':
    print("=================================================")
    print("1. Fibonacci Gen")
    print("2. Alphabetize")
    print("Type Any Other # to Exit")
    print("=================================================")
    user_in=int(input("Selection: "))
    print("=================================================")
    match user_in:
        case 1:
            n=int(input("How many values would you like to print: "))
            print("=================================================")
            for i in fib_gen(n):
                print(i)
        #working with a set
        case 2:
            print("This program will automatically aphabetize words")
            print("Input a word to begin, type 'END' to exit")
            print("=================================================")
            a_set=set()
            on = True
            while on == True:
                word = input("Input a word: ")
                if word == 'END':
                    on = False
                    break
                else:
                    a_set.add(word.lower())
                    print(sorted(a_set))
        case _:
            pass