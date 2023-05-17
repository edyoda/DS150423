import re
pin_no = input('Enert your mobile no:   ')
res1 = re.findall(r'\A[1-9]{1}[0-9]{5}\Z', pin_no)
print(res1)
if res1:
    print('Valid Pincode')
else:
    print('Invalid Pincode')