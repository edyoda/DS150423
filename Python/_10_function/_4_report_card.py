def student_info():
    roll = input("Enter roll_no of student : ")
    name = input("Enter the name of student : ")
    return roll, name

def marks():
    eng_mks = float(input ("Enter english marks : "))
    maths_mks = float(input ("Enter maths marks : "))
    hindi_mks = float(input("Enter hindi marks : "))
    return eng_mks, maths_mks, hindi_mks

def calculation(english, maths, hindi):
    total = english+maths+hindi
    percentage = (total/300)*100
    return total, percentage

def grade(percentage):
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
    
    return grade

def display():
    Rollno, Name = student_info()
    English, Hindi, Maths = marks()
    Total, Percentage = calculation(English, Hindi, Maths)
    Grade = grade(Percentage)
    print("Roll No. : ",Rollno)
    print("Name : ",Name)
    print("English Marks : ",English)
    print("Maths Marks : ",Maths)
    print("Hindi Marks : ",Hindi)
    print("Total : ",Total)
    print("Percentage of student is ",Percentage,"%")
    print("Grade : ",Grade)


display()