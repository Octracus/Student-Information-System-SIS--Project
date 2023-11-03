# Initialize an empty dictionary to store student records.

students_data = {}


# Function to add a new student record.
def add_student():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    courses = input("Enter student courses (comma-separated): ").split(',')

    grades = {}
    for course in courses:
        grade = input(f"Enter grade for {course}: ")
        grades[course] = int(grade)

    student_record = {
        'name': name,
        'age': age,
        'courses': courses,
        'grades': grades
    }

    students_data[student_id] = student_record
    print(f"Student record for {name} has been added.")


# Function to retrieve a student record by ID.
def retrieve_student():
    student_id = input("Enter student ID to retrieve: ")
    if student_id in students_data:
        student = students_data[student_id]
        print("Student Information:")
        print(f"Name: {student['name']}")
        print(f"Age: {student['age']}")
        print("Courses:", ', '.join(student['courses']))
        print("Grades:", student['grades'])
    else:
        print("Student ID not found.")


# Function to update a student record by ID.
def update_student():
    student_id = input("Enter student ID to update: ")
    if student_id in students_data:
        student = students_data[student_id]
        print(f"Updating record for {student['name']}:")
        student['name'] = input("Enter updated name: ")
        student['age'] = int(input("Enter updated age: "))

        print("Updating courses and grades:")
        courses = input("Enter student courses (comma-separated): ").split(',')
        grades = {}
        for course in courses:
            grade = input(f"Enter updated grade for {course}: ")
            grades[course] = int(grade)
        student['courses'] = courses
        student['grades'] = grades
        print(f"Record for {student['name']} has been updated.")
    else:
        print("Student ID not found.")


# Function to delete a student record by ID.
def delete_student():
    student_id = input("Enter student ID to delete: ")
    if student_id in students_data:
        student_name = students_data[student_id]['name']
        del students_data[student_id]
        print(f"Record for {student_name} has been deleted.")
    else:
        print("Student ID not found.")


# Main program loop
while True:
    print("\nStudent Information System")
    print("1. Add Student Record")
    print("2. Retrieve Student Record")
    print("3. Update Student Record")
    print("4. Delete Student Record")
    print("5. Exit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == '1':
        add_student()
    elif choice == '2':
        retrieve_student()
    elif choice == '3':
        update_student()
    elif choice == '4':
        delete_student()
    elif choice == '5':
        print("Exiting Student Information System. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option (1/2/3/4/5).")
