text = "В теории, теория и практика неразделимы. На практике это не так."
vowels = "ауоыэяюёие"
count = 0
for el in text:
    if el in vowels:
        count += 1
print(count, "vowels")