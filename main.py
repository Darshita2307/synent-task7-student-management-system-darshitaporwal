"""
main.py
==========
CLI entry point.
This is the file to run: 'python main.py'
Only responsible for talking to a human and calling StudentManager -
no file I/O, no validation logic.
"""

from models import Student
from repository import StudentRepository 
from manager import StudentManager
from exceptions import DuplicateStudentError, StudentNotFoundError

MENU="""
==========  Student Management System =========
1. Add Student
2. Update Student
3. Delete Student
4. View All Student
5. Search Student by Name
6. Export to CSV 
7. Import to CSV
0. Exit
"""

def print_student(s: Student)-> None:
    print(f" [{s.student_id}] {s.name:<20} Age:{s.age:<4} Course:{s.course:<15}" 
          f"Email:{s.email:<25} Marks:{s.marks}")
def prompt_int(label : str)-> int:
    while True:
        try:
            return int(input(label))
        except ValueError:
            print("Please enter a valid number.")

def prompt_float(label:str)-> float:
    while True:
        try:
            return float(input(label))
        except ValueError:
            print("Please enter a valid number.")

def main() -> None:
    manager = StudentManager(StudentRepository("student.json"))

    while True:
        print (MENU)
        choice = input("Choose an option: ").strip()

        try:
            if choice == "1":
                sid = prompt_int("Student_ID: ")
                name = input("Name: ").strip()
                age = prompt_int("Age: ")
                course = input("Course: ").strip()
                email = input("Email: ").strip()
                marks = prompt_float("Marks: ")
                manager.add_student(Student(sid, name, age, course, email, marks))
                print("Student added successfully.")

            elif choice == "2":
                sid = prompt_int("Student ID to update: ")
                try:
                    manager.get_student(sid)   # Check if student exists
                except StudentNotFoundError:
                    print("Student not found!")
                    continue
                print("Leave a field blank to keep it unchanged.")
                updates={}
                name = input("New name: ").strip()
                if name:
                    updates["name"]=name
                age = input("New age: ").strip()
                if age:
                    updates["age"]=age
                course = input("New course: ").strip()
                if course:
                    updates["course"]= course
                email = input("New email: ").strip()
                if email:
                    updates["email"]=email
                marks = input("New marks: ").strip()
                if marks:
                    updates["marks"]=float(marks)
                manager.update_student(sid,**updates)
                print(f"Student with {sid} updated successfully.")
            elif choice == "3":
                sid = prompt_int("Enter Student ID to delete: ")
                manager.delete_student(sid)
                print(f"Student with {sid } deleted successfully.")

            elif choice == "4":
                students = manager.list_students()
                if not students:
                    print("No records found. ")
                for s in students:
                    print_student(s)

            elif choice == "5":
                keyword = input ("Enter name keyword: ").strip()
                results = manager.search_by_name(keyword)
                if not results:
                    print("No matches found.")
                for s in results:
                    print_student(s)

            elif choice == "6":
                path = input("Export CSV path [students.csv]: ").strip() or "students.csv"
                manager.repository.export_csv(manager.students, path)
                print(f"Exported to {path}")

            elif choice == "7":
                path = input("Import CSV path: ").strip()
                imported = manager.repository.import_csv(path)
                for s in imported:
                    try:
                        manager.add_student(s)
                    except DuplicateStudentError:
                        print(f"Skipped duplicate ID {s.student_id}")
                print("Import complete.")
 
            elif choice == "0":
                print("Goodbye!")
                break
 
            else:
                print("Invalid option, try again.")
 
        except (StudentNotFoundError, DuplicateStudentError, ValueError, FileNotFoundError) as e:
            print(f"Error: {e}")
 
 
if __name__ == "__main__":
    main()