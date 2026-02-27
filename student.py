# Student Management System
# Simple project for managing student records

students = []

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    course = input("Enter course: ")

    student = {
        "name": name,
        "roll": roll,
        "course": course
    }

    students.append(student)
    print("Student added successfully.\n")


def view_students():
    if len(students) == 0:
        print("No students found.\n")
        return

    print("\nStudent List:")
    for s in students:
        print("Name:", s["name"])
        print("Roll:", s["roll"])
        print("Course:", s["course"])
        print("-----")
    print()


def delete_student():
    roll = input("Enter roll number to delete: ")

    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            print("Student deleted successfully.\n")
            return

    print("Student not found.\n")


def menu():
    while True:
        print("Student Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Delete Student")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            delete_student()

        elif choice == "4":
            print("Exiting program.")
            break

        else:
            print("Invalid choice.\n")


menu()