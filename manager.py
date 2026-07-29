
from __future__ import annotations
from models import Student
from repository import StudentRepository
from exceptions import DuplicateStudentError, StudentNotFoundError


class StudentManager:

    def __init__(self, repository: StudentRepository):
        self.repository = repository
        self.students: list[Student] = self.repository.load_all()

    def _find_index(self, student_id: int) -> int:
        for i, s in enumerate(self.students):
            if s.student_id == student_id:
                return i
        raise StudentNotFoundError(f"No student with ID {student_id}")

    def add_student(self, student: Student) -> None:
        if any(s.student_id == student.student_id for s in self.students):
            raise DuplicateStudentError(f"Student ID {student.student_id} already exists")
        if not student.name.strip():
            raise ValueError("Name cannot be empty")
        if student.age <= 0:
            raise ValueError("Age must be positive")
        self.students.append(student)
        self._persist()

    def update_student(self, student_id: int, **fields) -> Student:
        idx = self._find_index(student_id)
        current = self.students[idx]
        updated = Student(
            student_id=current.student_id,
            name=fields.get("name", current.name),
            age=fields.get("age", current.age),
            course=fields.get("course", current.course),
            email=fields.get("email", current.email),
            marks=fields.get("marks", current.marks),
        )
        self.students[idx] = updated
        self._persist()
        return updated

    def delete_student(self, student_id: int) -> None:
        idx = self._find_index(student_id)
        del self.students[idx]
        self._persist()

    def get_student(self, student_id: int) -> Student:
        return self.students[self._find_index(student_id)]

    def list_students(self) -> list[Student]:
        return sorted(self.students, key=lambda s: s.student_id)

    def search_by_name(self, keyword: str) -> list[Student]:
        keyword = keyword.lower()
        return [s for s in self.students if keyword in s.name.lower()]

    def _persist(self) -> None:
        self.repository.save_all(self.students)