card_number = [4, 5, 6, 1, 2, 6, 1, 2, 1, 2, 3, 4, 5, 4, 6, 4]
i = 0
k = 0
for i in range(8):
    card_number[k] *= 2
    if card_number[k] > 9:
        card_number[k] = card_number[k] - 9
    k = k+2
if sum(card_number)%10 == 0:
    print("Yes")
else:
    print("No")
