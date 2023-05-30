# Abstraction 
# hiding implementation and showing functionality

# abstract method
# - method without body
# - with decorator "abstractmethod"

# abstract class
# - a class with atleast one abstract method
# - we cannot create object of abstract class

from abc import abstractmethod,ABC

class laptop(ABC):

    def keyboard(self):
        print("Keyboard!")

    @abstractmethod
    def motherboard(self):
        pass

# obj = laptop()
# laptop.keyboard()
# laptop.motherboard()

class programmer(laptop):
    def motherboard(self):
        print("Motherboard")

obj = programmer()
obj.motherboard()
obj.keyboard()
