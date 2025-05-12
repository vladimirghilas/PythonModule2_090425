import math

def distance(xa, ya, xb, yb, xc, yc):
    AB = math.sqrt((xa - xb) ** 2 + (ya - yb) ** 2)
    BC = math.sqrt((xb - xc) ** 2 + (yb - yc) ** 2)
    AC = math.sqrt((xa - xc) ** 2 + (ya - yc) ** 2)
    my_dict = {"AB": AB,"BC": BC, "AC": AC}
    min_key = min(my_dict, key = my_dict.get)
    return min_key


print(distance(2, 4, 2, 9, 5, 7))
