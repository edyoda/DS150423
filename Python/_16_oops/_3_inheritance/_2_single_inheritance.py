# Single Inheritance - One child class inheriting one parent class

class Dad:
    def flat(self):
        print("Flat")

    def car(self):
        print("Car")

class Son(Dad):
    def bike(self):
        print("Bike")

    def mobile(self):
        print("Mobile")

son = Son()
son.bike()
son.mobile()
son.flat()
son.car()
