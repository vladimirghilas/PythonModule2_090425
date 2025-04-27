seconds= int(input('input seconds:'))

seconds1= seconds%60
minutes= seconds//60%60
hours = seconds//3600%24
days=seconds//3600//24
print("seconds:",seconds1)
print("minutes",minutes)
print("hours:",hours)
print("days:",days)
