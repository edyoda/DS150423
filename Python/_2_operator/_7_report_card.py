# rno
# name
# english, maths, science (each paper is out of 100)
# total
# percentage

roll = input("Enter roll_no of student : ")
name = input("Enter the name of student : ")
eng_mks = float(input ("Enter english marks : "))
maths_mks = float(input ("Enter maths marks : "))
hindi_mks = float(input("Enter hindi marks : "))
total = eng_mks+maths_mks+hindi_mks
percentage = (total*100) / 300
if percentage>=90:
    grade = "A"
elif percentage>=80:
    grade = "B"
elif percentage>=70:
    grade = "C"
elif percentage>=60:
    grade = "D"
elif percentage>=50:
    grade = "E"
else:
    grade = "F"


if percentage>90:
    print('You are awarded with the Grade:  A')
elif percentage > 80 and percentage <= 90:
    print('You are awarded with the Grade:  B')
elif percentage > 70 and percentage <= 80:
    print('You are awarded with the Grade:  C')
else:
    print('We are too lazy to code a Grade as low as yours')

print("Roll No. : ",roll)
print("Name : ",name)
print("English Marks : ",eng_mks)
print("Maths Marks : ",maths_mks)
print("Hindi Marks : ",hindi_mks)
print("Total : ",total)
print("Percentage of student is ",percentage,"%")
print("Grade : ",grade)