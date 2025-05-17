# У вас есть список словарей, представляющих студентов с их именами и средними баллами.
# Вам нужно отфильтровать студентов, чей средний балл выше 4.5,
# и округлить средний балл оставшихся студентов до двух знаков после запятой.

students = [
    {'name': 'Alice', 'grade': 4.8},
    {'name': 'Bob', 'grade': 3.9},
    {'name': 'Charlie', 'grade': 4.65},
    {'name': 'David', 'grade': 4.2},
    {'name': 'Eve', 'grade': 4.91}
]
def sorted_grade(student):
    return student['grade']
best_student=[]
for student in students:
    if student["grade"] > 4.5:
        best_student.append(student)
best_student1 = sorted(best_student, key = sorted_grade)
print(best_student1)

best_student1 = sorted(filter(lambda student: student["grade"] > 4.5, students), key = sorted_grade)
print(best_student1)

