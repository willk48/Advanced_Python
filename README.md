# Advanced_Python

Week 1 Notes:
-Read Chapter 3
-Completed Coding bat exercises

Notes:
  The match/case function in python seems pretty cool
  The way try catch works here is pretty intuitive as well
  Having some trouble find a use case for some of this string formatting, seems like the kind of thing I would have to lookup to use anyway
  A little confusion on what the guard statement is doing here:

class Special:
  TODAY = 'lasagna'
  
  lunch_order = input("What would you like for
  lunch? ")
  
  match lunch_order:
    case 'salad' | 'soup':
      print('Eating healthy, eh?')
    case ice_cream if 'ice cream' in ice_cream:
      flavor = ice_cream.replace('ice cream', '').strip()
      print(f"Here's your very grown-up {flavor}...lunch.")
    case order:
      print(f"Enjoy your {order}.")

Week 2 Notes:
-Read Chapter 4
-Created a basic script for choosing names out of a hat that utilizes import random
-Created a second script that uses functions from aforementioned and adds funtionality
-Completed Flip the Switch, Remove First and Last Character, Convert a string to an array, Fake Binary, Keep Hydrated, and Reversed Strings on codewars
-calling list() on a string and getting the array is super cool when used in conjuction with str.join()
-importing in python was way weirder than I thought

Week 3 Notes:
-read chapter 5
-learned about the is comparator that compares identity, useful for if something 'is None'
-it may be annoying to do anything with complex modules without global variables
-book set up the tic tac toe project very well
-the hungarian notation part seems pretty funny