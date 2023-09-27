#Flick Switch
#return one until the word flick is found, then switch and remain until the next flick
def flick_switch(lst):
    state = 0
    workL = []
    for item in lst:
        if item == "flick":
            if state == 1:
                state = 0
            elif state == 0:
                state = 1
        match state:
            case 0:
                workL.append(True)
            case 1:
                workL.append(False)
    return workL

#Remove First and Last Character
#Remove the first and last letter from a string
def remove_char(s):
    char_list = []
    for char in s:
        char_list.append(char)
    
    slic_list = char_list[1:len(char_list)-1]
    return "".join(slic_list)

#Convert a string to an array
#work with slice method, super cool thing to have in the toolbelt
def string_to_array(s):
    if s=="":
        return ['']
    return s.split()

#Fake Binary
#turn a string of numbers into a type of binary sequence and return it
def fake_bin(x):
    num_list = list(x)
    new_list = []
    for num in num_list:
        if int(num) >= 5:
            new_list.append("1")
        else:
            new_list.append("0")
    return "".join(new_list)

#Keep Hydrated
#happy to get this in a single line, I remembered the // operator right away when i read round down
#nathan drinks 0.5 liters per hour of cycling, write a function that gives his estimated liters of 
#water intake rounded down to the nearest liter
def litres(time):
    return time//2

#Reversed Strings
#given a string return the string in reverse
#i tried to use the cool join function again combined with 
#the list function when called on a string and it worked 
#pretty well
def solution(string):
    char_list = list(string)
    reversed = []
    for i in range(0,len(char_list)):
        reversed.append(char_list.pop(len(char_list)-1))
    return "".join(reversed)