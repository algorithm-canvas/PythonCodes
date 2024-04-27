class Demo:
    def check(self):
        return "Demo Check"
    def display(self):
        print(self.check())
class Demo_Derived(Demo):
    def check(self):
        return "Derived Check"

Demo().display()
Demo_Derived().display()            