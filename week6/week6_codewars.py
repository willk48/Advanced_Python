#Printer Errors
def printer_error(s):
    errors = ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    err = 0
    
    for char in s:
        if char in errors:
            err += 1
    return str(err)+"/"+str(len(s))

#learned a cool print formatting trick with f-strings 
#that makes this final concatenation really easy, just use {} when refering to variables and it concatenates
#https://realpython.com/python-f-strings/

#    return f"{err}/{len(s)}"

#Count of positives / sum of negatives
def count_positives_sum_negatives(arr):
    pos_count = 0
    neg_sum = 0
    if arr == []:
        return []
    
    for num in arr:
        if num > 0:
            pos_count+=1
        elif num < 0:
            neg_sum+=num
    return [pos_count,neg_sum]

#Calculate BMI
def bmi(weight, height):
    #under<=18.5<normal<=25.0<overweight<=30<obese
    num = weight/(height ** 2)
    if num <= 18.15:
        return "Underweight"
    elif num <= 25:
        return "Normal"
    elif num <= 30:
        return "Overweight"
    else:
        return "Obese"