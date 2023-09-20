# Advanced_Python

Week 1 Notes:
-Read Chapter 3
-Completed Coding bat exercises
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
