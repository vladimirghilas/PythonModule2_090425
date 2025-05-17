# У вас есть список цен товаров.
# Вам нужно применить скидку в 10% к каждому товару, цена которого превышает 100 единиц, и вывести новые цены.
discount_price = []
prices = [50, 120, 80, 150, 90, 200]
for el in prices:
     if el > 100:
         discount_price.append( el - el / 10)
print(discount_price)

discount_price = list(map(lambda el: el*0.9,filter(lambda el: el > 100, prices)))
print(discount_price)