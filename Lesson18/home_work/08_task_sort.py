# Телефонная база
# Отсортируйте список телефонов по возрастанию и используя сортировку выбором.
# Телефон задан в виде строки формата nn-nn-nn. Например, 23-45-67

phones = ["25-17-58", "11-34-85", "54-61-56", "34-61-72", "25-17-55", "34-56-56"]

for i in range(len(phones)):
    min_index = i
    for j in range(i + 1, len(phones)):
        if phones[j] < phones[i]:
           min_index = j
    phones[i], phones[min_index] = phones[min_index],phones[i]

for phone in phones:
    print(phone)

#Vladimir Ghilas
