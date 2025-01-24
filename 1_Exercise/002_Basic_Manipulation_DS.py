"""

Exercise (2): Advanced Employee Data Manipulation

Tasks:

1. Print the name of each employee who has been promoted.
   - Iterate through the list of employees and check the 'promoted' key.
   - Print the names of employees where 'promoted' is True.

2. Calculate the average performance score for each employee:
   - Calculate the average score based on the four quarters (Q1, Q2, Q3, Q4) for each employee.
   - Add the average score as a new key-value pair ('average_score') to each employee's data.

3. Update the skillset for employees in the "Product" department:
   - If the employee works in the "Product" department, add "Leadership" to their list of skills.

4. Filter employees based on performance:
   - Print the names and average performance scores of these high-performing employees.


Instructions:
- Try solving the exercise before looking at the solution.
- Use concise and efficient code while adhering to best Python practices.

"""

employees = [
    {
        "name": "Zara Ali",
        "age": 29,
        "department": "Marketing",
        "performance": {
            "Q1": {"score": 88, "goals_achieved": 3},
            "Q2": {"score": 92, "goals_achieved": 4},
            "Q3": {"score": 85, "goals_achieved": 2},
            "Q4": {"score": 90, "goals_achieved": 3}
        },
        "skills": ["SEO", "Social Media", "Content Marketing"],
        "promoted": False
    },
    {
        "name": "John Smith",
        "age": 35,
        "department": "Sales",
        "performance": {
            "Q1": {"score": 75, "goals_achieved": 2},
            "Q2": {"score": 78, "goals_achieved": 3},
            "Q3": {"score": 80, "goals_achieved": 3},
            "Q4": {"score": 82, "goals_achieved": 3}
        },
        "skills": ["Negotiation", "Product Knowledge", "CRM"],
        "promoted": True
    },
    {
        "name": "Eleanor Davis",
        "age": 28,
        "department": "Product",
        "performance": {
            "Q1": {"score": 95, "goals_achieved": 4},
            "Q2": {"score": 98, "goals_achieved": 5},
            "Q3": {"score": 97, "goals_achieved": 5},
            "Q4": {"score": 99, "goals_achieved": 5}
        },
        "skills": ["Product Strategy", "Market Research", "Innovation"],
        "promoted": True
    }
]

"""
(1) Print the name of each employee who has been promoted
"""
for employee in employees:
    if employee['promoted'] == True:
        print(employee['name'])

"""
(2) Calculate Average Score of each employee and store it in ['average_score']
"""
for employee in employees:
    score = []
    for key, value in employee['performance'].items():
        score.append(value["score"])
    average_score = sum(score) / len(score)
    employee['average_score'] = average_score


"""
(Extra) Calculate the average score for each quarter
"""
score = {'Q1':0,'Q2':0,'Q3':0,'Q4':0}
q1_score = []
q2_score = []
q3_score = []
q4_score = []

for employee in employees:

    for key,value in employee["performance"].items():
        if key == 'Q1':
            q1_score.append(value['score'])
        if key == 'Q2':
            q2_score.append(value['score'])
        if key == 'Q3':
            q3_score.append(value['score'])
        if key == 'Q4':
            q4_score.append(value['score'])
    average_score_q1 = sum(q1_score)/len(q1_score)
    average_score_q2 = sum(q2_score)/len(q2_score)
    average_score_q3 = sum(q3_score)/len(q3_score)
    average_score_q4 = sum(q4_score)/len(q4_score) 
score["Q1"] = average_score_q1
score["Q2"] = average_score_q2
score["Q3"] = average_score_q3
score["Q4"] = average_score_q4
print(score)
    

"""
(3) Update the skillset for employees in the "Product" department
"""
for employee in employees:
    if employee['department'] == 'Product':
        employee['skills'].append('Leadership')
    print(employees)
"""
(4) Filter employees based on performance
"""
for employee in employees:
    print(f"{employee['name']}: {employee['average_score']}")
