data = {"peter": 60, "Sam" : 75, "Rolf": 90 }

def average_grade(data):
    grades = data.values()
    return sum(grades) / len(grades)

print(average_grade(data))

print(data.values())

student_list = {"peter": 60, "Sam": 75, "Rolf": 90 }

def average_grade_all_students(student_list):
    total = 0
    count = 0
    for student in student_list:
        total += sum(student['grades'])


    return total / count

print(average_grade_all_students(student_list))