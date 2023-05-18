import re
pin_no = input('Enter your Aadhar no:   ')
res1 = re.findall(r'\A[1-9]{1}[0-9]{11}\Z', pin_no)
print(res1)
if res1:
    print('Valid Aadhar Number')
else:
    print('Invalid Aadhar Number')



