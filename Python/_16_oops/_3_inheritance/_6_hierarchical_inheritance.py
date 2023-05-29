# Hierarchical Inheritance : Single parent class and multiple child classess

class country:
    def region(self):
        print("Area")

class India(country):
    def language(self):
        print("Hindi")

class USA(country):
    def language(self):
        print("English")

i_obj = India()
i_obj.region()
i_obj.language()

u_obj = USA()
u_obj.region()
u_obj.language()