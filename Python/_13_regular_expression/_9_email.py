import re

email_id = input("Enter an email address: ")

code_pattern = r'^[\w\.]+@[a-z]+\.[a-z]{2,5}$' # from special character
is_valid = re.findall(code_pattern, email_id)

if is_valid:
    print("You have Written Valid email address")
else:
    print("Ooops!! Your email address is invalid Please Check")


# password
# atleast 1 capital letter
# atleast 1 small letter
# atleast 1 number
# atleast 1 special character
# min length - 8
# max length - 16






