text = "мама мыаааал рАму"
vowels = "ауоыэяюёие"
cant = 0
for leters in text.lower():
    if leters in vowels:
        cant +=1
print(cant)

