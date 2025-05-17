text = "Lorem ipsum dolor sit amet consectetur adipiscing elit Integer porttitor bibendum nisi ut convallis ante"

num_longes_word = 0
words = text.split()
for word in words:
    if len(word)>5:
        num_longes_word += 1
print(f"the number word more than 5 is {num_longes_word}")
