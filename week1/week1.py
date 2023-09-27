# Week 1 work on code bat
# Mostly review of the basics although I did have to look up some function names
# Lists actually don't come up in the book for a little bit so I had to look that
# documentation up online
# Exercise solutions follow

#Warmup-1 > sleep_in
def sleep_in(weekday, vacation):
  if not weekday:
    return True
  elif vacation:
    return True
  else:
    return False

 #Warmup-1 > monkey_trouble
def monkey_trouble(a_smile, b_smile):
  if a_smile and b_smile:
    return True
  elif not a_smile and not b_smile:
    return True
  else:
    return False

#Warmup-2 > string_times
def string_times(str, n):
  str1 = str
  if n == 0:
    return ""
  for i in range(1,n):
    str=str+str1
  return str

#Warmup-2 > front_times
def front_times(str, n):
  strPre = str[0:3]
  strF = ""
  if n == 0:
    return ""
  for i in range(0,n):
    strF = strF + strPre
  return strF

#String-1 > hello_name
def hello_name(name):
  return "Hello "+name+"!"

#String-1 > make_abba
def make_abba(a, b):
  return a+b+b+a

#List-1 > first_last6
def first_last6(nums):
  if nums[0]==6:
    return True
  elif nums[len(nums)-1]==6:
    return True
  else:
    return False

#List-1 > make_pi
def make_pi():
  pi = [3, 1, 4]
  return pi

#Logic-1 > in1to10
def in1to10(n, outside_mode):
  lis = [1,2,3,4,5,6,7,8,9,10]
  if outside_mode:
    return n<=1 or n>=10
  else:
    return n in lis

#Logic-1 > near_ten
def near_ten(num):
  lst = [0,1,2,8,9]
  return (num % 10) in lst

#Logic-2 > no_teen_sum
def no_teen_sum(a, b, c):
  return (fix_teen(a)+fix_teen(b)+fix_teen(c))

def fix_teen(n):
  lst = [13,14,17,18,19]
  if n in lst:
    return 0
  else:
    return n

#Logic-2 > round_sum
def round_sum(a, b, c):
  return (round10(a)+round10(b)+round10(c))

def round10(num):
  if num % 10 in [0,1,2,3,4]:
    return (num // 10)*10
  else:
    return ((num // 10)*10)+10

#String-2 > double_char
def double_char(str):
  strF = ""
  for x in str:
    strF = strF+x+x
  return strF

#String-2 > end_other
def end_other(a, b):
  a = a.lower()
  b = b.lower()
  return a[-(len(b)):] == b or a == b[-(len(a)):]

#List-2 > count_evens
def count_evens(nums):
  count = 0
  for x in nums:
    if x % 2 == 0:
      count+=1
  return count

#List-2 > big_diff
def big_diff(nums):
  large=0
  small=99
  for x in nums:
    if x < small:
      small = x
    if x > large:
      large = x
  return large-small
