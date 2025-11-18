# "Наивысшая оценка"
#
# Дан список кортежей, где каждый кортеж представляет собой пару (имя, оценка).
# Необходимо найти имя с наивысшей оценкой.
# Если наивысших оценок несколько, вывести имена

students = [('Alice', 85), ('Bob', 92), ('Charlie', 78), ('David', 92)]
# Ожидаемый результат: 'Bob' и 'David
max_score = max(score for name, score in students)

best_students = [name for name, score in students if score == max_score]

print(best_students)