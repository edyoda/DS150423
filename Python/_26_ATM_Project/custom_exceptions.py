class InvalidFormatError(Exception):
    def __str__(self):
        return 'The format of pin code is incorrect!'
    
class LenghtTooLongError(Exception):
    def __str__(self):
        return 'Pin code is 4 digits.'
    
class CustomerNotFoundError(Exception):
    def __str__(self):
        return 'Incorrect pin entered, Pls contact your bank branch.'
    
class NoChillarAllowedError(Exception):
    def __str__(self):
        return '''\tChillar values are not alowed in the ATM.
                  \tAlso transaction of more than 25,000 is not allowed'''