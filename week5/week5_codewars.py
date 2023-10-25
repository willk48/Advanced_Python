#Returning Strings
def greet(name):
    #Good Luck (like you need it)
    return "Hello, "+name+" how are you doing today?"

#Are You Playing Banjo?
def are_you_playing_banjo(name):
    # Implement me!
    nl=name[:1]
    if nl.lower() == 'r':
        return name +" plays banjo"
    else:
        return name +" does not play banjo"
    
#Removing Elements
def remove_every_other(my_list):
    return my_list[::2]

def remove_every_other(my_list):
    lst = []
    for i in range(len(my_list)):
        if i % 2 == 0:
            lst.append(my_list[i])
    return lst

#Will you make it?
"""
You were camping with your friends far away from home, but when it's time to go back, you realize that your fuel is running out and the nearest pump is 50 miles away! You know that on average, your car runs on about 25 miles per gallon. There are 2 gallons left.

Considering these factors, write a function that tells you if it is possible to get to the pump or not.

Function should return true if it is possible and false if not.
"""
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return mpg*fuel_left>=distance_to_pump
#a cool example i saw and played around with using lambda functions instead
zeroFuel = lambda distance, mpg, gallons: mpg * gallons >= distance
#works effectively the same way in the terminal which is super cool