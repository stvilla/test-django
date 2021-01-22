import test

class Car:
    def __init__(self,places):
        print("Car")
        self.p = places
        self.is_on = False
    
    def start(self):
        self.is_on = True
    def __str__(self):
        return "Places = " + str(self.p) + " is_on = " + str(self.is_on)

def test(a):
    print(a)

#test()

c = Car(4)
print(c)
c.start()
print(c)

test("ciao")

print(__name__)

#my_str = "ciao"
#print(my_str.capitalize())