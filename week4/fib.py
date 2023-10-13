def fib(n):
    n = int(n)
    match n:
        case 0:
            return 0
        case 1:
            return 1
        case 2:
            return 1
        case _:
            return fib(n-1)+fib(n-2)
        

if __name__ == '__main__':
    print()
    print("      this program will print the ")
    print("(n)th element of the fibonacci sequence")
    print()
    num = input("Enter a number: ")
    print()
    print("Element "+str(num)+" in the Fibonacci Sequence is "+str(fib(num)))