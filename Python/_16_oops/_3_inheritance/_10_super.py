# self - represents current class object
# super - represents immediate parent class object

class Dad:
    def __init__(self):
        print("Parent Class")

    def flat(self):
        print("Dad's Flat")

class Son(Dad):
    def __init__(self):
        super().__init__()
        print("Child Class")

    def bike(self):
        print("Bike")

    def flat(self):
        super().flat()
        print("Son's Flat")

son = Son()
son.bike()
son.flat()

