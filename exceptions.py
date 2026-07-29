 
class DuplicateStudentError(Exception):
    """Raised when trying to add a student ID that already exists."""
    pass
 
 
class StudentNotFoundError(Exception):
    """Raised when looking up/updating/deleting an ID that doesn't exist."""
    pass