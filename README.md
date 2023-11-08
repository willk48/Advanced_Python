# Advanced_Python

Week 1 Notes:
-Read Chapter 3\
-Completed Coding bat exercises\

Notes:\
  The match/case function in python seems pretty cool\
  The way try catch works here is pretty intuitive as well\
  Having some trouble find a use case for some of this string formatting, seems like the kind of thing I would have to lookup to use anyway\
  A little confusion on what the guard statement is doing here:\

class Special:\
  TODAY = 'lasagna'\
  
  lunch_order = input("What would you like for\
  lunch? ")\
  
  match lunch_order:\
    case 'salad' | 'soup':\
      print('Eating healthy, eh?')\
    case ice_cream if 'ice cream' in ice_cream:\
      flavor = ice_cream.replace('ice cream', '').strip()\
      print(f"Here's your very grown-up {flavor}...lunch.")\
    case order:\
      print(f"Enjoy your {order}.")\

Week 2 Notes:
-Read Chapter 4\
-Created a basic script for choosing names out of a hat that utilizes import random\
-Created a second script that uses functions from aforementioned and adds funtionality\
-Completed Flip the Switch, Remove First and Last Character, Convert a string to an array, Fake Binary, Keep Hydrated, and Reversed Strings on codewars\
-calling list() on a string and getting the array is super cool when used in conjuction with str.join()\
-importing in python was way weirder than I thought\

Week 3 Notes:
-read chapter 5\
-learned about the is comparator that compares identity, useful for if something 'is None'\
-it may be annoying to do anything with complex modules without global variables\
-lists appear to be a little syntactically confusing with some function calls being func(item) while others are item.func\
-book set up the tic tac toe project very well\
-did a normal draw style script with a running and exit state\
-the hungarian notation part was pretty funny, for some reason it was just a little goofy to take all the work that went into getting rid of explicit types\ in python just to still keep track of it in the naming scheme. This would also be super confusing if items changed types at any point (size restriction, memory\ usage, speed)

Week 4 Notes:
-read chapter 6\
-i am a little confused on what the Keyword Variadic Arguments section is doing and would like to go over it\
-otherwise lambda functions seem pretty cool and intuitive compared to other languages with this functionality\
-worked on a simple fibonacci sequence program to practice recursion\
-the setup was pretty similar to a java variety, but it helps to not have to explicitly worry about types until the end\
-to practice default parameters I remade the Fibonacci program with an extra modifier that could be used to print the n elements up to the selected number\
-this part was a bit confusing to write as a standalone program, but I can see the usefulness of this behavior in a situation where arguments are called from\ -the terminal, similar to how powershell commands work with additional optional parameters\
-for a lambda function I wrote a simple higher function that returns the larger of 2 given arguments\
-for an example of interior functions I wrote a program that can generate factory functions for given powers (power2(arg), power3(arg), etc.)\

Week 5 Notes:
-read Chapter 7\
-the classes and methods sections seemed pretty straightforward, similar to other languages and pretty simple to follow\
-it feels a little weird syntactically to be doing this without OOP and just writing the rest of the script below, but i can\
  assume for larger works with multiple modules this will fall into place more naturally\
-im confused on the purpose of the getter and setter method section, in my practice for this week I did not need any of it\
-not sure where you would use a special method, seems like a seldom used feature, not really sure whats going on\
  in that section\
-created a program that ranks cars 0-60 times and allows for the insertion of a new car and time on the list\
-learned the print formatting in python\
-did several codewars problems and learned some cool list slicing trick and saw a neat lambda function in action\

Week 6 Notes:\
-read Chapter 8\
-this is first time I have seen this notation of LBYL and EAFP to describe error handling behavior\
-usually in other languages you have to check before or the program might not even run\
-I added the code referenced in the book to my rank cars program starting at line 53\
-Other than some semantics, this seems very similar to error handling in java, 'catch the default error',\
   if the error is not specific enough write your own etc.\
-functionally in python 'throws' is replaced by raise\
-wrote a quick program to raise an exception to see some of the default behavior\
-It is interesting to think about when a raised exception would be used over a series of blocks\
-at a cursory glance it seems like the most likely use case would be internal processes that\
  need to reference whether or not a function has exectued before proceeding. As in, if I had a function\
  A that has subprocesses a and b which depend on the type of the argument. I may want subprocesses to return errors\
  and break rather than hanging and waiting for my try block to kick in.
-the finally structure is pretty cool and leaves time to close file or input streams and tidy up in practice\ 
-wrote a simple higher lower guessing game using exceptions to practice the syntax\
-did a few code wars, the higher lower game was pretty tough to nail down perfectly,\
  so that was the majority of my time spent this week\

Week 7 Notes:\
-its pretty cool that while loops have an else clause, I did not know that going in\
-tuple, list, deque, set, and dict\
-adding a comma after a single item to initialize a tuple seems pretty cool,\
  im sure it will come up at some point i.e. order = ("latte",)\
-deques seem super cool and I will probably make a program that uses this\
-sets also seems like a super cool data type and I will do something with this too\
-dictionaries are just hashmaps so that seems pretty straightforward\
-alot of these iterable built-ins seem super useful\
-time example on page 413 is pretty cool to show how python evaluates all the items at launch\
-generator seems like an interesting albiet hard to use structure. I am not sure if I will\
  have time this week to make something with this, but it might be worth it at some point\
-There was a lot to cover in these chapters and I am feeling a bit overmatched material wise\
  by this volume of new information\
-"Make sure you only use a list comprehension when you actually need a list object"\
-"There’s something about powerful one-liners that gets programmers very excited.\ 
  We really like being clever with our code."\
-I will probably make a list comprehension in addition to playing with a deque and a set\
-I am a little confused on what is going on in the coroutine section starting at page 450\
  What is going on with the yield here?\
-created a program that does the fib sequence with a generator instead of the stanadard way\
-really helped me see how satisfying it was when it it worked out in so few lines\
-I wrote that part several more convoluted ways and encountered strange outputs\
-turns out simplifying my code was the best way to avoid this\
-wrote a simple program to alphabetize words that the user inputs in real time with a set\
-set comes with some cool built-ins in addition to auto deleting duplicates, super neat\
-played around with a deque in a bit of a play on words by making the game of War card game\
-that game made the most sense to me for a deque because the game needs to maintain the order\
  of the players cards as each deck inevitably loops until a player wins\
-I did not fully encorperate the rules of the game based on time limitations and I was unable to implement\
  different handling for face cards and played all the hands by sheer numerical value\
-aces are 0s and beat all\
-this game actually rarely terminates in this format, so to make sure I terminate on simming, I had to make\
 the player win all ties\
-these are semantic problems that are outside the scope of what I am trying to learn here, so this is where I\
  decided to stop\
-added cool hidden functionality to SIM the whole game if you type 'SIM' instead of pressing enter\
-At this point I am about 5.5 hours into this weeks work and I do not think I will get any codewars done for this week.\


