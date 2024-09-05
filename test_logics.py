import pytest
from logics import CalculateCgpa


def test_calculate_cgpa():
    # Test 1: Normal case
    course_grades = [
        {"name": "Math", "grade": "A", "credit": 3},
        {"name": "English", "grade": "B", "credit": 2},
        {"name": "Physics", "grade": "C", "credit": 4},
    ]
    assert CalculateCgpa(course_grades) == pytest.approx(3.89, rel=1e-2)

    # Test 2: All courses with the same grade
    course_grades = [
        {"name": "Math", "grade": "B", "credit": 3},
        {"name": "English", "grade": "B", "credit": 3},
        {"name": "Physics", "grade": "B", "credit": 3},
    ]
    assert CalculateCgpa(course_grades) == pytest.approx(4.0, rel=1e-2)

    # Test 3: Zero credit units
    course_grades = [
        {"name": "Math", "grade": "A", "credit": 0},
        {"name": "English", "grade": "B", "credit": 0},
    ]
    assert CalculateCgpa(course_grades) == 0.0

    # Test 4: Empty list of courses
    course_grades = []
    assert CalculateCgpa(course_grades) == 0.0

    # Test 5: Mixed grades and credit units
    course_grades = [
        {"name": "Math", "grade": "A", "credit": 2},
        {"name": "English", "grade": "C", "credit": 4},
        {"name": "Biology", "grade": "B", "credit": 3},
    ]
    assert CalculateCgpa(course_grades) == pytest.approx(3.78, rel=1e-2)

    # Test 6: Invalid grade in one course (should not affect other valid courses)
    course_grades = [
        {"name": "Math", "grade": "A", "credit": 2},
        {"name": "English", "grade": "Z", "credit": 3},  # Invalid grade
        {"name": "Biology", "grade": "B", "credit": 3},
    ]
    assert CalculateCgpa(course_grades) == pytest.approx(4.40, rel=1e-2)
