import re

def validate_password(password):
    pattern = r'\A(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&+=!])(?!.*\s).{8,16}\Z'
    if re.findall(pattern, password):
        print("Valid password")
    else:
        print("Invalid password")

pswd = input("Enter password : ")
validate_password(pswd)