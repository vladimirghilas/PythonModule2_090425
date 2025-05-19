# Анаграммы*
# Дан список слов. Найти в нем все анаграммы (слова, составленные из одних и тех же букв).
from collections import Counter

words = []
sorted_words = [''.join(sorted(word)) for word in words]

word_counter = Counter(words)
duplicate = [word for word, count in word_counter.items() if count > 1]

print(duplicate)

#Vladimir Ghilas
