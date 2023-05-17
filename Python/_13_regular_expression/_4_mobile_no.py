import re
def mobile(s):
    res = re.findall("^[1-9]{1}[0-9]{9}$",s)
    return res

s = "1234567891"
if (mobile(s)):
    print ("Valid Number")    
else :
    print ("Invalid Number")