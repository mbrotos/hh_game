class Parent(object):
    def __init__(self):
        self.value = 5

    def playGame(self):
        return self.get_value()


    def get_value(self):
        return self.value

class Child(Parent):
    def get_value(self):
        return self.value + 1

child = Child()
print(child.playGame())
