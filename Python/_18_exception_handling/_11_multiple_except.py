try:
    
    str1 = None
    print(len(str1))
    print(10/0)

except ZeroDivisionError as ex:
    print("ZeroDivisionError")
except TabError as ex:
    print("TabError")
except KeyError as ex:
    print("KeyError")
except Exception as ex:
    print("Exception")