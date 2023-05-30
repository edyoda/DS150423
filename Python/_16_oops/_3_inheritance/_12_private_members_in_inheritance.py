# if there is some parent class data which you don't want your child class to
# have access to then we can make it private and restrict it's access just by
# adding "__" before variable/method

class Dad:
    def flat(self):
        print("Flat")

    def car(self):
        print("Car")

    def __fd(self):
        print("FD")

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
son.fd()
