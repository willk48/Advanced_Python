#Return Two Highest Values in List
#first attempt, went with my gut and tried to just iterate through and keep a running tab of the 2 highest numbers encountered
#it appears to work for small inputs but 
def two_highest(arg1):
    first = 0
    second = 0
    
    for i in range(0, len(arg1)):
        if arg1[i] > first and arg1[i] > second:
            first = arg1[i]
        elif arg1[i] < first and arg1[i] > second:
            second = arg1[i]
    
    if first == 0 and second == 0:
        return []
    elif second == 0:
        return [first]    
    else:
        return [first, second]
#this did not work for truthfully unknown reasons. I'm sure I am just missing something easy but I decided at this point to rethink my approach
#after some more careful reading of what lists could do in python I succeeded with this solution
def two_highest(arg1):
    if arg1 == []:
        return []
    else:
        arg1 = list(set(arg1))
        print(arg1)
        arg1.sort(reverse=True)
        print(arg1)
        if len(arg1)>2:
            print([arg1[0],arg1[1]])
            return [arg1[0],arg1[1]]
        elif len(arg1)==1:
            print([arg1[0]])
            return [arg1[0]]
        elif arg1[0] == 0:
            return []
#this solution uses set to remove duplicates from the list and then sort to sort the list in descending order
#after this process I just trim the list down to the requested size and return 

#Invert values
#This is a problem that requires the copying of a list just to hammer it into my mind that you cant just do =
#turns out after some research there are lots of ways to do this. Useful here are import copy (.copy, .deepcopy) and just calling list(original list)
def invert(lst):
    copy_list = list(lst)
    for i in range(0,len(lst)):
        copy_list[i]=copy_list[i]*-1
    return copy_list
#this did not modify the original as intended
#in true codewars fashion, it turns out there was an even easier way to do this one too XD
#def invert(lst):
#    return [-x for x in lst]
#The only language where you can just write return the thing but negative