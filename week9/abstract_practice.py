#importing the abstract class
from abc import ABC, abstractmethod
from progressbar import printProgressBar
#create  a framework for several character subclasses in the context of a game




class Chara(ABC):
    @abstractmethod
    def size(self):
        pass
    @abstractmethod
    def speed(self):
        pass

class Player(Chara):
    def size(self,size_1=3):
        self.size=size_1
        return self.size
    def speed(self,speed_1=7):
        self.speed=speed_1
        return self.speed

class Bad_guy(Chara):
    def size(self,size_2=2):
        self.size=size_2
        return self.size
    def speed(self,speed_2=3):
        self.speed=speed_2
        return self.speed

class Ally(Chara):
    def size(self,size_3=1):
        self.size=size_3
        return self.size
    def speed(self,speed_3=6):
        self.speed=speed_3
        return self.speed

if __name__ == '__main__':
    A=Player()
    A.size()
    A.speed()
    B=Bad_guy()
    B.size()
    B.speed()
    C=Ally()
    C.size()
    C.speed()
    print()
    print("=======================================================================================")
    print(f" {A} is {A.speed} units per second fast and size {A.size}")
    print(f" {B} is {B.speed} units per second fast and size {B.size}")
    print(f" {C} is {C.speed} units per second fast and size {C.size}")
    print("=======================================================================================")
    print()
    import time

    #progress bar to test that speeds are actually different
    items = list(range(0, 57))
    l = len(items)

    printProgressBar(0, l, prefix = 'Player:', suffix = 'Complete', length = 30)
    for i, item in enumerate(items):
        time.sleep(.1/(A.speed))
        printProgressBar(i + 1, l, prefix = 'Player:', suffix = 'Complete', length = 30)
    printProgressBar(0, l, prefix = 'BadGuy:', suffix = 'Complete', length = 30)
    for i, item in enumerate(items):
        time.sleep(.1/(B.speed))
        printProgressBar(i + 1, l, prefix = 'BadGuy:', suffix = 'Complete', length = 30)
    