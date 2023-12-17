
# Simple Management System.
# Add, retrieve, update, and delete student records
# Each student's records should include the following information:
# Student's name(String), Student's age(Integer), Student's courses(A List of Strings), Student's grades(A dictionary where the keys are course names and the corresponding grades)

student_profile = {}


# adding students to the lms


def student_add():
    student_name = input("Enter your name: ")
    ask_student_ID = int(input("Enter your student ID: "))
    student_age = int(input("Enter your age: "))
    student_courses = {}
    student_courses = input("State the courses you've offered so far: ")
    student_grades = input("State your grades for the above courses:")
    student_profile[ask_student_ID] = {'Student Name': student_name, 'Student Courses': student_courses, 'Student Age': student_age, 'Student Grades': student_grades}
    print(f"Student {student_name} with student ID {ask_student_ID} added")


student_add()
print(student_profile)

# adding students to a course


def add_student_to_course():
    ask_student_ID = int(input("Enter your student ID: "))
    if ask_student_ID in student_profile:
        student_courses = input("Enter course name: ")
        student_profile[ask_student_ID][student_courses].append(student_profile)
        print(f"Student {student_profile[ask_student_ID]['student_name']} has selected {student_courses}.")
    else:
        print("ERROR. Student not found.")


add_student_to_course()
print(student_profile)

# Grade point calculation


def calculate_grade_points(student_grades):
    ask_student_ID = int(input("Enter your student ID: "))
    if ask_student_ID in student_profile:
        student_grades = {"A+": 4.0, "A": 4.0, "A-": 3.7, "B+": 3.3, "B": 3.0,
                          "B-": 2.7, "C+": 2.3, "C": 2.0, "C-": 1.7, "D": 1.0, "F": 0.0}
        return student_grades.get(student_grades, 0)
    else:
        print("ERROR. Student not found.")


calculate_grade_points(student_grades)

# CGPA Calculation


def CGPA_calculation(ask_student_ID):
    ask_student_ID = int(input("Enter your student ID: "))
    if ask_student_ID in student_profile:
        student_courses = student_profile[ask_student_ID]['student_courses']
        total_points = 0
        total_credits = 0
        for student_courses, student_grades in student_courses.items():
            # You can modify this to reflect the actual credit hours for each course.
            credit_hours = 3
            grade_points = calculate_grade_points(student_grades)
            total_points += grade_points * credit_hours
            total_credits += credit_hours
        if total_credits == 0:
            return 0
        CGPA = total_points / total_credits
        return CGPA
    return None


CGPA_calculation(ask_student_ID)

# updating the lms dictionary


def student_profile_update():
    ask_student_ID = int(input("Enter your student ID: "))
    if ask_student_ID in student_profile:
        student_name = input(
            "Enter new student name(You can press Enter to maintain name)")
        if student_name:
            student_profile[ask_student_ID]['student_name'] = student_name
        print(
            f"Student {student_profile[ask_student_ID]['student_name']}'s information updated")
    else:
        print("ERROR. Student not found.")


student_profile_update()
print(student_profile)


# deletion of student records
def student_deletion():
    ask_student_ID = int(input("Enter your student ID: "))
    if ask_student_ID in student_profile:
        student_name = student_profile[ask_student_ID][student_name]
        del student_profile[ask_student_ID]
        print(
            f"Student {student_name} with ID {ask_student_ID} has been deleted")
    else:
        print("ERROR. Student not found.")


student_deletion()
print(student_profile)

# display student information


def display_info():
    ask_student_ID = int(input("Enter your student ID: "))
    if ask_student_ID in student_profile:
        info = student_profile[ask_student_ID]
        print(f"Student ID: {ask_student_ID}")
        print(f"info: {info[student_profile]}")
        print("Courses offered: ")
        for student_courses, student_grades in info[student_courses].items():
            print(
                f"Course offered: {student_courses}, Grade: {student_grades}")
        cgpa = CGPA_calculation(ask_student_ID)
        if cgpa is not None:
            print(f"CGPA: {cgpa:.2f}")
    else:
        print("ERROR. Student not found.")


display_info()

# While Loop to display menu
while True:
    print("\nMenu:")
    print("1. Enroll a student in a course")
    print("2. Add a new student")
    print("3. Update student information")
    print("4. Delete a student")
    print("5. Display student information")
    print("6. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_student_to_course()
    elif choice == '2':
        student_add()
    elif choice == '3':
        student_profile_update()
    elif choice == '4':
        student_deletion()
    elif choice == '5':
        display_info()
    elif choice == '6':
        print("Exiting the LMS.")
        break
    else:
        print("Invalid choice. Please try again.")
