if __name__ == '__main__':
    user_in = input("Enter 2 integers sperated by a space and this program will return the higher number: ")
    lst = user_in.split()
    num1=lst[0]
    num2=lst[1]

    higher_number = lambda a,b : a if(a>b) else b
    print()
    print(higher_number(num1,num2))