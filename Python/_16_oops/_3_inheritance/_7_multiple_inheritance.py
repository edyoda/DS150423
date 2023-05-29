class mom:
    def jewellery(self):
        print("Jewellery")

class dad:
    def flat(self):
        print("Flat")

class son(mom,dad):
    def bike(self):
        print("Bike")

obj = son()
obj.bike()
obj.flat()
obj.jewellery()