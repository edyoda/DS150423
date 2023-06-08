from custom_exceptions import *
import re
import json
class ATM:
    with open(r'C:\Users\vashi\OneDrive\Documents\DS150423\Python\_26_ATM_Project\customer.json') as file1:
        customer = json.load(file1)
    
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
                    if deposit%100 != 0 or deposit>25000:
                        raise NoChillarAllowedError()
                    
                    balance = self.customer[self.pin_no]
                    balance += deposit
                    self.customer[self.pin_no] = balance
                    self.json_update()
                    self.storage()
                    print(f'Deposit Complete! Your current balance is {balance} rupees only')

                elif choice == 2:
                    withdraw = int(input('Enter amount to be withdrawn:   '))
                    if withdraw%100 != 0 or withdraw > 25000:
                        raise NoChillarAllowedError()
                    balance = self.customer[self.pin_no]
                    balance -= withdraw
                    self.customer[self.pin_no] = balance
                    self.json_update()
                    self.storage()
                    print('Kchrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr! withdrawl complete')
                    print(f'Your current balance is {balance} rupees only')

                elif choice == 3:
                    statement = self.retrive_data()
                    print(statement)
                    
                    
                elif choice == 4:
                    print("Thank You for connecting with us!")
                    exit(1)      #V.imp , instead of break you can use this.
        else:
            raise CustomerNotFoundError()
        
    def storage(self):
        with open(f'{self.pin_no}.txt', 'a+') as file3:
            file3.write(f'{self.customer[self.pin_no]}\n')

    def json_update(self):
        with open(r'C:\Users\vashi\OneDrive\Documents\DS150423\Python\_26_ATM_Project\customer.json', 'w') as file2:
            json.dump((self.customer), file2)            

    def retrive_data(self):
        with open(f'{self.pin_no}.txt', 'a+') as file4:
            file4.seek(0)       
            data = file4.read()
            latest_balance = data.strip('\n').split('\n')[-1]
            # print(latest)            
            # print(data)
            return f'''
\t\t  STATE BANK OF INDIA
                      
YOUR BALNCE REMAINING IS : {latest_balance}

Transaction history:

{data}    

            Thank you for using our services\n
'''
    



branch1 = ATM()
branch1.pin()
branch1.action()