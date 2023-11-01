# use exceptions to create a simple higher lower guessing game
# the computer will choose a random number and the player will guess it
# hints will be given using the error handling pipeline to practice usage
import random

number = random.randint(1,20)
done = False

class too_high_e(Exception):
    "Raised when the input value is greater than the hidden number"
    pass

class too_low_e(Exception):
    "Raised when the input value is less the hidden number"
    pass

class got_it_e(Exception):
    "Raised when a user has correctly guessed the hidden number"
    pass
while not done:
    try:
        input_num = int(input("Enter a number: "))
        if input_num == number:
            print("You got it! ")
            raise got_it_e
        elif input_num < number:
            raise too_low_e
        elif input_num > number:
            raise too_high_e
    except got_it_e:
            done = True
            print("**<X> Exception occurred: User has correctly guessed the number <X>**")
    except too_high_e:
        print("<!> Too High! Try Again <!>")
    except too_low_e:
        print("<!> Too Low! Try Again <!>")
    except ValueError as e:
        print("<!> At least try and give a NUMBER <!>")