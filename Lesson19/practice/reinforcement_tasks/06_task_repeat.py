# "Фильтрация списка строк"
#
#  Дан список строк.
#  Необходимо отфильтровать этот список, оставив только те строки,
#  которые содержат определенную подстроку(keyword), игнорируя регистр.

messages = ["Hello world!", "Important INFO", "debug message", "User information", "USER logged in"]
keyword = "info"
mess1 = []
for el in messages:
    if keyword.lower() in el.lower():
        mess1.append(el)
print(mess1)