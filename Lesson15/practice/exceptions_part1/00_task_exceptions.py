from pathlib import Path

# Задача: Найти сумму всех чисел в файле 'numbers.txt', пропустив все нечисловые значения.

path = Path('data') / 'numbers.txt'

with open(path, 'r', encoding='UTF-8') as f:
    # Находим сумму всех чисел в файле
    s = 0
    for line in f:
        try:
            s += int(line)
        except ValueError:
            pass
<<<<<<< HEAD

=======
>>>>>>> cfc7a9b39710a1b574d089247f0f41f4336dc744

print(s)
