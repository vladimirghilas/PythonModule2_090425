import pprint

path_in = "data/salaries.txt"
path_out = "data/highly_paid.txt"

employees = []

with open(path_in, "r", encoding="UTF-8") as file:
    file.readline()
    for line in file:
        employee_data = line.split()
        employee = {
            "surname": employee_data[0],
            "name": employee_data[1],
            "midlename": employee_data[2],
            "salary": employee_data[3],
        }
        employees.append(employee)
#pprint.pprint(employees)

#for employee in employees:
#    if int(employee["salary"]) > 60000:
#        print(employee)
with open(path_out, "w", encoding="UTF-8") as file:
    for employee in employees:
        if int(employee["salary"]) > 60000:
            file.write(" ".join(employee.values())+"\n")