

from __future__ import annotations
import csv
import json
from pathlib import Path

from models import Student


class StudentRepository:
    """Handles reading/writing student records to disk (JSON or CSV)."""

    def __init__(self, filepath: str = "students.json"):
        self.filepath = Path(filepath)
        if not self.filepath.exists():
            self._write_json([])

    # ---- JSON (default storage) ----
    def _read_json(self) -> list[dict]:
        try:
            with self.filepath.open("r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def _write_json(self, records: list[dict]) -> None:
        with self.filepath.open("w", encoding="utf-8") as f:
            json.dump(records, f, indent=4)

    def load_all(self) -> list[Student]:
        return [Student.from_dict(r) for r in self._read_json()]

    def save_all(self, students: list[Student]) -> None:
        self._write_json([s.to_dict() for s in students])

    # ---- CSV import/export ----
    def export_csv(self, students: list[Student], csv_path: str = "students.csv") -> None:
        fieldnames = ["student_id", "name", "age", "course", "email", "marks"]
        with open(csv_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for s in students:
                writer.writerow(s.to_dict())

    def import_csv(self, csv_path: str) -> list[Student]:
        students = []
        with open(csv_path, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                students.append(Student.from_dict(row))
        return students