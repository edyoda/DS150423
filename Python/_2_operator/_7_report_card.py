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

print("Roll No. : ",roll)
print("Name : ",name)
print("English Marks : ",eng_mks)
print("Maths Marks : ",maths_mks)
print("Hindi Marks : ",hindi_mks)
print("Total : ",total)
print("Percentage of student is ",percentage,"%")