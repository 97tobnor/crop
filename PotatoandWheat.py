# -*- coding: utf-8 -*-
"""

@author: 97tobnor
"""

from Crop import *
from radiobutton import *
from Cropsimulation import*



class Potato(Crop):
    """A potato crop"""
    
    """The constructor"""
    def __init__(self):
        """call the original class constructor with defult values, light, growth rate etc"""
        super().__init__(1,3,6)
        self._type = "Potato"
        
    """now to override the growth method or pholymorphism"""
    def grow(self,light,water):
        if light >= self._light_need and water >= self._water_need:
            if self._status == "Seedling" and water > self._water_need:
                self._growth += self._growth_rate * 1.5
            elif self._status == "Young" and water > self._water_need:
                self._growth += self._growth_rate * 1.25
            else:
                self._growth += self._growth_rate
        """Now increament the growing over the day"""
        self._days_growing += 1
        """Then update status"""
        self._update_status()
        
def main():
    """The new potato crop"""
    potato_crop = Potato()
    print(potato_crop.report())
    """Now to manually grow the crop"""
    manual_grow(potato_crop)
    print(potato_crop.report())
    
if __name__ == "__main__":
    main()
    
    """Wheat inheritance"""

class Wheat(Crop):
    """A wheat crop"""
    
    """The constructor"""
    def __init__(self):
        """call the original class constructor with defult values, light, growth rate etc"""
        super().__init__(1,3,6)
        self._type = "Wheat"
        
    """now to override the growth method or pholymorphism"""
    def grow(self,light,water):
        if light >= self._light_need and water >= self._water_need:
            if self._status == "Seedling" and water > self._water_need:
                self._growth += self._growth_rate * 2.5
            elif self._status == "Young" and water > self._water_need:
                self._growth += self._growth_rate * 2.25
            else:
                self._growth += self._growth_rate
        """Now increament the growing over the day"""
        self._days_growing += 1
        """Then update status"""
        self._update_status()
        
def main():
    """The new wheat crop"""
    wheat_crop = Wheat()
    print(wheat_crop.report())
    """Now to manually grow the crop"""
    manual_grow(wheat_crop)
    print(wheat_crop.report())
    
if __name__ == "__main__":
    main()
    
    """Selection menu, between potato and wheat"""

def display_menu():
    print()
    print("Which crop would you like to create?")
    print()
    print("1. Potato")
    print("2. Wheat")
    print()
    print("please select an option from the above menu")
    
def select_option():
    valid_option = False
    while not valid_option:
        try:
            choice = int(input("Option selected: "))
            if choice in (1,2):
                valid_option = True
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