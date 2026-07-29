# Student Management System

A console-based CRUD application built in Python to manage student records, with JSON as the primary storage and CSV import/export support.

# Features

**Create** — add new student records with validation (no empty names, no duplicate IDs, positive age)
**Read** — view all students (sorted by ID) or search by name (case-insensitive, partial match)
**Update** — edit any field of an existing student without retyping the rest
**Delete** — remove a student record by ID
**CSV support** — export all records to CSV, or bulk-import students from a CSV file (duplicate rows are skipped, not fatal)

# Project Structure

This project follows separation of concerns — each file has exactly one responsibility

student_management_system/
├── models.py       # Student data model (dataclass)
├── exceptions.py   # Custom exceptions (DuplicateStudentError, StudentNotFoundError)
├── repository.py   # Persistence layer — JSON/CSV read & write only
├── manager.py       # Business logic — CRUD operations, validation rules
└── main.py           # CLI entry point — user interaction only

# Tech Stack

- Python 3.9+
- Standard library only — `dataclasses`, `json`, `csv`, `pathlib` (no external dependencies)

