my_money = int(input("enter quantity of your money "))
product_cost = int(input("enter product cost "))
c = my_money - product_cost
if c >= 0:
    print(f"rest {c}")
else:
    print("No enough money")
