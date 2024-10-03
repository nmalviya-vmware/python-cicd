class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def intorduce_self(self):
        print("My name is {}".format(self.name))


r1 = Robot("Tom", "Red", "30")
r2 = Robot("Jerry", "Yellow", "40")
r1.intorduce_self()
r2.intorduce_self()
