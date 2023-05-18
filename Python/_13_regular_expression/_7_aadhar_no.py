# 1st Way
# import re

# aadhaar_number = input("Enter Aadhaar number: ")

# if re.findall(r'^\d{4}-\d{4}-\d{4}$', aadhaar_number):
#     print("Valid Aadhaar number:", aadhaar_number)
# else:
#     print("Invalid Aadhaar number.")



# 2nd Way
import re
aadhar_no = input("Enter the  Aadhar no :  ")
res = re.findall("^[1-9]{1}[0-9]{3}[-][0-9]{4}[-][0-9]{4}$", aadhar_no)
print(res)
if res:
    print("Valid Aadhar Number")
else:
    print("Invalid Aadhar Number")
