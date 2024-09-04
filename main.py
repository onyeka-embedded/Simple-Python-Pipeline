from logics import CalculateCgpa


def main():
    courses = []
    student_name = input("Enter the student's name: ")

    while True:
        name = input("Enter course name (or 'done' to finish): ")
        if name.lower() == "done":
            break
        grade = input(f"Enter grade for {name} (A-F): ").upper()
        credit = int(input(f"Enter credit unit for {name}: "))

        courses.append({"name": name, "grade": grade, "credit": credit})

    cgpa = CalculateCgpa(courses)
    print(f"\n{student_name}, your CGPA is: {cgpa:.2f}")


if __name__ == "__main__":
    main()
