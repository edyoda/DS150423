from _14_custom_exception import *

class Voting:
    def vote(self):
        age = int(input("Enter your age : "))
        if age >= 18:
            print("Successfully Voted")
        else:
            try:
                raise InvalidAgeError()
            except:
                print("Exception Occured!")

obj = Voting()
obj.vote()


# ATM 

# pin, using re, validate it,  4 digit value
# stored_pin = 1234
# balance = 50000

# Enter : 
# 1. Deposit - ask for the amt , add it with his balance
#     10,20,170,1660
#     25000
# 2. Withdraw - ask for the amt , substract it with his balance
#     10,20,170,1660
#     25000
# 3. Mini-statement - balance