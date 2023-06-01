try:
    print(10/0)
except ZeroDivisionError as ex:
    print("Exception occured!",ex)