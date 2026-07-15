# simple students marks calculator using functions and lists
def name():
    name = input("Enter students name:")
    print("Student name is:", name)
    return name

def get_marks():
    maths= float(input("Enter marks in maths:"))
    history= float(input("Enter marks in history:"))
    marathi= float(input("Enter marks in marathi:"))
    hindi= float(input("Enter marks in hindi:"))
    return maths,history,marathi,hindi

def calculate_percentage(maths,history,marathi,hindi):
    total_percentage = (maths+history+marathi+hindi)/400 *100
    print("Total Percentage is:", total_percentage)
    return total_percentage

def calculate_avg(maths,history,marathi,hindi):
    avg = (maths+history+marathi+hindi)/4
    print("average marks is:",avg)
    return avg

def calculate_grade(total_percentage):
    if total_percentage >= 90:
        print("The grade is A")
    elif total_percentage >= 80:
       print("The grade is B")
    elif total_percentage >= 70:
       print("The grade is C")
    elif total_percentage >= 60:
        print("The grade is D")
    else:
        print("The grade is F")


name = name()
marks = get_marks()
percentage = calculate_percentage(marks[0], marks[1], marks[2], marks[3])
avg = calculate_avg(marks[0], marks[1], marks[2], marks[3])
grade = calculate_grade(percentage)