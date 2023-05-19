import re

s = "1234567891"
pattern = re.compile("^[1-9]{1}[0-9]{9}$")
res = pattern.search(s)

if (res):
    print ("Valid Number")    
else :
    print ("Invalid Number")