import re
def validate_pan_number(pan_number):
    pattern = r'\A[A-Z]{5}[0-9]{4}[A-Z]{1}\Z'
    if re.findall(pattern, pan_number):
        print("Valid PAN card number")
    else:
        print("Invalid PAN card number")

pan_no = input('Enter your Permanent Account Number:   ')
validate_pan_number(pan_no)



