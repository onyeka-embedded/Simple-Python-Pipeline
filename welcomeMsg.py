def display_instructions():
    instructions = """
    Welcome to the CGPA Calculator App!

    This tool helps you calculate your Cumulative Grade Point Average (CGPA) based on the courses you've taken, their grades, and corresponding credit units.

    Instructions:

    1. Input Your Courses:
       - For each course, provide the following details:
         - Course Name: Enter the name of the course (e.g., "Math").
         - Grade: Enter the grade you received (e.g., "A", "B", "C").
         - Credit Unit: Enter the credit unit of the course (e.g., 5, 4, 3).

    2. Grade Format:
       - Use letter grades such as "A", "B", "C", etc. The app will automatically convert these to the corresponding grade points based on the grading scale:
         - A = 5.0
         - B = 4.0
         - C = 3.0
         - D = 2.0
         - E = 1.0
         - F = 0.0

    3. Credit Units:
       - Enter the course's credit units, which represent the weight of the course in your CGPA calculation.

    4. Calculate Your CGPA:
       - Once all courses have been entered, the app will compute your CGPA and display it.

    Example:
    For a student taking the following courses:
      - Math (Grade: A, Credit Unit: 3)
      - English (Grade: B, Credit Unit: 2)
      - Physics (Grade: C, Credit Unit: 4)

    The app will calculate and display your CGPA based on these values.
    """
    print(instructions)
