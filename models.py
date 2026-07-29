
from __future__ import annotations
from dataclasses import dataclass, asdict


@dataclass
class Student:
    student_id: int
    name: str
    age: int
    course: str
    email: str
    marks: float = 0.0

    def to_dict(self) -> dict:
        return asdict(self)

    @staticmethod
    def from_dict(data: dict) -> "Student":
        return Student(
            student_id=int(data["student_id"]),
            name=data["name"],
            age=int(data["age"]),
            course=data["course"],
            email=data["email"],
            marks=float(data.get("marks", 0.0)),
        )