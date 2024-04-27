class Animal:
    def sound(self):
        print("Animal sound", end = ' ')

class Pig(Animal):
    def sound(self):
        print("Bruuu", end = ' ')

class Snake(Animal):
    def sound(self):
        print("Piss", end = ' ')                

a = Animal()
d = Pig()
c = Snake()

a.sound()
d.sound()
c.sound()