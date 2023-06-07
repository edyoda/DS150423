# datetime module - helps to code wrt to date and time

import datetime as dt

current_date = dt.datetime.now()
print("Current Date : ",current_date)

print("A : ",current_date.strftime("%A"))

print("a : ",current_date.strftime("%a"))

print("B : ",current_date.strftime("%B"))

print("b : ",current_date.strftime("%b"))

print("C : ",current_date.strftime("%C"))

print("c : ",current_date.strftime("%c"))

print("D : ",current_date.strftime("%D"))

print("d : ",current_date.strftime("%d"))

print("X : ",current_date.strftime("%X"))

print("x : ",current_date.strftime("%x"))

print("S : ",current_date.strftime("%S"))


# year = current_date.year
# print("Year : ",year)

# month = current_date.month
# print("Month : ",month)

# day = current_date.day
# print("Day : ",day)

# hr = current_date.hour
# print("Hour : ",hr)

# mins = current_date.minute
# print("Minute : ",mins)

# seconds = current_date.second
# print("Second : ",seconds)

# ms = current_date.microsecond
# print("Millisecond : ",ms)

# date = dt.datetime(2022,6,10,20,7,6,6132)
# print(date)