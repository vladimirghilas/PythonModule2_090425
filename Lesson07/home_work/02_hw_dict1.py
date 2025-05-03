# Данные о сотрудниках в программе хранятся в словаре
staff = [
    {
        'name': 'Алексей',
        'surname': 'Петров',
        'salary': 124300
    },
    {
        'name': 'Николай',
        'surname': 'Петров',
        'salary': 120000
    },
    {
        'name': 'Иван',
        'surname': 'Павлов',
        'salary': 34500
    },
    {
        'name': 'Василий',
        'surname': 'Кукушкин',
        'salary': 162500
    },
    {
        'name': 'Василий',
        'surname': 'Павлов',
        'salary': 47800
    },
]
# Вычислите:
print("Имя и Фамилию сотрудника с самой высокой зарплатой:")
max_salary = 0
# dict1 = 0
# dict = 0
key = "salary"
for dict in staff:
    if dict[key] > max_salary:
        max_salary = dict[key]
        dict1 = dict
print(dict1["name"], dict1["surname"])

print("Имя и Фамилию сотрудника с самой низкой зарплатой:")

min_salary = 124300
# dict1 = 0
# dict = 0
# key = "salary"
for dict in staff:
    if dict[key] < min_salary:
        min_salary = dict[key]
        dict1 = dict
print(dict1["name"], dict1["surname"])

print("Среднеарифметическую зарплату всех сотрудников")
medium_salary = 0
# dict = 0
# key = "salary"
for dict in staff:
    medium_salary += dict[key] / len(staff)
print(medium_salary)

print("Количество однофамильцев в организации")

same_surname = {}
for person in staff:
    surname = person["surname"]
    if surname in same_surname:
        same_surname[surname] += 1
    else:
        same_surname[surname] = 1
for surname in same_surname:
    if same_surname[surname] > 1:
        print(same_surname[surname], surname)

print("*Список всех сотрудников(Имя и Фамилию) в порядке возрастания их зарплаты")

sorted_by_salary = {}

sorted_by_salary = sorted(staff, key=lambda person: person["salary"])
for person in sorted_by_salary:
    print(f'{person["name"]}'
          f'{person["surname"]}'
          f'{person["salary"]}')
