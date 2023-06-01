try:
    print(10/0)
except (ZeroDivisionError,ValueError) as ex:
    print("Exception occured : ",ex) 