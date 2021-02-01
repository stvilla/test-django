#import test
import logging
#import app

class Vehicle:
    def __init__(self,places,wheels):
        self.p = places
        self.w = wheels
        self.is_locked = False
    
    def lock(self):
        self.is_locked = True

    def unlock(self):
        self.is_locked = False

    def __str__(self):
        return f"Wheels = {self.w}, Places = {self.p}, is_locked = {self.is_locked}"

class Car(Vehicle):
    def __init__(self,places):
        super().__init__(places, 4) 
        self.is_on = False
    
    def start(self):
        self.is_on = True
    def stop(self):
        self.is_on = False
    def __str__(self):
        s = super().__str__()
        return s + f" and is_on = {self.is_on}"

#logging.basicConfig(level = logging.ERROR, format="%(asctime)s %(levelname)s: %(name)s -> %(message)s")

#logging.debug("Debug message")
#logging.info("Info message")

smart = Car(2)
print(smart)

def ciao(a,b):
    print(a,b)

ciao(1,2)
ciao(a = 1, b=2)
ciao(b = 2, a = 1)
ciao(1, b = 2)
ciao(a = 1, 2)