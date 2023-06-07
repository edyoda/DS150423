from custom_exceptions import *
import re

class ATM:

    customer = {'1234':80000, '5678':90000 }
    
    def pin(self):
        pin_no = input('Enter your pin:   ')
        lst = re.findall('^[0-9]{4}$', pin_no)
        if not lst:
            self.pin_no = None
        else:
            self.pin_no = pin_no
        return self.pin_no
    
    def action(self):
        
        if self.pin_no == None:
            raise InvalidFormatError()
        if self.pin_no in self.customer:
            while True:
                print()
                choice = int(input('''    CHOICES
                1. Deposit
                2. Withdrawl
                3. Ministatement
                4. Exit

                
                Enter your Choice:  ''' 
                ))
                if choice == 1:
                    deposit = int(input('Enter amount to be deposited:   '))
                    if deposit%100 != 0 and deposit>25000:
                        raise NoChillarAllowedError()
                    
                    balance = self.customer[self.pin_no]
                    balance += deposit
                    self.customer[self.pin_no] = balance
                    print(f'Deposit Complete! Your current balance is {balance} rupees only')

                elif choice == 2:
                    withdraw = int(input('Enter amount to be withdrawn:   '))
                    if withdraw%100 != 0 and withdraw > 25000:
                        raise NoChillarAllowedError()
                    balance = self.customer[self.pin_no]
                    balance -= withdraw
                    self.customer[self.pin_no] = balance
                    print('Kchrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr! withdrawl complete')
                    print(f'Your current balance is {balance} rupees only')

                elif choice == 3:
                    print(f'''
                        \t  STATE BANK OF INDIA
                        
                        YOUR BALNCE REMAINING IS : {self.customer[self.pin_no]}
                        
                        Thank you for using our services\n''')
                    
                elif choice == 4:
                    print("Thank You for connecting with us!")
                    exit(1)
        else:
            raise CustomerNotFoundError()
        

branch1 = ATM()
branch1.pin()
branch1.action()
