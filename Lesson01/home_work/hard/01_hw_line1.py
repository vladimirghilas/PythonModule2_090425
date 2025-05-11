sec = int(input("введите количество секунд"))
s = 165%60
second = sec%60
minutes = sec%3600//60
hours = sec//3600%24
days = sec//3600//24

print(f"days:{days},hours:{hours}, minutes: {minutes}, second: {second}")