def fib(n, o='f'):
    n = int(n)

    if o == 'f':
        match n:
            case 0:
                return 0
            case 1:
                return 1
            case 2:
                return 1
            case _:
                return fib(n-1)+fib(n-2)
    elif o == 't':
        fib_literal(n)

def fib_literal(m):
    lst = []
    for i in range(0,m+1):
        lst.append(fib(i))
    return lst

if __name__ == '__main__':
    print("This program will print the (n)th element of the Fibonacci Sequence")
    print("Enter a 1 to receive results as a single number or,")
    print("Enter a 2 to receive the set up to that number")
    lit = input("Selection: ")
    if int(lit) == 1:
        num = input("Enter a non-negative number: ")
        print()
        print("Element "+str(num)+" in the Fibonacci sequence is "+str(fib(num)))
        print()
    elif int(lit) == 2:
        num = input("Enter a non-negative number: ")
        print()
        print(fib_literal(int(num)))
        print()
        print("Element "+str(num)+" in the Fibonacci sequence is "+str(fib(num)))
        print()
    else:
        print("Enter a 1 or a 2...")