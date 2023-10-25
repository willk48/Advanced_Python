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
-lists appear to be a little syntactically confusing with some function calls being func(item) while others are item.func
-book set up the tic tac toe project very well
-did a normal draw style script with a running and exit state
-the hungarian notation part was pretty funny, for some reason it was just a little goofy to take all the work that went into getting rid of explicit types in python just to still keep track of it in the naming scheme. This would also be super confusing if items changed types at any point (size restriction, memory usage, speed)

Week 4 Notes:
-read chapter 6
-i am a little confused on what the Keyword Variadic Arguments section is doing and would like to go over it
-otherwise lambda functions seem pretty cool and intuitive compared to other languages with this functionality
-worked on a simple fibonacci sequence program to practice recursion
-the setup was pretty similar to a java variety, but it helps to not have to explicitly worry about types until the end
-to practice default parameters I remade the Fibonacci program with an extra modifier that could be used to print the n elements up to the selected number
-this part was a bit confusing to write as a standalone program, but I can see the usefulness of this behavior in a situation where arguments are called from -the terminal, similar to how powershell commands work with additional optional parameters
-for a lambda function I wrote a simple higher function that returns the larger of 2 given arguments
-for an example of interior functions I wrote a program that can generate factory functions for given powers (power2(arg), power3(arg), etc.)

Week 5 Notes:
-read Chapter 7
-the classes and methods sections seemed pretty straightforward, similar to other languages and pretty simple to follow
-it feels a little weird syntactically to be doing this without OOP and just writing the rest of the script below, but i can
  assume for larger works with multiple modules this will fall into place more naturally
-im confused on the purpose of the getter and setter method section, in my practice for this week I did not need any of it
-not sure where you would use a special method, seems like a seldom used feature, not really sure whats going on
  in that section
-created a program that ranks cars 0-60 times and allows for the insertion of a new car and time on the list
-learned the print formatting in python
-did several codewars problems and learned some cool list slicing trick and saw a neat lambda function in action