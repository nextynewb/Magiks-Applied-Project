"""
Exercise (1): Advanced Student Data Manipulation

1. Print the name of each student who has graduated.
   - Iterate through the list and check the 'graduated' key.
   - Print the names of students where 'graduated' is True.

2. Calculate student total credits:
    - Calculate the total credits for each student based on their courses.
    - Add the total credits as a new key-value pair ('total_credits') to each student's data.


3. Add "Coding Club" to extracurricular_activities for non-graduated students.
   - If a student has not graduated, append "Coding Club" to their extracurricular_activities list.

4. Filter students joined Chess Club:


Instructions:
- Try solving the exercise on your own first.
- Use clear and concise code following Python best practices.
- The solution can be found at '004_solutions.py' and is only 12 lines long.
"""
students = [
    {
        "name": "Ahmad Faizal",
        "age": 21,
        "courses": {
            "Mathematics": {"grade": "A", "credits": 3},
            "Physics": {"grade": "B", "credits": 4},
            "History": {"grade": "A-", "credits": 2}
        },
        "extracurricular_activities": ["Debate Club", "Soccer"],
        "graduated": False
    },
    {
        "name": "Nur Aisyah",
        "age": 22,
        "courses": {
            "Mathematics": {"grade": "B+", "credits": 3},
            "Chemistry": {"grade": "A", "credits": 4},
            "Literature": {"grade": "A-", "credits": 2}
        },
        "extracurricular_activities": ["Drama Club", "Volunteering"],
        "graduated": False
    },
    {
        "name": "Mohan Raj",
        "age": 20,
        "courses": {
            "Biology": {"grade": "B", "credits": 4},
            "Physics": {"grade": "A-", "credits": 4},
            "Mathematics": {"grade": "A", "credits": 3}
        },
        "extracurricular_activities": ["Chess Club", "Basketball"],
        "graduated": True
    }
]


"""
(1): Print the name of the student who have graduated
"""
for student in students:
    print(student["name"])


"""
(2): Calculate total credits for each of the student and store the value
"""
for student in students:
    total_credits = 0
    for key, value in student["courses"].items():
        credits = value['credits']
        total_credits = total_credits+credits
    student['total_credits'] = total_credits
    

"""
(3): Add Coding Club to extracurricular_activities for non-graduated students
"""
for student in students:
    if student['graduated'] == False:
        student['extracurricular_activities'].append('Coding Club')
    

"""
(4): Filter students joined Chess Club
"""
for student in students:
    if 'Chess Club' in student['extracurricular_activities']:
        print(student['name'])
