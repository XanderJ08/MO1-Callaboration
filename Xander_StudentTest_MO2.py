# Name: Xander
# File Name: Xander_StudentTest_MO2.py
# This app will allow the user to input a student and 
# see if they made the honor roll or dean's list. 

# asking for last name
while True:
    # Allowing user to exit if they want to
    print("\nIf you would like to quit the app, please enter ZZZ.")
    # Asking for last name
    last_name = str(input("Please enter the student's last name: "))
    if last_name == 'ZZZ' or last_name == 'zzz':
        break
    # Asking for first name
    first_name = str(input("\nPlease enter the student's first name: "))
    # Asking for GPA
    student_gpa = float(input("\nPlease enter the student's gpa: "))
    # Setting up the if statements
    if student_gpa >= 3.25:
        print(f"{first_name} {last_name} has made the Honor Roll!")
    if student_gpa >= 3.25 and student_gpa >= 3.5:
        print(f"{first_name} {last_name} has made the Dean's list!")
    elif student_gpa < 3.25:
        print(f"{first_name} {last_name} has made neither the Honor Roll or the Dean's list.")
   