from abc import ABC,abstractmethod

class College(ABC):
    def timing(self):
        print("10am-1pm")

    @abstractmethod
    def hall_ticket(self):
        pass

class ClassA(College):
    def hall_ticket(self):
        print("IT Hall Ticket")

class ClassB(College):
    def hall_ticket(self):
        print("CS Hall Ticket")

class ClassC(College):
    def hall_ticket(self):
        print("BSC Hall Ticket")

        