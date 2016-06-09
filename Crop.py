# -*- coding: utf-8 -*-
"""

@author: 97tobnor
"""

import random

class Crop:
    """En växt"""
    def __init__(self, growth_rate, light_need, water_need):
        """SÄtt attributen till steg 1"""
        self._growth = 0
        self._days_growing = 0
        self._growth_rate = growth_rate
        self._light_need = light_need
        self._water_need = water_need
        self._status = "Seed"
        self._type = "Generic"
    
    def needs(self):
        """Skickar ut vatten och ljus behövnaden"""
        return {'light need':self._light_need,'water need':self._water_need}
    
    """Skickar ut värdena"""
    def report(self):
        return {'type':self._type,'status':self._status,'growth':self._growth,'days growing':self._days_growing}
      
    def _update_status(self):
        if self._growth > 15:
            self._status = "Old"
        elif self._growth > 10:
            self._status = "Mature"
        elif self._growth > 5:
            self._status = "Young"
        elif self._growth > 0:
            self._status = "Seedling"
        elif self._growth == 0:
            self._status = "Seed"
    
    def grow(self,light,water):
        if light >= self._light_need and water >= self._water_need:
                self._growth += self._growth_rate
        self._days_growing += 1
        """Statusen"""
        self._update_status()
        
def auto_grow(crop, days):
    """Väx växten automatiskt"""
    for day in range(days):
        light = random.randint(1,10)
        water = random.randint(1,10)
        crop.grow(light,water)
        
def manual_grow(crop):
    """Måste få ett vatten och ett ljus värde från den som styr programmet"""
    valid = False
    while not valid:
        try:
            light = int(input("Get ett ljus värde(1-10)"))
            if 1 <= light <= 10:
                valid = True
            else:
                print("Värdet du valt är inte korrekt, snälla välj ett värde mellan 1 och  10")
        except ValueError:
            print("Värdet du valt är inte korrekt, snälla välj ett värde mellan 1 och  10")
    valid = False
    while not valid:
        try:
            water = int(input("Välj ett vatten värde(1-10)"))
            if 1 <= water <= 10:
                valid = True
            else:
                print("Värdet du valt är inte korrekt, snälla välj ett värde mellan 1 och  10")
        except ValueError:
            print("Värdet du valt är inte korrekt, snälla välj ett värde mellan 1 och  10")
    """grow the crop"""
    crop.grow(light,water)
    
def display_menu():
    print("1. Väx manuelt 1 dag")
    print("2. Väx automatiskt över 30 dagar")
    print("3. Skicka status")
    print("0. Stäng programmet")
    print()
    print("Välj ett alternativ")
          
          
def get_menu_choice():
    option_valid = False
    while not option_valid:
        try:
            choice = int(input("Option Selected: "))
            if 0 <= choice <= 4:
                option_valid = True
            else:
                print("Du skrev ett felaktigt värde")
        except ValueError:
                print("Skriv ett värde")
    return choice
    
def manage_crop(crop):
    print("Här kan du hantera växter")
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
            auto_grow(crop,30)
            print()
        elif option == 3:
            print(crop.report())
            print()
        elif option == 0:
            noexit = False
            print()
    print("Nu vet du hur mycket växten växt")
            
    
def main():
    """Kör klassen"""
    new_crop = Crop(1, 4, 4)
    """Behövs inte längre för test"""
    manage_crop(new_crop)

if __name__ == "__main__":
    main()
    
    
    
    