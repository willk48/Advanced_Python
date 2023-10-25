#a program to rank cars by 0-60 time and allow for the 
#addition and ranking of new cars on the list by the user

class Car:
    def __init__(self, name, time):
        self.name = name
        self.time = time

    def compare_to(self, other_car):
        if self.time > other_car.time:
            return True
        elif self.time < other_car.time:
            return False
        else:
            pass

def get_time(car):
    return car.time


def sort_car_list(lst):
    return lst.sort(key=get_time)

if __name__ == '__main__':
    c1 = Car("2010 Acura TSX", 6.0)
    c2 = Car("1991 Acura NSX", 5.4)
    c3 = Car("1950 Aston Martin DB2", 10.9)
    c4 = Car("1985 BMW M5", 7.3)
    c5 = Car("1984 Buick Regal T Type", 8.0)
    c6 = Car("2016 Dodge Viper ACR", 3.4)
    c7 = Car("2012 Ford Mustang Boss 302", 4.1)
    c8 = Car("1968 Toyota 2000GT", 9.0)
    c9 = Car("2005 Honda Jazz 1.2", 13.2)
    c10 = Car("2002 Honda Civic LX Sedan", 9.3)
    c11 = Car("2008 Mazda 5 Touring", 8.9)
    c12 = Car("2022 Bugatti Chiron Super Sport", 2.2)
    c13 = Car("2024 Rimac Nevera", 1.7)

    car_list = [c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13]
    print()
    print("===============================================================")
    print("   ____              _____ ____     _______                    ")
    print("  / __ \            / ___// __ \   /_  __(_)___ ___  ___  _____")
    print(" / / / /  ______   / __ \/ / / /    / / / / __ `__ \/ _ \/ ___/")
    print("/ /_/ /  /_____/  / /_/ / /_/ /    / / / / / / / / /  __(__  ) ")
    print("\____/            \____/\____/    /_/ /_/_/ /_/ /_/\___/____/  ")
    print()
    print("===============================================================")
    print()
    print("Would you like to:")
    print("1: View the current list of times")
    print("2: Add a Car and see how it lines up")
    user_in = int(input("Selection: "))
    print()
    print("===============================================================")
    if user_in == 1:
        sort_car_list(car_list)
        for i in range(0,len(car_list)):
            print("Car: %s, Time: %f" % (car_list[i].name,car_list[i].time))
        print("===============================================================")
    elif user_in == 2:
        car_name = input("Enter the Name of the Car (case sensitive): ")
        car_time = float(input("Enter the Time Including a Decimal: "))
        print()
        user_car = Car(car_name,car_time)
        car_list.append(user_car)
        sort_car_list(car_list)
        for i in range(0,len(car_list)):
            print("Car: %s, Time: %f" % (car_list[i].name,car_list[i].time))
        print("===============================================================")
