# Convert letter grade to grade points.
def grade_to_points(grade):
    grade = grade.upper()
    if grade == "A":
        return 5.0
    elif grade == "B":
        return 4.0
    elif grade == "C":
        return 3.0
    elif grade == "D":
        return 2.0
    elif grade == "E":
        return 1.0
    elif grade == "F":
        return 0.0
    else:
        return None


# Calculate CGPA based on courses taken."""
def CalculateCgpa(courses):
    total_points = 0.0
    total_credits = 0

    for course in courses:
        grade_points = grade_to_points(course["grade"])
        if grade_points is not None:
            total_points += grade_points * course["credit"]
            total_credits += course["credit"]
        else:
            print(
                f"Invalid grade '{course['grade']}' entered for course {course['name']}."
            )

    if total_credits == 0:
        return 0.0  # To avoid division by zero

    return total_points / total_credits
