from student import Student
students = []
def show_menu():
    print("==============================")
    print(" Student Management System")
    print("==============================")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Show Topper")
    print("7. Exit")


def find_student_by_rollno(rollno):
    for student in students:
        if student.rollno == rollno:
            return student
    return None

def read_marks():
    try:
        marks = int(input("Enter marks: "))
    except ValueError:
        print("Marks must be a number.")
        return None

    if not Student.is_valid_marks(marks):
        print("Marks should be between 0 and 100.")
        return None
    return marks


def add_student():
    rollno = input("Enter roll number: ").strip()

    if not rollno:
        print("Roll number cannot be empty.")
        return

    if find_student_by_rollno(rollno):
        print("Roll Number must be unique.")
        return

    name = input("Enter name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    marks = read_marks()
    if marks is None:
        return

    students.append(Student(rollno, name, marks))
    print("Student Added Successfully")

def view_students():
    if not students:
        print("No student records found.")
        return

    for student in students:
        student.display_details()

    print(f"Total Students: {Student.get_total_students()}")

def search_student():
    rollno = input("Enter roll number to search: ").strip()
    student = find_student_by_rollno(rollno)

    if student:
        student.display_details()
    else:
        print("Student Not Found")

def update_marks():
    rollno = input("Enter roll number to update marks: ").strip()
    student = find_student_by_rollno(rollno)

    if not student:
        print("Student Not Found")
        return

    marks = read_marks()
    if marks is None:
        return

    student.update_marks(marks)
    print("Marks Updated Successfully")


def delete_student():
    rollno = input("Enter roll number to delete: ").strip()
    student = find_student_by_rollno(rollno)

    if not student:
        print("Student Not Found")
        return

    students.remove(student)
    Student.total_students -= 1
    print("Student Deleted Successfully")


def show_topper():
    if not students:
        print("No student records found.")
        return

    topper = max(students, key=lambda s: s.marks)
    print("=" * 40)
    print("Topper of the Class:")
    topper.display_details()
    print("=" * 40)


def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_marks()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            show_topper()
        elif choice == "7":
            print("Thank you for using Student Management System!")
            break
        else:
            print("Invalid choice. Please try again.")
        print()


if __name__ == "__main__":
    main()
        



