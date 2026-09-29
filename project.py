
students = []
def add_student():
    print("\n----- Add Student Details -----")

    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")

    marks1 = float(input("Enter marks of subject 1: "))
    marks2 = float(input("Enter marks of Subject 2: "))
    marks3 = float(input("Enter marks of Subject 3: "))
    marks4 = float(input("Enter marks of Subject 4: "))
    marks5 = float(input("Enter marks of Subject 5: "))

    
    total = marks1 + marks2 + marks3 + marks4 + marks5
    percentage = total/5
   
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    elif percentage >= 40:
        grade = "E"
    else:
        grade = "F"

    if marks1 >= 33 and marks2 >= 33 and marks3 >= 33 and marks4 >= 33 and marks5 >= 33:
        result = "Pass"
    else:
        result = "Fail"

    student = {
        "name":  name,
        "roll_no": roll_no,
        "marks1":marks1,
        "marks2":marks2,
        "marks3":marks3,
        "marks4":marks4,
        "marks5":marks5,
       "total":total,
        "percentage":percentage,
        "grade":grade,
       "result":result
    }

    students.append(student)

    print("\nStudent added successfully!")  


# 2. Calculate Total Marks

def calculate_total():
    print("\n----- Calculate Total Marks -----")

    if len(students) == 0:
        print("No student records available.")
        return

    for student in students:
        print("Name:", student["name"])
        print("Total Marks:", student["total"])
        print("------------------------")

# 3. Calculate Percentage
def calculate_percentage():
    print("\n----- Calculate Percentage -----")

    if len(students) == 0:
        print("No student records available.")
        return

    for student in students:
        print("Name:", student["name"])
        print("Percentage:", round(student["percentage"], 2), "%")
        print("------------------------")


# 4. Assign Grades
def assign_grade():
    print("\n----- Student Grades -----")

    if len(students) == 0:
        print("No student records available.")
        return

    for student in students:
        print("Name:", student["name"])
        print("Grade:", student["grade"])
        print("------------------------")


# 5. Check Pass/Fail
def check_pass_fail():
    print("\n----- Pass / Fail -----")

    if len(students) == 0:
        print("No student records available.")
        return

    for student in students:
        print("Name:", student["name"])
        print("Result:", student["result"])
        print("------------------------")


# 6. Display Student Details
def display_students():
    print("\n----- Student Details -----")

    if len(students) == 0:
        print("No student records available.")
        return

    for student in students:
        print("\nName       :", student["name"])
        print("Roll No    :", student["roll_no"])
        print("Subject 1  :", student["marks1"])
        print("Subject 2  :", student["marks2"])
        print("Subject 3  :", student["marks3"])
        print("Subject 4  :", student["marks4"]) 
        print("Subject 5  :", student["marks5"])
        print("Total      :", student["total"])
        print("Percentage :", round(student["percentage"], 2), "%")
        print("Grade      :", student["grade"])
        print("Result     :", student["result"])
        print("------------------------")


# 7. Find Topper
def find_topper():
    print("\n----- Topper -----")

    if len(students) == 0:
        print("No student records available.")
        return

    topper = students[0]

    for student in students:
        if student["total"] > topper["total"]:
            topper = student

    print("Name       :", topper["name"])
    print("Roll No    :", topper["roll_no"])
    print("Total      :", topper["total"])
    print("Percentage :", round(topper["percentage"], 2), "%")
    print("Grade      :", topper["grade"])


# 8. Display Passed Students
def display_passed():
    print("\n----- Passed Students -----")

    found = False

    for student in students:
        if student["result"] == "Pass":
            print(
                "Name:", student["name"],
                "| Roll No:", student["roll_no"],
                "| Percentage:", round(student["percentage"], 2), "%"
            )
            found = True

    if found == False:
        print("No student has passed.")


# 9. Display Failed Students
def display_failed():
    print("\n----- Failed Students -----")

    found = False

    for student in students:
        if student["result"] == "Fail":
            print(
                "Name:", student["name"],
                "| Roll No:", student["roll_no"],
                "| Percentage:", round(student["percentage"], 2), "%"
            )
            found = True

    if found == False:
        print("No student has failed")
              
# ==========================================
# MAIN MENU
# ==========================================

while True:

    print("\n                        ======================================")
    print("                               STUDENT MANAGEMENT SYSTEM")
    print("                          ======================================")

    print("1. Add Student Details")
    print("2. Calculate Total Marks")
    print("3. Calculate Percentage")
    print("4. Assign Grades")
    print("5. Check Pass/Fail")
    print("6. Display Student Details")
    print("7. Find Topper")
    print("8. Display Students Who Passed")
    print("9. Display Students Who Failed")
    print("10. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        calculate_total()

    elif choice == "3":
        calculate_percentage()

    elif choice == "4":
        assign_grade()

    elif choice == "5":
        check_pass_fail()

    elif choice == "6":
        display_students()

    elif choice == "7":
        find_topper()

    elif choice == "8":
        display_passed()

    elif choice == "9":
        display_failed()

    elif choice == "10":
        print("\nProgram exited successfully.")
        break

    else:
        print("\nInvalid choice! Please enter 1 to 10.")