from _2_single_inheritance import Dad

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