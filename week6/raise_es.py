#Practice with Raising Exceptions
inp=None
while inp is None:
    try:
        inp = int(input("Enter a Number between 1 and 10: "))
        if inp > 10 or inp < 1:
            raise IndexError("<!> I said between 1 and 10 , Try Again! <!>")
    except ValueError as e:
        print("<!> At least try and give a NUMBER <!>")
    else:
        print("Nice job, You did it!")
    finally:
        print("Finally...")