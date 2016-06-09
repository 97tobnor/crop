# -*- coding: utf-8 -*-
"""

@author: 97tobnor
"""

from PotatoandWheat import*
from Cropsimulation import*
from radiobutton import*
import random

class Crop:
    """En mat skörd"""
    #constructor

    def __init__(self, growth_rate, light_need, water_need):
     #uppger alla attributer    
        self._growth = 0
        self._days_growing = 0
        self._growth_rate = growth_rate
        self._light_need = light_need
        self._water_need = water_need
        self._status = "Seed"
        self._type = "Generic"
        
        #the above attributes are prefixed with an underscore to indicate
        #that they should not be accessed directly from outwith the class
        
    def needs(self):
        return('light need',self._light_need,'water need',self._water_need)
    
    def report(self):
        return('type',self._type,'status',self._status,'growth',self._growth,'days growing',self)
    
    def _update_status(self):
        if self._growth > 15:
            self._status = 'Old'
        elif self._growth > 10:
            self._status = 'Mature'
        elif self._growth > 5:
            self._status = 'Young'
        elif self._growth > 0:
            self._status = 'Seedling'
        elif self._growth == 0:
            self._status = 'Seed'
        
    def grow (self, light, water):
        if light >= self._light_need and water >= self._water_need:
            self._growth += self._growth_rate
        
        self._days_growing += 1
        
        self._update_status()
        
def auto_grow(Crop, days):
    for day in range(days):
        light = random.randint(1,10)
        water = random.randint(1,10)
        Crop.grow(light,water)

def manual_grow(Crop):
    #få vatten och ljus värde från användaren
    valid = False
    while not valid:
        try:
            light = int(input("please enter a light value (1-10): "))
            if 1 <= light <= 10:
                valid = True 
            else:
                print("Value entered not valid = please enter a value between 1 and 10")

                
        except ValueError:
            print("Value entered not valid = please enter a value between 1 and 10")
            
    valid = False
    while not valid:
        try:
            water = int(input("please enter a water value between (1-10): "))
            if 1 <= water <=10:
                valid = True
            else:
                print("Value entered not valid = please enter a value between 1 and 10")
        except ValueError:
            print("Value entered not valid = please enter a value between 1 and 10")
    Crop.grow(light,water)

def display_menu2():
    print()
    print("Which crop would you like to create?")
    print()
    print("1. Potato")
    print("2. Wheat")
    print()
    print("Please select an option from the above menu")
    
def select_option():
    valid_option = False
    while not valid_option:
        try:
            choice = int(input("Option selected: "))
            if choice in (1,2):
                valid_option=True
            else:
                print("Please enter a valid option")
        except ValueError:
            print("Please enter a valid option")
    return choice

def create_crop():
    display_menu()
    choice = select_option()
    if choice == 1:
        new_crop = Potato()
    elif choice == 2:
        new_crop = Wheat()
    return new_crop

def main():
    new_crop = create_crop()
    manage_crop(new_crop)

if __name__ == "__main__":
    main()
    
def display_menu():
    print("1. Grow manually over 1 day")
    print("2. Grow automatically over 30 days")
    print("3. Report status")
    print("0. Exit test program")
    print()
    print("please select an option from the above menu")
    
    
def get_menu_choice():
    option_valid = False
    while not option_valid:
        try:
            choice = int(input("option selected: "))
            if 0 <= choice <= 4:
                option_valid = True
            else:
                print("Please enter valid option")
        except ValueError:
            print("Please enter valid option")
    return choice

def manage_crop(crop):
    print("This is the manage crop program")
    print()
    noexit = True
    while noexit:
        display_menu()
        option = get_menu_choice()
        print()
        if option == 1:
            manual_grow(crop)
            print()
        elif option == 2:
            manual_grow(crop, 30)
            print()
        elif option == 3:
            print(crop.report())
            print()
        elif option == 0:
            noexit = False
            print()
    print("Thank you for using the management program")
    
def main ():
    """en metod som innehåller alla print satser, dessa skriver ut svaren"""
    #instaniate the class
    new_crop = Crop(1,4,3)
    #test to see whether it works or not
    print(new_crop.needs())
    print(new_crop.report())
    manual_grow(new_crop)
    
if __name__ == "__main__":
    main()

class Potato(Crop):
    """en potatis skörd"""
    def __init__(self):
        #kalla förälder classen krontruktor med vanliga värden för potatis
        #growth rate = 1, light need = 3; water need = 6
        super().__init__(1,3,6)
        self.type = "Potato"
    def grow(self, light, water):
        if light >= self._light_need and water >= self._water_need:
            if self._status =="Seedling" and water > self._water_need:
                self._growth += self._growth_rate * 1.5
            elif self._status == "Young" and water > self._water_need:
                self._growth += self._growth_rate * 1.25
            else:
                self._growth += self._growth_rate
        self._days_growing += 1
        self._update_status()

def main():
    potato_crop = Potato()
    print(potato_crop.report())
    manual_grow(potato_crop)
    print(potato_crop.report())
    manual_grow(potato_crop)
    print(potato_crop.report())    

if __name__ == "__main__":
    main()


    
class Wheat(Crop):
    """en vete skörd"""
    def __init__(self):
        #kalla förälder classen krontruktor med vanliga värden för potatis
        #growth rate = 1, light need = 3; water need = 6
        super().__init__(1,3,6)
        self.type = "Wheat"
    def grow(self, light, water):
        if light >= self._light_need and water >= self._water_need:
            if self._status =="Seedling" and water > self._water_need:
                self._growth += self._growth_rate * 1.5
            elif self._status == "Young" and water > self._water_need:
                self._growth += self._growth_rate * 1.25
            else:
                self._growth += self._growth_rate
        self._days_growing += 1
        self._update_status()
        
def main():
    wheat_crop = Wheat()
    print(wheat_crop.report())
    manual_grow(wheat_crop)
    print(wheat_crop.report())
    manual_grow(wheat_crop)
    print(wheat_crop.report())
    

if __name__ == "__main__":
    main()